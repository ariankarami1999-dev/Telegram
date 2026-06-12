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
<img src="https://cdn1.telesco.pe/file/WlCdA458Mu9036UYv8tQNJ9Jx0Rw_OBhwieKEgZnEbfDkQMZ0J_RtS6gsOORb5dalxH4ZdiJPNDt9fiV2T2pASF9rEfLZzgM3RAFBsaZeRtF4nTQPF0GWUPY3rE6XThLbTntSD8BdJgjxxTVzqZQ3aEOriwWo1LGIh7ZJYw0btaH6asd1Oeoym44bV24t89AXqXLm67xmZTPgS3xkOAuE6yipK9k5EbsebMtbM2bF9-GN6TgZ0q3wTcA_Rys3r8B83-s3LmOkATdMdpulr4BLGV5rT8W2LMxWqxH2uzM2eYdsxU-Vm1nw7Ig6e9kz82EarFJSqbHAU1Ktzf2pn0fjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 20:15:04</div>
<hr>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PW2WtP3yRCfvWR6cXpqhtjsdk1GyMM2sTZXmzBC__AFhjrQH9wR3pkJ2AkTWw0CmO38U6LkZFfuez56lya5fFuQRhDZrQTR7ai2uJyyFF3hqyCYZULEIkzwmvJwJY7XLkrOhcOJokQeh79_pz2_boPC346aqV7tCzEtDQiJsXPmdTl5qjuE-v1B_3sbQ7ZQGEVDrmUWduF9DT7cEQdp5xYlQBvgIVKkM2ssw6CwyQLDZ-5zpMvbEgrnT99UNGkJgYj2Cyc-IKGzSffTnHJR9MlZaCZ_tQXtpDIljn1qTWTiY595NvwobM9qUhIBQq50q4PFttEJdKWfbDoVMHUjwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرحسین ثابتی، عضو مجلس شورای اسلامی، نوشته:
"طبق اطلاعات به دست آمده متن توافق احتمالی بدتر از برجام است/ چنین توافقی نه گشایش اقتصادی می‌آورد و نه جلوی جنگ را میگیرد
دوشنبه شب در تجمع مردم در میدان مجتهدی طرشت حاضر شدم و توضیح دادم که دشمن به دنبال نابودی ایران است، چه از طریق جنگ و چه از طریق مذاکره و کسانی که هنوز هدف دشمن را نفهمیده و فکر میکنند با توافق با امریکا میشود دشمن را سرجایش نشاند، بدیهیات اتفاقات اخیر را هم نفهمیده‌اند.
سپس گفتم طبق اطلاعاتی که تا این لحظه از متن توافق احتمالی به دست آورده‌ایم توافقی ضعیف‌تر از برجام در راه است که خطوط قرمز رهبری در آن رعایت نشده و نه باعث گشایش اقتصادی میشود و نه امنیت کشور را تامین میکند.
در پایان نیز تبیین کردم که اگر بخواهیم امنیت مان را حفظ کنیم باید بیشتر از همیشه آماده جنگ باشیم وگرنه با ژست مذاکره و گفتگو و تن دادن به توافق به هر قیمت امنیت کشور نیز در دراز مدت مخدوش خواهد شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/VahidOnline/76272" target="_blank">📅 20:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nZ-udTvrtpKOLKUmKcBMmLNVhuRsfQulBgojYSftxK8FzPL7afXuMjwKU_99fPi7XKqivVO5L7clS4VEisyz1bRrFn2AEOG-kbcCl9w2yUpWstiQYnWEXgjdTZWHWTMnQzL7MPdIf_Eilrm_WIKsDaTq6lyKzomZ8RSUIBUllBfTLwTLIBp02rpRy3vf_SCEyP_zGwLxQtCU4yKOAkL5LAoVmwkHKDStoYUAkloN7CigjLihWAeusa47ha54jn_xEd_xSGUkqJvwXa95Ak5ebO49KXR7cl7eiy_-8_hQwAQXYv9Q6vF3_mk4duETb8xbBOTxMSagWtcPb9Y9tvjs0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان، در شبکه ایکس نوشت: «متن نهایی توافق صلح میان جمهوری اسلامی و آمریکا حاصل شده است.»
شهباز شریف افزود پاکستان در همکاری نزدیک با آمریکا و جمهوری اسلامی برای نهایی کردن مراحل بعدی این توافق فعالیت می‌کند.
او اضافه کرد: «در میان تلاش‌های میانجیگری فشرده پاکستان، ما کاملا از کمپین بی‌وقفه اطلاعات نادرست که از سوی کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده، آگاه هستیم.»
@
VahidOOnLine
نخست‌وزیر پاکستان در پایان تاکید کرد: «صلح هرگز تا این حد که امروز شاهدش هستیم، به ما نزدیک نبوده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/VahidOnline/76271" target="_blank">📅 20:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dwyOCuKEtL186EgrfeOTu2HKAxmMtHmuMvxSd2AcAAS8sspfz5b-YnMU4rFbiHZkE0irXI53DE6uCcgIKSwWLx0sxEv5jGu4DiKWmR3A1tB6Z-D2-BvQ93AZQqA57Eo69QMtATTC7x80935njdh__jwGT2sYGWoMUHBy7QbuXsXougDHOtfjrVOB7DYaaZXxQx_ctuzYwNoZCo1R9-nQtQ9K75MHUealBqYna2mtNvFTce4TLuqHQJhG6B_MTNZZOqQf3jv977ed6z0NCI0ezjJQISA6v5N0RukVCv-0y_mO9E2PUHpltQHJ3wQbKHxQmrkt23PCVQByWvJlrxw68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اسکرین‌شاتی از
این توییت عراقچی
رو پست کرد:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/VahidOnline/76270" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KS4MdsPm-XJEnOR_RTT0SmJzx0ACUlnOHYBUwoEEU6N6F-4ZjlEES6fI_M6GptUQFbKjM5V9SXbDD5BInIF9ej4EqfOi3OmxGFUBMMkLAhPLZ4Yp-UegtBM5pKwFZvQTfDg6bU3GpayrbLH8K-6wRdFOlxHlmwqnRmFlIROc4d3Bixxlsti4RqzdSCJcHEbvUB5pThE7nha1cU-EaSP8GQYNRHNWaUEXyK0acRJo2CkFQMVyPqV7DKm8CoQ80kB2dRvC0cX7vsTKxj69F9itZhcXNT52pLo_KijWpZZ6XNEBRL03tBaSTel6V23PSMlYbMQ7PW9PqvJiaQchUzHFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه واشینگتن‌پست در گزارشی خبر داد که قطر در جریان جنگ ایران مذاکراتی پنهانی با جمهوری اسلامی انجام داده تا تاسیسات گازی خود را از حملات تهران در امان نگه دارد.
قطر در واکنش، این گزارش را تکذیب و واشینگتن‌پست را به تلاش برای آسیب زدن به نقش میانجی‌گرانه دوحه متهم کرد.
واشینگتن‌پست در گزارش خود تاکید کرده که اقدامات پشت‌پرده قطر، تصویری از شیوه‌های پنهانی کشورهای خلیج فارس برای دور نگه داشتن خود از خسارات بزرگ‌ترین جنگ منطقه در ۲۰ سال گذشته به دست می‌دهد.
در این گزارش با اشاره به حمله موشکی جمهوری اسلامی به تاسیسات گازی راس لفان در قطر در اسفندماه سال گذشته، نوشته شده است این حمله بخش‌هایی از بزرگ‌ترین مجتمع تولید گاز طبیعی جهان را نابود کرد که نزدیک به یک پنجم گاز جهان را تامید می‌کند.
این حمله همچنین قراردادهای چندمیلیارد دلاری با چین و دیگر مشتریان را به خطر انداخت و چشم‌انداز پایان زودهنگام جنگ را با کشاندن قطر، یکی از میانجی‌های کلیدی میان آمریکا و جمهوری اسلامی، به درون درگیری تیره‌تر کرد.
به‌نوشته واشینگتن‌پست این حمله اما یک پیامد پنهان دیگر نیز داشت. به‌گفته مقام‌های امنیتی خاورمیانه و مقام‌های غربی مطلع از اطلاعات محرمانه، این حمله همچنین تلاش‌های مخفیانه قطر برای خارج نگه داشتن مجتمع گازی خود، موسوم به «راس لفان»، از فهرست اهداف جمهوری اسلامی را ناکام گذاشت.
یکی از مقام‌های ارشد امنیتی منطقه به این روزنامه گفت قطر چیزی در حد یک «توافق محرمانه» پیشنهاد کرد؛ توافقی که بر اساس آن دوحه متعهد می‌شد از نفوذ خود بر عرضه گاز برای تسریع پایان جنگ استفاده کند و در مقابل از جمهوری اسلامی تنها یک تعهد می‌خواست: «به ما حمله نخواهید کرد.»
یک مقام دیگر که به همان اطلاعات دسترسی داشته نیز به واشینگتن‌پست گفت پیام قطر به تهران این بود که: «شما بدون حمله به ما نیز به اهداف خود خواهید رسید.»
به گفته این مقام‌ها، قطر نتوانست تعهدی از جمهوری اسلامی دریافت کند. با این حال، روندی که پس از آن رخ داد نشان می‌داد که احتمال وجود یک تفاهم ضمنی دست‌کم به‌طور موقت همچنان برقرار بوده است.
قطر در سومین روز جنگ، زمانی که جمهوری اسلامی صدها موشک و پهپاد مسلح را به سوی اهدافی در سراسر خلیج فارس شلیک کرد، مجتمع راس لفان را تعطیل کرد. در آن زمان، قطر دلیل این اقدام را «حملات نظامی علیه تاسیسات عملیاتی» اعلام کرد.
تصاویر ماهواره‌ای که بعدا از سوی واشینگتن پست بررسی شد، هیچ نشانه آشکاری از خسارت در راس لفان نشان نمی‌داد.
اظهارات مقام‌های قطری نیز نگرانی‌ها را در بازارهای جهانی انرژی تشدید کرد؛ از جمله هشدار وزیر انرژی قطر که گفته بود این جنگ «اقتصادهای جهان را به زانو در خواهد آورد.»
قطر در پاسخ به پرسش‌های واشینگتن پست، هرگونه توافق محرمانه با جمهوری اسلامی را رد کرد و گفت تصمیم برای توقف تولید در راس لفان صرفا به‌دلیل تهدید حملات و نگرانی برای کارکنان و زیرساخت‌هایی اتخاذ شده بود که شریان حیاتی اقتصاد این کشور محسوب می‌شود.
...
iranintl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/VahidOnline/76269" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n0E4RoXqWBYQHLgFnOpnAfA-MtT86te4Ic1RrJkccrU1Nhu3iihptS5VFhDdAnri7XtYqjSHSm_gk8Bsg8-jnJVUtupQKzWjwGi4kbJHdX27u86MFHnX0UNEsoAxpmdDjOIOahuESxKK-czZLjitYfRChgBBUs1qHBWR7cU4uYrAWeteWVZeocDINmGQtOptMa2ufZCSPH8ve1Tx3fPEhlz37Vj5jfVN2tiyO8059QMptNrWCUv4qGjPkIrOcsf2sbwPczgG6ChC1jvAzWK1kSz2kPmw7D2Xi5HDQhK1PiYN8GCfYnqGgkw6IQHjANWIuaBQoxSJpDBISot0rAb_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز جمعه گفت که در ازای امضای توافق با ایالات متحده یا حضور در یک نشست، هیچ‌گونه منابع مالی در اختیار ایران قرار نخواهد گرفت و تهران «هیچ پولی دریافت نمی‌کند».
او در شبکه ایکس نوشت توافق آمریکا و ایران «به گونه‌ای طراحی شده است که اطمینان حاصل شود نگرانی‌های ایالات متحده و متحدانش در اولویت قرار دارند و در صورتی که جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به ایران و همچنین به کل منطقه خواهد رسید».
معاون دونالد ترامپ همچنین وعده داد: «این توافق این ظرفیت را دارد که منطقه را دگرگون کند و به صلحی پایدار منجر شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/VahidOnline/76268" target="_blank">📅 18:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XIL98dqGeF7GiAqVrpkjRI59HnqpaijdZwLj5timIvTIBldo_xcgen2w0aqSA8ApmDVaPZ-9Y6oIeepdJAHAaZvGYcLoDVmHx-CznHdNiw9uaaWhnyznnzS-tq2SmgnDz_YEOU6aWQQCrZx6bIkkkeTcPYDLDEHNRP75rOh_GqG7FLRIJ-4WGMsWNXoFXDvxbrFheB5xWfaWg8pkxAw8AYSIsPX19gDVEEW9C--gZWEZspdwNbnXauH6Vka-L4N8ag8jeuC9QybwNrNGtYd8SSKGImCgRSOIy5IB4KE0b0gXlRSfZ5C6whR0kyLnVJ_vFjOhIAhKFh-mNvYZ-e0Mlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز جمعه گفت که «یادداشت تفاهم اسلام‌آباد» برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران، «هیچگاه تا این حد به نهایی شدن نزدیک نبوده است».
او با انتشار بیانیه‌ای در شبکه ایکس در عین حال از رسانه‌ها خواست تا زمان تکمیل و نهایی شدن آن، از گمانه‌زنی درباره محتوای این توافق خودداری کنند.
عراقچی افزود که ایران در زمان مناسب، تمامی جزئیات این توافق را با افکار عمومی در میان خواهد گذاشت؛ اقدامی که به گفته او در چارچوب رویکرد مسئولانه و شفاف تهران صورت خواهد گرفت.
ساعتی پیش، دونالد ترامپ،‌ رئیس‌جمهور آمریکا، از آنچه درز دادن مواردی از توافق به رسانه‌ها توسط ایران خواند انتقاد کرد و اعلام کرد موضع جمهوری اسلامی درباره توافق «هیچ نسبتی با واقعیت ندارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/76267" target="_blank">📅 18:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fa55fa3355.mp4?token=WIIIG_E-_iihUsjr42pl9FT3_FrC94cEBNkShos9S48IlMPFDAQl7_tpXBDVLs7uLZyeKtAcrRROX6WUcp1IibwB7mRPk0scLrpLW-xOHDoQRdrylYJyOA-HFOtZ3r1zthYRfOAPVSL4JUVsbgwk6EQr_iVo9VhIM_sGayvJFrOHi4981O_oRBPA9x9aFgVv4eZuPMF5L_z2RH76bU1E_0SJUwaBgL4zKU1EYbxhIO-sOeoiFPYrT-9UYtSMAB7n2pAa7Nw0alue5xR4X52e4fPoKVcIPxFYsMLftb8Ak1l5mJdo7CABMMwrGu7GPiNe753dE5D4pcR0pw2DAEGBVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fa55fa3355.mp4?token=WIIIG_E-_iihUsjr42pl9FT3_FrC94cEBNkShos9S48IlMPFDAQl7_tpXBDVLs7uLZyeKtAcrRROX6WUcp1IibwB7mRPk0scLrpLW-xOHDoQRdrylYJyOA-HFOtZ3r1zthYRfOAPVSL4JUVsbgwk6EQr_iVo9VhIM_sGayvJFrOHi4981O_oRBPA9x9aFgVv4eZuPMF5L_z2RH76bU1E_0SJUwaBgL4zKU1EYbxhIO-sOeoiFPYrT-9UYtSMAB7n2pAa7Nw0alue5xR4X52e4fPoKVcIPxFYsMLftb8Ak1l5mJdo7CABMMwrGu7GPiNe753dE5D4pcR0pw2DAEGBVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: خطرناک‌تر از ناو، سلاحی است که می‌تواند این ناو را به قعر دریا فرو ببرد  رهبر جمهوری اسلامی تعیین نتیجه از قبل برای مذاکرات بین ایران و آمریکا را «کار غلط و ابلهانه» خواند و گفت اگر هدف گفت‌وگوها برچیدن برنامهٔ هسته‌ای باشد، چنین موضوعی اساساً جای…</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/76266" target="_blank">📅 18:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtmgFn9Xl3MGqO33kBRxTImNubuSm2gW9D3t_qTigHapBEWk20h3GxP38C_Ih3Oi-TV6-OIbnYg3o7s7gUDTqAVd1WsU8_4m1CjfZbZXpdZRhLxHSD95UfI5VQKkKbzDi2FuglT1RRc_IIGpYIFyreWukUpAMgaBgxso7PV5AOyIc0FovQ-J3bE5ISjTd5rewSkmdM3kxgS8M4BZXBrN6KP6t1Vb3E3IGeebimCWgrWsj-WRdY8EhqQSe3M7fkEkgiOxMHX9Fh_55YMnkh0kXas7w2Ooye_4Wvar_ii_fxrfbfaQkCwyeFeazMJsblzVZTTznQRq7nSGmL0EcWAdTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنها یک روز پس از اعلام نهایی شدن توافق با ایران، دونالد ترامپ مقامات تهران را «بدقول و بی‌شرف» (Dishonorable) خواند و آن‌ها را به ارائه اطلاعات نادرست از مفاد توافق متهم کرد.
ترامپ در شبکه اجتماعی «تروث سوشال» نوشت: «شرایطی که ایران به رسانه‌های جعلی درز داده، هیچ ارتباطی با توافقی که به صورت مکتوب بر سر آن موافقت شده بود، ندارد. بیانیه ضعیف و رقت‌انگیز آن‌ها درباره توافق، فرسنگ‌ها با حقیقت فاصله دارد. معامله با این افرادِ بی‌اعتبار فایده‌ای ندارد؛ در قاموس آن‌ها چیزی به نام حسن نیت وجود ندارد.»
این خشم ترامپ پس از آن برانگیخته شد که رسانه‌های دولتی ایران، گزارش‌هایی از «خطوط کلی توافق احتمالی» منتشر کردند و مدعی شدند که جمهوری اسلامی مدیریت تنگه هرمز را واگذار نخواهد کرد و آمریکا باید ۲۴ میلیارد دلار از دارایی‌های بلوکه‌شده ایران را آزاد کند.
ترامپ در پایان پیام خود، تداوم هدف قرار گرفتن کشتی‌ها در تنگه هرمز توسط ایران را «کاملا غیرقابل قبول» دانست و هشدار داد: «بهتر است رفتارشان را اصلاح کنند، آن هم سریع!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76264" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XjJR0Y9jgSkcy9bSSpjLhnsdR_gee_rayNtIm6puDZkxA4j7rqYqLQ3ozzI76x6Xj4HWWkpqLb79AjMBIlaDrb86DSE7Nls8HMjZhXR13LQ8FenhjEN8oRYDXUACdpN-wCHT_96N--pEeOXY5zkD128aPWtlQ78bbvV3OHyysTd5rwWvJt1Ep_lIk1cexMAcQabf37o8kbGmza3zG6Jo0l2h90wlCFxmglSeDJers3438hPm7A1NSyDc_WYidrUPv8ulH6e616lApyZpX6f2HFtBs2ljJUTx13_7px-oyPRf9Gs-q3q4q1Ln98uxZFjkxhHYuVGOK2Ss8VUHUHIigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در شبکه تروث سوشال نوشت مفادی که جمهوری اسلامی در اختیار رسانه‌ها قرار داده، هیچ ارتباطی با مفادی که به صورت مکتوب بر سر آن توافق شده ندارد.
ترامپ اضافه کرد: «آنچه آن‌ها گفته‌اند، از جمله بیانیه ضعیف و رقت‌انگیزشان درباره توافق، هیچ ارتباطی با واقعیت ندارد.»
رییس جمهوری ایالات متحده مقام‌های جمهوری اسلامی را «بسیار بی‌آبرو» خواند و افزود با آن‌ها چیزی به نام مذاکره با حسن نیت وجود ندارد.
ترامپ همچنین گفت حمله پهپادی شب گذشته جمهوری اسلامی به کشتی‌های هندی که در حال خروج از تنگه هرمز بودند، «کاملا غیرقابل قبول» بوده و افزود: «آنها باید خیلی سریع اوضاع را سامان دهند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/76263" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76262">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXQa3iHIoqzVnFElgqATxCV3phPpW1_-tingTo1QUD-z4uyfSBAi0vusqAd7ZpT9x5d4-rcI3rsONhzE-L8eljdCHDC3djCsRi4XY39km-Xh3Mp2Q2rPXpVHcH3DrIS6PMQX4tfOsZyq1c0peyigMjqiWkVLpovn7WJH6jKutmOR_2msoaM3yzuCb0v7k81EhwwGtCNZPnMiay8RJqYsQfqg3U7YCAGSjPSFcIZf9QdiEjTY53_PJabo2a3lIgdFQEOpnylhceAos7wT0NDjxsx3ROrD0xfenT-juA98kx6u_cr-lggnfo2nIrVigUluXcwEKnDAHw0QC1ik9BnNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، نماینده مجلس جمهوری اسلامی، با انتقاد از پیش‌نویس توافق احتمالی میان آمریکا و جمهوری اسلامی، آن را مشابه برجام و «خسارت محض» توصیف کرد. او گفت: «حرف از پیروزی با این متن مبهم و خسارت‌بار کاملا غلط است.»
نبویان با انتقاد از مفاد مطرح‌شده در پیش‌نویس توافق، گفت در این توافق جمهوری اسلامی حق تولید سلاح هسته‌ای را نخواهد داشت. او همچنین افزود سرنوشت مواد غنی‌شده به رضایت آمریکا وابسته شده و همه موضوعات مرتبط با برنامه هسته‌ای باید مورد مذاکره قرار گیرد.
این نماینده مجلس تاکید کرد: «این توافق مانند برجام خسارت محض است و بخاطر تغییر محاسبات مسئولان است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/76262" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc-jCFAfTdi0vqlD4Lz_aTL7mil6U4zpv387gSb1lPHcTcD5PtMRuPaZhEyc6yusnh0vCTW2j5f4x--4JWc4o7gDvjgazx4vVgJDi4Fw40ioJ2b91DUKc9St67Sk8Kl3Pqk3cee20HEaBfdXB3BUqeyaN3E8rhpmusfisraXdkZTfcffWir2z8Y6nBZpiNUwnDOs0rvMm73LHwJaNhS6Q3-ROjZvi9dLpYcPo1O8rV2KnkxRDaUXqUXXjCBRID8O4I3-4c8LG8UAk-p1a-FYf2wF67IT83Bn-XwWQiHiK9QLIWKWgqSOW-wZMIPXqb98jzMS-Nuvk2rUaHcd9VUpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اعتماد در داخل ایران به نقل از یک عضو رسانه‌ای هیئت مذاکره‌کننده جمهوری اسلامی و وب‌سایت اکسیوس در خارج به نقل از یک دیپلمات از یک کشور میانجی و یک مقام آمریکایی روز جمعه، ۲۲ خردادماه، گزارش‌هایی از محتوای احتمالی تفاهم‌نامه میان ایران و آمریکا منتشر کردند.
این دو گزارش تا اندازه‌ای به یکدیگر نزدیک هستند، اما گزارش اعتماد با وجود جزئیات بیشتر به نقطه نظر حکومت ایران نزدیک است، در حالی که متن اکسیوس برخی از موارد را منوط به آینده مذاکرات گزارش کرده است، مانند تعلیق تحریم‌ها که اکسیوس می‌گوید مشروط به پایبندی تهران به تفاهم‌نامه است.
روزنامه اعتماد به نقل از «عضو کمیته رسانه هیئت مذاکراتی ایران» از تفاهم‌نامه‌ای ۱۴ ماده‌ای می‌گوید که در آن بر «بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی» و «تعلیق تحریم‌های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن» تأکید شده است.
این در حالی است که در گزارش اکسیوس آمده است که تنگه هرمز «بلافاصله بدون دریافت عوارض بازگشایی می‌شود» و «ظرف ۳۰ روز» تعداد کشتی‌های عبوری از این تنگه به زمان پیش از جنگ بازمی‌گردد.
در مقابل این اقدام، آمریکا هم محاصره دریایی بنادر ایران را که بر صادرات نفت ایران اثر قابل توجه دارد حذف می‌کند.
اکسیوس به نقل از منبع دیپلماتیک خود می‌نویسد: «هیچ تاریخی برای تعلیق تحریم‌ها تعیین نشده و تعلیق منوط است به اجرای توافق [از طرف ایران].»
به نوشته اکسیوس، تعلیق تحریم زمانی افزایش می‌یابد که ایران «تفاهم‌نامه را اجرا کند و در مذاکرات بعدی از خود حسن نیت نشان دهد».
تفاوت دیگر بین دو گزارش از محتوای احتمالی به آزاد شدن یا نشدن اموال بلوکه‌شده ایران مربوط است. اعتماد به نقل از منبع خود می‌گوید: «آزادسازی ۲۴ میلیارد دلار پول‌های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.»
این در حالی است که دونالد ترامپ پیشتر به طور مشخص با آزاد کردن پول‌های ایران پیش از مذاکره یا رسیدن به توافق مخالفت کرده و به طور کلی به این کار به دلیل سابقه‌اش با باراک اوباما در توافق برجام حساسیت ویژه دارد.
گزارش اکسیوس در این زمینه سکوت می‌کند و می‌نویسد که «مشخص نیست» که متن تفاهم‌نامه حاوی اطلاعاتی درباره پول‌های ایران هست یا خیر.
درباره برنامه هسته‌ای ایران، اکسیوس نوشته است که تفاهم‌نامه شامل «تعهداتی»‌از طرف ایران خواهد بود، مهم‌تر از همه این که ایران هرگز به دنبال سلاح اتمی نخواهد رفت و بن‌بست در مورد اورانیوم غنی‌شده را حل خواهد کرد، دو موضوعی که ترامپ بر آن تمرکز دارد.
به نوشته اکسیوس، ترامپ موافقت کرده است که یکی از گزینه‌ها برای حل این مسئله رقیق کردن اورانیوم در داخل ایران «زیر نظر کارشناسان سازمان ملل» است، نکته‌ای که پیشتر روزنامه نیویورک تایمز هم خبر داده بود.
منبع اعتماد تنها به این شکل به این موضوعات اشاره کرده است: «۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته‌ای و لغو کامل تحریم‌های اولیه، ثانویه، آمریکا و قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین‌المللی انرژی اتمی» و «تکرار تعهد ایران در پیمان ان‌پی‌تی مبنی بر عدم تولید سلاح هسته‌ای».
در این بخش از گزارش روزنامه اعتماد به موضوع سرنوشت مواد غنی‌شده اشاره نشده است.
به طور کلی، بر اساس گزارش اکسیوس، تفاهم‌نامه در صورت امضا شدن آتش‌بس جنگ را، از جمله در لبنان، تا ۶۰ روز تمدید می‌کند، دو ماهی که قرار است تهران و واشینگتن مذاکرات هسته‌ای را برگزار کنند.
آن طور که اکسیوس نوشته است، ایران و آمریکا بر سر متن تفاهم‌نامه توافق کرده‌اند، و این متن توسط مقامات عالی‌رتبه در جمهوری اسلامی نیز تأیید شده، اما «احتمالا هنوز تأیید مجتبی خامنه‌ای را ندارد». بنابراین در حال حاضر گفته سخنگوی وزارت خارجه ایران که تفاهم‌نامه هنوز نهایی نشده به واقعیت نزدیک‌تر است.
در حالی که ترامپ از امضای تفاهم‌نامه احتمالا در روزهای شنبه و یک‌شنبه حرف زده بود، به نوشته اکسیوس، چهار هواپیمای نیروی هوایی آمریکا روز پنج‌شنبه برای انتقال تجهیزات سفر جی‌دی ونس، معاون ترامپ، به ژنو در سوئیس برای شرکت در مراسم امضا «در روزهای آینده» پرواز کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/VahidOnline/76261" target="_blank">📅 17:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeXB9WU4zTJXmf6KpUFrP5uizTzd9MGcnp970tqc0Rw6iIJJWLdkLTen-DBDkSi4BLVKXNAN3-Z4RUfqS7RSAtv8h8IZXERXnKO6m0xnwHsHM6wFKn0xeRJckhx087Ocg7Y9_tOL-AcWIWazVxQ7BMKY51bkH2rWZM3rB0gYVD_ND5KWbVbGK009mkAjhQmx3aJaBqOjQVD5SgtH2PWSn6YkSdnO-McmcC3Lv-iJ6ZO4z8Xr_CC6qv6Yod8S98nc1jEC0-5FEmb4HGVDWANuPtdVKw8HCJ1y3lpiAKPP11XNS2e6sHVEYkNe4JHiN-xt8i_QNa5OVgAIbEEBrSSuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ به نقل از مقامات ارشد آمریکایی و ایرانی نوشته احتمال دارد توافق میان دو کشور از روز یکشنبه و در شهر ژنو سوئیس نهایی شود.
این خبرگزاری بدون اشاره به نام این مقام‌ها افزوده که طرفین «در آستانه» دستیابی به توافقی برای بازگشایی تنگه هرمز قرار دارند.
بر اساس این گزارش، طرف‌های ایرانی و آمریکایی قرار است در حاشیه اجلاس گروه هفت که از دوشنبه در فرانسه برگزار می‌شود، «دیدار کنند».
اجلاس امسال گروه هفت از ۲۵ تا ۲۷ خرداد در دامنه‌های آلپ فرانسه برگزار می‌شود. به گفته افرادی که در جریان برنامه‌ریزی‌ها قرار دارند، شهر ژنو در سوئیس که در نزدیکی محل برگزاری اجلاس قرار دارد، به عنوان یکی از گزینه‌های احتمالی برای امضای این توافق مطرح شده و ممکن است این مراسم از روز یکشنبه ۲۴ خرداد انجام شود.
یک مقام ارشد ایرانی و یکی از اعضای گروه هفت به بلومبرگ گفته‌اند که «احتمال دستیابی به توافق زیاد است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/VahidOnline/76260" target="_blank">📅 17:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STkaalMGl2JwinFrVJoXL8_nOGfyNrKs3AU5m9JdsH_Qr2Bx8nl9VQYFrKSQggA6GAnCY4UHSQprvCIT4DWWbAF_KFX6_WmWIeEAOxY4Xcgcr0xGaIr4gBOn5hOv_oAm16naY2ji_iPB2dLopXCQF4VZHGRVgntHAYmHsAeaD1G37larGdrFyZZSixUYT7ngjvblwpMRi0A7RVIKa1CVY1wFAVzcJ3u6qUrnCvyDHMowWeli1eownUvRlcTHjkiu4t1CH-fgivZlxtrlISSIx3dhWvQJ9hA0MtbA-dRzWqh_IgsfJISzDGsk8l0-hkVE4-3-jCOmlz0uVv0P_-9jAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، جمعه ۲۲ خرداد به نقل از «منبع نزدیک به تیم مذاکره کننده ایرانی» جزئیات جدیدی از پیش‌نویس تفاهمنامه ۱۴ ماده‌ای ایران و آمریکا را منتشر کرد.
بر اساس این گزارش تهران متعهد می‌شود به دنبال ساخت سلاح هسته‌ای نرود و در مقابل، برخی امتیازهای اقتصادی از جمله تسهیل صادرات نفت و بررسی آزادسازی بخشی از دارایی‌های مسدودشده را به دست می‌آورد.
مهر به نقل از این مقام گزارش داد که پس از امضای احتمالی این تفاهم‌نامه، مذاکرات جامع‌تری به‌مدت ۶۰ روز آغاز خواهد شد و موضوعات پیچیده‌تر از جمله سطح غنی‌سازی اورانیوم، ذخایر اورانیوم غنی‌شده و جزئیات رفع تحریم‌ها مورد بررسی قرار می‌گیرد.
براساس این گزارش ۱۴ محور تفاهمنامه احتمالی تهران و واشنگتن شامل موارد زیر است:
۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲- تعهد آمریکا به مداخله نکردن در امور داخلی ایران
۳- رفع کامل محاصره دریایی ظرف ۳۰ روز
۴- تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵- بازگشایی تنگه هرمز ظرف ۳۰ روز به وسیله ایران
۶- تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷- لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸- ۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته‌ای و لغو کامل تحریم‌های اولیه، ثانویه، آمریکا و قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹- تعهد ایران برای تداوم عضویت در پیمان «ان پی تی» مبنی بر عدم تولید سلاح هسته ای
۱۰- در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱- آزادسازی ۲۴ میلیارد دلار اموال مسدود شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲- تشکیل سازوکار نظارتی برای اجرایی کردن توافق احتمالی
۱۳- تایید توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل
مهر به نقل از این «مقام آگاه» گزارش کرد که در بند آخر توافقنامه احتمالی، دوطرف تفاهم می‌کنند، مذاکره نهایی قبل از آزادسازی نیمی از اموال مسدود شده ایران، تعلیق تحریم‌های نفتی و رفع محاصره دریایی آغاز نشود.
دونالد ترامپ، رئیس جمهوری آمریکا شامگاه پنجشنبه گفته بود که به محض امضای توافق، محاصره دریایی پایان می‌یابد و تنگه هرمز باز می‌شود.
به گزارش مهر، توافق نهایی صرفا در موضوع سرنوشت اورانیوم‌های غنی شده و غنی سازی، رفع تحریم‌ها و «برنامه بازسازی اقتصاد ایران انجام می‌شود» و بحث درباره برنامه موشکی و حمایت از گروه‌های نیابتی «به صورت قطعی از دستور کار خارج شده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/76259" target="_blank">📅 17:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76258">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coOtx7-N7x8kd3dqKP2qJ7mLgRZPsgzF0JHqvMx1qV7ztbu5I6Z04bgGbv9kFhUO4zyvoocXs5iw2HuFK0bHAghbEjG8W1c8VYQY0P_7B9_NSJjjFn7BqbtBdWGZLEUQ7rkYsAUokN-6cDqktnaGlVmt54FyafPN5MRRDxFeIYjSaF0wfc03NItKOI4MkMJPJjucnkw71oOOY6dgG8X7b-je9uzqWF7NOY_GWJR6vuPX_UqbcTdtA97iOXrM4FUpl8yP0RVRdUsj00rKaGQlhUEgauRqkAiELFERy4w1Ych5CK3OsPAJqalbTbBcf-q-bPOYNTFRpFcDMZAUQ9YvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیر احمدوند» ۳۹ ساله، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در نزدیکی کلانتری رشید در تهران هدف شلیک گلوله قرار گرفت و جان خود را از دست داد. او متأهل بود و همسرش در زمان کشته‌شدن او سه ماهه باردار و در شرایط استراحت مطلق قرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/76258" target="_blank">📅 17:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZFQ70kPrrn0uybPU33dhsIkIv1sQtD-19-CK8TPYNzG5FSMUamjyhicHS7FQnArLdur9yy8Gtqqp_GY9HZ0KRAP-mdzz8nThJcveHnZRd4iAmJwGsLhYxuqfmZLrlr8IypWQtFSZf3FeclfjGuWUFw5oaCEfnkkrmsbDBGmr56OCVp-K3xmJ00ex-zif1GU65fhoee5EV7EbHOpMJ-pCGv-MK7d_dEOxRz6RciYOALRpLW-3aQPuEDyvCDGNNVozyGsLe20g5bd1SZPkDfqrthArrPj1EVKQQcBFn8xAJovko2_GALitUJR1bpEnkRFb5o0uFV87YqjU5a0j2PCdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش پولتیکو، اندکی پس از آنکه دونالد ترامپ، رئیس‌جمهوری آمریکا، صبح پنجشنبه در پیامی اعلام کرد که قصد دارد ایران را «امشب به‌طور بسیار سختی هدف قرار دهد»، رهبران کشورهای حوزه خلیج فارس و جنوب آسیا در تلاشی آخرین‌دقیقه‌ای با او تماس گرفتند تا نظرش را تغییر دهند.
آنها به او اطمینان دادند که یک توافق اولیه که مسیر را برای مذاکرات جزئی‌تر هموار می‌کند، در واقع در دسترس است.
به نوشته پولتیکو، این تماس‌ها که پیش‌تر گزارش نشده بودند، به گفته دو مقام دولت آمریکا و یک دیپلمات مطلع از این تماس‌ها، از سوی تمیم بن حمد آل ثانی، امیر قطر، محمد بن زاید آل نهیان، رئیس امارات متحده عربی و عاصم منیر، رئیس دفاع پاکستان انجام شد.
هر سه منبع به دلیل حساسیت موضوع دیپلماتیک با شرط ناشناس ماندن با پولتیکو  صحبت کردند.
ترامپ سپس در تروث سوشال اعلام کرد که ممکن است یک توافق در چند روز آینده امضا شود.
@
VahidOOnLine
این رسانه نوشت گفت‌وگوها شامل بازگشایی تنگه هرمز و دسترسی ایران به بیش از ۱۶ میلیارد دلار منابع مالی بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76257" target="_blank">📅 06:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUclA8DazQfpdStF9SWN5jkqDtDMatwUpP1T0otm1cJf1X-f9FXapHHkzfxt5Q5RTHRWhjJok_Q6LpGpbpyJg5WAQEnZ8b2iPAVQEspBsSwV-KnWb7UxHUxxxVfAYtze4Qddcc70XuTXN_p_m31xRRMGHf914kCwN5G1uhWWfBgWzvdYF0SFNe_DZdY0c-2EGChtD-SLNsbGsj4bQk3yxPw8tVpN3YgS0snG3lq7EKq7RHLYtaFAHKAIRSjH5vJOvcgyyHoJdizWgl_TKaT2_ncvasPvmf2YoCTN9z2ldeDpxs42vW8w5ayfKDfv2ZRB5UX1OUSyBNzqXNJRTzebTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته یک مقام ارشد دفاعی ایالات متحده، ترافیک کشتی‌های تجاری در تنگه هرمز پنجشنبه شب پس از آنکه جمهوری اسلامی ایران پهپادهایی را به سمت کشتی‌هایی که از این آبراه استراتژیک عبور می‌کردند، شلیک کرد، آشکارا مورد تهدید قرار گرفت.
به گزارش فاکس‌نیوز این مقام گفت: «به نظر می‌رسد جمهوری اسلامی امشب تلاش کرده است به کشتی‌های تجاری که از تنگه هرمز عبور می‌کردند، حمله کند. نیروهای آمریکایی دو پهپاد تهاجمی یک‌طرفه ایرانی را سرنگون کردند.»
این مقام گفت که علیرغم این حملات، ترافیک دریایی از طریق تنگه ادامه دارد.
این تحول ساعاتی پس از آن رخ داد که دونالد ترامپ گفت توافقی با جمهوری اسلامی ممکن است ظرف چند روز امضا شود و تنگه هرمز به عنوان بخشی از این توافق بازگشایی خواهد شد.
در پی شنیده شدن صدای چندین انفجار در سواحل جنوب ایران، پیشتر خبرگزاری فارس وابسته به سپاه پاسداران به نقل از «منابع محلی» در بندرعباس گفت که نیروهای جمهوری اسلامی به یک نفتکش که «بدون هماهنگی» وارد محدود تنگه هرمز شده بود اجازه عبور ندادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76256" target="_blank">📅 05:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8rDbeKMr6Ljf2ZOO0aex9V0VFnRR3tVZbU9lco0iKMI84wTG66XT6WI5RoKEpS_0p-SZobagjimugBanDz6gRPNuYDvXhfY3Zvpet8PskRrhSQHoWikw3-SNBHHg6zplcUpqtv2EnvTNNJCdofEIiVnsu27NCt1H5qokAT65OVb_tLY3pxbuyTHHTQ0ZSSp4EgfFMTQqLIFT4UCx1Y5EEJVCnc4R1_t1poo_9rwuoG1i4p7j93xznuQlTKh2GOo9katy_xsddHGpISqlBQoNvQfqfTbxYP-1x1yo5cZVZw_o1t7zJ6DZRt_cDFrWDS2yC6cK4mo46tjegfXDRmQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه به بزرگی ۳/۱ در پردیس
شرق استان تهران
عمق: ۱۰ کیلومتر
پیام‌های دریافتی:
سلام من فاز یازده پردیس هستم همین الان زلزله وحشتناکی اومد اینجا، کل خونه شد گهواره
سلام آقا وحید
یه زلزله عجیب اومد همین الان دماوند سقف میلرزید نه زمین
سلام پردیس تهران زلزله
۳
ریشتر
میشد شایدم بیشتر
سلام  زلزله آمد لواسان
ساعت 3 و ربع خونمون لرزید . رودهن
بی صدا بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76255" target="_blank">📅 03:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=kAWGmtH4r_eUl_GSoinQRSR-pz106YrBhrxVp1KiT5FCLL4Vrrtt7pe-KWsRB8424Q5M2T82uMC7vekHelezqqFQa8B6BDStVXPT6SzUS-MVVoarKq-mnY6ZSZiU-YAcESndjOZ1fuOCgYELBhXXkFXmJZetExc1_EtJD1AeTf8LkLG-YrxC91fq-PkxfFpCjDq7VAbAuCNQhYIwRaSHsjFOyAuYiN_KjQgC007WPmAICEwHkk7SGk_grSrvNZXZsGrycCNfkG9ZyoXNiHQSGAtcX-stpgLIMNXGwRtVMfbeCIifr9CqjMeJU4weAlGYe8Ivfa4oTHWR48vdCmfeAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=kAWGmtH4r_eUl_GSoinQRSR-pz106YrBhrxVp1KiT5FCLL4Vrrtt7pe-KWsRB8424Q5M2T82uMC7vekHelezqqFQa8B6BDStVXPT6SzUS-MVVoarKq-mnY6ZSZiU-YAcESndjOZ1fuOCgYELBhXXkFXmJZetExc1_EtJD1AeTf8LkLG-YrxC91fq-PkxfFpCjDq7VAbAuCNQhYIwRaSHsjFOyAuYiN_KjQgC007WPmAICEwHkk7SGk_grSrvNZXZsGrycCNfkG9ZyoXNiHQSGAtcX-stpgLIMNXGwRtVMfbeCIifr9CqjMeJU4weAlGYe8Ivfa4oTHWR48vdCmfeAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امروز جنگ با ایران را پایان دادیم.
و آن‌ها موافقت کرده‌اند که هرگز سلاح هسته‌ای نداشته باشند.
چیزی که ما روی آن اصرار داشتیم.
این کل هدف بود. این ۹۵٪ ماجرا بود.
در جریان گفتگوی تلفنی برای حمایت از نامزد انتخابات سنا در ایالت آلاباما
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76254" target="_blank">📅 03:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AeIvxbC4ZeqsHc_Z7ufwJUUDCsfnZOYUmnCVR8TxT4qCdyxTZl8pLycT9XKcXxfaRuTVMZVhRBMAm8QBgvQHPJQI5z4eq9wvbnjMWdEdPLMwmzDryRamziKsNqkor1z1k2HmR7XB_B9lSuWJGDh_L3SpZbU3EVtVD0ZuTgREUxSg6QEzkk-GA6qA-PKlCHKvEPX6yl-Xg792XVJMdrW6cIHA6n3mbUhD0C3F8o6k8TRrDv2Rly6kIonfGx4MKb2OnH-agf1JdEBOHkV-8JU5HziZMcl0iHFSmBnZvIqVSRbiQvHLTYeUhJJYTnnLVGbi3vAWS6cBJqkK1f4-dsY_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه بامداد جمعه ۲۲ خردادماه به نقل از منابع خود گزارش داد پیش‌نویس مفاد نهایی توافق میان آمریکا و جمهوری اسلامی شامل تمدید آتش‌بس به مدت ۶۰ روز و بازگشایی تنگه هرمز است.
به گفته منابع العربیه، مذاکره‌کنندگان در طول این دو ماه برای دستیابی به یک راه‌حل سیاسی دائمی تلاش خواهند کرد. این منابع افزودند مذاکرات هسته‌ای بر سازوکارهای راستی‌آزمایی، روندهای بازرسی و محدودیت‌های آینده متمرکز خواهد بود و در همین دوره درباره اورانیوم غنی‌شده با غلظت بالا نیز گفتگو خواهد شد.
به گفته منابع العربیه، آمریکا دسترسی به بخشی از دارایی‌های مسدودشده حکومت ایران را تسهیل خواهد کرد و در چارچوب توافق، کاهش و لغو بخشی از تحریم‌ها را دنبال خواهد کرد. این منابع همچنین گفتند آزادی کشتیرانی بر پایه توافق میان آمریکا و جمهوری اسلامی احیا خواهد شد و گفتگوها درباره لبنان و امنیت منطقه‌ای نیز پس از توافق ادامه می‌یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76253" target="_blank">📅 01:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ادعای خبرگزاری فارس:
ایران اجازۀ عبور نفتکش متخلف از تنگۀ هرمز را نداد
🔹
پیگیری خبرنگار فارس در بندرعباس از منابع محلی نشان می‌دهد دقایقی قبل نیروهای ایران اجازۀ عبور یک نفتکش متخلف که بدون هماهنگی وارد محدودۀ تنگه شده بود را ندادند.
🔹
گزارش‌های مردمی نیز از شنیده شدن صدای سه انفجار در فاصله حدود دو کیلومتری ساحل از سیریک حکایت دارد.
صدا و سیما:
یک منبع آگاه نظامی تایید کرد صداهای انفجار شنیده شده در شهرستان سیریک مربوط به مقابله با یک فروند شناور متخلفی است که قصد عبور از تنگه هرمز را داشت
براساس اعلام این مقام نظامی؛  شناوری که دقایقی پیش مخل نظم دریانوردی اعلام شده بود یک فروند نفت کش است که با اخطار نیروی دریایی سپاه ناچار به رعایت قانون منع تردد در تنگه هرمز شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76252" target="_blank">📅 01:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76251">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادعای تسنیم: آمریکا از اصلاحیه‌های اخیر خود کوتاه آمده!
خبرگزاری تسنیم، وابسته به سپاه، نوشته:
متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است
▪️
پیگیری‌های خبرنگار تسنیم از منابع مطلع حاکیست: آخرین تحول رخ داده این است که فشار نظامی و دیپلماتیک آمریکا برای تغییر در متن ۱۴ ماده‌ای پاسخ نداده و آمریکا از طریق واسطه قطری اعلام کرده است که نیازی به اصلاحیه‌های اخیر آمریکا نیست.
▪️
به گفته این منابع، ترامپ طی روزهای اخیر با شروع به فشار و تهدید و اقدام نظامی و از طریق دیگر با فشار میانجی قطری تلاش کرد تا از دو سو مواضع ایران را تغییر دهد که در نهایت ایران تغییرات جدید را نپذیرفت.
▪️
با این حال این متن همچنان نیازمند بررسی و نهایی شدن در نهادهای ذیربط در ایران است و تا آن زمان سایر گمانه زنی‌ها و خبرها، معتبر نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76251" target="_blank">📅 01:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76250">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">"خبرگزاری مهر" وابسته به سازمان تبلیغات اسلامی، در پستی نوشته:
♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
منابع محلی در منطقه سیریک (استان هرمزگان) می‌گویند صدای انفجاری در دریا، در فاصله حدود دو کیلومتری ساحل، به گوش رسیده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد.
🔹
با این حال، این فرضیه تاکنون به طور رسمی تأیید نشده است و‌ خبرنگار مهر در تلاش است تا جزئیات بیشتری را از مقامات محلی و رسمی پیگیری کند. /مهر
"خبرگزاری  صدا و سیما" هم بعدش در سه پست نوشت:
خبرنگار صداو سیما در سیریک:
دقایقی پیش صدای انجار در سیریک شنیده شد.
🔹
منشا و‌ مکان آن هنوز مشخص نیست.
🔺
منابع خبری از شنیده‌شدن مجدد صدا در محدوده دریایی سیریک خبر دادند
🔺
ماهیت و علت انفجارها در سیریک  هنوز بطور دقیق مشخص نشده اما برخی منابع آگاه آنرا مرتبط با مدیریت و بسته نگه داشتن تنگه هرمز می‌دانند.
آپدیت ۱:۱۰
پست تازه خبرگزاری مهر:
♦️
تکرار صدای انفجار در محدوده دریایی سیریک؛ علت هنوز نامشخص
🔹
منابع خبری مهر تأیید کرده‌اند که بار دیگر صدای انفجار در محدوده دریایی سیریک، در استان هرمزگان، به گوش رسیده است.
🔹
هنوز ماهیت و علت دقیق این انفجارها مشخص نشده، با این حال براساس اخبار رسیده به خبرنگار مهر احتمال می‌رود که این رویدادها با سیاست‌های مربوط به بسته نگه داشتن تنگه هرمز در ارتباط باشد.
🔹
پیش از این نیز منابع محلی از شنیده شدن صدای انفجاری در دریا، در فاصله حدود دو کیلومتری ساحل سیریک، خبر داده بودند.
🔹
با این حال، هیچ‌یک از این فرضیه‌ها تاکنون به طور رسمی تأیید نشده است.
آپدیت ۱:۱۵
تسنیم: سیریک نیست. سمت دریا است.
یک منبع در استانداری هرمزگان به تسنیم کفت:
🔹
تا این لحظه هیچ اصابت پرتابه و درگیری در سیریک وجود نداشته است.
🔹
صداهای شنیده شده از سمت دریا و مرتبط با تنگه هرمز است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76250" target="_blank">📅 00:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/clBgUYYPFvTA9cOh1WAdPWXR5fKQvVjeHW_chgySiinVBSiU6FqcsQvt_QvDSFuHI1Ci00BhBHdAcygkjOmtRUQCo7AAiUTx2k_ykSPLgaAt4ijumHLqT2Ur1jLh1IAe0hsZVIZZ4Ib45jPHa-1DsFsXxcDxWCPsas8-YaHPtgrFe8omGX47dvzJkpMXBDZSywX0hHghGfcUIgm-zBP9UIbnKUYsZpWTKPHPUABtVm30KOevkag3muO6EYVg2wsig1pJWnWJmW7yJLDOgdl-OUyVIvTJ6pw-90v8ztRl5cz72-h8hBG3nS8AtZhcoe8ymFmlrrSzhincucmAVqDXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابعی در جمهوری اسلامی نوشته‌اند که: با میانجی‌گری قطر، آمریکا به شبکه beIN Sports معافیت داده تا مسابقات جام جهانی را در ایران پخش کند.
تاکید هم کردند که: این امتیاز توسط دولت ایران و کاملاً جدا از هرگونه یادداشت تفاهم (MoU) به دست آمده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76249" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/efef15c7c2.mp4?token=rxvZ5PdYyx7F3JbOYnRrPmgu67K2z56FwJmsQury0IPWmyZ34i86eR_Udf84xPAN3eAwqx1TjDg-qBFIFOPI8Fmwz1e2T6DmS6ZCePtZIiCHrnfyhfDwgkKzTawFGb4BjkLeK7oXA94fagL8W9Irck0jU5sBk1CyLIP59BGFOl-csXZoaQh464GT_oTa4Wgw6WCawEcwlYE9T7Z0pj8mDVtGckEM6iheYtCO3btN0ODP4CVEtB7k1BPGkaMMBPIl_EvUW8Ya0yUIiXTymjqn7nI0uQyijrIRHS4ihdqHm6wBqNUk1U6ZEWo09S-JrI-698okzDVwHgqFCZIXJfKfQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/efef15c7c2.mp4?token=rxvZ5PdYyx7F3JbOYnRrPmgu67K2z56FwJmsQury0IPWmyZ34i86eR_Udf84xPAN3eAwqx1TjDg-qBFIFOPI8Fmwz1e2T6DmS6ZCePtZIiCHrnfyhfDwgkKzTawFGb4BjkLeK7oXA94fagL8W9Irck0jU5sBk1CyLIP59BGFOl-csXZoaQh464GT_oTa4Wgw6WCawEcwlYE9T7Z0pj8mDVtGckEM6iheYtCO3btN0ODP4CVEtB7k1BPGkaMMBPIl_EvUW8Ya0yUIiXTymjqn7nI0uQyijrIRHS4ihdqHm6wBqNUk1U6ZEWo09S-JrI-698okzDVwHgqFCZIXJfKfQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات جمهوری اسلامی:
من این افراد را بسیار منطقی‌تر از افرادی می‌دانم که دیگر با ما نیستند. این یک گروه متفاوت است و من فکر می‌کنم گروهی باهوش‌تر است که منطق دارد. همه آنها توافق را تأیید کرده‌اند.
آپدیت:
بعدا ویدیوی طولانی‌تری رو جایگزین کردم که اکانت فارسی وزارت خارجه آمریکا زیرنویس کرده و شامل حرف‌های دیگری هم هست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76248" target="_blank">📅 00:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2For9TcrBxGg-QTyyhz3mPcj-oqnM5dfhKPgHYkIiE8_A5Z4cwl5_P_jFYP1NIV3HdXliMyXva4F4desYp-x8c7k8-xabeySgdUQfi8MQxGa_rywX30nElNrT3WewIU3xJ8-QWBPdG4jtsKLUAfwP2A0apIMX6GFGufP87RHBxz5egtpnJy9oabhtMNWwm_i2J7Q-U6MBZyYx7qKSKCVEe62FIm-u9odG6U94PGgG3AynHEGvA2gNHZneR4q4quGlzEz4xSsUq_zAi4hr2XGYsCLTkheZt9CkgK-IsR5iSuYjktNXq-zsJUKJiBozVUf4mUmHswr2XppHYKUb1SAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی در یک مصاحبه تلفنی گفت علیرغم فعالیت قطر و پاکستان به عنوان میانجی، روند دیپلماتیک مذاکرات به دلیل اقدامات آمریکا تحت تاثیر قرار گرفته است.
اسماعیل بقایی تاکید کرد که بخش عمده متن توافق نهایی شده اما به خاطر مواضع ضدونقیض آمریکا باعث تلاطم و اخلال در دست یافتن به توافق شده است.
سخنگوی وزارت خارجه در این مصاحبه گفت: «ادعاها درباره زمان و مکان توافق صرفا گمانه‌زنی رسانه‌ای است و تا مراجع ذی‌ربط نظام درباره تک‌تک اجزای متن توافق به جمع‌بندی نهایی نرسند صحبت درباره شکل امضا و مکان آن فایده ندارد.»
آقای بقایی اشاره کرد که متن توافق از پیش برای ما روشن بود اما طرف آمریکایی هربار مطالبه غیرمعقولی مطرح می‌کرد و بار دیگر تاکید کرده که ایران تحت فشار و تهدید از مواضع اصولی و خطوط قرمز خود کوتاه نخواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76247" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZKZ9FgazCMI-37vkapYKzBOAQuaFOAlGwQt7UGfgDPgN30fOtFh-IavLwOh1BeaZFHmIF2RmGb03GT6IQnlOEuqWU1i4YtuZwJpSbgImpagyOxC6jv4eDow2nAhPKW2josMPqAhBUhE4TO8PHf5uKqu5BGq1t-jxKi2Ux8Y84jXJiAozYeUy_lXUdrRekh1zOu6A5ZEBb4_gMOzh9igR-CI2sp28au1B8f-zcvw0_ANgDaSSqG_wge3aoe16GmyYhH8WMrwma7r_N8beO1ZPvzdkNce_xYhqz4ry8TDSDer3p5ikJlSBxc_Jn4qL7v9s2nH-xLnfr4sPg7X3q9WCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل طرف تفاهم‌نامه با جمهوری اسلامی نیست
دفتر نخست‌وزیری اسرائیل، اعلام کرد که دونالد ترامپ، رییس‌جمهوری آمریکا، درباره یک یادداشت تفاهم در حال شکل‌گیری با حکومت ایران برای ورود به مذاکرات، با بنیامین نتانیاهو گفت‌وگو کرده است.
این دفتر افزود نتانیاهو از تعهد ترامپ درباره شرایط هر توافق نهایی با ایران ابراز قدردانی کرده، هرچند اسرائیل طرف این تفاهم‌نامه نیست.
دفتر نتانیاهو نوشت تعهد ترامپ شامل این موارد است:
-حذف مواد غنی‌شده
-برچیدن زیرساخت‌های غنی‌سازی
-محدودیت‌های تولید موشک
- توقف حمایت جمهوری اسلامی از گروه‌های نیابتی خود در منطقه
@
VahidOOnLine
به نوشته تایمز اسرائیل دفتر آقای نتانیاهو در بیانیه‌ای که «سعی در کم‌اهمیت جلوه دادن توافق احتمالی» داشت، می‌گوید که آنها درباره «یادداشت تفاهم قریب‌الوقوع با ایران در مورد ورود به مذاکرات» صحبت کردند.
به گفته دفتر آقای نتانیاهو، در این مکالمه، نخست‌وزیر اسرائیل دیدگاه نسبتا خوش‌بینانه‌ای نسبت به توافق ابراز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76246" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=Dkivsi-k6dh4msmJrBqMZC3vEKaLNfBfruHtLEWpwB80ThBjzdaUJGZqdtzm-_llnrEmCPybFLBhsw88Oaipxzt2Pq6z3bxY5B5kwVe0X8O3RVjEgEQ8CwVXBYYPr3IEusGPm-Z2ObyJMf-lofw87wnso1UUCBZ__8quST6bEFeWEIEq3vXlqeOVKcZBtj_woISf_CSYFUgWvFlsleSKqEC47OC9t-grtwJ-RD2-DZLmwBPvcW9_bhYAe7VtvzXJJLLPJHIvX88ARpVd7qFDgvgzkLO_g7NwtTk_-3tgoOoi2e1x6NU4XJhw_RdvGhkcKCpMd5bzsbXTfpuz3sDvNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=Dkivsi-k6dh4msmJrBqMZC3vEKaLNfBfruHtLEWpwB80ThBjzdaUJGZqdtzm-_llnrEmCPybFLBhsw88Oaipxzt2Pq6z3bxY5B5kwVe0X8O3RVjEgEQ8CwVXBYYPr3IEusGPm-Z2ObyJMf-lofw87wnso1UUCBZ__8quST6bEFeWEIEq3vXlqeOVKcZBtj_woISf_CSYFUgWvFlsleSKqEC47OC9t-grtwJ-RD2-DZLmwBPvcW9_bhYAe7VtvzXJJLLPJHIvX88ARpVd7qFDgvgzkLO_g7NwtTk_-3tgoOoi2e1x6NU4XJhw_RdvGhkcKCpMd5bzsbXTfpuz3sDvNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: ضرب‌الاجل شما برای رسیدن از این مرحله به یک توافق نهایی چیست؟
ترامپ: نمی‌خواهم ضرب‌الاجل بگویم چون بعدش می‌گویید من ضرب‌الاجل را رعایت نکردم.
خیلی مهم نخواهد بود چون قرار است امضا شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76245" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=oYIFF-muwj_Lp-QR6HFDcXl_Ya2PWOqUj_vtuV-T1633BZkZhIFBgQV7ItxPHVAww4W1XHn70J-2UWDAC_j_74__7jbKXjAWbDCkzlujZvRdBKbJxeGbUO0h6aT0Bz65AaRhnautOOhjRusR0u8i5qFPF-kxU1aSkd22e1xii3sSqZrJAFCFLTrc60uuF9L7cYZSVRnmwfCT0-SN6bDiIEmZnBfohd1dv2HuIWpFF7tSlw00oFwUhGB2Qs8BkGkMEGOGTZfsg-LutK2dURi9nzokSwY9jER7-a0CZq0Y7lY5C5Ptr78Dq5aOmU4Du4kzvl3cMCAkH2xIs_yl_K8B1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=oYIFF-muwj_Lp-QR6HFDcXl_Ya2PWOqUj_vtuV-T1633BZkZhIFBgQV7ItxPHVAww4W1XHn70J-2UWDAC_j_74__7jbKXjAWbDCkzlujZvRdBKbJxeGbUO0h6aT0Bz65AaRhnautOOhjRusR0u8i5qFPF-kxU1aSkd22e1xii3sSqZrJAFCFLTrc60uuF9L7cYZSVRnmwfCT0-SN6bDiIEmZnBfohd1dv2HuIWpFF7tSlw00oFwUhGB2Qs8BkGkMEGOGTZfsg-LutK2dURi9nzokSwY9jER7-a0CZq0Y7lY5C5Ptr78Dq5aOmU4Du4kzvl3cMCAkH2xIs_yl_K8B1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه باز است. تنگه برای چندین ماه است که باز بوده، اما شما فقط از آن خبر نداشتید.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76244" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=aj17k_hd6XVgqi2fjU_rUKXLnIheaJtwCJL2rMpm9b6vzZnyLyZiYv861qRMHikuO83R8UslLcQrP3I8vtA0CV3NsQxAHX4Qf-AvW0qRqrhMDxYpmsWnPVomx1w2C4Y67IWtGnO-O2fF3F2cgw3Q4PQmKo0INEO68TCKjxw5_gv7ZJ6TTpDncS7jp0cQ9RrDAiknGo57q3KNCiIDHQhOjPfDjWPy-5jnbQIo4RgXm8IVobB1iCPutFnl_mSlGigtwB4ZU0OFSAWxDIk3_DCoN5g_9CI6PAAC1G-8QJrdCIQ3OndYVmSHPrAUBzVsi4jhfxm93IRaryXrUQaxTfx8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=aj17k_hd6XVgqi2fjU_rUKXLnIheaJtwCJL2rMpm9b6vzZnyLyZiYv861qRMHikuO83R8UslLcQrP3I8vtA0CV3NsQxAHX4Qf-AvW0qRqrhMDxYpmsWnPVomx1w2C4Y67IWtGnO-O2fF3F2cgw3Q4PQmKo0INEO68TCKjxw5_gv7ZJ6TTpDncS7jp0cQ9RrDAiknGo57q3KNCiIDHQhOjPfDjWPy-5jnbQIo4RgXm8IVobB1iCPutFnl_mSlGigtwB4ZU0OFSAWxDIk3_DCoN5g_9CI6PAAC1G-8QJrdCIQ3OndYVmSHPrAUBzVsi4jhfxm93IRaryXrUQaxTfx8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما قبلاً گفته‌اید که ایران و آمریکا به توافق نزدیک بوده‌اند. هنوز این اتفاق نیفتاده است. چرا اینقدر مطمئن هستید که این بار متفاوت است؟
ترامپ: چون آنها ضربه سختی را تحمل کرده‌اند. ضربه‌ای که کمتر کسی می‌تواند تحمل کند. و آنها خیلی بیشتر از من می‌خواهند به توافق برسند.
===
خبرنگار نیوزنیشن در کاخ سفید:
از رئیس‌جمهور ترامپ پرسیده شد که آیا می‌تواند این توافق را به سرانجام برساند یا نه، چون پیش‌تر هم به آن نزدیک شده بود. او گفت: «من بسیار مطمئنم.»
او درباره اینکه آیا واقعاً این توافق تا پایان این هفته نهایی می‌شود یا نه، با احتیاط پاسخ داد: «به‌زودی خواهد بود، شاید همین آخر هفته.»
ترامپ در پاسخ به این پرسش که آیا رهبر عالی این توافق را تأیید کرده است، گفت: «برداشت من این است که پاسخ مثبت است.»
KellieMeyerNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76243" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=JmPcDNFxMLn5O-dJyxU1nn6ACz-8EIS7whaP8glfUrbHEFBmaZ3kr42GM8dIONlKExfX6z1INrbYQOLkgeYjdNjwUPpk9fYuTARZIpEjfPS7galfltT-yScC4IH8RMbTTOY9XoJeVK0LKaIMeFl-p384ivFZDKiU7mwvE8w28aMUpicyzFM8vdYdvFX9N04lrt1ZNzxaEsl3T1HKEetH3_D-bAACgatWzO6lYgWDGJ5tgtEJ8BB_iWvYAUteb7Fw8iF22SFwnTKZtNfDBShtWgyulgco8Zb18v0JW8jwrG8p6etJzWwRVc1XFnrSQynCxaUU76k-Q8WXUKTsAycmHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=JmPcDNFxMLn5O-dJyxU1nn6ACz-8EIS7whaP8glfUrbHEFBmaZ3kr42GM8dIONlKExfX6z1INrbYQOLkgeYjdNjwUPpk9fYuTARZIpEjfPS7galfltT-yScC4IH8RMbTTOY9XoJeVK0LKaIMeFl-p384ivFZDKiU7mwvE8w28aMUpicyzFM8vdYdvFX9N04lrt1ZNzxaEsl3T1HKEetH3_D-bAACgatWzO6lYgWDGJ5tgtEJ8BB_iWvYAUteb7Fw8iF22SFwnTKZtNfDBShtWgyulgco8Zb18v0JW8jwrG8p6etJzWwRVc1XFnrSQynCxaUU76k-Q8WXUKTsAycmHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ممکن است آخر هفته در اروپا قراردادی امضا شود. من نمی‌توانم آنجا باشم، اما جی دی ونس آنجا خواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76242" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=lwywyVlJigKg96rJn-l2Ktj1BBODopS_P0TnvAHxbXxlDvk8cUWaRA6aCY-7s4WxSED7ENfxNP2-rRSg5MEDg64llykACGf2B5PZ1qZrQ3xO4-rix-I2PzaiYHUzhVaMTZmpZDVFdnIXTE0AAa1tNB4VhvR62I6nM9bVNB3ZY1_BzlJ0XN1jXpOpDjY8CY3wvPugBY3YdsK2PNXnPkh-5ckPiTQgpl77_WX3LDPYL3iFOeDquLY7FB7Iy-1jz5wmowErPFirCERUfMN7TGttzCIhRhPOJpklSBtiog6FUCKn2tbO7OKiWew2x9U8BFqpYRkF9ZuZ1YoiJmUiG28axw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=lwywyVlJigKg96rJn-l2Ktj1BBODopS_P0TnvAHxbXxlDvk8cUWaRA6aCY-7s4WxSED7ENfxNP2-rRSg5MEDg64llykACGf2B5PZ1qZrQ3xO4-rix-I2PzaiYHUzhVaMTZmpZDVFdnIXTE0AAa1tNB4VhvR62I6nM9bVNB3ZY1_BzlJ0XN1jXpOpDjY8CY3wvPugBY3YdsK2PNXnPkh-5ckPiTQgpl77_WX3LDPYL3iFOeDquLY7FB7Iy-1jz5wmowErPFirCERUfMN7TGttzCIhRhPOJpklSBtiog6FUCKn2tbO7OKiWew2x9U8BFqpYRkF9ZuZ1YoiJmUiG28axw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما به زودی توافق را امضا خواهیم کرد و اسناد تقریباً در مراحل نهایی هستند.
دونالد ترامپ، رئیس‌جمهور آمریکا در تازه‌ترین اظهارنظر در خصوص توافق با ایران گفته است که ایالات متحده «به‌تازگی به یک توافق بزرگ در مورد جنگ با ایران رسیده است.»
او گفته است که «ما در حال نهایی کردن اسناد هستیم. این کار باید طی چند روز آینده انجام شود.»
آقای ترامپ می‌گوید که پس از نهایی شدن اسناد، «احتمالا امضا آن شاید در اروپا» انجام خواهد شد و این کار باید «خیلی سریع» انجام شود.
به گفته او «ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که هدف اصلی از آنچه که ما برای رسیدن به این هدف طی کردیم، همین بود. بنابراین، این یک چیز بسیار بزرگ است.»
رئیس جمهور ایالات متحده تأکید کرد که توافق «به زودی امضا» انجام خواهد شد و اسناد «تقریبا به شکل نهایی هستند، بنابراین خواهیم دید».
آقای ترامپ همچنین گفت تنگه هرمز نیز «به محض اینکه آن را امضا کنیم» باز خواهد شد.
او همچنین می‌گوید که با رهبران منطقه، از جمله متحدان خلیج فارس و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده است و افزود: «تمام خاورمیانه بسیار خوشحال است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76241" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سی‌بی‌اس:
احتمالاً اوایل هفته آینده یادداشت تفاهمی بین ایالات متحده و ایران امضا خواهد شد که راه را برای مذاکرات بیشتر در مورد یک توافق بلندمدت هموار می‌کند.
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76240" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VziLtV-rpY5K7SHT7QZonW3DeDgz71Fj2JtXCe6a0Q6u8HxHz9Nlpi5Hkut5fecGqrxI3nVhjGtgf77Zvz6uygTTTN7dcUmioqsazzEUi3MXmWdRB9L29nQpjIYILJJUTg75Y1wTvuG3bKv3X6iRSlyOIcxSCGbQwGKtBqoACe_h9b7YQi2XrYnaww6v0iWPBLJ2uKA2WahZGtcQ4k-9AP5e0wDHumW7q_Bkz3S0WY_2eLVr15uSJc7Mp3OzZKCnml0Cmnq1H2jiLiBewfo6tYktNN4zgrPLGWLZ10urwgDNDpIMMfmLWZHGp1eRgWiOMk7jpuLFs5S-x8iOL531Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در پستی جدید نوشته:
"بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال تایید این متن در مراجع اصلی‌نظام بالا است‌."
🔄
آپدیت:
خبرگزاری فارس جملات بالا که در انتهای پست نوشته بود رو تغییر داد به:
"البته بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال بررسی مجدد این متن وجود دارد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76239" target="_blank">📅 22:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fqf-lFwGdg_D6lJgHS6pg1ryP1YloIWXagPunoNoTBEY_cNflZqF39RNEPD7hK6UxpytOnlp5S09N2HR1VU_powUeTwrxr62oEgohAxF2lOHyIXz6uSh0JDU-nE9lXHwEUmNbm36ywXIwJk4an1FZPGNXEKcPhd9no_Dislj-34xDp_iGujvNY3PAsB3G9X9-WoUOWotaXQnww1XXewJVdb3jpougB6FKvkzaZtZQhHSK65ei_BHqZF-Tc4yFZ6PufYRLmBBEjnfflHP76K2Kuk7RBjFTRgc2vwejGHLkm5eE1WrEc3sXuneAlu90uZ5F-NEbVAa5EPYoUGxPoME2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث به نقل از یک مقام ارشد گزارش داد هیات قطری که از تهران بازگشت، موافقت جمهوری اسلامی با پیش‌نویس نهایی توافق را اعلام کرد.
همچنین دفتر امیر قطر اعلام کرد که تمیم بن حمد آل ثانی، امیر این کشور، و دونالد ترامپ، رییس‌جمهوری ایالات متحده، پنج‌شنبه در یک تماس تلفنی نتایج رایزنی‌های آمریکا و ایران را که به پیشرفت در تفاهم‌نامه پیشنهادی در چارچوب یک مسیر مذاکراتی منجر شده بود، بررسی کردند.
دفتر امیر قطر در بیانیه‌ای افزود که ترامپ به امیر قطر گفته است تلاش‌ها برای تکمیل مراحل نهایی پیش از اعلام ترتیبات مربوط به امضای یک توافق ادامه دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/76238" target="_blank">📅 22:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیویورک‌تایمز: ‌قبل از لغو حملات برنامه‌ریزی‌شده به ایران در روز پنج‌شنبه، ترامپ با میانجی‌گران پاکستانی صحبت کرد که به او گفتند با ایران «توافقی» دارند.
clashreport
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76237" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NSBFsh3qmPE3J-8zI1KJy430wOHjV2-whQi4EYxgg8Q_P05rm271MGPMtQ3PIEJJImlsbYUWRC2N0dDDPxagJHSO20VzEHk5-sOS0dBbKWGWHuYv_yZ67Z4kzZ9FtaXv6s2xXBkRmFA4KtddhO3hThyeJrCUxPrwE7VY5F_gHE7RPsRxJEBLu5sn2Y6pM_Ba0lgw2yG4A-Ouq9Yd-pq2pcjD2PNug1nguVTm5uMr-yh8IvIKBx1aIzh9GTk7t6tgAG5s-r4HWJwcdQbhv9AqGcbplZ1vw_X5lZQl_bAkZKqyzycaK5HXU319GyDDjqXbOgxcCpCHuhzCDJhhIEsxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع اسرائیلی گزارش داد پست دونالد ترامپ در تروث سوشال درباره نزدیک بودن توافق با تهران، بنیامین نتانیاهو را غافلگیر کرد؛ در حالی که او در میانه یک نشست امنیتی درباره ایران حضور داشت.
سی‌ان‌ان افزود که این کشور از وجود هرگونه توافق قریب‌الوقوع با جمهوری اسلامی یا تایید آن بی‌اطلاع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76236" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n2uxYfbHOJ5HKoM3jm862QYC_j9vQshNogQNlkjdulkZATqIcHsGMS2gkEokgHNadxYzPXaYHEXEeWYahm7ThQ7v2i04RtPzBaxui5q33n_Qa8En4QLAXy1b6DwEjwONIdaMnyPef3olmJQbQNB_05SnirqQGoYMf5I3xMcTklzFGDkEOHsKJ-EDMzmF-Eodrr7Bv2YStr35iWJqb63rIm4zwrpG3TGffVmL7LP5fvZQvw-NkLFHx8XdSGI9McVsRAYo3H_NpmHAWz4Y33o5wO7uf3KM97kWdOTET-U4WfIermMtOgbjkqMJQcR8KURFHUVdmInr1neAm--6qCdSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، ساعتی پس از پیام دونالد ترامپ دربارهٔ مذاکرات با ایران، مدعی شد که «هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تأیید نشده است».
فارس ادعای خود را با استناد به اظهارات «یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران» بیان کرده است.
رئیس‌جمهور آمریکا گفت: «زمان و مکان امضای این توافق به‌زودی اعلام خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76235" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ri8F5LFj69ORlkgMM-Mv9C-dEmG69hBriC_P7ZramKaSghnJ-qSbruR56V7N21BvTtBxrbAToALHdI5HK6xbhgGXhX5IxCAC80BKq_sI6ETwMwPPzl4TLmad7KidHK6c-R-LXuC3YSGL5Mg4-pQUr3oCDp6aiP3LPjBJYGfGmlTLrdCAl1GhwJqigkgQfpIllMg_9vnnOaRBs9DWNYt2U1Qys5ReIuwrrDGMRT2xqdVZUQbcp047eFbFKhUn6zyqGUnr3LFNCRdeKpfmieTolmOJzcxKDbqvkohcxgPXE8TmXUj5zMC3OJ0EnIl9YNhSKZ9kZTH9JAJr7nl3JkHDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه منبع آگاه گزارش داد اختلافات اصلی تهران و واشینگتن برای رسیدن به یک تفاهم‌نامه، چهارشنبه در جریان گفت‌وگو میان مقام‌های جمهوری اسلامی و میانجی‌های قطری برطرف شده است.
بر اساس این گزارش، مقام‌های ایرانی پنج‌شنبه به چند کشور اعلام کرده‌اند مذاکرات تهران به توافقی اصولی منجر شده، اما مجتبی خامنه‌ای باید تایید نهایی را صادر کند.
این منابع خاطرنشان کردند که هم ایرانی‌ها و هم قطری‌ها تاکید کرده‌اند که حملات آمریکا در طول شامگاه چهارشنبه، تردیدهای ایران نسبت به نیت واقعی ترامپ را به شکل قابل توجهی افزایش داده است.
@
VahidOOnLine
ترامپ: توافق تقریبا نهایی شده
ترجمه ماشین:
... نیویورک‌پست نخستین‌بار گزارش داد ایران چهارشنبه‌شب پیش‌نویس نهایی یک توافق را به میانجی‌های قطری ارائه کرده است.
رئیس‌جمهور ترامپ روز پنجشنبه، پس از اعلام اینکه حملات برنامه‌ریزی‌شده علیه ایران را متوقف کرده، به نیویورک‌پست گفت توافقی که مدت‌ها انتظارش می‌رفت برای آغاز مذاکرات هسته‌ای با تهران «تقریباً نهایی شده است».
او در یک تماس تلفنی کوتاه با نیویورک‌پست گفت: «تقریباً همه‌چیز نهایی شده است.»
nypost
سی‌ان‌ان به نقل از یک منبع آگاه گزارش داد مقامات آمریکایی بر این باورند که نشست‌های این هفته میان مقامات ایران و قطر در تهران، به حل برخی از نقاط مبهم و کلیدی باقی‌مانده در توافق با ایالات متحده کمک کرده است. این اختلافات عمدتا شامل جزئیات نحوه پیشبرد مذاکرات آینده در قبال برنامه هسته‌ای ایران و ترتیب زمان‌بندی لغو تحریم‌ها و گشایش‌های مالی برای تهران بوده است.
بر اساس این گزارش، ایران اواسط این هفته جدیدترین پیش‌نویس توافق پیشنهادی خود با آمریکا را از طریق میانجی‌های قطری ارسال کرد. این در حالی است که حدود دو هفته پیش، دونالد ترامپ با اعمال تغییراتی در متن، خواستار سخت‌گیرانه‌تر شدن لحن توافق در بخش هسته‌ای شده بود و از طولانی شدن پاسخ ایران ابراز نارضایتی می‌کرد.
با این وجود، رایزنی‌های این هفته از طریق قطر باعث کاهش شکاف‌ها شد. مقامات آمریکایی در تمام این مدت در تماس مداوم با میانجی‌ها بودند؛ حتی در روزهایی که واشنگتن و تهران به طور پی‌درپی در حال تبادل آتش و حملات نظامی به یکدیگر بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76234" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CtWzlzHEcVB_QLBM9VqFaIBz1-w8uUMOySZNhepYzsvbKhu9tc_M5u3j7fwCjIVCMghR6jP2RIFGeR3c8u8whQ7VXlR3YjKslku1y1rKMgCSWDo9KlyFK_3d_8-18hGxboqKvOqM7zIG0YK8R9pfcO9_phjcU-vKc1nNhmi2i6cEDMYiu2A5ha0aGd7AyLDBE9K4RKD3Kv2R8oVfjHpybR2SaVKTLoltuOVQEUQeO-dHVr9MjzIDZEridWTg2SCh4gmDfNTQTNkRnPuO3iTOUsS4FgmSQ9HWiUqLQILDoJz9IoXcxrGQUq9e8kZpYupp3S6ELSuUt1O910yuRO-qRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله امشب را  لغو کردم چون بالاترین سطح رهبری در جمهوری اسلامی توافق را تایید کرد
پست ترامپ، ترجمه ماشین:
با توجه به این واقعیت که گفت‌وگوها با جمهوری اسلامی ایران به عالی‌ترین سطح رهبری ایران رسانده شده و مورد تأیید قرار گرفته است، من، به‌عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران در شامگاه امروز را لغو کرده‌ام.
گفت‌وگوها و نکات نهایی، هم در کلیات و هم با جزئیات فراوان، به تأیید همه طرف‌های دخیل رسیده است؛ از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران.
محاصره دریایی تا زمانی که این توافق نهایی شود، با تمام قدرت و به‌طور کامل برقرار خواهد ماند — زمان و مکان امضا به‌زودی اعلام خواهد شد.
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76233" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdxWQakusBnd_SKmf4UHcYgVAMqsbOVPafMy9U0GeCkqrfgU8NE7lJsVf7ktWmvHUH_Vh9gC_DipmKyr3YbwJ-VF5SDS9FOu3NlirsiejSRX8kcp_oO7dwYLGF3c7JcdhB3bzOHBnGLN5xw_sHG0oGdXU7UNY5osjRj4sGwNcHNBAM68QaB421sDR6pI5m2NsJ-h5vFnD1dkxEn8zj_A65yFfAY80CR4e0rrMSK4gi8JdtFt7pnlxLwLq3vXU4uplK8XZ3_7nmJNArf8AqeIQ1bxn9As_qISWOqPnfZ9X4jYwKtbKRVtmK3B6MSEnTKX5U9daetSvGHzyVRGAv-aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، در گزارشی اعلام کرد ایستگاه‌های زمینی استارلینک در اسرائیل، قطر، اردن، امارات و عمان به همراه سهامداران شرکت اسپیس‌ایکس و زیرساخت‌های شرکت‌های «الفیظابی» و «مبادله» به فهرست اهداف نظامی جمهوری اسلامی ایران اضافه شده‌اند.
فارس مدعی شد این تصمیم پس از به دست آمدن شواهدی مبنی بر استفاده ارتش‌های آمریکا و اسرائیل از زیرساخت‌های تحت مدیریت ایلان ماسک، از جمله شبکه اینترنت ماهواره‌ای استارلینک، اتخاذ شده است.
بر اساس این گزارش، «ایستگاه‌های زمینی استارلینک» در اسرائیل، قطر، اردن، امارات و عمان، به همراه سهامداران شرکت اسپیس‌ایکس و همچنین زیرساخت‌های شرکت‌های «الفیظابی» و «مبادله» در فهرست جدید اهداف ایران قرار گرفته‌اند.
فارس نوشت: «ایستگاه‌های زمینی استارلینک واقع در اسرائیل، قطر، اردن، امارات و عمان، به همراه سهامداران اسپیس‌ایکس و همچنین زیرساخت‌های دو شرکت الفیظابی و مبادله، از جمله مکان‌های جدید در فهرست اهداف ایران هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76232" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o70ellaA0Fk_faPXwrD__U9KBfBQYPGGfIabv4GGGRoVlfXvApWbBX5PSAezPU3nGLLWtfow4O-XrQAkzQQTO6HRtB0HbJHDV7YVjk52825srvSGsb-OXsNdV_dsMPIwCyKnPewT8T7iRVfK1NGygmxdBTE2a5VXoWTJrI-XNu5KicHKwZgQAaBtYVPj0yOrR_am3uKt9Ap4uxBLB2ZqhwyMU8ZwaDldwtt9gTHksdXD-PyFUObUuieH4LngWoRvLq2fGUncpP7L2WSE04Suyj0TnaPaTFarSl3VSkQcGjOoVVU4c-QdF2Yj2t0-rHhGMJ2WMNOj0H0PRD2YaNd7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع جمهوری اسلامی در بیانیه‌ای اعلام کرد «هرگونه خطای محاسباتی یا تعرض به امنیت و تمامیت ارضی کشور با پاسخی قاطع، پشیمان‌کننده و فراتر از تصور غلط دشمنان مواجه خواهد شد.»
در بخشی از این بیانیه آمده است: «بی‌تردید نیروهای مسلح جمهوری اسلامی امروز از آمادگی، توانمندی و قدرت دفاعی قوی‌تر از گذشته برخوردارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76231" target="_blank">📅 20:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76230">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aHn6a3JSm2aAJqAqVmSoZ_etpRxqBku-TRp-QqDr_sbyvTMQs51xh2LXHYZCprmfjgYGWu0bs-1eiRZNba6wTGNphVPH9IPRdu0H68HmeBRnTFmR5029gkwpOatI72Pi9hJvoTCaDYJkqmY9eRLP8PqeAIT-4rJnzTwydBhGAXoZe9a5obvZu7ePTKGTGLHNkICClK9ilynBcddEFr0LC7ZZHzn4hESeeNb0djL1OD02XXv3pE3ZpySf13AVBg4J30GWKj5R29nXrnoYicS2kB1MqV4EMAfO4-4Irbas4AQxmgaIlMYTDCiWxuVsY12pCrGVxUNPOd7E76BtTtYI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، در خصوص تهدید زیرساخت‌های نفتی ایران از سوی دونالد ترامپ گفت: «یا صادرات نفت و گاز برای همه برقرار خواهد بود یا برای هیچ‌کس امکان‌پذیر نخواهد بود.»
او ادامه داد: «در صورت تکرار حملات آمریکا، پاسخی شدیدتر خواهیم داد و آتش جنگ می‌تواند گسترده‌تر شود.»
فرمانده قرارگاه مرکزی خاتم‌الانبیا اضافه کرد: «تناقض در گفتار و رفتار آمریکا عامل اصلی ناامنی در منطقه است و امنیت تجارت بین‌المللی، به‌ویژه در تنگه هرمز، را به خطر انداخته است.»
او گفت سران آمریکا با «عدم شناخت ملت ایران و نیروهای مسلح» در دور باطل قرار دارند و با جنگ رسانه‌ای نمی‌توانند «شکست‌های پی‌درپی» خود را پنهان کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76230" target="_blank">📅 20:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1ic1MXIVsje76ef43uHieqLXxW3Sj9FHhqvL3yDbOEj2uo7IcMK-UftEGWGlJZoIqvo0yl2JusbvmvLDJZWaGsmeFOEOirTULbu3W8N7jS9RWrEOPzU9r8765ruG4G9hkD64PDxZS1uMqhpfRaholRWw7uiPyHpvBLsym2L6pHDQzUAU6979RrRTyXuOHQajmiVaWz_CK18Xcyt44-XzL4wRCz1Mms9XGfncFtgVlKWA2FGBiJV43ke6uGOVsfxg-oQe_loK8ZcaxNruCrAqRlVyhUDnFzcSkycI8shmXp0IHisJ9a98C7oxZJ4ppJRqrEVRy2VyzClZoD3d8KFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
"تنگه هرمز برای عبور و مرور باز است
مسیرهای امنی برای کشتی‌های تجاری که از تنگه هرمز عبور می‌کنند ایجاد شده است.
این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.
صدها کشتی در دو ماه گذشته از این مسیر عبور کرده‌اند.
نیروهای آمریکا برای دفاع در برابر تجاوز ایران در موضع آمادگی قرار دارند.
ایران کنترل تنگه هرمز را در اختیار ندارد."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76229" target="_blank">📅 20:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=sI5bpJWvHnc_Fs-c1a2jX33XrVSU97V3gJADUe80RfOmVMz_bqwedzDQQj-hfR4AA9ilzafNfXqYi7nnoZNbxlgpNJ8J7gmKc4BLIm-g2G4bBUQM4uGYEsp8p9N_3XkTl55YZUrLEUtZHyndlUsK_NUitVpBH4P6ZdtJgb7NzFG4BXqM81SKemuVvaza3tco4dyx_ko0614Nx2aLocazdDS7D5mEOee4Cd_VrIZgWwppDkf6igZr6aQHclnf-obSPcAcJJxyzPnXRffQShg6A8nU_qLZpe7eLniHQ68vNUsIWHvuMtG3EpQAtcldxql5FlhElGVLIGccGsJESyQGK3eXzG90LCB0oK51NldXhlj6LURhRpfQH05oKz0GDkUdNw8QU3A-Uh7BYrDCSyI_zilHmOKKyvNRhvS6Y8nq-TOesc06pkfZ03B_bpOv2gI7quWxNnfpWM24q_aw8uILCaVKw_2f5JSiqfQPe8BVkTaY8sOoE9v5vnTUo9pOliQ9wio6mzNT47XGN48lc6P1FJjIk6xL-huOpVAuiFlHj4EE5ah6QUT-4TnmXaeN8jhuDLEYpSkm6lCO8C8dxVmZdSbb_CgTjSekrRirQvf4JqV9A3cCkZKh27Lef3mdU2aEjtufsxcfLKYUky3jMkyUT2h4W4JAsotXreK047CMfwY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=sI5bpJWvHnc_Fs-c1a2jX33XrVSU97V3gJADUe80RfOmVMz_bqwedzDQQj-hfR4AA9ilzafNfXqYi7nnoZNbxlgpNJ8J7gmKc4BLIm-g2G4bBUQM4uGYEsp8p9N_3XkTl55YZUrLEUtZHyndlUsK_NUitVpBH4P6ZdtJgb7NzFG4BXqM81SKemuVvaza3tco4dyx_ko0614Nx2aLocazdDS7D5mEOee4Cd_VrIZgWwppDkf6igZr6aQHclnf-obSPcAcJJxyzPnXRffQShg6A8nU_qLZpe7eLniHQ68vNUsIWHvuMtG3EpQAtcldxql5FlhElGVLIGccGsJESyQGK3eXzG90LCB0oK51NldXhlj6LURhRpfQH05oKz0GDkUdNw8QU3A-Uh7BYrDCSyI_zilHmOKKyvNRhvS6Y8nq-TOesc06pkfZ03B_bpOv2gI7quWxNnfpWM24q_aw8uILCaVKw_2f5JSiqfQPe8BVkTaY8sOoE9v5vnTUo9pOliQ9wio6mzNT47XGN48lc6P1FJjIk6xL-huOpVAuiFlHj4EE5ah6QUT-4TnmXaeN8jhuDLEYpSkm6lCO8C8dxVmZdSbb_CgTjSekrRirQvf4JqV9A3cCkZKh27Lef3mdU2aEjtufsxcfLKYUky3jMkyUT2h4W4JAsotXreK047CMfwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما هواپیماها را وسط تهران به پرواز درمی‌آوریم و آن‌ها حتی خبر ندارند. تمام رادارها و پدافندهایشان نابوده شده. آنها تمام شده‌اند... برایشان سخت است چون مغرور هستند. ۴۷ سال قلدر خاورمیانه بوده‌اند...
ویدیوهایی است از
این مصاحبه فاکس‌نیوز
با ترجمه و زیرنویس هوش مصنوعی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76228" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy01zYwzCj9le3yMnGZShuj0CLcn7I67DOJRWnGse8Ng8G0OeZas5428vvUFVZ3jcvaDJXu7ywUdd0GsPHwey4oaUrJQG1CyQK4wFZ2whJUJlAxzb8-xPYIQPUSi8Vk8giJ5vhq0QEksY4cCIQqKLLKBYkNnBy9W30EEjKpWRiGx-iVUDsJNyEs9TsCrrhPshjWMGsBoz5U4EWfEoPEqd49NicHGnWC5121TVCkmNOjrtyK81pLKUFJeg3G5Ex72AUsuTlmUOBrbGfCUi9B1f6M6N_8y8j8jzwb2tfLOKuhk6GbwZdXczmL4_0Ta57ZxiGr6Oty63S6YTfZqqIaOHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ به نقل از «منابع آگاه» گزارش داد که مقام‌های ارشد امنیت ملی امارات متحده عربی و ایران برای نخستین بار از زمان آغاز جنگ آمریکا و اسرائیل علیه تهران، حضوری با یکدیگر دیدار کردند.
این دیدار که در هفته جاری انجام شد، به نوشتهٔ بلومبرگ، نشان‌دهندهٔ چرخشی قابل توجه در رویکرد دو طرف است و در شرایطی صورت می‌گیرد که هر دو کشور بیش از پیش به اهمیت روابط دوجانبه آرام‌تر پی برده‌اند.
این خبرگزاری می‌گوید که منابع آن به‌دلیل حساسیت موضوع نخواستند نامشان فاش شود.
بر اساس این گزارش، رهبران امارات می‌خواهند برنامه‌های بلندپروازانهٔ اقتصادی خود، از جمله سرمایه‌گذاری میلیاردی در افزایش تولید نفت و ایجاد مراکز دادهٔ هوش مصنوعی، بدون اختلال ادامه یابد. این رابطه برای تهران نیز اهمیت دارد، زیرا امارات پیش از آغاز جنگ یکی از بزرگ‌ترین شرکای تجاری تهران و مسیر مهمی برای انتقال نفت تحریم‌شده ایران بود.
به گفتهٔ منابع بلومبرگ، تماس اخیر ابوظبی با ایران عمدتاً با هدف دستیابی به نوعی تنش‌زدایی با حکومتی انجام شده که آن را دشمن می‌داند.
از زمان آغاز جنگ خاورمیانه در ۹ اسفند پارسال، ایران بیش از هر کشور دیگری امارات را هدف حملات خود قرار داده است.
ابوظبی نیز در چندین نوبت پاسخ داده و در میان همسایگان عرب خود تهاجمی‌ترین موضع را در قبال ایران اتخاذ کرده است.
با این حال، به نظر می‌رسد امارات اکنون مسیری مشابه قطر و عربستان سعودی را در پیش گرفته که با وجود هدف قرار گرفتن توسط ایران و نیروهای وابسته آن، در پی کاهش تنش از طریق دیپلماسی هستند.
به نوشتهٔ بلومبرگ، عربستان که تأسیسات انرژی و پایگاه‌های نظامی‌اش هدف قرار گرفته، از اوایل ماه آوریل تماس‌ها با تهران را در سطح وزیران خارجه از سر گرفته است.
قطر که تأسیسات بزرگ گاز طبیعی راس لفان آن هدف حمله قرار گرفت، بیش از همه در پی آشتی بوده و اواخر ماه گذشته میزبان هیأتی از ایران شد و به‌طور فزاینده‌ای به‌عنوان میانجی میان واشینگتن و تهران نقش‌آفرینی می‌کند.
بلومبرگ تأکید کرده که هر سه کشور عربی به ضرورت همزیستی با همسایه‌ای در آن سوی خلیج فارس، با جمعیتی ۹۰ میلیونی و توان نظامی قابل توجه، واقف هستند؛ حتی با وجود خسارات گسترده‌ای که از بمباران آمریکا و اسرائیل متحمل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76227" target="_blank">📅 19:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0U2XyWEvWpkNwnP7UL3TXBmV4lMcOMYmvozGTShqW3YiBncWaVtSNx6qdpDKd0TpL1p2qgh14XOSXALeaCBbt49kTgI8Qw2cG9SnUvhoz8N_Vkgp0hmnmCtK4jDG211l-94X1JJqSO7e3s7h1daRa9rpZSE5ySDez4aBEMYOUgdRK0xIFya6wYfWioDzqQjLho7nQb0i_DcxJUuTzdludYXiwuzoJr-d_ZfvCitYOUwjIT-FaWXvYOeE1s6v3bUMcBSZZafJy4bZvchbNDGAiER60hBMOJN1tYHwQd7Mpbw6GBogUGrAh-Z2DKEKSTtSTenm0-yef9FbWXGysmsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان روز پنجشنبه به نقل از یک مقام ارشد پنتاگون و دو مقام دولت آمریکا اعلام کرد که طرح‌های ارتش ایالات متحده برای تصرف جزیره خارگ در جنوب ایران از «ماه‌ها پیش» تهیه شده، اما به دلیل «بیش از حد پرخطر بودن» کنار گذاشته شده‌اند.
دونالد ترامپ، رئیس‌جمهور آمریکا، ساعتی پیش از تمایل خود برای در اختیار گرفتن این جزیره به عنوان یکی از مهم‌ترین زیرساخت‌های صادرات نفت ایران خبر داد.
سی‌ان‌ان به نقل از مقام‌های آمریکایی نوشت: «دیدگاه غالب در کاخ سفید و پنتاگون این است که تصرف جزیره خارگ یا نابود کردن زیرساخت‌های انرژی این جزیره، عملاً ایران را ورشکسته خواهد کرد و توانایی‌های آن را تا حدی کاهش می‌دهد که دیگر قادر به ادامه جنگ نباشد.»
در عین حال مقام‌های دولتی به رئیس‌جمهور آمریکا گفته‌اند که چنین عملیاتی نیاز به نیروهای زمینی پرشمار خواهد داشت و «ممکن است به تلفات سنگین نیروهای آمریکایی منجر شود».
سی‌ان‌ان ادعا کرده که پنتاگون و کاخ سفید هرگونه اقدام برای تصرف جزیره خارگ را به عنوان یک «گزینه نهایی» در نظر گرفته‌اند؛ اقدامی که به گفته مقام‌های آمریکایی «می‌تواند موازنه جنگ را تغییر دهد، اما هزینه بسیار بالایی خواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76226" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDbGiMLd8yESiX44Wz_tQdi1keYvhg7ScsrZucvOV3cEWJQ9DUBEGPVAF6sCO_xyOcq0uXFg7Vrrt-2MxvYB_kh7BbEWJpPtFo6KOvBBX2S8c5vIlv_MuHvNNcsf9U_FneQyshLiMLjWaaniToKRzE1uBLWZC8JBPOK2wAIRlmI2oU0lMjr5TqGRpW13BFgFKZ20XnD2JjDMX-JYJEIlYeN5SjNICPxm7SzwxayHE90A0SjunMlTQ3vNNn8kG-5gjUy14OE-lvt5umRa-471_w69-s_C_uPgCODAeE3JiK8JIaPsaNvgxnMXaF6qQA7jyta8lKbSKi7mep0uJFKaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
راهبردهای نادرست و تصمیم‌های شتاب‌زده، کل صحنه را به شکلی بدتر از نو تنظیم خواهد کرد، زیرساخت‌ها و بازارهای انرژی را منفجر خواهد کرد و باتلاقی بی‌پایان خواهد ساخت که سال‌ها در آن گرفتار خواهید ماند.
شما با ایرانی متفاوت روبه‌رو خواهید شد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76225" target="_blank">📅 19:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYGCFSPeCijWph1Rfpz8PAVXG4utb1Z-ELw1f5VeFJ69LJfL4Cpo9k3emHqARDtXaooCsNa207vsx_5fT_CXaXer_oV-ybOdF_h7vjyGgCtLYm06WyMUsIgnvstBn45rlfFHU2ldOtZ93ZPBYykMTpNOkSIm1yWpRbRxArs6fOEN7ezlEPN8bs3OsQwjlKXJvjTuYgzDahQniexmoaMYjnnlTZxUANsqkoJyrsI4Iqgr4dLBzdP_1kvzjmBNQh5EO3CyfuM3XjLxKPNa-8UU-wpyEibKrjtNzTpmVYgoWPaSIeCWji41ln5EqzvWS0e_wxXLhUT2zDDj-TOsSazJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آتش‌نشانی و امداد و نجات شهرستان آرلینگتون در شبکه اجتماعی ایکس اعلام کردند که ماموران آتش‌نشانی در حال بررسی حادثه‌ای مربوط به مواد خطرناک (Hazardous Materials) در ساختمان پنتاگون هستند.
شبکه خبری سی‌ان‌ان نیز به نقل از منابع ناشناس گزارش داد که این ساختمان تحت قرنطینه و تدابیر شدید امنیتی قرار گرفته و کارکنان چندین طبقه از آن تخلیه شده‌اند.
در همین حال، سخنگوی پنتاگون در این باره اعلام کرد: «پنتاگون متوجه مشکلی در کیفیت هوای ساختمان شده است که تا زمان تعیین میزان اهمیت و خطر آن، اتخاذ اقدامات پیشگیرانه را ضروری ساخته است.»
او در ادامه افزود: «وزارت دفاع در حال اجرای پروتکل‌های حفاظتی استاندارد است؛ این اقدامات شامل صدور دستور پناه‌گیری در محل (Shelter-in-place) برای بخش‌های آسیب‌دیده ساختمان می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76223" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک صداهایی شنیده شده. گویا بیشتر در غرب تهران
پیام‌های دریافتی:
سلام وحید پونک سردار جنگل همین الان انفجار وحشتناک
۱۸:۲۹ یه صدای وحشتناک سمت پونک اومد
داداش صدا اومد الان، هوا هم ابری نیست، شمال تهران
سلام غرب تهران (صادقیه) ۳تا صدا اومد
توی پونک اشرفی اصفهانی صدای انفجار اومد
صدا میاد شدید ولی هوا صافه
سلام وحید جان
تهران ساعت ۱۸:۲۹
صدای چندین انفجار پشت سر هم
من از محدوده تجریش شنیدم
سلام‌ وحید جان
خیابان جلفا ۲ تا صدای انفجار اومد از دورتر
ساعت ۱۸:۳۰، ۲۱ خرداد
اندرزگو یه صدا خیلی دور اومد
شبیه رعد وبرق ولی ابری نیست
سلام آقا وحید تهران انفجار شد یا توهم زدیم؟
میرداماد همین الان صدای انفجار اومد
سلام وحید جان ساعت ۱۸:۱۷ ما سمت مختاری هستیم اول خیابان ولیعصر صدای انفجار اومد ولی خیلی نزدیک نبود خیلی هم دور نبود
صدای موشک و‌انفجار بود انگار
نمیدونممااا من از صداش خواب بودم خوابش رو دیدم بعدش بیدارشدم صدای انفجار شندیدم
من غرب تهرانم بقیه رو چک کن
سلام وحید جان اگر گزارش صدا از  تهران شنیدی ۹۹٪ رعد و برق هست ابر خیلی کمه مردم فکر میکنند انفجار هستش
آپدیت:
گویا صدای رعد و برق بود.
بلافاصله بعد از انتشار پیام‌های بالا یهو ده‌ها پیام اومد که صدای رعد و برق بود.
آپدیت: حالا بعد از این آپدیت هم شهروندانی دارند عکس می‌فرستند که هوا به این صافی رعد و برق کجا بود.
ولی برداشت نهایی من از اون همه پیام‌هایی که نقل نکردم همون رعد و برقه. آسمون هم همه جا صاف نیست.
آپدیت: بعدش هم برای خیلی‌ها که شک داشتند واضح شد که رعد و برق بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76222" target="_blank">📅 18:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15a23ead45.mp4?token=usUHSXlVsqBEc0QRf-3JbjOex7fykMcZIAKttTmKHYLl-7R6cSTbgN2qERUL67UGGkfI-H1OIcrOjCjW9JHbn_8Rb21YJxDDxcocyqGqu1OdkeU4XfQahfH9jCcpt3pdNq91FP0DFF7n7auOgI3NaFzio8AfZWTrO2pgteab-NNumaGe03edR6J7_fDd3JEDMNtwLVtP5T3hx8WNzYP3pXy62RGvBnwabRlit0oJ4GQwRnJ09Lm77U5xBt2WK_DYMV9QiAcIjiW31XP3EvJkCW0D0js8PoH3OGsE46OHKw4OOXUgZ6hOSlaWpKtamBM0rMh8ir4dlTDQo1H0Frg3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15a23ead45.mp4?token=usUHSXlVsqBEc0QRf-3JbjOex7fykMcZIAKttTmKHYLl-7R6cSTbgN2qERUL67UGGkfI-H1OIcrOjCjW9JHbn_8Rb21YJxDDxcocyqGqu1OdkeU4XfQahfH9jCcpt3pdNq91FP0DFF7n7auOgI3NaFzio8AfZWTrO2pgteab-NNumaGe03edR6J7_fDd3JEDMNtwLVtP5T3hx8WNzYP3pXy62RGvBnwabRlit0oJ4GQwRnJ09Lm77U5xBt2WK_DYMV9QiAcIjiW31XP3EvJkCW0D0js8PoH3OGsE46OHKw4OOXUgZ6hOSlaWpKtamBM0rMh8ir4dlTDQo1H0Frg3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'لحظه انفجار حمله حدود ۴ صبح به پیشوا در استان تهران'
ویدیوی دریافتی، پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76221" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZN4iX1mej5fTJKZ3rvLc7lBl0kcB6z8vAj9-PZ4fSWgaAsxMn_csADqatnF71sKMgDaLHDKnSBL2TTR7hZWjOSRSKiDCcoo1j5m74IEHXpSCwhuai_y2b1Ioq4Edh1MML2B85J7G_gwP87X4G5djuwm6d-JfzRfPPNExUfU1bvCK1qATo_UkEKffl31QCUv9FLKSX0njRyC9SIqN_jlaXjKe4UEV_JGUWDLOZDTYeHjBNCGLCH_cwGhgPg80Z9INtFPAokJnY4NcQAm-yzARbCOxCRvdM9T07iDOvKBkQr8tEgsyUg1tWsTuXFAnLnsp-e5OWKaWyoCXAsxIaBoFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RDDya00e-Z1rxCUvfPdGQytX4NzYikNsmgmizLePcvVfYwX0VeqXrnvW3q0BdBPrdBtosVfwTsHkq9dC2pXX2JahzBURbGEHEULDTeBnbnft3gVFthUGAqlhUTwkXfi6GDtKClQ7ZxdTXqYFpU3NmoM8SG4Dp8NcvRyFTAmVa-QIXEzbZDWElOYcZoZeCYNkjT4WACrw3oN5z4Dh1U0s_0FLR4CCA400_rzbcbr6MsWEW6_2OiOqsKU608BqM2oj6UgqIHfwPVjfdRRSQxwKeD1DBRD24TVgjbHlUB9SO8LY8h_oFgT2JRaDKUlNeSn7sAbijmbVEErJEOxSQ5Mqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tge2OIYVpzv_J15vV7PTQKEvvpM353SFWyUc8w0Dj0XsgCX0qD4_lNQ4dUtzGH79mvOD98JMxei1hZ3BBt52qkxTNoKA6JaRcIFVCnWPkYKK9o2X9oITxSiVUhi9U__6O4aBZOHRkx8CppRBDM2x_f7c0llCMf8pSXVgB8L66zbuYHNT9T4FNf3ZQe3Wd3uMmQes9PvqHRFGTZbZjw98vwB26IyYvjxgpGbbM4ibA4DbOSzjW51mQrjG2pWtHQYQ7UqeQ-eUesGUFmHTYLSukeoZS0COy0SQWKOpPB5o9ZL19uhBq5te4eT3o1ufASs6Kk1WR2b_EwCrboB6yeCxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/caQkeTn1hEu7HSetnl_ppNJP51naWvj1evEAwhE_C5b1_0LbcPwHwoDvEd0ZgAZg4eXwlVuwIj_lZHh7iiS6N9bJPTlR1WR1cShzB0XgAHwnNXDRjianoSWU5ctiz9isOTLXaRVvj6Ccb5M4G497XvhOawUvQqdxx5ouwvSCV7F6Yx_HIKaQ1YYrlbI3rKP6rHa0aqrOJtj2eVQGECZ0VSj8skFErsPYRm0BOBSBMO1yOhM8daerHEEx4ztmpvvANL40sBRK3cw37qWq8TWk0wRAtuYb8ePypIvMCuvOTESn-Q1DEjArfM9R3X7o_tSBNEyh4kQ3OFan523ow1AjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CV7VlqV2ZcbkFA8rKywK0eqvoNdkbkJRMm1bTTlVkGTRiemjX20TT14i2gLcgTR6HoWCl72brAw9N87-gMzGLn-ZnkTDeS98_99J64J3IilssEKYGmQv_WY-_M7wZjXNXOOoNei-UUBG8ln86YrbD60K-6YYDTJ5InFm9MGLfGxtK0xkIOnMDEE4uMV2EKWNapKEmmoQLlp7Ts2vnpuQNHBjyV4R4vzITiMwL5UvA8dRJO2zWXTku7l_L1I0hY8c0bfxdyjHvskYrh0qnzEhsa0PW-tXP0rBQbW8Ac-ck-EyWWRPqIDaH9JVcwRO54Hxbj_Xd5W6J_IK7gd7G6xO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pVf6Ie-rsBV9SJSakUR-8NtNV7IZJOcUCDE7afTXdO1kh1GwBUQ_W2Z_w2TvMiU0UGkzgDN-Q9vvGLbEHhRmWY_bWhtwqWrF3tIp9HH4s-eVaA27tVznzuPeCQwLHMEitV25utTfs9bNYQkBIeUhrz5I_hR2sYS0rtGaPu10079NXV8BbHrEaILd6K6dxiJW9qwWxbvdBOt_bU0cwbc8efriULLJh9vBQCnkUKtbBBKoz4eFSpVFanZoCT9FFo9vAY6X9PqKMZ7UXlmhAHtJkbnjAYPRDHY6RWGLgOOtMIpbunAGXwLrtYPoeoZw6_YHYBIpvYPez54GZIRwAv1fzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4acc6e36de.mp4?token=eeI5Xh7NLR4gRcfDHBx--a3PTC0_6jNZww0Zic9aMeqq-rzAvbZe00Z0kLZtfBRN2qIAeuc7zLqZKgu9799Yo-Ytv9av2jlYEqXSaGLIRhGYfuPAXbWY-4dP8xyBr6u6u99Oid6mWCnYrWVu_FAZAORXIwmH-PUWb8dkV7mWaEbyjsiNCqwBL36oIHLOfQ7tKVBHtnFjFCPeiVuDdsPFiOTiQhN7ri1idRkm6lopi0ZmuUpY2xzrrqAnpySe5qWw7vQ7yKmzYl6-63c4tPCxTtVB9_nnbDMKC5msv4Wo-qd2q_tph8gGiRFIrUG_M1ynSlP5SF1AACPAvvwBKhEv7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4acc6e36de.mp4?token=eeI5Xh7NLR4gRcfDHBx--a3PTC0_6jNZww0Zic9aMeqq-rzAvbZe00Z0kLZtfBRN2qIAeuc7zLqZKgu9799Yo-Ytv9av2jlYEqXSaGLIRhGYfuPAXbWY-4dP8xyBr6u6u99Oid6mWCnYrWVu_FAZAORXIwmH-PUWb8dkV7mWaEbyjsiNCqwBL36oIHLOfQ7tKVBHtnFjFCPeiVuDdsPFiOTiQhN7ri1idRkm6lopi0ZmuUpY2xzrrqAnpySe5qWw7vQ7yKmzYl6-63c4tPCxTtVB9_nnbDMKC5msv4Wo-qd2q_tph8gGiRFIrUG_M1ynSlP5SF1AACPAvvwBKhEv7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری آمریکا دقایقی بعد از انتشار
این پست
در برنامه صبحگاهی شبکه خبری فاکس حاضر شد و درباره این پست و تنش‌های جاری و فزاینده میان ایالات متحده و جمهوری اسلامی توضیح داد.
🔻
«ترجیح من تصرف خارک است»
او در این گفت‌وگو تاکید کرد که شامگاه پنج‌شنبه حملاتی شدیدتر از شامگاه چهارشنبه، ۲۰ خرداد در انتظار حکومت ایران خواهد بود.
او با اعلام اینکه در حملات چهارشنبه «۲۵۰ میلیون دلار» بمب بر ایران ریخته شد، افزود: «آنها [حکومت ایران] واقعا در حال تسلیم شدن‌اند، فقط هنوز خودشان این را نمی‌دانند.»
او هم‌زمان گفت واشینگتن همچنان با تهران در حال گفت‌وگو است.
ترامپ در پاسخ به پرسش مجری برنامه درباره تصرف بخش‌هایی از ایران گفت ترجیح او «تصرف جزیره خارک» است، اما تردید دارد که افکار عمومی آمریکا آمادگی پذیرش چنین اقدامی را داشته باشد.
او افزود: «با این کار ثروت هنگفتی به دست خواهیم آورد، اما فکر می‌کنم مردم آمریکا دوست دارند ببینند ما به خانه برمی‌گردیم.»
ترامپ در ادامه تصرف خارک و تاسیسات نفتی ایران را با تجربه ونزوئلا مقایسه کرد و گفت آمریکا «میلیون‌ها و میلیون‌ها بشکه نفت» از آن کشور خارج و به پالایشگاه‌هایی در هیوستون، لوئیزیانا و دیگر نقاط منتقل کرده است؛ پالایشگاه‌هایی که به گفته او «شبانه‌روزی کار می‌کنند و ثروت هنگفتی به دست می‌آورند».
ترامپ گفت از اجرای همین الگو در مورد ایران نیز استقبال می‌کند، اما مطمئن نیست «کشور آمادگی آن را داشته باشد».
🔻
«اکنون تمایل کمتری به توافق دارم»
ترامپ همچنین گفت اکنون نسبت به سه یا چهار هفته پیش، تمایل کمتری به دستیابی به توافق با جمهوری اسلامی دارد.
او افزود: «نمی‌دانم آمریکا آمادگی انجام کاری را که من واقعا ترجیح می‌دهم انجام دهم، داشته باشد.»
در بخش دیگری از گفت‌وگو، مجری فاکس‌نیوز از ترامپ پرسید آیا از جمهوری اسلامی عصبانی است؟ او پاسخ داد: «من عصبانی نیستم. من عصبانی نمی‌شوم.»
او درباره توافق هسته‌ای مورد نظر خود گفت: «توافق من راهی به سوی نداشتن سلاح هسته‌ای است.»
ترامپ افزود که ایران نباید اجازه داشته باشد سلاح هسته‌ای «توسعه دهد یا خریداری کند» و گفت در متن توافق پیشنهادی او، هر دو مورد گنجانده شده و حکومت ایران نیز با آن موافقت کرده است.
ترامپ همچنین مدعی شد «کار حکومت ایران تمام است» و افزود: «آنها دیگر نیروی دریایی، نیروی هوایی و پدافند هوایی ندارند.»
او همچنین اشاره کرد که هواپیماهای آمریکایی بر فراز مرکز تهران پرواز می‌کنند و مقام‌های جمهوری اسلامی «اصلا نمی‌دانند ما آنجا هستیم».
به‌گفته ترامپ، آمریکا همه رادارها و سامانه‌های پدافند هوایی جمهوری اسلامی، بخش زیادی از موشک‌ها و بیشتر پرتابگرهای موشکی حکومت را از کار انداخته و توان پهپادی آنها نیز «به‌شدت کاهش یافته است».
🔻
«نمی‌خواهم نیروگاه‌های برق آسیب ببینند»
در ادامه، وقتی مجری برنامه از احتمال هدف قرار دادن یک نیروگاه برق پرسید، ترامپ گفت: «بله احتمال دارد، اما ترجیح می‌دهم این کار را نکنم، چون وقتی چنین کاری می‌کنید، مردم رنج می‌برند.»
او همچنین درباره تاسیسات آب گفت قطع آب «ضربه‌ای ویرانگر» برای مردم ایران خواهد بود و افزود: «می‌توانم در یک دقیقه بگویم آن را از کار بیندازند، اما مشکل این است که مردم دیگر نمی‌توانند آب بنوشند.»
ترامپ در بخش پایانی این مصاحبه کوتاه گفت مردم ایران از اعتراض می‌ترسند، زیرا به گفته او «سلاح ندارند» و طرف مقابل مسلح است. او بار دیگر طی ماه‌های گذشته به کشتار گسترده مردم در اعتراض‌های دی‌ماه اشاره کرد و گفت نیروهای حکومت ایران به معترضان شلیک می‌کنند و وقتی مردم با مسلسل یا تک‌تیرانداز مواجه باشند، برگزاری تجمع دشوار است.
او اظهار کرد جمهوری اسلامی دست‌کم «۴۰ تا ۵۰ هزار نفر» را کشته است و افزود نمی‌توان مردم ایران را به دلیل ترس از اعتراض سرزنش کرد.
🔻
«از کردها ناامید شدم»
رییس‌جمهوری ایالات متحده در ادامه گفت آمریکا برای مردم ایران سلاح فرستاده بود، اما از کردها «بسیار ناامید» شده است.
او افزود با تحویل سلاح به کردها مخالف بوده و باور داشته است کردها این سلاح‌ها را تحویل نخواهند داد.
ترامپ گفت: «فکر می‌کنم آنها سلاح‌ها را برای خودشان نگه داشتند. این مایه ننگ است و من این را به یاد خواهم داشت.»
گروه‌های کرد مخالف جمهوری اسلامی، از جمله حزب دموکرات کردستان، حزب کومله کردستان ایران، حزب کومله زحمتکشان و حزب آزادی کردستان (پاک) در هفته‌های گذشته دریافت سلاح از آمریکا را تکذیب کرده‌اند
.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76214" target="_blank">📅 17:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76213">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apQVv5VMxcj18ohz9sCV32Y4uF02g3xj_WDsWM8XA2qN8I0LVHTXINwWbgiVb3KfwgzUVsN0AejjCTb5ryKDXBd6mjjbwj70ausHh2R_fKIo31iGrl6b8IFd86N96P-usPJ46kN9cAuF-C7JhJ66Qq_Kx7UH9EY7Ur4rFiZx__UxuycJir0bsKECb4rKsfVyFhWZLHwhoUwWDeqGXrkSpFxzIA_BOgeSgroS_u1wblxOZPb3epw_9hnNLA6Ybx3LAn5pGAkfJ2dxYNlZ2sv1YHS6bVafQP078hQ9RGvYAEk5w_ndyKVhTajgP33bBXoyTXetiIsOzvc8OJuoPPOaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسکات بسنت»، وزیر دارایی ایالات متحده، در شبکه ایکس نوشت که جمهوری اسلامی ایران در «بازی با حاصل جمع صفر» شکست خواهد خورد.
بسنت در این پست توضیح دادکه خساراتی که حملات موشکی و پهپادی جمهوری اسلامی به کشورهای عربی به‌عنوان «متحدان آمریکا در خلیج فارس» وارد می‌کند از محل دارایی‌های بلوکه شده در آمریکا برداشت خواهد شد.
وزیر دارایی آمریکا همچنین نوشت که هرگونه عوارضی که از کشتی‌ها برای عبور از تنگه هرمز دریافت شود، با برداشت از حساب‌های ایران جبران خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76213" target="_blank">📅 17:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmrFXpgYBVtuRlDcBQ1DlYypoL_P3OgJScjULyKijPoOIXZXeTYcq9ukpDjbb_59eFi0ZvusMPaVivlOfcG58Ms9-GSddS8sZbXSeOVWEe4RY8_0m7UFRvTxu88aW7BnuxyjP9pW7CFIGSxickbCmS0DjX6gR5_NhsRKg_XKJRhQVsaNIOfn9ixYbPERWIg7ttO4ma1_VU6kyi1O1Uy4AGlIR--AG-z95JiTZzP5uRqjQkt--oun5jGQUrafyIs7V8lP8pzoVo_nYKt47dUx-UCmBOyyoCAlnBsobj-RrBemk7TqPnleMUE8g3jbrkZ2H1awYZ3l0VDfUKCm18TjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز پنجشنبه اعلام کرد که ارتش این کشور امشب بار دیگر ایران را به سختی مورد حمله قرار خواهد داد و از برنامه ایالات متحده برای به دست آوردن کنترل جزیره خارگ ایران خبر داد.
دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروث سوشال نوشت: «ایالات متحده امشب ضربات بسیار سختی به ایران وارد خواهد کرد؛ کشوری که نیروی دریایی، نیروی هوایی، سامانه‌های راداری، پدافند ضدهوایی و تمامی دیگر اشکال دفاعی آن، به همراه بخش عمده توان تهاجمی‌اش، از بین رفته‌اند!»
آقای ترامپ در ادامه پیام خود نوشت: «در مقطعی در آینده‌ای نه‌چندان دور، ما جزیره خارگ و دیگر زیرساخت‌های نفتی را در اختیار خواهیم گرفت و کنترل کامل بازارهای نفت و گاز ایران را به دست خواهیم آورد؛ همان‌گونه که در مورد ونزوئلا انجام داده‌ایم، اقدامی که نتایج فوق‌العاده‌ای هم برای ونزوئلا و هم برای ایالات متحده آمریکا داشته است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76212" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj4LoyFPJb5x0WHSvuoTnUiyNQxDtsScY_kGD5h36q0OwiBIWXdcQ7gI9yVANbl81l4T_HRR0jBsq4gQyTvMy4D9rpSjtzQcTxOaRMtZIplWNLcx5nhr8oR3yx6-AL1nK5zWm3R61Q28LGOLK5Cs_UpR1TFYw0O1JlyyTkiv7CK3iu2s5t7RsCooXdHsI96hcz6KVEzrK0WkYeXA5pywSpJIorxwiorTTekI4FY5W_GSPQ7ZtJTPZwWgBw1VHcxTeNeFLvBv5qAqyuRRYjTvjkeTE5qXRqXpo4IwI0eARO5e_0Ey8uPyjblSyS2Ff3nBvjdLaP2t3eGrTDGCaBAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان ملل متحد، آنتونیو گوترش، در پیامی تازه درباره وضعیت خاورمیانه هشدار داد که این منطقه «هر روز بیشتر به سمت بحران عمیق‌تر کشیده می‌شود» و تأکید کرد پیامدهای آن فراتر از مرزهای منطقه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76211" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFgZo-s4VNbCxbESWifPdCUUdiDLRcRJPPnvqSzHSFE49fj2bQf-yewBxSqHwkXULTKSsayxR2g-vTn4DRY8q2XettvVi-Vnab7MxfD3veo-SXuBAoDT2Rm_7enMujdnwnq5CTNV-7ff74-GAfQEDDPny4DvRgk-U4Tge1uqIB0c9W72t-A82aT28xN0K0Qo4wMZj4HZqHc1vVBwI1-QrUBoIM_QIzzwUSjAIi-D5m1DYrtdge4LFkM88ydC0qOnhOgQIjhRrY43cVB1O7pQNJytOC2iDVM4JYHwmvM1l_HBAfLc8_xNQ-hjWxOleJ1eOw6xXY9Dqgh6uj00hxdRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی با صدور بیانیه‌ای در واکنش به حملات ارتش آمریکا به اهدافی در ایران، این اقدام را نقض قوانین بین‌المللی خوانده و گفته است این حملات آتش‌بس ۱۹ فروردین را عملا بی‌معنی کرده است.
در بیانیه وزارت خارجه ایران بار دیگر به کشورهای حاشیه خلیج‌فارس درباره استفاده ارتش آمریکا از قلمرو، امکانات و منابع آنها هشدار داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76210" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d46260783d.mp4?token=I-k8GMfSiLsyDmYCQ94h2i-8pT4iTDWSUo3s1u8Kt6DlD8SkUXLIau_hLhsLjUpkSjmR1aE9UQNReYI2XdHxFFy-eURqy2B4oz6gKZIUzizBnyD0XPxrpTovuFcm5nwxypF6emL8URkzl5EiJMInZg3wLrKI97Rp-Mxjoga4fk26yLkaHQsd2Tb-I7c3tj2vigrMjKjnWvjhPXOJMvroZQ99rpsfv0zNNyLiIb4tg8-NeSFlYUFgCOT2epJPMHhdcnQaQ_DXw_cik73vPLa3XFSdyIZp4u9yVAKrgxPjASjM2UG0_SleCDGMRBJXCbyRxm85MkFrhEUxSi4Gj_p1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d46260783d.mp4?token=I-k8GMfSiLsyDmYCQ94h2i-8pT4iTDWSUo3s1u8Kt6DlD8SkUXLIau_hLhsLjUpkSjmR1aE9UQNReYI2XdHxFFy-eURqy2B4oz6gKZIUzizBnyD0XPxrpTovuFcm5nwxypF6emL8URkzl5EiJMInZg3wLrKI97Rp-Mxjoga4fk26yLkaHQsd2Tb-I7c3tj2vigrMjKjnWvjhPXOJMvroZQ99rpsfv0zNNyLiIb4tg8-NeSFlYUFgCOT2epJPMHhdcnQaQ_DXw_cik73vPLa3XFSdyIZp4u9yVAKrgxPjASjM2UG0_SleCDGMRBJXCbyRxm85MkFrhEUxSi4Gj_p1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا سومین نفتکش ناقض محاصره را در خلیج عمان از کار انداختند
تامپا، فلوریدا — نیروهای آمریکا ساعت ۱۱:۲۰ شب به وقت شرق آمریکا در ۱۰ ژوئن، پس از آنکه یک نفتکش با تلاش برای انتقال نفت ایران محاصره علیه ایران را نقض کرد، این شناور را در خلیج عمان از کار انداختند. این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی از کار انداخته می‌شود.
فرماندهی مرکزی آمریکا، سنتکام، علیه نفتکش
M/T Jalveer
با پرچم گینه بیسائو اقدام کرد؛ این کشتی در تلاش بود نفت را از ایران از مسیر خلیج عمان منتقل کند. یک هواپیمای آمریکایی پس از آنکه خدمه کشتی بارها از اجرای دستورهای نیروهای آمریکایی سر باز زدند، دو موشک هلفایر به اتاق موتور کشتی شلیک کرد.
اوایل این هفته، هواپیماهای آمریکایی به‌ترتیب در روزهای دوشنبه و سه‌شنبه دو کشتی با پرچم پالائو، یعنی
M/T Marivex
و
M/T Settebello
، را از کار انداختند. مارویکس با تلاش برای حرکت به‌سوی یک بندر ایرانی محاصره را نقض کرد و ستبِلو نیز تلاش داشت نفت ایران را منتقل کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام ۹ شناور نافرمان را از کار انداخته‌اند، ۱۳۵ کشتی را که از دستورها پیروی کردند تغییر مسیر داده‌اند و اجازه عبور به ۴۲ شناور حامل کمک‌های بشردوستانه داده‌اند.
این محاصره به‌طور بی‌طرفانه علیه شناورهای همه کشورها که وارد بنادر و مناطق ساحلی ایران می‌شوند یا از آن‌ها خارج می‌شوند، اجرا می‌شود؛ از جمله همه بنادر ایران در «خلیج [فارس]» و خلیج عمان.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76209" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76208">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQc6fvuye4yNXI3zQKc0xigjloj6ttBruxd9v2qqq3g79vfEY9KlGt3k59CMXLEaLJekgvLPH8tIimy05Utw6131GAoF2THVYvhXrZwgWqbv8eI2Ellewv_wVVHXiA_X2ALNhnU4l71tHGS3LYCRRIf6-rZ5D7bKnqHcgC_7KL4aTDqOQvJV2KbaFS_V6s-qjX9UgxgQjWZI6OYQatGxpUT54cTvEkp2z7V7eKtGbIoh525KpLXNpk_PUMOQLSKEkrDcD1ccJ9yMyz7c16aTwqTP-td2P7ehMJhJKY92_vrq_y40tfXpDO5oHx7WuhkfF-R3GvVp71NdB8jkL_6_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرحیم سلیمانی اردستانی، عضو مجمع مدرسین و محققین حوزه علمیه قم، توسط دادگاه ویژه روحانیت به شش سال حبس، خلع لباس روحانیت و پرداخت جزای نقدی محکوم شد.
نزدیکان آقای سلیمانی اردستانی اعلام کردند که وی تنها به شرط برگزاری دادگاه علنی حاضر به اعتراض به این حکم است و در غیر اینصورت، حکم را بدون اعتراض می‌پذیرد.
او به اتهاماتی چون توهین به مقدسات، توهین به علی و مجتبی خامنه‌ای، توهین به مقدسات تشیع، توهین به مراجع دینی و هتک حیثیت روحانیت شیعه متهم شده است.
سلیمانی اردستانی در فروردین ماه توسط نیروهای امنیتی بازداشت و به زندان ساحلی قم منتقل شد.
او پیش از بازداشت و در تحلیل نخستین پیام مجتبی خامنه‌ای که به تجلیل از علی خامنه‌ای پرداخته بود، نوشت: «مهم‌ترین هنر والد شما این بود که مخالفان و منتقدان خود را بی‌بصیرت یا مزدور بیگانگان می‌خواند و هر برخوردی را با آنان روا می‌دانست! از صفات اخلاقی ایشان دو صفت لجبازی و کینه‌توزی را بسیار برجسته یافتم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76208" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rki0tgNVr0oNS5YZm0ti7xhIG9PI3nrADBf-K0GJw1XdvS6ldI49ODtsUFIP81u8DS9yRgJvlBbeuwK09Um6DUuUY6DHJWitqP2dmYFnMTuW_xAgCU5jZvAmi6K9_AyNh0TeR-hQQAGhGbs_dwLpUpIeFfUtFjKuSBHYNmvJvFNXs2e3pxWgc_8_BMsUEXydturqLrcOWfc-fytMitvR_lDoTDwm5Lb2wW0qM8cNN8srT6GHIBzgT9zqimk88BYYusC2p5W5hFAwFAr-DjGq6TUUUJ8YcKLx3SirETp1kJ5psliEuCy-g6pqTfGxtkzz9z8qVSYN8_XMk0xHCUwzcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی از پیشوا در جنوب شرق استان تهران
'دود انفجار حمله حدود ساعت ۴ صبح که در ورامین و پاکدشت هم احساس شد.'
پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 502K · <a href="https://t.me/VahidOnline/76207" target="_blank">📅 06:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/769901b74f.mp4?token=Z6FMig3OH4tfdHB9tftxgR_mkxbY84Ug5318L-cAWCazwg_41kfIZGGWMvRXk2SEJCNJdM6AGLwGY5JYbJ9pV8J_guMiTRTYBluqNvw-V4av2KVsz0WpsGPcO3wIpOrX8b0WjOviBcky_Y32QgVFRIQH-tYxf9qJ_5Ths_KqlqwbsHivZld1l1LEESFgE_2u3zET_ni0kVE89URYT18V_GIYVMxSYRWYWZEQV53XjezBssXw5PJo9Y0NHCx8g-Y8RKyjMOGR_qIDBR-U0tBAA0Af8c73vq2w4To56nIwMKZCB0t-j7Yf-o0QSyIXu38RkR9nHQC11AgM4hlc4OPUiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/769901b74f.mp4?token=Z6FMig3OH4tfdHB9tftxgR_mkxbY84Ug5318L-cAWCazwg_41kfIZGGWMvRXk2SEJCNJdM6AGLwGY5JYbJ9pV8J_guMiTRTYBluqNvw-V4av2KVsz0WpsGPcO3wIpOrX8b0WjOviBcky_Y32QgVFRIQH-tYxf9qJ_5Ths_KqlqwbsHivZld1l1LEESFgE_2u3zET_ni0kVE89URYT18V_GIYVMxSYRWYWZEQV53XjezBssXw5PJo9Y0NHCx8g-Y8RKyjMOGR_qIDBR-U0tBAA0Af8c73vq2w4To56nIwMKZCB0t-j7Yf-o0QSyIXu38RkR9nHQC11AgM4hlc4OPUiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'نور یکی از انفجارهای حملات بامداد پنج‌شنبه به استان البرز'
ویدیوی دریافتی: 'فردیس کرج، ساعت حدود ۴' پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 480K · <a href="https://t.me/VahidOnline/76206" target="_blank">📅 06:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T1eyIdOoHSom1VMosWyxPrLKkuhNs6nkMxEV39JONyGsHnoSEScIgVULCU0nKGs8L3dsc8Eo2c8m-iTCmXcniixnXdRLmvgNJlOtUvNClDpecfGKARdr9D3w2cIJPPGm8kG931jqb3PhysYGnX8wSeosSc4dd4KT5XxeI-z_7ywsK_5hV-izhP5bJPBkctuvzQP5jtsHi2APZiojrJwfJA0iYKLeobECXZyZc9OtAe-hZNr-17QcoWmyZLJYzIzORmkEiymEyuwifd4vvEWoGSrykqoLU8BpDF5z-YaasImS0XzrDLdTzk3LoJUUmQq0kvNoiAZa_TE6iKZaeB5FnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RpXmRGqIlWJNiNoAoodaCLeTPM1ZKk3qmTD7SkiYyE3swBziLsXGeb2gDISz2EK7iHiIV4KQpT8482C0Kn_d_jsVLevDCjsmAOxAY4hhXqAsssqTiQtEZbD-7dRn5ZQ5KCvVMQzlaE83GTDTZMjYRO1GAnba2u-MbskOIvTY0fRjBj3DlPAaqqks2XH_MhRorgacpTwQajY31zixjNPUs58gGtF909S5h6Hq_0j5ae84L7C71pI0Er9-UFyPXkaeHViy5GgSJ9caWhvxEuZx7Utuws1L9QpsJ65VPBpMfQ22mFhAUiRzFKuctKtfELVgUPQdqkq5WPFnbiJ7S11MZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ADiAWNAbbvlkIMtorSJ7jOp--kD6dbZ24A1p_of8qwOenra_DXOeS7zFz9vd3IfOCmyRwZDwzd1mfBA7jGUnBIyGCOyz4rVvof6Zl0NNbCFHs-yDCHnpHvr2XFVdOMA78VHNqCN1xw7hw-LcwwMnqhyIXVRuzitEJrJgGQnvss-zr3AkJHkyuBRBbDJ-b1-Zi4H7ACmc3JaX1QxXdt31UlmvbxsLMkwXvCt8urqPSMgtwISYB6tvmz23HCSUdQQ88GEvRbraDRYCqBo7q4fSa1zFIDFQG8OhAI0YpbMqRUo4eBWslA0AE8-s_rsEoAoQy6GGk8w75ZHNj8SCr3Ojzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cLW2pE-IF3pwqAYlQDFLdWFZ4vqUk3fqhmyY1Z9J_Szb4epwEdhEy9rlXl6pJUClFrkvUKKN_xaJT7aj5bBGzuDBSGbI9bC-nWmLnDSVyUM9ZyL-IDWRZn38ng6WHhpKjJHdbQyKxqMWeMdV2L603I450dlMlJmVDCICB3IDoW9AfvO4zla73iGypjdbl-l7JdCbHZuvOl4YiqgXp3KhMGRUj-zMFtGRuQHIgZpGxP7vP422nFiV_2YFoZ0fTTZfAcCmGgqpR4eF3LlwClwdo-UPVsf7yD2CjyXZKjKeS0FyirGSt_3MGeY7M4W2L30KtlcCoD5kmxq2URGbP5jaEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e891de921.mp4?token=FIUHOM1x2uZ08QFA0_7qVZNZTDA92GQNRMdzxK1GWA_o_xFois-buGNcy1w0H7DjpqWvfxdCE2oVKVsAHFS0etxybFAE3XyuMhM-ilz1ZOWwFYGaDx125C-QacuZVU7ntdMlhkpjrtqovJWSHWNNSo_HFVgovN9cSQTk74qlbMdJUH1Hufxi13vm4Ds2DD_5kQzu1kCgr9QDsBAsuu4faHeL4xLaq0J2LCJLSU0LrsfP96e7jeU12NxJLwRWYLwI1irJ8qQbdtqJCjxf1MRSGPY-ziwAqZzCwpaHgKQUVRvcCWb3vAYxmjsZZBXHDbhD3jZh6Br7jo569rn5a7APew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e891de921.mp4?token=FIUHOM1x2uZ08QFA0_7qVZNZTDA92GQNRMdzxK1GWA_o_xFois-buGNcy1w0H7DjpqWvfxdCE2oVKVsAHFS0etxybFAE3XyuMhM-ilz1ZOWwFYGaDx125C-QacuZVU7ntdMlhkpjrtqovJWSHWNNSo_HFVgovN9cSQTk74qlbMdJUH1Hufxi13vm4Ds2DD_5kQzu1kCgr9QDsBAsuu4faHeL4xLaq0J2LCJLSU0LrsfP96e7jeU12NxJLwRWYLwI1irJ8qQbdtqJCjxf1MRSGPY-ziwAqZzCwpaHgKQUVRvcCWb3vAYxmjsZZBXHDbhD3jZh6Br7jo569rn5a7APew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دود انفجارهای حملات آمریکا به غرب استان البرز و
#کرج
تصاویر دریافتی از  حوالی "حصارک"، "کمال‌شهر"، "مسیر کرج به قزوین" و...
بامداد پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/76198" target="_blank">📅 06:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gGY3te2pDidSBjhGvXDNJPqucgTVE7_bmoiJsrCPYWJm6XVESektwD5FLGU5qr3PG8jLl3hXzrsi9gLENFbcbSFaG5pX5-ahuVzEvwVcl0ewu2dUAwSIl3x2DUJGafQbCC1v0Ws7_GfKg-MZ6_NkOAZZnOmnkDLNLKBU1wUJHZEV6UlXtArScD8dzMBoncO29D4OiAcyNVSNq9h1_CTQoZvK6BOOl8_k17r3B0SsScPw-E7UTdMfhChKR7_CTU-BgRwDxhCUFHGu7vDTIJzCe_jrq-x60N8yVtRSdObDbfaX3aj3dprcgr5iPcfiN5hzIsvRwWz-_dMxGNb89YKMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح : شلیک موشک از استان اصفهان ۶:۰۳ پنج‌شنبه ۲۱ خرداد
آژیر هشدار حمله هوایی در بحرین صبح پنج شنبه برای بار دوم به صدا در آمد. ویدیوهای منتشر شده در شبکه‌های اجتماعی شلیک موشک از چند استان در ایران را نشان می‌دهد.
@
VahidHeadline
ارتش کویت بامداد پنجشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور در حال رهگیری اهداف «متخاصم» هستند.
پیش‌تر روابط عمومی سپاه از حمله به اهداف مرتبط با آمریکا در کویت خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/76197" target="_blank">📅 06:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76196">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/863187a248.mp4?token=c3AeylIQlD-AeOdrRS2OIPAs9rC-NVu1rIt89aC2dVFwtvhiHyEpzhmbfl4J6DZIOBivCAgJyfxSPkoC5XncEaeggxTYp-GkYjRm7rRqH4uE0dTycuQofQFOfh4613XPoF3sTMwPAzLdTv9TkPaTTzTrC5sDRlKe2s65MIATcLgPIx3e_Ou1WnMdf0uoYoiyRvo05zRrJpqr2Mp8ZWQ0DNWto_mCEwRXBIZrARTMGEDLsWlaDwKCFgL_6msE-nfayQNraMUyenTPTjOd7qJZeAba-8ZrsEBK0rBz_4LjtXJ-1yVy5F1DMhNecATP1lLQ0gDJjO-U_KuVTkPLz-Dt7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/863187a248.mp4?token=c3AeylIQlD-AeOdrRS2OIPAs9rC-NVu1rIt89aC2dVFwtvhiHyEpzhmbfl4J6DZIOBivCAgJyfxSPkoC5XncEaeggxTYp-GkYjRm7rRqH4uE0dTycuQofQFOfh4613XPoF3sTMwPAzLdTv9TkPaTTzTrC5sDRlKe2s65MIATcLgPIx3e_Ou1WnMdf0uoYoiyRvo05zRrJpqr2Mp8ZWQ0DNWto_mCEwRXBIZrARTMGEDLsWlaDwKCFgL_6msE-nfayQNraMUyenTPTjOd7qJZeAba-8ZrsEBK0rBz_4LjtXJ-1yVy5F1DMhNecATP1lLQ0gDJjO-U_KuVTkPLz-Dt7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'موشک‌های شلیک شده از استان
#زنجان
'
ویدیوی دریافتی، پنجشنبه ۲۱ خراد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/76196" target="_blank">📅 05:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76195">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ce876bdc1.mp4?token=qYpzNcubQZL3ci6Yno2Sk2w-38nJo1RIxtEICQCcr799mllD8zDcV-4wjp-Ah9XiE0WUPqbIGmTH5l8EsN3LmvGfvjQrHGNmZZYqPLskXRS22RTckowZI3KVcxM7ZcqzFH6atH4QUjPCwEXwky1MoqIxLubh2C2K09nl42XnPiovA_7tiBi76_OlO3eFqHH-5eaHx3tz179Kh45KR54rRemWPa-kV11ya9epCqsiKOX5tHNLpUmxEYcDqT3CRaT5skJwboOmla4J4qb8EqhkO7kSIfpE2z3BFm3iGF3dFR5-QuR0MF5zHg3vqaF4aDAxAv_h1UVZS5VEND9EqD2-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ce876bdc1.mp4?token=qYpzNcubQZL3ci6Yno2Sk2w-38nJo1RIxtEICQCcr799mllD8zDcV-4wjp-Ah9XiE0WUPqbIGmTH5l8EsN3LmvGfvjQrHGNmZZYqPLskXRS22RTckowZI3KVcxM7ZcqzFH6atH4QUjPCwEXwky1MoqIxLubh2C2K09nl42XnPiovA_7tiBi76_OlO3eFqHH-5eaHx3tz179Kh45KR54rRemWPa-kV11ya9epCqsiKOX5tHNLpUmxEYcDqT3CRaT5skJwboOmla4J4qb8EqhkO7kSIfpE2z3BFm3iGF3dFR5-QuR0MF5zHg3vqaF4aDAxAv_h1UVZS5VEND9EqD2-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان تبریز
ویدیوی دریافتی: عبور یک موشک از میان رد موشک‌های قبلی
پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76195" target="_blank">📅 05:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76194">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/056cecd324.mp4?token=BItNybLs1FO5SVzKpdvKKf16IhqaxU61LzPSGbzGWHBj1wh-4rV9xYiMo0PxcQ5_BTI5FcKvwMsousSSMU4Q5dRymBieLQDKs6M_2iZEl6ezWZkMeHtgYOWQAUSxbFV2vmx58Q4OwHM37_v32_MsURSRTM82l1YtdTBay42L_LCtbWSES0Myy2Gy_nkhLxRrzQxxj1ptU7-FGVrNFDVZgK8Wp2RWKPu-9qFkWwiNVmvAypqYl6P1PhwPcrEP0on_iY55HxtdRlOJ9EV098GpRhzswdXL2F-_djHh05uA5RGIkupMuRG3QVXdWWZIdEXeyohObeN4E0ORDd4VT-mQfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/056cecd324.mp4?token=BItNybLs1FO5SVzKpdvKKf16IhqaxU61LzPSGbzGWHBj1wh-4rV9xYiMo0PxcQ5_BTI5FcKvwMsousSSMU4Q5dRymBieLQDKs6M_2iZEl6ezWZkMeHtgYOWQAUSxbFV2vmx58Q4OwHM37_v32_MsURSRTM82l1YtdTBay42L_LCtbWSES0Myy2Gy_nkhLxRrzQxxj1ptU7-FGVrNFDVZgK8Wp2RWKPu-9qFkWwiNVmvAypqYl6P1PhwPcrEP0on_iY55HxtdRlOJ9EV098GpRhzswdXL2F-_djHh05uA5RGIkupMuRG3QVXdWWZIdEXeyohObeN4E0ORDd4VT-mQfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: رد موشک شلیک‌شده در آسمان ارومیه
پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76194" target="_blank">📅 05:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62d2ba90a6.mp4?token=gRKsglRE3c17JQX5VOGzZ4ew6NWknobpVMFUAmCr5N7MUZlT8MJ71k4Y3pa9Iy9BhemggkBN-ZMVEYRLKJoCqOeBJliP6vZoEKsckIDuOjdMmX6_wD7dkgGvwOEPHXATJAFckyE-Dtm1KJSdD_yilZojpB3Ep9Ul6iUbxbv482Zzp07fBR5ofNWBsdHYKUUjG2FS0t38PhIPY9TxBrAKfe4m38xNZG-Bo_nZyP4AOJ0PFETUUZTiph7nc3BuT-6dPQ5ZdRcM3rPq8rKvZxi-znVRe_A6gTj2ptn7qlS5avhudGKP7h8SVqEdVQbtHf7UZTr1gDpKKwWuLQScttVcvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62d2ba90a6.mp4?token=gRKsglRE3c17JQX5VOGzZ4ew6NWknobpVMFUAmCr5N7MUZlT8MJ71k4Y3pa9Iy9BhemggkBN-ZMVEYRLKJoCqOeBJliP6vZoEKsckIDuOjdMmX6_wD7dkgGvwOEPHXATJAFckyE-Dtm1KJSdD_yilZojpB3Ep9Ul6iUbxbv482Zzp07fBR5ofNWBsdHYKUUjG2FS0t38PhIPY9TxBrAKfe4m38xNZG-Bo_nZyP4AOJ0PFETUUZTiph7nc3BuT-6dPQ5ZdRcM3rPq8rKvZxi-znVRe_A6gTj2ptn7qlS5avhudGKP7h8SVqEdVQbtHf7UZTr1gDpKKwWuLQScttVcvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک از استان زنجان
ویدیوی دریافتی پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76193" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JpN7Tg7pLmuozBll90HY14cKnm-H-HnKgOPzQ1Lkie_UNN_KTAAbQWBoW_oZn15EaToC0STx8r8IxB2GMzqb8aFex8Qxt4v2ji6TLPRHJknU5OwUP4U7bWZ4hn7mlpmuo_IpOtAwqJ5-gmVkuzK51QrAnepVq-2EXSHJskL_ivBL-ggG0-18MLgh76XuLA_uTpbZuS39TL_vxrqwWFHIA8f4L0O4oV5Cbi2s_ixbi0zApJ-xAZO_IDq1CKL1YYcW0vmepupAa2ntFKpko9-b-yarsG8M8lFXR23wAIoaeEoac2RX0LXJ06qNbVOoQ2KCneNn-FWuiq3D7MNVBcvLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ra4fuv2BXAEgxi9wFbWqJEC72B_79WmRVADBnlgYe7Xz4DiDbryetsENp3mXJR_cvTT84dmg9CZYzkuCakvr56rr0ELf12H9rg5jcrBz-8yk7pik248v5TV0-Q4hQoBHU97dPlCG1eXNz9ddHK1qiLYqJjYaNGpErYGSLgIosAQsiiH6n1aQfJI42JFsxe1WDc2SwliUH2zEWlLcHPKmHVVhJNIH0picAhKqlWrgn7fXenfrbP0mFOXVUNnRkR3NnyUxhGIhiGiYppgjhxVbSHeRREYms5afauHk6FbiliF4KdOsL1T7DhmI_H3lVENrx8Vx7-9u2ND7VPNJAta-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A7FaXDiTClx9hil_zfXEDSNjnC-MCoiCRNzYjcenyn_qpVxSNf15xhtkj5FopCmkqU6okyzQUJljWl9q0ZA6EWVv0M17DQR63ymNH3zCTNd998fIxlwi9jKCuc21xQsu6rQ-JysV1D1e_Jyb32iehRGSQeEwfaynrzTANOlGpCfdZsgQDV7npvNH-MB6AQQn3ssNM6nUlokkBgA85afcjDLfGAdV5SLVNvUZNxqSMqUOprWM9H-XJoBHkuYpoLuVMsYKEfw_10yVdwyXUvpR7ULSUeY9W9piJ3ynWldhJwOWPObyjNKS9haEEVrvoo0LluS1m7tgqX3kI_YqwBFzdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلیک موشک از زنجان، تبریز و ارومیه
الان از شبستر تبریز سه تا موشک زدن نمیدونم به کجا
صداش خیلی زیاد بود
الان یدونه دیگه زد
سلام 5:16
همین الان تبریز صدای انفجار قوی اومد
از ارومیه موشک بلند کردن
5.18 ارومیه  صدای 4 - 5 انفجار
سلام وحید جان تو ارومیه ساعت ۵.۱۷ چهار بار صدای انفجار شدید اومد
هنوزم ادامه داره
3 تا دیگه زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76190" target="_blank">📅 05:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQUVcY6i19XhQzV7y_UtkOgdTqpBG1Vd3TY_kR13pA3rY4pjj4khiNG-T9Fmug_D_8rgiSbWEq9M6w5x9y7K-blaRrJw3VZJK0JkcWEtyCOBISO3Xje_qZRWmGBCLLFfr-sf7bhCyEXEiFJKsWvLDxEKVILvglHq-YM5wvO8Jr454RMrNoaLo7y4BrviS2yAatObC5YSfzNTtI8gcCcTcLtQ2sWxDst9PqdGl0JtR89YxE0YPt2MSY4YrPDER9w-U0DjsXHYw0M91p_XlphYNFlDcrGYqRrkMoyyaEbMB3oEv7Yif9gu2emG_uEdTUxLn7Qf9eNIqytAxWgk9yZ6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
ساعتی بعد از حملات بامداد پنجشنبه آمریکا، خبرگزاری‌های رسمی به نقل از ارتش جمهوری اسلامی ایران نوشتند: «ناوگان پنجم آمریکا در بحرین، آماج حملات پهپادی ارتش، قرار گرفت. در این موج از حملات پهپادی ارتش، آنتن‌های ارتباطی و تاسیسات راداری سامانه پاتریوت ناوگان پنجم مورد هدف قرار گرفت.»یییی
همزمان وزارت کشور بحرین در پیامی در شبکه اجتماعی ایکس از ساکنان خواست تا با حفظ آرامش به نزدیک‌ترین مکان امن بروند.
سپاه پاسداران از حمله به« ۱۸ موضع نیروهای آمریکا» در منطقه خبر داده است.
کانال تلگرامی سپاه نیوز نوشت که طی «دو موج عملیاتی ۱۸ هدف مهم» متعلق به ارتش امریکا در پایگاه‌های هوایی «علی السالم» و «احمدالجابر» و همچنین پایگاه‌های هوایی «شیخ عیسی» را هدف قرار داده و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76189" target="_blank">📅 05:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76188">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C9PzYuGI9YiFUGUP_9XR7JGRFnhBO7QrOElYie31i5GY1Zt6tBfxtf7JxKzu9EHUddQI9VUvVAO8kQQWWYjWtBZ9wyxfrcdLYbmA286mDTfUGl0qMpRMGCo6n1vkSnSpjbfpGrxz1G6gAWfuM_0drKstHkhWd21m2XbK1Krm771emx7S-PpvKHxTPgKLhdrA_BDa7C-WFOQoZOKjPYRl_cJIOLZn8bRxI7MOIGrT8PfE56i-Nf-zZlYY_T6lv967n-sXyMjitgSraXfbVagiH3CuE-hV43AYKAmUZQTlmEbLx0LhQSTA3FDedEKvi7scY4XOGbcUn6eJ0FpNHwcoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ گزارش داد که اسرائیل در حمله نخستین ساعات بامداد پنجشنبه به اهدافی در جنوب ایران مشارکت نداشت اما به‌طور حتم ارتش اسرائیل در سطح آمادگی بالا قرار دارد. او در عین حال گفت که آمریکا بیش از ۵۰ هزار نیرو در منطقه دارد که بسیاری از آنها در عملیات مشارکت داشتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76188" target="_blank">📅 05:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c67229aee8.mp4?token=LulGys0FGdAvwH1Y3NSLffPv_tA3SYdRxPeZk3LEySroKTw2SoyExi9h33XaCPp4b00iY1siCq4mUkjFz0IEV3vW-B0w6ar66mAvn3AaMXH4l2Q9mkB8X-gGE-7KH7dHsxqU6T-h1h1eJPtfVTIDzHuuWQsNnYkwiHUreXp8wdO3WhYK3yX6UmgNviET2m9s0IoSJDqWfCFCSvpIiJiKhm8yt_oTWQa_updnBXw9gj0HkAHw167Drt-z9M_9N3OoAC2QDbqUGdqewOKPkT-xmmli5et5Wk6la6gcp0kJIk1YE1aCsS27KJ9W-VfTCUN_2KoBW1eiyc-3HgKCzOTTbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c67229aee8.mp4?token=LulGys0FGdAvwH1Y3NSLffPv_tA3SYdRxPeZk3LEySroKTw2SoyExi9h33XaCPp4b00iY1siCq4mUkjFz0IEV3vW-B0w6ar66mAvn3AaMXH4l2Q9mkB8X-gGE-7KH7dHsxqU6T-h1h1eJPtfVTIDzHuuWQsNnYkwiHUreXp8wdO3WhYK3yX6UmgNviET2m9s0IoSJDqWfCFCSvpIiJiKhm8yt_oTWQa_updnBXw9gj0HkAHw167Drt-z9M_9N3OoAC2QDbqUGdqewOKPkT-xmmli5et5Wk6la6gcp0kJIk1YE1aCsS27KJ9W-VfTCUN_2KoBW1eiyc-3HgKCzOTTbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام: نیروهای آمریکا تازه‌ترین حملات در ایران را تکمیل کردند
ترجمه ماشین:
"تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا، سنتکام، روز ۱۰ ژوئن، به دستور فرمانده کل قوا، حملات دفاعیِ بیشتری را علیه چندین هدف در ایران تکمیل کردند.
نیروهای سنتکام حملاتی را علیه توانایی‌های نظارت نظامی ایران، سامانه‌های ارتباطی و سایت‌های پدافند هوایی در سراسر ایران انجام دادند. تجهیزات و نیروهای سپاه تفنگداران دریایی، نیروی هوایی و نیروی دریایی آمریکا مهمات هدایت‌شونده دقیق را به سوی اهداف ایرانی شلیک کردند؛ اهدافی که تهدیدی برای نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی در حال عبور از آب‌های منطقه‌ای محسوب می‌شدند.
این حملات در پاسخ به تجاوز بی‌دلیل و ادامه‌دار ایران انجام شده است. نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده هستند."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76187" target="_blank">📅 04:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پیام‌های دریافتی:
درود صدای انفجار در شهر کنگان ۴:۱۷
شهر کنگان صدای انفجار
کنگانو زدن ۴:۱۸
سلام شهر کنگان در جنوب کشور صدای انفجار
کنگان رو زدن
سلام.
کنگانوووو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76186" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76185">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یک صدای دیگه از کرج همین الان ساعت ۴:۱۰
سلام وحید
یکی دیگه الان
همین الان دوباره کرج
ساعت ۴:۱۰، انفجار دوباره
۴ده دیقه کرج کمالشهر
وحید صدا های جدید ساعت ۴ و ۱۰
ساعت ۴:۱۰ یه تک انفجار دیگه گلشهر کرج
صدای انفجار خیلی بلند و طولانی بود
ساعت ٤:١٠ دقيقه باز صداي انفجار هشتگرد شنيده شد
مهرشهر کرج ساعت ۴:۱۰ صدای انفجار
همین الان ۴:۱۰ گلشهر مهرشهر
دوباره صدای انفجار خیلی شدید به همرذه لرزش زمین
سلام وحید جان کرج دوباره صدای انفجار همین الان ۴:۱۱ دقیقه
و کلی پیام مشابه دیگر که نقل نمی‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76185" target="_blank">📅 04:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سلام از پیشوا صدای دوتا انفجار شدید
ساعت 4:۰۶ ورامین
۲ تا صدای انفجار
سلام آقا وحید، ساعت ۴:۰۶ صبح پیشوا ورامین صدای دو تا انفجار اومد و مثل اینکه سپاه پیشوا رو زدن
الان ساعت ۴:۰۵ دقیقه نزدیک پاکدشت دوتا صدای انفجار اومد
ساعت 4.5سپاه پیشوا
وحید جان ورامین همین الان صدای دو تا انفجار اومد
سلام وحید جان ورامین دوتا انفجار پشت هم ساعت ۰۴:۰۶ دقیقه
ورامین 2 تا انفجار خونه لرزید همین الان ساعت 4.8
همین الان دوتا صدای انفجار شدید داشتیم ولی مشخص نیست کجا رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76184" target="_blank">📅 04:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
بندرعباس همین الان ساعت 4:06 صدای انفجار نسبتا شدیدی اومدی
سلام وحید
بندرعباس رو الان زد
صدای انفجار شدید
صدای انفجار بندرعباس
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
سلام مجدد ٠٤:٠٥ دقيقه بندر دو صداي انفجار اومد
٠٤:٠٧ دو صداي ديگه مجددد بندرعباس
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
بندرعباس همین الان ساعت 4:06 صدای انفجار نسبتا شدیدی اومدی
سلام خوب هستین من بندرعباس زندگی میکنم ساعت 4:6 دقیقه صبح دوتا انفجار مهیب پشت سر همدیگه صداهاش به گوشمون میرسه
داداش وحید بندرعباس همین الان زدن
دوتا انفجار به فاصله یک دقیقه سمت دریا
۴:۰۶ یه انفجار دیگه قشم احساس شد
همین الان بندرعباس چند تا انفجار پشت سر هم شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76183" target="_blank">📅 04:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی از شنیده شدن صدای انفجار در کرج
آپدیت: میگن شد ۶ تا انفجار
کرج صدای انفجار 3:53
ساعت ۳:۵۳ کرج انفجار
الان باز صدای موشک اومد
۳:۵۳ وحشتناک بود خیلی بد بود و هنوز صدا میاد
درود کرج ساعت ۳:۵۳ صدای انفجار شدید
کرج شاهین ویلا همین الان یه صدای مهیب انفجار اومد
سلام، همین الان ۳:۵۲ انفجار شدید، کرج، ما باغستانیم خیلی واضح بود
سلام وحید ساعت سه و ۵۳ یه انفجار خیلی شدید ( گلشهر کرج )
۱ موشک دیگه ترکید
وحشتناک لرزیدیم
بازم داره میزنه
وحید سمت ساوجبلاغ ۲تا صدا خفن دوباره اومد
خیلی شدید بود نمیدونم کجاست ولی  نظرآباد میلرزه دوتا انفجار شدید فکر کنم آبیک بوده
بازم داره میزنه سمت هشتگردو ساعت۳:۵۵
علاوه بر اون اون پنج تا انفجار قبلی الان صدای دو تا انفجار دیگه اومد ساعت 3:53 آیبلاق
انفجار در کرج سمت فرودگاه پیام
وحید جان من مهرشهر کرجم الان یه صدای انفجار مهیب اومد
سلام نظرابادم
دوتا صدا انفجار وحشتناک اومد از سمت کرج
بازم زدن همین الان۳:۵۵
کرج ۳.۵۴ انفجار شدید
کرج جهانشهر صدای انفجار ۰۳:۵۵
تک انفجار شدید اطراف شهر کرج همین الان ساعت ۳:۵۴ شنیده شد
فردیس کرج هم صدای خیلی بلند اومد و شیشه ها تکون خورد
همین الان فردیس کرج صدای دو انفجار شنیده شد
۳.۵۳ هشتگرد بازم ۴ انفجار دیگه اینبار نزدیک تر بود درای خونه لرزید
سومین انفجار ۳:۵۶
سومین انفجار تو کرج
سه انفجار وحشتناک توی کرج همین الان!
گوهردشت ۳ تا انفجار خیلی بلند شنیدیم
شلیک موشک اینا نبود
انفجار بود
ما مهرشهر هستیم صدا خیلی بلند بود در حدی که خونه لرزید
چهار انفجار به فاصله یک دقیقه از هم فوق‌العاده مهیب ساعت ۳:۵۵ اطراف جنوب کرج. همه پریدن از خواب. لرزش عجیب و غریب. امتداد صدای انفجار شاید ۱۰ ثانیه طول کشید. مثل پژواک صدای رعد. تا به حال چنین تجربه‌ای نداشتیم
وحید نظراباد صدا از دور پشت هم میاد ولی شدید خونه میلرزه
سلام آقا وحید سمت باغستان کرج سه تا صدای انفجار آمده و ساختمون لرزیده
۳ تا صدای انفجار خیلی نزدیک اومد
کرج باغستان
شیشه های ما لرزید
ساعت ۳:۵۶اطراف هشتگرد نظراباد بدجوری دارن میکوبن
سلام از فردیس پیام میدم اینجا الان یه صدای وحشتناک اومد
دوباره هم یه صدا اومد ولی اینبار دورتر بود ۳:۵۷
سلام آقا وحید. من شهرک بنفشه زندگی میکنم و ۵ دقیقه پیش صدای چندتا انفجار شدید اومد
صدای سه تا انفجار با فاصله یکی دو دقیقه در کرج، ساعت ۳:۵۲ بامداد
وحید جان چند صدای مهیب در مهرشهر کرج الان.
۴ صبح . مهرشهر کرج . صدای انفجار میاد
سلام وحید جان ساعت ۳:۵۴ و ۳:۵۶ صدای انفجار و لرزش محدوده ساوجبلاغ البرز، مشخص بود از طرف کرج عه
یه جوری فرودگاه پیام رو زدن سه متر از خواب پریدم هوا
وحید شهرک بعثت کرجم ۴ تا صدای انفجار خیلی زیاد اومد
ولی صدای جنگنده نیومد اصلا
خیلی موجش شدید بود
3/59دقیقه فرودگاه پیام و زدن
همین الان صدای انفجار شدید اومد
بعدش ده‌ها پیام مشابه دیگر اومد که دیگه نقل نمی‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76182" target="_blank">📅 03:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام دریافتی از شهروندی با سابقه اخبار درست:
"دو انفجار. نیروی دریایی سپاه سیریک"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76181" target="_blank">📅 03:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پست خبرگزاری سپاهی تسنیم:
۱۸ هدف مهم متعلق به ارتش شرور امریکا طی دو موج عملیاتی مورد هدف قرار گرفتند
روابط عمومی سپاه:
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
رزمندگان شجاع نیروی هوافضا و قهرمانان نیروی دریایی سپاه سحرگاه امروز در تنبیه متجاوز و پاسخ به تعرض ارتش کودک کش آمریکا به بعضی از واحدهای خدماتی و پاسگاه های ساحلی سپاه و فرماندهی انتظامی و محوط فرودگاه بندرعباس طی دو موج عملیاتی
هجده هدف مهم متعلق به ارتش شرور امریکا در پایگاه های هوایی علی السالم و احمدالجابر و همچنین پایگاه های هوایی شیخ عیسی
را مورد اصابت قرار داده و منهدم کردند
وَمَا النَّصرُ إِلّا مِن عِندِ اللَّهِ العَزيزِ الحَكيمِ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76180" target="_blank">📅 03:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های دریافتی از حوالی غرب استان البرز و شرق استان قزوین
من سمت ساوجبلاغ کرجم
ده دقیقه صدای موشک اومد
الان صدای پنج انفجار اومد ۳:۳۲
سلام همین الان ساعت ۳:۳۳صبح اطراف هشتگرد صدای اتفجار و موج میاد
سلام ۶ بار سمت نظرآباد البرز رو زدن
ساعت ۳.۳۴
۲۱ خرداد
ساعت۳:۳۰
شهر جدید هشتگرد
۶/۷ تا انفجار پشت هم
اما خیلی دوره
نمیدونم کرجه یا تهران
ابیک قزوین ساعت ۳:۳۴
بامداد ۲۱ خرداد
صدای و موج انفجار اومد، به نظر میاد از سمت کرج یا هشتگرد باشه
۵-۶ تا بود حداقل
۳:۳۰ صدای ۵ تا انفجاد اومد از اطراف هشتگرد بود فکر کنم قشنگ شنیدم
سلام وحید نظراباد از دور صدا ۷.۸ تا موشک پشت هم اومد در های خونه لرزید
هشتگرد ۵ صدای انفجار از طرف اشتهارد
سلام وحید جان ساعت ۳.۳۳ صدای ۱۰ تا انفجار شدید اومد من نظرآبادم ولی صدا از دور بود
پشت هم موشک داره میاد با نور انفجار و صدای مهیب
محدوده نظر اباد هشتگرد
از پشت بوم کاملا مشخصه
سلاممم کرج هشتگرد 4تا صدای انفجار شدید اومد
دوتاش خیلی بزرگ بود بطوری ک کل خانواده از خواب پریدن
قشنگ کل خونه لرزید
۵ ۶ تا صدای انفجار هشتگرد جدید ساعت ۳:۲۰
سلام وحید جان
۶ بار صدای انفجار مهیب اطراف اشتهارد شنیدیم‌ از حدود ساعت ۳:۲۰ تا ۳:۳۵
نزدیک چهار یا پنج تا انفجار اومد از سمت آبیک اطراف ساعت ۳:۴۵ خیلی مهیب بودن
سلام وحید جان ما سهیلیه کرج هستیم بد جور لرزیدیم
۷ تا ۸ تا صدا انفجار بود سمت سهیلیه کرج‌کامل لرزید،
سلام ماهم اطراف آبیک قزوین هستیم ساعت ۳:۳۵ حدود پنج تا انفجار شنیدیم اما دور بود ازمون
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76179" target="_blank">📅 03:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SIQUPHzV-2omzSv6btpCnuCMC1N9M_-5c6-y9Qw5Q1iIJQx-CyD0R0F6OOYRZN02VaZe57XEoQLkOVNTwT6vyQkId6inoDAlm0Y9hOZNTUIFa1MGlp3TsPToFe4z2PBVM8FYfl2ttMF-qs05DKiBoQto0lxyvY11rGu-jSUJJV23YP-8UfcUnnCTmpwAwSERe1bhI376500q4UVzTHaCrfHvj6GgaAgu2nX2NWckLkRn0lDjYosdtUFCIrxy_icROGuB_XHK5zaZ3MgE1L7VBOu9G_g64yxMBr34VtqYMDE9nqagO0QrRk_ZJKqoh9vLa0MjLpt9wtxoEj3v_P2reQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما به نقل از یک مقام ارشد جمهوری اسلامی اعلام کرد اظهارات ترامپ درباره تماس او با مقامات ایرانی دروغ است.
این مقام افزود: این اظهارات پوششی برای فرار از جنگ علیه جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76178" target="_blank">📅 03:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YIqd4PcAkU8yFIvG_ZpqWGoN1DCA20j97F6n-R_IRnbmVYEW7SZNbLfrBF_5WujYpTQqMy-J-UMhi6jxIpf51U0BbhuGa4yYLna9Po41_KTSZ9NtI18aczIjK_nlrdMaMiFziURcNdrOHG5QaUTXflJH6D6v_idOBwQXXqePqjK44eXq1kJpYPOGCV7NgVXQLWJbFfVG7_iKgE8sf8TT9Xd3Xg2Lg4G_fhgwVIKVJc19HlCvWujc7uYbSla0zquLDRWscaavnLBFIxUMlEd4SyXPyZaghwMYUz171FPDz0BEm2rj26Np0Ey257qzQAi5-qtbwLglDaAGrFZxlJ9XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌‌‌های اکانت فرماندهی مرکزی ایالات متحده، سنتکام
ترجمه ماشین:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران مدعی شده است که تنگه هرمز بسته شده است.
✅
واقعیت:
کشتی‌های تجاری امشب همچنان در حال عبور و مرور به داخل و خارج از تنگه هرمز هستند.
CENTCOM
🚫
ادعا: منابع رسانه‌ای ایران مدعی‌اند که ایران به یک ناو جنگی آمریکا در تنگه هرمز حمله کرده است. نادرست است.
✅
واقعیت: هیچ ناو جنگی آمریکایی هدف قرار نگرفته است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76177" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7fTFWXNs0L5pk1-zUi2lkEmnIlObr_vD4s3nn1y5Cch2PWG2vG1OJn0BDL78aGDr3Qv86mN-5WwCM8__eI_TMsGVnZXUvvkPC0RL7CLFCwKgtMuVyUtKEootUgpIX326GwG4MwD1ts574R-kdre8abmpSTCrRXc9NKNfXzj2MrimMDPFrLcTfu0phPZv7IDsFdj6fzGMo7ziJHM3CgWwhjgPWoswlVGuZ8ohoIFsnECBdxY7CvuDs87iHx1BcPbu5GiNfldbt0nYbriUAEJfvjxPtRPxS6qD7poKwcnTwqZA19oL3FK_lPq3_UsvbhXOJm80YlDFKOu-ug_sqRLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: مقامات ایرانی در تماس مستقیم خواستند بمباران متوقف شود
پست خبرنگار فاکس‌نیوز، ترجمه ماشین:
امشب با پرزیدنت ترامپ صحبت کردم؛ در حالی که او از اتاق وضعیت، حملات نظامی آمریکا علیه ایران را زیر نظر داشت.
رئیس‌جمهور به من گفت که امشب مستقیماً با مقام‌های ایرانی صحبت کرده است؛ مقام‌هایی که از او خواسته‌اند بمباران را متوقف کند.
در زمان گفت‌وگوی ما،
ایالات متحده ۴۹ موشک تاماهاوک شلیک کرده بود و جنگنده‌ها نیز در حال بمباران بودند.
نزدیک‌ترین هدف به تهران حدود ۴۰ مایل [۶۴ کیلومتر] بیرون از شهر بود.
ترامپ افزود که
بمباران به‌زودی متوقف خواهد شد، اما اگر آن‌ها توافق را امضا نکنند، «تا سر حد نابودی بمبارانشان می‌کنیم.»
پرزیدنت ترامپ این را
نقض‌شده‌ترین آتش‌بس در تاریخ جهان
خواند.
جی‌دی ونس، معاون رئیس‌جمهور، به من گفت که ایالات متحده در روند مذاکرات، هم با صداهای میانه‌رو و هم با صداهای تندروتر در ایران سروکار دارد.
به‌روزرسانی‌های بیشتر در فاکس‌نیوز منتشر خواهد شد.
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76176" target="_blank">📅 03:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfKxzpUs1nANGv4oFpXEcOziW-k3tK6d_awTOAysSLjsc0UhaNMdXv_y78SShYrukwb-7GrvPMG6stRYhyRMkJerCtXIIN-noEH0WNT2ezLl5qsqBjcRgCr_q8A0byxjduCADooV2azsESWnoyAOPzAGxKEiGoWeFRYQAoXKJ9aVkKNqHGEeSSvWGwopEsQ_bkony-WJtPyH0X5K0g2rl5iG6Bz5PTf9HvptKpzllU_SjRF1I4bXUfSt6eEjkcvO1uiTCJBU1oMlhjB0Y-MEGNwWIGqrjO3rmA5RLUUHCkFbutkloRiHTio6J6xltyOoTU3yjGZqFfV3WCquftWwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دقایقی پس از بیانیه قرارگاه خاتم که در آن تنگه هرمز کاملا بسته اعلام شده و هشدار داده شده بود که به هر شناوری که قصد عبور داشته باشد شلیک می‌شود، تسنیم از مورد اصابت قرار گرفتن دو کشتی در تنگه هرمز خبر داد. در گزارش این رسانه وابسته به سپاه آمده است که کشتی‌های «متخلف» قصد داشتند «به‌طور غیرقانونی» از تنگه هرمز عبور کنند. هنوز مقامات رسمی و سنتکام در این زمینه اظهارنظر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76174" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LyIHqLu55Ucu18hsWkhXv8D02Sc-mgTKKU2kLn6Drht8rNYrXPkKy1K6QPWA3StQvjE7qVd197R96loPBQCK3ImllKrfsiKUXgG3VQ5mVN9vAG0MhRvyhFFpD6R09KHdfkNgj8-RpA3EyJ-ELWN-JDvAqt9oRLiyDO7air-990EfcqsTTfmenZa-M259MFsj4x-FnXwp0MxAGDrgDFPC59-kpDZQk_YPX2z2Xj5jmCaHwfk5ro63tNm3X5YmcoV50ZvJNSrc837j8pYDsDJwd5vZ_3rKqiDdCGkYPY1mS5fj3lo58aR7AIp3l3YkIpRgSydpOq_d1zr4nlJjb7j-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
روزنامه وال‌استریت ژورنال پنج‌شنبه شب به وقت واشنگتن به نقل از یک مقام ارشد آمریکایی گزارش داد که هیچ سایت زیرساختی در ایران مورد اصابت قرار نگرفته است و نیروهای نظامی ایالات متحده در حال حمله به پدافند هوایی و سایت‌های راداری در نزدیکی تنگه هرمز بودند. انفجارهایی در امتداد تنگه هرمز، از جمله بندرعباس، جزیره قشم و سیریک گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76173" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیام‌های دریافتی:
قشم ۲:۳۵ صدا و لرزشش حس شد
۲:۳۵ دقیقه بندرعباس دوباره صدای انفجار اومد
سلام  بندرعباس دوباره زدن ۲:۳۷
[احتمالا منظورشون اینه که صدا شنیدند!]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76172" target="_blank">📅 02:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76171">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AnDOh1247QO70WMphTms070ds6rCwGXKrvVVaz-IHgDk4lNT-fzvahAq4rGydtG5CgFX-S-xx7bPUeDjyGCQo7UTSLNEQgKb5VimG8AynEVHVouIS3ZozlLO1qiu-f-zrr2Tv_8MrXuCKL_CzWCfQkuhm_l7zVIhb4kFY2tnK0fNZU9jVARKYWkl1iW4V41pO_sGHw8Rk19KaMRlrE0srEukrmLMati2A9LV1CM5m7Td_Hw54wuGF3mcDomjCafvu3Aw1ouE8SzcDEqnj-3aLANeBpe98Doc1Gx-vY_D0-bzyHLW1AnDgVkNKj1ujha_BL97v_aUrMe7K3TAThSgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: هرگونه تردد شناورها از تنگه هرمز مورد اصابت قرار خواهد گرفت
منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
در ادامه شرارت های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت.
ادعای آمریکا مبنی بر عبور کشتی از تنگه یاد شده تکذیب می شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76171" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76170">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNOplmMyJAh6XNy3iFtyOtkpagxO6FabCrl8eV-D6Q3x0c-7txJkm5YnCgQipcfoadiaRUgmqtz4tvjilmORIRwP6oWfzOCHalJHwKUjCn-TR8nb28GN13Czk6Ww9nV0zuiVxhYgNCwLmwmOV2lHkfAfwyd-mrOATjuAE4X2xFAqtqIaPQwHC54RwYwhoc-L2h0R0O3LY1PH6miUJzOBZhZMIduFm0MF1XhqYasbYDcmYaNQCsdsixcVsZrWzlIMKoY576B4v5O_SX27vjs5gKsZPcvQau-6UXUBLuKq_MI4oAwLrTZWx_vlc0yBnH6U0E0my4sxFkjDg93wv5W9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس بامداد پنجشنبه ۲۱ خردادماه به نقل از یک مقام آمریکایی گزارش داد تمامی اهدافی که در حملات اخیر مورد هدف قرار گرفته‌اند، در جنوب ایران واقع شده‌اند.
این مقام آمریکایی گفت سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها از جمله اهداف این حملات بوده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76170" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76169">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بعضی کانال‌های خبری به نقل از تسنیم نوشته بودند:
‌
منابع خبری از هدف قرار گرفتن یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه خبر دادند
خبرگزاری تسنیم وابسته به سپاه در پستی نوشت:
انتشار خبر جعلی در کانالهای فیک‌نیوز به نقل از تسنیم
برخی فیک‌نیوزها از دقایقی پیش به صورت هماهنگ خبری با عنوان "هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد" به نقل از تسنیم نقل می‌کنند.
این در حالی است که امشب چنین خبری تا این لحظه بر روی هیچکدام از خروجی‌های تسنیم قرار نگرفته است و چنین خبری تاکنون صحت ندارد.
به هرحال اون خبر رو خبرگزاری دانشجو وابسته به بسیج هم منتشر کرده و الان به نقل از اون داره پخش میشه.
🔄
آپدیت:
ایرنا، خبرگزاری رسمی دولت در جمهوری اسلامی:
فرمانداران عسلویه و کنگان که هر دو شهرستان میزبان تاسیسات پارس جنوبی هستند هرگونه حمله و انفجاری را تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76169" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیام‌های دریافتی:
صدای سه انفجار در بندرعباس
بندر عباس سه صدای پشت سر هم ساعت 1:20
وااااایییی تو دو ثانیه سه تا انفجار شنیدم بندرعباس خیلی نزدیک بود
بندر عباس همین الان چند تا صداااا
بندرعباس سمت زندان شهرک صدای جنگنده یا انفجار طولانی اومد
همین الان یک انفجار خیلی خیلیییی سنگین بندرعباس
دوباره انفجار بندرعباس ۱:۲۲
وحید بندرعباس الان یجوری زد شهر لرزید
وحید ساعت ۱:۲۰ بندرعباس سه تا انفجار خیلی سنگین شد
دوبارهههه صدا اومد ولی خیلی دوررر بود فکر کنم سه/چهار تا بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76168" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEdHhvAYYVE-OMBHs6qTVmMsNM32bUV-vFifCBJzQoxknipHZHugygtv7lvwWRE6au1v65jL8obh0bOOUnwNXCSpRFieXxnutOv5zYBxEvqLVbikwaUITpggkY8gURwktFTuFIh5h91qXf4jqNtCwgEwR-qcn8RKU2tSgiEvOVKIiJRafBG-w26mQcQzpwsDrcNWcZtMdR_fB7XZH7X0cquDixv-7v8om496CGsyerE-GeIyJQNhWtcpUN_wWkbupIkv5Polr_1tD4A3XLuTyZKmA50gumZ6UGj9kkn7-gBIgLbpaKYoZ7KjI_y_Ray71tbPJDWR3s9K4_FdBtm21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی آمریکا امروز، به دستور فرمانده کل قوا، از ساعت ۵:۱۵ عصر به وقت شرق آمریکا، حملات دفاعیِ بیشتری را علیه چندین هدف در ایران آغاز کردند.
این حملات در پاسخ به تجاوزهای بی‌دلیل و ادامه‌دار ایران انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76167" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۱:۰۳ بندرعباس صدای انفجار شدید اومد
بندرکرگان شهرستان میناب، رو با موشک زد
همین الان
پاسگاه دریابانی رو زد
صدای دو انفجار در بندرعباس همین الان
سلام ساعت همین الان انفجار شدید در بندرعباس ساعت ۱:۴ دقیقه
وحید از ساعت ۱:۰۳ دقیقه بامداد
چهار تا انفجار بندرعباس
سلام وحید،صدای چند انفجار همین الان بندرعباس
سلام. همین الان صدای انفجار شدید، بندرعباس، ساعت یک و سه دقیقه شب
صدای انفجارهای ممتد میاد
صدای انفجار بندرعباس
بندر عباس فکر کنم سه تا انفجار با فاصله چند ثانیه
صدای انفجار بازم میاد میناب نوار ساحلی
انفجار دوباره
سلام،وحید جان بندرو زدننن من لرزیدمم
همین الان صدای انفجار بندرعباس دو الی سه تا صدا اومد
انفجارها داره زیاد و قوی‌تر میشه، بندرعباس ساعت یک و شش دقیقه شب
سلام‌وحید جان بندرعباس همین الان ۱:۰۵ دقیقه صدای انفجار اومد
سلام وحید جان
همین الان ۱:۰۶صدای انفجار داره میاد بندرعباس
پنجره خونمون لرزید
درود درگهان همی پنچره ها لرزید
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/76166" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، بدون هیچ توضیح بیشتری نوشته:
شنیده شدن صدای انفجار در سیریک
🔻
خبرگزاری تسنیم، وابسته به سپاه، نوشته:
بررسی‌ها نشان می‌دهد که
تا این لحظه
اخبار مربوط به صدای انفجار در جزایر کیش و قشم صحت نداشته و صداهای شنیده شده مرتبط با درگیری در خلیج‌فارس است.
براساس گزارش منابع محلی، دقایقی پیش صدای انفجار در اطراف میناب و سیریک شنیده شد.
🔻
پیام‌هایی در ابراز تعجب از پرواز هواپیمای مسافربری در تهران دریافت کردم.
🔻
تسنیم در پست دیگری نوشت:
تاکنون صدای ۴ انفجار در سیریک شنیده شده است
🔻
عکس‌هایی از فرود  هواپیماهای مسافربری در تهران دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/76165" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0af3a46aeb.mp4?token=L-9k6cUcd1uU1eqRQBjscCPojncgGwTv4asGLcaDlxhkdtDdH7Ib58nngqFRFRQ3WemVQHOAv2ztOvHGsjMMd-2HEafKUqZxgDogJbzUoQ-V64pC565drH8Uc5fFii-yCkG3fS_5CItLvDghsgsWf66dqim-jeUA8a-v6nAyvS-WRHAed9zIQPPecI-2FNnlu7Nru67-h-P3qrY5kxYLHFib_UENnMzARiWqfjSQviv2Y-jF3dhelRpQL3wcsrEMZFEsTWzoRQvyQtexi2rCdSJch8F_ozog18EOVYYmL178xmr8kB_Nswmpdu_3q344ptool8LfQ34bXo6qSamR6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0af3a46aeb.mp4?token=L-9k6cUcd1uU1eqRQBjscCPojncgGwTv4asGLcaDlxhkdtDdH7Ib58nngqFRFRQ3WemVQHOAv2ztOvHGsjMMd-2HEafKUqZxgDogJbzUoQ-V64pC565drH8Uc5fFii-yCkG3fS_5CItLvDghsgsWf66dqim-jeUA8a-v6nAyvS-WRHAed9zIQPPecI-2FNnlu7Nru67-h-P3qrY5kxYLHFib_UENnMzARiWqfjSQviv2Y-jF3dhelRpQL3wcsrEMZFEsTWzoRQvyQtexi2rCdSJch8F_ozog18EOVYYmL178xmr8kB_Nswmpdu_3q344ptool8LfQ34bXo6qSamR6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در جمع خبرنگاران گفت حملاتی که امشب به ایران انجام خواهد شد، «قوی و روشن» خواهد بود و فرماندهی مرکزی آمریکا امشب درگیر عملیات خواهد بود.
او افزود آمریکا تاسیسات کلیدی در جمهوری اسلامی را بمباران می‌کند و امشب «ضربه سختی» وارد خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/76164" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/riQ75j5C1AR4wrFVHd4lZVJEuYDINlzTQ9TTFmlI4Xt6um_DJKrv1YMSBwSrvjgMIrEntIrUFz7XR7642BWkK10KBqGPt_DnAJ8ulNgI9wsnpRBVOFiV_ztKuriDEAr7aXIobOw9N9j10ktgfeiGsL0xP2BJ2tlRM1vGuE7AVUygiCn886C-Vg8WUzWgmNeYZE_5Ip8F2Dye6kkj_aJNvjcyWwC3bACSXDY9W5OiucJzDuHYIO3u27lwOZR63_u4EfVxMUOxDWdgrSZ1E9Djk8Vhl-yXzryaM3jBh_594m_S6UhI3urvSnmilsKv_78X1fY1R8_h5r0IR_lkNKoSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: ترامپ درباره گزینه‌های حمله به ایران در اتاق وضعیت جلسه برگزار کرد
ترجمه ماشین:
پرزیدنت ترامپ بعدازظهر چهارشنبه جلسه‌ای در اتاق وضعیت کاخ سفید برگزار کرد تا درباره حملات احتمالی تازه علیه ایران گفت‌وگو کند؛ این جلسه چند ساعت پس از آن برگزار شد که او به خبرنگاران گفته بود آمریکا «امروز دوباره ضربه سختی به آن‌ها خواهد زد». این را دو منبع آمریکایی اعلام کردند.
این منابع گفتند یکی از گزینه‌هایی که ترامپ در حال بررسی آن است، انجام عملیاتی است که از نظر مقیاس بزرگ اما از نظر مدت‌زمان کوتاه باشد؛ با هدف فشار آوردن به ایران برای تغییر موضعش در مذاکرات.
این منابع جزئیات بیشتری ارائه نکردند.
پیت هگست نیز در فلوریدا خطاب به سربازان گفت: «اگر قرار نیست توافق کنند، ما ضربه سختی به آن‌ها خواهیم زد»؛ سخنی که بازتاب‌دهنده اظهاراتی بود که ترامپ پیش‌تر در روز چهارشنبه بیان کرده بود.
axios
کلی میر،‌خبرنگار نیوزنیشن گزارش داد پس از آنکه پرزیدنت ترامپ گفت ایالات متحده به حمله به جمهوری اسلامی ادامه خواهد داد، پیت هگست، وزیر جنگ آمریکا اعلام کرد سنتکام امشب مشغول خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76163" target="_blank">📅 23:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU_eYQ7uG9Dk2gxyYQaBVVmpgVMgG0LLgyHqjODWH-p7lz0xxUV57VFxOYxgbwkECYrjUWsmpflUO-g4JVyhZOkFPCbexM55piH8tBKRGiqOHMyEhlsMoJCYqeivbX_AbdY2k_PC09Iko5KMswwkwRQMIoszRc-YcAGHI2tFEpvN4EE_YDkIguqihWCNT_lv33GmgJKIYuThi9O5rtsAIC4QlJ2MO8SegH9XQHkVLZhMdmnWWYgDdOL9TQJ1RCGi59ukticAa-6fOcUZftFRdnY5IfvugMUnfXcr5gdHbbuvySRA240oDvVSYB-e2VXS71aU-bXNctbXUJ2CnvB39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز ۲۰ خرداد ۱۴۰۵، گزارش داد جمهوری اسلامی با پیشنهاد میانجی‌های قطری برای برگزاری یک نشست سه‌جانبه با حضور نمایندگان ایران، آمریکا و قطر به منظور حل اختلافات باقی‌مانده در مذاکرات موافقت نکرده است.
بر اساس این گزارش، مقام‌های ایرانی و آمریکایی طی دو روز گذشته به صورت جداگانه با میانجی‌های قطری در دوحه در تماس بوده‌اند. با این حال، تلاش قطر برای برگزاری یک نشست مستقیم میان طرف‌ها با مخالفت تهران روبه‌رو شده است.
اکسیوس به نقل از منابع آمریکایی و منطقه‌ای نوشت که همزمان با ادامه تلاش‌های دیپلماتیک، هیئت قطری روز چهارشنبه برای گفت‌وگو با عباس عراقچی و دیگر مقام‌های جمهوری اسلامی به تهران سفر کرده تا روند مذاکرات را از بن‌بست خارج کند.
این گزارش می‌افزاید که دستور دونالد ترامپ برای حمله به اهداف نظامی ایران تنها به دلیل سرنگونی یک بالگرد آمریکایی صادر نشد، بلکه نتیجه افزایش نارضایتی او از تاخیر جمهوری اسلامی در پاسخ به آخرین پیشنهاد واشنگتن بود.
به گفته یک مقام ارشد آمریکایی، هدف از حملات محدود آمریکا در شامگاه سه‌شنبه «بازگرداندن اهرم فشار» در مذاکرات بود، بدون آنکه تلفات انسانی بر جای بگذارد یا مسیر دستیابی به توافق را مسدود کند.
دو مقام ارشد کاخ سفید نیز به اکسیوس گفته‌اند که حتی اگر سرنگونی بالگرد آمریکایی عمدی نبوده، واشنگتن برای جلوگیری از تضعیف موقعیت خود در مذاکرات ناچار به واکنش بود.
به گفته این منابع، حملات آمریکا به گونه‌ای طراحی شد که تنها سامانه‌های راداری و مراکز کنترل پهپاد ایران را هدف قرار دهد.
اکسیوس همچنین گزارش داد که کاخ سفید ساعاتی پیش از آغاز حملات، بار دیگر از تهران خواسته بود پاسخ نهایی خود را درباره پیشنهاد اخیر ترامپ ارائه کند، اما مقام‌های جمهوری اسلامی اعلام کردند هنوز تصمیم نهایی اتخاذ نشده است.
بر اساس این گزارش، ترامپ پس از نشست ۸ خرداد در اتاق وضعیت کاخ سفید، دو شرط جدید را به پیش‌نویس تفاهم میان دو کشور اضافه کرده بود.
نخست اینکه ایران ظرف ۶۰ روز ذخایر اورانیوم غنی‌شده خود را رقیق‌سازی کند و دوم اینکه از دریافت هرگونه عوارض یا هزینه از کشتی‌های عبوری در تنگه هرمز خودداری کند.
در مقابل، واشینگتن آمادگی خود را برای پذیرش انجام فرآیند رقیق‌سازی در داخل ایران و تحت نظارت آژانس بین‌المللی انرژی اتمی اعلام کرده بود.
اکسیوس به نقل از منابع آگاه نوشت عباس عراقچی به میانجی‌ها گفته بود برای ارائه پاسخ تهران به چند روز زمان نیاز دارد، اما این روند به نزدیک دو هفته انتظار تبدیل شد و موجب افزایش نارضایتی ترامپ شد.
این گزارش همچنین می‌گوید پیش از تشدید درگیری‌های اخیر میان ایران و اسراییل، دو طرف به دستیابی به توافق نزدیک شده بودند، اما تحولات نظامی روزهای گذشته روند مذاکرات را پیچیده‌تر کرده است.
با وجود حملات متقابل و افزایش تنش‌ها، مقام‌های آمریکایی به اکسیوس گفته‌اند که مذاکرات همچنان متوقف نشده و واشینگتن امیدوار است فشارهای اخیر، جمهوری اسلامی را به ارائه پاسخ نهایی درباره پیشنهاد آمریکا وادار کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/76162" target="_blank">📅 23:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76161">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u2AJnaZ1qNSX08mm156ndwQmYKZjJJK-WXoGnowSugjT5AfhvQXd3WORyMpFVTephZNywK_mqfxnwYZZm7Bj3FvZcH6KBYvq8HHYpuQbqmlnTFA-0LlQsJtxpRSYnXSqoSGwxn36c5aoaSJ_M7jpH-3zRR7B45k9ROjxyTVdEkrnWa_zgdcfUNW5x1QDciTk2rixrQSrARvd0i9f-a9Th3eCD56dGywEKmAMj7syM77axb79E5dmsoVlSkpNzOyGAq39KshB3cj796S_pO7hEcxd0kfc63OgKAxhBV2WpAqxsu_G7eRS1mnryzXJsJHApfRZCAwzs1HPzW1u0_VC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی مجلس، در شبکه ایکس نوشت: «در جنگ ۴۰ روزه وسعت آب‌های سرزمینی ایران افزایش یافت، در جنگ بعدی شاید وسعت خاک ایران افزایش یابد.»
او در مطلبی دیگر تاکید کرد جمهوری اسلامی آماده‌تر از قبل است.
او همچنین در یک برنامه تلویزیونی گفت: «دست از لبنان برنمی‌داریم و دشمن یا باید به خواسته‌های ما در میز مذاکره تن بدهد یا در میدان نبرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76161" target="_blank">📅 22:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/274405ecae.mp4?token=MoY_EJQmatCk6lnXwKZzgQ_iYgwUlRCfp5bT0XolfRexNSpgBoKJ00foVSyZwLO3oscPsQGEV0UwKk5B7p103dIihRK5Fnaj2maKegQ8caSPKY8AEVZ5Kc5CAVhBDVUDsH7bGSxfJCEm6JyTLXqB8gsF13Cf_XMdApKzXCW9xfFY1w7QvkKYrfEcrv0qGJ0EewNQQz1Dribyia8IpjM76m27XEWAg2aLXLs_CWImNB6hNI_V22kCGlqt-K3Jj9VIhY5rQd5a-QFInsaRUoIJTTH0NHt9Lzv_yJjaJyuxCAI-68fjdoDAVTExSUOMjrTfp2bQpMGb_f2SNeUgMbnqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/274405ecae.mp4?token=MoY_EJQmatCk6lnXwKZzgQ_iYgwUlRCfp5bT0XolfRexNSpgBoKJ00foVSyZwLO3oscPsQGEV0UwKk5B7p103dIihRK5Fnaj2maKegQ8caSPKY8AEVZ5Kc5CAVhBDVUDsH7bGSxfJCEm6JyTLXqB8gsF13Cf_XMdApKzXCW9xfFY1w7QvkKYrfEcrv0qGJ0EewNQQz1Dribyia8IpjM76m27XEWAg2aLXLs_CWImNB6hNI_V22kCGlqt-K3Jj9VIhY5rQd5a-QFInsaRUoIJTTH0NHt9Lzv_yJjaJyuxCAI-68fjdoDAVTExSUOMjrTfp2bQpMGb_f2SNeUgMbnqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'آتش‌سوزی حوالی میدان قیام تهران'
چهارشنبه ۲۰ خرداد
Vahid
و گزارش صدا و سیما که میگه بیشتر انبار فرش هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76159" target="_blank">📅 21:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76158">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_m6ErQi9UzQM5nGymFXsmVv21CMY-QaBSgpY9mRjtV4h-JExYUIum3GvZaZcw4EwnftPUq39Cu6XD9s8Y2OlaT__r-5rlu_JMlV16_JeoubpwfT7CLOJbhh_o-2nYtbcmtuW7cfrgqaoc_WTmfmGAZLjcCQpZubnM8C8N4A6uWMdmkUzukDPlP1m_1_6u26hIX3pVZaDQ42_5xOEaAYWYSkBA0FsXMW6w6fZyBinRmQNcKFTComAET6eJSrC8zIinCo1jPWv6sj2LOoeF_EynplX5w3-uRKsG2VlgWB5_DZfWSLd8DdARCXLbJeAy2xA3NFn-p_l1zdcyNGvDFi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بیش از ۱۰۰ میلیون بشکه نفت در جریان ماموریتی محرمانه از تنگه هرمز عبور کرده است
ترجمه ماشین:
ماه گذشته، من به ارتش بزرگ ایالات متحده دستور دادم مأموریتی محرمانه برای حمایت از نفتکش‌ها و دیگر کشتی‌های تجاری در عبور از تنگه هرمز اجرا کند. امروز خوشحالم اعلام کنم که این تلاش باعث شده بیش از ۱۰۰ میلیون بشکه نفت از تنگه عبور کند و وارد بازار آزاد شود. بیش از ۲۰۰ کشتی تجاری نیز با ایمنی از تنگه عبور کرده‌اند.
این تلاش به‌شدت موفقیت‌آمیز به این دلیل است که ایالات متحده آمریکا تنگه هرمز را کنترل می‌کند — نه ایران. ارتش آن‌ها شکست خورده و اقتصادشان از دست رفته است. کار ایران تمام است!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/76158" target="_blank">📅 21:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76156">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O1Pb1vVqkvFxkffRXOMbkZBkxkFjA4TQxxQ8jbgRn2PwFr7bfv3woJoCdxTH5p9bB54dlQqVsxZevFndNl3JzS4YfS8DYJ357DNyDPSvoLqqz-bIO8iR5Jzb8qbLrGFqK5OUGpA64bDQ9rw69sSBBYI7BfcDrwMTPJ6xvPdekNX7RlCcY_dx62oJMy_zmlzedRrrs3namFTu7nfwCHTCtLBwZG3Gl3lJAjh4zNGK3xmQUmEoCE25h_UQP-fUAczf0P4jsIRjqV9qmlRsOKSnthy-EH1yPPJ0BK3JplrKF9ZwgUc-r6OluWwPXWuOPGOTL9A-PtF2TNiSOTUvOccPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1379a1972.mp4?token=C_nLSBcD2cr9rx-mwrAOVhLmVG9gs08rMGAfSbkjboqlP3qTJ5MLJd-4pIJyxjWr04s_gJxQJio90MPBfUuiYSqMk6h8t9nFrtbzb1Ub4Gn7l8pcowykJujhYw9rNW4HAS4DAN7xae0dOr62lyhPg0XBj-4Ak860lKeoYF7D1A36cnF_ASRd9bvd8yT0-Q1eGy-ZBEccQK1jI18kCnffgeLHywVyOGtSFWONNAMismzKnGEWEMloprsxeKBuI0VHzV-0Lrsdm19Rt6kObQbyexwvycYFm05CMlzNWqF0ZdonnyrfhDYIdk6POthBUlVNnX9LVhzTvDXcZnJ3TakjCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1379a1972.mp4?token=C_nLSBcD2cr9rx-mwrAOVhLmVG9gs08rMGAfSbkjboqlP3qTJ5MLJd-4pIJyxjWr04s_gJxQJio90MPBfUuiYSqMk6h8t9nFrtbzb1Ub4Gn7l8pcowykJujhYw9rNW4HAS4DAN7xae0dOr62lyhPg0XBj-4Ak860lKeoYF7D1A36cnF_ASRd9bvd8yT0-Q1eGy-ZBEccQK1jI18kCnffgeLHywVyOGtSFWONNAMismzKnGEWEMloprsxeKBuI0VHzV-0Lrsdm19Rt6kObQbyexwvycYFm05CMlzNWqF0ZdonnyrfhDYIdk6POthBUlVNnX9LVhzTvDXcZnJ3TakjCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از نزدیک‌تر: 'آتش‌سوزی حوالی میدان قیام تهران'
چهارشنبه ۲۰ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76156" target="_blank">📅 20:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FLksjK9ZTnbLrk036r7SLepIqn1qz-ail4W417o1_X0ox_B_S3Auy8el2sbfSBZCzxB0RX05wrROmdou89M4fkRxfb5vhUvoUBZYRUAOvhTa-8NmXWVXI9wQ_cU87__PvVB3aLxHig7VQNvfvXJqMpk16DHsMNd60urKQdDvIxO8jLx14ovn937JKyieKNJ2CLjkOmGQ0RlIQHaMepxspCBPOc7Ut6HGyfuejHBtF9MFf-y_hczNy_r_aFjJmp70OjB1ZQDvXvASzYlro3eaWEEfVxt6K59Bt0Eo61KvLBpZKXPNdun0v9HsvPMn0hnB6q2YsFd8VBlRb8UGW2h2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q4OyzEa3ioYpkuOgUgA79Js8BBLjbfQkhBaHahUne_hqsRxZ4qEAtWajHqNUWMefsyUTWij9pXFiJJB3wqYF4g7YTLtHFhJkQn61wyv06q2K5Rk1AxJ1aHP_8MZBaVfYsWSqyiWtSJ7ZpIIdUjGdNIRL8H4rVYNHhF0-JvQaSle_QrhbfzBhU6AYX3fN67ODMflPH1A026l5W_PFfc5xZVccIV38zgtuYP72-2dYLQTyGLuSgMlvICOhxkAAQheR1H4oGy4LThVsg_dqgnxpkw98-_KrpjgHo3GqfNTLr2RI0w7pKOM6UEXI-vcp8oAli0S4ke3hYu2kJE3IRfGYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TSIL1vDc3oVwr279DoR6RVkPhkH2Ce2tQLotpNgrfMq9cQcTGpNfzNb8I_DQJSf6K5gvZYhPmIu4yj9qYE7BfN0QLLEBCsSeRqzeJzl69o5cPm1FuLP5ixsp40bcPHCVI35r3UHyr_cxW-8WkiaVVNcXpRdSMZPOgoB9kQydvHfVQ68mKsciReeQYwk1Mh_0shWZ8K2rZoQkShE8GoVUGt-hCLS2BXdZp-3yJFVs1nt6v9hGeCrcnFiTRtshD1K3eKf8br_Rg-ajMJ0-0pRpPoGOvcukAuqER599H7cGrP2q3p-eJOOKh9G-dJGT2My5xJGNym0uHLJmXYM-nsSV-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SzFdkKHnBYC0KeYBkWuVbijKwgSLTkFZvpCG5m0PKy29rxcMSsFHP2O9ttagrdk6vTFjFx4cZivR7nwKYxz29BKmbqapPrTsFfam4Nxw4QEs7S_exeioffIqrhUzg2qKYmvcbxNVEicOgnoru1r5FBIxBZ6UuiAX2ImNVnaI4HDI2X9p8w49hNugZsYQiwgF4eO_fkYu_MH-uiJH7gg2hEVEXjzU5LSxJG7zE2bgsSxGwHLueNmUqxGgpG2qPHSf7_RxSyb5NEJlDv_Lf_I9K53Dht1BW2qvIdiTMkjMnL8wK8RdWq4GI6s1rlklQDSMBkXk3PbShxUwbZPnzlN0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a06pK8z8iv3EavhUZO_QD0NwZqe49AgvAy5TEXONMkKD9Ak-E1N5pwOSFEnGyXnxBB85Wz46fO0LTMZ57o08syG9roykfXmhyb25KxlLQBqRJqmEursxdpgtmxar_erURYDaD_z36rXQDK3GITeWvG_t4ZqRESMYJTX3I_Swfk2UVps3T746thSsYEddvf94z69Qy1ykaPBJu_5ip4yajTJgO-tKZLC0uNBmXOsfWEHSL2vfFAkKT6NtiBblKSwJJrJc3H_0xeeIa2i62naEkHuuTbMIPrM1EsCVbu3g7igjQqTB6J_P0CrB1GCaC04KNNS61OvLChpGnuDHPwHsMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی از ستون دود سیاه و غلیظ حوالی مرکز
#تهران
منابع حکومتی نوشته‌اند: "یک انبار کالا حوالی میدان قیام در منطقه ۱۲ تهران دچار
#آتش‌سوزی
شده است."
چهارشنبه ۲۰ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76151" target="_blank">📅 20:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/02bad1a497.mp4?token=fylTiaeHNpwxDLD87emWVAHBQBH5iC3eQQPPnttOVB3XsQihOn-rwNRPsIU7_L6mYhXl0TI9VbIn4fwBEKR1ocOXj4q65lubHx0hhsDuUJlnHWPcPJLdJ_oVkwHoNlFP7riqqBPfogFSKe6H7ydhlo2o6grOFenwVyUJZicatcS_qdLSXYry1svd7DIQ4Vvo61zTjWy-MB-ZO9nyMeOn_nn9Tu69RCZcAP640c17yADs3BeZbucBQvwF5-kkTPD_bbELyIqDhjbHiyQfFfmGOE7TjIu29P58I1SAO9g01qmYvNiuce51VZuNkiKu1qaweiK4De2svRLutM518XEFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/02bad1a497.mp4?token=fylTiaeHNpwxDLD87emWVAHBQBH5iC3eQQPPnttOVB3XsQihOn-rwNRPsIU7_L6mYhXl0TI9VbIn4fwBEKR1ocOXj4q65lubHx0hhsDuUJlnHWPcPJLdJ_oVkwHoNlFP7riqqBPfogFSKe6H7ydhlo2o6grOFenwVyUJZicatcS_qdLSXYry1svd7DIQ4Vvo61zTjWy-MB-ZO9nyMeOn_nn9Tu69RCZcAP640c17yADs3BeZbucBQvwF5-kkTPD_bbELyIqDhjbHiyQfFfmGOE7TjIu29P58I1SAO9g01qmYvNiuce51VZuNkiKu1qaweiK4De2svRLutM518XEFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، طی سخنانی در کاخ سفید درباره جمهوری اسلامی، گفت: «ما آنها را بسیار سخت هدف قرار خواهیم داد. باید توافق را امضا کنند. ما توافقی می‌خواهیم که معنادار باشد و کار کند.»
او ادامه داد: «امروز دوباره ضربه محکمی به آنها خواهیم زد.»
ترامپ افزود: «نخواهم گفت آیا پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد یا نه.»
ترامپ با اشاره به هدف قرار گرفتن یک بالگرد آمریکایی گفت جمهوری اسلامی ابتدا مسئولیت این اقدام را رد کرد، اما بعدا آن را پذیرفت. او افزود بمبی که به بالگرد اصابت کرد منفجر نشد و دو خلبان آن در جریان یک عملیات نجات زنده ماندند.
ترامپ بار دیگر گفت: «دیروز ضربه سختی به آن‌ها زدیم و امروز هم دوباره ضربه سختی خواهیم زد.»
او در پاسخ به سوالی درباره احتمال هدف قرار دادن پل‌ها و نیروگاه‌ها در ایران گفت جزییات عملیات احتمالی را اعلام نخواهد کرد، اما آمریکا توان انجام چنین اقداماتی را دارد و «قوی‌ترین ارتش جهان» را در اختیار دارد.
دونالد ترامپ، رییس‌جمهوری آمریکا، در در کاخ سفید، گفت جمهوری اسلامی «به هیچ‌وجه» نباید سلاح هسته‌ای داشته باشد و نخواهد داشت و افزود مقام‌های جمهوری اسلامی نیز با این موضوع موافقت کرده‌اند. او گفت تنها کاری که جمهوری اسلامی باید انجام دهد امضای توافق است.
رییس‌جمهوری آمریکا افزود توافق «کاملا مذاکره و نهایی شده» است، اما جمهوری اسلامی همچنان در حال وقت‌کشی است.
او گفت: «چند روز دیگر هم به آن‌ها فرصت می‌دهیم، چون این یک سند مهم و معنادار است و آن‌ها می‌دانند وقتی آن را امضا کنند، تعهدی جدی ایجاد می‌شود.»
ترامپ بار دیگر برجام را هدف انتقاد قرار داد و گفت: «توافق اوباما، برجام، یکی از بدترین و احمقانه‌ترین اسنادی بود که تا به حال دیده‌ام.»
ترامپ همچنین گفت جمهوری اسلامی از برخی اقدامات اخیر آمریکا اطلاعی نداشته و افزود آمریکا چند شب پیش ۲۲ کشتی را در تاریکی و بدون چراغ جابه‌جا کرده است. او گفت جمهوری اسلامی «دیگر رادار ندارد» زیرا آمریکا سامانه‌های آن را نابود کرده است.
او در ادامه گفت زمانی که تصمیم به حمله گرفت، به اطرافیانش گفته بود اقتصاد آمریکا در بهترین وضعیت قرار دارد، بازار سهام و حساب‌های بازنشستگی به رکوردهای تاریخی رسیده‌اند، اما جمهوری اسلامی به‌زودی به سلاح هسته‌ای دست خواهد یافت و به همین دلیل باید اقدام نظامی انجام شود.
ترامپ افزود آمریکا با بمب‌افکن‌های بی-۲ به جمهوری اسلامی حمله کرده است. او این عملیات را «بسیار شجاعانه» و «کاملا موفقیت‌آمیز» توصیف کرد و گفت پس از آن «مرحله دوم» نیز باید انجام می‌شد.
رییس‌جمهوری آمریکا گفت برخی پیش‌بینی می‌کردند بازار سهام پس از این حملات تا ۲۵ درصد سقوط کند، اما جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای «ارزشش را داشت». او همچنین گفت نگران بود قیمت نفت تا ۲۵۰ دلار در هر بشکه افزایش یابد، اما اکنون حدود ۸۵ دلار است.
ترامپ در ادامه گفت نیروی دریایی جمهوری اسلامی «از بین رفته» و ۱۵۹ شناور آن در کف دریا قرار دارند. او افزود جمهوری اسلامی دیگر نیروی هوایی ندارد، هواپیماهایش نابود شده‌اند، بخش عمده پهپادها، توان تولید پهپاد و موشک‌هایش از بین رفته‌اند و رهبری جمهوری اسلامی نیز جایگزین شده است.
او در پایان گفت فکر می‌کند جمهوری اسلامی خواهان توافق خواهد بود، اما افزود:
«خواهیم دید چه اتفاقی می‌افتد.»
ترامپ همچنین گفت با پایان جنگ، تورم کاهش پیدا خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76150" target="_blank">📅 19:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TymS2iVgrNOAO-v6zRyoj1zJP10TZ-_ubJ6hHEYG3al490Qq57CPyGnpzsD-WmBe1VhPe_wvb5cV5ClbVJyRsE68wbi-VaXFTEkT-Uy0ed45ZGYO1JW5Ea3gwCdzYcVwM6qMrlEKDANH5Vc5oaXI1IQNlkgR-Dql-4GhUI38McvsWyTm106uWHo_taSiWNJEkk6l4dHUGKmATryqj9O7h2K7DgcNgbSCQ53lxQDLSacvkzvkw9NEg2NlaOWh-vCEJvQbhkKzNDb_JmnMrD8iNzy9XEN65QIE5cUZkJPnI95Fal8JMgNIGuSyuILt1ZtAwUaPE10LjqcytH29JvdWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا روز چهارشنبه ۲۰ خرداد، در پاسخ به درخواست خبرنگاران برای شفاف‌سازی درباره اظهارات قبلی‌اش مبنی بر اینکه جمهوری اسلامی ایران باید بهای طولانی کردن روند توافق را «بپردازد»، موضع تندی اتخاذ کرد.
دونالد ترامپ در دفتر بیضی کاخ سفید به خبرنگاران گفت: «خب، ما به آن‌ها حمله خواهیم کرد، و بسیار هم سخت حمله خواهیم کرد.»
در ادامه از او سوال شد که آیا این به معنای از سرگیری کارزار بمباران [مواضع ایران] توسط ایالات متحده است؟ ترامپ پاسخ داد: «بله، خب، با توجه به موضوع بالگرد، فکر می‌کنم این حق را داریم که چنین کاری انجام دهیم.»
ترامپ ایران را متهم کرده است که یک بالگرد آپاچی ارتش آمریکا را بر فراز تنگه هرمز سرنگون کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76149" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
