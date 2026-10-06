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
<img src="https://cdn4.telesco.pe/file/AuC1YaQFcIQU0BSuH6A5TL1QLi3VccHvI3HEwBHierBWL2rq3n1sfXOjceoA6FwCYNrDiN0CzOuMrKYX_wHXbzBG4HaEnB1aYfr88W8zT1ni3T_t2R909oh8V2OJvV1YkQyoBzwDuyYwCPe3RpEsLsU_ypgMezIPlRJ8FyUQPOeHYNxiPJcaTleektytGm_QXS-BYbpCAVsBJmxwQFNrByLV5tuhq0t7MYL3etWBC099ORSutx--uRSzJ3spoTNxsam7toMQWxOn1IDYpKxizIZiQMQr0agWz1FoEQ93JoBW_Wgh2COhbN0GG3Hn2uhMSTpVxPiXfs58ZAuwscJ9AQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو با محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 8.2K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 من تالیف و تولید می کنم✅. نه ترجمه.نه اخبار. نه گرداوریدوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-1018">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آپدیت جدید، صفر تا صد سئو هست و سرفصل هاش این موارد هست که هنوز در لینک صفحه دوره قرار داده نشده و محتوای این صفحه، بعد از انتشار کامل این بروز رسانی جنجالی، به روز خواهد شد:</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/mohsentavoosiseo/1018" target="_blank">📅 13:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1017">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ5Mtrotfq4ba3O3A3QuPrTDd2j4QvfxZt4iFu8Mc_XT8TS3NU_lt2piVUDU5IsDo3AKcnikK6MoPCaXUIuaV-Gowc9Uuq0zzyaJSSh6B32anBMvvaQi0lcyArDFI8tRogf5jCLV44HuLdn99YWy2Z6CGxKJqHtH22W9CeIc_U7lOkdDzNKGO1-TbB6z08sDj5sVsoKP738s8A1T-b0ofxnOhLYBcSpup9gT8h8xY12Zw7cRR4xFPI0olj8tx6zbqf1B9Ke8ctBcE6yDIpIs_gLS5II3uGNvVNCVHFPL9qibG2XM7Tx0SGQY6qJ7wYTfaFWeB7Eft2Wzd8DcpNHV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کلاده. Opus medium. جمینای هم میگه! تدقیق رو از کجا اوردید اخه هوش مصنوعی ها! منظورش دقیق کردن هست!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/mohsentavoosiseo/1017" target="_blank">📅 23:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1016">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
بساط پکیج فروشی و دوره فروشی باید جمع شه!
❗️
غلط می کنی آموزش رو میفروشی!
❗️
کسی که بلده انجام میده. کسی که بلد نیست درس میده!
❗️
اگه پروژه داشت که دوره نمیفروخت
❗️
هرروز پست میذاره که دوره بفروشه آدم بی لول!
❗️
اکوسیستم، دیگه خراب شده باید پاک شه از آدم های…</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/mohsentavoosiseo/1016" target="_blank">📅 23:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1015">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نوشتن allow تو robots.txt موقعی معنی داره که قبلش یه چیزی رو disallow کردید که حالا با allow میخواید استثنا بشه. مثلا یه پوشه disallow هست ولی یه پوشه جلوترش که ساب فولدرش میشه، allow.
حالت پیشفرض robots.txt باز برای همه بات ها و همه صفحات هست. با نوشتن allow یا اسم بات، صرفا احساس بهتری به ما دست میده. هیچ فرقی تو عملکرد این فایل نداره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/mohsentavoosiseo/1015" target="_blank">📅 20:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1014">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عصر افتخار به محتوای انسانی رو به پایانه. و عصر بیخود بودن محتوای انسانی، در حال ظهوره. در حدی که میگیم: این محتوا که خیلی مشکل داره خب بشریه هنوز.
که: محتوای من از بشر بهتره. مثل رادیولوژی که هوش مصنوعی، انسان رو برای خوندن تصاویر بخاطر دقت پایینش حذف میکنه.
پی نوشت ۱: ما(تیم ما) همین الان داریم انجامش میدیم و این عصر برای ما شروع شده already.
پی نوشت ۲: همون محتوای تولید شده با هوش مصنوعی هم، دخالت انسان نیاز داره. یک انسان که بالاسر AI هست اون AI رو به اون قدرت رسونده.
این رو از من آموزش خواهید دید
😎
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/mohsentavoosiseo/1014" target="_blank">📅 16:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1013">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
بساط پکیج فروشی و دوره فروشی باید جمع شه!
❗️
غلط می کنی آموزش رو میفروشی!
❗️
کسی که بلده انجام میده. کسی که بلد نیست درس میده!
❗️
اگه پروژه داشت که دوره نمیفروخت
❗️
هرروز پست میذاره که دوره بفروشه آدم بی لول!
❗️
اکوسیستم، دیگه خراب شده باید پاک شه از آدم های نابلد. پاکسازی لازمه و منجی و مبصر.
❗️
من دلسوز اکوسیستمم وگرنه خودم که نیاز ندارم. ناراحت میشم اخه...
❗️
مردتیکه کاسب پولکی حرام خوار!
❗️
آدمای مادی و دنیوی سطحی که توشه ای برای آخرت با خدمت به مردم جمع نمیکنن و شیطان، دنیا رو براشون زینت داده...پناه بر خدا...
لینک ویدیو:
https://youtu.be/MqzjZt7H3_E
خلاصه متنی ویدیو برای بی حوصله ها:
https://share.gemini.google/m3Vz2erpvShs
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/mohsentavoosiseo/1013" target="_blank">📅 20:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1010">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-BJIkxg9p8PZeLsBV182Zu4XJKDDdQpKXHjuINonMboJBD4TkuAmf4QnY6iR53Hcd_KFLBoIIkG0X2gPYb-kKQ_Qfu6K8ywMjORlWK2ZkITmHP7i5oEnd0vFUp0XuYyXGHdU1ScoQboczzI166vhG0Bjmxgt55nZEd-0kGKyH8XTDQA-feM4y7ww6Df5NdoY1PSPlv_k5jqEZyXtTkjskWAtiP5tBSISbWAxSwdShZLVOYDQzfX1wmk3jOnYfpdXiKGu4ggvj0rQenoJRpkVIek7QdQaixG30mMkiwBC2RYxtdtOdY9D7FZbji7aup8FLXyu-wsTtcnZltNrz1cVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qst1_G9guPQgO-0UlOtQqvmU-s6OEF--YMDpMYR5QLTxFXf7QrnSHekEYrJmmIx50sUxtH9PzIYc_gFPb5kVVe8B7Y4eXySk8JqG6m7jgRNolxyks-4YHGk5CJNwrhum2YrSc3pj1DGQ1zXilRPdVC9lqRObkZlvXkGulcobgSOoBVafq3BVTR6kl-YTe-MniK_TISq8gGdftit5zxrvneYd4odyzoGMW_NLTkolMrJWTShOhXzC4KcwdLL-OLFHOoC50u4jXPuDd6Co_w6zcEpXNtNi75ynwrGtOMZYTtAHI1D1eVHJMCKT3M0iS4aS70AfZFZwyiEHii7RCc3ATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFHvCFiSqR6Iz1HRXHPiaMuWj9I_re8szX8vSPmwksQ6WoJWJYb0Gl1VrDuK46GwnOCPmvNxj_JFVCJ3-Rw1iza7P58vN_Fk204icfGITfxtlYyWZ6zqNTNKiqFrLmkvFcwHYXxJAHGy0_O_Nhl9Ajyx2SXe7Xoc88D2huAfpqZwA2rLJ6Yt2RFnPhN5CBNF2j3tWVeByuimng-RHM5jHc-cme4LE9lwXTP8ri--rv_WvvryHzsvmjBMidJM27wSmn8R16RZLIvpMWWD9oTDyGr-CYxgWk-V93acsC_SqEMuzFToTP_07Mwhl8KjIz56YDAwkAcVlrVke4yZj_NUMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تفاوت آماری ابزار های تحقیق کلمات کلیدی
کیورد یا کلمه کلیدی  "محسن طاوسی"
(لطفا ننویسید کیبورد. ب نداره. و نگید keeeeey word):
تعداد جستجوی واقعی (ایمپرشن گرفته شده از سرچ کنسول) برابر است با 560 به صورت میانگین سه ماه اخیر.
تعداد جستجو در ابزار ایرانی سئوسیگنال: 550
تعداد جستجو در ابزار خارجی محبوب من، ابزاری که اختصاصی نسخه Premium رو تهیه می کنم و اولین ابزاری بود که MCP اورد برای هوش مصنوعی ها، ابزار Mangools معروف به KWFinder عدد 100.
واقعی سرچ کنسول: 560
سئو سیگنال: 550
منگولز: 100
ممکنه تو کلمات دیگه، کلا آمار ها غیر دقیق تر بشه. بخصص غیر فارسی ها.
ابزار ها میانگین ماهانه یک سال اخیر رو میدن. پس با چیزی که الان هست ممکنه خیلی فرق کنه مگر اینکه ببینید جزئیات ماه های قبل رو که منگولز و کیورد تول میدن.
کل سرچ والیوم مثال من کم هست. آمار ها در جستجوی های بیشتر متفاوت تر میشه.
اگر اواخر صفحه اول هستید، احتمالا گاهی برای بعضی ها میرید صفحه دوم. و باعث میشه کل ایمپرشنی که میفته کمتر بشه.
--------------------------------
🟢
دوره سئو بین المللی(+فارسی) با AI
🟢
پیام جهت خرید دوره
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/mohsentavoosiseo/1010" target="_blank">📅 12:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1009">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGJVaa3_6CjU7nucYfWFO6DNwaczVCPU-AtWTn-_EgmxjvH-XF2Cm1s0m8Is-9D30h0Ra5ldidf5ebkmcMQk1E6Mvb_IFhjSclH0BPFw2bhnKtP1kkXv6XrOC3ggd1OaGsX6SWiC3l7edLDS0mPQl6N6FFroB09qnIFQfift1hH8XeSRvMoUimDM_0RCuCnSD1WPFLUgCeCxrjjE-nVtPCjTHF9h95mdzOAKjs2NsnAa_-eiUCYzxEFzSlIHj7k-3uRX2EYRTtHeUK8JdtCja50SqTTbFh2a-AADc--h1PF1GZ4IOx7IaNKULq5MRozcgUTrXAVNQTnin6EVTdZHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اینکه برای خیلی از کارها نیازی به Opus نیست و همینطور کمتر نیاز به Fable هست، متاسفانه خبر بد اینه که Fable به قدری باهوش هست که آدم دلش نمیاد از Opus استفاده کنه. و Opus به قدری باهوش  هست که آدم دلش نمیاد از Sonnet استفاده کنه.
هایکو(Haiko) هم که خدا بیامرزه.
این یعنی مصرف توکن بیشتر و پول بیشتری که سرازیر به جیب آنتروپیک میشه.
امیدوارم فیچری بدن که بتونی انتخاب کنی خود هوش مصنوعی بر اساس مدل تسک و پرامپت در لحظه، مدل ها رو عوض کنه.
البته در پردازش داخلی خودش، داره چنین چیزی. من منظورم بخش کاربری هست که مثل اسب، Usage سشن ساعتی و هفتگی ما رو میبلعه.
توجه: اشتراک Pro کلاد دسترسی نداره به Fable. فقط Max ها دارند. ولی واقعا با همون Opus کار راه میفته. فقط بحث معتاد کننده بودنشون هست و معتاد کننده بودن خود Claude. اگر هنوز کلاد ندارید و با ChatGPT Codex کار رو پیش میبرید، خیلی متوجه اعتیادی که میگم نمیشید.
-------------------------------------------------------------
🟢
لینک صفحه خرید دوره سئو بین المللی(+فارسی) با AI
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/mohsentavoosiseo/1009" target="_blank">📅 20:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1008">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خیلی دارم اذیت میشم! خیلی! چون خیلی چیزها رو دوست دارم بگم و آموزش بدم ولی الان نمیتونم. حتی الان نمیتونم دلیل اینکه نمیتونم الان بگم هم بگم!  اما این پست رو اینجا میذارم. روزی رسید که میتونستم بگم، رو همین ریپلای میزنم و دلیلش رو میگم.   جذاب هست و بسیار…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/mohsentavoosiseo/1008" target="_blank">📅 00:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1007">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/554 https://t.me/mohsentavoosiseo/596 https://t.me/mohsentavoosiseo/992 https://t.me/mohsentavoosiseo/873 https://t.me/mohsentavoosiseo/506 https://t.me/mohsentavoosiseo/907 https://t.me/mohsentavoosiseo/908 https://t.me/mohs…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/mohsentavoosiseo/1007" target="_blank">📅 16:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1006">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/554 https://t.me/mohsentavoosiseo/596 https://t.me/mohsentavoosiseo/992 https://t.me/mohsentavoosiseo/873 https://t.me/mohsentavoosiseo/506 https://t.me/mohsentavoosiseo/907 https://t.me/mohsentavoosiseo/908 https://t.me/mohs…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/mohsentavoosiseo/1006" target="_blank">📅 15:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1005">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">و توانایی خروجی گرفتن از AI های پولی رو ندارید،</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/1005" target="_blank">📅 15:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مدل Sonnet در حالت High و Extra برای تولید گزارش، شکست خورد. گزارش من پیچیده نیست ولی انگار کلاد داره یه کاری میکنه شما مجبور شید برید رو مدل پر مصرف تر یعنی Opus.   واقعا پیچیدگی نداره گزارش. البته گزارش من فراتر از یه گزارش هست و دارم براش skill جدید میسازم…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/mohsentavoosiseo/1004" target="_blank">📅 15:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1003">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مدل Sonnet در حالت High و Extra برای تولید گزارش، شکست خورد. گزارش من پیچیده نیست ولی انگار کلاد داره یه کاری میکنه شما مجبور شید برید رو مدل پر مصرف تر یعنی Opus.
واقعا پیچیدگی نداره گزارش. البته گزارش من فراتر از یه گزارش هست و دارم براش skill جدید میسازم (همه رو آموزش میدم تو این اپدیت در حال ضبط).
این یعنی شما باید موقع ساخت skill بذارید رو Opus high یا extra. موقع اجرای کار بدون محاسبه(تولید گزارش از دیتای موجود بدون تحلیل) بذارید رو Sonnet. مدل ما برای پروژه ها Claude Max 5x هست که حوصله ندارم کلش رو میذارم رو Opus. معمولا سشن پنج ساعته ما پر نمیشه.
ولی اگر Pro دارید مهم میشه اینی که گفتم رو لحاظ کنید.
اگر اصلا نفهمیدید چی گفتم و چی به چیه، تو این اپدیت پیش رو همه رو یاد میگیرید. ساده تر از چیزی هست که فکر می کنید. من ساده یاد میدم. بر خلاف کسانی که موقع آموزش دادن، فکر میکنن پیچیده بگن بهتره شما تا ابد فکر کنید آموزش دهنده با سواده شما بی سواد. و اعتماد به نفستون هم میاد پایین.
پی نوشت:
من ادمی بودم که از گزارش فراری بودم! حالم بهم میخورد از این کارا! الان به لطف هوش مصنوعی، خوشم میاد. واقعا ساده شده. قبلا گفتم بازم میگم. هوش مصنوعی نمیومد من از سئو خروج میکردم. الان راحت شده. شما رو هم با خودم همراه میکنم. خداحافظ کارهای تکراری مسخره
😎
-------------------------------------------------------------
🟢
لینک صفحه خرید دوره سئو بین المللی(+فارسی) با AI
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/1003" target="_blank">📅 14:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1002">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سوال:
یک وب‌سایت فروشگاهی داریم که مربوط به یک تولیدی دستگاه‌های صنایع غذایی است. قبلا، به‌اشتباه حجم زیادی از مطالب آشپزی در سایت منتشر کردند و همین موضوع باعث شده ساختار و موضوع اصلی سایت تا حدی به‌هم بریزد و صفحات محصولات و دسته‌بندی‌ها رتبه خوبی در گوگل نداشته باشند.
مطالب آشپزی به‌طور کامل حذف شده و برای حذف URLهای مربوط به آن‌ها هم در گوگل درخواست ثبت کرده‌ایم. تعداد زیادی از URLهای قدیمی نیز به صفحات مرتبط ریدایرکت شده‌اند.
با این حال، هنوز وضعیت صفحات محصولات و دسته‌بندی‌ها بهبود محسوسی پیدا نکرده و رتبه‌ها همچنان ضعیف هستند.
کسی تجربه مشابهی داشته؟ بعد از حذف حجم زیادی از محتوای نامرتبط و اصلاح ریدایرکت‌ها، برای اینکه صفحات اصلی سایت دوباره رتبه بگیرند چه اقداماتی باید انجام داد؟ آیا باید منتظر ماند تا گوگل دوباره سایت را ارزیابی کند یا مشکل می‌تواند از جای دیگری باشد؟
پاسخ:
همین موضوع باعث شده ساختار و موضوع اصلی سایت تا حدی به‌هم بریزد و صفحات محصولات و دسته‌بندی‌ها رتبه خوبی در گوگل نداشته باشند.
چجوری فهمیدید همین موضع باعث این شده؟من بعد از 15 سال نمیتونم اینجوری دلیل یه رتبه نگرفتن یا افت رو به این راحتی تشخیص بدم. اما میتونید بگید این یکی از احتمالات هست و بهتره هرس بشه. بله درسته.
برای حذف URLهای مربوط به آن‌ها هم در گوگل درخواست ثبت کرده‌ایم.
درخواست منظورتون بخش removals سرچ کنسوله؟ اون حذف موقت هست. دائم نیست. فقط زودتر حذف میشه و در صورتی برنمیگرده که کلا یا صفحه دیگه وجود نداشته باشه یا نوایندکس باشه. این کارتون هیچ تاثیری نداره.
تعداد زیادی از URLهای قدیمی نیز به صفحات مرتبط ریدایرکت شده‌اند.
این هم یه کار خیلی معمولی هست. یه بهینه سازی و هرس رایج هست که همه سایت ها باید انجام بدن در صورت از رده خارج شدن صفحات قدیمیشون. معجزه نمیکنه.
با این حال، هنوز وضعیت صفحات محصولات و دسته‌بندی‌ها بهبود محسوسی پیدا نکرده و رتبه‌ها همچنان ضعیف هستند.
با این حال؟ اتفاقی نیفتاده که. کاری نکردید. چرا باید رتبه ها بهتر شن؟ در اکثر موارد، سئو به این سادگی ها نیست!
اصلا از کجا میدونید دلیل رتبه نگرفتن سایت، اون صفحات بی ربط بودن؟ نهایتا اون ها کراول باجت رو مصرف کردند. حالا شما کراول باجت رو بهینه کردید. خیلی هم عالی. چرا باید رتبه بهتر بشه حتما؟ مگه مشکل کراول باجت بوده؟ از کجا میدونید؟ اصلا صفحات قدیمی مگه اعتبار داشتند که با ریدایرکتشون اتفاقی بیفته؟ اگر داشتند، آیا لایق رتبه بودند اصلا؟ آیا نسبت به رقبا قوی تر بودید و هستید؟ نتایج نشون میده نیستید. حساب کتاب شما نه. نتایج گوگل.
برای اینکه صفحات اصلی سایت دوباره رتبه بگیرند چه اقداماتی باید انجام داد؟
دوباره رتبه بگیرند؟ تو متن اشاره نشده بود که قبلا رتبه داشتند. فقط گفتید رتبه نگرفته کلا. خیلی فرق داره ها!
چه اقداماتی باید انجام داد تازه بخش درست این متن هست. باید از اول شروع به تولید محتوای مفید و موثر، اف پیج هم برید علاوه بر هرس. باید در رقابت پیروز بشید. باید صفحاتی بسازید که نداشتید و نیاز هست برای رتبه گرفتن (دو فصل در دوره درباره صفحه بندی و تارگتینگ هست). باید روی کلماتی در صفحه مخصوص خودشون رتبه بگیرید که رقابت کمتری دارند و ازشون لینک داخلی بدید به پر رقابت تر ها. باید تبلیغ کنید و ترافیک جذب کنید. باید اف پیج برید.
به عبارتی، کاری نیست بکنید همه چیز برگرده به حالت خوب. برگشتی وجود نداره. باید رشد کنه سایت. چیزی که الان هست، همون چیزی هست که باید باشه. فقط یک سری پایه ها اصلاح و ترمیم شده.
این است دنیای ارگانیک سرچ‌. تازه شدید مثل همه ما. Welcome to the club!
یا باید منتظر ماند تا گوگل دوباره سایت را ارزیابی کند؟
گوگل 24 ساعته در حالت ارزیابی سایت شما هست already. فکر نکنید گوگل دوره ای میاد سر میزنه میگه ااااا این همون سایته است که صفحه بی ربط زیاد داشت؟ حالا نداره! پس بیارمش بالاتر خوشم اومد افرین
😎
.....نه! اینجوری نیست داستان. فقط دیگه ارزون تر و سریع تر میتونه برسه به صفحات مهمتر شما. همین. هیچ امتیاز دهی مجددی با حساب کتاب شما و ذهن شما و انتظار مورد نظر مثبت قرار گرفتنی به عنوان پسر خوب...ببخشید سایت خوب در کار نیست.
یا مشکل می‌تواند از جای دیگری باشد؟
احتمالا تا الان متوجه شدید که کلا مشکلی وجود نداره که بخواد از جای دیگه باشه. همه چیز عادی هست. مشکل اینه که نباید دنبال مشکل بگردید.
اگر ناراضی هستید و همچنان دنبال یه چک و تیک و کار خاصی هستید که رتبه ها عالی بشه، سئو زمین مناسبی برای ذهنیت شما نیست. برید سراغ گوگل ادز.
-------------------------------------------------------------
🟢
لینک صفحه خرید دوره سئو بین المللی(+فارسی) با AI
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/1002" target="_blank">📅 01:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1001">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfEv2w9Fem5I7r1Umaaro1bhway6hLbrDyi1mmas2v7uaOPcniN529lE4CDt6Rj6_2qW0m-GUE2L5ht4UNd9Axy4KygKLooswlGEJapmNxnVO47O-8GCzDWubj-Ikm3KDqNq3xweIeQ8ZIfPIv-uU59LxylyasrvPpIsnEwoZr-I3xXMjivquA3uhRMIgorkh6CDxeodHJksKEAacfEKFj4GVQ6qMdJbg5RIddIKNaakr6xqGG6_q_vTXokc4N4XYs5Aph8bfoJCx6h4lgSKqi9bKBl9cM159WRGim5C3lT2mI2J4lyJ4PiweUE-YOWgHDQHPlk4aeAYOV7dBFy1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره یه سفر بریم بانکوک شهر توریستی بین المللی در قلب سرزمین شبیه فارکرای ۳ و ۴، سرزمین تایلند. ازونجا بریم جنوب اسپانیا. سوبرمسا کنیم و بعد بریم قلب نروژ.
بعد یه سری به کشور هاب گردشگری، ترکیه میزنیم و سری به استانبول و گربه هاش می زنیم.
بعد میریم آلمان و درباره اشنپس ای دی هامون حرف میزنیم و میخندیم و سپس سری به تفریحات کره جنوبی و خونه های کوچیک ژاپنی میزنیم و بعد یه قدمی تو مسکو پایتخت روسیه میزنیم.
بعد برمیگردیم فرانسه و باهم alors on danse رو میخونیم.
این وسط قطعا GCC، شش کشور عربی شورای همکاری خلیج فارس، سر راه ما هستند.
فکر کن این همه آسیایی بریم ولی هند نریم! قراره از بوق هندی ها سردرد بگیریم و توک توک سوار شیم.
یه درصد فکر کن آمریکا و برزیل نریم! حتی شمال برزیل یعنی آمازون هم میریم. آب نارگیل طبیعی هم کنار خط ساحلی ریو میزنیم. سری هم به محله های خطرناکش میزنیم که پلیس هم نمیره. هم فاولای برزیل میریم هم فیلادلفیای آمریکا.
سر راهمون تو آسیا هم دونوع املت گوجه میزنیم.
الان متوجه نمیشید چی گفتم. تا سه ماه آینده متوجه میشید.
ありがとうございます
Arigatō gozaimasu
Muchas gracias
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/mohsentavoosiseo/1001" target="_blank">📅 15:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1000">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پاسخ کوتاه تر بعد از سه ویس بالا درباره ایندکس نشدن ها:
Welcome to the club!
تازه شُدید شبیه همه ما. ولی پاسخ فنیش همون سه ویسه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/mohsentavoosiseo/1000" target="_blank">📅 15:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-999">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ویس بسیار مهم درباره این جملات:
با دیتا حرف بزن!
این دیتا معتبر نیست!
این دیتا معتبر هست!
تجربه مهم نیست!
تجربه مهم هست!
مستندات بده!
هیچ مستندی نداده گوگل!
اصلا این آموزش ها و مستندات به درد من و هدف من میخوره؟
مرز تشخیص محتوای درست وغلط و نحوه استفاده از منابع و تجربیات و مستندات.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/mohsentavoosiseo/999" target="_blank">📅 15:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEHf-ngQ0V43ctC75QYuA5YZhMTkcWMQWudofiO4MSI9ue23x1z-r1osU82RJH1On5ms-Kk0fO6uA03qlY2uKpMXek9DdEo3bI-oY8zSh05ybj9MxMMgpGvj9a4u5HRlPeL9q0CV819Hy8x6SjRBLtv6gBHNiWW7vKvLBgVs3d28jM02MOocN0kTIT306WBRgwaZZKbhsHG94cGI7Sq2FhAOR7ZBTFTuib364wbe8gA_BjU-lvQWneRi1CnAGTfjjF8wRCfDDQjgEekEovorAM-MlMHjuWGb1IiQbBM3mtoyuTSO8Eh4feHiMzl8kFq5nTzErmyArNixkOz2pavyeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9w_nvEbwOKbsYQrRrhKKsnzFgG4CFSuWf951TOZmx2XlrTHoQjafSUt7O2k0utH9TT74v1HuFGy5TdQCVRZjJzHcKztuBtrpnWf18HnPLihp9MlCwlsC0otAqN_iCIL1ggkOjdU4YOMmajpDPwzdq-3ClsdcKZ-t-VgBFf6NCyvcoLTgPyuMM-Yxj8I6EpeHDoj6k9fIQbdvxKJpdJc9bNMmeBddoge9elKP0l4dKn-49qxhmyXEk9QTrLC_bbkYLkQdzrmu5p2RFiz9lqLneNLpJM4KsSp1FvKqJH7-miH-o7JzAJXpM5dyHHBpEk_gBlHZr53Lekv4UKr7drdAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درباره بحث ایندکسینگ و ایندکس نشدن صفحات و وضعیت های Crawlded, not Indexed یا Discovered, not Indexed.
تصویر بالا، تصاویر نمونه هاست دارای مشکل در 90 روز گذشته و هاست بدون مشکل در 90 روز اخیر در بخش Crawl Stat سرچ کنسول (بخش Setting). همه این ها در دوره هست در فصل های تکنیکال.
تمام پاسخ های مرتبط با بحث ایندکس نشدن در 19 دقیقه ویس (در سه Voice) زیر:
7 چیزی که باید چک کنید:
https://t.me/mohsentavoosiseo/868
نکته 8 که دست شما نیست و بهش بی توجید و مرتبط هست به قدرت سایت و پتانسیل رتبه(نه رتبه نقد فعلی) و پاک کردن آشغال ها:
https://t.me/mohsentavoosiseo/869
قبل جنگ خوب بود بعد جنگ این بلا سرم اومد:
https://t.me/mohsentavoosiseo/996
نکته پایانی:
بعضی مواقع تسلیم شید. پذیرش یه حقیقتی که بهش اعتقاد نداشتید، بهتر از دست و پا زدن های بیهوده است.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/mohsentavoosiseo/997" target="_blank">📅 14:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/mohsentavoosiseo/996" target="_blank">📅 14:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">من داخل دوره، فصل سئو فنی 1(چهار فصل فقط سئو تکنیکال داره دوره) ویدیوی Response Status Code کامل درباره استتوس کد ها گفتم و 304 هم در دقیقه 03:15 هست.
قدیما فکر میکردم همه باید دوره رو کامل ببینن. حداقل کسانی که پیگیرن و فعال هستند دیگه باید ببینن. بعدا فهمیدم درصد کمی از همون ها میبینن دوره رو و این روتین و روال جهانی هست در این عصر پر زرق و برق و پر از حواس پرتی.
ولی یک بار اگر دوره رو ببینید به جای یادگیری های پراکنده و اسکرول ها و کانال های مختلف، بخش زیادی از عمرتون و ذهنتون صرفه جویی شده و بهره وری به شدت بالا میره.
اینجا هم میگم 304 اکیه و مثل 200 هست و هیچ مشکلی نداره. مرتبط با بحث Cache هست و این پیام به بات گوگل، که بات جان، این از آخرین باری که دیدی عوض نشده. نمیخواد دوباره بیای کراول کنی. پولتو هدر نره من (صفحه) همونم که سری آخر دیدی.  همین.
من تو همین ویدیو 307 هم گفتم. تو همین ویدیو اینکه نباید بگید ریدایرکت 410 هم گفتم. وردپرسی یاد گرفته ها به 410 میگن ریدایرکت چون تو تنظییمات ریدایرکت افزونه ها چیزی شبیه این دیدند.
ریسپانس هدر و ریکوئست هدر هم گفتم تو همون فصل. User Agent هم گفتم. Partial Postback و Json Request ها هم گفتم.
فکر نمیکنم جایی بتونید از پایه با زیرساخت ذهنی درست، همه چیز رو اینطور اصولی و شسته رفته و بدون مقدمه الکی و کش دادن الکی، آموزش ببینید.
نمیتونم کسانی که دوره رو دارند وادار کنم دوره رو ببینند. ولی میتونم بگم دارید ضرر می کنید حالا که خریدید و یک بار نمیبینید دونه دونه. بدون حدس زدن و این تفکر که "من که بلدم". میدونم بلدید.
ولی همین 304 رو همون کسی که میگه بلدم بلد نیست. دیگه ویدیو جدا نذاشتم چون 3 جملست کلا! ویدیو جدا بود هم دانشجو از حجم زیاد محتوا میترسه و مغزش میگه ولشکن بعدا میبینم.
——————————————————--
🟢
لینک صفحه خرید دوره سئو بین المللی(+فارسی) با AI
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/mohsentavoosiseo/995" target="_blank">📅 12:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اسم های مختلف میشونید:
سئو ایجنتیک Agentic SEO، اتومیشن سئو SEO Automation, سئو با هوش مصنوعی، بهینه سازی برای موتور های مولد، بهینه سازی برای LLM ها. Answer Engine Optimization بهینه سازی سایت، پیج و... برای موتور های پاسخ دهی چت بات، GEO بهینه سازی برای کلا موتور های مولد Generative Engine، و کلی اسم دیگه.
البته که ایجنتیک سئو با GEO/AEO فرق داره. عملا این AEO میشه زیرمجموعه بهینه سازی سایت توسط هوش مصنوعی و اتوماتیک.
درسته نسیه است حرفم.
اما اینو گفتم که بگم همه اینا رو تو آپدیت دوره دارم میگم(دارم ضبط میکنم). و کلا موضوع جدیدی هست و حتی ویدیوهای یوتیوب مرتبط در سطحی که من میگم، ندیدم اصلا در سطح بین المللی هم ندیدم. چند تا هست مثلا برای سه ماه پیش! یعنی کلا بحث جدید هست.
اونایی که هست هم به درد برنامه نویس ها میخوره فقط  و برای عموم مناسب نیست.
ارزشی که من خلق میکنم اینه که چیز سخت و پیچیده رو ساده بیان کنم.
من میخوام پیر نشید برای یادگیری! ساده اش میکنم و تو محیط راحت میگم. هلو بپر تو گلو بدون سردرد و وحشت. بدون ترمینال. بدون کد. بدون پایتون. بدون محیط های سخت برای عموم.
راستش سه بار ضبط کردم و از اول شروع کردم. هربار ساده ترش کردم. وگرنه ماه پیش آپدیت رو داده بودم بیرون.
خوبیش هم اینه که قشنگ من خاکی شدم وسط کار. هرچی یاد میگیرید اجرا کردم بارها. میشناسید منو. من آدمی نیستم چیزی یاد بدم که قورتش نداده باشم.
ضبط بخشی از ویدیو ها تموم شده ولی بعد از ادیت و اینکه بخشیشون کامل شد قرار میدم تو دوره. خرد خرد قرار نمیدم.
شما تا اخر 2026 روش حساب کنید و نگید کی میاد ولی از الان میتونید تهیه کنید که قیمت بالا رفت، داشته باشیدش با قیمت قبلی
. کل موضوع جدید هست اصلا و منبع جهانی هم نداره با بیان ساده و سئویی به اون شدت.
منتظر یه نشاط دراگ گونه باشه بعد از دیدن اپدیت با حالت "آخیش! چقدر خوبه!".
یجوری میگه دراگ انگار نه انگار خودش سوبره
😏
.من سیگارم نمیکشم شراب قرمزم نمیخورم حتی.
——————————————————--
🟢
لینک صفحه خرید دوره سئو بین المللی(+فارسی) با AI
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/mohsentavoosiseo/994" target="_blank">📅 14:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این پست بسیار کاربردی رو ذخیرش کن تو saved هات. هم معرفی ابزار هم آموزش. بفرست برای کسانی که دنبال ابزار هستند: و اینکه ما کیوورد توول رو از کجا تهیه کنیم میشه.هم لیمیت پس هم نوین ترند  خیلی بده سرویس دهیشون و لیمیت میخوره اصن نمیتونیم کار کنیم https://t.…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/993" target="_blank">📅 13:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چرا رایگان درست حسابی و بی دردسر نداریم یک ویس میذارم که خیلی مهم هست در ادامه(اگه نگاه تجاری درستی داشته باشید به این پایین نیاز ندارید).</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/mohsentavoosiseo/992" target="_blank">📅 12:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-991">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">درباره دلیل اینکه چرا اشتراکی ها انقدر اذیت کنندست و چرا رایگان درست حسابی و بی دردسر نداریم یک ویس میذارم که خیلی مهم هست در ادامه(اگه نگاه تجاری درستی داشته باشید به این پایین نیاز ندارید).</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/mohsentavoosiseo/991" target="_blank">📅 12:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-990">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تو ابزارهای اشتراکی، قطعی ها و ایراد ها و اینکه یهو میگه تو حداکثر ظرفیتو استفاده کردی(با اینکه نکردی)؛ رو بپذیرید!  طبیعیه. همون لحظه رسیدن به محدودیت اکانت، نمییتونن درجا شارژ کنن. دستی انجام میشه.   پول کم میدیم که استفاده کنیم فرقش همین چیزاست. قطعی، یه…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/mohsentavoosiseo/990" target="_blank">📅 12:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-989">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آموزش اتصال کلاد به وردپرس و هرچیز دیگه ای فقط تو یک دقیقه!   و این برای وردپرس نیست فقط. برای همه چیزه. کلا این قابلیت کلاد کروم خودش یه فصل جدید زندگیه
😎
این یک دقیقه انقدر کوچیکه که معنی نداره بگم تو اپدیت دوره هست. خیلی بیشتر و تمیز تر میشه از هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/mohsentavoosiseo/989" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-988">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خیلی دارم اذیت میشم! خیلی! چون خیلی چیزها رو دوست دارم بگم و آموزش بدم ولی الان نمیتونم. حتی الان نمیتونم دلیل اینکه نمیتونم الان بگم هم بگم!
اما این پست رو اینجا میذارم. روزی رسید که میتونستم بگم، رو همین ریپلای میزنم و دلیلش رو میگم.
جذاب هست و بسیار کاربردی دلیلش و بسیار در راستای نگاه تجاری هست. و مثل نقد فیلم ماتریکس یهو رمزگشایی میشه و براتون جالب خواهد بود و البته دارای بار آموزشی + چند تا چیز دیگه.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/mohsentavoosiseo/988" target="_blank">📅 21:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-987">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPVwsLn1q4JUbGpev-JGcJOyHORknrWBSsRjx-3g1DeFe7DbbCrGi0BgsTHog_9kOMyJE7j1a4EFZSUKLBR9itycEd1NjHG0aJqew6MXvHlrVPm5BczkbAPhp9et-GrBGprd4c0ot1aC5fr9z2qofi9xwshygulGEJXSY_mGX5bLxY92OmTKJhjvJe7gQuyUaWMAoGjxksP7fIyRpoYYNi32fgxSjA4se8qTMbfD5sA9zTwrUfimhE0hsRjerJxR_5NKuAZJzs9JPT6ykZk2JCc5d6uxu2v6bc6yjgMyDOBcxQS5H6KrD50wNZ2Y3xhvstFZCMZRgPMscGvHbH5RSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی معتبر تر از خود سازندگان هوش مصنوعی هست به نظرتون که تایید کنه در موارد خیلی به روز، هوش مصنوعی عقبه؟
من قبلا مثال اخبار رو زده بودم که هوش مصنوعی بعد از 6 ماه از سقوط بشار اسد میگفت هنوز هست و سقوط نکرده و منبع هم میداد حتی. منابعی که توشون نوشته شده بود سقوط کرده!
بعدا مدل ها بهتر شدند و این ضعف رو پوشش دادند.
ولی همین الان هم هوش مصنوعی در پزشکی پرکتیکال، ضعیفه. ولی تو داده های پزشکی کلاسیک، خوبه. همون پزشکی ای که اکثر دکتر ها درسش رو میخونن به شکل سنتی.
تو نمیتونی از هوش مصنوعی متد های درمانی افسردگی رو توسط گوارش پیش ببری. چون گوارش و ذهن و سروتونین شدیدا به هم گره خورده هستند. اما تو پزشکی کلاسیک، تخصص گوارش، هیچ ربطی به اعصاب و روان یا مغز و اعصاب نداره.
هوش مصنوعی هم همون طب کلاسیک رو بلده.
حالا چه ربطی به سئو داشت؟ به فاین تونینگ ربط داره. به اینکه شما چطور باید هوش مصنوعی رو برای پروژه خودتون آماده کنید. برای افکار و روش های خودتون. برای روشی که شما قبول دارید ولی بقیه قبول ندارند.
تو اپدیت دوره، این ها رو پوشش میدم. سطح کار بالاست مثل همیشه
😎
🟢
صفحه خرید دوره سئو با AI
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/mohsentavoosiseo/987" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-986">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhaZaUadK8wyfCnIQRi8yXuWjBcBD624FanXKZNPSQoCC9UCPCoeeC_rD9n89X-jChfiKTOtGozFLs7MUGQSUnfi5lWTR-qsOeBKN-_q3A5Ld0y_F7peBU5Y5F9L_EP8Tzn_IQN0EUr9C0afXgBuZkrh05Iqwbn53mh7KbnN9KHi1lUV8DTMWIkozIhJaGpkltHjdrCZLOMW0HLAjN3M3p3_fJf6CPFIEJvyI1PeImEdmB4QZI5Vj15R55KIW0_Uu2grZGcwz-9JGW_wFHYCupLvb0jMsJ2dhcyMPTvy7b4IABDfsXsJ0iGQ3SG--xX5qEj46y4iYkF-V2HqhyykLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تدوینگر، من رو دعوا کرده میگه چرا حواست نبود این رفته گوشه؟
من کلی معذرت خواهی کردم. گفتم ببخشید. ولی خداروشکر زمان کوتاهی اینجوری بود تصویر.
ولی آیا میتونم بهش بگم تولید کن منو؟ یه میرور بگیر یجوری lip sync (تقلید حرکت لب از صدا) بساز با صدام بیارش اینور تر بخاطر 30 ثانیه؟
واقعیتش اینه که بله، فناوری اونقدر پیشرفت کرده که بشه. ولی سوال اینجاست که آیا مصرفه؟
برمیگردم به نگاه تجاری همیشگی که میگم. مساله این دوره زمونه، امکان پذیر بودن نیست. به صرفه بودن و توجیه هزینه است(ننویسید توجیح خواهشا!).
❗️
وگرنه همه داروهای بدرد نخور صنعت بیگ فارما مثل اس امپرازول و کلا PPI ها
(برای مصرف طولانی مدت و یک عمر)،
جمع شده بود.
❗️
وگرنه همه ماشین ها هیبریدی و برقی شده بودند.
❗️
وگرنه الان همه خونشون خدمتکار ربات داشتند.
❗️
وگرنه همه الان بدون پول، به صورت رایگان، به همه امکانات هوش مصنوعی های غیر رایگان دسترسی داشتند.
❗️
وگرنه گوگل جاوااسکریپت رو مثل  هلو کراول میکرد و نمیگفت لینک هات و لود صفحات SSR باشه.
همیشه بحث صرفیدن هست. نه امکان پذیر بودن. و این صرفیدن شامل هزینه ذهن، زمان و پول هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/986" target="_blank">📅 18:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-985">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/985" target="_blank">📅 17:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-984">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تب و تاب وایب کدینگ و ابزار نویسی در عصر هوش مصنوعی بدون برنامه تجاری
دون پاشی چند ساله تلگرام بدون کوچکترین بی تعهدی و خلف وعده ای درباره بخش های رایگان(شعار رایگان و تا ابد رایگان).
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/mohsentavoosiseo/984" target="_blank">📅 17:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-983">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">1:06 "کانال های یوتیوب"</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/mohsentavoosiseo/983" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-982">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c43234ee.mp4?token=n-Zp72JwcgSeALPekPSUTu3HJWqmeNNZslyXeykpg7C18_rz0e9Sbu2nxrrPctpvdXq9b3RB2_EWVT2VOuJsWEP-cykPfLYpp8qfGPyB1ezOBTvj-KFsDQu7H0DdC7_gmBz9mJ0sCdu_8GeOp1KKSE2rgk-LhwwiEQuZe73ePXFws1DIWu9T9kKv4cosxsC9XGHO8XlEzfvUch2YyEXs1IdIttE8FcZ7D3kWkmSSecWsiWX8dONxHDGvp1CikooxmkPJRY85fmU3HBTUb6eqmVHhk_GmAIaoZGQidCaEDju6kYqSdX9otk0rsVneCGx4epUnOX5-xaiQv7PLmQX8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c43234ee.mp4?token=n-Zp72JwcgSeALPekPSUTu3HJWqmeNNZslyXeykpg7C18_rz0e9Sbu2nxrrPctpvdXq9b3RB2_EWVT2VOuJsWEP-cykPfLYpp8qfGPyB1ezOBTvj-KFsDQu7H0DdC7_gmBz9mJ0sCdu_8GeOp1KKSE2rgk-LhwwiEQuZe73ePXFws1DIWu9T9kKv4cosxsC9XGHO8XlEzfvUch2YyEXs1IdIttE8FcZ7D3kWkmSSecWsiWX8dONxHDGvp1CikooxmkPJRY85fmU3HBTUb6eqmVHhk_GmAIaoZGQidCaEDju6kYqSdX9otk0rsVneCGx4epUnOX5-xaiQv7PLmQX8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/mohsentavoosiseo/982" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">من فکر میکردم بحث "هدف" خیلی بدیهی هست. ولی نبود!
و همچنین فعالیت هایی که در راستای هدف نیست.
یا هدف، خودش پوچ هست و باعث سرخوردگی میشه.
پول، تایید اجتماعی، تمسخر، بی کلاسی، نجات دیگران، خیریه، خدمت، رضای خدا.
شاید مسیر باید کلا برعکس بشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/mohsentavoosiseo/980" target="_blank">📅 15:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چت جی پی تی رسما یه چپ دموکرات معتدل شدست که فاز شدید راضی نگه داشتن داره. گراک یه راستی جمهوری خواه ساختار شکن بی مرز. جمینای یه میانه ی رو به راست و پایه و خوش فکر و بی تعصب. کلاد هم یه ترکیب سمی ترکیبی با رویکرد "من همینم که هستم" با تعصب و موضع گیری های بیش از حد زیاد تو بعضی موارد هست.</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/mohsentavoosiseo/979" target="_blank">📅 13:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-975">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYSTvTOQ5mEaClVccsxrIuYexPIYcj6izjZgP6WsVrimTA2-ggKgrQYGCilkEOAzTZL6p9YbuGdzC4C3B_pimzpDUPBx_rVBT3iH1kEfnRcxqr8cgeDd_8sOTTZzA1MmsA6fZsl_mI4HmNbnElQXlGnvHSIzWiUfxdAyGSxig8P1a7JordB9JHQHakIa4s85V339FuWs250QRfzF-zZyETi1z4axQVUesnZMq4R7M5y0TFDRHz5qUKQNq4ymA1M5Vmhd7qBBoGo7JPbXG-ss6Po-95fLuKoS6HdKz-V5HMMXCdV_5oy7Hqhb-PL6aPEEHZp_S6PcAmT7NfbvaDTr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4BpVOMR0ywGLVWEhs2wTWY1PgySdGBZbZL3PGkbldcs1Kr8ifWbqS8RYk-Jpt49sfWCutVB-DzcrPSycBjAhFspSh6UIZmhAqIyvsh-nobuO09lJ4e59oBIyF68kByAm1AtJliqqWOPEZjeK1MhXPXjyX1EE0LaOY85KiiqKMXjL10IdAzhT7GtXjT8OUcz1PiIM4nQrZ-e6MfXyRo_3WF58WJWnyTgBslPckZTJsxYih11NSDI3OX5b7hzkavXPnwcXYEGG6aocChJt4Gpsllny2_WKDChGAbo1CDChNQtHpmrVeFllwPnYfrABjwlg8nXW7X1x21zX00ENia41Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هیچ وقت فکر نمیکردم با هوش مصنوعی(Claude) باید سر و کله بزنم که مسیری که من میخوام رو بره! کلاد از حد گذرونده دیگه و زیادی مخالفت میکنه. و حتی میگه ناراحتی گزارش بده آنتروپیک میبینه.
و خودشونم میدونن که زیادی مقاومت داره کلاد تو پذیرش درخواست که گزینه Overactive refusal و Did  not fully follow my request رو گذاشته همون اوایل بازخورد!
یعنی مخالفت و رد شدن بیش از حد و دنبال نکردن کامل درخواست من!
چت جی پی تی رسما یه چپ دموکرات معتدل شدست که فاز شدید راضی نگه داشتن داره. گراک یه راستی جمهوری خواه ساختار شکن بی مرز. جمینای یه میانه ی رو به راست و پایه و خوش فکر و بی تعصب. کلاد هم یه ترکیب سمی ترکیبی با رویکرد "من همینم که هستم" با تعصب و موضع گیری های بیش از حد زیاد تو بعضی موارد هست.
هرچند باز انتخابش میکنم ولی تو اون موضوع که زیادی کل کل میکنه حواسم هست به موضع و دیدگاه مسخره و متعصبانه اش! جمینای و گراک بهترن تو بی تعصبی.
شت! پارسال همین موقع فکر نمیکردم یک سال آینده دغدغم نحوه استفاده و برخورد با یه هوش مصنوعی متعصب و یک دنده باشه! شت!
سال دیگه خدا رحم کنه...
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/mohsentavoosiseo/975" target="_blank">📅 13:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-974">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آموزش اتصال کلاد به وردپرس و هرچیز دیگه ای فقط تو یک دقیقه!   و این برای وردپرس نیست فقط. برای همه چیزه. کلا این قابلیت کلاد کروم خودش یه فصل جدید زندگیه
😎
این یک دقیقه انقدر کوچیکه که معنی نداره بگم تو اپدیت دوره هست. خیلی بیشتر و تمیز تر میشه از هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/mohsentavoosiseo/974" target="_blank">📅 23:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-973">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آموزش اتصال کلاد به وردپرس و هرچیز دیگه ای فقط تو یک دقیقه!
و این برای وردپرس نیست فقط. برای همه چیزه. کلا این قابلیت کلاد کروم خودش یه فصل جدید زندگیه
😎
این یک دقیقه انقدر کوچیکه که معنی نداره بگم تو اپدیت دوره هست. خیلی بیشتر و تمیز تر میشه از هوش مصنوعی استفاده کرد که تو اپدیت دادم قرار میدم خیلی شسته رفته و کوتاه و کاربردی بدون اینکه مغز بیننده از جا دربیاد برای یادگیری.
توجه: این بسیار سادست. کار اصلی ما با MCP هاست.
——-————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/mohsentavoosiseo/973" target="_blank">📅 21:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-970">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چرا نباید از اول برای کسب و کار، با کدنویسی و CMS اختصاصی پیش بریم؟
چرا اول کار فقط وردپرس؟
البته استثناهایی هم وجود داره. اگر تصمیم گیرنده از هیجان زدگی تصمیم بر غیر وردپرس نگرفته و از محتوای این ویس هم آگاه هست و پذیرفته و حاضره هزینه نقدی و زمانی و ریسک با اختلاف بیشتری کنه، ممکنه اختصاصی هم مناسب باشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/mohsentavoosiseo/970" target="_blank">📅 19:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-968">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
این پست حاوی ایده درامد دلاری و افشاگری پشت پرده هست. دست به دست پخش کنید که در جریان قرار بگیرید پشت پرده چه خبره یا خودتون ازش استفاده کنید:  این نظر سنجی که روش ریپلای زدم رو یادتونه؟  نتیجش این شد که من ورود نمیکنم بهش. ولی شما ورود کنید! در ادامه میگم…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/mohsentavoosiseo/968" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-967">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چطوری ایده مناسب کسب و کار خودمون رو پیدا کنیم؟ اصلا خط اصلی پیدا کردن ایده کسب و کار مناسب ما چیه؟ چه مسیری رو باید بگردیم؟
ریسک های کسب و کار چیه در طول مسیر؟ آماده چه چیزهایی باشیم؟
این ویدیو یکی از مهمترین مواردی هست که تفکر کل زندگی و کسب و کار من هست.
https://youtu.be/2cW1RJKfOao?si=_YEhZViKApY3Nygm
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/mohsentavoosiseo/967" target="_blank">📅 14:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-966">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تو ویس پایین توضیح میدم این اشتباه فاحش هوش مصنوعی رو!  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/966" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-965">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvc4Wx-nCYSh3kLM_g_KJ18-rJsTcZRfqAqB69AGuhwSpE1B__KN1dy0jUfxSHsT6RYtTG6rgHp0SVV8UIEChVc-UueKWPf6HlccbzGGi1NGSZJ0QtlZbQ4L4Wt0fYvbQJIqubGDeq8omNEZ9NalJ_6qcSpdxV6dFVfTII8vQUfLCeqskgkogILwYBc2tMWaL8RLM6uTGh3F7RS9MEKEYnmJRWv1Jy8YbaX_v6AdCxYcYmo57C6_LKMRi4lcZYuVWGENuwxiGwaLeN8S7nrywabypSvxfOwHRqSOjWTniCXm62ehayFd0N4gUX78HpBchx0ReeVitwvZO2Dgd3xaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ویس پایین توضیح میدم این اشتباه فاحش هوش مصنوعی رو!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/mohsentavoosiseo/965" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-964">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⛔️
این خوب نیست!
تو این دو تا پست خیلی ها اومدن گفتن چرا به هوش مصنوعی توهین می کنی و اصلا اینکه هوش مصنوعی برات خط و نشون بکشه و چتت رو ببنده براشون مهم نبود! و فاز اخلاقی برداشتند!
سریال جاناتان نولان داره به واقعیت میپیونده. این خطرناکه‌. یکی حتی نوشته بود با کارگرت نباید بد حرف بزنی خب و همزادپنداری انسانی کرده بود!
خطرناکه عزیزم. لحن ما در چت خصوصی با هوش مصنوعی خطرناک نیست. سلطه ماشین بر انسان خطرناکه که از همین حالا عاشقان سینه چاک امام دیجیتالی(هوش مصنوعی) صف کشیدند برای بردگی و تعظیم برای یک چیز بی جان صفر و یکی(دیجیتالی) ساخته دست بشر.
خداروشکر از قشر آگاه تر و تکنیکال(دولوپرها) چنین چیزی ندیدم‌. دولوپر ها میدونن کت باید تن انسان باشه.
https://www.linkedin.com/posts/mohsentavoosi_%DA%A9%D9%84%D8%A7%D8%AFopus-5-high-effort-%D8%AA%D8%B0%DA%A9%D8%B1-%D8%AF%D8%A7%D8%AF-%D8%AA%D9%87%D8%AF%DB%8C%D8%AF-activity-7499816238756421632-mHI7
https://www.instagram.com/reel/DcqV0WHMZia/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/mohsentavoosiseo/964" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چالش تیم پشتیبانی رفع اشکال گاهی اوقات اینه که سوال کننده یه مدیری داره که مدیرش تو اینستاگرام یه پست دیده که یه چیزی نصب میکنی روزانه کلی بازدید روانه سایتت میشه دیگه هم به گوگل نیاز نداری.
از تمام دست اندرکاران و فعالان حوزه جدی تقاضا دارم، ابزاری که صرفا با نصبش، بدون کار محتوا، بدون کار آف پیج، بدون اینکه درگیر بهینه سازی بشی، اگر راهی میشناسید که با نصب یک افزونه و ابزارو پلاگین، روانه صدها و هزاران نفر از گوگل یا هوش مصنوعی ها بریزن تو سایت شما و سفارش بدن،
به من یاد بدید و مبلغ بسیار بزرگی هم پرداخت میکنم بابتش. تمام پروژه های اجرایی خارجی که دستم هست(و واقعا سخت و زمان بر هست) و فروش محصول آموزشی(دوره) هم میذارم کنار کلا و میرم که توسط ابزار شما، جریان مالی خیلی بزرگتری برای خودم ایجاد کنم و صد ها برابر مبلغی که به شما پرداخت میکنم هم خیلی سریع در میارم.
سپس میام یک پست میذارم و رایگان آموزشش میدم و میگم بچه ها! کلا دور خودمون میچرخیدیم! گوگل ادز و SEO/AEO و متاادز و گوگل بیزنس/مپ ادز(زیرمجموعه همون گوگل ادز) و تمام کانال های مارکتینگ بیخود و اشتباه بود. هممون اشتباه میکردیم. یه ابزار کافی بود ما رو سریع و ارزون و راحت به مشتری برسونه.
بعد هم میزنم تو کار املاک و پاسپورت چند تا کشور رو از طریق خرید ملک میگیرم و بقیه زندگیمو به گردشگری، دوچرخه سواری در تابستان های سوئیس میگذرونم و یک صرافی بزرگ هم در مرکز امارات با شعب مختلف در سراسر جهان، تاسیس می کنم و میام میگم همون پستی که اون روز گذاشتم و exit کردم یادتونه؟ همه اینا رو از اون پست اینستاگرام و اون پلاگین یا ابزار بدست اوردم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/mohsentavoosiseo/963" target="_blank">📅 12:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به من گفت: "خب حقوقتو گرفتی"!
تو ده سال جلو بیفت.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/mohsentavoosiseo/962" target="_blank">📅 15:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تله دلسوزی برای شرکت
تو ویس گفتم "خلق کن"
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/mohsentavoosiseo/961" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تله دلسوزی برای شرکت
اعتبار به صورت نقلی منتقل نمیشه
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/mohsentavoosiseo/960" target="_blank">📅 15:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/mohsentavoosiseo/959" target="_blank">📅 15:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-956">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اینها رو تو اپدیت دوره پوشش دادم(اپدیت در حال ضبطه)
Agent بالاسر Agent
——-————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/mohsentavoosiseo/956" target="_blank">📅 11:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-955">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کلاد یا چت جی پی ای کدکس یا آنتی گرویتی گوگل؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/mohsentavoosiseo/955" target="_blank">📅 11:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-954">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توضیح ویس های بالا و بحث سیستم سازی در کلاد و یاد دادن به هوش مصنوعی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/mohsentavoosiseo/954" target="_blank">📅 11:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-953">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم بعد از اینکه فهمیدند کلاد هم اخیرا ویس رو گوش میده و میفهمه و متن روان میکنه.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/mohsentavoosiseo/953" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-952">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم درباره ویسی که از سمت شرکت بروکر به عنوان ایراد محتوایی گفته درباره محتوای ما.
بخش ۲</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/mohsentavoosiseo/952" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-951">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم درباره ویسی که از سمت شرکت بروکر به عنوان ایراد محتوایی گفته درباره محتوای ما.
بخش ۱</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/mohsentavoosiseo/951" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-950">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جواب اون سوال.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/mohsentavoosiseo/950" target="_blank">📅 12:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این ویدیو درباره این ویس (سراب پروژه گرفتن) هم هست.  تله شهرت! تله geek بودن.  تله دانش بالا. تله محصول نداشتن در ازای برند عدم توجه به فرسایش ذهنی    https://youtu.be/njtLVwnzyIY  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/mohsentavoosiseo/946" target="_blank">📅 12:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMgS3MRioKD_w33myBeTBjQShJh21NoZoYGsoUft1sn7MEnb_w_1fW0Brzm_zJw1reaMZG2x_bbOyiCz5kXfHHPNw4Tra-VECLA2fDcullEtjVDmcgo_oC5_d02ButUtY4MHQIF9RLDmLYPsCnwYNv_knkNbw_OtZgL1AGc0QOzIcw4ZvXwQV-ti0pOJyyOyrD7sM_JWVv4dn3z9ZgNDEaXYyJZZg7xpHglzNcrPGOIeaWxjLEo31NYJvbKlnPhMQGSHjMXmTnHpcosi_1SICl5mbsYDxe16kCjIFp-FG6NR9CMYdj--QD0DW2EUlfR59OIqMvCQxDHW7YCpDHli0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bc2VSMl3j6-nqINP783yxjmgKZwjpv-oN7fDt4h8yOvjBn2d0rKxLtyvt1KR97NpzAnYNnn6Qyy276ifRF-RCjyCSb2MSBQGqqFCVar9orsr25oGui1k_s39QtNSAvW9-BbaaphTj2BS2cAIgBZVhAOH0pTgQDLqP5-TlQdD8TDBaDpvNElxvB1XN6EOf058L6ZyGQLZdjTZrzp1qgQ3nCbUHvbH7_HTs7922vA-j1vsQFjie1JaIQfApiNh-FRgaETcGFgJTnf_AJP9CwOsIaPuGqykdE8XGb9Czbn2bw_fySjRSTJxEKAMyHIYiSzj9-KuhyOm2169fM-S-QlHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnhkeTdVnWOv1pxk_71cnxX8N4XZuU8SYnA_IY85AX2tZ1WGx1DEv2r92aKPz-ZW2T53YctxRD9yaUuzlOMJhx1EPYOMXSxSgO9tyXLIrXHVVzsfJd_uHuIXnUhwkiHdrPBxKq9hmX38TW4LZLzw2vCrj_0DLxk5FopnZtm1IWxKnPhEXiydZCmcLwjdKsfj1nK1WHwFIReRyZl2IKxnC4UrCyFnC_bNvK10tzb3xCecj-zRY3_xpjZRtNmU_FSgpUlEf5XEqvDKt1cUiXEBCEtE1pcLzJJgF3urj3nbI537W1zdvsi2ihepGQy5XIHBlPh4yHiZwOMWluA_JQkjKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول به نظر موفقیته. عکس دوم رشد کلیک ایمپرشن اسم برند هست در حالتی که رتبه فرقی نکرده. عکس سوم فیلتر رجکس غیر برند هاست که صفر هست آمارش!
روی سایت هم چند ماه هست حسابی داره کار میشه.
1️⃣
❓
ممکنه تبلیغ شده یا کمپینی بوده که موقتا اسم برند، سرچش زیاد شده؟
2️⃣
❓
ممکنه رو اسامی برندی رتبه نداشتیم که الان داریم؟ مثلا مشابه های اسم برند اصلی؟
3️⃣
❓
ممکنه اسم برند رقیب شبیه ما بوده باشه و اون سرچش زیاد شده ولی رو ما کلیک شده؟
4️⃣
❓
ممکنه چیزی غیر از موارد بالا باشه که هنوز ازش خبر نداریم؟
جواب من:
هر چهار احتمال رو باهم احتمال میدم. هر کدوم بخشی از تاثیر افزایش ده برابری کلیک هستند. در آینده واضح تر شد و تحلیل کردم میگم.
پی نوشت:
تحلیل و نتیجه گیری از نمودار پوزیشن روی بیش از یک exact query اشتباه فاحش و بزرگی هست. چرا؟
اینجا
و
اینجا
گفتم.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/mohsentavoosiseo/943" target="_blank">📅 00:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1HV_urKBZVhku6Zx6SWuEWEsmOcpF4dcqEQzh0CLIGWWPWGy4TtKVMZ-7hbmQVS4qhpwGAehBfFhhWGeCyeDpqLkLGbTIw53YDeaFZf7MrTweJFH4c_ZtVpFkuk1VQatP21YjNGiD4pao2l9CSJiqIDA4sEDl4v8HsFJy9TRr2npPsrVkNtxp6ou-1aip9g1VXalwDkalLqVSvdD7o5VVaOgi7K1brEhhhjvRBX0QkPdYBPx2JyNl0vRbvnVdlBEiP4ZAtq3zbrGgD1WA56BJYdmg7lOdw3OgEr9r6vhGo5k8PS3yOmkDqKGbXS91F-KRDslO598WTVowhPzh0faA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/mohsentavoosiseo/939" target="_blank">📅 18:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Overlearning
Unlearning
❗️
مهارت یادگیری زدایی و جلوگیری از زیادی یادگرفتن تو این عصر خیلی مهمه.
❓️
چقدر عمیق شیم؟ از کجا به بعد زیادیه؟ چاهی که از یادگیری زیادی عمیق و بیش از حد داریم می کنیم، به آب و چشمه و گنج میرسه واقعا؟
❓️
چجوری بفهمیم داریم زیاده روی می کنیم تو یادگیری؟
❓️
تله آدم های باهوش و با استعداد و قوی چیه؟
❓️
وسعت دید همیشه باعث بهبود عملکرد میشه؟
❓️
پرداخت بهای عمیق شدن بیش از حد، میصرفه به نتیجش؟
❓️
چجوری بفهمیم تو overlearning افتادیم؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/mohsentavoosiseo/936" target="_blank">📅 23:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">واقعیتش ترسیدم! جدی جدی چت رو بست!   خطرناکه! بنظرم یکی باید جلوی هوش مصنوعی و آنتروپیک رو بگیره. چرا باید یه ماشین لحن صحبت براش مهم باشه و بهش بربخوره و حتی کار قهریه انجام بده و اون چت رو کلا غیر فعال کنه!   پس فردا میاد کل اکانت هم لابد بن میکنه! پس فردام…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/mohsentavoosiseo/933" target="_blank">📅 14:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xfto6etvGet35w0O8v_mO-20KhFaP4dhN-xSV7oBBZ6cP3usQSZfwK1oOzhjYREzDrE-1ReVmYsywvjEcQyUZtRhhh9-Lw3RbEFEXp3rptucWfnmTbYdTzx2EQuyC-9v5iP32FEFs_ROB4PEF1MbS6EuT88Shfbc973GVW7QwQimiLwFp_Fg4OxVFa5CDBxGAf_NMxVh9yqr0ht7BRB1lkJpNpUoWs44VK2HEwKNJJWIW0_3hn2vpnHX219SEXcy699wrz22g--RJ6lg_20qDySELg8B9eNYi4YL5CVjT2rfl6gpsoM7pUUdBBRvRtMP4TA3dUD97RU8Ttyt6SHIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیتش ترسیدم! جدی جدی چت رو بست!
خطرناکه! بنظرم یکی باید جلوی هوش مصنوعی و آنتروپیک رو بگیره. چرا باید یه ماشین لحن صحبت براش مهم باشه و بهش بربخوره و حتی کار قهریه انجام بده و اون چت رو کلا غیر فعال کنه!
پس فردا میاد کل اکانت هم لابد بن میکنه! پس فردام میاد به ما دستور میده!
من برای اولین بار ترسیدم. این خوب نیست اصلا!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/932" target="_blank">📅 14:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/mohsentavoosiseo/931" target="_blank">📅 11:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ساختار سلسله مراتبی URL ها، یک احساس، بیش نیست. هیچ ربطی به درک گوگل از محتوا یا ساختار شما نداره.
+روش پیشنهادی بهتر
و حتما
ویس بعدی
هم گوش بدید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/mohsentavoosiseo/930" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/mohsentavoosiseo/929" target="_blank">📅 13:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
سرابی به نام پروژه گرفتن
❗️
به نام پروژه خارجی داشتن
❗️
فکر نکن تمام ماجرا اینه بلد باشی و حرفه ای باشی.
❓️
من به گذشته برگردم و کسی من رو نشناسه چیکار می کنم؟ محسن طاوسی ای که بلد هست ولی بدون ارتباطات و بدون اینکه بشناسنش، چه مسیری رو میره؟
مسیر من رو نرید. از من استفاده کنید. از دانش من. از تجربه من. ولی مسیر من رو نرید!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/mohsentavoosiseo/928" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آموزش پایین اوردن نرخ تبدیل
😶
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/mohsentavoosiseo/926" target="_blank">📅 16:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صحبت از اپدیت شد، نیاز هست به دوستان یاداوری کنم، محتوای متنی و ویدویی من رو درباره بحث جاوااسکریپت ببینید حتما.
برای وردپرسی ها کاربرد نداره. برای سایت اختصاصی ها و دولوپر هاست:
سئو سایت های وابسته به اجرای جاوااسکریپت در مروگر
ارتباط جاوااسکریپت با هزینه های گوگل
سئو صفحات فیلتر دسته بندی فروشگاه - Faceted Navigation
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/mohsentavoosiseo/925" target="_blank">📅 16:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Mohsen Tavoosi – چرا آپدیت های گوگل آنقدر ها در لحظه مهم نیست؟</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/mohsentavoosiseo/924" target="_blank">📅 16:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چرا آپدیت های گوگل آنقدر ها در لحظه مهم نیست؟</div>
  <div class="tg-doc-extra">Mohsen Tavoosi</div>
