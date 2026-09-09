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
<img src="https://cdn4.telesco.pe/file/gXWM3fLObt5ePspFHClWkm199pIFyqwpoEsKqzrwaFXf3MUYw296b5NzIWAMwn9J4jNfFMy1INi3BR6eoi1eIRH3pWkUv_9-aGlO6LKEpZs3zMxOqa5XVp55DUXjcTkJA-sdqeje4ND2kisKzfC159xz8Ge0NKDEdDB-yGYWAtp8b8sRk1Dac4ffPSZGYQIj2hpfgPMeGiWUgB_5_oE922dLFhzgR5DgTtMXrMeK0OdkHg43IlWbL5jdXcs66Ml4TFEBVnOXqbKQsrbdxYswoqwKHBaLG7yFRr1NuztLyoUt-edrBXatV_yqNliiVcslkJZa4n_5ZQLtuyRU9EPcyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 450K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">۱۰ دقیقه پیش چندین گزارش داشتم از‌صدای انفجار‌ از تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/withyashar/22670" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/22669" target="_blank">📅 14:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHBjBAwDx8boJPhFMl7LUhURzKFWJCVOlEGGHuzcEy69RGTgIVPYyDQT0HVT_0mVjy5xXracOTkDpy6YC2F5Hvzko2WcoyvlcDFI1tUoSXDxwC7T9lg_sz9PayLlJQju1UmtH15KsKysSX7X8IOFGwX-fMqyP53kNmLuQdAx8VCVRtSUEM3AZOBvh18b7hB_HCvO_nRvljmdy4YizINu0i9QzsJpHQJfHDTo_6d1xf070s0BcU38qHVIprk2I7iBXOoxhSyP26YNQLrXjcrtO2_9q1nd0aFMWwbHr1963InfivklDaEraNGMHx5ofTVVf0Kx8PPZ1Yl4NnyyT4RPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریای بریتانیا UKMTO: گزارشی از وقوع یک حادثه در ۲۸ مایلی دریایی جنوب‌شرقی الفاو عراق در فاصله‌ای نزدیک از آب‌های کویت دریافت کرده است. ناخدای یک نفتکش اعلام کرده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته است. خدمه در سلامت هستند
@WarRoom</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/22668" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kib2VnWMlEemvm3xhBfTqjs2W9eMavS5k2qjhps7hfsMYN_kaASdumsJgM2Hp6etaRFCPL8BEYGrwKArbtiaV6YvOhNJBmSH5gTBAU-d4oFsft_XcVeGBxyanp1h_OxCQN6WxfVl_0RQlgv11qiKSZNfhXtIx8q5-wlueWzIr-OPhrXvcRWFa7UiE7xZVIKLGFbPPz9ku1oJzCm53qt3TWLnPrG4l9A1jtFSug8xCdn3AdHp7MA0bS02myHBAKt8dZ0rDcleJtPenwuouxf45alS-EpMGoLCw_ynAWM-ghUt-FLfOB00dWDU9PjatoTzCN57rwUyPWXmbB3KLgALHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: تصاویر ماهواره‌ای از افزایش چشمگیر ساخت‌وساز در سایت به‌شدت مخفی «کوه کلنگ گزلا» در نزدیکی نطنز خبر می‌دهد؛ محلی که ممکن است به تأسیسات غنی‌سازی اورانیوم یا یک مرکز امن هسته‌ای تبدیل شده باشد
@WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/22667" target="_blank">📅 14:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">العربیه : نیروهای مسلح یمن رسماً اعلام کردند که طی عملیات اخیر خود، تعدادی از سرکردگان شبه‌نظامیان حوثی، از جمله طراحان اصلی حمله به تنگه استراتژیک «باب‌المندب» را کشته و شماری دیگر را به اسارت درآورده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/22666" target="_blank">📅 14:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۴ اسرائیل در یک افشاگری ، مدعی شده قالیباف در یک جلسه غیرعلنی گفته تحریم‌های آمریکا اثرگذار بوده و خسارات ناشی از جنگ تقریباً جبران‌ناپذیر است و گفته «جمهوری اسلامی در آستانه فروپاشی است». بر اساس این ادعا، قالیباف همچمین اضافه کرده: «همه ما میلیاردها دلار دزدیده‌ایم، اما دیگر نمی‌توانیم مردم را برای مدت زیادی کنترل کنیم.» او همچنین از رویکرد تندروانه احمد وحیدی، فرمانده سپاه، انتقاد کرده و گفته «پافشاری و رویکرد او، ایران را به خطر انداخته».
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/22665" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حقیقت یاب سنتکام : هیچ ناو جنگی نیروی دریایی آمریکا مورد اصابت قرار نگرفته است؛ تمام حملات تلاش‌شده از سوی سپاه شکست خورده‌اند. در همین حال، نیروهای آمریکایی تنها در هفته گذشته با موفقیت
۱۰ نفتکش ایرانی
را منهدم کرده‌اند. این شناورها بخشی از یک شبکه چندمیلیارددلاری موسوم به «ناوگان سایه» بودند که برای تأمین مالی سپاه پاسداران فعالیت می‌کرد و ایران قادر به دفاع از آنها نیست
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/22663" target="_blank">📅 13:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره:
پاسخ ایران در برابر پدافند هوایی و موشکی یکپارچه ناکارآمد بود.
موشک‌های شلیک شده توسط ایران به سمت اردن منجر به تلفات جانی در میان نیروهای آمریکایی نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/22662" target="_blank">📅 13:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دلار ۲۳۲،۱۰۰ تومان (سقف تاریخی)
بازار آزاد ۲۳۶-۲۳۸ هزار تومان
تتر ۲۳۱،۰۰۰ تومان(سقف تاریخی)
نفت برنت ۱۰۰.۴۰$
انس جهانی طلا ۴،۳۹۸$
۱ ظهر تهران
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/22661" target="_blank">📅 13:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رویترز گزارش داده بنیامین نتانیاهو در آستانه مهلت ثبت فهرست‌های انتخاباتی، برای متحدکردن احزاب راست‌گرا تلاش می‌کند. انتخابات پارلمانی اسرائیل قرار است ۲۷ اکتبر (۵آبان)برگزار شود @WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/22660" target="_blank">📅 12:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رویترز گزارش داده بنیامین نتانیاهو در آستانه مهلت ثبت فهرست‌های انتخاباتی، برای متحدکردن احزاب راست‌گرا تلاش می‌کند. انتخابات پارلمانی اسرائیل قرار است ۲۷ اکتبر (۵آبان)برگزار شود
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/22659" target="_blank">📅 12:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcnXAHRayAHAn8vMg-2RXyPYpSx9LR6WTuivnJAPIeBkseJKoWAl_O2VSyKDiUeafrUs3Eoe3kC9vpANcD6M9tdopTY6fU1boWpcunEgmiXUVYYs957rouA0RlcoyTXm-hkdf8T6vQvCdAud-FYuf7gsjMXMUTHupu_nqt_hjRS44UYc80frFAlA-ToNkSZdpG65s3yJB3TQo3CNCG6jtkKK3gw8rZwxc09QX7eklDcCCf3wg2sI3v6MC4knMGjCIZHl_Vg4L3nXiBoi6TdaogIWRiEhXhnlqMthtQnrzthsoxQXyIjC3cV7kU6JgK1Z8uZHqYGVxc2wGqasM3hCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا (UKMTO) با تاخیر گزارشهایی از چندین مورد کشتی تجاری در شمال خلیج فارس و خلیج عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها به عنوان بخشی از فعالیت‌های نظامی دیشب در منطقه، هدف آتش‌سوزی قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/22658" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رویترز گزارش داده هزینه بیمه و ریسک جنگ برای نفتکش‌هایی که از هرمز عبور می‌کنند به‌شدت افزایش یافته و هزینه بیمه جنگی در برخی موارد به حدود ۶ درصد ارزش محموله رسیده است؛ موضوعی که باعث شده برخی شرکت‌ها از عبور از این مسیر صرف‌نظر کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/22657" target="_blank">📅 12:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آسوشیتدپرس گزارش داده ایران در حال شکل‌دهی به شبکه‌ای تازه از گروه‌های نیابتی، به‌ویژه حوثی‌های یمن و گروه‌های مسلح عراقی، برای افزایش فشار بر متحدان آمریکا در خلیج فارس است. بر اساس این گزارش، نشانه‌هایی از هماهنگی میان حوثی‌ها و گروه‌های عراقی دیده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/22656" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دلار ۲۳۰،۱۰۰ تومان (نرخ تاریخی)
بازار آزاد ۲۳۵-۲۳۷ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/22655" target="_blank">📅 11:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22654">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe589f1aee.mp4?token=jBTci9U3CKMuJMaOCXT24M4Ue3bhQwFrAnMuDsNHpjUV5SMno4QCVNXFDJdPIzQwsTGLkbrRubvSN6ZXOowA2LXypaxXg7tlTS-i4TCeu8XNYhSpyQGfmUcbypVNp5O6RXJOiNxKorqS3HRyCzuKkSoiIfqE6QAzSxWyLCuJ3TSJ1dwkUqsWwxe6nsgaSF_-Q3YNsKb8XCfpYkfYpc1J7oT7fH-voCZOmVekubZyC8irgtSw-tY_L8rJAy43KLRZlOqrPr6FSuuVyUNhN8jbQbqrKRSfcYZ19WHyvlr19JPfuac1966yVRnGEfjJZC7CBn9_St1Vx6vQ0KyGyPSAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe589f1aee.mp4?token=jBTci9U3CKMuJMaOCXT24M4Ue3bhQwFrAnMuDsNHpjUV5SMno4QCVNXFDJdPIzQwsTGLkbrRubvSN6ZXOowA2LXypaxXg7tlTS-i4TCeu8XNYhSpyQGfmUcbypVNp5O6RXJOiNxKorqS3HRyCzuKkSoiIfqE6QAzSxWyLCuJ3TSJ1dwkUqsWwxe6nsgaSF_-Q3YNsKb8XCfpYkfYpc1J7oT7fH-voCZOmVekubZyC8irgtSw-tY_L8rJAy43KLRZlOqrPr6FSuuVyUNhN8jbQbqrKRSfcYZ19WHyvlr19JPfuac1966yVRnGEfjJZC7CBn9_St1Vx6vQ0KyGyPSAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال تانک از نجف آباد اصفهان به جنوب
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22654" target="_blank">📅 11:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قیمت نفت با رسیدن به ۱۰۰ دلار در بالاترین سطح از اردیبهشت امسال قرار گرفت
وقایع شب گذشته در تنگه هرمز کافی بود تا سقف هفته‌های اخیر نفت شکسته شود.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/22653" target="_blank">📅 11:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847f998c3f.mp4?token=Mjti-r586keYWRn75cPGfNhfx9LrvUE11ExCM7p-A-uJNDaEPYNmerfdffkU3enBcd65RR2mhZAiSoA-B5G1zIUgRlO42gvCbfDiQ9w_xwX-AMPnw_spRMxfqt4m84eNTXqzw7b-o4bJZZCtVNTMm3udydCCr0aMpMqhDmDjPQxP1zjel4PkPQnsjz9h6w6HId-DRznd5SO7XQoZTdaz22qPDy9sz0LnAosoLOzzIXJK9RJHfC_shBXOKbu0Fym92k53UGx4x-nOQWs5cvlQZFUR6BsZF_vgosJCMm22JTVOocD8fTxZcFrzvOGFwQFhogYUCvaUKRvvC_sO1E-13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847f998c3f.mp4?token=Mjti-r586keYWRn75cPGfNhfx9LrvUE11ExCM7p-A-uJNDaEPYNmerfdffkU3enBcd65RR2mhZAiSoA-B5G1zIUgRlO42gvCbfDiQ9w_xwX-AMPnw_spRMxfqt4m84eNTXqzw7b-o4bJZZCtVNTMm3udydCCr0aMpMqhDmDjPQxP1zjel4PkPQnsjz9h6w6HId-DRznd5SO7XQoZTdaz22qPDy9sz0LnAosoLOzzIXJK9RJHfC_shBXOKbu0Fym92k53UGx4x-nOQWs5cvlQZFUR6BsZF_vgosJCMm22JTVOocD8fTxZcFrzvOGFwQFhogYUCvaUKRvvC_sO1E-13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نفتکش «M/T Riesco» پنجمین نفتکش ایرانی که امروز هدف حمله آمریکا قرار گرفت پس از حمله در دریای مکران (عمان) غرق شد.چهار نفتکش دیگر بر اثر اصابت موشک به موتورخانه‌هایشان از کار افتادند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22652" target="_blank">📅 05:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مقام آمریکایی ‌به رویترز گفت: «وضعیت تمامی نیروهای آمریکایی مستقر در اردن مشخص است و آنها سالم هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22651" target="_blank">📅 04:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارشهای بسیار از صدای انفجار در کنگان ، انگار از طرف بندر دیر بوده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22650" target="_blank">📅 04:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MDk0NzgyMzU1OTg1NTY1?story_media_id=3824690341744932317&stkn=MWF3bWE3bnlhMWkwcw==</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22647" target="_blank">📅 03:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22646" target="_blank">📅 03:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22645" target="_blank">📅 03:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22639">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ارتش اردن : ایران در جریان حمله به پایگاه هوایی موفق السلطی، ۲۰ موشک شلیک کرده و پدافند هوایی این کشور ۱۸ موشک را رهگیری و منهدم کرده است، در حالی که دو موشک باقی‌مانده از «مراکز جمعیتی» دور افتاده‌اند.
هیچ تلفاتی در نتیجه این حمله گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22639" target="_blank">📅 03:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22638">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpzKpZuY9w8h2tJoFLFVUbzxInL3fA2loj_HkU7Lyy005Y4UemhGgT3YG7wkccRSzMIu7QHJZnujHmWhtPk6nrRyEXeduLOZ0bURapKaE2I8UcY3R_2oYmDdhVhqrxuX-VlyUhaSpbPZryYQCre-Gax938z0-CmH6SCiESp2mz12e9GUk8Agpc3exII08CgSRF-v9S4Cz_dfy1mMUlM6D_6QFqEdd9hARKlIlvOWH9_qPqbuVbKnNkxaaT5saEi-R7iNWErczCRDFRwFneMM0_vNaHIbpbwU6nalBT7T6vPsH5E9fDV1SI1dEXBuiFhF6r4lJTLNLUXI97g_3T1o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران اعلام کرد در واکنش به اقدامات آمریکا علیه نفتکش‌ها و شناورهای ایرانی، نیروی هوافضای سپاه با موشک‌های بالستیک به دو ناوشکن آمریکایی
DDG119 - USS Delbert D. Black و
DDG53 - USS John Paul Jones
حمله کرده است. سپاه مدعی شده این دو ناوشکن که به موشک‌های کروز و سامانه پدافندی Aegis مجهز هستند، در این حمله آسیب قابل‌توجهی دیده‌اند. همچنین تأکید کرده به اقدامات آمریکا پاسخ خواهد داد و نسبت به «خطای محاسباتی» هشدار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22638" target="_blank">📅 02:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22637" target="_blank">📅 02:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22636" target="_blank">📅 02:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویدیو حملات به اردن توسط سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22635" target="_blank">📅 02:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22634" target="_blank">📅 02:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پرتاب موشک جدید از‌ تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22632" target="_blank">📅 02:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بیانیه شماره ۱۳ سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22631" target="_blank">📅 02:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541f997a69.mp4?token=Tx6THX9xBkCC9N7Ehk091XApc6gt6x6Xffne1J1eNNKS7ggqQt7TXogpbhwPZGSdixdrhuQy57gwY_QzNOrKHkYs-Y-LX-t-4ddT_bMUKT8NssyjK0K3hB46-KPREjOyIFm1A61ZM4KW33iwljb7bxCdchlMDARD7qDLGdkjRoEELiLayFclhUbANzj1c-XQO7CtJ4c0qWXfKCMC-nqEhSHeIYFwp0j6s5cRxaYoOsCXW1-57UuuODCKAeQ-UPDEvWkjKdcI35HGPgPaybBdM_0JOVEyW9oI-16nRUFyCe0e8Bi89diCRIEL3ZYvrc_vvTkTCkI9wLQ2AMUVZ-pnKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541f997a69.mp4?token=Tx6THX9xBkCC9N7Ehk091XApc6gt6x6Xffne1J1eNNKS7ggqQt7TXogpbhwPZGSdixdrhuQy57gwY_QzNOrKHkYs-Y-LX-t-4ddT_bMUKT8NssyjK0K3hB46-KPREjOyIFm1A61ZM4KW33iwljb7bxCdchlMDARD7qDLGdkjRoEELiLayFclhUbANzj1c-XQO7CtJ4c0qWXfKCMC-nqEhSHeIYFwp0j6s5cRxaYoOsCXW1-57UuuODCKAeQ-UPDEvWkjKdcI35HGPgPaybBdM_0JOVEyW9oI-16nRUFyCe0e8Bi89diCRIEL3ZYvrc_vvTkTCkI9wLQ2AMUVZ-pnKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره ایران:
ایران همچنان به تلاش برای حمله به کشتی‌های نیروی دریایی ایالات متحده ادامه می‌دهد و هر بار که این کار را انجام می‌دهند یا سعی در انجام آن دارند، نفتکش‌ها را از دست می‌دهند.
امروز دوباره شاهد این موضوع خواهید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22630" target="_blank">📅 02:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شبی پر خرج برای رژیم جمهوری اسلامی
سنتکام : ایران از این نفتکش ها به عنوان بخشی از یک شبکه مخفی چند میلیارد دلاری برای تامین مالی سپاه پاسداران و عوامل ایرانی در منطقه استفاده می کند.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22629" target="_blank">📅 02:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم  نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22628" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22627">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22627" target="_blank">📅 01:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22626">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم  نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22626" target="_blank">📅 01:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار : تمام اطلاعات و تحلیل ها و نام کشتی ها درست خبر رسانی ، پیشبینی و تحلیل شد و با اختلاف چندین ساعته امشب به اطلاع شما رسید !
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22625" target="_blank">📅 01:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم
نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت از حملات ایران جان سالم به در برد و به گشت‌زنی در آب‌های منطقه‌ای ادامه داد. هیچ پرسنل آمریکایی آسیبی ندید.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22624" target="_blank">📅 01:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/withyashar/22623" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخطار خلبان جنگنده آمریکای به کشتی HORIZON برای تخلیه موتور خانه در ۱ دقیقه
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22623" target="_blank">📅 01:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0NvqLkWbRUo8s6vC0RiIB-5B2UubPOXvcGJCUt-btKY6LDQzC8Hj2Ib9XmvbQF7rtpPXKwnMsJZR5mBzBUJVVhg6BUAzsUNXzI0I7Dgjp11P1NJazFxRYWz_EVP5O8OvLTLA6gZ1NlSnf8ohpLgQLLsYgQNtMG9l8cXdnma9WcJpt7_YcMQoMRdfKyDp-dRmYbwSukFXzHYhvCh74-hEhbfYeWQZ9725SgyndgsWQFmwS2Jf0kZZCeDCcFa9JSaAT4XIRR29Py1vDmyfKIWFKx7H3RB08ulABZkisrrKUunxs6QaC_bm7qA3tpQkpT_h_3ScSCD1yYtCCNF083q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی دیگری‌که امشب هدف قرار‌گرفته احتمالا
HORIZON
است که با نام هرمز هم شناخته میشود با کال ساین 9hek9 که به نظر میرسد مربوت به امپراتوری Hektor  همان حسین پسر شمخانی باشد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22622" target="_blank">📅 01:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تنها خدای واقعی زمان است</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22619" target="_blank">📅 01:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixFTak6PEVWeitsIDaJJFDrDpuI-gZ4SyXcJwgYFLHtTBLF5WXCes1w9eMhbvxDDRJ_DHFCyrOBOd1GjZ0S0UFMm3UTnal4c-qQ-xbO_4sB4SdN277b81z4_NwCTi6CUrrS__ZFnUzB4N1N4VDu2g4K1p0Zb2-qOXWYUXxCN1rLbPoVdiXpI4UagrLqMODOdaP34PijpCI4NvlCZewevSXpyYSN8baevm4qin4MWWKLfsRtzSyWLr5dBuJcACH5UpAdEQoptIIuQvMURHp_U_9f5LbbKgTkBz-fOZuXP3AhwVo9LDuknEJvezN2zcHmpoOEKQjFBGrMK2qZFfEfMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بروجرد پرتاب موشک ناموفق بود و ترکید !!!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22618" target="_blank">📅 01:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff90ac3f79.mp4?token=Xp5U3J9b64q6OK12sKC_m14PCMn5K_0qaiytiTugxzb2WKzWwbn1erOLKlV2pGTpxleamKiHP0Nv-3EoVpqkMeDn7B9mvgBnOMew2ONjJOl_YPKHbp68mxql0-i0LUxZXp2bgtLEXfLKARX6jEuyOKVrjdF6Ytk4RvErjTV8zqflSV0fa0FuO7cSIZEb1Lo2J22yQcbpxfmqVxJdExbTuyIGIkDdwbcvb77hnbknk6zrs1OxUE9EooGkE1t5rTxB8E90_Jrcm91NZK5hNE9QvnzOm_6GB7jhuBy4Zx_dIQivWkvBixVyhaj8yf7rviJ9YQtMtFi6CKlXx7qemfPgAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff90ac3f79.mp4?token=Xp5U3J9b64q6OK12sKC_m14PCMn5K_0qaiytiTugxzb2WKzWwbn1erOLKlV2pGTpxleamKiHP0Nv-3EoVpqkMeDn7B9mvgBnOMew2ONjJOl_YPKHbp68mxql0-i0LUxZXp2bgtLEXfLKARX6jEuyOKVrjdF6Ytk4RvErjTV8zqflSV0fa0FuO7cSIZEb1Lo2J22yQcbpxfmqVxJdExbTuyIGIkDdwbcvb77hnbknk6zrs1OxUE9EooGkE1t5rTxB8E90_Jrcm91NZK5hNE9QvnzOm_6GB7jhuBy4Zx_dIQivWkvBixVyhaj8yf7rviJ9YQtMtFi6CKlXx7qemfPgAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرجه موشکهای خوشه ای بر روی اردن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22617" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سپاه به اردن موشک خوشه ای زد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22616" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7a6210ca1.mp4?token=nnLIpJvFiyCVGRCZ6-XzO0J8F5A3X-5Zj6uaVRn90vrhyzXV3xCvA6jhhYxnK1JfCblFrE9lg-_jd-XN6wzvOFXTsSvt3d3_3IIuBKI-z9I-SvPM7WK0MoG3irebChvbLPmqn3ln7wgPAvf34HzgrkHzINDLKUTSve1mg-MnG1cCWe7ddwrddlgHsfl8VDfhXV9sjreVgorlc9ZPwmXhkGbPT9N-KaNGePHNU21QkBcVBJo_vSFK4-1Q5BxkWaf4auXMUofRWh-Sh4ekgYGvaiY5wo1hrfvpgrgJEOn4CTwev2jEbnjywszPnI0au-Q5uwY8YkhzDhP8eU7SRRx7yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7a6210ca1.mp4?token=nnLIpJvFiyCVGRCZ6-XzO0J8F5A3X-5Zj6uaVRn90vrhyzXV3xCvA6jhhYxnK1JfCblFrE9lg-_jd-XN6wzvOFXTsSvt3d3_3IIuBKI-z9I-SvPM7WK0MoG3irebChvbLPmqn3ln7wgPAvf34HzgrkHzINDLKUTSve1mg-MnG1cCWe7ddwrddlgHsfl8VDfhXV9sjreVgorlc9ZPwmXhkGbPT9N-KaNGePHNU21QkBcVBJo_vSFK4-1Q5BxkWaf4auXMUofRWh-Sh4ekgYGvaiY5wo1hrfvpgrgJEOn4CTwev2jEbnjywszPnI0au-Q5uwY8YkhzDhP8eU7SRRx7yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحدید سپاه : مرتبط با آمریکا، در منطقه تنگه هرمز و خلیج فارس شما در معرض هدف قرار دارید دستور میدهیم که خدمه و مهمانان خود را تخلیه کنند اگر تمایل دارید [در اینجا بمانید]، مسئولیت حفظ امنیت خود و خدمه‌تان بر عهده خود شماست.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22615" target="_blank">📅 01:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d364bd4e.mp4?token=Zuc3bMYHuk8g-zA3WG_09Umx8MTwHyFRFLsUAOhdSlDsApCyu8xNn656TqOwQ610YICbGkrLt7aXOIOGUX3mhnVGaoz8K23Ml6rjJoziW2qfjFn8fxBE5cNiH0tYYGb23aviAg9iN1xO1vhT22kMn2Mp85KFKjcyloLFgRImUQUAyeoEkkg7y3w_nF1xnjZDM0NLPdLNjgLCjKhtlpcrSqp2Lb9zc2dQPUH184RuwxJKMqeY-Gb3uWhHdE3TTfsoq7NUrd0wHOBtWbaksHiDOQzUzkmgzA7mPL2A_AWYVEmv9aWvxhU1JfHeEoGKN55fdyj-LFgKcz8CgEtWzeeYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d364bd4e.mp4?token=Zuc3bMYHuk8g-zA3WG_09Umx8MTwHyFRFLsUAOhdSlDsApCyu8xNn656TqOwQ610YICbGkrLt7aXOIOGUX3mhnVGaoz8K23Ml6rjJoziW2qfjFn8fxBE5cNiH0tYYGb23aviAg9iN1xO1vhT22kMn2Mp85KFKjcyloLFgRImUQUAyeoEkkg7y3w_nF1xnjZDM0NLPdLNjgLCjKhtlpcrSqp2Lb9zc2dQPUH184RuwxJKMqeY-Gb3uWhHdE3TTfsoq7NUrd0wHOBtWbaksHiDOQzUzkmgzA7mPL2A_AWYVEmv9aWvxhU1JfHeEoGKN55fdyj-LFgKcz8CgEtWzeeYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ قم حرم زیارت بود که موشک پرتاب شد
😂
✌🏼
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22614" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21c8f0d7d.mp4?token=ipcqjvFnTjZZDuNxfJ4dhfWf5YAXBusN-P70BRGf0Re4VaUSHy8ZWaOKCh-W3pOGkdz3XgfNgYxV3ZFBH9gjl-I63Huu1JQb5dAfGjoS1Yx8RPBlJdKsSU94QvYt5V5j7SqtcT6HGwFKQGS2eXlr2bwQAXJ0AHxHcxCccPRIQQEUYudzTr4AK1iuS_sgBW4FrvHFS4gYZOY_P8EdEsQ6vqX_lBDS119iKoB6wbG7U-J2UnVlh1cfYtzltJr2XEFebN-ruEtx3yUdyaNlV0WDARQVm2yDF_fPsZaelkeMY3hmMPNl_expBTFwn8gSxy8fkt6sy-ANJE89ulMZUChXhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21c8f0d7d.mp4?token=ipcqjvFnTjZZDuNxfJ4dhfWf5YAXBusN-P70BRGf0Re4VaUSHy8ZWaOKCh-W3pOGkdz3XgfNgYxV3ZFBH9gjl-I63Huu1JQb5dAfGjoS1Yx8RPBlJdKsSU94QvYt5V5j7SqtcT6HGwFKQGS2eXlr2bwQAXJ0AHxHcxCccPRIQQEUYudzTr4AK1iuS_sgBW4FrvHFS4gYZOY_P8EdEsQ6vqX_lBDS119iKoB6wbG7U-J2UnVlh1cfYtzltJr2XEFebN-ruEtx3yUdyaNlV0WDARQVm2yDF_fPsZaelkeMY3hmMPNl_expBTFwn8gSxy8fkt6sy-ANJE89ulMZUChXhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب یک دسته موشک از‌خمین
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22613" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a496403d.mp4?token=Zk6K3hdO7BWfWe59t1BRd8AN5giUJ9i1wJySBzU7Zlnj61dUhBmlRpqz4ZehCQM_sr-5OaHZ2G3MiFUWtI16I-6cVDdlCrvLOnQAysk6dirnDFiWAkQJQIBy5pSEG8i5grSBnGHqydpGCegT0cUVnZfHsM3t1doRgT4BPVWijyBRMTeAxa11YegS2js6ZyWIjUQKTkVdaRHNjfW7iJU1g1e5OeZbbFFXBgsMJegZpat8uyed3FZNVhVFbb3AyuRHWGv1mcp9S3afpMgX9srKMDI828Ly5rwjYTCMJYLmfP7Yg4l8WPun_0LomR4HqikDGEZYezlyLP6UYH7Z5BF9Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a496403d.mp4?token=Zk6K3hdO7BWfWe59t1BRd8AN5giUJ9i1wJySBzU7Zlnj61dUhBmlRpqz4ZehCQM_sr-5OaHZ2G3MiFUWtI16I-6cVDdlCrvLOnQAysk6dirnDFiWAkQJQIBy5pSEG8i5grSBnGHqydpGCegT0cUVnZfHsM3t1doRgT4BPVWijyBRMTeAxa11YegS2js6ZyWIjUQKTkVdaRHNjfW7iJU1g1e5OeZbbFFXBgsMJegZpat8uyed3FZNVhVFbb3AyuRHWGv1mcp9S3afpMgX9srKMDI828Ly5rwjYTCMJYLmfP7Yg4l8WPun_0LomR4HqikDGEZYezlyLP6UYH7Z5BF9Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22612" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bbb709c43.mp4?token=jZQq0-Q98EJxwDyK8Al0YhWvujuFMG2RWeCF4D-Hus3mbR3llhCA7SpF8xTGVp-_Ty3HfEAXeZWbOPd1gMLh_1ekfnQwYxpa2UAfT2OwsveHmsZbbQ4uuZnUcUHMTFyXuIOuIEk3CBHkAHd9r9GrZ_FlNAnvxJLbp-sEFk-Uox7a6TofkNNL3i000Gi7VJwGEKKOTlRYLxBjxD7r94Pja9zf9SQA03y3RRjnhpMfW12vqvaTTqYj1ys9DrAU73cAOaAC5Kg1NQJrmFoz3xAUyGrcmCpEftj06_VM02ox1Aitin2Zk5JYFO0umlhaOikBumKeOT8xoeQidrpLn15c-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bbb709c43.mp4?token=jZQq0-Q98EJxwDyK8Al0YhWvujuFMG2RWeCF4D-Hus3mbR3llhCA7SpF8xTGVp-_Ty3HfEAXeZWbOPd1gMLh_1ekfnQwYxpa2UAfT2OwsveHmsZbbQ4uuZnUcUHMTFyXuIOuIEk3CBHkAHd9r9GrZ_FlNAnvxJLbp-sEFk-Uox7a6TofkNNL3i000Gi7VJwGEKKOTlRYLxBjxD7r94Pja9zf9SQA03y3RRjnhpMfW12vqvaTTqYj1ys9DrAU73cAOaAC5Kg1NQJrmFoz3xAUyGrcmCpEftj06_VM02ox1Aitin2Zk5JYFO0umlhaOikBumKeOT8xoeQidrpLn15c-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پرتاب دو موشک از اصفهان
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22611" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش پرتاب موشک از کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22610" target="_blank">📅 00:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارشها حاکی‌است چهار نفتکش ایران توسط جنگنده های F18 هدف گرفته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22609" target="_blank">📅 00:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مقام آمریکایی به وال استریت ژورنال: ایران دوشنبه، برای دومین بار، حمله‌ای را علیه کشتی‌های متعلق به نیروی دریایی آمریکا انجام داد @WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22608" target="_blank">📅 00:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22607" target="_blank">📅 00:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/withyashar/22606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخطار اولیه  نیروی هوایی آمریکا و تاکیید به هدف قرار دادن موتور خانه و و دادن ۱۰ دقیقه زمان به خدمه برای ترک  محدوده موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22606" target="_blank">📅 00:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش حمله موشکی آمریکا به سومین نفتکش ایران در سواحل شهرستان جاسک
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22605" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تحلیل ساده
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22604" target="_blank">📅 00:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار ۲۲۹،۲۰۰ تومان (سقف تاریخی)
تتر ۲۲۹،۲۰۰ تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22603" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش پرتاب موشک از کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22602" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و…. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22601" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرنگار صداوسیما:
ارتش آمریکا به نفتکش دوم در نزدیکی آب‌های جاسک حمله کرد.خدمه هر دو نفتکش با قایق نجات در حال انتقال به سمت ساحل جاسک هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22600" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پس برم زیر سماور رو روشن کنم
🤣</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22599" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رویترز: امشب در سراسر خاورمیانه آماده باش جنگی است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22598" target="_blank">📅 23:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مقام آمریکایی به وال استریت ژورنال: ایران دوشنبه، برای دومین بار، حمله‌ای را علیه کشتی‌های متعلق به نیروی دریایی آمریکا انجام داد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22597" target="_blank">📅 23:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سپاه : به تمامی خدمه نفتکش ها در محدود اسکله های کویت و بحرین که میزبان آمریکایی ها و شریکشان هستند اخطار می دهیم شناور خود را چه در لنگر گاه و چه در اسکله ها سریعا ترک نمایند چرا که مورد هدف  قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22596" target="_blank">📅 23:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کامنت برای ترامپ
https://www.instagram.com/reel/DdCe4x2B6Qc/?comment_id=18626069959030735</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22595" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سپاه پاسداران اعلام کرد حملات موشکی جمهوری اسلامی علیه پایگاه‌های آمریکا در خاورمیانه به‌زودی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22594" target="_blank">📅 23:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مقام آمریکایی به فاکس‌نیوز : نفت‌کش‌های ایرانی را در نزدیکی خارک و جاسک هدف قرار دادیم.
این بخشی از تلاش گسترده‌تر برای اعمال فشار اقتصادی بر ایران است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22593" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رسانه های رژیم : دو تانکر نفتکش در خارگ و یک نفتکش ایران در جاسک هدف حمله آمریکا قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22592" target="_blank">📅 23:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22591" target="_blank">📅 23:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22590">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش های زیاد از صدای ۲ انفجار در جاسک  @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22590" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسانه های رژیم تازه تایید کردن</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22589" target="_blank">📅 23:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">منابع محلی خارگ اعلام کردند که این حمله خوشبختانه هیچ‌گونه خسارت جانی به‌ همراه نداشته و کارکنان نفتکش در حال تخلیه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22588" target="_blank">📅 23:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏I24NEWS :  نیروهای آمریکایی در تنگه هرمز به نفتکش‌های ایرانی حمله کردند @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22587" target="_blank">📅 22:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22586">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدای انفجار جدید از جاسک (ممکنه جاسک پرتاب دفاعی رژیم باشه)
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22586" target="_blank">📅 22:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش انفجار مهیب در تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22585" target="_blank">📅 22:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏I24NEWS :  نیروهای آمریکایی در تنگه هرمز به نفتکش‌های ایرانی حمله کردند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22584" target="_blank">📅 22:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22583">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22583" target="_blank">📅 22:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/no4vVK5qEz9LPy7EGj4iPq36ZBArG-s7s_Pep8Thce_nbsuwGf6O7adBRIlBlcCzwjSCfCMvm8z4HsDE8pVjth98yCqS4CRPkevld3U2FfEl95NldAMbbVPP8i_vRwQwwvBVcPYJGmH2Pw0bmLUMi-5MNkKj6JmZ3D-zb_i3c34hrZWhOzw6XLk_GcTvs5Kq22Vz4NnJnk2tF1ufNMj1Ns6y61ngEgQOgDFaIZfOm7QSDXHEKrPkfcz043CYulehcwjGe59AXtsLFbo3DWyeuerJQoI6JFjA7vOzsQOCJ9DeGujawLJ2IORWWcdvUZO9oe5-4caMG9RDddnvpts3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22582" target="_blank">📅 22:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22581" target="_blank">📅 22:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22580">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22580" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spLjcjoDNy5aZRmpIT4-eyw7q9fRVjXj5HH0EX3IgPSln18HinrvL_IO1_VCT6s1vmeIXSEnmGz2hjuj92ggpyQv6Xql_1BA0wLmYZDrRgTRBYAOJ-c2KnCe6m25VAXkRcD3ZOnwXxHQemgq0VQQ9t_sX0WfNYN-R9sJJVXbeJV-sahoy0RQzjZUVEvkUJanrl6AHlp25eBAVJ70u2NT4Te7PWxJ8IXt_CzK4AhAGqzr3aTPtXxAK2bPvtKh3y-6jBuZiZiwIyoqwCI99Ye_7p1w21V2W7YcF_8vEAZubJpS6S8INAC8EvYwcpIbC02WCtSvxthSH5cKW9VGQSK3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22579" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22578" target="_blank">📅 22:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22577" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22576">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدای انفجار ها در محدوده لنگرگاه جزیره ( محل نفتکش ها ) بوده و خارگ در ارامش کامل است تا این  لحظه @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22576" target="_blank">📅 22:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی سنتکام :
یک فروند زیردریایی بدون سرنشین ما روز گذشته طی یک ماموریت نقشه‌برداری از آب‌های سرزمینی دچار نقص فنی شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22575" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش های زیاد تایید نشده ، خارگ آمریکا داره ۲ تا نفتکش رو میزنه  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22574" target="_blank">📅 22:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش های زیاد تایید نشده ، خارگ آمریکا داره ۲ تا نفتکش رو میزنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22573" target="_blank">📅 22:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c17de1b0c.mp4?token=uKoFzyoaf7NHnpszIvzUDYd_cfEXaj5NjhI0u0_NE4057hKYFmpV2hS7E2w1obobycGlG-QmXlQK1fFBUyAVp-VCLZkfAOapQe_fcLdm4B0JkP3LoViNcsuGB0-_ow44IXqzmrO4_uzVHuGgKM9lhrEh_6Ii47uY7eAXvPpF6F-sVCSktGeCu-SFj26e6caCYDmnld8_fK8EgIzpOnFXbJmS4Ze_Ii-jVBKlcZ8I0Gva6PT-pE_Lle0scEstZ9_daX3Oc624sPLQceCI14XrqOZ867d30W2GY5nlcg_QRWU2IhSMCUo6BxJuVwImZn54AzjHYuVj47lvP3psETBo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c17de1b0c.mp4?token=uKoFzyoaf7NHnpszIvzUDYd_cfEXaj5NjhI0u0_NE4057hKYFmpV2hS7E2w1obobycGlG-QmXlQK1fFBUyAVp-VCLZkfAOapQe_fcLdm4B0JkP3LoViNcsuGB0-_ow44IXqzmrO4_uzVHuGgKM9lhrEh_6Ii47uY7eAXvPpF6F-sVCSktGeCu-SFj26e6caCYDmnld8_fK8EgIzpOnFXbJmS4Ze_Ii-jVBKlcZ8I0Gva6PT-pE_Lle0scEstZ9_daX3Oc624sPLQceCI14XrqOZ867d30W2GY5nlcg_QRWU2IhSMCUo6BxJuVwImZn54AzjHYuVj47lvP3psETBo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: یک زیردریایی نظامی آمریکایی بیش از یک روز پیش در خاورمیانه دچار نقص فنی شده بود. بر این اساس، ادعای سپاه پاسداران مبنی بر اینکه یک زیردریایی بدون سرنشین آمریکایی را در منطقه توقیف کرده، صحت ندارد و این شناور پیش از آن دچار نقص فنی شده بود. با این حال،…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22572" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رویترز: یک زیردریایی نظامی آمریکایی بیش از یک روز پیش در خاورمیانه دچار نقص فنی شده بود.
بر این اساس، ادعای سپاه پاسداران مبنی بر اینکه یک زیردریایی بدون سرنشین آمریکایی را در منطقه توقیف کرده، صحت ندارد و این شناور پیش از آن دچار نقص فنی شده بود.
با این حال، آمریکا تاکنون به‌طور رسمی از دست دادن این سامانه را تأیید نکرده و مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22571" target="_blank">📅 21:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22570" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22569" target="_blank">📅 21:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش های زیاد از صدای ۲ انفجار در جاسک
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22568" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22567" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmoyR4FJ2uyV3vbWM0Ol4wNhSX1aualQeapM8FYawAu6r823NpLjdLBDKBnlhTlPkhPJkZukUwT8ta8ES6e4IXVSj105Vtt64MOCC3celjSujav544APV6TKIquPDwNfHSqB2_PRFxQTKJ027EXZ9eS-jPIMQMj6c0RkznfkLledhFD4XwqCr6PQ_xrZX_s8K-xdOwlmA8G1zPfAczI6DeAxauWyM3Onv8Uu9QLmzdtD3dJ0KQ8Qo3Kalphbrh8r6u3qN3nvF3x4M7OeshzkeiAM8a3P8dJL4kNAHDa9o7UzOLdkMIBdRlqhHyHFThJ1cEt1gXhVBDIFJ7D7j2XDzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل فردا، چهارشنبه ۹ سپتامبر، رویداد ویژه خود را برگزار می‌کند و انتظار می‌رود از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و آیفون اولترا؛ نخستین آیفون تاشوی اپل، رونمایی شود.این رویداد
ساعت ۲۰:۳۰ به وقت ایران
آغاز می‌شود. آیفون ۱۸ معمولی، آیفون ۱۸e و نسل جدید آیفون Air احتمالاً در مراسم فردا معرفی نمی‌شوند و عرضه آن‌ها به بهار ۲۰۲۷ موکول خواهد شد.
نام «آیفون اولترا» برای مدل تاشو هنوز به‌صورت رسمی از سوی اپل تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22566" target="_blank">📅 21:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22565">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4dcb0a04.mp4?token=Ot2Q9E4xFkv0i3WE6ogvUsWYTizI8B-NHUNkWLgIkA_TJD9GSZqBCVRoJu3KXGok8lJmVH3KaZJL45y41D1MQzQ0M4mNVv1SWlWPOw5jM8e6ZytjXgdRIukQ27quyMn008JTMmGdwg_6e1j787aj90YCLdriG_1xZieboRnPSWfZ5Pg0fE35ee9Dr7h24Vu0F_2YbthZyG941buh3fe8tnkqickhANuunBm7R6VHuOtbyPxcCez8CjCd1XAjjskCQebnC-vyiLATsSK2OiyCihFWXFrmd6tXvDPblV5lEg3bbZfuVCdMR8EkPALolDT-NRDmEicSZXerM-bmWBpmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4dcb0a04.mp4?token=Ot2Q9E4xFkv0i3WE6ogvUsWYTizI8B-NHUNkWLgIkA_TJD9GSZqBCVRoJu3KXGok8lJmVH3KaZJL45y41D1MQzQ0M4mNVv1SWlWPOw5jM8e6ZytjXgdRIukQ27quyMn008JTMmGdwg_6e1j787aj90YCLdriG_1xZieboRnPSWfZ5Pg0fE35ee9Dr7h24Vu0F_2YbthZyG941buh3fe8tnkqickhANuunBm7R6VHuOtbyPxcCez8CjCd1XAjjskCQebnC-vyiLATsSK2OiyCihFWXFrmd6tXvDPblV5lEg3bbZfuVCdMR8EkPALolDT-NRDmEicSZXerM-bmWBpmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و…. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22565" target="_blank">📅 20:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoorena</strong></div>
<div class="tg-text">سلام یاشار رفتم خونه پدربزرگ دیدم هی داره پزشکیان رو فحش میده بعد فهمیدم بخاطر پست هایی که مخصوص دارن گرونی رو میندازن گردن دولت پزشکیان به همراه همه این بدبختیا انگار این گرونی بنزین یه پروژه هست دوباره برای هدایت خشم مردم به سمت دولت و نه رژیم مردم باید خیلی هوشیار باشن</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22564" target="_blank">📅 20:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadaeb8025.mp4?token=t94oOLgDwklOPi7QtTZEoNh79BmHSuFqjjp8TOk6CFFibi1r57sB9wCsO5twVkcupfMlEL_Woc5Gn9LzhSow2glJWjbMSoVMrQPcKauZnM-LNqJemUIJuWdiElj4_A0RM-9VRn4y-Novb-kmEJzR99fnyU93s1mTlwjyIv3TB7jb2OhpSo6SjlkxpM7iZmSr4B-iS6wAJHdDweyopNJFugwBixOkuQZlmob0UOICQBiDhdQ3SnQ5qp5mT3y8AFAFaqWE1OvfpijR_VYU57u8wI7sQMwexVl9kLwJhLVVGFu1nPc8fU1sJn78EgQn4M62xDJ01SI9Xc9WypeZjBg_pGZs9BF0GGc5obRs818oYnaHzH6h7XKCXjz2OX1_T-ouozFzGc9Gf1IdImbDZ2RQBNaUR9-bezWP8xjwakLJoDyJRFPm_bxxQLeQrl0HI6t8SHWHswEKB-lDIc5YnnyrrtW9Wy__C-xwxY3DalnF7wfDz0xgaoSumJT2oDdJsZH_XLSh6wT6xm5l0sjFPHa6ItOsgIGJnY9QnfPbjR7r0gWbBXgzZGpgvI_X_RkaxIEj6pOkdDSuf_NiQ2H5kBmZNMfXeE69BmYZGkAOMJfd1sGiRtj9tApPlOSF_m_cB91B78_1JAjkGNQRvvENXpzK2iSm06v2OQtPWRlRq8VXyOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadaeb8025.mp4?token=t94oOLgDwklOPi7QtTZEoNh79BmHSuFqjjp8TOk6CFFibi1r57sB9wCsO5twVkcupfMlEL_Woc5Gn9LzhSow2glJWjbMSoVMrQPcKauZnM-LNqJemUIJuWdiElj4_A0RM-9VRn4y-Novb-kmEJzR99fnyU93s1mTlwjyIv3TB7jb2OhpSo6SjlkxpM7iZmSr4B-iS6wAJHdDweyopNJFugwBixOkuQZlmob0UOICQBiDhdQ3SnQ5qp5mT3y8AFAFaqWE1OvfpijR_VYU57u8wI7sQMwexVl9kLwJhLVVGFu1nPc8fU1sJn78EgQn4M62xDJ01SI9Xc9WypeZjBg_pGZs9BF0GGc5obRs818oYnaHzH6h7XKCXjz2OX1_T-ouozFzGc9Gf1IdImbDZ2RQBNaUR9-bezWP8xjwakLJoDyJRFPm_bxxQLeQrl0HI6t8SHWHswEKB-lDIc5YnnyrrtW9Wy__C-xwxY3DalnF7wfDz0xgaoSumJT2oDdJsZH_XLSh6wT6xm5l0sjFPHa6ItOsgIGJnY9QnfPbjR7r0gWbBXgzZGpgvI_X_RkaxIEj6pOkdDSuf_NiQ2H5kBmZNMfXeE69BmYZGkAOMJfd1sGiRtj9tApPlOSF_m_cB91B78_1JAjkGNQRvvENXpzK2iSm06v2OQtPWRlRq8VXyOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت: «وقتی بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود. در حیاط‌مان مارهای سمی زیادی داشتیم. اگر سر مار را قطع کنید، مار مرده است؛ اما خودش نمی‌داند که مرده. بنابراین باید مراقب باشید، چون سر مار هنوز می‌تواند شما را نیش بزند و دمش هم ممکن است تا غروب آفتاب تکان بخورد. اما وقتی خورشید غروب می‌کند و هوا خنک می‌شود، دم هم دیگر از تکان خوردن می‌ایستد.
مار ایرانی، یعنی رهبری ایران، هنوز نمی‌داند که مرده است؛ اما مرده است.
»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22563" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه
حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و….
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22562" target="_blank">📅 20:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22561" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دلار ۲۲۹،۰۰۰ تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22560" target="_blank">📅 19:49 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
