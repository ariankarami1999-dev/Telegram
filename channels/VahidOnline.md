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
<img src="https://cdn1.telesco.pe/file/gMKK5P4FvFCp2EHSOgz640SRmas14srRpZkmE4ziqBq8wo_lq6_yIbO0S6SRlpJj7vt6_bCR_Y1zoEOTMBK3tJgRa2oVF0_fByT-k4xBJTEeDiiilEJyq4TlUxVEbob_SBFMXaihUZHmxdBCNtaOd2AlMXXeQqOTQ_bi4umZyD2T0w1hiGBY3OA5bniwPwopyenQrSkYLTkh5eg00QOtAlxUN3ngg9z5PUMhxE3WR1NlVxTkGmnrw_l1eMnVuUkJ2bHD7uPPw4GXoxcvurFEbfTnTENoCgqv0Lwb2rzkFaIcUCN8eKlA0aDjMdv1i75EDenPLhq5PGSO353VOz_tLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 21:28:40</div>
<hr>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LsHOlEdxEQHUSd6UF6sORX6iNgoe8kRL_pP2cRhEnEKsgwcF9vrvm2S2hUVg4Ag1bptSXtUkq3yu03pgYuLUX2i0JwLm412aU6MEPhlwxF7Fdtcy-qHdb4ItWS_jIyjrDafwfMAhx-T1umn6P9PH_QCNp3fE2fMrFXDxmFK6sqMmMiXwH402h_JHtx6axLq7X2klg4GdQIR25nnVeu_M4_dwCJXRNzvXhnCu_PsB68f9_MGKwBok37dwrqW7leyKKG3HE_M8U4OqmBXpU6iVvXgHzvRYXqoMyPDsBw68CT3XrxKmx3Ow485RyqZDShypuUO5Qt6MTROYQ_zJMUTX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH-AHbJtGDmc5BDQ-AaYFcg-WAtf9jB2zy9hAjfXRKnvWL2U1GPysNuO3sEyJd7Tr-m0xabBShOpDyIX4htvej9DV-bNUy07xr9OmoyVxPzC82d8wLNxJDd0UcoIFPUFVxP9pYqV6XJe139ODN_zjQwy3T8ft2J1l5Arpp0z2hVWz7ZO31vZCGMNN510aAx4ll-_ctnj0fFv6SEjnQ7TlQRWJbAk1Epfg8xgvLzueg6uZo90wG4Z01-ejxaCer8i6TNUbYFM_5Q9DZxmnwv8Tdxecijj4CP8v8Qt0n7DGGgJtBmwn4M2aODPcTAuVI_F_7H7crd2z3cMuWpn8sbrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/egL9qPDvubRemi7wEbz6l1zszXJq2Lswer2XLdFfiE3xCxPyvVXh2fBsyE96RMtFLhfWJU4J9suv4haTxdr5kgm80rxLzKOVlPIA_50t_Isu04bM_VIaKUBkkTlVGPg7p9Dk-x8K3j259BHn6GRFWWlNOT3aKl9TF1l6xZ_BH3_El9C33YQ0Hj2W5HD4gJtmM0T7OCQK3bFwuQ5AE05AHJWG3MEzvJvf30JRbYZ8AuqHmHcFoAYpxkXKEMHRIvVpdYV95J_OWZKadJW10UcCb5WMvbURnWAb0s2xDJV0Q1uEUtRcmwOZDoE0P8OjMP9c5yob39wgTMFmU0hcD1XIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=H6wl9HwENob4iQqxiTz-ylcS0R-8hOGayLU1C_2mFjHKAZq800GIIW-sdsKgJxDQStdXJMqhrE4gl_QU3B6VIR02Vx0t1EG1ninqff7H2VnMSkQrZYIv1F7MkLI8XWGXmC5Gnw7ACrw01xbwOJqta4yxJ0UjxApy_MLeOPhvSXUIcxbe3RVQd3_WKdcCoBOJdZpCfMdVY2XpcJxktO9r9xuhTjePPs8UPeh2_L8yjNlF_ohfQ2-OOovyzrqJVDv4Wc_JNb3IOAlsU1Y6Vt-jLLiJ9h3aF4-XfVZ4QERw5BqNb7EjvV42PaIPuP0MzAin1ZfrumGJxenohFaj4nXI7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=H6wl9HwENob4iQqxiTz-ylcS0R-8hOGayLU1C_2mFjHKAZq800GIIW-sdsKgJxDQStdXJMqhrE4gl_QU3B6VIR02Vx0t1EG1ninqff7H2VnMSkQrZYIv1F7MkLI8XWGXmC5Gnw7ACrw01xbwOJqta4yxJ0UjxApy_MLeOPhvSXUIcxbe3RVQd3_WKdcCoBOJdZpCfMdVY2XpcJxktO9r9xuhTjePPs8UPeh2_L8yjNlF_ohfQ2-OOovyzrqJVDv4Wc_JNb3IOAlsU1Y6Vt-jLLiJ9h3aF4-XfVZ4QERw5BqNb7EjvV42PaIPuP0MzAin1ZfrumGJxenohFaj4nXI7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVI4Y3bLh55rsomgPtqr2D-XY4z6RI-fnur5iTMh10zIWCHpB9pNQlc1J1OIv1kPY8Vd-PRGtrPmV7KPyH86T0_3LcrXONn_Gzv-2VkB6B9U-3Huu9gtvDCKFo4rp5necTnMC6JjG3Qx22d8u9sK217w5JcUEuKDwYf4H0pxggEknQAfVOC8Q5LG3QwhiMFe7SvDWUSe34h4ujAremv_GORTRzHVel4RHUxtmntZsvlFFq44oz6GxyWpnhVDNT9ViSosKEUY_3NaQkfHPMWXZYFhlVY3drX_b7W22kuDOY8id7UDB6qcWKR1BDXcIm9jj56O8Di9GrUNLNXwqTERVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceLDJmuvaG-au2iU1mwfAsYz2svUUsCdXd8oR4mcl-RYoAGW9KjIotNQlVXo2-XrxYTjtCaDYMemsvSa7kV--0guAFODOb39Vaxc-wmd_1fNgDQzZVWhGuA4rxXC3bQWTkB-aE3DkAvw0Q9PMeN_oHvUda7SppDmZt_K2NZ_Uf_jNd0SYJ47-E_0zo8LZqpYRzlMiuKDnP6Ejfd9AifBdRfVa8vTi4pzKkWUlIB_m3ALcUel5kG_rTyZPE7zJ1gYNe0PCwoT41e629eKOGJFgh2toyNFPFpUvg9WOgoCY6VGOp3mgZzUTNRf1ecq1s1V4IfGiHjmSbqRBCo4T4UTCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نشریه آمریکایی وال استریت ژورنال، امارات متحده عربی به‌طور مخفیانه حملات نظامی علیه ایران انجام داده است؛ موضوعی که به گفته منابع آگاه به این نشریه، می تواند امارات را به یکی از طرف‌های فعال مخاصمه با ایران مطرح کند.
منابع آگاه به وال استریت ژورنال گفته‌اند حملاتی که امارات تاکنون به‌صورت علنی تایید نکرده، شامل حمله به یک پالایشگاه در جزیره لاوان در خلیج فارس بوده است.
در اوایل آوریل گذشته و هم‌زمان با اعلام آتش‌بس از سوی دونالد ترامپ چند حمله هوایی به تاسیسات نفتی ایران در جزایر این کشور و اصطلاحا مناطق فلات قاره شرکت ملی نفت ایران صورت گرفت که باعث آتش‌سوزی گسترده و خروج بخش بزرگی از ظرفیت پالایشگاه لاوان از مدار برای چندین ماه شد.
ایران در آن زمان اعلام کرده بود این پالایشگاه در یک «حمله دشمن» هدف قرار گرفته و در پاسخ، موجی از حملات موشکی و پهپادی علیه امارات و کویت انجام داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75427" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1LOVFBdw1il00p_j-qQeFY0vK0oPEOOhd9Lbu8oVKbIQQdBN4Sg9gzmMuSPlJADLc2uqSVqzSHD6UxwTnXfcaksZE9JeaPkV93HmRlavFMCtE1cUWLBYhTgJ_dTO-xUFZixj490UV9iuTgV7Kca1ayOD1eQgUWDzKWaH3ez0ZrxEoqf2XHFgkwaQPli90PF5C7BqOxlF683XTwQ84drXNbZBBkxMOzMzzFlyJNj2Z4zjDeNPu4PhVFLWlrOcoNH4yvD0ZC_oYTg3XpynY5QJ7fudPOQje8FRDC3uF0tZhwnfhq1DVdu7byevgqtUBEpGo3rNcbVPt_izoN8XwdVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده، روز دوشنبه، ۲۱ اردیبهشت‌ماه، در بیانیه‌ای رسمی اعلام کرد که پاسخ اخیر تهران به پیشنهاد دیپلماتیک واشنگتن، نه‌تنها از نظر سیاسی غیرقابل‌قبول است، بلکه با استانداردهای لازم برای لغو تحریم‌های مالی و اقتصادی نیز همخوانی ندارد.
این وزارتخانه تاکید کرد که رویکرد فعلی ایران مانع از هرگونه گشایش در مسیر مبادلات بین‌المللی و آزادسازی دارایی‌های بلوکه شده می‌شود و تا زمانی که تعهدات شفافی در حوزه برنامه هسته‌ای ارائه نشود، فشارها بر شبکه مالی این کشور ادامه خواهد یافت.
در همین راستا، اسکات بسنت، وزیر خزانه‌داری دولت دونالد ترامپ، در اکس با بازنشر این بیانیه، موضعی قاطعانه اتخاذ کرد.
او با اشاره به اینکه پاسخ تهران نشان‌دهنده عدم تمایل این کشور به همکاری واقعی است، نوشت: «در حالی که دولت ترامپ با حسن نیت مسیری برای دیپلماسی باز کرد، تهران با پاسخی کاملا غیرقابل‌قبول به میز مذاکره بازگشته است.» بسنت تاکید کرد که وزارت خزانه‌داری، سیاست‌های مالی را به گونه‌ای تنظیم خواهد کرد که جمهوری اسلامی متوجه شود عدم پذیرش توافق، هزینه‌های اقتصادی سنگین و غیرقابل‌جبرانی برای نظام پولی و بانکی این کشور به همراه خواهد داشت. او نوشت: «زمان آن رسیده که تهران متوجه شود هزینه لجاجت، فروپاشی کامل اقتصادی است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75426" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V25pSzPciti7go_PQteHD6vwB6-xCfxTQpFsUzXcOLDHWSv6bqQIVEIWtnFGP9WuAVq3yRIP-6qpxMMmwKwYgkHPmMh6NWdsjGZhUEFhWNpflEY45Fru7jJaROIsaYtllCIVQp6Rlhe1RGRJk9dcKWwPpfUIwqx1TCot2ScDVTYN4qFz0txN-1d9ExqUu2Pgo-ldclc1j3RAoZujoiUI-faNbMtTXVSMdQ0M1OBGwsCQHEMbXkhztiD2uT_5jM_UvF7tw7gaa4QThJWykCyzls6s9bgUpayAvwk3MWHPkinEYEd0qKOgcgqjyQRIGIWz4FgujiQIXF6luySldQk4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیات جمهوری اسلامی در مذاکرات با آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در شبکه اجتماعی اکس نوشت نیروهای مسلح جمهوری اسلامی آماده «پاسخگویی درس‌آموز» به هر تجاوزی هستند.
قالیباف نوشت: «استراتژی اشتباه و تصمیم‌های اشتباه همیشه نتیجه اشتباه خواهد داشت. همه دنیا قبلا این را فهمیده‌اند.»
او افزود: «ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75425" target="_blank">📅 22:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCnPGUEFaLR16afOKkvknrkQdrizBYRFtDdkb-p_jFsqqTBbFFDdB2k6tH6Ekt1BxepTmKIYnFerM3MATkcb_CPzrafI2AaOMvZY-3jEdngPBMMEI59_Uyx9hleCEyncMLwn1GnrqyLvShxB-FMm4Ax8kWBJvpRItn9iqALMfGFqtCmkb5-ep-rLvsTTUF0GImScjw3MlR_XF5UVLKmH21aiKIKOSNRhWWYhs1UY-WFeGvzmC8DlCCFaObxK_PdEy_BGWT4azMKUf_1v6oPjvHkDRJMHuTOP1R0oPjd-OJCs3EeJfcssZV0dG_u3ZiVfMUZ7CkKfXVwsaWcsOcUQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد دونالد ترامپ روز دوشنبه روز دوشنبه ۲۱ اردیبهشت ۱۴۰۵ با اعضای تیم امنیت ملی خود درباره ادامه جنگ با ایران و احتمال ازسرگیری اقدام نظامی علیه جمهوری اسلامی جلسه برگزار می‌کند.
بر اساس این گزارش، سه مقام آمریکایی گفته‌اند مذاکرات میان تهران و واشنگتن روز یکشنبه به بن‌بست رسیده و همین موضوع گزینه نظامی را دوباره روی میز قرار داده است.
اکسیوس به نقل از مقام‌های آمریکایی نوشت ترامپ همچنان خواهان توافق برای پایان جنگ است، اما رد بسیاری از خواسته‌های آمریکا از سوی ایران و خودداری تهران از دادن امتیاز جدی درباره برنامه هسته‌ای، احتمال اقدام نظامی را افزایش داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75424" target="_blank">📅 22:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JFhxeBnX9l3a_8lQG3uLRh-wbucf8xnnsSc0IH-p8tdOVhZGEKbAHUx3sWiICW5vaeyESfylzYm7yMuMopX5tsEQG31Fk9AGHf33SUAMt7XUuLAFrcIXIwbdIawbzbcj0NGkpD4zO0QAQR3nWGGo3FTNSbAEsVpg2Y60CxdPiNkwnRr1kuvyW_OrORfgUAYSUqbKV5wGAeSoO_3yTJ3K52orx3pDfCpAIi6mlwrA0BEdGNuqBrWqY3JwxtzVZiSyZueoqcXDO5bkS4JAi-KS0fydJJPPUwnLFz3ZppBLbnVwV_JlyOFJwrSWTxwbRXUjtTOhwenwnTgZXnrY1GsvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ER8Fd1JcNpcZx6ieNq63lwouVKkiD9zF7xM7TI-6u-USXdQdOw6GFfrrQ50A1zbgfhO3JBjWa89EKDYhzXNA3GOx4SN1qx8hdZxHbt0CVyOfBAqj9hr1lDMNRm09TEMjNZ2u56Ka2_eYlbz0eSh999cnZqCLv-qpn53c_mTXbBOq2Fx3kRjdSX74shRiLbHaLbpvXa9c4QDO1W_6BC5OfD5CyFejlvdIdrc11u0u_luNMKsC6jGefZKloNjUvvp_Q_1hzucffJK36Apz7guu076ImCIo6cyklm3oJtZkOvH0HDewMNHVLYfm4N-5gW-85mjRW7ufgwoKDx7oBAt-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eBLfoU9gLNdNqvA7JeItSQMEnC-gTi8fwXHDdDpW8RSMvSmaKaYNeZmaCWf_ZWJJA-XFwIMcXWBorsW2ZRKOkl0WuBjlECzA5v8DEZrNy0Ny-xQcH_dWgqi9MC6QOsaOi0KQUD0mmLYqDzizCFUCcVQHq1diVc1qJg8_DPAZNgE6N9O6u9CKndwUs9I9GqrE2JwHEYT99b2PJZhi04wwuo-VcoY_yoydWhZJ22hifCDhEKhWFdP2jxWWirBusBVJ5NGcHgeN6qXASnQCkdHMqjV6FiALECHb52Bat0ZOwmfhucnuSCNIQEh_oPcf6nVavel5xYfivnN0vuF3pzbjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UwpZdIavwOhKjHEqUcoeU3iq0M4fzv87oDJFEPXbVva2pn9BQ8z6s-gyF7z0QuodgttLhQTjAG-fCFfD9yE7-JKSUGqDUDXRllChGybjgmVQU63jS5PASAKd6rDZP9R72TIK1aCIPpCT-YTBFuFvxXX9Sxe6tI0uZeyRCnyNGMkGIjhHJh_OdjY0jYzwDq034T4XUoyVj4cGCr0pvqJdDVqXUJxEwMGpCMes3T_SH1-fsmcYvdyk0PAr0-rzr0SEk4J8futK2L8rBN73I1jlYL9Vp_OkMj6eTyow85JGEL2HH_927RLHTFg7dGwA0l7Y7PUvOLzLgLOGoPgdoutJAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی حدود ساعت ۱۹:۳۰ به همراه تصاویر بالا:
▪️
وحید الان برام پیغام اومده که من جان فدا هستم و ثبت نام کردم ولی خودم در جریان نیستم
😂
▪️
آقا یه اتفاق جالب افتاده. ظاهرا بعد از هک شدن دیتابیس جانفدا دوستان یه فکر بکر به سرشون زده.
من هیچ وقت در این کمپین ثبت نام نکردم ولی پیام زیر رو برام فرستادن. فکر کنم خودشون به صورت پیش فرض همه رو تو این کمپین عضو کردند، حالا هرکی جرات داره انصراف بده… البته نمیدونم انصراف داره یا نه.
▪️
امروز این پیام برای من اومده در شرایطی که من اصلا ثبت‌نام نکردم.
حتی برای پدر خانمم که فوت شده هم اومده.
▪️
امروز عصر واسه من این پیام اومده
در صورتی که من حتی تا حالا سایتشو هم باز نکردم
حالا یا خودشون دارن روی شماره هایی که از یک سایتی یا صنفی داشتن ثبت نام میکنن، یا اینکه یک ادم [...] واسه من فرم پر کرده یا اینکه مسیج الکی فرستادن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75420" target="_blank">📅 20:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nqovXvOAI9DexPaMXTcMITatM4IJ2p00dN4zG4enGOTaZqzqWGYibKl0EPE95xtlyoYMvjzoafgU_wB05Ytj9jsP4uXXDq-F-oOxIU-JGOidA460EjIgg6Va7IfDcMG9N1XvDsWRrJaC2jVzD2FFHT7uUmZzFYMCL-jeNratnyK_e8g7YbXNJ-0hAXUAUHER2Djh169RoeRcE_5AfLcSH7mNxVrDL-ucd8gPlAbfJhr6rSCejTrwyE7jf_a1C0gqoEQcsW49uGYTW6qTbqFE5mam0V03goR51_WbW8pN0iv8diY7fzlpk7RP-L1fx2udWyt1z_p3DLa6pYX6LZ8GgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/isEFtCj59w--CEzayGCTNj2QcY1UEF-Ms0au_9EimtSVz6Zpei1p-tj5nuZTPMWX45Zk0AiPPSvcI7bPf3JKB3s67OGvgQTr5vcpVf5Hb_JDdsJKHGdQ6ZgauyFm7yu3yYDMDWn3EkOli-pGzfGz17uojGrCbBfv1IPkXNL4q_VK8PE1ZivemQjqPU97ndnOvGfuLvzBxVzWRhs91OTGmUFCLq4huM-XpCsodHuphve7tRPxzWH5z3qlYC_j2JaLGnLSKxhDB3IjRoOVmH89YFsoRjxdkFhiodVinwmfO8WOeO2UburcpGaoFTSkHDMlO3iuAA536cG5b9DnFPa9wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QQ5bYB-Zr4S00N-ZorpFJLiXQp9zTCoIbAdCHhBY3SY4gZgPsEA6_RFSnHBTd8N_lzQeFshqwpB4PbC53s5h_KzqKNdEWqJV8rBT_sFvtFBmd5z_cntJnG4QxGWKJw5oS4ZudbF-YzDnw16Yw8RXsT8jE3WqR11u-XY-LFkOwdLvWyb19Eiutz0lANMNMYXVhimy1fiFfAWixKUX_HYab72_eWh9gEG1SNi6mpwdxdpn6HLO9lL-l6spLGB9Vk-1ek4IDeXW8rEv4fP0T2kmzi9ytk389Mn8qOI83oiXbjIoeITDN7mTgCnd3yaWyGp6xs_R5oMG2QbJvBgOagiL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LJZJ08G9NyuwOl73yu-iBNEu3BLblw_P9MDyGZ2F8_L5GfCsnGv9d64Pj3aZO5ia7NuwCWUxzoQZUFIiAokRmCcPBCmSoKGD7Rilb0paTT0syGN5qCxDqzHkwgZucvInfnG6k2obiuEEJ5et96g1_SrthpzB8ySXTe2aWbezSqrfQlJaxGGqtsdPsJq35CJboE2LV9r8twpEH6Ept4sBdXegIUlR09K8H3-jsVpFRdHYDGSr9VrbOkfCK637PZ6SO4giaC2aya4IylHRXpJIwfdH_Ey4sOtojahygh3wg78VPTxCETuEc_YrJ2ZBSk9CAlwv5onKqWJtyo4Icfyghg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=mE58JjvlLY_LctyZFVqG7xkLNyPOCpOMdb0Rzf3VB_2y8RVq19cOB0GGVtH5omgU7tmA7p5khfPN0aBgpdt0NRaQQrmUKOIX_KPJqsjSMYtOCYCek1dKd5YqKsgKAiMI8iwpU5NbhUX449ndUr5uZ-bnBRBP299I0EN3UiGNmEWlPIbNZZY1rYh1Byolr-0WF0qxfwle4ZP4GOk-i1L8vFCghnqpPJOeaNuAkcDffW0LXrnp0n8GN9LpoRNaD5FA0_JgO2nskZmq9X4_pQqmzV_LxiBljYdFlwClY3auJ402QcSngMvpva1S6L56rGMi7ZKjrF4972dls58ga__0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=mE58JjvlLY_LctyZFVqG7xkLNyPOCpOMdb0Rzf3VB_2y8RVq19cOB0GGVtH5omgU7tmA7p5khfPN0aBgpdt0NRaQQrmUKOIX_KPJqsjSMYtOCYCek1dKd5YqKsgKAiMI8iwpU5NbhUX449ndUr5uZ-bnBRBP299I0EN3UiGNmEWlPIbNZZY1rYh1Byolr-0WF0qxfwle4ZP4GOk-i1L8vFCghnqpPJOeaNuAkcDffW0LXrnp0n8GN9LpoRNaD5FA0_JgO2nskZmq9X4_pQqmzV_LxiBljYdFlwClY3auJ402QcSngMvpva1S6L56rGMi7ZKjrF4972dls58ga__0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت گفت پاسخ تهران به طرح پیشنهادی صلح آمریکا احمقانه بوده است و او از ادامه جنگ و فشار بر ایران خسته نمی‌شود.
ترامپ در یک برنامه عمومی در کاخ سفید و در پاسخ به پرسش‌های خبرنگاران درباره طولانی شدن مسدودیت تنگه هرمز گفت: «احمق‌ها نمی‌خواستند قبول کنند. فکر می‌کردند من خسته می‌شوم یا حوصله‌ام سر می‌رود یا تحت فشار قرار می‌گیرم اما هیچ فشاری وجود ندارد.  ما به یک پیروزی کامل خواهیم رسید.»
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت، در پاسخ به پرسش خبرنگاران درباره آنچه او تغییر رژیم در ایران خوانده بود گفت: «در ایران میانه‌رو و دیوانه‌ها را دارید. دیوانه‌ها می‌خواهند تا آخر بجنگند.»
رئیس جمهوری آمریکا گفت جنگ خیلی کوتاهی در پیش خواهد بود. ترامپ تاکید کرد که میانه‌روها در جمهوری اسلامی از دیوانه‌ها می‌ترسند.
دونالد ترامپ از پایان هفته سوم جنگ می‌گوید با توجه به کشته شدن دو صف اول رهبران جمهوری اسلامی، تغییر رژیم در ایران پیشاپیش روی داده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد که در حال بررسی دوباره «پروژه آزادی» در تنگه هرمز است، اما هنوز تصمیم نهایی درباره اجرای آن نگرفته است. او گفت هدایت کشتی‌ها توسط آمریکا در تنگه هرمز تنها بخش کوچکی از یک عملیات نظامی بزرگ‌تر خواهد بود.
ترامپ همچنین درباره مذاکرات با جمهوری اسلامی گفت: «حکومت تسلیم خواهد شد.»
او روز یکشنبه نیز اعلام کرده بود از پاسخ تهران به پیشنهاد آمریکا رضایت ندارد و آن را «کاملا غیرقابل قبول» توصیف کرده بود. همزمان صداوسیمای جمهوری اسلامی اعلام کرد پیشنهاد آمریکا رد شده، زیرا به گفته این رسانه، به معنی «تسلیم کامل رژیم ایران» بوده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، به فاکس‌نیوز گفت واشینگتن در حال بررسی ازسرگیری عملیاتی برای بازگشایی تنگه هرمز است.
او افزود واشینگتن فشار بر جمهوری اسلامی را تا زمان دستیابی به توافق ادامه خواهد داد.
ترامپ همچنین گفت هنوز تصمیم نهایی درباره ازسرگیری «پروژه آزادی» را نگرفته است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در گفتگو با سی‌بی‌اس نیوز درباره پاسخ اخیر تهران به پیشنهاد صلح آمریکا گفت جمهوری اسلامی در برنامه هسته‌ای خود امتیازاتی داده، اما این امتیازها «کافی نبوده» و پیشنهاد تهران همچنان «بسیار ضعیف و غیرقابل قبول» است.
@
VahidOOnLine
دونالد ترامپ در واکنش به اظهارات بنیامین نتانیاهو که گفته بود «هیچ‌کس پیش‌بینی کامل و دقیقی» درباره تنگه هرمز نداشت، گفت: «من داشتم. من می‌دانستم آن‌ها تنگه هرمز را بسته‌اند. این تنها سلاحی است که دارند.»
ترامپ افزود آمریکا می‌توانست در چارچوب «پروژه آزادی» این گذرگاه را باز کند و گفت این عملیات می‌تواند از سر گرفته شود و در آن صورت «بسیار شدیدتر» خواهد بود.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده یک روز پس از مخالفت با پاسخ پیشنهادی جمهوری اسلامی به طرح آمریکا برای پایان جنگ، به فاکس نیوز گفت که ایران فنآوری لازم برای بیرون کشیدن ذخایر اورانیوم غنی‌شده مدفون زیر خاک را ندارد.
ترامپ در این گفتگو تاکید کرد که اورانیوم غنی شده ایران آنچنان در اعماق خاک تاسیسات هسته‌ای دفن شده که آمریکا باید آن را خارج کند.
براساس آخرین گزارش‌های آژانس بین‌المللی انرژی اتمی، ایران دست‌کم ۴۶۰ کیلوگرم اورانیوم با غنای ۶۰ درصد دارد که گمان می‌رود در تاسیسات هسته‌ای اصفهان مدفون شده‌اند. این تاسیسات در جنگ ۱۲ روزه و جنگ اخیر اسرائیل و آمریکا بارها بمباران شدند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده در اظهاراتی گفت: «مردم در [ایران] می‌خواهند به خیابان‌ها بروند. آن‌ها هیچ سلاحی ندارند، هیچ تفنگی ندارند.»
او ادامه داد: «فکر می‌کردیم کردها قرار است سلاح بدهند، اما آن‌ها ما را ناامید کردند. کردها فقط می‌گیرند، می‌گیرند، می‌گیرند. در کنگره هم درباره آن‌ها شهرت خوبی دارند و می‌گویند خیلی سخت می‌جنگند، اما نه، وقتی می‌جنگند که پول بگیرند.»
ترامپ گفت: «من از کردها خیلی ناامید شدم، اما ما برخی سلاح‌ها را با مهمات فرستادیم که قرار بود تحویل داده شود، اما آن‌ها آن را نگه داشتند. من گفتم آن‌ها آن را نگه می‌دارند، اما چه می‌دانم؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75408" target="_blank">📅 20:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZQaE7oGU9DInqHVhtyp_2QovQaBr8-MwwUq0HszDrBAjap5bAx3YUmOEvr_qXqgHQim3T2AkMMn24chPe_eaNlmBSHuMUkusZjA54KvuQ9WM8vGcUuGOrgvTO8_-7X6Sdzf1hXp7j7C1fbPnKXEUwgm7wWhJZ68KGuxIY3wwHud6vEJeWfBsQguTj4wBXQFcTrSTHyWlgaQ8cDdjMZgeyCZ1AlsK6ycdSsD-D4bMsxyxRba0ZCt1Q5jMC7Q3Yd9cDGQDBetMA-0-17nGu4sCzrvrTDPBx-QiwfMy2Tgz48r_B8XG5bCneBEvgJZCiJv3Zp8KlTt4l9s87v-fE9T-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BKKchqd0-IIEhe31uHxfbH36joAYWhteLv2la21DZFSIwN7iO-uXE3mEfXUsx-1xDxiQNIQApRi0QEQ9DG_tg9oJ_4W0_L06bZQSwkthkIzWo4HAbCx871TuzUiH2MsjbTziesnhRQIapkeXM-swc_oSeBVyiRUHrAmt_RHCPQVnNR5f9k4clubGCLHvE6OyMQP2FGLSl0CbOM25Z2kdNkvX-lTFdyNVHJ2aW5E_Pcwonaj1Ah7ehf446Ye5Y8x0jaz-jngNvJ2_nq1KfF1aL4SkgSAhoVV_RUpEJTeGExoVNih3-HGlCzOC_PgZSuCUj2kSHEDa2dScW18UoGNqsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">AmirKh1982
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/75406" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قطع اینترنت نه تنها ربطی به تأمین امنیت زیرساخت‌ها ندارد، که «اقدام علیه امنیت ملی» است.
در ۷۲ روز گذشته میلیون‌ها گوشی، کامپیوتر و سرور ایرانی از صدها پچ امنیتی حیاتی محروم ماندند و در معرض انواع نفوذ و هک قرار گرفته‌اند.
در این
#رشتو
بخشی از این آپدیتها را مرور می‌کنم: @
hamedbd_channel
hamedbd
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75405" target="_blank">📅 18:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC6N9nUVE7Lnx7h6mmTIVg6M24Xlc90oDIoowrgHxdHiO2PBoY86ieaB_vBVCGLTqzuVFA6lmEvCLjsYIVuzas7lldIfl04CmBgoyvL1MNiwzcOvExd3JSFzgsrcU8GO9Pn2G0RtIZge86DLApIVahULefpJtlctFfH2buyk0X9rQbibnsmgH-gdmJL2bg7DN_xtKchuJQrp3eU_CiqZtCOWapkt_Ri_CmDMzqu8P9Z6K8hCT7RWTGr5e-DwNMQUw3lWHSS2R_pf5OHS4KcKir7z0XGGEaTr2Se6SQWxj8PM8M9tSTmIA5Pv6q7q7w5dq7JxbxI_adprbyVgToljmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار روز دوشنبه ۲۱ اردیبهشت‌ماه در بازار آزاد تهران به ۱۸۲ هزار تومان افزایش یافت.
این جهش قیمت کم‌تر از یک روز پس از مخالفت شدید دونالد ترامپ، رئیس جمهوری آمریکا با پاسخ جمهوری اسلامی به طرح پیشنهادی آمریکا برای پایان جنگ روی می‌دهد.
علاوه بر پاسخ منفی ترامپ، بنیامین نتانیاهو هم اعلام کرد که کار اسرائیل با ایران هنوز تمام نشده و ذخایر اورانیوم باید از خاک ایران خارج شود. این اظهار نظرها احتمال برخورد نظامی دوباره را تشدید کرده است.
قیمت هر سکه طلا هم روز دوشنبه در بازار آزاد تهران به ۲۰۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/75404" target="_blank">📅 18:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gmnyDV9EaT-hog2AE4AT8YuWSNX0urYrwWnvf9PSEXmJ-FWLWmLvNXiQzGKaBUzRhaJDtMH_TvolPRDtGn5zIpX1pH64Y6ZGGuloCMVqQwSWd5dysNvVBHFej0x7TcpaDhrRfkdltQXgCErtsIOtmns6J6jz2qRpXh5BZ5RZEw3YqEVC0ZnJzeKnRiW7imWs1WzEVfy5BqlTBbecM15MM0d41vb6fMRapeMj475iWz_p5r0lO-WTR2mCXD3C9_ABIrE0y_52JmWJeGC-9GBcYUdbg786y5HHJzIWd3V444OP4Tl1X-Fzb8jC8BZPh6BOdsf_XgAbR_ETVaKWU9qSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l2zphs0TZYsSyrBKjjYXVV8vR3araTH9DE0XypoBSCGR8hbvikqp87KHQPklM44MW21_4ucgT0aI9S5lQR_FPeCceGgdGV7OgKSTn_AfqMIvWY5_e3a0t3Ni813MMUnGlvcBw7he2NHwqTRAdooJw0IJmVRIZghDWOFr2IC95UMluhBv1CJdlR-rhp9KFFSvsUtdzNajG_6KfG55UkI9IzeS8RgOvhFPekGfKCI09WGdsJvRIaM8ABr_ooEGqQ2dkfghFd7wIdEA_z5YkSJFt5OwN-WDAwDmOn5-Q5lHEIGAmJu5j-PTCd7_6EUsBWjp78FMO4fibFVYqn-j0Tnqfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😋
💩
«محسن محمدی عراقی» معروف به «محسن اراکی»، عضو مجلس خبرگان رهبری، انتخاب «سید مجتبی خامنه‌ای» به عنوان رهبر سوم جمهوری اسلامی را «کاری الهی» توصیف کرد و مدعی شد در روند این انتخاب «دست هدایت امام زمان» را دیده است.
@
VahidHeadline
«ابوالفضل ظهره‌وند»، عضو کمیسیون امنیت ملی مجلس جمهوری اسلامی، مدعی شد حکومت ایران به ظرفیت‌ها و سلاح‌هایی دست پیدا کرده که «بمب اتم» در مقایسه با آن‌ها «ترقه» محسوب می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75402" target="_blank">📅 18:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mNRpcg-9IjvrklQ3qty6tt0P2dDJsyM1bxp4k0WaqyQDBAyPi882kYZSoxNtLQzLuClOGwQSNDeH5Pmesk0BcFd31BCZ7Em3Z7g2Hleb6cKcCwjxrNqcLlqSsippYKufPglc6iU_Jl-avshAIXK1kPCmHEhMNFQcd9qTlaYoF4HX2Bvbj6f5QgIPK6Ul1dKEd7jgNb3Tpa8jvM7Xo8UDaoT3d1YGBEuXpROJqPLzE-RqMIA68ZkgjRL5MBAY-754ZFjxmdZfFWPOUJqVIk1-k-Nx5qfq3tM8N031MUUObno4fY-EawD4wUINB7MUkCFTuFWEaiz9HLbDKlgCZvnrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VFiljEsvY4WiLgbMdCn8Hp0CCpXTFvs_orW1Zk3zPj2bWDiI7JeXTwfffrH5gRfcZPobTKmo74NSZgtYX_1OmKXEr_oHGBz8Rs3hKIPACRoPbcJsvoDRoiSnneumRFQxLsIzcDMaMQXCIO-7WbjhjceHsUxZnee2chJMp5M7kF4CDFlZrHjL9JrNiXUhEwG9DVkbabLQqXwgLYKK6WXOiYKj11RvaiS3QiNoUZNaPOAZuU-m73RtOPaId7rtBxUdkMHb8TqYj7Yi31PmDP61SH6XrzqXAHqWJxAZwDuOI3pdeiJgZ8CBFhN2KuxUW-c-ZU2v277Tr3rtWvhbNdVqag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا تاکید کرد که از جنگ ایران حمایت نمی‌کند و افزود که شهروندان این کشور نگران افزایش قیمت بنزین و تاثیرات اقتصادی آن هستند.
کی‌یر استارمر تاکید کرد کشورهای دیگر می خواستند بریتانیا را جنگ ایران بکشانند اما او هرگز این کار را نخواهد کرد.
@
VahidOOnLine
دولت بریتانیا روز دوشنبه، ۲۱ اردیبهشت، ۱۲ فرد حقیقی و حقوقی مرتبط با حکومت ایران را تحریم کرد.
به گزارش خبرگزاری رویترز، این افراد به «مشارکت در اعمال خصمانه» علیه بریتانیا و چند کشور دیگر متهم شده‌اند.
در بیانیه رسمی دولت بریتانیا، از جمله این اعمال خصمانه به «طراحی حمله و ارائه خدمات مالی به گروه‌هایی که در پی بی‌ثبات کردن بریتانیا و دیگر کشورها هستند» اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/75400" target="_blank">📅 18:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKrcokT0YOom4vHMnftM6O86B975qCPSEHgFUatbSEhXo5v236TxFN6OQ-brAtAcV8Um79_yKbxiz8zMBctfLpgf73M1MUzLqWy1P45ObkColNTV3MUORn6146Hznr75xHPhfytKQdEtahYQ6fri_57Yo-4fCSwGDNns_DSZOUQM5BhEy9NIRScnooLHR1HwVS_HTOm7EJv5gM1vgtAPfPK8jtNkHl0egWLh0-F4Q3eJQuk8ae0kB53MPl_iFv6JVSnqbvIiXZUcPBLryBKM27AyaYsDkn8ik60VgOhvxGM5C4LneR6ZdqhoXd0E5za9UkuWdK0R1wuCleZAy2boWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی جعفری، فرمانده قرارگاه «بقیه‌الله» سپاه پاسداران، گفت: «تا زمانی که جنگ در همه جبهه‌ها پایان نیابد، تحریم‌ها برداشته نشود، پول‌های بلوکه‌شده آزاد نشود، خسارت‌های ناشی از جنگ جبران نشود و حق حاکمیت جمهوری اسلامی بر تنگه هرمز به رسمیت شناخته نشود، هیچ مذاکره دیگری در کار نیست.»
او افزود که با این سطح از بی‌اعتمادی به آمریکا، طبیعی است تیم مذاکره‌کننده با هدایت کلیت نظام، شروطی را مشخص کند که همه حقوق مسلم جمهوری اسلامی را تامین کند و این شروط «حداقل انتظارات» ما است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/75399" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u9PDPtC1jV51gGZ71oY7Ji-25xhRR__Js55WsH0hYJZlotm5KiKfh1IGjMx08ahA-_94cWCIomf-FW5j5ymL6Ck86OvbfcvETmSj3EjlvWxKjJBkv9Xb9xrFgIP4hWCIbTMYKiTNVWCKsr5z38zpSvFkvAjf-_KRIjqg7EXI_KAs4q9_iadKCDpJyjsCanC5PlyYC9zHKLNp4Fv99BXlAqGtElHwun2ZvpJPWjMe29Hhq99A3qkmgQDlJpyGsK28ccyHZO8H90-RMdhnO7G7wf1wCbSG0m8gROGFROTAyXNIpqtYVjP5H_iMEwiuiBnTADIINMYuQJUoRSrkRpuFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ezy1LhrLGlaNmC4B96kxUe7HK8BkU1qp2hdb4_XuAkBPN9fSl2k9BOjehEBODKn3UzE6_OW6svd5wKhJbf6JOzZxGF2aWRJvy3fQRyzD_RX-UJid0OFNG1xz4wHMFEL9bRLOtw9NTrmcRUEO8ZtTSF4xD72BoF94jctf628lB0j2AlzVvHyl4ecMEqBS8EWvfDzESl9COC9-aNR2FeTM4n_VVRoZ86lZFVsQoY6QjB-g-RIFbSg45KHHfG7wi6ZTQyt5DC9GfO6LgatyLJIR1BFg3pIgJ96WeDkTPvD5Gg9NgtGCVsc9cpuv8gFdQKC9gzomQTQocvK3cCLleb1Vqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=ZHFUEp0bpBvMDbW5eQSgecXX7P55H0p6juc3lXTN5bPv6HUzpdLv-5hpWbik3w9o4h3HeF0OybF4Fe9iltAiYMhdOr-JUH6OfJXXMeB9_AK6cLxkHcECiB7a4cM7WEIX49hc6jkbDjXffZ5foG181TnYBuZe9rOnm48TRkO8c0bdZ9B_k4SOVY1Q1RERci9O9WEyn6vpVXpQ3DaVxfBMxNfN1C4KfNS9DsfSPKRvQgQjakCKjuvsJgkE10Tzu53s28LtbcOW7p4EFY9hIueuRJ9g4PpbNHONWGKounkF0m2wq_yaIulkY9-xli0CY2HFxGoUX1iE_rqSpKVUQq2yhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=ZHFUEp0bpBvMDbW5eQSgecXX7P55H0p6juc3lXTN5bPv6HUzpdLv-5hpWbik3w9o4h3HeF0OybF4Fe9iltAiYMhdOr-JUH6OfJXXMeB9_AK6cLxkHcECiB7a4cM7WEIX49hc6jkbDjXffZ5foG181TnYBuZe9rOnm48TRkO8c0bdZ9B_k4SOVY1Q1RERci9O9WEyn6vpVXpQ3DaVxfBMxNfN1C4KfNS9DsfSPKRvQgQjakCKjuvsJgkE10Tzu53s28LtbcOW7p4EFY9hIueuRJ9g4PpbNHONWGKounkF0m2wq_yaIulkY9-xli0CY2HFxGoUX1iE_rqSpKVUQq2yhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نشست خبری روز دوشنبه ۲۱اردیبهشت۱۴۰۵ گفت در شرایط کنونی اولویت تهران «پایان جنگ» است و نه تصمیم‌گیری درباره آینده برنامه هسته‌ای یا ذخایر اورانیوم ایران.
او در بخشی از صحبت‌هایش بدون نام بردن از دولت یا فرد خاصی نیز گفت: «هنوز با کسانی که علیه ما تجاوز مرتکب شدند تسویه حساب نکرده‌ایم.»
بقایی در واکنش به اظهارات «ولادیمیر پوتین» درباره آمادگی روسیه برای انتقال ذخایر اورانیوم ایران گفت: «در مرحله کنونی تمرکز ما بر پایان جنگ است. این که بعدا در مورد موضوع هسته‌ای، مواد غنی شده ایران و مباحث مرتبط با غنی‌سازی چه تصمیمی گرفته شود و چه گزینه‌هایی را مد نظر قرار دهیم، موضوعاتی هستند که وقتی زمانش برسد حتما در موردش صحبت خواهیم کرد.»
او همچنین درباره روابط تهران و پکن گفت جمهوری اسلامی با چین «ارتباط مستمر» دارد و گفت: «چینی‌ها به خوبی از مواضع ما آگاه هستند.» بقایی مدعی شد چین نیز مانند جمهوری اسلامی، اقدامات آمریکا را بخشی از روند «تشدید یک‌جانبه‌گرایی» می‌داند.
سخنگوی وزارت خارجه جمهوری اسلامی در بخش دیگری از سخنانش، آمریکا را «بزرگترین تهدید کننده صلح و امنیت بین‌المللی» توصیف کرد و گفت: «جمهوری اسلامی ایران ثابت کرده قدرت مسوولیت‌پذیری در منطقه است. ما قلدر نیستیم، بلکه قلدر ستیز هستیم.»
اسماعیل بقایی با اشاره به حملات آمریکا و اسراییل علیه جمهوری اسلامی گفت: «حمله به یک کشور، از بین بردن زیرساخت‌های آن، ترور رهبر و شهروندان یک کشور، مصداق عمل مسئولانه نیست؟»
او همچنین در واکنش به انتقادهای «دونالد ترامپ» از طرح پیشنهادی جمهوری اسلامی، از مواضع تهران دفاع کرد و گفت: «ما امتیازی نخواستیم. تنها چیزی که مطالبه کردیم حقوق مشروع ایران است.»
بقایی در واکنش به صحبت‌های رییس جمهوری آمریکا گفت: «قضاوت را به مردم واگذار می‌کنم که آیا مطالبه ایران برای خاتمه جنگ در منطقه، توقف راهزنی دریایی علیه کشتی‌های ایران، آزاد شدن دارایی‌های متعلق به مردم ایران که سال‌هاست به ناحق محبوس شده، زیاده‌خواهانه است؟»
او همچنین گفت: «هر آنچه که ما در طرح پیشنهاد کردیم معقول و سخاوتمندانه بود و برای خیر منطقه و جهان است.»
سخنگوی وزارت خارجه همچنین مدعی شد که این وزارتخانه، از هر تصمیمی که از سوی نهادهای نظامی مانند سپاه پاسداران برای «تنگه هرمز» گرفته شود اطاعت می‌کند.
@
VahidHeadline
گزارش ایسنا:
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/VahidOnline/75396" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnApshLHkdvFnzaTlpWAT4u57pNNHrSHbMFG4zYe4i-ER7Lax2jjZJUyFUimyN9Bv80f2kl1J_pdoAv68jH2SQp6KswS4E-pQO2xsmjNoNXHTyqjse0vGAv8jlrDp4V22c0i0xIa0dDjpRks5H-Os4ZHM7zSb6sFX3Eih9nT4UQ4Ct2-ulviGzVoSOh1iX1bkisfA6MnA155ZyLmCl1zSBiowU0kfmq3hbzAesyXeepddPCNFVtvAS4eQXpZwlzDy9myZwIEC_C4DCfZGEXCcXzIsYX42_UGsKSqnERYUJ9xuB5pdHFJ8_G_AFR2xZdxPaCgwPwyojVNbDNXYDszAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار تصاویر ماهواره‌ای که نشان‌دهنده نشت احتمالی نفت در محدوده‌ای در نزدیکی جزیره خارگ است، سازمان حفاظت محیط زیست ایران می‌گوید: «منشا آلودگی مشاهده‌ شده در اطراف جزیره خارگ ناشی از تخلیه آب توازن آلوده یک نفتکش آسیب‌دیده بوده است.»
این نهاد گفت: «هیچ‌گونه نشت نفت از خطوط لوله، تاسیسات پایانه‌های نفتی و یا سکوهای متعلق به شرکت نفت فلات قاره ایران در جزیره خارگ مشاهده یا گزارش نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/VahidOnline/75395" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZwNzfNrkZk-eTCxYaGBAbdHDg8-2CdcNcS6SQw9FCaqlLFt4-9px7pNUoh9TNqY4K3BZntKljWSzGoc1UF3DefGY0AqSqV_xXWntM3f11BTyJA_NqYxgkpS7wGdI2HsWYanRf7k5TWRWUvhHs2tA1ZuyYuw5YQPi8J33Zi0noBhMEDK_0415piY29XH_ZBBR7FWCEKat8SDxW1Lom_y7FP2-j9qHmt1kBiK3NSOZ-GhXq-7pbcjdBduMZkwG0In2M5gz9TGgadzyW_WWNBj1HHTmga59LigqLvKTrQl35rxoKctBxZD3y0EBolRks7z-Y3Xo04NDcggBSMQK2I4ydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گزارش سی‌ان‌ان از اینترنت طبقاتی؛ «فکر کن با بدبختی وارد اینترنت می‌شوی و می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است»
♦️
سی‌ان‌ان در گزارشی میدانی با اشاره قطع اینترنت و رواج اینترنت طبقاتی در ایران می‌نویسد، قطع اینترنت در ایران اکنون بیش از دو ماه ادامه داشته و طولانی‌ترین اختلال ثبت‌شده تاکنون به‌شمار می‌رود.
برای میلیون‌ها نفری که زندگی و درآمدشان به اینترنت وابسته است، این وضعیت ویرانگر بوده است. فراز، ساکن ۳۸ ساله تهران، به سی‌ان‌ان گفت: «تصور کنید با بیکاری و تورم دیوانه‌کننده دست‌وپنجه نرم می‌کنید و به ترتیبی موفق می‌شوید ۵۰۰ هزار تا یک میلیون تومان جور کنید، فقط برای خرید چند گیگابایت وی‌پی‌ان تا بتوانید وارد اکس یا پلتفرم‌های دیگر شوید، خبرها را ببینید و صدایی داشته باشید.»
او افزود: «بعد وسط همه این استرس و خشم، وقتی بالاخره موفق می‌شوی اکس یا تلگرام را باز کنی، می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است؛ واقعا مثل مشت به سینه آدم می‌ماند.»
متوسط حقوق ماهانه در ایران بین ۲۰ تا ۳۵ میلیون تومان برآورد می‌شود. سی‌ان‌ان می‌نویسد، اینترنت پرو، شکاف عظیم میان فقیر و غنی را عمیق‌تر کرده است.
وب‌سایت «خبرآنلاین» نوشت این طرح «جامعه ایران را به دو طبقه متمایز تقسیم کرده است: نخبگان دیجیتال که از اینترنت سریع و بدون فیلتر برای تجارت، آموزش و ارتباطات بهره‌مندند، و رعایای دیجیتال که در محدودیت شدید، سرعت پایین و هزینه‌های سنگین بازار سیاه وی‌پی‌ان گرفتار شده‌اند.»
قیمت وی‌پی‌ان‌های بازار سیاه به‌شدت افزایش یافته و بر اساس اعلام سازمان «فعالان حقوق بشر در ایران» مستقر در خارج از کشور، قطع اینترنت طی دو ماه گذشته حدود ۱.۸ میلیارد دلار به ایرانیان خسارت زده است؛ رقمی که با برآورد اتاق بازرگانی ایران نیز همخوانی دارد.
روزنامه اطلاعات نوشت: «قطع اینترنت ــ که خود منبع درآمد شمار بسیار زیادی از کسب‌وکارهای مجازی بود ــ وضعیت بحرانی و پیچیده‌ای ایجاد کرده است.»گزارش‌های داخل ایران نشان می‌دهد «اینترنت پرو» از طریق «فهرست سفید» در سطح اپراتورهای مخابراتی و بر پایه «سیم‌کارت‌های سفید» عمل می‌کند؛ یعنی برخی سیم‌کارت‌ها، حساب‌های موبایل یا نهادها از سیستم فیلترینگ کشور مستثنا می‌شوند.
برخلاف وی‌پی‌ان که با رمزگذاری ترافیک اینترنت سانسور را دور می‌زند، «اینترنت پرو» ظاهرا کاربران تاییدشده را از مسیرهایی با محدودیت کمتر عبور می‌دهد. گفته می‌شود دارندگان سیم‌کارت سفید همچنان به اینترنت جهانی کامل دسترسی دارند.
بر اساس گزارش‌ها، هزینه اینترنت پرو برای بسته سالانه ۵۰ گیگابایتی حدود دو میلیون تومان است، علاوه بر هزینه فعال‌سازی ۲.۸ میلیون تومانی و حدود ۴۰ هزار تومان برای هر گیگابایت اضافی. در مقابل، اینترنت عادی ــ که اکنون به‌شدت محدود شده ــ هر گیگابایت حدود ۸ هزار تومان هزینه دارد و همین باعث شده بسیاری ناچار به استفاده از وی‌پی‌ان شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75394" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGi5ZV6B4m4uUq-bS-djKQmt44_4pT_Uzu_IYUAUSSod-zQr1puSp4adu2uvJ8rupzqWlT-RmPlXLweKdBB0jmYdI9dH8CByD3IgLCYX4B9gTzqdpkvy9WQ89bg3alCysG-V8kGxpeJvPGQua_Xzzfbyx2R9oYAavTVRiq0jBfnbpc6dzJUu_6aad6irC7S4EgsnsqSSQYkmUiCRe1-vAU3LpyeNSm3Abn63VsPRS1v9VWEmGCuP0vxVy493-3JM4uewImwxxmhDrpfFWUOh1JY3kfC_5pPaqD6hq9ylnX0SsKigAT7PKX0IB-j-dtO5spuHkZl6gfMkuOYU1xhZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، صبح دوشنبه، ۲۱ اردیبهشت از اجرای حکم اعدام عرفان شکورزاده، زندانی سیاسی، با اتهام «همکاری با سرویس‌های اطلاعاتی آمریکا و اسرائیل» خبر داد.
شکورزاده بهمن‌ماه ۱۴۰۳ از سوی اطلاعات سپاه با اتهام «جاسوسی و همکاری با کشورهای متخاصم» بازداشت و به اعدام محکوم شد و حکم صادر شده علیه او به‌تازگی در دیوان عالی کشور تایید شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75393" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/InQ0Gll1n4oG_G6CtqrjyVtHgAmO5qA2rBA3eYz8HcKdW95rpABKYUjdlFkuoRwSKuB9eQWGA0l8uDymkvk0M5KJOuTm-uUBNTDLZN2w0DTTdMkP4yPLDJEl9kdRaAJdyF2tV73tqXAnbAnf6JGN8goO2DKMdZS20hrHdEuosGrfVpArcHjhNAzcfp7kMPfn1kyGDEAO_CJhJnJ1ZZckFIhEHGXENOzYJWybk6u2V7Udcbg8Cwwj_P033kEuH-B3G0SGbiL2LYwObrkfFCqxLVkXA7GfA-Nd_AY76ce3XTLInpEYTpVSDW7hdF0YQv3Gt6-5DALV4u36MW8Oj9X6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I98SiNBkTuAAM2ubRGJ02-eKpA5RTqPINz_Q90xGymnWhzphJCCytBhDORjBHqq8cYyPZnvUtEpVhGeFgnmV0F0cv7R3Xm9k_0jcwCjulo_kScxAXFEVCqxZZjo9zQK89xVIINd6GN2CKsDPmERdzIq17AVhXTz86mrJs6wqcMRY0deNzRsVZBwsEYe9tf0BQYsAVii-i9KGn2w0LFXOiB57t1xuWHm-1_fN7qAi0hlhUipcmdN6CTIFEm2DExnXUUVfflqGdEXYhji73bAeU0NpcAfRA4mbSVdNcokufDduVAY5Ft6HvaAf9BB17BUUNykBed41OeTEf0TqEkef_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس
: پرزیدنت ترامپ روز یکشنبه در یک تماس تلفنی کوتاه به آکسیوس گفت که پاسخ ایران به تازه‌ترین پیش‌نویس توافق برای پایان دادن به جنگ را رد خواهد کرد.
ترامپ اندکی پس از این تماس، در پستی در تروث سوشال، پاسخ ایران را «کاملاً غیرقابل قبول!» خواند.
ترامپ به آکسیوس گفت روز یکشنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده و در میان مسائل دیگر، درباره پاسخ ایران نیز گفت‌وگو داشته است.
او درباره نتانیاهو گفت: «تماس بسیار خوبی بود. رابطه خوبی داریم.» اما افزود که مذاکرات ایران «مسئله من است، نه مسئله دیگران.»
ترامپ در این مصاحبه کوتاه روشن نکرد که آیا قصد دارد مذاکرات را ادامه دهد یا احتمالاً گزینه اقدام نظامی را در پیش بگیرد.
سناتور لیندسی گراهام، جمهوری‌خواه از کارولینای جنوبی، در ایکس نوشت که ترامپ اکنون باید اقدام نظامی را در نظر بگیرد؛ موضعی که گراهام در سراسر آتش‌بس یک‌ماهه بارها تکرار کرده است.
او نوشت: «با توجه به حملات مداوم آن‌ها به کشتیرانی بین‌المللی، حملات پیوسته به متحدان ما در خاورمیانه، و اکنون پاسخ کاملاً غیرقابل قبول به پیشنهاد دیپلماتیک آمریکا، به نظر من زمان آن رسیده که تغییر مسیر را در نظر بگیریم.»
گراهام نوشت: «پروژه آزادی پلاس همین حالا خیلی خوب به نظر می‌رسد»؛ اشاره‌ای به عملیات دریایی برای هدایت کشتی‌ها از تنگه هرمز که ترامپ پس از کمتر از ۴۸ ساعت به‌طور ناگهانی آن را متوقف کرد.
@VahidOOnLine
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، روز یکشنبه، ۲۰ اردیبهشت‌ماه، به نقل از «یک منبع مطلع» در واکنش به پیام ترامپ مبنی بر «کاملا غیرقابل قبول» بودن پاسخ تهران به پیشنهاد واشنگتن، نوشت: «همین الان واکنش به اصطلاح رئیس‌جمهور آمریکا را به پاسخ ایران دیدیم. هیچ اهمیتی ندارد؛ کسی در ایران برای خوشایند ترامپ طرح نمی‌نویسد. تیم مذاکره‌کننده فقط برای حق ملت ایران باید طرح بنویسد و وقتی ترامپ از آن راضی نباشد، قاعدتا بهتر است». تسنیم نوشت: «ترامپ کلا واقعیت را دوست ندارد؛ به همین دلیل مدام از ایران شکست می‌خورد».
@VahidOOnLine
خبرگزاری صداوسیما گزارش داد طرح تهران که ترامپ آن را «غیرقابل قبول» خواند، بر ضرورت پرداخت خسارت‌های جنگ توسط آمریکا و حاکمیت جمهوری اسلامی بر تنگه هرمز تاکید دارد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75391" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/puyv2nkoUqdQKbJMjt3mdSCRZp3ziyn3_Rbx07ut7jSEmMDy9lm47SJAC9NTdIkVN-fffJdipEJy_1N_bJSnW6v-bS0zrAE33axNdAK-VyWoQIxtHmsROCROQGoy9khe8VYntdFC_8zsWM3PbSl_94LFpHdLS28wyfz5G88PjuOq-SZrJw3QM6SY-etyyW_MhS7UDASzNtOvzcXbL0CxvyZzAQyUDcfrQ-2uS5lfhF2vIFqdaljRCZXrTT75BjOpBCZc312gLUvmSYLev95R1vBqNzyys5b7w29tKBygPOmxKkcVcJqtxPc1HMFK_qPEtWp5HA8YdHGL6ML85GLerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ پاسخ جمهوری اسلامی را رد کرد
پست ترامپ، ترجمه ماشین:
همین حالا پاسخ به‌اصطلاح «نمایندگان» ایران را خواندم. از آن خوشم نیامد — کاملاً غیرقابل‌قبول است! از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75390" target="_blank">📅 23:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqhYzmCa-vkD3N3O2LhbAy-66uXQ-nJhDY7-_qbhtkDINvpogA2Do3SA9awz5Kr133dQWZULYui-ZSwycN_jIQj6JHbE7s14AWTcybaFZY2l2P-Sxyoe0zFuGkPrSRwjYMwDtQYkm-fhkzpcd9ns3g1zKMP8XlMh9Se6kzDlW5G2F5BB4cxs-FtA97Ky7ZBXFnMnFZgWv2nlYkIZo_I7FlTfrN2tgx6tyso7newC5f1-7tj27hmdO2u7XjawLoJK3jiv3cMvZKZFUC8j-9YMeafe-Xj7XQALVpxkoSZ1pta5oHC_6lSMU84nShA7e7wAwuX6XgUBj_NFte_oufWuYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال، شامگاه یکشنبه ۲۰ اردیبهشت ماه، به نقل از منابعی آگاه، جزئیاتی از پاسخ ایران به پیشنهاد صلح آمریکا را منتشر کرد.
به گزارش این روزنامه، پاسخ ایران که از طریق پاکستان به‌عنوان میانجی به واشنگتن منتقل شده، همچنان اختلاف‌های مهمی میان دو طرف باقی گذاشته است.
به گفته منابع وال‌استریت ژورنال، تهران حاضر نشده از پیش درباره سرنوشت برنامه هسته‌ای خود و ذخایر اورانیوم با غنای بالا تعهد بدهد.
ایران پیشنهاد کرده مسائل هسته‌ای طی ۳۰ روز آینده مورد مذاکره قرار گیرد.
مقامام‌های ایران همچنین برای رقیق‌سازی بخشی از اورانیوم غنی‌شده و انتقال بخش دیگری از آن به یک کشور ثالث اعلام آمادگی کرده‌اند.
وال‌استریت ژورنال گزارش داد تهران با برچیدن تاسیسات هسته‌ای خود مخالفت کرده، اما در عین حال آمادگی‌اش را برای تعلیق غنی‌سازی اورانیوم اعلام کرده است؛ تعلیقی که به گفته این روزنامه، مدت آن کوتاه‌تر از توقف ۲۰ ساله پیشنهادی آمریکا خواهد بود.
بر اساس این گزارش، ایران در پاسخی چندصفحه‌ای به تازه‌ترین پیشنهاد آمریکا برای پایان دادن به جنگ، خواستار پایان درگیری‌ها و لغو محاصره کشتی‌ها و بنادر ایرانی شده و پیشنهاد داده است تنگه هرمز به‌تدریج به روی رفت‌وآمد تجاری باز شود.
وال‌استریت ژورنال نوشت ایران در مقابل، خواستار تضمین‌هایی شده است که اگر مذاکرات شکست بخورد یا آمریکا در آینده از توافق خارج شود، اورانیوم منتقل‌شده دوباره به ایران بازگردانده شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75389" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsuAmgBjTNBv8Lga1wnYVGFka8__GzA4z7zLRYtUIGKNVEoScLYDcxoSiYVqso130KoHGRp_E4r-5J2V9ZSNSe1YxUCN30DxejuykIyDI9DY1u4rkJKJQ4Q8CpelPXsAQM-x5EZx-f558Sg7QC8nHceReL87X9Q6l9sFHSL_8C4U9yGDgLCMBt3d3LXHIj_JvU0pmWAVmxnqz1LwEW6h7VlbbEZMKgNp7j31jY4_AwMjBKLp4BU4YrCxrSkGCgWiCPzfxvyvRiQk5w0L5Unui_sZUowLMI7CRJA0c3aWgQc5X7x1L0_tC62mll4heiMPyJekiW91zQyAeQ5tSB7KWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران شامگاه یک‌شنبه با اشاره به شنیده شدن فعالیت پدافند هوایی در اندیمشک و شمال دزفول از سرنگونی «پرنده متخاصم دشمن» در اندیمشک خبر دادند.
شهروندان نیز یک‌شنبه ساعت حدود ۱۰ شب از شنیده‌شدن صدای پدافند در این شهر خبر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75388" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">#دزفول
#اندیمشک
پیام‌های دریافتی از شنیده شدن صدای پدافند:
پیام ساعت ۲۲: دزفول حدود 20 دقیقه صدای پدافند میومد
دزفول وحشتناک صدای پدافند اومد.جدود ساعت نه ونیم
سلام پایگاه چهارم شکاری دزفول از ساعت ۲۱:۳۰ تقریبا یه ریز پدافند فعاله
پدافند پایگاه وحدتی دزفول فعال شده از ساعت ۲۱.۵۰ تا الان ۲۲.۱۷
فعالیت  شدید پدافند در اندیمشک ساعت 22.15
اندیمشک
ساعت 22:19 امشب پدافند فعال شد در حد 30 ثانیه.
یه صدایی میاد انگار پهپاده
سلام، اندیمشک ۲۲:۲۲ دقیقه چند دقیقه ست پدافند ها فعال شدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75387" target="_blank">📅 22:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QvDqd7bFjsixRPho5bl24Nv715VVd-N0ycYQIjF6X48PzooPplW4cNXg_sB4JEaBmL66hIwzEDF0zsgN9g1GNXywA1hAQAAPx_26FHen2U3Y0fKmSidfmwr_FSIOORoYEVd5_j1vcUeEfXxynrquM-eLHvDbjLRNctqLLt-VYBo1Hdrm9jNFMzbXHOhWC8tvAi904n3-HL6jHTGQjl85vz8CLU5jg5zTIfYkA6zFIFiXgkAO1gjf19Tt_AWcPVdz7avhnFcKhzbGcyk3vmi7oG6TrkR4BiVfLVrN7jgu0G5Myy63drLB6eEJa6QX-9yopLLu8xH1L81YhOE9SxbF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آن‌ها دیگر نخواهند خندید
پست تازه ترامپ پس از آن که جمهوری اسلامی گفت پاسخش را از طریق پاکستان ارسال کرده. ترجمه ماشین:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است؛ «تعویق، تعویق، تعویق!» و سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به گنج رسید. او نه‌تنها با آن‌ها خوب بود، بلکه عالی بود؛ عملاً به طرف آن‌ها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه، بزرگ و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار، و ۱.۷ میلیارد دلار پول نقد سبز، که با هواپیما به تهران منتقل شد، مثل هدیه‌ای روی سینی نقره به آن‌ها داده شد. همه بانک‌ها در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند. آن‌قدر پول بود که وقتی رسید، اراذل ایرانی نمی‌دانستند با آن چه کار کنند. آن‌ها هرگز چنین پولی ندیده بودند و دیگر هم هرگز نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما پایین آورده شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آن‌ها بالاخره بزرگ‌ترین ساده‌لوحِ همه تاریخ را در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی پیدا کردند. او به‌عنوان «رهبر» ما یک فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
ایرانی‌ها ۴۷ سال ما را سر دوانده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای خود کشته‌اند، اعتراضات را نابود کرده‌اند، و اخیراً ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند و به کشور ما که اکنون دوباره بزرگ شده است، خندیده‌اند. دیگر نخواهند خندید!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75386" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm6iCqMCxwTSsK4IKN60q7cXEfnaVmHxMZWn9zL43qTuJKnnud5W3QFdOJ_Gk_78nYtLwW9c7UOAdvuCBysburofB1l5rG47jHKwTLkoYC2uoacatD4g9GFvo7U7cCoILTl4CiYZ5_gEP2_jfDqPB-cq8AN96sZz6norX3_8LtJsofNKgGdTazf4kwG6E4Ys9S_FvwRfzJGGlkM_ERbuJOWCuwp88WyGXrj6-XVE6en_28mNty6zaKKrFLLmHe87yhRZmlA4QD0mqy01_VFJB2ZFeRfdWQuFYQGprarLJpeWLzsfPVQxQLblgp7DDDx5BBZQXHlK4I_Jj9KtoOOsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در بخشی از یک مصاحبه که قرار است ساعاتی دیگر مشروح آن پخش شود، گفت که ذخایر اورانیوم غنی‌شده ایران باید از بین برود تا بتوان گفت جنگ آمریکا و اسرائیل با ایران به پایان رسیده است.
او در بخشی از گفت‌وگو با برنامه «۶۰ دقیقه» شبکه سی‌بی‌اس گفت: «این [جنگ] هنوز تمام نشده است، چون مواد هسته‌ای، اورانیوم غنی‌شده، باید از ایران خارج شود. تاسیسات غنی‌سازی هم که وجود دارد باید برچیده شوند.»
او همچنین گفت: «ایران هنوز از نیروهای نیابتی حمایت و موشک‌ بالستیک تولید می‌کند. بخش عمده‌ای از اینها نابود شده‌اند اما کارهایی باقی است.»
آقای نتانیاهو در پاسخ به این پرسش که این اورانیوم چگونه باید خارج شود، گفت: «وارد می‌شوید و آن را خارج می‌کنید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75385" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qbhsyMlATUJTxP1MA5CKCeUdP7rArVLhzgO1MkMQlSDfQqG-lOFx2rs0UyHZ_sgH83jCVyh5N86kzysgZwGURR06uovVbr4sNbZtPBJ7DT2poivMlCg9xmgxhgE0ABbzcb0bn2YuGb_96ZCmp571K7umIALv89RUQsHeAQxNTc7vvyBdLTWHu7y5zdJJQ9PxHfV-ktDb82XXctmTNoAmTpIoTSEQBraGT2jKntnciPA6SYj2tQiE38mifo_h-H7dS4-eQ8Z2k80EvFV6_cmY12m-hUn8alCdhwIoQMl_M4JygFcM4BHpZyw1RC6JR8a19qlyKHu7w2OZ2Y_E4NKfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Afkham_minus
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75384" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYNHzpcL7e_Cm0EK0N8KvaEC7Euf7wQk3sWGQojd4a6_S4PwED2CWCp8iAN8JhTXlGgL_uhPIACHUPn5Yt-OUKRSD9oz8DuPf0Bb33CHVKA3U5HAPRXuqA2xsCKcXwL3d8_xQbMYm6PP2ptxGmQ0Watd-ZxRimdgIqNtyc3jkbfHvPn3M5rRmUH5l0VAmqNSW3tksVHv-k-g0lZzyIbiVWUyWj1YGJBMGwesyAWS7xWLLwn1YCsO2ilddU8SIIQt5qdqD-yLiJjx0Q9PCvWOb9bi_-nQRb4j_qvNjSO6bfSIqiyiuE6pTj72hPexDY8jgNd4EhZQWrtcGmJIhuz_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیم نادعلی، معاون فرهنگی سپاه «محمد رسول‌الله» تهران گفت: «در جشن بزرگ پیوند آسمانی زوج‌های جان‌فدا، خودروهای جیپ جنگی برای جابه‌جایی عروس و دامادها در نظر گرفته شده که با گل‌آرایی، پرچم جمهوری اسلامی و تصاویر رهبری تزئین شده و زوج‌ها در این خودروها در مراسم حضور خواهند یافت.»
او افزود زوج‌های شرکت‌کننده قرار است با «ماشین‌های عروسی به شکل جیپ نظامی» و «خودروهای نظامی گل‌کاری‌شده» در سطح شهر حضور پیدا کنند تا «فضای شهر را به یک شکل هنری و نظامی» درآورند.
به گفته او، هدف این است که نشان داده شود این «زوج‌های جانفدا» جان خود را «زیر پرچم جمهوری اسلامی تقدیم این نظام خواهند کرد» و «از هیچ چیز نمی‌ترسند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/75383" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JRN0PlJQjrtVxxDM4VDf7x1r_sOZoFzdbT7dSdJaPoMDMSghB5wZlCuwJtLU9ajG2yKSrptHLtbzGFin7GUQDuVFTdnUSTO9xxHteUhuOBOjth9wlj3MfRvk1OXpiLkw1vMk6zKUEF-y5HHsJoYw4ORbgFG3H7F29rkX1gtS1F1QSMxHZmFqHaeCQKQW14QVfjne_b_h3nqNLf4Nd4omP7FpL1u8D9sLkZwUb3blxmJCvqrv1q_VKAPXONAh07efOl953anCzpBh--XTlTb7DmCqDJS0-nbC19NIT_NC7Ob1IKqYWPFI7ji-vxH_kn-doFcgn6GXmqGisotjnWFI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vlrx6c8-hR0cUs9A3wP8aNmOVzN68gq8OQHIMDieKRAglBpXdPsaGrdOItWn7VyFjtK_bG_rZLaiFrcx5pHMfCChcr2Uq_JlpUI5jxhTTlt_9AoLpDJ6BmQh23cAr2CQrMJndvCznP7e2lcKbtjMfTsxhStMlrkSv259y6KjftGjYooXK9SbihRtpYRg1k3UgCOBngBATDY1Qrw0leGBmji1mkG5Cu8E9MbI5sPvEDJL6_ALV11TjaHq7i0cBQX8P6IoIq4dWpz9-R69thVom8_iZRxJiVdJ0vYcLlO1aQ0zAttZnOMbT8z6uNVVi9LRHcwDpqCCOXtutAi7vyT3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o6C8etT931VNjFkHf3QjorcWfQ-xSWTUx1JUfohR1a-rVoMA1F0YwGf3reN5Chd871R6-E3x_ni6PQ4Io1Tk1O3sMqe2JAJLyoThT9Q-JKR4Nf-L3T41QoZPrYvuMvoDT1RsfFuwnXkdUzFR3oRfToDgZXcvb93nbeZFbCjIXeXlrmPyHlSSgcLjIXwNz22iqPS2ga2rCdXaJAhrSJ8NT7279aoNp3ARvTgENJAQ2CsaEcd1tu8GC6GUS0N6T_kdrKhCB7XueTkNq5Xx6jUE-BcOApsJ_u58pbZqFAalDPR5V7MtftOOKhezW-W-mpNOPMSw1gyzfiXjerMJrIaNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ppmEdpRlcuAp4VTJGLdKm-HGoyE-M_cibCy_Orc0g6VTZgaPYFd9GyO-FE1i9B2giXhZ1fz41J5DlEkgUlvKLFNFhbWwzJkM_eXZq1BNX-Ey4MUMyUmLnr0uDqPB-463cCeIMe_u8VSHroKckmF8GPSLaItwDo3qZv-a_csZykwRlQxuGcxt7yXmnILwnJhbgtCVp8pGPrqQpgtIbnTpCElDrtx_emy5-MAUk34wL96ybkHSqeyFccD-r2X3Uybb_B3Cm11igYzC6THmDNh1xz6lGFZMMMAzOoZJgzupX4OxtE5Uy8ZwtCtpzsfpqGC_mxhDJTIGj8FiWsUXuQ-76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X_TAWGYnAE3aoXjELsk0vP9l4GtdEOQ6hNwxxOS0lUEupXmacJUjdff2WJhH9VAKUe3TgHi_uIM0S3xS0mdTk1MGb5W_WnBZ5JCutrzIU_TRcpmUURrB1LUUKJco_wy86JSEtrpcfurQ55lZE6V7d62DEqzTL9KzTcnijHTLf8Omk4mhqqjU_41JsuMEfB618GVPT66kAkPGOcqNbcqU2maN_WoYIP49z-_SQnCB7sXRD6Td6hGzwWZD001zjEPaVxMMMMxurTXiIyIPVYfTyZZNkWJoHxcLg1BvBeyMXfuA7PUx96c1pY7mUWCmAnndr1lGsMnIUDtYk61yiSVPgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید عملیات نظامی در ایران تمام نشده و ارتش ایالات متحده می‌تواند اهداف دیگری را نیز هدف قرار دهد.
دونالد ترامپ در گفت‌وگویی با شریل اتکیسون، مجری آمریکایی، که هفته گذشته ضبط و روز یکشنبه ۲۰ اردیبهشت پخش شده است، در پاسخ به این سوال که آیا عملیات رزمی در ایران تمام شده است، گفت: «نه، من چنین چیزی نگفتم. من گفتم آن‌ها شکست خورده‌اند، اما این به آن معنا نیست که کارشان تمام شده است. ما می‌توانیم به مدت دو هفته بیشتر هم وارد عمل شویم و تک‌تک اهداف را هدف قرار دهیم.»
او با اشاره به این که در حملات آمریکا و اسرائیل طی جنگ اخیر «احتمالا ۷۰ درصد» اهداف مورد اصابت قرار گرفتند، افزود: «ما اهداف دیگری هم داریم که احتمالاً می‌توانیم به آن‌ها حمله کنیم. اما حتی اگر این کار را نکنیم، سال‌ها طول می‌کشد تا آن‌ها دوباره بازسازی شوند.»
به نظر می‌رسد اظهارات آقای ترامپ پیش از ارسال پاسخ ایران به آخرین پیشنهاد آمریکا برای این توافق انجام شده است. هرچند که او پیشنهادات قبلی ایران را رد کرده بود.
رئیس‌جمهور آمریکا در مصاحبه با شریل اتکیسون همچنین دربارهٔ اورانیوم غنی‌شده ایران که در عمق زمین و در تأسیسات هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون شده‌اند، گفت: «ما در مقطعی آن را به دست خواهیم آورد… ما آنجا را تحت نظارت داریم.»
ترامپ اضافه کرد: «من چیزی به نام نیروی فضایی ایجاد کردم و آن‌ها آنجا را زیر نظر دارند… اگر کسی به آن محل نزدیک شود، ما مطلع خواهیم شد و آن‌ها را نابود خواهیم کرد.»
او بارها اشاره کرده است که توافق با ایران باید شامل تحویل ذخایر اورانیوم غنی‌شده ایران به آمریکا باشد. تهران چنین درخواستی را رد کرده است.
@
VahidHeadline
رئیس‌جمهور آمریکا گفت: «ما نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد، چون آنها دیوانه‌اند. نمی‌توانیم اجازه دسترسی هسته‌ای به آنها بدهیم. اوباما این کار را کرد. اگر من توافق هسته‌ای ایران را لغو نکرده بودم، الان سلاح هسته‌ای را داشتند و الان علیه اسرائیل و خاورمیانه و شاید حتی فراتر از آن استفاده می‌کردند. می‌دانید، آنها در واقع موشک‌هایی دارند که دیدید می‌توانند به اروپا برسند.»
از آقای ترامپ سوال شد آیا این درست که عملیات رزمی علیه ایران تمام شده است.
رئیس‌جمهور آمریکا پاسخ داد:«من این را نگفتم. من گفتم آنها شکست خورده‌اند اما این به این معنا نیست که کارشان تمام شده است. ما می‌توانیم دو هفته دیگر هم وارد عمل شویم و هر هدفی را بزنیم. ما اهداف مشخصی داریم که احتمالاً ۷۰ درصد آن‌ها را زده‌ایم اما اهداف دیگری هم هستند که می‌توانیم بزنیم.»
آقای ترامپ گفت حتی اگر هم این کار را نکنیم، بازسازی سال‌های زیادی برای ایران طول می‌کشد.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با سی‌بی‌اس نیوز درباره اورانیوم غنی‌شده در ایران و جنگ علیه جمهوری اسلامی گفت دونالد ترامپ به او گفته می‌خواهد وارد آنجا شود و به نظر او این اقدام از نظر عملی امکان‌پذیر است. او افزود اگر توافقی حاصل شود و بتوان وارد شد و این برنامه را برچید، این بهترین راه خواهد بود.
نتانیاهو از پاسخ به این پرسش که در صورت عدم توافق چه رخ خواهد داد خودداری کرد و گفت برای این موضوع جدول زمانی تعیین نمی‌کند، اما این ماموریت را بسیار مهم دانست.
IranIntl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75378" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikBhcKj3hzfKDBTV2DbixrXRGG5gH60COSXjE7lRyfZ9VsPKYrWT1UfpJ98QJ7fIc2NnhrbuE-41EJxU1a1FRYZp0Wmp5bC9Gmi_uOz1eSjIfw94GN2IYUSN_xRNqHdHNUI1rwBW3fdSHI94jyFwsI2IgKbZuMFa-ggrQyXp9FRPcxSW6q3eimE-RmUMKZpj1waeT-IIdrAe30aa5hVE0OzrX0iH3AokKH1GFkaPnVVwky1-YPlw3cvcJdGvtO5BmBQseg5wAhQShMaD6RsI9esw2hn8PnaGYS3L3qk7W5JK_gR5aFdzcAlCTQtPFUHFMvPn3O4ej3dBndu7JaWvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایرنا، روز یکشنبه ۲۰ اردیبهشت ۱۴۰۵گزارش داد پاسخ تهران به آخرین طرح پیشنهادی ایالات متحده برای رسیدن به توافق بر سر پایان جنگ، برای پاکستان به عنوان میانجی مذاکرات ارسال شده است.
ایرنا بدون اشاره به جزئیات بیشتر نوشت: «بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.»
وب‌سایت اکسیوس و خبرگزاری رویترز، چهارشنبه هفته گذشته گزارش دادند که واشنگتن و تهران به یک «یادداشت تفاهم یک‌صفحه‌ای» برای پایان دادن به جنگ نزدیک شده‌اند.
رویترز نوشته بود در این تفاهم‌نامه حتی به تعلیق فعالیت هسته‌ای ایران یا بازگشایی تنگه هرمز که از سوی سپاه پاسداران بسته شده، اشاره‌ای نشده است.
در مقابل، روزنامه وال‌استریت ژورنال گزارش داده بود که در طرح پیشنهادی آمریکا، تهران باید ثابت کند که به‌دنبال سلاح اتمی نیست، تاسیسات فردو، نطنز و اصفهان را برچیند، فعالیت زیرزمینی هسته‌ای را متوقف کند و همچنین بپذیرد غنی‌سازی را تا ۲۰ سال متوقف کند.
رییس‌جمهور و وزیر خارجه آمریکا روز جمعه گفته بودند جمهوری اسلامی تا پایان همان روز قرار است به پیشنهاد ایالات متحده پاسخ دهد.
@
VahidHeadline
ولی جمهوری اسلامی به جای جمعه، روز بسته شدن بازارها، صبر کرد یکشنبه پاسخ داد که ساعت ۸ شبش به وقت شرق آمریکا بازارهای مالی هفته کاری رو آغاز می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75377" target="_blank">📅 17:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6IXXmOnHx8obSRzv8Bq5JzNpfl_CfyV27L2RJNcyRsbCeVL1rs7Bpj5dMzozvukeP1Rebh9OC1PcxXF7oqJpK_JVjh9tbNKL_qzvMjIvOuiC5lpiFBykuu6N3imEGKgKK0JRgYhtB9Mpo-Hca4rQUqWlAcD2h_KL23w8R8q9hKPSLX6pukhOsCWsw9xOwMy_Hna_zaY25a4Cm9_sJeN4wW0tcAUwIHW9y7dxxnHRpIR7qHxvlnrk-3h5yS02s-tar_si8gsltqbTnkRqhGrALJqiP5ylyyqonSavTXaAp5EA_NI4kr4YeqI0G6uvBb7_dxwOIe5V1An2cNDCneOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی روز یکشنبه ۲۰ اردیبهشت اعلام کرد که سامانه‌های پدافند هوایی این کشور با موفقیت دو پهپاد پرتاب شده از «ایران» را منهدم کردند.
این وزارتخانه تاکید کرده است که از زمان ««شروع حملات آشکار ایران، پدافند هوایی امارات متحده عربی در مجموع ۵۵۱ موشک بالستیک، ۲۹ موشک کروز و ۲۲۶۵ پهپاد را منهدم کرده است.»
وزارت دفاع امارات همچنین گزارش داده است که از زمان شروع حملات آشکار ایران، تعداد کل جانباختگان نظامی به ۳ نفر رسیده و تلفات غیرنظامی هم ۱۰ نفر از ملیت‌های پاکستانی، نپالی، بنگلادشی، فلسطینی، هندی و مصری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/75376" target="_blank">📅 17:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OurnBD1zgcTqIj5V4jPrTaeP7vrKTN4RbT6vmaqzEsx_cjrDPRiSS0h03Po_kcXoq7EMMwmqxOwEcZ3eaJUKrrmBBbsjhL6HrICwjzMAAxwX7MJP4WCRw4z5XTMXAb4QFRLhfNErA7AgO0YOdBcDhvCUB6N-aK4TISm9OA-yTLDmSC0EeeyOSSp-2t7tPmw26PhG2GgJ1ybwBBgRJSP7s69g7ufMK6cu40ZW1qlxyB4ZvgKEMwdDUjHl-0P9wM2ZaTQC34_Zo_O7FC_LDCzLijc_m8WcqKTxafYrns-ta0t1Rp4qLJgaXybmEgKWp77HZRNW_f3UMtPiN4R1FTCL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی گفته‌اند علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، با مجتبی خامنه‌ای دیدار کرده و گزارشی از آمادگی نیروهای مسلح، از جمله ارتش، سپاه، نیروی انتظامی، نهادهای امنیتی، مرزبانی، وزارت دفاع و بسیج ارائه داده است.
بر اساس این گزارش‌ها، عبداللهی گفته نیروهای مسلح از نظر روحیه رزمی، آمادگی دفاعی و هجومی، طرح‌های راهبردی و تجهیزات لازم برای مقابله با «دشمنان» در سطح بالایی از آمادگی قرار دارند.
این رسانه‌ها همچنین نوشتند مجتبی خامنه‌ای در این دیدار تدابیر تازه‌ای برای ادامه اقدامات و مقابله با دشمنان ابلاغ کرده است. با وجود انتشار متن این خبر، رسانه‌های جمهوری اسلامی تصویری از این دیدار منتشر نکردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75375" target="_blank">📅 17:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGo71Ow1-hKvU-_kIlm9nbLxgx-1EGeeF40iXTUQGvVvToAzciDiuWoHA618zVL_u5EPepoft6WsuY-ztTuvjFekBIzJynkgJgpEZcaLTmikFMWXMFVT_9c8_gwaYjmzOxjDUfpPsc4MnZjicgvSoQGvUJBZL0t8wLDSF12ckM9EotCUsbeO5Rff2P64YScphqTw4TGpJAr_h6wDmlMCzvvFUOsLb3EWFp-DjLzaBv3w8ODtb09Jprx4PskTHaeORnfnk_czoShHHyjh6MvOVrug89CWxTKFRLMjBiINazjcRGCRoDtSR5uQIHFpne2LyVQ-qceAnCMMFAXO4ym7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران درباره کشتی باری هدف ‌قرارگرفته شده در نزدیکی سواحل قطر، به نقل از منبعی که نامش را فاش نکرد، گزارش داد این کشتی با پرچم آمریکا تردد می‌کرده و متعلق به ایالات متحده بوده است.
سازمان «عملیات تجارت دریایی بریتانیا» (UKMTO) صبح یکشنبه گزارش داد که یک پرتابه به سمت یک کشتی باری  در ۲۳ مایل دریایی (۳۷ کیلومتری) شمال شرقی دوحه شلیک شده است.
بنا بر این گزارش یک آتش‌سوزی کوچک در این کشتی رخ داده که خاموش شده است و تلفات جانی نیز نداشته است.
این خبر در حالی اعلام شده است که مارکو روبیو، وزیر امور خارجه آمریکا روز شنبه با محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، در میامی دیدار و گفتگو کرد و شراکت دو کشور را برای بازدارندگی در برابر تهدیدات و تقویت ثبات در خاورمیانه حائز اهمیت خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75374" target="_blank">📅 17:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhpGz8GmvdXfr6gRM_dTFBOIS3Fi3z-9AtVdpBi1vrIh_2KJfFp9_mEn_YM6_ZF2ral_Tt27jYa3bkZlWyrRR99nNQTinHtTmYrYDuoXdKijaGWmrppg1h7VsM2AWjbSxSV92tjxVHPEMra5TLhSa2RBSIH276FgR_QRt8hS92KYxgMB9pVE771-4j5gL_-yYyQQsQj3JljnlzctKMHyu4png0pvxFr9n2wVGm-4yhucGNa0bfIfaYTgjrBPB87cuSVNQWpZvJI-Om4v2FGJHfJWQonz9qYguVA5nLmc-xQIbdD1UKv_rCsffTPKY5o7LtV3KKOqhvivNeWZ0kJciA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
خبرگزاری فارس می‌گوید «یک نفتکش حمل‌کننده گاز طبیعی مایع متعلق به قطر به نام الخریطیات» با «اجازه ایران» از تنگه هرمز عبور کرده است.
بنابر این گزارش، این نفتکش «روز گذشته در دهانهٔ تنگهٔ هرمز دیده شده بود و پس از آن سامانه موقعیت‌یاب خودکار خود را خاموش کرد.»
به گفته فارس، «این نفتکش که مقصدش پاکستان است، نخستین نفتکش غیرمرتبط با ایران است که از نیروی دریایی سپاه اجازه عبور از تنگه هرمز دریافت کرده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75373" target="_blank">📅 17:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1ysRtnnenOB1Ed8wUMT7ijVe-CNk-BMYYHbqg4Uf48zy3ba9eqqKK2FhxudLZy9QxbvG6_Wb8t58dOiHAdgRpvElIItz1JWhrEf3pChL0LtvL4fD2ew78_nIwG82vkOSd_bJHieCyAwcaeCwiYAK1BIAPOcSaLDQgqU97KxRLMgnoIvxkg4JafuEIyE2ZP9_p2yjk2-6Oloj6iuGoTD5DqDFvl3vmNPYz1JLrSBt2s4vxXI5HQd0WmciUx7zy8BY9vfFwH-tzHghK5B6-gX14BN50QGvCH8-tb_scye65LpIQ1MV65j1isF3Irmk4nA4q9RXcn3Gusk0eqDsAm5rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخل ایران روز یک‌شنبه به نقل از مدیرعامل شرکت پایانه‌های نفتی ایران هر گونه آلودگی نفتی ناشی از تأسیسات جزیره خارک را تکذیب کردند.
او گفت: «به محض انتشار این اخبار، گروه‌های متخصص اچ‌اس‌ئی و اداره شیمیایی و آزمایشگاه، همه منطقه را پایش کردند اما حتی کوچک‌ترین موردی یافت نشد.»
خبرگزاری رویترز گزارش داده بود که تصاویر ماهواره‌ای ثبت‌شده در روزهای ۱۶ تا ۱۸ اردیبهشت، لکه‌ای بزرگ را در آب‌های اطراف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، نشان می‌دهد که به گفته کارشناسان با «نشت نفت» سازگار است.
بر اساس این گزارش، لکه‌ای خاکستری و سفیدرنگ در غرب جزیره خارک دیده شده که به گفته یک پژوهشگر «رصدخانه منازعه و محیط زیست»، مساحتی حدود ۴۵ کیلومتر مربع را پوشش می‌دهد.
به گفته عباس اسدروز، «طبق اعلام مرکز بین‌المللی «میمک» به نمایندگی از سازمان بین‌المللی دریانوردی هیچ‌گونه نشتی در زیرساخت‌ها، مخازن ذخیره‌سازی، سیستم‌های اندازه‌گیری، اسکله‌ها، خطوط لوله این منطقه و کشتی‌های در حال بارگیری وجود ندارد.»
اسدروز توضیح نداده است که لکه موجود در تصاویر نشان‌دهنده چه چیزی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75372" target="_blank">📅 17:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7yp9-NL52N24gi31n_5w4lP5wCeAf1RaLxFH54MyNEm5qYIiQEp9AlwN8cj9vTKg0aqdhvPF3IgkbDHRsjj7XrYjmH9zruWNLraERzZCFBXKs8MNFxXTgWfZ1hs5rkFxsuZ1k5ddytHX0GuIGi2yvPJ2OeDkFYcrowrZPzfrxiBG6F3mEtYY_wR56gHQMnHDmvML1xWJBI87mD2UtmjNsUv5xnixwEf5ISR4lekb8DYbvPQMozYO8gPCR5Yr5yr10Jasj4Jn_Vh7yWWupvBVLgaWBbLP9aj-thfGt6aWdRT21LuBGEcgb3QKAmdvgcYG-GrhDBSLcHUUT07lC34PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «وال‌استریت ژورنال»، اسرائیل در اقدامی بی‌سابقه یک پایگاه نظامی مخفی در بیابان‌های عراق ایجاد کرده است تا از این طریق عملیات هوایی گسترده خود علیه ایران را پشتیبانی کند.
این پایگاه که پیش از آغاز درگیری‌ها و با آگاهی ایالات متحده احداث شده، میزبان نیروهای ویژه اسرائیل و یگان‌های امداد و نجات برای خلبانانی بود که ممکن بود در جریان حملات سرنگون شوند.
طبق گفته مقام‌های آگاه، استقرار این مرکز لجستیک در فاصله ۱۶۰۰ کیلومتری از اسرائیل، نقش کلیدی در مدیریت هزاران حمله هوایی تل‌آویو علیه اهداف نظامی رژیم جمهوری اسلامی در خاک ایران طی هفته‌های اخیر ایفا کرده است.
این گزارش فاش می‌کند که مخفیگاه مذکور در اوایل ماه مارس و پس از گزارش یک چوپان محلی درباره تحرکات مشکوک هلیکوپترها، تا آستانه لو رفتن پیش رفت. در پی این گزارش، ارتش عراق نیروهایی را برای بازرسی به منطقه اعزام کرد، اما نیروهای اسرائیلی با اجرای حملات هوایی سنگین علیه سربازان عراقی، مانع از دسترسی آن‌ها به این سایت سری شدند که در نتیجه آن یک سرباز عراقی کشته و دو نفر مجروح شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75371" target="_blank">📅 01:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QeqCN3xxD4c6ouJUXHGTUuG9w4F7Y9Do1wDr20bks_jvlTjFRjUyJEoKr2QGRKrC3HbjhTKXNK5AScmf3cQ2ebFvk9MgzJUYCTJtwzyhMiGlL3i6P5-JNWyFR-eOEQNnAjELAqdyecnYkgPejAkGJKHZIVe02wKF14BM0QSxQaMEnk_5YfoRK1OJyvCubOl8HFLWrwL1kkVVuqIRfHFTnBs-LdXknIrwx86K2iCGW5x7Fqrv7l8Q-c8rCpj3Nbe0ujizlo4ARoF1JGRc6-RnAKyqsvRuUxfHq1hORUpXLnW2oL-N92b38ZXdSiL7X7M56buVqdmuMdx-N4c2riPHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l28YnQD_Rz6Laqe9v_fmYbugSaOcBJufq0M83HqAvikcL-3WFfmnkfaLizfVEgMJNKG-LKV-bENfRmqBZWb7z-GG143pruXrewhSfM2IkrieE-NHA64PN7FN88yrcYOxXPXZpKRTaCrfTCyB_p5a9_tg8eskkC5YPMqyJW-_YFUmp86Y4l3ZKJZUhjGNmEPh97PoNMRvNPDkFAFpqRs8fMRTmtiIx9a74OGtF-_MbRtc3y-FXveWKU8NtxTvpTd2HMbkCVLQVUtw2t74P9lmAmJr2RRCK_hofR9_P8TjU-Mhb2-YHjhheuBE-rXqX1x1-v9OU6duLv8oxX30ncJVdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر ساختگی دیگری که ترامپ در صفحه‌اش منتشر کرده
:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75369" target="_blank">📅 01:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QwNCAjZyx_0bhuAW6Vv3HmGEQDzckxXiYSE5LrXTZyA7mX3kKrwf-Uui_igRJdLIyisZU6Dg5kzxDuHepKcrErkUfxmBOKdRH6Qbn1NinCE7hZKjNbzyISMkRVo_Et_Vcg3DyMWauUXtsTELXsnrhZww7Hb6PK0oNR3piVe34uHBJ8T8iLhWuJBYOT5TycrY-VfOUhSrg6UDJkA98Tv0ufiRGFZ531luZwYXcqH78EaaBpjrPEnYzOsB-gEsvr8RyRGzfZ8hzTF0G-Oo8IURkh85I2IhFQjvSjaCEOY13IJ5K6Vlw3V2vLdPjEeEhGuaGlcXXsi9L3_q_CEjS0l3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75368" target="_blank">📅 23:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gtu8xcUqaDgYfzdZLZuIXjc0491Hymc5DvGAS6Hk2c9zx0FECaMSY32FsgCfFlsneR7i3uiQk7qg8tLzmyK-Gd6Z8wmIxEjgtm4o7iSQm_KjP5hdqe9_dBOyeRCuCAjVzJrkmnn5cHQjW5nSRrk41nO8i2yq3GPDxYogiqwGej1dSN4rB6WvstgKe9-6F3ZwVHADkeER2VIr9YhnVTEqFA_83tN_pfZTI5k0k7TlKeqWoKwguO_OAAQ0BCrEksViHVecFIQg1cgQs4tG-f4kjFd834wvvsbUw4LG2Lnf-RdPJnBV5fCZqjFSbVoq-bzjxEhZP0s0zRQtNHkvWlb76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، با اشاره به کابل‌های فیبر نوری عبوری از تنگه هرمز و تهدید به اختلال در اقتصاد دیجیتال جهان در صورت آسیب به این کابل‌ها، خواهان اخذ هزینه از شرکت‌های خارجی و الزام غول‌های فناوری نظیر متا، آمازون و مایکروسافت به فعالیت تحت قوانین جمهوری اسلامی شد.
تسنیم نوشت: «کابل‌های تار نوری زیردریایی عبوری از تنگه هرمز روزانه حامل بیش از ۱۰ تریلیون دلار آمریکا تراکنش مالی (شامل پیام‌های سوئیفت، معاملات بورس و تبادلات ارزی) هستند.»
رسانه وابسته به سپاه در ادامه خواستار «اخذ هزینه مجوز اولیه و تمدید سالانه از شرکت‌های خارجی، الزام غول‌های فناوری (متا، آمازون، مایکروسافت) به فعالیت تحت قوانین جمهوری اسلامی و انحصار تعمیر و نگهداری کابل‌ها از سوی شرکت‌های ایرانی شد.»
فارس، دیگر وابسته به سپاه، نیز در گزارشی نوشت که ده‌ها کابل فیبر نوری زیردریایی که آسیا، اروپا و خاورمیانه را به هم متصل می‌کنند، از گذرگاه تنگه هرمز عبور می‌کنند و تهدید کرد که «هرگونه آسیب به این کابل‌ها می‌تواند اختلالات گسترده‌ای در اینترنت و اقتصاد دیجیتال کشورهای مختلف ایجاد کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75367" target="_blank">📅 23:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4cX2tcu6SIqWefVPmQMrsT4VlXd9Q-HepclmFTrZFDjkJOY-QWujBAjdsL2J1fh_VWLOrlxpAthzaPmbcXiCPJkIfgZo-s9oCg6-no3SFwd-FUB3xtCdsoEHESxF4d-H8MsH8ZVYdqPNtHeFdL9WJWyGfZAyp7nO1vfU9JNP-y773S1p4olGMgWqA1W5iZ2mfMbaULuhu6CueUOWGFOHYJ_zNC_IQTPjlP-mTlugJ9NHQdKL7A6aeZL71Hzf321GjvxQIcB_s-NwVC35QXiECYUwYy2lGJC3MORMLdSdoJ8sklT3KU7ntYfj-Lq3zchajSM_StOQRZzRLHh0js3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، روز شنبه ۱۹ اردیبهشت، ساعتی بعد از برپایی رژهٔ «روز پیروزی» در مسکو، گفت که معتقد است جنگ اوکراین در حال اتمام است.
او بدون اشاره به جزئیات بیشتر دربارهٔ این جنگ به خبرنگاران گفت: «فکر می‌کنم این موضوع در حال پایان یافتن است.»
روزنامه فایننشال تایمز روز پنجشنبه گزارش داده بود که رهبران اتحادیه اروپا در حال آماده‌سازی برای مذاکرات احتمالی هستند. وقتی از پوتین پرسیده شد آیا حاضر است با اروپایی‌ها وارد گفت‌وگو شود، او گفت که گزینه ترجیحی‌اش گرهارد شرودر، صدراعظم پیشین آلمان، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75366" target="_blank">📅 23:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=qs1sP-vfCoTWgBk0n77nkfLm9FGdPRLPvP6vQvL9Uu9BUwrNlPzo-nPYaHj-jBpvoNPEEWlb1Ie2GvLmnCGtgie4Ko7BygYCLcNavTya9qGsdtHguus7lBAsyQDIc4jzVN_vUkSODzOhg0aNdGPzx_hGwM88IUXctad3HKnHBzdr_ESgdg0fVxMhtp22YpIlR82B8RA2nO3zCbWa4rajRagJVorD-MqN0eAveay34ddx5rEoEiXVezyOzZti5cMj_JP-01IharzGZZ29rI4wLcu2a5EHI_5k8T7oT0uPajqRJTSoYnkkAgdarCi2_uFrdWqRvGgAIalbjXwLFyVvgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=qs1sP-vfCoTWgBk0n77nkfLm9FGdPRLPvP6vQvL9Uu9BUwrNlPzo-nPYaHj-jBpvoNPEEWlb1Ie2GvLmnCGtgie4Ko7BygYCLcNavTya9qGsdtHguus7lBAsyQDIc4jzVN_vUkSODzOhg0aNdGPzx_hGwM88IUXctad3HKnHBzdr_ESgdg0fVxMhtp22YpIlR82B8RA2nO3zCbWa4rajRagJVorD-MqN0eAveay34ddx5rEoEiXVezyOzZti5cMj_JP-01IharzGZZ29rI4wLcu2a5EHI_5k8T7oT0uPajqRJTSoYnkkAgdarCi2_uFrdWqRvGgAIalbjXwLFyVvgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از تجمعات شبانه طرفداران جمهوری اسلامی منتشر شده که در آن فرد خواننده می‌گوید زنان «کم حجابی» که در تجمع طرفداری از حکومت شرکت می‌کنند «نور چشم» آن‌ها هستند و ظاهر افراد ملاک نیست.
نظام جمهوری اسلامی پیش از این زنان بدون حجاب اجباری را بازداشت کرده و طی لایحه‌ای به نام «حجاب و عفاف» قصد ابلاغ جریمه‌های و محرومیت‌های سنگین علیه آنان را داشت.
با این حال، در هفته‌های گذشته حکومت سعی کرده با انتشار ویدیوها و مصاحبه‌هایی از تعدادی زن بی‌حجاب در تجمعات حکومتی، پایگاه اجتماعی خود را گسترده نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75365" target="_blank">📅 21:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMqyAjSxyV-brUwvzyzgF38AV46k9EuIuVNmf3H-oswhe3nm9C4SQZGYRfKp5mMalgpX0b_TxklZR_rkmufZxwQOrvJxcjZTlT4yWJg8lhXyE8WTVUoAYeNvclR2NfmNwXoCHBA3axISeclx7dgdFnwUJEIVG1FsAxvoEj2d4uY1OBbe87XCxLBmtYlgMYPk2U6Tydelbh3Y8GV18TCjXqTasepq5fClWxonptieJSHnRlaLJKa4oAo_FViFn27npFa3dkbvx0S2XQzka5RGc0yvHeEo6_qMTBEyR7EFhEig1RiKdvsEVETcU5km3-9z-qMrlSexYkI733chi5JIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های لبنانی روز شنبه اعلام کردند که در حملات هوایی اسرائیل به جنوب لبنان، هشت نفر کشته شده‌اند. همچنین بزرگراهی در جنوب بیروت هدف حمله هوایی قرار گرفت.
این حملات تازه با وجود آتش‌بس سه‌هفته‌ای میان اسرائیل و حزب‌الله، گروه مورد حمایت [جمهوری اسلامی در] ایران، انجام شد؛ آتش‌بسی که تأثیر چندانی در توقف تبادل روزانه آتش، عمدتاً در جنوب لبنان، نداشته است.
حزب‌الله روز شنبه اعلام کرد که در واکنش به ادامه حملات، نیروهای اسرائیلی در شمال این کشور را با پهپاد هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75364" target="_blank">📅 20:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXzZfOoOlgV50syJx4pDl3LZv18naXlnwulNQnOQyYTeazz7TZIwS8xp5yspo6NqnXy88Hs88axJxd0hanM0aFKcedTfvEy6W8XsoXePVW45NBbIhtXUh25bsSeJoESCTNKNxUUw1POyX3MbXGjdHOaFcy1pKDpRzlPYhLgy0VMfx3K77R5krgHA-Lp8y2Vv5pVQRX1eKU10tQsZwS9DsVksFtlSsaD7NyHar2BAx6vEwtJFHzEpEK49w8LCZo9yx9egukMvSm3FCwKjuM3HCOgLvppACh9shtiw_fnlN_thNv0ZUO8_1SZk-4c4R2itegxwtECgw7N9tBFY2eG72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی آمریکا، سنتکام، روز ۱۹ اردیبهشت ۱۴۰۵ اعلام کرد محاصره دریایی آمریکا علیه جمهوری اسلامی همچنان به‌طور کامل اجرا می‌شود و نیروهای این فرماندهی تاکنون ۵۸ کشتی تجاری را تغییر مسیر داده و چهار شناور را از کار انداخته‌اند تا از ورود یا خروج آن‌ها به بنادر ایران جلوگیری شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75363" target="_blank">📅 19:40 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lGQQ8ToTkjfaQFvSW-c7HsnTXknHp1IHrc4vzhceb9w-KrusiGUoiN6dINr-USH3vQL8ZeirBiBpEkyfLI-RcqtwQ12h03W4ioAKli5N41e2Tb7znG2dSVJl66FPj-vZG06HZyRekRf-NDMqiec1UP3Y8OZNrudrXRB4g8RMQkO-Yz_uOTlhEQgmXugINI7_AzwmNh0R14JrcDqdSB_g6QEc6QPzQmlV9YFLar7HFbNXn5ajyfX52SE5a5_7Ki6c8piK_IroCPQqU4S9wQhPHfuplN_yXHN17CEx_QzufiM-OJdd24SprPuYxQxodEZ42lkxcDnbg4Lw7P_iTMqvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bHnkiN0vPUFisLQd6c5qI4NIRDi1TWvGIPV5WADkBUvgOZszzNoM0Mhhy5NE5vbt_aIWmyZurMpszE4Ad1ywamMd0d1LkQ4-Ipvs9kh_5u-J3sJ5JUJxu1c0ZO8FKa0AKANpgSA6B2AgmcsoCAepUMeUTmfZQFNtAg6iWRHrLLL5ShFFPGj2EXNxDd-y_PQGVsdnZYuzlsrpIO5s_rvQ5r0_o0jNzPyPsK1KC_lmNQ0zmYw2-OnnLndN4_oH-nj-FE7AfgPf1XIZvPjFfIoaj-hHdKNiFAV47rDBe9KdIgjVhUKYp0Z2tcatHD-wjHScoWkBDXRPXkp3ilRSaOHHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gtF3txkiipcjEQWzx9b619LH0wA7-8WLYLF1nQ9VFKDOE8uMyQ18yKNydNkS1mpVpzKLLsEwqygnqK-3j8NYkfDD2T_8C_rkuvpl_n9jkiM2brQqcAgDKSzsYE8T_TYb8kiPbb6Q12dJGZE4aLvs9kuAFcW54NA3vXFsa1FMk9-00kYl_1dxKZ9D75PMPfBBwwVMFt7-DV9TxPws33CwvQGjFG0tO4a3r21pWRmDP2SdbzcLuQLV4quTJAcP2S8vqj-OEFtyIj9XH7H8dRr7eFLDrgpmRQJ6ImGYc8tfxim8Z4lQaJ9ci4kWfTyYKhYzGRhAAo_DC4SJ69-VXxaPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FHOwaDp3daShtQMTkUI-tSY8jD1u3NAyVVILES6IpqM0sz_VHUcu0YA-BNJiJ3ZzXJeFvzZcIcbK5mfpj7tGAx3JqbUlp2tm_EmbSuY8hQ7STXm8QJ4Qtvax45AbmQWbWoxvvO6j-VnhN0pWI9tvKaOBvn0Hr6OE3Bi_pytMIt9S5xnJPT7ptjsI9H5NtcvuUUVG3z6fzxVEAA6LrY5KMzWoHSVDGLaS4hGWRs6L7ezO273_PRMbcbWoVJQmCHD2cFYfwoDxuhUoNHfptKHrPvQItOZTqrugsxQRB-hqUpitxqp41p7dMNJwGKztsOqjuXxaRwVIwuH1tNTkZy-uoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rQzF1XAeRsENBSeqjLOLPt90GVkdmYbeh4VvDvJm2noAvifyjNqUaxFApFzRqV6VrQFyjpUqtDJ2XN8nn2szztYD0c3tRZh8sbYgvQfuWA95X3PTon9qmVxlL3PI0eMOnaOPECbmgfttPL_CGaClyi9k_qcoyLQxV7mhzMuuziC_Da81caSv8ZLS563lF8fOBGThTXU16TUxvHOr7Rp8EaxDB7T_jOuZHsN656FwQFLpD8t-xW80nGoiSCSwl7r8pR8RoaL5ay1BJhBvqj4fizVqbB6-NPavj90MTIaJUPawKKbyZhR33YSgaY6qfBFmaC6kbHgBE7_2nPkl35FAXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذشت
‌ عبدالله امیدوار، یکی از دو برادر امیدوار که اولین نزدیک به ۷۰ سال پیش با موتورسیکلت دور جهان را گشتند، در سانتياگو، پايتخت شيلی درگذشت.
عبدالله،  برادر کوچکتر پس از پایان سفرشان به شيلی رفت و در آنجا ازدواج کرد و شرکت فیلم‌سازی در شيلی تاسيس کرد.
عبدالله۲۱ ساله و عیسی ۲۳ ساله،  در سال ۱۹۵۴</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75358" target="_blank">📅 18:51 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgb3_C8q4rOQ-TSEJISpdQ1r1xR00XXpWT9n6kibwxYw7Ug4s4vZGOgWSa_fTVB54AmwQZn_G2HAWX4eoTrL0TVNdyH989cMDDa2Qaqh47TbepOzH7_9t9bfuWMtTlT8T0pC6dWogzsw2e12NaoiBbzOeA431F0NcxGeuNkQ413AgHVpDBC_5IYaVncdDgt0oA4OObHYMgRKI5LOk3tT2jxnhw7XNIf4-3QuNasp7QiZzu2WwCmKqKZDFZ0lU1L4UmOaoW-hY28lk_74DHPEE1wk5soRv2NoOuMMJhm86YZVGmErlYAJyHd9i224VCI2TF22od0zAeVeMod-4A8G1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع بریتانیا روز شنبه اعلام کرد که پیش از هرگونه مأموریت بین‌المللی برای کمک به حفاظت از کشتیرانی در تنگه هرمز، یک ناوشکن به خاورمیانه اعزام خواهد کرد.
سخنگوی این وزارتخانه به خبرگزاری فرانسه گفت: «استقرار پیشاپیش ناوشکن «اچ‌ام‌اس دراگون» بخشی از برنامه‌ریزی محتاطانه‌ای است که تضمین می‌کند بریتانیا به‌عنوان بخشی از یک ائتلاف چندملیتی به رهبری مشترک بریتانیا و فرانسه، در زمان مناسب آماده تأمین امنیت تنگه باشد.»
لندن و پاریس چند هفته پیش اعلام کردند که طرح‌های نظامی برای تأمین امنیت تنگه هرمز در حال شکل‌گیری است و در بازگرداندن جریان تجارت از طریق این گذرگاه حیاتی موفق خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75357" target="_blank">📅 18:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qjy4N4nIEguJq7BcKWyN3qjA7wxyQXbjMIj7rWzEHMiTAxe8O6bj-M7rwe8HbU-ipSW4Oa8VR1jxM-YHNjCV-vf3EyhilKsspBjuAYnZIgYsuVUDuKovkSotEfZw2w8cGMdcsgK2jabbeYBoEfsk6jFMKDBV6V7becpRCeH1qr5vZ_I2IJMa3P05mFH0tH6_KvGvwV4Y6wbALNerMWa8hDN0PaJTiiOXvAcokQDHk0G1DvTuLwY2ZHFLUj_fpTmdPquBCIeuEeue7-Hd2RutP5PetO9kpjLhP4mdqcbllkgTJCdGzrxSFWZvDcEg4gJvaii2_qtgVzUMaKm-RAbi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U6U1UlUBflJs4AXfSjno4mhTqEiwF01oxENEQ_YVrCbHKiEjgaDivKbdbgPVb0hio-sfPv_I8R26uitpgT6I8gZbxwRPkKlARVdOgN7IF2_S4S4hmid7KHkZnRHhmqPUh3UBiPVOnWZWIKCGVou8iCusAvLRWEqH9mwvKnimp_1h9qgd1AQihJwWaCsBWZpSGR8xhc8yL2IpPsSzWIj4uTFJMuIlb4Ad67rL_fEi7ZOU8kxxLMxL0T-KYFEP6xJAxchFYeL-oBXKC2cvBh-wTBtab53aZlnXClWowiHA2qcdbxifD_Ibo1NkbA4npUjp6fWwB0eyOsB3BP0Wz9lxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V67I967qo85plJKCG6XzHuJzzZZ39DKYvjWri256qL61zZQUNTOrby-IFvftYDzUq955Iv-dzGyfQ9MdvhBvi-rMy5yI08dktdYc7zRcy9pnGdME3xJ-LEEFvSJ81gsisUT71N-ghwyXaGx1hGZoBZDiarn5sBTK5k4hOBQ6_8Sy-029LSkLNwQXL-l35os7PW3naZhfycA-DSkCUMTHBzyBO9SDZqD2wAaMko5Ln2oplCCbLOlHk-z1IOBRlx23y8UwR3CW111hahugfA5rSlF7g7BDAZlxW_eyfgsYXMeLhpel2OCJNUjMJk49F9vr9t_yV95-Q9tOBdAuQNqcgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت کشور بحرین روز شنبه ۱۹ اردیبهشت اعلام کرد که ۴۱ نفر را که به گفته این وزارتخانه با سپاه پاسداران ایران مرتبط بوده‌اند، دستگیر کرده است.
خبرگزاری دولتی بحرین به نقل از این وزارتخانه گزارش داد که مقامات امنیتی گروهی مرتبط با سپاه پاسداران ایران را شناسایی کرده است و افزود که تحقیقات برای شناسایی و برخورد با هر فردی که در این تشکیلات فعالیت داشته ادامه دارد.
@
VahidHeadline
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی، روز شنبه ۱۹ اردیبهشت، با انتشار پیامی در شبکه اجتماعی ایکس کشورهای منطقه از جمله بحرین را تهدید کرد که در صورت همراهی با قطعنامه پیشنهادی آمریکا در شورای امنیت سازمان ملل، با «پیامدهای جدی» مواجه خواهد شد.
عزیزی بحرین را «کشور ذره‌بینی» خواند و نوشت: «به دولت‌هایی همچون کشور ذره‌بینی بحرین که در حال همراهی با قطعنامه آمریکایی هستند، درباره پیامدهای جدی این اقدام هشدار می‌دهیم. درهای تنگه هرمز را برای همیشه به روی خود نبندید!»
قطعنامه مذکور که با حمایت آمریکا و کشورهای حوزه خلیج فارس به شورای امنیت سازمان ملل ارائه شده، از ایران می‌خواهد که ضمن توقف حملات علیه شناورهایی که قصد عبور از تنگه هرمز را دارند، محل دقیق مین‌های کارگذاری شده را اعلام کند و از دریافت هرگونه عوارض عبور از شناورهای عبوری خودداری کند.
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای حمایت کامل ریاض را از اقداماتی اعلام کرد که پادشاهی بحرین برای مقابله با آنچه «اقدام‌های صادرشده از سوی ایران» خوانده، اتخاذ کرده است.
در این بیانیه آمده است این اقدام‌ها به گفته مقام‌های سعودی، امنیت ملی بحرین را تحت تاثیر قرار می‌دهد و با هدف بی‌ثبات کردن امنیت و ثبات این کشور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75354" target="_blank">📅 18:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCSsCCglv9ZvCXmkwcSGRNfs8HdaEQ-XFLRzmV9ukvEECKUxtG0TipyGl2FH24A8jFtwgrz1ZMbK41J8_0TeAJxM1oveHbJ_p9Ke1MAVJF13yJVUnVtbsNumGNyYgOYZEbXO0WnqMzaOXdaL03-IOW9fEP4TzLbOxuwjWLikYwaLcnpd8AUHz3T1G0bLmoTH0UmhZP8lbYlr7o689TkO-9nXT0-0A7BsNLAjfeNpgba04fzHb5QIT2K_W-xe6b21EUfA3olwgoJrB4ujR-aiFcP1MwUHlHICj2rUC8Q81Msr8F_RA9O4jApdB4ahXi2-mm3QuLbl66rTjSxbb3FTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/75353" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tranBYD91vxlAK3FdxzzXmIOst23zY4NLsFWdzc6uMIYFA_pH7-jnVOizK_Q5HJtpe3RQ5ZBM2ojSTZn1jxq6LHT4W41K3blEAeaWuna_X83gSXsnAhNTlQ2ttF5dqHzzOEGxLzqGE1xrEjLxPJV_fT44uWcbjQECMu8UZac5bv24STPit9MD-SL8p48nU9sx6Phl69wcwl9Pg9k9Mnw_iSpct5c1syzr04Z7P7awk1xPFA6Sa2jnVVx9_z3Pbm04TA771wGrwylbK8vgXcMklbULV_uyV4dypT5K-H3Brl2QPLZsmfvaQSVq1uSYuzaBaawL8ozV96hwLPLMiQTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HcYpnGr3w0TqR__NmOASoLULRSyfAwTf4nZFKKiJxAZAqTpTe0s-ib9IHxVhRuHqYBF3A4N0YFA0jrnJ_P15OI8KRcCaTtw75U3GJWhcwUMxN-MsVGUkZ6oqxz15qVhvRTLtyzVZsSaCIb2yJ587rYBgzGBW3Fa1cLn1ilf9DZDscwLLijYS8AmV-TyE5b0Or2H6cBZLPcD2FRO5DEdsUQrun4wGADzJRe7F_5DJ7G552sIcSXnxxUfScXxYoI5P3d7QULZY8rpwX1k_W8shvzNqEZDXfOv_6Oay-NBhx7JEXdYy8iyDOxHsar6TxPg6adMiiCVA1ZQ0Lp8-i3RpSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i6RPc7KQwodf5UkaxhBHA1FwCXdBZ_Mhlf8g4i6P_MBPcxvRA6ajn-P6mvXTpnO_wM-WrCPh4TVNPGuPGltEVcgfHnFOblkIxEpGaRjAqnUL5bUCn7_oIkdd2vRTnNXc0QfW4iSsl1BEyX6SjnovC4mCjTsbsp6E67rDf184dDtepdXdvDKMTngh9B7l6I_CXWsCHNWWPz7kvadM0c9cFLKyAVfnU0cT1kIGxAFo5s5nFtdsY5n4SHowFlcD5jX6kkf5KU13hMTVfXQwJF3VGfpe6pOGuFwkCKgFGi8bkb01a8Ng2vpWfawQjUJZivJHx-mmlSRtilQ42V6_QpWiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L9fMBBPt2nV0vjlxSZWXDtaY9SJFZqzjn7PNNMXVrBqc3IHHvv3ecHe0O1GTiUFGwLXrqgCdHELQ0IrtFCJbSa-XP_dNz8BFsIzdBkbWF6TYrrmbbS4WC8raaJc3aZo0TfXJ47wMjfGAnD0oXkc5YGWwyhlpeIay9Jb1yiQ-D_y6p7eHKF1dttlXuX9zFRPUYKAqjRWbl1H8SiHxkjJPPucihgvMf8yhJJZYyYKoHYoenhkG-G3mwDCer6aoD-1n1UqkfL1n3ziktzC3cdlfylh-Nr53jWn1cVBQG1VcZZM7m5Jp4zEuVetQjhGp4MeamZyC8KJahM_J2bl0I12HGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aYcywgVruZryGJ8hIRWQh3X5H3eKkxDt8xZM3SGifDuP9d4fCQL7Tp897kBCsPXli47fEEyB_5tTP9Jb1PqGyYhUBr0eFUqmgODYvMJ44W2XTFb_VPgy4CkNofoSPqFdQU1Ic94ufllPidEyKL7v6A1KxD3c-5PHDjvkU-lVuvQISomAuRsEVj5PRGaQ3dg2I_mwPm-I89nY9iYwdaZYN2ZG5T6gquumYIgFYaI6ay8FUZ-t2Xn64ubEYHC1r40lp1qZNRCHkxBB9ODrcswJCNAyOjIFDTiBTCEZzesiyDaRF9KkFK1zzVw88vFxGhBlFCuu-oPudUHcB7vlfyMbIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در آغاز یازدهمین هفته از قطعی سراسری اینترنت بین‌المللی در ایران، یک مقام دولتی هشدار داد که این اقدام حکومت در درازمدت خود به «تهدید امنیتی» برای جمهوری اسلامی بدل خواهد شد.
احسان چیت‌ساز، معاون وزیر ارتباطات در دولت مسعود پزشکیان، گفت: «قطع اینترنت فقط در بازه‌های زمانی کوتاه می‌تواند کمک کند و در بلندمدت تهدید امنیتی است.»
قطعی اینترنت در ایران روز شنبه، ۱۹ اردیبهشت، یازدهمین هفته خود را آغاز کرد، در حالی که مردم عادی در کشور تنها با صرف هزینه‌های گزاف می‌توانند به اینترنت بین‌المللی دسترسی داشته باشند و مقام‌های حکومتی و عده‌ای از حامیان جمهوری اسلامی با مانعی در دسترسی مواجه نیستند.
@
VahidHeadline
معاون وزیر ارتباطات ایران خسارت‌های ناشی از قطع اینترنت برای اقتصاد دیجیتال ایران، در پلتفرم‌های بزرگ را ۵۵ هزار میلیارد تومان اعلام کرد.
او گفته است: «مجموع عدم‌النفع (کاهش درآمد) این حوزه نزدیک به ۱۶/۳۲ هزار میلیارد تومان برآورد می‌شود.»
معاون وزیر ارتباطات ایران همچنین گفته است قطعی اینترنت در حوزه مخابرات و ارتباطات حدود ۶/۴ هزار میلیارد تومان کاهش درآمد مستقیم کسب‌وکارها را در بر داشته است.
آقای چیت‌ساز گفته است: «قطع اینترنت برای کسب‌وکار اقتصاد دیجیتال ممکن است برای چند ساعت قابل تحمل باشد، اما قطع گسترده و سراسری آن عملا یک شوک اقتصادی ایجاد می‌کند.»
یازده هفته از قطع سراسری اینترنت در ایران می‌گذرد.
افشین کلاهی، ازاعضای اتاق بازرگانی ایران، پیش از این گفته بود که خسارت مستقیم قطع اینترنت در ایران ۳۰ تا ۴۰ میلیون دلار در روز است و خسارت مستقیم و غیرمستقیم این محدودیت تا۸۰ میلیون دلار در روز می‌رسد.
@
VahidHeadline
خبرگزاری دولتی ایرنا در گزارشی میدانی از تهران، عملاً تأیید کرده است که قطع اینترنت بخشی از فروشگاه‌های مجازی را از فضای آنلاین بیرون رانده و به خیابان و پیاده‌رو کشانده است.
ایرنا نوشته پررنگ شدن دستفروشی فقط محدود به نقاط مرکزی تهران نیست و از بازار امامزاده حسن در جنوب غرب تهران تا شهرک اندیشه شهریار نیز دیده می‌شود.
به گزارش این خبرگزاری، مدارای شهرداری و «دستور آگاهانه» برای برخورد نکردن با دستفروشان، این روند را آشکارتر کرده و بخش‌هایی از شهر را به ویترین بساط‌گرانی تبدیل کرده است که به‌اجبار از اینستاگرام به خیابان کوچ کرده‌اند.
ایرنا نوشته فروشندگانی که تا چند ماه پیش با صفحه اینستاگرامی، پرداخت آنلاین و ارسال سفارش فعالیت می‌کردند، حالا در نبود اینترنت آزاد و پایدار، ناچار شده‌اند در خیابان بساط کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/75348" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GvB8xYz_kbp6CW6yR80KrlSFEXAkGrw6ta2YB85LtuvMu16L_1Cc4eDqJVDI-UZ4XnUTHiY-2iTIVMMOFSS6aCfFPejtl5ZHDMrf_gU-x9Okc3NoN-PUjX-mbyIBfc9m6lq3nYopokCFEqYw2KMpes3wCd3VhKV02rhBKcPTMHgio-p6pW5BJnxm9APN97m3q_xUAxtqQMI0mKcr3RN3SqcUXfBm_YUvCACtoEsXH3PD072OLmHGhpn--du44hHjaKWd9QNHkR5LD5SsW8gC7Dn-0ecwjMe1413_R_5YF3ioG579Nx6xtb-oEGgUY1HYD7GNnLkLOz3WURI4ZvJs4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pD0VaP4ZlqvVAUXBO47uyLLb991Cxz6PfDSYUHWerUndH7j9UtftJT5yUQl3kyjjhYDmbcPP1cJWen-Roi0ORCiXqwt7NCe1a-I8OMahgCJP5kE4TUoZESLpIidY4kQvuLceHyScFYQeA4cre5N1wyYKjrLNJedDYWv0C9pT8qaamZT0IdfZMEREMCA9F7yo_JPN4drs5twMMYKuoVSQnkBRZEpemGAm4VqKknJol5DPhmSkSkWUaVUhafYBnsf7qw-M4L5zDz6XxeX3WOb9trgnmkhHn-CLfEF4QnahXmTBxIsKyFufr8GDJ0-lWvLOC4uI-QNiAGKfliq4KGVgaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه‌ترین داده‌های مرکز آمار ایران نشان می‌دهد قیمت برخی کالاهای اساسی خوراکی در فروردین ۱۴۰۵ نسبت به مدت مشابه سال قبل جهش کم‌سابقه‌ای داشته است.
بنابر این گزارش، روغن جامد با تورم نقطه‌ای ۳۷۵ درصدی، بیشترین افزایش قیمت را در میان اقلام خوراکی ثبت کرده و قیمت آن از حدود ۸۱ هزار تومان در فروردین ۱۴۰۴ به بیش از ۳۸۵ هزار تومان رسیده است. روغن مایع نیز با افزایش ۳۰۸ درصدی، از حدود ۷۴ هزار تومان به بیش از ۳۰۰ هزار تومان رسیده است.
برنج خارجی درجه یک با رشد ۲۰۹ درصدی، مرغ ماشینی با ۱۹۱ درصد، سس مایونز با ۱۹۰ درصد و تخم‌مرغ با ۱۷۰ درصد افزایش قیمت، از دیگر اقلام پرتورم بوده‌اند.
این جهش قیمت‌ها در حالی رخ داده که فعالان کارگری سبد معیشت خانوار کارگری را بیش از ۷۱ میلیون تومان برآورد کرده‌اند، اما حداقل مزد پایه ماهانه کارگران در سال ۱۴۰۵ حدود ۱۶ میلیون و ۶۰۰ هزار تومان است؛ شکافی که نشان می‌دهد حتی درآمد رسمی کارگران فاصله‌ای چندبرابری با هزینه حداقلی زندگی دارد.
@
VahidHeadline
خبرآنلاین در گزارشی نوشته اثر افزایش ۶۰ درصدی حداقل مزد سال ۱۴۰۵ تنها در ۴۵ روز از بین رفته و قدرت خرید کارگران دوباره به سطح پیش از افزایش مزد بازگشته است.
بر اساس این گزارش، حداقل مزد پایه ماهانه امسال ۱۶ میلیون و ۶۲۵ هزار تومان تعیین شد؛ رقمی که در روز تصویب، با دلار ۱۴۳ هزار و ۷۰۰ تومانی حدود ۱۱۶ دلار ارزش داشت. اما با رسیدن دلار به حدود ۱۹۰ هزار تومان در نیمه اردیبهشت، ارزش دلاری مزد به حدود ۸۷.۵ دلار سقوط کرده است.
خبرآنلاین نوشته قدرت خرید مزد بر اساس طلا هم افت کرده؛ حداقل حقوق که در اسفند معادل حدود یک گرم طلای ۱۸ عیار بود، حالا به ۰.۸۱ گرم رسیده است.
این یعنی افزایش اسمی دستمزد، زیر فشار سقوط ریال، تورم و سیاست‌های اقتصادی جمهوری اسلامی عملاً خنثی شده و کارگران دوباره با شکافی عمیق میان درآمد و هزینه زندگی روبه‌رو شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75346" target="_blank">📅 18:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4r7UV-DQciT1IJN_PcPpw8rNky-lwSDEPWiSsWlSnXUYSpbikMN563Fa-A0YFs0jnQrfBwNvqDl6u0WYWop8g0xyHOWOYZF4FzYEd7DI7JXp2718oV58BmbmLCUT2wilPvItEK2EPo7vET_vFQuKL98ZgiG5AztOjwy7ry1HZ1J28hdBnTYSxzBOgMvnlP3okQ676yijbOzwG4kxh3SW4RRScmvSdo2HeNaH-wFULE96xqcYoB4NP9cv16xkg46hxghniCTBx8dgdWbBGVtCGrd9jOb5WeWj5FdUghakUgeTm77bM8wy5B2DZCE9MIlWHzxOHtKrJK_6ShNCaEXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جمعه،‌ ۱۸ اردیبهشت، یک خبرنگار در کاخ سفید از دونالد ترامپ درباره نتیجه تحقیقات دولت آمریکا درباره حمله به مدرسه میناب پرسید.
او در پاسخ گفت که این مسئله هم‌چنان در حال بررسی است و نتیجه تحقیقات «به محض آماده شدن» در اختیار خبرنگاران و رسانه‌ها قرار خواهد گرفت.
در جریان حمله به مدرسه‌ای دخترانه و پسرانه در شهر میناب در جنوب کشور که در روز آغازین جنگ مشترک آمریکا و اسرائیل با ایران رخ داد دست‌کم ۱۲۰ دانش‌آموز و ۲۶ معلم کشته شدند.
چند روز پس از حمله، تحقیقات رسانه‌ها نشان داد که این مدرسه که در نزدیکی یک پایگاه دریایی سپاه قرار داشت با موشک‌های آمریکایی هدف قرار گرفته است.
از آن زمان تاکنون هفته‌هاست که پنتاگون اعلام کرده است در حال تحقیق درباره چگونگی رخ دادن این حمله است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75345" target="_blank">📅 18:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiGfrwwT0Da3W0Yl52W7Y-cxSFRQ0NqWXVH5osAHcM1PTzH9pC1E6r10mcKuNK8z2NAJQttEsRAy2KBuKl5JkQ9lNSKV3MO5Eq4JfV-hnGg6XLKn3c6e_Rqv4iW3R9cU7b6q4DRdZnG6D4oDYBho87GqItrKKfr6CimNqmBEYVlVeSWlqD_Q8BF5DUNtrad5ew7wBb25MALKk460HeshIoemz5NdzW3SLuy_-0cdC1-hcK2oy6IJR_dXwgxQSqP2xbuQM45pOuuP6AoeAPCauGtxC-HzYMUZCRj5SpMVNaPIrTpDwEBbHcGzg2np51_WagsTYSaUaebGM1-jfcMeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به خبرنگاران درباره چشم‌انداز توافق با جمهوری اسلامی گفت: «اگر همه‌چیز امضا و نهایی نشود، مسیر متفاوتی را در پیش خواهیم گرفت. اگر اتفاقی نیافتد، ممکن است به پروژه آزادی تنگه هرمز بازگردیم، اما آن پروژه آزادی پلاس خواهد بود؛ یعنی پروژه آزادی به‌اضافه موارد دیگر.»
او در پاسخ به پرسش یک خبرنگار مبنی بر اینکه آیا جمهوری اسلامی عمدا روند مذاکرات را به کندی پیش می‌برد، گفت: «به‌زودی خواهیم فهمید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75344" target="_blank">📅 03:02 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kfc291hi_SfDcTdl957f3YOM9PH5y16ONxls6r2exx2ZvivLk6D0H3VtoTesX8CN4fcR3i1vCJGudQNj7NB0sBelChrZ8Ul2CjpmlivWJaQRhyKJdfRv8v9GMiVi5sPANxB6Lu2t1IkmsYNER2gXHXNleDYbv1JfBX2nyCboYev5b_JA6K7kjzaqHuYwbRqpP2QmS07GISAlcFmDyg-bcj9U12IjejX43rQhq2nCN8oZumQUgBf3LXlgJdKE67l5jhdYPabMpj1VA3caKbYZc1mjmK8RaBn_oNVQ1ybLFzqknkhfsJ8BKUXEL4FlYZUlTyzyc2jYMoUqpgdGQJPDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داده که لکه‌ای نفتی ظاهرا از بخش غربی جزیره خارک، پایانه اصلی صادرات نفت خام ایران در خلیج فارس، در حال نشت است.
آمی دنیل، مدیرعامل شرکت اطلاعات دریایی «ویندوارد ای‌آی»، به ای‌پی گفت که از روز سه‌شنبه، معادل حدود ۸۰ هزار بشکه نفت از جزیره خارک نشت کرده است.
@
VahidOOnLine
شبکه خبری فاکس‌نیوز به نقل از کارشناسان می‌گوید این موضوع ممکن است نشانه‌ای از فروپاشی زیرساخت‌های نفتی جمهوری اسلامی باشد که زیر فشار فزاینده ایالات متحده قرار دارد.
به گفته تحلیلگرانی که خبرگزاری رویترز از آن‌ها نقل قول کرده است، این لکه که در تصاویر ماهواره‌ای کوپرنیکوس سنتینل بین چهارشنبه و جمعه دیده می‌شود، منطقه‌ای به وسعت تقریباً ۴۵ کیلومتر مربع از غرب جزیره خارک را پوشانده است.
مقامات آمریکایی بارها گفته‌اند که با محاصره دریایی جمهوری اسلامی، ذخایر نفت در ایران به زودی پر خواهد شد و رژیم ناچار می‌شود که تولید خود را کاهش دهد، امری که می‌تواند آسیب دائمی به میزان برداشت از چاه‌های نفت وارد کند.
حالا، نشت مشکوک نفت در دریا این نظریه را به وجود آورده است که جمهوری اسلامی نفت خود را به دریا می‌ریزد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75342" target="_blank">📅 01:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkWhXIrlpaxbKvwPqTkMwZo2XpUE0Jci9BzpcExVbMRK99J6OxqzVHBu5tauIwUMP4Qyuxv9PaU2N-6Bv7TYFM2rePqwzTBFIOJpkeuZnIE-ksjkPdy8aohWKQrMf43POSg6EoygAPidZCv94yRsTeV2-dfNRMTFIKG5VTVF42OAJjH2fm7NjYuvfEesqVy6Fgm9pZpA7e6f3HuQWileLbSQb5kwTuexH5A4y8QvvWe-MGWnxQP3xAZEg8LV2Ul1CNkKJ0mjJKlNgec_35jyscnSjfujABka9Y1DsWqsVMslKpoYgorVbe7ikuMMNz9xENKBCs2b2BlI-Ice5qH6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «واشنگتن‌پست»، معدن‌کاران در میانمار موفق به کشف یک یاقوت سرخ بسیار کمیاب و غول‌پیکر شده‌اند که از نظر وزن، دومین یاقوت بزرگی است که تاکنون در این کشور کشف شده است. این سنگ قیمتی ۱۱ هزار قیراطی (معادل ۲.۲ کیلوگرم) در نزدیکی شهر «موگوک» پیدا شده؛ منطقه‌ای که به دلیل استخراج یاقوت‌های سرخ تیره و باکیفیت که در جهان به «خون کفتری» (Pigeon Blood) شهرت دارند، شناخته می‌شود. اگرچه وزن این سنگ حدود نیمی از رکورد کشف‌شده در سال ۱۹۹۶ است، اما کارشناسان معتقدند به دلیل رنگ سرخ ارغوانی منحصربه‌فرد، شفافیت بالا و کیفیت بازتاب نور، ارزش مادی بسیار بیشتری نسبت به نمونه‌های قبلی دارد.
میانمار تامین‌کننده حدود ۹۰ درصد یاقوت‌های جهان است، اما تجارت این سنگ‌ها همواره با مناقشات سیاسی و حقوق بشری گره خورده است. سنگ‌های قیمتی یکی از منابع اصلی درآمد برای دولت نظامی میانمار و همچنین گروه‌های مسلح قومی به شمار می‌روند که برای خودمختاری می‌جنگند. در همین راستا، سازمان‌های حقوق بشری مانند «گلوبال ویتنس» از جواهرسازان بین‌المللی خواسته‌اند تا خرید سنگ از میانمار را متوقف کنند، چرا که سود حاصل از این صنعت سوخت لازم برای ادامه جنگ‌های داخلی و تقویت قدرت نظامیان را تأمین می‌کند. با وجود تغییرات سیاسی ظاهری در میانمار، ارتش همچنان کنترل بخش‌های کلیدی این معادن را در دست دارد و کشف این یاقوت عظیم در میانه بحران‌های امنیتی، بار دیگر توجه جهانی را به ثروت‌های پنهان در مناطق درگیر جنگ جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75341" target="_blank">📅 01:18 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b37b7b7858.mp4?token=k9TTFJDqxhSLdE_o-Pxq7HGLwgCRywuSgmGGuEHd_JIPAW1dgoxFfjryvxfGAQeOo0UNpdZm4sBv7woFI8bAOHY1SjL8DgV2iVPWULdu5_yxJrun3Z4gA7eztYAjOksgWul5CT66emNb1hoW_I6Y3EyPuAKo30bWUckzAx3O3ojOHKgMS-4j1EY0nI1ZasZXgz3sFWfFlbksmgkYxD0LzzqdbZBwzZQX8MdCv0LGOAOhzSg39eKAGb4x6drsFmuFTSHjimPoZriSoMNIfi5A8zUuELMoQl7_m57OW9sd-aVlIpjr6l0OK4WALMHVBesiH-Ut-aPAwkgHGGQzIt0d1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b37b7b7858.mp4?token=k9TTFJDqxhSLdE_o-Pxq7HGLwgCRywuSgmGGuEHd_JIPAW1dgoxFfjryvxfGAQeOo0UNpdZm4sBv7woFI8bAOHY1SjL8DgV2iVPWULdu5_yxJrun3Z4gA7eztYAjOksgWul5CT66emNb1hoW_I6Y3EyPuAKo30bWUckzAx3O3ojOHKgMS-4j1EY0nI1ZasZXgz3sFWfFlbksmgkYxD0LzzqdbZBwzZQX8MdCv0LGOAOhzSg39eKAGb4x6drsFmuFTSHjimPoZriSoMNIfi5A8zUuELMoQl7_m57OW9sd-aVlIpjr6l0OK4WALMHVBesiH-Ut-aPAwkgHGGQzIt0d1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی، مسئول دیدارهای دفتر علی خامنه‌ای، در تجمع شبانه حکومتی، گفت که مجتبی خامنه‌ای در جریان بمباران بیت علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، از ناحیه زانو، کمر و پشت گوش آسیب دیده است.
حسینی گفت: «زمانی که در دفتر بودم، در ۳۰ متری ما بمب خورد که شیرازی [رییس دفتر نظامی علی خامنه‌ای] و دوستانشان پرپر شدند. ۷۰، ۸۰ متری ما جایگاه کار علی خامنه‌ای را زدند که آن اتفاق افتاد.»
او افزود: «منزل مجتبی خامنه‌ای را زدند که همسرش کشته شد. مجتبی خامنه‌ای در بین راه که آمد در پله‌ها که برود بالا، موشک آنجا خورد و خانم حداد [همسر مجتبی خامنه‌ای] کشته شد. مجتبی خامنه‌ای در بین راه ضربه موج [انفجار] خورده و روی زمین افتاده است.»
مسئول دیدارهای دفتر رهبر پیشین جمهوری اسلامی، درباره آسیب‌های وارد شده به مجتبی خامنه‌ای گفت: «یک خرده کشکک پایش صدمه دیده و یک خرده کمرش. کمرش در این ایام درست شد و کشکک پایش به زودی خوب می‌شود و در سلامتی کامل است.»
حسینی گفت: «یکی از عزیزان در هفته پیش با او دیدار داشت، آن بحث پیشانی که گفته‌اند بی‌خود است. یک ترک کوچک پشت گوشش خورده که آن هم پشت عمامه است و اصلا مشخص نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75340" target="_blank">📅 01:17 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhyhOWpBBIyMscp9zNPC5laMVHPzYm49yFczJKARco2VHCPRqa1dntRCPxBSMBDUsBey7Ki3PaagOXd_5WNaIS8mmZFhNvxKu3UubNArY4AmABYGsLfnJCMJLOOTaK-T8q8qKpl0abmOvO59egK3EFVp7Vh6Gh35ZYdO42OZ40yi8JWJE3yr9n8EC6-aq66uo4cdCdYjgcrSY3iQsOukFmIXjub-OMZTnCYZ0irfoadVIhdAx51v29mWtedhq3IJMx7KWpB_O2DqW1vn2ZarU_AN6hIfe519Ly12flTOo-MR78diC4iGUPy_DstBEalhCvdrfj7zWnDVvDq0wYXiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۱۸ اردیبهشت، اعلام کرد که روسیه و اوکراین بر سر یک آتش‌بس سه روزه که از شنبه آغاز می‌شود و همچنین تبادل متقابل ۲۰۰۰ اسیر (۱۰۰۰ نفر از هر طرف) به توافق رسیده‌اند.
ترامپ در پیامی ابراز امیدواری کرد که این آتش‌بس در روزهای شنبه، یکشنبه و دوشنبه، «آغازی بر پایان این جنگ طولانی، مرگبار و سخت» باشد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75339" target="_blank">📅 22:20 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pndprIBMbnMfea3BHcojeSJg3uIclR6AwDuryUI3jAPy38WC4sWUFIv_5L-kh52jL76XPmCCQ-08YXbuiOf1EPS_vsMQYbQI2NH6LpwibVL23K7qY7Ats_AYkg1IgETL5FEUDjhp_iZ_1cVffGp8TzVlmGuug72sB5D9GqZ6Uidi2HumNYzJgICVjZhmIAlElKFsyaZd2Fpp8dHUrCTSInG5NsFmJqctcSmB7SA2YSZsuGLukTAgNKmMDQ0-VzAPb194RMHr5RQOTCg12XMdXnUkRsJEHVYpNjgIVA00Jwv-IV4DZjYDPCqwi-Fua3mJSmn50rbC7HTi7V8CDpCPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»،رسانه نزدیک به سپاه پاسداران به نقل از یک منبع نظامی نوشته است که  «پس از مدتی تبادل آتش، هم اینک درگیری‌ها متوقف شده و فضا آرام است». او اما در عین حال ادامه داده که «اگر مجددا آمریکایی‌ها قصد ورود به خلیج فارس را داشته باشند و یا برای شناورهای ایرانی مزاحمتی ایجاد کنند، مجدداً پاسخ قاطع دریافت خواهند کرد. بنابراین احتمال ورود مجدد به درگیری‌هایی از این قبیل در این منطقه همچنان وجود دارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75338" target="_blank">📅 21:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jg16TopvDC3mZWMqjQfMe1OtcM_3vU6xIbqQ08gv3c0tTfaqaSJja-x1K-8fPZFTgwAovSa-vkAXZ9WOPY5jhnkD613Kvpq_2vS5YuOJ0YQz5BA5lAYhxvjD0O6U_hQye8pBu4qTsKtm_lzFuFQ_IxfdIwKjUGSjiBz34m1VCAraq7oD7fgety4nm28mNPXPp2URv_ByMoBji-3MBePGyxl7wavJSt7llTm5fuoZhAV_vXowXkc0zFWHZnX08c_2v7K39KHuPMDk_2bLyOKvs65KfXtG88l6VC_m4REEX518G5i-Hchl2TSfLcW9ib86G5iGExLG3Ki0IzDUW5KBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/chc4HOGqN0tr1RCsHOTmTPTWMugUU0oKinglSCxMgL2l4VaYJcdN_MIycAuIn5R9Z7THDU2aHmCz_LJtb7aZhBmQj-5vHiu_oR4OFlWZAofuS28aYROHyu76o6OiJsIiaTtQtoQGRDfIS9AaSslbfHaRZgtaCZHMAWpI4CfjpX_V7MvxGBy2xQMBtXnHmnVuJmQVmJsFG1cmYVucOoA-F1lbmIp0G7CkKAPrbdSYhwsdVewhdaVak3Yp3jMuenhjP3sYNWFX_JYlCDEQFBSXeY1wHlRbCOOdG_0QXnR3HhctlOVGJC8DXEP6GHsTGsOqHyiAfrGkZV9aHU2YYlqssw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که در راستای اجرای محاصره دریایی ایران، نیروهای آمریکایی طی دو عملیات جداگانه، سه نفتکش با پرچم ایران را که قصد ورود به بنادر این کشور در دریای عمان را داشتند، از کار انداخته‌اند.
در آخرین اقدام در تاریخ ۱۸ اردیبهشت، یک جنگنده F/A-18 سوپر هورنت برخاسته از ناو هواپیمابر «جورج اچ.دبلیو. بوش»، با شلیک مهمات دقیق به دودکش نفتکش‌های «سی استار ۳» (Sea Star III) و «سودا» (Sevda)، آن‌ها را از کار انداخت و مانع ورود این کشتی‌های خالی از بار به بنادر ایران شد. همچنین در ۱۶ اردیبهشت، جنگنده‌ای از ناو «آبراهام لینکلن» با شلیک توپ ۲۰ میلی‌متری، سکان نفتکش «حسنا» (Hasna) را هدف قرار داد و آن را متوقف کرد.
دریادار برد کوپر، فرمانده سنتکام، با تاکید بر پایبندی نیروهای آمریکایی به اجرای کامل محاصره، اعلام کرد که این سه شناور دیگر به سمت ایران در حرکت نیستند. طبق بیانیه سنتکام، تاکنون چندین کشتی تجاری توسط نیروهای آمریکایی از کار افتاده و بیش از ۵۰ فروند دیگر نیز تغییر مسیر داده شده‌اند.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران، روز جمعه ۱۸ اردیبهشت از وقوع «درگیری‌های پراکنده» میان نیروهای مسلح جمهوری اسلامی و آمریکا در محدوده تنگه هرمز خبر داد.
فاکس‌نیوز به نقل از یک مقام آمریکایی، اعلام کرد که این درگیری‌ها ناشی از اقدام آمریکا برای مقابله با حرکت یک نفتکش متعلق به ایران بوده است. بر اساس این گزارش، نفتکش مذکور قصد شکستن محاصره را داشته که با مقابله شناورهای آمریکایی مواجه شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75336" target="_blank">📅 19:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsklA3pHy96mG8UGZmxGKbibO_ibIK4pHFPIfQW-9QFnUQCfLhf7DQ1yq9jhL4rCNgc_HjCc3y7PB1gr3KQTNCuqisIBnvAKZfGD1iW5R7PwgBSWuzJGZ0SvpzEenxaZd_KvWATkNLIbdA7YVJnktpIn5Y12gT-sjMeeE_bUjT3XUhOng8sjgWQcShupGdvx46YVoVcshpz7ktZoDOtZP9EebGGccB7xDx67jJsDlYcHTsOBZeMaiF2syeripcwnCjaKSXquRQLdlfBvQ4rSrDeGVM028AfY-OZpTAguCRSqMVpxEACRKg07UHVroNqBGyaKj88LSe1VRAUrD4Mo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روح‌الله مومن‌نسب، دبیر ستاد امر به معروف تهران نوشت نمی‌شود نیروهای مسلح، مرزهای ما و تنگه هرمز را به روی دشمنان ببندند اما دولت فضای مجازی را در اختیار آنان قرار دهد.
او افزود که «فضای مجازی به هیچ وجه نباید به حالت قبل برگردد؛ همان‌طور که امام شهید ما به حالت قبل برنمی‌گردد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/75335" target="_blank">📅 19:23 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PpzAP330Z1dqZe4gbhQbRRdOBHMsb0NlL1_Zxp7pDLzu3KSlQbcYce2Z-7JUqniJssQhoi7Cg0hnSSzgjsx7GAut3CMY5B68ERtM2AJDX1_35XExv_TH5vsA3aEWxyMEK64vcvV09rPb144lxCwK1z5gVCayq5FF3sJlVsm-ytMtwgxVyiBN1iPu_gLR-e0kpHkDc1JzYM-GVQ6CNBxR8-I36kqa0K3aYGnslyNjB-3_rruCCY2rv6tToccvhtq2DOymLqaNrpOmOHA4HcOlONKzhhXRQu-i8pdFHEfU0_k5Xm87EAbkmAHPkZlGYlwbxC3o0kTia1eHYP-qO98FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در حساب تروث سوشال خود با انتشار تصویری شبیه‌سازی‌شده از انهدام یک پهپاد ایرانی توسط سلاح لیزری نیروی دریایی آمریکا، سرنگونی پهپادهای جمهوری اسلامی را به «پروانه‌ای که به سمت قبرش سقوط می‌کند»، تشبیه کرد.
او در واکنش به درگیری‌های شبانه ناوشکن‌ها در تنگه هرمز، این تبادل آتش را تنها یک «سیلی از روی محبت» (Love tap) خواند و تاکید کرد که آتش‌بس شکننده منطقه همچنان برقرار است.
سلاحی که ترامپ به آن اشاره می‌کند،سامانه لیزری ضد پهپاد «لوکاست» (LOCUST) است که پیش‌تر اعلام شد بر روی ناو هواپیمابر «یواس‌اس جورج اچ.دبلیو. بوش» نصب و آزمایش شده است.
به گزارش وب‌سایت «وار زون»، این نخستین بار است که یک سلاح انرژی هدایت‌شده روی یک ناو هواپیمابر کلاس نیمیتز نصب می‌شود.
مقامات عالی‌رتبه نیروی دریایی اعلام کرده‌اند که هدف نهایی آن‌ها، تبدیل این سلاح‌های پیشرفته به گزینه اصلی مقابله با تهدیدات نزدیک در آب‌های بین‌المللی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75334" target="_blank">📅 19:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75333">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z19hwt2WRTU4kW_j1OFcZ9oZxfIfCwEGpd2LRdaZocvWHjwS3bqdL1EUb3oVmNCvCiKWKPiynTex55L-e7-LqFLLvUdyVqhA6KGExQVObHYtRqGscvfMh0nT9OR62aQiNf8bag3yT2cfCDtwmJmm-OfFRUl6CcwAW7BqD7gWsOj6IPv01UHmyv0S5QUuByX4hqXfffrq4EpO1eV-mwbxJwTFo_yEbbRITIhQ-mLRDZOguGGy4XUBYZskNDA7FlGyC8rWrk1tiMSVdu9BYZ8ezyF44Xuhbx4K-Nqs5llRMhcYxIdEGleaALY_poUM8VYBzlwfouLkjhABsIhENXm--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار میناب: حمله آمریکا به یک لنج باری یک کشته و چهار مفقود بر جا گذاشته است
فرماندار میناب می‌گوید که در حملات دیشب آمریکا یک لنج باری هدف قرار گرفته است که منجر به کشته شدن یک ملوان و مفقود شدن چهار نفر دیگر شده است. [گویا قبلا گفته بودند پنج مفقود داشته بعدا جسد یکیشون پیدا شد]
به گفته محمد رادمهر، ۱۰ ملوان دیگر این لنج هم مجروح و به بیمارستان منتقل شدند.
به گفته آقای رادمهر این حمله در نزدیکی آب‌های شهرستان میناب رخ داده است.
عملیات جستجو برای یافتن سایر مفقود‌شدگان ادامه دارد.
دیشب نیروهای ایرانی و آمریکایی در آب‌های جنوبی ایران تبادل آتش کردند، هرچند دونالد ترامپ می‌گوید که آتش‌بس همچنان برقرار است.
آمریکا می‌گوید که نیروهایش «بی‌مقدمه» هدف حمله موشک‌ها، پهپادها و قایق‌های تندرو ایران قرار گرفتند و ایران می‌گوید که حملاتش تلافی‌جویانه و در پاسخ به حمله آمریکا به یک نفتکش ایرانی و یک کشتی دیگر در منطقه تنگه هرمز بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/75333" target="_blank">📅 19:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rZEjW3_ubkq14YAQtEIdiacglGUFyxMh8vrBaOdWMZUSnzxvIzx9U-X1t69hkspfy9HZKNSJd6ovRwiirig7r-H6HZGwmStNwIdoK_kfDNBV3mvK3TaydaGWb2lWdwwf2Fby6ksY0hrDFpj5ujM-6fI7bu1pjrAoHtx57MVgy_b5nXFm6K4W9HbkBCqX7plN3im8Pj0d30UZyl4uiuOZNxZILAHiDAQvlrew6yHHWw9FhkLxLoEaeR0VVOiQNDR-Gur_akzL1DmoLaaLlzZlLb6VbErWIqh-qDOVLOAiIe_WF1k401Rb077vW79nQJetiFEX1qWrWSco9XC6uLVe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NpHCWaYzS7qE1QLGJvgt-cA5h89Im0-RcqqmDjrr3sNZO0DIRkf2A2rGeXsa3Cc8-sOQ1RdbTiAwDcpuqn7oQAGnRSvhmgA05JAsinrKNl0Kgx0W4Zmbh6H8RhRksDMffGCrSNm3rSArus1-1mnVhSE7KByplMYPLq7pz_6qsXoVjH_-EnXGv8dsW8etNn2K9XUvaKdfD1SurokE28EDaNAwH3qbhDJXi46uXzbyOfwAbfm8mpuA1uVlflKCRWF_-G8Q_55L9tOXYF_lz3sBO4waIRqCqlF_KibfC-VhA7wU6I-FjnhfAU92TJHOJupnCTciI-DgSuUtZ2CO102SmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ly80T9aQjhJnbwlLtDwV0CvnsbVaIoaGbOndgFDS24HU1DZxVc3846DiOKo8HsFPZhktI3Ssq31kRsCfhnap_IMLmTFUnE_HfOsJod-UazIpSt_7iB_XWSWLxWBpYCdc-fbLHukNXKKTmYxBnPccZhu-iPmxcPsJpS5IdUq91txXmgBnRxMkDVaYOgVULYm-xHwzgRmXTrMuENFzo_l6b67wW7nybwOV19nzNKftQ-o_Bg_ykQgbyfR2kuKkN4H0GPNFTOqQxLEh0O1xj_4v54Q3Xl6-MNBTNO_fi53WjS7VMqEJFXMLPTedbgvuycb1Qxa_tDh1Sk-a-nhhLoBgxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/858d7055f6.mp4?token=PNFW3HXUVSiEA_mM660dtK-j_G3I7-YYPiivxadqM6HkFqLy-jrFFDhUYiZBBmbwta677_vqaZzOrLdE4uh7maR5hcq5SJfXmWcDoM8_WLueM1YUBWSdACsNDmXice8XvTN99bUYpDQfRpKo_wowhy1MYBoYUhbt9i1xUH8yXM6Yr6SSsEPDcNetngn_1YhU8rsfULKzDBIo6LBnE7KslGVCNTDDK10c-bYu_w5ojTp6mCqT_Xrc9eyRYqBO6fWOM1cN1bUv0BdyukFLXg7A3fnH4rAtM_6MR8s40izPO4XhxAbaiu3AzUkpCZ28Ek-Du683r5M4yl1bcHvAKSV76w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/858d7055f6.mp4?token=PNFW3HXUVSiEA_mM660dtK-j_G3I7-YYPiivxadqM6HkFqLy-jrFFDhUYiZBBmbwta677_vqaZzOrLdE4uh7maR5hcq5SJfXmWcDoM8_WLueM1YUBWSdACsNDmXice8XvTN99bUYpDQfRpKo_wowhy1MYBoYUhbt9i1xUH8yXM6Yr6SSsEPDcNetngn_1YhU8rsfULKzDBIo6LBnE7KslGVCNTDDK10c-bYu_w5ojTp6mCqT_Xrc9eyRYqBO6fWOM1cN1bUv0BdyukFLXg7A3fnH4rAtM_6MR8s40izPO4XhxAbaiu3AzUkpCZ28Ek-Du683r5M4yl1bcHvAKSV76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، گفت اقدام نظامی آمریکا علیه ایران در بامداد جمعه «جدا و متمایز» از عملیات «خشم حماسی» بوده و ایالات متحده همچنان به‌صورت «دفاعی» واکنش نشان خواهد داد.
روبیو روز جمعه در شهر رم، پایتخت ایتالیا، در جمع خبرنگاران اعلام کرد «خشم حماسی» که او اوایل این هفته گفته بود به پایان رسیده است، «یک عملیات تهاجمی بود که برای نابودی سکوهای پرتاب موشک، نیروی دریایی و نیروی هوایی آن‌ها طراحی شده بود.»
او افزود آنچه ساعاتی پیش رخ داد «ناوشکن‌های آمریکایی بودند که در آب‌های بین‌المللی در حال حرکت بودند و از سوی ایرانی‌ها به آن‌ها شلیک شد، و آمریکا برای حفاظت از خود به‌صورت دفاعی پاسخ داد.»
دیپلمات ارشد آمریکا گفت: «فقط کشورهای احمق وقتی به آن‌ها شلیک می‌شود، پاسخ نمی‌دهند. و ما کشور احمقی نیستیم.»
وقتی از روبیو پرسیده شد که آیا آمریکا خطوط قرمزی را به ایران منتقل کرده است یا نه، پاسخ داد: «خط قرمز روشن است: اگر آمریکایی‌ها را تهدید کنند، نابود خواهند شد.»
وزیر خارجه آمریکا همچنین خبر داد که واشینگتن انتظار دارد روز جمعه پاسخ ایران به پیشنهاد واشینگتن برای پایان دادن به جنگ را دریافت کند.
روبیو در این زمینه توضیح داد: «خواهیم دید که این پاسخ شامل چه چیزهایی است. امید ما این است که چیزی باشد که بتواند ما را وارد یک روند جدی مذاکره کند.»
او همچنین تلاش‌های ایران برای کنترل تنگه هرمز را محکوم کرد و گفت: «ایران اکنون ادعا می‌کند که مالک این آبراه بین‌المللی است و حق کنترل آن را دارد... این اقدامی غیرقابل قبول است که آن‌ها تلاش دارند آن را عادی جلوه دهند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75328" target="_blank">📅 19:18 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXjTV4V8lOwt8J60tMGnHNViiihrqglDeDsA90nhuTSi1Nwa5XtZorhVzn1IoQl7TZQUiGDXYYHRz9KDQc0vgSdXkGye31S81AtqMA7nvPYk6HROMmWDPmRRC3Mb4OiQyPy8aty_TiKRpyWsRPw6p7O6JO46VMwcyXVfqMtNFq7oERtGvQ4qwVnFbA8FZ9GYW8Bfh31hJaTG20UPQyDcDjRTSQserQZV2fYT97bklIW-RbFIjNJgWTNpHJnlMVHJC0f9avx8ZzT08ru_gqTV1hYnohHk4bikqOmXcnLpcKY-fmNnz2uPwpk4acffzDrN1Ufu7gyFZNWFxjcCWAf7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی، آمریکا را متهم کرد که با «ماجراجویی نظامی بی‌خردانه» دیپلماسی «قربانی» می‌کند.
عباس عراقچی در پستی در شبکه اجتماعی ایکس نوشت: «هر زمان که یک راه‌ حل دیپلماتیک روی میز قرار می گیرد، ایالات متحده به‌ یک ماجراجویی نظامی بی‌خردانه رو می‌آورد.»
آقای عراقچی در ادامه می‌نویسد که دلیل این اقدام چه «صرفاً یک تاکتیک کور برای اعمال فشار» باشد و چه «فریبکاری یک خرابکار» که می‌خواهد «رئیس‌جمهور آمریکا را به باتلاقی تازه بکشاند» و یا هر دلیل دیگری «نتیجه همیشه یکی است: ایرانیان هرگز در برابر فشار سر خم نمی‌کنند، ولی این دیپلماسی است که همواره قربانی می‌شود.»
او همچنین ارزیابی سازمان اطلاعات مرکزی آمریکا از ذخایر موشکی ایران را اشتباه توصیف کرد و نوشت: «ذخایر موشکی و ظرفیت پرتابگرهای ما نسبت به ۹ اسفند در سطح ۷۵ درصد نیست؛ رقم صحیح ۱۲۰ درصد است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75327" target="_blank">📅 19:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75326">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urcrxy2GG7R8q6Zk3dRSU31xYWBp5QdXQZsm3u3wAPhkAQE7MI3M9gRiJOzSfZBSkAAhQRgMW-E_cLB5fxDMETfIA4obyoNdsvarjc1h_GlSNGjokoL43xew63A2p4bwQyU-hUvxN8CdI8pHz3HI85CQxeVgbyHewRfreVHcXOOdbWKkgMtNAbGe-dBbW4z-vc3QIXQ1dSy8P3fxu06TCD_nd0nNdYO22cx6lkRA0H70CD6VSF7oG5fTv3ucvS3GfqmvWtJI9moj01Jh9jr3HWcuIbD0_eu-LY35l93-hFvZ_RfwjfgVpAdT3XVI0pc-R__MpfksI1VtHbPwIDuEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، فرماندهی مرکزی ایالات متحده، اعلام کرد از زمان آغاز محاصره دریایی تا روز جمعه، ۱۸ اردیبهشت مانع از ورود یا خروج بیش از ۷۰ نفتکش از بنادر ایران شده است.
سنتکام در پیام تازه‌اش در شبکه اجتماعی ایکس نوشته که این کشتی‌های تجاری ظرفیت حمل بیش از ۱۶۶ میلیون بشکه نفت ایران به ارزش تخمینی بیش از ۱۳ میلیارد دلار را دارند.
این موضوع ساعاتی پس از آن اعلام شد که ارتش آمریکا گفت نیروهایش در نخستین ساعات بامداد جمعه حملات «تحریک‌نشدهٔ» ایران علیه ناوشکن‌های آمریکایی در تنگه هرمز را رهگیری کرده و در پاسخ، «تأسیسات نظامی ایران» را هدف قرار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75326" target="_blank">📅 19:10 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75325">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1KBbJjcm93W-UP-RocTuCpBwfidOd69fc16UeFI2lZ6UpUQw51VZl5deBPX6wksovhcxT4oNHR_IfLt4s9Uls8qcsRJlLVEsHLXlLIdkXThvO2VCznZlN5eXbEsOw3WRIHnTwgnO5lIi7uCCyeK9zSihRfMGCQVGLGiPow7rF2A2cQVgLCZ_RKU35vQMUp5ykgP64w0ATPGsXFjWvjjwO0Txq-DxDgkBd7fEgsV18t5wkxwHLYvbODUIoGwfX4StkejwyC34MDx-DfepkG9aGDqlB3Y9HZPg7c2BP5R6w-kYi5nZsemWoBpDV3b0nk3TLn6tEJbXCYxNm737ii1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هفتادمین روز قطع اینترنت در ایران است و به‌گزارش نت‌بلاکس این اختلال صبح جمعه ۱۸ اردیبهشت از یک هزار ۶۵۶ ساعت فراتر رفت.
این در حالی است که مقامات و افراد نزدیک به حکومت یا کسانی که حکومت خود با واگذاری «سیم‌کارت سفید» انتخاب می‌کند، هم‌چنان به اینترنت دسترسی دارند.
علاوه بر آن، اخیراً برخی اپارتورهای نیز اینترنت موسوم به طبقاتی را باقیمت‌های گزاف در اختیار برخی مشاغل و طبقات قرار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75325" target="_blank">📅 19:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhSb2VotOyru-hUTbMijb_AYjf71SYQtVjjLjYSa_Jt5UzG20le02KPbjU2aUWWKzVmKpvTUhLhrNhMAiOIZL4Wuoo0_A05Zqh0v56ebxbyJk4BAllswyzAG_Fn5FGrVITomCIc-ydEImHSlSQd0WlK6aqSvyTYw7OtYRwxoTigS1Nba4gmJXhvBFQDcOJoCK94PZhPZHk232EhgtLV_GiMlnr4kgEUbks6RzMPoIP1z5nkY5cd44ShIUtNVyMJWLX4QAC0-3CFevlqDVgfpddRJJLa7kNuyxhN_ZBxN79Bc989k5PaFQlvgkEmJ5O8RpPO082bZ6iuCAh0sPZ8-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز جمعه ۱۸ اردیبهشت و پس از حملات متقابل در خلیج فارس، تنگه هرمز و انتشار گزارش‌ها از مقابله پدافند امارات متحده با موشک‌ها و پهپادها، پیامی «تهدیدآمیز» به زبان عربی منتشر کرد.
بقایی در این پیام نوشت: «اگر دندان‌های شیر را دیدی که بیرون زده‌اند، تصور نکن که شیر لبخند می‌زند.»
به نظر می‌رسد با توجه به حملات روزهای گذشته به بندر فجیره و دیگر نقاط امارات و اتهام‌های قرارگاه خاتم‌الانبیا پس از درگیری در تنگه هرمز، بقایی با این پیام امارات متحده عربی را تهدید کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75324" target="_blank">📅 09:38 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/veG3IGsPqRGBrCacIygE-oudM_lBZAVdAujuaTwwy0vAMDttyk2TR4hd_Qv4CkGFNgTXCV86YNcwWQUi_vcG_p_UKgHoF0mIGyWTlFSGOwSFLVQcb1z3wTjtj1dYNJ_o2dZJt2fsrYdxmM1jHMnK_o_8RuSO_5NPbfzyT0eqzg_xXX_OGEIYRYV4kps1bQjmYN576DjnUKPwIRc_mDtZyLIEP7u1wlm5KiJt0h2EXZt_fT5coYZePAv66hU_kp9MBuRx8L1zLp6BZsRhg6u9-qMGyPGO5YuwzxMt_ULRXijsqoZarDizXeqCH5f_Ri_upxaVOr_oMlom3QSkImGXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اوایل روز جمعه اعلام کرد که سامانه‌های پدافند هوایی آن در حال مقابله با حملات پهپادی و موشکی از ایران هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75323" target="_blank">📅 06:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lT6u6IaM7plRDqRyz8ZZO7QYEldJZo_wDYg_LvDW7CuXGnt406eiQqvqIqhs2QQnyGR-hSv4sgjFVQR80yeAo0iEu-jsuKWsb0oo4dk76a3YkrBpTlbVa6BtHMLtGNyXCJGwMedtbTc5N_nbULTMuK2ds3GJsTmydQesbQTNJKvH8mC97m1Z_6lvrx6h_-lErw4WikLWuexARA10mpKayQSlMWET9ajkvn6KWSHh87lneM4eeOgtLmzFIMhhvaNxH2JhZpJZUQ76QIoyOeBtZ3estaHb92V2k4rEzkzAcK3v-my7NoBua276oUwWaJ1lXWnyTYRhPehjGBzT8glSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pp1kX4sFbUqYo4UvlVX4DJ4FZks9buxfD1tkdTRia812SCqCde4ZrbpMQC-Fmel54Eg_x-kc9mECEnZG_7riKsvfS84BkkDDKIhARxddwxNpfvpvcEUYL6MuKWamex5cYoJcwoUAKT-V5CV_lHBG_cTan2iBtv5X1MxzSnA8D2A7x8095IzdDhWIu8A51bmBeMVfE3IJD81iT_8XmiBPcG7ZbudQd2hHsvxodT4fAWLrGe2BvZkLUg3Opk7FAHFGxM0aKedL4NFqJYddzuHU7M66Ou3lcmXAst9Kp963dBrgB9wBSieWh26p2VCekhjnpcs_BxwFke-yCMETy1GXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VwXZsRkm5Bpzl41FJcARtGwgxHnWD6FfQNbtDgX5M2eOAbivOdYWCJQk5UVT0V4gy9IMLmhj9Mgo4OGcmCIhqUiIeqQPgvQ_L0ICyyqYa_z6GOfl9RkFJbJfw0ZzqTHTdn3jsG_DInL1TMgzHIlxxzzegI1ryLojFbTl1RaxV0Kv8V4SK3dDwRRD3N5DC_sOZzcFZiScEEe5C91GbHJg9eVQmB5uNHwMj7k1lkgw-HUAuLKKhem-DN_2yi_ZLEQsrJ-irIPjAtru-NKaSgWHQ5LxYFOMA1D8awrD7uHVFSYPRnYetTTWYQjuvmPr5D-Vw6o1nUGrcKkd6hQNe5uY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FLwVEKgUTHABRbsbMS635l2sC0qSHjr-iUFCQWX2KDsAKGTT8D6z4sKzrZl900GnwhuZlNaiDoSALLoS3HqCwI0U8Zo6IzGtO-Ys61UsEsrQCK8iFA-flCO1cxnaCZuQFgzrN9GqLA-b42FIZMmY84s4H3xxj3oRox4RUJfjfA6W9CbiQn0Fmdzoev1YHZbImjSjZT3wWstb3NBT2EMrEg4ZtFNQdpkr3wpqMVf8Pbk-sEOh26NJd2tiLPHivNAZ0uwzVfxDIW0K71YwYFMrCkcSfAFT43SJeebLo53h62UDCwevw9cNZVZi0xyYb7Vg0vVmIggqFJ6whrBWw7tkbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V7VeKRJLcCFnq-e-Qg8tKj8tBNHdS1_Dk-7OCZncliwt1lH-kYEhjjk8ERSuQxXTSTzq3GKFehoa_i2IEFuTogf1PoDkOVpPCKc9KIHm4ubF7vb4rPuueI2d0eKU6SjyZ420IYDy6sLXeneqZwbG_T69uYEAGLJHpOPYkPgaNw0uLQRcH-Ax6W2m9EZEx5rN9e7_z6NpDkzAXL_qNcF3vu0rCKTVGxnAH3ik78sWq-obL26piQbbfTilZ1iRzIGMEYiOVXfOIh3wCEKYy5ViMJilK3Aok9hkMZvA8e5vUirIDuWHqx8ilzXxEmecuiUxDAxDABGU0Omv5xyImQi6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FaFOcUTjsgqtZx0SZ1XGdemoahrm33XbcokJPGxnv_PmM-00zCIj62UamoHto8zmGNiAiRO-llDsyDyBYDw6kqWJq4Yh5S_dKiAcCerTi38EblssFfEc46M83_ESr95OskQ-qGw60BuSidywwTnuuZvzRMHDRsxRS0BLrHLfzK7YUSBrr7L8aiGarAWLu6NaYnv_PNaQTIlQSkUgY8A7MwF79Z5zA6RRJRymml-Gts8Ajb909_766v3ZUMf7zF_rGdZ32FOz-25poeILoUWHZidLZ2aEGJgjzgAlmsDPGWT2aC94lYKvvDDlo2TxUEKtpGDFtLLSG3IzFSK_v78oYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e24b568a6c.mp4?token=Rejm2VkJgrGEVXJFAoSRwNcAGDxFO1n4lMOnoGF5oCnNAQEDr85pqIcyTpEmp4rg21jPPJhKDjDV08t-SXlf6yIpiEpd29QdqMCzfJi-YpbRcfD3vsIoj4j0RClKiXTZm4mfEIByHhQYtoX-mSxwZu8LuoCPkR1p3iVZdUEIYFzLCnQg-mf3oK7Ubozi148d6nYWbhTZhzaNlKZ1kXXEPCMEau5ZMPEdsGHX0kHc-V5c16gwapt329ifTL8pmZqaGWeUbMrBUsYsOsSDpzRicEQaq_ECDEBZP6F0R-Xr2ndmT4jREuX1I9rXi6gJWSBGEJJD5rybkg5zDUZEO-DmbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e24b568a6c.mp4?token=Rejm2VkJgrGEVXJFAoSRwNcAGDxFO1n4lMOnoGF5oCnNAQEDr85pqIcyTpEmp4rg21jPPJhKDjDV08t-SXlf6yIpiEpd29QdqMCzfJi-YpbRcfD3vsIoj4j0RClKiXTZm4mfEIByHhQYtoX-mSxwZu8LuoCPkR1p3iVZdUEIYFzLCnQg-mf3oK7Ubozi148d6nYWbhTZhzaNlKZ1kXXEPCMEau5ZMPEdsGHX0kHc-V5c16gwapt329ifTL8pmZqaGWeUbMrBUsYsOsSDpzRicEQaq_ECDEBZP6F0R-Xr2ndmT4jREuX1I9rXi6gJWSBGEJJD5rybkg5zDUZEO-DmbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در گفت‌وگو با خبرنگاران در واشینگتن، با اشاره به درگیری جدید آمریکا و جمهوری اسلامی در تنگه هرمز گفت نیروهای جمهوری اسلامی با آمریکا «شوخی» کردند، اما آن‌ها ظرف حدود دو دقیقه نابود شدند.
او گفت: «امروز سه ناوشکن درجه‌یک آمریکا از تنگه عبور کردند. هر کشور دیگری در چنین شرایطی چنین کاری نمی‌کرد. به آن‌ ناوشکن‌ها موشک و پهپاد شلیک کردند و این قایق‌های احمقانه را به سویشان فرستادند. آن‌ها ظرف حدود دو دقیقه نابود شدند. نفتکششان هدف قرار گرفت. می‌دانید با نفتکش چه کردیم؟ نمی‌خواستیم شرایط حادی ایجاد شود، بنابراین سکان آن را زدیم و نفتکش شروع کرد به چرخیدن دور خودش. نباید امروز این کار را می‌کردند.»
ترامپ افزود: «همه موشک‌هایشان سرنگون شد. همه پهپادهایشان سرنگون شد و کسانی که آن‌ها را شلیک کردند نیز دیگر در میان ما نیستند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه گفت پیشنهاد واشنگتن برای پایان دادن به درگیری با ایران، بسیار فراتر از یک «پیشنهاد یک‌صفحه‌ای» بوده است. سی‌ان‌ان نوشت، تهران همچنان در حال بررسی پیام‌های ارسال‌شده از سوی آمریکا از طریق میانجی‌های پاکستان است.
ترامپ در پاسخ به پرسشی درباره اینکه آیا ایران به آنچه «پیشنهاد یک‌صفحه‌ای» توصیف شده پاسخ داده است یا نه، این توصیف را رد کرد.
او به خبرنگاران گفت: «خب، این بیشتر از یک پیشنهاد یک‌صفحه‌ای است. این پیشنهادی بود که اساسا می‌گفت آنها سلاح هسته‌ای نخواهند داشت، گردوغبار هسته‌ای را به ما تحویل خواهند داد و بسیاری چیزهای دیگری را که ما می‌خواهیم.»
وقتی از او پرسیده شد آیا ایران با این شروط موافقت کرده است، ترامپ گفت: «آنها موافقت کرده‌اند. اما وقتی موافقت می‌کنند، خیلی معنا ندارد، چون روز بعد فراموش می‌کنند که موافقت کرده بودند.»
او افزود: «و می‌دانید، ما با مجموعه‌های متفاوتی از رهبران طرف هستیم.»
@
VahidOOnLine
ترامپ در واشینگتن به خبرنگاران گفت: «مقام‌های ایران بهتر است خیلی سریع توافقشان را امضا کنند. مذاکرات بسیار خوب پیش می‌رود، اما باید بفهمند اگر امضا نشود، درد زیادی خواهند داشت. آن‌ها خیلی بیشتر از من می‌خواهند امضا کنند.»
ترامپ گفت: «ما اکنون در ایران با مجموعه‌های متفاوتی از رهبران سروکار داریم. وقتی درباره تغییر حکومت صحبت می‌کنید، آن‌ها مدام از تغییر حکومت حرف می‌زنند. ما حکومت اول را کنار زدیم. حکومت دوم را کنار زدیم. بیشتر حکومت سوم را کنار زدیم. بعد می‌گویند آیا این تغییر حکومت است؟ من فکر می‌کنم این نهایت تغییر حکومت است.»
@
VahidOOnLine
دونالد ترامپ عصر پنج‌شنبه گفت: «ما هرگز اجازه نخواهیم داد» جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند. آقای ترامپ گفت: «احتمال آن صفر است. خودشان هم این را می‌دانند و با آن موافقت کرده‌اند. حالا باید ببینیم آیا حاضرند توافق را امضا کنند یا نه.»
@
VahidHeadline
ترامپ پنج‌شنبه به خبرنگاران گفت آمریکا با وجود تازه‌ترین تبادل آتش با جمهوری‌اسلامی در نزدیکی تنگه هرمز، در حال مذاکره با حکومت ایران است و افزود پاکستان از واشینگتن خواسته است در طول این گفت‌وگوها، طرح او برای اسکورت کشتی‌ها به خارج از این آبراه را دنبال نکند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/75315" target="_blank">📅 06:17 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VHv9PMId1u_aPwLpa-2fJbIqgVa8jL88th9zrHcBN_Qew2LO0IgmUj3XFrtKE0v5pkexdBun2xsDuRZnQDMeV-oXo9uv9CfPGNUt5yqHET9Z2ddZN-4gcLprLrpJuaVXSg7Xbbteehe4Fxa8HNTBz26WgUAVcNaJ3rTM7dNdcBAz-YRrDRLCmhOsAF2tt_NkQ1Y0lIozQOpTm8WbGotkVI1oUVSsVt4S9VfJdFyBy6BSqnZ1g7veaYxD91lqyVOTaMcMQuIXdOEVYhUnePxBU8JCYu5Myua8Mj54r_mW35h0q71BCiqspIWXmsXSLsmE7-A_e2W9dW1VOoYIpX30AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران را دیوانگان هدایت می‌کنند
پست ترامپ، ترجمه ماشین:
سه ناوشکن درجه‌یک آمریکایی به‌تازگی، با موفقیت کامل و در حالی که زیر آتش بودند، از تنگه هرمز خارج شدند. هیچ آسیبی به این سه ناوشکن وارد نشد، اما به مهاجمان ایرانی آسیب سنگینی وارد شد. آن‌ها به‌طور کامل نابود شدند، همراه با شمار زیادی قایق کوچک که اکنون برای جایگزینی نیروی دریایی کاملاً از سر بریده‌شده‌شان استفاده می‌شوند. این قایق‌ها به‌سرعت و با کارایی کامل به قعر دریا رفتند.
به‌سوی ناوشکن‌های ما موشک شلیک شد و به‌راحتی سرنگون شدند. پهپادها نیز آمدند و در هوا سوزانده شدند. آن‌ها به‌شکلی بسیار زیبا به سوی اقیانوس سقوط کردند؛ درست مانند پروانه‌ای که به سوی گور خود فرو می‌افتد!
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند، اما ایران یک کشور عادی نیست. آن‌ها را دیوانگانی هدایت می‌کنند و اگر فرصت استفاده از سلاح هسته‌ای را داشتند، بی‌تردید این کار را می‌کردند — اما هرگز چنین فرصتی نخواهند داشت و همان‌طور که امروز دوباره آن‌ها را از پا درآوردیم، اگر توافق خود را سریع امضا نکنند، در آینده بسیار سخت‌تر و بسیار خشن‌تر آن‌ها را از پا درخواهیم آورد!
سه ناوشکن ما، همراه با خدمه فوق‌العاده‌شان، اکنون دوباره به محاصره دریایی ما خواهند پیوست؛ محاصره‌ای که واقعاً یک «دیوار فولادین» است.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75314" target="_blank">📅 02:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtEQfQUwxJ6oqz4WE-L2Y3-pRT6ZttS8jFJsVxlDBfzGTtnpBVZk9SWbjGqwltKTbWAliMo2p8RZXKU0Q4DZkXD5lK1ayTbu1oI79G2t9ns8vYNfpd5O7UEb8NSAFUovaaYdTe5QCG9OHcTgUrTuEYjKVsLOZz_Fgp858V6ayWnFK2cBY2FWXvJqt2VAriUbZY5axFxkSH-k8nMZVJstbeOk_ItmRE-H2wK_ohfejol6zSvtt-uXpvVEXm-MeRQ3y4v53YiJFvk6rYISzpAWVdLlPjP8p64XEVXKmNNq9ZHLL_epnrjnDWuaqR4T-o_Z72orAx_ALGbTZbliRHue4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا در پی حمله‌ها به بنادر جنوبی ایران و شنیده شدن صدای انفجار در غرب تهران به ای‌بی‌سی گفت که ارتش آمریکا در اقدامی دفاعی به رژیم ایران یک «نوازش دوستانه» داده است و آتش‌بس همچنان در حال اجراست. او گفت حمله‌های متقابل به ایران فقط یک نوازش دوستانه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75313" target="_blank">📅 02:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmI40zJ9XaA2w7HIeCu9rmGuSYlnU1LBgstYFhPlaG4FMb2ddlOkYf-EpmZgJoIyB62ESkTye296XfXh4djv5B8GEVKLZpkUJ-S1E2tOeZTfH-rx2JLCYatLbFpMBRfI79eAwYgCali2hTzXkW6nowk4qXJnOzFcIBrVquTWd6Vvw_ogly3EDgC5SHugU34V4C62c8c5dDHDY8qpCcDrx3-5sJ8XaxN-ZZEuqPiyE_xlYrEIdwdbERZKhrcHE4HNXkAIKU4i56nelf-QvE6OwSWkxZGluj8RU9WGEMSOPkhM-ia8cIHf_h93aM6Yl1RbtjgU2Niqsrvx8Jmug4eHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنیفر گریفین، خبرنگار فاکس‌نیوز، در شبکه اجتماعی اکس به نقل از یک مقام ارشد ایالات متحده از حملات نظامی این کشور به بندر قشم و بندرعباس خبر داد. این مقام آمریکایی تاکید کرد که این اقدام به معنای شروع دوباره جنگ یا پایان آتش‌بس نیست. این حملات دو روز پس از شلیک موشک‌های بالستیک ایران به بندر فجیره امارات صورت می‌گیرد. گزارش‌ها همچنین از حمله به ایستگاه بازرسی دریایی بندر کرگان در میناب حکایت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75312" target="_blank">📅 01:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvObJUOV7kI_-FpxQcBhGRMzyM3FDksWwn-UxRsOv5reHM0taI4LOe1f5-6dRICDPcOeQVGxB4B4HnUhhnt4gEYRdwgh1JqQ6gRP-g28OY-4gruT3o_SUoOC57O-adU-k7k7aIN_hA4umZ2mF4iFqALznaPx3SkvLZdgIoz_Kjg9JPtTy4-WRq0hN4hxWl3dYU_vcXTKqV7JoMCrnQZ9VleB5iIeixHaG9aHqvs4-BQswocxNh1lXIfljxK7OtSMMdFMD3zHrOTZiOBSmhTOMzcl2lO2KC2dG32_pz81TwmPrW7zkRIARjwT1rznjA22-Ut4VizuJqXieuAxZMK5fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، اعلام کرد نیروهای آمریکایی ۱۷ اردیبهشت همزمان با عبور ناوشکن‌های مجهز به موشک هدایت‌شونده آمریکا از تنگه هرمز به سوی دریای عمان، حملات موشکی، پهپادی و قایق‌های کوچک جمهوری اسلامی را رهگیری و به منابع این حمله‌ها در ایران حمله کردند.
طبق اعلام سنتکام، نیروهای جمهوری اسلامی در حالی این حمله‌ها را با چندین موشک، پهپاد و قایق‌های کوچک انجام دادند که ناوهای یواس‌اس تراکستون، یواس‌اس رافائل پرالتا و یواس‌اس میسون از این گذرگاه بین‌المللی دریایی عبور می‌کردند و هیچ‌یک از تجهیزات یا دارایی‌های آمریکا هدف قرار نگرفت.
سنتکام گفت نیروهای آمریکا ضمن دفع این تهدیدها، تاسیسات نظامی ایران را که مسئول حمله به نیروهای آمریکایی بودند، از جمله محل‌های پرتاب موشک و پهپاد، مراکز فرماندهی و کنترل و گره‌های اطلاعاتی، نظارتی و شناسایی، هدف قرار دادند.
سنتکام تاکید کرد که به دنبال تشدید تنش نیست، اما همچنان در موقعیت مناسب قرار دارد و آماده حفاظت از نیروهای آمریکایی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75311" target="_blank">📅 01:25 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b377a19a19.mp4?token=imagUwg3S6j74KZwWUcpN4C8f1ZbU8OF2xc2BCEqbL37rfzc6dpDa66wheRcaLCG0qLTwT-bvtmfTknP2HpA5nPm5JX7KRvt0Q-8Hv10ZL2KN-VHSw9mpiYUiTRMUdys6LzPvvRu_h2sSQFmZUue0rw3Q1uCcHG4X0MiAHaAsl-694QX5j1uhmGXE2q-oSuf7gk9RysCdLLYVu9UEnf15JVdHqH3LAzKS90Swp_5af0UC2UnFMkDs5922QvmImJ72woZjpkIhkmIQYzM8Xutx0ubvohp6eDwTSuw40hn4r2Y4mVR5nLVEjAug5lC9jxHH4eri_s6d1P37turRsFLrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b377a19a19.mp4?token=imagUwg3S6j74KZwWUcpN4C8f1ZbU8OF2xc2BCEqbL37rfzc6dpDa66wheRcaLCG0qLTwT-bvtmfTknP2HpA5nPm5JX7KRvt0Q-8Hv10ZL2KN-VHSw9mpiYUiTRMUdys6LzPvvRu_h2sSQFmZUue0rw3Q1uCcHG4X0MiAHaAsl-694QX5j1uhmGXE2q-oSuf7gk9RysCdLLYVu9UEnf15JVdHqH3LAzKS90Swp_5af0UC2UnFMkDs5922QvmImJ72woZjpkIhkmIQYzM8Xutx0ubvohp6eDwTSuw40hn4r2Y4mVR5nLVEjAug5lC9jxHH4eri_s6d1P37turRsFLrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه خاتم النبیاء که مدیریت جنگ در ایران را بر عهده دارد، ساعتی بعد از گزارش‌ها از حملات و رد و بدل شدن آتش در حوالی تنگه هرمز، با انتشار بیانیه‌ای این حملات را «نقض اتش‌بس» و در پی «همکاری چند کشور منطقه با آمریکا» ارزیابی کرده و گفته است: «ارتش متجاوز، تروریست و راهزن آمریکا با نقض آتش‌بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند و همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.»
این قرارگاه در ادامه مدعی شده که نیروهای نظامی ایران به این حملات واکنش نشان داده‌اند: «نیروهای مسلح جمهوری اسلامی ایران نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75310" target="_blank">📅 01:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHMs5vTAf0Vk6Cpy4AuvXLG830catxUI_lWXlcnLBk_x8Emn2B_W5rTQqbcb5LymJDjOwZcBP2U3eEJ7rk5vBmCRgJTvigOCvdCcj5yMZa3SQUP0a53FNHVrdywBkmT53pX5P5WcJD6HUaPQ3LZHOnK8OU8KMFdEd2OcAN4YnC7yJU3tBvDtWbvLxXnmRRYe6JHqlTf54Wl6hxk7z-QmESUn-Tk4W9iYk2EXaHcCPBN1teukpf9ZoXkNHkzqpsN46XDY9IbiRSL_W_hetb29pciy8-zogQktKx7J78wqVc4SeR1AzhfjrbNZlyj5Vx8rMrlrBK9tFB5RkLS1jqKpdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا پیام دریافتی پست قبل درست بود:
خبرگزاری مهر بامداد جمعه ۱۸ اردیبهشت‌ماه به نقل از محمد رادمهر، معاون استاندار و فرماندار ویژه میناب، گزارش داد یک پایگاه دریابانی در این شهرستان هدف حمله قرار گرفته است.
به گفته رادمهر، این حمله ساعت ۰۰:۱۰ توسط اسرائیل و آمریکا انجام شده است.
همزمان فاکس‌نیوز گزارش داد آمریکا حملاتی را به جزیره قشم و بندرعباس در جنوب ایران انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75309" target="_blank">📅 01:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هرمزگان
پیام‌های دریافتی:
وحید بندر صدای انفجار اومد الان
الان ساعت دوازده شب صدای دو انفجار دیگه در بندرعباس شنیده شد
همین الان بندرعباس صدای انفجار اومد
سلام بندرعباس ۰۰:۰۰ یک صدا اومد
۰۰:۰۲ بامداد جمعه ۱۸ اردیبهشت صدای تک انفجار این دفعه از فاصله بسیار دورتر ظاهرا از مناطقی در نزدیکی جزیره لارک یا هرمز بود.
خودم همچنان در همین محدوده نزدیک اسکله بهمن، محله دوحه و چابهار هستم
👈
پاسگاه بندرکرگان در میناب استان هرمزگان مورد اصابت موشک آمریکایی قرار گرفت.
پاسگاه دریایی است. می‌گفتند پهپاد از همین نقطه بلند شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75308" target="_blank">📅 00:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/95a8a7b0ee.mp4?token=TFr7qW8-bX94ehfKj4r-bBtDzsM2XYeegNyUeHNdnu5_t0pGHFi29j-ihLAzDVVKgONUaLPc8JkesJTNC00_gHJP8uZBsK-7GRhX7LNQUv3FWBb2QZpmNKNy-5I8fh128bHzUbccPLMAkkFCd6J8it5ZajufTAzzH9CGv0anhAKLP-SvgASHu4NbRSzWWoShZzWeFOMv9ru8WypGwHRG2Dkl_J5yWAjMqmhIg47CdEYsEWx9--Bt3hEQaQ0rdrUHX3_wtCK3Y1C_2qhxIfKROQ_DWUpIqd0-D-zIUpfDD4NFHp01P3xnfLyA6f-oAAktXHhzyq8_qMju8ZMt1Tc1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/95a8a7b0ee.mp4?token=TFr7qW8-bX94ehfKj4r-bBtDzsM2XYeegNyUeHNdnu5_t0pGHFi29j-ihLAzDVVKgONUaLPc8JkesJTNC00_gHJP8uZBsK-7GRhX7LNQUv3FWBb2QZpmNKNy-5I8fh128bHzUbccPLMAkkFCd6J8it5ZajufTAzzH9CGv0anhAKLP-SvgASHu4NbRSzWWoShZzWeFOMv9ru8WypGwHRG2Dkl_J5yWAjMqmhIg47CdEYsEWx9--Bt3hEQaQ0rdrUHX3_wtCK3Y1C_2qhxIfKROQ_DWUpIqd0-D-zIUpfDD4NFHp01P3xnfLyA6f-oAAktXHhzyq8_qMju8ZMt1Tc1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و پیام‌های دریافتی:
وحید جان سلام ۲۳:۵۳ غرب تهران فعالیت پدافند
غرب تهران نمی‌فهمم صدای پدافنده یا انفجار ۱۱:۵۳
سلام غرب تهران چنتا صدای انفجار و پدافند ۲۳:۵۲
صدا ها مرتب و پشت سر هم نیست
وحید من غرب تهرانم، ازادی. ساعت ۱۱:۵۳ صدای انفجار دور میاد
چندتا پشت هم
ساعت ۲۳:۵۰ امشب ۱۷ اردیبهشت صدای انفجار یا پدافند محدوده غرب تهران.
۱۱:۵۳ تهران شهرک اکباتان ۴ افنجار دور شنیده شد
مطمعنم صدا پدافند نبود انفجار دور بود
۱۱:۵۴ صدای پدافند به صدای انفجار ها اضافه شد شهرک اکباتان
ساعت 23:53، ممتد صدهای پدافند و مشابه انفجار باغ فیض غرب تهران
صدای چندین انفجار الان سمت شهران ۲۳:۵۴
سلام ساعت ۲۳:۵۲ دقیقه صدای چندین وحشتناک انفجار  سمت غرب تهران شهران
پدافند غرب تهران داره میزنه
از غرب، جنت اباد نمی دونم پدافندها فعال شده یا داره می زنه
غرب تهران بلوار فردوس ساعت ۱۱:۵۴
صداهای متعدد میاد
شبیه پدافند
صدای انفجار و پدافند
جنت آباد ساعت 1154 شب
امشب
سلام وحید همین الان دوتا صدای انفجار اومد سمت بلوار  فردوس غرب صدای پندافند هم میاد به شدت
چند تا صدای انفجار و پدافند میاد سمت غرب
منطقه ۵ ساعت ۱۱:۵۲ دقیقه
بلوار فردوس شرق، غرب تهران از ساعت ۲۳:۵۰ دقیقه صداهای ممتد شبیه فعالیت پدافند میاد، و یا حتی شلیک یه چیزی فراتر از پدافند
سلام محدوده چیتگر فعالیت شدید پدافند ساعت ۲۳:۵۴
وحید ۱۱:۴۵ شب، جنت‌اباد مرکزی تهران، یه عالمه صدا که فک میکنم پدافند بودن
وحید جان همین الان غرب تهران (سمت میدون آزادی) صدای پدافند شدید میاد
سمت شهرک نفت هم همینطور...
صدای پدافند از دور در مرکز تهران ساعت ۲۳:۵۵ شنیده میشه
صدای ضد هوایی بوضوح در جنت‌آباد شنیده میشه
سلام وحید همین الان کلی صدای پدافند تو تهرانسر اومد ساعت ۲۳:۵۰
وحید سلام شهرک غرب ۲۳ و ۵۳ پدافند فعال شد.
سلام وحید جان ۲۳:۵۵ منطقه ۱۰ صدای بم عجیبی اومد چند بار پشت سر هم. شک دارم چی بود.
وحید جان ساعت ۱۱:۵۴ جنت آباد مرکزی بنظر صدای پدافند میاد چندتا پشت سر هم
سلام وحید جان ما تهران، جنت آبادیم، پدافند فعال شده، انفجار نیست
۱۱:۵۷ دو مرتبه صدای انفجار و پدافند شدید غرب تهران شهرک اکباتان
ساعت ۱۱:۵۷ باز صدای پدافند شدید و صدای انفجار. جنگ اینجوری صدای پدافند نبود.
غرب تهران، ساعت 23:57 تشخیص نمی‌دم صدای انفجاره یا پدافند، اما صدا مهیبه
وحید جان ساعت ۱۱:۵۷ جنت آباد مرکزی بنظر صدای پدافند میاد چندتا پشت سر هم
صدای ممتد پدافند غرب تهران ۲۳:۵۷ همچنان ادامه داره
۲۳:۵۷ سمت مرزداران غرب تهران صدای پیدافند میاد همینجوری
ساعت ۱۱:۵۷ باز صدای پدافند شدید و صدای انفجار.
غرب تهران، ساعت 23:57 تشخیص نمی‌دم صدای انفجاره یا پدافند، اما صدا مهیبه
11:57 صدای انفجار میاد بعید میدونم پدافند باشه جنت آباد مرکزی
صداها وحشتناکه ۱۱:۵۷غرب تهران جنت اباد مثل زمان جنگ
الان صدای خیلی شدید تر میاد ۲۳:۵۷
جردن ۲۳:۵۵ صدای پدافند میاد
سلام وحید همین الان دوتا صدای انفجار اومد سمت بلوار  فردوس غرب صدای پندافند هم میاد به شدت
ساعت ۱۱:۵۷ بازم صدای انفجار و پدافند، انفجار هم هست  ولی انفجارهای بزرگی نیستن
باز هم به صدا انفجار میاد، به نظر پدافند باشه
ساعت ۲۳:۵۸، شهران
ساعت ۱۱:۵۷، همچنان جنت‌اباد مرکزی تهران، همچنان صدای پشت سر هم به احتمال زیاد پدافند
سلام ۸ انفجار مجدد ساعت ۲۳:۵۷ غرب تهران شهران
غرب تهران سیمون بولیوار دوباره صدای احتمالا پدافند ۲۳:۵۷
سلام وحید جان ۱۱:۵۶ صدای پدافند شدید محدوده دریاچه و میدان المپیک میاد
همین لحظه ۱۱:۵۸ همچنان ضد هوایی شدید
سلام سمت شهرآرا صدای پدافند میاد پشت هم
ما مرزداران هستیم
از دوردست خیلی صدای انفجار میاد
ساعت ۲۳:۵۶
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/75307" target="_blank">📅 23:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/872058ebf9.mp4?token=s_ZvgeqwTYjOxrWPRUtzNoSXF2gis9qR3FJBuBwhhJ2w2XWWKymRHW0gjEOusyEk9UCo_-TjVGlgY5G739KuM-vjgQw8sjnUjXXbOdX_7g-KRW_cs5AkGX4jMA-bLaHtFWaI4av_k-AkOGiNR6Z14Usp404wq3masYyFOCA95vrrnWBKrHZo7cGgqRrRqG-QpPUpnomNYXT3KbWLBdZocUOkfCkvFXSVHkHeWP23HEf6t0WPCkJc7xyupaCWwc3LAxG1HoABdJ-s1jkGUcWcWQIwy-kA6NI9QVKvAvKYi8S7qClBl5g1-e6ZZg7vYROQU0T2hOxeNwZ-KYxOMFQ-SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/872058ebf9.mp4?token=s_ZvgeqwTYjOxrWPRUtzNoSXF2gis9qR3FJBuBwhhJ2w2XWWKymRHW0gjEOusyEk9UCo_-TjVGlgY5G739KuM-vjgQw8sjnUjXXbOdX_7g-KRW_cs5AkGX4jMA-bLaHtFWaI4av_k-AkOGiNR6Z14Usp404wq3masYyFOCA95vrrnWBKrHZo7cGgqRrRqG-QpPUpnomNYXT3KbWLBdZocUOkfCkvFXSVHkHeWP23HEf6t0WPCkJc7xyupaCWwc3LAxG1HoABdJ-s1jkGUcWcWQIwy-kA6NI9QVKvAvKYi8S7qClBl5g1-e6ZZg7vYROQU0T2hOxeNwZ-KYxOMFQ-SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما به نقل از یک مقام آگاه نظامی گزارش داد «به دنبال تعرض ارتش آمریکا به یک نفت‌کش ایرانی، یگان‌های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی جمهوری اسلامی قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75306" target="_blank">📅 23:38 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZnqKWaPEp8jqTmtFLrKsdkUyNpCrxOZNnlSL027SqinfCwp7npiv8-tTfotchzQjTqP0vDMeA-xtXVL00Wfc8d5Ryrrt8peI6E4_ja_MoQVZgtQiNa5bD2trjRJT6zfBrxd0eCTi5_Keu-ESLRMZYiyFLOvOB6LK7hTlho5z-efGprwyqOmS6j1X4NcsbPuzO2wS93s9wO3S3tYqop3gOod14D2i4XSBcJ4FoTGYWSwSyu7KXlzC6vl1EkLVxF6S-PBR1Ng3szFK2zxEYV5nAdRCi59r9lCo78OQnFdFmlXoF-m2Zaly651h_Fqi-bGfq-1xWrgtex6PlNmMoy4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، در خبری اختصاصی اعلام کرد که صداهای انفجار که پنجشنبه‌شب، ۱۷ اردیبهشت در حوالی بندرعباس شنیده شد، مربوط به «تبادل آتش» میان نیروهای مسلح جمهوری اسلامی و ایالات متحده بوده است.
به گفته فارس، در جریان این تبادل آتش، بخش‌هایی از اسکله بهمن در جزیره قشم هدف قرار گرفته است.
@
VahidOOnLine
آپدیت: منابع غیررسمی حکومتی و سپاهی میگن امارات اسکله بهمن رو هدف گرفته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75305" target="_blank">📅 22:53 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p5TH0GMwvEyZwVZqhRHsm-jiHqn3d5Mk5wF79UjB-1BZ4yoWoRwg594p6l2NcJcV04L9k1HEl4_5ilGY-n_HgDPGzESaudNFnf7EX5lh6MytM4bvVIdlF8kReFxuBItDt4FiMdkL5fFGwrtEpduQSV6bAupYqa1-soZkwW0jyLMAJEm7myLpscvZyK6vw3pBcr6oHwh3GpUbz2rBNE19rqoE6zltP3f2kKO0cvNfbLU3JTMyJ2FH7FjXDPAOJKrTIa2JBPfe1i60tEjYVGeBLKiLY01hAztqBO0t18xhBGOVHWzPpKuEtndrXoUj_Mb5ppdMI6sJMrsrtPRsdd_tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
تماس بسیار خوبی با رئیس کمیسیون اروپا، اورزولا فون در لاین، داشتم. درباره موضوعات زیادی گفت‌وگو کردیم؛ از جمله اینکه
کاملاً در این موضوع متحد هستیم که ایران هرگز نباید سلاح هسته‌ای داشته باشد.
توافق داشتیم که رژیمی که مردم خودش را می‌کشد، نمی‌تواند کنترل بمبی را در دست داشته باشد که قادر است میلیون‌ها نفر را بکشد.
من با صبر و حوصله منتظر بوده‌ام که اتحادیه اروپا به سهم خود از توافق تاریخی تجاری‌ای که در ترنبریِ اسکاتلند بر سر آن توافق کردیم، عمل کند؛ بزرگ‌ترین توافق تجاری تاریخ! وعده داده شد که اتحادیه اروپا سهم خود از این توافق را اجرا کند و طبق توافق، تعرفه‌های خود را به صفر برساند!
من موافقت کردم که تا دویست‌وپنجاهمین سالروز تولد کشورمان به او فرصت بدهم؛ وگرنه، متأسفانه، تعرفه‌های آن‌ها فوراً به سطوح بسیار بالاتری افزایش خواهد یافت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75304" target="_blank">📅 22:46 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDyk4FwEcfqm5_WQWP541mVIvCXHod7Pf7eUYA8KC0Yp4dkImUKp03i5Vu8cljSy_2iMgpQtemuMnl8_rSrN5-aZ6yEIGIX2CcXy0tE-DtxW_d0E5Qrf8sF_VMtYhBw074vVHgGnb4U5l9Pn9dptc7FCtvQGrsBls2mb_tTwnKFyf6b_swsuYE-RiS5hkkpTWHyL4DLwAVWxM2QDo9ajYWAtaCr27RcZwXxRVg8uanrjRADrjxUtXmVURJVPwbJ-lm82e8eibB3K388M6TwbUFcPeX8OYvU8ZMKILymoLfqXMS1n-8rDX07teQmGa3s2fJ3YqfchUE_TwUG6oIb-Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با تلاش‌های ایالات متحده و بحرین برای پیشبرد قطعنامه‌ای در شورای امنیت درباره بازگشایی تنگه هرمز و آزادی کشتیرانی، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، این قطعنامه را «یک‌سویه و تحریک‌آمیز» و روایت‌های مندرج در آن را «گزینشی و جانبدارانه» خواند.
عراقچی در نامه‌ای به دبیرکل سازمان ملل و رهبران کشورهای عضو، محدودیت‌های کنونی در تنگه هرمز را ناشی از «جنگ تجاوزکارانه، غیرموجه و غیرقانونی» آمریکا و اسرائیل علیه جمهوری اسلامی خواند و به جامعه جهانی هشدار داد که نباید اجازه دهند شورای امنیت به گفته او مورد «سوءاستفاده متجاوزان» قرار گیرد.
او در این نامه تاکید می‌کند که تردد در تنگه هرمز تنها در صورت «توقف دائمی جنگ و رفع محاصره و تحریم‌های غیرقانونی» علیه جمهوری اسلامی به حالت «عادی» بازخواهد گشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75303" target="_blank">📅 22:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هرمزگان
پیام‌های دریافتی با جزئیات تایید نشده از ساعت ۹:۲۵:
درود
ما غرب جزیره قشمیم. از ساعت ۹:۲۵ به فاصله چند دقیقه ۴ بار صدای انفجار اومد و موجش شیشه ها رو لرزوند.
ساعت ۹:۴۸ یه صدای انفجار و ۱۰:۰۲ صدای دو انفجار دیگه. صدای جنگنده نیومده ولی
صدای چندین انفجار پیاپی قشم همین الان
بندرعباس همین الان صدای انفجار اومد مثل صدای برخورد بمب بود
بندرعباس صدای انفجار اومد حدود ساعت ۹ و نیم شب
سلام، ساعت 21:30  بندر خمیر استان هرمزگان انفجارهای پیاپی و شدید
سلام وحید جان قشم صدای پنج انفجار
سلام وحید جان بندر کنگ ساعت 21:50 صدای چندین لانچ موشک شنیده شد
ساعت 22:01 شهر قشم در محدوده [محله‌های] دوحه و چابهار صدای دو انفجار پشت هم شنیده شد
ظاهرا انفجار ها از سمت اسکله بهمن شهر قشم بوده
خودم حاضر بودم و شنیدم
صدا بسیار بلند بود و موج انفجار هم حس شد
امروز ۱۷ اردیبهشت ۱۴۰۵
سلام داداش
قشم دقیقا الان ساعت ۱۰
دوتا موشک زدن اسکله دوحه
خیلی وحشتناک بود کل آسمون قرمز شد
همین الان بندرعباس صدای دوتا انفجار پشت سر هم از سمت دریا اومد  نمیدونم لانچ بود یا برخورد ولی هم صدا داشت هم پنجره ها لرزید
درود بر آقا وحید گل
بندرعباس ، الان ساعت ده و دو دقیقه شب صدای دو انفجار پشت سر هم آمد
ساعات پایانی روز پنجشنبه
سلام آقا وحید. قشم  همین چند دقیقه پیش  ساعت ۱۰ شب دوتا صدای انفجار اومد همراه یا نور روی دریا. چیزی رو توی دریا زدن
همین الان ۲۲:۰۴ دقیقه
صدای سه تا انفجار سمت دریا میاد
سمت سیریک استان هزمزگان
یه موشک هم بلند  شد
با فاصله نورش دیده میشد
به سمت دریا رفت
الان سمت میناب دوبار صدای انفجار اومد
با شهر فاصله داره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75302" target="_blank">📅 22:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a9X3Isv7yUKVNVKAjgXWN1jhGl4s8E-gyEOeac6Jltv0eLJ3Pru6fldMgKvXDTaOlu2jPXOxocfSoMClONHJsuq7BDcGnUs12NAtV-ESPNdNa5X-HG4NzmWhb9--P0f2-sShCrWCHZXIrtGu0YxvAw9_KbQsdjsD2kvbAKi6E7kiBPg2pmJ52sJcAu8sQMGiBk_mlA6xKnhvmwZGQM27J8iBYM2GWRmLwirrCrgKsq2RKqk57zm8pe9Fr_LatcfdWfW7YIkx3RV8W13cvZ8lpku0miMzdAMhfomEwUiI-vtlJaqjXIUGlv0zlYLhAJHYvSiLWsAy0lx2CjpjnGhCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">mahshids979
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75301" target="_blank">📅 18:34 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j9KNBj0ricAcQlC1edTKFvYsfuyfvVIANyk28x9NyTV93GvMRgnlqX_w5ViMp5zXXl4IXQtaK1sdiEcjySwm2QuR5_jiEsRwxyU4fwdKiFJwvaKdP6GCVMR48zDHO4KZNSGjvF29iPHu6D7E-9zEV90bsiihC_TrQ7esFVnrPGz5x6Abhkm3X044Pl6Cq3eHrxGMhP2ISiAdTPv-tCguQXoPBv6UR0xXOXOq0D4D3ODRZoE3ps4ZWq3mfqTe6KcAEnr_JUW9rVn2GFwPsauaTY6sRC7oH3RkZZOyicIs1z0RYTx7S0P0d1-pGskMeQ_NsiNTvbevsyvqnNtJJMMnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SheykhSharzin
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75300" target="_blank">📅 18:31 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RFrTMLnSMuZZtXegf8UihWHIg--_ltypHjxdb9ZGfeAQoefBuKcNeWF_GQtpVG7vRlUTDKFo0rzBePbqWjeNWBLxA_p41jb4c_FPJFKAEAXWe-PSl7Z4tkO06Rf-8UR_0ZYGtvK6QF1qQII_kl1LrksI36Jpg6BN5Tb6Xmy6vw2wxWFSoRxt-gKPp7ofQUnkVVRq0rwvNrnluyFQTt29fH2sYWF3FO7tPM3QZ4DyIJR_kuHAQ9r9xFlUYwRZGhMGExqN8o0LBlpBeByyRKc5yaCF5V_x8wWb1Uo0i1zjcxf_ji1_D49T76fcTrB21SebCnQSXguLAZQw0nq6ca0CQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">t_golpoone
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75299" target="_blank">📅 18:29 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISDoLWjUn9izq3-dJ4xrMgCEFCT8h69FbXgmCOD4KO83RORP54na9EvV3pWu1XsyX_4ytSFgPheflCWbBXgc6ho_OsiKbiDgEwgpTo52IZkVFu00bh77rXV-gktrXRh527Y9Vsa0qqvv938RJG9wUujVmRr8pW7dPhsWmXai6YMjEHtw_mUvAcV7sn_z3Qx0_cGF_vbMqK48uxWx-w6ruwuNpNSo33kjQDWZ-tyw8qaAIMiDeNMOcyn2KTk4mhy49Bb_GXvVKEtIW3Dn8n_4wlK2lMqdkxuw5g6YVN9XI5fRksKR9FjjUKoetEcKWVMc9nz33bJjm7fT-jxf-m1_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس، در شبکه ایکس نوشت: «با وجود سابقه بدعهدی آمریکا و به ویژه حضور اصحاب توافق ذلت بار برجام به‌همراه قالیباف در مذاکرات، هیچ امیدی به مذاکره و توافق مطلوب برای ایران وجود ندارد.»
او افزود: «لازم است قالیباف اصحاب توافق خسارت‌بار برجام را از تیم مذاکره‌کننده کاملا حذف نماید.»
نبویان در پست دیگری نیز نوشت که برخی از «مسئولین و سیاسیون ترسو و غیرهمسو با ملت مقاوم ایران»، به دنبال آمارسازی‌های غلط برای تسلیم هستند، اگر اصلاح نکنند، اسامی‌شان افشا خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75298" target="_blank">📅 18:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tsQAhjBnPYK1O-FFlW8h0hUOsjCzGJRVtQzaOMiLun9PU-wQH1cD-VzLtRIsp6i52aHRWfXgcQjsY6-nPFG8B9IfU0cdKcsSKCOKbKMUh5LKxh8BhbNZdFGRsoPkw-XMcl-ETb1emBkDSpyLId4AIALDAF0O2RoiFfuK5J_XQs7_i0MVkygMcElt439yO6MEU1UwlhbopnQzYeuzQmJKlA1L4qS5BNg4l0quN0q0Z-jD8OjuilHbWFfAmUw3Q_TyInXR8-EWpC85tWFjkHnPfL32Ohh7QRlIYeuDXM6xxSCfHlVRKmLE83drHV8qj5v3JWBEjNNkAWvKfTKJn-lGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژان-نوئل بارو، وزیر خارجه فرانسه اعلام کرد تا زمانی که تنگه هرمز توسط نیروهای جمهوری اسلامی مسدود باشد، هیچ تحریمی علیه تهران لغو نخواهد شد.
او در گفت‌وگو با شبکه «آر‌ال‌تی» گفت: «ما خودمان تحریم‌های مهمی علیه ایران اعمال کرده‌ایم. اما تا زمانی که تنگه هرمز مسدود باشد، لغو هیچ‌گونه تحریمی قابل تصور نیست.»
بارو افزود: «این تنگه نمی‌تواند بسته شود، مشمول عوارض گردد یا به‌عنوان ابزار فشار و باج‌گیری استفاده شود.»
او همچنین تأکید کرد فرانسه نباید دوباره در موقعیتی قرار بگیرد که مجبور شود هزینه جنگ‌هایی را بپردازد که خود آغاز نکرده است.
به گفته او، اروپا باید وابستگی خود به نفت، هیدروکربن‌ها و فناوری‌های دیجیتال را کاهش دهد تا کمتر درگیر بحران‌ها و درگیری‌هایی شود که مستقیماً طرف آن نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/75297" target="_blank">📅 18:17 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRlLTCc4AKp4oBsK0NvvMVQgBixAojnBRu8EJCzF35w_M0dgpLbSo7zYvguMwd-N0hWYAvnJLFbLSqscCnzsotxWJCStmkX50RusMwgHxB2TYptgBQLQtHHS8Vc86setYYsvpaadxjopkoIWHLFqpzIeUx9qouJrzS3vkRu5E4tIHaBjuZscAev4GZRGEK1ZDSMuzg0YtiYKO6kgWsoDQZ_vkPsXap_65NzQJLhTRqExUaJ42kHpJ5wNcjq9_oxbm9RQnO3ZfNm3LGkzRA9s5K1ZP5Gkmr_-FmC1tPKdikmZQw2ggt5CR05-Usmu6h8m0CbSXx736iKuptQXbryKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، از ملاقات اخیر خود با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، خبر داد و گفت با گفت‌وگوی مفصلی داشته است.
مسعود پزشکیان که روز پنجشنبه ۱۷ اردیبهشت در نشستی در وزارت صمت سخن می‌گفت، به ملاقات دو ساعت و نیمه با مجتبی خامنه‌ای اشاره کرد اما در مورد موضوع و جزئیات ملاقات و اظهارات مطرح‌شده چیزی نگفت و صرفاً او را به‌دلیل «صمیمی و متواضع بودن»، «الگویی برای نظام مدیریتی و اداری» کشور توصیف کرد.
پس از کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، در روز نخست جنگ با آمریکا و اسرائیل، مجلس خبرگان رهبری پسرش مجتبی را به‌عنوان رهبر جدید معرفی کرد. با این حال از آن زمان هیچ تصویر، صوت یا دستخطی از او منتشر نشده و رسانه‌های ایران فقط شماری پیام مکتوب منسوب به او را منتشر کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75296" target="_blank">📅 18:14 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqeBaUQl-GQ49QcnJFA1OHEBezC_DQ18dCLw1WtbqIiMb8V2O-IeJfHE1agArSUNgok59lKNvUokKcSiq4p1BsEW-AjkkGu05Dsjc23EkOusG104-rFk3nfEHpTsNkOtmc5yR0plxVTM1ZnkM_uy8x5EwrAiyK_6i6BoKqn-1k5UTkUZrar66isYUzWhTEtdKjlpyYadal_m3vvhw6JDB_4jLoB8AuiZjHUWKMQlGZ6irrsA_rYnNQ-0abaKuFoNr6r17E8iG1IEaiBVbfj3xuDqg5Ycvx6K7Sz6DOJgENEaGksJPr_J_7k5AeDZvAu17LYtrvcmMKqazSR0hACeOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال در گزارشی درباره توافق آمریکا با رژیم ایران نوشت که ایالات متحده می‌خواهد همه ذخایر اورانیوم غنی‌شده از ایران خارج شود. به این معنی که هم ذخایر اورانیوم با غنای ۶۰ درصد و هم ۲۰ درصد و هر میزان اورانیوم غنی‌شده دیگری که ایران در اختیار دارد نیز باید تحویل دهد. این در حالی است که مفامات تهران همچنان می‌گویند موضوع خروج ذخایر اورانیوم غنی‌شده از ایران، از دستور کار خارج شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75295" target="_blank">📅 18:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75294">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUVjiUhZnB1WjJAXz-r2RaAkNqwc9t3nUi3ZTXelt2rv3MBPelKg8isyZERr4g9VeB06qGvn4IgtoGPa6B0whYvDpGUL5mArh7Ht0AiotXbSzPDY--_s_VCSN-FqTIDoGVJpgK_JG0ETUOiFVnRvdOIKtNgOVOiA1VbE-aeST5zQzuy1Vqbh-wMm21M7H11prI9Qm1W5rj174ze_k7kXrCc_KB8g8G5wGOPIuUIJtobZFzlyB9x1HtejUrn6s0aQLY5VziEr-T1oJl--2mLKEXlX1Zpdyr368g1YSE-b-plDDxiVYxgJyTD2rVwSAc3kQLbbf4vpvYQ3sBS8Cz-VXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از دو مقام آمریکایی گزارش داد چرخش ناگهانی ترامپ از «پروژه آزادی» تنگه هرمز پس از آن رخ داد که متحدان خلیج فارس از این تصمیم غافلگیر شدند و عربستان سعودی امکان استفاده ارتش آمریکا از پایگاه‌ها و حریم هوایی خود جهت اجرای این عملیات را به حالت تعلیق درآورد.
به گفته این مقام‌ها، ترامپ بعدازظهر یکشنبه با اعلام «پروژه آزادی» در شبکه‌های اجتماعی، متحدان خلیج فارس را غافلگیر کرد و این اقدام موجب نارضایتی رهبران عربستان سعودی شد. در واکنش، عربستان سعودی به آمریکا اطلاع داد که اجازه نخواهد داد ارتش آمریکا از پایگاه هوایی پرنس سلطان در جنوب‌شرقی ریاض پرواز کند یا برای پشتیبانی از این تلاش از حریم هوایی عربستان عبور کند.
این دو مقام آمریکایی گفتند تماس تلفنی میان ترامپ و محمد بن سلمان، ولیعهد عربستان سعودی، این اختلاف را حل نکرد و رییس‌جمهوری آمریکا ناچار شد «پروژه آزادی» را متوقف کند تا دسترسی ارتش آمریکا به این حریم هوایی حیاتی را احیا کند.
دیگر متحدان نزدیک خلیج فارس نیز غافلگیر شدند؛ رییس‌جمهوری آمریکا پس از آغاز این اقدام با رهبران قطر گفت‌وگو کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75294" target="_blank">📅 18:11 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dSJayqUfCo2c0wB78KlNxUM-0rESj24ViB1RsmjRxz67M-LO2HNJ2LLXbNrZVd5x78kopOR696NNL7gfqOnm0n7911fOqx5odzDMBfsUvQ25w87Ly1jkzL6-VcA-JlAwTLZtnDYqEp2lbdjau2WYHNL9877gwDE8fuMu0DIBH_v7NG-SMYVJ1qhqQv5F6sybGjlVI39gHJqyyI57yUKUA3h4-rEyZsxBzErb1u94lvxr81vbs3hzRY7C_lEqBKhnIb_jBeAjRfK4ppQhJRMNURPw1dyos-377hf2T8rhbSPYtGWq4Mx1-saMNAYeNp3FL7nQYFLNKimbhA9cGN2C3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ چهارشنبه شب در
تروث‌سوشال
تصویری منتشر کرد که مدت‌زمان جنگ‌های مختلف در آن نشان داده شده و از مخاطبانش خواست آن را ببینند.
او بارها به کسانی که مدعی‌شده‌اند عملیات نظامی علیه جمهوری اسلامی «طولانی» شده، پاسخ داده‌است آن را با جنگ‌های پیشین آمریکا مقایسه کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75293" target="_blank">📅 06:28 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">غرب تهران
پیام‌های دریافتی:
صدای انفجار 2:38 دقیقه جنت اباد تهران
شهران صدای انفجار وحشتناک اومد ساعت  ۲:۴۰
یک صدای انفجار خیلی بلند سمت شهرزیبا (غرب تهران) ، شبیه موشک نبود بیشتر انگار یه چیزی ترکید
پونک تهران
دو صدای انفجار شنیدیم
همین چند دقیقه پیش غرب تهران یه صدای خیلی بلندی از انفجار اومد
سلام وحید جان دادش غرب تهران ۲:۳۸ اینا صدای یک تک انفجار  اما سنگین اومد ولی هیچ جا نگفته کس دیگه!
چند دقیقه اخیر راجع به صدای انفجار توی جنت اباد پیامی دریافت نکردید؟
صدا شبیه انفجار پهپاد بود. موج نداشت اما شدید بود.
[دریافت کرده بودم ولی چون تعدادشون کم بود صبر کرده بودم تا پیام‌‌های بیشتری برسه. چون پیام‌هایی که بعد از انتشار پست ارسال بشن اعتبار زیادی نخواهند داشت.]
سلام منزل ما جنت آباد مرکزی هست محدوده خیابان بصارتی
حدود ساعت ۲.۴۰ صدای انفجار شنیدم اما دقیق نمی دونم چی بود
شهران صدای انفجار بلندی اومد ولی یه دونه انفجار بیشتر نبود.
ما سمت باغ‌فیض هستیم؛ ساعت ۲:۴۰ صدای انفجار اومد، آنچنان نزدیک نبود اما بلند بود؛ بنظر نمیرسید شبیه به صدای برخورد باشه؛
اما همین یکم پیش هم حدود ساعت ۳:۰۵ صداهایی شبیه به موتور اما تیزتر و ممتد اومد که حدود ۳،۴ دقیقه طول کشید؛ فکرمیکنم شاید پهباد بوده باشه؛ با صدای جگنده که در زمان جنگ میومد متفاوت بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75292" target="_blank">📅 02:53 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75290">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/551509ade1.mp4?token=Dqa0HuALoHFBEFWsW09Hpk0BEPwPS3PSjh1jZiZme6acaUL_X2SHyi3PaQbx1-_64EytAOB_GVLEN6-XrD4ijKseiPyZHzKafJZgW4RCN_OAq9veHcPCjGKX4HPsO6Hcet-dVwd79Dt9WNPDfhllJH6MA_4CeVodBLrQw0f4-IHsZIVc0kemEX9L8XQfAH_L6hxPYSQghhtIVnP5QKw_Ye5azDqZNumG0K6qVlPGcCsBEGQyo3L4T-8qj-DZ9Q-WbIzTgtxOxMo1kT2nsuf_Hd8pgBSnRp4GOvy8F6M8KBTyrlXyW30kzeYrYz-xJ72IqzmpSuxYWdb6cnj0D41EPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/551509ade1.mp4?token=Dqa0HuALoHFBEFWsW09Hpk0BEPwPS3PSjh1jZiZme6acaUL_X2SHyi3PaQbx1-_64EytAOB_GVLEN6-XrD4ijKseiPyZHzKafJZgW4RCN_OAq9veHcPCjGKX4HPsO6Hcet-dVwd79Dt9WNPDfhllJH6MA_4CeVodBLrQw0f4-IHsZIVc0kemEX9L8XQfAH_L6hxPYSQghhtIVnP5QKw_Ye5azDqZNumG0K6qVlPGcCsBEGQyo3L4T-8qj-DZ9Q-WbIzTgtxOxMo1kT2nsuf_Hd8pgBSnRp4GOvy8F6M8KBTyrlXyW30kzeYrYz-xJ72IqzmpSuxYWdb6cnj0D41EPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، شامگاه چهارشنبه گفت که پس از «گفت‌وگوهای بسیار خوب» در ۲۴ ساعت گذشته، دستیابی به توافقی با ایران برای پایان دادن به جنگ «بسیار محتمل» است.
@
VahidHeadline
ترامپ با اشاره به وضعیت نظامی کنونی گفت که توان دفاعی ایران به‌شدت کاهش یافته و نیروهای هوایی و دریایی این کشور عملا از کار افتاده‌اند. او با بیان اینکه «ما پیروز شده‌ایم»، اعلام کرد که جمهوری اسلامی اکنون تمایل زیادی برای دستیابی به توافق دارد.
رئیس‌جمهوری آمریکا شرط اصلی هرگونه توافق را دست نیافتن ایران به سلاح هسته‌ای و خروج ذخایر اورانیوم غنی‌شده از این کشور عنوان کرد.
@
VahidOOnLine
او تاکید کرد که ایران «نمی‌تواند و نخواهد توانست» به سلاح هسته‌ای دست یابد و این موضوع را بخشی از تفاهمات مطرح‌شده دانست، هرچند جزئیات بیشتری ارائه نکرد.
آکسیوس پیش‌تر گزارش داده بود که در یکی از بندهای پیشنهاد آمریکا، توقف غنی‌سازی در مقابل رفع تدریجی تحریم‌ها مطرح شده است.
این در حالی است که پیش‌تر مقامات جمهوری اسلامی هرگونه مذاکره درباره توقف غنی‌سازی را رد کرده بودند و بر ادامه این برنامه در چارچوب سیاست‌های اعلامی تاکید داشتند.
@
VahidOOnLine
ترامپ گفت: «ما در وضعیت خوبی هستیم و حالا باید آنچه را می‌خواهیم به دست بیاوریم؛ اگر این اتفاق نیفتد، باید یک گام بزرگ‌تر برداریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75290" target="_blank">📅 00:06 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75289">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBH0Pf8bLhzVfVPjIZsn_JLVi_m0lUhV4vpAchaJtBnGUxgbLA8bfAqyK0ZXHn_AYo_-pOVcKXnXyYL3SNl2rU_iGiDz_WibBRsUtc54AOones7OfCfI0HEMuO0A-tXdTfIKnunga6wxM5owD5y_wFPSUjbIQJXyMGIg9TVeVn5ZweQXBjymqqk40wyQIc-Rhi3Wh5ILGBEXXL1x2o93mPfLSQ4k0bDixToKUqqv4VFkHRfNsNBcpENmNLHWwxC73-JaEBOdlJh6U6iU1l42OKesPEllsfnJu-c5Rsim8-m5_HabeNkCAtYhqRtNAjHFmqVmDpIS5OM5AQ56uGqcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل عصر روز چهارشنبه در حمله هوایی به منطقه ضاحیه، حومه جنوبی بیروت، که تحت نفوذ حزب‌الله است، فرمانده یگان نخبه «رضوان» این گروه را هدف قرار داد.
این نخستین حمله به حومه بیروت از زمان آتش‌بسی بود که روز ۲۷ فروردین بین اسرائیل و حزب‌الله برقرار شد، هرچند درگیری‌ها در جنوب لبنان متوقف نشده است.
در بیانیه مشترک بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، آمده است: «عوامل رضوان به رهبری این فرمانده مسئول شلیک به مناطق مسکونی اسرائیل و آسیب رساندن به نیروهای ارتش اسرائیل بودند.»
خبرگزاری فرانسه به نقل از یک منبع نزدیک به حزب‌الله اعلام کرد که «مالک بلّوط، فرمانده عملیات در یگان رضوان» در این حمله کشته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75289" target="_blank">📅 22:38 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HzDM2DunmjuPJNN_tMgIsn8MOZpALUIghvhV5owuuWQ47mgMqFPokP_LYd1Nf91RERz-8YLIyEhjrwnNae0QgQ_T44Jd7h1LFvwMTx5rMTFi1-_lu-m24j6WhzGmrEAzhXJamrP64mlLDHLpLTv-WACh1EC6HaMbkpoQrRAiaC-UzzAaisFsKW1A3tw_DrFGKoOpsrtDD_jJKcCXckZO35UxA7IB64WxDCddcn28AjLhPPUl1ObhqPLvDN35NW7d_2Z4iSEqEW2pH6sy-33GREsZfoF7UUMYBCojI1pYSWZEghohotwnJfUj9S9CWW1LZ_P_77VuVtDOXKSt9OKS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p8c2Jp8gLD6vB8C9GZ5rVQza3fcmaR2br-42HK15Kuq2ZluIoISG6qAQfQI3u94p2Cjn3UyaLAR8O39WxbA8FDRjDmBbj9ZKu6a852jXANjvKW6nxK9i-nD2jI2C3SUeSxgUb5fSYIihoCxo51jgR6wmNMcXntQk9AW5ifAJiXxt-zgVXbtIfcXqgNkfp4e4E4PUwHRLr6rVNBpTtkw0XXJXlmHTN_ZpHUq9q8-lNXI-fUJbcUse5XILRA3qcF_aM_-J0cDmQq6knSkGID-FcFI7JZGbMxsHBObuZ3Ttm7V7FBGuVLs4CoVZytLyp_NHhW3Ku-uvA_UjdnqSjeVLmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل در آغاز جلسه کابینه خود امروز(چهارشنبه) به موضوع ایران و همکاری با آمریکا در این زمینه اشاره کرده است.
آقای نتانیاهو درباره ارتباط با ایالات متحده گفته است: «هماهنگی کاملی بین ما وجود دارد؛ هیچ غافلگیری وجود ندارد. ما اهداف مشترکی داریم و مهمترین هدف، خارج کردن تمام مواد غنی‌شده از ایران و برچیدن قابلیت‌های غنی‌سازی ایران است.»
نخست وزیر اسرائیل گفته است:«رئیس جمهور ترامپ معتقد است که می‌تواند به هر طریقی به این هدف دست یابد. با این حال، ما برای هر سناریویی آماده هستیم و این دستورالعملی است که من به ارتش اسرائیل و سازمان‌های امنیتی‌مان داده‌ام. اسرائیل از همیشه قوی‌تر است؛ ایران و نیروهای نیابتی آن از همیشه ضعیف‌تر هستند.»
او گفته است: «ما در حال حفظ ارتباط مداوم با دوستانمان در ایالات متحده هستیم. من تقریبا هر روز با رئیس جمهور ترامپ صحبت می‌کنم. مردم من و مردم او روزانه، از جمله امروز، با هم صحبت می‌کنند. و من امشب دوباره با رئیس جمهور ترامپ صحبت خواهم کرد.»
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز چهارشنبه و همزمان با تلاش‌ها برای دستیابی به توافق پایان جنگ در خاورمیانه، بار دیگر تأکید کرد که آمریکا اورانیوم غنی‌شده ایران را خواهد گرفت.
او هنگام ترک یک رویداد در کاخ سفید به خبرنگاران گفت: «ما آن را خواهیم گرفت.»
آقای ترامپ در جریان سخنرانی خود در کاخ سفید همچنین گفت «ما در ایران خیلی خوب عمل می‌کنیم. همه‌چیز خیلی روان پیش می‌رود و خواهیم دید چه اتفاقی می‌افتد. آن‌ها می‌خواهند به توافق برسند، می‌خواهند مذاکره کنند.»
رئیس‌جمهور آمریکا درباره وضعیت مذاکرات توضیح داد: «ما با افرادی سر و کار داریم که بسیار خواهان رسیدن به توافق هستند و خواهیم دید آیا می‌توانند توافقی ارائه دهند که برای ما رضایت‌بخش باشد یا نه.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75287" target="_blank">📅 21:39 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAvECH1QNlzy9A8twWnG2Vx6xVxWT0CIFS6PmSTanIrqfRwONJ3T1LOgIPWphliTkroRblyleGuwWCYePZkKHBj_fX2uPdhCCJajW5WmJrtak8lIPGDslUfSju072tn93f74Y231-n7n2kS53qpWtShwmTunUTyFmf4v0Woh4EtKHF8-nNumSCX9oEKS7hr7tUvl1RAabBa-sPMfzOJl-EoWPBVBwh4UCft1wWbVnlYnAJoAbz_LdDzyjv2o8k1WWPCEyzekwIYyNG4i9w4u-Pgo3wQZ0xCl7V3Mt_77qnFLgbj3bsRPE7D04aWInWDaDCHMa5d7m-3UTCWLgdbXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000pa2
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75286" target="_blank">📅 21:29 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr95QVvObYbmJWZnjRNfPkB5vnjHTiyqao9k1rglLRB7IwRQaYtWKpm7YMq4_CoITntjlYhTuSW2Cn2asi9I27jXxzCZI0tCIy15yhASpzcVm9Hylg6YXxXWmCki9v_3yodhWtI6b9k58Q7VIqVYxJZE0hpsvuqujmOV54CqcAK3WDDJ-D3E1DrxlHw_6rUyPQSFSmFLg1XGA0f02POTO9yqdTxh9-wswhaZ3-Hmcz7hVGoiZgnHOAsVXFnXMUqPuDUG90SkwQMjP-J1sPBXQvD7xYAa2qIeR77zwi9jyMYsPakiD_xH4P8KaE_asCGXKBZoHB1HdRRY10fhpmCsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام در بیانیه‌ای اعلام کرده نیروهای آمریکایی در دریای عمان «در چارچوب اجرای محاصره»، یک نفتکش خالی با پرچم ایران را که در حال حرکت به سمت یکی از بنادر ایران بود، از کار انداختند.
سنتکام اعلام کرد پیش از این اقدام، چندین هشدار به این نفتکش داده شده، اما خدمه از دستورات تبعیت نکرده‌اند.
در ادامه آمده است که نیروهای آمریکایی با شلیک چند گلوله از توپ ۲۰ میلی‌متری یک جنگنده اف/ای-۱۸ سوپر هورنت سکان نفتکش را از کار انداختند.
@
VahidOOnLine
فکر کنم ترامپ قانون گذاشته از یه حدی بیشتر نباید خرج محاصره دریایی بشه. نفتکش قبلی را با توپ ناوشکن متوقف کردند این یکی را با تیربار اف-۱۸ زدند به سکانش.
_KhodaBiamorz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75285" target="_blank">📅 21:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75283">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LXg_mpyH89ThUTTkO0qrfiufOg8SAmgLUXo1U2E-CyeLUU5gcmMcq6rr18dBTex9Pp_k2Q7xGlQPb2jqtHQ8AbjqdGRSn7uokjxWDnkdNEPKfkShQWp76jrJ5f3Sn_0rdLa1aeDggdKtu-_UqEZr_Zz2Y727szCkL6qMdsTpnTAjr3Zl-wnvEhQ-aOMKS2O5Enq780uwxe4dRYj3aVDvS5wtL39zes8syKPGcuwr4SXc7Z9wWYlAzdGQZhWx-9lnHF4DiAiAY46aJxH_aCbwHRetOu3qy6EJ1rQDLRgCTlsGdailk6Ag1KC6GuzsfZMbkzk6i9400ciOzvRf8TPHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EkyYDBzyGjB619WyapMvcUvFeZq-JVHtZaVin_HUXZImnljH-1ss7wmDMszOjtjOlrqYN_cwt9tMMLd5XDac0KvetsjxWNloLOut0rFY2iuyY4MhEcawV4ECOwrDZHeej6rQynDZ_SRU1UNttIjSQUmlOEBCmSsFGTp-w47XXx78O2weqMEjVLWjXtdg0E2VTBzbsPjA-DKfUN8rThJQK7C_jEa5ZxayariB-EG4LcAouHTylXJY8JYFYquqqGtI2VUXzcJd6lB9MhdhlfuJWKXIgoP2VbhHOSLRhheK_yGiNGFfivZpxanYOI9zqiwT_wpCQwzZqTWT-1-yML0CLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خواهر مصطفی حیدری‌تبار:
Akitakii731
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75283" target="_blank">📅 21:08 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75282">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/154603e865.mp4?token=ZK4IZgCQONNClKfEZbbtmVNf-3X74WM9NgBdMYGJurBKZKPu5CLS0v9mOCocU38mLNuQRXEh_l6ToXFgKm0cwi1WLy4R1uiq1VqRxnmeN5JfeGQmbdss-00OzWe40Smd66dKX8jld4GFN3I-XiS6H33JBoWc3OKe-slNMrgAQz9h24lN6u8kx6LllJw7EKSkXezNnvtK42ShroQV-t2Dg-8IEFY6lYP5jlLg0FiTqVaVt1_5sH3JygyEgyWkAvTWFeaR86a_lOIEwlFGegpXWvs64YQb5qc-QP-_ZGrfEg9NW8dwZAWlxEj_etCmA7WC7Kn6V29PSqAoOxMmx72DOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/154603e865.mp4?token=ZK4IZgCQONNClKfEZbbtmVNf-3X74WM9NgBdMYGJurBKZKPu5CLS0v9mOCocU38mLNuQRXEh_l6ToXFgKm0cwi1WLy4R1uiq1VqRxnmeN5JfeGQmbdss-00OzWe40Smd66dKX8jld4GFN3I-XiS6H33JBoWc3OKe-slNMrgAQz9h24lN6u8kx6LllJw7EKSkXezNnvtK42ShroQV-t2Dg-8IEFY6lYP5jlLg0FiTqVaVt1_5sH3JygyEgyWkAvTWFeaR86a_lOIEwlFGegpXWvs64YQb5qc-QP-_ZGrfEg9NW8dwZAWlxEj_etCmA7WC7Kn6V29PSqAoOxMmx72DOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'یکشنبه ۱۰ اسفند'
ویدیوی دریافتی با شرح: 'انفجار حمله به سپاه کهنز
#شهریار
از دوربین ماشین. تازه تونستم به اینترنت وصل بشم.'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/75282" target="_blank">📅 20:45 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75277">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u4CeCxkO2DrcQRXzycwN8zKs5OtK5uxFL_JzgK7opJBeZAmllv__XxMSFMX_oxtre9O0Gmk4sy404VZW9PNwavhvfjb98ZayskdsvdEyxX3ax02wghYZKBSCMAoKpyaGGRWeOmBW6goAwTkLuphAmqAhW_m7zS11DYy4ZkM9MQv3ScyNz3ck4K0KK9dAqmfYiAiC1pg0cQ25e1XVs7m8qLdbO2ZBLW2QOGhI2RrYlaCaa8W89-vdAsXNEREBj0I5vW_TlspbeDVrh8vO00m5Xeyak1xEr5TdKHQAzNWGf_DoXGhKhOGnq7uqAVQuD1DkcioLNp54wpj6Xm6aXj7sJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kh0G0cLwuze-dpo621CW44x3gDX1DvmT1fIHThYKFiwmXuozorMr-6Agr7YYxkeLUP8enlOugLuu3NrLU-baqW32IjgX4TiTi6ElE52N6l3W8foTx-vfowkOppjXkaHcmxUtgC3zyCSKHp5bcLUjM3cxd2rL-znvtH7ibJwMc55YgbXi6lpeIeZGfNIJev6R836vutuSbGKaR-aMzFXvz1cwRGGhg-RCQ8qj_LNHjo7gOBPMRvVdtD6drxf1RmgPDmtI-UaVnI17C1WiJDzmXAcVk5dIARioe2TQgJ-muQrnLwxvMip-QaBEcw3XL9lWpRYQjEwms8hoMepZInWrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tGh_OIKBUe0vz0t2hkrcvb6HcM1cnZU4cQf5Cke0a0PnTGmJQ9gOqRNoAWMNLaxWpdSzma9yUUEUeyAY7W0bqgmqJjxr5w5IBjejBLzvXdbetGE_OjgzCmCFq_PSMOHMuUZ7sRCKDcTENLLU7zJLLePwl4iB7YS4HdHSkb2XCPTkytQg1FHtHK7w4JsMgCia2TjBXTt06xNZUfwkfcCzLJqR-Nhwmwu6cALvZUHzDWQw46CwhHyxOy1NGl68j7jVb64FO-jGzgKXcIBJD1Bw_1I2AIzKbQAHrQtJlrtwwMfuaq-v2kZ4HtXhd_qAHFcMbcHxJeCnOAhvvYYDDNIutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d7-tdwqQkpkuAOn6aRPoQF9ImRgcgbaij5pRNgI4TnN87GA02Ph8EOJdiHOGdmYGci1cYWvIxctorbiuZIVnhDWwe0pI11-109JFQ8bqQVU6pLR1AbYxLiO0E98gc5jRcMalL1IqKJAzYZTer6lJpZxwAIXCONsriFcKxgqX1_jhRZ6O05EnTGn8t0nLIR8G3aBHzMk69RA3YKHrp-CLe2y56xP0_RFPy7MuO1yngfiKwk9qs6tVYHrOEFl18pTbVgc26is1GayQr4UwU2d15Kto9p88DD-eeXK6S6T07kM9VsTC8qkLUOKzyc2GqG68nWXVQeZsBjqJ_V0B-i0kkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94d4331fb0.mp4?token=esPKa6hjQ638rpzg8dhDwuHRmcx2e-SK1PhsZ0LNbmclB8nSeGT837l_mWBRUqvAfIjaYt17T63dU0guKFibnzpeRKrd26imCduIKokQtoXmgUHqH6E9W0TDqeHqbKlalIGZgDiE_AVAyU8iQR4G9MYoQHzwtZpKHcd3SmtJo7RosAsxV4MMU-bfmWcT0XcHAX94VsZCI4k38rj9-0WmobY7dsh9CHSCk4HVABuaYJ5J9MzQqpOK46j0H5mT_AZsnQAnlRpvEVptrb7n3WjP6S-4rGrtbZmOxfAB5q4D2z_R8-m06DKltY9j0ICpufqHvo9c2X5cTGWjpzL2E7WClw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94d4331fb0.mp4?token=esPKa6hjQ638rpzg8dhDwuHRmcx2e-SK1PhsZ0LNbmclB8nSeGT837l_mWBRUqvAfIjaYt17T63dU0guKFibnzpeRKrd26imCduIKokQtoXmgUHqH6E9W0TDqeHqbKlalIGZgDiE_AVAyU8iQR4G9MYoQHzwtZpKHcd3SmtJo7RosAsxV4MMU-bfmWcT0XcHAX94VsZCI4k38rj9-0WmobY7dsh9CHSCk4HVABuaYJ5J9MzQqpOK46j0H5mT_AZsnQAnlRpvEVptrb7n3WjP6S-4rGrtbZmOxfAB5q4D2z_R8-m06DKltY9j0ICpufqHvo9c2X5cTGWjpzL2E7WClw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس‌ مجلس شورای اسلامی و مذاکره‌کننده ارشد ایران در مذاکرات با آمریکا، می‌گوید واشینگتن با اجرای محاصره دریایی و فشار اقتصادی قصد دارد «ما را تسلیم کند» و درباره تأثیر این فشارها بر وضعیت جامعه ابراز نگرانی کرد.
او در یک فایل صوتی که رسانه‌های ایران روز چهارشنبه منتشر کردند، گفت: «ما احتمال حمله نظامی و مخصوصاً حملات تروریستی را کم نمی‌دانیم اما آن بخشی از طراحی دشمن که به جامعه باز می‌گردد، ضعیف‌کردن ایران از درون است.»
وزیر خزانه‌داری آمریکا روز یکشنبه اعلام کرد که دولت دونالد ترامپ همزمان با جنگ، «محاصره اقتصادی» علیه ایران را ترتیب داده و در حال «خفه کردن» حکومت ایران است. او مدعی شد که جمهوری اسلامی حتی قادر نیست حقوق سربازان خود را بپردازد.
قالیباف در فایل صوتی خود جنگ اخیر را «یکی از بزرگ‌ترین جنگ‌های معاصر ایران» خواند و با طرح این ادعا که پیروزی در این جنگ، «ایران را به یک بازیگر مؤثر در نظام بین‌المللی تبدیل می‌کند» افزود که رسیدن به چنین هدفی «با سختی‌هایی همراه است.»
او با اذعان به «فشارهای اقتصادی» به مردم ایران خواستار «انجام وظیفه» همه مسئولان اجرایی کشور شد و افزود مردم هم باید «اقداماتی» انجام دهند.
رئیس مجلس شورای اسلامی در ادامه «صرفه‌جویی» را مهم‌ترین خواسته از مردم خواند و همچنین خطاب به نیروهای «بسیج» گفت که «واسطه میان مردم و مسئولان دولتی و خیران» شوند.
ساعتی پیش از قالیباف، مسعود پزشکیان، رئیس‌جمهور ایران، نیز در پیامی در شبکه ایکس نوشت که «از افزایش قیمت‌ها مطلع هستم» و در توضیح دلیل آن گفت: «بخشی از آن مربوط به تغییر قیمت‌های مواد اولیه یا مشکلات مرتبط با جنگ ظالمانه‌ای است که مردم می‌دانند.»
این مواضع در حالی اتخاذ شده که قیمت ارز در روزهای اخیر به ارقام بی‌سابقه‌ای رسیده و گزارش‌های رسانه‌های ایران حاکی از افزایش شدید قیمت‌ها و گرانی شدید کالاها در کشور است.
@
VahidHeadline
محمدباقر قالیباف، رییس مجلس، گفت احتمال حمله نظامی کم نیست، اما «دشمن» به فشار اقتصادی امید بسته و بر اساس گزارش‌های «غلط» تصمیم‌گیری کرده است.
او افزود ملت ایران حتی در شرایط فشار اقتصادی، به خاطر دین و اعتقادات خود مشکلات را تحمل می‌کنند.
قالیباف گفت باید از ظرفیت ایرانیان خارج از کشور برای شکست «دشمن» استفاده شود و نخبگان نیز منتظر مراجعه مسئولان نمانند و راه‌حل‌ها و پیشنهادهای خود را ارائه دهند.
او همچنین خواستار راه‌اندازی پویش «ایران همدل» مانند دوران کرونا شد.
@
VahidOOnLine
فایل صوتی ۱۰ دقیقه‌ای و متن منتشرشده در منابع حکومتی رو
گذاشتم اینجا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75277" target="_blank">📅 20:17 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
