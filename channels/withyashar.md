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
<img src="https://cdn4.telesco.pe/file/ICYkaumb8w3_U9X_1qVn2OL3pTmz1zkZx3yjQpajsGh2V2MwqnDbwr1eOvGQw3b-uEGXmtFekQCnfLIBfG48f0T1LVpI8Iz4PhUDDuQCKQlzUqiv33JODV_T4-Ur9TWhv_o4hm-jymhdUgKc1qcqrqUZYR4XsMLolhWrU-9PeB9ChQE6CIQ6ix1yHD0sl-Bllq1wNn2xP5jWQBduQyf0JyZD1jr255aqS9XVbxy4EkGAchxICSaigUM7CneSObeYoaqByeQvZ5DvN438nH3Q-bTKySqCA_pMa-hOohjINJjokuzEO2WCaeQwcWMp3FsadFhcinR4UhhmMGour3QZ4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 19:14:45</div>
<hr>

<div class="tg-post" id="msg-20645">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزارت دفاع آمریکا پنجمین مجموعه از پرونده‌های مربوط به پدیده‌های ناشناس هوایی و بشقاب پرنده ها رو منتشر کرد در همین راستا شبکه خبری CBS دقایقی‌پیش مصاحبه انجام داده با «آوی لوئب» که ترامپ او را مأمور و نماینده تحقیق بر روی این پروژه کرده، از دست ندید.با زیرنویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/20645" target="_blank">📅 19:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20644">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سناتور جمهوری‌خواه تد کروز، درباره جمهوری اسلامی : اگر شما یک اسلام‌گرا هستید که از آمریکا متنفر است و سعی دارد ما را بکشد، من از اینکه شما یک کشور یا ملت را رهبری کنید و منابع لازم برای کشتن آمریکایی‌ها را داشته باشید حمایت نمی‌کنم؛ این جایی است که ما باید بر آن تمرکز کنیم؛ حال، چگونه فروپاشی حکومت را رقم بزنیم
@WarRoom</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/20644" target="_blank">📅 18:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20643">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=uz1gRiTWTe8W49p2V9Pop51y4zMJLwXIgQ2_227ckRyoq-Mgme2Ru0XPS7kPpRnkfFF7_vie6D2KxQyzYlI21V3DM2JTNMGmkvevAFXYePYd7jtoePFbwkB_7y_s9K86GXaVm6Mr_kB8WZBQ--__H2Xv3dFzdff1hYvZwXSLSu45sC5xN1MHFpTLpEczF-oSpijnvPbSjHLfIk8K7S9oMMwpSAixkFPMlTj9e0QzMJyQzZoL7fYqeStOinTW7DXQ3wiSd0jFQ4HLILjZfLybgBXu2AtCa7hO6vYap3zEOkgZDxJ0j58bgIS0XyvUj8WCx9tTl3CvQYY4Kz8hhr4MUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=uz1gRiTWTe8W49p2V9Pop51y4zMJLwXIgQ2_227ckRyoq-Mgme2Ru0XPS7kPpRnkfFF7_vie6D2KxQyzYlI21V3DM2JTNMGmkvevAFXYePYd7jtoePFbwkB_7y_s9K86GXaVm6Mr_kB8WZBQ--__H2Xv3dFzdff1hYvZwXSLSu45sC5xN1MHFpTLpEczF-oSpijnvPbSjHLfIk8K7S9oMMwpSAixkFPMlTj9e0QzMJyQzZoL7fYqeStOinTW7DXQ3wiSd0jFQ4HLILjZfLybgBXu2AtCa7hO6vYap3zEOkgZDxJ0j58bgIS0XyvUj8WCx9tTl3CvQYY4Kz8hhr4MUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شهباز شریف، نخست وزیر، محمد بن سلمان بن عبدالعزیز آل سعود، ولیعهد و نخست وزیر عربستان سعودی و رجب طیب اردوغان، رئیس جمهور ترکیه نماز جمعه را در قصر الصفا اقامه کردند. در این مراسم، محمد اسحاق دار، معاون نخست وزیر و وزیر امور خارجه، سناتور محمد اسحاق دار، فرمانده ارتش و رئیس نیروهای دفاعی، سپهبد سید عاصم منیر، و مقامات ارشد سعودی و ترکیه نیز حضور داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/20643" target="_blank">📅 18:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20642">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp1K2WJaJc2K6QhSbrNNL6gNLmn9mJM0-AODeIciwjQxsjawfQqooRBoLR3j2Kc0QIb_JVyX8mpBa6Okb5jd3urfT_sUlKxmmwQi6rAP_XzsjU5xl507TrGdw68F1UidRpSMg4X01iM7W1Po7ER26UlqUMsHoJoQO017eFYbmxOGOTZV2BlrovslMAldimKcHIm-6oMR4I70yHU2puSV16HJBUrSge98aJT3jBan8RVn6kXRLS6wGuzXiTK2s50vi8jhOJxt84VAoh3UGqBisGgisIV_lp1oQ_rB3vJTL-ZKutgIcEljL8XCvee-TayfuV6zZToeGrkONpQ995znoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/20642" target="_blank">📅 18:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20641">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شبکه کان اسرائیل: ایران صدها موشک پدافندی دوش‌پرتاب از روسیه و چین دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/20641" target="_blank">📅 17:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20640">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/20640" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20639">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRVFLQt_CfoOizKhzyx9128GLUV0NWnodM_xYdFL0KRVtmJfHsVs9hJDZbgV21kcuQYFz2E5F0Glh4l50TVDge_sE2-369P7blQwLa0ZV2XrrmaON1WCXMe0gbI2Pk78c7DHbgIc4uIbRbveLzBnogJ-sPFAXbViQwooEtuI5aeVlABBM4zLdc0E_CAzOZU81bOa9hWDcN_YA5icjh9X6wNTMVxfMJ-8tmH8pXVvEgBzIeUW-ygQjgtYoA0iMPod-otS6VN3ta5veZkkH_R8HAJRfP1PSocv-wRd4va8onCjCRY6Spp4SvXfT3fqIij7lsKUbQVKBY859WrYwXrDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست وزیر جنگ متنی از مقاله که ترامپ هم دیروز آن را منتشر کرده بود منتشر کرد. این مقاله فقط دیدگاه نویسنده آن را بیان میکند نه یک گزارش خبری.  متن عکس : ترامپ در جنگ ایران پیروز شد پس این هم واقعیت؛ همان حقیقت تلخی که تردیدکنندگان دوست ندارند درباره‌اش…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/20639" target="_blank">📅 17:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20638">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏نیویورک تایمز: برنامه هسته‌ای رژیم کند شده اما متوقف نشده است
‏ بازرسان سازمان ملل برآورد می‌کنند رژیم همچنان ذخیره‌ای از اورانیوم نزدیک به درجه تسلیحاتی در اختیار دارد که برای ساخت سریع ۹ تا ۱۰ بمب هسته‌ای کافی است. داریل کیمبال، مدیر انجمن کنترل تسلیحات، گفت سیاست فشار حداکثری و اقدامات نظامی دولت پرزیدنت ترامپ نتوانسته توانمندی هسته‌ای رژیم را از میان ببرد. الی گرانمایه نیز هشدار داد در نبود نظارت بین‌المللی، رژیم می‌تواند ذخایر فعلی اورانیوم خود را به سرعت تا سطح مورد نیاز برای ساخت سلاح هسته‌ای غنی‌سازی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/20638" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20637">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینستاگرام رو  هر روز میززند و باز‌میکنم دیگه اعلام نمیکنم حتی ! الان برگشته
🤣
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/20637" target="_blank">📅 17:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20636">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqOimgFFW4nMz8tJbDOn_fqrX4n6vaUcKs9RPSbfdsPM5PIa7hLMiY-aZ06TKfgs6xmDojXrHTz8hsC9FgORfK9sv2w4EOM67vGhswgWwTppFum6YqanhEvzpVXn7JTaIS-hhH1Hkg3Nepsz1ehsxhbaMM-ubvv-xQtE8U39_arOT7_fhuTxOEcGmRIoA-Q4DkC6rRfhTv3qxKzh9McZDYurCSYJgI5rNVQ0peges2g5Vj8nCqRTGDSMeMywWd6DFhwB-u7-RcKMpw8rPaAk_zrArNjIvlszF7rtYoZ6SgMVsw6SUvnnhBvLDOGeQkIxh0l4Cb9VJOkpLeo_R1dCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست وزیر جنگ متنی از مقاله که ترامپ هم دیروز آن را منتشر کرده بود منتشر کرد. این مقاله فقط دیدگاه نویسنده آن را بیان میکند نه یک گزارش خبری.
متن عکس : ترامپ در جنگ ایران پیروز شد
پس این هم واقعیت؛ همان حقیقت تلخی که تردیدکنندگان دوست ندارند درباره‌اش صحبت کنند.اگر ترامپ در این جنگ در حال شکست بود، هیچ‌یک از این ابتکارها و تحولات در حال وقوع نبود. آنچه امروز شاهدش هستیم، افزایش نفوذ آمریکا، گسترش مشارکت‌های منطقه‌ای و شتاب گرفتن روندی است که ترامپ برای برقراری صلح و ثبات بلندمدت در خاورمیانه در نظر دارد. این‌ها نشانه‌های شکست نیست، بلکه نشانه‌های دگرگونی منطقه در مقیاسی بی‌سابقه هستند.
رسانه‌ها و تحلیلگران می‌توانند هر روایتی که می‌خواهند ارائه دهند، اما تاریخ‌نگاران خواهند نوشت که ترامپ تأثیرگذارترین عامل در بازآرایی خاورمیانه در دوران معاصر بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/20636" target="_blank">📅 17:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20635">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به گزارش فایننشال تایمز، به دلیل محاصره دریایی آمریکا، حداقل یک هفته است که هیچ نفتکشی در جزیره خارک، پایانه اصلی صادرات نفت ایران، بارگیری نکرده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/20635" target="_blank">📅 16:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20634">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شبکه الجزیره گزارش داد نشست لبنان و اسرائیل با میانجی‌گری آمریکا در رم بدون هیچ پیشرفت ملموسی پایان یافت. اسرائیل با پیشنهاد عقب‌نشینی مرحله‌ای از جنوب لبنان مخالفت کرد و تأکید کرد تا زمانی که سازوکار قابل‌اعتمادی برای خلع سلاح و راستی‌آزمایی حزب‌الله ایجاد نشود، با خروج بیشتر نیروهایش موافقت نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20634" target="_blank">📅 14:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20633">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">«توافقنامه دفاعی مکه» رسما امضا شد : هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
محمد بن سلمان، شهباز شریف و اردوغان توافقنامه دفاعی مشترک میان ترکیه، پاکستان و عربستان را امضا کردند.هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام تجاوزکارانه است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20633" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20632">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0293ab00f0.mp4?token=hdqMgADVq0IK6BMh8-ECHAbMPyKRNPNW_FRz2r7giSiL8MuA7RwbUljJz4dIrmQadNMdBcptTxWYXx6ABg-q3ZXwCKfkqKZr1zww3oDMGhb9Wi2iCsLj8pY60BU1IwQDTr90D1PHfazvDS-xvm2dDRCjD-c180UkuQmvf4XrrvppiaDYM0xar4LrpAOulVzM77ZIsJ-H4mPMYhyfeqAqGgYz0ovUaO-gpq3OytZEwntodKCmo_R2HJPb7o2zP53RIHA5cSsS4_1yfu3L_4XCdgrY8p_pipPLjNJ5DBMMzwIfTEE0vu_cN8XzDnauMXaPLzP_2dAzK2qmLW0_EySbqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0293ab00f0.mp4?token=hdqMgADVq0IK6BMh8-ECHAbMPyKRNPNW_FRz2r7giSiL8MuA7RwbUljJz4dIrmQadNMdBcptTxWYXx6ABg-q3ZXwCKfkqKZr1zww3oDMGhb9Wi2iCsLj8pY60BU1IwQDTr90D1PHfazvDS-xvm2dDRCjD-c180UkuQmvf4XrrvppiaDYM0xar4LrpAOulVzM77ZIsJ-H4mPMYhyfeqAqGgYz0ovUaO-gpq3OytZEwntodKCmo_R2HJPb7o2zP53RIHA5cSsS4_1yfu3L_4XCdgrY8p_pipPLjNJ5DBMMzwIfTEE0vu_cN8XzDnauMXaPLzP_2dAzK2qmLW0_EySbqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
: فقط همین را می‌گویم؛ اگر اوضاع به همان سمت برود، آن‌ها این کشور را نابود خواهند کرد.
مجری
:شما دیروز، وقتی درباره نوادا صحبت می‌کردید، گفتید اگر اشتباه نکنم، ممکن است قیمت بنزین دوباره کمی بالا برود، و بعد گفتی…
ترامپ:
نه، نه. این فقط در صورتی است که مجبور شوم یک حمله دیگر انجام بدهم.
مجری:
یعنی…
ترامپ:
قیمت‌ها فقط در صورتی پایین می‌آید که به توافق برسیم. آن‌ها می‌خواهند توافق کنند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20632" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20631">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20631" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20630">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پرات ریخت ؟
😈
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20630" target="_blank">📅 12:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20629">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20629" target="_blank">📅 12:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20628">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مجری : مردم میپرسند کی‌اینا میرن؟  نوستراداموس هم نتونست بگه! مانوک : انقلاب تقویم نداره … I LOVE YOU @WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20628" target="_blank">📅 12:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز: نگرانی درباره تنگه هرمز قیمت نفت را افزایش داد
قیمت نفت امروز در پی افزایش نگرانی‌ها درباره شرایط بازگشایی تنگه هرمز بالا رفت؛ زیرا ایران با همکاری عمان پیشنهادهایی برای محدود کردن عبور برخی کشتی‌ها و جریمه ناقضان قوانین مطرح کرده است.
قیمت
نفت برنت
با افزایش
۸۵ سنت (۱.۰۳ درصد)
به
۸۳.۳۴ دلار در هر بشکه
رسید
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20627" target="_blank">📅 11:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20626">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e767e0b.mp4?token=LAsSA0Oz2hcz0AfqQg99ANKH7xEfss9kTUHrEPIjrNs4pU7P3jn9xfbwwZPTmlLsxpAM-9WB2d_1ykcXaWaWr_AfbciVowcz9kn7whNoHcR_FhjRzS1HcIHhyhowGOL9sX70iVxGtofUWPZUNILVofrkkKIaJ040n-wAyME1-AaPBQUxMdrltiugtLkfgke5DuxRoR42nmrn-tRhSShqPrATpNV46fTAF-_8XrNQ9kC0XOiUce9Tj2FOLXVIZkAsjE8YrydTUse1Yub-dC-ygCPhYH_IhOfYZ9I_wm1SL-lKeKcQQFHJlj1klPBubDYUmG0i7tDHrLgkSnxi-Rm7FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e767e0b.mp4?token=LAsSA0Oz2hcz0AfqQg99ANKH7xEfss9kTUHrEPIjrNs4pU7P3jn9xfbwwZPTmlLsxpAM-9WB2d_1ykcXaWaWr_AfbciVowcz9kn7whNoHcR_FhjRzS1HcIHhyhowGOL9sX70iVxGtofUWPZUNILVofrkkKIaJ040n-wAyME1-AaPBQUxMdrltiugtLkfgke5DuxRoR42nmrn-tRhSShqPrATpNV46fTAF-_8XrNQ9kC0XOiUce9Tj2FOLXVIZkAsjE8YrydTUse1Yub-dC-ygCPhYH_IhOfYZ9I_wm1SL-lKeKcQQFHJlj1klPBubDYUmG0i7tDHrLgkSnxi-Rm7FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : مردم میپرسند کی‌اینا میرن؟
نوستراداموس هم نتونست بگه!
مانوک : انقلاب تقویم نداره … I LOVE YOU
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20626" target="_blank">📅 11:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20625">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سی‌ان‌بی‌سی : به نظر می‌رسد توافق ترامپ در وضعیت وخیمی قرار دارد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20625" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20624">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏خبرگزاری آناتولی به نقل از منابع امنیتی گزارش داد رجب طیب اردوغان، رییس‌جمهوری ترکیه، برای سفری یک‌روزه راهی عربستان سعودی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20624" target="_blank">📅 10:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20623">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8554GFHlVJfQOqK6vwgGvJnQD6uS3nsQ8ibUzQjHuisFqLTEnlH9W2ur69XWt-WVza20WDR3xTxz24rjpR2zIXnYQiQClmlTmjH2JUEZblzRrCvvxXpYkNop-lyscJeBIxPsZdjQQ3jeasioFDRBk3VQV8QjIMucIzhdZUuA-jIv04CrVcgc8jw5EKpEbfmJx6lEU2Kgt1MTO-x36n_-JN-iQoWuKOXu--pitWpOKhibiApOTrX-KcDTq8hHb4WcRI3V9SU6FjqgUoyNbI6mnyBnVf9xDNiCvxSznfDOZaJ7tqEFPxfn_CZBWtILFUBHFiHC5ugQALUzF51mbM5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏لکه های در تصویر منابع نفت و گاز در دریای کاسپین , طبق تقسیم‌بندی جدید بیشتر این منابع به کشورهای دیگه واگذار میشه
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20623" target="_blank">📅 10:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پس از آنکه وزارت حمل‌ونقل اسرائیل پارک کردن تعداد بیشتری از هواپیماهای سوخت‌رسان آمریکا در فرودگاه بن‌گوریون را ممنوع کرد، به آمریکا اعلام شد که هواپیماها باید در پایگاه‌های نظامی نیروی هوایی اسرائیل مستقر شوند، نه در فرودگاه غیرنظامی بن‌گوریون.شبکه i24News…</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20622" target="_blank">📅 09:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">instagram.com/Yashar – Ruhollah zam and Msoud Molavi @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20621" target="_blank">📅 09:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=YmY3Ujx9A3lP0ULSwAWBGotaYQteniceyley0kjb0GquoGSVj_OsMwrUfjucWpynabZ7WkQaH3ZFdvwLBRtggVTOkYfhmDCmjFTv7rsFZse1-HGTWWt-xQGT8RUAqkJ3ZLgU_FZ0ZExLkbQ23tKJx0OicCK4Q_aJn6tei_hNN0MMi5sGpVW36KNyfi9nMoUaH0-BRRgeWv86pMl-_gBP6-0tEblr9f-7yqDukxGcgWe5v0nBMO9g6LEIeR1NTgHMS9SDVPa1_NvYllebbB5rhkdDPWJdt_vaNeFwL8PlzFYLYVLzwfTjXdmsHmlwN7cY9Zwt6uD8llw7SY-zQpSOV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=YmY3Ujx9A3lP0ULSwAWBGotaYQteniceyley0kjb0GquoGSVj_OsMwrUfjucWpynabZ7WkQaH3ZFdvwLBRtggVTOkYfhmDCmjFTv7rsFZse1-HGTWWt-xQGT8RUAqkJ3ZLgU_FZ0ZExLkbQ23tKJx0OicCK4Q_aJn6tei_hNN0MMi5sGpVW36KNyfi9nMoUaH0-BRRgeWv86pMl-_gBP6-0tEblr9f-7yqDukxGcgWe5v0nBMO9g6LEIeR1NTgHMS9SDVPa1_NvYllebbB5rhkdDPWJdt_vaNeFwL8PlzFYLYVLzwfTjXdmsHmlwN7cY9Zwt6uD8llw7SY-zQpSOV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز سی‌وچهارمین سالگرد درگذشت دکتر فریدون فرخزاد
۱۵ مهر ۱۳۱۵ متولد شد و در ۱۶ مرداد ۱۳۷۱ آسمانی…
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20620" target="_blank">📅 09:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مارک لوین : رژیم ایران باید نابود شود وگرنه این [وضعیت] هرگز متوقف نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20619" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">العربیه : یک مقام ارشد سعودی می‌گوید چندین گزارش اطلاعاتی معتبر نشان می‌دهد که میان حوثی‌ها، شبه‌نظامیان عراقی و سپاه پاسداران انقلاب اسلامی ایران (IRGC) برای آماده‌سازی حملاتی علیه عربستان سعودی ائتلاف هماهنگ وجود دارد.
این مقام این گزارش‌ها را «تکان‌دهنده» توصیف کرد، زیرا در حالی منتشر شده‌اند که ریاض در تلاش برای کاهش تنش‌ها است و اعلام کرده بود مذاکرات به‌صورت مثبت در حال پیشرفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20618" target="_blank">📅 00:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=F0jmfkiDVm1q4HbJjmXKhdv1V8h6bdoo6mckSKnMm0KxM4vtS29WvEEsCRikKftGT-nNI9TIyL2O3L7OyPl4K2pt3v71W3RcClxsLG3VN03XMNWlVBDy6_XPyBS6vKIMXeEiiqEz7sVrh6DNJnr7KP_Am0wXP5_I8J5ibW1Wwz4kgc-9KjYXpWX5LnKJ7fwvXNloE8anM7Cqac6jOn8A5fqMEozeTMUlTLePPxMTL2OjT9kx-MnoxyoMRrvHKNST6ZaIzQwGqfUMx13d0RjfuPo7hOsmhkhmtQAlHQsb7kspDaULIEheMw6aUh_j5ujhL2257UggyPBTeEBmx7zOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=F0jmfkiDVm1q4HbJjmXKhdv1V8h6bdoo6mckSKnMm0KxM4vtS29WvEEsCRikKftGT-nNI9TIyL2O3L7OyPl4K2pt3v71W3RcClxsLG3VN03XMNWlVBDy6_XPyBS6vKIMXeEiiqEz7sVrh6DNJnr7KP_Am0wXP5_I8J5ibW1Wwz4kgc-9KjYXpWX5LnKJ7fwvXNloE8anM7Cqac6jOn8A5fqMEozeTMUlTLePPxMTL2OjT9kx-MnoxyoMRrvHKNST6ZaIzQwGqfUMx13d0RjfuPo7hOsmhkhmtQAlHQsb7kspDaULIEheMw6aUh_j5ujhL2257UggyPBTeEBmx7zOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در سراسر جهان مهمات داریم.
اگر زمانی به آنها نیاز پیدا کنیم، آنها را خواهیم گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20617" target="_blank">📅 00:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=ERTw9z_2aHYaT587ljVk4xO3bFTEN0dwa5-PeqVHMy4O1nzy--hETwulhZytL4pgBMur-A0fLDhRbu_zplTaxdE2ghvWge95WBvidOCpHeI9Ad2qHr46Iz66DLyyrqwilOOXzgRrgN_0pOh5_bV5fQA0PQk4GcGkPmZuXfJ9jQ1Y6cAaXFJye0e1mY06K0ELqptjwprYw5ojVOKuj_KqVdtHniaxpDl-UN54mBjUVwdQZ3OAwPj6r1SSNLPBym8n9qnkRRIV_4Dlj9XmxYbhrVy8jRUdBwM5IxQ01LTpR0L-ISIwlLlzmgOo7FOrjK5PyHJeaWw9RZkX67BwFDAyHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=ERTw9z_2aHYaT587ljVk4xO3bFTEN0dwa5-PeqVHMy4O1nzy--hETwulhZytL4pgBMur-A0fLDhRbu_zplTaxdE2ghvWge95WBvidOCpHeI9Ad2qHr46Iz66DLyyrqwilOOXzgRrgN_0pOh5_bV5fQA0PQk4GcGkPmZuXfJ9jQ1Y6cAaXFJye0e1mY06K0ELqptjwprYw5ojVOKuj_KqVdtHniaxpDl-UN54mBjUVwdQZ3OAwPj6r1SSNLPBym8n9qnkRRIV_4Dlj9XmxYbhrVy8jRUdBwM5IxQ01LTpR0L-ISIwlLlzmgOo7FOrjK5PyHJeaWw9RZkX67BwFDAyHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گزارشی وجود دارد که می‌گوید شما به اهداکنندگان گفته‌اید که باید کاری کنند جی‌دی ونس انتخاب شود. آیا این حمایت رسمی شماست؟
ترامپ: نه. من فکر می‌کنم او عالی است، اما خیلی زود است.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20616" target="_blank">📅 00:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20615">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=PjjrNjPR7x2gYA5l_T6z9eR7gTDu7M-j6ttZgE8HKOVMtN60n9djV-zjwFQ9KzBXr3aoyek9eK7kI6E6FOBPy62vTHw35gvyzqzBCz6t5bx-YNpTlCbrvmrZ1g_vnK-vewsSN-olueiGOPKzFc2bEs20f6NJKXwlCadj_eVFhlXNNb1buUtB_Q0q3cYFwkmTVk8OMWZZeOiZKSjMXu2o5cMHIubm_GVDwTdY1JjkY6hMky5nv2HdKurTX8FevrNsYZKIhR98NbBKYi79FIux8Jh54vdE27TMpuQE1oMCluRuWQVr4QOoifMc8FWcyR6zYRXvvtI6YJMwcLuoWgzPkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=PjjrNjPR7x2gYA5l_T6z9eR7gTDu7M-j6ttZgE8HKOVMtN60n9djV-zjwFQ9KzBXr3aoyek9eK7kI6E6FOBPy62vTHw35gvyzqzBCz6t5bx-YNpTlCbrvmrZ1g_vnK-vewsSN-olueiGOPKzFc2bEs20f6NJKXwlCadj_eVFhlXNNb1buUtB_Q0q3cYFwkmTVk8OMWZZeOiZKSjMXu2o5cMHIubm_GVDwTdY1JjkY6hMky5nv2HdKurTX8FevrNsYZKIhR98NbBKYi79FIux8Jh54vdE27TMpuQE1oMCluRuWQVr4QOoifMc8FWcyR6zYRXvvtI6YJMwcLuoWgzPkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: فکر می‌کنم این جنگ خیلی زود به پایان خواهد رسید. به نظرم آنها دیگر نمی‌توانند مدت زیادی به این وضعیت ادامه دهند.
خبرنگار: آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
ترامپ: نمی‌خواهم بگویم که توافق انجام شده، اما در حال حاضر تا حدی باز است. ما کنترل تنگه را در اختیار داریم.
من در مذاکرات با ایران دخیل هستم. اوضاع به‌خوبی پیش می‌رود.
ممکن است به‌زودی توافقی حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20615" target="_blank">📅 00:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20614">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20614" target="_blank">📅 23:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20613">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20613" target="_blank">📅 23:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20612">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آمریکا : اگر
هیچ‌یک از والدین شهروند یا گرین‌کارت‌دار نباشند
، دولت قصد دارد در برخی موارد دیگر به کودک متولدشده در آمریکا تابعیت خودکار ندهد. این سیاست به‌ویژه افرادی را هدف قرار می‌دهد که برای
«گردشگری زایمان» (Birth Tourism)
یا با اقامت موقت وارد آمریکا می‌شوند تا فرزندشان پاسپورت آمریکایی بگیرد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20612" target="_blank">📅 23:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20611">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20611" target="_blank">📅 23:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwolXaMNHmRlT8i8RDglx3R7KZWH6wq792Lin3p3FQYGWjGxp8lYo5w3xkzdmoiATPNOfgZPe9QgzNCJMDgl-hshBczwkpeCS8tsvcFjNtoR5s1WY2NQSvwukd0xBiFxdacrha37nc_YuwI5dImM9tgwm-6ynjns-dxXP-O5ltzz_yfW2Ov1EDqi1rvZv87LquXdAGK00nOoyUbR2z7eyKwH_J-wabG7XaD2-wYbk6e1nWVeRccOp8pAy58wxKog3oesnFvCVltreSEb-1f7ji5aKIirgibgx4NkJ3dMDCjP9c74rck38Wi8zbuU-TxvRj5g5FyHbrlmcTWb9n_L8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم اکنون در آسمان انجام مأموریت میکند. دوستان بسیاری اسکرین‌شات گرفته بودند که این هواپیما رفته، لازم به ذکر است چندین نسخه از این هواپیما در پایگاههای آمریکا در منطقه حضور دارند. ولی این هواپیمای به خصوص همچنان به مأموریت خود ادامه میدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20610" target="_blank">📅 23:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏افشای تکان‌دهنده ژنرال جک کین :
‏"پاکستان و قطر بر سر منافع مشترکشان با جمهوری اسلامی، دولت ترامپ را درباره اهداف واقعی تهران فریب داده اند"
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20609" target="_blank">📅 23:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ایالات متحده، اقدام حوثی‌ها را که آن را "حمله ترسوانه" به نیروهای وفادار به عربستان سعودی توصیف کرده است، محکوم کرد و به خانواده‌های قربانیان تسلیت گفت. @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20608" target="_blank">📅 23:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMdtr383Mpl31Yh-ZwLuTVSARbWxA_RW_KBCL5b0fZrB5hgboEkvlAm03mnqUOXAHpjae0dBzLUv4F02tkR6jkC_N_8V7xUaGGWdcBBm2BQk6X-XiVYHmxY364W-TteX1JLfar8zjmLP_Bf5ouhsrQxkt0B-RqA6lZ46RiO6kCDZJm2jRoS0j7E93QwGK5H9SdW53A2QIurXFdkSEIqhnyrlTbDbis8MJxSJ9fb-l9_0DEsH5gMbJz77BC0Iy2Qp7o5Q0gdUP5LW82mA-Us8IbEAvMEgA6itNlYCQZr2LHTj_Evsto0KHMnWWHJ-C369r1hrg4O_VQ54Rt6iYsCuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان ۴ دهه واردات نفت از عربستان؛ آمریکا به سراغ ونزوئلا رفت
برای نخستین‌بار از سال ۱۹۸۵، واردات نفت خام آمریکا از عربستان سعودی در ماه جولای به صفر رسید؛ تغییری بزرگ در نقشه انرژی جهان که پیامد مستقیم تنش‌های نظامی در خلیج‌فارس است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20607" target="_blank">📅 23:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olnfcuGxBOZYz8ru7ETMXL66tKEyYt_Q3MPZJlCFJ0N17ncusgkYLz47mPqNf19A8pDEl_Y8tMWWdihjqcV3Ls_ps3ruL04rnP-xxq3S6MoTt0p1n413uNtbBj2q1ekQUwJ0d5WezV6H2eqN3QH10-ZbEPY902TuZjmy6d-Xrd5JjZZ0lvZMRlHkKA1ROdyhc0O_rVS6JHztqRTq8AoGe-F7kOoXFOBDa0uxmwBAJo-4C-ygeh4TKHuGq-3mEbRVQWnmrO9GVmZOdI7vl_1eJ-Q-ERc4AhyPJKtCknluejbCa2ef6F_I67g50BcszuoYaaVdCQ4eSrP9dlpryxt2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در لحظه گزارش شلیک موشک، حداقل دو نفتکش در حال عبور از تنگه هرمز از طریق کریدور تحت حمایت ایالات متحده بودند.
NISSOS KEA و NISSOS KEROS، هر دو قبل از نزدیک شدن به تنگه، سیستم شناسایی خودکار خود را خاموش کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20606" target="_blank">📅 23:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تسنیم
: منشأ صدای انفجار در قشم، هدف قرار دادن اهداف متخاصم بود
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20605" target="_blank">📅 23:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تایید نشده انگار از ارومیه موشک پرتاب شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20604" target="_blank">📅 22:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20603">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جنگ میشه ؟!</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20603" target="_blank">📅 22:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20602">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok67E3SR5stQkPGtYKWSe32WvFkRkqY0kH0W1ZSwclDTg4lzmbETbStKQfY3viJ_05QHKri_J5KnIyYOPmkmbczxa-ZAPZLtnBduL9sj6Z8wbGIUVhJCM8Nk7r-xi8vwF4hILuzo0e4PfT3mMeStishpDyVeW-vfudwwTKHnxsWANrv8rvNsVOnMwOMiC_eQYg4VaY7EY9vqRisSHRwb-iuYCHsthiAlPb5Nmh16Ohwfptq3ENULc6HovFi75262QStcG_QZ5mrSLJ4bAz3P6A8FKjtBgA5bzu1H_G4uddrJYsn4hqAB1X1lS_96zV6f1rWS6bYxluJqnYg_AF5mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دود از پایگاه موشکی پارچین ، بی بی داره خنثی میکنه شاید براشون
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20602" target="_blank">📅 22:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20601">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20601" target="_blank">📅 22:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20600">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رویترز: طرح ایران برای تنگه هرمز نشدنی است، آمریکا اجازه نمی‌دهد!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20600" target="_blank">📅 22:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20599">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اکسیوس : به گفته یک منبع آگاه آمریکایی، چند ساعت پیش ترامپ و محمد بن سلمان تلفنی با هم حرف زدند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20599" target="_blank">📅 22:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20598">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر انرژی اسرائیل (از مردان نیک روزگار): حتی اگر آمریکا و ایران به توافق برسند، اگر ایران برای احیای برنامه هسته‌ای یا توسعه برنامه موشکی خود اقدام کند، ما پاسخ خواهیم داد.
ما به هیچ توافقی که امنیت اسرائیل را کاملاً تضمین نکند، متعهد نیستیم
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20598" target="_blank">📅 22:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20597">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش پرتاب چندین موشک/پهپاد از سیرجان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20597" target="_blank">📅 22:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش های مردمی با سانسور : تنگه مال اقوام درجه اولشون نیست که شب خنثی سازی کنند
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20596" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قالیباف با صحبتهایی مانند آخرای شمخانی گفت:
حمله بزرگی در راه است... صبر کنید، نه، آن‌ها می‌خواهند مذاکره کنند. این دیپلماسی نمایشی است که بارها تکرار شده است.
استفاده از زور و تهدید، همراه با وعده‌های دروغین و اخبار جعلی، یک استراتژی شکست‌خورده است.
حقایق را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتر نیازی نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20595" target="_blank">📅 22:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش مردمی : اطراف یا خود اسکله بهمن قشم رو ۲ بار زدن ۴ بار هم دروغه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20594" target="_blank">📅 22:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20593">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بخشی از رسانه های رژیم : موشکی هشدار آمیز توسط نیروی دریایی سپاه پاسداران به سمت یک شناور متخلف در تنگه هرمز شلیک شد.
@WarRoom
بخشی دیگری از رسانه های رژیم: صداهای انفجار جزیره قشم مربوط به مهمات عمل نکرده زمان جنگه</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20593" target="_blank">📅 22:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یک صدای انفجار جدبد از دور در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20592" target="_blank">📅 21:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20591">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20591" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20587">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش صدای ۲ انفجار‌ در قشم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20587" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20586">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ruhollah zam and Msoud Molavi @WarRoom</div>
  <div class="tg-doc-extra">instagram.com/Yashar</div>
