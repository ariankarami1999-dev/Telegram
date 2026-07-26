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
<img src="https://cdn4.telesco.pe/file/sob3OiAxUDMWZdDZx24K8lou3cpg6fCyCoRCxN3lsQCA0jC9htkMz_5uNiuM5VPLYqQ_8inGPgP0F-ZgTbF8Gevfb49FekOTInCHeqH763Z3MN4G2LbQyELYRkZFIEVRmdNl2BuOjyUgI1yR1qAujo4FB51b0_i8lzNfT-HX6CXJcaXjwa-TpZ2o-tce0uTXGgyRYkS2PpNJ-wY5TcTp0vCuNNetCG_ZKsCP5oBpclY18DhLv4DdogFGACtYZNmaFSwKcR3FT7IflWpm4aXRROtOtmZLLTqSwCoALKIRL7mbzroCdQHo1_ROHqnubJDhP-GDPehzdBHUM0zx-_29rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 21:25:13</div>
<hr>

<div class="tg-post" id="msg-19759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مجتبی خامنه ای: ایران حفظ تمامیّت ارضی لبنان و رفع کامل و بدون قید و شرط تجاوز اسرائیل را به‌عنوان شرط اوّل تفاهم‌نامه‌ی پایان جنگ تحمیلی با امریکا قرار داده
@WarRoom</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/19759" target="_blank">📅 20:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اکسیوس : ژنرال برد کوپر فرمانده سنتکام، پیشنهاد داد که عملیات بمباران در اطراف تنگه هرمز متوقف شود، با این استدلال که این عملیات به حداکثر کارایی خود رسیده و بیشتر اهداف تکراری شده است
@WarRoom</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/withyashar/19758" target="_blank">📅 20:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سی‌بی‌اس
:
بسیاری از آمریکایی ها احساس می کنند که جنگ با ایران به خوبی پیش میره
این احساسات به طول جنگ، ارتباط در مورد آن و تأثیر آن بر اقتصاد مربوط میشه
@WarRoom</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/19757" target="_blank">📅 20:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">العربیه:ایران با تمام پیشنهادات عمان برای ایجاد گذرگاه جدید در تنگه هرمز مخالفت کرده است،
هیئت دیپلماتیک عمانی پس از مخالفت های ایران، تهران را ترک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/19756" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش CNN: عمان پیشنهاد ایجاد یک ائتلاف منطقه‌ای برای ارائه خدمات در تنگه هرمز را داده است، مشابه مدلی که در تنگه مالاکا استفاده می‌شود.
پیشنهاد عمان شامل یک مکانیسم پرداخت داوطلبانه برای خدمات ارائه شده در تنگه هرمز است.
@WarRoom</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/19755" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سی‌بی‌اس:حملات آمریکا به ایران به دلیل سفر مقامات عمانی به تهران در روز جمعه برای انجام مذاکرات، متوقف شد
@WarRoom</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/19754" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">در ابتکاری خوب برای کاستن حاشیه‌ها، شاهزاده رضا پهلوی تمام فالوینگهای اینستاگرام خود را آنفالو و فقط خانواده و پیجهای رسمی را نگهداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/19753" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سفیر ایالات متحده در سازمان ملل متحد به شبکه ان‌بی‌سی گفت: مذاکرات با ایران در سطوح مختلف ادامه دارد، با وجود اختلافات موجود در داخل رژیم ایران
@WarRoom</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/19752" target="_blank">📅 19:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90613bbec.mp4?token=pyD5pMejJXYZ7TMxHS0Cr3NvshFga78vevC8o5yAihPkTYopVJk-yBnD5S7kscwriqPDJIxI5rR4ha37tqt5hkk9JBGRJNzwIDE1_RnfYHetmPPTHW-uGKk8jznhZxqgJZ-nC_mn7BxUHPV_ntGy6FcEZAlU4Hi-hnAW7Tfo20GdEPhUvhBSKhSbDyvq8TZBaMwyVF0TMOqyPclI0jN2dt3D9PlGJV8QfhdCGkhHWUFaeX2SJmzLaDoOSe2rir-aqqTolbnJnReKdZnRUrD44kkREUQl8VWFS5mGRnBMXa7R8bFfGLniLT6S9NxzxvS-R7-BvcAhSiFTrQoh4CMJZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90613bbec.mp4?token=pyD5pMejJXYZ7TMxHS0Cr3NvshFga78vevC8o5yAihPkTYopVJk-yBnD5S7kscwriqPDJIxI5rR4ha37tqt5hkk9JBGRJNzwIDE1_RnfYHetmPPTHW-uGKk8jznhZxqgJZ-nC_mn7BxUHPV_ntGy6FcEZAlU4Hi-hnAW7Tfo20GdEPhUvhBSKhSbDyvq8TZBaMwyVF0TMOqyPclI0jN2dt3D9PlGJV8QfhdCGkhHWUFaeX2SJmzLaDoOSe2rir-aqqTolbnJnReKdZnRUrD44kkREUQl8VWFS5mGRnBMXa7R8bFfGLniLT6S9NxzxvS-R7-BvcAhSiFTrQoh4CMJZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل:
اگر ایران به اسرائیل حمله کند، چه مستقیم و چه از طریق نیروهای نیابتی، چه با موشک‌های بالستیک یا پهپادها یا هواپیماهای بدون سرنشین قاتل، اشتباه وحشتناکی مرتکب خواهد شد.
زیرا پاسخ ما، پاسخ اسرائیل بسیار بسیار قاطع خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/19751" target="_blank">📅 18:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مجری فاکس: در مورد هرگونه اطلاعات جدیدی که ممکن است در مورد برنامه هسته‌ای داشته باشید و قرار است به ترامپ ارائه دهید، چه می‌توانید به ما بگویید؟
نتانیاهو: قرار نیست من اطلاعات جدیدی ارائه دهم؛ فکر می‌کنم خوب است که فرصتی برای نشستن با دوست خوبمان، رئیس جمهور ترامپ، و شنیدن آنچه در ذهن دارد، داشته باشیم، زیرا فکر می‌کنم از بسیاری جهات، این تصمیم اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/19750" target="_blank">📅 18:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بنیامین نتانیاهو در گفت‌وگو با فاکس نیوز: برنامه هسته‌ای ایران باید به هر شکل ممکن پایان یابد؛ چه از طریق توافق و چه بدون توافق.
این جنگ زمانی پایان خواهد یافت که یا نظام ایران سقوط کند، یا آن‌قدر تضعیف شود که به این نتیجه برسد که باید برنامه هسته‌ای خود را متوقف کند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/19749" target="_blank">📅 18:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مطابق گزارش رویترز، به نقل از یک مقام ارشد ایرانی، در تهران، میزان تردید و بدبینی نسبت به تصمیم ایالات متحده برای توقف عملیات نظامی، بیشتر از خوش‌بینی است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/19748" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزارت دفاع اسرائیل اعلام کرده سامانه لیزری پرتو آهنین پس از آزمایش‌های گسترده، در مرحله تحویل/ادغام عملیاتی با ارتش قرار گرفته و به‌عنوان لایه مکمل در کنار گنبد آهنین استفاده می‌شود. این سامانه توانسته در آزمایش‌ها راکت، خمپاره و پهپاد را رهگیری کند و هدفش کاهش شدید هزینه دفاع در برابر تهدیدات ارزان‌قیمت است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19747" target="_blank">📅 17:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کانال ۱۴ اسرائیل:داماد خامنه‌ای سکوت خود را در مورد انزوای مجتبی شکست
رئیس سابق مجلس ایران فاش کرد که مجتبی خامنه‌ای «به دلایل خاصی» تمام تماس‌های خود را قطع کرده و در بحبوحه سوالات مربوط به غیبت طولانی مدت رهبر جدید از انظار عمومی، تنها با احتیاط گفته است «امیدوارم سالم باشد».
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19746" target="_blank">📅 17:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">العربیه:  ایران آمادگی خود را به پاکستان برای ادامه مذاکرات در ژنو یا دوحه یا اسلام آباد اعلام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/19745" target="_blank">📅 17:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یک منبع بلندپایه به الحدث:
ایران به مسئولان پاکستانی اعلام کرده است که از مذاکرات خارج نشده، بلکه
«آن را به تعلیق درآورده است»
ایران به پاکستان تأکید کرده است که ادامهٔ مذاکرات بر اساس یادداشت تفاهم ضرورت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19744" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الکساندر دوبریندت، وزیر کشور آلمان، در بیانیه‌ای در محل حمله به رژه همجنسگرایان برلین گفت: «همه چیز نشان می‌دهد که ما با یک حمله تروریستی اسلامی روبرو هستیم.» این وزیر افزود که مهاجم مظنون به استفاده از قمه است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19743" target="_blank">📅 16:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شبکه سی‌بی‌اس نیوز به نقل از منابع: مذاکرات بین سلطنت عمان و ایران درباره بازگشایی تنگه هرمز، پیشرفت‌هایی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19742" target="_blank">📅 16:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرگزاری الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19741" target="_blank">📅 16:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدا و سیما
:
جمهوری اسلامی بارها هشدار داده است که هرگونه عواقبی که ناشی از انحراف کشتی‌ها از مسیر اعلام‌شده توسط ایران باشد، مسئولیت آن بر عهده‌ی آن کشتی‌ها خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19740" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرگزاری وابسته به رژیم :
سخن از هدف قرار گرفتن سه فروند کشتی تجاری و نفت‌کش در میان است؛ دو فروند در باب‌المندب و یک فروند در تنگه هرمز. ایران در حال بازی با اعصاب ترامپ است و احتمال دارد قیمت نفت در زمان بازگشایی بازار به ۱۱۰ دلار برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19739" target="_blank">📅 15:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک منبع آگاه وابسته به رژیم : کمی پیش یک نفتکش متخلف در تنگه هرمز که از مسیر مشخص شده توسط جمهوری اسلامی خارج شده بود، بعد از برخورد با مین دریایی منفجر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19738" target="_blank">📅 15:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19737" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ادعای منبعی عربی به نقل از مقامات آمریکایی و اسرائیلی: نشست ترامپ و نتانیاهو، زمان عملیات مشترک علیه ایران را تعیین خواهد کرد.
مرحله اول این عملیات، بر تاسیسات هسته‌ای متمرکز نخواهد بود و تا 10 روز ادامه خواهد داشت.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19736" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19735">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کریم خان دادستان کل دیوان کیفری بین‌المللی ، که حکم بازداشت نتانیاهو، نخست‌وزیر اسرائیل، و گالانت، وزیر دفاع سابق، را صادر کرده بود، پس از اتهامات سوء رفتار جنسی از سوی یکی از کارمندان سابق، توسط کشورهای عضو با رأی قاطع برکنار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19735" target="_blank">📅 14:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19734">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سوأل شما : ترامپ رئیس قوه مجریه است، اما همه چیز را نمی‌تواند شخصاً جابه‌جا کند. معاون رئیس‌جمهور یک جایگاه انتخابی در قانون‌اساسی است که برای تغییر ونس ، پای کنگره و مقررات صریح قانون اساسی وسط می‌آید ؛ تنها راه‌های عملی برای رفتن او، استعفا، مرگ، یا در موارد خاص فرآیندهای قانون اساسی و رأی کنگره است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19734" target="_blank">📅 14:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19733">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیکزاد، نایب‌رئیس مجلس :اقدام نابخردانه دولت اوکراین درهدف قراردادن کشتی ما بی‌جواب نمی‌مونه
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19733" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19732">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سازمان دریایی بریتانیا یک گزارش جدید در جنوب دریای سرخ دریافت کرده است.
گزارش شده که یک نفتکش در نزدیکی خود، برخورد/اصابت موج آب ناشی از یک پرتابه ناشناس را مشاهده کرده است. گزارش‌ها تأیید می‌کنند که کشتی و خدمه در سلامت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19732" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19731">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۴ : منابع تأیید شده گزارش می‌دهند که جی دی ونس شایعات و نگرانی‌ها در مورد ذخایر مهمات ایالات متحده را دامن زده است. در صورتی که اگر مشکلی بود وزیر جنگ باید این را عنوان کند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19731" target="_blank">📅 14:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گرندپری فرمول یک بحرین به کشور مالزی منتقل شد : دلیل جنگ ایران و آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19730" target="_blank">📅 14:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شورای اتحادیه اروپا پنج قاضی دادگاه‌های انقلاب و یک هکر ایرانی را که می‌گوید در «نقض جدی حقوق بشر» دست داشته‌‌اند در فهرست تحریم‌های خود قرار داد.
«مصطفی نریمانی»، رییس شعبه سوم دادگاه انقلاب کرج؛ «ابوالفضل عامری شهرابی»، قاضی شعبه ۱۱۹۱دادگاه تجدیدنظر کیفری تهران و معاون پیشین دادستان اراک، «مهدی راسخی»، قاضی شعبه سوم دادگاه انقلاب رشت، «محمدرضا عموزاد»، رییس شعبه ۲۸ دادگاه انقلاب تهران و قاضی مشاور شعبه ۱۵، «محمدرضا توکلی»، رییس شعبه اول دادگاه انقلاب اصفهان پنج نامی هستند که به‌دلیل محاکمه اقلیت‌های مذهبی و مخالفان سیاسی توسط شورای اتحادیه اروپا در فهرست تحریم‌ها قرار گرفته‌اند.
اتحادیه اروپا همچنین «نیما صالحی» را به دلیل همکاری گروه هکری «آشیانه» با پلیس فتا و سپاه پاسداران و نقش این گروه در حملات سایبری علیه مخالفان داخلی و نهادهای خارجی و کمک به سرکوب جریان آزاد اطلاعات، تحریم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19729" target="_blank">📅 14:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">العربیه: منابع آگاه گزارش دادند که واشنگتن و تهران پاسخ‌های خود را به پیشنهاد پاکستان و قطر برای از سرگیری مذاکرات ارائه کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/19728" target="_blank">📅 14:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from❤🦁💚</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJok1OI0LMlMcHWk_pIm9nSlY_NBmyT53H2TktSIn8QUGjPTSLpITXFnmxE5jeacRjG4lIfuHAwX0zNqoriuy2ZycRJ_IUZJh_LVoTWHfYZxvUFzFGcgmaMO7uIBd2jWIUvJcoLxVp5sGBW_KxG3v6kTbYdXrnZ2YoKeY5GT58VUU200C8IppNOKnnDrUEn4H5poqx6Nq7QjTQpZOpSNlHnNAwTqe4JtpAM7L4mmCVDyDBz-uRw6zrlq7-7COjGUVXnbvnUn5q65_PVzX5oy27cZWA_9RX_W7pQxnVCJ8P_BPN6HgoHypccXc8yLOpHcPwo7huvp-xZ3suq-rMtOYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار داداش دیشب سنگ قبر رفیقم طاها نادری رو جاوید نام شهرضا رو شکستن حروم زاده ها دارن سنگ قبر جاوید نام ها رو تو این شهر میشکنن حروم لقمه ها از قبر هم هراس دارن ولی روز انتقام نزدیگه</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19727" target="_blank">📅 14:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کاخ سفید: در مورد ایران هنوز همه گزینه‌ها روی میز است
در پی گزارش رسانه‌های آمریکا که دونالد ترامپ فعلا از تشدید عملیات نظامی علیه ایران منصرف شده است، کاخ سفید تاکید کرد که همچنان «همه گزینه‌ها» در مورد ایران روی میز است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19726" target="_blank">📅 14:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjzBKSgz8M8DkMSiEnH7mowSo5KXYNQ8Nkhn8fKDm-xrvPhyBE0Nc6QTm54f8QoUwc8FVuQbLTmK_ZxkkKlJB7pM9QKAQoc44cKXJqb9FMBNj55rCDvJiTlvZOfqJmF1fJUTPhDawSedAZV71Nj63kmxY2za_OAtmi36ihucaYc-tYVtd9_osMxENsJL3X7D95oFXd_c_0FgV8Fq9SVYHVIzhVESPWKY4w9s_ooePH6OZNUFS39YWfNje_fTAgRn4G0IFHjmIG-6s889LC_8eRKOHQ_I4MFeGUGlHDhTbKImcdujofHG7N6lLrKss6fQ4fZDO_tvjMk43DJKYkIG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:این هفته با ترامپ ملاقات خواهم کرد تا درباره تمام موضوعات، از جمله ایران، گفتگو کنیم. @WarRoom
🚨
🚨
🚨
🚨
یاشار : آلبوم جدید داره میبره رو کنه
😁</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19725" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو:این هفته با ترامپ ملاقات خواهم کرد تا درباره تمام موضوعات، از جمله ایران، گفتگو کنیم.
@WarRoom
🚨
🚨
🚨
🚨
یاشار : آلبوم جدید داره میبره رو کنه
😁</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19724" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y42wzKKbDiXMeOcl8zwnVjJzhsPIVmVSJSHq0n-j6CKlJYPphJ6Qnja6KCApXIp8cTvXgnVEhY-IpIUJYlSWuqImIIidU2tILuYNmhfw2xmF9WMiZNcDCTbBcryDfp-dal_G7agZ57_HS_Lo3QPU93wam_0X2DzAELfhVmJOMG7bpcjzmEXjCQacDHMvNtYOnzVFRLOf6ZrAdZ9P5TOcSrrV3F-6h1nY0w32IoP-J0S6LVD689KMzbXehADpCT71oHhGgIPW_ZchLt4X93mxVc7Zju9NSH_mxxUFlhD9LWG--OcqfgHBag-GGmCZzVsoN00snnA9FpdV0LACMi9i4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن شرتی و غول برره که به مرده ها هم  رحم نمی‌کنند و پریدن توی‌ کادر زیر تابوت اکبر عبدی و بلند میگویند الله اکبر.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19723" target="_blank">📅 13:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw4jSYI5-N47siZ4tmpDIIhGsw57p-5lakNFx5JneBOoT4JgFHnVP8E6UmOXHHSWQZ2NjZHn46AhLCCmRfwKwIQOkLv0gFc0ocv0aFl754v4gvnHrDHJ1eSWVN7NC2pPwMW7kGPJOUs8_x_kqdVOl8LShVFLa5NDVVUzcE-Pfyx8byrgNJqoPNr9IBSW6zsc2k_JIGOHcDpEJx3hEgSU8pkk_y4Ml5JqBLHkf1SpxHQP_9dxQC_9mmL4lHPvJC0CdQGzPNeYlYlSs_yljr3lDlFF29sdPVMy0xWWMCh-f45r-oLUIZWWDYVm-BFXIJ-j8-uKGPs-Ax4MkRAE2I0pSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از وقوع حادثه‌ای در جنوب دریای سرخ دریافت کرده است. به UKMTO گزارش شده است که یک نفتکش شاهد پرتاب یک پرتابه ناشناخته در نزدیکی کشتی بوده است. گزارش‌ها تأیید می‌کنند که کشتی و خدمه در سلامت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19722" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هم اکنون هدف قرار گرفتن یک کشتی دیگر در دریای سرخ
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19721" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سخنگوی ارتش: با توقف حملات آمریکا، عملیات تلفافی‌جویانه را متوقف کردیم
ما برای تمام سناریو ها آمده ایم
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19720" target="_blank">📅 12:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ویدیو انیمیشن بسیار زیبای تحلیل فرضیه حمله به کوه «کلنگ گزلا»زیر نویس فارسی هم زدم ، از دست ندید
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19719" target="_blank">📅 12:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات سابق و کارشناسان هسته ای گزارش داد، اگر دونالد ترامپ، رئیس جمهور آمریکا حملات آمریکا به ایران را گسترش دهد، واشنگتن می تواند چندین تاسیسات هسته ای باقی مانده را فراتر از کوه کلنگ هدف قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19718" target="_blank">📅 11:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تلگراف: وزیر دفاع انگلستان قصد دارد روابط با دولت ترامپ را بازسازی کرده و همکاری‌های امنیتی را تقویت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19717" target="_blank">📅 11:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یِوگن کورنیتشوک، سفیر اوکراین در اسرائیل، در گفتگو با N12 به حمله به یک کشتی ایرانی در دریای خزر اشاره کرد: "کشتی که در دریای خزر مورد حمله قرار گرفت، قطعات مربوط به پهپادها و موشک‌هایی را حمل می‌کرد که در راه ایران بودند، نه کالاهای غیرنظامی، همانطور که ایران ادعا کرد. این اولین باری نیست که به اهداف نظامی این‌چنینی حمله می‌کنیم، و البته می‌توان انتظار داشت که دوباره به آن‌ها حمله کنیم. از نظر ما، این یک هدف نظامی مشروع است."
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19716" target="_blank">📅 11:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCnoEbbwuvXAE5ysbkN40RR3G4aZT_h8tbobqeVQ3O5BlJNqDIIY1uPL_9QQtEC0qZZtUUubsZs69uRJ_aFFlwYHTwq3sukLIEdO3IZSpXrKDkwwZ4EHwNLsOGyTgNAW-ePonbUaMg6npBBFvOXCSxu_3B0RprS-WyS8JO560WJ5zVLn7_iUY-MJGKFZixag0fhP-5Ia9FHQOVjS0XJ_8wFt-i15Oer7XamLYIBMnF5f8Vp6hCJAOWxBeBz8DM6jf_TpwuJXYTp0XT3eWkF8AyTnahbhhg2-7qc0ubKUtkTLzhmisG3tQIZEsTe5r4l9MklEZCXAbCL6-0qypAbWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون حداقل ۱۷ فروند هواپیمای ترابری نظامی آمریکا از نوع C-17 و C-5M و سوخترسان در حال رفت و آمد به خاورمیانه هستند
@WarRoom
دیروز خبر فیکی مبنی بر پایان نقل و انتقالات پل هوایی آمریکا پخش شده بود !</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19715" target="_blank">📅 10:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امروز چهارم مرداد؛ سالروز درگذشت رضاشاه کبیر پدر ایران نوین
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19714" target="_blank">📅 09:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدا و سیما :
‏ سناریوهای احتمالیِ آمریکا در مقابل ایران
سخنگوی ارتش
: یکی از راهبردهای آمریکا خروج از جنگ است البته اگر اسرائیلی‌ها اجازه بدهند.
سناریوی دوم
اینکه تحت فشار اسرائیلی ها عملیات هوایی گسترده انجام دهد. یا انجام عملیات زمینی.
‎
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19713" target="_blank">📅 09:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">به گزارش سی‌بی‌اس نیوز، مذاکرات عمان و ایران برای بازگشایی تنگه هرمز پیشرفت‌های مثبتی داشته، هرچند رسیدن به توافق نهایی نیازمند زمان است. همزمان با سفر روز جمعه مقامات عمانی به تهران، آمریکا نیز برای جلوگیری از اختلال در این روند حساس دیپلماتیک، بمباران‌های ۱۳ روزه خود را عمداً متوقف کرد؛ موضوعی که کاخ سفید و سنتکام حاضر به اظهارنظر درباره آن نشدند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19712" target="_blank">📅 09:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19711">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شبکه کان اعلام کرد که اسرائیل امروز تمدید وضعیت اضطراری را تا ۱۱ آگوست (۲۰ مرداد) به دلیل اوضاع در ایران و لبنان تصویب کرد. همچنین در مورد سفر نتانیاهو به آمریکا گفت: نتانیاهو فردا به واشنگتن سفر خواهد کرد و روز سه‌شنبه باترامپ درباره موضوع ایران گفتگو خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19711" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19710">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شان پارنل، سخنگوی ارشد پنتاگون در بیانیه‌ای به سی‌ان‌ان گفت: «ارتش آمریکا قدرتمندترین ارتش جهان است و هر آنچه را که برای اجرای عملیات در زمان و مکان مورد نظر رئیس‌جمهور نیاز دارد، در اختیار دارد.»
«ما عملیات‌های موفقیت‌آمیز متعددی را در سراسر فرماندهی‌های رزمی اجرا کرده‌ایم، در حالی که اطمینان حاصل می‌کنیم ارتش ایالات متحده دارای زرادخانه‌ای عمیق از توانمندی‌ها برای محافظت از مردم و منافع ما است.»
@WarRoom
part5 final cnn</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19710" target="_blank">📅 09:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19709">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بر اساس گفته چندین منبع‌ به سی ان ان، افراد کمی در حلقه نزدیکان ترامپ یا در داخل پنتاگون بر این باور بودند که گزینه‌های رئیس‌جمهور برای تشدید تنش، نتایج مورد نظر او را به همراه خواهد داشت.
پیش از آغاز جنگ، کین و سایر رهبران نظامی به ترامپ هشدار داده بودند که یک کمپین نظامی طولانی‌مدت می‌تواند بر ذخایر تسلیحاتی آمریکا تأثیر بگذارد(استراحت بین حملات لازمه برای پر کردن ذخایر)
@WarRoom
part4</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19709" target="_blank">📅 09:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19708">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به گفته یک منبع آگاه، تا بعدازظهر جمعه، دولت ترامپ هنوز در حال بررسی این موضوع بود که تشدید احتمالی تنش چگونه خواهد بود. این منبع گفت که کشورهای حاشیه خلیج فارس در گفتگوهای اخیر خود با مقامات دولت خواستار خویشتن‌داری شده‌اند، اما اذعان کرده‌اند که ایالات متحده توانمندی‌های منحصربه‌فردی دارد که در صورت تمایل می‌تواند از آن‌ها برای تشدید درگیری استفاده کند.
@WarRoom
part3</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19708" target="_blank">📅 09:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19707">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">استیون چونگ، مدیر ارتباطات کاخ سفید، در بیانیه‌ای گفت:
«با توجه به ترکیب تحریم‌های موفقی که اقتصاد ایران را فلج کرده و ۱۳ روز پیاپی حمله به اهداف نظامی در پاسخ به تجاوزات مکرر آن‌ها، عاقلانه است که ایران برای رسیدن به یک توافق مذاکره‌شده تلاش کند. در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
@WarRoom
part2</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19707" target="_blank">📅 09:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19706">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یک منبع آگاه و یک مقام آمریکایی به سی‌ان‌ان گفتند که جی‌دی ونس، معاون رئیس‌جمهور، و ژنرال دن کین، رئیس ستاد مشترک ارتش، هر دو در جریان نشست روز جمعه در کاخ سفید و در حالی که رئیس‌جمهور دونالد ترامپ در حال بررسی این احتمال بود، نسبت به تشدید جنگ در ایران ابراز نگرانی کردند.
@WarRoom
part1</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19706" target="_blank">📅 09:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19705">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ به LCI : توقف موقت حملات به معنای عقب‌نشینی نیست, برای انجام حمله گسترده علیه ایران آمادگی کامل داریم!
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19705" target="_blank">📅 09:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19704">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزارت امور خارجه: گفتگوهای ایران و عمان درباره تنگه هرمز که در تهران برگزار شد، سازنده و مفید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19704" target="_blank">📅 08:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19703">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2743288b5.mp4?token=PXmFXVudkdvdIWIGLEytlNhIccnFoh7ebUu-SePaqBHpTjX5LmFoRA5nqRRoYE1j4O0OJ3ThMX7Bokaf9bLqbKGJDX5i_m0ZlhDQcIJDqGPZfG3IIRJEMdN6iuSah5T9DRW5yiWUsoKS_xJcGgh-jsdquJSRGkswPPaYhf7eC67KkxysRYPbP1lEMb5dJSHbLMQeaUTSQvTa5GyzHj5B_WiGZdbPnekxn79kJ9VoeFUYcBoJZ49UrUyDVcHc6lx0tsnLHHETZF7nWWmL_nHnAHjKXb6zkXC1M4NMAT42egjAO_ah73c0oW4aitv82Fl5TsClASGGs9-QyoKMMlKvnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2743288b5.mp4?token=PXmFXVudkdvdIWIGLEytlNhIccnFoh7ebUu-SePaqBHpTjX5LmFoRA5nqRRoYE1j4O0OJ3ThMX7Bokaf9bLqbKGJDX5i_m0ZlhDQcIJDqGPZfG3IIRJEMdN6iuSah5T9DRW5yiWUsoKS_xJcGgh-jsdquJSRGkswPPaYhf7eC67KkxysRYPbP1lEMb5dJSHbLMQeaUTSQvTa5GyzHj5B_WiGZdbPnekxn79kJ9VoeFUYcBoJZ49UrUyDVcHc6lx0tsnLHHETZF7nWWmL_nHnAHjKXb6zkXC1M4NMAT42egjAO_ah73c0oW4aitv82Fl5TsClASGGs9-QyoKMMlKvnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاصره دریایی ایالات متحده علیه ایران همچنان به طور کامل برقرار است. از ۲۵ ژوئیه، سنتکام ۱۲ کشتی تجاری را که سعی در عبور از محاصره داشتند، تغییر مسیر داده، ۲ کشتی را که رعایت نکرده بودند، غیرفعال کرده و ۲ کشتی دیگر را برای اطمینان از رعایت کامل محاصره، سوار بر آنها کرده است.
اوایل امروز، نیروهای آمریکایی عملیات تأیید ورود به کشتی M/T Charminar با پرچم کومور را در دریای عرب تکمیل کردند و این نفتکش اکنون به سفر خود ادامه می‌دهد.
نیروهای سنتکام، M/T Lavine با پرچم موزامبیک را در ۲۴ ژوئیه در خلیج عمان غیرفعال کردند، پس از آنکه خدمه چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران در حال حرکت نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19703" target="_blank">📅 03:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19702">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک پهپاد در نزدیکی منزل ایتمار بن گویر، وزیر امنیت ملی اسرائیل، سقوط کرده است ، جزئیات در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/19702" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19701">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دریای قزوین
😁</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/19701" target="_blank">📅 23:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19700">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزارت امور خارجه ایران:
ما محکوم می‌کنیم اقدام دولت اوکراین مبنی بر حمله به یک کشتی تجاری ایرانی در دریای قزوين«خزر»که امروز صبح رخ داد. این حمله منجر به انفجار کشتی و شهادت یکی از ملوانان و زخمی شدن ملوان دیگری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/19700" target="_blank">📅 23:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19699">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال ۱۴ : ترامپ دستور توقف تمام حملات به ایران را صادر کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/withyashar/19699" target="_blank">📅 22:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانال 12 : بنیامین نتانیاهو تصمیم دارد در نشستی در کاخ سفید، اطلاعاتی درباره پیشرفت برنامه هسته‌ای ایران را در اختیار ترامپ قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/19698" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">زلنسکی : ما دریافتیم که ماهواره‌های روسی به تهران در حمله به مناطق خاورمیانه کمک می‌کنن
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/19697" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرگزاری وای‌نت : قطر و عمان ،رژیم تهران را تحت فشار گذاشتند تا سازش کند و از یک عملیات تقریبا قطعی و بزرگ آمریکا جلوگیری کند
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/19696" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ممد باقر : حملات ما به اهداف آمریکایی در منطقه، تا زمان تسلیم کامل دشمن و به عنوان انتقام خون کودکان بی‌گناه در میناب، لامرد و سایر مناطق، ادامه خواهد داشت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/19695" target="_blank">📅 21:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🥛
امشب دوغ  میزنمااااااا</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19694" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ , تلفنی به یک خبرنگار از شبکه فرانسوی LCI:
اگر از ایران ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19693" target="_blank">📅 21:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ : آمریکا «آماده حمله گسترده» به ایران است (کانال ۱۴)
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19692" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19691" target="_blank">📅 21:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سخنگوی سپاه: در طی ۱۵ روز نبرد، نیروهای مسلح ایران ۱۱ فروند جنگنده و بالگرد آمریکایی را در پایگاه‌های منطقه و روی زمین منهدم کردند؛  شامل یک F-15، یک P-8، یک C-17، هشت هواپیمای سوخت‌رسان و ۱۷ پهپاد شناسایی و عملیاتی.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19690" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ایلان ماسک: در سیاست زیاده‌روی کردم!
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19689" target="_blank">📅 21:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رادیو و تلویزیون اسرائیل:
در حال حاضر بیش از 90 هواپیمای سوخت رسان آمریکایی در اسرائیل مستقر شدند، موشک های رهگیر پدافند به صورت گسترده در حال ورود به اسرائیل می‌باشد، هواپیماهای ترابری آمریکایی بدون وقفه وارد اسرائیل می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19688" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شبکه
I24News:اسرائیل برای یک حمله گسترده از سوی آمریکا در پایان این هفته آماده‌سازی می‌کرد، اما این حمله اتفاق نیفتاد. تخمین‌ها نشان می‌دهد که آتش‌بس فعلی موقتی است و هدف آن فراهم کردن زمینه برای گسترش دامنه عملیات نظامی در آینده است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19687" target="_blank">📅 21:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19686" target="_blank">📅 21:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbDhrkWXLQBN8jc4SgXfhsgYoBNopCdRj-cX81zuT7GGzdilv92oQr5wLO0BHCDVzHtpJ9dIA3lhlfTRBbOr-pa_a9sZPumLGqkbLyW61291fY81RhslQ21b-g2lkz5jMv8qSulFV4MKp1Sa1UjYYc4rfbEwyllwmNBYiWxSPlsoK2FF9KtcDlDukbo08_yKG-137qKF3KCVxi0uGq97R4A3NQHsoLHFr67rktxglje42n41fmDn6xngDr24z53jQdEImSNrM_SvUFbfv9uCOaPxjmEH5XE_YvFN29wkpazo-2aqvSDHh6oIVFyPtJThPjt3N1Txn0fdCK1R2rAr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقال مجروحان آمریکایی از اردن و کویت با هواپیمای C-17 گلوبمستر به بیمارستان نظامی آلمان؛ مقصد نهایی مرکز پزشکی لنداشتول
بر اساس گزارش‌های منتشرشده، شماری از نیروهای نظامی آمریکایی که در جریان حملات اخیر در منطقه خاورمیانه زخمی شده بودند، پس از دریافت مراقبت‌های اولیه در پایگاه‌های منطقه‌ای، با هواپیمای ترابری ـ پزشکی
C-17 Globemaster III
نیروی هوایی آمریکا برای ادامه درمان به آلمان منتقل شدند. مقصد این انتقال،
مرکز پزشکی منطقه‌ای لنداشتول (Landstuhl Regional Medical Center)
در ایالت راینلاند-فالتس آلمان بوده است؛ بیمارستانی که سال‌هاست به‌عنوان مهم‌ترین مرکز درمانی ارتش آمریکا در خارج از خاک این کشور برای پذیرش مجروحان جنگی فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19685" target="_blank">📅 20:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19684">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19684" target="_blank">📅 20:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19683">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromَ</strong></div>
<div class="tg-text">یاشار جان سلام خسته نباشی اول از همه مرسی از زحماتی که میکشی ، من المان زندگی میکنم بعد ما رفتیم بیمارستان ارتش مخصوص کسایی که زیر نظر بیمش هستن فامیلمون عمل لازم بود قبولش نکردن گفتن تو حالت اماده باش هستیم پرسیدیم برا چی بخواطر جنگ خاورمیانه گفتن اره  هرچی خواستیم ازش جزئیات بیشتری بگیریم گفتن محرمانه هست هیچ جوابی بهمون ندادن</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19683" target="_blank">📅 20:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیویورک پست: ایران در هفته‌های اخیر دفاع خودشو به‌شدت تقویت کرده و برای سناریو حمله زمینی آماده شده
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19682" target="_blank">📅 20:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19681" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دو شرکت زیرمجموعه لوفت‌هانزا آلمان پروازهای تل‌آویو را تا سه‌شنبه لغو کردند
این تصمیم در پی ادامه نگرانی‌های امنیتی و ارزیابی وضعیت منطقه اتخاذ شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19680" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سفارت آلمان و فرانسه رسما شایعه تخلیه کارکنان خود را تکذیب کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19676" target="_blank">📅 20:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19674" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19673" target="_blank">📅 20:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19672" target="_blank">📅 20:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUN_eJQuGOgbDTZrU2Qpr4P_fLAgA_4bfyTho2Z0YSwpk5nyXlizc5dwILAsS-JwSkcrfzh_9ZWI-ivjx4N5sKq_KvMxIB9KYLsNZuhS5S1dZ11gykqo7VeliULTcnu6Cr2rHCQKEkY6SqRZzzEoLDiMmlwV2_Tgi0amSPvVZ-2gayZJ6Xb964myizxgrbeIzJw_lv_g62MmXYhxq96LGmP380Hwq4bvfIbaie6mZNleieIrtxpZpqjRPlkoZ8yQLUWxQzOrmMD153jmSOxguWFlWaxS3XSsUDtv_xhGdwR4BDesKNySAe7e1e65nd0pLdxDlYS1BEEzqk56kmcDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ریزه کاری هایی داره ولی خیلی سخت بود تا این بشه ، سلیقه داداش رو که قبول دارید
😎</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19671" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19670" target="_blank">📅 19:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی عربستان
سازمان عملیات تجارت دریایی انگلیس از اصابت یک پرتابه به نفتکشی در ۷۰ مایلی ساحل الشقیق عربستان خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19669" target="_blank">📅 19:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHrcTBdGrbmNjBB9gUgsw9MGcZnodWS7HyUSffOX_QZQRJhIP9y4iEKyhY7dGi_ewyjCbziFbakp7WbvTZBpIaScSSwioJ6HJ4ze4nwo_mEHjFbgVvZOZSkT8ooO2478TJQ0THQ8V9PAWTZSRNDyCajkM-NHeqXJ3JgHW2ns3zrfDCtJTWPj4Lf69xvBXf7K5dsIin5FW3fd1n5KVwwA9fqXAoH7lbXuwb7PmYuAfiTsqOviR6llFD-VcSI2TynjcJmmT4pMC5WGSHEhU5HEHo-XTzIOLYs-2TOG4WCstHeGuMkIQMEPiA6FaeTiw24v2Lhyowdq92C0qZeMILDWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یک هواپیمای آواکس E-3 Sentry در فرودگاه جده فرود آمد
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19668" target="_blank">📅 19:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWa8xs70k6U7fJN1fiYUmOHqtWIYTl6bH0c_RSIOCIi-Dy0sBFFklni-6CbnRvFzNs964fWrJZwrk7GLWzUbYa0CeT48pxxfL1f6prmqyrjuUKk2E64j9KJoO9_FWyCdJiqtXUXG22mDdKpW-eKws9VkkQDYQR7zisb3la_zEYFZKrS1GIfIPkmsyrw-MTyc1ldF5Kzf46EwvbanH36bamnH_Q4YrpMIQg52CT-3EfizHxXnoGmeNUJXUZIMBSKosZsIHa692zZHPSONsnuPWSIsRynpPQTtum7ZDXqYuHjcoMVSlklCXxvl4wIVCYqYCTKH6zrDShpdWFYXsXcszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان هم اکنون در آسمان اردن
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19667" target="_blank">📅 18:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اکسیوس با رد خبر رسانه‌های عبری:
آمریکایی‌ها دیروز برای یک عملیات گسترده‌تر علیه ایران آماده نشده بودند، بلکه برای حمله‌ای با همان حجم و ابعاد حملاتی آماده شده بودند که در دو هفته گذشته هر شب انجام شده بود
.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19666" target="_blank">📅 18:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به گزارش کانال ۱۲: آماده‌باش در سطح بالا در اسرائیل برقرار است؛ آنها منتظر تصمیم ترامپ در مورد آینده رویارویی با ایران هستند, همچنین شرکت‌های هواپیمایی خارجی لغو پروازهای خود به مقصد و از مبدأ اسرائیل را آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19665" target="_blank">📅 18:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وای نت : ترامپ قرار بود دیشب یک حمله بسیار گسترده به ایران انجام بده ولی وسط کار نظرش عوض شد و تصمیم گرفت فعلا به ایران فرصت بده تا مسیر دیپلماتیک جواب بده!
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19664" target="_blank">📅 18:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏وزارت حمل‌ونقل قطر اعلام کرد از روز ۲۶ ژوئیه، تردد تمامی کشتی‌ها و شناورهای دریایی به طور کامل از سر گرفته می‌شود. با اجرای این تصمیم، همه محدودیت‌های اعمال شده بر فعالیت‌های دریایی لغو شده و عبور و مرور در آب‌های قطر به وضعیت عادی بازمی‌گردد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19663" target="_blank">📅 17:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تلگراف : یک مقام ایرانی ناشناس، بریتانیا را تهدید کرد و هشدار داد که در صورت مشارکت این کشور در جنگ به همراه آمریکا، مقر نخست‌وزیر هدف قرار خواهد گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19662" target="_blank">📅 17:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وال استریت ژورنال: موشک‌های خیبرشکن ایرانی با ترکیبی از مسیر‌های پروازی، مانور‌ها و سرعت‌ها، سامانه‌های پدافند هوایی را گیج می‌کنند
این موشک‌ها بسیار ارزان‌تر از رهگیرهایی هستند که برای انهدام آن‌ها استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19661" target="_blank">📅 17:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اکسیوس: طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است @WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19660" target="_blank">📅 17:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19659">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foO9FHBSigBCVS-4FiGaTiAuK2m2CLv0NJH3ejxcuLL3hY8D9GugYdZui0mZ1oOu_sgj0bPkP75K3luhpfxKQiEMHm3FcaKNj3I390ZhagcDvS5m8nuSiMKwAl2GtaFrwW1FyU5we6uXoTWSYmAqk6U7jtgsveVbtKZ29koyOppsCQG0xruddsHyCWg2fRnaU1Vk7K12CKyUMLAqRH3jDvaSUl0wjvST6Zxb2PsgchI3j5gx-y_ERI-064XqK0hEuRbwwqT_rFT_vJ3ONcS4seav7WbKTN7SDAbDyvp6kOYSqCZxSAQCyZanrBGNZSjNpm7n45SCLFCcekKs9mYD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسال سنگین تجهیزات و مهمات به اردن فقط در همین لحظه ۴ هواپیما C17 در‌ مسیر رفت و برگشت ! نشان میده آمریکا در حال کشیدن کامل کمان «فول دراو» است
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19659" target="_blank">📅 16:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ورودی جدید
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19658" target="_blank">📅 16:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH</strong></div>
<div class="tg-text">الان جدی جدی آمریکا قبول کرده ایران فقط تنگه رو باز کنه و پولم بگیره؟؟</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19657" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اکسیوس: طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19656" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
