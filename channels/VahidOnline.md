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
<img src="https://cdn1.telesco.pe/file/q-7mrUI3xbkg0NG-lpZN0pQHbunk5CzAGQQ_vPEjc3ikUjpO7c9Rta8Z6fGo6F9bE2mzdbvZ821YbH4mhLmBLa6gxIZULDVAVXQWmZKfzUVLNjkBx1YUN7pjuW5N0cU10-VjO8ME0nyv0W8NlQgcFL9smRN-iSbJdLvezw0OiCEldqvbIv5cameFwouY8vYbNSAbNVbqu8dn_hkYhUARlGP7Elnrvs4e7BFSIZut0t7OYsG1UNCaFWbmI3BL7FGzj__YhXouRZCcz14abt3myKQkEp2TkGnF54SxwdTlkzTBFuyIuzsqHL9OG7m84RswXd2mBxOGcZ5tErnKLB7BmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 09:50:01</div>
<hr>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBTEXic92ypVXEM0mUu_SNcuTV6e4yJ4xVr2bch0KX98-0bvPjDq5WnjA6Y1m6q_4oCRtaEStSXlY_QZUUkxKKLeae5ivqjj4CI2BrE9tvBmjBgbi5oSqNw3Fi6fsHAG1cpo76bdTHzYq5uW3ndZddO4pllKRaeF6jzfg6LyuR39AnSc25GcErXOdyf3JBVzsz3Gb7DFI4Zmc7B6jPoDm4-Gnfkw0OEYXHZv0-mroT0-KMBRcUguirpp1WOGTasKpXtfC_SDKazycsIDGc6cbRwvip7oXMoJFpOj47U0FuyzNi7hxAK-LDCGGDbv0RNJhdfBuqGH93mKuFeJx5OtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
آپدیت: برگشت
پیش از آپدیت:
نرم‌افزار پیام‌رسان «تلگرام»، روز دوشنبه، به‌طور ناگهانی از فروشگاه «اپ‌استور» شرکت اپل در سراسر جهان حذف شد.
بر اساس اعلام کاربران شبکه‌های اجتماعی، جست‌وجوی نام تلگرام در اپ‌استور با هیچ نتیجه‌ای همراه نیست و
صفحات رسمی دانلود
این برنامه با «خطای ۴۰۴» مواجه می‌شوند.
اگرچه این پیام‌رسان روی دستگاه‌هایی که از قبل آن را نصب داشته‌اند کماکان بدون مشکل کار می‌کند، اما امکان
دانلود تازه
یا نصب مجدد آن روی آیفون و آیپد فعلا وجود ندارد.
تاکنون هیچ‌یک از شرکت‌های اپل یا تلگرام بیانیه رسمی درباره دلایل این تصمیم صادر نکرده‌اند و مشخص نیست که این اقدام دائم است یا موقت و آیا ناشی از بررسی‌های قانونی و محتوایی است یا یک نقص فنی.
پیش از این نیز در سال ۲۰۱۸ اپل برای مدتی کوتاه تلگرام را به دلیل «نگرانی از انتشار برخی محتواهای خلاف قوانین» از اپ‌استور خارج کرده بود که پس از اعمال اصلاحات لازم، این برنامه مجددا بازگشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/77726" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HRxdKQxuXSSWHFjc1sOSfbP-MPtlY_OaTbarGXdgOemZXJvIhuZ37GFoqkewYZOz6mJeXtYAubIF-tTRzTIOm121N5PxAUavSglzShW8WcoMYQBKgTBHyrmsag9dEOTVDYhlMyqnTZp0ytBKoEEE-P0WefLN0QNHJVF2ln-cqNm8mcxhDd-2oglahZXcBNu2WTVzHb8jahiXS5_ZGbT5Fk6jTJg9ZNVPXWRZm-K0u2YzlbYbgFLsxV_fmgn1VtWLkfJ7ZtkrZ88L7Kph0BY3dU4gDrHhKlbBFPwfULVqhEH2UwtV_j7mPRNwEMgLABbiqFXgVLj7vR3k3jsNVJufeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  گزارشی درباره وقوع یک حادثه در ۲۰ مایل دریایی شمال‌شرق الخصب در عمان دریافت کرده است.
یک کشتی باری از طریق کانال ۱۶ بی‌سیم VHF اعلام کرده است که با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
مقامات در حال بررسی هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/77725" target="_blank">📅 03:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=cw8tnFY_NRpL6nG_feZWAiPLbz09cqq6YrlnkMvqKHm4vKEEt6PdunMUeQAAqurUBBA9UOFM7P7vwHUiD5n8jBBE_XKYk7SQcFMnydxhJZLc41Kjn28SDFSN_EaipcCTHIOfyCccDc_tf2xJLYfCmC9eGsJc2tSjfCR-p7Ez61e3bms-XonTrJZ2TNMPNHz3ZMRxDwk8mxJW11ZH1RhEqyFqTx1s9jWKTVIwIrTEytx4sEFgpDRjIhzcET_PMRhCLlZQQGh3ZWUqpLqCknxY47kvpTA0LpYeB5xkJImQswi-wSJN_-2oBPXwO0UbTsjIWBoAtFdOEOv1p7bRf9gst2LG5E_mTC8vVEDceRGQZ4xnLBQFgmzN9ArpkcAujP-Ecqnkn8uUuhgN4eIxsd4Oa_36DP6OcWBra6gW__W6odeKYy433RzTYGPpVqogoizAR2VeOq4qlZnGMwkWyyeYEGqZDKGbZwYnFv1OB2cKKQuL8kbRMwic3i7Sw9O4e1n33JjBvS0JmQ86lzLQMxR0ZEXudNuJLcZA0IfYZStdwAbRaeAaggvRI9g6i7Q5FgybCKKIMTSUiPUJH8nlcJ6oWzu03oPj_MgFLXJQ55A0CjzOa4Ub780WlYoPmpiD9J8ART8Hq1gmaCaYevj7ozBE69YsQhJHLiPIO3onvmnZSXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=cw8tnFY_NRpL6nG_feZWAiPLbz09cqq6YrlnkMvqKHm4vKEEt6PdunMUeQAAqurUBBA9UOFM7P7vwHUiD5n8jBBE_XKYk7SQcFMnydxhJZLc41Kjn28SDFSN_EaipcCTHIOfyCccDc_tf2xJLYfCmC9eGsJc2tSjfCR-p7Ez61e3bms-XonTrJZ2TNMPNHz3ZMRxDwk8mxJW11ZH1RhEqyFqTx1s9jWKTVIwIrTEytx4sEFgpDRjIhzcET_PMRhCLlZQQGh3ZWUqpLqCknxY47kvpTA0LpYeB5xkJImQswi-wSJN_-2oBPXwO0UbTsjIWBoAtFdOEOv1p7bRf9gst2LG5E_mTC8vVEDceRGQZ4xnLBQFgmzN9ArpkcAujP-Ecqnkn8uUuhgN4eIxsd4Oa_36DP6OcWBra6gW__W6odeKYy433RzTYGPpVqogoizAR2VeOq4qlZnGMwkWyyeYEGqZDKGbZwYnFv1OB2cKKQuL8kbRMwic3i7Sw9O4e1n33JjBvS0JmQ86lzLQMxR0ZEXudNuJLcZA0IfYZStdwAbRaeAaggvRI9g6i7Q5FgybCKKIMTSUiPUJH8nlcJ6oWzu03oPj_MgFLXJQ55A0CjzOa4Ub780WlYoPmpiD9J8ART8Hq1gmaCaYevj7ozBE69YsQhJHLiPIO3onvmnZSXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مربوط به ایران
متن مکالمه با تشخیص و ترجمه ماشین
:
به دلایلی، وقتی در حال مذاکره‌اند، دوست ندارند بگویند که دارند مذاکره می‌کنند. من می‌گویم: «صبر کنید، ما در حال مذاکره‌ایم. چه اهمیتی دارد؟ داریم مذاکره می‌کنیم.» و آن‌ها گاهی آن را انکار می‌کنند، با اینکه ساعت‌ها و ساعت‌ها کنار یکدیگر می‌نشینند و مذاکره می‌کنند.
مذاکرات در حال پیشرفت است.
قرار بود دیروز آن‌ها را به‌شدت هدف قرار دهیم؛ بسیار بسیار شدید. حمله‌ای شدیدتر از هر حمله دیگری.
فکر می‌کنم می‌توانم بگویم—و ژنرال‌ها از روی آگاهی می‌گویند—شدیدتر از هر حمله‌ای از زمان جنگ جهانی دوم تاکنون. این خیلی بزرگ است.
ما آماده اجرای حمله بودیم که آن‌ها تماس گرفتند. علاوه بر آن، عربستان سعودی تماس گرفت، امارات تماس گرفت، قطر تماس گرفت و افراد بسیاری با من تماس گرفتند. نمی‌خواهم از کلمه «التماس» استفاده کنم، اما به‌ویژه ایران نمی‌خواست هدف حمله قرار بگیرد.
آن‌ها گفتند: «می‌خواهیم مذاکره کنیم. می‌خواهیم درباره تنگه مذاکره کنیم.» اما از دیدگاه من مهم‌تر از آن، می‌خواهیم درباره هسته‌ای‌زدایی ایران مذاکره کنیم، زیرا اصل ماجرا همین است. دلیل اینکه این کار را انجام می‌دهم همین است.
این کار باید مدت‌ها پیش انجام می‌شد. اکنون ۵۰ سال شده است. همیشه می‌گفتیم ۴۷ سال، اما سه سال دیگر نیز گذشته است. ۵۰ سال است که رؤسای‌جمهور دیگر باید کاری را که من انجام می‌دهم، انجام می‌دادند. یا کشورهای دیگر؛ لازم نبود حتماً ما باشیم، اما کشورهای دیگر باید این کار را می‌کردند. هیچ‌کس انجامش نداد و زمان آن فرا رسیده بود.
ما درباره تنگه صحبت می‌کنیم؛ بازشدن تنگه و اینکه به معنای واقعی کلمه تا فردا کاملاً باز باشد. این مرحله اول است.
مرحله دوم این است که پس از آن درباره موضوع هسته‌ای  صحبت کنیم. اساساً هسته‌ای‌زدایی ایران باید انجام شود. باید انجام شود. این مرحله دوم خواهد بود.
اما
مرحله نخست، بازشدن تنگه است. مرحله دوم هسته‌ای‌زدایی خواهد بود. آن مرحله کمی زمان می‌برد، اما ما در این زمینه بسیار قاطع هستیم.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من هرگز موضعم را در این‌باره تغییر نداده‌ام.
درباره کشتیرانی در تنگه هرمز: من اجازه نمی‌دهم از کسی پول بگیرند. ما طرفی هستیم که کنترل کامل را در اختیار دارد. ما کنترل کامل داریم.
می‌دانید، چیزی به نام محاصره داریم که با این نیروی دریایی اجرا می‌شود و به آن «دیوار فولادین» می‌گویند؛ «دیوار فولادین ایالات متحده».
نه، نه، هیچ پولی گرفته نخواهد شد. اصلاً درباره گرفتن پول صحبت نمی‌کنیم. پولی گرفته نخواهد شد.
فکر می‌کنم به این واقعیت بسیار افتخار می‌کنم که به مردم فرصت می‌دهم. به مردم فرصت خواهم داد. انجام حمله‌ای به آن بزرگی علیه یک کشور، تصمیم بسیار بزرگی است. ترجیح می‌دهم اکنون آن را انجام ندهم.
امیدوارم سر عقل بیایند
قرار بود حمله دیشب آغاز شود و مدت زیادی ادامه پیدا کند و در نهایت عملاً چیز بسیار کمی باقی بماند؛ هیچ‌چیز باقی نمی‌ماند.
اگر این فرصت به من داده شود که اجازه دهم افراد زیادی زنده بمانند، می‌خواهم آن فرصت را به آن‌ها بدهم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77724" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e70nx8zwoyTMfVI80GkBEK4zZkxgoHtEXXjOtBXZeHqdI4FDD3VoBRvKlb0WVroxIiV6QsGsErr1RTqVC6b14_ywnALqVH8pFeq4SHbYGoZeDN06WiTQ7Df2i8RAxT-8LX4ul6DdP-t-16iXPGUW1f59Fr5qJK_LUSsdAd_rfSaKtp5KxC9SrNyFFreEagNnFlIcBJOc-6wlFFWieesK47QwFcfqyH827yxEUf8CMKlTCR4DXifAQFJyeqe1PUJf9v4n83i0V6hfM874OMFir64RXqiAPXvOl2Yae7TwnIOKc8otdb-ZZ3CoDNBawDS182SO7xFdlPmKX438SpiXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه ۱۲ مرداد در حاشیه نشستی در کاخ سفید، به خبرنگاران گفت مذاکراتی که در حال حاضر با جمهوری اسلامی ایران جریان دارد، «آخرین فرصت» تهران برای امضای یک «توافق خوب» است.
ترامپ که پیش‌تر حمله‌ای که به گفته او «بزرگ‌ترین حمله نظامی از زمان جنگ جهانی دوم تا کنون» بود علیه ایران را لغو کرده بود، با انتقاد دوباره از مقام‌های جمهوری اسلامی که انجام مذاکره با ایالات متحده را تکذیب کرده بودند، گفت: «ایرانی‌ها تماس گرفتند، بعد از آن از عربستان سعودی، قطر، امارات و بسیاری کشورهای دیگر با من تماس گرفتند که یک فرصت دیگر بدهم. نمی‌خواهم بگویم «التماس» کردند ولی ایران واقعا نمی‌خواست مورد حمله قرار بگیرد.»
ترامپ تاکید کرد که این مذاکرات «با درخواست ایران» و حمایت کشورهای منطقه و جهان انجام می‌شود و «آخرین فرصت» برای جمهوری اسلامی است که انتظارات او درباره برنامه هسته‌ای را برآورده کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77723" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MrvZdYv6LGS3gL0ObTRbXnLxu4asEf9_rS0ZCcIGqGNyBdyib31Ri7C7NahebFQmtlnqrsui7Od31fsYY4MD6lG5KE5Uj-Scqhy_ys_7xUO1fnSFjx9T9EARmU-o20vb_cggYwiFVeG2E7IlL_QXvflWPUT0vK6Uhj64mgftAClfnGB4gP0QMKGhaLABrBfNEv3-fCUSJ2UZCWq9zzVxsw3hKt90-CEN9SX2h3aZ_cyioa8abLd205ymMnkR4ax9Iblin7iRcSntmEGG0awMm9Em4voXk1ar1LkAZVqSXYAon_ssIYjHG9O5pPn0fQp-V44inkBcqcTvkey9TB-Njg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رهبری ایران به‌طرز باورنکردنی دورو است!
آن‌ها درخواست جلسه می‌کنند ــ بعضی‌ها می‌گویند «التماس می‌کنند» ــ مذاکرات آغاز می‌شود و جلسات بیشتری نیز برای آینده بسیار نزدیک برنامه‌ریزی می‌شود، اما بعد آشکارا و با افتخار می‌گویند که هیچ گفت‌وگویی ندارند، درباره هیچ‌چیز صحبت نمی‌شود و فقط با «عمان» سروکار دارند.
سپس همان یاوه‌گویی‌های همیشگی‌شان را ادامه می‌دهند و می‌گویند تنگه هرمز با قدرت توسط آن‌ها اداره خواهد شد، در حالی که این تنگه همین حالا نیز کاملاً تحت کنترل نیروی دریایی ایالات متحده و «محاصره» ما قرار دارد؛ یا همان‌طور که بعضی‌ها می‌گویند، «دیوار فولادین ایالات متحده»!
هیچ‌چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ‌چیز نیز نخواهد رسید، مگر آنکه توافقی حاصل شود یا تسلیم کامل صورت بگیرد. چه ایران بخواهد این را بپذیرد و چه نخواهد، ما در واقع در حال گفت‌وگو درباره راه‌حلی برای مشکلی هستیم که آن‌ها طی چندین دهه ایجاد کرده‌اند.
موضوع بسیار ساده است: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77722" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxjDMEn6UdtLfDjC6ay2zSZG05F0H25niiAt_QDtW_F12SVdsg6dfcfHmEgbtaxEfwUfiWOAh9q1QQKYbHI_40Bt8Pm1U48rEcyPwB4K-zPeOr84Tjwr0mp4pT7rw08nk6RCswGsFiORPyRx5WFh7IaLNOVrinim_gnKZ3QXaPD9G5IrCT30Y_SIuqh_YHhNJd4mUbXCGmNRit1ZfI134ZQuK5J6PRREQzoAHJVka0AaZaHOil5gkmOIa12AN9hCDMoX62gm_U5EcOXc6w8oEceGZ8N6FW2R5Z73r52eGl6-brxWHkfaCClI66_ssZrJgPY1O_8ueMTTkM4H_rA88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیران امور خارجه جمهوری اسلامی ایران و پاکستان در گفت‌وگویی تلفنی درباره تحولات منطقه‌ای و روند تحرکات دیپلماتیک رایزنی کردند. در این تماس، محمد اسحاق دار، وزیر امور خارجه پاکستان، از عباس عراقچی برای سفر به اسلام‌آباد در نخستین فرصت دعوت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77721" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1Yy0g1HyqgrdPhq2Da005Lq-VJ6MHdzRNjvdkeHlA8835TUw_gQvCMjWDr6YYxpWoVG4TUH7HjDadkbLDqc7OyvvZFRpWLz4Pa2FtMI6XfDmoElM0dSKti-AT4vA6iPqT9EgiR-Zzu-4tjVj8nPwe6zWFBgyJMP-rR74iITzB-UsIbF8U4f3u6EbDJ9wVREVMcnA8rprpUHYGEvsza-5cdTk-CtwXFJDwGjk8n29DR94b-xW-b3YNqkcr40DTfuzIBJbOCIAeWpoNnHQ6KP1AAlwWSG57CBbeT9N96TKkIdHvs65t0zu3yCEcGhuJ3fY__T3bZ_nnhhMSwonEIE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز دوشنبه ۱۲ مرداد بار دیگر از شرکت‌های نفتی خواست قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند و مایک ویرث، مدیرعامل شورون، را به‌دلیل قدردانی نکردن از تلاش‌های دولتش در حمایت از صنعت نفت مورد انتقاد قرار داد.
دونالد ترامپ در یک مصاحبه تلویزیونی، ویرث را سرزنش کرد که به نقش دولت او در کمک به شرکت‌های نفتی اشاره نکرده است.
او در پیامی در شبکه اجتماعی خود، تروث سوشال، نوشت: «تنها چیزی که او به‌راحتی از گفتنش صرف‌نظر کرد این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و حتی خود کشور ما نابود می‌شد!»
ترامپ افزود: «برای مثال، آن‌ها مایک و شورون را از ونزوئلا بیرون کردند، اما حالا بازگشته‌اند، بزرگ‌تر و قدرتمندتر از همیشه، و انتظار دارند ثروت هنگفتی به دست آورند!»
به گفته ترامپ، «این موضوع شامل سایر شرکت‌های نفتی هم می‌شود... و همین حالا قیمت نفت برای مصرف‌کننده را پایین بیاورید!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77720" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfxVCSqJ8yWo2_FH2xJGM0VAyqBKGVPTUhZBBYxer2HTGUcQQG6jTHqLZ0mZPxhDbsUOg9JfdVpd5v8mHLEcA9RrgDKvaqYxLkOpdckglqu_86EhMA4lk6QoNZbdwxjVKA9AKbYKYEAMj_1wjLShwFtAQ1XVc66rzwEX84wOyM5SduX4BWcxiEpFy-386Kpa72liGJcqRke7peNYJFbWpmZ0RzERf_CNYlgk9k5FPAXU_ZHDm_VfSP4vww1lsNAhyWp5v-MpuI3ypHRJFTnnDmVsAAzdMYw6sdC2gHYCN6tBZ1PBhx548g1ayDDD_3XEhTKEYySdcvV6NrCQ4hsmoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی‌رغم افزایش امیدها برای دستیابی به پایان درگیری‌ها میان اسرائیل و گروه‌های فلسطینی، مقامات امدادی غزه اعلام کردند حملات هوایی اسرائیل برای دومین روز پیاپی به مناطق مختلف این منطقه در روز یکشنبه یازدهم مرداد، جان دست‌کم ۱۸ فلسطینی را گرفت.
به گفته مقام‌های بهداشتی فلسطینی، از بامداد یکشنبه، جنگنده‌های اسرائیلی شهر غزه در شمال، شهر دیرالبلح در مرکز و منطقه خان‌یونس در جنوب نوار غزه را هدف قرار دادند که بیشترین شمار تلفات روزانه در چند هفته اخیر را بر جا گذاشت.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از دستیابی به یک پیشرفت در تلاش‌ها برای اجرای توافق آتش‌بس سال گذشته خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77719" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqhT9Y1jrYE6jdNph7mNRJAs1T1665juOcrnnNw9Jjq2vCWiRoeS8wilIoBsqmEtVsXdI4mjKUy0YHebIEQlehm44eoA8t10CkCPoNB8TCdwPKMBzSC5FJbItoIsOL9TxpxoEKuzb_IvMaPKgnhpPQWT170Ox_Fzicqz4I5MEWXrBpy5Sl73TZVOWKd9lVo8zknw8hK6Mtmlk0BLUSS4Ck6s5t2ZJ-hNzbELjfqa1JfY0JgKwVT3VF34UlVi8lCbK2DNuXjBM9q53IupAW0FUotKVjeyRQo_jSoXQehsB78XDvjzfyIOXQorbpwP_BN2dYCG4MKAY1HbXrln5B0ZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۱۲ مردادماه گزارش کرد که «سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه» یک پهپاد ام‌کیو۹ را در آسمان تنگه هرمز رهگیری کرده و «مورد اصابت» قرار داده است.
این خبر در حالی اعلام می‌شود که دونالد ترامپ، رئیس جمهوری آمریکا از توقف طرح یک حمله بزرگ به ایران به شرط توافق برای بازگشایی تنگه هرمز و اطمینان از دست نیافتن ایران به سلاح هسته‌ای خبر داده بود.
مرکز فرماندهی ایالات متحده (سنتکام) هنوز واکنشی به این خبر نشان نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/77718" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KK-QELJPhR657AfEXruYUabD-IYklbLFsxNBYP3chCurcx7MzYcX0X3opPP6-i-2JIrTxxrc9W6ejQ5ZTKpRpFfcsOKLfo851ovrwCrTugo5o22_hhb4EcmwfJ6lNfq9Tl7qdYSmfXePHluxFt7CqoAe2UCN5DOGCULyQ0bLz7SDXvsGvVlOheRE67gac3dISjEXd8_qEQz0iU8j0oHdS2Ie0lqtwxuSZ1G4LH4g3p9dsUk2lIN9Wug7RzGvdtdUXSzJ7gY7MUo4FeAnsBwrUhlegW_BwJUl53vYOZ8KdVzck-N4nphj131rJwLsb1l0CIhnSAr5uM3TyQf3jX9McA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=onu851gWCrJOquokYvwK1nXpgqbk4n5Q6ufSK1OzT1Chv7HwmuxqZBmLrCX14KG3xBGaUGbLLcoD7XsOImcaLZerl2Pf9eqYuFkqpayv9uf99w4XSJF5Io2dMJY3O6j3YtJ-U2sl0haxeIPkJhohHBU03rI_cUJxLAClgUSPUTSJMdB8wekeR_WBwoUQguPgj5hSkDPC-iJaPK7irwdtjJXt1JUo-hQmjNvObE7yqeFf-HzikuoT9qyGwyudek4X1b71_ssIJi0pxqYBQ1IvIIxOOpYNK8tjhanhTwF5Hc6npLZEogwvu7Y8Hcafi0jQ1sDxMTJTAxdgOwgNY1Nv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=onu851gWCrJOquokYvwK1nXpgqbk4n5Q6ufSK1OzT1Chv7HwmuxqZBmLrCX14KG3xBGaUGbLLcoD7XsOImcaLZerl2Pf9eqYuFkqpayv9uf99w4XSJF5Io2dMJY3O6j3YtJ-U2sl0haxeIPkJhohHBU03rI_cUJxLAClgUSPUTSJMdB8wekeR_WBwoUQguPgj5hSkDPC-iJaPK7irwdtjJXt1JUo-hQmjNvObE7yqeFf-HzikuoT9qyGwyudek4X1b71_ssIJi0pxqYBQ1IvIIxOOpYNK8tjhanhTwF5Hc6npLZEogwvu7Y8Hcafi0jQ1sDxMTJTAxdgOwgNY1Nv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی، می‌گوید در حال حاضر مذاکره‌ای بین ایران و آمریکا در جریان نیست.
اسماعیل بقائی در نشست هفتگی خود با خبرنگاران در روز دوشنبه ۱۲ مرداد، افزود آنچه در حال حاضر در جریان است، مذاکرات دو جانبه و بین دو دولت ساحلی ایران و عمان است.
او  می‌گوید که «حضور دیگران در این مذاکرات می‌تواند سازنده یا مخرب باشد اما موضوع بین ایران و عمان است.»
اظهارات او در شرایطی بیان می‌شود که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرده که مذاکرات با ایران بعدازظهر دوشنبه ۱۲ مرداد آغاز خواهد شد.
با این حال او روز یکشنبه، هنگام بازگشت از تعطیلات آخر هفته در نیوجرسی به واشینگتن، به خبرنگاران توضیح نداد این مذاکرات در کجا برگزار می‌شود یا چه کسانی در آن شرکت خواهند کرد.
@
VahidHeadline
سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس می‌گوید در حال حاضر «هیچ بحثی» برای مذاکره با آمریکا در دستور کار قرار ندارد.
حسن قشقاوی در گفت‌و‌گویی که خبرگزاری دانشجو منتشر کرده، افزوده که حکومت ایران به‌ویژه در پرونده هسته‌ای، با واشینگتن مذاکره نمی‌کند.
او بدون اشاره به جزئیات افزود: «حتی در مسیر‌های احتمالی دیگر نیز بحث هسته‌ای مطرح نبوده و آینده این پرونده در متون مربوطه کاملاً روشن است».
این نماینده مجلس، اولویت فعلی جمهوری اسلامی را «لغو تحریم‌های اولیه و ثانویه در کنگره و بازگرداندن اموال بلوکه‌شده ایران» عنوان کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/77716" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8TK-JvHxfui-8-Dxl7IMCg9vdFixAI2BtQwVszFM7h5EO8u9qg-hmSroW1zrBd0lptbVWYK4MmdHWxsIbOrQmZUK0uRW_PGkXt2rJJz9oz2UvTyuANFwkbByHM3tERrSxcL6Pt9E_0i82elyr3257bQ7w0oB6vN1iZMdqy3WXBwTH9bh6Qtb5-wEPIQMuIuGSeMAqhR83DqMwnxfrMdO3CkL3CRJKfFptxcZRc0ldngehba7AphGlPwm68BBTLVGKlSywIAscNcZQxJuHkK211Qb4jjqvzB7aJ8eGQVmf0uq-uMhwPXbgT_uI7hQuKfb_rTDYYVcS2ii-rOyt8xyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ آمریکا، روز یکشنبه ۱۲ مردا گفت نیروهای این کشور همچنان در آماده‌باش هستند و آمادگی اقدام دارند؛ اظهاراتی که نشان می‌دهد تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به‌تعویق انداختن حمله به ایران، تأثیری بر آمادگی نظامی نگذاشته است.
پیت هگست در شبکه اجتماعی ایکس و در کنار انتشار ویدئویی از رئیس‌جمهوری آمریکا نوشت: «وزارت جنگ آماده اقدام بود و همچنان در سطحی که از زمان جنگ جهانی دوم دیده نشده، آماده است.» هگست سپس گفت ارتش «کاملاً مسلح و آماده شلیک» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/77715" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYp73IBRojTSfW7MD2ByBdP_gJaSUGTlHbZu6xOP0NapkLZM1jtAG5zM6NFAfQObdMrWZqaC5EU5KPYAtRlcotG8KI_c4jhxCGlCdn0JRbfwxrwuuttrLLoPhpRoGD7bqdWxxrX00f3M9N6BIeTcKnvf9-HotcYOLRdVGmUujMsdaTJOr_X0kWmCdIADUoGrFVxbyz-E9mnb3obqC5HGZq1DWk7ZHl8OaO5xCprGmUJob62Qee_SsUd6Yv_d_QdjjjlIetvNKvxMs9OtuEN-AH2qT84QptDq2ppdkWuDpyJt6kIKxKlO4jYwsmNnZDxyl1MOiNRadrRFy-PjJP0q-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
خبرگزاری فارس از کشف یک خط لوله ۹۰۰ متری غیرمجاز انتقال نفت در استان بوشهر خبر داده و نوشته این لوله نفت سرقت شده را به مخزنی زیرزمینی منتقل می‌کرده است.
به گزارش فارس، فرماندۀ انتظامی استان بوشهر گفته است: «انشعابی با لولۀ ۴۲ اینچی به طول ۹۰۰ متر، و مخزن زیرزمینی ذخیرۀ نفت در شهرستان دشتی استان بوشهر شناسایی» شده است.
این مقام محلی به فارس گفت که «تاکنون بیش از ۵۰ هزار لیتر نفت خام به ارزش ۵۰ میلیارد ریال کشف و تجهیزات» مرتبط با این خط لوله غیرمجاز توقیف شده است.
در این گزارش به مشخصات فرد یا گروهی که در احداث و بهره‌برداری از این خط لوله غیرمجاز نقش داشته‌اند اشاره‌ای نشده است و معلوم نیست آیا آنها شناسایی و تحت تعقیب قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/77714" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7hbIL2ioXBuVT-K_rvczwJaRtLop5hsmUeBxe89Q3l33DQoWaU1j6hWTqKDp9iTARUe6HCrMmYjqRTL72yK4hbHQlNNPbrLB5WvkJL93MvvwrlNP7imy4T2uf3cehkBvIvyUJ10LsTMvI_GsYXsmilK4Cje9aQneJPsBat5C6Whp90A9gwuYI_6zm89iC9m7Z9_dQvpMZBacO446o7xDnNhxOYh-GYxf7V1dXNUYdoBfPO6fDM5ZWlTu3lbf5TxbCg4j6nPzNU9AzDV4j2VTbZtIsNtrWM_xR7WDSTt1S0qR9iZ72by_859BNw4v3lWueGapCpq-Rx10no0dQalIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی نفت دوشنبه ۱۲مرداد۱۴۰۵ پس از اعلام «دونالد ترامپ» مبنی بر توقف حمله نظامی آمریکا به ایران و آغاز دور تازه مذاکرات میان دو کشور، بیش از پنج درصد کاهش یافت.
خبرگزاری «رویترز» گزارش داده که بازارهای جهانی، کاهش احتمال درگیری نظامی در خاورمیانه و افزایش امید به دستیابی به توافق میان تهران و واشنگتن را مهم‌ترین عامل افت قیمت نفت می‌دانند. به نوشته این خبرگزاری، نگرانی معامله گران از اختلال در عرضه نفت و بسته شدن احتمالی تنگه هرمز، پس از اظهارات ترامپ کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/77713" target="_blank">📅 17:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bkrMkAENiGT_EbeqkdcQfm0h_NRv9ph0WmzT1SGmENrmIE7Jl17kQPc-_tPOIq7Fn4qBh8Yn9EZ8bctrB6SoR31RXFmodgfXQw4Pny6sFkWFBmL1LCLKctj8fjbAqmB7AB8V4j6fABTRMDAl21O4leC5vJIZxwt-exWJRAr2x2ezL7cscw91ZUYRF-z4re-UBgrdG3qNW-I6gOaQhPMh2z_m_qfpX_vZbx_T7YhZzos2A7DZRzd-qH-zGhyLo1476HmYhgZgep2QmKV0V1SVnQCYcPyoBr4SV1KRl7Hflw0EwZ4_RwRvJDjjzyE4IMRy9abyuPqh9ruj3qHam7ltjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه وابسته به قوه قضاییه جمهوری اسلامی از اعدام دو زندانی به نام‌های «امید بهزاد» و «پوریا صفوت» به اتهام «جاسوسی» و «همکاری اطلاعاتی» با اسراییل از طریق «ارسال تصاویر مراکز امنیتی و نظامی» جمهوری اسلامی خبر داد.
خبرگزاری میزان، ارگان رسمی قوه قضاییه، اعلام کرد این دو زندانی بامداد دوشنبه ۱۲مرداد اعدام شدند.
به ادعای این نهاد، «بررسی‌های فنی» انجام‌شده روی تلفن همراه امید بهزاد این موارد را تایید کرده و او نیز «در جریان تحقیقات» به آنها اعتراف کرده بود. با این حال، مشخص نیست این اعترافات در چه شرایطی از او گرفته شده است. جمهوری اسلامی طی بیش از ۴ دهه حکومت خود، بارها اقدام به اخذ اعترافات اجباری کرده است.
در گزارش میزان، پوریا صفوت نیز بدون ارائه هیچ‌گونه سند یا جزییاتی، به همکاری «مستقیم با موساد» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77712" target="_blank">📅 17:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=uymAAKH7sXcrpAWK7Nfl2KziRnSrsGsA1IgjKJh66-BbZHlJQFpJ46fyzj--y7o5nC5MvX70H7vJQrgcr66g14-4jruZv1i6Rss_U3mBKOP-A9dDe6Zbm2d2BCTSNHSqCRIn6FYTFjVHHBWVbd9L2OQkkR4wbACBODDZXBvP36zV2conOsfvXjMA_3E-1GlxE7euTAQCjE1D_iNtNj-1jwE1keabHTUfA8e0XSiFL4KsC7nTfFvRXTCB4LMn9FSvomHZWTbvrZST-rEAeFN8V-HGQwbSjBLp5cfUFDI-kdqhX6TNdYlhs_fF65sN16L3_-zS3sf6n_skZJR2HN3im56orV15PnbBP_Abe1q1qXd0fBSbOMHFvTQ-iMIqX4eenorZnQCtCB_Xx3xfBHaqMwJrgp1fRpxPOKIOEDyIy-U2mG_xZTBU8R1QUQCYW8nhfdp1nL9DX4sRkc-3lHIkA_-PHpmnjjUUZtjAvrK9BNmUY-WtMFQ3RPtggboYawIRyvK46YtY9wJ_TIEE-s3sq0ZiRB4CDDec4mhdVNYRAKs9RK-RTTJph46fbP7Z_A2UwuxqLXDCGnMALsMcjB2DhzFawQ8KtQz3jtXvtoC6UPMuucXY0_NBlrESATxd2f5Fv5BieV2M17R8fauANSpWYFiK0UjrTQwoNq12g1WytCI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=uymAAKH7sXcrpAWK7Nfl2KziRnSrsGsA1IgjKJh66-BbZHlJQFpJ46fyzj--y7o5nC5MvX70H7vJQrgcr66g14-4jruZv1i6Rss_U3mBKOP-A9dDe6Zbm2d2BCTSNHSqCRIn6FYTFjVHHBWVbd9L2OQkkR4wbACBODDZXBvP36zV2conOsfvXjMA_3E-1GlxE7euTAQCjE1D_iNtNj-1jwE1keabHTUfA8e0XSiFL4KsC7nTfFvRXTCB4LMn9FSvomHZWTbvrZST-rEAeFN8V-HGQwbSjBLp5cfUFDI-kdqhX6TNdYlhs_fF65sN16L3_-zS3sf6n_skZJR2HN3im56orV15PnbBP_Abe1q1qXd0fBSbOMHFvTQ-iMIqX4eenorZnQCtCB_Xx3xfBHaqMwJrgp1fRpxPOKIOEDyIy-U2mG_xZTBU8R1QUQCYW8nhfdp1nL9DX4sRkc-3lHIkA_-PHpmnjjUUZtjAvrK9BNmUY-WtMFQ3RPtggboYawIRyvK46YtY9wJ_TIEE-s3sq0ZiRB4CDDec4mhdVNYRAKs9RK-RTTJph46fbP7Z_A2UwuxqLXDCGnMALsMcjB2DhzFawQ8KtQz3jtXvtoC6UPMuucXY0_NBlrESATxd2f5Fv5BieV2M17R8fauANSpWYFiK0UjrTQwoNq12g1WytCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، می‌گوید که «مذاکرات جدید» با ایران روز دوشنبه آغاز می‌شود.
آقای ترامپ گفت که در حال حاضر توافقی درباره تنگه هرمز وجود دارد و توافقی هم درباره هسته‌ای زدایی ایران حاصل خواهد شد.
@
VahidHeadline
گفت‌وگوی ترامپ با خبرنگاران در هواپیما
تشخیص و ترجمه ماشین:
🔺
خبرنگار:
چه چیزی باعث شد حملات دیشب را لغو کنید؟
🔻
ترامپ:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند این کار را انجام دهم.
ما تقریباً همین موقع کاملاً آماده اجرای عملیات بودیم و قرار بود حمله‌ای عظیم باشد. همه‌چیز برای اجرا آماده بود. اما وقتی متحدان می‌خواهند حمله را لغو کنید، ناچارید بگویید: «خب، ببینیم چه می‌شود.»
دلیل درخواستشان این است که فکر می‌کنند توافقی وجود دارد. توافقی دربارهٔ [واژه نامفهوم] وجود دارد و بعد هم توافقی درباره موضوع هسته‌ای حاصل خواهد شد؛ یا می‌توانید آن را «هسته‌ای‌زدایی از ایران» بنامید. من آن را هسته‌ای‌زدایی از ایران می‌نامم.
فعلاً آن را متوقف نگه داشته‌ایم. فقط باید ببینیم چه می‌شود. هر زمان بخواهیم می‌توانیم آن را انجام دهیم.
اما سه طرف اصلی از ما درخواست کردند. ایران هم با تأکید زیادی از ما درخواست کرد. گفتند: «مایلیم توافق کنیم.»
حالا نمی‌دانم بیرون چه می‌گویند، چون خیلی وقت‌ها این را به من می‌گویند و بعد بیرون می‌روند و می‌گویند: «نمی‌دانیم او درباره چه حرف می‌زند.»
بدیهی است که نمی‌خواهند مورد حمله قرار بگیرند. آن‌ها از وسعت حمله خبر داشتند، چون [عبارت پایانی نامفهوم است].
🔺
خبرنگار:
حالا چه اتفاقی می‌افتد؟
🔻
ترامپ:
کاری که اکنون انجام می‌دهیم این است که در قالب مذاکره با آن‌ها گفت‌وگو می‌کنیم. مذاکرات فردا بعدازظهر آغاز می‌شود و خواهیم دید آیا واقعیت دارد یا نه.
خیلی دوست دارم این اتفاق بیفتد. جان‌های زیادی نجات پیدا می‌کند و [ادامه جمله نامفهوم است].
سال‌های بسیار زیادی طول می‌کشید تا بتوانند آن را دوباره بسازند؛ البته اگر اصلاً امکان بازسازی‌اش وجود داشت. فکر نمی‌کنم حتی قابل بازسازی می‌بود.
حمله‌ای آماده کرده بودیم که اگر انجام می‌شد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
برای آن‌ها فاجعه‌بار می‌شد و نمی‌خواستند ما آن را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم آن را نمی‌خواست. آن‌ها فکر می‌کردند توافقی قریب‌الوقوع است.
🔺
خبرنگار:
آیا ضرب‌الاجلی وجود دارد، قربان؟
🔻
ترامپ:
توافقی قریب‌الوقوع است که به [واژه نامفهوم] و در نهایت به هسته‌ای‌زدایی از ایران مربوط می‌شود.
وقتی این را می‌شنوم، می‌گویم: «آیا می‌خواهیم تا این اندازه شدید عمل کنیم؟»
گروهی از مردم هستند که می‌خواهند من فوراً این کار را انجام دهم و گروه دیگری از مردم هم هستند که نمی‌خواهند من این کار را انجام دهم.
🔺
خبرنگار:
آقای رئیس‌جمهور، آیا ایران برای رسیدن به توافق ضرب‌الاجلی دارد؟
🔻
ترامپ:
باید ببینیم. ببینیم اوضاع چگونه پیش می‌رود. هر زمان بخواهیم آماده‌ایم وارد عمل شویم.
آیا ترجیح می‌دهم توافق کنم؟ من در پی کشتن مردم نیستم، چون مردم کشته می‌شوند؛ تعداد زیادی از مردم کشته می‌شوند و ما این را نمی‌خواهیم.
بنابراین آن‌ها از ما درخواست کردند؛ مشخصاً ایران. اما آن سه طرف دیگر هم گفتند که واقعاً...
از آن‌ها پرسیدم. [اشاره نامشخصی به پادشاه و سپس ولیعهد.] گفتم: «ترجیح می‌دهید چه کار کنیم؟ ترجیح می‌دهید ما این کار را انجام دهیم یا نه؟»
گفتند: «ما توافق را بسیار بیشتر از حمله ترجیح می‌دهیم، چون نمی‌دانید این [واژه نامفهوم؛ احتمالاً اشاره به حملات یا اقدامات] به کجا منتهی می‌شود.»
آیا کشورشان با ورود سیل‌آسای مردم و فاجعه روبه‌رو خواهد شد؟ اتفاق‌های بد زیادی ممکن است رخ دهد.
🔺
خبرنگار:
قربان، گزارشی منتشر شده است که می‌گوید نیروهای آمریکایی را از بحرین و کویت خارج می‌کنید. آیا نیروها از خاورمیانه خارج می‌شوند؟
[در ترنسکریپت هیچ پاسخی از ترامپ به این پرسش ثبت نشده است.]
....
🔺
خبرنگار:
بازگردیم به ایران؛ آیا آماده بودید اهداف انرژی را هدف حمله قرار دهید؟
🔻
ترامپ:
نمی‌خواهم این را بگویم. نمی‌توانم این را بگویم.
قرار بود حمله‌ای عظیم باشد. قرار بود حمله‌ای باشد که با فاصله بسیار زیاد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
اما از ما خواستند آن را انجام ندهیم. گفتند: «لطفاً این کار را نکنید.»
همسایگانشان هم همین را گفتند.
بنابراین فقط می‌خواهیم ببینیم آیا می‌توانیم درباره هسته‌ای‌زدایی به توافق برسیم یا نه.
🔺
خبرنگار:
[پرسش ناقص درباره اینکه مذاکرات فردا انجام می‌شود.]
🔻
ترامپ:
بله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77711" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77710">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEps9kp26ay3kDhpsT2SzfDPPj_42AajlaS6KHrhaa1EBE89i4AA7E0izfxYLmCT9y-C_EZzWA9XR5bfdDrf88Y8j0HgvKxCEZPluGf6PIy3RJnkjdd6izy7LkUQJK6em_OKc70L48jD4HpKzlurudOiCIT-GzpXW0zX31QnNjNKTaeirN50YnsElRj0LuODfVWmn1d2VqC7dtwlnv3SppPL25oD0P6HWtEDoNHhWiJzI-6nC2vdNY_j3SqHb0WnwIsdTMgCIdpnjuRARMYOkqw6rrP01S8H4DfkbQTbMB4zkzUTfTbRrxWiUTQX9v8Q0Y6vEdgpLARCdal38DQ-Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رییس‌جمهوری ایران، در پیامی یادداشت تفاهم امضا شده میان تهران و واشنگتن را «حاصل خرد جمعی اعضای شعام» توصیف کرد و نوشت: «باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند.»
پزشکیان روز یکشنبه ۱۱ مرداد در شبکه اجتماعی ایکس نوشت: «تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند. باور دارم این تفاهم‌نامه مرکز ثقل روابط خارجی ما در آینده خواهد بود. باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند. امنیت کشور، منطقه و هم‌پیمانان ما با این تفاهم‌نامه ارتقا می‌یابد.»
همزمان، کانال ۱۲ اسراییل به نقل از منابع آگاه گزارش داد کشورهای منطقه در حال میانجیگری برای بازگرداندن آمریکا و ایران به یادداشت تفاهمی هستند که ماه گذشته میان دو طرف امضا شد.
بر اساس این گزارش، توافق پیشنهادی شامل باز ماندن تنگه هرمز به مدت ۶۰ روز بدون دریافت عوارض و تمدید آتش‌بس میان تهران و واشینگتن است. کانال ۱۲ گزارش داد یادداشت تفاهم پیشین به دلیل اختلاف بر سر نحوه مدیریت تنگه هرمز از هم پاشید؛ به گونه‌ای که دونالد ترامپ بر باز بودن کامل این آبراه تاکید داشت، در حالی که تهران معتقد بود این توافق به جمهوری اسلامی اجازه می‌دهد مسیر عبور کشتی‌ها را تعیین کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77710" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عراقچی: مذاکرات ایران و عمان درباره تنگه هرمز به مراحل پایانی رسیده است
🔸
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه خبر داد که مذاکرات با عمان درباره تنگه هرمز به «مراحل پایانی» رسیده است.
🔸
به گزارش خبرگزاری رسمی دولت ایران، ایرنا، عراقچی در جلسه هیئت دولت از وضعیت این گفت‌وگوها گزارشی ارائه داد و اعلام کرد که «مذاکرات در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند».
🔸
هفته گذشته وزارت خارجه ایران گفته بود که مذاکره میان تهران و مسقط همچنان ادامه دارد. این در حالی است که کاظم‌غریب‌آبادی، معاون عباس عراقچی، سه‌شنبه همان هفته اعلام کرد که جمهوری اسلامی پیشنهاد عمان مبنی بر تقسیم برابر مسیرهای عبور و مرور میان دو کشور در تنگه هرمز را رد کرده است.
🔸
پیش از آن، خبرگزاری رویترز پیش‌تر به نقل از یک منبع آگاه گزارش داد که عمان پیشنهادی برای ایجاد یک سازوکار مشترک منطقه‌ای با پرداخت داوطلبانه عوارض یا هزینه‌ عبور و مرور برای مدیریت تنگه هرمز به ایران ارائه کرده است.
🔸
همزمان با انتشار اظهارات روز یکشنبه عراقچی، سخنگوی وزارت خارجه در گفت‌‌وگو با تلویزیونی حکومتی ایران مدعی شد که مذاکره بین ایران و عمان دربارۀ تنگه هرمز «ربطی به باز یا بسته‌شدن تنگه هرمز ندارد».
🔸
اسماعیل بقائی همچنین گفت که مدیریت آینده تنگه هرمز با ایران است و با مشورت عمان انجام می‌شود.
🔸
این مواضع در حالی مطرح شده که دونالد ترامپ، رئیس‌جمهور آمریکا، بامداد یکشنبه اعلام کرد طرح جدید برای حمله به ایران را با درخواست جمهوری اسلامی و کشورهای خاورمیانه و برای تکمیل توافقی که به بازگشایی «فوری، کامل و تمام‌عیار» تنگه هرمز و «پایان تهدید هسته‌ای ایران» منجر شود، متوقف کرده است.
🔸
رسانه‌های ایران به نقل از منابع آگاه حکومتی درخواست از آمریکا برای توقف طرح حمله را رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77709" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X4px1dhN_KLPKLuXfiBkGPNhUbk8vQnGQLhcTtU9BFRjTWdQMTqoiw2A9DycnrXu0ZdO_gM23CsboUqWBUcBDXLgNFQX_xZalJ0JbukMb-L0RfmWej-nHZTn6CprQwp-BTnE2KlMxBUxilDooorvHMeXuQBnp5U_9soQkYN1c4-wfzyHtVYnIO-Y2YwqpTvcZPmYcogalhCrT9dPLzsBs7mEWDsH5SMKM0LC8fC9sIb8qvodL1Samz4T79zOOXOEYXXeo9ehOgS7xRqC0OxoCMPXojT0x-Am1AkIwtzwITKEmHk14CGLFCtTARoedPfejnc1eeMebGqXKxDJGrICKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tLfGRRyOYh5SWhQHyLi4Yc2JAnUWkXfjSry65HJQ03ccKpgHyhybOnFJUdz2GmrYE6gLxkacUovshfkjE6QQ3-m-UrJuZ3V0u6B4dmazyq15aU9RajYE-vsZayFkFW1K3U9dJPXE-6kRoHYVsXJaKyqMDrt7c02jDBHQEsGHd4VuL8Ab8Z4lglDbnplb04fVS53s9nj2w9yWiHNSfUUwAC9C4Yme3KmLhkKgW-sSEnuNe7P8DiyCucIsxU6KSATff0MhY4iYrP0it7OlLe3ZkyGPeA5yTdHgFrgmsQtzizpd66RspsTa2ZjH13T4Gj0IMwDf5xPi0iTfnqt16BFXHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل یک‌شنبه ۱۱ مرداد گزارش داد عباس عراقچی، وزیر خارجه جمهوری اسلامی، شب گذشته با پیشنهاد مصالحه‌ای که میانجی‌های قطری و آمریکا درباره سازوکار بازگشایی تنگه هرمز تدوین کرده بودند، موافقت کرده است.
این شبکه به نقل از دو دیپلمات آگاه از جزئیات مذاکرات گزارش داد پاسخ مثبت عراقچی یکی از دلایلی بود که دونالد ترامپ، رییس‌جمهوری آمریکا، با لغو حمله به ایران موافقت کرد.
@
VahidOOnLine
خبرگزاری فارس به نقل از دو «منبع آگاه» گزارش کانال ۱۲ اسرائیل درباره موافقت عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، با طرح بازگشایی تنگۀ هرمز را تکذیب کرد.
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای ایران به این خبرگزاری گفت هیچ توافقی درباره بازگشایی تنگۀ هرمز حاصل نشده و اخبار منتشرشده در این زمینه «کذب» است.
فارس همچنین به نقل از یک منبع نظامی نوشت تا زمانی که «اقدامات خصمانه آمریکا» ادامه داشته باشد، تنگۀ هرمز مسدود خواهد ماند و عبور شناورها تنها از مسیر اعلام‌شده و با مجوز نیروی دریایی سپاه پاسداران امکان‌پذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77707" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77706">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KK0bwzGAUZAmfuxBmpsIOWHzwiEBN_J2pEeShkHYaYc8DcAfDjNw_lresqc83XwMTd-5A99pF1xA99YGcrUlkKKRXG6wJk-ZhLcFfLfAtAKNcW-A_BegAvaQRyECucxvivtkUxrZYKXX7nWCNM0GK4XAq8VRNfVxCedmIIK-QZyrQZZ_w7CV9AP6HODRNT8Wn8vgrfvCqFFKK8EhCuemTcYZjXP4ZIyZGt7hYcV1iL-CMjSZEUL7_Zu4efbIHHMv6sCCHZGq_D8BVOuQhliXH9CQBE6uc-HBwm5anL_zn8rAAKy3mKXI90DF4pF-lHN8E73K-COCybGUv76ekMyMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در مصاحبه‌ای با فاکس نیوز که لارا ترامپ، عروس رئیس‌جمهور آمریکا، انجام داد، گفت حتی اگر در تهران به‌طور رسمی «تغییر رژیم» رخ ندهد، حکومت ایران «باید» روش خود را تغییر دهد.
وقتی از روبیو پرسیده شد آیا واشینگتن می‌تواند بدون تغییر رژیم در تهران، ایران را «هسته‌ای‌زدایی» کند، او گفت:
«فکر می‌کنم آنچه باید رخ دهد این است که حکومت باید تغییر کند. ممکن است تغییر رژیم نداشته باشید، اما حکومت باید تغییر کند.»
او افزود: «حکومت ایران به‌طور سنتی رویکردی توسعه‌طلبانه در خارج از مرزهایش داشته است. در اصل، دیدگاه آنها این است که نمی‌خواهند فقط بر ایران حکومت کنند؛ می‌خواهند بر منطقه حکومت کنند. آنها می‌خواهند انقلاب را صادر کنند.»
روبیو ادامه داد: «این رویکرد باید تغییر کند و تنها راه تغییر دادن آن این است که هزینه‌اش را آن‌قدر برایشان بالا ببرید که دیگر قادر به پرداخت آن نباشند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77706" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77704">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3938f205b4.mp4?token=AMfkqyq7IafmU8sYXytnFLCY87EqXNUXUPtEGUGrDvXMy9rmjHac0xIBPN89GSfG5bMV7VL-i2zB3z7YneHMVZUE2lg1wSDF5wNBiGIy67QK_c1sOCb5rdOKXgW2K-ZXGHv2xf5sQfLvQs2lDHWGPfO_EXFnVs_tcS9wq-kiUalYTGPNhcv6cvGooKTSdUMjXHcbHG8F2QkSYgWXuOWJJTDSOTsI5Ap1U591-RlLnfB6U-tv71jQxwC610AhJe4c-7BtE-kuU0kf_IQOnalSl1KfSfz4epTIInjPP4-VlmcJgP5Iu6cAFkNddF7SxPbvU8-_r1NWxOGBXt5IIfi_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3938f205b4.mp4?token=AMfkqyq7IafmU8sYXytnFLCY87EqXNUXUPtEGUGrDvXMy9rmjHac0xIBPN89GSfG5bMV7VL-i2zB3z7YneHMVZUE2lg1wSDF5wNBiGIy67QK_c1sOCb5rdOKXgW2K-ZXGHv2xf5sQfLvQs2lDHWGPfO_EXFnVs_tcS9wq-kiUalYTGPNhcv6cvGooKTSdUMjXHcbHG8F2QkSYgWXuOWJJTDSOTsI5Ap1U591-RlLnfB6U-tv71jQxwC610AhJe4c-7BtE-kuU0kf_IQOnalSl1KfSfz4epTIInjPP4-VlmcJgP5Iu6cAFkNddF7SxPbvU8-_r1NWxOGBXt5IIfi_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشر شده در رسانه‌های اجتماعی نشان می‌دهد بامداد روز یک‌شنبه ۱۱مرداد۱۴۰۵ پیکر آروین خیرخواهان معترضی که در جریان اعتراضات دی‌ماه۱۴۰۴ بازداشت و ۱۰مرداد در شاهرود اعدام شد به خاک سپرده شده است.
خاکسپاری در سکوت و تنها با حضور اعضای نزدیک خانواده او انجام شده است.
بازداشت، محاکمه، صدور حکم و اجرای آن برای این شهروند معترض ۲۰ساله در سکوت خبری رخ داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77704" target="_blank">📅 17:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KqSq57gqagy7E7ffdDlckZ24ow7acirnWZMOBjQtCt18oNq4lAOr1aft9cBVjkwRHnUIn7ukYy25bUVep-idK-4Y4Cyab193xOfXsEeDjy5qD2DpUTp56W8mptBoneD9Ryzwf7SzE1XTlRfNrrCb_MKq8JJQTFNFBJ3d7ksDF3JaXsSgE5gk64E-CqnLBPSmhpcOzryxGn57vn6FaYKlkljkjYJc2znLQrrxPzhk9Z6qyQIT-jqg8OBhg92TQq_uzvgwNXcGECv_wRjg4JeU0vZ3-XKgTro3j_MocRGs_axUqVuodsbhmGw6FbZ3nSviv7zPkafuLoRQsxStZlRRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به درخواست ایران و کشورهای منطقه، حمله را برای فراهم شدن زمینه توافق، متوقف کردم
ترجمه ماشین:
ایالات متحده کاملاً مسلح و آماده است تا با جمهوری اسلامی ایران مقابله کند؛ با سطحی از رعب نظامی، توان و قدرت که از زمان جنگ جهانی دوم تاکنون دیده نشده است.
با وجود این، ایران و دیگر کشورهای خاورمیانه همین حالا از ما خواسته‌اند که از هرگونه حمله دست نگه داریم، زیرا بر سر چارچوب‌های یک توافق تفاهم حاصل شده است.
این توافق شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
بر اساس این درخواست، برای منافع آینده جهان و همچنین بقای ایرانی موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانیم به‌سرعت به یک توافق دست پیدا کنیم.
کشور اسرائیل نیز در این تعهد با من همراه است.
همه دست‌به‌کار شوید و کار را تمام کنید. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. is locked and loaded and ready to go against the Islamic Republic of Iran, at levels of Military Terror, Strength, and Power not seen since World War II. Despite this, we have just been asked by Iran, and other Middle Eastern Countries, to hold off any attack in that the perimeters of a deal has been agreed to. This would include the Immediate, Complete, and Total OPENING OF THE HORMUZ STRAIT, and an end to Iran’s  nuclear threat. Based on this request, I have agreed, for the future benefit of the WORLD and, likewise, the survival of a successful and prosperous Iran, to cancel the attack, subject to being able to rapidly make a DEAL. The Country of Israel joins me in this commitment. Get to work, everybody, and get it DONE. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 526K · <a href="https://t.me/VahidOnline/77702" target="_blank">📅 05:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WCtmCHhWJwN7FYIkpnsf8xaCrfgGFOk6CsnLuUY8EJkkkd7XIwzYOg6K49uhPh3VcVwbtNzqN_0dx9u4XX-pPUEb_YZSHrCiBPCM5J9x9_x4GwnLlnzqz7d__sMAOAyUSFIaSpaQZXx_9r90_PO6kvX0lRxp-PyZfQIo_Us56sC-ge5d6K9yTJ6KG7d0Zr1wtoGji-uvJpRahorhFBiWhacL9Xg-n8OaorJ89NDNsKaEO7i2d8P2WXv6b__uqVRtppMRl2XQ50A-Y1FNU2j5NP0SCZe9KTPfBWLxd1-kc_10EZrff6PSOl4vWyTDF796PVmAqHI8lpSPr1UqQnrF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد بن سلمان درباره برنامه‌های ترامپ برای حملات گسترده به ایران ابراز نگرانی کرد
اختصاصی
اکسیوس، ترجمه ماشین:
محمد بن سلمان، ولیعهد عربستان سعودی، روز شنبه با دونالد ترامپ، رئیس‌جمهور آمریکا، گفت‌وگو کرد و درباره برنامه‌های او برای حملات گسترده جدید علیه ایران ابراز نگرانی کرد.
این خبر را دو مقام آمریکایی و یک منبع دیگر مطلع از این تماس اعلام کردند.
چرا اهمیت دارد:
ترامپ در واکنش به حمله موشکی ایران به یک پایگاه آمریکا در اردن و ادامه اختلال ایران در کشتیرانی از طریق تنگه هرمز، به‌طور جدی حمله به اهداف انرژی ایران در روزهای آینده را بررسی می‌کند. او هنوز دستور نهایی را صادر نکرده است.
تصویر کلی:
چنین حمله‌ای ممکن است به تشدید بی‌سابقه جنگ پنج‌ماهه منجر شود؛ جنگی که با باز کردن راه مذاکرات از سوی ترامپ بارها متوقف شده، اما پس از شکست این تلاش‌های دیپلماتیک دوباره از سر گرفته شده است.
جزئیات:
ایران تهدید کرده است که با انجام حملاتی علیه تأسیسات انرژی و زیرساختی در اسرائیل و کشورهای خلیج فارس تلافی خواهد کرد.
▪️
یک مقام آمریکایی به آکسیوس گفت: «سعودی‌ها ابراز نگرانی کردند و خواستار شفاف‌سازی درباره برنامه عملیاتی شدند.»
▪️
یک منبع دیگر مطلع از این تماس گفت محمد بن سلمان از ترامپ خواست تنش‌ها را کاهش دهد و از انجام این حملات خودداری کند.
▪️
کاخ سفید و سفارت عربستان سعودی در واشنگتن از اظهارنظر خودداری کردند.
مرور سریع:
ترامپ روز چهارشنبه با شاهزاده خالد بن سلمان، وزیر دفاع عربستان سعودی که با نام اختصاری «کی‌بی‌اس» شناخته می‌شود، دیدار کرد.
▪️
یک منبع مطلع گفت این دیدار پس از آن به برنامه سفر وزیر سعودی افزوده شد که او با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، دیدار کرد و به او گفت عربستان سعودی خواهان کاهش تنش با ایران است.
▪️
این پیام با وجود حمله مشترک این هفته آمریکا و عربستان سعودی به شبه‌نظامیان طرفدار ایران در عراق منتقل شد.
▪️
این منبع گفت هدف از این دیدارها انتقال دیدگاه‌های محمد بن سلمان درباره جنگ ایران و اوضاع گسترده‌تر منطقه بود.
در پس ماجرا:
عربستان سعودی یکی از مهم‌ترین متحدان واشنگتن در منطقه است. ریاض، با وجود دوره‌هایی از تنش طی پنج ماه گذشته، از زمان آغاز جنگ در چند مقطع حساس بر سیاست ترامپ در قبال ایران تأثیر گذاشته است.
عامل خبرساز:
دیگر قدرت‌های منطقه‌ای، از جمله قطر، امارات متحده عربی، ترکیه و پاکستان نیز آمریکا و ایران را برای کاهش تنش تحت فشار قرار داده‌اند.
▪️
عباس عراقچی، وزیر امور خارجه ایران، روز شنبه با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، که نقش میانجی مهمی میان واشنگتن و تهران داشته است، گفت‌وگو کرد.
▪️
عراقچی همچنین درباره احتمال حملات آمریکا با وزیران امور خارجه ترکیه و عربستان سعودی گفت‌وگو کرد.
▪️
عراقچی، بنا بر بیانیه‌ای در کانال تلگرامی خود، به همتای سعودی‌اش گفت: «هرگونه اقدام خصمانه از سوی آمریکا یا اسرائیل — یا مشارکت یا همکاری کشورهای منطقه در چنین اقداماتی — با پاسخ قاطع و متناسب نیروهای مسلح قدرتمند ایران روبه‌رو خواهد شد.»
آنچه باید زیر نظر داشت:
میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی برای بازگشایی تنگه هرمز، جداگانه با عراقچی، استیو ویتکاف فرستاده کاخ سفید و مقام‌های عمانی گفت‌وگو کردند.
▪️
یک منبع مطلع از مذاکرات گفت این گفت‌وگوها پیشرفت داشته است، اما هنوز مشخص نیست که آیا این پیشرفت برای فروکش کردن بحران کافی خواهد بود یا نه.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 480K · <a href="https://t.me/VahidOnline/77701" target="_blank">📅 03:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DU0iwW8LuRvCkxPqQxVUQbezgfabn4MXmdHaTKLa-q__5COgglFB1t4x1f9sY3LEiyjPBc196gLQWYghOXXkCP_eeZwIANeIU-TF8_KvpggrDRon-3qbIwRnrRGbj6dpo-M9bAXhKnIRFYnmggN5Dj6CciPqGW86s2tvUHM0-3APdgtxlSDV9fm3rLwflt5ffwRTQLQHVbZtXB1mkkVFTXzAss6o-BIfKvxjqfl8OU1vuqGJz3gSgX5fYk1uueD3UZ1ecrDPUDMjQIos1-dZxyyaKGsMo3gah5THy-rUP_KNv1N3TImy4WQWqGL10daBh_5OE2qQj5CH_kivN8NIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با افزایش تنش‌ها میان واشنگتن و تهران، «وای‌نت» روز شنبه گزارش داد، ورود و استقرار بیش از ۳۰ هواپیمای سوخت‌رسان نظامی آمریکا در فرودگاه بن‌گوریون تل‌آویو و افزوده شدن ۱۰ هواپیمای دیگر در روزهای آینده، موجب بروز اختلالات شدید، ترافیک سنگین هوایی و تاخیرهای روزافزون در پروازهای این فرودگاه شده است.
بر اساس گزارش سازمان فرودگاه‌های اسرائیل، میانگین تاخیر پروازها در ترمینال‌های مختلف به بیش از یک ساعت رسیده و دریافت بار مسافران نیز تا دو ساعت معطل شده است. وضعیتی که هم‌زمان با اوج سفرهای تابستانی و نقایص فنی اخیر در سیستم‌های کنترل ترافیک هوایی اروپا، مسئولان را نسبت به تشدید بحران و جدی‌تر شدن اختلالات در پروازهای بین‌المللی نگران کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 473K · <a href="https://t.me/VahidOnline/77700" target="_blank">📅 03:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sEjTCNo-XgWoPiF659aylJ5kQdnAlKevblTpQBO9XRBsmwNd0pc8jAMeB7tPm77sXJZd-LORv6E_6P3Mdn7Mrg7nKYIEFHr5pMXf6TtkyQwq1qtp44JmeUuccNuTF0G3_VcxcWlbqUT1xkZUrKJVGcaPjFUOPnsHl2xtmOcPGANB1VgwNrgjZ3SrC06ZQBKJpAreJlna1YgTZX6tKumWzVjU4bO4S5nVR1qeVZzQqbrSBkA1x_bRXpmYZkawljkIqfadPaD3DZd9naGzrpegk3hV5XzbLektgbkmpM3UiS97YS9RLI4WVGamwcoi_0EBmjQTBTqH3rjqNaH1VfsAqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است
هم‌زمان با افزایش تنش‌ها در منطقه و انتشار گزارش‌هایی درباره احتمال از سرگیری حملات آمریکا علیه جمهوری اسلامی، دونالد ترامپ، رییس‌جمهوری آمریکا، تصویری را در تروث سوشال
منتشر کرد
که به کاهش ارزش ریال و افزایش تورم در ایران اشاره دارد.
در این تصویر با عنوان «ترامپ در حال نابود کردن ارزش پول ایران است» نوشته است که ایران با تورم شدید روبه‌رو است و ارزش هر دلار از حدود ۹۰ هزار تومان به ۱۹۰ هزار تومان افزایش یافته است.
ترامپ توضیح یا اظهارنظر دیگری درباره این تصویر منتشر نکرد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه شنبه دهم مرداد ماه، تصاویر ساخته با هوش مصنوعی را در شبکه تروث سوشال منتشر کرد که او را در لباس رزم جنگ استقلال آمریکا نشان می‌دهد. در مطلب دیگری، تصویری از ناوگان دریایی غرق شده جمهوری اسلامی در زمان ریاست جمهوری او دیده می‌شود.
در یکی از این تصاویر ساختگی، ترامپ با پوشیدن لباس فرماندهان جنگ استقلال آمریکا و در میان دود و آتش نبرد به تصویر کشیده شده است. در تصویری دیگر تحت عنوان «۱۵۹ کشتی ایرانی»، شناورهای نظامی ایران در دوره رییسان جمهوری سابق آمریکا روی آب نشان داده شده‌اند، در حالی که در به دوره ترامپ، تمامی این شناورها در قعر دریا غرق  شده‌اند.
این تصاویر در حالی منتشر می‌شوند که رسانه‌های مختلف از جمله
شبکه ۱۲ تلویزیون اسرائیل
از احتمال حمله گسترده ارتش آمریکا به ایران خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 546K · <a href="https://t.me/VahidOnline/77699" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNyYpUqhHoWsst8Rmv8-mT1AZsK_Sgy13IorvxDAhGyYvi2i5jONtstBvZ2g9HwENFz2vqKgEzAXEqoSIO_djzumiEybiwaESmoeakM7wh1p8z18QApkOlJAplLvb85tGS_v5iXQ8uGKvCCt6cm0ijXWxYmOaXsp9hvAbqZoGqWwYBzltb6wIkViT58ODguRxa4g5gVelTqb18Lp0O7_Kffvr8Nlk4mf0-BFziseHeJdT-ZkO8SFdwkNA-27kWeeBMUoEyA2FibuEkpRvxjVQ9vLCjzws-4aCn-S708sqpzTskMPsnJ03FlAaKBPfaFLJKzouLIfgcZuY1ylFVltmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سحرگاه روز شنبه ۱۰ مرداد ۱۴۰۵، حکم اعدام آروین خیرخواهان، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان شاهرود به اجرا درآمد. این جوان معترض، پیش‌تر از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شده بود.
به گزارش خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، حکم اعدام آروین خیرخواهان حوالی ساعت چهار بامداد امروز اجرا شد.
یک منبع نزدیک به خانواده این زندانی با تایید این خبر به هرانا گفت که مسوولان زندان تاکنون پیکر او را به بستگانش تحویل نداده‌اند. به گفته این منبع، به خانواده اعلام شده است که ساعت سه بامداد فردا برای تحویل پیکر مراجعه کنند و مراسم خاکسپاری نیز باید ساعت پنج بامداد برگزار شود.
آروین خیرخواهان در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت و سپس از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شد. این حکم پس از اعتراض، در دادگاه تجدیدنظر و دیوان عالی کشور نیز بدون تغییر تایید شد.
تاکنون جزییات دقیقی درباره زمان و نحوه بازداشت، مصادیق اتهامی، روند بازجویی، دسترسی این زندانی به وکیل انتخابی و مستندات مورد استناد دادگاه برای صدور حکم اعدام منتشر نشده است.
هرانا نوشته است، آروین خیرخواهان هنگام اجرای حکم اعدام ۱۹ سال و شش ماه سن داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 563K · <a href="https://t.me/VahidOnline/77698" target="_blank">📅 18:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=kTpXUbkMACUe6ybO9EM06UqzYORnamUqHfhbf3zipabfnTHk-6LJvnP-BNT_xcET6FBwbQmaLAdSG_o76PF0DF_LlhxaxQ5bEcfl5FHMJ_sAwV2i3vRznGPDm940rnsUOyzLWcyz3J3HB_b9TamJDYWZMNZ1sgBR2n33fCfcdR5GF4jfUWq4VTZnmHwPKQtMbCb9QXVWOKxnO6_kP55cmv1a8_SwvT2KNrfvQMoFvVzuXeYYnQYWsf-dTkU2GQ9mf2jfFZYh64YhVxEp6SUTlq-xq6YRwiO7J4PLcAY5JYb4EJFZ5s0oX3vXsNXCvLba2I11kGrtZMhCY9yH9FyN3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=kTpXUbkMACUe6ybO9EM06UqzYORnamUqHfhbf3zipabfnTHk-6LJvnP-BNT_xcET6FBwbQmaLAdSG_o76PF0DF_LlhxaxQ5bEcfl5FHMJ_sAwV2i3vRznGPDm940rnsUOyzLWcyz3J3HB_b9TamJDYWZMNZ1sgBR2n33fCfcdR5GF4jfUWq4VTZnmHwPKQtMbCb9QXVWOKxnO6_kP55cmv1a8_SwvT2KNrfvQMoFvVzuXeYYnQYWsf-dTkU2GQ9mf2jfFZYh64YhVxEp6SUTlq-xq6YRwiO7J4PLcAY5JYb4EJFZ5s0oX3vXsNXCvLba2I11kGrtZMhCY9yH9FyN3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر علی منوچهرآبادی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، با انتشار ویدئویی در اینستاگرام، تولد خود را کنار مزار فرزندش جشن گرفت و یاد او را گرامی داشت.
علی منوچهرآبادی، شهروند ۲۵ ساله کُرد اهل کرمانشاه، در جریان اعتراضات دی‌ماه ۱۴۰۴ در محدوده فلکه سوم تهرانپارس با شلیک گلوله جان باخت.
او پسرخاله میثم کُرانیان، از دیگر جان‌باختگان اعتراضات مردمی در کرمانشاه، بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 510K · <a href="https://t.me/VahidOnline/77696" target="_blank">📅 17:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ch082QdNl3Tl2ZPfFAPnZUNDVwtW6SCcPropyT5jH-GPM4N-sJy3ihcAAkOuwiRdChYM_ntPYznHlomqhdjimj_9nR5MmexdHTjAMmpw-iVHSEX1tnIBoTjO6za56Pv_YkZZg82yzUMCOfRCiGo5fE60usxEmGJDWTEA8SN24eMhwZxjOSnZnoV7Pp1cp6O-9AVe4Zhe6l9Lm_qKpvWJ_wQPudX4UFdwHPgCwSMNsI88w_pQnZqJpvU7XHkfd4g81QX2jye357Xb_ZC5G2G0h9txWpILfHWX_nV7Bwnw30226stMofvAEe6oO08zmGnMiKz1H-h5QIfgR2R5wx96ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت ارتش کویت، ترجمه ماشین:
سامانه‌های پدافند هوایی کویت در حال مقابله با حملات پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران، هستند.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان درخواست می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 555K · <a href="https://t.me/VahidOnline/77695" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fCx2_Y5lr4PEp0Ws7851_501yGy7bH8PEQqjywexu1H7Nw8pJuV6HA-xVgCkEaDtCbjYhnrM65QPNlEXANuw7uoGuJVOoW1M2tZk6L_bFsasOVZUNvcSxTdpr67fZmRyH6Dmr5NTr_dWOCKjBRGIo9Me94BSOUtUgJB0fcxxazl-f7Y8WyNeIaKyeTA6rW1MoipiXWwJMxfmLJtOw_Rc4Tu3htExUiYzW8SDywRl5qFcICFmI0xBcV4BTz0dIHJPKVGKa1wy1x0XKksN3w4L5na5tGsf9-BIGPSHODzAiEb9tofWkDPQLdmBLFQLcnmy-6QMMV232lX6SjHfTlu-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا از وقوع یک حادثه دریایی در شمال شرق خصب عمان، در نزدیکی یک نفتکش گزارش داد.
ساعاتی پیش نیز گزارش شد یک نفتکش در ۱۱ مایل دریایی شمال شرقی لیما، در مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 497K · <a href="https://t.me/VahidOnline/77694" target="_blank">📅 09:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJ1ITOflSIVd3n4j-UOVh6O8m0vDFDKyYUmKzRkTfAOSNYzHQMPmmugoyaarIubdbQ5I5azafHDB-Ic0oOTHWnhy-ytimfhLCRIUb2haEJq5xb6BmSpu03mDKf7zJ3toiVMW5JZXBAMcpSB1FAE89pSgPX330BmkL1jOpwam2dclscx98M-lDvAwtPSE7VGqJd6h94njXpdlfbNxbbYjrVV_gWI1J108zjydGzhYVkskH-pjjoknh8KKqfKA2GpNYmtRLGiZxXoIVeJ2-oA7ju1y15AIFQt43lZD_th1VFxNr98WjNX00RvNrDMsHDSnholgRkGsBoi-t6jaqPmUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس گفت: در روز اول جنگ در ۹ اسفند، ما یک‌ساعت بعد از بمباران فهمیدیم که رهبرمان کشته شده است.
او ادامه داد: تا ما توانستیم سران قوه را جمع کنیم و لاریجانی هم بیاید، ساعت هشت شب شد، آن جا تصمیم گرفتیم اعلام خبر مرگ رهبری صبح فردایش باشد. بعد این جلسه هم سریع پراکنده شدیم.
او اضافه کرد: بعدتر تصمیم گرفتیم همان سحرگاه خبر مرگ رهبری را اعلام کنیم و به مردم بگوییم به خیابان بیایید.
قالیباف در حالی می‌گوید که همان ساعت اول از مرگ خامنه‌ای مطمئن شده که مقام‌های جمهوری اسلامی تا بامداد روز بعد خبر مرگ خامنه‌ای را تکذیب کرده و اعلام می‌کردند او در اتاق فرماندهی حضور داشته و مشغول راهبری جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 517K · <a href="https://t.me/VahidOnline/77693" target="_blank">📅 09:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77692">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_MZ_1-Ll3p6YErkZ63UvRnybNOdJLK5a4XPoRbJLbuZECUn9nztgUN5l7QmiK0bkOjJlJw6auwb40akrpVT_zRTmOUWcogPJfMbT1agFcA8YkLypbcjSJBdkDj8if8_fnkC4-H52DGwTPQT63yKVSZ1Bx4wsaWLbSnhCOJgte89_lTl6bNw9Kx7ulNwU5UmqcRJR9zjDLehUPaiXc2DB7_367IuEqAe20JndmUmajydbHhZa2EVhtz7UWPfbEc0bUO_FeNXK41CJP52N2zzQwDQCEa3T5c-95ksCoPuPQZIMuJD-rN8kMyw3syUDcxTIwoerbrqP5gg9yn4lNigUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در حدود ۱۱ مایل دریایی (بیش از ۲۰ کیلومتری) شمال شرقی لیما، در استان مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 498K · <a href="https://t.me/VahidOnline/77692" target="_blank">📅 07:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MULNAZ_MVTCo15Sg_wcvfPnRzsXo4E7cu6Mrv1crZBrIlooxQPK9lKYqwQWCSjemxIWfASRvQcsGnR0Z8Is5P7Okb0t4du8QVHjcBfgECCt1mgEFslkPxs4hxE4p66As_W12dwhz2S26b9vzxptw7NL0a7zV0NA32bHcGQKG8UfPQipjNWHTAucgvICsyts-Vblrgjr9cPMfoEdORU_7nua0-atgPaJ9UkyJWr0IqXgB6oN6xHm9dBU3Jhc10UCtBrn-AI4yH5ccC_glUvmtupGEL8BfvDIGZqLE8Ik6gtq_y8NKmlIf9itDzzNWzxB8ymkeVkPC2lkoMgERyWsKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آمریکایی و اروپایی آگاه به «ان‌بی‌سی» گفتند که روسیه در حال به اشتراک‌گذاری اطلاعات ارزشمند الکترونیکی و ماهواره‌ای با ایران است که به تهران در جنگ جاری با ایالات متحده کمک می‌کند. به گفته این مقامات، ردیابی ماهواره‌ای و اطلاعات سیگنالی روسیه احتمالا ایران را قادر می‌سازد تا نیروهای آمریکایی را در حملات هوایی با دقت بیشتری هدف قرار دهد، دفاع هوایی خود را در برابر حملات ایالات متحده تقویت کند و در عملکرد تسلیحات ساخت آمریکا اختلال ایجاد نماید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 527K · <a href="https://t.me/VahidOnline/77691" target="_blank">📅 03:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ax8OFthcVy6xNaebdI7bSq96Hcv-wtP8qxr59k4SLj5l5kU-0QPCLzGL19496qjR-1PdGkn2SVpTLe19QppLJCSeFHiokddEyY8QGF1AROJ9X-j7eOSEv0F6jUcwcR8ymIRepTdq_so1YK6fSlGI8oD2xcA6EOmLzNZ3Jg-oq_eJWKY77bku8DOlHAS5XVXgAe7wbxDC-UoALwW5jXGNISV0SrNX1ZxtCMC33R4p6iuXzAiM-8WdM6B0iS8tvYqiprz5a70-feGpthlbYa_SRIHlLA5jlQFIFXe_s-KmSuYi2ewbQ_69Xi9JDMKnve97aU3s9kFBFThrMeYreHWrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
ترامپ دستور حمله‌ای تازه به ایران را صادر کرد
"
وال‌استریت ژورنال
به نقل از مقام‌های آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهوری آمریکا، طرح حمله جدید به ایران را که در کمپ دیوید ارائه شده بود، تصویب کرده و این عملیات ممکن است از آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز ادامه یابد.
به گفته این منابع، هرگونه پیشرفت فوری در دیپلماسی یا تغییر نظر ترامپ می‌تواند اجرای حملات را متوقف کرده و مسیر مذاکرات را دوباره باز کند.
این روزنامه نوشت یکی از گزینه‌های مورد بررسی، کارزار دو هفته‌ای حملات هوایی فشرده برای تضعیف توان موشکی جمهوری اسلامی است.
مقام‌های آمریکایی گفتند ترامپ معتقد است توافق موقت صلح کارساز نبوده و همچنان بر توقف برنامه هسته‌ای جمهوری اسلامی و پایان کنترل تهران بر تنگه هرمز اصرار دارد، در حالی که تهران از مواضع خود عقب‌نشینی نکرده است.
وال‌استریت ژورنال افزود مشاوران نظامی ترامپ کاهش ذخایر مهمات آمریکا را یکی از مخاطرات احتمالی این عملیات ارزیابی کرده‌اند.
@
VahidOOnLine
اکسیوس:
ترامپ حمله به اهداف انرژی ایران در چند روز آینده را بررسی می‌کند
ترجمه ماشین: دونالد ترامپ، رئیس‌جمهوری آمریکا، به‌طور جدی در حال بررسی انجام حملاتی علیه اهداف انرژی در ایران طی چند روز آینده است، اما هنوز دستور نهایی اجرای آن را صادر نکرده است؛ یک مقام آمریکایی روز جمعه این موضوع را به اکسیوس گفت.
چرا اهمیت دارد:
هدف از کارزار جدید بمباران آمریکا علیه اهداف انرژی و زیرساختی در ایران، تلاش برای واداشتن ایرانی‌ها به پذیرش شروط ایالات متحده در مذاکرات جاری آتش‌بس خواهد بود.
▪️
این حملات ممکن است برای نخستین‌بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
▪️
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین رسانه‌هایی بودند که درباره حملات احتمالی گزارش دادند.
آنها چه می‌گویند:
ترامپ در آغاز جلسه روز جمعه کابینه به حمله احتمالی اشاره کرد و گفت: «خب، ما خیلی سخت به آنها ضربه خواهیم زد و می‌دانید، بالاخره در مقطعی خواهند گفت که دیگر نمی‌توانیم تحمل کنیم.»
▪️
او افزود هرچه ایالات متحده حملات بیشتری انجام دهد، ایرانی‌ها ضعیف‌تر می‌شوند «و بعد کم‌کم از پا می‌افتند.»
▪️
کارولین لیویت، سخنگوی کاخ سفید، به اکسیوس گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در جلسه کابینه گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 507K · <a href="https://t.me/VahidOnline/77690" target="_blank">📅 01:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u7sFRf6BPB-UTiTyGwkdGQoPEQ27q4m36FP0SyLKeDq_7JNzueMGu1XHBb3rT1MR-IkpILAZfjC3JzruRiQ-g9XxVzxpDwtnGmiXqGV81S2ggr55FnCTBrtbfJJYclr_IHUluM2UUMbZg7dv0UIezDbof4SNd0X5la8uKaL7PjLyjYWcsb9bdpS4EQSL6IbKpO1GKuowu6jchgpUXvFVC0sOoZs4NOxXgOlqJdmUQRww-E7BzM4G7Oivm5tXjHW9seP9c7w57gUgVrABWLGnr0GCl5PLKn55vrJUUxieqzfZzp-q0eHelBg5_T9jI8-SisRYwSSaSyNNShwmEFmknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا و اسرائیل برای بمباران اهداف مرتبط با انرژی در ایران آماده می‌شوند
"
سی‌بی‌اس به نقل از منابع
ترجمه ماشین:
واشنگتن — چندین منبع به سی‌بی‌اس نیوز گفتند که ایالات متحده و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین کارزارهای بمباران تاکنون علیه اهداف زیرساخت‌های انرژی در ایران هستند و احتمال انجام حملات در طول تعطیلات آخر هفته وجود دارد.
بحث‌هایی درباره تلاش برای پایان دادن به عملیات تا زمان بازگشایی بازارهای مالی در روز دوشنبه مطرح شده بود، زیرا نگرانی‌هایی درباره تأثیر بمباران‌ها بر اقتصاد آمریکا و جهان وجود دارد، اما زمان مشخصی برای پایان عملیات قطعی نشده بود.
به گفته چندین منبع آمریکایی، اسرائیلی‌ها در جریان قرار گرفته‌اند و در حال هماهنگی با ایالات متحده هستند. این منابع گفتند رئیس‌جمهور هنوز دستور نهایی آغاز حملات را صادر نکرده است.
سخنگوی دولت اسرائیل به درخواست اظهارنظر پاسخ نداد.
یک عملیات مشترک به معنای بازگشت اسرائیل به عملیات رزمی خواهد بود؛ عملیاتی که این کشور در جریان آتش‌بس میانجی‌گری‌شده از سوی آمریکا متوقف کرده بود. از زمانی که تفاهم‌نامه از هم پاشید و ایالات متحده در اوایل ژوئیه عملیات رزمی را از سر گرفت، ایران اسرائیل را هدف قرار نداده است.
به گفته منابعی که بعداً در جریان قرار گرفتند، طرح حمله نظامی روز جمعه در نشست کابینه دونالد ترامپ، رئیس‌جمهور آمریکا، در کمپ دیوید مطرح شد. یکی از منابع گفت برخی از دستیاران کاخ سفید که بر مسائل سیاسی تمرکز دارند، به‌شدت با این طرح مخالف بودند.
زمانی که خبرنگاران در اتاق حضور داشتند، آقای ترامپ گفت: «ما آن‌ها را بسیار سخت هدف قرار خواهیم داد. بالاخره در مقطعی خواهند گفت: “دیگر نمی‌توانیم تحمل کنیم.”»
او در پاسخ به پرسش خبرنگاران درباره احیای دیپلماسی گفت: «فکر می‌کنم ما فقط می‌خواهیم پیروز شویم.»
دو منبع گفتند زیرساخت‌های انرژی، از جمله نیروگاه‌ها و پالایشگاه‌ها، احتمالاً هدف قرار خواهند گرفت.
کارولین لیویت، سخنگوی مطبوعاتی کاخ سفید، در بیانیه‌ای به سی‌بی‌اس نیوز گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در نشست کابینه خود گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
شان پارنل، سخنگوی ارشد پنتاگون، گفت پنتاگون پیش از آنکه رئیس‌جمهور تصمیم نهایی خود را بگیرد، درباره اهداف اظهارنظر نخواهد کرد.
پارنل در بیانیه‌ای گفت: «وزارت جنگ کاملاً آماده و مهیای عملیات است و می‌تواند در هر لحظه دستورات رئیس‌جمهور را اجرا کند.»
یک مقام پیشین نظامی آمریکا به سی‌بی‌اس گفت، فایده حمله به زیرساخت‌های انرژی این خواهد بود که بر توان نیروهای نظامی ایران برای ارائه خدمات و اداره مؤثر کشور تأثیر بگذارد.
یک مقام ارشد اسرائیلی گفت هنگامی که آقای ترامپ و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اوایل این هفته دیدار کردند، نتانیاهو او را در جریان سه گزینه برای جنگ قرار داد که یکی از آن‌ها حملات نظامی متمرکز بر مسیرهای تدارک‌رسانی زمینی بود. نتانیاهو همچنین با هگست، وزیر دفاع آمریکا، دیدار کرد.
یک مقام آمریکایی گفت ایالات متحده در جریان این درگیری پیش‌تر به پل‌هایی با کاربری دوگانه — که نظامیان و غیرنظامیان از آن‌ها استفاده می‌کردند — حمله کرده است.
روز جمعه گفت‌وگوهایی در سطوح عالی دولت آمریکا درباره قطع برق سراسر تهران انجام شد، اما تا بعدازظهر جمعه هیچ تصمیمی گرفته نشده بود.
هفته گذشته، آقای ترامپ در تروث سوشال نوشت که در ازای هر حمله به یک کشتی در تنگه هرمز، یک پل یا نیروگاه ایرانی را بمباران و نابود خواهد کرد.
این خبر فوری است و به‌روزرسانی خواهد شد.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/77689" target="_blank">📅 00:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aF7yv8PuIwM9Cbvlos8xkfhenNeNyvfBum3EVqnd9s2t0Q-jVxYMr5WSKdFTsyCr19fpVr6PF4UIfNhVTEzhsmYa_huSwJUw8pDon5JzeCngwcUb9L6ADlr7yRDaX-D86x6_TXggVS-rbXVA5r7nXRBm6W4LhN6h6gRBZRHA4mY_ioDhxEy6-5WxfwIrzXf1LjBjqljh1FutohTUgU0AW1mIJ60TCBi3HxLXBH59Wy2SnAPyUkputRFGUhn3c5w0rBGqrPdfSplr45vGINnmpKj4pxp9GlupGrmSapLjuSoifDfmk71YXb1YVP9l9-x4HGc0xDJNazOTPgQUlJ6B0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد. این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های…</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77688" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qieD3rt-ddsaDnpLqD7M3TTORGkCIWIcSW3Af4RcnOVgIHoOrtLHHowrJM-U4kTOGyGHzFKue-rlzDWF5_cS_G8hBfCr6brnuAGwBf5xqYQCsbxZQ3R2OY1KQsOMWD4-RMI_hE9gENkVGULhqkt1VVqZjBU35nmmfzbSaHXnVEJ5JtkPORjDMNn9KTFS53k6zNIvX-PjrS__-6GChCWHuU4sFMH8gbEhMB9wVBNnSlyWDdUREMc81NqFcMJgwJ2LEBSkdVzfhSsaPXZi7VMxJUEpqy_L-GXHDcWZe2GQCurRhCwu0OYN284WhjwTG89gSkwXXEHlVwmBERq5jM7F-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز جمعه ۹مرداد۱۴۰۵
گزارشی تحقیقی
منتشر کرده، از استفاده سپاه از شبکه قمار غیرقانونی ایران که با آن میلیاردها دلار را به رغم تحریم‌ها جابه‌جا می‌کند.در این گزارش به یک صرافی ارز دیجیتال مستقر در دوبی اشاره شده که  به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است.
در گزارش رویترز صرافی مذکور «شل‌بیت» معرفی شده و تایید شده است که این صرافی، یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به فعالیت‌های استخراج بیت‌کوین و بانک مرکزی ایران مرتبط می‌کند.
بنابر گزارش منتشر شده، «شل‌بیت» صدها میلیون دلار ارز دیجیتال را به «بایننس»، بزرگ‌ترین صرافی ارز دیجیتال جهان، منتقل کرده است. دو شرکت تحقیقاتی حوزه ارزهای دیجیتال و یک تحلیلگر مستقل مدارکی ارایه کرده‌اند نشان می‌دهد نشانی ثبت‌شده صرافی بدون مجوز «شل‌بیت» دفتری در بالای یک هتل ارزان‌قیمت در محله‌ای معمولی و نه‌چندان مطرح در دوبی است. این صرافی توسط یک ایرانی مقیم خارج از کشور اداره می‌شود. رویترز اطلاعات ارایه شده در این زمینه را تایید کرده است.
در بخش دیگری از این گزارش آمده است که یکی از مشتریان اصلی «شل‌بیت»، یک شبکه قمار فارسی‌زبان متشکل از بیش از ۲ هزار وب‌سایت است که توسط دو اینفلوئنسر مشهور ایرانی در شبکه‌های اجتماعی تبلیغ و اداره می‌شود. گفته شده که این دو ارتباطاتی در سطوح بالای حکومت ایران دارند.
یکی از آن‌ها در یک ویلای گران‌قیمت در مادرید فعالیت می‌کند و دیگری تا همین اواخر در یک هتل لوکس در هنگ‌کنگ مستقر بود.
هر دو اینفلوئنسر اشاره شده و همچنین فرد اصلی اداره کننده صرافی «شل‌بیت» در سال ۲۰۲۳ در ایران به اتهام مشارکت در یک پرونده قمار غیرقانونی، محکوم شدند.
مطابق قوانین جمهوری اسلامی «قمار کردن» امری غیرقانونی است و مجازات‌های حبس و شلاق برای مرتکبان به‌دنبال دارد با این‌همه گزارش رویترز تایید می‌کند که این شبکه قمار تازه شناسایی شده به سیستم پرداخت آنلاین ایران که مستقیما تحت نظارت بانک مرکزی است دسترسی دارد.
شل بیت بر اساس گزارش رویترز در مرکز عملیاتی است که شبکه قمار، بانک مرکزی و دیگر نهادهای تحریم‌شده ایرانی را به بازارهای جهانی ارزهای دیجیتال مرتبط می‌کند.
یکی از چهره‌های اصلی این شبکه قمار، «ساشا سبحانی»، پسر یک دیپلمات و سفیر پیشین ایران و دیگری «پویان مختاری»، یک چهره مشهور شبکه‌های اجتماعی و خواننده است که پس از اخراج از دوبی در اواخر ماه آوریل، مدتی بین هتل‌های لوکس هنگ‌کنگ جابه‌جا می‌شد.
پویان مختاری اخیرا و در جریان جنگ آمریکا و اسراییل با انتشار ویدیویی گفت که مخالف جمهوری اسلامی نیست و دچار «تحول فکری» شده است.
تحقیقات رویترز آشکار می‌کند که سپاه پاسداران سال‌ها پیش کنترل بزرگ‌ترین وب‌سایت‌های قمار قابل دسترس در ایران را به دست گرفته و از آن زمان تاکنون از این وب‌سایت‌ها برای انتقال پول به خارج از کشور استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77686" target="_blank">📅 22:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sOR94tmZiwURwD4pC71hqoWnrAui7NAbAaqt-8Nq_MkvRwdIXqVDUv1ryzk9n1hRDaQNK0LGQ7QY6YfvRZQUFWOmCaCGiKPYrLb2vyKk7-ul-9Dq7hEWnebyVgUOe1N_z5AG3m898t0vROfRpRy1xRt0Mpz4ed8qyc5-YTSH2OWAZII7Yo3HSJ6m2dfYvwFRioZjfhHyFLigZXfZWvCYyM52ZsZ_97tRiPjsGQm7oJ1Wa52ScwI8D58Y3sBwdZIpsW4wW_vIU_vH81LBY6-E0whUD89sRrP85CSQ2X3pfJHkLYx128tQm6NUWsE4SYubjwk34s3KUQwqYO3RwqhKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N_gVe1lq0SWFlbkOpY4eYOMf0ffpDT2gf_CYrsQQoTzSZPBVXRRT2gM2M3DyTGoObuXksrUSdxMiiif3Ll1HfQy3p8wkIG51eTR4IqPeR39QLS2Za4uzWLZKl325r-Hk_x8WH6sBibgOxbBdalbYqlyXqNuZiSJM_7Wky9epLyBYpJyLPMVvSaFdgOaO91MIzlfggShG8-SMADaFxnx0f_ZguSBAvUe6WCsU8RYEdleFyBSsKMtUQaWC1qpWP9CcLv9pTnOJlnatFuEFFe0zMzO32s1Dpj1ExVGokCsX-pBfBktudIwMM-XOCVhS3blvVR0wYKNQdZV376BwSmgKBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=XxmaexP9ZolxgplZCjHxRrc6mbUQzWO0voUXWLjHNsErDE6N4PbqZXgZDUUmDbQDaWhGUJ7FDTr8yFt49hEBRMutCEIpwGQJHmxfePnJlVY01GuTcHm1Ixu0qEJ6ebjWy1icCQQktx_vCzmes37d9yzuODe3SjoQvpwN1A4Z9DwbAiDv4uuNYikniGBTWXn4K65E5ek--wYk1xB5UsXd9_5RCo7Qf-v5z0xXtw4ioYwaihD3XvcVSh2EBdpVd1Nc5lBIKv1FkmFR9M4DfT-xdWsPTPnbebl42o1wMcLT5PkdPcdzz4JGPOnavT0crSj585P9O95uU3hKcNrUkej4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=XxmaexP9ZolxgplZCjHxRrc6mbUQzWO0voUXWLjHNsErDE6N4PbqZXgZDUUmDbQDaWhGUJ7FDTr8yFt49hEBRMutCEIpwGQJHmxfePnJlVY01GuTcHm1Ixu0qEJ6ebjWy1icCQQktx_vCzmes37d9yzuODe3SjoQvpwN1A4Z9DwbAiDv4uuNYikniGBTWXn4K65E5ek--wYk1xB5UsXd9_5RCo7Qf-v5z0xXtw4ioYwaihD3XvcVSh2EBdpVd1Nc5lBIKv1FkmFR9M4DfT-xdWsPTPnbebl42o1wMcLT5PkdPcdzz4JGPOnavT0crSj585P9O95uU3hKcNrUkej4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد.
این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های اسپانیا، پس از این موج ورود مهاجران، حدود ۳۷ هزار و ۵۰۰ نفر به‌صورت داوطلبانه به مراکش بازگشته‌اند.
در جریان تلاش برای عبور از مرز، دست‌کم ۵۷ نفر جان باختند؛ شماری بر اثر غرق‌شدن و برخی دیگر در ازدحام هنگام عبور از موانع مرزی.
پدرو سانچز، نخست‌وزیر اسپانیا، این رویداد را «نقض حاکمیت ارضی اسپانیا» خواند و گفت روند بازگرداندن مهاجران فاقد مدارک قانونی با همکاری مراکش تسریع خواهد شد.
اتحادیه اروپا در شرایط استثنایی به کشورهای عضو اجازه می‌دهد به‌طور موقت کنترل مرزهای داخلی منطقه شنگن را دوباره برقرار کنند.
@
VahidHeadline
پیش‌تر:
هزاران مهاجر از شامگاه پنج‌شنبه تا صبح جمعه با عبور از مرزهای مراکش وارد مناطق تحت اداره اسپانیا در شمال آفریقا شدند
ورود مهاجران در تمام طول شب ادامه داشته و صبح جمعه نیز همچنان ادامه پیدا کرده است.
همزمان، تصاویر خبرگزاری رویترز، هجوم جمعیتی از مهاجران به گذرگاه مرزی میان مراکش و شهر ملیلیه اسپانیا در شمال آفریقا، را نشان می‌دهد.
در سئوتا، دولت اسپانیا برای مقابله با صدها مهاجری که از مسیر دریا و خشکی وارد این منطقه شده‌اند، یگان‌های نظامی را مستقر کرده است.
تصاویر منتشرشده نشان می‌دهد صدها مهاجر با شنا کردن یا استفاده از تایرهای بادی از سمت مراکش تلاش کرده‌اند خود را به سئوتا برسانند و گروهی دیگر نیز با عبور از یک دروازه مرزی زمینی وارد شهر شده‌اند.
@
VahidOOnLine
وزیر کشور فرانسه روز جمعه اعلام کرد پاریس در پی ورود هزاران مهاجر از مراکش به سئوتا، کنترل‌های مرزی خود با اسپانیا را افزایش خواهد داد.
@
VahidOOnLine
فنلاند اعلام کرد از پیشنهاد ایتالیا برای تعلیق عضویت اسپانیا در منطقه بدون کنترل مرزی شنگن حمایت می‌کند. اقدامی که در پی ورود ده‌ها هزار مهاجر به منطقه سئوتا، تحت حاکمیت اسپانیا در شمال آفریقا، مطرح شده است.
@
VahidOOnLine
پدرو سانچز، نخست‌وزیر اسپانیا، روز جمعه نهم مرداد ماه، ورود گسترده مهاجران به سئوتا، منطقه تحت حاکمیت این کشور در شمال آفریقا، را «نقض و حمله به تمامیت ارضی اسپانیا» محکوم کرد.
سانچز پس از موج اخیر عبور مهاجران از مرز مراکش به سئوتا، این اقدام را محکوم کرد و تاکید کرد دولت اسپانیا از حاکمیت و مرزهای خود دفاع خواهد کرد.
@
VahidOOnLine
ایلان ماسک، میلیاردر آمریکایی و مالک شرکت‌های تسلا و اسپیس‌ایکس، در واکنش به ورود گسترده مهاجران مراکشی به شهر سئوتا در اسپانیا، با انتشار تصاویری از فیلم «جنگ جهانی زد»، این وضعیت را به «آخرالزمان زامبی‌ها» تشبیه کرد و نوشت: «وای، اوضاع اسپانیا واقعا دیوانه‌کننده به نظر می‌رسد!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77680" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نشست خبری دولت ترامپ در کمپ‌دیوید
ویدیوی کامل با زیرنویس فارسی:
۱۰۰ مگابایت
نسخه یک گیگابایتی:
اینجا
متن فارسی ۱۶ بازه از ویدیو
بخش‌هایی از متن لینک بالا:
🔻
ترامپ:
در مینه‌سوتا یک حمله سایبری رخ داده و آن را به ایران نسبت داده‌اند.
فکر نمی‌کنم چنین باشد. من مینه‌سوتا را مقصر می‌دانم، چون به‌شدت بی‌کفایت هستند. حمله‌ای سایبری به ۳۰ تأسیسات آب انجام شد و من مینه‌سوتا و فرماندار فاسد آن را مقصر می‌دانم.
آن‌ها دوست دارند بگویند: «اوه، کار ایران بود.» ایران باید خیلی خوش‌شانس باشد. ایران مشکلات بزرگ‌تری از نگرانی درباره مینه‌سوتا دارد.
....
🔻
ترامپ:
جنگی در جریان است. شاید شما آن را جنگ بنامید؛ من شاید آن را عملیات نظامی بنامم، چون آن‌ها دیگر نیروی دریایی ندارند؛ نابود شده است. نیروی هوایی‌شان نابود شده است. هواپیما ندارند.
بخش بزرگی از موشک‌هایشان از میان رفته است. هنوز مقداری دارند، اما بسیار کمتر از چهار یا پنج ماه قبل. ظرفیت تولیدشان تقریباً از میان رفته و ظرفیت پهپادی‌شان نیز تقریباً نابود شده است.
تعداد بسیار کمی دارند، اما هنوز مقداری باقی مانده است. از نظر من اگر حتی یکی داشته باشند، همان هم بیش از حد زیاد است.
🔻
به ویتنام نگاه کنید؛ ۲۰ سال آنجا بودند. به افغانستان نگاه کنید؛ سال‌های زیادی آنجا بودند. به جنگ کره یا هر جنگ دیگری نگاه کنید؛ سال‌ها طول کشید. ما پنج ماه است وارد شده‌ایم و توان نظامی آن‌ها را نابود کرده‌ایم.
باز هم مقداری برایشان باقی مانده، اما به‌زودی همان مقدار هم باقی نخواهد ماند.
🔻
مارکو روبیو:
نخستین موضوع، دادگاه کیفری بین‌المللی است؛ سازمانی بین‌المللی و نامشروع. خودشان را نامشروع کرده‌اند، چون ادعا می‌کنند حتی اگر عضو آن دادگاه نباشید، باز هم می‌توانند به سراغتان بیایند.
معنای واقعی آن این است که در آینده نظامیان آمریکایی، رهبران سیاسی و افراد دیگر ممکن است از سوی این دادگاه کیفری بین‌المللی تحت کیفرخواست قرار بگیرند. ...
🔻
ترامپ:
هیچ اطلاعاتی وجود ندارد که نشان دهد آن‌ها دنبال من هستند. البته ممکن است چنین اتفاقی بیفتد.
حرف من این است که این یعنی او نمی‌خواهد از من دفاع کند؛ می‌خواهد از بی‌بی و افراد مختلف دیگری دفاع کند.
افراد زیادی هستند که نباید به این شکل با آن‌ها برخورد شود، اما در حال حاضر هیچ نشانه‌ای وجود ندارد که من یکی از آن‌ها باشم.
....
🔻
پیت هگست:
... تعجب می‌کنید چرا حوثی‌ها در این درگیری حضور ندارند، با اینکه نیروی نیابتی ایران هستند؟ چون ۴۵ روز سنگینی قدرت آمریکا را احساس کردند. و شما شجاعت انجام این کار را داشتید.
🔻
اسکات بسنت:
... در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگ‌ترین بانک ایران فروپاشید. بانک مرکزی مجبور شد پول چاپ کند و این باعث تورم شد.
اکنون تورم آن‌ها ۱۸۰ درصد است. قادر به پرداخت حقوق نیروهایشان نیستند و به دستور شما در سراسر جهان به‌دنبال دارایی‌هایشان می‌گردیم.
این پول به مردم ایران و آمریکایی‌هایی می‌رسد که از اقدامات ایرانی‌ها آسیب دیده‌اند؛ چه در ماجرای ناو یو‌اس‌اس کول، چه پادگان‌های لبنان، یا حملات ایرانی‌ها به آن کشتی‌های در حال خروج.
مشارکت در این کار برای من افتخار بوده و مشتاق ادامه آن هستم.
🔽
درباره ادامه جنگ:
🔺
خبرنگار:
آقای رئیس‌جمهور، در ۱۰ روز گذشته حملات میان ایران و ایالات متحده را دیده‌ایم. چگونه آتش‌بس را احیا می‌کنید و دیپلماسی را دوباره از سر می‌گیرید؟
🔻
ترامپ:
فکر می‌کنم فقط می‌خواهیم پیروز شویم. عملکردمان بسیار خوب است. تلاش می‌کنیم تا جایی که در چنین شرایطی ممکن است، ملایم باشیم، اما آن‌ها در حال نابودشدن هستند.
دیگر نیروی دریایی، نیروی هوایی یا پدافند هوایی ندارند. این به آن معنا نیست که هیچ توانی ندارند؛ مقداری دارند، اما بسیار اندک است.
فقط می‌خواهیم پیروز شویم. نمی‌خواهیم آن‌ها این توان را داشته باشند. موضوع بسیار ساده است.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران سلاح هسته‌ای نخواهد داشت و نمی‌تواند داشته باشد. اگر چنین سلاحی داشتند، خاورمیانه تا الان نابود شده بود.
اگر من برجام، همان توافق اوباما، را متوقف و لغو نکرده بودم، آن‌ها اکنون سلاح هسته‌ای داشتند.
فکر می‌کنم اسرائیل دیگر وجود نداشت؛ در بخش‌های بزرگی از خاورمیانه و شاید کشورهای دیگری در قاره‌های مختلف نیز، چون صادقانه بگویم این افراد دیوانه‌اند.
بنابراین نمی‌توانند سلاح هسته‌ای داشته باشند و نخواهند داشت.
🔺
خبرنگار:
[پرسش ناقص و نامفهوم درباره آنچه در چهار یا هشت هفته آینده باید انتظار داشت.]
🔻
ترامپ:
می‌دانید، به آن‌ها حمله خواهیم کرد؛ حملات بسیار سختی به آن‌ها وارد خواهیم کرد. بالاخره در مقطعی خواهند گفت: «دیگر نمی‌توانیم تحمل کنیم.»
🔺
خبرنگار:
آقای رئیس‌جمهور، بازگردیم به ایران. گزارشی منتشر شده که ارتش پیشنهادی داده است تا ظرف ۱۰ یا ۱۴ روز حمله‌ای بزرگ و سخت انجام دهید—
🔻
ترامپ:
ما همین حالا هم حمله بزرگ انجام داده‌ایم. منظورتان از «بزرگ» چیست؟
آن‌ها ۱۵۹ کشتی داشتند؛ تمام نیروی دریایی‌شان همین بود. هر ۱۵۹ کشتی، تمام نیروی دریایی‌شان، در کف دریا قرار دارد. من این را حمله بزرگ می‌نامم.
تسلیحات پدافند هوایی بسیار خوبی داشتند، اما کار نکرد و همه آن از بین رفته است. تمام رادارهایشان از بین رفته، رهبرانشان از بین رفته‌اند؛ همه‌چیز از بین رفته است.
🔻
ترامپ:
برای مثال، خواندید که پنج موشک شلیک شد. سرعتشان ۸۶۰۰ مایل در ساعت بود.
فکرش را بکنید؛ اگر با خودرو ۶۰ مایل در ساعت بروید، کمی سریع به نظر می‌رسد. این موشک‌ها ۸۶۰۰ مایل در ساعت سرعت داشتند و موشک‌های بزرگی بودند. به سوی اردن شلیک شدند و نیروهای ما آنجا بودند: بنگ، بنگ، بنگ، بنگ، بنگ.
[خنده حاضران]
این می‌توانست کلیپ صوتی خوبی باشد! پنج موشک شلیک شد و هر پنج موشک را پیش از آنکه نزدیک شوند، ساقط کردیم. هیچ کشور دیگری چنین توانی ندارد.
🔺
خبرنگار:
آقای رئیس‌جمهور، گفتید هنوز مقداری توان برایشان باقی مانده است. آیا آمریکایی‌ها باید آماده باشند که این حملات متقابل ادامه پیدا کند تا زمانی که ایران دیگر توان حمله فوری نداشته باشد؟
🔻
ترامپ:
ضعیف‌تر خواهند شد. شاید اکنون کمی قوی‌تر شوند، اما ضعیف‌تر خواهند شد.
🔺
خبرنگار:
و بعد به‌تدریج از نفس می‌افتند؟
🔻
ترامپ:
بله، فکر می‌کنم همین‌طور است. احمقانه است که بگویم نه. همیشه باید مراقب باشید.
🔺
خبرنگار:
وضعیت مذاکرات چگونه است؟ چه کسی از طرف دولت در مذاکرات حضور دارد؟
🔻
ترامپ:
آن‌ها همیشه می‌خواهند مذاکره کنند، اما بارها زیر قولشان می‌زنند. استیو در حال مذاکره است. جرد هم هست؛ افراد بسیار خوبی داریم. جی‌دی به‌شدت درگیر است. افراد فوق‌العاده‌ای در حال مذاکره هستند. مارکو هم درگیر است.
افراد بسیار خوبی داریم؛ بهترین‌ها را. اما آن‌ها توافق خواهند کرد.
برای مثال، درباره موضوع هسته‌ای صحبت می‌کنیم و هفت ساعت آنجا می‌نشینیم و درباره برنامه هسته‌ای حرف می‌زنیم. می‌گویم چرا هفت ساعت؟ ده دقیقه کافی است؛ پنج دقیقه وقت دارید، باید حلش کنید.
اما هفت ساعت صحبت می‌کنند، بعد بیرون می‌آیند و من می‌گویم درباره موضوع هسته‌ای گفت‌وگو کردند. آن‌ها بیرون می‌روند و می‌گویند: «ما هرگز درباره موضوع هسته‌ای صحبت نکردیم.»
می‌گویم چرا؟ چرا چنین چیزی می‌گویند؟ تنها کاری که می‌کنند این است که من را عصبانی می‌کنند.
🔺
خبرنگار:
با توجه به آنچه گفتید، باور دارید می‌توان با ایران به توافق رسید؟
🔻
ترامپ:
بله، می‌توان. ببینید، دارم اعتمادم را به آن‌ها از دست می‌دهم، چون دروغ می‌گویند و واقعیت را تحریف می‌کنند.
چند روز پیش پنج موشک شلیک شد. ما آن‌ها را ساقط کردیم، اما در میانه مذاکره بودیم. منتظر تماس استیو بودم تا ببینم مذاکرات چگونه پیش می‌رود؛ در عوض پیت تماس گرفت و گفت: «آن‌ها همین حالا پنج موشک به یکی از پایگاه‌های ما در اردن شلیک کردند.»
خوشبختانه نیروهای ما تجهیزات را به کار انداختند. کارکردن با این تجهیزات بسیار پیچیده است. از این افراد می‌پرسید کجا درس خوانده‌اند و پاسخ می‌دهند ام‌آی‌تی یا کلتک؛ دانشگاه‌هایی که معمولاً با نیروهای نظامی تداعی نمی‌شوند.
افرادی فوق‌العاده باهوش این تجهیزات را اداره می‌کنند. وقتی چنین افرادی نباشند، شلیک‌ها خطا می‌رود، سامانه ایمنی خطا می‌کند یا دقت کافی وجود ندارد. ما افراد فوق‌العاده‌ای داریم.
فکرش را بکنید؛ چند ماه پیش در یک بازه کوتاه ۱۱۱ موشک به سوی ناو هواپیمابر آبراهام لینکلن شلیک شد؛ ناوی بزرگ و زیبا و از نظر طراحی یکی از زیباترین کشتی‌ها.
هر ۱۱۱ موشک مدت‌ها پیش از رسیدن به ناو ساقط شدند. در چند مورد تقریباً همان لحظه‌ای که پرتاب شدند، سرنگون شدند. فناوری باورنکردنی‌ای است.
ناوی که میلیاردها دلار ارزش دارد و موشک‌ها به سوی آن در حرکت‌اند؛ هر ۱۱۱ موشک ساقط شدند. من با افرادی که این کار را انجام دادند صحبت کردم. دوست دارم به افراد پاداش بدهم؛ من رئیس‌جمهورم و با آن‌ها تماس می‌گیرم. آن‌ها کاملاً خونسرد بودند.
🔻
خبرنگار:
آقای رئیس‌جمهور، در دو هفته گذشته سنتکام حملاتی انجام داده است. سنتکام گفته هدف این حملات کاهش توان ایران برای مختل‌کردن تردد در تنگه هرمز بوده است. چند حمله دیگر لازم است تا این توان به‌طور چشمگیری کاهش یابد؟
🔺
ترامپ:
هیچ‌وقت نمی‌توان دانست. بیشتر مردم تا الان تسلیم شده بودند. آن‌ها دیگر نیروی دریایی یا نیروی هوایی ندارند. بیشتر مردم تسلیم می‌شدند، اما آن‌ها نشده‌اند. از این بابت به آن‌ها اعتبار می‌دهم. سرسخت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77678" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qyR_3kIgszH5_XN4TdOcbm_CyPEsS3mYf0Kr_78pRogx8UdvaSrT-hYbdIRG6_EfftOhz-cX0RtGPQzXM9SndU6fgD-gnzJN22_bt2l07UnJ9Ay3a-qZ89zyimsi2pjVSXsRc0sZphWmG8CUxHxsfPDT0-cqQlI2lbcl6WRyEt8H50z3MdMibrpGuJHCvNGXJTDZ4A4fRp2SdBOOBufSDJ0kIMsw3pwwaDg10pV8eYaWjrPZ4L37rUFvbg6WxGkwiBvBhg1Ra39CKecUKL2mZGU02DuyRH_kPosr9F_L4z3nRxwype6CySO7lIibJucQPTZI8O4mKXFe91fkRLwGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: دولت ایران بار دیگر مدعی شده است که تنگه هرمز را بسته است. این ادعا نادرست است.
✅
واقعیت: تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران کنترلی بر آن ندارد. طی چهار ماه گذشته، هزاران کشتی از این آبراه بین‌المللی عبور کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77677" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jY6w5l3h1pO8rqUkWmL9AhoPEvgk2KHPgMPUsFYbXlSdN4f9jqxshGwWeE-MRqHRAvFLYkArWWPOlBz3UC6xMtbeDM5zzwLknYI-RnYimlUC5jaqFCqR9LaS0YwdCCYgXNYKzzSKCnOHj95x1ShNcegMwGI2uDaAR-6p1s2uDe-uLbN6aQX8nyklBlmqo0CInYdiZfjVMVHSIf0MaAY_mHokcvftfeTD4xEpnWgEAZh39jBIsZMt9UC4SCt_41-Tq9y-nZOh4z43DaUlFkEz0v8YuToXG8kwt0-jDvVDV511YCtqZeOaV-fLgvzV1xDNlfqW5GIAq0UEFJGJ9HgmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دوروف، بنیان‌گذار تلگرام، یک روز پس از آنکه اعلام کرد روسیه او را به دلیل مخالفت با درخواست‌های این کشور برای اعمال سانسور و نظارت گسترده بر کاربران، در فهرست «تروریست‌ها» قرار داده است، با انتشار تصویری از ملاقات مقام‌های طالبان با سرگئی لاوروف، وزیر خارجه روسیه، به این اقدام واکنش نشان داد.
دوروف در این تصویر که در شبکه اجتماعی ایکس به اشتراک گذاشت، عکس خود را با برچسب تروریست، کنار تصویری از دیدار مقام‌های روسیه با مقام‌های طالبان قرار داد و زیر عکس دوم نوشت: «شرکای مورداحترام» و برای عنوان این تصویر از عبارت «گیج نشوید» استفاده کرد.
دوروف پیش‌تر در ایکس خبر داده بود که روسیه به دلیل خودداری او از اجرای خواسته‌های این کشور برای نظارت گسترده و سانسور در تلگرام، نامش را در فهرست «تروریست‌ها» قرار داده است.
او همچنین به کنایه نوشت که بر اساس قوانین روسیه از «انتشار اطلاعات در اینترنت» منع شده است و افزود: «به نظر می‌رسد مقام‌های روسیه درباره اینکه چه کسی می‌تواند چه کسی را از اینترنت محروم کند، دچار سردرگمی شده‌اند.»
روسیه تنها کشور جهان است که رژیم طالبان را به رسمیت شناخته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77676" target="_blank">📅 19:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2YTih5skUUb-jhpxmBqOaxr4-TX6J7KyA25nEMBcjfYGu7P1a7aEpYiAga_14xRrBCCDOcU1x5QwKSnl6ysWLkkvf-UdFYeXbMl1OIT_r4B89hr4D4vzAb2pkeqgcj537MtT3_kqv-b7tVXN4xe9IImWRrkeH-NMNK9HAZf0oxJwzjP8Hu-GgubzOQo9GFYmBZAwdD_mv8ASLCurvlKI23EqxfHTkjM_CgVf6RxUHeZpwU_K8Ez9GkZDmk0_n9XnVKPyC72g_3jafBQJUTXJzlQhXAqysxoID5MmBaPxzHLMXAIzV9nNAKBHPKoFgWpxeLPXZICt9HnCPJiorA_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن عاملی، امام جمعه اردبیل، در خطبه‌های نماز جمعه این شهر گفت: «نتانیاهو در دیدار با ترامپ گفته قدر مرا بدان، من جلوی موشکهای جمهوری اسلامی را گرفته‌ام. ایران موشک هشت هزار کیلومتری دارد و به راحتی می‌تواند خانه تو را با موشک بزند. من جلوی ایران را گرفته‌ام.»
او ادامه داد: «ترامپ همیشه از نتانیاهو گول خورده و حالا محل بحث است که آیا این بار هم گول خواهد خورد یا نه.»
امام جمعه اردبیل افزود: «ترامپ پهلوان رسانه‌ای است، عملیات ما کمر او را شکست. او هر وقت شکست می‌خورد به جنگ رسانه‌ای پناه می‌برد و خود را پیروز میدان نشان می‌دهد. اگر این کار را نکند دق می‌کند و می‌میرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77675" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkmerz3Kd1iYhrE48qeGOH00wi8SqHVAbHai6xLOB_lOx-K_mWkpL_ZTNdUsiRwyjzrfysctKr53se3y11XbCIZBoh8T7Ef9Ep3cdsi_LMVs05CY6YO2GviHkMk1qOaSnSg_C11NtvrxkSHHiYYAPG_GORdR0fyCAxibI0P9buB1QqegG9HUYuXwtjCvbfOhD9phAYuI4zqCJ7T6jeLksGNQoVSx4ok4QkPwx3PYyDu2hC5k_kO7YY0YeBXGq5TKwgT5uTE3lK7_m0PICaAjxRfnThY-wbnswIo0iRd6TgnPDMq7cQkygOUR-EDMzh5ggnXIeFhhctafOM342QNvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس‌جمهور آمریکا، روز جمعه ۹مرداد۱۴۰۵ در گفتگو با شبکه «فاکس‌نیوز» گفت درگیری با ایران «به‌خوبی پیش می‌رود» و با اشاره به حملات ارتش ایالات متحده اعلام کرد که ایران در نهایت چاره ای جز عقب‌نشینی و تسلیم نخواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77674" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-ZvlUDhzNMWqsP62aab4h5vJHmQtyNQ0Jp5yIB8dNXE_INHZXu60cAWIv-eizQMFQWyK1Fb1Aupmz8OVY5BkflO4m0CFUUhzQhpHo11oGvGcLH6IpNciv45uwboY34kYh9fDK3cSZaxQpKUltan0lcul7jVBcE7lOA_-6lbowYLQ2Y_7iAJfNkaGhmcwyajSFDvFgbwfkbl4yuyAJChXX4iZcqmlldVmwTzYTDWh9SFIozWzeGYMFVYhWyxvdaoS239kA7VwLmNsqb-4cjyhG1UYuN7bBH1Urw6DGuoJKCm1GvT24QnEfp80QBRRmXgzFJHQqNJ-XAQDF3DenSWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا روز جاری و در میانه تشدید تنش‌های خاورمیانه، نشست کابینه خود را در اقامتگاه کمپ دیوید برگزار می‌کند.
این نشست در شرایطی برگزار می‌شود که دونالد ترامپ در تلاش است راهی برای پایان دادن به جنگ با ایران پیدا کند و همزمان قیمت بنزین را که به تهدیدی برای جمهوری‌خواهان در انتخابات میان‌دوره‌ای نوامبر تبدیل شده، کاهش دهد.
انتظار می‌رود سیاست خارجی و موضوع جمهوری اسلامی بخش عمده دستور کار این نشست را تشکیل دهد. ترامپ درگیر حملات متقابل علیه اهداف نظامی در ایران است.
ترامپ برخلاف برخی رؤسای جمهوری پیشین، در دوره ریاست‌جمهوری خود کمتر به این اقامتگاه کوهستانی ریاست‌جمهوری در غرب ایالت مریلند رفته، و این سومین سفر او به کمپ دیوید در دوره دوم ریاست‌جمهوری‌اش خواهد بود.
@
VahidHeadline
چون جمعه هم هست و بازارهای مالی تعطیل میشن باعث توجه بیشتر هم شده. دیشب، توییتر:
فردا ترامپ قبل از رفتن به باشگاه گلفش در بدمینستر، توقفی در کمپ دیوید داره. در هر دو باری که به کمپ دیوید رفته اتفاق خاصی افتاده. اولینش حمله بمب‌افکن‌های B-2 به نطنز بهمراه داشت، دومیش هم توافق با رژیم...
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77673" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMzdiTXEw7FRzdJRU42RSjzkjJFnkRGAw84VZsCm-lzTSuuFt6d8tAtRLZrJkGixv1HQw4LyGVN31Vtl_F0cpYxqK4_bIuDz4Ap3nSQlo_3FY9rMCn2svsjwJxAnHIirwBBiLHaDP-5HJtHuSmH_Gncrh6RLgLHvecWMMFkFJkxsqJfuDkgXkdwolZjEgHfmHLM04qSpOLtyhLxWIVDz5ndxYyV2ihJXXdpHRx338ssYDtFRNZ9PRRlj_6RaLo5n8CkCBnHTi7hxe6BunDN1Vv3bCZjWmrmPNdMiZ8Q-H5Htx6MflqdlGH_2AfEHK4iYAWXG07Wc-ceuv4GNBLmeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی رسمی وزارت دفاع کویت اعلام کرد نیروهای مسلح این کشور، بامداد روز جمعه نهم مرداد ماه، چند پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده و آنها را منهدم کرده‌اند.
سعود عبدالعزیز العتیبی در بیانیه‌ای در شبکه اجتماعی ایکس نوشت: «تجاوز گناه‌آلود ایران تعدادی از تاسیسات حیاتی و نظامی را هدف قرار داد که اهداف متخاصم رهگیری و منهدم شدند.»
او افزود: «در نتیجه سقوط ترکش‌ها، خسارت‌های مادی وارد شد، اما هیچ تلفات انسانی ثبت نشده است.»
پیش از این بیانیه، ارتش جمهوری اسلامی با انتشار اطلاعیه‌ای از حمله به پایگاه احمد الجابر، محل استقرار ارتش آمریکا با «پهپادهای انهدامی» خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77672" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXHhNlzGkDGisX90Hh3JkxvWAo3NjhzWCzKFxYovx4gK4iKJR0UC6XeOWhBQ4U4PW2v4kHTc5iRNZ1ArQBwhs4kRMcaBnu_iwziHF4KgauX6Ef0uEnTLowKKg9hqprC2gl3e4JOYqg9sFiM3NIcU4vKpf2kOSebg2g4YDCoVsejHvEods58Bk9EADHzFAvftqWYt57hPLPT4tq6ZmLxF9gsddID5DwW042oagf5RqMPCIR1qo3WcUGiTBU-JFqgf96AZd69CK3rpLQt__NqCOgMA-vcFg8xLoxiAyZ_kZ2AmyrvZMpeHnoFX6S1OMhmz0Nbd8zSoYHKzLm8GGmc-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، در پی اعلام فرماندهی مرکزی ارتش آمریکا مبنی بر تکذیب ادعای سپاه دربارهٔ بسته بودن تنگه هرمز، با انتشار بیانیه‌ای دیگر با پافشاری بر ادعاهای قبلی‌اش گفت به دو نفتکش دیگر حمله و آن‌ها را متوقف کرده است.
سپاه در کنار این بیانیه که روز جمعه نهم مرداد منتشر شد، همچنین تصاویری از یک نفتکش را که در میان شعله‌های آتش در تاریکی می‌سوزد منتشر و تاریخ آن را روز جمعه اعلام کرد.
سنتکام بعدازظهر پنج‌شنبه سه ادعای مطرح‌شده از سوی سپاه پاسداران و رسانه‌های نزدیک به آن دربارهٔ بسته بودن تنگه هرمز، انهدام سه جنگنده اف-۳۵ و عبور یک نفتکش ایرانی از محاصره دریایی آمریکا را را «نادرست» خوانده و گفته بود این ادعاها با واقعیت مطابقت ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77671" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=SgEOmllzF2_BcerPsrt_VLFlMuiGWX-STCufTwAbzAwOWgg1k-1yVaEINspY4s3bmQXMqRbAcKm7s4Z6NvCpopempP-ylgZ3vyS4Whry6VVZyjFRhyFZz1dEdNbZUAiucpdPiQZDdv3DJZIqk-JHG95psyPQHuImhKa9wYo0RghBVIIGtNs5tG6771F6DFw8ghrHS5h2lYnzH8MbfbMAXe7sk_As1FrMGq3xJvl_SegG42eWgyEmKM_8IcYYQmiWQjz8iNxVmUASVg6nPZCxo-AUFy2hfrIOhxoqCTzy6DQxUgJg7xXOiH02Dz1tcoYT3xzCFQ3iLH9InGHxeQGymw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=SgEOmllzF2_BcerPsrt_VLFlMuiGWX-STCufTwAbzAwOWgg1k-1yVaEINspY4s3bmQXMqRbAcKm7s4Z6NvCpopempP-ylgZ3vyS4Whry6VVZyjFRhyFZz1dEdNbZUAiucpdPiQZDdv3DJZIqk-JHG95psyPQHuImhKa9wYo0RghBVIIGtNs5tG6771F6DFw8ghrHS5h2lYnzH8MbfbMAXe7sk_As1FrMGq3xJvl_SegG42eWgyEmKM_8IcYYQmiWQjz8iNxVmUASVg6nPZCxo-AUFy2hfrIOhxoqCTzy6DQxUgJg7xXOiH02Dz1tcoYT3xzCFQ3iLH9InGHxeQGymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌تر در صبح جمعه:
ارتش جمهوری اسلامی ایران مدعی شده است بامداد جمعه ۹ مرداد، پایگاه هوایی احمدالجابر در کویت را با پهپادهای انهدامی هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای اعلام کرد در این حمله، آشیانه جنگنده‌ها، سامانه‌های ارتباطات ماهواره‌ای و انبارهای تجهیزات ارتش آمریکا در این پایگاه هدف قرار گرفته‌اند. این ادعا تاکنون از سوی فرماندهی مرکزی آمریکا، سنتکام، یا مقام‌های کویتی تایید نشده است.
احمدالجابر یکی از پایگاه‌های مورد استفاده ارتش آمریکا در کویت است و در گذشته نیز ارتش جمهوری اسلامی بارها از حمله پهپادی به مواضع آمریکا در این کشور خبر داده است. در یکی از حملات پیشین، ارتش جمهوری اسلامی مدعی شده بود ساختمان‌های اداری و سامانه‌های جهت‌یاب در پایگاه عریفجان، محل استقرار بالگردها در اردوگاه العدیری و ساختمان استقرار نیروهای آمریکایی در احمدالجابر را هدف قرار داده است.
ارتش جمهوری اسلامی حمله ادعایی بامداد جمعه را واکنشی به حملات اخیر آمریکا به ایران توصیف کرده است. رسانه‌های ایران پیشتر از حمله آمریکا به بخش‌هایی از جزیره قشم و کشته شدن شماری از غیرنظامیان در این حملات خبر داده بودند.
با این حال، تا زمان انتشار این گزارش، مقام‌های آمریکایی و کویتی درباره وقوع حمله یا میزان خسارت احتمالی آن اظهار نظر رسمی نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77670" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EKYUX8eRbNYefnUQ2mTM_mOfbmF4Wu2tlZe-y8NbucUCp_j6MvPX9jXvlx9f1UDikbpLJygJywVYfnzHXj63Wh-OIroiJbogd9wUapE39ofjOfka83rMK1D53hxujSNwY02j-SjyfyNVwn26u_0TFFBf_9T72Wa9T093cQ45SZJqMeoicqA01gJBCEZCPd_DropTwfSS6aOZIcFo81aZPKJCQtUzm-2V_13KCEWYk-Axw8zundPoJC08A4BJBC550GS32Y2jgPw1jdcTm0bdT-W5UZSQ4Ou9JVYa5ytt7d6DDv9dqD6JnYwViwPZZHtloFcLdzsLH2qGq1oHOTzZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ShNUZru5jrRYkXNhV6o-UwhxPvbgYKgcg_mo3WwWi6Q8gynRzpwjOhuDgdnLbViIzEkA_BKT3NzBDnPZICa3L4bTzQxIBhxxCcw3u_xPqNiLuS2iB47HuSxeHXKfhS3S1YUyKpWxTHJhDMdRjI58bYHi3WUA0uQmX_pY2RS1mQ-1eXEBAhz1so8lb1DcUbq770sjzgkO9LbuBek4RdcEbjw3oslWFGG-_iU4zLFC5BTJw11Rx0v7cID5izEO-92azRFjE79gNJYtrs3ROJsvdOCB0Z5fpbS6u7ReaxJEzRpjR0Lalzj-c89FWbsLiJ283-GnJYF1aVmYqYeq9xTHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DjqMvkqDCwy-PcwB4WkW0lpW3YJrB9yhkHjQcjuAx7uPD_5471O4b0X7Kl5HjI5OAo2uDNEP9NcvNygfbZ_HUeitm7d6KXRhvl7bu73HB4aEz-Yllk2YtC4Qh9ihYfNNjAA8MsuQ6zIFFa2m2aa-Kz-8ESQz7L05eYPI2C96tTHyGK75X045l5WKepcGrNQTMoICoDSgDitDqJG7kcCb1GF9yRcUzqFkjb6DDTBU3Rg5RHaUyvpMC6eEIrUqBiQlq2oZTRALPqOyHcywDOdfpfsMyFWdfABbQoqSNL59h3T5TUMxyB5bww4biiLWA2fiBLkuq99fHJhYhrrdlHCUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hNeOsmWqvL3Jg_gzFJ7djjiZJByO4_GBu05huRlBStSDVKN0BPXVIOvU9_f53B2fJpozn-xTK9J7xP39rARKMoVVnPWurXqVfeQXHxvKW2j1GuGurQOK8wPaeXkwmd8v1pFCpEMWfeWiXRWWnaRkw-ZBlC_7HeL6qC5W90P_9HeAR_E5yjl7lQp_HrP8Vnz_VdU0Tm8kvKJC1WbDYgiEl3THf0BbK93q8THhBftdYTwtYnUEIqOpwRbe9BtoY40v0Ujdoj2bSEdNTSyQTTOjwcOxmy3TIDWzfGqX4Newj0AwrFLD7-fvSQsFaKCaRHsEOhwZ_0BUkM4yo_Z0YqqcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MbRtxTu9WZ2OxSpWYU12oyjsjbEDq-mOdIpd_y1yD6H8QfIZE47GJQyEtuQSBLdbFbAvRg1FoYCQFyO_UWOZvYgSEQuJUW0eeIGYG3qBWzlzmiNT_JKZetODe5AkiCa4q3T9gJIdpJ-0Ogg3ji1tGYpO3SrmJjX02y5U5GW7EbfYFwZVROaiy5yVjaHUD6FvDUtY_ML_FJRdssZtpDkyVIMgbtJzJ0CJ1_gAkDcLOFwdS9hLT_UjjdwEVBZIdvUMWMMewwh5JylLKy4jup7xpXs0tDd8NgIPU78HgqRthYPFhkPoKYo2pmWg8XJgluzh3dfpBHWvsQWHmaWce6FBzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=qVGD66Qbsjjx5gHbuDLRcW1C-hjbxQCONsuFuoln4qh_ibqwKbwkydBmbV9tmDZJtue80U3u8aIHYValwrQ9mE4a0-VhjS9yXrEF2aSxITiIrb0sBa02Fc2EBcECyV76wXWaodLtxlddeeLCq13UsL8oYA_JXKvjLNkC5WH0fywuCT9954aggM6o3yPJwfjqtXg3YqooIPw7zpE2FqI1Lt8XNd9tkifI6ZYqCxSa8DVl4_BtA5IlVIIwuih7kH3AYy7tc2Pm9PjVPceE3pal1tWNkYKw3Msv-VA-rj_eGtYlxEFalPWVHrmuGVcn1nL_MBccF87z1ECv7yllQLgC8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=qVGD66Qbsjjx5gHbuDLRcW1C-hjbxQCONsuFuoln4qh_ibqwKbwkydBmbV9tmDZJtue80U3u8aIHYValwrQ9mE4a0-VhjS9yXrEF2aSxITiIrb0sBa02Fc2EBcECyV76wXWaodLtxlddeeLCq13UsL8oYA_JXKvjLNkC5WH0fywuCT9954aggM6o3yPJwfjqtXg3YqooIPw7zpE2FqI1Lt8XNd9tkifI6ZYqCxSa8DVl4_BtA5IlVIIwuih7kH3AYy7tc2Pm9PjVPceE3pal1tWNkYKw3Msv-VA-rj_eGtYlxEFalPWVHrmuGVcn1nL_MBccF87z1ECv7yllQLgC8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۰:۳۷ درباره پرتاب موشک از یزد
همین الان از یزد موشک فرستادن ساعت10:37
۱۰:۳۵ پرتاب موشک از یزد
سلام الان موشک زدن از یزد
از یزد موشک بلند شد ۱۰:۳۷
از یزد موشک زدن الان
وحید جان همین الان ساعت ۱۰.۳۲ پرتاب موشک از یزد
وحید جان همین الان از یزد موشک زدن
جمعه ساعت ۱۰:۳۶
یزد ۱۰:۳۵ یه موشک زدن
بعد از مدت ها جالب بود سمت جنوب پرتاب شد
همین الان از یزد موشک شلیک کردن
۱۰:۳۷از یزد موشک زدن
همین الان از یزد موشک زدن
جمعه نهم امرداد ساعت۱۰/۳۰
سلام وحید جان همین الان از یزد موشک پرتاب شد
سلام خوبین الان موشک از یزد رفت
شلیک  یک موشک الان از یزد
وحید الان موشک از کشور یزد زدن
همین الان ساعت ۱۰.۳۶ دقیقه از یزد موشک زدن
شلیک موشک از یزد به سمت جنوب
ساعت ۱۰.۳۶
سلام ساعت ۱۰:۳۵ یک موشک از یزد بطرف جنوب کشور شلیک شد
از یزد موشک شلیک کردن ولی مسیر متفاوت از قبل بود
سمت بندر و جنوب میرفت
ساعت ۱۰:۴۰ صبح یزد  موشک پرتاب شد؛ صداش خیلی بلند بود
سلام جمعه ساعت ۱۰:۴۰ از یزد موشک پرتاب شد
۱۰:۳۷ از یزد موشک زدن جمعه ۹مرداد
سلام آقا وحید ۱۰:۴۲ از یزد موشک شلیک کردن
موشک از یزد زدند
وحید جان شلیک موشک از یزد
چند دقیقه پیش
ساعت ۱۰:۳۵ از یزد موشک زدن
از یزد همین الان موشک زدن
امروز جهتش سمت جنوب شرق بود
بر عکس روزای قبل که روی شهر رد میشد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77663" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اکسیوس:
ترجمه ماشین:
ترامپ از توافق «تاریخی» برای خلع سلاح حماس و بازسازی غزه تمجید کرد
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اعلام کرد که «هیئت صلح» او با حماس به توافقی دست یافته است که بر اساس آن، این گروه خلع سلاح می‌شود و کنترل امور غیرنظامی و امنیتی غزه به یک دولت جدید فلسطینی متشکل از تکنوکرات‌ها واگذار خواهد شد.
چرا اهمیت دارد:
در صورت اجرا، این توافق تحولی چشمگیر در طرح صلح ۲۰ ماده‌ای ترامپ برای غزه خواهد بود و مسیر بازسازی این منطقه ویران‌شده را هموار خواهد کرد.
▪️
اما این توافق مستلزم آن است که حماس و اسرائیل طی حدود هفت تا هشت ماه، مجموعه‌ای پیچیده از اقدامات متقابل و مستقل را که اجرای آن‌ها راستی‌آزمایی خواهد شد، به انجام برسانند.
▪️
مقام‌های اسرائیلی همچنان به‌شدت تردید دارند که حماس سلاح‌های خود را تحویل دهد؛ در همین حال، اظهارات یک مقام ارشد حماس نشان می‌دهد که ترتیب خلع سلاح و عقب‌نشینی اسرائیل همچنان ممکن است محل اختلاف باشد.
آنچه می‌گویند:
ترامپ عصر پنج‌شنبه در شبکه تروث سوشال نوشت: «امروز، هیئت صلح به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی گروه‌های مسلح دیگر در غزه دست یافت.»
▪️
او افزود: «این گامی عظیم به‌سوی صلح و امنیت پایدار است.»
وضعیت کنونی:
دو مقام آمریکایی گفتند حماس پس از چند ماه مذاکره با میانجی‌گری قطر، ترکیه و مصر که یک مقام ارشد دولت آمریکا آن را «بسیار حساس» توصیف کرد، با مفاد توافق موافقت کرده است.
▪️
این مقام ارشد آمریکایی گفت انتظار می‌رود اجرای توافق طی هفته‌های آینده آغاز شود.
▪️
یکی از مقام‌های هیئت صلح گفت این نخستین بار است که حماس و دیگر گروه‌های فلسطینی در غزه با غیرنظامی‌کردن این منطقه و واگذاری مسئولیت امنیت و خدمات غیرنظامی به یک دولت تکنوکرات موافقت کرده‌اند.
بر اساس این توافق،
حماس از هرگونه نقش در اداره غزه صرف‌نظر خواهد کرد. «کمیته ملی اداره غزه» موسوم به NCAG به‌عنوان جایگزینی برای حماس و تشکیلات خودگردان فلسطینی فعالیت خواهد کرد.
▪️
مقام ارشد آمریکایی گفت: «این ساختار به نفع مردم غزه خواهد بود.»
بررسی واقعیت:
غازی حمد، از مقام‌های حماس، در گفت‌وگو با الجزیره تأیید کرد که مذاکرات «دشوار» به توافق منجر شده است، اما توضیحات او بلافاصله پرسش‌هایی را درباره نحوه اجرای آن مطرح کرد.
▪️
حمد گفت: «ما پیش از عقب‌نشینی اسرائیل از نوار غزه هیچ اقدامی در زمینه خلع سلاح انجام نخواهیم داد.» او افزود که کمیته ملی اداره غزه بدون دخالت اسرائیل خلع سلاح را اجرا خواهد کرد.
▪️
این موضع ظاهراً با توصیف ترامپ از یک روند مرحله‌ای و «با ساختاری دقیق» تفاوت دارد؛ روندی که در آن، هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی می‌کنند.
▪️
مقام‌های آمریکایی و هیئت صلح گفتند اجرای توافق از طریق اقدامات متقابل و مستقلی که راستی‌آزمایی می‌شوند پیش خواهد رفت، هرچند اذعان کردند که جدول زمانی عقب‌نشینی اسرائیل هنوز در حال نهایی‌شدن است.
تصویر کلی:
بخش‌های وسیعی از غزه در جریان جنگ ویران شده و بیشتر جمعیت دو میلیون نفری آن همچنان در چادرها یا سرپناه‌های موقت زندگی می‌کنند.
▪️
مواد غذایی و دیگر کمک‌ها در حجم زیادی وارد غزه می‌شود، اما وضعیت انسانی همچنان وخیم است.
▪️
وزارت بهداشت غزه که تحت کنترل حماس است می‌گوید از زمان آتش‌بس ۱۰ اکتبر ۲۰۲۵، نزدیک به ۱۲۰۰ فلسطینی کشته شده‌اند. برخی از آن‌ها از نیروهای حماس بودند، اما بسیاری دیگر غیرنظامی، از جمله کودکان، بوده‌اند.
نگاهی نزدیک‌تر:
این توافق بر این اصل استوار است که غزه باید یک دولت، یک نظام حقوقی و یک مرجع امنیتی مشروع داشته باشد. انتظار می‌رود روند غیرنظامی‌سازی بین ۲۰۰ تا ۲۵۰ روز طول بکشد و هر بار در یکی از بخش‌های غزه اجرا شود.
▪️
پلیس غیرنظامی حماس ابتدا سلاح‌های خود را به یک نیروی پلیس جدید فلسطینی زیر نظر دولت تکنوکرات تحویل خواهد داد.
▪️
پس از آن، سلاح‌های سنگین حماس از رده خارج و در انبارهای امن نگهداری خواهد شد و تونل‌ها و کارخانه‌های تولید سلاح این گروه برچیده خواهد شد.
▪️
سلاح‌های سبک مطابق قوانین فلسطینی جمع‌آوری خواهد شد.
▪️
تمامی گروه‌های شبه‌نظامی دیگر در غزه، از جمله گروه‌های مخالف حماس که اسرائیل در جریان جنگ آن‌ها را مسلح کرده بود، نیز ملزم به تحویل سلاح‌های خود خواهند بود.
کمیته ملی اداره غزه
تنها زمانی کنترل هر منطقه را در دست خواهد گرفت که یک سازوکار نظارتی تأیید کند تعهدات مربوط به آن منطقه اجرا شده است.
▪️
مقام هیئت صلح گفت در پایان این روند، دولت تکنوکرات و نیروی پلیس آن انحصار سلاح در غزه را در اختیار خواهند داشت.
نحوه اجرا:
بر اساس توافق، یک نیروی بین‌المللی تثبیت‌کننده به آموزش پلیس جدید فلسطینی کمک خواهد کرد، در جمع‌آوری سلاح‌ها مشارکت خواهد داشت و میان مناطق تحت کنترل فلسطینی‌ها و نیروهای اسرائیلی مستقر خواهد شد.
▪️
یکی از مقام‌های هیئت صلح گفت این توافق بر مبنای «اعتماد صفر» طراحی شده است، زیرا حماس و اسرائیل از همان ابتدا به‌صراحت اعلام کردند که به یکدیگر اعتماد ندارند.
▪️
این روند تا زمانی که ناظران تأیید نکنند هر دو طرف به تعهدات خود عمل کرده‌اند، از یک مرحله به مرحله بعدی منتقل نخواهد شد.
▪️
این مقام گفت هدف آن است که از وضعیتی جلوگیری شود که دولت تکنوکرات در طول روز غزه را کنترل کند، اما گروه‌های مسلح شب‌ها همچنان قدرت را در دست داشته باشند.
طرف مقابل:
عقب‌نشینی اسرائیل به‌تدریج و بر اساس جدول زمانی‌ای انجام خواهد شد که هنوز در حال نهایی‌شدن است.
▪️
ترامپ گفت هم‌زمان با تکمیل خلع سلاح و برعهده‌گرفتن مسئولیت امنیت از سوی نیروی بین‌المللی و پلیس جدید فلسطینی، نیروهای اسرائیلی عقب‌نشینی خواهند کرد.
▪️
اسرائیل همچنین عملیات نظامی و ترورهای هدفمند در غزه را متوقف خواهد کرد، مگر در مواردی که تهدیدی قریب‌الوقوع وجود داشته باشد.
▪️
مقام هیئت صلح گفت: «تمامی فعالیت‌های نظامی در غزه باید متوقف شود؛ چه از سوی اسرائیل و چه از سوی حماس.»
پشت درهای بسته:
مقام ارشد آمریکایی گفت دولت ترامپ در تمام طول مذاکرات هماهنگی نزدیکی با اسرائیل داشته است.
▪️
دولت آمریکا همچنین قصد دارد با وجود تردید اسرائیل درباره خلع سلاح حماس، اطمینان حاصل کند که اسرائیل به تعهدات خود در چارچوب توافق عمل می‌کند.
▪️
این مقام گفت: «ما از اسرائیل چیزی جز اجرای تعهداتش در چارچوب طرح ۲۰ ماده‌ای نمی‌خواهیم.»
▪️
او افزود: «اگر آن‌ها این کار را انجام ندهند، رئیس‌جمهور ترامپ بسیار ناامید خواهد شد. فکر نمی‌کنم اسرائیلی‌ها در شرایط کنونی بخواهند تنش‌ها با ما را تشدید کنند.»
در پشت صحنه:
به گفته دو منبع آگاه از مذاکرات، مصر، قطر و ترکیه فشار شدیدی بر حماس وارد کردند تا این توافق را بپذیرد.
▪️
مقام‌های آمریکایی و دیگر افراد آگاه از مذاکرات گفتند حسن رشاد، رئیس دستگاه اطلاعاتی مصر، نقشی کلیدی داشت. او میزبان مذاکرات بود و رابطه نزدیکی با خلیل الحیه، رهبر سیاسی حماس، دارد.
نکته قابل‌توجه:
به گفته یک منبع آگاه از این دیدار، هیئتی از حماس در جریان سفر اخیر خود به ایران برای شرکت در مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، با مقام‌های ارشد سپاه پاسداران انقلاب اسلامی دیدار کرد.
▪️
این منبع گفت مقام‌های سپاه از حماس خواستند برای امضای توافق عجله نکند و با وقت‌کشی زمان بخرد.
▪️
یک مقام ارشد آمریکایی نیز مدعی شد ایران تلاش کرده است حماس را متقاعد کند که توافق را امضا نکند، اما گفت این گروه تصمیم گرفت به توصیه ایران گوش ندهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77662" target="_blank">📅 06:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vlg5ckBh7F_BWFwgR3yS6BeENADOGeP-YuCgTUdUszWesgnygbJlMqXv8ZbasgTNuZwD1F2TKpnMprlljJ6mFAjCSdnxpGuxiCMMC6CLikO02Ehg1bHrq3qCL1s-TuiMxNa2tMwsOxQF6AJl9yAh3q1IjNd2oHstn-lMgrRPeakC4kBcOzZKlVhQhdfZefbzUXLWSVGC_oPH_66Y2oevuSYZFNhCWhvr5FZ51d9scTVWJNKPimfHE6eRyKwYjPyMfVVeT1CZ48pvpw9qp237-C-eWvub3hIu3SiUV0UdH6eR9mEa2OamEGqXxj6lwCcBMSXZNesecuu567q4I-sgaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
امروز، «هیئت صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و همه گروه‌های مسلح دیگر در غزه دست یافت. این گامی عظیم به‌سوی صلح و امنیت پایدار است.
این توافق، گامی حیاتی در مسیر آن است که غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای کمک به مردم فلسطین، از نزدیک با هیئت صلح همکاری خواهد کرد. هم‌زمان، اسرائیل نیز از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به‌عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این توافق، نقطه عطف بزرگی در اجرای طرح ۲۰ ماده‌ای ترامپ است. این توافق در مراحلی که با دقت طراحی شده‌اند اجرا خواهد شد. هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات» با یک نیروی پلیس جدید فلسطینی همکاری خواهد کرد تا مسئولیت تأمین امنیت غزه برای ساکنان آن و همسایگانش را بر عهده بگیرد.
یک سال پیش، جنگی خشونت‌بار و مهارنشدنی، بحرانی انسانی و گروگان‌هایی در اسارت وحشیانه وجود داشت. ما پیشرفتی تاریخی کرده‌ایم و هنوز کارهای زیادی باقی مانده است.
می‌خواهم از میانجی‌ها—مصر، قطر و ترکیه—به‌خاطر تلاش‌های مهمشان تشکر کنم، و به‌ویژه از تیم فوق‌العاده‌ام که تلاش خستگی‌ناپذیرشان این دستاورد تاریخی را ممکن کرد.
تهدیدی که در ۷ اکتبر از غزه سر برآورد، اجازه نخواهد یافت دوباره شکل بگیرد!
بر اساس این توافق، غزه سرانجام در اختیار یک دولت جدید فلسطینی قرار خواهد گرفت که به مردم خود خدمت می‌کند.
این تحول شگفت‌انگیز را که همه می‌گفتند هرگز دست‌یافتنی نیست، به همگان تبریک می‌گویم!
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77661" target="_blank">📅 02:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s38m_SVOK04VxMMm9vR2dVo9BaAAPN45MnybimbJtKz8r4RLnZJoV-4p_AaRUYKSoqJ3BZXcyJo7JwxwjY7Q2QBz_tA3oLEkcabook6hNnVRWiV5WUAW0A4PdI2xPHG3ZdDTAX2UxDIesUgxnGVHVq8EGyWWGcw8BT73QSZKIKI9JNhOgAF6mmBUqxmpERSBSLypmcd3eEP2qyQ8GbPPbWxLdu7uG6Iob2V29jxGLPX5KVmwoje7LbqGX-NwH93ZLuFrOcCv8sBkmdgTvpuCGVnruYZSkhlLriYGqRZBOroQA2QKgGcxrSPQfQXBT-d2MjDpJaat1-Is6oXB-m-_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس اعلام کرد افرادی که به سپاه پاسداران انقلاب اسلامی یا هواپیمایی ماهان خدمات مالی، پشتیبانی لجستیکی یا حمایت تجاری ارائه می‌کنند، به تداوم فعالیت یک سازمان تروریستی کمک می‌کنند.
او افزود وزارت خزانه‌داری آمریکا به شناسایی این افراد، افشای هویت آن‌ها و قطع دسترسی‌شان به نظام مالی ایالات متحده ادامه خواهد داد.
پیش از این، وزارت خزانه‌داری آمریک، شش فرد و نهاد در ایران، چین، هند و روسیه را به دلیل همکاری با هواپیمایی ماهان و سپاه پاسداران تحریم کرده بود. واشنگتن اعلام کرده بود برخی از شرکت‌های تحریم‌شده به‌عنوان نمایندگان فروش هواپیمایی ماهان فعالیت می‌کردند و در حفظ شبکه بین‌المللی این شرکت نقش داشتند. وزارت خزانه‌داری آمریکا همچنین شرکت «استودیوی استارت‌آپ داده‌نگار» را به اتهام همکاری با سپاه پاسداران تحریم کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77660" target="_blank">📅 02:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
مصر دوست و شریکی مهم برای ما در منطقه است و امنیت آن برای ما از بالاترین اهمیت برخوردار است.
همه ما باید در برابر توطئه‌های اسرائیل و عملیات‌های پرچم دروغین که برای تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.
تهدید روشن و مشترک است و از همبستگی مسلمانان هراس دارد.
araghchi
پست قالیباف:
ایالات متحده هر روز دست خود را به جنایت جدیدی آلوده می‌کند؛ حملهٔ تروریستی به منازل مسکونی غیرنظامیان در جزیرهٔ قشم، ادامهٔ جنایات در میناب و لامرد است.
امریکایی‌ها عادت کرده‌اند که سیلی‌هایی را که در میدان نبرد می‌خورند با ریختن خون بی‌گناهان جبران کنند. تاوان‌ خواهند داد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77659" target="_blank">📅 23:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3xHmTk42-OSqnMAFwZXXfjAZ7A0ZiRGIMCsiVNv3_P_CB_k2jUdnQf1O_lPEAzvDRfOmUEVfad9eFMjg04tsGID-Vhc-ypvgWmqnbWkFVj-CnM_QzAV_Pg8o1gM3CFbuGmCMGeQN1uKBoJV5G7lCoj2KfNLWYc5-eVPPbYWOD-07Gramu94r9eVkSa23xlYLxjIxbGBhWaIhA-tRHDSapUn1p_rz4pLLFt3p0wRZI40DwgHlOLLdr4LNgwElWSwJ_M0qQxVpQWcrMiKadVbEktqeXVgsxliREl3wJqXYF_VGLcJEyKdV1O8SrI9VXatQwTf-T4jUfeokd9WKjdqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی روز پنج‌شنبه از طرح تشکیل یک ائتلاف بین‌المللی برای دفاع دریایی با هدف حفاظت از کشتیرانی و مسیرهای انتقال انرژی در دریای سرخ خبر داد.
وزارت دفاع عربستان اعلام کرد نمایندگان ۴۳ کشور و اتحادیه اروپا در نشستی درباره این طرح شرکت کردند. بر اساس این پیشنهاد، عربستان به‌عنوان کشور بنیان‌گذار و رهبر ائتلاف عمل خواهد کرد و مقر آن نیز در این کشور خواهد بود.
به گفته وزارت دفاع عربستان، این ائتلاف با هدف تقویت امنیت دریایی، حفظ آزادی کشتیرانی، تأمین امنیت مسیرهای تجارت و انتقال انرژی و حفاظت از منافع مشترک دریایی در تنگه باب‌المندب و خلیج عدن تشکیل می‌شود.
این طرح پس از آن مطرح شده که حملات حوثی‌های مورد حمایت ایران به کشتی‌ها، یکی از مهم‌ترین مسیرهای تجاری جهان را با اختلال روبه‌رو کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77658" target="_blank">📅 22:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=A3xGlE1NONfdDcn1vJYuF11hLOJbJr-i_hlbv-SFBOLOvS_Ojx_8FaPMQf2G6bRuZw_AG7ZX3UNB8k1DQE168jHj_cHHBVwiRvVStW3GS2AFxa1on7dzsvQejIM-uf8Z6cRBODuZTathdCgZkh3PzIYOhkjwrQfGw0MR5retAYEvoN0e0T_in57uW5UrC2MiCyMqzBFweaJU05_VuHNRN8-XHcUd5fb8UFtdUAZiK3qTnpXVEOXpu6BvEw37UU0TnVtr31Usg4IuUSZRz6i34YkgBMSuzgTApxFSFvF-68-VSqSbwDeCP6ku46PDNLxQKghPj7-iiNfLRBoS9tMh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=A3xGlE1NONfdDcn1vJYuF11hLOJbJr-i_hlbv-SFBOLOvS_Ojx_8FaPMQf2G6bRuZw_AG7ZX3UNB8k1DQE168jHj_cHHBVwiRvVStW3GS2AFxa1on7dzsvQejIM-uf8Z6cRBODuZTathdCgZkh3PzIYOhkjwrQfGw0MR5retAYEvoN0e0T_in57uW5UrC2MiCyMqzBFweaJU05_VuHNRN8-XHcUd5fb8UFtdUAZiK3qTnpXVEOXpu6BvEw37UU0TnVtr31Usg4IuUSZRz6i34YkgBMSuzgTApxFSFvF-68-VSqSbwDeCP6ku46PDNLxQKghPj7-iiNfLRBoS9tMh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر جاویدنام آیدا حیدری، جوان معترض کشته‌شده به دست حکومت، در سالروز تولدش بر مزار او می‌گوید که آیدا حیدری «شیرزنی» بود که جانفدای میهن شد.
آیدا حیدری، دانشجوی رشته پزشکی دانشگاه علوم پزشکی تهران، در ۱۸ دی‌ماه ۱۴۰۴ در تهران با شلیک گلوله جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77657" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=GKwrhWG09dK0tGWCLASX8fLckD0HyPvd6-TzUBF20RW5PtkNlTmuc1-xEEshBQgO2JkTgIAK8PO-JExFzTLkt84qM-631G1S7sZSgf0qVor3mBqATTAfEGD160L71BXNacoHJVxb4tMUXQdLhpUhYizTqpl3dHN16FpO-31b5wm7zBkmidW2O6DDhZln3Rc-WagJbvUNcUZUbbqXFnQwUkB8Kp7UXO5-Ms9llY2P3AXDYrURCzStT4-WOYhjydVhWDpns5YsyqBwRmII5ZzZ6OyFXfdFdDq7kFP0AvC-SCLuY-YYAi9xdZx57sYnIW8oASctSsG1qw-ESxwUsP_QNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=GKwrhWG09dK0tGWCLASX8fLckD0HyPvd6-TzUBF20RW5PtkNlTmuc1-xEEshBQgO2JkTgIAK8PO-JExFzTLkt84qM-631G1S7sZSgf0qVor3mBqATTAfEGD160L71BXNacoHJVxb4tMUXQdLhpUhYizTqpl3dHN16FpO-31b5wm7zBkmidW2O6DDhZln3Rc-WagJbvUNcUZUbbqXFnQwUkB8Kp7UXO5-Ms9llY2P3AXDYrURCzStT4-WOYhjydVhWDpns5YsyqBwRmII5ZzZ6OyFXfdFdDq7kFP0AvC-SCLuY-YYAi9xdZx57sYnIW8oASctSsG1qw-ESxwUsP_QNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
در چند ساعت گذشته، رسانه‌های دولتی ایران همچنان ادعاهای دروغین سپاه پاسداران انقلاب اسلامی را منتشر کرده‌اند؛ به‌ویژه سه ادعای زیر:
🚫
ادعای نخست: سپاه پاسداران بار دیگر ادعا می‌کند که مسیرهای آزاد و باز عبور از تنگه هرمز برای کشتی‌های تجاری خطرناک است.
✅
واقعیت: خطرهای فوری برای کشتی‌های تجاری و خدمه غیرنظامی آن‌ها، تهدیدهای لفظی و تلاش‌های سپاه پاسداران برای حمله به آن‌هاست.
🚫
ادعای دوم: سپاه پاسداران مدعی است سه جنگنده رادارگریز اف-۳۵ آمریکا و سه هواپیمای دیگر در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✅
واقعیت: در تلاش‌های اخیر ایران برای حمله، هیچ هواپیمای آمریکایی منهدم یا آسیب‌دیده نشده است. همه موشک‌ها و پهپادها رهگیری شدند یا نتوانستند به مناطق هدف برسند.
🚫
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام M/T Nora محاصره آمریکا را شکسته است.
✅
واقعیت: این کشتی تجاری نتوانسته از محاصره «دیوار فولادین» آمریکا عبور کند. بیش از ۲۰ ناو جنگی آمریکا، صدها هواپیما و هزاران نیروی نظامی همچنان در آماده‌باش هستند و اجرای کامل محاصره را ادامه می‌دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77656" target="_blank">📅 19:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dFnbY1nLdm_1FTNkt8UTMrh49pvrHdtMzojEvgs7gAHOcy94S-sT8JySttaU-C4KjQ7MDGOTJyfEdyazQprENuWD04rcEHLJSxYFcsCrBshrPr34sQhOMqwlr4EnPKKymB5prNpaobOMHYGLA36sbQEPh9TjjVp0WP9E2i3b9ksV0SY8SIiZIpaTB7kEYaprp8COYWRFqodjRLmT1c4TNjOdJ93qaaDop4prMjlP5BOIttic8NosTTOdB2cETftSCZ9J8aXMXclnJ7swBBn4fDF5E7ZmHqdtXd2LwDt7UnEQHyBtO3p2kmNRKnnimiNsXAuPgHUFsr441hVOHVkmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=qtiYpScpxb9pxMqd9qzlYxjGrXmxTaGqU6z9U_bKWOzfdNEAGDdh8SAtaEH6m1L4HedeUd8pnKsTytlnFgK-PIMapCONuijy8d9hK5iHVDuuJLTMv9o5rq8X8JxtJxVa_LgtUxSkxdyvXvft_R8Z5vDe57qYexfPjc9wbz03-5hy9cBv8OmitO9PQK6VGCWjsixx8KygADD0XKVEx3_efE7yQ-cLQCM2ib_WjzeXY_2b1bx2uSs5-4MAw4PnXuuyotSj3OaqlbLPVpsnLA3VzZ2R0HmaCBEfxhJU91058HUxBvqw3Kr0gIx80Lo8P3gSAfaD3XfcKQntAQNLpm53ug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=qtiYpScpxb9pxMqd9qzlYxjGrXmxTaGqU6z9U_bKWOzfdNEAGDdh8SAtaEH6m1L4HedeUd8pnKsTytlnFgK-PIMapCONuijy8d9hK5iHVDuuJLTMv9o5rq8X8JxtJxVa_LgtUxSkxdyvXvft_R8Z5vDe57qYexfPjc9wbz03-5hy9cBv8OmitO9PQK6VGCWjsixx8KygADD0XKVEx3_efE7yQ-cLQCM2ib_WjzeXY_2b1bx2uSs5-4MAw4PnXuuyotSj3OaqlbLPVpsnLA3VzZ2R0HmaCBEfxhJU91058HUxBvqw3Kr0gIx80Lo8P3gSAfaD3XfcKQntAQNLpm53ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی قدیمی منتشرشده در شبکه‌های اجتماعی رقص علیرضا سپاهی در اصفهان را نشان می‌دهد.
قرار بود او بامداد سه‌شنبه اعدام شود اما پیش از انتقال به محل اجرای حکم دچار سکته قلبی شد و به بیمارستان الزهرای اصفهان انتقال یافت.
@
VahidOOnLine
یک شاهد عینی گفت پس از انتقال علیرضا سپاهی، معترض محکوم به اعدام، به بیمارستان الزهرا اصفهان، فضای بخشی از این بیمارستان امنیتی شده و شماری از ماموران امنیتی در آن مستقر شده‌اند.
بامداد سه‌شنبه، ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو نفر دیگر از بازداشت‌شدگان اعتراضات ۱۸ و ۱۹ دی‌ماه ۱۴۰۵ در اصفهان، با حکم دادگاه انقلاب اسلامی اصفهان اعدام شدند. ابوالفضل سپاهی بادجانی، پسرعموی علیرضا سپاهی بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77654" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebec49421.mp4?token=XPldcpkxQH1fPhHAj-383hUR_KTKLlIatcMn35fV-kZwVkXczhbAV4zzRLZiBDTg6K935CcXzHOtLt_dFR9CpSbdjFJN5jkHuuTrcV2GUqW1Q5ByFexuCPsxiZZWvTPJNmDjqD0dEbDAFIFkjgUNOso7CaywpuKBWLlXyK8Y3DJYpw_7pe5Z-I0sT5KD_74uGTGvsmMQ9EJRDzw3th9UfhxOLHXZsNo18ExdY6LXohCLlJhoRKlkWmyVwxCXG2RXlr_nQnJuv8hQjgNlLUe9XbvD0H2d2AhOTyT8hOG4okLtGzMNbYwWCUQBTikub_KRbtEegcCx154ImO4xWH7hnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebec49421.mp4?token=XPldcpkxQH1fPhHAj-383hUR_KTKLlIatcMn35fV-kZwVkXczhbAV4zzRLZiBDTg6K935CcXzHOtLt_dFR9CpSbdjFJN5jkHuuTrcV2GUqW1Q5ByFexuCPsxiZZWvTPJNmDjqD0dEbDAFIFkjgUNOso7CaywpuKBWLlXyK8Y3DJYpw_7pe5Z-I0sT5KD_74uGTGvsmMQ9EJRDzw3th9UfhxOLHXZsNo18ExdY6LXohCLlJhoRKlkWmyVwxCXG2RXlr_nQnJuv8hQjgNlLUe9XbvD0H2d2AhOTyT8hOG4okLtGzMNbYwWCUQBTikub_KRbtEegcCx154ImO4xWH7hnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار خانواده جاویدنام محسن رشیدی خانی‌آبادی و علی ایازی با خانواده عرفان اسفندیاری و امیر حسین صفری ـ گزارشگر (ویدیو صدا ندارد)
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77653" target="_blank">📅 19:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgbg7J3i-ybUC4XkTZ5V83Xx0GXExS3frbWjrRDwT4hFJ0hHGLi84du9DEq63SkNk5sZ4L7JhUwkvKb6n0FzLvz8aI_nQFdqgGXZtZxabTg73hB-ZK0az_TkZK_rKVAA7Cqq1Qh-WmidpXjc3aAhaUnTAtuDPwxnOI9BDEcYfRhapWer6Yk4wtw_1jvxgJ0urjgoUm48SUQFzuw_51txm4FVVBuT6Xpkpc4cjTKDN2n3s6MRHCy4dyMCmIwYgNi7ld8CO4qQV_Asf5H-8UIWKv1K5Bxi0M3mwDwiTJTthrcH4V90Z505CfoxbzVT4HeDXncH8Ta_Xr3_ri0Hk-C_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ان‌بی‌سی نیوز روز پنجشنبه هشتم مرداد، به نقل از یک مقام آمریکایی گزارش داد که دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در جریان نشستی در هفته گذشته از فرسایشی شدن جنگ، محدودیت گزینه‌های نظامی علیه ایران و دست نیافتن به توافق خشمگین شده و بر سر مشاورانش فریاد کشیده است.
به گفته این مقام مسئول، بر خلاف اظهارات عمومی ترامپ مبنی بر رضایت از روند جنگ، نه او و نه مشاوران ارشدش از وضعیت موجود راضی نیستند. یکی از متحدان ترامپ در این باره گفت: «رئیس‌جمهور کلافه شده است؛ او تصور نمی‌کرد گرفتن امتیاز از ایران تا این حد دشوار باشد و هیچ راهبرد مشخصی برای چگونگی رسیدن به نقطه پایان وجود نداشت.»
این گزارش می‌افزاید نبود شفافیت درباره اهداف نهایی واشنگتن—از جمله این‌که آیا هدف اصلی جلوگیری از دستیابی ایران به سلاح هسته‌ای، بازگشایی تنگه هرمز یا نابودی برنامه‌های موشکی و پهپادی ایران است—برنامه‌ریزی برای پایان جنگ را دشوار کرده است. یک مقام آمریکایی تصریح کرد: «ما پیروزی‌های تاکتیکی متعددی داشته‌ایم، اما بدون داشتن یک راهبرد روشن، با یک شکست راهبردی روبه‌رو هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77652" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8srBj6AhgMoumSJ6LxeKUdS8OYBeVismACwE0r1jcvDmizuE88DGi1KnuT1psUwDtlS0sig3GAkiYlZ7H1V5DvE3_Unm8HsTjSmKp--4g1De0vxIHr6sRYcc1qFixyT2Rsc9KQboeIzhNKdkQvaBSC2D5IQZkU-jber42omUBQ4gFAQ3Zw3VB1f3ZA-rGcfvyeSXM-nwmcyrUwvb_Z8JB7-Oj-CYE-Qhmq44TocegDyPbLTwap9j_dxKfYbqymUUAq43GS6Fy_3AhrcFVVxArGJ7X76nrVlFzyYmqrT-3MDx2r8D2JND-J7yeceQWImpaYbql4ZfZjwFV6tIRX2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌وزارت دفاع چین گزارش‌ها درباره برنامه آن کشور برای تحویل صدها سامانه پدافند هوایی دوش‌پرتاب به ایران را رد کرده و آن را «کاملا نادرست و خلاف واقع» خوانده است.
جیانگ بین، سخنگوی وزارت دفاع چین، روز پنجشنبه در پاسخ به پرسشی درباره این گزارش گفت که ادعای مطرح‌شده صحت ندارد. وزارت خارجه چین نیز پیش‌تر گزارش مربوط به این معامله را «بی‌اساس» توصیف کرده بود.
رویترز روز چهارشنبه به نقل از سه منبع آگاه گزارش داد که ایران قرار است ظرف چند هفته نخستین محموله از مجموع ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل ساخت چین را دریافت کند. به گفته این منابع، قرارداد مورد نظر شامل موشک‌های کیودبلیو-۱۲ و اف‌ان-۱۶ است و ارزش آن بین ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود.
بر اساس این گزارش، قرارداد با یک شرکت مستقر در هنگ‌کنگ امضا شده که گفته می‌شود میان ایران و تأمین‌کننده چینی نقش واسطه را ایفا کرده است. منابع رویترز گفتند که قرار بود محموله‌های اولیه از شهر ارومچی در غرب چین ارسال و از مسیر پاکستان به ایران منتقل شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77651" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RBT0AuaV5Af938lpWT7uMbX63JeTKjG6DxSKohac0owsVM0k_6nw40EBHQZlynUwH_QcHi5BZXgXJyRDZTTk0ZIq1B_tM6vwYu4ALnL0_zyH1L018XUhkmn9_PzcTQ0ZJr57pf4iJ0hhColqdPXzJcNa0m4S-vZgSQlZltvbsNKzLNmeqMjt-zr-tQwgYFvDL_ZB3kihm_GCu59LyM9Vi3VvKyvjRLMZr0lYnoHHeaHzV_IfZU-2dI3ZOggEhnIm3bN3AbkLzKZpku7ZA3zMCWyCCzqvs0FSf3DytMgy3TP7UY9UZBAggFRYawnXJto2OAbEz1EXIuOO1-p8iltJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OO45t3FASUuvUY8_DU7aES4ajprYWAIyyuXxdSNGgdkYnH1tNrywhZxSfpBDIkvaA2jhl11UX20N8nKBaeIlLh-1E5wTF1Ztpzi4CSeAaOG40YnTUb8C1i7SsVjsMN7mgeptf-PnWdbAs6Xy81pW3WpWAUoB_tnB8JWBhnxtvqEwYY9BFw670Ov-KjYyaYMKKmOJHfugnzplCEwT42XNEtqLpNodFu-p9u0ZRCKHM8NUVKqnyBUlgVpGNzFAkVq3V39QWh4_3Kz_0M7rhIMXLVFvNn4Y2Wtg-EIvfHjVv99_w5Ssu-5hMPMbIMLkoJMssCJ2EC5-iwXeACAAfB_Tsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: با شکاف عمیقی که پس از کشتار دی‌ماه بین مردم و رژیم ایجاد شد؛ حکومت ایران در نهایت سقوط می‌کند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در پاسخ به مجری ای‌بی‌سی که به او گفت طبق گزارش نیویورک‌تایمز شما به ترامپ گفته بودید که ظرفیت موشکی حکومت ایران ظرف چند هفته نابود می‌شود و تغییر رژیم ممکن است رخ دهد، گفت: این ارزیابی اولیه من نبود و این بیان نادرستی از آنچه گفتم است.
برآورد من این بود که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای اقدام کنیم.
نتانیاهو گفت، من گفته بودم که می‌توانیم شرایط را برای ضعیف‌تر شدن رژیم فراهم کنیم اما بر عهده مردم ایران خواهد بود که سرنوشت خود را تعیین کنند.
او درباره احتمال تغییر حکومت در ایران گفت: «فکر می‌کنم ایران از همیشه ضعیف‌تر و اسرائیل از همیشه قوی‌تر است، اما نمی‌توانم بگویم رژیم هم‌اکنون فروپاشیده است.»
نتانیاهو گفت: بگذارید یک پیش‌بینی کنم؛ پس از چنین شکاف بزرگی که به دنبال آن قتل‌عام (کشتار ۱۸ و ۱۹ دی‌ماه ۱۴۰۴) بین مردم و رژیم ایجاد شده، فکر می‌کنم که رژیم ایران در نهایت سقوط خواهد کرد.
نتانیاهو هشدار داد اگر ایران، اسرائیل را هدف حمله قرار دهد، «اشتباهی بسیار خطرناک» مرتکب خواهد شد و اسرائیل «بسیار شدید» پاسخ خواهد داد.
او در پایان گفت: «هدف من این است که مطمئن شوم ایران با این حکومت به سلاح هسته‌ای دست پیدا نمی‌کند. این موضوعی است که من و رئیس‌جمهور ترامپ هر دو بر سر آن توافق داریم، زیرا در آن صورت جهان متفاوتی خواهد بود.»
@
VahidOOnLine
نخست‌وزیر اسرائیل روز چهارشنبه در گفت‌وگویی اختصاصی با لینزی دیویس از شبکه ای‌بی‌سی نیوز تأکید کرد که دونالد ترامپ تصمیم‌گیرنده اصلی درباره جنگ ایران است و او تلاش نمی‌کند ترامپ را برای ادامه حملات علیه ایران متقاعد کند.
نتانیاهو در عین حال گفت نسبت به امکان دستیابی به راه‌حل دیپلماتیک با جمهوری اسلامی تردید دارد.
او گفت: «نمی‌دانم این احتمال کم است یا نه، اما نسبت به شیوه عمل ایران بدبینم. آن‌ها همیشه دروغ می‌گویند، تقلب می‌کنند و زمان می‌خرند. آیا تحت فشار کافی ــ فشار دیپلماتیک و اقتصادی ــ ممکن است این رفتار تغییر کند؟ می‌توان امتحان کرد.»
او افزود: «واقعیت این است که ما شریک و متحد هستیم. او شریک ارشد است؛ فراموش نکنیم که او رئیس‌جمهور ایالات متحده آمریکاست و من شریک کوچک‌تر هستم. اما من نخست‌وزیر اسرائیل هستم و هر زمان لازم باشد از منافع و امنیت کشورم دفاع می‌کنم.»
نتانیاهو همچنین از نقش دولت ترامپ در مقابله با «دشمن مشترک» قدردانی کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77649" target="_blank">📅 19:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_unWhoGbCig4srqrSdYkhfLLrbMuM4T7zq_-Ek5rWm_PZLzyiOMbG33G68NOSBF9X9U6LhXpszRZGBdAPVzN-YvNL3RGxqgd8ADNk1jwCErmbFQv70hRFU5Qovn_IzqpvYW1_Bmt_3AqO1W5t5EN0wsdN8XKKWkyEXXzFBdntvR06ulnCXy3dCePCRPQ36NuxEG5HWHj4P9gNs26XYRaHzuFFDL3nLjbKHWKVpr85LfIiOPmbEHCvLH1CJ0p7QXoTeQyFrkfWirnvC9R7cof3W8TNxDLAn3sCQ01hE5iFqPP-4MtihXW-7WZLuq5-27RHrzoUm7FDwyQXXKIJ4R4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار ویدیویی از ضرب‌وشتم چند زن در ایران در جریان یک پخش زنده اینستاگرامی، موجی از واکنش‌ها را در فضای مجازی به دنبال داشته است.
به‌ گزارش خبرگزاری میزان، وابسته به قوه قضائیه ایران، پس از انتشار ویدیوی این لایو اینستاگرامی با دستور مقام قضایی برای این فرد پرونده تشکیل شده است.
سعید راستی، معاون بخش «مبارزه با شرارت و جرایم خشن» پلیس اعلام کرد که این ویدیو باعث واکنش گسترده شهروندان شده و اطلاعات ارسالی مردم در شناسایی متهم نقش داشته است.
آقای راستی اضاف کرد که این فرد بامداد پنجشنبه، ۸ مرداد ۱۴۰۵، «در عملیاتی» در مرکز تهران شناسایی شد و «به دلیل مقاومت در برابر ماموران» دو گلوله به پاها و یک گلوله به دست او شلیک شده و در پی آن بازداشت شده است.
هم‌زمان، ویدیوهایی از این فرد پس از بازداشت در شبکه‌های اجتماعی منتشر شده است که او را در یک مرکز درمانی نشان می‌دهد. در یکی از این ویدیوها، او در حضور پلیس از زنانی که در ویدیوی ضرب و شتم دیده می‌شوند و همچنین از  شهروندان و پلیس عذرخواهی می‌کند.
@
VahidHeadline
دیروز بارها اون ویدیو رو برای من فرستاده بودند و می‌خواستند پخش بشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77648" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB4CeD3eRHcI1pBuLm6G2N5vRpaCXixnBtbI9OxJeEPKp9RqXjnN5HjDDz9OGoESvC6a1r5O2DurzGDjAvJm87JxWtb0IJi2ZNNrOlz8JvbPL2AgugDzKQGihsXgt3X2PV4Y1QXSnymp4JTvTlZY6coc7N6j8DVoJG4bQMvdkXthMa9f3yW3Lb2zYw0B6S9Mh3M4fy1hflYt0U3-FucU0O8XN3yd2oLJdtMeWF4_4g6Wu8N25KOqxvJxhtxp2TRPDX8iAtbLY-8Oa1bQxGSC5MPd282-pEfF-wb7rMLSCZtO2KxYkpt_gQY4OWNnRwSNI7p_GAU2bfnJ_HtKwoGaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی (آرمین) جنت‌خواه، فعال شبکه‌های اجتماعی، برای اجرای حکم قطعی سه سال حبس بازداشت و به زندان فشافویه منتقل شده است.
بر اساس این اطلاعات، آرمین جنت‌خواه روز ۳۰ تیر ۱۴۰۵ بازداشت و پس از انتقال به زندان فشافویه، اجرای حکم سه سال حبس او آغاز شده است.
اتهام منتسب به او در پرونده قضایی، «تحکیم مواضع اسرائیل» عنوان شده است.
جنت‌خواه پیش‌تر نیز در دی‌ماه ۱۴۰۲ توسط نیروهای امنیتی بازداشت شده بود. جزئیات مربوط به روند رسیدگی به پرونده و نحوه صدور حکم او به‌طور رسمی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77647" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy8CXSYMqN0diDwgPDQPSnL59K1jRKK1h_tGF_-xwhaSsk5Emwt6Y9FoqaYFuq_9ppKAvAa8Dnqkg5mgGiwpgiSK3Rd2HPKZGZBjES9uroKHnmRpmXx3-22JXRMmjCoOJ-ozyEjJb_DCwOzUyL5b8N7YJzp7THYtHG_e2JZoNiDxvNZHIoPUTEEdToFUklbJDAkXfikiMFd8Dg4Yfe_769oXeht3-dgf6R-p9d8g-H0gCKB1hcF6xETppjHGfWBJgYcCqD7ZvwBqVT72yZkLzdsChRWP4lmq5tuYlrWhnlpJTLyvbIPP_r3g_yl9lWxp822frtloXa0nm-Pvmj-h5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران زنجان با انتشار بیانیه‌ای از کشته شدن سه نیروی این نهاد نظامی در حملات بامداد پنجشنبۀ آمریکا به نقاطی از ایران خبر داد.
در بیانیه روابط عمومی سپاه استان زنجان، به‌جز اسامی این اعضای سپاه پاسداران، جزئیات بیشتری درباره محل کشته شدن آنها و درجه و محل فعالیت‌شان اعلام نشده است.
این در حالی است که تا ساعاتی قبل، رسانه‌های ایران این مناطق را به‌عنوان نقاطی که هدف حملات بامداد پنجشنبه قرار گرفت، اعلام کرده بودند: «اهواز، آبادان، بندرعباس، قشم، بندرانزلی گیلان، کازرون و فراشبند استان فارس، چغادک بوشهر، شادگان و اروندکنار خوزستان و جزیره کیش»
@
VahidHeadline
پیام دریافتی بررسی‌نشده: در خود زنجان کشته نشدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77646" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlnJ3-kEs_yoRYWCRXMpzo3LJP-1tqwFMm-MzmKwJhdJRcUxLmxlNmq91vbatBaPl_jMzUQNC4RUJU1fvjKT4QRPd7fjcaEYgV4ioT9GzAy8pL-JFCxsSr89sWKSSFdwwV59KfaqbyUHy5K08A4D1Qg3JAIQi9WBjsLG-9Ihm25uRR0i4EBytTxIddZGsrHj8vyEPNLI8OHT0wSYd4ADe-FFMd3H8EKk3xsChbCuN5W-68SRDBjnrsIvFGM1nAJJjy9YPowzMquD24fKqvK93YIJLOZ6fN3Iq9LVHbEa6vVOZLymr9zLRLpvbVh3xiMK6-QuF401d1aqlRu8wpuNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران ادعا کرد که در حمله به پایگاه الازرق اردن «سه فروند هواپیمای اف۳۵» را از بین برده است.
سپاه پاسداران در بیانیه خود ادعا کرد که پنج‌شنبه هشتم مردادماه، با حمله به محل استقرار و سوله تعمیراتی جنگنده‌های اف۳۵ آمریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، «سه فروند هواپیمای اف۳۵ را به کلی منهدم و به سه فروند دیگر خسارت سنگینی» وارد شد.
سپاه همچنین ادعا کرده که در این حمله «چند افسر و کادر فنی و تعمیراتی» کشته شدند.
این ادعاها در حالی است که پیشتر ارتش اردن اعلام کرد که پنج موشک شلیک شده از سوی جمهوری اسلامی را در آسمان این کشور رهگیری و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77645" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KznKzfa6CwF9-mwCqALQVMzQT5qHbMu5S3DR-sK0gjfTflUrPzd7OeYB-hX5-Kk8QTaMUmOqEhYrVFKG8CA0H7ul80yqVLNqjpwkVSeYTQpwwShL_6I81FICX_teN3tOWDYieMKniRO334gLAUQmtcLgMKy29iB6hHp6_8EzNdCZ_qdUXDedumUV8zRABHD7DHC8gpYZ5n0PL-54EAyhSXUzQwJLxeutDIecej-64bhYz0PFCNi3tl5ZfKk-eYHDc9HBbGJum6Yy5mofn0zpdwxGLb4MmZOXxxvotsvKimUxPYzYw3uE_f94V5f_hm1YHgleTW6_mYHbWnL3bkQUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۴۱ دیوان عالی کشور حکم اعدام بنیامین نقدی، از بازداشت‌شدگان اعتراضات سراسری دی ۱۴۰۴، را که پیش‌تر از سوی شعبه اول دادگاه انقلاب شیراز صادر شده بود، تایید کرد. وکیل او می‌گوید با وجود ابلاغ این رأی، درخواست اعاده دادرسی به‌زودی به دیوان عالی ارائه خواهد شد.
بنیامین نقدی شامگاه ۱۳ دی‌ماه ۱۴۰۴ در جریان اعتراضات در شیراز بازداشت شد.
بر اساس گزارش‌ها، علت بازداشت او شعله‌ور کردن یک کپسول آتش‌نشانی در مقابل نیروهای انتظامی عنوان شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77644" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LqvfgqO5zEEB6LnqeKXzb2tBXw_3y0C53WdC97dkf5V5SfOxKyeDRLGeeQNKTHN_zzB40M5piBiYOxs1jUG7zmnH0kQ05-UckfELgzTkR45lUe9LYkGz7CwwAHF7Cjub7V6PjbYzPd-RPBH3iV82Qg9dxtX5Nv9XM1ooJVcPnar_0IGh8LSR8Eytxn04WeaFYkXDY7NVdxqh2rzXNBz2k64Oua_rFOTR4i9rf3z_MNunTvvTw_zHf0v1igRYcSXF9x3KWfKOD2xpbIWrmQOYN4bMP38yxTuGbqLJ8_EU3W_LuELBzBhtE0J-hvWL5sEvoY2gS283aD2IYx6WIBzTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: آتش‌سوزی پس از حملات آمریکا به نقاطی در
#اهواز
پنج‌شنبه ۸ مرداد حدود ساعت ۵:۵۰
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77643" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOTUspmgwI5EuGMTSp8sgB1Ucwvtu9bPaaJE8CWczWeRlMARuqzPXcAHoiGPHw_mutifTDLQZqUfT6I3ArPHbE1w4ojBzIhWIDAooz20ijUK8nkVswyyySQDK-dz5f4RqxnvAR9-AHZTf9t5NSFg-HrDpUGM5fqQAhMN1Zb0s2wavP1H1R31xQ_rTbj5Kgd-bM9cG_x5lo3FNsv2lq8ZhyxcAol-td0gnCw7z0aGXyaxpSdypJiVM-CYuiBn6Y8mJ1fokvM4Yk2b4uNLkDSpOcDU1AXxLoPvhHIjDQPwSiu217oceDbKXlwxMqBwE_YyHlG6qFN1nSF98WI8f7L0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اردن صبح پنج‌شنبه هشتم مرداد از مقابله با حملات موشکی ایران خبر داد و اعلام کرد پدافند هوایی این کشور «پنج موشک بالستیک» شلیک‌شده به این کشور را رهگیری کرده است.
سپاه پاسداران روز چهارشنبه نیز باوجود توقف چند روزه حملات آمریکا، به سمت اردن موشک شلیک کرده بود. پایگاه‌های ارتش آمریکا در اردن از ابتدای دور جدید حملات متقابل آمریکا و ایران از اهداف اصلی حملات موشکی و پهپادی سپاه پاسداران بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77642" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=Vbh8uYEA_7Z9-NLnRO8cugRzms2V3k0yGP3qainUk2jL8Htxecp9J-u6sHHnsfl3YtXxVe6IOOQptIVfpNNA8Wqk1ls602_QZObqlQoyjFgXl9X0dlRAJz0bdGnjBKth07R5N-jt_tU061DhvkqnRgATtnKMmjrUwJv1gyZCt1b-AZG-MnttWyE9lTWggkuCyMzSqQa8dDsFRbhClJt49U6nC9d2upYtq7aPOYgZ6E8wV1INMz1NGykqrZMxYzLuyNJr6vraEIaRkcU3i5Sqapvs1cG0GMDr9SF6BtkdR3QQ1j54ChC-b291LxBk6EwFbhpbqk63XdTwpLzSR9afWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=Vbh8uYEA_7Z9-NLnRO8cugRzms2V3k0yGP3qainUk2jL8Htxecp9J-u6sHHnsfl3YtXxVe6IOOQptIVfpNNA8Wqk1ls602_QZObqlQoyjFgXl9X0dlRAJz0bdGnjBKth07R5N-jt_tU061DhvkqnRgATtnKMmjrUwJv1gyZCt1b-AZG-MnttWyE9lTWggkuCyMzSqQa8dDsFRbhClJt49U6nC9d2upYtq7aPOYgZ6E8wV1INMz1NGykqrZMxYzLuyNJr6vraEIaRkcU3i5Sqapvs1cG0GMDr9SF6BtkdR3QQ1j54ChC-b291LxBk6EwFbhpbqk63XdTwpLzSR9afWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/77641" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G_v0QJqU7HTTO1xVh0TG5vsS4sN7d4e9KGrrkuNrP6c8Zdj3LDzC4xI2LsyNTeoq4qiV2VQXyiqB7r7KKTAOcWoZuVtIK2azgu7u-DBQI-tsLtk6pSXtVBGq4DFTyNzfpFpRgjmtzzw0IgB1_vd_x_Sx9lS4Kw3F3NupWnIkPtBKURXTPV1i12NBwBcLhW96CWfyxNi5TTs95HGpZ67yuPBJ-mPKuVsWo5lX9Vvwv3TSWZm6Vlnhe5cLjmPV_9mEdJRV_wHGL_zcF3jgRsD-UtsL0r_xdJYJSDf8wH_NJuI4RlDM1HVfz5qVxQeyhwIvpwWwobu2ubbouDtC04tI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف خمین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/77640" target="_blank">📅 07:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgRiPLiFBdZeDB2gbzjAEnt88diKeKnUHyudO_mBQPlKskZd0AdJKnn2swEydt682XR7KEBhxMeVZOeESRznCQbd1X6JhzCSO6HZcVizPHasYRZaO57o9GiqDbvcbwWXtRp-r26oz6xAM2Ay-WVG6rbETPZzubffy334n88JlCbFMnEyIhxLsvpE_ScKTOyyCetSEeMb7o3ZOewRbF1YEnIHQXIw7Oj-F8D5YhsPx7lPZuJWH95q1ytmMuuNsmqIvxNMSyQYDMm6Frcm8z3t3_irINZVeDTabqVRuwr0JTzxrdBBh6VjWFOXa_U5RvP3R2visjzC-VLFDpVjPkfZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از یزد
سلام وحید از سمت یزد دارن موشک میزنن
از یزد موشک زدن
سلام ساعت ۷:۲۱ صدای ارسال موشک داره میاد،
سلام از یزد موشک بلند شد ۷:۲۲
الان یزد 7:21 دقیقه  موشک فرستادن
سلام وحید. جان ساعت ۷و۲۰دقیقه از یزد موشک شلیک شد
وحید جان از یزد موشک بلند شد
۷:۲۱ پرتاب موشک از یزد
همین الان از یزد موشک زدن</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77639" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXfA0n_yqdJVAdL-8keOPvdWD3QLUzzcMwZN_0e6t6lPpRcl_FWuocgmjHgbj1XvmIgnh4_yGdi1a1FqQsnxIjxwfGK656TjaqgIwhBUIRnLOLvC_H1afpEF0ajrpjoI1etNFHIQ095dyFW9E6azd5KnWcMb0QuEI_n6QC59-NdFYqFMeu2k-MtJTR-hMb49DanOvyVCOu3UBLO0VfmtpWnf1sqtTDynuLlSi9IGggkg58J3eT6E0DuGRBHgRyvGHn9QjPe2AjPdiFRepegff0FtFc-3K1XX4Gv-__LfbZdx9RPr2F6jHf_FHenJQbXxNcd8gHJ901TJ8kGUhdryFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال در گزارشی نوشت آمریکا در پاسخ به حمله موشکی جمهوری اسلامی به نیروهایش در اردن، بامداد پنجشنبه حملاتی را علیه مواضع سپاه پاسداران انجام داد.
به گزارش این روزنامه، با وجود گسترده‌تر بودن این حملات نسبت به عملیات‌های پیشین آمریکا، یک مقام آمریکایی گفت این اقدام به معنای بازگشت به عملیات گسترده نظامی نیست. امیدها به دستیابی به یک پیشرفت دیپلماتیک فوری نیز با این حملات کمرنگ شد.
ارتش آمریکا این حملات را «پاسخی قاطع» به حمله روز سه‌شنبه جمهوری اسلامی توصیف کرد. این حملات چند ساعت پس از آن انجام شد که دونالد ترامپ، رییس‌جمهوری آمریکا، وعده داده بود به این حمله پاسخ خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77638" target="_blank">📅 07:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=g6pMp-RXi6oUpYDVVkfEE2T6-subuF13EEZDrsxmbFZJLmm-rPmkRvXkrdRvXStKU7oYSn2PnJ9Ws4lslaV54jkeosc5k0S94YzWWz9fbH2_UWotAPA57f5dX6GLrhOaZcJqz8kE9yAWJL_QXWJLNCtZ27j13-K1EQoOMfMx4hYyTt6lmvGBkeQDK2rwLOCpbolBysIMgrFtjcL1UwbHWx9tDPFLtIjAAcRSMTL6L9ogJyhRhXnyspyeTobqErnXs05yIkZtp_yl0Kj82mx4d4WntfrNh8zYXKrJRbzLo7M7SQzUsGbMBaemLLGEgCPTwFfTiamyWqLiUoXVNUvhrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=g6pMp-RXi6oUpYDVVkfEE2T6-subuF13EEZDrsxmbFZJLmm-rPmkRvXkrdRvXStKU7oYSn2PnJ9Ws4lslaV54jkeosc5k0S94YzWWz9fbH2_UWotAPA57f5dX6GLrhOaZcJqz8kE9yAWJL_QXWJLNCtZ27j13-K1EQoOMfMx4hYyTt6lmvGBkeQDK2rwLOCpbolBysIMgrFtjcL1UwbHWx9tDPFLtIjAAcRSMTL6L9ogJyhRhXnyspyeTobqErnXs05yIkZtp_yl0Kj82mx4d4WntfrNh8zYXKrJRbzLo7M7SQzUsGbMBaemLLGEgCPTwFfTiamyWqLiUoXVNUvhrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا پس از تلاش ایران برای حمله، مواضع سپاه پاسداران را هدف قرار داد.
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۱۰ شب ۲۹ ژوئیه به وقت شرق آمریکا، در پاسخ به تلاش‌های دیروز برای حمله موشکی به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند.
تجهیزات و نیروهای سنتکام ده‌ها هدف متعلق به سپاه پاسداران انقلاب اسلامی در ایران را هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، مواضع نظارت و دفاع ساحلی و توانمندی‌های دریایی. هدف این حملات، کاهش بیشتر تهدیدهای ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حاشیه خلیج فارس بود.
در ۲۸ ژوئیه، نیروهای سپاه پاسداران چندین موشک بالستیک را از ایران، در تلاشی برای انجام یک حمله غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند. تمامی موشک‌های ایرانی با موفقیت رهگیری شدند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در خاورمیانه مستقرند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77637" target="_blank">📅 05:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پیام‌های دریافتی:
۴:۴۹ اهواز انفجار شدید
انفجار های وحشتناک و پشت سر هم در اهواز
خیلی وحشتناکه
پشت سر هم
حداقل ۴ انفجار
اهواز رو زدن صدای ۲ انفجار
اهواز و دارن میزنن شدید
صدای انفجار مهیب توی اهواز ۴:۴۹
همچنان ادامه داره
تا الان ۴ انفجار بلند
صدا انفجار پشت سر هم ۴ تا زد ۴:۴۹ اهواز مرکز شهر
سلام وحید ۴:۴۹ اهواز ۴تا صدای انفجار شدید اومد
اهواز سه تا انفجار ۴:۵۰
سلام وحید الان ساعت 4:50 اهواز زدن
5 بار صدای زیاد اومده تا الان
اهواز رو زد چهار بار الان!!!!
۴ تا انفجار سنگین ظرف ۲ دقیقه
همین الان اهواز چهارتا صدای انفجار شدید
ساعت ۴:۵۰
همین الان اهواز نمیدونم چند تا افتضاح بلنده
تمام شیشه ها داره میلرزه
اهواز همین الان ۶تا انفجار
۶ تا پشت سر هم اهواز
اهواز ۴.۵۰ دقیقه صدای ۵ انفجار شدید .
سلام وحید جان ۴:۴۹ ۵تا انفجار خیلی شدید اهواز
وحید واییییی خیلی بد بود چندبار زد اهوازو
۴:۵۰ وحشتناک نزدیک ۴ یا ۵ تا انفجار شدید شدید ماشینا به صدا درومدن
ما همین الان با صدای انفجار از خواب پریدیم اهواز ۴:۵۰
اهواز ۴تا اتفجارشدید پشت سر هم
اهواز تو چند دقیقه چندین انفجار شدید داشتیم و طوری که خونه میلرزید و برقمون هم به یک باره قطع شد
اهواز به گلستان خيلي نزديك بود ٤ بار
😭
😭
😭
سلام وحید جان، اهواز اطلاعات توی گلستان رو زدن ما اونجاییم
اهواز فکر کنم سپاه توی اتوبان گلستان بود، سایت اداری. ۴ انفجار.
اهواز کوی سعدی بعد انفجار دوم برق رفته الان ساعت ۴:۵۴
سلام وحید،4,49دقیقه4انفجارشدید دراهواز احتمالااسنگرشکن بودن،
سلام وحید جان ساعت ۴:۵۵ دقیقه صدای انفجار پشت هم از دور شنیده شد
ساختمان اطلاعات اهواز توی گلستان رو زدن
اهواز سمت سعدی و گلستان نورش بود،برق سعدی هم رفت
من اهوازم جفت خونمون چندتا پادگان هست الان زدن چهار بار
خیلی نزدیک بود و وحشتناک
اطلاعات اهواز واقع در پیچ گلستان  رو زدن
وحید تو کل جنگ همچین صدایی نمیومد اهواز به طرز عجیب و وحشتناکی زد در حدی که خونه میلرزه نه فقط پنجره ها
ساعت4:50دقیقه صبح هشتم مرداد
حفاظت اتوبان گلستان رو زدن
🔄
ترکوندنمون اقا وحید
این یکی خیییلیییی بد بووود
بازم انفجار اهواز. ساعت ۵:۲۲
صدای انفجار مهیب در اهواز 5:23
انفجار مجدد اهواز 5:23
5:23 اهواز انفجار خيلييييييىىى شديد
اهواز دوباره زدن شدیدتر از قبلیا
۵:۲۸ یکی دیگه
یه انفجار شدید دوباره اهواز
اهواز صدا انفجار دوباره
وحید همین الان اهواز رو زدن
وحید دوباره انفجار اهواز
وحشتناک همین الان
اهواز ۵ و ۲۳ دقیقه همین الان شرق اهواز صدای انفجار
مجددا اهواز ساعت ۵و ۲۲
۵:۲۱ یدونه صدا اومد،۵:۲۷ هم یکی دوتا صدا اومد
باز اهواز رو زد وحید
زیتون کارمندی ۲تا دیگه الان زد
اقا وحید دوباره زد اهواز
اهواز الان زدن دوباره شیشه ها لرزید
😭
خیلی صدا و‌لرزش داشتتتت
هم اکنون  بازهم زدن05:23
5:22دوباره اهواز و زدن
5,23حمله دوباره اهواز
سلام گلستان اهواز باز زدن.. ساعت ۵:۲۲، ۵:۲۷
5/22" بازم اهواز رو‌زدن شدید
۵:۲۳ اهوازو بازم زد
سلام ۱ انفجار دیگه گلستان اهواز ساعت 5:23
چرا ول نمیکنه
الان یکی دیگه زدن5:23
ساعت 5:22 انفجار شدید اهواز
سلام اهواز وحشتناک بود گلستان سعدی اگه چسب نداشتیم رو شیشه احتمالا شیشه های دو جداره خورد میشدن
ما هنوز برق نداریم
🙏🏼
🙏🏼
انفجار های آخری بشدت به ما نزدیک بودن
آسمون قرمز شده بود از اتیش و صدای ویراژ هواپیما میومد
راحت میچرخیدن
با انفجار دوم برق رفت
۵ و ۲۲ دوباره زد همین الان
🔄
الان دوبارههههه
یکی دیگه5:27
دو انفجار دیگه ۵:۲۸
دوباره زدن وحید
دوباره زد
خیلی شدیده
الان ساعت ۵:۲۸ دوباره بد زد
اهواز همین الان دوباره زدن خونه لرزید با همون شدت بود
باز الان صدا دو انفجار
۵:۲۸ دو صدای انفجار مجدد اهواز
بسیار شدید و لرزش شدید تر شیشه ها
دوتا انفجار دیگه تو اهواز ۵و ۲۸
آقا وحید انفجار به شدت  شدید موج های بسیار زیاد در خانه
بازم انفجار خیلی شدیدی اومد ساعت ۵:۲۸ خیلی ترسناکه
دوتا دیگه زد ۵:۲۷
بندرعباس ساعت 5.24صدای دوتا انفجار وحشتناک بندر
پایگاه هوایی رو دوباره زدن
به نظر میاد یک جا رو دارن چندین بار میزنن. احتمالا سمت گلستان
انفجارها پشت سر هم شدن دوباره
بازم دارن اهوازو میزنن خیلی وحشتناک تر
همچنان داره میزنه
۵:۳۰ دوتا انفجار شدید
سلام اهواز بد دارن میزنن برق رفته مثل اینکه اطلاعات سپاه زدن
هر ده دیقه یبار تا خوابمون میره یه قلمبه میزنن
افتضاحه خیلی نزدیکه صداش
همه شهر حسش می‌کنه
اهواز، همون اطلاعات توی گلستان رو همچنان دارن میزنن
۵:۳۵ اهواز
بازم انفجار سنگین
همه شهر رو بیدار کرد!
یجوری اطراف مارو زدن که کل هوش و حواسم پرید حالمون بده و دقیقا ۱ ساعت دیگه باید سر جلسه امتحان باشیم ...
اهوازیم .
پمپاران در اهواز تمام نمیشه مرتب داره میزنه
سلام وحید جان.
خواهر من دانشگاه علوم‌پزشکی جندی‌شاپور می‌خونه. خوابگاهشون  توی گلستانه، روبه‌روی اطلاعات. می‌گه بعد از انفجارهای مهیب و‌ پی‌در‌پی اهواز شیشه‌ی اناق‌ها شکسته و   همه‌ی بچه‌های خوابگاهی هراسون توی محوطه جمع شده‌ن.
صدای دانش آموزان خوزستانی باشید
نیم ساعت دیگه چطور به سمت حوزه های امتحانی راهی شوند؟؟
🔄
دوباره اهواز رو زد 5:43
ساعت 5:43 دقیقه ی انفجار
بازم زد همین الان صداش دور بود
اهواز ۵:۴۲ مجدد زدن
ساعت ۵.۴۳ صدای دو انفجار در اهواز
دوتا دیگه اهواز رو زد
وحید دوتا دیگه
بازم زد این یکی لرزشش بیشتر بود
.۵:۴۳ گلستان اهواز دور بود ولی دوبار زد
دو انفجار مهیب دیگه در اهواز
تمام خونه و شیشه‌هاش لرزید
اهواز ساعت ۵:۴۳ دقیقه صدای انفجار
اهواز ۵:۴۳ شدید ترین انفجار از ساعت شروع حملات بود
😭
یکی دیگه
سمت شرق خیلی شدید بووود
دوباره انفجار در اهواز ۵:۴۲
سلام همین الان ساعت۵:۴۳ دقیقه روز پنجشنبه  اهواز و زدن
ملی راه هستیم صدا خیلی نزدیک بود
۵:۴۳اهواز ۲انفجاد شدید دیگر
بسیار شدید سمت کیانشهر‌اهواز، دزدگیرا به صدا در اومدن و خونه کامل لرزید
۲ انفجار پشت هم اهواز خیلی سنگینن انفجارهاش
شدید کیانشهر ۵و۴۴دقیقه
صدای انفجار اهواز همین الان ساعت ۵:۴۳ صبح
وحید بازم زد اهوازو دو تا ۵:۴۳
اهواز، ۵:۴۳ …این یکی شدیدتر از بقیه بود
5:42 صداى انفجار در اهواز
ساعت ۵/۴۲ دقیقه انفجار فوق شدید در پدافند اهواز کیانشهر
5:44 یکی دیگه اهواز
دوباره اهواز انفجار شدید ساعت ۵:۴۴
وحید جان الان دوباره صدای انفجار اومد دوبار پشت سر هم اهواز
وحید زد همین الان زیتون اهواز لرزید
وحید مجدد زد دو بار یه صدا انفجار دیگه هم اومد اما لرزش نداشت و نزدیک بود خیلی ساعت 5.44
سمت کیان ابادیم ما شدید صدا اومد ۵و ۴۴ دقیقه
همین الان اهواز کیانشهرو زدن
جفت پدافند
ما کیانشهریم
فکردیم داخل خونمون رو زدن
تا الان ۸بار اهواز رو زدن ۶تاش اطلاعات اهواز بود دوتا دیگه خیلی دور بود معلوم نبود کجا بود
انفجار آخر پدافند بود کنار میدان تره بار
سلام وحید بالای۸انفجار در اهواز رخ داد صداهای خیلی وحشتناکی داشت تروخدا صدای مارو به برسونید بچه ها نیم ساعت دیگه باید برن امتحان بدن گناه دارن اهواز رو ترکوندن
اهواز هم ۴:۴۸ دیقه هم ۴:۵۰ دیقه
هم ۵:۲۰ دیقه هم ۵:۲۸ دیقه
دوتای دیگه هم الان ۵:۴۳
مجموعا حدود ۱۳ تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77636" target="_blank">📅 04:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myt-jLsHLXfUjdPSpkTj35lemHrg2xofbvjk29PbvELWlsuY3aQq9iaNbRiITtpigzgMvxqFPCM2dMDLFby3qL8lWalh1dZWpEVaCPIY8YczoBU-jOnA9C7fkaFRdReq5yVuGiNbd_IFJDcXa_T74uFwmcx8luHSrcfoRxlf9tisnhl9Jy9mFs15VGuJxZoBEMTmfY90ono31Dhq7HDiDotSA3JxZRqr2HNiabpzU_Sy7tTNxUUdM2olXaPAqdN4XpQEypejWVNYptoR4IQPPo4m0TWnDnmNnr4PjwcutZguN68GFE37s-iy7f06fXOreC1Kx4g6vXHCcbcdiqtLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم، در پی شنیده شدن صدای انفجار در استان فارس، منطقه‌ای در اطراف شهر کازرون هدف حمله قرار گرفته است.
پیش از این رسانه‌های داخلی ایران از شنیده شدن صدای چندین انفجار درنورآباد استان فارس خبر دادند.
@
VahidOOnLine
پیام‌هایی که من دریافت کره بودم:
درود کازرون خونه ی ما لرزید
در نزدیکی کازرون صدای چند انفجار اومد ۳:۴۲
ساعت 3:41 - 3:42
کازرون چند تا صدای انفجار شدید اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77635" target="_blank">📅 04:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیام‌های دریافتی:
‌
۴:۳۵ قشم دو انفجار
۰۴:۳۶ دو انفجار بندرعباس
وحید دوتا انفجار جدید بندر همین الان۴.۳۷
بندرعباس ۲ تا انفجار در حد لرزش در و پنجره ساعت ۴.۳۷
۰۴:۳۶ دو انفجار بندرعباس
صدای انفجار بندرعباس
دو انفجار شدید بندر عباس ۴:۳۷
بندرعباس شدید تر از قبل
دوتا همین الان
۴ تا انفجار مجدد بندرعباس ۴.۳۷ دقیقه
وحید جان صدای دو انفجار در بندرعباس ساعت 4.37
بندرعباس مجدد صدای مهیب ساعت ۴:۳۷
بندرعباس الان ساعت ۴:۳۷ صدای انفجار
وحید ۴:۳۷ زدن بندرعباس ۲ تا شدید موج داشت
الانم دوتا سنگین زدن از خواب پریدیم 4:36
سلام وحید جان همین الان دوباره صدای انفجار میشنویم
دو انفجار شدید همین الان بندرعباس
دوباره بندرعباس انفجار به همون اندازه ۳.۳۸
صدای سومی اومد شدیدتر۴.۳۸
دوباره ۴:۳۸
🔄
دوباره انفجار پشت سرهم ۴.۴۳
همین الان انفجار دوباره
درود ۲ دیگه زد ۴.۴۳ بندرعباس
چند تا دیگه هم زدن همین الان
دوباره ۴:۴۳ بندرعباس
این جدیدا فقط موج دارن
بندرعباس ساعت ۴:۴۳ صدای انفجار شدید
محله چاه تنگو درگهان چن تا خونه دچار آسیب شده انگاری ک زیر آوار موندن کسی بعد انفجار
ساعت ۵ و ۱۰ دقیقه باز قشم زدن
قشم محله ی نریمان،  زیرانگی و محله چاهتنگو رو زدن.. یه دکل هم زدن
سلام وحید داخل قشم محله چاه تنگو  یه خونه مسکونی رو زدن الان رفتم راه رو بستن معلوم نیست فعلا کی داخلش بود ولی خونه پودر شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77634" target="_blank">📅 04:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8HsuinkVUEywXPIIHRxocBGdJdiIhM6gJbcjtDHxL_46AQXYqMW2CRrPPcePgh8faOkMiCsioYEcHMs3mE4nkHveziseG399Jd1lNhJFZc0lV6w9oyaPMc7NxbhpuCtkylOhao2BTualDgZzzbeP44Mbgd6IaZHpX8hUrJeQc1-nP_B1Cr-cQ6gPiT6ZeK2CvKy53wfr8lNijZOcc1nraYFBWXWUOxLbmf7hUT_19bF6K--vvTDqvn6NpUVNDcMzKCMmrqBPmEdYTEqBphuX65ub-GHzXVvo2QP0G-5SUzurDb-IGNT0VEou72BLPlf2tXKZrl8D7jK1JlqkTgSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای ایالات متحده امروز ساعت ۸ شب به وقت شرق آمریکا [۳:۳۰ بامداد پنج‌شنبه به وقت تهران] حملات علیه ایران را آغاز کردند.
این حملات، پاسخی قدرتمند به تلاش‌های دیروز ایران برای حمله به نیروهای آمریکایی مستقر در خاورمیانه است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77633" target="_blank">📅 03:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان بندرعباس صدای 2 انفجار
3:40
سلام ۳ و ۴۰ دقیقه بندرعباس دوتا انفجار
۰۳:۳۹
بندرعباس
حداقل ۲ انفجار
درود
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
۴ ۵ تا انفجار توی کمتر از ۱ دقیقه بندرعباس
سه تا انفجار ذیگر
همین الان ۳:۴۱ صدای چند انفجار در بندرعباس
دوباره یک انفجار دیگه 3:41
دوباره یکی دیگه تند تند دارن می زنن
صدای انفجار بزرگ همراه با لرزه زمین بندرعباس
3:41 همین الان بندرعباسو دارن میزنن در و پنجره میلرزه
دو انفجار شدیدتر ساعت 3:41
بندرعباس صدای سه انفجار اومد ساعت ٠٣:٤١
سلام وحید جان همین الان انفجار شدید بندرعباس
سلام وحید جان بندرعباس رو داره میزنه سمت فرودگاه و پایگاه هوایی رو
قشم ساعت ۳و ۴۰ دقیقه انفجار در حد لرزش خونه ها
قشم همین الان با جنگنده بمب بارون شد
صدای سه انفجار شدید در شهر قشم
بندرعباس رو زدن همین الان ۲ تا صدای انفجار
شد ۴ تا
بندرعباس دو انفجار مهیب ادامه دار
صدا دور بود 3: 40
سلام وحید جان الان ساعت ۳ و ۴۰ دقیقه صدای انفجار اومد قشم ،برق ها نوسان پیدا کرد
بندرعباس همینننننن الانننننن خیلی شدید یا خدا
همین الان که دارم تایپ میکنم زدن
همین الان 3:40 دقیقه قشم با صدای انفجار بیدار شدیم
قشم صدا میاد پشت هم
سلام صدای انفجار۳:۴۳ شدید تر از قبلی
۳.۴۱ بندرعباس صدای انفجار
یه انفجار بزرگتر تر
با موجش در و پنجره لرزید
بندرعباس ۳.۴۳
قشم 2 انفجار نزدیک شهر
بندرعباس الان دوباره صدا اومد و خونه لرزید ۳ و ۴۳
بندرعباس ۵ تا انفجار پشت سر هم
انفجار بندرعباس ۲ تا شدیدددد بود صداش الان ۳.۴۲
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77632" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
بوشهر زدن
بوشهر چندتا صدای انفجار اومد
جم همین الان دارن میزنن
۵ تا زد
دوتا صدای انفجار اومد
بوشهر ستا انفجار ۰۳:۳۸
سایت موشکی برازجان رو زد الان.ساعت ۳:۳۷
بوشهر، جغادکیم
همبن الان از خواب پریدم
دو صدای خیلی بلند
سلام ‌وحید ساعت۳:۳۰ چندتا صدای انفجار شنیدیم صدا خیلی زیاد بود پنجره هامون انگار تکون خورد
سلام برازجان همین الان صدای جنگنده و یک انفجار
وحید جان جم الان چندتا صدای انفجار با لرزش اومد
ٰ3:38
بوشهر دارن میزنن
درود، سه بار جم صدا اومد.
۵ انفجار بوشهر همین الان ۳:۴۰دقیقه
بوشهر -چغادک ۴ انفجار ۰۳.۳۷
اقا وحید بوشهر چند تا صدای انفجار شنیده میشه
ولی خیلی صداش دوره
سلام آقا وحید ساعت ۳:۳۸ دقیقه بوشهر رو زدن
صدای جنگنده توی برازجون چند دقیقه هست که تموم نشده و هی بلند تر میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77631" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان سه انفجار در کیش
کیشو زدن همین الان ۳:۳۱
کیش دم بندرگاه ساعت ٣:٣٠ ٢ تا زدن
وحید جان کیش ۲ تا ۳:۳۲
سلام وحید
کیش رو الان زد
دوتا انفجار
وحید الان کیشو زد
۰۳و۳۰ دقیقه انگار  تووآب بود
سلام وحید کیش همین الان صدا اومد
سلام وحید جان
همین الان ۳۱:۰۳ کیش صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77630" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=MVh-uDGxm4K4CWO7Nls2pzHmPVBE1sPZNyrxMS6U8o06-pMHad7yY7m9trRjx9qM3MB7MSm16CB13oBeY3Hq6gKzI8hnJTqpBsC8-qVlw7h4wSRp8F4nNJNDdPH1qdUXtMvybEAc7FttfG03O7L6KfjBP97UrerOYMZZuUfBmv1plL-4HWPHxRM3Z5CeSW8cJPr7i-BgJ9IEb1PMu8SABFCPqVI-dFgrVtDmb8GQxzEROZ1nLHLYFV_rNeUp6fygEraZtN3rJH7lvGwK8RhjQFxHFCRaaHPI9np9y1qO2TNoKoBqZZBa8FKOu4IXEHbweOGdoNBidRJSQQjeBk64yA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=MVh-uDGxm4K4CWO7Nls2pzHmPVBE1sPZNyrxMS6U8o06-pMHad7yY7m9trRjx9qM3MB7MSm16CB13oBeY3Hq6gKzI8hnJTqpBsC8-qVlw7h4wSRp8F4nNJNDdPH1qdUXtMvybEAc7FttfG03O7L6KfjBP97UrerOYMZZuUfBmv1plL-4HWPHxRM3Z5CeSW8cJPr7i-BgJ9IEb1PMu8SABFCPqVI-dFgrVtDmb8GQxzEROZ1nLHLYFV_rNeUp6fygEraZtN3rJH7lvGwK8RhjQFxHFCRaaHPI9np9y1qO2TNoKoBqZZBa8FKOu4IXEHbweOGdoNBidRJSQQjeBk64yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
آبادان ترکوندن
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
صدای انفجار آبادان
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
سلام وحیدجان همین الان چهار بار صدای موشک شنیدیم آبادان ساعت ۰۳:۳۲
سلام آقا وحید تا الان آبادان ۸ بار صدای انفجار اومد ۳:۳۰ دقیقه
احتمالا دارن موشک هوا میکنن
سلام وحید، آبادان ساعت ۳:۳۱ پنج شیش تا صدای انفجار بلند شنیدیم
وحید سلام
۶ تا صدای انفجار
همین تلان ، ابادان
وحید سرساعت ساعت ۳:۳۰ ابادان صدای چندتا صدای انفجار اومد ولی دوره احتمالا خارج از شهره
حداقل ده تا انفجار آبادان ساعت ۳:۳۰
از ساعت ۳:۲۰ شروع شد
اقا وحيد صداي ٦ انفجار ساعت ٣:٣٠صبح در ابادان
وحید آبادان ۵ تا انفجار شدید ۳:۲۸
همین الان صدای ۶ الی ۷ تا انفجار از آبادان اومد
ساعت ۳.۳۰ بامداد
آبادان نزدیک ۴/۵ تا صدا شنیدم ... برای اطمینان حتی به دوستمم گفتم اونم شنیده
۳:۳۳ آبادان رو بیشتر از ۵بار زد. بیرون شهر یه چیزی آتیش گرفته، نمیدونم کجاست
آقا وحید آبادان رو ساعت سه نیم زدن شیش تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77629" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAvsxeMNkP3EIG1UQXSDN40s1anfMiKGVm5JgnZWi6FRmsBspYX_CZvAQ9Uon7npWUN9XmZ9PCNNMVaJOg-LmAkl72akvKmjCO-4b7weYKb21XSdUwm45CNqTSSJg_5cDX7RhqA7-SvW5Dk4ZhNtAX86SHHT_cBWHxwWCFGhChtadQr3VUIMIJ5k4X6TKN1fndEDxlcIWrr_B2pCiVf-866Rj8gp5gsLt5A5BEXfbUrsmdhIbCtYYgI8q1uKGw8X4wPGvrDnd2ObdZ5xACLFX0ETDxBwt4Pf4Br99ZKm4URAy8nw5PFTz6pfWahYa9d1VQQ1dN1Ip6spQmr77cpdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست خبرنگار اکسیوس:
یک مقام آمریکایی به من می‌گوید ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
BarakRavid
آپدیت:
بعدا همین گزارش در خود اکسیوس:
ترجمه ماشین: یک مقام آمریکایی به اکسیوس می‌گوید ارتش آمریکا روز چهارشنبه اجرای حملات هوایی در ایران را آغاز کرد.
چرا اهمیت دارد: این نخستین حملات آمریکا در ایران از زمانی است که دونالد ترامپ، رئیس‌جمهوری آمریکا، جمعه گذشته کارزار بمباران را متوقف کرد تا فرصت دیگری به مذاکرات بدهد.
حملات روز چهارشنبه در تلافی حمله موشکی ایران در روز قبل انجام شد که یک پایگاه آمریکا در اردن را هدف قرار داده بود. به گفته ارتش آمریکا، همه موشک‌ها رهگیری شدند.
محور خبر: ترامپ بعدازظهر چهارشنبه به خبرنگاران گفت که آمریکا در ادامه همان روز ایران را «بسیار سخت» هدف قرار خواهد داد.
ترامپ گفت: «حالا نوبت ماست.»
ترامپ مدعی شد ایران پذیرفته است که شلیک موشک‌ها اشتباه بوده و از آمریکا خواسته است تلافی نکند.
تصویر کلی: ترامپ پس از ۱۳ شب متوالی حمله به اهداف نظامی ایران، حملات را متوقف کرده و فرصت کوتاهی برای دیپلماسی ایجاد کرده بود.
حمله موشکی ایران این وقفه را درهم شکست و ترامپ را واداشت پنج روز بعد کارزار نظامی را از سر بگیرد.
یادداشت سردبیر: این یک خبر فوری است. برای دریافت تازه‌ترین اطلاعات دوباره مراجعه کنید.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77628" target="_blank">📅 02:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده از ساعت ۲:۱۹
سلام وحید جان صدا ۳ تا انفجار شنیدیم نوراباد فارس
۳ تا انفجار همین الان نوراباد ممسنی
آقا. وحید نورآباد ممسنی رو بد زدن
۳ تا شیشه ها لریزد
وحید همین الان نور آباد صدای انفجار اومد ۳ تا بود دقیقن
وحید جان چند لحظه قبل صدا چندتا انجار شدید نوراباد فارس
آقا وحید نوراباد ممسنی رو زدن
صدا هواپیما هم میاد
وحید همین الان نور آبادو زدن
🔄
پیام‌های ساعت ۲:۲۴:
اوه یدونه دیگه
یدونه دیگه ام زدن
البته دور بود
وحید بازم زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77627" target="_blank">📅 02:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیام‌های دریافتی شاید درباره پرتاب شدن موشک که با صدای جنگنده اشتباه گرفته میشه:
یزد الان صدا جنگنده اومد
ساعت ۱۲:۱۰
صدای جنگنده روی آسمان یزد
الان یزد صدای جنگنده امد خیلیم پایین پرواز میکرد صدای انفجاری نیومد اگر بیرون شهر زده نمیدونم
سلام وحید جان
۰۰:۰۷  از تنگه یه صدایی اومد مثل انفجار
شایدم لانچ بالستیک بود
ده دقیقه پیش از یزد موشک بلند شد
وحید جان صدای جنگنده میاد یزد
آپدیت:
پیام‌های دریافتی  بعد از انتشار پست:
یزد هواپیما رد شد
موشک و جنگنده نبود
ارتفاع به شدت پایین
سلام یزد جنگنده خودی بود
سلام وحید جان صدایی که از یزد میومد مال هواپیمای مسافربری بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77626" target="_blank">📅 00:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXpQA0Lb7bEqpUSeHs4nXcCGHop9H0PjseDjJ_yLjv8Hu77nMRfbnxX7JT7rVc8DAZwN4oK6Twx-J7bHLixXLyrdNNfX6sgOzoDf3Ha2jcfcr7Ayy_P3GMpc0LJua9qIBCFXUQP-EyZNv4y0xAt3eibg4m8jE4oOh8UahZi7BnnA77ustCM0OoQwpC4p9E3s--kh8KUhbDd9nlVRImNcftUTO4hGfo2CzQmVL199C5oB8tLE2f-v7MUzIb3oEkBB3w8Fm3ZMle5EOZ9MxjxfDNU4E4KeSTRkMfjz0GdyNpoCZvYJtzfKbxoaJdHAlgEOwPgaRQIZIwvOCGjL42W88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس نوشت «رژیم ایران که با سقوط آزاد اقتصاد و تورم سه‌رقمی روبه‌رو است، به‌شدت به منابع مالی نیاز دارد».
او تاکید کرد «ایالات متحده اجازه نخواهد داد ایران تجارت جهانی را گروگان بگیرد یا از کشتیرانی بین‌المللی برای تامین مالی «سپاه پاسداران»، اقدامات تهاجمی و سرکوب استفاده کند».
پیش از این، وزارت خزانه‌داری آمریکا چندین بسته تحریمی علیه افراد، شرکت‌ها، نفتکش‌ها و شبکه‌های مرتبط با صادرات نفت ایران اعمال کرده و اعلام کرده بود این اقدامات با هدف محدود کردن منابع مالی جمهوری اسلامی و سپاه پاسداران انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77625" target="_blank">📅 00:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c878874010.mp4?token=uFpId7K-qhdXsMPHMLvx0mctNCOb93EZlfOAniKWVso17xzLdRgQii663CP1ghXRVJKu3auoU7VX47f7SkME2o-_FCFsICK_G_NPQYpFSUzjfYxkzD4iaHGmx8pf3pFApC0RlcpvGjwx3r7lgmBPeQSB3VKFXg51nO-By6kX2__g8hwPGTdXqPCs9WqXO6AEsRvv1LoVogpvCeWNzJlivFxeOh591LGrqPQAqyx_G1xbC429zk0d-4EOFcRdOG_Ka9RmQM-y6elUsm2A2_JksEXUxHHj9ZExvY9h_OIQjK6mhy5-JZQr3d6Ig6XA7_JnfV6YRO_asaaAXxE0IJlinA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c878874010.mp4?token=uFpId7K-qhdXsMPHMLvx0mctNCOb93EZlfOAniKWVso17xzLdRgQii663CP1ghXRVJKu3auoU7VX47f7SkME2o-_FCFsICK_G_NPQYpFSUzjfYxkzD4iaHGmx8pf3pFApC0RlcpvGjwx3r7lgmBPeQSB3VKFXg51nO-By6kX2__g8hwPGTdXqPCs9WqXO6AEsRvv1LoVogpvCeWNzJlivFxeOh591LGrqPQAqyx_G1xbC429zk0d-4EOFcRdOG_Ka9RmQM-y6elUsm2A2_JksEXUxHHj9ZExvY9h_OIQjK6mhy5-JZQr3d6Ig6XA7_JnfV6YRO_asaaAXxE0IJlinA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از گفت‌وگوی ترامپ با خبرنگاران در کاخ سفید، ترجمه ماشین:
خبرنگار: در مورد حمله پهپادی به نفتکش LNG در سواحل مصر چه اطلاعاتی دارید؟ آیا نشانه‌ای وجود دارد که این حمله به ایران مربوط باشد؟
ترامپ: خب، می‌توانم گزارشی به شما بدهم. در این باره توجیه شده‌ام. این کمی از همان ماجراست، اما اوضاع رو به صاف‌شدن است؛ وضعیت دارد روشن می‌شود. در این میان، ما قرار است ضربه بسیار سختی به آنها بزنیم، چون نوبت ماست که ضربه بزنیم. آنها می‌دانند که این حمله در راه است و از ما می‌خواهند این کار را نکنیم. اما دیشب سعی کردند به آن شلیک کنند.
ما پنج موشک داشتیم که با سرعت ۸۵۰۰ مایل در ساعت در حرکت بودند و هر پنج موشک سرنگون شدند؛ اما با این حال آنها شلیک کردند. پس نوبت ماست. خواهیم دید که آیا در مقطعی به یک توافق می‌رسیم یا نه، اما ضربه بسیار سختی به آنها خواهیم زد.
—-
خبرنگار: در چه سناریویی تصور می‌کنید ایران به تأسیسات و پرسنل آمریکا در خارج حمله کند و شما عقب‌نشینی کنید؟
ترامپ: چنین چیزی را نمی‌بینم. نه، ما عقب‌نشینی نمی‌کنیم. ضربه سختی به آنها خواهیم زد. واقعاً می‌توانم این را بگویم، چون آنها در این مورد کار زیادی نمی‌توانند انجام دهند.
این گروه با گروهی که ما با آن سروکار داریم متفاوت بود. آنها قبلاً عذرخواهی کرده‌اند، اما باید یک ضربه‌ای به آنها بزنیم.
خبرنگار: وقتی آنها حمله می‌کنند، آیا همیشه پاسخ خواهید داد؟
ترامپ: بله، تقریباً.
خبرنگار: آقای رئیس‌جمهور، آیا این در پاسخ به حمله موشکی بالستیک شب گذشته به اردن است؟ وقتی می‌گویید نوبت ماست که ضربه بزنیم.
ترامپ: بله، فکر می‌کنم بیشتر به آن مربوط می‌شود. آن رویداد کوچک‌تری بود، اما آنها پنج موشک با سرعت ۸۰۰۰ مایل در ساعت به سمت ما شلیک کردند. خوشبختانه افرادی را داشتیم که بهترین تجهیزات جهان، یعنی سامانه پاتریوت، را به کار می‌گرفتند.
فکرش را بکنید؛ پنج موشک بزرگ با سرعت ۸۶۰۰ مایل در ساعت مستقیماً به سمت ما می‌آمدند و هر پنج موشک سرنگون شدند. چطور است؟ خیلی خوب است. فقط ما می‌توانستیم این کار را انجام دهیم؛ هیچ‌کس دیگری نمی‌توانست.
—-
خبرنگار: آقای رئیس‌جمهور، در مورد جنگ، آیا می‌خواهید مجلس نمایندگان پیش از ۳۱ اوت برای رسیدگی به لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: اگر لازم باشد، بله؛ هرچند راستش نباید لازم باشد. آیا منظورتان طرح لینزی گراهام است؟
خبرنگار: بله.
ترامپ: می‌خواهم ایران را هم به تعرفه‌ها اضافه کنند، نه فقط به تحریم‌ها. فکر می‌کنم این مهم است و همان چیزی است که لینزی می‌خواست. شنیده‌ام روی روسیه تعرفه گذاشته‌اند، اما روی آن پنج کشوری که به ایران مربوط می‌شوند تعرفه‌ای نگذاشته‌اند.
دوست دارم تعرفه‌هایی علیه ایران ببینم. این موضوع را بسیار قوی‌تر می‌کند. شاید بتوانید به آنها بگویید که به نظر من باید برای روسیه تعرفه بگذارند، اما برای ایران هم باید تعرفه در نظر بگیرند. این دقیقاً همان چیزی بود که لینزی می‌خواست.
——
خبرنگار:  رئیس‌جمهور شی به شما گفته بود که چین هیچ سلاحی به ایران نخواهد داد یا نخواهد فروخت. اکنون گزارش جدیدی منتشر شده که می‌گوید ایران قرار است ۴۰۰ پرتابگر موشک از چین و از طریق پاکستان دریافت کند.
ترامپ: خب، این تعجب‌آور خواهد بود. چنین چیزهایی پیش می‌آید، اما واقعاً تعجب‌آور خواهد بود. او خیلی قاطع به من گفت که در این کار مشارکت نخواهد کرد و می‌داند که من کاملاً ناامید خواهم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77624" target="_blank">📅 23:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اکسیوس:
پشت پرده دیدار تعیین‌کننده «بی‌بی» با ترامپ در کاخ سفید
ترجمه ماشین:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در دیدار خود با رئیس‌جمهور ترامپ درباره احتمال دستیابی به توافقی با ایران ابراز تردید کرد و درباره افزایش فشار اقتصادی بر ایران «از طریق ابزارهای نظامی و غیرنظامی» به گفت‌وگو پرداخت؛ یک مقام ارشد اسرائیلی این موضوع را در نشستی با خبرنگاران بیان کرد.
اهمیت موضوع:
دیدار روز سه‌شنبه نخستین ملاقات نتانیاهو و ترامپ از زمان آغاز جنگ در ۲۸ فوریه بود. این دیدار در حالی انجام شد که ترامپ همچنان برای دستیابی به توافقی با ایران تلاش می‌کند، اما هم‌زمان بازگشت به عملیات رزمی گسترده را نیز در نظر دارد.
▪️
چند ساعت پس از این نشست، ایران برای نخستین بار از زمانی که ترامپ روز جمعه حملات آمریکا در ایران را متوقف کرد، یک حمله موشکی علیه پایگاهی آمریکایی در اردن انجام داد.
▪️
ترامپ روز چهارشنبه در مصاحبه‌ای با فاکس‌نیوز وعده داد که پاسخی جدی خواهد داد. حمله غافلگیرانه ایران ممکن است رئیس‌جمهور را به سوی تشدید تمام‌عیار درگیری سوق دهد.
▪️
مقام اسرائیلی گفت نتانیاهو در انتظار تصمیم ترامپ است، اما به‌روشنی به او گفته است که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری و قدرتمند خواهد بود.
آنچه در اتاق گذشت:
ایران موضوع اصلی گفت‌وگوی ۹۰ دقیقه‌ای بود.
▪️
مقام اسرائیلی گفت آن‌ها سه گزینه‌ای را که ترامپ برای گام‌های بعدی در نظر دارد بررسی کردند:
۱. دستیابی به توافق با ایران.
استیو ویتکاف و جرد کوشنر، فرستادگان ترامپ، همچنان با ایرانی‌ها مذاکره می‌کنند، هرچند در حال حاضر اختلاف‌ها همچنان گسترده به نظر می‌رسد. مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است که نسبت به امکان دستیابی به توافق با ایرانی‌ها تردید دارد.
۲. ادامه محاصره دریایی ایران
هم‌زمان با افزایش فشار اقتصادی.
۳. ازسرگیری و تشدید حملات نظامی.
▪️
این مقام گفت: «همه این گزینه‌ها را به‌طور مفصل و بسیار صریح بررسی کردیم؛ نه با هدف ترجیح دادن یک گزینه بر گزینه‌ای دیگر، بلکه برای بررسی اینکه هرکدام چه نتیجه مطلوبی می‌تواند داشته باشد. موضوع گفت‌وگو همین بود.»
نمای نزدیک:
مقام اسرائیلی گفت ترامپ درباره تأثیر جنگ بر بازارهای انرژی و اقتصاد جهانی ابراز نگرانی کرد.
▪️
نتانیاهو به ترامپ گفت حکومت ایران عمدتاً می‌کوشد از تنها اهرمی که برایش باقی مانده است — تنگه هرمز — برای وادار کردن آمریکا به دادن امتیاز استفاده کند.
▪️
مقام اسرائیلی گفت نتانیاهو نگرانی‌های ترامپ را نادیده نگرفت، اما به او گفت راه‌هایی برای افزایش بیشتر فشار بر اقتصاد ایران وجود دارد؛ اقتصادی که هم‌اکنون نیز تحت فشار شدیدی قرار دارد.
▪️
مقام اسرائیلی گفت: «درباره افزایش فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی گفت‌وگو کردیم. درباره امکان ادامه محاصره با هدف تحت فشار قرار دادن ایران صحبت کردیم.»
▪️
مقام اسرائیلی گفت در درون رهبری ایران میان کسانی که به‌شدت نگران فروپاشی اقتصادی هستند و عناصر تندروتری که معتقدند تا زمانی که کنترل تسلیحات را در اختیار دارند و می‌توانند از پایگاه حامیان حکومت پشتیبانی کنند مشکلی ندارند، اختلاف‌نظر وجود دارد.
▪️
مقام اسرائیلی افزود: «آن‌ها با مشکلات تأمین سوخت، صف‌های طولانی در پمپ‌بنزین‌ها و کمبود گازوئیل روبه‌رو هستند. اعتراض‌های کوچکی شکل گرفته است، زیرا مردم به‌شدت ناراضی‌اند. حکومت بسیار نگران این وضعیت است و می‌ترسد مردم به‌دلیل شرایط اقتصادی قیام کنند.»
پشت صحنه:
مقام اسرائیلی گفت مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، «درباره همه‌چیز» موضعی بسیار منفی دارد، اما مشخص نیست دستورهایی که به او نسبت داده می‌شود واقعاً از جانب خود او صادر می‌شود یا نه.
▪️
مقام اسرائیلی مدعی شد: «او زنده است، اما هیچ‌کس نمی‌تواند شهادت دهد که واقعاً او را دیده است. به اطرافیانش گفته بدون تأیید او هیچ کاری انجام ندهند و حتی گفته می‌شود یک بار وقتی بدون اجازه‌اش کاری کردند، عصبانی شد.»
نمای دور:
مقام اسرائیلی گفت نتانیاهو نقشه‌ای از سوریه را به ترامپ نشان داد که براساس آن، مناطقی که ترکیه در سوریه کنترل می‌کند «۵۰ برابر بزرگ‌تر» از مناطق تحت اشغال اسرائیل است.
▪️
مقام اسرائیلی مدعی شد ترکیه ۵ درصد از خاک سوریه را کنترل می‌کند، در حالی که اسرائیل ۰٫۱ درصد آن را در اختیار دارد.
▪️
یک مقام آمریکایی گفت برخلاف اشغالگری اسرائیل در جنوب سوریه، حضور نظامی ترکیه در شمال سوریه در حال حاضر با رضایت و به دعوت دولت سوریه انجام می‌شود.
▪️
مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است اسرائیل تا زمانی که تهدیدی از جانب «گروه‌های جهادی» وجود داشته باشد، حضور خود را در «منطقه حائل» جنوب سوریه حفظ خواهد کرد.
▪️
مقام اسرائیلی گفت: «نتانیاهو می‌خواست این موضوع را به ترامپ نشان دهد، زیرا او گاهی براساس اطلاعات نادرستی که بعضی افراد در اختیارش می‌گذارند، به دیدگاه‌های مشخصی می‌رسد. اگر در همان مراحل اولیه راهی برای تغییر نظرش پیدا نکنید، آن نظر تثبیت می‌شود. بنابراین می‌خواستیم واقعیت‌ها را، در صورت امکان به‌شکل تصویری، به او نشان دهیم.»
▪️
مقام اسرائیلی گفت نتانیاهو همچنین درباره توافق هسته‌ای آمریکا و عربستان سعودی با ترامپ گفت‌وگو کرد. ترامپ به نتانیاهو گفت این توافق را در چارچوب عادی‌سازی روابط عربستان سعودی با اسرائیل می‌بیند.
▪️
مقام اسرائیلی گفت: «اگر شاهد پیشرفت واقعی باشیم، درباره موضوع هسته‌ای حرف‌هایی برای گفتن خواهیم داشت.»
تصویر کلی:
مقام اسرائیلی گفت نتانیاهو به ترامپ، معاون رئیس‌جمهور ونس و ویتکاف گفته است که درباره کاهش کمک‌های نظامی آمریکا به اسرائیل تا رسیدن به صفر ظرف ۱۰ سال جدی است. او تأکید کرد که خواهان پیشبرد مذاکرات برای تدوین یک تفاهم‌نامه در این زمینه است.
▪️
مقام اسرائیلی گفت ترامپ و اعضای تیمش اعلام کردند بازخوردهایی از جمهوری‌خواهانی دریافت کرده‌اند که نگران‌اند به‌دلیل حمایت از حذف تدریجی کمک‌ها، به ضدیت با اسرائیل متهم شوند.
▪️
نتانیاهو به آن‌ها گفت شخصاً و به‌صورت علنی رهبری این تلاش را بر عهده خواهد گرفت، زیرا می‌خواهد اسرائیل به استقلال دفاعی دست یابد.
▪️
مقام اسرائیلی گفت: «درباره یک فرایند ۱۰ ساله صحبت می‌کنیم. از پیشنهادها استقبال می‌کنیم و شاید این اتفاق بتواند سریع‌تر رخ دهد.»
▪️
این مقام حتی گفت نتانیاهو به بخش دفاعی اسرائیل دستور داده است روی ساخت یک جنگنده مدرن ظرف یک دهه کار کند تا نیروی هوایی این کشور حتی در صورت توقف تحویل جنگنده‌های اف‌ـ۳۵ و دیگر هواپیماهای پیشرفته از سوی آمریکا، همچنان قدرتمند باقی بماند.
▪️
این مقام گفت نتانیاهو نمی‌خواهد اسرائیل به «حسن نیت کنگره آمریکا» وابسته باشد، زیرا معتقد است جهت‌گیری سیاسی هر دو حزب درباره کمک‌های نظامی در حال منفی‌تر شدن است.
▪️
نتانیاهو معتقد است وضعیت اقتصادی اسرائیل به این کشور اجازه می‌دهد کمک‌های نظامی آمریکا را به‌تدریج کنار بگذارد. مقام اسرائیلی گفت نتانیاهو پیشنهاد کرده است تفاهم‌نامه جدید شامل ۱۶ میلیارد دلار کمک نظامی مستقیم آمریکا و همچنین ۵ تا ۱۰ میلیارد دلار حمایت از توسعه سامانه‌های دفاع موشکی اسرائیل باشد.
▪️
افزون بر این، نتانیاهو پیشنهاد ایجاد یک صندوق مشترک ۱۶ میلیارد دلاری برای تحقیق و توسعه سامانه‌های تسلیحاتی جدید را مطرح کرده است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77623" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=Gl91B3YVghA5YAb0r_Pom9-Dy3i1ZMppy9kHVJDApPCXb58vGkMJFqWlzP1_XoW47FdxQb-sK9hRzo5o7CJ8ROJcFFNDXkjCZ8Q5s2dhuBW8xzMEzyZaHlPh20_rEaOMZ8gATlPzO-asz4usLj1MmWKuqdpQNCinDCSD1cuPnl4pIwn95i_tYRMQmfRp4Z5s1PIBliCu0VuK9ct160nYl0ULiOxRZja9hit8hcz-4oUyEhFtW4CyFwzR2HotAeKAbEi_E_PiGRqF39XEzLgFyj0BEIM6dAQhMd-0KMP1u-_qAwTG1Fv38n-_upBAFvfLWSOVrU1ukun4iOneK6F3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=Gl91B3YVghA5YAb0r_Pom9-Dy3i1ZMppy9kHVJDApPCXb58vGkMJFqWlzP1_XoW47FdxQb-sK9hRzo5o7CJ8ROJcFFNDXkjCZ8Q5s2dhuBW8xzMEzyZaHlPh20_rEaOMZ8gATlPzO-asz4usLj1MmWKuqdpQNCinDCSD1cuPnl4pIwn95i_tYRMQmfRp4Z5s1PIBliCu0VuK9ct160nYl0ULiOxRZja9hit8hcz-4oUyEhFtW4CyFwzR2HotAeKAbEi_E_PiGRqF39XEzLgFyj0BEIM6dAQhMd-0KMP1u-_qAwTG1Fv38n-_upBAFvfLWSOVrU1ukun4iOneK6F3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی، جزئیاتی از گفتگو و تبادل نظر خود با پیت هگست، وزیر جنگ ایالات متحده که روز چهارشنبه هفتم مردادماه در واشنگتن انجام شد را به اشتراک گذاشت.
نتانیاهو گفت: «هگست در این گفتگو به من گفت وقتی به وضعیت جهان نگاه می‌کنیم، کشورهایی هستند که اراده مبارزه در کنار ایالات متحده را دارند، اما توانایی لازم را ندارند. در مقابل، کشورهایی هم هستند که از توانایی برخوردارند، اما اراده جنگیدن ندارند.»
نخست‌وزیر اسرائیل در ادامه افزود که وزیر جنگ آمریکا تاکید کرده است: «تنها در اسرائیل است که ما هم‌زمان شاهد وجود اراده و توانایی مبارزه هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77622" target="_blank">📅 20:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/khNyBfIMu-_b8cC1wz74bWqPBozV31s41JkGwtIyrBw8z9rlWPNa6TRmzs31E9BEjcqoqPlNW0R4LcAXF13m02dAiUwfLDVewPv44SWr61ajpAZbfvta7qwDbOnYW7T3eKh_XKZ1MFOiYulHv4Iivy4ebm4qMdA32CVPc-DKJuWC7PqpfvHmUbrq-QS5Y52X0w0pU6QtYwtLDBf35Fb-fekfvujZDa1wF0TSk6Fs98guJnY0Y09x6dRHGYUOvlO9_tg_fszqmyxB8H4qixdewjw7YbLMqy0aIITgsFBDSabsdUSaggqCt2vr5rbXiBCktATTc7nn78LrDhLz6uYiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از وقوع انفجار در پایانه گاز طبیعی مایع بندر دمیاط مصر هنگام تخلیه محموله خبر دادند.
همزمان، شرکت امنیت دریایی امبری و منابع امنیتی اعلام کردند یک پهپاد به یک شناور ذخیره‌سازی گاز متعلق به آمریکا برخورد کرده است؛ حادثه‌ای که به آتش‌سوزی دو کشتی منجر شد، اما تاکنون گزارشی از تلفات جانی منتشر نشده است.
بر اساس گزارش‌ها، این انفجار هنگام تخلیه محموله در پایانه گاز طبیعی مایع بندر دمیاط رخ داد.
شرکت امنیت دریایی امبری اعلام کرد یک پهپاد به یک شناور ذخیره‌سازی شناور گاز که تحت مالکیت آمریکا است، برخورد کرده است. به گفته این شرکت، در پی این برخورد آتش‌سوزی ایجاد شد و سپس به کشتی دیگری نیز سرایت کرد.
شرکت خدمات بندری اینچ‌کیپ نیز در گزارشی جداگانه اعلام کرد دو کشتی حامل گاز در بندر دمیاط دچار آتش‌سوزی شده‌اند.
امبری اعلام کرد خدمه هر دو شناور تخلیه شده‌اند و آتش تحت کنترل درآمده است. این شرکت افزود تاکنون هیچ گروهی مسوولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77621" target="_blank">📅 20:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BczlUJcQuRutcMakQY_1LqDWUOkPC14Ei8sFwO4sdnSGKOI9tEyw11sQ78Ih0X5X3KzYoFPC91BoQ62kTV8XzO91f4KBzt-iBHjKeTxtGyqLW3vpEO9gbbqnplQQN2zoL_pxoGXW6s96M8e4chemZppnVlCth0jw3o8o5xrXsK4eKCOmJ1jaQB_UBT7Qc0x_2fRfCNIf_d2CZskwQBFH_fXC_mCOryWvTZ9vY7gij1Jknz36winuWPoS1mFqxiYYar2AVGOR_y-m8aOD-5rZprhCFElFZlamD76CxcKoE-I91csbU4B30gjRVJejBVOxMElnQWRZLS358CHiHNtaAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: پس از تهدیدهای اخیر و تلاش برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناه در حال عبور از تنگه هرمز، سپاه پاسداران انقلاب اسلامی ایران همچنان ادعا می‌کند که دریانوردان بین‌المللی باید فقط از مسیرهای مورد ترجیح سپاه استفاده کنند.
✅
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه هیچ اختیاری برای تعیین مسیر حرکت آزاد و بدون مانع ندارد. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای سنتکام به عبور حدود ۱٬۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77620" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eghFfgtDslMy0sng2kxaUCDe29zsfS-Ya-X_NPmI8WJ2CHqD8xfHNtZpNKgWoR9XgHMgAkJBlrRFTyubv6iqLTjB_Z4MJf7OhdBcfQbpTTtufQKHgKoW1NmizdW-7TTRMiLCc9BYjeIHTEk6tVVMkc4s0dbCXqlJqsW41tRp8ppfDMB4H5JhvkOg9j3qfrHwKEZIzDlH54-uBFAOP-32oWgGIJbd0nncL7PEz7sGtCADM8dXr_MvW9V4LF4AUDihl6oHh4slsmN1gNTBZOYT_u5IRS5BCKVvEQT4vNcUgjwL7LY69vbEdwHHF-CtZaHMIY1sG9yeOMo6rRv4xHOnJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، نیروی دریایی سپاه پاسداران انقلاب اسلامی روز چهارشنبه هفتم مردادماه، اعلام کرد سه نفتکش را در تنگه هرمز به دلیل بی‌توجهی به هشدارها «هدف قرار داده و توقیف کرده است».
در این گزارش به نام این شناورها، مالکیت، محل دقیق حادثه و جزئیات تخلفات ادعایی آن‌ها در این آبراه اشاره‌ای نشده است، اما تهران مسیر جایگزین جنوبی در امتداد سواحل عمان را رد کرده است.
بر اساس بیانیه‌ای که تسنیم منتشر کرده، سپاه پاسداران تاکید کرده است که «مداخله‌ها و دستورات غیرقانونی» ایالات متحده از سوی شناورهای حاضر در منطقه «بی‌پاسخ نخواهد ماند».
مرکز عملیات تجارت دریایی بریتانیا، هنوز وقوع چنین حملاتی را تایید و گزارش نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77619" target="_blank">📅 18:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZsptOzsIw-iphpgXFWSyGBLkdLfDC8Ul5mMN7JnFA7I0RPf2UbVz7HZUMc3agMJp-D0EIfOvQ9jijKpoi3eToEaaRS97h0GSu7xAe_zpTjFs_Au7O5yXBY_PTo6SJSvsRXhn_LdCZfFWzV__1mS6uCkFV8fqvOLbAl8pE6WkkSoa46r5QFIOD8fuCVtDnaWb7avvlnnSjHx2WshTcjOUNbUW4w-RUSMAL-BiBMIGj5U6Wk5yosEQrIlx0cTkkSrXel23WgxLHE5lXcFb2KOQE74wG0qXHlsi0WDl-Q2N1ykvEO9Rcci0PMojjAu2uUpBdXWfreNIAP6AdzZEi78yIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ دانشگاه ایرانی در رتبه‌بندی تاثیرگذاری تایمز ۲۰۲۶ حضور ندارد
در رتبه‌بندی تاثیرگذاری و پایداری دانشگاه‌های جهان در سال ۲۰۲۶، نام هیچ دانشگاهی از ایران دیده نمی‌شود؛ این در حالی است که در فهرست سال ۲۰۲۵، ۳۴ دانشگاه ایرانی حضور داشتند.
تایمز امسال نحوه مشارکت در این رتبه‌بندی را تغییر داده و آن را به عضویت دانشگاه‌ها در شبکه پایداری و ارائه اطلاعات از سوی خود موسسات مشروط کرده است.
برخی رسانه‌های ایران این تحول را با عنوان «حذف ایران» پوشش داده‌اند؛ تعبیری که اقدامی هدفمند یا تنبیهی را تداعی می‌کند، در حالی که هنوز مشخص نیست نبودن دانشگاه‌های ایرانی ناشی از تصمیم تایمز بوده یا شرکت نکردن آنها در سازوکار تازه رتبه‌بندی.
رتبه‌بندی‌های موسسه تایمز از شناخته‌شده‌ترین و پرمراجعه‌ترین نظام‌های ارزیابی دانشگاه‌ها در جهان است و نتایج آن می‌تواند بر اعتبار بین‌المللی، جذب دانشجو و همکاری‌های علمی دانشگاه‌ها اثر بگذارد.
@
VahidHeadline
برای نخستین‌بار از زمان آغاز انتشار رتبه‌بندی «دانشگاه‌های تأثیر‌گذار» موسسه آموزش عالی تایمز، نام هیچ دانشگاهی از ایران در نسخه سال ۲۰۲۶ این فهرست دیده نمی‌شود. رخدادی که در کنار افت مداوم جایگاه دانشگاه‌های ایران در دیگر نظام‌های معتبر رتبه‌بندی جهانی، بار دیگر وضعیت آموزش عالی کشور را زیر ذره‌بین برده است.
بر اساس نتایج منتشر شده، در رتبه‌بندی سال ۲۰۲۶ تایمز، یک‌هزار و ۶۴۶ دانشگاه از ۱۱۶ کشور بر پایه اهداف توسعه پایدار سازمان ملل متحد (SDGs) ارزیابی شده‌اند. با این حال، برخلاف سال‌های گذشته، نام ایران به‌طور کامل از این فهرست حذف شده و مؤسسه تایمز نیز تاکنون توضیحی درباره علت این موضوع ارائه نکرده است.
حذف نام ایران از این رتبه‌بندی در حالی رخ داده که دانشگاه‌های کشور از زمان آغاز انتشار آن در سال ۲۰۱۹ همواره در فهرست تایمز حضور داشتند. تنها در سال ۲۰۲۵، ۳۴ دانشگاه ایرانی در این رتبه‌بندی ارزیابی شدند و برخی از آن‌ها در چند شاخص توسعه پایدار، از جمله «سلامت و رفاه»، «آموزش باکیفیت»، «صنعت، نوآوری و زیرساخت» و «برابری جنسیتی»، جزو دانشگاه‌های برتر جهان بودند.
همزمان، نتایج تازه‌ترین رتبه‌بندی جهانی QS نیز از ادامه روند نزولی دانشگاه‌های ایران حکایت دارد. رتبه‌بندی QS که از معتبرترین نظام‌های ارزیابی آموزش عالی در جهان به شمار می‌رود، دانشگاه‌ها را بر اساس شاخص‌هایی مانند اعتبار علمی، کیفیت پژوهش، میزان استناد به مقالات، نسبت استاد به دانشجو، همکاری‌های بین‌المللی و اشتغال‌پذیری فارغ‌التحصیلان ارزیابی می‌کند.
در این ارزیابی دانشگاه تهران ۴۵ پله سقوط کرده و از رتبه ۳۲۲ به ۳۶۷ جهان رسیده است. دانشگاه تبریز ۱۰۸ رتبه، دانشگاه فردوسی مشهد حدود ۱۲۵ رتبه و دانشگاه‌های شیراز، اصفهان و آزاد اسلامی نیز افت قابل‌توجهی را تجربه کرده‌اند؛ به‌طوری که دانشگاه آزاد از جمع هزار و ۴۰۰ دانشگاه برتر جهان خارج شده است.
در مقابل، کشورهای منطقه روندی معکوس را طی کرده‌اند. ترکیه با ۲۵ دانشگاه در رتبه‌بندی QS حضور دارد و دانشگاه فنی استانبول به رتبه ۲۷۹ جهان رسیده است. امارات متحده عربی نیز سه دانشگاه در میان ۳۰۰ دانشگاه برتر جهان دارد.
حسین سیمایی‌صراف، وزیر علوم، کاهش سرمایه‌گذاری در پژوهش، ضعف همکاری‌های علمی بین‌المللی، کمبود زیرساخت‌های آموزشی و پژوهشی و محدود شدن فرصت‌های مطالعاتی را از عوامل افت جایگاه دانشگاه‌های ایران دانسته است.
شاهین آخوندزاده، معاون تحقیقات وزارت بهداشت، نیز اعلام کرده بود که محدودیت‌ها و اختلال‌های گسترده اینترنت در سال ۲۰۲۶، پژوهشگران ایرانی را حدود یک‌سوم سال از فعالیت علمی بازداشت؛ موضوعی که به گفته او می‌تواند به کاهش حدود ۱۰ هزار مقاله علمی و افت بیشتر جایگاه علمی ایران منجر شود.
کارشناسان آموزش عالی نیز می‌گویند کاهش ارتباط دانشگاه‌های ایران با مراکز علمی جهان، محدودیت در جذب استاد و دانشجوی خارجی، کاهش بودجه پژوهشی، ضعف زیرساخت‌های آموزشی و دسترسی محدود به منابع علمی بین‌المللی، از مهم‌ترین عوامل کاهش رقابت‌پذیری دانشگاه‌های ایران در رتبه‌بندی‌های جهانی است.
رتبه‌بندی دانشگاه‌های تأثیرگذار تایمز از سال ۲۰۱۹ با هدف ارزیابی عملکرد دانشگاه‌ها در تحقق ۱۷ هدف توسعه پایدار سازمان ملل منتشر می‌شود و تنها نظام رتبه‌بندی جهانی است که نقش دانشگاه‌ها را در حوزه‌هایی مانند آموزش، سلامت، برابری جنسیتی، نوآوری، محیط زیست، عدالت و توسعه پایدار می‌سنجد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77618" target="_blank">📅 17:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUhEd5rDVqaVnYcbFokoJgue15ec7n1FwIEOlqkptBo1D6MXrMAzgEBSMAVoSursFi61HNIxN0WFKLtIOy0aM8v9jKRb1ttkqn_YDPlxZFo68xyUPfw_FsipUGfI0lSb6SAt_hz0f6LspPJdXRxwKe6_La2tRKyEfJTwuV65wliyPgMIvZ_2SuegchyHbNZ4tUcBY6EDKofM0yoAq4N18maHCaKx3ClumTHBKF1LotL0_N_73onAaKzVGSRw7F0YnKw33OWYlG-O_clOyKj8g7Fyauz8H7NvNKhpDP5siuWtv782Z1sUVAzaWKE8Hsg9fvsa2Yp1-1v0F_0axT4Eng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه پس از آنکه ارتش ایالات متحده اعلام کرد چندین موشک بالستیک شلیک‌شده از سوی ایران به سمت نیروهای آمریکایی در خاورمیانه را رهگیری کرده است، وعده داد که ایران را به‌شدت هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز گفت: «حسابی نابودشان خواهیم کرد. خیلی سخت به آنها ضربه خواهیم زد.»
این گفت‌وگوی تلفنی به‌صورت کامل پخش نشد، اما یکی از خبرنگاران فاکس نیوز خلاصه‌ای از اظهارات ترامپ را منتشر کرد.
@
VahidHeadline
گفت: حسابی نابودشان خواهیم کرد. ضربات سختی به آنها خواهیم زد و به‌شدت تنبیه خواهند شد.
ترامپ همچنین درباره حملات هوایی آمریکا و عربستان سعودی به شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق گفت این حملات با هماهنگی دولت عراق انجام شده است.
رییس‌جمهوری آمریکا این شبه‌نظامیان را «سرطانی برای جهان» توصیف کرد و گفت در حال بررسی صدور هشدارهای بیشتر علیه نیروهای نیابتی جمهوری اسلامی و ارتباط آنها با حکومت ایران است.
ترامپ همچنین گفت اکنون موضع بنیامین نتانیاهو درباره جمهوری اسلامی را درک می‌کند.
او در پاسخ به پرسشی درباره احتمال ادامه مذاکرات با جمهوری اسلامی نیز گفت: «اجازه می‌دهیم به گفت‌وگوهایشان ادامه دهند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77617" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=a7K2qEaADzS6RLvE4XZPt65aDwO0kibQERTQN6i9mbXeYFILSSEyuRuVyuaeiHnJMkvpBhEcSN0TMI3SVMURtS67p3_Nj49NF69AYhiXoagV37ah7mv2heIIHXN7LeZJpX1Te_jvnJ9HrV3rYP9nfboebnd3UgfHFEaoj7FAfvCCgJBFkjLxn1ukpLafwOE_4uUBhzZfAO3mvDlNmxJb4cHJ738NrXQA7DPdpnK00-gXxnlmyFZuB2Q-dMfh3GR141E3dnJRLm2d7ToEKQVCG3IzCj7OmlfjWOqzjmCCDt_vRuMymFkQWvft7rtZy47o7HdrVfLb730GcdrYPvyfew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=a7K2qEaADzS6RLvE4XZPt65aDwO0kibQERTQN6i9mbXeYFILSSEyuRuVyuaeiHnJMkvpBhEcSN0TMI3SVMURtS67p3_Nj49NF69AYhiXoagV37ah7mv2heIIHXN7LeZJpX1Te_jvnJ9HrV3rYP9nfboebnd3UgfHFEaoj7FAfvCCgJBFkjLxn1ukpLafwOE_4uUBhzZfAO3mvDlNmxJb4cHJ738NrXQA7DPdpnK00-gXxnlmyFZuB2Q-dMfh3GR141E3dnJRLm2d7ToEKQVCG3IzCj7OmlfjWOqzjmCCDt_vRuMymFkQWvft7rtZy47o7HdrVfLb730GcdrYPvyfew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب گذشته نیروهای آمریکایی و عربستان سعودی در عملیاتی مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در شرق عراق را هدف قرار داده‌اند.
@
VahidHeadline
بر اساس گزارش‌ها، پایگاه‌های حشد شعبی در استان‌های دیاله، کرکوک، کربلا و نینوا هدف حمله قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77615" target="_blank">📅 16:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNsy2HUiJdMz89yEVVbtqPVTD9hO2urZ0tYgxZcJwR-DJWuayaxgN6iCwo3PrEzAoPSG3ACtVKwOFtg7bgI2mQuE4TiYsZ-7uyR4s84M-i5-lzcuez1f12E1JwZfaL5DxaKYiu_nh_i5iAqMYGiG__gdMmzYp8F8n5725ciW-MOw7oL7at69rLLu6daJPd6Wn_24r6ccIQzGil2vLvtZm65YAMt3uH_Vbi-UeBgWcXdaTf_QnbAXP02hHe9Z0y0B9SUg9gCBjCHWkK7oNsMZSUhntJBF_FcO260DenqRzzlWHWYOaB9k3IyQ9E79icUH45EklkgEWDIuOMsCmpdK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرحی را به مرحله بعد فرستاد که در کنار تشدید فشار اقتصادی بر روسیه، تحریم‌های مرتبط با ایران را تا سال ۲۰۳۱ تمدید می‌کند.
این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، هنوز باید در رأی‌گیری نهایی سنا تصویب و سپس در مجلس نمایندگان بررسی شود.
@
VahidHeadline
و  در خبری دیگر:
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) اعلام کرد ۱۰ شرکت و هشت نفتکش را به فهرست تحریم‌های خود افزود.
این تحریم‌ها بر اساس فرمان اجرایی ۱۳۹۰۲ و در ارتباط با جمهوری اسلامی اعمال شده‌اند.
در میان نهادهای تحریم‌شده، «اداره خدمات دریایی هرمزسیف» و «شرکت بیمه دریایی خلیج فارس» در ایران نیز قرار دارند.
وزارت خزانه‌داری آمریکا همچنین اعلام کرد این دو نهاد مشمول تحریم‌های ثانویه هستند.
شرکت‌های تحریم‌شده در هنگ‌کنگ، جزایر مارشال و چین ثبت شده‌اند و نفتکش‌های تحریم‌شده نیز با پرچم کشورهای مختلف فعالیت می‌کنند. این نفتکش‌ها به شرکت‌های تازه تحریم‌شده مرتبط معرفی شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77614" target="_blank">📅 16:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPEcruT0zrpV9poid8j9cVG3V-ntb9B56Z_3u1EDhBwzy_bjLpTw7HSEv3YJ4_RQMH_Pj5D24e0qLUdPEgZVJMJ_BBF66flFoOm9j1h8ZAwwQevDYf3VEvo02Sg4p3pfenYUzH5PaYUIhsk4oGEULlB9WvlaygSeOwpM8-CjFYZkLdEWST4fiuSdimbPh6TYcnyGNJkpdaEup77TrZ546p2orHUdqMNkglet4fG9sj7YxZQhfclwtEzT3lffDYtU8Lf6x-oDZ_53qc-6hKRgB64jfvuMjWhpswdko2x8wo0gDv91Y-u4MqcnNQqOQvJfmh-Bege3JCEJfqfkgo0vVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع منطقه‌ای گزارش داد که حوثی‌های یمن در حال بررسی طرحی برای دریافت عوارض از کشتی‌های تجاری عبوری از تنگه باب‌المندب هستند؛ اقدامی که به گفته این منابع، پس از اعلام محاصره دریایی عربستان سعودی مطرح شده و می‌تواند فشار بر آمریکا را افزایش دهد.
به گفته این منابع، حوثی‌ها در حال بررسی دریافت عوارض از بیشتر کشتی‌هایی هستند که از باب‌المندب، گذرگاه راهبردی میان دریای سرخ و خلیج عدن، عبور می‌کنند، اما هنوز زمان مشخصی برای اجرای این طرح تعیین نشده است. دفتر رسانه‌ای حوثی‌ها به درخواست رویترز برای اظهار نظر پاسخ نداد.
دو مقام منطقه‌ای که از سوی جمهوری اسلامی در جریان این موضوع قرار گرفته‌اند، به رویترز گفتند مقام‌های حوثی در سفر خرداد به ایران برای شرکت در مراسم تشییع جنازه علی خامنه‌ای، درباره دریافت عوارض از کشتی‌های عبوری از باب‌المندب با مقام‌های جمهوری اسلامی گفت‌وگو کرده‌اند. به گفته منابع، هدف از این طرح عادی‌سازی دریافت عوارض از آبراه‌های بین‌المللی و افزایش فشار بر آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77613" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXijMOTdTcE4q1TPavpdRiBBcglTIMxZT2gUUxqd09tU-tppCzHtFXOYe_GOF1Kpt2ass3BToIVxV6xIXxwPqO13rKVDEBpD1vp1jAfR09ZS8Eaz0A6FzF_gVAD9tuZFmQSDdQwIL-P6KZY0dH2CL2Ehth6W33WYyJhB5jCoDQPwHU_cNVHtpl8n9zn02L2UVwKIPmMM8o4BF64r5Mf7Vlvp28ZNBcV_PrkSydgbRYBHB0dVpNVCguARH2RwTAn38GI5XyqEFfViajP8RwQHk-paXtYpd7KzdLbsZEcgi-nyzj_ipMI8oGiMO5jgUuuLcTf96ENltLC8et5IUOQmGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون دولتی جمهوری اسلامی گزارش داد منطقه‌ای در نوار مرزی پیرانشهر در استان آذربایجان غربی هدف حمله هوایی آمریکا قرار گرفته است. در این گزارش آمده است: «منطقه‌ای در نوار مرزی پیرانشهر مورد حمله هوایی دشمن آمریکایی قرار گرفت.»
پیش از آن، خبرگزاری فارس به نقل از یک مقام استان آذربایجان غربی گزارش داده بود موشکی به منطقه‌ای غیرمسکونی اصابت کرده و تلفاتی بر جای نگذاشته است.
فرماندهی مرکزی آمریکا تاکنون این حمله را تأیید نکرده و درباره آن اظهار نظری نکرده است. تأیید مستقلی نیز برای این گزارش وجود ندارد.
پیرانشهر در غرب استان آذربایجان غربی و در نزدیکی مرز عراق قرار دارد. این شهر پنج روز پیش نیز بر پایه گزارش سازمان مدیریت بحران استان به خبرگزاری ایرنا، هدف حمله هوایی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/77612" target="_blank">📅 16:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bN9SLQsQGgIMmOWfa_9qUAoJ10snAWmVuLHBQk2h6dB2XkqcaUgh2OB9E4_lYylbcslTs7bOnKg-EAL2cOtIAPoKXMvPJQOf_WBlB_6oSGSL9mbNoikvkEoiVMEx5BwZT8UvJEwz8lqcVZKtQVCXaQBoMqqwRHwTEzqdM1KSbNlBOAiGdD_GA1JgRc5FU8IvbG1yeJvjrtIhMrPvR1e7EFVRpq2Haxj9YDGuexVjnTzSJIhBdtPMSl2jzVJq4_3oSC5OpddafuNgiQNVqKc2s4eVilfxS21_pDG4zhGRTmBKmIsVXs_0RA6B-cCEjdxDJoUkdLGrQCsIcSpvHlg6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر، رهبر جریان صدر عراق و از رهبران شیعیان عراق، با انتشار بیانیه‌ای از سپاه پاسداران خواست خاک عراق را هدف حملات خود قرار ندهد و هم‌زمان از گروه‌های مسلح عراقی نیز خواست با اقدامات خود به کشورهای منطقه بهانه حمله ندهند.
صدر در این بیانیه که روز چهارشنبه هفتم مرداد منتشر شد، نوشت عراق نباید به محلی برای هدف قرار دادن جمهوری اسلامی تبدیل شود و از «برادران در سپاه پاسداران» خواست از حمله به «سرزمین مقدس و مستقل عراق» خودداری کنند.
او همچنین از آنچه «میلیشیاهای خودسر» خواند، خواست با اقدامات خود زمینه حمله کشورهای عربی خلیج فارس به عراق را فراهم نکنند.
رهبر جریان صدر با محکوم کردن هدف قرار گرفتن خاک عراق از سوی هر کشور یا هر طرفی، از دولت بغداد خواست حاکمیت خود را اعمال کند، امنیت را برقرار سازد و مانع کشیده شدن این کشور به جنگ و درگیری‌های فرقه‌ای شود. او تاکید کرد عراق و مردمش بیش از هر چیز به صلح نیاز دارند و سال‌ها جنگ، توان و ظرفیت‌های این کشور را فرسوده است.
این بیانیه در شرایطی منتشر شده که از آغاز جنگ ۴۰ روزه، سپاه پاسداران بارها مواضع احزاب کُرد در اقلیم کُردستان عراق را هدف قرار داده است. هم‌زمان، فرماندهی مرکزی ارتش آمریکا (سنتکام) بامداد چهارشنبه هفتم مرداد اعلام کرد نیروهای آمریکایی و عربستان سعودی در یک عملیات مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در عراق را هدف قرار داده‌اند.
@
VahidHeadline
مقتدی صدر در بیانیه‌اش به جای خلیج فارس از عبارت دیگری استفاده کرده:
Mu_AlSadr
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77611" target="_blank">📅 16:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx3wq-l4l5GWXlx0mD3G3PJ0iFU5SGzx-Ne6lW5AlSFw5DxyUJKS1mtcgBRPKlvCnKZ8Eha2uFzp8-Lh8JYJ3x3TdSpNHUyg-MoqAPfNrKPetQlP0AffKw4Z3W1CTInEcw9yLiRj0bLYNG-KAJdCMOz28GeqDTIAvCigANACico5pmSPX9MGzfVz79mWQMFN6pFddHuB5o1ej5mnrs7b77FZESAziATFVbgxxLLWbhycD2aeCm37-9IF5O1kIvy_ifrBee6c9J_RHwgrgx9L4zRNabw8Tk5M41fMltdi71YRvp7A0uYb45-CAI076a6GZi4HgtWHMphcL0pnfF8NHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ نیویورک‌تایمز، به نقل از چند مقام ایرانی و غربی که نام‌شان اعلام نشده، گزارش داد که حکومت ایران قصد داشت در واکنش به حملهٔ اوکراین به یک کشتی ایرانی، به یک بندر در اوکراین حمله کند، اما به‌دنبال اقدامات دیپلماتیک از انجام این اقدام خودداری کرد.
این روزنامه به نقل از این مقام‌ها نوشته است که انتظار می‌رفت ایران در این حمله یک موشک بالستیک با کلاهک کوچک به سمت اوکراین شلیک کند تا خسارت نسبتاً کمی به بار آورد و به‌صورت نمادین پاسخی به حملهٔ اوکراین داده باشد. این مقام‌ها گفتند که هدف حمله احتمالاً یکی از بنادر اوکراین در دریای سیاه بود.
بر اساس این گزارش بامداد چهارشنبه هفتم مرداد منتشر شد، مقام‌های جمهوری اسلامی امیدوار بودند این درگیری با حملهٔ تلافی‌جویانهٔ آن‌ها پایان یابد، اما مقام‌های غربی هشدار دادند که پیش‌بینی چگونگی واکنش اوکراین دشوار است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77610" target="_blank">📅 16:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vyozgVcr_pgTgq6mSjt1a4Fit4yyXyHDsn9l5EDadwOcbDR4KP51zNBpgt2le7CTUXsklLq_o4Le8S6Ir8gJiDK5Z_2OJTIJwtEZ9lc-xzCrAmZ5NoOSNxQK8V_ICcpjPwKEFzQJ5aqUe2OPfKsQAOsBVURMAJJEg3fkTRJnrwEh3QVgOAjqvG1GLj6GUZW3bLz3HvLioMIL5syV8WsPtFK4IgHtFib4BQ4i45g8yabfNFNfIXP7Yh_P8rMAdeMH_8SRQPvFYhwZ-QnFCdt_Fb8HmltwMBrG5Ckwvo71XitlNsiADdxWEZkMm2TeQkWawAhK4pWvROtds_YpSGFdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SynhNNKdJAtQqoAAi049UE9Ta-IbJ3sFM-BTFiUlFxyj3e7HQ_Qu480m6-poZ24C9z6XCVC0EGPtM0tqlHK3zGuPh_3R6zI8HRbj6poWGqHFguwDJskvrQw7mETD-SYg9oshFTSXX9toOwqiPCyObXSuiXfrDa-tYBQa6w0frjU-VHslrEQxsiQ0YiR56RQXyXIdXdhKAxnk18NMA1f8YL90cWSK7vycdm484hge5UGhhJa9q3ct-GFqI3D-8KTydeEC6Zq_0Cfxak0TebfGJahI9BcVY_53_HOvEbTm71djiB_rLM9VLm8J4HVWKi5GO87vSoujvXtlSz5ND8k32A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برخی رسانه‌های ایران و کانال‌های مرتبط با سپاه پاسداران گزارش دادند که چهار عضو سپاه پاسداران در حملات منتسب به آمریکا و عربستان سعودی به عراق کشته شدند.
به نوشته این رسانه‌ها، این افراد در حمله‌ای به کربلا جان باختند.
بر اساس این گزارش‌ها، علی اصغر آستانه، ابوالفضل متقی، مرتضی اکبری و امیرعباس درهم‌فروش از جمله کشته‌شدگان هستند.
@
VahidOOnLine
شبه‌نظامیان حشد‌ الشعبی صبح چهارشنبه هفتم مرداد اعلام کردند شمار کشته‌های حملات هوایی مشترک آمریکا و عربستان سعودی به پایگاه‌های این نیروهای تحت حمایت ایران به ۲۰ نفر رسیده است.
حشد الشعبی در بیانیه‌اش این میزان تلفات را آمار «اولیه» خوانده و گفته است که دست کم ۳۲ نفر نیز در این حملات مجروح شده‌اند.
حملات مشترک آمریکا و عربستان علیه مواضع نیروهای حشد الشعبی در بغداد، واسط، نینوا، بصره، کرکوک، کربلا و دیاله انجام شد و خسارات مادی به تأسیسات و تجهیزات نظامی نیروهای حشد الشعبی وارد کرد.
فرماندهی مرکزی ارتش آمریکا در بیانیه‌اش گفته بود که این شبه‌نظامیان طی روزهای اخیر بیش از ۲۴ حمله پهپادی انجام داده‌اند.
به‌گفتهٔ سنتکام، هدف این حملات «تروریست‌های همسو با ایران» بوده است که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان سعودی هدایت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77608" target="_blank">📅 16:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=rujSlI2uJO1_01jE2KNh338x-YRWvoEm78GADWAeoWfrmP0Q_fhp5QsgfFSBXzyPKUuHBxnc4zEsa4NqcUiAYzKr_IcMwBoa1J_TXvQf4zzM7YzilS5dNIBzoafg6HYBVA3yAvGXGBXKZkECRbZwek0LSFLzD97Bdzt31BhN6ll_QaxVNB3TjSRGzeZWKfntkAWswHqCYgrXF021ezHcKht627rWLEVRJt22InCkpGkopy38TRozGJujRRfxXjTlCWYgWZCJYrOvJyzgJYNL0fqoO_J8V57VFHC-2q_Ai8u33MnatZpNiViVLF1Fpi460VtZKF7uTtfCWABeRQyC3Hyvc_7hK_t4MvIge5j7PePrHKpzh4oYyMcx9hiDR4W_U_UXwq0JXpxBvR7CgQm2Ml9iygL9y1XxXduVKgJ3vAtDwNQ66oGrciw4ruSEyzgeoeq9rfDYUludL1_6eurpehkd7TtJQLxEGkFXabQAivGE06zF7KpbFLB4QHlLMJdFBuvEWhbkDsG0fqODt1PNHQjzzzafegG7as3ZY7msZN7lfKQRWHwSj-iY-3BHKkFDr4R9-qRc1ogFUrQqaxgSri1yTLVr0i4Prx8q0DjvtlMN5oq8aBiU5AqsmzH6mZapd4EA00iNPCmC70B5ZUIBP4Ml-zEqNtJFaXXUp_neXx8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=rujSlI2uJO1_01jE2KNh338x-YRWvoEm78GADWAeoWfrmP0Q_fhp5QsgfFSBXzyPKUuHBxnc4zEsa4NqcUiAYzKr_IcMwBoa1J_TXvQf4zzM7YzilS5dNIBzoafg6HYBVA3yAvGXGBXKZkECRbZwek0LSFLzD97Bdzt31BhN6ll_QaxVNB3TjSRGzeZWKfntkAWswHqCYgrXF021ezHcKht627rWLEVRJt22InCkpGkopy38TRozGJujRRfxXjTlCWYgWZCJYrOvJyzgJYNL0fqoO_J8V57VFHC-2q_Ai8u33MnatZpNiViVLF1Fpi460VtZKF7uTtfCWABeRQyC3Hyvc_7hK_t4MvIge5j7PePrHKpzh4oYyMcx9hiDR4W_U_UXwq0JXpxBvR7CgQm2Ml9iygL9y1XxXduVKgJ3vAtDwNQ66oGrciw4ruSEyzgeoeq9rfDYUludL1_6eurpehkd7TtJQLxEGkFXabQAivGE06zF7KpbFLB4QHlLMJdFBuvEWhbkDsG0fqODt1PNHQjzzzafegG7as3ZY7msZN7lfKQRWHwSj-iY-3BHKkFDr4R9-qRc1ogFUrQqaxgSri1yTLVr0i4Prx8q0DjvtlMN5oq8aBiU5AqsmzH6mZapd4EA00iNPCmC70B5ZUIBP4Ml-zEqNtJFaXXUp_neXx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند از ابتدای سال ۲۰۲۶ تاکنون، اعدام دست‌کم ۸۸۶ نفر در ایران را مستند کرده است که ۵۶ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
زندان قزل‌حصار یکی از بالاترین آمار اجرای احکام اعدام را در سراسر کشور دارد. همچنین بخش قابل‌توجهی از اعدام‌های صورت‌گرفته در ایران مربوط به جرایم مرتبط با مواد مخدر است؛ به‌طوری که طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مرتبط با مواد مخدر بوده است.
🔸
از ۲۲ تیرماه، در پی انتقال شش زندانی محکوم به اعدام در پرونده‌های مواد مخدر به سلول‌های انفرادی زندان قزل‌حصار، جمعی از زندانیان واحد دو این زندان دست به اعتصاب غذا زده و برخی نیز لب‌های خود را دوخته‌اند.
🔸
با گذشت بیش از دو هفته از آغاز این اعتصاب، مسئولان نه تنها هیچ پاسخی به خواسته‌های اعتصابیون نداده‌اند، بلکه با اقداماتی همچون جابه‌جایی زندانیان و ایجاد محدودیت‌های شدیدتر برای جلوگیری از ارسال پیام و ویدیو از داخل زندان، در تلاش‌اند صدای آنان را خفه کنند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77607" target="_blank">📅 16:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77606">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رویترز: منابع می‌گویند ایران ظرف چند هفته سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد
▪️
منابع می‌گویند قرارداد شامل ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی دوش‌پرتاب QW-12 و FN-16 است
▪️
منابع می‌گویند ارزش این معامله ۶۰ تا ۷۰ میلیون دلار است
▪️
چین این گزارش را بی‌اساس خوانده و پاکستان دخالت در انتقال‌ها را رد کرده است
ترجمه ماشین:
۲۹ ژوئیه (رویترز) — سه منبع آگاه از این معامله به رویترز گفتند ایران قرار است ظرف چند هفته نخستین محموله از مجموع حداکثر ۴۰۰ پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که هم‌زمان با بازسازی توان دفاعی این کشور در میانه جنگ با ایالات متحده صورت می‌گیرد.
این خرید که ارزش آن ۶۰ تا ۷۰ میلیون دلار برآورد شده، یکی از بزرگ‌ترین تلاش‌های شناخته‌شده تهران برای تقویت پدافند هوایی کوتاه‌برد خود از زمان آغاز جنگ با آمریکا و اسرائیل است؛ جنگی که ضعف‌هایی را در توانایی ایران برای حفاظت از مراکز نظامی و زیرساخت‌های راهبردی آشکار کرد.
با خبرنامه Trading Day، تحولات بازارهای جهانی را بهتر درک کنید. از اینجا ثبت‌نام کنید.
به گفته منابع، این قرارداد خرید بین ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، شامل موشک‌های چینی QW-12 و FN-16 را در بر می‌گیرد.
این قرارداد با شرکت Zhongqing Baoshang International Investment، مستقر در هنگ‌کنگ، امضا شده است؛ شرکتی که به گفته منابع، به‌عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
ایران پس از ماه‌ها جنگ نیاز به تجدید تسلیحات دارد
منابع به‌دلیل حساسیت موضوع، به شرط ناشناس ماندن صحبت کردند. وزارت امور خارجه ایران بلافاصله به درخواست اظهارنظر پاسخ نداد.
وزارت امور خارجه چین اعلام کرد: «گزارش‌های مربوطه کاملاً بی‌اساس هستند. چین همواره در جهت ترویج صلح و پایان دادن به درگیری نقش ایفا کرده است.»
گروه Zhong Qing Bao Shang مستقر در پکن، شرکت مادر Zhongqing Baoshang International Investment، تا روز سه‌شنبه به درخواست اظهارنظر ایمیلی پاسخی نداده بود.
ایران پس از ماه‌ها درگیری، که طی آن آمریکا و اسرائیل تأسیسات مرتبط با برنامه‌های موشکی، پهپادی و پدافند هوایی این کشور را هدف قرار داده‌اند و تهران نیز با شلیک انبوه موشک‌های بالستیک و پهپادها پاسخ داده، نیازمند تجدید تسلیحات است.
این درگیری دشواری دفاع از مراکز ثابت نظامی و راهبردی در برابر هواپیماهای پیشرفته و تسلیحات هدایت‌شونده دقیق را برجسته کرده است.
واشنگتن روز شنبه به‌طور ناگهانی بمباران‌های دو هفته‌ای خود را متوقف کرد، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت اگر مذاکرات برای پایان دادن به این درگیری پنج‌ماهه شکست بخورد، حملات از سر گرفته خواهد شد؛ درگیری‌ای که در ظاهر از ماه آوریل در وضعیت آتش‌بس قرار داشته است.
تحویل صدها سامانه پدافند هوایی دوش‌پرتاب، موجودی تسلیحات پدافند هوایی کوتاه‌برد ایران را به‌طور قابل‌توجهی افزایش خواهد داد و نشان می‌دهد روابط نظامی این کشور با چین در حال عمیق‌تر شدن است.
منابع هشدار دادند که هرچند توافق امضا شده است، برنامه زمانی تحویل، تعداد سامانه‌ها و دیگر جزئیات اجرایی همچنان ممکن است تغییر کند.
بر اساس طرحی که طرفین بر سر آن توافق کرده‌اند، تحویل‌ها در مرحله نخست از طریق هوایی و از ارومچی در غرب چین انجام خواهد شد و سپس با عبور از پاکستان به ایران خواهد رسید. منابع مشخص نکردند که انتقال از پاکستان به ایران هوایی خواهد بود یا زمینی.
روابط عمومی ارتش پاکستان، ISPR، اعلام کرد: «گمانه‌زنی‌ها درباره دخالت پاکستان در انتقال تسلیحات پدافند هوایی از چین به ایران کاملاً ساختگی و نادرست است.» سخنگوی وزارت امور خارجه پاکستان به درخواست‌ها برای اظهارنظر پاسخ نداد.
منابع می‌گویند چین و ایران مسیرهای زمینی برای تحویل را بررسی می‌کنند
کارشناسان نظامی می‌گویند با آنکه ایران طی دو دهه گذشته سرمایه‌گذاری گسترده‌ای در زمینه موشک‌ها، پهپادها و رادارها انجام داده است، سامانه‌های پدافند هوایی قابل‌حمل اهمیت دارند، زیرا می‌توان آن‌ها را به‌سرعت پراکنده کرد، با تیم‌های کوچک به کار گرفت و مرتباً جابه‌جا کرد؛ ویژگی‌هایی که آن‌ها را در مقایسه با آتشبارهای ثابت پدافند هوایی کمتر آسیب‌پذیر می‌کند.
یک منبع امنیتی اروپایی گفت مقام‌های کشورش از چند قرارداد در حال مذاکره درباره فروش احتمالی سامانه‌های پدافند هوایی دوش‌پرتاب سری QW به ایران، از جمله سامانه‌های QW-12، QW-18 و QW-19، اطلاع دارند.
یک منبع امنیتی دوم در خاورمیانه گفت ایران به‌دنبال خرید موشک‌های QW-12 و QW-18 بوده است، اما او از نهایی شدن قرارداد اطلاعی نداشته است.
‏QW-12 و FN-16 سامانه‌های موشکی زمین‌به‌هوای دوش‌پرتاب و هدایت‌شونده با فروسرخ هستند که برای درگیری با هواپیماهای در ارتفاع پایین، بالگردها و پهپادها طراحی شده‌اند. قابلیت تحرک آن‌ها امکان استقرار سریع در اطراف تأسیسات نظامی، زیرساخت‌های انرژی و دیگر مراکز حساس را فراهم می‌کند.
تحلیلگران دفاعی QW-12 را ضعیف‌تر از مدل‌های جدیدتر خانواده QW، از جمله QW-18 و QW-19، می‌دانند، اما می‌گویند این سامانه‌ها همچنان می‌توانند لایه‌ای مؤثر از حفاظت کوتاه‌برد در برابر پهپادها و اهدافی که در ارتفاع پایین پرواز می‌کنند فراهم کنند.
دو منبع اطلاعاتی غربی و یک مقام ایرانی گفتند تهران همچنین استفاده از مسیرهای زمینی را برای انتقال محرمانه‌تر تجهیزات نظامی و قطعات دومنظوره چینی و کاهش خطر ایجاد اختلال در انتقال بررسی کرده است.
این خرید نشان‌دهنده تداوم اتکای جمهوری اسلامی به ترکیبی از تولید داخلی تسلیحات و تأمین‌کنندگان خارجی، با وجود سال‌ها تحریم و محدودیت بر واردات مرتبط با امور دفاعی، است.
رویترز پیش‌تر به نقل از افراد آگاه از مذاکرات گزارش داده بود که ایران به امضای توافق جداگانه‌ای با چین برای خرید موشک‌های کروز ضدکشتی نزدیک شده است. رویترز نتوانست مشخص کند که آیا آن توافق نهایی شده است یا نه.
reuters
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77606" target="_blank">📅 08:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uk39suW7fzCsPyzmdkneEnhSEEBq4S40AcMhVG5tWP4O4QLFFJlMgAvaTqrgRCTc8T_BtF-34kwtS4FRhYK1AYaL1bmlPh9gC-3sndmH9eaix0XxWRPF9Kn-Rrqp1PeaLCMNKScPOD1mECJe-zr2rM2oqzFSH9b_eS6WQB89RJjq0jzvO0ndbZRVWHqe_NWxjW0YDqgOhWUVm28yFf210ByRb8vbS5k5jdSxauPwb-lH-xn4iSQjXMVQhKBNORwfUAexE1aw9UEE0mq7Abmodq_qstsImkjorbUL5TeXTQNZotgCXIRXF7rE1i02i3DaMQZbZqv8DpxqORVBA_bMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی ایران هویت خلبان کشته شده مجید کاظمی رو پس از چند ماه اعلام کرد.
نوشتند یکی از ۴ خلبان دو جنگنده سوخو ۲۴ بوده که در حمله به نیروهای آمریکایی در پایگاه العدید قطر هواپیماشون مورد هدف قرار گرفت.
نوشتند تلاش‌ها برای تعیین وضعیت ۳ نفر دیگر همچنان در جریان است و مجید کاظمی هم با آزمایش‌های تخصصی و بررسی DNA هویتش تایید شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77605" target="_blank">📅 07:03 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
