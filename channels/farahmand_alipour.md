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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 18:30:12</div>
<hr>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqpYtXr54RW4RV9sWQsqxRf9YfEAgSwWx_lbPmHUzndkMXB44VYMWZQVMkAKJeBxD1Bc9Lhk0vf0nATb4Uuh2VeVwrrM2OAmiJgh0WtbM9Rk50V12TTW8AmoB0fwPPzkNePIU-FV89Bg_2SiU9sSM8m3rNr_qq2nrato8D13vLIlNLalW09A87APJhA9gdLt7pp2MuT_WeslJv_8Cg8RP1y4GxPCkNuixNeCWIiEHbL_fcYPfMmEm6nXhv6U7NS0BPoXVirmrWi-GteNMZx0AOZUfwc1eCbgF1EEhvFDlwDck89x4dcFlw9Zh9qJtVGl2nh5cD4fB5QVrJkFM5KcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMg5GeC7LmHvPMKHD7YxCLaDcNo7b9thX-MU_nKpp7eay8jBzZRHQAOmyrfhp243_OP4rR8Pf_iqBNclKnTpRdvO3rjGEeQryrr1mtMTSZko1e0hS3K1N13eP8aTzoHQfVKGO2Jj2z_gI9iu-94vrrjjzcoFuDzZafzk4md9sg39Eg2Je8FB8AtpNDLkCDNBYg-lL0V_o2-DaBbk9zGOvOUL9EVLFwV_PipXzQVqJXvUE8WKh7agdIyD8O0cERZbVL5QqFJxfHlUyaaBqc-43dDlXgfrRkUjNz-_sWRhNR_XOc1WSLVgmJVLWTbsLEPVG0-i20dXsDsNXb02HXns9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0ry2yDNiPv0HK9VjVN16-9ch7habE0-j_qGGUXnSLuHsYDmgMFO-ImenA1Opj95gi0Lwt3xZVVYn54C04ZKDS8kF_dRfK00_h3NqfHasVFMSkvhZxi6yrVg9TMo1QJHw7CU5VXifyZdE4TquW6sohmO37D5wkxjBMsaoiormYWTnH73LrXcCWhEuR4FtvO3ndLMYazUlk6bENimBQ13JC05ZJwtKn3ZH0vCgW0Iw615-4JsU4M09JWQUmS8oTXhm9h8wE9C5P2VfAn3GjAvaLMz0jdEfSTsY74jDKDrF9N8e6ixvoDr2jRHCp1xrrNGnyAT1qsHmWgnmLLQ5ibdYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlnVzBIQgXIkYtcbZ6qUtWk7_iokG2H_rnHmojnaVsAwEo6gUeDF0_gvMngFePIncZXk61TbmAMx_UZoRs6mkD1IsuZ7UW06b2QwLalz8mPXMKzw7uJxclRIH44X2iPpORCygyMC7vupJnkmFsns8ILDAH-0vzgxW_aN-2dqgFdQH5zX48ouBCLMSHrSoGfll_0ERKeGX__QpFqqaOOkxy6krjX3_Wo1cOOX1J7nWbuyHPwRXFqzc95Lh6j2KioRLYCLbSkvHH4OQJ3OqrnG3oY0Rvfc5kIrq_RpJz6x0T63l84B5BLPrAdxYuSEpPm4tdwNd0TGvsuIv5WnBEUfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=LflsC3QuXxsvG1hWqeutYxbA0hwuL-e4GNgFcmYYapPpY3IqMSogN_4bEt6hf_CHMZQbY6wYK_xVbLnl-qz9v9LJZjzeqFG6FVDGwPrkzXOzbisRINK-6tpmnYGO358RWoo4DS-qLgb3W74QmbgFd-OnxG_qt3b5qDdulf_DoY2v8aHviXD8v_DjfVaohvp3d8OwNgy4hfqggu9lv7gromCB9jyTLjhAuVUhA4t0aG2ey8XawbtUT7Kg1FIrM14GXHa2pHTn4wAi-3zyBD8jkkDc5kxZ-syEd8A2fyO9j4DhXKhPBHSd9pIl1g5qh0fbRaxW137y0VvKApNmv426eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=LflsC3QuXxsvG1hWqeutYxbA0hwuL-e4GNgFcmYYapPpY3IqMSogN_4bEt6hf_CHMZQbY6wYK_xVbLnl-qz9v9LJZjzeqFG6FVDGwPrkzXOzbisRINK-6tpmnYGO358RWoo4DS-qLgb3W74QmbgFd-OnxG_qt3b5qDdulf_DoY2v8aHviXD8v_DjfVaohvp3d8OwNgy4hfqggu9lv7gromCB9jyTLjhAuVUhA4t0aG2ey8XawbtUT7Kg1FIrM14GXHa2pHTn4wAi-3zyBD8jkkDc5kxZ-syEd8A2fyO9j4DhXKhPBHSd9pIl1g5qh0fbRaxW137y0VvKApNmv426eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=CHAI_XN8UG9Yo1TC_nVi1ifZ2oiR8WAq6gX1KfpPYbqpjTzHQMSYI9J757GrzXG8IldeJhhtJPMvD5BUuPAddcOG9W8imhpPLJiC_dKQqZnuiRDANvMHLW5zqzcAfSjL9_Ev5wfzAxU5pvFjUduJJCrHsJuxUS6Sp-ZKkgO3ifBGAtA63yCpgV_7NaghLwoHDKKwGjAZi79_EajydTWlsKCq0YlRSY83GhYQWT6BgciDsg_eCyoEeBR62mejklHTwqxt4DKz8TNQRr-l9pBqcczswm9cAu74v0Mjk4cXW3VagIwRFyhtYSjyau5HubSMWx6UeyZNnsMpF0J4K_2p5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=CHAI_XN8UG9Yo1TC_nVi1ifZ2oiR8WAq6gX1KfpPYbqpjTzHQMSYI9J757GrzXG8IldeJhhtJPMvD5BUuPAddcOG9W8imhpPLJiC_dKQqZnuiRDANvMHLW5zqzcAfSjL9_Ev5wfzAxU5pvFjUduJJCrHsJuxUS6Sp-ZKkgO3ifBGAtA63yCpgV_7NaghLwoHDKKwGjAZi79_EajydTWlsKCq0YlRSY83GhYQWT6BgciDsg_eCyoEeBR62mejklHTwqxt4DKz8TNQRr-l9pBqcczswm9cAu74v0Mjk4cXW3VagIwRFyhtYSjyau5HubSMWx6UeyZNnsMpF0J4K_2p5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooXPqvI1q8taXawnq1FN12dPEqhZLLLOH9FdAjS2xz6YfW1_72kw3Bmovod5L7KuwOrYv1pcK-jlY1NWC6-5KEhcwsvf5RJG9Llsk3Trkpg5z9X_u1uaEBmhFUcfo_qKjSNff4TwDiE_ljzgxlz1EAI2IB38wkBmIm8R3QFqsvhwCf58Wft2k9g8hXTXSqTymsQvwO3z0eOk6-i8axkcMcG0nadoNFF4SAfxi3nY9LvBpSxtZzdZ5aHVNwoIEkaKs2e7L9uWwtD9jgqg185fQcBi64msUvdXLwtuJgxSHg_M92R9OO9gF_ibn2wkLqZ6giqoGLgUvjS8-wPYgkvcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I88TDluoWKwiUuR2oHQzQlFCKjr-DYs3rOcike2mEBA5LiMjJC80gnXPp6i6uQ2zsWduimUko3DNu3oMLhGG4b9_mf5kVKT8ATesr04CLTq9cxAaTNtoYFyOe8MTIPWeicgn1qF8F6R5X1NWOL_-Bsn_hufluqaUpXOXKD-A4AP_CHD95WrjHI5g_gxtYvFQUgBhaA-guZPSfb18T2SW1Y0j1Y8Af-SbZBI9vPCKqLHFvuVhSiumjd_tiaK1Wum8Tq6YSoE0mBi0o7DNzJ9ujtNH2Kn1KWBbygkEUElF6cDkSe5zsBMs9ztoFrYCLEuKyjcnQLlEInXGLxg4WoCdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ag5AnBTa3wLsB0v4nUUCLa4sHMyElS5lLfSk8bjhPiN6YHY0NL3IEFZkNHnp4W0Ltb66VnAmwAmrMw8YLOIAWZDADRBW7aHERx0FuRG6ztRLfNwLKjAL_Bv-le4RtmFjjezOo_KQu-yGorf4GCVCVlpTr1G974sYrZy2OM1yPmAi38lXSgnNGTubx1YpxE_FtHvNiRgyPaawHVDxE1b_3y8TaJ1d5IpjDri5x_JHmEINRR49ZavC-XWXK-N4j2huz9wVs3HmdgjRCQIsY7tguNnW6DKDTzxQkceipiqZVGBi00jcp-r4teVTUvTLKmt7WWnxuCAaH1SHJ7DIy4X9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrNylVhmU0T00Cefng5JKzc5v3F1JVr3EapJOxkBglAQU9uwTmBv8xXD0FyngttKISh4HFrpVDKZ8RTDVr81tBcpm_83QPnH9vQg0Nf-W-pp094nT398UYEGi8Btu9BEWUundUG2zJinI8QtbdUmmfl8nQ8NUlpsCYV7Fmwi7gabyFtU9rBqfl8pLb9AAVtosO8uK8pchuZVjQ0-qFbhMhKzwQxxNyVJBg7n94bwBAMu0EiwzG7aKJc0Fsj0MIAFKG6wC4AaAoFj9I_aWh-0cQS7sRyuvuSfIq0bAsxTyyGDVjW8xWooTPuvatD8fxj4csekIi-CeFzxPKz42kz6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAPeiA16gV8HKpjSKuBFv7k8B_bOAvNqTXONPMnfzjOuTAHLJot4iQhT-km6CB_pmqWFkhWIks0s5ZbLxHeJFndkSPJnoRAEdpxw60suBZFA4FA8PE1epeXvGGunkh1ZzDP8movryfEU9yTZPKlIBUAemw-3BhPhWsXbkSdWR0vaokKRN8UpG5rXYyo6HjQng1Np6WVeKfYNxnbSbAnP7nunGlhTOWVfkZ8RgC4uKj0snmsBqI7C7RawRBK-xgAJIxOWoQjCSQvAuGswSgAQJMiwGYxUi2inSAXBnrytEdNpyy7Eb91daWUuSmImAgvrDMbhT6g3BuwyZrekAaaqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rLUSqCBJYtYU6W_xaUygf3_JtXJQYDQB2fS8zQNFRpnkfYh3p28bMzGP_ye7fCmBpVj9kGVEfd6Litus9-87-diZf81dapiOegstn_xEPrsJ2gKjKSCH1DbkAX4kFOUCdmt609-6E_0d1E2LyCy0dGcGN_aF7OjR1zYICSWFHPuRoqPNdVdICAxtP-9aZ9nXsU0Gj4L70p-BRULSgHGjPwLLhcFdb8via6ZJz5Hl5rc-ZQjU4bv6YN9zLWUwb3S1Smo0qbSyOkrZL3VeYqIsoNC27VeZ66oUP3NtcdMwvftjM0a2mi6P8iqi8Zbfx8A8a4EI9TPFZMoxVOhRh8x_7gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rLUSqCBJYtYU6W_xaUygf3_JtXJQYDQB2fS8zQNFRpnkfYh3p28bMzGP_ye7fCmBpVj9kGVEfd6Litus9-87-diZf81dapiOegstn_xEPrsJ2gKjKSCH1DbkAX4kFOUCdmt609-6E_0d1E2LyCy0dGcGN_aF7OjR1zYICSWFHPuRoqPNdVdICAxtP-9aZ9nXsU0Gj4L70p-BRULSgHGjPwLLhcFdb8via6ZJz5Hl5rc-ZQjU4bv6YN9zLWUwb3S1Smo0qbSyOkrZL3VeYqIsoNC27VeZ66oUP3NtcdMwvftjM0a2mi6P8iqi8Zbfx8A8a4EI9TPFZMoxVOhRh8x_7gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2KT8nWSCO3WPOVpUxjf4WaJDO4EPLc3UtWbylbKa05hpnEOjEPJPj2VUoND7jaHzoSsU1aVHIWkbkLRYuGUEstXdwsjwFExn4qbqbT6GtcspePwvAh3gXIhBhTJb9jsQNUGsllP_eiGNSaLc_5b5sYumucTaKPsV8Xigh9D3um5cHG4zcH5NBpEh0vOP6FfMrSXPxEWXtWJZYU8OIJ-J5uMReJuGHtw5l90MgQL1l37Fm7FRUZr8o0Gee78ETI8iGYXBt3z00JbsLW8vt9A-8tn0BfT_jAQnyn65DFz_3F-kFCQFRnSYh8PwDv2EF3nCeEu82_Oym9E59_hoo1bbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4kGmoQIBR1RtPgoRKLRGejXxGJdqJCV5tBjXmXy_FTCDOQs_J0A3-TEJNuf41ZLxa0nxCsdYHvoOqU5yolw23bkvdcDfsiGFJW41b5aXw8sO65PJt5zCghD-3CZ1wpnFGjoauQkLuPm1O8sWOKa9lNQM1lHonzbdd0Srb3UGM7smiiNeLGKn_sG05QuP335jHfhku9Irn7QWrd9DOa2VDJTYCua8T_XfZD_S8DI162IRU28ZkxuzRBHYY_cWOA1hn-T9Yo4URDSCbZewrUl9GXvOVAdHx5pxnQIE-re7dTVdyQwbZHznDcq9W3v_6WSfQpxzZ8llVU4HnGwQTuD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exl0UjI6bPunkVfzaoNOMZMUs804mMaxoydJ-_h7PQ8ZbBm33NgGfjUJZEaCJeqU04trYc0LPudQ0xw0l9IIuepP-CeEf3TVA1vfd2nM5LAUsi2kGJJILHbmZXH7HxYbWybfKV-tGrs8GBYt-KcrmP29wEbdGyxw4796lC76dkhQBTCzIjm_R12EMS3UcTf-7quUO5rBaWSAcr854VOTCdueX3Mjx65bvDftftEJBB--kRlylRLBkIDo4bvMtMlC1ZdDb0x4HAPF_ogNsBfnkpTgVhw6uFoyR4pWkrhFCtYuFgYlbeaeyBvS4poDWyEzTibLlLRP5wtFFdSfM00hmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqGTJG5mzyfbu5bSsDRJrIrx3ZBhl1Bg_N9y-YwAtA06qcvzIF8wUctqGE62rCv_01BQsHKOtQqysyEvbwV5Ya385bNqOeBuLXiFAjThfncWoyeYKknAk7j9QzIovlCTFvikUmLmAlPNgMyrahyAUZMRixmb2NyD0NTux2M3RB--cRd2Z4qH8g2lW09dU6SBjna7feH48M8WEQz_Y6fC1kFwTNWVYuUJV4RuTs-_XF6HmiYxjk52OhDtsuBUhRmHxRcY892wzB2LHFZ68UKQ3iWnKlnFsUOlUH_ru25re--rzO3iUYRdQeLthfsK3goOGAyJ3qGFP4QhI6H-ijYJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXNivHUo0h-PD2ca6bi3_Ur--SnrlTHoZjXgAf96jIUxfW9mQKvjmXbOMtg6P9DLmMKhmmZiyfpZ40T5HngcN1t5x_7or-75_UzKiBis-c474SO8ypQHwhVx2Wv3tjzrsmigIjTkWOSXKKBkJ0TJttVOSGe1O5K2MzZzyMqPc3V4hQgJxMEIawFw5addm-DM4R3S5HanLGsn4L8d8CuSkZIBOXK-O0VhD3K2eI7B8nb7LJibJD30hrswO_z8_gQ6yG5ODBAjjGYYwhu_MpI7DAsg1kmAn7RBIaCI-TuTWJ8BauapJxilQzpoXIkHb0aWYu8uuLQ5-SFAssppVtrIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELCVL9-ohdoHlZpvwhtU_YpEo4u3Xkx_fb7qpfiJQW_-hjs2IzpxEiEog_EbZm_SSaUjB9s2ovN_3wtAKrK0sjL_RSaHNHDb-knYqK2p5djwOGA_IeYeJr_1PGG36NQsmLDZtJZC1CDCHeb2IDeQAx2SHksWMJ1cQbhcRQRhX6--T5Ny0R-A8rYVa09DAzeYasCKHNJtp3C9uOKdmvJAte2T4wtfOzrHZh_5eBoNJ9p_R3GAqltO8eoXYJbeFx077Z2wLeTb9id7ybS8swgBp0BcocDlDUVSExn6l1AQgUXQ1Wyu4rCQq1f4bFx8TUHSMALeQD4lQHUmIGSqn44qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBxay1PwcHYrfR6yhNCqimQvnSBQwkyCOosLpu6xn3X7IDVw8u5DPWVlDA9XMN-aukBmvMfkWoEm9lTnU55z-9speqNnytwPJJJMVqoxDVTz4LEjOsuZsB74jin8T0imxkYUFpjuC3eSDsVFONvKa32D_GVwgTRxCCbJEEytOeeA-9Q9u9HcpbTztoKT5JxGdqog2e8cxVS1tCnqyu5_fk8fi_rIAh3hjmfbQLwQgqcj1jc55MjmXyI_qIC_D1ixUK8Xp6xNzzkXDB-2kmcnIJxK2UagVnyz0rSNhIDbtB2Oz_Fu2VC93WqsosmL7oJzFzPP44QppioU5m7dnOw4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRqNPr_xX_VcxjnDUPh1zRo8m9ZHZDZK7VbiQK67yDa6kwO4vWH6I2Rl3Ruai7fYzSseE3G6gGLsm46BYfuA49eZcx0mfVpeCu8TSSe_GtDXL9oMZArOo9HRUYEUiN__-O_OH9wvytfYHeBBbQxOO12Sx1-Imc8ZL8WnzNfIWCUTLWpYphqdUhM7nMskmBmNB3T6qDBYJ2rJ81AbwHe0AYKHCSScTSwzUqPhmC3AK7TXi-e8oOkyYPbg9-7uDUBoz-0Q3SDMLzkTw9mOzBniYC4shkiHSnLk6FL9ZnB_Q9zgMlqCpjkTVTudsy3Ntgxa9yl47HB8NfrmfUSPHk9FNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb4qTulhP1oU7SMCjSNr1ZJx_dOuJSHM7aVHqct9FqaDQ4gRfyhzao2it27SWDO82vdJW1y-0K4c811MGU0rhUgIkr-r7X_EXYAziNRQhGa8_2ocsVLbNX_2xjHxBsknTuMNzd1124-G7OcxvOZzCYzGN1UWZEkaXZTOLcFvhAuujj1m7cFlgkAAmSDaUK9_qc6lsxSeSlhg2oxy6we1Op7MGst7FvbHzaD-0shM_aFroELezkh6cF5T_3QpYDwbZwPFRKPDOimpPZghFQny-dEfoSFEzig4ErqifcK-KomN9LTSFSeER-rebQcjeh8Qw9kd898d8SZRimQv-5q8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=QaRImqIUhV8wkZRetcd4fy7colhEf3zr8KxnGtw7m56pIaAmvsyXIJe5k-xZ9bSrmHFjXP2aYsBUZljUNGPEOOBiosE1CLeDGx8f88Fy_a2ik89orGVjEFm1owwAf9fm_FGn9-f1XwXlK9Q39ikM6fTUiwWBaofI_NHlaSKkZ2TApYgFUuCBu_ktd-hXtmuhSqJMlll_gZyti0gRPam3AlEYqduswLQ-O7eWkFD11sPZaU9wWr1Y9_RDcqxxWCQ44g0pLuL8sGxiJqExyA48o-TPDmEXUxlS6FU0t2x-BkvNCVMFeSxsPegb1m7Mnq2kAgwsznEVXqScAaA_5gT81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=QaRImqIUhV8wkZRetcd4fy7colhEf3zr8KxnGtw7m56pIaAmvsyXIJe5k-xZ9bSrmHFjXP2aYsBUZljUNGPEOOBiosE1CLeDGx8f88Fy_a2ik89orGVjEFm1owwAf9fm_FGn9-f1XwXlK9Q39ikM6fTUiwWBaofI_NHlaSKkZ2TApYgFUuCBu_ktd-hXtmuhSqJMlll_gZyti0gRPam3AlEYqduswLQ-O7eWkFD11sPZaU9wWr1Y9_RDcqxxWCQ44g0pLuL8sGxiJqExyA48o-TPDmEXUxlS6FU0t2x-BkvNCVMFeSxsPegb1m7Mnq2kAgwsznEVXqScAaA_5gT81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsGuzOaFTZkpBkgrcFDmctzO60aM3oTypi6paJDtr-g50P5BwSDkLuWqrs1gH5-EgwkKtSkvyM50dxC2OlNG0OVgNlH-DECkW8qUBcT1PNSkI51Mh_9f23W9EFlETFfe4QmBO--IGhjLVb3VULY51IZ8dtntVacqZlBJBe2JggD0ZstzfmxbqKSIY2myib2ijT_H6FXvu7diyr8jlauItcepexuBwj5lTe3RujtbgDGHpw9gqk0inb0bwh1YyHezkdq26YdElEB4LX63sIiVjUDYG1nzBHRfKitOEDgy6jftivCcub9bfG2vXJK-Au7zYFURsrp3jYITxVT7B_a6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsymsweEmWusl4pvP12NAbiA2CZ8xQSX8LzUWubW1t_VrjI1VXjFWHEACroNMc5bAdx0x0LR7JhKiBsrnIFTWs557dIAFb7TwN_s2yYBLjhzy7fNYcDzYNUXGJktEP2I-Zi5wQxPLyjOwJQ9yJ1Kx04Qgzc65dY7r1Un1Wm27-m_IA6X5j9q9oVw_GXKPPH_7NNIZwgkKd8k3l9cI1y3nVLK4Xk-L_HrrIDQhJ1FYZVjnZMxi1fkNdXyG1vlejumHbtdLiwqodeWZAGXPXLWt68Ds6xV9dyp0RmuHQq6DF4xExZFoVi_dOoz-1QKi2RMZYv9f2y5Soka_fsu9YwPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFY_dbr8kImxEvDeJgrFerF3VCAjJWCkh6Pc8c6hHV7LW3EsbeC13cbjt1Y_NVcrGiNWJeAu5iIjX2jo1vJiERLAZHC0e5Xdm1xjF9iveE3TxDUuUo9o_RVULyi06aSlCo1_rrO2O8_HzxiKdQvbjvatBPRKWgBqjJER08D9NH1QMPh8ql03nggaPbe4EFeogIbCL3Aq7x03Av7hyVYPHvovjwzflirUbgmTcXZDiFvI2ewjURm-M4JRS9AaNiuOPqsefG4jhUqLcS8cGb01yA4Hymp66K0O8k970VF-P_Wvzb9Se1DC_yTH6FARNT7uq85yIXDkh00POqMSY8f4FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEV17AFn-FOhLP3kOzldm4jMomd9HCUij9ZN-RrT1uYzuislaN8SnRwmTuvWxybMpxznT26dqMPPHpILfUQAE08cs8qcjeJ5JOQcP-qUFwxvBmvDTsdSzHaqZoUAHIl_uSX9HApn3p-Ssjb2KiAzCDeqacWaiBW45i93zccYzfp28ldHP4YhmX5HCSoqkCDeFSgiFUz1wnMFSNPSkH3M7Rua_5Fn7MWTbzHweMPOtlqOTZI4kNByOgiCY0V3-RCvxR3lPdFd3iWhJrygcMOieOsqbav9TSXjLziVhGf4TOAIzLPL2zmas34ttChDnhnWg-L5wrpc5Do4-g3tsri6TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ob2zRcwiNnA0mh2fdgmUFV21V3KfNxGbW1uEsTQ1fLUz1JMk5VhuR_sl0XzHgTTuQ9vRhCHzbOhFCUr8n7gpl1qr_7UOnJfGc0wApbUbvzThTpeDY1liq8A_Vliaxyuaz8BsUBfdjDbUJk12mju9WaDRMBDdwD51GHguBAMXggqG3vgkjVHKEidLttryeHMa22Sin00nbR74gISYGpji_SGjrXq3ow69VisOqMLnnlmd-CPd4aTz686xx20oEOzvjvs1llri9cD6k0kGLeXAu294cXJ_4Fc-8jHEgMjmWwXKTgq5ulgGu6HeX3vB4JIRKQSKVsRU9q2hTapgXC7BlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQPgoV3_I2nhme4ASR-U8A5Yn8W8PuMQMiRLvUsPCbdCPIoWb9HSfnk4h6etRNgOKfMw2lkg9L54OXiq5jKdBpY1KQGyA0BVssPMHRDdlna4ZS03N5fKf_j1zBWmiTh5YPEroC-krNTBd6Az2CvdSlp7zDD83VyZb9uMpq4eqaMRv9aJIjFJ9ulpRnAMZ2CYGnJsH3aVs6XB51GAG6sIR-JzS_a3svMYZoD2VYA3lZL3CErxunv98imZPzM0TP7MbNJhX8C6A4sgarS68Giiptq0Vv2NoC77w14KxVvpnCsqzQYVcxWwadoCcX5IhgaZDM0IcrTxKLC9R-H2mkFHOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fk7AzzN3BAGAOhXzfjJCGVwPEPewaYc-aTJfQDdn13k9BH8fmN-j1YDPeTERUxGolnHEfY4pIcm-ooQ0hsTtA-T_Fkkbw8kS96PXBNDkEPIaV1X-SM__bdhDPqKraIAeqb-VpZoxpRkU1nQw_XinHX3CCn6dmmejtgeYvSqkpmIx9mM6WoUvuhN_5BCj84NLleCiFIzkQPceG-fubCTGi4lXryBRaDhDM65dBBxvLkUJfFObpdlSrruscg05i4xjmSqLo4BcYnZrUb8vnumCxFKk6Shjaaew1l2XvY-Q1W2Gsah8ftu5Au-TGWH4KE1LH5WTWj5E9rMAQTRYRvhCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWhD7c8YP7Ng4uTBLiieAeVAro-91WZtLRLenfHNowxQGC7acTz9zcM7GIOyW2Lf7jQZ8B5-5d2Iw0ZSzF6y1C3ldSXLPiUTUG0qt2lg8_WH7GpnLjBCgMWw_3NQZAig2I0CKoBrkMiG4KhQo3ifHYytHVeFHY9LGoP2JF_bXfZdjR4oYVcBTki0gyzNHHcIDRIhvCUBHp86YI2_00KJhcKiPDK9qtbs1kzdGbXA76HAqmx9OQsNAEs6YvnNdBytiM3QoS5vI4u1haZ13qJ3QMAn8i2yUaJBQUcs2WkLffmorp3JB58tYl4Lv4pcobiy4LlpLBGtb6U-1cWuj4LETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=cR6ui8TE4IjzLUy01Kt0JFJcEgHh1AwtrBE9qZWFPvpal_4UymyQ7f2-tWm5WmPRErx_h3DSiO-ZWfLl01KvytzKSZnCnuigCfzlth8mEz9685WhwtYpyQw3CDYnkprpNSCt-pULQzYQgs6LCppKU8nfhQGFUaowyvUanjB64xbKbzJlWHs4Wx2hKBT0UlxPr4dCOFoMUtyjbIuP93iZNWxIiiHeCR3PK2JON78yMd9yLcet4JVVgpNoYBCvbMg9tb-KFdthejsu9D8kg2we8mCAkcNEMaXSSlO2uepvaujuaPByuXG7yK842fzZnV98WVnSxqy0TNuC4UMKhdq-OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=cR6ui8TE4IjzLUy01Kt0JFJcEgHh1AwtrBE9qZWFPvpal_4UymyQ7f2-tWm5WmPRErx_h3DSiO-ZWfLl01KvytzKSZnCnuigCfzlth8mEz9685WhwtYpyQw3CDYnkprpNSCt-pULQzYQgs6LCppKU8nfhQGFUaowyvUanjB64xbKbzJlWHs4Wx2hKBT0UlxPr4dCOFoMUtyjbIuP93iZNWxIiiHeCR3PK2JON78yMd9yLcet4JVVgpNoYBCvbMg9tb-KFdthejsu9D8kg2we8mCAkcNEMaXSSlO2uepvaujuaPByuXG7yK842fzZnV98WVnSxqy0TNuC4UMKhdq-OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs9Xo7Pn-NZKk21OsCrOfEZiuUGhkyl4fGilhmklNMe7sAOx1-7ic5-KaK_NpMTepPl3FwxZVX2qBjmUhmQKRkJekcNZsprKIlQb7K6FAYM83vv2A5_JBsX3AM_lHljUDnuNK6NMkFc6Ewku-bZT4Z2wWkl0IgTTmsVpl8xVVu0BocBkIQfGjjX9UvzGS12HFV1WlwlW9c5lugDLRYZdCWRKzHKzAHRXZ9pGvxdJoPDq-5MilMxVAI8YZa29bI41mXg6MABs1UydiPFu3AHnb-K_ICv0m7J4YM1GIgqVMNYdo1u4_jJJczhYvsXn4JhQAzo1mQ-VjXGRaaw3cRH3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt26MS46-ZOhrwpPGrKHjS-wpA0J5rGlIkuZA0PYMdbH-7c2ssLZo_tttlq12ouMyRAWUlHMxFDa6GaUrsht-uHQpgtHy_mymLLQVND4VxUe0ABAu0r4AXw-TkQvv_DcO32gcotYHKhMRyDEZOx2GwNDCO5G55WIIZSZLLg-cCrxB3APNuNsUyeS85dOPo-0QwxWTXnZs7dGFfk80PLbm2w3FNv2-j8JlkbGHvSS4pVBeDnas39XxookKC4-wPTf07UGuSleHWNj4UgmWK09K6l39J7IBV-Txp9ODFdDZ9lpDMoenD42rWaGZ2senFChLxjKApuaTiTo9fi1vLVDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj_MiNTe8-ie1GR3zu1gMTxUH9NR6irhy_NSgB2XGr8pAqTOdxloSry6xTc67-eq1vbvcn7ccId1UMq2QHJAi2MaT3F-hLg6CG2gkcDKE7XN9k7y-F9d2MUhTTyLm4lUiB1GF9qSptQpmW31e33UOvlb0vgdYFOVT8icLZdfPwAZFw6exgN7qcoLCD_DknYLCl9OgL3xE4NxICYJb7KTiPsn5plDYhLOufwen3P3gmcxfU3CONp7joG2FLzZUlOcMBwg8DodUjL44Vk2_AE5rdM-pmJ_5cvu5F4IanYOADoBfkmOT_UzDtdiL2wl7VEg8y8EI0ll6r7eb4yEZJXldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPa7wDo8PHQ3stNS62uccJzrWpMdCNyoBNKA3G0FvXFor7o2oH0EnO3ZmHy8Qj5toVpjtaUtvvAHIJf8WX2v-GV8Ao8eq8Bq3TC7DYh2jodC5t8MCHifjOUNbY9ku2SfSv7EoOqU4r2WLex2W1fzhprPKeQpRwh044fL4vu9MpA0wFaggiJGbb1VD0MpZ22BBLSbY1G9PToaaqK2gFY8IkcRhs3nao9DsyK77Xhzg6qAoO3pgy_mWvwNC9SyV7EKT0ZZtdVvaXyxfzXrxh_cMopiCfHWXrFuzsHRnUlGN-aP5O3ocHZVRkv5ItmYnpjriIpdF2HyJ02bKdBgO03EyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdcuGgqajEGhg7HcNaeESXYCZxnnaNvNp-e3uWtPyULQiBr0nIFcP4BWW2zGuDGStO83_ajpglAKFoETSMMVcAaYwvfVGa9wRaiklbdBk8I5xhorC7jeEXs2GhDlvXTExD9q24tpP1iUogcFamsS42kF4-JQiKj7mcXOYq_XuT4P7dM_rx8M-sar7cl8aa8sLua1zwxwj9n9uHbabzUJGCxAHPjNijt5TTZv32Y1MVygd6zXb06njfJLM71xBhYjuDSDqW4JCK9lonUWSgpUeO8Z0DzGjn2grfGilNGCt93gETI7mbANmjcQ_JrDW37EVR9y198DKUeTMCi_q_d1MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0sLww5r96twu0FL-Zh06Fxo_FsSNybES_Eo381v-bkR8g-aiMNvw13IVnQiwCJEjVAx-0c_nDRWzfEwpYCk0q3iOCw9FqLmIR73SiUPYCVs3Jv0k7MfriWk0Lbc-eeRVlw1_X2L52IC7b7RZA-akL9yeaatomHgwbFfBg7ZN0vK9wLWDS4RFPRPCn4PMumb7jaIoTFuPADpXaElG9H0GjhoihAzUICc9bzZKrustTV5KL4xmXP5BxICG9bGNwqxHIm0oGxZQVmZSEciiwQq67OkyfE2n8xINl8E5VYHTetZhJT_VcowFz2nXlKBq5tgOI8RAclalNFLqK3P_6pUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz04NCoUi_Eha49CQftu6FbIiaX_KIpd-5bDOwVdwLIOn6muywRrFTCvJCQC979lzdIuY4Urb1nD8cJ4ONkD8ZDrarlHL4JOxLSvqrvTYDQn4COLsdLVB71UkaSMI_UBslz7KEUu1BJ9UE7jzU9bdZNljvcoVyDAIa-bFBWgYUvhabc0KYi_LaZn2Kzed7zAz68UAIkzz-5Ur0ZWjCUfkOemBrib2Syha9rwFkvAuOMcW_qqfjpRuhFuBxWKOMdTT-OWhAjHkjgVde5ifUXiloxg9AV8QyD3zSSWu8rBOKjNBxovbl6GxntSqO43WbL3m_K3eZBIZPxPjVbRDXHelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ_IKu5OjBuV6VWZGE_U4dxcYzda_225zEhPlIsA-lH_B5oSs7Zb0Gtu7uMRTskPfCcoPSN0xoCWqqYthZbjYSau-cN1oXtPMamoU7SA6kjgIXvRfhl7xfyjekUp15kEvmA7dae5GI0oFhWSuBWCqQi-zo9NTRyiDjB6dty__wiMq0_YPcQ7PrXKx7e4dGiv2ZRotRZnZJKghZTghHt6Y-xRjxGiTyhjUnUbvA6PgZl4H5YfCufi8xLJnHF9x5rvGYRK5yoOtOICjE0ImXWQWYgxhRcujm6TeCwRIUqNKNCfAS9wyPKqdFS4U3qvvsh2BVcxCJpbDF6XsN7O626Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONKSDFTKnJdymCoIxhpJzyuS-SdV_SbdQBtot4K4m4P5w1KlWfxbvyWAVqwQlDJ9Vki03svdrmW2UrZi2NeQlvhRAXnKch1sbOvVl39MiYsOz6f9kFAmWYAO5xDudWe46NolbVemgIjaHAuWSY7UjdsbDIBJt7M5DzqUK0fk-yy5U3cGQ1UIQPAR-6Ca3VCHjsG1_dPFQdaxoPDkcNZVT5VtRo_4c_4F2d7qQMfaHiGOQWNy9V6IJBt62O0nXmZ2K2Twf4tXWBS5hDBv1nYAiKrwGV99K8aKcJknkeJfK1MZ06IHJXkpc9jWwGDFGDigr93wZ97QXNVYJMFpwuTvCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=f4xYJTWaJVLZTH2nRrWe700Dks4HPQz_FQQXuz5C2l3n2zeizgYAyZ3zo0iw8esY3gbKRzSN1Yja859eScqjnaYN7OamUAlkky6i8jnN6P-C-zGFu8pP9QM3092ImVWGOqbtG2ipBte9-w5PhCQlq9zEX9e-9F45lnZcGq-rnlROTFySEkP64OBRDuV0dIjObE7bWItuMLeCi1ZCbSVcLdTi6aA9co_xd4F839eb6cI-wDFIreY-eEytClBzURS39MtHjnk7yYnNgbm7GUCL7SMxPoUnMsnPH0343Uo1dfdozRcLCgb16F8n_Bn0bEgpUJfV_UO2_pls3ua1ugyiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=f4xYJTWaJVLZTH2nRrWe700Dks4HPQz_FQQXuz5C2l3n2zeizgYAyZ3zo0iw8esY3gbKRzSN1Yja859eScqjnaYN7OamUAlkky6i8jnN6P-C-zGFu8pP9QM3092ImVWGOqbtG2ipBte9-w5PhCQlq9zEX9e-9F45lnZcGq-rnlROTFySEkP64OBRDuV0dIjObE7bWItuMLeCi1ZCbSVcLdTi6aA9co_xd4F839eb6cI-wDFIreY-eEytClBzURS39MtHjnk7yYnNgbm7GUCL7SMxPoUnMsnPH0343Uo1dfdozRcLCgb16F8n_Bn0bEgpUJfV_UO2_pls3ua1ugyiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsSFf8VsJAXtAIJIo9Il021U7g6o3hpNcUgfQdOBc0sG0U8ujbLRRN27gOimSCcduC33xOgkQgurpfY2OgEZNW3Zg6ZkvKX_Fagk-7JHLhM_UoOfH9CEi_8FYbQ4qP7nuvQzrkOCoMkTBh1goZIL_8mau2TQmK1KOjgdbkraWPovFonFg_O3gUTmnHmF1_plA596cHmomSJGrkFcBtSoo4O1uNh_V8MYKQJr6fJ0prTQLF9nOePQY8fChAtp4XGNn03DoYb7xFy3f-9MUtAG8kr95xQJ3UYiaLYzxg99KwhVQWiJTK_-1WxDJ7ljNxBUw1GeGSbjzzN2KMWBvc_9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdI8ZHNzUw3-aC-0yb5BsBRp9qFhdr8CLCBVx-w5M8mHo6PH3ReUOafkM1m0fKeqm0WYTONdGAlyaGVP1ItAcuMFsQts6cGqZ_f6K4KEZqfPGSXs8S3GPbe3MDV2HDI0XCqfNGDYPlUSh6_0ZqBTdIIsWbz0kLo7oQe76uXkTsYIFCuSkNfm2jCAQHOdq2ffW5ou6MxQx-t9uCrMb4UMtJgiRnhh66yra3-Xl2vvPvlpSC9bz2ixpnu47g9s_P8yIfXzZ6zhPERaI3a1LAJKlOqR1s4Q5-PtuZA5aPdscdCEXAhNMRi-PLCrQ-5RW0F-rnOlIVyNL3z3vbgkuqgsxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=uETND9LxjgScWpiZ7eMn3fetRlkDuVFAxaDuv2yQut9tb5PAsvdNmpivDuW5gHyU0UdARyu5dLjZsC7lgY7YPBG8Vs_nF9Umw2_-oudn380Pz7NRH2DFnEFeV6kHfUmYnBqDYCoCOneiGBMLblTngEu4K1-O6VdtlwWLyVD7E99vEZt2VI3ukOBh57R5RG5-pWSoPIKTaSKtdDoS5HSc0NVjcObouoLUw5G7hA0SwyaOGOC2ItzxFeGRSDQhjBwE_LfgJmqMVhl8yojjDW6OSc0_bLZxBx2g1n9RPkCi5l2N-ejov6sJcRNDbosd5oGsznzNtl5Y3abQlAi2sPw4iTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=uETND9LxjgScWpiZ7eMn3fetRlkDuVFAxaDuv2yQut9tb5PAsvdNmpivDuW5gHyU0UdARyu5dLjZsC7lgY7YPBG8Vs_nF9Umw2_-oudn380Pz7NRH2DFnEFeV6kHfUmYnBqDYCoCOneiGBMLblTngEu4K1-O6VdtlwWLyVD7E99vEZt2VI3ukOBh57R5RG5-pWSoPIKTaSKtdDoS5HSc0NVjcObouoLUw5G7hA0SwyaOGOC2ItzxFeGRSDQhjBwE_LfgJmqMVhl8yojjDW6OSc0_bLZxBx2g1n9RPkCi5l2N-ejov6sJcRNDbosd5oGsznzNtl5Y3abQlAi2sPw4iTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olpy69H4BikzOrN3Sc7nZzsC8DfRwJWGGLFxqaiGv9yDJYwohbe1HWHCac2XRZYY9JV_dswbDDijppuM4nJEcs3fWbzpXeAcyD-X4IrwINihQvZxlgcFS7lNBtBxomkMxdYSaPXlYKt3vT0JhdrRU2FhJk_dKO6CEY3-pd4TfMX3lF_JEzl2EgANepMY7GqrRq47K1YECsaI-DniYRdLgby9_2iMwUyqo8xcsR9LsVHPynTonwoINErEHBkx0V-K1MULRxB56sR5ECArqVqtdSZxZ2VsO7HJt9jhcDIOFr-2sYFw18lV0SDoaLgZ0wAFf8oba7GNZo6_0RhgJFt7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDPvNdVYqxqMBHZCaQ_SFZDGaV5k1PVX92B9Vqy0ZlYt-pyeRy6vSiAEMPDwmMwOqLd1hGv-9D-qM0YUuP9s-DVi9Gh2uuf4QzoQtlRljfCbYCNYHCHxNuHNRyUtK4XtWzKiW4bNkTL0EJsvHNOosERYYsgEbkbTNeB4-18_dJdhbayEI6FChw_-dAs2UgqD7g6N6TnqMZoc7CDSJ6ASZuc_3anXFmJxqdSUwUkZvtsUch6ZS4FSC2EHBl5UtGGpmwb5bFYHuVYl3OAewinp3LWMliwGyIxDqcGcZRIz5Q2GUAs28pAP_GLMzWYq3JPD0Cu6YjQ7GY6GkRsjq_ZceQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZYkQK3CowojNQK2GVfUNY19uHLvwwdr7oyDLj5tKTkFTlYNJx8aVtM69vlA283znJLqvdJ-meOcWGXBCMaxSdmPx-Wuo11_1MryD-fk44PJh7f1Jct6fAvRul_9T7TiS7D7zo2FAqAbPcw5az9yoWLd5fX4yy65mjZzc3IWo5XKtV6yExRhUbEnQdO2lsPuPpKMVzOlzGG4Va9ErsYjcQo07Mg-MTmvFkiuAowdXFg_ZK2ndfpsmjd5ufJOWfhkH_jN6LbrYt05utQWHW5aJY6yzs9peTv7Lpw6BWKqKDkLoDU2Sx__kIZwI2DoU-10ITJxzcPH2LYF7rzCFZT-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPpfmIXvrT-ue3pytOTouqGq6MpbXNLof-m5FrYypN4Q0WzEvYBb7TU5c_-jnikbGNi4u1GCGEo0VC7jCbdy2sgdUcQZkr3erh7m8otp07eZEmPDYEiu3WfZXXoRRi_WdiXc_y6MfRQVD3zYDDPJI84EjhOj21lVaRxcHIz_mXNQu6E-ysLTsZK8zgHgIoLTN-9_5SFqqd_txB3zadqaJzxxoYgG7cUxFmIFs-qR80MsWR9lK9dnfp2EwV5P4udgEz1pIjp9azX1-_oE3JUjsRrp5ndCGXNpPh7n9h4cVu9o7-wsNF6KV7-wVrm6GB5BAy-ckYgtHdVRHh01uaXqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUNCowgDpsfFDpkshcwh2WiY4xo-8FmnLNc7xKX8IyrPtCPTVkpfd88wnqY0HZGC3EDeV883ph_py1vYYb8IQFzbMZiPRr5mauyArMnRFFNALRbtA9TTgia7sRshVjNTH0mwRBw1BiPfIptQ_SJoz5lYnnTsYTURyjBzRyEcxLNvBzZ1dEu27Bm_k157aIQN5KvXqjkhSTLOLgoMuGDeDoznLakt4yQvMF4FWKaYO5mGJN0q3fKR9TWq-rYJm6z6r7ERl1ap5iIchlic6POkq2T2gL01RU7-lYLe94bCkH2zBJ9upmCqNtq46OG29LX2wbzDxuUTMCpfFNLMea8xCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpQcqbErxeeDZtToX6RH6MhQPf2jrBPX7Amhqofl4zeQ8Ds-pwkjOKnpXMbZbmzfCVUbvqZe4qiLFqfJMXMeCAQQ2ojpX9eTe7srCKlaoHej5IpX-LfIb5fCNSgUixULablyk5N6gL5D_uW2Ed2looUFhbPkJbf0ns6MBPExNj_UQa3LoN2pMUHbUALGphCv98AC7bS6zX6GfImyjHxNBaTRsfGD7FIBx1yN37A8eKgtUyqpEuzD1xcwj_NcTBED1SWjLNY7Gw5RN5FsctaAdX3265At71tWhGMa5oB0-sNBJOnS7vjLT7bhFdUGrbr4hjRrXUVSS_CxB33rHVvmoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/4878" target="_blank">📅 18:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0TAZIY9sY4B0ek-upKEwxF-qFfp3oZxnTTMsWaHcdBmiL4gMkzh4HwVs3geRF_Z9gah8dcdPLZw5QRXmTMPAdHCRjMsKVODUM36e5_IxQopQ9UkfvPXjTnJk4OZ8vElQ_4aYyyzJ7izp0I0OqJWhvciVkyLszrPSJ0NMJGOObE4xUbCL8evJ4bQ7rSeyJmI-lNCqdkhAtlim3M3xis5s_efNFjMzrzmf8HDB_qIlW_959VJCtjY4QOLdu9A4pC5-864J8FxGDFPTfgDh4gCATtbJkfzFWkzY96N8Wl2-H8qj_nHwZ04bzs18dw9DL5ixyewAPRZ-7PVF6Cu2yxKbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sawD8O4pENYuR2J1vK1tKQs7iqZ84DN9mtVCsEqHpJ7eakHIWaHWAtnYwcwSSl6JSsUMCQeZEPIO4VEDMtfcj6GtrBcyzGKCKwpdx3HjHBuvSWEJ0j7JTtil_W5Je9KWchnNC9_nJIxcmm4T7HYTTgXeeaOJOMKf5oKLfRdvPnoVblPyvXz4v4n7Mwpa7c-8rFKJ29aQpmMqRLUBYr_NGV2ZptFKLhi2lysj23ASOKEOco80uqzzuqz_lgQUNfM6_NhxRkoQdOohoC7ImS3WzS8yOOcf65SR4Zy1YRhc_B8WpRMY2OCYB1PQQaN43gyrS_Wsrk_UQe9wCJe2bDXmMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL4Bepg56f7yH37h3MOpE-v71ZGAZFhSrpT9UkR8fwNaRzSHMVZiLEqvmmBkoWMPIzQq8zwubs7jggcSckX6S8Hy3ute-U-zzCtl6MD4ksXe05zINgAf3hVs6YiuS6aXzOtVq05w-9B-2luVXB4UDx1R_QxzHt8pm7MYtosHlmglocxrBy2vc8jakvgGC6tVuBJcIHnHlPIG8u2ybeHphPPZgyBQmbKWbAiFyvgYsJRelutKSxkfojd-0GwIBcVnaRzDuFhk8wOriGF9Pe8dAsYBUNBlXYjqWRmc_rSIyj52LX2xiOYPC-eQ9WlJHxcxtTM12Fu868oz_5mjlFLUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0QsbDJe0igEVD7CCtIiwzrb_DJVPDlvxxMxU0V2xeREOrpXwNV_ci9btMT7TaRAaEiFofBO23Im37_ZWwcLfeCAKDLOQhnBvQBpXOCvLNzBFP4hyJYbsZ0SZDswofbOTOS40lk5Z_nUwkYGzqxx0Uy7Mi2hFmJXrVnHPz8DdIATw32wPPZ9Q1A2eciwyTcR1eB7CrR9fejsgcNQMeIgFyWpR_SUUh-KQkXtPF8RVGSF6mEMwTiuKlwvTJtc-uKI5jU3U50_PXeHWIVFNy2zPVS3w_FOCKjFF-7ZVTWB3RVrMC4PqJl6C9NpALqvHmKcCoUgCKRr77qhYan96CeHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0KciY6m9weoWHdyhytXiJz3YXwCWLUckMF1FNT0Ur828HAF6V2k1VILDyQDSQRqQl9tasXuVOisI9hwJNmLSOY70QRbYu7ZQN1QEMC48WZVBQjo9rpOqZ2RJsOjvqm-ew2hZPJsT0u-6Q4KSUvOpBkZ4E3aGwmj5vsTHkXEEMgjiNm-NvWl5_w4-aGX6rrDWehAHXH3l944NKgYff7mvUtGgeB6cOAuYdgZDSKAzOdO3JCwfExIUCxLNrqEXPYzvhLooNCiQukmQEEp3CCAL83GVaBoLPxjwee8rO-ffm8IxMZwVY7xp8gviUPoo3OeaFdSn_qX1SvrSX1Gih4IHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
