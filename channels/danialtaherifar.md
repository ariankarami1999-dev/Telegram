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
<img src="https://cdn4.telesco.pe/file/NNoWDqeyQ0ufPKb2lsLHm_3uUrhM7J8k8qqAIEz5S-vEyqMo8BtBP6bpbmowRzmbDQI-_fm306GusoLqOIJAIm_DGpbGTVUQ9Zh3aZzZXQNEYreIZod2cIBp6DNnFn48dZ-MII0uK1utIg2rJkZDY4vu1Qu-7bdy1cWCcek3dU1bYPgU7f6r4rcjivTY0m71H3pKaUmDlz0JXpNQ7oRxFBTeIjwG1X-YVBO1fIcTF0fQQHP6uMyJMdn5FJ-DanJte5zffMWPivdRVUyRu8OxBVk2PtrRS6yP4RaEYYbSl3KPKVdL7s2rEMu3iWDEz1YHpzNp-N1KE1srOHMTZhRVfA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📚
۷ ایده از Phil Chen درباره آینده کسب‌وکار در عصر هوش مصنوعی
چند روز پیش رشته‌توییتی از Phil Chen، از اعضای سابق OpenAI، DeepMind و Scale AI، خواندم که به نظرم یکی از ارزشمندترین مطالبی بود که اخیراً درباره آینده کار و کسب‌وکار منتشر شده است.
خلاصه مهم‌ترین ایده‌های آن:
۱.
هر کاری که خروجی آن قابل ارزیابی باشد، دیر یا زود خودکار می‌شود.
بنابراین ارزش انسان به سمت قضاوت، خلاقیت، تصمیم‌گیری در ابهام و اعتمادسازی حرکت می‌کند.
۲.
کمیاب‌ترین منابع آینده پول نیستند.
زمان، اعتبار و روابط واقعی، دارایی‌هایی هستند که به‌سادگی قابل کپی شدن نیستند.
۳.
مهم‌ترین مهارت، انتخاب مسئله درست است.
وقتی هوش مصنوعی می‌تواند بسیاری از مسائل را حل کند، مزیت رقابتی در انتخاب مسئله‌ای است که ارزش حل شدن دارد.
۴.
به‌جای ساخت راه‌حل‌های موقت، سیستم‌های مقیاس‌پذیر بسازید.
هوش مصنوعی سرعت ساخت را بالا برده؛ بنابراین مزیت پایدار از سیستم‌ها به دست می‌آید، نه از ترفندها.
۵.
تمایز واقعی در «آخرین ۱۰ درصد» ساخته می‌شود.
AI پیش‌نویس خوبی تولید می‌کند، اما کیفیت نهایی، سلیقه، جزئیات و استاندارد اجرا همان چیزی است که برند شما را می‌سازد.
۶.
هم فرصت بسازید، هم از فرصت استفاده کنید.
برندسازی، شبکه‌سازی و قرار گرفتن در محیط مناسب، کیفیت فرصت‌ها را افزایش می‌دهد؛ اما اجرای درست است که آن فرصت را به نتیجه تبدیل می‌کند.
۷.
هوش مصنوعی فقط یک ابزار نیست؛ یک طرز فکر است.
هدف صرفاً سریع‌تر کار کردن نیست؛ بلکه ساختن سیستم‌هایی است که بدون وابستگی کامل به شما نیز بتوانند رشد کنند.
جمع‌بندی:
به‌نظر من مهم‌ترین پیام این نوشته این است:
مزیت رقابتی آینده از «کار بیشتر» به دست نمی‌آید؛ از «
اهرم بهتر
» به دست می‌آید.
هوش مصنوعی دیگر یک ابزار جانبی نیست؛ بخشی از معماری هر کسب‌وکار مدرن است.
📖
منبع: رشته‌توییت Phil Chen در X
https://x.com/philhchen/status/2072793818945167475
@danialtaherifar</div>
<div class="tg-footer">👁️ 161 · <a href="https://t.me/danialtaherifar/941" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 433 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh3YbIAc1lcdXRPXjKMr77cY6qo_N1mbNCg6nkIvSrV7xoxnDg1oT23jQj2DaItaZLBgC1txbJ-lZY9AETiaHllviBFJI6SzM6Fdu0-hS_iaaRLxfBn_I9xTwobeJ-8AYqTuvHchQS6Si6aTxNsYVlnw8NJwprkp30I69F5XdVz-QgNKVtNC2X2a7kP6eKY17EN3SG1iQKQ-MzAMGdXFaXr6gH49wpa7lZdcK8HHKu8R8kDTcmLoAoE8N5WHS5TVBl3vVZ85-EAQu7olv_5cPDGAkfnvuKOq1V1rTxvNxTxB4cz6sskI6mmEdgulpX8V_zia2D42H6T7UGR49XuaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 775 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 844 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dScy-XyEv4rMEg41hzhouINVWP9zOq8l4asIYcYE2oTe7U6CrV48BWoKF0DLPfgd7k5ISPLNVPbQ_YSVgf20BsV34q9Z94uI2VlZasUyNLLStUULmtIdFAnkwRZ-GlPbDrXkymhMPZ26YNTLyyw4CVK-Txl1bcx4UPGcc_Wp1l3TEF2AAkCBX2LnZw550C0f5ndWl3_C_EckIge5WVI80Xrzc4mnS07-tRVfKBcsov3WMvQc6CL43CiHjFI7QJ1FDi_nqC7kJ1pfr5oMRYROmE2WBcoW2vGJN7GPuU-Cd1PBG6ZImM8-ABC_8Yh7ii7mKJIYSCAxkdQgY_lauBSBPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dScy-XyEv4rMEg41hzhouINVWP9zOq8l4asIYcYE2oTe7U6CrV48BWoKF0DLPfgd7k5ISPLNVPbQ_YSVgf20BsV34q9Z94uI2VlZasUyNLLStUULmtIdFAnkwRZ-GlPbDrXkymhMPZ26YNTLyyw4CVK-Txl1bcx4UPGcc_Wp1l3TEF2AAkCBX2LnZw550C0f5ndWl3_C_EckIge5WVI80Xrzc4mnS07-tRVfKBcsov3WMvQc6CL43CiHjFI7QJ1FDi_nqC7kJ1pfr5oMRYROmE2WBcoW2vGJN7GPuU-Cd1PBG6ZImM8-ABC_8Yh7ii7mKJIYSCAxkdQgY_lauBSBPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 843 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN5rgsrlE6lRRh6AyKQ6g6-yUjCXxpgcUAMwau_UhFSMmgShgeyU1XHObSd83dKQDsi-KfeYvtb8ZkGnKSq-A0r11Z-Fsil2ZY0Wv85ETrJhIRx9b5MXBqsexZsXjK8rLE4z4YwWM2UKVQ044VFNveb68s6D0Bk3T9EMJ_MIwInSwyxQBSb7zbreWXWzG7ZICp883fjGJDWbo3cfxoaJHBMIWvMrGSe920NJ7oJzTUe3nXixoyW3P4uRjtylttq8WktVWmiQ-P7UNE_xo2SnUPhN7WKoPrYTyasH17k7lxcGMKkUTs0mUc54RFAQ9UN8w0lw96zGfxwM5ZNcY58QhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 695 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 737 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 998 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT_q8wDsGoqkp5q8sP2kyppGLV4f28fghZ5N3rccO3X56c-cLtoMCrckSaw8k9n9Azc31UI2-55GHzVtt4PZByTwrgE3M_5crc1frWgTUmg6vHLKWPN5a6KbqHMUfFHLHThy6ZhFbnafkR31XBEGUZgOUiXcU18UpAhzWkkIHHV1gmLCoe9znKlsimwAENCxnTVYIK-urFFJevzwdIzMcOzyCdH1wX5abHOWszLjM2Ws9VaNsa1jzwsHCWUQKQ1FUV70vCK9GlKoMCBJQ1Z3FzwNMBGmhNl_Z4Iib0AXV09u1CSrJBTo9uZ0Mz87P3dkY_bAblNh1tcXkCpkJsWeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF-uIF6dFP5n7bNeKLgB2oEmVdH_8Fa6fVdn-PoclKhaILoOMj5yP-ZojBeWgC-6AV1L9a6ckGfcpBahrgPjikQRFx-_b4yPhvE4UmS-W0eT21XrZJzJYfyYtUeNCUni0dQNGcp0hTav5MrY_D1UhwwiCrB0rtJxr8m9mQWgfxzC5QI_POHEOBUqfTI6ok5zXS3VckQYbU2jnvLwjoUrXAugM3ho64Y5FW-Vk4Eb-ScAbYaBci4MWFUzz_78bFHh3c_Ho_yi3Vqxhlb2lAK-k9NEB1e6MYnH0t-7mLHAPFhp4q0lgQ9r3TXitswmUYoJB_4RDcm9wuEMJITAhoRw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_Pmojqkcc0DSf_JyMwAZy6DycUGA2RvR0YfTO7kT9OC5juIwToSqTfiYIg7bCP5_3WCsBhbhaQlwecEhcJI_eW4ovZVDquxKUQjrrljUX0JwU6A2LKhCIHj0hNa0rJyE9QL80AKFKZbt11L-pf2ewt6dLpb2biZsssxbR7udDVmdlABnJHAmTQnxYY6Jk9XoJcSF0lCT-yfcAH7HZ6I-hHms6wHF4vAxxR_PILzT9_r9WfMpGbAlU95WkWrI2UkqsB_0dqWwkuoCO3f0Xt8jWz_UQN1HaLZxHQBu9ZvgBPmGqH_RkCUdsWVyh5_ZfC5z2acquScRKI_QpGgZbcP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f654NuEOPBEFT1VGM3w9sxkpnH1I12KuW6UBJbGggZu6TfxJ4qnBU89Hf4tjsHt7zeeXrSjB7Bun2zejMD5JU9oaGJ_BDE5mjD48saIDU11M4vVx08W320-9Owycau58NB-dHlHuENh0N4_iKJPRvRFRD_1zanklagHwOHbVmfNlHclH7vlIXs8JGBbVwet_wna98EmJ_itu6Axa6zEZQDtY8hwGDW5tt8Z7Yvwm1dkkheIxEdMuribMCQSkOY0dH1Lf4GEgK1JqJjpTJUFxKa3T4KAToZXbDxQT1i1Ou-zkRJCSw03lzBw417EZ-sBaTNkZyMSDjLSWQD3-wC8Z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiSlMYt3EhTHihhn8Yw6zZ1t3pWZLZEvvX4ZcwSgBqju_s3q-Iv11JS9y08uRiEk9llCvA4oG6iXwNLKuE0Cc7F6ry37bw1-aqujWGy6PiayXfAWXk65BNOYVWbWVryOWPryF5xYyyeD_175NfendvDG45QFRlV_8_VeGrTaoxy0lwfsJ_kw1kiL57zulGhM5Z5cmlOXDPGWLWyDomfDe1YHO1eFThGZAsnBLzTDYSvfj2mHM_k88rnr6elNfjopKDLmCoLf3lIxfeszSPirai7MQ-I3gbP980_yNOZahYfIZIrQwLk8IXCKXYkFvuVelzb-A5LK965JMvoCWHfn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oebeHhSs6xZ9vmSqyT09iTgOZZjEK6ThJhrKA67RH9mxOqVGGqTEEJacbQGRmMVNvIPnF9mt62FNnpCSZ7arrqSEu0bHe4WHJRWBQl9vd2WFCrq2kttsrbtJ8rwCDhwzBrvTBeeRS1KxBiDpWt9Ci_e45NvcPoi41SYez0MSHkCU_p3aciYWeD314SoxMFk5CI8akpnJC_t-Xp2rEFcrh65Ixkc3PyRRWYf-ypsyBfdhQQdnSh9rXGXJBXPW94POWNv6coXIvg6VJL3AgwH0rih6Oilhum_8P_ZVPD_cMYk2pdyouq0cXaEcOuip3tfVjndmcSv94YqMqgw5LRBwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTecQw7XxOJjQPxvgHO1xe_YevxjtNTTPAWrHscbg2IOoLmuwJslKdcTbUO7XirkYYd-dB0SDtduFJeFRXriDBFhZ9zXLlCyhXVNFqK-FxtgqeNG_MiVLeRAp47HfYdoqddvASXmiO_hWmxTdQeMf9-ht3ZgEm74GHdQ4Moxl6l4Z5hjg_WJfT6U5_xQzPxzgNlCq0sL99srHnl_eZJ8pFITCTFXiCVtF5BcOEv0oRwNedpfcALMlf5IAVSU0Wfhl1E_jB4Q1eXxLwhEjmD5FVJ0k87HRV6WKiA5bLybuV3eeJ3CuDKGmUFleBe7jNciyBnbgYddDcXBSDMJ4yEcNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACuU-7NR4j84NOPPYTSIXCGfGGHTC0lFe5sA7zgR8wTRfOGZdcjQyWUxnYUN3a84si-HZsVNK9gNl52bpOZfLfLL0Mr_hLrmjWE7r8UvDq55twckUGiVEg3JnnDjgO-tNmbp1GInT9JWO4g4bXwkFmyEJcnEcmy0KUC20fDgnm7x6cet3YyqwxiYu9qcHBxgss71mf6gJM9dI3eIah5Xo_6zOTd4oIzW4XA-t2k7mpXeghUt3rIsqRG6mFQqs1Wve58KTXTmFLpiuZuMbRWGvTKDbmVnk5Hf5078ft_-TUhSO9x7TdvfoX6VrV5bOHqdiB6Q7yScs1xnSnPFNVzlhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2twtrPtHUu9Vg2tFaikoe9eaZUjtitwP6EULcXtNBg-4kIafOsOZKeQmN6cgL4W_JOxTZFAOc2dCK0HzIW3ek9cdVVku0TWlRBOrfpeD5nP3lwizwVmO472Iy75EA_rk0GqLrYc0haIkY_pybW0r6tkrCEIX8XNt3SkpP-sMgzLTmU3aLtTdavt-WLCUWOoZi0-AL7WScH9e5n245nPeF1pbfX9ZFQb13NOrCsdOq9zQJ64-2nG_JwgpJ6gCf_4IrRek0WMSCUH00Z8wnF8eq10vVfpZ_6Qf1ZI24fMqBwWGcfL04jfScMY0_u_0LS3yb2DkxZLnOmrqWF609jS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 843 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCVxwscLuxZeuRWKRaspFZjqz3AAH2rO_6bard2CZDpMXmO6aTj-c7gdw4LWQjIZOBDpKU5wvb9JVm0IV0HOZj-9HeI_xh6SnD1ne1PyaErRkUxrecD0Pr_IGPxNLwh5y9CGPrJoz0hnqqLABBVGpZp7FBD3AapNGMHR0OToBJAvxAU2_TcpVXNxVgUCgKGBHpCaslaSP-mRzwjyNon41Kin3JdFNJBl6acn8mNv0RqXQYf0Hn6anY1QezJ46C6RamRDXOIF-FCgmPJL6iVCf8dK7v_igWX8qg34EC98uAvb50PP-Dcc6B-9A4X03NvJtTXraaAHMo9BvTms27rRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShKuHERNDNFlQ5XrTbbjv6GExw31YTYtNXQJwN6CXDwILuOafvwIi156Arj6oHXHMcAPP4fSo7QYB4k7BsgY6m-4jBp6d1lSmOyPihplSqQK64Yg1AZn0NU41sO1M8m6k1P0ic5MobyG7bHdcGfRRT_23F0-ueJKG8sLO2tV01yNYwC459HMx7sqn1CIPsuqXAMG-AfEwrR5ITxYQaFaR-JIQSNQ-Iafz8iUJqv7aRQs5_IJofXkvyEYvwKUFnYno6bVoFiElbAkSAWo3umqk44kFsHN_qStoQ3dzSHKcW5ODQUu2jywWrAZj4ZtNGH3kFPixquEhirffs2VT2yQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b57Yog7QB0o1P0h14V4ZN0HZHWFusAYCgH-ddp96k4rfXw-TUsLA8yjRgb4mod8_w8oFJS1XzoTiul-B1w68Ib5rjF5V-LAn4Zg6PhHIgfrO6FKG36zD3RTXCFf7J5NRmkoS_Im9t7GOYRlQk-3ESoUY6f4M7qwKNX3iaoFrRDC_Xvlvu_6Peg0PRm7-Y4CXzbAN9n81QkNnvySIX7p7lMFVu0BSjGzhl_yzD8bwYQGugqB7ALy-rOD57Kr_BiU4sj6iihmEQzgGmaGtHy2dUFgcUBIRrcGyNvGu1gPgHQ3eVFRkZ-aJfJmdarL9hAhFNR8Zt7uIDYe7pdOU38OVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tjq2vEY0vXi6g1mxATv3fnRTDWhr1w31GC3D0E9_K5vjQEqaa27rWKwe9c546LbPb4SLrlbeavGIdK2vx3NuiQsfhklF4cgFd-KqRZUnF7mI6qo3ydnCJliRuhQJCUsNeC25reK2bhq7illbPe6V1p5fNq-4I3i8WWEjFiD6Y4I66IvE7NMHw_RG8f_fIiJxtv1dZNT3GdNsNGxjblxUsIoYNhXYwYjUlITubFYJdgjLExTR2AN5w2FlhB9NoelHuiaLKmp-93laBFPFzhldwv8tDXLy2slqzH6tf9P5bjG_ohQIraARCMLIYN1W-EpJOew7-nu7JLqy38YcHfxZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ug3VAoYk8D1vjjglZ6LsaORpqrcmwCTFOLWyUf7bDmPnMXjvxElHBK_7pkcCclkRp7d_vDAvjUrQ5761oouh5QsaIWRZRatlVlIetJKjbrSdtOIhhHX4GWI7EJ28Zz8U6huQ4r4Q7YHlca6q-LFn-SPaf7dW_I7GCGapXPQTAiR0rstOUdsx96nhHqjoRnQqQFgDP5LbEQqROsF1nGbFu6vb9LEmsI2wboI8v8HireSGDGJ3fpm6WCywHccrNCNilr2PuVteW97HOJEKfnTINul_G-rE7vbMXCCH2w-cqJq0ovYqeLhJ9CfazegcXfSwnxcv_cXrYHmt9mWHfE8qjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJMF0MnuiUT_nZDRbk7pCcF7lp9EXk1spy8LVLj6eogkY1t9Wxjsf15F0Jq9F4Wc2HOmc7YbNs6bh_4HPuLd7rnN_TTUkZnksY7ihxd-TNTAw7G-LuXrFmbsz7mCAECe244ofqHjA_Rd7tu9c3BH0a3ZyEvu4LUGS2AeOlTYstVQm1xgcY1fJY1Bh9cyWSOy8d9aDYDSamju0j3JN4KIjtYlVP_ZNf5qRFRPd6UAHuQub5OCNE2nQiyDEDCck97_TqSwmKl9lu5crGuslX7_IZ3SjG5IsxCaOpdXl2q94ULQkVfxjj7attGz-1-5sMn2qnv2c4KFduZgDoygfdQidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tK8qKzoEptLs3nUTGWuxzskxBKBH5Qaho3-Oyy01eNYmbsDkMYmtbLRB9fSeAgTwbn6mrM5cZLz_7fbL4JkfXrxUesXHtw7ZHXVGaN0pnfFxfdynZ5j89AVV5OXp2j6k4LOIZjgsT7GyUF5WQn2f59AoL3LpAYSklqDOQECjLZ3ozAeOovx2HFlJvVEXItz5YcZL8v1CdHv0vuVI2bza6RggZdktU5E2MxjgMVieI4B0kLyWuQtY_THjWa0KUonoIt2mlfqWg9RdoIhuYNjZYfZdLd1JkyYAkPzgiv9zLZ6__zwxXpqZXMUR-55tUTwn7ihfFtGwX1LOj6ifVofQCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaffutIWbCc6n__U9QivvfeFitwhm3hDfjPX7uY6fep4H23z1MGzUHqW7m3Om7Paq4wkaItLrpn8--J0n8qN7BjojmKo4r00ZEmJU8eUZypl6vrbF1EZN5BqysXZsag1xmlSPRpzhOt6_xbvYbbQM2_NI7Z9bJ4HC97Mi1dwNP71sxigDIbg54zDRyKx4OcRr4lc6w88Qq8cCwg637KOMKKxstfKwdIq-2O2gof7TbPhC2QQaNVFm-ur-puQh-8aO-SgcoPuW5v9K1-v-0QXeDQpdKcHvmvrtcowQod43wFbiZVRJOJUzg01vy57-UyvIM9F3rflXzVbQAKzdLUf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ePtvgH-19D76m5aqfTDV-aoWSDY1lVGGg6Vh75Y-G1bKqbJnM8kpkC2INwwHbGxKX2IwIYnCb4_bR2lRiac29mCj9UzBUWHtplqORht7FtF99vxwhp3hmt-h5az5Tt1WTPzO1kLF4Qz9b15VMDpgttayNLgFMl0p9cRrDCb6pLkjX_53_NruweRAtNRBzQjEkHI4lsXxK0d5PlBLlhL8Y_R936HPI_d2rMFqk5Lpbsz48INHnPPCUJ9wCHQf98Lh0DkJqu4G-L9_X8ivM4i9WubAwtqMLezBF1wmpBtW9XByrhJJ_cRfw81HCDj1W0gSxIutpo4TJjGJKByoA9yNEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ePtvgH-19D76m5aqfTDV-aoWSDY1lVGGg6Vh75Y-G1bKqbJnM8kpkC2INwwHbGxKX2IwIYnCb4_bR2lRiac29mCj9UzBUWHtplqORht7FtF99vxwhp3hmt-h5az5Tt1WTPzO1kLF4Qz9b15VMDpgttayNLgFMl0p9cRrDCb6pLkjX_53_NruweRAtNRBzQjEkHI4lsXxK0d5PlBLlhL8Y_R936HPI_d2rMFqk5Lpbsz48INHnPPCUJ9wCHQf98Lh0DkJqu4G-L9_X8ivM4i9WubAwtqMLezBF1wmpBtW9XByrhJJ_cRfw81HCDj1W0gSxIutpo4TJjGJKByoA9yNEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC81sylDfe0pvpwQHGHxHSQGkB0-g5Vc8jE-yZx9jJyVgxfNztSV28rWYq7aR3mjVAhAjo525yjHcxB5Tc9IBTLAcIDbfj8u2r8plAC19kActwPk9cF-6PfkF6o9QaZdkDTQihCpOUn7-4zCU0xImVkQQH69R2KPkwhkwidwDAs47-zQzt7TCjvDBKZ-IvMmduRhofPwsTS3BILO-7gqmHRTBM1POL8lbVCDtO7CKxR0p3irHZpC5ZOpaz6RgUgpkhwbXCdAhNeL_qSQEllFBQP3lf0aJSET0dqLGQpBaUH3XdMB2Y_duQAxBvMViqDxZ2mwxzUb-PFmDRZSmWxTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IihcakczdhDNrKn4IOtA7kz5WRmHaPVTDfV1uSBcO_pjS2EhCkgQqh5750ASfS4yU536v8JwYKY_1XorNL6smwBS5Hzk4zlc8FFLMqSXUcBjghV0ilmbeTJcrG6FXZ30zjpF05CDNv8SUdeWJ_g67JRoIuD5p068i2vVq49z0_iO4LJ_SkOLjJFlY-sSwVlQ35zA0cRv3vEA4mTTNv0msfUKJkEGAJdIcdxAxcNE9-G0RTv4nirhDkw6rvZW6a3es7mtjauWxR5byKidbvYWsqyq16oMGDzj-10RK9LZER9xeXbqmOjmBJwFGjgxUOb4-f92Bglx_KelftqFyC5xUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oaulklu7ny7xCktNL8ND5QXLGx6sNwm03Jhd2T8Uk6LdkE1iB7v-Z7qQ8pCOgthxGfkNVmOU8Neiuc34zPukk88k8-LOuomogQGl9OipxkHT9x457nH2kLTnAH7XlyXnLXUJFnW7rLugR0AvrWtaHhzgpeVUQ3OK0ob1t2LITCxvyksSAAwEWzLnSAOipKqHH4E5a1mAEqGNdGkY9yhuP3WroRgI3WwhL4I6-8oibU261vqXbUoeawb49lyPXOUs6_FheUh2ITbHroPf1E8umJHkUcLlgaq6dIe1-B_73nrkazZTr3qd08Rv_f9d9ETYCmeOEoQGL8nvpaOHNvQYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X05oklwjSa2yHiyKkVq-I2xD6mHoHwOw7Y_pYc3HkANeE3YZ7NEAOJRUo6yrG4rdFQeY7S6MBNKzzmSs8khnOTysFJAGKA7n73lsEsOLZqFHfZyWrtSBVdAGUzxKPC1ZAlgyxO8g-mRuq7U_TjPdnMY0TmH3d0icxvtF-sp4lF9eD5Ijzes7l0JOj3iOEEMnHcFmqxAPqjCdEr-WMED6ow0n7NqWcpQMFHu4AFKEihxOifPFZnXCO8ywLDZRxK_7MogYwWNtyBCfzLBStGxGALhWbdiEPJOZ3_cL7Z2M9tEahSbu6mQ555fVgoM5ndOGgJwvSWWK8MocJAWtgtIeRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNI0h6U9jiYMXuZSupbmDAjNn2rA-LUgUzmTwKpoADxPlOh9LpluRKDPU2PsIP3kUAgizc2EiJ9HR5kq_9qaLI_4fkjwTHwUjhHslii6gtU9TmPWT1VHIiPCjlLJTt4CseoXSPTj1rQSiIn7bZihLBmTKDKn5YocG7r7PLKZn6qiFfvsDzsJCucPM1xbu5AX-Zu0J6dcInq-vRk2LItsvRyX9CrF14E9DlootVeJ-oTz9sc871NlEMVPlgqMNsjFN7_JbMkLIzUvO4fD3H4LO_MhQv-A3a219Jk8e1KrM2pH0COwOx5ZpD910vDw1MEzfrUvXscqlvn3odJPQwbU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au6NqA3LiPtZ-SoenmpeV4-J6btDDSbQu6dWEpEeEghX_ByWYWZw47us07CKUgaVntrrqiONGS1WHJDaU4Pox65EmWcJrJ-zcLXjIHc_Hvb1vbUCf2VIuIVZ7q5r8dMw0EFlgBDQTxKt-K3cOJHMlwp4hUeyhf8U6hb-URBJH4D1qkmPpmXl6vlcNh5PjNrZRYIRyA4_cB729hG8u-gjTMxJOmSiirfTdnqpSV_7cCb6IcQ7qnA9rEnM_kLbZ1Q5q-ysO_Ta2p4sKg1zuhuy7a1gmoodgm3xgGAuzBnI06KywFyliJXrtx47WF_tjsc51ZSaoCCikZU9TqHMEMWNFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 748 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZQoYDVvxOhIozCIw2dtUk8wkfqUIQitvKhvdrkDDOLsWJetBkMytQokZnDCqoM6C712GdhVlZAsER_8Ngc2yCfYB085mtF51KwoXFlPNWLC8M0_0PjpmN5RzKPCwBoz9UvIjPH8A6kmkYsv15lWdAiAu7XDRekIyWwrTaKfDqcgE_BhMCNhTu0p3kXh2NQIEbNNi0X79UgCPNDoomNPkY7GJ57VnnVMW-wwkCb6KOB419qEHtSysUyJI_oRwlthYyQV4P6hWVmPjEVTItsEQ1VY_ttuv76yVvhTW0sTGDkFw5JvVORvnElp9QyMJixmdt34kr12VhQgtZqCqL6-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RveA0zc67RplCvbqm-nEpKDKY_3_8n83Ys5ZgIWdcl1gVVFHRGfyTT2Xmmgf7byOyhMNnWvvSYHbD_oEixcE2vCxyIp-60BZRiXm1PGdsPu9zxm3QwLUxRDg30ZcRYSmorPQUb9INuEtsHJMntv0q8gn_V3rhU6Z_5eto7-V-Hcff64qQ5ieCCNlpgx6WFp9TAKL0qAzBoRbjDOC46CnMvWogl45JFwYSxAUfs0QnIRUfuNOl_i9u17m3yxs9ngyDKxjmB2xfJ-KiM72pK-ITirzk6cUNXwO51aADM1Y0GfME3JGJlnmXLhOiyD4LRrYCULSnNQxmRxnuvaJjkGxZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioD-X1M0ArKqcuNQqrvXV5xm9n25Wbxvi4G-aGw5VHijvfty6tZsK8mKS6J-b0KXcEyOw59SEVsc0SW15n-pR2mJvFl2q0pzdYdbvTkBi-Cl-YiaBdKtwZqPfWpX104Dm9X7IFcNqkxdOfHfxd9funeJ7pRNwNKvqS0A5hNGSbXLA2-glIo5wZaDRAoStQm4FAtgM2e49XQzFxFyQxZvhTunHrseS7K1dOJu3L1WZgHGFQ_FVFumTj66T3Mf0UL8kCRNZiji93lOncZSf_FMX5ze8F_D9MpGdqSPpjI032nejxp-h3aBuPd3Jf3lXjK3FdOpLUMg_oo1SPoklZ_XoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKhArMXBOrIpAmoHuvHvDLu-iHx38RJwqvfof0vQ5DMVQ8hqi0kAearh389Vb5wAh-u33i5qM3E4lts0DnLiMJm89X3XSDqERXCqiSRBPlrONGvMsW27lqIZcRv5v2LmviqzwejSVwDmt1ERXjwyt_IWgSbjt017W7IDrXSvwhVPyYK1BQLx1ImxxVxtEFi_lh5DamO3WytJvsbAvXkqULTlqORdPt3PuJWUB8AcS9fGtRJ0ZKM8EvT1UA1kXdsrrJ6Vod_rSm0-QiYkMO0fVT6LPhpY_E7l-7Kx62YDWz4OFNFngUPzrYQ9-4VekS_vkjRRTipKnxvoGuJxGQ3knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4AagKILvoSnRJpOu4bWcD66qBwEZqgjz0R-DjwZbSSx3x-DiJgbwkyn9agGg8iyAkwXkIBDdL_Pf72de0zUctHnrG9Byho0vPWvP_mABabIwR85aVpTDH-0TYOqTY3Qh3pZ_JrwKtQYuaIF7HXInTEIaCroEj7rBF9hIgRiW_76Nh45tVeYH89wwIIsQ8X7I1ZejHosjz_hOJbaxQG7Gx00BycVU7OHRu15eQFrQ_3QMNAnHASTkWQc7Pr-9aOj1LRbShYa5Nj9IMzoNi9aCDky6wrSn37BY6Vr9eVc3hUIN7H3Ac56kZOjT6VtfFaAsq9ugPt2RMEFLJHUPMsJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf-bj5XNTsJmTuu0ZmXH5jH5c9961re6M5xAUUb5ctroSjUIFN66KMcNBiQKkVFer7ihNwQLynyxsB7ztZBJd-e7zhY_aON5qGCVZwjH87b48vfPgXT3GnwY6lBvof5o8tORawCZ13hGD9N31_9kB8VLTPCLDqQm0mP7u0L4tw6l_Zfx_lTX-cNLxTLslkur9KVJ4udUqgqg1nTW5upnyzZX2VoL9ps0x1Ip_unTEaoBnjenz_bwYAT9ncButZfFMyZt6nwWyOf-lDlWc5MALYeo8xwP0aeJlRsQWwh50F1c5nQf0W0h3d8V1yXNo7zwVxNdV16m_T9H2IaTk-9mpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 641 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boYnJLXQeF2DR44rbaVzNOQELCU-dj68FnlW9ol6HdW6B_712IhZ2gPPLhiOlC_3XwVEZWanqL8f1dR070ycf-OyHTCsRK7q-KmuA6s2BntA1sgDCa6DSXHESp1adjbZOL8fvnObIRHtWpOjyqma4cD61_aVSmOi9HL5iAJIWgo0AcaXLDnviBWDb3NPLF09LXV4fjjCUdM7betwqwowytWxg5OgO2n5Xgwi5BfiYpiJ1aGUmKI1hR77aFRqkPbbz1bp_7KGzfxktuQyu7YVl4Tq_pmd0gAbPi8cI4BEmEoUqn5mKZeu1CzEjAsoC-X2PFOYnn8YBp9xtNz617MoHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V96iJYnPVDZlcB5NNBgTulTyNnt6wDBbtrTzVoQAO7mf0PxyqhXsaR-eWSC_kKchohykQ3pcLDRtszdmklPs2qx0Yj0u0193WeJiXmxGK-DkC6xa5lg38Fg_A-N6U1nGRf7eDhmyrNrEku_IFHUX7Ty_DELLiZ_vyZRfT3jrGUydpp3ABe65NG3GH9614ACEgQcfURZFB7eMZiR3To5lYGP-SH6jE0zwfEkfD-XUSA1p3XmOdf3cMRahjfyL17GjbxqG1wtXuXVI-lNMMD-bhkj26Oin3g-FVvM7AlegVxEecxPnhgbhLPinJVpL583jWcgK48NXXUgXJI6n6zF7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zgpqh7oWD5Tj0iw5WWoFYbwDT5Q9iHEN01HvBLohPwO5GTxdiIipCSVoR5KKQ2v5aHUnAQXfXlGLaOpRJbJuzW9dQSX-w_ep7acKPYGhEovG5apKhi0Lc68JXGu3Roy67OUp6CG1JqFCj6Z9IBJxESKhMpORF_q0Q-LW3mRjpf-Sdp4xeHLgMRvcsD5ULGIWcwTJOiDqbZzsOPr8KgPKtrrHzJ9qlQ88SSEF7M5juavpGz0rLn4E0bvkLg1pfNgD3LqdayWwyDJHZZchSGmzWrOxhrYjhjjFJ80eTWm9_TlzePBuXfmE_SZpBI3tNx7X_kZ8ZAWjDfCXYr1z7V_HhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSBVcjE3g7bBrOP_vtfAOTjSP1YwTQnu0sWPJcEcd1LH2LPXETuJyGRzt8Y8sZsY4Y3aL0uymO6jqUDRaSHwjB-qAdBH7fd7IhJmeH0_gBrz0i4xPHvwluQzUmgZ01R1qKloyBoixOe4O75n2QYlINVIsTQ6tsQbS6p4oLsxGen_vRIRd0w72yXnWVJZsTZC6tWIyKwhhqzQTR69mJRAiHiFgPmgrKxS0uxXeTXv2Ph6pbbTPcdyDW50W6r4UQhvCXmdKPbLOpMmPDEv9QK0VGWvA4H1wE0oY5achqd-0uk1krliY8-QvX2HX7OEs8YsxN4an4AwBb86Cf-nJaEtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLjGA2uXFAziJLg3u5QlIrz4b7fQW1I1EUwxg3HzcYPuHeLAkQqETvKueSyia1fc3pIBYIruSPRaUo-2cQMq7WVvPCLQrW_v71lS9iZVRn8Sey_b1Tmh6yCkJfUqjccMQbcAPJOefWO--ys5LjPT-jX86LcXJtIG5sljQeBS32WgaeTiDn5XEPPMajxwhiEiFs3MSCQ-n1Id8P6frS2tpZvcXS0t7N1TaNkmTZozY3tvGInBT4WAf1q9zwv5FA0pAmhxlF43VYt36qyUKSZT43WgLWiT3YtdLOKMQjsQtdaA3-p3fYTSDA5Qv44rAY5VUJ_ngwC2mBsZLAASj4xw6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4RV_VEBL0TD_ck8pVdI3ggmsSm5FJdmDYhCxXpwZhPTtrSTr0JNkxPYsox5So-ch1hPUNDPDQEx95qzo4VJYembyNf8qUM1Zph9qSnh3GSyL8sAlmRY9cNFx-0RUL5pAcE60L92N1FxLru5wuZDAxC04g7WMGK52SIKN6pPOdtVuyFljyOmOriArRML0EXvvVn0XeVh_MktwT6o72nNb5WX5dS2CtK02RX2KYjhfW2tbK0lsji7GVnWTAN6Y-b9lqd8kdyZkatxRATLY0CJepfF8yWzm3lX6YtaMBdNG__0E0tulpo0vBe06mI0X1H1A6zCJPjKJ2LRRAlr97wZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 582 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqnyfnE2kVqdd8kb3hmUiceVcDCSSnSWJZjU4hrkagx657Vxxnjz6uPs1JjZGlSWC2l5bIk2tnR-TLUU1Gtoryp6dxmSNfeabvR7s0UmY44tmfDOaa-sz34AdX2-MLIUWLeO7OQf0GtoXdVSfcxGctimQsvf9wKynON9jpe3gHi2QSBxsMsF4fRYo0d3f48eq0uGTKYpkBPfsHBgNP1hGDIrmV4wVhnXhr27VIyDoN19Bsymh_IpjWuilkN6TNG6zczLwz_RCxAAQTp1pjc7UVWErD3XbsfYuG-65q7wZotwyi65M2OsotRTEaNcq8yz7xYhjjs3HlD-OYJxwS8-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 594 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMGGZk6Amn4R2ipznkqaQLC1wkrKPc7smQlHDnN-YwVdGykVfdDBLNZ3Xm3yGIyu9tAsMOfWGFMi-Moj5bGPAZH7L4k6FcolIrbl9VKYM9TU7NM9OZGZybqrl0EumXxmYImHqT3qyMYagZLXhs734YdlkK46d8jDMZyZj7XTX0i2x5-f4tV9YnkzmSfgVxpLP7KRHJ0UzUcrb43dygt1Ish40xP6diV9GS1X3UOjg2vtohhE4wLkPpI8SEq5rFiruMtgxU0T09LhC1sfWwcTnveyyC8zdJk5vg7ewTG1OiWzBrXrJBSRaJsC2bImbV7O7mzhtbLEa1D3QpD0QDWzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe3ze3D8J9ta3Dt9A46M7oLqlAFyUhvJd87uSQnTXgj3sXolp34WYN17Lq0XVlwDLBG7PB9mhCW3sJezsaWdb2_mNs4gT2j5eCEaxMqiEh5u2xJafgR4Bi38IFQDZxlLTOSiHjd_Jpo5q3udkXi41qoqdFnHOzOSNo2EbLlY52lTwuQzmuUtOtiPzuyEEZz6rpy7LjL-D5lf2oK-S96Fw8VgQLfWJrff9iEpL7X7aVsKTzwxgr4esAJepoa3_Vi3n_-aq7QTiB6lISo9EFzL2QbRx9jSCWtyPb1TAEDZUXiHywCjp0XOadSuHEOd86yTGXZV7pdsy5AUF_1g0Eh-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 647 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caOwXIehykCweOQ0IIyV_p6SEG4OJLtOnoDT00wlvqPN6FiXaHQsjqHAxckOZQCi8DdJ9fv7UXswojSePMSJbAVJJBRf5HylKxctXWJYGRZoafU9iHlnfB60uFRUgyLS21Au4_fJYvSqxExLSIY0SIhuD1mPWcmeMzi3ac7dEqKSl8i-TtZDNwTUKwMfIGkCmmjVVnPGu9Mnk0CfOAlrOKUhTxbM09hD2CXKUyxZ0aMAjrbhyishvVlF9FjI8ENWYMSqmDjNNR4hUX9KGuKVuLqNTc_EWwz9Ky0D4HbqEMyZNcb66raY98XvY33SIm9wBnX4C9bP_KXnF8s91MLmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 715 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMaevo3EF_C-aGTXe-0BicC3PBfNlg1-Y90qbunhHkwq2qG8BRzKMR3IyEi5ZC8e3pwxU8RCFS6FKIh_8dvwfbi2eOi_eWEQFXUpd1SXdlvE16z0NJfVTKZQ8C2gfKekJupuahseN6xP3k_U2wzMzp9xAKsDTX5XxMhSgv5rOxxv25qF9QCjcz3zYNCxOoT43f5Th42vBkM-wL00udgWZQgyYz53VDEky2CJ5CyMvt1asrpBzgKn4i3uW70E_5OoFuz__WHxM6Yy3WYCcnaUX_ddIa3BVhy1ya5oSv_4B-px3VUFvGFF99mkIosxwWnee5BhHgWwhDwttGum6IucKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejVdsHhd5g9pY9vJj70QuFrZCbrdsl7pO8NRIEz4nw0te4RGRreJJ_KaWf-gYBX5zpiESKCfIyautUartnlno2jnV9yhzgWYSqDsAnZ8LNuayC64AwunCmt0Rn6Bli84zEL0A7g7VCU0-RanUOaooJWNQ5NBVJ5TG0cDp3dxWa_kGMe11Pm30BQkI7G77zwt9-S_9r7J1RAal1Uv7KnPqD471gOIoM1rnZKbW8WVY1PdEQykr1_d3NDOrFsiYM9WBE9aq7PKclsl00sXajcLSvVsmmCcn7hwbK6cPMOMs6zL8KNmNWfpdXBZwRSlP7i5eMsLMlKb85FsndYcvxskWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNi8RAvEBrG__e0aBuGfwd9x4WtA2KB9Fdp1b2kNZO6ewrcAvUEp8Hetz_D94xY9jmK5zfEqEN-_xihRlAg2RZlNwe2wOhk3JkBJ5SR--OZFXu94Ph2tpv06Q8gkrnx2GiLEQxprMVY5WvVLZJWhn6TszDC6kwlPyOv8jZYNxAby-hMcJUcgB8CSDJtZUjFv5_REY1Q6JRO7PEMDi9ZHqH-LCKcHPQtRY_2sfcAWLK1idP35Li1TVm6wQ7LsxprVN4bscSiv18K5wPdaRTEY1sKJcW4T16xxYG-PqZ3C6Wjt06dBwO5Alo8KEH_HfyiI5-9xavC7ts0rph7AguiF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muL9DNNagWLzJ1QqMDX7IJuQuOiFMH38AaIiajAJR3O77gBX9jVg12voJlSPRWxcsM9X4XHdRfZnBj_yfVWqyAHaodG5rmc1lXi7rMVNLHoe3vYUxY19nXudu6A7teHPoOYeeSdd8Ck4B_waiJ9sEoWOoDlgKkUezF-t9jQpDugvYicixeFoTqlQikclV-w2rVI21pxGKyU7ase_6J0sLH2xsMDJ8kSKoZXq4FzFY_bbcPj6cVpRtgOhbpF8duamZUr1uf3ei1PHMRc-CaqokTZVX9UN74Q-ET2aOSrHsDPNkKjzj7Rr7tHYQVDN1cp6T-PDbVScKZYQGYc-HMlW5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQg0waV-IfTbV7-nO4aOT9Rkbo11jgogRMi179F6LDZIsZnQkYEN6bssoFiE590lEs11vdUn64Y_GRz5qADzrX_Lp5WIRjevY7AM3cCi5Z8oD_ehWyf6mn0XleQuxkzQr3wfzaVx5gDVNq2W-h_5suVG4zrPbokGNHhn-p-_KqLRsAU6OFVXyOjxHOvaGujv0kbsECxk2MGZrCHpExU_poesZYAVHgLc7i8PrnVYVBfsRSh8MYYUpw5O-o57qqlKwIirHR10lwdR8iLaH81hhg2G3lVrw-VRktPezsJz3biwQwoxm33TvBQ1VD5PSwMlywExQeKfd8T6Am2nYhWcfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU3mt3mr4imlP7rKgAx0v2ONsMHWUkpnDkzU6giq8Pj8tbvmmKpRegvS1g-UAdPHi3DXj1PF5FY69eTf2iT12Sm1wqB4lroQ13YcKuL-XyjO9fvbW9pR_aULQ4hXSJBwgvOBgCN15HxY_SGajl5Jmc9BGzJ6DRcvGRYqbygf-TedreZoqS4AEZnDjfmmeexTBD1BIvxjtZ_tXlQbvBd5d4oQQJ0dCPpGQeRgUnMjg3LDO0lVa2wPkJUXdEdMTNklcDy_BiKBLc3zC1fdnzbFy1HslTrWI9C_bjLZM-eIFMa7d0dDp0QrSHMMJhfL4NOTBRu0dNSPvBrp6p8BWChOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZzaDDKVWnHfyf3K__s4xPQ3M71bfQ7g1u7yuOZMW3WwCjB2Us5-1A7rSxtq0op7O3Vrsm8wa4x7sXB9f39WEIEIMU8q6Yb4U_wkUtVRfykPVboFUepkjXYKG1CJlSil--E-Jei0g1vWd2od4JWYImuhsIg_40bwOt0C5v3uCBI9o1NqB0NHSecpoRasFzyZMtjH-gSTnPHqVh4Ke8m1TD9z-OIHK1jJvqa50cI1x4VkRXBw8vbe24PaNGX9E7Sk-yBCakrTdIgZLGaO9BXzsoYTJF5PoVqa6B0L_Lc61cTcGluX2gu3Ab9gN99T-BVpXtjNSDLlXAaoqoIV4Mh7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVXbacP-v2c2JZBJoAXxBTIcqwVRf7Pmrl4m_pq3PODTVTBikeOekbZukv1N7B1MoSOOszfKmkmyHSfOBxAPJP-AzR4VbnwCn214FLD3_VVik7NaZnkA8w1buLbJZYZZLUylGZsnZ0gRvdsahhcSqlLZu_GAmlvDidyBQJYzYh4Hwqm0N7toGaiw8BrYB2ZjxSdIRHsFBte1tTqP9zcl5rLxoK2S2AOSgvm7ydRzIptKlS1wKkyxNNFdLkgtH73BzTn9MDjSMxdRew3z5sb8cyz7eknJTmHtQL4F9RTaYVbtEWKDJr7A8ulNIUV_UB8Fp6-ivf4l267XkxpMz0VbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HieSjeAdoQG0-RxQf1q4yf8jDLtK2mXXpVojBGkamUL7DJGhVJm9mZdGJS51DySH-VMDLUcXQ0wKIyYWE_hKgCC3cfQD2pIn9wmXJzyYHQDTG5fpGKCOCtRTlAtRRfUKz0bpt3qW01l_3tUjTp4DmcQy1p7KdaGHt7M6y1jcBvYtKw_0sT3N9gBwP8cH5EUaLMIFn5VgquFk2qpl2OnNd_lbLZqqKdMXrMkyrKzlbrcLmFRhHkVf1kcgInbkaXlctsF-7Gz8MfWZALrk2MWQviP9sVf40wegrMTUe3tdC2rpK3PtThCddU93WCHL96NEbjKrN7BZ4l31el1EUbrOiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxGxZoEG9tyB-2wngarfmKEYrD3hVsZEVUfoVpubHNmFi0LNr323mmnqGYAo_tqhEqrnEnmbkO_e85unDW9WydaszFIuOv5bmWIcaMLG7SDqDKDNws0r10Ud5kwD7A4-whSwfnrx0I2PqT8UCHfE4T30hkl4I5CbsjZl-fDe-9ZH3UBTU5avFfOZf0mSjemCEkEpw-SM9B4_uOv9229-3jw9vy5To3H66sfXS9KLuQ9AOC4eDQYYlb-1o_VdfOK8jmeureVAztuOMVSINuAWEnNIolnd_UoDLC-wlbCyLiQD_C0nXezJxeQEdNp-2l-uj92Ddz8-Fh_w0GFU406cFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F52trRqWkprhTmdfEBOWL4k4fgwo-rv96EHYMsAoqZN37e0OdDuvtf6w5j0xldFE7aZhptigpHQeUjQbeuJ8loNM06WuXzTby0ER0eqe_N_hn6Io0lNE_x7Bz2Oq6haJWbob756V2i7M5itS4TZ1durx30NpLezl9ZAOgtmei-g99gD5ugUdxGrt5X-5dKtjwgt5s_-r3_QOyS208qWp6_2jDIdsREKAZqvrPChivZDKlf4oLNNVPpG6ylBnGw297ZeEzbYO0gozWKJKh5FCH5ExBRUFIRZnLfQBs1QgZpMPkEOCQCI67V4Q74DKfcz-Iw0Ik58qrNt11rDQj4ybHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqYrCmJ1KkACeHL539kEXCCora1S-RjFamiweQYyRY7xPJ-TMg1I5jj_4nhuaIZ2Ie5qas9CSElTRQkrTrZKu_LbTJt_bX_P1wuezdBg8rE-92AIfHXwHIwxPq4W4FGGWoS_yy8Dr5Wher2em07xie12JbhpSp55kfYmzBEYhCd4m7iiAPGSNtt03_LZ0MGRJJSKlLaZ9dDLQe6uSBzkVwDKfvZyxLmcFgaNDF-lriISjrruGmJWJQnPsoM_B_ttUfG6G4l-77IyVuJVvyuSv_PG0AuGyK0iFiQgZiMat31FYsvIypslbJNygmAdpj-XWXrmoqM6Bzz10h5tyFl1ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPKCLo_KJeOTwqJl2P2O0TEryAVxlYwxBEQOmhxvmKNgoU0fBi9KpDYrvScqwPla5BHYu_Vdop77sBimlTCwvF5Qco6tuhFPYwDI9ydW-VConZRSFr7XmLOge7nTyz-pONSnPJJCOOgtGzkKZcAUGPrrXYJKKKgMnciDh6qt87uVOZYxpP075apArQwmiScmnQiKtj1D-SCnoOaRcA4vR8zlRJoZH-KgPojjhTPvFFnwT_Z-cr3LN8bvkKXj3_BllQqIgobaSm7c8XtXYiIZLGGRvYFOqbS2g6-UYggn_IIA9UAEbHHTEEBndFD3rrtvP2xT47Xi3BKXXXSd-oiR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 587 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XW43vrF3dNeIYi2h72gCXkj_jQpdhv_hlBlWZGQ_wVYfoxVzhKMK9ebrIxkCnLc11dsu1C0Tvs4wu0beeJxuImyyvj6i9V0Q7SyFToavmeWLOoTI2WvdpJXFqu_f6sIUVBHq2CYr4PYQHtgtGk_XCyu-QUUoLIuq_2IA0FT_VJOSWdV0Dg1XGTvw77OR3cyz4KYinM5yPvnFogvjkAMnxZdPY-N2FqhP3JROUl5LGbseyqqPFDW7QhAeD9bbPEq3zIjEOKHdKdQ-S5vdGvByVwVtjaef6SDiCOtRy3Abog-bCNBS7gR2fozRX2bJpnbhSlX8qjsFC61whGXlmyiPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avw-PDD6zPp3bl-Up14OrsvnwI03_wQtz_tZ6I77HArzNZDU1kGkRn1aJgDjWnhaHKWBcE0N5OKSn03_rsvBbSwzHu319_Kcq1p9iTzycKYPh5MYdbd3nriI6tiDoj-xqINYeD6nuNnjDkkPjQFJ4IEYpWQn0p6gOb96wC0Xtuwdrhh7EvxuxhsbGNzPlKKcbrgKyXMMy1_DHd-oZulla35R3IxEN1K6cGUxFbpcdzRKhT6nT95PywOX_CZUvnnWAXyFv5mOsqVtguvIzdyP-qcfIbEBE40U8f9_T-EtU4wCJrUU2fhMEvxs_oOcjB4fS7IjrdB7dHpYjOnVj3CoiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW6pAOfvAJsnnLUzSkawMxSUrgMv3muqli7PW4S67b8XMUN3GlTsx2GVBpFlDn5JfYX5dTeUczQsz4Pf3ml6C5_yp1G25eZjOG0814A_QKrQ1u01FslbjhSCooqNW6QLpTPx2ZiS7FKq09Vh8Smr7nQZzwRxNYi6nRH9HOt8qR5f7bx5gudRjFLsfKIgbDicB9sEpclgxUDUec2fEBdFvHmDdGcqi42rSRefFa0qI4nueD8qqOO2LDUlzvFx6T_GWOt0If3TlmnmEt2nb6K2i1jqGtvhPrMW7N2kpZ0OHad0evxyaWjTT__n5wuCu_2I5uZDLpn2X825D3RO6v48CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Png0de0yBwVlzjt4933pHImWP5eFtO_afp_xwseejQPKKLxr62_kFkJtSHr6g981R4B0DqjaJRQ2Cv9E360ExZnhtvdIDLDDSlPmdikoMIFm-Io4__IAnEi8de9ADiuxO4wLDUmEAZRbU-9D_fied3s28gLD0v7SbLRXcQ2Cm2QYMwBbhg4QAsP4fd3qNzYPupCgSxbL5xsw-X9yCBKNRbzu45uga27Ao56XmkqV1yPWp_KyqSAymRsx_Fz275JvOZbeeD4NmYCgSI55MxOaTnmuCam5UPA0aSMGuQOrwp4BlPGexsbq0cu9D_gyjjtpXsnBJrGlY7_zGC243OIIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9QZ3nbVa1p0pUqGO9lzbSYZuEV21Et3twvfA46PX8vUGS0IwhlEPkk9BR10VxPWuo8YORbe2m0Va8vg8_kk9VUJhlnFjkGu46aF_6ntc0Awcf4pWbpvUXCQ9jHFhgJTAZYEDrjpld1dCmnear8F5LOL9ZLRhstK6mwbtt_yCwVcKKotjkcZjuaMvqv_NCZ2mBz93ZimYqo5KtvTIYuUpVifxpnDtbPQfuABtVkFmiAxY0SIgvtN63k69TMQGbrdEVgoPk6NHZm2YD74zi2BxD1PVOS4M9ffAJV35HtTQ5AOYR16iuF6KXSx6iJMqxp9jc8ki-DjXZbZSAb0tfPGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 771 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRf9T5X2Hi-n11rmN5dt3sjMHSpd38KXoL7M23JsBVmeeLlTQu2zFkt3OUfkqFMOczkPtyuRvbW-sD8itskaall2iEdRzZdqOyUmTIzlh-ZjIyX7xgFL9lJHZzyqI0nCNFk_rTgYeC9ehS7sY6zQqNlCn4ksJAH9G6vF_8SHtTuS5e1eNMGbJ54OJH5AA1OWGkq1wWMv2fxvflw4Xdul0WarNB4xIabxXgaVvNmZ_AMi8xLDOUhabBGD9Q3MtpWAiMRfhrLvUSPC1u_nUsY002uF9GwhzBB0MG9HZOBWLY148fZmbq7eZxDGBYGjU73GTohIaqfV6G3iL3foEVoTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUAicRfVWPzQfxOMWur7qy8MoDZ3s4_Y59Lt_ZfkNbV8cj-vLdgTTvPy_Ve_jsYpUBkAkdlkSOCNqW5uVSzY12ivnOeIIFbHJtwU0bo4hOB5xBsoY8i7zMhCMjDAWSwnbeHrDmmFY1990rvi59f5zwS3vJqkcWmgcSyTyEOPjm1rPHspf736YF-8WtLKq9-aPtiw8DO9EfUZXt73ecUfpMIZ62tY16fJY6DBzjHH7k5YrV7j2tm4uRj20Pu7VMIvsGPq7zf3SX3BYovwCahawgyMQiUzpwmdAhX0YvEc-lFM0lwLJTOEdQONwHC2WO0CfzwfGqeIIONdnu_puiDa_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrdpDdI7KwYmxpR0LKMnibMoYVcOfAACl_DsH5-ra65nmhOX2ozrEVP1lyQTFhHMxQC-QTEKiSfuURLpicSevCR1rN6qcqU68NYSay9KYqMZoLuLOUGFcGvU1C6JPEtU2ELgBYqOaHrcKKEvIYp2Eyi-HCodJJS96PPUc5bQxGuP_Rnj7K4n5-FKcmsNFstfn21TUNaQ88AHwaOTLW3PQG74UFrcEJ_mqOJzY57TsOB1YovuyuEDFn9jY3NuGhV5NGwThGpretOsi1tUkloOfHO03lkD9F391St7FEXhRres3REyAPGk6XpES6tJ9L8zNtNXnH0PbrqBCzio-k349w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9at399ZUdYG7vgxQWY6x4jDkBTyJPYkYjRnRUcuSwiDj2SEZJ4mvBa2-muk4V57xEXmR7HPlEA2XRAWBZsqER10tDw3PzOLYD0iRJbzeKHdiZSqSIwUgDcbn13hvSVrvCFlllokl2eqoUMSzSHY3W4WdwgDRP560a5mKge6mkBSfjIDLxpO9Ba8aYhak9L6NvGpZ2NP8CDXe3e3C_Nvt8lvyKJQyof5WzW_W75gbpy-P0mz09BD7CtsVltP6zPf-vxXkLBHmPXHN-bD70iup9-QNS85i8UknTmR_haL8FYUnoGUrHniaTMAvtkjDXYg2Lo5Zg-w4JbWeR7e3T7_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6TUtK-o3YoNWjs8BcIkY9veQyNmRuU7SJFaa0Oeu-tuCBoi8zQo2UhOEHxNHF7adeTduVTErwEo88TDWAsSf24ROEcHyMQw89L1NF4CoQmbucG5rTPzTJL5JScolVyOZkiafKKOXYpXtpZOaYk8LsIFD6eNBtR2GKrpqBcIhAwF-IsXdIeu5GDO8hMsAQVxKxxQoYPk-8ouMkF8uHx9SmSrc3Z2oKpKiqUNTRzGmWxwD24d8yTz3twRqrxyJiDNIYO7wHnC-8HuiCGI5Ek_fJrLpjftYsEZMyKz0cvq0XBQOP-gPluc-WZnflRcBCnUPbL-l_6i8m9RLah3OcLpzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKnQnbKw8gnU1b2E-F5Iffj20S3b6thqbWhs4sMsOo7T5Xo4iFzjHJNQrpMY9dYdr-fS-q3k9tS811biznazZ7Az1Bamphq1zqOww-TrPRCratPHlBD19oPoyqcwu5golEqYrBZBi18eviCdbpvZdmuqaukMpbpzPUD4mw3pjXDONhnQ3QMoUTkgP1TwS28B-Ia7r7V_bJrF8TThY9osicf0GR8Qpre99_8Ysij2gpbhXbkt5goYym3uz2LSGulbehy3iDbRO1YARJZB4xYCRCneHEhErbDjNSD8okCwhqKylUgWHfEpBKdDpu_UFcxAJ_izhVnmpJgRGoaY80qyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=d5yefDyx1mtsJtxD5lkWaTtQiHKAQYoDSWr0Ld0VlJb1tFiXvJjhMRz0s-A_Gf7NAD3FdBtYQ1oMZEAdUWFIfFpSzNiVI_n3ZB17yHStYSInPQs_8NKYU8fQNPPOLLTTQs_vi-o-RzikmyqjMVaSOFwJobrgqZxT38ZyZgKLvjoptjLUEXifSKW0yONwySQGS392G3H_s47zNKNuG_pyM-FRKuE4QK04IezxCCDxgvvH9c1OHFl-IXt72QyatOkyqFrx6I2DB8YGcOfehm23gI7r5QbCMvl8zyT6_QBcIejeT9vj7l8CHda9Vzde5Z2Svv6rO8HHDNtQHAb5vIgXLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=d5yefDyx1mtsJtxD5lkWaTtQiHKAQYoDSWr0Ld0VlJb1tFiXvJjhMRz0s-A_Gf7NAD3FdBtYQ1oMZEAdUWFIfFpSzNiVI_n3ZB17yHStYSInPQs_8NKYU8fQNPPOLLTTQs_vi-o-RzikmyqjMVaSOFwJobrgqZxT38ZyZgKLvjoptjLUEXifSKW0yONwySQGS392G3H_s47zNKNuG_pyM-FRKuE4QK04IezxCCDxgvvH9c1OHFl-IXt72QyatOkyqFrx6I2DB8YGcOfehm23gI7r5QbCMvl8zyT6_QBcIejeT9vj7l8CHda9Vzde5Z2Svv6rO8HHDNtQHAb5vIgXLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHunfbN4_Ukg5r8tSK8qcKZ6ZmyV6rF8obu5WJI0EwPusVsGE8odnO_ORgs7byHQMpzNOyOGfoHrtjoy3r3uqmeeMJkDyMKdWZl9vnsMi25r0vzKcaNXKnYQYbauiN-zsGwrHm52OUAfUfhI8-Js04wzaUCBKMhE-KXDtY8VZe7-mlCe7O-D1Fj-AGnaMVG2G01NfeEgvid6x5-Q9mLUK8gFe7-1CjI-i-Nt7XQhyuw2UKajmZ5JpkNmsAezUx_cNMbmbICMUZtzvhJo2Atnd0O-uq2149McdudZocYxGoUPPLLiG-DiOCDOsoNPAx0kbE0mE_a_V2i3nFrnEzppsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UT2xSILptTld3xdAQzNjwz9KqcgDMlDNdZf3jLARQoX2ixrt0byTymWaCq4b7AZad1vukyK7751EJ1gJ8A6Tg46wSuBKZX0gT0sQUb4iNMJS2lBrH-jg40FJoYi2FRYHqli1tsYDrLFKpXbuiDffwbhAYZivJneGgRsTeeZPUK_f19L6MdyXSU7p4d5WDWIfXychG_ZlL457gj_LDiZ4ji5iBdroyqlgymMmMXuKaoquTk3ftLmOizxn9dt--Vh4J7XfIDaznlSYufOC3j2roRNUKjUoF0RzSPHDTPGl9Kg5BGk_vShwEtxx-xwjolIwCnAu0I25vaeYKvswkQappg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImCeVq9vjxDYra63p1GUPRPDIW8EZKl3V5hp9sAQ6cJH28ni6KfpknSrJvepbS9NHXmTNN0667WpH_8huzwyqXBIglepFUG9HD0VDbqQFxPbp6_MxuOheP2lsBKBERgUbiy3IEu7j0NX-zJKVo9e77PdOv5pLoPwH93ybfvD9OK87bDUkk_Lc2OWXvmPl1l2yQOHpsp5vdLIVtejNymjZLgHS78ZFPBQpN-3Pd0-K2xhCJUVzRobzlMCadBWjluG3oOSFm3eio16-0Hw1iV20iwrK-ydGSQDMz_Jg5Fi-2B6ZemQ3iQnWbxAvNf1VH7SjOroeU5wM_KCOdr5jMJvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTxuPsnKVnM3k_2mUxLoc3nMl9rgkYXgb-Urs9whlO-A_fPFb15c1UyAi-kXidmrf6pLwzbAOzh9tXYs6jjhnOGA6OlqwqFQemwjVHwbshBGo3cq5SFBvE1fNAQlQWrweprS0K4tkyKD8sTA1-naLrMDwqlgDi_KTGUcAm1AP7P6YGxfkPV_WHRkDugKqwfKY4T4TZQuvssoGkfoE_CxBi5weXWsne77BMDduf7OrO3MdtcxM5jwUrma7nTD3mqtNYEs_4ok9D4ayOq-cH654k51peWhxUAsWP_95wX0rq08KvYnhJ-Q0mYcEFdHM_W5-5XnThRyFTR3ZDUU4eiwnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRpydd_6xASsUHFVd7_wr0Cy0YhYpTB-kqSVBwOBBx4GfGqsYx_5QaHxwOOo4tkpRcGzIulU8m0CeVQU69GNdoqFjSxQcf_cKBc_Mism5GkWjUeDzAFCqHs_WUfpqcf9kzAEZbon_cNFat0Ew2pZHwuce8lOk1OdBnIxk6MhHQxAJxKKn1QLWkN6sP6MjU7f1NACOusG_gYlSKykT3xXtU845ms22zcLemC5oqaG0losYuPvOJw-B_81zjJwy3VkzxSZz04xY2H-FeXVFW0CwIwiLD7vM8QtJoy-BFD9TdX608GLuDiYYEtsOjYpZPdc1qHN0huPIOpLpfpmbvR8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJR9woqX1MMeiReymmyIcNXuML29UugJrRGQTY6Euu_2um2_8y4Ut5DE136hMq2YYHnGAujp7XFazqG3CIs2wEbeMPV6dBaAblw7OYVYFRQnn0Ol-I0hDegvAuhsAS-o1l_iDdMY-8rNKO9ULNziRdznWzVT-U_DmbpeXLNR8uOreFi9rP680PFFodrEJ52kCJxe9d_4In4TR3KS-22Yh_vUWmjHG5qZX2q0UNfDd1g3IutW_1XjFBD3Yu2hgUAtP5n2_yks0VhGt-pXjcje3a8DickQuqhisht44hoUw-7_4qDI0SALqOBqknPEpBt23FMXPM0sq9Zuo0GkaekGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H89mTm3Yf8bp_B03qEMzxG0M6FN7qBDedTYKojXaWLVxaQzRyF4rdBccTSL7USavsFsHw9uEVM5ZirRIGdNV48etjl1Hkg5tkk8ZZ_uTCC1eCC6Coa2W_ScueQuS0fxfCIf6TJlWBnWPdxs6uWguUPJIsAMFd93T7gm6btf70mm-dRooua1gKYX63jGT83_ZwhjePouiXlmJUrHjS1_ULSxaZbH1dJXoZmEhbyniFmmER9FMx1yzrgef_QRxNX7BnJLS_ZKKecr_GpGrXbndz3KN_kdA8MvwkzXMoz1JQ_UpEoO1s0lfP4I2PS_uIE1El6xmE84g5f6P2qcwVjrh6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=IqS-o2e69MFwl6ZbvKGmQEo-DoKKwNvFrBFv0Q8faUsW8uZoIgtcwRcjGyhj-MosU6CM-8NWXhcZkiMVOKwzziyUEGpkBlhvZL8OKbOJRPcMZa6-mzcOGCrBq0N7YCe51Syo2_IA7vORsYfJw3yR9-kAyHTCRKVGW1L6Dy0gGGed3JyYQZVPuyIcuk_QPR-CfnBTX7_Pl-v2Yi-_03M8mGNzow3BClZmhFLX7E8MrFmZQ7aOhSZY1I7PR8MmNQ58JoPGili0ohPE41MMJjUpZzZbeADfHH-q8-yh1wUYRTWF7pJQRIt2VsJHvrgVl5_xvgJgxP_5608_FRbmpZ_x1jnKD7Z6xx4MRQrdPhlkRZ_0sHlsm4qAKmJX5J5uMhXwSASraDk8R3bHqJsg3y0Q9c9ZIVOIdPQB8qM8xojHOOFIyvnVg1Mq7_GPYN4EwOJFT2yF82-NHzW7zM0DjjzOsVYOE2Oq3TWvJF84C2L6FxDUwqRte-Q2zqvB0dR0JSjH0p1AXg2i6YBwCW5DCH6oe9BtsRUFKhH_K2UL4BBOznI-SXPZf9bfSKDA5zOirfVkM_l_4EZCP10F5KiDQuIFjL6TMVHEbcEOiWM_FVr_S_P23VCNjsq-2Oxcf5gFlUYTgoF2-Ok-f6tz564LFr9Iv6wwCI53w1i4qXxhN1M54-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=IqS-o2e69MFwl6ZbvKGmQEo-DoKKwNvFrBFv0Q8faUsW8uZoIgtcwRcjGyhj-MosU6CM-8NWXhcZkiMVOKwzziyUEGpkBlhvZL8OKbOJRPcMZa6-mzcOGCrBq0N7YCe51Syo2_IA7vORsYfJw3yR9-kAyHTCRKVGW1L6Dy0gGGed3JyYQZVPuyIcuk_QPR-CfnBTX7_Pl-v2Yi-_03M8mGNzow3BClZmhFLX7E8MrFmZQ7aOhSZY1I7PR8MmNQ58JoPGili0ohPE41MMJjUpZzZbeADfHH-q8-yh1wUYRTWF7pJQRIt2VsJHvrgVl5_xvgJgxP_5608_FRbmpZ_x1jnKD7Z6xx4MRQrdPhlkRZ_0sHlsm4qAKmJX5J5uMhXwSASraDk8R3bHqJsg3y0Q9c9ZIVOIdPQB8qM8xojHOOFIyvnVg1Mq7_GPYN4EwOJFT2yF82-NHzW7zM0DjjzOsVYOE2Oq3TWvJF84C2L6FxDUwqRte-Q2zqvB0dR0JSjH0p1AXg2i6YBwCW5DCH6oe9BtsRUFKhH_K2UL4BBOznI-SXPZf9bfSKDA5zOirfVkM_l_4EZCP10F5KiDQuIFjL6TMVHEbcEOiWM_FVr_S_P23VCNjsq-2Oxcf5gFlUYTgoF2-Ok-f6tz564LFr9Iv6wwCI53w1i4qXxhN1M54-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsyPp2ZNmaFIgmE6CnCe8Hlxo97bj7BxDaUfXUN-Vhg6zPUIJja8qt_fnI1K-gx2qjSbXcsIOibc4eWLoDZ3rT8KEYi1-rC3JNXW0Rr3pdZJ4uuB2o6SlcSste4MGBKs7C7IiT_PUfmUNCFucpJhjjjXM9c5xD9oar2rEXpkO10G2v1ta_8zHDGqRyer8XulN9p9Pn9sPsYUiVJmEnq8aJZEjk-rKv43GjHvjO4xuYEmVAgQKOGeX4CqFW85JbDVu4nISGOVM3wPNjTUxPp8hBt9MuYxE9eNt5A58LvSNm9_lhE6yU-e5E9WPPJVd2pczrf69Ti6HaXvO5wQsMOo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtF_83MOfCQNO2jJckGS4Rybn6c3fneFEDeHkXaPlc3lbDoUksAgrdJiWExGVL9omdic3nC-Pw0YVzTCZGlMfVeyCqGLoch04BU1-QbPq7C2RWTO8rSl4j-diEyEademAaqqk9tE2lgVDni0OIInpCYYNLUL6Zqf8RlkLu1JRDEwMH2bq0mplA8dJBeIji0n5Kt4JbbQeLSuVJkjF1oElAYa9WhUrVjhxZ7rGFvJIa3bi7rw7acr_yuy9UU9zaW7gyFM4ZG8m9ZtFBmLjwXfQBf77Bbzp54p0i_ugml9H_N0QGMM5Rv4tw-Zi58OFomNDPlycvda-5UfnXN8ALlT7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lsWZeGF8oWtuo2q6eFU6lem6QKnmiAowfqBhbbbbmY_UxC61YvbvrDYmv-5JEM1FfKWW7QdQGdLra94mNbNl_9Y5bhcbV0zI_Jtyp-k6NI1JPgNXAWDu0XPhGfBjJuz9GRNTEKn1JdVM2gi9MMxX2K2eQQU0oYpAO4CH80BIO9_v7Gzkhrs4M8swqiMd0RXhEOpZzGVWxFwWUi4ymCR-6Y7EgFi35dEwqT1vnP0rav0Xbplbl3oQb0705fqaEVt0SfC-gYIthqYYqOyg719ZJR3V-acnBFqogn_Lo2ZiY9Mbf7ijdiArtiqIy-90RDwx1iRAgnpIRvDfxbu5L1JGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qb6qBVAtPd4XAyfF01sbIgGu5m2zvkj_lJ4IHBb5sW_wMsEm1sEkEBrLNrFlor1wO2I2xhD6mF0t4V8He_fR9-EnZw6td3qAeUOk3yKmSsaq71nzCr5tzI1Pb_n30n3EmPfBmBk4PW5jvBRmLOvD_zVq_S8MwQQ3ZRCP5AK5Uz1ghVxN4KgB-isJG_fUvVoYls15VJ5o5PWCAISkGruVCXSmHRf2w4CPd2eQ9idHdOYsh6S4-VL_G4HLA8Oh9zN1tE37AHOPpTvullfmwgoPdFSVqv7IONuOuW1i5wOu2a_ZI9ErTkulg5dyXpiErWeAXq4C6136NC70UfPJ2Xqi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g61KhT5iFVy6GZWVyGc5XPcCnmBYxisS0rCgNawH7P5zOI4mNrN9bGBeFFYt8Fw8d1OvitJn_ea9iw1fIIKFfpZ0qvTGG15HFl5HG_G57F84o1klCDw1rGfC1TFWSBMHc5wi2M5FMNGIFdKrw7Q0Muf6DjOriE4mGa9IuUIAjoWCXnvlvCoe3wxtwTuYpf_2u3W_mwbmXGnPHsD1SQKeLWJQLWQ4oBlaBzBybEReKhJTtCZrhNC_JPbWH1aAzE-ECVM0aaZRVYC4QV4h-SfdkdPMAGZakwjOPFijoFZ0BXYXobo92CPLDu-FWTo9R7vwspbbDT6MwVUuMUw-FlmvXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RRsQPtxc7qpVkxDbjQjn5620C2nJFNr0gcic9hTNujrjhKEOxp95zFF-9NRL0smNIDDqFiSa672ojD9d4GyQYB1FpaYLZ45-992XdJNZwbpYD5-QeZQay9UQVF2ACEyHMZ6Bjt1AZmb4cg_Arzsup1WtFxQUEtLAYRZcCR0fHSRR_9wftrhNaqO-R_m6fKL5brQ6CfOg88cE8yCkuo0uf63aBz2Yn7wBoWEi3oB2DXIUMdXt-U1VtrSR1jM3CQ3IWbB2TlteuRAWrLVe5D6rn_kSLDBc5Crl6MAyaMjN1jH9h2UywanWC5mgnThJmFxlXzegenlx8KbbXnZj2RFaSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RRsQPtxc7qpVkxDbjQjn5620C2nJFNr0gcic9hTNujrjhKEOxp95zFF-9NRL0smNIDDqFiSa672ojD9d4GyQYB1FpaYLZ45-992XdJNZwbpYD5-QeZQay9UQVF2ACEyHMZ6Bjt1AZmb4cg_Arzsup1WtFxQUEtLAYRZcCR0fHSRR_9wftrhNaqO-R_m6fKL5brQ6CfOg88cE8yCkuo0uf63aBz2Yn7wBoWEi3oB2DXIUMdXt-U1VtrSR1jM3CQ3IWbB2TlteuRAWrLVe5D6rn_kSLDBc5Crl6MAyaMjN1jH9h2UywanWC5mgnThJmFxlXzegenlx8KbbXnZj2RFaSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
