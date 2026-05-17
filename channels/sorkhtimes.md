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
<img src="https://cdn4.telesco.pe/file/IE5bG27kXYR0Bdu0wUPHBiFzapVxR5SwCFEF9X0LTbGX0Su0IVEz4wdvpHmzeP7lR7AxLqDWDhfjCDSH6IHPWBRR_RBomW6EAqeu0sXMfNCHGYTOzx0H3AekMGU0Ed0RLpzi2dk56Q2po0Ex5Wf_sbf50TGnZDS7s4mzTZj62RBOz__ylE1xDyvDADwo0M9jY00CXgTKccWW188vHlFtv2hwFUqjICXiLyHj30a07NlYESxnZJD21Z1lHp_Thx2A-n9i_MlqfURzJqPc7bu7kMT7nS7N-MNg93mEe638NJ6L6tccaQ5JpIqLlb9isyTrwxVtaGWV6PMYR4WytKQcHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 22:25:48</div>
<hr>

<div class="tg-post" id="msg-131805">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فرهیختگان: یه واسطه تارتار رو پیشنهاد کرده که اگه اوسمار رفت بشه سرمربی پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 124 · <a href="https://t.me/SorkhTimes/131805" target="_blank">📅 22:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131804">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 125 · <a href="https://t.me/SorkhTimes/131804" target="_blank">📅 22:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131803">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHs49cIhNuCLUDFrJdC17810z4TL_Inx-m7Oe4b6DXljSz0Gj_jL7xc1V_EVJirFKfr02ljvv9-Ulmao2VZNvW1raiRdoRDdQmDdaV3fQlb5Wetn22FLEbFNLTw8e5F8PZ85FqWCNQ0m9u8tgLzCJtE53n9hJX2rwjhQTAmMMqIXXniIWkaGZ41yf7pYNs6-FS2fMkUXgUXfl-NCiJlPRyIMoeY6k5NHKki-XMtMUpBBf0z8fryhwrgau3c7FPMq3BPf_qSval1LTwgGzsKrG8Ol33CxRs2l75ZZ95HMGfkkorlSjT6DoT_LqYCTMC7cyxYX_MXgq7hl8VzA1CK-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 312 · <a href="https://t.me/SorkhTimes/131803" target="_blank">📅 22:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131802">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
🔰
1 گیگ 220T 2 گیگ 440T 3 گیگ 660T 5 گیگ 1.1T
🔥
تا ساعت ۱۲ شب
🛜
مناسب برای تمام سایت ها اپ ها   جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 356 · <a href="https://t.me/SorkhTimes/131802" target="_blank">📅 22:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
ترامپ: ایران خواهان توافقه و منتظر پیشنهاد به‌روز شده‌شون هستم؛ پیشنهادی که امیدوارم بهتر از آخرین پیشنهادی باشه که چند روز پیش ارائه شده بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 360 · <a href="https://t.me/SorkhTimes/131801" target="_blank">📅 22:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
بر اساس گزارش منتشر شده از
CNN
سپاه به چند شرکت نظیر گوگل ، مایکروسافت و آمازون گفته باید بابت انتقال اینترنت از کف خلیج فارس عوارض پرداخت کنید وگرنه قطعش میکنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 357 · <a href="https://t.me/SorkhTimes/131800" target="_blank">📅 22:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فارس: محوز حرفه ای باشگاه پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 355 · <a href="https://t.me/SorkhTimes/131799" target="_blank">📅 21:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔰
آف ویژه
سرویس VIP
🔰
1 گیگ 220T
2 گیگ 440T
3 گیگ 660T
5 گیگ 1.1T
🔥
تا ساعت ۱۲ شب
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 492 · <a href="https://t.me/SorkhTimes/131798" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131796">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2FK0D3CMe1vOTt4cIADd6iOoV4PeqQpL3NQTIKXidF2Ot4N_KfSzRSBnZAvu7AWg-Dld9F7JC4dV87syr2w7pVV8JVmE9mXeiGGNnZRr1jShOvKupmEZONV-XlS2AqS8d0uoh9KxZL5OLkeSp4HquNoHWTno3yr_b7EDYvkUGdbJJJtyebxOCS_w8mxhF2GWc2rQ-geQvTz2LrQvSsmYQMirJWPM4233CSAiQ4MH9L2t_yXZ6BwwIAfw5NcpPbAnP4r3p6oMI59q8cfwKZjWwIovJUJeePkg64z7iE61vkhTcJbSAU8BdKv0NwaV_J18hwa3D9-l2aoYIu9Cx1qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ از طریق Truth Social:
🔺
برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند.
🔺
زمان اهمیت حیاتی دارد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 527 · <a href="https://t.me/SorkhTimes/131796" target="_blank">📅 20:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131795">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آف ویژه
🛜
25 گیگ 4T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 507 · <a href="https://t.me/SorkhTimes/131795" target="_blank">📅 20:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131794">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEoez3sSMNWSaznWQKzS-eZCne5G1uLsedrxYS9eOI6EkF7pbVrcevBsqZ_yrCasyBI-0gCqJ3bk4yrcIEvw1awKw5v_BS32Ltz5PIsF64Y3bj3on8STDgTPQupOhi9w-tc0VuocG-v8lM7pbm9soA-pvDwxCxlsAJ748wriZ0KccsocO4SnLlB6Ab6hoW9avEli6VfrK8qgumaW1b1MzszQW5InDHrQssUX_slEP-r-oWrkdk6ETAawqXHfStCF7S6IBEO8lWdxz0sh5wVZZ3SR6HCIA-QBTZzUJd8suwRVc5tCgkNvtCYlSxQ0jdMEu7Y4XvPAz6s6_qg_3V1kXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سه سهمیه مستقیم لیگ نخبگان برای ایران
🔺
با شکست شب گذشته النصر در فینال لیگ قهرمانان آسیا 2، حالا فوتبال ایران برای دو فصل آینده به‌صورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود.
🔺
در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات دوم شد و ایران بالاتر از قطر، رتبه سوم غرب آسیا را حفظ کرد. بر اساس سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 570 · <a href="https://t.me/SorkhTimes/131794" target="_blank">📅 20:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131793">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNhD-ZJDTLqSMWkUPLzascbH00y-Ty3ywTmrCOfYsc5Ng25Ewp9CA-fhC_euQZOogAWIRb8W0ec7uZ52jd3eWjpLux4dJSx5LgaTRwsgXkfZIInHSXh3iuM_C6E9WqO6g8SOz4BIvFCg9jgw8jJtojXrbH3s6jwobPDMw6ndwjwfSxZFQRdYYIwYn2RESWJ2MzaH9Bgv1S2uzDMSgTq1EcuY5l7020dW7th-6KkvajiruVV64bAuKdbId8wY5T9-Fm3AqpO6uuRI69Lns8xDkxyPXUMmexKyXpxRX7ACepP0PmjvKFTjrWHLbFQlwPAob6HMFjhqQCJzTOHfwc5r9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
استوری باشگاه پرسپولیس به مناسبت روز ارتباطات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 526 · <a href="https://t.me/SorkhTimes/131793" target="_blank">📅 20:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131792">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
ورزش‌سه: علی پروین بخاطر افت فشار ناگهانی در بیمارستان تندیس جردن بستری شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 492 · <a href="https://t.me/SorkhTimes/131792" target="_blank">📅 20:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131791">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHJeNmsmktP8ysAW3zPSxv_DHQPLrgPq8Xz_Ww0NscESaa_aE054gsPqEG9zA2Y7v872D2fprkpfTm6BpZmykDXJI7jiuhZVzsDdY8Ojcd5373MdG9YbdlFK5YHLoKLofloaqUbjOUOroEJ5vxbAzjBU2CB7yXExNH0xNC0m1cAaVGmh6uZhtCbylQN7sS9O9QnA5CkZlkP16ja98Pv8XYnp95F09J1Bek7KIWtJgdnph1eLL3mCSoQ1swaaQS5dUe18-kfxPDLJzsiHFwZcsq73apb4PiubFmmmFYQNlvDg6EHJ7cDF0k335EbCQb3ub9dG9fhDWrv4x40bZK9eLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابل توجه کاربران محترم وینکوبت، تمام قابلیت‌های سایت یکجا در
ربات وینکوبت
در دسترس کاربران
قرار دارد.
📌
کافیست با استارت کردن ربات و زدن دکمه‌ی وبسایت، وارد سایت بشید و به‌راحتی ثبت‌نام و پیش‌بینی مسابقات ورزشی رو انجام بدید:
👇
🤖
-
@Wincobet_bot
🎰
از پیش‌بینی مسابقات ورزشی تا کازینو آنلاین، بدون نیاز به خروج از تلگرام با مینی‌اپ هوشمند وینکوبت بازی کن!
📌
در
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🤖
-
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 539 · <a href="https://t.me/SorkhTimes/131791" target="_blank">📅 19:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👁️
غول مرحله آخر…
👁️
🛜
سرور نامحدود 2 ماهه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط و فقط 6.5T
🔥
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/SorkhTimes/131789" target="_blank">📅 18:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7bgRVgBogtRgRBlPmW7k7N-Rb0djXNQsO9usGIij9BzB-EF3A5iXpUMK2uX_AYPxu_BUTxAVVxNJlDwRR7xoCBWDvwlHAI50ZwJqo3hJG5PEcRA28FVH8gI7RAOU4za5UXb9u6F78mRN4OXQ8ZqvyyfChyiCLFu_YvU8tVqiIdrTzHo6FwP3Bnio6tOTnelYo34BG1FGICg1arIQRfQdmHWlstHEiUKPS33ZAg_b9BRBtOvdY9ToLxDqto74dHPX5T4Yb7xQebxMV-3aXWvm0OlfRVxoIRV1GOmQ9GFgcw1xWfFRo280wEqxAG3eA0Ul-F6T-61Ty0iuv1v6Bv-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🚨
فووووووووووووری
🚨
مجوز حرفه ای باشگاه پرسپولیس تایید و توسط afc صادر شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/SorkhTimes/131788" target="_blank">📅 18:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
اورونوف: با پرسپولیس قرارداد دارم و فصل آینده در این تیم خواهم ماند، میخواهم با پرسپولیس قهرمان لیگ و آسیا شوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/SorkhTimes/131787" target="_blank">📅 18:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فرهیختگان: یه واسطه تارتار رو پیشنهاد کرده که اگه اوسمار رفت بشه سرمربی پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/SorkhTimes/131786" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131783">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔺
زیرنویس شبکه العربیه: از قرارگاه خاتم الانبیا به یگان های موشکی اعلام آماده باش فوق العاده شد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 715 · <a href="https://t.me/SorkhTimes/131783" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روند تمدید قرارداد علی علیپور را به اوسمار ویه را واگذار کردند و در صورت رضایت این مربی قرارداد او را تمدید خواهند کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/SorkhTimes/131782" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
#رسمی  تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 754 · <a href="https://t.me/SorkhTimes/131781" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
۷۹ روز از قطعی اینترنتی ایران گذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 750 · <a href="https://t.me/SorkhTimes/131780" target="_blank">📅 17:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
پرسپولیس، رکورددار تیم ملی در جام جهانی!
🔺
در این فهرست رکورددار لیگ برتر ایران باشگاه پرسپولیس خواهد بود که با خط خوردن حسین ابرقویی، حالا 5 نماینده در تیم ملی ایران دارند. این در حالی است که تیم سپاهان و تراکتور هر کدام ۴ نماینده در تیم ملی ایران خواهند داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/SorkhTimes/131779" target="_blank">📅 15:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131775">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfFMEFcDzxIMHeR9JQWQ1w4BiyuDzrMBbdk9eDbHCO9sOuTc7dbe2bKpdVyCo32G49HBCQ4lyXOYLhBex7zcFTyAmDYBMWX9Hl2CxafLUpshEL4atbcign22QZ2_OTJn6fjUkw5k1BFvvRpzLpDtSlBlLEvrSyjH60IGlVH0_g-_tiO0l_nXJ7mKEGGjfDN7y1UvtTBLyyciD97SWlf_arRgem3HK81Tg07Ly0G9AarUey1AVDHw81OM7kFatHSJS07rgn9bE4EIdxWNonVO343e8-fOjzg364ZfQWtB1YzJ4nt96T_ffnGrXG6V-IehNKknLiZIAfp13h0Ntp5rMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اشک‌های رونالدو پس از عدم قهرمانی النصر در فینال لیگ قهرمانان آسیا؛ او در مراسم اهدای مدال هم حاضر نشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/SorkhTimes/131775" target="_blank">📅 14:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131774">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/SorkhTimes/131774" target="_blank">📅 14:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131773">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
قرارداد علیپور دوساله دیگه تمدید شد
❌
✍️
باشگاه پرسپولیس مبلغ قرارداد علیپور رو افزایش داد و با این بازیکن برای دوفصل دیگه به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/SorkhTimes/131773" target="_blank">📅 14:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131771">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5-_yvH88R4gj-VvQ-iXwEjTQ2-heCx7l-lApypz3m6PxWBORZizJqPc3mkd2Ewc_SlSZvhfib3dNSS3ljSiCp4qLcWTianbmcqYQF9EbaypM3qANfWDMWm2ZabtQ86ec5NApUSqBHINLJX4MAJoSsFkdVV5UxPurZsufj0JkKbTmxpGFic9zWxLwlSu01JNpoljx3Qbb9k7xx26gyBBLBpct9ax0_uiCWF9cJq0TPvWu9mSEL5Zd3eY9XgEESCB6uhPMs_0ijC6Qs26vysifJY9iL9JPjKrraBlpORV8djBArKn7ekPzPbcjw8oFVm5n-Sstgg8uDUkMcWvZdXtvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
داداشتون رفته از استقلال شکایت کرده
😂
🔹
گویا براش پیش قرارداد فرساده بودن که جذبش کنن ولی پشیمون شدن اینم رفته شکایت کرده که پولمو میخوام
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/SorkhTimes/131771" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131770">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sr5-cdC4hR9JlZMlf86BWZq78pRHrN7cTXpvnfNz4jpH25YHN_HG_oHCxk6op3DzGNkK4BB1_Ka6qZ5ZQ-zXys6euudENCfJay7_i6oMYQ1Qn8UMDRec3Bh6TBDasquJS3d3ZZPPxk7EXPLKCdzyhs9aKQId5-603evuF8G0s0gokvTeCsjO_MhTOw70ZcSHAvlY_PE-Y1blsYfiCRkEv-aYY8F75b1aSDbbl37tA_M90uJzV1hvPtO9NNar3YtOyck2dkfOaD5ar3R_K2HzFXz1iR0euwVzQY_bTdR_77dmw6Pz6bwIclmkXJUgUQoHQP45brVTR2t7UDyxqOtQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پپ گواردیولا اعلام کرد ؛ فصل آینده هم در منچسترسیتی خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/SorkhTimes/131770" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131769">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLpkLnODSgP2zxEs-DDm3ZumbIQLvXEe4GxygXpAks5QnexMK1macPOTYk88WpZFYs27Jfre6jXZcDvJH7VGS5SsoBmbBkJocwjAW8vhauKqUS2qoDQWbkLu7AQrHMKjmmkdYeL_zgVT8CKkvT_-QOx3azJf6ySgBp0w45AydHrhqTMvke4GzEZOYwKFyJ2L7ZMG9M0e4epFekYktPQCnobJxH5FiK_cNdDcT-DwDZSVe9PTPG0c-UJM43L9BUc64R1Ka--_ngZk9mCvqOI2rhTJeBsckWE61rx2hVz61Ev9SpQ1fULzqT0RrpKwq6ymoAdEsY1mspfluUg8ZqgTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولیانوف: کارشناسان غربی معتقدند که آمریکا و اسرائیل می‌توانند حملات نظامی علیه
#ایران
را در روزهای آینده، اگر نگوییم ساعات آینده، از سر بگیرند.
💢
اگر این درست باشد، به این معنی است که آمریکا و اسرائیل از اشتباهات استراتژیک گذشته خود درس عبرت نمی‌گیرند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/SorkhTimes/131769" target="_blank">📅 11:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131768">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
#رسمی  تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/131768" target="_blank">📅 11:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXqkDdjb1BPzi83VszFx_abaeUHZR87GdO3UWLq5Qm8x76_WMJ1Zkh9ww-wujxWRSOX7MWtfROs6ipVFN3eAHUa6q_a1FuQLkAd92JoU6TCzp3LbVmFd0Qv9_MLY5WtBDEiJ59Yju8Pou448ryCdSrplwFx3HU66-UOrEtr37k6wdJTMXM22laMJY5SEe8I5hx2x7v7XY8qo-0hqpXiXUe6pOaY8fufQ1Hwvb2MXBdc_mywxWA8KSXjnFQIhDYwXRXhHbkHJu2KN3oKdGU895U7OpaKDZEGpB8PJPk6L99AbM6HUJBuIP3KoBvPML4kRduxG8F9eq1FFH_-jvm-kHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
علیرضا بیرانوند:
▪️
سرود جمهوری‌اسلامی رو داخل جام‌جهانی با تمام وجودم میخونم و مخالفای داخل ورزشگاه هم هیچکاری نمیتونن بکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SorkhTimes/131766" target="_blank">📅 09:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🟢
محمد شهباز شریف، نخست‌وزیر پاکستان، به روزنامه تایمز بریتانیا گفت: نسبت به برگزاری دور دوم مذاکرات مستقیم بین واشنگتن و تهران که منجر به صلح پایدار شود، خوش‌بین هستم.
🔺
پاکستان مورد اعتماد همه طرف‌ها از جمله ایران، دولت آمریکا و همچنین کشورهای خلیج فارس است.
🔺
تلاش‌های میانجی‌گرانه ما علیرغم تبادل تهدیدها بین دو طرف، ادامه دارد.
🔺
صلح به آسانی به دست نمی‌آید، بلکه نیازمند صبر، خرد و توانایی حرکت دادن امور در سخت‌ترین چالش‌هاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/SorkhTimes/131764" target="_blank">📅 08:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNlZxAJCKc_yXoI3zMZ-eRsiEdQPFOnwI0804DYu6buoF1JAuoJGAXyRUrzzP9-gREIxYHw2c1NR-U1tR6lTJAR-rbSfU5gY_c65EWNZXfHgzV-505WVRaI1s2ZMR28Ku2bCggSG3zQrPClOhIFyok-WsWTnqP-H7OOxaZjiD-wvct_rN8DSTg2OWJHThv787aej5_kHi0PQ2kof3_tRAAu1N2L91VxBEwHG8m8hpkC7I2xFiwaheEpdHB6vmPBDeDd6_cgVhEkxU6ZxW9OqVZjZ1nXuh24FtH4GiAPb1nG9kFiiATxUVQ-XfC6SQGD9yk9PsmH3RwoCbBQpni39ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
هنوز داری دنبال لینک می‌گردی؟
✅
حرفه‌ای‌ها مستقیم وارد میشن!
با ربات وینکوبت، ورود به سایت فقط چند ثانیه زمان می‌بره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡
بدون فیلتر و دردسر
⚡
بدون لینک‌های الکی
⚡
فقط یه کلیک تا ورود
🎁
اگه سریع و راحت میخوای وارد شی، این همون چیزیه که دنبالش بودی!
🤖
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال وینکوبت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131763" target="_blank">📅 01:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131762" target="_blank">📅 01:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131761" target="_blank">📅 00:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131760" target="_blank">📅 00:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
رسانه‌های آمریکایی: ممکنه دوشنبه جنگ شروع شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131756" target="_blank">📅 23:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131753">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
ده دقیقه تا قهرمانی تیم ژاپنی و از دست دادن جام با النصر و رونالدو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131753" target="_blank">📅 23:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131749">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/SorkhTimes/131749" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰  گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/SorkhTimes/131748" target="_blank">📅 22:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 939 · <a href="https://t.me/SorkhTimes/131747" target="_blank">📅 22:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131746">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT9mkVRIuKDHKoCcvmi9wSst5cDHtuM9WlIhpSfQbG3kqX3czL43gNV6aeeAz0WPCcu2xNfh4TwcBpxONxh5N3PQefmAJx6j7qlRQLx2ZjO33IPYQJ_JAd66BIAiKtFUD7NCW0KyezCADYV6_v8In3ESokTLe96dVTofWI4pIeQJdR0X0uqagtJ2Y__T7w3z-DOMaybV4_A7EEeTA5ad33-QaYiRds_Xw1B6b9N8HBYXHWkKo5LATQghMEkTPF7iCZdISZ5b-XtfBFc6116HWpMP_11BSupFzhit71nX-1YhHt5abcMt2_9Bpnka0dJBPpY_SFXqb8IbHs8MSVafJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#رسمی
تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/SorkhTimes/131746" target="_blank">📅 22:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131745">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
رضا شاهرودی: میخوام بازیگر بشم
😑
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/SorkhTimes/131745" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131744">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/SorkhTimes/131744" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰  گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/SorkhTimes/131743" target="_blank">📅 22:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
فرهیختگان: امیرحسین محمودی با درخشش در اردوی تیم ملی در آستانه حضور در لیست نهایی تیم ملی در جام جهانی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/SorkhTimes/131742" target="_blank">📅 22:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131741">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰
گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/SorkhTimes/131741" target="_blank">📅 22:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131740">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏅
بازیکنان پرسپولیس چقدر پول گرفتند؟
⏺
پیگیری‌ها از باشگاه پرسپولیس حاکی از آن است که بازیکنان این تیم مبالغی بین ۶۵ الی ۷۵ درصد از قراردادهای خود را دریافت کرده‌اند و پرداخت صددرصد قرارداد چند بازیکن صحت ندارد.
⏺
فقط یکی از بازیکنان خارجی پرسپولیس مبلغ بیشتر از سایرین گرفته تا بتواند به برخی از مشکلات خود در کشورش رسیدگی کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/SorkhTimes/131740" target="_blank">📅 22:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131739">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
قدیم‌ها آب کله پاچه رایگان بود تا اگر کسی هوس کله پاچه کرد و پول نداشت بتونه بخوره.یا سوپ توی رستوران ها رایگان بود تا فقیری اگر پول نداشت حداقل گشنه نمونه.قدیمها نسیه یه امر روتین بود و جایی تابلو نسیه ممنوع نمیدیدی.
برکت وقتی از زندگی هامون رفت که دیگه به همدیگه رحم نکردیم.
‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131739" target="_blank">📅 21:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ترامپ: اگه حکومت ایران به توافق نرسه، دوران بسیار بدی در انتظارشان خواهد بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 995 · <a href="https://t.me/SorkhTimes/131735" target="_blank">📅 21:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131732">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc8p3Fth6CrSB8QXEZyl8uWqjFQNuzJ6eBo-5CDPOATcKI5yojmrYMmYJMGPYI71twXgEp0cGGn1CaNZNg2wI_RZKpNILcX7hJIOTd121LB3zexIurNCc5LSzVOU62wpTeVkfKYIq2vM_prZPF_DOqC7awDHSDRl39cDqXMv8ZiwngJYwB9xVURO9gSGUhre6zQ6M7OgJdzth_z4DQ9yfEUnmxe03LAPqLDguNhxGs4MyJuwNWdlVoWTQw0LCFTbafKlwz3iYbdWvxcit8_X-Zrq-nc5hVH2lgiHpYbmVxw1fDxH7HytP1qqbNkV8T3IHjSKpBUCd3QFSNAlAWYQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Nassr -
🔵
Gambaosaka
🔵
فینال لیگ‌قهرمانان آسیا
⏰
شنبه ساعت ۲۱:۱۵
🏟
استادیوم
الاول پارک
⚽️
النصر حالا با رهبری رونالدو؛ در دو بازی باقی مانده از فصل مقابل اوزاکا و داماک، فرصت دبل در قهرمانی را دارد تا سی‌آرسون، اولین قهرمانی‌های‌ خودش در تیم عربی را تجربه کند.  تیم خسوس، آمار کاملاً بهتری دارد. النصر در ۱۰ بازی، ۳۳ گل به‌ثمر رسانده و سرجمع ۳ گل خورده. این آمار برای اوزاکا در ۱۲ بازی (با احتساب پلی‌آف)، ۲۵ گل زده و هفت گل هم خورده. تیم ژاپنی با فرم ضعیف‌تری به‌میدان می‌آید. اوزاکا در پنج بازی اخیرش، متحمل سه شکست شده و این آمار برای النصر، در پنج بازی اخیرش، یک شکست و یک تساوی بوده.
📌
در
ربات
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131732" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131731">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
فرهیختگان: سپاهان مشکل مالی داره و به بازیکناش گفته سقف قرارداد ۳۰ میلیارده و پرسپولیس میخواد از این فرصت استفاده کنه و حزباوی، لیموچی و یوسفی رو جذب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 993 · <a href="https://t.me/SorkhTimes/131731" target="_blank">📅 20:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
وزیر کشور پاکستان یهویی و فوری وارد تهران شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131729" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
باشگاه سپاهان به مشکل مالی خورده و احتمال داره از آسیا کناره‌گیری کنه که در این صورت پرسپولیس شانس اول برای معرفی به لیگ قهرمانان آسیا هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131728" target="_blank">📅 17:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-uhYzNXFhyTUjDOO-3TTvQ1YswenPlKNWm995Bw0bi3vZyflxsknWYaku87N8nNuHE5YXfSko9pbf24og1xeyl-BQlTSXcGVi2s7AdxNDIdzAgMGjEfZeoh4IxFovNxhTgEvJBy3PjArHcj9LaR1f7bCebOK6BxOwMzdUFuJpk-nfxtCBcuuG4CqJbyL8kgnLB-SJL9K7YCr-e7BXSHaOQ08k1UG-_OFrZ4hjU5Gr8TOAAy-KjbvKCfZ0BM-BkkzAJkcPPgxp7bob5eZV6mdsZiAGyvk-jx0DGZsRyz-RrXHgHs7JdS807a5_YEtaErykBtEAalEnlQad0cLAu2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب میتونه یه شب رویایی برای النصر و کریس باشه. اگه الهلال نتونه امشب بازیشو ببره، النصر قهرمان لیگ میشه درحالی ک خودش داره تو فینال اسیا بازی می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131727" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
اگه تمام نماینده های پرسپولیس در لیست تیم ملی برای جام جهانی باشند چقدر پول گیر پرسپولیس میاد
⁉️
🔴
نماینده های پرسپولیس : اورونوف - سرگیف - نیازمند - کنعانی - ابرقویی - محمدی - علیپور - محمودی
🔴
یکسری از رسانه میگن که الکسی گندوز هم اگه بره جام جهانی پاداش…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131726" target="_blank">📅 15:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1mxfpBJMl793p57FJy4p2tYcZ1GDwm13oNOlL1fnCJe-lb17U00WHyXNERBAPlYjEABKjTaxFh-KTFqPYukBV_rkNIJgFs0zUH4LqVinwXXbS23nwWGb6b0IJ405v2gZjTgM66ocJ5maijS-DrwYnD7q3ZorFxmSMz1So_QYnyqmK1ABU-FyRdiGwcmRKZsKN05ZQSah97Kg_xzzrEjUpFs-kKI-a2-duTWccyUgNGPy631JyF1goT2SHBLgktzDPDDCWWW26IFJu5KS9yChdgVwaaRXwrR6pakke35I10pSmXHGUm84MdrhJqGCZUndLREK8VlTU-u0bSLfBVwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مراقب پیامک‌های کلاهبرداری «اینترنت پرو» باشید.
🚫
🔴
اخیراً پیامک‌هایی با ادعای «آزادسازی ثبت‌نام اینترنت پرو و هدیه بین‌المللی» ارسال می‌شود که با کلیک روی لینک، گوشی را آلوده به بدافزار می‌کند.
📱
💣
✅
راهکار: لینک را باز نکنید، چیزی دانلود نکنید و این هشدار را به اطرافیان منتقل کنید تا کسی قربانی نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131725" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فینال لیگ قهرمانان آسیا ۲ امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/SorkhTimes/131724" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHIV4jsMnU-MoseEqeQ2jrB0dFZmbnKLDeUBVgmyI-Q7hJLoPmOxputE64RO7A2z499gHvg7s3HlPMPKLa_hFDdEBs6rEiveys3iHUrHbsPlONa1Xk4coNPXFYfpi3QqiyeQxrrSfweJwUZDmH9O1pGX2xMKnkcqlLXgYkiJ7W2qTfa0A5CHykVyZWFKYwdNhkrHWdvAdjQH_rgdtaxdsWmUgbgy4LccXsHBtYeg76VI8GEk774luHK8RuigEkxiIldsLvy8ZdV95i7Qi48dAT18mHx_xCGCfLVcNziTVMhS-dL0M1qSXhZ6tEo0869gRWG87miRWFP9rAr0s1Uj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فینال لیگ قهرمانان آسیا ۲ امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131723" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131720">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
پرسپولیس حداقل ۸ بازیکن تو  جام جهانی داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131720" target="_blank">📅 11:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131719">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 965 · <a href="https://t.me/SorkhTimes/131719" target="_blank">📅 11:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
آتش‌بس بین لبنان و اسرائیل برای ۴۵ روز تمدید شد  پ.ن پس اگه مجدد جنگی باشه میفته بعد از جام جهانی ..  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SorkhTimes/131718" target="_blank">📅 11:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIwdtwIpL3lQrWqSUG8v8hs63ua2g_9YDrdGlWIQoaMQqHlA8Q8O4wPGAqRLgho_tUgC_B4s99VVYFAgROXX3IskVCtE8BhYMdowxzGD1mk77HVIctiIBXNBGoMEsaebpaJYIYlaqEaDGdQLAfEHyMOlFLAAcQEFAOSmqbYioV99tbMoMlsbUKKmb1XfRdlosBufVxpgUuFOiyCF1-M6pKe19GhgS_Trf9idXvvqfpht3JIQc6U_ZDFWVd2CozCgBCYQT1mUq_MEQXFeVBqtAl_27QFXBjYrX054ElucMM1VgJ2Y4yIZZQMpDHVTiT8mD4pHZxREO6y2yU7WUPEbRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس
؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/SorkhTimes/131717" target="_blank">📅 11:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH39-nToO1q-GOqn3q9iNh21QPT3NYLVyvioAK_EbPIeFJexZ3-qaSnSWYbHp4GOiSfF5uNqS8yRTkk_vTAvjC57ncF8brzzbcdhu0bz43wVxQaDLr0v9kL6niiLs4QkMo9lwlyyJ8AyabRC2jJcXlqxurKd0JoFI7B8i8tXqfLtOqmkOHMXJkdTYEfCML1Q3laiRVihff3ICEdDG0S7W7WRIBeOZob7kKINiaDL3UdPID9uNN54x6Kkm3cFc78znI466N4ce-RlT2HBbBZ2iFAXVRJPzFSV0psIyhjJgttQ_s3_F6iZDwqNZG21dfK67_Gv1IbtsTJeh1uBa2dhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز امیدواری کرده که باشگاه بتواند غرامتی را از اوریه دریافت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/SorkhTimes/131716" target="_blank">📅 11:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbxW255EaBHw7Iedy4ISEDU2mRwzMkqAxf_hNC7EOsEoXvIJ3uOpg4UNYzjunB-eHQVtkgJR-Gfzbn8PCn8GptcoO--FTf-Kp5W-S2PcyqjH29NaWqNyMQEZgE03GNYM4f83f21pjEiT-WtUjR0p8lDDArUtc8SAwIBmziCIw_2gkjoQiRWrg6hgqIJLOZIlkOOmePN6Ar7PYC_JIuaZvCNjCaf-oXh_2svw-8Nw7Vnj6jtLtWDftF682KJZY28ojliWVewyGujgnuVQSVi37bOgsCcSg0_XSk36AO0MlXQK764wok2vfLXCExsmfu2RBI9g58xIMKmiEmDbH7Lejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه بازی‌های مهم فردا فوتبال
⚽️
فردا دیدارهای جذاب و هیجان‌انگیزی در فوتبال اروپا برگزار می‌شود که در مهمترین بازی‌ها، سیتیزن‌ها در فینال جام‌حذفی باید با آبی‌های لندن تقابل کنند. بایرن در زمین خود از کلن میزبانی ‌می‌کند و دورتموند هم میهمان وردربرمن می‌باشد. همچنین در دیداری حساس و در فینال لیگ‌قهرمانان آسیا سطح دو، رونالدو و یارانش باید به مصاف نماینده ژاپن گامبااوزاکا بروند.
⚽️
بازی‌های فردا رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید.
📌
وینکوبت
انتخابی حرفه‌ای‌ برای شما، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/SorkhTimes/131715" target="_blank">📅 01:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d607431a7.mp4?token=JODUuW7vr8cNB_kwws5uyQ5sR-aOGkQpPYLWtsDbKGprzixjIAGyaW-eR5kdgDvFcsvRsEd8iQtVZpaIU7Hdm3Zrvp2G19jsFRim4zkYZUIw207RLLOtEEBi3KqSFFsTBWOCg6tnZhMabAnKlQzRs45V6xicZuxXdmej-mxZM1DwCjF35FGQyCdeirFBSJE5eE3FNEM7lecP5YCNDpOfs-8WnQcstZvgNNPLBLpeAfGiRRmZRfIdFH0UnR60bXlDxOVP-uBvbidL4vzzzVR09Hj4Bwc_RY0Mmb1kKCZlSaYRp2LuWN2CxFTNluIl7CPB1rvThNGIZ5qojSL3Cr3fAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d607431a7.mp4?token=JODUuW7vr8cNB_kwws5uyQ5sR-aOGkQpPYLWtsDbKGprzixjIAGyaW-eR5kdgDvFcsvRsEd8iQtVZpaIU7Hdm3Zrvp2G19jsFRim4zkYZUIw207RLLOtEEBi3KqSFFsTBWOCg6tnZhMabAnKlQzRs45V6xicZuxXdmej-mxZM1DwCjF35FGQyCdeirFBSJE5eE3FNEM7lecP5YCNDpOfs-8WnQcstZvgNNPLBLpeAfGiRRmZRfIdFH0UnR60bXlDxOVP-uBvbidL4vzzzVR09Hj4Bwc_RY0Mmb1kKCZlSaYRp2LuWN2CxFTNluIl7CPB1rvThNGIZ5qojSL3Cr3fAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: از اوریه غرامت می‌گیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/SorkhTimes/131714" target="_blank">📅 00:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131713">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Juj-qOUcrANg_RJHwMQ9vnGRHuEPoytfW8YmyZpaJtDpDdr3aLaj8UUGKrjU7OnUogAZD7qeGyA0zZH-sp6hKGEb8TUSPdwsd2oLSiKYDBjDmp89zJbHzdG9716XTfmIJMzmUvDvB_HfjHe59uMkSI7XoxabeMmizbUJPkpx13me-zs1NrFDe5UHcc_OkgF9bdfr39zmTT-MqZyy_gMireoEZH7d7gQvRjJE7vBP-FcgrKuQ4Z3sJt1Z_CvEfhKb-mAkTra4SX60pKaU1PLku-5JENKAL6NMRoizH-Kr9cfMu2MgJTTY1ZRmWgt2MC99zGbCdYZNEBarx8TuUDKYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
محمدمهدی محبی، وینگر تیم اتحاد کلباء امارات تا پایان فصل به تیم فوتبال سپاهان پیوست.  پ.ن اینم پرید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SorkhTimes/131713" target="_blank">📅 00:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131712">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4ec80a48.mp4?token=po8NlyJEQ9NKy-bwVYyQR1YxUeLf8xWbb1bxbSOWqO1ALlSV6H-O5s4yb3L0_j_nIBh5VxbFv_MwYIMVeF_QwHWegOLRlpjFrjv53d1M8Z-ji_5LwB6iRnBsV5Q75deIrcEkog-YtZbeYntUu8CQm8XjdjXlRO3ms94SWlz68XPvesPuthvrBbB5ZW5T5WjvXGcFRRK_kOrWM-Ouu8UaNREu3r9pIA4Utf3JhC3rcLe6lUirmxtRx8r5nfZATalrkFX827ZtADY_SavIOMcy72ynFaE7w073GI29qGpSbDABAHFAM6M8WVdjNl1GBmYWiheeoipf4ISArpC5UV1U8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4ec80a48.mp4?token=po8NlyJEQ9NKy-bwVYyQR1YxUeLf8xWbb1bxbSOWqO1ALlSV6H-O5s4yb3L0_j_nIBh5VxbFv_MwYIMVeF_QwHWegOLRlpjFrjv53d1M8Z-ji_5LwB6iRnBsV5Q75deIrcEkog-YtZbeYntUu8CQm8XjdjXlRO3ms94SWlz68XPvesPuthvrBbB5ZW5T5WjvXGcFRRK_kOrWM-Ouu8UaNREu3r9pIA4Utf3JhC3rcLe6lUirmxtRx8r5nfZATalrkFX827ZtADY_SavIOMcy72ynFaE7w073GI29qGpSbDABAHFAM6M8WVdjNl1GBmYWiheeoipf4ISArpC5UV1U8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی: سروش رفیعی به تمرینات پرسپولیس برمی‌گردد. صحبت‌های پیمان حدادی در مورد آخرین وضعیت سروش رفیعی در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 939 · <a href="https://t.me/SorkhTimes/131712" target="_blank">📅 23:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131711">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">💢
پیمان حدادی: اگر پرسپولیس برای آسیا معرفی نشود، حقمان ضایع شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/131711" target="_blank">📅 23:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/091a89d5de.mp4?token=OYDzePbbzHMZIldb2B4BJqicxG_B4NNIa3LvNy2P2RCQfjrmsOwyNH9qlHC3Cot4rAgveeXoUFatoJ342mR90wEnYB87RO2NIsMidH9z1tkYOWxqvhtdClHP1jmB1FkwlEL8P-Oue2y2esJDatgjXqDBR0PT0_Ixr2Y0mPYwr8CUJMopW4PaXT-VLUJhT8m3kzg5HxuYbaa6ulOjd89S5CvBLGe3pEEzDPaLJcQ9JBFwcVk6BR4MVNoFC_3MrfAkduNmreaLghjApi3k2YBRKauHnHBMHW4ccY4fyrqRbPVqL2ACZzL5omgjhwy9mloenQ-Gsm1H8P9lD7iaHRfmgQpBKoKsekPm7bqP4OmlmiV_8j1Co3YZ2GPXssDLqOlqivT29mOn1SSiuTuflUMWDq002ls5huF2Vzzz_MS7EnQxfK4KkVjEPdi6eXWrrv2baRoToBQYujfvOsagdcjW3hm08agk3610kEdvJm-eDPxlBl6l9nTHH-hRsUFXVLPC5Fzq9io9rLBQzD9qXcHWaQV5E3DLmB7HjBSEYsSUkskPLLP55USt47bagQg_yJ83LgQWcEY84eNOFmtnSmM3WfeBXqld7FBPFA5EyMcyI2v4yw826tBv7Ayep1sQD1IxIcG1hGv02wWDT1OmBnFsB2eOPsm3Pks4O_ddxiHBFTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/091a89d5de.mp4?token=OYDzePbbzHMZIldb2B4BJqicxG_B4NNIa3LvNy2P2RCQfjrmsOwyNH9qlHC3Cot4rAgveeXoUFatoJ342mR90wEnYB87RO2NIsMidH9z1tkYOWxqvhtdClHP1jmB1FkwlEL8P-Oue2y2esJDatgjXqDBR0PT0_Ixr2Y0mPYwr8CUJMopW4PaXT-VLUJhT8m3kzg5HxuYbaa6ulOjd89S5CvBLGe3pEEzDPaLJcQ9JBFwcVk6BR4MVNoFC_3MrfAkduNmreaLghjApi3k2YBRKauHnHBMHW4ccY4fyrqRbPVqL2ACZzL5omgjhwy9mloenQ-Gsm1H8P9lD7iaHRfmgQpBKoKsekPm7bqP4OmlmiV_8j1Co3YZ2GPXssDLqOlqivT29mOn1SSiuTuflUMWDq002ls5huF2Vzzz_MS7EnQxfK4KkVjEPdi6eXWrrv2baRoToBQYujfvOsagdcjW3hm08agk3610kEdvJm-eDPxlBl6l9nTHH-hRsUFXVLPC5Fzq9io9rLBQzD9qXcHWaQV5E3DLmB7HjBSEYsSUkskPLLP55USt47bagQg_yJ83LgQWcEY84eNOFmtnSmM3WfeBXqld7FBPFA5EyMcyI2v4yw826tBv7Ayep1sQD1IxIcG1hGv02wWDT1OmBnFsB2eOPsm3Pks4O_ddxiHBFTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پیمان حدادی: اگر پرسپولیس برای آسیا معرفی نشود، حقمان ضایع شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/SorkhTimes/131710" target="_blank">📅 23:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: دوستان فدراسیون فوتبال زودتر اعلام کنند که آیا برای فصل سقف بودجه گذاشته می‌شود؟
❌
آیا برای فصل بعد قرار است برای جذب بازیکن خارجی محدودیت اعمال شود؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/SorkhTimes/131709" target="_blank">📅 23:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: دوستان فدراسیون فوتبال زودتر اعلام کنند که آیا برای فصل سقف بودجه گذاشته می‌شود؟
❌
آیا برای فصل بعد قرار است برای جذب بازیکن خارجی محدودیت اعمال شود
؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/SorkhTimes/131706" target="_blank">📅 22:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
حدادی: محسن خلیلی تا پایان فصل سرپرست تیم بزرگسالان پرسپولیس و جانشین افشین پیروانی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/SorkhTimes/131705" target="_blank">📅 22:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
حدادی مدیرعامل پرسپولیس: با خانم مرضیه جعفری سرمربی تیم ملی فوتبال بانوان و خاتون بم وارد مذاکره شدیم و قرار است در خدمت ایشان و بازیکنان تیم خاتون بم برای فصل آینده در تیم بانوان باشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/SorkhTimes/131704" target="_blank">📅 22:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4464cc1d8f.mp4?token=GxaZZjj_I0wqGUUi7BEslsCcwe5BS3PLewJij_r_Tka8SMy1MMBcA0sl9tY3nbKD1rYX9NqkztJHNjoYlwNFMM-pd1Ok0GTxhe7acp7FDP2rZI1boh9c2dIom5sHtDGcEV8B18brcJmcE3_xoPt3OSaezBkFooyyQt_LR_mzht7PjfE7lB7X1blAezMc-npjPuOrQaebmCoEC_Kte3RGLCFduRlLepqWlZ9KEt1VflbwPemyk_wsaiTSMB_C4Wh1KKhG1KEyqvr9XsrABp9h6egad5LskTbzK9L3WRh50C6EAcyF6UC00fHWOLoprYDesFYo4241sVvHJSxZ8qn4YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4464cc1d8f.mp4?token=GxaZZjj_I0wqGUUi7BEslsCcwe5BS3PLewJij_r_Tka8SMy1MMBcA0sl9tY3nbKD1rYX9NqkztJHNjoYlwNFMM-pd1Ok0GTxhe7acp7FDP2rZI1boh9c2dIom5sHtDGcEV8B18brcJmcE3_xoPt3OSaezBkFooyyQt_LR_mzht7PjfE7lB7X1blAezMc-npjPuOrQaebmCoEC_Kte3RGLCFduRlLepqWlZ9KEt1VflbwPemyk_wsaiTSMB_C4Wh1KKhG1KEyqvr9XsrABp9h6egad5LskTbzK9L3WRh50C6EAcyF6UC00fHWOLoprYDesFYo4241sVvHJSxZ8qn4YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: افشین پیروانی قرار بود به یک کشور دیگر برود نه آمریکا/ او برای رفتن به سفر از من اجازه نگرفت
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/SorkhTimes/131703" target="_blank">📅 22:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
پیمان حدادی : پرسپولیس پرهوادار ترین تیم ایرانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/SorkhTimes/131702" target="_blank">📅 22:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
حدادی مدیرعامل پرسپولیس: با خانم مرضیه جعفری سرمربی تیم ملی فوتبال بانوان و خاتون بم وارد مذاکره شدیم و قرار است در خدمت ایشان و بازیکنان تیم خاتون بم برای فصل آینده در تیم بانوان باشیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/SorkhTimes/131701" target="_blank">📅 21:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
ترامپ:  ممکن است مجبور شویم یک کار تکمیلی کوچک در ایران انجام دهیم، چون یک آتش بس یک ماهه داشتیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/SorkhTimes/131700" target="_blank">📅 21:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMhSg_N6cKt_Bump1nO9BAYllbcDqMW1SZrBbSPpIDHofZFdO52E5_jOiNO1nOIzt7tlpE0zA6nN2ZFdSRJpTa8BH2c5QQNdRVkU4tZAc3qtA450sN280lhu_5hFQNmEYLxAWalJy6iggpgcpGs36KKabHfIwKJYaJAQf_rzQWbjoYbAw2rpFlwnAoDx_hrpgt07l_NldbD6voOG7c3hkahxGi4if5KZ5t80QyqzsVUU8A-YiLWouZvRGYZ2SckAj1c7csAfibzeKDR_xDTVhXGGl_qXbeiGbYDpXroPZZ4vBRPQQE9HpWm3XHPv5fNCuu8iuDMysR0VEs1j2CD44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت جدید و عجیب دونالد ترامپ
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/SorkhTimes/131699" target="_blank">📅 21:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
ترامپ: اولین جمله پیشنهاد ایران را دوست نداشتم، برای همین آن را دور انداختم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 989 · <a href="https://t.me/SorkhTimes/131697" target="_blank">📅 20:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
آشوبی: استانداردها را به فوتبال روز دنیا نزدیک می‌کنیم/ مسلمان نیاز به فضایی تازه داشت
🔺
تفکرات و ایده‌های بسیار مثبت و قوی در باشگاه، به ویژه در بخش آکادمی وجود دارد که به نوعی برای اتخاذ این تصمیم مشوق بنده بود که در ادامه مسیر بتوانم در این حوزه کمک‌کننده باشم.
🔺
مربیان آکادمی سال‌ها در این رده کار کرده‌اند و شناخت خوبی دارند.
🔺
برای از دست ندادن استعدادها، تیم ب تشکیل می‌دهیم.
🔺
انتظارات هواداران از چهره‌های شناخته‌شده به حق است.
🔺
محسن مسلمان نیاز به بستر تازه‌ای داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/SorkhTimes/131694" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131693">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
ویزای هیچ یک از بازیکنان تیم‌ملی ایران تا این لحظه صادر نشده است
❌
برخلاف تقریبا تمام تیم‌های حاضر در جام‌جهانی که همگی ویزای خود را دریافت کرده‌اند[بجز عراق]، تا این لحظه ویزای هیچ یک از بازیکنان تیم ملی ایران صادر نشده است.
⚠️
مهدی تاج قراره در ترکیه با…</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/SorkhTimes/131693" target="_blank">📅 19:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131692">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/SorkhTimes/131692" target="_blank">📅 18:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
ویزای هیچ یک از بازیکنان تیم‌ملی ایران تا این لحظه صادر نشده است
❌
برخلاف تقریبا تمام تیم‌های حاضر در جام‌جهانی که همگی ویزای خود را دریافت کرده‌اند[بجز عراق]، تا این لحظه ویزای هیچ یک از بازیکنان تیم ملی ایران صادر نشده است.
⚠️
مهدی تاج قراره در ترکیه با…</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/SorkhTimes/131690" target="_blank">📅 18:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
ترامپ: اولین جمله پیشنهاد ایران را دوست نداشتم، برای همین آن را دور انداختم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/SorkhTimes/131689" target="_blank">📅 18:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
مشاور وزیر ارتباطات: اینترنت بین‌الملل حتماً به حالت عادی برمی‌گردد، خیال مردم راحت باشد.
🔺
روزانه پیگیر بازگشایی هستیم و بخشی از خدمات بین‌الملل هم‌اکنون برگشته است. امیدواریم در ماه‌های آینده با تصمیم نهادهای امنیتی، دسترسی کامل برقرار شود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131686" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
پرسپولیس به دنبال تغییر سرپرست نیست؛خلیلی روی نیمکت می‌نشیند
❌
پس از کنارگذاشتن پیروانی به دلیل سفر به آمریکا در میانۀ جنگ، در روزهای اخیر نام چند پیشکسوت برای پست سرپرستی پرسپولیس مطرح شد اما پیگیری‌ها نشان می‌دهد که باشگاه برنامه‌ای برای تغییر موضع خود ندارد و درصورتی‌که مسابقات ادامه پیدا کند محسن خلیلی روی نیمکت می‌نشیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 893 · <a href="https://t.me/SorkhTimes/131685" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
هلدینگ خلیج فارس به مدیران استقلال گفته پول نداریم و فصل بعد خبری از خرید خارجی و بمب و اینا نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/SorkhTimes/131684" target="_blank">📅 17:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
پرسپولیس
حداقل ۸ بازیکن تو
جام جهانی داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/SorkhTimes/131679" target="_blank">📅 16:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2YSxcvhesFT9ZsrR-YB1a0LumNFBj-rWWnSUiy9mPvZhLmY5gNU3KvBCHcvRXLnxau6rVhzb7Qv--Ddf3O3JgAvdcBJZKvekWEjhzt5p69VPHBo50cbAQS1_b_pD7SH4K7TEKn7rJkFdacQgdtgj4jGwy0tBgeOL7gXAVbW2DHJKdyJZX8411ts9LUmH-LnvJZrQOqEs50ZYN6ZXPyR7bq-4v1HENVw8I8-_e4rJyled5asCh3i5gmelX4hA4zH_HR3_l7SaUWPVxP4sfm9JEt7ebSMcyxQMH9Q1OplKTc9aSo9VJM9RTxV3iN0vDYgKuN-QFIjJYDurma00bAkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی، شهردار تهران: ما قصد داشتیم قبل از جنگ بیت رهبری رو با معماری جدید بازسازی کنیم، اما آمریکا عملیات تخریب رو که بسیار هزینه‌بر هم بود برای ما رایگان انجام داد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 796 · <a href="https://t.me/SorkhTimes/131678" target="_blank">📅 16:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBeMysxTFbExMNkW7Ag50S9l5lUvEaFcUbC5ZJEP8qVm1bODSb0srGFhQ_7TmpwOgyXaZ4emgA11Lq2ki7WCcPL0pvn9U7emBV5ybOKyqs1f13D7-0URfFDRhiIavsFEccNiviepfBYPTxj0BgH4VJKtcjMRM5yclAC54UH3hO5Ser4sh2YV3mWJq_t-HUaPfNWkzF78vbmKpW8S4kDdJ-wihTrgUQZTFrt3SpLDwBEYU5dK3FW5ns2QfnEtfJ1YfzebKUNCm74O-QbUsLsRa0-9una8G20GT9p6RLxMxdwGHDTCuRzJGMh9J2fIMKv9aD1YWCmFaKkaMjQeVQQ8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاربران محترم برای دسترسی به سایت وینکوبت فقط کافیه از طریق ربات وینکوبت وارد بشید.
🤖
-
@Wincobet_bot
🤖
-
@Wincobet_bot
📌
بدون نیاز به جستجو، بدون لینک‌های پراکنده، همه چیز از طریق خود ربات انجام میشه.
📌
ویژگی‌های ربات وینکوبت:
👇
▪
︎ورود سریع و مستقیم به سایت
▪
︎دسترسی راحت از داخل تلگرام
▪
︎بدون مراحل پیچیده یا ورود جداگانه
📌
اگر دنبال یک راه ساده و سریع برای ورود به
وینکوبت
هستید، این ربات ساده‌ترین مسیر دسترسی شماست:
👇
🤖
-
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/SorkhTimes/131677" target="_blank">📅 16:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1942fb9fb8.mp4?token=ubrmfLUglZz4WCgCnL1Qfhmj3VNNr2H3vsGZnvsYbUK_3x8e21uU5jzLiNbCZfPt9rculxMz_3zW_UGeB0N4o6CTBJa0dg8k1kmBs38ywgNSo9qLU6hOgaMvN8njZ6vNaDleGD80811zR1dGUUlMjUWDhlvnrPnadyTvBfFswiQfYWPXC5wU4E_vahX9TwoSzIxz9zb-MTOBlsK-pfn7ikeZuWnnmqdcK7kLxl9JU97r9H6uMs76JqVEJt5_5x56Toul3h2zjK41_sYq-1gzdxXsMMsWuf4HOuIePtGM8ptA86ZTyS9ka-DDX0jwt5ysialn-3i4iOmxScVpS4wV2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1942fb9fb8.mp4?token=ubrmfLUglZz4WCgCnL1Qfhmj3VNNr2H3vsGZnvsYbUK_3x8e21uU5jzLiNbCZfPt9rculxMz_3zW_UGeB0N4o6CTBJa0dg8k1kmBs38ywgNSo9qLU6hOgaMvN8njZ6vNaDleGD80811zR1dGUUlMjUWDhlvnrPnadyTvBfFswiQfYWPXC5wU4E_vahX9TwoSzIxz9zb-MTOBlsK-pfn7ikeZuWnnmqdcK7kLxl9JU97r9H6uMs76JqVEJt5_5x56Toul3h2zjK41_sYq-1gzdxXsMMsWuf4HOuIePtGM8ptA86ZTyS9ka-DDX0jwt5ysialn-3i4iOmxScVpS4wV2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
افشاگری بهزاد داداش زاده مسئول برگزاری مسابقات هیات فوتبال استان تهران از زد و بند خلیلی در آکادمی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/SorkhTimes/131676" target="_blank">📅 14:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/SorkhTimes/131675" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
ترامپ، رئیس‌جمهور آمریکا: ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/SorkhTimes/131674" target="_blank">📅 14:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131673">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ترامپ: اخرین چیزی که بهش نیاز داریم الان جنگه، ایران میتونه اورانیوم خودش رو به امریکا یا حتی چین تحویل بده و دیگه جنگی در کار نباشه!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131673" target="_blank">📅 14:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131672">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
ترامپ، رئیس جمهور آمریکا: من دیگر خیلی بیشتر از این صبر نخواهم کرد؛ آنها باید توافق را امضا کنند!!
❌
رئیس جمهور چین به من اطمینان داد که با داشتن سلاح هسته‌ای توسط ایران مخالف است.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/SorkhTimes/131672" target="_blank">📅 14:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131669">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/SorkhTimes/131669" target="_blank">📅 13:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
وزارت خارجه چین: در مسئله هسته‌ای ایران، استفاده از زور به بن‌بست رسیده است
🔴
درگیری بین ایران و آمریکا هرگز نباید اتفاق می‌افتاد، نیازی به ادامه آن نیست و پکن همواره معتقد بوده که گفتگو و مذاکره بهترین راه است و بايد يک راه حل فوری پيدا شود.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131668" target="_blank">📅 13:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131666">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
رسانه های مملکت : ترابی و اسماعیلی‌فر دوس دارن دوباره برگردن پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131666" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131665" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
