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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 22:11:38</div>
<hr>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OENnE6emzRs-rNh4mf9GKANY7T4xVIQqe5FSYR8mSKPIZvMWVRh8yst5GSfb6WyRAxW2I2zpJ4FZVJprAbfbGTD1LTgsEdoScAm1fFd67jAnAhkJwB_N27rQEn1T-DhcVEpwQHnNDkPDfWTMZEt1vGiNOr4FApRPIXuSK_7fsMo3rUVKzD9r91vQhrbsTpOW8g1-Hve0m3p_HUk7w18TLDqvwHW8fwE4Uxb6jt6HPp8-0Rlnju_GNvqEj1mliyeHqV3Wnl8SxNYBO0g2EzCs3WiduYTXQkmkQV9XmfGNL9rovFuogf4CGgKR_p9DJ6e8HSKgSPueVEkZJjpt-MGvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN5qa2K1Q6afAndskOz-9D4lLeFXOpKbeVnEbrnwtPxdWesdYsfUudAK8g51eXLnozGLrJIOieK_S1iuDXQ_dmajZSl2G6KFKIxD8BwgdskxuUAKeBP0yGCu3p_YrhK7_CSgHodEp7fretDtU4NFw5ui3W2oNohM9Uff4wZ1yr1rZ1dF0iy2wriNK5dcOuviaZoj7ky7N0-H2FUaVJRQhrt0QwsgJYYxrEg5sWx8RkBXOTpiNqAqiqebAi11i3vbpZl_RIc2ZG7QO8qH2iyX5bYj__OnNCCLoiu1r1PkEXsq7oMDLVaT-iXRC8wfwmC7JxRJzw7IKbslWPSnUyR_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtqSdSKpRFXwIWDMeR44L08-OgDfkD67WHOXuBtp3VvZ1cclyiC-YpOB_8-RUZpPCqPxTq3n3EqTl-1K7QXkVW_ge_kFiaW6qFjnFVZCAg8_Xe6ZjHpZAU4WyzZJa6wgIQwepjxEUceT3AEUbLS8T6aTKB_7KrQmdLxepS3LAwES2qvtkyuK15DQgdNU4M9RR7ONiIn480x7htYYLEb1quUv21MnQ1EAUoX49Ar32CGF0pYSed1zJRkMsqRQiGmAVGP6g7yyMa5S5AdHQqkBXTw5hRlyd1NRXB2eJUB3T5mqOqIqgUC8K63Ewba-tBehuUEiAdbdjGgwjsmJWdy3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csaBlTeHN3QgQ5LkyNMWUzsPUduhfrqUGAWZ0fUWY8pzzcN1H1LwY8hxjDvj7cd8kGUUG1aAKKUZlp2oKzQae7tRYGsBacTTXfnKPQ7OBg-qO4b7hy9tVnnwh5MT3Kd-Cx-3Vdp1Ded5Cu-lUDK4EkcBAmfauxUfaz0o1jnWHiFPIOK5Sw6H3OruxaTeCIEUqVhdhiqKdO1TuPTqv0GLbJ9FOM5Z-D9UTcFoQFADvUD5zUXH0_Kp6iNxrgm7FksBzmuSAGa2HEeV2OJhiSUOYxemKeNq_mjzRrDeBRI6leapX6XaXDpUybymbgZsChi4ksg0YoRxJN79mAzabK-4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMy6zA__ZvBA7D4_Gi8JrNrlrffDkTLOvoBV8Hr2VubfJuX1JQUOuMoLZIciDn65cb9glH-IopiXuaDaOvzcnPMRWo8dUYeNhY3ms-UVKMQQRJcHlWYBuYtssoixdG5dqkenCqWwvUQS2Q6mHD4FqtE_2ioVQZ_vUCsizFgxDBLEAWOsAutgciNGnOTTisPNLo1dE_OEc8Su1CQ5nXBSjiYXIQguVXTCyZeSVUn4up9x7bsIj11-7dFxH1UYeusaeHnQ27UcXgVNcXaXpNBJohlnqNzmm5HFM-0_O6RiExgWY5sLWJTaGxcduQR-9zkGCJZWDKpZonEeMu3A5Xa0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6fRAXIJKZv4KooSKMnjVYJEX2ecRRAgiTDqDqgz2hrrnnbYvPeORkoARUQpiPZq1vGEtgEUhW3ZfJtGNUcy0xA_r5ftFgWIEE2snb3IniYN34LsdSl6uQCugk_1xNZq_ia-9ppSfL_X0cNyyX63eIEHr7w5MD_3-IdybrW81UZysUXPFM_50S5YqvdOxE1QhD9duXh6a9ecweaTXlewTh8krw6d78SHxsvPocVeRNTI8ZzBc7lzjQqyDTMqgHJCx21L4TX_ekoPCHP1a6dIDiXYzQE1vD-SV3Ax65G1vXVAuiP9-CTRCy2qeQra4et65ZUkNdUVeeOhBYwmpRTE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMi18clNUoQI1ROilnVuhi32ajlU8RgdgqhOEhHt60flc9ZY2wXQmZthYuNlr-hjsMq7BN5Q3gAIIwJxEWIeCS_Dl6ZQ9CeJBwoiEbBOLuP5rRA53oIwsG7Cd8-4fQKdB-lQMjln3EtnELnl4kQ5RHnYLPtQ3wDt_COloMFz32Iwu_4IIVv3mWr7o39k03U3IE2O-EeGhtT5oqhWuEA-JiNopo5QLopK9RaQ8-iXDzZSuk6NFy2C4iHUaD4zVqdiRpz45nfD90VL4m95ZZ2qAEorGMcnTzUtVrTjcVpmDVazcko0p0UH2CF-p-AYH8xLq7K69wnB7F9XrNpHr40DIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADmX6iy2saQtxdvvsqd3kWqS5sNsuVF0gZKmMCZODe4HJFbWL19Cd4_G-jI0TtpsrKpk-a_e7M0m1QKos0dbgu-aHVgGXujTtvZctEQLpAED9zB4RfLoE-tuS2IxBOQaGJtCraV1_qbUlAtBzjRW-NCR-rP8ZYQakKmHcuuxBxZk0TmI24e7y1Lsi7fFewNLufWr6q3IiTTni_KEAITXmzbOwmaey8P4vqJjDV6XDbd4MgZCjVNBTm-LCPO3BVfvSiTU0qvEyeCovxJ0H8Ik4JZ1ZLkn_bs2KW5qSCJqTgJM67g6rKBjePGW0hP70R3iu-_R7hT_h9raHogjNLYOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j99gftpphTHyhkJ9xPEhGIPwVC0jf9TJz4vpgFHdB19oMbse0KS57Tgn3LMR_kzuT1begK0CcZgmKvFs41FUCl2_yMjnrP8B7UXYYwtduRw8u0o2zHhwSRX9bTl-s97kuEeBRrTeMwrbJFY5I-vuIzEbsaNNy_t4HArigrw2YLZBVTiQSUqoYNY27TKv46lB9ExDH9_M2gCHvnMSUMJTMiqceCfNL-dzixu7k3OSDXgGdaPLWxlNlYtJZwhtFP3n7PC482FANbvHknDB1YuMakdmcSLvwzrSXVVEf8-sdmXxT1gTvOtCPLnYzQeEPMq_xakCZmGWssWsWkkSaqGcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVWVDK4IFhJt4f3UtGNui5EDuGQishNfTmZDjE4ItSaS4vKNI_2HD8U2ZBMTtspiYDdWiaFOsN_0zj_vKlhPrVUZSAM66mwDGrv2OwUYzPpTP6A83R271a86E6QsnsIjWGZ6XlKZ9bqn10tGXS0q0fpeQC7XJQ0D2OLUW64dnSwXp_GF6t4l4G1lfEUphuHCKghs5AMaKTUtllFbwyQc3Lb3hiHUHZ4PZIeH0HTVUzDpmwBZxhZBg6nzbK6WlCBNiuoiCkaG_fPVhzO3o-qkq4dc6REZmPEZbIQXjnaeSoR-iFa2xVIz11y7jmiLTOv5FPh6hMnNziO_X8i6z-NrXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smkmjiejJEkPV683Ys8ffboChSJyuzALvxp-wBe0ye69oyJF4S6PvNwBi49dCdxkUg8KJ_y-kW8vnqgP5TD1rJwFD0jI5nIBmyWuxsAz4FHpMXIVP52gHzIk7RNqXrnnONbdub0mER3aQ685Nf-56YDFtjOTk3166x1t91lwUgo0O50R81a7Who_UEaokRDoYaR_9h_pjWuz-iX0P7_ekIHfo9iN_YZNlYBlbo0hf2Ch32K35fl_N_UCwyWpQqg3vu8xGaEfHRlN-z3P-amL3pI0pxCsAzyAeUkQ1l6NTQS69FWn4DzxXEzJ2moYJ1UJetS4Ccmrbp7kYMoP3wyR8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLWMpOlZjL_Jlco4r4dp_Gu43QAzogdf62ebmPrWF329vOlqkCQ0DeQhWC5RkrJDJuBJsqs9D3vH4UnYu_jvNy79qdoqh4J2xv5ZGtS8yZ_d8QcNNpwS0kE4CV7h7DZ3ebxFEZWB3GkeTQ8BSh38ykMzvUIdvk_VOIQDKulKuTddKicnl-ObdzfFaUWfT5qadPYhHyyMM9CXXdPuzGFKEvW9uibwX9LAmkWQYO3xVn7Q009Gd_b4Wf9DIjDHQoZc7pn1DG79HxLV4iJZNcWBN8LTy-O7hj_Ob2klmsgpXBpP_2yQMuIHsvyCXULbswRjhlz48BzdqG7SeJt7dxb_JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUnIA1wrSH_-AU7u-PApfILEnjCAkmDy22G96WGdGZKsyT4S-FF-B33OFAiGzSLpQqFct2dDDaz9TuF3CqTLHOThiMKvxVJYLY2oDNX6lXPPPEwnWzktlLIXbPLrQ0RkQaR4EKtjaMwOCyKn4_x6UOybeJZhMbDbOyl3vpN-i4fqhq1jlIVAfryE564Th8Vg2e0G0sY2qq3AneOZd_mUOtBqe2q4dfFAwrH5gv5q4pw-RlAnCWRNakbFiF8OtVTcql3lq2EENFMpSy8LHjULsoul4ea0AIzPncD_rZ_nX_fjoMsllVJ3pYQojI1WyJH3uBRvfcYRW_zbEfgq9QcHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxGYjH0h8AT50brXCb7aA9ivLPJgt2-geNmFeQHG3DSnni-Q4xM8qWz9tgmr8OHkpE-kzxEBIIM1BsztowtT6oPwnI0uAw56E4lMMEFkQmnFDq1ERc8uKNlqBn8RqUys57vGf_ALDbvj5ietNVDWBdg_1KuxDA6sJ2_DvfO5CQG5QzdoBOlCJYelrL5owKd1yZ1JkBs5h01-GU_XK9snHCWbl6k3oT3pgiUeIemZRpm0SIhM78hOrNwyJfqatPOgRKxUjzB6zYbRxkMJwZL0L35GSuFOwuLyCv2UausT14KfGPtz7_FeIdjMcWnOhJqZ6RFOLDzvVEekXDOzOaQD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swAnTshBY9aG5iJxMo26OpeK6EbSImAPLc5SWVQ228gtZt_pKd63bhsIDa3rQ7-70qip2KpEnpdicufb5Fam3Jfp3O8ugSMTqGUbQm66ecuDTU57D0E1PWPcs12kZFmFXdJ5TTvuJttktOfjLAtaj7Zjzp-YbmFdYy6YH6yfXlkncdhU-KEanIvXiRkyUH3UotOLm61VK9ZzUHcAsrLSDsh-Vl8tRA_xncXvZUSEe-3VmeXk1Re7FPFMgGSIs3QWHVhHM1zoBurwOsOilDRSP7PtJS2hRPjZRC8ZOjIO_7CE2hjuuq-3i_bxGaiDlVbiHz9lHJSaG1F3kB2rpTj3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBhiHjuNrn5jrVmYYjjwkun6iIIH1dUCWg2Ju797vA4yZllV9TCmbSRqw17rKMbxiajVl3_oTA2PTY1QVViZYLyOgB7kTodC7n-8mQgsPC1UUccf7CLyPnhpvOMST9jhEinaUaZP1YONcK5EHb0z4ztNuPnDhmNt_vTTFiG2N14DbNFB1jX1bsbNeIAm2CNG6KeDwfn924KT8MI1HsHAnmfeyNtbcuh6ZN5AH25NJ1RkOqTj3mwlyqccvgZvxvG4nGw2LWhBRMItknVxR3OWt9RWtQ0Uz3NeQT7VPLVQsFLfINL0zkURJMwdfrIRFcd_UrbQH2QTlH4zih94F7-dGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nS5TP8R0F1HXa6zaZC9zowWpAEgtvhPF9DPU_DcxaUgFZ7rKEs6Dkb-E9fDgJp8GhrJ3YtOlilLxGNJizZ3Sgr7OjcXFBDewJ4PvUpV7tH6YDG_k79ANSuug0J1DEk8xkvVjh2BaBODBiFo91CWG4_7xV4J0QVJUZ9aRYPEkKdauslRYGolTY_wuG_Bi4eZj9quOdVRQh9c841WoBM8_iU0TqUvE_bY5BpqEkBL7nJFt0GgkKpyaR3q5FChRokf7ZYVtyfe3YQhk9taaIiCLgJYSSLICuZnZiU8SS-0DCmcOW6e8HQDqrfDo4dRA32N3NY1REUFkJJajcdks_b_f9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2mr6tLP0sQ_KqvjeWCv9hbC1JhXZMSGrg6Xs4aDioOmG1C9m9jYPUuTBHOvW_bdPyrJ8jjP5Ryz5zv82W2XNUYtmNYSlU8vQRh_ZOEFgpyTpr26O5XHJII0rH4qoJycfm1zAyuaoKLPqM0fuJWYDAN57dCNYbnzoJR-yCEUkz9Dz_AOUmqRAgNwwKXwBwHE1daWPHC16W4tpx7LQtV5uOV3ziHIq3OnV_3_hVMK6YL0729e5jqHvC1fDAKUjiUQJ9_-sQcEImqZzMsvZV10jhFm0tW4WT3Svb9909V-HdhTHWwNs_MkTBH1SLytmgBkBn-y9wl3eQoiHJwjAtduoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qogr2gRVlUD3AtlWi6IwskAsNgAmosoN95Z0Y7v2Ysua_2eMFuh4xgEBAzKbyOpRuPilddJQGZHFf9qp7I34SO4P-UptFYLfyv_4bQIs0BsvuKTmEWVWwiECvgQAmVdknZAvbrJmEccVbAG3dI7cgic2Uu8PwngguoYLN1UpvAbuaHYidMH3LCdoeXIRPBpCXCoFczD1rjx1uwIFgIvXs2tJjDdPDjhybwLdMJbJpmb9MRFYjjPYpyCH89ummSp8qyMT6t10Hrkz5jIh_7KWqXGT7lVEMICdyFUg92ySrlZg9Kj0EKf1LtdPsi-OZnYUcRbcWpISaHn3oXCGbcxgVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=utJDGwgfRHn6DG1zi7syXvMLiRjdON7404_XtGtVpy4ZEwbqCX1dnWUCTmTyT6PvKuAfFaSmRWpNyaelhV4IlR9i1LIHD1cYQ_IPRZ0lj9TQPD3fjGtzTckg5ZNuka-8nbtVLi76HPxSAxhm0AjSRK23bf1AbbR6zvxC37cb9tfWZYkvLOJK7aX1SBnXFus73UEehQK2LME7meux0lkE47yYRT9UWwpyZarNYFU3x76Nv1Zc-CJUEPHAkkQFA8-HGdkkQCjKXk4tY9xwlTwR-kKa751IHYZBJfVohBU-bzKErN1jWfXXsQi4q4JS6MRPdqW0VOsxTTfSBl0CtucCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=utJDGwgfRHn6DG1zi7syXvMLiRjdON7404_XtGtVpy4ZEwbqCX1dnWUCTmTyT6PvKuAfFaSmRWpNyaelhV4IlR9i1LIHD1cYQ_IPRZ0lj9TQPD3fjGtzTckg5ZNuka-8nbtVLi76HPxSAxhm0AjSRK23bf1AbbR6zvxC37cb9tfWZYkvLOJK7aX1SBnXFus73UEehQK2LME7meux0lkE47yYRT9UWwpyZarNYFU3x76Nv1Zc-CJUEPHAkkQFA8-HGdkkQCjKXk4tY9xwlTwR-kKa751IHYZBJfVohBU-bzKErN1jWfXXsQi4q4JS6MRPdqW0VOsxTTfSBl0CtucCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddGFJzqHvGZ-KuLtMLBVqCNZt6bWpK3kyXVr493OQ8dgwztB5kJlnHgAbhhz7dBCtO9VB1SLzDm1-jEM9M5NR1hwOTsEwsIcicwIHzXx4X-46UveEJgmcniKsLJJ_fgBbMCoUHu69gbTf4k43m-Pw5MqhbaPOPzl8vFXtNBHMLZKT3E6UdvT2EGFF-qBciMsadkycJyH6b-azY7GJVLUVSJeGAZKT-qZlbVZ22nHmWougebIdNFA3dV2N4DqvxRnXc0dP-HNCyCKLMcZLDije4bzFl3ctxKovH0LYIGKRMz9IYiPPdxYzC1iKHAZB90UkHVWgKHjYaNUZkQ67FvnHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebf8dQQOLSPUgUBooMGl57YvzTi6OsIKsYlf71Yp_iq4PL3Hy7WPUTEAYbSo1JASsgmNuszHnESro-gvn2I0F1Ddif5OlLfIOU3cANevzdQx5RRN1O4ZoIhoCqkNJhI9t3EAbPer339BjQGiF4volpxIw2DpH3cU6g3XdHrwkVyb2mv4X0iB8RZ9gYSvmKfR8i8EFI0scLCEn7KYFuZlMEptWYniLwDDK19xaTEWiXVk5eivmdkrn-_wVEXLcoWwkwAyMThLg76Wn46AWSiBnaHvSTHO2d4mTvbsMMVEih-ibXXJT0-WtPrqIUfDE75KnnofmxwVXYK6L4oxplYVcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=ZgiHEfHnvVH1IudOt1-elqfloNsp2cPQVGarkwpyCZN1DIO6uzGf-utUaEqBpKhRwuQeJRcEUbKgtZLIDe_7nsJxmv8l8iiTV7lajMSa94KyXSr47DJod6QW1W1o8Bbto32BtpQXZfxGQDKiMVVRgPyKNIcTXxzreb2vpEWN6kHkNVwmJ8r_sEsa4wdM5RwlDItj6C27CmUDVKtl0kfDSni1fiqU-JQT-Z1DbfASk1f8KtiMk61ZYwo974C_T2HC_sh47jjEDZt_TtElVDxj5vb4n9YYiwosM0CIbwy8zNEMsDpUJrD3iczi5jr9is_VOqeqf3H4owSmBY2ON2sLjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=ZgiHEfHnvVH1IudOt1-elqfloNsp2cPQVGarkwpyCZN1DIO6uzGf-utUaEqBpKhRwuQeJRcEUbKgtZLIDe_7nsJxmv8l8iiTV7lajMSa94KyXSr47DJod6QW1W1o8Bbto32BtpQXZfxGQDKiMVVRgPyKNIcTXxzreb2vpEWN6kHkNVwmJ8r_sEsa4wdM5RwlDItj6C27CmUDVKtl0kfDSni1fiqU-JQT-Z1DbfASk1f8KtiMk61ZYwo974C_T2HC_sh47jjEDZt_TtElVDxj5vb4n9YYiwosM0CIbwy8zNEMsDpUJrD3iczi5jr9is_VOqeqf3H4owSmBY2ON2sLjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keJvVGue_fmBugNHJKc46tcdf9aQvDsRy9_J7XXrdDY9LR91_KP61vTg1ji9t4TVwdkEObSWcLJ0JlM-xspiHJzy_vYHKlVgIj-krvHQo93HU22e708pCe7uaqUBFc8_-UVKHtyjLXOL0ApwOw7ZWVqTtytmPBhsvpPuqs81wbRMQWZoAwOi8TE3fDeFz8fPcAbOH5_0ZevU9EXLjc3h0BL-h65ucQG9bKzRdvMv4bqXmdkcdBk-qNQh6nGffuE-JoEa2RrGVvX2JW1Zkglz9WQcR72eD018pRmA2SSPxfbmfXuPW5qra7bpjlwyz3fz6-XCPQB4Ja6XvHKenf-c6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oran58UKqhHNFqCe5mBG-ySSQIoPKxiX4ePY9i2RJI04to1BCPXhCRHZ2p2lEWwfsSCyOr_U3zYsqk6ib0SU2kEQ8VDJ8Qbn3e5VeuXVTlzdVJZL-YAuGKvcZD90oVT1oXOJTUS4a5O8PaIaikKu5k8rTWZaN65gr8Ee833W6A3Ag7ejgO0wmgLeQ6maXK7WPWBFtryvcIa5T93IUbukOetPyb7dmZ835brIBrllergK5SFKjmNpKrivytwSbPnD_P-XHL5bH_7rGxnPUVzgx1U0KxzMRBwtkj0yIacQbCCilD1nq0uWg9objvBp3pjAIEi6ggD8XsBsI0aaaJlujw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=Mu1bQsO4L_xvgCTb-7TuPgBq2FuTfzf1eDeAFeaiWuznq0PKp8Cb9SQC1qDeqw9S-0cGhw_VOyguOylOh16dOkQCfx9AYXrFgrz3YNh2bSTiO6Lv-qvd5h_KxQ2RR_ck6gZ7kht1erj5Zlq0WoylIeCDSYg9sr4p_C1NsuE8XrytGmcHN2Y00dDSnX07TybY8oOV_3p7Eqt39HYMbjn52g-hOq7qUX-r3CbIyRWQpBSFyzQeWc3blUqLghHm4BRCVq3v-az8I6IBxJ-KAsLSnuDW53nWFnhZnE_ym69yw4TaqW1VcNRrE1SnE8w3T_nXY8eG8IXYnOtA0Wpe1t0-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=Mu1bQsO4L_xvgCTb-7TuPgBq2FuTfzf1eDeAFeaiWuznq0PKp8Cb9SQC1qDeqw9S-0cGhw_VOyguOylOh16dOkQCfx9AYXrFgrz3YNh2bSTiO6Lv-qvd5h_KxQ2RR_ck6gZ7kht1erj5Zlq0WoylIeCDSYg9sr4p_C1NsuE8XrytGmcHN2Y00dDSnX07TybY8oOV_3p7Eqt39HYMbjn52g-hOq7qUX-r3CbIyRWQpBSFyzQeWc3blUqLghHm4BRCVq3v-az8I6IBxJ-KAsLSnuDW53nWFnhZnE_ym69yw4TaqW1VcNRrE1SnE8w3T_nXY8eG8IXYnOtA0Wpe1t0-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NN5SELt-LOlKaNRx5rXwH_oNIjwh4aU6wRyQs2WajlvQPOrkCUE6vPx5QpLL1wSnkU9fHbQanOHftyr2ZfTW0v0Yu6vLWBZ2hC83Kw1qQ8-vbOTj7ptz2KM2TuzkgdmVGRa5uDu7WReDAfwKUu_lyDz09iDr2MHc3GonU3Zch-skQmmP5zBsUgarL8cFu5JKjp0QA4LaXAmkcuoaEtKi_RS4VP2jfASRlBy15mxieLy0xGWmfQYGMLaJbv1SNCeeuzH6XuPtkLfBXZv0Rc4pZtGYb0cj3zYgQLmncA-azO9HhCtl2fkq22CJUSysqfgVZWCkIRmA0cKPXOpRChDK7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7SIjAWWd53cYUvFqdNiJYbYFGIaWdaxkpNhPzTtNrPTIcpTT1TFAaJcWsLmosiJQeslloDrxvfe2TzKqUnxQhdphUNSicgwgM5ppKy8qCRok78Ip_tfEgZL7eNd-ZjU0IKiBegLNdt6cBKeDPSj15lBt_n7dYKecerDsGhLXnOIKibp213LK2-hKRcn2dx2QWLygW1VIpN_Qfj6gKtp2MEZduZrocrgVgmAfs_yhty3TQ6Dg9SNGdZdLMS-rPyegTLOONFPLv_p5i-bR1gBtkdD14t3qu4yCiNSt3_j_m40vBc6Qi86CAmYAIR5RK9xh99BVCRMM9pLjqiJEiohTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=LQ1qhtUaz_Gqx2yVrDbpQk1o7OO_Q2lajGFRH7CeuB7k2-RDvskRBNMICmCQYHpngQMydXXFRvRRIyV-J96jpN_prFhKDqIoCImukHA4qw4R8qb28wZtLg4rZ4kd2vbMR6AclfZp1SlMK2Jzwfft18AGo-9dgucED8pTVFDKTebpHDiUSWxCeBj2-vsrOwDs2ee2wV8DTEB5hpTaAmhsQbcbqvj8FXWiCzAvIbJs1Ceisne0UnZHy7QNbK4eJA-rP7DdFLMtuRkFO7XtMoELnOzdlTHKzGSX0NPhwtnT3kHCBNy21plIV0QtT0wwhNZyRfhU3d8ipjv0gEKBukNsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=LQ1qhtUaz_Gqx2yVrDbpQk1o7OO_Q2lajGFRH7CeuB7k2-RDvskRBNMICmCQYHpngQMydXXFRvRRIyV-J96jpN_prFhKDqIoCImukHA4qw4R8qb28wZtLg4rZ4kd2vbMR6AclfZp1SlMK2Jzwfft18AGo-9dgucED8pTVFDKTebpHDiUSWxCeBj2-vsrOwDs2ee2wV8DTEB5hpTaAmhsQbcbqvj8FXWiCzAvIbJs1Ceisne0UnZHy7QNbK4eJA-rP7DdFLMtuRkFO7XtMoELnOzdlTHKzGSX0NPhwtnT3kHCBNy21plIV0QtT0wwhNZyRfhU3d8ipjv0gEKBukNsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8STTWYIY0BTu-cayE15qkTP0--8h3Se6e4TXMjWBzSLpMQBQyUAeMoUlT_ru71bNDOEAf0U5DHY7btW-7IA1XNNBTGy35INOxPnRn2-kZeLLLMJhj-tY8GNobzQUkpKyKv5ZGowjN1XdhYzYWgYia3mdeYIncJ7nYUTh6caKzuACcgyO0GQxkfueiv6NVKSLJmH5f6y4pcBYQI1i2-NaKE9EFZk3vLJoWcFWiKNumQKluhJt5RTi_v1XHVY4HjSnaO2DDGfqbKriG_zR4nxrLEyeFamjlZhjGS1L43RwoURo4Ml1VX-dTsa2vze9Kwt1C-k11vi0-w9ncj3Lw3z9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPAg4qIwYPA527o4BzUiQY4NC0AKwltG-uwPZthE-OeUB_s_L-hDnB0IHWnNps1GfwmeYkIhcc5D1qctvV7CtPs4RHKH5iU-Jsu14ZxeURVePP84aao5s-SEK6YduwYRle9tM2q9-pvF8iu4YWSskTQLR82XlUl7I2zdXQhkmrql8pZkOCUTVjMqBfd2Ctc87bJPPA9EgW2WBT2V-i__HUMtJ3YQCtk5j8CN5SobiLUeYmeFvFRYwQRRMvft5vBX8Z4_0Ca14nkV_9VHSrg3g0kx_82QRY3-_8XRITE9nhpvh-2fMGEA5eTBbqMg-26mFKsBfX0Yxd0PuXIYR1gg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAAJmUEQR0II7B49rjPacF_yc9An1WX38O0i2weDuO4YyYzKhjsi-43rOoB8-fGzdZi0PQd2DtdwnB8hIvdlqA9HCEmbDROBgMwAnwzFWU18ubXC5ZKDE5R0G5-eDcWMlmdTGKlsNwzWvTaPhBloFYjf27IsiGgFZ6aWUeZBHQGlhOSXZ5Gewt7vPt9QujbIg0TvvWzbmJbkmphTrtgwe594USvUQC4J40A9msGcys-VkAYE0oqTmGVIKcfjDhKlk_TbQjL_Uij-BVGYPzDxUzdfTc6e50KZoVVoT42aVcQ0KCKfcEOIQYFJAwkmzPOauKy66_-x7oki46x_m8qaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGdyIYJ0ju7nZnTEeAh6p0c0PQUvHRDD0578FV6ST1P9MddgGxc0c-_7a6Ei9ShssgxWzgGSRLNjJleahKP6IHvpmnx8KHuS-wbn8IgV7EahRijOFTNfmr8cW3j4WDlQiFaxp5bQpqgo4gKgSK3-ysJFb7fH53d2QvPHN1E3xb7--grMWfdT0E3rQrXYkYpJbZlzxDJuao8dnwKU_mBdsi0LSK3f0JDjX-c96vxnwqxfSJKOyimu_FwaIjSljkoU9jBMLEoRcyaVjHS54L88yCwectQW913SEOdo-gNV42lruPBC81oNyIySW9m3oUcDzFU-xedUPm46-D5YKOOgQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTBRV_A0J-RHIOy6m860CypMs6C2U9_-o6YS1ri08Z-z6lkSLnPeTODPGo7dgWKIgqIINascSnxTXtESE2SxBv535JzQNl5ZCfEtBK4VJKx4lVETqkkaGo0736H9qPwlYqdkinBoV64_z4Raf8jzfX95UZS7ONe9VvRHS3RK3znsDgwg9d-_2KepxQ-GuShI1rjVa4RYgYDLxss6IsI2kcmhe4Na7WDwIOUS20AkO0vwCdD_u0GhKqmVF_86qOLzM5KagW8vC-Ma1aP_X6jDTu2Y0KejB2Gp3W6uKsj3VfpKvdiug-Cp8XC3DfErMJkkMG2oKA4hkFlGDIYzGZCyKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC0hTqQoOvx3BSg3XZ5h3iJC23XkjpxI7bJXJ-synAPm-HbAizXys8TlviyXBI7jeMbBXAb9EBdW9-qc2wmuoNcns6JfmoEIAmyYayiC200X71OMO03ka_bcf183sMbOyPcKNgbk3THFVl9Ld-7YsMDmc1HuM9Tx4kO01brHl1cwtjzykLlYm6lcvznCrFrcMww3ilJNPifhNCwa3XU2J1bTCFjw_8xAkP94VqSGV_-W90UtxhTK9mxNDp_dFI6soBvv7V8FqcgCUPcBmgjfO1EfvZEKbDjGRQPPudhA61G_tPSo7CUpGu2ThXdWZCA5l4TiUt5UxOHI9LILbGlZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN4PankD9hqlUOwrL08IsaZs5D1h8Ip1A8DtE3ljNkcOkgNOlsU4uEdJpG4Hth6exh8A9oJ2KQSSV9sMyJBVJkSRyZwgINtSNsuk2JKyJ_yXmMUHCPVpLUgRs4i4ethzxB2M7g5hAL-JfbDGBaU83ksKmUrAm8p-HRCnLIOj7yS1m2DknYWDXwWuIaA0B2g8MvFLURrtqyQMB71SxA2q1ltY3NIoovIi8WjE4q02pD0nosLYUb1aXahn3Drsz7jFCoJgPLcepaGTzsp6YVapfB4dvnzXkwhmRd1Kwt7hWwnG_e4imcPioMASUq0K4qLlB5lQJNznogdPHwZ2XuBHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaoQMKZrPyoQuToahpRafz6REFvTI9Bcl5qNvXnuZ2sgvBMEVCJXGTUbUWx3s7--w_MKCI-Rfe7EquR7eTszh7-JsZu5qbbjplKOjkSLzeo1ip3eI43rpDGOzMFRny0wvp_JbIcOxHjRlCnLQ9fY62dACYW8FuzmuSBS15bS6nmKs9Oxzzgnh6xgErXZb8MgqquUk2QDrkhHcugAL3LeqFs5BCFXPvF90vfZS4pJSBDF2L2voVYMQNPCjDALOrivBVauOEhEBLVagjgIhynH61GwR3sPsCTe_UgAAUgh9rXRKv0u6CI3XdmwiRQ2ppBR8gUCR7c3EvKJhDY9uJ0bDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=GTiR8r5ZU-sTYxGwl_NIAwpaCXCYLt4S4UNSaPmsUNPvC7En3tqNs7fNTbYgEq0PXr2CdKtgQFHsmBFaZs7WNT_UhcLx2I0U3BzjO83M4LQ__afYLk7-hk8oMxNmPBI29TQW1BpcO-igJjgvdls3J4y8ubWbqv9ltqUPBXeVBFDdNOCMRqGdpGSC8RWY_AGcPKNnvcjfO6psUbItPiFFmijkxKybsbiFTMxx4MREU9Cra-tpJAv1s6w8YvhQrjXoELAIAtb5j8SiVUzZ7THjCqiJKPH5mFRwE0OpgNDDC2Mpkt72AdgpgtgmL4j-FUhmkCwOhVhuk_0C_3pV0QnjYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=GTiR8r5ZU-sTYxGwl_NIAwpaCXCYLt4S4UNSaPmsUNPvC7En3tqNs7fNTbYgEq0PXr2CdKtgQFHsmBFaZs7WNT_UhcLx2I0U3BzjO83M4LQ__afYLk7-hk8oMxNmPBI29TQW1BpcO-igJjgvdls3J4y8ubWbqv9ltqUPBXeVBFDdNOCMRqGdpGSC8RWY_AGcPKNnvcjfO6psUbItPiFFmijkxKybsbiFTMxx4MREU9Cra-tpJAv1s6w8YvhQrjXoELAIAtb5j8SiVUzZ7THjCqiJKPH5mFRwE0OpgNDDC2Mpkt72AdgpgtgmL4j-FUhmkCwOhVhuk_0C_3pV0QnjYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqMS_qFDjw_-vyPkFHO6C78u1gmQY5oeXUpsuIhVVpTyP-Hfat5SnfQchkFKhNTcHUUPjb_uDs9BHguONsaVczrQemuG_kLss9E6j9WYgV8jEmUO3h9jREG1e9LnGWBufsb7_p1NbpOkgPwQW6MDDwmtuRfn_8-LoEJP8lnwJmgrk__aRRU0C3JaSu6N3y78JmOzlw6R-F6ThMjBghYxvj5D3oPJ5g4V5BGk9I9WvIu7Osu4iLPnajRbw95acl4Ng5icKNHQRoJ03Cnbbqa2nabDdxjgDky89KsBLZaFG7eosBdTj0dceoC9EmKMVyZ27v-CWmnOYyc-kMnK8OaZQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=tArNUnrsXK9g4v5-8di7jWRWw_upD2NKfOKzdTGmxeKKooLWdb-mjspFm_bkL2IPlY5nDBNFdT2q29ekKYV1aECjGiOUQ9UjWLyCQZCnlANBvBrsL1VCowTZYJSqkrXa9AIu4_aEiutdW1pXDe4EvJ1Q--OEugJbnaJWkbvf9lXNjttXoy5GbnAovYmAhjOCulS0pLz7d2B8eyLZ7ZlI9d_Lb909ugDNrbq7ohMf-uaKIuSWxu0ov6Zcs8k_vh50gDZyEC3u1BhGPR7kJqR4QxFrNfUBCVPYX83t4jBeB6cQcMBd4jMc53i1pPXCTlgUayYz2KwxoJ6xdSAHYhppxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=tArNUnrsXK9g4v5-8di7jWRWw_upD2NKfOKzdTGmxeKKooLWdb-mjspFm_bkL2IPlY5nDBNFdT2q29ekKYV1aECjGiOUQ9UjWLyCQZCnlANBvBrsL1VCowTZYJSqkrXa9AIu4_aEiutdW1pXDe4EvJ1Q--OEugJbnaJWkbvf9lXNjttXoy5GbnAovYmAhjOCulS0pLz7d2B8eyLZ7ZlI9d_Lb909ugDNrbq7ohMf-uaKIuSWxu0ov6Zcs8k_vh50gDZyEC3u1BhGPR7kJqR4QxFrNfUBCVPYX83t4jBeB6cQcMBd4jMc53i1pPXCTlgUayYz2KwxoJ6xdSAHYhppxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=o9cuPWUGcyofiY1t5A8F6t6F_D-dBaIcrEQdUtQ-ublGrMid41gSrgg4xn-kUf2sBQlJOSxkvvqbxquYdCgjhs3AnrLUt3nksuMAXWF1kGqiiLWfOrheU8ct4HujNrr6lxjvsJY_A_ZArmksdS1FhUZKFRY4b4M3OgbK98RlpKZtDA9KTGI3A7Xuqs_6P1B8SvsoUmBdajjoYq-64O6HBdhgOH3Io5dwbyytn72wtPDk4mCcLfDmoE9PFp9HCAxfRGvwmHaUbCnk-5W0oXq-7pB9UdzjtZod88OODyRWiugioyltbE6y4ZabUi_WvG-3HR90EXQFs5AKjuw3dDviCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=o9cuPWUGcyofiY1t5A8F6t6F_D-dBaIcrEQdUtQ-ublGrMid41gSrgg4xn-kUf2sBQlJOSxkvvqbxquYdCgjhs3AnrLUt3nksuMAXWF1kGqiiLWfOrheU8ct4HujNrr6lxjvsJY_A_ZArmksdS1FhUZKFRY4b4M3OgbK98RlpKZtDA9KTGI3A7Xuqs_6P1B8SvsoUmBdajjoYq-64O6HBdhgOH3Io5dwbyytn72wtPDk4mCcLfDmoE9PFp9HCAxfRGvwmHaUbCnk-5W0oXq-7pB9UdzjtZod88OODyRWiugioyltbE6y4ZabUi_WvG-3HR90EXQFs5AKjuw3dDviCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=qhJ_i1bfxWNvSP3icSPd4HBQxEmM7U1jGShoC9Ed-U-y6-mVSEyepfnsmnnDZRnQGH9Ruj-TLreB0pGPcc2KIj5ZP4VNz-cAKTUDk31ZWQg5m6GUekabw1QoVj7kWyh1jznMOf7Uv3fHATHtqjouAU0WKAngWdnU8y-ii0fnZTvrGykNXFJnhI4kNgsB6hCQBLk7CoZ2OHwBT76xnmC0TU2gJLi9woKmXXFbHP1Gp2B2_wCJrPsd4H71Hk1eZk_SM7offVFl4Nq6UkM6pA9aKkoeUZ1EJpTgPC9svA0ACCskIEztXheOZoFOjiJmmGTHe01ra5Arq6VDVz197vlXfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=qhJ_i1bfxWNvSP3icSPd4HBQxEmM7U1jGShoC9Ed-U-y6-mVSEyepfnsmnnDZRnQGH9Ruj-TLreB0pGPcc2KIj5ZP4VNz-cAKTUDk31ZWQg5m6GUekabw1QoVj7kWyh1jznMOf7Uv3fHATHtqjouAU0WKAngWdnU8y-ii0fnZTvrGykNXFJnhI4kNgsB6hCQBLk7CoZ2OHwBT76xnmC0TU2gJLi9woKmXXFbHP1Gp2B2_wCJrPsd4H71Hk1eZk_SM7offVFl4Nq6UkM6pA9aKkoeUZ1EJpTgPC9svA0ACCskIEztXheOZoFOjiJmmGTHe01ra5Arq6VDVz197vlXfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0TI7mWlzybsp1-ZXRJ8hwuLBjdx9BkHcKRhoyfUtVItN7T_fP8POWKJ3InFNVODU1MrYmY-BauFN9RteCct9vA8toI3QWeuzixKyqQEZM_jUgbbWpW94r9WRqavpZv05iA5AhGL9TecDShiUd-RpsOY9tpx1F0-ZOG5DLBu2ut_GRN20K91NaX6LjGbxsqkeFkS2tMIsN4849c2xfCz6DY7rlpeEHA3rAJaTaogGaurbpCxYE4pK8xPIY4f0nIKnIj1DuBM0CMeRb1euFt7EAHb42Pj4eFNVPWw8ZSfMXXI3IyBiUWGY9wb2X74zypz37-gaS3L4ZowaXmnaaM7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn-H5IQ6XocZCtk5DS7XZQYoKgdk-azheo6rHpcbAmiqLuw-4PKCp4xRxJ0-Zjz7_ml807h6VYVPNYYXGHRfac3dGGvamr82gQtxGbIYLTP13_bZymfb7a7L65p0yMS35F1le1W1CybkPwLKchC3syyWOSi2vC4kqn1rcQeCtauXsHg8H85qpjM5vM7sn75rN14kEDPF4vxTn1SRg2U8N0VOoMOuLxGcOT7G-VshduCpGk8oAMb7-i0wNh2Wc3kPfxFNQsali_13SAPwX-fmf-4hy-2JIBmk931ApZT1kbp4SKUgkM6IrGPtWKU9MNvVMISBGZBu5uUHaOw5UJtQ-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=dXY9Hea7dOAX4l8NPhLQXomPbJ-1QXaB3PsBBN2Bfpinz0QOKAPGWKF_lQpkMcc5M5_ZDdCuv6Je_cob0QR4xiVPn6crctuH0XnuYPEdFFwmammNjCVq-eJ7zevSwT_efuAkkYIgaJoWIuJpiBqvK4eris4DSR3uWoDVaKI_nx0R30POHIuMfA3WAQ12MGZ1w-3pbhFeV4xm_bkI23EjpqdZ8NeEwXv5Q4cqGr-1wKDex9vTgPyBP2fkqcDxfD_-wfPlpJ46IZtf-PfZOIvIEUbgqZ7jG1hDtp9J0aAYyq70tv2-Mt5naBr9nL9HKolm-2_V5QxQ9ddzWJmhKBkg5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=dXY9Hea7dOAX4l8NPhLQXomPbJ-1QXaB3PsBBN2Bfpinz0QOKAPGWKF_lQpkMcc5M5_ZDdCuv6Je_cob0QR4xiVPn6crctuH0XnuYPEdFFwmammNjCVq-eJ7zevSwT_efuAkkYIgaJoWIuJpiBqvK4eris4DSR3uWoDVaKI_nx0R30POHIuMfA3WAQ12MGZ1w-3pbhFeV4xm_bkI23EjpqdZ8NeEwXv5Q4cqGr-1wKDex9vTgPyBP2fkqcDxfD_-wfPlpJ46IZtf-PfZOIvIEUbgqZ7jG1hDtp9J0aAYyq70tv2-Mt5naBr9nL9HKolm-2_V5QxQ9ddzWJmhKBkg5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=c4uv-WtWFT7LFe_-oi0VeWs4dC2bLrKQKBQkQ_GlNIEE9vvWG9JmkJp63idYCVJHSEAK1Z443Ad5yY7Hy7Ocs0ENrBgnU0c6aSKnJ6M0V1kjK2XJMdj9RggMTZO0Nth9eyJsbqHV39rTEJNU-geInKsUWkQ4sxtPm1TwOXdsDhXZNaIQRxDrn8hbsTuXxIlTL7cSYQ3u2PMSvXNSG8PGMuXmGicPZduayK-yc4YvOyLE_9krMCnRXvWvCmdHICj-owP-c7Q_6K-t8pL4suMu3u8_q_Tk4kDWAvqDAUvFEu-hKiLfYo8D39Cle5mQ1Vrk9vDE4PaMkEa_QZFYhoNG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=c4uv-WtWFT7LFe_-oi0VeWs4dC2bLrKQKBQkQ_GlNIEE9vvWG9JmkJp63idYCVJHSEAK1Z443Ad5yY7Hy7Ocs0ENrBgnU0c6aSKnJ6M0V1kjK2XJMdj9RggMTZO0Nth9eyJsbqHV39rTEJNU-geInKsUWkQ4sxtPm1TwOXdsDhXZNaIQRxDrn8hbsTuXxIlTL7cSYQ3u2PMSvXNSG8PGMuXmGicPZduayK-yc4YvOyLE_9krMCnRXvWvCmdHICj-owP-c7Q_6K-t8pL4suMu3u8_q_Tk4kDWAvqDAUvFEu-hKiLfYo8D39Cle5mQ1Vrk9vDE4PaMkEa_QZFYhoNG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7w3l9FuDEKcfJS3tB0raoKD4oWVrwXTcOP8aBWYwd5kJJq60rTYsigHDzeH6piMeu1aU2hJ7Q-fOpVlhfkcQmIgH_UEYMnk20qyLb0tjObx8EBEnyBx32-8cKJBJnNA47xbrh4-yz_EAJuGnIx38aXqqdDOTyTZ4ogUjj6xkNyJ0JYZzk9aixW_UwUzOIy_bRCl1LMnpt9pySgIWKfHS6ZoD7Zz2dmwdQm8SXY8cLLI_DZsN3rjxLY_dUdMIBRjP7Jk5I343rBLPF5bM79puQqOQ9ICMp83cL97H6OQ5dAMkPehPGhNENmSROo4Kthzd4zeAcGk0ojOtLnuuFoYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=Zem9jQEBp1UJHLEdkrbed-A4QCWRDlmgv-U1X29s-duVsu9aYN8MO2F_Q4ivq7K9ro2PbQ8geJLsw4CeAaUom1wmXIt2Bz7uAgAUKyNfIiApPodVMZJWGerRzb0CNvW7tYdBK1xXeZpNQG_i7nR_rL6GW7pbe7xCJpu62-N38JtskDVgUaLdjhjlwcITNj6KqIyqrvbupkI_xp6ZImnENt9s65M1PUECcmzEV6e6hsgaJj22FQXskQilaIP66RWZ6_-BbjbL2IS2_PQ9YhA7i90J3p5gk6Au-OYRUD2yv5RSCq12vreNnaWOhfTg64sMrr4jwOuUyBIu2HzomMGhJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=Zem9jQEBp1UJHLEdkrbed-A4QCWRDlmgv-U1X29s-duVsu9aYN8MO2F_Q4ivq7K9ro2PbQ8geJLsw4CeAaUom1wmXIt2Bz7uAgAUKyNfIiApPodVMZJWGerRzb0CNvW7tYdBK1xXeZpNQG_i7nR_rL6GW7pbe7xCJpu62-N38JtskDVgUaLdjhjlwcITNj6KqIyqrvbupkI_xp6ZImnENt9s65M1PUECcmzEV6e6hsgaJj22FQXskQilaIP66RWZ6_-BbjbL2IS2_PQ9YhA7i90J3p5gk6Au-OYRUD2yv5RSCq12vreNnaWOhfTg64sMrr4jwOuUyBIu2HzomMGhJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFOSTV9M0FTEEMxJfXGB1-_i66SQR84VFrUPy5Auw601Bui89XD4Vg6Ek7q8ovy4mpuSULnCCHPKoFymEjTQ8MBJe5gYGdVx4Frkzwj0bOj9ixhS1LVyc2w8FDFlqlwZ7YeYsYvAbrYEK46HF7mQcfQQlOE26ISNdRToTUOUilQ_AmGyEVVCdSilUA5OtDuCFeoTOhf9IS1NTkmjpxv-ar2I4vBbGTjacqFsMVT6xLUiL0qvwvL26XtyBuKGrmY6BGqt1H8KXd1nuybtjtKiPDuMonraVzl5IJgvbF5eGhNha2fisbbTtmc-rL3Zuc7o6exYhv5ox5-8hNrcSyDSzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1hZ0OJiDF_12eiyF7DPRSdIHxGF5FEtbx4EZemzQWVDN6qaZG9LK25VSeUKHftyp7VJwc5Zpwkjl6XQ1njAxTF0FjGdTA8hbeSEcwC3IExxh9M8rbngb6RiczpQ6DjencBJSlFhYSnSv0Rb7xTFlgTCgXiEMEgHvJTGHnxPA767Lq2elYe8q8-eQv5PTvLYqPa5TdIDxERVedhADqkVpsjWdBfvFZK5qXHpuupu0MF7_RdypKMGSM6oaWl0hTICVjQkF2V4dN9fL9Vh0FUOxIiW4YCmfNbIu7CQ_GoKcs3vJeydxZ-Y9P_FQK3Oh0LV7v_50ApRmMnhOEhkp539DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7OrcQcHQ1akLUJlJ1T2b624tX_YCp1Vp475BzTfjgf7ByPjXZ8nPPKg-7wqVuAAoEyydZuPYLNm-ZZC-_M1bCc-e6-Gg02sWmhc_36SqXPiqP0oNw22LLdGt94H1Ktu4c1AN1hNmovKEcS8Z97R_srC_1WBtwoi66wiKGm42wxkvwqisKZxCTWj2Z376aYeVaL88i1ZPHgCKJ7wCOZpZmShWy7p5GItFWW53QGgJqGTXaXMAM83lUIMOR1sYD60yMHdhSGw_UVfy0xozS7fdlwxPnROv0l3UHEz5lNfT0lAcKPajME5RhvsmZLLWcgkBMccf8tUVt-CFjvYrzzyFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtP5TbKxgmtze5gxOqDeW3RzFIjmpocC8uik2fE83hM0s5R5XKFjO9Q9tQNHE5hR2x08icXg07o1Q3zzooXEr9M2LPseSq4UsmvNUGQ2kE2164VhLIM_eQJcG2te03S2P7eJhKyX14A7SyzXBcC6g1V4q6ZHjo_S8BRb4i4HoGdS2JBuPAlhfyUwCwFLRRlaI_tVTArXU1Ehs8qHfdTrQJKU5EgAxjOrT2JOYC0aPUsKbjensw8S1efiPDH73uyNxzZrXExA2Oie6D_33mXgK9fca0Wb91W5h_au0EoksiiMZYiwybyU4MCgIxCBf6clpb4OQM8vtbkUDGxO1nVD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
