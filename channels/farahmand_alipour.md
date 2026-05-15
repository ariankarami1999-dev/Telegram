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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 14:12:51</div>
<hr>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlnVzBIQgXIkYtcbZ6qUtWk7_iokG2H_rnHmojnaVsAwEo6gUeDF0_gvMngFePIncZXk61TbmAMx_UZoRs6mkD1IsuZ7UW06b2QwLalz8mPXMKzw7uJxclRIH44X2iPpORCygyMC7vupJnkmFsns8ILDAH-0vzgxW_aN-2dqgFdQH5zX48ouBCLMSHrSoGfll_0ERKeGX__QpFqqaOOkxy6krjX3_Wo1cOOX1J7nWbuyHPwRXFqzc95Lh6j2KioRLYCLbSkvHH4OQJ3OqrnG3oY0Rvfc5kIrq_RpJz6x0T63l84B5BLPrAdxYuSEpPm4tdwNd0TGvsuIv5WnBEUfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooXPqvI1q8taXawnq1FN12dPEqhZLLLOH9FdAjS2xz6YfW1_72kw3Bmovod5L7KuwOrYv1pcK-jlY1NWC6-5KEhcwsvf5RJG9Llsk3Trkpg5z9X_u1uaEBmhFUcfo_qKjSNff4TwDiE_ljzgxlz1EAI2IB38wkBmIm8R3QFqsvhwCf58Wft2k9g8hXTXSqTymsQvwO3z0eOk6-i8axkcMcG0nadoNFF4SAfxi3nY9LvBpSxtZzdZ5aHVNwoIEkaKs2e7L9uWwtD9jgqg185fQcBi64msUvdXLwtuJgxSHg_M92R9OO9gF_ibn2wkLqZ6giqoGLgUvjS8-wPYgkvcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI3NqYvgnYCvdfwM3TIifs-Hrjd47WfjqSrLc-uBMqrMWDhV_STCV0IMAMUD0b9gv-WnErRjOfyfOT8OM4kdoSUxBCC6rYVpM99tLto53DO-bUR1gYwlpbu2xR65zfyJovtyJp-bmmJMVwPvIHTAewRs1264rZNZuyggNyXnFkJO15ZO1Gp9KACx1ZHLBmEmeZisaoHQtCmgrKpWD5jKCfP8FkjEvATQVP8fCcaHbkft8Q0V0R7J3hdjNnZAUUF_yGoULlIwwXaA5BOPGaP3ga4cM1RySMOnSACMN3CC1zx-s0ZeY--KKRFAnKL4C-tBKmj7vyj9-Hn8rFz57w0glQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkRtQweSpzVqw7FGYEWSZXpGw5TaOk2ZE8Qx94o1OFjACfqTgqeIJtR0hhJnmESf-xsaIs5yldosE1W9DE_MGKndZWaPogWI-0qiWd7YSojqnlzyciEWVFSe92heKIpFR2wewb1QDV_IgRW8UoFZJ0VN0aOyLZR9aWAVEtj3bbGbxBmmOIEHkanuVVHbloLwD2ARPFC8uYITNCzyorfmDMRbSeidds235gIwgrJM-bwFevmODNL4WTa2Xf2J0cZByUiXSOBI6ugzcxdrG_RZFMWaSd0lhroymMaDQYJko_yjilsRPN1c9ADQFX-DKwMatB9UmeA2td9A-FCpG35vIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TctuQBVWSHYzJWjsgbRF8SY2ih756ieywzbiHiQjLrqTrMz3mq2_kvChpXvWZfTD4p0I_2o6O-C20iJfcWHJ6TzQRufMJh2SG1yU2tkTjgoicIpg27qXT11-AIQyS6fCMf_FOkZbW0sVD_V5E8h86-3ELb9H98GNWMait_eci9RNT0xGvgk8CzOAqISAp3hWr6a07ZjXgVSHJji8BsWl5bRuUoQ2v-L3xw0MB4IsnvFHGITasEiMsFtmg8Kh90Zxe1U0i0EFm2H980Ufc9aPentUa-fpzg6daeJpp0UJwZ9I8ob-6ioqAACmY0KX_1eVlIj0_i0tiw3xt8A7uILnOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJqiGmXdWO1ei9fH-Hsz0MwOa6YuEiXj7AYUIENCzL5TXQPf5VoWrSGFMqrWgfITt1BHBafdzwf5gDj37ZEhxmPEYJqleWiJmATVeG-eLnxeimFZEnJjMddI2xhCfa8ag41NbaSy_PYy-ZzO3MNPRfH3tENXn3GcZeAdQwb6as99fViLy_WoEa2xHb8eJlgO9ni2XxKP4TjHj6d2kDcU8f_vxOl46jDJZ938UwDhvBqQvNgLy9EhnbRmgiP05p7D0wC4S39wZ2aWPRPef8YR3X_Lpi0eGkIiz2cGXpx1-K6YOz6URlv8ZWDHpys62qVkaX5BXYbJQR0DHCvy_UxkQg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rK9SNlipxaSDhCc3V--UdYPcqsnlD84712JquCELqpczgtKuWxayTWzDsbr0LPM6kDH5zTw7xPSbOpXjKdGwifa4xMa3KaXyqo1Qa1MvqhUCIjIDBZFR4QQX4Ddgok1CNFz9eYNYwpUH4yWN2MBDX_Oymgw6vrhFavpWv_mRxTZeLH62DJQ1sNLXVH7HWi3C9O_1Yb45V554QPVZHklPxsgoVhPkq2wkyWu70NgNd9QRn9eNgxiOfMWrMaZMt9O5y7XxTA8ftQoy272icCtMEbmhJ3HL-ptz_oM3Jx_VWokXIq_t8yZluMiECiky2h7z62qwZaI7KbJAi1-dtuM7aws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rK9SNlipxaSDhCc3V--UdYPcqsnlD84712JquCELqpczgtKuWxayTWzDsbr0LPM6kDH5zTw7xPSbOpXjKdGwifa4xMa3KaXyqo1Qa1MvqhUCIjIDBZFR4QQX4Ddgok1CNFz9eYNYwpUH4yWN2MBDX_Oymgw6vrhFavpWv_mRxTZeLH62DJQ1sNLXVH7HWi3C9O_1Yb45V554QPVZHklPxsgoVhPkq2wkyWu70NgNd9QRn9eNgxiOfMWrMaZMt9O5y7XxTA8ftQoy272icCtMEbmhJ3HL-ptz_oM3Jx_VWokXIq_t8yZluMiECiky2h7z62qwZaI7KbJAi1-dtuM7aws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiOPbWqcvxOed_dYQ79laWlUOjJ1UzyySS3U0DUEqzM6Gzy42K1Bob1CvKhtDy8342xFZG2i-ycNz16EMSwcfUL5AinpeOc_ppCH4Us6lYG8CvoYzIi5-atuxXGbJSUIxOwzL0chf3Od-nSq4g9YvG95JHD3_qzl-D6OUJI0GuLZMrXa-m8QSt6LwBPzqCql6yRI1npzoBmwL0JD0iCWLEvK4OHqG4mK3YCxL4xU4kxEOSn3wo5-7hDwW-hGaCanAFGdZgZr10NQ_jSO8UE4yint17YAhwJrhRpNjkxnykNPcItjmk14sqn0s2wypiQ2Z_kJxfXXopadQkdQ2NBnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJG3e0iZP1_tJCDsuy1WQl8oqdYOib90NQ6kTOKb6mj_P61D9WoqfhM_w9XpVcN_a6eiurwGDMKrei_EwMfCIoH85BTtRe8Y6VSkZG1aXqb_eaMCC7o9GPPux_ygK5V4AL3PieusOAPr9gOL-Sc1Wyfwl_dKL33JJHjAe_UWlGtRmXh7V62pAOzYNkBIB_-kCrd_1ZIb0MoDRE8JEJNML3XMBBLIr-5lB-x9te_wk9-9HSOIvv1ld6oWZ2-jxO-1vaZwiMGuUS6f8Ga2nlUWOnPk1CbB4LNm-urM6JRDrOhtJScpsjg8RmykIh1jeNMv7_uNRDfrgddA_tS1uzOgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEgpuXlQEXsDp7t-knrhgIo1EA0oO0PSrU2_6Jl9A70f1BhVcXDs7c8xbgd-bG4M18zMZCKwI-mr4vWDGv8XCUgAJcSzNCpoKnoMtXqEQL4xnZYqaxYu3yujiUfz8D3S_vnuRbmM2AuBjzQZ2m2R_tkLVGilAPi1MQUPeuFWsFmG8lChu7OzRSfYb29jhe7alshFXZjDFCtm-kYRWIe7aAcM5UC7kr6OHRHBg5XMcXMtOqbQxSyntCC5UUlrcMt_lziDaCYMbVgsHluZ0Ky1euB7b0y6UHLStBrTVN-eOZXb6lHcJPeNIEEw7Eax1YoE2bXhZj8d9MvknKzi40moIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0oYIUqPuBSmSRlPZIlaE6aShAt9I53Jd0ctwW8nZkglkD91WpuzbyqVQIeS_tKB0z6zQXPOFzU2GOcvcFmNNnl-07EobjORzVLgWWIot06Y-wWr5wCtSsT9QI1Fj2vlxNKGXhJlTdmyDqMYMILhM90a9UhwbNi5RPwyxNXpGMVzLfUY0v3BFKeFIyazJ3RaaW-jmBXaX_JRAZQtZ73iUiSHQJM6PopVzaAayvyXyPNjgOwbOvf-LCTUfSxQH6yZWDiqMoDOojPhtbntP-gRJeovJ6eGo534haUIxy0rWJch_F8je6agzBZl_C4f8br3chUUev0f033x_upfyQ8rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXH_arlMKHNj9PrcVrC__p2X0779lc_HNhuCv2w8SebKkfVXjmTt7uVVvIt83uUV6BmJ6zKDSKARfpXs7IBzMKZ4tLOjv3cf_aObe2E_y21ZJSQYN0iGpCUQoGyEJsH8-tHNBCQgOAqw4arxNrNW4XrI3uCdv9J9-P3trD1UquZ1oUh9qUhF93JR0dC_gHzAp3fUetJ7lacBopphSDD9yHC7zH8vmWu98PdtZqqClAT3Zu-sZtQTFTqS3GemifqUpsUcYzy5XfUp-30x7PUR6j4dIG6JeAeyq7tP-9IQYLKs3IbkcuPdNYxKpHy2d-5C7klBchHQ3ztBXcRZp_3TiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELCVL9-ohdoHlZpvwhtU_YpEo4u3Xkx_fb7qpfiJQW_-hjs2IzpxEiEog_EbZm_SSaUjB9s2ovN_3wtAKrK0sjL_RSaHNHDb-knYqK2p5djwOGA_IeYeJr_1PGG36NQsmLDZtJZC1CDCHeb2IDeQAx2SHksWMJ1cQbhcRQRhX6--T5Ny0R-A8rYVa09DAzeYasCKHNJtp3C9uOKdmvJAte2T4wtfOzrHZh_5eBoNJ9p_R3GAqltO8eoXYJbeFx077Z2wLeTb9id7ybS8swgBp0BcocDlDUVSExn6l1AQgUXQ1Wyu4rCQq1f4bFx8TUHSMALeQD4lQHUmIGSqn44qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgPUdKOJ2Tinlo9TuunRiQ0ndKvMlU7eiGM75EmhKKXEbNfg1oj8X8ouTNRDKeK1LSBXGO94hfbcX-p32c1f0hnzBJ0A1XybmR-Xy_oMccrr3hra5bOAWtyxeb6qYWwuRkcpvK30_4UTbOJb8H81EUYOUqFtbWrFA3P4thWBWWNpfnbdYWvsLukUwagRFJS64AwiEzoFi8tdilM0lL137Kr7DG4OCARqrKb9GoUHLjWlzjZvmRWFFwQglal-NARKwqV4za-D_Xx6x6_CLda3ZEHdr6icmzzmjdDa5fY2SX8v7clT_hEq9s_d_oYg8SyQf21nPM7YLburCG3gbBW_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNiGi_9n2GhIL2-5lR7mpq1xJh_xQBci3vLLl_20FesEDkqUhPrRzkhsaBaC9dFmayYqnfSp0Z1tdPT9VX5otQsC-8we6Tzz-XzuHXdAxxAjUw9rk06c8hn0dXX321FLigQnKnw_Qc0lL-ApwX4HweOeGuOJsye0WTnkUUt_tNBBKA_Is5uVKfZv2Cqv5gP6LYaGvdxChxvj2s_hLJle2_6SLno9-t7TqLMuBszZr3CcxG_XSZER4_vT0JqKD0Zrd3hbyJefenesI6HnQtuXRz8B4RpDiZAsm0e1V-8w8YvDI_5ANQ35K4fqKvHXVm2w5kQ9lnxi08UluqmHyAD3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AarMSSO4prJS7xBBTNk-eKpbX0wWDGD_UQj8p3l67k33uo_jTVR3tKQS-N9ZMH1W18XjCFdoSZWZ1ZXshLO_kF1i__AC5Uw46eabUgDtty_HnaSw_XmjIGG_ujaSF0U9-7tpZ1XEGaLTID1zJlx5r2WYvbyyU5wvCTzrU7aHBE4zNjkIPzg305RIdvL6HZASQc17_DgqWrvbRSdyo6wYem1FTgTLdDy_T0l-Alyk4qlXCYkUXU7Nsza9s02LESkvfyrdN34-J07ftB63ww7PZIo5GmN1CX89Kt4wK3dIi4EtAmj6ZTV80DxJJ6vVZ1nQva6_gI1C2vXNzdexv9Ruaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_ljN40P24uff0MN2aygfbNPZR6O0L2CPf6-ZXjswWKOLS654-383D1phEFWX42JxRSXJdEwmb_vMQ_NkRr2Dht8cNoZ-u4HI1tp_GdXvUgKyLUMf9Mty4-GIBa-BylIWgNYAimNuy1d6lQqvwGV6f8wM5Yi-QZ30BWvq3mJphLDBPRJJjxWvzvlGXXpcdVc6eZJly55PuIjZ-IzE6x9FUSmy2RZNAYzrnTH63GQa_CDS_d_slRkB5vwsGRQHud62vPVpV_P3hHzS8n6ODDylhI9Z1AEj-rd2OJaNQOsRtnHt8_rmzFie55pgyEJ0ejVAcmFe4tcUBQOHmnShideJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTQ22mlnoAe6oB5L9hMzcOIdGzsElSmVL3uLYX70QRETOYZJSlMwv4OL0tC0Ai0pbih9LqUIb-aGLGg9MM81HN0QN1DFVydBFFi3SXm4op29hNb-kOCE7uxV6BFK27EP4TIpj7G1yG_3amAp5m7SUNPWIIjYKLtqeeHrfcbI7SDQfWKuG3ymm6AihFym1fLEHQIaaffKZmq5advm1REUbzDhqjL1PY3E8GWBYe6-HzxQvujm8VmKGZyERLoF_UMIDjsZk3l3Px_C3uwVFMJEqXQ_nmkZjExSVh28rc3nAb_nMbL8mrhqeU6vOLGJ8qWjO7y0nMur_PbnK6sWblJStw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOIYQPv0P1HU-Vmikjb0VWTvKQxRyX_IagCWspUGlOml4Qk0c-hqpATeWeN7I14JQkgibvAs-F2s2IIDgPSh2vIHc4BgmgGmGniTr8aMEjkwY3Sgdn7N0xrK_tvg-aSX3lYB-dF16gGu3mX6gF9tHUHZEFwvJ7b0Wp7zy7iZu_2GBX5dREWgXJbAjs51xWcV6KSXWgupqdXUlRW5rojMLXeWzEtwbdttEXeWI_W17ahifgLQ5V9jOXlcaj2_QwPK3ItKbBFa1pmiht_Cjur-lqm1rDM0cXVzxwNQgvlmHxz5a0rrPHcYh5--HVcmjPH8I5CxEIThPQ2R3Y2zz5VviA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9S89LK-VJ1zJa7ZM_yIda6CNeF5vn4gHKY_IH7z-6stp3wYV7WV9wN7Wzj_i7V53foyttEi-gcJ388zCLZXAHiJlDuGhZtzGzGFB_SUFmsNBCWuaEgvJTnTkJX_mZ0Bt8jUEV6obrZqwjzkSI6EvqlMtOgrYOvzAOWSca4itk0Qp0c6Qaym4hWZuOlR8zKYKZEQfeHYS58htW9g5Q6xzjlpi7yafkepOpOJbExHeGdg-0JRHxH-ZQF97bW4BZvrm05z-sFhQK9Dq7HVH6sVaRzoQgt2dCdUztO6jTuoYrB5zafEydI6FhfJUQL15pi0ypD4J_dtHKgOjQGGF_RXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrYLf0De-85csswe3dcHXpJpv8-qwAcFoxABvFNut-GH0Aq4xtX5F-YDytGe42XtktJv3mukYLPZRxn78tVFrf7aDkRNd0wDulwOs6ehHhrm5_lcBmgVOZcpDXi27pF_6ZTdEYZvyDt3FfHloEwYZoti-KsDnh0KAcT-WL-p7MjYgDnU8_FJud49s_3rwjmWP88V-ndfb68otNPD7vec8cu0FJOiVGNNUS5-S3yX7jCtIgJDump9n7Q4YDEjRxjkaAsvrGC8MOswW-_X4hiG9SOtpRnjx8wqVmiKQeOiJQwNChdZsk08d6CvZAirTfLeVlExWsPHnxWiEJ2VnSCHCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrmFJ070rpFAcTAUua67fwr_1jlWzjtzNB8fKnwlo78wv7XMtdblMeM5KmYyaWZBytfgKuMmBcEweeVMXOzeQz_mmVDEhxB0yt9UBf-x6wgCEfBPOMQwWMhPt7auLYfIREoaGwHTeHpPsstOcIuuhFJlnc9sFZAnjJoRTfHUg3qowEH4_yreN_EkniEf0kdOdzcP6Z6q7KjXBjv0Xsi2BgSJd_teviCN5gpBrBZvL1cHFNg5DsdQTk5lbidf6apFfVul1H-tRbDbNR3CqpkGd92c4RNLy7wMedNHt4GhCZk8aroOgTmzLnoceO_VTtXExclKwDd6XCuD08XFnBJlug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzQA9WizNMa8nViAwY0MEJaVRcvhBFgPYJTluAMHpeUQA2_Oj3RuCQtPJmgSgv84TkXCK8v8g1UaKRIatNcDjc4BxeGteyHnqI_67p-nlogBc7hUvRUMdtCOcjOU6CVfEgsE5CcY5rEv5UPg2mRgRDCZ2CtZBCIHootyQZGgr7Q5s-7T2rP8Tgoe7WXKFzPJDo_rJLyCWjbUu0qm0jFaAwv_KgqJnLSeomtcdP6_i4H8JMGb3TlOC-31rlHBwQZ_9y2qPJijjzcxPLvZLHf7T-n6pU9NFT24yZELzTE-EHI3VkrdbO1VWypJUibYKU1JymJidC-1HO4oIqUrHiufog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=UWvkzW6A6U8nMWiDx6LyBKnn4l81GOzkfdv4awD-HNot9OZoQGuKpgj-wpK5mmZ8MkC395yO0XFZrR2NKo8V4nokzmfFdNCkjo0QkPjOuANfv_ID18K0t1jO8ATrDhkG_QS3XS4Vby2E-OYRI0DVL4CMoqdEkF9qd2n9Xm6CIQezWEPKB2Qp_CYYrR0pUUHctA66ds-kTXHZve-IK-yp-P5K5-JRMG_VAeKzfArz7N1YqzJ5wJVsx4il3gvr4MqB0A1stBSVVUsQ0fxNHMPx9DkcfWbWStBlsfO6RnfF4VcNBsMc0JtblFrAUqkikDpPoaH6T5BvTKKWJ60NotADhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=UWvkzW6A6U8nMWiDx6LyBKnn4l81GOzkfdv4awD-HNot9OZoQGuKpgj-wpK5mmZ8MkC395yO0XFZrR2NKo8V4nokzmfFdNCkjo0QkPjOuANfv_ID18K0t1jO8ATrDhkG_QS3XS4Vby2E-OYRI0DVL4CMoqdEkF9qd2n9Xm6CIQezWEPKB2Qp_CYYrR0pUUHctA66ds-kTXHZve-IK-yp-P5K5-JRMG_VAeKzfArz7N1YqzJ5wJVsx4il3gvr4MqB0A1stBSVVUsQ0fxNHMPx9DkcfWbWStBlsfO6RnfF4VcNBsMc0JtblFrAUqkikDpPoaH6T5BvTKKWJ60NotADhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMLa0CK8zXVWq6ldcnnULzi9TzYCUQBzNCQVfj3fyX_HBvjuKR3pGn16_IO8f7XcQE_c2Bk6k1Tm51MHJfHNfn0yysiqPcMunBn2Y7Z9DZwqTtIo1gFjOXM2ntP2lJHdRSG7KVr0Ex9KEiNWdFm_cdgjHgEsTHXhCyxObKxc9Kjk7b6WAP6qjVOoVtqD4z_Gb3yWF2a1ho827KZU-T-1_sWyfumqwjC4qY4zuuqz22Z8ulYX8-i50oX-zLZUAKaCsAG7T3IQgMusEQBCZVNioL_pcm1wgMe1PZwjQQPu-cSaTpEZjVBBDPO7xHd31MRNfdUWRwzAtkJP2ALi49-E7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2HZaNgGzyLBMhFMAbv7Ja9X-YPBZNTSRCFaxVhhHP5jZcnHqIDEXqpeMExiTugo3PsVH2dT0YE8PUVOSoiiVFoKOWgjU2OT9Ir1kCfbOocg6N1U2PdwWjU8OSMX24ozuFVnAewp0-Qj6qyFr--zHK5F_OA-7D8sz4mN80MpcEaMRmYUzAcdgkgRY7ijVwOEMfIFoHbXOkJbDlJ_IMKDWL25NmP0txH_YQJ3ncNfxao8cuf4dVfTSZyAHdaAEj12XF_GhRy-y-3hOIWjU_0_EIQeFhHvlx36-hj58-o3jL31aOD7cwvxcXmscSRctWkEqqYMdlJK7k-eD18LolICHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfOULOvuDmLn8vXqvS0wKUBwpqacXm8sfSiGT8trW1ukuO-oczvpqN5gFROCwBmKQ5KBxQ0QxKX1Vo1tkvFseWiEUwRE2IfZGQeiCBuxL9yQXQ8L6E3iP41-hgKka2lqqrb_bR7jMhjt4cGV62Me9TiYb20NK4q-7-IlwHNVam90YzBWFH8upDedJh-VPT-fQWffNr4ZLRCsnV8bc_SP5t5MAKo_O-Rby9Zo8_JhAzSFOn0ZivtLUD1zN9gvyIEmilLM5GDBaTmsBKsB-hoyaYL8UwZCz0XJAMxjGC2rCtWZXSU_fLr0uhYDxFYsf4B0HVbs0aL1gEVl6mxqhKXAcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aks7AUZOuSGljis3A1OF5w-OndoA7qj5Xlq5Z-xzMkzJ_ILQW2miRsKe-nkhk441d8wfGTEBxRYL-h6EHDGAyXHxQsY0aN046W9hqkkFk8IXnJ06t-xan_Qs0jJ06b487dBAeixHVojsaIiwb28Vyc9t9KgWTSUc1ioTmUuLXxBJMcJ4To4prNA6lJIF8Tc7DbFck6AdOZm9bZOubV4Iufhx6q8tzPXal6UrI5IagHYDIyPIOVdGW_lqMxY2iEkljHvTJnTTGjtaSbOnrfjAutPnxK7jVh3Mh5LT35_5NODklsGK4Ap3BR8HfcKIr5NtGaEBJMHvtgoviHNj4pv_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWxjm40cQI8U7esQ59iMSzXGRhyIbnx4O2wBXGU5CqAsfcFypvCkV8T40jdevdSSySjmhC5kW4SnCdOmF6DsgFKo-3CReBx_Uup-TJdQ2T5CvHoE6E5U4EY0RTxCYfE7Cn8Ua1NY3XGLBByT45lujBvUyjirJhALcsbmqHzGm4CHylHd4kflRhGXsYGKGoaoOZgkqDxTFtVjGIJnx5yof-hlDxkb-NSV1V6d1f6g07SLzXZfokeEVySV-fqaWEAUxuHKnpv87HeA6TNMAsoBUIukJy-DXarSwDB6JEA0cIy0i7Ao7iaRVwzU0DQFalCyQc56vlTuaKyCWO_-LSe7_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLhTWGzQn11jZlqwenkMStayiU2a06vai668ER3cLitNVtVgSRXkumeHDOS7ZbbbTs3X9nO96lQiRStN-_0ynUl_u-icxA8U7Ta2UC-R3SMLaf-0MblDNPm9L80grgyxKA9DCxow64cadtNyeewwkFvrhpOELMJM4w90gaYbGXxlnQDeKsK7sEo3UJfpiI4YAFIVtoH7dTx5pOqAJIRZbaCGygUNTrNBj6t70oFtoNF2nIexdeisa5rvZrf77O_5fBEdS8Zzbv2-L6j3RxqUJnXIuDYRO7fTxx-1Czp3xVZ_vnIKbWUJ0cEUcdHrgPnvH68juqdjOiBi_RHznkxvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siVp1w14ebAAPCzs5MIVuTjrJ60aPoO8VKoi0Ic3XbYqKZSQ81hPAt-EjvP4OuGN_FI2suWzs1s7ySgPutNWNsyE7-ChIg3_d0x1sq9NaXaKCxJBtLrn9LaRGbX4UnxLDmNDf44DI-VFhTktr7T2GY7T52889rt3ABb7DzyoKTwWVwMuYYK-YJJIWTLvmm88q_BhU3HpZsBufAp6o7tzOdzdfgg-Mkvct6j65rkqQTnZ6nIFWjQHFLJ8syd0fcEKqhp9YhUQPfwj_yS8CyQv6FHphCK_Asd4wtrU7E_VotQm8nFj0mm2dWkvSSqiCG3fNFoiIoaR9DCZ-I-GGzvUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbQqC3y--tu8ufmFiswRJh2KPTL2LDT-dT2xyX9ivP68MUkdqE0yQQGNhKPWwZAXS9STSpA32-B-KwEc4xaY7GR-t503B732IlzdJslvTU2T7uwj0bN_O-xdBz6P7d8A_Mejeiyt1bBuSPbDG5VWz7Oodkhv5TKyjcQnMV03Mm3hLFpMqOCQigCCpA3j9Oh2Nsrk8cur5TyTvJJFOS0Ewi-jqPcG6fwVKrBESuxQZqjnaWBrBvuCS9MUYiHwNx0QIbn0hg4YINcRAFveK8G3WxZ6rmzlXB32CMPphoktKgx3rUcmGFWb9P4x5ZsiSNryHOC2_cQdCbdwrtssb59jXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sc1rn8_0DdNqi1BtUYVt2l_ekSZXVXt9Q7jba2LaTNxY9GdIZzopAZXxS2JEYLU1iPTuM03xyGOqe6Opsn1cAn4HH0b0bX9j1FFl2srpdJBalIwIZ8KNnnu6qAj6LJSlHJicwI2zWLWwXnQVZ7MdY0TUoe81yNdSa5ROT7nLiUUDdTwLsHc3a7DNchkaZgPnQ7mTLagIErvfFYy_6N2wpWbNPXbHkmo6g_wzc5Jrjf9AHjXMWkTidDvoKrNxsi2jxluu2j4A1AivZHJRKE91cMOG-pgFlyY_eS5HVbMWkbrrr1t4885K3dnVbYiK_dWvOjZ5JIdll2uSBZZtGgWZjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwqbJf95llWj9Tofq7V1OfRC5mf5G9pGbUrMyEONi31E6NLL-4ntLFSnoSrtg02VX6OVxvFLyqJE8_ZY7y4fin_qLNagV05IPmtyr9JjsUqeWaklOMAg5hZ6rEylgKSS8_N5r9-U2UBuWa1Qc_ClcaYP0uuUd77znB5aZsXRGVYu63c0N9gcUiMM7QQmixVaShkuugRnhfcDcpX3jaEhl-IX1m6Jbx_5iteg8BhXUCm5cjA4tYVspuNfzWbTpRFjUg2o3wU1uZMDPEQr-bXbk_7SlHLZ58RfnTaK9Z5O3JtjssLtVCLHnBizJBFvlSjJRHRh3qZJ1FF1T1yHaZ-hfA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=fRtgCoEviCITXDFnRcmTbv0rtPUwdU6nuDejkjUAxivIbMusKMAr7NWSqUFarrwBdN7iOj_TSDmtHonZCmKlVXVIGQGlsMvgeRC62-GplOjjFwN--RK74XKnWldkpitKAKifRZHpgO03FME4hoNvgu0AZ2S9qGGL93teO7isNBX1-6vA0OyRQdcvW3kkDGuabM92DPw97pQnEj_zirz47PIW1Nz50JnWfDk0cFxE7uyT554b7Dsfak6906SXB0zCV3EFFSIdWUbEkAT8a45YfOQKImgLNARNZkC1jsHIcY7Hfk6Ty5_h5_xyIU7BoK4zDmul1XRYoa2vUZ24YVPwNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=fRtgCoEviCITXDFnRcmTbv0rtPUwdU6nuDejkjUAxivIbMusKMAr7NWSqUFarrwBdN7iOj_TSDmtHonZCmKlVXVIGQGlsMvgeRC62-GplOjjFwN--RK74XKnWldkpitKAKifRZHpgO03FME4hoNvgu0AZ2S9qGGL93teO7isNBX1-6vA0OyRQdcvW3kkDGuabM92DPw97pQnEj_zirz47PIW1Nz50JnWfDk0cFxE7uyT554b7Dsfak6906SXB0zCV3EFFSIdWUbEkAT8a45YfOQKImgLNARNZkC1jsHIcY7Hfk6Ty5_h5_xyIU7BoK4zDmul1XRYoa2vUZ24YVPwNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB_bxsHnjfOkHac8KBeoRt7fwvamFCG70kZhHZ6wJLg3QvvcVpXkeuFHzgBdswB_cH2eZaF-ZzucKv9Fn9XQ62jk_PlywOMWHc_8tLNZ4iedNijB4suz6ie0GukMsnhq5WEFkzxy9behqFjUscMhFJ0I-R8NMVhMAJVr3nEPr1vVV2MgZkDHThaSDvCFeKxk2K4JJDJswUZQGg-ISmcw1WiyP70xj8_wEMRJSZ3EHtu_E_F3gXC2jGXnMA7x6WwB-0dyqIdCeYy98HFG_50Jk8cB5I_zIzwst00gRJHp6kJSbi_DOb_EWxA3rhPaNWRibAE-Qaa0PHa2z1Rt6P3b5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GumkT34RSn2ffwe633MRnMIOAbw40__GCnoZuxWupxqwBydgmLvjVJXwspZeS8nlVmleJOZqNV6plfM4xQ7iXTlE3jref4L6RGVg5vpj38fSZ9gyDaot1g_VWWHMYKQK00aI087wTFZuHrq-AfxZgCtmHoV_MKTDdFYxwkp9dYITK7cToEBuJkxpjufJm6rsZWNAuBWFu59NOsqmzNnkHtXk8bwH0ax22RozU428zJslkhEdoF1Y4XgxHeDm5LizU9S51mXKM5sjIakMtdcZUkZkjmh64qy4Ac9cucEUc9x0DC8iHY5C8eQtcRnZQV8Egdc6xsck9q2zTvZdSrXVLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwuJP7C0t_mnICSyk0h5ncVH9cHIjoKTnrmFSFB8lry2x9Q5Zf8dy2ubjzNER5lB3Bu3ItO6mdqB9rth70qm1WfzpLrb4ap09iwhG9fgLiN-G7tHubbkw-8EuFCcoYW7IZzg2tp0xisHvuAezOZ5kX7I4DqGSbD6fF3OFa_2G9m05mGyhOhjKxO7MwCSYRa2oy74qZG5luyYyv99yrolUjXJTjXSoNJR_QulRofx7qUBBSUXkgiy3yvjNEf9C_Xt5szbQX-T2LTHBOgio9mpcvyiYm7kdC45GefKyXvy2I1jEdqV2dwxBLdc-w_DSFh4de5JRWAMI8BihSPdFNH76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fC8phojvpIFwanezaTEGjSV7z4kbuDtQul5fbrLNKt_EO3MWGrKwHm0XGHbu1rUwLgqvHOqR11ezw7VaBCyped7lUw_vJmkCQNrtA1zm7cLZEaT-jIC-ix8i7ipb-hXx9KRAmpfMj6JPFelIJt7wmv7Lwdsyc8fPOBfYMRIV4Bkva4Jnk7e6mcvazSkG5nByDUEtLsh3E6wde7gUaJpgaryhey9JMeKD6gf758Xn0Z7Y1lqCwLgXaJ97_15NuZsYCYXtPKeZJx5bkt_F6V1uomfuujBlQd7bR8W97OqZyBqlAbQnj-dvWfyA3JKx1avbf9nPwpx5y2PdZrGKr5uwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om8uDhIAC49scUDfol1UKBzCzQrM80gIhl9Ti3G8dYWsQS-NAOFyfu4vzbKjM5f0NV_F25n5aROmVgfNZFxku9oI_afgPmUQf5wSjXXpwzPvgGV9kccQUWH_eRaXi7j_JjDjOFqcyKmKQWHpGj3un5eFxXdbsE2decPVuaLZ9pJ6cDycwrf6HmJ7fVWWmHrNE_G_eTd-lCifFOi-vaGq3IbJwSqhKN0mUqNeyp7DQTemPtGYTNEJ102pFMigacD0llYq7OieEKm4z-RtU0mhKJHS9HBV1xDSTxdfTCANkW1HZc5CELJ3LyXGRI9k9zDL_5riNlvqjXqoWrpM9ZLUAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvJmNFrrOM_tu0g6izSmIBGpWYTJNk9I0YpL_EoyifNivwqUKK13Vwbcv3xkRBHPQj3XFPMkvo_kHOl3db383JxgDEjDpBjwlRclbKN21aZrSI2MmeFRYFsQVFTsXQoN2tSFfvgxkpHb7IKYCLrpZ9PCan-AXsQTNugbr0cfPwx48qGVEGDUfGOwKGzQxvj6s8SxItQcr6rS48g1Bky4MwEcEcKgKyBwK53UPkF6VbIvRakT8QBugyVZOoXMGcydouivuRjQU9FhCptHIYGh1bGP9pYOn6ks2VGyLWu7Skq-MFHc7Eqn0y2a_CHpsXR1wEKB4tNSv3nay58x3BkK_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmbLhOY4XEWKAbwhEJYlNICsHuokUiA9krerhh83pS3WWxaklf6rXf4vMlZ9RTjPEv56oDLQDCTnmQdCFMX8XJldbUzJ-2fUG2QFAm4l-dbnsXCaluFZUwshk1u4CHhrBbEuAI5UeCOXWkBL1Xhqp0HYRu1PHxLITEhrxSQKq3srwDyaUkUw7bGOquZQv7qzzfhl2FrhgdKVOAfR-D8gH0mv5NT1CRfS5pk8TDbnL3K2y0lYk1Ai74h0GVh-H4gMY-kr4KcwoHZ3xTSgL2rtmoNmoiBprp6Eeq1lpjCT52IANdXdb8ii9oA9N3XbevFwCM5NxyHxC2odH3_JpdabaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3J9qyXB9Uuru35-37ycnTSlCLvC5rVN6r9uA_ocseZVXczT0YDF3o3Ax-2HRMzKxQKx-klvF4SC2a2bOuSSc06jxmqD06bZBs-3qoYbwJDQlv2vIFKmeBXFECO2A7SQ70WNMHt0iWBnYZ5NfpIeRouKuM-97-GUqUtqUb8WlSfGa6Dbq9SG6UnV9H7aYld4qFueai47mYm3mH0Loov4AAaM5uYvgg5taxvFiPNK_d_rkF-D5THnNclWlP7elbhktXtk43D1PKIKYbu4hmVE2VLW-nVozdTsFwimpAESdLJltwo9qpUPyTe6MNEh73NkSfZCG9Zzezlo3MFwTPYuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgGJW3gWyS-LA2sOJ5zCzxBgydd-dZrbZii8OQghp571G-7cjQvdPbfjy4yPQ_XplfsPYQRaBSIgckzJIyrcv8p3QA5-mx3HuI1kxXLxh7cAl5hf9OBB-44NU2Z47V3_2GstX1lDrvwNscABUqhgfiQhl4GyiS-OqAtd2Pe11rvn6wAmDyS4WoSecxdruzb_j1jn_NNM8ER253iORt4uYVCXLID_tySOhf2LEpEwfhAnXwqdrtp3F1uQMTZSYQ4fWNuDTJemZLVNkdan3kDwyMKKPEygKHK78y55Rpo0SFt8fnRqonrXVJwviR_f-ogJGpI5p0BLW0jk5WBXfSrqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu3Xyy5tjXQWTrEHdy1LFXZdzlYhTU5ne_GSxD40WuU0GibpAKlXG0QVqyFVeEBeJX4r-ZIFoLgpAiI-1tdIPiIt00Xv__X7OIKTrL_3nGO0OONnKV4SJ1cJjXqhe9TSLX5DrYWUskRG-pnauDRr_wDY7nkh4pVLZigTKvzo6V-SxvN0T9IoCpGehqCOgOZe1at234x5zwZblF8CAErt3P3NDOPJKh9WNKN9Ze-zBHY-Z4tgXvd_9DBDFcYPlwIbszUemfbucYk8giw5Mpt3-zJJXbRI_sQm5QUEbLuAa3bAMKQu3Lu3LvMiPLM0Gza4UKST7jj5MraTpa9ETc4GJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNdVLAVCZMlXNS8phMp_Naw8b5TUAVSO5W9Cv8u8ca4PM_zKtcdpieeft_tSZgmax22bJYInB26phyz8U8X61cshdR5UhzQmMMh_fhGL8n9IYGD12ZZlP5vlw2HLtIwEyuegR79BSQaKjwx9AoFgFAXNM_oVDZHNPyiAorffcAgufMXC7yYWkK1wVSPno_XWgVeLR7Upmd9Chrx292dQHdj5li39WO9SFI0wFLNJ2A16Yd-SkCCCQFNFN9a6zdZaWuV-OzoyXDAV_7e9cKo-hoS93Gl-twYxNJ5_qfcWNeY2VKsbZgWKRI94oUvKwuGvU1YIkoAAyXccK_yrOpWIrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFY8EZPmhLkmjQUxAlEcC4EU-O1f9jSQo-cIXESLnVqSbtWxI1XMfnUTf19t6i0wytLOiEhGKqkB4Hy_oMNFUmkZ2j06WCz-pciI3SKD2m8GrWOFdE-qs0Hfx-2iWie7p07Jiu4ovXf-BshBPxe3uGsGjG0T3FmptYSneEOjMynl18lfl1f9fbS01iUj0UoykVxsU03eoiHFiuiOBsfMfZZonV0Xe3gn7O74lsv8tLiy29L7wZHOn7XnC_c3lWdxDohdS02uDshG9ZTn2EWVCp0-JTPPpHc_Vp6KzYk4X86TdAh7GRClpeF8CL3bCGrG5_0UJJV1uueqST0QDb4-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIXBoErLsmyuIZKQgDDJxzHwVhGcLlBR6qN1in1ZaodgoYR0eu9cWlUMkPdPLh0ZPgg88Pmz-CanU7WN_nHDe6PGdDQYR2ce5VeL9G1Tq260qHKNo5z-61e23YTlwvymg-T6yz40MGVVuHv-dqGx3QVuS_LI328YUimd07b7-E8Nbq-a8aYAkC0jyr_m4bt3_9TS2nDHzj1forMpEaVpdMSnmUPPRUjOcxTjmSsnVXU72vPoSkCmGg5SQdMCekO5zjthCTbgHFNSVWlbJK1Bex4XP88cf6kbtp_P8akEHbj5by16rZS8I0mFehAb8N5NerVjCjtpICLaV-olJkDzhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=KZ1m7jG77sbWF0ROnZPa2mhZv43tkDSII-0tHnIpJ6iec9v6VJk1uE2kQwfFd2imYycD607B6R7pZxnSeSNzpCzG3hQvMmU5TSAGETFi2B0-l-6J2izLS1Q6VxpDTTj12nFo6wE3SNA5AW-YAum60-TId9POJ1D1pp_VhTvjNr2laXyVbqlqZmvXgP5m4j0G6ZkaObQXDYQPDY_rwwUBhi_I1RLNadPrlJ00Y3jmO3coPu5SuurRAnMVg_58Kf-3xNzc1xIxqBH453eM0P6OyaFGldeZ3XvEzDAxDT0ZMGNUP6Q5e7RIo0GSs_BrFYcJacveureHJPKxZlQ0QysoXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=KZ1m7jG77sbWF0ROnZPa2mhZv43tkDSII-0tHnIpJ6iec9v6VJk1uE2kQwfFd2imYycD607B6R7pZxnSeSNzpCzG3hQvMmU5TSAGETFi2B0-l-6J2izLS1Q6VxpDTTj12nFo6wE3SNA5AW-YAum60-TId9POJ1D1pp_VhTvjNr2laXyVbqlqZmvXgP5m4j0G6ZkaObQXDYQPDY_rwwUBhi_I1RLNadPrlJ00Y3jmO3coPu5SuurRAnMVg_58Kf-3xNzc1xIxqBH453eM0P6OyaFGldeZ3XvEzDAxDT0ZMGNUP6Q5e7RIo0GSs_BrFYcJacveureHJPKxZlQ0QysoXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdcy9zFvsKnyIsSzZ7mBLCxKtmA7YuZiC3MxIl0Rk8h_yFoUQH13HvJVcClC3gVDnMIWwcDHq9HsZjJsmoujNSzZEnouaGOtV-20sYGfyEzOzJzXqLXJ-3cXPhAf1rYpQWbudjodAKHLcwyMCCtvCSUBUMoQMJAVEP3CbC0_QRrLGgA1uRVr3aMqNecaB1_BtP6Upvm84BqUGHJ9q1V0RVkMJZru7okzLc-s38pODXJNdDQiazBCrw2Puti5ErV9-F7X18pE7MjvThIcmFx-pLC6eyN5pd8_r_Kv_UeDXvVgIpiLCY_IJdG2mCRayAMDmo5eJJRzfdjtB9cWjTZ9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8zsPEyaqqD3fk215bC8t6i6KeQJq-77pR6J7N7zeS4CR2seD3m28gpGR31fiMzh3kqTCtText_dUKauQ-RpZBKG5W_Wm6de-uPusZ-HOvSfFe5IomRRj8NTeGVf3TThQH5fwybcliQ66im-DnseQW7Dl93vPgMkBImFm6Gh-8gx6xcQO2Gad8kpRiSbh-AcRzQzJr-YglAMP8Rf3i4zeeHoHfcIiPZ-RkbbWNnTpa8eyJWJ_WSZ-daK9eK05_IRXMwZmSC-7mNOk5qw8SrffDaMrhE2OrxNEUfcPpHciweeraON1KO-qPB-_Btbw5TW4_E7YiGdcB487oL2ab2xXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fg6HrTUBcovI7rskEHSK339OuhSzKcCc7TJLWK3_TpEwQn0Z14ZLUo1B9lMlSnrwCEAXdWJDOHyXuk8MwoP-uAg_6udxnsQER8ceZLCmtMc5QaxcYpV2MFiZlOkFHlPkoX-oHeBPf6SMYlO5JxsCLNR9x2nBA3OikQWhngZwbx2uUe8itfYI-vsIAsO5BdtzjniraLGVO938QDZoNca46wLjNrPEM02EjpuV_v8zYbd8SCPq4BKZKg2dCURqJqDP-4HfeSxY0K4ni3xxCZNPC67cs__OB_zD5tFy7pkMi-V_zirn8HH1KbCAnm4MiEkhGIRM6x1IUdjAyYBpVPKNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KriGA7vy5R-tVRedtuxI6WCKdq2RAJt8D5euEbfEO-APN0av6Go5rZ4NxB4g7N7rvdErPQxetD9FNosc2v2LtiXJ7IDLZB4emt6nkTBE6vTIZpU7usyFou43NmHgKlYBlgJb10AKObBJL6V9lRXHQA0TS3BlELr3AVut6PKr19M-VQgfSV0FFKooFTimnk4PKGJhtre7wUtAmkwHf-bj-J_PU7KKy5ROKbCatRKTVbZSMn4AuTcR9nU8OTArTghLbNUC1gJHrnEni-jej7sYL73bxBQKL2sIqtH-kGS19cNnWCRgwx1-oRUHcrGp67i4rs8plvRfMmho3lQolg8oyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHpv7pMP62M8AKB8zj3sj8XotSkXe6O2Hu4xxLL49qI6C5za4mVd6bswz2oyBgHcfuxm8Q_-S3huQqARedYc2YYOGkO11dQ3X2xOaGkNmgUbRzICOpW4AmuXoUp7J6RTXHmukrVk6hnngKkNgeewu-lpd6VfePHWSw9N5bXUAFjoUbgWlnxPYUXUbSfu4wUrZazOQE90WPKiNrTSLfhhH3_xEkpIgr2Iv1R3W_ebLJrQFTu66RTdQFe57vnKUabViBh3I21uQNxRTI69mrG172Il42iv7ao6zbUSfs_x65gRtw42OF6gosIIGW9A7pSykimya3Id7clyfBs_Sp0l0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZH5AfQx37UsmUu7lnC-02qzqOB2F7TBzNaPYo2K9djgihymUVHUict6igmTzFnCYsrHVb8VZcB4HsGLjv14KsWGV1lxpF6sGdRr_2Pr0Cpp78yM6Y679y9fEXfkR7xcLVipC7POztBNh3sFAz0VlSaUH2-7eNFnde-pMxiEtySDkvE7T3nyN2OJQJidzKIOR7MMsNSISRVXlPGc-alpGGgZXOuRoRSe6DMEgsEebLndhiB4H6koGby49hrzGPxf02XCc4eMDHLwBycdT39FKO4j0jtk-Kn5-Pq9o5qfYAa9UKtChnwEf8voYfqILVg_acm7LxIE6RHV2el_j8FNqYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gamAet-L3ouUbJyyi_F4ymjMkNYFmwWe212KXNaHA0ui8rQswSFVixOa7ThbuWdE2w6RAjKu47Cq49oGla5UMeAF82pHn6NU6Kjr3WjYALIGWjvY9-1pc1-nuWCve-3zzdFs3aaW8cf_-LLI668JWqTeUmpMa1PUi0xsPRJ3tFgvvSdZhaKGe2JCAzsoSV_xq_oo6HD_vAn942Giv2-3lOT0Pctl1QTSsP4rGZ9KnZ8qzWVr3aytQtbLVCzAcZxK4PVIcgRkm6vhfc80SH2qdLznBgr-SopMqt_Ol-pPp2SgIOU97Mjw26r3p2dCaP4ObCll6fU82S4gm-XLVJ6mqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNC5yw1iwZPuozOaYSSV65YNbec1Rx1ijpBOHKOmsKVbKHrtIvWJ0XFdqPe19-SVWDVTrIRDL9l43gQc3G2Kw2u3cPTPete-2b-GBjFECzxS4Xzvzj2dKVpi4SO1-X2Hip91M6YySP4u9wUHf6FtkIxh6rqcyAvTfeDIcCH4vdq29vxbZ9O7Qao50BHfqZ2OBS3PqrOOMsMzieK2DiElDmhOflklJGqjhhYFbhn4iG9Vu9kNl4_W6tUVpWHQUJqJXiHTGSL2gEm3u_XcODJ7W6sSbOxOnXmVM68_glm7mCBmhp9kYARV15xXEVsIvESEDB0JomqQCAkUG9xrn9h9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
