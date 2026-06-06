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
<img src="https://cdn1.telesco.pe/file/VtseXT9Cb1FW5V0JVJhS9b8XwovombAMzmnokK3Rj6A-mFny1BeUut-HnzFLJuAhUk7AHk8kyOl0vy4O1b_Su-DliRTeepxLXd5opvYcbWNixmPwO7akuahsRGD27ltWFMaw5Ub_5GCJN0cehFzdM_b72e664beJAUFmphqXoV7qMToVNqeioUpXtSG3FfLTnh1Ujo5k_6hrxd0Ewh6QDKHlsf7atYZgs8_2lxtJ_kGXMtRO2cSqzMCuPSMu6vj2OesrNQzDLCcHbK9ihQLKxFAI2n6WRYZ34cyxx6HWiWg1maGig_2gt2fA68d1h1P8M7M_ijgi1GKOw1wTacWR-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 22:15:48</div>
<hr>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تسنیم،‌ منبع وابسته به سپاه:
"روابط عمومی نیروی دریایی سپاه: صدای انفجار شنیده شده از اطراف جزیره خارک مربوط به خنثی‌سازی مهمات باقی‌مانده از جنگ تحمیلی سوم در منطقه بهرگان است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/VahidOnline/75975" target="_blank">📅 22:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dJaN6hlVK3bH4LejJvRduf4huAcIFmbNZUQTbjtLFjidM8Xysby1Fmv26mIgTIoZL65Er2UHOqHFCpPAkogOU9TCYivqbnYZPPFGFT6W_xUKUlO0iqLsXWi7gj22yO7_RLvgQsEKbqbOdjN7k5jqyu0WMH-FzbkHdAQCrEFnNTRm56Rh2aafWBr2u12ZGXQzo4UEWmszXs9mTf_wAhh9YTIEiRKVodiOrv6TQGwGrhBsFlxWFi7HB7LKTSjCFNzcsm4LDulmUrn954rl9Niq7gJj0Uwdrmv8OQtPLKpst_5wMDZpq4Xrod6C71ImF4g6Ll7uMi3wcUfbozPzRR3bLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد خاتمی، عضو مجلس خبرگان، در دیدار با اعضای شورای اداری شهرستان سیرجان با اشاره به وضعیت جسمانی مجتبی خامنه‌ای، گفت: در جریان حمله روز نخست جنگ، او از ناحیه پا دچار آسیب‌دیدگی شد؛ به‌گونه‌ای که احتمال قطع پا نیز مطرح بوده، اما این اتفاق رخ نداد و او هم‌اکنون در سلامت به سر می‌برد.
این در حالی است که از روز ۹ اسفند سال ۱۴۰۴ و حمله به دفتر علی خامنه‌ای، هیچ تصویر یا فایل صوتی از مجتبی خامنه‌ای منتشر نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/VahidOnline/75974" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lJhagEHYV1gTGSpbfl37nWFcHcuXPDmxTTnun3HI5o8dnoM7LbgCzn78ciNmKURo9UMkPOHFLByaZQ9LrFjtxwu-Vj7v7McWoBDqQLiJV28l-xWwamjiCzdtwVsU3zXyH0DxWQdklSUAK1b_IY8acmpt7-JkMEK9f3WiOW91tq2ppZC6hBkFGznODZ7jwODwo-ZBSAkwQC_nYXpKzvvAksqA6F9S2glunS8KZuLRP1aNNmwMhYyDLiv6t8oXN04f4edNOBiy7duuyTeBw7TEDBD4rCmZhXh-4jS70VG_eff02ISy1g67wP3w5Jd8cCMDCI5EB0-lvzpxW2L-z8Uanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز شنبه ۱۶ خرداد ۱۴۰۵، گزارش داد محسن نقوی، وزیر کشور پاکستان، وارد تهران شده و قرار است با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار و گفت‌وگو کند.
بر اساس این گزارش، نقوی پیش از سفر به تهران با شهباز شریف، نخست‌وزیر پاکستان، دیدار کرده و در جریان این ملاقات، دستورالعمل‌هایی درباره سفر به ایران و روند رایزنی‌های مرتبط با مذاکرات جمهوری اسلامی و آمریکا دریافت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/VahidOnline/75973" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ok736ncFuTyMxXmN2haoNQDaBIoaAVSl6nlZN30rNYwgHkp9KsNoJ5uWJua2eMylhFRvfb3daUedmNkp--DoyAu8WKLHAGH01VxBCnHF4VBHaKTQJH0IpIYY4g1VJLUGTJGrsa4wfRgEkeIEbkgBE7HwxxM0TNPkM1a3n5qFpFhiiA86JtCwsTYa4-owvAYYoCk-MyHwA-9Yh-vdFiLpHxNMTBfq2SPkgJoRZIBajkLMRptGZWxDKoIuKUtGe2OyYIjOI7HbDxh_p1RWWa9WOWnOAqJ7icweuW2F4xTijymME0A0IxEkdvEC9MOBARITQDLNRJB8xqcQ8zyrzFIOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول مسعود پزشکیان، در بازدید از دانشگاه علم و صنعت گفت: در جنگ‌های اخیر شاهد مهاجرت معکوس نخبگان و مردم به کشور بودیم. باید از ظرفیت ایرانیان علاقه‌مند به خدمت به کشور استفاده کنیم و با طراحی مشوق‌های مناسب، زمینه بازگشت نخبگان و استادانان را فراهم سازیم.
او افزود: نباید دنبال این باشیم چرا استادان مهاجرت کرده‌اند، بلکه باید به بازگرداندن آنان بیندیشیم.
در روزهای اخیر، بینش بلور، معروف به قصیر، خواننده لس‌آنجلسی، با حضور در تهران در تجمع حامیان حکومت در میدان انقلاب ترانه اجرا کرد.
همچنین صدف طاهریان، بلاگر ساکن ترکیه، تمام پستهای صفحه اینستاگرام خود را حذف کرده و با انتشار استوری‌هایی، از حضور خود در ایران خبر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/VahidOnline/75972" target="_blank">📅 20:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGSSoxH8oGPybsCtiXlXOfmEQyvvRg5uycdsxlFrchDsAux9WCSZ-OE0bFNwQUfQyMWDIWvjbLLXY4h98ZmQfHy-HXyxBaCh8RHnoixeuQL_xoVr4hbP0H5yEW6m1TaykKdxISXXTUNKy-iZpXti4K49Y7W-3efKDCRcgmj4tgznl5HRq6R_9ZeT-_QDoCb10qK4t5ei4YGz5VXV8rWHxillbxd1-vh4VphGfW3G1H2BcznnuW67rxrt-vL8XBp61HWb8xQQspgGEygSarscL8LPO6QfgoRmqSAH6EDE_Si3Ub6qx_B72Fwf__R9oD035KL0Nzb_TTAWok2SesL8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی در بیانیه‌ای حمله بامداد شنبه ۱۶ خرداد ۱۴۰۵ ارتش آمریکا به تاسیسات راداری و نظارت ساحلی در منطقه سیریک و جزیره قشم را «نقض آشکار آتش‌بس» و «تجاوز نظامی علیه حاکمیت ملی و تمامیت سرزمینی ایران» خواند و آن را به شدت محکوم کرد.
در این بیانیه آمده است که تاسیسات هدف قرار گرفته، ماموریت حفاظت از امنیت مرزهای کشور و امنیت کشتیرانی در آبراه‌های بین‌المللی را بر عهده داشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/VahidOnline/75971" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jqJ_XnIGxi0beE3eDcppS1YrsJ2goTXsuSAQ25d7bSEalh7QCBqGQy5Y-yXbkyxpSp3P9kf0G39ASfDgQXafmUaNvYicMYlM9RAD9A8XvlKkk0AG5ICIv3zDvbwbCSyDlhPJBny_4C9zV1Bs-cm2NhgOJR8ih09NOSL6Tx-092le-S0uoj8tHGWN-93dsvDbAsjOOnDGZrtZ1cCXqHOzY8iqE15Id7KVFyrMPxKD883ygkgq5r-lWXFI62ILenrXXWzPhy--qJpu4YR6NPLdeC6Ytk85st_4Gk95zDDnZSKyaGyqg0XwYzEPiLNoDePulPS2SYVgZ5rYN63CvVB2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S6QV5UWQxzHbqMQMOpdxRtn98qCyv46lZwZdQUQjzd3FMvQmX_1wuGLycfm7_Qpgg4D7Q-1lgJneFuxdLy1LCuKQwwjQEG9GfgtIl5hgsFZc72kLTmz9Yn4Hap8IX3S7hdCRXpifyc7xkQB6pWGtSQXTFYnJ_TRApp4pDrZqjPNwuyNGWe-eP7ZMCNdNBVLLeg2WkR9-koua1aB_kikJuSNH7NORmhYayCS3kO0I2F3SyFLi5jUpTnNLquHLdBk3DRykyzZkgstaeLrsvtoqwGA_ao9utIWf_w0fyjq5jw21viE-1zeP_bC0n0HKqkA749h01NSKGvwut5sd6MmFSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز جمعه در شبکه ایکس در پاسخ به انتقاد صریح مقامات عالی‌رتبه لبنان تمام تقصیر را متوجه اسرائیل دانست.
نواف سلام، نخست‌وزیر لبنان، روز جمعه، ۱۵ خردادماه، در یک نشست مطبوعاتی با لحنی صریح رهبران ایران را خطاب قرار داد و گفت: «به جنوب ما رحم کنید؛ از تبدیل کردن آن و مردمش به یک برگۀ معامله دست بردارید.»
ژوزف عون، رئیس‌جمهور لبنان، نیز در مصاحبه با سی‌ان‌ان پیام مشابهی برای ایران داشت. او گفت: «اینجا کشور شما نیست، کشور ماست. مداخله در کشور ما وظیفۀ شما نیست.»
در پاسخ به این انتقادات که مقامات لبنان ماه‌هاست با صراحت مطرح می‌کنند، عراقچی در پیامی نوشت: «اگر لبنان ابزار معامله برای ایران بود، خیلی وقت پیش به توافق رسیده بودیم.»
وزیر خارجه جمهوری اسلامی در ادامه خطاب به عون نوشته است: «آقای رئیس جمهور، لبنان را از دست دشمن واقعی‌تان نجات دهید.»
عراقچی در پیام خود می‌گوید: «بر اساس گفته‌های آقای عون، هر کس باشد فکر می‌کند که ایران است که یک‌پنجم لبنان را اشغال کرده،‌ یک‌چهارم مردمش را آواره کرده و هر روز کشورش را بمباران می‌کند.»
@
VahidHeadline
ساعاتی بعد نیز اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، در پیامی به لهجه لبنانی نوشت: «بیبیع اللی واقف حدّو، وبیشتری اللی واقف ضدّو»؛ عبارتی که به معنای «کسی که کنار او ایستاده را می‌فروشد و کسی که مقابل او ایستاده را می‌خرد» است.
رئیس‌جمهوری لبنان همچنین خطاب به ایران و سپاه پاسداران گفته بود: «این کشور، کشور ماست نه کشور شما» و تاکید کرده بود که لبنانی‌ها از جنگ خسته شده‌اند و خواهان زندگی در صلح و ثبات هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/VahidOnline/75969" target="_blank">📅 19:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75968">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04b6cd8529.mp4?token=g4kfTDztT6t3WHWTPubL8eAnbdGUJQvqXWHN2pci621cQWFQFP9KbkBXmS0bfCfCNwrze9UCS6gS4B2BvJAix8G6pcf517ypDAr2pvT1A26eqQd2JfYCpDo7y7iUrMXrkEGmpN2iaNF2btCOmxe1mjd6geJHng7xK7pZ3D2mou9Wm03lcT7_zPsHc_Tos6CIse9iME2fSYlM0WhdvCMCzuaQh5U8JmXdAUkjhTqJzLmDceeLGGPTndGKVzLxeaAQWPzfA3u_pzbaSfVNDeCoK7E6wbzHfeIHxKlzePzSKdwT9gmQ3misXIxhYFvJYw89QLIQiCwmHh_GIP0lwqjDHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04b6cd8529.mp4?token=g4kfTDztT6t3WHWTPubL8eAnbdGUJQvqXWHN2pci621cQWFQFP9KbkBXmS0bfCfCNwrze9UCS6gS4B2BvJAix8G6pcf517ypDAr2pvT1A26eqQd2JfYCpDo7y7iUrMXrkEGmpN2iaNF2btCOmxe1mjd6geJHng7xK7pZ3D2mou9Wm03lcT7_zPsHc_Tos6CIse9iME2fSYlM0WhdvCMCzuaQh5U8JmXdAUkjhTqJzLmDceeLGGPTndGKVzLxeaAQWPzfA3u_pzbaSfVNDeCoK7E6wbzHfeIHxKlzePzSKdwT9gmQ3misXIxhYFvJYw89QLIQiCwmHh_GIP0lwqjDHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شماری از دانش‌آموزان اصفهان روز شنبه ۱۶ خرداد در اعتراض به حضوری برگزار شدن امتحانات تجمع کرده و با سر دادن شعار «دانش‌آموز داد بزن، حقتو فریاد بزن» خواستار تغییر نحوه برگزاری آزمون‌ها شدند.
@
VahidOOnLine
صدها دانش‌آموز روز شنبه ۱۶ خرداد در شهرهای مختلف ایران ازجمله تهران، مشهد، اصفهان، شیراز و چندین شهر دیگر تجمع اعتراضی برگزار کردند.
دانش‌آموزان در تهران مقابل دبیرخانه شورایعالی انقلاب فرهنگی و در شهرستان‌ها مقابل ساختمان وزارت آموزش و پرورش تجمع کردند.
آنها به تغییر قوانین کنکور و افزایش تاثیر معدل در کارنامه کنکور سراسری معترض هستند.
گزارش‌های غیر رسمی از حضور نیروهای انتظامی و یگان ویژه در اطراف محل تجمع دانش‌آموزان در مشهد حکایت دارد.
پیشتر هم صدها دانش‌آموز روز سه‌شنبه در شهرهای تهران، مشهد، همدان و چندین شهر دیگر با تجمع مقابل ساختمان وزارت آموزش و پرورش به تغییر قوانین کنکور و افزایش تاثیر معدل در کارنامه کنکور سراسری باتوجه به تاثیر منفی جنگ بر آمادگی آن‌ها برای آزمون ورود به دانشگاه اعتراض کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/VahidOnline/75968" target="_blank">📅 19:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLQmkQN68KbDzeUNr-YYFNMgrypUiOhX0CnoEZ6TKeV1a_JHXzuwqw2qUosc_v7OPgzkuXqO7hiyCLZUaLiQ2B2HdqyBFoDHnHC7WVmKaZWE3TvXh2lOkwIfgXx8ZP54ynL19dl6mryhAH8IgIBPdvRbkNa9LK1_tjV7k0xXffkRJsHMSH92LZw3EgFLZt1nWSpLKYKQHrymP_NrtEt0X1rwUcAuP6G1NaLOlNeIXfDwtN4WxIgBx7uc5n4O84w45ZR3_aRKDZJbYdLGSlh_0JoAY1k8mRcx8uXIVNcBK7L_ZNsaw8IDFSGSw9Nfg_W64dQniJZPs-Njk00_3Li-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«رضا کرمی» ۳۴ ساله، ساکن کرج و اصالتا اهل شهرستان طارم در استان زنجان، در تاریخ ۱۹ دی‌ماه ۱۴۰۴ با اصابت گلوله جنگی به ناحیه قلب جان خود را از دست داد.
به گفته منابع مطلع، رضا کرمی به حرفه ماساژ مشغول بود و در کنار آن به طراحی و نقاشی نیز می‌پرداخت.
خانواده او پس از ناپدید شدنش، به مدت حدود یک هفته در جست‌وجوی او بودند و به مراکز مختلف مراجعه کردند، اما اطلاعی از سرنوشتش به دست نیاوردند.
بر اساس این روایت، خانواده در نهایت پیکر او را در بهشت سکینه کرج شناسایی کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/VahidOnline/75967" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1Tt6Y_n4REH6FJNK82vlQ6560VEqmMAsqeUQe2ZUhHsKefW3wZ9jTuwPr0ovsUI17LLfPAnYInIcfXYCPU-hrTq4_N64gJcxtHED-TPw8Yh8Qwxj7EDv-UJrxa9d2zVrUi2LbdNMxTIdcY7fUN6hjxuI7IiBJ4ujI9HYdQE2XB-AdYQlyywQveMaT-ZYqJLtZcZU2ibhcIcZDN1C07s6p4HqbIJON2YclR2_x6QoL8oA5IdWGU8vqW6Oj0XjBdUGn6V_N9nG2T7sKXX_8BYmY8F9JathLBA1CBlmDIFjuDXEFihgBkeyDgqvo4d8zKJj0OGdwnsGtx6EIDQDWUYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که بازیکنان تیم ملی فوتبال ایران پس از ماه‌ها ابهام، برای حضور در جام جهانی آمریکا روادید دریافت کرده‌اند، گزارش شده است که درخواست روادید مهدی تاج، رئیس فدراسیون فوتبال ایران، رد شده است.
به گزارش نیویورک‌تایمز به نقل از چهار مقام ارشد، درخواست همهٔ ۲۶ بازیکن ایران پذیرفته شده، اما بیش از ده نفر از اعضای کادر پشتیبانی و مسئولان فدراسیون که قرار بود تیم را همراهی کنند، اجازه ورود به آمریکا نگرفته‌اند.
یکی از این مقام‌ها گفته است روادید مهدی تاج، که سابقه فرماندهی در سپاه پاسداران انقلاب اسلامی دارد، نیز رد شده است. آمریکا و کانادا سپاه پاسداران را یک نهاد تروریستی معرفی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75966" target="_blank">📅 08:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/262f970692.mp4?token=E52nEvOC4JlU0jvfgPQJ2t3_gs6omdRdiPVqMPlEI2orWlhVi8KiWH8s_6jhoaVgrUbo_vDeHVs8fpgODSOJenUOoVyME-bnY87OLSIQU-ODShFBl9gNTv9cGMr172vdDTQ1RlaN1jZNvku12MbizSfMPCkBfWjkxE9HuzWrVr9Q66UcLPBcxUQ1Icbeicy_rl6myvf2JgToNKt0o-Uc8vM94udYjcfLCQWcAVdbY0Rz64UkBIRuzx9Jwsa5YRvkfVpO_lGteE7K9v5weXq3aKshd61KPLcKI6ErWoWAeKROHKpBI193z4EK-eWdF3EKU5FdmNf9YF0U4kABFRq6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/262f970692.mp4?token=E52nEvOC4JlU0jvfgPQJ2t3_gs6omdRdiPVqMPlEI2orWlhVi8KiWH8s_6jhoaVgrUbo_vDeHVs8fpgODSOJenUOoVyME-bnY87OLSIQU-ODShFBl9gNTv9cGMr172vdDTQ1RlaN1jZNvku12MbizSfMPCkBfWjkxE9HuzWrVr9Q66UcLPBcxUQ1Icbeicy_rl6myvf2JgToNKt0o-Uc8vM94udYjcfLCQWcAVdbY0Rz64UkBIRuzx9Jwsa5YRvkfVpO_lGteE7K9v5weXq3aKshd61KPLcKI6ErWoWAeKROHKpBI193z4EK-eWdF3EKU5FdmNf9YF0U4kABFRq6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده: "نیروهای سنتکام موشک‌ها و پهپادهای پرتاب‌شده از سوی ایران را منهدم کردند"
ترجمه ماشین:
تمپا، فلوریدا — نیروهای آمریکا در تاریخ ۵ ژوئن، چندین موشک بالستیک و پهپاد ایرانی را که از سوی ایران به سمت تنگه هرمز و کشورهای همسایه در خلیج فارس پرتاب شده بودند، رهگیری کردند.
ایران چند ساعت پس از آنکه فرماندهی مرکزی آمریکا، سنتکام، چهار پهپاد تهاجمی یک‌طرفه ایرانی را که به سمت تنگه هرمز پرتاب شده بودند سرنگون کرد، هفت موشک بالستیک به سمت کویت و بحرین شلیک کرد. این پهپادهای تهاجمی تهدیدی فوری برای تردد دریایی منطقه‌ای محسوب می‌شدند. نیروهای آمریکا سپس برای دفاع در برابر حملات دریایی بیشتر، سایت‌های راداری نظارت ساحلی ایران را در گورک و جزیره قشم هدف قرار دادند.
ارزیابی‌های اولیه نشان می‌دهد شش فروند از موشک‌های پرتاب‌شده از سوی ایران رهگیری شده‌اند و موشک هفتم به هدف مورد نظر خود نرسیده است. در حال حاضر هیچ گزارشی از آسیب‌دیدن نیروهای آمریکایی وجود ندارد و ادعاهای ایران مبنی بر واردکردن خسارت به مقر ناوگان پنجم آمریکا در بحرین نادرست است.
نیروهای سنتکام همچنان هوشیار و در آمادگی کامل هستند تا در چارچوب دفاع از خود، به تجاوزات بی‌دلیل ایران پاسخ دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75965" target="_blank">📅 06:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY2wWF420IE1vY9dvDK0_7_7-N3sWjID-eTyu4IRBehvLeMQwCkBEQHEbMT1TAj2b_vHAtV3B-5epl4QYctpupY5aQWbAk0JL9GWd2TJub8Hlg7RnxlJVZ68Us_nMzXHRXIGgQsI5ZOWFFq2sMV8ZEEQObBve97p-f86R7hljV6YwPJv99WxtwAMf2iMFGxSsvnCxvBkFVsNtl45j6NWxRmZIvnip66xduHHo1tN2Fp0UaFuwGui-MF_Kl6fyH18PMiN25AZSIsVApnPgXoq_S8N4zqkhn7y9n2o3nYFkh_UyCmY6PzMQFqdvMeMG7Bq7pSrD2mSuGgDQpYDIIav-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه، بامداد شنبه، با انتشار بیانیه‌ای اعلام کرد: «به دنبال حملات ارتش آمریکا به سیریک و جزیره قشم، پایگاه‌های دشمن در منطقه مورد اصابت موشک‌های هوافضا قرار گرفتند».
@
VahidOOnLine
سپاه در بیانیه‌ای با اشاره به اخطار خود در ساعت ۱:۳۰ بامداد شنبه به چهار نفتکش که قصد خروج از تنگه هرمز را داشتند، گفت یکی از این نفتکش‌ها را هدف قرار داده و متوقف کرده است و دیگر شناورها نیز به عقب برگشتند.
طبق این بیانیه، در ساعت ۲:۳۰ بامداد نیز پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک با دو پرتابه هدف قرار دادند که نیروهای هوافضای سپاه متقابلا با موشک‌های بالستیک به پایگاه هوایی علی‌السالم آمریکا در کویت و تاسیسات ناوگان پنجم نیروی دریایی آمریکا در بحرین حمله کردند.
در همین حال، ستاد فرماندهی مرکزی آمریکا، سنتکام، در بیانیه‌ای با اشاره به اینکه در حال حاضر گزارشی از آسیب به نیروهای آمریکایی وجود ندارد، اظهارات مقام‌های سپاه درباره آسیب زدن به مقر ناوگان پنجم آمریکا در بحرین را تکذیب کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75964" target="_blank">📅 05:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p-rmcLzVEnFIxg3jAW_MTKgd1yC6BN8tSVbDWiDrVzc8zxGt56N395z2G9X23-4ECc3iFt6JZxPXxYRhBEbCa91VEhz57mHfgXAUx6iGNrNbVAxS_vHoCuBTyAbgFqszI9kvGQoNu6TJMtkdiOruDDv4tp67mI-tyQMVD2UYiDv2pP4P9ivvVnDioNi-3Egi9_m6Q6kmXopxZWT3KIIJ5Ulo2yF9v3I2nCUkal4-021xU6tfLe-w0UyAMK60bGbT-7ftvQP_onTNEAz1_enTNI7NX-aI_TDXeqidLTT4M6JpO6wDgW7NQ4ExfkEF1ELbSQs80Ci_j3LBRIGhvS4mGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kZ0JvCLLJwxsH0RXDMN38jd5AsX7Q5Qvp-FNf89Oy_iiVhUHW746aZjkqcaum4TxPZJrneJZH1k-RSY3X58epBv7KSbd7KY2AjR2XJREH-CriOa1HKvgkKLJRsrDy7U8F6Y8HT8kBqjiAmlizIb3OcnGxhrBuwadAcwjPquMLm08L5IKls-LNZulTW4ulA3yvzG9un-wBpcWi3ZWtNXR0AmRzQYKJqr5-a-Qa7ZaPaGEwcIauZd5KCYd6D-USCwInATssA4iWn2YjKve0hI7nQKTzCAAFbNDgeqTF47bSf4kfaMm9_834NbWl5YLcoiko_5JZtSCMLx-49uk3RX8Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0de9d2e9d1.mp4?token=k2gIyicpUFxalTnx1qvl3zVJVWkZ0IOt8Fpl-4x8z3ouJWMzjZndfhXKdZKm-d-WV1KJN-uqBOurxt0zKp37N7yHy-RJw9c8BTLi3trWbLk7V8UUOeNMpLq-UVYSP3vBhGLxxUq1j651CGshHQkJHvjEJLIyh2NR7g_Cw0qKxnFjiMZjlTmRRwxJ3bS-YqjdsuWLXWl1P9f8_uw0SU0f86vuMXgVuTB_zyZ3Ek3POWme7csOwkl5aA4QczVUYSGSh4pYhspWUxF0SfxoqzrQjCQHu2000l8KptX5VpJq5iKqMSswMpWgpLB90msO7ffcJXAFCN5MsS-4W0vFgLv1CA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0de9d2e9d1.mp4?token=k2gIyicpUFxalTnx1qvl3zVJVWkZ0IOt8Fpl-4x8z3ouJWMzjZndfhXKdZKm-d-WV1KJN-uqBOurxt0zKp37N7yHy-RJw9c8BTLi3trWbLk7V8UUOeNMpLq-UVYSP3vBhGLxxUq1j651CGshHQkJHvjEJLIyh2NR7g_Cw0qKxnFjiMZjlTmRRwxJ3bS-YqjdsuWLXWl1P9f8_uw0SU0f86vuMXgVuTB_zyZ3Ek3POWme7csOwkl5aA4QczVUYSGSh4pYhspWUxF0SfxoqzrQjCQHu2000l8KptX5VpJq5iKqMSswMpWgpLB90msO7ffcJXAFCN5MsS-4W0vFgLv1CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'رد موشک‌های شلیک شده از ایران'
تصاویر دریافتی از استان‌های فارس و بوشهر
آپدیت:
وزارت کشور بحرین نیز دقایقی قبل از به صدا در آمدن آژیر خطر خبر داد و از مردم خواست به اماکن امن بروند.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75961" target="_blank">📅 04:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a-GQBaJHaq77ZtqA8ZNAQATyPl77_BHoK-Iq9-BSozdqA-GEpJogccJuyRpt7nuhvRIb9Hhb505xkkck83MhXe4mwj-vEbAOJYDQ6kvBXAcfzDLlnHtY9CEsKCEOcFsqgL6jjAFuHBg-nYxsHgyVUjjWCZZdL4gXxT2fxaL4tuxJ_RPAUL31Ecw20vmR9zoKdkUdai4bNgyeEdrdpiQ1FdUDRh4Ht1ou6VSgbzurnKxtFbtkkNL69uRHbBuPJTnQSrqUbOE6lcmO3a63VnhvBcCTIvXmPmEsJRtQEDl591uc2PxUYLeud2ktMauAoTCOsJalfbe3zJQxu_PirHzOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک‌هایی دیگر از ایران همزمان با صدور هشدآری دیگر در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75960" target="_blank">📅 04:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FoRp0ESEEESZnGBvJ_D5CFyAc8qyJjhDrxs3m--Fq2zzYW3JCnSsUBwDwwkj3Ox3rEqH6jSeWkg2MispnyGdt85eVMTGyN4P3G4qa-H5AYd8CRpIVHi7Ujlu-lUpofq9fgmvpAQh-hFLtw8JnxNU__z7PiF6nO12z8jaJX-Unwbfumo0I7PfL9SLCoLa62kGdk6ZVowX1c_NZ8eAvNNe6Ncq1XbS8HHHzmNNeS49pDwN0ykJRe2ele4-MptRcn2Deh7WXuj5JxlWecyClfbokczkE-8O_gZ7RTBoWrf47W5UIlcGK1415GjC-z92LMBvedMNbi77mO-rtwinubfsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: اعلام هشدار در کویت
آپدیت:
ارتش کویت دقایقی قبل از فعالیت پدافند هوایی کویت برای مقابله با «حملات موشکی و پهپادی خصمانه» خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75959" target="_blank">📅 04:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C67yUJTaaG9XHFqiKOpHMqHmOT9FHtBKsbBvIHtNZCzbydxEs6oQ8hxhYIBocI7GMsx1HQJ3QSmlVuth3Z_HI6Ree9MSnERURg6ZGhsK5oTzY2AU4udKcbQd13t1ZmISZ-92rRBzB42ZM1jsBrwtvGqL2NjgOw_xBqLZ6ErpQLoUOJqx8E5uS_CGquKi2VAIONvdh7DXdg6tFbcHlD4A3g7m0rmEneCYz0atLCHnX7-5ODC36tHYPAT6Xx2ODafCZ9q4_Mu3E32ElLYlzKyrhxXPaRfHC35jwPOCwaaaFsjgf-EUONqGtyT7P1riPsZoQGgwIqYdaLWkYChqOpR00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی مرکزی ایالات متحده (سنتکام)، بامداد شنبه، ۱۶ خردادماه، با انتشار بیانیه‌ای رسمی اعلام کرد که نیروهای ارتش آمریکا چهار فروند پهپاد انتحاری (یک‌طرفه) ایران را که به سمت تنگه هرمز پرتاب شده و تهدیدی فوری برای تردد دریایی منطقه به شمار می‌رفتند، سرنگون کرده‌اند. بر اساس این بیانیه، نیروهای آمریکایی متعاقب و با هدف دفاع از خود در برابر حملات بیشتر، سایت‌های راداری نظارت ساحلی ایران را در منطقه «گروک» و «جزیره قشم» هدف حمله قرار دادند. سنتکام در پایان با تاکید بر حفظ آمادگی کامل نیروهای آمریکایی افزود که واشنگتن برای دفاع از خود و پاسخ به «تجاوزات توجیه‌ناپذیر ایران»، در حالت آماده‌باش قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75958" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سیریک در هرمزگان
پیام‌های دریافتی:
پایگاه نیروی دریایی سپاه بندر سیریک  رو همین الان دوباره زدند. همون
لوکیشن چند روز پیش.
شهرستان سیریک صدای لانچ موشک ساعت  ۲:۱۴
سلام ساعت دو ده دیقه
پنج تا انفجار نیرو دریای سپاه سیرک هرمزگان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75957" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzjxAOe5kcLRgl7YNvrKwTo9V6ICcLpx7tlzxwdEtBAZOzi62rbChgsRDZaMAjqifUv8pmfSX7fiiTSVnmT-ElKUgBON78eIR9typDPUBiz-fmQgrYc--4V-dRPpmheMzPZ1YlConTePviY23xN1Th1simr90vaNFwQd2qbAIRx8_TJt17y0UDemCB-WiePDi-acCLMp1i1Bx9py8bh7AlMvxugzOjGMyaYPxAA9y0FpgakTAt57itsMXSQpfnMUySXAL1aQY0ipdHqbkSshb8aywcbWsZCWitl8xi3jp0ddQ4e5R1JjHRDmOONcY7L6WWC7OxIqohFztxLwQLINag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
وب‌سایت آکسیوس گزارش داده است که استیو ویتکاف و جرد کوشنر، فرستادگان دونالد ترامپ، روز پنجشنبه برای رایزنی با گروهی از کارشناسان فنی به آزمایشگاه ملی اوک‌ریج در ایالت تنسی سفر کردند.
به نوشته آکسیوس، کاخ سفید در تلاش است با ایران بر سر یک تفاهم‌نامه برای پایان دادن به جنگ و آغاز مذاکرات تفصیلی هسته‌ای «به توافق برسد» و می‌خواهد در صورت آغاز این مذاکرات، تیم کارشناسی لازم را آماده داشته باشد.
به گفته منابع آمریکایی و منطقه‌ای، تهران و واشنگتن همچنان بر سر برخی جزئیات این تفاهم‌نامه اختلاف دارند، اما مذاکرات وارد مراحل پایانی شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75956" target="_blank">📅 02:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XlWwuzeBH_ss6hPggUaomIqnXvrLuXfWX6cu-D7RB1cocNCSkAUpmIMNmG7zKnubXMd7168ysEBAog52XA6g_G_O9904Q1jVuAOHho5gt5LUoU2YIo4Epr_-WDvBbuJd_XcQv6h_mnaQkzh4Q3vnc8ShNKono4ALEELhuI_ZE8_r3_s1HzXaywbTobVeZ2jy6wgYzVbmY94KmK39pp93RfvNPxS9RwEORTkaW94CmPQb99Tq3R2Vjy_oG3J_bO63knx6_E-7ZrgxuODVCypyyWpF-dtQ9jIX2eK18c3vKOrllX5zUrIgT3FvpsdsBJ8aBwhfzyH4pz9qBcfhjBTCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مقام آمریکایی گزارش داد جمهوری اسلامی چندین پهپاد انتحاری را به سمت تنگه هرمز پرتاب کرد که هواپیماهای آمریکا دست‌کم چهار پهپاد را سرنگون کردند.
این مقام گفت مقام‌های آمریکایی گمان می‌کنند این پهپادها کشتی‌های تجاری در حال عبور از آب‌های منطقه یا نیروهای آمریکایی فعال در نزدیکی آن منطقه را هدف قرار داده بودند.
@
VahidOOnLine
ساعتی پیش‌تر اخباری درباره خارک و بندرعباس در بعضی منابع منتشر شده بود، خبرگزاری مهر میگه صحت ندارند:
جمعه شب خبرهایی مبنی بر شنیده شدن صدای انفجار و پدافند در جزیره خارگ منتشر شده است.
پیگیری های خبرنگار مهر مستقر در جزیره خارگ نشان می دهد، چنین خبری صحت ندارد.
بامداد شنبه برخی فعالین فضای مجازی مدعی وقوع درگیری‌ها و حملاتی به شهر بندرعباس شدند که بررسی‌های خبرنگار مهر نشان می‌دهد هیچ‌گونه درگیری در این شهر اتفاق نیفتاده است.
شلیک‌هایی در این منطقه صورت گرفته که جنبه اخطار داشته و کانون تحرکات در دریا و فراتر از جزیره لارک بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75955" target="_blank">📅 01:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75954">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4d85c72c6.mp4?token=jDCWJGN61j9GcrXbeF0O542RUSsqzvsnppBiDDrASmyoLm3FgejU0y9Hgp6MVbC2usf64zSscnn4UwVWIzYPwtEkw3FMHmRHkOf0qnEYihHoM3cA472NjDot8eycUSVqCt4sgZn1ms7fA--WA2tr6cbSUoAFlyKTKHLoLPN2N6WYfqQPUaJWzbDjxDIzn8iMKfLhVQomBsFjqZBaBJs45hdhh24dYSaHlGe_1MTGmDtgXSyVMXm_v-tQjYlTU3-ZBF79GcePnW2XyajvbHlDNCiIGK1DNd1dtuhzf3pidawwKQwf8GlnB7PRHGp982cit0VYmgwf2V3-m4DRpU-9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4d85c72c6.mp4?token=jDCWJGN61j9GcrXbeF0O542RUSsqzvsnppBiDDrASmyoLm3FgejU0y9Hgp6MVbC2usf64zSscnn4UwVWIzYPwtEkw3FMHmRHkOf0qnEYihHoM3cA472NjDot8eycUSVqCt4sgZn1ms7fA--WA2tr6cbSUoAFlyKTKHLoLPN2N6WYfqQPUaJWzbDjxDIzn8iMKfLhVQomBsFjqZBaBJs45hdhh24dYSaHlGe_1MTGmDtgXSyVMXm_v-tQjYlTU3-ZBF79GcePnW2XyajvbHlDNCiIGK1DNd1dtuhzf3pidawwKQwf8GlnB7PRHGp982cit0VYmgwf2V3-m4DRpU-9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش امشب برنامه «خیابان انقلاب» به خاطر این حرف‌ها لغو شد
beehnam
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/75954" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxWw1clHMoUQYMujk-zaWo635zF2uRSDZjbjgIjf1B1gfnKBVKoq-qqpUE-5tXwMv1j4XhZcKrx2ifGDutBNMWHdDeXrBwT-terSvtjgMbRMeciBUfH7_ksLQfCrrb8lFSYEgm0EUfT9eqi44wf-HO2FU5GWjb_4ucGoOkkAMSpLTCQNrULbpdSIrhe9t6hygvXpL1HRi9rC5FEn8J3f12q-HrcCIVsILjJV5CTkcUqAGjVIjLom2PJZpGd7oO1GHr-tNzEs7vP2l-pVnKdK67A30ScTx8EgElZ7zSGyzAt9gJHPY8DITcLWAv83dhgYIigIoIdm3h1EWEWStP5Sug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام کاخ سفید روز جمعه به خبرگزاری رویترز گفت که بازیکنان تیم ملی فوتبال ایران برای ورود به ایالات متحده و شرکت در جام جهانی فوتبال ویزا دریافت کرده‌اند.
تیم ایران قرار است نخستین دیدار خود در جام جهانی را روز ۲۵ خرداد برابر نیوزیلند در لس‌آنجلس برگزار کند. این تیم سپس در همان شهر به مصاف بلژیک خواهد رفت. بازی سوم در سیاتل مقابل مصر انجام خواهد شد.
@
VahidHeadline
آپدیت:
فارس، خبرگزاری وابسته به سپاه گزارش داد که ویزای برخی «اعضای کادر فنی و اجرایی» تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن «خودداری» کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/75953" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI_IyiZZzMfYldMRcCcLrzajK4IJz3PI3rhPUYVLug70-Zkolcos9OGp-_xPVjKwGYkieIIBlMUHw_FTfBL_MvzOPP1PMeAOlmumHwfxOedcAiA7tQyoLLzZlHG2BqsKxB49OE_LbHKFqV6WxpEqnYFz0Q2UtaeDdNN9TWWIvTwrkYwVLzN0ceJh272XhLqOmnqMZBkTGVLuhZt7bLQPvy25y5G7b-Yi9EFpyYm354A8sQwa64YLpJzapfK3qlb70BEy23N7QS3C4H9aOMOhrOgEBEEQdPqefWd1rGKzgR2ftF_UHFGcdLF73cHGp-EMov9UXqubFIhS_Iz2tlEBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسعود نبی‌دوست» خبرنگار خراسانی فعال در حوزه میراث فرهنگی با انتشار تصاویری خبر داد که کلیسای تاریخی انجیلی مشهد، از آثار ثبت‌شده در فهرست میراث ملی ایران، بامداد پنج‌شنبه ۱۴خردادماه۱۴۰۵ به‌طور کامل تخریب شده است.
رسانه‌های ایران از جمله «جماران» نوشته‌اند که تخریب این کلیسا «توسط عوامل ناشناس» و با استفاده از بولدوزر صورت گرفته است.
فعالان میراث فرهنگی می‌گویند این اقدام در سایه غفلت مسوولان میراث فرهنگی رخ داده، عملیاتی که حدود دو ساعت طول کشیده و صبح روز ۱۴خرداد نیز با بستن اطراف این کلیسا از ورود افراد و خبرنگاران جهت عکاسی ممانعت به عمل آمده است.
انگیزه، هویت افراد یا نهاد تخریب‌ کننده، مشخص نیست اما این نخستین بار نیست که یک بنای ثبت ملی شده تاریخی در ایران بدون اینکه نهادی مسوولیت آن را بپذیرد شبانه تخریب می‌شود.
کلیسای تاریخی انجیلی مربوط به دورهٔ پهلوی اول است و در خیابان جنت، کوچهٔ گلستان شهر مشهد واقع شده است. این اثر در تاریخ ۲۵ مرداد ۱۳۸۴ با شمارهٔ ثبت ۱۳۳۷۵ به‌عنوان یکی از آثار ملی ایران به ثبت رسیده‌ است.
پیش از این بارها بناهایی همچون کلیساها، آرامگاه‌ها و بناهای متعلق به اقلیت‌های مذهبی از جمله بهاییان، مسیحیان و یهودیان
تخریب‎ شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/75952" target="_blank">📅 21:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امروز ۵ ژوئن ۲۰۲۶
قاضی فدرال آمریکا امروز حکم داد که تمام سیاست‌های تعلیقی USCIS غیرقانونی هستند و باید فوراً لغو شوند!
leeleehozak
چه خبر خوشحال کننده‌ای برای دانشجوهای ایرانی آمریکا، امیدوارم بزودی روند بررسی پرونده‌های USCIS شروع بشه و استرس و نگرانی همه تموم بشه
21aban
بلاخرررررره خبری که ماه‌ها منتظرش بودیم، اعلام شد.
طبق حکم دادگاه فدرال، پاز برای همه‌ی‌ افراد در داخل خاک آمریکا برداشته شد، از این لحظه به بعد دیگه
#USCISpause
وجود خارجی نداره، چون این بخشنامه از نظر دادگاه غیرقانونیه.
درود بر استقلال قوه قضاییه که زد کل بخشنامه اداره مهاجرت رو لغو کرد.
درود بر دموکراسی که در اون قدرت، چک سفید امضایی دست دولت نیست.
پی‌نوشت: احتمالا دولت درخواست تجدیدنظر بده و اعتراض کنه به این حکم اما خب دیر یا زود پرونده با پیروزی ما بسته میشه.
BrmTheGreat
این
لینک اصلی و رسمی حکم دادگاه
ه
اینم
لینک جزئیات بیشتر این شکایت خاص
ولی از یه منبع غیر رسمی
mozfang
جزییات تکمیلی:
دادگاه تمامی استدلال‌های دولت را که سعی داشت سیاست‌های جدید USCIS را از شمول بررسی قضایی خارج کند، رد کرد و رأی داد که:
واژه‌ی «امنیت ملی» نمی‌تواند سیاست‌های مهاجرتی قوه مجریه را به‌طور کامل از نظارت و بررسی دادگاه‌ها مصون کند.
قاضی رأی داده که هر چهار سیاست جدید چالش‌برانگیز، ناقض قانون تشریفات اداری (APA) هستند و به دو دلیل عمده غیرقانونی اعلام می‌شوند:
۱. مغایرت با‌ قانون (Contrary to Law): اداره‌ی USCIS از حدود اختیارات قانونی خود فراتر رفته است. دادگاه اشاره کرد که اختیارات مربوط به محدودیت ورود (موضوع بند 212(f) قانون INA) منحصراً متعلق به رئیس‌جمهور و مربوط به مرزهاست، نه مربوط به فرآیند پردازش مزایای داخلی برای غیرشهروندانی که قبلاً وارد خاک ایالات متحده شده‌اند. علاوه‌بر این، سیاست اعمال «عوامل منفی بر اساس کشور مبدا»، به وضوح ناقض اصل منع تبعیض بر اساس ملیت در قانون مهاجرت (موضوع بخش 1152(a)(1)(A)) است.
۲. خودسرانه و دمدمی‌مزاجانه بودن (Arbitrary and Capricious): این آژانس نتوانسته است استدلال منطقی برای اقدامات خود ارائه کند، منافع و انتظارات به‌حق مهاجرانی را که طبق قانون عمل کرده بودند کاملاً نادیده گرفته، و به دلایل ساختگی و بهانه‌جویانه (Pretextual) متوسل شده است. دادگاه به یک «عدم تطابق جدی» میان اهداف اعلام‌شده امنیت ملی و آنچه در واقعیت رخ داده اشاره کرد؛ از جمله اظهارات بیگانه‌ستیزانه همزمان رئیس‌جمهور و کریستی نوم (Kristi Noem) وزیر وقت امنیت میهن در شبکه‌های اجتماعی، و همچنین استثنائات خودسرانه‌ای که آژانس برای ورزشکاران جام جهانی/المپیک و پزشکان در نظر گرفته بود.
🟣
دادگاه رسماً هر چهار سیاست را غیرقانونی اعلام کرد و آن‌ها را به‌طور کامل ابطال و ملغی اثر نمود. از آنجا که این حکم یک دستورالعمل دولتی را ابطال می‌کند، عملاً اثری سراسری و ملی در کل کشور خواهد داشت.
🟣
دادگاه درخواست شاکیان برای صدور دستور منع دائمی را رد کرد و استدلال نمود که حکم ابطال و اعلام غیرقانونی بودن سیاست‌ها به خودی خود برای جبران خسارت شاکیان کافی است و نیازی به این ابزار فوق‌العاده نیست.
🟣
درخواست دولت برای رد ادعاهای اساسی شاکیان (مبنی بر نقض متمم پنجم قانون اساسی در خصوص رفتار برابر و رویه عادلانه) رد شد. دادگاه بر اساس اصل «اجتناب از ورود به مسائل قانون اساسی در صورت امکان»، اعلام کرد که چون پرونده بر اساس دلایل اداری (قانون APA) به‌طور کامل حل شده، نیازی به صدور رای در خصوص بندهای قانون اساسی در حال حاضر نیست.
این حکم به امضای قاضی ارشد، جان جی. مک‌کانل، رسیده و لازم‌الاجرا است.
منبع‌:
کانال مهاجرت به آمریکا
BrmTheGreat
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75951" target="_blank">📅 19:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C4bXyOsyb00K_qkSaRgIDXznqQGZILHFSN4BmheM-ztUNYEjErdgsAjHihSwL85QPZ-7-w7_x5O4nGBvXsRZokdNU3elb1BvYli9QbzUip7mAmeXTo_dNhYUYWY1xjG62rbCO779frLWxeXcqhmPzlmBjzFAri2sIe_4ZIt8thwlzakK4qFsB_fttBop7V20lB_sVRdYYe-WU_9A1ueSwZi9MXzuXzo9ayNwehpw6uj7cuCndH2O_6E2igz4wukCruABX0bfCP0TLI0GlsVwsn9bzLuVK9tllQi0Xz1Bo8xj9oSyWXeUqJxekYWsy6nBdyJOaulc3mp1a98vHNEBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qaA3xX7_nkGjOhDAXSg-RkTfOO86-hwAKZvnAnkXH38qshTOjUqIswoKBnHxEmuTGDREgNzuQT3UokptrioBBzn_M1RFmimz0oI1GA8_zIds08mOWGmtKQ00QN_Ne9lybi7gq4FYjDHdTqddVgVWHIhXJT2dx94xq2_RXlEmYLutLagdMuy8N6wBtsfg25w_1gfDJEE46KIfOIu4t7p-Ma3MonAjPJnO3ka_VOcCV_6qsaYUlIw2OMTgEOJaP44GQCoK_HF7d2_EzEWKozELloOCOQs8rPV7zv3l_1bu9jwalzzW9sINRogNgb60mJzLpo_uyZcgRrR1QoNGDEpc_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شبکه خبری الحدث، روز جمعه ۱۵ خرداد ماه به نقل از «منابعی آگاه» گزارش کرد تهران موافقتش با انتقال بخشی از ذخایر اورانیوم خود به یک کشور ثالث را به اسلام‌آباد اعلام کرده است.
بر اساس این گزارش، اصلی‌ترین اختلاف باقی‌مانده در مذاکرات میان تهران و واشنگتن به موضوع آزادسازی دارایی‌های بلوکه‌شده ایران مربوط می‌شود و نحوه و سازوکار آزادسازی این اموال همچنان یکی از شکاف‌های مهم میان طرفین به شمار می‌رود.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران،‌ روز جمعه ۱۵ خرداد ماه به نقل از «یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران»، گزارش شبکه العربیه درباره موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده به کشور ثالث را تکذیب کرد.
خبرگزاری فارس به نقل از این منبع گزارش داد ادعای مطرح‌شده از سوی العربیه «نادرست» است و موضوع انتقال ذخایر اورانیوم در دستور کار فعلی مذاکرات قرار ندارد.
به گفته این منبع آگاه، موضوعات مرتبط با پرونده هسته‌ای در مرحله کنونی گفتگوها مطرح نیست و بررسی آنها به مراحل بعدی مذاکرات موکول شده است: «ابتدا باید طرف آمریکایی اقدامات مشخص و قطعی خود را انجام دهد و درباره برخی مسائل اساسی به توافق‌های روشن و نهایی دست یابیم.»
شبکه العربیه پیش‌تر گزارش کرده بود تهران موافقتش با انتقال بخشی از ذخایر اورانیوم غنی‌شده به یک کشور ثالث را به اسلام‌آباد اعلام کرده است و این کشور ثالث با توافق طرف‌های مذاکره‌کننده انتخاب خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/75949" target="_blank">📅 18:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuCRp5exqlqrAKabkG-JuDbQgQpHPBdko3ggnRwRiOjxzFYvmF_rQMlRZG0QdfwKpF6jClafYJVIEKHU11vfqwGxjW-QfQ_VgVvh2zrS985va3imac_SPiwXAGZzckEpFfnax38cx3AWZ6DS1JGPR6fRbm98-czYK-R1xj5K5Hx1uArwOnpOLbAjAHHxCm1OsuhEoucrHs7BGgu7b-PoKij9ujFMshHTGd1R1f1Lj3N2wqe8BNGpPzpWoWIBmcf4o-PBBSjM7DNSjo4pIa_QaMR7Ly2MKgtu2z1TrV6vfU4uG1evWCtx2fTBQlY0hqtJt3GB6dFryO8gcEvTlGaLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوزف عون، رئیس‌جمهور لبنان، در مصاحبه‌ای که روز جمعه منتشر شد، از ایران خواست در امور لبنان دخالت نکند. او همچنین به گروه حزب‌الله، متحد مورد حمایت تهران، گفت که تنها راه‌حل درگیری با اسرائیل، دیپلماسی است.
او در این گفت‌وگو با شبکه خبری سی‌ان‌ان خطاب به ایران گفت: «این کشور شما نیست، کشورِ ماست... دخالت در کشور ما وظیفه شما نیست.»
آقای عون افزود: «آنها از لبنان به‌عنوان یک اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کنند. این غیرقابل قبول است.»
رئیس‌جمهور لبنان همچنین گفت: «حزب‌الله باید درک کند که هیچ راهی جز نشستن و گفت‌وگو وجود ندارد؛ هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده است، جز از طریق مذاکره و دیپلماسی وجود ندارد.»
حزب‌الله از سوی آمریکا به عنوان سازمان تروریستی شناخته می‌شود اما اتحادیه اروپا تنها شاخه نظامی آن را تروریستی می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75948" target="_blank">📅 18:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75946">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PiYt2Dy4OiYr9Bu-1JnuZQu94KFGoLb-Z6ZNptRROFdH6vnrIX5NujsgWjyb_h-x4FNraJeQ6egq1C839m2Xb8UkR50bqV1RclFH3B4BmY7h_B_5-Ogtcjmf8iNU4-ySd1mGKFoOrDi0jnXRuRxsMUD3uxM_iRHQbAJsq4t1FZV0i2hGCp8afn1dsp--tJWfdarts8uh21lZUkjsP0HWKo9yokc1mWXM1Yk6GQuyopI1qDX1QxaCz2hckvMF4-janxFOUI1VyghbowoZi8IMXIQL9x1Ov8VC4NmpoMdoQkWZHIHtKchjJUE_xOjCNxpIZo6FzaDYWgsqcsew1apzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/03b8183b03.mp4?token=PBWYGDO5LXcFnB83VsNoPB-EO93gKihtG38Om2C9oO6u6vHQx16v-nxwiemzC_DW0LA0IpxiNH9b1irdVs1T-_T790oi4oHvJWwFrq9VhwuLruDHpQzEnyrt9NKx-snhKlFZOWMfu9eDco2nbEUG_7MJPrm4bOeFSlkis_oM4onGMgiWBJ3WpNm-0XdVOBhJcSZSOzg83uipzX7R1O0EY2I6k061cw0QEMhc5I-ZLRZqCd_DIEJsa5-K7kWpaks72K5u2nVtuT7vw55h12cY5ezXBDkneB1PORM42nbZZb07K_KBayIasL_Bi_eA-j5m63fpKYSMShebXa1Fp33L8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/03b8183b03.mp4?token=PBWYGDO5LXcFnB83VsNoPB-EO93gKihtG38Om2C9oO6u6vHQx16v-nxwiemzC_DW0LA0IpxiNH9b1irdVs1T-_T790oi4oHvJWwFrq9VhwuLruDHpQzEnyrt9NKx-snhKlFZOWMfu9eDco2nbEUG_7MJPrm4bOeFSlkis_oM4onGMgiWBJ3WpNm-0XdVOBhJcSZSOzg83uipzX7R1O0EY2I6k061cw0QEMhc5I-ZLRZqCd_DIEJsa5-K7kWpaks72K5u2nVtuT7vw55h12cY5ezXBDkneB1PORM42nbZZb07K_KBayIasL_Bi_eA-j5m63fpKYSMShebXa1Fp33L8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده، سنتکام، ادعای ارتش جمهوری اسلامی درباره شلیک موشک و پهپاد به سمت ناوشکن‌های آمریکایی در دریای عمان را تکذیب کرد.
رسانه‌های ایران روز جمعه به نقل از ارتش اعلام کردند که نیروی دریایی آن به عنوان «اخطار» به سمت دو ناوشکن آمریکایی «موشک قدیر و پهپادهای تهاجمی جدید» شلیک کرده و این دو ناوشکن دریای عمان را به سمت اقیانوس هند ترک کردند.
سنتکام که فرماندهی نیروهای نظامی آمریکا در خاورمیانه را برعهده دارد، ساعتی بعد در شبکه ایکس اعلام کرد: «نیروهای ایرانی به ناوهای جنگی نیروی دریایی آمریکا حمله نکرده‌اند و به سوی آنها آتش نگشوده‌اند. انجام چنین اقدامی نقض آشکار و فاحش آتش‌بس محسوب می‌شد.
در این اطلاعیه بر ادامه محاصره دریایی ایران که از اواخر فرودین آغاز شد، تأکید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75946" target="_blank">📅 18:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnOugJSXm685S30lF526RELCjQtKKZRMFjHBrg4uAPlEkIt_WYnIWOPfYNH-bnLhswJij1XtpPJwXgUVRNZm0l137pVb7BPY20C0HpIk4FdzLIDA1J7ztyuA5WLmioGBwC4sHgUsW_NmyTAtKzzHRbj0Kuz14x7r9BRoSu2D_1RpwhcMhTvftEFG3O1_w2Ln_uCLW61r1yYUDrHdqw55M8w5XRcbTONHv7QbTUPXxDtOamzR2GbJH7VYvJxDdrbZ3uZ0F0GfES4j3jL4xGQnqr_EU6RuQsTc_RafErRVr_qZ6a8bgkQ1Lra7ZuyXTxGF-h6ZjlkYWgXvWmD56MCjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کمالی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه ۲۶ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌است.
رسانه‌ حقوق بشری هرانابا اعلام محکومیت علی کمالی به اعدام، نوشت این حکم در حال حاضر در دیوان عالی کشور تحت بررسی قرار دارد.
به‌گفته هرانا شعبه ۲۶ به ریاست ایمان افشاری در اواسط اردیبهشت سال جاری حکم را صادر کرد. کمالی که دارای اقامت مالزی است، ۲۲ دی‌ماه ۱۴۰۴ در تهران بازداشت
شد و اکنون در زندان تهران بزرگ نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75945" target="_blank">📅 18:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K9uxT6qOWn-C_4wv4ukXaSw8iUrZY_FnM6vRXpmhco-r_ej34PGE5kraxSwXeAX9IWRP_8oCRN3laUQbm1acrTQr4dj4POGgEGHzf8GpoP2nU7hSwZ0BdDMjAoWDUOsDpKyzDeBe3H3Z7wMadbCnAFV4ykAvH7CXf8AwEBnrBxbjOeBpi3J59zEDqcJWpy8C_o6Sn7UTqOeebpdAC3yt8jNslsT7rcgVK4NyH5Cp6jAlMmWSuNNK53LOPMHttQZTN04gq_aGSFfWws3Ozk6-Q6CpC9stUOKe1wpyaF6Jt4UXAR8Be3bDni1P9vAQrJxTNNv-8e_w_ilwnPIUcj88Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع در روز جمعه گزارش داد که پایانه نفتی مینا الفحل در عمان پس از وقوع یک انفجار در نزدیکی اسکله‌ها، عملیات بارگیری نفت را متوقف کرده است. به گفته این منابع، انفجار ظاهراً در پی یک حمله پهپادی رخ داده است.
@
VahidHeadline
AJENews
هنوز مشخص نیست این حمله دقیقا چه زمانی روی داده است.
بر اساس داده‌های کشتیرانی ال‌اس‌ای‌جی، روز جمعه چند نفتکش بسیار بزرگ در نزدیکی این بندر لنگر انداخته بودند.
رویترز در ادامه
نوشته
:‌ رسانه‌های دولتی ایران روز چهارشنبه گزارش دادند جمهوری اسلامی یک کشتی نظامی آمریکا را که «مرکز کنترل و فرماندهی» توصیف شده بود، هنگام نزدیک شدن به آب‌های سرزمینی ایران در دریای عمان هدف قرار داده است، اما ستاد فرماندهی مرکزی آمریکا، سنتکام، این گزارش‌ها را رد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/75944" target="_blank">📅 06:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hvM6Xxd4RmNdYQId4DRMkwMxw26L4iLxY59PZHm3ynNnfNY4CcI-mTg_2Jf-Dn53Le3HiFjQV0q_Kl4pi-9_eXEv0PFLbTkfgu2N2A6GC4vGY9UHCJDQmGlvm3E6wgROjWRqje7vjmpWkrSKr1UnjBCUYkQ_RazXe5lzZGaYWUSNfmIIhA2S-rWRHUmbVzdEo3QdyqhFLbJgGNTj9WxO1ku0yl3DTOk34nKHABA1KYt40-1De9Lhwk4ogxfNzDzg4QPHKpCR_NAIU4xq9BJuyBVpuzcqEbVQ5u6Y04cPbigiZ90ATQl7j72LGNQGfwPl0iNAJQu_qEK3-dMmdsQnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: ایران نباید سلاح اتمی داشته باشد
دونالد ترامپ، رییس‌جمهوری آمریکا، در کاخ سفید در پاسخ به این که اگر حکومت ایران نیروهای آمریکایی را بکشد، آیا جنگ با جمهوری اسلامی را از سر خواهد گرفت، گفت: «این دلیل خوبی برای چنین کاری خواهد بود. اگر آن‌ها نیروهای آمریکایی را بکشند، فکر می‌کنم خیلی سریع دست به این کار بزنم.»
ترامپ درباره جمهوری اسلامی تاکید کرد: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا گفت: «ما برای به‌دست آوردن اورانیوم غنی‌شده آن‌ها به توافقی با ایران نیاز نداریم.»
او درباره کمک ناتو به بازگشایی تنگه هرمز نیز گفت: «ما به آن‌ها فرصت دادیم که کمک کنند، اما نخواستند کمک کنند. این موضوع برای آن‌ها بسیار پرهزینه خواهد شد، چون نباید چنین کاری می‌کردند. باید کمک می‌کردند.»
🔻
ترامپ درباره جنگ: چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد
دونالد ترامپ، رییس‌جمهوری آمریکا درباره جنگ ایران گفت: «چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد. بخش اصلی این است که تنگه فورا باز خواهد شد.»
ترامپ افزود: «آن‌ها (جمهوری اسلامی) هیچ نیروی دریایی ندارند، هیچ نیروی هوایی ندارند. ما آن‌ها را نابود کرده‌ایم.»
او ادامه داد: «رهبری‌شان را از بین برده‌ایم و تقریبا همه آن‌ها را نابود کرده‌ایم. بعد در رسانه‌های جعلی می‌خوانید که آن‌ها در جنگ خیلی خوب عمل می‌کنند. واقعا باورنکردنی است. ما هر چیزی را که می‌شد نابود کرد، از بین بردیم.»
🔻
ترامپ: حکومت ایران درباره توان و اراده آمریکا دچار اشتباه محاسباتی شده است
دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست کابینه در کاخ سفید با اشاره به مذاکرات جاری و وضعیت تنگه هرمز گفت یکی از محورهای اصلی توافق، بازگشایی فوری تنگه هرمز برای عبور و مرور کشتی‌ها است و تأکید کرد آمریکا «هم در میدان نبرد و هم در عرصه دیپلماسی» پیروز خواهد شد.
رئیس‌جمهوری آمریکا مدعی شد توان نظامی جمهوری اسلامی به‌شدت تضعیف شده و گفت: «آن‌ها دیگر نیروی دریایی و نیروی هوایی مؤثری ندارند. ما تقریباً همه توان نظامی و ساختار رهبری آن‌ها را نابود کرده‌ایم.»
او در پاسخ به پرسشی درباره احتمال ازسرگیری جنگ در صورت کشته شدن نیروهای آمریکایی توسط حکومت ایران گفت چنین اقدامی می‌تواند دلیل کافی برای اقدام نظامی جدید باشد و در آن صورت آمریکا «بسیار سریع» واکنش نشان خواهد داد.
ترامپ همچنین درباره ذخایر اورانیوم غنی‌شده ایران گفت آمریکا در مقطعی گزینه خارج کردن این مواد را بررسی کرده بود، اما به دلیل نیاز به حضور طولانی‌تر نیروهای آمریکایی از این طرح صرف‌نظر شد. به گفته او، واشینگتن همچنان توانایی دسترسی به این مواد را دارد.
وی افزود آمریکا با استفاده از سامانه‌های پیشرفته نظارتی و امکانات فضایی، تمامی مناطق مورد نظر را به‌طور کامل زیر نظر دارد و هرگونه تحرک را رصد می‌کند.
ترامپ درباره احتمال دیدار با مجتبی خامنه‌ای نیز گفت شخصاً تمایلی ندارد و چنین پیشنهادی را هم مطرح نکرده است، اما اگر چنین دیداری انجام شود، با احترام برخورد خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/75943" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpODWKC5etyBGk0b5BKhE0MGccAG396tRP7-oHmppWudBtfXwImMWQpRPRt_8PTRa8De6SueENrAGOMmdXRtnoW6Fq6VVoGYtWgrwLxbgV_nBq0gG92Hx_15wYUeuFucgk9H-AeAESV9gk1ApoZgcQjIUavHTv2OUFfMuXuVEmw5XD3phABvQpd8qmkOdQ3R0UtkIwoGWd3IEV_qogajfk5xK6lvqLD1vwrGo0CSEM97Z7qsFDCmYVZPgBLXS4_yFflQ8IWa1mAELiO3bSDLhHcgPTzKjnqG3QdNG03tRuWIxcKfskaQ_gvuV-P4iwD_vuE7ly9BVzXrM9sQ-aRU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه پنجشنبه شب ۱۴ خردادماه، به نقل از منابع اختصاصی گزارش داد محسن نقوی، وزیر کشور پاکستان، برای پیشبرد مذاکرات میان جمهوری اسلامی ایران و آمریکا به تهران سفر می‌کند.
به گفته این منابع، سفر نقوی در چارچوب تلاش‌های میانجی‌گرانه اسلام‌آباد میان تهران و واشنگتن انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75942" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75941">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g1SxIzXmuysQ59FiJLpi74i7w6lyYno0jEahyojyxZ1Spww2L4LBBOE3oiquV5cExyFNGurFgvU_CipRLbHesRTXB7eSFQIqgdnhtkBJxVXbP9Cf4NfHneJfvo1LUXOq9y2ACVjvOIfx18zpV9jmsS8HjZF3U8ueR7XZ6rcjZ4yy34ynwcK9RHLIfC-dTMVQ9o_aIrLdPDjeFiv6qWoBMTR6KX3u_oXytIdLJADEXwGrBKKYwFTPgx3rocSSBicDlZ_qnzoZ-5X-WG2HO3VzvjPtN09TrVGAauWBO20rYcSAK3SIOcnIZY5EYTRU66uVnZkX_Ge5JHR5A0bo84ryzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه گفت ایالات متحده بر جمهوری اسلامی غلبه می‌کند، یا با توافق یا با عملیات نظامی.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/75941" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgXMId-1muNuMLBigLWr35mKD6z100w3TV2YjVeEStwhJkNVWGHvDmurqeZz5D3pHf7ELGZuhBLz2lOR77FRJTDgr8rCWZhBX_oOE5SEOi54alsbO-YB6mylBR5aFGC60kYTeR6JpKWH5D7CW_KvJRBCoOqIfebJFD98rtlwnhpOxGOu1vZcUFbOUpIMhVhkeLJVLiKZ_wxnXFfB06PYEbetNKNfZEBXFCGG_D2LceRyEIg2eBxt7Ldka0oWIyQ0rJN2qDnG-DReXWvabY1oeEuBETN6wHCPefZITUN0U4HDqt6liEgVbydPTDxjcnUuNoXsOsNCdErXpGzAzaz6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی پنج‌شنبه ۱۴خرداد۱۴۰۵ در گزارشی به کشورهای عضو، بار دیگر از جمهوری اسلامی خواست «به‌طور فوری» درباره سرنوشت ذخایر اورانیوم غنی‌شده خود پس از حملات سال گذشته آمریکا و اسراییل به تاسیسات هسته‌ای این کشور توضیح دهد.
در این گزارش همچنین از مقامات جمهوری اسلامی خواسته شده تا زمینه ازسرگیری کامل بازرسی‌ها را فراهم کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75940" target="_blank">📅 19:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JQ6rvM6FYwXF6QE_vEu316pOK5Rov9j4RPwc-vfrpc4g6ihCY7Dwfz1QDbFU5q1CYzDEMr6OCLA7KRBDtwT8MIe1Jb-9pjDnPVYl_xrKAEZLbbV6-TfgTolXwxJT5bG6q9UseV-3MTcaMK8iysKTgYqxeofZlOnIvTFckhDgmi6ZOx27EHYUd_48cFxLhd3eOY0DDX86396mfbTRvR7yDa6A69ZNpiQl5SZ3wUPiGLuezRJlABW1XD7Maierut7xbNWyS5KML5cn6Kun4wLKkjX-Wctmv2wpA0GrPTnx84EugpQk5AWpxzd_uCDu4GtAZ2aPTuwthguTUz1c-lIM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل گروه حزب‌الله طرح آتش‌بسی را که دولت‌های لبنان و اسرائیل در مذاکراتی با میانجی‌گری آمریکا بر سر آن توافق کرده بودند، رد کرد.
ایالات متحده روز چهارشنبه اعلام کرده بود که لبنان و اسرائیل بر سر اجرای یک آتش‌بس به توافق رسیده‌اند؛ توافقی که مشروط به توقف حملات حزب‌الله و خروج نیروهای این گروه از مناطق مرزی جنوب لبنان است.
@
VahidHeadline
نعیم قاسم، دبیرکل حزب‌الله لبنان، توافق دولت لبنان با اسرائیل که با میانجی‌گری آمریکا تدوین شده است را «تسلیم و شکست تمام‌عیار» توصیف کرد و گفت حزب‌الله تنها به توقف کامل حملات، آتش‌بس و خروج اسرائیل از خاک لبنان متعهد است.
او همچنین خلع سلاح حزب‌الله را به معنای از بین رفتن قدرت لبنان دانست و تاکید کرد این موضوع برای حزب‌الله قابل پذیرش نیست.
پس از توافق آتش‌بس میان اسرائیل و حزب‌الله لبنان، آمریکا برای حل‌وفصل اختلافات مرزی و مسائل امنیتی میان دو طرف نقش میانجی را بر عهده گرفته است. در همین حال، موضوع خلع سلاح حزب‌الله و نحوه اجرای آتش‌بس همچنان از مهم‌ترین محورهای اختلاف میان دولت لبنان، حزب‌الله و اسرائیل به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/75939" target="_blank">📅 16:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75938">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XbqWmJ08Q5k_Wnp-Edtk_TDWH6UgxlLS0z9fLkGvvM4XnGQWygg2BrrGc4IoZ2ibWkd11IabL0HiwsCEkI073nzmmHyKRGIBdHl7P7-gMWWaLbU5fKkUu4lYaxQtYBOLko1Hbp5bKhsqiBVrVdS8jaOokHQ6TRnJUwqraqrmRUkm8XDynchuA1ipCt7vNk0Q-HHsKJIL_gBH0bDlMWgZvNxmgjkdMf8tgSbAtAhzWtvYmC0xgpkAnPjlaCHoNIM62euGO1QM4f56e60iciqlbLHeonjhj_L2JCpdFxmg8WAuHdm6Y7K0rGNMV2kb1N1e1sgsBlZb0Nfa-rtVKOJXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران روز پنجشنبه ۱۴ خردادماه و ساعاتی پس از انتشار ویدیوها و تصاویری از برخورد پهپاد سپاه به فرودگاه بین‌المللی کویت، به نقل از یک منبع نظامی، آن‌ها را «تصویرسازی دروغین دشمن» خواند.
این منبع نظامی به تسنیم گفت:‌«پرتاب پهپادهای هوافضای سپاه به سوی اهداف آمریکایی در کویت، در نیمه شب و اصابت هم در نیمه شب (و در تاریکی هوا) صورت گرفته است درحالی که در فیلم و عکسهای ادعایی که از پهپاد در فرودگاه منتشر شده، هوا کاملاً روشن و مربوط به روز است.»
سپاه پاسداران پیش از انتشار تصاویر برخورد پهپاد با پایانه مسافربری شماره ۱ فرودگاه کویت ادعا کرده بود که موشک‌های سامانه ضدهوایی آمریکا به این محل برخورد کرده بودند.
این منبع نظامی که نامش فاش نشده به تسنیم گفت:‌ «فاصله «هدف» پهپادهای هوافضای سپاه تا فرودگاه کویت بیش از ۴۰ کیلومتر است و این نیز نشان می‌دهد که اصابت به فرودگاه کویت ارتباطی به پهپادهای ایران ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75938" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTWdu_4toNYmOZWmRPKxvZFR_B1gBCBFtl7OHLAfXZozESEgH8CFNA9o4TSV6cS-yLnWk0cGnFZ3x4K-LuQAzrxrxqeVR9Xgg6DzjIUynZP2qNRsetcOKgmeb0dsD92Mm5SqmQbKCmYRfOxXXoPHuiFkw3Bg-xL9GaAhgWTADLyL_TUjSEBAk39pTcXlb_Ij7hRMjY7e8yH6VZuoWVCkyZNUOTNV5vTNYnPSVdAYgo1eMP9bgBJDfUtDTW6XqsHv2xeiKQxpv2nr3AltqDPeITEY5mIdRSfF5vsLVkCJgJWMa-Ng-ux-wF9PntqywxwgoBTSx1q5EXv1v2AVJZmrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام مکتوب و منسوب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در مراسم سالگرد مرگ روح‌الله خمینی در تهران، خوانده شد.
در این پیام که محمدجواد حاج‌علی‌اکبری، امام جمعه تهران، روز پنجشنبه ۱۴خرداد خواند، رهبر جمهوری اسلامی‌ آمریکا و اسرائیل را به «جنگ ترکیبی» با ایران متهم کرد و گفت این جنگ «بر دو نقطه متمرکز است؛ یکی تاب‌آوری مردم و دیگری ایجاد اخلال در دستگاه محاسباتی مسئولان کشور».
مجتبی خامنه‌ای همچنین هرگونه اقدامی که به‌گفتهٔ او «موجب بدبینی و سرخوردگی» شود را «کمک به دشمن» خواند و خواستار «حفظ وحدت و انسجام و اعتماد متقابل» مردم و مسئولان نظام شد.
مجتبی خامنه‌ای هفتهٔ گذشته نیز به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داده بود که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
در بخش دیگری از این پیام، اسرائیل «پادگانی متعلق به نظام سلطه» توصیف شده و تاکید شده است این کشور از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.
این پیام همچنین اعلام کرده است: «دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است» و افزوده است دشمن پس از آنچه «تحقیری پرمعنا و عمیق» خوانده شده، تمرکز خود را بر تضعیف تاب‌آوری مردم و ایجاد خطا در دستگاه محاسباتی مسئولان قرار داده است.
در پایان، در این پیام از همگان خواسته شده است با ایستادگی، روشن‌بینی، حفظ وحدت و انسجام و همصدایی نکردن با دشمن، «نقشه شوم» او را خنثی کنند.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
مراسم سالگرد مرگ روح‌الله خمینی که هر سال ۱۴ خرداد با سخنرانی رهبر جمهوری اسلامی و با حضور پرشمار مقامات و فرماندهان ارشد نظامی برگزار می‌شد، امسال به‌صورت خیلی محدود و بدون حضور مقامات نظام برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75937" target="_blank">📅 16:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veb6sEc8NhXT3DP0Jo6-hw4HtmNW0u7-xDmKfIzz4srNp80NI90wywOdyvo0FKWUrbBby6R1Lve1rxep0DT2XfoCtv3YXFzyUG5VoCUEO-_nucHT_tvvasz8xhssu-xTGi1FLJV34WtYm3ST_vXxnrn_exZDnvBgT8BD-6iWnWq2lzQC7SrW64IFMgqCd2o19sgXjN11cY0VRqi2pxMer7UblruEmShoM0kIIoIDwjUFjod7pq6h_ao5F2cZ-XLAatksCJirJGaPqU5Et9lKE1Lq5wxKOcFf_gIncYTKtzUJYN5PN9BRPJyGRLLUH7fYMM9hcPP2Elfgt8y-n4qqYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس جمهوری آمریکای روز پنجشنبه ۱۴ خردادماه از تصویب قطعنامه «پایان جنگ ترامپ با ایران» به‌شدت انتقاد کرد.
رئیس جمهوری آمریکا در این پیام نوشت:‌ «دیروز، در یک رای‌گیری بی‌معنی، مجلس نمایندگان، چهار جمهوریخواه بد و تمام دموکرات‌ها، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران، به محدود کردن اختیارات جنگی من رای دادند. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آنها می‌دانند مذاکرات در چه مرحله‌ای است.»
ترامپ با انتقاد تند از نمایندگان حامی این طرح نوشت: «دموکرات‌ها از سندرم اختلال روانی [بیماری مخالفت] ترامپ تغذیه می‌شوند. آنها ترجیح می‌دهند کشورمان شکست بخورد تا اینکه به من یک پیروزی دیگر، از پیروزی‌های بسیار، بدهند. چهار نماینده جمهوریخواه، داستان آن‌ها کاملا متفاوت است. آن‌ها خودنما هستند! آن‌ها باید از خودشان خجالت بکشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75936" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-OpQb288hPhaQfGnMMDu_ZSDXv5QxootI7OvyVpvxNOgQOQKp_ybychKkzmRTIi6Lm_OPLzGpMY9UU3-jpSktt-3x1JYwz-BheiV08iNc85U2StYf647Q1dpqS_F0tr836buri2fRsR8RYFT960KkbrHyOrpQPkZ3HOMv-whguqMdi5JGRzsnls1668KYBpD4ceJMwmkQphAOsT1oDxBALOQKiClVZRtT1vL6ajmihGW7SGWXl5M8WvbUJOTuJczzSqsOPIXYmx4loHhG1ku0E7q235CAwIKM7pi3qBYNLSp65Zf7hMw470XIr-tUZmshSNJT8nfJ-UYryC_b2BmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی، نویسنده، تصویرگر و فیلمساز ایرانی-فرانسوی و خالق کتاب مصور «پرسپولیس»، در ۵۶ سالگی درگذشت.
به گزارش خبرگزاری فرانسه، نزدیکان ساتراپی اعلام کردند او «کمی بیش از یک سال پس از درگذشت ماتیاس ریپا، همسرش و عشق زندگی‌اش، از غم درگذشت.»
ساتراپی سال گذشته نشان لژیون دونور دولت فرانسه را در اعتراض به ریاکاری دولت فرانسه در قبال مردم ایران و جمهوری اسلامی رد کرد.
مرجان ساتراپی با انتشار «پرسپولیس»، کتابی مصور درباره زندگی خود در ایران و مهاجرت، به شهرت جهانی رسید. این اثر با استقبال گسترده مخاطبان روبه‌رو شد و به یکی از آثار شاخص ادبیات مصور معاصر تبدیل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75935" target="_blank">📅 16:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75934">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFqhwc-MPCWfrvKskQP1t5FCJu7BwLvtOXoOOR0vVOEpF2QRqiIABMbZZ1japtxHtWTjMhUfzPwK9A-swdpx35iSuRse-w7ZZ4U464GhwmQGtc4-1qVl2cOFLp6Xq4OhUdiAy5cl6dTA22BaVmFnABjeyYI4IHNVi9poRxyqelM9fddON_Sga0MNNXkBkOrNait02r37-q92zcfgm62FfOTSQbnhOy8S41QHwuX3fk8vUDd09XeE_zFoHkreD0SrW30MB0AkkFml292LeJ_QC6SqBdlbj_7V_FRYCDALYgOdsBk_ffe-ITUgjOw5ogb5qW7d0MiQYw5DHVJYtDB5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هه‌نگاو و سازمان کوییرهای ایرانی سیمرغ با انتشار اطلاعیه‌هایی خبر کشته‌شدن مهشید فلاحی، زن ترنس، در سنندج را تکذیب کردند.
این سازمان‌ها ضمن عذرخواهی درباره انتشار این خبر نادرست، با وجود راستی‌آزمایی‌های قبلی، گفتند اسناد جدید نشان می‌دهد این شهروند زنده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75934" target="_blank">📅 16:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75933">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPLgCBVp5bGdFVUegmhshEehhkams5sz4McWhEDjPE7W0WGb-XUJPehias-uRveh8VHodn1IWxQfEwtggJlCwu8io7iVoV865s8h_p9T0fgNWxTbXERzxXpq0r2tHFvmOHy5Qe_9y2PVf3Mlh49q_PDkQcJzKfteV8PLx4FV0Bq9LgkI_JpQqqMa9yxVsThvumEAsbkNwzeor_Xr5K87Meum8UyqOmGBGZ7i51g71eqrEYTajutbzbeokfhO6-SSeu0Conzah9TP-DXs81xIyoofxqs19i-BHHwyzq19N5PpqJ-tsUtRc0KvfouteHEvzbj1Ok42Ixl_Uw_4x4u9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/75933" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75932">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YetTfXDFl4VsYffkEqtMOsrzV9dMsXHsXdDZh3i1_ln88ytMum4XFoVfw1EScge08vP29PS2le9vaADNYZbTl7_kQPT4_p1chobo6eOXu9VLW4Vzn3L6w6pthpnxL8wQdXmVjSxB4vlC3tnM8d2Kuze3uUnhqKNQKaDZgLlP8bcG5S7h_eo8o_4hL9QkjLUGZ69y1zWhhEZ3iefKSsMYP6USzYLHpjf6J1RLWjo5Td7hZLkiKZSdZDNqbNRFEDU7NyCaIYrbn7tx_4IFnZPhnZukldiUhTD5hAiFMd67Cqarv903R78hnVuFX9q-N4n3fJQ-yemEMmDSCYH5bAtlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد اسرائیل و لبنان بر سر اجرای یک آتش‌بس به توافق رسیده‌اند.
بر اساس بیانیه منتشر شده، اجرای این توافق «منوط به توقف کامل» حملات حزب‌الله و همچنین تحقق چند شرط دیگر است.
این توافق پس از آن اعلام شد که حملات اسرائیل به جنوب لبنان در روز چهارشنبه دست کم ۹ کشته بر جای گذاشت و حزب‌الله نیز راکت هایی را به سوی شمال اسرائیل شلیک کرد.
در بیانیه چهارشنبه شب وزارت خارجه آمریکا آمده است: «همه طرف‌ها بار دیگر تاکید کردند که آینده روابط میان اسرائیل و لبنان باید توسط دو دولت مستقل و حاکم تعیین شود. آنها هرگونه تلاش از سوی دولت‌ها یا بازیگران غیردولتی برای گروگان گرفتن آینده لبنان را رد کردند.»
حزب‌الله تاکنون به صورت رسمی درباره این توافق اظهار نظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/75932" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=hwbPccQF1RHofU7R5Hp_lOgDo5ImoIstKF3iK68mv0sPkiF9Zl-u63Ea2ob_73Ok5Y-NXYP-DdvuI2EEhhFDVqPOGlS94DFEz6HGlJNHF_JEO_Y3SCGZhpelUgEusgLzx_CrZ6LbNl2agQHkAIWn5Awp4rjsPtKkn4eSBYLCJ7_0My4JKuh9WJZtg_5NYWjylxMKhini7oea9rVz5DP0PojwNx6erwVqiRxaITnMqr7BbbazNQ1E5HY5vvcCEwDCAyOdtF0qpLFQXnEx0YoCI6LWDqZ_ugdXKNeB0-LYEKkQxAUGzHXPGKphKPn92LmI2mruqqMnEOQg8BQ3fs2guw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=hwbPccQF1RHofU7R5Hp_lOgDo5ImoIstKF3iK68mv0sPkiF9Zl-u63Ea2ob_73Ok5Y-NXYP-DdvuI2EEhhFDVqPOGlS94DFEz6HGlJNHF_JEO_Y3SCGZhpelUgEusgLzx_CrZ6LbNl2agQHkAIWn5Awp4rjsPtKkn4eSBYLCJ7_0My4JKuh9WJZtg_5NYWjylxMKhini7oea9rVz5DP0PojwNx6erwVqiRxaITnMqr7BbbazNQ1E5HY5vvcCEwDCAyOdtF0qpLFQXnEx0YoCI6LWDqZ_ugdXKNeB0-LYEKkQxAUGzHXPGKphKPn92LmI2mruqqMnEOQg8BQ3fs2guw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اصابت پهپاد انتحاری شاهد 136 به ترمینال فرودگاه کویت از دید دوربین مدار بسته.
mohsenreyhani01
سازمان هواپیمایی کشوری کویت با انتشار ویدیویی گزارش کرده که «نخستین تصاویر» حمله پهپادی به فرودگاه بین‌المللی این کشور که از طریق دوربین‌های مداربسته بیرون و داخل فرودگاه ثبت شده را علنی می‌کند.
در این تصاویر که از چند زاویه بیرون و داخل فرودگاه دیده می‌شود یک پرتابه مشابه پهپادهای انتحاری به سقف ترمینال فرودگاه برخورد و موجب انفجاری بزرگ می‌شود.
در ویدیویی دیگر، وزارت کشور کویت با انتشار ویدیویی اعلام کرد که شیخ فهد یوسف سعود الصباح، معاون اول نخست‌وزیر و وزیر کشور نیز ضمن بازدید از ساختمان ترمینال ۱ فرودگاه بین‌المللی کویت، این حمله را «تجاوز فجیع ایران» خواند.
کویت اعلام کرده در جریان این حمله یک نفر کشته و بیش از ۶۰ نفر مجروح شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر این کشور نیز در این حمله زخمی شده‌اند.
سپاه پاسداران که شب گذشته از حملات موشکی و پهپادی خود به پایگاه‌های آمریکایی در کویت و بحرین خبر داده بود، روز چهارشنبه گفت «هیچ شلیکی به سوی فرودگاه کویت» انجام نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75931" target="_blank">📅 01:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75930">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-u6xPeoIiJ64Fod6Y0CkqV-3u6fW5-XkHBHHHssVGu-Yuv5vGnZ7N609h6MLgt3vTt-YrEMx3OHFvzqzYROtV2mw6oCgRiisJPiy6gJcpmOcjkhM_Uhzvlx1pzoUimbtrp0PATjPo5-AtqDZGvVm2sZfOA2DAsLFB4helBAsnCcQ-iRpzG6AxRPRkJo2cWMsUlsNUQPTDPE9Ik8S7GJKKd1a7GDPvezINi2SwaswhwnlyI3UOczgyAhRN4uraxmPGcB0OpKzUJWpckxso8X9n1UFfPvGmxvoISM0DvOFfbj8JbsgkrXOS7t7PlsIl8T8W6a38Q-kvOtQGatIjZ99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا روز چهارشنبه از قطعنامه‌ای به رهبری دموکرات‌ها حمایت کرد که هدف آن متوقف کردن جنگ با حکومت ایران تا زمان صدور مجوز از سوی کنگره است.
به گزارش رویترز این قطعنامه با ۲۱۵ رای موافق در برابر ۲۰۸ رای مخالف تصویب شد و چهار نماینده جمهوری‌خواه نیز به دموکرات‌ها پیوستند.
این رای‌گیری تازه‌ترین شکست سیاسی دونالد ترامپ در کنگره به شمار می‌رود؛ با وجود آنکه جمهوری‌خواهان در هر دو مجلس اکثریت شکننده‌ای دارند.
بنا به این گزارش، این اقدام عمدتا جنبه نمادین دارد، زیرا برای اجرایی شدن باید در سنا نیز تصویب شود و همچنین برای عبور از وتوی احتمالی دونالد ترامپ به حمایت دو سوم اعضای هر دو مجلس نیاز دارد.
با این حال، این رای‌گیری نشان‌دهنده افزایش نگرانی در کنگره درباره جنگ با حکومت ایران است.
سه قطعنامه مشابه پیشین در مجلس نمایندگان شکست خورده بودند، اما با اختلاف آرای کمتر از دفعات قبل.
همچنین سنا ماه گذشته یک قطعنامه مشابه را در یک رای‌گیری رویه‌ای به پیش برد؛ اتفاقی که پس از هفت تلاش ناموفق قبلی رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75930" target="_blank">📅 01:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JdJXZR7bJTinTQ5Au4idrTxkk9Zx0PX9p28Tn_vYKr4w7_EY7IxLCXFcZ7lrLB06-4YYqawiXP1EnZJw7vX3_uB-ID_X73bdG0TJB2ShAoDuMQeVFKHiaKLpoyeofothlPzSw_AzmSF4P0rtwA_-Atm-fKPQo_2lOk-gDzJ3omR3vb4yg5NoZHrn5A3f9-HWhd5MY6KFwfD225ESJJZziFJjKPEP9TVOOIHBu74Ye-e9DV_60Rj5wKODUa2Qty8MpZ-y6hm4OtNAddHa-ZXnP0weke8Ao8CcEkSbAZCXFmnKoXr78gCuBou9G3PQpDClJ4X_5_TabNO33LobVqXu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: می‌توانیم همه را نابود کنیم، اما ترجیح می‌دهم به توافق مکتوبی برسیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۱۳ خرداد در کاخ سفید درباره حمله جمهوری اسلامی به کویت و شکستن آتش‌بس گفت: «ما سه‌شنبه شب حسابی به آن‌ها (جمهوری اسلامی) ضربه زدیم، و در واقع دیشب هم همین‌طور. و وقتی موضوع را برای من توضیح دادند، گفتم بسیار خب، پس همین کار را می‌کنیم، اما ما هم کمی داشتیم شدید به آن‌ها ضربه می‌زدیم.
ترامپ گفت: «بنابراین برای بعضی چیزها دلیلی وجود دارد، و معمولا دلیلی هست که گاهی منطقی به نظر می‌رسد. و خب، آن‌ها کاری انجام دادند که خیلی… مسئلهٔ بزرگی نبود. ما خیلی سریع جلویش را گرفتیم، همان‌طور که با بزرگ‌ترین ارتش جهان این کار را می‌کنیم. اما بعضی‌ها ممکن است بگویند که آن‌ها تا حدی تحریک شده بودند، چون ما به دلیلی دیگر اقدام قاطعی انجام داده بودیم. بنابراین آن‌ها در حال تلافی بودند.»
او در ادامه گفت: «خود مذاکرات بسیار خوب پیش می‌رود. بسیار خوب. اگر اتفاق بیفتد؛ ممکن است اتفاق بیفتد، ممکن هم هست نیفتد، چه کسی می‌داند. اما اگر اتفاق بیفتد، ممکن است همین آخر هفته رخ دهد. تقریبا اوضاع به همین شکل است.
آنجا بخش متفاوتی از جهان است، می‌دانید. من می‌گویم در آن بخش از جهان، آتش‌بس یعنی این‌که به شکلی ملایم‌تر به تیراندازی ادامه بدهید.»
ترامپ افزود: «تحت هیچ‌ شرایطی نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند، هر اتفاقی ممکن است بیفتد وقتی با ایران طرف هستید، اما وقتی با کشورهای دیگر هم طرف هستید، این یک بخش بسیار بی‌ثبات از جهان است، احتمالا بی‌ثبات‌ترین بخش جهان.
رییس‌جمهوری آمریکا تاکید کرد:
«ما از سه تیم رهبری عبور کرده‌ایم. این یک وضعیت نظامی است، و واقعا هیچ ارتشی مثل ارتش ما وجود ندارد. ما می‌توانیم دو، سه هفته دیگر ادامه بدهیم و همه را کاملا نابود کنیم. ترجیح می‌دهم این کار را نکنم. انجامش خیلی آسان است. آن‌ها آماده‌اند که این کار را انجام دهند. می‌خواهند انجام دهند.»
ترامپ گفت: «اما اگر بتوانیم چیزی را مکتوب به دست بیاوریم که همان نتیجه را بدون کشتن همه به‌دست بدهد، من آن را ترجیح می‌دهم. فکر می‌کنم بیشتر افراد من هم همین را می‌خواهند. بعضی‌ها نه، اما بیشترشان بله. یعنی ما بالاترین بازار سهام تاریخ را داریم، با وجود یک درگیری نظامی یا جنگ. بعضی‌ها اسمش را جنگ می‌گذارند، بعضی‌ها درگیری نظامی. برای ما چیز بزرگی نیست.»
🔻
ترامپ: اورانیوم غنی‌شده زیر کوه دفن شده و می‌خواهیم آن را خارج کنیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۳ خرداد درباره خروج اورانیوم غنی‌شده از ایران گفت جمهوری اسلامی در مقاطع مختلف با این موضوع موافقت کرده، اما چند بار نیز نظر خود را تغییر داده است و این مسئله بیش از حد بزرگ‌نمایی شده است.
او گفت: آن‌ها [با خروج اورانیوم غنی‌شده از ایران] موافقت کردند و بعد گاهی هم مخالفت کردند. این یکی از چیزهایی است که درباره‌اش صحبت کردیم. خیلی هم بیش از حد بزرگ‌نمایی شده است. من خودم آن را بیش از حد بزرگ‌نمایی کردم.
ترامپ با اشاره به گزارش آژانس بین‌المللی انرژی اتمی گفت این مواد «نابود شده» و زیر کوهی دفن شده‌اند که تقریبا فروریخته است.
او افزود بیرون آوردن این مواد بسیار دشوار است، اما تاکید کرد: «من می‌خواهم آن را به دست بیاوریم.» به گفته او، آمریکا و احتمالا چین تنها کشورهایی هستند که تجهیزات لازم برای چنین عملیاتی را دارند.
رییس‌جمهوری آمریکا همچنین گفت سه سایت مورد نظر به طور دائمی زیر نظر هستند و در صورت هرگونه تحرک، آمریکا از آن مطلع خواهد شد.
او افزود: «اگر کسی به آنجا برود، دقیقا می‌بینیم چه اتفاقی می‌افتد و کمی هم بیشتر آن را منفجر می‌کنیم.»
رییس‌جمهوری آمریکا درباره مین‌روبی در تنگه هرمز گفت ایالات متحده از مین‌روب‌های زیرآبی استفاده کرده و مین‌ها را پاکسازی کرده است.
او افزود: «تنگه هرمز بلافاصله پس از امضا باز خواهد شد.»
🔻
ترامپ: ایران یک مشکل بزرگ جهانی بود و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند
دونالد ترامپ، رییس‌جمهوری آمریکا درباره گفت‌وگو با حزب‌الله گفت آمریکا برای نخستین بار با این گروه صحبت کرده و سه‌شنبه توافق شده که شلیک انجام نشود.
او افزود اسرائیل نیز قرار نیست شلیک کند و تاکید کرد موضوع‌های مرتبط با تنگه هرمز، برنامه هسته‌ای و لبنان باید از یکدیگر جدا بررسی شوند.
ترامپ گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، برای او «شریک بسیار خوبی» بوده است.
او همچنین با اشاره به نقش آمریکا در تحولات منطقه گفت بدون کمک واشینگتن، اسرائیل قادر به انجام عملیات اخیر نبود.
ترامپ افزود ایران «یک مشکل بزرگ جهانی» بوده و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75929" target="_blank">📅 23:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC48oWUdiJuozOQq_J8nyhiWo2BY-pQ7cK1wELB9S3_tjCVmWP1TjtzhzwjJ2TNTe5NSAFsZB7deGw723AFTxqc0-g_WpmaIBhYyV7ebr-bbM2gagNGnremdONuXA_gdahLd26u6pLCnsP-ji1LSKArq778xwnKha62VKLBFPpHpl67xheynFN5Kt5M3TqybCq23odoCehCWwCSKBHNh6OBLAE__-M_-IP9cNvn-9Zf-hfubZI954Asi8KFsGi_8dIHa9K8lg24dhjB9AYPiT2VwaORIXPNO6i2DOUuban7CNzlQsalXAkaI7zO5x3iIHmhm8T4Py7gXUQHo1Di7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقجی، وزیر خارجه جمهوری اسلامی، روز چهارشنبه تهدید کرد که حمله احتمالی اسرائیل به بیروت، پایتخت لبنان، باعث «ازسرگیری کامل جنگ» ایران با آمریکا و اسرائیل خواهد شد.
او در گفت‌وگو با شبکه المیادین، نزدیک به حزب‌الله لبنان، همچنین ادعا کرد که بعد از تهدید اسرائیل برای حمله به ضاجیه، حومه جنوبی بیروت و مقر اصلی حزب‌الله، نیروهای نظامی ایران در «وضعیت آماده‌باش کامل» قرار گرفتند.
عباس عراقچی در گفت‌وگوی روز چهارشنبه خود همجنین اعلام کرد که ارتباط با دولت آمریکا «قطع» نشده است، اما افزود که «هیچ پیشرفت ملموسی در روند مذاکرات حاصل نشده است».
ساعتی پیش مارکو روبیو، وزیر خارجه آمریکا، اعلام کرد که ایران هنوز تصمیم نهایی خود برای پایان دادن به جنگ را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75928" target="_blank">📅 23:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y3D2aIymZ6GpCHtxHKVSoY5tnkLjtxY4lkT2XxZuNcj-HTQUJ1CxeZLG5Mz8C8S1gxcdiSikjM1yRX5NHBkyNsvNk1elFDFXH1LWviemI5B9sGZrJ1nc2Dt3Ce_fWupSV9jVAtp6U9LmrC7uEvt02UovYTZFEqTN7ehclDR_MTnwjTVvhHgWtlWbSMyzdVr-YIBwZw_MBVmwuhKQL2ttEKRcmMDu3ATW5zoHW115J8-Xnm2jhwVJizzwajkegNaenxzZ5EoPUaofNIDuR3tcY5dD21qfEIs5BDKylNTtjlAoXCCxkY6cnBU1W30u-uExRk0nCFoF5nwbPYldt6Nxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام
ادعای جمهوری اسلامی
درباره شلیک به یک ناوشکن آمریکایی رو دروغ خوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75927" target="_blank">📅 23:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=dtCHLpPwvnINM4_GbnzHSPc46n4fY0vRfi8gCZh-Q2JyPleT_CR89uAiVwtjmezixsod6zUCmh5M9zET6PAdh6zWEuQAmfQsTUS46i8F18TpWbDwGT6ho9MAHnpcGIhvK9Qg9k_wmBFyBr1RfaijdxhEnJkw0akmkmriMdVv6LX6Wvs8GlrAUwGJ3HrnF2YgQmcJiZ-mSe49B8zQVNlyQm4FvQNgCetP_wHhUkD4vet4vXn0kNd6lYPymmN0kEqFbe4jHi6rs0aZjOSgW-QfSRK3opTWVQq0adO172WPd2E4JYVN3di8ACWnG961gKneCiuYO5EhBiwWf3VZiodJzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=dtCHLpPwvnINM4_GbnzHSPc46n4fY0vRfi8gCZh-Q2JyPleT_CR89uAiVwtjmezixsod6zUCmh5M9zET6PAdh6zWEuQAmfQsTUS46i8F18TpWbDwGT6ho9MAHnpcGIhvK9Qg9k_wmBFyBr1RfaijdxhEnJkw0akmkmriMdVv6LX6Wvs8GlrAUwGJ3HrnF2YgQmcJiZ-mSe49B8zQVNlyQm4FvQNgCetP_wHhUkD4vet4vXn0kNd6lYPymmN0kEqFbe4jHi6rs0aZjOSgW-QfSRK3opTWVQq0adO172WPd2E4JYVN3di8ACWnG961gKneCiuYO5EhBiwWf3VZiodJzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک‌های ارتش به ناوچه آمریکا در دریای عمان
شامگاه چهارشنبه، خبرگزاری فارس نزدیک به سپاه پاسداران به نقل از نیروی دریایی ارتش جمهوری اسلامی از هدف قرار دادن «مرکز فرماندهی و کنترل ارتش آمریکا» خبر داد.
فارس نوشت: «ساعاتی قبل و درپی نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی از سوی ارتش آمریکا، نیروی دریایی ارتش جمهوری اسلامی، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی را هدف قرار داد.»
در رسانه‌های جمهوری اسلامی ویدیوی کوتاهی از لحظه شلیک موشک‌های ارتش به اهداف مورد نظر در دریای عمان منتشر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75926" target="_blank">📅 23:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p8CY-SFrxYtblolkSV62omtZriJzKJndH7PivPFPsJvZi8HaBJYpig_-NKUUCsMnAkgoyYUTzcdrIg9rMbem1BSDy0CItdNfNPyoa69uJDB2YJODiHtlGx9fILXb8ivjkIl2bLYTKE6rq8O-Olltq3RPH7ig9HqCGgby5UO9p9-W-zO_CBuTE4j3SfWK52jX-OnktG77zyaJUw6_BveBVcDTsbsDum5M60V6j4PkwWF6nogx5vaPrii1I2eBMTtDnBAWCLUqm0Avz6lWWN0v0_SMEOV5ZcpIrI8Z2aKn87r-tZFC2p7sXx8qWi45lo9mNJ4fxe_u6AFHWs-2a_zXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TH43yBgyDeb79_yirtS_qsrRY61WCY-xQBRQOS4tqHKKhQU06debjWRaGiJaMIQ4EygRpUeB9zXCZ6OApIR_ubqmOFn0-Oo7ygFV3rZfUIb_hGeJ1WqdeU3F_5hgmYTTxA38JFauxXxmT3eXgD6WNrwVDgnCM_4D7p9f4QyMlsLuXDV4h-dAPoGEe48Uluy6z6Myzy194L9P1lvog2bnG_15IbPJmWdQokMZujB1znlXBW7JB3t2_xg1-EbHWyzfgr-RMZQui74pznfjdkRK30oRqxHK7CtKk47GHM2dzpWt-wCB1vyAUOPBz3voJTYZbhDEp-XQaABTf0TvuTHqyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد ادعای جمهوری اسلامی مبنی بر اینکه به ترمینال مسافری فرودگاه بین‌المللی کویت حمله نکرده و خسارت ناشی از یک موشک رهگیر آمریکایی بوده، «کاملا نادرست» است.
سنتکام اعلام کرد جمهوری اسلامی با پهپاد به این فرودگاه غیرنظامی حمله کرده و این اقدام را «عامدانه، محاسبه‌شده و بی‌دلیل» توصیف کرد.
@
VahidOOnLine
پیش‌تر:
حسین محبی، سخنگوی سپاه پاسداران، گفته است که تخریب ترمینال فرودگاه بین‌المللی کویت «ناشی از خطای سامانه‌های پاترویت آمریکایی بوده است.»
به گزارش رسانه‌های داخلی ایران آقای محبی اضافه کرده است که سپاه «هیچ شلیکی» به سمت این فرودگاه نداشته است.
او مدعی شد که بنا به تحقیقات سپاه: « تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.»
در نتیجه فرود آمدن یک موشک در فرودگاه بین‌المللی کویت، دست‌کم یک نفر کشته و چند نفر زخمی شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر هند نیز در این حمله زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75924" target="_blank">📅 22:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOwruF5Joie39GNEZdf2rRard0xe_DxjXuFFbKeOO1uvUdbZf4gZjLVI5oBGKM4Lu5AqPxU-Zt-g5vRnDR5075XBUPKE_3DuecW2w_wJ6CuJKU8JtqKS_wXUYJZHI4IpYfZcMP89ndT9_p7FtHCOheizbHivK81Dr-qSTrvB14seGGrX1egJo34x9oAsflKtRwOKWeRQ6MOy-wbrNC8UerTOBhApHIHxTti6raCMr0Ej6_O9iQb6rrpqiexXkMMf6t2sFDuuPUjrrNRGO3JQ4kMJeqYBDOvVwziZHpopAzVUxpAj_n975IH3RJlDaBHAI_F324QY_4y1iSMnqmFXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CahGckeRAUxoX_5r1JepXd84X7DTZDc-QCEaNOhVCmO5cIZDNz3JiqHXJcN7p7MpUJB_wvyUc6gyhwiATYDuW-w_OZlUrsr_VqsPZP5yPSbgaldKkXOBswINm2dAmjqtVTuxmOglYLsdQAGL0D6v72oefyq8jjkSJanXq3t0Io722DQ0To_CQ_38rpphc2crhVWcb9SdbgTyT2wfnlA7vvZnY1tzM0pZkuSbfbZos5mmAlqCba5ctmrE9G8uhGuueUzRUTc5qYyT6xGbBHtfcBNeCE_4f5nm9yia1PTM_r5zz_qlJS-V15ghsIflraV8IM_V4p47pjPoIT_qkgPHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RwKXNHKHcque-Q73Dvbhg_H0zAdXVuXBlCH32V4SIxay0NSgNzihLSot-P7cAC1hJKYQGqp5-CbAGP3zqEqJ-5UTLvSFTMp6pAt36ihUjVWkeDbO4nyj0kwS5uXefT0JsxC89uh1hDa2ie_TWFXS2IkyUwnVChJVPVBbNEOiXWgPTzsxT3ZXow6P1eCzroDuuxoGJBWPamxXh502hI3Smnjl5B9ad03HWFoehhEHsL-GoNkL6nX6OLNwU9gxfjTxjszYXVQRjYxDupmp9dhbZTuCytekB8jmwin7CHy-tZ-okVEyqdGC-X-MX9n3Xx6LMILKR6P2tq9kOPzCbGuN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I-bh0fB8cZ8G1OKz3RfXIpSpHnZf-H2ssI8q2XzySF89gloGcmm0d9_82QSNWONGtq7VORDtIsDVtfETC3-WAqsPXjRYNorrcE2fCJeFQOV4KmdMItNuIg2noGU8WQbFHMmcVVqW8XTF-dsy6CQpeSzTQLt_8lWlaObiA_u9PzrEnBKhIkLK_IWNnv1ndlmnTWU6hePlt95_fAexbm_4VFhG4fbGQYnxVuODzOxdysDVp3CI7S0qbsO2heoa0cnle6VBnCAPmxxSSWbESlNrCCgKVtZYDdsD76X0XvTFxkqd95pLNZGkF2mbzjuAwA0-eZDoMGKK2tYL3MABs_7tNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v1T4UQrLTJ6_IT7FwucGpjqJCDBnGI1SVevb28705cJgP2gJw3JqqoN4Et5gMxsLJeHFWUUopybIS_RlnVV_oSlx5Ras3wmIyeMvZqkt2-U2r3p29J3kETTwsadv5SxIjq8obJXSd_3Rcl8evMA2A-iR29Ei2Vi5vVCvwTK8j3NftURd-3Of3lMJkAuuWOLvTBJRnmN6QRXXYgcEZXSH-Op08EPRkozbq2ZvkHSfhclm03iS_AyliAPD1WZULKEIklPGmm-o_HFpp77AR0ACgj2pLfeiDumg43MtnlSJuNnZQK1ZtjLlKcMAquECD7AK-cPOn2I_fy0mNIp5tVRpgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PzLMr8-SxbB-IZK-Dq0_uO-mgn83VIt13dM-OzKIXlbS9rHwpPaCHf-3H1g4l6SajcKhX4mW_GajrAHzVtcI0jXTSu-xblVK7XvUcP12MF0YZCME9DeJyR_BGcrsQ3RHJQe0NaOZngidjpwS-NtIqdgTb06tiORK5MidvpKmGO5yc0vHjcDbHFx8nPQX1QeCHOx5ab5RKy3zo6yr60RLMdlRXl_tp4cJqB7w5qDW_DSziLNYGeMKi08Qh-644K1LxB5DHuJuKbnpwFLOH2cYzGKEivpBUnEu2qhRyrLrnvhPADu4fG8e2HEcsd69Mjfaw_Yt4DCWbYkxGc_MRRXv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FOMEClG2XnaZCOMEQjGZSIN6RPafD3fbZF1yGp8QdYdUi_c9BSWf0Ezd17eL8qA49W2dWFu00ol1IsY1nMRWOmBE69Mgs5RPGe3IzVHdaIkpoCi77v7IEQ4BzSUT-Y7GsPUCtZcg-JAWZ3kbkTjIteRBtk096J3Odb7Bc8cx-emS3gj2OO5W24tBEvTWl579z7MPagQsU8QhqkmIgZV2oBPrfE7A741MdGUux-8wc0EjOQtDpBXGu0M41v2eKtzUT5REQwqLdZWfgzWLkeMhSDhGaWDEtTFwoK4R1zNWlnanVq_vzvpJy6y-RbjIO8uSMJsMNXBqWyRXFuIcXy0KpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DXGEwhZHdacDeq9clgVLxNe9jX8N71HPX1R8HLFGXYi2OwAPm6GMJeXUql1bY6BdV-vtqSCMaHFehhp3juvFqGLutb7HFpGqnr_sD0d7LAzoSfCJku3GwquKe6X0SQpFOulOKfv8Yn8Xis05gAw1wFHC_zgunuQ_IWbS4TUKnGJwsqJSCRMXVN3eklSZlhlvZQLgS3HfX480ZmtSenqQ8QP3fYesOwxdbOyUdPh5ffiQpPteYem69vDKJrusNrH3SQinLlMcbX32SqccBTulYcJyKeUq53UYz69-iX3ThmbgEzqVI3yVaUqmI7YTTa0GQl-T7XZigfl5EQKpkaUcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mvw8CdklF0aOTv6IVORrmltAdqtHjsJfxq_K9cwFoZY6t_SimhoCM7rY-kUqNqGeX9VL0LvEXQIYbO3auIFw14E1_q3Kokwzzs7RbmyWw5uW-lk9EZyvIRi0KM_dq_PgLb5klrIpxylVTd8olQRdUcO3sEmkpsL1uY0aEadw2wSSPB9wMtMk5A_A_mA2QBlAorDnFTus6n0kA3l7hL8t4hbKVegI3qbpVHFiwGJPXc5r2a6aXLpY9IiVJHmGsljZdXb_gfMdozRPWkz1cVYdCdwSfF6NrndD7ts_p9nUg0XUYrF67GlSVfQS5mm-zyLMDx8AC3Ic3kFsMDOVB_WY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IHqLQP2_clu1Dgin9yFZOB_OWGs7E4cM2Vjp5ifhgY9wCyu15a0N_Ddoa-S1YUb3UlNx0TVJgR7w9aeJ7YBLGRGJfXYijYG_L9L-9TUubQ6gpeYpbzgEDcFIQ9ng2EHVRnIfUJEhPX1pbI4e3hjLusrd3jkkdYfPcKliQOTMe5yIC_Q7zCFzqE-AtB7fGo5r8UN80PBAowJpXc5geDi2aeXvCtX0TS2xMsdaBPZ0JI1H2wW9T8GrIcu3-lPdhhmqPKxcanVdb7tq_i0l9o-GkI8N3kwq-WsuvEWha8HUsCvo6B3Yq8GtmIoJ6j5K8758vhpPjxyPpcW9HrrxqP0KBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دادگستری آمریکا روز چهارشنبه اعلام کرد مدیرعامل یک شرکت فناوری در کالیفرنیا به اتهام تأمین تجهیزات آمریکایی برای نهادهای هسته‌ای و نظامی ایران بازداشت شد.
بر اساس بیانیه این وزارتخانه، جمشید قُمی، ۶۳ ساله، شهروند دو تابعیتی ایران و آمریکا و ساکن نیوپورت کوست در ایالت کالیفرنیا، به «تبانی برای نقض قانون اختیارات اقتصادی در شرایط اضطراری بین‌المللی» متهم شده است.
او متهم است که «تجهیزات پیشرفته شبکه، امنیتی و رمزنگاری ساخت آمریکا را برای مشتریان ایرانی، از جمله نهادهای هسته‌ای و نظامی حکومت ایران تهیه کرده است.»
وزارت دادگستری آمریکا همچنین اعلام کرد که جمشید قمی از «شرکت‌های پوششی» در امارات متحده عربی برای پنهان کردن محموله‌های تجهیزات شبکه و رایانه‌ای که مقصد نهایی آنها ایران بود، استفاده می‌کرد و این شرکت‌های واسطه برای مخفی نگه داشتن مقصد واقعی کالاها و دور زدن تحریم‌های ایالات متحده به کار گرفته شده بودند.
جان آیزنبرگ، معاون دادستان کل آمریکا در امور امنیت ملی، در این بیانیه گفت: «طبق آنچه در کیفرخواست آمده، قمی با تأمین فناوری آمریکایی برای سازمان انرژی اتمی ایران و سایر نهادهای تحریم‌شده مرتبط با برنامه هسته‌ای ایران، به ثروت دست یافته است.»
او افزود: «بخش امنیت ملی وزارت دادگستری افرادی را که برای پیشبرد اهداف هسته‌ای ایران قوانین ما را نقض می‌کنند، پاسخگو خواهد کرد.»
به گفته وزارت دادگستری ایالات متحده، متهم بیش از ۱۵ میلیون دلار از ایران به حساب‌های بانکی خود در آمریکا و یک حساب امانی منتقل کرده و به‌دروغ این پول را به سازمان مالیات آمریکا به‌عنوان ارث خارجی اعلام کرده است.
بر اساس این اتهامات، اظهارنامه‌های مالیاتی فدرال او تقریباً هیچ درآمدی را نشان نمی‌داد و بالاترین درآمدی که در هر سال گزارش کرده بود تنها ۲۰٬۶۸۴ دلار بوده است.
وزارت دادگستری آمریکا همچنین مدعی است که او از درآمد حاصل از «طرح دور زدن تحریم‌ها» برای تأمین هزینه ساخت یک عمارت چند میلیون دلاری در اورنج کانتی کالیفرنیا استفاده کرده است.
@
VahidHeadline
دادستانی علاوه بر درخواست مجازات حبس، به دنبال مصادره اموال وی از جمله عمارت گران‌قیمت اوست.
بازپرسان معتقدند او به مدت بیش از یک دهه از طریق شرکت خود در تهران به نام «فراز پرداز رایانه»، بیش از ۲۵۰ تن تجهیزات کنترل‌شده تکنولوژی را به‌صورت مخفیانه خریداری کرده است.
او متهم است که با استفاده از حساب‌های شخصی در eBay و PayPal و از طریق شرکت‌های صوری در امارات کالاها را تهیه و به ایران ارسال می‌کرد.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75913" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D0UtU0Q9VVMm_L6VyzrHobSPqN34X2UK3B0mtfQNkjWRf9t1zfo-hOWTz4oJT2qAvAjzksg93V0aks_mXj9u5ki94WkKo61OFc09pFvkZ623EfUywdVP2fK6EK9N00vF5aLNHnWWIIj5cOJXD2vRRjo-BoqPndXDRcYrJJvBWcrCT4YD9IilFRzBsQSleRx32jZy4Vqvh7ktQYalGIw7caCLnbgxm4DcrHzw1FJESS1KZq9c3SBZN3ZSpcF994cdn8YevhO7MfOhJKWuxWziN9Ya6XWxlZzBKZxEcHM6QQS5KOAHdjqyjZjgS-VF5LnSrdN96C5PcPEKBorAPYvSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tCfqt_xhV6NDjnQlC2vcq0viFGDplVXs6LDi0G1rCtOGH_iq8hhePaB65Lo7yJd7JldHDNMBj3eXpln6B-RKW39K7b5NUPNE7M0ygRR8JZiYCHVTcmDqngrk_kwjPzvTM8GRio1vRxC2ngdxHnlo8_XnqXGui2YMs4tDCgFGvARDyTIYzfki6PA4S-QxsVrg_rt5ug3AE27ksK9PjqRbitK_xI7OcDvEE1odVvEYFdijeXxD9bF3ZrMw34uOtjbP_p9bDefgHxcPPg_Lj23M6VqSrxF_tB5AjdboUJxEPKbZBTVI2mgSlFBIWxw9L2vftBS196xYFIeHYECpL2k3oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌ان‌بی‌سی، ترجمه ماشین:
▪️
نتانیاهو از پاسخ به سوالی در مورد اینکه ترامپ در تماس تلفنی این هفته به او فحاشی رکیک کرده و رئیس جمهور آمریکا گفته است اگر او نبود، نتانیاهو الان زندانی بود، طفره رفت.
نتانیاهو در پاسخ به سوالی در مورد اینکه ترامپ ظاهراً او را «دیوانه» خطاب کرده است، گفت: «وارد جزئیات نمی‌شوم.»
[ولی ترامپ در
مصاحبه با NBC
گزارش آکسیوس رو تایید کرد که بهش گفت دیوانه]
▪️
نتانیاهو می‌گوید او و ترامپ «اختلافات تاکتیکی» دارند اما «در مورد مسائل اصلی اتفاق نظر دارند»
نتانیاهو هرگونه اشاره‌ای به اختلاف با ترامپ را کم‌اهمیت جلوه داد و گفت اگرچه آنها گاهی اوقات «اختلافات تاکتیکی» دارند، اما «در مورد مسائل اصلی اتفاق نظر دارند».
او گفت که این موارد شامل جلوگیری از دستیابی ایران به سلاح هسته‌ای و تهدید اسرائیل با آن می‌شود.
او گفت: «گاهی اوقات، مثل بهترین خانواده‌ها، این اختلافات تاکتیکی را داریم. اما ما همیشه راهی برای حل آنها پیدا می‌کنیم و این کار را به عنوان دوستان خوب انجام می‌دهیم.»
او گفت: «ما می‌توانیم صبح اختلاف نظر داشته باشیم» و تا بعد از ظهر به زمینه مشترک برسیم.
▪️
نتانیاهو در پاسخ به این سوال که آیا واقعاً آتش‌بس با ایران برقرار شده است، گفت: «فکر می‌کنم یک بازی تاکتیکی در حال انجام است.»
نتانیاهو گفت: «و ایران مطمئناً می‌داند [ترامپ] چه گفته است، اینکه در صورت لزوم، بازگشت کامل به اقدام نظامی وجود خواهد داشت. این تصمیم رئیس جمهور است، اسرائیل آماده است، و نیروهای آمریکایی نیز آماده هستند.»
او گفت: «فکر می‌کنم ایران باید این را در نظر بگیرد. فکر می‌کنم آنها دارند این را در نظر می‌گیرند که دارند با آتش بازی می‌کنند، این واضح است.»
▪️
نتانیاهو از اقدام تلافی‌جویانه ترامپ در محاصره بنادر ایران در تنگه هرمز تمجید کرد و آن را «بسیار مؤثر» خواند.
او گفت: «محاصره معکوس، یک حرکت هوشمندانه بوده است.»
▪️
نتانیاهو گفت که «هر دو روز یک بار» با ترامپ صحبت می‌کند.
او گفت که دو رهبر «اهداف مشترکی دارند... ما می‌خواهیم به آنها دست یابیم.»
اما در پاسخ به این سوال که از توافق آتش‌بس احتمالی چه انتظاری دارد، نتانیاهو اذعان کرد که «این یک سوال بی‌پاسخ است که جنگ چگونه باید پایان یابد.»
▪️
نتانیاهو گفت نهادهایی که به نفت ارسالی از طریق تنگه هرمز متکی هستند، در حال حاضر «در حال توسعه مسیرهای جایگزین» هستند که کمبود عرضه انرژی ناشی از بسته شدن مؤثر این آبراه کلیدی در طول جنگ را جبران خواهد کرد.
▪️
نتانیاهو انتظار دارد که تغییر رژیم در ایران رخ دهد زیرا رهبری فعلی «به شدت» تضعیف شده است - اما پیش‌بینی نکرد که این اتفاق چه زمانی رخ خواهد داد.
نتانیاهو گفت: «شما نمی‌توانید دقیقاً پیش‌بینی کنید که چنین رژیمی چه زمانی سقوط می‌کند. شما در بسیاری از موارد آن را پیش‌بینی نکردید: نه در رومانی، و نه در سقوط دیوار برلین، و هیچ‌کس آن را پیش‌بینی نکرد، اما این اتفاق افتاد. چرا؟ چون ترک‌ها از زیر در حال گسترش بودند.»
او گفت: «در واقع، شما همین الان در ایران شکاف‌های عظیمی دارید و نمی‌توانید پیش‌بینی کنید که چه زمانی این اتفاق خواهد افتاد.»
«اما من دیروز در یک نشست عمومی اینجا گفتم... ببینید، من معتقدم که در نهایت این شکاف‌ها گسترش پیدا می‌کنند و رژیم سقوط خواهد کرد و ما تمام تلاشمان را خواهیم کرد.»
نتانیاهو گفت: «من فکر می‌کنم که ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تغییر نکرده است، اما دقیقاً در لحظه‌ای که ما انتخاب می‌کنیم، این اتفاق نخواهد افتاد.»
او گفت: «فکر می‌کنم آنها به شدت تضعیف شده‌اند.»
nbcnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75911" target="_blank">📅 19:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LNDMYQScGsIdu6I2aHFaTqkWHB5mwkwZJ0nvwgUH9ZVnpVBtvqpw8WQ3kF_xq73ex8mV4l1EZUWIgrImVSb6zvAR1bzyWAIJY9AGOa3pAFVv0E2ua2Aai_GJIPy6vaCgDq5Wxmg9Ik63uW51Z8THFgMqH2iJsUD3QInFXAuHaW8fY_8Rb1VDq4GgUMKpliS_TIubbDCzXzDielCaQEk5FaTmrnihW3YhFrzyKEl9NqiKkuoeeFBITdPHE8amV4fi0KZX_PE7sjYzbpvRMfsX4PEG1EmypJMrNnv3FLDlOT3KQ5vRIBxRmhjyDZR_BJR30sVk5KKoy1dR2LumArdQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه گفت که سرنوشت ذخایر اورانیوم ۶۰ درصدی ایران در مرکز مذاکرات با واشینگتن قرار دارد و تهران هنوز با یک توافق صلح موافقت نکرده است.
روبیو در جلسه کمیته روابط خارجی مجلس نمایندگان آمریکا گفت: «فکر می‌کنم اکنون در برخی از اسنادی که میان دو طرف رد و بدل شده، این موضوع به‌طور واضح مورد توجه قرار گرفته است، اما تا صبح امروز هنوز تأیید نهایی از سوی نظام تصمیم‌گیری آن‌ها را دریافت نکرده‌ایم.»
روبیو در مجلس نمایندگان آمریکا بار دیگر بر اظهارات پیشین خود مبنی بر پایان جنگ با ایران تأکید کرد و گفت: «ما دیگر حملات مستمر در داخل ایران برای تضعیف توان نظامی آن کشور انجام نمی‌دهیم، زیرا عملیات "خشم حماسی" به پایان رسیده است.»
روبیو با تأکید بر اینکه آمریکا به اهداف خود دست یافته، افزود: «ما پیروزی را این‌گونه تعریف می‌کنیم: نابودی زیرساخت‌های صنایع دفاعی ایران، کاهش قابل توجه تعداد پرتابگرهای موشکی که در اختیار دارند و کاهش چشمگیر ذخایر پهپادی آن‌ها.»
او ادامه داد: «ما به همه این اهداف دست یافتیم. علاوه بر آن، آنچه از نیروی هوایی ایران باقی مانده بود را نابود کردیم و کل نیروی دریایی متعارف آن را از بین بردیم.»
با این حال قانونگذاران حزب دموکرات در این نشست موضع آقای روبیو درباره پیروزی آمریکا را به چالش کشیدند.
از سوی دیگر ایران بامداد چهارشنبه کویت را هدف حملات پهپادی و موشکی قرار داد که به گفته مقام‌های کویتی باعث کشته شدن یک نفر و زخمی شدن دست‌کم ۶۳ تن دیگر شد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75910" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75909">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۳:۴۵
سلام وحید همین الان بندرو زدن فکر کنم فرودگاه یا پایگاه هوایی بود صداش زیاد بود جوری که تا شهر نمایشو لرزوند
بندرعباس سمت اسلکه صدای انفجار یا بمب
وحید جان بندرعباس صدا انفجار خیلی بلند 13:45
بندرعباس رو زدن خیلی بد بود این دفعه صداش از همیشه بیشتر بود خونه لرزید
سلام ساعت 13:46 بندرعباس صدای انفجار اومد.
غرب بندرعباس
بندرعباس صدای چندین انفجار سنگین همین الان شنیده شد
همین الان بندر رو زد
سلام ، ۱۳:۴۵ صدای ی انفجار با لرزش شدید بندرعباس
سلام 13:46 صدای انفجار بندرعباس
وحید بندرو فکر کنم زدن صدا انفجار اومد
سلام همین الان قشم صدای انفجار شدید اومد
هرمزگان صدا اومد
بعدش این خبر منتشر شد:
"معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان گفت: صدا‌های شنیده شده در شهر بندرعباس ناشی از انفجار‌های کنترل‌شده مهمات دشمن است."
(گزارش درست اینه که: صدا شنیدم.
از روی شنیدن صدا نمیشه گفت "زدند"، "حمله شده" و...)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75909" target="_blank">📅 17:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75908">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eBfh-9KMqtBL75_AEpiPeZ4k4Vt4PYU6KhgFi7HWAkMoMAiKdo5fUGvnaba6naFfWW5EBS-7JGa8UaKn_ubgVCdtE1XTzngBEg7aDWnFuiNGq_Ss7Yzcosal6Qdr8os8K9PwtT5DGE-lZeFxfyZSu_ctXnrAVXEa9kTOz4lO2tIw75l1P79BZYgPcSf5Fqb1DQgvvEQu0HUrZxDprcHUh0RzU96HdhBsgJCjE2_v-B2HD6V0oktzZU5ctovHJOTwC5_g9sPmslnfPMTbfB2LtbmMCXFFxcn_PkIQ8C2qztJr_rtoKIKz4yFXIIfTFUWIUkZF7XHvlv1OYTZFl7Ynyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم جلالی، سفیر جمهوری اسلامی در روسیه با اشاره به سفرهای علی لاریجانی دبیر سابق شورای عالی امنیت ملی به مسکو گفت: سفرهای او، به جز دو مورد که خبری کردیم، بقیه محرمانه بود. یعنی هم ما و هم طرف روس، سفرها را رسانه‌ای نکردیم. فقط دو سفر اعلام شد.
جلالی به خبرآنلاین گفت، لاریجانی سفرهای محرمانه زیادی به روسیه داشت و در یک سال‌و‌نیم اخبر، هفت بار به روسیه سفر کرد. جلالی بدون اشاره به دلیل این سفرها و موضوعات مورد مذاکره گفت: «در یکی از این سفرها، طرف روس با من تماس گرفت و ابراز علاقه کرد که سفر رسانه‌ای شود و آقای لاریجانی هم مخالفتی نکردند و خبر آن منتشر شد. اما سفر آخری که در ۱۰ بهمن‌ماه ۱۴۰۴ صورت گرفت، به شکل دیگری رسانه‌ای شد.»
جلالی افزود: «ما دیدیم وقتی هواپیمای ایشان حرکت کرد، سه یا چهار هزار نفر در فلایت‌رادار آن را تماشا می‌کنند. زمانی که هواپیما در مسکو نشست، این رقم به ۳۴ هزار نفر رسیده بود. برای فلایت‌رادار، این عدد بسیار بالایی است. بعد هم یک‌سری شایعات شکل گرفته بود. در ماشینی که ایشان سوار شدند، به ایشان گفتم که این سفر را باید رسانه‌ای کنیم. پرسیدند چرا؟ گفتم با توجه به حوادث ۱۸ و ۱۹ دی، الآن عده‌ای از ضدانقلاب‌ها تلاش می‌کنند این خبر را به شکل دیگری جلوه دهند. برخی نوشته بودند که رهبر نظام به روسیه رفته یا برخی گفتند که پول‌ها را به روسیه برده‌اند و این خبرهای عجیب زیاد شده بود.»
جلالی در ادامه گفت: در ۱۰ بهمن، زمانی که علی لاریجانی با پوتین ملاقات داشت، در پایان جلسه من گفتم اگر اجازه دهید ما یک خبر کوتاه، با هماهنگی، منتشر کنیم. به این ترتیب همان دو سفر رسانه‌ای شد.
سفیر جمهوری اسلامی در روسیه همچنین گفت: پس از کشته شدن علی لاریجانی، پوتین متن پیام تسلیت خود را آماده کرده بود اما گفتیم منتشر نکند تا اول رسانه‌های داخلی خبر مرگ را اعلام کنند. [چون فعلا به مردم کشور خودمون دروغ گفتیم و ضایع میشه!]
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75908" target="_blank">📅 17:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75907">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy1C0uVi3PC0t5EJvdSKrnnRACkKGnqK86sX0_z_Lfx-JDkIm2EPURSimo9RF9lhTzTvynXvvbLMOl_w3ow21dq6R4HyzR2LIBKNiqM1b7U3faLfgUni8MWGFa0g7QARGKmAN7QPo14c_sOOjIvdZq45qeCYTuPF__KxKMz7PZxsUuFKoVVgXTfpdls1YSyC743TYdtKD2cA4Wx8NIc5vGi91tZZv5WI4aq0w-2Eo9prqBBGZb8qEUm8sby8WrXGZk9uVu4a5hdiBZwex4fiMWfMys_UiFs2xaFqPRrhwXoubf_6WTTpKjnpEhBPmqKwZOSc7WWsOrQucAQQ6Kwiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌وگو با پادکست «پاد فورس وان» متعلق به نیویورک‌پست گفت که جمهوری اسلامی موافقت کرده که سلاح هسته‌ای نداشته باشد، اما همزمان یادآور شد که تهران همچنان می‌تواند «نظر خود را تغییر دهد.»
او در این مصاحبه که روز چهارشنبه منتشر شد، گفت: «ما باید کاری در قبال ایران انجام می‌دادیم، زیرا صرف‌نظر از اینکه وضعیت ما [از نظر اقتصادی] چقدر خوب است، نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای داشته باشند.» پرزیدنت ترامپ اما اضافه کرد که «آن‌ها از قبل موافقت کرده‌اند که سلاح هسته‌ای نداشته باشند.»
وقتی در این گفت‌وگو از پرزیدنت ترامپ سؤال شد که آیا رژیم ایران با این شرط موافقت کرده یا خیر، او تصریح کرد که «بله، آن‌ها با این موضوع موافقت کرده‌اند.»
او اضافه کرد: «منظورم این است که آن‌ها اکنون می‌توانند نظر خود را تغییر دهند، اما این یکی از چیزهایی بود که باید با آن موافقت می‌کردند و موافقت کردند، این موضوع اصلی و بزرگ بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75907" target="_blank">📅 17:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75906">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSKXGrsq5jmu-CQzABNY9yIoQGwI7gVJtE6WC3mRZ_agGOUxveZVVZp64U9VBrEMuJ_hsQ4v8mh-xVxoFg0mKU5YOeiuo9O5bKRQRVMnHKgaMVYKMY2SXmVX9m2xt_2xn9sm460R8QZ9csuu2Z-VrT4BOiBr1_JLGnmjcWvZv_oj7cHs8gFvkqZ5EzR-FkhyhQ8xSQw6xB8LEFBGYri8bFh_wzHoO3n4-C8qKs8qUF5n_ybQbs8jXabHTyUkxGMd1eZOWJ9Y4plGbqtKPTFSF3NNY64_jXloGvipPlbPJx14aRROXCWNmI8jXCgY8ue0WPTBDCZcLkMXDDAkaIjBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید این کشور مصمم است مانع از تلاش ایران برای «جا زدن» افراد مرتبط با سپاه پاسداران در کاروان تیم ملی فوتبال برای شرکت در جام جهانی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75906" target="_blank">📅 17:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZyEcLLyC1RgXzK7fmcZp89EdWsO8tzDLjrXOlJ-oE3n-PxXjiRJ2GqNrUxwBdaXEOH0cR1DXoHEpJ2WXYEoS7EWjEds47O27cOTvcY4TRtrRfuLh2DxQ8CBw4nLDeXDMu03fTkhtE68w1-W3Ya_Kj2TPpu_IeG0FKxAgjzdT5LrDza3DVrJKG1bemDFPOkNO7rGslr_7x5UJDy-yC9Ze4Vvcl9a0Q1Gp2Gw_-9WXyZ8fdoo_U6tnN5mriTSKEhuq9NZ4MrY82YbxOV0aI1HEprmrhttrYgCf9GY27D25jH0vSWi3EenuXKyRhStml3FJZC3xpcbDBTWUL9T8OV1cow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SVefYuT8OZF9v9La_nsd0_5tT0YJ3KLtJXRhQswd1oee0_QRkGCbgQrBSPbjNyqMlXVNs1l7vmn0hzmwN3cnCHuWZuYRRgqXM3eMk8-E8uGlOGlJQSYV3AgcSB5yRdgTlxVSwZVgF52PfSaM7-A-kGvS9GJoM4yWtdHiiEp3exAEB3sgUAtxn8VKcCXHz-5aS75pfyozIZHzDS9dx5dF0uaE9xY16lKfgPCyi2FyzPum2l4T9JqXcf5cbohjO9osa3QdHmQA2z4h8OEQHaIOyCHrLl6l9crAjd816spJWYgTG2TFpKLVBvu5crvAKCCYwD_6HwP8_hBq0tz_8bD3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lzdrFsNzci27K2G12bRz6aegXHOVvMkwcZ82n63IeYt9F_GitS1qyq06UGr4kGUw_en81LCO0L7FiS8HOtP5Ow9dzTpsXXBfBfW0_G5m86Pmtb5uHvLctpIqEnpjl-9Dffqfe3rgiA1wQRJmeVwblKfFwH8QNF5q0eR7_YtU28Y9m0dgGlQpm_8adywCKwpgOZZSqpeOSadXgHhxnDUQXWvr4ZmzwRBAlhHG90lxvDI6M5IsKOPKthVKAlzbVcsf341pFfma_EyQnsk_llRQjj_UWiC-o7Os8q98xm1db7uSiTFU0eZjwHJGJFqaWcQ4tcEYsGjvraMjzqpdZaESHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ao-AwZtT-SZPysjMFrGFdar3eI_HecGtZumJKJRR02PGwwXrLQ2wQVrPxaKE_D3BWtHNqnvcczIJt_3K44Eq7Yzf3LBA9iyMXYeCraPQLkfGHhWU2Vou5JEjSDUDTmWzUi1bz-L3RRw_IrPiopVxh-4ENcI81XnlA-RsXG4tyVjYGypHw0NuUcjT5pX1e1b93EZ8Xu9g_NCHDU5uPOx22euBgT8_Fde2NRbiravT1oPmvSXP6V3UeO23oO4jcb4x2uBjF6q68NbSA-SwAEfbadWaer079sae1UJOtww4wujTUjg3cxQYZUdYpUWZjpptaDUEGup2nHkY0-4E-POyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W74tDh89y18zHbfcc6ojWmJCHsHFFlOB-x8xoddVuldB1W8RqexHUq1CRuYBW99GDoz1whK-SqfmpXE-yHLweecfczcn0kP1CEEQ6Au0S2WN-9aQVU06z1PfLNllqu8_GZaLVfXjMZMWt8OKwMb0J9cIloEzNeoF-McqDGH-uGocsqXXdrZcZOQ3NFCZxj9Hw6IaEn0_w2qgsFVjLJCAi_hJlOVI3zhcG9rKsQZ_xHIjrVWVz4PCYr_CdWi9ZF4H-F96U2j-eulXcuC7wxl4w95NyT2kAg_WAazFyXGLYgz60pq6Ox5eB-cB6tjk20zGNDwGelGTwKrpUI9h2KlcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KSY90EQOjf6I3qsFO2XOQP62gXuqPEJ8kp74-ilYxkTzUrIDLWSO7w3DA3XywEy6SyE9EY3FHKE30OLeI2LQVGsbXPRu4ehdle9Gz_LqkNT33eX9R9PfA9E5wQA2mmRzWbhH3s7njEU8cae9zUvxf9pHvV-PL_1EMzmXubJ2LR6Oxjiv9urtJcsvriJA2igycu0fgwvJ6SvcKojneV-GvSZbfsgGl3LuFo1JLjytrK3sgY43zsWOcwAQCKhQ_p25WfFQ-DemInyOE-8Tdvzm4sTTBVumkepyUXB93S3eD3-XMJVuzof0uQtvsYF19oqBmieOz6y1fvTwHMs3NOBdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VUZDL49I5RoPY6I2moLC_tx6_mA0qt_EtsrwDcciJaxUZaGXtmFhR5bkKC_x2MbHoF5giq_dO_KIpiMIImDwRMYVX6l7SsRSa73V14iW_Akn9NwPuRBGT5EaXhGXwzXEO26fO5N0iIXd0EiKAY9NnVwBMaWt9votSyKT_cLMKseLPWZYDoylmKLT8IPTZGdUYf_ZfXX9_XIuYIRyH8jVmnALlZjFUMH4-3PzT8Dts9XhjFX5bZ6VmEGr9fp-Qp61oXn0jfJ7SnXopcKL4Djh7lJJeQDI3dJtjbrPoWNJChqa2aMnY_l71o2DYvKbJlY9vnuhLwd-1i1eBYpZGbEsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j0D4W81BxVwoufYH4tjf2xIc5ecy1-GbGFps_74-_N4JLTqjYSLQ2Ht7TNx5qwG-7cvv78wrNQhW3rB0hd-qobzCDzveDUYsQR3EKGx1iuKVWe5ZsSGuEAitQ7-VxgvGA5lbLZNsEwKvWaRxns-imSsfmZSFBZ3z9RmvbSsw9cNl9nkXRAWcGMl_K2IYqPoG7vr1CRRQeBczytKDN0kmAQyqgchiBhv3EDXDt4zFLKdA00EsrJ9O2xFo1vNEURco7rbbS1UV-2HJerGpnLhGwMMJjmyCEh52ZoYPPxsa6zZ1zvJpB2veT4C0454VK9s9_vPr89mEymYHCXYjU39mMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=IY2ZtJ36j6DhUFOH8IHGmpvXdKpnQ-AkDN_EFqmBTJVW2AreeDcddWr4kEs68X2dg0bGCCi3BENIezSxDzZZYoy0ns9LJIuECIUBzOLrWpGZETK1GE7kP5oybTjGtPhlFO5NTtgN1ZVd4khOCUHZfg8Q2z34W0X5Ptahy7jB5BP34BXUlEKOSTzGzDm3NbTBejh3CVf4OO5Yid428bZlAd21yTkekcfv5FjNisaJUBWyftR1OvLw3pqz4Y1TOKclYXWQjLq8-SosJRUjZP0EV1otEt9j2jNd9VwV6vfLhzsZWzYYqgAkwv2jtq_92fT-35W7JBZ_zLNHEHgQaY_1AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=IY2ZtJ36j6DhUFOH8IHGmpvXdKpnQ-AkDN_EFqmBTJVW2AreeDcddWr4kEs68X2dg0bGCCi3BENIezSxDzZZYoy0ns9LJIuECIUBzOLrWpGZETK1GE7kP5oybTjGtPhlFO5NTtgN1ZVd4khOCUHZfg8Q2z34W0X5Ptahy7jB5BP34BXUlEKOSTzGzDm3NbTBejh3CVf4OO5Yid428bZlAd21yTkekcfv5FjNisaJUBWyftR1OvLw3pqz4Y1TOKclYXWQjLq8-SosJRUjZP0EV1otEt9j2jNd9VwV6vfLhzsZWzYYqgAkwv2jtq_92fT-35W7JBZ_zLNHEHgQaY_1AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت خارجه کویت روز چهارشنبه ۱۳ خرداد اعلام کرد در حملهٔ پهپادی ایران به «تأسیسات غیرنظامی» این کشور، از جمله فرودگاه بین‌المللی کویت و برخی نمایندگی‌های دیپلماتیک، یک نفر کشته شده است.
وزارت بهداشت این کشور نیز اعلام کرد در این حمله دست‌کم ۶۳ نفر زخمی شده‌اند.
وزارت خارجه کویت در بیانیه‌ای که ساعاتی پس از گزارش‌های اولیه از حمله منتشر شد، مشخص نکرد که کدام نمایندگی‌های دیپلماتیک در این حمله آسیب دیده‌اند.
ساعتی بعد وزارت دفاع این کشور اعلام کرد که روز چهارشنبه ۳۰ موشک بالستیک و پهپاد را که ایران شلیک کرده بود، شناسایی کرده است.
سعود عبدالعزیز العطوان، سخنگوی این وزارتخانه، گفت: «از بامداد امروز، نیروهای مسلح ۱۳ موشک بالستیک متخاصم را در حریم هوایی کویت شناسایی و با آنها درگیر شدند. این موشک‌ها بر فراز چندین منطقه مسکونی رهگیری شدند که در نتیجه آن، بخشی از بقایای آنها سقوط کرد.»
او خبر داد نیروهای مسلح کویت ۱۷ پهپاد متخاصم را شناسایی و با آنها مقابله کردند و افزود: «این تجاوز شنیع ایران، تأسیسات غیرنظامی و حیاتی را هدف قرار داده بود.»
وزارت امور خارجه هند اعلام کرد که یکی از شهروندان این کشور در فرودگاه کویت کشته شده است و این حمله را محکوم کرد.
این وزارتخانه در بیانیه‌ای اعلام کرد: «ما بار دیگر از همه طرف‌ها می‌خواهیم که به چنین حملاتی علیه اهداف غیرنظامی پایان دهند.»
پیش‌تر، خبرگزاری دولتی کویت گزارش داده بود که حمله بامداد چهارشنبه به فرودگاه بین‌المللی این کشور چندین زخمی بر جا گذاشت، فعالیت فرودگاه را به حالت تعلیق درآورد و برخی پروازها به فرودگاه‌های دیگر هدایت شدند.
اداره کل هوانوردی غیرنظامی کویت هم اعلام کرد ساختمان ترمینال شماره یک فرودگاه در این حمله «به شدت آسیب دیده است».
شرکت هواپیمایی کویت نیز اعلام کرد پروازهای روز چهارشنبه خود را تغییر زمان‌بندی خواهد داد. با این حال، اداره هوانوردی غیرنظامی این کشور ساعاتی بعد خبر داد که پس از ارزیابی خسارت‌ها و اجرای تدابیر ایمنی، پروازهای شرکت هواپیمایی کویت از ترمینال شماره چهار از سر گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75897" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KD05cSLs5tYom9jmfxb-2SJX75aTRQXh5nilDlu_wQh-A13m-Z8GFuGBmaDmz1rh-RHxIbvLrB45iSv5UqcnIzdo1G88XDEe_l7nIXbzfCpXAwQiROah8idmYtNRKzESdRqd8PGGT-qpabuHFFKf3vAM074pOdQ4vrU2Uq4vgeaWTMP-oWOkMjNGc1HY5F0Of3d1pGu30KeBS4WAl_8Z9Qxs5Q9q9aqYsFcsf1RBQUhvLEY8QH6dUrofu6KYzF2NMyvMtFo1gupj-sN6B9AoTFUeQTKsxME2PmVTE2Jq7mzRpIKRZfMWe1k79IA8g5WIBDOatvDaqLxHOedIPEHwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان وابسته به دستگاه قضایی جمهوری اسلامی، از اجرای حکم اعدام فتح‌الله آوری، به اتهام قتل محمدجواد بخشیان، از نیروهای انتظامی در جریان اعتراضات دی ماه ۱۴۰۴ در همدان خبر داد.
خبرگزاری میزان مدعی است که در زمان دستگیری، «آلت قتاله (چاقو)، هودی مشکی و همچنین همان کتانی سفیدرنگی که در تصاویر دوربین‌های مداربسته محل حادثه مشاهده شده بود»، کشف شده است.
خبرگزاری میزان مدعی شد که آقای «آوری» دارای سوابقی چون «آدم‌ربایی»، «ضرب و جرح عمدی»، «تهدید با چاقو» و «شرکت در سرقت مقرون به آزار» بوده است.
اما خبرگزاری مهر در ۲۹ دی ماه ۱۴۰۴ و زمانی که خبر از دستگیری وی در غرب تهران داد،‌ او را «دارای سوابق کیفری و امنیتی» معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75896" target="_blank">📅 16:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QGPPSNOY2ySYY3nM0ZbTBzX0B4aflA8hs4-qffety4n1SGB8LdvRuORSZH4h2zlcu8N0G2-G8IpxpTDhVa-3Vg-KWr6ANbjkvdKgUlJ42V-hqg22At0j9b9th8Sk_Hxm2yePC3mXSoyGMWXYB_NRxSe1rt-sTUePKXQ_cirUgUsjmG8qVSf5k_e8CbwBeMZ6sK9BGSCyA_YoYhm6EyMVblYl8MEkpPzjUslda3zWE4SI81UybMCbKv2B6Mv6KPuEc6l0UE1kjvB8LR5UDnrIoN0ToV7u939iKr2eJ6HvSf7CDsgDVqoiYoAurpc4F_ZVgv-ezZAJmXAGstpuMCXUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QGPPSNOY2ySYY3nM0ZbTBzX0B4aflA8hs4-qffety4n1SGB8LdvRuORSZH4h2zlcu8N0G2-G8IpxpTDhVa-3Vg-KWr6ANbjkvdKgUlJ42V-hqg22At0j9b9th8Sk_Hxm2yePC3mXSoyGMWXYB_NRxSe1rt-sTUePKXQ_cirUgUsjmG8qVSf5k_e8CbwBeMZ6sK9BGSCyA_YoYhm6EyMVblYl8MEkpPzjUslda3zWE4SI81UybMCbKv2B6Mv6KPuEc6l0UE1kjvB8LR5UDnrIoN0ToV7u939iKr2eJ6HvSf7CDsgDVqoiYoAurpc4F_ZVgv-ezZAJmXAGstpuMCXUbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75894" target="_blank">📅 16:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e49979671.mp4?token=YetIVU34wPB9hksjnx0kvICDmrYCKcncqUo4OHAwrEZWy_FNaskAi7wuTRkdc_LuiodmQlF1jCph2XVpH-pduBetwJ7iQgh57IIX53_KThOdjaSlkrEMT2bm9JbeCU8XDbboeTJtBkgzk4ubkYPJfteB0sMAkGmGi9xFA4FlA19Of8yYsV5nhBriE93Tadvkr7P2LGIqNinEtw6SMqEiWip-sTAvOjJa8D5gTsKYhdyKElemyKVvgQWCklxoncgnVoEUu15KNeZ-6oYC-1IvR4l39b2J6lL4udNCxkFB6I5V-YqXhttGHppFpnJy-LCqLJwmBNjcFnTTrZjY5FzBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e49979671.mp4?token=YetIVU34wPB9hksjnx0kvICDmrYCKcncqUo4OHAwrEZWy_FNaskAi7wuTRkdc_LuiodmQlF1jCph2XVpH-pduBetwJ7iQgh57IIX53_KThOdjaSlkrEMT2bm9JbeCU8XDbboeTJtBkgzk4ubkYPJfteB0sMAkGmGi9xFA4FlA19Of8yYsV5nhBriE93Tadvkr7P2LGIqNinEtw6SMqEiWip-sTAvOjJa8D5gTsKYhdyKElemyKVvgQWCklxoncgnVoEUu15KNeZ-6oYC-1IvR4l39b2J6lL4udNCxkFB6I5V-YqXhttGHppFpnJy-LCqLJwmBNjcFnTTrZjY5FzBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انفجار خودرو در جایگاه سوخت‌گیری تهرانپارس"
خبرگزاری فارس و تسنیم با انتشار ویدیوهای بالا نوشتند:
سخنگوی سازمان آتش‌نشانی:
در ساعت ۶:۱۴ صبح امروز، وقوع یک مورد انفجار در جایگاه سوخت گاز واقع در بزرگراه یاسینی، مسیر غرب به شرق، بعد از سه‌راه تهرانپارس (نرسیده به پل ۱۲ فروردین) به سامانه ۱۲۵ اعلام شد. بلافاصله نیروهای دو ایستگاه آتش‌نشانی به محل حادثه اعزام شدند.
در بررسی‌های اولیه مشخص شد که یک دستگاه خودروی نیسان یخچال‌دار در حال سوخت‌گیری در این جایگاه بوده که به دلایل نامشخص و در حال بررسی، دچار انفجار شده است.
خوشبختانه این انفجار منجر به آتش‌سوزی نشده بود، اما شدت آن باعث وارد آمدن خسارات قابل‌توجهی به بدنه خودروی نیسان و بخش‌هایی از سقف و دیواره‌های جایگاه سوخت شده است.
در این حادثه دو نفر شامل راننده خودروی نیسان (حدوداً ۶۰ ساله) و یکی از متصدیان جایگاه (حدوداً ۴۰ ساله) دچار مصدومیت شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75892" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام‌های دریافتی:
شرق تهران
تهران نو صدای انفجار شنیده شد
وحید جان ۵:۵۸ صدای تک انفجار شمال شرق تهران، سنگین بود. مثل بمب بود
سمت شرق تهران یه تک صدا اومد ۵:۵۷ وحید جان
ساعت 5:56 تهران شرق یه صدایی مثل انفجار شنیدم دقیق نمیدونم
سلام، ساعت ۵:۵۷
شرق تهرانیم و انگار صدای انفجار از جنوب غربی بود
تهرانپارس صدای انفجار اومد ساعت۶صبح
منم صدای انفجار ساعت ۶ شرق تهران بیدارم کرد ولی چون ادامه نداشت فکر کردم اشتباه کردم تا پیام بقیه رو دیدم
سلام، ساکن شرق تهرانم، تهرانپارس- با صدای انفجار ساعت حدود ۵:۵۶ بیدار شدم اول فکر کردم توهم زدم، الان که پیغام‌های شما رو خوندم گویا بقیه هم شنیدن.
الان حدود ۵ دقیقه ممتد صدای آژیر میاد حالا آمبولانس یا آتش نشانی نمیدونم.
سلام، پردیس چهارشنبه ۱۳ خرداد ۶ صبح صدای مثل بمب اومد
وحید جان من تو نارمک صدای انفجار شنیدم ولی نزدیک نبود  ۵:۵۸
شرق تهران یه صدای خیلی بلند اومد ۵:۵۷
سلام تهرانپارس فلکه اول ساعت ۶ یک صداى انفجار بلند اومد و از  ساعت ۶:۱۹  تا ۶:۲۲ صداى آژیر ماشین هاى امبولانس و اتش نشانى میاد
آپدیت:
دلیل احتمالی انفجار در پست بعدی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/75891" target="_blank">📅 06:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rplNo57XUnNpOhrwUGDu7i5llqc9yG8OEMQGm2olDBqIaW0rTa1mE-bbGgLJ_3qwGQOPQRVQ6OvfeT5PpT21h0TYdV906bnbVH12q8CkreOgWWD4RkdNcp7QkcGfQ2ODe1OaDl-DEigQUekdAj6ZIAVUvj9D2PzXGw-Id-mOUKlX_wRNzgVpoLR6e-SMNiq9sDcM52RVL3-wh6UNvSz6at8FkEJ-PSxVnvdo-EIK8wJAgHtv9dxH_x0pxnvFmxtRTFLM61YPrtr-pEp4FPwAbvO3EQZTU_P6iFYOvHZwBEDVuEkzfSIbw4dMC2yHFPHNXPy2qByZFM3EkGij8pHz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست می‌نویسد، بر اساس گزارشی جدید، یک خلبان جنگنده «اف-۱۵ئی استرایک ایگل» نیروی هوایی آمریکا در جریان جنگ ایران در کمتر از یک ماه دو بار در کویت (آتش خودی) و ایران سرنگون شد، اما هر دو بار زنده ماند.
هویت این خلبان هرگز به‌طور علنی اعلام نشده است. مقام‌های کنونی و سابق نظامی به نشریه «های ساید ساب‌استک» گفتند که او یکی از دشوارترین پنج هفته‌های دوران خدمت یک خلبان نیروی هوایی آمریکا را از زمان جنگ ویتنام پشت سر گذاشته است.
به نوشته نیویورک‌پست، بدبیاری او از دوم مارس آغاز شد؛ زمانی که در یک حادثه آتش خودی در کویت، نیروهای دفاعی این کشور به اشتباه به سوی سه فروند جنگنده اف-۱۵ئی آمریکایی شلیک کردند.
در این حادثه، هر شش خدمه این سه جنگنده مجبور شدند با استفاده از صندلی پران از هواپیما خارج شوند و با چتر در خاک کویت فرود آیند. همه آن‌ها سالم نجات پیدا کردند.
با وجود این حادثه، به گفته پیت هگست، وزیر جنگ آمریکا، خلبانان تنها چهار هفته بعد دوباره به ماموریت بازگشتند و در عملیات بمباران اهدافی در تهران شرکت کردند؛ اقدامی که او آن را نشانه شجاعت و فداکاری این نیروها دانست.
نیویورک‌پست می‌نویسد، اما چند روز پس از آن ماموریت، بدشانسی بار دیگر به سراغ یکی از این خلبانان آمد. یک جنگنده اف-۱۵ئی بر فراز ایران هدف قرار گرفت و دو سرنشین آن در خاک ایران سقوط کردند.
این خلبان در سوم آوریل به‌سرعت نجات داده شد، اما افسر سامانه‌های تسلیحاتی همراه او زخمی شده بود و پس از آنکه ایران برای دستگیری او جایزه تعیین کرد، ناچار شد مخفی شود. او روز بعد در عملیاتی نجات پیدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/75890" target="_blank">📅 04:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75889">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFawfGSw6cgnCYsy5dvGWGNLi7PF4QRK4stezXC0B9dWdrpur3X34rbXAQ7EYIu9ilgMb9rRUnFvHyfr-ZxtMon2A1kjZPnTffiYzbxDDfgi8TFoJEJxDfi9gaQtKTS9CkhyQIxHWODgMQ2cvjH157AaWKVjl8sMmPJMPJDS79DX0nYAvE_qItPNasZSDW2XmCbyU_z-vWHptME-hy25Q7r8GXVanRQq9iW35fGWTXrkB_wRjkNw5m545E3ccPNwhRrrdfVpp74JJkd1QtAdchPg3eoc4epZFCjZPFPiFzxZAU6MSVjYb4fu4uVwzNy_wy0n4Pmot9q21vCyc7VW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا در شبکه‌های اجتماعی اعلام کرد که سپاه پاسداران مدعی شده که در حملات امروز با موشک و پهپاد به مقر ناوگان پنجم آمریکا در بحرین و یک پایگاه هوایی آمریکا در منطقه ضربه زده است.
سنتکام گفت این ادعا نادرست است و تمام حملات جمهوری اسلامی به نیروهای آمریکایی شکست خورد.
@
VahidHeadline
آپدیت:‌
سنتکام توییت دیگری هم منتشر کرد:
ستاد فرماندهی مرکزی آمریکا (سنتکام) دقایقی پیش اعلام کرد که «موج دیگری» از حملات پهپادی جمهوری اسلامی که نیروهای آمریکایی در کویت را هدف گرفته بود، ناکام ماند و پهپادها به اهدافی که داشتند برخورد نکردند.
سنتکام افزود پدافند هوایی ستاد فرماندهی مرکزی ایالات متحده «با موفقیت چندین پهپاد را سرنگون کرد. سنتکام گفت هیچ یک از پرسنل و یا تجهیزات آمریکا آسیبی ندیده است.
@
VahidHeadline
(مثل دو روز گذشته در این ساعت، ده‌ها پیام دیگر از تهران دریافت کردم درباره صدای عجیب پرواز هواپیما که منجر به بیدار شدن خیلی‌ها شد.)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75889" target="_blank">📅 04:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75888">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rgk81NQ-UN1PyQ4JupgDO4Jd0E1Ie7SrAGqEIqLGYgmAkJMPh4vjzV61X6LCghH6vWn38lM54MmYolreo-XJOUuorb_QR53lbRPF3NuuTEDE-STJie7BrTAQ_Z2EGnYP01mu5n4Jk-XDbRpix9BDavQfFii9Dg9uKSPb1WvLPqyNWRRqcVRyG29F0IcuZD4gI3OX6n0wAoGHUZkWDmrdehdmkMbYJBCdabLOG_r5EnDfLXid2awISxGwfQnioU2IXWihkyxu3Ew7x1-hrI5lusxp91phn1xLQzHm63VRvJ_Tp1B06rRB4GVd4dsrCJzLHOasoVZ-UgNB1dYN-QkzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام از حمله به جزیره قشم پس از دفع حملات موشکی جمهوری اسلامی خبر داد
ترجمه ماشین:
نیروهای آمریکا و شرکایش در برابر رفتار تهاجمی ایران دفاع کردند
تامپا، فلوریدا — نیروهای آمریکا در تاریخ ۲ ژوئن با موفقیت چندین موشک بالستیک و پهپاد ایرانی را منهدم کردند و در پاسخ به تلاش‌های ایران برای حمله در سراسر خاورمیانه، حملات دفاع از خود را در جزیره قشم انجام دادند.
ایران چندین موشک بالستیک به سوی همسایگان منطقه‌ای شلیک کرد؛ با این حال، هیچ‌کدام به اهداف مورد نظر خود اصابت نکردند.
دو موشک ایرانی که به سوی کویت شلیک شده بودند، پیش از رسیدن به هدف سقوط کردند یا در مسیر متلاشی شدند و سه موشکی که به سوی بحرین شلیک شده بودند، بلافاصله توسط نیروهای پدافند هوایی آمریکا و بحرین رهگیری شدند.
لحظاتی پیش از آن، نیروهای فرماندهی مرکزی آمریکا، سنتکام، سه پهپاد تهاجمی یک‌طرفه را که ایران به سوی دریانوردان غیرنظامی در حال عبور قانونی از آب‌های منطقه‌ای شلیک کرده بود، سرنگون کردند.
نیروهای آمریکایی همچنین حملات دفاع از خود را علیه یک ایستگاه کنترل زمینی نظامی ایران در جزیره قشم انجام دادند.
هیچ‌یک از نیروهای آمریکایی آسیبی ندیدند. نیروهای سنتکام در جریان آتش‌بس جاری، همچنان هوشیار و آماده دفاع در برابر تجاوز بی‌دلیل ایران هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75888" target="_blank">📅 03:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75887">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-hfAkQIoVgp4gjNlYxzj7yh_m2p41Xx2cbJ0U6jzOXLCLFkOEOgYyWxyEUekp97MpF3-LSIIpJbobPm_TQBaeSBfoJmfWS8mrzHBD-yqfhVSSOwMW7gCO2z-RZa6mmFWpbcSM-uJD_QDgAvh4ZIcjodc-JGend1l8UIa7LOZ8-6F5vYmQciiLxFIlqXeE2kCoLeWj5gdW-eRTwNBRaiDgJcx-Hle2fU7EtCEjuM0yh49IMqi3BRIPfVKHwE-yqjo7XkAQdJvWigo7g2v1hWxta8SbMBsEzkTsd6QxthRij_NyfPr4hCQE8OiLfiR11mrr7a46tOH7t659xi77UbDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی پس از مخابره گزارش‌های متعدد از حملات موشکی به نقاطی در کویت و بحرین، سپاه پاسداران با انتشار اطلاعیه‌ای رسما از حمله به پایگاه ناوگان پنجم نیروی دریایی آمریکا خبر داد.
@
VahidHeadline
بیانیه سپاه به نقل از منابع جمهوری اسلامی
"بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد در پاسخ به این تجاوز پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
پیش از این اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم. این پاسخ ها باید عبرت شده باشد.
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75887" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75886">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KJmGMf1VKaV3YVfORRH2TJI-z5ThdnRLeg34KZ3VvXG9N-SREc1LzL7Z3rAcupnUPiEmRt8aTNCPnhqV1qMyxRgfgvaCiLbH7AyLMgJu7pDDIeNLhQKAOcMhfbjtIsde5lxt650mjAuI7DQjJ145RY9kXYuma7zEalhoxsqkgkJ3aj58PQMVANm--gkuvcqnaVhK-jlr3upLJ4-6ssPnoSHsS6bH7EKBhKT0ie5XPEB3p1icUY_1Wr6b18KOiG9II2cByPCRhC1Kw_576RvjLp5Q2dSgbFhZXRbyos58JxN9zVLjzgFKKgO0pRuQGrxXHCzjOLMd2eUpiuJl329qIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
عکس بالا: بندر کنگان دو تا موشک شلیک شد سمت کشور های عربی 2.19
ساعت ۲:۲۰ از جم بوشهر موشک زدن
درود همین الان از جم دو عدد موشک شلیک شد به سمت خلیج فارس
از جم ساعت ۲:۲۱
دو تا موشک پرتاب شد
از جم بوشهر هم دو تا زدن
همين الان
شلیک موشک از شهرک موشکی شهید چمران جم هم اکنون
ساعت ۲:۲۳ دقیقه صبح دو موشک همزمان
آپدیت: پرتاب سوم
سومی هم پرتاب شد
یکی دیگه هم همین الان شلیک شد
۲:۲۴ از جم یکی دیگه پرتاب شد
🔄
آپدیت:
وزارت کشور بحرین دقایقی قبل از به صدا در آمدن «آژیر خطر» خبر داد و از ساکنان این کشور خواست به نزدیکترین مکان امن بروند. این هشدار پس از آن است که کویت نیز اعلام کرد مشغول مقابله با حملات هوایی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75886" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QyaVj4zDc2qwYfXvviZKuL176aDUlhnClgayXC3nNl668Po99Ez1s3d4nPAVlcSwUa5nXJkqu6B_MrPZOnVV8J313Hoc9vEIalGW1y9CFrNEuZNAdXUNmhjLugeIokXPOnt7-jZ4dcrFPa46SUfBE8zUjxOln4JBUmQDopnCJIHmZRvBLYOe8uV5FpDxYj7kBbAdznSJuQpEjHKe-grUp_78vc5Bl2yTjOqBh0sxzP4pK0x0X16a49xY2YDacf9u5Jm1FwOQEsDrUX25Iv1KfJhdwtk6qMRnp1T6P0w_rcvOyztnyJg_dQ2vSoIYXjnP6IgngUJcV1pBri9VDq2qyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۲:۰۷ همین چند ثانیه پیش صدای پرتاب موشک از توی خود شهر داراب شنیده شد.
الان دوباره صدای پرتاب موشک اومد
وحید سلام
یکی دیگه هم الان زدن از داراب
۲ دقیقه پیش
۲ تای قبلی هم یکیش تو هوا ترکید
آپدیت: عکس بالا
و پیامی دیگر از کویت: دوباره صدای آژیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75885" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75884">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o4TTCD_dddOqZlPRRQ7nrDDa_-cOY3icphAZ3CYHiDBgE_AtOmikRLogcB5jPSfwSx9hnzfNUhN4bcOxaO741YODo1Y1lVrlEHQ79I5hSGZxNyXc5gg1HJ8U-R5gIUtZxghv3rTGr-_CXfHZfPkNHIRFNMyQ_ygXStFOLuua-f-xRWTwEQz8zDYR_jQSOxjqwbDczEoi93IWNLTvqejj6fMiq45YN7oan800b8qtA-2XQsVHTmbAxnwt6q5Dk8wI05pyNl0cFz6tlt3m0wLlT1qF7PUJ9SEr6j4-dsIom9H-I8-035oUdve5YA0jKmeiW4oQIp2PodsfpYY_6SI3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از داراب در استان فارس پیام‌هایی درباره شلیک موشک دریافت می‌کنم. هم‌زمان اسکرین‌شات‌هایی هم از کویت دریافت می‌کنم که میگن هشدار اعلام شده.
چهارشنبه ۱۳ خرداد
Vahid
ارتش کویت
اعلام کرد
سامانه‌های دفاعی این کشور در حال مقابله با حملات موشکی و پهپادی خصمانه هستند.
VahidOOnLine
ستاد کل نیروهای مسلح کویت با انتشار بیانیه‌ای فوری اعلام کرد که سیستم‌های پدافند هوایی این کشور، بامداد چهارشنبه، ۱۳ خردادماه، مشغول مقابله با حملات موشکی و پهپادهای متخاصم در آسمان کویت هستند. ارتش کویت در این اطلاعیه تاکید کرد که صدای انفجارهای شنیده‌شده در مناطق مختلف، ناشی از عملیات موفقیت‌آمیز سامانه‌های دفاع جوی در رهگیری و انهدام این «اهداف متخاصم» است. مقامات نظامی کویت از تمامی شهروندان و ساکنان این کشور خواسته‌اند تا آرامش خود را حفظ کرده و به طور کامل به دستورالعمل‌های امنیتی و ایمنی صادر شده از سوی مراجع مربوطه پایبند باشند.
@
VahidOOnLine
پیام‌های دریافتی که پیش از اخبار بالا نقل کرده بودم:
سلام همین الان ساعت ۱:۲۳ دقیقه دوتا موشک از داراب استان فارس پرتاب شد
یکیش حین رفتن ترکید
همین الان داراب صدای انفجار شدید اومد و شیشه ها لرزید
کل همسایه ها ریختن تو کوچه ببینن چه خبره
وحيد همين الان اژير كويت فعال شد دوباره
٦ تا انفجار خيلي سنگين تا الان
توي اين ٣ ماه اينقد صداش سنگين نبود
سلام آژیر در کویت
۵ انفجار بزرگ در کویت نسبت به روزهای قبل بیشتره
آپدیت:
ما بین فسا و داراب هستیم
یه صدای انفجار وحشتناک اومد ولی نفهمیدیم چیشده
من داراب هستم
ما عروسی بودیم تقریبا ساعت ۱.۴۰ دقیقه بود که یه صدای انفجار اومد و سقف سالن لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75884" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75883">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام دریافتی تایید نشده:
صدای  انفجار روستای نخل گل قشم
سلام وحید جان
قشم صدای پایان جنگ در همه جبهه ها از جمله لبنان میاد
خبرگزاری مهر هم نوشته:
"بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75883" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75882">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=IB4_pgliMr3qPq-dKvlCu88NSRKFGYQYkCnguTJVPUeeUzFNNS3K2r6f4Hte6kOxTcqCG775P1rSek4AwEQ-aDaSnjVmnb9vQyFjXfVy35rlpCghftk1n8MkFJ1RWz6JsI9HwjfW2KKHVHT1RJedXdKklZAgWvkFb_SnWAN4EKVnBy1vvq9WFsbPZkBZMiD9YadgRekDjWy1LZBHpUXC1wUbL36MHe-01vd6MGX5OYDqs1on3SPGRrTVjO8MEYLwM5Sv_HSQZg2BYW5PVlwu3ZbfhZx5emBrqN8xRBuY4_SARhOJQ5IP_fsMdrZjBgMFzqIxgAcH4DjOfCDFtkcZ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=IB4_pgliMr3qPq-dKvlCu88NSRKFGYQYkCnguTJVPUeeUzFNNS3K2r6f4Hte6kOxTcqCG775P1rSek4AwEQ-aDaSnjVmnb9vQyFjXfVy35rlpCghftk1n8MkFJ1RWz6JsI9HwjfW2KKHVHT1RJedXdKklZAgWvkFb_SnWAN4EKVnBy1vvq9WFsbPZkBZMiD9YadgRekDjWy1LZBHpUXC1wUbL36MHe-01vd6MGX5OYDqs1on3SPGRrTVjO8MEYLwM5Sv_HSQZg2BYW5PVlwu3ZbfhZx5emBrqN8xRBuY4_SARhOJQ5IP_fsMdrZjBgMFzqIxgAcH4DjOfCDFtkcZ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به یک کشتی دیگر شلیک کرد.
بیانه سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکا [امروز] ۲ ژوئن یک نفتکش بدون بار را که قصد داشت به سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند.
فرماندهی مرکزی آمریکا، سنتکام، تدابیر محاصره را علیه نفتکش M/T Lexie با پرچم بوتسوانا اجرا کرد؛ این کشتی هنگام عبور از آب‌های بین‌المللی به سوی جزیره خارک در حرکت بود. خدمه کشتی هشدارهای مکرر را نادیده گرفتند و طی یک دوره ۲۴ ساعته چندین بار از اجرای دستورهای نیروهای آمریکایی سر باز زدند.
در نهایت، یک هواپیمای آمریکایی با شلیک یک موشک هل‌فایر به موتورخانه کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شد.
سنتکام از ۱۳ آوریل اجرای محاصره همه رفت‌وآمدهای دریایی به بنادر ایران و خروج از آن‌ها را آغاز کرده است. با ادامه آتش‌بس با ایران، نیروهای آمریکا تاکنون شش کشتی تجاری را از کار انداخته و مسیر ۱۲۲ کشتی را تغییر داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/75882" target="_blank">📅 00:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MutuEy2OLDrvoIcwhelx6V0BRYwG5ll6jOhmGM-eRHXNRzVIiNO-2KsMyEVHTbLYM5Aq5oXjnFd1LVcRRv24nuLE-Uxz4ZydooL0_N04WLO6TpukNEMhj2WbAWTyW7hVNL_rMnV04bJUTUnNWiI6Tl0rqkbS1FvXEicjIBYGjyUsk-IPHDAyMYC9kQ7k7TU8umhylOMjHP-cslhErTnS6uOZ9X6WyZLE0j6-3fBN1YoHxEc3C9FvvrioBJWm3wbOX_SGxhbcwWjNAzjKmTyOjJ0YQBkxr7UcF52wae5-c1fSC1RfvIr3jLNNJyA47u81sWh9iCResA36kwZaAoG3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: گزارش‌ها درباره توقف مذاکرات درست نیست
ترجمه ماشین:
گزارش‌های رسانه‌های اخبار جعلی مبنی بر اینکه جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز پیش گفت‌وگو را متوقف کرده‌اند، نادرست و خطاست.
گفت‌وگوهای میان ما به‌طور مداوم ادامه داشته است؛ از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش، و امروز.
اینکه این گفت‌وگوها به کجا می‌رسند، هیچ‌کس نمی‌داند؛ اما همان‌طور که به ایران گفتم: «وقت آن رسیده است، به هر شکل ممکن، توافقی انجام دهید. شما ۴۷ سال است که مشغول این کار بوده‌اید و دیگر نمی‌توان اجازه داد این وضعیت ادامه پیدا کند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/75881" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75880">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUKSHYGEXpIyAEqG4WevcfFaDUPyjDnUzunvKpkSYSzmidH4tiE9OZAI7N9i9dcIwrOWr2RgYCHSoTOJhlTRlDC9z31vCx6ImPss9xJeqlNQFdLytXpfoPR2eZiHzacPVTGSukLkq_n2an4R4TXFIfFkr3KsmVNhjEFVoHmqE7-jm3MKBKaMHDSWCSzDuQFG3fPB8QVHLdvSmZFYdTB4gGVbzHqQ_YV_jYT-W44fzY1fQ4BJviTja1sKpqQrc6NTPxjHZo2QJx2wfUenA09PqzHL0vxhrI8PidQKi3r4XO27ztKhDUjysU58meIvy3Sc2b54zX-2OlKfwlYCsApBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که نشانه‌هایی وجود دارد مجتبی خامنه‌ای رهبر جدید جمهوری اسلامی در سطحی به شکل فزاینده‌ای در حال مشارکت در روند مذاکرات است، «اگرچه تمام ارتباطات او به صورت مکتوب و از طریق واسطه‌ها بوده است.»
آقای روبیو افزود: با توجه به اتفاقاتی که برای رهبران متعدد در آن سیستم رخ داده است، تصور می‌کنم که حضور بسیار علنی احتمالاً چیزی نیست که در داخل برای آن‌ها توصیه شود.
او همچنین در پاسخ به سناتور دموکرات کریس مورفی، کاهش تحریم‌ها در ازای بازگشایی تنگه هرمز را رد کرد و گفت که هرگونه کاهش تحریم‌ها باید پس از امتیازات عمده در مسئله هسته‌ای و اورانیوم غنی‌شده صورت گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/75880" target="_blank">📅 19:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75878">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vn941kgxqTpZUVmgyzqLgnqksETg81G8kmf46VxNqnM-Hl-h8FMrc527wWenyHx55W5UtkBtSKvt_jD-DRBXSHJiISFqQOhta2aoC1CTnwZmekoHgo_eNm1EZ1pgCx8BBC5TDrfANhQkJLJtdI9_8ZxZK6VR3Z41VjLOaNy1xTbwBH7JdoDKM2uo0h2-B_vmREHLa8fGsMG48h45dE9hJGXnPqYaAHfOu85LUWX2FCOnlNwM29RtDzZCyTmn_Xu47e4QH48CYz3HgE2zGxxHJ_Lm9BcsV76v_FAv5KL9aanSAUIqpz80QJqMnIjgbdk6PzDqZToKjkuDCLo6dETaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ttupl5AOkkyoS28u-7SUkmvIues4pplIW_XgbQJi3HntHGuHUvwWsopfEby2t6-5KIovGWm-1EiPxEEdDH-yK7iQznKJQBXRjcyrHIIW_wgQm1AmCO5HJdrih5raMhLmOLdChBNxhoxEC1yH7_YKM0Qoy-isPsDEJ-FSW9UlC468cUA4p-OS_B1vsszNBYMzBmTmnGvEF9AaTyL2FHPaE12GBnVbQN1QxH1AmUH00umaQscaZqoSxpxei7YIzQYTgE-FFi-0jjGIgQR1yBO4WadZg2xW036jEQa_CiaWiZ5nW5hW4TQ1f2sly4KVfc9hT78aosizZEgmPZnWC-n0Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو در جلسه کمیته روابط خارجی سنا گفت: «چیزی به نام نیروی دریایی جمهوری اسلامی وجود ندارد. آنچه باقی مانده تعدادی قایق کوچک است که روی آن‌ها مسلسل نصب شده و نیروی دریایی واقعی در کف اقیانوس قرار دارد.»
او افزود: جمهوری اسلامی همچنان تعداد زیادی پهپاد در اختیار دارد. توان بازدارندگی متعارف تهران به‌طور قابل توجهی تضعیف شده است.
@
VahidOOnLine
وزیر امور خارجه ایالات متحده در جلسه استماع سنا تاکید کرد که شرط اول آمریکا برای مذاکره با جمهوری اسلامی، بازگشایی کامل و بدون قید و شرط تنگه هرمز است.
او در ادامه تاکید کرد که منظور از بازگشایی، بازگشت شرایط به پیش از جنگ و عبور و مرور آزاد تمام کشتی‌ها از این آبراه راهبردی، بدون محدودیت و مانند سایر آبراه‌های جهان است.
@
VahidOOnLine
او گفت باز کردن تنگه هرمز شرط اول آمریکاست اما صرف این کار باعث برداشته شدن تحریم‌ها نخواهد شد و رفع تحریم منوط به شرایطی خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/75878" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75877">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJR16gxC-3SA-ndpDzea4fW67nbLvsMB_M9hMkF8MKWYTdzMkJsz1XS__8r5axi2gyF0MhIuCxww_rsRpZlXDsla69Agd9XlwfNNcWObsXSEUefxebBKZIJyQkaWWbRzFrg8MtRuMS-FsqjeDR9y7H8AL_nzuRflXqfsOedDZmjchfoLseJwAIOCOEQsG2GH13gtRFrvU_XWiBaKnMDYeHUrGYZq3raSiJAoioCX4-UuIgd42Q1SNEsx5rarfw5Convj_BxFyvjxZuxGClAoyM9rBRd7W79MtHuECt9GCko50qUvlWYpNwlI_rcnZaAadihqMH25itUZenIJbEoiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، در مراسم تودیع دیوید بارنئا، رییس موساد، گفت جمهوری اسلامی تاکنون به دلیل توطئه‌هایش علیه اسراییل بهای سنگینی پرداخته و سرانجام این حکومت سقوط است.
بر اساس گزارش دفتر نخست‌وزیر اسراییل که روز سه‌شنبه ۱۲ خرداد ۱۴۰۵ در شبکه ایکس منتشر شد، نتانیاهو در این مراسم گفت: «هر کسی که بدخواهی علیه اسراییل در سر می‌پروراند، بداند که توطئه‌هایش شکست خواهد خورد و بهایی که خواهد پرداخت بسیار سنگین خواهد بود. بهایی که جمهوری اسلامی تا همین‌جا پرداخته است، بسیار سنگین است. پایه‌های رژیم وحشت در ایران ترک خورده و دیگر به آنچه بود باز نخواهد گشت. من به شما می‌گویم سرانجامش سقوط است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75877" target="_blank">📅 18:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75876">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hs0AHQ0NEFAKtODVb5vGSNORYe2dWbRqw5Hf-qAm8iK12ngpKCzEpj4VFNSaXXdEUOBKk7YmpPuas4fnBhPfCqIfVPfgqzpwQPB8pSyDZbpswop8VXy7HKjKVXUuh5r0AHUygmXF2zcqTooZvdo88FjowfzM6wVBKEz_cr41M2yuhP9xI9_DTdnOPFroR2O8Z5dA7wgJ8uzDDGE4j1aovPOLFEwc7B98z6w1IjOham_MdUFMAcaePWoXkg4Eh03WcrvNrwErxZcnLLj_WIYXhq4lSKiNKJC3QH24qRD1Lh4paoMsR1hR4WnGogJZ0T7HWy18yiPARWz0nGlsvcWdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که جمهوری اسلامی در حال دستیابی به سلاح هسته‌ای بود و اگر عملیات خشم حماسی صورت نمی‌گرفت دیر می‌شد.
آقای روبیو با یادآوری این که توانایی نظامی جمهوری اسلامی به شدت تضعیف شده، افزود که جمهوری اسلامی ایران برای اولین بار در تاریخ، بسیاری از شرایط مدنظر آمریکا برای رسیدن به توافق را پذیرفته است.
به گفته او شکاف در ساختار قدرت سیاسی جمهوری اسلامی و زمان طولانی رسیدن پیام‌ها مذاکرات را طولانی کرده است. اما طبعا اگر مذاکرات به هدف دلخواه آمریکا نرسد، ایالات متحده گزینه‌های دیگری را درپیش خواهد گرفت.
@
VahidHeadline
پیش‌تر ‌خبرگزاری فارس، وابسته به سپاه، به نقل از یک منبع آگاه نوشت که تبادل پیام بین جمهوری اسلامی و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشینگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75876" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dSdtS8hGzC_mQK8zq30pBUTyCtFFYa9Bj8yEWHmZNl6tfymqn1m7R1oGZQwcP9j0QrfoMUPR1hRNelyUqEkvsZ08jWv5UA9BpGToTuzowE5rw9Zk8rHdO0dbU5dPgexPlVBT5EiWnG2tiWrgXpBGzuilpVSf3JsZ-ibm1dtIwRKogOppVM3Z-g63lJlVVN8Iuc3NWvHseh-1RGtu30dxvNb9CfA2EBBNZIri_RFamxlXzJjWDiFgz4YnI9oV9jcBfhRI_jesaeUESkDR0OXPSvSIS1A4CNJWaMXqQOV0DdfQTPwBJv4owbuT9d0g1jgzjUD0tlp5H7aMSBYFJNs8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=Mj7kI3Oljhjg6Skw1p3nOkXHj6fAf3CCG6rqVUNCV_QFvpXmjyjqZFqzxv4b9iyz9gehfVmjXbFEvhWk1UL_jiklcWcCTM3fStk5a_rCdceiwqL5158Hxm5OVMww87ilPLA1IJ4_jkkbae90f0av89Tfx-rJn6RAsQlkYfg6iqKiG19sgxYqjYqqn2vG_G8Dy0vtH0DMKh-kX_ZKdGa0skQ0OGN_36tReDBcWA6-HDYh6PCKvwPcj-QT0F39ZDPM3KYgP0MBP6glxcbe2fFWuzXULqU1SoDMmH38akJw2bEUCEQnAfbtR0Puji6O4G-BzPJ1_GS50FZSo3AEQ-iwjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=Mj7kI3Oljhjg6Skw1p3nOkXHj6fAf3CCG6rqVUNCV_QFvpXmjyjqZFqzxv4b9iyz9gehfVmjXbFEvhWk1UL_jiklcWcCTM3fStk5a_rCdceiwqL5158Hxm5OVMww87ilPLA1IJ4_jkkbae90f0av89Tfx-rJn6RAsQlkYfg6iqKiG19sgxYqjYqqn2vG_G8Dy0vtH0DMKh-kX_ZKdGa0skQ0OGN_36tReDBcWA6-HDYh6PCKvwPcj-QT0F39ZDPM3KYgP0MBP6glxcbe2fFWuzXULqU1SoDMmH38akJw2bEUCEQnAfbtR0Puji6O4G-BzPJ1_GS50FZSo3AEQ-iwjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هما میرافشار، شاعر و ترانه‌سرای نامدار ایرانی، در ۸۹ سالگی در لس‌آنجلس درگذشت.
مرتضی برجسته اشراقی، با نام هنری مرتضی، سه‌شنبه ۱۲ خرداد، در اینستاگرام نوشت که خانم افشار هفته گذشته چشم از جهان فروبست، اما خانوادهٔ او با تأخیر این خبر را منتشر کردند.
این شاعر و ترانه‌سرا، که بر اساس گزارش‌ها، سال‌ها با بیماری آلزایمر دست‌و‌پنجه نرم می‌کرد، از پُرکارترین و محبوب‌ترین ترانه‌سرایان قبل و بعد از انقلاب ۱۳۵۷ بود.
هما افشار با بسیاری از خوانندگان برجسته ایرانی از جمله حمیرا، هایده، مهستی، ستار، ابی، داریوش، معین و عارف همکاری داشت.
او در سال ۱۳۱۵ در تهران متولد شد و در جوانی با علی میرافشار، پسرعموی حمیرا، ازدواج کرد. این پیوند، دوستی نزدیکی بین هما و حمیرا ایجاد کرد که به گفته خود او، جرقهٔ تولید بسیاری از ترانه‌ها و همکاری‌های این دو با هم شد.
@
VahidHeadline
هما میرافشار، روزنامه‌نگار، شاعر و ترانه‌سرای تصنیف‌های عاشقانه موسیقی دستگاهی و آثار به یادماندنی پاپ، در ۸۹ سالگی درگذشت؛ چهره‌های نامدار موسیقی و علاقه‌مندانش در شبکه‌های اجتماعی از مقام هنری او تجلیل کردند.
او در سه مجموعه شعری بیش از هزار سروده دارد که افزون بر ۲۵۰ شعرش در زمره ماندگارترین ترانه‌های ایرانی است و بی‌دلیل نیست که در جامعه موسیقی به «زن هزار ترانه» و یا «ملکه ترانه‌سرایی ایران» معروف شد. از همین روست که ایرج جنتی عطایی، ترانه‌سرای برجسته معاصر، هما میرافشار را پیشکسوت خود می‌‌داند که «پیش از ترانه نو و در کنار آن شهره بود.»
هما پیشگام سرودن اشعاری بود که یک زن برای معشوق می‌خواند و یا حرف‌های عاشقانه‌ یک مرد برای دلبرش، چرا که تصنیف‌سرایان آن دوران به جنسیت ترانه‌ها کمتر می‌پرداختند. او سال‌ها پیش در برنامه «یک‌ حرف و دو حرف» رادیو بی‌بی‌سی به زنده‌یاد محمود خوشنام، پژوهشگر موسیقی، در این باره گفت: «منیر طاها، سیمین بهبهانی یا لعبت والا که کار می‌کردند، من ندیدم که ترانه‌هایشان بوی زنانه بدهد مگر این که از زبان مرد بیرون آمده باشد. اگر خواننده آنها مرد بوده به ناچار باید چیزی را می‌نوشتند که یک مرد به یک زن بگوید.»
«یادم می‌آید که یکی از من پرسید که شما این حالت را چگونه می‌نویسید و من در پاسخ گفتم اگر بخواهم از زبان مرد شعر بگویم، مشتاق شنیدن همان‌هایی هستم که دوست دارم از او بشنوم. آن حرف‌ها را می‌گذاردم در کلام و اکبر گلپا می‌خواند، یا می‌دادم به محمودی خوانساری می‎‌خواند اما گاه طوری می‌نوشتم که مرد یا زن هر کدام بخوانند فرقی نکند.»
....
در ابتدای دهه پنجاه بود که اشعار هما میرافشار و ملودی‌های زیبای محمد حیدری در صدر جدول بهترین‌ ترانه‌ها قرار گرفت و نام هما درخشید؛ مثل ترانه «دیوونتم» با اجرای حمیرا: «بذار بگم دیوونه‏‌تم...آره دیوونه‏‌تم من...نشکن منو به سنگ غم... چراغ خونه‌تم من...» یا ترانه «دلم می‌خواد» با اجرای هایده: «دلم می‏‌خواد که روزی صدهزار بار... بهت بگم دوست دارم عزیزم...» و یا ترانه «میکده» با صدای اکبر گلپایگانی: «هوس میکده داره دل دیوونه‏‌ی من، نمی‌‏دونه بی‏‌تو ایام بهارو چه کنه...»
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75871" target="_blank">📅 18:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K-ApgseVGN3qpLkRNx6pnVcDw_sx_h3VFa-cJ51HXqOaqiSLLR1U7CZBNwv3O2ZemIA5gR1foS0t3hdFj4JxFOnBaPpRqPRgefFcJDk5X4PFo704c3Bx549b1-Qwk1qN7hj4aTvvqyQhOncxxWbpPN-iaZf-jvoOxANgt7N_SkcXtrxnSLwWpiTKOZZyHP90pgBXaXLJk6Z8jb5uYlc9z-0PMnhQ96uu526zn9UZiSZsnKPRpPuJIbZY2A9w5z0X8O0HSri005RiEnA4eiUdeeQ1WqJVy3znQZjHIwifHFJu8avGWGa6cOLEozW6TtwHPexw8iGJcwhYKCUTJQ9nqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75870" target="_blank">📅 17:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRr6K83DcQkR45LxhrK_luLxCA84TLHv_TKGqMouCgBPAQhR3Y0IAh8UG8ZQLr07FwIIEM4YkLs1uzH3cY5ENd7dmsVSowJis15EkYW1vH210qAYDqbZzsNADd6lTGrdyalhdc4V1QBt0y6vYo8b-hGUi6HiFAhgLv4XcEJtudLjNUkmJbUgJ0Eg5VOx8NHO9MV6Bwo7VNu-haQ2PxBzEqBKi9kPe2KTtjhdlIDJfTsOe99pgKcFZBv3leCWiN93xvIW5iqrfnw80vZLwFPQc4N-5N-QZvPoOMLUI78ibhSxGslEnuZJfjadHXtLXGsqGLewwlgSiDF2ZLiBY6jklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام شهرداری تهران می‌گوید که برگزاری «مراسم بدرقه» و تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، در شهرهای قم، مشهد و تهران «قطعی شده است».
به گزارش رسانه‌های ایران، محمدامین توکلی‌زاده معاون اجتماعی شهرداری تهران روز سه‌شنبه ۱۲ خرداد گفت که این نهاد «در حال تدارک برای حضور جمعیتی بیش از ۱۵ تا ۲۰ میلیون نفر در تهران هستیم».
او به زمان دقیق برگزاری این مراسم اشاره نکرد ولی گفت که احتمالا در پایان ذی‌الحجه و اوایل محرم برگزار شود.
این زمان تقریبا مصادف با اواخر خرداد و اوایل تیرماه است.
علی خامنه‌ای از ۹ اسفند پارسال که در حملات مشترک آمریکا و اسرائیل کشته شد، هنوز دفن نشده است.
معاون اجتماعی شهرداری تهران در ادامه گفت که «مراسم بدرقه» سه روز در نظر گرفته شده و در تهران قرار است ۲۴ ساعت طول بکشد.
به گفته توکلی‌زاده، محل دفن خامنه‌ای «طبق وصیت ایشان و توصیه‌های نزدیکان‌شان» در حرم امام هشتم شیعیان تعیین شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75869" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75868">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbYKGj_V9jgQbC09RjAnEuJ58dNEXsDlKQ7ePXoPkMfhymhOhKxho0hnducswRcb_U7RSQiWweYqp8RIo5n2Kp1lM7_mHuUwk-JUFaJBnCMwxKxkFCIzIqj8xwPFyOUO_OnzjbP9wyh_5EOJwxtKxAOj9sFmqpDETg633vPlJyV_b0VoWSGLhDS1cAp2HmjSg5B0DSGTWUAk_RoI-2KrBqc2yZJuQaWaIZNwDqT3-aPoPbi1UmsJx4fE8bxcQfxJ1UEWMu2lM-SejKIw24qZnQ_sZB6hLEZHIR1fj5BGNSm7ZHxl6EKdoJV9kKFYrKvcX08NfudptWXzQIMV1xSoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از چند روز تاخیر، بانک مرکزی و مرکز آمار ایران به‌طور همزمان گزارش‌های تورمی اردیبهشت‌ماه را منتشر کردند؛ گزارش‌هایی که با وجود تفاوت در ارقام، از تداوم روند صعودی قیمت‌ها و افزایش فشار معیشتی بر خانوارها حکایت دارد.
مرکز آمار ایران تورم ماهانه خانوارهای کشور را ۸.۸ درصد، تورم نقطه‌به‌نقطه را ۸۳.۹ درصد و تورم سالانه را ۵۷.۷ درصد اعلام کرد.
همزمان بانک مرکزی با تمرکز بر مناطق شهری، تورم ماهانه را ۸.۵ درصد، تورم نقطه‌ای را ۷۷.۲ درصد و تورم سالانه را ۵۳.۹ درصد برآورد کرد.
بر اساس گزارش بانک مرکزی، شاخص کالاها در اردیبهشت‌ماه نسبت به ماه قبل ۱۰ درصد و نسبت به مدت مشابه سال گذشته ۱۱۳.۸ درصد افزایش یافته است؛ آماری که از رشد شدید هزینه خرید اقلام روزمره حکایت دارد.
اختلاف ارقام منتشر شده از سوی دو نهاد آماری به تفاوت در جامعه آماری، سال پایه، شیوه نمونه‌گیری و وزن‌دهی کالاها و خدمات بازمی‌گردد. مرکز آمار کل خانوارهای شهری و روستایی را مبنا قرار می‌دهد، در حالی که بانک مرکزی تنها مناطق شهری را بررسی می‌کند.
مقایسه آمارها با ماه‌های گذشته نیز از شتاب گرفتن روند تورمی خبر می‌دهد. تورم نقطه‌به‌نقطه که در فروردین‌ماه ۷۳.۵ درصد اعلام شده بود، در اردیبهشت به ۸۳.۹ درصد رسید؛ افزایشی بیش از ۱۰ واحد درصدی تنها در یک ماه.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75868" target="_blank">📅 17:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=kqJg9SjrPqx2nopIgKGTDxkdMz2p3nuTpeeQTuUOiMe9cdlwDnxFopHbmJQHbKPIx6myG4bfYQjHGFbhfFqaS2g8-FqTJ90QABwuGrb0FPnXsvYZ8VZZVz5l5YDQO15IYYTLCb2acD03RKOQ7GXc_2v-lrrnVVaDN1tYLC2VWI3WSBEJgW_5OVmTg8REaZ7JSJhQJZycq7tk7jh0_KNxx-UFHvFl3tpEDuF3N3-ffR6LT-0xtG6iAdXvant-Ie411d-pBPfFHM7N8PdfnDnUL9pu9wpsTh_ht-k6R65Tt73Beh3TpN2Q_hDKojZm93IPGV5CN2Mtikr-2Y4knAiYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=kqJg9SjrPqx2nopIgKGTDxkdMz2p3nuTpeeQTuUOiMe9cdlwDnxFopHbmJQHbKPIx6myG4bfYQjHGFbhfFqaS2g8-FqTJ90QABwuGrb0FPnXsvYZ8VZZVz5l5YDQO15IYYTLCb2acD03RKOQ7GXc_2v-lrrnVVaDN1tYLC2VWI3WSBEJgW_5OVmTg8REaZ7JSJhQJZycq7tk7jh0_KNxx-UFHvFl3tpEDuF3N3-ffR6LT-0xtG6iAdXvant-Ie411d-pBPfFHM7N8PdfnDnUL9pu9wpsTh_ht-k6R65Tt73Beh3TpN2Q_hDKojZm93IPGV5CN2Mtikr-2Y4knAiYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها دانش‌آموز روز سه‌شنبه ۱۲ خرداد با تجمع مقابل وزارت آموزش و پرورش در تهران، به تغییر قوانین کنکور، افزایش تأثیر معدل و پیامدهای جنگ بر آمادگی برای آزمون سراسری اعتراض کردند.
در ویدئوهای منتشرشده در شبکه‌های اجتماعی، شعارهایی از جمله «دانش‌آموز بیداره، از تبعیض بیزاره»، «دانش‌آموز می‌میرد، ذلت نمی‌پذیرد»، «وعده زیاد شنیدیم، عدالت و ندیدیم» و «فشار روانی کافیه، زندگی‌مونو پس بدین» شنیده می‌شود.
سیاست‌های مرتبط با کنکور از جمله افزایش تأثیر معدل و تغییر در شیوه برگزاری و زمان‌بندی آزمون‌ها، در کنار شرایط ناشی از جنگ، در ماه‌های اخیر با تغییرات و ابهام‌هایی همراه بوده که به گفته داوطلبان، موجب سردرگمی و دشواری در برنامه‌ریزی برای امتحانات نهایی و کنکور شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75867" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UufM_11bH4qFJWFNQbs2TBYr2xYKValHFC90ukhfrVQZ9TW0oMX7Xce9nc2WctMOk4rT_Fgm7wVh-PHo6D4ckj4WbJL22l89v0ieIQB_Gt6oOwbgVby8pOD9BSpyn7tL_fqYCdIeoQGI5CiDztfJSbD6pqO4tW2Ngq7Pci_b2tH9MqEL9H6lqcvCbVEEevnluHA1McRZvBaGbcj1rzwqGRKrR0W1oqEDcsPJl6z8zI7k4hBPGMuTu9STAe7bcul4Yw8q0QNPXKDNoKmuoKa6BzM44hIIP9OvLpYGTuJ2zpHH3X81ZtoVVc692GrWcEMsHSg3deGgN7rt7WWdk1ouhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای سومین بار این متن رو علیه بعضی از رسانه‌ها پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرام گرفته، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر تمام ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بیندازد و دست‌ها را بالا ببرد، در حالی که هرکدام فریاد می‌زنند «تسلیمم، تسلیمم» و دیوانه‌وار پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر همه رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال — یعنی وال‌استریت ژورنال! — سی‌ان‌انِ فاسد و حالا بی‌اهمیت، و همه اعضای دیگر رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد؛ اصلا هم رقابت نزدیکی نبود. دموکرات‌های احمق و رسانه‌ها کاملا راهشان را گم کرده‌اند. آن‌ها کاملا دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/75866" target="_blank">📅 05:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باز هم صدای غیرمعمول پرواز یک هواپیما خیلی‌ها رو در تهران از خواب بیدار کرد.
پیام‌های دریافتی:
صدای هواپیما سعادت آباد
سلام، تهران صدای توافق میاد فکر کنم
صدای جنگنده یا هواپیما ۰۴:۰۹ غرب تهران
دوباره همین الان دقیقا ساعت ۴:۱۰ صدای شدید تر جنگنده غرب تهران
سلام تهران صدای جنگنده میاد چخبره؟؟!
مطمئن نیستم ولی غرب تهران فکر کنم صدای هواپیما یا جنگنده اومد
تهران سمت  سعادت اباد صدای جنگنده میاد
خیلی پایین بود صداش
همین الان تهران صدای کلی جنگنده اومد ک رد شدن
خیلی بلند بودن
صدای جنگنده غرب تهران
ساعت۴:۱۰صبح صدای جنگنده سمت شمال غرب میاد
تهران جنت اباد 4 09 صدا جنگنده اومد
4 و ده دقیقه صبح بالا سر شهرک نفت پونک جنگنده اومد آنتن قطع شد و وصل شد
همین الان غرب تهران حدود ۲ دقیقه صدای جنگنده اومد
دقیقن ده ثانیه پیش ساعت ۴:۱۰ ‌صبح یک‌هواپیمای از همونایی که موقع جنگ از بالا سر خونمون رد می شد
تهران حدود ساعت ۴ یه هواپیما مسافربری رد شد صداشم زیاد بود
هیچ وقت از این مسیر رد نمیشه!
توی فلایت رادارم نیست
شهرک‌ غرب ۴:۱۰
صدای جنگنده او‌مد
سلام وحید جان . ساعت حدودا ۴ و ۵ تا ۴ و ۱۰ دقیقه صبح شمال غرب تهران صدای مهیب جنگنده اومد. کاملا مشخص بود تو ارتفاع پایین داره پرواز میکنه . البته نه پدافند عمل کرد نه بعدش انفجاری شد. احتمالا برای نیرو هوایی ایران بوده
امروز سه شنبه دوازده خرداد ساعت ۴و۱۳دقیقه صبح صدای هواپیمای باری یا مسافری اومد چون چراغهای کابین و چشمک زن روشن بودن، مسیرش رو دنبال کردم مهرآباد ننشست تا جنوب تهران ادامه مسیر داد، صداش عین هواپیمایی بود که دیروز دوشنبه ساعت ۹و۱۵دقیقه صبح ، بسیار طولانی و ممتد حرکت می کرد به سمت  شمال ،چون از  کوه های البرز رد شد
صدای جنگنده نبود غرب تهران
یه هواپیمای خیلی بزرگ بود که اونقد پایین پرواز میکرد احساس کردم الانه که بخوره به ساختمون روبرویی خیلی بزرگ بود هواپیماش و خیلی پایین
پنجره باز بود دم پنجره خوابیده بودم صداش شبیه جنگنده نبود مابین جنگنده و پهپاد بود
همچین قیرقاژ داد رفتم رو هوا
سمت پونک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/75865" target="_blank">📅 04:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75864">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن موقت خطوط تلفن همراه در بعضی از شهرهای استان‌های فارس، بوشهر و هرمزگان و...
از حدد ساعت ۲
▪️
شیراز کلا قطع شده انگار
نه میشه زنگ زد نه میشه کاری کرد
▪️
کل تلفن های همراه توی شیراز قطع شده
تمام اینترنت ها قطع شده
مشخص نیست چرا اینجوری شده
نه ایرانسل نه همراه اول نه رایتل آنتن نداره
▪️
وحید از حدود ساعت ۲:۱۰ تا همین الان انتن گوشی ها و اینترنت خانگی و هر چیز مخابراتی توی شیراز پرید
همین الان [۲:۳۰] همراه اول وصل شد با سرعت کم. ایرانسل وصل نیست
▪️
شیراز خط گوشی بیشتر از ۲۰ دقیقه رفت
از ساعتای ۲:۱۰ دقیقه تا ۲:۳۰
ایرانسل هنوز نیومده
آپدیت:
ایرانسل هم وصل شد
ولی همگی 3G  هستن
سلام وحید جان بندرخمیر هم از ساعت 2 همه چیز قطع شده الان به زور وصل شدم بهتون اطلاع بدم
اصفهان هم دقایقی خط همه رفت
تو شیراز یک دفعه همه انتن ها پرید. حتی نت مودم خونه مون هم کاملا قطع شد
الان بعد از حدود نیم ساعت دوباره انتن ها اومد
وحید فکر کردم فقط واسه من اینطوریه نت خونگی مبینت ما هم قطع شده خوزستان سربندر
از شهرستان های فارس نیم ساعت همه انتن ها رفت و اینترنت مخابرات هم کار نمیکرد الان اینترنت مخابرات اومد و انتن همراه اول هم با سرعت کم اومد ایرانسل قطعه
نت و انتن و... کامل توی بندر ماهشهر پریده
اهواز هم همینطور
سلام بندرگناوه چند دقیقه کلا همه چی قطع نه زنگ نه حتی شبکه داخلی همه چی بسته شد
بندر ساعت ۲ بامداد تقریبا آنتن ها رفت
و بعد برگشت خط 3g شده اما اینترنت کار نمیکنه
الان فقط اینترنت فیبر وصل شده
دقیقا راس ساعت ۲ کل دیتا سنتر شیراز قطع شد
تلفن همراه کاملا بدون آنتن
تقریبا ۳۰ دقیقه شد که وصل شد
همین الان حدود نیم ساعت در نورآباد ممسنی همه چی پریددد نت و آنتن و خط و همه چی
😐
شیراز از ساعت 2 تا 2:30 انتن همه اپراتور ها قطع شد
بندرعباس هم همینطور، قطع شد وحید جان تا الان
اینترنت و انتن های تلفن همراه تو قشم کلا قطع شد یهو
تقریبا ۱۰ دقیقه قطع شد
هم انتن هم اینترنت همراه
بوشهر اینترنت مخابرات و ایرانسل هی ده دقیقه ده دقیقه قطع میشه
خیلیاهم کلا قطع شدن از اشناهام
شیراز بعد از نیم ساعت وصل شد
کل سرویس های ایرانسل و همراه اول و شاتل حتی اینترنت مخابرات قطع بود
خط  ایرانسل هم برگشت
وحید سلام و خسته نباشی، اینترنت و خطا برای ده دقیقه کامل قطع شدن هم بوشهر هم بندرعباس، بوشهر وصل شده و نت همراه ضعیفه منتهی بندرعباس اینترنت ایرانسل قطع شده
وحید اصلا همه‌ی استان فارس همین شد
من فسا هستم منم قطع شدم
دقیقا از ۲:۰۲ تا ۲:۳۶ قطع شدم
وحید بوشهر هم کلا قطع شد الان وصل شده و خیلی ضعیفه یه نیم ساعتی کلا آنتن نبود
میناب هم یه ۲۰ ۲۵ دقیقه ای کلا انتن نبود
بندرعباس: ایرانسل کلا قطعه، همراه هم قطع و وصله
سلام اقا وحید داخل بندر دیلم استان بوشهر ما از ساعت ۱:۴۵ دقیقه هیچی انتن نداشتیم چه ایرانسل چه همراه الان درست شد تازه نت رو h هست
با تمام سیم‌کارت‌ها ما الان وصل شدیم
مرودشتم کامل قطع شده بود همه چی الان وصل شد
سلام وجید جان
ما برازجان هستیم
برای ما هم نت ایرانسل، همراه اول و رایتل و مخابرات کلا قطع شد
الان که برگشتن 3G هستن
سلام از جنوب استان فارس پیام میدم اینترنت خانگی و همراه و همچنین آنتن از ساعت ۲ تا حدود ۳۰ دقیقه کاملا قطع بود
بوانات برا یه نیم ساعتی انتن پرید
سلام توی یزد هم آنتن همراه اول کلا قطع شد، فکر کردم باگ گوشی خودمه، اما الان که گزارشات رو دیدم ظاهرا چیز دیگه ای بوده
درود وقت بخیر شیراز حدود ۲:۱۰ دقیقه کل خط ها انتن و اینترنتشون پرید و بعد از حدود نیم ساعت با سرعت بسیار کمی وصل شد
تشکر وحید جان
سلام وحید خط بستک و کل غرب استان هرمزگان بعد ۲۰ دقیقه وصل شد
سلام وحید جان بندرعباس الان 45 دقیقس که همه چی قطعه آنتن ایرانسل اومده ولی روشن نمیشه همه چی پریده فقط فیبر نوری وصله فعلا
سلام وحید جان :استان بوشهر :کنگان از ساعت ۲:۲۳نت ایرانسل و مخابرات پریده و هنوز وصل نشده خدا میدونه چیکار میکنن.
شهرستان
قیر و کارزین
هم ایرانسل هم همراه وصل شد اما مودم مخابرات از ساعت ۲ قطع
درود. از لاهیجان پیام میدم. اینجا هم امروز اینترنت مخابرات دو بار برای چند دقیقه رفت و بعدش با سرعت خیلی کمی وصل شد.
اصفهان هم حدود ساعت دو انتن قطع شد‌ ولی چند دقیقه بعد برگشت
سلام داخل اهواز کل آنتن ها قطع شد و سریعا به حالت قبل برگشت
مجدد همه چیز پرید توی بندر ماهشهر باز الان وصل شد
وسط بازی بودم پرید بیرون انتن رفت فکر کردم خودم اینجوری ام  از ساعت دو
الان وصل شدم دیدم بچه ها هم نیستن هیچ کدوم نوراباد ممسنی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/75864" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b5RQ-5xcNxOYwPAWMWenPQlhGHjDYvNov2K0ay4VHXFW-252jkej8Dv5YVLXAFQ8CX5j1HEkVSMPnKmlTtCZWBK0m0QVizgmMkt5E-XeU0-MHbxlS6aRSKD0S10Vy73k1MjLLof8GOK73TdKvZ1RFJOH8YLxLmaQSDLTVS44WRd5ER9ctXDr2fCUl_TzWauKy2tRqmex9gV3e3kWtcbqKaWmE5octCCzBpzHVKUqhubGASKTo6YpaNNSeJT-Mg-iYVwKDwzD5MUifEPFvbkjp9TPlOyWXg_m79ZMKacu-OQVkZ6dHcSnIyOtPz6vIt7fzPTMb2aJvAg97KlV8Sokww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگوی تلفنی با شبکه خبری «ای‌بی‌سی نیوز» اعلام کرد که به نظر او، توافق با تهران برای تمدید آتش‌بس و بازگشایی تنگه هرمز «طی هفته آینده» حاصل خواهد شد.
ترامپ روز دوشنبه در گفتگو با جاناتان کارل، خبرنگار ارشد این شبکه در واشنگتن، با ابراز خوش‌بینی گفت: «اوضاع خوب به نظر می‌رسد.»
رئیس‌جمهوری آمریکا با اشاره به تنش‌های اخیر افزود: «امروز مشکل کوچکی پیش آمد، اما همان‌طور که احتمالا پیش‌تر متوجه شدید، من خیلی سریع آن را برطرف کردم.»
او توضیح داد که این مشکل ناشی از ناراحتی و عصبانیت مقام‌های ایران از حملات اسرائیل به لبنان بوده است؛ ترامپ در تشریح نحوه حل این بحران گفت: «من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید؛ با بنیامین نتانیاهو، نخست‌وزیر اسرائیل هم صحبت کردم و گفتم تیراندازی نکنید، و هر دو طرف شلیک به یکدیگر را متوقف کردند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75863" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oTq4Y1avJkm71wqEPPuz6zFATPhuyv3AFE7bxgBwe-aEx9luzfo2WPnMAcPYToj4a-fXwOc69OTcLhNoB5ByycKqbVCR3_W3msqJQZ5iBc4aG8QsI8SnPThgKDbDUCOq6QQmcnoIxa4HjrhKh5wo75GZYPrCdp1MPh-68Bre8xXAT2eUtIiJ6cetmxOVCyxaUhhz_S7ekxGoNHFzG6xUiTat4Uuwo-ovAAOG21ntmS4-fI-mckUMLtUpj3VI0N8kDc_It46sKuWyaTd2XvKWQZuPIP-9EpzrVhudVLNpkIXS4icON3DRC3Rc_hg9YTnz1-db65t6rxI2gjMxqihDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
امروز با بی‌بی نتانیاهو گفت‌وگویی داشتم و از او خواستم وارد یک حمله بزرگ به بیروتِ لبنان نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
همچنین با نمایندگان رهبران حزب‌الله گفت‌وگو کردم و آن‌ها پذیرفتند که تیراندازی به اسرائیل و سربازانش را متوقف کنند. به همین ترتیب، اسرائیل هم پذیرفت که تیراندازی به آن‌ها را متوقف کند.
ببینیم این وضعیت چقدر دوام می‌آورد — امیدوارم تا ابد ادامه داشته باشد!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
خیلی شبیه به
پست چند ساعت پیش
ش به نظر می‌رسه. به نظر می‌رسه همون رو بازنویسی کرده ولی قبلی رو حذف نکرده.
نظر چت‌ جی‌پی‌تی:
در اصلِ پیام، تفاوت محتواییِ بنیادی ندارد:
هر دو می‌گویند ترامپ با نتانیاهو صحبت کرده، نیروهای اسرائیلی از رفتن به بیروت منصرف شده‌اند، و از طریق نمایندگان/واسطه‌ها با حزب‌الله هم درباره توقف درگیری صحبت شده است. گزارش‌های خبری هم نسخه اول را با همین مضمون منتشر کرده‌اند.
اما متن دوم از چند جهت مهم بازنویسی و تنظیم‌شده‌تر است:
۱. ترامپ نقش خودش را پررنگ‌تر کرده
در متن اول می‌گوید:
تماس بسیار سازنده‌ای با نتانیاهو داشتم و نیروها به بیروت نمی‌روند...
اما در متن دوم می‌گوید:
از نتانیاهو خواستم وارد یک یورش بزرگ به بیروت نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
یعنی متن دوم بیشتر این برداشت را القا می‌کند که ترامپ شخصا جلوی حمله بزرگ به بیروت را گرفته و نتانیاهو به درخواست او عمل کرده است.
۲. عبارت «حمله/یورش بزرگ به بیروت» اضافه شده
در متن اول فقط می‌گوید:
نیروها به بیروت نمی‌روند.
در متن دوم می‌گوید:
وارد یک major raid of Beirut, Lebanon نشود.
این مهم است، چون متن دوم وضعیت را جدی‌تر و عملیاتی‌تر تصویر می‌کند: نه فقط «نرفتن نیروها»، بلکه جلوگیری از یک عملیات بزرگ در بیروت.
۳. تماس با حزب‌الله با احتیاط بیشتری بیان شده
متن اول می‌گوید:
I had a very good call with Hezbollah
یعنی ظاهرا «تماس خیلی خوبی با حزب‌الله داشتم».
اما متن دوم می‌گوید:
I also had a conversation with Representatives of the Leaders of Hezbollah
یعنی «با نمایندگان رهبران حزب‌الله صحبت کردم».
این تغییر احتمالا برای این است که مستقیم نگویند ترامپ با خود حزب‌الله «تماس خیلی خوب» داشته؛ متن دوم آن را رسمی‌تر و غیرمستقیم‌تر می‌کند.
۴. تعهد حزب‌الله محدودتر و دقیق‌تر بیان شده
در متن اول:
all shooting will stop — Israel will not attack them, and they will not attack Israel
یعنی «همه تیراندازی‌ها متوقف می‌شود؛ اسرائیل به آنها حمله نمی‌کند و آنها به اسرائیل حمله نمی‌کنند.»
در متن دوم:
they agreed to stop shooting at Israel, and its soldiers. Likewise, Israel agreed to stop shooting at them.
اینجا حزب‌الله مشخصا متعهد می‌شود به اسرائیل و سربازانش شلیک نکند و اسرائیل هم به آنها شلیک نکند.
تفاوت ظریف این است که متن اول از «attack» استفاده می‌کند که گسترده‌تر است؛ متن دوم بیشتر روی «shooting» تمرکز دارد که ممکن است محدودتر از «حمله» باشد.
۵. متن دوم تردید و شکنندگی توافق را اضافه می‌کند
متن اول قاطعانه تمام می‌شود. اما متن دوم اضافه می‌کند:
Let’s see how long that lasts — Hopefully it will be for ETERNITY!
یعنی: «ببینیم چقدر دوام می‌آورد؛ امیدوارم برای همیشه باشد.»
این جمله نشان می‌دهد ترامپ خودش هم دوام توافق را قطعی نمی‌داند و بیشتر حالت آرزویی/نمایشی به آن می‌دهد.
جمع‌بندی کوتاه
متن اول بیشتر شبیه اعلام رسمی یک توافق فوری است.
متن دوم بیشتر شبیه بازنویسی سیاسی‌تر و شخصی‌تر همان پیام است؛ در آن ترامپ نقش خودش را برجسته‌تر کرده، تماس با حزب‌الله را غیرمستقیم‌تر توصیف کرده، عبارت «یورش بزرگ به بیروت» را اضافه کرده، و در پایان هم درباره دوام توافق تردید نشان داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75862" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lJ_vf3n7Cxoj9yaySqp2HJWEX0Ttzkj1SwhMvXKwYTa1q6NS8reOFuBdUxnHbApgBZ-FPv_7xbsFoVWbuf2aYgoIszSZ5nd28t6sQsnael4WgaMBUeZRhOsybusq-f8euNPsAusQ7LAukmD6GSjan5jb0jyRRgQAZq6I1JEm1pEqWWcasZekcjE_WmO3YJeYfTCrMvIEitvuVADja0WvLh_EnI3dgAMhpA2a0a827wkKkUgP6F3NybEOSqb2n56aJFI_mqOOFP8DJDpZf26zWWG3xLx81guRhCjhuGc54k3AhQERCROz_FYSH2c0yOMCA-uHTh33e5x76i18hqI7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری جمهوری اسلامی، ایرنا، روز دوشنبه ۱۱ خرداد از کشته‌شدن دو سپاهی در قم خبر داد.
این خبرگزاری ادعا کرد که این دو بر اثر «انفجار پرتابه‌های باقی‌مانده از جنگ اخیر» کشته شده‌اند.
طبق این گزارش، سپاه این دو نفر را حسین رمضانیان فردویی و محمد اویسی معرفی و محل کشته شدن آن‌ها را منطقه فردو، در استان قم اعلام کرد.
با این آمار تعداد تلفات سپاه در دوره آتش‌بس جاری میان جمهوری اسلامی با آمریکا و اسرائیل، و در خارج از درگیری‌های اخیر، دستکم به ۱۶ نفر افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/75861" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=e8RM7c0F_g09jAchskTkemN9kJNo1n7dZYKPK86yyKJuYuQlnAuj20Tx2JecMoq9qVIUYpvE02t220eo_uBqQAnvFZO5wHUmlWkfayoFd-ooHcUPgC3HZTIk44d0yxD9aPIi5mkZxMjhcFnXz_ePSZAIKFWicPfp0NCEZzJcvOMkRPvc7bA44Ksn23mL03BK2Edxq5b7N_WTzKO5aEtfx_cqpQWBpjF4oKsWvQ1dII9pN7gp04q4LS7dphiGQb7CdcDb04uqaQkvzBmWI7DCmlGDiyXtDG2lHQHcU6JCYOQHlKMqap25rjxSmHHDjEhkYBDljaL7Rfy3fc4ZFWRJUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=e8RM7c0F_g09jAchskTkemN9kJNo1n7dZYKPK86yyKJuYuQlnAuj20Tx2JecMoq9qVIUYpvE02t220eo_uBqQAnvFZO5wHUmlWkfayoFd-ooHcUPgC3HZTIk44d0yxD9aPIi5mkZxMjhcFnXz_ePSZAIKFWicPfp0NCEZzJcvOMkRPvc7bA44Ksn23mL03BK2Edxq5b7N_WTzKO5aEtfx_cqpQWBpjF4oKsWvQ1dII9pN7gp04q4LS7dphiGQb7CdcDb04uqaQkvzBmWI7DCmlGDiyXtDG2lHQHcU6JCYOQHlKMqap25rjxSmHHDjEhkYBDljaL7Rfy3fc4ZFWRJUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی سپاه اعلام کرد که در پی حمله ارتش آمریکا به کشتی ایرانی «لیان استار» در محدوده دریای عمان، نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی «ام‌اس‌سی. ساریسکا» با مالکیت «دشمن آمریکایی-اسرائیلی» را با موشک کروز مورد هدف قرار داد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/75859" target="_blank">📅 23:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0RCQ9TwnOtkU9m8993jR_snSEGry4hafKf7Y_Qfj-6bm7_QuFLLp1TdVvqhw02ZxvVLufcj8Wax6XKxyL-0Ssof1MGpfH9uEmk-x5aT52iHacAJoZdok99-4Zng3sTVOEq4Ty4ti-T1eAfwOvoS6llxcuvW7yrfMuyPZAw_Py5Qcm5oAWecleu9VtFF1bIe4nfV4QVtBdpHv-69yeDrWP-nyXL7hovyGJIYrsBaDkooHYZD6Ylt5BpHqh0YiNqJRjZLSS6UX6NY8QWhisnGCP47hGhbz-lNgcGvvnAreBtrDfcY-Grc10O7Cw-cc2YJfVEbWaqFjNOc6pKV4nvQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام دونالد ترامپ مبنی بر موافقت بنیامین نتانیاهو با توقف گسیل نظامیان به بیروت، در شامگاه دوشنبه ۱۱ خرداد ماه، با واکنش منفی چند چهره شاخص سیاسی در اسرائیل مواجه شد.
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل، با انتقاد از این تصمیم گفت: «زمان آن رسیده که به ترامپ نه بگوییم.»
همزمان نفتالی بنت، نخست‌وزیر پیشین اسرائیل، نیز در پیامی دولت این کشور را به ناتوانی در حفظ امنیت متهم کرد. او با اشاره به حوادث امنیتی در اورشلیم، بیت‌شمش، لبنان و غزه نوشت: «مکان‌ها متفاوت هستند، اما داستان یکی است؛ دولتی که کنترل بر حاکمیت اسرائیل را از دست داده است.»
بنت همچنین گفت: «هرج‌ومرج در همه‌جا دیده می‌شود و ما امنیت را به شهروندان اسرائیل بازخواهیم گرداند.»
یائیر لاپید، رهبر مخالفان دولت اسرائیل، نیز با انتقاد از نتانیاهو، تصمیم او را «اعلام تبدیل اسرائیل به یک دولت تحت‌الحمایه کامل» توصیف کرد.
@
VahidOOnLine
دفتر نخست‌وزیر اسرائیل در بیانیه‌ای به نقل از نتانیاهو اعلام کرد: «امشب با رئیس‌جمهوری ترامپ صحبت کردم و به او گفتم اگر حزب‌الله حمله به شهرها و شهروندان ما را متوقف نکند، اسرائیل اهداف تروریستی را در بیروت هدف قرار خواهد داد.»
نتانیاهو افزود: «موضع ما در این زمینه تغییری نکرده است.»
او همچنین تاکید کرد ارتش اسرائیل به عملیات خود در جنوب لبنان طبق برنامه ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/75858" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z4au43nxpJb-0xxjK2IjSvYVC-ehmd51OGbl7peT_nQxXSZ-3AiOoXeddbD-hl_vkCVDZmygm_C4ixuCQSqmlGleL0YOehzsXp_uwYQosjvF7u3jcJJ3MnwA1Qi9E_irFT47KH12gbd6ztn6n8z3nqukSnyQPuTSlCxBBbZbxjGX2R21EaDIINtH7KKa_vb5IaVKm1gtobIIPRHkGZzGfkc7UXNvGvgcsnESao2Bd3ns0n49D6WLny7ColVGv_Bt9sTlddWR9B_29T_BBVqxIXqEHAezgJGeLxQpj824ya7wFoPxmXK0dQNdLtgny7LA-OIL_rxOepgXT8sqeK-qqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی: ادامه حملات به لبنان و غزه، باب‌المندب را به تنگه هرمز تبدیل خواهد کرد
اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، شامگاه دوشنبه ۱۱ خرداد ماه در پیامی که رسانه‌های دولتی ایران منتشر کرده‌اند، نوشت جنگ اسرائیل در لبنان و غزه «در سایه حمایت‌های وقیحانه آمریکا، عزم محور مقاومت را برای توسعه پشتیبانی‌ها از هر دو جبهه، اقدام برای فعال‌سازی سایر جبهه‌ها و همسان‌سازی وضعیت ترافیکی تنگه باب‌المندب با تنگه هرمز رقم خواهد زد.»
فرمانده نیروی قدس سپاه همچنین هشدار داد که ادامه عملیات اسرائیل در جنوب لبنان و غزه، این کشور را با واکنش‌های گسترده‌تری از سوی حزب‌الله و گروه‌های فلسطینی روبه‌رو خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75857" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jWN5wL9u7l9T7qYEyjkdJxfKbfz6r0LV4p2fHGSmagROJPmx8B4upijyQGfjtPvdkCbeXI13-GmnLCu5JKBnx7xJoYJBzkYmxIw48oKGQdntPCu-kB2WZvJg1pMvH5OKR7QqEV-eIWUanWRHzTJqDy3oy3zSavF9eMXtaY2z1Acqi97dkrtlTigkX9NKm3H_jVSPvQxrZenm6ZNe8SUe-aY4jyu-VN_Imx-lkFdZT-7ZbKGK0bGa-hXUBtl_Y-0JgBgHbCk3-bGVSymujlan2-d7gbwA5KVmT9RCXIlCdTqiCJoL0zw3DQpnA-jeUjUc5f4X0dvdUVqWNPmwcs5JPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات با جمهوری اسلامی ایران با سرعتی بالا ادامه دارد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
این دفعه گفت "جمهوری اسلامی ایران"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75856" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JUS41G8WViMu-a0daVUCxIwJH1x0jEX4nSn__HSvvgoTcgn5JKNqbj16sH_9p0nR52lG4UUUY4vZOo9D6ZaP5TKrSK_oANfDkdO9wD94YdGrK9q7RxmlWnlqEAwm3qTm73w9I1ySazXxGt_Y22cFdt_NEU12Gs5naPJTUN78Vn8PogwvtT7QxC5YUuE537oHiC4cHBSd5-NblARj5hQRgvBUi0rZuTg5X_Ey0T3i3BeMltmHO5g3xYsR6_KvRSvqs1eF2jem2-6oJPsiN3lmXJq3-KwBek8q_b3g-qiDdhaprJMYM4Qe2Kwm2ld36V4El_BGwCUN9WI6huVgvI6zpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و حزب‌الله پذیرفتند حمله‌ها متوقف شود
ترجمه ماشین:
من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل، بی‌بی نتانیاهو، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد؛ و هر نیرویی هم که در مسیر بوده، همین حالا بازگردانده شده است.
همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها پذیرفتند که همه تیراندازی‌ها متوقف شود — اینکه اسرائیل به آن‌ها حمله نکند و آن‌ها هم به اسرائیل حمله نکنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/75855" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/snAwmCg2xSTLKLJsI8SoM2x5We4KLWwne2ImcMQ7UiBJgfAXoK24T_bwNNz0EiiRlrzRYDL2QMG--HI4cZZYsjzoUpT2UoU54h5ZYYIkikoygJDIfvFczEF7cj2nw77l1oBhIDh8MZhd5Z6LLvWW2Oea32hEFE8AzlkuAlU18MClALHDvBwcN5xZFt2qxsuh0IwtFpwmYObgvSNDxFK3vIwUpTk4SEzqpIruMnuu0ghKss6UGGhQWl5xPSwuvRTAt8mGaERmkq3Aw39HH8qzKLynFSVzEUHWMy1tY1QNap_zu-yzdoMD_c3-9Irrev8MHA--DDLKxmXnjmNziaBpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: محاصره را حفظ می‌کنیم
توییت‌های خبرنگار NBC، ترجمه ماشین:
تازه: رئیس‌جمهور ترامپ به من گفت که درباره گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا، چیزی از ایران نشنیده است؛ اما اگر درست باشد، اشکالی ندارد:
«فکر می‌کنم اگر حقیقت را بخواهید، زیادی حرف زده‌ایم. به نظرم سکوت کردن خیلی خوب خواهد بود، و این می‌تواند برای مدتی طولانی باشد.»
او ادامه داد: «این به آن معنا نیست که قرار است برویم و همه‌جا آنجا بمب بریزیم. فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم. محاصره یک تکه فولاد است.»
آیا می‌تواند آن‌ها را آن‌قدر منتظر بگذارد تا کوتاه بیایند؟
«فکر می‌کنم تا هر وقت که بخواهند می‌توانم صبر کنم. آن‌ها دارند ثروت هنگفتی از دست می‌دهند...»
همچنین وقتی از نویسنده کتاب «هنر معامله» درباره گزارش‌های تعلیق مذاکرات پرسیدم به نظر می‌رسید با اکراه نوعی احترام برای مذاکره‌کنندگان ایرانی قائل است:
«این حرف مناسبی است، چون آن‌ها مذاکره‌کنندگان بهتری هستند تا جنگجو.»
GarrettHaake
الان هم:
ترامپ و نتانیاهو دارند تلفنی صحبت میکنند.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/75854" target="_blank">📅 20:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vChj3x0JfRwbYzJ0YEz3g16NgxQiaUnJxUmNBx84cS2S2_qIcHCpBWh4JZlSFB-dxO8YrOg9D9vv4UDlDIslattogMGXbcr4YR4yEcTAW0qmj4XeMTGSvynxscZPcPmA6NJhcKv-LuYl6tAO_jH3PXw4oFu7Z0sbm_oRhtFHpRYVKH7jOjsrAfGVU5ots7n0gN66AVqa2pTTqvrcb17zGo8vI_jueyLt6n0L3ov58M3sEOUsFTyqzYmWqz_uUAMhaDgK91Xm2q6FOnNdhNzaiqtltf5sOxwWW60neEGi1VkL9skt0Au4GVApOT9fkVEKkYIUeTA1NK1uKOkqZskzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با صدور هشدار تخلیه از سوی ارتش اسراییل برای ساکنان حومه جنوبی بیروت، فرمانده قرارگاه مرکزی خاتم‌الانبیا به ساکنان مناطق شمالی اسراییل هشدار داد که در صورت عملی شدن تهدیدهای اسراییل علیه لبنان، برای جلوگیری از آسیب، این مناطق را ترک کنند.
علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، اعلام کرد بنیامین نتانیاهو «در ادامه شرارت‌های خود در منطقه»، ضاحیه و بیروت را به بمباران تهدید کرده و برای ساکنان این مناطق هشدار تخلیه صادر کرده است.
او افزود: «با توجه به نقض مکرر آتش‌بس توسط اسراییل، در صورت عملی شدن این تهدید، به ساکنان بخش‌های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75853" target="_blank">📅 19:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=MZyvw46Yt9M97SnWb0GV6_PnZJF5D6cQurUDuVvsl1R4Umiubfo6ZhF6dQ_cCam8KeFS4NVIKAf-BfpU4BEWmoS4bLsZ_96C8-gROjaixTk9DofLpsw9BGZ9fldHZL1KJu2LusbKb-Srgd1r9fxNPINLshP0OnboT3DlkH0zC7o_3vjeSLogZtR_q8LwAH5-2Q7RLr_m_N7oEn3HbdhEkmQcOLnNNAa4QqZm0p0myFIV91h2nUfdKYetA9DMkDw3m0XQHIDkzDF7zhC2uSFOVmwrWtjxeZoUhPYlS7VE_z2lJsi6ddtYfM6VS7uk_VA4HKkkkdkdle3PBe6csgxNuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=MZyvw46Yt9M97SnWb0GV6_PnZJF5D6cQurUDuVvsl1R4Umiubfo6ZhF6dQ_cCam8KeFS4NVIKAf-BfpU4BEWmoS4bLsZ_96C8-gROjaixTk9DofLpsw9BGZ9fldHZL1KJu2LusbKb-Srgd1r9fxNPINLshP0OnboT3DlkH0zC7o_3vjeSLogZtR_q8LwAH5-2Q7RLr_m_N7oEn3HbdhEkmQcOLnNNAa4QqZm0p0myFIV91h2nUfdKYetA9DMkDw3m0XQHIDkzDF7zhC2uSFOVmwrWtjxeZoUhPYlS7VE_z2lJsi6ddtYfM6VS7uk_VA4HKkkkdkdle3PBe6csgxNuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«حمید سلیمیان» در حال نواختن تنبک
#حمید_سلیمیان
، متأهل و پدر یک پسر چهارماهه شامگاه ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در زرین‌شهر اصفهان با شلیک مستقیم گلوله جنگی جان خود را از دست داد.
حمید سلیمیان راننده یکی از شرکت‌های فولاد بود و به گفته نزدیکانش به موسیقی علاقه فراوانی داشت او  تنبک و سنتور می‌نواخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75852" target="_blank">📅 19:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pgWAWNDHG8wb_Rc5MUP5t4KaLIkBdxNmxqbDojFPS1pSFYx1JZGo4vq2rGI70LwCIkdIyYzWpuy-oaBYwxDhTuN3kzGzGk9vdm1ome0C2ZN6TwH250Gx0zdUdmABjBNf-GuVQW6dNb8LtR8i25tGtspbUjzrSo2zflFK02yljbxpL2I3XvP-__HexJfwF4oVh8HiDbEG77WmOva29zAqooD1rqLKTqz_A7iSNU01b1h1jsJEtSf1Z3wI2dlLrb32MOCdFvPANryXbToZKz194ej8EFJgGjSQcQamGMpGj7G2bDq1GkzTw0MMFRRqvdN8Khau4bZ5sYxP3TCi7kROhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pCgOU3S7A-UVU1-aFSU7iQpX00Cltc2xvWNv98ho1VHLm5BXtV2pkIe-74cLoyGGGQext_pm3LIMogG7Z2Eq0SKfa6EyHamyqKATRgq3AtyyWy0zkb_Pyxh50-Km1tmijYKFbJSc_TW9L8FTw2FxVv4lJQjbI_4yJ25u5mM3D_EkUnR8eVasaqpeaWhoCuJEieViSyw5k5ovFcz5OPNH_Fufr9GXSstrmA1dgwS1Rev6Eh5SLWO8WqFHbTd7LvPQESOPo7wiOU7d5jazVD76O89_Sbzw2wpeghGL6bGk8RpSzQFWNbDfp0h47-Lf0eVwq1csXCPyy_iMouhfLYZ6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JkI3v8RACLqrYBoBOYmtEeHHJkrTeu8kr9Q1YVc3OfhYmWxZunLIXhc4TRLCoddOpcmYyyFsJ9DCDTUh-43tbk2BhAcx6WqK-3L60cKGWGtdJxMIpXmjud3edGjYy0HyI-x130I2-Fh4RTzdT3BkBQDp5TcFiJNaCrvKA7JuLIOoRHZ-MP6Luqqz4orElizRbsOjTCWAGWW_83lh-IIXHufv9jPRz0ISuZiH0jTIeofAZmf3OP2e2BJIktcs66TetKQyHacOy_TXi9V5duSyBYZeb0NbSCZbhRiJTvgSZadC7PjHSlCfIHo2aop13yoa0PV_gx8Z2zRUsMPmq3d_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hpPsrMG1P9L3STs8xO5-1vf5zHoH7o7wZWtsozx4LF1FFg_0SYlxZGvRY9I3Tun6GtGVfBosDrwVCjqiCckqmTdveAtYe4IR6bYbDUqjKuil_pWoHJFI9gEMT7WYjGrss_Btxlwn0RfOci8BClWXpO7RxtVn9sjOk87epqw3YcE4RjpB7s9L5cJymocv6U1obxQqV3wE4GP30YVfv4rSeF9xcmxS_IIvYqKRNJ8XHwL8ZPwKV9-XjiR2gLQVMfVTl-rShv66KSDPuOrQP0hXyKeoZeJn_k4pcFTukZ8-hCzZKUdwPxxS6G3GGj_TI2iuSucWF29N58Wm2Dute7qk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tG9ha9Kq9rAQaX0Ax1zIE3rgUVQrY1H8tBL7eVJYfTSNetbuMQBIdE0KjU2t7VQAwGU27KVGoWbu9ARPaIk4mvKABkZ5Zn78D46iPe_gxoBcljsSlAhX02MxPXZiwOuCBU5sijqLEx7IPaemKR2Irhmzg77PzX40DA9R41s4m5WadKv-v7eN7XybxuIgDLV7NA5bkVfk5vck4wv7I-wS7Yrh1p7D4Y0mgNANgSj_gEroRykrwIGSc_IMYrksxAVyX_hc0sv9gVuLg9AocKq2GP4wBLauN9d22-9CwQ6UjiMEQS35vaGYxecYVLSrAYOzen_hyLKmI25N05GZ-PX9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mNiPPxHWoVWjKhgDDwIBwSDUw7jFuv806YkUkyPI8ocrOm7ljvE-gYagqLh7ludUDE_GpgPGmtsbGGesXH8UaEvXWiY0keWIWSmpWAtFOBouHWTx3RasHHPX4uWNa85mYiWyxw5ekCBEAFAiPxFb24cGCuGoMwzfK26QKfWrs_c53HCIz7O4M3ynQ45aAw6hzT-hYsRx_BlBl31cOMy9jP4WRvsmKnMg2O-agaXiaok0XHpNjNKKFKuKOrCKAUA6Tfty1F2BZSvCjmXjjM8thqkkjp8nyTst2uYGp-y5PYBrAiyV7qjgU5syiQBDkI3Zxhlm7-PM80MijF9qz_TlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jkG7BrmhZBTRDJQrYmz8eVeD9Y6ciSRee5uOK1MM5ESVnhiSW_GVj_1oS-_uVWXuOAMyYP3AepcXLW8lV3hspsQS0DajQkCWkl-pyr-K4HwgrAPCFxDjjpmyxkWBlBJlmJC6TVkpD5pjTRHKr68h1AmmcwtRlHFdINVQMrJlESewFZNOjgGDSZCLQjctCXe5WiJk5pzG_yBwdNm5N3LLDWne8rdJC56sRoMNsmdhjU9C72upygvCvu4YtoCTbirp8DUacir41UCIcxOgTg87zQ9KZbqzwhSH1zgNuYE-aF2QN-FNRC-7Y_AI2vhD1q3QVvdtoSC5k2zIANhu0UsCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NdXzlexAPjiq3fy0FhHaVGap45ARyJvBF7HxDu-9ZC_fEcHpqRNPMp72G9kMQbS3gplQScyPLeJiSX1naxbcI3EJxfz8V3i7iKaB6JrPCOQ8oigtoMllQ0vyJp-A-ABOdLpB9ZR2Ibmj_dGD_WQWO9BCTHi7zXsWLw14o0mb7Mq3QRfDqstkiyj2L9QII8eXLSculCo-EhBM1IWBRomS9AwB4uPoklg22exYP5SVm_JiNKww_mz1PPS3JOmTncxBUSMMVhnmDyQ3mis4pw21kEYU5_ehOwRF4WjYHKI1Mabu3kojTI5_My_QYZesF8cx04GgmzRrG5BtNemDGHwV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DjZ0BmV0hoZsvijC_pTKzcFWPUoMDgsx6fYdnYi6QsbUfVMiux0w1HzvKInl-aK21_ShvuNFyYoIXuinqL6Cx9Spvzh4iplxZp7COS5KgH6QZLG_D5sNQeYc0vTd1kD5D0wFb3fP4jk-Cu24p9z0j8mTNsv14aKgMZLmQgISOyIzBVrpInmXNdzc9WbQyYZDQpTWAxbGrjZjSAurvRT1pFjeSWOSiLE0XSbjtLRgCFdm_WaBPJcNqhYyv-oim3ZlF863LrW6_Pme0VF7sdvWaVFfZOsnznES-C2BDKGvj0mtoshlnIYayEmqVtNyK23xuNdPMWbcy9BZ0syuaPELhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با تشدید حملات نظامی اسراییل به لبنان، مقام‌های جمهوری اسلامی بار دیگر تاکید کردند که هرگونه آتش‌بس میان ایران و آمریکا باید شامل همه جبهه‌های درگیری، به‌ویژه لبنان، باشد و هشدار دادند ادامه حملات به این کشور می‌تواند پیامدهایی در پی داشته باشد.
بنیامین نتانیاهو، نخست‌وزیر اسراییل، روز دوشنبه ۱۱ خرداد ۱۴۰۵، اعلام کرد که به ارتش این کشور دستور داده است اهداف متعلق به حزب‌الله در ضاحیه، حومه جنوبی بیروت، را هدف قرار دهد. او در یک پیام ویدیویی گفت: «هیچ وضعیتی وجود نخواهد داشت که حزب‌الله شهرها و شهروندان ما را هدف قرار دهد اما مقرهای تروریستی آن در ضاحیه بیروت از حمله مصون بماند.»
دفتر نخست‌وزیر اسراییل در بیانیه‌ای اعلام کرد نتانیاهو و یسراییل کاتس، وزیر دفاع این کشور، در پی آنچه «نقض مکرر آتش‌بس از سوی حزب‌الله» و «حملات علیه شهرها و شهروندان اسراییل» خوانده شده، به ارتش دستور حمله به «اهداف تروریستی» در حومه جنوبی بیروت را داده‌اند.
نتانیاهو همچنین گفت عملیات زمینی ارتش اسراییل در لبنان در حال گسترش است. اسراییل در جنوب لبنان منطقه‌ای امنیتی ایجاد کرده و می‌گوید هدف از آن جلوگیری از حملات حزب‌الله به مناطق شمالی این کشور است.
در واکنش به این تحولات، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در شبکه ایکس نوشت: «آتش‌بس میان ایران و آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمام جبهه‌ها، از جمله لبنان، است.» او افزود نقض آتش‌بس در هر جبهه‌ای «به معنای نقض آتش‌بس در تمامی جبهه‌ها» خواهد بود.
عراقچی همچنین آمریکا و اسراییل را مسوول پیامدهای هرگونه نقض این آتش‌بس دانست. جمهوری اسلامی پیش از این نیز بارها اعلام کرده بود که آتش‌بس میان ایران و آمریکا باید سایر جبهه‌های درگیری، به‌ویژه لبنان، را نیز در بر بگیرد.
ابوالفضل شکارچی، سخنگوی نیروهای مسلح جمهوری اسلامی، نیز به اسراییل هشدار داد که «تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود.»
هم‌زمان، محمدباقر قالیباف، رییس مجلس شورای اسلامی و رییس هیات مذاکره‌کننده ایران با آمریکا، با اشاره به آنچه «محاصره دریایی و تشدید جنایات جنگی در لبنان» خواند، این اقدامات را «شواهد آشکار عدم پایبندی آمریکا به آتش‌بس» توصیف کرد.
قالیباف در پیامی به زبان انگلیسی در شبکه ایکس، بدون اشاره به جزییات بیشتر، نوشت: «هر انتخابی بهایی دارد و زمان پرداخت آن فرا می‌رسد. همه‌چیز در نهایت سر جای خود قرار خواهد گرفت.»
این اظهارات در حالی مطرح می‌شود که عملیات نظامی اسراییل علیه حزب‌الله، از گروه‌های مورد حمایت جمهوری اسلامی در منطقه، شدت گرفته است. با وجود تاکید مکرر تهران بر ضرورت گنجاندن لبنان در هر توافق آتش‌بس میان ایران و آمریکا، این مطالبه تاکنون محقق نشده است.
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، نیز روز دوشنبه در نشست خبری هفتگی خود گفت: «ما تاکید کردیم و کماکان تاکید داریم بر این نکته که آتش‌بس در لبنان بخش لاینفک هرگونه آتش‌بس و هرگونه توافق نهایی برای خاتمه جنگ است.»
او همچنین حملات اسراییل به لبنان را از عوامل ایجاد تاخیر در روند دیپلماتیک برای پایان دادن به جنگ میان ایران و آمریکا دانست و بار دیگر بر ضرورت برقراری آتش‌بس در لبنان به عنوان بخشی جدایی‌ناپذیر از هر توافق نهایی تاکید کرد.
@
VahidHeadline
تازه‌تر:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد که جمهوری اسلامی در واکنش به ادامه حملات اسراییل به لبنان و آنچه «نقض آتش‌بس در همه جبهه‌ها» خوانده شده، روند گفت‌وگوها و تبادل پیام با آمریکا از طریق میانجی‌ها را متوقف خواهد کرد.
تسنیم همچنین مدعی شده است که ایران و گروه‌های هم‌پیمان آن در «جبهه مقاومت» در حال بررسی اقداماتی از جمله انسداد تنگه هرمز و فعال‌سازی سایر جبهه‌ها از جمله تنگه باب‌المندب هستند. این گزارش می‌گوید این اقدامات با هدف واکنش به حملات اسراییل و حامیان آن در دستور کار قرار گرفته است.
@
VahidHeadline
ارتش اسرائیل در بیانیه‌ای به ساکنان منطقه ضاحیه در جنوب بیروت هشدار داد و از آن‌ها خواست برای حفظ جان خود این منطقه را تخلیه کنند.
در این بیانیه آمده است اگر حزب‌الله به شلیک راکت به سوی شهرها و شهرک‌های اسرائیل ادامه دهد، ارتش اسرائیل اهدافی را در ضاحیه جنوبی هدف قرار خواهد داد.
در ادامه تاکید شده است دولت اسرائیل با مردم لبنان در حال جنگ نیست، بلکه با سازمان تروریستی حزب‌الله می‌جنگد.
@
VahidOOnLine
در پی اعلام خبرگزاری تسنیم مبنی بر توقف «گفتگوها و تبادل متون از طریق میانجی» میان تهران و واشنگتن، بهای جهانی نفت بیش از ۵ درصد افزایش یافت و به بالاترین سطح خود در هفته‌های اخیر رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75843" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fol39AQftNBiEyuB4xNyEEb_6267rLjYM1y0-tiKvjsQhUxbJu9q0ehqXdv77ymJlaKUh80KSqAFwqhjB2o3Hz72LIAXflZorianNm_ZaUH5Ew7Bg4XqEcYpBtACSCNA_QruDgwoAg_u3DOGi69lIQkvXMpz7j25LXKNZMDj3dOQRi_UwIgO7vrZz0cZp3qkYsUpJeNTokTZwSO7FR-ucW6l4bmLlQ-0ZoMYS8-6zOhxPSWzNfREYEOKey9wUkQCQwONP1PyYDH9gIcDCYe27m37sTTU169uazrV9kXDFq-36_VengA8VXYQG1X0YMkD7Q43cqlN8Pzgoyeq04esqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از کشته شدن یک دانشجوی زن در دانشکده دندانپزشکی قزوین به ضرب گلوله خبر داده‌اند.
میزان، خبرگزاری قوه قضائیه، از قول دادستان قزوین نوشت: «بررسی‌های اولیه نشان می‌دهد این دو دانشجو که در آستانه فارغ‌التحصیلی قرار داشتند، در مرحله متارکه از یک رابطه عاطفی بوده و پیش از این نیز اختلافات خانوادگی شدیدی با یکدیگر داشتند. صبح امروز، مرد جوان با یک قبضه سلاح کلت جنگی وارد محوطه درمانگاه شده و چهار گلوله به ناحیه سینه دانشجوی دختر شلیک کرده است. شدت جراحات وارده به‌حدی بوده که متأسفانه وی در همان محل جان خود را از دست می‌دهد.
در اطلاعیه دانشگاه علوم پزشکی قزوین در این باره آمده است: «انگیزه این واقعه، مسایل شخصی و خانوادگی بوده و ارتباطی با فرآیندهای اداری یا محیط آموزشی دانشکده ندارد.»
به گفته حمیدرضا قافله باشی، رئیس دانشگاه علوم پزشکی قزوین، «این تیراندازی به دلیل خصومت‌ خانوادگی اتفاق افتاده و دو دانشجو که زن و شوهر بودند در اثر شلیک جان خود را از دست داده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75842" target="_blank">📅 19:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی از تهران درباره صدای پرواز یک جنگنده یا هواپیمایی دیگر مربوط به جمهوری اسلامی:
سلام تهران صدای جنگنده اومد همین الان
غرب تهران وحشتناک صدا جنگنده میاد ۹:۱۵
صدای جنگنده داره میاد غرب تهرانم ساعت ۹.۱۴
سلام وحید همین الان تهران صدای جنگنده میومد نزدیک ۲ دقیقه
شمال شرق تهران صدای جنگنده
سلام تهران صدا جنگنده شدید
الان از بالا سر ما صدای جنگنده اومد
رد شد رفت
همین الان منطقه گیشا صدای جنگنده میاد
همین الان ساعت ۹:۱۵ دقیقه صدای جنگنده سمت غرب تهران اومد(فکر میکنم جنگنده ارتش بوده باشه)
سلام وحید از سمت لویزان تهران موشک بلند شد
وحید الان ساعت ۹:۱۵ صدا جت منطقه ۲ تهران
تهران-فرمانيه
ساعت 9;16 صداي جنگنده مياد
وحید تهران ساعت ۹:۱۷ صدا جت میاد زیاد
هروی
الو سلام تهران سمت شهرک غرب صدای نمیدونم هواپیما بود جنگنده بود چی بود خیلی نزدیک بود
الان ساعت ۹:۱۷ دقیقه در قیطریه صدای جنگنده اومد
شرق تهران صدای جنگنده شنیده شد الان
سلام تهران صدا جنگنده شدید
احتمالا جنگنده های خودشونه
ساعت۹:۱۷
سلام دوشنبه تهران ساعت ۹:۱۵ صدا جنگنده من شنیدم سمت هروی
صدای جنگنده تهران ۹:۱۷
صدای جنگنده منطقه ۳
خیلی پایین بود
تهران صدای جنگنده اومد
سلام ساعت ۹:۱۵ سمت دروس تهران صدای جنگنده اومد
صدای جنگنده شمال تهران ساعت ۹:۱۵ رقیقه
سلام ساعت ۰۹۱۵ دوشنبه صدای پرواز چند جنگنده شمال تهران
منطقه ۳ صدای جنگنده انقدر زیاد و وحشتناک بود که از خواب بیدار شدم
سلام  پاسدارانیم صدای جنگنده اومد چند دقیقه پیش
صدای جنگده نارمک
سلام وحید. صدایی که ۹:۱۵ اومد شبیه جنگنده بود ولی از پنجره نگاه کردم شبیه هواپیمای مسافربری بود فقط نمیدونم چرا از ارتفاع کم حرکت میکرد
سلام آقا وحید من خونم گیشاسصدای جنگنده نبود هواپیما بود من بالای خونه رفتم دیدم ولی هواپیما بزرگ بود ی مقدار دیگه باری بود یا سواری نمیدونم ولی از بالای گیشا رد شد
من از روستای اطراف شهریارهستم یه هواپیمای مسافربری بزرگ تو ارتفاع پایین از بالا سرمون رد شد به وضوح دیدمش صداش زیاد بود
سلام وقت بخیر نیاورانم صدای جنگنده اومد وحشتناک بود
وحید من شهرک محلاتیم
بین ۹:۱۵ تا ۹:۲۰ صدای جنگنده میومد
(با ارتفاع پایین)
سلام وحید جان صدای وحشتناک جنگنده ۳ ۴ دقیقه پیش خونرو لرزوند
-هواپیمای کارگو سپاه از تهران بلند شد
.
-صدای جنگنده برای این بود؟
-ممکنه برای اسکورتش بوده باشه
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/75841" target="_blank">📅 09:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی از
#بندرعباس
درباره شنیده شدن صدای سه انفجار:
بندرعباس ساعت ۹:۰۷ سه تا انفجار
الان بندرعباس ساعت 9:7 دقیقه 3انفجار قوی
یک صداهایی شبیه برخورد جسم سنگین (بمب یا هرچی) به زمین داره میاد از دوردست.
بندرعباس ساعت ۹:۰۹ صبح دوشنبه
سه تا صدای  انفجار اومد بندرعباس
ساعت ۹ و هشت دقیقه
دوشنبه، ۱۱ خرداد ۹:۰۷ صبح. بندرعباس.
صدای ۳ تا انفجار از نزدیکی پایگاه هوایی شنیده شد.
آپدیت:
خبرگزاری تسنیم وابسته به سپاه مدعی شده که مربوط به مهمات خنثی نشده بوده. البته دو روز پیش‌تر از این هم اعلام کرده بودند که طی ۷۲ ساعت آینده قراره از این صداها شنیده بشه در بندرعباس.
پیام‌های دریافتی از
#اصفهان
درباره شنیده شدن دو صدای انفجار از دور:
پیام ساعت ۹:۱۷: اصفهان صدای انفجار میاد، دو بار پشت سر هم
اصفهان همین الان صدای انفجار اومد سمت ناحیه ۶
الان اصفهان یه صدایی مثل صدای انفجار اومد
سلام وحید، اصفهان ساعت ۹:۱۸ ۲تا صدا مثل انفجار و کمی لرزش حس کردم فاصلش خیلی دور بود، بین ساعت ۸ تا ۹ هم یک صدای مشابه اومد فکر کردم توهم زدم
اصفهان صدا انفجار نزدیکای جی شیر(مطمئن نیستم)
سلام. اصفهان حدود ساعت ۹:۱۵ صدای ۲ تا انفجار به فاصله چند ثانیه.
نمی دونم چیزی زدن یا دارند مهمات خنثی می کنند. البته تقریبا هر روز صبح یه صدا میاد که به خنثی سازی میخوره.
امروز ۲ تا پشت سر هم بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/75840" target="_blank">📅 09:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6yN6XR98TYEPydzdKFqHTiJ47WDIFaD9ZZOMo9seQsPQeNnXWpkvIh8zUmU-DRVml0MnCgPwEuwCNjD8pa0u9f7ZBYlbLtnd1AAZaRNRggitIbeM7o8BLosfT_yLAKeq3Yb8yJ1W6w3L7RN3xOSSnMYtUtvDjNeb_kNUcg1OFxsIYPsYzEC6W5Ekhj-Inzm_dhOtLZ0gpI_S7i9wrn9FZh8DeogGmmmMGVFERasvELaVvXDml82PCYf59wY9NjGlmlx7GR7vCImkuug4yzjVbOsub7_uk3-KrzL-h6KWFrjxBSJ80rHM_Ev9flh63rqXJbdgwfwrUrsYP_BLWRz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌های کودن و بعضی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند وقتی سیاسی‌کارها مدام و با شدتی بی‌سابقه غر می‌زنند که باید سریع‌تر حرکت کنم، یا کندتر، یا جنگ کنم، یا جنگ نکنم، یا هر چیز دیگری، کار درست و مذاکره برای من خیلی سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت — همیشه همین‌طور است!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/75839" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی:
امیدیه خوزستان صدای انفجار شنیده میشه
از امیدیه خوزستان پیام میدم
طرفای ساعت ۸:۱۳ دقیقه صدای ترکیدن اومد
ساعت ۸:۳۱ دوباره زدن
همین چند دقیقه پیش صدای انفجار واضح ای اومد
امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75838" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد [گیشا]»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» اعدام کرده است.
نام این دو معترض که بامداد دوشنبه یازدهم خرداد اعدام شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
میزان نوشته این دو «از عوامل اصلی آتش‌زدن مسجد جعفری در محله کوی نصر تهران [بودند] که اقدام به تخریب و آتش‌زدن مسجد، تخریب اموال عمومی، درگیری با مأموران حافظان امنیت، انسداد خیابان‌ها و ممانعت از عبور و مرور مردم کرده بودند.»
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75836" target="_blank">📅 08:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZCs6BHA5nCu6x3lLVK5gGv4njza7uX27PnrwsgwiLNeYipPfQ7tGGIibcf3Bauvti4Db6hV4s8ocoh1eIpacWwq72PwGXpHCjmPWVDYHdqPz-xYJSO2Vw4hVKGYuRaP_FPGldg7AtG5ayK_hLm3ArmnsSX2aDLHu4uqeDFxv7Oa7Q_5VptS8lzxPW6th69KGmuTIyoQGMtmK5WM1gpTSOy_oEVYmmYPVP4_FP-Fun1fYSfEOMrtbOKrpFchwcO6whLBencMKLR2WXh7EWPaIMerPnyl5DWLM-GAAM13JCUVVYgc-Q4O7ZphK_7B55TNJxSZX1-OQ5NbWZP1EdIYVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ma3W1RmqInath66cN-mEXYlbG6Nv95_G8KwVhuMsZ9cuAI26AUIFBfm01tQ9blMol9E8KZ4mtZi7nNaVCS7ZhHtcKLJZmR-WSKg8R9ybT2DvlJh46NcHnLeFoES31JtEuojo5FfQ7NMPlvaMZ8OvS4pF5RB1KyHaRFVVZYj2nXTc7-nh1Cup6trJqDAqChjbI_ghtvgzJaDvBslNSRWAi0u18xrexmpRP8GqS_65f3Mkd3e2V48XCb2iFPFRiZ350b98wCszbKLeBtgl7vaYfnVVDmmtJoYdQdwlkjSfWM1cglAPLhOLdJd81EoQ4cH4hTca-71TNVszpnjc-mw7LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه سپاه: ساعتی پیش آمریکا به دکل مخابراتی سیریک حمله کرده بود پاسخ دادیم
من اون موقع فقط از یک نفر دو پیام داشتم:
ساعت 4:00 چهار انفجار در شهرستان سیریک
پایگاه سپاه سرخور زدن
ساعت 4:26 دوباره یکی زد
هرمزگان شهرستان سیریک
و الان کسی تصویر دوم بالا رو فرستاد و نوشت:
"حدود ساعت چهار صبح، آمریکا با چند موشک به اینجا حمله کرد.
پایگاه  نیروی دریایی سپاه  شهرستان سیریک ، حوالی روستای گروک"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/75834" target="_blank">📅 07:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75833">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=ZnLv1zrScNfV8FXEtsy1UzYg4xwiBEB-FxbPXh-cOYB1vZJoT8_7mwwFamFXHdMZFDZQkOKtQ_ngVKHkPJvjSX8xvKaRHcEJ9OjmP7C0HIR6dPT7B5bxD8VhSHHXuVS86rcHYB1I2XM83BZk8P5wzbYak0oIufRQJmjR5oTHLVQo3C0SaLu228_CMcD7qEz53yJjbbDmktkoOJhnjieQKWTG53DU3Uo5R5WtCqOru0uiw9tVyjMbRKp1rPZYzHq-FvmvXPIUWV6iznoPJbPeS6jn_OLoPpGuofWFVuSY_Z_iPMiMixxulo42QD4TGYgEPWn09W-lH9fAFWhUJgsDWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=ZnLv1zrScNfV8FXEtsy1UzYg4xwiBEB-FxbPXh-cOYB1vZJoT8_7mwwFamFXHdMZFDZQkOKtQ_ngVKHkPJvjSX8xvKaRHcEJ9OjmP7C0HIR6dPT7B5bxD8VhSHHXuVS86rcHYB1I2XM83BZk8P5wzbYak0oIufRQJmjR5oTHLVQo3C0SaLu228_CMcD7qEz53yJjbbDmktkoOJhnjieQKWTG53DU3Uo5R5WtCqOru0uiw9tVyjMbRKp1rPZYzHq-FvmvXPIUWV6iznoPJbPeS6jn_OLoPpGuofWFVuSY_Z_iPMiMixxulo42QD4TGYgEPWn09W-lH9fAFWhUJgsDWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
ویدیوی دریافتی دیگر از همان موشک،
دوشنبه ۱۱ خرداد ساعت ۶:۳۰
Vahid
ستاد کل
ارتش کویت
دقایقی پیش اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
به گزارش خبرگزاری رویترز، جزییات بیشتری درباره این حمله پهپادی منتشر نشده است.
ارتش کویت در بیانیه خود تاکید کرد که صداهای احتمالی انفجار ناشی از رهگیری اهداف مهاجم از سوی سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/75833" target="_blank">📅 07:01 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
