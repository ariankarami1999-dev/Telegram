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
<img src="https://cdn4.telesco.pe/file/MTLAxeaui2u_Zq6hgfHRnz6xUtsvPzTZOtnbY9LJpJ2D8XO6SNwxZaI9exg4rqLHDw9pWmFF4ehG2LrpgPWwgQejErWrAFDO5b1STT7CIwyk0uu1jdPM4QgM_DqnTSACtvA9J3gUSmaKBUK8XQACdC2szPWZawu3Bgu8D_q5usyXZt3wYLqq40h6vdB5nKpvNu8zA4wM8L5Fr5y60tjsSuCR41dMYAAke2KSdb-jVMfX8GkK7Cuizn4FAi6sp0Yer_iZJNf16Ak2UsI--KjpiVCpeAl7T9ciV8E8wqAnjqj1CkOnwkj5N8MWqF7Zk5wvurrEe-8A75_JuzELiavguw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 984K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 14:46:41</div>
<hr>

<div class="tg-post" id="msg-142435">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjynST7eBzOMprgjbVhktdu70rERRZzGZIR6vtF1iI9GbztI9BgM1HgHFzUsjxdDtd44VXhJBcGrOWPMf9uyyk0v5iz6OK9Ywq5VQVt3-T_XiuiOJl0s178xt5MPnXncx_JGhRsnICAZuS1Xa8X0qv8NkoxmQlUuzAWZHcnwAl6jTFvXPI5b1N8px_EBehxgm_XGLrfIHLC1u5fDPowwUOwAZmjozdtI0MZhXuvFZ77rVAkeBQbGuAFozyQIrB4CWdqlNAa1fb9iYuwB8TiMqsfwKBE7Giu75M7k7gC0J-5TIlri1vNsHdbel8Cr4FhpE8sUMO7uMarF7z4wdK37AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ تنگه هرمز را منطقه جدید امریکا خواند:‌ یک منطقه جدید در ایالات متحده
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/142435" target="_blank">📅 14:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142434">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رویترز : عربستان سعودی نقل و انتقالات بانکی امارات متحده عربی را تحت نظارت شدید مالی قرار داده است که باعث تاخیر یا برگشت برخی از پرداخت ها شده است.
🔴
مقامات سعودی محدودیت های مستقیم در امارات را رد می کنند و می گویند این اقدامات بخشی از کنترل های ضد پولشویی است، اما منابع آن را سیگنالی از افزایش تنش ها و رقابت اقتصادی بین دو قدرت خلیج فارس می دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/142434" target="_blank">📅 14:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142433">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: تلاش‌های کنونی بر خنثی‌کردن بحران جاری [میان ایران و آمریکا]  و بازگشت به تفاهم‌نامه متمرکز است.
🔴
تلاش‌های ما در مرحله کنونی بر توقف تشدید تنش و بازگرداندن دو طرف بحران به میز گفت‌وگو متمرکز است.
🔴
آنچه ما در قطر می‌خواهیم، توافقی برای بازگشایی تنگه هرمز و برقراری آتش‌بس به‌طور همزمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/142433" target="_blank">📅 14:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142432">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
تام باراک:ما نگرانیم از حملات هوایی اسرائیل به فرودگاه ابوذهور در سوریه. دولت بشار اسد هرگز به اسرائیل تجاوز نکرده و نیروهای نیابتی در اختیار نداشته است. بلکه بارها و بارها تمایل خود را به کاهش تنش با اسرائیل ابراز کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/142432" target="_blank">📅 14:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر:  در ۱۹ مارس بقایای یکی از دو خلبانی را که وارد حریم هوایی قطر شده بودند، پیدا کردیم.
🔴
بقایای یکی از دو خلبان را که وارد حریم هوایی قطر شده بودند، به طرف ایرانی تحویل دادیم.
🔴
طرف ایرانی به دعوت ما برای اعزام یک تیم فنی جهت اطلاع از روند عملیات جست‌وجو پاسخ نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/142431" target="_blank">📅 14:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از منابع غربی مدعی شد روسیه از طریق دریای خزر قطعات پهپادی، موشکی و مهمات به ایران منتقل می‌کند تا ذخایر تسلیحاتی ایران را بازسازی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/142430" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcXVem0PcPY4jWCmp-uaCdLQTIX6L8C1wDOTcD8719r1otOhqVOwSqIrusj3Tcy4dofE0CjeIuK_xa2wMbmqU3seit3ljltSoYik3Frm6bGTFemSFJGCRe_OO73dV66AYgAJQgyqOfgHkmSZ--UUZmeeWZXerUEQFf7UZ481EAB6ARPRNyddiFkyvxTq-JvFqOlUNVSnrHS2YMHRSTRtvG1tVKUhQa4uyQEOXAd1y64rLZ-0A-KnHJvCrtiOcCxGJavpZ2bw5qZKGoZXirOstVb0XyvtvzxfKETKaTWLO9z0MgKorgWut0gy6FEx31T5yNvabIEU47KVZpeNWAJDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه سوریه حملات هوایی را که به پایگاه نظامی ابو الظهور هدف قرار داد، محکوم کرد و اسرائیل را به طور رسمی به انجام این بمباران متهم نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/142429" target="_blank">📅 14:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قطر: تلاش‌های کنونی بر تنش‌زدایی و بازگشت به یادداشت تفاهم متمرکز است
🔴
سخنگوی وزارت خارجه قطر امروز سه شنبه اعلام کرد: تلاش‌های کنونی بر تنش‌زدایی از بحران کنونی و بازگشت به یادداشت تفاهم متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/142428" target="_blank">📅 14:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142427">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
خبرنگار الجزیره: در دوره زمانی ۶۰ روزه که در یادداشت‌ تفاهم ایران و آمریکا آمده بود، نه مذاکرات واقعی‌ای در کار بود و نه ازسرگیری جنگ تمام‌ عیار؛ کمی پیام رد و بدل و موشک‌هایی شلیک شد
🔴
منطقه اکنون رسماً در وضعیت «نه جنگ، نه صلح» قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/142427" target="_blank">📅 13:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142426">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtV5g51c9Iiv-OhhIjzDdXt92dBT6eCvnJ0b5dcNNNJpn2vmzeAPuC7a91ubox6XEO5hNXf2I74_Oh2F6-fgSXgZ6-fRm4Iz-k9VI7gc82SKEqls4qFGQHNRzRRn4Zmi2XhhYQqPNENCWcR2Y6fwGjfED8Xj1nSPbvlbFCJtr520vO6lXOrQob3drqTmPGsCvQqkYimuvSh2b8MeHwmhxjbwCCDz9NEem0ypoExzKfZAqTl6MMNtjjbOpHepWIkCAyfLN2V1T8Ze2cG1K96gI24lrn2zHAcEx7xybZoyetaxuy7U22JZFpyD5v96NUSsSugicWL9gQVhgHrujijy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: تصمیم تهران بر این شده که مسیر تنگه هرمز کاملا ایرانی شده و صرفا از مسیر شمال باشد
🔴
مقامات عالی ایران تاکید دارند که «بازگشایی تنگه» در مقابل «رفعِ کامل محاصره»، «آزادسازی اموال بلوکه شده ایران» و «رفعِ تحریم‌ها»ست؛ اقدامی سخت و پیچیده ولی شاید شدنی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142426" target="_blank">📅 13:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9rkl5aiDgh5vV71M0NhBnElzRrTUOD1ReXgz0gzrCjgUrO50mwtp_jzjj9QZLdUWhxWUOvZ05CiIMPtxoisSny0w2Dux1yhz9Pz2UvayjBUa6z7vF5-VGhfpOtwvcHTHII9Wsdz4G_8K429iHA9WuM7QI8wY2EUzSUvP3f7fdHqJ005j2H8PYPX-f9Z9HTVtHanGPt2JljX9eqvYwlev7A1OoOMc65WgOUIMLXz5i9Tc9yvRvl_OO_ai-3GN-rFJ0qm-pQoqBuvwGkMYPRSgz8dahWRHffkgB1O133MWhYcaDFj7g0PXhrxbzcWjhYTDDhDOnSp0SK4hwcLuPmz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uzb5ELPJpp3n1xMmZiDY0yxoBHAENOtZnmkM7o6gNvSFIrQsNnwl9L6dSInqDSY_4rRwDZf9FNwU5wvc1jp71vL685ITbkYGzG-jQhzHTVmnh0CIRnViDJt1KdfqFgTV-KzCxsMtsiY5e_PcJt02qXoTsv_mAzlOiKUvvTWGeOzd5s6jyoDFHYXbMFLnFZwLMr3Bl832F6bCWlARa5CuPgUCXJfODikJEq_0PaV9Gj1-sWXfyRhTY5cROzHJmk2gTADFziG_uK5vXpZAqjl1MQ5ylWfIMxuUWfcrZ9TZaE7Ryt8O3KqXDVJ8Kh6ScvWBzC3OtB6E1xkR4jqkXGsOzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d3d7902a.mp4?token=MB1jl-fjBHVlgHs2PCNGZNddD7X89wcRxaA0RMnxusRvxg7AbH7VNuSqiDcwYTVqnoifA5wnXOH1ovHXxPpuU4vziEJNejU-v-KMQ-U9IKJv65aSiSwEXIKV-z6Kx3OJv9m0uSsVgbJyrydXv_cVdd7plKnrmRcMF-YMP-e1ZVWsBeRTHFIJkSYwueJu4y2dScsf6HfWjhjFBhq-VpIUG1uf2YiPFHITfUw_5NcFUKHa6uNRt3vPa-S50FYUDONsLpxVJ4HVkro5Ps0vga8JKRddxoxBZzVifrwI68FMcdHcpR7R2J-lYPbxmrrgrc2SIrxv1RfNVHsZpkxq_cAqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d3d7902a.mp4?token=MB1jl-fjBHVlgHs2PCNGZNddD7X89wcRxaA0RMnxusRvxg7AbH7VNuSqiDcwYTVqnoifA5wnXOH1ovHXxPpuU4vziEJNejU-v-KMQ-U9IKJv65aSiSwEXIKV-z6Kx3OJv9m0uSsVgbJyrydXv_cVdd7plKnrmRcMF-YMP-e1ZVWsBeRTHFIJkSYwueJu4y2dScsf6HfWjhjFBhq-VpIUG1uf2YiPFHITfUw_5NcFUKHa6uNRt3vPa-S50FYUDONsLpxVJ4HVkro5Ps0vga8JKRddxoxBZzVifrwI68FMcdHcpR7R2J-lYPbxmrrgrc2SIrxv1RfNVHsZpkxq_cAqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند جنگنده F-15J متعلق به نیروی هوایی ژاپن، پس از بروز نقص در چرخ فرود در حین بازگشت از یک ماموریت رهگیری اضطراری، در فرودگاه ناها در اوکیناوا، فرود اضطراری انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142423" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سخنگوی صنف جایگاه‌داران: استفاده از کولر خودرو مصرف بنزین را ۱۰ تا ۱۵ درصد افزایش می‌دهد، لطفا رعایت کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/142422" target="_blank">📅 13:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe3abc88b.mp4?token=V_mhtR_ntwId5mtC5KpZv1xWa-57Xag3yLL5ZpHpxfQ5-IrEf0X1qFHVWhfEa-iOHrnsPzRj_I4jwT96ytLRRwYYn8YoPXmEEThC3TbB7ziPRmOxfExkVvWtGODgVHxFX6rCxkmxBBFTN4bnO4RNt8_cuevUfOy0V2SszmNadXwyHWalE8IOoB4x7r9WzQ70fl6jl5zEM7vM-5EjmPTmkYJV-FoaVzeUImSNYdnTlMTgbCJwTXYhyrI0sUh5TiF4FU103x4pGSQswt3vfwVSebq89m6rkOfgk90AtQilgWJBqrhYyFrwjuaKGMEIJmpkj8v77grBAkQvQxg1yzRYiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe3abc88b.mp4?token=V_mhtR_ntwId5mtC5KpZv1xWa-57Xag3yLL5ZpHpxfQ5-IrEf0X1qFHVWhfEa-iOHrnsPzRj_I4jwT96ytLRRwYYn8YoPXmEEThC3TbB7ziPRmOxfExkVvWtGODgVHxFX6rCxkmxBBFTN4bnO4RNt8_cuevUfOy0V2SszmNadXwyHWalE8IOoB4x7r9WzQ70fl6jl5zEM7vM-5EjmPTmkYJV-FoaVzeUImSNYdnTlMTgbCJwTXYhyrI0sUh5TiF4FU103x4pGSQswt3vfwVSebq89m6rkOfgk90AtQilgWJBqrhYyFrwjuaKGMEIJmpkj8v77grBAkQvQxg1yzRYiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دادگاه جنایی دولت سوریه امروز «وسیم الاسد»، پسرعموی بشار اسد را با اتهاماتی به اعدام محکوم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142421" target="_blank">📅 13:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
الاخباریه سوریه: حمله به فرودگاه «ابوالظهور» کار اسرائیل بود
🔴
فرودگاه در ۸ نوبت هدف قرار گرفت
🔴
خبرنگار شبکه خبری «الاخباریه» سوریه به نقل از یک منبع نظامی گزارش داد،  جنگنده‌های اشغالگر اسرائیلی بامداد امروز طی ۸ حمله هوایی، باند فرودگاه نظامی « أبو الظهور» در حومه شرقی ادلب را هدف قرار دادند.
🔴
به گفته این منبع، این تجاوز منجر به خسارت مادی به زیرساخت فرودگاه شد و تلفات جانی در پی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142420" target="_blank">📅 13:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142419">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIlETVAqAvcAftwknV76mr-VyTIjqGm0MpBakYHCzxp7Zk9yWKfHhPnlBAIMnNjuSmxiaVVHu1kbA-2j8qSQJGKw0geyJVr7PbKhfDV4UrKVKzd2mM-SlEXvB9sSfksGojuk_rox0O3uSmie5ld3OT48q2elm11EX1Btgep8xi1jCJVLn6BtCdb2coWfB_L7yCWdk4G8zV3_tMVHE_CQ9Rxs3iLY_cDkzMEBcE-fiuo2NvPUucA7CpJbTM1LBp1YdCQR0087J5Zv_kNlz14f2x3gpai82UUJ4JvZFL-FxH9miXxX9_bctU7BK5TEpTbJK7lmMO7mnjZRuFUl0Hr4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از دیدار ۴ ساعته دیروز نتانیاهو و جرد کوشنر، نخست وزیر اسرائیل هی سیگنال مثبتی برای اتمام جنگ در غزه را نشان نداده و اینطور به نظر می رسد که فعلا قرار نیست شاهد صلح در غزه باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142419" target="_blank">📅 13:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=MccqL4PVSXnt2bRhRT47JdcoeAUGEqFp5bndUkfIYNt4LV1Aaj0iwnTEAwMzjsdblt3_lIoBiSLB1dsOGVWOMxNV0SssauWBPknUOYa2cMwnjN01mp_4oDWP6iEPqCXXaETqYRYdu9vzlqs1hkp-_hWbbRVXDb0sLyG-ADHdj2sJgQhNojmY8y6bFUSHen4rjLktZvJbBozVh_bkYS1TLCApVmzciiPNAamkir9zHBeqImwFSPEUKLNLwk5gT2K5OFBmcbFW_r_ZKsvstD7RLk8sXZ0IYErokojWAPBnQEWDF6KsObTNFmCCphOSPKVViEEhWpgxeUwWrc6L5y3gJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=MccqL4PVSXnt2bRhRT47JdcoeAUGEqFp5bndUkfIYNt4LV1Aaj0iwnTEAwMzjsdblt3_lIoBiSLB1dsOGVWOMxNV0SssauWBPknUOYa2cMwnjN01mp_4oDWP6iEPqCXXaETqYRYdu9vzlqs1hkp-_hWbbRVXDb0sLyG-ADHdj2sJgQhNojmY8y6bFUSHen4rjLktZvJbBozVh_bkYS1TLCApVmzciiPNAamkir9zHBeqImwFSPEUKLNLwk5gT2K5OFBmcbFW_r_ZKsvstD7RLk8sXZ0IYErokojWAPBnQEWDF6KsObTNFmCCphOSPKVViEEhWpgxeUwWrc6L5y3gJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنسیس مدل 2013 در امارات: ۵۰۰ میلیون تومن
🔴
ارزان تر از پراید در ایران...
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142418" target="_blank">📅 13:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
قالیباف: صداوسیما باید کانون انسجام و امیدآفرینی برای ۹۰ میلیون ایرانی باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142417" target="_blank">📅 13:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گزارش‌های جدید بلومبرگ نشان می‌دهد که هزینه اجاره روزانه سوپرتانكرهای غول‌پیکر (VLCC) برای حمل نفت خام از خلیج فارس به مقصد آسیا، تحت تأثیر خطرات عبور از تنگه هرمز، به مرز بی‌سابقه ۵۱۰ هزار دلار نزدیک شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142416" target="_blank">📅 12:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrXCjBPJNHA7-KHLnJnH__7de-sfEetliRXq2qcN5-OOE0Z5ISoNUJx4xp5pvRsp0f1zQPBvBsBoqlM8TX7w9dIJ9CAlRTn5-0AT9cQL6E5o3PqfxPIS0YZJP5XzWlWXiYZaseNX6yTBP1MHccWfx6bcC6xuoMkDOwEPUoihhEzNrnlo3jULeGJvhkos_5eVaPV6dYehBgyIQko700V9CwmH7XzISOu5xYeQ0kkWSeLUR9oMxgs8E_U-SWozA2Xd6XJVg4-BkD4oxRdKXs0oGeglzB3Q6SFqWgWqivEi6iIiEoIrDY4tzj_SZCqScxW0-YuT-m8JVRuD_-aUZxNqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در محدود کردن شدید راه های مهاجرت های قانونی مثل کاری و دانشجویی از همه کشور های دنیا به آمریکاست.
🔴
تنها کسانی که پناهندگیشون قبول میشه، سفیدپوستان آفریقای جنوبی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142415" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ارتش یمن، مواضع نیروهای وفادار به عربستان سعودی را در مأرب با موشک هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142414" target="_blank">📅 12:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d3695c74.mp4?token=SEmBFLHXr30JZNzfVqzoWV0guIe9nkRnonrdIfJhFdavKkYcR8QzHqej7urqUw46IWGwMJmlDzZSGtYgY51OqHdYG8_1xxLw1HtzuktXof4BDiuAQQRanXgkWLyZacEfRT3K-L3gI2XMhoSEP1sjOf1jpuNSWSu2n1Agfr6J1mTuiCgR1ZtBB-nIUY1HqlBMsOzbwfdZ2eGukL0BD5Adw-1D1OLnrLXywMZWmf5l2L0W3ZNB9NYHPzjKGhmIWb4otekBioS9FjJSvdsepq5BtheDAwNEGcK8R5Am7aQ9HDdfKhpqgMhuNdJNyc1oysoG-alN3eRbi78uSJpM7wBh9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d3695c74.mp4?token=SEmBFLHXr30JZNzfVqzoWV0guIe9nkRnonrdIfJhFdavKkYcR8QzHqej7urqUw46IWGwMJmlDzZSGtYgY51OqHdYG8_1xxLw1HtzuktXof4BDiuAQQRanXgkWLyZacEfRT3K-L3gI2XMhoSEP1sjOf1jpuNSWSu2n1Agfr6J1mTuiCgR1ZtBB-nIUY1HqlBMsOzbwfdZ2eGukL0BD5Adw-1D1OLnrLXywMZWmf5l2L0W3ZNB9NYHPzjKGhmIWb4otekBioS9FjJSvdsepq5BtheDAwNEGcK8R5Am7aQ9HDdfKhpqgMhuNdJNyc1oysoG-alN3eRbi78uSJpM7wBh9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: یادداشت تفاهم اسلام‌آباد سند پیروزی بزرگ مردم ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/alonews/142413" target="_blank">📅 12:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eusnWqrHLQQpMD4kO1CFB8ZUGbtBha6yf8KrHMwXXeOX8ZyRsMdAHBxOuvcFTsk9xxGjogFRi4NgWh9ie6nG5Uk_wxQwGez4_5mDKPvRVhQp9C232MOYdaqNILYDiiY7EGZewIQMaGUGl7T_2KLGBHE5B30eAODllXY6290alFWnYCJuZS5pJNzmHTEw4D1yOzvpmJO1q-Wlq7KaTfyT2_kqHhxKXkSjQUKe9PDSiFO_xC-9Z8t2WhDul6MDnsxNOfozGfzU66PUMm6uR9XH4QjBSJMmmRTKAPL3SkRzlemiifm-Y03Ie4NrXxfQw6ZwhBXOc2ctzZgc5NpMfascGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: با رد ترامپ برای تمدید دوباره آتش بس دیگر امیدی برای صلح ایران و آمریکا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/142412" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW3BNj1foNXLf8NfT4FyEIHC88XHblO2pyoP6_N5yiEgZRGf_zWXfek9SD8LVsiV93-5Z9FHYKmXb6hl6SU4sLdJTbIjHjTDG9xXubHSdtkt5T5f3JnDIRb3xFW3BritOWntvBdYv6bhYn6LA-gGskgy_AkmDOJMAnnczA3Hezv5dePP2KuREifNPGImZET9ML169KKynhmsbBivG-AU6qH7FbcMtwJbcFKkcNwxyV71enjPMnpyK_Gc1PMnYblmwUWNk3-xrU4lz5XwJqOJHwNWoF2x9qNnvIhzgJAwYpPSgIyDlzNsrNTNgFjbu-uvH0UX32QOYFKxpjnbibf3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی به شدت حمله به دفتر مسعود بارزانی، نخست‌وزیر منطقه کردستان در اربیل را محکوم کرد و آن را نقض آشکار حاکمیت و تمامیت ارضی عراق توصیف نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/142411" target="_blank">📅 12:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0218bba7.mp4?token=BdxA2tZuDUFO3HiwJyzOwUinW3B8hHvp2B2EERRqpl9PAx5mlWZuB9j2i665cFlXc6Jeu3yO-u1bemmWTkB_NhtIgQr8Sz-goVEWcoLZ-KkSNsXD2b17mVDWKTsLGna0V7gVApKjwjpbaq3e2WN74vQCedGNWYgzfWR801ou5806zAOSe3t-K0XuCqGDg3vLk5ShMU6uJ4afa0s32_kdJIn4H0HhTtOsVe9dQl0hdetC5BsF8d_LmJr14FmutYwMX71yCVZP1MtketDt9aXz7M4jzhTdFQIN-FyvXFdprirK3Hl7Cq8hu62r6AhgQxWSBcgVZK7cXV6c-xLJ7iJqaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0218bba7.mp4?token=BdxA2tZuDUFO3HiwJyzOwUinW3B8hHvp2B2EERRqpl9PAx5mlWZuB9j2i665cFlXc6Jeu3yO-u1bemmWTkB_NhtIgQr8Sz-goVEWcoLZ-KkSNsXD2b17mVDWKTsLGna0V7gVApKjwjpbaq3e2WN74vQCedGNWYgzfWR801ou5806zAOSe3t-K0XuCqGDg3vLk5ShMU6uJ4afa0s32_kdJIn4H0HhTtOsVe9dQl0hdetC5BsF8d_LmJr14FmutYwMX71yCVZP1MtketDt9aXz7M4jzhTdFQIN-FyvXFdprirK3Hl7Cq8hu62r6AhgQxWSBcgVZK7cXV6c-xLJ7iJqaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: در دنیای وحشی حاضر قدرت سخت حرف اول را می زند. در جنگ این موشک های ما بودند که محور قدرت ما بودند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142410" target="_blank">📅 12:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
عراقچی : اسرائیل تمام تلاش خود را برای جلوگیری از دستیابی به توافق‌نامه و عدم اجرای آن به کار بست و این تلاش‌ها همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142409" target="_blank">📅 12:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142407">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS0PyPheJNMc9UbdVvBdhu4Gp5xpe5X1UGl6W4_qFCiXWAyfVi2xTboyT4lD0l_-78KePk03MU1lNnTq7CTlCC4ff2j38o_3CQxbT3MbMPI_IIp_hwIwgUsR9BGdp8ntwjA5dyJnGXE2oAv9KcOhjxh8ptPz__9bkc9rA2dxQscWz3DWp6kAm14RhlqCY-NiuG84NaVnZwQVbSHPVwTccAyU3QSyoI7a-lOgeTBhEyGQmgdE2j-O3gasmFmSXM5fe2MzSVZae5urWj-rhmorPpcL8W0T5JzgMZNxghjqZKfhU7u3cBbTllDE2qjxS7xaFClLa-Z5scUqYUkafLGY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZgYxgS7m6Mge2pwTK8d9mqe0QAA7uCQydj097bcbXhODa-QFH8fiItfsPQn0yo2zXjVoXbD4Rn80kDT1ybs94vx8gsM2XDE1AGMdZ1-Hl1aPNNR4xJjMMEUXXwqkGj2jp4zrNIqGOnXdf-wxzQoQ8qHdeEn3dBpnbxQlnlJ0c9jb5CWCk96llEhPKTnuzwKUtXXaL13StY0Y_gRFnB_J57q79NSWe2bI5rX8LYGKz4fOtgBoGmme2gl1bv75uFH-qwNQG8DwUHuxNB1j-tndbgno-zuitLvAzWZijUkdEyjEnAc860nvYsapw0SZDFbuImAYiEnOShIM7kq_sH_zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی که دیروز در تنگه باب‌المندب مورد هدف قرار گرفت، این اقدام پس از نقض ممنوعیت تردد دریایی بود که توسط ارتش یمن اعمال شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142407" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTOfKyqYiCvoGqPHxx1kvQFUnNlkNEBTk7RsqvrW32pAyzRry1qftcyzSpjZvMx2ETK08fqu7ZO96a7LzidhBOPN8xfJSxUo9y3aTdc4L9hfalDaT5cyBKPX5o5D64oYZj5FlAKnRXYH7bvc0lKU1c0XfMY-aJdtNAfNorgGEijNO9KSMGY16JWWr1SceYAj9euZ5eorBRrcTfJMe6i8_6GPjgDJIiEQj7gnnF3HWDfa4HF2kiNL86PVZMmVmkN9O_0CxXG9LOUKhfbCkQpouG6km-4nWk4RPug171k9MblhkKtNjTrp2oXm62-KHj87_-nVydqVMOm5_eNXtifBlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلنا: هر خانواده باید ماهانه حداقل ۹۰ میلیون تومن درآمد داشته باشن تا بتونن حداقل هزینه‌های زندگی رو بپردازن درحالی که دستمزد اکثر کارگرا به ۴۵ میلیون تومن هم نمیرسه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142406" target="_blank">📅 12:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8c1b68c6.mp4?token=AxsADPbaxlKnrq4Ru_QSPrImuMWgIgJNEOzUJ4UUolae4qsQmpPGcU2dpI-Kip3NZvnQbSZx6MkiiNr6cs37OOJJ-lel3vSiJKVJXMSh5sNuu6ryjYKjpdVVhmlSRfjjrsuWAV8RLWbE7qISBSO_7X1Lm_k3Azp1saYx8STueDsUFH4I5RgNWeBsm6pbePqawcgafwFoy64E05dpmfErWdmZD-O8N4qwL3rGhxIxXSHp20WPnJtvr4NEOiJ1yI-nlLyVERgC21pli91nkbFkIyffm1Yy08-k49UPrjmJeRqQFFGPNM0tAaRVVcUzvm9h5OApJUM7ZsICplcq7Fp256dB-0XPeGQ8-qcX-u8aRsDjUjqa8MpZl_YcCVxppQllk-oSvITQXqbVqonjJ74O7dxtcd_PhG1SQzJs4HNKw8T4lz1JnyYADiqumjRQle385IqOPhl5XJ3uoUfPWwyQxmcgOmjWlk0UC8raGZvCAi6oj0l_bClFGZgQgBi6fOHWxMY4vLYaVf8K1gDWnw2wYBMid2LS9tmX-3zuYOcebzN7gYRHnruyqogkNGrZ5i12M85qyIpFSB8GbnJ884HhI2TPikW7NEbGfexWT7gTdI5DpuSOC8REWDnEvZaQFd73I11jThJEE8IpVrPLJuQ8WkvJP1GeGlYx1s_EQ3qR1w8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8c1b68c6.mp4?token=AxsADPbaxlKnrq4Ru_QSPrImuMWgIgJNEOzUJ4UUolae4qsQmpPGcU2dpI-Kip3NZvnQbSZx6MkiiNr6cs37OOJJ-lel3vSiJKVJXMSh5sNuu6ryjYKjpdVVhmlSRfjjrsuWAV8RLWbE7qISBSO_7X1Lm_k3Azp1saYx8STueDsUFH4I5RgNWeBsm6pbePqawcgafwFoy64E05dpmfErWdmZD-O8N4qwL3rGhxIxXSHp20WPnJtvr4NEOiJ1yI-nlLyVERgC21pli91nkbFkIyffm1Yy08-k49UPrjmJeRqQFFGPNM0tAaRVVcUzvm9h5OApJUM7ZsICplcq7Fp256dB-0XPeGQ8-qcX-u8aRsDjUjqa8MpZl_YcCVxppQllk-oSvITQXqbVqonjJ74O7dxtcd_PhG1SQzJs4HNKw8T4lz1JnyYADiqumjRQle385IqOPhl5XJ3uoUfPWwyQxmcgOmjWlk0UC8raGZvCAi6oj0l_bClFGZgQgBi6fOHWxMY4vLYaVf8K1gDWnw2wYBMid2LS9tmX-3zuYOcebzN7gYRHnruyqogkNGrZ5i12M85qyIpFSB8GbnJ884HhI2TPikW7NEbGfexWT7gTdI5DpuSOC8REWDnEvZaQFd73I11jThJEE8IpVrPLJuQ8WkvJP1GeGlYx1s_EQ3qR1w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
قالیباف: افزایش قیمت بنزین توسط دولت تدبیر حساب‌شده نیست
‏
🔴
کاهش مصرف باید با بیشترین عدالت و کمترین نارضایتی انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142405" target="_blank">📅 12:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
با تائید حکم پژمان جمشیدی از سوی قضات دیوان عالی کشور، رای صادر شده برای اجرا به واحد اجرای احکام صادر شد.
🔴
چندی قبل خانمی جوان از آقای سوپراستار به اتهام تجاوز به عنف شکایت کرده بود که جمشیدی از این اتهام تبرئه شد و به اتهام رابطه نامشروع به تحمل شلاق محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142404" target="_blank">📅 12:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142403">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56de43f40f.mp4?token=Az9R26-n9prFj85cazaZu4frNomxS98EhbpTuUzAF9Q79BaEggzJd08qd9sI4Dd8tJrYDcx3IYE7KkG90cuCUG1xLnHhmNVyMnCzuHJ6FBQiFw72fM7NVxezcOPrH2UPJizttynykIs4W1xCtWyBkbp-m--lIc3fcPk7k7tG6eMxc6ouJG7bmpSWphJbnHYa_OnD918xPWlqovp7_3bsnCuFCFPY8NvC6IaveEZahGK6qARkYuXUeqyZ6tfOuGH7t_xoqIomoUMfj_LGV8GjKgEMzlrz2dVbptOTedP5Yee-70F32tjVrHVJYZAfUuhJQmOWBMYM_pqXSyQ_WSE2M4EfHgPNcLo2xI-hHLGwAtSESFCJrxNovoj_TB9I2TB1_5GNj_iufylpzykMqmQMbU3vQbZuambyiKg-11FsfcKv3qspAl9C04TRJolb1pGclBUu7-mzGgfwVgz5Y1jZDZhuOLNnMXomTSERmqbIwq1EqVzwpGqsWwO7FDU679xQY8Y4Iqlb7E1y4WRUjLmk2ikf0z440nvNy3zLBfo5OUn3tJjnzxuRq-Xiy15cNxa_aV-6YbIg2im1sxDn7-wO9X9OkBY-WoQHNS0fZ3nedkCjQcbekvDj7fg9kPXCM7JWNyuHCMQCy8fncKc5_k0ItmVzVyYwVOnm3XYx28ydz1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56de43f40f.mp4?token=Az9R26-n9prFj85cazaZu4frNomxS98EhbpTuUzAF9Q79BaEggzJd08qd9sI4Dd8tJrYDcx3IYE7KkG90cuCUG1xLnHhmNVyMnCzuHJ6FBQiFw72fM7NVxezcOPrH2UPJizttynykIs4W1xCtWyBkbp-m--lIc3fcPk7k7tG6eMxc6ouJG7bmpSWphJbnHYa_OnD918xPWlqovp7_3bsnCuFCFPY8NvC6IaveEZahGK6qARkYuXUeqyZ6tfOuGH7t_xoqIomoUMfj_LGV8GjKgEMzlrz2dVbptOTedP5Yee-70F32tjVrHVJYZAfUuhJQmOWBMYM_pqXSyQ_WSE2M4EfHgPNcLo2xI-hHLGwAtSESFCJrxNovoj_TB9I2TB1_5GNj_iufylpzykMqmQMbU3vQbZuambyiKg-11FsfcKv3qspAl9C04TRJolb1pGclBUu7-mzGgfwVgz5Y1jZDZhuOLNnMXomTSERmqbIwq1EqVzwpGqsWwO7FDU679xQY8Y4Iqlb7E1y4WRUjLmk2ikf0z440nvNy3zLBfo5OUn3tJjnzxuRq-Xiy15cNxa_aV-6YbIg2im1sxDn7-wO9X9OkBY-WoQHNS0fZ3nedkCjQcbekvDj7fg9kPXCM7JWNyuHCMQCy8fncKc5_k0ItmVzVyYwVOnm3XYx28ydz1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: هر فرد یا دستگاهی که با گفتار، رفتار یا تصمیمات خود، باعث نارضایتی مردم شود خواسته یا ناخواسته در زمین دشمن بازی می کند
🔴
تغییر شیوه‌ کالابرگ  یا افزایش اعتبار آن ضروری است و باید هرچه سریع‌تر اجرایی شود
🔴
مهمترین وظیفه ای که ما مسئولین کشور  خصوصاً مدیران اجرایی دولت بعهده داریم  این است که وسط میدان حل مشکلات اقتصادی و معیشتی مردم باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142403" target="_blank">📅 12:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قالیباف: خیابان، محل میتینگ های انتخاباتی نیست  بلکه میدان‌های اتحاد مقدسی است  که باید هسته‌ سخت ۹۰ میلیونی را در خود جای دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142402" target="_blank">📅 12:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d5daba12.mp4?token=Z520f7nJcsEBtIkEJ0NCpJf190b2M4_JSmOmdFTVgaHc8D6f6Dmo22akCPgilkgld7NR4FuIExRSN6RERxGZkGwxbot5UV00pvoRoXN1lzmH0KSO5sCdS_VpeDpCNuT7L5DUrkbG-VqwB39nLS7qykgoRYjGU9U1TiUeWaBO0yKKppsOh4x4GIvGhYbnFV0bfa-bXu7ClcpZTCj6u9eXB5CQFHoZBwHCtiBjxgqfRVph-cy5TBlKU0cOEPi2-kQBCJIWm1S4ePYVwuSbaH12sDoHdKSRI_XTm7i1-GO9BC-PibDW-zpYOXAvqNU_-dkvZWyQ36ekFoS3w5cBw4VW4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d5daba12.mp4?token=Z520f7nJcsEBtIkEJ0NCpJf190b2M4_JSmOmdFTVgaHc8D6f6Dmo22akCPgilkgld7NR4FuIExRSN6RERxGZkGwxbot5UV00pvoRoXN1lzmH0KSO5sCdS_VpeDpCNuT7L5DUrkbG-VqwB39nLS7qykgoRYjGU9U1TiUeWaBO0yKKppsOh4x4GIvGhYbnFV0bfa-bXu7ClcpZTCj6u9eXB5CQFHoZBwHCtiBjxgqfRVph-cy5TBlKU0cOEPi2-kQBCJIWm1S4ePYVwuSbaH12sDoHdKSRI_XTm7i1-GO9BC-PibDW-zpYOXAvqNU_-dkvZWyQ36ekFoS3w5cBw4VW4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: قبل از رفع محاصره، آزادی اموال بلوکه شده، رفع تحریم  نفت و  پایان تهدید و عملیات نظامی در همه جبهه ها  و دیگر شروط تفاهم نامه، تنگه هرمز باز نخواهد شد
🔴
فرصت بدست آمده از تفاهم نامه در رفع محاصره‌ و آتش‌بس، کمک شایسته‌ای‌ برای‌ افزایش تاب‌آوری اقتصادی و بازسازی توان دفاعی ایران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142401" target="_blank">📅 12:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
قالیباف: تنگه هرمز تا رفع محاصره و تحریم نفت باز نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142400" target="_blank">📅 12:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دختر متهم: من با حمیدرضا رجب زاده در فضای مجازی آشنا شدم، اون مرتب به من تذکر حجاب میداد و می‌گفت درباره مسائل سیاسی حرف نزن.  ‏
🔴
منم رفتم به دوست پسرم گفتم، او هم گفت تو این مداح را به یه بهونه‌ای بکش یک جای خلوت، تا هم او را به قتل برسانیم و هم فیلمش را…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/142399" target="_blank">📅 12:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc84a70aa1.mp4?token=ZSThtrx2M9Y7czxD6C0n_z_pIIp9WIZ5oTJgJmOjjS1VqQe4oECxCf8AN_RFgIJ2P_GU2l7AnBz-Zj9S6uhGojwd4NjgpfZixJH_7Hf0etTbjgakNHLSnfwh9deITN8Z-ydKB1rMntdVHmK-n0x12VP0Cmb-aZv5CfDbQHRp4Af_a1aB7M-Zh7J5Kd_FWuxtBkwkpDD2km9dSYWg7IFQbaZuS9WV_2_wMAVvbej1nBWOaWM9k7oQW-jTFbBUk8oRRRjg6PPs1d65OYKDoCZVNARtTUxAOOJwzrZPW5WzHlthRRdEhMpNt_UyYz-OIEPEs51sCFFtotaJS59VxDrVBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc84a70aa1.mp4?token=ZSThtrx2M9Y7czxD6C0n_z_pIIp9WIZ5oTJgJmOjjS1VqQe4oECxCf8AN_RFgIJ2P_GU2l7AnBz-Zj9S6uhGojwd4NjgpfZixJH_7Hf0etTbjgakNHLSnfwh9deITN8Z-ydKB1rMntdVHmK-n0x12VP0Cmb-aZv5CfDbQHRp4Af_a1aB7M-Zh7J5Kd_FWuxtBkwkpDD2km9dSYWg7IFQbaZuS9WV_2_wMAVvbej1nBWOaWM9k7oQW-jTFbBUk8oRRRjg6PPs1d65OYKDoCZVNARtTUxAOOJwzrZPW5WzHlthRRdEhMpNt_UyYz-OIEPEs51sCFFtotaJS59VxDrVBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که پایگاه هوایی سوری که اسرائیل شب گذشته مورد هدف قرار داد، در حال بازسازی بود تا برای بهره‌برداری آماده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/142398" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سپهوند، نماینده مجلس: برای فصل سرما قطعی برق کمتر خواهد بود اما قطعی گاز بیشتر خواهد شد به دلیل جنگ و تبعاتی که داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142397" target="_blank">📅 11:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f40a8df.mp4?token=MNW4Z0FI9iPrP7Q0PvipzaUyx_Jq3uYtNNQdZMXeq8HJhYUQmiUo_Zgg7DQonpWh0W0T8e4fayZ3gJiZhTsSVg_vcE2Mg2FvF65HiYRpne7xyrIHSlwnr-E0D_ezbpfb34m1mZkv7-Ppw8b-P7OOdHbOUQLNr5Eo0SOqH0qpLSuVUvvq2qhtemS1KfCM564Vzi_9lkM0rtkrctGJphnQVUNemI7zvGpGGqfFAIuK7RwleJB21uN36PiTz5z3DuQHSyXQTJ97h_3iNEkARvbuM2MrtGlFJkH5_NVNeGS20sFeXQlKu96cnHnEc-9J9Sa4Qw251I48GEzhWeuOQETrnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f40a8df.mp4?token=MNW4Z0FI9iPrP7Q0PvipzaUyx_Jq3uYtNNQdZMXeq8HJhYUQmiUo_Zgg7DQonpWh0W0T8e4fayZ3gJiZhTsSVg_vcE2Mg2FvF65HiYRpne7xyrIHSlwnr-E0D_ezbpfb34m1mZkv7-Ppw8b-P7OOdHbOUQLNr5Eo0SOqH0qpLSuVUvvq2qhtemS1KfCM564Vzi_9lkM0rtkrctGJphnQVUNemI7zvGpGGqfFAIuK7RwleJB21uN36PiTz5z3DuQHSyXQTJ97h_3iNEkARvbuM2MrtGlFJkH5_NVNeGS20sFeXQlKu96cnHnEc-9J9Sa4Qw251I48GEzhWeuOQETrnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏
اولین تصویر از سارقان گردنبند نیم میلیارد در شمال تهران
🔴
متهم به دلیل مقاومت و فرار حین دستگیری با شلیک گلوله پلیس از پا افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142395" target="_blank">📅 11:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF9dA2oLvS0JbPSVEwI8b1fdgFTRB8ptCSOtheJq-4aKZ4fKzqCUr5K04qRihO6op08LpKKnOhw43FHLAUcV4Gck7AQsDfzEigJTs-R4GmtMoaCejfPDw372Dc23mJQrm_k2uN3eU2mkmUQCSlrKgp879PG7JXgJljPdRLuTyjWrN7qXxpLLXme8X_0QMn9JDYCifUC0LK-ZJZacANTKdiTq5LV47SsNf0apLRVPGN_87Jbbi3IqK4AIdxxSXFg4F0WdkniYQ1UyFps4GnE3G7qrIsYlWzinSKhik97sYQihvX49R4R5JsjfM_rrS9b03iuus9FtFJv_yF33_29Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بزودی اسم فرودگاه مهرآباد به فرودگاه آیت الله خامنه‌ای تغییر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142394" target="_blank">📅 11:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس: تاکنون برنامه‌ای برای افزایش قیمت بنزین ارائه نشده است
🔴
برنامه دولت درباره بنزین، توسعه روش غیرقیمتی است/دولت در حال بحث و بررسی برای تعیین نرخ چهارم بنزین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142393" target="_blank">📅 11:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
روزنامه لوموند فرانسه: خاورمیانه همواره آزمونی واقعی برای عملکرد روسای جمهور آمریکا بوده و در مورد ترامپ، این منطقه ناکارآمدی او را آشکار کرده
🔴
ترامپ در کمتر از دو سال کارنامه‌ای مملو از شکست بر جای گذاشته
🔴
جنگ علیه ایران، به عقب‌نشینی واشنگتن منجر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142392" target="_blank">📅 11:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش داد دو شرکت غول‌پیکر کشتیرانی چین، ارسال نفت‌کش‌های خود از مسیر تنگه هرمز و تنگه باب‌المندب را متوقف کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142391" target="_blank">📅 11:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f69R7iYt8AtV7dhKMp11qzj56XoAMaX8r3iBu4XkTSNZ9x0c_viv_lfeIy8IfX0SjNAw_yLPV_hjn_zq7auEgqkkbZ931sr_hKb6n__T83745SZ_cx0Fs21AMpjbonImGNbMdp7ffmAetQjaJEiSEWKxHDkv-TWsFe-Xnq7dqLDq1FCz7H7YGITFwk00rP3TLEWFM1TzqLLYjiCYo6FP-wvtaj7ARIamwCEcwTpI6z_Kvl9qmtQE7PhucuhTaSI0iicVyyZZYStWBt491HbYix1kZFCzGv-KAvnOVcff0diUvwrI44Nf3vbnBGS4DHW7t77PMB9UmEBUJQGYpEHTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز قبل حدود ۲۰۰ زن و مرد با وضعیتی زننده در یک پارتی مختلط در شهرستان شهریار تهران با حضور بازیگران نوید محمدزاده و یسنا میر طهماسب دستگیر شدند.
🔴
آقای محمدزاده یک روز پس این اتفاق، تصویری با لباس فلسطین منتشر کرده تا خایمالی کرده و قضیه حل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142390" target="_blank">📅 11:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142389">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رئیس کل گمرک: ثبت سفارش واردات گوشی همراه آغاز شده است، مجوزهای لازم از طرف وزارت صمت صادر شده و سهمیه نیز اختصاص یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142389" target="_blank">📅 11:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142388">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فووری/خبر مهم درباره ابر تورم
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142388" target="_blank">📅 11:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142387">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bedf2cd22.mp4?token=NxFjr2KjmyJZeilLeMlOPxSWPZ27H60TfMk1KNPizJ8yCLRkAnxaWpLOip0FhhOSCEs7vwdGR17xLLECC1euABqIrDIP90suyp_2as58dyaKkNE2JJQE3PyO-K3ufAPqLyuymdFGIRFo1kITsykfxIrdzf5zT13QAJTQGGmJLIbhTX2LmmV2JYNI5G3qexUcN6bzdQXJ0UOkt5sCn6eUTizhx07_EEPP4L1KhfZJ-Tuz5j9_fw_kbUuY9vNq3yfW2WQ4_EvGZhWTU4mnKPGMGiAAS4DIZDCsQMAw7wlwBQgwGolrW0Y4F9lfn-l-aeGm0Ky9YMPrlJ8B4h07GmCkm3WaHzy8W1fUe-_MoBwKkvKka5FFifhu6narwvm7GoIK0Ytx49u5kBS920IZjoI8Zsg30lVzlTKKGEtdMKFaWz7f3dK8qVwUOnyEtnYOplWQ1tQUceqtURDdAWu3UcK76ZHz53JcapIDcMTwUASwdqLaGRxHq-B5lrse04NOqz2MQ7S8P3MqyuSCWwunPK4A3T2BXyzoAgrQpUWnhhyRtGahXQdoHr6tXZglYmqw3arE9wY96o4XbR19zNjZY5da7hvz3psczl3_v7AqsnkTA5iCOw-6NN4x_SGpR2Deh_caibJ0T0mKkgy33wbYO5I0DZKZCFE7vWzeRLfgPfz-CEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bedf2cd22.mp4?token=NxFjr2KjmyJZeilLeMlOPxSWPZ27H60TfMk1KNPizJ8yCLRkAnxaWpLOip0FhhOSCEs7vwdGR17xLLECC1euABqIrDIP90suyp_2as58dyaKkNE2JJQE3PyO-K3ufAPqLyuymdFGIRFo1kITsykfxIrdzf5zT13QAJTQGGmJLIbhTX2LmmV2JYNI5G3qexUcN6bzdQXJ0UOkt5sCn6eUTizhx07_EEPP4L1KhfZJ-Tuz5j9_fw_kbUuY9vNq3yfW2WQ4_EvGZhWTU4mnKPGMGiAAS4DIZDCsQMAw7wlwBQgwGolrW0Y4F9lfn-l-aeGm0Ky9YMPrlJ8B4h07GmCkm3WaHzy8W1fUe-_MoBwKkvKka5FFifhu6narwvm7GoIK0Ytx49u5kBS920IZjoI8Zsg30lVzlTKKGEtdMKFaWz7f3dK8qVwUOnyEtnYOplWQ1tQUceqtURDdAWu3UcK76ZHz53JcapIDcMTwUASwdqLaGRxHq-B5lrse04NOqz2MQ7S8P3MqyuSCWwunPK4A3T2BXyzoAgrQpUWnhhyRtGahXQdoHr6tXZglYmqw3arE9wY96o4XbR19zNjZY5da7hvz3psczl3_v7AqsnkTA5iCOw-6NN4x_SGpR2Deh_caibJ0T0mKkgy33wbYO5I0DZKZCFE7vWzeRLfgPfz-CEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تردد خودرو های خارجی با پلاک گذر موقت ۱۰ ساله
🔴
رئیس پلیس راهور فراجا: ۲ شهر دیگر به مناظق آزاد اضافه شده و مجوز تردد خودرو های مناطق آزاد با گذر موقت ۲ ساله و امکان تمدید تا ۱۰ سال فراهم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142387" target="_blank">📅 11:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142386">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
استفن استپچینسکی خبرنگار بلومبرگ:
امارات در حال انتقال محموله‌های LNG از طریق تنگه هرمز است و همان استراتژی‌ای را که برای نفت به کار گرفته، در مورد گاز طبیعی مایع نیز دنبال می‌کند.
🔴
دو نفتکش حامل LNG در نزدیکی صحار عمان و خارج از تنگه هرمز در حال انجام عملیات انتقال کشتی‌به‌کشتی هستند.
🔴
یکی از این کشتی‌ها به نام Mraweh، محموله LNG خود را از تأسیسات جزیره داس در خلیج فارس بارگیری کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142386" target="_blank">📅 11:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142385">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6527865aa3.mp4?token=L0aFD6JJ00UQEsf74cTh8mPPrpRlWFHWAOuxn227vEAEPAaD3KbNYH4JjlRuOzO1B9PW5jqvaoSgH1WodOwyTyhexsSeSk-bRzPi8QbpXxM7A-8Uq6SFAiM22KK4_2MLrkITQ2JK-R_kYd_aUFo_0Of8I9uknr7owBJJD7LBSGUpUYSTOEy5HKD5v1DPuFiIuqME8qRkQdO6SUouarWm1DoXLDjETndZXLS_BvG-l2wRjM_Q56hjew6Cs5NF_mmeYOQYUW54L3Fpfj3POqSwVTPsMsvqfEUlD6tVeX1fr7WyH45ntH2y4qf1hvi6Uu2UgA4r8gJi7q-9_1tvjC3a7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6527865aa3.mp4?token=L0aFD6JJ00UQEsf74cTh8mPPrpRlWFHWAOuxn227vEAEPAaD3KbNYH4JjlRuOzO1B9PW5jqvaoSgH1WodOwyTyhexsSeSk-bRzPi8QbpXxM7A-8Uq6SFAiM22KK4_2MLrkITQ2JK-R_kYd_aUFo_0Of8I9uknr7owBJJD7LBSGUpUYSTOEy5HKD5v1DPuFiIuqME8qRkQdO6SUouarWm1DoXLDjETndZXLS_BvG-l2wRjM_Q56hjew6Cs5NF_mmeYOQYUW54L3Fpfj3POqSwVTPsMsvqfEUlD6tVeX1fr7WyH45ntH2y4qf1hvi6Uu2UgA4r8gJi7q-9_1tvjC3a7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عقب‌نشینی دریای مازندران باعث شده ساحل گل شمال چالوس که روزگاری مردم جمع میشدن ماهیگیری میکردن توی ۵ سال به این روز افتاده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142385" target="_blank">📅 11:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142384">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b9ca9043.mp4?token=WPL9ma3gBmOr0aAzFq9xTHjiEhhFljqwSMlm1S9l80bOZdwpyfF6NXXHMM_EUhfeNrK55hCmLWbOl4TVL8O5fGVy0yZyn9yP9GJRKOTFahDUp3jnJBCfNEYT52LO1qXE4HKI37k_7auLdP6g0HDZJj7HnNzO1qkyxScshZoCFKhxyqr4EhCwWEce0lOr8mVtX5CWn1eKGxbUphqaYMaqlK11kxd1oV_mXqGrfdpWRFGResNcJBwp9f9fPF-EpYHUX3asf_WQbUb5zAyuf1bduwFbRdVXY4I_Hjjv3mwX4r1yUHUp6jUABiUxguJDKB0JuFfBUb7VZ7svTaTT0iRoSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b9ca9043.mp4?token=WPL9ma3gBmOr0aAzFq9xTHjiEhhFljqwSMlm1S9l80bOZdwpyfF6NXXHMM_EUhfeNrK55hCmLWbOl4TVL8O5fGVy0yZyn9yP9GJRKOTFahDUp3jnJBCfNEYT52LO1qXE4HKI37k_7auLdP6g0HDZJj7HnNzO1qkyxScshZoCFKhxyqr4EhCwWEce0lOr8mVtX5CWn1eKGxbUphqaYMaqlK11kxd1oV_mXqGrfdpWRFGResNcJBwp9f9fPF-EpYHUX3asf_WQbUb5zAyuf1bduwFbRdVXY4I_Hjjv3mwX4r1yUHUp6jUABiUxguJDKB0JuFfBUb7VZ7svTaTT0iRoSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین تصویر از محصول جذاب اپل: ایرپاد دوربین‌دار
🔴
کدها و ویدیوی فاش‌شده در نسخه آزمایشی macOS Tahoe 26.7 نشان می‌دهد اپل در حال آماده‌سازی ایرپادی مجهز به دوربین است؛ محصولی که می‌تواند محیط اطراف کاربر را ببیند و اطلاعات را به Visual Intelligence منتقل کند.
🔴
در ویدیوی منتشرشده، ایرپاد عنوان یک کتاب را تشخیص می‌دهد و  نیز قادر است به پرسش‌های کاربر درباره محیط پاسخ دهد یا رویدادها را ثبت کند.
🔴
این محصول با نام رمز B790 شناخته می‌شود و احتمال دارد در رویداد شهریور اپل، کنار آیفون ۱۸ پرو و آیفون تاشدنی رونمایی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142384" target="_blank">📅 11:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142383">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
حمله پهپادی یمن(حوثی ها) به پالایشگاه آرامکو عربستان در جیزان
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142383" target="_blank">📅 10:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دود از فرودگاه نظامی ابوذهور در حومه ادلب، سوریه، به هوا برده می‌شود، در نتیجه بمباران‌های اسرائیل که به باند فرودگاه و سایر نقاط داخل آن وارد شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142382" target="_blank">📅 10:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
العربیه به نقل از منابع ارشد کرد عراقی مدعی شده نیچروان بارزانی، رئیس اقلیم کردستان، طی دو ماه گذشته دو بار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه، دیدار کرده است.
🔴
بر اساس این گزارش، این دیدارها در چارچوب میانجی‌گری محرمانه میان تهران و واشنگتن انجام شده و بارزانی پیام‌هایی را میان دو طرف منتقل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142381" target="_blank">📅 10:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رکورد تاریخی کانال ۵.۹ میلیون واحدی شاخص بورس شکسته شد
🔴
شاخص کل بورس تهران با رشد ۲۱۱۰ واحدی به رقم ۵ میلیون و ۹۰۰ هزار واحد دست یافت. این در حالیست که شاخص هم وزن ۷۸۶۳ واحد مثبت شده که نشان می‌دهد مبادلات سهام نمادهای کوچکتر از نمادهای شاخص‌ساز جلو زده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142380" target="_blank">📅 10:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
عارف: موضوع تنگه هرمز به زودی حل خواهد شد
🔴
عارف، معاون اول رئیس جمهور: تنگه هرمز جایی است که از سالیان پیش متعلق به ما بوده است.
🔴
حال طرف مقابل در ادعایی مضحک و مسخره نسبت به تنگه هرمز ادعای مالکیت می‌کند.
🔴
اگر ما بگوییم فلان خلیج آمریکا برای ایران است، واکنش تحلیلگران آمریکایی چه خواهد بود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142379" target="_blank">📅 10:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ادارات بوشهر چهارشنبه تعطیل شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142378" target="_blank">📅 10:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142377">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e283d8ada.mp4?token=CdnRkt1SU7-DNiBzJHwe6bLDkYlIGhXoASS5-8BO2Gqy9ENtJGlp9ymK2r7LXvZOk6E-BSPKq6RXViV6cxPh3H5mSZlUd8pGMxlfr0gYwECu2CbMvJaS99oE3liYtKj5EA07z8zBNrQNYmdfb3tK8EBUmmcEMYnAxMtI9oKGvqHYvSX2rTlatEVWh5awiFXb8WZiGBwcJM5OUwS0_uPtqFdVWg78-Bx58Tu5PYNzvX-Cc0OPgJ2IbqxOWhV6TY51dFgssB_azzCV7tDlabIy_lz7qE5ioBplQgXbQnCTWrIvFJWJ3mN4BJAffmP4lzeM6X3ZjnYvrEomX-6MlgNetQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e283d8ada.mp4?token=CdnRkt1SU7-DNiBzJHwe6bLDkYlIGhXoASS5-8BO2Gqy9ENtJGlp9ymK2r7LXvZOk6E-BSPKq6RXViV6cxPh3H5mSZlUd8pGMxlfr0gYwECu2CbMvJaS99oE3liYtKj5EA07z8zBNrQNYmdfb3tK8EBUmmcEMYnAxMtI9oKGvqHYvSX2rTlatEVWh5awiFXb8WZiGBwcJM5OUwS0_uPtqFdVWg78-Bx58Tu5PYNzvX-Cc0OPgJ2IbqxOWhV6TY51dFgssB_azzCV7tDlabIy_lz7qE5ioBplQgXbQnCTWrIvFJWJ3mN4BJAffmP4lzeM6X3ZjnYvrEomX-6MlgNetQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تفاوت وحشتناک قیمت ها در ۱ سال
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142377" target="_blank">📅 10:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142376">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
مصر و کویت خواستار بازگشت ایران و آمریکا به یادداشت تفاهم شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142376" target="_blank">📅 10:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142373">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2oNI2ykBTaFEH__omU81_a1G-sh04OEHdZkOfbg-GXJa527KhE2qRPkWcbF6JEThcnKGsnQ8VkUoP0VaOJgH_ajez5Gy96mq_6x94RpH5wLxvf5FnCaoXSGIky1h7d3eOU0xqh2TtqLebHHldaI59JEetclm3HuE2qPAdU0GQpdHQ92PGpXgOOEMI4_0vTC3DuPSIXJ0BetJ-b1uFw9z2tgs3dusG5Gq1wdgNLpNxi7DWKPtzNi93EXXdmcvLS70F8-T-2hCMO9O83yZBQeVQd-MpGep1hkIxHhSC9eWeoga8k1dQmezZxPp0nQR3f1ZlCb-p0jTOHTXViBj3dn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-PYhnUT6JfXh2UHsNqoEaEzonTKyYMSRMn2o7G71zhF74JKE4qkQJipGYh-uzTBu4IYNFtN7YFRGzUBPO8WfGtoWoFDaqN1Mil9nnUpX9htsD2QjHXqiepPNMwuvDNHIy6HcCDwz40AvmOBE8aoUOub16O5Ynp5vUzrlCcDdQV6YbXvxyjqPLOEqHHjtBgC2NBPP_YwcnA2Pwl-FL5GwpqYHBhvrQw3ANSj54NnHQbyKM3IC9PUPJiH-E3ReO8WGaC2ReZMcIaqdeG0MQvqixj3kIZF-cNF6mhJeAdxxfyqrrkMb9BqSnGkZwsZHAGbVf7SKvU6X5cYHjsEtHLcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMVi2HuAahEkMVAjZ5yZvIMXCK3s-q8-taB-PRJ5SLiV2vLpYaHjlJwwkC8nsrncD12NW3QuR0_JMWkrF2xza89ZkmxnlHUg2lUm80Z9y9R699Re8Rn6JLRWnB5KfC1JDTfMWt_mBIeGpcj69gA-KyOjP0lpg468OCthShJkpGxpvQ3QeGYleMjtpwdy1WB9kVX3ipJM1isbAmi0xX4XOfJEZ7HzZJ_qI9v9G4ykkAU1nNGXtyWv_muWpoXuHJxbpEfKYbKJL5XgsVn6RTR1bDcIyDy3-fYUf86FGFbLDcwZM3A-VGB2fj73nZFWoJ1oVMP5ZWPuVA1vslqSyAZGKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویرى از محل آتش‌سوزی انبار سوخت در سلیمانیه عراق پس از چهار ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142373" target="_blank">📅 09:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798fcd12a.mp4?token=Wl4uluB5IjvJUniJLHm6nPrduf4i2hnZaUrsquQiovS8F1dNtMtwn9zx5CO_DVhNnBDyNQugrab_zFRKKNrY4Qz_Tjq4Rq_zRqnxE3j22EkDIU-AZ57Z6JPCnxvBRDsGbf4m75IuGa83IOWdDTZT1yKk8ZX9CEHbiWAyTLSQVZDpLRw6e9O5vDWVbm8KSIWzxXd30rLAOF6_mWPncD_5VoF0kj-bBn2BDV1Rwu5tJbxtBMxCN4eGoCt9l2V31zH160Am_Mzid-GNdDIjkv5lPgNJSbwqUHimr6QjJd2zgrj2wSkv7nSkBeIZP-odKc1Gu8gwdKatUwsRwpr7wfSulQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798fcd12a.mp4?token=Wl4uluB5IjvJUniJLHm6nPrduf4i2hnZaUrsquQiovS8F1dNtMtwn9zx5CO_DVhNnBDyNQugrab_zFRKKNrY4Qz_Tjq4Rq_zRqnxE3j22EkDIU-AZ57Z6JPCnxvBRDsGbf4m75IuGa83IOWdDTZT1yKk8ZX9CEHbiWAyTLSQVZDpLRw6e9O5vDWVbm8KSIWzxXd30rLAOF6_mWPncD_5VoF0kj-bBn2BDV1Rwu5tJbxtBMxCN4eGoCt9l2V31zH160Am_Mzid-GNdDIjkv5lPgNJSbwqUHimr6QjJd2zgrj2wSkv7nSkBeIZP-odKc1Gu8gwdKatUwsRwpr7wfSulQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی نشان می‌دهد که ارتش اسرائیل در نزدیکی شهرهای بنی حیان و تلوزه در منطقه مرجیون یک انفجار بزرگ انجام داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142372" target="_blank">📅 09:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سازمان ملل: یمن در معرض خطر بازگشت به «جنگ تمام عیار» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142371" target="_blank">📅 09:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: اگر گزارش‌های حمله به ادلب صحت داشته باشد، نشان‌دهنده تشدید قابل‌توجه تنش میان اسرائیل و اردوغان است.
🔴
ممکن است این نخستین باری باشد که اسرائیل مستقیماً برای محدود کردن فعالیت نظامی ترکیه در سوریه از زور استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142370" target="_blank">📅 09:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142369">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845ec2b32b.mp4?token=M4Y06afAbRsCm12OZxiPbcGSYkAXC3Bq2ssNexyAIlVmjraacmMMh-JeY-_xh6jDCUzC9ApS7aSOdkaEV0L8cxp_N4oEDaAGIbikClTs9A8_3M0DJwhTmbUak-aRDPcITSkyj2-MQWlrrcHL4c47xZTNaasl93_ptVZyyFGoniO7HDhbfAVl4mqM83ppfhSMOJ_yPjudVbscJmNnty4zP3rq3m8RT5FjNALE8_4fjXjKV2OcpAPu4jgU_2DbEu_2OlHp8DCz93PG_sRW3sg0enIfhKtr3Hol4Qmpkr7L1fSJWn0kZjnOVRtW9Di3Qqundc7ccZBibIfU6T8s_qlFBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845ec2b32b.mp4?token=M4Y06afAbRsCm12OZxiPbcGSYkAXC3Bq2ssNexyAIlVmjraacmMMh-JeY-_xh6jDCUzC9ApS7aSOdkaEV0L8cxp_N4oEDaAGIbikClTs9A8_3M0DJwhTmbUak-aRDPcITSkyj2-MQWlrrcHL4c47xZTNaasl93_ptVZyyFGoniO7HDhbfAVl4mqM83ppfhSMOJ_yPjudVbscJmNnty4zP3rq3m8RT5FjNALE8_4fjXjKV2OcpAPu4jgU_2DbEu_2OlHp8DCz93PG_sRW3sg0enIfhKtr3Hol4Qmpkr7L1fSJWn0kZjnOVRtW9Di3Qqundc7ccZBibIfU6T8s_qlFBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود از فرودگاه نظامی ابوذهور در حومه ادلب، سوریه، به هوا برده می‌شود، در نتیجه بمباران‌های اسرائیل که به باند فرودگاه و سایر نقاط داخل آن وارد شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142369" target="_blank">📅 09:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142368">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بلومبرگ:  با اعلام عدم تمایل دونالد ترامپ، رئیس جمهور آمریکا به تمدید توافق رو به پایان با ایران و تشدید تنش‌ها در تنگه هرمز، چشم‌انداز صلح در خاورمیانه با رکود تازه‌ای مواجه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142368" target="_blank">📅 09:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142367">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoSjUI8rMk-hCiwnp-wxH1d66dtxcmaRPw4TaK-O5PujMBrPD7xVqDaY5zwQUWY0SToiJJ0UikTxMxXwGobklmW6rCLVW6OQ_a0oCn3Tfx01jzFYBxcZ2muZ4r7LINxrBlhQrWWBrFnj86QFD7WqJj9xZ0MWiX520U840CL8wpwwcrSK1b2QpgMKEfRCZI5ZmNlXlgfZbh-ebfXu-CEq2Won4T5tBDposcmrspzaGVLJWhBEyK6QHiJrn1j0_Hlfi6UiKtAey0JjXJ5bXMpuTwdAOMBWvAav9Y0Bu9CV3UXuUORoWHdE2VDhu9PAn8zknHHMX4Gj1gS3HM3J-4TM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلزله ۵.۷ ریشتری در سواحل مکزیک
🔴
زمین‌لرزه‌ای به بزرگی  ۵.۷ ریشتر در نزدیکی سواحل ایالت چیاپاس در جنوب مکزیک رخ داد. این زمین‌لرزه در عمق حدود ۱۰ کیلومتری زمین ثبت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142367" target="_blank">📅 09:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142366">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
عراقچی:با اقتدار جنگیدیم و با اقتدار هم مذاکره کردیم
🔴
بارها سفرای کشورهای مختلف به من گفتند که از مجموع بندهای تفاهم‌ نامه، تقریباً همه آن‌ها به نفع ایران بوده و تنها بخش کوچکی به نفع طرف مقابل است؛ علت نقض تفاهم‌نامه از سوی آمریکا هم همین بود
🔴
وقتی می‌گوییم دیپلماسی را بردیم، یعنی ایران پیروز شده
🔴
دستاوردهای قدرت توسط دیپلماسی تثبیت می‌شوند و گل قدرت را دیپلماسی می‌چیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142366" target="_blank">📅 09:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142365">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عراقچی: دیپلماسی و میدان در هماهنگی و همبستگی با یکدیگر حرکت می‌کنند
🔴
دیپلماسی با اتکا به قدرت دفاعی و نظامی کشور، دستاوردهای میدان را تثبیت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142365" target="_blank">📅 09:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142364">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: ترامپ می‌گوید ایران به توافق مورد نظر او دست نخواهد یافت و تهدید به بمباران عمان کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/142364" target="_blank">📅 08:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142363">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y52hmCRA_k1zBgGoSTIHgWK8HvKM_ol_1kpnddiv0S1WYjm9JqY_mH6TVJPL--ccEVwuEH5WrhAJm2re_XvAH3NWDnnNioNE4x8w90QqCWi4SRP2eifkGIZM11ENjMOb-6I2vcJdXvWTeZnN3g6IJmJ-gsM1wZ9WIri59KBWbWQVQU3T1By43v2Xednvu_SE2PFKHUX4zfIXKR5dIDtbpPN8ZZ3oJexN6B1uQ3fM7uDWfO6okCZk-BZcgHINZ9bWmunow9Wa1ehjT3kP5LvPMoJezy2MYWas38qWlmtSoeWWRhxPOe3iJkWiMFlNXpP7O_Uy0YmIfv_N2ljQHkoAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارس: هدیۀ آمریکایی‌ها به ایران در جنگ ۴۰ روزه!
🔴
در میان بقایای جنگندۀ F-15 آمریکایی سرنگون‌شده در جنگ تحمیلی ۴۰ روزه، یک قبضه سلاح ویژۀ GAU-5A به‌دست آمده است.
🔴
آمریکا این سلاح را برای یکی از سخت‌ترین لحظات زندگی خلبانانش طراحی کرده است؛ لحظه‌ای که جنگنده از دست رفته و خلبان باید پس از اجکت(خروج اضطراری)، در منطقۀ دشمن برای زنده ماندن منتظر رسیدن نیروهای نجات بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142363" target="_blank">📅 08:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز با استناد به داده‌های ردیابی دریایی اعلام کرد: ۶ کشتی باری روز دوشنبه از تنگه هرمز عبور کردند، ۳ کشتی خلیج فارس را ترک کردند و ۳ کشتی دیگر به سمت آن حرکت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/142362" target="_blank">📅 08:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx0CxirM2hcn30rfMJbYrxi7rc6kkehcDiLjkMf1ql14wmHVAQ52cy-U7XJ9zzBTYNp06qai4Wdlbc5lB2s_Cx5P7CRnvW9hhV3xiKos2pGFgCqbRTPBYa1CTCMRm5440kSJVRUZBGsiptSUqp-arSbLvFORyxQjH7vNPXcZscn-bBVDmJGfgfceS5aooC4euz1-5Zeb0-Fke12lX2-YMUCXnVePvtuGO-QCQcRJ-W0hALzOIP8faQLpyKQTfTCJVdjOCZYq3-VdTemiakrPWyFBgZdOReuNw7k_xK35DdI_ZMGg8Lx-oxCMHePyReftW6x3XSHTc6Pw4ul4RYFhUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: مقامات آمریکایی می‌گویند عمان در مذاکرات با ایران برای افزایش عبور کشتی‌های تجاری از تنگه هرمز پیشرفت کرده است
🔴
این پیشرفت می‌تواند فشار بر بازار جهانی انرژی و قیمت بنزین آمریکا را کاهش دهد. با این حال، برخی مقامات ارشد آمریکایی مسقط را متهم می‌کنند که به تهران گرایش دارد و نگرانند توافق ایران-عمان کنترل ایران بر تنگه را تقویت کند.
🔴
ترامپ خواهان توافقی است که تنگه هرمز را کاملاً باز کند، نه توافقی که کنترل بیشتر عبور تجاری را به تهران بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/142361" target="_blank">📅 08:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jrsar5iEMHa5aMIYEQmuq8rh4CpvGV0B7riZx6W6PwLgi61E5lPU4pGOtSVnWKyFXcQ1HALhTJcH4AEKuBS_EBns5EX6cfkqwUC7bjg-TR9rtJHICan14XSOh2dQeBqX8Tabs2rdubfX9I-CFvsCI-sEP9fWp8gP4-IuLsLKQSW_hm9nynj0QHLn58y1sjaSX3dFgd1U5kHt43HEIcuIlwswUfkmAObITLadZFGHCd6L9OFyDprtP_X5IT1DneVud2RXtsZvoo_GIaMfzk7bUNkU3r76rPgB0J9UP17whCzq-FhzPxiPXA_xBcrjnQ2baPeOfTBC2CigS78RgWGdGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا از اصابت یک پرتابه ناشناس به یک کشتی در تنگه هرمز خبر داد
🔴
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی از یک حادثه در
تنگه هرمز
دریافت کرده است.
🔴
بر اساس این گزارش، افسر امنیتی شرکت مالک کشتی اعلام کرده که این شناور هنگام عبور از تنگه هرمز، بر اثر اصابت یک پرتابه ناشناس هدف قرار گرفته است. این حادثه به
اتاق موتور کشتی آسیب رسانده
و به کشته شدن یکی از خدمه منجر شده است.
🔴
در ادامه این بیانیه آمده است که سایر خدمه در حال حاضر با کمک
گارد ساحلی عمان
در حال دریافت کمک هستند و تاکنون
هیچ‌گونه آلودگی زیست‌محیطی
گزارش نشده است.
🔴
سازمان عملیات تجارت دریایی بریتانیا همچنین اعلام کرد که مقامات در حال بررسی این حادثه هستند و به تمامی شناورها توصیه کرده است با احتیاط از منطقه عبور کرده و هرگونه فعالیت مشکوک را گزارش دهند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/142360" target="_blank">📅 08:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بلومبرگ: ترامپ و مارک کارنی، نخست‌وزیر کانادا، دوشنبه شب پس از چند روز مذاکرات تجاری بین دو کشور تلفنی گفتگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142359" target="_blank">📅 08:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز: ارزش دلاری حداقل دستمزد در ایران از مارس تاکنون کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/142358" target="_blank">📅 08:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: درحال خفه کردن تدریجی ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/142357" target="_blank">📅 07:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خیانت بزرگ چین و روسیه به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/142356" target="_blank">📅 07:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjJVW4YiUoxB3zLrWx44NkFJpOgbwzWxIK_1MeUMBuZo7rRH7QFIw451poXote-JDF0_qFQLkKM7dLhCfrC5eGuauDgLK-uEUcPjkFyNe5fYKbKm4ZYT9lpIYWLZXsnToE3CWkf1iZFIYyUsIqYAhI4x687OUbw9NYw8LiJss3M0h4GVJ2VBDpejOiSsBWcBQpXE6xSEkihhsHwlAmmdIv7XZ6f0yOrXHv6pUbjuUs4I8QoX1BBhjiyOaMuto0lb025492yQZVx3_nHXQ2j3bWg08FhaF2P-bqAC183gb1oRA5z648ipDU4adWzLD_qFPCNgoZIDk7xLF79dzLPClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ترامپ می‌گوید ایران به توافق مورد نظر او دست نخواهد یافت و تهدید به بمباران عمان کرد
دونالد ترامپ، رئیس‌جمهور ایالات متحده، گفت که احتمال پذیرش توافقی که واشنگتن آن را برای پایان جنگ ضروری می‌داند، از سوی ایران کم است و از تهران خواست تسلیم شود. او مجدداً تأکید کرد که هدف ایالات متحده جلوگیری از دستیابی ایران به سلاح هسته‌ای است. این اظهارات در حالی مطرح شد که مهلت ۶۰ روزه توافق ژوئن ایالات متحده و ایران بدون رسیدن به توافقی نهایی به پایان رسید، در حالی که تنگه هرمز همچنان بسته است و مذاکرات در بن‌بست باقی مانده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/142353" target="_blank">📅 01:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
قالیباف چهارشنبه به عراق میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/142352" target="_blank">📅 01:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دونالد ترامپ اعلام کرد که کیم جونگ اون، رهبر کره شمالی، به پیشنهاد آمریکا برای آغاز گفت‌وگوها پاسخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/142351" target="_blank">📅 01:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPQQ7jVp0AK-EeSrVnDuMbCsN7RuKwCziJ17HjcEZjXW6ladi5xlf83FCXA6PNcY8CzdxB8bRFq1PcaS_eI-llaIQe-sEs1dr62rrcuRDZrKlZ_zeHS5rc_EkrYcKqw00xAuR5dLvenW2p3UQEwrIcxN7ctFMNiiuX46jzyi4fdhvpJJ0TDvYhhsh9w7LKnX2ZQOXv2xQVKjdrtJhI8Ak4FnKu7U426Q7zDQAmqT-tw3S5tl1P7jm61oyE2rZcH0r6oBaVJpzQHH7JU0zy6mclfLdbMyWQB5zEOjP_sHapy2T8VVrXtDJ08UKqN8yhVep8Q6PaX0EGB12Gy4MPvn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
اسرائیل باید نابود بشه و آمریکا هم از غرب آسیا جمع کنه بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/142350" target="_blank">📅 00:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142348">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUjSKrcSCPU0NuK3PRv-MDNdo4d4kxl4JNym1GtVs94OGQqQqJRcL16orlfHWVOJETkc0vWDJs1g95KJeiyBVwLuJVwJNWEO-4PVW7w_QOO7ArEF1v7L9dOeoJ5yCBxI4yym-Z0aJsbqA_qZm3sLlx9XAVIM3WXsLWeQ2-a92g9CecjRkYUrAYk14wueEN5uYfoH2chszAAs4QtPKlayUxIx2RToEqQVvwREhSILHAmCxmgGjaux-qnCWoNgO-3GW25ZX_MWpGZu9aU3OWfXe01czYxqxwnxscZb2ZwFU1VZbMAoPpVYuejv5f3IxxcaAE5tZj4OP49fyNfihhzmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ تو تروث سوشال که سعی داره کره جنوبی رو اذیت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/142348" target="_blank">📅 00:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142347">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0e46cbee.mp4?token=Jx9oyaCOmglZUVqiYMxKwFi8sZJEbyEsCFML8ce8BW-p9LLMmYyGiI79uANDWOA62dlM2P4Z-Sq14H1BdyhuW35Z8MqIrzaV0q--RCgCf5Dqw_B4fVWiBjtQOq33Wc2oUn909_JlqOhvowJSPo-GzUU0RBZu_-L8IuwdAal3IG9PDTJZ_4dy0-myylOAcVo13OqrDpmnYzQGRX7wH6bqhj4qe3JEs5yRIUjwlvhKRWgF5h9wnREoKbnYl7QiKNfsm1r64-7FfgPCxiP_abX_pSmg4c7omNe16QDqmJeqWpYOcJebcyUF17k59dpg6G-S3X7Hw7yHjBA6ss4ek2RpZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0e46cbee.mp4?token=Jx9oyaCOmglZUVqiYMxKwFi8sZJEbyEsCFML8ce8BW-p9LLMmYyGiI79uANDWOA62dlM2P4Z-Sq14H1BdyhuW35Z8MqIrzaV0q--RCgCf5Dqw_B4fVWiBjtQOq33Wc2oUn909_JlqOhvowJSPo-GzUU0RBZu_-L8IuwdAal3IG9PDTJZ_4dy0-myylOAcVo13OqrDpmnYzQGRX7wH6bqhj4qe3JEs5yRIUjwlvhKRWgF5h9wnREoKbnYl7QiKNfsm1r64-7FfgPCxiP_abX_pSmg4c7omNe16QDqmJeqWpYOcJebcyUF17k59dpg6G-S3X7Hw7yHjBA6ss4ek2RpZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور مالی اسرائیل، بزیل اسموتریچ: کاری که بیش از همه پسر مرا ناراحت کرد، این بود که نتوانست بجنگد.
🔴
در روزهای اول، مدام به من می‌گفت: «بابا، کار را تمام نکن. مقداری برای من باقی بگذار.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/142347" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142346">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6FO0_so-EXlYDf0pqSaS7-Y7hWgm479ti6yraDPzeoVkif9px3udtBlh9XLfbJyaRh9zT9DvQLnsZQw0148gDG0skkmjjs_fXo6ju-yIy8QT0bWCUVnDcSWsPDPglz9RhBhkCnaGAzd7V0PTWInIc440Ds22z5kLFfKR-Eyd9xKPoBD_zy-6yPnGv2lb5Cva6rVAXGIOa2e3DcVriqQJe_k_iPwPDcnH-k3FEwZNRtxbJDZYTcCqaKCQ46aaPvCDgicaURBhZtLG_DO7q6jJuBdt4LUOSOEJdCHGU4ohdiTjyMBRf0xb30jOpbczMAOh_A2RwQSWCTVHlcqMVtDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شانس توافق هسته‌ای ایران و آمریکا تا سال ۲۰۲۹ به زیر ۲۰ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/142346" target="_blank">📅 00:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142345">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مرکز آمار ایران: نرخ تورم قیمت مواد غذایی، با احتساب سالانه، به 128 درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/142345" target="_blank">📅 00:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142343">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7R5gSeijgT0IeEX00YTT3TnBrjHVaa_mgf5UFXjsR3NQIPr1z7n9uec5H7EVJGMkGaeOJMrbxQI1Vba3AmxmuCZFq8wt9rBVEFeYBeHzrS7EJCDxplsim-lAsdvtSf_zRnYV-B3A4yJOJc0j4qegzfELaQEuwHL1RFVw3ZLLVfsljbjvsaATZnhTSNKf88qV0CDrGtwKnyMmfAO-lyUmEv4uXrPQVS_LAG--i_Ei-gsoY-Rzjx3N0gHFqjhJVu242fsz9lK8_RDi4oV2g_t5-i6W-mrkYWilVkNoF0CA8p8rfbt1xHjRv3LhmKiFjg6Giq0QSvRlT9EGri81X6YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهار فروند هواپیمای آمریکایی تانکر سوخت‌رسان که در نزدیکی سواحل ایران پرواز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/142343" target="_blank">📅 00:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142342">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شعام: تا حالا زیادی صبر کرده ایم ، لازم شود از NPT خارج میشویم و خودتان میدانید این یعنی چه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/142342" target="_blank">📅 23:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142341">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
👈
تریتا پارسی، معاون اندیشکده کوئینسی: من به طور فزآینده‌ای به این نتیجه رسیده‌ام که جنگ آمریکا، اسرائیل علیه ایران وارد دور سوم خواهد شد
‏
🔴
تریتا پارسی، معاون اندیشکده کوئینسی نوشت: من به طور فزآینده‌ای به این نتیجه رسیده‌ام که جنگ آمریکا، اسرائیل علیه ایران وارد دور سوم خواهد شد. این اتفاق اجتناب‌ناپذیر نیست، اما نشانه‌هایی که از دو طرف و همچنین از کشورهای کلیدی شورای همکاری خلیج فارس دریافت می‌کنم، باعث شده نسبت به این موضوع بسیار بدبین باشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/142341" target="_blank">📅 23:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142340">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مدیرعامل مخابرات: سرعت اینترنت بزودی با مهاجرت از کابل مسی به فیبر نوری تا 8 برابر زیاد میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/142340" target="_blank">📅 23:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142339">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUsZ6_BseLFrRWJVjHASmEpi12n3-vaDpa_IRn_xnlo-jpXLcmsT-WmoxPmx15tJWDSxD3aPAvXZUYGElWxfxV_Qbi9GaGb8zIq93hkLpqd5wkBL-azzrqyyUqWqjS5ewbedVnhtxR5GQ0qd8-S2x7sqZgbdhP2hJ_b8icPr6fVkLLwP7NrtFCQeXk0G-JlgCwsbOgfDTwvmAOp1B_A4O7IvaBWoVJv0i4X-vMge29_ixUxZMIe0peaWJ42AVrx2rx_XZwO3Z8Og4KIup9ThHVe7a1B5hVYvHW7OC8UXay2yK-RpUNA9FCybq1AFrM1JRdpTBzkby0insMJje5qzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد خیره کننده مساجد در انگلستان:
تعداد مساجد در بریتانیا به ۱۷۵۴ عدد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/142339" target="_blank">📅 23:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142336">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxGI1ryDc8UoHh_YxIsIo7OJoOqhA_cunulx0MCQlRtldygcawnVvk_-vbbnH-nIUgpJFmGHf1zRTIN3ozMJdfyleMx_CWtqGEoHmt2B-rVw8VmPQmX0EOgcpU4ThDmhlmdY0Nv7MnONE1ZsiZyeqNN1DD52J-RCUnh2Zfc9I1vQj_mEH5cIP1zhuN8_6qX77umLNezcDK2CFzQeLg4uHMNcEbEN-M0-xR94RCMWrX8qe1gOlwxOW47BXYox2VJVPfICwlGF8vQlMjW6JIilVrvartCBTmlfTNZ-YMK41j-x_AYfUFOzdnjzEfNvm9KUEZtJqhEkwwkzfLDWaTa-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FL0RvxpiecoVdmbgZ64XCshSHCVw5A6BxtMyLbTnYlEZR0WpS-ie97_7xA35V7HqjdPKzaopvNKqKLiMk2h04450odhsXjn_gjYCQWPXbsasVItz6OaQjdvsIHMq8A_Xfh7OboJ5icVYo0IiHE3GEj3Hw5KAlxMizpEmifVvLXSHpJIO4HVP737Vgu8HwjDdgf3LM_QYaJasMStriN4AIJqb34GzPRbgrXy8tzBxkOTobe_YXOPhcwqr43nJjNQrt_9ivFpmftIJ-L_VEdw4Tlr4G9soufLZvyzg-nL-Nww2R-GwYp9mrx_c5GCfk4qVoRQLjizBpjoCScOhslr-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UI9Pea3PHxGYMw8gQojrESx9X_3dNYxFozgy_yN7RV6bS7j8DW2YIrxR-foib-uzPXkFwzXfcY15ugiBvnMcnUsZHEc4Hn7aUEBpBqmrs9xupnYBRI5xoJYnjzrhBZhPc987gyBt10a8yo0LWCi6E6QEY-yRwAnKbGwr_hzKu5lh4jGE38kKAsrOCvR1jyQ5S69CX8eQFDgNAQDVq8Z9csr06BsBFPr-_Ke8VKDUSCUz-3p-8L7GfKrELP38BIA1Ji9Vzd3s7iQYhndjO4WYVBcKYEDMOc6VWY1doOv00cC6-a8R8IcK7SGGZ8Kke0EaEohEnn2bkIkVNlGjvM2IMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خودداری چند فروند هواپیمای مسافربری از فرود در فرودگاه دبی و چرخیدن آن‌ها در آسمان به دلایل نامشخص.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/142336" target="_blank">📅 23:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqLIQKhIx80PSYTcJ0-C19DsOT5n6YrSjk4uKIQyWe3EGDsoJqJTmBqTJR5yaWdujVm_a-yR8Di7QD816QNAdbA76DlV5nWb6VVKMvChJbAn8rdPQooVcWgM43qWbO8eY5PlZgFpxbiAp5HUI3dnTVMXJ6hRWd-3137LvR2r_OhxToY-s64ygRozLF6YJLZePy5mSZDgQWFKyPzMipFY223bjJT6KHRnfmXeBKp38ILe5fL3I40wBp4HR2yPMycKPCc5I5E9ifd9Ev61QBURGjuivsTrrjAObki9v50U8SDffVtnUBMa-6gaxw1dKKFFzQv-YdjRvqI6zAU1wnp5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در نظرسنجی جدید i24 اسرائیل: نتانیاهو و حزبش با اختلاف از آیزنکوت جلو تر هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/142335" target="_blank">📅 23:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142334">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کانال ۱۲عبری: حجم صادرات تجهیزات نظامی اسرائیل به قطر در سال‌های اخیر، صدها میلیون دلار بوده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/142334" target="_blank">📅 23:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142333">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
اسماعیل بقایی و عباس عراقچی حمله به دفتر رئیس اقلیم کردستان عراق را بسیار مشکوک خواندند و اعلام کردند این عملیات ممکن است فالس فلگ یا پرچم دروغین باشد و کرد ها باید نسبت به اینگونه عملیات آگاه باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/142333" target="_blank">📅 23:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142332">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پولتیکو: رئیس‌جمهور چین قرار است برای نخستین بار در ۱۱ سال گذشته روز ۲۴ سپتامبر در سفر به واشنگتن با ترامپ دیدار کند
🔴
انتظار می‌رود در دستور کار این دیدار تحولات ایران و تنگه هرمز قرار داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/142332" target="_blank">📅 23:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142331">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9trM80BK4it7YZtyBTWRXwNlq7sdpxfsgvl7eeNMoaI9eyrrOwohSzJycUMh_7Kl_cl0WdYqQdjp9v0Ss_Ik6CroTWOvhAsb8Ro2ZD4it5rIZjKMpNe2EgerlJAVOVLvr0toNbpt0oEuQ8zNDCEL8XuBnJqr4eTfw9WqUYQmmJaDRUC3WMWcYZoL5K6x0wwdejWlbxPBDt-3ANupyvMoVyqVC0QKxRDom-w0sFP-jyxSGbRJ3j_KonN8Q8TXuP93ANzk-MDKGpjcLuyQpIzTxq44LbKNI3iqN1Pf7mCVbPL0-aQ7qxpC9yMO-CMTN5duB0qsTRjOEKCq358epxQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پسر ایرانی بصورت ناشناس اومده این اعتراف رو نوشته:
من یه پسره ۲۱ ساله‌ام و عاشق یه زن ۴۵ ساله شدم. اولین بار که اونو دیدم، توی یه کافه کتاب بود. احساس کردم کل زندگیم دنبال یه نفر مثل اون بودم.
اونم از من خوشش اومده بود و باهم اشنا شدیم. وقتی قرار شد ازدواج کنیم پسرش که ۲۴ سالش بود مانع ازدواج ما شد
ماهم یه شب باهم نقشه کشیدیم وقتی خونه خوابیده اونو خفه کنیم تا باهم یه زندگی خوبو شروع کنیم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/142331" target="_blank">📅 23:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142330">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/142330" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142329">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکریپتو اسمارت | Crypto Smart</strong></div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142329" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142328">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-F4j6evR8xlUZdGNXmpagz-CaH734X6c_52NrlYjx9MdEOV8qNQO9a04gG12y8IOa2HupbDr0cPPNoa-l3iEkcKq0D7ej51ZNZSGe_UzX7x21AvlQW3l4RHB5sNWzAXKRwLuVqBS_DcTGqS3Ou1UP77EZNjLLmWS3vzO5MshEXFMq8LPIHBA5gzDSSlvIv9nMioicFzoBZesRrHdtmnelsduSwl1wjvO_rt5ZSKunYo6ojc-3qnOCGKwPfKdLZq2iSBmRMC5O6lurYJQcuNBDC32vz3T8LiYxZnxsqndj1LsXvYM7T6qmArR2Hmqz3xMmr1HVe1XpGOO-Ln7g--bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آمریکایی مدل E-3G، که برای هشدار زودهنگام و کنترل هوایی استفاده می‌شود، از ریاض به پرواز درآمد تا در نزدیکی تنگه هرمز فعالیت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/142328" target="_blank">📅 23:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142327">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Msajx8naPmCzUseuRFShrnpqDxZBWxJYb6AucbhMrvrnQX4bMVPyfMeTOQ8mg_e-75TJoDO3u9WDGJQU8TVOn035Wulf1S_lUqGl8BJTLvF2Gmpy0TNuC8s_I5g2jl7FV5ZVYh_mrU8cv-sq9EWAOu8ftwwO37CbOh3S-Vxm1GkDK7VKAs6AWTXAlwWXqwanC04n7zb7FVqZxWhjWi3F7Pa6SSJcxJkVp8_TBMXZlapIoDJcVcO3siU6sd5A-sdydTL6dkxUdw_0Efrty97NkTm0L7ZQEsXCvotoakTq29LYTcIfdi-xQtbEE82o5-MYde72is1JdqdFjvw3o_uAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غیررسمی/طبق برخی اخبار گویا بزودی قراره به فیلد مارشال، درجه سپهبدی اعطا شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/142327" target="_blank">📅 22:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142326">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کوشنر ، داماد ترامپ : گفتگوهای بین ایالات متحده و بخش‌های مختلف دولت ایران، قوی‌تر از هر زمان دیگری است.
🔴
گفتگوهای مثبت و سازنده‌ای در جریان است.ترامپ در مورد توافق با ایران صبور خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/142326" target="_blank">📅 22:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142325">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کوشنر ، داماد ترامپ : گفتگوهای بین ایالات متحده و بخش‌های مختلف دولت ایران، قوی‌تر از هر زمان دیگری است.
🔴
گفتگوهای مثبت و سازنده‌ای در جریان است.ترامپ در مورد توافق با ایران صبور خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/142325" target="_blank">📅 22:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142324">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845779b633.mp4?token=k2ksbzlMVJrGvVCREfYml_ebIQdF8ct2jbltAumxb4QubSBdrABVss123wmYnox_u7TGDcNaztccvoQnnOF0qkl0M3vfS0OEGXEAh52rX6TGqRZy67mVQI8lVyyV49fz7_q6gZa0yMAkNpY3dHcusX6OoXb4QvaEFSh5aNrFAO7pqjhDKop0suZeyO_7V5VwwYu5Gf13wqZQdjF8kWYZCrxv5UicA4RFEYWHT_7HXyDLOA7o1zKZ2WbWLGUL4i_RAheK1WOBlEdtgQ12F4MXNPjGbYc8FXSJzBBBlLIAZY1uzWu7EP26kSzGpyCDhF6b4Y9BOpE9r0Hlovq8LJ3wl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845779b633.mp4?token=k2ksbzlMVJrGvVCREfYml_ebIQdF8ct2jbltAumxb4QubSBdrABVss123wmYnox_u7TGDcNaztccvoQnnOF0qkl0M3vfS0OEGXEAh52rX6TGqRZy67mVQI8lVyyV49fz7_q6gZa0yMAkNpY3dHcusX6OoXb4QvaEFSh5aNrFAO7pqjhDKop0suZeyO_7V5VwwYu5Gf13wqZQdjF8kWYZCrxv5UicA4RFEYWHT_7HXyDLOA7o1zKZ2WbWLGUL4i_RAheK1WOBlEdtgQ12F4MXNPjGbYc8FXSJzBBBlLIAZY1uzWu7EP26kSzGpyCDhF6b4Y9BOpE9r0Hlovq8LJ3wl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا بنزین گران می‌شود؟!
🔴
رضا نواز، سخنگوی صنف جایگاه داران سوخت: تا الان هیچ تغییری درباره قیمت بنزین قطعی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/142324" target="_blank">📅 22:28 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
