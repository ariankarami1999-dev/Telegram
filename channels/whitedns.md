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
<img src="https://cdn4.telesco.pe/file/tZg1VIW4247u8vUhhWBdQ_Ep0XnwQM3lFQxT-O-zfWhvndWYratF_XtY_em-iRuZ6aSv-GtcZWg2HbJ7HVNoWdI00PuqQWubssiC2xMlUya0CP3tRwE2GegeneB9LuHcol__ri2N6rpmkjrn2pHRVmJdY5GAVcHKO9dzgLxPifarjaXO6henZRES4P4uvgY7xbvM1yv_gVqHDvKokCJXtcCjevU_3wMyLSyOL5dZk89TA8itI6r7R2rEHsszFjANZf6RREOt3zwjVw1-3vqP-E4LGFkuY-Laz01nw8cITe9cU37FQxxJOIKDg9N50hzEceb_Wp44Pki9uC_HKHv-tw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 109K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 19:05:58</div>
<hr>

<div class="tg-post" id="msg-1325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-poll">
<h4>📊 از چه دستگاهی استفاده میکنید ؟</h4>
<ul>
<li>✓ اندروید</li>
<li>✓ اپل</li>
<li>✓ مک</li>
<li>✓ ویندوز</li>
<li>✓ لینوکس</li>
</ul>
</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/whitedns/1325" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FuzQHY8xE8dKmiRr7wcblYFuTIbJNzScfYDpG-DVQa0GUXa8kV8T40pVjNXTGueGDbIn_OkgGk1mAMw0k-mVb1vPp3NA1LKupkyUkZa4_7uRJzFbh9hJjdkZW20kzLbjcmo9aNeyMFPkGNejvKsLBKY4fsZed9k-t9AAvoCm-0OFupANFreg4CG6ozSVh-qig8YGXN4-XgO28cyHyDn0ULW51fp4DIFEx1NuRHidsxxjEGBqUzzIaN7ae-lZX40XqMHgcMEwMIipYAZqpcxmMYUJvdooNAz_eerWpc1zZR5PaOngzehPVDH7uyTMS1fny7UEOLGJHF1E683KAfI-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/whitedns/1324" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوستان عزیز، اونایی که Aether واسشون وصل نمیشه، یه زحمت کوچیک بکشید:
📱
✈️
چند بار گوشی رو بگذارید روی حالت هواپیما و بردارید تا رنج IP‌تون عوض بشه.
🔄
اونایی هم که با وای‌فای و مودم متصلن، مودم رو ۱ تا ۲ دقیقه خاموش‌روشن کنن تا آی‌پیشون تغییر کنه.
🔌
⏳
اینم یادتون نره که ما تو ایرانیم؛ سیستم DPI و محدودیت‌ها روی هر سیم‌کارت با اون یکی فرق داره، چه برسه به منطقه به منطقه و شهر به شهر!
🇮🇷
🚫
اینجا خبری از اینترنت استیبلِ خارج نیست.
📉
اگه این کارا رو کردید و پروتکل‌های مختلف رو هم تست زدید و باز هم وصل نشد، یعنی اون کانفیگ کلاً روی خط و منطقه شما جواب نمیده.
🛑
یکی دو ساعت بعد دوباره امتحان کنید یا برید سراغ VPN‌های دیگه که با اپراتور و منطقه‌تون سازگارترن.
🚀
🌐</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/whitedns/1323" target="_blank">📅 12:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1322">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-poll">
<h4>📊 با این لینک موفق شدید عضو بشید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-text">https://t.me/+FE3VusXUmuE4Yjhk  در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/whitedns/1322" target="_blank">📅 12:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1321" target="_blank">📅 11:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lcoK__w-jnWgC1zmXBMY6YvrMjeYK0Gk3FUW_jxNTdIocgvz9qiv3Q6V4b2lHMgYWiR0SIY264RZRagE_rWsDFVHwGBn6NhX1nwlDDq6dy-qd9nk9JxfMwPsIYpRpPMkysUM3X8NcRCRfj6aNjlYNTlTWSpEZfz1aVNT9qZnyD8aUQezOdusjKyT0iOR-d-F0gg0FyOguZzQId9Q7vjmEk5MdEM_P5I5i36zoNcYcQMYAhZGM24bRx1vD5cS4iHyG_3gWdp9V_1Yo_-_30p35QQJ-V7RV9rx6Rnu6yAXEXArRu2GlUcP7FfQcUlFBn2NdYEhowsSWnidlPdjhhzeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/+FE3VusXUmuE4Yjhk
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/whitedns/1320" target="_blank">📅 11:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1317" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1316">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سلام دوستان عزیز.
راستش ما قبل از اینکه بخواهیم نسخهٔ جدید ۱.۲.۲ پروژه اِتر (Aether) را منتشر کنیم، ۱ روز گذشته را کاملاً درگیر تست، آزمون و خطا و چالش‌های فنی بودیم. خیلی از کاربران از ما خواسته بودند که قابلیت انتخاب کشور را اضافه کنیم و خودمان هم خیلی دوست داشتیم این کار را بکنیم؛ اما بعد از کلی کلنجار رفتن و تست‌های مختلف روی اپراتورهای مختلف، متوجه شدیم که با توجه به ماهیت فنی این کار، عملاً چنین چیزی نشدنی است.
برای همین تصمیم گرفتیم خیلی روراست و خودمانی با شما صحبت کنیم و بگوییم توی این مسیر آزمون و خطا به چه چیزهایی رسیدیم:
### ۱. چرا در پروژه اِتر (Aether) نمی‌شود کشور خاصی را انتخاب کرد؟
پروژه اِتر (Aether) سرور شخصی و اختصاصی ندارد و کارش این است که شما را به شبکهٔ عظیم WARP کلاودفلر (همان شبکهٔ معروف
1.1.1.1
) وصل کند.
بزرگ‌ترین مانع ما در تست‌ها یک مسئلهٔ فنی بود: آدرس‌های کلاودفلر از نوع Anycast هستند. انی‌کست یعنی چه؟ یعنی یک آدرس مشخص، هم‌زمان در صدها دیتاسنتر در سراسر دنیا فعال است.
یک مثال ساده بزنم؛ شمارهٔ ۱۲۵ آتش‌نشانی را در نظر بگیرید. شما هر جای ایران که باشید این شماره را بگیرید، به آتش‌نشانی شهر خودتان وصل می‌شوید، نه تهران یا یک شهر دیگر! حتی اگر عمداً بخواهید به آتش‌نشانی شیراز زنگ بزنید، باز هم شمارهٔ ۱۲۵ شما را به نزدیک‌ترین ایستگاهِ خودتان وصل می‌کند.
آدرس‌های WARP هم دقیقاً همین‌طور کار می‌کنند. پروژه اِتر (Aether) به هر آدرسی که وصل شود، در نهایت این سیستمِ مسیریابیِ اینترنتِ اپراتور شماست که تصمیم می‌گیرد ترافیک به کدام دیتاسنتر برود.
*   وقتی اوضاع اینترنت خوب باشد، معمولاً نزدیک‌ترین نقطه جواب می‌دهد.
*   وقتی مسیرهای بین‌المللی شلوغ یا خراب باشد، سیستم شما را می‌فرستد سمت آلمان (فرانکفورت)، آذربایجان (باکو)، ایتالیا (میلان) یا هر جای دیگر.
توی بررسی‌هایی که قبل از انتشار نسخهٔ جدید داشتیم، دیدیم وقتی مثلاً لوکیشن روی «اتریش» تنظیم می‌شد، پرچم اتریش نشان داده می‌شد، اما خروجی واقعی اینترنت کاربر یک کشور دیگر بود! در واقع آن منوی کشورها فقط یک برچسب تزیینی و قشنگ بود، نه یک انتخاب واقعی. ما هم چون دوست نداشتیم توی پروژه اِتر (Aether) ظاهرنمایی کنیم یا آمار دروغین به کاربر نشان بدهیم، کلاً حذفش کردیم تا همه‌چیز واقعی و شفاف باشد.
---
### ۲. چرا ویژگی «اتصال فقط به لوکیشن‌های غیر از ایران» را اضافه نکردیم؟
شاید باورتان نشود ولی ما این قابلیت را واقعاً کدنویسی کردیم و قبل از نهایی کردن نسخهٔ جدید، آن را زیر تست بردیم. اما خروجی کار روی اینترنت ایران اصلاً خوب نبود!
منطق کار این بود: پروژه اِتر (Aether) وصل شود، آی‌پی خروجی را چک کند، اگر ایران بود قطع کند و برود سراغ آدرس بعدی. اما مشکل بزرگ کجا بود؟
وقتی اپراتور شما مسیرهای خارجی را محدود یا فیلتر می‌کند، تقریباً تمام آدرس‌های کلاودفلر به دیتاسنترهای داخل ایران هدایت می‌شوند. در این حالت، پروژه اِتر (Aether) یکی‌یکی آدرس‌ها را تست می‌کرد، چون خروجی‌شان ایران بود قطع می‌کرد، سراغ بعدی می‌رفت و در نهایت بعد از کلی معطلی می‌گفت: «اتصال ناموفق». یعنی عملاً به‌جای یک اینترنتِ وصل‌شده (ولو با آی‌پی ایران)، شما کلاً قطع می‌شدید! درست مثل کسی که چون فقط سوار تاکسی سفید می‌شود، تا صبح گوشهٔ خیابان در سرما می‌ماند!
تازه یک مشکل دیگر هم هست؛ سرویس‌های تشخیص لوکیشنِ آی‌پی همیشه دقیق نیستند. خیلی وقت‌ها یک اتصال کاملاً سالم و خارجی را به اشتباه «ایران» تشخیص می‌دادند و پروژه بی‌دلیل آن را قطع می‌کرد. به همین خاطر در آزمون و خطاهای قبل از انتشار متوجه شدیم وجود این گزینه فقط باعث خرابی اتصال و اعصاب‌خردکنی کاربران می‌شود.
---
### ۳. پس الان پروژه اِتر (Aether) دقیقاً چه‌کار می‌کند؟
ما در این نسخه همه‌چیز را هوشمند کردیم. حالا هستهٔ پروژه اِتر (Aether) در چند ثانیه کل رنج‌های WARP را اسکن و پینگ می‌کند و به بهترین، سریع‌ترین و پایدارترین نقطه‌ای که در آن لحظه روی خط شما جواب بدهد وصل می‌شود؛ بدون قطع و وصلی‌های الکی.
البته اگر کاربر حرفه‌ای هستید و دوست دارید خودتان دستی همه‌چیز را تنظیم کنید، هنوز هم می‌توانید از بخش تنظیمات، اندپوینت دستی یا رنج آی‌پی دلخواه خودتان را وارد کنید.
یک نکتهٔ بسیار مهم برای آرامش خیال شما:
خیلی از کاربرها نگران هستند که اگر آی‌پی خروجی ایران باشد، امنیتشان به خطر می‌افتد. اصلاً این‌طور نیست! حتی وقتی نقطهٔ اتصال شما داخل ایران باشد، تمام ترافیک و داده‌های شما کاملاً رمزنگاری‌شده است. مقصد نهایی این ترافیک، شبکهٔ جهانی کلاودفلر است و هیچ‌کس در این مسیر نمی‌تواند اطلاعات شما را بخواند یا ببیند چه کار می‌کنید.
آن نقطهٔ ایران، فقط و فقط مثل یک «درِ ورودیِ» امن به اتوبانِ کلاودفلر است، نه جایی که اطلاعات شما در آن تخلیه شود. پس اصلاً نگران امنیت خود نباشید.
---
###
💡
حالا چطور آی‌پی خود را به خارج از ایران تغییر دهیم؟ (دو راهکار عملی)
اگر به هر دلیلی نیاز دارید که آی‌پی خروجی شما حتماً روی کشوری غیر از ایران قرار بگیرد، در حال حاضر دو تا راهکار کاملاً واقعی و تست‌شده برایتان داریم که می‌توانید از آن‌ها استفاده کنید:
*   راهکار اول (سوئیچ بین پروتکل‌ها): تنها راه طبیعی برای تغییر آی‌پی این است که داخل تنظیمات پروژه اِتر (Aether)، بین پروتکل‌های مختلف سوئیچ کنید. در این میان، پروتکل وارپ (WARP) بیشترین احتمال را دارد که شما را به یک سرور غیر از ایران متصل کند. این تغییر پروتکل باعث می‌شود روتینگ اینترنت شما عوض شده و در نهایت به یک دیتاسنتر خارجی هدایت شوید.
*   راهکار دوم (ترکیب با سایفون): شما می‌توانید از قابلیت «حالت پروکسی» (Proxy Mode) در پروژه اِتر (Aether) استفاده کنید و آن را با برنامه سایفون (Psiphon) زنجیره یا ترکیب کنید. با این روش، ترافیک شما از تونل پروژه اِتر (Aether) رد شده و در نهایت با آی‌پی خارجی سایفون خارج می‌شود که تضمین می‌کند آی‌پی شما به غیر از ایران تغییر خواهد کرد.
@whitedns</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/whitedns/1316" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hJdImCp7erGuz0NZbsrOhhWe9_A3SvXwwgYXp_2NV9QYT-F-eXTWTC0smsq_ubsZ8h9koeJBTkr0K_TLmIjHkkpEue8pWQ6ma75o-PQlJLbhZq41rllyKyzOASk12I1jVRmz1CgdECHPTEQhDqZFpQ0IuA6KQMW4jmV-uNMgCJYktiODa7XnjJfGy_d-pfDgi3jAk7LVtAq-LJiDZc6RGuR8dPgsbv-7lRxrZMRAVPbdETRcXe0NndI60-26Shc0j8-4AQQbqooN5NIZkw7siqovQ0XEYPr5W6utIItm-iMm9gezKBl_5DW5i3beVOFeoug7hkUagZ-exABo-P91-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1315" target="_blank">📅 10:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/whitedns/1314" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/whitedns/1314" target="_blank">📅 04:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1313">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IIOeWHwE8meEv1Zl9GKNruXJ1iLsrStYVbqlJEQvUd4JoR8BYlIgW7HGNQ1O3vJgcC7bqqn7kqZpYwdtlgqjDpDpNtKhSTxUKeiDL-K0IsYH6ciAilbGSxviyiyYY5umcE7M8dnDdWkJa4LYnyA7krOSiHxQUlYNqvcN85Drfvxp-KtNt79Z9Gboa2jGQxSk0Lg37a9ZhA90uQiu1rZYnB_Rl-lQYYAXVHbt2XkZX9ZlwskNCC3TAByAAHUoScSKurWOVIjJSy4p5x0C3Du-ZJKmaZFWZbrzS9fl4yeswwoSciWjzPhXBN_Q51oPDCCg96uPkT5IcKF9A6tQp-1RpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
هرمس رو با گوشی موبایل روی VPS رایگان و تلگرام اجرا کن! + آموزش بکاپ کامل از Hermes
⚡️
دستورات نصب استفاده شده در این ویدئو:
https://t.me/MatinSenPaii/4683
⭐️
توی این ویدئو:
1- بهتون یاد میدم چه شکلی با گوشی آیفون/اندروید/لپ‌تاپ، هم Hermes و هم 9Router رو به رایگان روی سرورهای Railway بالا بیارید.
2- وصلش می‌کنیم به تلگرام و از مدل Mimo رایگان روی OpenCode استفاده می‌کنیم و API 9Router رو ست می‌کنیم.
3- به طور کامل بهتون یاد میدم که چه شکلی می‌تونید از اکانت گیتهابتون استفاده کنید تا Hermes رو بهش وصل کنید و به راحتی، هر چند ساعت یک بار از تمام داده‌هاش برای شما بکاپ بگیره.
4- به علاوه روش ایرانیزه شده‌ی استفاده نامحدود از کردیت رایگان 5 دلاری Railway
😂
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api و سرور رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/whitedns/1313" target="_blank">📅 04:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1312">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سرور های اهدایی و فعال WhiteDNS پارت ۲ داشته باشید برای زمان قطعی (کلیک کنید روش کپی میشه)
Server #11 thx to Araskhatare
♥️
Location: Germany
🇩🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6nwn4eqIDIgICB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiZGUuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI0OWUzNDlhNDc2NjQyYTg4ZTQ2NDVmYTJiZjgwZjhjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #12 thx to Araskhatare
♥️
Location: Israel
🇮🇱
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4exICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI2MmIyNjQ0NzU5MjU4OWE0NmQ1MzdlY2M5NDc3MzY2NiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1312" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1311">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">10 سرور اهدایی و فعال WhiteDNS داشته باشید برای زمان قطعی (کلیک کنید روش کپی میشه)
Server #1 thx to Coreforge
♥️
Location: Turkey
🇹🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7nwn4e3ICAgdGh4IHRvIENvcmVmb3JnZSIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFub255bW91cy5vYnNlcnZlciIsImVuY3J5cHRpb25fa2V5IjoiYjI3NTAzOTE5OWIxYzhjOSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #2 thx to Araskhatare
♥️
Location: Germany
🇩🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6nwn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI5ZGIxNjYwMmM4Yzc3NjcxOWJhZDE3ZWZjOWQxM2E0NCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #3 thx to Araskhatare
♥️
Location: USA
🇺🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7rwn4e4ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6ImVkMGNlZjE2YjcxNTNiOGQ4MzVhMzI3ODYxNTk3YzY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #4 thx to Araskhatare
♥️
Location: France
🇫🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6vwn4e3ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImIuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyZjAyZTNiN2NiNTg3ZjM4M2U0MWM0MmU4ZWYzYWY2MSIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #5 thx to Araskhatare
♥️
Location: UK
🇬🇧
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6zwn4enICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJkYmYwMmYyYWVmZmQzM2QyNDY0M2ViODM4OGY2N2Y0ZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #6 thx to Araskhatare
♥️
Location: Ireland
🇮🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjY0MTVlYjhmOTBmMWQ0NjY1N2JjZTljYjc5MTg2NDY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #7 thx to Araskhatare
♥️
Location: Sweden
🇸🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7jwn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InEuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjFkYjFiMWIyNGM2N2IxNzYwOTAzMmNjNDdhZmRhMzZlIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #8 thx to Araskhatare
♥️
Location: Spain
🇪🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6rwn4e4ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Im4uYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjU4MTcyOTA4ZGFhNTAxZTk0MjUzNWU2NTY3NzkwM2ZkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #9 thx to Araskhatare
♥️
Location: Italy
🇮🇹
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4e5ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imx5LmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJkMzM4NmM1MzkxZmRmOTJjMmNkODM3YmFkZTBhNGVjYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #10 thx to Araskhatare
♥️
Location: Brazil
🇧🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6fwn4e3ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlsLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJmNzk4MDAyYzlkMTkxMTg4M2MzOTE2YTQ4ZTkzNTVkMiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1311" target="_blank">📅 22:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1307">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162866f874.mp4?token=tpGyr5oRO6ZVkDqNh7p3FZU9rbhg-a3pskqtZWJCPZwCWt0V0CQGZbdAoPd5-hV4m_l7nxDgbyEyBW7113sv8nonennCf4WXq7YymDxmpIV8uCFHtaH0vnPe6iM6roA2F10KElKOXUiwFKdyIvw7BHDTaONYtMgYw57NMna6DTFqkQZPUk3R6VmeFml5A_Lkf5wUBw71x1xqInWGilJs8TSF0G3TZpWhwMwNuJESC0IVC_1AP2MSnkW1JeZrT_AMmazqDoeGJPFtMMvvLY1QIDIo1BOLpO-IUKGpI5f-jtMrQMsHl0ZzuVDttu3IbPOTx5KPvcO51HtOqPGOOUJ2CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162866f874.mp4?token=tpGyr5oRO6ZVkDqNh7p3FZU9rbhg-a3pskqtZWJCPZwCWt0V0CQGZbdAoPd5-hV4m_l7nxDgbyEyBW7113sv8nonennCf4WXq7YymDxmpIV8uCFHtaH0vnPe6iM6roA2F10KElKOXUiwFKdyIvw7BHDTaONYtMgYw57NMna6DTFqkQZPUk3R6VmeFml5A_Lkf5wUBw71x1xqInWGilJs8TSF0G3TZpWhwMwNuJESC0IVC_1AP2MSnkW1JeZrT_AMmazqDoeGJPFtMMvvLY1QIDIo1BOLpO-IUKGpI5f-jtMrQMsHl0ZzuVDttu3IbPOTx5KPvcO51HtOqPGOOUJ2CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش وصل شدن به این روش شیر و خورشید در Mahsang دوستانی که بلد نیستند.
1-اول به داخل mahsang برید
2-سه خط سمت چپ رو بزنید
3-قسمت تنظیمات سایفون رو پیدا کنید
4-پروتوکل روی cdn fronting قرار بدید(دکمه ذخیره یا سیو رو بزنید حتما)
5-برگرید صفحه اصلی گزینه F رو بزنید
6-حالت فقط سایفون/only pisphon رو بزنید و دکمه کانکت و تمام
حالا شما رایگان و با سرعت بدون نیاز به پیدا کردن ip به اینترنت آزاد متصل میشید
🔛
لینک دانلود نسخه جدید
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1307" target="_blank">📅 07:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rMftUc6S4z-DZCp2Xfn4mYdnBZCRcA7RxJqesKUseiWoo00oO_f2cz1v3LrzO_Yj9Gu0cN2C5ikM4XRdH2E9qyyF5RyWxz71gIsLdsPMgpeu4TZXDYHhdZqv4OR8zJAmJEci5A2ECnxXMCMczNziFYfUuWlgBaH2_y0W0L38oG8eSup4OIwBRgH-mt9cfZIWovsmqfmzpyFYeq14xWZf6NWJ0xhW4ukAlqU9jlkhKRtkcmZrzV9qH4UPfkatfz-bk0XT1oYVjACHop3t-RTKCgdlW09_x_ufUG3Jv7k_hhKUbsN2URVWOG2eXXh04slCbjceG4yN8gPyVL-qI9mT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/whitedns/1304" target="_blank">📅 05:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📱
آموزش کامل اپلیکیشن WhiteDNS منتشر شد
سلام به همه دوستان عزیز
یک ویدیوی آموزشی کامل برای استفاده از اپلیکیشن WhiteDNS آماده کرده‌ایم. در این ویدیو، تمام مراحل از نصب و راه‌اندازی اولیه تا اتصال و استفاده صحیح از برنامه، قدم‌به‌قدم توضیح داده شده است.
در این آموزش با موارد زیر آشنا می‌شوید:
• نصب و راه‌اندازی اولیه WhiteDNS
• اضافه‌کردن و مدیریت Resolverها
• اسکن و پیدا کردن Resolverهای معتبر
• تفاوت حالت پروکسی با VPN کامل
• نحوه اتصال از طریق DNS Tunnel
• مشاهده وضعیت اتصال و میزان مصرف ترافیک
• مدیریت پروفایل‌ها و تنظیمات برنامه
• نکات مهم برای داشتن اتصال پایدارتر
https://www.youtube.com/watch?v=tz8cj7HzHVI</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1299" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HQAmaBzTCLFs9nReckFdIi6TnkTENRAayv7Gzg18397ndM7cP3YKyNSho_goaCmyHNctgmPM9lPfRL77JbjyYfYzwq6mjBnwbGX3L5zHHB8xE6aUAve3Gv-BbqD9rMAWOlPA1U23sajQTVRosmR8GFI2Y7olbFZajRI-zheGhyiTm_X0Sb-J-_3pySOdPc4Pp2PIBGDsaXR-__2kFrx7CgKdfpl2vSQAXnkZDnd6OdmDOi_U9EBnswhhhYGQKG1sdwLvCksB5q3_o1iV2ZJq7otdco3aYXLjMT_9rEoaJSybI1IhdWIw6l6o34eT4viO3BrRZNEje8ntCowLXELTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1298" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UiNkh5EsmIMX9yzcQlBirh8BhDOrY03R9AJoeq-K6mP7cM-zz6madWzENFcMX7JwE4Z0tgJZwkn5fqulWP4dy0p5lD32i_5aoTzvVYNcmS0RPW3wLS1xf9wOto15Co1q5IaTA6YLyoHpkpF3pAfyS3-SInamRSiLW6lIJP26IPfEE9a53iNzXACaLuh85EgUHADKXeh_mVybRUx-uJc7GHjVWqxqfYqpu736QpahtOGjcCm_iGKjxOsR85rjpq33BEqJgTbkvT4bBAhZej9x4mXGW2ZA3_jjlsimWIvUSR3dVYspPNpFoQZ7BND_Jleutf0--zMAv_JtVNDWh0JMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1297" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1294">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخهٔ جدید Aether منتشر شد! (v1.2.1)
نسخه قبلی رو حذف کنید بعد نسخه جدید نصب کنید
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1294" target="_blank">📅 16:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1293">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XEZjxX6RYvDNW6O61TUnQipRIEhwxxwBvusiE1iYN3byhloe_NrOPSPp16k_Zkt7y75dZ1MlLcdFFJqNvN47dAqwy0D7_IFPasoPGsKHfH2HwPDzc1ZBdhvgWpCZLpSkcDPTxMlTaEZbq3vD483GjRKtRYf6EH4RZEqt6So5p9kwf7xJANUkVvylApKm5VDZ3829VVe6ycCbWXaKdVWXaurNmeEo1BelQtXhTYiaX6Q8gMvrTNwC8XmNKtGzCn-pOEDslS4ZeYlt8gOBiuLVpcXDvO0NGqCKcckjct9AdIG5tW-NpXHpeqZTux-QZpPTUzbEKYW3p7wOfDrPMvnihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخهٔ جدید Aether منتشر شد! (v1.2.1)
🎉
اگر به دنبال یک اتصال واقعاً پایدار، فوق‌العاده سریع و بدون نیاز به برنامه‌های جانبی (مثل v2rayNG) هستید، نسخهٔ جدید اِتِر موبایل با قابلیت‌های شگفت‌انگیز برای عبور از سخت‌ترین فیلترینگ‌ها آماده شده است!
🔥
تازه‌های بی‌نظیر در نسخهٔ ۱.۲.۱:
⚡️
موتور هوشمند واقعی (Smart Auto):
برنامه مانند یک مهندس شبکهٔ حرفه‌ای، ابتدا DPI شبکه و وضعیت اختلال‌ها (مانند فیلترینگ SNI یا خفه‌کردن UDP) را تحلیل می‌کند و سپس بهترین چیدمانِ اولویت‌بندی شده از پروتکل‌ها، سطح مبهم‌سازی (Noize)، فرگمنت و رنج‌های آی‌پی را برای اتصال گام‌به‌گام و کاملاً پایدار اعمال می‌کند.
🟢
«متصل» یعنی اتصال واقعی!
دیگر خبری از کلمهٔ «متصل» فیک که هیچ سایتی را باز نمی‌کند نیست! برنامه تا زمان دریافت هر ۴ تیک سبز سلامت (پورت، هندشیک، اینترنت و آی‌پی) در وضعیت بررسی می‌ماند تا از اینترنت واقعی مطمئن شود.
🛰
نمایش آنی آی‌پی و پرچم:
با موازی‌سازی سرویس‌های تست سلامت و تشخیص IP، این فرآیند با سرعت بسیار بیشتری انجام شده و بلافاصله وضعیت موقعیت جدید شما نمایش داده می‌شود.
🔄
آپدیت آسان و مستقیم (مشابه تلگرام - آزمایشی):
از این پس برای دریافت آپدیت‌ها نیازی به سر زدن به گیت‌هاب ندارید؛ نسخهٔ جدید مستقیماً درون برنامه به شما اطلاع داده شده و با یک کلیک دانلود و نصب می‌شود.
🛠
رفع ریشه‌ای تداخل‌های متنی زبان فارسی:
به‌هم‌ریختگی ظاهری و راست‌به‌چپ اعداد در فیلدهای حساسی مانند ip:port و اندپوینت‌های دستی کاملاً برطرف شده است.
🔒
امنیت بسیار سخت‌گیرانه‌تر:
تأیید نام هاست در اتصال‌های TLS (بستن راه حملات MitM)، حذف لاگ‌های موتور در نسخهٔ نهایی و مسدودسازی ترافیک ناامن HTTP برای محافظت حداکثری از اطلاعات شما.
🧹
دکمهٔ بازنشانی سریع تنظیمات:
با تنها یک لمس، تمام تنظیمات پیشرفته را به مقادیر پیش‌فرض بازگردانید.
لینک ریپو :
🔥
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1293" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1291">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1udIA3ZnQgAEZOeuo6dnKi0isfEAQNOB5g0EeU5JTFrfaBJKRfnN16e2OAUmZP-Cc40FfF7eVLKQKJOGGcGXtZYXZ0KMylHoPR4xlCGQsu6C0sT05Zu7nO3mazwTaL_EK2LGi7B82064HwNANO1iB3D7mvs2OFG9kBd4O8aV2lxWI3DNQoX7sq_K3WuqSEhgusaj4ZdJDDuRrPibbLRWGtGZdAvcvrDd9kHipAolGDP-JCuFeR6Z3vw3EF6Fy005QdzuZm1UkevtoiRNjaQCC1zdl9HefFbmlUk7dIy80tkBObF7dm8UENd2W06WPOysdlleXNo2vEHk2zKB6n2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/whitedns/1291" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1289">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنوا پروکسی | Nova Proxy</strong></div>
<div class="tg-text">🤖
ساخت پنل نوا پروکسی فقط با ربات تلگرام!
دیگه لازم نیست مراحل نصب رو دستی انجام بدین.
😎
فقط وارد ربات نوا پروکسی بشین، اکانت Cloudflare بسازین، توکن رو دریافت کنین و چند ثانیه بعد پنل اختصاصی خودتون آماده‌ست.
🚀
بعد از ورود به پنل هم فقط کافیه رمز ادمین رو تنظیم کنین، کانفیگ رو داخل کلاینت Import کنین و از اینترنت آزاد استفاده کنین.
📺
آموزش کامل مراحل داخل ویدیو گفته شده.
💬
اگر سوالی داشتین، داخل کامنت‌ها بپرسین.
🔹
ربات تلگرام:
@IRNovaProxy_Bot
🔹
وب‌سایت:
https://novaproxy.online</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1289" target="_blank">📅 09:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1288">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1288" target="_blank">📅 04:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1287">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1287" target="_blank">📅 04:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1285">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg0T5SUPw-EdHM3Ja8LJkGdAq-rQejfNd-75i4yDzYaorqvDzYOxaTmgabfFdQi2mfknyfCkUAfaECkspTlO9deq2cTeT5jwK_f5r7Hms4YmjKh-Nb53sDGaZA-zwItUWmZrbz_OPrWIkv3vuc3X8lxoVTTc6dYb8UudwwLvCjsmodMquPytrBDq55BrAmZXRrWM01mJbpySZIvQn0IHGg73h0mwqYv1TFzogzh5tINRM-qeNbijTkCqJUHKDf0wI0calaYr-ObPTn4G1bqY8z-eNkT1n_w5INrxELOr2VuOIO8Mfiljg_PU8lWbvH3WJWWMPUThTHk4rqK6Pz7bjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/whitedns/1285" target="_blank">📅 15:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1283">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یک ظرفیت جدید برای تست فلایت داریم که میتونید از لینک زیر استفاده کنید
🚀
📱
اپ  CoreForge  یک فیلترشکن ساده و قدرتمند برای iOS / آیفون که مخصوص استفاده در شرایط سخت، اختلال شدید اینترنت، اینترنت ملی و حتی دوران قطعی کامل طراحی شده.
https://testflight.apple.com/join/3htm1Whc
آموزش
🎥
📹
:
https://www.youtube.com/watch?v=filwdiPKN90
@whitedns
📢
🔗</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1283" target="_blank">📅 12:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1282">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/r6yeaodZwQCt52ZiZ6Hv_P9Q9NRC2pLXUf-OipjgaZkbmB_iCp5_p26igrk8nz91dl0lwCC1QbuqQPL7G3FUr211MhoIB2tQkKDQx5520ZStP43yrRhcXNOEDdY9foy9Xx8v6iF7Uh659VPU9jNJxDLxCZucBFMqpyuEG4-pDWcwwb71XhPyrJaKFsEpXlsJVm7R77sXdin_TJpVmTv_eAWjX4MOfkDWq0B-imPNy6eo-04PJk2ie_SIrCK2AFcOZo-6C4_8zklG8wQFMuBECL2fKBXEWCkOqzwyPgfuZuyde-O8t9s1xFo5jV3jinsw7wgxIK-dXz-tVINQXSjk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/whitedns/1282" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1281">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Eu_ksyet-Ndbpwot8C_4wHXr82OWZ1tlP9T79k5nKvKWkYG5lybcgDYVgaq714ukKBKf5yg8uEBWTZKGFWswxJ0xe5mSi-uZhRzNGbt1n_Dauygv3zk-xzNlLOcaQqx9fFYH2jM9lsetjTQoANSbYIhWYnjJNwBtzqJY93JdT4vjMU1cMz9dQmW37zR8PAmeFizs9zrso1ShmsSKYwupBVcoWzdJXcQS83iQ8iAtA7Ct1l5pH5PMjr2yn2k3VvzNXS9HThOmbd66z7771tF4dYZHfx0qn4ZJZwy9hIlczSE22Qo6tx62owM5_dKHfIsB9__kmYU7AeyRkzWY5r-Fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/whitedns/1281" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1280">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fR33tjuKXfYx2A_eyY6AQ0wxms45aDEirKduKnEsPTh8lPSeMmiyD5t7UVvG6gCwx0VtdDblxtyODT9epamGYDDos7nZgXU1m1NTecZd39zjvAO3pE9_21Lf8wCJ66v0vkLWC1LwXqUcwRQvknuVCYYjkgKqVIEgUYjUQ6GFpZOuFVyrZ06GmalKpdhS6JAvJNH5KmXgW6sNjh316LS5X5ij389DHB-liDwl-shY9XeVn4NHv1wNByNU7YGE4MvI9s9O2wN87TWvKIG3A6rPDlFJ91pp5iQ-shTwUJpDyZiKMrfvsvmvzErAl3kfOZ0YJVBKx2xQb-dQ0kWhkUCpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/whitedns/1280" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1278" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/whitedns/1278" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tmXF7L9Kjg1u-VajcrUo0KuW4ezgYNsQwtNRuXnPyzh43pHeGH2kORWGuL87r-tDLYvbqLe0T8jq0a6gsfA6XmDjvRmTOW8BIKu-IFpQt_wrdtvuJBKwW4E8pdtUAi8IE8i1ZkDo1YIhKuQTkGU3Z_6ggx4Md2b1985Uz_aKQdQ_1_QVzU7q6evxht0GKACidaXeTNESKKffjJ9KDnC2572oPXiRUJ_ZeZDn7odLzEZamcx1zGmwGgWSbWT34LXbZBFJgaNf_VDt7bIeHInmwlsjiMDyFkwyQkx4bm5KL1B54YSvq3ku5XW880fCEXW8HgTb9KqIBB9617PxmKI4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
تنظیمات اختصاصی whitedns
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1277" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📌
چند نکته مهم برای عملکرد درست برنامه‌:
1️⃣
حتماً فایل PDF راهنما رو بخونید
تا برنامه بدون مشکل براتون کار کنه.
2️⃣
وقتی متصل میشید، صبور باشید تا
آی‌پی و پرچم کشور
روی صفحه ظاهر بشه.
3️⃣
دوستانی که میگن آی‌پی ایران می‌گیرن و سایت‌های هوش مصنوعی باز نمیشه:
• یا چند بار قطع و وصل کنید تا آی‌پی غیرایران بیفته؛
• یا از قابلیت جدید
حالت پروکسی (Proxy Mode)
استفاده کنید و اون رو با سایفون ترکیب کنید. این‌طوری هم سرعتتون عالی میشه و هم مشکل هوش مصنوعی کلاً حل میشه.
💡
*نکته:* ترجیحاً نسخه
مودشده سایفون
رو نصب کنید تا محدودیت سرعت نداشته باشید.
https://t.me/whitedns/1261</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1276" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvBoiig1uo0LLqeG54DSBwIkni06oMaGE-BNSUNvPC6fVkzcKzSAoDCZEmbrnNGOyb5n5KQKHDNS_YqMppeEN-CRS-79XD2lRCEv49foznMgkH4jrPmVh8KOh42Cjg7xjLMuYN-O_M9UAoiUtcmjam1DHVOWgqQqwY1xhreE-5NOyPRVIrgqX3bowr8_RNF1HEDoDnaUM3CFEgUqkUVd1vDDet3S0MJr6m9COW17WOKXDYS2EgC8NTa-J3-NJX8BRh5HIeNO-FRt8ZAnepFOSJ9zQbdTlDa8VUCpT-uJjaNNLiL11Z8EFf-tqQBn73w5CU_oLNmnpp7TmbhnbFFpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/whitedns/1275" target="_blank">📅 06:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/whitedns/1274" target="_blank">📅 05:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1273" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1268" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/whitedns/1268" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1267">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgs92oD448o_2-wHAOfIOevkOHzJnV86oBpD2Mx3xqDOfh44BhZ7-nq6SMhCJlZZoW1OfguOVgV-UbmHRKX3qwKBzPu6IENTdF2XjNuBsFpk5IKAD1hogAwfC6WmMgy3zepur8Dv-dw5t0lb4Q7oMyWqQ-Rt77PmjtEWaEi87RAh1w2pGEHAE4sB7wOVItzKyADMaWLpi_BXZ7tWaxd92Im8bdul-mo-GjbHmiyAlfrs9pkipKkCw3EDhwgutnH1hiHHI_8m2yGX3F2vrYGM7CblQgcEAR7xIOor0DRGN98BTq_OCeNs9GYikyCf47wVeUhfUOos01JtIanF0lnbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/whitedns/1267" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1266">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اگر توی نصب مشکل دارید نسخه قبل را پاک کنید و این نسخه را نصب کنید</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/whitedns/1266" target="_blank">📅 05:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1262" target="_blank">📅 05:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VlGyNCvl6aF8azTgE_N8kn1msX7hQuM4OCwsMp_KQ-NN7QX-4Vt8CcXKLaEiJQ0K5L758rft2xpvaIA_ZIRe7ZL2ORg7AaLbrAiAb4g1IpTBxA0-GwEeqbiAcnNqozE73urD3XKpd6KJuXfAkfxDrHgjC9SJRVsIhWpibN-4JnhbBfjfvfl8FnfP0Z7s9B_eFxyIRXJgGk8eQ7z4qkAMg_ss3wCgAZp95ISHcBe7trFvcbpMIzb6pkRHWoda0GnJOEplL-niJNGSLNEtxsRMKYd_VdLhYEhJwepuhCua-obdzV8TziIxDYjZE1eDldhXOLROu8UOyFjs1I5o1c_yTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Aether
1.2.0
🌐
✨
(فقط برای اندروید )
آتر یک ابزار ساده برای اتصال امن و عبور از محدودیت‌های اینترنت است. برنامه به‌صورت خودکار سرورهای سالم WARP را پیدا کرده و یک اتصال رمزنگاری‌شده ایجاد می‌کند؛ بدون نیاز به خرید یا واردکردن کانفیگ.
🔒
🚀
📱
روش استفاده:
1️⃣
اینترنت را روشن و برنامه را باز کنید.
2️⃣
تنظیمات را روی حالت خودکار بگذارید.
⚙️
3️⃣
دکمه بزرگ وسط صفحه را بزنید و درخواست VPN را تأیید کنید.
📲
✅
تمام! بعد از نمایش
Connected
می‌توانید از اینترنت استفاده کنید.
🌍
🎉
مهم :
⚠️
برنامه روی حالت اتوماتیک اول اسکن میکنه و ممکن هست بسته به وضعیت اپراتور شما و فیلترینگ حتی تا چند دقیقه طول بکشه. پس صبور باشید و به برنامه وقت بدید.
⏳
💤
یک فایل PDF با توضیحات دقیق در مورد کارکرد و نحوه راه اندازی براتون گذاشتیم . کامل بخونید لطفا
⚠️
https://t.me/whitedns/1265
کد پروژه :
https://github.com/QW-AI-Code/Aether/
@whitedns</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/whitedns/1261" target="_blank">📅 05:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1259">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmOE9al-UeHmkUdVjhjO9Xq4M45e3_Ce-5wMoind6ekt3TVi5TSJVO-t5guDCZGbhq42tXTj6KAjSqmP0sI2Y3TUKy7WIXhj9UtNDnSrrluppO8b6Pgy2pmRJl_RbxK_3ZVuSMRoDCZMW4YR5uVCdAabDKFydOwJgDUmRKXtq34f0Wf29PKAaL9mRRVrYBPV9I4m0BfU5h2k6nX7YHyRgT6kIj8rNnfDxasvyYLT-4cflc4qcURIq9vL7EacmKahBcRVQjKLqO7z0ku-3sWXz7jPHXlnO2GJSl0ypupahQswBz1CyecqUFDaOdn9Rn4bYhl2L-5r7SsPcLZHbBjmdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/whitedns/1259" target="_blank">📅 01:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1258">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/whitedns/1258" target="_blank">📅 15:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👆
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1257" target="_blank">📅 14:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/whitedns/1252" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7AqARzXknerfc5mwGCoZHfVvch6AHYhrrJ0hNEJa8hK0BuKLKxJs5J1BLpAgrqYI1a6Z_vgpLiiJ7JXRmszJepzvKnUd5pe-eERzHc55ggWphp_vRSvuHUR2WnSnjNniH_F7HMqupqR8aLibOuF1uV19uJRMtkIi4mJA78zumVIjyVGkaPDsPGFxpu_j9IxBIRdmpDIKaaQZ_bZ42sm6LuZ2CC37XvAagS4fgYoRQ2Q9Y2Ec7yvJa3UJT37TWD07CdccXrLs3lI5COWgNO08ypwyHt830mGlq0wlG8l5eihbKoXRTeMDTUVAGTgg8zAL3fELiiVHuy-B93FVgRnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/whitedns/1251" target="_blank">📅 14:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آموزش آماده شد اما تا ادیت میکنیم، ورژن جدید WhiteVPN رو ریلیز کنیم چون آموزش رو با کمک اون ساختیم.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1250" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">همراه با فیلم آموزشی، درحال آپدیت کردن هسته WhiteVPN و اضافه کردن بهترین پشتیبانی ممکن از آپدیت جدید BPB  هستیم تا اتصال شما ساده تر و پایدار تر بشه.
نامگذازی اپ هامون هم داره کم کم تغییر میکنه تا کمتر گیج کننده باشه براتون
به مرور زمان همه اپ ها تغییر میکنند به نام های زیر:
WhiteDNS
WhiteVPN
WhiteScanner
WhiteBPB</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1249" target="_blank">📅 08:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">White DNS
pinned «
جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟
🔥
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1246" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-poll">
<h4>📊 جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟🔥</h4>
<ul>
<li>✓ بله❤️</li>
<li>✓ خیر🫤</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1245" target="_blank">📅 16:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/S2eqMML1wtPS6miFbh-YJJir0nzfppkoRW7h5994Miqh6FDPo9hUnOHCK1v279pWmrwP0JteOIkZzZe7xroevfcfwduAqHFMMQXG3r3T2bduxykj4j3gJALfpnujEk7xysq94J4kLQUwYwquQEvkrWBhV7BEJ9xHS-7WHSdIdC-vVteI5ggG2-cOftIpsEgVfW7auaP2TkvAiyf_T_angkwO_6TIeii1GKe0qry8pSiUthIjYpPXMU26n13baGgQzo1LicoSBLHloVUFTOXNXllcLPom_BDuS8sRp9hikby7leJTku3EVputYWkmXmk3HKpFzU2nLhffXZlVmQu_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
لینک ریپو :
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
لینک ویزارد :
https://wizard.bpb-panel.workers.dev/
@whitedns</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/whitedns/1244" target="_blank">📅 12:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1239">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/whitedns/1239" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1238">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToDRvKPW4NdXQBAdR_JvP6R9qD5U3JPXliyIpOTitEKxoxmr05qEyQts0DIi2k66zZLJueTpruLlJ1sET5LrtLsiTzsdffKDBhFCZ6u5JvQMpFQqjbtlJcDJK7HsuCNmF7TFCpzydcXLglMlRJ7X_lCX4EuJOm1XhQNBBpkkc30zNlAQUFf7LIDqiANwasm7mPUmR9uIke2yAc7ZoJjU5WDTpzEFPyMZ5MFaI9wLrK5lpHkTPEZZkMNWF1Fgbjkq7kXUhCb7InyoF29xWY5h29w0yZeJUmGo9k7Essbor01EIZBOYyNGJA8DIiTMaYiipt-MGmMK0SBj_zpcX_T-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/whitedns/1238" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1235">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.2 MB</div>
</div>
<a href="https://t.me/whitedns/1235" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تازه‌های نسخه ۱.۱.۰
🆕
اِتِر (Aether)
تایل تنظیمات سریع (Quick Settings)
— روشن/خاموش کردن VPN مستقیم از منوی بالای گوشی، بدون باز کردن برنامه. یک بار اضافه‌اش کنید: منو را پایین بکشید ← دکمه مداد/ویرایش ← تایل
اِتِر
را بکشید داخل.
اشتراک‌گذاری VPN با لپ‌تاپ یا گوشی دیگر
📱
💻
— از منوی کناری ←
اشتراک‌گذاری VPN
. گوشی شما یک پراکسی
HTTP (پورت 8118)
و یک پراکسی
SOCKS5 (پورت 1080)
روی وای‌فای/هات‌اسپات باز می‌کند. آدرس دقیق
ip:port
قابل کپی است و کافی‌است در تنظیمات پراکسی سیستم دستگاه دیگر وارد شود.
تنظیمات پیشرفته در صفحه اصلی
⚙️
— دکمه جدید بالا–راست صفحه، پروتکل، حالت اسکن، نسخه IP و بقیه تنظیمات را در یک پنل پایینی باز می‌کند.
آپدیت بدون حذف برنامه از این به بعد
🔄
— همه بیلدها از این نسخه با یک کلید ثابت امضا می‌شوند، پس نسخه‌های بعدی مستقیم روی نسخه قبلی نصب می‌شوند. نکته: برای آپدیت
از نسخه 1.0.0
فقط یک بار باید برنامه قبلی حذف شود، چون آن نسخه با کلید موقت امضا شده بود.
رفع اشکال:
پنل اشتراک‌گذاری VPN حالا بلافاصله بعد از روشن کردن سوییچ، آدرس
ip:port
قابل کپی را نشان می‌دهد.
✅
عنوان ریلیزها تمیزتر شد (دیگر پسوند "(build N)" ندارد).
📝
Downloads
📥
https://github.com/QW-AI-Code/Aether/releases/tag/v1.1.0-build.2</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1235" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1234">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید   درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1234" target="_blank">📅 11:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1233">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/I9y0x8OOOM6HWyYzOaaNhIGsyz67jXptUDZxiR1CXCGmBYZ8D94AaauKGp7ae1uuU1kzH7NLjVyvFdW6-xbiK6an30zpUmYAIdh3U03uJQkFr5-7GJFzF9zP0U-PWj-Bv48AyfUMmGc62VDqgotrqHIS2LSvLQ-QDfgltghncDOYCFX_vO3qR2S344f4pDa2--xh7gMsuqCtI0sWS-Io28jPh-IhyfUmE6POPd-tKMmBm06Dk0tf7zmEFUWqREvzvAWL7omHtVEO30BZjmz4aAhpiRqKZUANAKjIlqtsI4YYDWKnPCsSmrtiDlULR_Vs7z2VmIkHB7bqbHEN15FuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1233" target="_blank">📅 05:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1232">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید
درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور پیشرفت
ه WARP با تکنیک‌های ضدفیلترروز:
✅
پروتکل MASQUE (HTTP/3 و HTTP/2)
✅
تونل تو در تو WAR P-in-WARP (حالت gool) برای سخت‌ترین شرایط
✅
قطعه‌قطعه‌سازی ClientHello و مبهم‌سازی ترافیک
✅
اسکن هوشمند و خودکار بهترین endpoint
⚙️
۴ حالت اسکن برای هر شرایطی: Turbo
⚡️
/ Balanced
⚖️
/ Stealth
🥷
/ Thorough
🔍
📊
نمایش زنده ترافیک — سرعت لحظه‌ای و مجموع دانلود و آپلود، درست مثل VPNهای حرفه‌ای
🌍
نمایش IP سرور با پرچم کشور + تایمر مدت اتصال
🧪
تست خودکار سلامت اتصال — بعد از هر اتصال، خودش بررسی می‌کند ترافیک واقعاً جریان دارد یا نه و دقیقاً می‌گوید مشکل کجاست.
🔁
اتصال مجدد خودکار — اگر ارتباط قطع شود، خودش دوباره وصل می‌شود
🔒
امنیت کامل، بدون نشت:
✅
بدون نشت IPv6 و DNS
✅
بدون بکاپ اطلاعات حساس
🎨
رابط کاربری زیبای Material 3 — دوزبانه فارسی و انگلیسی، با منوی مرتب و مینیمال
📱
سبک و بهینه — نسخه مجزا برای هر معماری (arm64 و arm32)
📥
دانلود مستقیم از گیت‌هاب:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1232" target="_blank">📅 03:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1231">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سلام دوستان عزیز
👋
🌸
اپ CoreForge یک قابلیت جدید برای کاربران iOS اضافه کرده
📱
✨
این اپ شبیه WhiteDNS است که برای iOS و شرایط قطعی اینترنت طراحی شده
🚀
🌐
🔗
لینک:
https://testflight.apple.com/join/3htm1Whc
🎥
آموزش استفاده:
🔗
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
📲
کانال تلگرام:
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1231" target="_blank">📅 17:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1230">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرپارسا گودمن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=jNWu4uueuv-u8YTc_SiTfzBSBl1IZd5DoA5QDRvgOE531p48myjbrNlAQp9Vm_FuLiCylAejbOTFk7HcL3249Sb8zT-dCj9g1VM9SVDZSkDDWydXM93Rpt2G2d1Eo9B0qFjBYemd5Hth8DEUykswV5LzGLzOk-mQMLk-70HdCG_Rd_uKBu1jHfWQzdnh8JYj3PQkQ-v7hBuQbusIW48_7LpuzvFiuXCWwBOa-oFJfCsnb8elwuULRAS58lkwzYxKuR0JvyUVg5dR3iGX3cJwpElN5_6F3oJoRVmU-0VL65au53X9thANAwcfiEp4nQiXkcp2Q0uTF7Vmk-NRwr_VLk8_Wbyy4WLkN3qpDyv9aK2pqtGfwhxQokQZZo57n4xBUzdGOurrO-nv_Kqbtr-M0JSjh30YYyNwrnA_B1EUCQ3ZY2SMakej_EBimXukfiDPQSp_K9yzO4fVnIU32fpiBoOYVUNqDQ2X4b2ai3xnXqwaa1niCtWy7HeDazzP59VvJ3Gz2WlwjCM4LPUwvrbr86SUpic_bCTA56afhbEOvR3b65KD5eEWNG2KIIIQGiz5eIOoEHuW_w0WRIXsff6FslkE1glQ3f-yq2c3bBGMnx-pRTJ-4PmZRZZlbsjAH9fR7zGbDbh7ugT5norZpgj0NJblU26lmHJ08uluaoAUfZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=jNWu4uueuv-u8YTc_SiTfzBSBl1IZd5DoA5QDRvgOE531p48myjbrNlAQp9Vm_FuLiCylAejbOTFk7HcL3249Sb8zT-dCj9g1VM9SVDZSkDDWydXM93Rpt2G2d1Eo9B0qFjBYemd5Hth8DEUykswV5LzGLzOk-mQMLk-70HdCG_Rd_uKBu1jHfWQzdnh8JYj3PQkQ-v7hBuQbusIW48_7LpuzvFiuXCWwBOa-oFJfCsnb8elwuULRAS58lkwzYxKuR0JvyUVg5dR3iGX3cJwpElN5_6F3oJoRVmU-0VL65au53X9thANAwcfiEp4nQiXkcp2Q0uTF7Vmk-NRwr_VLk8_Wbyy4WLkN3qpDyv9aK2pqtGfwhxQokQZZo57n4xBUzdGOurrO-nv_Kqbtr-M0JSjh30YYyNwrnA_B1EUCQ3ZY2SMakej_EBimXukfiDPQSp_K9yzO4fVnIU32fpiBoOYVUNqDQ2X4b2ai3xnXqwaa1niCtWy7HeDazzP59VvJ3Gz2WlwjCM4LPUwvrbr86SUpic_bCTA56afhbEOvR3b65KD5eEWNG2KIIIQGiz5eIOoEHuW_w0WRIXsff6FslkE1glQ3f-yq2c3bBGMnx-pRTJ-4PmZRZZlbsjAH9fR7zGbDbh7ugT5norZpgj0NJblU26lmHJ08uluaoAUfZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://t.me/xsfilterrnet/3623</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1230" target="_blank">📅 00:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1229">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/o4-mNr3eq_pzyfBejlHGgaYfBT3kTwa-WYwLLYhyEWXN7EBoiJymVQ49-iCPyAuERPtSu-xVAjXFdEkEHQ2w2uQomn4wpTqnvQdrB6BOjPbKQaEFxbjJdAanXCwNRVBzxpzFA5YdDR2HF8Xca21wG56MRew5h7nfDE4q2DnMqUEJlfGWUUw-LAAZMX72zrmKNR_9icGpujnBwIvyWnd-NOrTppWBncgJaQktsMRQ8X6WdEcl3rRMIJU7ePLYigsCUWTuwKegXhZ6E1v9afnDjpeiIvYKObdFNdbFBBSctCi68cgy3BdS8bM6TquAOETSRlLLWl2uIQbGClGJF38TXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1229" target="_blank">📅 17:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1228">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1228" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1227" target="_blank">📅 12:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1226">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/1226" target="_blank">📅 12:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1225">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qs8GUu45vVDWMxT50bdBJ9tohyaSeR0snOpIPUzqLOeXd6jef9kGI5ITK8dKBbFzSdNXeItkUqPWJExmvser5l87vb1-OcfXRpaOGjI2TyyGCX2h0HrR_5hibIuJnbW6NkyEWH5F7aDHKjeD1t46YcP1teB051ixbPgAPbB8uXA6sTLcLN1cEurEHnRPLjcGZjETI0NO-1xJ13d-H4STM5RRjCr42uKTltSNACGvzmjhRrNkEXTKhrGtW89OUiUQZWug_X22YXUH1EAKQyLTlHYwplJKeCF7uoBZPFSrdDeSViIiOjNwlnL-vyV59fgolza-PVQylSJ-SCKGBCVkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/whitedns/1225" target="_blank">📅 06:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1224">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YYpzoqPp2Dw5woXVMzkQLqjmwykOP5BYwIQoDWBLle6xPmRQIQC1Sr7tKXd8Bk3pZiAmaWzU0M3IawdZ7Yf9iPotLUXo0vz-uzKy89J7TNOqoYg5DdHRr-cyngWK8UHVXz8PX7hF2WwU8j_cpW6lerWFK28jrqq9tafR5sW86N1b0upwQzH2BeY8mYCEmvt-FgCaPpEvprCuCDJ7rn7s7noys_39I4yvAeTT0hrh62f97K_GCKQ5MPoUaXV75Wds3O4DawNDMKvn4hlhxwQPh4X39DFlTurPvIqNdsaMu0ugt3m_1VCVLent7ixx-xt2TtVwwIeorpJ6-WMLVVscIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/whitedns/1224" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1219" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/whitedns/1219" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnE-85MR9OZB0t5Q6WKEhRNuRMP0KQqmdz1mA4wtgOoMG_1ncQtc-LoNd7IxvwpvxucyEX1bueF3COuE2jSlufo1tnvnp4dsVtdBxGBpFhPeCY9QjXB-_-Ribb6TRmF-i8M_IgGH0q5wGVkOGKeXxGuOdxCOvXzmZKm1P1GSkLbgyAj25qfvCTUwDdU6dGqoxbAqNDOf6yh0c5jWyaa_jS19l2zEBaFSzaQJBxNGf-1czGqGav_HmiJLWQtbmoE-NW0MFGbXFs2_oiAzj2R8jFd0j1jWxUIXDFX914ady9opT67fUcSeibU3oV9ZqTwXYFy1QRV-JBHXnv56VAmy4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/whitedns/1218" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1217" target="_blank">📅 17:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1216" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">White DNS
pinned «
دوستان برای همه اینها اموزش هم گذاشتیم که الان لینک را اضافه کردیم .  لطفا بدون دیدن این اموزش ها سوال نکنید
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1215" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1214" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1213" target="_blank">📅 12:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1211">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AD6NMrpPzEP-8coRsmPQab01zJMpHPiIq5jY1TVtvJRvQhLHHY8_gjG_oIV7WctjQcSBmTrIS-5KCPsfU5UWvBlJyJBv0-WCAXJFuzDLYAWmgvWPOS-6P5KxpV_8OGfYmt71UlWfN75R46TFZMbVdBTf8r3v-iRpCmn-68-HFdUL9meRCWwk_eDAcAjd2oyN43gQd-EQ-dk3zjqazdvaOWox64aq4pW3psp8MCKv0m13ArW4hpCWfdBDcjiT5bnlWlPrK1sz50Ke97joUTNx04OTBeLn70QNHNzdLS2ZIuQCKOKmdb2bLSsGL7gcit4sXPY_5hBMPxdTyCr0l6vfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/whitedns/1211" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1210">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EAg1Agq0r8P5C2-5jNIb3rm0elus6rjNwDUeGOGijRB8qEfyA5GGDSbsNROhkPoWJ7AqyDMscaK-x-gbuswY70mXaMUqU4FXWYGUaB3BQCbmBVyNOKfJE4U3WJMQBKV4XSaB9h2OqZPnTVUWjdW4svPBM9yGw68tsR46RiSxg-4tWs_mqBs9YGj0tHFuxMCzBpXfJblFnbDR4w2zQsm_ZNZDAI17zwtrR12_uJ1Wl1f7dCJxjkhtkorlZrC_c6T3282res26u05bEYyOb5Cedn9kYWrbSNzhd6sLOijKLs0kcB2ZF5_oHFK0jkNvkOZhcdVqZGqw3UJJD9CApDI3sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/1210" target="_blank">📅 12:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FGElYKSRJbDXSTcWS7j_AlewM43AQmh-DQnZMmvCklRfOxyh1WNlP0mIQ13JURI3pnLwvPqWN9UwuSOQH4E1LNtl9uJXbkZ9UORrNjBJXjkq8NZ8qnZhIWxGzRH60vq6NFQrnG9ZOOyuPDhhq6Ur03R50MBAtSRhRzxDjgOF4AOj_DnZHpdj3jFNBC4_5jPyMFJX4UxBop0v_VfzF867qtXeXQgM5MrLKApvBtwu1DbFCY9zGDKrLX7yaCcpS8MPcLekLZXXLS1zWD247EFgFVmNHtwU8Wlt3ts8ar5L0oRxJPFhjfgEcJGeHsgMZp1iG_4PH_mV0B2JVNOoxx1Xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1208" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1206">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1206" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1206" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1205">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Xd6AbWDknc095Xk3qfj40lLYPJQbmEOxh0TQCZ1VVEE6qGtXa_qazmKIUrj1bMgMIxdpgjK1q3254Zu1udD-0pAPQZ36sL7INYGJPAn3gs7LR4HhhxzCFrIogQJc22aTQ9UbmiStiQe8g5eaK0lKPogyTCOL7v9zHQWmhkcnMTJTdPQZGT8pwuoadF1wzjqfBExnvKSlTSvn8xpey_QBSyo66d72-Z8-4-VIdIHpGKNt7zQ4X3KEVBP2iDDHo8O_zRqKRJ27bshQ7rLH0tAw9kFAUZmQkZcC_Alf2-W3PGQBsciv1qKp64RZ2dFrSW-pGoUrHIqRx0JCbeaplXdMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
تنظیمات اختصاصی whitedns
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/1205" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1204">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1204" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1199">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1199" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/whitedns/1199" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1198">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7RXx5X1ZEepGaFRXHWvicSeSz9_LDZKFjiQh4naamEX-XnKZLMedoYeokmORfA1SWsZexaj6yXztzMdmBpfk3DD9kFnQdMHBLP7bMtfufg1jSzyrFOnhQj9BFLvS9nFVPh2thYHuTEMhpoBEEF6dSm-Zelkzk4gXWsdAsmxZJSraz1Uov7WrGcrFNAAR15HmWWsjzzwy9kq7_WAJ92Egfgmo0BT6Ea20rRQCzzeP_g-F5vPQOGMaLYQkGJBYFIPuxI54nF4wODdsFVduJAK52DjpITaaKShhgJKQqtWZ8ak1FBzzlvvFkLO5YE2y0V8GQS2OGj9xiSQCSmMKm61xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/whitedns/1198" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cXvaPuefZh4hKveYroI-41LCvEWP9cJ8fgPSu3rKeQDw-44vAe_1npz5hxzw27H0oEfkO5z2uHWYNHk06u-j7cnbLmXiHBuclmKhsrcR_uEngMXdwm1BeU8z9eJdg0rLFlIZ-uFGaIUekAybCAXE48osQlDH19NCN2SeF_tmor3Z1fKVSB29Jv_gQ6LIn7Edcm_GY_jRWzgTcU7e7kb8Wz4gmAhXWFTf-Yc1ml12cQmhDXFJDQCYZkpoXIXqJpME6bKXa7I2dWTCb2JBk1pzJTFdfyuV7TBh0dw-s5SXNgOH43CnNQ2dZ58ENxePEO4WcltsKI_Y5_mePIwMnBQ3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B8RbmPrnKlituJa_Azw4HMKIObXqeXCIef2q_a5RFSjupd88OYd2_oWYsa5QFuAAS4klmAKSUcHk6N-IlOowYOh6WNQDy9iSBSrxcgfjprrQ3E91kwKOnOXfR8KAqxg11yl-lJJSMmBmDd_tlBRQPSbjEjsflAtleLlyG1snS1N19Sn-hw7W4ftftSDZn6daHUyVklPPnTEhDfno8Z1CL4VU2am7kPCOVF5CWoYA_S6TIZ7lOmN_9hoTE-QgisejzflSWH64_bEDhKDHs3N7eAP1Xy0V7v3nLD8MGHziZsHRs_jkYNUyIdAQrT2BwbwOEBw_7CQe66YOCB4KAdhBzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1196" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1195">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qvXrBEYersoNW6o4O3cPuGhK3Tb8emd5LVJbzaaxLjK3M_f1CHPt84Kl2tre8Kx7CRK00LiA57eiPvySpHSuHEyAenYSeyGXsfL3eRD8qvTsu-ItLsnBpgdmSl4WWZmhhg74qq6S837s2p2YW5tBB8S13OaYoEVaaytxZGosKc5ZywBVYonaXBFXwBCC91hECGMuX55L7AZoTBW5iXRY5TY0-j0ftqmPMxSzX7_vGYw4liQ_Db-RHu_HCV8s9suqLLFzeRV-PNQ4LZa3ZpXxX4aWKnynxEFnvuI0pyn98StqxP6GmvD-4m-v6TaXIGIgYJe0lUH-OT5Lkk_9j-gB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
راهنمای جامع تنظیمات APN اپراتورهای ایرانی
📱
📥
۱. مراحل تنظیم در اندروید (Android):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
اتصالات (Connections)
یا شبکه و اینترنت بروید.
3. بخش
شبکه‌های موبایل (Mobile Networks)
را باز کنید.
4. وارد گزینه
نام نقاط دسترسی (Access Point Names یا APN)
شوید.
5. روی
افزودن (Add / +)
بزنید تا APN جدید ساخته شود.
6. فیلدهای
Name
و
APN
را مطابق لیست زیر پر کنید (بقیه گزینه‌ها مثل پروکسی و پورت حتماً خالی باشند).
7. از منوی سه نقطه بالا گزینه
Save (ذخیره)
را بزنید و آن را فعال کنید.
🍏
۲. مراحل تنظیم در آیفون (iOS):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
Cellular (تلفن همراه)
بروید.
3. گزینه
Cellular Data Network
را انتخاب کنید.
4. در بخش
Cellular Data
، روبه‌روی گزینه
APN
مقدار مربوط به اپراتور خود را (از لیست زیر) وارد کنید.
5. یک‌بار اینترنت گوشی یا حالت پرواز را خاموش و روشن کنید.
📋
لیست مقادیر APN اپراتورها (برای کپی آسان روی کلمه‌ها ضربه بزنید):
🔹
همراه اول (MCI)
* Name: MCCI Internet
* APN: mcinet
🔹
ایرانسل (Irancell)
* Name: Irancell-GPRS
* APN: mtnirancell
🔹
رایتل (RighTel)
* Name: RighTel
* APN: rightel
🔹
شاتل موبایل (Shatel Mobile)
* Name: Shatel Mobile
* APN: shatelmobile
🔹
سامانتل (Samantel)
* Name: Samantel
* APN: samantel
🔹
تالیه (Taliya)
* Name: Taliya GPRS
* APN: taliyagprs
⚠️
نکته بسیار مهم:
اگر در فیلدهای
Proxy (پروکسی)
یا
Port (پورت)
در تنظیمات گوشی شما هرگونه عدد، آدرس یا کلمه‌ای وارد شده باشد، سرعت اینترنت شما به شدت افت خواهد کرد یا کاملاً قطع می‌شود. حتماً بررسی کنید که این دو بخش کاملاً
خالی
یا روی
Not set
باشند.
@whitedns</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/whitedns/1195" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1194">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1194" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1192">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :   ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.    پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1192" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1191">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1191" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1190">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LQsTRnJhHr0ZKzwN6pg8znzC1mJU63OOeJ1tDu3vUZ9INYWg3n-FSHsaJHPERKw529-_3gpSXJBvJcjYvHELPvygHw973V_unl4_JhWJl2JeCOooG31CjKsjmsIInxSLM_rKyGc2Mckw7aqM8FY4bMx2kGn67FQZNM29sc6VqLb-fs3SIe_oVaMzhag1U9Mbn1pSy2fO7FoDMJWmyn_70vUsrP3gOYQI9UVkEC2MHgAoopTJaQfuxy4PjkYAfB7fFUtpVEwvLH68aAflzbIn--lFhuNMOfAbWoy2UvrMTZNQPG26gxWMa3_6ZM4Pl8b5-TsWTu16XUvgDBKvwktcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/whitedns/1190" target="_blank">📅 12:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS VPN
👆
👆</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1188" target="_blank">📅 11:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/whitedns/1183" target="_blank">📅 11:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWvDxvGSx8lxxjo7jxKgMYEeKS2VkyolUN69dmqok53Q8d_py7X5xUJoNRjocoplD4i2zYklfadgXF93nk66zHma2mV7bD6S9_0Z0ixQegTyCEYYqzw3cIQ7Zg3OYMkW3doQLc3mvKbmnA1TY_4Q8toazJngRKNjFOl7bcBQTLOxah3EKSiOkh270Pty9oltoSPltbsCx-fEzRTZBrbWSkSJ3dX_v1NOoIrLDcADYYFj9IU4Z2GH4IuchwXcn_JvWdCIJ0jmmOSFUpRvbjfbWpSnl8KpGi4A7ghNWWBdBV7IYHTV6-joRRiHCA025WAaNKPeHLJsPTxcy-mRoTYMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/whitedns/1182" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1181" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Mx5snA443kLfB-_hw64vLFZM5UD1-IPYJAdhmYFADEkmct_PymfFXmK__r01EaAw_Wzkg5NQBQYyWR4e1Q5zJQKBNGttab8yp0f_DUx9zotnwyIu6_wWikskYi4XKfBKWUj383tID9togDBeLJtLQ_598l3GEzyKEaDDk7t7cVIHS_vqeH22sEfTkH4jkAkye2JUnrAgUCKMb8pGKttLxPMngwCw8scHKBnGMwlDE95c9uWfrHDi4XPQOruA5hUa3TZoUesgzyWlgjUGA7Ze6sy6rkTg_sfzjagjd3IfILtdlHfFyW2F5YAg9a1mBF5d7WcgYSHwVMhzP8820bFNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/whitedns/1180" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✍️
در مدتی که اینترنت وصل بود، تیم ما تلاش کرد ابزارها و روش‌های جدیدی آماده کند تا در صورت بروز قطعی شدید، بتوانیم بهتر از شما پشتیبانی کنیم.
متأسفانه بسیاری از این ابزارها را تا امروز منتشر نکرده‌ایم که برای این تصمیم دلایل منطقی و امنیتی وجود دارد.
در صورت شروع محدودیت یا قطعی گسترده، تلاش می‌کنیم این روش‌ها را به‌تدریج معرفی و در اختیار شما قرار دهیم.
برای شروع، تعدادی سرور MasterDNS نیز منتشر خواهیم کرد. با این حال، پیشنهاد می‌کنیم در صورت امکان، یک سرور تهیه کنید و با استفاده از ربات زیر آن را به‌سادگی کانفیگ کنید:
@WhiteDNS_installer_bot
❤️
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/whitedns/1179" target="_blank">📅 04:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1177">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ksWWkHi1x68pAbruGB1d3LhwLPkLRcrlgviKbErsOK0ViLay-rmOpQqQPx1CsihXTfLu_UVynDPAxZr_kXAx_mf52mrUJMchagfQVzdYZyaVYRbJqBbHaOCGf4dgmvElvNpNGOyF44v4hjQkE5Uz0YfGHmXelFBQQW6tzZJlGywedpwGMCUvZIIkiErUFBtDk7adQU_FKEZDCcmai-Dqh85SemIeHT35u2ukcdCIPjwUuwA7oeZJwUdipvTHde2_7F2n2SzV5WwrUYOrnwLKg6wrpMOgi8euhPTOljJTzylDyHjjp27IUtScs7EdmvwQsZw9kfCW7HZx8oGtF3rBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1177" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1176">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GUkddb0qOSr04j6kzJJHetzGN5nM04CjwktTJTxf8IyscRcnYvJTq7Kw-9Nz_iixI2fo02Nw1ajfu-sibzIrOhVqqpFPGNVEs1Ce25Txt0balW27IAEAtF86e8cK3I5EuZ6t2HBvcX35iR_NxcJhIFGlAxx5FqKs_IrkfP4vrbuWvDOEuvVNYD83fa55dPIG2NU6mC2AJAJfAYQjY7RSB_njuz89Fwaj2h9gVf18jwKFFiTllzWBhGhOIb8Sk2nBwHx0eL9dB6hY--XSQt04kyxBJssupJmWhG37SJHnj136rdD3lI-0WRcOtbJLaOEfObX_HFX8yse28TiGBY2Log.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
OnionHop V3.7.2 - انتشار جدید: اتصال هوشمند و عیب‌یابی شفاف
آیا می‌خواهید ترافیک سیستم خود را بدون درگیری با تنظیمات پیچیده از شبکه Tor عبور دهید؟ OnionHop، ابزار متن‌باز، سبک و قدرتمند ویندوز، برای همین کار ساخته شده است. نسخه جدید 3.7.2 تمرکز ویژه‌ای بر پایداری در شبکه‌های سانسور شده و شفافیت عملکرد دارد.
✨
امکانات و قابلیت‌های کلیدی:
🛡
حفاظت دوگانه:
انتخاب بین حالت
پراکسی
(سبک) و
VPN
(سیستمی).
🌉
عبور از سانسور شدید:
پشتیبانی کامل از Bridgeهای Tor، شامل
obfs4
,
Snowflake
,
WebTunnel
,
meek
, and
dnstt
.
🌍
انتخاب کشور خروجی:
امکان انتخاب دقیق کشور نود خروجی (Exit Node) برای تغییر موقعیت جغرافیایی.
🔒
امنیت بالا:
شامل
Kill Switch
(قطع خودکار اینترنت در صورت قطعی Tor)،
DNS امن (DoH)
و پشتیبانی از
IPv6
.
🚦
تونل‌بندی هوشمند (Split Tunneling):
انتخاب کنید کدام برنامه‌ها از Tor عبور کنند و کدام‌یک مستقیماً متصل شوند.
🤖
اتصال هوشمند (Smart Connect):
قابلیت جدیدی که به طور خودکار بهترین استراتژی اتصال، موتور Tor و Bridge را برای شبکه شما انتخاب می‌کند.
📢
مهم‌ترین تغییرات نسخه v3.7.2:
۱. تشخیص و تأیید ۱۰۰٪ پل‌های WebTunnel
در نسخه‌های قبلی، برنامه فقط آنلاین بودن CDN را بررسی می‌کرد. در نسخه ۳.۷.۲، OnionHop یک
اتصال آزمایشی واقعی (Handshake)
با خود پل برقرار می‌کند تا مطمئن شود که آیا واقعاً ترافیک را عبور می‌دهد یا خیر. این یعنی دیگر پل‌های خراب به اشتباه «سالم» نمایش داده نمی‌شوند و شما زمان را برای تست اتصال‌های مرده تلف نمی‌کنید.
۲. عیب‌یابی شفاف با لاگ‌های دقیق
اگر یک Pluggable Transport (مثل obfs4 یا Snowflake) به هر دلیلی اجرا نشود، دیگر با پیام‌های مبهم مثل "status code 2" مواجه نمی‌شوید. OnionHop قبل از اجرا همه‌چیز را بررسی می‌کند و دلیل دقیق خطا را در لاگ‌ها نشان می‌دهد؛ مثلاً: فایل اجرایی خراب است، نسخه اشتباه پردازنده است، یا مجوز دسترسی وجود ندارد.
🛠
راهنمای قدم‌به‌قدم اتصال (How-To Connect Guide)
براساس اطلاعات مخزن گیت‌هاب، نحوه اتصال بسیار ساده است:
نصب و اجرا:
فایل نصبی (.exe) را از لینک زیر دانلود کرده و اجرا کنید.
اولین اجرا (انتخاب حالت):
Proxy Mode (پیشنهادی):
اگر فقط برای مرورگر یا برنامه‌های خاصی به Tor نیاز دارید، این حالت را انتخاب کنید. نیازی به دسترسی Administrator ندارد. باید تنظیمات پراکسی برنامه خود را روی
SOCKS5 127.0.0.1:9050
قرار دهید.
TUN/VPN Mode (دسترسی ادمین):
اگر می‌خواهید
تمام ترافیک ویندوز
(کل سیستم) از Tor عبور کند، این حالت را انتخاب کنید. این کار با استفاده از Wintun و sing-box انجام می‌شود.
انتخاب پل (در شبکه‌های فیلتر شده):
به بخش
Scanner
بروید. اگر در شبکه‌ای با محدودیت هستید،
Bridges
را فعال کنید و روی
Scan
کلیک کنید تا برنامه‌ها پل‌های سالم را برای شما پیدا کنند.
اتصال:
روی دکمه بزرگ
Connect
کلیک کنید.
Smart Connect:
برای راحتی بیشتر، می‌توانید Smart Connect را در حالت خودکار قرار دهید تا برنامه خودش بهترین تنظیمات را اعمال کند.
🔗
لینک‌های رسمی
🔗
متن‌باز و رایگان
#اوپن_سورس
🚀
دانلود مستقیم نسخه V3.7.2:
https://github.com/center2055/OnionHop/releases/tag/v3.7.2
🌐
وبسایت رسمی:
https://www.onionhop.de
@whitedns</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1176" target="_blank">📅 14:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1175">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns16.7.2026.txt</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/1175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@whitedns
🔗</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1175" target="_blank">📅 12:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1174">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ayA4woWntmRWpoy8YSM6Gzu9NBCm9UJ26HmeWZXx5rAz2zJBeOdw86xUOT6P3JRRUKnSHBGITyier6jGeYPUw8WhMhnIQ6h9Zafy7c3UcWSSHZl6sZjMKvkaf7nSrgo5uy3-UOvwIF0HybnBb8YKs8qX-N4ztsn6Yy0od7ldMWZIOzG-LVfY7xjRKzN0lhSPLwhCNNdDFERSCtml1gP189ih0yNKnAw5VbzKRMXjh1TokXAQdZotAdJqVs6zFHjg0r5oYQQKlRnyE49Qi_JYH6FHrkvzZ6e8DpzwY_Rmlz9d4jLaBtrc99pYYe0NzB5RUwptVu-vFrnJ0CUNeYwv1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">16.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1174" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1173" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PH1oeuAcJ3rSbU16JiXmVVk2K9aiQqJpwl3zSoThHHZJyAnuKVvsXjG9Y5DTnpXiqcyIjC8G2hi4BQ-nr8hxhy8ltHOuY_12u193VcTnJMfRPdX_7Gyy7TWM6gmnruICKkFmnggqvwminL2n1JOyHskkjG_iieqseQAETOGHdeFa_Zkfam-YFKp1ISQpc85yv1E-lAF-UtDLd8CM8BDJm5PZKJD3iqfqrzAkqhl5vNL5Fgflwb7aPmAQW3UUhSe4Wy1PuC_GUw_4FvczFM4Rk_lYwQPwvImOlslXUYB3kYlCxTDJ6dufqPZNVh6B3d6TFRk0LH9ehy6o-ZnYPMldsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش جامع استفاده از
WhiteDNS VPN
و
WhiteDNS Scanner
برای اتصال امن و پرسرعت!
🚀
🛡
رایگان
در این ویدیو به بررسی تخصصی ابزارهای اختصاصی *WhiteDNS* پرداخته شده است که به شما کمک می‌کند بدون نیاز به دانش فنی پیچیده، به اینترنت آزاد متصل شوید.
🌐
🔓
خلاصه‌ای از مباحث آموزش داده شده:
📝
راه‌اندازی WhiteDNS VPN:
نحوه نصب اپلیکیشن و اتصال اولیه بدون آی‌پی تمیز (0:00 - 5:30)
⚙️
📲
*
اسکنر قدرتمند WhiteDNS:
آموزش کامل کار با بخش *IP Scanner* برای پیدا کردن آی‌پی‌های تمیز و پرسرعت (7:40 - 18:00)
🔍
⚡️
*
کاربردهای حرفه‌ای اسکنر:
بررسی قابلیت‌های پیشرفته مانند *SNI Scan*، *HTTP Proxy Scan* و *Config Maker* برای ساخت کانفیگ‌های شخصی‌سازی شده (20:30 - 27:30)
🛠
🔧
*
نکات طلایی:
نحوه استخراج آی‌پی‌های تمیز از دیتاسنترهای مختلف و استفاده از آن‌ها در برنامه‌هایی مثل *v2rayNG* و *Psiphon* (22:40 - 25:00)
💎
🌍
✅
این ابزارها با رابط کاربری ساده، برای همه کاربران (مبتدی تا حرفه‌ای) مناسب است.
👨‍💻
👩‍💻
📥
لینک‌های دانلود:
- دانلود اسکنر: [GitHub WhiteDNS]
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.5
- دانلود اپلیکیشن: [Telegram Channel]
(
https://t.me/whitedns/1072
)
💬
با تماشای این ویدیو، سرعت و پایداری اتصال خود را به شکل چشمگیری افزایش دهید!
📈
🚀
لینک ویدیو :
👇
https://www.youtube.com/watch?v=N5hKuWXp37w&t=57s
@whitedns</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1172" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GZchnWpcJFsRa_wUwmPosjId_f7VKCzMS00gzI4bnRLlqn8KsPcIa6rw7qgDFgalNEougfP0yEkJAJp4bHi9fSlDe9OSHLCGD4reSAs7QiZ8uQMCCaPiPrstRC6kyJN8PDMLUqzQbObYHj8vcrMq9LDphBzi9FFW87aqAnGbF-FjLQVpKi_4iZgdJ6y52dDsE0dS5_lCgpCd9UlWOQP-gNjnyTw997DLe1mZ9z5XMD45BD7GWvNgWHlNC_KCMaxBMJ7BVDbZuExfBHK46B8DbSWtcEO2MZ8arNpUBulvgPD_OjlNOyx7ROc9UGl9zb6_ori7KcJgQ-yypbbrucleLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش کامل راه‌اندازی V2Ray با پنل قدرتمند 3x-ui از صفر تا صد!
🎓
اخیراً با کاهش محدودیت‌های اینترنت، روش‌های باکیفیت و پایدار دوباره فعال شده‌اند. در این ویدیو،
WhiteDNS
🛡
تمام مراحل راه‌اندازی سرور شخصی و فیلترشکن اختصاصی را به زبان ساده و کاربردی آموزش می‌دهد:
🔹
سرور و دامین:
نکات کلیدی برای انتخاب سرور خارج و ثبت دامین در کلادفلر
☁️
.
🔹
نصب پنل 3x-ui:
نحوه نصب این پنل کاربردی با استفاده از هسته Xray بر روی سرور
🛠
.
🔹
ساخت Inbound:
آموزش مرحله به مرحله ساخت اولین ورودی برای فیلترشکن
🔄
.
🔹
تنظیمات کلادفلر (Cloudflare):
نحوه ثبت DNS ریکوردها و تنظیمات امنیتی ضروری
🔒
.
🔹
استفاده از آی‌پی تمیز کلادفلر (Cloudflare Clean IP):
روشی برای بهبود سرعت و دور زدن فیلترینگ با جایگذاری آی‌پی‌های تمیز
🚀
.
🔹
ساخت کاربر و استفاده از کانفیگ:
نحوه اضافه کردن کاربر و دریافت کدهای تنظیمات برای استفاده در برنامه‌هایی مثل v2rayNG
📱
.
این ویدیو یک راهنمای کامل برای کسانی است که می‌خواهند فیلترشکن اختصاصی خود را با امنیت و سرعت بالا راه‌اندازی کنند. اگر هنوز شروع نکرده‌اید، این فرصت را از دست ندهید!
✨
برای دیدن آموزش کامل، روی لینک زیر کلیک کنید:
👇
🎥
https://www.youtube.com/watch?v=vVjqNQBUGIc
🆔
@WhiteDNS</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1171" target="_blank">📅 09:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C8oXqDjX9aeU2yeNo8pw-fC-RUAn61DAHADKjJUxJj1kGxit8xdA17mV64Exm9lb6Yiar-x4Ke0KOvvSdlXLsnKLUlg1-HU102kWqTN9e8a4hu2hUuAKlyWhl7jOo_ITgB03CqPhqb5kptX_RhcVRaPNbEuFv95V6nATGSJSx28VbFtdPnAPfxWySAHPgCAQFBfnfAF5UG0o8WyZrlRySASVToE1DoD0SJjICS8npI0Bjqq-1pG8bnjowX8rXGB2qgK0YUe5Nl5YEczFues3LSC1Pz3cs8q0b7xPVhS1KYwmG7tRH0CGI2VUv9m-atwrVyzEaes7HZl1bitCwv8t1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1170" target="_blank">📅 13:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/f4pxk7A-iuLzoJ5Bjp1dCZqBUKGz0t-ScYgyBT4tlyz_BKN1zJBwYXZUaIdYKiuQq4UQ3T2nxLmlHECTZzkKwYiQjASC8BvWYf_jaNcQ3vDFGqfsP_g6gY9s1lq6IKesXG4n4i6ATPYQLCq-La3oOsN7EcOeK-axPqZl_enEgpqxUUwZMRiB4Od79zzdjJAWh8hg2NFTNrKICAXQIblQ4XlEMRrd42BD_lkKk-FB7Q4WH7XqXhbDKYZ6zLFU5HMdo9m0Hlj-3O0Ov647vLvDNC3MzezE4qDtZKUO5eH_Ne-MYhLz7ebs-19n_DRsLiBM3Hea0XeGibHN262e-uxr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر برای استفاده از سرویس‌های هوش مصنوعی (AI) مشکل دارید
🤖
این پراکسی را چک کنید
🔍
برنامه یک اپلیکیشنِ نوار منو (Menu bar)  و یک داشبورد محیط ترمینال است که به عنوان یک
مرکز کنترل و مانیتورینگ برای ایجنت‌های Claude Code
عمل می‌کند.
به طور خلاصه، این ابزار کارهای زیر را انجام می‌دهد:
نظارت یکپارچه بر ایجنت‌ها:
وضعیت تمام ایجنت‌های در حال اجرای Claude Code را در یک نگاه نشان می‌دهد؛ بنابراین دقیقا می‌دانید کدام ایجنت در حال کار است، کدام متوقف شده (خطا داده) و کدام منتظر تایید شماست.
بررسی وضعیت اینترنت و سرور:
به صورت مداوم وضعیت اتصال اینترنت شما و سرورهای Anthropic را چک می‌کند تا در صورت توقف کار ایجنت، دلیل واقعی آن (مثلاً کندی اینترنت یا مشکل خودِ Anthropic) را به شما بگوید.
حفظ لوکیشن (Location Fencing):
ایجنت‌های شما را روی یک کشور خاص قفل می‌کند. اگر VPN شما قطع شود، به جای اینکه ایجنت‌ها با خطای دسترسی (مانند خطای 403) از کار بیفتند، درخواست‌های آن‌ها را موقتاً متوقف نگه می‌دارد تا دوباره به اینترنتِ همان کشور متصل شوید و کارشان را از سر بگیرند.
ردیابی مصرف (Usage Tracking):
میزان مصرف واقعیِ محدودیت‌های اکانت شما را (با خواندن دیتای خود Claude) به طور دقیق نمایش می‌دهد.
https://ghhrmnzdh.github.io/tower/
🔗
@whitedns</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1169" target="_blank">📅 09:35 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
