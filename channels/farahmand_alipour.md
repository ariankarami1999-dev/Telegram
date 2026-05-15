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
<img src="https://cdn4.telesco.pe/file/NoHYwl4mcvUU9MJsSJNHkrH2LI8d05XSK4-wB-dhXZ4mVIW14svOjrlsV2xvvzQHFZbVi4dnQ0lOUdpVMe5OsHVtjRhKFJpi2Qt8B1fhNHu-sa4vxb51g9MOGXdMJeDBVbbO-ONyFi5IjLg7ecEB-bhXtKsptGB0xJ7rJKI3WCTAP4SRv8fJasxL3imHwUCr5Z2AeYt-DU7pAunI9paoKDMj_IY9_hYrl2xyonCBtlf9u-z5upMFwJpfMcoArrzDOGm4Wl9SwP-F8VUHahDBDD1siiCDnraU-UV_gkZsaIkFHVtnpCXRlOL5YvBxbVwTvPJqG4qFDmN1eow7l-8MJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 60.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 15:58:03</div>
<hr>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=FXRalYcCLPysr8u2HnaRlRvpLP3XklWzlXt-N71dKhFK_663MPFK-wIKv7NEPodQH2GS0iInxqf1aabgVrZDMocNZtKYEu3W_lUxLteinsN8pgXBT8XdVmDxCV25CWiXCB1uxlJYQVM-uYmF1Ie3XGGg9PM_4n9zDyQwsEcrn0bXPqwrFw4HJfVsvO4in98OSCtjlquPUknIYrIVTkaJqwf8gT4OAySquI9-L1ujQ6wIOGtmS0jwhEfcopRb_GfstFgfL-KD0OEzgvAGq064u_895O9_qItgZgAdy8G63GAmsP12TbltF9I_GRib3_xEnsd2_H4TYSiPyKJB6Lx48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=FXRalYcCLPysr8u2HnaRlRvpLP3XklWzlXt-N71dKhFK_663MPFK-wIKv7NEPodQH2GS0iInxqf1aabgVrZDMocNZtKYEu3W_lUxLteinsN8pgXBT8XdVmDxCV25CWiXCB1uxlJYQVM-uYmF1Ie3XGGg9PM_4n9zDyQwsEcrn0bXPqwrFw4HJfVsvO4in98OSCtjlquPUknIYrIVTkaJqwf8gT4OAySquI9-L1ujQ6wIOGtmS0jwhEfcopRb_GfstFgfL-KD0OEzgvAGq064u_895O9_qItgZgAdy8G63GAmsP12TbltF9I_GRib3_xEnsd2_H4TYSiPyKJB6Lx48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMg5GeC7LmHvPMKHD7YxCLaDcNo7b9thX-MU_nKpp7eay8jBzZRHQAOmyrfhp243_OP4rR8Pf_iqBNclKnTpRdvO3rjGEeQryrr1mtMTSZko1e0hS3K1N13eP8aTzoHQfVKGO2Jj2z_gI9iu-94vrrjjzcoFuDzZafzk4md9sg39Eg2Je8FB8AtpNDLkCDNBYg-lL0V_o2-DaBbk9zGOvOUL9EVLFwV_PipXzQVqJXvUE8WKh7agdIyD8O0cERZbVL5QqFJxfHlUyaaBqc-43dDlXgfrRkUjNz-_sWRhNR_XOc1WSLVgmJVLWTbsLEPVG0-i20dXsDsNXb02HXns9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0ry2yDNiPv0HK9VjVN16-9ch7habE0-j_qGGUXnSLuHsYDmgMFO-ImenA1Opj95gi0Lwt3xZVVYn54C04ZKDS8kF_dRfK00_h3NqfHasVFMSkvhZxi6yrVg9TMo1QJHw7CU5VXifyZdE4TquW6sohmO37D5wkxjBMsaoiormYWTnH73LrXcCWhEuR4FtvO3ndLMYazUlk6bENimBQ13JC05ZJwtKn3ZH0vCgW0Iw615-4JsU4M09JWQUmS8oTXhm9h8wE9C5P2VfAn3GjAvaLMz0jdEfSTsY74jDKDrF9N8e6ixvoDr2jRHCp1xrrNGnyAT1qsHmWgnmLLQ5ibdYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlnVzBIQgXIkYtcbZ6qUtWk7_iokG2H_rnHmojnaVsAwEo6gUeDF0_gvMngFePIncZXk61TbmAMx_UZoRs6mkD1IsuZ7UW06b2QwLalz8mPXMKzw7uJxclRIH44X2iPpORCygyMC7vupJnkmFsns8ILDAH-0vzgxW_aN-2dqgFdQH5zX48ouBCLMSHrSoGfll_0ERKeGX__QpFqqaOOkxy6krjX3_Wo1cOOX1J7nWbuyHPwRXFqzc95Lh6j2KioRLYCLbSkvHH4OQJ3OqrnG3oY0Rvfc5kIrq_RpJz6x0T63l84B5BLPrAdxYuSEpPm4tdwNd0TGvsuIv5WnBEUfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=HBd2p9VFgDu_3V4V4CQapncWDbf9IHmQn8uZluF87qqlmiu8R7Ui4nfhwHdjUO9lFeONZuxUAAgva_4soOgZ4pO6D-YSBDZxE3P_x6YBlkfqZeYXeb0SJ_Q8Lsa1quQyS_78mcogw44fpBGp8MXbufiP-gC6eYkl19vqtp7vkO1ovmCAGatBQju2y_uYCnrC2Es8lcV2dwPO1wKG3pNei938DflFPL6n_o8lS8zNQcZa4NqJYTi-VDkuPArIEN4MUSrYtP4Ob9EbwFXchwCjLP-X_Bldvfr5J6LncGc_N1hX2myxa8x1OZhVSJmkfwuTvWUXtIBTOlI_zlE6qaUd3miPsZ3V6LnyIEDbgi383fD9dgZ843ju3KibIDywRURIcvJR9Z0EelT8msQxW5eutm5PjRkJ71nibx2sPSixAjOrWztJWT9rI0QeQuWbIiHNL3LWFUl2ucBfADXbUR7CmSHyfL0cdzuV-RPhlovvkyfGVGGw6LHW_4ezewIr5QUYhWcfkESegGHIAG83dZRYVRLVcac7raGpIoSWznAZKS46dI-nNXGlIL0J5tjlb84DrScDlj9F2TjgH1lwugGbwTQqapb-Yg9pUYaeCEPj_igMX7KuihGpiWfYlbmJVyWh11NexPovwA5Ve2PTNCB2EKTofq-Htx70XYwe_-mg53U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=HBd2p9VFgDu_3V4V4CQapncWDbf9IHmQn8uZluF87qqlmiu8R7Ui4nfhwHdjUO9lFeONZuxUAAgva_4soOgZ4pO6D-YSBDZxE3P_x6YBlkfqZeYXeb0SJ_Q8Lsa1quQyS_78mcogw44fpBGp8MXbufiP-gC6eYkl19vqtp7vkO1ovmCAGatBQju2y_uYCnrC2Es8lcV2dwPO1wKG3pNei938DflFPL6n_o8lS8zNQcZa4NqJYTi-VDkuPArIEN4MUSrYtP4Ob9EbwFXchwCjLP-X_Bldvfr5J6LncGc_N1hX2myxa8x1OZhVSJmkfwuTvWUXtIBTOlI_zlE6qaUd3miPsZ3V6LnyIEDbgi383fD9dgZ843ju3KibIDywRURIcvJR9Z0EelT8msQxW5eutm5PjRkJ71nibx2sPSixAjOrWztJWT9rI0QeQuWbIiHNL3LWFUl2ucBfADXbUR7CmSHyfL0cdzuV-RPhlovvkyfGVGGw6LHW_4ezewIr5QUYhWcfkESegGHIAG83dZRYVRLVcac7raGpIoSWznAZKS46dI-nNXGlIL0J5tjlb84DrScDlj9F2TjgH1lwugGbwTQqapb-Yg9pUYaeCEPj_igMX7KuihGpiWfYlbmJVyWh11NexPovwA5Ve2PTNCB2EKTofq-Htx70XYwe_-mg53U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hlKyrFAYSZTRMdoOHh4Dkf3wtTjgKKpLwPURpKIYNMC0JPEGwH4afqDOa1sevFYTVB7VTqgZ1E9cjleG7wTAFaRPEvKkmSp6vMvaLKsreRznwuckG1t9OeMo4Yp4vxnoZ6KP08GH1AHSqqIlti0J7yxH1porPc-6CVyFLce5es4tUoO-_sAmFLeidFxWl3h13eTLWLM4H6rFPT3NMWDdEYe6WIC84eWrTtWTCgiR7syjwmzlqmKthbOZiWYToc-KBGVsg9YKlWHZMVSUB32aKRz9jWt2sntQ-7p2CHAU4wLHUyTf0vOjpLXBOPsOQJjq8KIHJwOqnyoscwqGuupklA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hlKyrFAYSZTRMdoOHh4Dkf3wtTjgKKpLwPURpKIYNMC0JPEGwH4afqDOa1sevFYTVB7VTqgZ1E9cjleG7wTAFaRPEvKkmSp6vMvaLKsreRznwuckG1t9OeMo4Yp4vxnoZ6KP08GH1AHSqqIlti0J7yxH1porPc-6CVyFLce5es4tUoO-_sAmFLeidFxWl3h13eTLWLM4H6rFPT3NMWDdEYe6WIC84eWrTtWTCgiR7syjwmzlqmKthbOZiWYToc-KBGVsg9YKlWHZMVSUB32aKRz9jWt2sntQ-7p2CHAU4wLHUyTf0vOjpLXBOPsOQJjq8KIHJwOqnyoscwqGuupklA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=IxRJGqLc_vQw6e7S-LPtjkqaLcmbpNSWVsXEfbZfjVOEQ-VB90EhkfUzOl1dwGG6dyLYJ55465VeaoiJ_KZgvGCn-Str1Y8JZzFhNUVfOwRBSiTl9qBpzau-RMqBwbqowxu9Ey8WY2kGUT0MGuMWgFo6HJTQ2Y2dvZ6iFe7VeShkfPXGlaGvBkuC31hDH9HFIdQUSKuNXZGVM2LmMxihnCI49S_pBt0OlCT_1ze2SybmE5-UokWeid4oepcta-591R0GnKqBPm2cRmaa2anYiT2JrrtoCUyAcTqy_NEDmqJAVuaIR0lqdiBevP6W6ku56Eh2RoF3b6ZDJnOnOWuuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=IxRJGqLc_vQw6e7S-LPtjkqaLcmbpNSWVsXEfbZfjVOEQ-VB90EhkfUzOl1dwGG6dyLYJ55465VeaoiJ_KZgvGCn-Str1Y8JZzFhNUVfOwRBSiTl9qBpzau-RMqBwbqowxu9Ey8WY2kGUT0MGuMWgFo6HJTQ2Y2dvZ6iFe7VeShkfPXGlaGvBkuC31hDH9HFIdQUSKuNXZGVM2LmMxihnCI49S_pBt0OlCT_1ze2SybmE5-UokWeid4oepcta-591R0GnKqBPm2cRmaa2anYiT2JrrtoCUyAcTqy_NEDmqJAVuaIR0lqdiBevP6W6ku56Eh2RoF3b6ZDJnOnOWuuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=CMIf_Th3a8hKk4eRMpkNlTW2zumSTLf08iahw4qaMjn690lL27OucSiYRF7LdFxdEUrzc4hwHvxauc6o4TRCk9bkB6isL6GqjNnvBXzZ7li4DLqBlE76yqlCsOS9risvcN_L2WYC3OIUPWNhBRcfGmLw82FZbjcS_Xs6HPuGyDg_pHNDzQ7pqcSN1mTmK9Qtupo0xdnw-ZJudbQj9fGRFRJ14AY6blGc_3k25m1a0pCwqyRK70tTWjqU-FU3ONEvU4Hlw-Kgm-mIY74ZvHrPgDpGEOgqNw-GCbpDPkCuolQatE7UobI73KQpMIu3ZeUvc9XsPEcBM7YK4dObOUPM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=CMIf_Th3a8hKk4eRMpkNlTW2zumSTLf08iahw4qaMjn690lL27OucSiYRF7LdFxdEUrzc4hwHvxauc6o4TRCk9bkB6isL6GqjNnvBXzZ7li4DLqBlE76yqlCsOS9risvcN_L2WYC3OIUPWNhBRcfGmLw82FZbjcS_Xs6HPuGyDg_pHNDzQ7pqcSN1mTmK9Qtupo0xdnw-ZJudbQj9fGRFRJ14AY6blGc_3k25m1a0pCwqyRK70tTWjqU-FU3ONEvU4Hlw-Kgm-mIY74ZvHrPgDpGEOgqNw-GCbpDPkCuolQatE7UobI73KQpMIu3ZeUvc9XsPEcBM7YK4dObOUPM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooXPqvI1q8taXawnq1FN12dPEqhZLLLOH9FdAjS2xz6YfW1_72kw3Bmovod5L7KuwOrYv1pcK-jlY1NWC6-5KEhcwsvf5RJG9Llsk3Trkpg5z9X_u1uaEBmhFUcfo_qKjSNff4TwDiE_ljzgxlz1EAI2IB38wkBmIm8R3QFqsvhwCf58Wft2k9g8hXTXSqTymsQvwO3z0eOk6-i8axkcMcG0nadoNFF4SAfxi3nY9LvBpSxtZzdZ5aHVNwoIEkaKs2e7L9uWwtD9jgqg185fQcBi64msUvdXLwtuJgxSHg_M92R9OO9gF_ibn2wkLqZ6giqoGLgUvjS8-wPYgkvcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI3NqYvgnYCvdfwM3TIifs-Hrjd47WfjqSrLc-uBMqrMWDhV_STCV0IMAMUD0b9gv-WnErRjOfyfOT8OM4kdoSUxBCC6rYVpM99tLto53DO-bUR1gYwlpbu2xR65zfyJovtyJp-bmmJMVwPvIHTAewRs1264rZNZuyggNyXnFkJO15ZO1Gp9KACx1ZHLBmEmeZisaoHQtCmgrKpWD5jKCfP8FkjEvATQVP8fCcaHbkft8Q0V0R7J3hdjNnZAUUF_yGoULlIwwXaA5BOPGaP3ga4cM1RySMOnSACMN3CC1zx-s0ZeY--KKRFAnKL4C-tBKmj7vyj9-Hn8rFz57w0glQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUu0oBhDBCk6Wq35g4rofZjcc8dXsk8Mbjz5s4n6vAkWnuIC07dfeShI9zOJQdfLPDvqbRhQLK9KKmu3JOQ5t2LU5W--F5gzTffpLybyy2t3akZbcqzmh1xAes6eNvnrd6ElrgMwyAieUmOmyc0d_uQn-Wi8WJ36LKeglrKU4ksEbdydrdNuwEdVN4BtgmHrXWUnPeDIt1k7J4g9BbpOz3SMm9ZbFAhPo7LKnpk1cQE9Euie6lesYIQCnWKKxYUPZiLZKKAqNItJh_DBREMj8II_l7C3Lm9ceJdVktX5zsqVnHfX7pNCrsL0WgBmn37e1y010Byd8lBVVSALTBAgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPaxHTSDLu5iHxfVMZCdn0CJSiUNxCleJKBeHt7ZRjxSK1qFMmmy_JGyuaZ9X7ChLQXP3aQPInxcFyxspQiJAGtQJHdPrsbuYAizLphETsYeLp-fY5k62eOJJj0CJZvahPZApz6qClLqj5toHbr1-xO9Ddlx-5mr-oPncHM_-f6lMG0HXeBGiiEvm4ybmwaCoVPvhThzTXWjlAqBnnGWbUDRhe1CYhTGWFg6sav06OaAAfRhYtT09aY5Yg7AWkYAwOmjW-lPnihkLFwNBlS4VAHSUawXA8hcff_LvlQMN9fUFD7Q-RGcBj8e02lR-NJBsLu40jHxD6I8hxjke9mKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IurKkkurIaML_SiWzrkTAfCq2V6cCLc2n2FF9Ev54vOhVSuDnRc4fKxcrkjpE87VyqtnAOOIcEA_88WlGvq0A9SMJOcX66bAFup3iIY8rxsve9YBtvSU1CsUeXkiX8XYt2lrat7FKxbxbzd8-l-YhjuJ_yZy2WC3G56A_g98UQ8zSaP4vI-4Y5FgSIIa2RbrlHAyulEj_6HbELt4StX4U1Qs5H2RZfxSt3iT7_gHWMHcanzLdXzJfT2G9D38UxrUYnqQ6NbrWGYVQhlaE0mx-uD3iDqeU-F2ry1HmVosy4Oq80kcb9SScTn3cL7eSCqCZAbRm_Q0xw1dY2EOm0HSBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rAEIzmZHIoMTCN3Eh_d-Gi0Afsydscr7zKklblgXS0vph9aRyP0-otTq58Qc94cJuopCrZ9XlrFACT1nDOox2KCreQqr0s0GZnBP6lWdAnEVc4aUpE5vX5JL0ambYat1M-S6UcUtCF4lBgGkTZZTFlgZLUdu-j5phRpYsp98zqy3B6B0odR1Q5QQX1ibu9h1pZTgWo4OTDqQnlOFQ6o9QEBRBKJqIcqQ1NMTZ_Klo_bVF9x0kWBTUvUJUfX5XEGn0ms-vcznu2isvxjmcrS3wWW2DIs9d8khECKEmxPoRr_-1QR_HnY67mHS6T2LQ8_RLyPDsqVy6Qfri7Q_MeA3C-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rAEIzmZHIoMTCN3Eh_d-Gi0Afsydscr7zKklblgXS0vph9aRyP0-otTq58Qc94cJuopCrZ9XlrFACT1nDOox2KCreQqr0s0GZnBP6lWdAnEVc4aUpE5vX5JL0ambYat1M-S6UcUtCF4lBgGkTZZTFlgZLUdu-j5phRpYsp98zqy3B6B0odR1Q5QQX1ibu9h1pZTgWo4OTDqQnlOFQ6o9QEBRBKJqIcqQ1NMTZ_Klo_bVF9x0kWBTUvUJUfX5XEGn0ms-vcznu2isvxjmcrS3wWW2DIs9d8khECKEmxPoRr_-1QR_HnY67mHS6T2LQ8_RLyPDsqVy6Qfri7Q_MeA3C-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=kJnG3e4t5TOowfT8WV11Wodlw9m6aEVFP2ZLxoC59wS_vIlu9rnSFK9S1oMosARfOJ5YPYcV24hvzAU2lW6_FEY3z7_GAaDUi5WAIl1dZCnmru-pxCWiKotLEz-Mx0nI0PsDMIg5CYbN0vCI9yaSK5zFAoW5zYn02f6nJmLErj95pw227OP-lDl9cFgWA-JUiLuFKe_65SITdd8iV7tPZrNbC-BG80GyELPIbOdlXxmzip3ticWOCqiexLexFxesnShptELYftgGHjUB4Vg5Wp_klbcYZaUyt2o-gHM4xXyFIvHGUegIx_v2PAMOkKgcb5_NyjglTfaNc6urGBH9w3jD7REpR4MYafewBpvDuhSLI18k-ebGqkfUURF8Mo0Wd6Th4Gfqco1Z4JWpcioi-WuSHvg5HTM4fkfSgKIPHjVaGCPwZTFbI3g8pcgi-CVVfpmmJXzKhIrk9OdsFSnRShqxYTAAFdOaUpqJCXDRx0cFJXxHooeQ9fCtc4tBQ4Ri7RryXx1jDjkaFGei7g41V4rfTO25PSoYzK2Mc5SqGGXK_II1Wx5LiG5aBDvL2boZLLX-UWMsWZbKL0eXKUq8betkKpBIIyKGtI_AW5nsVWu_oee_p_ElH5PbEGcbj4pG3_vMzH3Ok5P8x9gWakA4J-Vpr7gCBIle_-XsdxSeSt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=kJnG3e4t5TOowfT8WV11Wodlw9m6aEVFP2ZLxoC59wS_vIlu9rnSFK9S1oMosARfOJ5YPYcV24hvzAU2lW6_FEY3z7_GAaDUi5WAIl1dZCnmru-pxCWiKotLEz-Mx0nI0PsDMIg5CYbN0vCI9yaSK5zFAoW5zYn02f6nJmLErj95pw227OP-lDl9cFgWA-JUiLuFKe_65SITdd8iV7tPZrNbC-BG80GyELPIbOdlXxmzip3ticWOCqiexLexFxesnShptELYftgGHjUB4Vg5Wp_klbcYZaUyt2o-gHM4xXyFIvHGUegIx_v2PAMOkKgcb5_NyjglTfaNc6urGBH9w3jD7REpR4MYafewBpvDuhSLI18k-ebGqkfUURF8Mo0Wd6Th4Gfqco1Z4JWpcioi-WuSHvg5HTM4fkfSgKIPHjVaGCPwZTFbI3g8pcgi-CVVfpmmJXzKhIrk9OdsFSnRShqxYTAAFdOaUpqJCXDRx0cFJXxHooeQ9fCtc4tBQ4Ri7RryXx1jDjkaFGei7g41V4rfTO25PSoYzK2Mc5SqGGXK_II1Wx5LiG5aBDvL2boZLLX-UWMsWZbKL0eXKUq8betkKpBIIyKGtI_AW5nsVWu_oee_p_ElH5PbEGcbj4pG3_vMzH3Ok5P8x9gWakA4J-Vpr7gCBIle_-XsdxSeSt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZiHSEtOlXu6RKfzPTQeofdEwsCbPkKdHnkr9TWWUq41LPfD64N3DEkoqYQl__CtqSddZfry1vt4lB3XtXL7FEwtPtDBAEX7QqBJDbn2BtlG4Hfzkxm7Bc7fvME-p6cesbh2HvxXKw6TJwpB7miIKQqLSLxUK3dQldS0NVGgh6rmrG-PLPF7FXDze3WOC5jdwSdKXOMRgE-d5Z039Ko_csj3ntje2vNC7teLQ2StNTv8FoTz-ZusybmPptEIiaYPy5bsKxFcPhALixDC6tGs7PXYCKkEGcHMNlSsupiJVrFlEyYwzt5SPvJhUvBArj09yyWGXUZaUrQ59wlkwkjsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak4pqhgIpNlm6HN07gXC1EUKb2VC-jB13YIMLVj9r6SAf4T_l5xHuBplcYGcsIOdkRHJnsaSfHuOz83OrjPJO3dErV1_A27DF4rJSwzvXCGCs_6bJ0HJynSHm9G6xvfYS2K4FYa8lZjQ6ZUdRv5sJLoEfurQVXaMM2WxBcI8DJvFo_qGOyw9dB1kc_ckw-douMHeKjwm2VLtCgRt4bFW00sGQDe9pXtcMikkXotpkgiqiyDfaEBd4SoDp1DPv0rN1CsQgsesHszxnSzbCS9g1aGAbXLsNx6pPbN7TNxHr5UPyNp0ApJzXeB7nUMxMPeGLrb1kLL04cQFbKB_5GHqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMzxIE4mXZcjp4HS74SeOQcQBYLkO659oRXdL_jlfoqTRd7aC83WfB-FftORiKwHa0Vz0Msm8hZZmL5rmUX0ScA3E5SvfTBX2B-9VMeJNFbSvJKQC5DK1FQDXScrVjAdCbE4bPusDebEKSZLP6BA2QGQbCmgwnTZPf1QgWIWLVKfLi2mbOFo75TbCLnXxinDR90DdbUDg6nehhlkngEYpcwXg3sgSPXjdPydqu6FtlacuUSXSjpWHBWGN4TlA-JsNe0fUDkxLlHuPSF3xF_d8e237O6AllT6W7rUrlD-2jnKOGFlETD72u7jj55qvt4rrRzEDv8W7RCdgJWf-rSOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0oYIUqPuBSmSRlPZIlaE6aShAt9I53Jd0ctwW8nZkglkD91WpuzbyqVQIeS_tKB0z6zQXPOFzU2GOcvcFmNNnl-07EobjORzVLgWWIot06Y-wWr5wCtSsT9QI1Fj2vlxNKGXhJlTdmyDqMYMILhM90a9UhwbNi5RPwyxNXpGMVzLfUY0v3BFKeFIyazJ3RaaW-jmBXaX_JRAZQtZ73iUiSHQJM6PopVzaAayvyXyPNjgOwbOvf-LCTUfSxQH6yZWDiqMoDOojPhtbntP-gRJeovJ6eGo534haUIxy0rWJch_F8je6agzBZl_C4f8br3chUUev0f033x_upfyQ8rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKoybR0ALMrYvpGb9ZDYgWj9MLcqVUbHDmHYQBhjBndbGiLkOvOAov4G11jGXr7c9gyG6MvMUftlyb1iWfeFKOC6SQGn78bJAbunoejfrR-ZV_ISJUOosZ31PzKmCao2DC0gBlY2WrAJrCRRbVjmcEouQNAZAs6u6rDhWOl70dAb_hxl2K6KP8-lQ6RrFDGXiQ9J8NPDtbODfqY9GwAcdiYK3TS80cx96h6UkhFOnexgm5CVvwHtHCdJLpdplQCo9raLnOLKYW6MJ4QiFB4rnd4mEwoYtRp2hXEm8okvr_5OUEDguXPvI2KSgVDfj1vndI0L1YTMWt-NgkdXxw3dwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELCVL9-ohdoHlZpvwhtU_YpEo4u3Xkx_fb7qpfiJQW_-hjs2IzpxEiEog_EbZm_SSaUjB9s2ovN_3wtAKrK0sjL_RSaHNHDb-knYqK2p5djwOGA_IeYeJr_1PGG36NQsmLDZtJZC1CDCHeb2IDeQAx2SHksWMJ1cQbhcRQRhX6--T5Ny0R-A8rYVa09DAzeYasCKHNJtp3C9uOKdmvJAte2T4wtfOzrHZh_5eBoNJ9p_R3GAqltO8eoXYJbeFx077Z2wLeTb9id7ybS8swgBp0BcocDlDUVSExn6l1AQgUXQ1Wyu4rCQq1f4bFx8TUHSMALeQD4lQHUmIGSqn44qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY9u9oQ1K4lQpKes95CFRsifNq84nZ04Nx6hOx3mY5wg5jf8klrezmngyEAatDZOQ8OtrSmSbiYSoMAbQQBQh_X1uZjAJ5wruviAZxKrVQbXbdIkz3GMS4IhZU-sfsVPJV9L5w0DvGf1VXCwgQSHlYOFfKIwPFwdlUXGWTR-3P_bdwqGK-vt7Au_C15Vuy639QJsyiwK9DEjiV6-6_DmLCsYHeQjScpvOoK88-9fI87L0dVUVGdEy5uzpGzEZLYJ1tqsqY02f0bqWUbL-u8VJo1mz2L_UiduLj0zTi8z9KHgG5JV3_z6pWC696XjgPfwwJpDvbZqtJBmXFIJrCJKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRit566NZIHN7X3Mop8NIkyuclR5cxV6GPWrvZUKoGzIGvKqJQIJhQOn0rIYxymaPzDmJ3hfrwhKIOz9UkrEZkMUlm7TJSWRPgfUBRdYDYCHNgiPRCr15Axa3zp5Oa1ScCh32UNmeqHBQN02Njly96NpgzmMJnH7v-zk2XH0kFNyvEtab3e1AS33F8vGaYZ0l3QypH3z3r8FMosXmb8ecOytpqDLX6tkpcTNfXy2MD0HExQaIUQssAiZnnbuaAW9YTtBTaxX05ANA_3s1lshA5oEE6grhh_LOaN3WgXumWe3FsqOcCw8fZPdb3X73znt9_PoR-x_Fk8BlyHfH7Yslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyQA0PF55Qx6kAHxYi4VaraeOHoSCIo_14NMoa-RljMcT-vUTj1k6Te5ASzKwo44qjoqFnVok9Wfh3KOGjVyFGeqvCalRXQPP0qG2P6jA-reWr1wwmogbzyhfiWnQyQHujkA2vOg4VJKtJJyrxuz3Uzd6f0Od4m37jhN4gBTCYCyj_c4vv7VA0PFpGLmWTi2kynb7mNr0CXSQPO9JEYdCmtT2_8mYw_VGzOBUxHjXXynbnzbqbLWPKKVAA7J-KNuP0wxRze-t06b5aMjgZNHsK8YQukqkO8koM8E7c8yUF5AL-z_h3F_7hAjd1YpY9zdygL5NCfkm5nPyO0NYIJ6qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=QaRImqIUhV8wkZRetcd4fy7colhEf3zr8KxnGtw7m56pIaAmvsyXIJe5k-xZ9bSrmHFjXP2aYsBUZljUNGPEOOBiosE1CLeDGx8f88Fy_a2ik89orGVjEFm1owwAf9fm_FGn9-f1XwXlK9Q39ikM6fTUiwWBaofI_NHlaSKkZ2TApYgFUuCBu_ktd-hXtmuhSqJMlll_gZyti0gRPam3AlEYqduswLQ-O7eWkFD11sPZaU9wWr1Y9_RDcqxxWCQ44g0pLuL8sGxiJqExyA48o-TPDmEXUxlS6FU0t2x-BkvNCVMFeSxsPegb1m7Mnq2kAgwsznEVXqScAaA_5gT81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=QaRImqIUhV8wkZRetcd4fy7colhEf3zr8KxnGtw7m56pIaAmvsyXIJe5k-xZ9bSrmHFjXP2aYsBUZljUNGPEOOBiosE1CLeDGx8f88Fy_a2ik89orGVjEFm1owwAf9fm_FGn9-f1XwXlK9Q39ikM6fTUiwWBaofI_NHlaSKkZ2TApYgFUuCBu_ktd-hXtmuhSqJMlll_gZyti0gRPam3AlEYqduswLQ-O7eWkFD11sPZaU9wWr1Y9_RDcqxxWCQ44g0pLuL8sGxiJqExyA48o-TPDmEXUxlS6FU0t2x-BkvNCVMFeSxsPegb1m7Mnq2kAgwsznEVXqScAaA_5gT81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AarMSSO4prJS7xBBTNk-eKpbX0wWDGD_UQj8p3l67k33uo_jTVR3tKQS-N9ZMH1W18XjCFdoSZWZ1ZXshLO_kF1i__AC5Uw46eabUgDtty_HnaSw_XmjIGG_ujaSF0U9-7tpZ1XEGaLTID1zJlx5r2WYvbyyU5wvCTzrU7aHBE4zNjkIPzg305RIdvL6HZASQc17_DgqWrvbRSdyo6wYem1FTgTLdDy_T0l-Alyk4qlXCYkUXU7Nsza9s02LESkvfyrdN34-J07ftB63ww7PZIo5GmN1CX89Kt4wK3dIi4EtAmj6ZTV80DxJJ6vVZ1nQva6_gI1C2vXNzdexv9Ruaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjkSHT_CeLpKbCBmu4txWyoLDF3GUEaIZKPHLTokwC-1iq4HEHesg9dBCFQLxnO3L4TqFdNSozhX766VNTVQxbmQ6tKKA5bO6tLSzytXBz1-E54pEbUhSEvVfcmmapuCUaD9FQowq_s8lNW_tdX8LxAaXtpB9vyAMcvVFc9abPTZgw18aD5WE3bT5UUGuIUy6jakUznDmv80AI374f3Wl_b7V5BFROfylh0aSv4KqCLoky_1bQFxA48zeb98pAHzC7IGRGgREfia1fpLum0NRivLunI275W9WOZHHpjk-GPgvPylLQX3Px6D2xWngExc19BqXDnEqdH8b5KjfLESng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTQ22mlnoAe6oB5L9hMzcOIdGzsElSmVL3uLYX70QRETOYZJSlMwv4OL0tC0Ai0pbih9LqUIb-aGLGg9MM81HN0QN1DFVydBFFi3SXm4op29hNb-kOCE7uxV6BFK27EP4TIpj7G1yG_3amAp5m7SUNPWIIjYKLtqeeHrfcbI7SDQfWKuG3ymm6AihFym1fLEHQIaaffKZmq5advm1REUbzDhqjL1PY3E8GWBYe6-HzxQvujm8VmKGZyERLoF_UMIDjsZk3l3Px_C3uwVFMJEqXQ_nmkZjExSVh28rc3nAb_nMbL8mrhqeU6vOLGJ8qWjO7y0nMur_PbnK6sWblJStw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT4xnSmr4MZzWI0Ld3IFb2cfBA5C1S6n3cQ9Y1aaA8Tz3jloTsIcJPqHwtdCFjgRcbTVljTiiK3qfb47nlMEQcBvA1oIDvOhTJV6S7iVJXAMC3R9QYV5SguUaWk5mF3l0kcrOjE7CiKlr5alsFYbeOqaCD9fT7O8PLt041jsOf4DqChEJpkPc0w7XInfstJxo4a67WHoqezNVtDOF7FaNQ33w2NQMcFVm_5ykXjKDvRoHowY1Je_NkGYqZlMI_thOs9Km_BGT3Gm4I83YhfmRhrcMYsW75jMOWvVmtbOjzKvrkL_xrIw0ljRbYqkQFUQCyCayEtStAdJO9o95f-wyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ترامپ در آستانه سفر به چین: نیازی به کمک چین در خصوص ایران نداریم.
🔺
یا ایران مسیر درست را انتخاب می‌کند یا ما کار را به پایان خواهیم رساند.
🔺
‏من به یک چیز فکر می‌کنم: ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
🔺
با فوران نفت در بازارهای جهانی مواجه خواهیم شد.
🔺
همه زندانیان سیاسی ونزوئلا را آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oC2I1d76S1GatBStfFJYIGMIxWYGiGFYYLwtoMorpKdHqx1Uo-QtnJHFBLfujTikvrwTtsruvzcYxTO7RbIweJLr-4L5DGa1a4Xn70m7cHq5FnYHupNNBiApAvcOvw8elT1iyLF5NfsPdZ7CyU4lGr8FTdJx4UZRhQgHw9-ulhkyq7YUzUgf8_M0m_tsg46-pAwodyBmp0mLv7tCmJyVf2IqIq1-UjQE7j66mWkdQ3cao4Qxb_to9ZaAMJDIrWabf9hRV966wRtqL6sWCYWMbQ4kXgT7d6W8cfor5gCiD0bvRyBcAQqSzOl2ctKtpwp1ojY6yTYBpD1GQMiMgRc2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmBjzqyEVcxEMclRWzkxGnj2D9PAKJ5XOcYDnoGcYfEeRaBT079_d0UYOo8HOO3LPEqvC5ck3_DyMuH69cdoPT5FF17m-kNiOsBNoBQET3g8nD550uEH6k930S-5oqtNmBm3zCwi2vdRzwv8DT6w1SYS7KtdI5fjiLarH4n7Pq6CF5ezquGgFL_POWejQsC7qbjHSdYz9x1v9SLjr3_1MFvcvfqKFC1kmS2NNdriKXdBRitfxO2qsXV2uC_QJsV20wJmL4FZ0WHsnbdsFsyrOGNpo6eU4N1PVBzsGmhfT_uuCzgucRS--Lm5SLoid67fKJ0ZUxFDYLdLh6GhXjLVJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای
رسماً جمهوری اسلامی  را متهم کرده که گروهی
از نیروهای ۳ پ  را با قایق ماهیگری
برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری
یک نظامی  کویتی زخمی شده است.
کویت که امروز سفیر جمهوری اسلامی
را نیز احظار کرده گفته که ۴ تن از عناصر وابسته به ۳ پ را دستگیر کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_ivCvZmSIBfQVpsEAKxOfRnme1uvl6DaW_UVOD2s1C_hyFpMeL1EkL5EygaXR0p5PmMRTfCoYYSaVb0_vKSInYsTWLGl4D8rmGHURSbpdqfLIsdBXV7OFYQ74aJxK_FKgvNWE-uhHhB6WyHVtWavgt7iDG2OFHX2a8D5kaJsFE7kWqUHNABSJcaO6kSxMpv6Kvzy-1kiuZfJ0cd9riwmasIy7q1gLiTa_yIqa6kFkW53RxzV-9KQMI82nunZA7PqJmSDsSFGxn78to6D8dzKd-UfdCwgTUl9gxuC__901F9ew41sEMiDlmy9iOQ2t2oz_bFohaR4TnSX3vqGjOGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8CrYI13e9WsrX3sbShzl1LY0DOUl1fkO76kMD-PuAg82LLZjtpjOgy-MP-nIzKWiOrFG12DyttPBzGBMMKhdmfXUWnAetyy6wk5pA_co07hnMNc097I9H7OiX3yb3zmhmwMDnFO3LNsXtvK0wTjBnzEi1bBJi_RY_BHQh_BHeVf8W351QjKDpbvb9on9K7FkgmjEyOPS1lKZhEQV_bfQh3AxMZ3YgFozCwt_92u-uuFzmNM6sLOFpknJH489WOTdt-Wm1AWkr9SOV5QjpuJd1I8lwcwYjg5jsYT84MLWq9z5AB-TkWuXzaY3lt07WFgDPbBbzPq0Dn7rtSSCuCrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=R0SuUmbye-z4ikGJ3XMDG0FV2pG5BxagJ7fHU0BvRZPHpnyIRSdr4XdMjsf5pzbIzwq_gXX_sLMFah_MLq1nD_vtB-n6saaLctdOoN4pQMW1tXQ-RrcwnhpToIs0EEC-V3L301egapeSQLR1Q9RNf8Vwd-u2Tdvuqv9Zyzgvy3Wc7wmHSAmv1EEkA2ZnU2GkVczYK_1OABZQZbaBw5P5NqP1sLPsLVZ19GPjRAvl3mKob7fPfL1FbNBP3ZKhQt7QjnPbHVHR9LR2zstbQtG-GHu1Q_mQ__4jVQcl32gKa7pOgoDoXqFvYl0dZzF_WqKfEYZgjSve2Ej329lRVsK2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=R0SuUmbye-z4ikGJ3XMDG0FV2pG5BxagJ7fHU0BvRZPHpnyIRSdr4XdMjsf5pzbIzwq_gXX_sLMFah_MLq1nD_vtB-n6saaLctdOoN4pQMW1tXQ-RrcwnhpToIs0EEC-V3L301egapeSQLR1Q9RNf8Vwd-u2Tdvuqv9Zyzgvy3Wc7wmHSAmv1EEkA2ZnU2GkVczYK_1OABZQZbaBw5P5NqP1sLPsLVZ19GPjRAvl3mKob7fPfL1FbNBP3ZKhQt7QjnPbHVHR9LR2zstbQtG-GHu1Q_mQ__4jVQcl32gKa7pOgoDoXqFvYl0dZzF_WqKfEYZgjSve2Ej329lRVsK2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQsGCzV50qnYae02BRLoQw44fCIrJss2Uw1NUrF57-0QTLtenv40oI9Oss34JEQABO9e3938wsi76S7oIru11ivF3myS4wouKQYyuFDZ2lnT-RDLNMLjj_xSU6t5RxNUxon9EiNc66b3l4bxdBL24rkkh2_w4TiVq88WIa1KkXfBOZaZ11xUE-b9tMOF2MGq0eMKpkF9YPJuVlYu-KS0nD9YyaptpfwwJfj7zvdqbSXoL9Ui_asVY786YqbabqLSl5TlPpK-_irgcWeQ_6fPrGHVXTJ9whzYAaD-uyKm29NBAwjUudkJ9eoEN89z_bbBZlFUIG2ES48frdsmtSVETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnj8s9kQMuuQ_jJXxjdUhnFpcEDxgCjdBkEVYaa6lyOKSKOorrnR5LrYWQoEGM5maY5gxUylyHG3hs3-rkS1Wle-tmv3dqZL4Sec7fEOsOY_eqTWusm0OAIs-FXMci_IQTRPEKiTQeOLbMUCiTxoaaF89TgtjI2o1oQCqx2es5k0d-IUCLTPzK7zYknzEdz837xmnCeZwAF0UvAH0XqzG-pKG1ST6HT4ypGakBeFJigYzfI58rWSpD5JxaZFv2W8IMU8Hm6Nd-_GxRdOVlAtUWKnrjX4P39Z3G3-7aG9Pam9Il1AzyteEy8CuhXTKBE-vCTzsPVk_TkbM3DyQEHXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7poeWsfTIy26D0kBkxnE-ghFs-mor5e9LJ32xuI1GO5_YgrnUi25g9AhpRiyeBiSSV_syGdHmxd2QMbc9Gnpms48DxmvMNrLixVVLUb8hzakysCzYySorYLjM28CYXo1N_QQ1SG6h6UrDtA68eb1-20eh6HqF6_VHhqu-fXs_Ml4KxhfwYrxXSscPEsGHkuq5QGLd3YuUHQ_xMr-TA3Mxy5HmIYWZCvoS-AFBTIJGnTP1p8rZKwM8r4SlzfCG_dR2K-08-D8NWzA0oqkdOLTuFOQRjyLpp7NzkjtmNqw1rhtCio3hPLdaNTAlUVl99WIFEbFaHe0EwZvuA6pw15Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMIejJuBFBKA20bN1cwOEMcsWlylEugs5ISfF_Uhx_L2uBA2qgT7Kb003UP1a1VtoUSipuM0ZoSYsLX2npi_71fb6nzf7y53GZcHMcu-UxcpwGprIgo40eDLNC0fmGCsgTVl9CIv16dlrJxDuajHQg1wBCbqMdpfQqY9Iqgh2zWOew9ZFLpxxe997Ivpk04lD76qKnxDqjlRuH6DcrHfQPo_STDBo0iJNNtVSRYd8vko8vGXhB-Xq72Pm5CtcpdfDOUGOBLNg9w-EAENHtWRvdn6YODtnEoBq_PTUGEOIuhDrzbiAHTyNuwf8wrZDAhyHngUawTjMTqCRZqYQMqroQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP0Zo8h7qofdVahYzm5cDTOgaATqbbh4I8Gb6lEEgW12w7xMxvOFHTcmtrQ_-thAFTqrcfCHJr6nezwkpDWsCzWEtLpTQ4Y6_ffjlvWnnvvBXRRfHu5zhB54MgUYxKWJ1QICdGgnBfF0nJ6vJjGAaHJPpITNC-9aB17qKH2Q4RXtR-M_xkwo5_ITNmwYBX89EeNY5ZhQXR2C1PejEhlzi-DuD_GucoNBMJZfICp7Z3n-bTkjGvtjtxB8F6Ywgr7PU2l4siXMzeMWv4joW_lprBwyP0M4gBtjkDdyF5RPiALggRPqaU1HW_iKvFzoqIIBNjsyqMCIUb3L9DEW-Yv8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
روزنامه «گاردین» در گزارشی از ارتباط اسحاق قالیباف، پسر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با یک مرکز پژوهشی در دانشگاه ملبورن و سرمایه‌گذاری او در حوزه املاک در استرالیا خبر می‌دهد.
🔸
آن‌طور که در این گزارش آمده، او از طریق «اجاره دادن دست‌کم یک ملک در این کشور کسب درآمد می‌کرده است».
🔸
گاردین نوشته اسحاق قالیباف چند سال در ملبورن زندگی و تحصیل کرده و طی این مدت با بازار سرمایه‌گذاری املاک و نیز دانشگاه ملبورن ارتباط داشته است.
🔸
این روزنامه نوشته که اسحاق قالیباف، ۳۸ ساله، همچنین موفق شده بود اقامت بلندمدت استرالیا را دریافت کند؛ این در حالی است که کانادا دو بار درخواست ویزای او را رد کرده بود.
🔸
در این گزارش این پرسش مطرح شده که علیرغم اینکه قالیباف، از فرماندهان سابق سپاه پاسداران و رئیس سابق پلیس ایران بوده و به نقش خود در سرکوب و کتک‌زدن دانشجویان معترض افتخار کرده، فرزند او چطور توانسته از املاک در استرالیا درآمد دریافت کند و در این کشور اقامت موقت بگیرد.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1W3csi-LRiBYQ31Iyrbp4dzMpPcjgGBpY8y130HEOjqPSRcrfO9jlEXoqcGOrs2LU4SyNvDTVNOq4fJFawqUoZreA1K5Y0LN1OEDewfhM5aukxd3rQAmrUgNbwxUdwL5zAi7TY3PC75wNx_k7ufNsFaOTuacFJ8I2BXxJKcLrk6yCOsbqlbcs86AgBMvf79LBTsUeyfqd2pv3Yo-B_iMwUzoKb2Znv3AQdA1DbG25YALHxpFDvjj4QtvnVg0__Ok8Xes1MrI-MDuCXvT4-dZk96G5F60MX-kiEbRlN_zlsp34eHzChBUsafzTprkg_sBV4v1punJk5t61bOPK73EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glEuZILAuobzKuzW2aYlCd9K1Twd24f2VyQ1nrTpqkSYLqt8ABStuKnchMB5xPNS9ns89sU4gB2cDRVaxPaZcac-Hs0bFlJAfv5Okd6pmsjNGftCaBHjXWTsZksAJYm5IS_5WpCK4vyl8TRCdUpVV6kdIhDC8mr-ogJKb6bq1YULr7O-rhpHe0rLiLvMhrd_6_kzhVNg4G1PBaL0JVgMIyrXSllBPCUX8wlH7xhLyJ7iNBO3iRGLKQNdRDGyHushzhEFVAQ5UrxPqidhSEEhWXjEVIPtjnt92GssWMpc3mDXlfwqgykR6Dk_e7ZaxtLjNjjJV6lpGQCC-kXlrRYDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvqABya2Vh1XaY3ZKJqoRe5AY35ecz7pf2nfNgmeRh75yipnmA2w33DwBesPkZDbsnrKdH1Ur0inmY92DjWHVgURl9aibJ_zzID6KMg0HaMTlQoyqG9ACq9RyeSlMtf1ac3OF5vhkKelJZoPFkyebkjusjzv1xK3zZk1iO_-z70a04Xq3flqtJSp0dhWSihvYU1AMTk1Z_WSIBmUROWrIpbt8aYVN0Qb7TBPz_H61RHTRgv8jp8zfSXeAjXB38LFuTmYCc0gsqbc3DuFYwBrbqYOtZNTy1YpuQWErLaW6Q3SDwC0-UeIjzN1pLHqLdmz8pvlMRuBFtw_s5ISwDsVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
دونالد ترامپ در تروث سوشال:
«
ایران ۴۷ سال است که با ایالات متحده و بقیه جهان بازی می‌کند؛ فقط وقت‌کشی، وقت‌کشی، وقت‌کشی!
و در نهایت وقتی به “گنج” رسید که باراک حسین اوباما رئیس‌جمهور شد.
او نه تنها با آنها خوب بود، بلکه فوق‌العاده با آنها رفتار کرد؛ عملاً به سمت ایران رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار پول، و همچنین ۱.۷ میلیارد دلار پول نقد سبز، با هواپیما به تهران فرستاده شد و مثل هدیه‌ای آماده تقدیم آنها شد. تمام بانک‌های واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند!
آن‌قدر پول زیاد بود که وقتی رسید، اراذل و اوباش ایرانی اصلاً نمی‌دانستند با آن چه کار کنند. آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید.
این پول‌ها داخل چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها باورشان نمی‌شد چنین شانسی آورده‌اند. آنها بالاخره بزرگ‌ترین ساده‌لوح ممکن را پیدا کردند؛ در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی.
او برای رهبری کشور ما یک فاجعه بود، البته نه به بدی جو خواب‌آلود بایدن!
ایرانی‌ها ۴۷ سال است که ما را معطل نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً هم ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند، و به کشوری که حالا دوباره عظمتش را به دست آورده می‌خندیدند.
اما دیگر نخواهند خندید!
»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNgbUL_LZNKuJ75GCHws_ETBPRzGjBGiCm86ZHqPZxRK3nEC2JgOOaKKi_HBCuMiHa-vIoV8WEuC9Vwfw9trW5DNJUMFikp44MvFV98fMi_0iGvepqJZ2fU7Hcw7bFksg4bno5pW8SnOGfx5zAy4vE8fR81EtMNNNw51p8q_dNTONjl6X3ia4Owqx2Fpp2h0L8gr6v6xpfdsRSNTcG_L9S8Obmv0-kSyPkJICJtK4W3oLVQjGyK01JvSztfrhyfrsR0NtPhu1LuHqPYKKY4i7qq6-0CRmhaBJXbHWemfDw_UISuio7LjzsalluwKQzBsS9Gd4fnQi3WxrHdf-Wee-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه چرا کمونیست‌های ایتالیایی نخست وزیر ایتالیا  - الدو مورو - رو در می ۱۹۷۹ کشتن!
چون گفته بود : «باید قدرت رو با چپ‌ها تقسیم کرد!  اونها هم ایتالیایی هستند! نباید مانع شد که وارد دولت بشن!  دولت ائتلافی ایجاد کنیم اونها هم باشن!»  کشتنش!
کمونیست‌های افراطی کشتنش و
گفتن : برنامه داشت تا ما کمونیست‌ها
رو از مسیر اصلی که مبارزه بی‌امان
با لیبرالیسم و سرمایه‌‌‌‌‌‌داری است منحرف کنه و ما رو به فساد بکشونه! در حالی که وظیفه  ما «انقلاب کمونیستی» است !
و نه سازش و شراکت با سرمایه‌دارها!
و‌ همین چپ‌های افراطی (در ایتالیا، آلمان و فرانسه)  که به خاطر مبارزه با سرمایه‌ داری به کشور خودشون رحم نمیکردن و دست به بمب گذاری و قتل و.. میزدن، بزرگ‌ترین حامیان فلسطین شدند (چون اسرائیل طرف آمریکا بود)
چپ‌های افراطی آلمان حتی می‌رفتند اردوگاه‌های فلسطینی
کار با اسلحه و مبارزه رو یاد بگیرن!
کاری که چپ‌های ایرانی هم انجام می‌دادند!
خلاصه ریشه این داستان‌ها و… خیلی طولانیه!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=lTv3BUT_iekFXoqmYG2gAyXdWk9GCddxd8ZiCQgA3amzr3ZuVhAXQM0y5f2KBeePhlr2NMLw99L5V7zwkdA1LjIZWbCSx32_px0yET0BIGtL-Qd9MJ_dlX_FwWp-s98XpNyP7Z1LQRWUngMrPqrnZhO2Mn_4F_OszH87u_o6ZD3pYDm4ROajlXOs6npSPEDVKyulE_YdkZqW0wHyMQyz3QEjIvAqsyzbX-I09jRYPKw_-vdO4dsGXRX5OdRSVg2za_187wMtEsoK9YeQ6p03Zgu35szYXMCu7mTVfOTqj2eJGydqCeG6bHeZw1F3aRvmMY7ckxR0BU5xxZIeWlvn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=lTv3BUT_iekFXoqmYG2gAyXdWk9GCddxd8ZiCQgA3amzr3ZuVhAXQM0y5f2KBeePhlr2NMLw99L5V7zwkdA1LjIZWbCSx32_px0yET0BIGtL-Qd9MJ_dlX_FwWp-s98XpNyP7Z1LQRWUngMrPqrnZhO2Mn_4F_OszH87u_o6ZD3pYDm4ROajlXOs6npSPEDVKyulE_YdkZqW0wHyMQyz3QEjIvAqsyzbX-I09jRYPKw_-vdO4dsGXRX5OdRSVg2za_187wMtEsoK9YeQ6p03Zgu35szYXMCu7mTVfOTqj2eJGydqCeG6bHeZw1F3aRvmMY7ckxR0BU5xxZIeWlvn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به مارکو روبیو در وزارت خارجه ایتالیا
سند و شجره نامه خانوادگی‌اش اهدا شد.
خانواده مادری او ایتالیایی است
(از منطقه پیه‌مونته - تورین)
و خانواده پدری او از اسپانیاست (سویل)
او کوبایی است.
در این مراسم گفت : از طریق یک اپلیکیشن ایتالیایی تمرین میکردم. همه رو متوجه میشم! (به خاطر اینکه زبان‌ خودش اسپانیایی است، متوجه میشه
و نه فقط ا‌پلیکیشن و تمرین ایتالیایی)
هر چی وزیر خارجه (ایتالیا ) میگه متوجه میشم.
اصلا نیازی به هدفون و ترجمه نیست.
دفعه بعد که اومدم ایتالیا، سعی میکنم که بتونم
به ایتالیایی هم پاسخ بدم و صحبت کنم.
باید اپلیکیشن زبانم رو هم تمدید کنم.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4898" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwqbJf95llWj9Tofq7V1OfRC5mf5G9pGbUrMyEONi31E6NLL-4ntLFSnoSrtg02VX6OVxvFLyqJE8_ZY7y4fin_qLNagV05IPmtyr9JjsUqeWaklOMAg5hZ6rEylgKSS8_N5r9-U2UBuWa1Qc_ClcaYP0uuUd77znB5aZsXRGVYu63c0N9gcUiMM7QQmixVaShkuugRnhfcDcpX3jaEhl-IX1m6Jbx_5iteg8BhXUCm5cjA4tYVspuNfzWbTpRFjUg2o3wU1uZMDPEQr-bXbk_7SlHLZ58RfnTaK9Z5O3JtjssLtVCLHnBizJBFvlSjJRHRh3qZJ1FF1T1yHaZ-hfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcdqw1aA_wK3xqBCjpiRjDJYPdSGup-Zdyjm7l7tyMaLn2PA7PMv5VG1Vi2p_4kn8JMnSAzrH85pGPp6q0SOCE8E3S1PwqsvDdQNcbzbSMiEzFIcRgIa8w6KMwJ5G_3tYrUG2JQq6SqG9U2Gde5CQTtPTSRkD2bCuU2L6_B0mH7VSVLkF6BbZR-SWdVofCWrJS1pvcEd18YAxu0sG_rPyrdkh-EZHa4ch_jisl0hmF_hkG-SlBb-Iwpfh7p0WbZoR-LvxLJHsUO1B_4Gfrf_A39otH45LWmjdWO7ZQF7u_uxkXzuObrbBWdrDrMdicGX_WI_SFUThf4ZiPy1u5qbvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=kbeVm-3OsCQucYyzmpvd98ZnbKk4CesRCaiIvaQTxbxVsDEvffbDnLyk4UMhv3z0t8VySVx1uSX0lEr_hld9EtLVQ_buDB91qO_lVNM6VJnzf5w-JGMyQpX4wYgWU-PJSyudFc9S3uYleHo3Oa9590Y7nZ8DOOofBxM7nP-6hLsArHYSj18OQP5DAcJyeN0I_wjrOpHd-yMjHuoSvTqDEhVIP-95BjgwEMm7KOBunx1NMfDtj5Vb4ajOFGVdk-0NKuhiicp4fUPRxBzMReQo0vzYfdDwfuJJD8LRkQ4MiaaOCv9OAELFcafXD4BlhA-svbAhpxR4ywNVUOwPqca2wjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=kbeVm-3OsCQucYyzmpvd98ZnbKk4CesRCaiIvaQTxbxVsDEvffbDnLyk4UMhv3z0t8VySVx1uSX0lEr_hld9EtLVQ_buDB91qO_lVNM6VJnzf5w-JGMyQpX4wYgWU-PJSyudFc9S3uYleHo3Oa9590Y7nZ8DOOofBxM7nP-6hLsArHYSj18OQP5DAcJyeN0I_wjrOpHd-yMjHuoSvTqDEhVIP-95BjgwEMm7KOBunx1NMfDtj5Vb4ajOFGVdk-0NKuhiicp4fUPRxBzMReQo0vzYfdDwfuJJD8LRkQ4MiaaOCv9OAELFcafXD4BlhA-svbAhpxR4ywNVUOwPqca2wjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
‏ترامپ: «ما هر سه رده رهبری در ایران را از بین برده‌ایم.
ما ممکن است دو هفته دیگر به اقدام نظامی علیه ایران ادامه دهیم و به هر یک از اهداف تعیین شده حمله کنیم.
ما اهداف خاصی داریم که قصد داشتیم در ایران به آنها دست یابیم و ممکن است تاکنون حدود ۷۰٪ از آنها را محقق کرده باشیم.»
‏ترامپ درباره اورانیوم غنی‌شده در ایران گفت: ما بالاخره به آن دست پیدا می‌کنیم، ما آنجا را تحت نظارت داریم. همه‌چیز تحت نظر است. اگر کسی به آن محل نزدیک شود، خبردار می‌شویم و نابودش می‌کنیم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4893" target="_blank">📅 18:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHD3i7hRqvhwhN-LsdpqOfmQqFCYBUx8n0zIgMWUM1-rKcEiaPBALREF0WMuoinxqCLD57wS0b50E4R-TBmO8gHOPBILYb1LvNvaGAKVIkNvJjcfuPKcRhofSHfXdKLk424qthIT2DDyqtR5ECkiVUv1eoMK7My16-LbGXhc3Z4Ap_SuFqCIn1jXeL6NdImZISin0UB9ezebgE0whas3Pg8EihWYfBaPpmgqIdogavg6p5Uy9iseNYzC0ALez9LeaqOcGV0x-Y665zmejzGj8lYmTC2VM28Fz_KC-HX837--oo6KPAygeoSilTcyp2F0E4ffocCQBOWLFXVY0nHhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilpy6FBnfAqSQRiU6LtQq0Mo5opsGvi7MCLHF6fBx7lYf0B7bWbR2xzv5MXdOs46kLx2ClhbBjJd0utRPyaUDfSsihbyS_Uqb59jwVwwyc8gTqXjOZ9mxHxb3tzPlRHGYEQW8LxW4ikIYu31Rsq7Okz_S7iT9JadVJ0bJ496_vXKLkuAnwhRSyckothj-AyiNHEhG4HwrnnpePyb1o7Vv79C7lVfUBBfOxtOrwyo3FfUS5KHAToDhitTVeiZm_sseSvXkxrPiVcIcJdEhLkGG6UfHS7BKelpjBfpvjpNXcdt1hx1fvipex7DId1LQNkMGCX5a8Fg3E1kGFF3O_601g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰ سال پیش در ۱۹۳۶و در آستانه برگزاری بازی‌های المپیک برلین در آلمان نازی دستورهای خاصی صادر شد.
مثلا گفتن که دامن زنان در این مدت
می‌تونه ۵ سانتیمتر کوتاه‌تر باشه،
گفتن یهود ستیزی باید کاملا متوقف بشه
که وقتی خارجی‌ها و خبرنگارها میان،
بهشون بگیم این حرف‌ها، فقط تبلیغات
دروغین خارجی علیه آلمانه و واقعیت نداره.
یا مثلا دستور دادن، بخش زیادی از نظامی‌ها و پلیس،
با لباس مردم عادی توی خیابون باشن تا جو پلیسی و نظامی به نظر نیاد و عادی باشه و نشون بدیم آلمان نازی اصلا با تبلیغاتی که بیرون آلمان میگن واقعیت نداره.
حالا توی جمهوری اسلامی این چند روز
زنان بی‌حجاب رو ویترین کردن! و طوری وانمود میکنن انگار ما اینها و سوابق شون و دستهای خو‌نین‌شون
رو نمی‌شناسیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3i0merBbY2jFMrnNO2d_785HiqD16DCl5G9oiS4RtRAc7m9fRB-0SBQJWlrnh4HQRn2DBgiHDz7rXXO8qHntxeKo_tsTLrImr-195BlIMWU4xLG0laEYghnFaCuGiWMp3O9Exre37A_eRi2eAMzmVqo33rg7A9-X2Qpev6N5PQy0lfCnvULKIgbqghZkslTOlcY6kPJIjTnjecJaPcRrz0P2MtLFciYwmP6AlJL6jxXvIKJhZqh1-RDlo3dJNej6HLa_vd3bOvyVOjuzpB_kaztjV41Z6EWgStvbG6BReUQykslgLyEG6Bn0eII5QxWP2myuCl0o04ceAMs6SrQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdTjFiwOMcaMlWiYZbAowqG3LgLU37ZvhA8TykJszPyx9ErCUo6srw_Xh7hKJmUdO_xdj09R39wPrkC2W82DKr3U_UbM43SwWDgC8YSt-DXYyqDIO9K8lWlOfeXplNGzY_bs3jmCtmg9KdIlyetTMVxFuqljQBZFrtHMsqkK4aOj-0O1WWuBCIXq28GF9hvDvINNw5EubOgiinK4f4W0wiRl0FvVjISnuK1V1nsXjyaKVpeN71GW9E_gqdqytpX-WQZw_n5jc7MhNo5PLdlHMBGM03cd5KtAIBBIE3B7RKNKXgobUaztWFwUdqsIfZMQJeeJ-mIwMZ_5xl7FlIScJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuKPX2A68lqoqqPF19yQNGB5thCKHE3Jwnap1ght3Qd1AaIjLMMq6Eg5d1mefbddnToOF8tcG-lCy2j2I0f4UTsWUWnSMqL5cTV-zn7AGJFphpSrm8WUrc9P01IC1ywrDVQVwfngMUHf5IvsbvQJUEypEBhu-ujf9qzKvWyRUg-sYb1eyV7_gQWNjIBhRxFz1d3BDuckYsS5xgav7KwbFFroT4dAWIzEuPWdovk4BeRI2NZEk8cHS-EQBM_hTCx39PJAkM16o2ajMni2F1H9j2gz1OPk_26SXjT39lAuHwGZnl1Ckyn7Y09fVa6c7AbXbLToWKAMlqkRIyLFImXt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ‌دست به اخراج گروهی از شیعیان پاکستانی مقیم امارات زده که برای جمهوری اسلامی تبلیغ میکنن.
🔺
امارات چند سال پیش یک وام ۳.۵ میلیارد دلاری
هم به پاکستان داده بود، که چون پاکستان
آه در بساط نداشت، هی تمدید می‌کرد،
که بعد از خودشیرینی‌های پاکستان برای جوش دادن معامله بین جمهوری اسلامی و ترامپ، امارات بهش گفت سریعا این بدهی‌ات رو پرداخت کن!
که یک شوک عظیم روی اقتصاد پاکستان ایجاد کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/4880" target="_blank">📅 12:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHJnbYx179DICbOZi-2AsMDvq-QI3TjcHXpw3J63o3RId0ufJM_HL6qF-8C1I--vgukFiVKJxjdVKJXZbMnmxk20GlAJfVZYZocE6mRRLlxNDs2khSMNUa33Xli-e9IMWkezuw4XPoBnnzPjLm4ML_9CrzOiljcFY9TC2ngsT-2N5dWFKMO06PaXp-TXFclcnLjg8H2wGJwLKvsJw4vVn9yfys-gDtBuvj8NsV_K3eqq4kz5g0GDhX8eCMnzZcwXgYRkZstC63UA_1S2-sE49bVKDZeR5wPuT-VwSBHjNI70YSKyVHGOH4FxJNL3cCi_srskhyLgMXvjbvaFnqmjgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت «مبعوث» شده :))
این هندونه رو  این چند هفته حاکمان
جمهوری اسلامی زیر بغل عمله‌هاشون میگذارن!
که منظورشون چیه؟ مبعوث/ برگزیده شده برای مبارزه با آمریکا و اسرائیل!
«قوم برگزیده» لقب معروف و شاخص قوم یهوده! برگزیدگی هم از سوی خدا بوده!
اینو فقط تورات میگه؟
نه! قرآن هم اشاره داره بهش:
سوره بقره، آیه ۴۷:
يَا بَنِي إِسْرَائِيلَ اذْكُرُوا نِعْمَتِيَ الَّتِي أَنْعَمْتُ عَلَيْكُمْ  وَأَنِّي فَضَّلْتُكُمْ عَلَى الْعَالَمِينَ
«ای بنی‌اسرائیل، نعمت مرا که به شما عطا کردم به یاد آورید، و اینکه شما را بر جهانیان برتری دادم.»  بخش بزرگی از کینه مسلمانان به یهودیان از  شدت «حسادت» میاد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/4878" target="_blank">📅 18:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR-p0AOimbI3dd5XF6Oum0VLJ7pYvScxApuKnrMFlbrffN5UAxGH7gdq8IAc3n5isT_J7jdzGazgKj0IYzZGANPhTZ28qV3HmIHCjqzY1n8wEYn8LC2JrOM1IecBcysAiSuDVrCI1MOmLizZ03Qr_Fo7nYUy-ceDk7CQpG69sI4O21_7GMG0_XHbGsIdsxrcJaWGKL_pHxgG6Zsjy4KWmcDPf4DiLC1-RBx8VENdexorx3hQl_UT8RxZXLeRO06rwxb1-eB8-PmzYRDgKu0JkdI7_cWO4rGtqriafsbseEp6HsnJV9t1rCa4h68Q0n_BNHrslCbD0EFgPkFyXOKv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط واسه اینکه
روزنه‌ای متفاوت داشته باشید :
در قرآن بیش از ۴۰ بار واژه «اسرائیل» ذکر شده! اما یکبار هم اسم فلسطین نیومده! حتی به روایت صریح قرآن (یعنی
آیه ۲۱ سوره مائده
)
موسی که به‌ دستور خدا رفته بود قوم بنی‌اسرائیل رو از مصر خارج کرده بود و آورده بود تا «سرزمین وعده داده شده» (فلسطین) رو بهشون بده، میگه : « ای قوم من! وارد سرزمین مقدسی شوید که خدا برای شما مقرر کرده است، و به عقب بازنگردید، که زیانکار خواهید شد.» !
يَا قَوْمِ ادْخُلُوا الْأَرْضَ الْمُقَدَّسَةَ الَّتِي كَتَبَ اللَّهُ لَكُمْ وَلَا تَرْتَدُّوا عَلَىٰ أَدْبَارِكُمْ فَتَنقَلِبُوا خَاسِرِينَ
بله! پیامبر خدا، موسی، به روایت صریح قرآن ، به قوم یهود گفته وارد این سرزمین «
مقرر شده
» «
از سوی خدا
» شوید
و خارج هم نشوید
!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3J9qyXB9Uuru35-37ycnTSlCLvC5rVN6r9uA_ocseZVXczT0YDF3o3Ax-2HRMzKxQKx-klvF4SC2a2bOuSSc06jxmqD06bZBs-3qoYbwJDQlv2vIFKmeBXFECO2A7SQ70WNMHt0iWBnYZ5NfpIeRouKuM-97-GUqUtqUb8WlSfGa6Dbq9SG6UnV9H7aYld4qFueai47mYm3mH0Loov4AAaM5uYvgg5taxvFiPNK_d_rkF-D5THnNclWlP7elbhktXtk43D1PKIKYbu4hmVE2VLW-nVozdTsFwimpAESdLJltwo9qpUPyTe6MNEh73NkSfZCG9Zzezlo3MFwTPYuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSpN9Vfarux4YZmkN9RhWXhdblOnu0zfNzTCPBNgLY4S85OrJ_pPq42OM5Kkf_o5BqWkv3D3SE5tXfWW7eHMFYTZ60egjTTKTXqL8zlGjs2nOwNpFFTJash8nqS5PC2113xCkrLjXmreiPwS4LBdChuwt9qUodm_szcIpnbdRuOZ8zTldL8JKyY3Ek1xCJ-qrM54jyu0n8tLlNGBuJQ939T0PigCxyNc6PC8llkeVQCkgdY9N1f9W41J6eFHrRKJNvnL3BbXmuupEfZG90wZYLUbyq-If5IEDNyN3mYsEDhfZkr6w5V5MhwEv4Ibx4RueKhdH4hPwP5o_a8JreUylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5lxEZCIepp9Y5f9UzPaA38_WOZaG1A1Cf8q8MHX2qb-vjSW6MVTWqxtH1DEzvfDow6ia-RiFs4M2DNkZ8Nb0j2ESNbr2L9H82rz0EnmqkqMNVxvC67V-nI-fZVAADvhAyS0alKSkxoe3ydNFdJol33iphFOZm16hV-0UfXDmBmyGw98yRd8KUngYgEky0-Rgtbk6uc18Rob9tdslrLyYWTCSra2d2HRIgFGafscFAEqGlN5MVtoPW7EyiEXzdOFvL5JlAAuNfPPX77f6DaZ4PX2qVJp6ilH8TEtFe02I37G1bZnsmwDvXJKZHF-jig3wgOO6lAKW7TBqVqAEO5wPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsc8PPN4sgaHEBDPdol7HsNHh8BHKrjnyXzg6a9HODY_myzmgk28yPeYhMo0kGxmSjjunTBIzpCCI4TYnPxL58MsHw79h3vZKhssHfYnV9LOssuoY_fCja-Xi4Vwfn0i6U-mQ1rP0Lbz6iAHhwfHuupA0hN9TBOgAkPzhiA60zvhf58ppLTCE8_RgBJ02uSUdHwvcaUa7NAvQ2zTYvQBTNyFwc8K04nMGUobLHRuW5Prw1tw299hDCUeB4Vh5jK7CMLIjGvqHUHSLMNQqxK5HGkFh1NM7vU8v088abB_vfHP5N-LVUViMCtOVM5Wu3Wxijob4_aK4SMIITc_lrqIhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIAaBzlWvqjd9z1L_xTJN381N78ZVvR_Ry7U8nCzDsUSWlHtYqjzSlxsAdH1xXkik2L1IJXdjhB0-HjIOq2ehUXIFV1iFNQMQPpmH2b8_7TpsdkiL1n7-cizCK_ZcUYs5LL1Tm9Ooh05u4L-RRTGqX9JHoGD5aA-bDxbzOaSADZguVdMCD_nKjRAMn7egBzEl97V2m_cRuZXNAOUfmUFulSmUaSu2lvff57rFRZGS5x6eI4xBSDN63k2HXcggsSXmR2z4So4HQPWNCgwU4ilsvx7xMifHv1ME8ykciQ_EIbQm_toIdvO3Bi2Vy-1xFPTqKKIYKrE5c3jC702egcbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvMwSjWdxsT1Y618XEqqbgi0FMjeVG8q4NSGdzEg5obfgVd-C651BN_9VdHAlCWvVfRkWKL6jPpTZCDxbTG89PC79SC5Q_cGZKGq3_l9sOuTylbYuUUphg4IIvuz8gy4Vez_PVWESibJtOONVj99_uAWvSrcX9YdNAGt89uNDsu-EGRZLro3Xy1ziZw8_yrkIqjJp3awLLVEeXfwO-Pm4Xp_zmNLuCoF0suZJ-_as5nlZ2I6GGjpZJ_TkjdwW0IsP58Iox_o5KAn4VnWKeFrgJ952Q25CA_5ojIQ2Kg8MtpkyaGYf2aZ42t_LgJRK0EDvUdHNLXaFiJnv1IUag1CaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=JCeHZzfbdI9087Ggz55Gd8dSuG63ToIlGhXsFN0xEaSAjQgItrkMWaV2C7MW6PDC6bF3vakNLDBtgcjXOAkhpI5YkjPO4_Y6_UrfVDimCH2L908J7--ZXPvf52NB84A1c7l3oshARJZGNJB21Z_oecTH4wM0KaAihjjMT0nKyRPiruR2TVse1gqMxGJQHRognlYGhPp7pUy1cWY7Qfx9MMXXj-gmHATDlkMbZ4vUAvTkg8gZQDGEfvEDqBI0vWufPPPGcQOKGTcokCekv7y2Wr6d2JRhosd2AcPcFsqvtm3FO_GCpeKGb1KXfOwvL9uGPkYPjuDgEhOhOMyWJJg2bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=JCeHZzfbdI9087Ggz55Gd8dSuG63ToIlGhXsFN0xEaSAjQgItrkMWaV2C7MW6PDC6bF3vakNLDBtgcjXOAkhpI5YkjPO4_Y6_UrfVDimCH2L908J7--ZXPvf52NB84A1c7l3oshARJZGNJB21Z_oecTH4wM0KaAihjjMT0nKyRPiruR2TVse1gqMxGJQHRognlYGhPp7pUy1cWY7Qfx9MMXXj-gmHATDlkMbZ4vUAvTkg8gZQDGEfvEDqBI0vWufPPPGcQOKGTcokCekv7y2Wr6d2JRhosd2AcPcFsqvtm3FO_GCpeKGb1KXfOwvL9uGPkYPjuDgEhOhOMyWJJg2bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،
یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت
از امارات در این کشور مستقر کرد
(همراه با خلبانان مصری).
رئیس جمهور مصر گفت :
«هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر قرار می‌دهد.
ما از امنیت و ثبات امارات حمایت می‌کنیم و تجاوزات ایران را رد می‌کنیم.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4866" target="_blank">📅 12:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KggGZ7ry0ZuVQHIhl3DjIpFdv11KVaz7gLgH3fNnEp-CidKwB43V8UC4XlEtVdQ88sMhMWFsmpbFFI_k1WAhIHa9-20nq6R5dqzWLUVBGmDv6yKvGiOjl_uir4TB0q0KiC6ke5D5ZrwJdFMlW_UrlF6Qai83KnOUsvnwzR7OoyswiDNqqV6xa9JM60ltb3fRIJvj2b1mgv1IS6x62KyzUlbtdvPSdj8TClqkrEtA0d0RCh1EBUa0SPb4ONR-ldYUtqABRks0qbB4VNOZHTvzth0n6P93xz8RAQTgyKC4M-POJPfBQknqef3-g-x7J1h0Wkp76FnSUg5le2nfcgCR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8zsPEyaqqD3fk215bC8t6i6KeQJq-77pR6J7N7zeS4CR2seD3m28gpGR31fiMzh3kqTCtText_dUKauQ-RpZBKG5W_Wm6de-uPusZ-HOvSfFe5IomRRj8NTeGVf3TThQH5fwybcliQ66im-DnseQW7Dl93vPgMkBImFm6Gh-8gx6xcQO2Gad8kpRiSbh-AcRzQzJr-YglAMP8Rf3i4zeeHoHfcIiPZ-RkbbWNnTpa8eyJWJ_WSZ-daK9eK05_IRXMwZmSC-7mNOk5qw8SrffDaMrhE2OrxNEUfcPpHciweeraON1KO-qPB-_Btbw5TW4_E7YiGdcB487oL2ab2xXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPlxc1M7BO-bvcf_L6lQSSGpiLLxt1t6FZRU3-6cIwk2bM9xLFcv6NhmYRATBUdUKugZ-dvpytESsvxDSyjy4zoLiK8ebNLYTBqUWY2UR64GKA3ikV6_64JeV16Z-eCB7NucXPGzOgN-YSCEhvvQ1h5MDEyEkSZe4Xac1ROXWXpqKbFTnczppafhFZzQ2ZNUCjwIz3pOY8Ri722YFJvUoM_-5N57pG43xx2_W-53DLxUQAqUAVU52OSVR5pM18iBwketYS9bZ1fPEdtcYB3V-KjrYVMY2fsKORMPkmPTNrx67MfENBTWfJJW6PjUfy9mgwnkSFo-Ub6vlOaiTtI77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucGN3uGul38d2cfaNPs1yHL1QIw2Q1vN2bs7zIqQ1BukB-JrPheTC6ETPChLbY8n1z_TCyb9eOtAZmgIXkMiBRa59BAn4lLF9zRENx2Hvvnb60UclZKyWiip5xf-Ipsts6SwnacoA2dYSDtCrCruJ0HUPIgkAALtSMOGu-s7U9NDDq0yDhj6y-5gxCxESRY4H0sQdSYYeDfr7CCQL1ztVEUMOQzd4VbhEWoOZ9aTXg3sYfrvKJuU6NENN9QsR4xnhMn-B0u8I19_1ud2CXeUZ2vje5ULGqmQyzzwFH2zDvgWlKI3O3jz-ZYn_dbeBCH7LPdXElh0gYx6fGrOnWTVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHpv7pMP62M8AKB8zj3sj8XotSkXe6O2Hu4xxLL49qI6C5za4mVd6bswz2oyBgHcfuxm8Q_-S3huQqARedYc2YYOGkO11dQ3X2xOaGkNmgUbRzICOpW4AmuXoUp7J6RTXHmukrVk6hnngKkNgeewu-lpd6VfePHWSw9N5bXUAFjoUbgWlnxPYUXUbSfu4wUrZazOQE90WPKiNrTSLfhhH3_xEkpIgr2Iv1R3W_ebLJrQFTu66RTdQFe57vnKUabViBh3I21uQNxRTI69mrG172Il42iv7ao6zbUSfs_x65gRtw42OF6gosIIGW9A7pSykimya3Id7clyfBs_Sp0l0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bww3DZt4XVFQ2oX2PcdNxdnIpBL4goRlqpKUoiswcd7WK-1Q0DBibuWHujjkCF8fyK5bM5Wc8DsmKn2ghq3tUSC_MRZNjIa1AOFJd7SrJEzjEKVApMI2AHzEYM-Xot7RATqAky5L2EM2zrL768fdf9fSqINUd2VAH_taL-tzMmShagsRmcoV-v1D_TuuFkQci85kdXpN53rC1ija_WWX0mw3wTe-knCFr6f55K9HdF7sFyGtw_1rrgKTsHyk92QeH41qsZoPC2Mw8i7XyD_8Q1nnOt6UNUU3-v1DvKftCNQBy2fW--_-DKih5P7c4gT_We_bpmwGMpadXAPNo0f5kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
