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
<img src="https://cdn1.telesco.pe/file/H0VksxhbMHXQMpAOO5cklaiF3fRUdiDpsO2yxvbqh9Btfol55AdLf9QlUT-rBo-CxD9q3y2BNiXPeYdqSY1t4d0vt2Qi9tHAXq74aBFt6ETSKpFUkRy7s_NKcHOwyhH3Y3uPQfrvY1vlD3vxPVxVDL9u-s6XzmhtezIwLZRsSiPzW5fLwK5jXZasVruwAVKV0Rv1Sfd6IXOPtJOMxdAEiRS3yFJ52UpN4m_s0BMDTf4ofYycJlk-iobqWCJivx7zz0mmcR_FecxjhfhjsTbg_5xjUJPpezAFzemnUKWEd68qdcUnUXU5bSMmN7QUe7gWSg4uWT4VDWTvcq1bB0dj6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYSfGBJ9o7c0ApeunYf4B5QXwv2cIFXEVEvOto5R_-y8bSkw3cBHhR4joOZvpqxTVN0NVRsImtAxh6eMckEHsGlIofikerq24xqRJ2LzUilUFFH0vVpVnn5hjKL9d-hItm8GSAQY_gflVanlTcHfOz2dY-tR3Ft-TEjaYbQBbzCKQzV6aNo5lrUTgFWUBcxximTRUCiDZVzDB_0G-c9hoxMlb_h5aE3KIojL-P9GK0u8FsggqjikXt8m7KCB11fXXL-IHP5lxXolw_O0VYow2qCh__2kEWAoFonw4bINE5-l41puQ1Dz5oDxT5eT3qSfSW4OpQy1TnV1YYTRvRQP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P-tnpFu8iitbY6fJYF7n464fc_wZMl9fYvh5ItC7v-hVPH8dra463B79DerKziC7jKFyQRhGE5EKg-tYKz7bKc7T9V_77cH4xMB1Lop_5-r-PVtK9bED7VN9___8W4YTYHVj8tufD9vjARX-Zymk_JgmFoN4mEJSxc5hgdaqM6NrI74623gBBELS4ngOhI_iMnrToxsq0_o2L0wOUkASFk98cdkEnrgGeqMvUcIw69ffqh4fDi0UD3TIEh2NXNS2ebGlQ3KuL0tHM9wqRCfNnjRbt-MN-PfG4VySpEVskddB9pssWzDIkuzrv0EMfNlXlCirbQiOGPjqawaXfXILPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنجشنبه خبر داد که رفت‌وآمد کشتی‌ها در تنگهٔ هرمز پس از دور تازهٔ حملات آمریکا و ایران به مواضع یکدیگر، تقریباً متوقف شده است.
بر اساس این گزارش، داده‌های ردیابی کشتی‌ها نشان می‌دهد حرکت‌های قابل مشاهده در این گذرگاه حیاتی انرژی جهان عمدتاً در مسیری انجام شده که مورد تأیید ایران و نزدیک‌تر به بخش شمالی آبراه است، در حالی که کریدور مورد حمایت آمریکا و عمان عملاً بدون تردد بوده است.
@
VahidHeadline
راه‌آهن جمهوری اسلامی می‌گوید بر اثر حملات آمریکا به «یکی از ‌نقاط مسیر ریلی تهران–مشهد»، حرکت قطارهای مسافری در این مسیر متوقف شده است.
در بیانیه راه‌آهن به محل دقیق هدف قرار گرفته، اشاره نشده اما آمده که تیم‌های فنی و عملیاتی به محل اعزام شده و «عملیات بازسازی محل آسیب‌دیده در دست اقدام است».
توقف قطارها در مسیر تهران–مشهد ساعاتی پیش از برگزاری مراسم تشییع جنازه علی خامنه‌ای در مشهد رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76891" target="_blank">📅 10:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=E3BjfR1r6I5aZz4iKEeCoSaxpmtEg_VGwL3sAKHpbbWkQHixK_oUV1mFNJIiwLRgsr1jkDFwyy90bsehr9EucKjKb3uoMOIbesEZFSSsmWXkllJhQusP5f-jcJJhtiAwsTGl8ArqOeombvEn13zu4DofiRLzQHenelT3BPFe3wNUfiZ-WygDXXLnkw17W9-JiLnLaJrtm9FZQsRSLJdHunvRRXyM27dgTMDFoTfsF57gFEitj4eX6xQgBPtExStX8i8HPO1F1zwKkfEMUMs8M5Mj00eQZuB1ZAqiRPuTvHXFD08kkAeedI8ocfOHVukAfVBzqpk05N6s6dVP1FmVRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=E3BjfR1r6I5aZz4iKEeCoSaxpmtEg_VGwL3sAKHpbbWkQHixK_oUV1mFNJIiwLRgsr1jkDFwyy90bsehr9EucKjKb3uoMOIbesEZFSSsmWXkllJhQusP5f-jcJJhtiAwsTGl8ArqOeombvEn13zu4DofiRLzQHenelT3BPFe3wNUfiZ-WygDXXLnkw17W9-JiLnLaJrtm9FZQsRSLJdHunvRRXyM27dgTMDFoTfsF57gFEitj4eX6xQgBPtExStX8i8HPO1F1zwKkfEMUMs8M5Mj00eQZuB1ZAqiRPuTvHXFD08kkAeedI8ocfOHVukAfVBzqpk05N6s6dVP1FmVRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در توییتر میگن 'ترامپ به محمدباقر قالیباف گفته محمد سامتینگ':
twitter
ترامپ: می‌گویند یک محمدفلانی دارد آنجا با بیل‌ یک کارهایی می‌کند. بیل‌ها شما را به جایی نمی‌رسانند. بزرگترین ماشین‌آلات دنیا هم احتمالا شما را نمی‌توانند به آنجا [محل دفن اورانیوم] برسانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76890" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=kX-ns3h5A4AGkTA26wF5HRgNsaex9wPRcdbx3PGGGqUTH7TAb4cT36PZND-9N1WveG3roTch8_RHeRTaXH1bNLKf2Wvds_LysNTayAqlB8pWJZGJjM2c4Md_i-XrrQewZ51Oqeq6O9S_t3ToA6DWZcGSkpkxrGrbdRvQdebWPFslxaz4eMkr040UY5axutJ_Xr0DTyEtYl2p3nb14qii3pz1iLIMAIvV4ULTWmbynmris4BSnMKkewKHUOtKt53UNk0lJ23NE_gwgf4mvQVjG81m2OYPQHZ2q6NKgLMNzBJQuLE3iySW7dSZybN2lGOy_11R2lG1rp44UpMyiZs8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=kX-ns3h5A4AGkTA26wF5HRgNsaex9wPRcdbx3PGGGqUTH7TAb4cT36PZND-9N1WveG3roTch8_RHeRTaXH1bNLKf2Wvds_LysNTayAqlB8pWJZGJjM2c4Md_i-XrrQewZ51Oqeq6O9S_t3ToA6DWZcGSkpkxrGrbdRvQdebWPFslxaz4eMkr040UY5axutJ_Xr0DTyEtYl2p3nb14qii3pz1iLIMAIvV4ULTWmbynmris4BSnMKkewKHUOtKt53UNk0lJ23NE_gwgf4mvQVjG81m2OYPQHZ2q6NKgLMNzBJQuLE3iySW7dSZybN2lGOy_11R2lG1rp44UpMyiZs8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا از حملات به چندین هدف مختلف نوشت: نیروهای آمریکا دور دیگری از حملات علیه ایران را تکمیل کردند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۸ ژوئیه دور دیگری از حملات علیه ایران را تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
نیروهای آمریکا حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، محل‌های نگهداری موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
این حملات تازه در پی اجرای موفق حملات تهاجمی در ایران در شب قبل انجام شد.
نیروهای سنتکام در ۷ ژوئیه حدود ۸۰ هدف نظامی ایران، از جمله بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را هدف قرار دادند تا به‌دلیل نقض آتش‌بس از سوی ایران با حمله به سه شناور تجاری در حال عبور از تنگه هرمز، هزینه‌های سنگینی بر آن تحمیل کنند.
نیروهای آمریکا همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که از سوی فرمانده کل قوا دستور داده شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76889" target="_blank">📅 06:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
ترجمه ماشین:
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود.
مقام‌های آمریکایی به Axios می‌گویند طول و شدت کارزار جدید کاملاً به اقدامات بعدی تهران بستگی دارد.
چرا مهم است: جنگی که با هدف تضعیف توان موشکی ایران و نابود کردن آنچه از برنامه هسته‌ای‌اش باقی مانده بود آغاز شد، به نبردی بی‌پایان بر سر مهم‌ترین گلوگاه انرژی جهان تبدیل شده است.
یک مقام آمریکایی گفت تشدید تنش فعلی می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد؛ بسته به اینکه آیا ایران به حملاتش به کشتی‌های تجاری در تنگه هرمز ادامه می‌دهد یا نه.
این مقام آمریکایی گفت: «می‌خواهیم کمی بهشان سیلی بزنیم تا بفهمند ما شوخی لعنتی نداریم.»
محور خبر: دیپلماسی فعلاً متوقف شده و فشار نظامی دوباره در مرکز راهبرد رئیس‌جمهور ترامپ قرار گرفته است.
ترامپ روز چهارشنبه گفت آتش‌بس ۶۰روزه‌ای که در یادداشت تفاهم (MOU) ترسیم شده بود، پس از تبادل آتش ناشی از حملات ایران به کشتی‌های تجاری «تمام شده» است.
سپس آمریکا دور دوم حملات را در نزدیکی تنگه هرمز آغاز کرد، از جمله حمله به اهداف زیرساختی در داخل ایران برای نخستین بار در چند ماه گذشته.
ایران با حمله به پایگاه‌های آمریکا در کویت و بحرین تلافی کرد، در حالی که تأکید داشت از ادعای خود برای کنترل تنگه عقب‌نشینی نخواهد کرد.
کمی بعد، ترامپ علامت داد که آمریکا آماده کاهش تنش است و به خبرنگاران در هواپیمای Air Force One گفت مقام‌های ایرانی «کمی پیش تماس گرفتند» و «می‌خواهند توافق کنند.»
مشخص نبود ترامپ به کدام تماس اشاره می‌کرد و مقام‌های ایرانی نیز فوراً هیچ ارتباط مستقیمی را تأیید نکردند.
ترامپ اضافه کرد: «فقط نمی‌دانم شایسته توافق کردن هستند یا نه. نمی‌دانم قرار است به توافق احترام بگذارند یا نه. راستش را بخواهید، یک جورهایی دیوانه‌اند.»
طرف مقابل: مذاکره‌کننده ارشد ایران، محمدباقر قالیباف، آمریکا را به «قلدری و خلف وعده» متهم کرد و هشدار داد که تنگه فقط با شروط تهران بازگشایی خواهد شد.
قالیباف در X نوشت: «اگر بزنید، می‌خورید. تنگه هرمز فقط با «ترتیبات ایرانی» باز خواهد شد، نه تهدیدهای آمریکایی.»
تصویر کلی: بازگشایی تنگه هرمز و بازگرداندن آزادی کشتیرانی برای کشتی‌های تجاری، عمدتاً برای تثبیت بازارهای جهانی انرژی، به یکی از اهداف اصلی دولت ترامپ تبدیل شده است.
برای ایران، حفظ کنترل بر تنگه به یکی از اهداف کلیدی در هر توافقی برای پایان دادن به جنگ تبدیل شده است.
این مسئله یکی از بندهای محوری یادداشت تفاهم آمریکا و ایران بود و برداشت‌های متضاد از بندهای مربوط به تنگه اکنون باعث فروپاشی این توافق شده است.
این یادداشت تفاهم ایران را ملزم می‌کند اجازه عبور امن کشتی‌ها از تنگه هرمز را بدهد. اما اندکی پس از امضای آن، مقام‌های ایرانی آمریکا را متهم کردند که با عبور دادن کشتی‌ها از یک مسیر جنوبی در نزدیکی ساحل عمان بدون تأیید تهران، توافق را نقض کرده است.
پشت پرده: مقام‌های آمریکایی می‌گویند کاخ سفید معتقد است فضای بیشتری برای تشدید تنش دارد، چون صدها نفتکش در هفته‌های اخیر توانسته‌اند از طریق تنگه از خلیج فارس خارج شوند.
به گفته این مقام‌ها، همین مسئله نگرانی‌ها در داخل دولت را کاهش داده که درگیری تازه فوراً باعث جهش بزرگ قیمت نفت شود.
پشت صحنه: یک مقام آمریکایی ادعا کرد تشدید تنش فعلی ناشی از سرخوردگی عناصر رادیکال‌تر درون رهبری ازهم‌گسیخته ایران است؛ کسانی که معتقدند یادداشت تفاهم منافع واقعی برای تهران به همراه نداشته است.
این مقام گفت ایران می‌دید که اهرم فشارش در هرمز در حال لغزش است، در حالی که صدها کشتی از مسیر جنوبی نزدیک به ساحل عمان عبور می‌کردند.
با وجود معافیت‌های تحریمی آمریکا، ایران برای فروش نفت با مشکل روبه‌رو شد، چون مؤسسات مالی تراکنش‌ها را تأیید نمی‌کردند و کشورها تمایلی نداشتند به معافیت‌های موقت تکیه کنند.
هیچ‌یک از دارایی‌های مسدودشده ایران آزاد نشده است، چون ایران هنوز گام‌های هسته‌ای مورد نیاز طبق توافق را برنداشته است.
به گفته این مقام، توافق چارچوبی که آمریکا میان اسرائیل و لبنان میانجی‌گری کرد، بخش مربوط به لبنان در یادداشت تفاهم را غیرضروری کرد.
آنچه باید دید: این مقام آمریکایی گفت: «بخشی از رهبری ایران از همه این چیزها راضی نبود.»
«آنها شروع به تیراندازی کردند و ما تصمیم گرفتیم وقتش رسیده محکم بهشان سیلی بزنیم. این یک روند است. ما صبر داریم. اگر احساس نکنیم به توافقی که می‌خواهیم می‌رسیم، آن را انجام نخواهیم داد.»
جمع‌بندی: معاون رئیس‌جمهور ونس روز چهارشنبه گفت موضع آمریکا ساده است: تنگه هرمز باید باز بماند.
ونس گفت: «اگر تلاش کنند آن را ببندند، پاسخ ارتش آمریکا را در پی خواهد داشت.»
«یا می‌توانند از آن تبعیت کنند، یا دقیقاً همان چیزی را داشته باشند که دیشب برایشان اتفاق افتاد. این فقط ادامه خواهد داشت تا وقتی که آن مسیر را باز کنند و تیراندازی به کشتی‌ها را متوقف کنند.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76888" target="_blank">📅 06:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRzpc8hvuOHqq0NSMw-GAhpZtm9fkIMDK1ZNxUHW2rv8kTv68H0PnQzpwyzuGkzBy1ByIvcQWsPfzOJ6ZC0bT2UDTLpFvSFKf9ab0BueZGiuWjKj5RQF-pYqe4wVrPdfMQck_nrW1BAQMu50lVCHpt5PXctAqGIdO8luYuKDCCbVjV2MVi8IF1P8RUeTnFbty7zj0kbCHs97xIlSW4f-17UHyNJV13FsivvW9XcalwTUITIJSrAQ_1ZUFSw8548OJXQXq9UnrT8mzS4B23osATo2zZs456GE-R4P1uAQsfsQjUMrYibWFdGny6huN99IV--qDjgppgjAlzQAndf22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای که از صداوسیما پخش شد، اعلام کرد نیروی دریایی و نیروی هوافضای سپاه در «یک عملیات مشترک پهپادی و موشکی، زیرساخت‌ها و تاسیسات آمریکا، از جمله اردوگاه عریفجان و پایگاه هوایی علی السالم در کویت، و همچنین پایگاه هوایی شیخ عیسی و منطقه جفیر در بحرین را هدف قرار داده‌اند.»
@
VahidOOnLine
متن بیانیه به نقل از ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
🔹
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید، سرزمین عراق حبیب، مستکبران کاخ نشین را وحشت زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
🔹
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی پاسخ نخواهند گذاشت.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
و ماالنصر الا من عندالله العزیز الحکیم
سپاه پاسداران انقلاب اسلامی
۱۸/تیرماه/ ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76887" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlLxWQg96JhzS4BShKT9MJ8BVlKRD8JAWWOxILBailWywfc4oDRgYtS3e9SOvQy70H6SW747qgIvDk61Aq9-Xm3eMlmKJ63HITj0YWeutRKzfrlmGE_lzQDDrIaM1CFjKucPFLFZVFZXZTbXeYOvii2V5J-FbQbDWZHvxzujVkEpQkNyTWMBlT_b4LDPDttBRj4p_PwJnZupAiX0A4-jcrNiH7jO1L5aCe-DP6NzY6jQ4UsgwX2tea2N003tJ6Wgpp4byWHFiHI9gfm5rGCITIgjBTc7Ngcb850zaLIn7dueuHG68PSKuvQm5chlPMSdvp9EIdZHYUYx20sv6MsS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی:‌ 'برج مراقبت ترافیک دریایی بندر
#چابهار
که چهارشنبه ۱۷ تیر  مورد حمله قرار گرفت.'
Vahid
چند دقیقه پیش هم دوباره از سیستان و بلوچستان:
سلام سمت کنارک الان صدای انفجار اومد
کنارک رو یه جوری سنگین زد از خواب پریدیم
۴ تا پشت هم
از بوشهر هم پیام‌های تازه‌ای می‌فرستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76886" target="_blank">📅 05:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=l45WfZGzaBpccESTPSVgty3zc3GkgG-PqKvvZ_u7LmEAn9G6SVBxM3PEk6Ux-Era35ral3-Brj3Yks_YYVjyJf5nQIj7veGCePYzCUDzTr78rhe_bhIHr7pYqESCUH3UcDSbDuvkVnveXooUBmL3ygtJv2kYPN0vgcWVBok7EC-EeLJEJd_i2WM1YYMtZpE6xfSTV8IjPyNZrzAL9kw5I3YPsvnrTkDps_LUWxWuIa7coKPyaJl89cEK1NTJb9DzdzWeXJz2F9PywIeMoafo6SpJfyZd2IKjEJF--0fy9dqNNDjj6hZ2H8MOXHJLDdjUHp_zcPDYxXyv6HQ3Wsg2gw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=l45WfZGzaBpccESTPSVgty3zc3GkgG-PqKvvZ_u7LmEAn9G6SVBxM3PEk6Ux-Era35ral3-Brj3Yks_YYVjyJf5nQIj7veGCePYzCUDzTr78rhe_bhIHr7pYqESCUH3UcDSbDuvkVnveXooUBmL3ygtJv2kYPN0vgcWVBok7EC-EeLJEJd_i2WM1YYMtZpE6xfSTV8IjPyNZrzAL9kw5I3YPsvnrTkDps_LUWxWuIa7coKPyaJl89cEK1NTJb9DzdzWeXJz2F9PywIeMoafo6SpJfyZd2IKjEJF--0fy9dqNNDjj6hZ2H8MOXHJLDdjUHp_zcPDYxXyv6HQ3Wsg2gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد پنجشنبه ۱۸ تیرماه، در مسیر بازگشت از نشست سران ناتو در آنکارا و در هواپیمای ریاست‌جمهوری «ایر فورس وان» گفت آمریکا در برابر حملات ایران رویکرد «۲۰ به یک» را دنبال خواهد کرد.
ترامپ گفت: «همین حالا ضربه بسیار سختی به آن‌ها زدیم. هر بار که آن‌ها به ما حمله کنند، ما ۲۰ برابر پاسخ خواهیم داد.»
او افزود تهران سه کشتی را هدف قرار داد و تاکید کرد هر زمان حکومت ایران حمله کند، آمریکا «بسیار شدیدتر» پاسخ خواهد داد.
@
VahidOOnLine
پست قالیباف:
آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با «ترتیبات ایرانی» باز می‌شود نه با تهدیدات آمریکایی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76885" target="_blank">📅 05:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا در چارچوب حملات روز چهارشنبه، دو پل راه‌آهن را در شمال‌شرق ایران با موشک‌های کروز هدف قرار داد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76884" target="_blank">📅 05:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=Eu-bYrrSiS3IfjVbAz-YoWuj_SRfG_8oVo-_Gfc8BV1pjGOuWIjPflRDesfrWHnIJh7YvyKzi7fAiYNNSCK-J9DITXrXRqFBtzFK4S6tGk4mEb3P18EMI8Z485VEzurze0IPnoY1jnjOhBuVSXNn4iaRAf8_JxhqBl5Kux-dPzkvO3uU4371xkqvFCR_bNy09aYDdQa0_uuDgXp2gAM9iUxM_eg4vC0M3BGnML3VmTJA8XugUwAlKJgIbp644476gbmcK6f_oVvJsBLZZEjlqGIKsd3WvzOqVyljBcOGi6MrERHGuzn5Cgb57bT0Nrg5AWsordcbk51XDH091rWMgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=Eu-bYrrSiS3IfjVbAz-YoWuj_SRfG_8oVo-_Gfc8BV1pjGOuWIjPflRDesfrWHnIJh7YvyKzi7fAiYNNSCK-J9DITXrXRqFBtzFK4S6tGk4mEb3P18EMI8Z485VEzurze0IPnoY1jnjOhBuVSXNn4iaRAf8_JxhqBl5Kux-dPzkvO3uU4371xkqvFCR_bNy09aYDdQa0_uuDgXp2gAM9iUxM_eg4vC0M3BGnML3VmTJA8XugUwAlKJgIbp644476gbmcK6f_oVvJsBLZZEjlqGIKsd3WvzOqVyljBcOGi6MrERHGuzn5Cgb57bT0Nrg5AWsordcbk51XDH091rWMgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی پخش شده با شرح: 'بوشهر آخرین دقایق چهارشنبه ۱۷ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76883" target="_blank">📅 04:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oY4uUbiOwG-3-ZyBVfQ-YQNy7v2Q3hTPC8rgQHuDLBhqeIVo1IBAo9gx_cCnGFTpIZssju17OR6u0AOpHnUeoW_C1OsGLLcQUtH6oaZyk_rPOtB-OZzqdYyuaqgu-KcgAp_wVcU7ibfWmdmlAEUKiRsRkGPe9NTC-Pj0e5JbV_FlRFYBxEapXM6GkoeSpBaGWK09a6XkLVbL0miI-VZqiBdM7ggYb400gGz98rRy8zHKexJ22bKr_A9kut4emvzJQcdAUy4UwNWMj0ilWEdRpz8AWLBaRwcY81teW47h5RmJK9b16Fvsc36NWSI1Fw-Ioo3mFHbVU6IwXTLkQ_kHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی پیام درباره شلیک موشک از اهواز و امیدیه در خوزستان
و هم‌زمان درباره اعلام هشدار در کویت و بحرین
در خبری دیگر:
برای  نخستین بار در نزدیک به سه ماه گذشته چنین پیام‌هایی برای ساکنان قطر نیز ارسال شد.
قطر همزمان از میانجی‌های مذاکرات تهران و واشینگتن است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76882" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=eZDlkWyUPEQO8qbd1v9wqZyf8A8hcOT18TtzITcv4h7Y7xwttRxYldY5BXoPNXBhD2UJ6-R5ooH6w16wjHjLcsKwxJxsgQARV-A0OLm4VfxPNzeH0vUctch4gto30_rX26in76Bm9LA2x7YI1Kv7S6X7wVpkwLUr0-2ljopba4mIlXjXug9VilcBQFMUkS2BuA_FxgSpuBoeX3Qv1XzB5O12jKs_uqYXa6KIZbnv5UzjbqC9asQKuVTIj1oaKF9dhsRZoxI711hxhzr1ZT5Goiou0x2TXfBbVjeyBVoqWEpWaNVBxx1kt43gsVFmocbk9oMmS2J-hAkgZlfYXJm-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=eZDlkWyUPEQO8qbd1v9wqZyf8A8hcOT18TtzITcv4h7Y7xwttRxYldY5BXoPNXBhD2UJ6-R5ooH6w16wjHjLcsKwxJxsgQARV-A0OLm4VfxPNzeH0vUctch4gto30_rX26in76Bm9LA2x7YI1Kv7S6X7wVpkwLUr0-2ljopba4mIlXjXug9VilcBQFMUkS2BuA_FxgSpuBoeX3Qv1XzB5O12jKs_uqYXa6KIZbnv5UzjbqC9asQKuVTIj1oaKF9dhsRZoxI711hxhzr1ZT5Goiou0x2TXfBbVjeyBVoqWEpWaNVBxx1kt43gsVFmocbk9oMmS2J-hAkgZlfYXJm-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی و تصاویر منتشر شده با شرح 'انفجارهای حمله به آق‌قلا در استان گلستان'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76879" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wg4DL_lzaSE91tvJxBfq4oC1u4Pq9SHXIMNVPU5a4Gf54EUqm2Aox89HFzi41WpsDokpYnRgn5YmFg1Gm-F7ExncD6qwMS6tzIobFYpiHEda3bwwzhHH_9OgzdveLQ1XwFEaAXNIyHGU2anivriB4NorxbCxhOHZVyIwNuPvKX7lnqe1uL3IHVSwt7jbaVIzCyTezWEKiIMIDe-Yp4BxJTU4NXdT6sgFkmEqvLzOv-jppJEHg9THhn5WxVlvx8ms7D-7yBv-kJQSpZarK8HEbdKHV474pnGEAFX6P9HGljnF75UC88euOfHfNmlsgz-cn236JSdukbRudxoFjeK2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=MQVR5jrPo5ZJfDUDA2Omtd5jU9COfcDphyLliSXNmhNxpy8V6fmBeg1XCI3gDglmsfcBwGp9u3S4KYuaB2rmMJC6fFG3ijYv2vPObpsTuL0wnv2G6CRXnl8tCwVGJOjPN6KtUvwzq8QjmLz7mQ_8uWSiQsSiOYZuSXINnB3Sp2V2d7DQeeVxXmfw3iUYuOb0zbRJmZHQIKMn8mp4PvNJVezBQFqcS1ut6XJEA5GdmUBhbUAimJ90b7j4akAZOxGSK43NdDXaTzbJBew5OJysDJxbUmMnD3StNiqRvEHmYl8zWxzwLU8Nrjho1cIpPuhQPTI1sK6VGP_exABpfsHQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=MQVR5jrPo5ZJfDUDA2Omtd5jU9COfcDphyLliSXNmhNxpy8V6fmBeg1XCI3gDglmsfcBwGp9u3S4KYuaB2rmMJC6fFG3ijYv2vPObpsTuL0wnv2G6CRXnl8tCwVGJOjPN6KtUvwzq8QjmLz7mQ_8uWSiQsSiOYZuSXINnB3Sp2V2d7DQeeVxXmfw3iUYuOb0zbRJmZHQIKMn8mp4PvNJVezBQFqcS1ut6XJEA5GdmUBhbUAimJ90b7j4akAZOxGSK43NdDXaTzbJBew5OJysDJxbUmMnD3StNiqRvEHmYl8zWxzwLU8Nrjho1cIpPuhQPTI1sK6VGP_exABpfsHQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'شلیک چند موشک از جم در
#بوشهر
پنج‌شنبه ۱۸ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76877" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=RKQIiIQybmdU0iRyiXvV1YmDS2-qEIyoJcqB2LLO7HN1bPUjIqt1g-GaWJrm_31JzMtyKDC5ctDKGvtitwCF8NACBqLgw8_QBMQBSXZyP-jNfFEzO_23wt_HmZGSB_hezCvIGy0Z_m6Dtr0Waanp-Sgqx4347oCDpPLyFTTl01XkBtbUShavzo8OF1F2aypUOTyqMCUW7e9tfRnT70VIoRjz7Nk40ryhn0F325l2GlCTsYkL0LgL1_3KJq5cTl6kIFElCwnRyxrrurj_g-_IimrnG3sVOTWdZk4fjKM4oJq0KOaJ9OU4ee_5yxOJBWZsCEz7K1XhHopmG7mWPjYD_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=RKQIiIQybmdU0iRyiXvV1YmDS2-qEIyoJcqB2LLO7HN1bPUjIqt1g-GaWJrm_31JzMtyKDC5ctDKGvtitwCF8NACBqLgw8_QBMQBSXZyP-jNfFEzO_23wt_HmZGSB_hezCvIGy0Z_m6Dtr0Waanp-Sgqx4347oCDpPLyFTTl01XkBtbUShavzo8OF1F2aypUOTyqMCUW7e9tfRnT70VIoRjz7Nk40ryhn0F325l2GlCTsYkL0LgL1_3KJq5cTl6kIFElCwnRyxrrurj_g-_IimrnG3sVOTWdZk4fjKM4oJq0KOaJ9OU4ee_5yxOJBWZsCEz7K1XhHopmG7mWPjYD_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ویدیو: هوافضا ی چغادک بوشهر رو زدند
ویدیوی دریافتی، نخستین ساعت 'پنج‌شنبه ۱۸ تیر'
Vahid
📍
گویا اینجاست:
GoogleMaps
via
Mitch_Ulrich
🔄
آپدیت:
پیام‌های دریافتی الان دوباره ساعت ۳:۳۵
بوشهر دوباره زدن…
همین الان پنج تا انفجار بوشهر
سلام وحید جان ۳:۳۸ صدای چندین انفجار، بوشهر.
سلام آقا وحید بوشهر سه دیقه پیش صدا انفجار اومد
🔄
آپدیت:
بوشهر رو خیلی بد زدن.
ناحیه‌ی بهمنی، چهارراه ریشهر.
ساعت ۳:۵۵
سلام
بوشهر همین الان بازم زدن سه چهارتا پشت سر هم صداش خیلی بلند تر از قبلی ها بود
۳:۵۶
وحیدجان الان ساعت 3:55 صدای 5یا 6 انفجار پشت سر هم اومد، احتمالا از پایگاه هوایی بوده
سلام وحید جان بوشهر الان ساعت ۳:۵۵ خیلی شدید زدن پایگاه هوایی رو
دوباره صدای انفجار اومد بوشهر ساعت 3:55
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
بوشهر از ساعت ۳:۲۰ تا الان ۳:۵۵ کلی صدای انفجار میاد، ۳-۴تاش خیلی صدای وحشتناکی داشت!
الان بوشهر ضداى انفجار ٤ ٥ تا
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
چند انفجار هم بعدش شنیده شد که بنظر دور تر میومد
🔄
آپدیت:
بوشهر ساعت ۵:۲۲
صدای دوتا انفجار پشت سر هم اومد
۵:۲۲ بوشهر رو همچنان دارن میزنن، احتمالاً پایگاه هوایی
سلام بوشهرو زدن
الانم صدای فعالیت پدافند و توپ سنگین میاد
وحید نیم ساعت پیش صدا انفجار داخل بوشهر اومد نمیدونم دقیقا کجا بود ولی خیلی بد بود صداش
🔄
آپدیت:
دوباره الان صدا اومد ساعت ۵:۵۶
اطراف محله بهمنی بوشهر ساعت 6:01 صدای دو انفجار مهیب شنیده شد
ساعت ۰۶:۰۰ صدای انفجار مهیب در شهر بوشهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76876" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i_4tDcU_kXtTCKHui1wlRvmtRKXZ-POPmy1Ge9nVJgoUPexaNFQHmKlkjWVYuShzk9G4-Kr5Dmmi9JryuV_BQ5JA4x41sdLdJAiTOgc1qRSCuA9C6S1RGjqADINlyACH7D1xvmvxoQV40XkHPkC_v9H5hlQq7vtcdpEPfgQ3eDFHoWda4TOQh9dPAYNDEbeQ5znRBnMC8dnG078CYZRdLaTktnaFnbrC10ExIiAtUdQmUOfh8IWBZpQtkSltqrgKmXakTy_aNye17PWRo7J5muAqhNZg14bPamcAzAHThW4h8j7JheTITVHVT6AOVwhOjLIccHjSjMrlfCmZEuYP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S5qOw7NdufL6KmwTJ8F3X9R_lP7YpMlOcTxATqqzwXIGwxeySvDieLtcib3tYhJ-PyYKDi6Ectiq_iZx1pBEdib05KT1iJGKjR5oEFr1YdOoJIe6AT-IRaAu782pxW8iGfuXdk0g9yktsXhzsDqW6CUl7an-mnwka4XVKHf2HRxWo46W0Da7dPngP5ClwGJcbTTyu9o1LRDVI5EVUJbxN7I5Fjs_zY1zE7PtItvSmrkWT8-L4a0KxRNhmD--QhAVLXwtzCewIU3S5mXbZlDpts3E0xBJAeYBnyYXL2lLPKxnP3DWUQxINoAzC1uPKjfaSaZbxBpKFuCKjLG_5pmEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pyo1QG8H79abIaJhYDj1kPvGQNpPhM0nvU6GJDdBFOYQgWev3r-Y0Zu5O2dOoQuOFUjFWAju134GQQbBbvURcE1SqAtIJW2xcqlAhU1F06GOP5x7elIV7hjRrQfQZSFYqjiZ3h0bPxAbDOkH4lJy_qN5oDXdur5GQeVhPW4ns91LsDShmGxRQHepGb4FmN2h8kFDF7vl1Ib2KHdtTe-3wLJXILZU0wohnjMRsTsaCRVn8O4h0VXGG5nY7mmhuMzPfR1J2TG1BUXCl3sQDCe9emdUBELwsMEgIJ8KxvpWLOc7coqJRY1pW70cQekL6Wd0aTwvvYrSdsr9p5Otg4PMrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=FGwaN8feMLOs6TA_E2U-CGhAfcZoXekRI6UG5PXmFH7Js4-BpedyzYeU08eRIRgKKE0rLw5Vi_dvJ3qi3g5nra99tkUKALYDoIkdidDz_jmR4ZAdPuNS5FJ_gt-Ka2YrCY4ph4tl6HD-317hRx0vUvRoH93D-5Hoz5wSP5mtEZIjm6l8slxvRrklh4PKuJogqcboC5HVUGk-xgpZN9k_elzHACgMataVxWuDlRSOQRi1H2JMfps1qG4_kpl8iybsR5cZGdwl30UrDO2YWMaxhbawqpLJ8BxiBBF-GugZMzHIL9SPh62iLHeXqAzSXfohJddnZoxXs2ucySNTOJjvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=FGwaN8feMLOs6TA_E2U-CGhAfcZoXekRI6UG5PXmFH7Js4-BpedyzYeU08eRIRgKKE0rLw5Vi_dvJ3qi3g5nra99tkUKALYDoIkdidDz_jmR4ZAdPuNS5FJ_gt-Ka2YrCY4ph4tl6HD-317hRx0vUvRoH93D-5Hoz5wSP5mtEZIjm6l8slxvRrklh4PKuJogqcboC5HVUGk-xgpZN9k_elzHACgMataVxWuDlRSOQRi1H2JMfps1qG4_kpl8iybsR5cZGdwl30UrDO2YWMaxhbawqpLJ8BxiBBF-GugZMzHIL9SPh62iLHeXqAzSXfohJddnZoxXs2ucySNTOJjvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تصاویر با شرح پل راه‌آهن در نزدیکی آق‌قلا در استان گلستان دارند دست به دست میشن.
آپدیت:
منابع حکومتی:
براساس گزارشات منابع محلی اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا در استان گلستان گزارش شده است.
براین اساس حدود ساعت ۱:۳۰ بامداد هفت پرتابه شلیک شده که دو مورد منجر به انفجار بر روی ریل راه آهن  شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76872" target="_blank">📅 02:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EOPgPidcnZSNpasRvM-XorYK5klLBtF6mNihQ-0MNsvwxtCSd5wk3KauJq9VudW-lhmrplxz6mMIty4_GVgmBI5BxypqoxSGvQQnRscl9kPDA_JFEcm8lum3J8EBzJnFmigdy-OTA-Qq0Lg_LRSQYit8TKq37XsPOCFi9fRNp_p4DmhpzuGv-eoluWwQ829Sf3cDB9DjqOsiJkaEcW9jtI4w1wgXCE6LTDxzzRZWBe5sMfyJhEwSNQuKpEANwn8p42YiN7svnUqWnszGc4CPmITga76t-EeuA_6Pi6CvV06xaIKd66A9ZNj9HgzAawwqvK2kp176EIG14TQQOY57gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در نخستین ساعات بامداد پنجشنبه گفت که حکومت ایران پس از حملات مکرر آمریکا در منطقه با او تماس گرفته و خواستار دستیابی به توافق شده است، اما او نمی‌داند آیا تهران «شایسته» توافق هست یا نه.
ترامپ در گفت‌وگو با خبرنگاران در هواپیمای ریاست‌جمهوری آمریکا، هنگام بازگشت از نشست ناتو در آنکارا، ترکیه، گفت: «آنها کمی پیش تماس گرفتند، آنها خیلی زیاد می‌خواهند توافق کنند. فقط نمی‌دانم آیا آنها شایسته توافق هستند یا نه.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76871" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
استان گلستان آق قلا پنج شیش بار صدای انغجار و نور شنیده و دیده شد
سلام وقت بخیر ، استان گلستان هم زدن ، بالای پنج بار صدای وحشتناکی اومد
سپاه شهرستان آق قلا واقع در استان گلستان و حومه شهر گرگان رو هم زدن
سلام وحید جان
۵دقیقه میش گلستان رو زدن
شهرستان اققلا بدجور لزرید
۵بار لرزید ناجور
سلام وحید جان
شهرستان آق قلا بدجور زدن و مکانشو نمیدونم
کل شهر ریختن بیرون
سلام آق قلا صدای چند انفجار و نور رو ما هم شنیدیم ساعت تقریبا دو بامداد
۲بامداد چهارتا انفجار پشت سرهم آق قلا استان گلستان اخری صداش و شدتش بلندتر بود نور یه  لحظه دیدم ولی کجاخورد رو نمیدونم احساس میکنم دور بود سمت گمیشان رادار داشت قبلا
شاید باز اونجارو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76870" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LI3yJMdWhnVVNnNgAUMnplRw89gF67iEPJdJ9DFzKuQMTgX3bKAwf9ooGdpTAEdQwexYsSd9BpSayXnTwbICKrU22avsyvPaCPiFrEEHrEBr9NtVCfTamd-BY-0UCbuu52rQRtPUhM1w7VgmparqDZvjrDeiwYssYrXWJ4M6SGI1QD1H7i3yVW4PUFSfSuNaTP3XbXuBNNUSUd-gFO_D7ms_1paP1OR_85FSn9Al16P35b9gGs3NJPeZ9hjFdd8j7ZHR-RP0pTBglvJdIPiMwjckKBpMPngymjZiQY6MVBlVtu7RfoZz5gdnX4MjzMvOm4rh82Q7mpajvLddZU7_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f66b394713.mp4?token=dArYXVK8xiLbho0lVCpzAnNlqSvGln2p91we0d0HMojt1WADYaK-xwUALlwIWi0hqfTrUiKOB-cMPLH-yXCX_oz-oo8p3K4lw-ZztV4iegYr-iWyYzmY2Zu-r9kCUSNiXFbsFt7XgluDP5FkCcvp_BQvD2F77b-nabZehPXAB5CJrLc2UeRH3sLWogTh4UM5BzJ_l3RjDSZBhbkgSrN_RdBFkQV1X07lCkg_yhoAS3YMQPkmWY1IM1x2GduxyyfA4Mr7cF63XUiiUyyD9UODA96zsEFn26chhZJ6_aKgRfeWFOzLfT2Fg2UErp3xGT53q2FnBKt_UGWNKc65EPuGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f66b394713.mp4?token=dArYXVK8xiLbho0lVCpzAnNlqSvGln2p91we0d0HMojt1WADYaK-xwUALlwIWi0hqfTrUiKOB-cMPLH-yXCX_oz-oo8p3K4lw-ZztV4iegYr-iWyYzmY2Zu-r9kCUSNiXFbsFt7XgluDP5FkCcvp_BQvD2F77b-nabZehPXAB5CJrLc2UeRH3sLWogTh4UM5BzJ_l3RjDSZBhbkgSrN_RdBFkQV1X07lCkg_yhoAS3YMQPkmWY1IM1x2GduxyyfA4Mr7cF63XUiiUyyD9UODA96zsEFn26chhZJ6_aKgRfeWFOzLfT2Fg2UErp3xGT53q2FnBKt_UGWNKc65EPuGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر گزارش داد صدای چند انفجار در منطقه شمال شرقی «ایرانشهر» واقع در استان سیستان و بلوچستان شنیده شده است.
این خبر هم‌زمان با ادامه حملات آمریکا به اهدافی در جنوب و جنوب‌شرق ایران منتشر شده و جزئیات بیشتری درباره محل انفجارها یا خسارت‌های احتمالی اعلام نشده است.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام شهرستان ایرانشهر روزدن
سلام ایرانشهر هم سمت فرودگاه زدن
سمت ارتش ایرانشهر انفجار شده
سلام ایرانشهر سیستان بلوچستان ساعت۱۲:۵۹صدای انفجار میاد
فرودگاه ایرانشهر میگن بوده خودم ندیدم ولی صداش خیلی شدید بود
سلام ایرانشهر سيستان بلوچستان همین الان ساعت ۱۲:۵۰ صدای شدید انفجار و پنجره ها لرزید.
فرودگاه ایرانشهر
پنج دقیقه پیش سه چهارتا صدای وحشتناک تو ایرانشهر(بلوچستان) اومد در حدی که شیشه ها تا مرز شکستن رفت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76868" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YLeXGlM-v5uYJzAY4u6D7RF0vKvjz2WijmuJvt31MJ0363pcF6uFWibfvQ5pgFZMIlegV7Ekb1EOWcOQSNKhNFCSkPOdnOBIpPF6X8eXLrP1yW_qcfglh_uvN0za0GYZRnAe7PAnd0fJ2T614YstMXNsZP3oVeGokDnlAtO3qDF7EE5m61z3ZKMcIueivQX4_eWiCSwvXgB9hSZevLvQZrsfzBGpP6UiLBA36A5ijsuIlKTUH8x9OA9rDqN58O6GqU-QyCmKj4UFHp-hDcHp5-cVtOXqQ902chHWS4X21wCmpNXDL7ycKiKwj_axRwvronwJZPDRiN4nLPJwQNB6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته "این در تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، خیلی بدتر خواهد شد!"
بیشتر از ده تا عکس و فیلم با شرح حمله امشب پست کرده. حتی عکسی که اشتباهی بعضی از منابع پخش کرده بودند:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76867" target="_blank">📅 01:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=tDHMXncrm-WM05sCeJX4Tc_NexaXB2x2qqHwF9ECTtxYno_Fk1OoMrpKdp7lt_OugS9L1ntJQmFe_pNKJTwcVyWfkX7Y70CGIWUvPvAkV5cGJAXj4lA7-SVjl8VSyWbVFOn_jGKG0pJ8dygyxLROc8AJmGfbLC_D-_Sk-myHJmno8XuToTcYpyrbKYD-Rf25RhE0fRdcQelevlHiAU0XYNgQGARzPoQR4hqyuOwgkHX3khIWKK03Xrnm_uOotjH6N5WBf0CCMYqikbSMaDiwdyzzqBJkf-A6cjvmOaShcohEe_jHKW1iT3srVexXEwFOLgl91EdyZ6Ke8uxUkOsy5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=tDHMXncrm-WM05sCeJX4Tc_NexaXB2x2qqHwF9ECTtxYno_Fk1OoMrpKdp7lt_OugS9L1ntJQmFe_pNKJTwcVyWfkX7Y70CGIWUvPvAkV5cGJAXj4lA7-SVjl8VSyWbVFOn_jGKG0pJ8dygyxLROc8AJmGfbLC_D-_Sk-myHJmno8XuToTcYpyrbKYD-Rf25RhE0fRdcQelevlHiAU0XYNgQGARzPoQR4hqyuOwgkHX3khIWKK03Xrnm_uOotjH6N5WBf0CCMYqikbSMaDiwdyzzqBJkf-A6cjvmOaShcohEe_jHKW1iT3srVexXEwFOLgl91EdyZ6Ke8uxUkOsy5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'همین الان پایگاه نظامی بین چغادک و
#بوشهر
'
پنج‌شنبه ۱۸ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76866" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BoKwzxW0dGxSXBZSHh2sHCJFa5fX6_kNyyJKXfYmVeaj5frxEsv0ivwxj4Peo0Rz7dyewsvlN0YBpXSgRqMaLr24ytR5Dvlss_PvcWMsGA57ivdUuxrBg_M0rIPxkWtzZ67A70FKIsf_iXWwqJe-3uWbfsO_ITxY1wFUjMxCUkhIo4OzU0IVZZoAf0g08jSyDAn_NzlR54zfKQ4DiP42oWv3USxONZB9K4-C-Gcq_cJPAjJGbK2fVtM93LhF-wE3yKBp5G9Em8wzk3KdPYIXsIYRMvvMpwmxwUOuByrL6-ZHbIUu7kDNW7yrtlV_MdpZ0G-zleecSD-NX-P2jnMylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JVmcC0sN_Sk36ywwNh0XuIonRSkjlwe9bMStX4CIYsHxCIfHtmOrxdIecmy-AtlfSlI0kD3FH80yI_M00bRla6xgEXSDC1wyIBs2xX6DCgDQJkUCPArMCeW5ymeFT2UG2xrn5CQy-zXGL06M6WGKIMW-yN3ioXpKNlQsn1jX4C9uRrNwzu9Ekaa_5E4OS5Pul-HuTyg8_pQyZfEsDRBSDcuT5-rBoX6mqJr3Q8J9FnBRMlQrA-he1suwrYZQ4WnA78uF9ta0rX3W7bCasguJvrviu1eTEyTbMPciLWT67Gzdsm0KuAQ6tpTZKpn1Z2ok6SWfxO96K4VLfUz-3aCyeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=ih9cX2MHD0AW4ONRyP76JYHAfKIxhG6Po6tl2UExZehajV7ARodt67HGVleG4L4zJ-fnpbHTl-ex9ithQNWIKTemu8ViyfSoOe5GVq57XTYviooSiF7GMmtY2V1FI_Nal3OjNDj4o9VdMdQjmvKhnO34Xsa4y4-Rcp7a1qZAhqZx5B5xXDhrXl_0znyqTbiwoG7a0Xehw0l7E8e4--d_-dzTKGKBWX-kJmdatUvG8kyRgGQ-ENGmRp00ojsxr6U5l9eReF6gYSnCnCT0pDjUb6MQoxehte6jKTa67AHxt7AU6IX-YKAltZwncoyVURCbg82JjgzhEv-ZQOaciGvcLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=ih9cX2MHD0AW4ONRyP76JYHAfKIxhG6Po6tl2UExZehajV7ARodt67HGVleG4L4zJ-fnpbHTl-ex9ithQNWIKTemu8ViyfSoOe5GVq57XTYviooSiF7GMmtY2V1FI_Nal3OjNDj4o9VdMdQjmvKhnO34Xsa4y4-Rcp7a1qZAhqZx5B5xXDhrXl_0znyqTbiwoG7a0Xehw0l7E8e4--d_-dzTKGKBWX-kJmdatUvG8kyRgGQ-ENGmRp00ojsxr6U5l9eReF6gYSnCnCT0pDjUb6MQoxehte6jKTa67AHxt7AU6IX-YKAltZwncoyVURCbg82JjgzhEv-ZQOaciGvcLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر بالا با شرح
#چابهار
پخش شده‌اند.
در خبری دیگر:
خبرگزاری تسنیم گزارش داده است که جنگنده‌های آمریکایی پایگاه امام علی ندسا در چابهار را بمباران کردند.
تسنیم اضافه کرده که تاکنون صدای حدود ده انفجار در چابهار و کنارک شنیده شده است.
برق قسمتی از شهر چابهار نیز قطع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76862" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=u78WRQli22QqAyXnxq_pDBN69KT71zFcQxjZc0qM-RtgjiiPQ460oW8c_KEIgKCE9Ol6e1bHfMriQE5K7Q9oMM6liNEhjbeu7ok7bLjE2ccA1sO5pI_9TEBst0SGaa5ogFLwr3ajYznfZGd3azd5EBhGFc1yB1CMhfS-_CE-3NvtI9aldwnXJyIP1tkkUaoLBfqZhf-k4VGiJV5YpVvafUvkxg_qCBgD4zwUQFGjZ3obxFc1ofXHuP3no7VpncgIRqUI3pws7N0qyCKH64SGFYF_GFJWmAyI-gVlkceshN7v531UQL3NPFuLBLLk-DAhWs2Qrkg8IuHv-73jplnJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=u78WRQli22QqAyXnxq_pDBN69KT71zFcQxjZc0qM-RtgjiiPQ460oW8c_KEIgKCE9Ol6e1bHfMriQE5K7Q9oMM6liNEhjbeu7ok7bLjE2ccA1sO5pI_9TEBst0SGaa5ogFLwr3ajYznfZGd3azd5EBhGFc1yB1CMhfS-_CE-3NvtI9aldwnXJyIP1tkkUaoLBfqZhf-k4VGiJV5YpVvafUvkxg_qCBgD4zwUQFGjZ3obxFc1ofXHuP3no7VpncgIRqUI3pws7N0qyCKH64SGFYF_GFJWmAyI-gVlkceshN7v531UQL3NPFuLBLLk-DAhWs2Qrkg8IuHv-73jplnJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#چابهار
، انفجارهای حمله ۲۳:۳۰ چهارشنبه ۱۷ تیر'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76860" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پیام‌های دریافتی:
چغادک بوشهر رو همین الان زدن چند تا انفجار خیلی شدید
سلام ساعت 00:28 دقیقه چندین صدای انفجار در بوشهر شنیده شد
00:30 هوا فضای چغادک 15 تا صدای انفجار
همین حالا بوشهر زدن
حدود پنج تا شش بار خونه لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76859" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76857">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aw29LaRjMMLlDXCNcnphB12Y8nCODGUKTFbzms4jIRRFRPkEOvxGzofQvZdSYBMCb1ZcNsZIpNwkXctF4O3ta-qYHo-E_7_tfmRwsSZpCBGnXt_d2w6mHPbDmI7Avg9e7kzlgIJMTMSeKAUTDNjuhmPApmEUUGs_Pv7RxUAlFnBKJpJNJvxlyRvIIH2bFf92RQlmQM2Boco-z9jT4hLc9gPJ0bFj8UCRExI4WkAaeq4D5SVFaF5P7AKMfwl426yIzJ9dcDzI1cHQFlLGM0RXMaiFW-XPTN0FT4tEOY6YLnVR9LiugZ8u1ytEKklb4NyKR2ONgpZO-yeBDOwXgOcEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=p-DUSNvV8lZsWkKW8SVdkBYtpsNQ_6_RWyJvsO5EhGrcVAdZSuJxh7D_hqNGpNLRucehihEs2nyDGWLHPCVdgIeGSL_-EPOSFOQVv5do_R0vXUn4g58tDxY3c7_JXEDTpCYC2nz-rt4f7NHBg76WUcPWHKh7xJ5YSTbcouoFaJScBxUUfFanD0ga2tOhFao_ICnA3yOo9wcXZsUd57BSdtzwABtd9jDylIfa_R7etk51oRPbDi0Vs_BijczRpTyP2Nd7F8HD0FPSRUriuQgD_Gp38_tl_HsRgO3HogqihDut4QRKG7Z_aPrTxtLtfPr_jbsUSUFyn7iFGzgAS4tpoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=p-DUSNvV8lZsWkKW8SVdkBYtpsNQ_6_RWyJvsO5EhGrcVAdZSuJxh7D_hqNGpNLRucehihEs2nyDGWLHPCVdgIeGSL_-EPOSFOQVv5do_R0vXUn4g58tDxY3c7_JXEDTpCYC2nz-rt4f7NHBg76WUcPWHKh7xJ5YSTbcouoFaJScBxUUfFanD0ga2tOhFao_ICnA3yOo9wcXZsUd57BSdtzwABtd9jDylIfa_R7etk51oRPbDi0Vs_BijczRpTyP2Nd7F8HD0FPSRUriuQgD_Gp38_tl_HsRgO3HogqihDut4QRKG7Z_aPrTxtLtfPr_jbsUSUFyn7iFGzgAS4tpoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون ریاست جمهوری آمریکا درباره درگیری‌های تازه میان ایران و ایالات متحده، با تشبیه تفاهم آتش‌بس میان دو کشور به یک «معامله» گفت:‌ «توافق اولیه‌ای که ما امضا کردیم این بود که اگر آنها از شلیک به کشتی‌ها دست بردارند، محاصره [تنگه هرمز] را لغو خواهیم کرد، اما ۲۴ ساعت پیش چه اتفاقی افتاد؟ آنها شروع به شلیک دوباره به کشتی‌ها کردند.»
آقای ونس با تاکید بر اینکه در صورت ادامه شلیک به کشتی‌ها در تنگه هرمز آمریکا ایران را نابود خواهد کرد گفت: «حالا، رئیس‌جمهور ما گزینه‌های زیادی را در نظر دارد. بدیهی است که من نمی‌توانم بگویم امشب چه اتفاقی خواهد افتاد، اما رئیس‌جمهور خیلی ساده به آنها گفته است، تنگه هرمز باز خواهد شد. این بدان معناست که نفت و گاز به سمت مردم آمریکا جریان خواهد یافت. به همین دلیل است که می‌بینیم قیمت نفت و بنزین شروع به کاهش کرده است.»
او گفت که تاکید ریاست جمهوری آمریکا بر باز ماندن شریان حیاتی مهمی در حمل انرژی جهان است و «این چیزی است که ایرانی‌ها باید بدانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76857" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان شش انفجار در بندر جاسک
ساعت ۰۰:۲۴
سلام وحید جان جاسک رو زد دوبار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76856" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bF_oyzT718RBciBZOsyhgTT6MsgX1kLaKnxPHbCT1y7VXx3drNl7ZcixnDawSv93A4XOjh5-yC5bOBkprxs9rdCukHvSpFxkuwgJSyV3Vx6BcZkHd-YLIL17VYNNsVljSWqFrhWEd2m5CpXpS5unOoA54zGka55aaKYIHOK6CSjQDQbKQHhSLsgeg3x4V-kMARO20VGbSO8imwJYoOkoYpgXI2MU3SmeALgKqkVHN7k8t66yZlawVDtRqLdWWNT78iITtycuWTlHYziXD7vrD7GI4ORre2hWM2v3zRsWtLoX25irDLHLadJ4bPksPK2ygHSLOIgBc8fCpINCAZvN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=ZPhCbCfcb2dwdXc83JS1KU89JDU39hk9PHGPKBIauAmNWyeTS2vRY6dy-pDUeetRIws0g003cLkcNKqvd3u0-mgXXbeIssGrfz96YrKnFuKMQFdCbAG3zvwbbzmzyFn7Phz2qWYwXmFFH9nvOToKKMP9vHKiL3dd512pQ_7uf666oM68C9fwx4Aew6fivfjNekNX5moQNGjcTBmKFgIqcRDPwT_XI3EQzZc7gFgWFE147oLqzdSvRHvEvgGHfNWJEqslCOVRzUxs9pI90z7MA16kL05rmT9SNCdJjzm6YLr9zDGaeo6ZrLqRpQov5cdrSUK6_IOY7U5VfauEhKSl-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=ZPhCbCfcb2dwdXc83JS1KU89JDU39hk9PHGPKBIauAmNWyeTS2vRY6dy-pDUeetRIws0g003cLkcNKqvd3u0-mgXXbeIssGrfz96YrKnFuKMQFdCbAG3zvwbbzmzyFn7Phz2qWYwXmFFH9nvOToKKMP9vHKiL3dd512pQ_7uf666oM68C9fwx4Aew6fivfjNekNX5moQNGjcTBmKFgIqcRDPwT_XI3EQzZc7gFgWFE147oLqzdSvRHvEvgGHfNWJEqslCOVRzUxs9pI90z7MA16kL05rmT9SNCdJjzm6YLr9zDGaeo6ZrLqRpQov5cdrSUK6_IOY7U5VfauEhKSl-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'بوشهر، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۴۵'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76853" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=uTTOGTi9o_0ZIFJftJsHWGrQeJBdMQq6NfZH0WNyT_yqlYTr1Wa6oxU1liKg41igHchNnzMjP1sYUq69JUenPPFQSgd61NMm352lP8llh6_jrw9Q2iXW80gFz0AjFz-FfX_uMiNy7l9ci5a0X-IHxfYeI3zM141qFNe7a40xiWMghQHhtbNMn42CiZmKyODzEebQY_2eaqldacN4ZXsorCIgvyRTjTLxZjDE3GY27NVPV9yFHeiG456njlSyd5vlNzEATvBr-xSyOMgZBKfLEo-FWN8ahMU8P21Yl6v0a6WKBdLP3DEtBXcnefsAqwH9oWSJbNUGCEPNmiWz8OLY_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=uTTOGTi9o_0ZIFJftJsHWGrQeJBdMQq6NfZH0WNyT_yqlYTr1Wa6oxU1liKg41igHchNnzMjP1sYUq69JUenPPFQSgd61NMm352lP8llh6_jrw9Q2iXW80gFz0AjFz-FfX_uMiNy7l9ci5a0X-IHxfYeI3zM141qFNe7a40xiWMghQHhtbNMn42CiZmKyODzEebQY_2eaqldacN4ZXsorCIgvyRTjTLxZjDE3GY27NVPV9yFHeiG456njlSyd5vlNzEATvBr-xSyOMgZBKfLEo-FWN8ahMU8P21Yl6v0a6WKBdLP3DEtBXcnefsAqwH9oWSJbNUGCEPNmiWz8OLY_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'چابهار، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۳۰'
لحظاتی پس از حمله آمریکا
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76852" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان بوشهر ساعت ۱۱:۴۸ دقیقه بد زدن
بوشهر ۲۳.۴۸ یک بار انفجار
سلام وحید جان
بوشهر ساعت ۲۳:۴۸ صدای دو انفجار اومد که از صداهای صبح شدتش بیشتر بود
سلام بوشهر الان صدای انفجار اومد
اقا وحید بوشهر همین الان زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76851" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار بندرعباس
باهنر
بد داره میزنه
بندر دوتا صدای انفجار امد
بندرعباس منطقه ۴ انفجار های شدید و پشت سر هم
بندرعباس ۳ تا انفجار پشت هم 23:45
سلام الان ١١:٤٦ دو انقجار با موج بلند در بندرعباس
بمبارون بندرعباس شروع شد وحید جان
ساعت ۲۳:۴۷
اقا وحيد الان بندر عباس صدّا چند انفجار شديد كه پنجره ها لرزيدن
ساعت 11:45
چند صدای انفجار بندرعباس ساعت 23:46
سلام صدای سه چهار تا انفجار شدید بندرعباس اومد
بندرعباس الان چندین صدای انفجار پشت سر هم اومد
سلام
23:47
صدای 6.7 انفجار از دور
قشم
سلام بندرعباس صدای انفجار مهیبی اومد
بندرعباس سه تا انفجار پیاپی و مهیب
صدای بیشتر از ۸ تا انفجار این سمت باهنر و اسکله اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76850" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DmiAQ2b8LmW7aPW1oHlXoKgJGWczQ9Ck5MUtq2fYL7y3vDnR2hTQ5QdnoxJC_hqLQizJybAm2a5Vp4ez_vPedGTx6xsULfU1HdCaq__bUdsb_wQOHWXhAEN0O_ByaIDK2i-b81rjWIgw60peAVdgfUPytT3ytVRvQzttah_G51nFmvy6Agw4vQE8g2kYY0Is06xPfI6zG_QWScmL3i2wCofxXzbyeCXKa0BCoKn2qwBnMX0kLVPO7D9tL-Omb2NWmc93UHgJlYh2s5KsSpTDQHEVpy3jZcRQz4_V2anvWO9niPRSIeRw8FCLKR20oMy5uRQnpcu1Z9Xzx2zIRX3uVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی آمریکا اجرای حملات تکمیلی علیه ایران را آغاز کرده‌اند تا توانایی این کشور برای تهدید آزادی کشتیرانی در تنگه هرمز را بیش از پیش تضعیف کنند. ایالات متحده ایران را بابت تعرض بی‌دلیل اخیر علیه کشتیرانی تجاری و خدمه‌های غیرنظامی که آزادانه در یک آبراه حیاتی بین‌المللی تردد می‌کنند، پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76849" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
صدای انفجار چابهار
فکر کنم کنارک بود
چندین صدای وحشتناک  10تا بمب زدن
۵ تا صدای انفجار شدید اومد
چابهار
داداش الان چابهار رو هم زدن
7 و 8 تا صدا اومد
ما تو روستای رمین هستیم برقا رفت و صداش اومد خونه لرزید
سلام کنارک وحشتناک صدای انفجار اومد
چابهار زدن چند تا انفجار شدید
ما کمب هستیم واقعا درهای خونه ما بشدت لرزید
صدای انفجار از زمان جنگ هم بلندتر اومد
دود غلیظی بلند شده که تو شب هم کامل معلومه
از سمتی میاد که پایگاه سپاه اونجاست
البته ممکنه نقطه زنی باشه
الان 3 4 بار دیگه صدا اومد
جدا از اون اولیه
مجدد زدن با جنگنده
فک کنم اسکله سپاه بود چابهار بود صدا نزدیک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76848" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MshS_zd5QTbFh_GN9gSXib_ZrGeAmrKqLSTaFNOxniKIGrmx059gLOI4p-rtAZ4iQ-2fdfHj7phiYthjt7JRM-B0CBZGdjMWfrrxFhcRfH0ooJQJZGZroy778dYoPh14Z9CwLA5ryNcxIdwOW2R9S0J90S3RQmfmkBDSUzeSR08hhdHgjCzjh_mfJWwZKgC7dmXlbNLphS8OQA4illoXjMu044EPdM2UlNd5AWGhV5ffhNC3z0c3Is4gCyTUJWwqH-f6QlAi1IPBZtYXDz9a_s-YraPL0wuPu81H6eJBnI_QKAbt6i-WP0Lw7d0BlZaj2IkioYPRl-0GS_7btJ-qXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری‌های فارس و مهر شامگاه چهارشنبه ۱۷ تیر گزارش دادند که حوالی ساعت ۱۱:۱۵ شب صدای چند انفجار در بندرعباس و شهرستان سیریک شنیده شده است.
بر اساس این گزارش‌ها، شماری از این انفجارها از سمت دریا و در محدوده ساحل غربی سیریک به گوش رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76847" target="_blank">📅 23:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">(
⚠️
۴۰ دقیقه، ۸۰ مگابایت)
کل سخنرانی ترامپ در نشست خبری اجلاس ناتو با زیرنویس فارسی ماشین
دونالد ترامپ، رییس‌جمهور آمریکا، با اشاره به رهبران جدید جمهوری اسلامی گفت «ممکن است آن‌ها هم از بین بروند». او هم‌زمان تاکید کرد که درگیری با ایران طولانی نخواهد شد، اما واشینگتن در صورت لزوم به حملات خود ادامه می‌دهد.
ترامپ روز چهارشنبه پس از پایان نشست سران ناتو در آنکارا، در کنفرانس خبری خود از نحوه مدیریت جنگ با ایران دفاع کرد و درباره رهبران جمهوری اسلامی گفت: «آن‌ها رهبرانی داشتند؛ دیگر نیستند. حالا مجموعه دیگری از رهبران را دارند. ممکن است آن‌ها هم از بین بروند.»
او افزود: «ممکن است من هم کشته شوم، چون من هدف شماره یک آن‌ها هستم.»
رییس‌جمهور آمریکا در بخش دیگری از سخنانش با اشاره به تشدید تنش‌ها میان تهران و واشنگتن گفت: «فکر نمی‌کنم جنگ دوباره آغاز شود. آن‌ها چند کشتی را هدف قرار دادند و ما خیلی شدیدتر پاسخ دادیم.»
ترامپ تاکید کرد هرگونه درگیری احتمالی «خیلی سریع» پایان خواهد یافت و افزود: «هر اتفاقی که رخ دهد، خیلی سریع تمام می‌شود و فقط اوضاع را امن‌تر خواهد کرد، از جمله برای نفت. ما به دنبال یک درگیری طولانی‌مدت نیستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76846" target="_blank">📅 22:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eojGcYoar86uIP5smGfT6haun-HTm0KVgQiv5w3GAPW7EKW7oPYsz5Dy41FTrwfm0dsiFT537guyJDIg6nmjQuCUV5fPjjoDDq41Ax__QrvXmBSqt6mrYq8cbkYfmyFGbmLQLXUxDDoo6lXNlomNq0RDRgu5QQMaJokBdmgmThTTj1OFzzB3ezIHyrjT16P8iyyDvJmnZy4j0ywOFfsq4qNGsYWTN2lhe4xO4FE3rsbZoH6v8jRlEwpxybL6OfreIhbYMPs8BiI2J1qvqICzYm92rRKB8W0t-ZR3Tvqmy0eT0bRqR2pI5sDBKR4oxdJCZoVW7sN411tAi-d8gAxj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی با انتشار بیانیه‌ای اعلام کرد که در پی حملات آمریکا به مناطقی در جنوب ایران، هشت تن از نیروهای هوایی و دریایی ارتش در بندرعباس و بوشهر کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76845" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lS9GYh5L54v3JOXfbjF5a1MCYspUivelXbqK9HLmcfAgmScqwacS2AHW6KPbxV9XgYLzeYr9JD41An4te53VG1BRyLXSmRB6kO3NZOKDSKVxlkNfidy6tGP_ooaeEqEvmP2qCKVvRJJopbLN1z0iKE0hPhcAs2gMSkPBF4qWs4NE9ioB586PdyX9f2B6OqmODi8F5Z3q8IJBRDDshlmoEUNpPRQ9-19tR0MDWTI1xbUf6Z3tW1IhLwPbvGVhjXj5ons3tB4iOrCeMQ6TCuU54dRM6YyuIX_Nv6baETU-gnYm9UJIl4l4oXu5QJ0mX5DwoJcRHtF9C_GbEt-zLLOMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=CgDxqEUQZfpd2yby8_1SXNqK8K--2fNvTZUXitIFJ4UdbcoW2q9cztvQD0JmDrxJHtGWIZ5fAUZ9zL31Xh68E-OIq0hc9_PHxNtd3l8BnVvlq5CtrTr_xORtJPZPigpAKUOQi84mWweQ2CFB4Vzl4F74giDiQXHCjr9Wa3KThl-qMwEy9a4ZslYH0VB_yJyqpNmVoX4TckkvwknjFqXuDaasXRo2Fg-SHk3vhgb_PrSVQZplhUElxarPTJwbTpLfTixQP_WMgSiGJ-fID5HBvLF54nSj1Z1fJXx2tQOSY6CdbLEidw7jpRCXx5MeDPfOOsD1e_miJV41H2QtlmrPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=CgDxqEUQZfpd2yby8_1SXNqK8K--2fNvTZUXitIFJ4UdbcoW2q9cztvQD0JmDrxJHtGWIZ5fAUZ9zL31Xh68E-OIq0hc9_PHxNtd3l8BnVvlq5CtrTr_xORtJPZPigpAKUOQi84mWweQ2CFB4Vzl4F74giDiQXHCjr9Wa3KThl-qMwEy9a4ZslYH0VB_yJyqpNmVoX4TckkvwknjFqXuDaasXRo2Fg-SHk3vhgb_PrSVQZplhUElxarPTJwbTpLfTixQP_WMgSiGJ-fID5HBvLF54nSj1Z1fJXx2tQOSY6CdbLEidw7jpRCXx5MeDPfOOsD1e_miJV41H2QtlmrPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری فرانسه، چهارشنبه در حاشیه نشست ناتو در پاسخ به خبرنگاران گفت حملات جمهوری اسلامی به پایگاه‌های آمریکا در خلیج فارس، توافق موقت را نقض کرده و تهران در انجام این حملات اشتباه کرده است.
امانوئل مکرون در عین حال گفت انتظار دارد نشست‌ها در چارچوب آتش‌بس ۶۰ روزه میان آمریکا و جمهوری اسلامی ادامه یابد.
@
VahidOOnLine
فریدریش مرتس، صدراعظم آلمان، نیز در حاشیه این نشست گفت: «ما به دونالد ترامپ گفته‌ایم که باید یک توافق پایدار با ایران حاصل شود، اما این ایران است که مسئول آخرین نقض توافق موقت آتش‌بس است.»
@
VahidOOnLine
دبیرکل ناتو، حملات تازه آمریکا به مواضع جمهوری اسلامی را «کاملاً ضروری» خواند.
مارک روته، پیش از نشست سران ناتو در آنکارا به خبرنگاران گفت وقتی آتش‌بس برقرار است و جمهوری اسلامی «عملاً آن را نقض می‌کند»، واکنش قاطع آمریکا اهمیت حیاتی دارد.
روته روز سه‌شنبه نیز گفته بود هرچند جمهوری اسلامی در حوزه موشکی و هسته‌ای تضعیف شده، ناتو همچنان باید نسبت به تهدیدهای آن هوشیار بماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76843" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Apc-suF6wfbgBVJAt2oHd47hvzBLkwXiFSDoD9uTbo_vMYQCQnlJ7OVFCAJ1x5quJmRi5iAvJ1myjlMcnFy7TdUjx6dztRjtPJfkAH6UnEtrtouup5wYd7BXInuazodu21XrZCSSKA-FcTPdt5F-zBY65uWfWb-9mayJeIiAaAWlxQsTTTM9Uv3cOpap1HDeA0ZGBwKbCVpdRvxUEM-5j1ijdZk92MCgZpAasJ6urcZCi9tfEq8TbAbbTFzhPOA_UwrqoB1FZ-LrLGX4nLn_tLitdPtyG_5HkiPAbfyQYkrZdkprf4YhnbA3HMKul37HILiMHLa56Jg8NwH8MWaKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Orn_t-xqucoTt6uc0Loy-0udNF9mTgwaIcWv81D8r0x4zsoYMiO7uxaKhrsTN469HtioRHMxh4vM9rW6CmoZrTYwvLh2531QzAKVnBM8Iwr4mzNLOszLVY2IXbStPnpepKc1n5nuLR1PY7-ZOiFsb7ruFhNbWvbIXmDqPsR9SXjccRwC_fIt-ghze6NNukWe_GchXH06IlELXfMulWgt3qxFiUYQX06kFMOUy01-xKgQjv-XxpUhjrdqsG63QqXpFwk6F26Y9-TnOh4OY5zo47JesU_bYiOIcr3tXklUebahc-E0IqOBh8ak9ZGH0EObdCsDtCQHzB2EYj8NOPJ9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SkHUnFfCOAdlPSkAjeSiBGHHRgKfWpcV9leTV2JRAd1BJsWo4FV9kx7YrgZ-FjAlkit7wmCmNNtFlgCQne_qHwnKI9D7EhFU_Rgu43alKKt-7srr9ZwWj7v4qyaLktcFWkHeWNQCpWj17OgKsRj1N5frQjGhscwehw7_7qOCeEY7sf_JH7fnK_ME1z1vLpvHDMBvvQLPuVYE8aIAgdWUTbHxyWkH-uvtFGbm2iy4_6WklxfQWw0gMZ5ZSNPbGR-Gr-cv1b5V-Td-6h-O-6lX3xaiVGdcZye65WkLD_L_78fUsRlaJIJUQdxn564BM67qUbZRxeBCVk2_oGwNGCZMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uH7k6O1oZfe8VkI-9bKG0I-BUyuuvRAPY79IzlaPrRU4KdzBkojvik_6wdLuH0asDMta5uNuHr0SPFEyPYtT9JymBk5HEScl8WGXQTHvfMHBi-uIICEZvthXo1HQSJOneCJ_0jq1UE9oDeWPrGoTL0IjQBSgKADcQMDJ6EyVyC1BgOAo371OQ1BTarJdj2Kw0qYelbj2CKwlbtHezvsslZzuqm1NJc4BzXwq6adqZ1GncAN1egwcNWgKVDNmK9xBcaZsKW9pAc7j3R4jVSNCwMve5lIpMACcnF-8PaumySQg3kwP9cz3UIBH-dxvf7Q2pk8hqyf56ggVf9mHT7SVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hZRKiWU0WlrM0gR7_RBV1wHRaGKYhY5lfmSo-1iWhcsSJ35w8w9II3j8Ud6LYi_oytJCQWmSvE9LlD9K6WdqOke-S_WD-QykxM_JcbHeIkiW_iOp3dGgNpAwqhkMDES5o9epPJ_FwmZiGMMB60seXdB0YetXSEcZPMNZkW7iApB8TGNSWxryP1Xg_P9RyLNxuyPtpjUeMzlG513b50OAFc1kHDrDmjwZHyaJDko4fruzwRG8bmp6Rg29iCe144_Q2DciFwpUSxjtOr_aErEsAQB_gVG2wnmfxOYu5-vZPWisXHxnImR6e5s3Vm20ynTYt6H9pfZ2vYtdiyG6IiKriw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=gmfLuc62aGuVMDsOfuCUCMMl1DpESNyRFr7X2kI5IikFNumDBroSled2wx9t7qoOalbDvUVPxPlQcBqE6029es6x7TeCcEbbkrUMSaZeC-2pTPG9WcPRZpBhBnzHVoabLE9HHm4g4s0sMgEssRMbPrazFURQJjsqbkRT5m3abdMZXSMDTXUhR7-6KoEIFfDAL4ONMK5BkO4O60mmGuf3I_3VceiIo_MCFU8o8FVA1g-y1GcwL5oDDXcIO1Rk7ZmjHpx-_kki3Z67xskyo-0FI_xvoThQIEkKIP_rSLnmKiL1kWfZgjbCdBef4JmmzR0OH4CEdfH9CJhXsCe0uYw0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=gmfLuc62aGuVMDsOfuCUCMMl1DpESNyRFr7X2kI5IikFNumDBroSled2wx9t7qoOalbDvUVPxPlQcBqE6029es6x7TeCcEbbkrUMSaZeC-2pTPG9WcPRZpBhBnzHVoabLE9HHm4g4s0sMgEssRMbPrazFURQJjsqbkRT5m3abdMZXSMDTXUhR7-6KoEIFfDAL4ONMK5BkO4O60mmGuf3I_3VceiIo_MCFU8o8FVA1g-y1GcwL5oDDXcIO1Rk7ZmjHpx-_kki3Z67xskyo-0FI_xvoThQIEkKIP_rSLnmKiL1kWfZgjbCdBef4JmmzR0OH4CEdfH9CJhXsCe0uYw0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت ارتش این کشور احتمالا امشب دور تازه‌ای از حملات علیه اهدافی در ایران انجام خواهد داد.
ترامپ پیش از دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با اشاره به حملات جمهوری اسلامی به شناورها در تنگه هرمز گفت: «آن‌ها چند پهپاد و یک موشک به سمت شناورها شلیک کردند، در حالی که این شناورها حق داشتند در تنگه هرمز حضور داشته باشند. به همین دلیل دیشب بسیار سخت به آن‌ها حمله کردیم.»
او افزود: «احتمالا امشب هم بار دیگر حمله بسیار شدیدی انجام خواهیم داد. فقط کمی از قبل به آن‌ها هشدار می‌دهم.اما باید ببینیم در نهایت اوضاع چگونه پیش می‌رود.
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، با تاکید بر نقض مداوم آتش‌بس از سوی جمهوری اسلامی، گفت: «آن‌ها هرگز تحت توافق ما به سلاح هسته‌ای دست نخواهند یافت. اما نمی‌دانم اصلا توافقی در کار خواهد بود یا نه؛ شاید این مسئله را بدون توافق حل کنیم.»
ترامپ گفت جمهوری اسلامی «هر روز» آتش‌بس با آمریکا را نقض می‌کند.
او افزود: «آن‌ها دروغ می‌گویند، تقلب می‌کنند و آدم می‌کشند.»
ترامپ بار دیگر از توافق هسته‌ای دوران ریاست‌جمهوری باراک اوباما انتقاد کرد و آن را «یکی از بدترین فاجعه‌ها» خواند.
او گفت: «توافق ما دیواری در برابر دستیابی به سلاح هسته‌ای است، اما توافق او [باراک اوباما] جاده‌ای به سوی سلاح هسته‌ای بود.»
@
VahidOOnLine
رئیس‌جمهور آمریکا با انتقاد شدید از مقام‌های جمهوری اسلامی آنها را «بیمار» خواند و گفت ما به آنها گفتیم بروید و مراسم تشییع جنازه خود را انجام دهید. آنها به جای آن، دیروز شروع به شلیک موشک به کشتی‌ها کردند.»
دونالد ترامپ که در کنار مارک روته، دبیرکل پیمان آتلانتیک شمالی، ناتو، در آنکارا با خبرنگاران صحبت می‌کرد با اشاره به حملات هوایی شب گذشته اضافه کرد: «ما هم دیشب ضربه سختی به آنها ضربه زدیم، خیلی سخت.»
@
VahidHeadline
ترامپ گفت: «آن‌ها درخواست یک وقفه کردند. می‌خواستند برای مراسم تشییع جنازه خامنه‌ای بروند. من گفتم این فرصت را به آن‌ها بدهید. و آن‌ها دو موشک شلیک کردند. منظورم این است که این دیوانه‌وارترین کار بود.»
رییس‌جمهوری آمریکا افزود: «ما می‌توانستیم آن‌ها را بکشیم؛ بنابراین فکر می‌کنم باید از این زاویه هم به موضوع نگاه کرد.»
او همچنین گفت جمهوری اسلامی درخواست کرده بود که آمریکا آن‌ها را نکشد و افزود: «ما گفتیم قرار نیست شما را بکشیم. هیچ کاری نکردیم. در واقع، ما امنیت آن‌ها را هم تامین کردیم.»
@
VahidOOnLine
ترامپ در جریان نشست خبری در آنکارا، جمهوری اسلامی ایران را به اشتباه جمهوری اسلامی «ژاپن» خواند. او بار دیگر اشاره کرد که در جریان جنگ، جمهوری اسلامی ۱۱۱ موشک به سمت ناوهای هواپیمابر آمریکایی مستقر در منطقه شلیک کرده است. فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از این اعلام کرده بود که این موشک‌ها رهیابی شده یا به هدف نرسیده‌اند.
@
VahidOOnLine
ترامپ گفت که حملات اخیر ایالات متحده به ایران «تاثیر فوق‌العاده‌ای» داشته است. او گفت که در این حملات، سامانه‌های راداری که تهران در حال بازسازی آن‌ها بود، منهدم شده است.
ترامپ هشدار داد که آمریکا می‌تواند تنش‌ها را بیش از پیش افزایش دهد. او گفت: «تاسیسات تولید برق، نیروگاه‌های برق... اگر مجبور شویم، آن‌ها را از کار می‌اندازیم» و افزود: «تاسیسات آب‌شیرین‌کن... اگر لازم باشد آن‌ها را هم هدف قرار می‌دهیم. دلم نمی‌خواهد این کار را انجام دهم.»
او همچنین اظهار داشت که ایالات متحده می‌تواند جزیره خارگ، جزیره‌ای با اهمیت استراتژیک در سواحل ایران را «تصرف» کند و گفت که در آن صورت، ایران «هیچ کاری» نمی‌تواند در برابر آن انجام دهد.
@
VahidOOnLine
ترامپ گفت جمهوری اسلامی «هر روز توافق را نقض می‌کند» و به همین دلیل آمریکا «چاره‌ای جز ادامه حملات» علیه ایران ندارد.
ترامپ با اشاره به توافق آتش‌بس، گفت: «آن‌ها هر روز توافق را نقض می‌کنند. دروغ می‌گویند. تقلب می‌کنند. مردم را می‌کشند.»
رئیس‌جمهوری آمریکا همچنین با انتقاد از دولت‌های پیشین ایالات متحده افزود: «در ۴۷ سال گذشته هیچ رئیس‌جمهوری کاری در برابر آن‌ها انجام نداد.»
@
VahidOOnLine
ترامپ بار دیگر تاکید کرد که ذخیره اورانیوم با غنای بالای ایران، تنها به‌وسیله تجهیزات آمریکایی قابل استخراج است. ترامپ با اشاره به حملات تابستان سال گذشته، یادآوری کرد که این مواد زیر آوار تاسیسات و زیر کوه باقی مانده است.
رئیس‌جمهوری آمریکا، با تاکید بر این‌که نیازی به اعزام نیروی زمینی به ایران نمی‌بیند، گفت: «وقتی که آن‌ها کاملا از بین رفته باشند یا توافقی حاصل شده باشد، برای خارج کردن مواد هسته‌ای می‌رویم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76833" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-USQ9zqrM_4HpDfcKrPyknm6cBYxSTBNDn_uRvUQw8qMXZV3Y7yZCVDCHeXl9oXT_zblLMDl-wsT8dxSv9_nhsCxMgPLMT60X7CN825C78xSNAF7FWeQcfYBZughwDyd5i4_CpY6Ceh4oalWYwSTu1jqNk5Ks61lQ5uIW4JdI62f1UBMYeOrcCCVnRTflYkquJEgCY52d1c1JQ4yiVb-MgOIXP8QusJ1iFxNdJe4XSAJmT3eO4KQsKpAkUyQKbGk8FE-s-to97qQUeLKjEvhx_mgsCyZyFehjNdmXDGCVybhF_g6pQdAj4FK23u1t_z9okPZZkMZZpMiYm-jjeVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل هم‌زمان با گذشت شش ماه از سرکوب خونین اعتراضات سراسری دی‌ماه ۱۴۰۴ در ایران اعلام کرد با توجه به این‌که در ایران «هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد»، دادخواهی قربانیان این سرکوب باید از مسیرهای عدالت کیفری بین‌المللی «به‌عنوان اولویتی فوری و غیرقابل مذاکره» دنبال شود.
دیانا الطحاوی، معاون مدیر منطقه‌ای خاورمیانه و شمال آفریقای عفو بین‌الملل، در بیانیه‌ای که این سازمان روز چهارشنبه ۱۷ تیرمنتشر کرد، گفت: «با گذشت شش ماه از زمانی که نیروهای امنیتی ایران طی دو روز، هزاران زن، مرد و کودک را به‌طور غیرقانونی در سراسر کشور کشتند، ناتوانی جامعه جهانی در برداشتن گام‌های مؤثر برای پیگیری عدالت بین‌المللی غیرقابل توجیه است.»
الطحاوی افزود: «این بی‌عملی به تداوم چرخهٔ سرکوب مرگبار کمک می‌کند؛ چرخه‌ای که در آن بازماندگان و خانواده‌های قربانیان از عدالت محروم می‌شوند و زمینه برای وقوع جنایت‌های بیشتر فراهم می‌شود.»
این مقام عفو بین‌الملل همچنین بار دیگر هشدار داد که تلاش‌های دیپلماتیک برای دستیابی به توافقی میان آمریکا و ایران نباید باعث نادیده گرفتن نقض گستردهٔ حقوق بشر در ایران شود.
به‌گفتۀ الطحاوی، مقام‌های جمهوری اسلامی تاکنون هیچ هزینه‌ای بابت استفادهٔ گسترده و غیرقانونی از نیروی مرگبار علیه معترضان نپرداخته‌اند و همین مصونیت از مجازات، آن‌ها را در تهدید به سرکوب‌های خونین بیشتر جسورتر کرده است.
به‌گفتهٔ سازمان عفو بین‌الملل، «با توجه به این‌که در ایران، به‌دلیل بحران ساختاری مصونیت از مجازات، هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد، باید مسیرهای عدالت کیفری بین‌المللی به‌عنوان اولویتی فوری و غیرقابل مذاکره دنبال شود».
سازمان عفو بین‌الملل در بیانیه‌اش بار دیگر از جامعه جهانی و کشورهای عضو سازمان ملل خواسته است بحران حقوق بشر و مصونیت از مجازات در ایران را در صدر دستور کار خود قرار دهند، از ایجاد یک سازوکار مستقل بین‌المللی برای تحقق عدالت در مورد ایران حمایت کنند و از شورای امنیت سازمان ملل بخواهند وضعیت ایران را به دیوان کیفری بین‌المللی ارجاع دهد.
ماه گذشته، رئیس سازمان عفو بین‌الملل نیز نسبت به تداوم سرکوب داخلی در ایران ابراز نگرانی کرده و هشدار داده بود توافقی که صرفاً به‌طور موقت جنگ را متوقف کند اما حقوق بشر را نادیده بگیرد، خطر آن را دارد که به پوششی برای تداوم مصونیت از مجازات، اشغالگری و سرکوب تبدیل شود.
عفو بین‌الملل می‌گوید توافق ایران و آمریکا، موسوم به «تفاهم‌نامهٔ اسلام‌آباد»، تنها در صورتی می‌تواند به صلحی پایدار منجر شود که حفاظت از حقوق بشر، پاسخگویی عاملان نقض حقوق بین‌الملل، جبران خسارت قربانیان و تضمین عدم تکرار این نقض‌ها نیز در کانون توجه قرار گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76832" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tAqe5a2aQ4Cm_d4aX1CIjxNygcbPwb1_o1yVns3llkOpH7rcBXSRcN0aD89fneX3hjwEtaWGCFlRPWBWyuM_D691Ah0pup61pXLlgbbccvL25EZZ-GbLn_vzxCqQq6zt3C3OzRZMBgE59XKmkdFxkfxb4sTEVl6HGx9flpSlbYgCQ2FnjJtKOnvJnmbETgtM6643kMVMDi1Ti2jZnKngYxUCBni9M8N122m6YyHanUtAGQXtmSrNH2GARzXmXw7eEo_S4GtrWUoGRf5sN9s4cL_y1vxBRR2a7N5GEmcKRBp_g4bKJE_V9BlV6Rfgk9H85pZsXh3JLCk0H_dFhcAUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U3_3zTj5WTIH72hGrH9WGiEnauzPVVH0HPYADXA2zQP6Hmx8x0tc2qqVp9FMdAUc8Rjka-xwQGD097ObLYj7VV1LwY2Wkiup8SpaLGZCBeKwiJQpzwyGvSY7W1mwwYxVOTLZdtduND5qNxMvcyhwr_t2gMvJYxGZooNEBQOHCkjRPCVemHcmFzt2qi7-_FlLOeVazuycBfG9vH-2DZaMRJvFn1VwEeW-zm5mbc5QQ-DMP-LG3qm-1E2FOiRd0HIn7QC6IWbVUWrhckaeDrVYhYXKQ9mr8WzAR-jZW9jjetf7h_Yxt6LPkTkGlIGK7p3bBwqNm-d4R3p6xxOOABCSnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با اشاره به مراسم دفن علی خامنه‌ای، گفت جمهوری اسلامی به جای حرکت به سمت کاهش تنش، حملات موشکی به شناورها را آغاز کرد و آمریکا نیز در پاسخ، حمله‌ای گسترده علیه جمهوری اسلامی انجام داد.
ترامپ که در دیدار با مارک روته، دبیرکل ناتو، در آنکارا سخن می‌گفت، اظهار داشت: «ما گفتیم بروید مراسم تشییع خود را برگزار کنید، اما آن‌ها به جای آن، دیروز شروع به شلیک موشک به سمت شناورها کردند. به همین دلیل، دیشب بسیار سخت به آن‌ها حمله کردیم.»
رییس‌جمهوری آمریکا همچنین جمهوری اسلامی را «بیمار» توصیف کرد و گفت: «آن‌ها بیمارند. یک مشکلی دارند.»
ترامپ افزود حملات آمریکا «۲۰ برابر شدیدتر» از حملات تلافی‌جویانه ایران بوده است و گفت: «باید سرطان را از بین برد.»
@
VahidOOnLine
مارک روته، دبیرکل ناتو، در نشست خبری مشترک با دونالد ترامپ، رییس‌جمهوری آمریکا، در آنکارا، از حملات شبانه آمریکا به جمهوری اسلامی حمایت کرد و گفت این حملات «کاملا ضروری» بوده است.
روته با اشاره به حملات آمریکا افزود: «این یک پاسخ بسیار قوی بود و من در این موضوع با شما هم‌نظر هستم.»
دبیرکل ناتو همچنین از مواضع کشورهای اروپایی از عملیات نظامی آمریکا علیه جمهوری اسلامی دفاع کرد. او این اظهارات را در واکنش به انتقادهای ترامپ از برخی اعضای ناتو، از جمله بریتانیا و اسپانیا، به دلیل محدود کردن همکاری نظامی با آمریکا مطرح کرد.
روته گفت: «می‌دانم که شما درباره ایران ناامید شده‌اید، اما به نظر من این‌ها مواردی استثنایی هستند.» او افزود: «پنج هزار هواپیما از فرودگاه‌های اروپا در حمایت از عملیات «اپیک فیوری» به پرواز درآمدند و اروپا به سکویی بزرگ برای نمایش و اعمال قدرت آمریکا تبدیل شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76830" target="_blank">📅 12:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=gTp9cQT-aqFfJ20EeN0oovQSTDhlp-f-osXAUUPjHmGiIDN0NAN5bzXpjj6lgPBH115JHQalwNvdiEXqVc5Fp8YJ-2tLnqXT1wmGb8DtuhmHS71yIjKC0OrTB-lbqeppWj0mQIVxbdbhYhhCdihohEUP7uUeXeon3v-Td0taUMbO2ViA-7erJyF7Qli_gYP8SmXIvsJgN9cLnqZdymZoeUGW-29liW3EKR_0VSl8rmzjAaumw6QRw5tptO1WHh9H5X12FTR4AePfPwK7dpDCKfti2JGRCUnWBDIGy9GBepJPPByLPYgQtnlkbYhk2Lw-NMOVBnecw73q2sSfXb8dzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=gTp9cQT-aqFfJ20EeN0oovQSTDhlp-f-osXAUUPjHmGiIDN0NAN5bzXpjj6lgPBH115JHQalwNvdiEXqVc5Fp8YJ-2tLnqXT1wmGb8DtuhmHS71yIjKC0OrTB-lbqeppWj0mQIVxbdbhYhhCdihohEUP7uUeXeon3v-Td0taUMbO2ViA-7erJyF7Qli_gYP8SmXIvsJgN9cLnqZdymZoeUGW-29liW3EKR_0VSl8rmzjAaumw6QRw5tptO1WHh9H5X12FTR4AePfPwK7dpDCKfti2JGRCUnWBDIGy9GBepJPPByLPYgQtnlkbYhk2Lw-NMOVBnecw73q2sSfXb8dzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات ج.ا: یک مشت آشغال هستند!
نقل زیرنویس، ترجمه ماشین:
سؤالی دارید؟
ـ آقای رئیس‌جمهور، آیا آتش‌بس تمام شده؟ آیا آتش‌بس پایان یافته؟ آیا تفاهم‌نامه مرده است؟
سؤال بسیار جالبی است.
از نظر من، فکر می‌کنم [تفاهم‌نامه و آتش‌بس] تمام شده. دیگر نمی‌خواهم با آنها سر و کار داشته باشم. آنها تفاله‌اند. می‌دانید تفاله یعنی چه؟ آنها تفاله‌اند. آنها آدم‌های مریضی هستند. رهبرانشان آدم‌های مریضی هستند و آدم‌هایی شرور و خشن‌اند.
دروغگو هستند؛ ما توافق می‌کنیم. و اگر من با او توافق کنم، یعنی توافق داریم. و او بیرون می‌رود، حرف می‌زند. ما توافق می‌کنیم. همه موافقت کرده‌اند: هیچ سلاح هسته‌ای. ما توافق می‌کنیم. آنها بیرون می‌روند و با رسانه‌ها حرف می‌زنند. می‌گویند ما حتی هرگز درباره‌اش حرف نزدیم. یک جای کارشان ایراد دارد. آنها دیوانه‌اند.
آنها دروغگو و متقلب‌اند؛ مریض‌اند. آنها به مردم خودشان آسیب زده‌اند. تا همین حالا ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید وقتی مردم می‌گویند چرا آنها حکومت را سرنگون نکرده‌اند، نمی‌توانند سرنگون کنند، چون مرده‌اند؛ آنها را کشته‌اند. کسی سرنگونشان نمی‌کند.
آنها اسلحه ندارند و طرف مقابل مسلسل دارد و آنها را می‌کشد. رسانه‌ها این را گزارش نکرده‌اند.
اما آنها آدم‌های بدی هستند؛ آدم‌های بدی هستند. و صادقانه بگویم، نمی‌خواهم وقتم را با آنها تلف کنم.
حالا می‌گذارم مذاکره‌کنندگان فوق‌العاده‌مان اگر بخواهند به گفت‌وگو ادامه دهند، اما من چنین چیزی نمی‌بینم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/76829" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fR8qJYi4e-JTo-0A-CqgmGW-tTnGSSBHgwsmUqUDPO1Q2JcoBCl_QxRw1_dIAdFBH3Q52fC1-qEiy9ZEJXA245uNGAhqGDoyZUJ29dO5LxQQ6jI8hoJXJr3fWxTFfY-optz2hU8wr1PkncmUMNwAwNDa_sKySkZpk3RvT-5k7seMPEASvt6Oq4RPhHhKi9ShaIAwlCpv42jTAbZxkNENZWkX5ViAun5cYO2i2g9xeXH9Hdw6ArDWdfarzI4IXNmhQKusvKxRRvuQZvtgLCkjK_7A7kl5RZaxbI_3jwShl7acumI6BCZnc45_4p1VVhiDChcspafHYneF8SxzZME7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست پزشکیان، ترجمه ماشین:
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی همان سیاست خارجی آشنای آن را دنبال می‌کند: دستکاری قواعد، زورگویی به رقبا، مانع‌تراشی و تقلب. این همان دستور کار MAGA آنهاست. ایران چنین بازی‌هایی را رد می‌کند. ما قاطعانه پای حقوق خود ایستاده‌ایم.
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76828" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76827">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
الان زد بوشهر رو ۱۰:۴۱
سلام وحید جان ساعت ۱۰۴۰ صدای انفجار شدید در بوشهر
سلام وحید همین الان ساعت ۱۰:۴۰ دقیقه صدای دوتا انفجار شدیدی توی بوشهر شنیدیم
سلام وحید الان بوشهر رو زدن فکر کنم پایگاه هوایی بود دوبار صدا اومد
بوشهر پنج تا شش تا صدای انفجار سمت پایگاه هوایی و دریایی ارتش
بوشهرو الان دوباره زدن
بوشهر یه بار حدود ۱۰:۳۰ دوبار زدن یه بار هم حدود ۱۰:۴۰، بار دوم نزدیک‌تر بود
ما پایگاه هوایی بوشهر هستیم
حدود ساعت ۱۰.۴۰   دو تا صدای انفجار اومد
دو سه دقیقه پیش هم دوبار
به نسبت انفجارهای روزهای جنگ معمولی تر بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76827" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NN2TOovgKJgVUDpyERebE-nZsFK3-xh2yLzkMFkQvwydFL_kQrNokVVwxaCdyW0e_eXsplRTK3IXkjXWWBvjYuqrqDbE0qZcf61hIevtp7NZYZ3-oH-9WseeCEd9xpRf1Z0xwN-r-tdAYPMpIlKgMWFvQr2zKki2LQHsBxI6sIhfm74srIWWVZXynpm_7oOgw3xUwvrwp5ZNvPQMjfUOkXbTeycr0OZIywE4PzbW3PFDH3Fs0ZiP1U_76NY8oFnm3lLxi3qYNgTfSVVnqIvCCXTHR2UdN5Az4NwFgggfIfKWiyEImqgDSomuik2Q0HFVYH1iGwuIIkELZfzv4HhDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: پاسخ دادیم
منابع حکومتی:
پاسخ اولیه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
🔹
به دنبال حماسه سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر آشکار می شود و بازتاب جهانی خیزش عظیم و میلیونی ملت سرافراز عراق در بدرقه تاریخ ساز رهبر مجاهد شهید را شکست بزرگتری برای خود میداند، بار دیگر عادت پیمان شکنی خود را تکرار کرد و وحشت‌زده برای تحت شعاع قرار دادن این رویداد تاریخی، ارتش کودک کش و تروریست آمریکا در ساعات اولیه بامداد امروز با تهاجم هوایی به تعدادی از پایگاه‌های ساحلی و ایستگاه‌های غیر نظامی در سواحل استان هرمزگان و ماهشهر به طور آشکار آتش بس را نقض کرد و تفاهم اسلام آباد را زیر پا گذاشت.
🔹
در پاسخ اولیه به این تجاوز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی طی عملیات مشترک موشکی و پهپادی، ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در بندر سلمان، منطقه پنجم دریایی بحرین و پایگاه هوایی علی السالم کویت را در هم کوبیدند و یک پهپاد MQ9 دشمن که قصد دخالت در عملیات را داشت، سرنگون کردند.
و ما النصر الا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76826" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0y4tR-DEOB_td-DXBFVOKb0JylbGfo9xw5R3z12Y5QtIEUgw8I-QEQitruGWDSqNlprDfhKuqodDne1AlYxZ6U09g9Ncol7K4KXSmH-MxmhZ_mYN9lwr-G0K49QPDKnnvh00m--bIw3W0zz1GI8WsEGCTPoEqsva8uXXiHH5bpfQtoV86KmnRIPZf2YrYMglIuOy39hGy9KIT_XfJ7h2ibfTFIVD2UnVxTbNRkqNkUsPturi_lOVAekk_cFtpK520rW3jRjGK26cwu5MJbVN4j0K79ZoQpffVJKgIiP2aff2s6esTeWIMmQ3Yo5JHTIQg1c71rhTVF6kHG20rIInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شوری اسلامی پس از حمله‌های بامداد چهارشنبه آمریکا به اهدافی در جنوب ایران در واکنش به حمله‌های دو روز گذشته سپاه به سه کشتی در نزدیکی تنگه هرمز در پیامی به زبان انگلیسی در اکس نوشت: کلیدی‌ترین موارد نقض تفاهم‌نامه ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگه هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار حمله‌های اسرائیل به لبنان
او در ادامه این پیام نوشت: «دوره قلدری و باج‌گیری تمام شده است، راه به جایی نمی‌برید، ما اهل کوتاه آمدن و عقب کشیدن نیستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76825" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIKpnCk308VoBhyGZ9iWdZFxlTGylzFzxMVTlOtjt9g_Is2Yy9BXpbOLNRk4-XJHboC_Az5pYe5YfOojsEkegtsdKRJenm2BWChYYuYc2MHb7cSwqBLxqOJeSH9p-CSE55gHoWxdDZJ2tgkW80LTgP58qX_5fZFsV9AP82ZHTBmtZMRXpAKQYkRXMERbKN-iFw0uttNkqhrKkbiLKycJqoJMcOTBus-ttacfDOP9SGCg6mjmQxI82ssULMx5TrfpBXtj30IM25HFFUknXxm2v4OXa2TyeAeQDFyOSRAQFJFDFZqW6mqmYWAJnY7l87HNxZqL0HoCOnAE4nfL5Akzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت ۶:۲۷ چهار تا موشک داراب شلیک شد وحید
موشک پرانی همین الان داراب فارس
+ کلی چندی پیام مشابه دیگر از داراب و هم‌زمان پیام دریافتی درباره آژیر در بحرین:
Sirens again in Bahrain for the 2nd time just now
آپدیت:
ارتش کویت: پدافند هوایی در حال مقابله با حملات موشکی و پهپادی است
ستاد کل نیروهای مسلح کویت بامداد چهارشنبه اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
در بیانیه ستاد کل ارتش کویت آمده است: «اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات دشمن توسط سامانه‌های پدافند هوایی است.»
ارتش کویت از شهروندان و ساکنان این کشور خواسته است دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76824" target="_blank">📅 06:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=D8S_UCxctT-mZqdz_P06eoURmphk8rFxsjXR5-DT23k12jM7OJn4WjCk6tMbxM-YbFXC2ultd8UDuRqyNHdW3d65Xk1C9EGzqVq_HfEMcuQ3OvaVjGHbhBg1kKIxmxZdoKEC1v2gLKLS1adY7w7NjPrldpUJ5c8YwgLJrHKhDVepQuAKRTGhLyoa1-y-TxIxs6oBWqq5yMQsRvLB_M_sYhZOL94gJ6QMViORD6Y4OkFc_HaV8Z_P3t-HCQUfQZu4AeuI2xzkDj_EQ_-WE_6VMqAtP7QB0d6rJZXUGYio14yKXMgO2vjsrSmhE8eZKBaJqGuCZlioWyRuupPvi09l0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=D8S_UCxctT-mZqdz_P06eoURmphk8rFxsjXR5-DT23k12jM7OJn4WjCk6tMbxM-YbFXC2ultd8UDuRqyNHdW3d65Xk1C9EGzqVq_HfEMcuQ3OvaVjGHbhBg1kKIxmxZdoKEC1v2gLKLS1adY7w7NjPrldpUJ5c8YwgLJrHKhDVepQuAKRTGhLyoa1-y-TxIxs6oBWqq5yMQsRvLB_M_sYhZOL94gJ6QMViORD6Y4OkFc_HaV8Z_P3t-HCQUfQZu4AeuI2xzkDj_EQ_-WE_6VMqAtP7QB0d6rJZXUGYio14yKXMgO2vjsrSmhE8eZKBaJqGuCZlioWyRuupPvi09l0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: بیش از ۸۰ هدف نظامی را با مهمات هدایت‌شونده هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده آمریکا (CENTCOM) روز ۷ ژوئیه دور تازه‌ای از حملات تهاجمی علیه ایران را تکمیل کردند و در واکنشی فوری به تازه‌ترین حملات ایران به کشتی‌های تجاری در حال عبور از تنگه هرمز، بیش از ۸۰ هدف را با مهمات هدایت‌شونده دقیق هدف قرار دادند.
نیروهای آمریکا سامانه‌های پدافند هوایی ایران، شبکه‌های فرماندهی و کنترل، سایت‌های رادار ساحلی، توانمندی‌های موشکی ضدکشتی، و بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را در تنگه و اطراف آن هدف قرار دادند تا توانایی ایران برای ادامه حمله به تجارت بین‌المللی در این گذرگاه تجاری بین‌المللی را تضعیف کنند.
ایران اخیراً به سه کشتی تجاری در حال عبور از تنگه حمله کرده است؛ از جمله M/T Al Rekayyat با پرچم جزایر مارشال، M/T Wedyan با پرچم عربستان سعودی، و M/T Cyprus Prosperity با پرچم لیبریا. این تجاوز بی‌دلیل از سوی نیروهای ایرانی نقضی آشکار و خطرناک از آتش‌بس است و آزادی کشتیرانی را تضعیف می‌کند.
نیروهای سنتکام در موضع آمادگی باقی مانده‌اند و آماده‌اند هر زمان که توافق رعایت یا اجرا نشود، ایران را پاسخگو کنند.
CENTCOM
قرارگاه خاتم‌الانبیا: پاسخ کوبنده می‌دیم
خبرگزاری رسمی جمهوری اسلامی، ایرنا:
قرارگاه خاتم‌الانبیا: نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند
🔹
تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را نخواهیم داد.
🔹
بی‌سابقه‌ترین رویداد و حضور مردمی در تشییع و بدرقه قائد شهید امت اسلامی، شکست خفت باری را بر استکبار جهانی و آمریکای جنایتکار وارد نمود.
🔹
ارتش تروریست آمریکا بدون هیچ گونه پایبندی بر تعهدات خود و در شرایطی که پیکر مطهر رهبر شهید مسلمانان و آزادگان جهان میهمان مسئولان و مردم سلحشور عراق می باشد در تجاوزی آشکار برخی از نقاط جنوب کشور عزیزمان ایران را مورد هدف قرار داد.
🔹
نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند و تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را به آنها نخواهند داد.
🔹
مجددا اعلام می‌گردد تنها معبر ایمن برای عبور و مرور کشتی‌های تجاری و نفتکش در تنگه هرمز، مسیری است که جمهوری اسلامی ایران آن را تعیین کرده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76823" target="_blank">📅 05:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bx2imkbRc2IqFkF3K_RUoVUB3SteWom16ike7h1Jt8nBv-W-8zKugFY73SuN8gyL-I6SBGH607aDZtJng9NfcIh59XjYoHoZCcsaWkhrIg6BvEDYAOr1xsuupL-KB9pQaEfN8yXP0kCBKqGOKz_Wsm4yjkVE6-aWFQFOpkN3cGfLh8bFiolyht_GvhgqJG0kqa9eBUlDxuiC5PgBdryxpDuWEEspk9kNi2nWWbU-bdp0SdzNmADSzn3MOJwugZkq5hAldgHCdDMcLj2ZQ3d42V8QOGjlomL-o3ocQesf6X-mav3tamPW2wuwgsTc0jIV_fd2T3_iqScjG8N-Pl-xQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ea6wutDnjFlLaebFv1FIdc9CcUcp7UCQD3qxsNoez-PN2igNx_63QX5X9A-w9Vjz5ptVkgEmWEIFRHuetUega0U5Yrxvakf00ju8iGtvRkXQUOJnvw1Ka6LU0dsnAZ3tWKWOG5QCzx-oUqJ9p2qLcy2eLCp-Nr12GY1IAOi-PkwNvcn1jHoISTWEA9h6j8PM0-8cwPKIjOI7Bjgei642VDhAICUeRBjCqqTR-rYHKoGpG1YeAFh4Nx7M62Ph0o_bzWdqiLS9pnBYeRMghw4H8XffMXv-pObPXJAwRrNGbdYkDd5BJIanY7aWEczNFauItMg1SdRXw8Eo39_Py1XG1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SF_3PAqEafgBT0oNwiqsZuQIoxRr0cSoX10oCJKAdwkjZ1bhpI-67vSf0TjnAzyByq_4HLOPnZ8teZIt5HSE9hyhOCTd9eLV_p0JPH0-cK-Z0oOUxmItkvF0SsoTJAxnD8Vn9HeEFTY9tsSQTa4i809EUT_O6VhLdIlCWm-DD1GgSKi0aNTPSdYBC5SBRHiHKSN6Q58D80Ik4_bV_YFKTHR4mFmm8PiXDf-KKgFYxNoAxGTL5F-aaMaeh3ARSQ7Xva8rfCbPBm7-5ikSxUf63euaOZi8sWPwvxCKvtOQcMP7xci5Opszux3rW17_lFWvrWCgYA3f9C0Ky1mQ0Yn11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BB4vyzhvhuf-cluP-laBIsn5N_p48tBAS381Vf6Cm1WunDXq7l8ygxR-QUECL4OaPmunQmnaEjM17RxSQg9kp6RtOivElMxG81qGoMyu0egiN8Vwob5oXR9sWTWms8JG4oZpKMicouyXnGKG0PJyXjPcakiSTIQKbXvjHqwj0jrfJYQAdbPuvvib4mavG89zkbT5Jt3-bBzGPH_7iiS6kNhScHCMIb0ezJ1sKZtQYRIWuzTRw3T9oafRbitDvaTDpLIxy66cV7Wxzq432wEs8wiTDHUVy1G2E3NVvYwbpexhZPCey2MD96EAfKxG1CvGnHN6xQR1X3lcnFIhZBLZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pZleeO0qIK5tu5K9jlOJwrnyps9gN5ux-9FQ6idEbgkfUJGfy2d4ltDQaLp9V1Yz-Hrji8IG9AiJ8T-NL4B3ZzdVgl515ARr7xIGE12-9Q9sRQKGhBmYSPR0Ms_RNcnXd8SbPebLJt6b9TqEVAZxRUoYc2ooiW9ZSUNBg6Ol_LaB_p7BAjShtuxHNOyPJvcfO4CB2qDTNsivXpfAYLrP7a-zA1VuwqLuHxV7syrIz0ZsLSpFuxCygfx1BrtWY8ceBy9IbJXkMBFvHRPsdqY1npdjnHmzUqP8u2YRX383zaxuoLWLHK9A6hfDY_ZM9DAKZ2OGu-JYXfNGFEbZq30kog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/964f541742.mp4?token=XUJFUj8plxZ_9xJStqWiR2CzCsG6G3cNQZ75IU_yx88vZCylDTgO-rvvLfKocoedVYzylsaqWz3QbmmeV2H-T5NmMuUh6lXqYMNXqtp9o8e0_VjTkwChwT_aG1sqY53SVC1Ml79MDlvSh3VFDG28uM83ekYw5fZrf_85r_4pgpwhQA7iWn7QQLgQKJduK2hUf50H0W42wYhAevR0KQ7suyyWv61RsYZB-bDef7hKgJhRVJktaTLrKe0MUtjeeNBCCY0Wd6I1TltPpBDVXLIgX-9BlO8buXezjFZwq-q_KbY7RGne4-P40KlB3c2dhjX8kSJcwWhuua92ujP6l04PnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/964f541742.mp4?token=XUJFUj8plxZ_9xJStqWiR2CzCsG6G3cNQZ75IU_yx88vZCylDTgO-rvvLfKocoedVYzylsaqWz3QbmmeV2H-T5NmMuUh6lXqYMNXqtp9o8e0_VjTkwChwT_aG1sqY53SVC1Ml79MDlvSh3VFDG28uM83ekYw5fZrf_85r_4pgpwhQA7iWn7QQLgQKJduK2hUf50H0W42wYhAevR0KQ7suyyWv61RsYZB-bDef7hKgJhRVJktaTLrKe0MUtjeeNBCCY0Wd6I1TltPpBDVXLIgX-9BlO8buXezjFZwq-q_KbY7RGne4-P40KlB3c2dhjX8kSJcwWhuua92ujP6l04PnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکان نیوز تصویری از یک انفجار بزرگ در بندرعباس و ویدیویی از انفجار در سیریک، در پی حمله هوایی آمریکا را منتشر کرد.
@
VahidOOnLine
+ تصاویر دیگری که با شرح امشب پخش شده‌اند و من از درستی همه‌شون مطمئن نیستم.
اسکان نیوز گزارش داد که ستون دود از سمت پایگاه هوایی بندرعباس مشاهده شده است.
منابع حکومتی:
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان: دود سیاه در پشت بازار ماهی‌فروشان بندرعباس ناشی از اصابت پرتابه‌های دشمن به اسکله صیادی بندرعباس و آتش گرفتن تعدادی از قایق‌های صیادی مردمی است.
🔄
آپدیت:
پرس تی‌وی، شبکه خبری انگلیسی جمهوری اسلامی، از شنیده شدن انفجارهای دوباره در جزیره قشم و نیز چندین انفجار در جزیره خارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76813" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JjWGXL0yorzV0WvCxy_0x4gfI3oZDRYeYj_thkm3XDe1BSk0S1QIeb8X64oyAflwYVFNP-jmQp55NQjf2DaaflBPGU5vUZxWm2yokKp9-fVKtO-YW7qGRqVv83q_KXmOy4_PsiUo3CyqBf_sWH0u0-usCvHMANTsK2bOR2a6hwoj9BlxOjGPcFfU8bF3g-jy6cAJ9GKZJ8Q7zhjbdMvmcW8Q55GKyPASEFYkR2Hqgd0pekN0yOlJA2O25goVXvzg1Rqk3mDxqZZE6NKR1F9rQpaCVjdw5N9Dx8ssCe7zTlCI9zQfT19u63T2QqZzXyyLZHt1c9D4jXz-WK6ZAIbK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت اهداف حملات شامل سامانه‌های پدافند هوایی، سامانه‌های پایش ساحلی، موشک‌های زمین‌به‌هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تأسیسات بندری ایران بوده است.
به گفته این مقام، حملات امشب از نظر گستره و قدرت، چهار تا پنج برابر بزرگ‌تر از حملات مشابه آمریکا در هرمز، ۱۰ روز پیش، بوده است.
رسانه‌های دولتی ایران نیز گزارش دادند که صدای چند انفجار در شهرهای بندری بندرعباس و سیریک و همچنین در جزیره قشم شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76812" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DVBLWncU9Nb0bzwwX1WcC0ZIV9meSNW22Lmg2xl8g1YlOIgWMPoxtMH7m8KVCdQXGTweoij9wTkB83JjA7uuUnQLHbEP8MNZNsOJ5edeasB8kTWZqFoHk1As9UjyGT99Hy4wUm1uEhWdAjWWB19t3eSvvHYMMvPKFDVzgY73IK-k9Noy1bw_knW2Z-Va8EKGryQplsX55v48kBsPdN908CLEbmGppguTnacGo7jEdQOfQG3QN-fAcI0D8lIMtqzkavW-cHoTizghtdVmli-Yb-SWZCZxYs6OrsMX8zOWQqXEDrrI-fGwl-26l_gSKowMLez6WmRpsrFqOyvQFxi3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی، در بیانیه‌ای، این که آمریکا اجازه نمی‌ده نفت بفروشند رو نقض تفاهم‌نامه خونده.
پیش‌تر امریکا هم
گفته بود
چون به کشتی‌ها حمله کردند، شایسته مجوز موقتی که صادر کرده بودیم نیستند تا رفتار مناسبی مطابق تفاهم‌نامه نشون بدن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76811" target="_blank">📅 01:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oliRbMswp9167icdTMq6KM0VzU-iC_0v7GojO_a02XXb2zoZk8xjXldw_9BoaTIv8JtApaoGRjtEtgGKdzhobEs9h_vVqFS2J-s1URjc5Iycb-L-ASi-kFvDK7MlevcSPVNzZUKpOi7-h5AzFQoby_wVEM_RDgpdmbb1ZlgvlAluIQsfcUwSI5VV_t8KFAQXm4IMPZ7EeFZLNbL8_OvFtVQiXveZPbgfEnWYMhvinQsQpXvD69ZYNK44ROdeqjNXNBtgKWvcgva69h0TQj9cIMPGES6FLHp_mVQQ5DQGYBvyOHxGSx73AVJ5GyANbHck51CUYvKkdbofBLuuo5OUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی ایالات متحده آغاز به اجرای سلسله‌ای از حملات قدرتمند علیه ایران کرده‌اند تا به‌خاطر هدف قرار دادن و حمله به کشتی‌های تجاری با خدمه‌ای از غیرنظامیان بی‌گناه در یک آبراه بین‌المللی، هزینه‌های سنگینی تحمیل کنند. حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند. تجاوز آشکار ایران بی‌دلیل، خطرناک و نقض روشن آتش‌بس بود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76810" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
سیریک، صدای چندین انفجار پیاپی.
جزیره هنگام الان صدای چندتا انفجار بزرگ اومد تعدادش ۱۰ تا بیشتر بود
صدای انفجار درگهان (جزیره قشم) میاد ولی صداش کمه انگار دوره به اینجا
سلام وحید جان بندرعباس صدای انفجار
قشم صدای چندین انفجار اومد
نفهمیدیم از کجاست
قبلش صدایی شبیه صدای هواپیما میومد
صدای دو انفجار ۱۲:۳۵ بندرعباس
سلام وحید جان
ساعت ۰۰:۳۲
ما روستای سوزا تو قشم هستیم
اول صدای جنگنده اومد
و بعدم صدای ۵-۶ تا انفجار اومد.
سلام ساعت 12:35 بندرعباس صدای انفجار اومد 4 تا.
سلام کشتی سازی بندرعباس خیلی صدا وحشتناک اومد
سلام بندرعباس ۴ تا صدای انفجار تا الان
آپدیت:
صدا و سیما:
شنیده شدن ۶ انفجار در روستایی حوالی شهرستان قشم
دقایقی پیش صدای ۷ انفجار در محدوده روستای طاهرویی شهرستان سیریک شنیده شد.
فارس:
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔄
آپدیت:
بندرعباس ۴ تا انفجار دیگه
دوباره ۴تا تا الان
شد ۸ تا ۹ تا ۱۰ تا
من مرکز شهرم خیلی بده
سلام وحید جان
ساعت 12.30 صدای 5 انفجار شدید ذوالفقار قشم شیب‌دراز  نزدیک جزیره هنگام
سمت پایگاه هوایی بندرعباس انفجار شدید همین الان
وحید جان سلام همین الان ساعت ۱۲:۴۷ بندرعباس چندین صدای انفجار پشت سر هم اومد لرزید
الان بندر عباس سه چهارتا انفجار بزرگ
درود بندرعباس ۱۲:۴۵ چندین انفجار پشت سر هم
همین الان کلی صدای انفجار اومد بندرعباس 00:48
سلام خوبی، همین الان بندرعباس صدای ۳ تا انفجار قوی اومد ساعت ۰:۴۵
بندرعباس چندین‌تا صدای انفجار پشت سر هم اومد
00/48 قشم پنج شش تا انفجار قوی
00.48 بندرعباس چند صدای انفجار پیاپی
🔄
صدای انفجار پشت سرهم بندرعباس 12:50
هنوز ادامه داره
یک سر دارن میزنن ۰۰:۵۰
مجموعا بالای ۱۵ انفجار
۰۰:۵۰ صدای ۹ انفجار دیگه هم با صدای شدید از سمت پایگاه هوایی داره میاد
بندرعباس ساعت.همین الان چند تا صدای انفجار پشت سرهم اومد۴۸دقیقه بامداد چهارشنبه۱۷تیر
سلام همین الان صدای انفجار پیاپی و نور نارنجی بندرعباس
بندرعباس رو همچنان دارن میزنن
👀
صدای انفجار و پدافند پی در پی بندرعباس همچنان ادامه داره
همین الان بندرعباس
صدای انفجارهای شدید، پنج تا شش انفجار
کشتی سازی بندرعباس، اطراف بستانو رو زدن
سلام صدای انفجار بندرعباس بیشتر سمت اسکله ساعت۱۲:۵۰چهار صدا سمت شرق اینجا صدا نمیاد سمت غرب بندر اینجا صدا میادسمت اسکله
🔄
ساعت 12:57 انفجار دوباره بندرعباس
بندرعباس ۱۲:۵۸ همین الان صدای خیلیییییی شدیدی اومد
خیلی تو شهر بود انگار
اقا وحید بندرعباس یجوری زد شهر لرزید
پیا پی اسکله باهنر داره میزنه پشت سر هم صدا میاد
ساعت 57 : 0 صدای شدید انفجار در بندرعباس
00:58 دو تا سنگین تر زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76809" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j_MwMp-KTnDhDPhCABggT_3XMvwDcN4m-WAglhuMdlLG3B2ASU-XOonlBrZxav-NgGUZhpGGIi2w-1XSNrxGpMSXdIS6-1Ol91l0jBesrf4I_rOXcahhkYWFM2NTQYApXxbDaSvn6yUIa7Yy6AIuAQCS9u4JUt3c9GK1-qtZ-Wjuu4A8vr8kKwkAuUbNuW8QbjBe4gmxnlr4q8M2ZUNzpUZsDE37vDYG2ct0imrJQ7qMy2wuQTD5LZmg7ZImuLvWVPrXBu8fVNUUsZBpH3sLOxRE8lIWZlvwoHlaka5upeXld-q6gPLC1roQEwXAikX-HwOCXOwdVzajMlRhvm5Lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا معافیتی را که به‌طور موقت تحریم‌های نفتی علیه ایران را تعلیق کرده بود، لغو کرد و اقدامات جمهوری اسلامی ایران در تنگه هرمز را «کاملاً غیرقابل قبول» خواند.
یک مقام آمریکایی به خبرگزاری فرانسه گفت: «اقدامات ایران در تنگه هرمز برای ایالات متحده کاملا غیرقابل قبول بود و با عواقبی روبه‌رو خواهد شد.»
این مقام آمریکایی گفت تفاهم‌نامه واشنگتن و تهران «کاملا مبتنی بر عملکرد طرف‌ها است» و هشدار داد که ایران تنها در صورتی از مزایا برخوردار خواهد شد که «رفتار مناسبی» نشان دهد.
مجوز معافیت از تحریم‌ها که حدود سه هفته پیش اعلام شده بود، در ابتدا به جمهوری اسلامی ایران اجازه می‌داد به مدت دو ماه نفت خام و محصولات نفتی و پتروشیمی را صادر کند، تحویل مشتریان دهد و درآمد حاصل از آن را به صورت ارزی از راه بانک مرکزی وارد ایران کند.
اقدام آمریکا پس از آن صورت گرفت که بنا بر اعلام ناظران دریایی و دولت قطر و عربستان، در فاصله چند ساعت سه نفتکش، از جمله یک کشتی حمل گاز طبیعی مایع (ال‌ان‌جی) متعلق به قطر، در تنگه هرمز هدف حمله قرار گرفتند.
@
VahidHeadline
وزارت خزانه‌داری آمریکا مجوزی را که ۳۱ خرداد برای تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران صادر کرده بود، لغو و از روز سه‌شنبه مجوز عمومی جدیدی را جایگزین آن کرد.
وزارت خزانه‌داری آمریکا اعلام کرد مجوز عمومی X به طور کامل لغو شده و مجوز عمومی X1 جایگزین آن شده است.
بر اساس مجوز جدید، شرکت‌ها تا ۲۶ تیرماه فرصت دارند معاملات مجاز بر اساس معافیت ۳۱ خرداد را خاتمه دهند، اما
از ۱۶ تیر خرید جدید یا بارگیری نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران ممنوع است.
اوفک همچنین اعلام کرد هرگونه پرداخت به اشخاص یا نهادهای تحریم‌شده باید به حسابی مسدود و دارای سود در ایالات متحده واریز شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76808" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVQz3Sd-B2cSm8h6rfVgIM7yRWQuG6VYnswkP-2yv0nbMm9FCN0Kdutf9iGoNNWKXXx3u5oE__aJPGselHSAm321DaVa8nrGq_H02kOD9g7SvGTQiUbsZYRQqT4CWbKkWO1wQ1lUfuI-19UxlcmOujYCJd813XJlNh4uS7K_HfLP0oHUeooDwkrlVo8IgOHkU-WiF5QrheHmimlVVRot_4ry-vr9ZkTdykWOA5VrA9zdZuswXavJBiI9nRNeudvR180T86bYvp5GpQdT1bfQcAka3dQ8N91mphux8j-Q9Yasp2JDXuOwca1kX0BaemZpda0K9zDhbLNwzRrfJr47ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت قطر اعلام کرده است که در پی هدف قرار گرفتن نفتکش قطری در هنگام عبور از نزدیکی تنگه هرمز، کاردار ایران را به وزارت خارجه احضار کرده است.
در بیانیه وزارت خارجه قطر آمده است که این کشور حمله به کشتی خود را به‌شدت محکوم و آن را «نقض جدی ایمنی کشتیرانی بین‌المللی، تهدیدی مستقیم علیه امنیت عرضه جهانی انرژی و تخلف آشکار و صریح از قواعد حقوق بین‌الملل» می‌داند.
اعتراض قطر به ایران در قالب یادداشت اعتراض رسمی به محسن محمد قانع، کاردار سفارت ایران در دوحه و در محل وزارت خارجه قطر به او تحویل داده شده است.
وزارت خارجه قطر اعلام کرده که در این یادداشت از ایران خواسته است درباره این هدف‌گیری توضیحات فوری ارائه کند، اقدامات لازم برای جلوگیری از تکرار چنین حوادثی را بلافاصله انجام دهد و به‌طور کامل به قواعد مرتبط حقوق بین‌الملل پایبند باشد.
قطر همچنین اعلام کرد که این کشور تمامی حقوق خود را برای اتخاذ هرگونه تدبیر مناسب، مطابق با حقوق بین‌الملل، به‌منظور حفاظت از منافع و توانمندی‌های خود محفوظ می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76807" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKISsuEwZioVnl9kYfBPiyNxhQAsa3dg5_x17meMHnkSABvCMVQ9jwtvImUzTw4NGY4aFa7obPtCFdjlDbZonjcRH9_6BlfWbUyovC_SWXM1KWNcn8D7OI3zLimxkdnTx01AzYpLMi7bB-_XsVGoBzVasO42w7ccpzejf4XuRL3aLjp4Zr25gBr2OqJAaY9_TTU7TqAT2CgWGMTf6pe3c7puKCsYJ-F_-abjy1siFei3J7m0Qig1gUspMaUDWj_OyTHo_aVvCeBywpGdNvbwpenmoq2mvseMGneaT_IU4zLLV5voN9XuLp_WJzAWHRH_RWpGY7aqoTUU2ePSfhWqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده مجلس جمهوری اسلامی، در شبکه اجتماعی «ویراستی» نوشت: حالا که دونالد ترامپ در تیررس ماست و برای اجلاس ناتو به ترکیه آمده است، رسما و بدون تعارف، محل استقرار او را در ترکیه با موشک هدف بگیریم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76806" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmVc70jSOYML6Yf5DA9dTFQPiQy_K4CvMCbMS0cxrssL40iBiJtmk43V76FIENDrhIE2pcJ6Xd43y40QPtzuOQMO_gFhsd9wV4_Xk1M_UbbA4ANBorU0-43CuCowgV4HIdgX-UyauP-WrBz7-DjkMwPdECrN99DEyY_CbInS65N9QEIlWVTyaZKmXRm1SWHCtJfy2yaKt3EVwm0rc2EO88Y_EUh6Ol6uGB1kDEwXJQKR8GM_VRAENlpUAFb9X6WpFMAz-rAoKszUg19LAbHeVOw7t0xeiq2TB1yt__8-0Dq7dCFTGGRE9TYRf29nSWcowPAVz-6VxEqzl6L4waTJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۱۶ تیرماه در گفت‌وگو با شبکه سی‌ان‌ان گفت که با وجود اختلاف‌نظرهای گاه‌به‌گاه با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره ایران، آن‌ها در مسائل کلان مربوط به نحوهٔ برخورد با تهران «هم‌نظر» هستند.
بنیامین نتانیاهو افزود که هنوز زود است درباره آنچه پس از امضای یک توافق صلح موقت میان واشینگتن و تهران رخ خواهد داد، اظهار نظر کرد.
او اظهار داشت: «رئیس‌جمهور معتقد است که می‌تواند برنامه هسته‌ای ایران را متوقف کند»، اما افزود که در این باره تردیدهایی دارد.
نخست‌وزیر اسرائیل می‌گوید: «در مسائل بزرگ هم‌نظر هستیم و گاهی هم اختلاف داریم، اما متحدان واقعی هستیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76805" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCa8D2P9hGYHYsZqjYCYHE_5AVgTZ27kBmjf7P-_g3ijMG7WRuP0Zm3q7dvAbrup7-d9YYRPnyuOCQdO7XivTGZwoknG3lLW2Xe8RqGbvBqyOfrGoVnbS-9nw9hxUJ_nAzEO0nhuauQ7X0B0pX19xS_WUR-6SOwb0weXyk6DIx9w6WSpqdth3TPKMWcXf9MgYZ10E-0fqVvwHPAUf45hBBtn_e8zpipu4onW65Niyhbfq1Yl_3f-PqzEgvCN_bHd0mPie-6JPWxFcqSpJxwReZ0-GZN3PJuPj8xq9gUO5CELC6gRChnHuNf2H0d3hMhhx6f7LoQ9me1NEar8N4EFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز سه‌شنبه ۱۶ تیرماه، به ان‌بی‌سی نیوز گفت حملات جمهوری اسلامی ایران در ۱۲ ساعت گذشته «تهاجمی» بوده و «نقض مستقیم یادداشت تفاهم» به شمار می‌رود.
به گفته این مقام، ارتش آمریکا امروز چندین پهپاد شلیک‌شده از سوی ایران را سرنگون کرده است. او همچنین با اشاره به حملات شب گذشته به دو نفتکش در محدوده تنگه هرمز، گفت که جمهوری اسلامی در این حملات از دو موشک کوتاه‌برد استفاده کرده است.
این مقام آمریکایی جزئیات بیشتری درباره محل وقوع این حملات یا میزان خسارت احتمالی بیان نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76804" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lCtACqczfIzAKf1Tb8ZVKJtfJRoCMVg5DWn-wUSyUnyUMhnY15vFYaTqpz1MrP2KY2-d2hrcXnmavqC-5upnX0Ge6VulNIDpL-S53QVtGmLYXoOVzM4nq-GIExMSGiC__a15fVPh8D41EZwK5TbGKZ-FvuHQdL0k3dGGDx_ppzbY7SH0CZirwl07834B-xwy6zluk63FgYDctS6m5uuYlt49ACLHSWVWpdaBLe7BrSAuYYdbdIjDD-pcadzcDKxtCuiEtgUB3-Vv_h3OMznM2h0mTNfPhauwoXUWt8BR02loSCJ4FAdjPN5s6M9dZ0HtCVwI6XgdG50G4CTWoi4zXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=AvHovjteevDy6dCyG-_XVoBonvutThZ7Ms3xK5vlqeeEMhfyVsQtcwoQq42dIwgjfUQH5FznpDKR7RAK_3vDpAGaDmDmV0kxHKq8aXbghIfkgPZ3O-nPkFVYUb8GOMwLsEVXoVwEd_ba9RfI-ZY6bqZ1qXbOcp6gc_iWoue9qCguVe5GNGtapxRru0rEeCwQFBM73Q2wecmmZK7tJEcA2k7ezMTTfumAxbfc8JRScEXxmdmRZW03H9HHIcXAX5aQVMyWk2TJXjtxAvjnsjBzaIxAzeHnoB7-oKUV_Mm-yjfwiU5CjQNvK6IRzIJYHKwQdtQiNI7izBDQOR_SXS-0xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=AvHovjteevDy6dCyG-_XVoBonvutThZ7Ms3xK5vlqeeEMhfyVsQtcwoQq42dIwgjfUQH5FznpDKR7RAK_3vDpAGaDmDmV0kxHKq8aXbghIfkgPZ3O-nPkFVYUb8GOMwLsEVXoVwEd_ba9RfI-ZY6bqZ1qXbOcp6gc_iWoue9qCguVe5GNGtapxRru0rEeCwQFBM73Q2wecmmZK7tJEcA2k7ezMTTfumAxbfc8JRScEXxmdmRZW03H9HHIcXAX5aQVMyWk2TJXjtxAvjnsjBzaIxAzeHnoB7-oKUV_Mm-yjfwiU5CjQNvK6IRzIJYHKwQdtQiNI7izBDQOR_SXS-0xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۱۶ تیرماه در جریان سفر به آنکارا برای شرکت در نشست سالانه ناتو، در کنار رجب طیب اردوغان، رییس‌جمهوری ترکیه، بار دیگر از عملیات نظامی آمریکا و اسراییل علیه جمهوری اسلامی دفاع کرد و گفت این اقدام را نباید «جنگ» نامید، بلکه هدف آن «خلع سلاح هسته‌ای ایران» بود.
ترامپ با اشاره به نقش ترکیه در تحولات خاورمیانه گفت این کشور جمهوری اسلامی را «به‌خوبی می‌شناسد» و همراه با چند کشور دیگر، در تلاش‌ها برای پایان دادن به درگیری‌ها نقش مهمی ایفا کرده است.
او گفت اطمینان دارد رجب طیب اردوغان نیز خواهان دستیابی جمهوری اسلامی به سلاح هسته‌ای نیست.
رییس‌جمهوری آمریکا در ادامه با اشاره به روابط واشینگتن و آنکارا گفت: «این حتی جنگ هم نیست، یک عملیات نظامی است؛ خلع سلاح هسته‌ای ایران است.»
او همچنین با تمجید از توان نظامی ترکیه گفت این کشور می‌توانست وارد درگیری شود، اما چنین تصمیمی نگرفت.
ترامپ در بخش دیگری از سخنانش از عملکرد متحدان اروپایی آمریکا در ناتو انتقاد کرد و گفت از نبود حمایت آنها در جریان درگیری با جمهوری اسلامی «بسیار ناامید» شده است.
او اظهار داشت اگر نشست امسال ناتو در ترکیه برگزار نمی‌شد، شاید اصلا در آن شرکت نمی‌کرد و با اشاره به اردوغان، او را «دوست» و «رهبر بسیار قدرتمند» توصیف کرد.
رییس‌جمهوری آمریکا همچنین گفت ایالات متحده برای دفاع از اروپا در برابر روسیه هزینه‌های هنگفتی پرداخت کرده، اما در مقابل حمایت متقابلی دریافت نکرده است. به گفته او، در جریان تحولات اخیر عمدا واکنش متحدان را زیر نظر داشته تا مشخص شود آیا آنها نیز در مواقع لازم در کنار آمریکا خواهند ایستاد یا خیر.
ترامپ در این زمینه از بریتانیا، فرانسه، آلمان و ایتالیا نام برد و گفت مدت‌هاست این پرسش را مطرح می‌کند که آیا این کشورها نیز در صورت نیاز از آمریکا حمایت خواهند کرد یا نه.
@
VahidHeadline
رئیس‌جمهور آمریکا در عین حال تأکید کرد «ما به هیچ‌کس دیگری نیاز نداریم»، اما این پرسش را مطرح کرد که چرا آمریکا «تریلیون‌ها دلار در ناتو سرمایه‌گذاری کرده» تا از اروپا در برابر روسیه محافظت کند، بدون آن‌که چیزی در مقابل دریافت کند.
ترامپ گفت: «به نوعی داشتم دیگران را آزمایش می‌کردم تا ببینم آیا کنار ما خواهند بود یا نه، چون مدت‌هاست می‌گویم ما به آن‌ها کمک می‌کنیم، اما مطمئن نیستم آن‌ها برای ما چنین کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76802" target="_blank">📅 18:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=Oz-NJTYyQMC_H5EuqKOwnMiOmlZgDx8Yf0zv9HbqUt8uKGulzP_O-CNwSezPCo4XqEscjjIwgCL2_gkM_BhU2brf4baExznBo1fcIRKCsqV4-MrsrRXF7E0-JSv9hkPD0jLaZIhHyvw6cF5-EuD-K4SJuD5qUS67IqW5_nHe6H4MJziiflKM2TA8xAgH1AA1zMTfi9zEDuff-DZ7KoSEfXeRgALTgzmTdirWMfUe7tra6Cd-WIe1pncNFzUg5Vy5fLj8GGDsvd4C_ZTmCorQMpBr_uK79KJfWVvsf2dIhOPGxM-m6bg2vMKiWY9wbwdgGitCKnZI0QPfvvZG6KFufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=Oz-NJTYyQMC_H5EuqKOwnMiOmlZgDx8Yf0zv9HbqUt8uKGulzP_O-CNwSezPCo4XqEscjjIwgCL2_gkM_BhU2brf4baExznBo1fcIRKCsqV4-MrsrRXF7E0-JSv9hkPD0jLaZIhHyvw6cF5-EuD-K4SJuD5qUS67IqW5_nHe6H4MJziiflKM2TA8xAgH1AA1zMTfi9zEDuff-DZ7KoSEfXeRgALTgzmTdirWMfUe7tra6Cd-WIe1pncNFzUg5Vy5fLj8GGDsvd4C_ZTmCorQMpBr_uK79KJfWVvsf2dIhOPGxM-m6bg2vMKiWY9wbwdgGitCKnZI0QPfvvZG6KFufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهوری ترکیه روز سه‌شنبه ۱۶ تیر، در نشست خبری مشترک با دونالد ترامپ، رئیس‌جمهوری آمریکا به مذاکرات جاری میان تهران و واشنگتن اشاره کرد و گفت که او و دولتش در تلاش‌اند که روابط آمریکا و ایران را به سطحی باثبات برسانند.
اردوغان در این نشست که در حاشیه اجلاس سران ناتو برگزار شد، تاکید کرد که این تلاش‌ها در راستای برقراری صلح جهانی خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76801" target="_blank">📅 17:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekS9iPJ0krJl0vGG1PrUX7wROyok1rOLH7kjMHqAhg7h4ZxGSn2_HXnGfDiCTnaXQSnHaqlGpVpDuOOJexh6L5cp39qayNzbV5ZPfE8-NYhZxnalmnsabfZhRqQpcyCRDTEnzWKPX_lKh2lrk7OQ98V3ijMqTH2PoYwy-DHX8rs1TaFYXb0te4r4QPb8G6R-mIRMwRdLzW97JMxN6qCwy3wPv67_2pB67W06107kog8VpDgcqjGuyiwDCB0PJiJWwdohJEyo0to3e7M1fG_DoFiSGyznbEfN6Rq2OCP_T9T_vGYbeb9sq3o9a2-0P9nI67cBAfbUT8oh6tld2FZSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است.
خبرگزاری رویترز حمله به آن دو کشتی را تأیید کرده و وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داده بود که سپاه پاسداران دست‌کم دو موشک به سوی آن‌ها شلیک کرده است؛ ادعایی که جمهوری اسلامی تاکنون به آن واکنشی نشان نداده است.
سخنگوی وزارت خارجه قطر روز سه‌شنبه اعلام کرد هدف قرار دادن نفتکش قطری «الرکیات» در نزدیکی تنگه هرمز، حمله‌ای غیرقابل قبول به امنیت کشتیرانی بین‌المللی و تأمین جهانی انرژی است و ایران را مسئول حمله به آن دانست.
هنوز هیچ گروه یا کشوری مسئولیت حملات تازه به نفتکش‌ها در تنگه هرمز را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/76800" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=fSpTWIhR4jMFiT-0VHIlzOWT3cnd0UTcbg5l0mW2IqdgPxHHvd4dMI9IAoTl8afYpwJ3i7fyniKMtB3AEZqb05S4QgxZ3XrwetgeTIkoKCHeDN6n2jhgKsceuxcSh07zVH_WBob9J1ZWOqkSYDjRwI7sSGo3CqdChrBpjlqIaH43Vo6NAdgUIBFtDNN6P_F50eHC5e3z9eBNm-z5jZL8AO3QxjG48GLAN1wKBL_eo1vyAx5zxACRNb6e4Zo4w28euly6S42WMX6UqlL7QCrVp3u2bS6-n38uEa4KsqWD59N6P067iH5HAUw04NQKeg6ka57U8GtrImCNAVIEbkzDXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=fSpTWIhR4jMFiT-0VHIlzOWT3cnd0UTcbg5l0mW2IqdgPxHHvd4dMI9IAoTl8afYpwJ3i7fyniKMtB3AEZqb05S4QgxZ3XrwetgeTIkoKCHeDN6n2jhgKsceuxcSh07zVH_WBob9J1ZWOqkSYDjRwI7sSGo3CqdChrBpjlqIaH43Vo6NAdgUIBFtDNN6P_F50eHC5e3z9eBNm-z5jZL8AO3QxjG48GLAN1wKBL_eo1vyAx5zxACRNb6e4Zo4w28euly6S42WMX6UqlL7QCrVp3u2bS6-n38uEa4KsqWD59N6P067iH5HAUw04NQKeg6ka57U8GtrImCNAVIEbkzDXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری که در شبکه‌های اجتماعی منتشر شده گروهی از شرکت‌کنندگان در مراسم تشییع جنازۀ علی خامنه‌ای را نشان می‌دهد که به عباس عراقچی ، وزیر خارجۀ جمهوری اسلامی ایران، حمله کرده و او را «بی‌شرف» خطاب می‌کنند.
گروهی از هواداران نظام جمهوری اسلامی که با مذاکره و توافق با آمریکا مخالف هستند، اعضای تیم مذاکره‌کننده را به «سازشکاری» متهم می‌کنند. روز گذشته نیز تصاویری مشابه از حمله به مسعود پزشکیان در حاشیۀ تشییع جنازۀ علی خامنه‌ای منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76799" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqXaW5kdOKwJ_1OQV0k0uKvU5puNPL6Hh8A3m7nlKMlrgz3Xg8eUt3t794hdN6NhE5XO5hFd1veug3scG8XRZrKLf5pEuA032wbSSSwaPTtNFL6JcjJ9ak8Yf--oqMOvNbMcX6u62uyAodMyJwypCuwt55wCEXnULUydBs9fJIWXIFAiZSrhifxOXUI1LHqx0SSrQ1CB49_FOVJVA3aSAYEGp6F3oyZxoX-LFBpgLSXqXxj-_0KLGEWnW-to3EQgPzCuoGbKRLK6s4PLP4c_Zwu_meNQs_ZqleWdPCAqIWrZ2NAKiwYIg8f20ABxmmZCmVX1LLEUVHoCgUNkl6eEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با نزدیک شدن زمان انتقال تابوت علی خامنه‌ای به عراق برای اجرای مرحله تازه‌ای از مراسم تشییع رهبر پیشین جمهوری اسلامی، محمدرضا سیستانی، فرزند ارشد علی سیستانی، مرجع عالی‌قدر شیعیان در نجف، به دفتر علی خامنه‌ای اطلاع داده است که پدرش بر تابوت او نماز نخواهد خواند.
در همین حال، جواد شهرستانی، داماد و نماینده علی سیستانی در ایران، نیز در مراسم تشییع و نماز میت علی خامنه‌ای در تهران حضور نداشت.
پیش‌تر محمدکاظم آل‌صادق، سفیر جمهوری اسلامی در عراق، اعلام کرده بود که مراسم استقبال رسمی از پیکر علی خامنه‌ای شامگاه سه‌شنبه در شهر نجف برگزار خواهد شد و آیین تشییع عمومی نیز از ساعت ۶ صبح روز چهارشنبه در شهرهای نجف و کربلا ادامه خواهد یافت.
خودداری علی سیستانی از اقامه نماز میت بر پیکر علی خامنه‌ای در حالی صورت می‌گیرد که جمهوری اسلامی از زمان کشته شدن رهبر دوم خود، مجموعه‌ای از مراسم تشییع و وداع را در چند شهر ایران برنامه‌ریزی کرده و اکنون نیز در تلاش است این آیین را با برگزاری مراسم در شهرهای مذهبی عراق ادامه دهد.
غیبت مهم‌ترین مرجع شیعیان عراق در این بخش از مراسم، یکی از مهم‌ترین حاشیه‌های مرحله عراقی تشییع علی خامنه‌ای به شمار می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76798" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQJmDuj3rnxmFAuFtFx4UY-WJo4v358HVNCpvBGl6w-4g0AF-EuHObCBclnbqe1OuFXiJV2tP9lHnYrQ2LGHOLL--SQ0tEokcEadZWHknlTfnBt2YdKYjYVO7FrU9fKhLO6hUOZAPbvw-HDIJOO_eIRMfTht1r5Ll5vF-80L9GNlmZNvndzzdUsFegKdZy7mQr2_ncKsVBSHGlOz1UiY7CPGBkzlV77Q_8KU5QM7ufoyRlG6VwjYcBgidoTnkQVifsZ7fsFTV1N-IXNGTFXwu00UG1gWzswmKG2zxcssCoqXTPgqw5W5FBhAGC2wRL_Oj-ZoNWVP9XzAgMIn5XnefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داد که سپاه پاسداران روز دوشنبه دست‌کم دو موشک به سوی کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است.
بر اساس این گزارش، دو کشتی در پی این حمله آسیب قابل توجهی دیده‌اند، اما هیچ تلفات جانی گزارش نشده است.
حمله گزارش‌شده پس از آن رخ می‌دهد که مهلت توافق یک‌هفته‌ای میان ایالات متحده و ایران برای توقف حملات در تنگه هرمز به پایان رسید.
اکسیوس می‌نویسد که ازسرگیری حملات ایران، تفاهم‌نامه‌ای را که کمتر از سه هفته پیش امضا شده بود، در معرض فروپاشی قرار داده است.
این منبع خبری می‌افزاید که
احتمال می‌رود ایالات متحده در واکنش، اهدافی در ایران را هدف حملات نظامی قرار دهد.
@
VahidHeadline
صداوسیمای جمهوری اسلامی به نقل از «برخی منابع» گزارش داد که «نفتکش الرقایات» متعلق به قطر، قصد داشت «با حمایت نیروی دریایی آمریکا» از مسیر عمانی تنگه هرمز عبور کند، اما «پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است.»
این گزارش تلویزیون حکومتی جمهوری اسلامی این‌گونه القا می‌کند که تهران این حمله را انجام داده است. با این حال، جمهوری اسلامی تاکنون به‌طور رسمی مسئولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76797" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyqwpU4Ah72cpGDufG_Cl6r6PWuZ2He5So8K4SWZYttVyqO7oQRS6-_SmgzGhWMcBmJwx4yFYkSbkJl5Av6FmHO7sFJAwzaNVX8rXm18UMBrNDer-UDtTzbMns8eaem0TCGGRX6Mm9EB_Oh6X_DUU32sSzfgd9VcUc1r1rLGIm3RpeHu2GXeluHNlvEgrt0ayzyf5-JNPttKxfbcNIarKRl1QO0PZKTyyllLyef5Y-T--yI70ydu48rSgeILMN4uBTVZ3ZKm28mvd07IVLpgMtqtzZGIZbSEqkYQuCarS-P3rMLsSrJGdu5AMOEtkUMBww4wXAvp6EWlyO23ifue-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، بامداد سه‌شنبه ۱۶ تیرماه، اعلام کرد یک نفتکش در حدود ۱۵ کیلومتری شرق لیما (Limah) در سواحل عمان، هنگام حرکت به سمت جنوب، از سمت چپ بدنه هدف یک پرتابه ناشناس قرار گرفت.
به گفته این سازمان، این حادثه باعث آتش‌سوزی در نفتکش شد، اما تاکنون هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد مقام‌های مسئول در حال بررسی این حادثه هستند و به همه شناورها توصیه کرد هنگام عبور از این منطقه با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به این سازمان گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76796" target="_blank">📅 03:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=dDwv77k1iTGY9nPJ2WhtsoRJdxJQxTdL3U7i6yMzPMhmhk2XYrWL6c8kWt7QwpLhHWuHNFKWS_p_X5kcgiQrOMxWLyT95IINfsdWiAKFlh7hrjUjKkUOxN_9u59TcHU1XGrJSms2dMNkARHQXEH4GbrNhCRHDnbJNsUXL1ojwDwrhSDtecX1URkiyiH_74Prlbpbpmqd3ssAlEoTMPaBpuInG8xKfvhjig7-zuG_IMi1s9leJMnjRWXcq7k54jhtu17ydPTBotZBkfG2PgZ9sUU73IIx9-U9nOdilE0ic4S6EgEBbCeu43Z2NcoJfEhF7KayH0z8FaqFh9HEGTGN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=dDwv77k1iTGY9nPJ2WhtsoRJdxJQxTdL3U7i6yMzPMhmhk2XYrWL6c8kWt7QwpLhHWuHNFKWS_p_X5kcgiQrOMxWLyT95IINfsdWiAKFlh7hrjUjKkUOxN_9u59TcHU1XGrJSms2dMNkARHQXEH4GbrNhCRHDnbJNsUXL1ojwDwrhSDtecX1URkiyiH_74Prlbpbpmqd3ssAlEoTMPaBpuInG8xKfvhjig7-zuG_IMi1s9leJMnjRWXcq7k54jhtu17ydPTBotZBkfG2PgZ9sUU73IIx9-U9nOdilE0ic4S6EgEBbCeu43Z2NcoJfEhF7KayH0z8FaqFh9HEGTGN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که از جانی اینفانتینو، رئیس فیفا، خواسته است اخراج فولارین بالوگون، مهاجم تیم ملی آمریکا، را بازبینی کند، زیرا به اعتقاد او خطایی که منجر به کارت قرمز شد، عادلانه نبوده است.
آقای ترامپ در جمع خبرنگاران در دفتر بیضی کاخ سفید گفت: «تنها کاری که کردم این بود که درخواست بازبینی دادم، چون فکر نمی‌کردم آن صحنه خطا باشد.»
او همچنین داوری را که این کارت قرمز را نشان داده بود، «افتضاح» توصیف کرد.
این اقدام بی‌سابقه، روند رسیدگی انضباطی فیفا را در کانون توجه جهانی قرار داده و با واکنش خشمگینانه بلژیک، رقیب آمریکا در دیدار روز دوشنبه برای کسب جواز حضور در مرحله یک‌چهارم نهایی، روبه‌رو شده است.
اتحادیه فوتبال اروپا، یوفا، هم به‌شدت از این تصمیم غیرمنتظره فیفا انتقاد کرده و آن را «بی‌سابقه، غیرقابل درک و توجیه» توصیف کرده است.
@
VahidHeadline
در ادامه واکنش‌های گسترده جهانی به رفع محرومت فولارین بالوگون، مهاجم تیم‌ ملی آمریکا، فدراسیون فوتبال بلژیک روز دوشنبه ۱۵ تیرماه اعلام کرد تصمیم فیفا برای صدور مجوز این بازیکن در رقابت مرحله یک‌هشتم نهایی جام جهانی را به چالش می‌کشد.
فدراسیون فوتبال بلژیک در بیانیه‌ای گفت از روند طی‌شده برای این تصمیم «عمیقا نگران» است و برای دفاع از «اصول بنیادین اخلاق، رقابت عادلانه و منافع فوتبال» به پیگیری این پرونده ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76795" target="_blank">📅 22:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f07511960e.mp4?token=d24IArJYSxhUsJM9iBN8p5PmW3s0wTJVaBq4FYpbIJayZDwjD3thz0ygFGPVZgkEO5oKxPLnP4LplfpjyTtY5nCyKz7XY884FTEsO2FFFyAvfy-DJjo17b_I-0a5pJ9-NmV5Syj-Y78QrVHX3eky3WSL_I6GFrdkhNOB8iDvpv1LM3fY_lNqZ_Lp0KpwPiMk_azrxtvlVPwO2bPK7yIFBN1vD9reni0XbdUSfbzjSv6BwUrZiQ-f2FM7so-yxGXcVR_pX3cQS2RF9SxUAkWfWChPBtrg7-oip556WV3YN1sHeWvEP_aOULwqbtwwbslJgVoZjzwMg1Tlopem9nYz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f07511960e.mp4?token=d24IArJYSxhUsJM9iBN8p5PmW3s0wTJVaBq4FYpbIJayZDwjD3thz0ygFGPVZgkEO5oKxPLnP4LplfpjyTtY5nCyKz7XY884FTEsO2FFFyAvfy-DJjo17b_I-0a5pJ9-NmV5Syj-Y78QrVHX3eky3WSL_I6GFrdkhNOB8iDvpv1LM3fY_lNqZ_Lp0KpwPiMk_azrxtvlVPwO2bPK7yIFBN1vD9reni0XbdUSfbzjSv6BwUrZiQ-f2FM7so-yxGXcVR_pX3cQS2RF9SxUAkWfWChPBtrg7-oip556WV3YN1sHeWvEP_aOULwqbtwwbslJgVoZjzwMg1Tlopem9nYz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه بار دیگر گفت: من به دنبال تغییر حکومت در ایران نیستم، هرچند این تغییر حکومت اتفاق افتاده است.
ترامپ افزود: حکومت اول از بین رفت، حکومت دوم از بین رفت. حکومت سوم معقول‌تر است. خواهیم فهمید.
@
VahidHeadline
دونالد ترامپ گفت آمریکا یا با ایران به توافق خواهد رسید یا «کار را تمام خواهد کرد.»
رئیس‌جمهور آمریکا در یک گفت‌وگوی تلویزیونی گفت قیمت نفت با وجود بسته شدن تنگه هرمز چندان بالا نرفت «آنقدر که ما نفت از آنها گرفتیم. مردم اصلا خبر نداشتند و همه اینها فقط در عرض یک ماه و نیم اتفاق افتاد.»
رئیس‌جمهور آمریکا بار دیگر تکرار کرد که کشتی‌های نیروی دریایی و تمام هواپیماهای نیروی هوایی ایران را از بین برده است: «در نهایت فهمیدند که دیگر رادار ندارند، چون سامانه‌های راداریشان نابود شده بود. بنابراین، آخر شب و در تاریکی آنها را هدف قرار دادیم.»
او همچنین گفت: «نیروی دریایی قدرتمند ما بزرگ‌ترین محاصره‌ای را که کسی ندیده اعمال کرد و در طول دو ماه حتی یک کشتی هم نتوانست از محاصره عبور کند. بعد نزدیک شدیم به اینکه شاید بتوانیم به توافقی برسیم پس محاصره را کاهش دادیم. نمی‌دانم، شاید هم به توافق برسیم.»
آقای ترامپ تاکید کرد که «به هر حال پیروز خواهیم شد. یا به توافق می‌رسیم، یا کار را تمام می‌کنیم.»
او گفت تمام کردن کار ایران کار آسانی است: «تمام کردن کار دشوار نخواهد بود. البته من ترجیح می‌دهم توافق شود، چون نمی‌خواهم ۹۱ میلیون نفر تحت تأثیر قرار بگیرند.»
«ما می‌توانیم ظرف یک ساعت پل‌هایشان را ویران کنیم. می‌توانیم شبکه تأمین انرژی را از کار بیندازیم. همه آن نیروگاه‌های بزرگ، زیبا و مدرنی را که ساخته‌اند. آنها پول زیادی داشتند اما حالا دیگر پولی ندارند. ما هیچ پولی به آنها نداده‌ایم اما می‌توانیم برق و نیروگاه‌های تولید برقشان را از کار بیندازیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76794" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e2iCryNpjIzngZ6O6HmULA-qWRUAB6syBoEhvtMMpwla6RxjqieUPWpjW6lbTq2bfWhYrBwlsqVrr08uPBGzDWAUx1CsZjvpwhzq1EzUuvJIbMG7WRE5db48xObMSHd7SQ29X14cW2_P5hazbCrEQYZ53BnFG6wv5aCb8oiZBT5w81fYnm4ZQhJdM6k1Ne3w_AVAySQbiqkmxMcL6xK87YIeaSGVnxbGHcyVJ0qtIdeT7m4rEbs0SoEUgDqWZqYbw4AV_mF_KbiCwQ7tidSZ_De7sJwgw7ZJtqTlFw8wGAuONM24EwkBHCRbg-j_GrPN3NujA4oH-13wP84Cw3iF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=ZmTVgZi5kD-FmYdOz4GDGY41dRsFPsEYW15hmpxoVupkmCn53j8TJmWhUeJqI8mHSw_Xzh2g_LpRmVzorLNHDwqJ-DvOPkQ1Ton6ZFl97x7QNpvk8gBfz9lLa4g2UYOWhiUfbyQok1HZror1Llq-5mH4h8L6KH0U_6IhCqsQkCi1h9Q0rvO5X8D_8hq-WppdMCPds3V5Rn8L3naMeQ_j_EhMrko0cCp1vnlf0vofPAZ7MfrsDb19Td1neFxA829fSzILJhlTQVclDp2180FGXWtRYnC3dRniJ9kakGwUUBUH8yuWbfLccDphAdGMc4ZF55ifXOKt6WOYNY8-uNHBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=ZmTVgZi5kD-FmYdOz4GDGY41dRsFPsEYW15hmpxoVupkmCn53j8TJmWhUeJqI8mHSw_Xzh2g_LpRmVzorLNHDwqJ-DvOPkQ1Ton6ZFl97x7QNpvk8gBfz9lLa4g2UYOWhiUfbyQok1HZror1Llq-5mH4h8L6KH0U_6IhCqsQkCi1h9Q0rvO5X8D_8hq-WppdMCPds3V5Rn8L3naMeQ_j_EhMrko0cCp1vnlf0vofPAZ7MfrsDb19Td1neFxA829fSzILJhlTQVclDp2180FGXWtRYnC3dRniJ9kakGwUUBUH8yuWbfLccDphAdGMc4ZF55ifXOKt6WOYNY8-uNHBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیمای جمهوری اسلامی روز دوشنبه ۱۵ تیرماه تصاویری از حضور احمد جنتی، دبیر شورای نگهبان در مراسم تشییع پیکر علی خامنه‌ای منتشر کرد.
رسانه‌ها روز دوشنبه همچنین تصویری از محمود احمدی‌نژاد را در مراسم مرگ رهبر سابق جمهوری اسلامی منتشر کردند.
خبرگزاری فرانسه روز دوشنبه گزارش داده بود در حالی که مقام‌های جمهوری اسلامی تلاش کرده‌اند تصویری از وحدت در صفوف حکومت ارائه دهند، تاکنون هیچ‌یک از روسای جمهوری پیشین جمهوری اسلامی، که روابطشان با خامنه‌ای دچار تنش بود، در این مراسم‌ها دیده نشده‌اند.
مراسم تشییع جنازه علی خامنه‌ای پس از دو روز قرار گرفتن پیکر او در مصلای تهران از ساعت شش صبح دوشنبه ۱۵ تیرماه آغاز شد.
روز ۹ اسفندماه ۱۴۰۴، در موج اول حملات اسرائیل به تهران بیت علی خامنه‌ای به‌شدت بمباران شد،‌ به شکلی که تمام ساختمان‌های محوطه بیت با خاک یکسان شده بود و همین احتمال سالم ماندن جسد رهبر سابق جمهوری اسلامی را بسیار کم می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76792" target="_blank">📅 16:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgoxxczbMpqPYXVQk3piVj-M5U6AhMbvrgH5UkYCe-MB_KR0NCV2sxJd2U5ihdVOlTI-WTRGriYCn_8MxqM3QvHOimMgnWQoxwg2kI-EL66Bb6ajJaGmXw1SxLpsg-BYpDI5mW_xO5v7yjOasLbTHnWxMo4n7OLx4VJC8wGeot0QyUc3vPSAN1xxrI3_xkcFPUvNkcUutdkTZObZxmvZesjjYp3Z8VmNy-iDxg3uNb9VCsecpwxh4SO093haAA42ihZgHh0C2UhZcsI3sV1LI_aFQd_l5pisF2Q8cIlf6HB8hc5-xb84ie_VeFxGgGrgul-o9Od7ExVVmy8hxgcTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، آقای مهدی ناظر و خانم مهناز چاردولی، نامزد او، را به اعدام و ۱۰ سال حبس محکوم کرده است. همچنین خانم عاطفه ناظر، خواهر آقای مهدی ناظر، به ۱۰ سال حبس محکوم شده است. این سه نفر در تاریخ ۲۱ دی‌ماه ۱۴۰۴ در تهران بازداشت شدند.
@IranRights</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76791" target="_blank">📅 16:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZsYWsAsAyBghyHr23u1zvHV9o-42_K2_4RP2SMtJTnXCKwcw5W-kxZPItQpQFQF5pySUpLhKFjTssEBXsdZ5m32SO5sZR9bkslhrEYuf1INEYKqWmMEXH6ptc7-Nc0Y0pgL8AIAfhpOWcTOggqdCqQXyD_ipb85B8ljeXMglXBp0fhUCUQKyBdVu2jc9fEZCrCFC6Lu0o0B5WzFB-SYxEi1o6uLDpeK_GjC96M-NTpaxZvluI1Co64C5FUnHZSQ5dEfK5fjEj1YhXqGIDEq-YoEHv-wP87AyQWGAehRgX2Qb302a_G2Q-RYXqwjPTzG4zX72yJRb3fRYExKQaefeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه روز یکشنبه ۱۴ تیر متن حکمی را منتشر کرد که در آن مجتبی خامنه‌ای، رهبر جمهوری اسلامی، غلامحسین محسنی اژه‌ای را برای یک دوره جدید پنج ساله به عنوان رئیس قوه قضائیه ابقا کرده است.
محسنی اژه‌ای از دهم تیر سال ۱۴۰۰ با حکم علی خامنه‌ای به این سمت منصوب شده بود و مدت پنج سال ریاست او بر قوه قضائیه به پایان رسیده بود. حکم رهبر جدید جمهوری اسلامی با امضا در تاریخ ۱۳ تیر منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/76790" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uu63J3Q6eqj2_ogdVj1O_F8bU7P9PAth_hBRkoTsmfSIRfEQtvv9qdrj-4J8Sbaqnf4bAuJ-m6jAs7jUCscfUO7FdulwihZwB6WnTtDMIiUjpaaTuemMJQODSsjLTM2tpNxuzQPmVPfyoOvC5a7e8XjJxeKMFVvb4YjKRSf-EHGUnCGjcwL63ALVI6HAEIZZldeGJ2fp-so8C-edSk5pJin3kIRTs6mU_RiocYEW_FUjsPuNAbDDZvHv3LUCSQ_I8_KkAjevLK7fVPIeyRxbgP_wY_eQB7Hvk1bLj4Zgk1RqaOC4uL1I25EJDjlfnmzT6lGJWA2IC4cN_2xhx7E9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=PtTnENQpRhkZ7MvMli0AMPaj7JSianWlUCMgqm2l_KEqOfot2QIIZ05JSKOP0M2sp76_z1lDq6zWyjJ4EgNOr1m-C7RasnwQ7afOVgNdcXYZAtMTgY8_zHrAeHkbGN2OCjjG1V8oJ5wrhXt-x1dZAURPU1HPqtbh3J3bdaByzgjMyEKnQX8bBM9-vf2W8640nWhXhWrfuWbqAI4G4-W-51dX-H5MQ92jvHdh74dAr_42OxdK2oUv1LcpN0Xhg7yeRlvODPjAn8l23AsxldKwZEBO6guztfgBQdL8vD1U--Hns7CH88-wub7zIxkQN9tHSMBNaq_5L_GXAIb3WHerkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=PtTnENQpRhkZ7MvMli0AMPaj7JSianWlUCMgqm2l_KEqOfot2QIIZ05JSKOP0M2sp76_z1lDq6zWyjJ4EgNOr1m-C7RasnwQ7afOVgNdcXYZAtMTgY8_zHrAeHkbGN2OCjjG1V8oJ5wrhXt-x1dZAURPU1HPqtbh3J3bdaByzgjMyEKnQX8bBM9-vf2W8640nWhXhWrfuWbqAI4G4-W-51dX-H5MQ92jvHdh74dAr_42OxdK2oUv1LcpN0Xhg7yeRlvODPjAn8l23AsxldKwZEBO6guztfgBQdL8vD1U--Hns7CH88-wub7zIxkQN9tHSMBNaq_5L_GXAIb3WHerkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماز میت بر جنازه علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، روز یک‌شنبه، ۱۴ تیر رأس ساعت هشت صبح، توسط "آیت‌الله جعفر سبحانی" اقامه شد.
مراسم تشییع او بیش از چهار ماه پس از مرگش در حال برگزاری است.
اما نکته قابل توجه در این مراسم غیبت مجتبی خامنه‌ای است که از او به عنوان آیت‌الله یاد می‌شود و کمتر از ده روز پس از مرگ پدرش به عنوان رهبر تازه جمهوری اسلامی معرفی شد، اما در این مراسم حضور ندارد تا نماز میت را برای پدرش اقامه کند.
در این مدت طولانی از مجتبی خامنه‌ای نه فایلی صوتی منتشر شده و نه ویدئویی که نشان دهد او توانایی رهبری حکومت را دارد.
با این حال سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از روز ۹ اسفندماه سال گذشته یعنی آغاز جنگ تاکنون خبری از آنها نبود روز یک‌شنبه بر سر تابوت پدر خود حاضر شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 480K · <a href="https://t.me/VahidOnline/76788" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIb_Tppv39SRJVU0h1rqazWY6K0QChHnJLi0ykDQl2uxUbR7mEy9nFObi356bGsL8SmIljbTcTQO8nY0_SbeAD_gcipMGHAMC1o8XuGPB7j4Uj2OpPSLGJXCF5V5w-oMDulBbJenDJFC7qHfnBbDcpK1BFPS_OhYNpKQ4SNZFq36fSQ0smPeid8m8Das8mWmjw6ehyTiM7-q3QAIwMZDAllvtSA05cSayula-7wR0v2J3e2R6ulQOWFozSUjwCfs1wbP5kVI4NDb_kgsCpFBoVWaWbtvn7YHLo6hONokdo8dkE_wRXLs-YBFtjJdrYRfnx75IBjo5L__65doAoF7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا روز شنبه ۱۳ تیر، در گفتگو با وبسایت خبری آکسیوس، اشاره کرد که تصاویر مربوط به مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی را مشاهده کرده و از دیدن گریه افراد، متعجب شده است. او گفت:
از دیدن برخی ایرانیان که در مراسم تشییع گریه می‌کردند متعجب شدم چون گمان می‌کردم مردم از او متنفرند. شاید این اشک‌ها ساختگی باشد.
ترامپ پیش‌تر اعلام کرده بود که مذاکرات جاری میان تهران و واشنگتن، به‌دلیل برگزاری این مراسم یک هفته متوقف شده است. او در بخش دیگری از این گفتگو با اشاره به حضور اغلب چهره‌های سیاسی و نظامی جمهوری اسلامی در این مراسم گفت:
آن‌ها همه آن‌جا جمع شده‌اند. کار یک شلیک است! اما این کار را نمی‌کنم چون در آن صورت کسی برای مذاکره باقی نمی‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 476K · <a href="https://t.me/VahidOnline/76787" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این مجله ۹ ماه قبل از سرنگونی حکومت صدام‌حسین در عراق و سپس اعدام او نیز عکس صدام حسین را روی جلد برده بود. معمر قذافی نیز از دیگر رهبران منطقه بود که ۶ ماه قبل از کشته شدن به دست معترضان، عکس او روی جلد تایم رفت.</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/76786" target="_blank">📅 19:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=endsIqu7SumHmfrKBLai2vf4-Tys-dtQfDDZLhARtLpGVdgQLoRNHyOuASQqKfu7rLuZ4V9p1RAd354_X4FucT91HZ7B6ult35vlDCGR3xB8ink1y6UZIiIKvoeYG3YI0QVFM9WPU-MIRSNi5yRKF5iy5zkzR1NklbBif2Fov_3Tkv4O9J7LqJR85ywdekMAvkOfh8JDr5YgsvSydKI_E6d7ZMDopZT6r5in3MtrdtkyW5MPTqOs3bnWtx_ge8DdKsH-NtNds-iWPpBaIBrkEltXTV6GkekwU8kHqKkCYntGWn9irYPEsd_tQuex3HSZMXtM6wgsjIG6pMxJyGnEfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=endsIqu7SumHmfrKBLai2vf4-Tys-dtQfDDZLhARtLpGVdgQLoRNHyOuASQqKfu7rLuZ4V9p1RAd354_X4FucT91HZ7B6ult35vlDCGR3xB8ink1y6UZIiIKvoeYG3YI0QVFM9WPU-MIRSNi5yRKF5iy5zkzR1NklbBif2Fov_3Tkv4O9J7LqJR85ywdekMAvkOfh8JDr5YgsvSydKI_E6d7ZMDopZT6r5in3MtrdtkyW5MPTqOs3bnWtx_ge8DdKsH-NtNds-iWPpBaIBrkEltXTV6GkekwU8kHqKkCYntGWn9irYPEsd_tQuex3HSZMXtM6wgsjIG6pMxJyGnEfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحیم صفوی: این یک جنگ موجودیتی است و مطمئنم که اسرائیل از بین خواهد رفت
یحیی رحیم‌صفوی، از فرماندهان پیشین سپاه پاسداران و مشاور مجتبی خامنه‌ای در حاشیه مراسم تشییع علی خامنه‌ای، با اشاره به درگیری میان جمهوری اسلامی و اسرائیل، آن را یک «جنگ موجودیتی» خواند و گفت دو طرف در نبردی قرار دارند که تنها یکی از آن‌ها می‌تواند در منطقه باقی بماند. او افزود: «من مطمئن هستم آنچه باقی خواهد ماند ایران است و آنچه از بین خواهد رفت اسرائیل است.»
او همچنین با مقایسه کشته شدن علی خامنه‌ای با واقعه عاشورا، مدعی شد کشته شدن او، «حرارتی» در میان مردم ایران، شیعیان و جهان اسلام ایجاد خواهد کرد.
رحیم‌صفوی در بخش دیگری از سخنانش ابراز امیدواری کرد که مجتبی خامنه‌ای راه پدرش را در حفظ «ایران قوی»، دور نگه داشتن سایه جنگ از کشور و پیشبرد توسعه ادامه دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/76784" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuMOrhIplh_0hwXH9QH0DxwftogXVXzT3-1NV-lXmPAdUssj8riAH_lgt2YiezxtPdJW1Zi_uQuYFepHCZXXZOGvvLWctzd1mIo77VFOxtEfX6jE71m0DZh3FzqnvXH_jkBTHa8bRtJ-H5O-btjV9Ja2vR1NRrDGuFEk_eyskumJswFTceQ-VDr98dz3BOungzcaf9veYQUtfeYO0yLItCzCQfnV6oO9E4lXJQMM3lGw__F8NdB6b_Wb1IGJnSjblg736vGExXPBkqIZFRmSdo05IfOL2BRzmwAn9RzFeL9QHc-7pRa2gCa1Ji9_9qT4LCKZZKjQ4kvr_uLUHMaC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ اعلام کرد به‌دلیل مراسم تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، «یک هفته» به مقامات تهران فرصت داده است.
رئیس‌جمهور آمریکا در سخنرانی خود در مراسم دویست‌وپنجاهمین سالگرد استقلال آمریکا که شامگاه جمعه ۱۲ تیر به وقت تهران برگزار شد، گفت: «ایران را به‌شدت در هم کوبیدیم. آن‌ها برای توافق بی‌تاب‌اند. به‌شدت می‌خواهند به توافق برسند. ما به‌خاطر مراسم تشییع، یک هفته به آنها فرصت دادیم، چون آدم‌های خوبی هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/76783" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ-Y0KjbrhRbR4aiJ1YLydB1dG33T5FsUyBC0LcQazbBaPLMGpmnEWL1ynOA5BUA7rZSX7hZnGO8mXsT3UZLCN3r5FvdwnUi6nwvUP9zbVPRSB06GGrGGKkc306ejkF8qjDNoFBye-raRITZaBas4KfRm6CTUK5Z64SvvLCj9Y9H2hFovlF2uMhVkhmAB4GFUvodf4MNQqWM32YKjQTzHM7eFl4xftPR49juUKiax2VcYCJovBtykScgi0Ojc4KCLjjAao4VuSvFZzrn2yxLcZsuBYkPQkQ45-BEf9WVMdepIX9fmTgh5wEekQ24trnJnQOtzVGwgPXHKD910DpF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگین کیانی، عکاس مستند اجتماعی و مدرس عکاسی، از سوی دادگاه انقلاب بابل به یک سال حبس محکوم شد.
رسانه‌های حقوق بشری گزارش گزارش داده‌اند، شعبه اول دادگاه انقلاب بابل خانم کیانی را به اتهام «تبلیغ علیه نظام» به یک سال زندان محکوم کرده است. این حکم روز ششم تیرماه صادر و به او ابلاغ شده است.
نگین کیانی ۱۹ فروردین امسال در منزل پدری‌اش در بابل توسط نیروهای امنیتی بازداشت و یک روز بعد با قرار وثیقه آزاد شده بود.
این عکاس ۳۷ ساله پیشتر نیز به دلیل فعالیت‌های مدنی خود چندین بار احضار شده و با برخوردهای قضایی روبه‌رو بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/76782" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxGHsrZ4K0ZF6pFInSCqm7KJAmRjBJl2YciMYhQxS9mexH-natDEdZWUKMcdbI8WAQ5QVQn_07Yg0SFqErlRk6NOGz9qioqP7RmYWqO_6ikNmgKaY2AHjfYe9EI9hB78n-wrBX2-GdzayC83shWF6zRHPqkdzRmkzt3Svw-r4fmgfYrXUF2PukhD5ZziLABWdMyS70NRQ9AdOWV1d2_-3sh1DFfODwvtySCzI0tqn8Kw5ezYGv030fHB5hri7vO0tZip2JAMYhmP6LUlL5J28RLDjNprolwT2QgsqBfRgkYm-LNdbYBrB5YvJVw2EzBcwoarX79fv602wCYCRlhKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرنوش پارسی‌پور، نویسنده، مترجم، تهیه‌کننده و فعال اجتماعی ایرانی، امروز در بیمارستانی در حومه سانفرانسیسکو درگذشت.
خانم پارسی‌پور که از دهه ۷۰ خورشیدی در شمال کالیفرنیا زندگی می‌کرد، از هفته گذشته به علت سکته قلبی در بیمارستان بستری شده بود.
او در سال ۱۳۲۴ در تهران به دنیا آمد و اوایل دهه ۵۰ خورشیدی از دانشکده علوم اجتماعی دانشگاه تهران فارغ‌التحصیل شد. نخستین داستان بلندش، «سگ و زمستان بلند»، را نیز در تهران منتشر کرد.
خانم پارسی‌پور در دهه ۵۰ برای مدتی در تلویزیون ملی ایران کار کرد و سپس برای ادامه تحصیل ایران را ترک کرد، اما در سال ۱۳۵۹ به ایران بازگشت.
او مدت کوتاهی پس از بازگشت به ایران بازداشت شد و چهار سال را در زندان گذراند. پس از آزادی به ترجمه و کتابفروشی پرداخت، اما فشارها ادامه یافت و سرانجام به آمریکا مهاجرت کرد.
خانم پارسی‌پور در سال‌های اقامت در آمریکا نیز چند داستان بلند و ترجمه منتشر کرد.
شناخته‌شده‌ترین آثار او در ایران «طوبا و معنای شب» و در خارج از ایران «زنان بدون مردان» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/76781" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gh-39_gSKjueWsYKljmfe8EVeNDazF0noKzWa330LBy00WwyFkiHanhnm1672XawwmvkSLMqTKri6c0z3hkAPIT36s2ZMgb1a1AXD9j2iLWFQYNxLkcBE87vFVE5KvleZXQyr-BXiasyFlmQ69T1Fxmoss2OJKMMQ8a7TXquT_InWbaK1ZhrrAkyOgoUjJgfvNz8iEem8xaEPSkt6P2AH-Dm-ZvOZn7LanOBFsRDk3uq813EBZXSgh6y2PQT47YerZeM_dZ4ZH-Y9j4eee-C_lQMrQwaHJ9pl8QZy3L4zn_r2GeFX-GcUplddl625XSnMLgjA3DszLFBlmcNWswYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MQKsOOSo0Prr2sRPp7Ozd-YDWNF74PZcLpi_wyd7FCqTaap1ZFad3FXrH17DW56wxFLTXn-sQDZIx_g8x2mySvz7jIceMluadHx44zGJD1-p366b4Has-xNUZ0qOejYWnlkM6v1EY5GCsG04wjGDi3TFCEysTCN4inibg3EB1aP9VGTl5a94qD3Zwvjmr5tHemJqS9B2rvxxvTocv8x9qVdTdPpRaayDvFWPiswIxglsPL0tZmomTx8VbCBCzGj7t60lHcPPLlOM8MPJAbrPjVNMlb7h9rXzB0x0kJv0_aW9xIpT0B1kF-P1QxqyoYHq2N9UTp5FhdcBiqcbuzzrkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=Fi86H5jDBPlGPXAbMeVicnP5SzLbadgt7iWEHkcEBGf3Zr439X5syxI9X1LKX3MPaXb67uJUvdO9Oi8oTonqKAOQVnVz57NnY9zlOoYNtpO_N1YoRTn62oNT77NHztQE__rU0p9hpdyozavpVxBUCcEg22WLQf3eEU5atcKDwc77JHitMt-iIMvjfk-dsbLMkcfplBPl9JsCuWbPO3y4d9L37UN9j4gN22YNREUw_NLPShY7CuMaSPvDIP2W4x7E7ZGB8JFsjvt1QdUosRoU9Fa1JmCup_55eBX_7Kj_5HJA-eaIkx6f1aaytIs3uU3EvSCbmYqsV54REIJOuQ7I9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=Fi86H5jDBPlGPXAbMeVicnP5SzLbadgt7iWEHkcEBGf3Zr439X5syxI9X1LKX3MPaXb67uJUvdO9Oi8oTonqKAOQVnVz57NnY9zlOoYNtpO_N1YoRTn62oNT77NHztQE__rU0p9hpdyozavpVxBUCcEg22WLQf3eEU5atcKDwc77JHitMt-iIMvjfk-dsbLMkcfplBPl9JsCuWbPO3y4d9L37UN9j4gN22YNREUw_NLPShY7CuMaSPvDIP2W4x7E7ZGB8JFsjvt1QdUosRoU9Fa1JmCup_55eBX_7Kj_5HJA-eaIkx6f1aaytIs3uU3EvSCbmYqsV54REIJOuQ7I9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/76778" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/555882678d.mp4?token=WWJeR_JFG7oU3C2vsZk_U9YqKkN0crv62rmK2URWnzow3EiTkFE97tTlgJhoY3eTRZxNfKO69coAl1sEc0IoqfSpgmac_BDKwYDN8wxboRPjB-JVk3XPyxGSdNAfM8YTMxA_6_O2vnGqjj9ubuwbaAWvVn5wvaBEzSmw-xJ4HfvbEasf1DxIkFQ9EnhHo23OpZ8bFqnL9SFVIKeetIQjAxp48pGq-KxIQV6AUPoBsesqagzbWdVDig7pD9Ifnatg7Xd7xM8Rm2iTA7KF24XSnOKqQYH8IR2in66zE9Md2jdg_Pi2tVr2kxEwPrLx0eZonk0iRc08TX5tg6yXW8brOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/555882678d.mp4?token=WWJeR_JFG7oU3C2vsZk_U9YqKkN0crv62rmK2URWnzow3EiTkFE97tTlgJhoY3eTRZxNfKO69coAl1sEc0IoqfSpgmac_BDKwYDN8wxboRPjB-JVk3XPyxGSdNAfM8YTMxA_6_O2vnGqjj9ubuwbaAWvVn5wvaBEzSmw-xJ4HfvbEasf1DxIkFQ9EnhHo23OpZ8bFqnL9SFVIKeetIQjAxp48pGq-KxIQV6AUPoBsesqagzbWdVDig7pD9Ifnatg7Xd7xM8Rm2iTA7KF24XSnOKqQYH8IR2in66zE9Md2jdg_Pi2tVr2kxEwPrLx0eZonk0iRc08TX5tg6yXW8brOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">[بنا بر تصاویر رسانه‌ها، مقام‌های مختلف در گروه‌های چند نفری در مقابل جعبه‌هایی که گفته می‌شود بقایای علی خامنه‌ای و تعدادی از اعضای خانواده‌اش در آن‌ها قرار دارند حاضر می‌شوند.]
رهبر ترکمنستان، روسای جمهور عراق، تاجیکستان، گرجستان، نخست وزیران پاکستان، ارمنستان، روسای مجلس جمهوری آذربایجان، عمان، قطر، عراق، ازبکستان، قرقیزستان، بنگلادش، مصر، وزراری خارجه نیکاراگوئه و کنگو و معاون رئیس شورای امنیت روسیه، رئیس اقلیم کردستان عراق، به همراه هیئتی از طالبان افغانستان و شبه‌نظامیان مورد حمایت ایران در عراق، یمن و لبنان و همچنین دبیرکل جهاد اسلامی فلسطین در مراسم ادای احترام شرکت کردند.
از نکات قابل توجه عدم حضور مقام بلندمرتبه‌ای از کشورهایی مانند چین، روسیه و ترکیه به عنوان حامیان جمهوری اسلامی ایران در این مراسم بود.
تاکنون تصویری از اعضای خانواده علی خامنه‌ای به جز هادی خامنه‌ای، یکی از برادرانش، در این مراسم منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 501K · <a href="https://t.me/VahidOnline/76777" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3rZczCMs2Brn2nLWBWT5zyz8BLEvCTufoEJJxMPZqmTUfHG_6Q9BLsZ7pHzqehs_gW4__mJoY2Fe6dJSFBEnCJDlUfsTHTqZvh_8L0KvqjUzyp4A76phStkKoprR1NRjL684MnPxNhD5NHsu-C79jrcvEtoP2XnzLhz8ZW-pLEOJEVvf3mhC8dAehQRFA3wQGKbYMTWkPlEd1tEYDIkgYYQ1_jEd62mSS60BKPbGdf6zHoptFQIitob_FYn52UkICCQnBsbZAzAPCc2xPvyGB8--YTNx6H4MjVmp-CWletWu78CqSbLUFbqfL0QksEupraNGUfCSWCF5rTLSLb3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سایت هرانا الهام زراعت‌پیشه، وکیل دادگستری، از سوی شعبه اول دادگاه انقلاب شیراز به شش سال حبس، دو سال ممنوعیت خروج از کشور و ابطال گذرنامه محکوم شده است.
بر اساس این گزارش، شعبه اول دادگاه انقلاب شیراز الهام زراعت‌پیشه را به اتهام «اجتماع و تبانی علیه امنیت ملی» به پنج سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم کرده است.
این دادگاه همچنین او را به مدت دو سال از خروج از کشور منع و گذرنامه‌اش را باطل کرده است.
الهام زراعت‌پیشه ۱۴ اردیبهشت ۱۴۰۵ در محدوده دادسرای اجرای احکام شیراز بازداشت شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76776" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHCSewXGk8MnFHEk2fva5m9xhLVTQeLlK3pSUmr8EiV-uwBpKGyQfjaOh2OA-IujCgJBHZ6_0CnVfo39OXsqAMWvfVBwhyEd90ofe3kAwCpUKl09pBKmdEBOrzLrVSPvq9k0qLxIuVr9pKZ6NboXg8pjBPMDpc_RI5MLhtQ9jYul0BxeRc9U3BXAyxrboRNfp3wqGqu-K5TiEAX1kZJfmebTFeGMRCGOz9R9Bg1QxmyhvsPqprgol4iHrF5h2z08dW1b1O68MIOe_Cm-P1xbza34Hfat_fejIpLRIzceu6miUF0oXhzndTvabcwOJXwGbzLJBgyuliApf90Reku1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فلاحی، زندانی سیاسی ۲۴ ساله محبوس در زندان اوین، از سوی شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، به اتهام «بغی» به اعدام محکوم شده است.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، با اعلام این خبر نوشت حکم اعدام فلاحی بر اساس ماده ۲۸۷ قانون مجازات اسلامی و با استناد به اتهام «بغی از طریق عضویت در گروه‌های مخالف نظام و اقدام مسلحانه» صادر شده است.
ارغوان فلاحی در جریان پرونده‌ای بازداشت شد که چند متهم سیاسی دیگر نیز در آن حضور دارند. نهادهای امنیتی جمهوری اسلامی او را به عضویت در گروه‌های مخالف حکومت متهم کرده‌اند.
منابع حقوق بشری می‌گویند او این اتهام‌ها را رد کرده و روند رسیدگی به پرونده‌اش با محدودیت در دسترسی به وکیل و برگزاری جلسات غیرعلنی دادگاه همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/76775" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XUZXqengZGnPmO5XnSiKQaJRK5LRobEctIRFEa0WdknJtzkVx0BdN2ok0YUTxlj45eKvwMBs8P7kUQ99VVS3QA3BosssQRb1cZ1lZN9cWslNoBdMmeB9hPcug0qTKMyVTxzEwws0ll7f0jT1hC8SuFhfFYSp23DSc9xKr2bS-QYpXpfWqYefOZerJU29kAb0huSkyReOGIm-YP-RSs4rJ5DkzbG5NoO7Uf6WqmHIZ1fzIv-uhgZaOnldBgbnvUVOjB8VkICwI0tiKt-nSJyNEcBPOCiB9A378UDa_lJR75RqF5euc_Hdgo8LobaNz5i3gAcpv9QNDHD7UmhHJNXIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد جمعه ۱۲ تیرماه در گفتگو با شبکه سی‌ان‌بی‌سی گفت جمهوری اسلامی از نظر نظامی «کاملا شکست خورده» و مذاکرات میان تهران و واشینگتن ادامه دارد. او افزود: «فکر می‌کنم آن‌ها تقریبا با همه چیزهایی که ما نیاز داریم موافقت کرده‌اند» و ابراز امیدواری کرد این مذاکرات به نتیجه برسد.
ترامپ با مقایسه وضعیت کنونی با جنگ‌های گذشته آمریکا گفت برخلاف جنگ ویتنام، افغانستان و کره که سال‌ها ادامه داشتند، در چهار ماه نخست دولتش توانسته جمهوری اسلامی را از نظر نظامی شکست دهد. او گفت: «آن‌ها کاملا از نظر نظامی شکست خورده‌اند. هنوز چند موشک برایشان باقی مانده، اما اگر لازم باشد آن‌ها را هم از بین می‌بریم.»
رئیس‌جمهوری آمریکا همچنین گفت هفته گذشته پس از آنکه جمهوری اسلامی یک پهپاد را به سمت یک کشتی فرستاد، نیروهای آمریکایی سه بار مواضع آن را هدف قرار دادند و هفته پیش از آن نیز دو شب پیاپی حملات مشابهی انجام دادند. او افزود این عملیات‌ها هم‌زمان با ادامه مذاکرات انجام شده است.
ترامپ در بخش دیگری از سخنانش گفت آمریکا با استفاده از نیروی دریایی خود «دیوار فولادی» در اطراف ایران ایجاد کرده و «حتی یک کشتی هم نتوانست به ایران برسد.» او ادامه داد حکومت ایران با تورم ۳۰۰ درصدی، کاهش شدید درآمد و کمبود مواد غذایی روبه‌رو است و در صورت دستیابی به توافق، آمریکا می‌تواند گندم، ذرت و سویا را از طریق کشاورزان آمریکایی در اختیار ایران قرار دهد.
رئیس‌جمهوری آمریکا همچنین گفت «قدرت و جسارت» جمهوری اسلامی از بین رفته و با انتقاد از گزارشی در روزنامه نیویورک تایمز که نوشته بود ایران نسبت به چهار ماه قبل در موقعیت بهتری قرار دارد، افزود: «توان نظامی آن‌ها از بین رفته، رهبرانشان از میان برداشته شده‌اند، فرماندهان رده دوم و حتی برخی فرماندهان رده سوم از بین رفته‌اند، بنابراین نمی‌توان گفت امروز در وضعیت بهتری قرار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/76774" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gli4RufzxsQS17_rhpJJstODBN4Tzto8B65kcQkC_LRfJyexJn9oYB_9t2lLtNhZ8ifbZ9T45yDIOxwuu-wUD4GKuMqSO9-HjDgApPoiZ3ZN6aSDhmSSdGjWA-sOF0s182R6kljk6DuYsoVBr8BA6f5bUmqwh3eDOaP4hu82oSjwRikCanb27M8NEWOrXwgwyEEigKlszjjhe6tiOsQ6o_HnFERfegz-Zbtg_a17RFD0w8T7t3RHCkYMoOACKDlXX_8hxir7Cb4C5MPYqLf7iUmaDCodoWZVK3ZSHrh_z1BB30fOxIey-ywMOWL21_YUvCR_VQlYPLkIqjoLXneLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fw-R_-n6aZUe2tmePIxZn0agjcriWZjSv8KAgkkUlZv8pvJXjwq8aTGfGZxgSXia6nKuq7aeReurlyYU3l6ewtPVpzS9ywSHUm0iAg4WCIvEWQIKKVHOAtRVgk5dnsoEOqD2WIATsWD1BmeLFTgisDHEoxGTSj2IJx3aNJjbPi9ymH7Iu2CBxBRQB-o1jKb238auKCymsYJneWOCJvIgyc5LsMTB0WgaherD9BN8qFWj58O1SEZlrd7IKKu8n3PE5zLShnB6wQwd6fMlN3fdHpDpSWjgcADmZEAy2Vn3f8Jl2FAzxuqEDZyag0Dc0V7evWyAz0AbP1tORK1Z7HOOBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی کرابی (برسام) شامگاه ۲۱ دی‌ماه ۱۴۰۴ در منطقه سلسبیل تهران هدف شلیک مستقیم قرار گرفت و به کما رفت.
این جوان ۳۰ ساله که متولد سبزوار بود، بر اثر اصابت گلوله دچار مرگ مغزی شد و پس از یک هفته، در ۲۹ دی‌ماه ۱۴۰۴، در بیمارستان امام حسین تهران جان باخت.
پیکر او برای خاکسپاری به سبزوار منتقل شد.
ایران‌وایر مطلع شده است که به دلیل نقش بستن عنوان «جاویدنام» بر سنگ مزار او، مسئولان بنیاد شهید خانواده‌اش را تحت فشار قرار دادند تا این عنوان را به «شهید» تغییر دهند.
پس از آن‌که خانواده از پذیرش این خواسته خودداری کردند، سنگ مزار مجتبی کرابی (برسام) شکسته شد.
خانواده او نیز تصمیم گرفتند تا «روز آزادی» سنگی بر مزار این جوان کشته‌شده نگذارند.
مجتبی کرابی مربی بدنسازی، ورزشکار رشته فیتنس و داور رسمی پاورلیفتینگ بود.
یک منبع نزدیک به خانواده او به ایران‌وایر گفت: «مجتبی چند سال در کنار دایی‌اش، روح‌الله نصیری، از ورزشکاران نام‌آشنای خراسان رضوی، به‌صورت تجربی و آکادمیک آموزش دید و با تلاش و پشتکار توانست به‌عنوان مربی و داور رسمی پاورلیفتینگ، با مدرک معتبر، فعالیت حرفه‌ای خود را آغاز کند.»
او از هواداران تیم پرسپولیس بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=SKA5VAjPqW-L8cWZiWJNRxx9xqj2FjPOQBm025oZonN70lcjXNrVtGzea-pNgIrnkK66EzUQu_JDjP6LsCKlnAluIp1KXiYSw8gSE8ZffPdekKELCYJnpoPWDZmH3JsnkSADEuiyTGPO9ut9yo4_-E-Av_NtW_ReJ6T9Xt1j4sZJfj0LPoZVIiDN04zzcahYHvA1k7uGSBihyAhCzPYDEAb8Tfxdp9VCPuoc79XQBT4nMFDyz-csWkPjJQUPlhhz7RpGgmJXbRiKn_QdK7ubV7VPAsuPAS5lN_Jo4MGpz4pJhwj70mMNUAAG8pdTgr6_75Y_F8HfDu67jT2uD6UV-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=SKA5VAjPqW-L8cWZiWJNRxx9xqj2FjPOQBm025oZonN70lcjXNrVtGzea-pNgIrnkK66EzUQu_JDjP6LsCKlnAluIp1KXiYSw8gSE8ZffPdekKELCYJnpoPWDZmH3JsnkSADEuiyTGPO9ut9yo4_-E-Av_NtW_ReJ6T9Xt1j4sZJfj0LPoZVIiDN04zzcahYHvA1k7uGSBihyAhCzPYDEAb8Tfxdp9VCPuoc79XQBT4nMFDyz-csWkPjJQUPlhhz7RpGgmJXbRiKn_QdK7ubV7VPAsuPAS5lN_Jo4MGpz4pJhwj70mMNUAAG8pdTgr6_75Y_F8HfDu67jT2uD6UV-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I0awiof4_Wml4HtiDmVOqYnp6WEI3THga6fRMxlIRIXOH2TG-oWS_9BSykoHz3GGw1U8pUGTDGkubdbhqkBMvphrEFX6qqNRVCs7XTy95ImAvi2KHuazrFLMW_SJpwh_u_SkXslIiaX4fdVz1OzVRSNStXwhVir0GkWPSZMBSBaNK1IRE0JvAq6oSZdFhfDN3h672YeYLZejMNoQhuSaajHSh-L8_etcS1i_5uC7IBQe9oJsm0JqNTc-4zgkrswv5m9pDjL5TjnzrkevFosqxCKaul9Z3TVWoHUrAgRU1-WLtqOuT9voTItUCtymUXhBlozVJRWGYKU1YNeR8RHhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HM-C_bVKKH9BRiozKpszemA9_5tkrAAGmHSKpwi5l-0QBg9a62f_f5SJKsiXh3N5Aeu1oBOIEsTw34OpTCOJr835y4dqSbc4xG0Ej18nVeg_vZKQXF9EkdRrrwSym6db3oNs9v6Xj7vX0SBEa7twSm9xVG1N2P7FVhKbrt6-qKF-sqFfN3Kza0R_iKy8iReqU6a4LWeCXtEs2KJHywnygilXmUrpI-rdS2uCQ_RJgiv6umsYskMPkoKV414qK7Jbo4NX55nX8phEuwgdQU8It884MtDgOrdtAL9UVcbLLFNsrVD-cH60dGkIINJJFofDTPokHGPQLe1TRCHRANxq6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع امنیتی عراق از وقوع یک حملۀ پهپادی به اردوگاه گروه‌های کرد مخالف جمهوری اسلامی در منطقۀ کوی‌سنجاق در شرق اربیل خبر می‌دهند.
هنوز جزئیاتی از این حادثه منتشر نشده، اما طی روزهای اخیر چند عضو سپاه پاسداران و نیروی انتظامی جمهوری اسلامی در استان‌های غربی ایران از جمله کردستان هدف حملاتی قرار گرفته و کشته یا زخمی شده بوده‌اند. یک گروه مسلح کرد هم مسئولیت برخی از این حملات را بر عهده گرفته بود.
مقام‌های امنیتی جمهوری اسلامی طی روزهای اخیر، بار دیگر از مقام‌های عراق و اقلیم کردستان خواسته بودند که به حضور گروه‌های کرد مسلح مخالف جمهوری اسلامی در خاک اقلیم کردستان پایان دهند.
سپاه پاسداران طی ماه‌های اخیر بارها با موشک و پهپاد به پایگاه‌های گروه‌های کرد در اقلیم کردستان و عمدتاً در اطراف اربیل حمله کرده است.
در همین حال خبرگزاری فارس به نقل از «منابع محلی» از وقوع چندین انفجار در اربیل و سلیمانیه، و از جمله هدف قرار گرفتن مقر «حزب آزادی» با موشک بالستیک خبر داده است.
@
VahidHeadline
درگیری‌های مسلحانه میان نیروهای سپاه پاسداران و گروه‌های مسلح مخالف جمهوری اسلامی در اطراف شهرهای سردشت و پیرانشهر، شامگاه چهارشنبه ۱۰ تیر و بامداد پنج‌شنبه ۱۱ تیر، ادامه یافت و به کشته شدن چندین نفر انجامید.
سازمان‌ حقوق بشری هانا اعلام کرد این درگیری‌ها در مناطق مرزی آذربایجان غربی رخ داده است.
رسانه‌های نزدیک به حزب دموکرات کردستان ایران نیز اعلام کردند در جریان درگیری عصر چهارشنبه در نزدیکی روستای «قزقاپان» در اطراف پیرانشهر، پنج عضو این حزب کشته شدند.
خبرگزاری فارس، نزدیک به سپاه پاسداران، بدون ارائه جزئیات اعلام کرد شش عضو حزب دموکرات کردستان ایران در این درگیری‌ها کشته شده‌اند.
کانال تلگرامی صابرین‌نیوز، نزدیک به نهادهای امنیتی جمهوری اسلامی، نیز مدعی شد در دو درگیری جداگانه، ۱۱ نفر از اعضای گروه‌های مسلح مخالف جمهوری اسلامی کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76769" target="_blank">📅 16:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fjd8bMkgIrpxove0kypy5nd85vqjzSyeMFkMEHeKOchWsMOCNx2Z3ZV9SrKPcc5OYK67lxakyY4DR0S_pZqrGCU5y0pqhBYPC3RuxS0cUqTwEcpNBo4FkG3M8CmbIxFvFlYe_vqEtcjV7hugB3dpg3BqJJuqFvCq2HF2EaZ3EFckPL-K6Pfivi1wb_SBOlfGQp7loGqTYf3QEfzYkdjYxvVuuj-hdp3nNyDF7twUM3BzmIa62k_Ay5mlBsuNymgODRdC4p13qukRflHygZ7qpqKrT9mFA4V_uXwhlenDx75TYbc-8IVOcJNG9Cs7qWyHtdCFN1Or0Bm60aTExyjYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت کرمانی، وکیل دادگستری، از بازداشت دوبارهٔ سپیده کاشانی و هومن جوکار، دو فعال محیط زیست که پیشتر سال‌ها در زندان بودند، خبر داد.
آقای کرمانی به وب‌سایت «امتداد» گفت مأموران امنیتی عصر روز چهارشنبه دهم تیرماه با حضور در منزل این زوج، ضمن ضبط تمام وسایل الکترونیکی، آن‌ها را بازداشت کردند.
به گفته این وکیل دادگستری، نیروهای امنیتی همچنین سیما کاشانی، خواهر سپیده کاشانی را نیز بازداشت کرده‌اند.
او افزود تاکنون مشخص نیست این افراد توسط کدام نهاد امنیتی بازداشت شده‌اند و با توجه به تعطیلات پیش‌رو و بسته بودن مراکز قضایی، نگرانی خانواده‌های آن‌ها افزایش یافته است.
از دلایل بازداشت این زوج گزارشی منتشر نشده است.
سپیده کاشانی و هومن جوکار از اعضای مؤسسه «حیات وحش پارسیان» هستند که به همراه چند فعال دیگر محیط زیست زمستان سال ۱۳۹۶ توسط اطلاعات سپاه بازداشت شدند.
کاووس سیدامامی از بازداشت شدگان این پرونده که تابعیت کانادا را هم داشت، چند روز پس از بازداشت، به طرزی مشکوک در زندان اوین جان خود را از دست داد و مدتی بعد سازمان اطلاعات سپاه پاسداران دیگر فعالان محیط زیست بازداشت شده را به «جاسوسی» و «همکاری با دول متخاصم» متهم کرد.
سپیده کاشانی در طی سال‌های زندان در نامه‌هایی اعلام کرد که در دوره بازداشت تحت «شدیدترین شکنجه‌های روحی و روانی، تهدید به شکنجه فیزیکی و تهدیدهای جنسی» و «تهدید به مرگ» قرار گرفته‌اند.
او در نامه خود نوشته بود که بازجویان این پرونده «ویدئوی جسد» کاووس سید امامی را برای شکنجه به او نشان داده‌اند، و همسرش، هومن جوکار، را برای تهدید و شکنجه به پای چوبه دار ساختگی بردند.
سپیده کاشانی و هومن جوکار پس از سال‌ها زندان، در فروردین ۱۴۰۳ در پی عفو از زندان آزاد شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76768" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=aTsPfQGjmyd2Y7SSjW2IAIcQRtp4p3my0NKR2fpFxG9SWHF_kmKXx8W1jgpgc7HCmbArszCMFIbs-KkAFwBq4gASB7Ke-DzQv3XQflmk5EVo6vA--4zTokH50S31lBuKIK1Iw0IJpr-ecWPNFt1k-TumS2G0lSkqjQpY4xYCxR0DIFWbLX0XkDEnbywObNBkO15P2OYUu1zNQNAlcrSsKG0ns6SNuUKZYPBvSTyXsYoQpxhubCyjmKWl3O0PDZrwVclUEoRJk77zBfiENK5EXT14NXh-3rCiepGurLCEjzA-IrGKwdF9-EIk8oX33gTt6c8r4pTujx_U2Nv8lUCStA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=aTsPfQGjmyd2Y7SSjW2IAIcQRtp4p3my0NKR2fpFxG9SWHF_kmKXx8W1jgpgc7HCmbArszCMFIbs-KkAFwBq4gASB7Ke-DzQv3XQflmk5EVo6vA--4zTokH50S31lBuKIK1Iw0IJpr-ecWPNFt1k-TumS2G0lSkqjQpY4xYCxR0DIFWbLX0XkDEnbywObNBkO15P2OYUu1zNQNAlcrSsKG0ns6SNuUKZYPBvSTyXsYoQpxhubCyjmKWl3O0PDZrwVclUEoRJk77zBfiENK5EXT14NXh-3rCiepGurLCEjzA-IrGKwdF9-EIk8oX33gTt6c8r4pTujx_U2Nv8lUCStA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dz0vxmr4IjE2656EtQWCxGk7iGZzqiAXsoFOtegH6B7gf5yvftfNjren4qJC3UGAOozH0WCjnmgsbLQ4SWx8T1eDw6Ah3XuGspLkXjxrc19mX4LsPmX7_2f728PD-pK14XVnqzW1SdHuPX7aVUV4Zf6fTQ8wbqWF2p_k6ZosZluUN9375xb6GmXT67WXmtSctdeHQX6cIh_FYGnUvUCfhZQwIIw4a9mB7NnJqE-VDc7u4FzksNUqHIN_h9SYqSzFrcY_LMilLme-qcLpOj8VNU8Ieex3cVAXkBbH_ZaWJGhpFjoR2_S7a3IWFwk6-m54QhGuu06yL1X3w-aMTKulIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nAnqHbtlNuqaVmBz1WtLoVTI6Lmjckkcyjr5Fn_2s2vPx5LnFkR4iWyM4s-O5-KUgjD1hHN0LRXonJgQY76k-KL3eglWLboZoai6AwiNrhm1LehCE9L9ELYAPMWjv8_-Cgt-wg2YtfPniENAMUJkud-YiU2yY3QvGpZD7Bn9QRqPx5InsISH7DV0td5XWTok2K7R66lU54HFcsk_hJV8T02cEG5VCiGZkb3GOaWhm06Jym7o1G_lXdoeh23W1RCcVzeAKpPHnjw0p8KppDC2oZuoFTrVwugSQ5rq9jS-g62RLfJB7jC-BnCbTj1tg97UT1QHVMauN9HE9MSeWGAZkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A4h5vV4WGCwxkd8C5wRG6RDcBTCXPgx5CcrSC7aRZz0ebtS7EFUbf1vrohSidGCCn-OSQYO1jDb40UnRbmfOmsft_kNj8VMO7BnbEaIYKN8mp8ByVo9-F8Na6xZWHzlZcn44e2YueBRtqjh8QUDAsCR69yvfBwz6HqO3WrK6RbBdlPlc_-VCiaa6uomQvebFHsaibY0Huo611FhSBfTXVvUpMLJ8n3t7Gc4NHcd0rEF0ETvsn4oAhU6NDqLQKAXfJ_hz0NekVHQTNxqzpTEQdvm6qomo8hZxEH3SmPKsdAws5vRBP56_FKBE-eH0rLYAYk9CRom0G7U9p-19p7zlaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nl9YATwy7MlN1oG8bk4YkuKIKctx8mXspSZx8IcvZR06BpCrfkMJ7u17LYoImgA-Zp4JG1sXwHxBfXw8U_tWD3DnkEe8Kbh8o5rWBQbNcNw394vrbGFMOSWEQ13hs005Yxb6GHvDUrHOfq0aU6PVsnDoqhOFvGvTKWxiuotVhdZx_W3-E--FCMDCWxesvq1_R-jKB5YTb5_fzxXSccExiBwdSLfFxD5LtnCdu89g9ywDrj9Je6P7LoEIVIyQBwbySlBFUhJ9XEjxffhTuyWJ9xSV9cnR0t_hEb0fYsDv3Axg7h74gW22g3AvX_I0cO51tmaSRMSWuROylTvzSHsm3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pIXPsRVx20UTYJUa9GAzyNzfefj-eJqJhq8947W-p2-o7MNfwgr2wvneppz-G333BO_l5qbzTch6jV38h3qDpnnMGzW95UNQi5VdJRtl5dUdNsnzOklxfkYFR912UAmFWEhX79ghzjAG9pFWvdnOCX63oxonKC27J2HZKjlwlc4HQWna77oDKl8F3dhWHvgAJkn2BtHRU-VnDMnCvVoPT5bUAlgU3b04gM3S1ejMF5cEv7hA7fHzpLCOt_Gmzv_a92o503hv907s6JebC9xoexF2HC92tGXBaS76BYoAQNj9MzGSuvmEARGLaoBvbGtcj4PNjhm8NgptNLWfK4r7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fp_TSdCXgaGQ1Jh_Tvv-jvdwW2dmnGpX3dfgcz4-5vN5KAcAUDjAmSMFopI9pVYKJwRGZ7lycwHrsgXaUrLg3isaWo2gQHACiBk2hK3bnRFkmpQ69a1gXcwTDRVx0ARhxtIpgRaj7TpTxCKTixEEUNoU2CdTiHXV0h-AZMkeb_GELuav7MdjsxGuWZqTjyVf3QeNF4dAvGJONN7hubcXR_nsqu6z9NuzHqtq3bJS47XHr3BePCU_eiMybjWcspofR6QEPZy1NHm3XpEokEuZv8azsddxsdT9nh9lWYoiObJsT-o2rLE5zBFa5iz83gZ9GH2q_jufTWBC9CmCO1zStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=rbCxl1_TDlECwS_7Qha84rdJ0-0ZiKSwjH_fvqmTroSZWsFwYSWA2sFOeJ97whpiDNXhLUOSdN57QHIoygQVx7B-t372GZFOd85rB1HDegoIhb2l7nLTsr4kPCUddYN6pDHnMF2dUaCxfEhPpAJav4PJ78RTU5_mq6Qx2_C6ld7EByH4krhfsNsmom23-AHrVlyXSgNONJyr8FRzGcnqe8N07JeGHquyLB2KOOV5kijJ5s1DWrpVuCLtlzEbmuy6l7ETm9sQqavIgI6KkZpiO0-UziwDU34UKuGfRA7FGOp7VPwTs7Z2R75qARxm6oKyMp8ZfFJ2RBaWMrO4D3_38g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=rbCxl1_TDlECwS_7Qha84rdJ0-0ZiKSwjH_fvqmTroSZWsFwYSWA2sFOeJ97whpiDNXhLUOSdN57QHIoygQVx7B-t372GZFOd85rB1HDegoIhb2l7nLTsr4kPCUddYN6pDHnMF2dUaCxfEhPpAJav4PJ78RTU5_mq6Qx2_C6ld7EByH4krhfsNsmom23-AHrVlyXSgNONJyr8FRzGcnqe8N07JeGHquyLB2KOOV5kijJ5s1DWrpVuCLtlzEbmuy6l7ETm9sQqavIgI6KkZpiO0-UziwDU34UKuGfRA7FGOp7VPwTs7Z2R75qARxm6oKyMp8ZfFJ2RBaWMrO4D3_38g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FksRNvWiEhDOWCVnHWVEyF0CilZic0kImnfScCUPaDsD1lCIA07Ozan0bJgeuABua2z1UWDI3mCnLTZTnS7GoRuZQLDIAxCDG8kMttHIaIcdd0THJEoPgxrZZDdXO9Y5400G4tF0u1QTcBB7aiGgjf_YuAu40W_mUEWVQdLQsnLklwbKciHDM7Zm77-qUpEdjTIBoxfFXzFL9zdINOLT34qoilphBXic5H_Z-sUQ9G4ZzfAewoPf8kU7p73i4d737g1cwRvTUAhShlcot_1wAS5kZhKZnMPAGZh-NN2p8sw0D4Xc-86AN1ubkdN_1vnaPKOSxJOYecI-inxImzsrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJwb42aYK7vCuFz7MZwTBv12iNtdDJDZ71cGb4OawKkHO0OlwfcWV6YtfSn6cf8yxmwLhHCpsvJ5-roZ2Ka9L5aLy1x6H6BwxmaVlZqDQyMQcE-JFsnTCwf9L1cTHNk8Ho7xxvn769pFfZHLh5qIBoUS7b5arRWFeJ5oNVFfiQtvw-fBOnS-t-TS4Jl3u5kNLvQ9qknVhx1O46QIjE68RGc4OKMcbX3fG8ccV0PypZkxsFRj3vEdfWh4ph6SnT9N5RY3avs2o0KAbCGEnFHjmReQq9YkbM626shG3sZ_37AM0HD7gSDiquOrDb7GewVpUe9US1hTkgwO-rJHz9j0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgdTzwQwluJ7UAnPvR5RyQAZNMkSDwxpxdf2i-ZOBPRJsVQRDMnH2CDF7QLEZMAbs4KHeQvK75lj3fR9FiYOVGgg58GipMRTAx8c9C4DA9rNxyxhT-RuABKV1e07137tJ_FQpRVWJge9SV4lM9U5oBscSLsFkcxi6N_aO4N0Ea-3evCcCd2Dy_iho-mUeWIh6u637cZoy0K-uwCvoM3EjwpedfI60zoPeLjoGc0JVqAhItnk1TuUwkrG69unGhwAIR8_HT7ZMaXs_HuVQlq6e-fu8uZRb_Ey1uxsaEKaD15HwlkJZruKAuyNeQULaCDWSaYFa8ut2e8b0PmObmhagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tidZtPRykfwyKBzRFlUZ2HLQyPY3vuGPaORQfxFQwfWQ-ghlSj6sTxPHKaHdsL33kKq41QeLaZYfs1uiHWkjpcc-4CG7SM420jM1rG98daixoqpOpz7Cah4SvkUR_FOBxvhAQq0fbMw8w9rkXQaCNmJA4MG7-i9r3bOIFL-gjtLxcb3nbyKk8Z3NzbB1pEI25UieNNw285rI3usPdqfA3lf_l5YWndDq2bihzIUPtgRm5KpeWTNkNxUaAqFSRNH8mQVZAXGso3O2fQK4NpZRNYDNro2R3rZfxjoYJRIWOqz6hBoFhP1QXPtN_Yfs44gtkO8K9I22oDgk8uxz2iz2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EKn8F7rzBCLNrX69ae6Ibc5lUOquCPuW25GIOz_LokRZPpSRaSaNhf585kWmiBWNkRmkrDbCVhcolnIt5tP7clmSoK_-lB6NC_4_pWFzMJi0DNQX8Mqqaef_gTRGKRqTQLpl5UuQxwjUaUKb01K94zaGqwCcDzRcJN5HkOJvEtlHZwi3CeH78xZNFNZQmgU1hOgereH1xTm4nkyAHhTozUjMmp1vNroS_00zUt39GoWhfZmvafW7YH7rcfqM3naEnXM8WJopVT13N7vfqBzwsxJrWwI9ppd3PcrpDlDuhixMGkP7hrvXvvBFihFsZPuiZQpj0tgyaT9im-RN2ADjYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De-K8BbLKaL_oXL-WgCD7HXBQz_jVy6KLEnL2IIkDuwr8F5_DPGbNOirpGBN3k1393tegx2_WkMz3JXDzxmeXvQMBygmZO6L5xEjy3iWtbVFiBL0WK62o6d2KAagVvo0wUHQHvdGTdNEQ61AsKYji-kO1S3OE6k3i7VHY9cIRNDC3Vf04IeEJop_S8urt7g1QYlvWvkZdOzTM19i-RXinP7b7soRDQTZkbCd-vgi_t5_BkzuvsQ8LnuUjtlfM-C5KBgMZwN8qp4nsehWVdB_BMjGC7RnsOe2CtV-IjEWK0dQ3c8fYoLVQ0RlY69RxRlqqw6Am8WNzxqMoLkwxhNDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMJK88Vzohq8pVfFAJ86gRMaDqHJSZmS8L7yHj7wvS4GxzGz55fTFdEk2xhVsqototbXuBWqY5jTRbOH0QG2pvJTUiDwquiI39-UoGzotmOyicrrriVj-QWfJaleWrkSsUfg9le6otVC24Iw9lD7FBB8sE7QIB1VqqmbF2RYYsNp0T_wwSyTikZXKPVCYpedloo6QLcnQ3Qkfua4iy2y7ghFKkBKhgVdG0l7RW7az9gIHsKByatF-1VLq5lbFCYQbaPNSPpG_TnM_5vG7HzGBB607oyoLZh7R3OMFVbeBk81zW03PX5SUrn0CW7MqFKbOlgM5CmIoVUzzhiV1xjLGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCnDDXKRZpiRPrE61a1EvxG5F223iFe_sZMxqiiu8JOG3Zj04MFmSEvc7DS-OH0bJo-rcHqkCWBoVJhsxMqDpgjhKYAog_MpEZuq1q1p20JdNyoKus9TqVfpOp7qxQ-yk_J2jKbv1kWcwRJ_w_PqIMgAHitDasjTPjCL0WkP07U5j1eLBZeXIH2Oy2FqoIj7Dnc2iYc9ZBzkW-AQZrDqur5eBXKxooJG331Q60Q-t1FV9cc1JRXTVpanzWlgCPVXZmD09zdQHVQoDXnovXrP7b1TF5WFYvYfcivpVlE6zaUJy4fQH9t_SB1QfjtPgFVex4188ioN4JFbgct42Y_4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CA6Th49ki10BI5vhKzfOJMm3ftdReCXCesaU2bGifWdbxHNLf75TogBVhNhZPy8WuFyzcl1xYSeNGGJ7ZCYP7fOkajAKH8Ow_4aq8WyXtoQP6jbuR8m0NmkwRiP8E-rKlvrPqoRhW2xRdj21iGZAAY1gv7BoHjw3aH0oXV8hB99OSdW5UjtDahsFDS2p_sJo4hmX7AUXRwt0Wwl-sG7kTZWpUWNZvOWQ7FAfJaKfPEnFcoQNw6X53cS1u7FEz5YnC-eCfEqtUAm-b2oRYGZaVkSGcrJC5CHEgVHPPX1OlKX-cEaL-OcyzkESOM7RyP5iDWeViwJKAJZ195xDSrNIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbYZtIJ-POrYmXZdh_HccDlwtZDdM8tkv6tYp0wrNWJahH5NC3ZBhZRUAB-ZGxYFBbg06odLPASOoAZ5SCB95ASTgdDL8gD9UaBsOFroNrS1SbOq1N735YiGeJRO994OMEKmKi0geZZuPTW30h38ykCyqUGfQEttNLx6HSGCmzK_J93AsasgKzrGkgZwa3hd66KX6bz0eMpTtY1UJ_BrWevIMDooutY88VVJ71rOj747q02pC_cdkBCsIlpd2Plt6I-EgEMfOKgVwhLz4QhZ9xi3s5wrHCJbo5DXJ7hkeuCQASZzk5Xk5iB0kTuT4uOkMkNm6rDTUYbEzJmM-DOHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTb4wyKCrdDXRCI8lAEx21qF_pbq-x6oKQA9zun6YweLZ0GEKQh75HVNqsUokvrUdHbAbQ_yQqbHrhF1V5oej3SrTLOYSqohkCd41niCfUbBqhZ2O20aHeVi_LUkwzDGD7W3RJH3IRchsADinRWbzpDj91I3Gn2nWtAsZEo6EHGl5yB0Bi0jWxDJx9MopfAFnepsH_9yEzAXiX9SEnZDPwVXuBZixP_IfGJR-RYY9zhMMEYdw6qPLyeudTsfyV6M8t9JEkNpEllQ0PF6Eahfh5VXjZohorbQvealjfDBdK9PiAlDWbth2e9e8xSyRxcmIoMSMX00z6Vfu9aCihGkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uGi8Mplmr01-3S1PsL8QzUbeSgf7f-L0KHa3QZomB0hgJyTqsi4NPW2l_9v5YfGB245JKj4PerohhmYR8tXm5GGDKVR_ZPm7ojlTdVBHJqBDnqv08K2htt-5zCEZGlA-nEtFrlk7IMB_KbS4jepSiEDKA8azcRQ1x1ZLHdGbzSCHrkWpsfyWF4Ni3AS1hgNUo6K40ICgBul-_6kToHsvKdRArWxHa0w6gcTjc-xwfuQwVJtWq_cRVFw-7i4pW0CpzhHdY1Q1-mUn23CWE2-duoVympTdjl7mNR5AOgod3GPO56Lm_Kbzn6__Cj4ssa18SdhLJ6Dtr8hxYH4Eg8K0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
