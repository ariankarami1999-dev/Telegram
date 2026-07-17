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
<img src="https://cdn4.telesco.pe/file/uhDvF0Gd3UEBtEBFl4Yp7Sh3i_muUp38zvdlXLEKhGwsCO4Ia8JfvG34n7f23tFfktpfRgkygpIhV9EDe_JocDXI037w3kc47LmuKryf5dRDQh6pRb7vApZMvyt9YWo7sTaQ3B4Le138NoBtqwFFM04DJ0-y_wx8KK71UMidxZ38dfLtUAVygO2-GAfzrMxg-IJEWKMp4Bv-o03ShPmVM3v-U9REKx8EBRwDZJcHkXLRwoDflmxT852VRvjgKHrAONAnk_15mMLOvMtILUjhDlz8jxqEL_2-er1RINOdbdc8KpLlMrtAjQEgKg0kCvB4lUzADkKyMbtWlCgTZyXukQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 23:29:19</div>
<hr>

<div class="tg-post" id="msg-672300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی، برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم
🔹
حملات با هدف تضعیف قابلیت‌های نظامی ایران، به دستور ترامپ، طراحی شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/672300" target="_blank">📅 23:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
پاسخ یمن به حمله به فرودگاه صنعا؛ فرودگاه «ابها» عربستان هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/672299" target="_blank">📅 23:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تصاویری از لحظه برخورد پهپاد انتحار به پایگاه آمریکایی الحریر در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/672298" target="_blank">📅 23:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672297">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAooAkTjS3ox1ZY3VNH2gALAnCyEuoWSs2CSKOX1rMZ8rmFAlYi-6WomSwII53QDepgWo546RvgH6KNeZD_OLfxVWFKXEBRrtsUYMKto5IwIAgmoGMhgGA_M8cxVjK47RGq2M07Vek0h30iqv9nIRBfBas4pI1tI5c22I1bplOkvqcpLFnfklu7_8P4-nkfJpV2Plp5yocwlsWWJ-Bjn2IgKr3G-2e7zfs8KMbWu7MmtBnnRfMHdmWdqt3B2Xjscf7KtxH1Q_SU40IiOPFJdlTcx_qqeMxmQDZVtoQZQNRN7-TNNTIpOCKrY-WjUaeoUtgAxfg-rEvTZSE1GiC8Vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
احتمال به تعویق افتادن فینال جام جهانی به دلیل آتش‌سوزی‌های جنگلی در کانادا
🔹
دود غلیظ ناشی از آتش‌سوزی‌های جنگلی در کانادا، ایالات متحده را نیز فرا گرفته است.
🔹
به گزارش خبرگزاری Ole، احتمال به تعویق افتادن فینال جام جهانی در حال حاضر کم است، اما فیفا این…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/672297" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
هدف‌گیری تاسیسات در کویت
ارتش کویت:
🔹
حمله ایران منجر به هدف قرار دادن تعدادی از تأسیسات و اردوگاه‌های ارتش کویت با پهپادهای دشمن و مجروح شدن تعدادی از نیروهای زمینی کویت در حین انجام وظیفه شد.
🔹
همچنین تعدادی از تاسیسات حیاتی و عمرانی از جمله ایستگاه تقطیر برق و آب مورد هدف قرار گرفت که منجر به آتش‌سوزی و خسارت به تعدادی از تاسیسات ایستگاه‌ها و واحدهای تولید برق و همچنین سقوط ترکش در تعدادی از نقاط کشور شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/672296" target="_blank">📅 23:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd672daa05.mp4?token=WfvNaC5aG5h4TYAeVGSNKuggTb78MPUrAvOP8e3w4hppyB56jLsz5PCaHjKtXJyT8iS6ey2V_-nO_rXzXE5tWzr5vxEdIzwQQ7xANgcDqOPgAgBEu3K1lgw72m8fLx5py8ddRQuxszb7NJxRe-YJG04sczYQIhgAs8S9-L9R5_WAR0IR7ZYVW9bc7VKpliWG4OB723-f0iw4jg6LG1VTZpOQstG-aMLlGEuGPi3WjVoKE3lb86wLSvxYMV3u1NLYnDqJbg-ENSWLywcR4mAltaqL5tKNAgIftkFg6vriYFHDPkgWBWbromlrHczyuPJ3gR7PtOvZAZGjSCGlwE19FWTMZ5ayVjhvu5-ApIK3ostHx4CCWElNLKCVL0RRpDFdajSWu7bKCrR8H-SYMa963l8GQnFEVRH6sBe5UW7tiEh8VhuB8WbliqJX70MXojwM1PmNhnTVjAU2N0dbOuAoYHs9yfygBh-bPEPIM53eGe0hAYda6uRsFH4tShXMjfOKuL4DGmr2c5a6P4jscqYQ8Ulbo83h5sXyqB7BcMN_Y6JtU2y6Vc9L1XVYUhHV4OasP1xDJ2JWgh2DxLZ5zjpkPofe3S-v1gy6t8CcPNnrbO35mvsQxTpZw5mr9LPuWkdAGUouYCeYwgZKE8MGOTxEnUd9o6OMpV_gmsfzZmd9FrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd672daa05.mp4?token=WfvNaC5aG5h4TYAeVGSNKuggTb78MPUrAvOP8e3w4hppyB56jLsz5PCaHjKtXJyT8iS6ey2V_-nO_rXzXE5tWzr5vxEdIzwQQ7xANgcDqOPgAgBEu3K1lgw72m8fLx5py8ddRQuxszb7NJxRe-YJG04sczYQIhgAs8S9-L9R5_WAR0IR7ZYVW9bc7VKpliWG4OB723-f0iw4jg6LG1VTZpOQstG-aMLlGEuGPi3WjVoKE3lb86wLSvxYMV3u1NLYnDqJbg-ENSWLywcR4mAltaqL5tKNAgIftkFg6vriYFHDPkgWBWbromlrHczyuPJ3gR7PtOvZAZGjSCGlwE19FWTMZ5ayVjhvu5-ApIK3ostHx4CCWElNLKCVL0RRpDFdajSWu7bKCrR8H-SYMa963l8GQnFEVRH6sBe5UW7tiEh8VhuB8WbliqJX70MXojwM1PmNhnTVjAU2N0dbOuAoYHs9yfygBh-bPEPIM53eGe0hAYda6uRsFH4tShXMjfOKuL4DGmr2c5a6P4jscqYQ8Ulbo83h5sXyqB7BcMN_Y6JtU2y6Vc9L1XVYUhHV4OasP1xDJ2JWgh2DxLZ5zjpkPofe3S-v1gy6t8CcPNnrbO35mvsQxTpZw5mr9LPuWkdAGUouYCeYwgZKE8MGOTxEnUd9o6OMpV_gmsfzZmd9FrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد انتقام خواهی مردم بندرعباس در حضور پیکر مطهر دو تن از شهدای حملات جنایتکارانه دیشب آمریکا در هرمزگان
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/672295" target="_blank">📅 23:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672294">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=YLllOwCNSgEwAWVe8tI9XlTKmqrPuRzi7i1N1JomyJAZAUNIkfGM3BELMVSgmLpbGLJbbavIQr9DU4yaXddxw4tcPLKe9f1qGbuJrhR9xBEj3-xHguywoIeAeCbgZiDAnXTdM0J2woC_e5yTAJvhxOGXkJ0S4z265p0DXXj-OA68ZhQfYGqWRh9MA-qkUtNyF8z3uDdxRfnEfsBvHRHPrVweJnXsbUc-QoBw91trx0ix0DhWjVdbZVlVrlhJ5imkSppSycr3lLI8ap9wC7vsPKTf4J7O_7t2kVdrGgzkyvYld6RmFDs-kqaliLj_PKmUNdgyE3JrikIHgMvR9IpdMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=YLllOwCNSgEwAWVe8tI9XlTKmqrPuRzi7i1N1JomyJAZAUNIkfGM3BELMVSgmLpbGLJbbavIQr9DU4yaXddxw4tcPLKe9f1qGbuJrhR9xBEj3-xHguywoIeAeCbgZiDAnXTdM0J2woC_e5yTAJvhxOGXkJ0S4z265p0DXXj-OA68ZhQfYGqWRh9MA-qkUtNyF8z3uDdxRfnEfsBvHRHPrVweJnXsbUc-QoBw91trx0ix0DhWjVdbZVlVrlhJ5imkSppSycr3lLI8ap9wC7vsPKTf4J7O_7t2kVdrGgzkyvYld6RmFDs-kqaliLj_PKmUNdgyE3JrikIHgMvR9IpdMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله سیزدهم عملیات صاعقه ارتش؛ شلیک موشک کروز به سمت شناور دشمن متجاوز آمریکایی
روابط عمومی ارتش:
🔹
ساعاتی پیش و در مرحله سیزدهم عملیات صاعقه،  سامانه موشکی  نیروی دریایی ارتش، با موشک کروز ساحل به دریا، شناور متخاصم دشمن متجاوز را در شمال اقیانوس هند، هدف قرار داد.
🔹
شلیک موشک کروز توسط نیروی دریایی ارتش موجب ایجاد رعب و وحشت دشمن و دور شدن شناور متخاصم از تیررس رزمندگان دلیر این نیرو شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/672294" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672293">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
والیبال لیگ ملت‌ها | ایران به اسلوونی باخت
🔹
ایران ۰ - ۳ اسلوونی
🇮🇷
۲۵ | ۱۹ | ۲۴
🇸🇮
۲۷ | ۲۵ | ۲۶
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/672293" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672292">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4576e8e153.mp4?token=OrBHShKfvjH6ZqQ9iolysgds-dDvGRT1_6OaAuXaavvtOycST956SrVmb6gr1Bv9bjVzMMG3AHoYnqUwXksOjcj0-TW9dfqa3drfwe3hNbFMmpBYgo8LhPO4BLxfWXcnjRcFLKAMtwrdKUwRftN0fNoLx13O-Esm6GgA3c9ICQPSGz2UvSqMQyWNLhzFjgzy1sQsct80boUGK7Ty2LvLq1ZcQ7u0BYDgCXNh_sPN4lDmr746wOmACtKEnUW7keU_VAd14UrWBJIoxsv4ACNRYGhHmiX6IpDD8OAcoSlrkVdLRldht480Ih1_kqqlnPrjNumBP8sqstFeA45wY-x-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4576e8e153.mp4?token=OrBHShKfvjH6ZqQ9iolysgds-dDvGRT1_6OaAuXaavvtOycST956SrVmb6gr1Bv9bjVzMMG3AHoYnqUwXksOjcj0-TW9dfqa3drfwe3hNbFMmpBYgo8LhPO4BLxfWXcnjRcFLKAMtwrdKUwRftN0fNoLx13O-Esm6GgA3c9ICQPSGz2UvSqMQyWNLhzFjgzy1sQsct80boUGK7Ty2LvLq1ZcQ7u0BYDgCXNh_sPN4lDmr746wOmACtKEnUW7keU_VAd14UrWBJIoxsv4ACNRYGhHmiX6IpDD8OAcoSlrkVdLRldht480Ih1_kqqlnPrjNumBP8sqstFeA45wY-x-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از لحظه برخورد پهپاد انتحار به پایگاه آمریکایی الحریر در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/672292" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddad2c1542.mp4?token=mvvYlJ7Jbm4IG3pZiGAFVICNhTKw52LSJA6tDyiaZfr2xxHd8eSG-pRZDsUAc7N2DjYA1HGwiDHZhT8PhzRGTvizqjCH8Q1lQenpBUZpwqNeErUngaqFCrXJuqBTIOdjLAsWS-QsHJLqm361VwKq3KWCJ5AIOY3JTUzdGVxe0gBXXst7g6pTz0_mSrTjg6E0znAKwIrUZOJ0NM_rZaQz15p-a-_P6PbCf0UpJEQ7yvry-fsK-pdV6JbvdLMtiNvnWpIdBHJUTd8ALJt7FVnhtOUZyF36UxK7Vn-ZLBDCc5T3gTXD59UiwyW2fAbkyOtuwifjd5QhOdV9IqfuPe396Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddad2c1542.mp4?token=mvvYlJ7Jbm4IG3pZiGAFVICNhTKw52LSJA6tDyiaZfr2xxHd8eSG-pRZDsUAc7N2DjYA1HGwiDHZhT8PhzRGTvizqjCH8Q1lQenpBUZpwqNeErUngaqFCrXJuqBTIOdjLAsWS-QsHJLqm361VwKq3KWCJ5AIOY3JTUzdGVxe0gBXXst7g6pTz0_mSrTjg6E0znAKwIrUZOJ0NM_rZaQz15p-a-_P6PbCf0UpJEQ7yvry-fsK-pdV6JbvdLMtiNvnWpIdBHJUTd8ALJt7FVnhtOUZyF36UxK7Vn-ZLBDCc5T3gTXD59UiwyW2fAbkyOtuwifjd5QhOdV9IqfuPe396Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای انفجار اربیل را به لرزه انداخت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/672290" target="_blank">📅 23:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672288">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
محسن رضایی: اگر فرضا دشمن توانست در جایی پیاده شود، چطور می‌خواهد فرار کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/672288" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672286">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9ZiDaOYklRoOsA4j7eUL8tUiF2gBPCwxTgR3M8iNuADWHqV3Hs3HXMX1O2p04UwIEvuGAvTnLcXxAWDX30EAAAxOap_LnfdqTqVFgAu5g6ozKrHTvz06517c3kbTi54QultYovweci6WC6QujLrQvrHHP944AHK5GzEiNmGDV6EAmNEL1tsUltYqO3MmYc07X5pJZYA2hnUQ1HSkiqCqbiEZ-y4mh9JGpWUHEtDevpkfxAfW4yHzkhPzviekfgyRVBqAskzJGwiQC2oFLFS-mu9HHH0IfROuOC4cLOmzB8hkJUxh8W0I5gkoyEOOgqRvBkkrAbQVQj3_amuYSdezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQAUS2mg15fpZLs3DGKSajXuzfkxIfuYFSC4lOudD27rLYGSJwik_ecNRzPvMynCbnUIG74vC6w26RsUKk0XO0uPsUxGhauwHpM1sh6F8egkl5j2YZ_6Tg9JPqXh7fHhKmoYUBj6DUtTa3FDBUSg3H3A9SeITdr-7kVXJq1hJ4EcXzSgsSVx6-104xDcQFvEThfe3TcdWwml6NM3TnAvxSBl779oC2lmMFjAr-06_WfmeYkRJLVI1ys_g6yzhqLz19sGxyh3nMobAZvH0qXJkL03cYqXvcdqwmSlL6CESr6zBH8wHFKElts5KGFi-cXNB7TL42QqxCwnSHHMdWGxlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی: تعداد زیادی از آمبولانس‌ها به مقر تروریست‌های تجزیه‌طلب در سلیمانیه عراق روانه شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/672286" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb16946e3.mp4?token=frG_CeHUbBp63lG8u_F1hSFJ2tPb_zic6AYwDJv2gCmNhG8QJA9XTgRVSvoThwuBPy4awfuad6o4ABJhw45LDhlLMEouXEl5bFu4zrNrpnRZutc4W3TkMIDLQnwYAFu1rlK6BiE8ZTG48DIJGMnx70DDz7O5C5nTShXqjet73c50MYDIlwyvy3XH6spxfbb2WaAdYuqW-PHiD41OGm9v8Ll7_IzfPKGk3u_aNdLGJLiPEo_pfH9gaW27_gUHDAK0Lg9tcaZAK5N9w6uP4K4dWiPOnTFRSHqRCdzsWZJFVHMkRiUJvea-gW7GRB8yADlaG6ueYEjg6b-tEgYptgAwww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb16946e3.mp4?token=frG_CeHUbBp63lG8u_F1hSFJ2tPb_zic6AYwDJv2gCmNhG8QJA9XTgRVSvoThwuBPy4awfuad6o4ABJhw45LDhlLMEouXEl5bFu4zrNrpnRZutc4W3TkMIDLQnwYAFu1rlK6BiE8ZTG48DIJGMnx70DDz7O5C5nTShXqjet73c50MYDIlwyvy3XH6spxfbb2WaAdYuqW-PHiD41OGm9v8Ll7_IzfPKGk3u_aNdLGJLiPEo_pfH9gaW27_gUHDAK0Lg9tcaZAK5N9w6uP4K4dWiPOnTFRSHqRCdzsWZJFVHMkRiUJvea-gW7GRB8yADlaG6ueYEjg6b-tEgYptgAwww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادهای انتحاری به پایگاه تروریستی آمریکا در شمال عراق
🔹
خبرها از حمله پهپادهای انتحاری به پایگاه نظامیان تروریست آمریکا در اربیل، در شمال عراق حکایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/672284" target="_blank">📅 22:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deafedf62.mp4?token=sKvRgibUgbqIoGSQnwAuybkCRp2QO4jp7DBynEc8JVy0QEYKYIIhF07MwxH54nuFWBXsoqNgiOHiaNcWine3D4kYL8FroiHtTEHwqMQs8TQCGsw2RDFZYLfEg8WtsLFXfH1JeMy-dE5-wYpO-B28sycNuBJ-KtmtVziNO_hMOpNwaaorT4eZaJ0_RSgpW8OG1Kv54XPyBNRsqS8FK4-Dk1Qzauj8fT2vAVx71nTrht_aOVdVQBSGxf0zCs1S1ItKh16KrzZMjADfOMp0zs7Fxo_Z7p9FAR5_JPA7ZQm3I20t1ICvkr9BZTWYLu7njdnwktvSb4v9rxf-BOZ75tuMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deafedf62.mp4?token=sKvRgibUgbqIoGSQnwAuybkCRp2QO4jp7DBynEc8JVy0QEYKYIIhF07MwxH54nuFWBXsoqNgiOHiaNcWine3D4kYL8FroiHtTEHwqMQs8TQCGsw2RDFZYLfEg8WtsLFXfH1JeMy-dE5-wYpO-B28sycNuBJ-KtmtVziNO_hMOpNwaaorT4eZaJ0_RSgpW8OG1Kv54XPyBNRsqS8FK4-Dk1Qzauj8fT2vAVx71nTrht_aOVdVQBSGxf0zCs1S1ItKh16KrzZMjADfOMp0zs7Fxo_Z7p9FAR5_JPA7ZQm3I20t1ICvkr9BZTWYLu7njdnwktvSb4v9rxf-BOZ75tuMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: به هیچ عنوان از انتقام خون قائد شهید نخواهیم گذشت
🔹
امنیت و آرامش آینده ایران در گرو تحقق انتقام خون رهبر مجاهد شهید و شهدای مظلوم جنگ‌های تحمیلی است. #تقاص_خواهید_داد  #WillPayThePrice #خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672283" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaEhcT3yD3yXdofGtWiIFO9TYv5RONJepzN-bbn9RegD28zUN6T7bmI-qEk0IlD7GHvtsZyFexSsaACWma3B1T01rT6hSOIPJvPcVQxKbqpqiVjHB33t9aqgK6oWh5R3-ecKnjr0TOXjFXNhN0P6QrWICSov-5B2xh9ocrnlVdS4DyG8B8dEYChHu56CiJeHnWONCEsaz9-V9cuGeva2CEtxVzKzH1ToUJNV2xuGIhlwPoq7tjzNy7q433GOFKbn5q_7vxyFrIkTuIOm2FhjaFiDFsv5Z-_x7nTh8K7vlsuLPW61CFfGT8QVtk6r7xEfQ_lv3HynXIMxRFgJVfzhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCC1FLVHa6MrQkc6Ed8zT8Kw8EvLHBFgLf_GCRr8axQ0dLp-PUn5jR4ES_77W-HPT_T6nA9ACxbCJwy6PRY95PCcNW_7NvyiicYWNgerkORJP3L2a4TiFnsVlmppvExN-3mDrpbjuHZ9TY7CqwkMPYQ0H9FTvt4-o2APLz1l_DQnPicU9Hq4hhlyKncCDkqQfpFMp2XBmsGXxJ6crD4jFtkvSK5SaL-YxsI-M15H4npGWqRO9eu3L7az85onDXPxyaLF9rAhMK0OP61vKMKqAOI8NPBNWcJW-fc3WmVrh0SNyzQJwMISLoCOWZr-Fd-mmi6j9rTHC9K-mOwYlLlIpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
استوری بیرانوند در واکنش به صحبت‌های علی دایی نسبت به تیم‌‌ملی
فوتبال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672281" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: به هیچ عنوان از انتقام خون قائد شهید نخواهیم گذشت
🔹
امنیت و آرامش آینده ایران در گرو تحقق انتقام خون رهبر مجاهد شهید و شهدای مظلوم جنگ‌های تحمیلی است.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/672280" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صداهای انفجار در اربیل به گوش‌ می‌رسند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/672279" target="_blank">📅 22:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672278" target="_blank">📅 22:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672275">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01892723ac.mp4?token=RtwDg75b8WJRYjyey3jcz0FNnBS_vm-0yuz-8ArADJsGgCHLMapqbciwILubC6orStLZl1qK2WL-2id_KwqCmhY0Na4u9euKSYiXib9Iyeyja2wC5xRmyaoSFaRWZoZjRfCcd918ulTpvDHrK4EK8ysPFoH9XObfzHqAO-UB4NMLojLwpSBdCRlX-ZbSQ-UQoYWllN7iEHt6QvGUSCAg53XNDOHF81kev1yNugEK8p3zzFW80KhQRtLgJWnFL_Ur39StSg6kr9GkB_EatFnaNf7r57JZuRBDsNLoO6VbVBWnq-srGLL8-6bsUL68OdYW6YSV8zh6tr69JAKnSIsmDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01892723ac.mp4?token=RtwDg75b8WJRYjyey3jcz0FNnBS_vm-0yuz-8ArADJsGgCHLMapqbciwILubC6orStLZl1qK2WL-2id_KwqCmhY0Na4u9euKSYiXib9Iyeyja2wC5xRmyaoSFaRWZoZjRfCcd918ulTpvDHrK4EK8ysPFoH9XObfzHqAO-UB4NMLojLwpSBdCRlX-ZbSQ-UQoYWllN7iEHt6QvGUSCAg53XNDOHF81kev1yNugEK8p3zzFW80KhQRtLgJWnFL_Ur39StSg6kr9GkB_EatFnaNf7r57JZuRBDsNLoO6VbVBWnq-srGLL8-6bsUL68OdYW6YSV8zh6tr69JAKnSIsmDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: سیاست هم مذاکره هم جنگ تمام شد؛ اگر آمریکا طی ۲-۳ روز آینده آمریکا جنگ را ادامه دهد وارد مرحلهٔ «تهاجم و انهدام کامل» خواهیم شد؛ به طوری که پایگاه‌ها و سربازان آمریکایی در فراتر از مرزهای سیاسی هدف تعقیب و تهاجم مستقیم قرار خواهند گرفت
🔹
رضایی…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/672275" target="_blank">📅 22:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672274">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
محسن رضایی: ترامپ پیش از خروج رسمی، با نقض بندهای توافق و حملات نظامی، تفاهم‌نامه را از بین برده بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/672274" target="_blank">📅 22:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672273">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5205697d3a.mp4?token=c4jAuGgzxxC-7F8xpzvKjjASqufhOTqfLl1SH7Pt-ptCXkFXNvEjUlyAyaxBv912N36T0QoG3yd2Iq_8MGCNM9yvfqeB082HYp9jAMymsJTXi0vUycxOkEmOOwbaXPeMChHd5TcKjcchKR2zIgWFge9DS44v10xZXmSYH1NGiLy_z3XRkdiVsW15LRzAGxO9NCA9uBiRqgVDVR6Fp35elkpl1kRqOvE6KlwAX2iQCmmyd8spwG-pt3woTnj8FUcrAjpjU2fVnycV5P0de5hYP86V4tYQzoOqfklto7MnNdfIiYb_vpLv3fEBdAgL1vB9SZbO217qsg7mTIeNuS6v50XkvT4iGlI--NrekhwohRYW_uVqQC3wlURkvOkBAJEA_FWNcnUvk0K5BrDZl0odJTSHHnO_fGMa97ZybMpwe_01hV-Ad7Hz6v5JT7tw5h9bOP37l8KvyOJ5fD346PO99URCAv8bZNEkJuAnwbUSTQQY_8slbCXhx6pjdApzcNNC-aIlhayAqA2IAHL1TjiEj3hJcZG0-4CPB8v5TnUF5YD2xZZofazHMPN5cpShkuIiYKwDpyw-xsLqL5SGxD5xVdTxvKKV7-B_2e_xl2Lzsud9R7IWEpiCPXqN3-IHABXWOuZlS5PvJyaMd-IOYebeKvx7GwW34mo9vfo33TtQcUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5205697d3a.mp4?token=c4jAuGgzxxC-7F8xpzvKjjASqufhOTqfLl1SH7Pt-ptCXkFXNvEjUlyAyaxBv912N36T0QoG3yd2Iq_8MGCNM9yvfqeB082HYp9jAMymsJTXi0vUycxOkEmOOwbaXPeMChHd5TcKjcchKR2zIgWFge9DS44v10xZXmSYH1NGiLy_z3XRkdiVsW15LRzAGxO9NCA9uBiRqgVDVR6Fp35elkpl1kRqOvE6KlwAX2iQCmmyd8spwG-pt3woTnj8FUcrAjpjU2fVnycV5P0de5hYP86V4tYQzoOqfklto7MnNdfIiYb_vpLv3fEBdAgL1vB9SZbO217qsg7mTIeNuS6v50XkvT4iGlI--NrekhwohRYW_uVqQC3wlURkvOkBAJEA_FWNcnUvk0K5BrDZl0odJTSHHnO_fGMa97ZybMpwe_01hV-Ad7Hz6v5JT7tw5h9bOP37l8KvyOJ5fD346PO99URCAv8bZNEkJuAnwbUSTQQY_8slbCXhx6pjdApzcNNC-aIlhayAqA2IAHL1TjiEj3hJcZG0-4CPB8v5TnUF5YD2xZZofazHMPN5cpShkuIiYKwDpyw-xsLqL5SGxD5xVdTxvKKV7-B_2e_xl2Lzsud9R7IWEpiCPXqN3-IHABXWOuZlS5PvJyaMd-IOYebeKvx7GwW34mo9vfo33TtQcUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: آمریکا با نقض تفاهم‌نامه و حملات نظامی، از فرصت آتش‌بس برای بازسازی تسلیحاتی خود بهره برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672273" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672272">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
محسن رضایی: آمریکا با نقض تفاهم‌نامه و حملات نظامی، از فرصت آتش‌بس برای بازسازی تسلیحاتی خود بهره برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/672272" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672271">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84851cccf2.mp4?token=EoKWhwdjIfxYMwUAdZq1oun1JKtV8miPVlX0WCSuirxwx1wdEnULi95iZj14x3bIl9h9aHlrunEHdkQRLbYATLWqszw19ujpEHhMxr7r8EQ_9EsQaCsq6lYRu8CnmWMsfa0Q8DJ9GXY6lwZswqZtmdqKkHyKuLQ6KR7Ei59uRCIm7tbMWwrpWwCGdJK6_EAymeaGhzPqz7J1P0MoGYOfOEWD76w9OA7rmwkD-CTsdgydRwWXPPp64R7WZnte6MhKcMVyfYvaxxUhFA2NjdzPqYm-TMc-DDrB6ETZHrhNDcq2HDtujDtZPVqtClQKNHZuchQBBXPkMCbiePG1DzBG4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84851cccf2.mp4?token=EoKWhwdjIfxYMwUAdZq1oun1JKtV8miPVlX0WCSuirxwx1wdEnULi95iZj14x3bIl9h9aHlrunEHdkQRLbYATLWqszw19ujpEHhMxr7r8EQ_9EsQaCsq6lYRu8CnmWMsfa0Q8DJ9GXY6lwZswqZtmdqKkHyKuLQ6KR7Ei59uRCIm7tbMWwrpWwCGdJK6_EAymeaGhzPqz7J1P0MoGYOfOEWD76w9OA7rmwkD-CTsdgydRwWXPPp64R7WZnte6MhKcMVyfYvaxxUhFA2NjdzPqYm-TMc-DDrB6ETZHrhNDcq2HDtujDtZPVqtClQKNHZuchQBBXPkMCbiePG1DzBG4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه تروریست‌های تجزیه طلب هنوز در آتش می‌سوزد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672271" target="_blank">📅 22:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672270">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEzdvcRDzzC6bdRGC8ei9b91Tz14SJYmtmd3bG5veQ1Vmolkx0hqkl3RyKO0nhLLhQ2yaqpa3irnXd6Wivp9tQQs0BhL1hEo3-v4Ddak-4Y0OExonzVd_xLVkN5yRnOK8xbiOUGeHW8OazeNn4YIzhJXWLpYy5CxWM_S09IRLZm2csrTY8OEGGJk9FZgaYpW345EoU8DT_TehX3e9-YcrE4_BT5XmrEsMeJWXASLI3YpvT-t2DeahtAkpFIXi7JomTtYhEp9o2WbHX9FhPDPEfKjYPRgZQQkulYK_4je-KrgwkSQ2CIzSyAaKT8E0WsvEaBenAVhqY4TwdeEYRmlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای همدلی با مردم شریف و مقاوم جنوب؛ ایران وطنم
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و با لهجه شهر خودتان، یک جمله همدلانه و امیدبخش خطاب به مردم شریف و مقاوم جنوب کشورمان بگویید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و با صدای واضح و رسا، پیام حمایت و همراهی خود را به گوش مردم جنوب ایران برسانید.
🔸
صدای شما می‌تواند روایتگر همبستگی، غیرت ملی و ایستادگی مردم ایران در کنار جنوبی‌های عزیز باشد
👇
#ایران_وطنم
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672270" target="_blank">📅 22:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672269">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پرس تی‌وی: هیچ پرتاپه‌ای به محوطه نیروگاه هسته‌ای بوشهر برخورد نکرده است
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/672269" target="_blank">📅 22:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672268">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اعتراف کویت به اصابت موشک‌های ایران
🔹
کویت به اصابت موشکهای تلافی جویانه ایران به دو موضع در خاک کویت و به آتش کشیده شدن آن اعتراف کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672268" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672266">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC_JddAQkDjl6ryra3S_QKQsyiGMjWcQdWgtxDTQrOnXbJgFJd7Ya0MuWWqfMcgKiq_cx5aci8qRVoFlnqhI4g9wU3Brh6E11KEH3N_wiHKqcbbnfwlXYFTiUmCySUSVAa1789L3uP9A0PmwzFaDIBVNLi9CLwVaC-mJ-GM5wXpsYxim4xHB0SxfE20DA-tfqs4SLBTfWiGyUAPHurICrPgAeWshTmrvJrGjThK2LnyA6hza4uctpM35-hHlTLCJRNV3JFGtmc19viYm_dfRqFGufDAkO9Og-DlxQsaCbEMEtZsWtFFD8a3PmMl5aW6Y98LZeymonujuMAaQ6ItTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672266" target="_blank">📅 21:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqJzU9-S5lOjo-svVK4pQUsmRZEvqrh5xeopDykpjZjcjW1nUXC6kGu59ZdMDWz_bn0AzaNqZ5zo-FQeZZxGgILDOPzpCFwHg1IKHuzCZNyKhpgTnXG_ZoGd6yF9JEkbn09Pix35JnrMLtDigUTEGWMTz2MGf-uURBlEbQPC63tADcAE5LYmW9eUaRyB8bEa0rSbOjgtUurMahTHiXa6e6KwK_bXr0_BzwIh1rFbRYxarBPP6qGUt_hJGepAkC6AZpCRLyBj2F_sR9elDtyAQJuynSMnjUwKQBuKIAJIGMKtqd4G5TR4lremw9nI8W0NawaaC54aQ6_ZZdg5Kpl45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت بورس امریکا در لحظات آخر این هفته معاملاتی
🔹
ریزش سنگین بدلیل درگیری‌های تنگه هرمز.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/672265" target="_blank">📅 21:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c71764ae7.mp4?token=Y9AumAVJQWJzyENLnUBqwVKKKDxv5HZuBcJXIE_sScyuS2jFxx8CwavF1koRjwSr9hFM5CkQK30zdBpK_VHIlPOMNX9H6b_-ObVT7Q7SGnBKZuESD447Nx9XerJ99h71fk1n7BVPZPwwTMPVshk5DlmN3iRB1ZB7Su3V73dkTlx5U7frp7oPfhF0E2dIoM_TxPvnWt_Ani7t7hQBpl0qUlgThaeA5EVzK6qWoJrpDvXiG8QlmbB0er2TSnnbfGFetJ5UQrbGgaY3-jMphh0QIBPMOP6dS--LVCE2AznbOesowCcnrBO4D2OJwoUn8c2ba7XbxaonxHPrdvBNuNrJo4Y4_2I81-Vi8bj_ZDcc8UfuovCJkQGg-rKVzrZEO7bY1b6C4ouQlTdBHsgl2vwb6r3fRLneSuXFo0oEfvfmvH0TDBpuzcHq_AsL-LqkYrw4gPFRSs7GD_PJpS9IDeXs7S1UyW4XKybyXQQyh8wDzPyxNm7MQuD5-1CukgKKXHbqDlL0TZsZhQwVkAObdYucys_FXcVgnYOJm2OAU80nhoTjA6LnhrAsmqgkBgsOkaqBO-Md_o6TGqcUq3Oj_JNY3SXbSj8GBes6vbzE66oghokMgaMhTJK3r9gjEi6JW5o44jvbT2U0i6_73vEYZwGmV9c_P_4GUgaHbIECJdlPr_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c71764ae7.mp4?token=Y9AumAVJQWJzyENLnUBqwVKKKDxv5HZuBcJXIE_sScyuS2jFxx8CwavF1koRjwSr9hFM5CkQK30zdBpK_VHIlPOMNX9H6b_-ObVT7Q7SGnBKZuESD447Nx9XerJ99h71fk1n7BVPZPwwTMPVshk5DlmN3iRB1ZB7Su3V73dkTlx5U7frp7oPfhF0E2dIoM_TxPvnWt_Ani7t7hQBpl0qUlgThaeA5EVzK6qWoJrpDvXiG8QlmbB0er2TSnnbfGFetJ5UQrbGgaY3-jMphh0QIBPMOP6dS--LVCE2AznbOesowCcnrBO4D2OJwoUn8c2ba7XbxaonxHPrdvBNuNrJo4Y4_2I81-Vi8bj_ZDcc8UfuovCJkQGg-rKVzrZEO7bY1b6C4ouQlTdBHsgl2vwb6r3fRLneSuXFo0oEfvfmvH0TDBpuzcHq_AsL-LqkYrw4gPFRSs7GD_PJpS9IDeXs7S1UyW4XKybyXQQyh8wDzPyxNm7MQuD5-1CukgKKXHbqDlL0TZsZhQwVkAObdYucys_FXcVgnYOJm2OAU80nhoTjA6LnhrAsmqgkBgsOkaqBO-Md_o6TGqcUq3Oj_JNY3SXbSj8GBes6vbzE66oghokMgaMhTJK3r9gjEi6JW5o44jvbT2U0i6_73vEYZwGmV9c_P_4GUgaHbIECJdlPr_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع پیکر ۲ شهید حمله آمریکا به بندرخمیر در اجتماع شبانه
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/672264" target="_blank">📅 21:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f219ddcb5.mp4?token=gKQId9XydBoAE1tYCSNLt1twd9HgsJ1ndfqES7i5jiZFIewhJ_7TnPfReQcOxLnmJY4oL1B99DquszvN74ZFmu3i0k4_ttk58piBMfWUA38gLLUEk1BbydS1dEeH5LUtYNGEBIehRZqtm_dQnq_uQ8PVOy6FjDLA41nSJuUj079cwPwzom5SDClA4zzhUWawG1mc2C4c8p5isVbzVHzr5KmP9u0qlwmbMF9gXIMIRPV0Mtpwc88loybv5_oaLHN4DL_7IWHBYpuQIviQjlAHF9Szi0sGnPB-j26TNa_hnfPUPVUmmFirYexTSH4JPWgMzonYXuCdhcLU7lPNN6mKAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f219ddcb5.mp4?token=gKQId9XydBoAE1tYCSNLt1twd9HgsJ1ndfqES7i5jiZFIewhJ_7TnPfReQcOxLnmJY4oL1B99DquszvN74ZFmu3i0k4_ttk58piBMfWUA38gLLUEk1BbydS1dEeH5LUtYNGEBIehRZqtm_dQnq_uQ8PVOy6FjDLA41nSJuUj079cwPwzom5SDClA4zzhUWawG1mc2C4c8p5isVbzVHzr5KmP9u0qlwmbMF9gXIMIRPV0Mtpwc88loybv5_oaLHN4DL_7IWHBYpuQIviQjlAHF9Szi0sGnPB-j26TNa_hnfPUPVUmmFirYexTSH4JPWgMzonYXuCdhcLU7lPNN6mKAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت یک مادر و قطع دست کودک یک‌ساله در حمله آمریکا به بندرعباس
🔹
در پی حمله آمریکا به محله «تپه الله‌اکبر» بندرعباس، یک مادر به شهادت رسید و ۸ تن مجروح شدند. دست کودک یک‌ساله این بانو در جریان انفجار قطع و وضعیت وی وخیم گزارش شده است.  #اخبار_هرمزگان در…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/672263" target="_blank">📅 21:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72169cd2e.mp4?token=OvSM-L9sd6lmE4ICsmdiP9g4G0F0ZJuyUb3nHwcRYZBSHJLzidLyV643WCnVZwwD15kPyDAwyDnUUwOzfRQa1LJs3-fjWDm3UGyHia2HsbJ_FGJ-Y4COYWhTrRU2ci-wy--Xw0EmdZpoVvtdJyT1OlscTHYQeOVTsHnhaKzV1YvpQGgbLS8Sg6rc5LU3hZRJvD_53vW0lUMMiiC5zN0JkGThiNC5DaY5Ex3etKGwvtGIa3Qjeabl4mfNOgc3i-bQkmz5hXmGzr5ABzMMQyWk1LjlxkI1H7KJGz7obJJoZ46tnDS1mxaTOM_Ez1CT0JOxRRefWEMgZv-Y6eJMuZX57g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72169cd2e.mp4?token=OvSM-L9sd6lmE4ICsmdiP9g4G0F0ZJuyUb3nHwcRYZBSHJLzidLyV643WCnVZwwD15kPyDAwyDnUUwOzfRQa1LJs3-fjWDm3UGyHia2HsbJ_FGJ-Y4COYWhTrRU2ci-wy--Xw0EmdZpoVvtdJyT1OlscTHYQeOVTsHnhaKzV1YvpQGgbLS8Sg6rc5LU3hZRJvD_53vW0lUMMiiC5zN0JkGThiNC5DaY5Ex3etKGwvtGIa3Qjeabl4mfNOgc3i-bQkmz5hXmGzr5ABzMMQyWk1LjlxkI1H7KJGz7obJJoZ46tnDS1mxaTOM_Ez1CT0JOxRRefWEMgZv-Y6eJMuZX57g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه تروریست‌های تجزیه طلب هنوز در آتش می‌سوزد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672262" target="_blank">📅 21:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ0IhmcK3z82EF_otNNqBxCCJRjSekXz87GyBKYdDhShYpcVOdDuzNzr0xo-ZOiUK5ePdXd73GnUGB-KM5FpkXJ9bVTitQZVd7yS4oaSK-kfDyeRM2XBdt_hrDbyK7-ugQ31uB-v-akQOX1u7Q1q5rcHzRAibKir33KKCvEZk2PqyNYfFe7DIGzXWO4ZLtZkn3p5tg3VwcW1u2dYD-6XKxizgypsjNpOAobqt8AFVmH3D5tcAb4Gh1-SG6rtuu4WTgXMCGXEFIFvVf3YVVYOIUMMnXMDgIRKrqrICTxrB1oLJZeLoMy4CdsanJkHquyrTDmjWaST9FkyL3GiT-ckMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جهانی نفت به ۸۸ دلار رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/672261" target="_blank">📅 21:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf1d7b71d.mp4?token=YimTECpT8u094D7CnD0Mrlc4Uig8a4M3wgHgklzbmhugRNW93mG_NAbX17VrJKDt9kV3d8X8dW7rPLIBytwyH3lrgR7F5IWIgRa5qN8Vj2pcJ_n221NQ3mOOxiM9uXud3p_XkSHB9nZylqVg1_v8X4Ip8uRTfaK4xA0D74kE2h7nMduWiQY3Bky7L67XBzMCOswuOU-JxIF3M0GVYgKqJdElAi3szUL_j2uOoXG4x2MciMxDW-8CZBt8ozfRLLoJarxgbCQgAZLNMOle5YCH35_J2E4gCdr1RO0v78c-NnSIfTNRB8RAoTPcYUqaQo8b7iGJOM2Y1BGjhpEk55JT352OR99zOJnNGWnOosOuEiu4FAnXxfrJUW4natQYvNzLAyrr8YeOdrcjc2HuNhx-d8hjzjxiWRyBoX7QCEmfn8VYDiDBUrZIhbjJtNft52XZa402I8sqglzjFo9PtcDU9TRvMTbg-rDXV4s43Wsu31Oc04ciY5hlJ2TbfELre3oRu4y8wS5cH-mEIx66RnBe50cszNeUTJoaRrtlU2RDUEKFFoiAFGu4qKam6oMfbdQ0Nh065WChtZRz0p-dtFlFDcfUFpc_-j74R4vaE5EWOCB7chB45bgkI3_SNI8CUfRvVZmaTCxPTkawrq9B7E7RMOmT074Iga-5TUM5hu9WQz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf1d7b71d.mp4?token=YimTECpT8u094D7CnD0Mrlc4Uig8a4M3wgHgklzbmhugRNW93mG_NAbX17VrJKDt9kV3d8X8dW7rPLIBytwyH3lrgR7F5IWIgRa5qN8Vj2pcJ_n221NQ3mOOxiM9uXud3p_XkSHB9nZylqVg1_v8X4Ip8uRTfaK4xA0D74kE2h7nMduWiQY3Bky7L67XBzMCOswuOU-JxIF3M0GVYgKqJdElAi3szUL_j2uOoXG4x2MciMxDW-8CZBt8ozfRLLoJarxgbCQgAZLNMOle5YCH35_J2E4gCdr1RO0v78c-NnSIfTNRB8RAoTPcYUqaQo8b7iGJOM2Y1BGjhpEk55JT352OR99zOJnNGWnOosOuEiu4FAnXxfrJUW4natQYvNzLAyrr8YeOdrcjc2HuNhx-d8hjzjxiWRyBoX7QCEmfn8VYDiDBUrZIhbjJtNft52XZa402I8sqglzjFo9PtcDU9TRvMTbg-rDXV4s43Wsu31Oc04ciY5hlJ2TbfELre3oRu4y8wS5cH-mEIx66RnBe50cszNeUTJoaRrtlU2RDUEKFFoiAFGu4qKam6oMfbdQ0Nh065WChtZRz0p-dtFlFDcfUFpc_-j74R4vaE5EWOCB7chB45bgkI3_SNI8CUfRvVZmaTCxPTkawrq9B7E7RMOmT074Iga-5TUM5hu9WQz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اصابت دقیق پهپاد تهاجمی نیروی دریایی سپاه به یک فروند نفتکش متخلف در تنگه هرمز
نیروی دریایی سپاه:
🔹
تا پایان شرارت‌های ارتش تروریست آمریکا در منطقه، تنگه هرمز بسته خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/672260" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672258">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27926a0c3a.mp4?token=v6_atXnq_OEMpGfQY2tmKWIYcd-1pQz4E0AHpNIjSuO5B4Ol-GP_GS0r8cJThJoh0-cwbS4eQ-1xOO6GWh4GmWUP8bmMpiqj2dWnX4oHTJrs6Vu73qqHGabCO9VJRAgx0RRntY8C_9n82UBrtYdw4tNHGCGEQOOAuwNfcfecyIa0AcHqQ1DtKnGjOC99Oq5YBDhxcvsm0cpL550L9F52LSHW2Zf4cYHBo2sqzIOzzetRwE3fmaGaPXGdRHxUlEpdqrTzBrT1KrEPobSh0HemIzKE8kC9s337nYGmYEMSqj5xe5uD4C3Lm9I9e4d594hTeBZHE2TGKjuiUjd0ZNZrig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27926a0c3a.mp4?token=v6_atXnq_OEMpGfQY2tmKWIYcd-1pQz4E0AHpNIjSuO5B4Ol-GP_GS0r8cJThJoh0-cwbS4eQ-1xOO6GWh4GmWUP8bmMpiqj2dWnX4oHTJrs6Vu73qqHGabCO9VJRAgx0RRntY8C_9n82UBrtYdw4tNHGCGEQOOAuwNfcfecyIa0AcHqQ1DtKnGjOC99Oq5YBDhxcvsm0cpL550L9F52LSHW2Zf4cYHBo2sqzIOzzetRwE3fmaGaPXGdRHxUlEpdqrTzBrT1KrEPobSh0HemIzKE8kC9s337nYGmYEMSqj5xe5uD4C3Lm9I9e4d594hTeBZHE2TGKjuiUjd0ZNZrig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل انبار مهمات تروریست‌ها/ الان سلیمانیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672258" target="_blank">📅 21:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672257">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c411da7d.mp4?token=Z3uMU5PcKGbk8v_o5U0IoG7EqsCPaF67sCfhMP5PkqmtscEViu8bSnnicpfqBYT6w4CDKioTCEJYtrOM8rCEn5dWIa1Md6vjJIojywCulv01ipNLd7A4nGB6OLDCqpKuSZnfrP8dZqJ2RBHvvmDlSmJ9TJ1fLfEZMZsL43N-tvWBn2nAtYZK_VgA0yPm9xWU3C-tbsXJ3EkZkHtJnkeUKvKjpLEErCz3dOp6rRxiX5r2IbaC3paL3gz0AbHE0vUQGf7E7koAmKyKzjZC5w5JXvhDaj-RsZmMf9yC3ALB16CXZuytIoU3RpILNOsCC4Ipt3hNpLMFpkO-ZeqKjvHnAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c411da7d.mp4?token=Z3uMU5PcKGbk8v_o5U0IoG7EqsCPaF67sCfhMP5PkqmtscEViu8bSnnicpfqBYT6w4CDKioTCEJYtrOM8rCEn5dWIa1Md6vjJIojywCulv01ipNLd7A4nGB6OLDCqpKuSZnfrP8dZqJ2RBHvvmDlSmJ9TJ1fLfEZMZsL43N-tvWBn2nAtYZK_VgA0yPm9xWU3C-tbsXJ3EkZkHtJnkeUKvKjpLEErCz3dOp6rRxiX5r2IbaC3paL3gz0AbHE0vUQGf7E7koAmKyKzjZC5w5JXvhDaj-RsZmMf9yC3ALB16CXZuytIoU3RpILNOsCC4Ipt3hNpLMFpkO-ZeqKjvHnAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار رونالدو با نسخه کودکی خودش در فضای مجازی احساسات میلیون‌ها نفر را درگیر کرد
🔹
این شاهکار که توسط هوش مصنوعی ساخته شده در فضای مجازی نزدیک ۲۰۰ میلیون ویو خورده و خود رونالدو هم لایکش کرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/672257" target="_blank">📅 21:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672254">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5aeae1ea.mp4?token=pK00EMYcq30s9WehEYco21wBRhBWhsu3wIMGSpyo8XhxGy15OQHkjgPQ5UFVMviOlyqRo2zEBt291bEkZKJ9UeSFORDHc68X6gSe_v5dJpTZH_25X10r4vWcenlTPfb2oeo5sP3zQBj2MdDbG2xMBw7klU7A9BOO_tQ65WM6c8Kmw7j39PvlXpB9NY3slQgVpAJow_gIHYlAmcUSd6Jm3hiIeAPYBUxiGi8myLTeDqQPN6StDhtVGbeNodcOEAVn14kZdMM9eHdsklyPS-qXxcaqSbY_KD0z6cGZ4YPVLOT05STX7N4ZEaI515zMM5bE69PvDg-0Re7PCI0dqTQ4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5aeae1ea.mp4?token=pK00EMYcq30s9WehEYco21wBRhBWhsu3wIMGSpyo8XhxGy15OQHkjgPQ5UFVMviOlyqRo2zEBt291bEkZKJ9UeSFORDHc68X6gSe_v5dJpTZH_25X10r4vWcenlTPfb2oeo5sP3zQBj2MdDbG2xMBw7klU7A9BOO_tQ65WM6c8Kmw7j39PvlXpB9NY3slQgVpAJow_gIHYlAmcUSd6Jm3hiIeAPYBUxiGi8myLTeDqQPN6StDhtVGbeNodcOEAVn14kZdMM9eHdsklyPS-qXxcaqSbY_KD0z6cGZ4YPVLOT05STX7N4ZEaI515zMM5bE69PvDg-0Re7PCI0dqTQ4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانواده‌ها در منطقه تسلوجه سلیمانیه خانه‌های خود را در نتیجه انفجار انبارهای اسلحه ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/672254" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672253">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
انفجارهای جدیدی در سلیمانیه به صدا درآمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672253" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672252">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a36259b44.mp4?token=k_S6U4__3ygFUN5Y_ltng4xQGPnIAXwU41yVmhZXOUBoIvaQ9VCQSfqrLGsuedWEyGFeXW4K2ZXsMdcBlr0w3Pl07akKHTTUsqHcpkWbgz1xlxjsrycl3KCthBceQ0V_dsolGLolrxiirG99iYnhgryTsCQpPKSMUvt3hrGJ_VlDryLG1SlSZrSVSxQhz0Rofw2qLYVk6lj4bBVLroztGUsvRGF3vltWiPopghMed4PtdJFKcIsnc938jgxq1pQDLwTZWllOB_fSgBI2kI_6kdebCUb1KzkeX0nzt5hdCgyW1zI1kBFEF06apmilWSh3Aik5l3cUa9IfHv6h-oQ1iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a36259b44.mp4?token=k_S6U4__3ygFUN5Y_ltng4xQGPnIAXwU41yVmhZXOUBoIvaQ9VCQSfqrLGsuedWEyGFeXW4K2ZXsMdcBlr0w3Pl07akKHTTUsqHcpkWbgz1xlxjsrycl3KCthBceQ0V_dsolGLolrxiirG99iYnhgryTsCQpPKSMUvt3hrGJ_VlDryLG1SlSZrSVSxQhz0Rofw2qLYVk6lj4bBVLroztGUsvRGF3vltWiPopghMed4PtdJFKcIsnc938jgxq1pQDLwTZWllOB_fSgBI2kI_6kdebCUb1KzkeX0nzt5hdCgyW1zI1kBFEF06apmilWSh3Aik5l3cUa9IfHv6h-oQ1iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانواده‌ها در منطقه تسلوجه سلیمانیه خانه‌های خود را در نتیجه انفجار انبارهای اسلحه ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/672252" target="_blank">📅 21:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvBIBGVjqzG0Gp9Md4WWrOkzsJFZzxypRS0LBiZXB8WTMw2fpFC-x8BIr3hoYP7Q4EcMDCHf3htxDXLoxzON3y80rCxL2NebNmbL_tNVlLvE_uwvwSkT_XDdCCXoUCQL0Mrm67KumohHRpJU7ufWuiOGOfysYQBCV_I7rSqOoA44lsu48iOoq0IDFS1fQSpkh58KmOYxzAfQI0hEDLv980pNsY1IGpEcGM9FN2bJYn-GzJ4lsFd_AgjI1cXr9CR16YXCcoislV7PK-DpuaQSvFXM6M_atF5fusC1W7N5Yil1bsKmIlsSRNlPR3w_HJ3l7_qKZA36yKLOIe34-Z0tyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر پربازدید در فضای مجازی «خاورمیانه ساعت ۱۲ شب به بعد:»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672250" target="_blank">📅 21:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00cc54f29.mp4?token=msIHOwy8gEV6idhCzuSFg796KjcKUc46yoOeFH_tHWJIVTE37TUEtQtP_FgBcupvg6bicW7t1UqxaCNm2ezjo8gina0HFt3LFlML6Ep9XItc2gq-4JgsYUbiRC4fZTXMRISpfyd2fav93aoykAJcPNxNosH8CUUSAkB6S4tQqyfHgcYM9GtrMuDsTJj6wOn47C50ntjzEqu7DJ6HanqjMzD-Bie6LdY_jcoY-XtTwhH0lV0gmCFr6KqlgkYBI8EOzBzTetyYx3h42zTfF8sGTVuPveY4AxF5QxCFohAZTxOzBsZR5QJWjJwvORh0ws5DT6zd7T2nkBGHf9q55Qpdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00cc54f29.mp4?token=msIHOwy8gEV6idhCzuSFg796KjcKUc46yoOeFH_tHWJIVTE37TUEtQtP_FgBcupvg6bicW7t1UqxaCNm2ezjo8gina0HFt3LFlML6Ep9XItc2gq-4JgsYUbiRC4fZTXMRISpfyd2fav93aoykAJcPNxNosH8CUUSAkB6S4tQqyfHgcYM9GtrMuDsTJj6wOn47C50ntjzEqu7DJ6HanqjMzD-Bie6LdY_jcoY-XtTwhH0lV0gmCFr6KqlgkYBI8EOzBzTetyYx3h42zTfF8sGTVuPveY4AxF5QxCFohAZTxOzBsZR5QJWjJwvORh0ws5DT6zd7T2nkBGHf9q55Qpdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت به نمایندگی از هیئت دولت وارد خوزستان شد
🔹
این سفر پس از حملات اخیر آمریکا علیه مناطقی از جنوب کشورمان انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/672249" target="_blank">📅 21:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bad651ee4.mp4?token=i9eIEv2Oehq1oLWPqLxU1KkJ7rctWE305xiQz3yK60tA0qUzzTp2IveTyJciVvtKqkRhz3yKMemMK_neI67ckNmKeso0lknj5WRX35uQpRYCClwIqiu8VxSKFpr5LD2NgKC4LZWyX8E7wRHeIYJwJhgL7gyFmBjS1Y0RbMpepTNeSRgRCPOYkQepOsTdYKXD9nTjgmG4SXR4C4tfuG3-0hPDCRdCL2Zt-l-jhElMliRmel6RD5Ho4cwQqJT6qxSD454dgnGnceZYZ0W-eDSJ_b9asJK-buMdG-krshhv6IQqSzvYAsSnvPzBRO7epuyK_SYLw_o_i8vLsmk7Py0JyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bad651ee4.mp4?token=i9eIEv2Oehq1oLWPqLxU1KkJ7rctWE305xiQz3yK60tA0qUzzTp2IveTyJciVvtKqkRhz3yKMemMK_neI67ckNmKeso0lknj5WRX35uQpRYCClwIqiu8VxSKFpr5LD2NgKC4LZWyX8E7wRHeIYJwJhgL7gyFmBjS1Y0RbMpepTNeSRgRCPOYkQepOsTdYKXD9nTjgmG4SXR4C4tfuG3-0hPDCRdCL2Zt-l-jhElMliRmel6RD5Ho4cwQqJT6qxSD454dgnGnceZYZ0W-eDSJ_b9asJK-buMdG-krshhv6IQqSzvYAsSnvPzBRO7epuyK_SYLw_o_i8vLsmk7Py0JyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌ها و انفجارهای بی‌وقفه در انبار مهمات متعلق به گروهکهای تروریستی در استان سلیمانیه عراق
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/672247" target="_blank">📅 21:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTT_B2AXZxYzvSuNPfdDO-P5Kp1ikXBNaD1gNFsD1kvjUtZX3WXuAzwqPvpwWvF2jM1Rz5RORge-z3shw6cRtKwMK5KlA0VL365B7sxM6dVo04p5T3V0PjxBKTa1gkOCRkaw9le21BF8RigsVSdDqAg3bDbZAStnhsljrpGqmFOT9yyv6Nkpj7kLqUMgg_R6BpmYmZpmcv4loimyhIMPFqMkd4GxwpG1R8hMm4FF4rLuEupikCsKUgwHxMhSHQPAloV3QuwF_-1GODlxNGOHYoAdwzSShqhTg7EH9X7-JSNVOa0bBP9U3Kp-FRrFB--S9LINuHySWJDN8ROirygrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت سبد نفت ایران از مرز ۸۰ دلار فراتر رفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672246" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf43f42cf9.mp4?token=YyIMyxNT-1s-5Kr2Pa7omfaN3tTeMKRthZopxRqtp4uKgw-6t8VvMnex48DFkE4sDBxUDhWsmV3OjtpuwKpPNbdIVixjTfgYci5qVNT4EHWxTvpAA8JzZXLpZDn4phaVXY6D6wbvejY_C-8z3058G0RpeRZCF9fSdeKwIUWSVmxWJhta7j_QeMScwNM3uT0XgyiFbhpR_vfV_ldjV6wLUs-T5rMm7tXRYh4e83wNA6F8pSca1jvWNSbi0zmXnoAxqfMplqbFeO1g7wOT_6KRf1GW2oEaZH-MgZDFeWvqNYVJ5mOXzGby6Op-A6k9yArAGAlf1V0p_SUeQS-9zMybCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf43f42cf9.mp4?token=YyIMyxNT-1s-5Kr2Pa7omfaN3tTeMKRthZopxRqtp4uKgw-6t8VvMnex48DFkE4sDBxUDhWsmV3OjtpuwKpPNbdIVixjTfgYci5qVNT4EHWxTvpAA8JzZXLpZDn4phaVXY6D6wbvejY_C-8z3058G0RpeRZCF9fSdeKwIUWSVmxWJhta7j_QeMScwNM3uT0XgyiFbhpR_vfV_ldjV6wLUs-T5rMm7tXRYh4e83wNA6F8pSca1jvWNSbi0zmXnoAxqfMplqbFeO1g7wOT_6KRf1GW2oEaZH-MgZDFeWvqNYVJ5mOXzGby6Op-A6k9yArAGAlf1V0p_SUeQS-9zMybCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای شدید در سلیمانیه
🔹
منابع عراقی از حداقل ۵ انفجار شدید در سلیمانیه عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/672245" target="_blank">📅 21:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672244">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت باب القبله طهران</strong></div>
<div class="tg-text">نماهنگ
«اگه گوشواره هام بود»
اَلسَلامُ عَلَیْکَ یا سَیدَتِی یا رُقَیِه بِنْتُ الْحُسَینِ
🚩
هیئت باب القبله طهران
🎙️
سیدجـواد پرئـی
🖋️
امیرحسین فیروزی
🎼
آریا شمس
🎞️
محمد نصر آزادانی
‌
اینستاگرام
|
تلگرام
|
واتساپ
|
بـله
|
روبیکا
@babolghebleh_ir</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672244" target="_blank">📅 21:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e4b8e77a.mp4?token=CZsPjA3meZqegEPYy7Q9ob0sosJhaKqMP9TOz1t5i-t8vxr_gJyBJt3J3UTcYQCSw8bxg9G9IBxmw_vJsGUJ56cWMoDktXrY6Ao1D4q0fXzS8sR1VeFJMyJZdMSkph4eXPSzdKqHGn0zQmLFDC-3vphVex5PJ8g6ExGUhLQ3JR_9v0-3u0Xh2veuXSBFnQi1vokRCdDeYHzcEoaMYHXFEXVgPAQekvvci9UzN0TiJEdOfyv73f4snMJWMDy16lwjvTxA3J9L5f15p1Q6Sw7Z6ZkiF4mvNxj1DkUg51Hr1uS5_lXBEUjYT5OPUykDxNWiXjvKkBs6siaW0X4eDaSnhleiYIeWFuadeW5-0-qnkAqOlcu193zEOkhNT68YhVoHGDjVNTL5zgl78mgp74rxZm5qgttbkA2uuZkI9jhhUu1T3qERrEuXbVeckii64Fw3XIiO6T35Cng7RU7g8INpvcVVnoZw6ZPvHFKkcRMlU9bPqbs2__wT33SY0-5i9RerhCAQ94nTxT_LgRm9Jdso2ujPFBOOY6hO3cYmPdBZ4OVUz19Q6Jd7SgsX5nJeH9gJ6o9pXWwdfPVEijdRLZbwySIvZN-dITdQQTL4iZuSnCMGJF1fUI44FpUHgSCN8VTCMCmLqb3NIt2vDGNNYI54Nd379mt0VHw3TTepPuEap1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e4b8e77a.mp4?token=CZsPjA3meZqegEPYy7Q9ob0sosJhaKqMP9TOz1t5i-t8vxr_gJyBJt3J3UTcYQCSw8bxg9G9IBxmw_vJsGUJ56cWMoDktXrY6Ao1D4q0fXzS8sR1VeFJMyJZdMSkph4eXPSzdKqHGn0zQmLFDC-3vphVex5PJ8g6ExGUhLQ3JR_9v0-3u0Xh2veuXSBFnQi1vokRCdDeYHzcEoaMYHXFEXVgPAQekvvci9UzN0TiJEdOfyv73f4snMJWMDy16lwjvTxA3J9L5f15p1Q6Sw7Z6ZkiF4mvNxj1DkUg51Hr1uS5_lXBEUjYT5OPUykDxNWiXjvKkBs6siaW0X4eDaSnhleiYIeWFuadeW5-0-qnkAqOlcu193zEOkhNT68YhVoHGDjVNTL5zgl78mgp74rxZm5qgttbkA2uuZkI9jhhUu1T3qERrEuXbVeckii64Fw3XIiO6T35Cng7RU7g8INpvcVVnoZw6ZPvHFKkcRMlU9bPqbs2__wT33SY0-5i9RerhCAQ94nTxT_LgRm9Jdso2ujPFBOOY6hO3cYmPdBZ4OVUz19Q6Jd7SgsX5nJeH9gJ6o9pXWwdfPVEijdRLZbwySIvZN-dITdQQTL4iZuSnCMGJF1fUI44FpUHgSCN8VTCMCmLqb3NIt2vDGNNYI54Nd379mt0VHw3TTepPuEap1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت یازدهم مستند احیا و حقیقت | آتشِ سرد
🔹
روایت محمد جامعی از شعله‌هایی که زبانه می‌کشیدند و جان‌هایی که در پناه لطف الهی، در امان ماندند...
🔹
آنچه در این قسمت می‌بینید، تنها آثار یک انفجار نیست؛  روایتی است از اتاق فرمانی که آتش، دیوارها و تجهیزاتش را…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/672243" target="_blank">📅 21:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e471521d.mp4?token=FN1uhWxtIZxCKsEuRwAjZYEAhJ_u_qoJr56QubLmc2VJRE9QzQD7mP9E2aY3zTqjOKI49oPyqgnfji1TreOIurQku_WKpDp3WzaTk-x9-p5VcHUPspD6nBTmU56odB0sPPeH6q6I_wRRsfSu26ZjfFgSeqs7CPWzbPk1t-LXel-hctJb_Hq_ihwwaVJ65dJwspKVGkT8MmRdjMPUD_EEMaVa9lvC7tD1Bp6PupWD5PKjiIrerrgTZw7Tett1NyVcx92e2B87G1p9LN6f_osKysnLqVG-_rxas3gExfYZQU8sCGRlQU7tg1aTurwRlKx2-MHpe9MiYOchOSuDJtdFgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e471521d.mp4?token=FN1uhWxtIZxCKsEuRwAjZYEAhJ_u_qoJr56QubLmc2VJRE9QzQD7mP9E2aY3zTqjOKI49oPyqgnfji1TreOIurQku_WKpDp3WzaTk-x9-p5VcHUPspD6nBTmU56odB0sPPeH6q6I_wRRsfSu26ZjfFgSeqs7CPWzbPk1t-LXel-hctJb_Hq_ihwwaVJ65dJwspKVGkT8MmRdjMPUD_EEMaVa9lvC7tD1Bp6PupWD5PKjiIrerrgTZw7Tett1NyVcx92e2B87G1p9LN6f_osKysnLqVG-_rxas3gExfYZQU8sCGRlQU7tg1aTurwRlKx2-MHpe9MiYOchOSuDJtdFgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صداهای انفجار در اربیل به گوش‌ می‌رسند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/672242" target="_blank">📅 21:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARpd1kcZbDdGwyieIFwnepMOePrHaOkfmaQtvaaquWSFVOFWAcZ6_Jk193wfG3K3BPKVUCxLBxPJKR_m_zI1PmVudi0_ZbsGpHlSOw5gA_zFlJszfYudieOLuwbPLw59177RAiwZQhQg-DbjmFWQ7o8gOUilxb0c_sgewuVHPtMVEvJGXMbcrNBtO6mZ1BSLDGCLFxDm8jWvHGVJubzYUzfjGWFi4h0wH_ezUubz3C2LPrLf4FmQNc1Vwt52CfiU2znFV01MEDff_5OrHRGV1ddc0jN5pkaZ13iUpKtK4K9DIUR0tbswMPhiC_bKbrltL3QC5UmRqUugj6lRuufGIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شورای آتلانتیک: پذیرش واقعیتِ تسلط ایران بر تنگه هرمز
🔹
کارشناسان شورای آتلانتیک با اشاره به ناکامی سیاست‌های واشنگتن (ترور و مذاکره) در مهار ایران، هشدار دادند که با روند کاهشی ذخایر نفت جهانی، بازار انرژی باید خود را برای شرایط بی‌ثبات و پایان دوران «عادی» آماده کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/672241" target="_blank">📅 21:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حمله نیروی دریایی سپاه به یک کشتی تایلندی در تنگه هرمز
منبع آگاه:
🔹
امروز یک کشتی در تنگه هرمز مورد هدف قرار گرفت.
🔹
این کشتی با پرچم کشور تایلند بدون توجه به هشدارها و بدون اخذ مجوز از نیروی دریایی سپاه قصد داشت از تنگه هرمز عبور کند که با ممانعت نیروی دریایی سپاه مواجه شد و مورد هدف قرار گرفت./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/672240" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
آمریکا جنگنده‌هایش از اروپا به خاورمیانه را بازمی‌گرداند
نشریه وال استریت ژورنال به نقل از منابع آگاه:
🔹
ایالات متحده، جنگنده‌های خود را از اروپا به خاورمیانه باز می‌گرداند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/672239" target="_blank">📅 20:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672238">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4FQB9dbut0LFkmN-5Ipn5DOJ5e1wFobWPENNL5v0m2fDGsuOvqCD8QI4qXqkChGnrJJOjiQUJ7CjpZ-TS1GSVeXRIZgN_2EPTmJJE4xr7nMwzrvoJoLS4rsfzH3ctCznDOtWBmwcgZo1kD2Y3m-cdC-_T81RQzRPwibSd665HLglh__b0cIPrLhO3ZIbt0KE8EYTfnvk0E_seJ0wnufwwxIa2wm_w8zMnX20rM77sXNlWxbh8H5WHPxicIhM0_wJM_m134QrtU-El9lz6k0eEp_jNcdlK0LaK1FYm6N8lQTmv-Ay6YCmLM6WirwZj0xc4dbx29fdlYk1KAdTyHXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند  استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/672238" target="_blank">📅 20:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672237">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صداهای انفجار در اربیل به گوش‌ می‌رسند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/672237" target="_blank">📅 20:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672236">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تجربه‌ای متفاوت از مرگ؛ پاسخ سلام اهل‌بیت(ع) و بازگشت به زندگی
🔹
00:08:30 ماجرای سقوط از بالای تریلی با ضربه شدید به سر
🔹
00:15:10 یادآوری شکوه آنجا کافیست تا ناخودآگاه اشک در چشمانم جاری شود
🔹
00:22:40 رؤیت خانه و باغی که متعلق به من بود
🔹
00:25:00 درک عذاب چند تن از نزدیک‌ترین دوستان توسط روح من
🔹
00:28:20 سلام به اهل بیت در دنیا و گرفتن پاسخ در برزخ
🔹
00:34:30 به زانو درآمدن در مقابل امام جعفرصادق(ع)
🔹
00:44:10 غم و ناراحتی باورنکردنی از بازگشت به دنیا
🔹
01:09:00 قدرت شنوایی بالا در میان هیاهو و فاصله دور
🔹
قسمت چهارم (تردید)، فصل پنجم
🔹
#تجربه‌گر
: حسین حاتمیان
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/672236" target="_blank">📅 20:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672235">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مخابرات منطقه لرستان: اختلال در زیرساخت ارتباطی شهر ویسیان لرستان برطرف شد.
🔹
موگرینی: دیپلمات‌های ایرانی برابر فشارها خونسردی خود را حفظ می‌کنند.
🔹
قطر بر لزوم توقف فوری همه اقدامات نظامی در منطقه تاکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/672235" target="_blank">📅 20:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672234">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWFkG8psdkTnqIjHYEnNQbpGq7C7RPakXtk6Tts25er69DHefCNKovzWjvIs0g_pegqA55Xyh6U9nqRFjCrKZCIq2W16jOxHmLZ8cCdzhZ6XlbEKu0JYfnRtdZyCKeyx7O-urmlLdgJsscnjdEFV4_Sd-s8ahEQrj7OlgHtrNY1c7QLdJftu6sTD6FKcWhmQk2QzuHMPAOGPgCLohu39GVQjLO9vXsOLPROyKeU-nrl6yaGiD99w8s3OWquKrUIERaZqyW9mBQKqbyOtJ5xDQl6fAkb2HkseoUykmIUGn4mwiQ-9s2Hj4ummBd2D6Zp_s1GM-Ufnt9OaXt318urZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه امروز قیمت‌ها رو دیدن...
تو شرایط خریدت رو هم ببین
💎
اجرت از ۳٪
🏦
خرید طلا با هر بودجه، از ۵ میلیون تومان
🔄
تعویض طلای سالم با عیار۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
📲
داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672234" target="_blank">📅 20:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672232">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
یمن خواستار باز شدن مسیرهای پروازی از صنعاء به تمام مقاصد شد
یک منبع در دولت صنعاء:
🔹
خواسته ما این است که مسیرهای پروازی فرودگاه صنعاء به تمام مقاصد بدون هیچ استثنایی باز شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/672232" target="_blank">📅 20:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672231">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqwQ3Ru2ZXcg4GYiAau48MFCHwvDNMw-fX4g8zh52qHcas-UmjrX7jVX1L49GRin0Pgo34ZPidzEy9pF50XMkoqF7XXjJacQ-tOC08he7hnG6qQ4QfeWDbxI2rnwzKk0sUA5rGVtxGamLHmUvIELLW6w2CBui2IjecbVLdIvQizMHgYkfYzrwUsdFTjl86GJFwa4u-556w2cwjcipTZyDD9Kgeq4UgxFyG46S3hGoFcjt2wZNtPO6ZRfAqKkuzg6x6Ps6cbESeyweENzyWDvCHIuTZimvd8Og8rnay1gesmb8y28cxVlHOotqLtjqEYfQGeK5vOpy7s34vclq1t0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثبت نخستین تصویر پلنگ ایرانی در منطقه شکار ممنوع کوه‌خم فارس
رئیس اداره حفاظت محیط زیست شهرستان سرچهان:
🔹
حضور پلنگ ایرانی برای نخستین‌بار با استفاده از دوربین تله‌ای در منطقه شکار ممنوع کوه‌خم فارس به ثبت رسید.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/672231" target="_blank">📅 20:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672229">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehZG7ZOCInTlB7ftXqMHdVC8U-tXl6mZsfLZgEtoExVK17r_h2dNxGDg7cenPZaj3y_G5LsXcnB6kB0XKujzBnzVT0FIu4hP1AHPAs9Ii4WKbq9C8gb2loo1zc9RJ7ET206pPAyFK3lIh33G_mz5sxTcOCHMb9NZ_LGO32RZSppJBKXHM3M537qMWdrBTfD2F4HSoGazNH1kowkBUmRagC3eBNnO2rW7MF3m52RWds2ONNQ_dr5yP6wMjFoQTthAxv9FEj_K7fyihIYtB0pP5rHOfopn3H5cEzO5nq-irb2d6l6ON53DpXcJ1HwjN92LYs6qgcmXirJDHFUN46kf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/672229" target="_blank">📅 20:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672228">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آکسیوس به نقل از مقامات: واشنگتن در راستای پیش‌بینی گسترش احتمالی عملیات علیه ایران، به اسرائیل از استقرار هواپیماهای سوخت‌رسانی اضافی اطلاع داده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/672228" target="_blank">📅 20:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672227">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
قلعه‌نویی تا جام ملت‌ها ماندنی شد
رئیس فدراسیون فوتبال:
🔹
آقای قلعه‌نویی باتوجه به مشکلات و محدودیت‌ها نتایج قابل‌قبولی کسب کرده و همکاری با ایشان فعلا ادامه پیدا خواهد کرد./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672227" target="_blank">📅 20:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672226">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از مقامات آمریکایی: ترامپ ممکن است در روزهای آینده دستور تشدید حملات به ایران را صادر کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672226" target="_blank">📅 19:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672225">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e68436f0.mp4?token=qZB6l1XdT8PJ4KqIJT1RzprTqRRsYLkhupJwQ-KjeD9ITczjEFJv0JhlBiLvKK7U4FalFQlTS1i7wqWBHLFVq3VHcv5lVd1YOZ3y8kjZamr7QW8Q4oIOqupPApuJtt_xHVLIafY2jpaMwSdm9xCqIdo_q1i2LAK3xxjsahqTI-4hk4_NxBqD3QeAvUFlRm5Zn_2Akp1QzsoWQlxNCB1Vd41I3A_P9sfG7-Oi9ZDW7UW2VJ6eboPcvNguyogCRZiBkv0OcKDeTsUBlmysDg9ywu_OWNz3DxmxHk8gmcnbWI5zLAFzSLUQMWm64KnHnS-mJufXNBmfSYewCW7rSNYliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e68436f0.mp4?token=qZB6l1XdT8PJ4KqIJT1RzprTqRRsYLkhupJwQ-KjeD9ITczjEFJv0JhlBiLvKK7U4FalFQlTS1i7wqWBHLFVq3VHcv5lVd1YOZ3y8kjZamr7QW8Q4oIOqupPApuJtt_xHVLIafY2jpaMwSdm9xCqIdo_q1i2LAK3xxjsahqTI-4hk4_NxBqD3QeAvUFlRm5Zn_2Akp1QzsoWQlxNCB1Vd41I3A_P9sfG7-Oi9ZDW7UW2VJ6eboPcvNguyogCRZiBkv0OcKDeTsUBlmysDg9ywu_OWNz3DxmxHk8gmcnbWI5zLAFzSLUQMWm64KnHnS-mJufXNBmfSYewCW7rSNYliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از اوضاع تنگه‌هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/672225" target="_blank">📅 19:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672224">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4sWr6siHKM-4tixmapfwlNwZsRsOvM_7VG8WY2EWlinI4Oh7bLuL6flYPd3ko5jdOcjubOoq-BQfxR7ajPCfc7gIluvJUVKOKxDBrDraYNUCA8Rcw8uIoTOWU-IlKZT_ks28JGcl5Ei4iqaSSi_RasIq03ImVJr0JfzU-Dy5643uqlFYYKeHMxfa60Krc0QPci872vguBxv1uPf6ujV4d96JM154yCudI3TRJFWvvZcpeFVKHk_0wf6NZVAudausK4y370nG6ZigzES6KFcyOmOd2pmwBlqHM200L213T-n3KbkZIJrNb_nBKCR9bg1hcZK26cNaxawwPKoR4AITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یک فروند پهپاد آئروویرنمنت آرکیو-۱۱ در رامشیر منهدم شد
روابط عمومی سپاه حضرت ولیعصر(عج) خوزستان:
🔹
یک فروند پهپاد آئروویرنمنت آرکیو-۱۱ ریون توسط آتش سبک سامانه پدافند هوایی پیشرفته سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی در منطقه رامشیر رهگیری و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672224" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672223">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC5qXIZvVQYvd_f8wRp-6ZT_8p2dtKUjLHdXyJvP02_fKZ9tVDO8JU8UcY-AV0X84NlidNSOlF1gIQVXf-Lwp2o2cNlMhc7c3klnBUEgp6Ry8m4Ob_9hEFLcY0QDKYm8Yw2eYeQg_JX0kWksrUY7n1xw31-fjWD04gKIOb7goA62B20LQCYgeqfBrHutyzLB8Oq8q8JzlM9idyJ3_s5_ipVMoGg9zCpxiipMobnUSdRhaEuQw8ZWBEKOOtpgRLp2pdThuhUUu1uSJJ9-JJeugccTtxxasuudGhMeDHcMImiQMBMRK5SdKEofzWT5gmi0ZAyyv0GMAknPDvNWs2bdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام یک انبار لجستیکی آمریکا در کویت پس از اصابت پهپادهای ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/672223" target="_blank">📅 19:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672222">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvBxRWocydVBHyJohwfgF7DnUbidU_2L_0WsduykWMQK9-gk2ZKvfdwlEFaxFiLvPJxCMSma0GOyvqZe2_XTImYmvyhw2dXSXwmICLu6SXbN5VcGa_hWqDZpWAxFG-XOd1EtbSMKBF6ohXDZKCUv5ecgDG4qdYCreXfS8pHdmBS-Y-2SjBGRrUcg4bfDCKrgyXKwcfxChPz3i43ewlqC4HbODJzXQf-NR9DEO0o8UcyC-cq-SbQI8QS42HzA_XIxhz8hDpwa2MpudB_ei2UR1MoXgdIKMrqhFylWfvzmtVqpJbVyT4K8BPTJU2Ksxl37GsAUWQUT5CBKI2SySWgsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرژانتین و اسپانیا در فینال جام‌جهانی با پیراهن‌های اصلی خود به میدان خواهند رفت
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672222" target="_blank">📅 19:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672221">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به برج مراقبت دریایی چابهار
🔹
صبح امروز ۳ انفجار شدید باعث وحشت مردم منطقه شد، اما منطقه مورد انفجار مشخص نبود. جنگنده‌های ارتش متخاصم آمریکا ‌برای سومین بار طی روزهای اخیر، برج‌ مراقبت دریایی بندر چابهار را با شلیک سه موشک…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672221" target="_blank">📅 19:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672220">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZbDzgmrFjlxNaGHtuFRPIsQ1dZ-ANupuTqwnOMJ6Vn4yakpbA1uxOL2Q01EkHmwfdnv7cuqKpoWJ8anRbLJqKqanonW4D-GWFWh1qwcQVAyRiJk6AdRWLN79Su7PiufE4b5PxtyxZ5NkUVMZKwbf76saMuPqI-y5uR3G-9QgfxXWV0AVs66lWWm5ZxkxsZp0Y0KemnidsY917tq9k27Co5oF2QM-guYZVO40-ED5BOgclzGuh_H8VkfXjvf0SlFf4Q1o8Hg92geIWsmXIM0LPg-r82vDzo5s_huVfzmXfhRu-acAZja7dxobcN63KXAqxeAGq5mUyNrerCIA542MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش یحیی‌گل‌محمدی به حملات آمریکا به جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672220" target="_blank">📅 19:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672219">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZzhkCy4H8Vmvz6Nvxxs0tkFDkv7Oz11wEvnQcZAJPy2gw0RkP8ahUn3i2N91vHozrsg3ycyZuhJ1FcllzcHQOgJkmvGyadRbINojEJKYwvDaDwguKpm9bYEW1_2P3-zQgrE9EuD8Jp38SFORpqiUzKnh0NhRNs22zSvhxCQb3-boxv6ajxZham0m3-Ed6nXya4aZ5KE6hA1Nz_cvj6X0AWgu_8tz5XxBMOUZ9NBjr6-JxJ_EOIXSDXA80qHnMLLt45-DX2MfdMUbrqWCUX6-AJ_glwGKI5aaj6eWkG2NCwy54hsiz1uY28TNJnGW7fU-l_IRY6BGrhYEFZTcjfbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست‌های ترامپ هم اشتراکی شد؛ هرکس پول بدهد زودتر می‌بیند!
🔹
شبکه اجتماعی Truth Social در حال آزمایش سرویسی به نام Truth API است که به شرکت‌ها و معامله‌گران اجازه می‌دهد پست‌های جدید را چند ثانیه زودتر از کاربران عادی دریافت کنند.
🔹
منتقدان هشدار می‌دهند با توجه به تأثیر مستقیم پست‌های ترامپ بر بازارهای مالی، این کار عدالت را زیر سؤال برده و رانت اطلاعاتی ایجاد می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672219" target="_blank">📅 19:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672218">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da8847885.mp4?token=Knt3X3RlhxCG-8iUjIugmSRc3uq9aNazw_hj8Lox2VTSbTendJYeXNF_LbrR4VvFQ_2YiDF7Umw-NZzyDJ2kKdouHfJTcWzkPbrtWqWV98UGQExr99W_njAlo2HjJ3Si3bZVl22LmCnAAxpe0d2Lfnha7dIh3PRYfnDe7IOXUQi9PzxbODGlEVvJV66gw8L5ayrwUS2FwIh_yjCZNeUsBNUHISfzYJNWLTNcsuaV_Bw0R1LDZwHs9f4jcXi5VaHH0Gjg4BEQuTH-AynreQTyOxU7QO5XPmWP8zhhlCivC0Brw_yPcWkRbUjg8WeO1q4XOCj5LLZBt3gqKqJh55ajNzKtx_WvNzEbWOLHn4BOUajvrWRhG35DjtTIrPrOTUkcSOXp9HAHEyq4K1YJlfRggXtC4t1TPeLG1kEo2GSe8jnpO7pA6vxmrlT8LhQ4HlyMfWu6pMhRi9jgkiRVvDiNP8Rq5VxFpqdJuqsm71ZvioDbxSAOsazNt5EkvQfRk0KN8-cB0VfJ-oBNa-JWXVOimViW2QuQRdJ2Cpae-izzsFSt8SNslACDYMLfT6VbhQBA9-MTbjwqFGKelOtSEnO1xWA6QGbAhhYzIWM_h8Obnn1-k7FOslXh1OCkGwCB7SL62whmyxyggCtaYZHtiAt-WtW_zc_WT64C2iCPIJleR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da8847885.mp4?token=Knt3X3RlhxCG-8iUjIugmSRc3uq9aNazw_hj8Lox2VTSbTendJYeXNF_LbrR4VvFQ_2YiDF7Umw-NZzyDJ2kKdouHfJTcWzkPbrtWqWV98UGQExr99W_njAlo2HjJ3Si3bZVl22LmCnAAxpe0d2Lfnha7dIh3PRYfnDe7IOXUQi9PzxbODGlEVvJV66gw8L5ayrwUS2FwIh_yjCZNeUsBNUHISfzYJNWLTNcsuaV_Bw0R1LDZwHs9f4jcXi5VaHH0Gjg4BEQuTH-AynreQTyOxU7QO5XPmWP8zhhlCivC0Brw_yPcWkRbUjg8WeO1q4XOCj5LLZBt3gqKqJh55ajNzKtx_WvNzEbWOLHn4BOUajvrWRhG35DjtTIrPrOTUkcSOXp9HAHEyq4K1YJlfRggXtC4t1TPeLG1kEo2GSe8jnpO7pA6vxmrlT8LhQ4HlyMfWu6pMhRi9jgkiRVvDiNP8Rq5VxFpqdJuqsm71ZvioDbxSAOsazNt5EkvQfRk0KN8-cB0VfJ-oBNa-JWXVOimViW2QuQRdJ2Cpae-izzsFSt8SNslACDYMLfT6VbhQBA9-MTbjwqFGKelOtSEnO1xWA6QGbAhhYzIWM_h8Obnn1-k7FOslXh1OCkGwCB7SL62whmyxyggCtaYZHtiAt-WtW_zc_WT64C2iCPIJleR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاد بگیر مثل سرآشپزهای حرفه‌ای مرغ رو خرد کنی!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672218" target="_blank">📅 19:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672217">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پیام قاطع وزیر دفاع یمن به دشمن سعودی: تداوم محاصره بی‌پاسخ نخواهد ماند
وزیر دفاع یمن:
🔹
ما به کشورهای متجاوز، به ویژه دشمن سعودی و کسانی که پشت آن در تحمیل محاصره هستند، هشدار می‌دهیم که گزینه،‌هایی برای نیروهای مسلح باز است.
🔹
ما بر آمادگی نیروهای مسلح برای اجرای هر دستور فرماندهی در صورت ادامه محاصره علیه مردم یمن تاکید می‌کنیم.
🔹
سطح آمادگی در اجرای منویات رهبری طی روزهای گذشته بالا رفته است.
🔹
گزینه‌های ما باز است و در همه نوع و تشکیلات نیروهای مسلح آمادگی بالایی داریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/672217" target="_blank">📅 19:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672216">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330fbcbd73.mp4?token=pcvghnLQnyd3ZZtxq-Q0O9GxpS-Rswywoxvg6nj_hU4z_RuOyPnvBYmJeS2vODsHkgx-umO4oJe1yDnBR5zI9G96nlquYXCnkC6J_QtCofmHUSy-OYTGAME_R9ur7wELXqxcOoOtm3gO4zGqP40Wep5kk5sTZ8PYDWg4wN6sb-gMxem_c0C3qv47jY6azlWyqrCNgi7bn2z92_lvmgJxk9emjVjvaiALQbYEP6dhYAyM4K5nxV_7oDOi0AKzXhnsMZxrB6VWSVPTJ9O7-Iptxsodo9UfuLunhKEsy94xEYMX7IK--92hEan3CEqjFmuKSwO0uCztQ-t1SZxRkWL5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330fbcbd73.mp4?token=pcvghnLQnyd3ZZtxq-Q0O9GxpS-Rswywoxvg6nj_hU4z_RuOyPnvBYmJeS2vODsHkgx-umO4oJe1yDnBR5zI9G96nlquYXCnkC6J_QtCofmHUSy-OYTGAME_R9ur7wELXqxcOoOtm3gO4zGqP40Wep5kk5sTZ8PYDWg4wN6sb-gMxem_c0C3qv47jY6azlWyqrCNgi7bn2z92_lvmgJxk9emjVjvaiALQbYEP6dhYAyM4K5nxV_7oDOi0AKzXhnsMZxrB6VWSVPTJ9O7-Iptxsodo9UfuLunhKEsy94xEYMX7IK--92hEan3CEqjFmuKSwO0uCztQ-t1SZxRkWL5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرزو کرد که آرزوی پرشیای سفید پنوماتیک به دلش نماند؛ اما ماند...
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/672216" target="_blank">📅 19:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebff8c971.mp4?token=saBkTas-FILavmj6pFT02VKjL3R9qvwRFpFreB9GFLhtO1K_tj21g4UQ5UTppBWd0C4muk84ML8Xb6qeBJx0cLg9wHI-93WnrO6tYcJZmCBlANHA5jy6vXEW_CzFkWfhr7mUpHRfvah3jnv6SQfYfX96ibqaKaagF1X5TbOqUj2qThAEzRVxOvRNxcU5YdJjYp9tlvakFxeIBD-dyIr6tf5kzj-7vB3qBOSE7Jm_-A28NYXo5adiI0tKpKLZ5FLGyTqxnm-Vqzfdq0pIeT2FW3GQWR40kMdxP-ecS-I-dhu44BA8JGzRvbW4--9v1RP55cpi0vC84YGzDtytheayDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebff8c971.mp4?token=saBkTas-FILavmj6pFT02VKjL3R9qvwRFpFreB9GFLhtO1K_tj21g4UQ5UTppBWd0C4muk84ML8Xb6qeBJx0cLg9wHI-93WnrO6tYcJZmCBlANHA5jy6vXEW_CzFkWfhr7mUpHRfvah3jnv6SQfYfX96ibqaKaagF1X5TbOqUj2qThAEzRVxOvRNxcU5YdJjYp9tlvakFxeIBD-dyIr6tf5kzj-7vB3qBOSE7Jm_-A28NYXo5adiI0tKpKLZ5FLGyTqxnm-Vqzfdq0pIeT2FW3GQWR40kMdxP-ecS-I-dhu44BA8JGzRvbW4--9v1RP55cpi0vC84YGzDtytheayDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور و مرور زیبای تنگه هرمز ببینید
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/672214" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGcHuSOvYreQZzsopa1TbKXKFN5Qv-USJei1JXpifnDPw00LEc0w30HNQ7e-o6TiPyBR9hIrSWChADcSyC8TEDrlXwQpWfJro2wWc0HUxlkLbVJSo843t6JgE7SdfRsnytXKYhHsQ6AlBwAyiwM1hfgl7bhL7ocks1qY8XfewMXX-ippCbPgmGoaG-2J3g8lbxgqpRiMTZraPKYPysLg1VnSnG4J8e5YsiWUMWGlHEmmLfNDtEyN0nxPkFobUM30xrc861JOuUs1xnZSjUEgWJ39aEdM20tr1SJ_Qie9y9hmdGGAdVUXiXMSypC6tu-SK7zT2XLSoy83QOvmDjG55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
https://khabarfoori.com/</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/672213" target="_blank">📅 19:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06710ec42.mp4?token=lJG7633Y_OgGpoNT8TZOu4lW-7FLwbt6kt6oJ0BT-oRoFvDMnAdYkbSmzuUh88PZOYFgfXQgEwjV1RFCIbFpS2F4wpX-QUm8sP7nuMUW6Owi0NNJcaczeh7soWz4XeUuxX9IBoCOO50fLxNsBZPbp_eOFetjqDahceR03ESfvRl7Q1og3J5lzXKACgTtkvAq39LNYz0ezQU28--BnX11519Qx4yaD0zF5WyWKqJIblieuMvS5-4zb6T52ruu4z34CMCfWalMI9wgZafSOq_Cgme8UbyG7VSULg8kJwIUPfGcyutugZ_RYYQMB4qrnredMEuRBbxE_HQNAPk2nqEPIUsBCDrc1JIYDkZnZrykYxCe2MUhdX7J358n4TWvZYqmbHKJFShtQHwpQ-sBDTOF3T23Pw_OV_TfC_qb5mxFOb4qK3Zxjd1VS_u7mqRQagKY2YggQlAbAFZoBq_nFx8t99VGWGGBndz8_UZrRQuGgvJFffpBK-sK73-RNigiZlOyeRq4RMvRysekkuNURov_r1ZfQT3HAb8Vj1UTIvdiYsdZQiRGpKAlSBmkXWMeV0Mds6PJ8qdowfqgc8yt2CT8EIn3zw4cWzh_Y8EE287ZGvX6cU_Go7jL8_HLxzNUJqO0pqn7IzJgthUJ53MV-18ZXscRO4ud9_XxWk7w2MSXD7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06710ec42.mp4?token=lJG7633Y_OgGpoNT8TZOu4lW-7FLwbt6kt6oJ0BT-oRoFvDMnAdYkbSmzuUh88PZOYFgfXQgEwjV1RFCIbFpS2F4wpX-QUm8sP7nuMUW6Owi0NNJcaczeh7soWz4XeUuxX9IBoCOO50fLxNsBZPbp_eOFetjqDahceR03ESfvRl7Q1og3J5lzXKACgTtkvAq39LNYz0ezQU28--BnX11519Qx4yaD0zF5WyWKqJIblieuMvS5-4zb6T52ruu4z34CMCfWalMI9wgZafSOq_Cgme8UbyG7VSULg8kJwIUPfGcyutugZ_RYYQMB4qrnredMEuRBbxE_HQNAPk2nqEPIUsBCDrc1JIYDkZnZrykYxCe2MUhdX7J358n4TWvZYqmbHKJFShtQHwpQ-sBDTOF3T23Pw_OV_TfC_qb5mxFOb4qK3Zxjd1VS_u7mqRQagKY2YggQlAbAFZoBq_nFx8t99VGWGGBndz8_UZrRQuGgvJFffpBK-sK73-RNigiZlOyeRq4RMvRysekkuNURov_r1ZfQT3HAb8Vj1UTIvdiYsdZQiRGpKAlSBmkXWMeV0Mds6PJ8qdowfqgc8yt2CT8EIn3zw4cWzh_Y8EE287ZGvX6cU_Go7jL8_HLxzNUJqO0pqn7IzJgthUJ53MV-18ZXscRO4ud9_XxWk7w2MSXD7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابستان گرم هست و همه نگران پایداری برق هستیم .....
🔹
این ویدیو را ببینید تا زاویه دیدتان به زندگی تغییر کند....
👆
🔹
ببینید اقوام ایران چه درخواستِ مهمی دارند....
😊
🔹
اگر میخواهید همه چیز را دقیق و موثقی در مورد برق بدانید.... در این آدرس‌ها در پیامرسان بله با ما باشید
ble.ir/bargheiran
ble.ir/tavanironline
اینجا همه قرار داریم ....
قرار همدلی
🫶</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/672212" target="_blank">📅 18:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
زمین‌لرزه ۷.۴ ریشتری در جنوب غربی مکزیک
🔹
زلزله‌ای به بزرگی ۷.۴ ریشتر در جنوب‌غربی مکزیک رخ داد.
🔹
تاکنون از میزان تلفات احتمالی گزارشی مخابره نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/672211" target="_blank">📅 18:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
بیانیه ارتش: ۱۱ عملیات برون مرزی تیپ ۶۵ نوهد ارتش مقتدر جمهوری اسلامی ایران در خاک کردستان عراق، با همکاری اطلاعاتی گروه‌های هم پیمان ایران، ۸ فرمانده میانی گروهک‌های تجزیه طلب را حذف و ۳ مقر را تخریب کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672210" target="_blank">📅 18:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnXcDnS-CRXmatTZPFbQ_EaPxWN0j9PJShIUwuFmFyygCNQo7d5GKBiSNtgxHSfa_JbjfJFkQV8R-rWSuReoNy5qwB3xG77uzvkyTNI8uHBkoe1gmMG17zMjypxFq9parlnBx9B_4Z9RsllsDQvfMUc5LDAgJj0voD3BPNJ89M0tWjcvNnRj_dik50Ea-t4V1ke2twRCfhFZXVqGjDVUzCur6oNTmDkUQX9DT3taIFyrLXxZYjzjpgBE4_lTwTe_b_IZPT5a8f5NS6Xmu5yXXOnJ8t7b1q78iz_4Bfq4PsNWeq-0P_2egVWkE5iOUIGSApBgsNN19ZZGxPzsF3RcAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تظاهرات میلیونی امروز در صنعا، پایتخت یمن
🔹
اعطای اختیار آقای عبدالملک الحوثی به نیروهای یمنی برای پایان دادن به محاصره یمن و یمنی ها از سوی عربستان در دریا و هوا.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/672209" target="_blank">📅 18:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDRpkbI9gnyQICoDzobCR2uXgJUIf_XR9Cgq6QPg6kinMoYqeOyTW4p2tD1sE5ic1DZr7pNG-WS_Vqyo38nlCmYFe5HuVkTboXnYhQf1LkphiAEDSUTVQx5JYQwl46feo1qW3Wzg4idINp92XvhZgeXqsdnEMvZCyZ4xWzEVnbWBr34VRFBfLQWWfcBngikOuaDAac4MqwjfB_F-APzaM-phHexdDDAW7zeEA9ijN2EWEYFvInkBU3hUIbO5wdu0GBVye0PwJwLc-hrFgeRijUMDMOKIJG9elobIqWOO_Q--stJeeC2dI7qcPTnsultn-9IB0e-_ThQYrf-G9n4Qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیراهن نمادین پله در فینال جام جهانی ۱۹۵۸ با مبلغ ۴.۹ میلیون دلار در یک حراجی فروخته شد
🔹
پیراهن شماره ۱۰ برزیل که پله ۱۷ ساله در فینال جام جهانی ۱۹۵۸ بر تن داشت، به ارزشمندترین قطعه از یادگاری‌های پله تبدیل شده که تاکنون فروخته شده.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/672208" target="_blank">📅 18:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت خارجه هند: پایانه بندر چابهار در ایران هیچ آسیبی ندیده است.
🔹
ادعای آماده‌باش دیتاسنترها برای قطع اینترنت صحت ندارد.
🔹
ارتش کویت: چندین نفر از پرسنل نظامی ما در حملات اخیر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/672207" target="_blank">📅 18:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
معاون استاندار بوشهر: یک نفتکش مورد اصابت موشک آمریکایی قرار گرفت
معاون استاندار بوشهر:
🔹
نفتکش بلما ان آی ۲۲ دوباره مورد اصابت ۲ فروند موشک آمریکایی قرار گرفت.
🔹
این نفتکش که تانکر آن خالی بود در جزیره خارگ پهلو گرفته بوده است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/672206" target="_blank">📅 18:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تردد‌ها در تنگه هرمز کماکان از مسیر ایرانی است
مرین ترافیک:
🔹
داده‌ها نشان می‌دهد که ترددهای تأییدشده در تنگه هرمز، به ۸ فروند کاهش یافته است.
🔹
از ۸ عبور انجام‌شده، ۷ مورد از مسیر آب‌های ایران صورت گرفته است.
🔹
هیچ ترددی از مسیر عمان ثبت نشده است؛ همچنین هیچ گونه جابه‌جایی از سوی ناوگان سایه مشاهده نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/672205" target="_blank">📅 18:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
صعود پرسرعت قیمت نفت ادامه دارد
🔹
قیمت نفت در سایه تشدید درگیری ها در خاورمیانه، به ۸۶.۵۵ دلار رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672204" target="_blank">📅 18:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe3776c2d.mp4?token=V1tt044jy0OilVUz0qCq1zFNKaOAjvrja-PGuKyxXE4IcO2pX6KCHN0YDBJ9o-zchnb0036FcEUtiXNFMrfOTQqWaW6dddmRlGB1Kf0fALb6TZBGxZxQ8LanyVD6r2-LeAFRnrWq3rxAOrEKbyFxHwTiRcarIDC3tUm8kcug1SVa1SxF8lYqy7wY31my7arEuQYuHo_xMobL0pZeFWzjHHeTvoeYl2KTgTp9hC4YPQvrcZVmLf4OO4pBhqsBby21M-tQjJcFERecUSLnunYjuzLKByCIo5fAk3MtR_NOzbvfpUdb1Syk4O0AhzVMg55kOPmZQptjJ_xarFZyE3nKQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe3776c2d.mp4?token=V1tt044jy0OilVUz0qCq1zFNKaOAjvrja-PGuKyxXE4IcO2pX6KCHN0YDBJ9o-zchnb0036FcEUtiXNFMrfOTQqWaW6dddmRlGB1Kf0fALb6TZBGxZxQ8LanyVD6r2-LeAFRnrWq3rxAOrEKbyFxHwTiRcarIDC3tUm8kcug1SVa1SxF8lYqy7wY31my7arEuQYuHo_xMobL0pZeFWzjHHeTvoeYl2KTgTp9hC4YPQvrcZVmLf4OO4pBhqsBby21M-tQjJcFERecUSLnunYjuzLKByCIo5fAk3MtR_NOzbvfpUdb1Syk4O0AhzVMg55kOPmZQptjJ_xarFZyE3nKQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله جدید ارتش رژیم صهیونیستی به مراسم تشییع شهید در غزه؛ ۶ نفر به شهادت رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/672203" target="_blank">📅 18:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672202">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f1d97831.mp4?token=mEWAA9V_N-nnjFeakNoheKov1xgfRY3sihZFuhroCQ8c7aHip46L7xJAEyU57HLvLac0hpnndpQznEMld09ub7y63NAGgZGLl705AuAyTUXMYYRkb8aeo1JNbGtJaJ0-wrNoJ9BoZ2_gniSIkzH3aOenZTCqtM8t6jvmwLE09wYoOTr9_f3JCpZjp9TAZMSrgzKWoJfOEBvEHPYXMOYJn2UDL_azsV1hi4kKyJ6UPbDOfH6U32PimTbjAZ4N_sOFwloYYv00DQ7g0lyrBGc1x-6i5QXzhvgKEu3cMy9YPqu8s9dzI9sWfHbhGtHCOgkj95BvhTDFnXILCqzOxgllekmUs1cQuf7o6bxYtV8a8O7DskEoLBzi_56GbeEIzwoQ6mcO5rlWOCdxHY-PG0l3coRSK2v2XCgHVwSjgsWeZA0V2bO7kZBvLA-PDVpegDEXHGV7Ols7ATQotdT76RyLDlkvaghD3D1dg4KHQrj8LAr3NT97kiDTFDPr8CFvs5aCV7n5q6BL5KlZOTX4UlFGKZwJJhxqqGoJYqSa-0SmBoIQzd3vkUooynsNWRtcxcfxiw_Oq0CfTS_58iR_0sCH1AS-giQrGaGROiDug_HdSMiqmMuf7x9qcFOS_BifMZPk_SY7oaM84Ol7Lw1Ag_-YZIhcI5ZosZAMIzx8GLp04xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f1d97831.mp4?token=mEWAA9V_N-nnjFeakNoheKov1xgfRY3sihZFuhroCQ8c7aHip46L7xJAEyU57HLvLac0hpnndpQznEMld09ub7y63NAGgZGLl705AuAyTUXMYYRkb8aeo1JNbGtJaJ0-wrNoJ9BoZ2_gniSIkzH3aOenZTCqtM8t6jvmwLE09wYoOTr9_f3JCpZjp9TAZMSrgzKWoJfOEBvEHPYXMOYJn2UDL_azsV1hi4kKyJ6UPbDOfH6U32PimTbjAZ4N_sOFwloYYv00DQ7g0lyrBGc1x-6i5QXzhvgKEu3cMy9YPqu8s9dzI9sWfHbhGtHCOgkj95BvhTDFnXILCqzOxgllekmUs1cQuf7o6bxYtV8a8O7DskEoLBzi_56GbeEIzwoQ6mcO5rlWOCdxHY-PG0l3coRSK2v2XCgHVwSjgsWeZA0V2bO7kZBvLA-PDVpegDEXHGV7Ols7ATQotdT76RyLDlkvaghD3D1dg4KHQrj8LAr3NT97kiDTFDPr8CFvs5aCV7n5q6BL5KlZOTX4UlFGKZwJJhxqqGoJYqSa-0SmBoIQzd3vkUooynsNWRtcxcfxiw_Oq0CfTS_58iR_0sCH1AS-giQrGaGROiDug_HdSMiqmMuf7x9qcFOS_BifMZPk_SY7oaM84Ol7Lw1Ag_-YZIhcI5ZosZAMIzx8GLp04xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از سوراخ ایجاد شده بر روی کشتی فله‌بر تایلندی بخاطر اصابت موشک نیروی دریایی سپاه در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672202" target="_blank">📅 18:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672201">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrTuc-hg_iH8urBI2ti0464kFcsL0PvvET8WilaEe3vDuDM4uqKFKVXKHMOhpCbRcHAAD_s3J_J8z7b1i7DuHMB527siUQTGCQvX55o0Ny6gVsEfBD48g9m2ZhcuBm84Tuz3-HmyJ5e_zgFTCKS9cf8ts6YvZV73XfryzRjFPOmdwp0Pw-UzedHLTFJUNBRItDSAMyv2g7yyXXblmc1LjYk_KDv_xk2fI9nPvzYjiKIkbPO9pAQhdfEa2NWIjzeWNVyXyBVhD38EN_hUT2Xq5-rhXyCqETplxwiimEq5qwvsUZ_lAWwRbFaf3VjVidodOtFnY7j9aI3lV2VTpNVDmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی نیروی دریایی سپاه:
آمریکایی‌ها هر لحظه خود را به ساعت صفر عملیات علیه یگان‌های دریایی سنتکام در آب‌های منطقه، نزدیک می‌کنند.
🔹
انتظار بکشید...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672201" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672200">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da5fcca64.mp4?token=fMHbpccf8bNxpNAn7CQttMfGmstSrUflSA7wlZoo6sXJ74A9ltjM6icaTkwyp_KNTPO7eQnXgLP-YyeutPxlj1NKq4Un9PPHLD73FS9X-A6uFKFgOnMmfEhpzMYM6rw9Wd68xa6aJ0_pIAjXNRIld9-buSBhQ7jmOnKcxoZZYMIv5GZioXFUMLC9pzDOiLMoBEsTkO2WDD2UYoXNUJ1BWX0IUjuGq5eN44-d_cxoQjuhoVfCL40hnGY7BOrvt7jLLanltANlhdy7JPndDgvSoR-S3wLc58_cllzr95bmtbpUaRdQ6ukpuwLsytFAk1UrWBVLb85CNMoLTQTozRoTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da5fcca64.mp4?token=fMHbpccf8bNxpNAn7CQttMfGmstSrUflSA7wlZoo6sXJ74A9ltjM6icaTkwyp_KNTPO7eQnXgLP-YyeutPxlj1NKq4Un9PPHLD73FS9X-A6uFKFgOnMmfEhpzMYM6rw9Wd68xa6aJ0_pIAjXNRIld9-buSBhQ7jmOnKcxoZZYMIv5GZioXFUMLC9pzDOiLMoBEsTkO2WDD2UYoXNUJ1BWX0IUjuGq5eN44-d_cxoQjuhoVfCL40hnGY7BOrvt7jLLanltANlhdy7JPndDgvSoR-S3wLc58_cllzr95bmtbpUaRdQ6ukpuwLsytFAk1UrWBVLb85CNMoLTQTozRoTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترس غربی‌ها از حق وتوی ایران در اقتصاد جهان
🔹
حقی که اگر تثبیت شود، رفاه و امنیت را با هم به ارمغان می‌آورد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/672200" target="_blank">📅 18:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672199">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16aeb874a3.mp4?token=qFLg-_Zm7D_14iPOLfts1OfpJmFQqjWdX4gcHnLaAOvgEOYdbP8yIazgssBXOYGZMQee7C15gPaabgdk-BeOFeL4ZJgJRwZ7f1hmg8XWJj_ClMToXb5Cfo8aquS546YNNO_g456UvFwLV6PLJIHhDubruRhGRG1jbcijtx_4asIzoTreHJg7DBzfmhiwlLMfndHfX-73PxrJPcI4SMjYCiBoJp5gdmdSTGR1GCCXh-nvGi3-EZUzR4o3BSMdhbPPGk5eCs18rcqIU6_9djVelmlCLZ0f3c0-VlFQ2SCngfyQGRM5E2dmEHxx4BNjDT5SAKQQr6_5KXDqW6skD5Lq2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16aeb874a3.mp4?token=qFLg-_Zm7D_14iPOLfts1OfpJmFQqjWdX4gcHnLaAOvgEOYdbP8yIazgssBXOYGZMQee7C15gPaabgdk-BeOFeL4ZJgJRwZ7f1hmg8XWJj_ClMToXb5Cfo8aquS546YNNO_g456UvFwLV6PLJIHhDubruRhGRG1jbcijtx_4asIzoTreHJg7DBzfmhiwlLMfndHfX-73PxrJPcI4SMjYCiBoJp5gdmdSTGR1GCCXh-nvGi3-EZUzR4o3BSMdhbPPGk5eCs18rcqIU6_9djVelmlCLZ0f3c0-VlFQ2SCngfyQGRM5E2dmEHxx4BNjDT5SAKQQr6_5KXDqW6skD5Lq2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دشمن آمریکایی با بمباران پل کهورستان در محور بندرعباس - لارستان به هدف خود نرسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672199" target="_blank">📅 18:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672198">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5UQm9Pje6I1S3UW3ZZbCjf52Pw4OYpsfNaKwW2VoeEG9_6k0-6jcQFzO5PDK8I76vMnIhU74Z4OU-pte7dJ4Y7AUS1w_-waAMp5XRNqKFcnZaeoYO5Zof4GILvkWKSZ2wQD8bZww6aZS4CM7yTKxMZORNtgHHwCziuF9_FBg6YepJ_qxHy6h2IYWaWEoec4NSbONdE8B4yRHUkTUPeMDGEXrkEHRp7qQLDWdVXWumjQjohlyFudE53A2aMCpr-LpubCFpJK3Wp0b4BdejhxE96TDDIy-mFzeWL1AM8Ac467YwMIs41SRT5ULjXUwD2YmRS4-TXiDyPXSvW1Z0yNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شدت حملات آمریکا به زیرساخت‌های غیرنظامی و پل‌ها این تصور را ایجاد می‌کند که ایران به یک هدف بسیار مهم ضربه زده و این حملات در واقع واکنشی عصبی و از روی خشم به آن است
کنجکاوم بدانم آن چه بوده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/672198" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672197">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vma5ocxFQEiLC5LFq9WOw9deiD93a9kU8ig6dqsIRXcGKgD5L-yl9QjCIj7zqadaVSgUmK-xjBqchsLei-ImQETSoyu-5shltYwbzOAlmA8v7qM1JnwwiRSxOx6USk0ggNqyKwncc5P48dps8R-egXkm4yf5QLoftluVwYIIjiWVABHaernY8VzNvIfzxroJaWuJ8MhkRKs2Rhn53IlpI-CE5vW5jROKgD75o1M2XM1v5670WdnbVaGTO6ENX7aW-Yusbh7RD_zj9gOQNNbnqB1KOeg6MUkNAc9D4-qn6CnAT7axmtVic3OvZam3gGMiw-6d_uj77s9RbgxPHNP2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت ابوالفضل بازرگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672197" target="_blank">📅 18:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672196">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a84b28869.mp4?token=tGytKabP5xV9gmRhsSS0GsVcQ6YsO4NzpekmHfm2vOvrqbENe6suEQ3uGxvviYEgLxjxr0Fp0s_-Z44OZlbH8kuQTNi-Vk-Pi_r1J10xZxDC9_7HnRgpSD4ThTrZ-9IORZrHSrQ02lfi6XJTodcAwOru-tEEm58qkq-7qk4mUZG_DvbUdvDjILvJATCSIWwCjwz-eCJv3vZ6on5iiJojDUwMMzqaGsvu9qbb2CWotbZ26RDiuMK1iubsAHg-UjHgQmVgcEEWrZ7pnduUSf47kDbqXowtzSHldChSXefHbOvVB1lnxps_Aym3l37fS5C4ezujymbgZKzZ7V_4KmRHPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a84b28869.mp4?token=tGytKabP5xV9gmRhsSS0GsVcQ6YsO4NzpekmHfm2vOvrqbENe6suEQ3uGxvviYEgLxjxr0Fp0s_-Z44OZlbH8kuQTNi-Vk-Pi_r1J10xZxDC9_7HnRgpSD4ThTrZ-9IORZrHSrQ02lfi6XJTodcAwOru-tEEm58qkq-7qk4mUZG_DvbUdvDjILvJATCSIWwCjwz-eCJv3vZ6on5iiJojDUwMMzqaGsvu9qbb2CWotbZ26RDiuMK1iubsAHg-UjHgQmVgcEEWrZ7pnduUSf47kDbqXowtzSHldChSXefHbOvVB1lnxps_Aym3l37fS5C4ezujymbgZKzZ7V_4KmRHPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا تنگه هرمز خط قرمز است؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/672196" target="_blank">📅 18:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672194">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d7ddd4f3.mp4?token=CuyfqA3PbXVHGUUWX3HaOZRC_vXJgxTdL4aXcLWIZeuxCD31z5Mqu7Vlh_FuW_foPdNuXbZIIRTcj_TH1pny8Qmxg8a2UKIaJ11Oh02WMr5rXq3vTA3r-nrgs5sArrZj1_cJCHSOiQQyDmSFRa3GBHX5lktB483pmNoD3K8fw7U-zn3tvTkG7DtFO5YkjWZSIlB9xc7B7IkTtJpB2abO8zNwYgpn2gFVzm1zQTs4mYG4L4nCYn6hi4a-4ZJDBK4PKHJBlbzSH8tsu4UUz81tMunfJ7zZnssNPlVUZysVIDFLxBVDHTCFZ_cz-fzn0mOY8gLrwwUmOjkS8kx57dYU5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d7ddd4f3.mp4?token=CuyfqA3PbXVHGUUWX3HaOZRC_vXJgxTdL4aXcLWIZeuxCD31z5Mqu7Vlh_FuW_foPdNuXbZIIRTcj_TH1pny8Qmxg8a2UKIaJ11Oh02WMr5rXq3vTA3r-nrgs5sArrZj1_cJCHSOiQQyDmSFRa3GBHX5lktB483pmNoD3K8fw7U-zn3tvTkG7DtFO5YkjWZSIlB9xc7B7IkTtJpB2abO8zNwYgpn2gFVzm1zQTs4mYG4L4nCYn6hi4a-4ZJDBK4PKHJBlbzSH8tsu4UUz81tMunfJ7zZnssNPlVUZysVIDFLxBVDHTCFZ_cz-fzn0mOY8gLrwwUmOjkS8kx57dYU5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از گرما یخ رو بغل کرده
🥹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/672194" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672193">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FylQbTfffNgmoMzzDsVPklGsmwovYXXI0uk3ZRy0r4hIfyi6R-dnHUrIB78jlcdHaAo255BFdA1eV4LYlbBGBNKLdtdiSslkB4sf2AZb8DAmIDdrAHoyWnf8KuIf43x46DbFns1n6roJ2eos-A1JCmXq-zhy9n1Rp9qvIC7tw0RrTmjOATyJkH0hnwDaZVPE33QJHk3hHMnwq5d03KuN5Y8269MmkDJJ9BVr-Q_z8FPr9yIujTkdJT7YmIgtJxgWD6ieAxxMtPGHg0yteL1F5JcIX9OkyrVv7u0ui58abFgqaxINKoQHwLreUZ22RQDHhTJuaOzATHa-H1CwkauOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت یک مادر و قطع دست کودک یک‌ساله در حمله آمریکا به بندرعباس
🔹
در پی حمله آمریکا به محله «تپه الله‌اکبر» بندرعباس، یک مادر به شهادت رسید و ۸ تن مجروح شدند. دست کودک یک‌ساله این بانو در جریان انفجار قطع و وضعیت وی وخیم گزارش شده است.  #اخبار_هرمزگان در…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/672193" target="_blank">📅 17:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672192" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62390cef03.mp4?token=WZwn36Bk4XCUC9GLX76ppb0W0nZk2wIGCPAYZStlxjP5O0PokimfzPRGt9elaciq-DcHH8LNyK_yimfup09xR8WQK7BxpOJIoSrmjVfr88CeKts89fM2Tj_5DWN8dIqfesYI7bBewYX-XPjunNe0HQamij8M6Tpn0YFKRLx4x2cIhXTldtHB_bjpp5-_p56wfdFKp5K9LqX2VZ-ojDn53xQBAWi3YRB9ojOwAbXAIFFoPhZ2AuuFvet7DaY3oC6rZjtf-TZvSPdoZIt8vzMIah2azlr5dvBmv6o0xib6WfYX8GskPSTQ2WJhV2QSbJ_D4dUkSG3cOFctu_WvRq-9r3IarexCiptPD1d7kId2NraesyPAyr1a-itr_1n4T3y6D_nKQtRLTtXkdNV2uUPYQbECOLeb0JQwkGM5ulHY0VF_QEGftQSsCHAjTFLXukNDBhTo33KdqIRggT9JSV04ubYE1q-04GrxxnJFgCB5I0VnPmtPsWtzrwdUG4nP1Pt7_TvOPejOxe1pm2o2YQCzWLeVMeydvHuF7nGdLxNgjmBBS2qgImOi1pHR9B1zinNmcQLgrJMRVdlZtEKFB8i4StNhHroZFLiYPzcZnXM0pkTqvppyUIBUsddrPI7oKyTr7zRwdaOUHMo8C9vIdBPkPj4_Xx9NlBlLb056YrxsPrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62390cef03.mp4?token=WZwn36Bk4XCUC9GLX76ppb0W0nZk2wIGCPAYZStlxjP5O0PokimfzPRGt9elaciq-DcHH8LNyK_yimfup09xR8WQK7BxpOJIoSrmjVfr88CeKts89fM2Tj_5DWN8dIqfesYI7bBewYX-XPjunNe0HQamij8M6Tpn0YFKRLx4x2cIhXTldtHB_bjpp5-_p56wfdFKp5K9LqX2VZ-ojDn53xQBAWi3YRB9ojOwAbXAIFFoPhZ2AuuFvet7DaY3oC6rZjtf-TZvSPdoZIt8vzMIah2azlr5dvBmv6o0xib6WfYX8GskPSTQ2WJhV2QSbJ_D4dUkSG3cOFctu_WvRq-9r3IarexCiptPD1d7kId2NraesyPAyr1a-itr_1n4T3y6D_nKQtRLTtXkdNV2uUPYQbECOLeb0JQwkGM5ulHY0VF_QEGftQSsCHAjTFLXukNDBhTo33KdqIRggT9JSV04ubYE1q-04GrxxnJFgCB5I0VnPmtPsWtzrwdUG4nP1Pt7_TvOPejOxe1pm2o2YQCzWLeVMeydvHuF7nGdLxNgjmBBS2qgImOi1pHR9B1zinNmcQLgrJMRVdlZtEKFB8i4StNhHroZFLiYPzcZnXM0pkTqvppyUIBUsddrPI7oKyTr7zRwdaOUHMo8C9vIdBPkPj4_Xx9NlBlLb056YrxsPrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش دوخت خلاقانه کاور برای دستمال کاغذی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672190" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672184">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: شورای نگهبان افرادی را فرستاده بود که از همسایگان من سوال بپرسند که آیا همسر من چادری است یا خیر/ شورای نگهبان کسانی را مامور می‌کند که در خانه طرف بروند که ببینند ماهواره دارد یا ندارد!
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
خیلی‌ها را به خاطر اینکه حرفشان مطابق نظر آن‌ها (شورای نگهبان) نیست، رد می‌کنند. بسیاری از این نابسمانی‌های سال‌های اخیر محصول تفسیرهای شورای نگهبان است. تفسیر کرده‌اند از راهی که دوست داشته باشیم، می‌توانیم نظارت کنیم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/672184" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672183">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458316cecf.mp4?token=nAwmeLqFSwIoxcgHKn3pP0m9RFgT77aRs5a_H1DQ0-iwPrCWfM8_QPlQ8i8oie4jt5UtkN2SuFhCnEIkI4UN2m2uQWdAzvHOXcMLGacFjukrvfQY8lRH25DsZrudB4gN9WUoUkCwS-VYVK1eScvtZ96aQATrmqGy9eApA2NRui2p0Gd0MNF8T5zvK_tQVK7kU2xxi1mgqa-Qq7rSGCaKFHlegePAyUY0xhMHM-QsFD-BqDAvR1EfVevsalkofOjCXh79fmV4Fm3-V1vhEovXP3InT2peeUsoECNBZTfAtctYWmsWGw34GTl745GWxELXfN_VI_qV225ksne48A9rHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458316cecf.mp4?token=nAwmeLqFSwIoxcgHKn3pP0m9RFgT77aRs5a_H1DQ0-iwPrCWfM8_QPlQ8i8oie4jt5UtkN2SuFhCnEIkI4UN2m2uQWdAzvHOXcMLGacFjukrvfQY8lRH25DsZrudB4gN9WUoUkCwS-VYVK1eScvtZ96aQATrmqGy9eApA2NRui2p0Gd0MNF8T5zvK_tQVK7kU2xxi1mgqa-Qq7rSGCaKFHlegePAyUY0xhMHM-QsFD-BqDAvR1EfVevsalkofOjCXh79fmV4Fm3-V1vhEovXP3InT2peeUsoECNBZTfAtctYWmsWGw34GTl745GWxELXfN_VI_qV225ksne48A9rHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارخانه‌ی شکلات سازی/عجب جای شاهکاریه
🍬
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/672183" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e468509e2a.mp4?token=iIDAXW07s39X6MBXIhyVSidbtivIb9fQi6W5EuF9t88bZM3qm-6sUbYR-G3in641dS5gbmK8Ck3e0LZM_y-iUiHJ3hdp8O3VRsMFqdDNlX4H8MsbyqGCpRC3xZEE_P9CnEW-ksqhzpuwAinYl8VaQp9FEHl1_vsKeb1o76BRnEYbw_hXa4WhCbDMJ5CsWNU6dzkLGEPXyApjgkmyyRYwplDKIxd77tOMJqvwhaOSv_fmpt6WoVwf6wW81E7Adk2qU9gEqW6P8KcL33Z1PN_deXLx-o4ix1dLoiD7tcFVVJeNl_eG2_K6gd-O43DCRGuUH2XJ3Dhwvn2uZF78HsUJlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e468509e2a.mp4?token=iIDAXW07s39X6MBXIhyVSidbtivIb9fQi6W5EuF9t88bZM3qm-6sUbYR-G3in641dS5gbmK8Ck3e0LZM_y-iUiHJ3hdp8O3VRsMFqdDNlX4H8MsbyqGCpRC3xZEE_P9CnEW-ksqhzpuwAinYl8VaQp9FEHl1_vsKeb1o76BRnEYbw_hXa4WhCbDMJ5CsWNU6dzkLGEPXyApjgkmyyRYwplDKIxd77tOMJqvwhaOSv_fmpt6WoVwf6wW81E7Adk2qU9gEqW6P8KcL33Z1PN_deXLx-o4ix1dLoiD7tcFVVJeNl_eG2_K6gd-O43DCRGuUH2XJ3Dhwvn2uZF78HsUJlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه پایگاه العدید قطر؛ جنگنده‌های آمریکا به اسرائیل و عربستان منتقل شدند
🔹
تصاویر ماهواره‌ای از خروج ده‌ها فروند جنگنده و سوخت‌رسان آمریکایی از بزرگ‌ترین پایگاه هوایی آمریکا در قطر حکایت دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/672182" target="_blank">📅 17:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rxo7cdymPIX91Zs50fKVmkCgpZCcjGRgPcX3ynIEnGg91t4f6fSWGY59djkHej9SBDCaRKiFv2fqKhtQU4uPF3Tixho3jlaAZko4kqLkBIs6dFbIaneJqr4mC6m-sjbaiKR30rnbODUF9HwNEQUqGEpeRWAs4fXlxB4oK1WVs8-ByAUnbUNUepothiKnZnolnDtDDeJhPmEDSiArxoKgLaD5zqQFpfa5TnGMNgYiYlmr-v8K2PPsZvDaJdiAudKc3VLZPMd-iPJk2-xD45aoh4AyTk32FCR3f4UTyhyf4tsTl9KfDg_rbwdg0rQTfLns8BGbdXlwgAKTY1pewIK4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H59_WhzC7jR-UjR3SI-gZLfamE54Jx_7FIIHZMoPffIenqBZJL75w_6Qrd5znYrvLE1x7HwYt-Qoi-E_4IPDKNINIlCYKUP_3J11S_0WbJBx4r-gN7fFIMOdhaXPyfD6vdh7L47MeEQGW-xizpfOGwM_uBiKGOATSebswbcwoK0evGGKcXou_t1I7OfRg2lBlLf56FtmMi9z2Mq9RalyvGj6ZQZ0VPpuv-xW1ckiMvHzXjTQx2lYKY4q76ZGodOmRPGEph9rs2jEgQAROZ7VHMM7pnYryDCI4bC0gp4v-Kv7iPDVB_-_6LMoHBsHnpAVecvcwjIrhHVtD4ib-ezzRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTO8W3EBkGpSE4YeVymfXIxMAjK7JSpzgPD4QdPyyB_sK5wNG25JZ_xd0JEmQEtQ5xCgKzuf8v_sTGJYP648O3mJndWO8jvYcj4-UPiG-PaW-m9woWucBtX2HSFnwm6E-xb9jKsr0nb2vIQr8KzSrD1J6RPORcTgqXGnV-_y7te5xHcqM9Exgzep6c7hAR7eO1_wu503gsD7XdDBohFbS8EIg-t0M1lvxAyYWZO2HkiN8ty2wS_uGIpNQj3ucKB5j1nNj-GeXrwEjByEFOWlcb7lGpZSQCqJN-0Ai4EEv-scYKPI40Rx_jOinNnk8PZaTnAbu_H7e5KmfkEnJooXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jILjTZLnjdTmO6WmarGHDLB_FL4vMsw3d5wRZ24Hnh-4gJVB1nZE7e1Hl_L0mCI85Q89LekJ2CSGirACcPw_US2qAp6IUpjO7knjnFd7PMML_8--JvmgirhIZTUcBY5g7Ifp5-irpoUZBpZyxU3SyyoA2BagADk2fA9qtqe8-NPoZcCWOWShRnzngwuB-hsRlvaT6lPx1ophZ50PBpczPj3StCocOKLSE8_ObR4CfBYCXi9bLx3e0hy0zvDdJwVpAo7-l52Qi1eTk2xlK-ccnBjLsvqa980COFqDoXh_gXWDIiB3ij4-AkJcEfB21RJ1FVaf2gjWx2hf4Vtj0BNpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ev2FrqrLMKbzMmhNTG7ITUjBpd2yLyhLmDOefoJedPwTR06czemW9hpDRknidISo19BBzKdUHIr9KkI4SyODRy94gVc3ZAikA0ERgnFcEuDmN56cK25N5TDnU5BC_wSYUzQa50gCYMuAgdMxj1QHpQrnDBf_A2nLQuNBtC6IL77onjuGRccTzCPd53lNnu28XsJ0esx6lJyI9t44x6nNn5vPWpRWZxORIu81Thh-19KAzPDh3cnB14xtAEUI3pKNYtmxcmp29aIgqJkEGDzFu9TV4U9O22RByHkvDv0PpDctYjmyCZlTiCilZHew6AAEecfzNn5fsIAyhwXWYlo_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ae6uMQm_VaqLK1H1iwKj9dYgfzKy2viK1kzdGiGKXsTCEalwAbofBFo2ocFxZG-RYBkXHOfZG_rzuhRSGm6LgMfM9XLUZ7vxqGKk4quBdNups7ISCnoYBQCqwJtMOkz1K1VMNxeKiBezknu52nzd0Z5deFXJtL1Zi3-ezlAuYr4_EbzXWfRY9vKf_7YYNIYjQOtyU38rGgqT9m47zVi63yovf3XhUkWnYPJDUe6I2BB1I7UyohFUweoE_2KjRlixxdlS4LjUYtfdMezHZAYKmn87-fjIMAdGHuBKj1GBfpprBPRUR--Nf4a6aH30X9nOZckNCVvglKoLL9htLUpoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u09AkJM2tiRFdVXGO_yzHz4KSHf1TsPDY5Hnfj9h3Ui5eVpWgC4_AvnPBblq7PQvEI1jd9oTQmA_2BG2S1AiMZxrxtD8tEa974az3whyObd-kCCnyPSr-8q_PD61IxoCLCAl9DAQNVlf27B4xWBPaRYtpW17UOZEjqPf6bb9Mkx4TUpU0IarlcR5wOpeMRA7N5LBdr9w1rsveizJVkLi3LzihF6zttycp5qjQqY0ARDzVUxCQzeQDpysChQ0Sq1NaIXBeOHwheueWN7tQg_pyTkOpIfEuJgD55ICeDbTvi1-_6-xzKB0za1X5Q3ioWWY6QrXAM6wxe4zY6PAwIksPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WM5f57qCRtIaVQjsGe1mi31xdmwoJ2HTCiFZi1QPPGplD4l81I77vCI2_FVARBPPHbJHt4CnRmHsDY7UyiFbd87Xh6tQcgcWkMMpA9Kny65IhM92tir9yMCM9-QhiTZFlZEB3Yobc61t2UIgU4pJ7P__o-kiDopZN3vXx8GL1GVWIM5SdPYxX_mrq9j2k1mpvkKo8ZZ__3r_ZKuYnGBS3-wmPL2XJst9ThL0-o7psJAyLwWAMPyNBJ1bM3xZEuo-15Mj8_yum-I828GORUyGHMOKDIBoDkXjz9PoKlDwti785gWDEU91O4jU1iQlgj5Bp7sPH--6wlRpo_sZwiuQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLXY-cGfZ233NGnpbXNNIOGX7lcJkqmeO6v4KxhA7ECrVqTdhe7W-VE2N5tNArsW7Cy7695vSR-zOmFz1Pjv1XthneKIWFEeShLIVOgbSmdidOPSAlJf8n7lHXoIAKd6aN-YupJ2KRB0PNsYd2IMhGNoU_jVn44zYGERuJCfqL4PoYG1Q7L0rNCkiG7FTWtsvZc8dTgHXPY80cmMEtbum_5vWPsEMq2x3HskXMPd25_bDCStygkoByjvadFXd7f1jh2rM7xpvF2O1olrJdx4eb9x3KNE1pFPT3qaCDisB4HBmwAmoTdfPkSdWFRw9kJK9h5wPfGz3-gMk8imasl6nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی از جنایت آمریکا‌ در حمله به پل‌های بندرخمیر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/672172" target="_blank">📅 17:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETniqasXkCe4wZa3EOG1CF_v3tVn60KwzX5BbSNtlbYBaWM8H9EeaSYrVJ4QetA9MrCemeiZSTo_RfyWnlts3GsF46gcDslUU9hZ7_ECwfln3xSyZHQG0Nx1v-zyxrRfV2CLnKrxBBcWLO5SYGVco2enPBQwZBfl0u1yHdBJVSejJcfYEiP780hAbBz9ntQgtKF-K5JoN0a55YxUuG2k5lSgPegEEszAH_03lg2X8o9Kq4_uJKdMkRGeE-xbKmY3TBk9MGi5Gz3LQ3_V3K7P4b5yrAEg2hVPOH0rCVzRsot49nUQV4j51P5cTLASd9qqa8Bg8K0UoSo2VQIW-LzvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/672171" target="_blank">📅 17:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672168">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
برخورد پلیس فتا با کانال‌های مدعی فروش سوالات امتحانات نهایی
رئیس پلیس فتا:
🔹
کانال‌ها و وبگاه‌های اینترنتی رصد و با گردانندگان این قبیل صفحات، بدون هیچگونه اغماضی برخورد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/672168" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672167">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIgq7ROBc1n9jbDEEE1s9yGfrCw3mML3K93BKrcMvrNnD27DulUC5PfZrwRov650QXNhAARcgIe7rmeSDUddHk-g79RtKUSlOmFf9d9291POyHMhVpxSqyKjODNLnpRzEvEgyTg7VrF2q_GWWgFK_cysqaTKOxKEcTYZD1mwpk5u0SrNy9O4_99tQpn_mEs_UfcJ1q4caQTklpF3CqcmBe-_0L-rHh-T3vkve-QNIAqdQVqkMqMkThy2sSrmp5OD6rB9P4fZoyGArfHvc_y2hlnesFkq8DDtlwUn_4-mKr7IIEVNQD8NtAC_X4oaeT9y0vd4jHcyPYunNC_Tgmk6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانه تامین کالری در کشورها چقدر است؟
🔸
این شاخص، کالریِ در دسترس برای هر نفر در روز را نشان می‌دهد؛ نه لزوماً کالری‌ای که افراد واقعاً مصرف می‌کنند.
🔸
میانگین جهانی کالری تأمین‌شده ۳,۰۵۶ کیلوکالری است؛ آمریکا با ۳,۹۴۷ در صدر و یمن با ۱,۸۸۱ در انتهای این فهرست قرار دارند.
🔸
ایران با ۲,۸۷۵ کیلوکالری و رتبه ۱۰۷ جهان، کمی پایین‌تر از میانگین جهانی و بالاتر از کشورهایی همچون تایلند، هنگ کنگ و اوکراین قرار دارد.
@amarfact</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/672167" target="_blank">📅 16:52 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
