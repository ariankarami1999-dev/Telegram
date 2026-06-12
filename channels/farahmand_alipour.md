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
<img src="https://cdn4.telesco.pe/file/fCTAvFmpGhIiDlGKyMLZf_I6ZNZU6_lrgFlDmDO06hhkU7ZSRONIF3hQTVywJjNRy4cC7XLETBShSqnJW5XZDMUeZ40qx8gnfnvwQIeZ0GYSbC2cHfBZk7h-3sfVlKAwvuJMD_64Jn9T99ohgEDSYStewm_QKbMY8Jf1xWevoXn1Myg_gBEmsbk70NTbxbjddQsNrcH2dloMQYoVqaxXtaDRC1NDn3LHLTq8ZnH2U-xUx5ABqnDBxUG64TmcxBIQmnSkIMUm2K3uNqhhVXLNvz_NgKXTVJCv_lkOm9XtMtO6dUvUCk9S0dKW2bv98ychhkoD-EfCKAqhuK3nktKSww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 05:12:38</div>
<hr>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkVg761KSZAfaC4OXcuYo7SAJa1RjV237Yyf-QwFenlX-GsGqWOJz477oFhfsHAhWKuHXbAWG-F5YMnKMzamSyRIXJ8CtOjfZb7ne9BrNPkMxQybLCI3O69OdVTEM8eGeAm0pAY0zGRDisHqOuKZ2PLYErCWs-8mlWTAQiQh90ETl-PWzCIOnGjdNi0fRIR6FRiCC8vF5FE_DCCIgIhzGcQ1NPHLF3zQltHYbWiACiXB05QqzRilX4lqOH08r61ppiTZWvn27oT9eYp-TYPzjrNZ8fjpOW53IOU45qp53u0b1EbzvBXePp6CgKzyVRIlu5VQ77QTQks8iondQVmPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=MTQx-xdvtNZ33E-O8VbdvvVNfKtatosZcGBfnetZQVqYTHXE0d30KKO2Kl0epVK6lRWiae42cZEfcfZ7U0lPF5IQ_8-KgkM_JyRvh00vcV8lANyB0pmuRIehsITR9Uc5QIx5hGn5N9piOA0kCgjWEjPeVRK8aCffa7Esa2Pw97VRZhic3Vjpp_VC0mIScTWuzV4PxFK-J_BV3noPsAZ8yY1C90rU02_5npd9ix1TpGfd8HgrQMqrPDDX0p1ueI0fKW310_RTxGTY2Jw5azlFQ1CfeYYOdm7n9s4HssfsVRfbyGueB7KG_pTQkwIDU9YWbOnoxxUnla-DKsC7KEq2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=MTQx-xdvtNZ33E-O8VbdvvVNfKtatosZcGBfnetZQVqYTHXE0d30KKO2Kl0epVK6lRWiae42cZEfcfZ7U0lPF5IQ_8-KgkM_JyRvh00vcV8lANyB0pmuRIehsITR9Uc5QIx5hGn5N9piOA0kCgjWEjPeVRK8aCffa7Esa2Pw97VRZhic3Vjpp_VC0mIScTWuzV4PxFK-J_BV3noPsAZ8yY1C90rU02_5npd9ix1TpGfd8HgrQMqrPDDX0p1ueI0fKW310_RTxGTY2Jw5azlFQ1CfeYYOdm7n9s4HssfsVRfbyGueB7KG_pTQkwIDU9YWbOnoxxUnla-DKsC7KEq2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OENnE6emzRs-rNh4mf9GKANY7T4xVIQqe5FSYR8mSKPIZvMWVRh8yst5GSfb6WyRAxW2I2zpJ4FZVJprAbfbGTD1LTgsEdoScAm1fFd67jAnAhkJwB_N27rQEn1T-DhcVEpwQHnNDkPDfWTMZEt1vGiNOr4FApRPIXuSK_7fsMo3rUVKzD9r91vQhrbsTpOW8g1-Hve0m3p_HUk7w18TLDqvwHW8fwE4Uxb6jt6HPp8-0Rlnju_GNvqEj1mliyeHqV3Wnl8SxNYBO0g2EzCs3WiduYTXQkmkQV9XmfGNL9rovFuogf4CGgKR_p9DJ6e8HSKgSPueVEkZJjpt-MGvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN5qa2K1Q6afAndskOz-9D4lLeFXOpKbeVnEbrnwtPxdWesdYsfUudAK8g51eXLnozGLrJIOieK_S1iuDXQ_dmajZSl2G6KFKIxD8BwgdskxuUAKeBP0yGCu3p_YrhK7_CSgHodEp7fretDtU4NFw5ui3W2oNohM9Uff4wZ1yr1rZ1dF0iy2wriNK5dcOuviaZoj7ky7N0-H2FUaVJRQhrt0QwsgJYYxrEg5sWx8RkBXOTpiNqAqiqebAi11i3vbpZl_RIc2ZG7QO8qH2iyX5bYj__OnNCCLoiu1r1PkEXsq7oMDLVaT-iXRC8wfwmC7JxRJzw7IKbslWPSnUyR_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtqSdSKpRFXwIWDMeR44L08-OgDfkD67WHOXuBtp3VvZ1cclyiC-YpOB_8-RUZpPCqPxTq3n3EqTl-1K7QXkVW_ge_kFiaW6qFjnFVZCAg8_Xe6ZjHpZAU4WyzZJa6wgIQwepjxEUceT3AEUbLS8T6aTKB_7KrQmdLxepS3LAwES2qvtkyuK15DQgdNU4M9RR7ONiIn480x7htYYLEb1quUv21MnQ1EAUoX49Ar32CGF0pYSed1zJRkMsqRQiGmAVGP6g7yyMa5S5AdHQqkBXTw5hRlyd1NRXB2eJUB3T5mqOqIqgUC8K63Ewba-tBehuUEiAdbdjGgwjsmJWdy3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csaBlTeHN3QgQ5LkyNMWUzsPUduhfrqUGAWZ0fUWY8pzzcN1H1LwY8hxjDvj7cd8kGUUG1aAKKUZlp2oKzQae7tRYGsBacTTXfnKPQ7OBg-qO4b7hy9tVnnwh5MT3Kd-Cx-3Vdp1Ded5Cu-lUDK4EkcBAmfauxUfaz0o1jnWHiFPIOK5Sw6H3OruxaTeCIEUqVhdhiqKdO1TuPTqv0GLbJ9FOM5Z-D9UTcFoQFADvUD5zUXH0_Kp6iNxrgm7FksBzmuSAGa2HEeV2OJhiSUOYxemKeNq_mjzRrDeBRI6leapX6XaXDpUybymbgZsChi4ksg0YoRxJN79mAzabK-4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMy6zA__ZvBA7D4_Gi8JrNrlrffDkTLOvoBV8Hr2VubfJuX1JQUOuMoLZIciDn65cb9glH-IopiXuaDaOvzcnPMRWo8dUYeNhY3ms-UVKMQQRJcHlWYBuYtssoixdG5dqkenCqWwvUQS2Q6mHD4FqtE_2ioVQZ_vUCsizFgxDBLEAWOsAutgciNGnOTTisPNLo1dE_OEc8Su1CQ5nXBSjiYXIQguVXTCyZeSVUn4up9x7bsIj11-7dFxH1UYeusaeHnQ27UcXgVNcXaXpNBJohlnqNzmm5HFM-0_O6RiExgWY5sLWJTaGxcduQR-9zkGCJZWDKpZonEeMu3A5Xa0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6fRAXIJKZv4KooSKMnjVYJEX2ecRRAgiTDqDqgz2hrrnnbYvPeORkoARUQpiPZq1vGEtgEUhW3ZfJtGNUcy0xA_r5ftFgWIEE2snb3IniYN34LsdSl6uQCugk_1xNZq_ia-9ppSfL_X0cNyyX63eIEHr7w5MD_3-IdybrW81UZysUXPFM_50S5YqvdOxE1QhD9duXh6a9ecweaTXlewTh8krw6d78SHxsvPocVeRNTI8ZzBc7lzjQqyDTMqgHJCx21L4TX_ekoPCHP1a6dIDiXYzQE1vD-SV3Ax65G1vXVAuiP9-CTRCy2qeQra4et65ZUkNdUVeeOhBYwmpRTE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWJpKke1M0ayZ9SG6XpGV5bSrdWmurMYikEgQXXU-NY2NUp9Wt6puwlWeenravvWWhFyINa0CSbjeTzk_oXp8QzetHFhClWbesYQ1DoZtdvafiurHg5TN7fwjcXdckrSN--z_Mg6y0hVZ-C2k5AOkuwMCW_SPP6JNpHgnmcWayIhqP9V0kObh5iZ-KUQL4CQy4QIOXX1_-xDAUI-i3hbwV23nBLg_OrXVwXFIJCXDsh0bXVGsOqKOOBGP-dXuEW3DgFpxUti_WXHtq50lWgTiwTrRDmXdZOWcorGkqcsdY4crn_FkkEKR_wcPPQzh7r7nPBL20vq0QSiAdOi_Xh0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwJUS3rgbRl0_I74l74ypcXx-EabgK6kDf1M7H03MV0trmeI8oSlGgfkA2n4ucoafICObvHqpJoqCtqV0uTAA0hF1HRCPQyRjeFB_Tuo3AL5mUr6J8Gj6MImb0pGKpSD3Wbo3ytqJCR91FCSFB3HXPq8Bb_5crQd7r-c4yjMZSS_e6GuKD6DBJW25yMXWvZGVZSwD9W_2W-4950yncuDO0L6LnfdWRhUfQ7VlVZJIH2kanVOs7tSkbjyOh6XZ58Mlso3h8ioEA8u3LBjkYnuQOtZ8aLSSRccmUTvHu2gTCbG5FuEjLuQAfZ5DQBMOwbAhAt0_TGFeYnT8dRuoTtuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vArpnyOoUeIPlwRedpoItCqXtYnthsafw4Tw5P3QlJzemeVOKSSt6REMFAQfUVdNXQM5jvP2h3J0wm94JwNMIf1rdOBnZu0SVGacCz8aSgaq7ZGCi01X7tSbwLebxOoFQs5UPVtysdZBZGoQbq8CZf8VyknJk8zUrP5tjgdlgvD6MWkPKunU8wN_OikxbFVMoYrQTouSZ8J7O42B_rFFfX51AgKIZkBKepRJ3edZ_YJZuYBdxzRWN1LT0y4680c3uYGNi3RIRW-r6j-K9apuMeZhz3Jq8kOvwJTK2Muh01IT4wRmtxUs4pHacAiE2Tq4G-ByGzvL7_T4o2qbYhj6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlOY0m4fV8UoDrk-MvjstgOWJmREdbGuq7gektyPPkNy12_eeYyKemge3il2GwkYnFhik6ABhW3Laob-QjGbCXJbhoe4KOn_pnxC7LAe53Z7xx9VglPWCgQt6SxoR8lFmP5NQAl1O8UWznBv-mK3MYkawa0XFRt2mXCyKLgQ51EDc1R_K4imADurRps-LnhJi4HFp2N_uG9C1Bsa5aMnBcuwJVeadrV3RA1T8SAPSTbDbmc6oKYSqRGZhuV4hUSUe6s0CSSMXr7Zzx3KTw9aHUKy_a0fGHe8FGLuFhLU6XC2uAnOnluzRcymA8r_SES-tA1GTEge88RYtyslUhf3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=D9LlmkqhXkSXxGk3NKMWYmY_dvn9lb4i1BtfRQIMVoaGaw2WjJwhm6rg1T1UURuPPNbPDusQMiBn68n1RegW67-b6uj8j8FkMxZ3JWzidgN7pDis4gLnXpL4LOFDllSX9RLnSSeCZT5lvQnuTOl5B2qHG8t8ebmK69wJGWuipU9OBfFt-KRJ_aIC9aRGtt00hnc5d1paBDzZOrAlnrEwfksqHOhXDcwJ9-TlW-C6E7cK3kAkwVRAElETB2wFhGoUQrSBQyrTIFoovMt-pPnLPYMQ09DbplKxSi0mUJni8fkc-LABWAfynp-c9uczt0SEZ4z2PFeuxuMAu4um73pVFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=D9LlmkqhXkSXxGk3NKMWYmY_dvn9lb4i1BtfRQIMVoaGaw2WjJwhm6rg1T1UURuPPNbPDusQMiBn68n1RegW67-b6uj8j8FkMxZ3JWzidgN7pDis4gLnXpL4LOFDllSX9RLnSSeCZT5lvQnuTOl5B2qHG8t8ebmK69wJGWuipU9OBfFt-KRJ_aIC9aRGtt00hnc5d1paBDzZOrAlnrEwfksqHOhXDcwJ9-TlW-C6E7cK3kAkwVRAElETB2wFhGoUQrSBQyrTIFoovMt-pPnLPYMQ09DbplKxSi0mUJni8fkc-LABWAfynp-c9uczt0SEZ4z2PFeuxuMAu4um73pVFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atB3YCPwI8jVMqu56Nq2N2Bswp65QS5pMrqOgufkfXfyVpLB1bKTlpmTUSmfzSr0Jcb32TGFntjoxSgSgFCaLsjbpGFGGeMmTWt5lHKKYxHjwjLT-JDyJo48x1R_qKB1_Zv1D9KewdF5naYpnyeEuyu5tZfA5LNY_CblA6imq7FcLm3Zh39NS6nyNcx10O3oCf7ZaVRCIAPNWpIWLg3R_aUJ0YeWVNLSZ6YNUfcy2rT8-m1IeuW5hSwg5xaXCqJ5_XHvUymmKnGKwmFrY2Yv_4JQIzoWSCidGkMtuPxQ4DRMTCY6XcYHvIcZ733627Hyi1jw2UQJUj5mJgE5BfVpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv-y2ddWQNXj3McyTcxo9fqS9YjP1vh_PYaSSUd3QW-cnHqPLKMTa8mGXa3AQw37rhiSwdPnTzcQPjElYtzPo2QZXoCbs2cxvsD5_MBSY5r50M454xIqCAmd9SfxJT-Toc2WvS2UZbbDhF64wjXit4cUAUoKFdABCqiYDbxhgQpLcjCCk4YlsDUJuLLPynXspoiWEVbTTHKDOhnr9AfQoYbXEMtFrQFZ7qRdlS36Up-xCvFhPJ3ilY0Ag8E-PAAqMMiw9F_YxRCg3bxnJ1Dzch3-NIfmL3zUucmJ2N6MDzSovSrQc4HQpCWww25A7jeitqb2SNxuYyxDBGqC2Sqylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k01NvdKCYox4IjJdvTyjq4F6NpLJU_R2avk8vV6sfbxMd4I6hrP7eZ2GIW4S5azgoBv2tffd4FcY7XtP0cf8zbx8IKwb7JsIy9g03byrPSxtacVGo6ThpDGuV2yVDHDabBUsTZ5PGlSNcS7HSKA19Sg1xmCih1dmqHkC7EAVJn6L_Q956H9tUYQYOe4yL4INKzwUN7IFAu38ppDtM1TleRUDOLrTKgpId9uY-yaE-thhv6VH8Y-Mqa3G8hCIucTWxI-rJo7PvccGkIebSz0gN9kfJwTbY1DVWHXQW9r4PnFt7Gtm6G15wiw9TnVHOnXeFCwLW5wKpOHtQuG1sGjekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdtvBM6xIjm97nL-sdNaUgNANFlvDuHDuuxA0_YR7PT-BUP1q56UDKRd1F6lO6K1bYvrMvaqbczNsQPfYTQAJBo-Cpwa7skR50uOV_ciTK-IysCjpSWT80M8qiVdeaBWais3qFiWahcHtXSTqvnjPlkSv85-aqig-QAfE-9KFrwxaHc_zVlPR4K7lmxI42mPXMNlEJxAxNH-gL1ofd3cTXyXtpdMFCFq1kUdBXxl8L8NKK6Ny99t2Q5K0LpUNo4AdsAp_OPMJg4Da_9I4ilNpP5-TEQiNt1MtfFpsDOlBxsPZknCMgi4OaoTtVRQ8xgsIKNiVAZ4JU3eBL88QW0tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxGYjH0h8AT50brXCb7aA9ivLPJgt2-geNmFeQHG3DSnni-Q4xM8qWz9tgmr8OHkpE-kzxEBIIM1BsztowtT6oPwnI0uAw56E4lMMEFkQmnFDq1ERc8uKNlqBn8RqUys57vGf_ALDbvj5ietNVDWBdg_1KuxDA6sJ2_DvfO5CQG5QzdoBOlCJYelrL5owKd1yZ1JkBs5h01-GU_XK9snHCWbl6k3oT3pgiUeIemZRpm0SIhM78hOrNwyJfqatPOgRKxUjzB6zYbRxkMJwZL0L35GSuFOwuLyCv2UausT14KfGPtz7_FeIdjMcWnOhJqZ6RFOLDzvVEekXDOzOaQD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swAnTshBY9aG5iJxMo26OpeK6EbSImAPLc5SWVQ228gtZt_pKd63bhsIDa3rQ7-70qip2KpEnpdicufb5Fam3Jfp3O8ugSMTqGUbQm66ecuDTU57D0E1PWPcs12kZFmFXdJ5TTvuJttktOfjLAtaj7Zjzp-YbmFdYy6YH6yfXlkncdhU-KEanIvXiRkyUH3UotOLm61VK9ZzUHcAsrLSDsh-Vl8tRA_xncXvZUSEe-3VmeXk1Re7FPFMgGSIs3QWHVhHM1zoBurwOsOilDRSP7PtJS2hRPjZRC8ZOjIO_7CE2hjuuq-3i_bxGaiDlVbiHz9lHJSaG1F3kB2rpTj3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNtJIvhWINdGsrUQhv_SKASHGZHKkWzC6MxdiPbCSpSyyP6eFcxL4PBDK9JnZHfhsVDYhUMGE1CQ-OENqpdCigTLDyxgTtz-nxle3HTCnIs8z_hsu1YBAvYMw-iyoaAvX_3TKAtQKRhQwDjMLJBPHWFGXbcnoyPqaexUvEov86szT9ECZMtrGBt5k07llRhVNmpivUumrG78Li_kRa1QOwB-3heb36fCjpY8qXqsUoiHxntZzViRnE3bduKUy4WRAnBZqehQAf0qan2EQdsPOePn3eG8uLvae6onEzDdlx7QGonwoNZrEAltnRD2YYl7kbFATFuBYzpL3Rf_lL5Djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pstHfJCarzZ0cx_vyLpQ-zYxkbQwLOR1Hib6ZavqGOhton58H8yQxwKZHe1YqaUUXLOnv8-lMFD3d0_YpgHFVMUPPBYPsFT-OoXWoMYspAr9jJj3RX5YfGAV9_TxpKrJhQ6AmCri7HRvW_EzvNgiueTyvoCYkVEsNkMaUZFXUXp2AYyN2dUeKtfHRHdFUOC9nqqIBLfuOq9Q-FpNsBo41a_57fZJeXkYq-wplRU0Ug9gt8BJ5N0fgR5kutAxYBei8xVVbZUOrSZ5ASf-ZCfMQxLQ4pr-BpoDcz2sOkZg3yJbcK_YzLtSkVyBJxL22NscYmm8rtcU7H_-NTQ8E-NaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPVFcAsoxRrKGIA04lONOzNYNGZ_gf4t75hRXYLrfXm-EhbhLTJEWVBdhl-WvLYdH4--Q9JFZ-MQA_JpPFaahNqSRWDuPdAQ5t1cuaExXgx7YNXZstfzE18XIYHEvMv6CnACo7_Fhg2SXBxO0cCPsj9H3Xqlys-albFpQb1ND3x2BwDAvS-idt4hvzgnuMF-ach3hBJWqgbnCTC-PY7_tHUU0ThGO4k0FAqrswQ-bfzHKTjN76fYFFkTjqoGlkT8B88O19dF3uaf42dQrVhihN-3OHu_JNUD9Jb6o8CNEyyir3auzxOe1mvg49W4JDUBn0_-auypAFgEp4Os5P50CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll0QIbi-1CjDWRHVdAtB6azq5SCG_1tA5rEhunTkdEAXHugUgU5P24lGeYmsueEGoDMljBg_8ZGcfG_scELscrKNI8kR06iJHzyNHmxq2-oyCrlB4DQ_10uPINqzRvP-br-5a-wHbPK11ecgk-GmxjxMiIADrKdwQNzfqrZxLYIS5Q1RQn9bbkjeqXe9KdsGU8hsnKrCw_qNYj5-5FVDy6cxYEHSx8YyC1JQxBHeoc0GhPjy9DwJMQ6iv27AaIFWAEte0QMUVLstimzUXAQtxVSDkHB1_7OMxX9IGOPLxL0GqjOpa_euqCDsLIrdkNS7Oiigxs1qntjNYM3Q2Kg4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=SRPAHJaUo_Q4cAAQ_PlxEZUZOxkGoYBhFFiS7N-IX-Ji7Gpqy_EOWYhkfocn4Fr__LTt218LcUjbYLakFgKd-tpMoy_DYAWs4mt9Yj1EJZt8zpQZThnISKdeut6pBF65cdl02t723rX7be1kkI7ZHgLPL-8RybzN632COP0_ezQlOMOTHgdjnqsqWn06LRWMS1fT1edqVOWq8_E3xzke_jXroDgt0_eu8s_1rz5LdYXyv44UnvIYlzZLDYPtZHSxSEVtlDOfQGRsn3w-bSwxGf7C9pFwy6VVzo4YO_-iUcUWe-ncVjvk9WQWlUbfbEdVixajvmsnOSirhIuyoUygaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=SRPAHJaUo_Q4cAAQ_PlxEZUZOxkGoYBhFFiS7N-IX-Ji7Gpqy_EOWYhkfocn4Fr__LTt218LcUjbYLakFgKd-tpMoy_DYAWs4mt9Yj1EJZt8zpQZThnISKdeut6pBF65cdl02t723rX7be1kkI7ZHgLPL-8RybzN632COP0_ezQlOMOTHgdjnqsqWn06LRWMS1fT1edqVOWq8_E3xzke_jXroDgt0_eu8s_1rz5LdYXyv44UnvIYlzZLDYPtZHSxSEVtlDOfQGRsn3w-bSwxGf7C9pFwy6VVzo4YO_-iUcUWe-ncVjvk9WQWlUbfbEdVixajvmsnOSirhIuyoUygaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOsld0kc-78s98IOigpFDK2QTNB-knAfJ01hxDJ2rU3a2DpwtP8lm5hvVP3r6psZx8zkqsccS2ku8l_yCrCd-SDHPXKIFp3MW_N_2HZT4sgdq-2KjGv0z4PXSBgryywD0Wsw8HIWK4qDmZKL8XRQ_-dBvdx8Uz1XKUCa4P9zNj8qnag7ptFPoMhd83vBHLH3ZjV7QNty7_T2IjiD0fOHK6QIeFyKj_fWI3teXC0JGK4HK05wOztGp0uDZnmI59yYjEqbPJB7dJIxtcHvbu4gjitp3YLFGZqtLNMsy__h3rZxf1v5xfXsIY8HD5nYzw-1-AF6jC6Afj3_qdzHKIljaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrzwiLvW0vxQLxHIk7wmClipSZCOruGpr9cBq0xi08hNPY0537r5F4ee9hETse5dpRQsbW0H0JBbRxCKGxfaBelE1sz5RcmGnxqpa6gMiUSQn111lSwv4kZYUh3noy_rLvFVNcjNlU3hiYDC8hYkQWqX09gy_7PK3A16i2c9hhBRpQH0k2Zx5KTt3hRHec5JiLKIS7DjFOryQ1l95KmTOiEEB-hv3QJ1z6Rg8VzP-l8cVVHYIcgMIoy9a9RPmheATIaQW7Ndnb-onKOAsVXIxP5xJr90Rhs1SOKv-lVsHMxKcM7AdMCTxsnSGydRjYyQtAnmhWxao6Luja2tk2-fJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=T9gqnu5AISEZeXP8dYyJw7hIhd8s_sxxsS2WaLryJWD0W_J5EZFXPyFSJUBt02V38tOFufTO3UNyK8ncJwThRv-vLMqsCefttfdZOrJPX_2cDzZrad1S_jhkjsmTskwPZ63Lnmu_eNd8lKez6TJoiuXuN9rCa13hUB3RKh-k1HPU6rd7t8B9bqfOF2UOBKSuBUAjdFmhfzxlCaYWv_-f0LvVE4DZGhlVJxXbW9krKomqHobYuDFNoFJ3Xv6POzkOna8qrnkNBjGSVyDOtXzTsiaWC0qnJbwwscBB7S-KYk-hxaS8fuJpaUiBPoZk37Twnf_7i2kKaANAcKgS81BgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=T9gqnu5AISEZeXP8dYyJw7hIhd8s_sxxsS2WaLryJWD0W_J5EZFXPyFSJUBt02V38tOFufTO3UNyK8ncJwThRv-vLMqsCefttfdZOrJPX_2cDzZrad1S_jhkjsmTskwPZ63Lnmu_eNd8lKez6TJoiuXuN9rCa13hUB3RKh-k1HPU6rd7t8B9bqfOF2UOBKSuBUAjdFmhfzxlCaYWv_-f0LvVE4DZGhlVJxXbW9krKomqHobYuDFNoFJ3Xv6POzkOna8qrnkNBjGSVyDOtXzTsiaWC0qnJbwwscBB7S-KYk-hxaS8fuJpaUiBPoZk37Twnf_7i2kKaANAcKgS81BgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEmYCuU0QAgGLhWtgaKL18e54G-zKZRgWsa2UsP0UUZNmvMWO5VUS3diBxc774NqripwXWsWEURLTuFsSUcY_8fxUmWGpPK4lKypCTYkUGU9prnaZDFau0sqVWRVR3HUVaCcZIvL3TjYgaVX-5pVoOPxn7v4c5R3vBtcMbovK2pV-6etO2L1OJYz756m5GQddmd57evnYED_7N7cJBfA7m8Duup0T1wVxKqeCNjarl4WsPU36PfSFx_nxKwn4Cd6ROLfiver9BgisxMvBltCZJL8_2UxgVKl7ZMsmXXAR52QlZYKAnwbCHpZ0tQntzJSbDavSVF1yl5XuDrsnML8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkHXk6nLz3MPzuEY0oOrpUIVTjCD2WCRd97ugYWSu6-JcuXYhGK9Qqhgi8882Lm_J3nv9zfSh3Mjws1MejlguCqGSrUqpvFdkvV8TBZpf1sDCg85Y6LW67pLdNgKqPZxx6qtUaSXQMQvNFXJNqwN8Ap2kkhz-vIcgbo1OtSSZiV59j9o9LtqPYSd-Qz0rIkuEF6nLjEorVpeYPSgygXIu6-f3j33e-hpTdwNhBhs9GlbiW046JUReX7XMSkhviG6s0qSwxGP9t32SPSn03JRtO8vXAe6u36MVTOMlC6Lu9vnRlVpoLiFg_7HCKq5LcijjY0GI5mR8UFl-ZsEhg0u-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=tfV-R00zuhCE8Yn6QHLDKsdSSqvnIN7UWsiKzwf4YXUHZ_ul_1ZpJ3iMlyD_Wnp3d74pX7PH-KztNerrWHJ3qcFQk_VxkNou132qpgti5V_n5BKogd0ISPkhaw_FS_S3YNQE6mD7ggztmaeVo0zg7b6kR-vG4hKl_u5lQISC4J9pRtNkwTukzKmk7HnehGovgpLStKRI4CA_TqT5-S1RjuWY_whMUsl7Dfo3QkM_XXmE2GiQ1Bmv2HiWOyLEf62FGsx8VSQIUlF3w5L7am8np1zC5Vviui-tiTafdsAtuklHqifjPQ8lm51P22KJjqBSdPlsc-s9OO3AwkvkNILqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=tfV-R00zuhCE8Yn6QHLDKsdSSqvnIN7UWsiKzwf4YXUHZ_ul_1ZpJ3iMlyD_Wnp3d74pX7PH-KztNerrWHJ3qcFQk_VxkNou132qpgti5V_n5BKogd0ISPkhaw_FS_S3YNQE6mD7ggztmaeVo0zg7b6kR-vG4hKl_u5lQISC4J9pRtNkwTukzKmk7HnehGovgpLStKRI4CA_TqT5-S1RjuWY_whMUsl7Dfo3QkM_XXmE2GiQ1Bmv2HiWOyLEf62FGsx8VSQIUlF3w5L7am8np1zC5Vviui-tiTafdsAtuklHqifjPQ8lm51P22KJjqBSdPlsc-s9OO3AwkvkNILqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NhNz4RAPVIvt2H6NqLgZt8-I8q47vSs0U9npxiajE_muN8F7HNrNGXruZruESznXPTVpNsbxrOys0xhnaQutvazVw5dviI4ZzHFU7XkkiQL-Uwtnmp-s1MAdJmg6wQT7MFYqpsOQlElOW1JtmkphNZJ1iLmq3oe-gKxKRbTVSZZZULSbi5TtaLX7T0KBnIbrINunbXbNquToGbUeTlJf5g3ZlirrNMPfT2n2mr8qgOXo_V1pHZPxcvUu6xrpUuLJRBKjrnRICoIEzDtzG1Gsw6fyqvUg6iF_n5sX86iOeANicfIWpHtXfjHn0-1HHdFvxz5KgM2x9S3vkc0Op1zf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hk02ta-YbBcAcO1hwKfzVJkZ2KmX_r05sa5Ua_tDzRyJgLTk5-vhGNHfahxk_N71nFx67GIvNSuGHgDA9Vb2GbRYPNa-regHItmlCWlgE_RZ4vM3XZrNhObYDjq0UDGXYbkE-loQf53u3Pb0u44RidN6Ngv2SpG_xVRC8a1ZtoC4rFWdlobiGqBkIGLDRqIMreZoetLXeqbgypsKjTDTMlW-xDjP76WSuO5kl1UJNFhJI5E9Drqew8bwQ3-qtIaYFhjU65L0zOWz8pCm7Ei6O_8bpKn351kMOA8wPDIP3HZJ3Daht1k1TgtNiwDDqWCeNYgJDlb11csu_aTopMLbAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=ZeB5SEnwsyT6E7HClc0oIFr6hEhqf4HNdojEFfcIDPb0gT_BYTjq611tWTrcvJ-qN9Yhb3sM_nyEBiJifY2WN36I4TYgr1Iq9iOaY5QgdyY0ZUTsWXgGBCHy_zAcZhw9fes-n1Dd4i6onzjbEj18pDNqXwbNTQmyby-0z2-GMd7Xx6bQOLbxOzyg3G6yrQvIHx3BbbXQ0hdFoV7KJfSrwtU8f961KPCTSVHcDBhPq_PUlXfz1dOIMKblpd81GThudKSRqwQvcm38b3uo--zXSX9nhQfWEZzrh-7gJZ_Ph4BfZyGGJvayOUrE1Y_LhQ7vY20XWnKKMYTqbQvtc4tkqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=ZeB5SEnwsyT6E7HClc0oIFr6hEhqf4HNdojEFfcIDPb0gT_BYTjq611tWTrcvJ-qN9Yhb3sM_nyEBiJifY2WN36I4TYgr1Iq9iOaY5QgdyY0ZUTsWXgGBCHy_zAcZhw9fes-n1Dd4i6onzjbEj18pDNqXwbNTQmyby-0z2-GMd7Xx6bQOLbxOzyg3G6yrQvIHx3BbbXQ0hdFoV7KJfSrwtU8f961KPCTSVHcDBhPq_PUlXfz1dOIMKblpd81GThudKSRqwQvcm38b3uo--zXSX9nhQfWEZzrh-7gJZ_Ph4BfZyGGJvayOUrE1Y_LhQ7vY20XWnKKMYTqbQvtc4tkqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a66q44CvxGEXKbo4kjcmuOFVBzFeecrFKHmQ7oLtWh9hzZ9EoZGsveigNwVwk-1R4IXa0FcCYb9npb8BD-6L6BLI6UrFpns-ADMIEcjWS754pyeTCuqFll1ctZ0KwYEJZ3W11NRedLNH8lAYds0UEzKF53v4fS-3pcJ87Xz9QW1MjQczxzy_h3-k1in-RbN9b6E2Oq53ly9-0DFCMTkjSVJqL0Avpr61AT08ve9GTf9_otezsgNROvXziMRsftZ5zZ0aVVk7Bf5smYWTDnKqEl87e0y0LtF6ihKQAmXkchBMjxLO_zqE6Xuqc8RG-4v1r6m1Nu7HYFcA8MHaKqOdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIkVc2qArjYk0duzAWji4GUrDYkr9dH5X9aCJzOgISJswsHzzzPLI8s8GlNe5GPkdTB96ywDL2GysoPEru0swhtuVKKZUd4-P9hSj9hYRTrmMOPkXUnXFKAFbKxG_Kr3dZKyVVelLH7VLUl4dlNF2saiO2Y-w0cCpTKFF0W04cpL0nB8sc3uwlGoOInpDqF36eNF1LN64F46HE0WXRraqiA0a_vbTd79wM_dZDmf2I--5xazKeyDNXsz9JmBgLJdyu6BHkdCoS9T-mYURdzLLUdqyaomg8alp22psNyAQDnojBCb1Joxhb3wHw3r0cgqbQiaBhylQPTCJigGAITgGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWpLUA_8EYE4r_u0kr5wGNnu6WtSqMtT7AhvyadZu-TDI9YykJCnCrVncl8HAzIHCbCoXZcf3rQKnCezNQA43t6HlS7fi3gOstZUZUZnyC2grwkSFYu6GVFKh5fXhv-geDIb7UlZUXO9Ro-KdK2O1RDU-KJG0_NLa02zMrYeNNrGtb7Rto7Pcos2vuK3HDvwEjLN8QITD5nMZ-0p25w4oQwf99L-7QBhb0LWIKTl65VD-sTiaLgO5s0J69vdSdnpcswSY-gSB8VXEqm8yBJ_1XjVJCQrPla8KFa5QZSb9AcUnacxKR2ajBht5h9DaO38jqNNFM7Kbesj_46jwEduJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Axjy97t2Jqo3DmVTr7REMnlOa0kZRuPfn86iiPgibtQ5C1X9LdjFdWIBf5UF-HwtwxuaSTQ5gZ1bRPlADeNFG_0ai7jhG-kdW2ZbBVt2PFNY9wSuwWw2Hx8O3rm3WZQm2q_ATXmgtJ-mw6DJ4HOQbApyivBZ2ZcOupplsIbiDRq242wkj2sUlRNxcINPcgzRunD4QyhTCyFLJKbnWtgA5z0wUd5f3U-ZlfQ5yuiNQNJPkczlVVbGFXE8QUO9n2m2wkaOEGUyZNylz2ca1xR5z7PJRL-vUfXiUpwcf4o0j1MHvSLlnJ83UFBsjXBiFrfCriZA2Rw71ygFccD8ExI2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZCARGTdxUrlsGz0uGd2XUm4hvcKO_LDmNaZVYaTwoXCiPBB75k8bGnyrRvgoBLqQGGrYha4EKxbG_KmacHhzKoc_wkRC6O8EHmbxNBKjSl-8wAoqoewZLdMAsQrXRpGyM_6EQ7stGLQSunPiQwfAqFGK_SPeOiU2zjnjKtpsfPmbjNrPPr13g77MY5ewt_pupyWAct212B-ufhwnYkXhfRSDB8qjfX5nO_L74kqZLszcqtS2eBrme40aWrGIpcTef2Qp-WhUVWNk3iF7PNfe5wjCFT8M0w53EDE2xLDyLPQ7NsyPxZ2ITL8Mt2MjwsMrWTkHTB5wssr24gg0uI6jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJeqR1gwigv5bkh3CNSZs2d0j7hiwKsRh9cFNE4zmdewdtWrrCRKBDDF4Ee0IQIgGSUcHXt2KMdQE-9stn6xhgSkoY3PP41z3dgt6GYu-cK9tUTp9tQ-RMTOKHywUttdpHMvsWc87q7Q5WSTHCTTi0Cygn5W96f3TblxSFbdSMegLyyJvRVu2uALD5gMUsFIhnrmokkuXTBvk8kzF02EpgjQv6WuQSuDR7VKYu7qi-uKs2AFjHu1fONUhRx3BWWMpD-ILle3VUKOMwcqM8AEtgOcI7JZD6dyh8qMLUQ43nneu2BpNWdR62-QLn6ntsA96pJT9JbVOi8Ss1qW3DzoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8IiNRLz1V5KHTxaUU8W7y2Y0bsG5I582r_Uecldz2rvDT0AzPRsivwwVVUOe2Qtg6L75xTXdSI5gXXrwjIcykm6H8L-kXzWPgJStyVyG4D93TuDf9NqUeKPDZHGHOo9tnsHTRKG1LN7LeQECoAGjaWBzM4MXSaZB18vlog2SIfcAFFHB4cBirKHs9pPR841H76OO59EeqgMpQMaqBOcWSIRnDa5a97gcNsuAwxmGZ6qRM-YQf1ompNW90kd7i92elDOsTlj4qTY8T58EU5Ba0u8Co5Dowkf-ZjiqNZw2DTXSWTC4oKpYowvXmsvIo8FkXN7yo0AM37G-_ycVf1ggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0bdzEEzSJTN9dTGLfg4QsWIktTcrvSgM9GSsYdsAi1O1V-3mH8eH6uPEsKcySh0VtYDg5INhW-MGyYkUKAcaIkPUdnMgTzMi8qrmCeiw9dSfHFQjgGe6NqvqK97dkYx58D6VO9ckxOeGyzPcMSSv0hnDQ2JwmPkrueIixCFw2W9ibA1ObzjWVnR_Axu_p5vNBklJEZF9qIropDO5bd3LX_TsqXspT4AS14t8vfh1T9kjXNJXnxmLmmBr7DfLxeVZAAtMUoK0QR9wuVOyQQ6gvrDccKUu6PFfw6IpFmR__EjbzEDJ8iaUj9oio7j6dEd_4ylwtDKRrsyqiLkgPA_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=mFIwriBrk2unmlsSynonLorFad5KYCS3auxXuFl3WQqnKsaLIhRtb2JxmSl6-vORsjczz6SvJzT7z9uSBKep5xwo_BuCdjhp4czJIj_HZAcWh5qBuPPa2Ov8SWtfub2VQtGn1S_QxSIAYMXGNQNacilDjxi67YwJ_oPHQvsKv-CaXPJNFR8d333_yRpiwVWxig4iEOxkOyWfA5erUQlNd7MVVG4ZKxDG6RnBkIOZYHkBWbOV27-aoQpPvPYKgw_xrgmO-B7c3S39-YFsOO2Sout3FL2Wluhph50kgVUnOEqJKCq7b6IN6iREWnBAuWxt6JEbmIm2pZypxIXmfc6pYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=mFIwriBrk2unmlsSynonLorFad5KYCS3auxXuFl3WQqnKsaLIhRtb2JxmSl6-vORsjczz6SvJzT7z9uSBKep5xwo_BuCdjhp4czJIj_HZAcWh5qBuPPa2Ov8SWtfub2VQtGn1S_QxSIAYMXGNQNacilDjxi67YwJ_oPHQvsKv-CaXPJNFR8d333_yRpiwVWxig4iEOxkOyWfA5erUQlNd7MVVG4ZKxDG6RnBkIOZYHkBWbOV27-aoQpPvPYKgw_xrgmO-B7c3S39-YFsOO2Sout3FL2Wluhph50kgVUnOEqJKCq7b6IN6iREWnBAuWxt6JEbmIm2pZypxIXmfc6pYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPEziWynOlRLfoR01M6ynZNzL5RlLY_1PLDU_db9AVz8s05XdbytHIu1wv2kyd-ZwyUt-zO6RXFsfjmNaH-auFR46UB58arlQzwoNoaGhx8XNPCkyzhx6eG81Ju21u6E2maEBlBBTrT41WUNAg0P0iA0hk3Dwrff_QY_q9x3CzNSbX1e-QEXfWdny8m_89VkqST5kmqIMO_akV8JatvNVQqRpov1GTAdK55_pWua7UaRvrtwlOzrMq1yRzc_bM-HJlWNRfY-ipK0MDchH9FtoTmosFa_ynjIxKZxLIRUAFJSQu-9sMOfHdf5QD6dhUu_RDoU35mu1enxT9lcEuxgYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=ry5PT34PNCtKkzuWunqBlVK4ncxUc4EUa0bO0Mj7T2IhmT903VOGMItlYA6ba9pNEr1iyYk79X7AX-I9cqp0hygE-M1xS88qbVaS8S3mGkw-9zp1Zc1sI0oOk0QWeJdZ-j4IathnX_DVapFjv5gxlVv_Uf4KKGO91vSO18VWwec2L90sqfC6rAq_cZSohEwos1qxEKMeSO2D8jOWxZvlETpp2TvQr5QaRx9juuDabPG79UKSI427z9iuLmBqHo3-zwjUCgpqzsoZcggB_CNyRIptQxMsPIyP6uUJh0Tsw-9BeRP67NpuBsdsel3EoO1WNGEPym2WYh6QtvU5ioLcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=ry5PT34PNCtKkzuWunqBlVK4ncxUc4EUa0bO0Mj7T2IhmT903VOGMItlYA6ba9pNEr1iyYk79X7AX-I9cqp0hygE-M1xS88qbVaS8S3mGkw-9zp1Zc1sI0oOk0QWeJdZ-j4IathnX_DVapFjv5gxlVv_Uf4KKGO91vSO18VWwec2L90sqfC6rAq_cZSohEwos1qxEKMeSO2D8jOWxZvlETpp2TvQr5QaRx9juuDabPG79UKSI427z9iuLmBqHo3-zwjUCgpqzsoZcggB_CNyRIptQxMsPIyP6uUJh0Tsw-9BeRP67NpuBsdsel3EoO1WNGEPym2WYh6QtvU5ioLcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=Q3KaNQKngxt3vTN69iRsSghSQQYSGBXuY-DlwMUknQkg6v29GgREMsRCRknO_oE12QzO4zwHnZ7f4xrf1QUbJeqY-77zjT-ClOHMtnKM0lS9glLw_9GJ2Z9cy0fFpd5hT2d5R3qbodXnIKpAKC6P423xECbYLNca-aylv0E33eIciGTRt4O5FnYGz2eSD7EIOR-KC-vo7SBT1iXCaYsOz0HEvnCJb_-dGSG4c0VZdfNRTXtcQk0xNwYaOGzlY1ep-xllpF8fM6zV18slG1jOFuCp3Q1uCj-u5SmeSlzYUO_eoMeWFbeTV6pKwd0whdqCPXAAq7061DePWB3eIW6dQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=Q3KaNQKngxt3vTN69iRsSghSQQYSGBXuY-DlwMUknQkg6v29GgREMsRCRknO_oE12QzO4zwHnZ7f4xrf1QUbJeqY-77zjT-ClOHMtnKM0lS9glLw_9GJ2Z9cy0fFpd5hT2d5R3qbodXnIKpAKC6P423xECbYLNca-aylv0E33eIciGTRt4O5FnYGz2eSD7EIOR-KC-vo7SBT1iXCaYsOz0HEvnCJb_-dGSG4c0VZdfNRTXtcQk0xNwYaOGzlY1ep-xllpF8fM6zV18slG1jOFuCp3Q1uCj-u5SmeSlzYUO_eoMeWFbeTV6pKwd0whdqCPXAAq7061DePWB3eIW6dQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=ezhiTEoK7yTAUP9hMCkwT7T9Whmgu5Sawyi8qyj3wMrqiJHa7_dz26W5AX5omJyqlbk5e_Rm44rZdRvId7AyICBqLB_cSMWNvHqrgUN1Vw5sy5_VlUWyw-aGrkGf15GTUi9IlUNt7U8dWJBE96SRVRDxtkRMb2Nj2AztliBNMr9UDJ2hLTB8eYPnmkx3zN6cYs_XuoSMhLl3pG5ZUxqMpbVDaQvq5niyvCat6dzNEGyHTHnr00cEgZn_6oSRYTRh57OpjWQbwu52CZ49WVXM909lX9SWdMg31u678yinGFyWrhGHN-asdZriHyecfH1XWax7fXipJRY_xeqtD7OgEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=ezhiTEoK7yTAUP9hMCkwT7T9Whmgu5Sawyi8qyj3wMrqiJHa7_dz26W5AX5omJyqlbk5e_Rm44rZdRvId7AyICBqLB_cSMWNvHqrgUN1Vw5sy5_VlUWyw-aGrkGf15GTUi9IlUNt7U8dWJBE96SRVRDxtkRMb2Nj2AztliBNMr9UDJ2hLTB8eYPnmkx3zN6cYs_XuoSMhLl3pG5ZUxqMpbVDaQvq5niyvCat6dzNEGyHTHnr00cEgZn_6oSRYTRh57OpjWQbwu52CZ49WVXM909lX9SWdMg31u678yinGFyWrhGHN-asdZriHyecfH1XWax7fXipJRY_xeqtD7OgEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dq8F7suO6OeHivzcjbkm3T7xh9LwIbjYpbzCUZtcu_zuAPXAn2N9Lia7e174DA6uTTl3s1vmcEfuntcRrlQ4hAiBb36z5TJngAtD-6EBgiImGW8E1QYP_t1hq4IRrvz0wzQn5udsOUL7YlTyYFB73EhyUnkMDFgC-acmVm9pvjXm3Nn6QzkLMteEzjCRGaOj59wcGC0Cd4ifHKEX7WGD4SM9MLUhzfN83LE4a8QFCw169aQhxkWk-9CwwX7L-EJ_ANH9rhNS__5ttCYGebv0DUUV1DA53BIYTU0G6kJHeG_44-TbNDC6m2bVT8LrPkFSFO624_ZYMKjlgvadwBvCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roqz1GxWgqedGumX7PK1ciHgqOdGdn23-aS9bo_za1-XWcyYRowei_zmnDj2Vce-FvNlrjUpes33ZUzI_BcvO7KR53o17eoGdCxf7qwaARzdJubA_FPkDkkUyIIROwc99sYFY-V_ev1tGVO6nIqaYQq7YE46-HuS1efy1stCs8hOcl75xoZDSCQFQkMxG8j3ZKWNUDAhzf3lpesi4bqniPGgQyPdhsudVnjsfwyH7X2bJBJJB3iXJBGG75YDcGsUVUaUz8-6Kn9z-91SxdkKTlShvixhUUbJ7iw0WIcMsB5zX-_KGw_SwY9H8aypXycrSGVqXei5E2ls-dHFK5WZdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=G7_C_IV_cxCZNmQvp6xNd8KkkAw8SPatoJ35p3EBb4gtvXZR4tANF-YV-hrz_8XIKRtNthqP7XrFJAgplDRO7zgiXnPoPckYAEvOuBbQnWGwbGCPRxHpJvS9SsYqOPPyFh1hYXK_kqOGnXs_8IhaPpP3ML9ATWiTqjCqKUv9G1BKsT9R_cY5IZSjDrMPpPuY563pIgkYvTNKuDudUZhR0SE9G1i4XvYqBQefTtHTH_gSlRup_Hp-af0qT2Cf4TK-FnGvW52vD_KbAqKECjvzMh9gdtf365okJ7u-xgh3CezqmXOry1I1wgsglICl80AHAEFek3aYiCKsTlTFc14Q9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=G7_C_IV_cxCZNmQvp6xNd8KkkAw8SPatoJ35p3EBb4gtvXZR4tANF-YV-hrz_8XIKRtNthqP7XrFJAgplDRO7zgiXnPoPckYAEvOuBbQnWGwbGCPRxHpJvS9SsYqOPPyFh1hYXK_kqOGnXs_8IhaPpP3ML9ATWiTqjCqKUv9G1BKsT9R_cY5IZSjDrMPpPuY563pIgkYvTNKuDudUZhR0SE9G1i4XvYqBQefTtHTH_gSlRup_Hp-af0qT2Cf4TK-FnGvW52vD_KbAqKECjvzMh9gdtf365okJ7u-xgh3CezqmXOry1I1wgsglICl80AHAEFek3aYiCKsTlTFc14Q9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=TstTZpKsE0tNdsvvWTAQFL2BCTT9Jt_WCvv7oMPV2qpnLorokzBim1nVXqCmA84omw0HRhqhGP_m78YvVomh_jiWqs0503P0zxOXR8vMwpLmELhDj81izOrbPh23LWKlIUK7U0Hv1Zy7xAC468LN6Cag7hfpLKQvCS_bded0TsVcni5scLwiQ5n0zhcFKsLcHD8egjVmk7cDY1x6ukuZFNto7wbpRLAPksc5krd0WlP8QB8Axzgq_gTtott0bMWljVxwot7iDVleYg2i_t-DeO5moHQcVoQ0BMp76W1EyzCWx3of3yT_lRqOu1IZDdBvUnrGedmctWTXLxjh8s_XeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=TstTZpKsE0tNdsvvWTAQFL2BCTT9Jt_WCvv7oMPV2qpnLorokzBim1nVXqCmA84omw0HRhqhGP_m78YvVomh_jiWqs0503P0zxOXR8vMwpLmELhDj81izOrbPh23LWKlIUK7U0Hv1Zy7xAC468LN6Cag7hfpLKQvCS_bded0TsVcni5scLwiQ5n0zhcFKsLcHD8egjVmk7cDY1x6ukuZFNto7wbpRLAPksc5krd0WlP8QB8Axzgq_gTtott0bMWljVxwot7iDVleYg2i_t-DeO5moHQcVoQ0BMp76W1EyzCWx3of3yT_lRqOu1IZDdBvUnrGedmctWTXLxjh8s_XeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rkib9lSjGGYehxKemceFJGvRrTbaTg3aJUg_enJUC4xeg4hiWOhtXwY1fVmMMwMQVolRa4TQtihAq0FYb56FlmFBJ3FqUDhGw5wV6cWX1qXcXyaJXWTSbIEfMzwEMNonWwCKszXPv-fnju6Eo1V0LauBNvFQvD5sxcEsnTiLqMOYUvXbBf-PgkTUJlNkTMZlvGk4AzkvPwEL1BTKQ8fu7nRZz2ijHUXIfvs722Nk1Jjms0gVNxhISF2fJFIl2Z1FEcjcVX9oT_oYdekavqNRwykpQ9r5NCrPUblEHswk-q3eufBcC7jVjodPcGEBxgW2ZA1ytR-0zw4W5CqEaT3XeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=NFX-w4zphx6DqzLkKjTKy-o660GlcI5PIHgvtn-moz1SwqULHj796MUemFVe1WsUgD9QL-GPXXJRlsxRhMswJzETXjUnP-W_REB8UKk8YQ_B5Y6Ss2vCHrX7G0CNFvlztaRV0gKK95IPBD9IGCuVL8gXj0eFG7clPucCOgwe0D17xdCy8i_I24SXmTFDPYcVgffilNgUiPVWuOdCjybCGaj0KFjrE3QU0kasCNtmrIktnaGhKBOpFwKlFWB1swD5fYM5FBV9DvJn8UOPsi4of-Qk3wmeNpWwijpp_8qrvZBfgqrn7dSTzreZlj1wJ_O5GdGCZRnP0X-iV9b8crjIIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=NFX-w4zphx6DqzLkKjTKy-o660GlcI5PIHgvtn-moz1SwqULHj796MUemFVe1WsUgD9QL-GPXXJRlsxRhMswJzETXjUnP-W_REB8UKk8YQ_B5Y6Ss2vCHrX7G0CNFvlztaRV0gKK95IPBD9IGCuVL8gXj0eFG7clPucCOgwe0D17xdCy8i_I24SXmTFDPYcVgffilNgUiPVWuOdCjybCGaj0KFjrE3QU0kasCNtmrIktnaGhKBOpFwKlFWB1swD5fYM5FBV9DvJn8UOPsi4of-Qk3wmeNpWwijpp_8qrvZBfgqrn7dSTzreZlj1wJ_O5GdGCZRnP0X-iV9b8crjIIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK1Sr_dEkbZuF89MAKYL7_owhAOMpSY_eUzkcTi84ZoMOAzYLg8jsER6P-6yJlOoZMCiaZ92jnx64PlC7gEwPDRj53_YORF62lKqHm5VMmi82N-wn7OqcdADeIsqCl0dOHRTC2I3dUY7BF3SbQt1hkXnKbsdUZIHM5oNxZGMJQdCA_urN-bde4y_UX2PE_FEG8rtWjNUjm_mZsvLiE8505UdK7_JOy9pU5AIlYXxZ-Ceqs5iUz944vqBjDgis8y2rbfoRLvbwz6yc9IIIwf8SJTuNWKjtnmQ4cUU73FbNiRqxbIPj9z7pS74_OrGABbDRhsgOaV40FOUlt947CcB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhLstxKYtMnXfth3sn5IiOfSXlSPVr5xp7UkxoeYKDKCuRUnBekPlrbZl1lliOVSpHnEnCTkt3WUO13g1fWLQhRcnz0A7YbNVgpMazUuTvlj2P2w2-0twA_POMD1KSa5ZigWnwBujydCeYgrQ9DFVAuJxLDYgMH-17Gx-MNlssfUJlMclVIBh2Xz_FXQFiRTdS2neKWMaOZhWePZYeB7RpTNNxaEIkwgRLlxyhU-VMW0ZUhl0DL7wwUOZosZmOutFu6XcznukfVd_GjpM67MJ__s0Ebr7fmfVPYzO25y-OzaTZRcgiOsIPIhTP-autfytZvLXhXf1yXGu0787X28nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
