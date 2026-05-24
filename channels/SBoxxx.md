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
<img src="https://cdn4.telesco.pe/file/eYsgqY3VKoMdgTsWxQyZJ2t5TasL-7LQihQSCytnAMfh5TwQS2PMGPpJB0o7GqyxhAehrpKvyaXtQYvzoV1aMAukW5XJFLbmKylKMV3TWxrgo-iQqpFjE22hxvDVnjipe35WnOYQEV6LWd2EJ70uCxsaqwgeOq924cpW4DpuzOeZ0VCL11GUTJGz8WPfqAZsIW9KsF-qgAdLjdngp-mbTLIpTi3QE9zAb--ZB2P5uYrO8GFOv_q7jvgfQAPzly9zVnfOfGq2WXgsRDXt13QS1MX43ibe4XXPl91c8kKI7uoZHrIhGB2oubMgMmlbmbpGENQQ3dsSyN44KrWFZlLvyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.87K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 13:46:11</div>
<hr>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SBoxxx/16587" target="_blank">📅 11:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SBoxxx/16586" target="_blank">📅 10:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش موسسه مطالعات جنگ از روند مذاکرات
توجه کنید که این گزارش پیش از توییت شب گذشته ترامپ منتشر شده است
آخرین پیشنهاد متقابل ایران
تمام خواسته‌های کلیدی ایران از جمله برداشتن «تهدید آمریکا علیه ایران»، تسکین مالی، و «حق» ایران برای مدیریت تنگه هرمز را در اولویت قرار می‌دهد، در حالی که تلاش می‌کند مذاکره درباره برنامه هسته‌ای ایران را به تأخیر بیندازد. پیشنهاد ایران ارزیابی مرکز مطالعاتی (CTP-ISW) را تأیید می‌کند که حکومت ایران معتقد است در حال برنده شدن در جنگ است و از موضع قدرت مذاکره می‌کند.
آژانس خبری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی (IRGC)، در ۲۳ مه ۲۰۲۶ گزارش داد که پیشنهاد ایران به میانجی‌های پاکستانی ارسال شده است. ایران خواستار پایان جنگ در تمام جبهه‌ها، از جمله در لبنان، و خروج نیروهای آمریکایی از «منطقه جنگ» شده است. برداشتن «تهدیدهای آمریکا علیه ایران» به معنای خروج آمریکا از منطقه خواهد بود که هم اهرم نظامی آمریکا را حذف می‌کند و هم یکی از اهداف کلیدی ایران، یعنی اخراج نیروهای آمریکایی از منطقه، را محقق می‌سازد.
در این پیشنهاد، ایران درخواست کرده است که تا زمانی که جنگ پایان نیابد، برنامه هسته‌ای خود را مورد بحث قرار ندهد، از انتقال ذخایر اورانیوم غنی‌سازی‌شده (HEU) خود به ایالات متحده خودداری می‌کند و تعهدی برای برچیدن تأسیسات هسته‌ای خود نخواهد داد؛ همه این موارد از خواسته‌های کلیدی آمریکا هستند. آمریکا در فاز اول هر توافقی، اهرم قابل‌توجهی را از دست خواهد داد، قبل از اینکه حتی درباره موضوع هسته‌ای مذاکره کند. این پیشنهاد همچنین شامل خواسته‌های ایران مبنی بر لغو تمام تحریم‌ها علیه ایران و آزادسازی تمام دارایی‌های مسدود شده ایران در فاز اول است.
ایران در این پیشنهاد تأکید کرده است که تنگه هرمز تحت نوعی کنترل ایرانی باقی خواهد ماند و اگر آمریکا محاصره بنادر و کشتی‌های ایرانی را پایان ندهد، مذاکرات را ادامه نخواهد داد. شرایط ماکسیمالیست در این پیشنهاد نشان می‌دهد که حکومت ایران معتقد است از موضع قدرت مذاکره می‌کند، زیرا خود را پیروز جنگ می‌داند.
مقامات ایرانی
همچنان بر مدیریت ایران بر تنگه هرمز به عنوان یکی از نقاط چالش‌برانگیز در مذاکرات تأکید می‌کنند. سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی، در ۲۳ مه اعلام کرد که تنگه هرمز «به آمریکا ارتباطی ندارد» و ایران و عمان باید به عنوان کشورهای ساحلی مکانیسمی برای این آبراه تعریف کنند. روزنامه نیویورک تایمز در ۲۱ مه گزارش داد که ایران و عمان درباره سیستمی برای دریافت هزینه از کشتی‌ها به عنوان «خدمات دریایی» به جای عوارض عبور بحث کرده‌اند. این اقدام بر اساس قانون بین‌المللی دریاها غیرقانونی است.
آژانس خبری تسنیم، وابسته به سپاه پاسداران، در ۲۳ مه گزارش داد که ایران خواستار شده است که تنگه هرمز به مکانیسم و «رژیم حقوقی» پیش از جنگ بازنگردد. تسنیم اضافه کرد که ایران خواستار پایان محاصره دریایی آمریکا شده و اعلام کرده است که مذاکرات تا زمانی که این محاصره برقرار باشد، پیش نخواهد رفت. آژانس خبری فارس، وابسته به سپاه پاسداران، نیز گزارش داد که ایران تنها متعهد به بازگرداندن تعداد کشتی‌هایی خواهد شد که از تنگه عبور می‌کنند به سطح پیش از جنگ است، در حالی که ایران تعیین خواهد کرد کدام کشتی‌ها مجوز دریافت می‌کنند و باید از کدام مسیر عبور کنند.
ناوگان سپاه پاسداران در ۲۳ مه اعلام کرد که ۲۵ کشتی در ۲۴ ساعت گذشته با دریافت مجوز و تحت هماهنگی و تأمین امنیت ناوگان سپاه از تنگه عبور کرده‌اند، که نشان می‌دهد ایران سعی دارد خود را به عنوان مدیر و تأمین‌کننده امنیت عبور از تنگه معرفی کند.
دونالد ترامپ، رئیس‌جمهور آمریکا
، در ۲۳ مه اعلام کرد که تا ۲۴ مه تصمیم خواهد گرفت آیا حمله به ایران را از سر بگیرد یا خیر. یک مقام آمریکایی آشنا با مذاکرات به آکسیوس گفت که مذاکره‌کنندگان هر روز پیش‌نویس‌ها را رد و بدل می‌کنند، اما پیشرفتی حاصل نشده است. ترامپ گفت که شانس رسیدن به توافق با ایران یا از سرگیری حملات «پنجاه-پنجاه» است. ترامپ در ۲۳ مه با رهبران منطقه‌ای برای بحث درباره آخرین پیشنهاد ایران گفتگو کرد. یک منبع نزدیک به مذاکرات به واشینگتن تایمز گفت که انتظار می‌رود آمریکا و ایران تا بعدازظهر ۲۴ مه اعلام نهایی پیش‌نویس توافق برای پایان جنگ در تمام جبهه‌ها را اعلام کنند. ترامپ گفت که او تنها توافقی را خواهد پذیرفت که به مسائل کلیدی از جمله غنی‌سازی اورانیوم ایران و ذخایر اورانیوم غنی‌سازی‌شده آن بپردازد.</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/16585" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در ۳ روز گذشته:  — افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی   — تیراندازی و ترور در اطراف کاخ سفید  — دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/16584" target="_blank">📅 09:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در ۳ روز گذشته:
— افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی
— تیراندازی و ترور در اطراف کاخ سفید
— دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/16583" target="_blank">📅 09:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حمله انتحاری در ‌کویته پاکستان  ۸ نفر کشته و ۳۰ تن دیگر زخمی شدند  انفجار قوی در نزدیکی یک مرکز امنیتی که مشرف به ایستگاه قطار است، شهر کویته را لرزاند.  منابع بیمارستانی گفتند که ۸ جسد از محل حادثه انتقال داده شده و ۳۰ نفر دیگر نیز زخمی هستند.</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SBoxxx/16582" target="_blank">📅 09:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/16581" target="_blank">📅 09:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AniK6UZVx711IE_5kgcvHBDg1aS8vsMyeWRKf4WU4XUxGaHlkcMuBXY97IVgtJnJHITCEQXlzolIbi634rKeGcDUaDYNv7zut1lu7eJqKz6zwz8u-Y5WgWJf5V4EJXkcYuAKR8DatOqsOfzRTfR8jQ2aN1OeDn457I8xEOsA-iWFyyAqQbgqveMlJsySMDg5W9r8kPvo5pBizJhM1UqxeVDoc6RB6DNDdYO-PMfDqk9OquIP7VvKyxad19qIv4xq3umgaWC8X-dpunyETuMcUdxMtvRGI0UmGP-Byb-cFxEIYb1uLNSKJCUeaypVZtfE7KmsgTKAGVC4ysF7dCpRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاهک موشک اورشنیک روسیه تا 4000 درجه حرارت می‌گیرد که می تواند فلز را ذوب و بتن را تبخیر کند و خودروهای زرهی را فوراً نابود کند.   برای اینکه دید بهتری از قدرت ویرانگری این دما بدست آورید اینجا میگویم که چگونه این دما با سایر منابع گرمای شدید مقایسه می شود؟…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16580" target="_blank">📅 06:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16579" target="_blank">📅 06:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA806WybTYfgE9xyNqG23G5WfjHbtvBOTasPa3nDzzU7B_2dwGJLVR8sgYY0VVl303OuRCW7R5uzhFi-GpqojeGyXpqaFfmnh3curxgZH9ABfa14lTnpmgFL61tkX5xA3xbaHNLkOosZOS2xxd9JNW_6penefMwCXyNhB9S6ichX8yXBap8RXvXHGJzvrz9NFUaadBhqvL0wPtGgcWBGJwpBWJBhcNLSBsOtCkl-bA8EsgQabx-l2cGNGxYdAddGxgpthpxl-jsKyiFeGRNGvkUKV276H7SjG9AUNSazNV1QLZ6mZrBDa9JzuyVjw5l8-U10FYnktW8gAODLnlfDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس مخفی ایالات متحده بیانیه‌ای در مورد حادثه تیراندازی در اوایل بعدازظهر امروز در نزدیکی کاخ سفید در خیابان ۱۷ شمال غربی و خیابان پنسیلوانیا شمال غربی در واشنگتن دی‌سی صادر کرده است:   پس از اینکه فردی سلاحی را از کیف خود بیرون کشید و شروع به شلیک کرد،…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16578" target="_blank">📅 06:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/16577" target="_blank">📅 06:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هاآرتص درباره افسرانی که در لبنان می‌جنگند:   وضعیت ناامیدی در میان ارتش به دلیل افزایش تعداد تلفات ناشی از تجمعات حزب‌الله گسترده شده آن هم در حالی که ترامپ اجازه عملیات در بیروت و دره بقاع را نمیدهد و عملا ما فقط خانه های روستایی را منفجر می‌کنیم!</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16576" target="_blank">📅 06:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انتشار داستان طرح ترور ایوانکا ترامپ و همینطور حادثه دیشب نوعی پیام هشدار به ترامپ است.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16575" target="_blank">📅 06:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">واقعاً طرح پروفسور شریعتمداری جواب داد؛  اکنون که تنگه باز شده دیگر وقت ترور ترامپ است.</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16574" target="_blank">📅 02:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16573" target="_blank">📅 01:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">توافق صلح آمریکا با ایران شامل بازگشایی تنگه هرمز، پایان محاصره، آزادسازی ۶ میلیارد دلار از دارایی‌های مسدودشده ایران و خروج نیروهای دریایی آمریکا از اطراف ایران است</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16572" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16571" target="_blank">📅 01:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16570" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjvlfP7BQfEOgq2tmNY9qhTSS88FjeTM70-i7s_NnBDxwYPK8ZPrXPpVMpZ5F7cBQkWznhAMNd18uizGjmWOrBGhGXC72NduweI67xRtIk4i1EYvI2AEqmcy1bmnqVIoqw0V59fRxpYCYDn_-5vZbe-wxfwP6VFYbgMopyLLur0jtfZtB3wGMhVEE-xEDXNmoc5QZ7lDWAGgFnyHnLixCuzSUJuBWo1uyxRAS6neHx9dqlfbtDv52wRJyoo1e_x9Ci_BuHYAiVfZ0bvjhFrTlRvX3sRRCvqf-AWs3sHAdNxJ9LFdoX-NxLoQ6iQrYEx5UUI_zOUB4aXzfOkNtvDHQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...  سبحان الله!</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16569" target="_blank">📅 00:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1dNAJk-kW7rsV9weSXgaxuj3bfEqP8VoJMbqlUFEjBtKweykZ-dqQk3A9bA3RQutjOZkahmcHwYWX8l5Csebp7yHjo4dCIIhc_fFXShOgOTKvqPLXYgoWL-GHWJVNwYJhWcow59asWcVQyITicimeAfEBAuzfkO86dEJyVG0WIAnFd8xdy_1ZNoGlTbcDA8Tel4DzpEk3AOMuqSlQVzoA47UUtrKgdfFuVfPdmSUEwF_om-BRvtUFOPz4k3jqk0Zr4cGpIh7QL5Artu1XPhurcTT8OHYZjMmYfjlbDJzbmDLSsbeM0byF0Ob_SWcRHOoWvFEzY8ytkffFFZJVvB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...
سبحان الله!</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16568" target="_blank">📅 00:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
متن کامل توئیت ترامپ در مورد توافق با ایران:  من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16567" target="_blank">📅 00:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
متن کامل توئیت ترامپ در مورد توافق با ایران:
من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رئیس‌جمهور رجب طیب اردوغان از ترکیه، رئیس‌جمهور عبدالفتاح السیسی از مصر، پادشاه عبدالله دوم از اردن و پادشاه حمد بن عیسی آل خلیفه از بحرین، درباره جمهوری اسلامی ایران و همه موارد مربوط به تفاهم‌نامه‌ای درباره صلح داشتیم.
یک توافق تا حد زیادی مذاکره شده است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر ذکر شده است. به طور جداگانه، من تماسی با نخست‌وزیر بیبی نتانیاهو از اسرائیل داشتم که به همان اندازه خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بحث است و به زودی اعلام خواهد شد.
علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16566" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
۶۰ روز تاریکی
❌
🟠
۶۰ روز از شروع عملیات نظامی ایالات متحده و اسرائیل گذشت و اینترنت که از ساعتی بعد از آغاز تهاجم قطع شده بود ، کماکان در خاموشی مطلق به سر می‌برد و با طبقاتی شدن روند استفاده آن ، شکل و شمایل یک اینترنت با حیات نباتی را به خود گرفته است…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16564" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
ثابتی ؛ نماینده مجلس
:
جنگ نظامی مجدد قطعی است ،  حتی اگر آمریکا تسلیم شود</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16563" target="_blank">📅 22:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">—مقامات اسرائیلی به آکسیوس:
« نتانیاهو نگران توافق مورد بحث است و از ترامپ خواسته است تا دور دیگری از حملات را آغاز کند».</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16562" target="_blank">📅 20:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ادعای جدید روبیو درباره مذاکرات:   شاید خبری باشد، شاید نباشد!</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16561" target="_blank">📅 20:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👽
ذکر نام "ایران" در اسناد جدیدی که وزارت دفاع آمریکا از پرونده های UFO منتشر کرده است :
4 شیء ناشناس پرنده به صورت گروهی 26 آگوست 2022، روی آبهای ایران مشاهده شدند</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16560" target="_blank">📅 19:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
تقی پور ؛ نماینده مجلس
:
جمهوری اسلامی ایران می‌تواند کابل‌های حیاتی فیبرنوری جهان را قطع کند</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16559" target="_blank">📅 19:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-C1dOoXqMZQgrDaSKHbkgmAQ_pd0r8tvExSOci_FkzFiO38wIqE_rxA9MCVyxeSH_F_ZADdGy8UKq2ljj0MDAhYy_suAQr0qYQbcoAwn02a1CzjJmZ8ZvWRY_duRO7ZD8Wv9EKZVY-Kr39EfOSGPt0phmv_pcREBiJj-eijDqnQ_U4XBo-PstUMw3jaI16O3LW4B7bYvUy8hdi05ez_X98Us08apm6fRyq1mwnAol2P-_o_bO8HvQ9UAlmOKq3w50k21OqgeoDXWa22nTZ9v5wKvq4mpqDIbT3kfe3kt5cyfWmJ8GyP_L69IqX0ON4-QU0-mWK3zZkogKntiBS9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16558" target="_blank">📅 18:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16557" target="_blank">📅 17:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی، به زبان عربی:   اگر دندان‌های {آرواره}  یک شیر را باز کرده ببینید، فرض نکنید که شیر در حال لبخند زدن است.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16556" target="_blank">📅 17:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ43xYQMC8FTwhEoPxGHn-zNUZ6mRtHcEzXuboCE4xrl3TrSgd_XwVF9_IYM--PDQ_UNDRvuMp6wTRxGV-_4KGfUzT2VRvtULhtdxZOr9Wzq-LPo4DA34ieTESg2ImT1P7MWU6qK7jgSD--NlaxYZbXcXS3AvTxz2pGSXc8vv6mmCYvBA3k0GWRYlJVZu2JLIlnmbBTdQeA6MWSpRSf26JfASNWw1I5pSIpWYn5KD1l4BPlAQowaChSfRI7cbU3Ru1OSReunKclyL6_f6GlM9EMmQtfN2g_557bmf1aZxQR79M5gMDdkmO_OASmW-6U_74S60Vuef5_ZsjIVWBw4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16555" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16554" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16553" target="_blank">📅 17:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">—یک مقام ایرانی به الجزیره:
«ما با میانجی پاکستانی به یک تفاهم‌نامه رسیده‌ایم و در انتظار پاسخ آمریکایی هستیم.
تفاهم‌نامه شامل پایان جنگ، برداشتن محاصره، باز شدن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
تفاهم‌نامه مسائل هسته‌ای را شامل نمی‌شود زیرا پیچیده هستند و زمان کافی برای مذاکره نیاز دارند. پس از ۳۰ روز از توافق، دربی برای مذاکرات هسته‌ای می‌تواند باز شود.
پیش‌بینی شده بود که رئیس ستاد ارتش پاکستان تفاهم‌نامه را در تهران اعلام کند، اما برای هماهنگی با واشنگتن رفت.
برای ایران امکان‌پذیر نیست که امتیازات بیشتری نسبت به آنچه در تفاهم‌نامه مقرر شده است، بدهد».</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16552" target="_blank">📅 17:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjcPEaztXhW4rgaxlazHJiceSFPAeCCbVvWOeTBcQiwy11ocRP0rq1q4emsCZXJsIAETmwH_w7n-7vEDS0wSd1yFMKXZlEVjrwX1UvUukFuwjT07rPc-X4ivYZrNg5TYdznJdcRPa1dPS65emQ2gpTtXXzFAApj5l0iW3QHCEs68fNf2vxP-Tc8c53P0RkpgOxwbPsOHn08ujVhJ87htfkPbSt9dW28IJNK4wmKSvPKqbvlfoTlS6XExIr1z_SinqE0qRP60BRV5Cr7JQdkC5YETlXuNkLfE6sFOv_kybWAtpzrjy_RDfjueVdva3VfyeLrXhFnKeWgJuhrpjt0adA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!  نکشی مون آبجی!  انشالله فقط کاربرد نظامی دارد دیگر؟!</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16551" target="_blank">📅 17:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m360p69-SNCNJs9hPZcbpw_E-VQPkVF7RRs0dg6ntChO7OFHu8BDlWEUJhPd1wyXqw4XNsyJkAFaqFDMolftsDjVuTpxQEhoDldHJ8OzeO7Zcztp5bBJia-jPrWQ3dPPYlHH_hNBT_w7wli9naytPEkYR414rOEN8WyHfiNQOXD8B6eFnnTd0CkTNXIghKmzKYQ868vNyRvugFG5os5DFSThyYUV7jfsfunoZ4PvLmY-sunZ6d1Dya2JMnmAPistvCgsi7w_bqBGB5i9rd2TqHNkVCCwrOBUMSO3xLXz0HyXf9V3qEj5zUMoJkyzJC-zNJTIuZTuvBeqL3vojFaOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تایید واگرایی میان اقتصاد اروپا با آمریکا پس از جنگ ایران
داده‌های اخیر PMI نشان می‌دهد اقتصاد آمریکا همچنان در محدوده رشد باقی مانده، در حالی که اقتصاد منطقه یورو به‌ویژه در بخش خدمات وارد فاز انقباض شده است. این واگرایی می‌تواند در ماه‌های آینده به یکی از عوامل اصلی جهت‌دهنده بازار ارز، سهام و اوراق قرضه تبدیل شود.
در شرایط افزایش تنش‌های ژئوپلیتیکی و رشد هزینه انرژی، آمریکا به دلیل استقلال انرژی و عمق بازار داخلی مقاومت بیشتری نشان داده، اما اروپا به‌دلیل وابستگی بالاتر به واردات انرژی آسیب‌پذیرتر شده است. تداوم این روند می‌تواند به تقویت دلار، فشار بر یورو و تغییر مسیر سیاست‌های پولی بانک‌های مرکزی منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16550" target="_blank">📅 15:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/16549" target="_blank">📅 15:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کارمای اجدادمان که سهل است، کارمای قابیل دیوث را هم سوزاندیم در این زندگی</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16548" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صبح تا شب این وضعیت مجریان ماست در سداوصیما ، در ماهواره هم که فقط صحبت جنگ و حمله است، نت هم با گیگ ۵۰۰ هزار تومانی باید برویم تانکرترکرز و فلایت رادار و اکانت کله زرد پفیوز و حساب محمد something های وطنی را چک کنیم ببینیم کی جنگ بعدی می‌شود!
بعد این نکبتهای انگیزشی میگویند بیدار که شدی به دنیا لبخند بزن!
به … عمه تان لبخند بزنید قرمساق ها</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16547" target="_blank">📅 15:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سبحان الله!  نکشی مون آبجی!  انشالله فقط کاربرد نظامی دارد دیگر؟!</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16546" target="_blank">📅 15:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtvxaaIynmaWQ0MtfXwq9mnikOfFfMAiuwKmnyHBKcBCM9qLiwLMy7EMJp5dsuCCqOUEb_k-J5oWdqlwS84TQuHTCEOLwYVmWo670toYFHfCxwoc_9iHndZ080zypRmq18bOVrOnerufNdYrDJ7XyPP-eSk_51-9xjwHNNsbAvukXqrDCRdzMYwehb7bS-2rICs98TI-ArGFl8lH8a1s2-PXqnAcEFHqn0zCaVJ6EBntWri-Jdlg2rfUMOgTxTg_Vwr72h5JJERCcUawo4KUciLZ3mliY6cjKaVvh9jspYtbLyPvScHSFISVoyfo3VyjW12IbMOxAhiO6oAKspj68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16545" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16544">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ اسرائیل را از مذاکرات ایران حذف کرده است!
به گزارش نیویورک تایمز، این واقعیت که اسرائیل «تقریباً به طور کامل از حلقه مذاکرات آتش‌بس» بین ایالات متحده و ایران خارج شده است، به یک «شکست خوارکننده» برای بنیامین نتانیاهو، نخست‌وزیر اسرائیل تبدیل شده است
نکات کلیدی:
🌏
دونالد ترامپ بیبی را به عنوان متحدی از ایالات متحده می‌بیند، اما نه به عنوان یک شریک نزدیک در مذاکرات با ایرانیان
🌏
اسرائیل از شریک برابر کاخ سفید به «چیزی شبیه به یک پیمانکار فرعی برای ارتش ایالات متحده» تنزل یافته است</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16544" target="_blank">📅 14:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ژاپنی‌ها آمپولی ساخته‌اند که می‌تواند عمر گربه‌ها را تا ۳۰ سال افزایش دهد.
یکی از دلایل اصلی مرگ‌ومیر حیوانات خانگی پیر، بیماری مزمن کلیوی است. به مرور زمان، پروتئین AIM که باید بدن را از زباله‌های سلولی تصفیه کند، به سادگی از کار می‌افتد.
اما دانشمندان تزریق‌هایی با AIM مصنوعی ساخته‌اند که مستقیماً تصفیه کلیه را تحریک کرده و با سموم مبارزه می‌کنند. این تکنیک حتی در گربه‌های بسیار بیمار نتایج قدرتمندی نشان داد.
انتشار جهانی این دارو تا سال ۲۰۲۷ پیش‌بینی می‌شود.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16543" target="_blank">📅 14:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📡
وزیر ارتباطات دولت
:
این نگاه قیم مابانه که اینترنت را خلاصه در ۲ پیام‌رسان داخلی می‌داند و برای مسیر اینترنت مردم خط کشی می‌سازد ، نگاه قوه عاقله حکومت نیست</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16542" target="_blank">📅 13:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ایران یک اطلاعیه نوتام صادر کرده است که پروازها را تا صبح روز دوشنبه در بخش غربی فضای هوایی خود محدود می‌کند.  البته خب منظور پروازهایی است که می‌شود ممنوع کرد ولی خب  از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16541" target="_blank">📅 12:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">استعفای تولسی گابارد: ایستادگی در برابر از سرگیری جنگ با ایران؟
تولسی گابارد ممکن است به دلیل سرطان همسرش استعفا نداده باشد، بلکه به گفته مجری TYT، چنک اویغور، به خاطر امتناع از همراهی با برنامه‌های ترامپ برای از سرگیری جنگ با ایران این تصمیم را گرفته است.
ت.</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16540" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16539">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هیئت قطری که انتظار می‌رفت حداقل تا روز یکشنبه در ایران بماند، دیشب پس از دریافت دستور فوری، ایران را ترک کرد.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16539" target="_blank">📅 09:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ایران یک اطلاعیه نوتام صادر کرده است که پروازها را تا صبح روز دوشنبه در بخش غربی فضای هوایی خود محدود می‌کند.
البته خب منظور پروازهایی است که می‌شود ممنوع کرد ولی خب
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16538" target="_blank">📅 08:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.
اما جنگ اصلی برای چند ماه بعد خواهدبود.
در واقع این جنگ کوتاه را می‌توان یک موج B درنظر گرفت که از سقف موج ۳ ظاهرا فراتر می‌رود اما هنوز بخشی از موج ۴ است
سبحان الله!
این هم نتیجه مکاشفات و مطالعات ما با گیگ ۵۰۰ هزار تومنی در روزهای مثلا تعطیلات!</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16537" target="_blank">📅 08:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqR9jqmspVQ-GT5X6Nz0q0-NfRjZ_3iiZMyRcs99uplwqufXKEnt-2x_Bqz8B4rtfeiIDiMfm_X9xIqRP1r8upW0o3xfQh4kxriAlSMJV3ZdBLdST-Reo83qW4kUGOYr10yAh79cg0BX4MaZNlkovQAZbpcPJ_W3tsg3Tn6XKwToVYxWevFBZRjqRZ3Ykkcs8QsOJqk2vuJ052gN-HNTTX7oXp67ypWUdhT6SrUEOh8gF6EglgDKl0Wy40S-pjPHYlrzaJf059iuKmadr8Cl15rJc9SLH7cPnshtTpXDVFh5wFr4YQDN20L1QelNWntTYNZ_jrk8BmaWboIB3XddCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری ایالات متحده دستگیری محمد باقر الصعادی، چهره ارشد در گروه شبه‌نظامی عراقی کتائب حزب‌الله که توسط ایران حمایت می‌شود، و انتقال او به خاک آمریکا را اعلام کرد.  طبق این بیانیه، الصعادی حملات علیه منافع ایالات متحده و اسرائیل را هم در داخل ایالات…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16536" target="_blank">📅 07:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U68w61chUZHUjqCpZTv4b87tMzTN1xlpoUV3ArSKLvhIlc-LS1QgjoZrQnQkW-GwYgNTVR01FHvzuxBwy4XVoq3N-6YmIpQizVKXZ-mZI47o2RZcBX2iCNVl9ouwGPLqh16dVWJsDq4MiyEknFfrTHHhGWSSSMDyVBx4wBgrj5cTrxT0snw1rDsGlpVorfEmMqnCWYxmn5TeCV3valQ80um1OK46DCEMrSJ04m5ke5L9ovguHhqYmsUgFO2PPCHK3OcnruOzALupglB4SGy7Tm8C6fqaw5DO_WCFcuhfezPZ38Ye5xwf2nl2xdK0Kz7uMvuXs_oobdjLj-AObGDKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری سی‌بی‌اس در یک پیام فوری اعلام کرد که دولت ترامپ در حال آماده‌ سازی برای احتمال دور جدیدی از حملات علیه ایران است.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16535" target="_blank">📅 05:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک مقام آمریکایی که در جریان تلاش‌های دیپلماتیک قرار دارد، مذاکرات را «رنج‌آور» توصیف کرد. این مقام گفت پیش‌نویس‌ها «هر روز رفت و برگشت می‌کنند» بدون اینکه پیشرفت قابل توجهی روی بدهد.
یک منبع نزدیک به رئیس‌جمهور آمریکا، ترامپ، گفت که ترامپ در چند روز گذشته به طور فزاینده‌ای ناامید شده و احتمال یک عملیات نظامی بزرگ نهایی را مطرح کرده است، پس از آن ممکن است پیروزی اعلام کند و جنگ را پایان دهد.
میانجی‌ها در تلاشند تا یک توافق موقت بین ایران و آمریکا را تضمین کنند تا از حملات جدید آمریکا و اسرائیل که مقامات هشدار داده‌اند ممکن است ظرف چند روز رخ دهد، جلوگیری کنند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاشند تا اختلافات درباره برنامه هسته‌ای ایران، رفع تحریم‌ها و مسائل امنیت منطقه‌ای را کاهش بدهند.
هدف، توافق جامع نیست، بلکه چارچوب موقتی است که آتش‌بس را تمدید کند و اجازه دهد مذاکرات گسترده‌تر ادامه یابد.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16534" target="_blank">📅 00:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsMiC-2JH9qNt1pKX1uDfNbhA6ebVtVqrLk9M0XhVunIeldWfMF1uPctvsuK2ChpIUa_j_rkxga4QyRLa6gIPeg11fOwH5pKN9o_JwvpF-FJWcUYvO0mU_U0VRKyN9ZjytQQchZN7CzYlq49GeguJ6M04sKzxFiUrdSQGq57ETc1jCFEGkOL4vboPba-CVZZQ27VVc61sp2PQUQMGjc_XsT6WdrhDbaKcKlcYxtxWL_TXtYwjUG904QO9t4VfYwYShbq78WkhaudXU2T6zDAoG9nZAAulvgMfrQ74H30PfjeDRqhvhK3wtgW29ilvvAhNoytqYubrD69XfTjcZc1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کوین وارش رسماً به عنوان رئیس جدید فدرال رزرو ایالات متحده سوگند یاد کرد</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16533" target="_blank">📅 00:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خب به صورت رسمی از این طرح رونمایی شد.  در واقع در این طرح که حریم دریایی نهاد تنگه خلیج فارس نام دارد، عملا بخش‌هایی از دریای عمان هم شامل می‌شود که اساسا ربطی نه به خلیج فارس دارد نه تنگه هرمز و صرفا برای فشار خفه کننده بر امارات طراحی شده است.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16532" target="_blank">📅 23:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایران: آخر هفته‌ای بر لبه تیغ
۲۲ مه ۲۰۲۶ | پیترو باتاکی
مذاکرات درباره ایران همچنان ادامه دارد، اما اختلافات اصلی همچنان پابرجاست. قرار بود امروز ژنرال عاصم منیر، که بسیاری او را «حاکم واقعی پاکستان» می‌دانند، به تهران سفر کند، اما بنا بر برخی گزارش‌ها این سفر لغو شده است.
شکاف میان ایران و ایالات متحده همچنان بسیار عمیق است؛ به‌ویژه در موضوع برنامه هسته‌ای، انتقال ذخایر اورانیوم به خارج از کشور و همچنین مسئله کنترل تنگه هرمز. طی روزهای اخیر گزارش‌های متعددی درباره اختلاف‌نظرهای احتمالی میان واشنگتن و تل‌آویو منتشر شده است؛ گزارش‌هایی که حاکی از آن هستند که بنیامین نتانیاهو برای حمله مجدد به ایران بی‌صبرانه فشار می‌آورد، در حالی که دونالد ترامپ با احتیاط بیشتری عمل کرده و در تلاش است از طریق مذاکره به توافقی با تهران دست یابد.
با این حال، این احتمال نیز وجود دارد که چنین گزارش‌هایی صرفاً بخشی از یک عملیات فریب و انحراف افکار عمومی باشد؛ تلاشی برای پنهان کردن اهداف واقعی آمریکا و اسرائیل و فراهم کردن عنصر غافلگیری برای موج جدیدی از حملات که این بار قرار است سرنوشت‌ساز و تعیین‌کننده باشد. از این رو، به نظر می‌رسد آخر هفته‌ای بسیار پرتنش در پیش باشد.
در میدان نیز وضعیت تغییر محسوسی نکرده است. آرایش نیروهای دریایی و هوایی آمریکا نه تنها کاهش نیافته، بلکه در هفته‌های اخیر ده‌ها پرواز باری تجهیزات و تسلیحات جدید را به منطقه عملیات منتقل کرده‌اند. این جنگ هزینه‌های سنگینی به همراه داشته و فشار قابل توجهی بر ذخایر تسلیحاتی وارد کرده است. تنها در شانزده روز نخست درگیری‌ها، بیش از ۲۵ درصد از ذخایر موشک‌های تاماهاوک و حدود ۴۰ درصد از موشک‌های رهگیر تالون مورد استفاده در سامانه‌های دفاع موشکی تاد مصرف شده‌اند.
بر اساس گزارش اخیر مرکز پژوهش‌های کنگره آمریکا، تنها یک ماه جنگ حدود ۳۰ میلیارد دلار هزینه در برداشته است. همچنین ۴۲ فروند هواپیما، بالگرد و پهپاد یا نابود شده‌اند یا آسیب دیده‌اند که ارزش مجموع آن‌ها حدود ۲.۶ میلیارد دلار برآورد می‌شود؛ هرچند نویسنده معتقد است ارقام واقعی احتمالاً از این میزان نیز بیشتر است.
در سوی مقابل، ایران همچنان بخشی از توان فرسایشی خود را حفظ کرده و گزارش‌ها حاکی از آن است که در طول هفته‌های آتش‌بس، چندین شهر موشکی زیرزمینی را دوباره فعال کرده است. در چنین شرایطی، اگر جنگ وارد مرحله جدیدی شود، نمی‌تواند برای مدت طولانی ادامه پیدا کند و باید ماهیتی قاطع و تعیین‌کننده داشته باشد. در غیر این صورت، طرفین ناچار خواهند بود برای مدت نامحدودی با وضعیت کنونی کنار بیایند؛ نوعی «جنگ سرد» که در حوزه‌های اقتصادی، مالی و شناختی جریان دارد.
کنترل تنگه هرمز همچنان مورد مناقشه است و حجم تردد دریایی هنوز فاصله زیادی با شرایط عادی دارد. همچنین محاصره بنادر ایران که از ۱۳ آوریل توسط آمریکا آغاز شده، همچنان ادامه دارد. محاسبه ترامپ این است که ترکیب تحریم‌ها، محاصره اقتصادی و فشار نظامی در نهایت موقعیت مذاکره‌ای تهران را تضعیف کرده و ایران را وادار به عقب‌نشینی خواهد کرد.
محاصره دریایی به‌ویژه فشار قابل توجهی بر اقتصاد از پیش آسیب‌دیده ایران وارد کرده است. ظرفیت مخازن ذخیره‌سازی داخل کشور به حدود ۷۰ درصد رسیده و همین موضوع تهران را ناچار کرده است برخی نفتکش‌های قدیمی را به انبارهای شناور نفت تبدیل کند. طبق گزارش‌ها، دست‌کم ۵۰ نفتکش ایرانی در حال حاضر برای ذخیره‌سازی نفت مورد استفاده قرار می‌گیرند که نسبت به آغاز محاصره، حدود ۶۵ درصد افزایش نشان می‌دهد.
ترامپ بر موفقیت این راهبرد حساب باز کرده است، اما این رویکرد ریسک‌های قابل توجهی نیز به همراه دارد. زیرا تداوم این وضعیتِ «جنگی که رسماً جنگ نیست» می‌تواند پیامدهای گسترده‌ای برای ثبات اقتصاد و نظام مالی جهانی داشته باشد و در نهایت هزینه آن نه تنها بر دوش بازیگران منطقه، بلکه بر دوش شهروندان عادی آمریکایی نیز قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16531" target="_blank">📅 23:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16530">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VntDzQoaEM5AJHQw0dCgUy1fo1VjlQ_Pi-wlxzybai3VGLtSBKOHCu7BiHu03aVM_Lm_-q9IJECwL4qAYgS_j4ZSfq_uA6I5o96wZ8LPeUINemo91lo9PWSzayY7iHcr09HZXq4yMBzZBp5FBOMJv6qYQLkcU1YqME_4pNtkvfYXgvUmgBHZbs4t1hl3gFj33Vj6CE-gHLr9temH-SiAIJGqu4NDJdObEggT-HQ_skbv1jDuexEOknHmzpnAXCRDB6yvaoH0WH4GfxyvbTQODhlYcsAMSE_CrtKJqa8gcahRFV7Js3puVWZy3uRY4oB1DxGCd71NgETAosWjMbBIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ فرزندآوری در کشورهای جهان
نکات کلیدی:
حدود
۷۱ درصد
از جمعیت جهان اکنون در کشورهایی زندگی می‌کنند که نرخ زاد و ولد در آن‌ها پایین‌تر از
سطح جایگزینی
مورد نیاز برای حفظ اندازه جمعیت است.
نرخ باروری چین به تنها
۱٫۰ تولد به ازای هر زن
کاهش یافته است، در حالی که هند نیز با
۱٫۹
پایین‌تر از سطح جایگزینی قرار گرفته است.
آفریقای زیرصحرا دارای بالاترین نرخ‌های زاد و ولد جهان است که به ترتیب توسط
چاد، سومالی و کنگوی دموکراتیک
رهبری می‌شود.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16530" target="_blank">📅 23:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ffd0c130.mp4?token=P7puX7K9nRfmhDyT__WoN2n2Ivxu5r3Gu9Rv0vi8qcuE1LtVZ6QlZnC7-LapTVggEYuy4XcTtMsBR6DriAs-kQUcAgZ_8KZ0PDDT2XStzrV0asqUm-oL81CZtkTwSCYMu9qMjhTOM6qcFdJDDRgrMYoENwrDcWti1MLhpZqr0so7Ksh_OLjxZh4wmYOZ-Onwh93eHG9Hbv2evIQ7wP6dCAN204CQJczG495zqfE637M_RmS82131DnptbjLNTiSOyLyr8bVbsN-CFUqWc2xwHlO2ONu0FKUPZtXdv94vseF4ueXvhxvxP7LMz5CHD_hDWEEK_DP5VelLVpN3tk5pKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ffd0c130.mp4?token=P7puX7K9nRfmhDyT__WoN2n2Ivxu5r3Gu9Rv0vi8qcuE1LtVZ6QlZnC7-LapTVggEYuy4XcTtMsBR6DriAs-kQUcAgZ_8KZ0PDDT2XStzrV0asqUm-oL81CZtkTwSCYMu9qMjhTOM6qcFdJDDRgrMYoENwrDcWti1MLhpZqr0so7Ksh_OLjxZh4wmYOZ-Onwh93eHG9Hbv2evIQ7wP6dCAN204CQJczG495zqfE637M_RmS82131DnptbjLNTiSOyLyr8bVbsN-CFUqWc2xwHlO2ONu0FKUPZtXdv94vseF4ueXvhxvxP7LMz5CHD_hDWEEK_DP5VelLVpN3tk5pKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی
این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای میدانی» معرفی شدند
فیلم ارسال شده مربوط به رونمایی حرفه ای یکی از ربات های انسان نمای بومی در آنتن زنده صدا و سیما است:</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16529" target="_blank">📅 16:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🍆
طبق ادعای برخی منابع ، عاصم منیر ، بلندپایه ترین فرمانده ارتش پاکستان به زودی راهی تهران می‌شود
🔻
رسانه ها این امر را نشانه ای از پیشرفت قابل توجه مذاکرات می دانند</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16528" target="_blank">📅 16:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
الجزیره به نقل از منبع پاکستانی
:
بالا رفتن سقف خواسته های جمهوری اسلامی ایران و دولت ترامپ در بحث تنگه هرمز و اورانیوم های غنی شده ، منجر به بن بست در مذاکرات شده است . ما همچنان به حصول توافقی واقعی خوشبین هستیم</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16527" target="_blank">📅 12:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jtul1R4essefPT8zxEehKp5_s8xsRkGNkRZ5G4_jN4WpAJrl87VJ3q2-HMcDBEO45qdSOIhRefl4QBVWHOaM8WJN4pDqjo88EWazFGClBpPiJNuia-_YU1i35jSjXVRTHGnu5SiH4DYaSpfs-itC9mJvi86lIFt7y9y6OE45CfVgi1vraV5TLwnEltAipcp8Sg4yCfSHiS9VXLUYjT-CPK4SJreVzpy7ap08b9N_s4yno6hIy8ybn7ogH_dXP9wCVdnnxXHKWhtvKKKNo9BSjI1BbYk89XDX4Dh5blrRwZZlVIaCfgGeSkhL-5oLac2vnKg791CHVHW1y7sOCyUoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TUR — D  عیناً طبق مسیر می تواند با تکمیل این سروشانه که همسو با پایان یک رالی 5-موجی است یک افت سنگین اصلاحی داشته باشد و سپس رشد اصلی طبق مسیر پست ریپلای شده محقق بشود.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16526" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXF5EM01wANZiWbYeWOkAdhCxhcMS1jEnOV2Ua7IblpzWU1-IOEE1DlooA1--YVOrGNBd-eVxtbyZcIXXVutnpHDbAoCfAwx2IltRMRebu8vPx9nwhMf2JYA1WtBSbRpwPqXEF8xsXlBOdoUssQ3wbzKE5DlTnh1ssYdkeCM2tFphKJQgLWIFhKRa0VWfUIoa9WG7HR1P62N-kN8w6fw2oq8bAOa0qH-KKQZRkjrNwl7cWdxbnyibKYC1ceszIh8_4ZVYLSy3q6XLAHr9Xtv1FswkSakrN5lURXCM0xMS8lFI5YB3gc02hrC16k19ILiRN_LcK8TiJ6jqM995w0awg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TUR #Turkey
🖊
با داده هایی که اخیراً منتشر شد (موافقت ترکیه با پیوستن سوئد به ناتو و انعقاد قرارداد خرید تسلیحات 23 میلیارد دلاری بین ترکیه و آمریکا) به نظر می رسد سناریویی که اینجا گفته بودیم (نزدیکی دوباره ترکیه به غرب) در حال تحقق باشد.  این نموداری که…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16525" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fShAujtrok_s4GWGFGEiEPhLYfksTmTLINaZzY8c_7wlsMBsO46rTsKgG2qFkoV-5l_iYRWJzjmkAen6DFRbejCn5QkT-byBuTuix_gD1yh9vfpUG0MofWi_2MI2lU39VRndnMuiTqluEQ0pBMLf5uarki3Hjmv78S1bTH2v-djUj77UQQp8jMdJikeTRr6jKaHbYbM0WiE3kqcr7gefa82AK5u4yF_f3qECDI5Fwvo5O8Y8SFn9qgWTcY9k0sZgDPM2bupcb8HkHoftpdRouhw81HgP5vCmIy5WO3_AWAT3ddsulVdK0L_iQ7MdbcvEqWDYPLjwh0Ze8qUgX4Mp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط آزاد شاخص بورس استانبول در پی صدور حکم دادگاهی درباره ابطال نتایج رقابتهای درون حزبی حزب اپوزیسیون جمهوریواه خلق</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16524" target="_blank">📅 10:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دولت ترامپ فروش ۱۴ میلیارد دلاری سلاح به تایوان را متوقف کرد  بر اساس اظهارات هونگ کائو، سرپرست وزارت نیروی دریایی آمریکا، دولت ترامپ فروش ۱۴ میلیارد دلار سلاح به تایوان را موقتا متوقف کرده تا ذخایر تسلیحاتی آمریکا برای جنگ با ایران حفظ شود.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16523" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16522">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به نظر معامله بزرگی در راه است.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16522" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجار در ابوظبی!</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16521" target="_blank">📅 10:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وقتی صحبت از عقب ماندگی ذهنی میکنیم منظور ما این است!  رفته با دیوار سفارت آمریکا در ترکیه عکس سلفی گرفته!</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16520" target="_blank">📅 10:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFnv3uzxfwidbTmf0AtSu2cBxNooxoTtRyB0OodlDOBLIG-mp3BtkWgM7m3x86Aal78V6A-CMYvhGm8obykNLsBUo0VIX3p1gyOW4XPuWloZWIgqmSdbbCz05KKhy6lbfATDM-reprviBt_ouPFZiC0008JTBa4Ae4pAoaiwg0Cgf3JRiWbGR9dXDILuyUDbFH1KdhYnku_JapJVYOAJnHvQTunxMH_4vUPweeAU2SWMRwYaHUliHg8vjCZ46RVHwEZE572T74fyS87V_hX8lDSIjnapo_gvD-6N3pqYrtZxt1sziDMhB06Kc3apa7ODYRyohLwZkTLPNdruINBYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۸۰ درصد هم عقب ماندنی ذهنی داشتیم که ۱ درصد آن را جبران کردیم ولی خب هنوز خیلی کار داریم و نباید بهانه بیاوریم.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16519" target="_blank">📅 09:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgvy0CIDYfvB9wrHDwVW84C2rin4uEfVlyAYIisbEWVhBhkDbr3P-bOIkFspu7O54Aa_XZHZ7GyiAH4Nsgivj-2SoqDVaI2yj1pbHBHbAXSdFXic3iKyRW3uLbSiuEnF4-vjDkkpn1DHFvJ3HNOhClhZ6TPyriXsbvKVvYRonXdg7GDcqk8vHj7rh2kBBGfYFIEBgMLZ4V4xK5kNt_y9OIP9CHs2L1k_dsvshrPkmkg9m-IgcYfZViyGRy3TZBma_FMSE5T1q4aR65739w6bF0NxBqUGGtrUflCxYJsftWcZOuNJjOfg7ImGFVomVoBURS5lss4Sf0u1z8OugnQ-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سهام چین</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16518" target="_blank">📅 09:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رئیس کمیته نظامی ناتو:
پهپادها نوعی مسئله انقلابی در میدان نبرد هستند. آن‌ها تنها سلاح نیستند، اما احتمالاً برجسته‌ترین سلاح خواهند بود و بر کل فضای نبرد تأثیر می‌گذارند.
احتمالاً در درگیری‌های آینده، آن‌ها اولین چیزی خواهند بود که در جنگ درگیر می‌شوند. آنچه اساساً آموخته‌ایم این است که آن‌ها به‌طور چشمگیری زمان چرخه کشتار را کاهش می‌دهند.
این موضوع به دقیقه‌ها — یا حتی ثانیه‌ها — برای شناسایی، ردیابی، تحلیل، کشف (شناسایی)، شلیک، ارزیابی خسارت و تغذیه اطلاعات به عملیات بعدی تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16517" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZelYhwLbupU1LO7mpwzSMWikayo9ioX3PVVA-T9pOu4zMTNRO-7D-Cwwp6htvtdII8cy0QR48QJxJbIGrBu-6n7C1qW5k7UCmrI9aUs6OlsSPW91mggiOm2SNMnD9DHyyTzqFRPusRHuoNl3O3Aq_bxyZ2fucE-TWZLVMakCellc_aQ7LfYMWNajcAqBpAPJwPPm7RZQgXK2bZbG20yMfqeJBBYlrXbX9vuyGVu0hKR1VyUVHuS9iDe_YCBRc4JJhjL_6hnLVcaRYoyOTeuvClsQtVTxQOBapvdtDWBdf0WKevvUiNIQPjQl3Lw-HQb3F-U9GuT119Aee9qDdwihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16516" target="_blank">📅 01:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این جنگنده ایرانی هم امروز در تهران مشاهده شده که ولی خب.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16515" target="_blank">📅 01:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شماها چرا شب جمعه اینقدر میخند؟!</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16514" target="_blank">📅 00:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این همه زحمت میکشیم بهای نفت را بالا ببریم تا هزینه جنگ برای دشمن زیاد بشود آن وقت این دوم خردادی های چهل پدر میزنند زیر کاسه کوزه مان.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16513" target="_blank">📅 00:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">العربیه:   «توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.  این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16511" target="_blank">📅 00:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای العربیه:
عاصم منیر امشب به تهران نمی‌رود</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16510" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">العربیه:   «توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.  این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/16509" target="_blank">📅 21:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">العربیه:
«توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.
این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و تنگه هرمز و مکانیزم نظارتی مشترک است.تحریم‌ها به تدریج در ازای پایبندی ایران برداشته خواهند شد و مذاکرات درباره مسائل باقی‌مانده ظرف هفت روز آغاز می‌شود!»</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/16508" target="_blank">📅 21:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فیلد مارشال منیر پاکستان امروز به جای فردا به تهران سفر می‌کند. با این حال، به گزارش‌ها، منیر به ایران سفر نخواهد کرد مگر اینکه نشانه‌هایی از پیشرفت واقعی در پیشنهاد فعلی که ایران در حال بررسی آن است، وجود داشته باشد.
گزارش‌هایی منتشر شده که احتمال توافق قابل قبول میان آمریکا و ایران را کاهش می‌دهد. به گزارش i24 News به نقل از منابع آگاه، آمریکا به اسرائیل اطمینان داده که هر توافقی با ایران شامل خروج کامل اورانیوم غنی‌شده از ایران خواهد بود. با این حال، امروز گزارش‌های رویترز به نقل از مقامات ارشد ایرانی حاکی از آن است که رهبر معظم ایران، آیت‌الله مجتبی خامنه‌ای، به تصمیم‌گیرندگان ارشد ایران دستور داده که با توافقی که اجازه خروج اورانیوم نزدیک به درجه تسلیحاتی ایران از کشور را بدهد، موافقت نکنند.
این در حالی است که فیلد مارشال عاصم منیر، تصمیم‌گیرنده اصلی پاکستان، قرار است فردا به ایران سفر کند و دونالد ترامپ، رئیس‌جمهور آمریکا، می‌گوید زمان برای توافق با ایران رو به پایان است</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16507" target="_blank">📅 19:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsCpxhvxxQVDXLJRhdKJakDDaUFWZYD4e-WfER4dPLkTe65p2B8QReWv0Cscvm7TPET_SEH8cJfa9j1A_gk5NcFIQ1KH4_gowQ8M53QesduHDtY2cHki5F7aYa-np424nHInwjxKAY9Wh1EfgHvJOGxsAJshWrp7nH3BfN9ejmnYAVeOVVZ3Q2dcAz-faxmBzI77cWWM9LuMw11aplA8zcA4bcT4Zb1dfqhoI2gWe88Vd9ezdLanq0jFbxQ32xs1dAV7IKmuPf7Bk-vNNKVA0xZn97uHKruIJGDgr6_vdhETeNFTajRyybFIK1zvC7e9BCETDFC1bK3VDgacMHV08Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاتا الکترونیکس و شرکت هلندی ASML در ماه مه ۲۰۲۶ یک تفاهم‌نامه راهبردی امضا کردند که هدف آن پشتیبانی از راه‌اندازی و توسعه نخستین کارخانه تجاری تولید تراشه‌های نیمه‌هادی هند در شهر دولرا ایالت گجرات است.
این پروژه که ارزش آن حدود ۱۱ میلیارد دلار برآورد می‌شود، یکی از مهم‌ترین گام‌های هند برای ورود جدی به عرصه تولید نیمه‌هادی‌ها به شمار می‌رود. بر اساس این توافق، ASML تجهیزات پیشرفته لیتوگرافی، راهکارهای فنی، آموزش نیروی انسانی و پشتیبانی عملیاتی لازم را در اختیار تاتا قرار خواهد داد.
فناوری لیتوگرافی یکی از حیاتی‌ترین مراحل ساخت تراشه است و ASML در این حوزه جایگاهی تقریباً انحصاری در سطح جهان دارد. انتظار می‌رود کارخانه جدید تراشه‌هایی برای صنایع خودروسازی، ارتباطات، هوش مصنوعی، تلفن همراه و کاربردهای صنعتی تولید کند.
با این حال، این تفاهم‌نامه به معنای انتقال فناوری‌های فوق‌محرمانه و پیشرفته‌ترین دانش فنی ASML، از جمله فناوری ساخت تراشه‌های نسل بسیار پیشرفته، نیست و هند نیز در کوتاه‌مدت به رقیبی برای غول‌های تولید تراشه جهان مانند TSMC و سامسونگ تبدیل نخواهد شد.
تمرکز فعلی این پروژه بیشتر بر تولید تراشه‌های مبتنی بر فناوری‌های بالغ و میان‌رده است. با وجود این، همکاری تاتا و ASML از منظر صنعتی و ژئوپلیتیکی اهمیت فراوانی دارد و نشان می‌دهد هند در حال گذار از یک مرکز طراحی و نرم‌افزار به کشوری با توانمندی واقعی در تولید نیمه‌هادی‌ها است؛ هرچند موفقیت نهایی پروژه به توانایی آن در دستیابی به تولید انبوه، بازدهی اقتصادی و سودآوری پایدار بستگی خواهد داشت.
گفتنی است شرکت بزرگ تاتا توسط پارسیان هند بنیانگذاری شده و مدیریت می شود.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16506" target="_blank">📅 18:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اورشلیم پست:   ایران پیش از جنگ اخیر ماهانه ۲۰۰ تا ۳۰۰ موشک بالستیک اضافی تولید می‌کرد و تنها در ۸ ماه حدود نیمی از موشک‌ها و نیمی از پرتابگرهای موشکی از دست رفته خود را جایگزین کرده بود.»</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16505" target="_blank">📅 15:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GandIOcByF7zLmoeP20Nl4Fb96VhqEiFG9I25pbAojNv_BL2Adqxpq9AyrXBMibJGarF7SdBDsHPJG2iAupdDKSEs6jUOv9JYpwW3BzRw1Pqm_vESp0eZyvl0N-71NI8md2XFEpOB4F5JBBw3B4i0l8RuxM-8UdTurH7M_NmohvjQy5YLuAGuDSOp8INvuNQV6FXO-yjStaQs1THvwpbHAvKfksOSmb-ZDFSzB2-1JW43csG8LA4a3IkklhwWPwmsm9Q9y6l_Vf_dIyFKNHqJgLwGKEbUFOzQRxPM-fqKL-pa-QNk91oSp_-qvGklWWpNs7-huM6d0GzJsPBrEa4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16504" target="_blank">📅 15:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز:
رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16503" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kobqa0Zw9uS54rHDutJ3QZM0Eq-jPvlkOXf1jIso2eS__lJaS-sYJD9VZU-nEfMx82WRNsQ2U6mmFB-HjTy1SJS-_juzARwSMZ6Yzmd23X94Y5X-iqzgiPxWWeYw4LGw14neYjyOYBL4HO5KFLSvmeLZq95ZKsH_rJvOBHkfxhLbUUxeCk9Irx9M4-Yh4lYzHkewf4nige5Riufovk2HzyQRHAZvIga6yJJw3i1hn6-ZWrmdUsFCSOYUy8mTPV6Tc6BAbIJpKWtdcWAMzegekH2kxubndQgtWqPshzcqEF-43gVQP8ZNDFgQfDFB8DNn2otWB8NLnckTav2EpWCHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
هوش مصنوعی "بله" همچنان بعنوان جایگزین چت GPT و میرا ، در راستای رفع نیاز کاربران فعالیت می‌کند</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16502" target="_blank">📅 13:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-pqK8LxQxtb052UHKmtyhbd1_r7HLYMf-UQJYEBsUvYNRmpWRphac9BDar24NXI0N1wWDMZYtSYXa74Xsq_kYlRMRoxD7OYfCHC5TZHm0xpaNO445BO9c2aM8uKFIh-EPinxpB5YiHSrzdNKtVaWLnAdt_j0LsKRc3rsuE7UBGxJUeOt2HXgxWSH3xpU5XHT1KTKfsdqPvn9PcxKFjZHmiodCOYCHIIT8kn7CpbD6GfkCihcRopnKfoaoAO9tpHsFNnlFayRqNNiGGGfhIkT-4OB0XF3yZm6WyxZNUyVvkQ2QnoczUNWZMRBWxd-Untqia5G8oJ0vLekYA8xQPB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ایحاد شکاف طبقاتی دیجیتال در ایران طی ۳ ماه گذشته
🟢
در این مدت سهم کاربران اندروید از ترافیک اینترنت ۲۵٪ افت و کاربران آیفون ۱۸۰٪ رشد داشته است
🔴
آمار فوق نشان دهنده خروج میلیون‌ها کاربر حاضر در طبقات میانی مالی جامعه از فضای آنلاین هستش ، به این معنا که کاربران آیفون بطور معمول از طبقات توانمند جامعه از نظر مالی بوده و امکان خرید کانفیگ با هزینه های هنگفت فعلی را دارند و روشن می مانند اما کاربران اندروید که درصد بیشتری از طبقات میانی مالی جامعه را تشکیل می دهند،  امکان تهییه ابزار دسترسی به اینترنت آزاد را نداشته و خاموش شده اند</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16501" target="_blank">📅 12:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🛜
روزنامه الاخبار :  اسرائیل درحال برنامه ریزی برای ترورهای گسترده علیه حزب الله لبنان و جمهوری اسلامی ایران است</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16500" target="_blank">📅 11:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16499" target="_blank">📅 11:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🛜
روزنامه الاخبار
:
اسرائیل درحال برنامه ریزی برای ترورهای گسترده علیه حزب الله لبنان و جمهوری اسلامی ایران است</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16498" target="_blank">📅 11:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16497" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌊
شریعتمداری؛سردبیر روزنامه کیهان:  تا زمانی که ترامپ را ترور نکنیم ، تنگه هرمز باید به روی شناورهای آمریکایی بسته بماند</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16496" target="_blank">📅 10:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌊
شریعتمداری؛سردبیر روزنامه کیهان
:
تا زمانی که ترامپ را ترور نکنیم ، تنگه هرمز باید به روی شناورهای آمریکایی بسته بماند</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/16495" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شرکت SpaceX، کمپانی xAI را تملیک کرد و به این ترتیب ارزش کل برآوردی آن در آستانه عرضه اولیه اش به 1200 میلیارد دلار رسید.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16494" target="_blank">📅 09:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روایت ترامپ از مقابله ناوهای آمریکایی با پهپادهای ایرانی با بهره گیری از سلاح لیزری!</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16493" target="_blank">📅 09:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ریزپهپادهای حزب‌الله   فیلم‌هایی از جنوب لبنان تایید کرده‌اند که حزب‌الله بارها اهداف ارتش اسرائیل، به ویژه تانک‌ها را هدف قرار داده است، در حالی که اسرائیل به عمق بیشتری در سرزمین‌های جنوب رود لیتانی فشار می‌آورد   گزارش‌ها تایید می‌کنند که یک حمله پهپادی…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16492" target="_blank">📅 09:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNF3pnpYjGAuFTQv-JiAzfSZrKb2bEXqcQFUH0v0ody-zouIhntdKSZnz1D5yClW8crv5LSjeFHLuhHv0MiNXmdlAlrUoQMRC_LjqGW63Jj9z9jo7TC018F0qLgYQ72FBuFHZ7lmR3BdiSOCx1CfQGhF7xLEjFwL77u9EeGxk99f1Mvn-198cDBlwKk8lAb2jzuRG-HyQF3-G8DVYk54zMgORojW4ZDYN2JXs-HN7YMOiTMRGsHwQU2QsWWBAi5OLPcVpuJsfC6uHESP9JZdYIpvwl3qsi5Q8Pmg-j424lRS4lQmzGjMG-ze5Et8vwvsbaPutf2lSjx4dHUuwgwGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طرح جدید سپاه، کل منطقه بین این 2 خط تیره حوزه دریایی تحت کنترل ایران تعریف شده که ملاحظه می کنید بندر کلیدی فجیره نیز درون این حریم قرار گرفته است.  در واقع آمده اند تا خود فجیره این حریم را تعریف کرده اند تا امارات نتواند از این بندر صادرات جایگزین انجام…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16491" target="_blank">📅 07:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzmum1yhxkITW0FPuQBdEGc2Qc2faxGEqicntf_SmhGXr1QQSFP60jQRuyGapkU72_2RBEN6e6GCFPgOngoPcFkK1DNwOJy367UMpqpD1mrRy-NW4pHeFP01p5KB4lqiatLGt1aSEZIbnyUbOdbyGCeeV9yYCS4VZqEtMpkmcjxGmHjLQr5WBpZ2OX8j_nODBFJH-dWA0uE0kve354v_W21CXYgg9PQqfL9lzTU0a1Ixn7LHqpCWLyg7VXvhbVx9UkedbZD6PGwhoOAmrzOT1TSpKkRo5bohPc9ywGxTJMLBR08hiLURLm2c6QuS6F4Q6RiY11uiT3QM7eJrXD2_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16490" target="_blank">📅 07:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzfhO7aMRUZFP6jYKugGf_5bjflYeZ-pPRMVeAxpX9GieBxVsSCUYgkIO8bkbFwKjDAKzrUrf5wxlU9a9lWELHhLKXQV5S1ZSsQH-kCgPSSt9ImXkaVxM39KA03kWWFBTLurPK7_b0pLRA96ZUUJcYAPlgbv3vu90DBuVfCnCM9XIkksVPd8aztbYa-NjJpqLgvKvJywev05mAaI6o5xy43Gg-y-gZ2RuvdvNQh-zGfq14FwcsFGgVjwcZwaPxGpTs0ve6OHMbAosYjTmiNe2q07utWA_8nNOgQfOuguL4y9fShMaTwdNTpsGMJP7JFjCz6ouCFZ3QwozVJQpzQoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران، احتمالاً با کمک روسیه، الگوهای پروازی جنگنده های آمریکا را نقشه‌برداری کرده و خود را در موقعیت بهتری برای استقرار سیستم‌های دفاع هوایی خود قرار داده است.
یک مقام آمریکایی اظهار داشت که نابودی یک جنگنده اف-۱۵ در طول جنگ نشانه‌ای از این بود که الگوهای پروازی آمریکا برای ایران قابل پیش‌بینی‌تر شده‌اند و با طولانی‌تر شدن جنگ، ایران به موفقیت در نابودی هواپیماهای جنگی آمریکا نزدیک‌تر می‌شد.
ممکن است روسیه به ایران کمک کرده باشد تا الگوهای پروازی آمریکا را نقشه‌برداری کند تا تجهیزات نظامی و سیستم‌های دفاع هوایی را با دقت بیشتری مستقر کند.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16489" target="_blank">📅 05:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۴ اسراییل:
نیروهای آمریکایی یک نفتکش ایرانی را در خلیج عمان توقیف کردند .</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16488" target="_blank">📅 05:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
کانال ۱۴ اسرائیل
:
باید به یاد داشته باشیم که ترامپ یک تاجر است و اظهارات امروز او با هدف تثبیت قیمت نفت بوده</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16487" target="_blank">📅 23:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">توماس ماسی جمهوری‌خواه ضد اسرائیل در انتخابات مقدماتی در برابر نامزد حمایت‌شده توسط ترامپ شکست خورد
توماس ماسی، نماینده جمهوری‌خواه کنتاکی که از سال ۲۰۱۳ در مجلس نمایندگان آمریکا فعالیت می‌کرد، پس از باخت در انتخابات مقدماتی حزب خود به اد گالرین، کنگره را ترک خواهد کرد. ماسی تنها جمهوری‌خواه بود که در پی حمله حماس به اسرائیل در اکتبر ۲۰۲۳، از حمایت از این کشور خودداری کرد و گاهی در رای‌گیری‌های ضد اسرائیل، همراه با دموکرات‌های رادیکال رای می‌داد.
در شب انتخابات، ماسی با کنایه‌ای تیز گفت:
«دیرتر خارج شدم، چون باید حریفم را پیدا می‌کردم تا باخت را اعتراف کنم. و مدتی طول کشید تا اد گالرین را در تل‌آویو پیدا کنم.»
گالرین، که مورد حمایت دونالد ترامپ و کمیته‌های حامی اسرائیل بود، با کسب
۵۵ درصد آراء
پیروز شد.
ائتلاف یهودیان جمهوری‌خواه، که مدت‌ها با ماسی مخالف بود، این پیروزی را به عنوان پیامی واضح از جمهوری‌خواهان کنتاکی دانست:
«در حزب جمهوری‌خواه جایی برای کسانی که پشت به برنامه MAGA می‌کنند، وجود ندارد.»
آنها گالرین را یک میهن‌دوست واقعی توصیف کردند و رفتار ماسی را در طول کمپین انتخاباتی، از جمله تبلیغات ضد سامی‌گری او، محکوم کردند. در یکی از این تبلیغات، که به شدّت مورد انتقاد قرار گرفت، ماسی مدعی شده بود که پیروزی گالرین «دیوانگی بیدار ترنس» را به کنتاکی خواهد آورد و این کار را به درخواست پول سینگر، میلیاردر یهودی حامی جمهوری‌خواهان، انجام می‌دهد. در این تبلیغ، یک ستاره داود رنگین‌کمانی کنار عکس سینگر قرار داده شده بود.
با خروج ماسی، حزب جمهوری‌خواه گامی دیگر در جهت حمایت از اسرائیل برداشت. این انتخابات مقدماتی نشان داد که در حزب جمهوری‌خواه، مواضع ضد اسرائیل دیگر جایگاهی ندارد.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16486" target="_blank">📅 23:40 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