</div>
<a href="https://t.me/withyashar/20586" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">صحبتهای افشا شده از مسعود مولوی با روح‌الله زم در مورد اسرار سیاست و پیشبینی جنگ ایران و آمریکا.
‏این صحبتها اولین بار چند روز پس از ترور مسعود مولوی در ۲۳ آبان ۱۳۹۸ پخش شد. همچنین روح‌الله زم در مهر ۱۳۹۸ توسط جمهوری اسلامی ربوده و یک سال بعد حکمش اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20586" target="_blank">📅 21:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20585">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش حمله سپاه به اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20585" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20584">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شاهزاده رضا پهلوی : جمهوری اسلامی تو شرایط ضعف و بحران مشروعیت، قصد اجرای کنوانسیون آکتائو (رژیم حقوقی دریای کاسپین) رو داره. این کار بدون اراده ملت و تضمین کامل حقوق تاریخی ایران، تهدیدی جدی علیه منافع ملیه. معاهدات 1921 و 1940 و اعلامیه آلماتی، حقوق مشترک و نیاز به توافق همه کشورهای ساحلی را تأکید کردن. اما کنوانسیون آکتائو با اجازه توافق‌های دوجانبه و چندجانبه، اصل اجماع رو دور می‌زنه و جایگاه ایران روتضعیف می‌کنه.
این اقدام از موضع ضعف و مغایر منافع ملی است. حقوق ایران تو دریای کاسپین قابل معامله نیست و هر تصمیمی بدون رضایت ملت، نامشروع و قابل بازخواست خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20584" target="_blank">📅 21:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20583">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۲: رئیس سازمان موساد دو رئیس بخش را به دلیل شکست در تلاش برای تغییر رژیم در ایران، برکنار کرد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20583" target="_blank">📅 21:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20582">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9xnyEYAPHZTG8RN1F7KpZ4aNOG8L_h2Rmg_M-w53awGMqDV6ixlg35mp3lq_LacrFRfuGoCL1TrxE6iLusTEmfNtmKAHZgNuq2aECk28DqTHgpmThIJGjoh3k0S411dTQz0v4ix7XMYsRsjuDPLsfz6zuysnLTOty0vAzhxuGRqMXgv3t1yjG80PK1VXmKBOCK75p3JUtrStzwRCNSRZ_W2UpMi5GC-pK0YAN4liXfYd-QOef_vI3_RCDYFHUsZ3t9XgcdvYfYglgp0krtMsvwtXy0baNCRtSqFQ6bogVXyai5s__cIjhUBuTr10v_9RA5OecbD0RvSOISxnqHtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جعلی، مثل همیشه، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس هستند. من از عملکرد پیت هگست کاملاً راضی و خوشحال هستم. همه چیز فوق‌العاده بوده است، از جمله حمله ما به ونزوئلا که در کمتر از یک روز به نتیجه رسید و به ما امکان داد یکی از خطرناک‌ترین جنایتکاران جهان، نیکلاس مادورو، را به دست عدالت بسپاریم. همچنین در مورد ایران نیز همه چیز به‌خوبی پیش می‌رود؛ کشوری که برای این هدف که هرگز به سلاح هسته‌ای دست پیدا نکند، به‌شدت تضعیف شده است. پیت در میان نیروهای نظامی احترام بسیار زیادی دارد و اصلاحات بزرگی انجام داده است؛ از جمله حذف برنامه‌های DEI (تنوع، برابری و شمول) و افزایش جذب نیرو به بالاترین سطح تاریخی. این شایعه را روزنامه واشنگتن کام‌پست، که یکی از بدترین رسانه‌های این حوزه است، منتشر کرده؛ آن هم با وجود اینکه ما به آنها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این نوع «خبررسانی» جعلی، مصداق خیانت است!
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20582" target="_blank">📅 20:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20581">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">توپ در زمین آمریکا است,ترامپ باید تصمیم بگیرد
الجزیره : در خصوص مذاکرات باید گفت که به نظر می‌رسد توپ از زمین ایران و عمان خارج شده و به زمین آمریکا افتاده است. اکنون چشم‌ها به رئیس‌جمهور ترامپ است تا در مورد جزئیات باقی‌مانده و تعهدات آمریکا تصمیم بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20581" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20580">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-s-PeDJwLS4HUDKWjvvjh79aa0baJ6V3ETdBM_gXldAduQCeSY79siztOM8JI3nHfTFmiDi9ddBxxzkpwCSc6OVn2lYTDpGFCsOieKJvJnUQVVFu8HqVx-7MI76prKtntscfBDESpM0jfZUyzaoswAIYFbtlWbx-Hl7-m4twT5w7IIanF2sHYnZDYzgL0Zr5BHuj9FUt_nr3RaYSgxTc5EARdw8FmBj09NGpDVyFE1u-blhZIfsbnjuk9ryEuT9Lg_hrEH5YmvWD1SqwnOcDg0UmBMOkhJIyMG4qFSp7iJW3UIrqaWjkA8LOTJnCHe3tkOUrhBIbeUNr4BkgwBOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب‌افکن مخوف B-1b از فیرفورد بلند
شد تمرین کرد و با توجه به الگو احتمالأ سوختگیری هوایی هم امتحانی انجام داد ،  حسابی خودشو گرم کرد و آماده شد و دوباره به مبدأ برگشت
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20580" target="_blank">📅 19:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20579">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20579" target="_blank">📅 19:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20578">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رسانه های رژیم : طبق چارچوب مذاکرات میان ایران و عمان که نهایی نشده است ، در مرحله نخست کشتی‌های ورودی از کریدور شمالی تنگه هرمز در نزدیکی ساحل ایران و کشتی‌های خروجی از کریدور جنوبی نزدیک ساحل عمان عبور خواهند کرد. پس از پایان این دوره، تردد از هر دو کریدور متوقف شده و همه کشتی‌ها از کریدور میانی عبور می‌کنند؛ به‌گونه‌ای که ورود کشتی‌ها تحت مدیریت ایران و خروج آنها با مدیریت مشترک ایران و عمان انجام خواهد شد. همچنین هزینه عبور به‌صورت بهای خدماتی مانند سوخت‌گیری، بیمه، خدمات محیط‌زیستی و سایر خدمات تعیین می‌شود و ادعای دریافت تعرفه ثابت ۳ یا ۷ درصد از ارزش محموله‌ها تکذیب شده است. بر اساس این گزارش، عبور کشتی‌های آمریکایی و اسرائیلی از تنگه هرمز نیز ممنوع خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20578" target="_blank">📅 19:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20577">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال ۱۲ : نیروی هوایی ایالات متحده تخلیه بخشی از سوخت‌رسان‌ها در فرودگاه بن گوریون را آغاز کرده است @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20577" target="_blank">📅 19:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20576">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuTnL0xrexuZWzUX8NkqQK0JWNujEgdtTZlQHNrGEU2IrNV41HVJzkhxCAg790lB7hbH2tZef82wAWo9s704F3KLfJZqV81ESQkQz7RtsFztZM3NbAmY1BVa3sS56q0SFjy6AdrLmL8sawoiIRK-7u9U6tJz-QVXXFpNBdxxfYy3qAcQiOOohOGQQCsn83J_Ved2FEbUswv2kcAk90-0jiLhrcIrORzNZcAO2auUKXLWZhN1Af5SmT7faGztCdzeX87kraHRwfD6Gjei4SxgNKdp6lbH6J9sIxySBP4PQ2V4MdEh1OrmRe0rr5z5QGyqOf3Wieq2gJTeEZXZfkzcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20576" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20575">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تعدادی از نیروهای عربستان سعودی کشته و زخمی شدند، پس از آنکه یک موشک شلیک شده از یمن مستقیماً به پایگاه‌های نیروهای تیپ واکنش سریع اصابت کرد. @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20575" target="_blank">📅 18:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20574">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ان‌بی‌سی نیوز: پنتاگون جلسه اضطراری برای تأمین تسلیحات برگزار می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20574" target="_blank">📅 17:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حسین شریعتمداری نماینده ولی فقیه و مدیرمسئول روزنامه کیهان : باز شدن تنگه هرمز یعنی باز کردن راه فرار دشمن و از دست دادن یکی از مهم‌ترین اهرم‌های فشار جمهوری اسلامی.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20573" target="_blank">📅 17:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری رویترز : هنوز درباره نحوه اجرای «کنترل» ایران بر تنگه هرمز توافق نهایی حاصل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20572" target="_blank">📅 16:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54aca75746.mp4?token=rsHnq2oFJYgLpz-0u6vEa583awixj-0R63ePtj8xfgGuOveGtHXTIxSVJ-r4dnakbXBBumpSNB1yitORzzLQN2dkvGEpjDgfjP0pvsNW7RWYc33MUV307INFSkG47scR9DtP8aq84r_6Rcjjo9qd-shuN3sLvE8280gLP3bcTSjC1RHP6RLgTnZUee9w3yL2m3WPEHXbQeOYsEG_OjcVYZYMJ0XBKzo7sSlkO_K_N69q1OCVKwcYZpXHMTznRpA_bQ2OPAi2XAI7d_hG5dwsicEC3dg87deyyxTNR0LdlLtHxZOHZzjk5-YxWCCbfIwiBcCfVkOpeiFO72oiS0cIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54aca75746.mp4?token=rsHnq2oFJYgLpz-0u6vEa583awixj-0R63ePtj8xfgGuOveGtHXTIxSVJ-r4dnakbXBBumpSNB1yitORzzLQN2dkvGEpjDgfjP0pvsNW7RWYc33MUV307INFSkG47scR9DtP8aq84r_6Rcjjo9qd-shuN3sLvE8280gLP3bcTSjC1RHP6RLgTnZUee9w3yL2m3WPEHXbQeOYsEG_OjcVYZYMJ0XBKzo7sSlkO_K_N69q1OCVKwcYZpXHMTznRpA_bQ2OPAi2XAI7d_hG5dwsicEC3dg87deyyxTNR0LdlLtHxZOHZzjk5-YxWCCbfIwiBcCfVkOpeiFO72oiS0cIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری: آیا هنوز معتقدید که نوعی تغییر رژیم در ایران امکان‌پذیر است؟
‏مایک پمپئو: 100٪
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20571" target="_blank">📅 16:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منابعی از گروه تروریستی حوثی های یمن به رسانه های رژیم اعلام کردند تا دقایقی دیگر، نیروهای مسلح ما با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20570" target="_blank">📅 16:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کویت با استناد به امنیت ملی، دستور تعطیلی فوری تنها مدرسه خصوصی ایرانی خود را صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20569" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b68ab7702.mp4?token=qlig2vivaXWs3VTXqO-31kpYr1FipiwkbnYS0OFQEykDvIvqYJx40EKvmMnNkwG3hlphRQg3Gzj75mVRZaYURoLjm-N-DRithhlcSP59wMSqNwxz4s5oVm5M6wCzTb_ltjHSsBkKYqg8k5uIHlQP4jBCVLgApTviQIdEFWpcKBy6yGVVoLfaECiGuOEu1X1KuS4EDzjvdCOt_Ke8IOFftr6zyFaHqS0xZH2KPfppn3f6Q_NxFarzwQGP7BAoSSPuwfr7Dyjo75SCn2ai9iom11ahN0Uv6_-svFeKo0eBzRfXPQzrMrL7v2BAiXHgnDK2ScWXAUHZkuebJ7QFkRpW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b68ab7702.mp4?token=qlig2vivaXWs3VTXqO-31kpYr1FipiwkbnYS0OFQEykDvIvqYJx40EKvmMnNkwG3hlphRQg3Gzj75mVRZaYURoLjm-N-DRithhlcSP59wMSqNwxz4s5oVm5M6wCzTb_ltjHSsBkKYqg8k5uIHlQP4jBCVLgApTviQIdEFWpcKBy6yGVVoLfaECiGuOEu1X1KuS4EDzjvdCOt_Ke8IOFftr6zyFaHqS0xZH2KPfppn3f6Q_NxFarzwQGP7BAoSSPuwfr7Dyjo75SCn2ai9iom11ahN0Uv6_-svFeKo0eBzRfXPQzrMrL7v2BAiXHgnDK2ScWXAUHZkuebJ7QFkRpW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مایک جانسون، رئیس جمهوری‌خواه مجلس نمایندگان آمریکا، گفت:
‏«ما در انتخابات میان‌دوره‌ای پیروز خواهیم شد؛ چه مسئله رژیم تروریستی جمهوری اسلامی را پیش از انتخابات حل کرده باشیم و چه نکرده باشیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20568" target="_blank">📅 15:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جروزالیم پست: اتهام جاسوسی به نفع ایران به دو زوج اهل عسقلان وارد شد.
این زوج، اقدام به تصویربرداری از مکان‌های حساس، از جمله بندر ایلات و کوه هرتزل کرده بودند و همچنین خانه‌های افراد امنیتی را تحت نظارت قرار داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20567" target="_blank">📅 14:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6MaxBqM9EpWLU0H5w_JnOV7pTTne_kp4wWCjNec7lGLZpp0hSLSrLtflQV3Molr5JGc3zOQgh2822XyMy1UwgM78Aqn5RH_XYbuYq_46x_jitVCo0Th0WwH8VAsutd1_gDh2dp-U07_-2eRYjiwhdBOjZiT0Q0YkiMvodF3ygK6KcJUDb_Rg1IZbEOORi7Njzrn8D2RLs84rt0tDNnYgScr_Qe2n5uPEj4Ys0u7MmQRZUc_WSKiSbdkJLu2CNfcKaGr-OiNZ1t9sjm0tbMjWldzQZ6gXrZGsaZbXkszsQMBgYp6qAxkfapK1YqCmUPFcXtAnxI31P2KN5MnutsjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ : نیروی هوایی ایالات متحده تخلیه بخشی از سوخت‌رسان‌ها در فرودگاه بن گوریون را آغاز کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20566" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حکومت ایران عوارض ۷٪ را بر تمام کشتی‌های تجاری عبوری از تنگه هرمز اعلام کرده است , این امر برای ایران ۳۸۵ میلیون دلار خالص روزانه یا بیش از ۱۰۰ میلیارد دلار خالص سالانه با حجم ترافیک پیش از جنگ ایجاد می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20565" target="_blank">📅 14:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل می‌گوید ایران از ماه مارس حداقل ۵۶ نفر را اعدام کرده است - افزایش چشمگیری نسبت به ۱۵ مورد تخمینی در مدت مشابه سال گذشته.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20564" target="_blank">📅 13:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏واشینگتن پست گزارش داد که دونالد ترامپ، رییس‌جمهوری آمریکا، در دیداری خصوصی با حامیان مالی خود گفته است: در نهایت، باید جی‌دی را انتخاب کنیم. این اظهارنظر نشانه‌ای از احتمال حمایت او از جی‌دی ونس در انتخابات ریاست‌جمهوری ۲۰۲۸ است.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20563" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20562" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20561" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20560" target="_blank">📅 11:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یاشار : امروز سنای آمریکا قرار است ساعت
۱۰:۳۰ صبح به وقت شرق آمریکا
، برابر با
۱۸:۳۰ به وقت تهران
، درباره لایحه
CLARITY Act
رأی‌گیری کند. این لایحه با هدف ایجاد چارچوب قانونی شفاف برای بازار ارزهای دیجیتال تدوین شده و از مهم‌ترین قوانین تاریخ صنعت کریپتو به شمار می‌رود. در صورت تصویب، بسیاری از تحلیلگران انتظار دارند بیت‌کوین در کوتاه‌مدت بین
۳ تا ۸ درصد
رشد کند و آلت‌کوین‌ها نیز افزایش بیشتری را تجربه کنند. در صورت رد شدن، احتمال اصلاح
۵ تا ۱۰ درصدی
قیمت بیت‌کوین وجود دارد، هرچند شدت واکنش بازار به ادامه مذاکرات بستگی خواهد داشت. با توجه به وضعیت فعلی مذاکرات، احتمال پیشبرد این لایحه حدود
۵۵ تا ۶۵ درصد
و احتمال شکست آن
۳۵ تا ۴۵ درصد
برآورد می‌شود، اما هنوز اختلافات سیاسی بر سر برخی بندهای آن به‌طور کامل برطرف نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20559" target="_blank">📅 10:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPPSkNJ5WYGQm2ekmGnlDZb3OLTjmhjh64n8S2-o4C2nmOcuqUPt0cJ2_-xnCkVDPkHrkIZ_Sc4RDtA1zoMUw9oXcpbAKBwilb7HHM2gLsljNamvhqQnidPFeRYzff6lwKEwCTQQlKfYkz_kcfzT7Q_Rmrtfwy5A8X4S3JPqdBzJLbpvnoOJxAL_lSnQmM_3neLtDXs5fmfFOYsnhYqbaE33ouxNMmFfAk5jKFpVOLce-b4WmdTSvWxj7PvIF8bHMTpH-liaY1p8BfumTzRPSkp5S4Fc9pOX2ZsG4aB6a1-OT9iNd4bqHqRmlYb7yu2M4Qm9t56X2kDkgqXWzypR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «افشاگران» این اظهارات…</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20558" target="_blank">📅 10:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utgHV_Jgwr2Pgse7tfl8J0w5wAHtPYRIVjiwD0-TdwDog5ZHPAa4uCuHElcuUT7D8Rt4gsZW9_7pIpSTcRtAapffS_IxptlrLYqAZga_0q_9OANRwofr0jfdmeo8z0hcPLDpN9v-EnvPv6k9sJAakIoLWjVFuxC0TVH57hCOdFeWQxGMouZbJVPpD7BQ3C8jFEgL_7oIotrZJ-P6ttjfM86r6gn0nQcwHnpZPxUF7qnUFSeiD9q0iS2qNKzlzIhR6EVIZTfCxjkNJzMxLD71N1MSPKQzA4aCWUm43JjIRGsnvxMhRoJyi17wAZVAA3E1C8P9B0D4tudKEL4kKCWegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: قیمت نفت در پی امیدها به توافق ایران و آمریکا در مورد تنگه هرمز، کاهش یافت بهای معاملات آتی نفت خام برنت با کاهش، به ۷۹ دلار و 2 سنت در هر بشکه رسید
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20557" target="_blank">📅 09:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSLBb0zcFvkSRmVEFdOmD8zrHvmCttWOy05Yp1onmtDv-Q-vtSjEu1HgPWhNy7g5aNVDDBOL8DwmXOc8yh2mb8CIJvi2qWQku7UETWe8YJTwSjxweJ9yQvLt08IIPf-56S49tFV-rcSxfYv-1Tql-dRxrcmR0MbZ1Io2WVPP4lWWLeswUV6tfbPzYv0lTfuULHAYLn_NY18iHK8OQkL6sZYlLsFTCF-q28c7w_L7BO5hPARshwqhYLhfUgCaq4xv-1KtDJJQCsSsxs6HMERK0asUKaMl2G11Qn5NFfm7rBjuh18Hu6EBiAKlPYGAmHFDPAUe9-FzAdQrL17l5dGqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «
افشاگران» این اظهارات خیانت‌آمیز تحت تعقیب هستند. احکام حبس طولانی مدت برایشان
درخواست خواهد شد!
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20556" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=AsjBIGYkPwbwMvXb9s8OPQc5mpAX05PU6MCn-qyW8DtzEQRyC4KYZ536G9clND0D470EU6F8bx0Gj-64FI7_qx5OkNZ5NMe4HGUKRdLHg7vHIYVmhxnueY9tMP9OJPpmWGl99aTYBUbz62UCFkP-krJxgFKroQzSsDi89OiKfNsEs7ODcc_JOTYyGjGaRVy5MLgImYXDKPWvjmz7GyPxltpcbrsTkOn8-SapCLgpkn-ITw9zmnCl4OoxouuosIf6P6BJ9fmfktNFg20fjw4Bu79_izgk5xldxoyxl-M3k-IgN2rx7F1VHSuJxqLM11_5coXuRYqR_nqb2dq8DqJrzlj-j-4W7SN6yc8fFYJPotPwG0zLxKY4GKKcmZUb-WPMc-hFlKbqPqqhwmwjL06FjXuy5q1D8Lw06WuYPvc8ITjKTmQAkuz1FYnh-zgX1s-tjBSw1CFAS75TW8V7pOjt13HvS1_1l2qb41HqGpnq8MHtnVzt3YpkjKqWyMTthcutXoA4vjiSHPlZtTSQiEWaKe9oKV1C3JEjm1LGunuQQnGrcfnveA-Mf12ZvJxB2-0qbX6L5i2lhWY8xXx8nWrLs205sHfRfB60OhEgn8DA-wdF0co0oAvWVLe3XMcBszYBllZKVGbmDbcwBshRIkmlrmy1HkcbRDTemgV6gaHE3mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=AsjBIGYkPwbwMvXb9s8OPQc5mpAX05PU6MCn-qyW8DtzEQRyC4KYZ536G9clND0D470EU6F8bx0Gj-64FI7_qx5OkNZ5NMe4HGUKRdLHg7vHIYVmhxnueY9tMP9OJPpmWGl99aTYBUbz62UCFkP-krJxgFKroQzSsDi89OiKfNsEs7ODcc_JOTYyGjGaRVy5MLgImYXDKPWvjmz7GyPxltpcbrsTkOn8-SapCLgpkn-ITw9zmnCl4OoxouuosIf6P6BJ9fmfktNFg20fjw4Bu79_izgk5xldxoyxl-M3k-IgN2rx7F1VHSuJxqLM11_5coXuRYqR_nqb2dq8DqJrzlj-j-4W7SN6yc8fFYJPotPwG0zLxKY4GKKcmZUb-WPMc-hFlKbqPqqhwmwjL06FjXuy5q1D8Lw06WuYPvc8ITjKTmQAkuz1FYnh-zgX1s-tjBSw1CFAS75TW8V7pOjt13HvS1_1l2qb41HqGpnq8MHtnVzt3YpkjKqWyMTthcutXoA4vjiSHPlZtTSQiEWaKe9oKV1C3JEjm1LGunuQQnGrcfnveA-Mf12ZvJxB2-0qbX6L5i2lhWY8xXx8nWrLs205sHfRfB60OhEgn8DA-wdF0co0oAvWVLe3XMcBszYBllZKVGbmDbcwBshRIkmlrmy1HkcbRDTemgV6gaHE3mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا : بر اساس این گزارش، فرمانده یک نفتکش در حال عبور از تنگه هرمز اعلام کرده است که در فاصله حدود ۹ مایل دریایی جنوب‌شرقی منطقه کُمزار عمان، صدای دو انفجار را شنیده است. @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20555" target="_blank">📅 07:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جی دی  ونس : من با ترامپ در مورد ایران اختلاف نظر ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20554" target="_blank">📅 07:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سناتور تام کاتن: «ارتش ما آماده است تا کار را تمام کند».
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20553" target="_blank">📅 07:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C89rLwE6SZg8zFlts5ElO3fDgJTrf1BPW1qcrtwBwFsoZafx6ZiyQdwmhORX5PGAYbcjwfhvb93ZVKgwEfrWohvUOZR-DpJb85Z4lVsd7Guovxvv6U-U4AxVPXR2kEdYYaNYcmqEjdoM81beTdBlc2GRuNQEQkJ4bDwV5vExXQMC93-3zbHeNPnYbhduAud77qFtbc9q4_-LViPP7Eb7dsMes7GStqTQQWSM1gv5HSuO7X00gpObPRdwywFce-HLBIAOXs4JQskIFrVSQOFgX4oh_f9fCcQt-LzrGMjAycXDDmLdmnf8hI_CgjXd58BfhHNyD0sxpQejrIA2YAacTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20552" target="_blank">📅 07:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c627cc882.mp4?token=rjPHMoFOe6GZ7YcMEscfTJmdlPfXBUj4WykadtVIWzccJy6jEMVNMs-vE1XGPJLgOiIw0tA1R8quBQiTOqpUp3AfwiHmYRWLcSePEHyikM4tIF6aTDjCYfm1I_9ykdtZGCnAILxps5mI5GGHg7SFxoNqsTSK0Mwqzrl5dezHHMmxlYoFkXVze1oRxWVV6KWYaR6UQy5R_1i2fvBJh3dJOE2H-EniIptUAHvvVf37-kG7AoV2kG8paFBudtBrE9Ww7Mw5ayiZBQBsXnavSlQgPUbVQU68dzO50-68n6-V5rJBG67MZFayPfp5gwvWjK0WKEtZay18X1wxSTgDnMX-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c627cc882.mp4?token=rjPHMoFOe6GZ7YcMEscfTJmdlPfXBUj4WykadtVIWzccJy6jEMVNMs-vE1XGPJLgOiIw0tA1R8quBQiTOqpUp3AfwiHmYRWLcSePEHyikM4tIF6aTDjCYfm1I_9ykdtZGCnAILxps5mI5GGHg7SFxoNqsTSK0Mwqzrl5dezHHMmxlYoFkXVze1oRxWVV6KWYaR6UQy5R_1i2fvBJh3dJOE2H-EniIptUAHvvVf37-kG7AoV2kG8paFBudtBrE9Ww7Mw5ayiZBQBsXnavSlQgPUbVQU68dzO50-68n6-V5rJBG67MZFayPfp5gwvWjK0WKEtZay18X1wxSTgDnMX-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران با من تماس گرفت. آنها بزرگترین حمله از زمان جنگ جهانی دوم را نمی‌خواستند.
ما گفتیم: "ترجیح می‌دهم این کار را به این شکل انجام دهم." من به دنبال کشتن مردم و نابودی کامل همه چیز نیستم. و این همان جایی بود که ما به سمت آن می‌رفتیم.
آنها می‌خواستند مذاکره کنند و ما در حال انجام این کار هستیم. و به نظر می‌رسد که این [مذاکره] کاملاً خوب پیش می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20551" target="_blank">📅 07:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8609e5317a.mp4?token=KpzipaWgmL9tEzBYaurq0LGRbigM5WORcFTvkYDsyONlEtoXsPis-E8bXT4vKFFiIpuXXLCE8DtB8ILZTOSyRhRHuclY-PeWoEnKN0UJnS6byDwBYcCMMqTtOxO1ij4iL1Hn5TwzCKYortBhH-QXSPXiIeFAzKUoKeRek55pDuqkOnxLRVAV039SrsAcxSpWaWglD82SCh19hnllfGApNkWedP32x_abs7-2IwZYtwYoSsqQtrD7D1_GV3iWlAqIGBEbsu1SdO4rZgkpNe7KbfV9wA51BQg4liqNEAfFpOC-2-tMnT1lMOZnyEQxo47nhZqn8NEvAhjqZws6e4bPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8609e5317a.mp4?token=KpzipaWgmL9tEzBYaurq0LGRbigM5WORcFTvkYDsyONlEtoXsPis-E8bXT4vKFFiIpuXXLCE8DtB8ILZTOSyRhRHuclY-PeWoEnKN0UJnS6byDwBYcCMMqTtOxO1ij4iL1Hn5TwzCKYortBhH-QXSPXiIeFAzKUoKeRek55pDuqkOnxLRVAV039SrsAcxSpWaWglD82SCh19hnllfGApNkWedP32x_abs7-2IwZYtwYoSsqQtrD7D1_GV3iWlAqIGBEbsu1SdO4rZgkpNe7KbfV9wA51BQg4liqNEAfFpOC-2-tMnT1lMOZnyEQxo47nhZqn8NEvAhjqZws6e4bPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ممکن است این بار با مذاکرات متفاوت باشد؛ ممکن است نباشد.
ما آماده حمله بودیم. در زندگی واقعی، آنها می‌دانند چه زمانی آماده حمله هستید و چه زمانی فقط بلوف می‌زنید.
و اگر مجبور باشیم، آماده حمله هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20550" target="_blank">📅 07:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شبکه i24news درباره تنش‌ها با ایران: "وقتی بازدارندگی آمریکا تضعیف می‌شود، بازدارندگی اسرائیل نیز تضعیف می‌شود."
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20549" target="_blank">📅 07:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9266609aa.mp4?token=NptsGiZmHbnwFzUX9RPObZ9ECkb5t12FuXCxVouN67oRYrZqqjBuKUfC38VJ2VeQS_7fJtt24a43GFiDJxsCOeLPjnvkn8X9ySfC3HdcrCgFOz9J_1LbFgpIUZ0Sxjfw3iv9vfITyU_HRyqOVj5huvNcC0RN9GqnTLOc3EqeqYuzWmkAAmcSIjLC0HeNfC1Os0K93U44RAeCNAjYWpi3sxC1p3FdlZ-y6e8MzqmOPIK1vZZqYzmLlsEPet6ExfIKSagNCfiQKUlpplkTw7-Lzt3QWMTVTt-GHfX0TDcphTl_VzlQIdWmi5YM9HFnCUDf_SzVD14AaASHloj1GbJKZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9266609aa.mp4?token=NptsGiZmHbnwFzUX9RPObZ9ECkb5t12FuXCxVouN67oRYrZqqjBuKUfC38VJ2VeQS_7fJtt24a43GFiDJxsCOeLPjnvkn8X9ySfC3HdcrCgFOz9J_1LbFgpIUZ0Sxjfw3iv9vfITyU_HRyqOVj5huvNcC0RN9GqnTLOc3EqeqYuzWmkAAmcSIjLC0HeNfC1Os0K93U44RAeCNAjYWpi3sxC1p3FdlZ-y6e8MzqmOPIK1vZZqYzmLlsEPet6ExfIKSagNCfiQKUlpplkTw7-Lzt3QWMTVTt-GHfX0TDcphTl_VzlQIdWmi5YM9HFnCUDf_SzVD14AaASHloj1GbJKZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره عبدال السید :
این آدم از یهودی‌ها متنفره. بعضیا می‌گن این حرف تنده، ولی نه؛ از یهودی‌ها و اسرائیل متنفره
عبدال السید! باورش می‌شه؟ فقط برای من همچین چیزی پیش میاد
عبدال السید ظاهرش محترمه، ولی آدم پر از نفرتیه
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20548" target="_blank">📅 07:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=fOmBZpVz8PSZUG7QSS7Fv3o329a4-o08dN0G70BgtHvWJ9JCuVY9iJCPt4Rq2wzqYeHfR5kCh4U_elzsEUOmP21S-OK9ZuBTVB_STjjQyQ66R8_ickjdqbY7LQWs1GQG_qrJGYetlSuNm7R7Bnf_n8OfGRQlBOnYRNsJ-QyPG3SWOneYZCyyHTlekxCQroQBZOvSTfPXHAF1LF6VqoxuUSCBFFT5Y_jvjz1nUlkwFxgWXbxQYKvzJcuNMJZx_oWpBgZAI4uZGtxe-rb1sBJCCg_UWBR1-z1H7f3FYLWGnUrspe3b5zWOI_TXj6AtpVNs6HMQ-R-9ymXCqKjDlzPOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=fOmBZpVz8PSZUG7QSS7Fv3o329a4-o08dN0G70BgtHvWJ9JCuVY9iJCPt4Rq2wzqYeHfR5kCh4U_elzsEUOmP21S-OK9ZuBTVB_STjjQyQ66R8_ickjdqbY7LQWs1GQG_qrJGYetlSuNm7R7Bnf_n8OfGRQlBOnYRNsJ-QyPG3SWOneYZCyyHTlekxCQroQBZOvSTfPXHAF1LF6VqoxuUSCBFFT5Y_jvjz1nUlkwFxgWXbxQYKvzJcuNMJZx_oWpBgZAI4uZGtxe-rb1sBJCCg_UWBR1-z1H7f3FYLWGnUrspe3b5zWOI_TXj6AtpVNs6HMQ-R-9ymXCqKjDlzPOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20547" target="_blank">📅 07:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20546" target="_blank">📅 23:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به گزارش رویترز، به نقل از ۵ منبع:
رژیم ایران به کشورهای خلیج فارس هشدار داده است که هرگونه حمله جدید آمریکا به خاک این کشور، منجر به انتقام‌جویی علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20545" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی: «هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد. اگر آن‌ها…</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20544" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20543" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
