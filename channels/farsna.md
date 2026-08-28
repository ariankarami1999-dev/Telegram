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
<img src="https://cdn4.telesco.pe/file/s51JG8acMDCVFVweWWqwjmmFFAw5iurd_refp3UKstrFfqmoVC6ylhgMPwzRPuDUieVOqsQFB2vKvHTcGg-zqmEUWvSRrNwoDnvSpiecVKMIEUGWQ0j8YQW8XIEu4BTjRVl0F-HFA6R58sQhsix6me39t4c5TLibqRyaNJjJeKqRpBIZjFpg3Z-io7WOSP2mot2Azzd24TCUH9HxspjD1LA_u1LXZoZRirXv3YkgQJnO-eVfrDylYjRpgsRsGLhRUnDC91jm2bHVwlDlA3M9O1BPdXuYzDhFi1whllbDCDXHVgsSOrcPIYFJ3MVAkPncjqkjjsmUNDXt5BcuJ6uLbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-458584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIIm3lYcaFpFnx295k4UJld2nfVpERisrGTPjrb5FcJQtU6VJSlB7QLLxwgExxU0433bVeDJSnwIbl5Gkn-qrL0F6NBSGeR5LGK10kBc51yssgv6udQTf3fNB9r48WE306p1DlKnImpquNqnrB6kMoROPVGYU-8QYsLaJsqpguC-V4D3gdtwu8D7e6Q-dzd0tdaBtmmXkKofM3Z_Vd3CjlTm5TKnU1cWOI97qirC4GOYVhcRIricdELzL_y-oA3sxfoOQOI1pg4PG3sQVe3iGu5KAcWnTTDrZLLwA6dpptzrxDWodP_wqDwW--vjSHVss1E8FNUpBu3JvX_7WzqIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی برای اولین بار دست به تیغ جراحی شد
🔹
برای اولین‌بار در جهان، یک بیمار ۴۸ ساله بریتانیایی به نام «ریس هیبرت» تحت جراحی تومور مغزی قرار گرفت که در آن هوش مصنوعی به‌صورت زنده تصاویر جراحی را تحلیل می‌کرد و به جراحان در شناسایی رگ‌ها و اعصاب حساس مرتبط با بینایی کمک می‌کرد.
🔹
این فناوری که در دانشگاه کالج لندن توسعه یافته، به پزشکان اجازه داد هنگام برداشتن تومور از بخش‌های پرخطر فاصله بگیرند؛ زیرا در این ناحیه حتی یک خطای یک‌میلی‌متری می‌تواند به نابینایی، سکته مغزی یا مرگ منجر شود.
🔹
تومور هیبرت در صورت درمان نشدن می‌توانست او را نابینا کند، اما عمل با موفقیت انجام شد و او پس از بیدار شدن از جراحی گفت که دیدش به‌طور چشمگیری بهتر شده است. این فناوری در آینده می‌تواند حرکت ابزارهای جراحی و تماس آن‌ها با بافت را نیز به‌صورت لحظه‌ای ردیابی و به جراحان بازخورد ارائه کند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 342 · <a href="https://t.me/farsna/458584" target="_blank">📅 05:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عاقبت تلخ کشتی متخلف کویتی در هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس تأیید کرد نفتکش «السلام ۲» متعلق به کویت، شامگاه پریشب در ساعت ۲۱:۵۰ به وقت جهانی مورد اصابت قرار گرفته است.
🔹
پیش از این، عصر همان روز نفتکش یونانی «مترو ونیزی» هدف حمله قرار گرفته بود.
🔸
توالی این حوادث طی روزهای اخیر، نگرانی‌ها دربارۀ افزایش خطرات امنیتی برای تردد نفتکش‌ها و حمل‌ونقل دریایی در منطقه را تشدید کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/farsna/458583" target="_blank">📅 04:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458582">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOv69Lt1jRin_kS0h88Qjd4tLno3uAwce5-6KdgOKYZUd4Xj4aDgzjTjhSvTVgxP2D1K9X2hFde4ArdS5wguPMw_O7Ve4p93zMy_Li8U41A2-I40kxtqkEGFI4PbsdWPBm7ws-yKzaSmOeTyI5iGfU2EtAWwFvCADQ46LI1bDDJYcTzBRQswqp2M42TV7PaCDVcDwrT0v_hvADXchLiXD1MgdFis7VaYPqRgy1WGUu3A0wcmkXzt0bBASKvgcm4pEJXpgnPDQeSKBZ1K_SZcK6Ke8IVtFK6NCnaebIGfYS3Cpe31YHYjh_RKKmTFTK6UJRQxyHrZpLk3XiMlWOUgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیت گذر نفت از تنگۀ هرمز در یک هفتۀ گذشته
🔹
درحالی‌که منابع آمریکایی مدعی عبور ۱۰ میلیون بشکۀ نفت از تنگۀ هرمز هستند، داده‌های تانکرترکرز عبور ۴.۱ میلیون بشکه را تایید کردند. رقمی که معادل ۲۰ درصد شرایط عادی تردد از تنگۀ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farsna/458582" target="_blank">📅 03:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458581">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5ZuwfbHAmWhGOm5JCmgHX8Uqfxw1UpYanFndBXSQzBA--p2GjLo2pc2g9udC0XmtKRii2jH0VTSn2i6FvTwaXldqAiVkxipNoVTzWoMWTMUuLmhqZBnxdLtenaWMJe34duaMhKgHjiBKhPQeKpOM-baEtSBnUYp1P6naPmiRbGSGMncG-hlx85C_4L-Oj1GXXJLUfUclct_gN9k3VlPTvGU044r-IkS7xZpNaO1ycrRvzIrHJEAyUzE5nZGfEA7lbw16RKiQRinbr_vaAU-l0XMy1tpQp_j3RDxU71kprreopfRYA9sXncCdTb1AF6DH6UYZkcs4-U4NjFFjrmH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوی ضعف نظامی آمریکا به مشام پوتین رسید
🔹
گزارش‌های اطلاعاتی جدید آمریکا نشان می‌دهد کرملین تحت ریاست ولادیمیر پوتین بر این باور است که جنگ شش‌ماهۀ آمریکا با ایران باعث تضعیف ایالات متحده شده است.
🔹
واشنگتن‌پست می‌گوید مقام‌های آمریکایی نگرانند روسیه بخواهد این وضعیت را فرصتی برای تشدید اقدامات خود علیه آمریکا و متحدانش در اروپا ببیند.
🔹
این ارزیابی محرمانه اندکی پیش از سفر غیرعلنی رئیس سازمان اطلاعات مرکزی آمریکا به مسکو مطرح شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/458581" target="_blank">📅 03:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458580">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ونزوئلا خروج از اوپک را بررسی می‌کند
🔹
بلومبرگ گزارش داد که ونزوئلا به‌طور جدی در حال بررسی خروج از اوپک، سازمان کشورهای صادرکننده نفت، است؛ سازمانی که بیش از ۶۰ سال پیش در تأسیس آن نقش داشت.
🔹
موضوع خروج ونزوئلا در جریان گفت‌وگوها با مقام‌های آمریکایی مطرح شده، هرچند هنوز تصمیم نهایی در این‌باره گرفته نشده است.
🔹
خروج ونزوئلا می‌تواند پرسش‌های بیشتری دربارۀ انسجام اوپک و توانایی این سازمان برای تأثیرگذاری بر قیمت جهانی نفت ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/458580" target="_blank">📅 02:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458579">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هشدار یمن به شرکت‌های بیمۀ دریایی: فریب عربستان را نخورید
🔹
وزارت خارجۀ یمن: شرکت‌های بیمۀ دریایی به اطمینان بخشی‌های عربستان سعودی دلخوش نکنند. این اطمینان‌بخشی‌ها خطرهای موجود در ناوبری دریایی را از بین نخواهد برد.
🔸
همچنین سخنگوی دولت یمن اعلام کرد نیروهای مسلح این کشور با جلوگیری از عبور ۴۸ کشتی از دریای سرخ و دریای عرب، و هدف قرار دادن هشت کشتی نفتی دیگر موفق شده‌اند محاصرۀ دریایی کاملی علیه عربستان اعمال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/458579" target="_blank">📅 02:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458578">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6COADb-q-Vm3rpdoHxgrMY0z7-0FewMjP9yf_I3cXBBl1tAm-L8LW2bxRc9BWP6x8HINUfBqpLLf21LWwBCyM2nvoG3kBpBDaYYuMX3IKVndW7rU799PCSF_jCknkeAfiBc6CW4LYHGMhQMIejeDkYrwtNJMF3TvZWpvr7z49hgE6t5spZe55WA4cYnkK1Ih1vrnOsJDl6sbttd_bwJQ_N0XDOtpC26H1JexAA2JSiJK7csIgHG7oh3_Jlv7Pd5I9uYOfv4urJ9ghXKj9gNxnvMCg8wADy1bzkL1Q2u2yduZetQdRsfPl_o5XNKgunTRPHOXEIJ63Q2NWkjzWXgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه اسرائیل برای مهندسی هوش مصنوعی
🔹
روزنامه گاردین گزارش داد رژیم اسرائیل اقدام به راه‌اندازی یک اندیشکده جعلی کرده تا بر پاسخ‌های و حتی داده‌های آموزشی چت‌بات‌های هوش مصنوعی اثر بگذارد.
🔹
این وب‌سایت که «مؤسسه هانوفر برای سیاست عمومی» نام دارد، طی تنها ۹ روز ۱۲۴ گزارش با بیش از ۵۶۰ هزار کلمه منتشر کرده  است.
🔹
گزارش تحقیقی گاردین نشان می‌دهد که این وب‌سایت تلاش کرده است روایت‌های مورد نظر اسرائیل درباره جنگ غزه و مناقشه اسرائیل و فلسطین را در اختیار چت‌بات‌های هوش مصنوعی قرار دهد.
🔹
گاردین می‌گوید موسسه هانوفر ظاهراً در هیچ حوزه قضایی به‌عنوان یک شخصیت حقوقی ثبت نشده، آدرس فیزیکی مشخصی ندارد، کارکنان آن معرفی نشده‌اند و هیچ‌یک از گزارش‌هایش نیز نام نویسنده ندارد.
🔹
حتی در بخش شرایط استفاده از سایت آمده است که این شرایط تابع قوانین «کشوری است که مؤسسه در آن تأسیس شده»، اما نام آن کشور مشخص نشده است.
🔹
گاردین می‌نویسد این سایت بخشی از یک کارزار بسیار گسترده‌تر است که
ده‌ها میلیون دلار از سوی اسرائیل
برای آن هزینه شده است.
🔹
هدف این کارزار، به گفته گاردین، این است که محتوایی تولید و در اینترنت منتشر شود که احتمال دیده‌شدن و استناد به آن توسط چت‌بات‌های هوش مصنوعی افزایش یابد و در نهایت، این چت‌بات‌ها هنگام پاسخ به پرسش‌های کاربران، استدلال‌ها و روایت‌های مورد نظر اسرائیل را ارائه کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/458578" target="_blank">📅 01:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458577">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48134c9b6.mp4?token=sVien0PHwvK5wR3tS1Eqo7vitIubYF_jh0UT-OoFC5zl-_cjgxg036Ykqhifj7Thc8v9z48k030KdG-WdwvTSrwz6eXj0KH7xIfj4X90lg0Z7tmlUEobNyH4SzmilHe1UudcX4o2ud7EivfqtvhERHSpIHiLvwZc0zQ3kmMoeeawHNdcHQ3fho5-ymNYMcAVD0cNvgTIG_6mbqIYSNFo8DOr1wVOp8lcMpJmGOyI_4bjg7cxUO-X-bmkv3EZFSuoAgXooroAPMfVNuDvJgoCarLVVlTpUZuewEPV8Al1y1qUM-XKO0IEFHbB-QF88VXm4SF-A-I88HvSM_0HR4GQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48134c9b6.mp4?token=sVien0PHwvK5wR3tS1Eqo7vitIubYF_jh0UT-OoFC5zl-_cjgxg036Ykqhifj7Thc8v9z48k030KdG-WdwvTSrwz6eXj0KH7xIfj4X90lg0Z7tmlUEobNyH4SzmilHe1UudcX4o2ud7EivfqtvhERHSpIHiLvwZc0zQ3kmMoeeawHNdcHQ3fho5-ymNYMcAVD0cNvgTIG_6mbqIYSNFo8DOr1wVOp8lcMpJmGOyI_4bjg7cxUO-X-bmkv3EZFSuoAgXooroAPMfVNuDvJgoCarLVVlTpUZuewEPV8Al1y1qUM-XKO0IEFHbB-QF88VXm4SF-A-I88HvSM_0HR4GQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهید حاج قاسم سلیمانی و رهبر شهید انقلاب از سیلی خداوند به صدام و مستکبران دنیا در اوج غرور
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/458577" target="_blank">📅 01:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458576">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNstVbJOA0LqMU1VsiEo9WxXWEpw-t5drDUaLVgXy-HwT9A8kU2gh3g77l31zylLBbQTox2tjsq1KTLXBG-OdYZwAvRPAxPrkguNGVnGtldyNQQxb2uW0Ca5ia5TUKIzXY1DM6OuWkr1-GnHoX6d3TlBkjIeMYpjV0npRmwrGhzfvJJ6ry-s0IRtwn8jiKzoVbzVRkE6Q01M8sSTuqQ-GdaOW7Oa7OnsUJoqkN25UOtiHoZUtLT-bkR0qhEOwf916u1firHZMtVQ9oC7aCTQEaTlA7rDvevbl9MZaghv9WZwujxYziwVmp1BnYILe7nxdfmkFgZDqgqABjc7LwKPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزی: هیچ شناوری بدون اذن نیروهای مسلح از تنگۀ هرمز عبور نمی‌کند
🔹
رئیس کمیسیون امنیت ملی مجلس: رفت‌وآمدها در تنگۀ هرمز با نظارت و کنترل جدی نیروهای مسلح انجام می‌شود.
🔹
درحال‌حاضر هیچ شناوری از تنگۀ هرمز، چه در ورود و چه در خروج بدون اذن و اجازۀ نیروهای مسلح به‌ویژه نیروی دریایی سپاه پاسداران نمی‌تواند عبور کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/458576" target="_blank">📅 00:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458575">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حملۀ اسرائیل به حومۀ دمشق
🔹
برخی منابع از حملۀ رژیم صهیونیستی به مناطقی در غرب حومۀ دمشق گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/458575" target="_blank">📅 00:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458574">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkBC5ACiAjh8rf27uzQzKFeMBuSK7QNISQHhsBJq6ot15ddTBv_eH805iRXpDJ9rsemEQVlV7Znef7448ezBKqqwhubrqhjrYrOSrFkrEWPoG2oASlL95Cu6VpCwnat69fbKYY76nXXXfDVd-z0dtYOpIVEKp4uSYZkiMUys35rZZBeMz24Q1_I1Q6vT1WMvgMHVoHrmfGVKy1pnYjHc_QQ0P9jAUHG-dqyg2e0zN9h7-7Wi9In2KO9NFApiC_mgDC2y4EW8IGkORnY_hyFWSxto9ULtE_9Av8lptmz5NrFCwBy5U3L2wloereS0pV-gYJtMxNuACbEl3AyTm5i_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا علی کریمی علیه رضا پهلوی و سلطنت‌طلبان شمشیر کشید؟
🔹
ماجرای درگیری علی کریمی و رضا پهلوی در شرایطی علنی شده که بخشی از حامیان جریان سلطنت‌طلب، پس از ماه‌ها امید بستن به تغییر شرایط سیاسی ایران، اکنون با واقعیتی متفاوت از آنچه در فضای مجازی برای خود ساخته بودند، مواجه شده‌اند.
🔹
امید چوپانکاره، عضو شورای مرکزی جبهه شریان، می‌گوید که این افراد متوجه شدند که آنچه برای آینده ایران تصور کرده بودند، در نهایت چیزی جز «رویا و خیال‌بافی» نبوده است و مردم ایران تحت تأثیر چنین پروژه‌هایی قرار نگرفته‌اند.
🔹
حسینی استاد دانشگاه هم معتقد است که تصور برخی جریان‌ها این بود که حمله نظامی، می‌تواند جمهوری اسلامی را در موقعیتی قرار دهد که امکان ادامه حیات سیاسی نداشته باشد و در چنین شرایطی، رضا پهلوی خلأ قدرت را پر می کند.
🔹
بخشی، استاد دانشگاه هم می‌گوید که تحولات اخیر برای این افراد روشن کرده که جمهوری اسلامی از پشتوانه‌های اجتماعی و اعتقادی برخوردار است و همین مسئله آنان را با واقعیتی متفاوت از تصویری که در فضای رسانه‌ای ساخته بودند، مواجه کرده است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/458574" target="_blank">📅 23:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458573">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌ سرلشکر رضایی: ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند.
🔹
ما با جدیت کامل اوضاع را رصد می‌کنیم و زیر نظر داریم. اسرائیل مجبور خواهد شد از مناطق اشغال‌شده در لبنان عقب‌نشینی کند. @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/458573" target="_blank">📅 23:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458572">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: ما نتانیاهو را روانهٔ جهنم می‌کنیم
🔹
سرلشکر رضایی در مصاحبه با المنار: ایران بنیامین نتانیاهو را به جهنم خواهد فرستاد. ما ثابت خواهیم کرد اشتباهات بزرگ نتانیاهو باعث شده پایان موجودیت رژیم صهیونیستی نزدیک شود. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/458572" target="_blank">📅 22:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458571">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNd0KimZsotjlJVx-Zn3fMrDG0B9of0FN5sP7p4_6E9WITb3fMdK-kNOKYlKLanvS326GRYmlMBgIJPJNMtcwiJ9QLhs6gwNlpyegFURmNOVqlultK4XUopFjSYHfcJ0f-hwRsz9aDMhi5MzYnIzpQc782Z5mfjomfHgeB_ozQrhMvJZ7_EzdQnOEDcR_FcZQ1IvMb9nbDHKtDlmB0mSHdPlLg6_wzYvm4tTJbNnQz0MmiQdkART5P94Ot1P0uaFsT9Tc7728An5nqlYkrutirlBjGLgnNmRUiaAoZ7NcxP1yPepL3nFQNphF05_Hxvp4sgdWwF8zUK2k1_RyvwRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: ما نتانیاهو را روانهٔ جهنم می‌کنیم
🔹
سرلشکر رضایی در مصاحبه با المنار: ایران بنیامین نتانیاهو را به جهنم خواهد فرستاد. ما ثابت خواهیم کرد اشتباهات بزرگ نتانیاهو باعث شده پایان موجودیت رژیم صهیونیستی نزدیک شود.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/458571" target="_blank">📅 22:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458570">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXrZqj_IU0X0exI2z56DnaN0PZ-RotTu_vMIcUIFjKAgUr3qrOBAFotSK_OWUWxKS_6mZFCyuf5HH_k7ZxnaMMre-hWSr8hk_wevSXz5FpXw3Dbu6LdRi56dchK3NSXJYX-0Xn4jvHCeHmhNFSaSMUuqTlWsszaGoKof_a-_KzyQqt3oIa4v13D9x4sIuD13SSNaL2FJYsNAMp2lM6GWrBfZd-_eYlFBEgeZULNjSE1dfUizV08br2yjWHhJrFCTdE7lKIbrxeDPtSCW5Bv-_JABiQLA9aTOuAWUIVUnqJG8Jp17X-yUp-std2gDUiQW_eaLsFFU94gYCzyWyVYSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت‌ژورنال: ترامپ تمایلی به بازگشت به تفاهم‌نامه با ایران ندارد
🔹
روزنامه وال‌استریت‌ژورنال گزارش داده مقامات ارشد آمریکایی به میانجی‌گران بین‌المللی اعلام کرده‌اند که دولت دونالد ترامپ هیچ علاقه‌ای به بازگشت به مفاد توافقنامه اولیه‌ای که ژوئن گذشته با ایران امضا کرده بود، ندارد.
🔹
به نوشته این روزنامه این موضع‌گیری، تلاش‌های گسترده این هفته برای ازسرگیری روند دیپلماتیک را با پیچیدگی جدی مواجه ساخته است.
🔹
به گفته منابع آگاه، ترامپ اکنون بر سیاست فشار حداکثری اقتصادی بر تهران متمرکز شده و حاضر است منتظر بماند تا ببیند آیا این راهبرد نتیجه‌بخش خواهد بود یا خیر.
🔸
منابع مطلع گفته‌اند ترامپ به‌ویژه دیگر تمایلی به احیای تفاهم‌نامه ژوئن ندارد؛ توافقی که در داخل آمریکا به‌شدت مورد انتقاد قرار گرفته و آن را در برابر ایران «نرم» تلقی کرده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458570" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458569">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt3ij96AMdURvMftV6khhjcouuryk0jtz0iqxQO7xFr2l9Bux997Y4CAIKyx4MZMNISWy90_-4YoOOX4Tl4xHCK5qgCZRRXb2y1nmLZnaDYMsjp6dMohYtFllMj6pRh8PhoyquQ0-k4-El9QpW9kV4L2UOiGA2OFT08wXAiGNl_2mYjUKoNL-dG22dPIGutkjC8kRzmxZTB-62Ryg35ZLdofwXvW5MrwSS3l1O36dzBISievN4dZIc0BfWaEGb5xHOC8jQ1f27kbnIfco9c6SNFTWznlTesdvF9Q-OLrMr9qD3tuq9GmKVOegYLqdyIlU3TEQ-tKTTE1hM8QyZIz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فولاد شادگان تا مدرسه نابینایان شیراز؛ روایت ۱۴ گام بلند «امید امروز» در گوشه‌وکنار ایران
🔸
۴ شهریور ۱۴۰۵ را در تقویم امیدهای ملی ثبت کنید؛ روزی که خبرهای خوش از ۹ استان کشور، یکصدا فریاد زدند که چرخ تولید، آبادانی و عدالت، حتی در سخت‌ترین روزهای تحریم،…</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/458569" target="_blank">📅 22:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458568">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۷.pdf</div>
  <div class="tg-doc-extra">3.6 MB</div>
