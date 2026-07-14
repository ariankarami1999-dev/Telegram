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
<img src="https://cdn4.telesco.pe/file/eUE84zS9yoBbFgBG6TBg28zbV1DqGgqgwYwzgO-zAL0WxMvYsKz33DhcW0JN9lRFvavjMgFH2ZebN2FYv0y6Kpsed6glmrKpTJPn6B0esqdzGIOqJ8tCAuSux1HUAMScC-2LkGc22b-MEjmIHTgWysnwHCdBNf3l6pZithroFOLmucQqQAeSqx9Rh2xznMglhSfwin4lJXOuBWzIgXnm4t8Jsnz2vN7BT0cQQ8mwpsf3lEflDLW-QmJ030J86BUNHQ6YV3E-kX6xw61QKJ-eO2Yl2BmA6xBFAs9yMZ9dMcEnSL2HQAyHCRf1E1SbnpQ8Xuv9p5TKyW5f3a1PLwWi0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-942">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">باز بریم بک آپ سایت هارو بگیریم :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 248 · <a href="https://telegram.me/danialtaherifar/942" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-941">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 308 · <a href="https://telegram.me/danialtaherifar/941" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 558 · <a href="https://telegram.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlKxnfkybp9r2gg5dZyLsPED9aVT5mNnW22tbzNUHm1_1AAKukfpsaaV1b1zjUMwA5zXC4XkwR1_tWqwJ7N6L2GdC4S_97YsCmyYrmRm_DOnHRInLJqog7WKKWJxzrJtwPEUUaQ6WbzHWJCpdt6I-j9igaisVrVdGcxLTA-xRnepCBChQ4UCj8ggRUSyvU9gpKaVQm_5WyYemDPSRZYytXUyxPrgZkRst9DoitixYyb3E0vnx4xaL4Ykl6kGgmr52ACY9l-fUycpnz72a9MRAMFD-_R-mf-gAtMqu46zYULMW8bvNkHWQZvI-C8YmDMxk9ZMapguhKeMzv5MtjmhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 751 · <a href="https://telegram.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 868 · <a href="https://telegram.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 909 · <a href="https://telegram.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 899 · <a href="https://telegram.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=tCKe7C6WdhXAKnrPH17mukffc0Jja9Tm4EBTjjRLDy4IzSI1VgjMU4nosLXdaXYhYoXyDc-KLSMsitXa4lKYBvOQCsQ1Pb3lr0Dc5UpIxZwB7nyKGuvDr_WjO9-lJddDqoz85_hdG9YK9wkLPbtsI0lWCYZEVUcK9JY2MZJdZPc4WZ50fDFvcfSGw4_C7cbKDQ7ArZzBZSHLDe4qxpUMoRbG5MR5Wtl8Xz4c275sUUM_kJEF_Fq2MSV2e4iOSM3lRbG-G9UbD9-S2mNPot1RMOWEHKV8NWZYGQo02q90BJJjX0mCS9_pGd7z8FkhgY7hfh3TNU5zwlvnLfBIqwr7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=tCKe7C6WdhXAKnrPH17mukffc0Jja9Tm4EBTjjRLDy4IzSI1VgjMU4nosLXdaXYhYoXyDc-KLSMsitXa4lKYBvOQCsQ1Pb3lr0Dc5UpIxZwB7nyKGuvDr_WjO9-lJddDqoz85_hdG9YK9wkLPbtsI0lWCYZEVUcK9JY2MZJdZPc4WZ50fDFvcfSGw4_C7cbKDQ7ArZzBZSHLDe4qxpUMoRbG5MR5Wtl8Xz4c275sUUM_kJEF_Fq2MSV2e4iOSM3lRbG-G9UbD9-S2mNPot1RMOWEHKV8NWZYGQo02q90BJJjX0mCS9_pGd7z8FkhgY7hfh3TNU5zwlvnLfBIqwr7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 890 · <a href="https://telegram.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntRa05r2guIQUHn11FPbTJEHClO8XpLZ_lp0Lvm8DtQerQfEZjSyFcU8vPiF4-wfeldWkw-DY7hSmGu2Z5rLT4xEQhaibg-XK8O9GPTQh_kr-awF1G6az2klfOohSCEBZkMGbik61dwnrU-xqZHiFmJI8VRF-BMPTuhczHefXXtuEc3mkpkNDsbSRqfXcgosZYz0-hYoiFByK7FcGSHyges_WYNR8_7oeISwWhDAvSWenzJpQYDV_dKfisK0Bo-LDjuB5ok8ifmY7NwAPKsF1R2orUeCk3oc_LrEYa0QiURb4vUd8U2EuFAFoE__afVX-Mim9e4Hvty2dwhUwtKwSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 732 · <a href="https://telegram.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 748 · <a href="https://telegram.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 890 · <a href="https://telegram.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://telegram.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voINcYOlHig5Yd1cvL0r_TT4L1vAu1Tl52BPj3JhGr5uyvcf292A45pYwFm4zchwa9QROSGvIWOXcQZjfXeCEoi6xxF8CBcVGnJtlr800nJrgkoUbTb0X5AGYp_LzwFP5zM7qE9Unn4ABy1LxJiC47EM_VRtyPwiah2kZHSMs3VnrbjqZWBBz6tkXINPkUaUTzMENPw-1MKwrOgwNI3UVGP22ggOuJ0LXnF-Q_q9pbpyIt7A7myK1KC6NHwQ8zkKarLakpKGT8njaWI6i23Jqm6ScyoksepBc7TLYLlEMqFoCkfdLNRWfiZ_EHCszaUQfJDDcLxBGFIQfMg04RjyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://telegram.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://telegram.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7Hu-P_lkTOqSmQ4rNMA-ux6DaDxcqp6Mi5mmJ_HGAV7eqM1V94s5Rh4yW9whzJP0Hq_2VUvqqrUbjhqiFs6tMF9RF2KA_AHGwQsx1j0ocINLbuq9-qKaC32vYXH9yJL-3-eAJfxFM12TIM8oGBTwDSnlePKL9PvYK0n4-kLGwpHLsW2kYJV1jqDU9S0XUrc_YjtE9nTCCTTnSVMW_wuWcGXA4FaBV0tTDBmjJK60ecAvOiQ59p_eBQjIu3dSSgrxikFdSbRoSWNUkpax0BLl74H-085Cj-x0kddPs9yafD9sXkFqzgs5qRJJdAl9mBGu7otwzrcyXHvESXChKbJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://telegram.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://telegram.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDM3JhWG2QoIl7BAWsEVTYuznkoo7wkZCuD2WuLSIPE5HdE_jsyrawvb6_Vig2G8myDkd41lCf_iaFTVVnHP3BnaDjn9lVvfNUPnj-stgo1diEvdWONpDpCvduJVAD8hGaxW1GD2rY2ONzAArwvAgRo6-D1UD4f0WLa_PRK8d5rPbsYcVbrIH3ikoyAtkxxKwIoPcE8b9TaWelkLc5HHKUT9kx5t-Y6yZ9gaiNPx2ihpNTzSksBGpuKmLcP10_lhyzG_k8SKhFyvmgYNornM1Ee0ZdEJoqdaUP6qOLL1_8rUiK97_HqSIoKqIQzH-RoAzU4bUe8OOXBs5pFgAnXzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://telegram.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewEwB_MpZZgXCFUSD7jOBqwJMXC8kWPsKCva_aUpBspL_wSpyhpgNsPmWP77ITSzbA5MPz-RTHFGG8ixSnpJxulMGN_o1Mb-1C4CPrQ2mdPhSpibaME6BMT2-imWIlV4M5_7rtSREGvnxeG0vjT4qO4lf86rK-AELQ8Y6RNqdpui3NRlF-3dAg7807UPRVcLTUMkDa5m3M7_kcT3yDKcs8rDYUmjuX57vyiXnJ6snRwJxcolta8BOk11lWWu28v7PevTEMbaW3NU_nThYgLcsrv0R_a9Ry2Gxblppg_IOA6j7IRw3KEeY3fSH4GfFQIdseDTa1Q-v77DT5oxZEsbyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.23K · <a href="https://telegram.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU-x34CP6cr0NKRp-hepoUl8wY5yCYnKnfwgl2qeRc4-tS-LVGTZF4xfbdtjR1KHPXjfX9rWq0BAU1k3mfD-ZXKItEvrxSbLnIzOLNOHnda0NBnD_qGOJBl0oedErKmOe4q1M47ktw-weae30kwV0GzGuBcIuiFBdCIWQAaZdof2g3XMEAfPmUSgxay3qOYKEPOTKAxEz5Lr1uyaQiI_usQU6TE_aTG_TsrjhV21ubIua-tzIgpXNCSDNrLcqxLOuDN23UnfOFCKlEuxQZGrWptUZpRfWroaF8p0v8o6V6PXntHJ9-K31h11ftDg4Ng3JJ40RbmFa_JlfK5zsNu0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 958 · <a href="https://telegram.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://telegram.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 919 · <a href="https://telegram.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 978 · <a href="https://telegram.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://telegram.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJNlmX0LiGqJTvAgV5zkt4DtXSpVTVJz3hE0qQSkmB8JF3qivS137M9fx1erIXJ4I9GpMAfXYLPlt_8Ji_Fme-R_fVyPWSvQnABbbXsy-12NvTxf936BmphDvgTNFewORg611pU0kyKBypq0a1Ncn1Q6nMJk0m93EKQONUhbzVUJBDV9TMcNh-IqbTB3sZvSD0Ggx1lkjp_o5KQQ2qUKDJByjJz7sTiR8Q9tasz0uZjp5DozukEx4QSCiTJS6Yv_pdiMUnphJxztbNbXzAZsefjOehGtOQch9Gwg7oSdOjJ5St4DaSeesQbkd1k7zimbeRAJOeGrTrRW1Tcu5Ka9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://telegram.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHZM0d4vF9UZ9r4FsQqCbQ5r4Szc4RaiQG4GBUuPiRhpUxlnwVrNTTpLUTentzWZ8xCOVtKNNHGn5gEQh3KGQqrUs54n6-K9TDMnLwyzWD_W-iwLBBb_9LFJkaUoWJSGCb14TV0ik8I8LwbhpdYAqAjeY72_IeChXnthX9_Pk-y0Nyix7X8A7jlYTD0OgJ-cTmvKL_KfL8pZhWduFZkd1l4ziv7q9JnNp7se1G_xuR-4Z3vC0DDkVBixfDSATnfavXBcNO8BvaB-jEJ0XxbEpmMxXBPLlTdiTK7o5tB5Nj1A4DurSh11hGtbAAon-Kwb-vi74wd0tA3qSBOxcAe4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NF_CegeIVpSldaPPYXD3ibWsQN7wVZo2j32VJ5X0n3p0schPpGWfmr8LnMcXgIrIHX0DDp1iqtq-FX8bvbrwkxBFKv5Uai6OPU6sFohf9Okxfz6BiQvsGNJf7Vgcymbgi1RQ1Folx1dZAbJgVUsTpj4Gzj8P7XLbEagBMehGQmdj2m_lBaRSQ1ClzEKwCv8FQ-7MdM8rS0UybQKcCAjz8MVu8_494K4g7RwnMVhxMep1CsueBcBObvJOdauZ-pbR09eCO4qNRpGUjVfQNm0ZVIfhDmJOIF5fieCMlC9WUTi34BFWzSez9uwC51ta4MRbHZ4_mHgLOqE072DdixdoSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://telegram.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY1Cotz9VOQQfxdt6tmhY7sDXJoq7kJ68-xthEehQNS-npFjRegFmIdvyCZIK01Km6BS_EMD7esrOCXQXRyuMFI2Ud9i-TQ8rdkZyMlxO87csH5vrfIQjGmDU2y2TLl_m6tIduJT5e0gTRFyfoaaNuG8W7l8sdWQQxaDl1CNWH6waJ4QM1RoWa6tO4hbejfg8i2O207NiQofQAx-_pOya_ozNzg-nX4TLwYqG4aOZJSgPe7IfPRHM5dd43rK-Ww33D7EBe8Jaaq_2CXtvh5fBaTfQO5ovcXeNsZpJ_ltllOt-MGMFvXAdxezJoik4wUjBXeuXXQIMYYSqV_srAtDmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 895 · <a href="https://telegram.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://telegram.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 845 · <a href="https://telegram.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 686 · <a href="https://telegram.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 909 · <a href="https://telegram.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot-71JMcQA-rKCcDZG5OxQ6Yv5lAyS8khtBiiwhU-2jFdURh_aclH8mR3PUBvxQ6dpKmfstTWsPe0TN3Z4iOLXnjq3t7bwKrwlkzCNDoc1Nn6sHDgp2pB1mdFIAfBzH7b3HjYotwskwwr43RkNgirAym1nHeAgjFESS617Nr4i347RnIii-00aOF5NWJ2_ZBPZA-uj2a5zRIiE7F4AvbVZDfE93owzH6YTew_iqTYZc8pq-YbAVQwdiGU1f_lgHkvQRRCjs8rNglpxaUvTWJZ2Mp5CBX4gllxL_9c-dob1gHXTzkYkU7V0JeOxF2847yA4XoUAOJ5_us-a4SEIhYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 895 · <a href="https://telegram.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 839 · <a href="https://telegram.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 780 · <a href="https://telegram.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 1.29K · <a href="https://telegram.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKkNLjR7qBYuMTTADs6KK_qC55N-i88VN_hv-sPnHlGXVc7Q7ouoaLUeX-nmllyofxISAuoA9bXMrorPdU5oAKKzgjj85JA61UNFlEgFQ6qIVOI0wTnq-NYa3sStKXhZrBXHdwyu4XXZu6KpSdaphnjproi7-UMTRiczjK4PvYU1_EOJpMZXqJxQR3oK-22IQsZQ-j9mSVMnLtN5LoyW7zwbeOIF0lc8749Ius49bsQpixT0nZL-ARNNHX2wEf_WV70u_X4xwKGKCS5jOTF-s_kacTJJsyaotvBoxmPr00Liwnrb90QSHQz2FdYeCAdpA_a6ogY8zAoE8Kyq3EqPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 859 · <a href="https://telegram.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 691 · <a href="https://telegram.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIClg5Y-6m0xyIdH0WR3j6nTXqV2rnKcX4p-BhWSbwZBH-9Kno_C0EZSjxIPY99beHUf1vLFOkMOkJf5uJD-XEv-UX3stIu_rT6HmcNqW59FJd9C8qootH1UfTpoYerXDuqRbA8mo299Pk8qfUDyfaPNID5eAef-EJVXR-Tp4GA-3SlF03Kvus5h04dQF1n273Dn5L92Z0s1DcOX7KluvwCstPyWSBQ2rA__tMflpnlQLfSK7zveZp_JCBBBfY4BDD3MtOkCvFL9FqBZIKXX4uBIvxlSvMjiD5zOFXK6C5d2clI_tFsnc5N1mZMVjg4JLDp1LoBjoNskQ-V0_moH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 893 · <a href="https://telegram.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZyLwbthq1SPTXJWov7vxcDQEcipex8E7XE-2A7thAtEf4to-6toN1PJ9IqQTJYauuD9kQVtHFG1vYLdkAGHtavyBZPrHxL3A3zvDaRI9BM9Lo2Q8LQmDwKn2eoFqB8uGcPaHW8G-ESeD2oOWeEQKDCV3lR6VNON-GtXWFN2uCim3fszTK--s0-TjtkPqhpsoJPAkusP9xbv5yzYUYF1unY_szie65tUfL20UqH6DOCbSh3OwlOoSRVq2QAqCC4LGU_yF5WQh5NNLse_UwL2mh465s7QTI28FsyDql7T7dL2A8GwAek7qwdmKWADeHMZAJewf3OWnHhIjoADbMsOHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFwXiE39Oj1R_CabXZrGga1GsFS0KH3SocnVLl5brTDYWnknl-5mxKlcctYrjDoc4URjx62Ws9r2FV7maLVIIVSh4HwmYhaNgyDDvqoCSbywC1R4xNTVQd55E0RX5pUgFPmMjJ3_AVPVKyHhaCa7rSTtnIzpjDfo4vs7mO1kQOIOPEeOxzfE1OM0LQcCqKtp7r2VvS3FfWyiXVyV8eVmlLpcwryMV45AaBlaUCzeiXuCxnvvjES4as60OKmBI4OxJ_mQaxvxSv0mS4ZBtEtnwtKQQSI8qHoJOoZJ-m-IBm4Ua6nIlJbelwetWrdMZp2he5f0kKKoJv5ITr446pvTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMu_YupyPgomOUu0eOrX685KXyUx-NhrgPCepKnBRqdthkhLrKT9Oyg_Eq-M2hRcC_PVsL5pnfE6-vP0f-qazBpkw2KTAUapKX6AN0JrP1skIB-MfkbzbMfLBDTTXNNkXedCmSxWpcOD5Gb77360XEUX_nBUdr8jQqu6-G-iafuQuq2CEM1tkjbYs7wdRNGsN9XavT2_-Y0w-ASbLoZbRPJIpz3RsUTGULqeXS-GGkJas_PTmHtBmtvtVjhKfSTWMSEJKs-CvJ5e2TtMROIse6b5tDbox22WI0aoVjNBJ7tVXzxlYh2aTITvLQkMFn41try8sxJwHc3Rb2tGM4pyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnQ_guhpbPnB97Blalmv_ixppigYHnyFqAWor7m9LDoonTKo-vI8i4uV560xQvaT86ZKO6oRom3_DRzWc8gYgdc3bdhgPoQGBAksVNVgSPWJ6UcSU73IC0hGM-tvO9Npr1qbTaZDti74cGcFl1rZ56v-HwNfpzsiAfJOYjx_tYgWYRqk0cPntdgYGbLDWxkDTYO31KOpObA69Ha-msVafgPnRV0KLHmc6vU9B8bjfq_MBBA1cmKg-VZ3AQVTPxBJb0YoAkZPB__W-P39V3_waPMxzzylsFDfgXSteNNYdq7QASaQTSfhz-b4zy4D1oNMaIPTffhPyuw7zggO6yqhnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 984 · <a href="https://telegram.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byviRDELLlSeSvIZrNw3qE12di74jfSbY1gxkN4wS7Qatvauq-tLSTZGBJz3qbX9Qw5wa-DSwHu5C0MwH8mhDg4CpqtO-WsvwzYmJjQkBTqF7ECafnnqfNGSS4VPDwNGTOz_nD4x0TTSC9nONB36lUu86ROfrpK6s2hnB3gPR5ZQSabJ55rIMRi04XBnEwS6FF1C84x5Vxw1W1p5MtQc0XrO1UC2giXsOWSAYhhcCHn2tNt07WsndArlIxQPQCM5IT8Rh5JgtOSNdnv3ocBal0N4FI62xqo24hM90sREN0MbGTExXXu37uuLzS6wjLDBDVhaejLoEKDHQjJu5jiAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://telegram.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=kBxD1zHDco6KAUZBnb-PkR_B3OYG11EsyMUeD6c35l-dx0F6umjoR2mwcSe9BRvKojGwmqKDTqweLdZu-hTTvAeUYHDMqZ3IShUXeWnrRzVPtpvCG1Gk-IBdD5YzYvz03DKqcWjdqER2Jenmf9Cwmprf44gEPse83ITlUDyWnw3-mgBWY43R98OVTiqH3_bko4ygYj2TzQ77sP-ZUX9arAwktbyPe9pOgH9R39n9LHqNH1L6AEf8D6tuKrao4yN1BE82NxazcJDM83VTg35FUN2doOd81TvzoHLLTr8fGObwwl0KiIyK_YcykjbR8j8PNi4fbzeNcgTyrVGghAAryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=kBxD1zHDco6KAUZBnb-PkR_B3OYG11EsyMUeD6c35l-dx0F6umjoR2mwcSe9BRvKojGwmqKDTqweLdZu-hTTvAeUYHDMqZ3IShUXeWnrRzVPtpvCG1Gk-IBdD5YzYvz03DKqcWjdqER2Jenmf9Cwmprf44gEPse83ITlUDyWnw3-mgBWY43R98OVTiqH3_bko4ygYj2TzQ77sP-ZUX9arAwktbyPe9pOgH9R39n9LHqNH1L6AEf8D6tuKrao4yN1BE82NxazcJDM83VTg35FUN2doOd81TvzoHLLTr8fGObwwl0KiIyK_YcykjbR8j8PNi4fbzeNcgTyrVGghAAryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://telegram.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeQBFatdeq5hbzCFl5d4Mz-ODpu3Ln8XKKMBLUr5SJlCJPptcXPrJqBHpJmGBqHtArLvuJB85fkIN2Vd9dV2jcXzXiRoJ3EaKbY9BnofqeGhmOMO_OwaRAm9kb-2gYg3o1u4TK9NZdeJ49Dx2JS46Rt-EGHyi20juJ6vTEUkV6D8YxtgzJxSNUshsz6MSqJi6dB8iYvX9yFUh-a-8zAHOkhWVy9C4ysYCamJgX3UpLSd8RaAVm4VgY5-OtbnePxE4snqi_fV7Ovh_akqovFqu9urqjAWE6tRB8CL6HzRiWt2DCx4H5pIgvEXpVu7YfT59lr5XfO1fw2IrGoemO3ZgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://telegram.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 937 · <a href="https://telegram.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF_OrZRXDvr0wnum3hHeymANSV0SXP58yzkAzDHkU_4Kp9R6yQNEi91klpgI_2JDvjIjHIsIElUOP7KGwe-MnLkJwaQzkx8P8nUjePXrjaX2qC7gVJxYK1s6b-cPQwJjTQCb-tBJ9iG_LgMp9tK2SImQRynAG2eufA1kwJi57KpwCCu6TzwWRS-dr14EB7qmhDB6qnrJD2bHp4UP2S2OGU1kNVOKlpwqMhukidGmK7BZLk-U3mZvGTsYq9m2GdJuMwnLqw0Vs7hSBsa0j38X6Qa71mruVNacAfk_yEPtiWNP3lykbTatmNhaqVp9tUezjmmqNeHNZvG5emGLj1mQDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 784 · <a href="https://telegram.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mroU7547s0P0UfHABR3yTb253M4Z6x6yYU9z4oQVsDtV7YxqSpGFv__jkJgYFJAIErd9m_HosPJQPBpPjrlvAmxPzujr7weggsKIiz5mYIekmNbuEcQivJzlUbwNQCLifJLrmqBgz-KZfqav2JfWcoLaeDIfB6o5_B9QX7L9eAgLX-Z3_SUrwg7LKZgtGbry7zwKfrif8dK_mV1ai0SNAMYKyM97JZIYbqmuzBqB_bXaYL-iFa_m7JdeModDwtseh_-hnBATUuIPvu9XeedFi2MFbyDci30V_yFdamM7wUkNJhv5hjAR9zeGmLPAQxqCuiOKSe20RqrVv-_BruUnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olHqrd6EC7omRsbsJyH8lonokOBNoOut2qX-aAPojQ5I2Xm1FBfJiccMES87leg9YrFyQUAieSOmV8ynqTERgpO5cpVyBskN4tb4xzZeShGZFbCdvJY5C6XIgyGy7RLGApeHLkk35AsiBijyuyU7T5OwqFRj6AsRZVlmRU9ECTQGZAQKUPJrwRq0ODKjn_OEH18-FqM8xQsBxGzcWZmS4ZcFFYIcJHqKQCvCDMVENH4j7mq9PTTXoAlVgwdzSrSREnMRnJdjJ0iCK90P7l1oLy8FLMxi0v7L76OgKAGWeQ5daBi3qdwVonX4enDzg1RQcszQ_HGfPIsmvzfPeAzdKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 805 · <a href="https://telegram.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 994 · <a href="https://telegram.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agp7Gx6cqewFJ503S7oE7kYZ4QQPbFUHDJKPxIUcISOG8Ao03tZanA2sxdIS47Oz9m8GUP6RLf3rZZhyd8UVjYiT-wySTYFbJhrDH8N50pRYbeZNyDwGDLxwaYmgJ6Nxa_e_xj2vnjTPDjwI2_QosnEaOLy6h_X2Z3Igq3Vb0Ig7-pgUCye8y8Weue5HckqNiJ38Nf_ytePp-BUnlN5Ud8hs-aS0zW6eE5IHIS9CUEeGQGtkRInrdK8i6v1yX3C3Zlv4fuIUkfWbqnjI2B89-qCLfFFMwUQbZZdHC8h42677Q95nFmKp0KIzK6Y8vUZNlyg0dEXLIe_RgUfbqMkMZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 930 · <a href="https://telegram.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVFGRUHsCYvT2p-BAtbtYOYkLfUQLx8H_bb1sj85TWnfokSQo9qeGS9v-mHwh2UdP2j5uHspDYnys-4z5-4RuHhBRcbMdfNjzqIlnZWhpE6KRMScAFSYmlYEcKRT6An_b0LVQHyCLMOmzm-ygu1bm4NOdZ23lztyRTXyyQwN0iyiZdPxND4BP6nChlPANhTI3e_lz5UqCmOcULb9S14WufnBZjJZiFc6OIbAqtkR_-uZPhZSBJkY7ZUpH1RmUXV7_1JQ-csrPLko4yJzglA27jApJGH7bXJA-dmg_seQcD_Y2umYwmeiUPK3SmRCgSkTLvktNFzDzjQOFVMgkKlaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 749 · <a href="https://telegram.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKYI45_Z5q4e41nQqBeQ0mYDlF43VCeruxIF1rVlialz4M0RP01fJWscPWxXucXmz90swqx0Z-A6J47xDMLz5Vki5NNh6bZ6lt6kzMKekiv9qBu9Uc8CllrGnYb-ZA4ktqWD9FEoCBewMZvQn_7z4-7h1sdr9G_H8mh0-v7YmRPUeG8dCwDEIaVor2vsJiCqG_85gxG0gTO8a1LetdHD4p2O81QW5MuZb7cdKIAZVJSSyW5FqfN0Qru0g4WeFDaNOs-PlyUgw96mrlohzgLz8hjo56YixmzMoL03UHiOnyJcthKad0WsYXjHyhoQsKlyg2cc8JtslZD9sqH_q6hlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erAcTUfmo44AB6uWXJKCILy9dtzZjJkzMyHV8KApstRva1QRhFN-qPXZ5VjcSj9iO0l-drf9TOU__mpJ-7q3eM3UcagL-oz0LSRiss8NaVXAPbk4OuM5KrJUHBuE3-pRe1NpJ7qACmUNZLdEz3oKn9k9sIT3jlbENS99ZxethcHLc-CXfzOenUusj1Dy1zWUcWRTzhwUHRQk50u8akkGuTknFCybBl77QiABTpPlCYNF079aFBsUcfpik_JK7EuZySWj8ZwNLauVphsYWUHlz-LTlyyvJEZZfMsW0qdXYyvq9CvulHQsfUfyQnMv2FjQ99Va4zxXLTDYHkQvw7kPjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 761 · <a href="https://telegram.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4jefKtdSKVTeSplOAnaNffG-rR2tYZ1YTXCMCjlD3qsZKxxUeNH8zEfJnUvvRQ8NmxffPUvGpO65dIrz3fgGmtoc4c4kilpEFT8YhF7qJOSoTinSP6SIlz9NFhlw3e-y_PQHs58lurYhAi5xzHVqq5ctp5Yfx5VlrTYmI-TzTmKAmz1Hux0BPRiy9nKFvIIYRxkPolNxMl6fGcwHlnF5JLIIS3hCGYAs7utpNIgX5YgHXe4yXMAKNrB-0gc8BOZDgvFV_npBNw_gxVAPjF5lbiUis7K4Eu2rt1bvWQWNZPWf_sMLdRHQuvvLV_tRCedAU2PofKvaehAh-E5I0TOHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 675 · <a href="https://telegram.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 817 · <a href="https://telegram.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 823 · <a href="https://telegram.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://telegram.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 722 · <a href="https://telegram.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP_KWqAbQZFdMp65faE_Q4rQPQYKpfDXNR6lkcCDoq8sdG1j78MIRDV-oysoX1K2H_UckpjphFHKs-SSf_dt0fO0f-zeFZ8H2-zVatkYdGjOITik42sVUCo9GEcDsdF6jlfQZmQzpi8E74ofpuIza4XL3nDQi3DVBVzH86HY3tPIvGGaG028JoaGOwNw-s-dyLW9KUUp1h850dcp3iYrD1uWqZH8fuXrOwaJlt00oTuCxfL1hPLBeA9o1qLrNzYzUY4SXAdFRUW6OecOuDa_Z7R82dZCIFoYm9ChLntrW4TypAEL0npa25X9kvW7npq75M8H3H7vLxIcqPLTKarlgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 823 · <a href="https://telegram.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rD86tD1H9dG5bubFXzgCjpDNJ6nKS8z-h6DDocphc_O6KjJqMlHsYKcV9_qLvSBxNWLKuWeZhSNMknz6CzoaFfZZxVBnrm5dR0PFEIOpPYYyzlqJgYTuPEN8kPV4T0xdiDlYH1gKoJf0kCLqzeMzK80nSE5xr2LMYQfvnVtfUNXfI5W6gvh-t_HvM8OEp_ymTn5uGo9llW6gD5hwtAT5VyJ5S-8IkS7Q7Mu-Bn2xluRMZo160qdBAgeRZjedNqwaTLverM84MDBoDWl8sBr3oYzoEpAgNFITlDFqBjf7fKzKPhqLq3_11M6jdEzdA_i7oeRM9iRTb_MLCht7_cJdPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 607 · <a href="https://telegram.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKwTzl43jxaSx2XTEozrZQ2b7Kw5MlTJJ9k2v52XFR5lZPGS9qvu1zIAwUd5CZyCANXnBWMhCr7EKUcvfMx0SawtSB63EUYHU_Utii6mSO1NN3GuVREZehp6mWjs28PwDePvT62e3pXu_cRv408d8xQjCboMoOHyTqb2vAdX9Qgfz_oGdFGG1EF6kzKiBT4YHubPlTmX8Sg5sszS_dROhbCE6Fm3c5ngrR_7ll0n5wW7DQllQ3dNticre93mUQxHKXVUaQhhMHHD8njl3y9nDC8DIGGGzu2v6DPcUNPGV9p4704bYmVtbW-8WPYeW906i7FB7eEjQWUBAeqhDKEiWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 699 · <a href="https://telegram.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 643 · <a href="https://telegram.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ub-jCsP3wUW7CJo6kxVtk98b4OQpgmadLgD4A350kc_FTUCY_eZSU2xgT-_09ELTNboWwoLqspwNVu7T9BwOW4ofX_QDVcoY8WLtiOsY1s7_rdRy1nJOlmsZEksQs2IKwiFNsczCjx4FvSPRMGMM1BNS7cIkRlBMAtkAXuxMp0SHMYhelHNjoILv_W2xBj3cqySm3aEvm8FDifaIyN7NhZTSUY-QD9FsKQlMj6heBq-YLRF3UQncBqg4mCtjR1XS-Qe7GROfCMDOlswQS0Eam-XCgA16jl_QymsVarrXMFcO7tLOTSQrAGzClLJAEaXzaeTI0NfIkmQ1hEVCNabR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnqzZ-Gl9NRrjmNW7-nPsc81sk9SMOW7_pBtg5ipwWybEkFHcXfjPTQRH2lPQTk9SBLPvZ9i8FgEshez2YhNLERqMs46fdgHiCzY5ybcTDdVKJg7T4K9jznS4JdkkTzHQ0EyTWsZqSuyKCf6i6Ae0I1QZinVZGNCfJoNmPZMU1fUcgLSK8nqotuwagc6VXL-CgXISaT88jt0DWOr9d_yXq4PpBVfLAfUZEITncGUus741dyVW8XQOkdrTnYJsAJzUcekiuNHk1N1-YHOMC69Fra6PNE6mmirp8rZaAB72nn1pAi1zDOdh0C1OGAai7J7cyPdDK1LZszfqqhkem_lFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYNZPWXK6JT-d7uF8K5lLfP_Rn9JxQade4VaSWgjCqzz0q3l36ojMwoydFyqhUr2_tZXulZguZjFtO1B1FBuk-apa8ahBx9sJEnzufD-D9_ZJN5gscPnGr-RFP4BfWDRYSvbrtWI65zO3lZPNxF31OBuxTbw5Ewe56xy60vNm_9N32zehyzE05mmXfN8v06WFmUiX-EXXytmxsN2X2LFqEdqUBwcwRLdkTwfejfBqACvZ4Z6N6-Xg2SIEEInNOqLfhiDqkPFF1nn2bfSdMGSTYcfLWl6VnwM7ypwAhzrn5o3aMvbBPtKR3_rrng_vveuHM8C6sgG2fhCg79SgWCu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1RD1TtunM9aEToB-nXOIOCr7EImIyjNBE6tuXbj4WfSoptGZHIMeWBsl_LBN4NvRw2pEJh_9tnGNvfq0p_KGFZzPqM57K0jl0WRwq7Bsvaudjjd5MmDddYx7SQXQj7VaaTHWVxp0beWvE8gHcZ1xbR6oAgi3QKIrrSVxhmrpGM2W-Qux5H5_V5DLv4Jnv_zeyuF02aYMXj0Z1SneQcipukaLGcT2jJn3tX-OZ0tgnmM7MLJmbBDpnmX6x5fJVcCeo45JhivmryNQ3e9Bus-sMJT8Tu3A74ce8irkEITXVkKiqkj3LXJPHyefI0lZIKKJ5t_T-lVS9O6xhicr9JJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OH5KGAbr59WvLPE6lt74Nw90PqpdhH9C2S90ktKJbF4qkAMCYcLWztNk7Ubh9KLrwgmpV1UTYH1RfZagPklm3aiU0cRdPEzCLbDP93LxdvGsi0ezGevK_NL3eh4Jo0q6BujgbsxxT0ch05pVMnGQdYeGc-25NBBjxA2u0IhiiymVoZwv0fyVO3kcKKxvRkFI7IIkxBAn724-8U7Yi8XXtNtexevPuu2oGGwLR8y5EoFe2x0bB2NRUorxqq4_3q4lGyvm20tt6fZDNGwlS-ehZCUKdDbhioweaYJoQnJNSEblKPsNwrzIBsjxg2VIUgqdlfwVsecyrcuHO_MVEioN_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 787 · <a href="https://telegram.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3dv4xy_uDgFaqxqP9TNlexzj_Pu9MKMoyHbCROoelAU3W6HbqkxxnWkpG7KJLlQO8-Nt8pTudyR_WVRtuP4PGLUO9g28xp3JcNzE2Ogjtf0P6rBcUSQzImlNtv185fMa4W9TtPjrQ4rN45a4qb2WAQGz-w8yXc-AbAgtFLRqcFVULLLBjyEvNL3yABb0wPEwomOFWkD1mRbAgnB5iYu-bodMH4O3sjyWpdR5KKbrbCw4MmJ-TkiWFHMYPFlS7cKLGn7eUjE4Keu9xFYK-dTSCrVsiRT2jCgjLSOJ1VdCLXcaGTN2wsl8sfRuD2uL2mayAYbXr-wYWHkGQHccEZYrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 583 · <a href="https://telegram.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DymTjDe11IN7n_a7gD8MTDZkI-NT5dWHkrQ5tAP69G8vyYacrlxisVpsSlqPtAQ_41VW4Dn-r0ytJ5MYi15jcT8x1J9ssNUsI7GaeLDAmZacsLdWrWKUm2ZNtb0e4KwXno0vFeDurCSAkh4HEIahMAUxH5W9_s1zWNg6fhUfMbpSPKbRxOzulronQfgiSmDK0ohYSy1-sC3ZmwkRpRqrayFEgdzALGHYb8wZn5pNUlG63NJEXKGxCEIpqmwMmFrGrcSCfUojwZbgKjWJSDv2SGUN461YsxDsogAbLIkYKVMtfg8TRF4o14waIQe0KA9Or_behuV7GacdAOlXbhkVIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 595 · <a href="https://telegram.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVpFM8nPxQxcy9BxK_Ar_S4uEpyo2nUXgbw2QXReUI-HIr1nDkOv0VhCvNq9Hnd3Juz2oyaivnTK_YwKgsjwdWGCosgbzbqrC-k_pcEsHnF3xLX6uCv8SwMEXJlZXYp3RgDlutUyFDecPdOZPa0TmhSBZgcgYmKF8Ph_tlLBrQFP3cn51luaS_-W-74V8oBdO7sHEbgeGPJo1D6ib_EKZpFZQfgdCgk8CIhXMBvSF_eSbsRRSK4XhaQkOa_-DvBBWoan0_BH5H1aIBQAv16ipFL0IQ9Z-9mBJo-CN1DuocVo0b5YQHH1CVQFfOrAiMv5rKmO4BnLCjIn8F25cbBhcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 703 · <a href="https://telegram.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY_wW2nG0VPojEnxo4-U4uCag3IWEMcwsVKziPLerkq5gFD2d2f6v9fGpqOX3NiS_WXK8l9cC95OsZJAbAFxCdMnfVonLAYEbkPdrpTTJ4asBPbYzu3RiHthj6FOhPvX_n9umSOiO92dBjN0bXpA-iaipwEKbp_CYQ6N1B_EmpLUlVLJpoR9XV8v7aswAV9EkaPyXVG4JzN6IdZl_NWwzvJiCtyOhr0wqvwSdS_1nL95Afi07yLN51UoKpw3zupX6SSn77VGnXo9Az8tZQ0LCnOqAZUX_v_hZByj3S6E49pxcyHCbntpLed0ZeGpwQ2QxTIkbInuJ-_1U3jn46eXvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 648 · <a href="https://telegram.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG_DnEDqeQ2mXUNV3wtd3t2HpIFwd-hqhPQf9OyKTDEmhmPB7Nptxm1MRp7PBu-PKDGXUneYMvZn1dHwwdUOz3ECF3AUyM2fHMtwSuSa4vFaTb7fZM3VHmFHSj42efl8Qw4Uhf4WXBnF-DX20p1yWwxNN8jJV875tPtVanS5sMDIgQDpCXq4Xwx8fonX0Mp1nEsl2VGXk1gcqYWodzeFVa3M9YeG7Dn1VWGF4KLCFcHrF54iEhp5n4a7GLNPuDUmui1t66grTOSKjkwX5LhezeTkAQgenN-u9Rt2wrgfbH8O3g7MPk0VNoTkCp_CPOh7CX0ywPOcKx02WjdgzA2emA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 716 · <a href="https://telegram.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II62kwHo4HubbfltDXPw_KINGQqi3plH1Qa2ieK7ycEF_SK8uMMCmOnIRpVlYJndKJoBMQh6ISP7WjFA152_D3RgSN9dE42ZPnzubMSp5g24hwaSU2h7KK2cXzZxLY18Yk-NYcrelcyIW5AVB6sY0H-RljAXJ5so8qEc8zwMKRMYVlraQ9xE1zhZJAmqqYeaIcqpc90p2pqYrm4Uc7vfUQ5gdHwsQr9JAdeiIqy7vzP5EH9ebNhMSEle0XP3RlhvqU4hDdZRBu5uapeSD6dSK6Vxq3uvbgIZRO-iCQrwzBjNU_mYh742uKBvG2AZY2-ngTMKCi3ZwFi4AqTMtXySeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 614 · <a href="https://telegram.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPQ4JB60Wwhv0aLD9DP0db7GiF1W6x_hcKCl13GbagaFd1diKlJiTCEu5-9qcB76l9OfZj7CA_cxexHFJTg-YvXt7Q5n9ejKBvO8zA6dbD0sIWX7iCmGqjXHp7Pa7FCFDbrjv9uDf7ybA0TSGCeKVnxhGko74fPCmhPecrE66y2ZotafZqkyu0In6Fnhno0WnHcOjevGOgGE_xwtlVjr0bfFxTOlkCV_Rq1i-dMTWVdwBwt6JAtYAiANVxGRr9rjE47oVgdTVCyDoMZuBNJChbW6xJS4jmKS0MgnpcP5dHb1tKT4A_GffNZQdFNFjkjWi2AC5yMhBFmifeyTDnPF1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 641 · <a href="https://telegram.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfYOpLhbWnPMDXEYPpNEkN2nCh0T7OyyGnOAfeSDyJuXkvAzXC9e0bPFljew8BpXI_PamEwS7mQvGy-ftnBWXNNHKA5bexL_hOojN-7vJUqVZ2rxGct79xx3Sjvb2HqIUUM3GCSVNLPefy5Q2S0V543bH6I9UKuiksNp2aH8k26xMs5XssgaTmQvkbMutb7izc5XUf03N0ovwKfwD_7lh4lWUb-n7H8q8cpzPNIrAsh0MqC52oj_PFaGZszCnthbLWdJwbg5TzIgS355lxiDJPT4sPLXev5NRh52ZjYknie_v4N2Vwup8e8-GU0Q53wwJbMos3hzmV2VU0M2FflKAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBOjQmEOgfzYKyWbBtGpbmltG67VqztG2S3x4FX72eJcfOl9LVvi18RXy1Clt0p79ByrX6UB5_SkdwspdYNeIFz63AB4wqKFiqjqZsxEwPWjFrIvpopRcdPxSpRtn9d9QrlVjp0pRE6StsLDHyCfywVFSkvCv7fDofB5kcOxbjEMaKks9hYoJ8A3aJSIuQoNmg89_cPsgB0KbnwvDpxIz_nLLMDMJG3KZ8zfPdBgkdu25rLngbb59bTHkLzLYK0HGIo9xc3hLujCOb-Q6PCScufng5aAfRmsNz5JMSWADbx7tnNMTJzMuMdxns_uB3ljgqQ0xpkWYEQ-FJEIScai3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 667 · <a href="https://telegram.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLvvhDpvn2dC4VDO4ZiyzgUK-KFs7rrkIP7nwCWam0L6qxS6tGnjX2GR46ooj6f7HuSlQQBp2bRzEkzV_bGIwNYRbS6U2kUzFLd8avOx5jw5v38Xeb1MiP4xLiiG9m8nk3jKg8qJ_XAxzyLBeVxNS9X_Nl6-BEZhla4Uwhtu_6M68D9odl_yBEwnZmQnUFiHTEEOHdydPA51R1uwHDbKzHBjZnx8Df9NABGynuhIWGNi6Hu1LMAdxvU-Xa8o9HZnLAlVhFrh7UWQYxSUc3Ys-WCQGJflyGkSdSEiunsfnJgZ13IB2C8VtOe3W-TXYoTGpbiBXn6Aa3p09zFUGFNk1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 547 · <a href="https://telegram.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YicIWWyowEOKUtCsI5769YXIwii-qvb8pKoXa4wpjEGSEILADPVLKXFt1LMrYr41V71eq7S13CWVyplF1KZPgaPpqfSBwCgop6_OqLqMZK10S427AFjuvmXcCWRnZzaa4lICRa4dS6W6VeUFnz1WXCrX2CXS-gN6UZmnxHNk34t8-CdXatMkNvdDw7ql_cXSkvFOyB8Ke_Av_dgSZaBzoUjMCNI2qRg9XNqZyUk8EJrkaXC_iTiFXlD6vInBLU8lOHpQuqim2tZsHsSWR9ucfqljZPY3pYKUQYkhFjCl7b1x4WtFbJtfvlv3TgvvUwNj8UnnBJ6EhhNZdNcecaDp2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 546 · <a href="https://telegram.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdsTXCFqcPOT_BgD1FZdV0RH1QjBwlgm3ZZBzVxqG_E3WQuhApchytzW2jvuuw49bAsefTRzMM9JoPbIwmdb0072Dlo-tq9U8BDvu8FBKoOkcKartqA06MxdApiQ0-OiQzFQgLv1UYuFo60HfwEn-RWGHE3JLuJ6Zw2sjJKfplLCEguu5JgEqJ06AQ_ecHClJLIUXQbXb9fiSagrmmat6T8_krurzD1NFUibhDxPSGPPqafGkJvWErVYdpSJ2M3zkwKTKH_UgHiG0r4FhsODu6CYCaeEC39ZM5Z8UU6oSmjWuQREqhCsoBhNXj56mUZppJXEe8J7YuYWs72vsEXM4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 671 · <a href="https://telegram.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPzH5xx2PeAokSYLqmP453nj_yEe3HOCf_j9XRBV74egzVcXvVEAAAj7zStuwv_4sWPJ1uuOeqbjhWLLg55q09rX8ZpmXSOnDafdMXgCkWubxvlAssLN01UL4Cu3tyB-U77BMEjvv4IGTXL1H7BDu2tZ98xlPeu5IyuyjM7KWiUxz6cHw_rYnkihI2nXXoccdk3z9Rptb6wPQtYJGQkSsxN5_H_sWCQqbVBVmWWa98S0V1PSs1OLbgrgLNNYukndMTPQ2d4UZ3kz5T7P5Bzl3HkiDu2ovs6rNwHinQTteZtKK8Ec6ENV_6SDab5T3M0ZWXP4A-MI5UAL9dAOw2bLDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 685 · <a href="https://telegram.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 693 · <a href="https://telegram.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 877 · <a href="https://telegram.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqLPj9PsZ2GetRH8JQ3e8lrU8xn7_9ajXg-C9olgxlv9RbZfeCAeTCZNUZicvDeeA53UHIj9vrb9lgMVsro_PxoM4-CJ9AVDxseBMZt7GYEoEQ155Z0ZO2I29UUQQqNjDKyt4fNqg-HQBhQ6_z8ze3dQKdFPcmLQ77G2DX73gV07Bp2IQ4u-Ce33oZaLo57l_gSjoctKFsiUiKotpi_MDktFfR5Hp4ZTLi8RhlMhIc3gEn8rQru0v0GEBY_H4A6dtgbaLZK1_nYzx0XKACQG_7VKCP0Hd1NgTi6xzXMNdZkpG3HVZeWwCFTpI6nrB1JCkZ_2iOX_UzujThIkCMrdpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6P-sI2Zs3IZ4S7MqHDcE6HXl94-6fOuXorNLxW4-PJQTaCC26lIfyXI5Ot_xLgIkDCJFmx38GqpjiYAeFEngZiU_7c_gsFL2po_lk3ijmDB70n-pbf6uXiNgm8iMOCzJj--pC-Tyjsmf6musmJP1-7fnxB4kwixWc8sOWy_yQLJm38-59qRUExeGZ0wm7N3h9R-mTrVNqRzaMF4Bm2R8K53xNiCwjfGk-H9mMdGwGrZPDRsidJfHVAEamX5Kq6cXJR5dk42IzT-VBmyUO8TAiDJ33Ozm8E7mHUnSECuyE5A2jzH-yNCvIhoH4IMUkW4UFO1ljDDq4Metv66udd6NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 817 · <a href="https://telegram.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6kR4_Ozvji0fEEKzhDdBd4sbAMUDZiaJmjF5AyLqRVgR2zWW77Wj8RtBDt33l12GDpa5AgwlF3qMB3wo_T247c_96bQQ2_SRS590mq29C53OscjCz4RRG8aHYTkS3C9rDU1AvHHNkUj7wlkK8_8iODptV2XhCrgf0MixicOPw8k-6W3NID5rVh4mWjnFa3h5M79jxSkrFFyNAWAuaB4W8cfhoi9EbL2QLB6CmTmSMRitY4TzA9TZ019Vvl6efJ1UFPI5Cg1J0GXA__rN5yHxv0Jio_JGIhuJqfvyz-lG0yG0cXS7UGBDz2KzIaRB2lLaRgOvg80RQC7Q_ObNGtmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnJe9lkVsgE6hXLlHZv7rMblAV0svD1MhPFyZnUVcQtRbpbaqYbFcpuggCGf_9S9MqqbJas33Vh7fxXdaeXZ-Vz6OjbfX6HMEJ-0kgfHaqGJvuE3-ayszewlo0cpMHWJa1W_KKsJMNAhCK8YSJluDC_gPgvWvj9_oGWwmeJ35H2eRKXfFR3cA1P2O10UxY1CkiPBZb5cMWEsUTxDu8o9ZnlcXE30dUQ9ZH_RG45EqIoJyDq1S-ytkQARricw2RpYAN0kmu91XkVPoAPX08oc9EVYJSxQAR9kCaoUddMdZ6Q7Wi_B5vZYxTds506OjzLhZ-H0HD7o1_jTyoU5ClIzXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 808 · <a href="https://telegram.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5xOBkfzgGgeKpGo-ec93G5O9T810YDUpsv39beARZ8qnolDfSACho-wR3hzUDn_8Zgnfh2gWgoKDCuC8bV9eZc-FpI7YZIUspKMv8bgKmnhzEKffNsxj5xdkElI8mlrSZFtUOCTcvHJeoPQxE9OBi_fVv3mtHHbD2Q7hg-Kap_GubOkM71AyzwXeemD4dfCvwRicUYEbxD1pTkiAYw-0h5et1Qe6cmI2Kd2m9rblvyZK7eihx66rgvdB_035zIFTsIGSDe4prSFQJfLotowxS3zM6VOMiWDBAsGnOKRT_Wnwu0x9fLZnncReThF-1e5bP3_5z_75cqY3qYlS-A9ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 588 · <a href="https://telegram.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 587 · <a href="https://telegram.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHHF31gt2QTTSYIRjS7gorXZI6bxs1CY2wu6-ZuVEaAdBz3K40oyKvmXTG-9NEBrTE9nDYOslTpD2b73tMi6PrspWy-o5EBlcBHmR_SSj5BBwQ7Wfd_jNvpBzo8B49IJvzShUldFW83fniEyEsxRggzEQtLQZAlYZJuLbi_crOKEdkwARG-w_QFn-5n_PPZklgcfVRv2RusQ4kN-OPVyO-x9W5ZfLAokTQN8GbryLVvi5DDkrXzPETgr44wXt8udF-u32rUK3m8jDnRP_Gq3DkcCis6zinnrXyJOGRWu59SMvtQbL1hXUxty-swl3EoPbvM2A2JJGG5PjuCTwG4_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dV07CM-JwXt81AddHmKvbUbrE6aXL0ZVupLr-ohaSjkUfIqxBCRgGtaFY_HMh5MOQNdr7spHkOL7B1yFXQxFtT3_atnPbDkcB4HV0RM6A10vkVOrDUIpMTQpuar60Wbqvmh-W0M0TZG9OxkQG-WuyUKIqpIYSA71fG7RR7AS8-H5LXcOQJuTPOo2YxhnKtiMj01A-hDNWx-ZDpc_kig-DN2c9fcchyVw2NlTOTwMv4BkTGkLcBHT6b7u8iOo0oJVs5c6tKsM1JidRGQza69COViIDAm4TopAtjT90JUb8sqmuIasLqhclpLzZncKdUtewe7m9fjj7liIIWxF4_mpEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 676 · <a href="https://telegram.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 903 · <a href="https://telegram.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 884 · <a href="https://telegram.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 973 · <a href="https://telegram.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6SkLzYzGAbLCZmT1so-ojK56TFGVVO5vxa5L1U--TX4R_4ydBlRrRLH0cAg_8fneGkxClxBJy1JWHTMTQfYVzoY7FW9ig3V0uj8rUDB8dHD-WmvmxusPkckZPILS5mWgzjvon3TPC7yHuO5SdsXlyy50byu5gKBvx6daeOi5sYzsY2KPhCHIEF8ZEqhN8fKAeYvXX1FtMdsouqfJTVE1FyeTTkfSVqhsd42hGUUClfFvcwO-JWj0iSGPTdNnQFzTThJLSLw1XiIFegoOljpHm-15fnR3-L8i1b7wdtKkiwg0gIz6GSOmxqx9zVlMrcgOT1vEohjOI5hSqGpMTL6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 718 · <a href="https://telegram.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRmEnTco_F-83sbEA2j-9R8WfMr7q0HpeAC6Ab5m3KzskbkcyDX_T4dis_SZp7Vs30RVBYxgFcq1uqSbm_eYhoQuYEGZx9_GUHDR_dSme8081uO3oIxGQr8EjGg8xi4EhVjkCnWcHNokgy-wVoIJN3mKZ5ajSKlLxf8BdnlNOutmyFm14e15fYHzRAPMYx8ofO8LcH57RJBIqAZx7rdMEKWWonc9eJzfebF9RV7DRpwE7OfWcBPRl192Xt4gcDzHULleAy0EL2v6__Shea_BA_bJp2k4IkpiqGfs15X-rvnrQ2MnFEkhY6rWrcHX9vwqVo_CyR6DhR6gNWpipIf9hA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 775 · <a href="https://telegram.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqZHWnIS5UKyIUUv2P577vqXm_a19eIFD8osnvjBJOfaukc_f20W39pvVbnTUAfQSdoZrhc8NO-otfjuiNfXWsRDsz6coWVbfSltMk8KQ94eV_9bYBTuQR-D7sQGEPvgvZ8ygm1w436oDM-PRnM7VYTs_Hm_ZWVuRibIYjtepcpNrKZSRT1D2lC21IBdv5c5ClDHV5cboWRqDfIfi0IOwwZD0bdDvIE9JGeYe5UwDmzRlkNFLEbFvZJ-4rk5Bbi2Vos21BcnO3EHiFL8h9ylUY901rp6zxYG6k_KZ_ZtrmPKJNyWIej7NoCJyEgww2OGhVKY2eZvueVxvz5KPWYsIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 772 · <a href="https://telegram.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvtLEF3cQPlbBI0ty0X1-n9ruBnzL4dyyjR8QRY4TKZ8ELs7dXgkVnyV-B3tIYMzzFeUW-Jc9A-2QmT3IMVYwiUGcplx8UkR0vlZn__Iy_Qu6QyHFEoOHv80kGcgSauhg7nnMtDRhZBHbT--Uc017-PyiNxODpTWlNk04GWHXrj2t7zUn9iod_qOfQt3zJ9uZvVkxWic3_xTXtRoa0taQaYrVqD9lX4y1P28HmhXRZPHbE1tNX9YtxSSeUYkkpLm9PTIN5XmTsFM4AUfzEj0Vbau4VJ4XXFEHCjoj5sPv6tsY7R_bL6zArwSIMXCfCP1eKF6MDqqUo_UCQtgkxVcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXv8glOYWYMW4TaJaVcu1BFIx0AMGyGzSvwmpXa5-Tgqbt7NFBjZZQFKEB1OeRTU1FnpAeKCsepyCjL-sByKrZ-ymYoESnIGyGIwZHp8IejPiP8bChZ568mcnqb5JGdl4IgIeqkSiYDN16_s_EX6AOlmmFU-f17tX6yyG7Mk9bFxS0CcOYitqoYIrASDr9CnShe2VXQMjv87bA27izX-EUvXcfS7LD7vufoJEHn9QI3dqRW7JGYNfDSNfS6k42tdE2A985tqKKOXJYc3u8H1qSdoPtLNS-_eHpsG7JIZMetIeP4Flc9uMqV9pniToWxnPMnvQeXe3yQQBydN_RlSDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 611 · <a href="https://telegram.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj2u3MxGq7kM5qHZE3L_aHQaNYTR9_yH159h_9RChPwlSJeRzRJAOnuRIzeXW_TuR6JpQJtZ92sp30b-BuDHJNsnFY7tQkwDbU-AQep9oOgj4FpKNLeU15H9RGrXLohphxtuf9p_o7vuzQ-XT3IPpPmOptjf8WRooNr6uUZHTQakM5fpX2JSntfEHcmTcTPdg0SH6N3sOmxo-V7PWJ3TwdCmOqOmRsHRiHYRW4QuhFXx61UIl1q5F0E1UdUYpcSaDYmqigH36EE6tvdk641kvIkeHw0cedFZQ2aBOvDVHkdt58LhUjl-bnwdStcoCGkVzPoiIFRdfjDEzeiBUOPTQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 622 · <a href="https://telegram.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxMIABnf4IU7d0k0owi8pZIa7IMw7KALopafZRfyEFstYwmxfzsrrgoRVB4ieshEbm-uRXjt6x-9GNO0h4Qv9vxxPRnKfftaTsWr8V-u5ZuzByVznq_238nXZ_FSsjmckvkXUJA2GA0YnYnbQ_NkPSidlH2NPPKBqb2mpwAPVhS3tgC_tu4bNfz81nRgO3v0sY6k-JlaEoCHZmfz8zjMJLxYTynJKrOKJTt-NALYCxqhpbYyugHm2WsFuOv-ViR4tNRSgoh-6fs433LqzZrnrte7KRNZUuiv3nOtlscP2-l-UEe9f9Bw9Y_4SoghLvWKKoNVSBKAiZefl7krd7BX-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 663 · <a href="https://telegram.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 611 · <a href="https://telegram.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 674 · <a href="https://telegram.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 675 · <a href="https://telegram.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyPpMrnDVhGRJVlHpS-gSW8LnZtXWmMPzgNhrFV1A1noQPQVEE7caCkCjX4sfZVLcHICowaCQvj9VrTGTlF6beJwPBxKvrLe0qYV0SJdEGu7ojoznKER3QKdo_ZDL8J0up58w3NN9yuYgzLGaTZnrxkoGSm-tCacwnvRc7Vyuqzs6QuigK2ckIbj2T2a1rW4F5iG2Ojvgys3loO5evrjyP4rHLnOoDXN7JozgtwYBHVbmnFDfJF6XwtC4bGs3m9rvQZ1JRW4a48xLEfQaQd6MQE0T9Kp82a289zNPoa9pm0uj--8QnTfoO05T91V3B-EgRcFgVctN2Fg8GvzDSBYTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 660 · <a href="https://telegram.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYvZbjZ-ZXDYb-gKmHaydfob0-SKJ0vq_cJxynJnCB5RkFFyKNP54UWE_AMJbhZocYteBeNbIPFaWJ-w3QLxrF_z3PAVSl8rPcDG2YKHUSeMKlkpXlfT3Hx5WbYt4k-9fIMqdoJfYM4INiuSa7UvtI2QPp4yv5Oh5yteUS4yDisaq0PzwWN8SoOFv4Mipq4SEFRezDvIdiVZECnCr2nMWjLab-Er2UOCQ7fUDu8oohtd5UxLaECK9sXKHJ5ziIGBFzuAYmhC0KhgOqiyVITXx0njTgiFB-MnYkh0suq11LjvVKO0lrcnXSj3o4NPtTDES6hdiQkGQvGdCiyIIfRk3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 703 · <a href="https://telegram.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=P3hDikJE-dQ52W-BcG29xYKpoy7ce8xb3ACL0gcPAdT233eNuN-P4Lxss0Gg5uRNwiSr_RicewlXv5OBogHia3XjsbNnjPHqqXwBJ3k3WJReha11KFH1UbGVaP2Nitowg6o2DmaxoN9voCXGT5Ac_Q1u0sxjEt5ri6Sji2V_PW5k1rVXnPCiHXBVYh2tQA_wq1QoB0mh0Hoipvrms-nlpR5Ic_Ik-jNM2srpemyxMQ7M8Sye386MVAAt9_aAhx_mm_5TiqCyMTaqzJqdtfaU9ApueDu_pzIznwGxykTIfghWPnXj1egZ5lJZMkcFfMH2rm4Rh94MMR_K-TYjSmJ-Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=P3hDikJE-dQ52W-BcG29xYKpoy7ce8xb3ACL0gcPAdT233eNuN-P4Lxss0Gg5uRNwiSr_RicewlXv5OBogHia3XjsbNnjPHqqXwBJ3k3WJReha11KFH1UbGVaP2Nitowg6o2DmaxoN9voCXGT5Ac_Q1u0sxjEt5ri6Sji2V_PW5k1rVXnPCiHXBVYh2tQA_wq1QoB0mh0Hoipvrms-nlpR5Ic_Ik-jNM2srpemyxMQ7M8Sye386MVAAt9_aAhx_mm_5TiqCyMTaqzJqdtfaU9ApueDu_pzIznwGxykTIfghWPnXj1egZ5lJZMkcFfMH2rm4Rh94MMR_K-TYjSmJ-Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 834 · <a href="https://telegram.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djqFwDiIfgAvWFXImUD7Q5zF8hupLHfVHYZT1IXxROxAWNKwEY7ScT6noGF0PejLCCU-bmMlhvHojA1xV6ND8NEIZtc8uFl6-UqJfNqjwpV_8fvgO2mCtoRwS64jGxzQYvrck6VZYpYG_9fNSLeqmdU-WfKjm110w-wodTbyFmPrVBMg_cMp25gKUSGMXmJDfFM2IZgFgLjJWEoDKVdaMOV9svY5p5wMDgLc67CZP3y6-xLrXIU0lhst5RblKUpubKe9f_V-Gb_0CxrVtStJBC8lJu6dk2mF1v86oeIy0mjnIS1oXrExEp8EyiD8HTJXtTq0Vkqvi5212Xtaas3AFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 877 · <a href="https://telegram.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 1.04K · <a href="https://telegram.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKJCsdqrgWkPUAHwwQQKRT64sBaq1RjfQxzCsIXJTW9q1y9I4VzLLD4rEMbpgtdLS5sHznd36AfEFtMYlcZqNAAlF26CvMRt4qQ60B0hUEUAl9sqRDdMb5vo57JwZY3XjpOODGBM4PcOCAwDH-mUG94QlxC8tn4c-km3nAbvoBaBm6jztoNmdwK-y-MusUa2I9qtPEwVaH_68cO67GjpaYpxzIABSTCkHirjFIZUAs5jOCRBxpi6NjnivNewmEGGQlEoqOGMRQ0ogLbe1Nll-2dG68IcyCSjXu_kH34hoBQCjvqtZ0QmSUzd5Q-s9gLLKqd6xw07oEgS96PtnojxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://telegram.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://telegram.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://telegram.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSgyySh0nN2t3r_HQ7LL1yLDI4my_04Avo8Ba-rAf4t9Iz10wu_0ig9yIx8EMPNYRDwJ-QvcKHHt4BhOzCtcA-UGjqedyjyX7DutmD-4_NWpg_DzLKmNU7ymDMpywqxpUWf5KbPEbHAC0L4ywIW-SVCCZskfv5lPfVUkDCH4dNlJWy8FyQV0EQ7ZXqOvRLClfY6s8M_b_7IqDQi51EmrwzjPaXlbiFKiTOivcNtpT99gtdhmi2u0RabvqCopXDKQ1kgiCYSNX85CZ_LdcZwsRjtQcl-YBlxcqAAHiNZ1Y4q8g5M8u6_tgnvMlP2ybx2sIAY80z5K7Jsvac72zJvIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRDu7uWYH1lpqcK5EI0MdTB5JcdsT5YrSxDxkqMzpgAtS8LM7LQ0bN2CqzGT_vvGidKXj-x2MMpRIj_RZbZbE0CJjRHPXRl1_Vz9I-T23caJfGWcqO0iYSF9Ixrb8EH1W-0ZQC9ZGDFYsj8dpAf1kMxJRTvzzkfKPmwQi7BK0CdYBSxvBwiz_9jeJTuDo7Dn6pwo_Y-m35QWs3yXL6OIGI6zazgQgRMhuNrfMjmErpgNGY-9k9GruFYHJPGndaxYnNPZJ3buxKpX4kVA2YjCu5YCR7po8ihM75u4GdMXJpE2ET5lz1bbSWxzI5svPXSKtS7FIcKv5AtKDIZXa0e1KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://telegram.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDo2z_FydPyss-zDpRhZca5tnbquSQjtQrnggkE_NpZm_sMJxy7b0N1uASPN3P0c9UAu1UxNQrK5IriSb2ivqcw2fm9Rv5_vbDQtDcbpEobbsNLig8l3p9x4pxVpqAHXs-2mExlo3u16Ow-uqPa4xt-jE8dq1jRb4eMDIG0CgCtopTOdrAFWDThnS6fMBQPTZcimN0FEdFhcdQLEqqtUeXxRjtbFcURyd_m6mNDUsUr2RXqWGCeFG2JKYV2ixzYVOpu6C9rKpkejNRuuzXjWZw77xNsC4m35meM_-wcRIqspx8IsY-KsD04Qk4HCdgN9qmBmnm2_eO0DnN8yLpibTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3z0z3Xq8uOANbQeIXsQq4tDYZ8zjkJZ5soRxpTyY7b2pfZMGUnABf1gDC7nTZlc2zzmrnBPEJ9AAqatnMl3n3Jz88X5xBuC4emYWQuVDPgbpvq40r3Ups3195uaGxT3tMYm6sxVY84Ren-SOezk1UyvLr_AwxktBQYr77Nri8SAPYaiGEzbngE70pp1p9H8DyNhVjVZf7ZGE7oV_C8BH2p471qfzAU86tX8twnvLKlQi5xxYN7_7RuS_YOjYyX-QmZHB7GY61P7tBXLuLBgVuoN7uupbANO-gwEUUGwEkiEFa5iLGXHCZUNba5N2XpW8KzYvwO-S4dTAQKfODNDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PR7Gzi7bl0znnnRB5zuM9NyZIDroxJo23YYDea09IqdpiLRv8BUj5-K0_lpiJERLb2kofKr5P2KHJgmFrZ-aWm2lqstd0n399gH0F4rLHBZ9fQRFiN804DdAAWftuLhOOCThfEJ5U9UDTimdu6PcEM8uIrP0ohfLlbtXi9s8xxyxJG2kpeOtx4V_J7aXm--NlsvFJYlc4xdzeCahS3x5Xg_Z9Nej9rEsmEYxDpagR4dlpdik0WSm_9wtIL87UsExXE25k_efTq4NZK2Dd-uGqg6O4BqaaVD4SnVt8J5VOX3QkshGnXsQSRzgRAeYb59S3cyQTB4NRAIVet6WOLJ3Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://telegram.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=kn5a8ryFqZcuUyfb11mIZ_sR8gyB7pNUdcuqxAQ9tAyl40ri2XDUCi0h1dSO-ibauIvAQkAbPbcM1fK0exMEgS0xfRoSGLFPdAqlagR4gYOui6btp-vaytrLkSH74EZukOf5bp5r6gX2rfZt0_UAicvZXhun06D5HcGdK3T4JmV4zQqUimmC_wGIvcEaCSRSbVlHJEqD0oFzsu_jCgYocBZoUo9J-Y1yMtAagvLinsHrQ1NXALn9P6kKO-jGezuYTbnS_uNB3zdQyP1AWuWnLvmU-DZHjxYdi01Tq0TXGianE1sHrm3A42Z6bEqa4ItBzEm2n3OPcnvP7LHWrS4ZjpJwcwSwMx0FZioA0mUDIDjrgkfuQI4WiBF39cjXoOtVLaIcgBrCTRCcuYEkTUmDoA1inz7M8tMHnqqFtsf2Z7017Xt6m6ENluhJRqHCHd9_-OiABSfBqIzeLRgHxdjePwoZ7SGhgux6sH_l_WBuzUAQsICLOSxyeVpnuu9BMscz5cs8CFxT3k-J9OAX-RewAl0ET1uAh07wCgG4tTs7BFYL39YqWH0RF1Luc5tmchZinclp6V6csPPRHGfI_KvRs6waiXyfKK7Ct6eSQsrQqHgxh853VaTpOeTCju3IHBId3HVR-RFZlnkyAJ1Moh5WyFiA2k5JcQDlT5OPd9Cvh6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=kn5a8ryFqZcuUyfb11mIZ_sR8gyB7pNUdcuqxAQ9tAyl40ri2XDUCi0h1dSO-ibauIvAQkAbPbcM1fK0exMEgS0xfRoSGLFPdAqlagR4gYOui6btp-vaytrLkSH74EZukOf5bp5r6gX2rfZt0_UAicvZXhun06D5HcGdK3T4JmV4zQqUimmC_wGIvcEaCSRSbVlHJEqD0oFzsu_jCgYocBZoUo9J-Y1yMtAagvLinsHrQ1NXALn9P6kKO-jGezuYTbnS_uNB3zdQyP1AWuWnLvmU-DZHjxYdi01Tq0TXGianE1sHrm3A42Z6bEqa4ItBzEm2n3OPcnvP7LHWrS4ZjpJwcwSwMx0FZioA0mUDIDjrgkfuQI4WiBF39cjXoOtVLaIcgBrCTRCcuYEkTUmDoA1inz7M8tMHnqqFtsf2Z7017Xt6m6ENluhJRqHCHd9_-OiABSfBqIzeLRgHxdjePwoZ7SGhgux6sH_l_WBuzUAQsICLOSxyeVpnuu9BMscz5cs8CFxT3k-J9OAX-RewAl0ET1uAh07wCgG4tTs7BFYL39YqWH0RF1Luc5tmchZinclp6V6csPPRHGfI_KvRs6waiXyfKK7Ct6eSQsrQqHgxh853VaTpOeTCju3IHBId3HVR-RFZlnkyAJ1Moh5WyFiA2k5JcQDlT5OPd9Cvh6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://telegram.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekRwtYVirYbDZfrFstYrwVYoMERLLL2GUYkR8okuQXBCgmdCMh9Fw7xO-sw3nppluwvzABGQU1X6TUOjakdDBcfw7G-oebSFR8Urt0NQrNk1fseQUOTPViV9i9xzcI52l4E9qR3hvcAM1NmxbnbA_8GEoEXRWuWqGIP0MZnuVvxLYLJgM5k10j9PppZA5GLfqNoIZuEMnG5rJkjCeS5-mom9I1iJO-CZsDZ3IT6Zk3Ex1C5u5FPdJVnWaY3c_Ebn7FKgl1IflHWabpZ9yIDDrXp4vUXonOax2SbsalsGlq16sk58bb5zQiuuh_P5mBFjevQZsbhZsiAEGeIdd0XfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuaUg6U3uE6XB_E1aaZ9CJgI49zUHMgsGJzglsMSYckIyA00VXlnYf5p1XiInLMVUb_AldamxwbAeF5EV-1CRpNc83EuCaB-rYkgYU63w4gMeQTd4AbbpBoFTsBxn1n1opLjJ2qBSW_D_V7qJP9nNk_QysJMwqnC9BleW0VGtkDCiieTAlBmd71nFPKx4SQ9BFk3kg2e1IQZ3COqtntZ1HdOBtjCfLYxY_Xv_ztqfirahTjwAL2HYo4G1dvtOBB4y9aXXVbLmPTyiZbq-7VHPV7WX9x6K1Ka_qw3Vv55e3DphfXuCCnjXiHcOSYeNtQ_UAw9xm-DvT84NGK1eIAhag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://telegram.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ma_ZfjxqISBbY6_Lfu3aAMuvaS0wraR0MaeWAWtUyv2bOIFfwsHm96zIvRpjC7of5KZHjIYCZkXrEUn17eRX_0U3Mg7wi8n__VXR7u4ExcZzyuXxU0H5limiolMFaHk1wSX1ezvgO2vUhN9FwmhpyYqDCT3HLfqVqU8g5z-ClTdTF7K81CNBbCy1ber6AHE-oYYfYJX-3x3ywYA033666M_pgBwzRTBRmYXIPzPdO4jy0h7hTE2CPucyRSaNVaPRCFWrzKd4L1_I-f9YHJFMBq-e2irl29bNO71bJL6YHop00aVEC7lfJAtngLQLGiyvDXV4ElUtwRTN11G4xUYszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4t7RrFRNj90XrnBsd3kv9OGGMY3mC2ViXXirDhAQbyIOkpWA6D7xDxtjo0JkGfUHXa9WatCKEgwgBMyhBqpWClZ9XpyV1MX-84f0CIF1eiz2HyEOBug38KZVPuaNycclVRmO09I4iyz08U4mdzmEfw9SaHJ1BmcjMEKEAj05R1W4U8thBizBBw_IN0njbqaSCPL3pWQD3CoRbdfOD2xEU0hHQjl98fBrX4HfzGn9HRA46aVSX_M27wSsyXj4G1S97ieVK4iAmbWwCnIpfFVBlOjHIfRG5M4gSZi3mlmFLFHjuTmdyOLFOil2FYyeo8dZo2c49IZMWfG36ZCBW6JOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg9aJ6iLP7IkAtrs5-o7C2HRCjDE0Ohpk1EFUP097fmrHKtn42uLzDW3E1TUeBVO088y2Ymg-RANM4M8A9QiJAUAOFyod2RAf3miiOj0myoql4m7hD9VYLqm11ga1VGXtMFIhO6m5kETWIR9T1uiIWmawxqGL_birgJ3sbLy1gPEVEDKMvUKepn5IpzC2pTUOSIPgl6XL-J0IZD1F4-zynKKezFzI28pKZPNSnRfbHFd42-qTTNmBxZIEw73kSPussMNcGYkc980f10uN1Z1vuivd-p8WVuyIKtI42IRiPh8XyOTQbGBnYPf0K4FucqkSEOUphwTrzHA8qdNzU-IKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://telegram.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
