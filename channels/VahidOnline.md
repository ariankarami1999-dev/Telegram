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
<img src="https://cdn1.telesco.pe/file/L-2f71w1P-i-yzzeFU4GmOqIin94hMkK0tyfLHyXpwFbzSvVi3Qv3UYAlkXwmtm4QiLS61ip2lpb1XhwdfHEiWn0E6uQEB-0-fYgopFhTv4XvDLKpmOhMHFb6Pe7zrBAzoNk4qbk8r2HQuGeYp6oRzL_NGoTK8ZpSzRMNxDpHYaREYRC3T-2K4-jJHY670yK62YoQQY-kU_JFXZjR6erMX_sqRazoCXnwPmTNB8deP_Dsw6PXfgfvNQiRcfNgAfI9uEysTb838t3PWasUieFCkOirgTr-iHO-K5C0FbY__RUtLJlUViiKZVF3-u7aKDGEuhytBWpDN01HFX5wAjm1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 15:00:30</div>
<hr>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rpx9jVo1H6ulKnsZvvJVHLzkftfEItpY5UDMQz7NQP2Imy_6v3DOslnXVTSqphzbJiGL4IaC5Uq1gYJNLrtkEhXcL5pcnLteqWn05p6w6rfntABOUflwC98tgZUMR8UEvh0Ii6nDT4K8ISglWJfxUk7_2o4a92bBZa8XC6FY_mTAfHFo6IkCitXNsy4Rt4ssHW8fn0Pn9RgaUNDmDfZl6G6k5nwJ6CLO6ZeUe0oZpgNEDn70N7DCyZKuZRDkSJxh3SgG83OqLROjaYpIRxLFn--al5RbTdDve3K7ziXfV5HA-yRiNdIdPjznmxo5EVMidVk0qv8vwRNCX-FllUBboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ با بررسی واردات گاز ترکیه، ارزیابی کرد که هشدار جدید واشنگتن مبنی بر مجازات اقتصادی کشورهای طرف معامله با تهران، این کشور را که متحد کلیدی آمریکا و سومین شریک تجاری بزرگ ایران است، در برابر چالش قطع واردات گاز از ایران قرار داده است.
ترکیه در سال گذشته ۱۳ درصد از گاز وارداتی خود (۷.۷ میلیارد متر مکعب) را از ایران تامین کرد و ایران پس از روسیه، آذربایجان و آمریکا، چهارمین تامین‌کننده بزرگ انرژی آن بوده است. با وجود انقضای قرارداد ۲۵ ساله در پایان ژوئیه، دریافت گاز ایران همچنان ادامه داشته است.
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرده است هر کشوری که به روابط اقتصادی با جمهوری اسلامی ایران ادامه دهد هدف تحریم قرار می‌گیرد و دونالد ترامپ در حال رایزنی مستقیم با رهبران جهان است. این موضوع احتمالا شامل تماس واشنگتن با رجب طیب اردوغان نیز خواهد بود.
بلومبرگ ارزیابی کرد اردوغان که ماه آینده عازم واشنگتن است و برای خریدهای نظامی بزرگ از جمله جنگنده‌های F-35 و F-16 به چراغ سبز آمریکا نیاز دارد، بعید است به دنبال خشمگین کردن ترامپ باشد. به گفته کارشناسان، در صورت قطع گاز ایران، آنکارا می‌تواند این کمبود را با افزایش واردات گاز مایع (LNG) گران‌تر— به‌ویژه از مبدا آمریکا — و اتکا به ذخایر پر شده خود جبران کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/78045" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H0zFD7N0VvY7rXvAnnHwFs0wrrnKVVeV3S8o_NK8yES_gGviyE4Eue3C6Fv1iIzGDmmi4RB_l7hjhonLp8phVCtV41c0G4vaOUdTjmXW5xsqbH4MsabPQBhI1r30-kf-mX9ShORefpkQWJs9-xMYZNSDzA-tBReCy4W9VFlNiPjrh9FkbkS4P6iDV28Kg28f37oQ7MWNp-paAI0BZjdlpeUs6_qqECXsIA8-pNq9wpMyvg6HUZ08uU-gJ2gTBjRBM1wCwuNmLEB6Qpcx57rkPSte0u1nXn0nSkMU7UB-bAncAd9dA9PAJ3fK-p6zD2GeLGnzY_4o3GXJZJ59nio7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان هیلی، وزیر خزانه‌داری بریتانیا، اعلام کرد دولت این کشور در کنار آمریکا و دیگر شرکای خود به اعمال فشار اقتصادی بر جمهوری اسلامی ایران ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با «فعالیت‌های خطرناک ایران»، اقدام خواهد کرد.
هیلی، روز سوم شهریور ۱۴۰۵، در بیانیه‌ای گفت دولت بریتانیا از زمان آغاز به کار خود تاکنون بیش از ۲۴۰ تحریم علیه ایران وضع کرده است؛ تحریم‌هایی که به گفته او در واکنش به اقداماتی اعمال شده‌اند که امنیت مردم و بریتانیا را تهدید می‌کنند.
وزیر خزانه‌داری بریتانیا افزود لندن مصمم است مانع از آن شود که جمهوری اسلامی از اقتصاد جهانی یا نظام مالی بریتانیا برای پیشبرد برنامه هسته‌ای و فعالیت‌های بی‌ثبات‌کننده خود استفاده کند.
او همچنین از تلاش‌های آمریکا برای دستیابی به راه‌حل دیپلماتیک حمایت کرد و گفت بریتانیا از افزایش فشار بر جمهوری اسلامی، از جمله در قالب عملیات «طرد اقتصادی» آمریکا، استقبال می‌کند.
هیلی تاکید کرد بریتانیا به همکاری با شرکای خود برای حفاظت از منافعش ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با آنچه فعالیت‌های خطرناک ایران در منطقه خوانده شده، اقدامات لازم را انجام خواهد داد.
وزیر خزانه‌داری بریتانیا از جمهوری اسلامی خواست فعالیت‌های بی‌ثبات‌کننده خود در منطقه، از جمله در تنگه هرمز، را متوقف کند و وارد گفت‌وگوهای دیپلماتیک شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/78044" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1_DlCliR-pdi8O3uz3WHE6Zf7Js9_pwK__lq7HqZSAMhz9Pkiv2XY17-wXn81rxntsD3um8zsnX7MmFIFAyZLXsktyEwUlE3s_XZ2c8qbtjdnwjDmYlkO6IqJ_G1G0DILw418yt54wMYyF8tIWa56xBkrd3UXLTDds-PtBn1nU6eO-iG6kF4q3CgQ_78CDMzHOSpc45lo5MWWFTwPvvTcetyQpX8O1t1yGDbwHvPJDMjr70QEom9Bh_7mGOn0MGEAHPGYfCY53wOhMHf4TpRVU8v15iBsceXBefCcB3eUDbZPKiUStAaNjZBGJN1yeDW1sllVgiR2DKf51mL_xjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس، سه‌شنبه سوم شهریور در شبکه ایکس با انتقاد از عملکرد وزیر خارجه جمهوری اسلامی نوشت عراقچی بر اساس کدام مجوز از دستور مجتبی خامنه‌ای مبنی بر «انحصار» مدیریت جمهوری اسلامی بر تنگه هرمز تخلف کرده است.
او افزود چرا وزیر خارجه بدون ملاحظات امنیتی اسباب محکومیت و اجماع سازی علیه جمهوری اسلامی، به سبب «اعمال مدیریت لازم و درست ایران در کریدور جنوبی» را فراهم می‌کند؟
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/78043" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tiW9dWT44OKYJyuGXTxQyoNUvJm67XfiJb8OUBhaHn6bW3PKGQaKPLXKNRZ7ZpDgZzc5WGQffNR22dxbwQdjxhFPbk30iLv2w0edjRM5ZZ4aSUU-JLOnS-4WvzGah-AL0wbay7s-YPLmkcQMhm76qWqLnxisTc0b49aTijZZ3lSjP51Yqd5E2najFCNW_SZAmbPa9FWHBKp48OwfcoWbClpK782TgJhisDaH-aRaX-udyfZ3EamLMbPHysryUDwDQmX7biljOgNRTZhhCwvaav6B80hTlRy_TQ1GYhrGm2l7tVDK383zkhW7E6juECqpW9oK77MHgKiYZOyMYUZrZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با انتشار بخشی از ویدیوی نشست خبری اسکات بسنت، وزیر خزانه‌داری آمریکا، در شبکه اجتماعی ایکس، با کنایه از اظهارات او درباره تحریم‌های جدید علیه ایران انتقاد کرد.
در این ویدیو، خبرنگار با اشاره به ادعای بسنت مبنی بر آغاز «روز دی (D-Day) اقتصادی»، از او می‌پرسد چرا تحریم‌ها بلافاصله اعمال نمی‌شوند، و بسنت در پاسخ می‌گوید: «چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟»
قالیباف با طعنه به این تناقض در سخنان وزیر خزانه‌داری آمریکا نوشت: «او ابتدا می‌گوید روز دی اقتصادی! اما پنج ثانیه بعد می‌گوید چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟ جناب، اینجا ساحل نورماندی نیست؛ این یک نمایش کمدی است و شما فیلم‌نامه خودتان را هم فراموش کرده‌اید!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/78042" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KTDDu9T5hvfw74RIypSrDekAHyw9Su16COY-j4kz5jAs7MJr2XJeXKiJmTVm2L7ycNRxa_sOjAvIPde2M9OZFC9jlYOBz_1KHtlATRFAfri1J8AloS-Cq27aeLJSkKKHdJA37VglwLkHPGFyQsuKdnwSj3NdgmyRm2CtEJhByaJ_10FdeunBf8CggaqD9PLDn5XRprQqFE1WMuNbnRU_AbvbcpL9c6b4kW2rPbv688R4AfaABPZaATjf0k6js7l0ZQR735lK0yqEfw1vDUq9YjpvcCGJe5WsV4YKAT4YwkEnLCtoupBE92qmy4CcN5vuCJsaXdfnXMhdbzXu1URPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VkodEPa3okn7Rft9mHBQP-9Uusf0RoeFAAxY7wVpL86XInQoDHsJEj4BbJowv6_Fwf1iD9RUKDWHVWZLEPO8P6qe9GrDzvyKNXfvsXD_cuC_K0zzzwQjIUQpLoqmcXrZGQ7dNI02F-e5sF2Sfpuv-u4Iml5afKhxvSSnGVkvvOj6zGz6D2DmeRiYm1rG1xE4wSaeDyJf6lylCWudMMbqv1ByR52ioFqDpICHVkJZOFr0zjSlbuYFhxxCUyrIjbs_wA8lvlIbR3kQOe8Xt-PTxGhbImu2ijK_JJsWgCw0LE-nhWtKmTflUTtfIvshngDOABN5i9UN0l3JIbH3sPPXBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو منبع آگاه به گفت‌وگوهای مارکو روبیو، وزیر خارجه آمریکا، با مقام‌های کشورهای مختلف، به کانال ۱۲ اسراییل گفته‌اند واشنگتن در حال حاضر انتظار ندارد حملات تهاجمی جدیدی علیه ایران انجام دهد و تمرکز دولت دونالد ترامپ به افزایش فشار اقتصادی بر تهران و تامین امنیت کشتیرانی در تنگه هرمز معطوف شده است.
به گفته این منابع، روبیو احتمال اقدام نظامی آمریکا را در صورت آغاز دوباره درگیری از سوی ایران رد نکرده است.
این تغییر رویکرد همزمان با اعمال تحریم‌های جدید علیه جمهوری اسلامی و ادعای دونالد ترامپ درباره پاک‌سازی تنگه هرمز از مین‌های دریایی صورت گرفته است.
بر اساس این گزارش، دولت ترامپ قصد دارد در مرحله کنونی فشارهای اقتصادی بر ایران را افزایش دهد و شرایط را برای عادی‌شدن عبور و مرور کشتی‌ها از تنگه هرمز فراهم کند.
منابع آگاه به کانال ۱۲ گفته‌اند انتظار می‌رود این رویکرد دست‌کم تا انتخابات میان‌دوره‌ای آمریکا در اوایل نوامبر ادامه داشته باشد و پس از آن، احتمال بررسی گزینه یک کارزار نظامی گسترده‌تر دوباره مطرح شود.
@
VahidHeadline
پیش‌تر:
پایگاه خبری اکسیوس به نقل از مقام‌های دولت آمریکا گزارش داد انتظار می‌رود تحریم‌های ثانویه گسترش‌یافته، دست‌کم تا پس از انتخابات میان‌دوره‌ای آبان‌ماه مسیر اصلی اقدام واشینگتن علیه جمهوری اسلامی باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/78040" target="_blank">📅 22:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t-1CE5XHfrl7a0LkyyBAyXvrUJLvL31lsUSWzkRJ1wMNI2x7n7-nxvmFJMAD0wRGBe3XB27B6SgWVl2yW2cEAVFHftk8YQ7lKDajnjyyJ7Js5FE7B1P5GaJ7-fEO6jcKZKcDK8ushCJMBQTTMRtToDAaYHqZoQmN3Rc1pK0UYxZeHmPyQ1NDBZEbudnINP8Y-zlR9ptBger-8DkPkQEwFoEQT9G9dQbSvehe2N1TH8z3ds4xVdmoSqH7fMuV5NV2WKmxVQ3lJTxYg7MCKYi929gALPB_PqNtbwhVSCcCEf3ZEN5dmDplplTkv_ySpDMj2xgk7g9wUadt821RSRmjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی نیکزاد، نایب رئیس مجلس شورای اسلامی، در گفتگویی با خبرگزاری ایسنا از کاهش دو سهمیه بنزین بر اساس آخرین تصمیمات مجلس، سخن گفته است.
به گفته او سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان محفوظ خواهد ماند اما سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا خواهد کرد.
همچنین سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان هم قرار است به ۱۵ لیتر برسد.
او البته گفته است: «براساس آخرین تصمیمی که درباره بنزین گرفته شد، مقرر شد که قیمت بنزین افزایش پیدا نکند.»
اشاره او به بنزین ۱۵۰۰ تومانی است.
آقای نیکزاد تعیین نرخ چهارم بنزین را رد کرده است.
دیروز رئیس دفتر مسعود پزشکیان، رئیس‌جمهور ایران، هم گفته بود سهمیه بنزین حتما کاهش پیدا می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/78039" target="_blank">📅 22:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RE7vhagmjubbBxZ3wms_moFFalrtPTTIsB8qbKXBz78xgjDmQuxuBGEexBda9mF30SOviZ56mlLoe4H2ifK3ExPVcqwF8lw5W6s3lQ8xk3PG7l6376nfmdJ-e42vn2o549_4OMpb2_k51sSYK0QsUUDG4qoqKkEI8uYRW-MvfpNL8vC5wDfdZ2__Oge1hqY4AB7P5lgvzQ7njBBuxzEfNjIadf4YIpC-tVahgzGcPvXvNHZaTuuTK1K0wBcZmiDccl46R5UZMGUammbQLUuAUZBK1-pMfQ_fietUowfgIMDSpIj5cXsXuGWKPkUBTQx-EFQFPleiEkUyPUIOKie9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DBUV4pnhBYRRUwtQeIr6JYFXRKQTtxysxCpYEPEkRd4g314nWKLjqJIupJSSyrBnItd_mTdl_A2NTYuCzs_rLGCGppcmJi5AGnmlTrA0lOEu7nTItsjPrtw1KuixL6QrSZnGt_kJ4nwjyW2S7q1qHSCBaLp-RaedLqx-D22gxmhCl1NysECxGVPw8K-jHC2QZcFWaKAWYcC1bHoNSIAFfV4Wmat2QlnxzCd6NViEI823tImuSwT8EReVcncymABcYoKrdczTSiXdOG64gXS2unYAISKRvz2A9D_Cw0d-Auibl0_ATq_iov5hPvI3MBZjw22d-dl4rY3RNmxhaL8wsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rj-dM47w4dhVvLZnOW-2Bm2JhqFFZG0gPIaMCnQ0TXCKtOyMawNswgi1nrr-z1lB4jqG_iYvJi0gAMPPkA2mWD1T7tHvFTKWBwQhDF0QSfkpOsxhf_YgnT9u566gnh47AQPS1_LldwzIFztzurXHd97YQmz4aWOU7pg7vTaR2t7NhxQdVK_eLpSwSJ5KUbnxGomkBTi6kcB9aTQ2vIkHol79k4oFtF74uhMXhHvPmxhnrG-w8IRKBb5WP8bHo2PIfjG9T2MGIWl0z_Ox3aCaweYwBv8ljKZhr59VOIcsvmmoRQjdSggfepBv2Ng9-6Oe5V-TVSWCPGw5qQNNmsXimA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست اسکات بسنت، وزیر خزانه‌داری آمریکا،
ترجمه ماشین:
رهبران ایران دارند به چیزی اعتراف می‌کنند که حالا جهان می‌تواند ببیند: فشارها مؤثر واقع شده‌اند.
مسعود پزشکیان، رئیس‌جمهور ایران، با اذعان به کمبودهای اقتصادی کشور گفت: «جنگ بالاخره باید در مقطعی به پایان برسد.»
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر گفت: «هرچقدر هم قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید داخلی نداشته باشیم، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری به قطع هر شریان اقتصادی که این رژیم را سرپا نگه می‌دارد ادامه خواهد داد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/78036" target="_blank">📅 20:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gBPBxduOUZJbJ39MIvx5W9guwAosin4M-F-QfRrVxkgCM9cmYugeOcmGa_DrV9MJMmOT-gguSC7rGeC1poYw2x2RAOOyknEo2AuFHjlMbaLVVMWOIU2eShKDAnFn7R2qYIgBd36xdB4qwRFNTPwaCRdYYdxPtxIsToyj7j1UtgILsOMyTH429_sFTp9TCKakVXPsL60wikovJBYeC-qSHyw492NHuGrLgozrzub1T0Dd9qFNpBgB0FN6dYVsAks0KgoeMEGri6xy_mfjgtrxe116d3TIlIgmbcWhy6FsaKTMuRPsG6UoR5NWm6QTu1m4AwXVEGPb9YTFRAULu1CDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه
بیانیه
: گفت‌وگو کردیم که مذاکرات ادامه داشته باشد
در پی سفر بدر بن حمد البوسعیدی، وزیر امور خارجه عمان به تهران و رایزنی با عباس عراقچی، همتای ایرانی خود، دو کشور بیانیه مطبوعاتی مشترکی در خصوص از سرگیری دریانوردی ایمن از طریق تنگه هرمز منتشر کردند.
بر اساس این بیانیه، وزرای خارجه دو کشور با تاکید بر حفظ حاکمیت و حقوق حاکمیتی خود، درباره چارچوبی مرحله‌بندی‌شده و قابل اجرا برای مواجهه با وضعیت کنونی تنگه هرمز و پیامدهای ناشی از جنگ اخیر گفتگو کردند.
چارچوب پیشنهادی شامل ایجاد یک گذرگاه دریانوردی موقت مشترک از طریق تنگه هرمز و اجرای پروژه‌ای مشترک برای پاک‌سازی تنگه از مین است. طبق این توافق، مذاکرات فنی میان تهران و مسقط برای دست‌یابی به کریدور دائمی، مدیریت ترافیک، تبادل اطلاعات و ارائه خدمات دریانوردی و امنیتی ادامه خواهد داشت.
همچنین دو طرف بر اهمیت گفتگوهای مشترک با کشورهای هم‌مرز با خلیج فارس، رعایت حقوق بین‌الملل و احترام به حقوق حاکمیتی کشورهای ساحلی تأکید ورزیدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/78035" target="_blank">📅 20:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78034">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F49kGIUqN5PjxKlLrXfDKkHweIK5iFG-UMmpgiDaobNwia-f3tZvKYx1Zi-LJwTqyvmHPkMYB1wjGkozbg1F6I7BiAznIcGNPapN6Q7XVAQZSTLqjjOpk9i4WMCyQf_y3yLT1y3eO97W5505FS02wyBE3rtuMljWvMq3AvDdSowdjkOYP6u2gj3-aU7oHlKH-SNtvnS00WEw_KYf0l5gSmdTDZUefMG5oLjeKc_jlHs-36gpZ50c73fskCXEWW_3ChW4usjcZImgtnZZxJCoPz4_GHZxDs9pcMOtlUkFN7LJPTdV6R0T98mkkEPRSX4otK-dxF6RiNxZUJVMt8fBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها و ویدئوهای مختلفی در شبکه‌های اجتماعی از «تعطیلی» تعدادی از جایگاه‌های عرضه سوخت در تهران و تشکیل صف‌های طولانی در مقابل پمپ بنزین‌ها منتشر شده است.
برخی رسانه‌های داخلی از جمله خبرآنلاین، خبرگزاری دانشجو و عصر ایران نیز تعطیلی چند پمپ بنزین در تهران را تأیید کرده‌اند.
در همین حال فریدون یاسمی، مدیر منطقه تهران شرکت ملی پخش فرآورده‌های نفتی با تأیید تعطیلی چند پمپ بنزین در تهران، «افزایش ناگهانی تقاضا و ترافیک مسیرهای مواصلاتی» را «منجر به تأخیر در ارسال محمولات و اتمام بنزین در تعداد محدودی جایگاه و بسته شدن چند ساعته آنها» عنوان کرد.
به گفته او، در روزهای اخیر توزیع بنزین در تهران «۳۰ درصد» افزایش داشت. یاسمی مدعی شد «تأمین سوخت تهران به‌صورت پایدار در حال انجام است.»
خبرگزاری فرانسه نیز روز سه‌شنبه، سوم شهریور در گزارشی از تهران، از تشکیل صف‌های طولانی مقابل پمپ‌بنزین‌ها خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/78034" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sOCBx2DzPlR_Xox4RPlh5NZ8jvbjl0xCkwLUHq0Nuc0vDSpTE4I0MFq3_yv7JNLR8C1GI0EGzPNC0a_Sp6lJPR55CZSS89cejVvJXbuPnWZV3vCbqYikOR1JFFWFA4KCivgE_7Vy0hUVFnFMCL487bHxIv9hmC4URuPFqjcfTbO7WT7L-LnJt0YvTzYsowMKY7ytMGhEVopZJwrBM_2DPQqqW9yG2Jad5uDkCSwfHTPCMaO44-chyrzOfhnySSsYggLdXRerLwtQCc_npX-daxM6jWBXKhvqOODP8LzxVuxLdSH1Me2SVPBqHU59IJPZMT2XjcI9qsZlfswnQ5EA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، چند دقیقه پیش:
همین الان نیروی دریایی ایالات متحده به من اطلاع داد که همه مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدید کار بگذارد، فوراً و به‌طور نظام‌مند نابود خواهد شد.
از طریق نیروی فضایی، ما تک‌تک وجب‌های تنگه را زیر نظر داریم؛ همان‌طور که کوه پیک‌اکس و سه سایت هسته‌ای دیگر را که پیش‌تر نابود شده‌اند نیز زیر نظر داریم.
سیاست «تحمل صفر» در قبال مین‌گذاری به‌طور کامل برقرار و لازم‌الاجراست.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/78033" target="_blank">📅 18:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mkkX94DknsRVazcW5q1HrANUAuAJ37ewzPttyI7B-JSDUqc2vzRwxVOMWe0H3pt4eHaDyBucL4rfH8cQHyjW5DeuuHy-8VE4DEripwav-WMe0KbhESlTy50737xqXFT37O03oC-jGKZW93vWE0qJuvC-U0wX4F8DexpvZjbQA9GRCi1mT0y_Ww38aZDhdVZ7us2im8XCgd14TWXOIjqfI6YDfsC7cSk93BL7WhIsrtJfjPyFi86bMZ5-oqgrvWgO_yRmJ2YneCh0_v5mcV8-NUQJ-ik5ZivbzmjaB82bB5Ucr2-QjJrJtC8o7v66TeR1mgSeM57sgdb75hQdS32HrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چند ساعت پیش:
جمهوری اسلامیِ رو به زوال ایران، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را ــ حتی زمانی که در حال اعتراض نیستند ــ در ابعادی بی‌سابقه می‌کشد.
این یک بحران انسانی در ابعادی عظیم است و باید همین حالا متوقف شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78032" target="_blank">📅 18:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpzlBJnm_FcXIhGSFpcdDtu9WlTu_xbOUdY1Ev8H5RN6CdCGdnvcDsxh9wnAgJB3mKFU8jrZJ6r1vnd-8UpGEMRzkTas4RWZu3hddNnYciE-Tw8RD6SgsCarcGrBTr8CBUnGOIDN8ZpSpxXzaQdHRn5LZ015c-8RGe69_MUiKy4suVsfffULY6tCziKjKQ5_73AkcNBuYGycuqs5NZGwlILda1w--dF2jlEcfnrY4RgX12C7_ODNzuMfjftG83kAGhz7k94fhVem7rAjtIsIRQKvxuRqxwDECnyzdq_HDkTZz5unyJ09cNJfkyMLHed8OBinzzPq8fRhOUmkWXkKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز سه‌شنبه سوم شهریور ۱۴۰۵ به ۲۰۵ هزار تومان رسید و سکه امامی نیز با قیمت ۲۲۴ میلیون تومان معامله شد؛ رکوردهایی تازه که ادامه سقوط ارزش ریال و افزایش التهاب در بازارهای مالی ایران را نشان می‌دهند.
براساس قیمت‌های اعلام‌ شده، هر پوند بریتانیا نیز به ۲۷۹ هزار تومان رسیده است.
دلار در آغاز هفته حدود ۱۸۶ هزار و ۵۰۰ تومان قیمت داشت و روز یکشنبه برای نخستین بار از مرز ۲۰۰ هزار تومان عبور کرد. بر این اساس، بهای دلار طی چند روز نزدیک به ۱۰ درصد افزایش یافته است.
سکه امامی نیز که در ابتدای هفته حدود ۱۹۱ میلیون تومان معامله می‌شد، با افزایشی بیش از ۱۷ درصدی به ۲۲۴ میلیون تومان رسیده است.
جهش قیمت ارز و طلا یک روز پس از اعلام بسته تحریمی تازه ایالات متحده علیه جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/78031" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcdVZuI6_2b6SrHtC5lWpuDMWq_0GILdZUqdGIm8XzA7xQJmodSmzDB2OuKlzOnj9funtTRKpZHlkGTa-QyaW38v3Ghtw1G85RsLfvQ9WnkbnOiHLSkPZJgOvmq_J-HA8CyZX3s8bI-slYbkR1XAPwi1n8E2dgMTaMxAEnMxQ47V4nnPx1QHbbUrDWmopJmvXDgNCKJoJvrKTyhtrSXzQBAfiuRjGxQlcJmFaRrS6ZhmACfsWHYxq_TJHSHlYXaeknkita3srqT0GMwYCWVy7SzT6vg_mtHKigGHnS6_kdoXgIofT73rqtbGHtZOePMeUxJfulres6Wu-O8m3RSk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتایون ریاحی، بازیگر پیشین سینما و تلویزیون ایران، از تشکیل پرونده‌ای برای خود و ارجاع آن به بازپرسی دادسرای فرهنگ و رسانه خبر داده است.
این بازیگر با انتشار تصویری در اکانت کاربری‌اش در شبکه اجتماعی اینستاگرام اعلام کرد که پرونده‌اش به شعبه بازپرسی دادسرای فرهنگ و رسانه ارجاع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/78030" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UXAcLexdKHg7cSXhGU5qAtAfiPgp6EM_JiwGWSLlvsnwhAJpfLv-tdCsMYQJqCmw0E0OVL40JCBqK_abwkZz7c_6DWO9taNAIo70rzH-LIFUZIkm89CMlfePC5UuQHD-wwJwlVHoyxi1s_9sqWTMcO2PeSjZXpKCN-5OqXhDpW4D8ZtpJkIs126twH5wnFdxpgjnh5rN1FY_CU17LRDBSTuoN-Hc-cJxOpHIMIjnPcHdb1c4cNIER0z7LVhegs6xfS1mJNiyU5IIkICWVbBnePEp9fW3c0UfJONk6SFfvxvAA-4EBBltXjc1wplXVKk1po3qwP5PmMvEyUpXsfG_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ade157391.mp4?token=jAlA6WydYOyZSanDESyDxqEW_aZZIbjxw1osDquji4FzTi9wZSa-GlPCw_D0UsbCi-xx_NNbZgvvpnJcufXVsX8pCJCnORi-wwDxal3SEDakLr93TUWhYfUL9F11qtsfCxweKzptfQRPz2uzdRTH4-2NmSjhn3D-J49r1vD9u_qJn-Sr5AwMPeotJCSHbhG8yUjtG2XE-os0uXgZa9mOVNpEimJyUwDwXrU5cKGYnHSIDpc1T3R-yqB2hOmrcqL8t4IeOUh2JvpInu38bXkibWFLlZ4iBS62vuM5xY8ob7z2CW31DQUTwuGDnc0dTzDKOCIac-UDPPGDPfTB4YFiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ade157391.mp4?token=jAlA6WydYOyZSanDESyDxqEW_aZZIbjxw1osDquji4FzTi9wZSa-GlPCw_D0UsbCi-xx_NNbZgvvpnJcufXVsX8pCJCnORi-wwDxal3SEDakLr93TUWhYfUL9F11qtsfCxweKzptfQRPz2uzdRTH4-2NmSjhn3D-J49r1vD9u_qJn-Sr5AwMPeotJCSHbhG8yUjtG2XE-os0uXgZa9mOVNpEimJyUwDwXrU5cKGYnHSIDpc1T3R-yqB2hOmrcqL8t4IeOUh2JvpInu38bXkibWFLlZ4iBS62vuM5xY8ob7z2CW31DQUTwuGDnc0dTzDKOCIac-UDPPGDPfTB4YFiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرویس پلیس مخفی ایالات متحده که وظیفه حفاظت از شخصیت‌های سیاسی در این کشور را بر عهده دارد در بیانیه‌ای که روز سه‌شنبه منتشر شد اعلام کرد از وجود ویدئویی «که به نظر می‌رسد بارون ترامپ را تهدید می‌کند» آگاه است.
اشاره این بیانیه به ویدئویی است که گفته می‌شود در شبکه سه تلویزیونی حکومتی ایران نمایش داده شده و حاوی اطلاعاتی از محل اقامت و رفت‌وآمد بارون ترامپ، کوچک‌ترین پسر رئیس جمهور آمریکا، در شهر نیویورک است.
سخنگوی پلیس مخفی آمریکا در بیانیه‌ای که به شبکه سی‌ان‌ان ارائه کرده تأکید کرده است که این سرویس درباره هر تهدیدی علیه افراد تحت حفاظت خود تحقیق می‌کند.
شبکه خبری سی‌ان‌ان در خبری در این مورد نوشته است که از زمان کشته شدن علی خامنه‌ای، رهبر سابق جمهوری اسلامی، رسانه‌های حکومتی در ایران بارها مطالب و ویدئوهایی درباره طرح سوء قصد به جان ترامپ و خانواده‌اش منتشر کرده‌اند.
حدود یک ماه پیش نیز خبرگزاری تسنیم، نزدیک به سپاه، ویدئویی منتشر کرده بود که در آن شکاف‌های امنیتی پیرامون ملانیا ترامپ، همسر رئیس جمهور آمریکا، بررسی و درباره راه‌های هدف قرار دادن بانوی اول آمریکا بحث شده بود.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه دوم شهریور ماه، در جریان یک تماس تلفنی با برنامه زنده تلویزیونی در شبکه ۱۴ اسرائیل، در پاسخ به پرسشی درباره تدابیر امنیتی برای حفاظت از پسرانش گفت جمهوری اسلامی یکی از پسران او را هدف قرار داده و تلاش کرده است او را ترور کند.
به گزارش تایمز اسرائیل، نتانیاهو بدون ارائه جزئیات بیشتر گفت: «ایران یکی از پسرانم را هدف قرار داد. ایران سعی کرد یکی از پسرانم را بکشد، به قتل برساند.»
نخست‌وزیر اسرائیل در دفاع از توافق خود با شین‌بت برای تامین امنیت اعضای خانواده‌اش گفت: «بنابراین، امنیتی که آنها دریافت می‌کنند یک کالای لوکس نیست.»
تایمز اسرائیل نوشت، نتانیاهو با اشاره به توافقی که بر اساس آن امنیت پسرانش و همسرش، سارا، دست‌کم به مدت پنج سال، حتی در صورت شکست او در انتخابات آینده، تامین خواهد شد، از این تصمیم دفاع کرده است.
او با اشاره به مهاجمان احتمالی افزود: «بدون این امنیت، آنها موفق می‌شدند.»
مشخص نیست کدام‌یک از پسران نتانیاهو، یائیر یا آونر، هدف این سوءقصد بوده‌اند و این تلاش چه زمانی و چگونه انجام شده است.
آونر در اسرائیل زندگی می‌کند و یائیر که از برادرش شناخته‌شده‌تر است، بیشتر سال‌های گذشته را در میامی گذرانده و به اظهارنظرهای تندروانه شهرت دارد.
بر اساس گزارش تایمز اسرائیل این تلاش در زمانی رخ داده که یائیر نتانیاهو در اسرائیل حضور نداشته است، اما مشخص نیست که آیا او هدف این سوءقصد بوده است یا خیر.
در این گزارش تلویزیونی همچنین آمده است که طرح ترور ادعایی چندین ماه است که برای نهادهای امنیتی اسرائیل شناخته شده، اما مسائل امنیتی مانع از انتشار جزئیات آن شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/78028" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AzP3_coAxyNCjahLXL_NOFJgTQ3IG19Ybjgfxb4fVm1oF6oeAX15xhqna-F7ml7A_ETdv8ZTdCUyLUS7-zSqQPLBaVC3VKLOoShwqYmi9iXIHgpXf-OFsOKLH3GbIP_QqLVhOS8U_zG4Nxd5zek4mK-nh40oM8BjtCHq740jYhqWvjLLjGmw4IHv8FxKEmm-ppBKAek6EUOKSZyFyvgDUesLeb8PH9UTbPVbE5UEgDehcEbd3N5OVK3e4Y8YUHsYIA766sXIwBa26PReqczXYGfewLtsY3_mNAFQ-HM8WzjV73rOzvYOBb4t62rZ_EjWKNasJsqB9IBomRJTry9xZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه چین در واکنش به تحریم‌های تازه آمریکا علیه ایران اعلام کرد همکاری پکن و تهران در چارچوب قوانین بین‌المللی انجام می‌شود و «نباید با دخالت یا اختلال روبه‌رو شود.»
لین جیان، سخنگوی این وزارتخانه، روز سه‌شنبه سوم شهریور گفت چین تحولات را از نزدیک دنبال می‌کند و برای دفاع از حقوق و منافع خود «تمام اقدامات لازم» را انجام خواهد داد.
او در ادامه تأکید کرد که چین همواره مخالفت خود با تحریم‌های یک‌جانبه آمریکا را ابراز کرده و آنها را غیرقانونی دانسته است. به گفته او، جنگ اقتصادی و فشار حداکثری «تنها به تنش و درگیری بیشتر دامن می‌زند».
آمریکا روز دوشنبه تحریم‌هایی علیه ۶۰ فرد، نهاد و کشتی مرتبط با ایران وضع کرد و هدف آن را قطع «راه نجات اقتصادی» جمهوری اسلامی خواند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی را که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
چین خریدار اصلی نفت ایران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/78027" target="_blank">📅 17:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EkfBFG4w_Y-RSvh__UuUZiTEEdUNPF8xT-50zpR74lpBgRcF82vA0787nN6vEcZLjLQC3y3OEaYr8zhYf2KsYz5XS84miVeE49xU6eOnx1N2TE_rx05B_WICKoXfKeuG9ej2Qh5Z_rppBNLPF6-HQ17TzsJ6WBeFKDj78B0zJyX-T1T2K4MFHVbfCpU-1UI8rUNknk8h0V7wAGLsslBfykN6TCk8XWdUf36iZv6lA7DxlpO4lm0IMJ_lQNPAJcupG5rH3hu7eI6LGfbVPmsVeukgQniy4vIxyIW0L5EMDZiO0B-3XqMCALQwS_bOgRO2k5IjvH42TtRrxZPAnn76AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی پیشه‌ورزاده، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در رشت، از سوی دادگاه انقلاب این شهر به اعدام محکوم شده است.
کمیته پیگیری وضعیت بازداشت‌شدگان
خبر داد که شعبه دوم دادگاه انقلاب رشت به ریاست قاضی محمد‌علی درویش‌گفتار این حکم را در مرحله بدوی صادر کرده است. پیشه‌ورزاده در جریان اعتراضات روزهای ۱۸ و ۱۹ دی‌ماه بازداشت شد و اکنون در زندان لاکان رشت نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/78026" target="_blank">📅 17:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=JiGPT8zkjeN3xfS0oqzLrowWo2XsKl4ssfnlS6fDuVdEc55y6fTl3ogBbZo6fxojOweB6iTDHv-u86_OSPnr1G3Gat_WUJS2QqMosmDzAXQy07NjwVsdwrRz63PHDq_p_iar-ztQrextDTZgff6Upi3pj2R2kOOYTs1A85w9TARN6Xm9AZ1CZrLTSBPXh4Nvp3KoweJaFYS5Hmf5vCq-XLxLpBb4oUIpKnUkMdA9ztk01E4E_FsczaAotml8Xczn1lJyYnFfSdt8t6ppK4jL_GyBcHW1iou63V7ALqCZXZ__nXaNTy_-RH0rd2EXUugE8sAF5eqixTr4oBpkPm9K5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=JiGPT8zkjeN3xfS0oqzLrowWo2XsKl4ssfnlS6fDuVdEc55y6fTl3ogBbZo6fxojOweB6iTDHv-u86_OSPnr1G3Gat_WUJS2QqMosmDzAXQy07NjwVsdwrRz63PHDq_p_iar-ztQrextDTZgff6Upi3pj2R2kOOYTs1A85w9TARN6Xm9AZ1CZrLTSBPXh4Nvp3KoweJaFYS5Hmf5vCq-XLxLpBb4oUIpKnUkMdA9ztk01E4E_FsczaAotml8Xczn1lJyYnFfSdt8t6ppK4jL_GyBcHW1iou63V7ALqCZXZ__nXaNTy_-RH0rd2EXUugE8sAF5eqixTr4oBpkPm9K5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع آمریکا می‌گوید اعلام کارزار تازۀ اقتصادی علیه ایران، به‌ معنای حذف گزینۀ نظامی نیست.
پیت‌ هگست که شامگاه دوشنبه و پس از نشست خبری اسکات بسنت وزیر خزانه‌داری ایالات متحده صحبت می‌کرد، تأکید کرد که «به‌هیچ وجه گزینۀ استفاده از حملات نظامی در تنگۀ هرمز یا اطراف ایران را کنار نمی‌گذاریم».
وزیر دفاع ایالات متحده در عین حال ابراز نظر کرد که ایران نمی‌تواند فشار اقتصادی تازه را تحمل کند.
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78025" target="_blank">📅 09:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eU1ggscMJual_qFPevdUoTYcoiK7Fwmw_nlITfuL5E_H8QkaSI5I0hswYV67fJKiYBcqHbCA_rhrESXZZ_fpgS1R7KooUyyOja4-CZ0zXkIeUBTrOopXEOrJ_pa3YTs_-rnv5pYfCcyMaAv7VUtH6MLHE-uOvgRC_F17iusj-O_Zz4dIKEa_Nh51Rij8EEtsvoGYRj0sjWwQrwrl3ypFikXkI2x9INOqmgfxAt-BoJF_I0ZclLOQgLBHEEXDgR5Y0-djzfY8DkEyLYxXt8FCc27_eApv9K5aUMbTSikwpOOEP9Snt0_G0X5AUaUD_pOnNkjM7l4sjll_t6xWDvOMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در ۹ مایل دریایی شمال‌شرق «اش شیشه» (Ash Shishah) در عمان دریافت کرده است.
ناخدای یک نفتکش گزارش داده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به موتورخانه و از کار افتادن شناور شده است.
گزارش شده که خدمه در سلامت هستند. در زمان دریافت گزارش، تأثیرات زیست‌محیطی حادثه مشخص نیست.
...
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78024" target="_blank">📅 01:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">(۱۸ دقیقه، ۳۰ مگابایت)
متن کامل سخنرانی و پرسش  و پاسخ:
telegra.ph/bessent-08-24
اعلام کارزار اقتصادی آمریکا علیه ایران؛ بسنت: همه شریان‌های حیاتی آن‌ها را قطع می‌کنیم
🔸
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
🔸
اسکات بسنت گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
🔸
وزیر خزانه‌داری آمریکا این اظهارات را در جریان تشریح راهبرد جدید واشینگتن برای افزایش فشار اقتصادی بر ایران مطرح کرد؛ راهبردی که بر تشدید تحریم‌ها و محدود کردن روابط اقتصادی و مالی تهران با سایر کشورها متمرکز است.
🔸
او هشدار داد که هر کشوری برای متوقف کردن فعالیت‌هایی که واشینگتن آن‌ها را مرتبط با ایران تشخیص می‌دهد، مهلت مشخصی خواهد داشت؛ در غیر این صورت با اقدامات وزارت خزانه‌داری آمریکا مواجه خواهد شد.
🔸
بسنت گفت دونالد ترامپ، رئیس‌جمهور آمریکا، در حال تماس تلفنی با رهبران کشورهای مختلف است و از آن‌ها به‌طور مشخص می‌خواهد تعاملات خود با ایران را متوقف کنند.
🔸
هم‌زمان وزارت خزانه‌داری آمریکا با انتشار بیانیه‌ای گفت دامنه تهدیدهای خود برای اعمال تحریم‌های ثانویه مرتبط با ایران را به پنج بخش عمده اقتصادی گسترش داده است؛ اقدامی که به گفته وزارت خزانه‌داری آمریکا، در راستای تلاش واشینگتن برای تحمیل یک «روز سرنوشت اقتصادی» بر تهران انجام می‌شود.
🔸
در این بیانیه آمده است: «خزانه‌داری علیه پنج بخش حیاتی شامل دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی تصمیمات جدیدی اتخاذ کرده است؛ بخش‌هایی که رژیم ایران برای تلاش جهت سرپا نگه داشتن اقتصاد در حال فروپاشی خود از آن‌ها استفاده می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78023" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RQptR7jNBMK0JAN-iRODkCWlEGcHX57hjKRDR1r2SD7Uraz2J2L3TncydhvSvLnC9epe3_iwiu_Nv1GOoRvg47zHD_NsybD6AsaYrPH-arXjVEv_hxnZ7_83i-IZnkM0_8x2aZRm4Si5U7pHBUfJqsjIVawqmQvKwbDIwKl30C8nIaSRQ0GZRi7a9ZX54L5xUuFiRbY6N2kGf_UMvsrAWhjiuBBcQpfhuYtoZTZ_V6CO5-T_LQ73qelo6b0FsA1Y0nUfdgnOMD-Sgzmvsz_3z3OtvOmyJk4QpVZt5IQFUxdGfr09jrio2cNOvjfTKeFsTxPIrxQQqTqbToyBo31gCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز دوشنبه دوم شهریور بار دیگر روندی صعودی در پیش گرفت و در معاملات صبح از ۲۰۲ هزار تومان عبور کرد.
همزمان قیمت سکه امامی به ۲۲۲ میلیون تومان رسید و بهای طلا نیز در سطوح بی‌سابقه‌ای معامله شد.
بر اساس آخرین نرخ‌های ثبت‌شده، دلار آمریکا در بازار تهران به ۲۰۲ هزار و ۶۰۰ تومان رسید. سکه طرح امامی نیز ۲۲۲ میلیون تومان قیمت خورد.
در همین زمان، قیمت یک مثقال طلای آب‌شده به ۹۶ میلیون و ۲۰۰ هزار تومان و قیمت یک گرم طلای ۱۸ عیار به ۲۳ میلیون و ۲۰۷ هزار و ۸۶۰ تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78022" target="_blank">📅 18:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BU4LiDU88Rk2ah2vijywH3CZrRdSEO_KlmDJ2Nybh-e6ZShwWnQO0M5s5YTX0YhrwSvBRDSeQnq9ZNBHp3KJoBfvFLqjNnjfca6LyLqOda850r3Pbj5DodPssv8MhI1748xyXSTapOutK52wCc_yPp5G3nkB3mGMYBMHWBTwIYuXb1kieswtmVp-p2Gmp99jVTmKm8lXaZX4j5QTWCOFTr9aqCNWhGAmRd4OkWbdHDLFYdD3UfJU7XuvqBDch6iiUn2cFKrrrGI_QT1nJHu33kmS3Z6_0sZzhonwpeQw-BilqdrNFXYZ2SoVdPLkdCIsHv-O4O1APfApgyIrQxW3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران کاملاً در حال فروپاشی است!!!
رئیس‌جمهور DJT
realDonaldTrump
اشاره به ایران در پستی دیگر:
دموکرات‌های چپ رادیکال با نظرسنجی‌های جعلی دارند دیوانه‌بازی درمی‌آورند. آن‌ها این نظرسنجی‌ها را در سطحی منتشر می‌کنند که هرگز پیش از این دیده نشده است. به این‌ها «عملیات تضعیف روحیه» می‌گویند؛ جایی که تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آن‌ها برای رأی دادن بیرون نروند — اما نظرسنجی‌های واقعی فوق‌العاده‌اند و روحیه در کشور ما هرگز تا این اندازه بالا نبوده است.
ما در برابر همه در حال پیروزی هستیم، از جمله ایران که کشورشان در یک مارپیچ مرگ اقتصادی و نظامی قرار دارد.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78021" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iN0IQ4AQKoCkQQNEksLMW1Ng-XYZuVPCUNSbVodgjpDkV2RnVYB394wZ0idWsnhbQHgvqX-jfvyflKlr7NOVOpx9PwpuuK02AwWzYhX6KVEsKihRCrwx14fk1bJAVTWq5KSq4FplpUrU-4EFltEDNd8T0HyzCRyv8VgJHrsI4NwCBiUCfoLIiSQQDs7IjSG1FkPFqRY7Lv-BLB_rKAMrtW8p3Ms4s93olFJUvWS5FiXVANg65uszFVd3ggspgD8KinD1uRYnh3f2PiTrSd29WUmLXRJJQrRZSbziaujVYPzkUTFgffStG-XsQdwPoiBswFUw9eQOgso4DXM-EOLylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/REBKXAMT6kbjhJ_Ni6Xs__6JUHi5JDMZJPP77WQOqBdIN7m0emACOBdMLeQzmQsdZmGxu5qyjPk7m5-LPhbCNp4kDL7ffhW5R84W-pIn2CsseaTJ14qpsccASilmGnfJov30TxPjQ6TyAfW2kJGqF8xjUYl02PEKUIN_Mj3hqfRrbTy146XECXSWoVBoTQNmQOLygQYt-AsylkR6suqJj3QbThs8aD7df4brdcmNsLp6MqRTRBj1OwcPk3uaRXXp8Q6He-HW4cwRCQsOYNbis_EpA_q3q6b-M5FnS0SJPaMPbSsp6HdQetZA8pu11t-fGg8Hh-nxX-7wQ2YcQ2rLAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری ایالات متحده روز دوشنبه دوم شهریور مقاله نیوز مکس درباره سخنان هفته گذشته محمدباقر قالیباف در عراق را بازنشر کرد.
رئیس مجلس و عضو ارشد هیات مذاکره‌کننده جمهوری اسلامی ایران، هفته گذشته در جریان سخنرانی در جمع فعالان اقتصادی ایرانی و عراقی گفته بود آمریکا در جنگ نظامی شکست خورده است و حالا به سراغ جنگ اقتصادی و شناختی رفته است. اگر در میدان اقتصادی قوی نباشیم، شکست خواهیم خورد.
ترامپ این مقاله را در آستانه اعمال تحریم‌های بی‌سابقه علیه ایران بازنشر کرده است.
@
VahidOOnLine
محمدباقر قالیباف، رئیس مجلس شورا و عضو ارشد هیات مذاکرات جمهوری اسلامی، روز دوشنبه دوم شهریورماه با انتشار پیامی در اکس، شعار انتخاباتی «آمریکا را بار دیگر باعظمت کنیم» دونالد ترامپ را به «آمریکا را دوباره گرسنه کنیم» تغییر داد.
قالیباف در این پیام احتمالا با استناد به داده‌های سازمان غیردولتی «تغذیه آمریکا/feedingamerica» و ادعای ۴۷ میلیون گرسنه در آمریکا نوشت: «آمریکا را بار دیگر گرسنه کنیم. با ادعاهای واهی نمی‌توان شکست‌ها را لاپوشانی کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78019" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lKVneKT5JSdXfzjYy_q1uyPD7a7eqJKVGS-6n_b92fWgJBq0SVNXSqsuJx8im4VzY-vVbMdLbt5QIWjN936nTnbaQ2mvokFoxJRSff4KSSOz7rJ0KkM55WeQiNu264wlcUg0FBvEyV6oEJs-yqQONq1NlOLYGHRPWQuWSbRvcbouV8Hnc-GPK4p_4pZyNsxPfvzMjcTufYdP5hhGA3W7gJLbEWPE4HhARGao8RFmOlobhrIlR1vX4yeb1POu5wXRRbjto4qEST-XKR3Uho1_qBAYzNSj7DzfpnT1FLNgIqgYirEIah6oYz7WfecLgFPdCEQHGk3HOQzwABeo_XxDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gYpgnx6kkqO-jTo5ua3kWyHUCixbXaivEvcwmXiX-WVNYn3JcFkl7YJV0GEckgd9wzee7Os_4rz1saYTrdLqenSzhMcRMZYtArFZ6YFKphRjQVsAzzfeZfyLSAic1-wdBfhCsYQxAvVri4JVkYzF0lOBux3G0FmamN1VPQYrjzaSds4p5EII1kWNDDN7Jw3VakaU2YqEK1Vypxyx7KIkXWdVg_lW0-5Ug18_rLaA50vT2L3Lh_sAS94SnhLHRw4DxwLc4mXH9ypBYuhe_UGwW8BcgKARWlXWK77g5xnNG0Ro38cFx61KND98bbe4zeLps4ZSrK_UWqhAnWWKiYoqHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فیلدمارشال عاصم منیر، فرمانده ارتش پاکستان روز دوشنبه دوم شهریور ماه وارد تهران شد.
محسن رضا نقوی، وزیر کشور پاکستان او را در سفر به پایتخت ایران همراهی می‌کند.
ارتش پاکستان با صدور بیانیه‌ای اعلام کرد سفر این فرمانده ارشد نظامی به تهران «در راستای تلاش‌های اسلام‌آباد برای ارتقای صلح و ثبات منطقه‌ای و مذاکره با مقام‌های ایرانی بر تقویت تلاش‌های صلح و یافتن راهکاری مسالمت‌آمیز، پایدار و جامع برای حل درگیری‌های خاورمیانه متمرکز خواهد بود.»
خبرگزاری صدا و سیما گزارش کرد عاصم منیر با مقام‌های ارشد جمهوری اسلامی دیدار خواهد کرد.
@
VahidOOnLine
خبرگزاری رویترز به نقل از چند مقام پاکستانی اعلام کرد عاصم منیر، فرمانده ارتش پاکستان، هفته گذشته و پیش از سفر به تهران، با دونالد ترامپ تلفنی گفت‌وگو کرده است.
سه منبع پاکستانی در گفت‌وگو با رویترز تاکید کردند این تماس چند روز پیش از آن انجام شد که انتظار می‌رفت منیر دوشنبه برای گفت‌وگو با مقام‌های جمهوری اسلامی به تهران سفر کند.
به گزارش رویترز، این تماس که پیش از این گزارش نشده بود، در شرایطی انجام شد که آمریکا اعلام کرده است تحریم‌های اقتصادی گسترده‌ای را علیه جمهوری اسلامی و شرکای تجاری آن اعمال خواهد کرد.
در این گزارش همچنین آمده است انتظار می‌رود فرمانده ارتش پاکستان، دوشنبه با افرادی نزدیک به مجتبی خامنه‌ای، دیدار کند.
رویترز نوشت تنش‌های میان آمریکا و جمهوری اسلامی یکی از محورهای مورد انتظار در این سفر عنوان شده است.
یک منبع دیگر در دولت پاکستان نیز گفت: «منیر همچنین قرار است درباره حملات اخیر حوثی‌های وابسته به جمهوری اسلامی به عربستان سعودی، متحد پاکستان، گفت‌وگو کند.»
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه دوم شهریور ماه اعلام کرد بدر البوسعیدی، وزیر امور خارجه عمان روز سه‌شنبه به تهران سفر می‌کند.
به گزارش خبرگزاری صداوسیما، بقایی به خبرنگاران گفت بوسعیدی در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار می کند.
در پی حمله آمریکا و اسرائیل و بسته شدن تنگه هرمز، جمهوری اسلامی مذاکراتی را با عمان برای تعریف نظام حقوقی جدید تنگه هرمز، آغاز کرده است.
تهران، مسقط و دوحه از پیشرفت این مذاکرات خبر می‌دهند، با این حال دونالد ترامپ، رئیس جمهوری آمریکا هفته گذشته تهدید کرد که اگر عمان در مسیر «توافق» تهران و واشنگتن مانع ایجاد کند، این کشور را بمباران خواهد کرد.
البوسعیدی، سال گذشته میانجی دو دور مذاکرات میان جمهوری اسلامی و ایالات متحده بود. هر دو دور مذاکرات بدون نتیجه و با حملات آمریکا و اسرائیل به ایران پایان یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78017" target="_blank">📅 16:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=JBqOMxniTO45EChxZjjGo45xLz95jjgqmfmV23Aixz__tGvqU50T9nDd1lZWRZatGIhFi7DrNN6NjxAXJr5tlFizY8zqUEPDYov5TVgwkiyRRdKv_RNs8XnjfgYo5VJupNV2BUk2GvLRpmz0A8c3IFRWmp1GUr5vPUdhCRC-66bvjVX9dGB8P42S7JY6quDj1sOGmKsa9jlMqfKqgDnlT2C-Va0B9sWNHfaFMZcGNPBqAc7lvp6E4wzX6dIVol4O2HrKhrHjNKMwyepFPjqTLx8hKC3vUvN8kURjMP6xHIVtkAarkve1XXpWZUfBLCXDGsobfbQ4fpGZRVDAk_GQwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=JBqOMxniTO45EChxZjjGo45xLz95jjgqmfmV23Aixz__tGvqU50T9nDd1lZWRZatGIhFi7DrNN6NjxAXJr5tlFizY8zqUEPDYov5TVgwkiyRRdKv_RNs8XnjfgYo5VJupNV2BUk2GvLRpmz0A8c3IFRWmp1GUr5vPUdhCRC-66bvjVX9dGB8P42S7JY6quDj1sOGmKsa9jlMqfKqgDnlT2C-Va0B9sWNHfaFMZcGNPBqAc7lvp6E4wzX6dIVol4O2HrKhrHjNKMwyepFPjqTLx8hKC3vUvN8kURjMP6xHIVtkAarkve1XXpWZUfBLCXDGsobfbQ4fpGZRVDAk_GQwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@
VahidHeadline
این عدد ۲ از کجا پیش‌فرض گرفته میشه برای تعداد جناح؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78016" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W_WEsdpps_h4fRv4rOkogj92Wc2qiZRETUCsnbG7BtGpsAreOCfDFULIZF4JD1NG0E6-vw18IgzvM0hn1Ksh_jrnGXBvGDit-ymuYGIUsdTMgr0j48fGT_FqIqcBS2q483NZA9ZASMd2BFrO9nAE0GHKV_28E6Bc2KllwMfGPg8dW0sWZFZHy2UgWziRmHAPW2lKOzPbAb0sSt8FqagXMBWlsfU2dg6haWGNV1Ge7ZeOwWvkz99oH8mDjRp4KbwW0SYSKKxvqqfn_6RAsGlMPfge3VzDVNlS266P82LD4p6AXOQ72QKOQpETRO9LcmcO94rsLZxuDm-nW9kJcFsgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه دوم شهریور، در آستانه اعلام جزئیات طرح تازه آمریکا برای افزایش فشار اقتصادی بر ایران، بیش از دو درصد کاهش یافت.
دونالد ترامپ، رئیس‌جمهور آمریکا، این طرح را «کوبنده‌ترین» عملیات مالی علیه جمهوری اسلامی توصیف کرده و از متحدان واشینگتن و همچنین چین خواسته است به آن بپیوندند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه در یک نشست خبری جزئیات بیشتری از این طرح ارائه کند.
در معاملات روز دوشنبه، بهای نفت برنت و نفت خام آمریکا هر دو ۲٫۳ درصد کاهش یافت و قیمت نفت برنت به حدود ۹۲ دلار در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78015" target="_blank">📅 15:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kd-oXoHa_odfj7dTosqssz-wIHV4HdDCtnXLhXpLLbXzSfcdcjrVRqdzyRsFOejmYUD18fpvmG5gkYPJY5IuotB6cS_l5BCOzYegYFwMuR-b6MfNMqCDO7nqNu9fH-rg_j_N_vRrwXS3Z2Yy0jX0wyKHug_QFFoyLGioPyhyJkN8OPpaA0DhdvhxKr-GWTnm875DEua-tTaDq5WOcqj1EtRMApAvz2qb2xbnwR0_Ein_qnnBlGp4FjK4oz1Fjx_IVxtvLYo7POMw7Z3pZAgnP64HS5C-OmCi7RBXuhbpxUpCwaDRuNX70HQ0SyC8wVm0adggD6K5hrQiF9R5tdLsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی تجاری بریتانیا اعلام کرد: یک نفتکش در ۶۳ مایلی شهر بندری ینبع عربستان سعودی، هدف پرتابه ناشناس قرار گرفت.
این سازمان زمان حادثه فوق را روز دوشنبه دوم شهریورماه اعلام کرد و یادآور شد:‌ بر اثر اصابت پرتابه ناشناس، قسمتی از عرشه کشتی دچار آتش‌ سوزی شد، اما خدمه در سلامت کامل هستند.
سازمان دریانوردی تجاری بریتانیا همچنین اعلام کرد که تاکنون خسارات زیست محیطی بر اثر این حادثه گزارش نشده است.
نام و پرچم نفتکش اعلام نشده و تاکنون هیچ گروهی مسئولیت حمله را بر عهده نگرفته است.
ینبع پایانه اصلی صادرات انرژی عربستان در دریای سرخ است. حوثی‌های یمن ۲۰ جولای ممنوعیت دریانوردی برای کشتی‌های سعودی و مرتبط با عربستان اعلام کردند و از آن زمان حملات متعددی به نفتکش‌ها را بر عهده گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/78014" target="_blank">📅 15:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PwErIjAw7ysB7osTGj_d56AJqfR_Fo0e07J2GVVC88i1gfwUkCM9N60KTA3X7HYO8SGsUNbgUggSK3MAgRE9F9YSOFCXBKXVailZS4jsg4S-CjcbExs2x9CbXmktepvQ62JzUJLBQ7hwAt-TZSJe2Zgis1tA2S-btZGlMxnlOJGPts6xrT014s2FIhwTQGf2TCJ3STxXScE3XVC7aDp6x6MD1_Z-BglaoSYKDFpUrjybmlXSw9_0O7khXFNISVs6YYy3SP5zUNF5l4kdX6R_AeXAFXrmbRgzSvWZ-QaPdL6dMklti7VkpjUEp-5wHLtVmKrpd0ehndyD-XyDcD4XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آتوسا جعفری»، زن ۲۷ ساله اهل سنندج، یکشنبه ۱شهریور۱۴۰۵ مقابل منزل خانوادگی خود با ضربات چاقو به قتل رسید.
رسانه‌های محلی و شبکه حقوق بشر کردستان گزارش داده‌اند که آتوسا جعفری هنگام خروج از خانه و پیش از سوار شدن به خودرو برای رفتن به محل کار، هدف حمله قرار گرفت و با ضربات متعدد چاقو کشته شد.
براساس این گزارش‌ها، عامل قتل همسر یا همسر سابق آتوسا جعفری بوده است. منابع محلی گزارش داده‌اند که او با هشت ضربه چاقو به قتل رسیده است.
درباره وضعیت تاهل آتوسا جعفری در زمان قتل روایت‌های متفاوتی منتشر شده است. شبکه حقوق بشر کردستان گزارش داده که او دو سال پیش از همسرش جدا شده و با مادرش زندگی می‌کرد، اما رسانه‌های محلی نوشته‌اند که آتوسا طی سه سال گذشته برای جدایی از همسرش به دادگاه مراجعه کرده بود و درخواست طلاق او پذیرفته نمی‌شد.
براساس روایت منابع محلی، آتوسا جعفری در این مدت بارها از سوی همسرش مورد خشونت، ضرب‌وشتم و تهدید قرار گرفته بود. یک‌بار نیز در نتیجه ضرب‌وشتم، دست او شکست.
شبکه حقوق بشر کردستان نوشته آتوسا جعفری کارمند اداره پست، دارای مدرک کارشناسی ارشد حقوق کیفری و مربی و داور رشته «کنگ‌فو توآ» بود.
این دومین مورد گزارش‌شده از زن‌کشی در کردستان طی چند روز است. روز ۲۹مرداد۱۴۰۵ نیز «لطیفه محمدزاده»، زن ۴۹ ساله اهل سقز، در یکی از جاده‌های روستایی این شهرستان توسط همسر سابقش با ضربات چاقو به قتل رسیده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78013" target="_blank">📅 15:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OgrSCfrZ-Xtv5vGBbkqfr75zWhwFwWl2z8iNGsg_wneHtCyJrNgGBR3tZHSucGMIsFljUFcKpJhpwfKi3WK_-oU1gsea7k2f45v4eKZZojSyd7ttpIy9fhwp-Rk61uJAfAnUeEMSwjvhofo36jpsuFUkebr9HmypZt7fjBUjkKuEFSEZ-0bTyDH9WjRoCiDxzXn3rE9C4ee58ivBuXpw9c8oSakwCOtxd36ClrdZnCc2VeI_ZiJyR_3iGmW6Xw_EvhxSZfXb-0liVwSfSctgtBQgfuoXA4MK5n082QGfQzdP36V--QDijF3Qu66wPyecz_KRCPteW249lMF45Du6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ شهروند بهائی از سوی دادگاه انقلاب ساری مجموعاً به ۲۶ سال و ۱۶۵ روز حبس تعزیری و ۷۶ سال محرومیت از حقوق اجتماعی محکوم شدند.
بر اساس دادنامه صادرشده در تاریخ ۲۹ مرداد ۱۴۰۵، راکوئل عطائیان، کیومرث اکبری، سهراب لقایی، زهرا گلابیان، بنفشه اسدیان عربی، فؤاد لقایی، آناهیتا کوشکباغی، نسیم صمیمی، حسین فنائیان، امیلیا فنائیان، ملودی صمیمی و سهیل حقدوست، شهروندان بهائی، توسط شعبه اول دادگاه انقلاب ساری به ریاست عمار رمضانی محکوم شدند.
در این رای خانم عطاییان به تحمل چهار سال حبس تعزیرى و ۱۰ سال محرومیت از حقوق اجتماعى محکوم شده و دیگر متهمان پرونده هر کدام به تحمل دو سال و ۱۵ روز حبس تعزیرى و شش سال محرومیت از حقوق اجتماعى محکوم شدند.
در دادنامه صادره، اتهام مطروحه علیه این شهروندان «انجام فعالیت‌های آموزشی و تبلیغی مغایر و مخل به شرع مقدس اسلام در راستای ترویج و ترغیت فرقه بهائیت» عنوان شده است. جلسات رسیدگی به اتهامات این شهروندان در تاریخ‌های ۱۰، ۱۱ و ۱۲ مردادماه ۱۴۰۵ در شعبه مذکور برگزار شده بود.
یک منبع نزدیک به یکی از این شهروندان بهائی در گفت‌وگو با هرانا ضمن تأیید این خبر، درباره روند رسیدگی به این پرونده اظهار داشت: «اولین جلسه رسیدگی به اتهامات این شهروندان در اردیبهشت‌ماه ۱۴۰۳ در شعبه اول دادگاه انقلاب ساری به ریاست شجاع ذوقی برگزار شد.
این شعبه به دلیل وجود نواقص در تحقیقات، پرونده را سه مرتبه به شعبه بازپرسی بازگرداند، اما به دلیل عدم رفع نواقص، پرونده از دستور کار این شعبه خارج شد. در ادامه، پرونده به شعبه ۱۰۴ دادگاه کیفری قائم‌شهر به ریاست رضا مجازی ارجاع شد و جلسات رسیدگی در تاریخ‌های ۲۱ و ۲۲ تیرماه ۱۴۰۴ برگزار شد.»
این منبع افزود: «در جریان این روند، سهیل حقدوست و همسرش راکوئل عطائیان بازداشت شدند و امکان حضور در جلسات رسیدگی را نیافتند. این دو پس از آزادی موقت، به‌صورت جداگانه از سایر متهمان مورد محاکمه قرار گرفتند. شعبه کیفری در ادامه با صدور قرار عدم صلاحیت، پرونده را مجدداً به شعبه اول دادگاه انقلاب ساری ارجاع داد و این شعبه پس از برگزاری سه جلسه رسیدگی، نهایتا اقدام به صدور رأی کرده است.»
وی همچنین گفت: «راکوئل عطائیان در جریان بازداشت سال گذشته با پرونده قضایی جدیدی مواجه شده بود که بنا بر تصمیم شعبه ۱۰۴ دادگاه کیفری قائم‌شهر، روند رسیدگی به آن با این پرونده ادغام شد و در نهایت هر دو پرونده به صدور رأی در شعبه اول دادگاه انقلاب ساری منتهی شدند.»
پیشتر، جلسات آخرین دفاع این ۱۲ شهروند بهائی در اسفندماه ۱۴۰۲، به‌صورت جداگانه در شعبه ششم بازپرسی دادسرای قائم‌شهر به ریاست رضا مجازی برگزار شده بود. همچنین پیش از آن، منازل این افراد توسط نیروهای امنیتی مورد تفتیش قرار گرفته و آنها با دریافت پیامک‌های جداگانه از تشکیل پرونده قضایی علیه خود در دادسرای قائم‌شهر مطلع شده بودند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78012" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4jV5WO9oR0tMmdMWzYAq8VVC_SOsiLovcp4XKv1VAYjIqG2nxaG1LUBjNe0WmYDp4U3O83y_7mpfxpxjZS_gi6N0zKCps5I-YDxz43kx9qPslQO81jWR-LHTEnbZs0Q5Atlqw_BcgPdGsTVIVXaaGusdgOG6Bv7ApfWzlLYU9cwzKVzigiGppIH3Lc4AuGKnRXh8pFNgPpsgqMaNjoyPXJNSk3_Dgn_UKkwPgx1b0o1BgW5X1ysJ3fkhJnrOuzi-LsQgnHZQTV4W249rKbtcf4qxklYEGjAxndPNjTZJiv0OD27BZPifrUQ2EYFbTyGLavEpRm3agbsmhk2cHIfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با نیوزمکس گفت با وجود تلاش‌های جمهوری اسلامی برای بستن تنگه هرمز، آمریکا موفق شده است روزانه بین هفت تا ۱۵ میلیون بشکه نفت را از این مسیر خارج کند.
ونس گفت واشینگتن در تلاش است مانع وقوع بحران انرژی شود که به گفته او جمهوری اسلامی در پی ایجاد آن است. او افزود یکی از قدرتمندترین ابزارهای آمریکا، «وادار کردن تهران به پرداخت هزینه تلاش برای خفه کردن تجارت نفت و گاز» است. معاون رییس‌جمهوری آمریکا تاکید کرد جمهوری اسلامی توانایی قطع مسیرهای تجارت بین‌المللی را ندارد و این مسئله اهرم‌های فشار تهران را کاهش می‌دهد.
معاون رییس‌جمهوری آمریکا گفت واشینگتن ابزارهای متعددی برای مقابله با جمهوری اسلامی در اختیار دارد که به گفته او برخی «قاطع» و برخی دیگر اقتصادی هستند.
ونس همچنین تاکید کرد هدف نخست و اساسی حضور آمریکا در خاورمیانه جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78011" target="_blank">📅 04:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y3rrjJ3HCGthuu7xmOWtXeeVrUvEPhDwLzZhKTY35e8hVWvoM_lnQB8uBY4uPvk1J-2gP6gnIQn__C6pfl9ztot7XFi-WB3hDeT3zpLq_03T1IW2jTy8H8k96MTTai-dggIwQlIwoaXskpAevhv8RBnjdo9Pl2PJ4Okb98q2ntXYngT-72xzvXcirpcp3fORba245IAgx1dNCjVOdFSp81chjxuAUs4DsJZCNPf5iXq_CUkbI1JmdQz2B16fgG-5PoY6ulabtRvNHZ7Xq7hwXqfARRrr4MkoSatgQQ7Jc_XbpYbMDVtrhz3u3OEA1Pn1F2GSvJJxcHiagXpeVyM2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اسکات بسنت، ترجمه ماشین:
رئیس‌جمهور ترامپ توانمندی‌های نظامی ایران را در هم شکسته، نزدیک به ۱۰۰ درصد کارخانه‌های نظامی آن را نابود کرده و برنامه هسته‌ای‌اش را مدفون کرده است. اکنون وارد مرحله نهایی می‌شویم. با سپیده‌دم، یک «D-Day اقتصادی» آغاز می‌شود — بزرگ‌ترین تهاجم مالی واحدی که تاکنون علیه یک دشمن بسیج شده است.
جمهوری اسلامی با جا زدن اخاذی به‌عنوان تضمین‌های امنیتی، به حیات خود ادامه داده است. این رژیم از محاسبه‌ای قدرت گرفته که در آن، تلافی ایران قطعی و اجرای اقدامات از سوی آمریکا قابل مذاکره تلقی می‌شود. تحت ریاست‌جمهوری ترامپ، آن دوران به پایان رسیده است. و کسانی که از خطر سرپیچی از تهران می‌ترسند، نباید هزینه آزمودن واشنگتن را دست‌کم بگیرند.
رئیس‌جمهور شرایطی را فراهم کرده است تا از هر نهاد، هر اختیار و هر اقدامی که بسیاری تصور می‌کردند هرگز به آن متوسل نخواهیم شد، استفاده شود. هدف ما قطع کردن هر شریان اقتصادی‌ای است که این رژیم استبدادی را سرپا نگه می‌دارد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78010" target="_blank">📅 03:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، به کشورهایی که به روابط مالی و تجاری خود با جمهوری اسلامی ادامه می‌دهند هشدار داد که باید میان همکاری با تهران و حفظ دسترسی به ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا با انتشار مقاله‌ای در روزنامه فایننشال تایمز تاکید کرد دولت ترامپ قصد دارد با قطع همه شریان‌های مالی و تجاری جمهوری اسلامی، تهران و کشورها و نهادهای همکار با آن را در انزوای کامل اقتصادی قرار دهد.
او که قرار است دوشنبه دوم شهریور در کنفرانسی مطبوعاتی جزییات اقدامات تازه دولت آمریکا علیه جمهوری اسلامی را اعلام کند، هشدار داده است که ادامه همکاری با حکومت ایران، دسترسی این کشورها به سرمایه و بازارهای جهانی را به خطر خواهد انداخت.
وزیر خزانه‌داری ایالات متحده از آغاز مرحله‌ای تازه و گسترده در فشار اقتصادی علیه جمهوری اسلامی خبر داده و آن را «روز سرنوشت‌ساز اقتصادی» و بزرگ‌ترین تهاجم مالی سازمان‌یافته علیه یک دشمن توصیف کرده است.
بسنت در این یادداشت با اشاره به کنفرانس تهران در سال ۱۹۴۳ نوشت رهبران متفقین در آن زمان در پی یافتن راهی برای وارد‌کردن «بیشترین فشار ممکن بر دشمن» بودند. به گفته او، تاریخ اکنون همان پرسش را بار دیگر پیش روی تهران قرار داده و زمان آن رسیده است که ایالات متحده با تمام توان به آن پاسخ دهد.
او تاکید کرد دونالد ترامپ، رییس‌جمهوری آمریکا، با استفاده از قدرت نظامی ایالات متحده بخش قابل‌توجهی از توانایی‌های نظامی حکومت ایران را از میان برده و برنامه هسته‌ای این کشور را تضعیف کرده است. بسنت افزود واشینگتن اکنون وارد «مرحله نهایی» شده و می‌خواهد فشار نظامی را با حمله‌ای گسترده به منابع مالی و تجاری جمهوری اسلامی تکمیل کند.
وزیر خزانه‌داری آمریکا در ادامه، جمهوری اسلامی را حکومتی خواند که طی ۴۷ سال گذشته هم در داخل ایران و هم در خارج از مرزهای آن نقشی مخرب داشته است. او گفت فساد و سیاست‌های حکومت، اقتصادی را که می‌توانست یکی از قدرتمندترین اقتصادهای جهان باشد به ویرانی کشانده و مردم مبتکر و کارآفرین ایران را با سرکوب روبه‌رو کرده است.
بسنت همچنین جمهوری اسلامی را متهم کرد که در خارج از ایران، شبکه‌ای از گروه‌های نیابتی را برای ادامه فعالیت‌های خشونت‌آمیز و تروریستی حفظ کرده است. او گفت ایالات متحده بهای سنگینی در رویارویی با این شبکه پرداخته، هرچند تنها کشوری نیست که با پیامدهای فعالیت‌های آن مواجه شده است.
به گفته وزیر خزانه‌داری آمریکا، با وجود گستردگی تهدیدهای ناشی از سیاست‌های تهران، واشینگتن در بسیاری از موارد در عزم خود برای مقابله با جمهوری اسلامی تنها مانده است.
بسنت کاهش شدید ارزش ریال و نرخ بالای تورم در ایران را نتیجه سیاست‌های دولت ترامپ دانست. او گفت اقتصاد ایران چنان تضعیف شده که ارزش پول ملی این کشور به پایین‌ترین سطح خود رسیده و تورم نیز به یکی از بالاترین سطوح تاریخی نزدیک شده است.
او یادآور شد آخرین امید جمهوری اسلامی، ادامه همکاری کشورهایی است که از روی ترس یا ملاحظات اقتصادی تصور می‌کنند سازش با تهران می‌تواند امنیت یا صلحی پایدار برای آنها به همراه آورد.
وزیر خزانه‌داری آمریکا بدون نام‌بردن از کشور مشخصی گفت برخی دولت‌ها و نهادهای خارجی همچنان نفت ایران را خریداری و حمل می‌کنند و انتقال منابع مالی این کشور را از طریق صرافی‌ها و مناطق آزاد تجاری تسهیل می‌کنند.
به گفته او، برخی کشورها همچنین به پروازهای ایران اجازه فعالیت می‌دهند، کشتی‌ها را به نمایندگی از تهران در دفاتر خود ثبت می‌کنند و بر انتقال سوخت میان کشتی‌ها در دریا و استفاده غیرقانونی از نظام بانکی‌شان چشم می‌بندند. بسنت این کشورها را متهم کرد که هم‌زمان می‌کوشند میزان همکاری خود با جمهوری اسلامی را پنهان کنند.
او گفت این کشورها بر اساس این محاسبه عمل می‌کنند که مماشات با تهران، در مقایسه با ایستادگی در برابر آن، گزینه‌ای امن‌تر است؛ اما باید پیامدهای کمک به بقای جمهوری اسلامی را نیز در نظر بگیرند.
بسنت برای توضیح این دوراهی به دیدگاه بلز پاسکال، فیلسوف فرانسوی قرن هفدهم، اشاره کرد. به گفته او، پاسکال معتقد بود عدم قطعیت، انسان‌ها یا ملت‌ها را از داوری معاف نمی‌کند، بلکه آنها را ملزم می‌کند خطرها را دقیق‌تر ارزیابی کنند؛ زیرا در چنین شرایطی بهای یک محاسبه اشتباه می‌تواند سنگین‌تر باشد.
وزیر خزانه‌داری آمریکا گفت «شرط‌بندی پاسکال» اکنون درباره شریان‌های حیاتی اقتصاد ایران مصداق پیدا کرده است. به گفته او، کشورهایی که برای در امان ماندن از واکنش تهران همچنان منابع مالی حکومت ایران را تامین می‌کنند، در عمل همان حکومتی را تقویت می‌کنند که از آن هراس دارند.
بسنت هشدار داد که این کشورها از مرز تحمل آمریکا عبور کرده‌اند و باید میان ادامه همکاری با جمهوری اسلامی و حفظ روابط اقتصادی خود با ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
او گفت ترامپ در حال انجام کاری است که روسای‌جمهوری پیشین آمریکا از آن خودداری کردند: پایان‌دادن به تهدیدی که دولت‌های قبلی به مدیریت و مهار آن رضایت داده بودند.
به گفته بسنت، طبقه سیاسی آمریکا برای چند دهه چرخه‌ای بی‌پایان از اقدامات تحریک‌آمیز جمهوری اسلامی را پذیرفت، در حالی که باید منافع ایالات متحده را با قاطعیت بیشتری پیش می‌برد. او گفت نسل دیگری نباید زیر سایه تهدید نیروهایی زندگی کند که شعار «مرگ بر آمریکا» سر می‌دهند و در پی تحقق اهداف هسته‌ای جمهوری اسلامی هستند.
وزیر خزانه‌داری آمریکا استدلال کرد که انزوای کامل مالی تهران می‌تواند نیاز به استفاده مستقیم از نیروی نظامی ایالات متحده را کاهش دهد و هم‌زمان امنیت و آزادی عمل متحدان واشینگتن را افزایش دهد.
او همچنین برای کشورهایی که روابط مالی و تجاری خود را با ایران قطع کنند، مشوق‌هایی در نظر گرفت. بسنت گفت قطع همکاری با تهران می‌تواند دسترسی این کشورها به سرمایه جهانی را افزایش دهد، اعتماد به بازارهایشان را تقویت کند و جایگاه مورد نظر آنها را در اقتصاد بین‌المللی بهبود بخشد.
در مقابل، او هشدار داد کشورهایی که روابط خود را با تهران حفظ کنند، ممکن است مسیر دستیابی به رفاه پایدار را از دست بدهند. به گفته او، در کشورهایی که اعتماد سرمایه‌گذاران و بازارهای جهانی به آنها کاهش می‌یابد، فعالیت‌های مالی غیرقانونی معمولا گسترش پیدا می‌کند.
بسنت گفت هر کشوری که به‌عنوان شریان مالی یک حکومت رو به زوال عمل کند، باید انتظار داشته باشد در انزوای آن نیز سهیم شود. او افزود کشوری که به پناهگاهی برای فعالیت‌های تروریستی تبدیل شود، از دید ایالات متحده به بازیگری مطرود در جهان بدل خواهد شد.
وزیر خزانه‌داری آمریکا جمهوری اسلامی را متهم کرد که طی سال‌های گذشته، اخاذی را در قالب تضمین‌های امنیتی عرضه کرده و از ترس کشورهای دیگر نسبت به اقدامات تلافی‌جویانه تهران بهره برده است.
به گفته او، قدرت جمهوری اسلامی بر محاسبه‌ای استوار بوده که واکنش [حکومت] ایران را قطعی، اما اجرای تهدیدهای آمریکا را قابل‌مذاکره می‌دانسته است. بسنت گفت با بازگشت ترامپ به قدرت، این دوره به پایان رسیده و کشورهایی که از ایستادگی در برابر تهران هراس دارند، نباید هزینه آزمودن اراده واشینگتن را دست‌کم بگیرند.
او افزود ترامپ شرایطی فراهم کرده است که دولت آمریکا بتواند از همه نهادها، اختیارات قانونی و ابزارهایی استفاده کند که بسیاری تصور می‌کردند واشینگتن هرگز به آنها متوسل نخواهد شد.
بسنت هشدار داد هرگونه ارتباط باقی‌مانده با تهران می‌تواند انزوای اقتصادی کشورها و نهادهای مرتبط را تسریع کند؛ خواه این ارتباط آگاهانه ایجاد شده باشد و خواه دولت‌ها و شرکت‌ها عمدا آن را نادیده گرفته باشند.
وزیر خزانه‌داری آمریکا همچنین درباره احتمال واکنش نظامی جمهوری اسلامی هشدار داد. او گفت اگر هم‌زمان با تضعیف اقتصاد ایران و کاهش تسلط حکومت بر قدرت، تهران علیه نیروهای آمریکایی یا کشورهای همسایه در خلیج فارس اقدام نظامی انجام دهد، ترامپ «به‌سرعت و قاطعانه» پاسخ خواهد داد.
بسنت در پایان هدف دولت آمریکا را قطع همه شریان‌های اقتصادی توصیف کرد که به بقای جمهوری اسلامی کمک می‌کنند. او گفت فشارها تا زمانی ادامه خواهد یافت که تهران در انزوای کامل قرار گیرد.
او بار دیگر با اشاره به پاسکال، تصمیم کشورهای همکار با حکومت ایران را نوعی انتخاب درباره آینده آنها دانست و پرسید آیا این کشورها حاضرند در برابر موج تازه فشارهای آمریکا، آینده خود را به خطر بیندازند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78009" target="_blank">📅 03:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fD7TcnlCxxM3f4MtNmN1c8izHjr97tILlVGOY_3bHUPnH25cgXvusq_LouvkvU855Sgq16gyKwXUwpeASlitHaSea5QLCmwL7Nmq8V4BIQDznIrJ2GwsccWQb8grCbncqmFGezSyeN--B3gvuct5knDDGMz1iCEQXaasrcsqtxmORaQeWQADwaUiQwNLmVo10PQcjBPrYYJhPHL7t6VQxBJEI7w5d3TuhL4nEHAs-nxiE4_HpKVdnXwpJZxkyLvB0l1Qa9dgBX0tE3Pipfv48RPuXBlwMK1q6zLpE7TTKwGTOtMw8V9Saqa3pNPE1D8Lf03GLeRyUgIyk9t1Ey-dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای دلار آمریکا در بازار آزاد ایران روز یک‌شنبه اول شهریور از مرز ۲۰۰ هزار تومان عبور کرد و رکورد تازه‌ای به جا گذاشت؛
همزمان پوند بریتانیا از ۲۷۲ هزار تومان گذشت و یورو نیز به محدوده ۲۳۴ هزار تومان نزدیک شد.
قیمت سکه امامی نیز از ۲۱۸ میلیون تومان فراتر رفت.
این جهش قیمت‌ها در ادامه روند کاهش ارزش ریال و همزمان با تشدید فشارهای سیاسی و اقتصادی بر جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78008" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KwdX51JCmBIFOR7wNA_F5ZkPsAbH4tobs2A30_MBjKSn-JkxFVSAl_pIvgH8I-V85u5rqokz3QhUH4rwh7b_qh3r_f9JGnJusHHaC9tQM0kntBmGdL4nqYjn1ILMaFaG3m-vOLOFKrUQgpUHIutyH47I0n6TRHdj_P4upNzsmTSqqYOIl5VJa7CFOw50iI4H1QuMX8RW54sO4y3xeCcQSICRx0KF0KmEex75TAvprXe1hcS_XxzyqpmI9fkpD3JB8zqCJwSXtEQE0l0Va1nrDpbS1vepvaaP7OimtkCUg60euMT6_mE4nwrN_FvFy0yJnvBu7YPWoensr4NOOx1bmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل حسین شنبه‌زاده، از صدور حکم بدوی موکلش در پرونده‌ای جدید خبر داده است.
بر اساس این حکم، شنبه‌زاده به اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به یک سال حبس تعزیری محکوم شده است.
رئیسیان در حساب کاربری خود در شبکه اجتماعی ایکس نوشته است که این پرونده مربوط به پیامی است که شنبه‌زاده از زندان و به مناسبت روز تولدش برای دوستانش فرستاده بود.
او با انتقاد از حکم صادرشده نوشته است: «فقط تصور کنید یک زندانی با استناد به "نحوه انتشار در رسانه معاند فضای مجازی" به حبس محکوم شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78007" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTTOi5Ft8fiEI0_86VdiLgP0agaTTlksGMEEscwiTdSnu5ZtA_f9p6Bwjv8MAsS_rp3LC9_OI5k6RM3sesaMAARwkZiWeVBeSyN-IPCKcSc0Hfk1xwqA1RFYWXF3Bm8N4J2pHPTeO_OMwXIgsCcOkEup7Nlpf6x3soKIcR4M3hLqwvaYS4ylJhgtOseZucYBzGhj3uWayx05sheSTxlWKMR-1bZvlZhBkSdS__AJxeGISUVc1xjovx0RPyOyRPud6edBHky2F89GxI6jOgyKNjzXuKpbd4zbTyPKfk2t0m-p45o8JEd7SqMXEozRxNFS1AumceP0Rvun6-Try20WDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اجرای حکم اعدام «مجید آدینه»، یکی دیگر از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در کرج، خبر داده است.
براساس گزارش تسنیم به نقل از قوه قضاییه، این حکم صبح یکشنبه اول شهریور ۱۴۰۵ اجرا شد.
مجید آدینه روز ۱۹ دی‌ماه ۱۴۰۴ در محدوده محمدشهر کرج بازداشت شده بود.
مقام‌های قضایی مدعی شده‌اند که هنگام بازداشت او یک قبضه کلت کمری، سه خشاب، ۳۰ فشنگ، دو شوکر برقی، دو افشانه گاز اشک‌آور، یک اره برقی شارژی و یک بطری بنزین همراه داشته.
قوه قضائیه اعتراضات دی‌ماه را مطابق روایت رسمی جمهوری اسلامی «کودتا» خوانده و آدینه را به همکاری با آمریکا، اسرائیل و آنچه «گروه‌های متخاصم» نامیده، متهم کرده است.
دادگاه انقلاب کرج او را با اتهام «محاربه از طریق تحریق عمدی» و براساس قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم» به اعدام و مصادره اموال محکوم کرده بود.
اطلاعاتی درباره دسترسی آدینه به وکیل انتخابی، روند دادرسی، زمان برگزاری دادگاه و نحوه اخذ اظهارات او منتشر نشده است.
اعدام مجید آدینه در ادامه اجرای احکام اعدام علیه بازداشت‌شدگان اعتراضات دی‌ماه انجام شده است. بیش از ۳۰ کشور روز ۲۱ مرداد ۱۴۰۵ با انتشار بیانیه‌ای مشترک، ادامه صدور و اجرای احکام اعدام برای معترضان ایرانی را ابزاری برای «ساکت‌کردن صدای مخالفان» خواندند و محکوم کردند.
عفو بین‌الملل نیز گزارش داده است که جمهوری اسلامی در سال ۲۰۲۵ دست‌کم دو هزار و ۱۵۹ نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78006" target="_blank">📅 16:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d23144315.mp4?token=imxFoZ6li_f9a_aijcKYEgm1LUPmORqJIsu0V2BH9bmISUlnIwC1HsVLJzaPfi7haB8CKAuD8FdOM1I6nPp7icd0x9_RSky3Uu66Tk9llvz3BndbfomMjEcXYAHV4TyabfdIjXHJ5iOoA7rKy_LvBDEKrMMRXdyeG9-PoaqfEq8x1risvLL4IiRIIGmpNyq3Fsri4oP0j1Yoj25AQe-OtGfp8a7tqLkqFso2mvzEAPfN0SINvbSO4pmdyICSLpQOUhWYNj1dPhgtUsvjOb57-RjNYRZcnPOpUSUJrP0L7FnaxSXj1nj5mAIvxVj691YLUichJj4NMIorFyVX4GROcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d23144315.mp4?token=imxFoZ6li_f9a_aijcKYEgm1LUPmORqJIsu0V2BH9bmISUlnIwC1HsVLJzaPfi7haB8CKAuD8FdOM1I6nPp7icd0x9_RSky3Uu66Tk9llvz3BndbfomMjEcXYAHV4TyabfdIjXHJ5iOoA7rKy_LvBDEKrMMRXdyeG9-PoaqfEq8x1risvLL4IiRIIGmpNyq3Fsri4oP0j1Yoj25AQe-OtGfp8a7tqLkqFso2mvzEAPfN0SINvbSO4pmdyICSLpQOUhWYNj1dPhgtUsvjOb57-RjNYRZcnPOpUSUJrP0L7FnaxSXj1nj5mAIvxVj691YLUichJj4NMIorFyVX4GROcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی، می‌گوید از نظر حکومت ایران هر کشوری که با آمریکا در ایجاد محدودیت اقتصادی بیشتر علیه ایران مشارکت کند، «دشمن» تلقی می‌شود و تهدید کرد در چنین صورتی این کشورها هدف حمله قرار خواهند گرفت.
محسن رضایی در یک گفت‌وگو تلویزیونی که شامگاه شنبه ۳۱ مرداد از صداوسیما پخش شد، همچنین تهدید کرد اگر طرح جدید آمریکا علیه ایران برای ایجاد محدودیت اقتصادی بیشتر اعمال شود، جمهوری اسلامی اجازه نخواهد داد «یک قطره نفت نه تنها از تنگه هرمز که از کل خلیج فارس» خارج شود.
این اظهارات تازه‌ترین واکنش مقامات تهران به تحریم‌هایی است که دولت آمریکا قرار است روز دوشنبه آتی جزئیات آن را اعلام کند و اسکات بسنت، وزیر خزانه‌داری آمریکا، پیشاپیش آن را «سخت‌ترین تحریم‌های تاریخ» علیه ایران خوانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78005" target="_blank">📅 04:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hTtVOOyP1Y-H0W5gpRxH9FgnQarp-MPgF2bPUqFmu5s-JRs6yu-agqIokbcoO31Pi3oPIEsv8vhEfERRw2irVAl4Xwa8XCSpFjbJnFxKOaR9bCoft8jrieKTSmAxk3te1xI7YJSx2YM1PUh656nktjQGLFYZQvJ4d1p6y4JFN9AiMTeHuOuFDs5ZhpCs_PSXziB3F8nnKI01TZTsTwmNJuaLVLl6Pzy52uz72JXfCUm8S_5vZ0UkHjINGX8KY5otJzLqN2QRVRtNeDMvSBh4Hrn4FUeCvfVpAj7Dg0jH0lDvA3y6F8O_740cxUlyuEoq4Qx0vDyzTqYVy8H1vjqkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، با انتشار پستی در شبکه اجتماعی تروت‌سوشال بر عبور کشتی‌ها از تنگه هرمز با اسکورت نیروهای‌ آمریکایی تاکید کرد. ترامپ مطلبی از مارک تیسین، مفسر آمریکایی را بازنشر کرد که در آن، تیسین به آمار خروج بیش از ۱۰۰۰ کشتی از تنگه هرمز با اسکورت نیروهای آمریکایی اشاره دارد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، بار دیگر تصویری از نقشه تنگه هرمز را در تروت سوشال منتشر کرد که در بالای آن عبارت «قلمرو جدید آمریکا» دیده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78004" target="_blank">📅 02:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aU2ZG-0ju74xUvmghJ6AkC3EKkE37kBTnzcgCgH0G_iE_Siom2I7MiyK8eGpPy-A3XYvXhtD03ctWpZ8M1Vf2TGsRYl9JAbGojPEUu0DFV_JLk8mdoDLZGWW0HTNCj62NmueQFDM9un-TwhaY_WOXZYTuJ7d3NWQcG4ElNIWrS7uE0Rxu70AXwhb1beP6h4Q5r9Js-fBI8gSZ7LHrQ0qJHVcSvEB75NtOYisCHiCIo5UEoWKkxV5Y500gcKlkVRW9GuFHfaDjl_syIhybxGOfGs9oHQdnqwsRBIOKG4aECujdoQG76iADq_6nfq6xoemFu55dpGi5m9Iczak4R5q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار وبسایت اکسیوس، روز شنبه ۳۱ مرداد ۱۴۰۵ در شبکه ایکس به نقل از سه مقام آمریکایی گزارش داد که حدود ۴۰ نفتکش شامگاه جمعه از مسیر عمیق جنوبی تنگه هرمز وارد یا خارج شده‌اند و حدود ۱۶ میلیون بشکه نفت از این مسیر به خارج از تنگه منتقل شده است.
همزمان، رسانه‌های دولتی ایران مدعی شدند، تهران پس از درخواست‌های مکرر بغداد، به شماری از نفتکش‌های عراقی اجازه عبور از تنگه هرمز را داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78003" target="_blank">📅 18:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qu0W4V0rNPGjPdWVcOJUrYOVbBV-gm_1ogokE4RcbnPGtwU45m3hyPvUodiapvp7oLXb8-p_nEO0BAlhQtJuee02dhr4h8im9VIaMBENjTnF9ikcAKwxMW96v7tHuQLIDEfRaqmK0SjNRaGmkicilVzMh8xsHZ6cXviFoo4w-oI0rm8zmfGVZFkDNa8E6nzbqKLKLD4YQudGR__tLyNWGws382XfryFNWXFiZyAA3ez3cyiATPwRZq1x_fgoPwd3e3J2Es6haJ8WIzJbpQ4p2_89W0qmwMdP6fQEGKIfHGDFF1K8fCW1k61P6Zkdys4FJ1KAhsZJYtJIgUAJxc7BDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به پیمان جبلی، رییس سازمان صدا و سیما، ضمن حمایت از رویکرد این سازمان، نوشت که صدا و سیما در دوره جنگ اخیر، «در ثبت و ماندگار ساختن این حماسه، سهمی ارزشمند در تقویت جبهه رسانه‌ای انقلاب اسلامی بر عهده گرفت.»
وحیدی همچنین عملکرد صدا و سیما را «مجاهدت ارزشمند و نقش‌آفرینی موثر» توصیف کرد.
این در حالی است که در روزهای اخیر، محمدباقر قالیباف و مسعود پزشکیان صراحتا از عملکرد صدا و سیما انتقاد کرده بودند.
محمدباقر قالیباف ۲۷ مردادماه گفته بود که صدا و سیما در زمینه «جنگ شناختی» تاکنون موفقیت‌های لازم را نداشته است. رییس مجلس همچنین گفته بود: «تبیین ناکارآمدی‌های ساختاری، رویکردی و عملکردی صدا و سیما فرصتی مبسوط می‌طلبد.»
مسعود پزشکیان نیز در چند نوبت از عملکرد این سازمان انتقاد کرده است. پزشکیان ۱۰ خردادماه گفته بود روایت‌های صدا و سیما از شرایط کشور غیرواقعی است و این رسانه نیازمند بازنگری جدی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78002" target="_blank">📅 17:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WSogRWgrtULvi2F3HQt69hOhMQLttQKHrtre2HsWYkL4fOtmG3IQhlS--BkOcARMIhdmNnX8n4lRuhVLmVOXZHoupt3PQPDmD8vu26NF42h5NaTc7NQy7vIcCD7kOUggtdPZSe78-P69CqBJuYBwis_sitrsX0x_kaLUZB18GBWUa2-W-hFmNzvZp97zpPc31w3274hkLaDNC0AD-sbqvfgqlcp3c1Huj7ef76APP_Pu6EJ_A2NA57mB2hKI5buxeuPd3EQgTEYEhP6QFauGtD5m5k0RkdvOcrMn0QGWtQ-QrICFzJ_9okyOc-Vfyo4kqcAqzqCx9bwQJVB7__NZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رییس دولت در ایران، با تاکید بر ضرورت آنچه «اصلاح الگوی مصرف انرژی» خواند، گفت: «باید مردم را توجیه کنیم تا بدانند که اکنون بخشی از درآمدهای کشور صرف تامین بنزین می‌شود و این موضوع هزینه و فشارهایی را به بخش‌های دیگر تحمیل می‌کند.»
isna.ir
عارف شنبه ۳۱ مرداد در «همایش ملی صنعت، معدن و خدمات سبز» با اشاره به تفاوت مصرف سوخت میان گروه‌های درآمدی گفت میزان مصرف دهک دهم، ثروتمندترین دهک جامعه، حدود ۲۳ تا ۲۴ برابر دهک اول است.
عارف در ادامه، مخالفت با گران شدن بنزین را به واکنش اقشار کم‌درآمد به تغییر سیاست‌های مرتبط با مصرف انرژی مرتبط دانست و گفت: «وقتی قرار است اصلاحی در این زمینه انجام شود، اتفاقا بخش‌هایی از اقشار آسیب‌پذیر و کسانی که به هر حال در زندگی با مشکلاتی روبه‌رو هستند، تحریک می‌شوند که بگویند بنزین نباید گران شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78001" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FjEyRfu2xk_EHUzmDXLbyJ_v4VRFwCkNYNTc_5nCcTjtvoap0jSuVVYgAcHEj-FUE0wntPdZ0ir78QWl0cRNskG8c-qSjUgXX_kJbuZQgvBo3V3cu1qD1Pxior3CyTGfD09-jqhKHyV1k0tgXOVYP_Q2m11kitXF7aFebaYzbQUsApArbE4z8EXPeP10idHNFz1lFCPFq3E_0_d70P572KUpE6gp0scLDA90-goSdjqsy3r0Sl0xkfcSGu6rboZa9FrMyR4ppIcaOEbWINYNe_QjaASaKLLRB4DSpSpJewvV4_UzludIh1nL8CWJT4-vYnoRJ7ClQuyAGFv5v-6mhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، گفته است پس از اعتراض به کشتار معترضان در دی‌ماه ۱۴۰۴ تهدید شده و مسئولان مانع حضور او در مسابقات قهرمانی جهان شده‌اند.
فصیحی در
صفحه اینستاگرام
خود نوشت که در این مدت بارها به او هشدار داده‌اند: «مراقب رفتارت باش، می‌دانی که قهرمانی جهان و بازی‌های آسیایی در پیش است.»
او در ادامه نوشت: «همان شد. قهرمانی جهان را که بزرگ‌ترین رویا و آرزوی هر ورزشکاری است، از من گرفتند؛ بازی‌های آسیایی را هم خودم تقدیم‌تان می‌کنم.»
این دونده ایرانی گفته است تنها ورزشکار ایران بوده که سهمیه حضور در مسابقات جهانی را به دست آورده و فصل را در جایگاه نخست رده‌بندی آسیا به پایان رسانده، اما مسئولان از ثبت‌نام او در این رقابت‌ها خودداری کرده‌اند.
فصیحی درباره سکوت خود در ماه‌های گذشته نوشت: «صدها بار نوشتم و پاک کردم. هیچ جمله‌ای نمی‌توانست عمق ظلم، بی‌عدالتی و خیانتی را که در حق من شد، توصیف کند.»
او بدون اشاره به هویت افراد یا نهادهایی که تهدیدش کرده‌اند، گفته است پیگیری حقوق خود را از مسیرهای قانونی آغاز کرده و اجازه نخواهد داد حقش «به‌عنوان یک ورزشکار زن ایرانی» پایمال شود.
این ورزشکار در پایان نوشت: «من همچنان می‌دوم؛ برای مردمم، برای رویاهایم.» او همچنین ابراز امیدواری کرد که «عدالت جای ظلم، شایستگی جای رانت و پاکی جای فساد را بگیرد.»
فرزانه فصیحی پیش‌تر در بهمن‌ماه ۱۴۰۴ و پس از سرکوب اعتراضات سراسری دی‌ماه، با انتشار متنی در اینستاگرام از خشم و اندوه خود نسبت به کشته‌شدن معترضان نوشته بود.
فصیحی از چهره‌های مطرح دوومیدانی زنان ایران و دارنده رکورد دوی ۶۰ متر داخل سالن ایران است. او در بازی‌های المپیک توکیو و پاریس نیز حضور داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78000" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gTXzYcu36BNL3VdEPf6pw84vWti-x2Y6zpl5tonpsPj-9h_zYf_RnLBGr12Ptw6qDVRvIh619HkvHlSWlS05Cm5EFWo1pVWqpm9kd61NHdS_oCuk5eVWA5lak9ZWnSfGa_4NUIbm_hcMmA5XzSa22XTVmCQef5IIUcfMg-sLT2tot6EfZfG4OQ3aUCByM16xqJ_SwGM0J00iIhVVgQQ8WO1k8Fafa07Nv_PyR1n6SoMx1WTLfb2xL6kRKsQwQvmkSiAfdm6liYU7mXrGzIBMthRv1lP9nFW4p4WfZ1qXVUiNkap5gEW1eK6E4QmZiJFtvxPxFe9N5s57fPRlAKS1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف در شبکه اجتماعی «ایکس»، بدون نام بردن از کشوری نوشت: «پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی جدید و همکاری‌های اقتصادی در منطقه دریافت کرده‌ایم.»
او مدعی شد آمریکا با «قلدری» و نادیده گرفتن منافع متحدان خود به سود اسرائیل، امنیت آنها را به خطر انداخته است و افزود یک «نظم بومی و مستقل» می‌تواند صلح و امنیت واقعی را برای منطقه به همراه بیاورد. رسانه‌های حکومتی ایران این اظهارات را واکنشی به تهدیدهای دولت دونالد ترامپ علیه کشورهایی دانسته‌اند که به همکاری اقتصادی با تهران ادامه می‌دهند.
اظهارات قالیباف در شرایطی مطرح می‌شود که روابط جمهوری اسلامی با برخی کشورهای عربی خلیج فارس در روزهای اخیر با تنش‌های تازه‌ای روبه‌رو شده است.
علی عبداللهی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، روز چهارشنبه به کشورهای حاشیه جنوبی خلیج فارس درباره «هرگونه کمک یا تسهیل» برای نیروهای آمریکایی هشدار داده بود.
عبداللهی گفت جمهوری اسلامی فعالیت هواپیماهای نظامی آمریکا، از جمله هواپیماهای سوخت‌رسان مستقر در پایگاه‌های منطقه را زیر نظر دارد و هرگونه کمک به ارتش آمریکا را به منزله مشارکت در عملیات نظامی این کشور تلقی خواهد کرد. او خطاب به کشورهای منطقه گفت: «هیچ‌چیز از دید ما پنهان نیست.» کشورهای عربی منطقه پیش‌تر مشارکت در حملات آمریکا به ایران یا اجازه استفاده از خاک خود برای این حملات را رد کرده‌اند.
همزمان، امارات متحده عربی تمام فعالیت‌ها و مبادلات تجاری و تراکنش‌های مالی خود با ایران را تا اطلاع ثانوی متوقف کرده است؛ اقدامی که برای جمهوری اسلامی، با توجه به نقش امارات به‌عنوان یکی از مهم‌ترین شرکای تجاری ایران، اهمیت ویژه‌ای دارد.
این تصمیم پس از آن اعلام شد که مقام‌های اماراتی گفتند دو موشک بالستیک شلیک‌شده از ایران را شناسایی کرده‌اند. بر اساس اعلام ابوظبی، یکی از موشک‌ها خارج از آب‌های سرزمینی امارات و دیگری در داخل این محدوده به دریا سقوط کرده است. تهران این اتهام را رد کرده است.
ادعای قالیباف درباره درخواست کشورهای همسایه برای ایجاد ترتیبات امنیتی تازه در حالی مطرح شده که او نام این کشورها، محتوای پیام‌های ادعایی یا جزییات طرح مورد نظر تهران برای «نظم بومی و مستقل» را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77999" target="_blank">📅 17:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edOMosoCs8nKgmqqt3q6QoJoJ2A0rSS4lVbFt1wDZsCvYw46qprX3rWkCVYzk0j4LBAAKQcbUAOMDHTpgi2OMy0fi2u0CjhZ5kkCmRWzqQafvnJ_m-shLPOdHtan-6hlUmG-snN3mqQOMT8475sJXmE-heBHQjbZoDs7ebeocY2cHPnps5-RDaZrfqMpol6KpPUgt2KB5Ez4nNj-pkjdUqac24iukCQCr6mDOEbikp7tWxnViuBoiFnG_87Ik6ZiUg8M2vU2Cb5PiDrrDCHvC5CX9WynJOuxUn5D_qYk4hBltu7yX5VN6-VSsc-c6BH_6G3iYAaKwqkq4jd6J9zcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آرزو کشور» مالک و مدیر یک سالن زیبایی در اصفهان به اتهام «ارتباط با دول متخاصم» به ۱۲سال حبس محکوم شده است.
آرزو کشور از بهمن‌ماه سال گذشته، در زندان «دولت‌آباد» اصفهان نگهداری می‌شود.
آرزو کشور پس از بازداشت در بهمن‌ماه گذشته، در سلول انفرادی نگهداری شده و تحت بازجویی‌های طولانی قرار داشته است. مواردی که به‌تنهایی مصادیق «شکنجه» محسوب می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77998" target="_blank">📅 17:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R1M2fh3FTN9o-Ngs9vGN95M9mZmbul_pRIlngaPd8vuIMJutNH-oP5sYTL98TliIT7etyEz4ZgTz-kIKJD9FCWYoUxlYL09KS_OTj55HVOhPTpN1E9GHiUrL9Vbis4Ueh9vAyLneLszb5ULH1cmC-E9qTQhWSyqzGqaw4ElkLoCXHSNBfWKQXqNQsGM7Pzy0cMR4j3yFXWMzHyOV2Rhc7Lo9ahl40eMzDkwilz7CbDE69qO-Rf59dKm3OkFmgKu3Mg1lzthmN4HTItEat3d1qxqrR5l8YgLcsDu6lhKNokz8WjGRft6TWDGasY681LI20rE1LCraZitCyx9UTYIOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jvU0EHGsCYQbwhElq8ZG9NTT3tMVRJU0eLQMxHhN4HpaZe45koewctDZ4WaBJkYK1P5xPyMfom9ums3im9kEUeQg6sYv3wmVR-Q2lTRDzQtX-hY05Srb2Tvb4DFgJHyICpH1ZJiVD7Inc98kT2qUvw8eKXEPT4BF3AukxPTUcyozr214PkM9CxMpJ0XWhev0XQQhZOfDoWz9w6K8gw3YXzgAU7fD9cbFip8i480wckx0d811z0CbWXiOw2Hlvx399FTtb7FzciusGNl9mOsH1FB_J5BZkQsbhrZ7cZea6NFOVilr-KK7DEaQwm9KXp7PRhyvsXzfhxkSYbKHP8_xXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rLw8IQjVq2beh7cV7_HnL7LEaBfmFMIgi-a8R0l3WedzTQTIuKRWbZBR7gkRXx1h86dVz6YTvf-WxQYtr1pN9BHG9C6sgD9XJptmmSd_hFmTX44fnmxAv-bglxWhGhzOfkd3vEocHeB18ca2-Bhq1YjgO4IpQU3NCQTRZC6LzC074nUfv943dJSfrP-7lyNus8fHWmckjNMCVwdAa8NSYG2XG079EEcKWyVhJUTjcYO-KeTa0-4tctMe2EEDBFEsJsCa_CSepv4IkHfaoENkEP-eaT-KrXFm_sQHUXyGoiKvr0ydcPX9uJrriDdRj08yfVZogxc42-GIaZx7enK0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D9RGLPXJhZrG0yNSJAcBVB1ufHzz5ed4gru5R6AvXRFRSi6l74-sWMPoAcQNnAmBC7YfSlTPS-lC5b9qB1Gk2c62F18o6ruHnSBLHSQUiQB8Tw2r5Zv-eF_AvYLkpQvJPq5Ub9y4x3MOCSxUihknJ820lvQPduJK8udfJC1p73ESZAWP6g3yYo44mDriZ-DzSwySNpGfZ1_dJo2EBxNUXHlZexkEZPIZ9tEDMHwO3uUM_JsFIoiAi_2P0mgywbc-Yi-kjKQ1st0szbz_9Ifxs3L42SHkxXkiyiylEkmXFZO0xeQODmdcr2SOVqSvk9TZDIsFCuGubZ0LisoiNqiKUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=uoL_jHmUS4amN6aWvyfffg-DlQ11YHfdr0kj2C7QPjXWgisOy0v7zbI_FmsJCM8HwqYa_04D7bduC2XfoHWfqoAN4kBsDGzRJO0OxHpibqdFpWYOwCQ3vcgzd3UrpUwwQwOrPYulbVMgPTf_SBnIF5yVEt6j6fgZnLlM9Anro_F9H-OIjAiogmyT0028r7jdlLy2WsTe7H-co3tJpHo2zWzhvu8SbiCrY3x-ePRsyf0E-NLDhxAofyn_q8vUT8WQk1bMhXyeR_vtQ6JrlMwA486YRYKq5u2HSk6FM4ERuGteQwz5vPQlOywcC7Kpfjt2VNAW6AOGM_CBv126stYVFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=uoL_jHmUS4amN6aWvyfffg-DlQ11YHfdr0kj2C7QPjXWgisOy0v7zbI_FmsJCM8HwqYa_04D7bduC2XfoHWfqoAN4kBsDGzRJO0OxHpibqdFpWYOwCQ3vcgzd3UrpUwwQwOrPYulbVMgPTf_SBnIF5yVEt6j6fgZnLlM9Anro_F9H-OIjAiogmyT0028r7jdlLy2WsTe7H-co3tJpHo2zWzhvu8SbiCrY3x-ePRsyf0E-NLDhxAofyn_q8vUT8WQk1bMhXyeR_vtQ6JrlMwA486YRYKq5u2HSk6FM4ERuGteQwz5vPQlOywcC7Kpfjt2VNAW6AOGM_CBv126stYVFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مرتبط با ایران در سخنرانی دونالد ترامپ در ایالت کارولینای جنوبی، جایی که رقابت‌ها برای کرسی سنای آمریکا در جریان است، با تشخیص و ترجمه ماشین:
🔻
و به‌محض اینکه کارمان با جمهوری اسلامی ایران تمام شود، قیمت نفت پایین‌تر از چیزی خواهد بود که حتی همین مدت کوتاه پیش بود.
🔻
اما با وجود همه این خبرهای خوب، گفتم از گفتن این خوشم نمی‌آید، اما باید کمی مسیرمان را عوض کنیم و برویم سراغ جمهوری اسلامی ایران و باید ماجرای سلاح هسته‌ای را جمع کنیم، چون آن‌ها دارند به سلاح هسته‌ای می‌رسند و ما نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند.
نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد؛ خب، چیزهای بسیار بدی خواهید دید. پس رفتیم آنجا و جلویشان را گرفتیم. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
آن‌ها به‌شدت می‌خواهند توافق کنند. ما حتی نمی‌دانیم خودمان می‌خواهیم یا نه، چون من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم. این قلمرو آمریکاست.
🔻
در مورد ایران هم به همان اندازه [ونزوئلا] خوب عمل می‌کنیم. رسانه‌های جعلی فقط نمی‌خواهند آن را این‌طور گزارش کنند، اما حالا دارند کم‌کم می‌پذیرند، چون چیز زیادی برای گفتن ندارند.
وقتی کشوری دیگر نیروی دریایی، نیروی هوایی، رادار، تجهیزات فنی یا تولید ندارد، رهبرانش هم دیگر نیستند. دسته دوم رهبرانش هم دیگر نیستند.
بخش‌هایی از دسته سوم رهبرانش هم دیگر نیستند. در واقع، این یکی از بزرگ‌ترین مشکلات من است. نمی‌دانم اصلاً باید با چه کسی طرف شوم. این یک مشکل است.
تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.  می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور شوم.» پس کمی مشکل است.
🔻
او [لیندزی گراهام]  واقعاً دغدغه‌اش این بود که کشورهای خارجی به کشور ما آسیب نزنند. دغدغه‌اش این بود که ایران سلاح هسته‌ای نداشته باشد. خیلی شدید روی این موضوع حساس بود. ببینید، اگر چنین اتفاقی می‌افتاد، اگر آن‌ها به آن دست پیدا می‌کردند، از آن استفاده می‌کردند. اسرائیل را فوراً نابود می‌کردند. خاورمیانه را نابود می‌کردند. و فکر نمی‌کنید سراغ اینجا هم می‌آمدند؟ می‌گفتید: «شهر بعدی کدام است؟» ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما قبلاً... آن بمب‌افکن‌های B-2 را داشتیم؛ یک سال پیش، آن‌ها به آن امید پایان دادند.
🔻
ببینید، جمعه‌شب است. وقت زیاد داریم، درست است؟ اصلاً چه کار دیگری دارم بکنم؟ برگردم، ایران را یک کم بیشتر بمباران کنم؟ دیگه چه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77993" target="_blank">📅 05:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77992">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=j86x5YDm9bxSupvaxmN7Y6IbVYXhpbClHVGFX1BvO0GBtOGxRYXfhimfhsNbEH1HWHek5-FALGuwi21dRuubNcqU4jewYiDC4eJpTKvH_9ni2cGvwLYwOz1fOFnXelQGxeJ2CVROxZ6YrzEiFQNZG59nOfXneJMP7bXhdYykd5dOc7Z27uUbjMUWLOnrGhyfPVHECHOR0SpCe6AIHO_ncLaX4dqH-85EwnkfpJYb9A6hgtydu79uzDESjExm6_09uulxopRJK90vd21Arm5DZjBzlt16bzITqS1alMI1RLKbAgUmUGfgAQ-RY7_Wn5S0p-AYJfUiTo6M9c0YNnsEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=j86x5YDm9bxSupvaxmN7Y6IbVYXhpbClHVGFX1BvO0GBtOGxRYXfhimfhsNbEH1HWHek5-FALGuwi21dRuubNcqU4jewYiDC4eJpTKvH_9ni2cGvwLYwOz1fOFnXelQGxeJ2CVROxZ6YrzEiFQNZG59nOfXneJMP7bXhdYykd5dOc7Z27uUbjMUWLOnrGhyfPVHECHOR0SpCe6AIHO_ncLaX4dqH-85EwnkfpJYb9A6hgtydu79uzDESjExm6_09uulxopRJK90vd21Arm5DZjBzlt16bzITqS1alMI1RLKbAgUmUGfgAQ-RY7_Wn5S0p-AYJfUiTo6M9c0YNnsEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: آیا حرکت به سمت جنگ اقتصادی علیه ایران نشان می‌دهد که گزینه‌های نظامی آمریکا در منطقه محدود است؟
🔻
ترامپ: نه، اصلاً. فقط یعنی اینکه داریم می‌بینیم چه اتفاقی می‌افتد. آن‌ها هیچ پولی ندارند. نیروی دریایی ندارند. نیروی هوایی ندارند. به سربازانشان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند. تورمشان ۳۵۰ درصد است. بنابراین فقط می‌خواهیم تا حدی ببینیم چه اتفاقی می‌افتد.
و همان‌طور که می‌دانید، کنترل کامل داریم. اگر به محاصره نگاه کنید، کنترل کامل آن را در اختیار داریم. تمام آن منطقه‌ای که مربوط به تنگه هرمز است، و این یعنی تا عمق آن، مناطق خشکی را هم.
پس آن‌ها خیلی دوست دارند توافق کنند، اما از نظر من هنوز آماده نیستند که توافق درست را انجام دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77992" target="_blank">📅 01:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بنا بر پیام‌های دریافتی حوالی یوسف‌آباد و امیرآباد و فاطمی و... صدای شلیک پدافند شنیده شده.
ساعت ۲۳:۰۸
🔄
پیام‌ها همچنان ادامه دارند.
کسانی هم معتقدند تیراندازیه ولی خیلی‌ها هم پیام دادند که صدای آتش‌بازی و ترقه‌بازی این وقت شب در کشور جنگ‌زده مربوط به یک مناسبت تازه‌ساز و "عید" جدیده!
دو روز پیش:
اجتماع "عید بیعت با امام زمان(عج) " برگزار می‌شود
به گزارش ایسنا، این مراسم با هدف تجدید پیمان با امام زمان(عج) و همچنین تجدید بیعت با مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای، از ساعت ۲۰:۳۰ تا ۲۳:۰۰ در میدان ولیعصر(عج) تهران برگزار می‌شود.
در این اجتماع علی‌اکبر رائفی‌پور و شیخ اسماعیل رمضانی به ایراد سخنرانی خواهند پرداخت. "
isna
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77991" target="_blank">📅 23:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sZfrAiQRiWOnzVePLeagoc4eo-7gWYHcAx0TBtECJWSjkP_j9zqhgRQx07MDSCLc-_T9xIi44hSA4LQS921XnXdI077gxgZ6pYwxZr8DWTlKt6yDQ82_tsody5M-BoaalqPHdl0s3YtxSGq-UAV1_geV7UKtQNvi1uk-eHdS9bs9bG_XX06iL3Hq5rxGhniP6khmF2ZoKMRBvAZ8hKZnGMOk3VyEsOJAU2381107mVn3w1zEprJ6PZb6VNoXV1Reia7Fx5Q5sLWFlFVPpJS72dNuKV97KC0kaFIV0GqdUKMpvATriJWGaw9GfueI2G6j7l4KbktCZZdDKZhgPezIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر عکس من در آوتار اینجا جزو تبلیغ بود کلاهبرداری خطرناک‌تریه.
این تبلیغات به خود تلگرام سفارش داده میشن و کانال‌ها امکان جلوگیری از نمایش اون‌ها رو ندارند.
هر روز صدها نفر برای اولین بار با این تبلیغات مواجه میشن و به درستی احساس مسئولیت می‌کنند که باید این چیز خطرناک رو اطلاع بدن.
هر روز خیلی‌ها هم لطف می‌کنند و راهکارهای مختلفی مثل درخواست برای ریپورت کردن تبلیغات و بوست کردن کانال و حتی سفارش تبلیغ برای خودم و... رو پیشنهاد می‌کنند.
یک مشکل بزرگ الان حجم پیام‌هاییه که درباره این موضوع دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77989" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qJeVqDqAYxWKndOZ6jSdjvUaVypiarwLK-NuAcaBsjAlL6qyyicZ3In7RUWw6_XPqRciTE7pTS5VZwPCuaXpeOGGQRtadYwxxqfHzr2nuCyyTlldGf4w-dbT3F_gj4yyolQuglGAzFbLNTihBs0OI3jx-E7iSuS6LVG5fQGUDe-KreJqEROhkDsSdyrOmbFSXsJyuIK27J9qvcZZ4SMK5NP4Tde-S2qBcT0spcE9AES3G4b_5EGqjd2Amdnm5Etzbb-ubfkMOE_gkW35sOWPArckvKCdnUNV55IR3jNjzAkgGAlSp0gJ9bX8I_kakcH4DJq5JGZZ_4tG_wLTbvsD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هرانا» روز جمعه ۳۰مرداد۱۴۰۵ خبر داد که دیوان عالی کشور، حکم اعدام «ارغوان فلاحی»، زندانی سیاسی ۲۴ساله محبوس در زندان اوین، را تایید کرده است.
حکم اعدام برای این زن جوان در شعبه ۱۵دادگاه انقلاب تهران به ریاست «ابوالقاسم صلواتی» در تیرماه ال جاری صادر شد.
ارغوان فلاحی که اوایل بهمن۱۴۰۳ به دست نیروهای امنیتی بازداشت و به بند ۲۰۹ زندان اوین منتقل شده به «بغی» متهم است.
هرانا به نقل از یک منبع مطلع نوشته است که ارغوان فلاحی مدتی در بندهای ۲۰۹ و ۲۴۱ زندان اوین نگهداری شد و برای گرفتن اعتراف اجباری از او درباره کشته شدن «محمد مقیسه» و «علی رازینی»، دو قاضی جمهوری اسلامی، تحت فشار قرار گرفت.
فلاحی پیش‌تر نیز در آبان ۱۴۰۱بازداشت و به اتهام‌های «اجتماع و تبانی» و «تبلیغ علیه نظام» به دو سال زندان محکوم شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77988" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C7hQ3A6e7qiY_wax64NgeaxqmUb6mgP26iL-8kGwUCweLV0VebS8Da_A3ZG_orP6N3g4enJ9WVmBrwdsKeSilvtKgRX5Uu6autLbEZN4yeoJxuFqY6leOJBPcgXJvo8mDyXN8iIInL-9RgqOFwdq4BCxX6p1yQiqqtGhd_ZVuoOIFi40vKYHKLWBgePQVoeZIJQ0DN02p6jxTbSZYRr_Y7aXYAH9CSTSOrsiXmSXjSXMcAZ0hnoM-HVtG4gvRv1LCAkmuyVQQNvIH7NT0f2e0FNSfTZWLKsKUOjX3Gz6ji4PLKgM9cKATVmtVc7EE_HubceFqBSScEXw5d5x04G88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
امروز: «کوبنده‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
این فیلم را قبلاً دیده‌ایم. همان مزخرفات. قلدرها عوض شده‌اند.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77987" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=MKaQzXPMzfGxr5x4PekYGFfCIhcKcdsD3mTVjtL9Yw9l-ZF9avMzeceX2k0F3OzVNhJs_0-h3Xow7URWt-K1czsZzOehk33VCu8PvK3TVEBFGwwJNKaoPSI6bLA4eZHGd5L4Qf4xL44LSydgtt2ByQ4PkBZgo7GDyoao6EvF3CZaGeKq2q5Mio_xRTFwLRvG0uSG0PJp2YdlsN_QZF2EbBQJj2-2Z6H89vWLQ5rVgVpm8Q4GAnCXqLr2fjbD2LFsygqiYngsHECdcCoiru0WvwUAxFrMhVZnVKrgdwCKxO66WgnRtArXlMxrfZOrP9E-kiR56B058eUDtN-bWzgJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=MKaQzXPMzfGxr5x4PekYGFfCIhcKcdsD3mTVjtL9Yw9l-ZF9avMzeceX2k0F3OzVNhJs_0-h3Xow7URWt-K1czsZzOehk33VCu8PvK3TVEBFGwwJNKaoPSI6bLA4eZHGd5L4Qf4xL44LSydgtt2ByQ4PkBZgo7GDyoao6EvF3CZaGeKq2q5Mio_xRTFwLRvG0uSG0PJp2YdlsN_QZF2EbBQJj2-2Z6H89vWLQ5rVgVpm8Q4GAnCXqLr2fjbD2LFsygqiYngsHECdcCoiru0WvwUAxFrMhVZnVKrgdwCKxO66WgnRtArXlMxrfZOrP9E-kiR56B058eUDtN-bWzgJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمیدرضا حاجی‌بابایی، نایب‌رئیس دوم مجلس، روز پنجشنبه ۲۹ مردادماه در گفت‌وگو با خبرگزاری فارس با اشاره به تحولات مرتبط با تنگه هرمز و تلاش برخی کشورها برای ایجاد مسیرهای جایگزین انتقال نفت، گفت: «کسی که امروز خط لوله می‌کشد تا تنگه هرمز را تضعیف کند، در واقع به ما موشک می‌زند. نباید اجازه دهیم خطوط لوله جدید ایجاد شود.»
او با تاکید بر اینکه احداث این مسیرها در راستای منافع ایالات متحده است، افزود: «هر کشوری که در زمینه فناوری یا اطلاعات به آمریکا کمک کند، عملا وارد جنگ با ما شده است. احداث خطوط لوله‌ای نظیر فجیره و ینبع برای کاستن از اهمیت راهبردی تنگه هرمز، مصداق بارز جنگ و حمله موشکی علیه کشور است و پاسخ ما باید ممانعت از ایجاد چنین خطوطی باشد.»
این اظهارات در حالی مطرح می‌شود که شبه‌نظامیان حوثی یمن، وابسته به جمهوری اسلامی، در هفته‌های اخیر با حمله به کشتی‌های حاضر تنگه باب‌المندب تلاش کرده‌اند صادرات انرژی از این آبراه را مختل کنند.
از سوی دیگر، مرکز مشترک اطلاعات دریایی (JMIC)نیز، روز پنجشنبه، از عریض‌تر شدن گذرگاه جنوبی تنگه هرمز خبر داده و اعلام کرده بود این تغییر امکان تردد هم‌زمان کشتی‌های ورودی و خروجی را فراهم می‌کند.
مدیرعامل آرامکو نیز روز ۱۳ مرداد ماه، اعلام کرده بود این غول نفتی با تکیه بر خط لوله شرق به غرب عربستان سعودی، کانال سوئر و تنگه باب‌المندب، به صادرات نفت خود ادامه می‌دهد.
@
VahidOOnLine
مصطفی خوش‌چشم، کارشناس صداوسیما در مصاحبه‌ای پیشنهاد داد، «نیروهای محور مقاومت» با استفاده از «مین‌های دریایی هوشمند» خلیج فلوریدا را مین‌گذاری کنند.
خوش چشم، در تیرماه گذشته در تلویزیون به شدت از عباس عراقچی، وزیر امور خارجه، انتقاد کرده و تحلیل‌های او را به «رانندگان تاکسی» تشبیه کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/77985" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h9Z29SDF0kufetN_7oarBvEmbP8zg_KYI2gkGrB2ovcy0A_gc8TfTRU2Bgh7MLr9cZoFdMe7hz-Io6S2xZhHRgJb7ba4ij88z0-tvwb0WBv3XwYfjxYNNWtuZkQz-GOaA1BOvBmxunNzCCqrDKkFE9LM2yTW73rnLIa9H9cCIy6hIcZMFnAYyB7qNmLLAV9PRb2s2JFoDjzAIHE4icF7ZrhLTr7FrGQp1jYCPv4QmKnfVak1chrymPHJd8VVVtpxRfK5nlR6H7BQrhsVYNWhoNaDdChjcdSs6RrmjxVnzzKa2O491tcs6Y4uY1-eqPkIC7k5oudMUSJ2fjd4bs8wKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nocMsMhocbevoadp4cAz7Is1OfPT2fXDaVnka_jRaw0ailfjDlHvzQBfkw6MT7rcmLSJlEjdSI_IR2eIqkA8NG7XDmNzWhfsw4xuzYE5TFcu3k15ZOwF3ok0dA_1CdAjnJL4Ok_OT8cgS2n7rIae9y_BwARylBl0jVCFldF_M-7QR-sibQ354zCTRfim7Lk22miM3sjucMM--Jbsc7sPsxOUWnuQEshxj52XMk-1Y6yY-9vgH5Cwgq94ZM1c5BUTnmb1ehWjLtuZZWxe7A9aC22B9UaHyNDOBAPKwxbXW6lPYte_UprFvTTQZFaOax8xsnLpjYCeho-b5lAhI42zxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس پازوکی، معاون ارتباطات و اطلاع‌رسانی دفتر محمدرضا عارف، معاون اول مسعود پزشکیان، اظهارات منتشرشده عارف درباره تعیین نرخ ۸۷ هزار تومانی در دولت را تکذیب کرد. این در حالی است که رسانه‌های ایران پیش‌تر اظهاراتی از عارف درباره تعیین این نرخ منتشر کرده بودند.
به گزارش رسانه‌های ایران، عارف دوشنبه ۲۶ مرداد در جمع خبرنگاران گفته بود پس از تعیین نرخ چهارم بنزین با بررسی کارشناسی و تعامل با نهادهای امنیتی و سایر قوا، قرار بود این طرح به‌صورت آزمایشی در کرمان اجرا شود، اما بدون هماهنگی با دولت متوقف شد. نرخ چهارم مورد اشاره ۸۷ هزار و ۲۰۰ تومان است.
با این حال، پازوکی در ایکس مطالب منتشرشده درباره اظهارات عارف را «ادعای ساختگی برخی کانال‌های غیررسمی» خواند و گفت: «معاون اول رییس‌جمهور هیچ‌گونه موضع‌گیری یا گمانه‌زنی عددی درباره نرخ‌های جدید بنزین نداشته‌اند.»
او افزود: «موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت، روز جمعه ۳۰ مرداد ماه اعلام کرد مطالب منتشرشده به نقل از محمدرضا عارف، معاون پزشکیان درباره تعیین قیمت ۸۰ هزار تومانی برای بنزین صحت ندارد.
مهاجرانی گفت چنین عددی نه از سوی معاون اول رئیس‌جمهوری مطرح شده و نه مبنای تصمیم‌گیری دولت قرار گرفته است.
او تاکید کرد در صورت نهایی شدن نحوه «مدیریت مصرف سوخت»، جزئیات از مسیرهای رسمی و مستقیم به اطلاع مردم خواهد رسید.
@
VahidOOnLine
مسعود پزشکیان، در مجمع عمومی «انجمن اسلامی جامعه پزشکی ایران»، گفت: «جدا از بحث محدودیت‌های مالی و محاصره دریایی دشمن که کار صادرات و واردات ما را با مشکل مواجه کرده است، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/77983" target="_blank">📅 18:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IkPL__uzNYiAj-woxi_rF4Bt1ggSKjKHjDpu9swQSq2iTUMuAO7jnEeCnSFfbZATuFNt93L2KvjC7F-9qgz_uHHDkCjLueNSOTZfNcsRSWsYhhcQDNrnGYuMO5w19TTY97iBbyz89KPy32vIB0fBvj7H71SNhy3Zg3MroVhJARsd1jhRXBaYoL9ELKBuZBa712XsTpVtc9wO-SFKF8ozp1jGBLPeK8UYWaOW9a38OvueyzyKwATwlchMJ4lOuMg1Rqc-pFrTnnLVfN1hgioEM3C3fAgfwDAiu54NLJD0I_xo7d-frghX76EA8lGcWjNjOMO2zFw0Ogt22P8zkxo28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس دولت در ایران، می‌گوید اکنون زمان آن است که به جنگ با آمریکا پایان داده شود چرا که تهران در مقابل واشنگتن در موضع «قدرت» قرار دارد.
آقای پزشکیان گفت: «بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و تأکید می‌کنند که آمریکا برخلاف تمام مقررات، به مدارس، بیمارستان‌ها و زیرساخت‌های ما حمله کرده و در دنیا منفور است، جنگ را پایان دهیم.»
رئیس دولت در ایران همچنین نتیجه مذاکرات ایران و آمریکا را که به امضای تفاهم‌نامه اسلام‌آباد منجر شد، «دستاوردی بزرگ» توصیف کرد که «با وحدت و همدلی در شورای عالی امنیت ملی به تصویب رسید و همه کسانی که در این شورا هستند و دستی در آتش داشتند، با قاطعیت از آن دفاع کردند.»
آقای پزشکیان در ادامه از کسانی انتقاد کرد که «خارج از گود نشسته‌اند» و «نمی‌دانند دولت در چه شرایطی است، مجلس در چه شرایطی است و فرماندهان در چه شرایطی هستند، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند.»
مسعود پزشکیان در عین حال تاکید کرد که اظهاراتش به معنای تسلیم شدن در برابر تعرض احتمالی نیست: «ما به هیچ عنوان در برابر قلدری سر خم نخواهیم کرد و هیچ تردیدی در آن وجود ندارد. تا آخرین نفس مقابل آنها خواهیم ایستاد و پاسخ کوبنده به آنها خواهیم داد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/77982" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=RvQAeCtyTOhOT9Q8PQLgTMNSZdlxPq5ZgSWWmDS_AOT2w-t-AJuGPeorz8HNGMXK1EaMu7UbyLMHeOgwziqaDfuYrK5DwvTTsSHYSGXDlLCRZqfdjO6sXss98Ibp282lfjv9SutYRWODOcZEHA2aoY7fIHF5LcRTuGbtkdXUxjySBIqivu6AK7r8I9ye5dLAgEavfsrc24KRgJEjCPrGq9nVvnc1bGhfzQqLuL7LjralzcKP3xRiCfXdQzsLPbTGe6ETgfVtZgjpOWnZ1qYZWPmryStCnhpJL4molr-dG2fdhRMoBJAZqoMqwDtkkt2SMXuWmbfyVMyjlC_nyQwf9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=RvQAeCtyTOhOT9Q8PQLgTMNSZdlxPq5ZgSWWmDS_AOT2w-t-AJuGPeorz8HNGMXK1EaMu7UbyLMHeOgwziqaDfuYrK5DwvTTsSHYSGXDlLCRZqfdjO6sXss98Ibp282lfjv9SutYRWODOcZEHA2aoY7fIHF5LcRTuGbtkdXUxjySBIqivu6AK7r8I9ye5dLAgEavfsrc24KRgJEjCPrGq9nVvnc1bGhfzQqLuL7LjralzcKP3xRiCfXdQzsLPbTGe6ETgfVtZgjpOWnZ1qYZWPmryStCnhpJL4molr-dG2fdhRMoBJAZqoMqwDtkkt2SMXuWmbfyVMyjlC_nyQwf9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل، گفت جمهوری اسلامی بیش از ۴۷ سال است که شعار مرگ علیه آمریکا و اسرائیل سر می‌دهد و تاکید کرد که این تهدیدها را نباید صرفا حرف یا شعارهای توخالی تلقی کرد.
هاکبی روز پنجشنبه ۲۹ مردادماه در گفتگو با شبکه ملی اسرائیل (آروتز شیوا) گفت: «۴۷ سال و نیم است که می‌گویند ما را خواهند کشت، اسرائیل را خواهند کشت.» او افزود: «این‌ها صرفا تهدیدهای توخالی و شمشیر تکان دادن در هوا نیست. این‌ها کسانی هستند که واقعا می‌خواهند ما را بکشند.»
سفیر آمریکا در اسرائیل گفت آمریکایی‌ها باید این تهدیدها را جدی بگیرند و برای اثبات سخنانش به حمایت مالی و تسلیحاتی جمهوری اسلامی از حزب‌الله، حماس و حوثی‌ها اشاره کرد.
هاکبی افزود جمهوری اسلامی علاوه بر صرف منابع برای تسلیحات خود، حزب‌الله، حماس و حوثی‌ها را نیز تامین مالی و تجهیز کرده است. او در ادامه گفت: «اگر در جهان اقدامات تروریستی در جریان باشد، معمولا می‌توان رد آن را تا تهران دنبال کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/77981" target="_blank">📅 17:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZVmzqludYdJBRulnZ6OE4razCRnCgJomgJbeqfkPSG6ZTKKOpHvewFs7wetGf1AMy2tuU3LbB-Tu1HcYbaDdP3Ih4dAY7iSLwxr_5zhQh5aB8rI-a1cNMifzqs6Mqi9Xu8xFYYO-TFbfOSiuu3qwO0MpxC8-M11MLvOY6Kj6zwQQActCcTbAUQFL5Djt3S3aJopFXAQTR0MF7EWyoUJ1d8Sz1kY8QF70vO5Ux5q6371WDkoBNdgCAcR_N7bKRZbCcxa3-YIH4vTkLGptuydzZU2-VOSLK6k9C7ipSrqsZpgSjUmTZ3-0AENWamZFPOJX7TS9xvkuwvMAYuv-haTbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس شورای اسلامی با هشدار تلویحی نسبت به شرایط اقتصادی جامعه ایران گفت: «ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید ملی نداشته باشیم، دوام نمی‌آوریم».
محمدباقر قالیباف روز جمعه ۳۰ مرداد در اظهاراتی در عراق برای افرادی که «فعالان اقتصادی ایران و عراق» معرفی شده‌اند، با «ظالمانه» خواندن تصمیمات جدید دولت آمریکا برای اعمال تحریم‌های اقتصادی شدید علیه ایران گفت: «باید برای غلبه بر آن‌ها برنامه‌ریزی کنیم تا بتوانیم بر آن‌ها فائق آییم».
قالیباف که رئیس گروه مذاکره‌کننده ایران با آمریکا پس از جنگ اخیر بود، در اظهارات خود خواستار استفاده از پول ملی ایران وعراق در مبادلات تجاری بین دو کشور شد و گفت: «می‌شود به دهان ارز آمریکایی زد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/77980" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qojyUzLgEI_cnxKjxwRzhKDdTaEu0YSjnb6Fs37xIfmR19CzlWTNdcXehLeGHPRECu9rk8hIuj1ictbp7HSjT7R0c5ymHYF-_XWzouGtDTSYrxzhrEk0jCAy98F-OhSx34LdvkycxffObjPKX12QOmZD63Vk137zBwiGd4wMCE8eujGPYv9x7ybQCenjx1zU78pvBnVdLnl2io9__Hz5PpyV-jGNemU5ZCBy8cpoKnLFwJKAetTCdECOlzheMmnnckyzXYPvmbiorOFIXVCuoj3lluMu57IazzTPPJDwj9ZnaiF88Rc-GogudjrJvigApUIE7aI-rgfF2GCzbcYFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه لبنان می‌گوید روابط عادی با نمایندگی ایران در لبنان تنها زمانی می‌تواند از سر گرفته شود که تهران مطابق با رویه‌های دیپلماتیک تعیین‌شده، از تصمیم دولت این کشور پیروی کند.
یوسف رجی در گفت‌وگو با روزنامه «النهار» با پافشاری بر تصمیم قبلی‌اش در «عنصر نامطلوب» خواندن سفیر جمهوری اسلامی در لبنان و اخراج او گفت: «ادامه حضور سفیر ایران نقض یک تصمیم حاکمیتی است. این تصمیم باید رعایت شود و هیچ تفسیر، استثنا یا مصالحه‌ای را نمی‌پذیرد».
دولت لبنان چهارم فروردین امسال با رد استوارنامه محمدرضا رئوف شیبانی، سفیر ایران در لبنان، او را «عنصر نامطلوب» خواند و چند روز فرصت داد تا خاک این کشور را ترک کند.
با این حال، وزارت خارجه ایران این تصمیم را نپذیرفت و سخنگوی این وزارتخانه اعلام کرد که سفیر همچنان در بیروت به فعالیت خود ادامه می‌دهد.
اسماعیل بقایی آن زمان گفت: «سفیر ایران با توجه به مباحثی که توسط جهات ذی‌ربط لبنانی مطرح شد و جمع‌بندی که صورت گرفت، به کار خود به عنوان سفیر در بیروت ادامه خواهد داد و کماکان در آن‌جا حضور دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77979" target="_blank">📅 17:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/282709f91d.mp4?token=r7w4gWxHLP2TOnFRbKqoNp5bjp42FrxRrtef0-FBMQJUYDHSB7MR2tfz061NpvhFODjV1_Mknzdz9YuAQlMD1V7uuX4vWCmiE9zUGXDpLzIaNudPQ4u0qv3RBDQDCHu81SqtV9tM8FUEoFeCVGVh9MRvG0b_91w-y2dCPdcJD39fcxmPCjWE-28CJUmHok63MbCgWkcvsQgX72klkhHqIpvw4h5zk6okJyl_AZESv10pryTk45gHcDuW6kWA60HosOUGLQYL1LrAOSDkwRBe_3SeXBuGbg--0HlPIB6Ku9Iq4YDDH7fJmDKPNxvT4ZGjOG1Awpz5Bxq0bsRlo6GPLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/282709f91d.mp4?token=r7w4gWxHLP2TOnFRbKqoNp5bjp42FrxRrtef0-FBMQJUYDHSB7MR2tfz061NpvhFODjV1_Mknzdz9YuAQlMD1V7uuX4vWCmiE9zUGXDpLzIaNudPQ4u0qv3RBDQDCHu81SqtV9tM8FUEoFeCVGVh9MRvG0b_91w-y2dCPdcJD39fcxmPCjWE-28CJUmHok63MbCgWkcvsQgX72klkhHqIpvw4h5zk6okJyl_AZESv10pryTk45gHcDuW6kWA60HosOUGLQYL1LrAOSDkwRBe_3SeXBuGbg--0HlPIB6Ku9Iq4YDDH7fJmDKPNxvT4ZGjOG1Awpz5Bxq0bsRlo6GPLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"حمید مهدوی، متولد ۱۳۶۶، آتش‌نشان ساکن شهر مشهد شامگاه ۱۸ دی ۱۴۰۴ و در جریان اعتراضات کشته شد.
ویدئوی کوتاهی از او در حال حمل یک معترض مجروح بازتاب گسترده‌ای در رسانه‌های اجتماعی ایران و جهان داشت.
پیکر او در آرامستان روستای تویه دروار در شهرستان دامغان، زادگاه مادری‌اش به خاک سپرده شد."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/77978" target="_blank">📅 17:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gk3ZVyDOGeLFgmSmiUMJPxqwqyUdsJSh-NSZTVqH3ADR_xrFuf8LGLuytxed-wYAPtPh1bThESfIlECxh8J_TFdYZbQUhMmae2KuysRD6Fdo-UyheDyQ1EQnlImno9KFu5z-nRgsyCxAC3pVSuuZUj4snGUeDo4ipQaChaUdqAm8lchGDcmAS1ifzk4nMvr_rYIF_lRd-Z6tQSXkdodatfqD2I3Zt-h6EnP17CVwgkxb_a5XdmLXMxfGpjMUZfN9hwH49P_StFq7gHlet3Rpmxn4pSFo9KT22mgrH3VYKPXVsQ4e9sXLORMtcwbssVOSb3Pwxy1Q7tsBx-wWy6pCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون از افزایش شمار زندانیان سیاسی و عقیدتی در زندان شیبان اهواز خبر داده و گفته است بیش از ۶۰۰ نفر در بندهای مختلف این زندان نگهداری می‌شوند. بسیاری از این زندانیان، هستند که در موج بازداشت‌های پس از جنگ ۴۰ روزه ایران و آمریکا و اسرائیل بازداشت شده‌اند.
تعداد قابل‌توجهی از بازداشت‌شدگان جدید را جوانان تشکیل می‌دهند و سن بیشتر آنها بین ۱۸ تا ۲۵ سال است و اکثرا از اهالی اهواز، فلاحیه (شادگان)، ایذه، بهبهان و مسجدسلیمان هستند. در این زندان بیش از ۳۱۰ نفر در قرنطینه محبوس هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77977" target="_blank">📅 17:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8Apxl889GbNNTX-hIQayWj06sJrImPAM-iAPKVZSSpUH7SIFNYJis6QNaX8vjOwNethovuJL0Csd6Yyab8cnwjCuGufb_Ov7UGdPw8FV88VxOAtQnZQKVW9H0NduGAcekS-vt7W-K3RKJhujGjibwsCr4KKLMaie--24HQ7JNOBCspq5UoymZvGP38PrjA78JEGSVu9jkYBrWRNAjY2Jl7JNm6RxlsDrFTnpNzHiaOras9hNDZLLZnYI-s-ntBN_QESxkxzdpI8iGnDe_MhQ5v503eXNwziRBZg7kCb9-8xOUKUDXkl5MUgFciocOAE97aG5gmYPpwRy1Uf1D0fBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ozdlti6suVTkOXU6VRtFokgvYpjuecHS_d4nERVAV07uzGdOQPgR4O92oaPVi8jstKId4BoDv7w12P7hjDyg8t2bX52-VHsee3xwbCSJ64Moqj91xmGeRIyE53K_f4CEt36wLLgfGvJG3GMIER8V0fD5W5YfMISEHcaAzY-M2nh8_hgps-6X7gERjRRzj-VXXRbKCHSEKdFK7DpJbtMLNTioHOSWM-e7ZemYwrhwMptL6zfGSswRrNi3wl23dLjS9yQ1Hg3m-tBxwJRY0eqSQMgh7COd6BmjFnoLzKqegV04zFkwt5MD5J1MTKlGqyTHaieWu6mT9TKNW1YfwV6INg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UBqn98qxAUvNnf14GhAKzVMcPfKU8D574VUUpYx9Y5W97UJ3l97xZNJYrmYzRQKUA8y0nXJpZjGW7ng4hgkIVQ1xjXpoZleTVLYIXh_fNy5i2IMkg97bjoqHczpxVfWDuaU7hQFNrCYy5inRnG7ojLhyMxbah_G4cC3FcW06uTOkQCLVJyKqG4RBbgq7DI53jhcRN45C8CWF8nsao-NfIGjpnmVRquWa2P4JE52GqAj4MstvpbHddR398aDWqjVfDWEzH6l_PmupfRa8rmekhl5twMkqixD2fPgc8AOBcUow167K9TRl0Bly3eNY9CI1M5JL2z411C3l5qCiPBAQJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rpIiRVGgl03-YtW8zWYMPc37T41bvlruNIOQJMJDwYG7T-EDSeiIWBsx2m4WV6s76IBywd4pnRUckLNjqVyMiQ_Xasv2v-q8H9z5XGFArYzCeiJTlDa2wAbBFOn_UCB8_eWX9OfMmtiZIgQQfS1DUcx0lAu7RmPH6NuuzUe8z_axT2uEqwpEhlf9PR7eQkaVt8Jj2qF4jBSJWeXr5w28-ZabaVbq28GhhCvAnfIedJvQgBMDR4lW3N0ogt1hAJzpTTDa4Uy84QByhFAF4i-pCm8ONtX6mVZYCxCmG--nDWatNVIdbR6z9UoBCDboGPlm2QRySOfWmyciyxKxGm7Tig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه ۲۹ مرداد گفت طرح واشینگتن برای افزایش شدید تحریم‌های اقتصادی علیه ایران با هدف «سرنگونی» حکومت جمهوری اسلامی دنبال می‌شود.
بسنت در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «این طرح در ایران جواب خواهد داد و ما این رژیم را سرنگون خواهیم کرد.»
او افزود: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود.»
وزیر خزانه‌داری آمریکا روز ۲۳ مرداد نیز خبر داده بود دولت دونالد ترامپ قصد دارد اقداماتی در مقابل ایران انجام دهد که به گفته او «در تاریخ انزوای اقتصادی یک کشور بی‌سابقه بوده است».
او گفت: «اگر ما حداکثر فشار اقتصادی را اعمال کنیم، به احتمال زیاد دیگر شاهد ازسرگیری یک عملیات نظامی گسترده نخواهیم بود؛ اما تأکید می‌کنم که این وضعیت مربوط به حالا است.»
اسکات بسنت همچنین خبر داد که روز دوشنبه هفته آینده یک نشست خبری برگزار خواهد کرد تا «دقیقاً درباره اقداماتی که قرار است انجام دهیم» در قبال ایران توضیح دهد.
هشدار به متحدان آمریکا
وزیر خزانه‌داری آمریکا همچنین در پی اعلام طرح جدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای تشدید فشار اقتصادی بر ایران، به متحدان واشینگتن هشدار داد که در موضوع انزوای اقتصادی ایران باید میان «همراهی با آمریکا یا قرار گرفتن در برابر آن» یکی را انتخاب کنند.
او دربارهٔ پیام خود به متحدان آمریکا گفت: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود. ما به آنها می‌گوییم که یا با ما هستید یا علیه ما.»
وزیر خزانه‌داری آمریکا در پاسخ به پرسشی دربارهٔ احتمال اعمال فشار واشینگتن بر چین نیز گفت: «بسیاری از گفت‌وگوها بهتر است در خفا انجام شوند»، اما همزمان از پکن خواست «با این برنامه همراه شود.»
او گفت: «ما اطمینان داریم که همه خواهان بازگشایی تنگه هرمز و کاهش دوباره قیمت انرژی هستند.»
بسنت در ادامه با اشاره به وابستگی چین به نفت خلیج فارس افزود: «در نظر داشته باشید که ۵۰ درصد انرژی چین از داخل خلیج فارس تأمین می‌شود. بنابراین، همراه شدن با این برنامه می‌تواند خدمت بزرگی به خود آنها باشد.»
این اعلام موضع وزیر خزانه‌داری آمریکا یک روز پس از آن است که رئیس‌جمهور ایالات متحده اعلام کرد که کارزار جدید و بزرگی را برای هدف قرار دادن اقتصاد ایران به راه انداخته است.
دونالد ترامپ شامگاه چهارشنبه در شبکه اجتماعی خود، تروث سوشال، نوشت: «امروز، من کوبنده‌ترین عملیات اقتصادی‌ را که تاکنون علیه کشوری انجام شده است، اعلام می‌کنم! این یک جنگ و انزوای اقتصادی در مقیاسی بی‌سابقه خواهد بود».
او افزود: «همچنین اعلام می‌کنم که هر کشوری که به نهادهای مالی، کسب‌وکارها، فرودگاه‌ها یا ارگان‌های دولتی خود اجازه دهد هرگونه راه نجاتی برای ایران فراهم کنند، خود با عواقب اقتصادی بسیار سنگینی روبه‌رو خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KsSW0bAIpFkDAZyZI_KUtWoLqQSs26bc34dy3-9UzvVW6sl-eslQ3MoYb2puYalQVSv7qeSugvuhApDfMdKBveWi36GobdXolmK30ObreiOkGvJTTnbmQthzQQcHICvnrA8gtvQZL-4d_a0s2oDtntI9cHClILTaAafAn-CukT6iu4AzZ5DSvzwWizOlWSa_Jo0QC8AL-dzrK76uAny8aa8I_7xmA54qZfFA94j72tE_CZB_Gbm5ucr8CjL35TvTWBBy0-XZHlbm2TuOndv4mPDeLffjscRl6-WY7UqwWdJ_xjacjl3ZguIXWjdE6T4Q8IYWtiDmkBoZKkdMX3bDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ocPZp547I1CWz1MyIK1y0Ao4yyNZaM3a2Ee1LsrMm1LEq7KfDqCjyTjDvKLRWql0HCtZ-astpU_ToUwsaQiVoyYgRi7vPaXvq2PCkxaf9wfmtM002ZDfvMyVSLOhXlBeZ1PAkTpVEGpZuozst_b_rjRvzM3YaCwV-wVikAnut5-T_W7O6jz7yYkos-SITfVQjw0EXO1M3GXVFE69e0PDf_13II7MPC605tUiB1T8RrVI80sPQiBt7hABCQRRjYr6OMA7fGOql724aELCYgXSd5mf5J64OLM8JtZCrp5qnF7L2JOlX5phy2Zs0a13zPzxLYBylepWV0GvKNP3dRdXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fYI698V8k1g7zCMWcgK4Vj6XJNLLI7wBMP3yqWDMSxJG1Vki2gd21DabyFwxwjO_gvUcTbqzBxiiqXzIeZUAyH4i4HzNvEJG97aWZmLI4Ec3hewYlzkdq1-maOuBOl-l2NfVRCIqRe_dNXKxa5VzV5-oyGLL8zZJBlzbieds24lNVoQcB_Gcc48-s-WnBtLXnQTVyl5o9r4O2J_gANPKIME3q9f67R9UkCmxJATNKl_y7xmPZb0ATErMmDfi9kaUFI4YyenOQhC8tGXzyan_ExY6LhkFbAefXkLO5rkLnb8U9A7n50N5CvFyRot1EVTCi5yVsMbhSwVZUApRulETDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=sHbp0KTnWHzpqGWolK0BvqOrqdxgafhzBoJH6WrcNj8mw5p87NBAQAY2mjjWdTjujFjPmizBXFiRqRTIHq2NvWar-NEhRhSrlEQnyM6nTBsLMRJRFAabmAmtD0UtVX-oJH73RhMYLaUqKrTi3uPg5ml8YQtVcHUFsyay-X-03dNAv14_OQ16kiSNrPYDl3q7MnWu1zXgSHmAhJaig0rYPWExpkKnHjBqITJcrRp48s73cG0beJgKMA5HME79SB4DhMYQhO_1nwPJhLZ6V1olSqJpIJQ54Yc7l3qNEeFLN_IMUEe907Tdo4ugGGr8QKfgDyjroIBPAQ7l5uhbkzc5LoEWUw5aqDhduYaarun2A2Q910faGkaFUgW6bKXtYjqmKWx4RABWBq5WZNkE4DdRoxFx07diag1osaZrKdHOXkFS7BL2fVfEGj-zt_FZrQ7o4TVoypTTVRfUGdCzM0VF3uDSmaO0GrsI6a04xJXk2A3jrNFihjooB7UXrukHxSdqMCRh6lNbzYA0eh5BujVD3YGTXkGIzu-CecwslWtvyp04fzkcv_IV930CocuyIj_Jg0Wwtfwgjb7swUGO-Wxuw1mTXhsnhcJZQOscvqLEftvvWe7Zx6444EB_2bQ-aki0RunjjUAAiKdWgMhrHEqOTlW4DnrnAy81P9zxkyREWF4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=sHbp0KTnWHzpqGWolK0BvqOrqdxgafhzBoJH6WrcNj8mw5p87NBAQAY2mjjWdTjujFjPmizBXFiRqRTIHq2NvWar-NEhRhSrlEQnyM6nTBsLMRJRFAabmAmtD0UtVX-oJH73RhMYLaUqKrTi3uPg5ml8YQtVcHUFsyay-X-03dNAv14_OQ16kiSNrPYDl3q7MnWu1zXgSHmAhJaig0rYPWExpkKnHjBqITJcrRp48s73cG0beJgKMA5HME79SB4DhMYQhO_1nwPJhLZ6V1olSqJpIJQ54Yc7l3qNEeFLN_IMUEe907Tdo4ugGGr8QKfgDyjroIBPAQ7l5uhbkzc5LoEWUw5aqDhduYaarun2A2Q910faGkaFUgW6bKXtYjqmKWx4RABWBq5WZNkE4DdRoxFx07diag1osaZrKdHOXkFS7BL2fVfEGj-zt_FZrQ7o4TVoypTTVRfUGdCzM0VF3uDSmaO0GrsI6a04xJXk2A3jrNFihjooB7UXrukHxSdqMCRh6lNbzYA0eh5BujVD3YGTXkGIzu-CecwslWtvyp04fzkcv_IV930CocuyIj_Jg0Wwtfwgjb7swUGO-Wxuw1mTXhsnhcJZQOscvqLEftvvWe7Zx6444EB_2bQ-aki0RunjjUAAiKdWgMhrHEqOTlW4DnrnAy81P9zxkyREWF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TxMFmSDbqYU22g8dtLwvv4pcBkJfYZOOTVOQl18PTrb6QAshDpiGAZo0RZs6m2BbWomWePZbWfAYj-ZvpiTGi-oefSe7_ccrZmSO7QmUt_O4tiVgAQgGF9xeeHXcYVstkycRetsUre01gMqhIk7MxxPb8g79I_lzh9djhFMQkkbexBi3IOxFW0Fprhfkr_crAcMeTXnFDr-IkWN70kX74f1OjbYyFQZvCnFepqz8FLqx2Jb89BiOHZTO7DgIf57hEurCHhrxqwjxCYvV0DBORx7dobLHwKeWLk5VdkKvSLP083mCdxCIY2_f7X2ljgJ20GPrR4TguNv0ROVgeCl_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TgKdOVAtP2IXlvFnBcR_H9AEAlMf_7E1Dd_oqNRzOiadO8OELq7ZOObta1FOW58e2btX-LoCn7dt1eDibhBtJP12J8RTVgVD_NkRvNIIAC1CrA5yDFfIlsf23jJcX-pfWlxTijCSt2CkH2o1ue5uoHOe_Yd4Sa7-cZIcbRJB2oVhrxjPMPdgzpR2Pz8bwAGVdl-jHD5XN2VS7L-bU9MNHpGPk_8JMOTeurpvncvbUGV-dr5aBp-TOk4j5a6lJ_hEQjIFcozP3_PUBqWDITRuuwXVauURbTJfafvZIjuelXc5byiy7kXxn5ZMbElwyiP5Gv1r_UZAZVCG6_IuD0_07Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، تهدید دونالد ترامپ مبنی بر آغاز کارزار اقتصادی گسترده موسوم به «روز دی اقتصادی» علیه ایران را تلاش برای سرپوش گذاشتن بر «بحران‌های داخلی آمریکاست» توصیف کرد و از «بدهی‌های بی‌سابقه و هزینه‌های فزاینده نرخ بهره» به عنوان نمونه‌هایی از این بحران‌ها نام برد.
@
VahidOOnLine
معاون وزیر امور خارجه جمهوری اسلامی ایران سخنان ترامپ در مورد کارزار «روز دی اقتصادی» علیه ایران را تلاش «محاسبات غلطی» خواند که برای پوشاندن «شکست‌ بزرگتری» ساخته شده است.
کاظم غریب‌آبادی نوشت: «ادعا می‌کنند ایران در آستانه شکست است و به یک نخ بند است، اما به همه متحدانشان التماس می‌کنند که کمکشان کنند.»
معاون وزیر امور خارجه ایران در ادامه افزود: «جنگ نظامی نتیجه نداد، حالا اسم شکست بعدی را جنگ اقتصادی گذاشته‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=sUptHP1RJzJsLuY_I9a7jGPZoAPRWzWN0NNVlpUevn8nGB6O30KWLeR25I-Ph8pETOeAM0w0TEaKozzF2sjYMumI7wpS2CzDtcZT9-Z1IXLCZC5sNMnUGhBceV8mOuN6lF44vyVao5c2H5cv_YQLIBS3W_byzyFdwt_ROtcdzCwUDAlPXvUxOCEUUGppwSnjivnyJ5ShwT8QvF0nxBHHo-NSZ8X4FiDZEeaDQz9KNGgF9ESBDTrwXU8NlryknIFjMnd8hOjKtltAQMPOSmDxrjm5UqlzcSz8sHAmTL35XWZHKxef1W08-YF_fU9JR3swlqgWt0jBKpeUaq-n_x-JGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=sUptHP1RJzJsLuY_I9a7jGPZoAPRWzWN0NNVlpUevn8nGB6O30KWLeR25I-Ph8pETOeAM0w0TEaKozzF2sjYMumI7wpS2CzDtcZT9-Z1IXLCZC5sNMnUGhBceV8mOuN6lF44vyVao5c2H5cv_YQLIBS3W_byzyFdwt_ROtcdzCwUDAlPXvUxOCEUUGppwSnjivnyJ5ShwT8QvF0nxBHHo-NSZ8X4FiDZEeaDQz9KNGgF9ESBDTrwXU8NlryknIFjMnd8hOjKtltAQMPOSmDxrjm5UqlzcSz8sHAmTL35XWZHKxef1W08-YF_fU9JR3swlqgWt0jBKpeUaq-n_x-JGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالناصر همتی، رئیس بانک مرکزی ایران، در یک گفت‌وگوی تلویزیونی تأیید کرد که صادرات نفت ایران در حال حاضر متوقف شده است.
او شامگاه چهارشنبه ۲۸ مرداد اظهار امیدواری کرد که تفاهم‌نامهٔ ایران و آمریکا احیا و مذاکرات از سر گرفته شود.
این نخستین بار است که یک مقام رسمی جمهوری اسلامی به شکل رسمی از «توقف» صادرات نفت ایران خبر می‌دهد.
در هفته‌های اخیر برخی مقام‌های جمهوری اسلامی با اشاره به تشدید بحران اقتصادی و معیشتی، نسبت به دور تازه اعتراض‌ها هشدار داده و از آمادگی برای برخورد با آن خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77963" target="_blank">📅 15:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmohnyewXrTvsH6y_ge0RKA12EsdDtye5mPVxBKiVz54rX5GlOM44b8qSrHfzA_TjOnuzve8aMSD2ToWwnfzZZSDt88V6-3R-Mpmx9kulLM8bUrXk8gn8varglp6-OZjthpiF6zwLmIeeRe8icVWL9X_-em5gMrS8rWtuXHJbP-nEV9mnR9ueJOW_LH6Qi2CTWxkP45t7nasqgzOKxoWnwY2YnbhROOOLLpe28F1Eu2s95rtOjY5z0O9Kgauk0UHD5fMFgRqYBAAcZRbU03EEtvsNgoHn_q4U1KkjwgC_3LvSCtCperq7HIQhHiNOuPHwqJTRyEj1JLiGGpzaMmWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی صبح پنج‌شنبه ۲۹ مرداد ۱۴۰۵ «قائم حسینی»، معروف به «آرین»، را در ارتباط با اعتراضات دی‌ماه اصفهان اعدام کرد. او پنجمین فردی است که در پرونده موسوم به «میدان علیخانی» اعدام می‌شود.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حسینی را «تبعه خارجی» معرفی کرده، اما تابعیت او را اعلام نکرده است. در این گزارش همچنین اطلاعاتی درباره زمان بازداشت و محل نگهداری منتشر نشده است.
قوه قضاییه حسینی را به «دخالت در وقایع میدان علیخانی اصفهان»، کشیدن سلاح، ایجاد رعب‌ووحشت و ناامنی گسترده و اقدام علیه امنیت ملی متهم کرده بود. براساس گزارش رسانه‌های حکومتی، حکم اعدام او پس از بررسی فرجام‌خواهی در دیوان عالی کشور عینا تایید و اجرا شده است.
قوه قضاییه پیش‌تر «ابوالفضل سپاهی»، «امیرحسین صفری»، «عرفان اسفندیاری» و «گل‌محمد محمدی» [پسرعمه قائم حسینی] را در ارتباط با همین پرونده اعدام کرده بود. همچنین میزان اعلام کرده بود که برای ۱۶ نفر در این پرونده کیفرخواست صادر شده است.
شروین باقریان، امیرحسین ملکی و علیرضا سپاهی، سه محکوم دیگر این پرونده‌اند که درباره احکام نهایی و وضعیت کنونی آن‌ها اطلاعات شفافی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77962" target="_blank">📅 15:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/klPrOcQN7kM0KYGhHKCFil2g9T1loVJxJfonXDrv3VfOqOPAHUT0NHXErynsTsID651BhiGwBjZttBtrdQJoBBqKqDsceLuUqqKoWqKFrnh3u4t0hnBYIsgYhDyfKFDpMbtEUvBUGIpc90XrbPjxao8sKkMdcutuggxpmMVJPYy4TBmDgcFs8z_9IbuczyQQdS-Y3BMHtxrPRL16FmGJJ4d6aaJfnCSBRvJzc80uGtS5CuATioqeZiEva6_qnG_HCDntY5gL0FdNfOrgeh79vL3EpV55rRl9icfwG2CjRE3LSy579ggWsGFXVVB3U-5P3CBJaJ8Nx1t9ovbZy8Ic-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ:
هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند.
بنابراین، امروز اعلام می‌کنم که
کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد!
این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
امروز همچنین اعلام می‌کنم که
هر کشوری
که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با
پیامدهای اقتصادی عظیمی
روبه‌رو خواهد شد.
قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید
همین حالا
متوقف شوند. خودتان می‌دانید چه کسانی هستید.
این یک
D-Day  اقتصادی (ECONOMIC D-DAY)
خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور
دونالد جی. ترامپ
realDonaldTrump
توضیح چت‌جی‌پی‌تی: D-Day در اصل اصطلاح نظامی برای «روز آغاز یک عملیات بزرگ» است، اما در کاربرد عمومی تقریباً بلافاصله عملیات نرماندی در ۶ ژوئن ۱۹۴۴ و آغاز تهاجم گسترده متفقین در اروپا را تداعی می‌کند. بنابراین ترامپ با گفتن ECONOMIC D-DAY می‌خواهد بگوید این اقدامات اقتصادی قرار است چیزی شبیه یک حمله بزرگ، تعیین‌کننده و همه‌جانبه در جنگ اقتصادی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77961" target="_blank">📅 02:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77960" target="_blank">📅 01:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j7uVLPJkhJekySf3Uxb3Yknto36IgYpXtbtJGCmnA4S-8drNB6dKOYgCQJMSPYzaeSWY7Kgl387j7dFEe_s4S3JxJyulmr564i_ZgvYI8Q51uvSZe5sqnrgiJk-R_eAXV_rMJ9uRqs4wSJamFHeBkXSp4gLKMTPpmvVxcpdI9hOBvVvWcuMj1MdK6uPr73qloTnNB6VgryEW0hpXR73E5_hV-me2Q8XtfqdbJsQm5W5Vabn6XZQAIQg2-ma0gpJHg537ONjwVeLmk5uP1n4jRbc9r_VuFFDH-KQvtTdG5_APv-6ny_Ypz5vQ5vyZKrhlVCOY69X6h5gdCjfqT_Yzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس، روز چهارشنبه ۲۸مرداد ۱۴۰۵، گزارش داد، ارتش آمریکا طی هفته‌های گذشته یک مسیر کشتیرانی تحت کنترل خود در بخش جنوبی تنگه هرمز ایجاد کرده که امکان انتقال روزانه میلیون‌ها بشکه نفت به بازار جهانی را فراهم کرده است؛ اقدامی که به گفته دو مقام آمریکایی، بخشی از اختلال ایجاد شده در صادرات نفت در جریان جنگ را کاهش داده است.
این دو مقام آمریکایی به اکسیوس گفتند در چارچوب این عملیات، هر شب حدود ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز و در امتداد ساحل عمان وارد یا خارج می‌شوند. به گفته آنها، اکنون حدود ۱۰ میلیون بشکه نفت در روز از طریق این مسیر از تنگه خارج و وارد بازار جهانی می‌شود؛ رقمی که تقریبا نیمی از حجم انتقال نفت پیش از جنگ است.
به نوشته اکسیوس، عملیات آمریکا تنها به اسکورت نفتکش‌های حامل نفت محدود نمی‌شود. نیروهای آمریکایی نفتکش‌های خالی را نیز از دریای عرب از مسیر تنگه هرمز وارد خلیج می‌کنند تا این نفتکش‌ها پس از بارگیری نفت در بنادر کشورهای منطقه، دوباره از مسیر جنوبی تنگه خارج شوند.
یکی از مقام‌های آمریکایی که از نزدیک در جریان این عملیات قرار دارد، گفت آمریکا حدود دو ماه است مسیر جنوبی تنگه هرمز را تحت کنترل دارد. او افزود سپاه پاسداران ممکن است برای کشتی‌ها «مزاحمت» ایجاد کند، اما کنترل تنگه را در اختیار ندارد.
بر اساس این گزارش، عملیات انتقال نفت از سوی یک گروه ویژه مستقر در مقر ارتش آمریکا در فورت براگ در ایالت کارولینای شمالی هماهنگ می‌شود. این گروه با کشورهای عرب منطقه همکاری دارد و هر روز فهرستی از کشتی‌هایی که قرار است از خلیج فارس وارد دریای عرب شوند و همچنین نفتکش‌های خالی که برای بارگیری نفت وارد خلیج می‌شوند، تهیه می‌کند.
کشتی‌ها هر شب در دو بازه زمانی مشخص، در قالب دو کاروان جداگانه برای ورود و خروج از تنگه حرکت می‌کنند و با هدایت نیروهای آمریکایی از مسیر جنوبی عبور می‌کنند. جنگنده‌های نیروی هوایی آمریکا نیز برای مقابله با موشک‌های کروز و پهپادهای ایران از این عملیات محافظت می‌کنند.
به گفته مقام‌های آمریکایی، ایجاد این مسیر پس از یک عملیات دو هفته‌ای فرماندهی مرکزی آمریکا، سنتکام، علیه سامانه‌های راداری و نظارت دریایی ایران امکان‌پذیر شد. در نتیجه این عملیات، توان ایران برای رصد تردد کشتی‌ها در مسیر جنوبی تنگه هرمز کاهش یافته است.
مقام‌های آمریکایی می‌گویند ایران اکنون برای نظارت بر این مسیر عمدتا به چند رادار بازسازی‌شده و نیروهای مستقر در قایق‌های تندروی سپاه متکی است. به گفته آنها، کاهش توان رصد باعث شده است حملات پهپادی و موشک‌های کروز ایران بیشتر به سمت مناطقی انجام شود که احتمال می‌رود کشتی‌ها در آن تردد داشته باشند.
اکسیوس گزارش داده است که شماری از کشتی‌ها در حملات ایران آسیب دیده‌اند، اما نیروهای آمریکایی نیز تعدادی از حملات را رهگیری کرده‌اند. به گفته یکی از مقام‌های آمریکایی، نیروهای این کشور در اوایل هفته جاری هشت پهپاد و دو موشک کروز ایرانی را سرنگون کردند.
بر اساس این گزارش، طی دو هفته گذشته هر شب ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز عبور کرده‌اند و میانگین انتقال روزانه نفت اکنون به نزدیک ۱۰ میلیون بشکه رسیده است. مقام‌های آمریکایی می‌گویند در برخی شب‌های هفته‌های اخیر، حجم نفت خارج‌شده از خلیج فارس به ۱۵ تا ۲۰ میلیون بشکه نیز رسیده است.
به گفته یکی از این مقام‌ها، در یکی از شب‌های این هفته بیش از ۲۰ کشتی برای عبور از مسیر جنوبی تنگه برنامه‌ریزی شده بود و در صورت اجرای کامل برنامه، حدود ۱۵ میلیون بشکه نفت از خلیج خارج می‌شد.
دونالد ترامپ، رییس‌جمهوری آمریکا، نیز در گفت‌وگو با اکسیوس گفت «حجم بسیار زیادی نفت» از تنگه هرمز خارج می‌شود. او در عین حال گفت آمریکا در حال حاضر با ایران مذاکره نمی‌کند و افزود جمهوری اسلامی در مذاکرات «وقت تلف می‌کند».
ترامپ همچنین گفت ایران هنوز توان مقاومت دارد، اما در مجموع «بسیار ضعیف‌تر از گذشته» شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77959" target="_blank">📅 01:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=a1t1PGYbVHADLPgIn2YHQmSrHqhWpOi0jRB_LMhOZtf3uJJHuhzaBaWfkH7TfR5-FY1ii8QB1Bofwpt35bKIZ5r8BKCPEo274bD3fxFeTgrRkJrwPg_h5pYnB28LOtqPgTSyTnc-JGI-V6VngvAfC_4Yrxh3S4ODtEAGaRU6HjVLpVDlhQm4YGjL74hzl9p2Kyc0jvP2ubrhJCi7EKoqOnhTwXLvL-ukymEyw8mbx9wLY2bsTkrvbBlxTMTKs9QfwODYbRBzW66ig5ig60KZi--UR4DGDdyxSJO0TmKZESsKlivZs56YEwPlQSxJ7-iGOHF7BzYk7uBwyu02o-4BwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=a1t1PGYbVHADLPgIn2YHQmSrHqhWpOi0jRB_LMhOZtf3uJJHuhzaBaWfkH7TfR5-FY1ii8QB1Bofwpt35bKIZ5r8BKCPEo274bD3fxFeTgrRkJrwPg_h5pYnB28LOtqPgTSyTnc-JGI-V6VngvAfC_4Yrxh3S4ODtEAGaRU6HjVLpVDlhQm4YGjL74hzl9p2Kyc0jvP2ubrhJCi7EKoqOnhTwXLvL-ukymEyw8mbx9wLY2bsTkrvbBlxTMTKs9QfwODYbRBzW66ig5ig60KZi--UR4DGDdyxSJO0TmKZESsKlivZs56YEwPlQSxJ7-iGOHF7BzYk7uBwyu02o-4BwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: وزیر خزانه‌داری می‌گوید ممکن است همین هفته شاهد اثرگذارترین تحریم‌ها علیه ایران باشیم. این تحریم‌ها چه زمانی اعمال می‌شوند و چه چیز دیگری ممکن است در ایران تحریم شود؟
🔻
ترامپ:
خب، چیزهایی داریم که می‌توانیم تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه می‌شود.
در حال حاضر، تنگه باز است. کشتی‌های زیادی در حال عبورند. این را گزارش نمی‌کنند و ممکن است در مقطعی کمی کند شود، اما همین حالا تعداد زیادی از کشتی‌ها در حال عبورند.
محاصره دریایی بسیار مؤثر بوده است. صفر. یعنی واقعاً، تا وقتی برقرار بوده — و مدت زیادی هم هست که برقرار است — به‌جز یکی دو وقفه کوتاه که عمداً آن را بر اساس یک توافق باز کردیم. اما آن توافق به نتیجه نرسید. می‌دانید، توافق آن‌طور که آنها گفته بودند از آب درنیامد؛ وقتی یک چیز به ما می‌گویند و کار دیگری می‌کنند.
اما محاصره ۱۰۰ درصد موفق بوده است. هیچ کشتی‌ای وارد ایران نشده، اما کشتی‌ها برای جاهای دیگر وارد می‌شوند. خواهیم دید. خواهیم دید چه می‌شود.
یا اوضاع بسیار خوب خواهد شد و قیمت نفت مثل سنگ سقوط خواهد کرد، یا دقیقاً همان کاری را که داریم می‌کنیم ادامه می‌دهیم. می‌دانید، از ۳۵۰ دلار برای هر بشکه حرف می‌زدند و امروز ۸۴، ۸۵ دلار است و ما داریم نفت زیادی استخراج می‌کنیم.
اما اتفاق دیگری که افتاده این است که مردم گزینه‌های جایگزین دیگری پیدا کرده‌اند که هرگز به آنها فکر نمی‌کردند: تگزاس، آلاسکا، لوئیزیانا و جاهای دیگر. علاوه بر این، تعداد بی‌سابقه‌ای خط لوله در حال ساخت است. بنابراین فکر می‌کنم تنگه هرمز دیگر به آن اندازه که در گذشته اهمیت داشت، مهم نخواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77958" target="_blank">📅 01:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LVQ6K2_4UPEARd9hRws3WEWrURlPHFwsN2RopM3d9-X6N_CNGsnFxzsZNpRCw1Qhj8O2EdlteTFuxDa1EP04GB6HoYTOQ9bshfpYX7H0jkQJvhWYm-V7e1j612idQKk7YADWo5VT2357jMKcyESSMKfR4rDo3oLzfjIYdPyLX1SM86GFDZbnVvghQfZ3RkhoynK_9asZpjuaL45vmvyBsPPgVcBXJNeB_ZUqD1eo54p-bT7wufbBUAu9qHEPsHy3p2oA_hgC2HzDc-CgPjfK_6QixSlVp3SM2qr91VDdh-IR-lpH_290IkTRZTV0RRFsbDBiuheurbU9g5jLuJfFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فرانسه روز چهارشنبه نیلوفر شادمهری، رایزن فرهنگی سفارت ایران، در این کشور را اخراج کرد.
ساعاتی پیشتر وزیر امور خارجه فرانسه رسما خبر داده بود که به عنوان اقدام متقابل دو وابسته سفارت ایران را از فرانسه اخراج خواهد کرد.
هنوز نام و سمت فرد دوم که از فرانسه اخراج خواهد شد اعلام نشده است.
پس از آن که وزارت خارجۀ ایران در بیانیه‌ای دو تن از کارکنان پیشین سفارت فرانسه در تهران را عنصر نامطلوب اعلام کرد، فرانسه نیز از اقدام متقابل درباره دو دیپلمات ایرانی خبر داد.
در بیانیه وزارت خارجه ایران آمده بود که با توجه به «فعالیت‌های خلاف حقوق بین‌الملل، به‌ویژه کنوانسیون روابط دیپلماتیک ۱۹۶۱» از سوی دو مامور شاغل در سفارت فرانسه، این دو فرد عنصر نامطلوب شناخته شده و حق بازگشت به ایران را نخواهند داشت.
طی روزهای اخیر مشخص شده که این دو فرد، از کارکنان بخش فرهنگی سفارت فرانسه بوده‌اند و ظاهراً در ارتباط با پروژه‌ای فرهنگی، با دو گرافیست ایرانی دیدار کرده بودند.
این دو گرافیست هم از همان زمان در بازداشت هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77957" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=WzFk469HZEitQRUrZ73iDx8B0yVK3CJOhdvcseXbovKfWRQVrL5O0wsBi6FPTbWm36v4uBiKUZDuttfEMs1oMGvXSCJ0O3d1t9jrgKdGFg8BKkjzq3uOS1MIPps-ujySlqtyt9P_y2qAEpdYr2X4SuDQGSSF-7i2AX3Gx1Tlst4LIHXqooHxJ67OCtKhEv871Wcr-oFU5J-0M7eTvk38d4JwusS-gM912hGFbC-I-Sxfl07awYcjrBcQAcU4xTzYrZ3_wlzsalyAGZSXTe54kL2DO2GXl8l5z8v0ir3hd8MUvxwaPVCDhsygzcYJIOi82YHuVdRjayOEKR5Rnb36JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=WzFk469HZEitQRUrZ73iDx8B0yVK3CJOhdvcseXbovKfWRQVrL5O0wsBi6FPTbWm36v4uBiKUZDuttfEMs1oMGvXSCJ0O3d1t9jrgKdGFg8BKkjzq3uOS1MIPps-ujySlqtyt9P_y2qAEpdYr2X4SuDQGSSF-7i2AX3Gx1Tlst4LIHXqooHxJ67OCtKhEv871Wcr-oFU5J-0M7eTvk38d4JwusS-gM912hGFbC-I-Sxfl07awYcjrBcQAcU4xTzYrZ3_wlzsalyAGZSXTe54kL2DO2GXl8l5z8v0ir3hd8MUvxwaPVCDhsygzcYJIOi82YHuVdRjayOEKR5Rnb36JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hI9MLDx1e0UXlzqcufLC8VwM8Rn968N9op5av-fgeGNj8qLC7Wj_LusdcanH0730QMvlyMBma3DswibQKWIYpNj85Rzv4qK4nRFq05MbqZUZqUuhJ7LmmutFk6EnGkXUy0rIywqzCESeaHmUVUVmra3Erj1xXcuZGW8nhpjx_cO5N1A1O5SU1xu1eoEfOTpl30vmIXbX8HIvgyZRbICtyduFFOhEYWvpxj6Rx-75ve34nk-mQ_YbvhV2R7xrb0BSw2MXCFydLekY7DoZd_hK0iamV-ZC9F6h22bCbNXHBu1Ws4svoS0mPeubWtDGsy1SvomDAMG_kKvFn2SQQEcSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kie7h8omwo5DUGDWg8m-JMz-pM9VLrIPJVF8DLYhTP5e8Knvuaps8r8N-hC4uJtUcqN1qLS-U19iNbor2nSzYKnaVxNq5V-Chbzphp_xPzZ2V8ULkEEgCwuIH-f6oZFpO80LKufpHKA3n1jYMq-LD9oNbNkygQnrAm924-Bxw3eHvM8ittvj6osbtTwLI5TkvKNSP4kPaTj3IlBLcJo7gq5Pu4v-7EJmsMZ35_7ygWSM2gPJIg5EFencJFNj6ezvFCOyKMwtFQBTMyfaDdt66zZ3mIaSQUZbNMgyLofTxSqVCJXL5CSyb6a0wsSMPvNmxefwuSdzLe1jBAwKmDjx8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZkVaoggMclCJJftrFjGXjpvokK91GIlv7WT-7yMKbJKYEyx7iM6tq1jClgqdEM203sqefbSkj8VlPBVdEjr3cHojXpghslonL3GzVAd1bwYYyFshieu-eCCdxt7w-pPquGtpxyGg_DXoZgA-DQ4sWY2Z8ZKLfjR7APXKApnuyqs_WslMjP57Xq0xnFdtKssyitOxrMlkGaTGFFyjDMElkk1sObQ_1-sYTBqtK7B1alGNI3OdfRlrPVBrIRYdzIbljRP44vRrS_B4avzsCVr13STkSvdhtu62vbsS5EIAXUjagX-3Vu9XhluvBOzn2fcMPT9mFqunyjuF5rtRy84bPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n9QTLbUXH7LjvXI9jw_HZHCjWYJqb7u7tfeMfMEPinqjvGybojAOl2pgQ0OV89COp_FXj3wT_M7w9VvLxxmnR-6oSvxUs8h4m2Q_jrtIoz9dSYYqq1GsilGDsP2MmR3vhHKj2auL_h2wvJ0KH4k8len7CKn0_KXvcoYywEq1Pz0evfsqZTJQcfcS_1xyiof1Kgn9NQwnTATND9md9wPZjLOuXrScGZT4HcsD26ROqthrjchyTXIFBNr79PZDGtOjfrX6eMPbiKwoLRPqZ0uBV_gQD12rJEyN0Q5tOmjRnIqvssUZqHFjKpvKxQLoheP7sZrtwzrPVsunXfBGFWNBGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روند افزایشی قیمت جهانی نفت، همزمان با مبهم‌تر شدن سرنوشت مذاکرات مربوط به بازگشایی تنگه هرمز، ادامه یافت و قیمت هر بشکه نفت خام برنت روز چهارشنبه ۲۸ مرداد با یک درصد افزایش نسبت به روز قبل به ۹۲ دلار رسید.
روز سه‌شنبه دونالد ترامپ گفت «هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است».
@
VahidHeadline
قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۲۸ مرداد بار دیگر افزایش قابل‌توجهی پیدا کرد و قیمت دلار آمریکا به ۱۹۱ هزار تومان رسید.
این بالاترین میزان برابری دلار آمریکا با ریال ایران در سه هفتهٔ اخیر محسوب می‌شود.
گزارش وب‌سایت‌های اعلام نرخ ارز و طلا نشان می‌دهد که قیمت یورو نیز بار دیگر از ۲۲۰ هزار تومان فراتر رفته و هر قیمت درهم امارات نیز از ۵۲ هزار تومان عبور کرده است.
روز چهارشنبه هر سکه طلا هم ۱۹۴ میلیون تومان معامله شد.
افزایش قیمت ارزهای خارجی و طلا به دنبال اعلام امارات متحده عربی در توقف هرگونه مبادله تجاری و مالی با ایران رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77952" target="_blank">📅 16:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PWEPKkAfMO-lTI5mG6mSXggE9lWAvMZeyPjVMU-_TdS1Y5NXoY4Xe5X4dcjrLX0A67k0jX1CY9Z2mGu1ktw_bolACd7L1r6b2gxnp8GiCGM8F-DDcJTE_wzPKoowKW42Z9VH49jYTG0FGwflD9Iap4aY6s3768dsBYuhYXsDUuZ-frSh29-2k3hWlVHyCwGwZnDCHieETM9BKqPQ6H4Xzwcnbj5nJfra0j935qX_qpdSBRdr5EEyL36ESIP5S5KN_0CZOt-U7CCHyzg9w9GIynB45iLTX33y6Icb_VKld0A5IYuohEsWCQ_nt_BTs2xRT6PnjbJoRxPFf5SD7tCTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وای‌نت، نفتالی بنت، نخست‌وزیر پیشین اسرائیل، گفت که در صورت بازگشت به قدرت، معادله بازدارندگی را تغییر خواهد داد و هر حمله حزب‌الله باعث خواهد شد ما ایران را هدف قرار دهیم.
نفتالی بنت همچنین وعده داد قطر را «کشور دشمن» اعلام کند.
نخست‌وزیر پیشین اسرائیل ادامه داد: «ترکیه و قطر را از غزه خارج خواهیم کرد و به جای آن‌ها مصر را وارد می‌کنیم و در عین حال آزادی عمل اسرائیل در غزه را حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77951" target="_blank">📅 16:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b4d-WlnnGix2k5rg-4tc_4uAWitTu-0zqD94FAcxJqhtV8a_qoE1pvssSncTZefW17KZFjyWN5ZeL1UuWKoHFwK9funPJGqnTMol9DU1jCXMftjEAb_xHmSbYa_HK6jlIT8CoEBZsHFAQ3bN1YU2hY-tblgCdxEiCERakFhnO_nSIp3E6nugzNspkvad7IN-maG8cIGWAtSQpllSWAIdkwkQ5bxw6rN8O0Hg9RkBiXRflBX7JzhrHU1IFwyVe7LsQnK-pM541ldXjyKaC-LqQrhkiLAUI73MPgQHdyb3qkeViwWQKnAu8RZUQOBEIcl-drF3zeXlWXFqiccwfBpQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح جمهوری اسلامی ایران بار دیگر به کشورهای حاشیه جنوبی خلیج فارس نسبت به «هرگونه کمک» به ارتش آمریکا هشدار داد.
در پیامی که روز چهارشنبه ۲۸ مرداد به‌نقل از علی عبداللهی در رسانه‌های ایران منتشر شد، رئیس ستاد کل نیروهای مسلح ایران به کشورهای حاشیه جنوبی خلیج فارس گفته است که «چیزی از چشم ما پنهان نمی‌ماند» و افزوده «این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.»
فرمانده قرارگاه خاتم‌الانبیاء در هشدار خود توضیح بیشتری در این باره نداد. شب گذشته امارات متحده عربی اعلام کرد تمام مبادلات مالی و تجاری با ایران را تا اطلاع ثانوی متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/77950" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IA7NdRhoL4BsHTKnHoXHJva3Ah10DUHyWkLE7TIyYar3phy8hBQ0SiZWCmZiheawATM54fSB2tzVNyuwNjzWov2kXJ-AvXKhNz6Okp6FF7DrVt-vp5Kr3PbxTbppSk3z1PpZFurMer4r-5mMvXeutAK96HtPnCXomEihdBtCczJVTi3NBMZHk2G5N-dkZkPWNs15doEkfXRhFFrCd9oOr_S_bhzRo1P0xOmaR0A4aAVGsWVkld-jSaJwfbQEnPHlOi48uLMT84tocaL8rIVIJ693IjmLDKkC0oV6XOaOgRwebblfmmGgIM_Pv_c370QYfJSKqMzsgbf_5X2dxgbY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، صبح چهارشنبه گزارش داد نفتکش اماراتی که در کریدور شمالی تنگه هرمز توقیف شده بود، مسیر خود را تغییر داده و به‌سمت بندرعباس در حرکت است. بر اساس این گزارش، مقصد اولیه این نفتکش بندر جبل‌علی در امارات بود، اما پس از توقیف، مسیر آن به‌سمت آب‌های ایران تغییر کرده است.
فارس نام این نفتکش، شرکت مالک، پرچم کشتی، محموله و دلیل رسمی توقیف را اعلام نکرده است؛ موضوعی که ابهام‌ها درباره ماهیت این اقدام را افزایش می‌دهد. گزارش‌های بازنشرشده از خبرگزاری فارس نیز می‌گویند این نفتکش هنگام عبور از تنگه هرمز و در محدوده کریدور تعیین‌شده از سوی ایران متوقف شده بود.
این خبر یک روز پس از آن منتشر می‌شود که امارات متحده عربی، ایران را به شلیک دو موشک به این کشور متهم کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/77949" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TVaI1NV_J-GDmodlBXi9HWtkOAFeksCMZSo-vItCsLvwWIzQw-F83cNfPkNwAPFtwk2B_1Jch6v2UVv6KdPn4p41KuRL3mtfgJcYASstJD-EVgv6EqnMHnVsMYue0-m3kg__a4zPKCKJZ9vGbhqPZ6qBp3gyEQ0u989ZhiJ34OyE5DYiJX9PBOkEBLsoIkrSwYncjq6SN_eDzlx5hZ7iHezT_3yj158JVCgLuJYOoS26TudXkysi1t2ArcjFpJl2Cf8JO0ycbkEwUkOZ4ouosAPC5yq0xVrHEsDlYZswNUDZ8dV6RUM5LFaOftI6mKxkFeSwphnevQwjD-haijooIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب مشروطه ایران (لیبرال دموکرات) اعلام کرد فؤاد پاشایی، دبیرکل این حزب، هدف «سوءقصد» قرار گرفته و در بخش مراقبت‌های ویژه بستری شده است.
بر اساس بیانیه این حزب، این حادثه ساعت ۷:۴۵ عصر ۱۷ اوت (۲۶ مرداد) به وقت لس‌آنجلس رخ داده است.
حزب مشروطه ایران همچنین می‌گوید پلیس لس‌آنجلس در حال تحقیق دربارهٔ این حادثه است و اطلاعات تکمیلی و «تأییدشده» دربارهٔ این حادثه بعداً از سوی حزب منتشر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77948" target="_blank">📅 16:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=UvdVr2rWsnYFaaZkl5vV11REwB78ch5xNi1omMU6okVgeeS01toqZ33zdnIestoGPN8tc79AqPPfmkxlCaD_-u3hQJT32ssUZvA0UMeJqX2-yYXgqNGDPjNhJcsD0RsEwk0zs0ntVyLapQUEV2hEHAtAZPU9atyijbzk4XP6mceB0MzKlp6FqyYlH_tSFn42I2w1U1G5QQEAOk2XRteFCVN88l2J9d3F6RHHvNU-E37XodsGg-3Uw5C5r-SIL0HWxq9lw-4IPpDFsCSsUpflhG5EmJIqkrrkyNyEjVxFzs14ydA6m23BhR_hHzonhBjjVm1iSLOx8gwMoOiTQkgG9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=UvdVr2rWsnYFaaZkl5vV11REwB78ch5xNi1omMU6okVgeeS01toqZ33zdnIestoGPN8tc79AqPPfmkxlCaD_-u3hQJT32ssUZvA0UMeJqX2-yYXgqNGDPjNhJcsD0RsEwk0zs0ntVyLapQUEV2hEHAtAZPU9atyijbzk4XP6mceB0MzKlp6FqyYlH_tSFn42I2w1U1G5QQEAOk2XRteFCVN88l2J9d3F6RHHvNU-E37XodsGg-3Uw5C5r-SIL0HWxq9lw-4IPpDFsCSsUpflhG5EmJIqkrrkyNyEjVxFzs14ydA6m23BhR_hHzonhBjjVm1iSLOx8gwMoOiTQkgG9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیوا سیفی‌زاده، خواننده ایرانی که در جریان تک‌خوانی در «عمارت روبرو» در اسفند ۱۴۰۳ بازداشت شد، روز چهارشنبه ۲۸ مرداد با انتشار ویدئویی اعلام کرد که دادگاه او را به اتهام «تشویق به فساد و فحشا» به چهار سال حبس تعزیری محکوم کرده است.
خانم سیفی‌زاده در این ویدئو به رای بدوی دادگاه اعتراض کرده و می‌گوید: خواندن شعر سعدی و آواز ایرانی چطور می‌تواند مصداق «تشویق به فساد و فحشا» باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/77947" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/meHNHqYnWIIFKB2YttHUz7b7xCg4XF3jVFuI8_NXac5NR0Xq04O2nuWH4XaMBa93ae0vhtqga5u3c-cCjtMfonlknQDssPHr7Q-BNw1V2LyhyVEYs0W8xZzlY7bLsn8aPIR24T1mwttGbrZ2Rt6THnmWKR_oFGWEfwzl-St2v7WKAk2Jnq8MV0NHWzYCTuBzjHbLcd2-dKvBkZsoPTc2MebsIk5yQ-GxireiPuvGWVmmna7ihR5c7US0oIVUooPg6C-NT5TK3lb2P-ZNXE82Tiun1yMMqM8PIX53HIc8rW8BAtRSKSJdhGv8KlfxEpt_9K1LP8tTNHdtv_Sc-3jLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرانا: آرمین نورانی، خواننده موسیقی سبک رپ که با نام «خجسته» شناخته می‌شود، بازداشت و پس از مدتی با اخذ تعهد آزاد شد.
در پی بازداشت این خواننده، ویدئویی از اعترافات اجباری وی منتشر شده است.
در این ویدئو که مشخص نیست تحت چه شرایطی ضبط شده، آقای نورانی نسبت به شماری از اظهارات و مواضع پیشین خود در ارتباط با اعتراضات و حمایت از معترضان ابراز پشیمانی می‌کند.
لازم به یادآوری است علاوه بر نقض کرامت انسانی که در سایه ضبط و پخش اعترافات اجباری صورت می گیرد، اساسا تا زمانی که فردی در محکمه محکومیت نهایی دریافت نکند، از منظر قانون بی‌گناه محسوب می شود و هرگونه اعمال مجازاتی پیش از محکومیت نقض حقوق شهروندی و انسانی او محسوب می شود.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77946" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NeYvW2Zn-hNXPsFypvqa2EixsAvGh4nhs04VC9Qv3lckPyDwWRUQ6HOea0AtdCmZqIfujabq3IDOEBcOFNETZGabIdMb1duXP0bTW2gIq8a3OhjB7pNIO5uKRMkPbkg05p65c0W3mUUlsvsvhVOEcXE1d_7yj_2HjBrtOsqMh6Pf3d9bbXfp5Zd9iqt4uJ_QyLVGr3EwILWfQiaHbWR068k8d9hTA6LPFEKZwIjHwYowvRAwIMLl5nEq30xJMCOYRR-AE6INhpdPd1fSUkCQOWDC6S2ATgvFu9RsTQ7TN8ru5Yd8P7i6PrAwP4WwnqrldENlHzL0K85kmUJmfpVPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OGxeJPnmhJoLHLQVeV8oSxuYhBxIHWiikksaYLHClOCli0VAEWbMV9hr-UO3HIFLP2MMKyqrbAFe_Ff8Y7jmmc82JL4cTYwaN5SmC4lKNKiDqYoXPXMvuz-1vEMfR_AVDwGLaUMvo8gQBL0FQB8SWg9OeLFULVR4mGL3JeJ6RVBYJZNzDbmoQcLjDhT9d-mS4n6VF6Pm1pk3yEzOsZ9EyX30dndsj32nxMKt739uBlMdp2BfAUv3h4zUCczm6_h_KSCrhpMtHiYmZyr9JBU4o8hz0viPO5oueK7Cfhrqody3YCtj7rwOJOz_NfBvqfcGEWNY2eMrZP2bAtQji_ZbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QTojIrv_rH9XlShKzSwrdcRLShY1Tp1xBqhPY7cPvabH8zG8S508wWGqAl3uGYOfQGogJ26FEokOR5nknBWWye5MEY1b6ABClVFIHEgnBZ0_tLnxxl5Kmyp2YNqIhglYQHyhHuMWI7TPEOqkJY5N8K5T48XvM5nrV-ImLa7mKsBIPMtHEP-1nz4LwQqVd8Zdn_71khkFUnIuDv2paWoX3d7ZHYSznlZuuI0nOdG2EV28BpEt7T5ydIdVW6Q3YMQsRadngmY6STriWHsnn2gL3NSsgxz5glsh40yqvDXnF6NXZqL-g4k3WJWkM-E4cbAa0GgBJg5ZMEDknMChtwomZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uijdj5AqC4wbrp08z9Mgz6PtwzUU1QVkLpI4a9oVDTcOeieZ_XrguJh_BYCwVPLDCo1lfXV2uFjpvJUTjH5exvCcxH370gmljCWVxsNUGu8Iz6Mcqkcvsn4BdQrcrgkelUo78CGWUSqm8oo9IRlKZFl8-OLuWhuDq8eh19CdVY2cKT7xBWahy0E2rDef5HJkbjv3W_eTNr-4RjJniRpc0jh94Sd5-BvvKGOOznyD4r-Mip781YQ7_Rmx4AI1RnwifLGiskPyvLuWFX3P9R-adu_dp0X5fMuV28gqJV91bt46bsE4kOfyLcAbc7RhrqQ1Gdd2vBieWUw7CvmWj3iJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FermF3oiOOc7Squ6seX48ixPxl4yfZm73Gv1GReTsPpD-7YIHFNktDshHQEN-I52DhLY1hjcxhN9meICVAun4h9dQg3dy_bb3LYQKyKpK1nC_CB7Jq6ZfjYtGuqlD8A-NylIAxb1eK4DIAH4VhMjgWme2TqtlY3kvGlPxkR6fo9OMgroG9Vw0kQG8aRb3pu_Akmh-6y0e0cnYvyl1q3cHYXW3oDGYa5-5YZc0Pl5Uz6OYRHvLwM4jnLLUBgmXffj5vBjgvjGCJ5UQ0YLC-6qYbAXylQs8dWtIGRgM_KgCjNgkQGKIE4KWiuqWpLdhP_PojMHuwk6vybndEkHgtWKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u00Z9VJ80jiSRXTDpQPVATg15LWE-_UjC7hOaWwq15Ork8K2db8RS6fRKCWOwtS08Y6Cy-XuZIYeKfxVz38RZeOq4qhiAu3aVd8RqOEYszA27Iu3khgv7UeQwgpBIe56vB7OKmAPn4cX6Q_Y0O_pyO9B6L-sRhGNjE4nrDxxYkTItiacNAgyFzKM-aJr9Zs7eSBeKotDpaTaA8trOaTRy3GRKm3U_EjoA0Lnnjpp9YhHVZ0cGO_VYlSVHV0Vr0MEctlbM2pnn5Wegvru3TJgbFFGeh8uvbFnKNjILBZOLUetZbTVB3Dk6hsKQ5CVdhwiwHNPcF0HCBk8xi2qf_aJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQ5WTQ0iUzT3QG9l3HDHHVREKmqDZFNf8SipHXw4-NYdi-R5Kdumv55sNKvXccIosgUur_XYM2mipY7ZIe7IuLRvg2PyNd38d8wRj7xqgHvbdjXd9j9JmLg5xC_cJ69lAuHjLvqEJIAf7OzJDw3-D7ImEZri58zCsgMkc7dharWXP-WNuYu6jNXJ3R9sDGAFGOru8wfDy1M3GzJQzK1HfvJWkCxnEPWVECNJJt6csgNU3NwsicIN_B0FjyWyq8yRRxhiAkh-vgfNg9xTM81o2P2ymfU9rrdbw9rZ4WHqvPu5MmweUxRpRDygG4DOxhly7Pso2AzivmD30sAA2WW37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D0hSRGHTBqYWZpGIvR3SeFWtrRl_OjJg_XzQTEz5eX7q3INsEjxbgc3fGo-W4v9fTEVnrfBbQrksLm_SBDzbwvIAetIw2utYOWBMXbW9AbCYk4nu8pWPR949ZgWmPL6FE5r6HI9_ayz_mOLBfYENthXSagAHKf58LVfpwi4xg4P4nIPH2isWaLd5cKd_SW6V3x-XvZ8_cR0W0Y_O1ydnjM2WbbNyFFnEKwu-isEE16ORPWLShCVRAp6yyAIDqVlZ7X0818GrurxiJL1k-T1XqSEYMYcQqpcKfMu2W7f_RcYR78jlqZtxxMGkMKee6hG7Va9viFEQ7BnHUgLhEH6laA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه ۲۷ مرداد در پستی در شبکه اجتماعی خود، تروث سوشال، بار دیگر تنگۀ هرمز را «قلمرو ایالات متحده» خواند.
دونالد ترامپ با انتشار پست تازه‌ای در «تروث سوشال»، یک تصویر گرافیکی را به نمایش گذاشته که در آن، تنگۀ هرمز، به‌عنوان «قلمروی تازۀ» ایالات متحده نشانه‌گذاری شده‌است.
او پیشتر هم در یک سخنرانی با لحنی نیمه‌شوخی و نیمه‌جدی، این آبراه را به‌عنوان بخشی از قلمروی ایالات متحده معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77936" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lYkcJWummA2oVWEWape6M0IFPs8UcBepGxFyT0NYkUjRnt3M14L1jFb3cUB3plWPN83LICfWcTtrZh_J7wo1-SgQmP8w7b72MG8cUp8PSSbh6bgEVwcelCItUntOZl9bNvpa5YdDG7RplEBMgfHHK0mhMkuAdM_v9kmaKG5kHfSjAbVjdOa6-YbbNipCCtI_hLsF4TetpCGSEMtCsGCT06t_Ot1hQ2FAOntAR4d1d52iJdATs32Dxw9M6JIVzNosdZD2Kia2od83NZ9B5_14uRfpmSvpk1jOVdrgaCnFlAN1jDdq5uIvGQYQJI0cYqMUWCfQ1u7aHL4Db1BY_iVIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر درخواست جمهوری اسلامی ایران برای ورود کمیته بین‌المللی صلیب سرخ به موضوع خلبانان ایرانی را «ترفند رسانه‌ای» خواند و گفت ایران هنوز به دعوت این کشور برای بررسی موضوع پاسخ نداده است.
ماجد الانصاری روز سه‌شنبه ۲۷ مرداد گفت «دعوت دوحه از هیئت ایرانی برای سفر به قطر و بررسی این پرونده همچنان پابرجاست، اما تهران هنوز به دعوت دوحه برای اعزام هیئتی به قطر پاسخ نداده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77935" target="_blank">📅 16:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=aKomu4YhMXyE_hDSLbxGypyiHrwdFUFOjrjSqMudwvVRcc8INNj1BOtOxW2t1MTVnChWbL7P2Zwmb_oOT8LIe90DBXyJCr-Z5MDWH1v8tZLNtcoIRRiuS66xvUUghsXqJ7OfB9M_YP3nRJUK2di1jBXFFPYgIF6-FpDwa-sFmHsttTTE0p5sQwOG2k0uNfV_Ul7MqullAW5Uu6B-yh8nOg7Wt0KA9sMaKP3jbFWN3ijS8696NSS1kihzqi7nimZv7AzvWDyUJ8AuQWmBsBbPRD4qu1w8gvYWES9JjlHlF7YD7KzBpa-o44kJaNUO70k5E7alJTLzkN8cXljpG9xbjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=aKomu4YhMXyE_hDSLbxGypyiHrwdFUFOjrjSqMudwvVRcc8INNj1BOtOxW2t1MTVnChWbL7P2Zwmb_oOT8LIe90DBXyJCr-Z5MDWH1v8tZLNtcoIRRiuS66xvUUghsXqJ7OfB9M_YP3nRJUK2di1jBXFFPYgIF6-FpDwa-sFmHsttTTE0p5sQwOG2k0uNfV_Ul7MqullAW5Uu6B-yh8nOg7Wt0KA9sMaKP3jbFWN3ijS8696NSS1kihzqi7nimZv7AzvWDyUJ8AuQWmBsBbPRD4qu1w8gvYWES9JjlHlF7YD7KzBpa-o44kJaNUO70k5E7alJTLzkN8cXljpG9xbjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی و مذاکره‌کننده اصلی با ایالات متحده می‌گوید تهران تا قبل از رفع محاصرهٔ بنادر ایران توسط آمریکا و انجام برخی شروط دیگر، تنگهٔ هرمز را بازگشایی نخواهد کرد.
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس، دیگر شروط ایران برای بازگشایی تنگهٔ هرمز را «آزادی اموال بلوکه‌شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه‌ها و دیگر شروط» تفاهم‌نامهٔ اسلام‌آباد دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77934" target="_blank">📅 16:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aL1210jcHL2ALI3JRQXtBGdHSBIGeW0bP0dcrfdoyp1Cs9hTiH0JdPjE_XniEMjuuw7Ns9aLbkJrtbiGVvOpW9RiLM69A1CrnodVdArf9eR1BtE-JHYld3N3KTs4lF1o7MfYo58YruhSdW5Wq-_HM3ABGSEbOn7m1I3PQUtNuioaQIB_9UB7rSYPC72afCR8Oved_hpxsZ6Q0QzCh-R1KzA3jNYOzIG4DCDxTNcPd38a0YR0s9ZXtfJwh6r9upHOSIXOQuQILadqOjQT_APRh7gtjsS_p85CkSjOd4TpDD7Pfqlv5HZ5tucieo8YgIDIYHgmeZC4mVOn2nUjcyggbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آنکه دونالد ترامپ کانال ارتباط پشت پرده آمریکا و سپاه پاسداران را تایید و دولت ایران و سپاه آن را تکذیب کردند، شبکه العربیه به نقل از منابع آگاه جزئیات جدیدی را از تلاش‌های نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، برای برقراری تماس بین آمریکا و سپاه گزارش کرده است.
العربیه به نقل از منابع نزدیک به ریاست اقلیم کردستان عراق گزارش کرده است که آقای بارزانی در تلاش برای کاهش تنش میان تهران و واشنگتن، دیدارهایی با مقام‌های باندپایه ایران و آمریکا داشته است، از جمله دو دیدار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران.
به گفته منابع العربیه، آقای بارزانی میانجی‌گری میان ایران و آمریکا را از اوایل ماه مارس، یعنی چند روز پس از شروع حملات آمریکا و اسرائیل به ایران شروع کرده بود.
دلشاد شهاب، سخنگوی ریاست اقلیم کردستان عراق، دیروز در پاسخ به پرسش بی‌بی‌سی‌ فارسی، تماس‌ بین آمریکا و سپاه از طریق آقای بارزانی را تایید کرد:
«این خبر از یک جای قابل اعتماد منتشر شده و نام برخی افراد به عنوان منبع در این گزارش مطرح شده، ما هم همین اطلاعات و جزئیات را داریم، همه آنها صحت دارد و ما هم تایید می‌کنیم. من فعلا اطلاعات بیشتری جز آنچه منتشر شده نمی‌توانم بدهم.»
خبر این تماس‌ها نخست در وبسایت اکسیوس گزارش شده بود.
سایت خبری اکسیوس به نقل از منابع آگاه گزارش داده بود که آمریکا حدود یک ماه پیش از امضای تفاهم‌نامه با ایران، با میانجی‌گری نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، با سپاه پاسداران تماس برقرار کرده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران دیرور به خبرنگاران گفت: «خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.»
حسین محبی، سخنگوی سپاه، هم در واکنش به اظهارات دونالد ترامپ که وجود کانال ارتباطی پشت پرده میان آمریکا و سپاه پاسداران را تایید کرده بود گفت: «این دروغ ترامپ، صرفاً فانتزی‌هایی است که به خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/77933" target="_blank">📅 16:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=pK_jEEgzyhhOebvY7O_EtbDR86Nvvs0W7ArHnGJWMMlX8R6PaaGu9qc5XQTiM1LsTz8QJ7ULs8aFLNouPjhGrijJ30Ale-qreNpBGYC0_r5TZd-QG2OF7C0LzLKPqFZMEM0JZTwY2-OKWY593hcd16isFrRcd3pYhjqayynk0m6ct-fCavXa0M1OLGcZYd2lY5Ba8Q8g0UStoR-z_NGwTITFlpWAYBwMHgkfSZVq3ON3TqLg0PGuKP6uhzWunsdiGOJ_5w9EiCfSBS7Fr9lHtQ50W4yDdeHc-os3u4ojwwfwVFyP2OfaKRvUpqvBbx6wc52xH6LmClqr3Zl9RN1eeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=pK_jEEgzyhhOebvY7O_EtbDR86Nvvs0W7ArHnGJWMMlX8R6PaaGu9qc5XQTiM1LsTz8QJ7ULs8aFLNouPjhGrijJ30Ale-qreNpBGYC0_r5TZd-QG2OF7C0LzLKPqFZMEM0JZTwY2-OKWY593hcd16isFrRcd3pYhjqayynk0m6ct-fCavXa0M1OLGcZYd2lY5Ba8Q8g0UStoR-z_NGwTITFlpWAYBwMHgkfSZVq3ON3TqLg0PGuKP6uhzWunsdiGOJ_5w9EiCfSBS7Fr9lHtQ50W4yDdeHc-os3u4ojwwfwVFyP2OfaKRvUpqvBbx6wc52xH6LmClqr3Zl9RN1eeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید که افزایش قیمت بنزین توسط دولت مسعود پزشکیان «تدبیری حساب‌شده نیست»، چرا که به ادعای او، «دشمن» برای این مسئله «برنامه‌ریزی کرده است».
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس ادعا کرد که «بر اساس اطلاعات پیدا و پنهان، دشمن مترصد ایجاد آشوب و ترکیب آن با عملیات‌های نظامی مانند ترور و اقدامات تجزیه‌طلبانه است».
او بدون ارائه راه‌حلی تأکید کرد که مشکل کمبود بنزین باید با برنامه‌ریزی جامع و بسیار هوشمند حل شود، به‌گونه‌ای که «بیشترین عدالت وکمترین نارضایتی را در مردم ایجاد کند».
مسعود پزشکیان، رئیس‌جمهور ایران، روز ۲۵ مرداد با اذعان به تأثیر محاصره دریایی آمریکا علیه بنادر ایران گفته بود که راه ورود کالا به ایران بسته شده و دولت منابع لازم برای واردات بنزین را در اختیار ندارد.
بر اساس آخرین آماری که دولت ایران منتشر کرده، تولید روزانه سوخت در کشور بالغ بر ۱۱۵ میلیون لیتر است، در حالی که مصرف آن به ۱۲۹ میلیون لیتر رسیده است که نشان‌دهندۀ ۱۴ میلیون لیتر کسری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77932" target="_blank">📅 16:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZnpJfkXlb1eMfuys173_w-aikOw3PBN9fQirTdtvqBYReuGATHjOm1ff21b2Z1iIJI6dLE_0gxfNW889psX6zXcU2ETTVqKOcfuuHsHOUw4l0_K4Ot3MGAO87YEBP3xoeSrkJ5--_AKs8dBufApExkS1hmH9GYGDaQOP74Si_eY1NEQrcCHi4_ui3Bsfo7Op2CMBIIK7WA40X7iGhmCUIP-K0OpDq2Yp_VEairyZsPitD4Ygr4MfEtOjNCt1AjRL67mtVc7WrxjgqogMM12kg9zTB9x1bMwm4XzpzXXRCF7zfNGkcCoYLiLO3R88kiyLkR6vXmpUH_yTaampa8wtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع مطلع به ایران اینترنشنال گفت که محسن (مهرداد) تکش، شهروند ۳۳ ساله در اصفهان در رابطه با اعتراض‌های دی‌ماه سال گذشته با اتهام محاربه به دو بار اعدام محکوم شده است.
تکش، ساکن دیزیچه اصفهان، در جریان سرکوب اعتراض‌ها در هفته آخر دی‌ماه بازداشت شد.
منبع مطلع گفت که او در دوران بازداشت به‌شدت شکنجه شده و دستش بر اثر شکنجه شکسته است.
به گفته این منبع، تکش تحت فشار و شکنجه ناچار شده اتهاماتی را که بازجویان به او نسبت داده‌اند بپذیرد و همین اعترافات اجباری، مبنای تشکیل پرونده و صدور حکم علیه او قرار گرفته است.
خانواده تکش تا حدود چهار ماه پس از بازداشت، از محل نگهداری و وضعیت او اطلاع دقیقی نداشتند. او پس از چهار ماه بی‌خبری، از بند الف‌ط زندان دستگرد اصفهان با خانواده‌اش تماس گرفت.
منبع مطلع به ایران اینترنشنال گفت به‌جز اعترافاتی که تحت فشار و شکنجه از تکش گرفته شده، هیچ سند یا مدرک دیگری برای اثبات اتهامات مطرح‌شده علیه او در پرونده وجود ندارد.
محسن تکش پیش از بازداشت، در دیزیچه یک تعمیرگاه مکانیکی موتورسیکلت داشت و از این راه امرار معاش می‌کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77931" target="_blank">📅 16:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KrgabqUZ1AWrJcsklGy5zMP11n3Pugfv9b65lWGfvyTvKoagqmw2oxa_PxZTCmBZ-wCIaZRI3SdzeHgmE1liW4HHvnOa9d66OWvGwxrvAyV07hvStn9FjfsAQWuhLLwiUUL7eGxu3tn1JuBePbwjddsiYuk0No0FPXQtgXe-M0PED36uFnpQUJ2a2fRBU7zIMRLycVZN4z8d7KLz2NXgHMfLjXiYMt71AtBbOx85ueUTkxxVwC0T6rB8aKQ1xSVL92PXtlTntALNskDmjsUg7_gzDih_e3BxdCAMKWs1y-4GQQ1FWrcze-4B_GNve2GysVks5uNH8Yrc04i1LeRcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت گزارش داده که یک شناور هنگام عبور به سمت خارج از تنگه هرمز، با پرتابه‌ای ناشناس مورد اصابت قرار گرفته است.
این برخورد به موتورخانه آسیب وارد کرده و باعث مصدومیت یکی از خدمه شده است.
در حال حاضر، گارد ساحلی عمان در حال کمک‌رسانی به سایر خدمه است.
تاکنون هیچ پیامد زیست‌محیطی گزارش نشده است.
مقام‌ها در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77930" target="_blank">📅 07:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QypSg5d0JX0D603h2DjPblExfvmprhAI9RT56tHCpXmtgq6iiUccbvYY2BXT-WsnG-Z1DBoDyZVAJe9c3FX-Mm6Z1_cjc_mUw_9-OJ2c7XbC88xZNKO4VTQqauNyQpjqlyJfhofiZv5cx7xQ995mc_FNmj_Z0tuE93xwc5l22--NTbA9vwy1nJY3LeCKcK06FC0uYDoo6pYFoWetT6SAv_2v9PPRDQweGs0n5CJkNGFL7-cPrt1sc01Bvoq1PZ1RbqhB26wUdPS4IFmyKGAre-6soLSqSHgkcvIlRzXeLVLAtd8bcOcQi0FXxzRTOgJ_w0GOrUWc9n854xi2OjNlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه فدرال کانادا در حکم نهایی خود درخواست سلمان سامانی، معاون و سخنگوی پیشین وزارت کشور جمهوری اسلامی در زمان سرکوب اعتراضات سراسری آبان ۱۳۹۸، برای توقف روند اخراجش از این کشور را رد کرد. بر این اساس، اداره مرزبانی کانادا موظف است حکم اخراج او را اجرا کند.
سامانی پس از استعفا از سمت خود با ویزای توریستی وارد کانادا شده بود. این در حالی است که بر اساس قوانین کانادا، مقام‌های ارشد حکومت‌های ناقض حقوق بشر حق حضور در این کشور را ندارند.
سامانی در درخواست خود مدعی شده بود در صورت بازگشت به ایران با «خطر شکنجه، اعدام یا خودکشی» روبه‌رو خواهد شد.
بر اساس حکم دادگاه، قاضی این ادعا را رد و اعلام کرد سامانی در مصاحبه‌های خود از عملکرد وزارت کشور در آبان ۱۳۹۸ دفاع کرده و هیچ مدرکی وجود ندارد که نشان دهد حکومت ایران او را «خائن» می‌داند.
قاضی همچنین تاکید کرد منافع عمومی کانادا در جلوگیری از تبدیل شدن این کشور به «پناهگاه امن سرکوبگران»، بر ادعاهای سامانی ارجحیت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77929" target="_blank">📅 07:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVDwSB59Ee0rW9fKQQHia0Wde0QAG9x4A46Z7F0xSRpXm9G5r27vCBlO6lssE7qrmnsN-_3-GJKOyu4-uNbiEbMLPbMrM2XKAJyNnq3BBrAr7dZ_GhJQixTrclQnTsDSR509mL8QCaVoWMmMUCVAhZ_eZA7mWkbQi1nbjNTBzO1B8YwIaQwGL3AV7OQWtSgiPS7tWvyz97R1aDE1PrI-gF4gCqBykYHJ81cYZcayb2Tmrdwf90yo94h-mT0A1_vYJOkisk0Of5-b5nGlwFLnV5ZjdRyusvdBQ8ix7JXecoPieJJsku3eLopgn19b9qyuJ8SVau_wERxhYPjmGXanAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، در گفتگو با دونالد ترامپ، رئیس‌جمهوری آمریکا گفت که ادامه گفتگوها با ایران برای بهره‌گیری از دیپلماسی حائز اهمیت است و ترکیه آماده مشارکت در این زمینه است.
دفتر ریاست‌جمهوری ترکیه اعلام کرد که در این گفتگوی تلفنی رجب طیب اردوغان، آمادگی آنکارا را برای حمایت از تلاش‌های صلح ابراز کرد.
پیش از این جرد کوشنر، فرستاده دونالد ترامپ، رئیس جمهور آمریکا، گفته بود که گفت‌وگوهای ایران و آمریکا جدی و فشرده است، اما دو طرف هنوز به تفاهم نرسیده‌اند.
آقای کوشنر که داماد دونالد ترامپ هم هست، به فاکس نیوز گفت که مذاکرات آمریکا و نهادهای مختلف حکومت ایران احتمالاً قوی‌تر از همیشه است، اما دو طرف هنوز به نتیجه نهایی نرسیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77928" target="_blank">📅 07:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=G5y-BvjTzjuXaVyroIMgvv1Lmug2ZUp502J8XKCwLtb8fng8-16cJf6tow0JkLcUm_b2GEIqjsgSIGQ1r5SlUarIkHtIPmCt23m3jJITHU1bZW6Aw13zNADV5zax8SsWwVx-_IdfZ_whwbhmEAQkYjlqAv4Lbzd5r5A5eDuiCyDDvC2g6HaGNzq_dXTdDn-9Ajorszev-o4BOcQSou-mthOAG2mpmswqLI6rCEzo3A3c46e3W3OYidwk2OJf3IddMK_FkE-QTbpE63NAclYu2XxDF6Bh336KfSlwon6zFW5v0QxhPwQ8lxrTQN7viwNRwJnYSIP1qvwAvzOASDm5ajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=G5y-BvjTzjuXaVyroIMgvv1Lmug2ZUp502J8XKCwLtb8fng8-16cJf6tow0JkLcUm_b2GEIqjsgSIGQ1r5SlUarIkHtIPmCt23m3jJITHU1bZW6Aw13zNADV5zax8SsWwVx-_IdfZ_whwbhmEAQkYjlqAv4Lbzd5r5A5eDuiCyDDvC2g6HaGNzq_dXTdDn-9Ajorszev-o4BOcQSou-mthOAG2mpmswqLI6rCEzo3A3c46e3W3OYidwk2OJf3IddMK_FkE-QTbpE63NAclYu2XxDF6Bh336KfSlwon6zFW5v0QxhPwQ8lxrTQN7viwNRwJnYSIP1qvwAvzOASDm5ajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان ترامپ، بخش‌هایی مرتبط با ایران،
ترجمه ماشین:
🔻
خبرنگار:
درباره ایران، امروز صبح گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، حسابی عمان را بمباران خواهید کرد. آیا می‌شود گفت صبرتان در برابر عمان، این شریک راهبردی، تمام شده؟
🔺
ترامپ:
نه، فکر نمی‌کنم خیلی خوب رفتار کرده باشند، اما خیلی راحت با آن‌ها برخورد می‌کنیم، مثل کارهای دیگر.
🔺
ترامپ:
وقتی اخیراً با رئیس‌جمهور کره جنوبی تماس گرفتم، که از او خوشم می‌آید و واقعاً فکر می‌کنم آدم خیلی خوبی است، به او گفتم: «مایلید کمی به ما کمک کنید؟ ما برای ایران به کمک نیاز نداریم، اما اگر مایلید، درباره ایران دستی به ما برسانید.»
گفت: «نه، ممنون.»
من گفتم: «یک لحظه؛ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ‌اون، همسایه کناری‌تان، محافظت می‌کنند و شما نمی‌خواهید در یک عملیات نظامی خیلی آسان در ایران به ما کمک کنید؟ این عجیب است.»
گفتند: «نه، نه، ترجیح می‌دهیم درگیر نشویم.»
من می‌گویم خب، پس چرا ما درگیر کمک به شما هستیم؟ من می‌خواهم به آن‌ها کمک کنم، اما وقتی از کسی می‌پرسید «مایلید کمی به ما کمک کنید؟» و می‌گوید «نه، ممنون»، بعد ما داریم در برابر یک کشور از آن‌ها حفاظت می‌کنیم و خودمان میلیاردها دلار می‌پردازیم؛ این کار برای ما میلیاردها و میلیاردها دلار هزینه دارد.
نه فقط برای آن‌ها، بلکه برای کشورهای دیگر.
به ناتو نگاه کنید. ما صدها میلیارد دلار هزینه می‌کنیم تا از اروپا در برابر روسیه محافظت کنیم؛ صدها میلیارد، عمدتاً در برابر روسیه، اما در برابر چیزهای دیگر هم.
بعد می‌گویند نمی‌خواهند وارد موضوع حفاظت از تنگه شوند؛ همان‌جایی که بیشتر نفتشان را از آن می‌گیرند. آن‌ها ۵۰ درصد نفتشان را از آنجا می‌گیرند و نمی‌خواهند درگیر شوند. پس چرا ما این کار را می‌کنیم؟
تمام چیزی که می‌خواهم انصاف است.
🔻
خبرنگار:
با منقضی شدن تفاهم‌نامه، آیا امروز به رسیدن به یک توافق نهایی برای پایان دادن به برنامه هسته‌ای ایران نزدیک‌تر شده‌اید؟
🔺
ترامپ:
خب، آن‌ها می‌خواهند توافق کنند، اما قرار نیست آن نوع توافقی را که من ضروری می‌دانم انجام دهند.
ببینید، ما فقط به یک دلیل آنجا هستیم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. متوجه هستید؟ ایران نمی‌تواند سلاح هسته‌ای داشته باشد و سلاح هسته‌ای هم نخواهد داشت.
و همین حالا، اینکه آن‌ها بعد از کاری که قبلاً با بمب‌افکن‌های B-2 انجام دادیم یکی بسازند، قرار است... قرار است خیلی طول بکشد [نامفهوم].
اما ایران نمی‌تواند داشته باشد؛ خیلی ساده است. آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔻
خبرنگار:
هفته گذشته گفتید که به‌زودی تنگه هرمز را قلمرو ایالات متحده اعلام خواهید کرد. می‌توانید بیشتر توضیح دهید؟
🔺
ترامپ:
خب، به نظرم ایده خیلی خوبی است. بله، منظورم این است که ما آن را کنترل می‌کنیم. با محاصره آن را کنترل می‌کنیم. ما محاصره داریم. با محاصره آن را کنترل می‌کنیم و ایده اعلام کردنش به‌عنوان یک قلمرو را می‌پسندم.
ما کنترل کامل تنگه را در اختیار داریم. حالا آن‌ها می‌توانند دردسر درست کنند. می‌توانند در آب مین بگذارند و مردم خوششان نمی‌آید کشتی‌های میلیارددلاری‌شان به مین بخورد و از این قبیل.
اما محاصره بسیار مؤثر بوده و می‌دانید، داریم خارج می‌کنیم؛ حالا شاید این متوقف شود یا شاید حتی بیشتر باز شود، اما ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم. اگر به اعدادی که ثبت می‌کنیم نگاه کنید، داریم این کار را می‌کنیم.
تنگه باز است و قیمت نفت در حال پایین آمدن است و به پایین آمدن ادامه خواهد داد، مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از کاری که الان می‌کنیم انجام دهیم.
ایران در دردسر بزرگی است.
آن‌ها تورم ۳۰۰ درصدی دارند.
کشور به‌هم‌ریخته است و ارتش کاملاً شکست خورده است.
خیلی ممنون از همه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77927" target="_blank">📅 23:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VDiLrNoig1TSAoyY4IJaBFcel6-Yv8-TIJWwMqb5JgDJMbQH66uQNIJmP4vNxWExy_FD57duEqdlcCfvYa26014hQ0wLLpTUHLLocpoHGBqICItOAVKOc42SMNfI6XgVPZHqoAfKfh1-1bfHN9ptk-bl3vmW5IWwLetKcuFoDzk-u1amkMwWnIpqRCYJJBvMQHnNwiOv66pzmC5r7kIuE6hjPoP32gYK_EE26MVyGfZbl7lxlTFs8DwczTISLs2fl_OEta5KzYnXMhOr6XMsGivyOwCbK3sdpmMRwXndKyY5MrKTPr09WpN1OLJF6XgAXuZhXlgjA-f0AgjOJmUNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=hrPFHWyYlqB7FwbnM8_dcs7JMoTeR554EtcMMhxiJbgarvh4uudoAbuSAMaFewgIhxlXEozQvKeJvy2onh6SUNGXSPURkA4nrOjLB93jS2s1c-BBUf101sSNge_iXr4mP--WXvV9l3nLmVc8SbXVxGEMTUtKtHkoV-hkGAwN5rPkx2_YJ2uG0cJ3JKC4O0kL-nA-w-tZ_DkpvDqDdgTiKyeD18y1ZhsuLHYTJgJnycq1VZtSwxkkyIQEKNp3L4Kow5XVUz3RE9c_kjpC2BJhooF6tAHYbV8cwl8wnLzcdAP3zKWcYX5_IM9Avb-kSmwniA2TaMlBivQerviLMLooIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=hrPFHWyYlqB7FwbnM8_dcs7JMoTeR554EtcMMhxiJbgarvh4uudoAbuSAMaFewgIhxlXEozQvKeJvy2onh6SUNGXSPURkA4nrOjLB93jS2s1c-BBUf101sSNge_iXr4mP--WXvV9l3nLmVc8SbXVxGEMTUtKtHkoV-hkGAwN5rPkx2_YJ2uG0cJ3JKC4O0kL-nA-w-tZ_DkpvDqDdgTiKyeD18y1ZhsuLHYTJgJnycq1VZtSwxkkyIQEKNp3L4Kow5XVUz3RE9c_kjpC2BJhooF6tAHYbV8cwl8wnLzcdAP3zKWcYX5_IM9Avb-kSmwniA2TaMlBivQerviLMLooIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: آتش‌سوزی بزرگ در میدان شهرداری گرگان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77922" target="_blank">📅 21:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPE5l3xcdXB-dKKbY08yTeHIz6nvRxcTVozYJtbVHJ-nmhXCL4FkyVylR95X7K565g81Sr3yhXgbOUVA_aD4g_KiB6aJIX7W5WdIJ41PRQ79pF65NsznjW2-KDXme3DKoIyJf0ESgG4shar7WmWMy7s3__yey9YSU1T4HNN1m0ceNWT_sk3HdJNhwWyafGK63v3ETMFzzLmYS41XZA-3QUDUuAkhDZob_jsckEHUNSivuuO39T81AMILIHMrfeAEY72sO-x_RBCMx2jiK4REuA4QyUPgbGjGuNA2ZXuNuB-XxXomcr9Yf3YVAAelBDH6ejEbcQeEIyqQa_fWV6gZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43c261d593.mp4?token=WQXBad2rGGt410sq6vzkNZRPQzZPLkCd5FdEPgu1WFymEyGqg2SzPlUr1Gb2OJ9eHuwK_YNa218gj79dP6r2WkBb7u4eYDkVzUPPxDEcxPJaQWgGJPp1Nq3iiSvynHCM4UaXsXowkw5bjHCGHvS2FXugwQcx_9qfM_Ogo9FF53-e9XrWVHmlM3fG3WMAAJNau5u83RfFcO3G35HzGCvlfRUoFX9-87VC7FAvuy5N2VUMYnSmbCeXKux2O9A-ACsZDu3CW7f1QpvPzCzxSaZoW87hnnbuvPFm-dyjptP_EyGH__ECmV7TGaR-THRxHizaHesC8sWVZJvMckgY_4kbyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43c261d593.mp4?token=WQXBad2rGGt410sq6vzkNZRPQzZPLkCd5FdEPgu1WFymEyGqg2SzPlUr1Gb2OJ9eHuwK_YNa218gj79dP6r2WkBb7u4eYDkVzUPPxDEcxPJaQWgGJPp1Nq3iiSvynHCM4UaXsXowkw5bjHCGHvS2FXugwQcx_9qfM_Ogo9FF53-e9XrWVHmlM3fG3WMAAJNau5u83RfFcO3G35HzGCvlfRUoFX9-87VC7FAvuy5N2VUMYnSmbCeXKux2O9A-ACsZDu3CW7f1QpvPzCzxSaZoW87hnnbuvPFm-dyjptP_EyGH__ECmV7TGaR-THRxHizaHesC8sWVZJvMckgY_4kbyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ در مغازه‌های دور میدان شهرداری گرگان
تصاویر دریافتی: 'ساعت ۱۹:۳۰ دوشنبه ۲۶ مرداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77920" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K3HHnkqeh4FC0X89Ey03VKuNK-A1VS-5hAWnPXEfORbiEYsGx_cgzcIzM0KqcFvtBxP6HFIIvuNEZeHOYSSOuZxY1MAQyC2Mie3MKWpr5BMXXUqM06e1i8wNXgLx7Zv9Ob2p-yTBMQ6-mHTB8cyZ7lvgrO4F2zFcXidbmAnI8lvPu2PFTZZgAL0L2exSa_IWZFxnJU8OBY_cJacBuxL1KaTIsE-xsQ0SAUiUd9S6lpmDbH5esmYPXSONTS2QhoPHiEKdS49GmyZYxh1fI6F6m1_juig6tyo4Y19eqz1A4MyRbIJpFZdWi56jHqDf0zI-X7-mQ-EmyNZcEGMt9h23jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/unuK79LfzOe5mez1LWn7kkOpWZu8IPVHD-dr21oOqbM1M4vzYXEt8ta9NP6o2b-TQ2Q9JhE3SiZewNR0LzT_wwxeSRNz3eLRE5JcE58nBAYsOE3PP3JyyBHscVPTUjUYk9bn80-gpUSMOqN6T7FLq7g_gGJm_XHWRtIIOkEIREAB85NwTTMQHyM8cMG15cIoHzwnL4TLUKx16RYXZR4HjPLRmYDRKK2FG0CF1knKFYrYfjH3jYuUYgMidubzzdIlanQGNemmiruHCwkZlavTk0EkC0Y3NUocVoClj_cLLkKtKQp3jNglS8ahP1Ce11_AZM4uhQ1-z87_WSUh9f5mCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که در مورد پرونده ایران عجله‌ای ندارد و به «کانال‌های ارتباطی پنهانی با سپاه پاسداران ایران» اشاره کرد. او افزود: «ما به صورت مستقیم با مقامات سپاه پاسداران ایران صحبت می‌کنیم».
او به فاکس نیوز گفت که «ایران باید پرچم سفید تسلیم را بالا ببرد» و خاطرنشان کرد که «محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی را بر رژیم ایران اعمال می‌کند».
او افزود: «آنها در پوکر فوق‌العاده‌اند... اما دارند می‌میرند.»
پیش از این، رئیس جمهور آمریکا تاکید کرده بود که «ایران تحت هیچ شرایطی نمی‌تواند سلاح هسته‌ای داشته باشد.» این اظهارات در آخرین روز از مهلت ۶۰ روزه تفاهم‌نامه اسلام‌آباد برای دستیابی به توافق صلح دائم و فقدان پیشرفت در تلاش‌های دیپلماتیک برای پایان دادن به مناقشه بین واشنگتن و تهران مطرح می‌شود.
@
VahidOOnLine
سخنگوی سپاه پاسداران، ادعای «دونالد ترامپ»، رییس‌جمهوری آمریکا، درباره وجود کانال ارتباطی مستقیم و پشت‌پرده میان دولت ایالات متحده و مقام‌های سپاه را تکذیب کرد.
براساس گزارش خبرگزاری «تسنیم»، حسین محبی گفت: «هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست.»
او اظهارات ترامپ را «فانتزی‌هایی» ناشی از «توهمات و کابوس‌های ناشی از شکست و استیصال در جنگ» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77918" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lb4fD5JW_b7wpgfUcJxxdO0f91mK3ixSn5ZNt_Kt3OhVXBd0rHGaTP3Kgpf76tHAjZD_X_RI06Zdsem6xuKaiojaTI-az21nERz7WB0kiPXcG9uYUoxY0f-gdrNdfYdBRKElstARUjA-J-y7RfIdM0CpO0NcW-xtPPwVbFcNUJw8-MoDGWmG_6UfNRSOip9fqx4xG5thM5WPVazvU_RWwjtABLs9mOeIdMqH8v_pKn6Q1mATjNOoN9zy1VmHfX2wVAaSkNnAKLx59UoSF5LUsRdjsGxWd8UN1PLUEuad59Vhns7lyjQ5oyRru3qak-VqIfOnmykNtXRQh__J4lJ0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره مبارزه با تروریسم اقلیم کردستان عراق اعلام کرد دو پهپاد که شامگاه یکشنبه ۲۵ مرداد از داخل خاک ایران پرتاب شده بودند، دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق، و همچنین منزل رئیس اطلاعات این منطقه خودمختار را هدف قرار دادند.
بر اساس اطلاعیه روز دوشنبه این اداره، «دو پهپادِ حامل مواد منفجره از نوع حدید-۱۱۰، از آن‌سوی مرزهای ایران به سمت دفتر خصوصی نخست‌وزیر اقلیم کردستان و اقامتگاه مدیر آژانس پاراستین (سازمان اطلاعات اقلیم) شلیک شدند. خوشبختانه، هیچ‌گونه تلفاتی گزارش نشده است».
مسرور بارزانی در پستی در شبکه ایکس، به شدت «این تجاوزات گستاخانه و غیرقابل‌قبول» را محکوم کرد و نوشت که «این اقدامات به منزله تشدید خطرناک تنش‌ها و تهدیدی مستقیم علیه امنیت و ثبات منطقه است و چنین حملاتی ما را از ادامه انجام وظایف و محافظت از شهروندانمان باز نخواهد داشت».
انتشار خبر این حمله یک روز پس از آن صورت می‌گیرد که وبسایت اکسیوس گزارش داده بود دولت دونالد ترامپ در دور قبلی مذاکرات با تهران، از رئیس اقلیم کردستان عراق برای برقراری ارتباط مستقیم با فرماندهان ارشد سپاه پاسداران کمک گرفته بود.
@
VahidHeadline
اسماعیل بقائی، سخنگوی وزارت خارجهٔ جمهوری اسلامی، این رویداد را «بسیار مشکوک» توصیف کرد و خواستار «هوشیاری بیش از پیش همهٔ طرف‌ها» شد.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، نیز در گفت‌وگوی تلفنی با فؤاد حسین، همتای عراقی خود، گفت «هیچ اطلاعاتی مبنی بر آغاز این حملات از داخل خاک ایران» ندارد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77917" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=DXfaCF_adrpVNuaNEVf7rAy3x3sGUGtdGcwze8MmD_tAXMsOJz-OVhI3oI-V08TGw702HL-8t797c4HEe-Ce4eTT4JB_3V8-BbLMhd2otys1IoS1uZbTwEv5SzYKfxHejJAdc87sRSc7DudpOH1GCV3JTvJjwao_2YFdxru_X0nYNLqmtDaTyAsMSExqLhbNQpn0OTKVx2IdOCbpN0TVtwkWq2rRtu0gXcBuK5KJNc5SXGcq-eWe_GFv2-OAfg_mfprC0SxQyxkomQsvag05TlhEYjZ66YfomULmlvRVi0OmANA3hL54tN6R8ZxuJmUFE6Mpvlf0rq5Ly3-NKtGaMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=DXfaCF_adrpVNuaNEVf7rAy3x3sGUGtdGcwze8MmD_tAXMsOJz-OVhI3oI-V08TGw702HL-8t797c4HEe-Ce4eTT4JB_3V8-BbLMhd2otys1IoS1uZbTwEv5SzYKfxHejJAdc87sRSc7DudpOH1GCV3JTvJjwao_2YFdxru_X0nYNLqmtDaTyAsMSExqLhbNQpn0OTKVx2IdOCbpN0TVtwkWq2rRtu0gXcBuK5KJNc5SXGcq-eWe_GFv2-OAfg_mfprC0SxQyxkomQsvag05TlhEYjZ66YfomULmlvRVi0OmANA3hL54tN6R8ZxuJmUFE6Mpvlf0rq5Ly3-NKtGaMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از صحبت‌های یکی از مجریان صداوسیمای جمهوری اسلامی که می‌گوید «جنوب ایران، فدای جنوب لبنان»، در ۲۴ ساعت گذشته در شبکه‌های اجتماعی فراگیر شده است که با واکنش تند کاربران همراه بوده است.
خبرگزاری صداوسیما روز دوشنبه ۲۶ مرداد با بیان این‌که این صحبت‌ها «تقطیع» شده است، ویدئوی طولانی‌تری از گفته‌های ریحانه قاسمی‌زاده را منتشر کرده است.
با این حال، آنچه در ویدئوی منتشر شده از سوی خبرگزاری صداوسیما هم دیده می‌شود، همان صحبت‌های پیشین است.
در این ویدئو، مجری صداوسیما در واکنش به انتقادها درباره حملات هوایی به جنوب ایران، حرف‌های منتقدین را «دلسوزی دروغین معاندین برای ایران» دانسته و تاکید می‌کند: «جنوب ایران، فدای جنوب لبنان».
در زمان حملات هوایی به جنوب ایران در ماه گذشته، بسیاری از ایرانیان در سراسر جهان با مردم جنوب ایران به ویژه مردم بندرعباس ابراز همدردی کرده بودند.
@
VahidHeadline
با توجه به چرندیاتی که قبل و بعدش میگه به نظر می‌رسه منظورش این بوده که مخالفان جمهوری اسلامی درباره جمهوری اسلامی این رو می‌گن که جنوب ایران رو فدای جنوب لبنان کردند.
اگرنه وقیح‌ترین‌هاشون هم درباره مسائل ملی مردم‌فریبی می‌کنند و این طور صریح نظراتشون درباره «ملت فدای امت» رو جار نمی‌زنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77916" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