</div>
<a href="https://t.me/farsna/458568" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۶.pdf</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/458568" target="_blank">📅 22:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458567">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db7c1b068c.mp4?token=FYX8y9EXEd4WQjdK29dZTBzCZ2aiTfcx9L1N82-xQcUdC0x4BuSD4s12YuCZvAzfPTA0ajWSsxIt5u7wZ_4rGC8VmAokvLwEpjrqmAC1d7Re7iB1UC1T-aVoFqH5jEhv0X9A35noHHViGiOZUAAphWauV6BKi2WTj5EaCPoawJDbQo6YBoF7CAEpRgh3yMR1Mbxjf4zQ1olR-fb5ECD4WYOZkicjTkgigF3AQIJlZYlOzhZ8yOJjlJggOyDBT4r3cGL5eetSv7MhNmT49crukIHKc00lTWKDOHMYk9aP5DgpyWvyG3IFzOIfx5cz-HRD0InEHXh0h34mdr4BhH2O82zJe19HmVR389K5s4wqVCrSWNPKIZtCgungHhk9JGOcjTY4kBG1CGrdkvoY0G3Rz27gvHtrZqXK_sP1zRXFnoerQvUEBWEPDx4tUjF5MoSotzZWhSY-BtA6OkhCaIItex5qShNa3U_gUa3C-a2fwjdtx-Gvd59VG0cB3XjT6MwRdDrWGTV44PIPBTxkTtvsvM9XfZm3W8P_W7u6TbHCiZF_AuDIur9RY60BFkJP2k88-adaqqFJANqyuI8bp5t0fgZIoK6wSjY8trlZPEvu2BOsVmZg5lK9bp8nNL_DikUJa_N6Eb8YvOnigQo1-TDbZMVyRVUF92vLV0h0nhMhChc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db7c1b068c.mp4?token=FYX8y9EXEd4WQjdK29dZTBzCZ2aiTfcx9L1N82-xQcUdC0x4BuSD4s12YuCZvAzfPTA0ajWSsxIt5u7wZ_4rGC8VmAokvLwEpjrqmAC1d7Re7iB1UC1T-aVoFqH5jEhv0X9A35noHHViGiOZUAAphWauV6BKi2WTj5EaCPoawJDbQo6YBoF7CAEpRgh3yMR1Mbxjf4zQ1olR-fb5ECD4WYOZkicjTkgigF3AQIJlZYlOzhZ8yOJjlJggOyDBT4r3cGL5eetSv7MhNmT49crukIHKc00lTWKDOHMYk9aP5DgpyWvyG3IFzOIfx5cz-HRD0InEHXh0h34mdr4BhH2O82zJe19HmVR389K5s4wqVCrSWNPKIZtCgungHhk9JGOcjTY4kBG1CGrdkvoY0G3Rz27gvHtrZqXK_sP1zRXFnoerQvUEBWEPDx4tUjF5MoSotzZWhSY-BtA6OkhCaIItex5qShNa3U_gUa3C-a2fwjdtx-Gvd59VG0cB3XjT6MwRdDrWGTV44PIPBTxkTtvsvM9XfZm3W8P_W7u6TbHCiZF_AuDIur9RY60BFkJP2k88-adaqqFJANqyuI8bp5t0fgZIoK6wSjY8trlZPEvu2BOsVmZg5lK9bp8nNL_DikUJa_N6Eb8YvOnigQo1-TDbZMVyRVUF92vLV0h0nhMhChc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۶۸ بار حمله به یک پایگاه؛ چرا العدید مهم بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/458567" target="_blank">📅 22:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458566">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کلاهبردار ۱۰ هزار میلیارد تومانی در ارومیه دستگیر شد
🔹
فرمانده انتظامی آذربایجان‌غربی: در پی گزارشات متعدد مبنی بر کلاهبرداری از شهروندان به شيوهٔ خريد کالا و صدور چک‌های بلامحل، موضوع در دستور کار مأموران قرار گرفت و متهم فراری را شناسایی و دستگیر کردند.
🔹
متهم در مراحل بازجویی به ۹۰ کلاهبرداری سریالی از شهروندان در استان‌های مختلف به‌ارزش ۱۰۰ هزار میلیارد ریال اعتراف کرد و تحویل مراجع قضایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/458566" target="_blank">📅 21:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458565">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f09d5bca.mp4?token=ZuAUxjg6NrhHHpgonztdyexdr7fd9DFkTDvgAQIUGaB87EJ7YuY7KtO75WcBB81vn4b7oHXa1nABjrbbh4z0Ehf-CfqHQecHnVzF6S6me-rySKoTwVz9K7eriT1wDRCrrThhnZV1IIbA2VI1cfhO0qw54vWL_invfmgyJxKNZ5y5xQxjhHWFSLHwxqSgxlRgvRI8Jg_N-QclaCITPQBVQZFgOxK6k0HM7PFAEdUEy-CthgBx2pDptBmWG9ODNamvs8h0eV4Vk7dfxHNSGMWM1kKV6bH7FDtKGzolZ2ZH-zcQbwZsRQSAQZpUx0qHpCPQ6PQbxiGEH5abgGYRz3b8Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f09d5bca.mp4?token=ZuAUxjg6NrhHHpgonztdyexdr7fd9DFkTDvgAQIUGaB87EJ7YuY7KtO75WcBB81vn4b7oHXa1nABjrbbh4z0Ehf-CfqHQecHnVzF6S6me-rySKoTwVz9K7eriT1wDRCrrThhnZV1IIbA2VI1cfhO0qw54vWL_invfmgyJxKNZ5y5xQxjhHWFSLHwxqSgxlRgvRI8Jg_N-QclaCITPQBVQZFgOxK6k0HM7PFAEdUEy-CthgBx2pDptBmWG9ODNamvs8h0eV4Vk7dfxHNSGMWM1kKV6bH7FDtKGzolZ2ZH-zcQbwZsRQSAQZpUx0qHpCPQ6PQbxiGEH5abgGYRz3b8Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعی، کارشناس مسائل منطقه: اگر آمریکا بر تنگهٔ هرمز مسلط است، چرا هر روز مجبور به تکرار این ادعاست؟!   @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/458565" target="_blank">📅 21:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458564">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4308563c0e.mp4?token=nXyVHa-g0EvgNnk4Vy7S3mKG8TjogU3JloRU1vwuIBJZ4aizAvVi2--JPA4x3UoLtcQ39dYK8R40r9kkbnFrOK1jMdBE8_WpbRXH1dyc0dJi2dPmU16YIzh1MhJ_0Dg627DJrXTjj8WA1iBVSKSS1cbP9ou5v6W2lGWKSW7-XBm23rAVKIdzSb1duFd4c9S9P82jPc2mGAspjMWESvPY-VPi5m241oQcdb4JjYQYYNo6OH5z472-VAuP1-nHxNjj2lFR7Yv5Dloi2CA6tVS-OHy_QkKbQ8v9bSDDpKYBBC3oA7qZVK6YCTwvvURQRLauo45w90SDNjyBT7t7xG58mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4308563c0e.mp4?token=nXyVHa-g0EvgNnk4Vy7S3mKG8TjogU3JloRU1vwuIBJZ4aizAvVi2--JPA4x3UoLtcQ39dYK8R40r9kkbnFrOK1jMdBE8_WpbRXH1dyc0dJi2dPmU16YIzh1MhJ_0Dg627DJrXTjj8WA1iBVSKSS1cbP9ou5v6W2lGWKSW7-XBm23rAVKIdzSb1duFd4c9S9P82jPc2mGAspjMWESvPY-VPi5m241oQcdb4JjYQYYNo6OH5z472-VAuP1-nHxNjj2lFR7Yv5Dloi2CA6tVS-OHy_QkKbQ8v9bSDDpKYBBC3oA7qZVK6YCTwvvURQRLauo45w90SDNjyBT7t7xG58mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعی، کارشناس مسائل منطقه: اگر آمریکا بر تنگهٔ هرمز مسلط است، چرا هر روز مجبور به تکرار این ادعاست؟!
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/458564" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458563">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f572f47b.mp4?token=UGWepb3qnq01ucwGeyek0V-v-9MrCqA6ZJA981-M_ClI4dsGqA1HXuCApxSX-ER2KphN9d4rPryVZIRarb0VJte0nMYaz0dRl-1UjQw0BrcGItgLhMk5L8os_lDfzRIIl6Of-ng5Jh4n_VQpVT6rUj4LG56vR-4FTdAs37pyCKE1vTiXyPTgg15yetVxYSNURLgWeHtAfzi90gZwnqlEkEf7G-h5rcTt3aIWslXHi8-UfS8tHwVgBNRZRK5gfY7itw_1zqCU0kG_ac0o0WMiHvJSE2churnf4opYfY8WPD4_hARnK8voKrnPJAl0D-Hb1cQIiXnY-2XANIA1eCFhzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f572f47b.mp4?token=UGWepb3qnq01ucwGeyek0V-v-9MrCqA6ZJA981-M_ClI4dsGqA1HXuCApxSX-ER2KphN9d4rPryVZIRarb0VJte0nMYaz0dRl-1UjQw0BrcGItgLhMk5L8os_lDfzRIIl6Of-ng5Jh4n_VQpVT6rUj4LG56vR-4FTdAs37pyCKE1vTiXyPTgg15yetVxYSNURLgWeHtAfzi90gZwnqlEkEf7G-h5rcTt3aIWslXHi8-UfS8tHwVgBNRZRK5gfY7itw_1zqCU0kG_ac0o0WMiHvJSE2churnf4opYfY8WPD4_hARnK8voKrnPJAl0D-Hb1cQIiXnY-2XANIA1eCFhzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید لاریجانی از عطری که شهید لاریجانی به رهبر انقلاب هدیه کرد  @Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/458563" target="_blank">📅 21:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458562">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f61098eb.mp4?token=IZd2IODvkhOeD13sgO83md7ukWx9BZxnvxPQsuaDkkjmaCvuaTSA1Iw2Sxm_bT2QsOfN29_2AmDNa57JpFLaqwq_tKteinuxGOK6m45rKoTwEtfxILFVHsIXH9TnrTVS1p93RnRZ-H4Bw6IzDW5FivW9y7h1JOuMxnqrY1NFAH9xQjXwPRfg1Djopb5nxD6SzZ6jWuSfJBUhTdNh_2lYcbvq7a6lhgZN9FAjIVSK_iip7TclPMGVRdrsfH3YprAkAAAoIpmQ5a9tev8ndGlobNcjJ7aM-QYWnlhPoMYONhqA-xgGsXpOCGab041nQjATrC9_9wrq_Oil5tXNYK8oeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f61098eb.mp4?token=IZd2IODvkhOeD13sgO83md7ukWx9BZxnvxPQsuaDkkjmaCvuaTSA1Iw2Sxm_bT2QsOfN29_2AmDNa57JpFLaqwq_tKteinuxGOK6m45rKoTwEtfxILFVHsIXH9TnrTVS1p93RnRZ-H4Bw6IzDW5FivW9y7h1JOuMxnqrY1NFAH9xQjXwPRfg1Djopb5nxD6SzZ6jWuSfJBUhTdNh_2lYcbvq7a6lhgZN9FAjIVSK_iip7TclPMGVRdrsfH3YprAkAAAoIpmQ5a9tev8ndGlobNcjJ7aM-QYWnlhPoMYONhqA-xgGsXpOCGab041nQjATrC9_9wrq_Oil5tXNYK8oeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدار  اعضای دفتر حفظ و نشر آثار رهبر شهید با خانوادهٔ شهید لاریجانی
🔹
حدادعادل، وزیر آموزش‌وپرورش و اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب به دیدار خانوادهٔ شهید لاریجانی رفتند و به ایشان ادای احترام کردند. @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/458562" target="_blank">📅 21:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458561">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec9b5f41d.mp4?token=lukR5hIDSCLqfyMyADpuJEfk1QDBB37Bs9CRRsl6vJihzlqZ5QDxm-dXyXbJqrkvkQQNPLhJ4yXjsIuuOmuiEalc2qkINCO1-ByhqZtPKBRVx07cTcZWyPAc-f3MeRC2b4q4godWkdR1oiabv8W-nAOmXDOe1avI46tx6teiMMs0fOsxctLZM7H7d7TPILr57BFMztlbXe79sXNxz-GLJkuxvKv7426iveNZnBGcpB-UyGzM_NZhyDzbudLq-aWW56UnHT6sbgTz73s70vZip4SZwq9-CeAJkOk6dr6lTQGRZFUDSJIrc_5WadVgFs4bPh-IdTbZQb_HElnEMXhG3g3bsIb8DGz5HnCzZUzW6UkMBYAwVp7OBTPOq2ombMSq6BsfnJsUGYnmOOMQvR4cqgBvTRmsfwjpd6pdvD-By2tqqqQx8jn1t1PJTa4IPt_uyufv0FHAbZvDIn7c9AEAtlk3hYx6ln_j17sMV9Fn7TKaWdNM5QFWozBJIeNCI92gbsdDxMLwCd4bI39zYjjVKi1IokaZMntNSq9GHuUZFdsypcH6Wfx73SNB6pHJLCiPrjgEDd9eRxroDejW4CZCW_QLPPNbpsnYF68kUGErAvSD9sXDdxflwHivu0Hk5zsDhQIo656HIDLTpKIaabQFUEPj-Y0jrYssPJwsOjBZcMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec9b5f41d.mp4?token=lukR5hIDSCLqfyMyADpuJEfk1QDBB37Bs9CRRsl6vJihzlqZ5QDxm-dXyXbJqrkvkQQNPLhJ4yXjsIuuOmuiEalc2qkINCO1-ByhqZtPKBRVx07cTcZWyPAc-f3MeRC2b4q4godWkdR1oiabv8W-nAOmXDOe1avI46tx6teiMMs0fOsxctLZM7H7d7TPILr57BFMztlbXe79sXNxz-GLJkuxvKv7426iveNZnBGcpB-UyGzM_NZhyDzbudLq-aWW56UnHT6sbgTz73s70vZip4SZwq9-CeAJkOk6dr6lTQGRZFUDSJIrc_5WadVgFs4bPh-IdTbZQb_HElnEMXhG3g3bsIb8DGz5HnCzZUzW6UkMBYAwVp7OBTPOq2ombMSq6BsfnJsUGYnmOOMQvR4cqgBvTRmsfwjpd6pdvD-By2tqqqQx8jn1t1PJTa4IPt_uyufv0FHAbZvDIn7c9AEAtlk3hYx6ln_j17sMV9Fn7TKaWdNM5QFWozBJIeNCI92gbsdDxMLwCd4bI39zYjjVKi1IokaZMntNSq9GHuUZFdsypcH6Wfx73SNB6pHJLCiPrjgEDd9eRxroDejW4CZCW_QLPPNbpsnYF68kUGErAvSD9sXDdxflwHivu0Hk5zsDhQIo656HIDLTpKIaabQFUEPj-Y0jrYssPJwsOjBZcMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدار  اعضای دفتر حفظ و نشر آثار رهبر شهید با خانوادهٔ شهید لاریجانی
🔹
حدادعادل، وزیر آموزش‌وپرورش و اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب به دیدار خانوادهٔ شهید لاریجانی رفتند و به ایشان ادای احترام کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/458561" target="_blank">📅 21:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458560">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرماندار چابهار: فردا از ساعت ۷ تا ۱۱ عملیات انهدام مهمات عمل‌نکرده در محدودهٔ شهر چابهار انجام می‌شود و صدای انفجارهای احتمالی جای نگرانی ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/458560" target="_blank">📅 21:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_RvL4F2m2qMGPXasXWMj4XkqNWNGHUHWRAjA0-Uga1PPQ6VYrFh9blh3xfpByrfJEOP3brIQn6ozdv9HMgH1RnXjS75PfmjlBKRl6RA9n4YwFfSdvmZPJQgX8pJCz_yuNw0OJqIcc78V8UqNUIDSZdOMRg2Gd3R3pK9UgOYKroTbGFd2mxwTAIft8SZr6YoQq5OfUEkCd_oHW1fauoL6AWXTNAGYDt_PEvwxRgm64l_e4lRHIYobN1glTDsqar6tppaIfbvLgt79t2JSEAmlIuwrAWaSKwwgjRe4Uf_FP9S86eMcbLHzM9FfpzCERuEX7fpNJv88xHdCs3vL-n8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeO9r49iyHiGd461V73Z3LcUPwUHfI38_Lu60Py_COIxzqSDlvXDfDOpMYSY2LbssBjPeMvNSjIzsxV1kuhdPFkwmAWg1bgYwtIPhzLRJ4oj8N-qHd6CYoXyEjeMUHn_9d1Is3PvS_-6P0eD1YRLAD1rhr3xD2Qck4WZRotQfOYuyEURHGaXz_-NPKS2NqWBb13TGTrrIZ4V9RdJ7BQXPukAT172uPgbYiwrNoqeghUY4N2MC1tJo7y7ovE0brUJ8gocbodLGe-kbHVKkOR4I248UpakpGWSz7xqJqNlJ08EQ45BOiebl8vfOIsg2N1yR3uWRqOkbA-Y9eF2Nm2duA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9dRE415nhQR2xfFTJ2Zc3P9daEht3Na0V4loAHUepXne3-6BOU1NFm7wI1kdougZ28mYH2ZkkrHt-ItpUjrHRTrBWCYRwfcHqTpV5BivJjoBm5og3OVi6qtTCr-26BRKCUKUmpHm89FJyXSM6174-y2wTwpb-4-YpbyavgfDgU0ZdLdAue-4qdyZgptBWLNMfkP5ZM4l32dABqRQ1dRmmKKfCOI-Uaidey5FhcGYIoZCGESmSx7GmGssC6gKSFQ87jbO7x_Xyp07B9rimaILyYF9_zN86ooP_kM23RwTKfW3m4qDl7lAUvTIUWnj2Xdq0vPPrXABC19O1ZmaTWLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIPhQAdngoESv4tqs4lrS4zf8fBEhUSFQnL2KKyz52pKbuaZSeo1OtFBcc02OhAtUYX_sq6CUfTny5uGoqT2xh_6noZpN8-MjDduBu9XgTveJN1G7wcSPelkkg5ixwGCUi1BrSFnNlHGU4DWBD66oj2TtjPQdMAEgoy8ox1aubWSEx_PdumB4JVaypauX8ItUUCpiWHp3tgOlCAg-xadNnU2wuYzCQ6oF_7JeXn8Mqm97JhobSMetI7HdPfG1FQVP78AFrdQVLnhVNto4dh8Rdh5NfGWVKmZyPbKgTPmMiAZ6NTB9rmkfTGbbqznbe9xTEw0coNdF6w-6_9_5ifBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7NX65DQegkwBMhRpZ0hoA4HlsjnEdLHTewTE36ojmF8jprRxOn-xXgV5sKmY0MkmDvgIe6wvNg7T6Hz64F3x4iQcN7MmrjdLQUSz-O9_SVRKxx83tHwry6FxPcqOQp7V15MJH0MEudaGrMafX09_UtoudWpTNDpbV11mJz2j9YDZ11Un2jD9jy9W573D75NdH2HgVbYRy9pMquGBT26jstdD-LJ8hkAoqmN12Sj5JSRQ-0H2o7n5XPSx8eQAzA5CELKfKXkbcd5MWcGUYt8sJRZ5rx8CmujQIvZ6GMjtmehfvrx-MA8Pm370h9mOvAp2w2gOlCA_btB9B41uwQdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVXLAesdgzbanr6ZUuQ4LbmAFBqD7xDUAKS_rNoUCTArxh0P1H-ZxKo0mHuYluEJ5XvM_fEvVsHr9m05axgE7ndqKCMrICXklgKqa90M9Mj5r7MV-U3bKUnNJTfJXOTQEgGN715W9KZMPTUOqeoPk0tw2bdpbvK12f2MpFnb6gs8q5MKz0KZxfdPzrsEMhmw6OyLlf8kfyZaIKiKKuNFaW8yieTTvSbZZySgtUjXCOz0P4cqnR7mO69UU5-O5sSx0OP0-uJi1pluNZoN6LYM3ukZR774nQU9TDODXxdP-WV4f2xTmjhtaetthxRb0Rk81aYHxx5ll9Km_qzmANfuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V70qmBehjayEBKMSmVmWS6umAmPTI_CmgIoQiDhtvEVpJoU4YFCQV6P7KbzwNpZi-6a7DNX630Ukas9UGDPt7r7PV0phgnwvOLhiLot_3lQBYOZ6fyp1Lj7QVb6Krv91gVB6HrIzoybCszBJc1q-rGJ9zlGmnRIQGqjBHXxZepQKBOHNUmWXpTSToc-oSauTcv7piBC6FS5w_KtQEAfkjKv6kfHeKwxBXGVs_185dE_GnzlCAgDqZi05llUXlOm_b25LHqcKXl-nAmwP1oLMOYizyUp0KZfiJKU-KIgVsRKwZpWxQPQ2-GaIO0QZK_vlTXT1txF1EgWDlOI1jWCRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxCG3Bvz4iImpob_jh6tkZE3Av4IngUB8uS8D6PCOPS5UtY-FAMnQyBAUPoWjlNJvWZXBfq75Kw5gy9rGYEPDE9jAQe9CQYc6pYa5VPYP1mG4NDFhrof4DGfBG3RCdAxpaVK58UnZkheZWDsgGaMr_jN5_qcZdOFLJWALszOIxJzd6y6KjDLBDEdI2QGhbuKuMOTM90OZZMnEE2f6Z63Xc9KZnLmCatBTAlJ7NK8HyoYq58DQLS7TatZ354RuXSWGzn9o6jGMlqcu3JwV2r79kQnUs_9PSFJNtTgFr6RrBz6Jn4Bdk-YB0PRYG-ZZOA197KCT-3vMBvVhP8VQrDkGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEPhqOzhoAtosAnoqIl5VlPsWWcDWCWmKDGwWi-6hF7Y3FccVMrKMMXi6QVGpGB5Tie6tl5r77G-V6DOUfLzIHAHfKfzz5Evd0GgylBMuYccUxe-m7p68ucvu1pv8YsXuTPGOYDEIvEEc8DRBsI04AgWfHnuBZvtbogD6sCN-ZJSS8lA3_F7J8ymWi_-OJENLLeqZ_R4wQkhIK6dZMr4dmUajAfzA_WEhjcK9Vh9bT9gw8IFJNUtNFw3dg4EbKSzCXSUpFu_K6bB2T1Z7cxsgwwBl2R6UsDB7lCO_977TyZNnJeI6k2WMDfZ5DSPyNhz2f3oUAwEJxhxsLlfAj4H6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قرعه‌کشی لیگ قهرمانان
⚽️
تیم‌های
سید یک
حریفانشان را شناختند
@Sportfars</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/458551" target="_blank">📅 20:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzJaIaJJ0gJr4C5MX0HgSF6n_JXZfZ7U9uRfGszp3mPD04j3k9AQksRcwHw3hmPjbIULvVkaxNIaVo1VadviZeOhHRESF8fwX8I4sdh8wNH2eCW6Rw-FPQwmHsX_ERoUVcabX9Ec_zBtLSCv1JIoHmO9g0NU8qe7C2VmuczQxZfEbLFy2nqlwhac9laC-uqr0ReHVJ5OjF4Jj1mDrmO3cCiNxlQgHyk4OrQjzpd4jrwwWerTrPrJe6voAR59lcbj4xMLmk9hQ4utpOLDHaKMJWZg4EX4wJ3ab6hO8pTq0e_gDJKsIMphIqxd60RH9AvNu85T2XJls3lwPE_v3437vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف به بسنت: نمایش مضحکت «روز پیروزی» نبود، «روز دلقک» بود!
🔹
وزیر خزانه‌داری آمریکا که ادعا کرده بود تحریم‌های جدید علیه ایران مانند «عملیات نورماندی (D-Day)» کوبنده و سرنوشت‌ساز خواهد بود، در نشست خبری دیروز به سؤال خبرنگار درباره توخالی‌بودن این ادعا…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/458550" target="_blank">📅 20:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شهادت یک مرزبان در حملهٔ تروریستی در مسیر میرجاوه-زاهدان
🔹
مرزبانی سیستان‌وبلوچستان: در یک حملهٔ تروریستی کور، استواردوم «علی حیدری» از دلاورمردان مرزبانی استان بر اثر اصابت گلوله به شهادت رسید و همچنین یکی دیگر از همرزمان او مجروح شد که بلافاصله توسط عوامل امدادی به مراکز درمانی منتقل و تحت مداوا قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/458549" target="_blank">📅 20:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458547">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWCspbw4c6CnS-PgJynBeKlRRjmQDo8K3Z1Xhrru5A3ETKYcQ36EO-BZpihgjfde1xI6qJfkesdo8GeJYCNfSzQ9K1EZUx_gH3pg0NZ40Av99AqjXgMhRFUcF_U7eIqXDOeXssleo4scH9R9oO1s_ZqT8CTjOqzzNMkHvq2E89At7S596tl4TSFpdXuGHutlVFFIgjr80JZilgDoFrX3itnSMLWl2dPWShH2ifjaX6p5B-xtWwhH2_IXhqJxzwwMw4sjRd2HDuNflkgV8l9yaDo6xNE1L0GlCDhR3A3rcnOCIL4uuYro23SkCwO5lNW0qdbUkw2LPaibOv1W8hq6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجهٔ قطر در دیدار با پزشکیان: امیر قطر شما را مثل برادر می‌داند. موضوع خلبان‌های ایرانی را هم با صداقت پیگیری خواهیم کرد
🔹
محمد عبدالرحمن آل‌ثانی در دیدار با رئیس‌جمهور ایران با بیان اینکه «دکتر پزشکیان نزد امیر قطر از جایگاهی ویژه برخوردار است» گفت:…</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/458547" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458546">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Al1zDtP7ZC2IoEqDmhB0InHBviykKT9j2PWQJpW0XrzmFwnZN8UIH1tt6S0TPWAqcWZ711OVIxUO_hyl3QGPjvCtZE5s_4VDHddELXCPkj5P-zrtxZtYGCUNiQ4xNfpctnXHEdOvnaOx1Q12FFiKzpDCL1pKr_T_fNruHOMeeqn6gjnGxy2DF0p33i3_T9xO81OiqIyboCKTdYtIEA-Ny81SB0Y5nAdFOQmbUO5oy6cufNKUO2sBttSFoOY2AEqZX9Dp27bY98OKse-8Xqbh51vaIArobwh3CMjGwJB0G-PkxTePvZNffvjKjnjaTgK54Qv42xnyff0lidBniEDA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار وزیر خارجهٔ قطر: نقشهٔ رژیم صهیونیستی جلوگیری از برقراری روابط صمیمانه میان مسلمانان است
🔹
مسئولان آمریکایی باید صداهایی را که برای جلوگیری از بازگشت آرامش به منطقه تلاش می‌کنند را نادیده بگیرند. منافع عده‌ای در ادامهٔ جنگ است، اما ایران معتقد…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/458546" target="_blank">📅 20:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458545">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv4dDJGclvJB7clxSLBKMnU9lXmda7Et5ELw0WUOxlSxG7LdOsM8D7tVcOgu5l0sr4csxAJ5KUglBWW6m-MISDG0_ZvFw2eMDpzRTuzdq0ZLHPhxr03iqxu1Ag1IETYd97_sltwGIykEYTRcCxyj8Zv-f5-ru7G0UKLu4Na3lh67EroCwglcFPstDuPfIBI65GuekmUXx0knqeu4MIFfcXqOSM9q1C5kfkoEj2iAV0eY3wP-hB7sL74KqyBnVKQ2eRH6sIpPHVLR-IiwS6xFW1pqN-exoYk7SSpwkPisaWvjtGDcM5wfCSpLWNq7fU4LoYiDL37-Cq-nc4_iqxp7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر خارجهٔ قطر در تهران با پزشکیان دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/458545" target="_blank">📅 19:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyQ-C9GLhzivHQaNRV8B1Ra6JUdymJPAU1VQPp7lokF0Zb3QK-H_viiS6HAnZzQ3i48q5r1UDt3P4J_Hqv1G2B82iDOFg-pdsXOLsQknGQ2QjvcCM8boWRJVbAbZIYf8FN1fnuq60tmDGc82_CmIKT6uxhqR8vRuyFK-jay9D5s6TdXXR6FAywDND88LgRviu_iaB3KWjs82Uzcoo7pO6XS3bnUjOgHBtLUPQZrUSe9XqemH9Wo9_v3J1RJD10sp96AOMlI0aLA8kJ_-FXnVrT3UfCOv-1KoYDvmJQjyraUw7h_octpaZ2QmS5VntSeP45TygC4HKOcYmsAJUQ0ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_GmeD3PRVrdRFpiesL3t2mR4N-z-01XTlFffaoL6zqZpbfEMb8vYRajD9-ZWnt_ZOXLIhEZMdTdCcumYwbiJGAcH4Upy8jGxht-LCpmD8vn32Oo0h_N6rZvNPvkHFCSl9eOIcERGCP1DXYsDIax-EEq1n-qGtHfxbrdOnVq6yFX1GnlJIfwJzgJw7wu4xn3sD4LHzGMZDA3nQG2LhvrYkKQeFgp9qFV0sH6YC3pFNgGzzZDm-8jTUWucuf5CL4JcKhBJjpneWhQf5g9DWzvCRoFx7i0hhQDtA5ffJ2Ba7isLrVOS2_SWxIZS7xsprq4EFsVPl7K37Vg2h8dgY3sNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAnNLXrVQ5uQzlP16JPuR6MdllLTjIbEK4I67v-I3BNVxLUiPBlb51NI_Of1o98KtVu7akRCdAmldRMCRbS0OoLDRZf02rJJ4FvFC3wvFWOJhlS2c3K5DSScoHL4bFhFaOfyU5cqDCReNn4NR7AN1S7pkhBP_Ym_DSmSpVVRS_2oTSp9-KIswKlBov0DRE0RGNWy74btqZxlR8DXZGCCB36-iI9_IJz2XaLeu77KuDLAnjZb_WUEEwmLDp357sW2MTTOpS-sIc1rrFwDES-g8ztWsgwimsg8QTCbH285UVxw0up8lDNC_0dkiCV19rJLdhzuJ9_j1sYewpGkGKtu6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
همزمان با روز پزشک و طی بازدید از بیمارستان سپهر سلامت انجام شد
✅
قدردانی مدیرعامل بانک صادرات ایران از کادر درمان/ افشین خانی: ارائه خدمات درمانی مناسب به شهروندان، نماد تحقق رسالت اجتماعی است
🔹
مدیرعامل بانک صادرات ایران با هدف گرامیداشت روز پزشک با کادر درمان بیمارستان سپهر سلامت دیدار کرد و ضمن قدردانی از زحمات آنها، ارائه خدمات درمانی مناسب به شهروندان را در راستای تحقق رسالت اجتماعی مورد تاکید قرار داد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#روز_پزشک
#کادر_درمان
#سپهر_سلامت
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/458542" target="_blank">📅 19:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromصبا فولاد خلیج فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzGET1Yxk1ncUmq9wTO8dzOFd5Qh8VhRKbxuDAXwAFDvfKUTCIou4wMxgf_qC6io18SjPyuAWHROLTEaGtFsGs62h-4jNG75M6T9Y53Zs2ucINglCd8MseRqpYp4SfuOZmGKkNSUQHE7fIOXRMIZj6qV-kwo64Ra2VVxfN2GO42EPUUvmI1PP3bM1eyKGG4Ft1o5N1NpIRkr13jc89in71o1lHI5ArDS3KI2-VassgvEpWqXEnk-gQtGZsB_U02DOpM9GYAYgvN_vsK6JAL6PSD-3g2yi2UCE1s-uAG-dfY2joUS6K7_bkPeAwy5PbO59f5FTHbBNG9_-R32c3rUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد ۱۴۴ درصدی درآمد «فصبا» در ۸ ماه؛ فروش ۱۹ همتی با تکیه بر صادرات بریکت آهن اسفنجی
شرکت صبا فولاد خلیج فارس (فصبا)، یکی از زیرمجموعه‌های قدرتمند صندوق بازنشستگی کشوری، با انتشار گزارش عملکرد 8 ماهه منتهی به مرداد ۱۴۰۴، خبر از دستاوردهای چشمگیر و رشدی قابل توجه داد. این گزارش، تصویری روشن از موفقیت‌های عملیاتی و مالی شرکت در مسیر توسعه و سودآوری ارائه می‌دهد.</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/458541" target="_blank">📅 19:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/458540" target="_blank">📅 19:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIt9aQH2oYxWKKw43wvxvoEgVUqQLY71TVOpDpFTwR1Dv4O-742yFCP-E4vueP3vgTE7rh69TmOx2VXXC31Zy2CEjcc-o_c6FbzHeYNWkbC7Mh0iJdjPXoEU_Cg0WGOJHp-M_YuSZoRbQ2Oh31AOO30p1sBIbnaAeN9rRq0RZp5pV-W1xqghtIiywbW7rwfrkwmRlSZJNGPqhHIhaN7mERd_QeoXr5kEiXZT-wiiH-C1vZ8FF9n7W6LaHDIA1eTA2S4bTpam5a0x5lp30EjronaUY6SAIpouPhlK3jRC12Y4MW5B5Psb3hstDGyGeLcvBX4wbmhJvXLnkw0C31FatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: ایران در عمل معادلات قدرت منطقه را تغییر داد و ثابت کرد دوران بزن‌دررو، لشکرکشی از پشت اقیانوس‌ها و تهدید تمام شده است.
🔹
نمایش مضحک رسانه‌ای، واقعیت میدان و طرف پیروز را تغییر نمی‌دهد. تاریخ چندهزارسالهٔ ایران را بخوانید تا بفهمید باید با ملت ایران با زبان احترام سخن گفت‌.
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/458539" target="_blank">📅 19:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1502ec842.mp4?token=JEt6qYuEOLmjzI4XrIdssgEF1j_CgjqOU2d-0MppfprrjRVVkYB1heZKNj13nvs700glkJZMGeydC-4fNUwamHZvLSCm2OeBNaLnfCDOT1hxZ7LZTgSyCNcA9nv4bsdtNKQrfjBq4vA4MUlYHgvJSnt5mV3hwmOJz14Vk4LMeuqLUd1Yab4Tu92-ls8LGjAw1-rUeZ-60hmcMOokCDI1dHcWB7VJTfDLzqME1dYIt5kty4wnEWnwDwHy8DJlZoTU_9twVEf6ka_CGp-67K9UyYOZaxvo59ohWFXnkCT1AFMClYfki9q6oQuDPyT5ar9ztmvVfypcosMSHmWBCZSjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1502ec842.mp4?token=JEt6qYuEOLmjzI4XrIdssgEF1j_CgjqOU2d-0MppfprrjRVVkYB1heZKNj13nvs700glkJZMGeydC-4fNUwamHZvLSCm2OeBNaLnfCDOT1hxZ7LZTgSyCNcA9nv4bsdtNKQrfjBq4vA4MUlYHgvJSnt5mV3hwmOJz14Vk4LMeuqLUd1Yab4Tu92-ls8LGjAw1-rUeZ-60hmcMOokCDI1dHcWB7VJTfDLzqME1dYIt5kty4wnEWnwDwHy8DJlZoTU_9twVEf6ka_CGp-67K9UyYOZaxvo59ohWFXnkCT1AFMClYfki9q6oQuDPyT5ar9ztmvVfypcosMSHmWBCZSjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات جنگنده‌های صهیونیستی به جنوب لبنان
🔹
خبرگزاری رسمی لبنان گزارش کرد که در حملات جنگنده‌های صهیونیستی، شهرک «المنصوری» بمباران شده است. همزمان با این حملات، صهیونیست‌ها شهرک «برعشیت» در جنوب لبنان را هم هدف حملات هوایی قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/458538" target="_blank">📅 19:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458533">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttmzvDiKZqKs4g7ST59LLoe-ND2vTFjWX4kPci-_zbDbjAnRquVbrJnu-OPVGEilHRuze2bQKwZQg0COmeaOiaIMW2FVJ8gD7TAaV-uDwwFjk1yqmXJ_JLtVsGYiNyZXDu6qQN0cJqPPMgUr3s4nBV9adB4Svz8C-d_wu2lK36_CAmTGGVfwTQU0ZC_WVkdUhMEMDJE580lZQ0Hay20MNhCr-OskV6VvZWUWaczbjcDqhhCNt97NPdRYIUYXjFMTbhEKo4bueqssZ2fLenmQlKIVMHBcZ3O3HFWtd6Rt9d37k036dywL-1AxTqqLfcqaFKz3W0sqlASPMzz8YgZExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jUmBqiHGLI4xxruwMw6jttvmN1IjOsjpIsFBLsVc2F8O2ClGP1ZCHe_mkPtQiVxehl3wcrLN2u06hFYUg7Dhqmswpenf9bMS7mYzxC-LbD55t9lmdwaYxKTMDFmSAw2w6bmglwzNI3kzeo0DOs36KDFr2oRf3P5wp8S6tDkikpb-oz-xbXn8XHvCnYhBpIYnJvQl9zr6-xMVHbBWTSD_-tM4t4IXLSftohfMLc66loL9FuiA-2EEW7XrGPnUsKz8waR-RWo1qH18L6_JFa4iy0cGRnW81oCWp2SQ0VQx_0KfRvSWUC432_NL_W8NHwj778DCD1qCFBvCHLBkosvMGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6UJ7tGGNRzKN5UrBPCFWHtXN-WxNpzuU_xNWVPBI2QvMU6wXZNBf9hsaIpxj3gihdUBqu-uiIt9SPocqkFAxaEr2WiTblDYg3tFXjxp5NkcdUMdOa__RoDAGpHS8sFownddh8scTlwDAVYxrYLnRBPfJrff3szIb_eciSxBZ4T7yLjHFFNWrC5B4jGfp5qBctO_47WrJdWmH-Z1s2OwIKYmDO4uZIuzsIZGElTRCPVZi9PrlVswkIu8CnrlioZRhv6Wq2C2GxtROZ-v9E4uUMWw8MDaWBDVGzMvbUYUdpBbETDm2rjyaLDcUcia3dfRULzEIU6qLMjmttSTsFCkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjZ7VCtF6NOO8dzArze2C4VMAKZhLC5BJqnLVTtQyJBuPyyEBvVZYSyGbCM71Peb14X-YoLqR7hF_PILiDr7p0x7iFkxUTRifn8ZI0SyKBJPvwS4P_RWAnS8H-FeSEzdUs1_hUfbQb2pzMIjuUR60iFFiBaFnCUjUTNOkfRsOAn0DaHA5CvKIWUCCeJRATTqdpKnfWfLpUf0u5bbiSCEHhneaHASAqO18sJ9ZOC0-_JAub6oRtmycIjmUsWl7jpHM9QV_oRiFqcQyMbLfgjvq3PkN0MJEtXJ0wTpUlRVUlOZtrYzvkVKC8bSk4PkuJQXTSFCkn3xA2eFDW9Z7bchtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsYkPAKaldm5U3qAFBB4dvYj6pMhJhHzv5oJnUadtz7tZuRbcddMBHs3KN99f7S8NkKYLepqNUlmt6SY6K2qVtn3Q4OrbrITBNSEIxi8rKf9NBtLL4pBZkVzt-uftxx74Ru3P0KqRiK7uyHAjXoKlc0qYUa9mMp9EqCLsyShr0BofHqsJH0y7Pj-lRFZmkSm8wCINQMar9NroUzTYXM1WFAbdOkjJd3EDOCHOu0YHNfBfHHDcDYO6CHg7PuGfMfu3IdOVPwvSTRJJbl_Rf5J47pLj5PZgfPg72-OVSA6gl6r-jlmSvsgSac4ww4RuC_K6skvzkdaqphjwKAg0hNKMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از دیدار وزیر خارجهٔ قطر با قالیباف  @Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/458533" target="_blank">📅 18:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458528">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I47N4sh87khs9SLpoa3gz3bV87Wta2Anzed_sYTwjY-_wgU7s5hAEBzVw0yp1bh9JSKddWzE7EHpTQJjjp5ZfiG90um49L-gCLHQdE5KtFVwuOLPfqpf2iGMCG634KcsOfIPp-enHPqGullDicgtZzv6RUmRE01ypn24oGmBGTLe7-JFrSCDm_oWCZE6RRK7Qz2uMBnl52mZieGcMDYwNJfJtIzAVT8kuhuV1UIjp28U_7kv24dgLsxlf9kQ1grbUkKqCyG_ZC0Drf_w39ZdxaZEW4UHcDX0I9CJbEhFUpFnX9D4psHiOdSlCcQL_CEZTPts__y7RVdgROWIc3jajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCk-wiqTSZux7UF5C-9kOCwfmkX_v8sbh6r7shhnvikbi1vAfRB5YnvAohYGE-iMybchHbRvjgMd9Rb0WmFy5q03VuS5vfWhzdLgvEec7-zShl4x_AiX_3Ve-O5IquJql0xFpbdR6fZutpcUNQzkBXip8KtFKRhiM3L4ltL9JBWS7cyFNeC5uG2-hJ2sZMVOCpSptYzoRiV63rPEn_P4_pGqHwm2g3HgVSAwilYKXyuZ-JgGequM0CTBATd4ud6_pOkaF5Sy-cKnOqvi-XFEZkpANMyd61gtotUGZwTt_X6bPk5F5ft5PVVAUeX918ev-T8nzfVuerF5MTL4BEmSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UivdwTVqT-OJik0cbz3-CJ3fTJE46pxdMYZ-UiwmBmuiNekZxR3L_yK1en5VjeEtACA-LMpr1y9pcVlp1YlvlBI5YtU2QdGgyXX330-t0s_Bw-zaxvJNOOW7RFocGUzudOad0xTn3Kv0exha0GVhz5hexYtL1QCTKun6UBUAPjdrm15aMzv-1L_6yRRAbHdVIEo4nuRSuh5BE0oI1UjyKK_WdDoQkh2snCZ_hN4OpE9wg4pPWNQFtFB9mByTs-9SomnwpBiBaRPTVHcElfV5WhbXBYHg0BsmBpn85TeqZl0d3_bS82sk42O1eka3TPVEnOIuKJoo7y5oET8K_ai97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CeNK31-jOD0052pE880sFbMVPQmlZWtP-fOx9pTtl_1N1CqpHY25z-zoLUS1HKgYkGPO2SW9QpeQs7BnfAtALG9jIvN82vFoxJeLxfYHwowqIPPf0vTHBsyuKlVOJg5c9h_5x5guMfGd6lnUgRdNF-TaVa9FotykF9ZYHy3zLsMKDDeZHNz05d1JmwGPHszpG9DEyE8O97JkbSKEhvSsHO3Gbe_Z0xBTxUIBmvjLdsDz-IRlwOP1pe3DnwZIIogV5KGPhCihaAv574WjuQT3mEhj4dhjwA6mIkEu2wpv2BTfoU3XNgeh2Tpz3zn-6T-5o2VwcLeJnTrkalkl16ANgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzi3AfOx9pbsTpnp6WJ9o1sMgGNkh0HlhQF6ooFO7GpkYweqNuWXZAgPOM3FBshNacMKpKzAW2qAc9vCvSO3GRDJqn0gvDbg6zn1banoPemzQa0doErV4vUgyLkJcLbIZ1Q7CPBryzC8s25YvFV8LfMHeXkS2fFC5IIUOmPu3adFve8VLqXmUHiGVsHXdBEpXlQLeFerX9qMiovxYPmKcqTnPvViUxgrx096w0tEzhP7SdAVeH8Kok3Rp_oeCbZsyYZcdczMDzYSB_5F53aTHaRBxmUekdDV8RAz4vkRhbhWq2BTw_7rmmTeQqCQr0gpcpN--qyS1B8tr8lNZUP1qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
بیانیهٔ سازمان اطلاعات سپاه دربارهٔ ترسیم صحنهٔ سرنوشت‌ساز مبارزه با دشمن خطاب به ملت ایران
🔹
سازمان اطلاعات سپاه ضمن تبریک میلاد پیامبر اسلام و گرامی‌داشت یاد و خاطرهٔ شهدای نبردهای قهرمانانهٔ ملت ایران با آمریکای جنایت‌پیشه، بالأخص شهید خامنه‌ای(قدس سره)، بیانیهٔ خود در خصوص ترسیم صحنهٔ سرنوشت‌ساز مبارزه با دشمن شرور را خطاب به ملت شریف ایران صادر کرد.
🔹
در این بیانیه بر ارادهٔ خلل‌ناپذیر برای انتقام خون شهدای عزیز تحت رهبری زعیم عالی‌قدر و امام مسلمین، حضرت آیت‌الله سیدمجتبی خامنه‌ای(دام‌ظله‌العالی) تأکید و اعلام شده: با امام خود عهد می‌بندیم که تا آخرین قطرهٔ خون، مدافع مهم‌ترین یادگار امام شهید، یعنی «ایران قوی» بمانیم و برای پشیمان‌کردن دشمن و رفع نگرانی‌های ملت عزیز ایران لحظه‌ای درنگ نکنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458528" target="_blank">📅 18:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458523">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nX1tociwiau3fnHXcAPVRE7lkecKOIzdS80l1k_rGwoMJyT_q42ad2Zpmw0dtYMQXHsPS85kRogiPtYNvWrop8_4xO_ROp5Gnt-Bvtr98nfwdRHLAnASnQwNH2fAyW3yjVJ4WchaRm40k2GZSnF_etirqxziKpaz_3iJoCNq_JC9bSDCdEi0vVgKNo6K2l87-gpj0VareOLUcN4IY5XeTpXzXj27C72tL-Oir88v2COonf3b5dFsymufvAFk-z9_pF58Apa1gh9fBXTBIKXNA_kmsrlFAiMeFtfBcAJZ0O0YlzPTbKqoCW7kCkLn72uOgMWS4qywanBAPrfKnPpcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuMRut3JvPyrqlr1FTGK3fvO3DeVrwRKYlH3zoP6DkN9yjrFV2x3hAnwBJI-nfopdLi91fasqgbj64IDa0hvBrKjaDt6qx-Dg-4TF8KhwFg48uUJSkLqsIOrQZRkgx9OxZst7jN0Ddj5n46Syfu0snGC6nagHglNn_Od3j-5_fCKlmPzmYiTosKTVh4sjzK0dIHjXrlOhPg0npXss-Kdy0GSZAMHxNu8VP04-yxbflvQ2fHtSPdRUR9m-as7H5y6J95nrKwOkceTqH4qGi4-CTuBNAtsQMmrRGovx31MPMyyDLSQXjzr9_1Gsha1ohi2qKVWhga-HNNY-dOw7n2FOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Omdr56eSafTJxLhQBndiWtkUrBpbRQ45tjvlIJdM3bZ4YgcP-69STknt6a4IUJZx2Luxu6Mxgn8MkI-eJDOq-s14LRb5ttH9SgNNoVjY4RHNRbT0vPiyAueZZeITkA7NhNrRbK4ZxKDsxKHvz2E9VeaZFQncuBXmDRYKVuQuulcH0Kf93W1awTKDkixgt28bPGZ--BaPn2h8xht-b2Ye-8bdELjOJUz_biInK-ItjJfT82TUbqcR8p18hrmJZZn7syr8YF5MQeb5huMj2STChvap8rp8yflRK2tGzf8QZWC6we0YVXbM_LH5w-CGWEH1Zgnc_QHjN8856DAMIfLAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJKehjM7Wn9hbNsuT_CbbnXevnyK45qQ2kiioCLkiT-e2ehd11pBPtdjjU_vriRa1qHJ4Llvxt24Trc2qYDr4nacOfo2-Xsj5pdKsKyk96WhOSI2X_1XtSACWJRGsKiTpcJSvEvrv92GKy-M_MUhf7wpxCuyALCZrU7b-zIc9NwOvV75-mX0V11ZjFOMo4_jGTdrbrcPldcL9UG4fINFZ6tMZO_GbAOxCvRtY_ZAWMLKIZvvT6oE9lHqERADBUDOZrmCPx0AJH9iWYi7V3og393xS4ymAulCmBKKFGI19GosOc20gBfLwKPYY7aAl7zRJpZs-au0jOc-eBybdaSmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7Vj1fcclhK3ib8mlEikITNxledNN7_bK9LIVgwT2XxlAP1yEtrROL3WtXaBZdx7oEWevLcNWw1q6iwGIeOuKZfvb4toCYXj1p3v7i2vJOocajnByBP1bteQRy3Or_528ImHqeZ9NC9plHUuM3IRMrTyKHxY_2hWufGtRhDxn0WVMc83ONJs0QIu9lrxAiP2MSKSn7kEnb_JSPPLi6KcPdt-dYvbfUtcWOE_bhswSSjOcGpJftXdrKjZUGptJWeBLNQKxMNQKBtcrP4lt8ncjMOt0_9N3q_URpR6UTlnVyJTnex7huWzw8o4mAhKx8zCcjk6ROB06WOqe-GSup5xyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف در دیدار با وزیر خارجهٔ قطر: ترامپ با محاسبات غلطش ناامنی دامنه‌دار در منطقه ایجاد کرده
🔹
قالیباف در دیدار با محمد عبدالرحمن آل‌ثانی با اشاره به موارد نقض عهد امریکا در اجرای یادداشت تفاهم اسلام‌آباد گفت: دولت ترامپ با اطلاعات غلط، تصمیمات غلط می‌گیرد…</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/458523" target="_blank">📅 18:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458522">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3G4bQ05wZxi9P7BtQIVVLKxxKIT0Vhi-tI5RAZTftfub40mHRjK_B9JkKyx5ylDerVPlpI_z881Z3RfodH8JpfHdG2urs62ltx3E565eP7obRlsyy3K8E25jRm82RMM7UICN6isdHKR5jiY_X5OIIsZ2yw3PPTuSH2R-cnwHxrC4lhXdVTpQhCOkLwLENxK8BNkSSC0JPX0mzU5mi0sENRk2LJcBR2Um-VZnZCkCeMpLS0n0WHIaqsIQCG1rzaA0oq7y3oT3yXPrgDN8Zwtf4koqX9srgqcYW7-H8wesZcXrFH7-nci_GADVjXGjNydJ3BkAx5glVGXnHn9w6gKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایزنی وزیر خارجهٔ قطر و قالیباف دربارهٔ کاهش تنش در منطقه
🔹
وزارت خارجهٔ قطر از دیدار وزیر خارجهٔ این کشور با قالیباف دربارهٔ تلاش‌ها برای کاهش تنش و ازسرگیری گفتگوهای تهران-واشنگتن خبر داد.
🔹
وزیر خارجهٔ قطر در دیدار با قالیباف بر لزوم ازسرگیری روند دیپلماتیک…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/458522" target="_blank">📅 18:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458521">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9MG5Xi8qa2W2XBMdmcwcsRP-DHolV79T59rheHHg-Q1u3J73DixbDX1da0Qc0jSdl9ZH8Ecb62Bt2Or--wBoyf5PgiNE9nZOycEPwD9igCR0dEmFKFLeTzUcNHpjsMAiAiQNOM5eljlgBS8esbi_1-bXpjjNxyDm8pNViqbg0GlYF7eMGw4RRPJIbut5Mzp07ov6kkqzQ66yRoX09PLowi2TcOHoVI6stJ5zxCNg9sVBxXSOzrTCEJAsPSAyKyHiX-qgtFNK3jc8hSnk_bExB2VYmyH0z9k8tTR0lgsvOm16CMasTM86IWth-C9th7ExwCx752E-FB0ZyoycueGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روایت دوحه از رایزنی امروز وزیر خارجۀ قطر با عراقچی در تهران
🔹
وزارت خارجۀ قطر: آل‌ثانی با عراقچی دربارۀ تلاش‌ها برای کاهش تنش و فراهم کردن شرایط گفت‌وگو رایزنی کرد.
🔹
در این دیدار، دربارۀ مذاکرات مربوط به چارچوب موقت پیشنهادی برای ایجاد یک مسیر موقت کشتیرانی…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/458521" target="_blank">📅 18:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458520">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQpVNiTR_84fZmuy95sa6EWpkx4uhzqPscy4poPcFRp06-63LevVYutY-R-xDGVzu_NlfQzkPjvnIEPUXsuqyyiY8pwVSt7mBHl3IcVPwixGHMM2RDbnYs5TCod8mwr1hVDCKEth3LVseTlN9ZsADx_nYj3MSN_TQh3w7xL0w5w59h5mZ7O0od-649vSi1XgixGmMMmqk9f-QzGbta-kI05RBiMcdhGC39M6DfuP5OF66i30sMtS4X8y_1CdEX7m4AJStVhjOEDiP4Y9-rhfd6Pn1uUiukgXN3ty4RsZO7IgQcwVxXxEn4KNHkUA_5FGTrPVcquyz0zk4DwhP9vt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چماق محاصره و هویج مذاکره؛ آمریکا از ایران «آمادگی» می‌خواهد
🔸
کاخ سفید در حالی از تداوم محاصره دریایی و فشار حداکثری اقتصادی علیه تهران خبر می‌دهد که همزمان، آمادگی ایران برای نشستن پای میز مذاکره را پیش‌شرط هرگونه گفت‌وگو اعلام کرده است.
🔹
کارولین لویت، سخنگوی کاخ سفید، امروز (پنجشنبه) در گفت‌وگو با شبکه آمریکایی فاکس‌نیوز اعلام کرد: «در حال حاضر هیچ مذاکره‌ای در جریان نیست و این وضعیت تا زمانی ادامه خواهد داشت که رئیس‌جمهور احساس کند شاید آن‌ها (ایران) بالاخره پای میز مذاکره بنشینند.»
🔹
لویت در ادامه با اشاره به ادامه محاصره دریایی ایران گفت: «رئیس‌جمهور (دونالد ترامپ) البته همچنان همه گزینه‌های ممکن را بررسی می‌کند و محاصره دریایی که بسیار مؤثر بوده، همچنان برقرار است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/458520" target="_blank">📅 17:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458519">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceu67zBCwtruQ8FFJBx02x2zfc-Sh3jfzPqYtzbF0oAKUxqOY91YKS-AZLUf7bkf8qv0XCEJHf_xfUi3liB_JNOTxtHEgMjRn8vZmUO2Tfc_WteoDl08_elA0ohqYvuk_ZFXl1OrA6ugl2Qo4C8q180rMQ5-8LczSnS3EiMBmz9P46sgtadpRYy2EEsQt_9hp2KY2ewbLY7R8PTKNJKGmVRw-lpItssDfeuEEjY8MVVvsxAIOB7bRlPxTdI_Fi8baKazqhyJl9zmjphZDnOuYWZdX0ClBMyYVTU-WY_GqOwenFzQxJzBBwzSyM-O8GKEXAHnShrbWRN8mnbDsvZCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔹
کوروش اژدهاکش، بازیکن تازه‌وارد پرسپولیس قرضی به نساجی پیوست  @Sportfars</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/458519" target="_blank">📅 16:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b8e26657.mp4?token=r6kBO1MX__kkvTmQ2h8eO_MtdcT0q_LyuoKFIz19tKBLfaoxyoSV776iZCpBPtoucHzO2vfvsfL-WG3XmRKaoyHANvK16ZwJLph_YBCt7pPQvdx7TgepW092DuxaI8nJo_6fV7OtVrHgy28sS11PpwLToNN8vftUNw1SGVeGfmYPo6TiBTeQ6Y2VgI7ohXpbAvDFH61faZbbQkxLhSJHPDTz2CbXUsIgVArxf2zslP3yh8T-5zAyNprMr4tZ03v4IVzk607QHYNP5WjOQywxyFR7i71orPFkauweNS4JStpi5mJtn2Zz8SZklkL8ZFaA2Y2amMl-MzzWsqJY-9O12Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b8e26657.mp4?token=r6kBO1MX__kkvTmQ2h8eO_MtdcT0q_LyuoKFIz19tKBLfaoxyoSV776iZCpBPtoucHzO2vfvsfL-WG3XmRKaoyHANvK16ZwJLph_YBCt7pPQvdx7TgepW092DuxaI8nJo_6fV7OtVrHgy28sS11PpwLToNN8vftUNw1SGVeGfmYPo6TiBTeQ6Y2VgI7ohXpbAvDFH61faZbbQkxLhSJHPDTz2CbXUsIgVArxf2zslP3yh8T-5zAyNprMr4tZ03v4IVzk607QHYNP5WjOQywxyFR7i71orPFkauweNS4JStpi5mJtn2Zz8SZklkL8ZFaA2Y2amMl-MzzWsqJY-9O12Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار و گفت‌وگوی نخست‌وزیر و وزیر خارجۀ قطر با عراقچی در تهران  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458518" target="_blank">📅 16:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458517">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2cd79445.mp4?token=J3LyTywSg9nD6rNAQnsqeYlyc33P45qP6IfWpIG73FwU-YLLME8A2aAx3ootM0NKVTk9oIMAVetGtPi_x1XKONSOhdCf00q_lVEiQ-tXshOFX1KOMSkvNtWQqx3IK-TX5ufPdwJSocpIEpUJfir2h25W52dsWe35h9Fb07U98HlbmHdHgiOKmYSBvQeo8CrR-7gsh6O3WoFk7ziNTZK2JFdfPDoerat77yQ03H_S07yEHMzzVELdeWc27U-NobjOo9z0cvTMZs2-k6Co1mqQX9fu9iqosf0-LxECV0e5MaXuPj9OiOX9FHpTmCSOG66QulV28RqdIu-mi8Qe5QjWw31ZoX03nsruCr0ttGLZCuPtA5rY4Y1buhC54-qq0Whx0f5fxUjW1DdSzW-mMkUaA_ds0d6w3xp1XATJqE3YWYadKIBmGy7Mx2D2Ovj9W9B0X-319Kb8P8sLI07hLUch8m0LWor93gc1PXlKkhNCopq11qPOHBi1Vuy8mAVxeU_Zz48eo-AN774etpv6T9N4X26DYjkmxuJpc_3UEmAG2IYSAmfdqPcPX5GHS5SuRkz5p7BvZ7BRYraQcNUwmRK-z0SovP4NKMJKKqBzDlaDDnZEtmUwhOLd40for-UhwexcZMqkV_tr8c7ItdBMlr8VDiMZo5ewBs6jx1PQdaZxpQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2cd79445.mp4?token=J3LyTywSg9nD6rNAQnsqeYlyc33P45qP6IfWpIG73FwU-YLLME8A2aAx3ootM0NKVTk9oIMAVetGtPi_x1XKONSOhdCf00q_lVEiQ-tXshOFX1KOMSkvNtWQqx3IK-TX5ufPdwJSocpIEpUJfir2h25W52dsWe35h9Fb07U98HlbmHdHgiOKmYSBvQeo8CrR-7gsh6O3WoFk7ziNTZK2JFdfPDoerat77yQ03H_S07yEHMzzVELdeWc27U-NobjOo9z0cvTMZs2-k6Co1mqQX9fu9iqosf0-LxECV0e5MaXuPj9OiOX9FHpTmCSOG66QulV28RqdIu-mi8Qe5QjWw31ZoX03nsruCr0ttGLZCuPtA5rY4Y1buhC54-qq0Whx0f5fxUjW1DdSzW-mMkUaA_ds0d6w3xp1XATJqE3YWYadKIBmGy7Mx2D2Ovj9W9B0X-319Kb8P8sLI07hLUch8m0LWor93gc1PXlKkhNCopq11qPOHBi1Vuy8mAVxeU_Zz48eo-AN774etpv6T9N4X26DYjkmxuJpc_3UEmAG2IYSAmfdqPcPX5GHS5SuRkz5p7BvZ7BRYraQcNUwmRK-z0SovP4NKMJKKqBzDlaDDnZEtmUwhOLd40for-UhwexcZMqkV_tr8c7ItdBMlr8VDiMZo5ewBs6jx1PQdaZxpQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: ۴۰ درصد ظرفیت آسیب‌دیدۀ پارس‌جنوبی به مدار تولید بازگشت
🔹
آواربرداری پارس‌جنوبی به‌طور کامل انجام شده و فرآیند بازسازی به‌صورت منظم و برنامه‌ریزی‌شده درحال دنبال‌شدن است.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/458517" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458516">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2111b7992.mp4?token=uVgDfnAmR8dSTGlYgH8ficrTFh0zuMfFiN2Al9ECJvNAjgrGv2SIeBAI7lBeiVAfniJ8s733fcDy1uB-yxY6oNFYQOQJUp85t6Ch10Pj-9t_lF1folfmHr9yq_AcMI4N6tiKFu6hxlWy_XqGYw2qWAKj5QsHENSYpPtr3oSm14yabTEHHuQ_hoiWZ_RynsBDbyX1yJwhri2ybnN2nPZju2haWUrQYAPWruDGwM6HeEUvkipFq4vFq9L0kc7H6BVWjuh1xNWnvGatrl29HSpyOZ7Fnu-J7fkrCiP0PVyISBKGDHgm2WFhD7G4U0hd0gPmO2dmSn25QHOzA0FYUnP_KEJpbnLx3bjteK_jIAVrV-3vh2o6OvXh2B9za1lYjtuOhU0XzwHkj0tfK1BBlq2ak60xIk-1RiwTcTUYj46z8bSk-GDXNunjinehgnBSytfmYWauCm2wZQH3uc9e3QSETMCT3i4hXU3g2-0NUqwOmKVTcUkkzB5iehcgNkyG8Jf1-FY_Yv6Yhf66Fyec1cVFHw84dsIWcgkHYmkTvbZnCbyefqqFL1OZqqo1qfmvDBqmoJMV_C9Dkfcpm83QqofYaUhDaK5NUfc_LOJbF79mg412-OdFzgB2g3mcX-kbzYFgNYu1p102Bo8O9AKaqFhy4omaQvuEP7J-fvUJqMqzlF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2111b7992.mp4?token=uVgDfnAmR8dSTGlYgH8ficrTFh0zuMfFiN2Al9ECJvNAjgrGv2SIeBAI7lBeiVAfniJ8s733fcDy1uB-yxY6oNFYQOQJUp85t6Ch10Pj-9t_lF1folfmHr9yq_AcMI4N6tiKFu6hxlWy_XqGYw2qWAKj5QsHENSYpPtr3oSm14yabTEHHuQ_hoiWZ_RynsBDbyX1yJwhri2ybnN2nPZju2haWUrQYAPWruDGwM6HeEUvkipFq4vFq9L0kc7H6BVWjuh1xNWnvGatrl29HSpyOZ7Fnu-J7fkrCiP0PVyISBKGDHgm2WFhD7G4U0hd0gPmO2dmSn25QHOzA0FYUnP_KEJpbnLx3bjteK_jIAVrV-3vh2o6OvXh2B9za1lYjtuOhU0XzwHkj0tfK1BBlq2ak60xIk-1RiwTcTUYj46z8bSk-GDXNunjinehgnBSytfmYWauCm2wZQH3uc9e3QSETMCT3i4hXU3g2-0NUqwOmKVTcUkkzB5iehcgNkyG8Jf1-FY_Yv6Yhf66Fyec1cVFHw84dsIWcgkHYmkTvbZnCbyefqqFL1OZqqo1qfmvDBqmoJMV_C9Dkfcpm83QqofYaUhDaK5NUfc_LOJbF79mg412-OdFzgB2g3mcX-kbzYFgNYu1p102Bo8O9AKaqFhy4omaQvuEP7J-fvUJqMqzlF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حیرت تلویزیون موساد از فاش شدن ضرر ۵ میلیارد دلاری ایران به تأسیسات جاسوسی آمریکا در عربستان!
🔹
شبکه اسرائیلی اینترنشنال: ایران با یک عملیات پیچیده توانست مقر یکی از دقیق‌ترین و حرفه‌ای‌ترین امکانات اطلاعاتی CIA را نابود کند!
🔹
حالا ما می‌دانیم بیست مرکز اداری فرماندهی و لجستیکی مورد هدف قرار گرفتند.
🔹
حملات ایران در محل سفارت آمریکا در ریاض انجام شده؛ جایی که در طبقه سوم آن دقیقا مقر یکی از دقیق‌ترین و حرفه‌ای‌ترین امکانات اطلاعاتی CIA بود.
🔹
عملیات به‌صورت پیچیده‌ای انجام شده و توانسته‌اند از دیوارها عبور کنند و بعد از تخریب دیوار، خود تأسیسات را نابود کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/458516" target="_blank">📅 15:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458515">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-bGQXaj9-G3EriPnvHGkGfOJY1TRzWgWw82JGybcxNGBlocVqYr0rqLVH0JwRLNJ0th5Jm49ibqQQZvfktLwAUGr3LDo8iiiyCP3tziHYEOh5i3niWoT4x1V69llMuhdCsgwqO9krT_05FhXy0Z-bO7gl9-rzQDrriPsDWeSYo3QlvkmMHtxETV7BNvEW_Ba4nEiFAwdT7iV5BDh0VwMfQVX7sxQHxlREK8wk4eRsGkZgBDvot0u2iHiBxyA9ieQxbMWt2GKdHu_Yj54N0wVAjU4vhqpLHf4hiNFD7Gp7lXjymj-PNnjEgUdxZ6Gtu467A_Z5ntFkOACK_MwTFEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک محرمانۀ موشکی ایتالیا به اوکراین
🔹
طبق گزارش روزنامۀ ایتالیایی «لا رپوبلیکا» دولت جورجیا ملونی نخست‌وزیر ایتالیا مخفیانه بستۀ کمک‌های پدافندی را به اوکراین تصویب کرده است.
🔹
این بسته شامل موشک‌های پدافندی «آستر ۳۰» و همچنین رادارها می‌شود. آستر ۳۰، موشک پدافندی ساخت مشترک ایتالیا و فرانسه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/458515" target="_blank">📅 15:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp3DemCBkw94AiENmMw-HYx_XTt4yMLKPoe42rxUsnaK0SdOU2OwQDSjQ43OOatiS6_V52Mzeb94y4n5Dma2h0WsSDFetbncqi2murhovVe3IU8YkwfGFGQvyH6rjLqaK5njOb9D3a5RaE30UyvEEI3WDBRSQFwPtvYwpmDahI7ymGGrAfU_PSQgVQFihS6JuWkKO50nbtQ69YZ56WbvZWtAyagZulcoAqQYtgDL4oSa_RzU55q8Y_VOi2NnWuuE7nhy8NwbD_Ie0wFhcM9zppcWPbk2AkJ-zmwNoZ7d50Fzt1F-LuqVmruCBO3HfRus50lm6RV5q0-crhw6utTp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشین، معاون رئیس جمهور : قدرت یعنی «حق انتخاب»
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، قدرت را بیش از هر چیز در داشتن «حق انتخاب» دانست و گفت: کشوری قدرتمند است که هیچ‌کس نتواند آن را در برابر یک گزینه ناگزیر قرار دهد.
🔹
حسین افشین با اشاره به تفاهم‌نامه اسلام‌آباد تأکید کرد: اسلام‌آباد برای ایران یک مقصد نبود، بلکه انتخابی عقلانی در میان گزینه‌های پیش روی کشور بود؛ انتخابی که از نگاه او، معنای واقعی قدرت ملی را نمایان می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/458514" target="_blank">📅 15:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458513">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTechnolife.com | تکنولایف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prr8niWb92jWtdXftRf6wrZ39oci7VG_ifU9Iq2qVBnXBufx5vJSEEM_Usn0Uz8Z9HPcRrXkAf-i5vIupDHLS8ySoQzb35v4xMN5MeVWA6j8jQOAEIxVYJ-jrD4WquwkDt52rIVPccjhlk1vnk_hJfJ3Dmg-iZd-KTS3H71Wuu3yG5X6Qqt0BluXmY5Y-cB_OonEQnLPSjgtnDwIvBEsDlwRKO_tcqWopE1d4t7KEdHj2y3zr8a47TSYkwyrZOmBQrgh95lFl0t2q9v85TobiOo_wVK8DLZ6FxHJ43Gkrr_8cW6qUZbYiCww2IyL_sZQDZw-zqGAM4Yt51z5X0vu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یک خرید؛ شانس بردن آیفون و BMW!
✅
تا
۱۰ شهریور
، از تکنولایف با تخفیف‌های ویژه و قیمت‌های کف بازار خرید کنید و شانس بردن
آیفون ۱۷ پرومکس
رو از دست ندید.
✅
اگر پرداختتون رو از درگاه اسنپ‌پی انجام بدید، علاوه‌بر قرعه‌کشی آیفون، در قرعه‌کشی
یک دستگاه BMW
هم حضور خواهید داشت.
🚘
http://tchl.ir/HNgrp7
http://tchl.ir/HNgrp7
http://tchl.ir/HNgrp7</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/458513" target="_blank">📅 15:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458512">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/458512" target="_blank">📅 15:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06bd6fc33.mp4?token=IdBSUqpvsYtG3HqRGGUKKcjQxi1LZ3YCiE4OwqzxANyJZ84f134rhJDlJ18KMIdbpCb8ERsvdUbWwTL5qd4pC-lqnmToQY8t90qxDGikg9CM-n-vfiiJ-4_iBNDxbZwliCjWrsrmwbgkloQksf2FMAuFZkDGgvXhIiszSMRFwDJmYW5vfG8KIrwa_FxLgfmOzcXDqCqa5lMIqXHK3kmlW7ToppQT8uoffZc5UgYwv1ChMHPc6jFPPsIdxLi1XTbfRJa7pMsjDlt2h9b2xbvGb5EXA4_umCg-PyWeF_OKtQ9a-0gyWrWwv1rdC9FxlO_h4E6cRe0BEOeUpv02KETHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06bd6fc33.mp4?token=IdBSUqpvsYtG3HqRGGUKKcjQxi1LZ3YCiE4OwqzxANyJZ84f134rhJDlJ18KMIdbpCb8ERsvdUbWwTL5qd4pC-lqnmToQY8t90qxDGikg9CM-n-vfiiJ-4_iBNDxbZwliCjWrsrmwbgkloQksf2FMAuFZkDGgvXhIiszSMRFwDJmYW5vfG8KIrwa_FxLgfmOzcXDqCqa5lMIqXHK3kmlW7ToppQT8uoffZc5UgYwv1ChMHPc6jFPPsIdxLi1XTbfRJa7pMsjDlt2h9b2xbvGb5EXA4_umCg-PyWeF_OKtQ9a-0gyWrWwv1rdC9FxlO_h4E6cRe0BEOeUpv02KETHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان شدید در مکه
🔹
طوفان شدید در مکه مکرمه، همزمان با حضور زائران در مسجدالحرام و اماکن زیارتی، حال‌وهوای متفاوتی رقم زد.
🔹
زائران در میان وزش شدید باد در جبل‌الرحمه برای حفظ تعادل و جلوگیری از سقوط، نشستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/458510" target="_blank">📅 15:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بازداشت
۴۸
زمین‌خوار
و
انهدام شبکۀ بزرگ جعل اسناد
🔹
مرکز حفاظت و اطلاعات قوه‌قضاییه: یک شبکۀ حرفه‌ای جعل اسناد و زمین‌خواری که با سندسازی غیرقانونی، ده‌ها هکتار از اراضی شهری به ارزش هزاران میلیارد تومان را تصاحب کرده بودند که سرانجام در چنگال قانون گرفتار شدند.
🔹
اعضای شبکه در صدد بودند از طریق اخذ انتقال اجرایی، مالکیت ۶۷ هکتار از اراضی مرغوب شهری به ارزش تقریبی ۱۸۰ هزار میلیارد ریال، به‌همراه ۶ قطعه ملک دیگر به مساحت مجموع ۴ هزار متر مربع و ارزشی بیش از ۶۰ هزار میلیارد ریال را به‌نام خود به ثبت برسانند.
🔹
در نتیجۀ این عملیات، ۴۸ نفر از عوامل و افراد مرتبط با این پرونده شناسایی و بازداشت شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/458509" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3755aab14.mp4?token=ohpv9OlUucsuYlJV-QppzQRMJHLjiOd8uaP0dJqXH1_19sd8RJq1s3NU4bsC2LVaXawecu-bym8yYE6Z_V85fvII3rcXmlCb3rKhRocX0pzvZ1w6aQdJzELm14gouynFLcK-PAlOF1VTP-g6Xh4V8jn-FU2gDpeOKV1Ei0mChwDwlrFl-kXszh0Hy0iDKgLmsAryDyoyJ191B0GunXM4eABSxYzum-hcJ0lQ1et_USDAvkFootBP3XYgiTxChPGRHWAPkokT972_DtqcC4sJe-abyX0up6URWE93kPS4tiwhZ9nkf-WfatUjdkd37y6_uHrpBrAMssTVsNAxPsvoaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3755aab14.mp4?token=ohpv9OlUucsuYlJV-QppzQRMJHLjiOd8uaP0dJqXH1_19sd8RJq1s3NU4bsC2LVaXawecu-bym8yYE6Z_V85fvII3rcXmlCb3rKhRocX0pzvZ1w6aQdJzELm14gouynFLcK-PAlOF1VTP-g6Xh4V8jn-FU2gDpeOKV1Ei0mChwDwlrFl-kXszh0Hy0iDKgLmsAryDyoyJ191B0GunXM4eABSxYzum-hcJ0lQ1et_USDAvkFootBP3XYgiTxChPGRHWAPkokT972_DtqcC4sJe-abyX0up6URWE93kPS4tiwhZ9nkf-WfatUjdkd37y6_uHrpBrAMssTVsNAxPsvoaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازرسی سرزدۀ بازرسان از چند جایگاه سوخت در تهران
🔹
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی: در تولید و توزیع سوخت هیچ مشکلی وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/458508" target="_blank">📅 14:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKUHj6W2K4lYXfk1N13eo7jx9mHEOw7_2BIuIh4Tv60YVtSAVaDI0Wiqf3MLY9PDetvLI3FwjX2XpfoIxEqPjEwmqlY7V7lcOnKUgCDGHE8Uqw_iSsHQBIOxxJMT6j3BZ9fqA0zOkhDcyolcfSLlnFJ6sMiXp5mM5IMnPU5kT7ESxASQUyq57IuRn7sFBn9i-68pBa-bFdvgXwkKdgE4KVELbRDn0xZ_A90drswg_LgYTsBGiSRzjMV_1bsVlFW2vy0lGghHTOuzsrlMuakcHJQFUHWR0pt6DuienNA6YrWSW2nzjkho3JCtxBtzuegBg7oYSYrxmGflTaQYM_Q3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر قطر به تهران سفر می‌کند
🔹
سخنگوی وزارت خارجه از سفر شیخ محمد آ‌ثانی، نخست‌وزیر و وزیر خارجۀ قطر به تهران در روز پنج‌شنبه خبر داد.
🔹
این سفر در چارچوب رایزنی‌های مستمر ۲ کشور برای گسترش روابط و تقویت امنیت منطقه صورت می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458507" target="_blank">📅 14:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-Lhg2VRX6JF2s7GPt6TAw0YCGt0Xa76_dI-vv_HIT0MUS-WgR2RHCTPPoqDseL5J5jwgNjJZP1RWl68J7U2e910XY-dOWTBq4hKaPvWsKyLgcbOVYJneCJDqDCawXQwNKRRG5wDXc9Fyokg8zvI82w2z9K140yJvkGY5DNADzLRmofkBZ8grV3yPwrPXtW_fjIo6pnddnYOAgQ-1AiQy7gdQGOBLJJ3KvAI4o6EhAqIOe-mp3CbvYoV8DhyQLumzaJ_3DOpXoi2kPBxq4Z-IK_jkxe-3B4bEziMhchlA9x88gsztxIYXfYDlmDeUK7nE9e-l5Npbbaegfq11OtJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تلفات سیلاب در نپال به ۱۵۷ نفر رسید  @Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/458506" target="_blank">📅 14:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار کرمانشاه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869259682f.mp4?token=ntVM9b9sASKx95SzrqfLxdYFZFV_LTtQkEpIjf1qRUgZnE-X3M67aBzoYDCpF1eShyyrRHZPt7NyiymNSrua7T19C6C8FfpScjJpH_dSZj-ZVDH2PA2tOebloNo7zlHnqr8NxHxdBkccluEfYXt7w3g92SKiIkcJf1PuZUp7FT54-z_NXROp8JIdMWmXH50VK4sEOJDfFwtsgzWf4XlOBYSDV1wgbQ97QU1f6_DLXmpsaNjvC6qTHyey9Pk10HZ0A2YDHvbI-0wEfJP87e4DbIbEPFdW5520X196lfZF0Kf1WRiJOx7ReaoCE0iiMTC995LVaRBpnwZLVEuvm7hQwGP4bOOrg5TRljOUAPIfae8MuSFnRVd1xdhQHyKYnGVXmKQeAIOhiNjMSFTz5qonOCXgEVAx8UE1vNd7JSGp7UQZAnZwYYnucq4Op0N4NEwA9dbmX10peY7ZfTirG3weapLAgZMYjnNGDeU6U_xfuji_t0IInsispHh7Y3sGaEmNBhO8_cSebg01o7K0wgsYNvy1vFsZhFb9iunWgTub-kX9IICClqnoFicn9pd7s9zdPdKM1RZMcuTC6uu4zur68PyvA_I3OWYtc43JHuONdIv5WNSaIctm-2ykbk1GZ0Z6gSVD19YgoNdZf3BAilGcGVLHH7YH67mgAZzuI7Op8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869259682f.mp4?token=ntVM9b9sASKx95SzrqfLxdYFZFV_LTtQkEpIjf1qRUgZnE-X3M67aBzoYDCpF1eShyyrRHZPt7NyiymNSrua7T19C6C8FfpScjJpH_dSZj-ZVDH2PA2tOebloNo7zlHnqr8NxHxdBkccluEfYXt7w3g92SKiIkcJf1PuZUp7FT54-z_NXROp8JIdMWmXH50VK4sEOJDfFwtsgzWf4XlOBYSDV1wgbQ97QU1f6_DLXmpsaNjvC6qTHyey9Pk10HZ0A2YDHvbI-0wEfJP87e4DbIbEPFdW5520X196lfZF0Kf1WRiJOx7ReaoCE0iiMTC995LVaRBpnwZLVEuvm7hQwGP4bOOrg5TRljOUAPIfae8MuSFnRVd1xdhQHyKYnGVXmKQeAIOhiNjMSFTz5qonOCXgEVAx8UE1vNd7JSGp7UQZAnZwYYnucq4Op0N4NEwA9dbmX10peY7ZfTirG3weapLAgZMYjnNGDeU6U_xfuji_t0IInsispHh7Y3sGaEmNBhO8_cSebg01o7K0wgsYNvy1vFsZhFb9iunWgTub-kX9IICClqnoFicn9pd7s9zdPdKM1RZMcuTC6uu4zur68PyvA_I3OWYtc43JHuONdIv5WNSaIctm-2ykbk1GZ0Z6gSVD19YgoNdZf3BAilGcGVLHH7YH67mgAZzuI7Op8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کرمانشاه در قاب همدلی شیعه و سنی
@KermanshahFarsnews
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/458505" target="_blank">📅 13:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2035eebd22.mp4?token=UCl5eHMpbKF64DLbzRKJbIgZSaih1GWVz4BOBndrkq7PjhLZlFEzPIGgtqmFcIV7I1Gx--ZuAV0gSN8UwOnUMUiUpIQdC3s9KZf18OYaRBAmvQ12_xVCsk0YLbLffB7cmQGp0CAAg_BFQ-JfIS1YJmjFXK6-Y6DIbRv0euNXymHHxrJrHDljTAGdN2Qod75pUtEPNIYP8QwzPV8B5IY37_qSaSmfhQRRO4TKfytcgZgOb67AOwCG17hDaa1BMx-5_AGE7KzmsSCir-YQHwuNlYpjFSkyRkLlDUTlfFxnVpNlAb1jgXM3XJUIWQJZoKC05g0aYUgRptX-znS6BxBEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2035eebd22.mp4?token=UCl5eHMpbKF64DLbzRKJbIgZSaih1GWVz4BOBndrkq7PjhLZlFEzPIGgtqmFcIV7I1Gx--ZuAV0gSN8UwOnUMUiUpIQdC3s9KZf18OYaRBAmvQ12_xVCsk0YLbLffB7cmQGp0CAAg_BFQ-JfIS1YJmjFXK6-Y6DIbRv0euNXymHHxrJrHDljTAGdN2Qod75pUtEPNIYP8QwzPV8B5IY37_qSaSmfhQRRO4TKfytcgZgOb67AOwCG17hDaa1BMx-5_AGE7KzmsSCir-YQHwuNlYpjFSkyRkLlDUTlfFxnVpNlAb1jgXM3XJUIWQJZoKC05g0aYUgRptX-znS6BxBEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرخۀ درمان سرطان در زاهدان تکمیل می‌شود
وزیر بهداشت: مجموعۀ درمان سرطان شامل رادیوتراپی، پت‌اسکن و بخش ید درمانی بیمارستان علی‌ابن‌ابیطالب(ع) زاهدان تقریباً آماده بهره‌برداری است و با راه‌اندازی این بخش‌ها، چرخۀ کامل درمان سرطان در زاهدان تکمیل خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/458504" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVtQZppx-tfFdBxoUJGaxHuvOIWQDSH8A90ObMCH05wplhbz84UHbv-sWys6Kc2Ki1q_qrXFDHo5Qb5oFoAOF0sfU-925Uw7SjY9xKI8N_vZyM0kHJrXDmuSQbR9VfFNMYusinR_GI4hvaZechIWi1D-tBX5RrGiaoRg0QLkQ_fTcRHYAMfe4x-kyhQcT-q2jQn9PsyHGLWyaeAtQq8g3E_1m3LCGGTD2cVIP0tOX4x2uy2fAmMt-hUoAjTowII01Q5GjBAa3eaeuNYChE_JTyzcoeJFDe4i0tDXUfU5SFON5qTAsiKLp0HXZF1f5Xijuig3EN2e6ac3V5MWcf0kbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: هر ایرانی در جنگ اقتصادی پای یک لانچر ایستاده است
🔹
رئیس سازمان بسیج: دشمن پس از ناکامی در جنگ نظامی به‌دنبال کشاندن ایران به میدان جنگ اقتصادی و شناختی است.
🔹
اصناف، بازاریان و تولیدکنندگان باید با حفظ تجارت، افزایش تولید، کنترل مصرف و جلوگیری از دوگانه‌سازی،…</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/458503" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce098a5fc.mp4?token=BcOD4Wu-eOD_KP243WsUjT6I2TYlj6aOpuwQTEm7dDUsRPG8_3SCFahsICzOQH_Nt-sbmVyW9yUT4GVSb9ECPf79JXBIgDWpSq8sZOB2G6ibsYZJdYu_CDQMzpzKxAs7k75e7vGoHBvtUemVXXURLaWvtGsVaq9o9SufVdgEtsW2YGF8M47AiLxQIIyYaDRFVN4X3hr5wcRVjegnVfbx7A3ruEyWv-NlB55ydvKSbMgIUG0oblYmhiwD5UC9Z2uF0DyboAW79yEkg2Tplsa2JzqSqGaUxRZKfBipz_s1wodWOb23781MmS97KYhv85CqO69uVT0cyGtTrNL6WTgHJQxN3q8snsG53EjfGPY1Iqkzg4qIszZTZAcUg8z_dV6fhDStAjK5xThir31Uz2iSJaMlAQdloSdb0EgZm59jZa1m6o3j2s7fLkSC72fGm0Cj5sDp-sPHYFtN3Mmf0OkeGhD6nG-6oq2uo3_J4cKEbbJDwYIk6xoXOf0pBAjsHISFzJX_ihqN5DJoXjAXZe5MXdqBtrAvDg0hcXqO6ryEPrXDKhH1D2GTJ7GU7tR5bjuuVqv93fVH1iJ4_kP3xNcTO9bbmhqbTsdZDtm8VMd6pqbwUoQg7E300BcLZFK6c7tEywHRgKv5CwTihEmzqA46WWChUstbVD3gF0xWexMpyU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce098a5fc.mp4?token=BcOD4Wu-eOD_KP243WsUjT6I2TYlj6aOpuwQTEm7dDUsRPG8_3SCFahsICzOQH_Nt-sbmVyW9yUT4GVSb9ECPf79JXBIgDWpSq8sZOB2G6ibsYZJdYu_CDQMzpzKxAs7k75e7vGoHBvtUemVXXURLaWvtGsVaq9o9SufVdgEtsW2YGF8M47AiLxQIIyYaDRFVN4X3hr5wcRVjegnVfbx7A3ruEyWv-NlB55ydvKSbMgIUG0oblYmhiwD5UC9Z2uF0DyboAW79yEkg2Tplsa2JzqSqGaUxRZKfBipz_s1wodWOb23781MmS97KYhv85CqO69uVT0cyGtTrNL6WTgHJQxN3q8snsG53EjfGPY1Iqkzg4qIszZTZAcUg8z_dV6fhDStAjK5xThir31Uz2iSJaMlAQdloSdb0EgZm59jZa1m6o3j2s7fLkSC72fGm0Cj5sDp-sPHYFtN3Mmf0OkeGhD6nG-6oq2uo3_J4cKEbbJDwYIk6xoXOf0pBAjsHISFzJX_ihqN5DJoXjAXZe5MXdqBtrAvDg0hcXqO6ryEPrXDKhH1D2GTJ7GU7tR5bjuuVqv93fVH1iJ4_kP3xNcTO9bbmhqbTsdZDtm8VMd6pqbwUoQg7E300BcLZFK6c7tEywHRgKv5CwTihEmzqA46WWChUstbVD3gF0xWexMpyU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع شهید مدافع امنیت در بروجرد
🔹
شهید امین عزیزی که در ۲۹ مرداد در محل ایست بازرسی اندیشه تهران که در اثر حمله عوامل تروریست‌های آمریکایی و صهیونیستی به شهادت رسید امروز در گلزار شهدای بروجرد تشییع و خاک‌سپاری شد.
@LorestanFars
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/458502" target="_blank">📅 13:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdwy6pVh2uXjO_7IMq9XX0D4KRoIvYsSmFP3oBuF1UaOtDeikoeqpB4Mk4T18vDR7GCKnAC1TVBBrrNyeqGThMRiyzW2-YIWfASK5hgcS8tLa7M9J7TA1-pp9Rchw64iB-RtUXIVfFKWa4gQmdER4qDP6LicqTKfXwh1KnA-XW6NfmWNA0nc6FLHrOeScAPNX_a0LU2jtH1dsKWGk5rpHxS5r4TfQGkNVzKXzw6bs_i7WKyqvDUSTWyOOcygFGLQrRZg7yVPrkA2AeLPRQD9dQwQ8UyRJasPxe9Nw3tyFYQ7CqZIYd3PZbW_5QSabAqrkjBMlEicsTBBApXOYpjqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف خودروی نیسان با رانندگیِ دختر ۱۱ ساله!
🔹
رئیس پلیس‌راه اصفهان: مأموران پلیس‌راه جرقویه-ابرکوه حین ظارت بر تردد خودروها، یک دستگاه نیسان را که توسط دختری ۱۱ ساله هدایت می‌شد، متوقف کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/458501" target="_blank">📅 13:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">استقلال و تراکتور رقبای خود را در لیگ نخبگان شناختند
🔹
رقبای استقلال: العین - السد - شباب الاهلی - نفتچی - الوصل - الغرافه - پاختاکور - الشمال
🔹
رقبای تراکتور: السد - العین - نفتچی - شباب‌الاهلی - الوصل - الغرافه - الشمال - پاختاکور
🔸
لیگ نخبگان از ۲۳ شهریور…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/458500" target="_blank">📅 13:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458499">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRQHCQMwIpADBOX4QgAPMHbZllWv5e_cWWIjic4QPJ6DgYZhGLxDTTIjkbSmtqt7y1VyceAZ0olF9UIRPUi97Rcl2_vbFdnN90yQRO7HJ5sgq7dS8MGO0EEcJO2FheIzu0J7479H60v9h-exFlJ5vvqID7QzWu4hR1rSZ2zmtLlvGmRbD1uaZDxA5UY6d-Sw4nF2X6NxkFLTHjrKs_-DeJYi48zPfjzE8bg8HSzjLZQMWZgLMHjt-o95GZmD8mSMEm-_BQmWvsPmvOYSTpBj6JjqV8vUwjNc9YzOgp6Sl-xYZ2x-Q_5P58D0l3BVtpVM5GXw8pDnVy0l__ztM0M88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ارشاد: طی ۲ سال گذشته ۸۲ سینما و ۲۴ هزار صندلی به ظرفیت سینمایی کشور افزوده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/458499" target="_blank">📅 13:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoS0_JZF-8CRAsBA95fuxdqavzHcNi8gN3Io4D-KjMkIXT9dlHpfMjG7-YX2DiN6TXGfG_wDQ_q98osJYUuy3C5w8axwohkgBzTGKOMpS8_WjXRR9pNUvtlju0xfpwjNT1_wLhfaC1o5qsdeajHtB1DbE-eDceGWG4pWKQ7tRGhfV2DVHjLbqXPjTF9Ky4pUKI8smMwoqYJytE52lGZJVD0Ovm3UFbDJrpHJvQ5Rd1a35C9pZSOij-nHLLpMK-cyFVskq2QwmWjnfMvsbsWunWNq6m_KMr81CKgcnk6Tq8sTVYhk4Rg1d2qXUl1sXeGo5YAY6vJkYVrpZO-Aevq_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: حمایت از دولت به معنای چشم‌پوشی از ضعف‌ها نیست
🔹
پیام رئیس‌مجلس به‌مناسبت هفته دولت: این هفته با نام‌های جاودانه شهیدان محمدعلی رجایی، محمدجواد باهنر و سیدابراهیم رئیسی پیوند خورده است.
🔹
مردانی که دولت را نه سکوی قدرت، بلکه سنگر خدمت دانستند و نشان…</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/458498" target="_blank">📅 13:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU6v7N6lge9sHVNkKkB3sgwQNPvHv-iOJjwXufhnscnDQsTknib1QSaqaUBQSGX3fWal0QMIPx-w6i8lYre9imcEcDDuMC5FsmX8LjhYK7DaXVwFLcExjGzLI1EUWerPEXLLtfqlCUHgjUTDZfbEdYgZObWGrbEb9wHuy0DTMHOEV82xSNgTuUl6RzmOl8fZUJu1JfkTHcJTPkYRXsvjWtX6zacMA6Z13FBRDB8qilNc1nRzcT_RkSXl-Zy8GP-a5wLAEueP-s0IfQptLu9UQ1M-q3PUL10Jg-DRkhqeL_Ii9I2FYr3IQ0eohdhZkycNmCeyvlJuzlZjY9vWRc65Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: حمایت از دولت به معنای چشم‌پوشی از ضعف‌ها نیست
🔹
پیام رئیس‌مجلس به‌مناسبت هفته دولت: این هفته با نام‌های جاودانه شهیدان محمدعلی رجایی، محمدجواد باهنر و سیدابراهیم رئیسی پیوند خورده است.
🔹
مردانی که دولت را نه سکوی قدرت، بلکه سنگر خدمت دانستند و نشان دادند مسئولیت در جمهوری اسلامی، پیش از آنکه امتیاز باشد، امانت و تکلیف است.
🔹
امروز، در شرایطی متفاوت و سرنوشت‌ساز، دولت باید در کنار حفظ کیان انقلاب اسلامی، معیشت مردم، قدرت خرید، اشتغال جوانان و امنیت اقتصادی را در اولویت قرار دهد و باری از دوش مردم بردارد.
🔹
رهنمودهای رهبر معظم انقلاب اسلامی درباره حمایت از دولت، حفظ وحدت و همدلی و هم‌افزایی ارکان نظام، نقشه راهی روشن برای عبور از شرایط دشوار است. حمایت از دولت به معنای چشم‌پوشی از ضعف‌ها نیست، بلکه اعتماد به دولت برای خدمت بهتر به مردم است.
🔹
در شرایطی که جنگ پیامدهایی بر اقتصاد کشور ایجاد کرده است و دشمن همه ظرفیت‌های خود را برای فشار بر ملت ایران به میدان آورده، مسئولان اجرایی تلاش های موثری  برای اداره کشور داشته اند و تلاش فراوانی برای برطرف کردن نقاط ضعف دارند.
🔹
در چنین شرایطی گوش فرا دادن به توصیه های موکد رهبری معظم انقلاب مبنی بر وحدت، انسجام ملی و اعتماد به مسئولین مهم‌ترین پشتوانه کارگزاران کشور برای عبور از چالش ها و اعتلای نام ایران اسلامی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/458497" target="_blank">📅 13:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3a7d162e.mp4?token=Z3gQDz-V-aE5v9zcAQtQAGDwBOboZBVRHkp3BVyrY3v0qcVSGVk5Z1aMLvy0jYAnma-GaUZqDwrlG8JVsIlJx-MtJ4VGR93pP9lMx6DWoIaBsNINdNBcQOkSwdp0iJjfnnQuKHNJiuofUOsb475Q0a4WAM613LswtNGsxEHXk4j2LPv4Js4KhPFxjpT-biKd84PyUoPY5-FKDho8W1GvWsQYrftaiSMI12qjOjK6TS8KrHH6MI7LFErOVfQ5U6TaJBlA0fiE3iQRtDUv22ydlFVGy40k9zNIQjD8stYJ-jiEC6MsgHwsUEdL3qahjheeCm-kI2r9Fzbxg92vDK5yyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3a7d162e.mp4?token=Z3gQDz-V-aE5v9zcAQtQAGDwBOboZBVRHkp3BVyrY3v0qcVSGVk5Z1aMLvy0jYAnma-GaUZqDwrlG8JVsIlJx-MtJ4VGR93pP9lMx6DWoIaBsNINdNBcQOkSwdp0iJjfnnQuKHNJiuofUOsb475Q0a4WAM613LswtNGsxEHXk4j2LPv4Js4KhPFxjpT-biKd84PyUoPY5-FKDho8W1GvWsQYrftaiSMI12qjOjK6TS8KrHH6MI7LFErOVfQ5U6TaJBlA0fiE3iQRtDUv22ydlFVGy40k9zNIQjD8stYJ-jiEC6MsgHwsUEdL3qahjheeCm-kI2r9Fzbxg92vDK5yyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیلاب در نپال به ۱۵۷ نفر رسید  @Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/458496" target="_blank">📅 12:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adnmubKI6GyRZv1c8eoNm9RRt_EN3DqilutKkFDhxYz3p3UdxMjIQeMa3UOUwZzwFD6fvIv2Ec6RCqv-qIhEvqpYjbqLORAaJPYkQzrLgm2xRiY8PU0fdgiy_HevlLRUOn6_M1LIZaaR3sa3aOLyezUl8kycGxf4kgtbx3HaebMNjHzcD5MJFexX6WtHsqjmZwOOG84g0hopw0BJvPX9HEdNRir1ixwFC-B9z2nGmDFOWhk5jxmMjrxNu7p6RKgsYnwJNZ0BNVUrcXRed9y0OoE9QvP8BN2xw1LgZKbtSx6Kf6DzBPNwRZ5TwCKeNLHEbnv1Nt30uqhYge_S5FHCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
#یادداشت
|
۸ راهبرد رهبر انقلاب برای دور جدید نبرد
🔸
پایان
#جنگ
نظامی لزوماً پایان منازعه نیست. گاهی با پایان نبرد، فقط میدان رویارویی تغییر می‌کند؛ از موشک و پهپاد به اقتصاد، افکار عمومی، محاسبات مسئولان، انسجام اجتماعی و کارآمدی حکمرانی.
🔹
مجموعه پیام‌ها و احکام رهبر معظم انقلاب در ماه‌های پس از جنگ تحمیلی سوم را می‌توان از همین زاویه دید. اگر این پیام‌ها کنار یکدیگر قرار گیرند، مجموعه‌ای از توصیه‌های مناسبتی نیستند؛ بلکه تصویری نسبتاً منسجم از الزامات اداره کشور در
#دور_جدید_نبرد
ارائه می‌کنند.
۱.  حفظ وحدت ملی به‌عنوان زیرساخت قدرت
🔸
نخستین و شاید پرتکرارترین راهبرد، صیانت از انسجام اجتماعی است. در پیام‌های مختلف،
#وحدت
صرفاً یک توصیه اخلاقی یا سیاسی نیست بلکه بخشی از ظرفیت قدرت ملی معرفی می‌شود.  اگر دشمن به دنبال فرسایش تاب‌آوری و ایجاد شکاف میان مردم و حاکمیت باشد، جلوگیری از تفرقه و تبدیل اختلافات به تنازع، اهمیت راهبردی پیدا می‌کند.
۲.  تبدیل اقتصاد و معیشت به اولویت حکمرانی
🔹
ثبات اقتصادی، کاهش تورم، مدیریت نقدینگی، رونق تولید، اشتغال و حل
#دغدغه‌های_معیشتی
، صرفاً سیاست‌های اقتصادی نیستند. جامعه‌ای که از آینده اقتصادی خود اطمینان بیشتری داشته باشد، ظرفیت بالاتری برای تحمل فشار خارجی خواهد داشت. معیشت مردم بخشی از امنیت ملی است.
۳.  بازسازی حکمرانی با محوریت کارآمدی و مسئله‌محوری
🔸
پیام‌های پساجنگ بر عبور نهادها از بروکراسی و حرکت به سمت
#حل_مسئله
تأکید دارند. مجلس، دولت و قوه قضائیه باید آثار عملکرد خود را در زندگی واقعی مردم نشان دهند. اعتماد عمومی فقط با مواضع سیاسی حفظ نمی‌شود؛ مردم باید نتیجه حکمرانی را ببینند.
۴.  اعتماد به مسئولین و استفاده از ظرفیت سیاست خارجی
🔹
مذاکره نفی نمی‌شود، اما
#مذاکره
به معنای پذیرش نظر طرف مقابل نیست. تجربه نقض تعهدات آمریکا نیز اهمیت سنجش اعتبار وعده‌ها را نشان داده است. دیپلماسی باید ابزار سیاست خارجی باشد، نه جایگزین قدرت ملی یا مبنای اعتماد ساده‌انگارانه.
۵.  مصون‌سازی جامعه و حاکمیت در برابر جنگ شناختی و رسانه‌ای
🔸
در جنگی که هدف آن ایجاد خطا در محاسبات و تضعیف
#تاب‌آوری
است، میدان روایت اهمیت پیدا می‌کند. جامعه باید توان تشخیص خبر، تحلیل، عملیات روانی و روایت جهت‌دار را داشته باشد و تصمیم‌گیران نیز نباید تحت تأثیر فضای هیجانی تصمیم بگیرند.
۶ . تبدیل مردم از «مخاطب سیاست» به «جزء فعال قدرت ملی»
🔹
#مردم
صرفاً مخاطب سیاست‌ها نیستند. ظرفیت‌های انسانی، علمی، اقتصادی، فرهنگی و اجتماعی آنان بخشی از قدرت کشور است. شبکه‌های مردمی، گروه‌های جهادی و مشارکت اجتماعی می‌توانند در جنگ ترکیبی، ظرفیت مقاومت را فراتر از توان دولت گسترش دهند.
۷.  حفظ برتری نظامی در کنار توسعه توان مقابله با تهدیدهای نوین
🔸
دور جدید نبرد به معنای کاهش اهمیت قدرت دفاعی نیست. آمادگی رزمی باید در کنار اشراف اطلاعاتی، فناوری، آموزش، نیروی انسانی و مقابله با تهدیدهای شناختی و ترکیبی
#توسعه
پیدا کند. تجربه جنگ باید به بازطراحی مفهوم آمادگی دفاعی منجر شود.
۸ . پیوند قدرت داخلی با موقعیت منطقه‌ای و نظم جدید
🔹
#خلیج_فارس
، تنگه هرمز، همسایگان، جبهه مقاومت و روابط ملت‌های منطقه، بخشی از محیط راهبردی ایران‌اند. هدف نهایی، صرفاً حفظ دستاوردهای جنگ در داخل نیست؛ بلکه تبدیل قدرت ایران به مؤلفه‌ای برای شکل‌دهی به نظم منطقه‌ای جدید است.
* مسئله اصلی، اداره «روز بعد از جنگ» است
🔸
اگر پیام‌های رهبر معظم انقلاب را کنار هم بگذاریم، یک
#منطق_مشترک
آشکار می‌شود: جنگ نظامی پایان یک مرحله بوده و مرحله بعد، رقابت بر سر اقتصاد، اعتماد عمومی، انسجام اجتماعی، کارآمدی حکمرانی، قدرت روایت، استقلال محاسباتی و جایگاه منطقه‌ای ایران است.
🔹
بنابراین دور جدید نبرد قرار نیست صرفاً بازگشت به وضعیت قبل باشد؛ فرصتی برای بازآرایی همه‌جانبه قدرت ملی بر اساس تجربه جنگ است. مجلس باید مسئله‌محورتر شود، دولت
#معیشت
و ثبات را در اولویت قرار دهد، قوه قضائیه عدالت را در زندگی مردم ملموس کند، نیروهای مسلح برای تهدیدهای نوین آماده شوند و رسانه میدان روایت را جدی بگیرند.
🔸
اگر دشمن پس از شکست نظامی میدان جنگ را تغییر داده است، پاسخ ایران نیز باید از دفاع در برابر حمله به بازآرایی همه‌جانبه قدرت ملی تغییر کند. پیروزی نظامی تنها نقطه آغاز است؛ تثبیت آن به توان کشور برای اداره اقتصاد، حفظ انسجام،
#اصلاح_حکمرانی
و مصون‌سازی جامعه در برابر جنگ ترکیبی وابسته است.
➕
متن کامل یادداشت را
اینجا بخوانید.
@rahbari_plus</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/458495" target="_blank">📅 12:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458487">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRHK2mVZwYX4zmdnX-rx0J2k01EcgfwASs1QpsKeVEgrbt4E_5RlVkad0LPfenxBeTg6vOWaToopfW5k3yr-JXGcbJEl9fpDLFCs-o51po8fqLCa7oV14p7tJ_B6ao6OKUCBHhxtJGM9psww9QOxZmM4mzwq935oyVURseJqIXsKHSxNnQYM1HTwzLQVgpmAgar02iA4AwpRURm6ASu8wCYXWsFRhQiy_DtjpFkP75Vwz81rqIlXOEagBtjTUO09V0ysX0HbjbBW094kop8TyQ0bVX1eQNp-8i7EbbTeY8-MK8GXCxn15wl3BcGfI6JOBQgbH-th2KkFRcs1tcYxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opH3kOS3-exocQLim-wK-nS2dIX8DKdZFo4HC-MpJo23oXIXR6-rwwG_F4zMZVz78cogCB2tLnCo-PEfA0yb7KZoL36vCjVgJjnPZ7G4UxRMDRSJc38ywiocvsLEw5wVuBiCt8_KIXhIatbTFlGBybJjCkoZapJ1_-7LyVJr0B2DCwGVAipu_pdgbnDHnqsvoUQisRDq5BwzR21Jpdv1Kmm-kwe-E25sJ3BT66uuCmbLF06e2qx-tGyTn3NSxWCK2IqkFoqNfg4-qOHwSw3m7ZM9BpiSw93ZTcVS4-Sz_s5fvyCsZg1D1KWhM2HGDAVbr5gI7Aw6-yDKxL2hgwX4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxLGvvshIiiMoV3-2h4Gi8CRQ5jP2aLKGn1sb7OPbqaASc14GkHmvXKmA-AIPwR0gtdxYPTd7HbSa7TR5gF9U1NkjslQDfF1X7wpvyaWYdHsyMej9ogidzAIBgfWB6B8JhXIhBijhCW81J-VQLb5t4CJytsSsBTKLzh1yeTNYFeIuqEb9yr-N2y5VG5PC9FW-EnOsCu_jHYhcm82H0zr1SsPKlhXvVOdVXk7kXql_nb1NI8jjchfCPK4QdcHVgXoJ8CKJE8LgK5xI2Bn0CtrX5i6p93dFol85myVfPS8jJ6O8kLOHE7hqHT36ael5NEWr0xZ2whv5e0tAt9h7iijRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdbEH0j0iRLMKD_JpXvuvoBDnqRPn3yPuicuLJRzgV2AhcuzMPe8uDmhohlygD-odKZsST3bOdXokqcgvMRyywglC8fG-IOAfXzmi3Cq-IA2w_zAToYOiXSIqObOhB4L8Utc6jWp8PhwgrmDfTBVAga7h25ulqdNSVTWUimpJWQNrYvmM6tfF6GlQM8WhON6CtINm3AiTvSAgWiGgL3aPB1WzFW0S3WtWfiYPy4Vt8cSJqIka_Uj34oPl4-er7LhgFMcUIXDfz9ImBgx0sDIqB-GTTxuTsyLfyBd9uRC360v9ILTXIV3ga5O0-wKGiDGEzMunSz1KaFDAycu9UF5kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_kkvvmMSRUR7yYST7ub1zDFEUnzRReHQ1T4CHA4KuZ-IAGLf_XvXy4rCHMZ-HJZ6FXskbk6SgS4Y_TW7dmIqenSEbNDBQFcVJPYxHT7VR-UNr-2oWBYqwZk9cMstIdZt5Sl0Ud54Jltm0vC5dtaKLXm2ZiiXa04AmC2bWXs5FZwrdnXV-g7_ekc6PGuiMN5gf6m_eWrjmC4wjx2r7ph6VsCvtX_65EpWZ0e7ADFCc4Xs1q-36o1ptRR6rKJwLHEN1V8kPvmlw7jhJAfeI-RbSzyAausMUh8JbCweU2P3J8_Vw6yHctXRRen3cFmM1427bYJbweATBi8jakpZs1wJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8b-23prYWyboKyFghY2ZXAq_QhOVaHPIJOFYEj3pv5OHlTfYoTccuqnsPgKYfOhmD75mTZkBVxt0feTX5-M4htEeoqD7W7rOykqoxhwxPVW4Xv7ng1Prb53DPGtqXnyKQgo8JWIyIhW8nrDaNwORRT4vsYBKOh9JHjItHKJz3oygyQKZxzkHtLl2entdrVqQKvWREjrSwpEibI2W91ovYJJXokRMDRTWp5B6JQc5otUw7Y_rQKmJYbG3xvwDnL4EYoPJJyQa7cPj01cKPdRJhevIH1fO4a7YnYFEjHzaBw6DGY8zZ1EM99ONYZpl8SpOEDvL5gYOh-Kzwmt1wPJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e24G-dYZ0YoXlrpT6bV99NyuAkhc53fo5kvTa0PHF91sjUjucv2wS30xxDLkDyPv0qM_VqsiYZRDIcIMq5Y9ryrquNYIqZZFObfKG5BmlXp5tffIyvAFBrzEgh1kW7MC_yahFwskGEcvZqncPjl8gp3euMHW043WrDgwWJcvZ62QuhVtqd4kESzbgX7fsDSynOYnBe9e0r8c7LldRwrspXZnPqOiCxsYUr2EyD0RrRcZbixf07gOxc5DtXYKY59hXN7rApt5gdTNxhdjEikp6PsKzci45J0z-SOG56fW-AqyQLixw_WmcKEfefpNq2KZ_qKtJ0QH8BSNlmgu6Jobzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچمداری حاجی‌مقدم در دمای ۳۴ درجه
🔹
هر روز درست در دل گرمای ۳۴ درجه، حاجی‌مقدم با همان موتور قدیمی، خودش را به چهارراه ولیعصر تهران می‌رساند؛ پرچم ایران را به‌دست می‌گیرد و ۳ ساعت زیر آفتاب می‌ایستد.
🔹
مردی ۵۰ ساله که پرچمداری را به رسم هر روزه‌اش تبدیل کرده و بی‌آنکه خستگی را به روی خودش بیاورد، نمی‌گذارد پرچم بر زمین بماند. رهگذران از کنارش می‌گذرند؛ بعضی مکث می‌کنند و با یک «خداقوت» کوتاه، پاسخ این ایستادگی را می‌دهند.
🔹
برای حاجی‌مقدم، این فقط چند ساعت ایستادن در یکی از شلوغ‌ترین چهارراه‌های شهر نیست؛ قصۀ هر روزۀ مردی‌ست که باور دارد پرچمی که برایش نشانی از ایران است، باید همیشه سربلند بماند.
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/458487" target="_blank">📅 12:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458486">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYR471uyVUKJ7ttERrcdFrz73Y0LynKQ_FemRUu20h56bUEb0nc0cjnNNSDOL2bITNZ5H8DOgS6D90FGH1FLGmo02_QmrBYxQTRvW3uMm5u25yW9sCGEQ82pCL0hPgBnb23hZT-zgbbFD-3IxdrTbdOh2ERDrcu2ogZ_bA6FCfLqSAd4kekRWAJ9y53Dr7_Jco4Vdn2sm0fmWAO_GKY6UOU_bjriLZEUJPMHxe6VbxlKTm7PD5CXaM5FUUmO7gcNvj4cLjszv8rT_otiBPK2TP2rv9nvWLmGtbGxwDqBDJwoe2afEGbIhZNrT4cgMgDQp0jpOrKl8l5abfYuY6_6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی: در مذاکرات هسته‌ای با ایران پیشرفت حاصل شد
🔹
مدیرکل آژانس: در تماس‌ها با ایران پیشرفت حاصل شد. مسائل کلیدی هسته‌ای برای همکاری و حل‌وفصل مشترک شناسایی شده است.
🔹
ایران همچنان حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا در اختیار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/458486" target="_blank">📅 12:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458485">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d04ee8e4.mp4?token=a9xw5VMLqi0ykgbLsWybOFL9i8TQSB5M_k2jPDltiMW62tzhAWUojb3Wtxgvy9deiolBK81IL3w89DItVL51m3NgyPB2228OCjCGW3wn7YnYzw-RZEpywhYGY52yktTfr5AMY9kxmV_JM7EJ35-CH0ezDPvDLsxz1qR2U961c0xOZybr9cJ0WhyAUG4CLxHCwiPkwm9vwg-rLQ33UGmbqRu8-bQaauGjw6fO_3hCYPipFHXHVGWpmgOAY2eIRTP-zWbQtKGv-gpbHRUEaGOfz004vAEv0jTnRcsHwp70cMCJFCntDzKFMWU8cOW6MLtBLtcDEdRVTTo-mlchx3Buog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d04ee8e4.mp4?token=a9xw5VMLqi0ykgbLsWybOFL9i8TQSB5M_k2jPDltiMW62tzhAWUojb3Wtxgvy9deiolBK81IL3w89DItVL51m3NgyPB2228OCjCGW3wn7YnYzw-RZEpywhYGY52yktTfr5AMY9kxmV_JM7EJ35-CH0ezDPvDLsxz1qR2U961c0xOZybr9cJ0WhyAUG4CLxHCwiPkwm9vwg-rLQ33UGmbqRu8-bQaauGjw6fO_3hCYPipFHXHVGWpmgOAY2eIRTP-zWbQtKGv-gpbHRUEaGOfz004vAEv0jTnRcsHwp70cMCJFCntDzKFMWU8cOW6MLtBLtcDEdRVTTo-mlchx3Buog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشف ۵۴۵ کیلو تریاک در اتوبان آزادگان
🔹
رئیس پلیس مبارزه با موادمخدر تهران: یک محمولۀ سنگین ۵۴۵ کیلوگرمی تریاک در جریان عملیاتی در اتوبان آزادگان کشف و یک قاچاقچی سابقه‌دار مواد افیونی دستگیر شد.
🔹
محموله که به شکل ماهرانه‌ای در قسمت‌های مختلف خودرو جاسازی شده بود با گزارش‌های مردمی و هوشیاری پلیس پیش از توزیع در تهران متوقف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/458485" target="_blank">📅 12:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458484">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشستا رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7796797d6.mp4?token=RBtcJmKMrmKQGzdcfZq820WEpJAiq4ym2-gIrTxLIiTDKRtfa3l-6rbYGkAVqIXN8VB4M8tUEQh7drnlUH72D47I8WidP2R-pcBL6gOEG6jKUViubK0KkG5KnHComuk-WFLKIYuywGGxDFjCVYS0_aOC2WGqpxXgtrhMuEO-DS-lbdtrqQ9a8pq4NlVAU-pYCs00YKLjZpYazbQwkY4QYMxjsXSBRpRnC9aHfWcfb-GLjqzTLbdOtmOOvhuYRsvts1InqGn0-kJ76U9KpYE8fgRtsb47hW959c4nhhA90cmHHEznbKNCzOqXJS8Ku49NsWU0f49V_h7tqRkjWVgXWDm0rgpFjE-5mlDTeH9_zFWtfP9HXyAvXfU9s3wr4jh2EhlhCVs0J5kFCO3VBJFKMp06DQsoOmHAUYvi6kANgrYYlibHdFEm9TUGIPM3orKyVY0U2kOjuEmIOsiaT9r1g8sJK5ma0q8x_6uiT6h7F9dSdc1OVB7NHPaEyppd0MLVSMvfTV0hUwGYsaXcjHR7SX31Ti9eU4iLRaD20c--nZ31Q4rObYZZ2AiJ6RSeglfagDVDxRJqYKTrgrZ_0IMRAi6Y21jugogsPmcpQepFbJj_iYqVWjT6MxgIs80wxOhkLT_lo2BbV9VkGOeKmNAgcoeifoFwlXCs094SFFf8QAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7796797d6.mp4?token=RBtcJmKMrmKQGzdcfZq820WEpJAiq4ym2-gIrTxLIiTDKRtfa3l-6rbYGkAVqIXN8VB4M8tUEQh7drnlUH72D47I8WidP2R-pcBL6gOEG6jKUViubK0KkG5KnHComuk-WFLKIYuywGGxDFjCVYS0_aOC2WGqpxXgtrhMuEO-DS-lbdtrqQ9a8pq4NlVAU-pYCs00YKLjZpYazbQwkY4QYMxjsXSBRpRnC9aHfWcfb-GLjqzTLbdOtmOOvhuYRsvts1InqGn0-kJ76U9KpYE8fgRtsb47hW959c4nhhA90cmHHEznbKNCzOqXJS8Ku49NsWU0f49V_h7tqRkjWVgXWDm0rgpFjE-5mlDTeH9_zFWtfP9HXyAvXfU9s3wr4jh2EhlhCVs0J5kFCO3VBJFKMp06DQsoOmHAUYvi6kANgrYYlibHdFEm9TUGIPM3orKyVY0U2kOjuEmIOsiaT9r1g8sJK5ma0q8x_6uiT6h7F9dSdc1OVB7NHPaEyppd0MLVSMvfTV0hUwGYsaXcjHR7SX31Ti9eU4iLRaD20c--nZ31Q4rObYZZ2AiJ6RSeglfagDVDxRJqYKTrgrZ_0IMRAi6Y21jugogsPmcpQepFbJj_iYqVWjT6MxgIs80wxOhkLT_lo2BbV9VkGOeKmNAgcoeifoFwlXCs094SFFf8QAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔷
تعامل کمیسیون اجتماعی مجلس با شستا
#شستا_کنار_مردم
@shastamedia</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/458484" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458483">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جشن روز ملی ارس؛ شکوه یک رویداد ملی
جشن بزرگ روز ملی ارس با حضور پرشور مردم و ارسوندان، خانواده‌های معظم شهدا، مسئولان و فعالان فرهنگی و گردشگری به همت سازمان منطقه آزاد ارس برگزار شد؛ شبی که یاد شهدا، موسیقی، هنر و معرفی ظرفیت‌ های تاریخی و گردشگری ارس در کنار هم قرار گرفت.
از اجرای چنگیز حبیبیان و گرشا رضایی و رونمایی از آهنگ «ارس» تا تجلیل از خانواده‌های شهدای مرزبانی سال ۱۳۲۰ و شهدای جنگ ‌های ۱۲ و ۴۰ روزه، رونمایی از آثار فرهنگی و گردشگری و پوستر جشنواره ملی عکس ارس و اهدای ۱۵ دستگاه دوچرخه و یک دستگاه خودروی MG5 در قرعه‌کشی میان شرکت کنندگان.</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/458483" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458482">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/458482" target="_blank">📅 11:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458481">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBO6Eob_gJ29NnkbBCltGzLLpybZtRfd1LyAadar5B6qmFzdnhAIRLNpa9u7GWG9EmV7-KhDO0bKnTmnhtfY9YffLf7ZTzUjQqo5ll95Q1S2b1njohD2IxSmeAgwh3K4bFl8chPhKHlaiwwVivuiG6FQbjUb9sifnp0h464fZ9srmPyvAMPBAcsarmjyWbOphGYqALZs4bvrUNYeHxRe0JmhuXMYMEO_qqtW9lYQf4frtq-jX1UiBZfwWRGU99E9ttPoQ1g2FrwGIBD1dErvzsdowjbmz094-a_vf4J4S8UF8_oE3c3X3k7Wt0wrhb4eoIbJNhm7i5aKDO_sdHifhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: هر ایرانی در جنگ اقتصادی پای یک لانچر ایستاده است
🔹
رئیس سازمان بسیج: دشمن پس از ناکامی در جنگ نظامی به‌دنبال کشاندن ایران به میدان جنگ اقتصادی و شناختی است.
🔹
اصناف، بازاریان و تولیدکنندگان باید با حفظ تجارت، افزایش تولید، کنترل مصرف و جلوگیری از دوگانه‌سازی، سنگر اقتصادی کشور را حفظ کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/458481" target="_blank">📅 11:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458480">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88d48e901d.mp4?token=eSjPiiBMUPZ0L1LnBQfqbe9-vR_dxa2_Ns7Pmi-jyP8W6y5J89rAnDJadKPCpvViyAe87SeAbvzLBGAmJOJ2atrTGdMfVv0hneuNRGjdJ_EQS5sOp2elIgOfOOm6ahZeMfwWevDzz9xtcy-3oxiW5-7gkfEb7YwrumbVgOOrY9HVKQEMiiKRZFELajA6Zc2iE8CtyrrDoRI7d69bs5WtjZ4zT8WmPva6YnsQ0Lz3Tys4cDQVZE8YuHtViyFYrOEuAdjdV_UlsAhO_pNKjFeOyXmOT68OahWw_DSQXuZMc6TMnqFXKNkT_TzdA9XxCg1RRPjz14OVcSif8DFZg9FNnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88d48e901d.mp4?token=eSjPiiBMUPZ0L1LnBQfqbe9-vR_dxa2_Ns7Pmi-jyP8W6y5J89rAnDJadKPCpvViyAe87SeAbvzLBGAmJOJ2atrTGdMfVv0hneuNRGjdJ_EQS5sOp2elIgOfOOm6ahZeMfwWevDzz9xtcy-3oxiW5-7gkfEb7YwrumbVgOOrY9HVKQEMiiKRZFELajA6Zc2iE8CtyrrDoRI7d69bs5WtjZ4zT8WmPva6YnsQ0Lz3Tys4cDQVZE8YuHtViyFYrOEuAdjdV_UlsAhO_pNKjFeOyXmOT68OahWw_DSQXuZMc6TMnqFXKNkT_TzdA9XxCg1RRPjz14OVcSif8DFZg9FNnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت بارگیری و صادرات نفت در جزیرۀ خارک
🔹
مدیرعامل شرکت ملی نفت: چندین پیمانکار در حال انجام عملیات بازسازی و نوسازی مخازن هستند.
🔹
بازسازی اسکله‌ها و مخازن و همچنین پروژه‌هایی که از قبل تعریف شده‌اند، بدون وقفه در حال انجام است و هیچ‌کدام از کارهای جاری متوقف نشده است.
🔹
در حال حاضر برخی پروژه‌ها حدود ۲۰ و برخی حدود ۳۰ درصد پیشرفت دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/458480" target="_blank">📅 11:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458479">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کندوان یک‌طرفه شد
🔹
پلیس‌راه مازندران: با توجه به افزایش حجم ترافیک در جاده‌های شمال، مسیر شمال به جنوب آزادراه تهران و البرز واقع در جادهٔ کندوان مسدود شد.
🔹
محدودیت یک‌طرفه در هراز هم مقطعی اجرا می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/458479" target="_blank">📅 11:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458478">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb68788489.mp4?token=p8DFnNALJnlhq-L6sY1MsgyGmKd6EkeGfXYXHiyEP8Un0VpsHqIkrNebK3i2Am1eGqi4gyFu0sBcn6P-Y-osY-CJ4agevOsaLAg1d7BUyADVGL2EYzMOsV-GXy99DvaoOZifqw11DMLgRlA5sFGwcUGthaiPyh3zxv79-vUjHNFHI2N9ZM-RBoa9oiz5wu95NH3BUiln0s7A-tcOtTHjlJs_A5lFEblvoV98QDoCg1pSZSSlERywxwp6ZvIZyCeT53_xxYV8mxQ9AWAGgs52ZFazPoZa9F9y3FYPTcofPN1UNi3lWCddCs2jCgvxrOZ5TkVjYASHl2J_Ij83CM7sWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb68788489.mp4?token=p8DFnNALJnlhq-L6sY1MsgyGmKd6EkeGfXYXHiyEP8Un0VpsHqIkrNebK3i2Am1eGqi4gyFu0sBcn6P-Y-osY-CJ4agevOsaLAg1d7BUyADVGL2EYzMOsV-GXy99DvaoOZifqw11DMLgRlA5sFGwcUGthaiPyh3zxv79-vUjHNFHI2N9ZM-RBoa9oiz5wu95NH3BUiln0s7A-tcOtTHjlJs_A5lFEblvoV98QDoCg1pSZSSlERywxwp6ZvIZyCeT53_xxYV8mxQ9AWAGgs52ZFazPoZa9F9y3FYPTcofPN1UNi3lWCddCs2jCgvxrOZ5TkVjYASHl2J_Ij83CM7sWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اراذل‌واوباش سطح یک در ۱۳ آبان شهرری زمین‌گیر شدند
🔹
فرمانده انتظامی شهرستان ری: با کسانی که بخواهند امنیت و آسایش مردم را به‌هم بریزند، شوخی نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/458478" target="_blank">📅 11:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458477">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b2076bfb2.mp4?token=Y0Jqb4rcuFihqpT1wUApn7fJ8DZiIzsXZWqa_M2wkK3hBRKQVnMtcJxQJOabstMDT6zG48phVhZ8YgNCgsjNjNDObJr2HazlQBNDfQ0IsDdjMjcSRLgdJjYbjKY3My8mNinVO10sn5CQqfThMPi7YPOG8rwqjAMHfueDgz1-kA-gIiF3yqIJyM7oJKr64Z8xr4eGVcsiv1J4RIO-Gl6senmyScND8Mu8QKj21GDZJ1C1e9a1AfQLfhz57V_HyMc2_ASox6hYxs52XCFwvg2DQ5tqzGEyp5tGHzaLvQFc6H1MNK38A1uyVkrmeH9XvJbzEeHcnf1EAWGdIX_BAS5c7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b2076bfb2.mp4?token=Y0Jqb4rcuFihqpT1wUApn7fJ8DZiIzsXZWqa_M2wkK3hBRKQVnMtcJxQJOabstMDT6zG48phVhZ8YgNCgsjNjNDObJr2HazlQBNDfQ0IsDdjMjcSRLgdJjYbjKY3My8mNinVO10sn5CQqfThMPi7YPOG8rwqjAMHfueDgz1-kA-gIiF3yqIJyM7oJKr64Z8xr4eGVcsiv1J4RIO-Gl6senmyScND8Mu8QKj21GDZJ1C1e9a1AfQLfhz57V_HyMc2_ASox6hYxs52XCFwvg2DQ5tqzGEyp5tGHzaLvQFc6H1MNK38A1uyVkrmeH9XvJbzEeHcnf1EAWGdIX_BAS5c7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با ظالم باید دشمنی کرد
🔹
جمهوری اسلامی ایران بیش‌از ۴ دهه است که از فلسطین حمایت کرده؛ به‌دلیل اینکه فلسطینی‎ها مظلومند.
🔹
اگر ایران از فلسطین دفاع کرده و هزینه داده، این را تکلیف اسلامی می‌داند.  @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/458477" target="_blank">📅 10:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458476">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfcf322ed.mp4?token=DJimxWHlj-VilXLiOyAaoDH53nW22GkxB0HzJJB4GLi0Qh0ZkIvayqfFEki9uJSPU9Qx706s3ekU_f3iS6N1EGeKkUOp0WEhQyOK_eMxcdaqw7SUumeh0psVuFkm0Tp_XGG8EDMMgguROnenAWMlocw5n2rK0ScNDbWzwizivnlzJsWtxtiO5T4XLKJ49evR_nA-yNfJ41qjcOBVCj_JxgAlzCSdunMEM7-UlE7k6fGl6BkrHqt0IEt-PRvZrby0qpBytPaFA8s30yiI28102KLYwYHNxWEO8cZQC27xDOA5BxGt5btrOrX4hQNu03lozmvmp4lSI2cet-y3mBUapA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfcf322ed.mp4?token=DJimxWHlj-VilXLiOyAaoDH53nW22GkxB0HzJJB4GLi0Qh0ZkIvayqfFEki9uJSPU9Qx706s3ekU_f3iS6N1EGeKkUOp0WEhQyOK_eMxcdaqw7SUumeh0psVuFkm0Tp_XGG8EDMMgguROnenAWMlocw5n2rK0ScNDbWzwizivnlzJsWtxtiO5T4XLKJ49evR_nA-yNfJ41qjcOBVCj_JxgAlzCSdunMEM7-UlE7k6fGl6BkrHqt0IEt-PRvZrby0qpBytPaFA8s30yiI28102KLYwYHNxWEO8cZQC27xDOA5BxGt5btrOrX4hQNu03lozmvmp4lSI2cet-y3mBUapA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دفاع از ایران به معنای دشمنی با ملت‌های مسلمان و همسایه نیست
🔹
هیچ سرزمین اسلامی نباید سکوی تجاوز به سرزمین اسلامیِ دیگر شود. هیچ کشور اسلامی نباید امنیت خود را درناامنیِ همسایه جست‌وجو کند.
🔹
ایران دست خود را برای ساختن چنین ترتیباتی به‌سوی همسایگان…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/458476" target="_blank">📅 10:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458475">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49bc6f25f4.mp4?token=vlgT3AXpSIRdgo672IKX17PMkQq2HXF7mb9UdeHbYKgtaFYm7ZSk5dxRZSWu5sI5iNjCrguXx3rCrg1onf1LgsUoAbeyWkY06kbxnBaDN5SBi5sTaFYbao0--iPhgAYCREfY53R_TekiVbwp_yBYdAkimLX70dhC1vVlpGp_oviUOKjqtOEBeoVISBc_qrf1kPScvuQxu8EjNuEdu_pDiqyT9IgR8aLzKy6tuYLC6l9qbmGLV5kBPDHGshn4mSqDQgAewmmd-8XO1ZDxzlC2Iu0c_P2ikYsZCvQNcxhw8xBFaWhi-476FkkSIasvUJfr4-sBtRwxzn1mswkkzv0TxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49bc6f25f4.mp4?token=vlgT3AXpSIRdgo672IKX17PMkQq2HXF7mb9UdeHbYKgtaFYm7ZSk5dxRZSWu5sI5iNjCrguXx3rCrg1onf1LgsUoAbeyWkY06kbxnBaDN5SBi5sTaFYbao0--iPhgAYCREfY53R_TekiVbwp_yBYdAkimLX70dhC1vVlpGp_oviUOKjqtOEBeoVISBc_qrf1kPScvuQxu8EjNuEdu_pDiqyT9IgR8aLzKy6tuYLC6l9qbmGLV5kBPDHGshn4mSqDQgAewmmd-8XO1ZDxzlC2Iu0c_P2ikYsZCvQNcxhw8xBFaWhi-476FkkSIasvUJfr4-sBtRwxzn1mswkkzv0TxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دفاع از ایران به معنای دشمنی با ملت‌های مسلمان و همسایه نیست
🔹
هیچ سرزمین اسلامی نباید سکوی تجاوز به سرزمین اسلامیِ دیگر شود. هیچ کشور اسلامی نباید امنیت خود را درناامنیِ همسایه جست‌وجو کند.
🔹
ایران دست خود را برای ساختن چنین ترتیباتی به‌سوی همسایگان دراز می‌کند؛ نه از موضع ضعف بلکه از تجریۀ جنگ.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/458475" target="_blank">📅 10:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458474">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کشف خط لولۀ ۳.۵ کیلومتری انتقال سوخت قاچاق در سواحل بندرلنگه
🔹
مرزداران پایگاه دریابانی بندرلنگه در عملیاتی در نوار ساحلی این شهرستان، یک خط لوله ۳ هزار و ۵۰۰ متری را که برای انتقال و قاچاق سوخت در زیر ماسه‌های ساحل جاسازی شده بود، شناسایی و منهدم کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458474" target="_blank">📅 09:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458473">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siwbVxzEh1cflVzgXl6LVJUYnsvj_eqrWoDZAj9yl4dG7zOJr5iJgQAgKc8GQG2itgnomBj3x6K74rT2Z0TKL3-YBQD9tiHLcbXZnDhoMBlZkGvT8bTMs1BFfV3s1sxfpXEQFJDvMztxRfsf_J9TVO5Z9qCKgHtNbhbHAbCVsLO-_QLok4U0cQ51mEbpVN_lyC3UWXcEhxtALdahOV7cmFuIqt7PaRXh1U5FvW1qqW2tHnZrrlCOlZV4Yo5O0fYbLKklECbGUJL5RhqLnLDg9ZnaIckDdshXE5UOZOD9X8a-nr5-FUgoyBbvCJOY_AJ57T8QOoqrWMKbHZdqQN08Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضع اضطراری برقی در آمریکا
🔹
رئیس‌جمهور آمریکا در پی آنچه «تهدید فزاینده» بازیگران خارجی علیه شبکه برق این کشور خوانده است، فرمان اجرایی صادر و در آمریکا «وضعیت اضطراری ملی» اعلام کرد.
🔹
طبق بیانیه‌ای که کاخ سفید در وب‌سایت خود قرار داد، ترامپ مدعی شد وابستگی این کشور به تجهیزات خارجی شبکه برق، به‌ویژه با توجه به رشد سریع مراکز داده، هوش مصنوعی، صنایع پیشرفته و تولیدات دفاعی، خطرات امنیتی بیشتری ایجاد کرده است.
🔹
هدف از این اقدام، حفاظت از امنیت، یکپارچگی و قابلیت اطمینان شبکه برق آمریکا در برابر تهدیدهای خارجی و کاهش وابستگی این کشور به تجهیزات تولیدشده در خارج از آمریکا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458473" target="_blank">📅 09:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458472">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbE85uVH-dZWuoV8FoZ1bOo8e96CKDin9HxwxMHvV0sKzUIhuC055_Pn_aH9e0Myz4yMZBSBO_GxK1cyXjWL5ZGMn1buQugKIeXi620at_2dYtIRD-BRj3BaGg_QUN3nL-DKV6TEOjqO4iGd145A1JXBIluPrQ4TTVSurd-l28QaGe8Vyz2papCwtywBsq_HwDHds_d_Wkl-Rve8k_63IW7UwXCsrfDcgEJcTaz7xx-UTArtzceNpVC1iTv-6rHymRopkdM44rKo3T-eRE9YSLELbig2xFJgdgpdXxCTwjb-gRTkKtyOXA9mGTAMGpW-VK7NKsRfNey2E2SVxQd34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چگونه جنگ اقتصادی را به آمریکا برگرداند؟
🔹
نشریۀ آمریکایی «امریکن پراسپکت» در گزارشی با اشاره به سیاست‌های اقتصادی دولت ترامپ علیه ایران و کانادا نوشت: فشارهای همزمان واشنگتن بر این دو کشور می‌تواند پیامدهای قابل توجهی برای اقتصاد آمریکا داشته باشد و افزایش قیمت سوخت و کالاهای مصرفی را برای مردم این کشور به‌همراه آورد.
🔹
نویسندۀ گزارش با اشاره به اعلام آنچه دولت ترامپ «روز D اقتصادی» علیه ایران خوانده است، همزمانی این اقدام با تدابیر تجاری تلافی‌جویانه علیه کانادا را نشانه‌ای از رویکرد ترامپ در استفاده از ابزارهای اقتصادی برای اعمال فشار بر مخالفان خود دانست.
🔹
به نوشتۀ «امریکن پراسپکت»، برخی تحلیل‌گران این سیاست را روشی انسانی‌تر برای مقابله با ایران در مقایسه با اقدام نظامی می‌دانند، اما نویسنده معتقد است تحریم اقتصادی نیز در نهایت می‌تواند فشار سنگینی بر مردم عادی وارد کند و تفاوت آن با حملۀ نظامی صرفاً در ابزار اعمال فشار است.
🔹
این گزارش با اشاره به سابقۀ طولانی تحریم‌های آمریکا علیه ایران تأکید می‌کند که تلاش برای تغییر رفتار تهران از طریق فشار اقتصادی، سابقه‌ای طولانی دارد و حتی در دوره نخست ریاست‌جمهوری ترامپ نیز به نتیجۀ مورد انتظار واشنگتن منجر نشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458472" target="_blank">📅 09:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458471">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۷، ۸ و ۹ فردا شارژ می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458471" target="_blank">📅 07:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mk0w7ptapdoBb_bWqrxKUUWjNotuRN1ZFDrw43ihpj6jFKD92oW1-RYIyD6VIj6eEu92gvaxYju-PUDVouZp56q0Ac2CT1YfqYZCWC8ATsWQPcbbANIuP2SWb9T7eYPiP7fu3u0JJqhzEL-PCoMaVaMgOrw0GGO2WsmmS3I8YLazIiZd1Wi5r2h35uEP-pgap24YLA-aXcXcY41SF4tXCbACiBdn3TK1u-K81ar5xkYEZctZ85T_FyN7EjjYyQ5ruRjp3_C8IkVNRiM0QjkrbdbC6tt2loj1qOaUQnEPwDeoOmmoDhndE5pBL4iD0WQa6_jMXJ9a8iMLmyZxU5b57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyBy9pIxv3MftPMZCE2KpqcrrYVglp1FnJ88SvKNJfzqv95ggmdcZQjqDtTIe9ybvCx0J4bCz04-6ayTTyTLLX8XRio_7Dsp_ecnTrbu3ZlVCQ8B8XaTREIFZfrSFv5ezkYJJYlexhMvzK3MPTylf31LJiZmNkokHr6MtA2KatMMk-MR47zXNwhMLWrT1Uh9-ThgyQf2TDgNNBeZ61RdEkaemp_ZNQdaF6db7E_Q0BQ7zxeC5_UkRsGkOoW_kfI8fWfJR9_7IsBFcRuX4XLrFPJ9hkqAU6u_voDpIKtH-3Yjb0etkeFTCCwVFC6SeI46-_SJqvAIHCrCxYWHzg-TUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoqBdHABoHHv3_XSzqYH7eWLxSm6V2cIyFXz-Q3uF4kIAKAuhjBPvo0Gq_PqLbiRD_x0vYAZbNa9dy003axWeRh0z6p1QhtTDFaqQ5IHkvnUsnaunsziIsXegCy3Xbvcl_040YgdIurQYKtrWF1_Z_ysFGCxhuSfT6lT_x4mk1khIiB1EQ-IJlsmSRlaHcmX7tnMs4dMSgKYR1qLzSu1BrJZl9mIAbnkr8sQAzrSzcduQ3g8X1jWAGI2L6F4ku_rgrmvjZ98Q4Jbo3SY-WdGV3YZiYgtqlneX4xWgy8JwhjANfXFyqmDkhC99Eh5wG2LfIq-IrlJAmsEyaQErWh-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRSstY4UQBCVyQ6BMeO_6ApoTMV85rImQ4oDiYteqWi94mmuJ1YNqW2ozmoOlymhuIeVMT86VjUzlZdyQGE4B86O6UZ0kp79oT47alxtpd-OjubvstDW_xKC2okTYg_Lxc2RJhsdQLfR0lVdjanIRPaB0uaepm5OXqOTfV-78YFHBAOhhsl2VOjUL6BiszQmF6dJvwJU7gmfEgPFx6cCszgD4EvNEvHUoaI32KjZWWdDtKlmFrPICz32FDc7PeE-dzVKsl45FpzHeSz9DkC_a9aOHo7AmLIcGoBYuHa8iEQ03iLHPC2q4qEJXFlid9Rm8rmfjz2LtmSf0v2SuSUaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCM2x4mFQh5jUbkR_7AHTII_tflN0qJHO1BzSrLtJg8Kncl9HpsRKB9VLVlk29QLH-I3N8VZGH3xJZMqDImfJr8k-epwkS4ZHqqj8hBo-kBFoxKwFDVQDizWZCQGovrf-Z9ZXd3txQEeqiNFGEkIvGcK30sfy5reHc_WfRGwIwF_1wvH8_9lipytVpXMn2zgjQvl78yZxdtkKP-MRWYSYpqI8XqDoq9kuJzJUTymOLJyYQxXBmfePzOKWK41LDc14PKpNgC5ZPMVguh6Tcyx2iAjG5KvQkZd21gzRMlimX68giNUKVVwtfnFlHUH8FrZn57X5FI2nnzB_qnx9ozwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ak1M5P_eYkBUeKV17OqyW8xka6x9SHNWDhsa4cM94O5Ql5FiBCrwXSXh2rz5Kw-yTtisuPw0tKTijtYPLWW0yOfKC2DuQukdhrvZnL5q-lzd4sGZNjql0dYz2EsIFqPUBMVfyhTfzcXBm4AWhiWk5trHbs0i415W5kwM52vWTp2cWYCjw7CsfIY5VISPGeBwDJE7ll5cP4pWGZ_u7YY148lMcAFxLdgws2hwIL6hnbn88aPe7edNX9fTvsiM-UVhDDPx28glcSTlhzL1teApwOPmH0o8orf6Uc4QlsvLuJsBvrwiGETIPWap_TB0eBBdKVeKuz4KMJSU9WxyHlCLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhMQq-J7X98sPKgm95KDGr4HrsA8AWj3kbyoAoi68BNfNO9U61CAEl5BJsgLq2hIJqQ2ZGjuMKPk9hKE-uVqMbgrv1hjOyl_WZV4KIs9L-YlBEZqDZKsVVmUsGITCgYvImFSS0PAzEdWE6Sh2NlysryXslbOF4DqU2FWu7nnHpGcYLn26M8ZLk2G_Fm_IKeIiiTjCRz3FnJnqtgNQu3m7V6ezL6ywWmGYmh4Wb1VIVdlvg1UuukBnPoMDy_Wo2nz3_vSWJyDsbDfPXrgze2kf_LAMzXj3immiUVkPHRXPq0Bucq8_2x4isv-p3Ux9O1gqiw1cTneAyzZ-MTnNUCO2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
المپیک ملی «ربات جنگجو» در قزوین
🔸
این مسابقات با حضور ۱۸ تیم در سه سطح دانش‌آموزی، دانشجویی سبک‌وزن و دانشجویی سنگین‌وزن برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/458464" target="_blank">📅 07:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-hIsbO5L3O6eGMr44Y1kD7fqFve2860qliUPsC7h4kNPTQ03KUUjgl60E-6ZyS-ZPoduejmFLqp9d_8-zVk5Yyn_3EfpJaY6LFPIx6PdhMeae0w8o3LgLWK0J-gPoWlybiTgKoRrVsNTT0Yxw8VFUg-RTyEo-A1TNcWeieKt-_4_IPBlbrtQ1y9ybrJVKr-iPMlgQNVD927cwLnbAzIr4WbmjNVxCZlTxtJ2I_xBX592-22EOA8PZvNwZqOczF9R31At0sX4E4L-6wMIpMIgLMyxpEisg01XlUaaz-_hW56M34YFs3FOGEAzeFLzJhfWif9NxXqbQl9xE7UyiIcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام باند سارقان ۴۰۰ میلیارد ریالی در تبریز
🔹
رئیس پلیس آگاهی آذربایجان‌شرقی از انهدام باند حرفه‌ای سرقت در تبریز و دستگیری ۶ متهم شامل ۲ سارق سابقه‌دار و ۴ مالخر خبر داد.
🔹
اعضای این باند به ۶۰ فقره سرقت از اماکن خصوصی و کارگاه‌ها به ارزش ۴۰۰ میلیارد ریال اعتراف کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458463" target="_blank">📅 07:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زاکانی: کالاهای اساسی را ۲۵ درصد ارزان‌تر می‌فروشیم
🔹
براساس بررسی دانشگاه تربیت مدرس، حدود ۵۵ درصد خرید در حوزۀ مایحتاج عمومی از میادین انجام می‌شود. همچنین قیمت برخی کالاها در میادین حدود ۳۰ تا ۷۰ درصد پایین‌تر از قیمت پیرامون آن‌هاست.
🔹
در شرایط فعلی، گوشت…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/458462" target="_blank">📅 07:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leN2V91EzRZytcMeVlUV9KinqKb-fgA-7ysn0q7eJwIkRSOzr5lB-yuvW7EF77TQMBgpAjXQzY1UFgzcKq0f8WB_vvPmcfze49RiX2tMYo5JnZaxgj_n5Gn-HW79dfihRC92XC-DzcSxHEAjfer243cf_kNlzCDj1ua_xvoCCCDIOAmro3JGbsY253Yk1hF8GOACEB3lLsbeSa5bbUffJeVpsPeMtOugTDF2_Y26l53RY3DcG1Lu3AmyLsD5gpfkxuPyCCXxj-O_ne2PQUAeL7Y08CXTK6OLzjdkqpc7NYAMEfhn0kagVJzwKdNuqYNSaC22dKDpUfjXHN15gSmXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z9z0jR3E0vMPrx-UQGT97ICeBx9qarkwskEing3lHrblX8kGST5oYl5Dlq5MWrI5Wy_6HzAk8vyPe6q8LbNHJ1vT4BxFKeyjD2A34F8cGUwQtP8hV6UnTo11gkUDbwJwy1grlGAbXs0ANO1y_s7RLpi4GLu2CHVw1icb8BfRFRGMPOLf0ivlsZY95VJRwAQE6p180aOwx9xNzlJSF4Mx6-tQsuybJyzS8B4TS8ENwYaf6WvpNpq0cVmmebdftN-xnH1OX_vRGonAdzHa6rvl1spdvjH4ZIJRDJlXEyVmsbfWuceWEiyq5GQfAuqS8-2xtOMVO-X4n0Wkchbxy-imOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ka5GND-chvzDHIH6C-PBdQ0xn_ElcXYctP98BY2LXrsM5IOkoZEKyemEiPZGDR_WoNlyvzK6ybuNDy2lvqpuc1cDR_XFu-yJUW7ayrzWua00HS2XyN4LYIm2xVxClCwwilzxjH0T-OInk6ZNMi_vnA4InJjTkmcIwK0DNUmCWezNaeQAPnexeKu-_A1adQFir24bVENiWPQwfK9IiBmHmoOXAwIdagLLbkUsDqI0cITnt6iz71xrEdnzx9a5D97iZGXaiK0p8ImBLO9tlUhJ0fLaWN1tAlPMZq8hfUH0n7P7D587gc8LfIE47J1xPYlD3YWk4SdzzM41nWwvKfCilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jzbv0YHCKY7NOr7taDFvvG5uQASW95ljBFvsHOuPbszuJ7IJ6WV2V00F_SmY51-VCEJLa6LRfgGWC1fB9Fk_LwZ6NHPJVnzVmSznZbTp1RlkJXRghI9sC4Xsfkn0H-GmP9jUnW2CVSp9IMN8J5-ZzKYQJAmV80ZQ1hnoDKExBb9DmXjenMcdDB2hk39tR7jJcN6l9WHHgowf_sdpZNXQrk0NauWJNU_My1UJaQccGvGpoQBWZLZweBkQI82Jg8cMpERypZlnXuj6U7HYC4GDHxdptIuJT60oRQ5DUWshRcg10smbWYjH6bZAl3_axY5eKGtY0FVd-TqHas2SqqniKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UaHDZiA_UhlUo3g-hdjZ7vQ5kM6T3Ov96pPuc9WrBjCvBrqXzyIfNiANho7J_BXObWFl9B5FPw9cI5eb3QDBT06beWdKMeilWaBKrY5z7YP8gdt1g0vH1z32kJQN8zYQ96PFC3-iGO3NWiVswTU2PzjCX4Ond4qnil_lhs4QfGTEhTsF-Weq8sJKSbh1j6P5gH9pAM_INQV77FTxlxcVOLJHyjbsAjFscQ-xHD0CcXIEscvt1A4vhJcGCAu57VPr6i5ln7dy_DAmq7VBymiECz5_1zNtTnUsvQI7oj-XZH_cNCz6lUsha7LJiKvpR2K83r_DnnJNqokqUKaarWjDlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هفتۀ اول لیگ برتر وزنه‌برداری دسته‌های مثبت و منفی ۱۱۰ کیلوگرم در سالن فدراسیون وزنه‌برداری برگزار شد.
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/458457" target="_blank">📅 06:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLY-gukM1wocKPj25l8aBtScBYaZQ-PL3FIPBN9k_RCX80U2LxjFssEBipv8LNwLl4Oi36AjrCUB6HGfPDLk9M4MT67RcUf9jrO1foRtYgRTwJH1gjVbbwjML7HYeq_mIcTvPQGxQx3qhkOoAqttB7XMoFdaf8Tv_obcVa2eJ4xCda2Mx9Z1AeGD1-9BKHmt6a34mNAbhPTIRSWQ2verAIeCLnGndV4O05K0YMEBO8EFhRb1Ca81Ewii7-5V0Ci2_lWemVu3pGVyQBJWdxlQHIv3lnWC1uF41khTTLKmdHRanyF2qVadNmxyxg5is_QEOibgFqYZkWmtWRwjCbbu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع‌آوری ۳۰۰ هزار انشعاب غیرمجاز برق و ۱۲۵۰۰ ماینر قاچاق، از ابتدای سال تاکنون
🔹
مجری طرح کاهش تلفات توانیر: طی پنج ماه گذشته حدود ۳۰۰ هزار انشعاب برق، و ۳۲۳ دستگاه ترانسفورماتور غیرمجاز که عمدتاً برای تأمین برق باغ‌ویلاها و چاه‌های کشاورزی استفاده می‌شدند، شناسایی و جمع‌آوری شدند.
🔹
همچنین از ابتدای سال حدود ۱۲ هزار و ۵۰۰ دستگاه ماینر نیز کشف و جمع‌آوری شده است.
🔹
مجموع این اقدامات تاکنون حدود ۷۰۰ مگاوات از بار غیرمجاز شبکۀ برق کشور کاسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/458456" target="_blank">📅 06:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458454">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yba7lO_rfoksFhix9ABp7En0vYJtleshjmv00KjjjWuBXZ9mO5EEDz7XCsfGCmPokLg3iKJ1w2ExmytqBBDNF0Ufk1cD6kYst7cNfhw4lBg0noJOvchfCRsoPeL0O_UfUgiyaIl7njdflTxnGKn-nRCJeEZx2BclBSIs1NYEoXNFBD9Ilo52uObUD_P_aoW8CbW2-dgWjtAfDpjUy0wlIW4r2WVbhsbscDXKx-iK6XoN26RYnX-fg_bj4SUWh4BqaaFScBPyd6Un1AEtN2jBzBXpCjBNfhCYIz3Zutj73yG1U9WkxGkGBAObpp6yiGQ6sEaehtu5H1LV6L_MCypqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c2a029ae6.mp4?token=pNzV4piSegfrc8A2VX6M9xQR9tJAWjwiR8j3BtJFCdB8KKdfoZbCnlJ9dKIrSwM6GXaC4fbWWQsNNkDG55K60scl7-nFBXvF9cROzu_HnaP0C5VhoygrlJMD9k2rjgmnyc342Q-1kkGNVutCURIP4xGxokorY10JYXXygLRJGgclukfL8FfXtsxyRaz6-K82EtHdgFHlEdLC-DQ0hYxDqPAr8HvKFT5PACLkw4dXwYHiSRr3_t4ytP4B3jPzNZxniPAmeREM8bCaZEc06D7CStGrO5RTPvGPMN0tcG9sp5fG_2fgQv3jJrRrBIdc95vNMeoXZzYE5eF3W9302DXAHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c2a029ae6.mp4?token=pNzV4piSegfrc8A2VX6M9xQR9tJAWjwiR8j3BtJFCdB8KKdfoZbCnlJ9dKIrSwM6GXaC4fbWWQsNNkDG55K60scl7-nFBXvF9cROzu_HnaP0C5VhoygrlJMD9k2rjgmnyc342Q-1kkGNVutCURIP4xGxokorY10JYXXygLRJGgclukfL8FfXtsxyRaz6-K82EtHdgFHlEdLC-DQ0hYxDqPAr8HvKFT5PACLkw4dXwYHiSRr3_t4ytP4B3jPzNZxniPAmeREM8bCaZEc06D7CStGrO5RTPvGPMN0tcG9sp5fG_2fgQv3jJrRrBIdc95vNMeoXZzYE5eF3W9302DXAHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از شایعه تا واقعیت قبرهای میلیاردی در بهشت زهرای تهران!
❌
در روزهای اخیر، انتشار آگهی‌هایی با قیمت‌های میلیاردی برای فروش قبر در سایت «دیوار» باعث شکل‌گیری شایعاتی درباره قیمت قبر در بهشت زهرا(س) شده است.
✅
شهرداری تهران: این قیمت‌ها رسمی نیست و تعرفه قبور بر اساس مصوبات تعیین می‌شود.
✅
معاون خدمات شهری شهرداری تهران: در قطعات روزدفن یک طبقه قبر رایگان است و هزینه طبقات دیگر طبق تعرفه مصوب دریافت می‌شود.
🔎
اطلاعات خبرنگار ما: استفاده از طبقات اضافی در قطعات روزدفن، برای هر طبقه ۲۱ میلیون تومان هزینه دارد. سایر هزینه‌های آمبولانس و کفن و دفن نیز کمتر از ۸ میلیون تومان است.
⚠️
خرید قبر در نواحی دارای تعرفه اجباری نیست؛ بنابراین قیمت‌های میلیاردی آگهی‌های اینترنتی، تعرفه رسمی بهشت زهرا(س) محسوب نمی‌شود.
@Fals_News</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/458454" target="_blank">📅 05:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458453">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA6HdwOPrQjrd02Byzx2L8DP0X-JBoe8Bupw-nRuSwYHtkqebKhS74tkaobjKtw7tgXGTWG0iX1ITMLbUgQ-4V53j_ESGHELDKgjUrYKNe_CgJJWS264tv6VPf80P23Pj-crMrJxXJrFVJi7MwIfljIXN4MJz7eNtjfeXCVo5oFWWN2i-z8rm_cTJqEJts1TZszJB9tKwkl_bEt2MAnB2YZ6C3KKpb9UIqlhcUXDjy8S10rcaQCEPITdiYa2MIh_GttvF11hXNApyY-VKiPiEx5v8ze8RENQE03uCNVB5lhObl8qDstlxo1DE_58tJTah2YEsoPUUOXv_yZXCbKtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای دلیل سفر اعلام‌نشدۀ رئیس سیا به روسیه
🔸
رسانه‌های آمریکایی گزارش دادند که رئیس سیا به مسکو سفر کرد تا به مقامات روسیه دربارۀ حمله به کشورهای عضو ناتو و کمک نظامی به ایران هشدار دهد.
🔹
وال‌استریت ژورنال ادعا کرده ناتو احتمال می‌دهد روسیه حمله‌ای را علیه یکی از کشورهای ناتو انجام دهد تا اتحاد این ائتلاف نظامی را در چند سال آینده آزمایش کند و بین آمریکا و اعضای اروپایی ناتو شکاف ایجاد نماید.
🔹
از سوی دیگر، وبگاه پالتیکو ادعا کرد رئیس سازمان جاسوسی آمریکا (سیا) در این سفر از مسکو خواسته تا حمایت نظامی و اقتصادی خود از ایران را کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458453" target="_blank">📅 05:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458452">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnVJAHev_3WyjbrE0BEb6o3aHb_gHXJbX4cUpTa44O6IW1Qfw8W_2Ov9nxSn27u7hrBpGQe4_X-5pw5CYSo1xsensRATf8u4ST5yptKvwRis5zQIUGpKVjFARPnrpArOmrDHFwOQ8c9_NhOAxNc9F2ebzsuRfjg75q2f1dvfL1Q2Nfo1rkslzATmY1-zJKWFyRexZipqyFSiX_bHl5oqe0x9OEYpTvsGSKJi6Du-ypiuCCNgrou5xtKDnjwRb3JkQTvjSVPdemHERW01Xs6zNCvfspQh05ROJefmD5-uSYBjEJnjMRwqoAPRaB_zbJiBsrVx6-IE0ICN-AZo10O1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در تنگۀ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس: گزارشی مبنی بر اصابت یک پرتابۀ ناشناس به یک نفتکش در تنگۀ هرمز دریافت کردیم که منجر به وقوع آتش‌سوزی در این شناور شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/458452" target="_blank">📅 04:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkOwSA5uU2Xatcl-VmPSrtyuej8spgLJ42yWsPQUsSs597nP2UD-5qE-MhuViBtFWshKIEMLO6DcrEV-5h468dF2jOp26O1IKT0zjHRIQfEy__dvJWLFepmG_ZHIJuvf7BVxxmaZ5SeDtX-Rl2Al0kU0-nXlcUDSd7qDVzc8hnW_nFpPrBDpSyqi1AW5IyA3yskX9j845t87Pl_S75dZ-Je7sZShh6xfeHSD7LgHMmTUC-5AS7VbWUM8jpi6vsGls77ljn0sNxCmLlPWOHgpeuv-k_LDvH_uEzEbjy2VtSQbKMVyZgb5PJN87l72DErq6qLPI5pXHJXYQnEZLKhZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام شب‌ها برای زیر ۱۸ ساله‌ها قفل می‌شود
🔹
شرکت متا برای پایان دادن به شکایت ده‌ها ایالت آمریکا دربارۀ آسیب‌های شبکه‌های اجتماعی به کودکان و نوجوانان، با پرداخت تا ۱۸ میلیارد دلار موافقت کرده است.
🔹
این شرکت همچنین پذیرفته به‌صورت پیش‌فرض برای کاربران زیر ۱۸ سال روزانه دو ساعت محدودیت استفاده تعیین کند و دسترسی آنها را از نیمه‌شب تا ۶ صبح مسدود کند؛ والدین می‌توانند این محدودیت‌ها را تغییر دهند.
🔹
متا گفته اگر یوتیوب و تیک‌تاک نیز به این استانداردها بپیوندند، محدودیت روزانه را به یک ساعت کاهش داده و بازۀ ممنوعیت شبانه را به ۱۰ شب تا ۷ صبح افزایش می‌دهد. این توافق هنوز باید به تأیید دادگاه برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/458451" target="_blank">📅 03:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgYFasJEw2UGCRfCZCLtfZaYD4LfXV1mv_ynpokHPxH2buKiR2t-cwZVPjgRRUn1ydtygQlUK8IoQIqCj8vIeS9869TDM9xnxW3SZ5KVwb7-5WEC8bm5dup0hKhu9-fnIM1_eyV-qbvMwLJ_xMOdJBI4PF_ieK_Eqp9_3hI7WUwy2p_SovFmQWhrRYratkVCj52KkynmuDuRW69qrjJN5JmVbyC1pNGX4SKtjDGmk1d5u9R2PsCZzorr2nQyNVrUCELYt0rkf1ipga2su6CAly5ymNnNkp6p7r7TC5Rp7pAD8xL3sY7Hhla1uI8uotsK1pnXJHZ2Wf6MXOnh5qr05Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفوذ هکرها به ناسا، فدرال رزرو و سنای آمریکا
🔹
آمریکا مدعی است یک عملیات هکری مرتبط با چین به شبکه‌های چندین نهاد حساس این کشور، از جمله وزارت دادگستری، ناسا، فدرال رزرو و سنای آمریکا نفوذ کرده است.
🔹
مقام‌های آمریکایی می‌گویند این عملیات فقط به نهادهای دولتی محدود نبوده و شبکه‌های زیرساختی و حساس دیگری را در آمریکا و سایر نقاط جهان نیز هدف قرار داده است.
🔗
شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/458450" target="_blank">📅 03:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFZXhizVmD_2wOR172bJVMCO2hLewq-GltrtJKngsZodGTIdj_d97VoeWMRt52veO3OibLudqgixNLihmmpSJV-SCBIun0IBnTYOze_e5npNOjD1xCvkw2A8Zsonsh_DJM4GURtSFJ0t9DncC_tlsGTICUWKxlTgW7L1CrM02jHa2OfStM5meLEC5y_f8_Lc92Ix7W2PnGATUfCnpdGP4h4aLf8R-Y2nlCOHO6wrVNWhfVHcbLQiCGXPLlTYYihHid45IFXlYIFVMOE6eB_yyQr2T2Fq9O3hVCVC6ogdof9vpAR2vPAuxh1kUkWiLmn_ANfFyW2e9EXwRjOUYgQPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔹
کوروش اژدهاکش، بازیکن تازه‌وارد پرسپولیس قرضی به نساجی پیوست
@Sportfars</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/458449" target="_blank">📅 01:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">منابع محلی از تکرار حملات تجاوزکارانۀ رژیم صهیونیستی به مناطق مختلفی در جنوب لبنان خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/458448" target="_blank">📅 01:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458446">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a681aaf99c.mp4?token=mXyjhxZg54nfk3kDyRIf4h-zPRbg27xv4z6gSIX0DFxD6IlfZa8XlUjyGVTSOpa5n8Nx9Ihsxl2MdZ4XwqUHQhfsYjWeYN-DQOfwI9DUjslF12Zau_u7VBLLiC7QEeFRco0jXcgzVe63DSnZcBUYFk8PPYJxvL-pbNFZ_ANTEBkd2VgDFFcO3jCxFfGNamj686D7_mab959tz3JBSXqDbE5VfxnD_hIUeLEBDHBnLYioo88X7xvBGeUQFa89VWc6aCVJgZFl0o_sREWVpF5VxZT3NfQiL4j67rK56Fw60zaAwehosZ--usLwpbROWVyxEXtVgcwWWpWd_Ega8u5VUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a681aaf99c.mp4?token=mXyjhxZg54nfk3kDyRIf4h-zPRbg27xv4z6gSIX0DFxD6IlfZa8XlUjyGVTSOpa5n8Nx9Ihsxl2MdZ4XwqUHQhfsYjWeYN-DQOfwI9DUjslF12Zau_u7VBLLiC7QEeFRco0jXcgzVe63DSnZcBUYFk8PPYJxvL-pbNFZ_ANTEBkd2VgDFFcO3jCxFfGNamj686D7_mab959tz3JBSXqDbE5VfxnD_hIUeLEBDHBnLYioo88X7xvBGeUQFa89VWc6aCVJgZFl0o_sREWVpF5VxZT3NfQiL4j67rK56Fw60zaAwehosZ--usLwpbROWVyxEXtVgcwWWpWd_Ega8u5VUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنگونی پهپاد عربستان سعودی توسط انصارالله یمن
🔸
منابع محلی از سرنگونی یک پهپاد جاسوسی عربستان سعودی توسط پدافند نیروهای مسلح یمن در استان «اب» گزارش دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/458446" target="_blank">📅 00:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/beg28WrrOD52Z3PQTeKsodipT3I94QWflJJ175ra1qONjpx0ciyruIqLqM2G3Ng-nfpg0ocpLIZyc_UfzFZ06Ob0wZORjSbi6OvWxDxDbI3rj-B0gDGUGTuJ0IVWGRnQKpPGU0O6xwc2HBN5yCk1CbiVrTAfaD7qJJZW0jY3ShOYZx88iNoo1-zLFjlDRT9xkMpSTR5Bpq0BV0eqpoIxu7N3JwdttGm51Ko98EYwMQ0BM3szAbNVOkIQI8_VHrgbIeBsric0EBi9JBM0FUDgQflJXg6zlcqqgVLTjG5FxQll7NLHthWY-ZI2EjLUntJZeEgXnJH1DNGz35GltPyxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YR6OtAFMEp8L1OanAuXHYh71hWt26e37iR2Ep-nWu_RDuOO2jZB3YIygOSe6UN2sRhEIk4W9FwzzbVD9hTBN6xnwMx7EBOJXnEwD6maDyb7rHW13NW3Vv6FuIU-KIsApn7yl9tCtHY3gtON9A4QkcLcBjD4B08qw0M0xahYrKguqwMPCk9-0fYmL1vK_kkKOGJd-bKqgIAB5XrruRix_NTKyrdugNlV-0jAxpWAYocblK7eTskyZQQcORCbRkEgXqaM_iEDwXa9KzqKiCYw0Zd8BXaPfderkO4oDHmwHzT5wVX6s96TvFlVjptx7B1NzHGJeBvVJU7Vzc4DlgOpxCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVxIr8ICnfAvLxnSv2uUwpV0-koOqy4_k55vAUxGT1p_745y3ITGO2mOfTk8qHehLEhwxzn50oouydFvNZ8AA0Mu2yHMDvrEK5ifm3336tVkxBGUlfuZSelOH9dawNmMWV_CxT2BFLE3g6iS_dFayINQuy-5MRCVG9nJ0XB-CtFTFXER14R7KLB5ZRizihryUDeEOFSX4oksmPnoBMOk9ViMqClO1doiVNwM5v0l9f1An8dXLB-UpoxRbnHBuoF3q278FFcv1gvR2dXSCN9u-8N_5UIK_sNm6EWE35N05xC8G1je3NszoY0-JB-CjRSo3EwYMyi_gKRqKy3DlKOvtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ci8IKHUxto3A4C6JvygYO9gLc7Rq_PoQ5Zj1vNUyvwhCqtGS4tibQMMI7UPx6yBncu_SbueeLzzjJ95wVhz1q6jSXBob2ByWRt1qT3I_Czbc606NB9ut-ccGyd6TxfyeWNh9Iv6stERAMS0IvUzxX8tnf0I5NkqP7FQtK_ofoz8WsjxkILKAXDshS0tANNEMWDIM8VKF8nDSBO6Jl5P8oijyoMpW6hDB_uLCjs9aedXU5bQxbHR56XacxMhryOZqL9j48PukFFNxwag0Je7PtCv8jo2R1ZMGJ_n26yuBgdjI1XstvKuIa76--WCSVwW45B_AkGIpTFiiqaGWcPv_6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۵ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/458442" target="_blank">📅 00:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwie_oBwwTVKp-XNRx_bMAW3CDfCrwwP_0OleJ-ErG_8QLGLYeSeRXBKygyRfCMi4FpQdWub0AGE78SGo40yOserLmFXWnh80pEUabj4Dr6ow9Fabh5Z-G2ru8DNPoVRdHYuC_T5q3cQf35tRX3IgamIuLvRiNgAa1cAP93w5dctikNqYZgqMMQyxvKjD3hwqe-JbJFxYpA-q0OVG2noLMF_g-NUdwmzUuL7ZKIzMI7X_bN5i7g4lEKT6mnSqKnu6iy_eZAWKfXNhMb4oDBI3PCoLAJH134N8DH5hbL1tL6LiJjPYalzmIgKcd9AEsYNEtlncqrWWKbQGFbAp0fbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PejUPdywaZp1Vc8HSa4XanEmQ4boUopoomYJ9fZHxzt2pEKUwctA_gt2amIg3U2NcgpVL4BSxG__BxbiPsqEmgF8zqWkfURCMLrHiT8G92W_1gjVwD9UhvQJbP6KS-WttmrCRThmIN5wmf8QZL4E1uDbKoEx0Ou32MPkRGwWvmcr6NNM7gjcRju-ubZsPo1fZrcBFCU-bBgnWTYUXyihcvaynZEdLq8vTJU-mnwsC6y1FPjH957ptGHIOpRihxsdObriU2XV28_wjylfIe4pfRxW2_R5gn1t-lHg7z2O4OS3KxnhDxYgIVKV6bwbFgMWklSsG5F4er3UdN4k1NnG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeyHtQYe15ZVlUS6Yqu_UhjXH_ttQ9KqWGrLt8Ja0e5hmT4_FOwpA0_Lsj80whSWr8ZPAXPi4MzOjoo2Qp_NC5kPJDqTYx0H2XRtcgbbxyS_qY5mFbgaKCrZClUMwmYbzUmHRn1kDhL91NNnNEbiN5W8MtZ_GARu6WUsia0AXiomw4YLiuBTKuiB4zIelyQ1uD7hYMKeAJ6-Toh3aFkxm-f00c6UJrUJ_uZIVVthDq46MjJreF4lZYzyuRR4zv_63qG2P6gSsl-P_WmzW06HESnJI-WAQ5ChxnyiACoNxcECC_g5j19KTrmw-BxttPtS3u5FsL8oN1k8F71At8Widg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giN2tJn98ANHj-DT0KJAdB98ds6NxTmxC9jWfaXNPdbYp5_bA7QebIRBkCewgvD_Ejb1ROY1Y1g9GVDKhba6dcJb6YFmTBPfK9nkFef-joYET1phrLif4J9V8_25iD6Tr_LVadlkfqaVZ02fNVqDwc6R7Q9arodazTsd8LCJ-nPtXEWFguVjmPgjPTZ44TZdlzNv-uZjk5NfEXCMCWsOz_HHq2EEoWVcpXwC3xeqkLvPgN0G1mttEsLmP1255-W9g4jhSQRX6owtztcIDhas_a7-Fmv7WbCIWgWHAEWNrkEO-vEhkzWVEq271ji6JMH5Da4l5bZXoFr1IjmqzdWb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtYkfjgNP4haAPBQoAIagK4BUqnAuYxjO6BTaTDmR320FfCTKVNe1sdqaXI68wtsJfvhJlJU_Z3xkapJKx61Xh2WDCBFZapx7oK49c2ZZrhMqZXwSamArYB4sZ8UQ65_qmVcs0ZOzcEe12ArT4eMv-lTGmHQ5Np9-p6KLGwexgJdfRnlY22RLQXAZXVxjUVjFxco4cXifbeYAFekjGLefSDK-U5t6i_wZ2N6Jk27aJ0F5K8x_ov2V16kZMBy7pvuk7EOOjYj9QzNHS2EPHyXNbvp3nz-CWUV7PA8psBNxjnRsH_2j4HpmQaMxVJtbDyyqy9XR3_EX1d4iZx_N6TTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYSRtQKrgqhHt5jMwrzpsjhehHX09M_IgotIKsfuIwY_a_ozvi7LhRaotfmAYyLr941x9hagqwHFkE-9oFBGi4hYMKs6qls92lxI7JtnZtbyxDek-bJmt4OieRP06EHRLzG3oATVsdR7Nx7vn22ncF0HCHcP6kURiPXiSpvwNB8dL7hmu9UNVnVPjpyFNMCViLDViR4aOjDRlC-DDrDfs1YAtLVgb2-wd-gg6gP2ohbRs5KM0EaCoJClb6b2S16Dkar8A_JtyKaSCpU-k3PvaA6EnDeA_AdGvWC-J5vUXlN_CyhQb4QX1QVPPrXyAxishmKCbqcPtk-Zz9Ijm2cADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXRZs_3D-gsIzema4aHBeAB18NJw-Eq125aZRGiv1JE900mMUHTer3_tDbBKMo4BYBDQJ4ohyUAqVUeCNtcbwguKiHuL5qaje7sjgQMyO2FEm8uDphAA8EUN3Z3U5Uv_A9gnIgDug6SZrgv1f-IjyFM4V2HQl2dmekMyKQY68uiUcn3Y7W5yj7UdB6XLlvWfePUoC6GKO5vNlJgtKD7d8LD17G9TuO21c2qoO0J7wcCz8R4D6FHoLfIZD8McRO5BtNex2zSvfOP_-7u5Y-TP9qF4IWYwAxBDG91a0yFIqMAFCuG3mJwvjXBFKh_TMZGdHBtXRSYXgHk0_1erh9e7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i139GwfqP1fXK4zbdCcI1jSMFA8TBkdM45loWz_xZDuLVTEPhz5_IH9tLJuRCTX1tymKG4dtwSkgY6ln2b8xvKRRgPSLna1TViPc-5SFSpx0TK5-w1AwJgSXORU4XXyTH2lRjYsUvz1Fi5U4mKx4zcwrTXFdGMeTH2YYtIRZfvJR4KzxmQt9qIH6XfSd6cdlUoGw6SKrXNnojP0uwOdJUeCRGvnoqCfky3f2CXedtSiowev7NdXilOXJj3oSb9nnWsl7-FlKqILOy-AJjsdEr-JboTR5SxlWdQHcjCgryHfShog_rgGfspd7uaeuoMQcwTSONRC3C7jhsy9pstr6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bt5h8VTZVad1nnOeKJuVo_uAavtIAMRAQ3cYFI2prRidjOgTBgobDCzXYqODo3E9zf9xtEOHKyqzHDJdQ_pCX0m26lc5X8vaaiJMyRQm0ueSywnb67HojrK5Ooq2nC1jt3LfPuiIkjcBGlkpUiro0Znij3wU3Yp-zFl6v2npqk5ZpmUpEwAF5VpidKJRF-vI0Q8yKWiLZGZFh-97kBMxo0GEEe7LkXadK5jaCsYRVnyOWQGA9F9PlbGs4EjnaU-l7SQFnOix1rVQ7EeuUGi326rP5Csf0YK8kxZKj59wtjF2ikHsUC48ZlqNvt5SX71btbNsK22lkZ0cqvF6nbF5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3mOD_TL6AMWKgRXFFZiozC05HacwBE_XIrUd8NBB00vvM6QCYnuTCBN3mbMe2JIg5eS1NUiRvecPtgn7VjfMutwJst4lS5eZNWxy0jTnizvFkZSGqpSJkuiKU2Lp9GgmDyJyRMz_RxJnmPR1n09Ck4K2okUzfWS_3GAvHk0yGBQn9HIxK4CwvEzzyHAZt3zIzFJ8Kg5REGRyQuXvaDh3S12sA5JS67S7su8wWGhCTpzNThqROI6kyDBaWt_9iIwUFYC9wzbjKTxqUC7rOHLVUFH_AiB1__IqJVK_mGx0ki67UUJIGqMxLMzXhPAXoh92xhL98WwMjyi-JoGwM58yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458432" target="_blank">📅 00:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458430">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5216002f80.mp4?token=fv8FhoY_vjwwgJHMECRdOg26v1MSmb-N8KxIy4LSR2rWQIcC3VVqchx4bJjUl9s1csJU5m6UQT5Ya7lpW7MDeBiOycE50k31xioMivlG4_GF3Y2UXJn1pk-tznmrKX2HswzyWcE4QSWenU9XhfeoBRhZgQpvcpB7wg5JSyZZANXlRFpQyvOaawEl2s2QhWNgjXY9HbGrxAPGLu7iyVsaqOCflm-Oz9Ml8QYBipnANyaQa51hHYG4Qaw2R5-rwsNNhkxBDV3Dx29FPKjuuYyErx9jIDBPVmg9Y41UvD1fpe7fS__qKUajNDJAC1I0Gp1CGS60rbmsIKczg7Kq7JSMiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5216002f80.mp4?token=fv8FhoY_vjwwgJHMECRdOg26v1MSmb-N8KxIy4LSR2rWQIcC3VVqchx4bJjUl9s1csJU5m6UQT5Ya7lpW7MDeBiOycE50k31xioMivlG4_GF3Y2UXJn1pk-tznmrKX2HswzyWcE4QSWenU9XhfeoBRhZgQpvcpB7wg5JSyZZANXlRFpQyvOaawEl2s2QhWNgjXY9HbGrxAPGLu7iyVsaqOCflm-Oz9Ml8QYBipnANyaQa51hHYG4Qaw2R5-rwsNNhkxBDV3Dx29FPKjuuYyErx9jIDBPVmg9Y41UvD1fpe7fS__qKUajNDJAC1I0Gp1CGS60rbmsIKczg7Kq7JSMiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عراقی از حملات هوایی به مقرهای تروریست‌های ضدایرانی در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458430" target="_blank">📅 00:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458429">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">منابع عراقی از حملات هوایی به مقرهای تروریست‌های ضدایرانی در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458429" target="_blank">📅 00:21 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