</div>
<a href="https://t.me/mohsentavoosiseo/922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چرا آپدیت های گوگل اونقدر ها هم در لحظه مهم نیست؟
چرا نباید نگران اپدیت ها باشید؟
وقت تلف کن ترین کار ممکن، اینه که تند تند برید ببینید گوگل چه اپدیتی داد. رسمی بود یا غیر رسمی.
درست اینه که فرض کنید گوگل هرروز اپدیت میده. اونم چندین اپدیت. هم رسمی هم غیر رسمی. واقعا هم همینه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/mohsentavoosiseo/922" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">طنز:
موقع تهیه گزارش به کارفرما، وقتی پروژه ای 400 تا دونه کلیک داره در ماه، و 40 تا کلیکش کم میشه، میگیم، طبیعیه ده درصد کم و زیاد اصلا درست نیست در محاسبات و تحلیل بیاد در دنیای Organic Search.
اما وقتی 40 کلیک زیاد میشه نسبت به ماه قبل، 40 بار در گزارش، مینویسیم 40 تا کلیک اضافه شده
😎
✅
ولی واقعا، جدی، رشد و افت و درجا زدن رو باید همه رو نوشت. فاکتور هایی که هیجان الکی هست چه مثبت چه منفی هم باید نوشت.
✅
برند رو از نان برند هم باید جدا کرد حتما.
✅
میزان رشد ایمپرشن ها رو باید لحاظ کرد وقتی کیورد جدید رتبه گرفته ولی کلیک نگرفته.
کارهایی که فعلا باعث رشد نمیشه و حتی ممکنه باعث افت کلیک بشه ولی زیرساختی و لازم هست(مثل اصلاح تارگتینگ و هرس)، باید بهش اشاره بشه که توقع و انتظار طرف از نتیجه سریع، بیاد پایین.
❌
به هیچ وجه هم نباید نمودار کلی پوزیشن نشون داد از کل سایت. برای تک کیورد Exact اکیه. برای کل سایت، بسیار بسیار اشتباه و غیر حرفه ای هست.
اینجا
و
اینجا
رو بخونید.
متاسفانه بعضی ها که تجربشون بیشتر میشه فکر مکنن ایمپرشن کلیک ملاک نیست، میانگین رتبه ملاکه و شبیه پزشکان متخصصی عمل میکنن که زمان پزشک عمومی بودنشون، درمانشون بهتر جواب میداد. نمودار کلی رتبه برای کل یک دامنه، آمار بسیار بسیار تباهی هست.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/mohsentavoosiseo/921" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9jvN9QGFhLcVgyNCbqFXdsY-b5hycOXsrnjbUUYqE6rM5Jl_VaSpnvPvsY6BdTy70TwMkzWZIOOqGO5kRBlvj_FJ8Ra0O1oIAim4CTY0i8HeWSF20fZDzSPIVAkNjf-BJxa51HHTnq5mf417T_tJZ_eFfL6p57l-5Ds0wp_8WeUt47vPKM7fpqcuLn_fOCz3y-jIaDZv0ZfYvWCQKTlWmZC9I9MGYrUeW2qRKlWjwW6eiusH8Bk6Fg7VCJB5waDCmpMqbnIboa2-61kcMTW7y5XcjrG61BSWmjYa5an3izUQKz888DrDht5l6OapKsizRftj-3Ai_SxG9DCee1nqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیچاره گوگل. عقبه هنوز.
تازه تو بعضی سایت های غیر فارسی بخش Generative AI داخل Performance اضافه کرده.
فعلا کلیک رو یا اصلا دیتاش رو ثبت نمیکنه یا تو گزارش نمیتونه بندازه. یا اصلا کلیک نمیگیره که برای من ننداخته. و طبیعیه که کلیک نگیره.
چرا بیچاره؟ چون خیلی عقبه. ما رفتیم تو آمار گیری از Generative Engine ها، این تازه بعد مدت ها آمار AI Overview خودش رو تازه داره میندازه. از گوگل انتظار بیشتری بود. ولی خب. خوبه باز.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/mohsentavoosiseo/920" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لیست بایگانی مقالات (پست ها) من که سال 93 , 94 منتشر شدند! یعنی 12 سال گذشته. از سایت web archive.
✅
که همچنان معتبر هست! و بسیار همین الان با پوست و گوشت، لمس می کنید! باز هم باید بگیم سئو عوض شده؟ اصول سئو همون اصول هست!
اون زمان کسی نمینوشت و فقط بلغور ترجمه در سطح وب بود.
ولی می تونید خط فکری الان من رو 12 سال پیش ببینید! حتی پست دارم با عنوان "عصر بی حوصلگی آدم ها! که متاسفانه تو web archive نبود.
هوش مصنوعی گوگل به زبان ساده
اشتباه نکنید! این مقاله سال 93 من هست!
چرا محاسبات ما در سئو غلط از آب در می آید؟
قوانین نانوشته گوگل
خاصیت تضریبی فاکتور های سئو
تشخیص رقابت کلمات کلیدی
(پست تلگرام رو اپدیت کردم و این رو اضافه کردم. جا افتاده بود)
تناقض های گوگل
بروز رسانی Freshness گوگل – تغییر لحظه ای نتایج با فرشنس
پرستش گوگل
114 فاکتور رتبه بندی گوگل
لینک بیلدینگ نکنید وگرنه پنالتی می شوید!
اینجا در نقد تفکر اون زمان بود که تازه پنگوئن نسخه های چندمش رو داده بود و همه ترسیده بودند که کلا دیگه لینک سازی نباید کرد. و این تفکر که بک لینک بی اثر شده. اون زمان هم بود. اون موقع من میگفتم A و T از EAT رو چیکار می کنید پس؟ بهرحال فعالیت اف پیجی حتی نوفالو نیازه. میگفتن نه فقط محتوا کافیه. محتوای خالی فقط E هست. اون موقع هنوز E دوم یعنی Experience نیومده بود.
سه راه پنالتی شدن در گوگل
روش های خروج از پنالتی گوگل و ریکاوری
تراست رنک
محتوا پادشاه نیست
قوانین گوگل درباره بک لینک
جهت اطلاع کسانی که تازه وارد سئو شدند، هنوز هم در اواخر 2026 همین قوانین هست!
برندینگ، دست برتر سئو
اولین ویدیو یوتیوب من سال 94
- بررسی چند موضوع رقابتی در ایران
(ورودم به سئو از 91)
اگر دوره من رو دیدید یا حتی ویدیو های رایگان من رو، ادبیات و لحن این مقاله ها، براتون آشناست.
همین مطالب هم متاسفانه بدون منشن و یاد کردن و چیزی، توسط بعضی از دوستان، از زبان خودشون مطرح میشه.
حالا همون محسن طاوسی 15 سال پیش، یک اپدیت game changer داره که کاملا تهاجمیه! و عملا انقدر بزرگه که میتونم بگم یک دوره است!
دوره تهاجمی سئو بین المللی با Claude . بدون مرز جغرافیایی و زبانی. برای اکثر مدل های SERP فارسی و غیر فارسی. که در حال ضبط هست و برنامم اینه قبل از پایان 2026 منتشر بشه و هرکس دوره رو داشته باشه رایگان دریافت میکنه.
چرا تهاجمی؟ Aggressive در اینجا به معنی شدید و طوفانی هست. تا نبینید متوجه نمیشید چرا اسمش این هست. برای همین سورپرایز هست. ولی انتظار رو پایین نگه دارید که بعدا سرخوردگی ایجاد نشه. فرض کنید یک آپدیت معمولیه. خیلی معمولی. سرفصل های حدودیش هم در صفحه دوره هست هم در
این پست تلگرام
.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/mohsentavoosiseo/919" target="_blank">📅 12:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-917">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به زودی به جایی میرسیم که اخاذی از skill ها و md ها و اسناد کلاد میشه.
ما بحثی داریم به نام پرامپت های چرخشی یا لوپ یا تکرار شونده. بعد بالغ شدشون میشن Agent.
پیچیده نیست ها! مثلا یه کار رو سه بار میگی چک کنی بازبینی و اصلاح کنه. بعد مامور(agent) درست میکنی که اینکارو انجام بده. بعد اون ایجنت رو میذاری سر کارش، هربار خودکار انجام بده.
چند وقت یک بار هم میری سوله مامور هات، بهشون آب و علف میدی و پیچشون رو سفت میکنی و برمیگردی پی زندگیت.
چجوری اخاذی می کنند؟
مثلا میدزدند فایل های شخص، شرکت و سازمان شما رو و میگن انقدر بده تا این همه زحمتی که کشیدی این سیستم و مستندات و مهارت ها و بلوغ رو که ساختی، بهت برگردونیم.
دو بیت کوین بده بهت پس بدیم. شرکت های بزرگ هم می ارزه براشون که این باج رو بدن.
من بخش سئوییش رو آموزش میدم تو اپدیت جدید دوره که در حال ضبطه. بخش های دیگه خارج از سئوش با خودتون
😎
البته سئوش رو استاد شید بقیش هم استاد میشید.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/mohsentavoosiseo/917" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مقاله من حدود دوازده سال پیش!
March 2015!
ویرایش هم نشده. همون خاصیت تضریبی فاکتور های سئو، چیزیه که تازه بعضی ها دارن کشفش میکنن. یا بهش فکر میکنن.
من خیلی خوب بلدم پیچیده حرف بزنم جوری که فکر کنید واااای من حالا حالا باید دانشمو زیاد کنم تا بفهمم محسن طاوسی چی میگه. اما فایدش برای شما چیه؟
برام مهمه مخاطب من، یه چیزی دستش بگیره و اجرا کنه و فقط نمایش سواد من نباشه.
114 فاکتور رتبه بندی در گوگل
https://www.linkedin.com/pulse/114-%D9%81%D8%A7%DA%A9%D8%AA%D9%88%D8%B1-%D8%B1%D8%AA%D8%A8%D9%87-%D8%A8%D9%86%D8%AF%DB%8C-%D8%AF%D8%B1-%DA%AF%D9%88%DA%AF%D9%84-mohsen-tavoosi
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/mohsentavoosiseo/916" target="_blank">📅 16:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🟢
دوره جامع SEO/AEO بین المللی با AI
🟢
از این به بعد، هر ماه، قیمت به صورت تدریجی افزایش داره و دیگه اطلاع رسانی مرتبط با قیمت انجام نمیشه.
https://mohsentavoosi.com/course/seo/
آپدیت جدید، صفر تا صد سئو هست و سرفصل هاش این موارد هست که هنوز در لینک صفحه دوره قرار داده نشده و محتوای این صفحه، بعد از انتشار کامل این بروز رسانی جنجالی، به روز خواهد شد:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors که جداگانه نیست و کاملا در فصل ها آمیخته شده است.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
🟢
Local SEO برای بیزنس پروفایل ها
🟢
تحلیل و بهبود وضعیت در AI Generative ها
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
به سرعت در حال ضبط هستم. و تیم تدوین، در حال تدوین هست. از نظر خودم این اپدیت، سورپرایز هست! اما دوست ندارم چیز بزرگی در ذهنتون بسازید که بعدا انتظار ایجاد بشه.
این امضا یا مشابهش، از این به بعد زیر پست بسیاری از محتواهای کانال، قرار خواهد گرفت و اطلاع رسانی قیمت و... حذف خواهد شد.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/mohsentavoosiseo/914" target="_blank">📅 12:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/mohsentavoosiseo/911" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/mohsentavoosiseo/910" target="_blank">📅 14:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/mohsentavoosiseo/909" target="_blank">📅 14:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/908" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خطاب به همه کسانی که خیلی حرفه ای و باهوش هستند.
خطاب به کسانی که از اینکه یک سری بی سواد یا کم سواد حرف اشتباه میزنن، ناراحتن.
خطاب به همه با سواد ها!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/mohsentavoosiseo/907" target="_blank">📅 13:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه اشتباه بزرگ کسانی که تازه مهاجرت کردند یا تازه درگیر پروژه های غیر فارسی شدند یا حتی مدت زیادی گذشته اصلا،
❗️
اینه که فکر میکنن جهان یا بین الملل یا "خارج"! یا کشورهای دیگه، همونی هست که ازش تجربه دارند و همه چیو با عینک خودشون میببنن.
❗️
❗️
حتی استناد میکنن که فلان همکار یا مدیر خارجی هم اصلا اعتقادش همینه.
❗️
❗️
❗️
در حالی که همون همکار خارجی هم اشتباه میکنه. اون هم فقط نگاه خودشو داره میگه و تجربیات خودشو.
✅️
در همه جای جهان(غیر از هند و پاکستان و اندونزی و روسیه و...)، لینک بیلدینگ و پست مهمان مشابه رپورتاژ، بوده و هست و خواهد بود.
✅️
مدل پیدا کردن و صحبت با رسانه ها در کمپین های روابط عمومی PR، یعنی کاملا کلاه سفید، بوده و هست و خواهد بود.
✅️
مدل اینکه کلا کمپین اف پیج یا PR و کلاه سفیدم ران نشه و فقط تبلیغ بنری یا گوگل ادز یا کلا کمپین های تبلیغاتی فقط ران بشه هم هست که سئوشون فقط تکنیکال و سئو داخلی و کیورد ریسرچ و ساخت صفحه میشه(اونم محدود).
✅️
✅️
همه اینا هست. فقط شرکت با شرکت، فرق داره. سایت با سایت فرق داره‌. هرچقدر بزرگ تر باشن شرکت ها، مدلاشون به مدل آخر نزدیک تر میشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/mohsentavoosiseo/906" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سوال:   دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش  اولین سایت که ترب هستش  ولی اگه ترب رو حساب نکنیم میشه سایت سوم طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته  ولی کلیک ۵ تا!! راه حل برای کلیک گرفتن چیه؟ عنوان  و متا هم از دو رقیب دیگه…</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/mohsentavoosiseo/903" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-902">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سوال:
دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش
اولین سایت که ترب هستش
ولی اگه ترب رو حساب نکنیم میشه سایت سوم
طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته
ولی کلیک ۵ تا!!
راه حل برای کلیک گرفتن چیه؟
عنوان  و متا هم از دو رقیب دیگه خیلی بهتر هستش.
چون روی کلمه ی اصلی اومده بالا
پاسخ در ویس:
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/mohsentavoosiseo/902" target="_blank">📅 19:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سوال:   من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟  پاسخ: https://t.me/mohsentavoosiseo/511 این ویس و ویس پایین  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/mohsentavoosiseo/901" target="_blank">📅 13:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-900">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سوال:
من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟
پاسخ:
https://t.me/mohsentavoosiseo/511
این ویس و ویس پایین
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/mohsentavoosiseo/900" target="_blank">📅 13:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/mohsentavoosiseo/898" target="_blank">📅 11:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/mohsentavoosiseo/897" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تولید محتوا با کلاد
استاندارد سازمان رو برای کلاد تعریف کردن
هوش مصنوعی، چت کردن و چهار تا فایل اتچ کردن و اسکرین شات فرستادن و چهار تا پرامپت خوب دادن نیست! اینا خیلی مقدماتیه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/mohsentavoosiseo/896" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/846
بن میشیم نمیتونیم کلاد بگیریم!
Ban
#بن
#ban
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/mohsentavoosiseo/895" target="_blank">📅 15:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/mohsentavoosiseo/894" target="_blank">📅 15:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تفاوت کلاد تو چیه دقیقا؟ نسبت به بقیه AI ها؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/mohsentavoosiseo/893" target="_blank">📅 14:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=SNIanQtwjKAjfH8WJtRFlyAy-sbqdrNcdztwzMjJpn7xcdd9OXsYFUgxs0iSN1dr3bVvIQRnOHY0SaNw5HLaLbZ3ep7Pxkq74N8Pe2O0LoJmppAGN8qSzVoAnKKDiv24IgHS0KcqxNYoplptcE57BOYccC7KwmPPbAyAbyk4dghD0fEboW11y4KS7LwC8qqx4Hjfhe2P9VomqytBx22ODjckL3QPxF4iQmd3AeJk5CMJD7sseoa6oWwfy1fxOB5Sir625Wp4BMOJUiVgi9TZ2rzQ8TbCZHhHnymE2gFSmFq4i5SOMXwk9gax1-OYvkKFMkc-NytcxWn84v9cRSCxNCB2QxMImGr3nws3y9mRAqjjOCdMiv5PlDftjG_ga9_lwvhCH4zfje2CeQKGgKVrxNgR5D2W8AURK3XqIngMlUZLlvKUEosDzyHAql1V9vNMuW617EVhZKBZU04z9uAfLHZGcCypCV5sZA-GcR1PVuBpmJfPO4-OxMO_8Q1MfUsxC1qZeswerkPNTTJCXiPkB8R8Co5H4xJsgNL1GBRx1e_bpVNN2Ki6qYOlF7s4esl7GqJOjXUSIju_2i8HWCOf_ESuGRZ0cfH_q-bKyEshBVpL2yRD9lrW9TYr04hWM7gKcy8Q6OXIcSJux8YS36vXcqBrc0m8nMh0TLqR9QLDSes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=SNIanQtwjKAjfH8WJtRFlyAy-sbqdrNcdztwzMjJpn7xcdd9OXsYFUgxs0iSN1dr3bVvIQRnOHY0SaNw5HLaLbZ3ep7Pxkq74N8Pe2O0LoJmppAGN8qSzVoAnKKDiv24IgHS0KcqxNYoplptcE57BOYccC7KwmPPbAyAbyk4dghD0fEboW11y4KS7LwC8qqx4Hjfhe2P9VomqytBx22ODjckL3QPxF4iQmd3AeJk5CMJD7sseoa6oWwfy1fxOB5Sir625Wp4BMOJUiVgi9TZ2rzQ8TbCZHhHnymE2gFSmFq4i5SOMXwk9gax1-OYvkKFMkc-NytcxWn84v9cRSCxNCB2QxMImGr3nws3y9mRAqjjOCdMiv5PlDftjG_ga9_lwvhCH4zfje2CeQKGgKVrxNgR5D2W8AURK3XqIngMlUZLlvKUEosDzyHAql1V9vNMuW617EVhZKBZU04z9uAfLHZGcCypCV5sZA-GcR1PVuBpmJfPO4-OxMO_8Q1MfUsxC1qZeswerkPNTTJCXiPkB8R8Co5H4xJsgNL1GBRx1e_bpVNN2Ki6qYOlF7s4esl7GqJOjXUSIju_2i8HWCOf_ESuGRZ0cfH_q-bKyEshBVpL2yRD9lrW9TYr04hWM7gKcy8Q6OXIcSJux8YS36vXcqBrc0m8nMh0TLqR9QLDSes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/mohsentavoosiseo/892" target="_blank">📅 14:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سوال یکی از بچه های گروه دوره:
میشه بهم نظرتون رو بگید که چقدر تفاوت هست بین جمنای با اشتراک گوگل پرو و کلاد ؟
چرا کلاد انقدر محبوب شده و اقلای طاووسی هم دارن تاکید میکنن روش؟
تفاوت سطحش با جمنای در چی هست ؟
خصوصا برای تولید محتوا تجربه دارید جفتش رو مقایسه کنیم؟
البته چون اپدیت جدید در حال ضبطه این سوال پیش اومده براشون
😎
. پاسخ:
https://www.instagram.com/reel/DcBLYe_MLHx/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/mohsentavoosiseo/891" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پاسخ سوالات پر تکراری که درباره دو پست بالا پرسیده شد:
❓
آیا ما که قبلا دوره رو خریدیم دریافت می کنیم این اپدیت رو؟
بله! فکر کردید من شرکت های خودروسازی داخلی هستم؟ حالا که بازی قشنگ شده جدا شیم؟ شما همراهان قدیمی رو تنها بذارم؟ هوای شما رو که بیشتر باید داشته باشم! پشتیبانی هم دو نفره شده از دو نفر قوی. قدیمی های سال اول خبر ندارند پشتیبانی تلگرامی دارند. جایی دیدید بیفته دنبالتون بگه این ویژگی اضافه شده بیا دریافتش کن. قبلا پولش رو دادی. من میگم! الانم گفتم
😎
❓
این اپدیت چه زمانی منتشر میشه؟
شما تا پایان 2026 روش حساب کنید. خودم نمیدونم. در حال ضبطم. دوسه ماه طول میکشه حداقل. همین ماه البته فصل اولش میاد که البته سبک هست فصل اولش.
❓
من تهیه کردم ولی اون دوره بین المللی، توش خالی هست هیچی نیست!
بالاتر گفتم، اون رو تا اخر 2026 حساب کنید کامل بشه. کم کم میاد در حال ضبطم. اصلا هم نمیتونم عجله کنم. شما اون یکی رو ببینید. دوره سئو جامع. سوالات بعدی هم بخونید!
❓
به درد سایت فارسی هم میخوره؟
بله. ولی مثال های من به همه زبان هاست و کلا مبتنی بر زبان یاد نمی گیرید. مبتنی بر وردپرس هم یاد نمیگیرید. اما هر زبانی و هر CMS و برای وردپرس هم یاد می گیرید.
❓
برای چه سطحی هست؟
از صفر تا خیلی حرفه ای ها. همه. ولی کسی که تا حالا پشت کامپیوتر نبوده یا در حد لاگین کردن تو سایت ها بلد نیست یا تا حالا تو زندگیش فایل word باز نکرده یا بلد نیست وی پی ان استفاده کنه، نه ها!
❓
باید صبر کنیم اپدیت جدید بیاد؟
نه! ببینید دوره فعلی رو. دوره جامع فعلی که دسترسی دارید، کامل و به روز هست. اگر خیلی بی حوصله هستید از فصل "تحقیق کلمات کلیدی و صفحه بندی در عصر هوش مصنوعی" شروع کنید. همش مهم هست و موثر و به روز و کاربردی.
❓
میشه فقط آپدیت AI سئو بین المللی رو جداگونه بگیریم؟
کلا یکی هست! صفر تا صد هست. هوش مصنوعی جدا نیست. بین المللی هم جدا نیست. قیمت دوره هم بسیار پایین هست بخاطر جنگ. کلا امکان بخش خاصی رو جدا خریدن وجود نداره. یا همه یا هیچ هست.
❓
سرفصل های این اپدیت جدید که تصویر یک دوره جدید گذاشته بودید چی هست؟ تو صفحه دوره فعلی سر فصل های این اپدیت هست؟
اون عملا میشه محتوای فصل سئو بین المللی همین دوره جامع، که صفر تا صد سئو به هر زبانی و کاملا آمیخته با هوش مصنوعی(Claude) هست.
توی صفحه فعلی دوره، این سرفصل ها نیست. اما اگر بخرید، این ها هم دریافت خواهید کرد:
موضوعاتی که در آپدیت، پوشش داده میشه این هاست ولی دقیقا عنوان سرفصل ها این نیست. به دلایل متعددی، فقط کسی که دسترسی داره، عنوان ها و سرفصل ها رو دقیق میبینه بعد از انتشار:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
ساخت دسته جمعی صفحات سایت با AI
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
جهت خرید، به
@mohsentavoosisupport
پیام بدید. من نیستم پشت این اکانت. بچه ها هستند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/mohsentavoosiseo/890" target="_blank">📅 18:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
قیمت دوره، قرار بود سال 1405 بشه 18 تومن. بخاطر دو تا جنگ و دی ماه، با مبلغ پایین تر در دسترس شد و از 1 شهریور(هفته دیگه)، مشه حدود 6. و سپس هر ماه یا هر سه ماه، افزایش قیمت داره. و طبق معمول، تخفیف دوره ای و مناسبتی هم نداره و هر ماه یا هر 3 ماه، افزایش تدریجی داره.
کاهش قیمت بخاطر جنگ بود و هست. کسی که پارسال 12 تومن میداد، امسال 5 تومن رو سخت تر از اون 12 تومن پارسال میده. درامدش فرقی نکرده و هزینه هاش هم سه برابر شده!
✅
به نقل از خود شرکت کنندگان دوره میگم که در هایتلایت اینستاگرامم هم گذاشتم:
اگر اهل یادگیری سئو یا نمایش یا فروش بیشتر در AI ها هستید یا میخواید اپلای کنید یا پروژه بگیرید، یا کسب و کار خودتون در داخل یا خارج رو به هر زبانی، گسترس بدید، اگر دوره رو ندارید یا نگیرید، احتمال پشیمونی و حسرت که چرا زودتر نگرفتید بالاست. به نقل از خود بچه ها.
❕
اما در عین حال، تضمین نمی کنم. هیچ تعهد و در باغ سبزی هم نشون نمیدم. صرفا هر آنچه دارم رو در دوره آموزش میدم که هر کس با من جلو بیاد، قوی، حرفه ای، بازای و تجاری و بین المللی و با زیرساخت درست بالا بیاد و آبکی نباشه آموزشش و
احتمالا
به چرخه عوض کردن دوره های مختلفش پایان بده.
🟢
قبلش تحقیقات خودتون رو انجام بدید. اگر ذره ای شک داشتید، تهیه نکنید. پولی که با شک پرداخت می کنید برای من جذاب نیست.
و در نظر بگیرید، برای کسب و کار خودتون، خرج نقدی میخواد. فکر نکنید فقط یادگیری هست. پول هم باید خرج کنید. مگر اینکه بخواید استخدام بشید یا پروژه بگیرید.
خرید در:
@mohsentavoosisupport</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/mohsentavoosiseo/889" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-888">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG4EwAw0lnCgfPmQlkWGySpm-6GIKvfzmt_0Gm1IEAFDVXkF5p1RfB1wvQe_Txii7fpXGksZ00-7fb7VEjVYJn-6lract4PnbrCvF2ltSKuBx3uFpn6sk1K4M_AApzS7P8WHOD1Jel0kC75PNxvrWci7s_hMjJ4ny05CJAdgT5vVZ4mSGyB8ZaeOkoynd3PlLbInDtJcrmvCu4sWE3GV5FbLM_2XCQWySNa4T2mOmUkt1zQgb_8PS4rcZpomGaVMwjsUAPG5hXD1AC3FqIFvm02SNy14v1JYVZKXLE1iSNLeDBcD6m8BO6leOkwLo7QxpHQgCJISqU-7J5Uu2GtXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسانی که جدیدا دوره رو میخرند، دو تا دوره دریافت می کنند(قدیمی ها نگران نشید تا آخر بخونید).
دوره جدید، برای راحتی ذهن شما جداگونه قرارداده شده و دوره صفر تا صد SEO و AEO برای همه زبان ها و همه کشور هاست! و کاملا آمیخته با AI که ابزار اصلیمون Claude هست. کلاد اختصاصی در محیط خود کلاد. نه این Opus که هوش مصنوعی های ایرانی و خارجی، میفروشند.
البته بگم من مثال هندی پاکستانی نمیزنم. ولی از شرق آسیا یعنی ژاپن، تا قاره آمریکا رو پوشش میدم. آلمانی، ژاپنی، ترکی استانبولی، روسی، فرانسوی، اسپانیایی داریم. فارسی و انگلیسی هم که سرجاش.
این آپدیت احتمالا تا آخر مهر کامل میشه و برای قدیمی ها در فصل سئو بین المللی قرار میگیره. و برای جدید ها، در این یکی دوره
هم
قرار میگیره.
خرید در:
@mohsentavoosisupport
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/mohsentavoosiseo/888" target="_blank">📅 14:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کلاد، برای هر متخصص SEO و هر متخصص دیگه ای ضروری هست و یک هزینه جاری هست. شما میگید من غذا نمیخورم؟ سوار وسیله نقلیه نمیشم؟ اجاره خونه یا پول قبض نمیدم؟
کلاد هم بهش اضافه کنید. بایدیه. اونم اختصاصی. نه اشتراکی. اصلا با محدودیتی که کلاد رو اکانت هاش داره اشتراکی معنا نداره. با این همه قابلیت، فقط چت نیست! باید اختصاصی بگیرید.
اپدیت دوره که تو همین شهریور یک فصلش میاد، کلا با Claude هست. کوبیدم از اول ساختم. نه فقط ایرانی و فارسی. نه فقط حتی انگلیسی! هرچند Base همون قبلی ها هست که الان هم تو دوره هست. فقط یک ابزار قدرتمند بهمون اضافه شده.
به زودی سورپرایز خواهید شد!
😎
پی نوشت:
(کلاد تلفظ انگلیسیش کلاد هست)، ریشه اسمش فرانسوی هست که میشه کلود. شرکت آنتروپیک هم آمریکایی هست.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/mohsentavoosiseo/886" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ابزار های سئو خارجی رو به صورت اشتراکی از کجا تهیه کنیم؟ از سایت لیمیت پس! Limitpass.com ایرانی چطور؟ ابزار جت  سئو و کیورد چی و چند ابزار خوب دیگه...  http://limitpass.com/ https://www.jetseo.ir/ https://keywordchi.com/    کد تخفیف سه سایت بالا:  mohsentavoosi…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/mohsentavoosiseo/885" target="_blank">📅 20:09 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
