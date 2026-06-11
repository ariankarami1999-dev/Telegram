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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 00:43:33</div>
<hr>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OENnE6emzRs-rNh4mf9GKANY7T4xVIQqe5FSYR8mSKPIZvMWVRh8yst5GSfb6WyRAxW2I2zpJ4FZVJprAbfbGTD1LTgsEdoScAm1fFd67jAnAhkJwB_N27rQEn1T-DhcVEpwQHnNDkPDfWTMZEt1vGiNOr4FApRPIXuSK_7fsMo3rUVKzD9r91vQhrbsTpOW8g1-Hve0m3p_HUk7w18TLDqvwHW8fwE4Uxb6jt6HPp8-0Rlnju_GNvqEj1mliyeHqV3Wnl8SxNYBO0g2EzCs3WiduYTXQkmkQV9XmfGNL9rovFuogf4CGgKR_p9DJ6e8HSKgSPueVEkZJjpt-MGvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN5qa2K1Q6afAndskOz-9D4lLeFXOpKbeVnEbrnwtPxdWesdYsfUudAK8g51eXLnozGLrJIOieK_S1iuDXQ_dmajZSl2G6KFKIxD8BwgdskxuUAKeBP0yGCu3p_YrhK7_CSgHodEp7fretDtU4NFw5ui3W2oNohM9Uff4wZ1yr1rZ1dF0iy2wriNK5dcOuviaZoj7ky7N0-H2FUaVJRQhrt0QwsgJYYxrEg5sWx8RkBXOTpiNqAqiqebAi11i3vbpZl_RIc2ZG7QO8qH2iyX5bYj__OnNCCLoiu1r1PkEXsq7oMDLVaT-iXRC8wfwmC7JxRJzw7IKbslWPSnUyR_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtqSdSKpRFXwIWDMeR44L08-OgDfkD67WHOXuBtp3VvZ1cclyiC-YpOB_8-RUZpPCqPxTq3n3EqTl-1K7QXkVW_ge_kFiaW6qFjnFVZCAg8_Xe6ZjHpZAU4WyzZJa6wgIQwepjxEUceT3AEUbLS8T6aTKB_7KrQmdLxepS3LAwES2qvtkyuK15DQgdNU4M9RR7ONiIn480x7htYYLEb1quUv21MnQ1EAUoX49Ar32CGF0pYSed1zJRkMsqRQiGmAVGP6g7yyMa5S5AdHQqkBXTw5hRlyd1NRXB2eJUB3T5mqOqIqgUC8K63Ewba-tBehuUEiAdbdjGgwjsmJWdy3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csaBlTeHN3QgQ5LkyNMWUzsPUduhfrqUGAWZ0fUWY8pzzcN1H1LwY8hxjDvj7cd8kGUUG1aAKKUZlp2oKzQae7tRYGsBacTTXfnKPQ7OBg-qO4b7hy9tVnnwh5MT3Kd-Cx-3Vdp1Ded5Cu-lUDK4EkcBAmfauxUfaz0o1jnWHiFPIOK5Sw6H3OruxaTeCIEUqVhdhiqKdO1TuPTqv0GLbJ9FOM5Z-D9UTcFoQFADvUD5zUXH0_Kp6iNxrgm7FksBzmuSAGa2HEeV2OJhiSUOYxemKeNq_mjzRrDeBRI6leapX6XaXDpUybymbgZsChi4ksg0YoRxJN79mAzabK-4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMy6zA__ZvBA7D4_Gi8JrNrlrffDkTLOvoBV8Hr2VubfJuX1JQUOuMoLZIciDn65cb9glH-IopiXuaDaOvzcnPMRWo8dUYeNhY3ms-UVKMQQRJcHlWYBuYtssoixdG5dqkenCqWwvUQS2Q6mHD4FqtE_2ioVQZ_vUCsizFgxDBLEAWOsAutgciNGnOTTisPNLo1dE_OEc8Su1CQ5nXBSjiYXIQguVXTCyZeSVUn4up9x7bsIj11-7dFxH1UYeusaeHnQ27UcXgVNcXaXpNBJohlnqNzmm5HFM-0_O6RiExgWY5sLWJTaGxcduQR-9zkGCJZWDKpZonEeMu3A5Xa0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6fRAXIJKZv4KooSKMnjVYJEX2ecRRAgiTDqDqgz2hrrnnbYvPeORkoARUQpiPZq1vGEtgEUhW3ZfJtGNUcy0xA_r5ftFgWIEE2snb3IniYN34LsdSl6uQCugk_1xNZq_ia-9ppSfL_X0cNyyX63eIEHr7w5MD_3-IdybrW81UZysUXPFM_50S5YqvdOxE1QhD9duXh6a9ecweaTXlewTh8krw6d78SHxsvPocVeRNTI8ZzBc7lzjQqyDTMqgHJCx21L4TX_ekoPCHP1a6dIDiXYzQE1vD-SV3Ax65G1vXVAuiP9-CTRCy2qeQra4et65ZUkNdUVeeOhBYwmpRTE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWJpKke1M0ayZ9SG6XpGV5bSrdWmurMYikEgQXXU-NY2NUp9Wt6puwlWeenravvWWhFyINa0CSbjeTzk_oXp8QzetHFhClWbesYQ1DoZtdvafiurHg5TN7fwjcXdckrSN--z_Mg6y0hVZ-C2k5AOkuwMCW_SPP6JNpHgnmcWayIhqP9V0kObh5iZ-KUQL4CQy4QIOXX1_-xDAUI-i3hbwV23nBLg_OrXVwXFIJCXDsh0bXVGsOqKOOBGP-dXuEW3DgFpxUti_WXHtq50lWgTiwTrRDmXdZOWcorGkqcsdY4crn_FkkEKR_wcPPQzh7r7nPBL20vq0QSiAdOi_Xh0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwJUS3rgbRl0_I74l74ypcXx-EabgK6kDf1M7H03MV0trmeI8oSlGgfkA2n4ucoafICObvHqpJoqCtqV0uTAA0hF1HRCPQyRjeFB_Tuo3AL5mUr6J8Gj6MImb0pGKpSD3Wbo3ytqJCR91FCSFB3HXPq8Bb_5crQd7r-c4yjMZSS_e6GuKD6DBJW25yMXWvZGVZSwD9W_2W-4950yncuDO0L6LnfdWRhUfQ7VlVZJIH2kanVOs7tSkbjyOh6XZ58Mlso3h8ioEA8u3LBjkYnuQOtZ8aLSSRccmUTvHu2gTCbG5FuEjLuQAfZ5DQBMOwbAhAt0_TGFeYnT8dRuoTtuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vArpnyOoUeIPlwRedpoItCqXtYnthsafw4Tw5P3QlJzemeVOKSSt6REMFAQfUVdNXQM5jvP2h3J0wm94JwNMIf1rdOBnZu0SVGacCz8aSgaq7ZGCi01X7tSbwLebxOoFQs5UPVtysdZBZGoQbq8CZf8VyknJk8zUrP5tjgdlgvD6MWkPKunU8wN_OikxbFVMoYrQTouSZ8J7O42B_rFFfX51AgKIZkBKepRJ3edZ_YJZuYBdxzRWN1LT0y4680c3uYGNi3RIRW-r6j-K9apuMeZhz3Jq8kOvwJTK2Muh01IT4wRmtxUs4pHacAiE2Tq4G-ByGzvL7_T4o2qbYhj6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k01NvdKCYox4IjJdvTyjq4F6NpLJU_R2avk8vV6sfbxMd4I6hrP7eZ2GIW4S5azgoBv2tffd4FcY7XtP0cf8zbx8IKwb7JsIy9g03byrPSxtacVGo6ThpDGuV2yVDHDabBUsTZ5PGlSNcS7HSKA19Sg1xmCih1dmqHkC7EAVJn6L_Q956H9tUYQYOe4yL4INKzwUN7IFAu38ppDtM1TleRUDOLrTKgpId9uY-yaE-thhv6VH8Y-Mqa3G8hCIucTWxI-rJo7PvccGkIebSz0gN9kfJwTbY1DVWHXQW9r4PnFt7Gtm6G15wiw9TnVHOnXeFCwLW5wKpOHtQuG1sGjekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdtvBM6xIjm97nL-sdNaUgNANFlvDuHDuuxA0_YR7PT-BUP1q56UDKRd1F6lO6K1bYvrMvaqbczNsQPfYTQAJBo-Cpwa7skR50uOV_ciTK-IysCjpSWT80M8qiVdeaBWais3qFiWahcHtXSTqvnjPlkSv85-aqig-QAfE-9KFrwxaHc_zVlPR4K7lmxI42mPXMNlEJxAxNH-gL1ofd3cTXyXtpdMFCFq1kUdBXxl8L8NKK6Ny99t2Q5K0LpUNo4AdsAp_OPMJg4Da_9I4ilNpP5-TEQiNt1MtfFpsDOlBxsPZknCMgi4OaoTtVRQ8xgsIKNiVAZ4JU3eBL88QW0tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxGYjH0h8AT50brXCb7aA9ivLPJgt2-geNmFeQHG3DSnni-Q4xM8qWz9tgmr8OHkpE-kzxEBIIM1BsztowtT6oPwnI0uAw56E4lMMEFkQmnFDq1ERc8uKNlqBn8RqUys57vGf_ALDbvj5ietNVDWBdg_1KuxDA6sJ2_DvfO5CQG5QzdoBOlCJYelrL5owKd1yZ1JkBs5h01-GU_XK9snHCWbl6k3oT3pgiUeIemZRpm0SIhM78hOrNwyJfqatPOgRKxUjzB6zYbRxkMJwZL0L35GSuFOwuLyCv2UausT14KfGPtz7_FeIdjMcWnOhJqZ6RFOLDzvVEekXDOzOaQD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swAnTshBY9aG5iJxMo26OpeK6EbSImAPLc5SWVQ228gtZt_pKd63bhsIDa3rQ7-70qip2KpEnpdicufb5Fam3Jfp3O8ugSMTqGUbQm66ecuDTU57D0E1PWPcs12kZFmFXdJ5TTvuJttktOfjLAtaj7Zjzp-YbmFdYy6YH6yfXlkncdhU-KEanIvXiRkyUH3UotOLm61VK9ZzUHcAsrLSDsh-Vl8tRA_xncXvZUSEe-3VmeXk1Re7FPFMgGSIs3QWHVhHM1zoBurwOsOilDRSP7PtJS2hRPjZRC8ZOjIO_7CE2hjuuq-3i_bxGaiDlVbiHz9lHJSaG1F3kB2rpTj3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYhnVnyNkdQKEUx4YUJrQHgBwt9TiN8BRGjsxQQbpyTsUW8CZjNsEuAlumM3al8aea0LvCF3qjvInOlcJ71dPbJyyPgrfsyqGcmctMelcw5nYcGlUxZfsNsIiwiXbCzK2Qz3do7LvpxF9uWN-qj1hnZLi44LBK9Sh08fhk04EOhia9ql9amDwqPsd3MlO-DT0pjiNwJzWyAFrviIvs4vyXYm311Co_HUqUnrz6HF_Ib9EETP629mh3GqLZ7nyzTYCQ64gXN_nDIJ9zmEh5uf01rm36i0OlzPhsDWxZHHTsHifLctekaRbcfpw1HBpxc836EOkOSCFHVjnOjDq_uNsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pstHfJCarzZ0cx_vyLpQ-zYxkbQwLOR1Hib6ZavqGOhton58H8yQxwKZHe1YqaUUXLOnv8-lMFD3d0_YpgHFVMUPPBYPsFT-OoXWoMYspAr9jJj3RX5YfGAV9_TxpKrJhQ6AmCri7HRvW_EzvNgiueTyvoCYkVEsNkMaUZFXUXp2AYyN2dUeKtfHRHdFUOC9nqqIBLfuOq9Q-FpNsBo41a_57fZJeXkYq-wplRU0Ug9gt8BJ5N0fgR5kutAxYBei8xVVbZUOrSZ5ASf-ZCfMQxLQ4pr-BpoDcz2sOkZg3yJbcK_YzLtSkVyBJxL22NscYmm8rtcU7H_-NTQ8E-NaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPVFcAsoxRrKGIA04lONOzNYNGZ_gf4t75hRXYLrfXm-EhbhLTJEWVBdhl-WvLYdH4--Q9JFZ-MQA_JpPFaahNqSRWDuPdAQ5t1cuaExXgx7YNXZstfzE18XIYHEvMv6CnACo7_Fhg2SXBxO0cCPsj9H3Xqlys-albFpQb1ND3x2BwDAvS-idt4hvzgnuMF-ach3hBJWqgbnCTC-PY7_tHUU0ThGO4k0FAqrswQ-bfzHKTjN76fYFFkTjqoGlkT8B88O19dF3uaf42dQrVhihN-3OHu_JNUD9Jb6o8CNEyyir3auzxOe1mvg49W4JDUBn0_-auypAFgEp4Os5P50CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll0QIbi-1CjDWRHVdAtB6azq5SCG_1tA5rEhunTkdEAXHugUgU5P24lGeYmsueEGoDMljBg_8ZGcfG_scELscrKNI8kR06iJHzyNHmxq2-oyCrlB4DQ_10uPINqzRvP-br-5a-wHbPK11ecgk-GmxjxMiIADrKdwQNzfqrZxLYIS5Q1RQn9bbkjeqXe9KdsGU8hsnKrCw_qNYj5-5FVDy6cxYEHSx8YyC1JQxBHeoc0GhPjy9DwJMQ6iv27AaIFWAEte0QMUVLstimzUXAQtxVSDkHB1_7OMxX9IGOPLxL0GqjOpa_euqCDsLIrdkNS7Oiigxs1qntjNYM3Q2Kg4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=NQyczxOwYxXfvXkvPHXkji6jc4WoBujGuLVzPix5rtuqAUZOeV0PmjSuOFjhO2NGCLkXr9bcQlOD_j6dC8dk1KlBzvitbkVuN9wWvFcC0tvD_x1GKB-XUPtj6wRGP4iklfuSKL7LsQk7gs3LmzTq5GTCV0PiMgxjZyNkgL_Ltns9x35wi5zFc2XJ6DpDXkIg4gWcZTV3huzLCjyd864M_4oXsssgUjsKcv3acDaAJ_tVYnYJv0iB-cwuB4ZrRu2IcdMAYGFED_9lDRp5QavZSi0wE-i3gjtKIKAfjgspz9khw3XhiMQP8Bll9lNLq02OGCeZ_f72kIHgHoQ3Hd0Ylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=NQyczxOwYxXfvXkvPHXkji6jc4WoBujGuLVzPix5rtuqAUZOeV0PmjSuOFjhO2NGCLkXr9bcQlOD_j6dC8dk1KlBzvitbkVuN9wWvFcC0tvD_x1GKB-XUPtj6wRGP4iklfuSKL7LsQk7gs3LmzTq5GTCV0PiMgxjZyNkgL_Ltns9x35wi5zFc2XJ6DpDXkIg4gWcZTV3huzLCjyd864M_4oXsssgUjsKcv3acDaAJ_tVYnYJv0iB-cwuB4ZrRu2IcdMAYGFED_9lDRp5QavZSi0wE-i3gjtKIKAfjgspz9khw3XhiMQP8Bll9lNLq02OGCeZ_f72kIHgHoQ3Hd0Ylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJwBEX1Xd49nQIsTo0Ypo8c_GaT5nD7NFCqVL5SXREZdqXd4x3prVeum65XQFh4J1RaWMYUiOrxHuzHqPHuaewfMhPUh0vy77jzi2awaexMuTzKQlSg_YznH-y9VhvqU33OICffZNCa5eV9NOh8AJADuqA10Hx8f4j06J8MaKjBEVajjfT57E1bBhlZgzLR1mbumUJAWpakBuP9H_E7NDX3-dOUPoNtuWuas7pmB2rjBT3VaMSyAnidrgl3VieIAiAbKNk8Etu_DlRf76iPAqV1-C9DifNd7idvu_0uLDCEAuBTh8CSFQHRHpGofxEl7CCOJWD0HR4pAZwIQbNPw3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6MDrgcm1Lbqj2E3rE6Jls8ICW-FujwB0DSNQ9ttkwLI7uTW-AjgYJB98KxgsJIUay31MjUnkGmcFDQDK5c2lZXM8iXSCtEh0bzpJNiy6Yv1LRjCll0xaR7MvNMSkNszgN6g0SBzruOvWPT0Q7dzfLnnH59Zi1HJi1Np2otDatXChk9_7FJorQ_1qnHOc27pFNEUDCCq0YT34GJ30vkbrQ4c_DoICSR8OsehxaU6szPF52qCs8NnUUCvIIephFzCEv8W2GgrAgLiH1hDc6fFyQquFtyTZhmPrnSkYQfyf35hI5wpCJntoJWvdHJqVE7sxV0AR3z1asg_J9O13a9-ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=BHVDnjfWKHGc8kQ8Wake2BiTuaXOubv9_L74ZSecZnMUU09S0bMHOXGtJpAJg59ZkxDo7idDBkXlvu_utJ46Pwf_XGbl7d5F5Ng1KrjgipMZByIZ8ElguL5vok1uyAmTVjjnwUahU3Rkr3q0p9gFdg80NmbUFs1JEP1Hw3sRpG2nyo8hUY3mOGbc36rKvHhjXudNxUURch98lERWjKuXWF_0VTfduY6d2j4XNTRrLwI_odzDHuL-APNUYn86hdcm4QsshcRKyfsSuCz_yavKIYFeuVqxIoIGgyzW5jHkNdMgZBl0U800tpxU22fO3jMbQz1_9cILI6dErJk8KWVeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=BHVDnjfWKHGc8kQ8Wake2BiTuaXOubv9_L74ZSecZnMUU09S0bMHOXGtJpAJg59ZkxDo7idDBkXlvu_utJ46Pwf_XGbl7d5F5Ng1KrjgipMZByIZ8ElguL5vok1uyAmTVjjnwUahU3Rkr3q0p9gFdg80NmbUFs1JEP1Hw3sRpG2nyo8hUY3mOGbc36rKvHhjXudNxUURch98lERWjKuXWF_0VTfduY6d2j4XNTRrLwI_odzDHuL-APNUYn86hdcm4QsshcRKyfsSuCz_yavKIYFeuVqxIoIGgyzW5jHkNdMgZBl0U800tpxU22fO3jMbQz1_9cILI6dErJk8KWVeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9Dq7iOXllPwDdxCXiKz7eJ9GIk05liVkLGucc6s1Y1RBuxQSMhgCDBq0qwHeERn2V-N-6zyKo157TZ79aM9ku31TVYVsWRd3CM3v52S6w6SjA1Z-poQ4wEhJBtHbrgLU6_nNfRXDBZgx0BFAVrBd-jZ9L0_dMsodftKi_wtlsuKk_xR9Z5SsepS0g6zJo6j6cQApGho1qqGySzRL5-93iDCA1QsNTZQ5a7cXkv1WP61qSBygcebmCiG47-sqrDjacD4wgf8dHE5q6ZmQQ2KWHMsTV7gKn3SWU6alunkRzsc-pUjRTLwbSOO5Y1Jr4iKhWL6ps4uZTePeTXj5jkUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2ACNWDu-R03MwNNFuchmYjjiny9v_EQhIxPVKds3vYPp2T3TqLePCCPsaqWSbubkAEgTmAB1pEWya3zE49R-vhT9a01VSLR6bw47Y5_S1k6jfoEjGZdFqazVLJPT16BUUHVwNAiKgM3JjYvwRLUWLDPwJdLw4GddjMhDU_KLf4ZqAEkCBS1O8C4Gq4SKO5IFe_OC5ZAC3a-YIwC2l4O6gQSosqIl1X3o5sord09z84c21CAFvtQOneR09wVM4IMB6OdpmKkCcfi2HSfk0y_aidVruNAVhLxVjuV0dAKjOl1fIJceSRhWQoffONcz2A9Yh4uNybXITQRTZQZLmBK0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=TrL25qUYaFw0NkM1hczvonvbJr3uUcgda9aE12zRohbCGZj6LOVuDQm2I8nCvytysLwd8KzBxdCNxZ7Nqsf7IJCz1nkcSpM2z9JlTexrUi1B3nxBIZlCelxLpsd_FdcvkkTEuOTfooZup933tPpmTv9r-XoGfFcumQEH83cUKEhOvsK6reU46PKLwZV5Q1rsPCZ2Hf_-f8FQSpP1ikwfIwAIF5-DFaNPIAsTRACRhh1oP3R5xZSv_iNFIQUreAi1OII8qHhiSVuLKkGpB1CAvf20AqWDR7D2e3tMq43tO1sPYqr8HK5K_3sRVU_Aw85EucAHMaeUXY6FiNxu_jK2eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=TrL25qUYaFw0NkM1hczvonvbJr3uUcgda9aE12zRohbCGZj6LOVuDQm2I8nCvytysLwd8KzBxdCNxZ7Nqsf7IJCz1nkcSpM2z9JlTexrUi1B3nxBIZlCelxLpsd_FdcvkkTEuOTfooZup933tPpmTv9r-XoGfFcumQEH83cUKEhOvsK6reU46PKLwZV5Q1rsPCZ2Hf_-f8FQSpP1ikwfIwAIF5-DFaNPIAsTRACRhh1oP3R5xZSv_iNFIQUreAi1OII8qHhiSVuLKkGpB1CAvf20AqWDR7D2e3tMq43tO1sPYqr8HK5K_3sRVU_Aw85EucAHMaeUXY6FiNxu_jK2eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtZkbEuKDUMlty1V_DD_2mhKUxoh9Rf3LzwHRr66kGYOTFXz0EM-Ehx5PeGT0e9dBaAlaU59QCvDLWbElpgBL6JjDLb2OmWhoQcFsiPHNIPLNtU-xeUbe_ik00rpBIZ59oflrqrP9Hby3u72FNVGbS7ObnQDpQTu9rYE5nl_PB_PugDdAmKj-wryxaxAWJq0vaf1KM0Z8ymmyxxpX1ss3iqr9f1YQm1hH-0fjn7lXNvOI8LZcoliOwGIHcTw253Jebbfsw8_zZBdb9mZmxf2RtX3a9PS2B1Rt8NQ7H7KXjQew0xkr7CPSnE8CsK8qr171w38MgS-36pwm92tqhNe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqqNXKgnO0uh71gTkSM2uq2f0R-u129jO5KeAU1Xuh_HHt97QjVqIhZi0zxl-uuJ_izCuW-WrUQ8_95mjqd-vXVjTPraW3wESXBc82hlCzt1mdff7Npipr3YpK8TDvhPDWe1kNrqoXnmtOqFSHw3SDenOW4S4QQ3Gkw1pXI6Ia2-jqu1UykMGst3j5TgTljM6P2KLIo_3z_HyFkvED4ZUMbIX0JTaIu2kBqAtavF12V8EeMfzHr6FNeEYOKqTbf4SlogiEqogzYjDBJhSeQ8aHIK1GeztUOy7mEW3EVKFFGZi4SM6NOPlk9CXpojpV1E0FDy09uH-j9PDrKFMlJYow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=GA6u0Oe4yiY-Z7fXJjSpKIM8fIhXi0gy2WGRVRr0Cd57MJIi3aeS9uKV1j0B2DXsYlOjeZwya4DF84C0ThWaVwaF5DwK7DEgMt4aM0PiDRa0QeGH8Aa_BV2xPPRv0fBdaZsKU-1qMrmoFpmlrDCO7z_wbLNZozzes9QTlsj-UPkRG2W0yegxFGvEI5N6vUQGHDpj4D6GT0CrxFJSbKQ9qXvLPtrQn3JFw97HQF6TXWd44OkRtj-k_fnTEvVNHLQ4_I-79_sLKf4trBScoj8-Ugy966cD00U5E8v7AAKFBTcvgyWAnmTH_fOn1wAJFcUkp584diFQPVayFi1k59_OXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=GA6u0Oe4yiY-Z7fXJjSpKIM8fIhXi0gy2WGRVRr0Cd57MJIi3aeS9uKV1j0B2DXsYlOjeZwya4DF84C0ThWaVwaF5DwK7DEgMt4aM0PiDRa0QeGH8Aa_BV2xPPRv0fBdaZsKU-1qMrmoFpmlrDCO7z_wbLNZozzes9QTlsj-UPkRG2W0yegxFGvEI5N6vUQGHDpj4D6GT0CrxFJSbKQ9qXvLPtrQn3JFw97HQF6TXWd44OkRtj-k_fnTEvVNHLQ4_I-79_sLKf4trBScoj8-Ugy966cD00U5E8v7AAKFBTcvgyWAnmTH_fOn1wAJFcUkp584diFQPVayFi1k59_OXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrzFkqPXpz2u4FCav0J1SzRSDdYEQoHlwBJ5Nf55hbFrEocjA9mhQIWl0EkVM36OVCu2ZktT4xyJtPgFszBtVOUhk1FtXMKIX1ihcn2kP7kW_hgVc4qCRirJqn3oovd6U6_L_5J0uqRmCrE4unzwP0cYHvba_LhtCRZrHpw78udXzinRz5HGtZ-0I-baXW072XbhTxWzopOPNZptQSo9MpgKEkVERLiIuCTWZcyPXl1rqC7gZ-5PENqMi_ZLlPyol34T05_7u5TA2LtrJrON3qOR5PMjNTE6jQLoZheR-nzlG_iyVLXnx0ww6jlkfeGO3eykvBJrKlvnzn5jNQkdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nhev0P23AOlb9Ntt4m1ZgW6B6QEJs99KuQEwvzcY76go1SREOERHsQ-S85MRBT5nMTF0cfnNOW8VIfUpFKRITGjBTlSwD9QHKq5My_KC9VKJb6n9LdkBR9K-Eg6yoLycdccku6mALc34b8H9LGzYDcobD-7Y4eUXJCgGt-2vTbjQa9uVdgcFk4VWQtYgvI6r9DwcM92ksisBTnWuB_6a1AMkqx3ZKrdnV3nFLvEON9qKDG-joPziyq8FxGRNYpkQXX5H06t1kajj2lv3ZkZGWb3c7AoLO5RonWjNhfokXMAxL6DDND17KwYm0P57OSEUOEbkpig0rIu7gmIukfa54A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmCgcK6rYFJt4GHxsVOANh5PzBJ65_mYS280JzTaN-5csJ8CqSgC3gtMubjB29w3qveo6QwnfSSYQ244OG-e6oKhWLH1YVCbQ_PTPWRUMXqEENW2QmDBwhZk6wyX14Ofs8W5AgbY7yrMjppiysE3Vea-zHf6oQxLLxnFHdUz-Yq0vEqnEJAzywvHUXIFnF2tf1qlAhzlRV4BRQhyp5A2Qmo8uBunIw2T7MVDJVQUYMKBB7-k-9mChwkFH2i9mOJTWnfvYPO9UQIddbMIUHT5Q_vgBpgQOQrhLlpbZCMvhDl1QlgyaroVJR98GJQ2WNLatlFn_tmHQv5KuY4F0aFXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbrmRyrFOQHeL38Q2Mu3Tt5sRvH2ZqdBgPBnM01VLdcCz1Sw5eC9gKRgmXXXZs82THhzuQA1tfcFzm7jRQiC8CtVykIfBnx2j8hgERm0_K4nQEqOL5zBqrqMEiGZT8vyV-epnlWAkluko-OMiX4KQIudoSa-l8-Z0abjRzywRbQjrR1f7P8zOeCyUvnuhEVhA3_9FX6auq_9Q5wR-vsAIdu4Dk_bOQVdjMyJpaa8-BpGzVFSgfHUHuHyDgiv-bcSLN7t9NwvXogksJGs_-feCdYKh6XJ7wOn6lG-_GzguN2AnMwEX0COMYgs_RRlwbpx-IlB8Q-QH2n0kkS3YY-b5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFdxqGbwILzgVsZkEEgH5tJ3gqufvkBRIPFooFO6pRbLiIrr8w4WCzaoYsthhNLyknMyCcL6nDEMShv4--t0fvdiqzTBc9pGUTZAYOUeXPu-nPXhirpBNAIfraV-O8vuqwgJTb3frUpFPeq96fePVGww_YM7wg07BWXXe44lP-4N19G_L1pwZUSkl-MzH6ZP_FbQkXvtFztJr8KaF8bhoM9WsTVcDIcdnhHYHxc_2HkG9nVUYXrGGOTnV1mE5fPPf8BSjxT-qLJhuQTVZPobPnmAefT2HjhIjPORntaU2N0wHFxiYErwecCNerOPysZ3uQDQSLNvSV2SoXVSGS6Krw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZPoNBevCZk6Nu8TcN0YEerJgvtv0IC9R6rg-NjkGz07v6vYVsd2hwplMInaXFpQmZZxAFfBcD-R2qSY2T37qWzSu15MHb9HDI8j-tWg5paR9vkvtOdWeKnM-9Al0hkBCVl3NvumRiKXa33O4a0fryFDMV91Gc8DAxA5NwvRH_VICXoSuVYZU7DIxFY0X_qk9rT5lPwFfCINWtO1VziAizP6ocCVwD2yqWUe6BAoEv0v-5qSyR1_B1vU2TaiP4Ea4KBLihH0ZyAtB_arlSUV3SjlhfdYxswSxnzkbT1DOWQT1p9Ki9TDrMya726a_wOpzJvka-VU0do6L0e_UWQkjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjXQI1hIvdqGUJhnGqmr4nBYPOj_cBsWqFNpjvurpnZpr9JA9dzKRV6qNTgR2Kspmm22Y9R9AQVxxDvSKW-UmMl1HgoyU4CrcGFAZXZDniKaPWvFTcXn7i_hxJbNnK9quFE4MZALfJCTx5SIgAL7sRfz97vzbzPP1sdBKe4gi1vhhUSu_WlrDd0zS4xyF7oD9sF8g6S_19ZWfhizo6xYzja5KK0UGAX7cYDtrc2mFrIqmKS2QJYeKglgyCWs_K8WdCRClowJUsgYGFATcCSgN4pozlowuZLCSg11awCdKF6GU1e54nMUfgiqWtjLA_X7FR-PSGh8sOo7wFJfTehmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob4EwT7q66kTu4vIzrGAKQm8aln3ac5LZJG0A6X8OqrDgvUQ8wNs2jl3ddtACxeQPS-s8zIp3_FtmWUvY0umTAB6r9bH6_m7IlTjCGumiGRIVe2AtPKgmM2J7_XBOJTRyOZW8FTq1OvosNx5MztTg3XLVxOx76B2yM4hP2nK_pGCEtak6kuROh5cy3a_WbJsRbOJm325dUVdqPQ41qoI1o1o4YgBs0uYzPe5y3Rmf4VeU2wk6HNsAggb4kZX2pnXPltnVo6qjLDH1MeUE3dVd1MEgCJrXFOt-nu3mlwzzGEe8jmSHOWaHeEE6r6aF3qYWlyT3tvL60rPmjXrhK7AkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=uoajegCrJZNBha8pPP6Afj4r8AJQX-9mxUisJ14neq0asLGdKRGfh1FzG0FAEbjaLbHk4vX2yrpoX5AD0ZlWd45NTHvUfDKQ0KxtBzEcOt5aDeZEv6WpO5_Qn8zg6aI0l2NjqAqD-hf3oc9V1_-0TGdQbFP-a6J7FT04peFPOdjkQYlg7BD-pCn3_pA0TwRhic9psV3NWKDe1JZVgZ5tgZU2wQh2xNDC5dazkjNkCUMBuBAJWfYipOEqnSfBvZJfXX4zidiN_ZFrJoV3xliqWp0JT61rf4JikE-OfC2ucoQqeOy8EN7gyiVTbGDqruQWYqlTHxYjDwMdbOsHtZk9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=uoajegCrJZNBha8pPP6Afj4r8AJQX-9mxUisJ14neq0asLGdKRGfh1FzG0FAEbjaLbHk4vX2yrpoX5AD0ZlWd45NTHvUfDKQ0KxtBzEcOt5aDeZEv6WpO5_Qn8zg6aI0l2NjqAqD-hf3oc9V1_-0TGdQbFP-a6J7FT04peFPOdjkQYlg7BD-pCn3_pA0TwRhic9psV3NWKDe1JZVgZ5tgZU2wQh2xNDC5dazkjNkCUMBuBAJWfYipOEqnSfBvZJfXX4zidiN_ZFrJoV3xliqWp0JT61rf4JikE-OfC2ucoQqeOy8EN7gyiVTbGDqruQWYqlTHxYjDwMdbOsHtZk9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_Rrdg1-CI-w9wicZdO0s9x1f3JY_IGGCZVbXS8G-DPVys2aNw9yn8L4ckrb1Ggj60GCG-iIGhGWYfM7lo84yZ7Ku3X20llVyrMyIIqC8Q7v9mztS2GzORVBuKzWgV4OytZgUgCWjHEOlv3aAjY9ed-XP56G8Iiu4xqfDi2sGgen9TD-szvj31Cl9l6v8xJ06-7S_y7zqR-KztJlD014ODTfuVdxUnJHwXD4oUhva6lhDSL40cecwOx53qseJ_WQjKhNCMUAH0HUTKxEgnjaWizmuSRRXyVJU9UQWdTllzOGqWM1jXSPrL9Ec_P6UPVbCuwFTD_6jdNc7j17tegJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=LU1WUiJLHA0O5JWcf82FA9WPsxc41JzcsUn19dGOLm9sKmdDBeIwtYHTKt9zTrgaUgLGR7ECuDmta5zEqJDNq4Vab5atczaOowUer88sMq8giNOPrn1K1IgjRKogIBFN5Em81GIAC8dB7hVKjBXStNVA6Xu_iyTcsKp3l05tIn58NIaHVHqDgpNXgxqMY9_58VcVff9ywdQ1VtmorJQgtpQQZJI0u8xq7eru34hWWo0TLGmFACYoj1g_8FgSraIf2ra9KLjQw_xBdBYy0wprQs-OAknX14fFtLuIveyYoEsdNiWXGwtWQdXG_3_OawrImfXk6-Dh5sfH1st-k05Jfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=LU1WUiJLHA0O5JWcf82FA9WPsxc41JzcsUn19dGOLm9sKmdDBeIwtYHTKt9zTrgaUgLGR7ECuDmta5zEqJDNq4Vab5atczaOowUer88sMq8giNOPrn1K1IgjRKogIBFN5Em81GIAC8dB7hVKjBXStNVA6Xu_iyTcsKp3l05tIn58NIaHVHqDgpNXgxqMY9_58VcVff9ywdQ1VtmorJQgtpQQZJI0u8xq7eru34hWWo0TLGmFACYoj1g_8FgSraIf2ra9KLjQw_xBdBYy0wprQs-OAknX14fFtLuIveyYoEsdNiWXGwtWQdXG_3_OawrImfXk6-Dh5sfH1st-k05Jfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=NPDyrngQtE7JPRP7zGk42m8tV60SvHGOna5n53SK_GyNzMCC23MdEJWfCR7DHc-uGNeuQBZ2nVJrWbQJ03DhTwdZsnIAQ36IUYHXzyCsUvUmjBBG1nzGwnR-bMalEdu_DeboQ6Vw8WcVCWuUblJY-QaSDf8esR5sfzJmt7mnOnmoD054Lo3CgUxM12WUnIshLupfz8klTs-zLxYVVTCDpYHSxFM26l3lu8TSWbGasYojPv8fe--sSteKvNiHGHoNc2uw3kVewaCpE1gC-bYXCF-VUwi7rRSbCbpv45CTTh8TWHBiBjabBCxqsnqjHt6M9u--tHEB9UzVc-8j4e0z5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=NPDyrngQtE7JPRP7zGk42m8tV60SvHGOna5n53SK_GyNzMCC23MdEJWfCR7DHc-uGNeuQBZ2nVJrWbQJ03DhTwdZsnIAQ36IUYHXzyCsUvUmjBBG1nzGwnR-bMalEdu_DeboQ6Vw8WcVCWuUblJY-QaSDf8esR5sfzJmt7mnOnmoD054Lo3CgUxM12WUnIshLupfz8klTs-zLxYVVTCDpYHSxFM26l3lu8TSWbGasYojPv8fe--sSteKvNiHGHoNc2uw3kVewaCpE1gC-bYXCF-VUwi7rRSbCbpv45CTTh8TWHBiBjabBCxqsnqjHt6M9u--tHEB9UzVc-8j4e0z5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=A7BOx49_j5BKe_LHPPpmejKjD3y-KieFo8ic8pET9DihWKGXqIcQu6moOvcb5gyLRjvI2jNi5pCrY8iyNsWnDFFUlM8OL18h4Cx5MG1aHm1kwC9P_1mTL4MupSpQAdOxhRLsOyHG-a4qcQ_KnGvuEX9dOTAwUU31cKjqzNj45Qaddb-A_KtMF8pvoK1AQHWcqb1yGb6vQyJpVfQdGZ8mmcasGwgB9h8bCDwxq2Sl9laurUGCYohdFE7RWLQZ7gbIrwg4bTk8qKnqJpBUjlnRXMnjy_5l2fIHv0zEYiFdvniL7hCLgPafsHIbHZcVpPKIQ4Dw2uoaYT4XV_S5VLzuJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=A7BOx49_j5BKe_LHPPpmejKjD3y-KieFo8ic8pET9DihWKGXqIcQu6moOvcb5gyLRjvI2jNi5pCrY8iyNsWnDFFUlM8OL18h4Cx5MG1aHm1kwC9P_1mTL4MupSpQAdOxhRLsOyHG-a4qcQ_KnGvuEX9dOTAwUU31cKjqzNj45Qaddb-A_KtMF8pvoK1AQHWcqb1yGb6vQyJpVfQdGZ8mmcasGwgB9h8bCDwxq2Sl9laurUGCYohdFE7RWLQZ7gbIrwg4bTk8qKnqJpBUjlnRXMnjy_5l2fIHv0zEYiFdvniL7hCLgPafsHIbHZcVpPKIQ4Dw2uoaYT4XV_S5VLzuJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQe6nQcxBw81--LR9LIAVJKy6je6bEWb8f1yp2P-ne4hGr1-4UAIuQRuLCjRRGVd8kIObRUf3bIZQyJldl_FQA2Gu3DHM01fSUgrK7K9nDNE_qiyUM9va5T-9Vp_8XtBYBP7kmocU7A5Ix1U-7bfgQLZy_3UOTJyQOtdnHBHl1dWb5IjEfXY-5w11vAQoRUxUMdc4_BVZftsg52G8ELJAnL75bOx1vvLluYGBKaWENngc_851SIH5kvqhJGWxQkki2fcsyMatyJ2GAmzv_7Js5EfJ076k-uK2ZJg6pqFeWdxzR5eYsVkUqJXmID2l5ehtrn5j45YbymJklY-BCJC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0kLivgDW8fKJ_PIwylKxnW6ls2hf5Ni1OKf8WrH4YKSdk4eyIp-2WludOZ8cRCxb7_Old91meoEMdrfb1fNwM3bt_LLBykO0JtyikP6OppxUYEYWNtP65KQzmRXLoeQtHSSaYmfBojsj6TpoZ-hAaEYESwaDn30LuKpq8Ezjttl84ui1JQhLJCtAnPtOXv7OMD9PT1AHyhEDEON6PnHKq9JZpY3sSzVd3wikp-AHjHXedjc7nLpj9oDhQP2PSloBSUiB4e16PPgWTPNngMVQELBlOTGS5-JPnXEUd9j4bmK9WnlA9RgFCZsgNlFlTHtI5zdt3RSTR6P5y3ypNaYPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=Ijthy79_W763Tc7cBPbyg6F9uJ9gf4NTR1UkMyirfAq393VBkk9Z9IAF8T7WKFMdcVLxq_tlqLcIHCmyG_X9v3FXLTKG-e-DwwEzD6TEqQlQCEQKH_sL8IcP0hBoSt9cOQ-O6WEgdMqdEFq6-CWPz4m_9sSuwxsk2G_B2ZB6t3VEk-lLozAeWD5bUhT0KVLPjXpeGuOo9HFtqHRojqLd3cFWm_1-kcPXQzUhdxnwDOvRf7-zWmCBb8bH5oS_5uDK8TrBK-xIwk6YN-3WZUIkbcpOMjoS-lgFmnF-XIn_dv2JutYwjdsnCmdSS26HyZocPUtEcRGmZ05Y2HMoisKabg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=Ijthy79_W763Tc7cBPbyg6F9uJ9gf4NTR1UkMyirfAq393VBkk9Z9IAF8T7WKFMdcVLxq_tlqLcIHCmyG_X9v3FXLTKG-e-DwwEzD6TEqQlQCEQKH_sL8IcP0hBoSt9cOQ-O6WEgdMqdEFq6-CWPz4m_9sSuwxsk2G_B2ZB6t3VEk-lLozAeWD5bUhT0KVLPjXpeGuOo9HFtqHRojqLd3cFWm_1-kcPXQzUhdxnwDOvRf7-zWmCBb8bH5oS_5uDK8TrBK-xIwk6YN-3WZUIkbcpOMjoS-lgFmnF-XIn_dv2JutYwjdsnCmdSS26HyZocPUtEcRGmZ05Y2HMoisKabg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=JG6bkfOVDisOQ6euUyC7hKomFwNswVL79zZhHrMrTUXOL5OmPH2J-K3UKxeF73ddiZea5BjgbPe0-hpK1cxTcezD27ApCQS9ZJ-VwbcCGp_kZ9TM3ZhuEBJ5FWC0Pueln_DbagJvpU3s8iBJsj08VRbzarBxGBRwZTjLnGuOAYJbT8kOkyM404RRTTvmg4UWzTcC9yPFfSweMZG8ncktYHMoOLKaTDyH-Zx8OZQcdDgylmCON36eEztJSpQK-bl4AocnHw5I5j9em-X4z7-wSrz08VUfK9ZPn3ul8ePM-B_-mHZH6GYTSxaaiv93NjX_kumXDkf6dP05UFQvh8FVMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=JG6bkfOVDisOQ6euUyC7hKomFwNswVL79zZhHrMrTUXOL5OmPH2J-K3UKxeF73ddiZea5BjgbPe0-hpK1cxTcezD27ApCQS9ZJ-VwbcCGp_kZ9TM3ZhuEBJ5FWC0Pueln_DbagJvpU3s8iBJsj08VRbzarBxGBRwZTjLnGuOAYJbT8kOkyM404RRTTvmg4UWzTcC9yPFfSweMZG8ncktYHMoOLKaTDyH-Zx8OZQcdDgylmCON36eEztJSpQK-bl4AocnHw5I5j9em-X4z7-wSrz08VUfK9ZPn3ul8ePM-B_-mHZH6GYTSxaaiv93NjX_kumXDkf6dP05UFQvh8FVMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDxAlinpQPKqZvMq78_0ceJ2HbEhxzsh06uppgpwJr3EHPTiKZt2zubqBnJThOhj-HL7NS1nzPK4QZ4KloQ8_cRIr9puQxlWmdrjwgXL0Oy9gn0dBJ9XXuBNgIxP7ytAw9DBpX0tj90RiX4BJbn_-aeeKWZv10DgXHM400ojpTXqiem7DIpegCfsOgcDHCsJFZSFMq9eAQiUuK__adsPnZWJuiJMUpAMqS7oGPWCb8yyedhgWuVgrtx0rRq7kKygCY1elrmu3bKNMnI4AfNQeJ5wrhIJwCXjP8WgN2oE6g6DceOBS4oVRY58TGJkg6cm-4-ssAAcbyCKZHcI8NwGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=Y08dRngXq-6txC2myPxMBJm0xpoCHGX6IHR9_0zF_zmbBS9t4_TnlQ1lGmNKuRyq0Y37XLEpKTBCSRf2av52FdRvtXlmT-jv9TWGPcw6xk7sC5phe3mQIAlPvH_S878L0DG6dqbZikmiYQb815m1gixq_GnTtUEm6VSYWUhopKSWX9RAVd0Lx71c4v0ynyYp_GK2jWdJzEg8SROJXpsyPOdQ_5R2FPjJt3yAuH2RKJ8ubsq8Cy5r8MJQhwQEpnO6pqU7F09nU0jBinGqqyDzIxRpKztkE7uBN9K1779KoBWjrEBafCqqlsSZz8xeGhsgk1FcYFYTkAGFWLikOxg7Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=Y08dRngXq-6txC2myPxMBJm0xpoCHGX6IHR9_0zF_zmbBS9t4_TnlQ1lGmNKuRyq0Y37XLEpKTBCSRf2av52FdRvtXlmT-jv9TWGPcw6xk7sC5phe3mQIAlPvH_S878L0DG6dqbZikmiYQb815m1gixq_GnTtUEm6VSYWUhopKSWX9RAVd0Lx71c4v0ynyYp_GK2jWdJzEg8SROJXpsyPOdQ_5R2FPjJt3yAuH2RKJ8ubsq8Cy5r8MJQhwQEpnO6pqU7F09nU0jBinGqqyDzIxRpKztkE7uBN9K1779KoBWjrEBafCqqlsSZz8xeGhsgk1FcYFYTkAGFWLikOxg7Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQO-rX-mbzX3TGPa2uFG7ZNfQmkZ25HpbXq3nhkRK6ZTrnIcRsPMPEUqK8Mp8MIf8Q-0cVxnHABb9fXLW9La2awQ4GJ-49d-LTULsIfmeBp6lvDkew6eCfmj6jFTx8WwArfG5H-RqqcHt_erPFG0eN0hPHjtYpwi08juzzDPmDPHMTyMx8GYFkKmyY-0eHH3nigkw71Io9YvKzXPHLaRKYfHxx5gkZUE7yuiMp8ng1XS3T3r4HBXDYhKewglR9YutaewGTs_pl6cLljEeM7byNBdr31sBVGCHnynXK5MBjjlbi16gmNoz74WxuYEiLRlXc3ZFOD9ydbB5EUYlT45mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCcCDN17MOAon7KvFMp2FjV20UJSh5yG99IwuJdSoX8eWIRvukjpV4oF2ON6BPAyV7Ph4YrAhjoxQX_gOh-NRq2ofHo5dXuCuEjPdqrKGr3pb50joLHT7x_lUbmX75it2zgIpCM9oniqVBHeZkhJvqUn7ThV_16PCXbzZL6Ih1CBVbEWJGGkroDnY_4E3Bhydht1jI92IZS4ViVHxu7ELNkTiZrux3TRZDxSps-1DtcQI64c3T_L1xNM1fRbojxZkOXd-LMCTvw6ikF_bfTge6NtiLhorI-R1WL-Ec-4-HTWk8sB13vy33E1sQGIZeZFTB33dNKwhNySkL0E9_JOlg.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
