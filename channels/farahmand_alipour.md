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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 11:50:17</div>
<hr>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMg5GeC7LmHvPMKHD7YxCLaDcNo7b9thX-MU_nKpp7eay8jBzZRHQAOmyrfhp243_OP4rR8Pf_iqBNclKnTpRdvO3rjGEeQryrr1mtMTSZko1e0hS3K1N13eP8aTzoHQfVKGO2Jj2z_gI9iu-94vrrjjzcoFuDzZafzk4md9sg39Eg2Je8FB8AtpNDLkCDNBYg-lL0V_o2-DaBbk9zGOvOUL9EVLFwV_PipXzQVqJXvUE8WKh7agdIyD8O0cERZbVL5QqFJxfHlUyaaBqc-43dDlXgfrRkUjNz-_sWRhNR_XOc1WSLVgmJVLWTbsLEPVG0-i20dXsDsNXb02HXns9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0ry2yDNiPv0HK9VjVN16-9ch7habE0-j_qGGUXnSLuHsYDmgMFO-ImenA1Opj95gi0Lwt3xZVVYn54C04ZKDS8kF_dRfK00_h3NqfHasVFMSkvhZxi6yrVg9TMo1QJHw7CU5VXifyZdE4TquW6sohmO37D5wkxjBMsaoiormYWTnH73LrXcCWhEuR4FtvO3ndLMYazUlk6bENimBQ13JC05ZJwtKn3ZH0vCgW0Iw615-4JsU4M09JWQUmS8oTXhm9h8wE9C5P2VfAn3GjAvaLMz0jdEfSTsY74jDKDrF9N8e6ixvoDr2jRHCp1xrrNGnyAT1qsHmWgnmLLQ5ibdYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlnVzBIQgXIkYtcbZ6qUtWk7_iokG2H_rnHmojnaVsAwEo6gUeDF0_gvMngFePIncZXk61TbmAMx_UZoRs6mkD1IsuZ7UW06b2QwLalz8mPXMKzw7uJxclRIH44X2iPpORCygyMC7vupJnkmFsns8ILDAH-0vzgxW_aN-2dqgFdQH5zX48ouBCLMSHrSoGfll_0ERKeGX__QpFqqaOOkxy6krjX3_Wo1cOOX1J7nWbuyHPwRXFqzc95Lh6j2KioRLYCLbSkvHH4OQJ3OqrnG3oY0Rvfc5kIrq_RpJz6x0T63l84B5BLPrAdxYuSEpPm4tdwNd0TGvsuIv5WnBEUfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hlKyrFAYSZTRMdoOHh4Dkf3wtTjgKKpLwPURpKIYNMC0JPEGwH4afqDOa1sevFYTVB7VTqgZ1E9cjleG7wTAFaRPEvKkmSp6vMvaLKsreRznwuckG1t9OeMo4Yp4vxnoZ6KP08GH1AHSqqIlti0J7yxH1porPc-6CVyFLce5es4tUoO-_sAmFLeidFxWl3h13eTLWLM4H6rFPT3NMWDdEYe6WIC84eWrTtWTCgiR7syjwmzlqmKthbOZiWYToc-KBGVsg9YKlWHZMVSUB32aKRz9jWt2sntQ-7p2CHAU4wLHUyTf0vOjpLXBOPsOQJjq8KIHJwOqnyoscwqGuupklA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hlKyrFAYSZTRMdoOHh4Dkf3wtTjgKKpLwPURpKIYNMC0JPEGwH4afqDOa1sevFYTVB7VTqgZ1E9cjleG7wTAFaRPEvKkmSp6vMvaLKsreRznwuckG1t9OeMo4Yp4vxnoZ6KP08GH1AHSqqIlti0J7yxH1porPc-6CVyFLce5es4tUoO-_sAmFLeidFxWl3h13eTLWLM4H6rFPT3NMWDdEYe6WIC84eWrTtWTCgiR7syjwmzlqmKthbOZiWYToc-KBGVsg9YKlWHZMVSUB32aKRz9jWt2sntQ-7p2CHAU4wLHUyTf0vOjpLXBOPsOQJjq8KIHJwOqnyoscwqGuupklA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=IxRJGqLc_vQw6e7S-LPtjkqaLcmbpNSWVsXEfbZfjVOEQ-VB90EhkfUzOl1dwGG6dyLYJ55465VeaoiJ_KZgvGCn-Str1Y8JZzFhNUVfOwRBSiTl9qBpzau-RMqBwbqowxu9Ey8WY2kGUT0MGuMWgFo6HJTQ2Y2dvZ6iFe7VeShkfPXGlaGvBkuC31hDH9HFIdQUSKuNXZGVM2LmMxihnCI49S_pBt0OlCT_1ze2SybmE5-UokWeid4oepcta-591R0GnKqBPm2cRmaa2anYiT2JrrtoCUyAcTqy_NEDmqJAVuaIR0lqdiBevP6W6ku56Eh2RoF3b6ZDJnOnOWuuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=IxRJGqLc_vQw6e7S-LPtjkqaLcmbpNSWVsXEfbZfjVOEQ-VB90EhkfUzOl1dwGG6dyLYJ55465VeaoiJ_KZgvGCn-Str1Y8JZzFhNUVfOwRBSiTl9qBpzau-RMqBwbqowxu9Ey8WY2kGUT0MGuMWgFo6HJTQ2Y2dvZ6iFe7VeShkfPXGlaGvBkuC31hDH9HFIdQUSKuNXZGVM2LmMxihnCI49S_pBt0OlCT_1ze2SybmE5-UokWeid4oepcta-591R0GnKqBPm2cRmaa2anYiT2JrrtoCUyAcTqy_NEDmqJAVuaIR0lqdiBevP6W6ku56Eh2RoF3b6ZDJnOnOWuuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooXPqvI1q8taXawnq1FN12dPEqhZLLLOH9FdAjS2xz6YfW1_72kw3Bmovod5L7KuwOrYv1pcK-jlY1NWC6-5KEhcwsvf5RJG9Llsk3Trkpg5z9X_u1uaEBmhFUcfo_qKjSNff4TwDiE_ljzgxlz1EAI2IB38wkBmIm8R3QFqsvhwCf58Wft2k9g8hXTXSqTymsQvwO3z0eOk6-i8axkcMcG0nadoNFF4SAfxi3nY9LvBpSxtZzdZ5aHVNwoIEkaKs2e7L9uWwtD9jgqg185fQcBi64msUvdXLwtuJgxSHg_M92R9OO9gF_ibn2wkLqZ6giqoGLgUvjS8-wPYgkvcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKnhIUVuqDA_mDbCGoyrTig3YFn4A600EBLWLTvHywe9kqq-qUoXkqh_CC9HE85IO9mEcbSi1tHqKDSBHlJJfCPQcBxSEJHq_1M-L_xRJSKadnINslztPNh_QgGTkvgAlY9xyTvejMQRP7lkOcbby2sHoWrbg7bgP1_OJrh1Q4dKg4RyZMrn6MqRGuNRmKCerPkYn7606tmoqfnwCSmPpwAF2og9GShE0fYFQgBBgXDcKQGH7S7VSzy9jITVlAchZX9guusSCXcr5D6eEyOVMxqm07Bc3hXlKdozQ3nc62f8hpNxNQNg6l95Pv4M5BbljfMXjYpD4VHl2fFMoX1Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oodGfRKQNkBVN6rsaK-VbU_80tFAq4Z5JvkcSB3Keu5Y44fA_Rr7OWpzf2BAKC4ZHkfPFIkVOXOPIDa0ak1TIp-yd-DXL3ORQZ03kMCQ1E20wC0W5YuBzvT5YvdjHJAta-QuLf0ZT_nkW7ptbQpQQ0w8epTJVLjcILNjsosszsI95UfWCJadqjoi-aNUJzqoiv4yaOqlSs9UfXnxgpkVgNB9Rr-xoVoveB5kAP9WbTvgB4N3uRdpCwjct-f10P0tyKbVgiCcB9nhnIzDXk5oNE2XSo6DnpYQ4SeEqB_9Q9dBgpgnGtMObSknq7Dkxqm999KbiTZapIFG0Vc5pMUfGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdPa3MYP4wtU9wDjBgBCG714D6ym3ww9M_ywcD3-6SRs3piqFhO0YG4yd8eq-VDGDbG5C1HI78In9GHhw2Dc_K7zK4gUQCwah3AWlG36Kt3LJpHbb5QrW_1T6gIrOhKcAjPdqhJ8ovNr7PTuNzwh4eSamlXupzOupLnL5C7__2IiiKq-Fuw3sB02yoP2DB2RWD12CT9Cm4YZWttPAOqHajkSLe8yR3gCcid2hj4H3_ajOa1eTRUP0iuu_lVBZKa9YjES80Yuie1C8u501HvDIWRjePNHLJhYcX41RROeGAISvuojpXqqN8xR8Jt8NnxDmWf1kGbJiUyNCIRP7eYgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIrtpI6oK-4S4_w1uxfYhQVYKtKEmYokvJ7l40h36GLtVCyihehmK_85As-b3miV4vhm0r0JkdZKDBtL14NrR5ilaWdlD6XD9qxA_8d7bAQiD0X_8A0WoDBNxRlI_WRNEODOHzBTpDBcz5uVC9XnU2ACrD0gT0CIuhV6YB3iCn2N1S0Ekx9djmgRT4r-v3qosTtoa-3D9XCdv8K3qx1QF7gT9_DouGujKGWNcz8-h244cNKow5iJ38n7dfmhJFBKHEqReiFye_u9pjiMoaALt9jgN4_-vV8O5Nx8nE1bwV9WJ47k3uXEhBRJ1xDTX_efpgUYFUdqeLrMF3eb2c2MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rAfli-hWZQs_zVbObHMLcYgnYHYgpv_ZQllvTj6hx57s6ec87ioPv-oBQfbAoGfAmbqHOiVW2_EpPzPTyXGosu3oJwmK7yJyFTKO2kdcX4jj0dJgdAu9nEeWfJ-T1olf04Bl9ilshbrvfGqBJilbLuy-B57OHn-Id7bDS06ueyWHzvga1xJFqCHovvBYt36FGBkLjtD8r3k4b1CFqUIU6TCnDzAUzSNDXufqfiaA8Sc5qRXyiRg0B0SPRUCBNGTltwJgl_ZZqOV6j_CK3VvsIjOqY8Cj5T2Fe5CIj1YLRejF2PKkkOyp0R-FI_xDmGHpahi5x2eo10XhPqNyydReRRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rAfli-hWZQs_zVbObHMLcYgnYHYgpv_ZQllvTj6hx57s6ec87ioPv-oBQfbAoGfAmbqHOiVW2_EpPzPTyXGosu3oJwmK7yJyFTKO2kdcX4jj0dJgdAu9nEeWfJ-T1olf04Bl9ilshbrvfGqBJilbLuy-B57OHn-Id7bDS06ueyWHzvga1xJFqCHovvBYt36FGBkLjtD8r3k4b1CFqUIU6TCnDzAUzSNDXufqfiaA8Sc5qRXyiRg0B0SPRUCBNGTltwJgl_ZZqOV6j_CK3VvsIjOqY8Cj5T2Fe5CIj1YLRejF2PKkkOyp0R-FI_xDmGHpahi5x2eo10XhPqNyydReRRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=fhrfRKXs-MXzA3re5hX0Ot69Pef09lPUZBRICNEbLTVSR7fowXdoghlX5b1SLMVUiIFcj9f6asKJAUnuqGQhmj1o7IyX7xOcBx7k2YUIxAS18q5s0nOZLPQEwtHbNjJMariJZhD7g0ihZgmqrUFBXJRe9z0KkYbKi923BaAcvsKmsHuBGMGDnAO1YkOpN6xeYAA25KavYzfXPrP94IpiiX8Y7pow0IgcXhtzc59G9qxjJZPm5rqIMMeVnygjzWWxAP0j6dlFQTbCAjivB5agn4QAR160IiQquKHU5i3jWvZRAAHu-jCozk1ZIJEdGCcVAaQsSMufulV-SQQZvCytu1EPQtZZA6wia2OV9dlHEyH-yuo6nDrwRr5-Pa8IlAoDXZwFxYDw7yL4ZRy93QT028fZFlODd8LfJCbc92v2_t04lHs2HICl2HH7-J494z6GycZ9TANPBB9LY0jX-t9DkpoXT3_ltcQ-wXpTpJvO4iRsU1gupSwAraVQLs8hyrPXgplyFl4etll9cVqKsjvUV6bssD2OCXA2xGX03bqLGpiyGLahDJH5Xo49JRndsJDXNrfLd1qsnxNBgZ-i3rUqx1D-nATzbELcguQnhVTy6ykNZqEcyo9L4oNE8FiXUjG3weNJmGTo19_Kobodoi8w_TJJJgxRBjsCe4qHcw1Ba6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=fhrfRKXs-MXzA3re5hX0Ot69Pef09lPUZBRICNEbLTVSR7fowXdoghlX5b1SLMVUiIFcj9f6asKJAUnuqGQhmj1o7IyX7xOcBx7k2YUIxAS18q5s0nOZLPQEwtHbNjJMariJZhD7g0ihZgmqrUFBXJRe9z0KkYbKi923BaAcvsKmsHuBGMGDnAO1YkOpN6xeYAA25KavYzfXPrP94IpiiX8Y7pow0IgcXhtzc59G9qxjJZPm5rqIMMeVnygjzWWxAP0j6dlFQTbCAjivB5agn4QAR160IiQquKHU5i3jWvZRAAHu-jCozk1ZIJEdGCcVAaQsSMufulV-SQQZvCytu1EPQtZZA6wia2OV9dlHEyH-yuo6nDrwRr5-Pa8IlAoDXZwFxYDw7yL4ZRy93QT028fZFlODd8LfJCbc92v2_t04lHs2HICl2HH7-J494z6GycZ9TANPBB9LY0jX-t9DkpoXT3_ltcQ-wXpTpJvO4iRsU1gupSwAraVQLs8hyrPXgplyFl4etll9cVqKsjvUV6bssD2OCXA2xGX03bqLGpiyGLahDJH5Xo49JRndsJDXNrfLd1qsnxNBgZ-i3rUqx1D-nATzbELcguQnhVTy6ykNZqEcyo9L4oNE8FiXUjG3weNJmGTo19_Kobodoi8w_TJJJgxRBjsCe4qHcw1Ba6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B50VYs8v7DnIcQ5zs9j_VrDK7j8IYbCXhnV-ag6bL_iCHIAER-tPadgrnRQVQfldKpHGwxbJmLXIKFXlHF4lLq9b2QfJlPkrilIghR9TiSCGc7IxgmGfNCr_ZtImJHNyBGjeATcVdxism5RcZR93uSgeGSUUXDdQyNojm3UmcrFh2dzT2RkJadlgfHSa1PxR5N7sRq0S9S7fJDK_PN1T526q-UQMzGdR9CsYnCd5ACIWNsoZL2ENNmltuI6Oqloxl8xOfo6aB_g0x8b_mNkY9boIvL4Ad1dERyEMQAMr05rwMgTcE9EIn30nfCnnIQr-l9MP-YrE5rsuD1Z9_VhV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQZUVTatSlPfoOwRYK3rhOvoPr6zwlWrQbE4_E1MQSwlyXTIUsgafgOsTQcCyf2HB98Cod4MmO626R7EXp2AFk2s5CN8hkn_XtuRp6THE9uodtzQqUum9kwwumUP8mwO0p6uMKCrpHMyiJ7BMa4SA3xzxd2dzGIsu-wZQavGY-W61AjN5_hEMEJ9CrP2JRsN3_MsViP33fcBcgo0BPTPYg2lMMJ5bYz-BZWi1PooMO6Bcd9mzyQJThJMpQdKeOwuzCWJyeFgiTSLJMtbaaqy43WKK-Yu7OqqAE2fM04ummDVTnV59PQxLC2LutGlEso9ABAtzGeuAthgQGp10wTH3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyRCS2CFhlGiF0S4kV-3hTmI9LmmUrxnzeEc9yN2sMjiKU1MSix0YlMC9V3PpJ2Ml_fsCLrygjHpcnpVp-qMLKbzc2syV6LkhHLarPEHuLXOHA_8OIK5iiRi4OBjgm1cx7JUFDVDeo2Zwfw5umED7tWOTXtDpTLSX30g_Ug1-BJSocIEYOAzsfH8Kr3AFRjNl-nXjclmpkwfz9PmJQT4Z_lCRmO0I9bTEXnlq2VrEvjdWY_IXPZ9gGdoIeAafVHuivkrKalkMcDce0_j7dRq87B-228SElCuioerKuTJFTDf_lpoKjUgeJZMljhqObbTuO9txVJkFADarWP2jHHQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3gijX2EHPOLcNAb48Z07FqKZd-JEIzxmHEnBXQEzOxtAe19xEVpzW9tlfxaZSD_iqh6It3EWDxPrr5aSHyDRUisjIZp3Q2I6wc39NhxMkbh31RToCDup3_iSrN2Iek2-FkrhYKdtDETo-lfSke3FvJjcpM8OO--A9dSXHrt5LRp21Y_HGNHeG2WGQO50_7vXGFiOUrm6b1ngEjEE_FvK730S5-wsgbXpiNECcDwbA9eUluD3ovzP_rfjncg_IEswft5Cx5sN-ZQL88bFiP8O94VbrtFGy7Hu2VsvqepO9yr0VwPOYX6i6bqaTcxgat9_HrlwV8ZemAiQ4Dc5B5o-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_aWMaITcdUlpVzRctFV4mnJ_zpnc-zd9B9fzIaJ5W53-jWQWxMdDOHRQMraNYwSecSPXEmP3wQxSo0ookhfVxHIOTrJHrzLFMeBloAd_hgZom8lisZY_gZzckaYzxBa7jnAVSThph3HzwK43DcttMLKZGYkx04dEql2Z3oQXXUpe_qjol3mCd4rbvgvREuIgPbgTn8Uzki8OSa6O4SSJxJdb_ZniWUaB7gqZIuZfbElLJdHVNV8U8SnzinwH_3d4_Gf6zD-PrteM8hdsDSU_9aEJq6tNpymtqS8--I45pWWRNpI55emk7S2FtDUyh9mnTiMAvdUaUPBWBzRwKhhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOKYUwcjXlb5bTZgjYAv0vtjlZt_k0yakpJ2ESKOFy887FYaxJl7kDWbtwlgl12P7xMSKLdDcBEcKoTttiHhgiE0sain2wG__8Zik9MzRvH0RGcdL4wtVanRTWeACVYS9-wRwBV8rES4BTiTmDRo70uVPg-RbGO-AR6kXqHKq7nz7VNeIQilFPOrt7kdcbDilClf7s_ZebqipFXMik41W4cT8y26etCjQNR4YKvMsTfkX0MdMsXmMyh6LKZ3O6YtYux7x5ZvzNWnJoIfmk1pQ0FDYzwzBoxfuMMjAp_B1oK5GiCAKAKKioWW9gKoYh86A3Bc5dJRJYbwvmoa63N5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbVu9fCkbOER5BU-pW0NVQWQilB13YJB8MEPpFIPb0miukMdQWOwISdQ0qhLqwpwjgUh6HAZPY8mTfBFUA8SPXuLyb4ZKdap3GbUTP0Y_F6ghSLHq6Bs2yqtewiNv_v2P0tQWpmchws9u17DMKTxTEKlwbETmJwW8e6-lJiWsBOG2h0N5tUV84cZa70zNVu1BjcLCKD5v1HkkKKW5xqkKLB1-zM54yw1ik9oi8AuebueH7UCjzCi2uF2SiNEEtcLtnpKs9sMDwzZ0JcGtoEEoXrgcYRsDqSRXcUM7GZjnBSRT8m3xKM1GqdmI_w-ngDLQTMVlELaK2TF_Nl6H1by0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN1LKNiprNgQLYjXlmhZPj5Eqzc9jtsjoDc3NZhCfrOc1FCGYY4Xgq_yU9jK1UE41ojofElyF4XMMkZk-yGA4yNFu4Ezw23b5hHtS08GkLEfjAljhpgHKGFpthM7d8OLWE4tEitQGqZ9L9cHEpS-1AJTj-bj4PmyJK9NucBRF5dDsX6_60wqYn84oM4C1umwySvW-hPZ6ae1OsQdW-eEnvALNBpoHP-51EFy7Z2is7P9zAA-a_QsFMp__41sY-e2V89q_IGz04xI82cFObx9f76owYP8Fijp1zPr0nftSNCaFO8yTIVLtk7UxQgE85jHmOuJqj5RTr4bIOEY_7AL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHQHs5moHni3Umqd-GYdV0ZNzzFTQvd-ZoIeormro2h-DU4DRanBdl9w3avFhMN5UKYoGLmWu0M4kqEIID3qkdPFoipBaBiiaFW5OXhsSi_oARzPDrFJSyvc3J_dSa9bAElZXM09hh5xQGcketpXqb7i4IpwoGnirICDUVWkS8MReI7-ZNFf0HC92Q3nBJFOWqpytAGw3sz2__a0oQW3Fik9-Qg5ONZER7bOKVsozXFvN5XqMABSFfNLGGA_sOE2GgtKKsrE3B88XTNEHA0YLfboafvfoUkTu5PWblLFatCZfJf-kF67NWtxTg__f_zWC5ZUzR98ut3P9nPfBoghpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=rfiKAwX23qUmAvqrCLW8wsmOFswXqs5_3CAktfY75ufm96xa80YySJXHfIi7oV3s5Zj0n369F45CacjZ4fE3ZfHyqKmkWZq3R1j0MqXXHs8fNbSen8_vR3G-eXwiv2X_K5SH5MurXQN5vdW7BOoEjly0TdzK0mLmsP_PJpFa3_HELcLH1OOi2dU3D-JKyZiTcxmEZNWrLoBnaFNYSmEkO_YFFQeaTocHT8n7z6RWLf2b36XTymOS1W82kOcKULPA4o8kf9_DmcJHXM-xpADDkLuvfUYPuyLeEnlkz_U5CiFoVj8pwyPDFuNSySEAR1Mofy2uGFKKNWCRYHm0Jpt1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=rfiKAwX23qUmAvqrCLW8wsmOFswXqs5_3CAktfY75ufm96xa80YySJXHfIi7oV3s5Zj0n369F45CacjZ4fE3ZfHyqKmkWZq3R1j0MqXXHs8fNbSen8_vR3G-eXwiv2X_K5SH5MurXQN5vdW7BOoEjly0TdzK0mLmsP_PJpFa3_HELcLH1OOi2dU3D-JKyZiTcxmEZNWrLoBnaFNYSmEkO_YFFQeaTocHT8n7z6RWLf2b36XTymOS1W82kOcKULPA4o8kf9_DmcJHXM-xpADDkLuvfUYPuyLeEnlkz_U5CiFoVj8pwyPDFuNSySEAR1Mofy2uGFKKNWCRYHm0Jpt1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I3-VT43WVupV3a9St6TmX8bS0obf-FLvIQtZVDThz6nCl8v2ICW63YVMaGHAVT_KgK9FZWF8nTZK-v0Anzc1ETPc_trNlVOiohkuXmlz5nlNhih5kZeTGFJRVFiwLKGNQgshF5t8iwKCOqxzjcFUZC6lU7Xx6OMRIQkeDyZMjL3rKiVnRVc_FTlF5N5zwHyzkivMH4ki6GizJjj0FmhPDtAS9yNK6VB1ftb7_l6Km-XPtHh43byyZY8K5CnOHQstRe31KdjMl2R3DAdlv30yTr26zJ6bPjq5djX55-ntntbSjwjnemrTzDG1ZaoKFBRwV337hFISGbkC3zp3jft8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0ucN0w5TzClSsN8h_l3nQir1Yw16ct7EKUFb84cuiZxm9Qb_v4F_gOHUxD069mqWy3-55HckgCCDXW28tr0l3APObXIUgAEU1iu4LU8TIs8dpyHGvlTcam70IVrTVmi8PBItq74l9TdzFImk8w1AannG-ivndKM9kZI-xaU9pyPItwvpkLw0v4jRI8xMji3TtWLJOcP32a0gF-TslaQKZMJ98K5TFWihC276goYznNqSAtB8njmvPSZTOQEjviO6h1cF7kCLfycN0xW678P-bDZHiaa1GAwQV46AvRVaRABLFcWNfU5votfuQHxTcFRf0qjAgvY_GjA_ZEf3rnQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFT6TCpZ2GfHyEFuKsPFDIfFkeL7pCBywySUW1HEpXMZz8s1frWhySxGSu9_tPF9RRN3v0aGZjppAMkNkg5L8l1K5yN69440uTZEttO0ev7u0BqDZrcRzL_bPqRNYc7IzvMDK5PUJf2kqJRnlKJV-g3n1YJCDhHFO9D9szytf7JW6ynFNHH1IvCBvhEwyy3rItb2KIrpch1qM41r11HlFgBwaHrGO63x_dkvXvaQCuEMwX2UP87sY5xTvqYYla6GSc9TkTFPGY3ggUjFRA11XGUuAvKN8v7V0A08aj_aUrih5AHDpPG0wkuIEBgEYJLcTJKTkbZETDwgu_q2ShBGhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAq9Z-WyvtBvp2OoJ3MbK-XrNPx5slIGTdb_pyMna6SUqdJLa67HacfuGidi95DptIs9OIQbvO79WgDw0deS3sCrUiT8x2U22ftT-IhWajJJ7Q8EdVkBz8b8Jdr8DuaZOQghQjXs5IWQcq-vetLwBYrwBBkcM8cDOFU9QyRi7NGOziWRxHDuJ0aW1GOQxBjaC3WYxqUyEzHPWw2kR9jRSIQn21SGi9w8PDoU5WB5D8WlXb5E7Mh2_WrWHR5CT90MhfLH5T3H7duBE9ObrXd_cmZmS3swCSrmUrr4yQVA7osqxaOynKFjtDNwwUtBzqtyHrR9qB7G22AoFJ73srGniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tti016lMbBqf79N-Rbufgi3IHafrMHyUfuzruLTJdWognQ5vfg_1QbyeuL9e_Gz-tywYOvWs5kMHtg1ikg6BbhKIQ5phcapa9cuEcNeBknH-kkWnctysMNrB7qXO2s965uy2frFXy-JWOvPalA6nVkRBMTQuaAI19f9eZBUCb_kRUdp1Ya664rwzf5ZK5hUIVRB1mKiWtq5Zj6qoPL3UybT837fq-4xQuxft8ZDcGt7DVdDgX3YrRERbmvL0tLdFuaZnOnyTCl8SHgx2YINXg1wd-WhOoSwsa6TdXGuVMxIkv_y3emyla5hhVsCBGhSAUJdV4HWrGKdwaijLS_AMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOPyDWv0pc7uoi27ADM1aN5T-hfeLIh-PWCpnGLUWpKJMKT7aQJmhTXKpmWzJFvQ8LRjgKpoVE0Lu2qsy2voGf15vfgCs5yCjEA5_8q-KZSymTvRa0DAtjIVBQ77HTK4ey-Kepp4K1G0UeRt18aulWCP5T9856zV7636trb_0BKFOxOogg1jOra4YAzbPoULSjubLiuU7xKj_4VUUIp0ozyo5t5pAZdqC1CZn91nD8cb4qa8VQWCo_YIUumq5X9l1lwX8rq2_uLo1jQ9Kx7VfoBeVitaK_7ttCNcnQI6PZ5lR72FvGwiDqwDo3YovlzuZs5yX8WEsQ9xJuQes_BLuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzacjNjPoY9uspXGKHXuqPMynuGdr7SHggxyY07a9TgXKSibQgtXMSKZnJfY6n0Cf35YC9HFU3292pEXEx8DF7wkvJ_uIuZJG2bozQZdhwzQYgrCSVQhgHyu2YhVnyUOUQTDV0y7FuXWpXSjCeSVMVq0bQ6PiEHgJXk9uhpDcvIOkIMWjHt9ZlQi5ECAmvgxjCZJH4R12-of3AGd6eCCx_AtngmDAYSRJX12AnSFsOxv7RVX6pO6w9IgdG2Zrsjd9QSBi0WrN9ydJRUyLOxp6xoIQPnfiknnLFso39O4npOU4lCNSJ34ESaxq3liaYPcbLWJ72tDeB52ErfEJv3D-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ37-h3piwwlsTtXKDwDLsVpbQaJ7F6_V1YNt99D_a2C80FNMDmOadcnHjgIjlnCHx4LSGHugOMAmCub22w0OD8KXryqK3u4tVYlB-v1ynzjq9I9McrkCBHgbCVPnvnXuJZgsS8LO9KhPRR8aEoiN0QbxQvx0Jp-JSKD7Dn2FVO4V0tfHlcx__l0rsr9XndzKJRdSQN9mErqfeZ-yMLSOQWpfz_u9nrO6xXLzPbGaMQSLpA4PfgpJr-mvquDWeHqVw_vvq_UAHNJFme91mhGVEedCf0yPK64ma0WRaMQhT37N3iXF4OqF8M1eAeMu9DePgAdOVj_V8jPGgt81hNNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=qx_GwERBbT0ItBBMUJkIl42KVvEVK1FlJowSaoVV-CicAeNZSLgxVy2_UP8rs7wlHdo8npdwZ1vUH_hRFB6Nf5kNNYHYiuLtK5pyzyupaNPT6yUsa_jHaCaJ3gjdYRCSP2lY_nG8RQUXivaA-u4tEmtKjfWT_9l_v2W152P6JTiPNtBLdHtoWSz4i4JiE8zSPp9cL5PysNmGo9pXTyIGxc7--SQ4X5Ep3D5uTNJiPCN7aYlhhHcMg48IAvBOI6nFTfgGsbwYqL7OEx0WvAOpxt8vVXk6bAPmnAn-KPxACcNlkRdAV4Cvj4N5On0eU2NG2r2tO8movXYbYr6uVdCm3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=qx_GwERBbT0ItBBMUJkIl42KVvEVK1FlJowSaoVV-CicAeNZSLgxVy2_UP8rs7wlHdo8npdwZ1vUH_hRFB6Nf5kNNYHYiuLtK5pyzyupaNPT6yUsa_jHaCaJ3gjdYRCSP2lY_nG8RQUXivaA-u4tEmtKjfWT_9l_v2W152P6JTiPNtBLdHtoWSz4i4JiE8zSPp9cL5PysNmGo9pXTyIGxc7--SQ4X5Ep3D5uTNJiPCN7aYlhhHcMg48IAvBOI6nFTfgGsbwYqL7OEx0WvAOpxt8vVXk6bAPmnAn-KPxACcNlkRdAV4Cvj4N5On0eU2NG2r2tO8movXYbYr6uVdCm3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8YvQm_zt4HOdt915EaD_AEFfg9fTsdCC-D0lZlPZN3j7JtV8tydWws0Je3P_r7DVmhbsh82dJtl3gdABNTHX6eCoEEHVR1ygStoD-n298bYNPJJJOwhzuw9ZwUa8OUAIgVnc6CQLyR-x1JpyxDoR80p05ryQ8j10JwKAxe13_Rsrr1p1KRp7ZPbhpO1lpkRipCPnIIFX02pL0DKENo0rtscbFWxH89Is-Y50c3JLozY1iDmouWJCMpr3sbS1TEAQtH4aXn6Rq_82LSwTbhnLsrSBBLOH-jEIqOYFsif0P8iVdq5WoBmCVNW0j7CsQptmnPW28cyD_6qOnmzWEK2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYFdtCOH5JDnuBFPSiYj9ABKJxKuRM2TtAo6216XWm6rXkBkZb7NcjmKRiumrZK2PEgIYTMS9ERoCBSkX_hKa2G-P5OqLcz-OldTHdkW5FvLzm_JmggfRJOMCEyMNv5LwAtSTe-6AcS0y8QRmlH3TBKvpJlQ5uaURhj1TLrHJ99TCecqYvLWORQtwcJbihm2A2NHbIAxFnClp1tfQt32E4-fXLH47BGUJ6L8Wqzrcg1aDsDWRGvB09n0bcRktfy9GM_NoprFQPXbdYI_O0PfXd1OraT3nvoJRjl8xLO4chtMGvfhkOdhVJWIGZjnTlHXIOIY5UsSz4_55RK9PnT9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myevUaIlmPjMefI0Q1_QucsLPjO0nP6K-e5iinxMGGKBGsTwjW2RN1HIu_K-stvOCi06N3k24IYsNZ4TMbfP-tfsjzXY9SQYCq16uVy2bNTWoWxvDOOeNloVjfN3yoE8rEg8dkbd0yPXYPp3mFRiBIBmlZhwvPvZSQSul8NPx9cogbrJxr4G85fEi7nBou_zYrrP-Epd2YIMKCH2CIzhFEWnFAINnT3Jwo8MvdCSnQFT5aFoDdVr_KtWQ7NR_YiISqIaX6Ft01QTvx0cLvkv9nTUKSv1U1VOEqg4lYTPuGTyvGRPI6t1nYT6hmzccwy4ADJSKGtBj2g_ZhnyNwbXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfzFPy2ic-zTo1ZXLn7pcz2D3oPNtMZYt_4k6eu6IgjZR4W420bOs0gvOTGebEYVOb3ntGUiCBdhN_8XiuuDwuz_FTsCoGMoF2xMD213ZLYfJ-FfFU7I2ksAnufG_keLrzfRqd1gW3L9bgz-b_YCHZzud4mBBV1DWJ1xm4YWAiV0nf_RcPnbeQ0EaXrE9FBB0J3mnLGhbsaWSeaXg7xG2_M9_LwCC1MLI4FlA1gLUKSW6lh7AbQo9bpZ43caoL7aN5_2pv_btKuJASbmFwHpHRgreM74J7m8QPHv2p6HzKuhwd1jQPfl0aKzq3yGhbOqNwVYiwzHM1qd6SyRfCrQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROM4c7Kc_J0dz4HQbtHTxV9n72QoaSjT_91I5rc7ztWQsPGEgiQzlj-yLmg8NtawLFsula2GoMpDcjZScQsVYE_ZmcUDAGhDpyBSkSUvnucUInGlPBW8VducyRzlyA5HWs_iA9--FQxVjijSPHSyIN5TMJbNU_9kCAF2yHcVVfclxXwcLC6lXtEkyikDwnlC8csDRDC3hs5BfBBXbAN36oIxBBC3kPPriduECFw36nCAt74O5IFD7b_NjLo09SVzTDtG0jX5waM6HkcdYG8v0dgRHa5tE952djK13cBYvLgJ4cJjVOKifayfimdlB8Zbhjaohd-l_gN1ufILBEAGWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyP5sNrQYIvl-wP6YCVDPL1qn56rlmuuPAZNOyFpPxx9rDDX9bUq5qHRu0tpwU1wsVj-eENEXMZ3N9KXYngZuzbP0e7M_-_AjYgCsuAh3tANxxvNlDDuNHjqjq2T8DuXGDO9veFLhRlVQXCzXJPTJlaNq9DV5ud3esighF7pE7MSYijmQKZ_zxBJjsfl1tuP3JSJ5cpG9cP-TrFZebk3OL_T2QMDoKEwTeO6BBRQBvT_8ZcFINcuX20DJB2K_cFBEPQob5OK_z-emfC9bdgEyX7R4N_ZSDe1aehj3abZjH6afnXEpLHdWJjqvS3dE2B4N05r-kiQWLcf2iH2MsoNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZQVGvd9dQXCr573_c9MN6PUDHpLgCcW5cSp70WUMfIwPJpvqAyUAtYxqRRmbY0WChGwM_H9ECwZRdq9FThTEpbk11GlVzWGTSKKIMUfa-HqSv6fur5bgCh8WtWnAWs3IzYq8MRaYSBh_BvnxGUxxoyffv9rUIUUenDTwSHLfX4t7Px5D-PxXr6XJ-xapJMTPh4OGJ91SigFdUtw1Ga9-TPTkh3PJfB5EZmSYsyJuUxv729g7QGodc_WQ1Ce1P5ZoRB6jgvMtKUzZDw3SbpR2_8-zn4xUb3K6MpeXqZRED3YgAUHlBNBYGsyKYiJH0oswC40oAOKKXKFzXzlBqN2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF4MB43DSSw8L_raiAc5lilkkjTaPolla450WXfc4tl323Etd-2XdvO7LO3IttmhfHOQTYpqnwTHT_K5Ped7x9ZKdT6NvRIL8HRJH_kMfjhTT2UYCIbLfoqjQRe4REHDtzUKgYfNjsEqdr5--bin3Yx5s6K-JQ34vwV24C_2tLIrULmiJvV7yv1UkxSRJHY2xVJhUGdtnTp5vA6OecA59lLMRfkHYkyEww7cFRCYoartMYYXRnaln8gqUGKgxQiad9nxbIFSJTum7So7KVQWi5USLzS6_3-lxxCUyyfLKB_t1m4sEu8E0TlAc5cCVO6JIHfLl5Wt4lbYmQ8nVXIxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnQz3cG3gnItkiMhXi3Galpw2HKn1mzNtEg3feGw8Ls4M4F84G3kLkQtVpmF8z-mzy23WanDaS9Js5gF7QvnshrcWfxHAFR5tWO7ys04HhJz4Tn9YFQPLVjVsj9BySvapzeKJYoI81yczX5r8TGmIwCnXwyTz0sV6QRrFoK6Mg2amt-SW2QRzZUiccubWcuUP6-Ed0ado4k-xInYH9tvpAXOqBMaiea7LwMt5_kk62aQ6r6JvoSQof0oHO42Ix708crnge0-rd1oJChwr1q7t4VPWphbQSReSYcAoxJr16DXC0RlAL5udB8iLyiEvBX1oHbRu1ImNnGlZ2hsDo1HJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=q78-hQ1oZOrCkK9yDY8gTmvNhMq7Vq6GJVC0Aapz02_xOjUy24FhOK6T7TxsL-nQ1hv9rcAgmsnwZ4uBe8jaNUf91wq8GbTEd1CwbxrB30jTaxbc2VdPkTKzLtDpeVC517w6AaBbK87RMaHAoq-g89BadRfMGF61-ZMahcBshKcvdkCSfV9BndlI12QiqxB3smmvxlJPmVEgBkV_wfsLwe-FRq_hh5a6570yE3t4MN3_C5Ky7fLF1xQf-wcLtrCgUaOydureC78M_CnGRIEtui6arexc_488BuHzfwhKOpj_IQbongd0jYxnd9JXfBbCrtjoefwxZM2JlWmFT06nUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=q78-hQ1oZOrCkK9yDY8gTmvNhMq7Vq6GJVC0Aapz02_xOjUy24FhOK6T7TxsL-nQ1hv9rcAgmsnwZ4uBe8jaNUf91wq8GbTEd1CwbxrB30jTaxbc2VdPkTKzLtDpeVC517w6AaBbK87RMaHAoq-g89BadRfMGF61-ZMahcBshKcvdkCSfV9BndlI12QiqxB3smmvxlJPmVEgBkV_wfsLwe-FRq_hh5a6570yE3t4MN3_C5Ky7fLF1xQf-wcLtrCgUaOydureC78M_CnGRIEtui6arexc_488BuHzfwhKOpj_IQbongd0jYxnd9JXfBbCrtjoefwxZM2JlWmFT06nUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcsVbkmJlH2AC7QeGgwGDz-eRBns10301aiGGqhL-SRSRnJVnZkOltqqTC6zioD17CPCd_cbMfg_RmSjbu_2QTj-nw6kJdnAhwW6TDVxOOhdLpI_4-IN9XrzDT8MlVXkO_0eSP7JZuUelzDzn1FqIqcMhhG2au9ujJlQzSyP-cfcc4PvtnprpLYyIMqVQnJkWOciyUV5qDtUO12UBwU4jKzTGGy5mn3SAWMyAvILOsk9t7_z8MM87PuctASRCYkUN3rjsIG-Ll6cWjicJ_aOGErPE35hny2oC_S_FQnlYNFcKFFuseUpd9adxfodLwu5W999nMT3aphZjlQVnik3CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcdqw1aA_wK3xqBCjpiRjDJYPdSGup-Zdyjm7l7tyMaLn2PA7PMv5VG1Vi2p_4kn8JMnSAzrH85pGPp6q0SOCE8E3S1PwqsvDdQNcbzbSMiEzFIcRgIa8w6KMwJ5G_3tYrUG2JQq6SqG9U2Gde5CQTtPTSRkD2bCuU2L6_B0mH7VSVLkF6BbZR-SWdVofCWrJS1pvcEd18YAxu0sG_rPyrdkh-EZHa4ch_jisl0hmF_hkG-SlBb-Iwpfh7p0WbZoR-LvxLJHsUO1B_4Gfrf_A39otH45LWmjdWO7ZQF7u_uxkXzuObrbBWdrDrMdicGX_WI_SFUThf4ZiPy1u5qbvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=kFLXEUWb2BUVURJjzUHBCQ69g7kxfs6wGiqWGLRBjWJogf_cMCwUEsbVr5_197vFMGGhGbSam6fbQ9GEmUdlSB8u_EU1jW9tlRS-4UGfc7lHsGr_VGgVUq5iAcBrYyE-V7jQ3aUeDwZ2FKoKqJLxcK2PkzrEfq5LxZ7J9FddQA0lYCqVIx0WTLaBbypV5GNdhUsdXoI76OvPYbsOwMeBqxRD_xeWSdKxpeoeD9l629m_XZEn9Fp6UW_6vO29qjwhoJftNo5hoM9RklKZI5i_ti_N4GRFK7ZcdzsSpXG2vK9_Bdp9bsez0t89NtRGr8Ot0LCrA8YN7DOL8SKr5ylyTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=kFLXEUWb2BUVURJjzUHBCQ69g7kxfs6wGiqWGLRBjWJogf_cMCwUEsbVr5_197vFMGGhGbSam6fbQ9GEmUdlSB8u_EU1jW9tlRS-4UGfc7lHsGr_VGgVUq5iAcBrYyE-V7jQ3aUeDwZ2FKoKqJLxcK2PkzrEfq5LxZ7J9FddQA0lYCqVIx0WTLaBbypV5GNdhUsdXoI76OvPYbsOwMeBqxRD_xeWSdKxpeoeD9l629m_XZEn9Fp6UW_6vO29qjwhoJftNo5hoM9RklKZI5i_ti_N4GRFK7ZcdzsSpXG2vK9_Bdp9bsez0t89NtRGr8Ot0LCrA8YN7DOL8SKr5ylyTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJt6X_OpGAeqhMvh9li9clhKapE95UTrJhSwR9_P5wstova2ewfRkwU3Z0cu-SF_5V0pT7AWI84yxgmgrAu2geT2rWUXXcJwqvfgew7c1oKsvhmwt4YpQEQUV-F6vd08q2EbBO_BQLrXUbcAoiNnFRGnGSjZ2L9cVuG-MQ14ui9PpB4lNehEv7A2h4qLaGcCi56hnNd6P96cTcwvvpbXMPom1U7gRJA-jzEsH4yUEUgDSt9u1pIu6k80vRKi-bKjlaKKDD3G0YPJFO7ySW9O0v1Qq5SCVhR9VqKj5xpRhNc4W1XZwhJIGslSSlkd_WXbCCve5hwm7eJtGvdpvJrR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWCHlNOR3H7F9CYdPkEVhfgwq2mnJ18I6JRUFf1gt1vkwVOE1A57RqXP1pW04IUyfHiiMtgYLsnXqV-bum3J5OaUovDmCivfuVek9yX2N9JQyTU9m3IxFzVlJ9rJ22E_qEIwpCug5zBStSYkL7j6eRkrhFGAYH-JysLqZpyfBSHF6xi9msrr8Q44KsVn-DsI1A9VwJr4x7gUy4dyg3sbDUE_1FXmiV-9-evAICDw5mPZvBkRs7MYp3rRq41Eq1TRaLm51c5vvmcVtjRvCFyfK8j3HHzVo1rKzLbAYu3ivItObdXMIInR0t9aX4cYtwbOc677jYaQ-EkhLbnAO4KkzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAUff8EMn5wkIbL-zxEncl9mxdIwg1psRCAnYb2iyFJGrPsPL649q8t47NWPOvEZMXuPoEBvdcCde5_gQzxbGqCRZcmh6rT33LdOt7vQ1TtKpA1sKd6CXZLdtkeefGCGsQRa_2_IpZatjUwu4Dvf4K48Q2wFNIml3jCusi5Lp110nPwo1_GXf3DIJb4kNsKswob32MdBFqfVWo036ASHK8ftEeL7dBcS2SUUbM0kXDArdjZwJekULWmoUJaMb98XTlSdy5qTVvHu4GlcwU2_tDWESUp8Xlfdf0A_zQTECEVQVV60zWDzdiuoRYv1_yTKUQuE2IxFQRBG5juS9baYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaLE2bgjZODT4E2SdRpTXW1Jmh4xYhpox1NKeGuBlTu3STOcfbYN7D7_kozMLo0fH2rRq35_10pMpCluMvQQDXafIxGJROsceACYsTBG2Kc7_t95DgH3NYN9N31BnrM69Q0RSrQSLfabBEENnMEGfCn60ByHn-FtzMhNArxji4V1PPPVOrS01JL-1q7BItrdpP52rjRHmIqsrvod4wse2XR6rFgn2A64vseZnkBrkNFeP3H-Lc4dN8gDRJzU3YMbm2HHipzxoV80EfwMFvDPC9KcwX98dABlWTY34uWgFL9NMWHfmCGbZOEnLew938sqUlZEI7o1r3Q3CZKhaoKpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQAtktJn2B3EzMqz_NkuYmhX_2cOwsLY5-3p1M7GrArs4mVeSdm9MeqV6RRw0BWWjphDcqWFm_eQrfMy97YS5r9zDTdFj3mbw0dt9_Xbtyja89zGrxKgYln6--USuopRorETgG-CDXMbifZa5imJ3t-kWBS7XOqxyFDTJct5rC4V-KgnzlBXg9Wrrb4YtkpKw9z_Krr-elHgtIaDSAhxFxy3M4y6hviCTbhxvpTocrlAMW8u2yyNcypYrDmdc4IVZvtqKGikguayG9Tvl025Z5mVkeOaBEGAnKy0FbYNlWFVM8gaUDvVQmmotwD9M1tIon6u68I7g6iyCiAk7pNkAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVDKi7Rjg045U3h64yBcAqBGggfftEU_7CM9Ajr42SKGkxlylAbe0swZx7J7kQnmnfao-FQR7qaBbNXY2twWRaGSFlIaT_9-6yHoNJu7Og63_VroFImtWIXAveZwLZCWuvbLyAWyJo3o4WNb67PU22Cjhpp_MDl-TcDJE4JOGp55DdVeQkprbW2FbJl4uBeIDicnoLHQYxiI3uq9M624KigCDiNFiJG2DOAF5V8qlSr86bZe-hb0OPq9q3H4dHVVMRYRWYNY0JWFed__cH7UbpK1e3NsuCvxMMRoIR6zJ0rUcjR--9fiELZRTknTyoqcJs0gBpdqLOxW3-VJas9LkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6h-tdV7Zod9-NeeuVW7_XwfJAmUX4OsL0CnOyFzU4tm0jaieUsJmPJb1Si-4ho6zHebkRrpY9cRfBstsfEmv5gCrvZt_PBMciTKC9Pi7MguNLY16aXHQ6L3gPzx3ECEDrNgJk58rCPFHsn6oj-nI4isMthwjVxYxOG-7pfUk2PkjOepfC4UyNIHCfU-phZTVvyN4vo6iuYSYKBih-_axVmuSZLeJdEBRjlpzmZpwTET_MSyzJyF7MYqnc3y2LCOglEcOj2rrI2iCXSVbVpJ87LGYRLYIjbvX9TePfqBKP5XauwnF8TAocUHK-D9k2x12JG3Ynd3ZHzZG9QNgqbhdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9kcRsAG8_v1fFyaOoNOXspx_t2eKSJCPsdskWKfl3COWdncG_ibxQ40spZ3mFwdBFGf1mr-a6zE3vYygzo-0iRaa45CFA6mUNvoSoYhYdnvswhyj4p-1fx391ZcoefA3m1wjb9zNC5c6XayUCltq_fv52uo81DYQPty0Kyz2mnlunTv0AEEmDUkrhUxiEQlbYisLLLPUaUBaFHQ4pVm-7pmWDpZgYqEsHEjy7ajzMhEVQhjyru3mzlt26h6b72X8NyazZEK-skAs9drq57jLoHlaCFsAMov-hwTeDRkGhKAIUFQk8SHFuzo9qVm414diPYeLA7fOvq5FtE1EjuTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqif2Z2T8IA06DYVSvCONkofJhWg7PtlM03Abzz5BMy0EWHgYN0k58DOsPeuzDTDpGCleZ_lRUBbFt4oXxSkxQpIc4Y0-SlVd0BjkyoT7N1wPpEwPK24VSskQ4XkZ7qQWTfepWOWhVaIdTko1p9PYdm_3bf6qCeByGevEyp6g0qCYpvuOPfCX3iuc6A5gygx1L__5luC8EkDHBsNdI1UgoRZT-2NwX5GnkhrygXaLQwfEgToQY6eSins0l4Fp9pPGseZNMeXt8lJv57hjOPOHFV1RKNPJfoUz4g4bpwUxfQa7MkBoAKFfvErLOnWJ36Ykf2uSnyPCvWp4gHF7DCRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBE4mhpI5-k51QK6advdT_L8g5KlhVfiAx9ax49T5ubHz6rL97JwqrbUxtwfJUaUBaqsqdIttKRb4JRlE-1j5fQsfeQE2W-oHcTJD2Xk1VurpCMiRAsWuJAD-ZWpDYKocBQCiaeSvNYfjn8iZFumE3rKucju_hfRyYZjwMIDxwiXBuNZsB5NkKykDwpt1qdDguoseM2qKswpcfO4IqMNm7JS2XQX8ruqV8ynwcYN_7dVNDEBkZwHVyg-VaNM6zD5LBEPlkf5Nz9aX6FUawERTLMaWfArVgjTvCoKf5eEo3fYvHwRludHSaXz1Vv3_30WO04lYwPpb9O_km4SPyub2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjq7F_mM-G-YbCTCgLbct8_1XiIMmuRE2dVLRkmkndjc10Cdfds9EoLeTul9VNVlmJ5B7f6oEWHTucCOg7znQ1vmPR78-LwZkrk5SoUc2S-ca34CGPoQzmfYKuRNe10dpYbbvvtL_-wkObfvzzqn20uGJc0uhezR-Zh9AT2dc79khFcAFbHrMiwVAbdv2YQwmgFT4tKhItgPjHQXRNkxqiNUQtKxFXXhEg5XAYJ3GpiujZv6x1dklgp94kJcdopG4JoSj0i72O-qq6hjQYyRxRcESluxxNwwiFGeybcf9kPlr1m_Or4ST_YAx0zizrXnzqrHci8RiFj7gdnxK5uTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSyQvpko2uDh0kRlVDr1cj2r07pPsOf3g-C1YSeAiXISRw5oI685Z_6vK0qLA2N6wotiDVk2pm0SSFK1dG8OozCtQDrDcr72ZOZJnUCtDvXIOkraLjHp-F1YfuIr5e8AjP1o2sGmlzACLswJ2ri2GqZGT8aTLob4KjWbJrxu5TkWaZ9kFLTOQF_YBqZ4hMnB9KANQIbjx2uoAlJWoWbvL0SXp9c_bMWEhH9hcQclmEXil4YQ5Hgv9kQbHWerHRwdcdG9whOoKHKy01YXnQfFVYgAfBBH4_aZrB2uqrYRoqs7aSo7VNzMZp7jFFM4B9SWCY89PIa0Jyo3Nz-akgTtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG7cxMocSqEMEmws0b6361eWURErSZZ1QgkyCAYlNyQ4EM9Dd63hH5itouFSC76UcaV9I6bxkPN4p4dUDLx9SuHxPtqqCyUxZn7L_j2InyPjvMeC5WREBZ3Yvl5g08GMpwUc0R67xnAcWI6n1L8OhQbEOfWGHo-Cg8KTkJP9-2RuZuNS8pJU8bOAss_LAwHPY8qN8Nlfr-JWA9cwMZYq0FUhU0il0b7PhaV6dcESd7KAlg1CfoCSsmLBT2MFlsLhErH43If4Dx-5TqQLKAj_lQjRxUAkEPH6Kx-DwybAf8V_PEE6yaozmrjXCwzgzeRPnAsxTn8U4YEKdx-gLXAtJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=qAziDega0QLBXasw9lvYyphAWxHoVI0CN-ZQ-mIoXQH3oI1oLi5UPoY6vksMjziyxNazpw1guVKULB49kqvUMxx0W_vwT6m5TyR2sPQATYt8gpEgeAgDWShyazUu3_VQ4b3R3ZiRnr-E_saNBlSJqFM13BJHXB8GwVDa-RyKXF_Udz0TMtDSLFPhD1cW8A4lPJsJZwhMVuuqd7Le601rW9lp7ogFIFZdfy6V2hEcZXbi72jlazs5-5jgJui12dq4vWq0p73PwiBbRk63iSZKy4e9WWtmySMSMloEwdr_96iACrFChXke7IqDwNt7xiVDl1eIJ9UO4ZjAU1bCjRlEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=qAziDega0QLBXasw9lvYyphAWxHoVI0CN-ZQ-mIoXQH3oI1oLi5UPoY6vksMjziyxNazpw1guVKULB49kqvUMxx0W_vwT6m5TyR2sPQATYt8gpEgeAgDWShyazUu3_VQ4b3R3ZiRnr-E_saNBlSJqFM13BJHXB8GwVDa-RyKXF_Udz0TMtDSLFPhD1cW8A4lPJsJZwhMVuuqd7Le601rW9lp7ogFIFZdfy6V2hEcZXbi72jlazs5-5jgJui12dq4vWq0p73PwiBbRk63iSZKy4e9WWtmySMSMloEwdr_96iACrFChXke7IqDwNt7xiVDl1eIJ9UO4ZjAU1bCjRlEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTqbdPBkAL3-do3Sy8u78kxuqYPM_x0uHY0DFrHGhZiLLZXs_3yRYBu04KOEDbX2YktOdKx_jkjJYRq4qduTX0Ob_wYTk9xdQ1Y_ZrJjfGXmo7YOOCxvbYchux5G2ty2MSl6U1bwyEMCsqwTprFZrwAqfpn0Xby4W8yegkJWbc7cIMNC5eEaXZv2NQuZY-Wbhg1eWAmxdeUNnBZePe71fUXp0hwJlARv4cD6XY-r05vEpu6g5RQ6Mvftd4Tu20klsIMZ5UWfnHqfblOnmV5ia83aVDXYMYcEIfN4SxUUVDYeZuYTVkl7YfoNJAUiFjBmoabwV09n_nERl6AZJVgmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfcK4OCpwSBmY5bwmh9gMtLZl-bPDmecSoXaOrhwH5fGPhkIPWYp4ud-LgI5wGo0ksJjctPp-DCzCYaoTZ8u0uW0w_ej10xI9o5AH849yFKsQzMgfzYm1VOF878Z1klQLjSd3-j0YDdnwVVddZnBF1fWAs--zE2a8nSTX3aIGU8IuJboVaPw7qA9zZKT2lwvfTMgbPCOBz4i1qIC0753KSqycqrRBUZPHJX76Phhh9LA88vklD5Liu68EMEgqeWWY2nAEZhRktY1gXhC36EtZU_JnzzqysFVcO22IZiQyMJSq_9irUBUBgW7uJl7XVs2FHQ7ZLjp5TvxBsL8gt9C3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRBUDXPHejl3CdiBiKvu7j0rIn7G3oUAUonArSvHM_q1yaUZU8-SPFE3FGcPb2KN6SV5TpEGg7sGOfgMNVF4ntyQNcImn9nY1ukOK0uR9RZaGc3fYU41rBBHCkrm0W-9oxCQ7Z385jN2ihaIKWsltf06cH50UjDOjwLMItDos9NL_iMOgfLej--akt16YAB1LEi2i2miaAzw3Db_BGZIER8qyl97HWd5jKvf6uztT39u0F5qzBE38xjGi45ZOFktKZ1UKcOObRMoYLbstPQ0guYRA8QEBLohtvAZGfCOoSiCFPZ5OZVdGVN4Kwk1B2u4gaQlw8jImhmFhI1Au_S1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaWEedAxwsMIxohNIMM_L9hiTvLvbBdZekNvgW_Cj50HMq0LHPR0ktgFQHHu1Km_fA7RnpCXJTPUjqeUotGff33XPl--2qYGhUpH7TpsY15XejSG-a-pO0HvdlG0G-GyAqvyW7VAgzJbFgP0y_pNy4LFRl3VuRXwZRRgfsKJuv-tG1hbHOuoWcF7DS7VoRQRxkOEWCam8GhF-pxag-GW_WLN2duq7kwcfrp6-648KML-0PuyjjSwzOcHIda28NJoHBWWkqPCIro_UqVGcIBs2Ie2IKs0ia0t0zen9R1Gx5OWdzm-Cdr_Ms7ISi-pwNLKRh7RytmzVCAEujNUwUxdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhOJ5lSZpy77BYgfA8lJN7g6dlw8zPziKr3WIajB9qmPD72ZOacqNkrnLiUlv14OAHYVUGwBkgKmJIY6aYgs_n4oSe7Ofac7fzk6b-_X4ODQsyYhZmwSwHpwTAQtSElMsFdF30wyMlcWp3EPM1Pui8T2Of6-bj6608HHN4O-W0rbjzKI0-HuRxhsghyjBXiGRbz2ceKW_xRz0wx6t6WDHCdyZ87-dPzbN7KaaO142IXTU8lVzFBjZeaoYvHHmr840Cft6P15Y60lYxwkde8kQvKD70PxvZtcQyWdmpd4lyG_GkjGeeBfAGraiCGqCk6CDmBbTN8vfh_wb3t1sUTaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRmL8kRNLk4Ha-s58DDbA0iakhyzII_gwUJd3lpQD8E6TAcyZlHp4570WGFo-oWJFo4cl127ZYN3AZaajU1jUf8ON0E0j3u1mPS-A2mimYMyXwXq3mGOPl7gOa6wIUltWGxANlyzu5I4ECYE9a27KsMjkly3EMQB76EBr9fh1YkZueVD2btGYEbw1AhOJqhryyTRofO0Psfk58XIiGstUc9BlB1WsnYmrflpb1ysqYgw52Ky2ABNijVd8FRkp7E0POf0MgZoaM9X0-fwkAHFMmwNyPa1htbYBROKVnuWBPnEojAkX9shOOn2053XZ771EloYMOJmbpTSkQHMu1fIWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxF6TpqHdXY4ryt5JDE-_pSap_3ueHvWJ7igoBY4UGd2hFiv51mJbqIR6v24dWMgfOdVXGazloheIr7xdHmURGHvxn6EWMQ3vOPiXvqHNQc9Bcbm1xquA0zwLgmDTs6NivNxAS9JdUa_ywUzZccRAO0HaR9pssHHV1viPQJoRnSxfhYMmn3fT9DNB7kdnDrxWiKUBGQW8gRKxz0b5olhCbTzY3KwCD7sTXG7cEfHOvi1rPziqgCoeRbwPs7WCFAxGX2rMktyyy0NOhQvJrk3kCMobIe7Mh1M4QiNRNnB3zvf2PaSKMddxtjLkKWtWm4K263rZ4MWWM5a_eno9wy7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
🔺
سه ناوشکن آمریکایی درجه یک جهان همین الان با موفقیت زیاد از تنگه هرمز عبور کردند در حالی که زیر آتش بودند. به این سه ناوشکن هیچ آسیبی نرسید،
🔺
اما به مهاجمان ایرانی خسارت عظیمی وارد شد.آنها به طور کامل همراه با قایق‌های کوچک متعدد که برای جایگزینی نیروی دریایی کاملاً سرکوب شده‌شان استفاده می‌شوند، نابود شدند.
🔺
این قایق‌ها به سرعت و به طور مؤثر به ته دریا رفتند. به ناوشکن‌های ما موشک شلیک شد که به راحتی سرنگون شدند. همچنین پهپادهایی آمدند که در هوا سوختند. آنها به زیبایی در اقیانوس سقوط کردند، مثل پروانه‌ای که به قبرش فرود می‌آید!
🔺
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند،
اما ایران کشور عادی نیست. آنها توسط دیوانگان اداره می‌شوند و اگر فرصتی برای استفاده از سلاح هسته‌ای داشتند، بدون تردید این کار را می‌کردند اما هرگز چنین فرصتی نخواهند داشت و همانطور که امروز دوباره آنها را شکست دادیم، در آینده بسیار سخت‌تر و بی‌رحمانه‌تر شکستشان خواهیم داد اگر سریعاً توافق خود را امضا نکنند
!
🔺
سه ناوشکن ما با خدمه‌های شگفت‌انگیزشان اکنون به محاصره دریایی ما می‌پیوندند که واقعاً «دیوار فولادی» است.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4859" target="_blank">📅 09:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vo5zsIZoX0xr2wxHx90DImxeBqfNjs_XjDdj2r55ioKtgQ6xCNqF3iGkJqISbESm7vHd_cF027G89lkEnxOiO3P4duRh12Jg98l9s4Is3475kf8uJB8DUDYdQcbYmT1QRT4tMLoDU4l6oG5stu8N3CgHw9H8wZknmncQmGhsHRoogeKeXdIDjs29qHXh9UeEogQ4j1RBnEltIGw3p3U9A5A4Oec2p-GI25o3523wUFOBXo2l0nRA4CwYVGsyRPti10x6nUGu9BV1Y60WjAR7imlBH2DXU4vBq3_pBTjlyUnfn0SVWi77KayeD46oAnN_jntGj-oBFh48T8EC1leV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
