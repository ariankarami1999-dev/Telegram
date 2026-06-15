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
<img src="https://cdn4.telesco.pe/file/ZzDp9W0ZDLtejLlQiyPBG8RhXlGzCcQ_fletEC4kPUO2-L9y4xL4bBFV22D2AO5OkVAlWfvdEFzCZI7Y3bHmtK3IvxEeM3Ox0rm_nobh7D9u9fVkjI3p81JqE9rH-UhZgNlL-S2VrrJkiVHRCwg9bVWvdyF9F6XawkjLT4F5eCacKOv-tEDRljrqwKiUZhpC4zZd4Zzd3eQ3ec3OU9jySMZ8p2o2Q8ZamazJ0fCiBzeUoVPmBT-XAUTXAPvhXJwxLhJ4piXOxaZdeSsgeGqFcqN4X65NsrFZzg5oS31Z1ImtiLTSNO-szc2MCFJsLSuBGGDEZSbKqVO-jKhZesQmCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.52M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-659829">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
پهپاد اسرائیلی یک خودرو را در جنوب لبنان هدف قرار داد که طی آن راننده خودرو به شهادت رسید
🔹
این نخستین حمله مرگبار اسرائیل به لبنان از زمان اعلام توافق آتش‌بس بین ایران و آمریکاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/659829" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659828">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e249466fd7.mp4?token=a8Ii9vllzJxne0DfNhbFc8ouzqlm2l_4UpPzioG2pVfUUoA51vFPTI596rtU9J7t-SzgKoGW2R5K5yFaGslj5t4pEf-7K98uga3bz4YrzDlB4r_NMuzVWA4_R0anIU_4PWhtnmQHH1V6cojdOd14BZZo4TA2Ip6hB73sTCgdus7GCk1sw3nY8FffubVfKHb7QDxJn71mvK_c0P9TtFLpWE0R3pmfAH2cMWhcftYJQPLAdwUwfLii04dyQFHekz6rS2Wi21yE_0znpWZbqLh33p4iMqJl-REdw3Cfpt192kgIC-Q4VcJa85uFKfW9eXfmj28O9zj3oX4_KFgWLWQXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e249466fd7.mp4?token=a8Ii9vllzJxne0DfNhbFc8ouzqlm2l_4UpPzioG2pVfUUoA51vFPTI596rtU9J7t-SzgKoGW2R5K5yFaGslj5t4pEf-7K98uga3bz4YrzDlB4r_NMuzVWA4_R0anIU_4PWhtnmQHH1V6cojdOd14BZZo4TA2Ip6hB73sTCgdus7GCk1sw3nY8FffubVfKHb7QDxJn71mvK_c0P9TtFLpWE0R3pmfAH2cMWhcftYJQPLAdwUwfLii04dyQFHekz6rS2Wi21yE_0znpWZbqLh33p4iMqJl-REdw3Cfpt192kgIC-Q4VcJa85uFKfW9eXfmj28O9zj3oX4_KFgWLWQXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا پایان تابستان، تعداد لابراتوارها را به ۱۰ مورد می‌رسانیم
سجاد محمد علی نژاد معاون مالی و اقتصادی شهردار تهران در مراسم رونمایی از لابراتوار سیار خلاقیت و ساخت:
🔹
این لابراتوارهای سیار برای گروه‌های سنی مختلف، از دانش‌آموزان هفت‌ساله تا مقطع دبیرستان، طراحی شده‌اند و با توجه به میزان استقبال و نیاز مناطق مختلف، به‌ویژه در جنوب تهران، خدمات آموزشی و مهارتی خود را گسترش خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/akhbarefori/659828" target="_blank">📅 18:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659827">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txuoEBBGh33YN_yVGuvjPBOw-97pTz2_5EV1vRYENk3SXGfcMcCuHAOpfoM7SOf9dUxkjMEIAHUCqvIty9zghGyarhkk9ocusizcsMbqbvkkM4rZelafIRndzrYPAmuc4EaXoHzpZuncRIL5x1EXn5uZPm2gEO7gxE5b66m_GGUjZ-M4_juEJZxMAuR5EIwAZtcYYgwy_uCdFc0tW_HpK7OJObESDEvEErVMpDI6eWaZ8fwmOSFtG8V25MW0Pj6EbDnXkS7D9jtyYm97frp176QkT4dLv8FJIRCvPxCd3gNkSVqLugHy6Ss-VzNUAqHf3L6B0s_YFnikjXyldjSLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابن مسکویه؛ دانشمندی که در غرب شناخته‌شده‌تر است
🔹
شاید همه ما اسم ابن‌سینا را شنیده باشیم؛ اما کمتر کسی ابن مسکویه را می‌شناسد. فیلسوفی که اندیشه‌هایش درباره اخلاق همچنان تازه است و در تاریخ‌نگاری نیز جزو نخستین تاریخ‌نگارانی است که تاریخ را نه براساس…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/659827" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659826">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حمله انتحاری به یکی از پادگان‌های وزارت کشور سوریه
🔹
وزارت کشور سوریه از وقوع یک حمله انتحاری به یکی از پادگان‌های وابسته به این وزارتخانه در استان رقه خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/659826" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659825">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
شرط‌گذاری جدید معاون ترامپ برای توافق با ایران
ادعای جی‌دی ونس، در گفتگو با شبکه سی‌بی‌اس:
🔹
واشنگتن تنها در صورتی آماده تغییر رویکرد است که ایران تعهد عملی خود را با ایجاد «مکانیسم‌های راستی‌آزمایی» برای کنار گذاشتن کامل برنامه تسلیحات هسته‌ای اثبات کند.
🔹
فرآیند توافق باید «ابتدا با بازرسی‌های دقیق و سپس پایان دادن به برنامه هسته‌ای» آغاز شود. موضوع آزادسازی منابع مالی مسدود شده ایران، تنها پس از طی شدن این مراحل و حصول اطمینان از توقف برنامه هسته‌ای مورد گفتگو قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/659825" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659824">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8935d8f26.mp4?token=KJsUPULUt5PbKRGNrBXAlS7R5SCsBlRbCx8oqmkrzmCVpuQYl-Hf6aIKM3ukq0VchEK0fOK7pVupWt6TPRnz_wZugDmndFfM6ofzWpVGNm7SFYFTAI9F-G6T8qcXvPTqkhBmwxkLbdhZEf6rYPPdKONL9lZeccXvoyi2PEsppmgRfUEoIA4ALKHFdBlZu6sliHZ1wPWfvW8mvaQWnYriQ5g1kXYHDdOl2D_pw8olZNIijzx3K6EpPjU1Gy73Y-gPMLhTPyj7kPxwAephcgWcIid42-_8iEP91RoQpB6mz-KDSUft9EJjQ285aDh5YTnqNU8qsDdnHmvZkP1I15gi5KhQnnQml5NrmmFZV1xE7BaTj0sf03o8R-5UoLFt-B6E6KF9zpcd5ztpl6rVLpARMeQSCuIeu8YJqWcQihWHl0M13UX_vB8jL6ag5jCk6AtUMPtwf-hlfwsAzrxuzGNQW_9qKUplB4hC7HFtFLcx7tWIsVKMKO1V6uVp2CN8xhiR407-SaTBfuM8__OFbXOodUt2rGgqIgr3HyQ2ijTdWJf2oIzz74ATPWURzoJ3mzyE7J68Ll9QePYBu4GstLYbGsg1k2H0Xb8WUR1X1LngwyG0yznNFKEioBiLJzuioHjoMAY-M8Aa5w_CHKD51XzDjwfYG8xRmLXca1g1uKs70d8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8935d8f26.mp4?token=KJsUPULUt5PbKRGNrBXAlS7R5SCsBlRbCx8oqmkrzmCVpuQYl-Hf6aIKM3ukq0VchEK0fOK7pVupWt6TPRnz_wZugDmndFfM6ofzWpVGNm7SFYFTAI9F-G6T8qcXvPTqkhBmwxkLbdhZEf6rYPPdKONL9lZeccXvoyi2PEsppmgRfUEoIA4ALKHFdBlZu6sliHZ1wPWfvW8mvaQWnYriQ5g1kXYHDdOl2D_pw8olZNIijzx3K6EpPjU1Gy73Y-gPMLhTPyj7kPxwAephcgWcIid42-_8iEP91RoQpB6mz-KDSUft9EJjQ285aDh5YTnqNU8qsDdnHmvZkP1I15gi5KhQnnQml5NrmmFZV1xE7BaTj0sf03o8R-5UoLFt-B6E6KF9zpcd5ztpl6rVLpARMeQSCuIeu8YJqWcQihWHl0M13UX_vB8jL6ag5jCk6AtUMPtwf-hlfwsAzrxuzGNQW_9qKUplB4hC7HFtFLcx7tWIsVKMKO1V6uVp2CN8xhiR407-SaTBfuM8__OFbXOodUt2rGgqIgr3HyQ2ijTdWJf2oIzz74ATPWURzoJ3mzyE7J68Ll9QePYBu4GstLYbGsg1k2H0Xb8WUR1X1LngwyG0yznNFKEioBiLJzuioHjoMAY-M8Aa5w_CHKD51XzDjwfYG8xRmLXca1g1uKs70d8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد علی نژاد
:
در لابراتوار سیار خلاقیت و ساخت، ایده‌های مفهومی شرکت‌های دانش‌بنیان نوپا را به محصول صنعتی تبدیل می‌کنیم
سجاد محمد علی نژاد معاون مالی و اقتصادی شهردار تهران در مراسم رونمایی از لابراتوار سیار خلاقیت و ساخت:
🔹
در این مراکز، به کارآفرینان و شرکت‌های نوپای دانش‌بنیان تهران کمک می‌کنیم تا ایده‌های خود را از مرحله مفهومی و نرم‌افزاری به محصول صنعتی تبدیل کنند.
🔹
ضروری است که کودکان، دانش‌آموزان و دانشجویان ما از مهارت‌ها و ظرفیت‌های ویژه برخوردار باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/659824" target="_blank">📅 18:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659823">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ارتش آمریکا: محاصره بنادر ایران تا روز جمعه همچنان ادامه دارد
ارتش آمریکا:
🔹
محاصره بنادر ایران همچنان ادامه داشته و در انتظار تکمیل تفاهم‌نامه‌ای که قرار است روز جمعه با ایران حاصل شود.
🔹
ارتش آمریکا همچنین از تمامی کشتی‌هایی که در طول مدت محاصره بنادر ایران آسیب دیده‌اند خواست تا زمان دستورات بعدی، هیچ‌گونه حرکتی نکنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/659823" target="_blank">📅 18:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659821">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای ونس از روایت‌های رسانه‌های ایران از تفاهم‌نامه
معاون ترامپ:
🔹
رسانه‌های ایران درباره دستاوردهای ایران صحبت خواهند کرد بدون اینکه بگویند که تهران چه امتیازاتی واگذار کرده است. برای همه ما مهم است که این رویه را اصلاح کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659821" target="_blank">📅 17:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659820">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای ونس در مورد توافق
🔹
سی‌بی‌اس: ایرانی‌ها می‌گویند که به یک صندوق بازسازی ۳۰۰ میلیارد دلاری دسترسی پیدا خواهند کرد. درست است یا نادرست؟
🔹
جی‌دی ونس: این از آن دست چیزهایی است که آن‌ها می‌توانند به آن دسترسی داشته باشند، به شرطی که به تعهدات خود پایبند باشند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659820" target="_blank">📅 17:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659819">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ترامپ وارد ژنو شد
🔹
ترامپ پیش از عزیمت به فرانسه برای شرکت در اجلاس گروه هفت، وارد ژنو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659819" target="_blank">📅 17:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659818">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1c6103bc1.mp4?token=INJ-PsTCQfnIy-xe6aVLhdICEPt5iQ6M1D4sW0qJcEloFqD4GZM3Pw3Lux-0wymmC0wanpGxrrT2LvpfYL-O_n0wGPM4_NpTMLm9KxUf2Z_Php6qwOvdE9cDUlYDzg_8TcD2OT-JK4DYvPxU2YVmr5DdhW7KrNlHeCWjkDwYyKhw-dpaguwgZdD-FMC-0YukyIjaBG9WiFSo59YA_Bdfa8L2eBDurL5KQ2pWBuAiG8rmMTjCVr0nYeNTDSvHYl8wBwl3lgnRvC-EEimxlbujV5IWPgY0LfuqK4u7MpO-zduDGSTSR783fXoNmpLkjavG289y-6fqzrUM4uzS1JG53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1c6103bc1.mp4?token=INJ-PsTCQfnIy-xe6aVLhdICEPt5iQ6M1D4sW0qJcEloFqD4GZM3Pw3Lux-0wymmC0wanpGxrrT2LvpfYL-O_n0wGPM4_NpTMLm9KxUf2Z_Php6qwOvdE9cDUlYDzg_8TcD2OT-JK4DYvPxU2YVmr5DdhW7KrNlHeCWjkDwYyKhw-dpaguwgZdD-FMC-0YukyIjaBG9WiFSo59YA_Bdfa8L2eBDurL5KQ2pWBuAiG8rmMTjCVr0nYeNTDSvHYl8wBwl3lgnRvC-EEimxlbujV5IWPgY0LfuqK4u7MpO-zduDGSTSR783fXoNmpLkjavG289y-6fqzrUM4uzS1JG53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پارک علم و فناوری تهران
:
هدف از افتتاح این فب لب‌ها کمک به نخبگانی است که ایده دارند ولی امکانات اجرای ایده خود را ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/659818" target="_blank">📅 17:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659817">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پزشکیان: اگر همۀ مفاد تفاهم‌نامه به‌درستی عملیاتی شود، به‌عنوان سندی افتخارآمیز برای کشور تلقی می‌شود
رئیس جمهور:
🔹
اجرای کامل این تفاهم‌نامه می‌تواند بسیاری از مسائل را برطرف کند و شرایط تازه‌ای را در ایران و منطقه رقم بزند. این تفاهم‌نامه نه‌تنها برای داخل کشور، بلکه برای کل منطقه و نیروهای مقاومت نیز افتخاری بزرگ به شمار می‌رود. جزئیات آن نیز ان‌شاءالله در زمان مناسب ارائه خواهد شد.
🔹
لازم می‌دانم از اعضای تیم مذاکره‌کننده تشکر کنم؛ از آقای قالیباف که زحمات زیادی کشیدند، از آقای عراقچی و همچنین از اعضای شورای‌عالی امنیت ملی و همۀ کسانی که در این مسیر نقش‌آفرینی کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659817" target="_blank">📅 17:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659810">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JP5sHYoCBttjdqwdLdP-VSfMUbBZoV-IRkqJTPRARR6ncOKS8Qs4UtOSt6xTUnoASa3bIniNbkGhLH8K_68KNAO2OugLZXYlE3U4vMuHaT1PR0bb5wpcRx5wJIhd_6crSGLvKBN6UtAfDSpS87Kygun1JPr8Uv33-BSmw1HcwnQQ4v0kS9axYAN9et-bTwCXE0PbUGLPKp8owznQib9JqPS5EE5zaJvmrWKE0pNH3WvQXoJ2eWcUlManLuzgfM_nHtWPHg4mkt_XcM8jtVV6BdAWmD1I-250050ugBOO1ebvt3W0xLGkjYoBx7qnd7rE3yryuBXPgJh07DHHK5MfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fddyIW6-gGPqrXJakMnSDjMLZ1Wc4TrTI21hjW6jujbSGBMDmyN1O1OdL3yH4MIxJGut5lXD3p5_azFXThWXnN5V4v_EhHnwwaXMKAibPi-ExZcyrkK7oBgf8TGbPMN-NrXeMG-fZEdIjcruGDA1wcrDYw-KHTsuphxGZOJ8bXSRV8S-slkVbywENxtl1B_8YckBqjQ5EeUQ_FVBFqzOxUMwtuG3ptuGpNxjqxjrR67dq_4QGxdJHjcon3wixnXxdc5lAQuVG-lNueAiK0n0S4-t8ENyNhpEyVwz9OLtCLjXI7zH2XlDth5XHGMqLbsCPiF9cgXOnQr7RTx1JnduxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rgn5m90v7X8jTUT91h6tRM29H1rGlegFvqRMeWLLEKPFOK0jjIpZtfTE9iVtobv6KmoTAJS4Rmz1qz526Z4UU6SGp9BtTWfk0xEcqiw9GQzJ7Mnb__5_KHhEVQjlFnC0NvN6gTVr1oonlDMSFDS7V9jdcJZKslFXffZ5mSd8_TyCc4EwzwM8vQf7Hbo3H_z5uSi29h63Fz1w-5TdeCb1yky73lnK_wdojgeqEqLngP9rClumt59GSIh1DrAi1m6bXYEMunjbJIIIjRMSIAIZNRx87OcpfAogrCApgKH9MUWGMGKYY-n1vqepdwLn7tLUIhZeeJbH3DF2aIk2Kdf_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmvtiigU6JJ5AbEJqS7oZ7ZnrEPTLjOQPmZB4fdUGkyFtl2-A06R7SNLaU9OYQ8_xDomiqKXF9IpmKCtwUP5nAzAEvPpoSFLDUUlalK3VEM832a6retdXqvgCDeCJNIk3LAW_9eqSmlIsAjzRPdZwdlspLWTZaoXOWPm02uaG7yPACICv7-OX9bUaMpVm4ygXEqEM_e7LAWBZOW5VpYvYA1Zxo7aciUMm2-weartVHYf5yCeCNd7XkmxHcaWKcFoLTLx7xJixypiQ2__bQDBaElMYeX-l1QuWKyT_qY9ZM7KQ0FwwPHbYBk0tQXcv-HFPPy4TOO6BxFpa8UT0Z8mTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOCvKtx5GbuuKvfF4cyEZxwNPFy9DPHtF8BIXmX7h4yINgIG41za99NEk4LYLMkeWgrdOjS-TDg2d0P629dTCzXzB6FcuHw2_8Rvx2zFleLUQZPzYosgA4h53BfKvjUnJUx4u243qeM-t3XU6eXHxve5xNO-VDYU8WS0df7R1hpyVMXgKB42NMRyclScRBV8qqqPY8TJKBeBllgPmFUJZ1KBfGKuJ9hZyIcTvqEVhADLnPDq_JH6tDMMJ2a45bArMFNDkpotVD2Qh6joIElfHsmfWrnaePWvuC2JQ3HD-nhSVLkKO8T67pv_0wsvNv9mWnYmCrZVz4bOmPrUGEPCTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2ZbiRMHbb__JUmUboJejH2oGD7EHhcoUvedB09y7vwLpTn1WK_SE6REtBd3PAVkIAnmnXC2iPuCJHJoS844ffjbP9UgASZdZIKfc63b_Q2M0cYIlKr2enlxGWirjxdNh2zTWVHQZ3T0FUz9AduOIXfhIftEyTsZPFvarTm5vMYx6wS0yTacvZVsi0v6gfHeVooVhoSejQclF306ilJoJmQmc0t4P_ZGNBJyXR_cnpNNdNZTXr9kfKjp5edmHw1nvSaIeX-LhcSIg7CvxNfBo8kpWPZ8ng00nuik6UDouUBImDxSM14oR1Lp4affUluXn2deWuDC71GCHWeenYq9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_JafVKfu6fSDXVu1yCa0vbhI2YuuY2v2fA9gvd4GlOrPuUKOD0c9p8e11YG7H2hvzVXhKTIicnu_xexLsXkS4hRgjZSVZLSkGld521WlgdUMWkuugrHKzWRDF_tXkeTRt164gG2zDRShPpXTDFmVrDjkvwhz93ZD-QHcaFgHw5yY30A1RRWDrMFDvz7gmMwvxWN-caVj77XHk6hx83naHWgUfF4_izyipvCyw79DrAXztvU462dQnvRk3GUQuBfRNyZYnKN-gxfC4eDFYpzX2RQi6MNVAD-pyp3i4N9W7hgC63UT9JE2ECWF-S_yXiR60HdBHY4AUrZ6DhKxkfo2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تأکید فعالان اقتصاد دیجیتال بر تاب‌آوری، ماندن و حفظ سرمایه انسانی
🔹
در همایش «نقطه تصمیم»، مدیران و فعالان اقتصاد دیجیتال با تأکید بر افزایش عدم قطعیت در فضای کسب‌وکار، «تاب‌آوری سازمانی»، «یادگیری مستمر» و «سیستم‌سازی» را مهم‌ترین راهکارهای عبور از بحران‌ها دانستند.
🔹
سخنرانان همچنین بر لزوم بهره‌گیری از فرصت‌های نهفته در تهدیدها، ارتقای پایداری زیرساخت‌ها و سازگاری با تحولات ناشی از هوش مصنوعی برای حفظ رشد و تداوم فعالیت کسب‌وکارها تأکید کردند.
🔹
حاضران در این پنل، «حفظ سرمایه انسانی» را مهم‌ترین سرمایه شرکت‌ها در شرایط بحرانی عنوان کردند و همراهی کارکنان را عامل اصلی عبور از چالش‌ها دانستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/659810" target="_blank">📅 17:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659809">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrP7QUex1wVGYGCviWdUuqHIOXL5n4-MrewdLRkZhMiotplExhh2lGcAaGbBavnuxXnvzoqh1HpUnqjHPsiIimRSvo5j5Kh0H8SCogSTepwlVuo76I7y7p3YOe-IbQ5SFM4UC8FTjiVE7aVlSy5K3u9GaqZDpQA9QS2w4AwOKBY-_BKNyhsqR4pDri5pHpZK1D4LMZP_aNUCJiVgaIleSXfvIepL4it-Wp71VmZRIkt_dmfhIUd35PIc5hw6VpgFg-nB9oSdpd5I-Misd4znIr-HrOJIBq2kjjPbNGzmhwBizqS41Vg4i9UZdCLx1OC90Tvr9Rr3AyY9noI3pmwpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری سردار آزمون و آرزوی موفقیت برای تیم‌ ملی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659809" target="_blank">📅 17:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659808">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
افزایش سقف وام ودیعه مسکن؛ پرداخت تسهیلات به ۳۸۴ هزار خانوار
مدیرکل دفتر برنامه‌ریزی معاونت مسکن و ساختمان:
🔹
سهمیه تسهیلات ودیعه مسکن از ۲۰۰ به ۳۰۰ هزار میلیارد تومان رسید. سقف این تسهیلات در تهران به ۳۶۵ میلیون تومان رسیده و تاکنون به ۳۸۴ هزار خانوار وام ودیعه پرداخت شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659808" target="_blank">📅 17:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659807">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/659807" target="_blank">📅 17:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659806">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU8axL0isyTZFFqEVSyT5tL316UZ7xM6CKmkMmX-AR_QNufyopzt2vIvxVWBO_QECmSqsmqoJO2pfcw_KdUgufCqLTiq9iGdhiVpOe001xSCliXeYmDV6BN3Qrr4Udqer1NZhyk6Mvw-ieaiIlhAQ0ABd4dVFWOxdo3MlNJZi4vmPSjtUAu16Gq-nQwU2qvNpfb4sWlcV0CCvTA1mFGi78agdcLVf-4by-VuaITS5IZVydKgUvFZkkR8hQx0AUggwWCRi37SRL6H7O83fXv8lvIfG4qcbGJWMSHtWtIOugYkczAX17wXkHU4OThTOe8XkP4WZ6Q5QDwbp8T1DqfwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه Haaretz: ایران به بقا قانع نیست و در پی تبدیل شدن به یک قدرت بزرگ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659806" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659805">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsuYIDh889BUh3vR9K-EL8sh7TeiaoS4-6BqaLAoij0GG2iyIstgCfkRe_RnHjLLCCGym7AoJ2w3hGDvoxyJJ4JwuTdUoXehy7Iq_8Z0KOhG0CacryYAYTgCfQQLS9nc0LiQlNdyIlixQ0t-Nrjd4M34DNKF6m1qNRtQNU5sSnjOzgdYcjZR7_amuqxrecQdHhqMG-BIn1OHWQVqibSNBy9rkWFU1_EpXsKrEnE4Oou-PD4B17_OVVV0lGoJzJIi2tL8hEUGinlJdcARokoUegf8RjayjnBqAzPFs0i8ZXy_areRYExnzaTCsxg31IZeMTz1AMvQxSOPi3-SsdvAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی تصمیم‌های مهم در تاریخ کشورها نه در میدان نبرد، بلکه در عرصه مسئولیت و تدبیر گرفته می‌شوند
محسن بیگلربیگی نوشت:
🔹
آیت‌الله سید مجتبی حسینی خامنه‌ای در مدت کوتاهی فقدان شماری از نزدیک‌ترین اعضای خانواده خود را تجربه کرد؛ رخدادهایی که برای هر انسانی می‌تواند با اندوه، خشم و احساسات عمیق همراه باشد. با این حال، مسئولیت‌های بزرگ گاهی انسان را در برابر انتخابی دشوار قرار می‌دهد؛ انتخاب میان احساسات شخصی و مصالح عمومی.
🔹
بزرگی رهبران را تنها نباید در تصمیم‌های سخت، بلکه در توانایی آنان برای ترجیح منافع ملی بر ملاحظات فردی جست‌وجو کرد. در چنین شرایطی، آنچه اهمیت می‌یابد حفظ امنیت، ثبات، رفاه مردم و آینده کشور است.
🔹
اگر توافقی با هدف تأمین منافع ملی، کاهش هزینه‌ها و آسیب‌های احتمالی برای مردم و گشودن مسیرهای جدید برای پیشرفت ایران پذیرفته شود، می‌توان آن را نشانه‌ای از تقدم مصالح کشور بر احساسات و ملاحظات شخصی دانست.
🔹
تاریخ نشان داده است که ماندگاری کشورها بیش از هر چیز در گرو تصمیم‌هایی است که با نگاه به آینده و منافع عمومی اتخاذ می‌شوند. شاید مهم‌ترین آزمون یک رهبر نیز همین باشد که در لحظات دشوار، آنچه را برای کشور مفیدتر است بر هر ملاحظه دیگری ترجیح دهد.
🔹
ایران امروز بیش از هر زمان دیگری به همدلی، عقلانیت، تلاش و نگاه رو به آینده نیاز دارد. پاسداشت یاد همه شهیدان این سرزمین نیز زمانی معنا می‌یابد که در مسیر ساختن ایرانی قوی‌تر، آباد و امن‌تر گام برداریم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659805" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659804">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس درباره ایران: ما دیروز به صورت دیجیتالی توافق را امضا کردیم
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659804" target="_blank">📅 17:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659803">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df0d20618.mp4?token=aSO7zwVfLFthgdry4i1N62fFSSK43h0QSnb7ZpW33RP1tGg3dZF7T8bBwcrXErz3bqm28WVbRBsRaMFm8VfM_payKG35o0xb1BPPUQdr8uiCHNxp-Wm3HszYrZD6IaXuri6I5ziIUqklzow8JlFnue_WgLRHx0Trmvl1aINZjcjTwIqzBmcYkomD6vZI8cWdbnoqFt_zQsCf3D_m-qZytXWDa5jOx4Fn7HBTV_9J7rL5zl2ES0kcwYMDYb6d1J6H-vQ45o3cZXYHC0HMkO9KpDNR7iBX6fRQSML_G0GJ4g4jj3taDx7or1s7NeNb4exduqUYtwwkphRmC0159xIA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df0d20618.mp4?token=aSO7zwVfLFthgdry4i1N62fFSSK43h0QSnb7ZpW33RP1tGg3dZF7T8bBwcrXErz3bqm28WVbRBsRaMFm8VfM_payKG35o0xb1BPPUQdr8uiCHNxp-Wm3HszYrZD6IaXuri6I5ziIUqklzow8JlFnue_WgLRHx0Trmvl1aINZjcjTwIqzBmcYkomD6vZI8cWdbnoqFt_zQsCf3D_m-qZytXWDa5jOx4Fn7HBTV_9J7rL5zl2ES0kcwYMDYb6d1J6H-vQ45o3cZXYHC0HMkO9KpDNR7iBX6fRQSML_G0GJ4g4jj3taDx7or1s7NeNb4exduqUYtwwkphRmC0159xIA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند طلایی برای آبیاری گیاهان
🔹
این روش یکی از بهترین راه‌ها برای زمانی است که ۳ تا ۷ روز در خانه نیستید، چون گیاه به اندازه نیازش آب مصرف می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659803" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659802">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf2518627.mp4?token=TGNWW8aOJ7zQlng_LW975m9sP9QR1qJCoCcaQbvZsVimzLXrSUdH813CFBIeNgB4IW_XWsgLmb2TATUx4ywayy4EZw57g2535AMhCHZyWIqCP_7LEo9LhCW8Q7TSAXRYM4DtWXLDkwVDt3f8N1gOM4SMwote6oOPsiFxpj8SQK2ZEYP545tvPJyGx8FuiDAjwkHvAH6HbZEEuzCG73ylCe76Ddh3FLuFBTXKK8Il2hDOZbft10tpsChznfRwXBn_EU0RwJ-hi8j_A26FVHP-kV7_lkwyJnBS1j_YVg0HMgFlEUDXCkSYTf4Zl6muxFHfkaml4LoA4XFrrNhQ_zimtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf2518627.mp4?token=TGNWW8aOJ7zQlng_LW975m9sP9QR1qJCoCcaQbvZsVimzLXrSUdH813CFBIeNgB4IW_XWsgLmb2TATUx4ywayy4EZw57g2535AMhCHZyWIqCP_7LEo9LhCW8Q7TSAXRYM4DtWXLDkwVDt3f8N1gOM4SMwote6oOPsiFxpj8SQK2ZEYP545tvPJyGx8FuiDAjwkHvAH6HbZEEuzCG73ylCe76Ddh3FLuFBTXKK8Il2hDOZbft10tpsChznfRwXBn_EU0RwJ-hi8j_A26FVHP-kV7_lkwyJnBS1j_YVg0HMgFlEUDXCkSYTf4Zl6muxFHfkaml4LoA4XFrrNhQ_zimtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد علی نژاد
:
رویکرد ما این است که در تهران زیرساخت‌های حمایت از شرکت‌های دانش‌بنیان نوپا را توسعه دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/659802" target="_blank">📅 17:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659801">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR902UCfqCXHF0eB_psQiWp6fQYMgws-rl3RTc-FFS4DBBZdlwdBqOCMnEM8mBaze7CNs-SeheVBjJ6wSCqQv7ZJhgny5ExcM8gZThQOh3YwfKEA_si06vTHvlKI115OqmWVmg9foazz82u855k731IdT4z0bpWuH2dgRnTXk0tyCUOaEExXIT46VQqzKjSwCMzmaRAJQhCtURQk7l6QC4C15TFkKv6wlIs5LMXCnRP9mFQ02pyBcuCAYjJh1JOetyZBdeDaXlTXcr8CUyO8QCU2X2k0xFKU0qy2yMseXTDllhmoIW_JrRQhwSqEMufrgEv4q-bfUsAn3quIcgYkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام معنادار نخست‌وزیر اسپانیا درباره جنگ ایران
🔹
پدرو سانچز، نخست وزیر اسپانیا، از مردم خواست که هزینه درگیری مسلحانه آمریکا با ایران را فراموش نکنند.
🔹
به گزارش Ukrinform، او نوشت که «بیش از ۷۴۰۰ کشته، که اکثر آنها غیرنظامی بودند. صدها خانه، مدرسه و بیمارستان ویران شد. افزایش گسترده قیمت‌ها و میلیاردها یورو خسارت، به ویژه در اروپا. اینها پیامدهای درگیری در ایران است.»
🔹
نباید فراموش کنیم که جنگ یک اشتباه است و گفتگو و دیپلماسی تنها راه ممکن هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659801" target="_blank">📅 17:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659800">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lii_OPmSrn3QzlaLiZ-2XTVmdNHQVRPS1tMcYt7E3T2Xjw17YG5w-irrEZBxjaF6w4xpyt3dUR1IOTvn51gWYrsc5o6GzqzfO_lNfg-1JJGgtRtPLH9iDkmg55EF-yLiQdENJABEEREXyhKdvlOS40KJxiwvEAX4RzNUztyzknRhtFHI0hLF_LytXyjQ_S8gr9AuxAUR6uWR_NPB-E9WwM31YgkgzuTEvNCacKXKdAgSjPvagg4f-c9C7eG3qdoqz8jUs8JmbZMjm2zab4NP7lfCNDI_8P_nEbRXzOYEtzQV0RlyNKVN81SZCElupfk-vcpaql1-nXiz1UEvYlw2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«من ایرانم»؛ نسخه «اوج» برای بازگشت مخاطب به تلویزیون
🔹
«من ایرانم» به جای ساخت تصویراسطوره ای و دست نیافتنی از فرماندهان و چهره‌های رسمی، پیش از آنکه با سمت و مسئولیتی دولتی شان از آنان یاد کنند، آن ها را به عنوان عضوی از یک خانواده به مخاطب شناساند با ترس‌ها، دلبستگی‌ها و انتخاب‌های دشواری که داشتند.
🔹
شهیدی‌فر نیز با همان شیوه آشنای خود، بی‌آنکه بخواهد ستاره برنامه باشد، اجازه داد روایت‌ها شنیده شوند. او به جای آنکه احساسات را هدایت کند، به مهمانان فرصت داد خودشان قصه‌شان را تعریف کنند و همین صداقت، مخاطب را با خود همراه کرد.
🔹
در این میان، نقش سازمان اوج که به تولید چنین برنامه‌هایی میدان می‌دهند نیز قابل انکار نیست؛ سرمایه‌گذاری بر روایت‌های انسانی و پرهیز از شعارزدگی، نشان می‌دهد که گاهی اثرگذاری رسانه نه از مسیر پرخرج‌ترین پروژه‌ها، بلکه از دل انتخاب درست سوژه و اعتماد به قصه‌های واقعی به دست می‌آید./ روزپلاس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659800" target="_blank">📅 17:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659799">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb22ee8c3d.mp4?token=YQthkX5ooRyfqCy43O7FIjJwx_0kgnMnDGuy9N_1EyJpTrrT9IYmPhSj0N_msn65-l4LQ8atfqKlgwMIq2JCFVurfR6kz1eSqBdD96UzpGvwZvfk6wPVyNdG1x-vzxTn7up5bA2vaJE526UijdMQK4FjgNbJL9LtV_nr_I2nmp3dm71-SYpBR_Awk8Atjs2BEZZyHj1I-U56Hmm5r0R0EbVCUhaIU-jb0UWDOzuqWH_6HiO0klQt4Kiqh0ObjD7V4YXcKLXZLrIZkONipOOyLmRFmv4SldJDccwfqQaWHLul0QJ0qKK4z0bAgTL_VvW8Na7gmgB7SnE6SB3nBlMrRjPK5r94d3DMEFAsj3nDz9DI4as0JOYh5UM2VBZrJ_DMMoLIV3gcr4tEBKmBTAx2XIV4HhVTgItNO1NArDKmXhrdK_CyWXsDEokJWqdNYQ9fa0AsdE_kYrGI9C9kBeOyOlkCUL3FuPbK-Ky-7J7_A5DQlrGxgMl-xePRxQ_4YohNNgbGnzY0_nmbMUrXYOUe5VYFxiru4udo-pg_tffNc-dtoQPJUipsn0p0ip8LpKO1u-e4XarEAbavQggValDpX6B6dF6f5i1VEr45PfYfGJXFY-zv-5FjYVE1BRnzcw14XoJwezwQwS_LXAFPOHXdAJkmmU2VZRT_l39eyzSteNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb22ee8c3d.mp4?token=YQthkX5ooRyfqCy43O7FIjJwx_0kgnMnDGuy9N_1EyJpTrrT9IYmPhSj0N_msn65-l4LQ8atfqKlgwMIq2JCFVurfR6kz1eSqBdD96UzpGvwZvfk6wPVyNdG1x-vzxTn7up5bA2vaJE526UijdMQK4FjgNbJL9LtV_nr_I2nmp3dm71-SYpBR_Awk8Atjs2BEZZyHj1I-U56Hmm5r0R0EbVCUhaIU-jb0UWDOzuqWH_6HiO0klQt4Kiqh0ObjD7V4YXcKLXZLrIZkONipOOyLmRFmv4SldJDccwfqQaWHLul0QJ0qKK4z0bAgTL_VvW8Na7gmgB7SnE6SB3nBlMrRjPK5r94d3DMEFAsj3nDz9DI4as0JOYh5UM2VBZrJ_DMMoLIV3gcr4tEBKmBTAx2XIV4HhVTgItNO1NArDKmXhrdK_CyWXsDEokJWqdNYQ9fa0AsdE_kYrGI9C9kBeOyOlkCUL3FuPbK-Ky-7J7_A5DQlrGxgMl-xePRxQ_4YohNNgbGnzY0_nmbMUrXYOUe5VYFxiru4udo-pg_tffNc-dtoQPJUipsn0p0ip8LpKO1u-e4XarEAbavQggValDpX6B6dF6f5i1VEr45PfYfGJXFY-zv-5FjYVE1BRnzcw14XoJwezwQwS_LXAFPOHXdAJkmmU2VZRT_l39eyzSteNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صفحه رسمی جام‌جهانی ۲۰۲۶ با انتشار ویدیوی مهار پنالتی رونالدو توسط بیرانوند به استقبال دیدار تیم ملی کشورمان با نیوزیلند رفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659799" target="_blank">📅 17:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659798">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=iP7hiVJgPZMabAXeIl3yPptBPJyJ4y3LkYhpebekJ_nwVzQHvELFQCHnCk0MdZ-zuc1IhtRbF4SWiac9DK1eFh7KNqbUonMBrZFjbwHr6RXptcM1U-zaI4yQm2lQTFBdtlctriTaDyUpc9iOZk81gR5YTtNXq3YiQMev50_ZP-KsnerSEA5p7AF4rv5mRN5V7_t88lfc4yXYVxUg53lIK51-H-0VZM3ycraI_jLOWak0jbeMdMdKM6MyF1wqME_hcsggzlzpcI8CFKNvHakcKA7bPhU4PdTdqOG0euehOcJc62-potv-ZQ-LKI_rR6yZ9n4E7J72f6ZnwykrX-IsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=iP7hiVJgPZMabAXeIl3yPptBPJyJ4y3LkYhpebekJ_nwVzQHvELFQCHnCk0MdZ-zuc1IhtRbF4SWiac9DK1eFh7KNqbUonMBrZFjbwHr6RXptcM1U-zaI4yQm2lQTFBdtlctriTaDyUpc9iOZk81gR5YTtNXq3YiQMev50_ZP-KsnerSEA5p7AF4rv5mRN5V7_t88lfc4yXYVxUg53lIK51-H-0VZM3ycraI_jLOWak0jbeMdMdKM6MyF1wqME_hcsggzlzpcI8CFKNvHakcKA7bPhU4PdTdqOG0euehOcJc62-potv-ZQ-LKI_rR6yZ9n4E7J72f6ZnwykrX-IsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماکرون: ناو فرانسه می‌تواند ظرف ۲ تا ۳ روز آینده در تنگهٔ هرمز مستقر شود؛ البته با هماهنگی
🔹
ما می‌توانیم از همین فردا یک ناو محافظ و ظرف ۲ تا ۳ روز آینده، ناو شارل دوگل، تجهیزات مین‌روبی و ناوهای محافظ شرکایمان و سایر تجهیزات را در منطقه داشته باشیم. اما تمام این اقدامات تنها در صورتی معنا خواهد داشت که یک توافق بین‌المللی وجود داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659798" target="_blank">📅 17:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659797">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgUqm1iJoPjFhuwJlg5mZixokpEGhBzNwX41VegoupNr1r6vCWmAvXhPNMKbGb3F2OBUPidpdj20wQzf6RhyIkYSTyFvyHywEnQW3n3QZU9663bIGvRAFGJFQn3A8z5uCnH8B9icWMa2fK-PS_buY9BGrmvyu7vqhJdvOmtyLpoMx33CN__i1h0mjgpRMm6LlS_hyXispbH04UNhNeHk8rQifferO61QScYfbpRX94kRhZOnhM-LYSuWJpjHMfIAwkN90UL71Yo2QemjX_xy0HYt26viEz69Nnf5mH3pPD5Ab2WzLi-u4uZ7CTorXKQ83CfqW-nFSmlWY8VpBGXP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفوگرافیک/ روایت نقش‌آفرینی بانک صنعت و معدن در توسعه زیرساخت‌های انرژی
🔹
۴۱ طرح نیروگاهی، ۸ هزار مگاوات ظرفیت و سهم ۱۰ درصدی در تولید برق کشور
🔹
بانک صنعت و معدن با ایفای نقشی مؤثر در تأمین مالی پروژه‌های نیروگاهی کشور، از اجرای ۴۱ طرح در حوزه تولید برق حمایت کرده است؛ طرح‌هایی که با ظرفیت ۸ هزار مگاوات، سهمی ۱۰ درصدی در برق تولیدی کشور داشته و گامی مهم در تقویت امنیت انرژی و توسعه زیرساخت‌های صنعت برق به شمار می‌روند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659797" target="_blank">📅 16:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659796">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
بحرین برای ۱۲ طرفدار ایران ۱۰ سال حبس برید!
🔹
بحرین ۱۲ نفر را به دلیل حمایت از حملات ایران به ۱۰ سال زندان محکوم کرد
🔹
آناتولی گزارش داد که دادگاه عالی جنایی می‌گوید افراد «مرتکب جرایم حمایت، تشویق و تأیید حملات ایران» در بحرین شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659796" target="_blank">📅 16:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659795">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda12651f0.mp4?token=CrKz5tI3zyGRpqXAE5rvKGMbXNb2twuvy72rnMF3-6G0e0vonVv_NiHDLvtsFBtZcMbAZUhFIqPfJa9TWgx9DcZCc0zWETS1Tl1hV2x5RydaR8WQ5B3TCzKX-9GyhM_yuuGqQGXqAn2OVstt_EqDLE8c6MGma0MXlqhqsyrbNvZ6rV2q4Ys448tuiy6qd28-RSntC_a9_dobmPQrKQrutdGpFfXVDnqBPYL9F984HpetO1PKbHDPzInS9jvSVk1bQHWUNJ9DzAoqq0dGCFqGbBEfQHku92yAQ-GX5SfpDRZKP4EB9xyK5rFsIRsFg1PwmXLNwxz87W6NatN_EZ6qCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda12651f0.mp4?token=CrKz5tI3zyGRpqXAE5rvKGMbXNb2twuvy72rnMF3-6G0e0vonVv_NiHDLvtsFBtZcMbAZUhFIqPfJa9TWgx9DcZCc0zWETS1Tl1hV2x5RydaR8WQ5B3TCzKX-9GyhM_yuuGqQGXqAn2OVstt_EqDLE8c6MGma0MXlqhqsyrbNvZ6rV2q4Ys448tuiy6qd28-RSntC_a9_dobmPQrKQrutdGpFfXVDnqBPYL9F984HpetO1PKbHDPzInS9jvSVk1bQHWUNJ9DzAoqq0dGCFqGbBEfQHku92yAQ-GX5SfpDRZKP4EB9xyK5rFsIRsFg1PwmXLNwxz87W6NatN_EZ6qCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای نخستین‌بار/ آخرین مصاحبه فرمانده شهید گروه موشکی ۱۵ خرداد
🔹
شما آخرین مصاحبه فرمانده شهید «عبدالحمید رهبر» فرمانده گروه موشکی ۱۵ خرداد نیروی زمینی سپاه پاسداران انقلاب اسلامی ایران را می‌بینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659795" target="_blank">📅 16:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659794">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
لاپید، نخست‌وزیر اسبق رژیم صهیونیستی: نتانیاهو در آزمون لحظهٔ سرنوشت‌ساز فروپاشید
🔹
اسرائیل شکست سیاسی شدیدتر از شکستی که او در قبال پروندهٔ ایران ثبت کرد، به خود ندیده است. زمان آن رسیده که اعتراف کنیم او دیگر قادر به انجام وظایفش نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659794" target="_blank">📅 16:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659793">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
کانال ۱۳ رژیم صهیونیستی به نقل از یک مقام ارشد اسرائیلی: این توافقی شوکه‌کننده برای اسرائیل است، هیچ کسی در رأس قدرت نیست که چنین فکر نکند، از نخست‌وزیر گرفته تا رئیس ستاد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659793" target="_blank">📅 16:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659792">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8b3ddeae.mp4?token=EMekqrY7C6n8683Inrsuc9NAI1hn60mkX92qR8omxHIygnXSjZHN23uY3U0_hIQ5XvQ-DmCGi0xhCtWzKlNd0T-LOBYiXyXhQDcTBRhtc00VX-4-wHyuzVuCiKq8av5SfxJHbzi_oYVsuK0SXMDFi0oq8VG5fOHBEg0aPm9J13RekS9xOoFbSEiXp6aJiDv8AgbVIumbkn-XSEaLkLxtvoQm-fWoAWbicG0n4WjySKCxL0j48-R2EbJ7J_ZdG1_tuKX6DnMMrWHBll_3bk3UMTqigcnYgmUjpXuEgArDG-m92j2Bpa57YnxJ_TegIMmSVQM3om81rOgY-tpHHrpFDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8b3ddeae.mp4?token=EMekqrY7C6n8683Inrsuc9NAI1hn60mkX92qR8omxHIygnXSjZHN23uY3U0_hIQ5XvQ-DmCGi0xhCtWzKlNd0T-LOBYiXyXhQDcTBRhtc00VX-4-wHyuzVuCiKq8av5SfxJHbzi_oYVsuK0SXMDFi0oq8VG5fOHBEg0aPm9J13RekS9xOoFbSEiXp6aJiDv8AgbVIumbkn-XSEaLkLxtvoQm-fWoAWbicG0n4WjySKCxL0j48-R2EbJ7J_ZdG1_tuKX6DnMMrWHBll_3bk3UMTqigcnYgmUjpXuEgArDG-m92j2Bpa57YnxJ_TegIMmSVQM3om81rOgY-tpHHrpFDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ورود رهبر شهید به مراسم محرم سال گذشته؛ لحظه‌ای که دیگر تکرار نخواهد شد...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659792" target="_blank">📅 16:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659791">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8IkodRj2fRktCM2xIoQZIbgzHf0lQItPmckLqcpnZ2_AYKj9ay0aHkb9qwGBfeUvojx3xx9eG6okzbNksjSxUgw8wQ7XHbHA_n54xczCaeWClwjbCuBAu3Iml-JVhvKAPMtMWKy60KLpzEsMulb5vBypzJ7pFBwxQ_ER6OJonPMLgtDhFyQwGCOssP3iCdAcE3s7QVTaxYRFXHkijdou4AA3j3obc5gEJSpfQUHXtEIKBXvBhucYB55HjzycmL5J8W6pIadOLKLX9P1-qAKmVcqiMTuBElOvC2lHJgRRzuKl7aIXD8SsOveTUq7NDxXSMNVdSu8JoqE_ZP1bv0_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: ملت ایران با تأسی به مکتب حسینی توانست در جنگ تحمیلی سوم متجاوزین را به شکست و هزیمت بکشاند
🔹
اگر در دیپلماسی، عزتمندانه و انقلابی ظاهر شدیم، چون درس‌آموز مکتب عزت حسینیم؛ حسین (ع) همه وجود ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659791" target="_blank">📅 16:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659790">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
رژیم صهیونیستی چند ساختمان را در شهرک عیتا الجبل را منفجر کرد
🔹
منابع لبنانی خبر دادند که ارتش اسرائیل با بمب‌گذاری در چندین ساختمان در شهرک عیتا الجبل، آن را با خاک یکسان کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/659790" target="_blank">📅 16:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659789">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJLnEu79vvoEsM4myciH_6iIn56P09Z18sxPsAKjn5jXOuznLjBao-Sk-dqattr8yQ7lxUzkPgrw12ONUtGKR9pvOqT3f94qHLx0jTeOZbB59Wpfk641y9Ja05FPJIrA3W1BUhoGvvrZwUMEmHod84qG9w0A3ZWVzmTBDwCPe3c4fODzkTvvwg0njsAeIpXOU-HPS9qHnpfzKyw9jmnon5VD2vv2WaBxye74hsk-vy3Kmxowm6dtpBpub_plwFM9SXwXxeLXdpIOKqahyrxBPGmmiRr47m_fZ4cPnJBgvjmywmzVnSwpm_6_eA2gCdX9NhLWP3u8ovtmMjsHWAhj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: کشتی‌ها شروع به حرکت کرده‌اند، بسیاری از آنها با نفت بارگیری شده‌اند، از تنگه هرمز خارج می‌شوند
🔹
آنها در امتداد «بزرگراه» جنوبی حرکت می‌کنند که کاملاً ایمن، مطمئن و بکر است. مناطق دیگری برای سفر نیز وجود دارد!!!
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659789" target="_blank">📅 16:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659788">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTqOFVavfHjswvCXPkZhRu0XaKdJa-x80r_YYB6dhDuZXN7aLVehB5auh-A55CFK-su5lERbmjLWh1XiNySC8KI_GkQY3_GsTuU7hdzGLIv-6prqBjEUD1SvQVfGLnjWyKS_RNVqSpHmlhEWLOgniI6k7qVfxX8ZYnuoj0pD_P1_cLo3-Gcb3DsVniIW2sP767ii_3YOs6MvrjhxROIbmkZ8WtaOX4q1817qwg4WSNgKhvGQvDO3AfrgcCTDUSuOz0iPEMo6QMdH7lTQ3lrbTDU63WD3oaEaLmPXhsPtweRiYxAcUhLsONCa5HeM2AsszGBdpMJUbo8aEojUJu3QDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون پزشکیان: ایران از جنگ با دو قدرت اتمی پیروز بیرون آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659788" target="_blank">📅 16:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659787">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce210dcf0.mp4?token=rzq56C0jXJN8YSjmPoxEZeIn4C_mMl4AJty-2KFjASDOC5qkmcP3FfIfxbfWY6oyUBawELZoPiIdbPFkQY7EIgb9fYGFEqmFgRhejf4pZ6oMhO9IjB93CzmhTrnwGdy3RcVaZrXVZlIPhzvAThAM6sOSE3ejvf7Ja5Bl_eIGkBq-pCCt78CpoUPiWIlPfIDLGvM03mXt8w59PEA67DenkDJMBJfZ2uJrWFHIdRwekVeDUCk6VNTwPotybfBK6DiZgZtiNOUmEsOerNxK-g8Tf8bUTLsJeUHpIfcKuR2F7ILw5jFIBXRqv41Gnz_bI15IY31FnDy-Nk-rlLEtgzmkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce210dcf0.mp4?token=rzq56C0jXJN8YSjmPoxEZeIn4C_mMl4AJty-2KFjASDOC5qkmcP3FfIfxbfWY6oyUBawELZoPiIdbPFkQY7EIgb9fYGFEqmFgRhejf4pZ6oMhO9IjB93CzmhTrnwGdy3RcVaZrXVZlIPhzvAThAM6sOSE3ejvf7Ja5Bl_eIGkBq-pCCt78CpoUPiWIlPfIDLGvM03mXt8w59PEA67DenkDJMBJfZ2uJrWFHIdRwekVeDUCk6VNTwPotybfBK6DiZgZtiNOUmEsOerNxK-g8Tf8bUTLsJeUHpIfcKuR2F7ILw5jFIBXRqv41Gnz_bI15IY31FnDy-Nk-rlLEtgzmkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: ما اساساً همه کارت‌ها را در اختیار داریم
🔹
اگر ایرانی‌ها تعهدی ندهند، ما مجبور نیستیم چیزی به آن‌ها بدهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659787" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659786">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10548b8f4.mp4?token=XqBj_RMwK-BjicoeY-CvL8HSD0n0qhpU63YuUtW2pNetOPpzu5KhcItaCJAeL5HOj7sXVyNnLc9h5I0D83ewYqzaa0FhU7nb0e0fAbziId8cJ8pck-JXHkHQO2pCTBAMgE3lAnPnAX5bzllGQeVgFUml-JTVpzrGj8e1uBHsU8w4dS7S8jrdCzxn5T7tZ5aFm33bBGH4M2_D_j0wdl-NjdUoIGPbvXPAl2h2u7kGqQqrFbfB6Waw6Mima5yy2li3t0YKe5QV7V-e8E5Gg4Es21wzsNLjWmvjnADSn4SeCbUf6V9TdpjCCXrKy-zQA1DXESMymX83R3Uf1gc1Zo7s8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10548b8f4.mp4?token=XqBj_RMwK-BjicoeY-CvL8HSD0n0qhpU63YuUtW2pNetOPpzu5KhcItaCJAeL5HOj7sXVyNnLc9h5I0D83ewYqzaa0FhU7nb0e0fAbziId8cJ8pck-JXHkHQO2pCTBAMgE3lAnPnAX5bzllGQeVgFUml-JTVpzrGj8e1uBHsU8w4dS7S8jrdCzxn5T7tZ5aFm33bBGH4M2_D_j0wdl-NjdUoIGPbvXPAl2h2u7kGqQqrFbfB6Waw6Mima5yy2li3t0YKe5QV7V-e8E5Gg4Es21wzsNLjWmvjnADSn4SeCbUf6V9TdpjCCXrKy-zQA1DXESMymX83R3Uf1gc1Zo7s8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: ما دست دوستی به سوی ایران دراز کرده‌ایم. اگر آن‌ها بخواهند رابطه‌شان با ما را تغییر دهند، ما نیز رابطه‌مان با ایران را تغییر خواهیم داد/ این پیشنهاد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659786" target="_blank">📅 16:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659785">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgpiOOYh0zP4J5EN788jLuhvhMJfr5o6e2NIkoiuhiq1Iwi-OdYswFcEOwwEVkzXloNl-eezoFrOVqNDQqxcxPQmW6ypr9w2SzbvTimdizYvOoC6kdoUTzl4f2ca6A4RZWdBNRgjtAsXCIxXHzWIYjf81v9ONmIAawcxjc8BUkZI0cojT-S8mWjeiLpGcztIoFY6ghVbxkFpj63KMi-2LbMmS28DSe42hx1Dls-54c09FD8PDP-r86fPtJVeUY55KmjlZex3ry5z7mxGdDp1YZTAtTkYqF1s-j_lx34hmUOoePzh9ODVZbyypYf4fJ6nxmJ6Lq_holbycYNYqXbizw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر صفحه رسمی جام‌جهانی برای دیدار ایران و نیوزیلند
🔹
این بازی فردا ساعت ۰۴:۳۰ بامداد به وقت تهران برگزار خواهد شد. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659785" target="_blank">📅 16:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659784">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e51b0e9f7.mp4?token=acDl-V4Kw5zRapqQ77zPtLWA9bQoBgvZdcZcpSNLhEa8tUOEOTIs2ISF_6ND49fe5j23ac-AliEy7gIbw_Qg_2ghdsWO4WMmTn3e39__iOHpiiXhsT72NX08RvdLQk0HHH0JCBXCoDQmYS-3wa_TH--m-0Zc5AqY2U9r7A9wu4UxlxNhDael1gGY7HhKOhqw5XKdThm6aInJL6YsRZJRF-6o0j-S_iSemHDIYXv04QBO8XW-50tkarFG2Aw2M7KvYHkTOqPhOnTQ4QwBsxeG66wPWO_5OWuLQwyUpUrjBNJRr65x-SHnrqfHySZcr6KnAbfM6oSdpH1ptrGkFdguyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e51b0e9f7.mp4?token=acDl-V4Kw5zRapqQ77zPtLWA9bQoBgvZdcZcpSNLhEa8tUOEOTIs2ISF_6ND49fe5j23ac-AliEy7gIbw_Qg_2ghdsWO4WMmTn3e39__iOHpiiXhsT72NX08RvdLQk0HHH0JCBXCoDQmYS-3wa_TH--m-0Zc5AqY2U9r7A9wu4UxlxNhDael1gGY7HhKOhqw5XKdThm6aInJL6YsRZJRF-6o0j-S_iSemHDIYXv04QBO8XW-50tkarFG2Aw2M7KvYHkTOqPhOnTQ4QwBsxeG66wPWO_5OWuLQwyUpUrjBNJRr65x-SHnrqfHySZcr6KnAbfM6oSdpH1ptrGkFdguyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایۀ بقائی به حواشی امنیتی پیرامون کمپ تیم‌های ملی مختلف در آمریکا
🔹
خوشبختانه کمپ ایران در مکزیک است نه آمریکا؛ از مکزیک بابت میزبانی خوبش تشکر می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659784" target="_blank">📅 16:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659783">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خسارت ۱۷ میلیارد دلاری آلودگی هوا به اقتصاد ایران
شینا انصاری، معاون رییس‌جمهور و رییس‌ سازمان حفاظت محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
آلودگی هوا از طریق تحریک بیماری‌های زمینه‌ای، منجر به فوت افراد می‌شود.
سهم هر یک از بیماری‌ها در مرگ‌های منتسب به آلودگی به شرح زیر است:
🔹
بیماری‌های ایسکمیک قلبی ۲۳ درصد، سرطان ریه ۲۱ درصد، بیماری‌های انسداد مزمن ریوی ۱۷ درصد، سکته مغزی ۱۵ درصد، عفونت‌های دستگاه تنفسی تحتانی ۱۳ درصد.
🔹
مبلغ دلاری آن بر اساس گزارش وزارت بهداشت، معادل ۱۷.۲ میلیارد دلار در سال است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659783" target="_blank">📅 16:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659782">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
بغض سخنگوی وزارت امورخارجه هنگام پاسخ به سوالی درباره مراسم تشییع رهبر انقلاب   بقایی:
🔹
هیچ وقت فکر نمی کردم در نشست خبری درباره مراسم تشییع پیکر رهبر انقلاب صحبت کنم.
🔹
وزارت امور خارجه پذیرش مهمانان و صدور روادید و گروه های رسانه ای بر عهده خواهند داشت.…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659782" target="_blank">📅 16:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659781">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ونس: امیدواریم متن توافق با ایران این هفته منتشر شود/ خواهیم دید که آیا تهران حاضر به امتیازدهی است یا خیر
ادعای ونس، معاون رئیس‌جمهور آمریکا در مصاحبه با سی‌ان‌بی‌سی:
🔹
ما انتظار داریم که رئیس مجلس، وزیر امور خارجه و دیگران، نمایندگانی از ایران را در مراسم امضای توافق‌نامه حضور داشته باشند
🔹
روند راستی‌آزمایی دو مرحله‌ای در مورد ایران وجود خواهد داشت. ما انتظار داریم تنگه هرمز برای مدت طولانی باز و بدون عوارض باقی بماند.
🔹
هنوز جزئیات زیادی در مورد این توافق وجود دارد که نیاز به توضیح دارد. فکر می‌کنم کسانی در اسرائیل هستند که این توافق را می‌پذیرند
🔹
تعهد بلندمدتی وجود دارد تا اطمینان حاصل شود که ایران هرگز سلاح هسته‌ای تولید یا به آن دست نمی‌یابد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659781" target="_blank">📅 16:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659780">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رئیس‌ پلیس راهور: صدور گواهینامه موتورسیکلت بانوان، منتظر ابلاغیه قانونی است و بنظر در شرف اجرا و ابلاغ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659780" target="_blank">📅 16:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659779">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX8SI3CYAQy3pp3kGHTaQ3RSh1mw99LDqx2x147j7_3zlAghfUgX6HjekhMG1XjVhLwbJNalpqRqIYZr2yvPPeIP3v6GLdME6j-anSyJMoUmDcZa97LWSm0OpzV8_n6mRteR0h1wT5wMzubOwTVb8unazJXMlxz43UwbTWj3gRfSRUdvKM1ZxhVd8VqZ2-2BG1jPHiey07YFDGdVUB1FJMNNK6iXFR1YRVCAUTawTz_RCby9EKZVrWmcMUmJf2bLE3uoQdrDyuIw6qwpbuSqRFeOh5qrXV0InvK0Rcyh32ztaDAg3Ytuu5wzCSwABSSF7DAuCgWaNwn4_q_J2kUzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659779" target="_blank">📅 16:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659778">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f3aeb6fc.mp4?token=J7Sp2XR07xpFz3ESeYSIGuUP1ZReVfWjtxFraue3QDV5ZGQbRtZtRGHER_kkA-Dta1QqYOznPiVt0FiaE-hMJgVh-nGQxe8EYyCdT2iwrriZIXDjQloO8bvtq0PmHRnUD_6nDPOPWkQB58soDhmn4hz9ehvyLNSR9KgzD1YMIIJVfS9jCR8Yd-sk9trQBjnr7Tj_akEOBukXJfyB_fuw-LyeRE8eF1ZRFMqCSz8EpNEGrJN-74npYDmeqHqJw-e9oKPjnvsS4ioXbI3AJlCBWMt56vLm9C6kLN2c0bTW3ZQNB6IvxSYYN3SnQ0xqri-p6PlgAMsmyC_tYUZkUMYyoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f3aeb6fc.mp4?token=J7Sp2XR07xpFz3ESeYSIGuUP1ZReVfWjtxFraue3QDV5ZGQbRtZtRGHER_kkA-Dta1QqYOznPiVt0FiaE-hMJgVh-nGQxe8EYyCdT2iwrriZIXDjQloO8bvtq0PmHRnUD_6nDPOPWkQB58soDhmn4hz9ehvyLNSR9KgzD1YMIIJVfS9jCR8Yd-sk9trQBjnr7Tj_akEOBukXJfyB_fuw-LyeRE8eF1ZRFMqCSz8EpNEGrJN-74npYDmeqHqJw-e9oKPjnvsS4ioXbI3AJlCBWMt56vLm9C6kLN2c0bTW3ZQNB6IvxSYYN3SnQ0xqri-p6PlgAMsmyC_tYUZkUMYyoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بغض سخنگوی وزارت امورخارجه هنگام پاسخ به سوالی درباره مراسم تشییع رهبر انقلاب
بقایی:
🔹
هیچ وقت فکر نمی کردم در نشست خبری درباره مراسم تشییع پیکر رهبر انقلاب صحبت کنم.
🔹
وزارت امور خارجه پذیرش مهمانان و صدور روادید و گروه های رسانه ای بر عهده خواهند داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659778" target="_blank">📅 16:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659777">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
وضعیت نیروهای آمریکایی در منطقه طبق تفاهمنامه ایران و آمریکا چه می‌شود؟
یک منبع آگاه:
🔹
بر اساس ماده ۴ تفاهمنامه، ۳۰ روز پس از توافق نهایی، نیروهای رزمی آمریکایی باید از محیط پیرامونی ایران خارج شوند.
🔹
همچنین بر اساس بند ۹ تفاهمنامه، در طول ۶۰ روز مذاکرات برای توافق نهایی، نیروی جدید آمریکا در منطقه اضافه نمی‌شود و ایران نیز در این بازه اقدام هسته‌ای انجام نمی‌دهد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659777" target="_blank">📅 16:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659776">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حزب‌الله توافق ایران با امریکا را تبریک گفت
🔹
حزب الله لبنان در بیانیه ای، توافق ایران با امریکا بر سر یادداشت تفاهمی شامل آتش بس در همه جبهه ها از جمله در لبنان را تبریک گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659776" target="_blank">📅 15:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659775">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDoIIMHkLWxrbdIZfU6-cxxc5oZui4s_JkEt6gv28dx-Se9R_Eq7pq7UYPf0qHOr1DEKV87pLvtp-pT_Y3cCvPsjv3LacmLNx3vYVUSYlQExY5nvd4oGPzRZnr61edha2Q0ijl5Tw-My8rt_cXxTXC0SAS11cDZgRlo6ugCrO2NbAvMQ0em39c9gtWjQ-JqXRyt84DDZdjAOU-W9NY-uCbrK_XRu8P8dgtj7TeGQsIQ1Ul_8Nq7u9XkG0mzeEMfQq2V5OSz5VxYNu9hIoiaM5DtRM4NciO8YUkW4yLw1azuycAL-4gxHuAuIC19lj4Rsbf-IED2gwsjtd16ryW2Pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر صفحه رسمی جام‌جهانی برای دیدار ایران و نیوزیلند
🔹
این بازی فردا ساعت ۰۴:۳۰ بامداد به وقت تهران برگزار خواهد شد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659775" target="_blank">📅 15:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659774">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9122e82f3.mp4?token=Ab2sOd_Nu0en5CsZl4k62ATket_p2vkLoflJIVrO8aiw9v9mDvFCIblf8zYqBJiJFz3aTLVdFoxkT1cPt4d0a4WRIFq3EMHmbocx5i688bS2TVNgM4B2O3SHcO1s4eJ7-Oh-2nXvhbbISite1tIKwa1Ul3ogfkBV0O-u5S-U3YTKVobWTLfwywSDrbcBK9D5ltCY09WZlySBI7F5gI2fxTeeZix6nOzrIwNDMRDT3tMqYGqg4MsOjL-2i8_zYL8LMUeFuNcoDkk9x_oNFwkZLTUNFVk78PTFz-G1XVTqjaaJebt0uPp-EHoplEn052r5_6BL3BPDn0uuf35_DjyOLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9122e82f3.mp4?token=Ab2sOd_Nu0en5CsZl4k62ATket_p2vkLoflJIVrO8aiw9v9mDvFCIblf8zYqBJiJFz3aTLVdFoxkT1cPt4d0a4WRIFq3EMHmbocx5i688bS2TVNgM4B2O3SHcO1s4eJ7-Oh-2nXvhbbISite1tIKwa1Ul3ogfkBV0O-u5S-U3YTKVobWTLfwywSDrbcBK9D5ltCY09WZlySBI7F5gI2fxTeeZix6nOzrIwNDMRDT3tMqYGqg4MsOjL-2i8_zYL8LMUeFuNcoDkk9x_oNFwkZLTUNFVk78PTFz-G1XVTqjaaJebt0uPp-EHoplEn052r5_6BL3BPDn0uuf35_DjyOLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: به ازای خدمات ناوبردی و بیمه در تنگۀ هرمز هزینه‌های لازم طراحی و دریافت خواهد شد
🔹
برای مدت زمان مشخص قرار است متناظر با اقدامات طرف مقابل تردد ایمن در تنگه هرمز را مدیریت بکنیم.
🔹
این موضوع به عهده دولت جمهوری اسلامی ایران به عنوان دولت ساحلی گذاشته شده است.
🔹
ما به‌دنبال گرفتن عوارض نیستیم اما برای خدمات ناوبردی، بیمه و حفاظت از محیط زیست و ... هزینه‌هایی طراحی و دریافت خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659774" target="_blank">📅 15:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659773">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f406b6a53b.mp4?token=Q4anjXiA5zGKpA8EwHfmucpUvHxqW7I_B-smv26A1aSz5AVlEN5CmZpdqeGSN9Xwafa_-mn9z6NaYrIMoLY8CrqTjLBQ8CZBhRwE9dtLJi-H7lSvI6M7YGUP4txVTWf1vELhG8VtVgFFxTz0wOmZipMcV9OdfcE7rxjV3ODtPM4uh8oEqfMMUWXMg6pZU-P4ox5mx8tVnd1sPGDUP0K7NBNUUpJ6bIlROnHLxVYXlNGzO2VGX6GEBZOzRiIKM2gpAkBdiWXk6jv94_P4CGmP-fidGYFKwFDmALPBMONAreipKu32ESRXKjl17SIVBN-SL6kA8AUSpF06hUgtLt9mlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f406b6a53b.mp4?token=Q4anjXiA5zGKpA8EwHfmucpUvHxqW7I_B-smv26A1aSz5AVlEN5CmZpdqeGSN9Xwafa_-mn9z6NaYrIMoLY8CrqTjLBQ8CZBhRwE9dtLJi-H7lSvI6M7YGUP4txVTWf1vELhG8VtVgFFxTz0wOmZipMcV9OdfcE7rxjV3ODtPM4uh8oEqfMMUWXMg6pZU-P4ox5mx8tVnd1sPGDUP0K7NBNUUpJ6bIlROnHLxVYXlNGzO2VGX6GEBZOzRiIKM2gpAkBdiWXk6jv94_P4CGmP-fidGYFKwFDmALPBMONAreipKu32ESRXKjl17SIVBN-SL6kA8AUSpF06hUgtLt9mlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روند امضا توافق در سوئیس به چه نحو است؟
بقائی:
🔹
ایران برنامه‌ریزی کرده است تا در روز امضای رسمی توافق‌نامه، هم‌زمان متن کامل این سند و گزاره‌برگ توضیحی آن را منتشر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659773" target="_blank">📅 15:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659770">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1mfE4ktGFh1PeTHpmB7m3480rwLUepddqz7we5AHMdlMXlLuLQr8-pTba04dImEA-N6Cwp5C1MgRKGCSmd9ZCHLk0pV7o8SFh14qiCRRF62-pC-VGCkc0u5vfj34WD8evIa68x6YTqLGlVT4a-DR_bKWQzRDSEDB8QuA1VXopO5-y292Caa0lerbLNY9_Z5ZhEXhbfF7yJmXg1h4SfTn_GYTEyjgm4vJpJvaKalMpJT3oFHDvtwXoFSg2cdjN6Jz5_TlRQ1o2LFHPZJ3evYd9x8hj7hByxZZhquM5hQOnyuzt3H-vBZYDperTfh1RXbhSh9Qz8SRbjqLvRFj703sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ac71e6ada.mp4?token=KRLdXlqDnR7Qff1arHheGxsros64S3BCPgxGbnjv5wttCg1bJv2oXoHnyt3cUMgoqpIgBSAdjjxlERIx2eltp4R2URds2DEf2PO4oJvwmrnkE0WUY9KuZ4vzAPLWbWLfGB7Gada4F6mlTqnK-AqEaUefaBdHk-OpaNyMKrX5Ot_Gk90od6YcISqMnWdNjDOmKs8BLHPtxMgmmuNHhUH-jU71iJ6Ym2g98XDDYcUlGf0PemJXl7ny5pu5GDcY06IxLV1wlIQlEdcWCRTDFwmnTiwbe3nquLalPHqvVAM-kNkAeaC2IndhnZyjv-Mvzb28038zYFkgleNFzrCUA4PjtY9VAWuPHAK0m9kEfpnyVyuYkaZWyxQjwL64wOeusjtHIvOQ5J_88JC8UYbzK92v2QUu3SCEH9A5rlOvIS_9GR0V4lZscQoUM47vPt4KQ96lQqqWdyKI6efzuv1ffHzc0J_wWtJV-82dFXIRq29UqdLa2cbIHvkVOmYwOOiT2sRWcd9BlDZgtUe4auuQqublDvrby-e5GROCOqd2azQsys29fVur_6qbxeRw464k2oD8WFjOV-Cr8fLq9wG_Fnp5Gy4-0oFjVG2aonAcrpOtQ1SzU_rVhnirRMY1i8mT5JViJcrLwl1bTAivmJ-wTOqCTVEelerHPX3dI51eecor5A8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ac71e6ada.mp4?token=KRLdXlqDnR7Qff1arHheGxsros64S3BCPgxGbnjv5wttCg1bJv2oXoHnyt3cUMgoqpIgBSAdjjxlERIx2eltp4R2URds2DEf2PO4oJvwmrnkE0WUY9KuZ4vzAPLWbWLfGB7Gada4F6mlTqnK-AqEaUefaBdHk-OpaNyMKrX5Ot_Gk90od6YcISqMnWdNjDOmKs8BLHPtxMgmmuNHhUH-jU71iJ6Ym2g98XDDYcUlGf0PemJXl7ny5pu5GDcY06IxLV1wlIQlEdcWCRTDFwmnTiwbe3nquLalPHqvVAM-kNkAeaC2IndhnZyjv-Mvzb28038zYFkgleNFzrCUA4PjtY9VAWuPHAK0m9kEfpnyVyuYkaZWyxQjwL64wOeusjtHIvOQ5J_88JC8UYbzK92v2QUu3SCEH9A5rlOvIS_9GR0V4lZscQoUM47vPt4KQ96lQqqWdyKI6efzuv1ffHzc0J_wWtJV-82dFXIRq29UqdLa2cbIHvkVOmYwOOiT2sRWcd9BlDZgtUe4auuQqublDvrby-e5GROCOqd2azQsys29fVur_6qbxeRw464k2oD8WFjOV-Cr8fLq9wG_Fnp5Gy4-0oFjVG2aonAcrpOtQ1SzU_rVhnirRMY1i8mT5JViJcrLwl1bTAivmJ-wTOqCTVEelerHPX3dI51eecor5A8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم تجمعات حمایتی از کودکان میناب در قلب آلمان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659770" target="_blank">📅 15:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659769">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5413aeffb.mp4?token=MQ_DLNp_y7TqQL4nxkcC2FIVAdYFJQjdhkTq22m_ZiwmN2wvBdYYVyM8Bk-XUXj61l1LMhNG9bD6PnJ6EMxKjSGks75g-9a7IkCaltcRteX-6g-S0XzV8Ebs_u8qSY_pkzCxNieFR4HvTuV4dTGC6vu01hT4hhqb3sGMYwi9GR6mMrUnyehvm5OjZaeNevT3Z7SzoT66kSsv4PnOZeEsyK3j13fSnWAo9nAtiCjvHoFrlkxrI6Iw7_M4n0O2AxRPaopkXhy3u-pR4UfExhvZIQk9SyjNDDsD-ZIyRMI-IMWiYml16ljSCNYqHLs8kDilz6EhA1aHCczXwrq70f-h6DKk3lI5Fh1k9CZD2P-SIWlKEXeO5oKP6ZX7CQ3R91bB96yhjOwuOHwyg2ecnb8Yzy8T-mj9qdUDOOnVayq732IAocqA8rxpscce2UrChU_LdKHwLnCCGMP4KMcaJqAtT9-BTdl6mlpzDuAwKvjQXXD7PabnUtmsqWu0mVx52lk6-_UxEJBVg_7PBSgg3J_tOFg_sSsxtR2LhHnPNhOGm1djTSzVTTzyhTnJ4grLoF4PV5UHPib6vpmBRDM_f5n9sMG-CJYqRr8bHn19sc7MpnaC3RB5DRbHffQluRncKf71vicc8-3-bKdd_SScZBp69H1G--x-LjOb-Snu-jQV_fI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5413aeffb.mp4?token=MQ_DLNp_y7TqQL4nxkcC2FIVAdYFJQjdhkTq22m_ZiwmN2wvBdYYVyM8Bk-XUXj61l1LMhNG9bD6PnJ6EMxKjSGks75g-9a7IkCaltcRteX-6g-S0XzV8Ebs_u8qSY_pkzCxNieFR4HvTuV4dTGC6vu01hT4hhqb3sGMYwi9GR6mMrUnyehvm5OjZaeNevT3Z7SzoT66kSsv4PnOZeEsyK3j13fSnWAo9nAtiCjvHoFrlkxrI6Iw7_M4n0O2AxRPaopkXhy3u-pR4UfExhvZIQk9SyjNDDsD-ZIyRMI-IMWiYml16ljSCNYqHLs8kDilz6EhA1aHCczXwrq70f-h6DKk3lI5Fh1k9CZD2P-SIWlKEXeO5oKP6ZX7CQ3R91bB96yhjOwuOHwyg2ecnb8Yzy8T-mj9qdUDOOnVayq732IAocqA8rxpscce2UrChU_LdKHwLnCCGMP4KMcaJqAtT9-BTdl6mlpzDuAwKvjQXXD7PabnUtmsqWu0mVx52lk6-_UxEJBVg_7PBSgg3J_tOFg_sSsxtR2LhHnPNhOGm1djTSzVTTzyhTnJ4grLoF4PV5UHPib6vpmBRDM_f5n9sMG-CJYqRr8bHn19sc7MpnaC3RB5DRbHffQluRncKf71vicc8-3-bKdd_SScZBp69H1G--x-LjOb-Snu-jQV_fI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: توافق‌نامه اخیر آمریکا را به لغو کامل تحریم‌ها موظف می‌کند/ آزادسازی اموال مسدودی حق قانونی و اقتصادی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659769" target="_blank">📅 15:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659768">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewQO5FXFoMdy_3gWjWKMFCqXGuuEP6JDxzHrkvgMGveSNgbhITIVA44YA3QamVd0wRdU5jmx0dUvDgJkxIkBoJu31TxfILiCtsuobx5Aqn2JRnSjo8tveXyjAdbaL_9ALX0irCCBLa_wuZyW0aFF7wFrevRypkatHwPIVO7Hdu1tzht01gZJbMNYfshgtCkxPl_4nbdaFFwZx6kSZpamTeSIv2dD3979IxW2LQDCwKmEWH8Gu5YpIypun3WVjM9r8SmUfYxQr1PCENqxSuvyWPwsSi07Gj5aHG-q1mm_XPF2_HX028L8EVy3W2PzTKx9CV6Y7Sk5lfHZ43LvOZca6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی چهره‌های فوتبالی از اولین بازی ایران در جام‌جهانی مقابل نیوزلند
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659768" target="_blank">📅 15:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659765">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gh0-fizaTU-chOyxp8r0WeU5l8ECQ1aqYfGFMBe-spgwn6kDlOBJrg53YaB18yFV1j6cS-Cee0zpvi-YvTcxd8fLPXm6IWogcEVAukDQw1cByKfMoLrmu3YunXqtYS9j6mP0hQKMDJL2K6EHIqGjDW6nn0E8dVhP0QhVz8ky-Wd9EoZgO_j92Z2JgNHnzKInUoqq4Fze6Rl4kfUoagpYw5Km_PKr4Dv5yKoVSH3EfieI9ms-ZgQbP21zReiclBMnt8pZ3L1uIeZNZBwFr4jNk-rrMJXRWhCVTj6kY-lZl9EwAlPrlSMhg37Y5sU0BVWF6xdh-FI4yl3UH9MD9ky4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xegz8LTUUW1Txg4PZ_a05653Vz4fWlKNnveujNFAVIPl6ZBBDl7R8j8HAto9fS8iF9QJtwARYON9UPt_j7kVZK1NDSgsO3edDrmw9gccqWI2UyWmA4H9b2r7RMiHltXMB321IUYJJCRq3MSePkRWMc2tuQRYsUjyP7O44OvaJh6Hf3RYyG-OjYKtrRXQYkeX6TFib6O-M5Yhjs5PL32enBWhoyRPk1pa1XzkeuBnC8GwGeDeaIpcMQIYZVBzyO1fiGGznFbcUT1YU3upxC4pIb20kFxtACnnmEdKdWdlxqhyb7zTIU2UIx9b0nciHWGNtBK5r_98wjpajNTaGJTIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5pCI0J4sICfKIK2tRsEjEO69y44fbbBc7Ytfn6GgJUEZTgjRvgZpe58my7Gh4pCn2IQLPgQte6EDmmFkfEE0V-yeUIJvcQQAt0pUMk8KOIY7yorvgONZ705fevR6DjBeFq5SL3nBS749pv0DwNOujxlmH2JzVdYHGwic8WGuG8S8EUvvTJ2dfWW48Xwhb_oBBAeOTZ9HK13MJwhXhosVrsTcShacwYkXeqtPv72Kc5x6LQEvps0KkQwxof9OP-RBb_VpYLuPvYi6yT0YySorPa6Ey7nvshLDqhgvVGNAwIlt2N1uNthmRmODjmZ2nybvYQ2LIYftb4UYL7gultJnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کلاهک ۵۰۰ کیلویی موشک سقوط‌ کرده در ورامین خنثی شد
فرمانده انتظامی شرق استان:
🔹
نیروهای تخصصی پس از بررسی‌های فنی، موفق شدند کلاهک ۵۰۰ کیلویی این موشک را خنثی کرده و محل را به‌طور کامل ایمن‌سازی کنند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659765" target="_blank">📅 15:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659764">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162a0df50b.mp4?token=DRtBvl7poGaPjbszFQXigI3xaARVb2QAdh5YN1pOtuDe9K1O3Pn19DRXJCEWdZ7fcWSiJA-T8pgf9zsvB8MvoBjwzqjEvCVl21j3EzcTy2uPaB_s2Tmiafkll7RwJXO4-zY4JVN1gxgpNmJoGlXXd66pM7a_iRbnoWFLz1sSY8UMZxYqU6mSb29KPQ1D7dcNsiRLdMjoWFP7ia-kvKF45aerFygMV0T8nKeAeOutWu6OnaEDf1XcUFqJTT1vKlS523X5zNuw_Z8LQ2mgQCYV76YjPi5u-Y_YIcY9ax5YstDt0gtxO0qTxlR47VZMAmgT_k0BhAQYG5799yNkrhhHqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162a0df50b.mp4?token=DRtBvl7poGaPjbszFQXigI3xaARVb2QAdh5YN1pOtuDe9K1O3Pn19DRXJCEWdZ7fcWSiJA-T8pgf9zsvB8MvoBjwzqjEvCVl21j3EzcTy2uPaB_s2Tmiafkll7RwJXO4-zY4JVN1gxgpNmJoGlXXd66pM7a_iRbnoWFLz1sSY8UMZxYqU6mSb29KPQ1D7dcNsiRLdMjoWFP7ia-kvKF45aerFygMV0T8nKeAeOutWu6OnaEDf1XcUFqJTT1vKlS523X5zNuw_Z8LQ2mgQCYV76YjPi5u-Y_YIcY9ax5YstDt0gtxO0qTxlR47VZMAmgT_k0BhAQYG5799yNkrhhHqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین طاهری: هرکس علیه جمهوری اسلامی فراخوان دهد برای من با پهلوی فرقی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/659764" target="_blank">📅 15:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659763">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e32345399.mp4?token=FEWTPUp8Z6b6do6BT0z4RKzGz05fPYUbJl7PYNp5X889eeVnD_I4e7vtge-G1aVc9_VQSa8JJUBuBILjDuVM3TXwNChmy3PPIkCJasQd0-pBd13TGV6_mrwwQ-zFUzsnYi5YM9td5wbAHDsoOhb9g1seORuKlAao7YOPSw_G31-CUDJItKUzR4bOzEUj_TJEHUFC8J0lfthaaFIRQQuF7fyYIJ-s4mVzv4d0FmUQmuKHcAFMhRQ3UXO4sFUrXQmgsCog3Ej2VNkRLIx0yxkAGCtCrnM2-PzPyD-Gj02-ncRHDn9D5aji3tUEHY2T8qrB1GSermOfru4cdX1o5_chFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e32345399.mp4?token=FEWTPUp8Z6b6do6BT0z4RKzGz05fPYUbJl7PYNp5X889eeVnD_I4e7vtge-G1aVc9_VQSa8JJUBuBILjDuVM3TXwNChmy3PPIkCJasQd0-pBd13TGV6_mrwwQ-zFUzsnYi5YM9td5wbAHDsoOhb9g1seORuKlAao7YOPSw_G31-CUDJItKUzR4bOzEUj_TJEHUFC8J0lfthaaFIRQQuF7fyYIJ-s4mVzv4d0FmUQmuKHcAFMhRQ3UXO4sFUrXQmgsCog3Ej2VNkRLIx0yxkAGCtCrnM2-PzPyD-Gj02-ncRHDn9D5aji3tUEHY2T8qrB1GSermOfru4cdX1o5_chFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: جزئیات ابعاد دیپلماتیک توافق به زودی رسانه‌ای خواهد شد
سخنگوی وزارت امور خارجه:
🔹
برنامه سفر به برخی از کشورهای منطقه و همسایه، پیش از آغاز نشست ژنو، در دستور کار قرار دارد که به محض قطعی شدن، جزئیات آن اطلاع‌رسانی خواهد شد.
🔹
همچنین در خصوص نحوه و سازوکار امضای یادداشت تفاهم، تصمیم‌گیری نهایی ظرف امروز و فردا صورت می‌گیرد و نتایج آن به صورت رسمی اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/659763" target="_blank">📅 15:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659762">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
پزشکیان: تفاهم ایران و آمریکا جمعه امضا می‌شود
رئیس جمهور:
🔹
تفاهم خاتمه جنگ روز گذشته با هماهنگی های لازم مصوب شد و قرار است روز جمعه به امضا برسد.
🔹
دشمن تصور می کرد با شروع جنگ کشور برهم می‌ریزد. آیا اینگونه شد؟ پاسخ منفی است. این به مدیریت استانداران و فرمانداران باز می گردد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659762" target="_blank">📅 15:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659761">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4094c516.mp4?token=mm1hJ-3t4kQZz_bpnnnGd-CZvbGYMHC7eUXb9DMRh80MnFWw0_BPfFECXLFQr10I1ioU0ev4-iO7rz_zbidjazXI-kbxcpp6VWIN5Yv_SleAGXu1yEzePuBX2cOU7tw0NUqPxdzoV8w_9VMbE53uq_BTKT01Y6FTT5UY3wDeMvjfsYLhdFmJQgdlMGw9F8c2PrpIyE5TvxlmVyLcaD0Rdz7WOSRLTw1uZwukJqOpqw-onvR4QWCHMrFX1KkzMQbJDPg30s_AYgRHp0ESNio9zG9VfHnxf7iJz9SWwl3WS95dzpfBquBKRVqiPGCi-lJ3kQxuvm5IaUP9ybFlwKQPFnJQ9O_HRM8TX5i3G224scgvcL4iU8RqBkXNPBchuispmg_IrSXgiGOzV5yj9lsXwtKDyFIQe-WQvOOWjGlMZgA6Khzv7-he-wAC44Xe-3JXu560r0DwDPjxtrYJNwl51_fjJJbLVn-SiDVGJbcEF_ZWgFyz6OFhzWEPmDCcwWaGm6TiTxdZm-udkl7jR1HqpJ1D8rjsQjTz0APPuzC4Of2LsRTbb3ZKHZ97x2_z-hq7QkUCuzwsAoo0wv2iifJMSL7tsfyX4PkFoDqr52zt_4b1iDE4QoqtIP6kb7yeTQBxI08E4hGU7CICKfa-zU09y-ICExgM7MLeCWE29QlNio0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4094c516.mp4?token=mm1hJ-3t4kQZz_bpnnnGd-CZvbGYMHC7eUXb9DMRh80MnFWw0_BPfFECXLFQr10I1ioU0ev4-iO7rz_zbidjazXI-kbxcpp6VWIN5Yv_SleAGXu1yEzePuBX2cOU7tw0NUqPxdzoV8w_9VMbE53uq_BTKT01Y6FTT5UY3wDeMvjfsYLhdFmJQgdlMGw9F8c2PrpIyE5TvxlmVyLcaD0Rdz7WOSRLTw1uZwukJqOpqw-onvR4QWCHMrFX1KkzMQbJDPg30s_AYgRHp0ESNio9zG9VfHnxf7iJz9SWwl3WS95dzpfBquBKRVqiPGCi-lJ3kQxuvm5IaUP9ybFlwKQPFnJQ9O_HRM8TX5i3G224scgvcL4iU8RqBkXNPBchuispmg_IrSXgiGOzV5yj9lsXwtKDyFIQe-WQvOOWjGlMZgA6Khzv7-he-wAC44Xe-3JXu560r0DwDPjxtrYJNwl51_fjJJbLVn-SiDVGJbcEF_ZWgFyz6OFhzWEPmDCcwWaGm6TiTxdZm-udkl7jR1HqpJ1D8rjsQjTz0APPuzC4Of2LsRTbb3ZKHZ97x2_z-hq7QkUCuzwsAoo0wv2iifJMSL7tsfyX4PkFoDqr52zt_4b1iDE4QoqtIP6kb7yeTQBxI08E4hGU7CICKfa-zU09y-ICExgM7MLeCWE29QlNio0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: پایان جنگ در لبنان بخش تفکیک‌ناپذیر تفاهم جامع آتش‌بس است/ ایران اجرای دقیق تعهدات بین‌المللی طرف‌های مقابل را رصد می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/659761" target="_blank">📅 15:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659760">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: یادداشت تفاهم ایران و آمریکا محصول ایستادگی اسطوره ای ایرانیان بود/ در یک سال اخیر، نبود آزادگی را در رفتارهای آمریکا و رژیم صهیونیستی دیده‌ایم  بقایی:
🔹
جنایات آمریکا و رژیم صهیونیستی در جنگ ۱۲ روزه را فراموش نمی کنیم. شورای حکام و آژانس…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/659760" target="_blank">📅 15:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659759">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3090ffec28.mp4?token=fwH1imZmjo5wc_DGIdxx58B1bntw2XXs-xqQqrahiVgloaBFkdw4chZ3VCCZ_Qf2mgkL3RK7xGYz_FWQzsjqzzLoXyaKgjUm1HegM8XqIxTy4LZZOeVP-6QwQk3JgKPzCVyrcLj6SnbAA55xV1g9a_FFgnwASdaJwxQTe4Lg5c0s5Rsj0d55RFG6nemplLsnhnpEYZV-UkjEjqX29AWNRdU_s2369ZQ_q1vTTVQEb9dia4hHB61MQC0rPB9FlW-Uy5mX8VKQMizWibVY1_teVtsTnKoIFkOGGzUKGsTkPdg6UaMvD-7jxT0ZUKnT0pdQgAvGCci69NjMPkNxvZmCDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3090ffec28.mp4?token=fwH1imZmjo5wc_DGIdxx58B1bntw2XXs-xqQqrahiVgloaBFkdw4chZ3VCCZ_Qf2mgkL3RK7xGYz_FWQzsjqzzLoXyaKgjUm1HegM8XqIxTy4LZZOeVP-6QwQk3JgKPzCVyrcLj6SnbAA55xV1g9a_FFgnwASdaJwxQTe4Lg5c0s5Rsj0d55RFG6nemplLsnhnpEYZV-UkjEjqX29AWNRdU_s2369ZQ_q1vTTVQEb9dia4hHB61MQC0rPB9FlW-Uy5mX8VKQMizWibVY1_teVtsTnKoIFkOGGzUKGsTkPdg6UaMvD-7jxT0ZUKnT0pdQgAvGCci69NjMPkNxvZmCDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: یادداشت تفاهم ایران و آمریکا محصول ایستادگی اسطوره ای ایرانیان بود/ در یک سال اخیر، نبود آزادگی را در رفتارهای آمریکا و رژیم صهیونیستی دیده‌ایم
بقایی:
🔹
جنایات آمریکا و رژیم صهیونیستی در جنگ ۱۲ روزه را فراموش نمی کنیم. شورای حکام و آژانس بین المللی انرژی اتمی از این آزمون سربلند بیرون نیامد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/659759" target="_blank">📅 15:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659758">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzVk2nPkCLcX1wrFzHN7_fIAjOdgJdRrArPKYkXDMbJCTGk_0KL0T6FWMTiWChnXRuTj7qfRFcx0cKRifkz9sgihVksEK9QiRPM6o-qpGY84AiyaPdyD45JApFGRJztzjMhAdGgKaqj5Xg8sgTrMeultGUNVTdhrXYeBd1KxMQ7tg0Y8sFQBRgRMgA8l6p1_xzRW2W7zB2_T32r9AMG1Gp6P51YcCZIWVlJrnvyOcLk8jtrzNOjnyEHgcvSHJc4r_imjJ4phYMxjmf1Jh_sb3JWdHjH_Ciwq1akFr1DDcGVMnlvvP-Z3kxkErU0c-zYbncXzn3oDbXsH_eVDqoxYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: مقاومت از میدان انقلاب تهران تا میدان آزادی ملت‌های مظلوم به پیروزی رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/659758" target="_blank">📅 15:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659757">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bffa0d97.mp4?token=PY5AoW07j-qTzFHV8wl8quxUAI6NMgH0_kvViWh0ZahBiAAQK1CXMBW2SIH9SLP6Bhj2ypbPI2-rY_ZhfLfJxY8-9oLvWNzMXFCMum8vSvr5XVCzfaTWFGtbl9evpZYncUR3e8rZpBDiQJ70a4jm6szLSQpBGdawvGW7yVnNrKC9NwqzbYFJnUptNBfYTUTyGBxCj_-DY5Y0P-C_vg5DMIotw9-zJtqZ2SRMp66FtHg2cnoeb2k2CBMqPLtmB6G2Evr3gTKWpcNGDA_SIgE4thH2_JOMgX5QnfvD9osq3I0OG8OneI54f9L8WdKbOPpJTmuu0C86zy-ptBjGgyPP3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bffa0d97.mp4?token=PY5AoW07j-qTzFHV8wl8quxUAI6NMgH0_kvViWh0ZahBiAAQK1CXMBW2SIH9SLP6Bhj2ypbPI2-rY_ZhfLfJxY8-9oLvWNzMXFCMum8vSvr5XVCzfaTWFGtbl9evpZYncUR3e8rZpBDiQJ70a4jm6szLSQpBGdawvGW7yVnNrKC9NwqzbYFJnUptNBfYTUTyGBxCj_-DY5Y0P-C_vg5DMIotw9-zJtqZ2SRMp66FtHg2cnoeb2k2CBMqPLtmB6G2Evr3gTKWpcNGDA_SIgE4thH2_JOMgX5QnfvD9osq3I0OG8OneI54f9L8WdKbOPpJTmuu0C86zy-ptBjGgyPP3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: «اگر دین ندارید لااقل آزاده باشید» و این نبود آزادگی را ما در رفتارهای آمریکا و رژیم صهیونیستی در این یک سال اخیر به عینه دیدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/659757" target="_blank">📅 15:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659756">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6344876d5.mp4?token=pMJHM88HfJPqGjRD3hXd67o0cIp-PRMg84VwPSqwjaopNYigj6Zfki8kYIokDs4oWNh0v01fhxa3mSPEWqnAxr7QabuEAvAZM9xSSwu_MQI0wAlSHmSdpdKsDqMQNwT6sjvlpIrgXl1C2gqa39CkNZe6tj_UQuS61-jYwAXSAebyTM2TEpONLZUH_WSusO9lKqjzbW8ntJKFKunTzwWd7kOnd8WGcYahQ1Nvdv-1B_7f8GC19Xu4EQWalneQ4j7cdgJM8BI_yhtDWhIYIul6WGLIA70Gjf5vQscCwZ-Sf3nvOqgtHn2dbmwBn84Hf7HrrgyTUtV3gKvtkkKxdXv06QROkDmz9HYK9dW_eOBybETDh9iCrUOtXUpD_lumjGQHW5pVr_CIi3BxCVppUbXWOjdP84W-Jndp_1wZZDqBtATOqb6JOdZkqdom7PSo9xDsWvN6dUxS_TsgPohGvHCTSKEVYSDThyuMLHRBcykmgbzjC9dKjkTEzEexhlr1uKvpaKJl7a7vijpuJpKwkqmTbG-E8qsOjyjQnGYAQ-0OoBhWEsD8JIhleJwJRORrtiL2zZKX7k-IchvLdUMw0TzPaDl1jko26gEn2N_T2wO9ZJGeOtJ8sW7X3ibeevgmbdz2KS-Mn5t0xZtoBRNT_fzBW4ElODTaHxtxtcIPEHCl_eU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6344876d5.mp4?token=pMJHM88HfJPqGjRD3hXd67o0cIp-PRMg84VwPSqwjaopNYigj6Zfki8kYIokDs4oWNh0v01fhxa3mSPEWqnAxr7QabuEAvAZM9xSSwu_MQI0wAlSHmSdpdKsDqMQNwT6sjvlpIrgXl1C2gqa39CkNZe6tj_UQuS61-jYwAXSAebyTM2TEpONLZUH_WSusO9lKqjzbW8ntJKFKunTzwWd7kOnd8WGcYahQ1Nvdv-1B_7f8GC19Xu4EQWalneQ4j7cdgJM8BI_yhtDWhIYIul6WGLIA70Gjf5vQscCwZ-Sf3nvOqgtHn2dbmwBn84Hf7HrrgyTUtV3gKvtkkKxdXv06QROkDmz9HYK9dW_eOBybETDh9iCrUOtXUpD_lumjGQHW5pVr_CIi3BxCVppUbXWOjdP84W-Jndp_1wZZDqBtATOqb6JOdZkqdom7PSo9xDsWvN6dUxS_TsgPohGvHCTSKEVYSDThyuMLHRBcykmgbzjC9dKjkTEzEexhlr1uKvpaKJl7a7vijpuJpKwkqmTbG-E8qsOjyjQnGYAQ-0OoBhWEsD8JIhleJwJRORrtiL2zZKX7k-IchvLdUMw0TzPaDl1jko26gEn2N_T2wO9ZJGeOtJ8sW7X3ibeevgmbdz2KS-Mn5t0xZtoBRNT_fzBW4ElODTaHxtxtcIPEHCl_eU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدانی به وسعت یک ملت
در این میدان هر کس به‌قدر توان، نقشی دارد
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/659756" target="_blank">📅 15:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659755">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خودروهای ۴ منطقه آزاد جدید پلاک می‌شوند
رئیس پلیس راهور فراجا:
🔹
به‌زودی سازوکار آغاز پلاک گذاری خودروهای مناطق آزاد بانه، مریوان، مهران و بوشهر نیز فراهم خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/659755" target="_blank">📅 15:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659753">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
لاوروف: ویتکاف و کوشنر به روسیه می‌روند
وزیر خارجه روسیه:
🔹
سفرای تروئیکای اروپایی در نشست  برگزار شده در وزارت خارجه روسیه درباره اوکراین موضوع تازه ای را مطرح نکردند، این کشورها به‌طور مداوم میانجی‌گری خود را پیشنهاد می‌کنند.
🔹
اروپایی‌ها به اشتباه گمان می‌کنند که می‌توانند به مسکو اولتیماتوم بدهند؛ چنین موضعی غیرقابل‌قبول است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/659753" target="_blank">📅 15:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659751">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9vejhR0bQdCy50Nbq0Ih99S4un8VbZYFFv9o_cRNJ_oj-zYToeWPKtNw4okG8eSWruENxxFONJ5gjSwsqbaxa_4mq324ZNtMQq6OOXoMmbbR2EAvmjNFVV-JKs9eyYqcMD0nmza7xhdMsWgdLULKLZVXNsz2i3qk8T9bmUNTXpoZdswXi0kMUUKhkw3FTRRlskUc8FjavacN8oZRMfoyCa3VCkbLxXVsJWAO-lOrKgpc8yHtL2EFd1V1j0xpyiEDmP65zW_54KNIzgg816v_gPxG3IwDSxkCdPjjth7o4NyJadHpbPKrZXnZoEwo3BsCACyVWV9hAHuYyVRszNFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۵ خرداد؛ روز ملی گل و گیاه
🔹
۲۵ خرداد در ایران به عنوان «روز ملی گل و گیاه» شناخته می‌شود. این مناسبت در سال ۱۳۸۴ با هدف ترویج فرهنگ حفظ محیط زیست، گسترش فضای سبز، حمایت از صنعت گل و گیاه و افزایش توجه به نقش طبیعت در زندگی انسان نامگذاری شد.
🔹
هرچند این روز پیشینه تاریخی یا مذهبی خاصی ندارد، اما با فرهنگ و تمدن ایرانی پیوندی عمیق دارد؛ از نقش گل در آثار هخامنشی و باغ‌های تاریخی ایران گرفته تا جایگاه ویژه آن در شعر و ادبیات فارسی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/659751" target="_blank">📅 15:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659750">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
آیت الله نوری همدانی: از هر اقدامی که موجب تضعیف وحدت است پرهیز شود
🔹
لازم است شرایط کنونی کشور مورد توجه قرار گیرد؛
خدای ناکرده بر طبل اختلاف کوبیده نشود
و از هرگونه گفتار، رفتار و اقدامی که موجب تضعیف وحدت، همدلی و انسجام ملی گردد، پرهیز شود.
🔹
در رأس نظام اسلامی، ولایت فقیه قرار دارد که باید در نهایت از تصمیم ایشان تبعیت شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659750" target="_blank">📅 14:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659749">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMUg5AXwV15IlJ688l8pU0x71NJgFC2YeOyFgLx7Gk-Mpg-f5qIQ2Ydjr47TeHYHjrJNTQ0zwUsId2M2yKlB7mLICVwh5g9xcVcpci234W57u9HXt4-Fh_MrQeulvgU_kJsm6t8ZnYLlrVkysLCKuhSMjKA966O3VLxdA_Ox3E-vXzxJn3SYs0hkrtRiaKi2Szc8bq5tSfpQAE8fhQNlEnwXkz0ttiARzoLBGdCvDvVNYdJ1FrSbPi-b3DcSlx6Gg7_POQOldAOgQSfynJcRlfYB7KLSUaIVXRoZ2NM60keiA_2i8yn2-bI6ATtKgtrpVs88pPD_jPp__nhLIP7tdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس سازمان اطلاعات ترکیه: با احتیاط منتظر توافق نهایی می مانیم
‌
ابراهیم کالین:
🔹
خبر دیشب مبنی بر توافق بین آمریکا و ایران مورد استقبال همه ما قرار گرفت. اما ما با احتیاط منتظر می‌مانیم. زیرا دوره پیش رو، دوره دشواری خواهد بود که در آن مسائل اصلی مورد بررسی، بحث و مذاکره قرار خواهند گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/659749" target="_blank">📅 14:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659748">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
احتمال کناره‌گیری نتانیاهو از انتخابات بعد از توافق تهران و واشنگتن
بوشینسکی مشاور سابق نخست‌وزیر رژیم صهیونیستی در گفت‌وگویی رادیویی عنوان کرد:
🔹
توافق میان ایران و آمریکا، نتانیاهو را نسبت به خودش بدبین کرده است، وی حتی ممکن است از انتخابات کناره‌گیری کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/659748" target="_blank">📅 14:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659745">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AcFFTkBBdeE-cFi0ssX4rvEeNbNQd-fegBkwDz80oshtKUaHOaFee-8POoiWxHdXNhWY69Qzazt4W5vlsAg5Ruwtf_V0Wm-_RttXH7QOs_f2s2jUnFat3NBIe_MltD0fsSRgas-aJ_HzlCaAMMOL0oIEgTS1D5qX4vh9hkBXSUWXdhMKtTIUBqxh04QUOvlV_m-2sWHOd9bCWg95E2BW73lBmFKrupwU-EKntiDdAGZuHnwoz07waCJ_MCoFI4tXbLt7oDghcc8fujDxIkxj3OIVh7eu4GF92WQRjwbOJfRChsAg5aWWk88qbHO0T_9-lDXxBMMfBl78BXlZoybfxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goMn0RD_-uvThmYbQoCveCfSAh1dopU-NgpqrqJ2TOhyQJW1_rfTPexVMidpboC_pXyk4vjOOsu3s-QTPFuxALHAv2KrKl4bx_yNMNEXGNjAy0WboR1kBhUEMTT-iohRjpLu5qubmyv9Wl1mgrxb9X1c3ZLPSUzs1Qi9rSx2dY3cvo_kH6Yk_suvdN6hLv37YuP2YrXfO6xdMn4fJN_8SQrCQVc_1iCT_9RdnbndEJdto3cqfKQd-hDU5qHqak7K4Wq77izF5HZ1BFQI46OAq-JB_RimBpkKxfnakiPNXbQIuat6it0FbpsgYNPPQ_8IsbKBRXAEtZWbJS6xft9hRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOtjxZBlmoq6p-wjj2liqL6l4rhyH4ziJcZJZbN3KCMm5knAmlDg9G355qFE4dasFTe28ft_JyoOfIxOrdIVwYWg_e_vwcegvU-68qmbspbW5uFrtb2BYI_5KnWitHQiaD44LcdMr8Mq6jABojs__iaxmraGepF-AwS_ZMJskeALoLEHNYgZUz0r-O05GrIsDYfaDqDmto34HEpcfh8kPR0iqtR-WCpMXX3U5F3PjUOUdYYrSYF71tjZJeOHh0AAfZYYAT7HR1xUb1azBuvWwC3b0ppZmO-SicDK0Tj0L7v4CdKmyeFrNyzKPG1m5NgLPYChMz4b4So_eIFCr2-04A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هزاران آواره لبنانی پس از اعلام توافق آمریکا و ایران در حال بازگشت به خانه‌های خود در جنوب لبنان هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/659745" target="_blank">📅 14:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659744">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5862994f3e.mp4?token=OVF3RWb2FyQKtydzRG7r2uMyWkgQEp9Z2TYxTarK_FXjFeRD4fG7w_aLySDP63VNMD6DDY1qRbO2ugKqi9ElhSa4h28N7nGaR92qvyywAcVVQA0U8YlNpNjAPv40daIw2W7-4_pbzVCtScSfZ2PGRXfUU8nN6CaPWpWBxn3WPAEkDm6OZprUf-elSl5i-w1QG3cBlXCuzWhQfOYFC61izkYb180hQ0Va9rVzayiSOJFkEF_j7mB86hiwJ6--9oGmuZIb60VEVLZ1CcXPQcPlfBu3kPFSM8UFHjKXcdFGju6r-PEAaxw4BPKSvcwJlWqd9r37tK1caBzkTYhXUdj5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5862994f3e.mp4?token=OVF3RWb2FyQKtydzRG7r2uMyWkgQEp9Z2TYxTarK_FXjFeRD4fG7w_aLySDP63VNMD6DDY1qRbO2ugKqi9ElhSa4h28N7nGaR92qvyywAcVVQA0U8YlNpNjAPv40daIw2W7-4_pbzVCtScSfZ2PGRXfUU8nN6CaPWpWBxn3WPAEkDm6OZprUf-elSl5i-w1QG3cBlXCuzWhQfOYFC61izkYb180hQ0Va9rVzayiSOJFkEF_j7mB86hiwJ6--9oGmuZIb60VEVLZ1CcXPQcPlfBu3kPFSM8UFHjKXcdFGju6r-PEAaxw4BPKSvcwJlWqd9r37tK1caBzkTYhXUdj5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یه قابلیت قدیمی و جالب توی گوگل ارث که خیلی‌ها ازش خبر ندارن!
🔹
در نسخه دسکتاپ Google Earth یه Flight Simulator هست که می‌تونید باهاش روی هرجای دنیا پرواز کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659744" target="_blank">📅 14:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659743">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سازمان هدفمندسازی یارانه ها: یارانه نقدی مرحله ۱۸۴ خرداد‌ماه به حساب سرپرستان دهک های اول تا سوم واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/659743" target="_blank">📅 14:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659742">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-jowRSUjYdRJW-Dv-6gTgfuQYC_1IXsDnX8M4gcX2eQn7KGsvunpV8m26Mtpwz6Y_vdd0nvxJVpkd-faTDoliN8cI47DqN73zxZlMDjYmVvO0sZaYs8KgIfltyXGC1mhXthBpbKhngfTGKITSS5gW3XQCHvQEkr3-b0qx8IJJQXGHWylqcWeSyNxKI2wLN2m6dN0jtttTXEPaJ1tGm5VXJpaxr3LzRMm1SKLiknSjOETxyFJ4OUZd0jvNxsKQ6Qi_Xomxm928xRg_9gTI0lIDWsB94TlaTqpxSjpNy_IQfKgrB--a17plsFUJBHn8NuZYYxljBrcRD8CmAF_N4odQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش جواد ظریف به توافق ایران و آمریکا
🔹
‏هوشمندی رهبری و ایثار رییس جمهور، رییس و اعضای هیأت مذاکره‌کننده برای تثبیت پیروزی تاریخی مردم و سربازان وطن، شایسته پشتیبانی ملی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/659742" target="_blank">📅 14:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659736">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LV6g7xpBe_qBAOmfleANVTcRv0uSQJMIngprPj5CDXnkE3Iard6L_uUMZ7_Yv-iQOOkmYXJr0Tlg9T8iy2eAYwIts2dG3aoL6JTdOsw2HvWJhZHR8klq-s5P4OSZ2uziM72zq6Nm4kGjJzGG6ziD_iXRO6O4M-eZjUlcgVlQ685kTOUwVYjqBCDwfc1D5_nqTOOSSWlQ83-gKe5kQsbAR3V5knWJR2tPHU-3ZC7b-d3W5vTdxJaH-DdqxfKBGZtRDOEzsTteb7q8ccIjio9jipYJEOyg88sfec3oy3IxEHm9Ez4RibbN6cuz5KiTF6kQ2d8kkJcDB5LcVfo4jRhjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cj9Mr81MwUZrpadCdcBWYdDDaqKlFtIx5Wf0gFfiePe4MFnbLcYBV9HVlU-kdAMo4mWmuSph2InlBCnvYzNGbIzRlzO-sHs5HMVUTjkGqIoZlOPBU5O5Jzfae6edO0sm97hxill2eNkNuJE5YM00zEpElcr8HDb05yC_CEs5vMLl8r1tjc4XFXhsckIn5_NFxLrS_N7wyGsMy0zgzwPUnj-8UUQFdMfVPx-YGuDnabwouaQk_VnIhRtkT78kpLyCH9ztx5fKixrXmgWGRv-ghdfWb2GOLipwOYJYJHYX8oM0F7sx9PUvQnimWYK5yr9TLIiYbVxoyWm-5NAwtgYY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9426SgTMewvTwKqRXPj28isf2A98kP64U24SQ1r9ENjym1OaVTCg8cvxg7_nkgHJYtbdsE1GaeH8KsitZO5jFYHuz8riAhbvET58_dje7hg1cglz7X9qJzBisPai9SvSfSRr__2wGozz8z6GILqKOzhSPC07oZWQ8V1MRwc1tmbNWSSEYixzj9fOuoGGWGqq2zUGVBlptBy3vtBBG2kJQgR_G5_pQ4-bAcysNSFXmbaj3v4vlf2vDB1oDDzGGgsboYnOYPES61aKsuiEvTh5FWsfpHqGwspZLiNZvve3INEMX0EQrw7PXrO6PzXOiD7q51_M2sjCqzzB_Wk1rvSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKImrGJOnejm99bPCsZTQi8GHukIo7sohptL-cDX5g9eDY0r0w85ZbhIdkIblp1Te6oHszSErVAsjJU1ND59UqBEnhGTFw6iOfowNCdQkGp1dAdgsVUq8uBZab7yM5nYIJ3onc4ATsM68PClDNEJMcCFvYzFTL4S95i94-AySHilX1bTfbUQOVD4EniMf1KeG4nRk3MUY5wj9SmPqG4C0JyfZgG1qzT8YDupqgAZypKqT-RGRd5yycxh3HpF9gyPNZwGZCOAo4plzvQZd4w_n1V9qjOM5K5SI4r0f7DoV36xrPdOFgYmjjfia6Mp0Tc6JxGYmCLLIcT7a7BxR7kRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfxLCVHA4j8lK0EKTObycySDxyWdGvwyX42ZKiaylwlSAnznbYHTqOnIborVddEC0Yk0kypBoQBllScNjxWahakxzt9irSDUntsRn_YFGyE4UpNIEC9qhh-3G_RhYbnegI7T_Ow03fesxxsXu-yBuh-xZ3NiOlFlL389P8a8-60OBtAoyhvrBXdxEskAJL2UOPKMT1yukDqnnoevkgiosxT7aoAo0KhxK0mWOBM6SQRgRdeZfMQ9UAv9hLYfY7LeFysxwhtLutPsaIHeoAkvtSOY4UoV_3qyaZy_AqXNqB_K9PIxCDP8ptr0tI0I776Foet79DCM6Qivalskl2WYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9eX08NbinUeqhJXn1pSL_SQb6-KvngzlqCju_NhDnx7LkPC69UKdnr_60tNFRCctEEY9PoHx7cbSsUr5KisiDylrfs-zIddqefNX229xC2Sr6Vu1o_DDSTRBvfUUuR2Jf9UqOukxBjmtca9AuYArIGn1TdseLxUJa4UK9mzhEHdBBcIVoh_UadB9xsAdIqxk-eixldBV35UOwi6niapBNn9qRbHG1QFbmi4UAeqq-p8-WDHPvCqj2yF5-z9FEj_YffzXNO4DjJF7qA6W_FVzPNwTR26ZN-HHgwaucd_LQ8LoYtTp0R98kGPiCehai7aMcGRsMGnNLeBYeuJA9sfoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش سران و مقامات مختلف دنیا به توافق ایران و آمریکا
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659736" target="_blank">📅 14:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
اسرائیل هیوم: جنگ علیه ایران شکست خورد؛ تل‌آویو ناچار به پذیرش واقعیت است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659735" target="_blank">📅 14:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4852617c77.mp4?token=IRFw1w9IdiAYFFpaMh7VeEuxFR5X22cVDt7PIPBehddaf7MMyru1v3j7Hp3twryTmMwoUf-vNG1-BC8MfOPIru1aTSWGwbkisa3Re5VusIX8qSU2o8puVhTU51y8N9CH9CC8UBsgdjf7YTQbL1-rEJp3zr5ZkT9PULAJWyfbn_guQ1qZGbkx-LNyHv9uHLy03fhyqS5Onz-jg4BtYNN5jTvTVkA8Tow0UZViuEE5T-Bzafs_pXYJFnQ6abKLMw3J3URa_ZI0HuMXPjQhHcrkKWrCSL-9g7D9P_sF1yYZhkdbkGBTPxeX-0eXWVjb-N4nm8Es47ibzA-hc4y9ePa18Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4852617c77.mp4?token=IRFw1w9IdiAYFFpaMh7VeEuxFR5X22cVDt7PIPBehddaf7MMyru1v3j7Hp3twryTmMwoUf-vNG1-BC8MfOPIru1aTSWGwbkisa3Re5VusIX8qSU2o8puVhTU51y8N9CH9CC8UBsgdjf7YTQbL1-rEJp3zr5ZkT9PULAJWyfbn_guQ1qZGbkx-LNyHv9uHLy03fhyqS5Onz-jg4BtYNN5jTvTVkA8Tow0UZViuEE5T-Bzafs_pXYJFnQ6abKLMw3J3URa_ZI0HuMXPjQhHcrkKWrCSL-9g7D9P_sF1yYZhkdbkGBTPxeX-0eXWVjb-N4nm8Es47ibzA-hc4y9ePa18Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور صفر، در تنگه هرمز؛ بیش از ۹۶ ساعت است که نیروی دریایی سپاه هیچ مجوز عبوری صادر نکرده است
حسنی خبرنگار خبرگزاری صداوسیما:
🔹
تا اطلاع بعدی، تنگه هرمز بر روی همه شناورها در گذرگاه ورودی و خروجی بسته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659734" target="_blank">📅 14:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e2d6ec122.mp4?token=k5rYV6A5uR7ZadMGIdXoi0uxC-VIocVlpPsU3YlKOizd6cbtIzvOyXmzyBv8pBRc81dTNVQlejxUeFKJ5AQkeS9IN_CGE61Wg-TKWkDLCzR5Pt5Ylh_VkF1tWVfc6ZOleRb7Aw6jAFl7KXhsVgw7IhBInX266HQeroSo_6_2ZJZnxVm5z0v1DvQWSn1LjvGppsV1dKOjsjQKi_xhgPmJXp6CAmoRe5Kz7-M3wRHklPr_bfaz34cZLvM6FigsTcFUSfV7dqfKEyHdWklWI2I-xwqqjfytnzUWcGcTY1jVf5Ob9gJH0zb6lrlZf9Bh4hfjkgut3RC3dAU5Kn4VxUe0CxjjEP-Y0GoudWEi4MSITuZB30ExItEaMfYP9LWF3c6fSm8wDeIsN7indJ4jJRBHoaMSkl0AIiqKsj1L0gwEW0fIjxQ14_H7p2oZy_0_ycAwCXdm_0dnyg509_UsKEWAIjA_9l3UjVfMRykCvw_cGLSTpIeb97d9I1ZyGAD-lqgNqEEOzJz2FbkIHjgolODWlB8ftcQe8BC3hne3s2h3E6fBbgJEpGgmy1esvP2rjag5Sjh6gi_cuUqgn7x2epz3dyUpuYW9lsmu8-YAOz2-R1IWDLLTez0V2Zg9ukxjtEIGaqJpVNiMtpf_DKLAv_2BkR2Wkr5wYchxLxMIlpeV1wI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e2d6ec122.mp4?token=k5rYV6A5uR7ZadMGIdXoi0uxC-VIocVlpPsU3YlKOizd6cbtIzvOyXmzyBv8pBRc81dTNVQlejxUeFKJ5AQkeS9IN_CGE61Wg-TKWkDLCzR5Pt5Ylh_VkF1tWVfc6ZOleRb7Aw6jAFl7KXhsVgw7IhBInX266HQeroSo_6_2ZJZnxVm5z0v1DvQWSn1LjvGppsV1dKOjsjQKi_xhgPmJXp6CAmoRe5Kz7-M3wRHklPr_bfaz34cZLvM6FigsTcFUSfV7dqfKEyHdWklWI2I-xwqqjfytnzUWcGcTY1jVf5Ob9gJH0zb6lrlZf9Bh4hfjkgut3RC3dAU5Kn4VxUe0CxjjEP-Y0GoudWEi4MSITuZB30ExItEaMfYP9LWF3c6fSm8wDeIsN7indJ4jJRBHoaMSkl0AIiqKsj1L0gwEW0fIjxQ14_H7p2oZy_0_ycAwCXdm_0dnyg509_UsKEWAIjA_9l3UjVfMRykCvw_cGLSTpIeb97d9I1ZyGAD-lqgNqEEOzJz2FbkIHjgolODWlB8ftcQe8BC3hne3s2h3E6fBbgJEpGgmy1esvP2rjag5Sjh6gi_cuUqgn7x2epz3dyUpuYW9lsmu8-YAOz2-R1IWDLLTez0V2Zg9ukxjtEIGaqJpVNiMtpf_DKLAv_2BkR2Wkr5wYchxLxMIlpeV1wI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی که بیش از ۲۰۰ مبلیون بازدید در فضای مجازی گرفت؛ لحظات وحشتناک حمله گله سگ‌ها به یک نوجوان در اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/659733" target="_blank">📅 14:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای آذربایجان: پهپاد حامل ماری‌جوانا از ایران رهگیری شد!
🔹
سازمان مرزی آذربایجان از رهگیری یک فروند هواپیمای بدون سرنشین حامل مواد مخدر از خاک ایران خبر داد.
🔹
به گزارش APA، نیروهای مستقر در پایگاه مرزی «لنکران» موفق شدند محموله ۱۱ کیلو و ۵۰۰ گرم ماری‌جوانا را که با یک پهپاد از ایران به سمت آذربایجان ارسال شده بود، توقیف کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659732" target="_blank">📅 14:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659729">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEPf_tmNQBziKlts0TcOVZUOz6lDyaHxh7HRh3qDLWhle4swxpTC-4D6B-QSVrhesuweCwfWU9iQJomF5GMaJQcuvI7tZ3uNvdcKJYRyQEjkWLttt9_pgflj7_7Anl3W-hwLxgNY4LiQ1qp0yPIZ-wiwuJFUszp9O4irgjuCkMT53c_wgVMg8WvmNOWT3Rgq3luZ3r3bR9rJfXC0nDCGxUlgJwA8AQyv7AoW9dJ6aVdlzYWRXJidv1_sWSQfQT7FNa3zMtDTz4jmTd9VGzDocJ3YjTrpQE9Z-lBcsfiRSWqF1YaLqtn8t5J2KMPAWy23Pg2g7CyWb8OewiJh3K_TDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0p4hu54s18858Q8jF1k73DDF7f-Cby2J5TeAjaHzznC1UNWyNAtOhGN9OJnuWANE_3ZzxcQZvCU2ONg1Gf4kFb6Jysn3bdHqQ8sJqLB-aEQ3mZvTk8xUd9xW0-8tGFJ3PGRpFi7_R-r6jT8g_FM88HIzN_oCXopYfRyfNUhaA0Z4NJYRp4HBcsgv2CHPJcAcKpXKK1MpTNbHfNRpSpsxkSVILZMzgSUjkrBu7JrN1qdFWn-HDplfJ5Q43XeqI5UtlN-WaY1_DhmIErRmXEw6YzMg-wLuDAEd9l3WI5z-kf8NWBgdKJvf1wP1MFkNEP_bylQMEzkaCPD4Q9ko6T7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7W4W0sJa9Lvo_B7x8zWEnsvStUDj6LMLBQORldBigBrF3jSZ-viwCKWfiDE2TSWGciNzr6XHpUSqrAOw7nHjUazxqOkhsO_4hGIUoHSXCoEj2_WK5DarhMV3c7tGJESoBqxddmgdVOBmt5qWQmrU927tn8E2zn1Eh2_m2ncP7E0BI4MPKO66Sd6ZWgLTP0ZYBClk0zdmes80BTnSxKSpbkWLdN9-A5GustDZFmF5OaZ--BwZj8nzqRKZpC-6U8E_jB96myHwipEcIn7BKtYpR7P7KMLiEuN4AoaYPHEP570ThuYxgycow-l0xAzvhChR4VC4stdieRbSJfDn0VCEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درس فرهنگ از سامورایی‌ها، ژاپنی‌ها علاوه بر استادیوم، رختکن تیمشون رو هم مرتب کردن و از استادیوم رفتن
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/659729" target="_blank">📅 14:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659728">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhIBl4Bmp4djxR5gtGkBFJJJOSCDLtYM5Qp7pwuwZmiuNgIE5T4ZYQvyfK7T10vj3fMkFRC9L3soxxbAW1fh7DHgk2U7GGWqJrUG6XNWC9FaZS5QCDsygaePyntiurU0WpaKUqwmuh2XL_Oc5UcYfmXhlQDzq_2-f8jkL4em-d9VDZ61-Qv8pWNAlV1WUABeoilE5zPvKj5VacXPtCcyBDZXn_z4solqEmjfIRwTUsMfpksCNJULBXwSbCbo-sP75mYxKzfsmwNizBjwNoSFjhJMsnOpQFyzNOBYXUuo7f33JKZTHdr8iYev3-PiGRtiqKj4FfXziCuEHbPIawu6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش‌های جهانی به خبر توافق پایان جنگ میان ایران و آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/659728" target="_blank">📅 14:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659727">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9zJAS36OlabvlLk5acWMzP-o0U3SNeA_7_BAwsbWFJUk33NwuSS_wzRVMPEvWNDHWmozpGMNwO6WV7heswHhVOLrylzvT6MVaQpGTtDxhunYoMTaPzlnaFZxGiQXZbXm55JdGVVicLKcxpI4KTT3TglRhphGoCs6h6f9mim8AC0aRTKMG_-vhOAj6dGi98S0bBorInxckp7XcVJB5FBnks22dTauzYxxHri1C3dO2pB7NwEbMh_EzH9VsdyH2K609b2eqF6XHC6I5oIhHJPNDcZMnzIkZVjo0Ln-R4vmiGGKmexqnWxIbtzgiDsH99kmbBTOh8Vs1SPeQpaMu7uvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش جواد ظریف به توافق ایران و آمریکا
🔹
‏هوشمندی رهبری و ایثار رییس جمهور، رییس و اعضای هیأت مذاکره‌کننده برای تثبیت پیروزی تاریخی مردم و سربازان وطن، شایسته پشتیبانی ملی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/659727" target="_blank">📅 14:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659726">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ab29831d.mp4?token=khLsSFor0Up4M5FGsEmbqwa86wXDoLjJIvbKr-EPe_80OS9H0lIYTTrbp6KsXVRWC1OmjSr6sLlJUM2cXoSrk_HhM84lgrlBtH8J4MIDkHxw2UsDtFYNUBBlviy2WvC2-dVHKgRA3nzkxSMxCTqM0jQyz6PXqYhrW1MDlfw3e0N0xoBcDIZm0vaFtPbyiySSfVxxSjgcD1I04P7pvPMbrmqbWQXRnowKBoA-Ju4JpIEzxLoFPjleG5l_G0tQ6cWqMutmVAfHvfzLW9qFAIGdyaG-wIS2hIdcKoLN5QS7jtXytengz0BbJJyRbWSfwM5jNHocr2PCPKr2fFwhgNBOWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ab29831d.mp4?token=khLsSFor0Up4M5FGsEmbqwa86wXDoLjJIvbKr-EPe_80OS9H0lIYTTrbp6KsXVRWC1OmjSr6sLlJUM2cXoSrk_HhM84lgrlBtH8J4MIDkHxw2UsDtFYNUBBlviy2WvC2-dVHKgRA3nzkxSMxCTqM0jQyz6PXqYhrW1MDlfw3e0N0xoBcDIZm0vaFtPbyiySSfVxxSjgcD1I04P7pvPMbrmqbWQXRnowKBoA-Ju4JpIEzxLoFPjleG5l_G0tQ6cWqMutmVAfHvfzLW9qFAIGdyaG-wIS2hIdcKoLN5QS7jtXytengz0BbJJyRbWSfwM5jNHocr2PCPKr2fFwhgNBOWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقش‌های ماندگاری که به بازیگران دیگری رسید و آنها خوش درخشیدند
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659726" target="_blank">📅 14:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659725">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpSjHGWQmjoOrxcpEwLAGpdIJGDqHTFLUqlZfvDnfW9R5SPwIZLdCh7Vo7Sri6KaWG9PRYy21w2HgWVL3ejFmGbHRbGrfbGPNAIsQmczvCLaaiQa_B8Jbs702ElH1dM1gL7yyJH-qJbSbvXPzos-z3S0dHEa2xCmcYosv8c8KmwrSsvc9ddlpSBeWq4HoXIoVoj7O4kz50GihHS1jg9y0hK7jwxI7xKSKbBWtdN4cuMnIeU4C-ONR5nWP0NQjV_aYT3wJC-mX78P18Rr5Mxy-Xmqd_KjRgGRvO7XenJUoh72JyXHi7joIA1ibtnNSqWMt_Kux8PbHzXnyZX28LkkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری فرانسه: جلسات مقدماتی پیش از امضای توافق‌نامه ایران-آمریکا در دوحه برگزار می‌شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659725" target="_blank">📅 14:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659724">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سرلشکر حاتمی: دشمن فهمید باید به ایران احترام بگذارد
فرمانده کل ارتش:
🔹
دشمن دریافت که پیوند ملت با نظام جمهوری اسلامی و آرمان‌های انقلاب مستحکم‌تر از تصور آن‌هاست.
🔹
دشمن با محاسباتی نادرست وارد عمل شد، اما به اهداف خود نرسید و نخواهد رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/659724" target="_blank">📅 14:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659723">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
موسیقی خیابانی؛ هنر یا تکدی‌گری؟
🔹
موسیقی خیابانی در سال‌های اخیر به یکی از جلوه‌های فرهنگی شهرهای ایران تبدیل شده است.
🔹
با وجود برخی برداشت‌های نادرست، کارشناسان معتقدند موسیقی خیابانی با تکدی‌گری تفاوت اساسی دارد؛ زیرا هنرمند با ارائه مهارت و اجرای زنده، اثری هنری را در اختیار مخاطبان قرار می‌دهد و حمایت مالی مردم نیز داوطلبانه است.
🔹
فعالان فرهنگی بر این باورند که موسیقی خیابانی نه تنها تکدی‌گری نیست، بلکه می‌تواند به افزایش نشاط اجتماعی، گسترش فرهنگ هنری و پویایی فضاهای شهری کمک کند. از این رو، بسیاری از صاحب‌نظران خواستار نگاه حمایتی و فرهنگی به این نوع فعالیت هنری هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/659723" target="_blank">📅 14:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659722">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54313f3dd6.mp4?token=h7aLnNHNfI6gsxprK3Vt0GHa0MsCvYG6woRYvrJrlJjck_XF5ioG0qWchDPB3dt06uZ-epyVBcayeuUtsc1R68d7CsPNyHTv1_MlYkmaVXteqPzlgCxa7XVXWL9VNXCjn2WSkew2gYOqpmFORYTcgSu8DbA6FGGoPsh3mZHXFrdrz7qyvVr1H3wPIn1nv6oOacBPdIkaAfGaWVR_WY000kF3D1eNXzbulutCbjvXzRhwa7qbdQSEh72zipBnLxVtySs8vD3EVi-_DBs1LOBn_Wif3Tk1TRPg_6-VuH2pSF9gbA49rmI06ChEX9dI7yk7ZVUsaHHLLVXXtUz6XbvF5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54313f3dd6.mp4?token=h7aLnNHNfI6gsxprK3Vt0GHa0MsCvYG6woRYvrJrlJjck_XF5ioG0qWchDPB3dt06uZ-epyVBcayeuUtsc1R68d7CsPNyHTv1_MlYkmaVXteqPzlgCxa7XVXWL9VNXCjn2WSkew2gYOqpmFORYTcgSu8DbA6FGGoPsh3mZHXFrdrz7qyvVr1H3wPIn1nv6oOacBPdIkaAfGaWVR_WY000kF3D1eNXzbulutCbjvXzRhwa7qbdQSEh72zipBnLxVtySs8vD3EVi-_DBs1LOBn_Wif3Tk1TRPg_6-VuH2pSF9gbA49rmI06ChEX9dI7yk7ZVUsaHHLLVXXtUz6XbvF5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی نماینده کنگره آمریکا درباره ۱۱ سپتامبر: واشنگتن عمداً ۲۸ صفحه از گزارش ۱۱ سپتامبر را پنهان کرده است
🔹
در حملات ۱۱ سپتامبر ۲۰۰۱، چهار هواپیمای مسافربری ربوده شد؛ دو هواپیما به برج‌های دوقلوی نیویورک برخورد کردند، یک هواپیما به پنتاگون اصابت کرد و هواپیمای چهارم در پنسیلوانیا سقوط کرد. در این حملات نزدیک به ۳ هزار نفر کشته شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659722" target="_blank">📅 14:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659720">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1d2b7bfb.mp4?token=hppT-cgvCGPQ9KRpn3qyxM1c2DXWbUC8MSoQ1YFNyfSevDxDBWTbuwm1J2U5DswkMZf0bt1D1ZmnfhRetIvyNYjkb5ZlUB0P32yyBzlYk21Vg0_f1DN_NQIZiOYu1D8DrbOh2a4GDrfCkdoNnR5GZWKZeFEo6g7N-65xXG4G56B_vPxDP3nP9OYL_NVRxjLL7l-EVTB0dYZSShmdyOx2MqZjcUCxkZB6XodCvqQYNvbjqLFlRAndbOINLcR-6ZGP_9TPJ_gu_TtSgvO70FxoaVJSNMjbOZtfBYH-Tg1zqNWSyQQ-elJWagTOzYyCtGZbaanUrVPepG-3D_KvOo491g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1d2b7bfb.mp4?token=hppT-cgvCGPQ9KRpn3qyxM1c2DXWbUC8MSoQ1YFNyfSevDxDBWTbuwm1J2U5DswkMZf0bt1D1ZmnfhRetIvyNYjkb5ZlUB0P32yyBzlYk21Vg0_f1DN_NQIZiOYu1D8DrbOh2a4GDrfCkdoNnR5GZWKZeFEo6g7N-65xXG4G56B_vPxDP3nP9OYL_NVRxjLL7l-EVTB0dYZSShmdyOx2MqZjcUCxkZB6XodCvqQYNvbjqLFlRAndbOINLcR-6ZGP_9TPJ_gu_TtSgvO70FxoaVJSNMjbOZtfBYH-Tg1zqNWSyQQ-elJWagTOzYyCtGZbaanUrVPepG-3D_KvOo491g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چون ایران نباشد تن من مباد
✨
#ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/659720" target="_blank">📅 14:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659719">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6281c32d.mp4?token=KwLdTesKY2NYmWT5EoxQdI8FxHYtKzawX-T4-djF7tsROk_n4ORfSvkGPM26wJqtTcyp8f8z7_mtAaGQZftYzEDg2cbE76owbPNayZsqqkBvjlJQKuLoI7-gcBEN1geDodhyRrMeJlg8I40FycgwcM5-C4itHRvQMmdFB-C0XlBEBcmHmaW8IO_QjeRqyh3ECEDdGmM2s2VVw_755MSIkCb7vHT0UdhqahJ-NnMGa9UA4Y3an6b3baI7XvgFalRVCIuTHcmoUfrVKiAMsKBQoph2rymL0As6xeV6RLYifp2Me5FSVpbsEZmf6eMTRvMpFNtRdML7RV9NmBrABNKuRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6281c32d.mp4?token=KwLdTesKY2NYmWT5EoxQdI8FxHYtKzawX-T4-djF7tsROk_n4ORfSvkGPM26wJqtTcyp8f8z7_mtAaGQZftYzEDg2cbE76owbPNayZsqqkBvjlJQKuLoI7-gcBEN1geDodhyRrMeJlg8I40FycgwcM5-C4itHRvQMmdFB-C0XlBEBcmHmaW8IO_QjeRqyh3ECEDdGmM2s2VVw_755MSIkCb7vHT0UdhqahJ-NnMGa9UA4Y3an6b3baI7XvgFalRVCIuTHcmoUfrVKiAMsKBQoph2rymL0As6xeV6RLYifp2Me5FSVpbsEZmf6eMTRvMpFNtRdML7RV9NmBrABNKuRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هرجا آلمان و عدد ۷ کنار هم دیده بشن، یه برزیلی یادش میاد که زمان همه زخم‌ها رو درمان نمی‌کنه
▪️
اولین قسمت از برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/659719" target="_blank">📅 13:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659718">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
یک منبع مطلع: چالش درباره بند اوّل و بند مربوط به تنگه هرمز تا دقایق پایانی اعلام تفاهم ادامه داشت
🔹
به گفته یک منبع مطلع، در روزهای پایانی تفاهم ایران و آمریکا، عبارت «تضمین حاکمیت و تمامیت ارضی لبنان» به بند اول و «اداره خدمات دریانوردی در تنگه هرمز» به…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/659718" target="_blank">📅 13:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659717">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وثیقه خروج از کشور مشمولان غیرغایب حذف شد.
🔹
یک هسته تروریستی در سیستان و بلوچستان متلاشی و ۴ نفر بازداشت شدند.
🔹
مصر: توافق ایران و آمریکا گامی برای اعتمادسازی است.
🔹
بریتانیا استفاده زیر ۱۶ ساله‌ها از تیک‌تاک، اینستاگرام و یوتیوب را ممنوع کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659717" target="_blank">📅 13:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659716">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950be6aa50.mp4?token=jX75Ed4WKxLnWT8WiLCq8va-UHo4KNpvuFElfnEgRDjyHxhC6GqPNwWAIwU-9-2r6xYLjcZ60J9pBtIeI1dm8CiY1aJGqpUrcU4KrcCWdLjnpoAmVFVC4n6oAdaokKSeiwOR89aI654VG4NzgFXPSAf4mKBFnSMR3ZpQbF4KqP8hbkBAnr919X4OsmkKZpEMQGI6U1bcSekZvLQUY8rNsb6cfafRwRnJBPoAOXwI5k7Kg71Xz1AcdSVV14N6vfKjm2LpDUALqwhYLDVSX8SPn6adRBIu7XnjqgwwNVNkXuSMTcGgCrVa1LEuLo_uHeMeZ3u11ehhS2rlR_D0jwokUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950be6aa50.mp4?token=jX75Ed4WKxLnWT8WiLCq8va-UHo4KNpvuFElfnEgRDjyHxhC6GqPNwWAIwU-9-2r6xYLjcZ60J9pBtIeI1dm8CiY1aJGqpUrcU4KrcCWdLjnpoAmVFVC4n6oAdaokKSeiwOR89aI654VG4NzgFXPSAf4mKBFnSMR3ZpQbF4KqP8hbkBAnr919X4OsmkKZpEMQGI6U1bcSekZvLQUY8rNsb6cfafRwRnJBPoAOXwI5k7Kg71Xz1AcdSVV14N6vfKjm2LpDUALqwhYLDVSX8SPn6adRBIu7XnjqgwwNVNkXuSMTcGgCrVa1LEuLo_uHeMeZ3u11ehhS2rlR_D0jwokUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در جشن تولد ۸۰ سالگی‌اش در چمن کاخ سفید در رویداد UFC Freedom 250 هم خوابید
!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/659716" target="_blank">📅 13:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659715">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ba8ee397.mp4?token=hI4mIcqHaOXo9yb2Q_nqlhZmw8pRSMPFpkrfC3ckMAAfTE8w4rcilhC1gizApD6o3Jc49-VvKDlGvi5zbMHt_pmFTDnTasee0I6mKWDBPR8Mb4stoorT4zL9wWFDyQtnGesjxQf2h0fjx34F3dbW2xZi463waoLTc8ilH_y2f1PWNG3mJQcMcbHDWQSzaiu7c4LvTfH22CIRlBXazKCokVAFro8J0Z6KAQp9keRjE-2xOBkPZVpFDPkFmhYaKBa9jSfvylugmiUfgaUZzST0j9Qtukz9nwb0Y-qxLyCWE5UBokmblfDks56opayAxqL3PSJHN1CrU1Iafc8j6T9Msg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ba8ee397.mp4?token=hI4mIcqHaOXo9yb2Q_nqlhZmw8pRSMPFpkrfC3ckMAAfTE8w4rcilhC1gizApD6o3Jc49-VvKDlGvi5zbMHt_pmFTDnTasee0I6mKWDBPR8Mb4stoorT4zL9wWFDyQtnGesjxQf2h0fjx34F3dbW2xZi463waoLTc8ilH_y2f1PWNG3mJQcMcbHDWQSzaiu7c4LvTfH22CIRlBXazKCokVAFro8J0Z6KAQp9keRjE-2xOBkPZVpFDPkFmhYaKBa9jSfvylugmiUfgaUZzST0j9Qtukz9nwb0Y-qxLyCWE5UBokmblfDks56opayAxqL3PSJHN1CrU1Iafc8j6T9Msg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشست خبری سرمربی تیم ملی فوتبال ایران و مهدی طارمی  امیر قلعه‌نویی ایران:
🔹
خیلی خوشحالم از کشور بزرگ و قدرتمند ایران اینجا حضور دارم و امیدوارم فوتبال وسیله‌ای شود که کشورها و فرهنگ‌ها به هم نزدیک شود و خوشحالم که از طرف کشور و قدرتمند ایران اینجا حضور دارم.…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/659715" target="_blank">📅 13:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659714">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpbWReC0C87MbR45Cc5WGdfX0FoWbRVq6uouVCjf7xNNzE32W6vXmzoSbChNc9HyF4G4iKn-b-Y-Qv4Vzewn4XDC81DOJ9VXUG124FSHso8uIcKi53fx0B2Q-J9UdOwIM8s7u_sR8oQxfiEDi3SDMi6ffElLKBZnOjXRD_dHmvdmUxrVCnPFLXRat7-7dFFsEJvhKYhDzeJ9ZuEFxDVMFrJHIJG2Od433DbOumLoi6eiUydmbIEJJ1An2d_lwBXGZP6WLwI9xI1ZvW9SyvVr257NFiwtnay6gSH6Rqi20GRFlkc_fpj7ZUUa1WwYusN7hEN2P9trFWz9DewpE7S1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ظهوریان، نماینده مشهد: محتوای یادداشت تفاهم ایران و آمریکا هر چه که باشد، ایران بعد از جنگ به طور حتم هم از لحاظ قدرت سخت و هم قدرت نرم قوی‌تر و مقتدرتر از پیش از آن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/659714" target="_blank">📅 13:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659713">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پزشکان برای پرکردن بیمارستان‌ها ام‌آر‌آی الکی می‌نویسند!
مهدی فلاح، عضو کمیسیون بهداشت و درمان در
#گفتگو
با خبرفوری:
🔹
تجویزهای الکی و القایی یکی از علل اصلی ورشکستگی بیمه‌ها و افزایش بدهی‌های سالانه آن‌ها است. برخی پزشکان برای جلب رأی یا پر کردن بیمارستان ام‌آرآی و تصویربرداری‌های غیرضروری می‌نویسند.
🔹
تجویزهای بی‌موردی مثل عکس‌ها و سونوگرافی بی‌خود، تصویربرداری‌های پرهزینه و مکمل‌های غیرضروری چندین برابر هزینه سرم به مردم و بیمه‌ها تحمیل می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/659713" target="_blank">📅 13:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659712">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
واکنش محمد مرندی عضو سابق تیم مذاکره‌کننده به خبر تفاهم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/659712" target="_blank">📅 13:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659711">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ایرانی‌ها سالی ۱۱۷ کیلو نان می‌خورند!
🔹
طبق داده‌های رئیس کارگروه آرد و نان اتاق اصناف، ایرانی‌ها روزی ۳۲۰ گرم نان مصرف می‌کنند.
🔹
این رقم در سال معادل ۱۱۶.۸ کیلوگرم است. این داده‌ها نشان می‌دهد ایران در زمره ۵ کشوری است که بیشترین مصرف نان را دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/659711" target="_blank">📅 13:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659710">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzj4m2H6j74kDWbk5LW1Szs1YhbZT4nOytk8nc-qcYXZjy-mV_kg8Lzoy0RuXbMoYcplzQ_vcpbIfi6F2_0SiHLoxqF-TxLX8Aq7MKlJNgc--6WFwszl4ggkwtFI7nKvqBFAi3M45khGdO8i7_PMcdjZ-1omAS3YdPw47i3oaZhowWojaVG4R5ZporvamIW56dQ76VKf5XOAbCU-h9_Pi2w8vamoMfjPSbEcOicinHzuSoGm1XLpDNfBrJoOhLG8b5hiyN74CH-lhNxcZoCIrgAD4sL-eE00p8TZRKMnYBRyhBm-b_TOYFy5w06l_6rtAxaFQgU2_nC2RwqC5R69GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انگلیس: توافق آمریکا و ایران، بسیار مهم است
🔹
او خواستار باز ماندن دائمی تنگه هرمز و اجرای کامل تعهدات توافق شد و تأکید کرد آزادی ناوبری در این تنگه باید برقرار باشد.
🔹
استارمر همچنین گفت موضع بریتانیا همچنان این است که ایران نباید به سلاح هسته‌ای دست یابد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659710" target="_blank">📅 13:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659709">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96c745c53b.mp4?token=n-SbYHuyAiAKG9ghrVel4u-fJUj-u9DYpH_obrHMziyfqGpgOObYFP2mhvvv4dzFR9bFKbusb1IWtCnr1DEYZMUf7UdN3kSKBed-wA2NILpOWoC9S2zTKZpkOg2lmkA3qgBhvBfHhnXDJRV0b5lTjf0PGXt4sOKTrroWvPZKqGfGlF9cW_9D0IdUa2xck9WlKo4Dny1ldxWykiqLyqaJjRyaPeWyzcyW_tIHI8-xALTt0CpVCd0nuwhwjllgmTMEh2IkW3j2zEYEfE1G3BG5VOwwgMU7G8n0kDwiPTt7LeMD6yVRJ2BagKNMbLC54GadFvAcaniQTzqcacEieyCxaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96c745c53b.mp4?token=n-SbYHuyAiAKG9ghrVel4u-fJUj-u9DYpH_obrHMziyfqGpgOObYFP2mhvvv4dzFR9bFKbusb1IWtCnr1DEYZMUf7UdN3kSKBed-wA2NILpOWoC9S2zTKZpkOg2lmkA3qgBhvBfHhnXDJRV0b5lTjf0PGXt4sOKTrroWvPZKqGfGlF9cW_9D0IdUa2xck9WlKo4Dny1ldxWykiqLyqaJjRyaPeWyzcyW_tIHI8-xALTt0CpVCd0nuwhwjllgmTMEh2IkW3j2zEYEfE1G3BG5VOwwgMU7G8n0kDwiPTt7LeMD6yVRJ2BagKNMbLC54GadFvAcaniQTzqcacEieyCxaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار از حقیقت؛ عدالت‌خواهی گزینشی وزیر کانادایی در قاب المپیک
🔹
وزیر کانادایی خواستار محرومیت روسیه و بلاروس از المپیک شد، اما در برابر سوالی درباره اقدامات آمریکا، پاسخی نداد و محل را ترک کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659709" target="_blank">📅 13:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659708">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQB-hISFGDBdYFOzcd0OJmSw6fJtjKIXW4xGwl01bLihVVzTq8qOrEHQiVamFAn1iD3jM6BG9bE-29LYFfvU1skDZmaTkY0LPnMOnYqjTcsQkYj2VkoJYUhBlUX8BmnRO5AFdD4HSUaj64bJ0u5LOIcaiErDvxMVB6BiAB6vg1MsAnt3D6ELw3ghW1RxTVR4wfeLF9BSFC5SqD7LK0rrARji52a4tXIb-pRkpsSij7B9jCxsA2A_KUdByaoX6OA_jmuANJ2zBbZAbQ0PNJmrHpSIstUrEnBIao9Uv1hcsB0WA9eI_VDr-oWGh-Cn6WbQjo4SM8u-DTcmwXEkmUE8qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعویق هوشمندانه امضای توافق از سوی ایران برای اطمینان از رفع محاصره
«ایران هوشمندانه مراسم امضای توافق را به پایان هفته موکول کرد تا مطمئن شود محاصره آمریکا لغو می‌شود و این بار ۲۴ میلیارد دلار دارایی مسدودشده‌اش واقعاً آزاد خواهد شد.»
@amarfact</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659708" target="_blank">📅 13:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659707">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رئیس جمهور لبنان: ما مشتاقانه منتظریم که این تفاهمات به گام‌های عملی تبدیل شوند که به طور قطعی به چرخه خشونت پایان دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/659707" target="_blank">📅 13:20 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
