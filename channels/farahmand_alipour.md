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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 20:37:23</div>
<hr>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8dNkK1szn1BNp25MrwT3wYm54cVhCBAxZtf0W7_M44izNpHgyHjuEcZJ0Mk3UcAQJCbB01HqmshDdtuIigAP1I7F4YSqquDfmBlGFqXO2UyPUKpxkldjY7wVgDxCrkRwfnObu65H7DVBw4vyXWNpDTlon6BZOx6ahVcTaq2_qpFTlMdfp3g6P3989B80aHyZ_fqlnstTAcC4EZo1H_5fiqDcbkbvEZ3NfuL1EpQUHPHN4O6lir0Oy8cz0d6F2Xcuugu8c23XX7oi0p_Co64kItMzznb6v_F2fZMMGNDrpXwiRUiAO0LVXik_uIogz3RdbOmaaErm9Oi3yU8QZJz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmxAcD4X6Yxk_l9zHaVoAmdIIXpORSZdJTRWyK931qDNqMFldSFp-a_llTMMWNld8ToI-4j0jxbR9QGnsokwwM_IC3UL7qe_ydsEu-wlA1-NrxdJc8X0-2T-6OxmPEbYwjUwP2Jo5hB7_0IuOopjGVBwqAzyx7IFfQC330AeYE4Shvx8mE1JSP2X9RWLYyjuGzyvejwfScbpHucMDfSXAboZIzILjlKr6k7n-jRZHAjD_rO_fSDpi3a9exriMAUyjGJ7Wsofia_qZFr-lXyQh5rUrfCu3jlLNQ4aCQfQlo7760raCekyFqEzLYaL7WWx3Fv8Q5VDk4yiBluG0pDv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqpYtXr54RW4RV9sWQsqxRf9YfEAgSwWx_lbPmHUzndkMXB44VYMWZQVMkAKJeBxD1Bc9Lhk0vf0nATb4Uuh2VeVwrrM2OAmiJgh0WtbM9Rk50V12TTW8AmoB0fwPPzkNePIU-FV89Bg_2SiU9sSM8m3rNr_qq2nrato8D13vLIlNLalW09A87APJhA9gdLt7pp2MuT_WeslJv_8Cg8RP1y4GxPCkNuixNeCWIiEHbL_fcYPfMmEm6nXhv6U7NS0BPoXVirmrWi-GteNMZx0AOZUfwc1eCbgF1EEhvFDlwDck89x4dcFlw9Zh9qJtVGl2nh5cD4fB5QVrJkFM5KcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMg5GeC7LmHvPMKHD7YxCLaDcNo7b9thX-MU_nKpp7eay8jBzZRHQAOmyrfhp243_OP4rR8Pf_iqBNclKnTpRdvO3rjGEeQryrr1mtMTSZko1e0hS3K1N13eP8aTzoHQfVKGO2Jj2z_gI9iu-94vrrjjzcoFuDzZafzk4md9sg39Eg2Je8FB8AtpNDLkCDNBYg-lL0V_o2-DaBbk9zGOvOUL9EVLFwV_PipXzQVqJXvUE8WKh7agdIyD8O0cERZbVL5QqFJxfHlUyaaBqc-43dDlXgfrRkUjNz-_sWRhNR_XOc1WSLVgmJVLWTbsLEPVG0-i20dXsDsNXb02HXns9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0ry2yDNiPv0HK9VjVN16-9ch7habE0-j_qGGUXnSLuHsYDmgMFO-ImenA1Opj95gi0Lwt3xZVVYn54C04ZKDS8kF_dRfK00_h3NqfHasVFMSkvhZxi6yrVg9TMo1QJHw7CU5VXifyZdE4TquW6sohmO37D5wkxjBMsaoiormYWTnH73LrXcCWhEuR4FtvO3ndLMYazUlk6bENimBQ13JC05ZJwtKn3ZH0vCgW0Iw615-4JsU4M09JWQUmS8oTXhm9h8wE9C5P2VfAn3GjAvaLMz0jdEfSTsY74jDKDrF9N8e6ixvoDr2jRHCp1xrrNGnyAT1qsHmWgnmLLQ5ibdYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlnVzBIQgXIkYtcbZ6qUtWk7_iokG2H_rnHmojnaVsAwEo6gUeDF0_gvMngFePIncZXk61TbmAMx_UZoRs6mkD1IsuZ7UW06b2QwLalz8mPXMKzw7uJxclRIH44X2iPpORCygyMC7vupJnkmFsns8ILDAH-0vzgxW_aN-2dqgFdQH5zX48ouBCLMSHrSoGfll_0ERKeGX__QpFqqaOOkxy6krjX3_Wo1cOOX1J7nWbuyHPwRXFqzc95Lh6j2KioRLYCLbSkvHH4OQJ3OqrnG3oY0Rvfc5kIrq_RpJz6x0T63l84B5BLPrAdxYuSEpPm4tdwNd0TGvsuIv5WnBEUfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=oj2-RWxkgwHH8bzlXFgXFp1cqkllflcUjpaZigWgwbKQoFqB1ElmL0UePDZqz38B-TfhZokr9qDrD-vpxAm4OE8KAcAuG4LNCdhvft7htk1l90fnn8vc3kZMNwD5wRppKeqVl0CNqdN96S1LK9Z-nmPmIZMlTZKMNPFsmjXMPj_4h--lSsUKEnBiky8OddSmDhDvrd-aWJh-MFYXm0PJLV24tO0cYRwNeJIRfGBHiuU1mKZjKVnW4k7EFGphiFppzaP6uhtvmlDwFWDxnDBCDBGuxEupcyBNr3JFoowAQrLnkSdWMAl_21DruQ4R0VP89NzyROHYAYrBcKzwWxVSihXS_FRjVxXsYdqatIVW6kyzOGj8uDxPvm--EgdETAWsbRsSNPRjKsYpD89Lt3ZGdpCnzZ_ewEwCsfBKmwaST96bLaLfPFzddlpJg_2zbhtt6cwyJmn56j-XbqCzirMnvfAHmaG21GsN9SXGXoLEc05JTb_ndm4YpayUnHtQOtfiVjPtqJEXvmFRyXHHR5bghbRzpuy66PQwlYat928lUMpaZAslZEq4LgUXjCjDF6InJREE7wEhyX4BIkz_JoSkCLZBd9D_oiWVojr6TlqpFzJtJqePFf9ilp37fAu19XwLdvJubDxZHJEzV_GZCPJxBV-0MhZVZPXs1fQvH9EbJCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=oj2-RWxkgwHH8bzlXFgXFp1cqkllflcUjpaZigWgwbKQoFqB1ElmL0UePDZqz38B-TfhZokr9qDrD-vpxAm4OE8KAcAuG4LNCdhvft7htk1l90fnn8vc3kZMNwD5wRppKeqVl0CNqdN96S1LK9Z-nmPmIZMlTZKMNPFsmjXMPj_4h--lSsUKEnBiky8OddSmDhDvrd-aWJh-MFYXm0PJLV24tO0cYRwNeJIRfGBHiuU1mKZjKVnW4k7EFGphiFppzaP6uhtvmlDwFWDxnDBCDBGuxEupcyBNr3JFoowAQrLnkSdWMAl_21DruQ4R0VP89NzyROHYAYrBcKzwWxVSihXS_FRjVxXsYdqatIVW6kyzOGj8uDxPvm--EgdETAWsbRsSNPRjKsYpD89Lt3ZGdpCnzZ_ewEwCsfBKmwaST96bLaLfPFzddlpJg_2zbhtt6cwyJmn56j-XbqCzirMnvfAHmaG21GsN9SXGXoLEc05JTb_ndm4YpayUnHtQOtfiVjPtqJEXvmFRyXHHR5bghbRzpuy66PQwlYat928lUMpaZAslZEq4LgUXjCjDF6InJREE7wEhyX4BIkz_JoSkCLZBd9D_oiWVojr6TlqpFzJtJqePFf9ilp37fAu19XwLdvJubDxZHJEzV_GZCPJxBV-0MhZVZPXs1fQvH9EbJCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=LflsC3QuXxsvG1hWqeutYxbA0hwuL-e4GNgFcmYYapPpY3IqMSogN_4bEt6hf_CHMZQbY6wYK_xVbLnl-qz9v9LJZjzeqFG6FVDGwPrkzXOzbisRINK-6tpmnYGO358RWoo4DS-qLgb3W74QmbgFd-OnxG_qt3b5qDdulf_DoY2v8aHviXD8v_DjfVaohvp3d8OwNgy4hfqggu9lv7gromCB9jyTLjhAuVUhA4t0aG2ey8XawbtUT7Kg1FIrM14GXHa2pHTn4wAi-3zyBD8jkkDc5kxZ-syEd8A2fyO9j4DhXKhPBHSd9pIl1g5qh0fbRaxW137y0VvKApNmv426eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=LflsC3QuXxsvG1hWqeutYxbA0hwuL-e4GNgFcmYYapPpY3IqMSogN_4bEt6hf_CHMZQbY6wYK_xVbLnl-qz9v9LJZjzeqFG6FVDGwPrkzXOzbisRINK-6tpmnYGO358RWoo4DS-qLgb3W74QmbgFd-OnxG_qt3b5qDdulf_DoY2v8aHviXD8v_DjfVaohvp3d8OwNgy4hfqggu9lv7gromCB9jyTLjhAuVUhA4t0aG2ey8XawbtUT7Kg1FIrM14GXHa2pHTn4wAi-3zyBD8jkkDc5kxZ-syEd8A2fyO9j4DhXKhPBHSd9pIl1g5qh0fbRaxW137y0VvKApNmv426eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=CHAI_XN8UG9Yo1TC_nVi1ifZ2oiR8WAq6gX1KfpPYbqpjTzHQMSYI9J757GrzXG8IldeJhhtJPMvD5BUuPAddcOG9W8imhpPLJiC_dKQqZnuiRDANvMHLW5zqzcAfSjL9_Ev5wfzAxU5pvFjUduJJCrHsJuxUS6Sp-ZKkgO3ifBGAtA63yCpgV_7NaghLwoHDKKwGjAZi79_EajydTWlsKCq0YlRSY83GhYQWT6BgciDsg_eCyoEeBR62mejklHTwqxt4DKz8TNQRr-l9pBqcczswm9cAu74v0Mjk4cXW3VagIwRFyhtYSjyau5HubSMWx6UeyZNnsMpF0J4K_2p5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=CHAI_XN8UG9Yo1TC_nVi1ifZ2oiR8WAq6gX1KfpPYbqpjTzHQMSYI9J757GrzXG8IldeJhhtJPMvD5BUuPAddcOG9W8imhpPLJiC_dKQqZnuiRDANvMHLW5zqzcAfSjL9_Ev5wfzAxU5pvFjUduJJCrHsJuxUS6Sp-ZKkgO3ifBGAtA63yCpgV_7NaghLwoHDKKwGjAZi79_EajydTWlsKCq0YlRSY83GhYQWT6BgciDsg_eCyoEeBR62mejklHTwqxt4DKz8TNQRr-l9pBqcczswm9cAu74v0Mjk4cXW3VagIwRFyhtYSjyau5HubSMWx6UeyZNnsMpF0J4K_2p5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooXPqvI1q8taXawnq1FN12dPEqhZLLLOH9FdAjS2xz6YfW1_72kw3Bmovod5L7KuwOrYv1pcK-jlY1NWC6-5KEhcwsvf5RJG9Llsk3Trkpg5z9X_u1uaEBmhFUcfo_qKjSNff4TwDiE_ljzgxlz1EAI2IB38wkBmIm8R3QFqsvhwCf58Wft2k9g8hXTXSqTymsQvwO3z0eOk6-i8axkcMcG0nadoNFF4SAfxi3nY9LvBpSxtZzdZ5aHVNwoIEkaKs2e7L9uWwtD9jgqg185fQcBi64msUvdXLwtuJgxSHg_M92R9OO9gF_ibn2wkLqZ6giqoGLgUvjS8-wPYgkvcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaS5c38dvFHpnKzsqhxqiqBAUB0q_KuaLnc41HR2DWjHDxpf_brE6Xx7x3jZ0_h_S9jB4aMK7UHxw_1hPuHz2C4o0gMY4SsbXOwy4egSKeDwUzSBTB8B54Clpu0vEJ4AY8MfVy6ce48pVd7vnZLbJxaqhgCEqv6j7JAPp6U0tGWbhX2kjdOUy6PJbEl7gJOSzQ3_MTTH7MzPeuR6nfV2H4E3I4r-nFeS40fdcRLBenJPf_q5Upm-kOMC07N0Fp5dR9PWN2Mmo88AE5aQMJeWP86G7jIXmQg2wYfS2e_vWSzTHufjJo4teOEP8bLHw3nUIgUQiKo7d1Ep6yG9ZgBRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dupxAbYqSGdVAJH6INTpjRynYqtYaoe5GsBfS-ELoPFB3kvRcxhccZ4SW6ju_nrBfAlRhf-QlfgTIRli4KmSl4YQtRlFjAAOYeKCGSEhsgAR70Ep_LRklHRavPfW2N7RIY6v8K9urfsrtdg8dXa8rbhBS69DU4MBvb8tMkfFXQ8kjnXJdqdjB3IVOUv6MEIIbVY0qDuvXpm_zMLhfk3IF23pUteQX8zscNfQaPPJR4nPF-nMS2LSUsSsdP8Hrm4UudnRTo8oYNzK3Svz1uLMDrRtX0mAvammWfulS23ZiDDM46_Dqw2p6XmprfIKUn5dPAwqlrR6P6o_tIe38W0QAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKo6GMuB0iqaOFrShjZ2cym1F7fF9wiCUKHtTP-Iz2xCGbYO4ObKW4Rp3lgNC_QH7Bk5BSIDKssg5G8WmTvShP11fgdF98-jjxOvwqKBC90bEdWnY2ThpBAsjBwtNsrTzrO1h90rXMCPsIpRjhR8doM9zyKhsNcOj6jFWXvG0gcDUy0gcMTzke0XaGtLIclbCgllrQMy06qLdHKozI5nbY1K8sVQOf8mfQbyT80CYS6YjFn9xHExa9LED-5qlrRkKjdDSY58tU9Hh45UHmX_UNLhucnFslaTelcusRSi8H_pm-gH_jfz6bQGRtoyI4n9oEjd-lSvPcZ-9jEsIHnIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAXPDIeznt_qCy7PuiruY5lspuxc28CUVni8NxiOVjfBkBoXCdAiXPyEwnk36EmZdI55HNDa3R3dcabFZPAKTZ64gjkHVAq8lR4tfGW9dz8iPaA1xCfxyVIla7r-YQqYtSkgz54j1xGrj3YE5W7HJ2pTv8oniK-fiHWpFLAtvbu36LNKn94plr2GUXPwjllwC34P7HhCa9zj7SGmIampViRZBg1chQioHTYSPCuN41Mhv8pfuU3f_3lYVG1yPpOgpyGr1jwsusoD_NbvsNdjvgT_OULTFc9-k-m-4KXMpYJFjjfoV0CLadMVd200L5gR5KLCHpqnbWWBLlmCY6ZXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rBak3jFeoXbAvi7-e6xYfvPq-BLTMMTDsH1FASE0bFa4pGbVuY3-5dC43vZHBnmytyaK-f67PO_lXTZfXRp0_8qYiMIf6_NP9y4qdmkr1E9oPPyDHGguX6LO-cpCHOsazWDUqbWYvQ3GNOn0EYmKYmuiP4RUUc3BSh-epXWAvp82OxRAb-0W81OkbFA_mLdoCgsVRgRJJlH12tcoXii03Z3uOWYaF2PQjd8SNE6HaLmIjlnhmhwfiCl-nmslwrA5ipkmqPPU5wCAhyTkA-1fSqxBeGtzb45PzVuRPBQp--RP-ddYV4Hj-oVY_H1aDgculsMoNRpwAWFVq_bYYS53ayo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rBak3jFeoXbAvi7-e6xYfvPq-BLTMMTDsH1FASE0bFa4pGbVuY3-5dC43vZHBnmytyaK-f67PO_lXTZfXRp0_8qYiMIf6_NP9y4qdmkr1E9oPPyDHGguX6LO-cpCHOsazWDUqbWYvQ3GNOn0EYmKYmuiP4RUUc3BSh-epXWAvp82OxRAb-0W81OkbFA_mLdoCgsVRgRJJlH12tcoXii03Z3uOWYaF2PQjd8SNE6HaLmIjlnhmhwfiCl-nmslwrA5ipkmqPPU5wCAhyTkA-1fSqxBeGtzb45PzVuRPBQp--RP-ddYV4Hj-oVY_H1aDgculsMoNRpwAWFVq_bYYS53ayo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=WxSubDcKcj09n51kHs_b8m6HuDcMY-93gOezv3Ul9I7vdC3kY8ltrn9PSXDQJOGzPh5Y9SWMSNVzLNXDyUT0SaXe6EvdzyHzYkqisVi04ySZUSoxlUbHKGZtV3qRbeQQIvHPo2Ihm5b9gbOJU4GhhyO-AFON_ADAOqoDYt1FfwHW4ClszC829fSJKjDgxaI2BXRicRpWHBpd6W5Os7ALITKZgNyXwc7ck9CoihJsEZYI_SSNFHUbOMrXac2SoXeFqlS0eRcT5tJ8W0QeMSG7F1Jbxja3h-h4WN97epql1MT2p-oQ7a6CCK_l0RsIu-76b06it_Na-MFGn-4Q4VcBQVGqVduOMRltMiKO02gN3vzrSVXLmr5J_WM7pfKVwxZ6i7gQTqNrJRIqAChO5rhUqywKoWM1g9vzqeHfBkInQBqHHnQAeF69gQTbApAXTR5bEWtbtt4k-48slaiX0BIvV-mA8gFdVAev2t8gVQfGUkB-N6307oS4sl8RkYh-09E_5CTyk9snhi13LocqrJldYo_ZJ4JwPCT57C3djKirt0xA1svLIqSIYUpXTs28M5B79L7cCdx3ooNdjWd3PGstxAwjoAcnHxNJVg4HUCZZRMzPFup19R_7ExPFWSpJ8LPlhEhSjXw772_0WNpXzHQP7PVSvrKfUso-vpZfDBKiaxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=WxSubDcKcj09n51kHs_b8m6HuDcMY-93gOezv3Ul9I7vdC3kY8ltrn9PSXDQJOGzPh5Y9SWMSNVzLNXDyUT0SaXe6EvdzyHzYkqisVi04ySZUSoxlUbHKGZtV3qRbeQQIvHPo2Ihm5b9gbOJU4GhhyO-AFON_ADAOqoDYt1FfwHW4ClszC829fSJKjDgxaI2BXRicRpWHBpd6W5Os7ALITKZgNyXwc7ck9CoihJsEZYI_SSNFHUbOMrXac2SoXeFqlS0eRcT5tJ8W0QeMSG7F1Jbxja3h-h4WN97epql1MT2p-oQ7a6CCK_l0RsIu-76b06it_Na-MFGn-4Q4VcBQVGqVduOMRltMiKO02gN3vzrSVXLmr5J_WM7pfKVwxZ6i7gQTqNrJRIqAChO5rhUqywKoWM1g9vzqeHfBkInQBqHHnQAeF69gQTbApAXTR5bEWtbtt4k-48slaiX0BIvV-mA8gFdVAev2t8gVQfGUkB-N6307oS4sl8RkYh-09E_5CTyk9snhi13LocqrJldYo_ZJ4JwPCT57C3djKirt0xA1svLIqSIYUpXTs28M5B79L7cCdx3ooNdjWd3PGstxAwjoAcnHxNJVg4HUCZZRMzPFup19R_7ExPFWSpJ8LPlhEhSjXw772_0WNpXzHQP7PVSvrKfUso-vpZfDBKiaxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqpIY5ngn4lCZQZmB7Vcrl8L2ko-oI6jjKBWPWC_zXGcCd3OQM9MjxpQnqJIFe-WFxJ2MNv8e0VzO1kESSpSaX7cUUr0r0Tjro5044vw2sT6mP3nkmOcr_xii_z6Z70OSrcn7bKcl7RlugArYXFE8pY3brlneHNUU_6-Nb_lAnwlsbbi1xKWawYI82fOtHyI3O0FvXrFjpS5bmn6V6spyJo8SyWZSuoZeUslhRrJR02nk09QRYAy4c9CYjnX6jpf5M4wjY73tnws42JOtyYEf0iQ06Sw8BwzYHME0pX__EFT_UEFoOMamFPB-BeGyQB7GNXW-lFNR18HS50S2XLgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdrUKYICsLxIkFJoKXyV9qD-ty-mBGFpQTHjU_uaapopr1nO_Yh3dIjg3Wx4XnNDhIZjtZVzrEsbr-LxKb9xwsge0ghca1md9CDCpEvJ_hZBsRAW2fZVJ00dVjY4fhbWOgNIbc8V1q2RwVKXQpEKcTd62CW5yt0glqTe-UnsgQ8r0qeLBUKGRKqB1cC3SYfcUt5fbVqWdBjyx-aYqor1oKgAMiq_pMaex9vYZI-2Bz8rTI8njcqq86wF8sUJDfSdfqgSdwI8TiqXuKTGGZRQMLycRdJ9UkkfeB2J8RZwmbWWpVLjiUMp-QcOCMpnObUsTIY8ieEuJgzlxM1SSiNQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLmjV9J69msVDX8oZ-P19x5qaskBCNApi_Zkv9w_3lQOBeEEY6tKX2OsdeyLLzojM08aoRlz4KRQz3Ip_Sg-r9wxQ_n-w8l-WgLR-2h4bx-QzMFevJQRZ0LBo7pUK3RSToprXQyBjJR_tS_UxbJaeJinfvcUVc8LR5xfbWqieSagfOYKT_SZNzrpcVGjihxhn2_znQUsZx_aANUXU-bQCqkf-CfyM19ekRsmXrwtAIhqqYpzgXgz7TW0FZL9uyCaBmLEFsApNiLAI2iQQRe9hKVD--t-E4qdjRElbRS9X7KlMmD1qmM3rlHpgXKaki9IJ4nwqTuVkFpf7hH8W8ZMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egKmXKIKMCQL663wGr1SBy4fxLP6qlGDR-q2YFJlSF2aeFiv1z-dlBw2AI1uHRupXnNDkLNhayyVDQvBd9XlVXHZMKJY-2giFrxNH8ni30QLQfnt4_OnXNgdwMxNkw8LW0zG0JN6hmgtMtGNicsM2ZkoyYS_Mx5KcnMQpncfT3ZA3PtPMZ3woD8VyicbRdSUK6UFpOYKiXeoiXj3jroRcSjUR1M_f-u6S3xsEeE2lsM4QEaA7orQ5Lvvo8aMLB7EEfofhjhcvISAsizfvfxbOmge8P4-uJ3v54suB6LluAGPEofWd2ImKanPYrX_AnBUwxNzGAVHhBW-TlbJrsdgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4rf3KBOvLdxAuXThrf7Q7akIPlVfbdGkQZbA5Mii6_f7AmEEu-edsJ9oXWoBLfxWnQBJgGEgYdV2YrdW4AnnjUnACOOJieHf8wCEG9PP7fiMbfLN82rIWv3yf6uhdrVM5ZFrgvAwRVOtyzrl8ZwaiuGGKwEo8O_LuZ8wmuMYzJcbTPHGj_qtoGfMhj0k0ewXmpa4JJGUKauTZw0AQaokal8ZpJWMRzdGWei5JLNQ7v7UyqY7xULD5jmm2Rng8y8m-aS9JUNxnH81LZB6EzCq1twPUNSKI_hRF1eqfIkwvM54WxoSS0ThJt-HbhVWtRM4XVnDW2IDZVlRQjcmvAkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELCVL9-ohdoHlZpvwhtU_YpEo4u3Xkx_fb7qpfiJQW_-hjs2IzpxEiEog_EbZm_SSaUjB9s2ovN_3wtAKrK0sjL_RSaHNHDb-knYqK2p5djwOGA_IeYeJr_1PGG36NQsmLDZtJZC1CDCHeb2IDeQAx2SHksWMJ1cQbhcRQRhX6--T5Ny0R-A8rYVa09DAzeYasCKHNJtp3C9uOKdmvJAte2T4wtfOzrHZh_5eBoNJ9p_R3GAqltO8eoXYJbeFx077Z2wLeTb9id7ybS8swgBp0BcocDlDUVSExn6l1AQgUXQ1Wyu4rCQq1f4bFx8TUHSMALeQD4lQHUmIGSqn44qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-6hF1yYBvOhVcXIhfor1OGsaYoZI8rawLIjUr5FEk3ipUdJVwHc20Lyk72ScF2BlU93m5DApXOJOttw6WJau0ePdir75rMyk5iMMRA6Zj6hIsgW7IGYgv_COMjM7TL9Ubo84z8FdFDnjpA6ABNYpGygA-MeLEi1KayLGIThiC2FPwdHrjNCAqhEiGk61rGfAe7k5EcxnvLScIg4G1CD_f1L4Wz_LE-sWwv6oFeB6Z_OUec6jyorfj5t6M58t_tVfrHcI8tHQs7zK8ST90LDY48MU3ub_g8MfoexIVpCxWPlreBtzsesWmQ5-I4fCt3IFi7TJDBhkwAEHMpGU8H8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6Ohv9EbDQmj9Tc1PH1jHtq1EUVYMtj5zg0joaQAhtiqfVw1n9-jKoeKu-YPPpciqstU5N9tmIR7jgrWKi2bCNE1GMj-VFzW00WWw4U07USkWRRHbU77vMU-f8USW9dWQyRigAvgCb9Kk8AU2y3s1ZAWAIKcGmxlHDEvIg6k98GDOZhPwQvTcHNif4enkwekrOTUOwiqJ5ZSrFuCd8_XOC0Qwp9p-Z34Sc0hTsD2wJxzr7Eyl-p_Q9UeM2gLwlMfW6k0nFxpSl6m7SfFLJLa8nx8Ult31Bj0ben91BhS93DpzjCp1UfP0uvPpTU_mPbjNCDT_Wac4x4StGd_sVPRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MexuwjbFwg9QCTUXnwprqoB2B5XXpnL5420FsXLK__Zd6_DJ1LXNQzcs_pgHeuxel6ko22rpYsBjopa9-zOHEjvtAmXF52L_bBUlF6ugmF0uwYd0UBsafDAqw3cCnRDuDSN7_ViILYdkXEia18kvxgLjSf6_5AMygN6wWbjKZbeB5smtEROJhpgAxbaDjySSg2DFAObpoYJr9B8eoVkUVjkisBDe06z7eprTpzu0jm4KT0_x9E04f3Qr7sry6li5L-5Zy55m3gIc_7ikPwdy99QonTCQTAJTB3pjGXctrwm_whXzSO4ydguisogVsqJF0_Es0PqSTfM2ZNgZr28_ZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAHVO0SHyZmEhTdTe5goVWxK6qD0ngyxFl1A8ZibwCsUcuFffOIJA0whG5oWBwoN-BQFE4dGDvXEqjn7St8-N8dD6jG27q31CBMX17d_UP019VXzFUPllNlFzhUkXXmfnB8g23xoF4HyJ-YjGhamLxSfpYJuSbYg0tvA8yjg9ARJiVLlFPiTFcAz8m6vW2AjBzLapngcivNZMmi3EvFKfA0zsFxuSwMOoPzChg19kK0681RxQWJ0Y-XmgPsfetS72kreMBKWChHTM8ijexAyYU4vhCjQsP6IR_JRutQlhS-FYA_OagJbFSeEYCrEWRtM4HGBTOEwSD7JyMUwyLA3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYuDdp9_FwML6KeY5nIL-057a2S4VWzvGE2EbUggNkhe3nASABTSf4lcZWA8Z8eGpp6G94BkvwoRWY5k-aB_N1KW4PK0LuguI6e_FvbmAkcg6dSnUvKpKN9mHQWpVx_dLhq1j7_kGDPEd3zeRI373940LwnokgujTrNy86Ju1FTgXGgh1fwd_6ENrjTiJWaUhV1X4yNg9E2jN0VP5I7kn67NlPk5My_gAygGBI-1wVAEL0F5T9X2B3t_5m3VKurxsn0RJXkx5zUhvy3jeCB5Ex1RfcFHrLIVaQWt5e0CSLdPXI9Xz9r-JmFqHABRryRMhkY-FlHOMI9elq5BBp_OZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gm6sTaZe0Z0C4FFEVNnoH7057gCzXNz7cR5LnXFand_56Io9zbOmFJKzlUb608Jm9iERqxuiVtrpql0LB2bW3BH_kggwz-WElFFbbhIuRXZxA6BfPDB549en15Ime0bRMuG2EPG9CFYpgRO509Go7V5X2MP63QgRE6887xof7EtL3VwyJ-1b2PDdr-PGfVS50pKh5zPZLglzVY-uFmIYnPtEKzpLHzmw_roFfFVwcI9XVFswgq_nc4ngZQd8kWxDApqpAf8WbSnAn2yfiM7Dmly8e2WEfyxSGYSsuA79Q0_9_-oM_Akswq6iniIj__xtR6Sdls8XFbUHUOyYd7Ev3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE8cnMxr76zVeIjmYRs3l9n4a2t2EzTbc7wzPrepMaxsgM38oDx_QAi6d_YfLsIZueXsnEOdL8f9l7T2irBuzCrZ3ff39Uj8KUCtreU3_89kFNCjv5DCTzeAVKOj8I1e49czRD88xcExQzxSEtDOZPgx8uhzmXTMW-Q1HSncZFi6SKmgtxNBeFE2gGQiFDk2_1y02Xv52ANv_wD2Q6h7CTI3YjH7pT6Vx6kAy5nIVwR9RV6intNLqN_1bd0QSriL2BtDMbGRwUzQj2a_abYXCgDs9GFSSga3zAkly7Dhk0FQE79OddmTx7asIRrktnd366DRct3JNqj-v1aqGQQ4aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n22aC7iCQ1e_QHmTciD-CXenpQ8S-NYzD7c55ipm2SQPVUuiC75VB4kxQOzzYLJarAlhOuyzhY-lOnt478pqXY1cXHd-DK6yT2LOv9agw223yI4eDBml12G45Wz2XFVEDUIMYltty1Q_GGlJ9CbNooThikgRQ9UYTE02a06J41NsNdtu-Stek4T5MI5sL4LRNkxtZ40pE8IYNmYZkg8VecOBYMYpXrg7ypbcDNcUt5NdkzN1DCKIRzTr6Vmr3ZTgNqtdyK0N23P-8aqYykqmsfd4dUQgmcvD44HM4rhlESABnhEIS3x0UHXL_IZK8YTr4UBRXH0ou-FCiMwPXIwOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2ylDi1eJZSvKSOFDVmr25QbxJlaehrD7jtzjO5-5UetMLCBpa3Og2kfFr593Jl071QUzfqfAeZyb2G4fy00BQGcKGrcwM-QacS_3IDfww_0UEoSIobN_iGyCfoAysRpwj8m-37X5pSpfuG5EnnUdQJlT1gLNJak6IN8wMiNbcV_FB1LEjFplZduwTOFqqutNdM6GPOwDKvOMbuWsJBq0oXOAfbmlKRDVMpXQ22_1IgdPLfdXeA1WNfaFlLjJyHVNc1hPmazITq5O5y3YTrWs2N9R10LXDKuB0UGX4CcwnDic451YmJGpUddFuL1poSSeHpI8kN9hWfFU_G0B0kG2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwzOpq3cwVaz-JGFYysLt3uzP38v8yZGMyqVzw-nfBzL4fDH02_C2O-F6QjvD6hk3Xs3_uENycZa8AGWGz4xuTR_fGFFZGvAxPo-v8P4bmfsK7_TCt1_6MLNm8TMyzjEHHsX0IZiF5Dwq1_dW0hyuth4bx1A0LyfZ4tIdtDdMZzk9QOGqJEY6MPjJbeiT-mpPDMD34xcR0VhZCeZxubWCX2pBGAKBWAvATFa9yN1gRH79_jsLkP5PvyKvy1QfpHF7E9A-F-MSBnWRMyTZ5tdA9lGviruKeOsYbRzrd8L5B6NzeKtrSnIqv9wiuFIjqx4tF0Owg0zEbT181P1ysHb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SANSB0nWPxKtnKRXQuf0_yX_Y2oNo3ECFin6yQrdbBEGWg8lz0uKrbkQqS-wFM6xVjLYaFy9S6pgufRB-MS2OygXR9t-B4-OhlorLWnbMPNjN4iFzcKOjfgIw6_vZmahR6THFNESqoPC_amvHueKPOxXyJrszVBvl6e80bFkDZ6F45CbeVfEicISCkEzrrC3mErGvtT5YxDCblKzuy_VOT0TbUHR62Bed2ZP8Kq5-qwLF5zlpFm3_wHQze_vaDpebeq-0Mi58zj_vEWsv2pDZ4UMeVtTli6gyyKuVjXEvlUz25MPbaImGvGEbXeTc-gHEFeGpG2R3WbZ1N66vIqeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=WyMXGyBNIm_y_u0vi5boiSI8EZApP-cnBWTF8WmPanUEa7LQnI0G4r8G3XgaMM2fSx3YmUl1DWpWwUNVzOLjYj-GQLtuWGIBkSRi6Np8B2GVIxXBavhIX2FPXydRsIXFQJ3OE-jdvXPgw1khbvZPEk1ZGdT4LN2SNCOOoh4QdDV7DZwLRjgA7ROL7fK4UQl1DwLRg76giJ9SKTyv-Ueb_kaBtxih8-HxHz_ZKVWPzd_oxKMdiDhpyIOV82uLfsLUooj5r0r81T8ZrnMuYD9HsniQ-_S0kOYprx0ReJxx9MTfCe6Uu3m3oOQKq3NIbhZ_qL5rKioB9lsH7mMum11tdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=WyMXGyBNIm_y_u0vi5boiSI8EZApP-cnBWTF8WmPanUEa7LQnI0G4r8G3XgaMM2fSx3YmUl1DWpWwUNVzOLjYj-GQLtuWGIBkSRi6Np8B2GVIxXBavhIX2FPXydRsIXFQJ3OE-jdvXPgw1khbvZPEk1ZGdT4LN2SNCOOoh4QdDV7DZwLRjgA7ROL7fK4UQl1DwLRg76giJ9SKTyv-Ueb_kaBtxih8-HxHz_ZKVWPzd_oxKMdiDhpyIOV82uLfsLUooj5r0r81T8ZrnMuYD9HsniQ-_S0kOYprx0ReJxx9MTfCe6Uu3m3oOQKq3NIbhZ_qL5rKioB9lsH7mMum11tdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCaqn04WAdGgzm9MBc8yR3BcRQZqfdClUeJdEgj7IRmWOynre3jhCtA2_3c1lgHmO5seNCQXeADOHPDuKoibAyOc_pbxGUvyDYsz81DIyK24XXPOHsIbfjjZrBCe5Fowx4ZAYXXSeI0Eh5CWL6rQNS7RQLHWfs1vfLSIwQ8j98lkCvdBbdoqrs_iY79nVc7m0zLq9oNcJ9OKTRcBfGNmKZJJoqfYNt2MnVGVlblHX1Wauf0vl5rRuMa7IIMoMj-X1Ejucrr7lctJSQacFY95h8L1ziLeUiuE2BieggThofik-aKoJnAgrFwB9z3cr1VgOeTOW_meacUY0fczeB6zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv9UPhpw0PmfIE6eZnPJY-sT8yqn2zthyVNoKsxpiy2OcNmXb501UUR4ZCxnzL9BP9uUz24KsSRvbZ2Ctia10QrGUp_wYrXvNUHDd-811SWZiCCYW6uenI9Clwn6mvou9JG9aSTodeyR4aYsVIdRbv9gpA3P-UWYPYJKWWc3i6C7pWKlT4MiX8rB8Ijef_zd_RK8JF57kyuzGDyEUUOGGmQpcrK3iKaDTRC0EvZ1Eo8zWlhD4wOwoo_re2E0Sylahmg8zJriXYSNU34deTJ3wQU4YsBJxPxNkwA6cxoQM_wQx4p1jXSjrE_eQsCq7WG-mvc_eCA4mZJ5LK-c1SSf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6pDqjPJ3GJh2QC-xOneIdyiCdIQtuk9GYv06Hxs6C5fQNREQEKlKrHo2e8qzgWECmdzVp7nv1qBlwWBmRopza_2hPJCJKwgSsEHwQhPxudttsGFI4RAxf4dN3fBYiyRYeEr0BRmCYDQ5w2rd0qAjDdmOzi6SjlX2ireFNrHx_S0eSeefdcwOvwuc5twvQWbh4tSMliPQiqTfT8mFqzA95NNctGG8kg_G4V6oGg32GQ0fJgvcSbdn-nJ97WJNdZMj8gVBp2OMHUO8E7E1jhpxxHqu8jAdW-sMLSD0c3IFzeh5P5ePR3gdgPb4aI4Wg8fpKX1MbklymXMbBvEcoeSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaTJrkfQJygWrzbBAaF-sHFe90Sl2335pP_tMejC7SVTgg-afk7k5YutwAxFBmTeBmcWta5Ojc3y75-MN9JAq1E3x8lylNY3HkJBu_iZbVL1FhxcnkgptqGXpFGO5FX0qFa4mEkUqAQIXDeSYjrIt0HuMsNMV8W0JGJkan3jG-jrsF0lDJmyRRlSIqQFjdg7D3J2dAyQX9V494mw3ybAw8HdQWwjq5fwMnrT66sB1J2iE36sEd_KWnxlYtg0_xV2ZRzX07-5loh9RX7-1UBcB__uiimm3lGt4bGk4A6ugsOoOKkLmALcTFSzQWQTLKZuOLNgDoEluX1feTU0Kl_Zug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxLvFIieoPRN_Ft5kvivCWCUPu_FfoYv3fmebK6p0FGfDhTiwPly8dSb1mR2vUKeoQnUWLkgRuL0LgKZoxQGKXwVtQ0cLbxFpIBJzAZS8XE38eo7CfEXtjSZuk0Z7bBC5Ak26MlY7JLMaNqBSGvoJ_ngV5PYuIQKbjUGV2Y3aZzbS5rto-UZ3mDmqzean0eRfgSaQzSwNwKLrreL7NPX1yx-OVmQ15n8UWWWGT0RbyTQzOtJNANfGZniPAoP2Yj7jI71b-FcyoIbekY1plx99J1gUqCuo0PWR5aLWegPaSfYfCyqriaaVIuGjZoRDxXFFocLwzQVj4ORzAff3uOYpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P844rVA0AlvpaD6vGBuNi92M8qCeU3QToIZyMu3SG8zAcPEa9yB1sF7y4E6LuraQdFWOd1FaUDmCky9qry1uAJ9eQ_2JJccOoubhwjCPd0EU5L-xKvpto0r3jCP4w1gjbovvaZvrSVZ2j6BSWHUrcesjzanVv_ERijIom6RQKg7gHjw1oE9pUDC9ru2SNYhLBCYUTGQkfefjV2x4D8FWz4G3pXXGVRCGzjCyzrxpcltPBuzkPEwumODaSAzOgnCxRdLbvbzWOuaNSJxXUeyn8Q0l71GkvQfa0T6dIlMzSBEs0YK0VEntmQQXa_TvYvAjGCVcyNppPxeRn_R4AgT5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN6v7TrXMt3lPVzD--POUwMmpDRamB0KaG0U0FRJ0Yv9Au0XDuAChpCfL1cLJTDqodgsacVlE3aRKLng1nIH7iFctuSSvjb5F4e2HyWmmFhUmk_NfCr-LiNJmiuwe-ltbXTX8RJEFc4qdJHnzWDnSMfTwb7fesStcsMQYbpXAC-1zWuvQ7Ed3jwuxji-3t0xgNLTT_bOEpxs-XgCpSlOPATfciR9RJAoROfFRJp5_sMSYnSIRxrox9l8W9aP1grl2OkOJ2_K2_B2oNh0It1SdwMI8ANkZ3TLH1rUeuKmaCLwWOQ37YphYC363RK8Fb8QTrYgUdWR5pAzeqLLtrB2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHwq3Cm0jsS4lWBS5A5rlJ3px0mJPGSZ13uqW7-LdYYOPN19kazID8uLD9eoim5r5ZUtYGf9lYb68Q2JawKxXCNC7ZvgXX6R9i9m6OEX8b_Y7u1pN92AchIVdIIY3Utflx0SanSBLTyeNwtnO1ME6fVOTyuRfs1r2uhcmB_0RxC48pOzxLJClUI544ZqAxdHI09wr-iIah29EslzO5ij_LhbOYyCWfXyuIx8zD0EZsjMrxd-wp6TnSWXBYguyKA4dorFj6BQQpNF9XwEEr3I_5IUrVjNtn4OEABVgvbfanD3DRe6Qt_nxP7kxEJ04R-qBwLWshGWMiUEokSYOPp5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8U8t57K79c1k4uv8ixU9fIpLdfp7Dj3aYcLHnC9aTepQj4zoRRefQAJG6CgLgMLklaxgOVRUS5kcLo9CZMsmO9Rl14wbnnj6JS8N5-9wIBatAmeDO3eyxTf2xVqlu7oupPtSGoj6FPQfGHcFhJoPZVhprt8-g9i0S4taDY907O6WUqnU6bmaG4YJmQQgDehK73mvZEHLMYgAHVwOAp6SOabuqtcs0BEnfDwE_XHu1IBa3U2Cas-6Cuyv9qCYBcMlrbCSWq0sspRaZQK6-osNKMz9mGGmjlYYwJdUWsS7G5Vq0bNLzHijG38CPlQWOoxfN36z6FZGT03ej_lwDPhvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=fSTKfINnUAXJ5oY4_7pdSfV47kaE795x1XY_wDuBIw0EeqdxaDWsz6ASubZs-KlUmvyZITqlGsX6F8_3mVRB5uoCEZWt6W2wxpdgJyliKVdil6alMBPfrCnXK-ybp47g8WiXQeSkqj7kwvsW6ugba_N8TErBzaJhAqIh9mwu_-Ykwn9Z1hX4vk9o-rj6Bc190Mbg8v6uPdy1kOdZTSYj0kN6NZekakmPgU8WVQyJZHGkvjW0cNy-N8Q-g13sXkDTkskmooufLor5eiZop4vgOmG7W6LVOJ0mvng_D-jvoIv_mwKJhP7SsDtl--s-Qb7io6qJNT7ZTSQ38u_ZTOTkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=fSTKfINnUAXJ5oY4_7pdSfV47kaE795x1XY_wDuBIw0EeqdxaDWsz6ASubZs-KlUmvyZITqlGsX6F8_3mVRB5uoCEZWt6W2wxpdgJyliKVdil6alMBPfrCnXK-ybp47g8WiXQeSkqj7kwvsW6ugba_N8TErBzaJhAqIh9mwu_-Ykwn9Z1hX4vk9o-rj6Bc190Mbg8v6uPdy1kOdZTSYj0kN6NZekakmPgU8WVQyJZHGkvjW0cNy-N8Q-g13sXkDTkskmooufLor5eiZop4vgOmG7W6LVOJ0mvng_D-jvoIv_mwKJhP7SsDtl--s-Qb7io6qJNT7ZTSQ38u_ZTOTkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5tFy3u183WX2kkuLLIoDlKkrvGy3JAmOe2pvFkpVEu9b1vCiykmfHpPdEMneIuQt2Hn74yVXjOmDzqhzuahf06g1PHLAC12DkXTU40mqGxkMGg8HqbXRgLmL81PYHP-yfMERnmM6uI0LPEAa1UgAB8uQJiEvMZLvh-aKzeCjz87o7YZkO2qqgY7PJYSzFBhEz-63ZiWqHfX-LUziJ6w2cc7pb_AgkuYzFN_F-ID0wH8BJ8vFB8RjTRF2aOhJAwsHtjGaTw14oJhVVc5zotI9Nn3ePgJ6ZXTu8URUhILCrJlENk103JgP0R_W7x26wN8eaKUnPwrC9nF2nvJTrLysA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArNsbuX9i2nkKCiLbgWroe8Lur0aRWjqmsl-KYqfi6Re3utd6rVvyRP2DwJOefeepF2Wkr9jkhu50oZEPfeH90Z0uvqAU0i5R4HT3M3WYSdl7gUIlg0kDcKmruvWdA4eFt3wew8VxOYB-i8Mh5kNQtnVc3p2MoX-NOYoLJIaQTBu3Sp7CiLpmfZuG3e1Y67A-R0iLlCU4nQ6YoZhzYuyfXR7DYb65qFxNqsGlm2xxkIY_cBmVyPZGcKqMBMdtIXmCJ26givcButVJPC7-DSfS0zrSuIy1y2NSZDYHPdggrh3pBEUe5loO92stidJVFFMZtQq2tC-p__uMYrHsVM0wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=jDGHol-nk2jkbMPGcD2hFwgcTgNe6hywaBaw8BMu_AZ6ffWwe2LqOeEdzdD3dAAh-P7LifUSda5CO8X7Kf3nbCd-Y1DP81pQYDEl-1cvmDy7gTTmGGeGMGZtekoEslE9eAlWQAPJ1f-9t410kBtPv4iYW_TtvEwUgRfhFKoEHK_uYEQTvsJ3_uNz_6QUH3CONISSxlkZmOstM99jBuK0K69dIcpmP4D8GJNBApeFNr6Xhc3LJ8zBYbt_wAxVcViURfCreMjk5iAL4zIsOxMQLFe41zxZp9ngHlKRFnMYZtpuTh4cGr8Hm2L8f7tNORsW9Weu7AaVyGaeYTxNw_Ph_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=jDGHol-nk2jkbMPGcD2hFwgcTgNe6hywaBaw8BMu_AZ6ffWwe2LqOeEdzdD3dAAh-P7LifUSda5CO8X7Kf3nbCd-Y1DP81pQYDEl-1cvmDy7gTTmGGeGMGZtekoEslE9eAlWQAPJ1f-9t410kBtPv4iYW_TtvEwUgRfhFKoEHK_uYEQTvsJ3_uNz_6QUH3CONISSxlkZmOstM99jBuK0K69dIcpmP4D8GJNBApeFNr6Xhc3LJ8zBYbt_wAxVcViURfCreMjk5iAL4zIsOxMQLFe41zxZp9ngHlKRFnMYZtpuTh4cGr8Hm2L8f7tNORsW9Weu7AaVyGaeYTxNw_Ph_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn0B2dFrKpvHM0UtsxqI5IkTxC63IUX-5-4atDmflNTUuj01A09Bz25vHQC5PWvxIt3hBopwS5sor1lJ16a1dz1EHIKe1CrdcLkB93UnSkRLBJ6SrCvABsxup6svqYoW4o6yImXTnd_LBf3kiS8xf60PLRnr4SIfNGLY9zBnDuwkRbUChqWALT3Oyi5Ubi7OKtgMAlOIPhqF1tk2EtCChPxn_kGJLnfhNKFAWujkfYL6_-Yel5nfvrrBidZ57if5YwjAVTU1qxUkKG6FpB9h8qXwn6Zr45-JIjE5G7ZLOS9EBil6LERsyh9XPFVc6C7kdclUcJd2TWNbQW4zJJp-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCfeHvKt0lt1vIz4u1dLqI41fNN9N-2s9ydy42osVp-WkPQswxLOfCB5A8eH1OL1w5AHeQH6T1d_mNtbzDmoiMPnJKmAZutbTUKudq7aExgfu9W-LDjtmjmVaG_06BhnVYNkw5IUT1yvUpTo1TbGrxcRx6fu8ew3yvTF__5FnzhLC6KqlDqlh4Npw4O5uPVpLlWPcnhgUXI6z_CaHApS2QK-x1dJ3VRQOdhHqvrJHuBLtxib_E2TRcJuM8X_QDkmjHilBcKOyya1oNnTOH5tTQbMqawU7NUuQzQFO0h3joeHJYVCQrmL3ii73EsgmyLYcLjQwjZSsDf8PjwoGXTIpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEM-2Xm8-467rmcyKHzNmCOSnQxZXQh8SuVpUK1uR3Wrpww5OKHVe7Fe6mGE3DJbgt96eqCTU-oNstU88MaIX0XBnow4ImHhJ71vSopXgGEJCZm9v9OlfBGG3xSiMFkFxdK76m07-7ZtwoQ42e_T7Nf38LWHV-G4rnT3qLXcwf1mrnpt5ZPLpRgpEGAw4jEKEzhFKmRzhrFR1E28luMUQPTRwzHKMJ_YPS9_W3fAbZDyHhjDUiACYbwvkoEjYy2UlKcpEACbSje7kRpgOyVStc58O7pQpExVqq196n5zzZ4x3hTJPIIAFx8YPGoShYpjyOfg2JH4z4F3sdTNJaxK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAoqqAX8PVbC-sIVxVP_brhm1Kqek0sWh0hEnboi4Q6wQA64F1XqbrWBIiiJjtOUHoJs1e-2rjFv5C22EdW5ztQIrxMqXNQ1WVZHeYoniWhc_4mx2Q3LbOI8MjLL64mEt0t-KIpldpV-ucD5S6IeFBNX7dH4MpJMj5-slTagnZoJIUTpXipDbstX2Lrec92pseod6W-mGDshQ-qQIWGgiOyHoNeE5OI_bhCy2Dtd5Ms5uJC2y4qitKBisR5DCbnhQaSrhFmDY5UdWrSVEKGvnoyWBESkfnRJfaim_gpkvIF1tmGIROckvq7k8j4knyJZ1q2z6tg0cknY_Q8RgJhFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgMcbffGPuuTDTpHDZkXQBMwB9-Pv161tjcQ0R7xdTWkAYeKrytjnFBttbUE2DCBrVfS-eL53z0660mTU7IXTLpSx0sO2kEYDFger08M0b63QqQQ5qULV89z97jE0Sa7hXrrm-DEjbxVNKdS1yGDV0wsnFGt5CA3RG7X1IKCmwWzHuSBWPPU7zd2pRPd0YYtRh790y8WYPesApradYpoflOSdKDppMPe09w9lCrRux0r82RhLbDleoSRRphMAMedEHeTfy5f7k2gO1iHmy66rm0FyH6pK09w9lJ6ZbAGcAr0vfGxPghOoO2mDkVPeDtiEvpPKdvI1B90RUlUvAma2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJqPj07LEJFF5L29ASshrf_p_AhumWbMYPvMiI78bXvn70vRyypNjskyf-HNfuBE202023bU8G8EnuuB3V1BIM3qn1bpGh4PqaDHTj-kp8MKU7vccoQ9auYX-BFFAy7C-D3veYgJi-aeF-nIKXMOsKGciUufSOSsLHmZ-hms5RZ4OaqadVsM5F08JEbXEcgDn7Ixvl29z53gEwmpQ98gUJDjTrrRbHDUcQtyTZzFa6iQw8_Tyn6d34l2T0hj9j_VC72PJNOxKyqdww5EYweU9QUDKuWuKY-GWx49tbD_ksuCUWuZvm9KCEo86ciWh5KOiv1s23nnThkApsMfUCqI3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dycqUj7K4OuUEdYC2fqhHUihnHZ5e6qafb00-h7E-tbqkBGB4I1JZD1Wb9a69gyld4r7z75wCgz796etmoacD-t0dOuAn_40qK-jW6eVNRwZ7VKU4MZigP38XW-CdVpFNLfDqttikeLrqtRwHezejgczQcNKOI50TPdTjvxhsYDU7ww9tZjAjkNWL31WhyQF3jioC9vt0XuwbAYs5scopso2eDSfp9oIzwdB1UkczR_wq6o0a_oGA4eYEzHEvLzLOPFBJlDy2W_Wrn_coX2ZS18ZAuYzxwLBfBrmBmdKFi11SNPh8WkW0_XmInM5jRBS3qFdw6dpbEIRPo1kCSEUgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7UeHJyPHiq2ldIid-tdK4qjv213aOcqiL1e6u6rs_1nZojNAIFCj3lc41DlqtflKTSGviX1gh5QH8y5oT_z9EXPcLgo3kGO-21Z9I6_Wj1Ra38B1Vu-jfPtKZzMtkQUL2MJxnj2jKgVMWxeMH0vem-XBnqRs0qlIFKumQcHzF_PyO4ulWHCnTVJ31wTFu7-uE-F_BewLcF0H6QrYLmdXFzf2vtrf0MP-uFRcSZknAtn2CZkbdRZWLHhekB8fXoIagwvPRqgvR5vprsXiStEWAJxvpQFdnFom7t3TLOO9-egVojJ5VjPixMprdJ8-3JAOKrs8FP8g_7nypqnR00I5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkTN1SJNDFhothjBWKDZR5aO_wAzYZ6gyKP8qE5hGuwKnHRV14x9DcuXQS9nIu_Fiw_UMIpc2YXTnH9WF0aSPXkI2bR4e1EYZqIiJxXFZomnGQkxRD_6F40lp05droP1dz44cv3NAVGibLlx-aNB_wXplCpj1YKf7dv06R4yowrfmEnRgyQFu8X4Zjw245DcK8FkuS_AWSFe2yu-udNYhnipAh7EGjmSi8TTZ5mCWAXuSgj9B1WOHrtc1C2kdgcLTZ0P1HjkNY2_VP_ligfaVRxFc76XQkokHRWXaDgVkHXY39WPvlGzCw0fSG-nkkwUNJpQti-IjzRT3XAb6zwJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFZ6d1PCbCegi9o3M_IaPCBWYgxpAMgtsPkHoFDvPO9NX1jMIlvHmnYaCELaXxwIPam6JwloHsxH2OcWJIgroIQ-cdOimg9md1mww4hIGOHVH9nW8Suxe4Ahf5AlxFSo04SxaBiWvTDPz4e7l0aS6hn7pexNaKzQTxKHqz3vdYGw2qm84VMGm_ynvFV3T0Ovf4LmYf0vk-R3gBL2PMzqHaNZzECtClAb0X82qLGfYwcHTLeOKXrF3IymWgb2SKOGrDQk7RFFKIaA30kvu8Vta0nqziyoNgoeToj5ef9tXGKzw6CHMWWQsNMkNLA7VPIVXj9ytcEkmRhpFPsAC7hR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWSEDLgFyBCbTyfY2W6GjeeMlsZhASwqcJt7gi4HQNAXNQvH20Kn4jelDbMCKOmiYXiQ7ZxIpVCEfsNwvSAcc6LGZMpnh0xjPiy7fZzG83tuHGly_dGnIvlkulbOgmnf_uy1I2aLpVHbO37qTYRxdeyBcIwaluhAx2D1soaufXqYjllp1s4qqtB5vQTVinKcjMWjhWYk6IKvyYyFWs7kMOEeqdLOExwTSbecimKmiuUas_5EKaV4SvxoTqahNTYUvlRp7IuKzALhgQs2v4_lr_2zL0gY7U-RtAER1Jt1WI8x0NzP6Rh4XyuSkruXQoUqXY13tAZ2MsosINP9MSDKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
