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
<img src="https://cdn4.telesco.pe/file/S3IdUroGKnTseHkP9ZLAZKAWQvGTbB9RI1irxMNz9_cnkg9iA97KLB-GBZGZwSj2vT6SUuQQV8T-tybNH2Cytf_LxZ0l8jqoJfJInd_Bf_ZWENIiYgntSi0jZEJBC9LPG-9hMIbpgMWnSzaRiUY5tZY0XuBH728vLdx4mvecXYNqgajYbt6YpXz08nW0y4IC071Hx1fXnMCwHOOD2O9peum64VA8s6UpMlNUlS8sFFouElzgLba0kpH7KnRFcAW25sPbGkMKS90dHZNDUtzb6h76FrwGAd8hjZ1EmSt_PsZNRtP7RaL2WC247Udx97RDiw_Bc7fYQpDfSw1999iRiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 17:36:18</div>
<hr>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123544aa58.mp4?token=mh1wdv6TbtzMBnc9IbSwDCpynSiYIZxYEes6-YbYhIXcs87EBADcCGChPxX-wYcmmk5Hh87ohVctvXsL13OO2tyf4eeuXisN6Sud4r9VZpiuWg6tQV2SAlYTLkH3NI7bia9pRHJ-MwOrjEke9_9eOncZQPWd6ZBEYuCV4A428NVCYjj13Vq6LdhRYr_XRgFv2pF1Il0gW0VrmEky8RVxTh6spEx8i1GYviGMBi-6Bks770lvqwE935J6X1adkuDxUB_bRBP7L4LeJXWXdByStvrDZSgeJwv1V7B6XnhBEzE7nC0JSMPJ5tvJLVUW89nFdK_np_3gw09-BoQ7hbMTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123544aa58.mp4?token=mh1wdv6TbtzMBnc9IbSwDCpynSiYIZxYEes6-YbYhIXcs87EBADcCGChPxX-wYcmmk5Hh87ohVctvXsL13OO2tyf4eeuXisN6Sud4r9VZpiuWg6tQV2SAlYTLkH3NI7bia9pRHJ-MwOrjEke9_9eOncZQPWd6ZBEYuCV4A428NVCYjj13Vq6LdhRYr_XRgFv2pF1Il0gW0VrmEky8RVxTh6spEx8i1GYviGMBi-6Bks770lvqwE935J6X1adkuDxUB_bRBP7L4LeJXWXdByStvrDZSgeJwv1V7B6XnhBEzE7nC0JSMPJ5tvJLVUW89nFdK_np_3gw09-BoQ7hbMTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جکسون هینکل فعال رسانه‌ای امریکایی در حال توزیع شربت نذری در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/131766" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
به گزارش بلومبرگ، سفیر ایران در پکن اعلام کرد چین و دیگر کشورهای دوست هنگام تعیین سطح و نوع هزینه‌های خدمات دریافتی از کشتی‌های عبوری از تنگه هرمز، از «ملاحظات ویژه» برخوردار خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/131765" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ادعای الحدث به نقل از منابع آگاه:
دور جدید مذاکرات آمریکا و ایران در تاریخ ۱۱ ژوئیه [۲۰ تیر] در پاکستان برگزار خواهد شد.
🔴
دور بعدی مذاکرات بر موضوع تحریم‌ها، دارایی‌های مسدودشده ایران و پرونده هسته‌ای متمرکز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/131764" target="_blank">📅 17:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAMxTg3ljJiV4Pimu9fNAovRlAzYeUV7dHS57gyZC27kHmIwQKV1AaAmB0Dp_buU6lnQX6hSdbPtnBqQnnF2RjSf_PQwjXdgrpbhXdHKdgeMUDIR79ycA9SNsIPDM4SfJkgOuCJPuKgMZitFIc8VaipX53tfC5qRhv1zQBoDVUkpVe3HLze6htUrwcnRr8IZJ2XkHbSRbteBtzdhKE6GihcS_LTaRVtwbAs5qBCEj9aGLXef3HmVVmUIWiqbPfYwXtX-4sZ4g6wocJw59AHmF0JxVbAHqUDrghXPkdPtRrBxZ8TEN0m3lvko73x8nRmBaNALmCYpnRxQS703T26IJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز مستقیم هواپیمای باری 17-C نیروی هوایی ایالات متحده از پایگاه هوایی نواتیم به پایگاه هوایی الظفره امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/131763" target="_blank">📅 17:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=t7i-gIjMtw14b0qCUWMqQkXg__dgyNj3q09cR2HC6idbMmk96kmT0PoLxQ0ZZkuZMDDkMT4cZHslz1cfl72csxVoL3ceCPuRThHkrfY9Ma3hAwpOzP60Eor8Gyzt4cS2wCIeB6aMMTWB1gA1mC-VxY-xVMGrX35LMJx8IjJzIv4W-O_vVs3vCK4WIHaRadth8x8GPfE4OXiyT4XFEVMgrN2q9rOKYDnR8sK_dwzX9E8-IuQMic9iGd0OcLEqGy5eBIKufeKS2K6sAhHwmfxB-QWR2f0ZilM51OXvzhL8HbMPY4Yc5COvdEY-SNV2xDfkuNOkZLB3aKjv-ym_2cmNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=t7i-gIjMtw14b0qCUWMqQkXg__dgyNj3q09cR2HC6idbMmk96kmT0PoLxQ0ZZkuZMDDkMT4cZHslz1cfl72csxVoL3ceCPuRThHkrfY9Ma3hAwpOzP60Eor8Gyzt4cS2wCIeB6aMMTWB1gA1mC-VxY-xVMGrX35LMJx8IjJzIv4W-O_vVs3vCK4WIHaRadth8x8GPfE4OXiyT4XFEVMgrN2q9rOKYDnR8sK_dwzX9E8-IuQMic9iGd0OcLEqGy5eBIKufeKS2K6sAhHwmfxB-QWR2f0ZilM51OXvzhL8HbMPY4Yc5COvdEY-SNV2xDfkuNOkZLB3aKjv-ym_2cmNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز : هم‌زمان با مراسم تشییع رهبر جمهوری اسلامی در ایران ، آمریکا جشن دویست‌وپنجاهمین سالگرد استقلالش را برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/131762" target="_blank">📅 17:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
به گزارش فارن‌پالیسی، هند و ایالات متحده ممکن است در برخی اولویت‌ها اختلاف‌نظر داشته باشند، اما رقابت جداگانه هر دو کشور با چین همچنان به اندازه‌ای جدی است که همکاری راهبردی بلندمدت میان دهلی‌نو و واشنگتن را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/131761" target="_blank">📅 16:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کامران غضنفری نماینده مجلس: پول دادن به مداحان که دیگر در تجمعات شبانه حاضر نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131760" target="_blank">📅 16:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
روزنامه تلگراف گزارش می‌دهد که یک ابرقایق ۱۳۳ میلیون دلاری که گمان می‌رود به ولادیمیر پوتین، رئیس جمهور روسیه، مرتبط باشد، به سمت بندر مورمانسک در قطب شمال در حرکت است تا خطر حملات پهپادی اوکراین را کاهش دهد.
🔴
این کشتی ۸۲ متری گریسفول توسط ناوشکن روسی سورومورسک و کشتی گشتی وووودا اسکورت می‌شود، در حالی که ناتو کاروان را زیر نظر دارد.
🔴
از این قایق تفریحی در حالی که تورهای ضد پهپاد عرشه آن را پوشانده‌اند، عکس گرفته شده و پس از ورود به دریای شمال، سیستم شناسایی خودکار آن خاموش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/131759" target="_blank">📅 16:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131758">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نخست‌وزیر و وزیر امور خارجه قطر، محمد بن عبدالرحمن آل ثانی، با وزیر امور خارجه سوریه، اسعد الشیبانی، در دوحه دیدار کرد تا درباره همکاری‌های دوجانبه و آخرین تحولات در سوریه گفتگو کنند.
🔴
در این دیدار، آل ثانی مجدداً بر حمایت قطر از وحدت، حاکمیت و تلاش‌های بازسازی سوریه تأکید کرد و بر حمایت دوحه از آرمان‌های مردم سوریه برای ثبات، ایجاد دولت و بهبودی بلندمدت تاکید نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/131758" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131757">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نشریه نظامی «میلیتاری واچ»: کارخانه هواپیماسازی روسیه تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط ایران را به پایان رسانده
🔴
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
🔴
احتمال دارد نخستین سوخو-۳۵ها از سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131757" target="_blank">📅 16:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01db34aaaf.mp4?token=X5o1RSSvnu80uYhliJ-0qt7qg6Ib1I399K2o2bNzdF8AXlH5-Z9HEjyNibk1-vl8weIUmDibfYfo90Mt79nAnEgXlGLWeuDGRnuP49FVu_oFJwhKswV4fBMrCEF43ZWR6H78ElxsAm_rH0b7x3LhEM1hdvtAFNlCLaYYGZihJ_absL4OehGHJl23YBHphMTTV2jwP83NdXSsyvhBD8ztPdlQjkjPQv6sqadH22RrKvjyb7AgmGj1_sRTKTkupfZiKj8ibanrQC8P0fVfuLiO2fmqWyXWo6aQAIZpS8NI-KfLa_78-S3CfNnnHGTz1cwlG9KLu24XBigIMBAQoWS7GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01db34aaaf.mp4?token=X5o1RSSvnu80uYhliJ-0qt7qg6Ib1I399K2o2bNzdF8AXlH5-Z9HEjyNibk1-vl8weIUmDibfYfo90Mt79nAnEgXlGLWeuDGRnuP49FVu_oFJwhKswV4fBMrCEF43ZWR6H78ElxsAm_rH0b7x3LhEM1hdvtAFNlCLaYYGZihJ_absL4OehGHJl23YBHphMTTV2jwP83NdXSsyvhBD8ztPdlQjkjPQv6sqadH22RrKvjyb7AgmGj1_sRTKTkupfZiKj8ibanrQC8P0fVfuLiO2fmqWyXWo6aQAIZpS8NI-KfLa_78-S3CfNnnHGTz1cwlG9KLu24XBigIMBAQoWS7GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای روسی مستقر در آفریقا، امروز صبح حملات هوایی را بر علیه مواضع گروه‌های FLA-JNIM در شهرهای آنفیس، گائو و سِوارِه انجام دادند.
🔴
همچنین، یک اردوگاه کوچ‌نشینان توارگ در منطقه زارحو، واقع در استان تیمبوکتو، مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131756" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpbd45n83Y6xXY5I9USlo6jqXfr5xNEp0HAPuoxk1HtIXfVy-pc3BiGTt4xL3W5icuw3bI-I9mi_MkbgiPZ2h-WcCGjiTjJfiWEGzq198oq_wHwb8Ti-ePdZDQNuPifxjBIVlkXPHXIsDy0AIMWw0-CPVUJUoSEWjH318WwS6OOUadBSFLlNkSCQ_pax28k-Jt5bggP8lDgYMN__bZQz88TeTNKFJmIXvqZ9eZ9w27EZ3hztS-PSMIkUwYBWlLnVajYZ1ew1WVlPKbZBA4X42uOpRASG9QVYrf87UpMKZRDHzA2Rx8MQnniLsouwHnDj26oyP6PqDeF3piw4yiOZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی در ایران به اعدام محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131755" target="_blank">📅 16:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/فردا یکشنبه سراسر کشور تعطیل رسمی اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/131754" target="_blank">📅 16:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdhyqBS7kkszvCITqSlegFY0DYlLMvONru0rvoKR79luviWeNibhGQID6dJA8uW5AIbaXxae6ENtv0Xj7WLazsmyroiO_Y6vlI8_qe2RnRQlppMN4L-AEvxfYSqkyrpAbVZPlIlp3Sli69rmcV3_XcIzZaVi68Zu3n1yt2ulEkS9lLVWuxJEa5zeCgDUB6aHqHcDm7lbC8tdgLejyquQ_NIi-ITpo6Se3Psci2-dm7WQbX1KuZRcEyhLfKhVjAev2uQvNOgtgS3UCK1y6glyi413d1Yf9Cuw9B3fvaSsQCqMbs6Kf1Wjes6OoRxV8JGexe2AFOUDRmsODpcPt8slHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار عظمایی به عنوان فرمانده نیروی دریایی سپاه معرفی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/131753" target="_blank">📅 16:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9286675b.mp4?token=gLDzVHhmCPZoQ2XfvVuwCyHbFqMG57SYD20juAOalZBT1okgMoSNiScUs97OO8orFTnp4UO1De3l-tdUBth8WSEyQY72x48kF0lL3eOUXEv_x26ZIJmskK6ucBpYbGanTIcYk_dpT4ynYLfsGYnyks0KLMxEyU_E5KeC5KuX2NxE5KaaPi_aYMvg6ypERLVVWZ9SdA5XQVSRZZB06oMThP2XhwnZGou_Zm2rlFYi5s6spAW8qu8bS4Q9U5eK7f8cFgF9FwfBwMyzlVlUzR43UkpaNCRtyXisg-5tSkrg0iz_9G_xzqcXSLWP5qr8Dt5iCkx-7Br3ge3xVI9HfEpbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9286675b.mp4?token=gLDzVHhmCPZoQ2XfvVuwCyHbFqMG57SYD20juAOalZBT1okgMoSNiScUs97OO8orFTnp4UO1De3l-tdUBth8WSEyQY72x48kF0lL3eOUXEv_x26ZIJmskK6ucBpYbGanTIcYk_dpT4ynYLfsGYnyks0KLMxEyU_E5KeC5KuX2NxE5KaaPi_aYMvg6ypERLVVWZ9SdA5XQVSRZZB06oMThP2XhwnZGou_Zm2rlFYi5s6spAW8qu8bS4Q9U5eK7f8cFgF9FwfBwMyzlVlUzR43UkpaNCRtyXisg-5tSkrg0iz_9G_xzqcXSLWP5qr8Dt5iCkx-7Br3ge3xVI9HfEpbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهرک‌نشینان اسرائیلی، دسترسی فلسطینی‌های محلی به زمین‌هایشان را در نزدیکی شهر سنجیل، در مرکز کرانه باختری اشغالی، با مسدود کردن یک جاده، مختل می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131752" target="_blank">📅 15:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
آگهی دبیرخانه شورای عالی مناطق آزاد تجاری: انجام هرگونه پیش‌فروش خودروهای وارداتی در مناطق آزاد ممنوع گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/131751" target="_blank">📅 15:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزیر خارجه مصر: از تسهیل مذاکرات ایران و آمریکا حمایت می‌کنیم
🔴
باید آتش‌بس در لبنان اجرا شود و اسرائیل به طور کامل عقب‌نشینی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/131750" target="_blank">📅 15:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131747">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003c393383.mp4?token=vtPF5DwOuofdAtRxPZ6GmcuRF0MS60W6dFphdbReG6-uY-VNnHhm8Qx17aNj-PBC0pLpXYf3F1Wd3aDBRBGdxyzbr_Ll67q6MvYcq0WXlWCTloEIW2fFk3H4NboH7kdlObzYL7xZuQvu4kdUH10AeCyfl_0Fzbnd-h-rVYBJAZ1s3tnZxuNqAQI-fQxibDlZFOuDUD8SPGyx9jTV6MEwsPUtot2D8bWjaf1TPqozrQ5qo-MGAPWulzZZ6u8Nb58q8nE-Fhd_XknRchEYME3WOUD_t9s4WwIMwj8nPZ7Iy8RIj6n5CvovNBzTiNOZ5JoPRqmm2JJ0QjrUnvJy4oA2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003c393383.mp4?token=vtPF5DwOuofdAtRxPZ6GmcuRF0MS60W6dFphdbReG6-uY-VNnHhm8Qx17aNj-PBC0pLpXYf3F1Wd3aDBRBGdxyzbr_Ll67q6MvYcq0WXlWCTloEIW2fFk3H4NboH7kdlObzYL7xZuQvu4kdUH10AeCyfl_0Fzbnd-h-rVYBJAZ1s3tnZxuNqAQI-fQxibDlZFOuDUD8SPGyx9jTV6MEwsPUtot2D8bWjaf1TPqozrQ5qo-MGAPWulzZZ6u8Nb58q8nE-Fhd_XknRchEYME3WOUD_t9s4WwIMwj8nPZ7Iy8RIj6n5CvovNBzTiNOZ5JoPRqmm2JJ0QjrUnvJy4oA2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه‌های بزرگ وابسته به سازمان FLA-JNIM وارد شهر آنفیس در شمال مالی شده‌اند.
🔴
تعداد زیادی از نیروهای ارتش مالی (FAMa) کشته یا اسیر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131747" target="_blank">📅 15:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131746">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b402cee7.mp4?token=DVjPkj0_YBROg-1FiEEHAKmwL_GonsG9_h1TTffn3nhlCJrV0B8Jyrmrqbjl5yEoIuSXqL1qN3N3TYSudSmXerA0rlTG8JD8olAnantvyDSDZlntIG7mi6CkOCLcV7N8rA6NoABodyMN55iX_lYluVcDmwDCaX-XWyKeE4druwKZLQAVflMtkM_YPDAyJLwe0ea1SCl5MWwLD9eBMZJhqcgoysm2H7FPeZeix1jRUg_Bs8bMMFpA2SLTZqAgeTOEksKS3l3hiTTPLioR-S8QQFM1V_KagzaP76-MqK1xYXb4bbPYjA-rj_8x3YpSaGdqWydi8C1Rb6yJvCt9RxJJKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b402cee7.mp4?token=DVjPkj0_YBROg-1FiEEHAKmwL_GonsG9_h1TTffn3nhlCJrV0B8Jyrmrqbjl5yEoIuSXqL1qN3N3TYSudSmXerA0rlTG8JD8olAnantvyDSDZlntIG7mi6CkOCLcV7N8rA6NoABodyMN55iX_lYluVcDmwDCaX-XWyKeE4druwKZLQAVflMtkM_YPDAyJLwe0ea1SCl5MWwLD9eBMZJhqcgoysm2H7FPeZeix1jRUg_Bs8bMMFpA2SLTZqAgeTOEksKS3l3hiTTPLioR-S8QQFM1V_KagzaP76-MqK1xYXb4bbPYjA-rj_8x3YpSaGdqWydi8C1Rb6yJvCt9RxJJKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار نمایندگان جنبش امل لبنان  با سید عباس عراقچی وزیر امور خارجه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131746" target="_blank">📅 15:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131745">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی: پزشکیان به مجتبی خامنه‌ای اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
🔴
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی خامنه‌ای با یادداشت تفاهم موافقت کند.
🔴
دکتر پزشکیان، قبل از امضای توافق، به آیت‌الله سید مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/131745" target="_blank">📅 15:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131744">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گزارش ها از پرواز گسترده و غیر عادی پهپاد های اسرائیلی بر فراز بیروت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131744" target="_blank">📅 15:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131743">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131743" target="_blank">📅 15:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131742">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSyowGP0DaIrGYxLi6IS4ZAIWI6r7Rrae-WV_T5u7rEyAY_LiwFddqqLiB46TIBdaXZApvUhbrHlOOttzEO83GpfLVo69TQzh55uQquY5O-HObLPRn5Ds7s_7Xb0TyKVKOTv8-0Jc5Hv-W0rZQjnOa5XxQ166J6YgtXJCIMaR2OG8uB4_JmSjVysQMOSUSP7FfNUFh8IpNc_aZ8Pc-2w8rO8jdA-APe6jG8id9LBx5lFaOgrkIx2zN5ptz_w4n5_7izd-VxAw6hruD08XyRzyN_Zq4i8smCS-0mvYlJnScrPHUIfrL3-MsSa0v9abZhq9Zm6NzwW3otwVLczkak8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خلاصه‌ای از کیفرخواست رضا پهلوی که توسط خبرگزاری تسنیم منتشر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131742" target="_blank">📅 14:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رئیس‌جمهور عراق: عراق نه با ایران در برابر آمریکا متحد است، نه با آمریکا در برابر ایران
🔴
روابط خود را صرفاً بر اساس منافع ملی تعیین می‌کنیم
🔴
پرونده گروه‌های ضد انقلاب بر اساس توافق با تهران، حل‌ می‌شود
🔴
امنیت خلیج فارس، ما و منطقه به هم گره خورده
🔴
تلاش داریم تا بهترین روابط استراتژیک با عربستان برقرار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131740" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131738">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d_Ct0ynsRcnZDeNPoz59KPFKOZLs_i-x786K7s1KCxXb-TufKScnnZRFog-oRjACgDCb8AEGvTZO1-HVTFd6JZiOQ5iic7n__uD8nWaFfPQaYbh-OvlYxDtKDXlNR3Y-jS9Sr00W2p6GvdZ_agzoibUI6g_glZj16Gzh6G-SoOjmN2dc5tzyq9StE8RKdSluAlkNkY9MV7M_vQuV_Wv0KqtRkt4Zm9lt2QiDLRd2YdhLR9GnKAldJmXqCzHMsZcPmNXC2qoCRbPOHsf9vP4B8aqDhSFXmqUoZrfPkQ3Ex0qCwcRIZfXeV0lw6qIrpnp-OiuXgPDEXX1O7o4gIFhc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UXbEXLCv2dxPusgLLL5up8sVmzB6yMoVIciakL8jIp_lJaFUqTtfwp8F3ZVYIm9Y96gTAk_8bSoqHVK7zJ61lzty6vakOVUc2jSv4Tz0zVz-g_7WUgpJk-53kJfqATxo9dSEU1PPFQqUeX7SRQsmiaCQHBeY1-MX5ARDGfcYAT6OzbC-UsVUJe2pEsLLdvIS0GyyHU8iKk8LxzCYXnYu_1I5ISG_vdaAaFzFzvRgAiAVkJ55nabWAZZU4OAPsi0DLz5FtVf8H08FVN7zNfqchfywLjQ26l4_nwD74mFHOnXCsAfve3KMQLWjIwu_CQ6A_bh76HfrU7wCaz5sYMCLuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا یک بالن نظارتی (الکترواپتیکی) یا مخابراتی در آسمان تهران مستقر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131738" target="_blank">📅 14:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131737">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
به گزارش اسکای‌نیوز، گروهی فراحزبی متشکل از ۷۱ نماینده و عضو مجلس اعیان بریتانیا از دولت این کشور خواسته‌اند بنیامین نتانیاهو و یاریو لوین را به اتهام نظارت بر سوءاستفاده و شکنجه سیستماتیک بازداشت‌شدگان فلسطینی تحریم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131737" target="_blank">📅 14:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131736">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ : کمونیسم یعنی مرگ، استبداد و دنبال کردن شرارت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131736" target="_blank">📅 14:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پیام پوتین به ترامپ: مطمئن هستم که روابط برابر بین مسکو و واشنگتن، به نفع کل جامعه جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131735" target="_blank">📅 14:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131734">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
به گزارش بلومبرگ، امانوئل مولین، عضو شورای حکام بانک مرکزی اروپا، اعلام کرد این بانک پس از افزایش نرخ بهره در ماه گذشته و انتشار داده‌هایی که از کاهش تورم همزمان با افت قیمت نفت حکایت دارد، در «وضعیت خوبی» قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/131734" target="_blank">📅 14:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131733">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است؟
🔴
مقام‌های ترک و اسرائیلی سال‌هاست که علیه یکدیگر تهدید و توهین نثار می‌کنند. از زمان آغاز جنگ اسرائیل در غزه در سال ۲۰۲۳، این جنگ لفظی تلخ‌تر هم شده است. اما حالا به نظر می‌رسد اوضاع دارد از کنترل خارج می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/131733" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131732">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5_DeWNi1nYik9V297R8wJ9zWFyw85Km9gJyV276YpRk5IrWWFHy5rcQYTPPwAjgslgS_Ouxx-kf7Ct5_3hfoCgtM9umunnSZKtNo9NKs198MIq-AnTeIOxY1LebAXH5PrixSwEhGJyGBZZfEMLU-5MOFu6TBbtGGmaYuQSwkhUGOAdo7MqVFn-KxAkVuOcrJBMRNEf-q9U4ExR_5Ye9wNlqjZzmnOuneBukDz16gVf_PiOvLCFj-jHonpPis7as4s8ZA6ETgcNTKuEDEEYv19F1Qf8S-sJhUXZToix8186fptUKHBPpVNS0fHDfc1CzuZ5i4fDCfXEtA2-OxnhLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار سی ان ان در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/131732" target="_blank">📅 14:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131731">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m89zcPHBiw-UEmi0q3y5X3bZ4pZe06jTeOKnv_fJVTndwpQ0auRZlbaZg4E-ovgEVhyfMSZaF8EhyElsJVOn4hrUHExXqY6s6wUCl46aKX5Z_TjEJs5ue6fHdBaCd6gmF_k_AUyxnI4xWeZgrZrq_l2WIv70wPo7rxQTBJ1IABwKxEKCTXl3KfbAFc_e0ZQl8I98G8N_eocmUJsZcksVooExwEwOW-5-uZXZZVssJFJplgk7oNZIr_3wJ0KTkR2zAzYT62LI_GB0c1uK9jZS3Ah_IxBb7dqaCkNEZLqIyj4o5rLmmvhQPg3q4f2DNtW4azMCLgtd6my1gLK-AQthEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/131731" target="_blank">📅 14:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131730">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر سقوط یک هواپیمای جنگی متعلق به ارتش روسیه به دلیل آتش زمین در شهر گائو در مالی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131730" target="_blank">📅 14:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پاتریک پویان، مدیرعامل توتال‌انرژیز، اعلام کرد تولیدکنندگان نفت خاورمیانه به‌دنبال فروش نفت خام ذخیره‌شده در جریان درگیری‌های خلیج فارس هستند؛ با این حال نگرانی‌های حمل‌ونقل همچنان بر موجودی بنزین و گازوئیل فشار وارد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131729" target="_blank">📅 13:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مهران رجبی : حسرتی که پس از دیدار با رهبر به دلم ماند این بود که نتوانستم پایش را ببوسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/131728" target="_blank">📅 13:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی : تاکنون هیچ حادثه‌ای در مراسم وداع گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131727" target="_blank">📅 13:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKxfyIFFweOqd4_2kOR4iB-DiRacTStObbx6_RJlJPkmeluyLOfo3D4wPVd2LyKDIVCvo1YVcSksQp1e28YYGGpI5F_K42DW9OogpmrLx3VbCsegTQejuBtDxN5mc1Eu6pKIt2WDEwqWjP0Xs7a-CFRWr8Nc5XMmbHaMeCWHCy-9Q4cElFhv_tuD9FFS79h1KN0HLA73Cx3_fNDrcQGe3OkHdydY_5NlMqEqlvLI4GCNTn9zXlTU9Yb4MhelFSQ533Wl8kl_08aUZDfKdQt-W3H-iq2pbYdHay2Oj7rVu_b0fHwT9Q4Lr18RMlihUlgLxLUXTzI55OZqTw8ELadJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز روز استقلال کشور ایالات متحده آمریکا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/131726" target="_blank">📅 13:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X53spOYrWcvT-hXyOHbqrrj0hYCg46jWg4kzSisaCwb9XSRITItUYISiuDRgnvmO5EVa91qhpvnixGQ45wLAP1HRevPPgWXuYect7vcgaIsp-B_gkNp2STUczZoQOZx9igGHUUEt3IPfBfyRicpI-GqXSiINIEkKW8EVv8btBRSBrXjXjEzU0nzLY4Rm9OeCnGqHMM9zl6QMWSGPJk4xa8JFqBSw0bwGFH9aMIzHeDbd3Pyob80ZEC6JByDEm2SpvAzSvLQlbFa2o8CfJDcg9QAtcQU4n2GUDw9aTJ_IYpmRgxwJPFpq3mnNGDU0AUcRf7I0VKWaY60YUxYb-D09LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب/برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131725" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
میشل عون در پیامی به ترامپ : از شما می‌خواهیم که همچنان در کنار آرمان‌های عادلانه لبنان و نهادهای آن بایستید تا بتوانیم فصل جدیدی از امید و صلح را آغاز کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/131724" target="_blank">📅 13:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ:هیچ کشوری به اندازه ایالات متحده آمریکا، خیر بیشتری برای این دنیا انجام نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131723" target="_blank">📅 12:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131722">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آلمان انتقاد ترامپ درباره صرف هزینه‌های نظامی کم در ناتو را رد کرد
🔴
فریدریش مرتس صدراعظم آلمان، انتقادات تند دونالد ترامپ رئیس‌جمهور آمریکا، در مورد کمک‌های ناچیز آلمان به ناتو را رد کرد.
🔴
وی پس از دیدار با سران کشورهای حوزه بالتیک در برلین گفت: آلمان در حال حاضر بودجه دفاعی خود را ظرف چهار سال دو برابر می‌کند. این بزرگترین تلاشی است که ما تاکنون برای تقویت قابلیت‌های دفاعی خود انجام داده‌ایم. بنابراین، چیزی برای پنهان کردن از کسی نداریم.
🔴
وی افزود که این موضوع را با کمال فروتنی در اجلاس آنکارا در روزهای ۷ و ۸ ژوئیه ابراز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131722" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwBkcSMna5liEHzgr9WEQEzDrshmo7gbX1jOPPsHMT1JU2hi-6xYj9ZhZ9GGQZK-9lZyPtACJC34H9ZqbcNny0FGEhsZ3VJYbRjJAzW3HuLXuS4oHfXF5Z9kF4enS63j9Cwfg0XvQecxrXW75FKEYXe9EHmRtUhOsMzzInfh6wFt92U1edkzvY3RCdOxxaRvlBCmDPcuRdaFyc31BddX2zldAWQmOln2R82d21KoYNH17d2gmAK2pagujB2W_V2Prru7eMlNgMF8L1052chd_bCTXnr63J0SNsKtDR0ftaK-YBoouB7YaYILXh2qtPmLV30q4St2go0ayG4SsSKBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atoXGr6uLVOpZhb8laFE-2q8HVdVhYlpduKNsUuFbBBTaouNHx_t-MUK8CUl9KR7MbJ80spXKhx6SN62HLUYt15Fp9EIKWIsv0M8W5qNo9DOYpqxRYz-faLjofysBm4nGk-VRFDsveEcZz1992-FC5y0cQqr_gT-M9tw0c49JLhb50Xiz8VH1V38EWLrmz3CB68UXcF23vKfpG-WwKn-zNR8G3CsDFZ5PfkbbhUOykFvdgbw2Rftwz1m9MEsZG-XMS5iOcf6UGloZ7estZHUW4jLg3DDom8DylGIVdnZYEMSleaxMsiFOwtc4Y5eOHHl0KNF472qSOYCHdAirEEkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKNRmP0t8OVvun3qCgjwCrvD-TjERSvm9e6YNhl2yUtNiaqcwiZ5jja-IGtUZEAp3Tw6I87AJzFSEAs1eoEMhwWs9Uqr8pLCjvzLmayl6udGPyWmuYGjaXR65uPoRcP_SToZJahfUE-EmqHJWgYEe7Od8WxyXodWFJilkuqJO8w4uIRJGT-_vt_ObGs_8iL2FVF_b4VqyizE81G6nGM8C70DGAJg5_tj3vIfSGca4Kt2QwCPJD1FTJxFNPU2vo1CuWRPpROW2DC54YD4PfMI9NSl-0J46v8EYpdOTvclTeFaFJ8Zokb3ClZBPV1a_ilKKjkLox91hxnCXcsb22FldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vx14sjFM1WKGp8WklFCPaO8o7hyLDhUucxzJfzEgEpN9wsXfDhkOcT5AlukvIY9gXWbqSKjpEBtnnSpDfdlrYIWmFmk5c0GYA4jUgAulKxfuaJcjcepBPTGpCNdmvJBcMAC441Okqk2DGQ_XpgNDZQPK0esCYqpRFXlbxxvB6AI36x178XzurcAI1AU2Bi1oCw7Z8LFLBzzmT6wFoSZUe4X17r7WH8gI5i6Hk8trR8xOgqku1G1G_Y4lW5QrvdsuZWQB-B0C8OTSSCkZp0DeD5TptrMG1fI1lx6F0sl3vodYR3jPCdN-YlCENJXIbVTHS1mqrR_hLInQ1q8wgzvjmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به‌روزرسانی (تنگه هرمز): چندین کشتی به‌طور ناگهانی در حال تغییر مسیر از کریدور عمانیِ تحت کنترل آمریکا به کریدور تعیین‌شده از سوی ایران هستند، یا حتی دور زده و بازمی‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131718" target="_blank">📅 12:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع لبنانی از حملهٔ پهپادی اسرائیل به اطراف شهرک «صدیقین» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131717" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی: به سایت‌های هسته‌ای ایران باید دسترسی داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131716" target="_blank">📅 12:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
زلنسکی: زیرساخت‌های نفتی روسیه در نزدیکی سن‌پترزبورگ را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131715" target="_blank">📅 12:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBTCkqxe4fNo3oh3E_ef9G_8bfEcb064zEhIiHVEqqEezSLRV2vk3_74um5YSV0xQsxgJMb9VsV6VJZzw3mPAsnmD_HZlAIejhoPIaKkZytXjkFV51qB0kHICShxx1FaVbbY5DIdEox9h46XS3XxKao2n6ULBZG9nBwg-O-PVcGkTSEsgQdGwJad2bDZ-fEyUILW_2Bbaux7ZNN_c6y5OtvRZI3eTma8DQ4ltLnS9MajBWAGbMTVyP_Arm0vIWZS4jChgtjsxjv5wxyk5EurLCOCSN7BxjiGi8k2i7KQIB8i-KjEJeOaf4cBAUZ1gEv7Jezc6MnuXvxl5K5KKsMC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ پهپادی گسترده اوکراینی ها به یک پایانه نفتی در سن پترزبورگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131714" target="_blank">📅 12:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تولید نفت اوپک با بازگشایی تنگه هرمز و ازسرگیری صادرات تولیدکنندگان خلیج فارس افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131713" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxDqWPt5m7I3dseT0H7fYgBkIpS6i5kse99uo7uhn3aDtHSfuX_vIzJMtIJ06dzeWnAfPM5JnXWwwEh63FwmuSHY_ZTinKlWoa0N_irmzslh08FuY6WBXREiExIrIRwPd6ice6PofzFkVh2s6vCssZREHObdBp0ngjkALNDFgKpTuD4bRn8RiVuMv6GuY-NqQrVq_jdfJNBiw5NeJf2I5chJ4tUsh6Pc9Q6_Lw74Y0sjKbgVKTAsrysEyqzGWJsq6fXB-xT-PC6r4nDBPmhcLqIazA4nb0DjW6EZZ0eZ9pH2d8id_a1FMCOt6sMKhCK3eRlcqnAGITZG2HUOgXQ9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: به گفته سه نفر که از موضوع مطلع هستند، مجتبی خامنه‌ای در حمله‌ای که منجر به کشته شدن پدرش در آغاز جنگ شد، جراحات شدیدی متحمل شد، از جمله سوختگی در صورت و بدن و زخم‌هایی که نیاز به چندین عمل جراحی روی یکی از پاهایش داشته است.
🔴
انتظار نمی‌رود که او در مراسم تشییع جنازه پدرش شرکت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/131712" target="_blank">📅 11:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131711">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRW84rlvx_Xww8fnAOyUubBr55GLXhcggYWijWMxvrgilCO5rB4IklWuFJs1mUQoSk90kZEUdw2AbM-SReNaRzWPrILGmZJ3d88jVBvqPEytLqcA7cEFl-goPIMIm0ecPtgILRNzWPzSigNa-FoNQg9xWCzERfIS3mBwEuXUxUre53vcdGTfAz43gI6kevRVBhXfrR8o5ARvXl7o6bfXuFpbPYw7YO87o-dLfoFghBDKy9l5N0jGfYCWBrJhKDpJXkRxdK7JJCSNwGZZV4JTcGF7MUwGxWuIuCtUMRzlPPzEr8-Zn7VWKb0tqrMsHQD_OZW9jQ0OPDH454SxIv1qYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک
کاربر اسراییلی:همه کشورهایی که در طول جنگ توسط ایران مورد حمله قرار گرفتند، در مراسم شرکت کردند؟
🔴
چه آدم‌های بی‌اراده و بی عرضه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131711" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
محمدباقر قالیباف در دیدار با رئیس پارلمان عراق: درباره مدیریت تنگه هرمز موضوعات مهمی در تفاهم اخیر با آمریکا به امضا رسیده است و بر اساس قوانین بین‌المللی، اداره تنگه هرمز باید میان دو کشور ساحلی ایران و عمان انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131710" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
انفجارهای کنترل شده برای امحای مهمات عمل نکرده، امروز در جنوب اصفهان (ارتفاعات صفه و بهارستان) انجام میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131709" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131708">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0S1hKT_xPq7Sp82zVQd0CwynUuRvrxWAz7FhHLzaMsXNuD4GfCI5dGGJTvts5fGWS0cm_Miu2_i03gvE8i7O_9qZUwd4M6ZoiemquTq3_KIQ0fDk3cJHwaWYPTmYrMOrLyR93KrYgC8AdPnTu0_oofT9uLVepzlv9XBlBodS89gubjB-hB9CRP4vnrmFqN5gk_hvylNK5QA0BKdSHM-eMKxpZwC8IqRllIDTAxj-_AuzkXOOdAbUrRwoA1eN1Yuow87XE5jVPJ6m9RC1qMENXW5w7XXv3ZWHiAspcYAM9kDt1dQ2H-mjhfiUKOIRVcKyJZXUpvUW5sl-PPA6ioKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده در رویترز از مراسم امروز در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/131708" target="_blank">📅 11:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131707">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مدودف: تنگه هرمز اکنون برای ایران به سلاحی تبدیل شده است که از نظر اهمیت دست‌کمی از سلاح‌های هسته‌ای ندارد؛ اما یک «سلاح هسته‌ایِ» دیگر نیز وجود دارد و آن تنگه باب‌المندب است.
🔴
روسیه، ایران، چین و دیگر کشورها می‌توانند درباره ایجاد یک پلتفرم مشترک برای کشورهای تحت تحریم به‌منظور مقابله با محدودیت‌ها و تحریم‌ها گفت‌وگو و رایزنی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131707" target="_blank">📅 11:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ارتش اوکراین کنترل شهر کوستیانتینیفکا در شرق این کشور توسط روسیه را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131706" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131705" target="_blank">📅 10:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
فرانس۲۴: عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند
🔴
از آنجا که‌ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد
🔴
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود
﻿﻿﻿﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/131704" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIYKnCFsitnicjchj1lmbm0XgEyMIagtr4VU6xuSiil0KzfvpabPK-pYii323d8dTBoLzadd2xO4SKyY8GirwU2Bq0MBTGEp3OEd1rmo1uq7JVjTxORDJq8Nk47qSNaL1_inG5EvIscs2WpLl4br2glGd49kO_u8cljGgsxh9uAfPw1k8krKN5Z_gdXabVlIJy6fF1cePOHPNpYhjre0LBJUwuRXxG8QMTG5ItCyRW_FKK2fvyI2rOAj_MjnHDKPLyelUAhTEXhGyE3ZjwskMwcJLl7RzrWHBY-q3bOTdDmbvZmB08ItWlHBkG2U0qPGSKqnm7s_Ap7l4Lmlk_Y97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت سنگین نیروی هوایی آمریکا در خلیج فارس
🔴
نیروی هوایی آمریکا در حال اسکورت کشتی‌ها در آب‌های عمان و جمع‌آوری اطلاعات درباره جنوب ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131703" target="_blank">📅 10:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
🔴
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131702" target="_blank">📅 10:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxieX523kjDauR7BsGGOUVHRzQV09HVLzCYDcWIhjIwojRRCR35iLjJHojglfrV6MyxZzlUVF_4lZZotKnTYhH3t0Db1RORinu1R83-5y04re_3EjvLJekTN8TP2CLPQW7EusI6RfFsALoNgiti5fVTVkMabhC7SVVDKP-3Fh_contz3Z26Qkbrn1DWP-SXdmtfgUBTYr60EYh1r6vUskL9MWB1sU8qBbMnImvGUXa0ehVG4KRruLMYLwnrdjciRYPqK7jXYLHLYiwQwtIckX-_VWWuwAx-3dVvASaq9qwIWlYJoYBau_Aelz_63SAwC-gqQGzTJNijw8rvYeo79xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار غریب آبادی نسبت به هر حرکت نظامی در تنگه هرمز
🔴
معاون وزیر امور خارجه در واکنش به بیانیه مشترک فرانسه و انگلیس: تنگه هرمز میدان نمایش نظامی قدرت‌های فرامنطقه‌ای نیست. ایران به‌عنوان قدرت مسئول و ضامن امنیت تنگه، نسبت به هر حرکت نظامی در این آبراه حساس هشدار می‌دهد.
🔴
امنیت هرمز با دولت‌های ساحلی است؛ بحران‌سازان مسئول پیامدهای ماجراجویی خود خواهند بود؛ این هشدار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131701" target="_blank">📅 09:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گروسی: تاکنون نتوانسته‌ایم به تأسیسات هسته‌ای ایران دسترسی پیدا کنیم؛ این موضوع به مذاکرات جاری میان ایالات متحده و ایران بر سر تفاهم‌نامه گره خورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131700" target="_blank">📅 09:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرنگار الجزیره تأکید کرد که تاکنون هیچ اظهارنظر رسمی از سوی واشنگتن منتشر نشده است، اما رسانه‌های آمریکایی به نقل از منابع آگاه از وجود «تفاهمی موقت» میان ایالات متحده و ایران برای کاهش تنش خبر می‌دهند؛ تفاهمی که امکان ازسرگیری روند مذاکرات را پس از پایان مراسم تشییع رهبر فقید ایران، فراهم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131699" target="_blank">📅 09:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مکرون، رئیس‌جمهور فرانسه: دو شناور مین‌روب را به خاورمیانه اعزام کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131698" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGJjwxtf7iYr2VbUTILjnG3fW8vbs29wkIjue4tSCMX2zjsNdRGpn4STzJJ3YJF2gstmli72EWTnClQPaSZz7_5GENyqf4PXYZz6o82OoMn-S2nMII8epdLRcLCg1gAgpW_jSgNZNvhGYIi6ry6_r-uvrwJdoJr8KS9ZymU1DXloY0b34tqlmseVIRtf6UVIOiqlsRa3z2TYvi1yWpDuJcXVjVzSwcqdH-NAtTwIZ-8PSiioUQOYkAnNZD35t__OGmEUjEcli066_sJZecP98H9xAtlj3tVKJZfz2d2eLm48n81AXq1tPOe2DnYt_FLlAq8RKSWhL-L22SJDEfOQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی از پهپاد انتحاری دوربرد «SKYWASP» رونمایی کرد
🔴
این پهپاد توسط شرکت SR2Vector توسعه یافته و برد عملیاتی آن حدود ۱,۵۰۰ کیلومتر (۹۳۲ مایل) اعلام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/131697" target="_blank">📅 09:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
فرانسه و بریتانیا آمادگی خود را برای استقرار یک نیروی چندملیتی به بهانه حمایت از آزادی دریانوردی در تنگه هرمز و تضمین عبور ایمن از تنگه هرمز که یک موضوع با اهمیت جهانی است، اعلام کردند.
🔴
فرانسه و بریتانیا هر دو همچنین بر تعهد خود به ثبات منطقه‌ای و احترام به حاکمیت همه ملت‌ها تأکید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131696" target="_blank">📅 09:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lRZNcM57R9BtrxJCPDuxLVghPmEcZvoFdNFskEiaK7fpROzBpzN6QezYxSVcxqhysv1tTgGbmc-Ynx3MO1QGaujD_PAWKT8mR_P_KlpA_jxelC-HDImnW4vD0B1BYuR-xT9V3HPQzS5GMT_0x5kLrASs0Nq6Fl-vZU2E8UYsLqjuqdmGrbg-gEoQ2iU-VV1PEHix13aWewlYrt2bQeb0pLWFuWtNtf4GX6ggwkbvDq26btQdR2rWhG7DaQS9QFp9kIlR6r5lcDyxF9QrgPKkbyMjH7sTDDJKxwnZH6oDAT_5X7fgpqTjtGiNms2C3X5smGBzhGHvGfNrnMJbiv52Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی اسرائیل در نزدیکی تپه استراتژیک علی‌الطاهر، در جنوب شهر نابتيه، لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131695" target="_blank">📅 08:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
متروی تهران از امروز ۲۴ ساعته شد
🔴
مدیرعامل متروی تهران: تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌صورت ۲۴ ساعته و رایگان ارائه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/131694" target="_blank">📅 08:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
منابع محلی از حملات توپخانه‌ای اسرائیل به منطقه «ارنون» در جنوب لبنان خبر دادند. گزارش‌ها حاکی است اسرائیل این منطقه را هدف حملات سنگین قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/131693" target="_blank">📅 08:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=M5PeEn7qv9-Jvnzflazn47EP1zv0O4prOGaqMZUw0TYZkc_OLa78WFAfqPowrv8Gg7KoR4H2plFR3VHn-g4M9pkZMWBX8WWgKjJYDCYZiCMFYvZPLmGohxSwOgKCtlsEOKIpAmuTvcq-0Nqx4I2_6LNhHifPGjz7JDTEAZ5nuhTJSgtG56KXbrnRWKyKlIYpc0LuS0TGNHGikEYj-r3yfcAKcQatiWrqiKl6Ka35gq9nvJfcd7u4I0YAUSPn0ImHg0bReG25yZoxs--r4ahUivk1wviGLJXkObu4VVCnhY6Fi2vXNzUka6tI6r_TNmGDEQ43oklt1Qdhq5HQEV7VlVz19BrXpMEzAP4mrlvNZNmJTfcLYVhaKAb9UY92I_vdjm3WpI61BQjP4NbYrhoURq7wkjkxlpSiJINXlaOdgfZHRcwoIRdzOnanZqa4zh0LSoWlgxyU7ymPN-vKKTqunly3cllyB8p-OGeE06lLXH7kCgMOV7dT-0J1SaHjOko58Oho5w4xF8gaL487ccDlI1lfv-ipGsDNrBi0FKdvWyzT8vNokDktB3eGQTPnC_2sJa-SqpP4L0-YM2dzm40Eez5islWZ0nM-ORN-EbZowid1nl5K-bebAR8DxveDAalb3AU6lzFeWgrU3C_SdFTF6WPqWIEljzvjO6JfpRWn1q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=M5PeEn7qv9-Jvnzflazn47EP1zv0O4prOGaqMZUw0TYZkc_OLa78WFAfqPowrv8Gg7KoR4H2plFR3VHn-g4M9pkZMWBX8WWgKjJYDCYZiCMFYvZPLmGohxSwOgKCtlsEOKIpAmuTvcq-0Nqx4I2_6LNhHifPGjz7JDTEAZ5nuhTJSgtG56KXbrnRWKyKlIYpc0LuS0TGNHGikEYj-r3yfcAKcQatiWrqiKl6Ka35gq9nvJfcd7u4I0YAUSPn0ImHg0bReG25yZoxs--r4ahUivk1wviGLJXkObu4VVCnhY6Fi2vXNzUka6tI6r_TNmGDEQ43oklt1Qdhq5HQEV7VlVz19BrXpMEzAP4mrlvNZNmJTfcLYVhaKAb9UY92I_vdjm3WpI61BQjP4NbYrhoURq7wkjkxlpSiJINXlaOdgfZHRcwoIRdzOnanZqa4zh0LSoWlgxyU7ymPN-vKKTqunly3cllyB8p-OGeE06lLXH7kCgMOV7dT-0J1SaHjOko58Oho5w4xF8gaL487ccDlI1lfv-ipGsDNrBi0FKdvWyzT8vNokDktB3eGQTPnC_2sJa-SqpP4L0-YM2dzm40Eez5islWZ0nM-ORN-EbZowid1nl5K-bebAR8DxveDAalb3AU6lzFeWgrU3C_SdFTF6WPqWIEljzvjO6JfpRWn1q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در آمریکا، ما به زبان انگلیسی صحبت می‌کنیم، زیرا این زبان، زبان بنیان‌گذاران ماست. و برای هزاران سال، این زبان، زبان آزادی بوده است
🔴
یک آمریکایی همیشه خواهان صلح و آرامش است، اما ما هرگز از خطر یا تهدید فرار نخواهیم کرد. ما همیشه خواهیم جنگید، جنگیدیم و خواهیم جنگید، و همیشه پیروز خواهیم شد، پیروز شدیم و خواهیم شد. ما باید این کار را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/131692" target="_blank">📅 08:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: شما می‌توانید به کارل مارکس وفادار باشید، یا به آمریکا.
🔴
شما می‌توانید یک کمونیست باشید، یا یک وطن‌پرست. اما نمی‌توانید هر دو باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131691" target="_blank">📅 08:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=f6lU_bd8BnYE4r4OHQipMUJHW7XgrbZRsMmBuGDGD3K6NzvqyUIY5wQ943s9vI4K56kGmJvPboGTAxarRaODpH6UbzzttsefsEF3EnV0u6_yy61PFDvvtX11pFmB5wF_tteVVw3Jgm72FRJhKc6wNyQb47FpcrFhut4MiRAMWFqvZDUrrV9D2FWqmJnDuAKRVPTzwSnulckErvdoJa5bOuID-_xBX774FaMrdkCrLxHC6WRiUCX7tNWC6rzHLh3W31xOC7fqr9DmKPbJ7WIYoC6N7Gp4jTJwi6jHVB6U7sP17ORZbpyaEHqMtAxwWmAYj9bftJsxELvlGvANT5uJDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=f6lU_bd8BnYE4r4OHQipMUJHW7XgrbZRsMmBuGDGD3K6NzvqyUIY5wQ943s9vI4K56kGmJvPboGTAxarRaODpH6UbzzttsefsEF3EnV0u6_yy61PFDvvtX11pFmB5wF_tteVVw3Jgm72FRJhKc6wNyQb47FpcrFhut4MiRAMWFqvZDUrrV9D2FWqmJnDuAKRVPTzwSnulckErvdoJa5bOuID-_xBX774FaMrdkCrLxHC6WRiUCX7tNWC6rzHLh3W31xOC7fqr9DmKPbJ7WIYoC6N7Gp4jTJwi6jHVB6U7sP17ORZbpyaEHqMtAxwWmAYj9bftJsxELvlGvANT5uJDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
🔴
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/131690" target="_blank">📅 08:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-IxIbdPuk27PF-F29XmIGwuQwEdzuI8-3ehHb7lBFwvuOZ-bh9heBYlvuqljXTcdsck-GH03quZoWpD8DFsxLQ1LWSSg1eiiJgVH-Xk54IU9eb7BLigGx5Q25xuHuUwgTLSM1duF9EV0XYBFvx_LcRSzijxUxU67sr8_lA7PmuttpF4SNbaEbcBhn2kL2PO--_g3s1CxDDaL4lat2Qfe7LaD1vnfOKZx4pEOpnkzpocMuXY9UIlzkNKGIgJg8Wj3Fec3riNBnCCtTze0C9eX4YBGrEOt3u_UsUXC8xr8EVyY2pKK1FLcRzjAABX14uz1Y716LjF_BUu0V_5efLxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بزرگترین سایت کاریابی روسیه، برای دفاع از آسمان مسکو از دست پهپادای اوکراینی به دنبال استخدام داوطلبان اپراتور پهپاده!
🔴
وظایف این شغل شامل آماده‌سازی قبل از پرواز، شناسایی و جمع‌آوری داده‌ها در روز و شب است؛ تنها مهارت‌های فنی اولیه رو هم داشته باشید کافیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/131689" target="_blank">📅 08:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prgNmX9H2Kr_Tj3vw9zhkbLcvRjDX1E98_vQm7-eFKNR4RnYZa-89JBCfKoS6JMvk4WAjFbeQQzGMapOdBeTnyhPzVQ-xYfLi1ICDIFkk_7PrwP6INwlbK4U35M6G2t9uIrmg1ACnUOSDUqjQs-EsVOSQQZ3-mjDNRQGmRMmnqR35m272pYB5ZWsTpYCqkLA4ekyfII5nseIVPd0CP5LBLJQOAYyzy71C65W4R51dGqfpk0Vl5eMuMDBRWoL23IXFJOODms1G-81sHtlv6c4KoFkOsZsRZ1nhy-THzX9nye_363X7iNdesFCC8ZQaE1U2aZdNsEWBeZDWr_zVZkgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mk1eKhpx_A6YTa5gl89rretYos67CqV66s8Qp9UyOSeUS7njvbY1ANha_dgIVrTRMRz5BhfwujEMN7p3jpu7A2Dj72W83RZBgjeHCPtODbYm34kiBHJ4DGdHdyFutlcavwGSVJwFyitSeVZTOREmjsEsg-LvbSf2iInsj6ed9UaH8Z1gDz4sOc538qLP6inYGKGlkk2v8tv2dZq8MQnzGn70Y6aRTnckisCCEtKB3nQHZcF7tExlZc8sn1x15LK1l3oy9d9EJ9IJCRd9ZNTM4bv1GdaDjjkepRK7QGZHkY5J8yYS2LwYnO52Ns3LqwrMrW1DH_ZH8SJbkl8B_LJqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3HwToLVxFasxwAh44xLl3CS17vz1RHoMKsf0KjnFLRhZ2evvH3_qcF1OQbga8QOEpUSFf7tKxvdBhw9jp3phMUslPyQzz38VvzBdkBnnLhRB49GO6VVLvP08_srv5dwUl_cjbwjjpC-05U7GLXzHf379ZadtC5lSZu92qhIjhzFVB0HoIw_e_b3qJzhTTHtsJb26FmTW9neRca5yMszJkCPGCaCPiMiI8DLUqDmh6e--xyREWI3B8XVRwcc6eQABohvekBrVCE1InyRinea0t-e_iRAIbli2MOoqboN6QCUn-2Y0eeKPvbW-T9g8VecR4FjwNXEOjaAZ3Roh8ZJ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/131686" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=KowiR8ryM0fUyiyUN_DCZttg9H_gmUuBgBnKDTGbPcxgxZQA-q5aXUZmcAx2x5LgmieiBxM2Dwfx6xJ35KjqghySdFaPzqchTvRdp5C9vh9UFhEu56NlQ14-Ps2kkVABx6M4Br7s47ATIKT_3O9P6UHuvrGHDBVBK5ed-Jx0JJ_gvYt7aJbOQdL1zVJRuMvUbFi8BG36C9MSoTXctWgevLbWwb3NYQV0Sm3sogv6x0Z0v5T1HJoP4o5TR-5IzgN1n32s-VdH4-yNSXY_eM1L5-_YdJjzu9x1f549psgyEEtMDNNWcu592D4afzehc8U0QCe5LnLMYQ9uba_R5iRXCoZCcnatS0e0qv8c-M1swIE-XffSHPzJLtglec0l-El_s_xAa5mlTanmGfH2VD5ldaey5WkKS2ZIycfZVr08W7tzbCFQGUt0Cu-_DpndbIuNh6wn7DZfrg5Uu5DxHWJCAnCq-E7Zl-E_UNIg4XUS2F4deoNi05WlEawtSpFAwm9Nma7NicQPuCp4oxvA3HlwqLcy0qqrxI2wxgKyVUta0sbkw-n9pabIOCbQ_E_nuOptMkSNkkEDGC9svpyerLTeeGeUHfffIto7XMw9MFXvHqTrYLBCUlF_Nls9EpB8EBw5cNtHMDlFYVR1fmOdMzsekUrDnyoK4pRrUTZdvNHCHhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=KowiR8ryM0fUyiyUN_DCZttg9H_gmUuBgBnKDTGbPcxgxZQA-q5aXUZmcAx2x5LgmieiBxM2Dwfx6xJ35KjqghySdFaPzqchTvRdp5C9vh9UFhEu56NlQ14-Ps2kkVABx6M4Br7s47ATIKT_3O9P6UHuvrGHDBVBK5ed-Jx0JJ_gvYt7aJbOQdL1zVJRuMvUbFi8BG36C9MSoTXctWgevLbWwb3NYQV0Sm3sogv6x0Z0v5T1HJoP4o5TR-5IzgN1n32s-VdH4-yNSXY_eM1L5-_YdJjzu9x1f549psgyEEtMDNNWcu592D4afzehc8U0QCe5LnLMYQ9uba_R5iRXCoZCcnatS0e0qv8c-M1swIE-XffSHPzJLtglec0l-El_s_xAa5mlTanmGfH2VD5ldaey5WkKS2ZIycfZVr08W7tzbCFQGUt0Cu-_DpndbIuNh6wn7DZfrg5Uu5DxHWJCAnCq-E7Zl-E_UNIg4XUS2F4deoNi05WlEawtSpFAwm9Nma7NicQPuCp4oxvA3HlwqLcy0qqrxI2wxgKyVUta0sbkw-n9pabIOCbQ_E_nuOptMkSNkkEDGC9svpyerLTeeGeUHfffIto7XMw9MFXvHqTrYLBCUlF_Nls9EpB8EBw5cNtHMDlFYVR1fmOdMzsekUrDnyoK4pRrUTZdvNHCHhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس :ساعت ۶ صبح بیاید مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/alonews/131685" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/667106b64a.mp4?token=M5LSrGL9jgMO419QLo-uI7LDkh9xqjokKUrYEAYOeSIcsCzWzqOGFo0lAY-8nLKS2fxRBVaMQMdzqyl7RSNFOmCS3LHpPeabIEuw0em2rWjraxLfDiOztbBcqrvss86GknikbaclKA6eXgWHQs-H0XehzrnL8854gy-d8DtOmKSkel75Qva_o_xjpcp6xLro02fuuhzIy-4V4mF6UNkLyqqflJ4FdQQ0oY0eTF6jYpuqjx4_yzQC3ZnNg1pVzGlI7dg-KhAfTgGCor-UzFIyBTpSN2iP5c9JmHFXxrpJqKXBB5vq-hZw-1wyCBL-reBieXIrhiCtDpWKazPoLE7RG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/667106b64a.mp4?token=M5LSrGL9jgMO419QLo-uI7LDkh9xqjokKUrYEAYOeSIcsCzWzqOGFo0lAY-8nLKS2fxRBVaMQMdzqyl7RSNFOmCS3LHpPeabIEuw0em2rWjraxLfDiOztbBcqrvss86GknikbaclKA6eXgWHQs-H0XehzrnL8854gy-d8DtOmKSkel75Qva_o_xjpcp6xLro02fuuhzIy-4V4mF6UNkLyqqflJ4FdQQ0oY0eTF6jYpuqjx4_yzQC3ZnNg1pVzGlI7dg-KhAfTgGCor-UzFIyBTpSN2iP5c9JmHFXxrpJqKXBB5vq-hZw-1wyCBL-reBieXIrhiCtDpWKazPoLE7RG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موزیک ویدیو کامل آهنگ جدید توماج صالحی به اسم «تو چی؟» که تا تونسته به رضا پهلوی دیس داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/alonews/131684" target="_blank">📅 01:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131683">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم  «تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/131683" target="_blank">📅 00:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131682">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr7MO4F-TR6nK1AW1Qaxwx1tuNYzwS5ZaYLLyKC5bPpDmNIrV_dZr3WmPW_n7vDtmFNCIrRGuyo4_DTxay7y02269vEYissf5IJxa9kwXthMRImvnPu6dGyv_39HiJBd7QNMxTEJXJMQyPN4mQlTSXQUifvrtHP32N0rvUfP2cXQQ7JKCzsnfZoJe6dJd-hYQWp9XL46oOJexI9n0efLd1ENePwBF3iJIjIlVYqh7GHD5FI914aR_nA7q9Vp6fn_bV5Fww0h0_oKi-q7ZYL5mDoSXXRyPJ2QlPHo0y2aZvIaetVQzZynyJJP5Sd0ghhu8kUs3K5ZtRl4R0k7Jvj0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/131682" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131681">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=t_NYuFYLGA88XYst7zKwTDLmzaQt5A7jF8o6xUdoHPtM48L1g9pS9S6IxHIzp0pSG92wvS67LvHOj5rlLeJR6w11ygJUsNBwGEt97627WlekULl48Acbtqigka_AkYqEjQu18H_f3Tn7ZHKQ9UUZaEC3DeR53J_ALBaYKtDejNz8ojBx9gNJuLRAY_B-6W6Wb6ARcj4jceCyEVBTtpjTsznq86T0j8e1g59dEMkO_6FSVRsFIvSe6d723YRUlgLOk4mPaciaCapDnHe8OMJfPsflDhlTaj3rF3GGZmQhADQKjFYMyAyCKhyz174rhYd9GW_r43ZTZEaftmOh7a5_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=t_NYuFYLGA88XYst7zKwTDLmzaQt5A7jF8o6xUdoHPtM48L1g9pS9S6IxHIzp0pSG92wvS67LvHOj5rlLeJR6w11ygJUsNBwGEt97627WlekULl48Acbtqigka_AkYqEjQu18H_f3Tn7ZHKQ9UUZaEC3DeR53J_ALBaYKtDejNz8ojBx9gNJuLRAY_B-6W6Wb6ARcj4jceCyEVBTtpjTsznq86T0j8e1g59dEMkO_6FSVRsFIvSe6d723YRUlgLOk4mPaciaCapDnHe8OMJfPsflDhlTaj3rF3GGZmQhADQKjFYMyAyCKhyz174rhYd9GW_r43ZTZEaftmOh7a5_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم
«تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/131681" target="_blank">📅 00:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131680">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت
🔴
پ.ن : تاثیر گذار بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/131680" target="_blank">📅 23:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHfSEUL8cMjBdK_Yfpq29DV06RvfUJHpxvCuTtAKCX2cGyU70kZeD0sHwAJUgRlraooO0xf3w2wPm_yBkeLtblvlQyHWEQuE2TKFRLA9z7ueKfGXsEFEDRTT9Fg--SnjbnsCy4yIBGYqk1J8Txz1ZLp9fYj2cutdy4DM_E5YDgMco_EiDhLHNsLtTMMVd26-1p6Z5JxAiTNvF8yA5kNtgfWsBZ-n6t_53BxnNlm_lC2veIVR5DYgq31kYDO7U1JGHtM6LlgohJaAfn9ecs0f6YVrdRZetxl95y6YIM93iy7Zi4vDiQkpFjHAwvJj4uozkVVKpDZLnNe8dSWXDhNX_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر پاکستان بعد از ایران به ترکیه رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/131679" target="_blank">📅 23:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/131678" target="_blank">📅 23:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/131677" target="_blank">📅 23:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJIiozo9CPj4nSwkmCMwye_KwHL2luQUgk7vx-3LNh5GSXTrlIpEEZmpnOlnGzyjpOfOH2HXMQo6QjQ312U_xdUyAahsNYHSHRLPCNhPpHNO-26-k-rLNY_smVPjla1XJkUOCTA46sSMZxGs4w2DLEnJm0-b636OURiNteuD9DUVJ5AR2KWd50XL4PAgzdN5xWGryIqQ4VYzK4bleLxGyy0M5fumCW6TeoYPJxqnPWGGllEWrgKEmvlSPEd3gkCaMrPzBNJe5CjWbYBRRdwak85WIaWyISYZAJBCWfZ86qXLa10IkJV-xUl6zrDGDaFauJhq6QpZkN9WgOYY9jHbvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به فارسی: ابراهیم ذوالفقاری چون تو مراسم تشییع رهبر شرکت نکرد،پس صد در صد مطمئن شدیم هوش مصنوعیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/131676" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE6pL8JTXLsN9Kmdx_EZ4VE_T173NBHNQc2sFQMIsU0iR2Z5xY1BKXQ-YPbCqEQdIgsdSQZ0Gpg2_-7W4AUjnPrWvAzB7slpdlCZOYkYa7KjIu-WnBl2XQjN6Jb12XlVpaer3z_CSNxYqueRzr_sFt6KMi0PAKm9U4Hk40uyWk_GwjExuhukvBHKknxL22iJ97BhF8IQ9mN2iwiz1KWhfmN1PL1usy9XYrdbiiw0RbG48qC8yAKplnes3KSEW6dcJNPgJef8ZWkGbi8ZgXRXg0QX3_MJKSU7Gur6v8EDFDOyXa9jNZ1TKJYJDlDWuE5iCmDfkfoHTvtGojuAF5Tpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/131675" target="_blank">📅 23:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=VhwaJErar3gI3Z3eI12lKpGj6reWQkp69OXV34_m2FKUoatpdUHJU5-ZNzPi1eMpciCAmixVlnNBeSN3XjOMUs3E6pLwEImOhnGd1njumzhVUa5hZlkAYxhuzKoEE3F6-q1OadlAHoG4ZyTnbySEqGN6g3jCsXgnogHQGAfJ9PIyN-1l9yT31zGpdKyIgwNQ8Unq_wzy-eVt8LWp_wwuTgSfzzfIH_aEslCQp9eE5w7woe276TBIIJknS2smsielRNNM8VhN9xtD4eGdObqbmF2xeCIIyll8il4MKrwLsIb4LgDXaZvbz0VIyvHJeKbtYKrzLeIDVhhjMVv7Ol3OKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=VhwaJErar3gI3Z3eI12lKpGj6reWQkp69OXV34_m2FKUoatpdUHJU5-ZNzPi1eMpciCAmixVlnNBeSN3XjOMUs3E6pLwEImOhnGd1njumzhVUa5hZlkAYxhuzKoEE3F6-q1OadlAHoG4ZyTnbySEqGN6g3jCsXgnogHQGAfJ9PIyN-1l9yT31zGpdKyIgwNQ8Unq_wzy-eVt8LWp_wwuTgSfzzfIH_aEslCQp9eE5w7woe276TBIIJknS2smsielRNNM8VhN9xtD4eGdObqbmF2xeCIIyll8il4MKrwLsIb4LgDXaZvbz0VIyvHJeKbtYKrzLeIDVhhjMVv7Ol3OKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین یبار دیگه با لباس نظامی ظاهر شد و گفت که نیروهای روسیه ابتکار عمل استراتژیک رو تو خطوط مقدم جنگ در دست دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/131674" target="_blank">📅 23:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131673">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی کرملین دیمیتری پسکوف:
پوتین دستور داده تا به دقت تحلیل کند که کدام از متحدان کی‌یف در تحریک ادامه درگیری‌ها نقش دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/131673" target="_blank">📅 23:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131672">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2dD03DEJDG7mOXBAyzNWumJRIZFeu4jK0tmg8nAILa-91kEBCdqQVaCVryA5pPBmOiC6yR38Ftx71VbaWfIaVcpH_sts-QtMgjSrPKsUjr_wHtDj47egOc3EonyD-a-C8ddbyapyPmqLntEjZkCPZarDFNy_rcBMYeHvzwkORRNopR61u0t9lcI1xFvgb99ZojytJth5WTB1yczdgvkxLz0n3JN1SxnMB-8Mgds_vzl6AY7f2PrlQV1X3vwnRj_C09Sze6GoCDxAnfnUb23nbGM5PbrmVxLUYYBlD5c1zP2AiALIlT4jU2_d0CZ9RTQRr39-pEuOfh148Lm4KAHWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: افتخار بزرگ من این است که همین الان برای شش نفری که توسط دولت بایدن آزار دیده بودند و در زندان بودند یا به زندان فرستاده می‌شدند، به خاطر «تعمیر ماشینشان»، بخشش امضا کرده‌ام.
🔴
در حالی که می‌دانم این موضوع مسخره به نظر می‌رسد، با این حال یک واقعیت است و بخشی از تسلیح‌سازی و احمقانه‌ای است که کشور ما مجبور بود در طول چهار سال طولانی خواب‌آلود جو بایدن تحمل کند.
🔴
من همه آن‌ها را همین الان آزاد می‌کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/131672" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131671">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6ccf94e0.mp4?token=XFdPyizZPq1Z7yO_UyFd3JtJCLiENwiauUXs9G5CG-mVGyK5rnZ0-vJn2MFnJX1YxwzwEbHoUYyJ99_zP6Ja1XSvJ68_j-2TSkkbd5uIcaRU5xRAYQplsYhgN3Xae0a9elk5kIbMHNNKlkHyEN0hKceHro4ZmYWu1ov2dYJ7gxd-BHs9qW18K2e0LcOJ3rv5hen8DkHUY3nKxFrwDkUBB1AvVCJ-ijB1UQYDoklFvbsNQtI46uH22-yuMPuRLrlmxYkvP7TQPcJKtvO4vx8FGU-YCI5ZTzQroh5BAPEr7Dnp4VTZ7UiEx8ehGihkE5UmdPqWX-EGTuJAq6UVoWevNZePpRLYZ9Yd8dLl5JIBIWKQzO7w0BEjraUIQEhMaRguE8G4hpYT-BJC2BVNpYvUljtcjF8Dn4x9TQ1DNuvjums1zt5M1aAIHyje8QjGqwBN8Te-78hiy_xKaj3dMuavOSWmvdQiwEsBJeS29QgjPFJ7gPlewBxTL09v9IBDP4k3fcqIXdeeySarvmcn4MiJztFA4E6mAlIeOcI6wgqmuFAGmAYHXsd3jWTh9-n5bl-fkp919R_Amt5P39AgCCVR9JINIozV2bip2hantKmTsUNgRvrb2UOBzMTFuypixSNbGHsaK2eXoCLH3UIIbHzE5j9aFdUrYPvjRyWMfu7w58k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6ccf94e0.mp4?token=XFdPyizZPq1Z7yO_UyFd3JtJCLiENwiauUXs9G5CG-mVGyK5rnZ0-vJn2MFnJX1YxwzwEbHoUYyJ99_zP6Ja1XSvJ68_j-2TSkkbd5uIcaRU5xRAYQplsYhgN3Xae0a9elk5kIbMHNNKlkHyEN0hKceHro4ZmYWu1ov2dYJ7gxd-BHs9qW18K2e0LcOJ3rv5hen8DkHUY3nKxFrwDkUBB1AvVCJ-ijB1UQYDoklFvbsNQtI46uH22-yuMPuRLrlmxYkvP7TQPcJKtvO4vx8FGU-YCI5ZTzQroh5BAPEr7Dnp4VTZ7UiEx8ehGihkE5UmdPqWX-EGTuJAq6UVoWevNZePpRLYZ9Yd8dLl5JIBIWKQzO7w0BEjraUIQEhMaRguE8G4hpYT-BJC2BVNpYvUljtcjF8Dn4x9TQ1DNuvjums1zt5M1aAIHyje8QjGqwBN8Te-78hiy_xKaj3dMuavOSWmvdQiwEsBJeS29QgjPFJ7gPlewBxTL09v9IBDP4k3fcqIXdeeySarvmcn4MiJztFA4E6mAlIeOcI6wgqmuFAGmAYHXsd3jWTh9-n5bl-fkp919R_Amt5P39AgCCVR9JINIozV2bip2hantKmTsUNgRvrb2UOBzMTFuypixSNbGHsaK2eXoCLH3UIIbHzE5j9aFdUrYPvjRyWMfu7w58k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار CNN که مجدداً به تهران آمده است، از جزئیات مراسم تشییع  می‌گوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/131671" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
بر اساس گزارش شبکه NBC، حساب‌های سرمایه‌ گذاری دونالد ترامپ، رئیس‌جمهور آمریکا، در یک روز قبل از توقف تعرفه‌های بزرگ، 327 خرید سهام پنهان انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/131670" target="_blank">📅 22:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131669">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/131669" target="_blank">📅 22:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=oDP9NsxT1OJ1VQh9GNI3G67YEKJ9-PaulGEGUDpK8vKCQSzmBVB92jn1h0_Xik5KVoIllI8G6V8QTVtElK1tGLx8ec5u4G-canz4ETMvHiP64oYylMJNU5EylldGSlZNjN_iyyzbiZh0sCJrX2ujcfhiwShlScHBr0r3DPmV_iZ2T6Jy65dPqZinQahOtxtU0-eE6dDJkNmhp2pXIKjPuiQIHI_FFtrv_nEPNHPN8DcV7oIatacAbV-RmQkfUVyGXPmnxMNtWu6cMzX3Irzoo6Cl0cXErVcKeWQVhnJtBTTgJf_Nsc9own0AaeetSwccHNbdA8AJm6xNkX3tkpnmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=oDP9NsxT1OJ1VQh9GNI3G67YEKJ9-PaulGEGUDpK8vKCQSzmBVB92jn1h0_Xik5KVoIllI8G6V8QTVtElK1tGLx8ec5u4G-canz4ETMvHiP64oYylMJNU5EylldGSlZNjN_iyyzbiZh0sCJrX2ujcfhiwShlScHBr0r3DPmV_iZ2T6Jy65dPqZinQahOtxtU0-eE6dDJkNmhp2pXIKjPuiQIHI_FFtrv_nEPNHPN8DcV7oIatacAbV-RmQkfUVyGXPmnxMNtWu6cMzX3Irzoo6Cl0cXErVcKeWQVhnJtBTTgJf_Nsc9own0AaeetSwccHNbdA8AJm6xNkX3tkpnmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های آشپز برنامه "به خانه برمی‌گردیم" صداوسیما که تغییر جنسیت داده و دختر شده :
تو 5 سالگی، یکی از آشناهامون بهم تجاوز کرد!
من کلا تو خونه پوشش دخترونه داشتم و این عمل، تغییر جنسیت نبود، تطبیق جنسیت بود.
من حتی دفترچه خدمت هم پست کردم که شاید از این حس فرار کنم ولی نشد.
تا 25 سالگی به کسی چیزی نگفته بودم ، حتی اون زمانی که تلویزیون می‌رفتم هم از همه پنهون می‌کردم.
2 تا خودکشی ناموفق هم داشتم چون اون موقع حس خوبی با جسمم نداشتم...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/131665" target="_blank">📅 22:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131664">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید کاملا مورد
تایید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
➕
با کد تخفیف زیر میتونید با ۵۰ درصد تخفیف خریدتونو انجام بدید(فقط100 نفر اول)
✅
🎁
کد تخفیف :
Express50
.
🤖
خرید سریع
:
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/131664" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131663">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
سرویس VPN (V2Ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
پنل اختصاصی (مشاهده حجم و تاریخ انقضا)
✅
سازگار با تمام دستگاه‌ها و اینترنت‌ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
تمدید و خرید مجدد بدون تغییر کانفیگ
✅
بدون محدودیت تغییر دستگاه و IP
🛠
پشتیبانی تا پایان اشتراک
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 100,000 تومان
▫️
۴۰ گیگابایت — 190,000 تومان
▫️
۶۰ گیگابایت — 280,000 تومان
▫️
۸۰ گیگابایت — 370,000 تومان
▫️
۱۰۰ گیگابایت — 460,000 تومان
▫️
۱۵۰ گیگابایت — 680,000 تومان
▫️
۲۰۰ گیگابایت — 900,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 1,150,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 190,000 تومان
♦️
۵۰ گیگابایت — 280,000 تومان
♦️
۷۰ گیگابایت — 370,000 تومان
♦️
۱۰۰ گیگابایت — 505,000 تومان
♦️
۱۵۰ گیگابایت — 730,000 تومان
♦️
۲۰۰ گیگابایت — 950,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 1,350,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 480,000 تومان
▫️
۱۰۰ گیگابایت — 555,000 تومان
▫️
۱۵۰ گیگابایت — 785,000 تومان
▫️
۲۰۰ گیگابایت — 1,010,000 تومان
▫️
۳۰۰ گیگابایت — 1,445,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 1,650,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/131663" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131662">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJAqD9TzCRsH-GbQH4pwnYyEQnX6xU-Yc4rGAIIL3boxuicqfEShwdhK83gJqMlB4cs-eZzE_9XE2uJA0okEENk3PsRh9uvJvWqfnn1MA9hPANdPUQP3Ij8yppMKPtIu1qRRbOqtCx1sc8QNhH7kLCiFM9XVDhrMvigmsp8f8NN04ZsJkUpnem9X9aiBxJZNOTd4I1HibRNIdAfk8ga_F59vpusQBFnP0FB547cMQs-3K1sH7C8ielEi4E8883TTAoNs9oJzLf_pZ9XtbkfTpBVnDi1H2MjdxtCPKi3t6Y4F5RnaOPhcfcKRdd6OlMRlW1JBm72S6OIbl5PXrpu2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف به ترامپ: به فکر سوء تغذیه ۴۰ میلیون نفر در آمریکا باش، مشکلات خود را به دیگران نسبت نده.
🔴
ایران خودش درباره دارایی‌هایش تصمیم می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/131662" target="_blank">📅 22:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131660">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
حسین یکتا: ترامپ که می‌خواست ‎۳ روزه کار ایران را تمام کند، هنوز خون‌خواهی ملت ایران را ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/131660" target="_blank">📅 21:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131659">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpiUtGk32TEqlV-smtw1JDGY6VZlQrd2bl7DzQSLEXExPdGXKOeaF_UdKcGRfrCs3mJqVFIZzIv1nE_w6RefTLjyYS92Xfp9u78AidqF70p4e_kWnbTQrbjcRP4jysiJg6E-FW6_Io7O5G1zZvmQVsEpd_T1CZ1z8JFJHyWXQY1-y4DxqMdn1FjReIqFySxzjf5ZD_PPTouGUqb6GbcKkrCX1ibInZilXPiFXpWXYdN9h_xvDQghKcOpb40xO6mzkNp2UEut1PWq3fXzcIvFnSdVPf2j5HI8EKuGECbKrHtsubco5tXbjXooqsaitL0w20QWuQvuZk02zj-76OPA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سال قبل در همین روز، مجله تایم عکس سیدعلی خامنه‌ای را صفحه اول گذاشت و دقیقا بعد از یک سال روز تشییع جنازه علی خامنه‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/131659" target="_blank">📅 21:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131658">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم: اولویت‌های دفاعی تعیین‌شده از سوی قائد شهید امت، دست نیرو‌های مسلح را برای پاسخ به دشمن باز کرد و پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/131658" target="_blank">📅 21:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131657">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
المانیتور: مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/131657" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131656">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سی‌ان‌ان: رفت‌وآمد کشتی‌ها در تنگه هرمز در حال افزایش است
🔴
هفته گذشته ۳۳۵ شناور از تنگه هرمز عبور کردند و پیش‌بینی می‌شود این هفته نیز تعداد عبورها در همین حدود باشد؛ به‌طوری که تا پایان امروز، شمار عبور کشتی‌ها به حدود ۲۱۵ مورد برسد. این در حالی است که پیش از آغاز جنگ، به‌طور متوسط روزانه حدود ۱۰۰ کشتی تجاری از این تنگه عبور می‌کردند.
🔴
اگرچه روند کلی فعالیت‌ها در حال بهبود است، اما بازگشت کشتی‌های تجاری بین‌المللی احتمالاً با سرعتی کمتر از ترددهای محلی و منطقه‌ای انجام می‌شود؛ زیرا بسیاری از مالکان کشتی، اجاره‌کنندگان و شرکت‌های بیمه همچنان رویکردی محتاطانه در پیش گرفته‌اند.
🔴
ابهام درباره خطر گسترش درگیری‌ها همچنان پابرجاست، به‌ویژه پس از آنکه حمله ایران به یک کشتی در هفته گذشته، عملیات تخلیه دریانوردان گرفتار در منطقه را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/131656" target="_blank">📅 21:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131655">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
باراک راوید: ترامپ امروز با نتانیاهو تلفنی صحبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/131655" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131654">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sjvxRwChxZlnENTiYYIYqVgpgKyQ1iwmatDP32YXVgd6VtbHIBILp1_qzzJKIeViH2yodaWIybDpe3E2Zi3pTyCrZJcNrIGt8KaTXnCb9MEoDSt34Qa3RvRv8DfUmtxU-m2OiVe8xFx9qhdqSNRDXxeoJoqETL5ER88gTg8e-uEsehXAkueDncBBAzIG-vL0tbVOgyFCysYZEE-L6wNg4-DkR6ZpJrCekeMK55bhnYDKUUI8A-AY_C2Bo67-a4adT7P66gL91VcdtEQ8CVsTiq5m5g93hwDfQ6gUyeQz2g_SJiYvkiSY2R9uLav9dMol875g6d11fUfHFnGdBb7nmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@AloSport</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/131654" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
