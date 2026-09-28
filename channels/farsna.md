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
<img src="https://cdn4.telesco.pe/file/B3xCMfUgM297WjgXcPM9xwlIUwNE29zV6E-1yljg_mk2E0k4Rgm_hx0V0NNPweZS-Q4Wr7l7cHENF74ZZxWtHydIWTBtTeyCYoeat_eRkFJnl29wynAXUIuv5J4wvncj-oi_rTRHVMJpP7jaPoNB1vboItS_FLQJf7yP73OL26OuGG7_WTvpBrq-gh_PwEjf495RaUsU_k8C9MwsJ9ZYBSZ5iQZ2UD37-BwNcowboxButyiv-1GdTI7nP-fDAuPXncY-fgPPX0MUZ8vPvKfNMwMKSsXCS4CyUXtWCA20nkz-DhS0wlnVf3fpHCvqkxRutTAM-JvUL-QKALsUPLAy2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-464986">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnpkJfr_6IGR519kcQ8TmQf-Py77oVNnhhRp-cggV6bficOhu7tvIQLqNrg07surc3vHCNPhlY6_qTwRHLoOoHCY-nDlhwS7t75KCupKloB6dyzX16P_q6xZhxfAxTDuZbA0MgoVruBiw-LTITUQc5PIu6AxHxw7aKRoDAyPSuk9RgAOJjpWV-DgnNu6zHuvOz7I7jG1MykWPcj4S0CfUjh-JHJCH2iPXMqLijQab6N__Q-qGGycHSiyZZrI4lttJrh1clPdm5McUThO4xipKb6vYZ9lXRQnIBWXTB-FoE-NdQLPb1OgviPqUYQwPeAiUMfVdxOPoS4cTx5jP98wOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز خیلی سبز بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۸۹ هزار واحدی به ۷ میلیون و ۴۶۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/464986" target="_blank">📅 12:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464985">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ced4e753f.mp4?token=cz_TYRH9UvD28iohu9di0CraPHkOLwGXQcuVON17gkSW8elRME5-AORkaPshtQlRenFOPIYWzB8eGvfg1BI41Z5px2sUZPFyb36ldu4mCD1oehaqK77dVESio7U7f9Lp_T47HdLPZDlkm0KnIsh_hCDUwzY_8KmEGeZ05OPoevrXxrUjh_lQheVkpRozIWrGc9XMzmfXWHWCjEPgjnPUi8cO45LyJSmyXPEgKnp6BgujGIjHRbZOLeuCmAcjKhHeUTkrZydUEHptFYexAvp_8QqT-r0ZhS9zKLKA6nfw16OctghD5RlZnCw0PQe26Piz-1AJJAnle39Wzk34RBfDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ced4e753f.mp4?token=cz_TYRH9UvD28iohu9di0CraPHkOLwGXQcuVON17gkSW8elRME5-AORkaPshtQlRenFOPIYWzB8eGvfg1BI41Z5px2sUZPFyb36ldu4mCD1oehaqK77dVESio7U7f9Lp_T47HdLPZDlkm0KnIsh_hCDUwzY_8KmEGeZ05OPoevrXxrUjh_lQheVkpRozIWrGc9XMzmfXWHWCjEPgjnPUi8cO45LyJSmyXPEgKnp6BgujGIjHRbZOLeuCmAcjKhHeUTkrZydUEHptFYexAvp_8QqT-r0ZhS9zKLKA6nfw16OctghD5RlZnCw0PQe26Piz-1AJJAnle39Wzk34RBfDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مسئلهٔ کنجاله‌ها و گوشت‌های فاسد در انبارها را رها نکنید! مسئولان مربوط باید پاسخگو باشند
🔹
۶ هزار کنجاله وارد شده اما ترخیص نشده؛ محموله متعلق به یکی از شرکت‌های وزارت کشاورزی است و بخش زیادی از محموله هنوز در واگن است و تخلیه نشده است.
🔹
باید…</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/464985" target="_blank">📅 12:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464984">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e1645a3f.mp4?token=Fca2v4TrruKFMiXaYRGHP4PaG116x-8UcM-9nYyg0G-CUEEYhm4eZEcMZK3LE9MDMZ5Ajzo5iLtJpLCcGJwNQT4Cy5f0HWcy-9zNwy9OJ2y-z5WmiobeXH9A8pTofSaPaC__HzcXoxO5qzaqm_rJsXnmVbmpjPU1EV5UAwZ7JV94URsXzfnJWJfdi5uch65AiRXhWSlXjqxyCYrK1dhktwNQEKpXDIWxabjyf5WiRSYLS6mBGlCwzvsmIYizTCBGpLPtFCgwvox1n7MYsOzRGpZfUJ415bYUi3wz6tgf01mQ-iwMpq87yGTdGXVmfW4Fw9cU0IZ04EDaOn80-srqWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e1645a3f.mp4?token=Fca2v4TrruKFMiXaYRGHP4PaG116x-8UcM-9nYyg0G-CUEEYhm4eZEcMZK3LE9MDMZ5Ajzo5iLtJpLCcGJwNQT4Cy5f0HWcy-9zNwy9OJ2y-z5WmiobeXH9A8pTofSaPaC__HzcXoxO5qzaqm_rJsXnmVbmpjPU1EV5UAwZ7JV94URsXzfnJWJfdi5uch65AiRXhWSlXjqxyCYrK1dhktwNQEKpXDIWxabjyf5WiRSYLS6mBGlCwzvsmIYizTCBGpLPtFCgwvox1n7MYsOzRGpZfUJ415bYUi3wz6tgf01mQ-iwMpq87yGTdGXVmfW4Fw9cU0IZ04EDaOn80-srqWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مسئلهٔ کنجاله‌ها و گوشت‌های فاسد در انبارها را رها نکنید! مسئولان مربوط باید پاسخگو باشند
🔹
۶ هزار کنجاله وارد شده اما ترخیص نشده؛ محموله متعلق به یکی از شرکت‌های وزارت کشاورزی است و بخش زیادی از محموله هنوز در واگن است و تخلیه نشده است.
🔹
باید مشخص شود چه کسی کوتاهی کرده و چه کسی تقصیر داشته. باید مسئولان ذی‌ربط را پاسخگو کنیم.
🔹
۶۰۰ تن برنج در مدت طولانی در انبار مانده؛ صاحب برنج می‌گفت که ۹ میلیارد تومان به‌دلیل تأخیر در مجوز به هزینه‌ها اضافه شده؛ این هزینه را از جیب خود نمی‌دهد، بلکه قیمت‌ها را افزایش می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/farsna/464984" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464983">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPAIQC5XtLa5PD5lvscbVswiN003Jm9qBFOOLZ-rtsDmlMvNHrrNKGGMqAGoAOxF6OTH0r6VtnDUI891tcdsO52CrSy1CzgvakirfirLnGzi9bhDtyiw5EXwsyifN0KK5-pvPcpkkh8THE10JUyp_yb5pLoQ_G3chxNel87kTIEJXJKN3rmIfKBGrOuEeKzPU2fodHA2VJQ6vSweG7VDPkemwRmGqSPzc8STSQ2ORaNmrMHGMJgFT6FNCGn1vLgmW24sM0Rtif7D8KTxt5MUoBfLVWoHZ8BMO1qVCikbx3gGLxdCilbddeebb0hajmVDBCfh8bLvsSwq9e9lwJRbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو در سفر به امارات با بن‌زاید دیدار کرد
🔹
شبکه عبری کان: بنیامین نتانیاهو، نخست‌وزیر اسرائیل امروز در بحبوبۀ پرونده افشای هشدار ابوظبی دربارۀ عملیات طوفان الاقصی، سفری به امارات داشته و با محمد بن‌زاید دیدار کرده است. @Farsna</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/464983" target="_blank">📅 12:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464982">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0ec72a01.mp4?token=hzKr1YCPT-ojOea_9yb40PM1xw-X2OvOKuAPxGH_Oycy0rTRajS4-NJ0AaLFRH_Kk_CZMxEGRnN3I-hV4q3KC3vBNfFkgFsEMgObzvR4DgGHgloNUxQNgwJHpCQyquoSmryRUrng7YBrjQ-FAy67TWh_AhvO9FaKLXdxu0l9n6fxvjwc1you9V5retQ5WMLDlDn1eynVZa80WzVb7mV63w0EDzfwwcvbU-zR5ZypA6i1WPVmjAg6Gc0acypnPtANHPuRulZsake7ceC93Kn38RwNyaJ3rAcYje38V3hDoTMaqvQr3AlSwRl-ue7xQAZCJ7rTLfoEiQzNlR72V4iFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0ec72a01.mp4?token=hzKr1YCPT-ojOea_9yb40PM1xw-X2OvOKuAPxGH_Oycy0rTRajS4-NJ0AaLFRH_Kk_CZMxEGRnN3I-hV4q3KC3vBNfFkgFsEMgObzvR4DgGHgloNUxQNgwJHpCQyquoSmryRUrng7YBrjQ-FAy67TWh_AhvO9FaKLXdxu0l9n6fxvjwc1you9V5retQ5WMLDlDn1eynVZa80WzVb7mV63w0EDzfwwcvbU-zR5ZypA6i1WPVmjAg6Gc0acypnPtANHPuRulZsake7ceC93Kn38RwNyaJ3rAcYje38V3hDoTMaqvQr3AlSwRl-ue7xQAZCJ7rTLfoEiQzNlR72V4iFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شروع بی‌‌دردسر والیبال ایران در ناگویا
🔹
تیم ملی والیبال ایران در نخستین دیدار خود در بازی‌های آسیایی ناگویا، بامداد امروز مقابل قرقیزستان به میدان رفت و در دیداری یک‌طرفه با نتیجۀ ۳ بر صفر به پیروزی رسید.  @Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/464982" target="_blank">📅 12:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464981">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaNe5ehZ2yzkMLr7XdI8qvu_bGiPEZYte6fkFXuujOLxGuiF9EuZCvqECAVhKpA39jd4lHTlGEDA4LqIWXZxFJLGOGKVmnYvN-lojfdNDR1TufKk3aKv-WW6aE-WUQr7d1np0D5cPnSo5qUjhq-Az83_apqiZqrHgzMOwN7qBwMq7UFTcKoNMWExTHtd2XGH__D7HPZQVMpI6h-aeYmtTuDRvKPjyyL8jB5qzFbzoSwgBBscQMixuVb7lvDbWiO3hjbUZ8EdlKO7La1YuXPOzMbqQHtKAxHbEPHHD0UYpnU8HE4ltoauAVHYwRQkV7BcGr7My_R6kMNwv-_wYlCYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت‌ عراق در محاصره؛ مقاومت تهدید کرد، پارلمان صف‌آرایی کرد
🔹
بغداد با موج فزاینده مخالفت با ممنوعیت پروازهای ایران محاصره شده است؛ مقاومت تهدید به قطع حمایت کرده، پارلمان، کارزار لغو را کلید زده و خیابان‌ها ناآرام است. دولت الزیدی اما می‌گوید این تصمیم برای فرار از تحریم‌های آمریکا ضروری است و در پی گرفتن معافیت است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/464981" target="_blank">📅 12:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVcHWpo7H2EW25eXZg6IBsMK6hs_pYYzj6cWhCgD-iqpkepNEvTDWqF-vrBEA4SMqbtMiLsu06nHaPtj7Vm6NVgTSGBaG2-j08aEuNCKwKCjqZkDvru-WUpxKI61ZjjgkQapTSC_bvcqCFGzpeK7WfxJ9SYoab9M1bx0rsbDPev1SfASa-wU6NIl_92qoIgSzoV55vMdJYID5CMtqa8LiaBk4fqZHxPl2JAWauESWZmm7oMiO3GEn2I4bT1YVdzNMSajwYttN7kF2T_BRxNt9olN1y8qwR4ZcXrDy7IGQGdB1khpeEE3CwkLRkUJ_ZUW4E4k0Rv3Zea21YYP-gdvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUWx7pOVvZFRWbLjm3uWMCaEOKn-K9po8_QS0v1JiHmyprv-vbz7TdiMmXl8NCD5S4VmBVeOANJRfQ7U5zIoUWg8R9RZXN_xuOGO7lENAoQnWfAOdhF5qg5aqdQ8gmqLvp2NfD_cX8ThxiwY3AB2qBbTZ6TIPvkY04zH812v7fieuNvjWYF2EZ7pJnaNvhjWZpNwj_2rETBPlAdhkU-0xVUTXgTGrRxIrONBPgcBSUU1M9EfabfAX2q9k2NbJ6Qai4js6HES3EucPH8VEgEDjAkexul6nnK0yfh5VyhVqj9Fprd2682T-ZBE-Y7XxthTexPRPd-2GBuapO94kmCDFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfw0appzPnuPek_E6UeaRPWKtiyMoJEjS87plowLz9dirgITMQz0PfH8tQ0TBLyshdzrh4NKo2zf1MMKS_-xTt777R74gnF_ONEc-4aMoDWrOi4kMOiMOw8TJN5yuLcRoA0X89R8WPciBQP5jmTLr_rbiWs5eXcUFCAfemJC9Mo1ORz7O-pVWDRkt0ulHHkU6Zd8a4OkFdOYmfttd9QQKSL8MITNIzaE5MH37E7WhqABoUgtUVpKpyl93SxE6U0x8l6oFryZmwcxsOX3F4geqVoGWXOcp9tOWTpeMVwTWxHcAdw8KpVDOY6IXC5QNoo9Jzh7b_yGHXc1X2VCvRn0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbKSw4jmbRTu7KT6Sx9vy-nWqvItC4ZKQEaxa0cV4El8KGqubauMP8matqny0qbvdLXxzO82QZgnuURbYRBaMaHZPyRaCEcaoxKhX0UNnLO7SfF5uYGUwj17Vrc7GboQJKOCEDv9SnfTBAsL4elE1Nt-N4IZdJ66_R0FhFMONagDeQT1OnDKR2_4c-JpLCVACi3-TsMRfLs8dV5OuuW4FY9IYw8LmOEuuw1lq1zC9mmU_iAhpYWvLpLWVDt4l4Pa1Rh-oXgUAHeM06M0cYgz4JELKCpEm7EKF6N_ubmG52BJhmf_ISuW4LURVX9ygvQ0cPx4X6YgKbQeZ7B2SIRE2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۱۴۰ هزار جان‌فدا در سیستان‌‌وبلوچستان به میدان آمدند
🔹
در این برنامه که صبح امروز برگزار شد، ظرفیت، انسجام، سازماندهی و آمادگی بسیجیان استان که در کنار آموزش‌های مورد نیاز قرار گرفته به نمایش گذاشته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/464977" target="_blank">📅 11:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ثبت‌نام عمرۀ مفرده از شنبه آغاز می‌شود
🔹
رئیس سازمان حج و زیارت: ثبت‌نام عمرۀ مفرده برای پاییز ۱۴۰۳ از شنبه آغاز می‌شود.
🔹
میانگین پرداخت زائران ۴۵ میلیون تومان است که رقم دقیق با توجه به انتخاب کاروان‌ها به زائران اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/464976" target="_blank">📅 11:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lc7gkGbJY52PB9kL2fWai7jfCGmPN8BL9rNbAZZOlvGSX4aScR7S1-XTZnXvqAReBvbYCZHSXSq_ffewOk1yewb6RH7LXvIeT6qxnc2J_MMineWMZBsvd2PM3oHMUuqEFjDGR31etf0hdvJRohfa3xB3-w3FI2EdIDGUrQ4BD1QdksfuZi4bxORvK8XSc6e3_I7c7DS5FE0sbtqrrlyxCtXhNimGLdyXQUjldUpQLKDdzW4PClNM3VgMEqQ_M2d8WJOe4tXSG2Qe_cJXiVJsn9OHf0Kbz1OJDe42w403YD4eiuZPoghrrvf2_OWa5xcXG8TAUSLA6pOm3lM2HasAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNTLgrCcl4d_ApVQ4HWQj5EMEId-cOV0ldi-W0rl_yF6mpXIrsoWBdymyU-BF-xjKm6g5vN8AINc1EMatdfi9DHBNwJaN9D7_PUCWDY74Jc1oZ516Ahm2iq4yFIDmYELRKhIpcUxFbLpFWnRWyqrRV0uFC_KPvizBi_Cl-q9DQ84MwUDY9zqw1EjFJT_O554naeVgQe6anC7xSzqkGBlDWiLUPk87ipgrhvssfKML6iGShNmDJc5sQf-yy6YQ-EbdO2jOLbTUCCZVu0h06E42nWC7aFaO-rL5kfynrNqwR6pQgaPdO_FURj6L2QUjrh7W3KgzRefHjksNzgw6nqjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnIltablcRrvUfpMRUx_XynnBvuq612Ks4Um9d1NQSjaYAYxsWfskNdhydzT5QWc_gT6_okdpYUImc_JUyRaIPIEuyJ2yH_uIwHTASVwykEbfD8OXTHj0rZqMwBuaJlK9KoRoR8Bczff9am3I_W2dCq9ADiZpgDwspwBDsayybsBKvcEebN1BHZrtAnXdXgHn8Yu1aZRzZcU_3bKWwgB71GQcyJuaK-TUUgYjsuAcE9H9IDSbt9R-H8wUvr97yzOmYmfyWCzOufPi_rPdhRkTjqd1d9iKG2zBzH9H8CbxlozriG5ikqLEM03dI8gSs85fxBtDzwlkWs5a4LkL6YDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-BXcqTVCh9WpDcPwVoXRCjIH9hMy5oqvBUv6y7FDzhj8Ry4Voh6TS_I7w2FOe-yObvwqfFM90BUOP4jVc6_QpIqDxk9oEFNMPcL3oUtaI-Cq3y7ajNhqyUE76AvOM1jqMWbzmgrCTHTho6_g-osyuF4r0rAN02UfU0hDI91JP904hMiWInNfdnFicLL89mWLyDOvS4P-OlK0m6Ie2P9Mwao3hvgckVdwA_2ft_bYujT3Qq0wO5GBgKjmg4OytPX1JJ6enBZPiCQ7dt4miPNugJQqLnZ0tOLho6r68ReWHNLz_vXMJeWWTPk5MhjfyTrGqwPvInnDpzd9HPr0KfCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p--9coLk1ObZjcxaAwHrIeeKJngXR8Q5Y-MAN4zrcxdKfnjkeH9Ns0lQmmaTT2XIRC-MbPO4gMjngqQTl-DRWikud08TzbeR-1KjtwtPEUqnUpWp78lAtuwoCs9cbpITgQVmu9RipIW47Fy5Cp4Ch9VQdBhDXvUiHZvdnVDcPD3_6bTqAgqf1AqCdhSOmyxd0E1UhNhjQDEF3FZgHD2I8GsVOsgnwfFVYHvOMrPeUo2SwkYFwnPOFNUWKFuK5QyjV9w7Hi6_M-paWWudYlZpl69cYDRByR-hBhsS3zfXRoM1UaS_qLySrDuDx0poU62-QeV2QZw4TOqRrQAvFQi5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2sIl_4SX_X4AgOiyT5v1wiaoc4xy1HD946c74_93bZgFpjUbeE6JQf8O5Wk_o1dQdKKvMHOnlAjDYUf2EIj0zj6RwUnrq8KofABDlPH14r5J1DdfLDAijXg4QTAx1fyE3nxZPYz5AgK1BcIRF4NKZGAPcTQnieodzzeHzklAJDdlrqRVyYFveDR-KUaUYxcVDe_eHY31cm_G1f8COL6kT1qS2lt_TZ0T4vqnQw1sLzpxebkTBxOa9Nr0peGYwnjfIq9DTJr4eFk3PveBEfK2zAXCiKV8SZwM90WK5EQQ9hydzBNWYbZy47PZNqBjcL1wK4HS5Rdu5-EMmOVFFTq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1ySclKAWLC_DabkMVbpTsQYrxqA7TswLIQThggEiH_Kh42wWBaO5VGvLnqvYTlja4JkK4NoXmhdv8RY-KzxfjJbze9ER7juAhUuoVz919s-2BsfEJsuKDoCyn1q-T3YMfyGoejP4dBAcYoT8kaYBeRBkqgZz52vO_XMBx-QnN8Cm330ycQj2iq_5aXk3NpRCwVOUCnHmK09fXZgxbnx-DLL3a37gQ-jft4rZwHfPGNEu_dw3Z7H1faD7L2ZjZa73ueIIxJuenH4NNXVTfXx2F5DndsZ17-OtSQTYA_ysYfoaCE9-WgQJaRpY7_S-QQf0j8t0uwFZMZG8WtjygNv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Js8nZG_yJoIVIWKgYDWXk2T7N6mvL6ASg2dYNb4lNFdeUl4SAujytd_lSW205lgOfaoZd7gORZ8U3sJCvkCT5peg1VzIxjERuYz31QIErMDI2h43QIVqjRC8brYRpMZ3Gne9lf7NMQsB2pSf7TaFIovU228qsQsB4BZ40Np5DPU3HiMg8ft57vIV59gNRbztkLrM0Sc7-rcWnBHwl43tmPUOEBObQRpafQwy1ZuHjgxPcgNUVKSLe_1je4HlqrDt5jvC71kurIJKgNbhGY2AVl15lyR_o_TrbcbyQtEOUcP60ZJ7JoKfe5EWv5lQegZuwayvidpo8mQxkuouHTmAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3ztX0GOUShC3CKN4_Jxel1iUAVRu71l3BXlwyYlSQmyY1zJMYFyglWad1gGR3nZkUyKHaoF9mmdzvMU2OheeOjASkOkx4F8dDokB3DUUactNDIqj2_6gekqUQVQJfT3tvwon042HygqRzdqn5WTdGj4NWsmurVwChWIuiHXy2WgcYcpUt6wSOVW11LsXD3mILjfuZGsXxjS4FwB9h6s2Wv8EDopL-rieb0L-Z8ZCzchCFjGG1cbAJKD5QKGeaBv_7zIv2YEuAGWtFGFAkAulFVe7or3d5wFZuV1NjeIUbQ_SbOOhjBkcQrD6S7JhLxT7ZYShwVDAN_u9FA0QGU6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q95HVKqSdljfgFQAeCE9Ev3DElsV-7u_GOjMRbxTX83O5Q2Bk39Xfo-s0ESXJ-5IOesmPr4NiF1O7nhvp2dvEstog3n9_z_GvB-uyL3zJArxYja-z3TEMCz-dM3h6eDm785zmQLxIuRJMXPNYOSrJewCTX8U0dKDCbU2bIDRQVq5tPeSCopx4nNAPSTb2_IadI3yNxzr_JCc_5USWtcbvSds8LHu_riA5z03RXv7Ne55urtb4jW0bjqqZQxOyl0O6NyP5SYAbeqAUg-Rufud55qFhNA0uoaoSSboDpiazWdihiwiop5rK-1N1keNeTrvD_8eI8DWnM4hrf2crfYXrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصویر منتخب مسابقهٔ «عکاسی نجوم» سال ۲۰۲۶
🔹
برندگان مسابقهٔ «عکاس نجوم سال ۲۰۲۶» مجموعه‌ای از چشمگیرترین تصاویر نجومی امسال را به‌نمایش گذاشتند و جایزهٔ اصلی امسال به علی العبیدلی از کویت برای تصویری با عنوان «شکارچی آرام» رسید.
🔹
او در این عکس، سحابی تاریک…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/464966" target="_blank">📅 11:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464965">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef8aa9c35.mp4?token=UejNmQaQjHxOQD6ZlKJ-GVhXenrwnn4btw28mhO-kfV1jXkr2t9XRchGW-6KSxobV4FX0NVHRZjERDl9l-NgW30vq-YQtRDr3-KqjMe7BN4jBbW2Dz6vdejSD1-9OUBTQHn9jZAgVzFEySG07ShnPc2KIjRJnPaJfz-cAPWsmyuBQNjTPQduRvc4AHCe27sejwwWm2i8swIPpC8g6LVX3HYIySANaJLoftf1kijIG9SZ6wMz6pi6b7T_BNofkOliEr5Ae5Br8JHhaZhk4ZKTD-zXNF46a3rokQl1ZVMVHalYq4J1lMpym3cBpVH1AaA9UpoovsbmgZrGzBvo_7ov0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef8aa9c35.mp4?token=UejNmQaQjHxOQD6ZlKJ-GVhXenrwnn4btw28mhO-kfV1jXkr2t9XRchGW-6KSxobV4FX0NVHRZjERDl9l-NgW30vq-YQtRDr3-KqjMe7BN4jBbW2Dz6vdejSD1-9OUBTQHn9jZAgVzFEySG07ShnPc2KIjRJnPaJfz-cAPWsmyuBQNjTPQduRvc4AHCe27sejwwWm2i8swIPpC8g6LVX3HYIySANaJLoftf1kijIG9SZ6wMz6pi6b7T_BNofkOliEr5Ae5Br8JHhaZhk4ZKTD-zXNF46a3rokQl1ZVMVHalYq4J1lMpym3cBpVH1AaA9UpoovsbmgZrGzBvo_7ov0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد خطاب به داخلی‌های طرفدار تسلیم: هیهات!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/464965" target="_blank">📅 11:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464964">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56daa52e9.mp4?token=W1-vV46C0G84BLCCBNje-Jq4sQJPhmbTSflQpTknuiCMzKoHJmETMcYgU-GReAF3rbYahKDj41yd-OPFmu0DMAlNnvpJWGxZi8p0oywbTpqFOI4iOmKId47w-mR4m_a1KBGgkMpMwpAmNK_eVaRWxM-OfRi8KK6UJu9XFeLfjSWA3z_ipvR7vGLG4j3OdypOcn1szKli04FHIM9bjm5JMoOBLwCuL1hjDTtvkgcEaSWmvCOzM0Fz9odzKUXzmQ9r8S7KniLFGVjZJjrNlyS8segbfCEnDTJ-2OHupKnEskbObof2zk-mXWs89hcnb0Mx11fLv_vzWzSJxwY--mb4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56daa52e9.mp4?token=W1-vV46C0G84BLCCBNje-Jq4sQJPhmbTSflQpTknuiCMzKoHJmETMcYgU-GReAF3rbYahKDj41yd-OPFmu0DMAlNnvpJWGxZi8p0oywbTpqFOI4iOmKId47w-mR4m_a1KBGgkMpMwpAmNK_eVaRWxM-OfRi8KK6UJu9XFeLfjSWA3z_ipvR7vGLG4j3OdypOcn1szKli04FHIM9bjm5JMoOBLwCuL1hjDTtvkgcEaSWmvCOzM0Fz9odzKUXzmQ9r8S7KniLFGVjZJjrNlyS8segbfCEnDTJ-2OHupKnEskbObof2zk-mXWs89hcnb0Mx11fLv_vzWzSJxwY--mb4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعلام «حادثهٔ بزرگ» نزدیک پایگاه میزبان آمریکا در انگلیس
🔹
پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست خبر داد و اعلام کرد که شماری از خانه‌های منطقه تخلیه شده‌اند.
🔹
پلیس شهرستان گلاسترشر انگلیس امروز…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/464964" target="_blank">📅 11:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464963">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhw0b0XgnzKg7HkdOp-JNRVm0rmPn_5JC4H2PXNVj_1xeZAgzNSjUkEP8DhOdcbY_ynG7UB7u9x4i7IGAlPwbaiOQvbw2I_3IcgU9xQujNxbPEkJv6Nv8EtgxvF8TJHZN6vqH1ofn16trtRznB1jDXpWihcJhzVDBFKNjU2NYAs7P5BaT7jPK33Hp_GjzPeV1ge1l5GNNBsOYMoLqFI9Yu0GXykJgo7lQuJrT8wq6l1dAp9sYqkIzPGvLqqE8dR8sOchUH5vhR4MGoSo1AAJzc9T-olFXe9789C9iXgGzC6s5--H7XMDK_Ih6pnacnhpgSomHkXABBlHfPMy2-na_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مداح بحرینی پس از ۱۹۲ روز بازداشت آزاد شد
🔹
۱۹۲ روز پس از ناپدیدشدن، سید احمد الموسوی به خانه برگشت. آزادی‌ قاری و مداح اهل شیعۀ اهل بحرین درحالی رقم خورد که خانوادۀ او گفتند «سید محمد، پسرعمو و همراه روزهای بازداشت او پیش‌تر در زندان جان باخته است.»
🔸
سید احمد و سید محمد الموسوی بامداد ۲۸ اسفند پارسال پس‌از شرکت در یک مراسم مذهبی در ماه رمضان، هنگام بازگشت به جزیرۀ محرق ناپدید شدند.
🔹
مقام‌های بحرینی دربارۀ سید محمد اتهام جاسوسی و ارتباط با سپاه ایران را مطرح کردند. سید محمد کمتر از ۱۰ روز پس از بازداشت بر اثر شکنجه جان باخت و پیکرش به خانواده تحویل داده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/464963" target="_blank">📅 11:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITYbdq0He6OqGJDEpD3B1hhLALKh_D7uvpImM4CvjBReyIDZo9ClU3tBvi_MK7zuq1I-Upk2Tf65IhNqt0EsLQ_scQYBHAuOFFZpQL62qu9b4SzZUWv9H6t5x9GfseTM3G94bUUMWUrr9bSpYLzuiYDmbxQTQHxS7ovOYnQeTBpF7qrOZvEkcg7L9IXZcCBJySogQfl5uDq63fxb9YaRtiJ6FT2lrhVV9ZXnj57zXqFONBJ0WKt1mEaivrFHDkh_N34sOtRLSyia1DzwQlo1_bweTZLuD5lgC_-_46U8C2UxWbti24GpLxeFKfoLX4BnK1adoTduS3jG_42vUnvlag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر منتخب مسابقهٔ «عکاسی نجوم» سال ۲۰۲۶
🔹
برندگان مسابقهٔ «عکاس نجوم سال ۲۰۲۶» مجموعه‌ای از چشمگیرترین تصاویر نجومی امسال را به‌نمایش گذاشتند و جایزهٔ اصلی امسال به علی العبیدلی از کویت برای تصویری با عنوان «شکارچی آرام» رسید.
🔹
او در این عکس، سحابی تاریک کوسه یا LDN 1235 را ثبت کرده؛ جرمی که با فاصلهٔ حدود ۶۵۰ سال نوری از زمین و در صورت فلکی قیفاووس قرار دارد. شکل خاص این سحابی نتیجه وجود ابرهای متراکم غبار است که نور اجرام پشت سر خود را مسدود می‌کنند.
🔹
العبیدلی علاوه بر جایزهٔ ۱۰ هزار پوندی، مقام نخست بخش «ستارگان و سحابی‌ها» را هم به‌د‌ست آورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/464962" target="_blank">📅 11:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
نمایندگان استان بصره در مجلس عراق: ۴۸ ساعت به دولت فرصت می‌دهیم تا در مورد تصمیم منع پرواز هواپیماهای ایرانی تجدید نظر کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/464961" target="_blank">📅 10:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72e383477d.mp4?token=SrGMAEbtWU_4JR3Zoup-ai40oXu5d_aSeNeaxH0Eci-ClIwCu2lC6O5zPHivSXoQR_wbiVCnxmvDo3nc7afHgpje4dGrS3vBPUIHHh9bJsGsd6eK6NAEMCfT0GJQjT3IcPZVprGpP9fSom-YKMqKlIO3OVFwsoze-hw12eI9gHFUPsxAb97CD4IVyYinTidVt-uYHXN4CY0NuNHmm3dDT27o0bD7HvsuQfH7hnCNeexVuSCM73OnkdUBnSrJnU7ufpafh4Xg7W1yI-_BtA75KYvKO3tpCZZBtk-w7xBJJUy5YHPZC9bPfpXrCePEk4Yhnp9Rod0J6-ashrPLQw3pNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72e383477d.mp4?token=SrGMAEbtWU_4JR3Zoup-ai40oXu5d_aSeNeaxH0Eci-ClIwCu2lC6O5zPHivSXoQR_wbiVCnxmvDo3nc7afHgpje4dGrS3vBPUIHHh9bJsGsd6eK6NAEMCfT0GJQjT3IcPZVprGpP9fSom-YKMqKlIO3OVFwsoze-hw12eI9gHFUPsxAb97CD4IVyYinTidVt-uYHXN4CY0NuNHmm3dDT27o0bD7HvsuQfH7hnCNeexVuSCM73OnkdUBnSrJnU7ufpafh4Xg7W1yI-_BtA75KYvKO3tpCZZBtk-w7xBJJUy5YHPZC9bPfpXrCePEk4Yhnp9Rod0J6-ashrPLQw3pNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: سرمربی جدید تیم امید تا دو روز آینده مشخص می‌شود
@Sportfars</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/464960" target="_blank">📅 10:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnyynQyQCbA1qpRhfBguy__Zx7HMKgE5SZVtvj_iOC_1EujiwIqozonjIxrUcI6tSQigBz_ZZgUZRGFIWD60yRZjOTorxdEwDxOyo7yLab7CxyOG1cWs1gdcQAl9xxu-DxuggZCo_o0QbFb5tpDfVy8uPS3QW-_8_kCq85TFUauX5J5nNqws6AEgScr8SWLRgtbblMzrPPGnA0-Yb_EvUcyWTA5MAi1WmAvqzB1AIFs8kKtig-nj3C612xJSrXWCmIor9MwoUB0Ae4wC_2MOams1LgqpxdYVAd1xmlyj_sP_Xxx7gl5ZsxBZ6Oo4K1MHmF7rDKVxTyxOY9FTnCKxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت همراه اول از کودکان بازمانده از تحصیل
🔹
پویش «بنای مهربانی» با همکاری سازمان بهزیستی و همراه اول برای حمایت از کودکان بازمانده از تحصیل و افراد کم‌برخوردار برگزار شد.
🔹
همراه اول با استفاده از ظرفیت‌های خود، از جمله کد دستوری ⁦*۱۲۳#⁩، اپلیکیشن‌های «ستاره یک» و «اوانو» و باشگاه مشتریان، حدود ۶ میلیارد ریال کمک مردمی جمع‌آوری کرد.
🔹
اهدای ۲ هزار و ۸۰۸ سیم‌کارت دانش‌آموزی و اشتراک رایگان «آی‌نو»، توزیع ۳۰۰ بسته لوازم‌التحریر در سیستان‌وبلوچستان و کمک به تامین بسته‌های معیشتی و بهداشتی، از اقدامات این پویش بود.
http://mci.ir/-ADTJ56
@mcinews</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/464959" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6oTsZYyVx6TWfT9JCzIwd16Artmse_0zAy1Yco1CjbLTkz9WRokfyzcmHk7M3vLEGEnSNZXG3xyb8ETxIU9HxmwqcVNBcYDUCmzP_CHamKqi-wU12kGSGM5FnHAv1CrK9nX2Cz_NpV3ZE-w13qTc9aTQ_P5s_h33yInpPmxtLfkySXIyD_aFDs4nLZRu0rrirrn7pWGXwTPJ_FAHIuiDu9edJCb1KGS-QiWfqqQFnIiUr8qAs0kLpob8iSf10kYmZsFfx_eJCALATaBUszZc9h_6K-BLdJvpU6mFnc1pwDltadpvWH8WxKRpInToY1IsVW87PUsom_DYVQ5SNXksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کارسازی ۷۳ همت دیگر از وجوه گندم در بانک کشاورزی/ پرداخت مطالبات گندمکاران به ۳۴۶ همت رسید
🔻
بانک کشاورزی با واریز ۷۳ هزار میلیارد تومان دیگر به حساب گندمکاران، مجموع پرداخت مطالبات کشاورزان گندمکار را به ۳۴۶ هزار میلیارد تومان رساند.
🔻
در ادامه روند پرداخت مطالبات گندمکاران، ۷۳ هزار میلیارد تومان دیگر از منابع مربوط به این بخش در روز ۴ مهرماه در اختیار بانک کشاورزی قرار گرفت و این بانک نیز بلافاصله فرآیند واریز وجوه به حساب گندمکاران را به انجام رساند.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/464958" target="_blank">📅 10:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464957">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/464957" target="_blank">📅 10:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464956">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkLCGJY5VnTjxyWbxaxZXs-M-0-upII8o6l2ZvCNf6rGDcuRhpXVCL3CmDIK_xemCRT9i3t5yeJCya6VndpEDbeycAq7-YbKc4q4NhUu8InoVUA3CvBHZjZIFtBXb37LbAbZaF3I-L_Kdm8a1wojqYhB4gJLVZBehyBGfqwB5sw6dWnuObP6MvLCAmxFeZ19nwZWliOXTUDKvy_OY1KYeTHZBIXSBImBzudqN8YdKraZK-OvgBUlZa7amTtZYJm7DNDbXK9cZiHIxrMHbVeYbB6DF2ZOAlmZ6djLNK6eAVPE9P6N7OJCJcOYktI75k2ZTTwvGaByVZkHdxOpByqzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریادار سیاری: برخی همسایگان خواهان ایران قوی نیستند
🔹
معاون هماهنگ‌کنندۀ ارتش: دشمن نمی‌خواهد ایران را قدرتمند ببیند؛ دشمن، ایران ضعیف و تجزیه‌شده می‌خواهد و منافع خود را در تحقق این هدف تعریف کرده است.
🔹
اگر به کشورهای همسایه در حاشیۀ جنوبی خلیج فارس و مناطق پیرامون دریای خزر نگاه کنیم، مشخص می‌شود چه حمایت‌هایی صورت گرفته است. روشن است که آنان ایران قدرتمند را نمی‌خواهند.
🔹
هنگامی که به برخی از این کشورها گفته می‌شود پایگاه دشمن در خاک شما قرار دارد و دشمن از این پایگاه به ایران حمله کرده، درخواست می‌کنند که هدف قرار نگیرند؛ درحالی که امکانات خود را در اختیار دشمن قرار داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/464956" target="_blank">📅 10:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464955">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcwUhPpKo5DMeIdw6KGmutbzzE0Ij8YFemm9-bXQEaWu8419hefEpm1s2gphXvFQ_e40rcEw2aIu5wB0tsfPLd9vv0kdg8Bs7qycDCnxoo_zXgSpurer3BPq3loYUq6kdGv_dqh11hA1a1UvFvZhS8rjSklpJJsVGm1KjZXSzj8CxjGIJHAEoJEZ0eOveZzFWdfrU84XBqESJcaViuORgNn12wMGOw2q-S4dm2RsWFgWfOtjgwHtsN-ZG2BcJKeZKlU19mrxIYHcY2PsLQCVl3t2bKnkUIiqaKXWQChFgL4QzSc4AuUZNvLdfhpmwYP8N6zKCx_Oln007fj7Mro3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی مسافربری با ۲۴۰ سرنشین در آب‌های اندونزی ناپدید شد
🔹
یک کشتی مسافربری اندونزیایی با حدود ۲۴۰ سرنشین پس از مواجهه با شرایط نامساعد جوی در دریای جاوه ارتباط خود را از دست داده و عملیات جست‌وجو و نجات برای یافتن آن آغاز شده است.
🔹
تا این لحظه گزارشی دربارۀ…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/464955" target="_blank">📅 10:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464954">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bc46924e0.mp4?token=GhMBqx3IGpe3xeshivaDqDWJZa4CwowKieuTXNDOXvpY0FQdlUNFrlmmFdoDgBBzOsYtbh-n3Soiky6jzLS2zQjx084CqS0u7Tid1Qgs3h_M5SjhJ5hEPXohx1Cj29XOPhFYPeyyfSH93dRJuvl1FQjwGRV1ZmtVhcxeVSGum-yOfS_0kvaAwy1oA2nPLPV_HMzQp7dsLRb3ayIiNKYuMcHRiKlQGngVCoZqv2SWCQRHEIv82XcNOVFDpLYXmxG0HXYGN1lp3I1fSiHmrRSDvD64w9ZpkV3it75sq4g_qTE4GMPsDYXS80U5lfci9LBUv8Z_Te09TSdZqudstBOxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bc46924e0.mp4?token=GhMBqx3IGpe3xeshivaDqDWJZa4CwowKieuTXNDOXvpY0FQdlUNFrlmmFdoDgBBzOsYtbh-n3Soiky6jzLS2zQjx084CqS0u7Tid1Qgs3h_M5SjhJ5hEPXohx1Cj29XOPhFYPeyyfSH93dRJuvl1FQjwGRV1ZmtVhcxeVSGum-yOfS_0kvaAwy1oA2nPLPV_HMzQp7dsLRb3ayIiNKYuMcHRiKlQGngVCoZqv2SWCQRHEIv82XcNOVFDpLYXmxG0HXYGN1lp3I1fSiHmrRSDvD64w9ZpkV3it75sq4g_qTE4GMPsDYXS80U5lfci9LBUv8Z_Te09TSdZqudstBOxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین به نقره بسنده کرد
🔹
رامین احمدزاده در فینال رقابت‌های وزن ٨١- کیلوگرم کوراش بازی‌های آسیایی ناگویا مقابل حریفی از ازبکستان شکست خورد و به مدال نقره رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/464954" target="_blank">📅 10:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464953">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df98e5a9d.mp4?token=EV-G3v6aNUNEl2M0AwZq9My6uophWv64JSyGorIA8ecnkUIIeqZ1VnCvOqRt4Rkd6jo6b-jHIyg4DKfcsuZLAQ_SLODoOfQylvEh8yQl-bCvXB4P9pAaWagI8TpL5p4oUpmLdIFeo_Zlz90qXmHBCvKuiDy1pSGGNDpV19el0L8UmMbjPi-ZoAYLzRdDpJEQiGLhGDDzmxo2cSOXV9zL9bimj9XrH4JI1Xddh3VZ2Mret516zJQNC38lhSozKQ4W5Bte0sIRi9j1Ha8DIcWJNOQr6w3wtzYTl5jKJxAwa0H7Nk_WXQslybZzWM_Bgv3s7CEL3oqkAs2okZh871VSIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df98e5a9d.mp4?token=EV-G3v6aNUNEl2M0AwZq9My6uophWv64JSyGorIA8ecnkUIIeqZ1VnCvOqRt4Rkd6jo6b-jHIyg4DKfcsuZLAQ_SLODoOfQylvEh8yQl-bCvXB4P9pAaWagI8TpL5p4oUpmLdIFeo_Zlz90qXmHBCvKuiDy1pSGGNDpV19el0L8UmMbjPi-ZoAYLzRdDpJEQiGLhGDDzmxo2cSOXV9zL9bimj9XrH4JI1Xddh3VZ2Mret516zJQNC38lhSozKQ4W5Bte0sIRi9j1Ha8DIcWJNOQr6w3wtzYTl5jKJxAwa0H7Nk_WXQslybZzWM_Bgv3s7CEL3oqkAs2okZh871VSIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا آمریکا می‌تواند صادرات نفت ایران را به صفر برساند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/464953" target="_blank">📅 09:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464952">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در دزفول
🔹
فرمانداری ویژهٔ دزفول: انفجارهای کنترل‌شده ناشی از امحای مهمات از ساعت ۹ تا ۱۱ امروز توسط نیروهای مسلح در برخی از نقاط شهرستان انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/464952" target="_blank">📅 09:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f78f27b1d.mp4?token=rIgwt6TTJz_IW4i_Zj0BcGOI4EggfOP0woS2iD5069X2mOc5iVmnuCWfdPu8ni6EC0D72CjGUI7DZtZJWTZN5wCHskT2YnrAx6gKqTXurGOV6tDYbKByjWYlboK__3Eu4cduYYcDCsHcVX8qnO4vaXH9y63mOhyazyHEzNNNsI_9R1zIXbqgWEm3ekA0KyZoVi7pq8-X9pj3hKbQ9KIpVuzNMeu0_9IcpK0tgZp74ddn105qPWnYOBarBxLHjWu9JE52JPu875sE-3TrIVm8_tBigeOnKdDW5uTBT_LU_c2ch4PAO946wa_t48zUDOrhcc45Wwl_5nSYoq7BdV1Xt3lMjgMQ0uFONah3u90bpSHtMsdCCcSzeTasbMcUL5K2v8yxRxKpfcIhdGWWW4duqMHs2S1uQHn-2NryEQJZ1SQvIPX0s9Foqdj5Ppg0IUAocjHMBhAT7ARs6m8j1HmU7IcZF-jwDprtVTB7_NUxmwIwb4_xR9cYOO9RYDemFnyEtDG2ea_4wc7e4Yg93E1M76YmXKwl2RZYKeEdX_Kb_5cIOmEeOup3WRjBNvu01cM7Bdlb5DzLNZelmc2edEAFdHCBMV3rTgmiDH1rMxTS9CrqIlXbJv_nc7FIERn6o9Uugan6GDeCeqQ8ygMKuLcFzYf06jXdIbJesZ4xE7mW0io" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f78f27b1d.mp4?token=rIgwt6TTJz_IW4i_Zj0BcGOI4EggfOP0woS2iD5069X2mOc5iVmnuCWfdPu8ni6EC0D72CjGUI7DZtZJWTZN5wCHskT2YnrAx6gKqTXurGOV6tDYbKByjWYlboK__3Eu4cduYYcDCsHcVX8qnO4vaXH9y63mOhyazyHEzNNNsI_9R1zIXbqgWEm3ekA0KyZoVi7pq8-X9pj3hKbQ9KIpVuzNMeu0_9IcpK0tgZp74ddn105qPWnYOBarBxLHjWu9JE52JPu875sE-3TrIVm8_tBigeOnKdDW5uTBT_LU_c2ch4PAO946wa_t48zUDOrhcc45Wwl_5nSYoq7BdV1Xt3lMjgMQ0uFONah3u90bpSHtMsdCCcSzeTasbMcUL5K2v8yxRxKpfcIhdGWWW4duqMHs2S1uQHn-2NryEQJZ1SQvIPX0s9Foqdj5Ppg0IUAocjHMBhAT7ARs6m8j1HmU7IcZF-jwDprtVTB7_NUxmwIwb4_xR9cYOO9RYDemFnyEtDG2ea_4wc7e4Yg93E1M76YmXKwl2RZYKeEdX_Kb_5cIOmEeOup3WRjBNvu01cM7Bdlb5DzLNZelmc2edEAFdHCBMV3rTgmiDH1rMxTS9CrqIlXbJv_nc7FIERn6o9Uugan6GDeCeqQ8ygMKuLcFzYf06jXdIbJesZ4xE7mW0io" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهی به جز دوقطبی جنگ-مذاکره وجود دارد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/464951" target="_blank">📅 09:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5616927f6b.mp4?token=XBuEHde5crAZVf0z1X99lTtvFAhg5kpHrr2nNJ2QiAWo0omCa0ROyyn0VPpDLF06YOHaRNn9plJrSY4JKdQDuFWlSDKS_UQzUYYHJomO6IR1s4vfF2jExYuj202NpWmasCJ5SVCyBCuXS-N70ahAqDPZ2p9h7DvHdE86Plppt-j_R8Z4fAMLTIdAkDqFIWNBUZIcCziWNLVIzhGNALUUZZMnWr4UDR_kyCO4_L2FhtrUgm_I_ojc06bA4WgURqx2NooNCVxJR65vikhJ9vZd8NNZ-sMn-GlfzDcpj_6Vj_0H1uNV-3DCBn8xAdzW5atrealYj4rU5T4LPTNOqKXV0oe_wiPUCI9BeuV27ACFQUb067ra5_8dOX-KKyBaJAx2uSPEHg_Pdt_p9EQIkWrV_onxPn_o1XYU8QW4D3-DpO9OFf8DKaFME0WYG8JAcmy6ycsUxsUOhVbt49gMe4hq9kDhwvexwfhAvmN0OVTmMHqMvPmbf6M70HojiKCnEcZctBLlyba6w7lWhBId2PLPSdxMiufFV7nE4NEhc0h6iveSseYVz6dcvZSgP9f0lRp0P9NNEeL1k_YBOe-d9s3kLHuRpFcpNAnC0O8ZWmsKD0pLVXSK9OP4IO2kDrGUueE52pryBjebP6QcFntE6cThkoogJy5A7ZsqvrCDUDfdbjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5616927f6b.mp4?token=XBuEHde5crAZVf0z1X99lTtvFAhg5kpHrr2nNJ2QiAWo0omCa0ROyyn0VPpDLF06YOHaRNn9plJrSY4JKdQDuFWlSDKS_UQzUYYHJomO6IR1s4vfF2jExYuj202NpWmasCJ5SVCyBCuXS-N70ahAqDPZ2p9h7DvHdE86Plppt-j_R8Z4fAMLTIdAkDqFIWNBUZIcCziWNLVIzhGNALUUZZMnWr4UDR_kyCO4_L2FhtrUgm_I_ojc06bA4WgURqx2NooNCVxJR65vikhJ9vZd8NNZ-sMn-GlfzDcpj_6Vj_0H1uNV-3DCBn8xAdzW5atrealYj4rU5T4LPTNOqKXV0oe_wiPUCI9BeuV27ACFQUb067ra5_8dOX-KKyBaJAx2uSPEHg_Pdt_p9EQIkWrV_onxPn_o1XYU8QW4D3-DpO9OFf8DKaFME0WYG8JAcmy6ycsUxsUOhVbt49gMe4hq9kDhwvexwfhAvmN0OVTmMHqMvPmbf6M70HojiKCnEcZctBLlyba6w7lWhBId2PLPSdxMiufFV7nE4NEhc0h6iveSseYVz6dcvZSgP9f0lRp0P9NNEeL1k_YBOe-d9s3kLHuRpFcpNAnC0O8ZWmsKD0pLVXSK9OP4IO2kDrGUueE52pryBjebP6QcFntE6cThkoogJy5A7ZsqvrCDUDfdbjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنوب لبنان آماج حملات جدید رژیم صهیونیستی
🔹
رژیم صهیونیستی مناطق جنوبی لبنان را بامداد امروز آماج حملات هوایی، آتش توپخانه و انفجارهای متعدد قرار داد.
🔹
وبگاه شبکه خبری المنار و وبسایت خبری العهد لبنان گزارش کردند، این حملات شامل حملات هوایی، گلوله‌باران توپخانه‌ای و انفجارهای متعدد بود که همزمان با پروازهای مداوم هواپیماهای جنگی انجام ‌شد.
🔹
از جمله مناطق هدف گرفته شده، میفدون و کفرتبنیت در منطقه جبل عامل از توابع نبطیه و المنصوری  و وادی زیبقین در صور بود که این مناطق طی ۲۴ ساعت گذشته نیز هدف حملات متعدد قرار گرفته بود.
🔹
طبق گزارش‌های خبری مناطق نبطیه طی ۲۴ ساعت گذشته نه تنها زیر آتش بوده بلکه با بمب‌های ممنوعه فسفری نیز زیر آتش رفته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/464950" target="_blank">📅 08:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38527a726.mp4?token=CwDu9mRFlm5eKju8fBCe5ubLg386ImHhiMPCN6dbwZduoNPJyY1Dnynufv-mWW9XnJt00iN5RdAU84dfC48LZjd06GD8ux-fj12SvhYj8UF1t7jRMpp1Py9fhozQndBrHshunz9OHQnz10n05d8oW11F9zZFhLj_PTTbdxuI9NTkOCNIuKFnoPGXcg-Lyb1elbGMUEwZgS0v98b1jsOZYEUQnMcxjlYvhSvJnPhGR79agsGKmZlxHsmTmg-_PHzp2osO7f_BR9qw3Op6F0tBpJRPTx6uEPmFxPFa91w8bPC-abozErjEC5qig0gIskJFuTkRX74aRrfFJ_uuGxI0CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38527a726.mp4?token=CwDu9mRFlm5eKju8fBCe5ubLg386ImHhiMPCN6dbwZduoNPJyY1Dnynufv-mWW9XnJt00iN5RdAU84dfC48LZjd06GD8ux-fj12SvhYj8UF1t7jRMpp1Py9fhozQndBrHshunz9OHQnz10n05d8oW11F9zZFhLj_PTTbdxuI9NTkOCNIuKFnoPGXcg-Lyb1elbGMUEwZgS0v98b1jsOZYEUQnMcxjlYvhSvJnPhGR79agsGKmZlxHsmTmg-_PHzp2osO7f_BR9qw3Op6F0tBpJRPTx6uEPmFxPFa91w8bPC-abozErjEC5qig0gIskJFuTkRX74aRrfFJ_uuGxI0CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوشاد هاریموتوی ژاپنی را برد
🔹
نوشاد عالمیان در یک‌چهارم تنیس روی میز بازی‌های آسیایی ناگویا مقابل هاریموتو، نفر چهارم رنکینگ جهانی از ژاپن، قرار گرفت و ۴ بر ۳ به پیروزی رسید.
🔹
نوشاد با این برد راهی نیمه‌نهایی شد و مدال برنز خود را قطعی کرد. حریف بعدی…</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/464949" target="_blank">📅 08:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQkJf3tDUwizJvKr3L2TzRLIWmVsu_uTLSUELbaaQ-etWUc5jz--ukEXRTgPviOuQJLO1jAkmXFckAp1i9dFX01V_UvjQ9A6mzwvzNjZwExocCj7EmhLDEhIhL4i1IDG9IGwpJ-iRQI757sNli73Jfbv_Z5c4Zt1DzUNd9CJYZax7dPsVGabSvvHyryQ7sDjSfKvFA0fEgpltclQLL145a2fc2HafKmlVhXLW40cMB9SwyTjcX8LiU8NLTa6JJIs5Kc0uQH2nwOLA2yzQH6W4fMhKsIIkmbg0fNv5WOws1NFpjGTmmppL6d4IFZs8TZFDvWnVTp73GeEIOqTX8ZDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور از آنفولانزا پیشگیری کنیم؟
🔹
آنفولانزا یک بیماری تنفسی واگیردار است که معمولاً با تب، سرفه، گلودرد، بدن‌درد، سردرد و خستگی همراه می‌شود. با رعایت چند نکته ساده می‌توان خطر انتقال آن را کاهش داد.
برای پیشگیری چه کنیم؟
🔸
واکسیناسیون سالانه، به‌ویژه برای گروه‌های پرخطر
🔸
شست‌وشوی مرتب دست‌ها با آب و صابون
🔸
پوشاندن دهان و بینی هنگام سرفه و عطسه
🔸
تهویه مناسب فضاهای بسته و کاهش حضور طولانی در محیط‌های شلوغ
🔸
پرهیز از تماس نزدیک با افراد بیمار
🔸
در صورت بیماری، ماندن در خانه و کاهش تماس با دیگران
🔸
خودداری از مصرف خودسرانه آنتی‌بیوتیک؛ چون برای ویروس آنفولانزا مؤثر نیست
چه زمانی باید به پزشک مراجعه کرد؟
🔹
تنگی نفس، درد یا فشار قفسه سینه، گیجی، ضعف شدید، کم‌آبی بدن یا بدترشدن ناگهانی علائم، نیازمند ارزیابی پزشکی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/464948" target="_blank">📅 08:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464947">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4bf2f580.mp4?token=SckssHn494Z3LhlUmwE0eP_asgYUOGQoK8u1KMqmH-yxACurx_1kaRkzjOkt-qj1fzyy4fRa30s18POVa3CqcwNj5RU6vLcuvyx9dS95DFQsglKbAKS3JPW-Vmuq6wU73O5D3mEeDJY3HHZCjryk23eZL4opvw3-_ULCV3qEZiKnv9RHM25K7e8SAWGIVx9WHRUyLqbDf5Gk0Q9JEsX6hXkMMdxAbvQW-OcmEFMyq8z1_Hdl7KMtQ1FDIXlS1Ha72HRX5Thf_ZJPJqXwm2zz2xFyKQ7SyYpLdmt5_eqiCueUDjTWBckaTZWQMNtWu9sXkzPHA2oKChtXyLkNUv9awBzH7qIpKUD9zFw6QS3aI9RBr77BeYoJ8qz7Q9RZgXI_8pz6gHvPecX9oAO3Bjum3TI3qBYO5UOX-jUU6r6P9Z_DfijQOw-hjc3arJ6i59y15vsRxihiNwZK2dOzJvNHyqwX3t9tF9yLDIxFhBBcCZzyH_ecTj7CCE3Dy3PCp9VRQEvWcZ-JGPpgWKnj9B1QhbrLy4nDZojyIz7A3lG_BwxD6e4nl7Q5kcnSADZMIap8x1jikGpYQybnN4CUGFzvcaO9XUDdfqOyL9auaQOMq7MmV8LF8cZF0MseD_DNC8aT1RXx7Hm5B-gxkacRx3zkunQ1G99XE6DOWv-9bvGB2DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4bf2f580.mp4?token=SckssHn494Z3LhlUmwE0eP_asgYUOGQoK8u1KMqmH-yxACurx_1kaRkzjOkt-qj1fzyy4fRa30s18POVa3CqcwNj5RU6vLcuvyx9dS95DFQsglKbAKS3JPW-Vmuq6wU73O5D3mEeDJY3HHZCjryk23eZL4opvw3-_ULCV3qEZiKnv9RHM25K7e8SAWGIVx9WHRUyLqbDf5Gk0Q9JEsX6hXkMMdxAbvQW-OcmEFMyq8z1_Hdl7KMtQ1FDIXlS1Ha72HRX5Thf_ZJPJqXwm2zz2xFyKQ7SyYpLdmt5_eqiCueUDjTWBckaTZWQMNtWu9sXkzPHA2oKChtXyLkNUv9awBzH7qIpKUD9zFw6QS3aI9RBr77BeYoJ8qz7Q9RZgXI_8pz6gHvPecX9oAO3Bjum3TI3qBYO5UOX-jUU6r6P9Z_DfijQOw-hjc3arJ6i59y15vsRxihiNwZK2dOzJvNHyqwX3t9tF9yLDIxFhBBcCZzyH_ecTj7CCE3Dy3PCp9VRQEvWcZ-JGPpgWKnj9B1QhbrLy4nDZojyIz7A3lG_BwxD6e4nl7Q5kcnSADZMIap8x1jikGpYQybnN4CUGFzvcaO9XUDdfqOyL9auaQOMq7MmV8LF8cZF0MseD_DNC8aT1RXx7Hm5B-gxkacRx3zkunQ1G99XE6DOWv-9bvGB2DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با شکار دومین زیردریایی ارتش تروریستی آمریکا توسط سپاه حال مردم بهتر شد
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/464947" target="_blank">📅 08:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6ea7c2f4b.mp4?token=Y9hKfbRUWTKeOyURUTFIbEfFjkr8iJEbPIzztLBJNY9-B1KDbobC_8ZWseSSms_XdtzZTOAhUFfOeO53mCer2EzCrJIswyUyx9hjPtb8dXgVEZmLf_G4CYP8iZDHyJRKrCOlN8dGGwOW1yQvha_hPT13TzMS2wsnKMPQaYUcDvmwd8uCofw6xW3syqofcMTY9toqXSo_VYYAsf89RvYeXhqWj_Xuv4EEd0K1sUbaGh5zvFl6KfZxI9zP-14tg_DB0etgMxM88YWhYmkEIf-JtX6ks77oDdtRxVeEzswERyMT7ptHzyhSO4je1JFekRIsegaXtPkQKkA8a1HAJsxPRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6ea7c2f4b.mp4?token=Y9hKfbRUWTKeOyURUTFIbEfFjkr8iJEbPIzztLBJNY9-B1KDbobC_8ZWseSSms_XdtzZTOAhUFfOeO53mCer2EzCrJIswyUyx9hjPtb8dXgVEZmLf_G4CYP8iZDHyJRKrCOlN8dGGwOW1yQvha_hPT13TzMS2wsnKMPQaYUcDvmwd8uCofw6xW3syqofcMTY9toqXSo_VYYAsf89RvYeXhqWj_Xuv4EEd0K1sUbaGh5zvFl6KfZxI9zP-14tg_DB0etgMxM88YWhYmkEIf-JtX6ks77oDdtRxVeEzswERyMT7ptHzyhSO4je1JFekRIsegaXtPkQKkA8a1HAJsxPRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به‌نظرتان مهم‌ترین علامت فشارخون چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/464946" target="_blank">📅 08:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">استفاده از پوشش فوتبالیست توسط سربازان صهیونیست برای کشتار فلسطینی‌ها
🔹
نشریۀ هآرتص اسرائیل خبر داد که از سال ۲۰۱۳ تا ۲۰۲۶، ۱۹۶ فوتبالیست‌ در ارتش رژیم صهیونیستی خدمت کرده‌اند.
🔹
براساس گزارش‌ها در حال حاضر بیش از ۱۰۰ صهیونیست که متهم به کشتار مردم غزه هستند، در پوشش فوتبال در باشگاه‌های اسرائيلی تحت حمایت فیفا مشغول فعالیت هستند.
🔸
طبق آمار ارائه شده از سوی رسانه‌های فلسطینی، صهیونیست‌ها در مدت ۱۳ سال بیش از ۹۰ هزار فلسطینی را به قتل رسانده‌اند‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/464945" target="_blank">📅 07:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWmpV9PPhXJdHzKWoJEIABRgKgE04YxMysj-7Vhrpw0lGce-Ajuxt6-WNO81OBrBD_hMz-T_nH-NVE1qCqDUl1Wcjjk9Qnt9TnqJ0kmkRQ7Yq-0jhbquB-n_lbJNiTb2p99sfV_h-vFxkWIuiD3Ei-P-bzhJ8qOYae48pqtlqkJbE7kPfE3-s7GWOZP9zJ3rMcedJ8cNqDydLGyNiASIUSYzBRyQFfTZJsiEhQYSOFW8z4LHKQ6xu1YkP2-0bwXS5LJdCXaTvvDM8vY6eborEdEtKWtyNg993pNov7FdLvm7obN37bq-KMSaVeA1imjyGK2Edl7YLr8bN5u-5FUQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZxooF9O9pKNFVuw3hecpe70-rnblb8kJKCvO-WLmFgu5h8dT7sSqz-o_P9MzGobESRobh8s3B0Wr7LBMC5rSxtp2D2vfKfbnNYkU8wtT0A06kcKUm01IKYwZGiB3jnG6_VDvsMxyJG-vpdUO7sy-6k2lC6CwmmRvxXeBknuhpdDXSx5wP489wzKEGKDAy9tUBWCuEUeYEsLbebVWe2IMVnaZd-s2akmllOPTkhaE18z1A_ISHJ0YOyORqeMS90P46IOKMjVhK25YY9xtwLkMFoS-OhrJdsOeU-sCglMmpOIxryItloNTIDn1HZ54S_LR3lELusunhbU9uO7Q3VZU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqswUjKGFDVAG6JyfnbkorChTBj0WvDPeD7prWvD4Fai1FR2TUKCWlqnoO6OywfAPGgRjcBeM5MhlusorR71mNe7Nn7QITS6Ip4-uMj8kBPVpbeRg0zlYIJM6I7yPSSqytAcAKQoJQliHchrjP7jJ3eWiuH5neFJTDxK5LF4pYz1fKdZlFC5BpqkTo910uu6gsPTrNLpA025Y-CHT8dJE-s87H2Srja6wEKiuWLhUAGDcElei3_9UnsxvBTNuILF70G5nx_ZPNaoJE2fa94PuvroRhsq2NWoZ_pUMveosQqpjH9SP1Tqes-FX8L4dey6yi1uCfTXRjG6NTSU_PWEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNuJ5Tqd57h-_BpI1SD1w7suh4ctJ5u9xZkVgKB5JNMk29aGdGiG6tH0Lo9DLNgc4VWU1fU2LI9zx1YEu2sF6UIueX7PV-Buc29qJSRyYhpL3Wy97EIb1x1wSq4XueJ5DYAyZ4YKWC2K-pPB_SrEOYX3bDV8bkrJfhYq_IjQi90coy4cQhpVltReYKVe6VWTJnkIfrXUJFHDPQNLy2LM3eldbUVj1Xsx9DlRXTjAspHOGSWWgSUn6Db3r034XnVVEKSx2Uj6Sn-dsNNEdIAOdSlxZiwSc1LiGcAxp6Za5DO9-y3gpxkrRF0KdemYyOq4CCbmweosMjmWuSHxPM1u-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTFdZEhUNigvtkPeLBsS5EZM6OU7Lftdu3uG-pMWL-CPVD1KiKJls4FGDHLrm4eHPl83o9GeL-GAKxuDPioEzsvMmnAEt1Rleq2dCxtEv1U2UB64o0cd4Y6KCYnK8rOsftGvtDhycXwChXqRYBd3xJU_kznRu5VnmsN8VWl3phSjE68TxzdfWnvo3rGBw2CErSB5-hPiHxwd1cmCOK_miFubjbraacUAeQoouDNgrYjD-Nz2TxTLo4gIPrUq25W8bwFK6pteI57MklV773XID1ZVBSrDREIIBlnwJcUDVOBtUv2oz3R_NcAB9aifOB7IbF7KrT91L52prE3oSuJgfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2Pd8npIUlqV9yQLJQyDbDVJJq60sORQlF-BrQHKbs7VNmULTKuv-U28EP0lZiT4OhLY1_MEWYksOh-aFJ820765omTb6LReaZLSYoZAhsJhGQtzzsDAmDFffhK6_onBIkfT1d-CPbKr4XarMNumdyjnEF_6mpotLeFgk-XL7EzU-dtOUeykeAFPz420ZO7lrUN0io_XTOOBUbbSvjXrh0HL5rHNNtYNP8w3JaFSq2aNglYc05NheaP-UA-frXaCMZNw1Yn53NXk8PmveAdLkFma0X_0w1FGr7R-3rKY9Pl0GGmrP9yQEjfwTaGrksIX_m4LbM4U5-6fX---96jOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nb3S_05wAcAEw1K6mPdH0HyqLxwD2N9wD3zSNFkwmHvH9Eeowx0tRb0mhJHgQksBH_OBWUDIqtyPvG4dr5Tv9k2DPVidfc58PEQDSPunSdJ8Y2KTS07swFKwuGKZaEIpTdf81GC25eqC8h7nTeMvHa0I-fswIRH8GYLlsbyWqhZfBem2kHC8a1EF_w46pwnhaZwAb8_reKG-mHeAbzXie7CJQv8A8GzRwSJhigc7vTV9A7ysKvrIJ2iS3Tgo4DBsR3FE2t-Y9_RnR67NTw6eF3jzFF1W-a4D0HZ-tKJMBcKlKx85M_a1OJRbxro2G4JfNclXcxCjrXmUzL8Dr95jvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونمایی از ۴۰ کتاب روایت مردمی دفاع مقدس
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/464938" target="_blank">📅 07:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صعود مقتدرانۀ رستمیان به فینال تپانچۀ ۲۵ متر
🔹
در پایان دور مقدماتی تپانچۀ ۲۵ متر بانوان و مجموع امتیاز بخش دقت و سرعت، هانیه رستمیان با ثبت امتیاز ۵۸۷ به عنوان نفر نخست در بین ۴۴ شرکت ‌کننده راهی فینال شد.
🔹
همچنین سامیه یاسی با ۵۶۳ امتیاز در جایگاه سی‌ونهم ایستاد و زینب طوماری نیز با ۵۵۴ امتیاز جایگاه چهل‌وسوم را به خود اختصاص داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/464937" target="_blank">📅 07:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پایتخت نفس تازه کرد
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۶، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/464936" target="_blank">📅 07:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آغاز بانوان اسکواش با شکست
🔹
تیم اسکواش بانوان ایران با ترکیب نجمه بوشهری‌زاده، فرشته اقتداری و نرگس سلطانی، در نخستین دیدار خود در گروه C به مصاف ژاپن رفت و نتیجه را ۳ بر صفر واگذار کرد.
🔹
در این رقابت بوشهری‌زاده و اقتداری با نتایج مشابه ۳ بر ۱ و سلطانی با نتیجۀ ۳ بر صفر مغلوب اسکواش‌بازان ژاپنی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/464935" target="_blank">📅 06:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌ یک مدال برنز کوراش قطعی شد
🔹
رامین احمدزاده در مرحلۀ یک‌چهارم نهایی رقابت‌های وزن ۸۱- کیلوگرم کوراش بازی‌های آسیایی ناگویا به مصاف حریف ترکمنستانی رفت و با برتری ۱۰ بر صفر ضمن صعود به مرحلۀ نیمه‌نهایی، مدال برنز خود را قطعی کرد.
🔹
رضا احمدزاده، دیگر نمایندۀ…</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/464934" target="_blank">📅 06:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
صعود نمایندۀ کوراش ایران با ضربۀ فنی
🔹
در وزن ۸۱- کیلوگرم، رامین احمدزاده در دور نخست حریف تایلندی را با نتیجۀ ۱۰ بر صفر شکست داد. @Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/464933" target="_blank">📅 06:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAdHaOb97YfClS5-n-cxw26yczsCPtecJBXjN54f6shmZTVvPSVa9vz1vBtxN0_ClU95HIOrbxnF5BKWOvID5ovCJTasyFffqO0mGcJbAQW3nZFO2-lO6nV3LNQwnww2EG4i3a070WExMfCAo4RB1pGy1U7ZrOp05MkoYtcxn32i8pRydCRs7_JE2WyxZEd2_PqTrgFExU7juSQLg9qGo-Ow9Eyl6BhoWwkaSAdpgXSSRUHdeyR4FmMbVeSECFHE-Ycyl-LDPjgv0iFgInySfF6pXTzCqdjwl12AuME7np5qwnGPyJ6ytutVuKkNwKWNoFNIReMiFuAAZhbcZE6qbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: قرار نیست مدارس مجازی شود
🔹
مدارس در تمام کشور حضوری هستند و اکنون همۀ دانش‌آموزان در مدرسه حضور پیدا می‌کنند و جای نگرانی نیست.
🔹
اگر در منطقه‌ای نگرانی یا شرایط خاصی ایجاد شود، استاندار و شورای تأمین آن منطقه متناسب با شرایط، تصمیمات لازم را خواهند گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/464932" target="_blank">📅 06:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1Oxd9id2bOstjht-m2dxywVmbi41kNdidKoGMq_Xwb_P8ijQenaUnEGeVdJ_tRJS9o7ubuIDQW-aGkcTFbIRo7GrDS6Jf_qLbYcyAYZ8RYR-fWqX3aCJ7BVU3zO51zhvnY9XTwZqCaR8kT9oZGsoopb-sE5GJMTtOrkgaxfS0SSQcsLWH8t0DKeeQwRpggVwbVKOnsM4BZrqVj3QsNNVzUVTqzPXArFP9vVHiHor_avFvUBnfWARYCtBDP8_UnA5ua1NK64PWenGyXxExr8XvYsmECzPm_Rxo4DPMLN-FxLuIeR4K3SGv2XzqVpcW78o92JG1Ojudr8H7oZJAiA2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKsVHJDsfSe4sRogKhQMtuONylYRWQwCoIL00qZD1NzUoie3cYW4TAOouZxgpQq_URY3CrzBGr0zhW4ETveQz1R63fABdIUrCKmI6529l2kQ5OXVgZAQX5NIhs1gHLfn8XkrhhSOAC5_MZPHih0ssk8mw2knKqmqT8aRFLvJMveJA5UmqZFUusceTogklODN6NQNNK8igozGQn_Mqe_R5lqq_1rjfEk9MBwMrDtwDXS8VnyroSG5kcEuR-1n-WMe3nYiaOQmP0SuNeNi7vv3xw-gj4qeBnwE3hwQQkrXJlPj3Z06db8ktDek8hJTZZqORsqdRGhtsURdK--zh3-ZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhtkuqJREW4H_Gp5lJ8Ho_8IMXDZK4EKsjzAnFw3_vIBmUrBQDsC_bupdCMi_U9zvWIeB7Pp_PbDnllYXxS82PF3esQEnoVzseDPHoNSKDCMB9EuwD8UWYnXepBhgbaI4medPrbDiVZ4af1gWTaLlHFKYvknsdRpwR7cX2eNkFdiiwcrDOXL0Dsp547UfKbeB_D9vViKDxi3ITYjBOE7F__d8oFvSk16HJ9AEj5xQnpVbElPEzzExdNvwbiS9Q1O-NY2p3hQC0dw8l8EJkd2bgzDWaX2kB0UnxdIJ46fF4ugL4gkW4EQz5GJC3-uxBd_0pe_Yka8idWA0ywT2lmV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjqsbHdsmV8FschPDPSI6liyUTYaB5GXAMFYloNk6yaHjMhJ71sIUeMgm9HUHweTH4iIDlNS4-2hRxwzNQD85R_oe9N8A4JlW0MVQM1J17zqSVOpzII-O_71cbuffu11wLoT5DarqBo0oDgg7gkNRwbLYUxE0n6VsukUbrzdLU-gADMHfDo1WjA1_MMxdXWnlynSgBEADcLYDdvyAKcg81cNHNUOEeY04JBiG8ZwQ5hghG4Qa5csisb9G-tlEbehy79kjhMbPRDwJbASY7WX17s0TvczVjoagvdRcL33xqkRw5GBpVS1FNtRIQ3pHo6JPO-LFgF1YoQiKx2BZh04dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUh1s76AOZS4p07wCcHRcFiUFfT-U-mDe2FyTpRfN2kR6gVRh_xLpsKkeeI5xymWVHwiYwPm9WODkjYGDVOEP-7tOxOcBMA8Uxhe5Mc-xTsDyyS-sLJi686wXUN551-StrP_GcoaG-JvoZtWyBrKXYW-iTnay-IOSA6tS_HzRsRguYNRwjBLdn0UHSbzqhzejd_RiXmMER_sOnUzXAukLqUapDc7sN1Nc_FJxY32kmsv0Nt9jvBX9_awjn0DcW45xfwy-3mVwMiyBid4BDzI_ud7Mj8nBsOr5P8m4ZkkJM5CnQIks1mHHKETcasMYnXm_TaYEqu__Ia0ncSH8l_RlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OB0n9MFYScICnfy7ifzmHvzcRTKfPfMZ9vOLyxyYYA1P4TiVZ7ceL-owVfFQgPYFItVtG9GHgGP1UBXyPVOAXEwfuOzmv39ucecuToa6Zg57Dmp_fQXCL1yxJgFqzXgHF56BlULgvvhZihlcPWFJLHVhpiDdDV9lNuYCf71JTJppK2YqPQxPpNBHDDuxyzElREyoYaBXBoEqyWgcUQkD-gCdntZw61FKYYPJhUSuBa58MY6XgLNZFQI424720SD7S6JZDh8ODsUlsZO4Wit3gmJNHLrz3ee-_3BTa0vW2XWdzMmUa9xsGSrEY-0rkHyh6DQ4msSD8dd1HnyyGp7EMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRX8Frpa-xhSQZ4UJ7gQ8MJ_61mFRJqOzs_uHqEH8yqheuiHvrX5JFtTRlPLZTrOTcteE2FAFvlDmaGDs69solECHZeQutFJ_099IXJg2ifTB9ls5XfEgcb8ThQt4KehAnVryIWIzRhrvOmS_DGbMhjGe_qq9wPxbvJOPtVSOf2FCQ20ZjI5t7VU092CHwpXdIWfjCc8RfJASp5jr1xm15j0LSZZsjeRznbWDiyTUdV96-U89CKy-Npv62r8NAzVC1A44BmBvcriqKcuApeROSY29Sm8BaRv3-a8k7Pq49X4tdYhz_oVzkbiBnDW6UX4cN7etytnUz3RZ76DE57FLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت میگو از مزارع چوئبده آبادان
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/464925" target="_blank">📅 05:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464917">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6KL4zRJXpcXIUI6mLbdCHCSJtpkgelJl0OkmxQSrP9o7y3ju27Cd2p-A3lM-546idNjNircG8zc2vIcjlXz0zRjG4BOvfaHQfNP55wmgZ5HU6NLMdUOtxD8ArgiM4_fiGpjGtQTtxeICqSKq6endJOubB9RJIPnMPhcMKXk4cIm9Dv_twtozhUvzss2lu8M9oj98jSTBTmJ7J2JBisMoJnMiT1rh1yZKK4xfFDG2U_ud9T8xY0Tw_2Ln9j1Mj0-PUOJGScPCEd8EYW6mYNJxWfjyi3-7ixBhwJ0weIMLzv_jSkC1nh6OkwjanDZ8zUzsEiJF0fDyrJZB8NMo2c3uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال سنگین در حریم هوایی قلب عربستان
🔹
طبق گزارش‌ها، فرودگاه بین‌المللی ملک خالد ریاض با اختلال گسترده در پروازها مواجه شده و برخی اخبار از ممنوعیت موقت فرود هواپیماها در این فرودگاه حکایت دارد.
🔹
داده‌های رهگیری پرواز نیز نشان می‌دهد چندین پرواز به مقصد ریاض یا تغییر مسیر داده‌اند یا در حالت انتظار قرار گرفته‌اند.
🔹
تارنمای ردیابی پروازها هم شاخص اختلال فرودگاه را در بالاترین سطح، و از تأخیرهای طولانی و لغو چندین پرواز خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464917" target="_blank">📅 05:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464916">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f464db16ef.mp4?token=Ve_uI_oA4kSwlrlxk6Ixx2i0Xs8EYfp-g2iIgVY7bmP-aHaYpMeMzeMD0tHTRo9wMRe6LQIhCDAqe_8EINqy6s0Gfi5_PWq8Q5GdlovoVtBZ08KkLDZCcvBgVW4tgBt_DsIFZdBExYXCxKikquuksnBoPVUv27np87bp53_jYKkTC83wJ5C8cTqUYK9jGrDhnN_afC1S0K5nz8-fDfDqBSjnKs6tStFV1nLnUtrfvvkP44J9XDRP8LnQTvdiLr7xkQ4YQBCwDyRogDpP65MfFnYTZqadHI0wqED_c7hG6DDsFzIW6Hiloeps3ABjDS8Nh8hCm_x1LI-slVBV_tDAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f464db16ef.mp4?token=Ve_uI_oA4kSwlrlxk6Ixx2i0Xs8EYfp-g2iIgVY7bmP-aHaYpMeMzeMD0tHTRo9wMRe6LQIhCDAqe_8EINqy6s0Gfi5_PWq8Q5GdlovoVtBZ08KkLDZCcvBgVW4tgBt_DsIFZdBExYXCxKikquuksnBoPVUv27np87bp53_jYKkTC83wJ5C8cTqUYK9jGrDhnN_afC1S0K5nz8-fDfDqBSjnKs6tStFV1nLnUtrfvvkP44J9XDRP8LnQTvdiLr7xkQ4YQBCwDyRogDpP65MfFnYTZqadHI0wqED_c7hG6DDsFzIW6Hiloeps3ABjDS8Nh8hCm_x1LI-slVBV_tDAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف ۲ نماینده کامپوند ایران
❌
میلاد رشیدی در یک‌شانزدهم نهایی انفرادی، ۱۴۶ بر ۱۴۵ به نواز احمد رکیب (بنگلادش) باخت و حذف شد.
❌
فرهنگ خداپرست هم پس از تساوی ۱۴۶-۱۴۶ با دیلموخامد موسی (قزاقستان)، در تیر طلایی مغلوب شد.  @Sportfars</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/464916" target="_blank">📅 05:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464915">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">حذف ۲ نماینده کامپوند ایران
❌
میلاد رشیدی در یک‌شانزدهم نهایی انفرادی، ۱۴۶ بر ۱۴۵ به نواز احمد رکیب (بنگلادش) باخت و حذف شد.
❌
فرهنگ خداپرست هم پس از تساوی ۱۴۶-۱۴۶ با دیلموخامد موسی (قزاقستان)، در تیر طلایی مغلوب شد.
@Sportfars</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/464915" target="_blank">📅 05:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464914">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
مجروح شدن ۸ تفنگدار آمریکایی در در حملۀ ایران به ناو آمریکایی
🔹
ان‌بی‌سی به نقل از مقام‌های آمریکایی گزارش داد: ۸ تن از تفنگداران دریایی ما دو هفتۀ پیش در حملۀ موشکی ایران به کشتی آن‌ها در تنگۀ هرمز زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/464914" target="_blank">📅 05:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464913">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk2QaVfSp_TAcrLeOL_ITbu65-rnHWW9q1qdW-88404zW0b88JCVDgdi16knjGZqmQ5U_X8NsBliAw9V-HDj9uxvqbNcLyHnrAL4WKCmpNEpWjYjeEKJMyTswOY-DOOsB2SA3lRy_-XY3L-LOL2r7goZ8oB3fdE8oygFO4RpDxRZuj8MfzI3F8QJlyED34CsC0cvl_c8SfQWd9qVtokTUPszqvSux6g4zNqHSLVlk24QPgB6Mqjb0TGD4gcZUoS34Z48bbWE84UUF8m41l1aEoQcLkP8p_tVPPozCaAhtuwJH4hix-I7BuzvbtusdK0P4gLJiZIk-QIq9y7uv4lrAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جدید نفت بی‌توجه به تلاش ترامپ و آکسیوس بالا رفت
🔹
قیمت جهانی نفت در روز اول هفتۀ جدید میلادی، دقایقی پیش از ۱۰۶ دلار برای هر بشکه فراتر رفت.
🔸
ساعاتی قبل از باز شدن بازار، آمریکایی‌ها باز هم خبر مذاکره به ایران را در آکسیوس منتشر کردند و ترامپ از کاهش قیمت نفت گفت؛ اما بازار نفت نسبت به این اخبار واکنش عکس نشان داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464913" target="_blank">📅 04:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464912">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY067wgIgewloYvRkucvzfdP-c25ziEj85LEbZNzVQW4W5OeuiyAl_V2_bmLmo9i937gRd8Usko96IpeCQIJVQPvm8kfDuueTu4ukGbhv05o6wTd4lENGUGDebQ30Vme2noluXYA7atuie_6gL5z7TskUIk2VeVcEtAIWd7fZdrt7pVolOsHaTRtwXrd3STsGiG0EKUudwYfCpEl2TG0V9S5DjpHHLTDIZb8LndHvDMY8KUbllYUmUi7X4zVDeny4U-jEymaZMcyIAtCYqa_19kM0BV-0xGuYrmi2U25SMVIgC86LXOwFC98XlxfHRsnaCroESM_sTIlVPHyhRP2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناامنی هرمز دامان اینترنت جهان را گرفت
🔹
هم‌زمان با تشدید تجاوزات آمریکا و اعمال محاصرۀ دریایی در خلیج‌فارس، کشتی‌های کابل‌گذار یکی پس از دیگری منطقه را ترک می‌کنند، پروژه‌های چند میلیارد دلاری معلق مانده‌اند و برخی مسیرهای حیاتی انتقال داده شاید هرگز تکمیل نشوند.
🔹
در جهانی که بیش از ۹۵ درصد ترافیک بین‌قاره‌ای اینترنت از کف اقیانوس‌ها عبور می‌کند، بحران هرمز دیگر یک تهدید منطقه‌ای نیست؛ به یکی از حساس‌ترین بحران‌های زیرساخت دیجیتال جهان بدل شده است.
🔹
به همین دلیل یکی از بزرگ‌ترین پیمانکاران کابل‌های زیردریایی جهان، وضعیت فورس‌ماژور را برای عملیات کابل‌گذاری در این منطقه رسماً اعلام کرد.
🔹
آنچه این بحران را نگران‌کننده‌تر می‌کند، هم‌زمانی آن با ناامنی مسیر دیگر است: دریای سرخ و تنگۀ باب‌المندب. کابل EIG (دروازۀ اروپا-هند) که یکی از وابستگی‌های حیاتی برای داده‌های سازمانی بین‌المللی است، به‌دلیل عبور از باب‌المندب که اکنون منطقه‌ای نظامی و محدودشده است، دارایی پرریسک تلقی می‌شود؛ به‌گونه‌ای که هرگونه آسیب فیزیکی به آن می‌تواند به قطعی نامحدود بینجامد.
🔗
اما چرا این هشدارها را نباید دست‌کم گرفت؟
تجربۀ دریای سرخ و شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464912" target="_blank">📅 03:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464911">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نه سوئیسی‌ها به «بی‌طرفی»
🔹
رأی‌دهندگان سوئیسی با اکثریتی قاطع طرح تعریفِ سخت‌گیرانه‌تر «بی‌طرفی» در قانون اساسی این کشور را رد کردند؛ طرحی که در صورت تصویب، سوئیس را از همکاری‌های نظامی با ناتو محدود و از اعمال تحریم علیه کشورهای درگیر جنگ، از جمله روسیه، منع می‌کرد.
🔹
بر اساس نتایج نهایی اعلام‌شده از سوی ادارۀ فدرال آمار سوئیس، حدود ۷۰ درصد رأی‌دهندگان و تمام کانتون‌ها با این طرح مخالفت کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/464911" target="_blank">📅 03:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464910">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464910" target="_blank">📅 02:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464909">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">🎥
از بزرگ، کوچک نخواه
🎙
استاد صفایی حائری
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/464909" target="_blank">📅 02:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464902">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEe1zBWMF4S6KMR9DnQT6XnQLcIOvRn2rLAVjQ8tHuIdNENefHWXPTKWuYstDTDM1ntNpx1Dj2R95MODWmtGG7L5R1W9rS16_gMEDIhkAIf6zXB_ZovRrUugzOHF038j1NRxly5jtXWzgINS_DPFKjRMJ7hSR_N6LEy2H8l1AlphESUgtokfGJtsZvwmwpE5ALPjoUqf7gp2FSoIZk7Xvey9K-bM9FiLbG-Ig2c3K0GMzz3e7lierxoI3jdJJgEX0qBG26XIZuUB7UoUkkcd-RulhmSHFboivu2O7Cu04oO7b5jl5N3aZiak6dPMHpye8dXQnitV9fMVcmjSiqZcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRIEyzM3TM52Vd41WaFNV30UqO_T8QaVifFQvM14Qk3BoAh_-_PE07xm2VKndfaZlOQHxtFuOdnLLFBgjy6aOihKKp_0tINowP1tTcD-X0xr_m_WrkgQqYYQmXQ_C4haVJNngCt1Jr7enEVZECdrVqTPsBeDOCEuMT-wYJtjwqGYbhsorKOPGe4Zfbcsbln8Kfrn3AD_9Fjajm8ejyb8As4nzpfe2XlZY3HyRyt3T27ubKqyBsrMe5XawYyOwc-TSKIsKChTyUbabM5X9sVD83xVo524AtfEEO4h03XZwoDuz62Bjz-hz3D6ZmzupDjhWDX-NR2XUM75KZbv6-QN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmYIdBP6tcH_kjaC51Slq35PAJ8yPMLlKXRTvITZW2QsWzmD1OOzjEtx0kNCXqplOVB-JK1uQgVpIVqDlzSCzKRsK1fqhfmFv1QvgMJfnnJ39FpSmNcysZhr8V0zIdHj6tYmb1Py4pc57U0lr0JdV5EiJUWHQOQRBJtJ93toxHv3Pt31Ny4foyQY3n6dQydu_saFKFfi17N_3b_kx-xFjpphn5gHnUzbIsjYiZ7Qz4LMhjNQDkvAcrcvlyU8x4KiKgyNw8cYi9p19nl6wFhnyHYRV91RNzBDlEOIUn46hElTPt2cNmhkY34CK_cWZ05mMx4d9wREaDRxo4DxCM4gXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jn5-i7VsfGsWYPAYA-RnhzWn7sbRHvRXyPQRxUgbGt9-GqqR_rnKsAvUP5BzTnTbwR7yawoHY0KF1KClEa5sBQ7-FI759Hg450roMFo9shbTQQ6CzygHjC3Um-U_CR1c5yrj8CG6HI-FvZz0WzPqfjbhOShHHHR1viefhdN52Ffay3GGXStqPaHgPzcmfUhSWFmRUtiGdckGCJudiJL_uH_Yf7Ily5llI9sHB7w2cXKV-HC_5vzItcIcPbS4uhxFrytgmL79NsJ4eU2VNRP472yR_FWZW5yeSZeiZvJGZYOWUVnFrUMv-YXB9uJsTM0ihS_NhQfH4gTUvCq5MCji3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XX7Di3z6KoX-_gRoOQ8FbXsg99zRhm3yIpm7MQ1BsIuMoEaDslhUW9qqxQGzpzsaYNatqyLKTTuE-nvQVEb-NqqkacJVOdkDSEObUEI3bdubkRE83K7ppqIIM-0bOmJzhRtWi3PXTZmf2cVXR7d8b7mhQNadGueeVsD9BX8qVVvw_sHXUukKDCaZQZUAqiJcN4fZFAEW_PIuzdZw4R8Tw9LcEw5KyOrBZhmz7xS8R2_rm8Y6S4VDNuAuaE9NqEwJUD9lCiKt5VnVeZGRmY4xvi_mTumjpPXAsaHya96xmqGHTnITWhdAGvVKSERU2ErIH3M-3z9FOhiTg8T5iWp6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2R1t5v-vPAMDXfRYjQUdEYj_5Y4A15WlQt0tX3qM6TlU33ngd4AYmg07nGxRV9kVlyOROA_hmoC5_BJdWiDyrCkwgMWDPgf-3Yr7LM2jHywPhbOabJCzr_12dFTbluLqE8ntOwr6f6iV9T0Y7G58vKJwtoG6asJYdwOurWWl6lmnEMJ5imgU1gBi6SOV8xCo98WmmAj5GKu7kvv7nbA7xcFUl52q4Q_mQyPCHQPVzuq-c4P8s0O_BEsTHjNew1bHypICsqvjGOZXSaIwG-57Ij5b635cTI_LduM8qUzTYOrxqOJCW8RPjZrNglq7frVDPxb4JTUN8bcSHp3PHeD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOtmXI5K24Qiry0asZBGC5KLsAP--7NolWpYSPJemof_GUkn91ewaFsnnj9dY1nyaE3qYUsEHkaA3b6PzBw0XaSXamJVABJIwM7MkLkYz74LR0xyhgGorBGku1sjdHAZw40g_Jav9gYAZoDmPIXdGUhftBk4E9EwB__LpwFk0ZO_0iuSd2yL2wmWZjyR9xpxIfpUGCMlYRFgW50wZVmcBUdt_JKV0oDT8IcySPbPUtlHwS7GsvgCe0QEdXZLsQFs_YyKOgHBot5opYcgoAodS5Y9Z66BzB7OHiWHaTYv_QFACh1kgAPX2lsCtw9mvJxgfQvhw2ry9JvCiFHj46VrYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دومین سالگرد سید حسن نصرالله در محل عروج او در بیروت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464902" target="_blank">📅 01:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmEvbdNbnsWxETYzPjN_nIjHDAsElJnk5ADu2RBcmg6TePP8nBp7HsewtULnkcm29bhA1jzLJ95dl6eTN6V1jH8kyQUSP5n4DdDlldCwN_HzmKvmmPUXrl8CTFcmZunJTSkUknoFjXJRLb01b9AjXdzXQBoia2UeuaOPk-Q6QfdxPfzzp4Qg7s643bYDzS5Z4lHhUZWRt9k2rAv3UghQN4D_XiMOqa9Esd8sryEy123dKhdV_Fp-9DXOgRP5VTxTTRUvbGFTdCXeeujA-oIBCL7EsfIaC29qamXQYgnkc5zT-EM-UIW6p3McdtfL--iOEcIqVSAhMmGgyMpciTDb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حج‌وزیارت: تحریم شامل پروازهای زیارتی عراق نمی‌شود
🔹
در حالی‌که هیچ پرواز ایرانی به عراق انجام نمی‌شود و زائرانی که مسیر هوایی را برای سفر انتخاب کرده‌ بودند، در روزهای اخیر با تغییر برنامه مواجه شده‌اند، اما حالا رئیس سازمان حج‌وزیارت می‌گوید «سفرهای مذهبی مشمول تحریم‌های بین‌المللی نمی‌شود و رایزنی‌ها برای رفع این محدودیت و برقراری پروازها در سریع‌ترین‌ زمان ادامه دارد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464901" target="_blank">📅 01:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXfG1H4v94dvq6etnXx9uvuGWZl8tG8bYEpQ1FTHgSpI1NCLOVqVlJtM5jgTA3nSPDgKKczZeqgYi1BIkmmb030hTKUyqnTwqx0uMDdEpkQg34stt4b18ewsxLAkdrO223wE26M1iwOYSwuuqQurcHuLsAcD0TsXNv8dkcn0uYAlbdD89u0J_Ey0_-H2jQoHk2nAgXVQRcsJTVTve8lIu0SMj-0uAKpMmvMkSQCcXblsExCVdmtgLlmi7yHBr2OOEvE2nEnUfHtxm4iIf7lQDSEETI6cUoEKZ7Y0z_UITRsWF6s1IN4dwG-iKsY1NVbrJY2ClY1ccXTKM6c0QR5pyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد عجیب ترامپ به شی؛ از آمریکا سلاح بخرید!
🔹
سفیر آمریکا در چین اعلام کرد ترامپ در جریان سفر اخیر شی جین‌پینگ به ایالات متحده، به او پیشنهاد داده که از آمریکا سلاح بخرد! این درحالیست که فروش سلاح به چین براساس قوانین آمریکا ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464900" target="_blank">📅 01:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیانیۀ سپاه به مناسبت دومین سالگرد شهادت سیدحسن نصرالله؛ سید مقاومت زنده است، راهش در اوج شکوه و اقتدار ادامه دارد
🔹
در بخشی از این بیانیه آمده است: دو سال از آن روز خونین و جنایت دژخیمانه و تروریستی گذشت؛ روزی که دست جنایتکار رژیم اهریمنی صهیونیستی، سید مقاومت، پرچمدار آزادگی، حجت الاسلام والمسلمین سید حسن نصرالله را از جبهه مقاومت اسلامی به ویژه حزب‌الله قهرمان لبنان گرفت، اما برخلاف تصور و نیت شیطانی دشمن، درخشش خون مطهر او نه تنها خاموش نشد، بلکه به چشمه‌ای جوشان از اقتدار و بالندگی در پیکره مقاومت تبدیل و جاودانه شد.
🔹
سید حسن نصرالله تنها یک رهبر نبود؛ او معمار راهبردی مقاومت نوین، استراتژیست میدان و دیپلماسی، و نماد عینی پیوند ناگسستنی ملت‌های مقاوم منطقه بود. او به تاسی از مولا و مقتدای خود شهید امام خامنه‌ای (قدس‌سره) مقاومت را از یک تاکتیک به یک منظومه فکری، هویتی و تمدنی ارتقا داد و ثابت کرد که مقاومت، نه یک واکنش، بلکه یک انتخاب راهبردی و یک سبک زندگی عزتمندانه و قدرت ساز است.
🔹
تأثیرگذاری شهید سید حسن نصرالله فرامنطقه‌ای بود؛ و شعاع آن از لبنان و فلسطین تا یمن، عراق، سوریه و فراتر از آن، به صدای وجدان بیدار امت اسلامی تبدیل شده بود.
🔹
شهید نصرالله، معتقد بود که مقاومت یک جبهه واحد است و پیروزی در هر نقطه از این جبهه، پیروزی برای همه است.
🔹
بی‌تردید، دوران رهبری شهید والا مقام سید حسن نصرالله درخشان‌ترین و پرافتخارترین مقطع تاریخ لبنان عزیز و جایگاه ممتاز او در تاریخ معاصر منطقه، کم نظیر و ماندگار است، و نام او در منظومه فکری مقاومت، همواره‌ به ‌عنوان استراتژیست و نظریه‌پردازی  شناخته خواهد شد که مقاومت را از حاشیه به متن آورد و به یک گفتمان مسلط در معادلات منطقه تبدیل کرد و تا هنگامه شهادت، معادله بازدارندگی برابر رژیم صهیونیستی را برقرار و افسانه شکست‌ناپذیری آن را برای همیشه فرو ریخت.
🔸
بی‌تردید، راه شهید سید حسن نصرالله توسط مقاومت اسلامی لبنان و رزمندگان حزب‌الله تحت رهبری جانشین صالح او حجت الاسلام شیخ نعیم قاسم در اوج شکوه عزت و اقتدار تداوم خواهد یافت؛ کمااینکه مقاومت کم نظیر جنوب و رشادت ها و حماسه‌های تاریخ ساز در علی الطاهر روند مهاجرت معکوس را شدت بخشید و فروپاشی قریب الوقوع رژیم صهیونیستی را نوید می‌دهد.
🔹
امروز، جبهه مقاومت در سراسر منطقه، به ویژه از هنگام وقوع جنگ تحمیلی ۱۲ روزه و ۴۰ روزه آمریکای تروریست و رژیم جعلی صهیونیستی علیه جمهوری اسلامی ایران نشان داده است که نماد عزت، آزادگی و ایستادگی ضد سلطه و ضد اشغالگری است.
🔹
بار دیگر با صدای رسا و در اوج صلابت و اقتدار اعلام می‌داریم؛ حمایت از جبهه مقاومت، دفاع از حقوق مستضعفان و ایستادگی تا آزادی کامل قدس شریف، رسالت ابدی، ملی و انسانی سپاه مقتدر مردمی و انقلابی و سایر نیروهای مسلح کشور است و به فضل الهی تحت هدایت‌های فرماندهی معظم کل قوا حضرت آیت الله امام سیدمجتبی حسینی خامنه‌ای (مد ظله العالی) و میدان‌داری شکوهمند و مقتدرانه ملت مبعوث شده ایران و وحدت ساحات، توطئه‌های شیطان بزرگ آمریکای تروریست و سگ هارش رژیم اشغالگر صهیونیستی و حامیانش هرگز به نتیجه نخواهد رسید رزمندگان اسلام تاریخ آینده را رقم خواهند زد و تا پیروزی نهایی گامی پس نخواهند گذارد.
🔹
سپاه پاسداران انقلاب اسلامی در پایان این بیانیه ضمن تجدید میثاق با امامین کبیر و شهید انقلاب و پاسداشت آرمان‌های بلند شهدای جبهه مقاومت به ویژه شهیدان سیدحسن نصرالله و سردار سرلشکر پاسدار عباس نیلفروشان، تسلط، اشراف و مدیریت جبهه مقاومت به دست رزمندگان غیور اسلام بر تنگه راهبردی هرمز در میانه نبردهای تمدنی و وجودی امروز را از دستاوردهای ایمان و باور به نصرت الهی توصیف و تاکید کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464899" target="_blank">📅 00:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144f6c0818.mp4?token=YnRmivJKKS6dmmDsuXgI-SNWnzEijw0XaK4awRuqrNF0NTIyQjKNi6FZDAnpciPoCJrJp3Usg8PxJeocPY2_XPF-6zBisbBQ2qBcf_8l04DJQq3qJfdCW6E-kp1z3MPyVQQMHxRStNFYX3Ed05WLFInJeqOGBAHw1mB8Co1WW_I7KYYFpVkES8LRu7lPOQgHr9WElVNOyoT9AEHGPiwtXJKsP72rH5_QiZyd75LvxWwAqMyWfYHAsWMuo7QgMCuzOXislLp3q2blnnX7ub75XbGb_NFdYDt1_xGgqudhAFX72z4t6bSNjt8Pvpw2x-5oPBvCEjp68mcwUWrADvkWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144f6c0818.mp4?token=YnRmivJKKS6dmmDsuXgI-SNWnzEijw0XaK4awRuqrNF0NTIyQjKNi6FZDAnpciPoCJrJp3Usg8PxJeocPY2_XPF-6zBisbBQ2qBcf_8l04DJQq3qJfdCW6E-kp1z3MPyVQQMHxRStNFYX3Ed05WLFInJeqOGBAHw1mB8Co1WW_I7KYYFpVkES8LRu7lPOQgHr9WElVNOyoT9AEHGPiwtXJKsP72rH5_QiZyd75LvxWwAqMyWfYHAsWMuo7QgMCuzOXislLp3q2blnnX7ub75XbGb_NFdYDt1_xGgqudhAFX72z4t6bSNjt8Pvpw2x-5oPBvCEjp68mcwUWrADvkWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژۀ رزم مشترک فراجا و بسیج در قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464898" target="_blank">📅 00:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAPBuPOnaAdUhTCOum2cSEH7kx-MIOYtQwK0z771DYBw72we3WSBArxt95k9PKvtbhMwxVyKjRspzlzJEq1DZeOtHf-wg1nodlZcwiiW5O97mrFqZ-l18OXl3PqdqKO_7eGthapozmrcXFIexda8tms55eJWiPxemBG_niRuH8u_USsHHArk56FG7AhmhlGHvLNUo19DcrStcaGBP-cMus5VdTqqgJQVhy8BrkOWDCXxO-h6tDmgt_g7S4_Yphc0u-TTT4FIu1oFoZt7C0priiOTg_uimsWOch4LZTkjY_6tHZIOPukSjPQcZwg5SKwoyFxIDu_t7Ob87jKFRh5ExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور صربستان استعفا داد
🔹
الکساندر ووچیچ روز یکشنبه استعفای خود را اعلام کرد و به دومین و آخرین دورۀ پنج‌ساله خود پایان داد و راه را برای انتخابات زودهنگام ریاست‌جمهوری هموار کرد.
🔹
به گزارش رویترز، استعفای ووچیچ هفت‌ماه پیش از پایان دوره‌اش، همزمان با کارزار انتخاباتی برای رأی‌گیری زودهنگام پارلمانی صربستان در ۲۵ اکتبر (ماه آینده) صورت می‌گیرد و به او اجازه می‌دهد تا در صورت پیروزی حزبش در انتخابات، به‌عنوان نخست‌وزیر منصوب شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464897" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464896">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzDmMkKCEmQ-6fXg3Jlfbwy7_8ew6NU90W-qky7q32EDsXFrTqqQPYOC51CnoRlcDpafVedNe26r0tltAaj88WAtBKVXbpj109L3ASKwBHJIKjtgAEX_pF33h3xpM_puGY5Y6fCThKkX7cmVDLqODEF4asJGDW5V_1bqORMiTj98gf3jLpEjJwoA5FWKgX6vRm66zYNPFXvIb49qajt81caBUh1LhMEFXei44UwWkTKEHxJinl524u9SDSfBZo5N7AuDzOE59M2HvfU8ZRSMk7SYqh-FCrDs8c5a1zI2bmTU8Xu0tgqxrrbpouGX55LvlylIFhYEa5GwWEHtF15E9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بیانیۀ وزارت خارجه در محکومیت حمله به زیرساخت‌ها و اهداف غیرنظامی در یمن
🔸
وزارت امور خارجۀ جمهوری اسلامی ایران حملات نظامی به نقاط مختلف یمن که موجب شهید و مجروح شدن تعداد زیادی از مردم مسلمان و بی‌دفاع یمن و خسارات شدید به زیرساخت‌های این کشور گردیده است را به‌شدت محکوم می‌کند.
🔸
تداوم نقض حاکمیت ملی و تمامیت سرزمینی یمن و عملیات‌های تجاوزکارانه به شهرها و روستاهای این کشور که چندی قبل نیز شاهد حملات رژیم صهیونیستی و آمریکا بودند، در کنار تداوم محاصرۀ اقتصادی این کشور، خلاف اصول بنیادین منشور ملل متحد به‌ویژه بند ۴ ماده ۲ و مغایر با مبانی و آموزه‌های اسلامی است.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464896" target="_blank">📅 00:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464894">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh1HKSWKZLQ__3gVjySPTRg2iAJTxMhK9WXRfaSLrNbtY0g29r_cNIbr8XRVBjAy3yhKD05inxYT6o1VwsyM832FPbbRsuQEuuKxEX7a2Rh9vYGbPEzwm4_4kTqlffSib9NJ26Vwxz_PYiAEKBYDaYJQbkL0aRmoC1Gi67OfJt_pDjyRlio8x041BZOzb6wv1nn6tms569QdeEZc0hmGIDRv9YMFHXLaJwS1SsaCHdcm5e_YVpEzl7wwM78MauU5xvyXHLn_qrEn5P6eHeXNnFDKv_7Dqzyk1WCcv3__hkC2rrexXsPl1Z-S7IpncU1iCGI7vBs4iQ_yaw49EAKs3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عفو گناه‌کار
🔹
در روزگار پادشاهان ایران باستان، یکی از نزدیکان و درباریان پادشاه مرتکب خطایی شد. پادشاه از دست او بسیار خشمگین شد و تصمیم گرفت او را مجازات و شکنجه کند.
🔹
روزی پادشاه با یکی از ندیمان خاص خود دربارهٔ جرمِ این شخص صحبت می‌کرد. آن ندیم که با فردِ مجرم خصومت و دشمنی داشت، به پادشاه گفت: «اگر من به‌جای شما بودم، حتماً او را سخت مجازات می‌کردم!»
🔹
پادشاه چون این کلام کینه‌توزانه را شنید، پاسخ داد: «اما اکنون تو پادشاه نیستی و من پادشاه هستم؛ پس رفتار و کردار من باید با رفتار و منشِ تو متفاوت باشد.»
🔹
سپس پادشاه از گناهِ آن مجرم گذشت، او را بخشید.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464894" target="_blank">📅 00:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464893">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXT9e_tvWQf3wj9iVvplmRiWOIIDGgoVWMmn_OZqcvsycRUfw2079Pm9j4Ri5bhqsujOKHauJS8TS9nBd6ZX-mOHF4Byy1tr8IhFvBEcwkF3wPgMIXatxdKa2kSCcvlVjjmcYutwonwQiWOAS2NwMlzEEDBCkB-xBASD-Ooz5JoP9zQV2SqPrgoKxg-FZjU8YkzA_tJtSwQt7WJN2QpOlD5wGNhjSTrripkBwkrerqQ4-d6_DQZfBnWJ6fO5VX5P7m31EZ1DeYVxPJzfkNwH9pWROEWw3I1IdTH1zQT6qDdnjWHdY7IBYzBqdrtP1xw1lvdc3NevfX94Muu1anasnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464893" target="_blank">📅 00:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464884">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iho83oOXmHIsjGQ4Jagmq8mgMiT3TN6qNSJtLJw0qUhChQPNsl8AjYd36ZPzl79OoMgl3FaJhujYEjkCEXwPIhDEar-eN7NPAKuwnxTMeELG2lB6sz9I85Fa9H61eLSZchG7q4F5_5uSLwjiUFPCxJmOs_RU7X2URQTiTPasvs7g9oKtOgP8jZ38eR4NXx9RpM-9bfsTgeVCPCRmtKm_qY7ekfokW5Nrxbk-71II5qtC0vhiJvM4hTJIaimI8RUhowH5VOc2HBXIpcM3tEhoCW1spSL-Lwu3WY-leSE-9S6TIV-WTPkzuMU9jCc2iKDKXP3U0pwtqV1TSRubZb1r4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVcYOF_cvjAXQY6b23diNYlWoNp463gUiQjv1Ig3Qiit9sUBBXrGiC23hxwkZd-34F7wIXZFq5RxJ26svz8-ZBb7irUaTNC2GsZycniJk9W4AZWAckal5yJtHgiyw9z4LpmRCAY0USxbkqG_8XuNKmJvElNtSePYyh59d289PbhdX4L1WnoG1vnrvuZuEjJkXNttqJe8AuJN-JsNcN-tErIlPoHJM2SSMG1LycdQpNbgcmvo11KN-AcEwnhKQMU0r97-yF1-4-38AcevT65t26XWaC1LyYjS7wkxwqukwSRalhmeX8y5-fTmNlskCtLp6eejZvZ3nf4X_aJgmNoJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bR5FHZJFKnalyGXyup2_8YLjs-1ar7U_5I6If7Kepx-qKKOIEvUcL72g0gTJ5Y_mzEpkZ5F7jfcJHCrgAXZAAV-uU2H5ipfXBE53-rG6tHigNfs38cXJOyr1z8-xnhM3fQTpkILii4suJVC3cp8maX-wDAIBcLiSJyoeZGnE2MHUYVeoQ2ElYTSew9REPPUXzBU1e74Nl2C-txdBc9oIkTcH1_FLNe3cmyfQLpx7pfIYqq_tpOFnguo1ztN5N4i037uOD02Rmuh0qoTVP6UivUbuXqyk3G-ch9ce4uX6yeA3NYSOg6_-WvnXafPL8ghxJn-WYDAmMqweEqfzFALtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRr24o0ZaDQjJNPXMQ0N2ec36mA6meJFzqZTDwvnyNChdQ-YxsjkA5YpmF_pP4SaQ-_UWem57rNIMTgRwLFflKW4FFtG7xF3QXsX5LyUYKcHumW0Q4_ELCFtTgH88ijpu6yRCqEWD9tWvoX-4xNlkiS72VFFeh34urY_s8_gWQy_oP1FybMpqmuRLTXcTWsAuThv2I7TzgLHygHZ4GYVbAJK8nbbFKlEFanBEUBqjpbeVmwQmb3dw8FcBJWUz1Q8hQqQqx7FEDndO_xUPRLDLr6Q8-7wvdOUyPv-Ht-OSZjpy0r3tV9B9ZQDbF4u6oUwfRqi78RpslvpRrgPAjICXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyjMzC5PprXgUqi3MlxV3NlIoJM_QEc7f3GUWaG-wadMDpN7xkxcs4wv0k0sNt3YMBEiwRmBb9gsmojELY0KD8COdINrhwlZ6JheiuG-Co0SKYglSEcGvTw9EHR0UpwKPdYKwfLR0gQwUmSeAuD4pqAIaa5HuxrTA3gxDiCSHaNYkN63jCWNQKyBm1dJaVtV8-Z7-qokpTVsQezpXLaa_qfxe66JO9YVpm_NT2ZQmu2JvFGJGhuNitJ3mWzTO9HPpYf-4KRTajuP7q8hOAwhBTOiUfXrY91Nq14NYOLq_Mey2uXUDl9CW13KF1lXdb5I5sdl9GAXf_79uS9bjeWj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTh_PI4AlKh9TQmpcqX0LF6WYq529HxULlVSB7O9SRQ9vUcXBUxB-ZVcRQwC6iT8d-FVYwxWyUCSEt3RSrjcInSv1lpTbzXyJSNIGBvGTAsR44Nu4GTPWKlynoPZVAoApX7wtrZkxagUJWeLK-RoMbPs4LDRnjx6POPQqBrYNIsmECa6uykzS485EkpXVtRCuBUR7WH-pLyP5bCtm_WDM_SIEvabatBbHDtrgvcWPn1WMoKWDyrZFVKBaaDEMZ76tv2hrDxQGNB2B-u_gtLDH93LBT08Y4h_zANd_23j5Ho5xEb69D719ETb9zipNhXfatf5YpWZBLNjKERDohSJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHfZtiAIQzwPBL3bOxERuqqK1e1r2W7KWXOfMTRtLoUUxVs5ye3DE6gLNo_eszKQETnpo8m3_0xKn8wC-KmoKAA7WwDq_lNicqYBNYKqTlPo1_I-WOh6TTuMOZJM0j3glBkrwfuREtpncjqB0afRWQVk6wW_O07kp0ECL7K4BHOzmDt9rKBgTUxNIu4tsy2yTO9djd6pg_9DX5aaJjptel8I4F3jCEHm9tv2ZJn0Pg_UWEI582aLREi4D2-jSli-ogADL7b1RR6fkYddK-QRWL9DgBli2AWXxXKmJJiUv7phfkC4jj2P_DHScdoMMnQ2yzNQWCqhKrVfda6zoKW4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVRRKZZ8VFZF-1OeJpeI_HAYO_GXRxOIuydj5h6LHPORnu1w9lDrOTb8NEr1P_D7KBVksVdjqf0vukDEEf1WGQCmEGYkcKiPvvL-YbBVckG-H-UCouX5IOLHZZ7GdYoPFpujcwKwgZtJ_m-SLzDgXVV9TFemyKZyn8er4b3a-FnelebHxkTvKWRrYd_FbonOMlotMhhrBtZu9lQ2G5SdKMEVGveLLX739Pivncdbyr0yl1JwwcH7Mw95zhIlNqohKAa0B0oBpz5sgCTIJR_mv3NLnkwl4zOIutmGQLoHqx322C0SsZPlC0tXPi3Zqh7yzhF3wayd21rhCWusKm2hQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBQtJ0HgaEuil9ubqs-3rQCDR0oRFtKSE_Kp9DcoOqkXAK7kXY4G7qHUTCy8owc-fHLBvjW2lL4Bk0-iBBGXBAnLJ4i1j4YimmP_9cCQj9HYtGaBnGQF81ZlriQAltd70261ac_8LJg18a4sPvKeej_BW_jANaWtrgIrDhU3fb_EsWz_3iy3Kra1K4rUiYO0H8GMhCWFyHFKj_7YqlH7psbs6ebn_cBSoWzJa44PmMFdEo9aOll6Jq-3RdhilAjYVgdC_Wz_JBAEeyp3XT3QfnASuaJGqQiNFA6p1sHFvZaoP890LQFQ_iGNsj8BdO-tJFkTHLT2vNIOItg9U5WVsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رهبر شهید ایران در قامت پاسداری از وطن
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/464884" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464883">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506ad2cc04.mp4?token=dFD-X3majY5cnUc_dixf1tkpslq5v-0gN_Y8ZDsYc28Ezcz6UG4zeYhIErnEHz_1ahN5pinJHWqSjmC59lCK4ZX3L2_Ejm0NomfzpmX8J9i705m7biBoxZCB-FjS6cuwGlD3kRz0Hf4jcUEId7L8GYZPpTIwFyLRg9axeK7d7tsbBgdS3uEJXq2RSeNyAKgsT3TedN_w6bEy8I3I4-JnPsM8WuhtZj0rFAlqfY8Q_FqsxhkuzTuQFupJic4l1IAmXBbsNR2DG_L7b_y_qj6jml7uKXv-CHeTWWnZ-Fr8BARNGhragYq_utMpo87YjHHiFckoK-ORjpPZRHt8HGbp9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506ad2cc04.mp4?token=dFD-X3majY5cnUc_dixf1tkpslq5v-0gN_Y8ZDsYc28Ezcz6UG4zeYhIErnEHz_1ahN5pinJHWqSjmC59lCK4ZX3L2_Ejm0NomfzpmX8J9i705m7biBoxZCB-FjS6cuwGlD3kRz0Hf4jcUEId7L8GYZPpTIwFyLRg9axeK7d7tsbBgdS3uEJXq2RSeNyAKgsT3TedN_w6bEy8I3I4-JnPsM8WuhtZj0rFAlqfY8Q_FqsxhkuzTuQFupJic4l1IAmXBbsNR2DG_L7b_y_qj6jml7uKXv-CHeTWWnZ-Fr8BARNGhragYq_utMpo87YjHHiFckoK-ORjpPZRHt8HGbp9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معنای «لبیک یاحسین(ع)» در نگاه سید مقاومت
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/464883" target="_blank">📅 23:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464882">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgrCWH8XDuoJfdAlHqrMmN2DwzWZ4ey8uViIsjeCh-AJLX9KEAZR7_o4Yejfiqn0eU2NbHg8eXlEdNcW_Qj0HZ0ZcDCuU7oRM_qp5G-F0YpObZ1YIiYoRTxPLHOpYc2fXRcVXfKwbYGoLkBzeP5fOrjI3fyPQXB0iXcVDDhzuInFEZBYW5nmLkhhkNtMI64wyJIhk5eKNTGlh_m_9JQYkDU7IPYmyR2tf5U9U8sxxLqpaaBFoZxb7frVT4JAH7dQD4uk7DEiUH01_d-_9Dm7UrLlArIl7wph8yKbVEv_Hvg8GG3a1DYwM71u1lk56OMZZSPJIVFo6vu71FH-yow1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه: تنگه هرمز نه تنها باز نیست، بلکه شکارگاه نیروی دریایی سپاه برای زیرسطحی‌های آمریکایی است
🔹
دومین شکار هم صید شد، این‌بار Mk 18 Mod 2 Kingfish؛ یک AUV پیشرفته، خودمختار، مجهز به سونار و ناوبری دقیق و با ارزش چند میلیون‌ دلاری.
این فقط یک شکار نیست؛ غنیمت اطلاعاتی است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464882" target="_blank">📅 23:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQt6VgUFXKKimnKCQdkIAC_PKnOfdDPd7SXL4N9Faedwp7botIQis4eXlB3U1fNFwBmNJ9ibizLtCuyXcTaLb52xSdCz3EV94UfInNR9bRHerKEYiFb55TLN6VPPzrEjVLyLAwa7exxWw9OjZ5FgnV2wWfk1PBLmFCA5S8OSaGIvgqMqjohH_6lubaKcnkLYtQF_ORhCeNHioNt2DjQR30Ju2mt9bBttZIk0ZrCEqEd-A8uN0ficyaNvdbd_rP091-nVluQe4mfTL5xC8X4zaoQYr6wkwu3PO0Ol63a3lYaFIv8HSNFByGBjOTfrx0gvqY9Uz9Ct7no413DyWcDWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR0lTI5m7AcqyNNFjlixF4Y_8uohWaPjJtTIoCg7ZKFS1xT9aY9ZxsKNGDcRT7nsUka3ID78Txh2M2XdtKLjqtHdfz7bl9ZsH_UesV8d-lu1328PGg4W6EH9zA8NKRWTUQKRiQf4AIiGaXG-WPB8OA9dUvzrFQLVve3ofzGs1dC7hTp2_S6XZ9Wa2sX_LDbH56LieUVVsX24zpDAzdK-PUnzgWqcrM6cHIPdRgAu1zsStd0jYes5t4WKk95H5peBt9RrXKEfPb7meoP-2ZTylw5mx2WOBhZKckT2K1KdbEryR62pp-CQNZjVhw1cqkYwdz0Hls-7C1xwpstKCO1iHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h61yHCTwAmZHTLWO6hbbgNoi2j_lHT1syUZCFlirU__1CFBE4rvxi1_Ncm36LVuV3x_qAfdFtnYWftp2gxJ0J0-05Ud392ZvNa1RrkO8lZf282--puN_lAtT9WEC8oC7utRBC6SfSgGc2SET_kmAgRZpSh_J53uinuNLxy1x0ejn0iw1f_WA0jgyyNCZKtUktXJabB1JfqXKiWS2R2m8T6MMUuSVvHf2BzoTxbXV5-Zr8xSg--i4tertlumJFJ9KCQ3zt5WxM00Rzvk4Vu-w35ExKlKOTumtWWNKzK1_2DAJBNtEtw_DLHOpdPXn0QWUJLFp7WduM4eU4E3ie4_UAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myvO9VgJbplQtEM3Vi_IG9goFwXKaCIVLQewxmC9e69rsLMzcFfkjTVHRUpSymKb52b9B3U3RT_LWOMh0092kXdbR0QvrMPUAHdfpHdJvXjMXowlDB2Yab5ptsUlpxdYgnfppXNXnHjEqY7R1YZk596_G9NvfJyQ9CxtnKOxw6ZhchCZp2Jdfw-wr-egQM9mppDIv1rbVjNyQctbqq1ZfyX9mApQ3fM4mrPFe3AwFWlJumxSNacVYVXXKsG0GbdIDwmPN-LbgEN5Y5VjGVQWTnSDzN-NtfOV602ykBkHqWVTPylaTIF0788EuFFl89Xp_tBpI-qi-vSVH5u4B9Q5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncSWcZXYmZ4vhGR6-X1f5aiIyfzWcT21HTGy45UAwrc7nENJ5CB_6weUFuV0ACGpx2FwBcz25qn4kNkTeF9jT1BRsHxhmvwxP2up_XirmnpQD7GfvUBIS9hEYhzyxMitxrHgGVKnx5B1zYiTvwtNTOZCX2nSSw23TJrohc3hcdoLFOE5IW7R6P9IpHyJlO_UXkfmp7wSnxuBU04GsdfBUzFvMtfq8mZY4D0NRa9rn_P2uBYB2DDgQKFxewA39U4uAqLa_ALANCnmturh8hSUKWQPczxG-40uaJIoM30lLxX3UtNm_4kkTGapZq2JTVJOQvpvPJKUJB1o-SWf_JhxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozWYIAnglRvxZUnlf4eHwFRlYfmqVwo4MPOPPLCrzM3YwZxdj9kE5E5DeD_oPH_K2yqP59n3Gl-qncx8wC-4OiZMdOnjKEuaThxS3L5upppTuUfb8QXkrOHxz27r3sQ2Z5UEMDBx8AktqxLX6LMATUa3vxCQhND_JQOmuv-KvF5e5ijsXEmJuo-raxSsWGg_tUb_WntDgUk9x_NQmwVepKXHnBiU6KQgT9xmsYXVIjbgvJmVdjOfxLlZ_Kso9S3EVcslITn7Xny_TJ-gEXRXceJw2GZ9GGSqVhBl95Sq8g8hvkpYqBNUVvUwql2pQJ4am-GcWNWpG5G83TsvWbK60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peu7vBjI6OeBp7FahI5lmHKfCTRPiuIJfm_8YSaxRGiVvBYuc1r51L2_DSFUdKMYZv597j17vhdH1U3NERoK3XKNB62SmC6ay9Lk8QYscFFDDZ0Pz9VlrFWvKxUjAvYmpVUmblCZmb8W4jBSlcnkSqEYNZ2ix-7eSTLKvM16iW6PD4cAetZXwI8Ral7E3i56An8kvHXcmVhaSh5R3hrUwJ_UH6-ZsFiW_FqDv5M_cYUEGlCEFYjKQivxBDblBE1G605rINDEV8Y5oyFdV7nEjkUW1ubpM2hNQM-OfGpsYHEQAEwk0Sx8gyOlS95_MefDewxvZ63nnp2n0HMPSSTduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6H_GYtpFIpmfXAKe9H8iQJQhY8yMDwK1W3CAL_YB0E3GSpng2GGbuVAfg--1psbKFAmIJNtpmvqlaETq-guiLi5MH48LH1gwlEKUMCtNcjYe6r1WPUxKyCbwW5IehIT9uXZZx07wP9L-GFg6ze9j0_wMCsO_PnGOB69QlvQTSzubO_PZgCezbc7TC2VCq-wkveEqovaRmm3ousvsjtpD17DSIX6rK6WhWZpYK030-DI93xIsZml5Z2gNHdhHLm4TccG75rR7Dwq9YvuJb5w0o_IJCft6QJGGdQpFz1wl_b4bGjowWAUuuFA5ahyiBtJ5CBIk5kZ1erMkzsokdJo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyDiXFHKjUi9wfjksnR9v5Dn7SPPpWj6EJ2G-N42grx01gwtl12a7jR269oIAaGHWpXHrrN3Nb5AXMb7NFL0hpgKvWrsjMiuP_rZ8WGRtska29Pp_ZUwV_D497CGZ7yOjIfml_MOfHisvIaRTCQjaYoKidVZWx9Zy3_1YnnC83a03yyuFiYxM4xjMJFYhE_kZVnO_oSKpKUCGolYhyHWUoBpxCIhXr4MRZT9338kXLWMh4eBrT-4Qi0PUsFY7brHfD1cCKu0Ckc5JpIeua_rIld7vWnsuj_yI98aW9_MvE7B_a8u830QctfPxVKom2UeSsWlPLZyDQ_5IPriYoT1PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از آقای شهید ایران در لباس رزم
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/464873" target="_blank">📅 23:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f73145a9.mp4?token=fTPoHG0Qcc1r7wVcTmZ96OTc52bAfKMYcokAtL0xQZ21vHwHgDsHlHdNqbfhf7J-qyysIhWplkgDEBnWaD6TJURnWrT8vtTo-7CPwJhJGiLmpW5z42xdKTdx6K4GVZoEdFAXc2uT9fZ0kBle7lxEv269vymB1vLqthgbcZbUCjqktxlsUN5dZMsUgOcRZeX1QSrXZL611jfxhETdF9iOBbq_a2qIC5dsA1FI3BD7pUWvVeKAyCNx4JhJpunFjmv1dy8PTryfBJvWV0fuxoYvbHYzfA1QDlmWM1lHOddVAZP-fFKEIcAjBuQqdOb5FCupYEcRtdyq2HWFASRschLkCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f73145a9.mp4?token=fTPoHG0Qcc1r7wVcTmZ96OTc52bAfKMYcokAtL0xQZ21vHwHgDsHlHdNqbfhf7J-qyysIhWplkgDEBnWaD6TJURnWrT8vtTo-7CPwJhJGiLmpW5z42xdKTdx6K4GVZoEdFAXc2uT9fZ0kBle7lxEv269vymB1vLqthgbcZbUCjqktxlsUN5dZMsUgOcRZeX1QSrXZL611jfxhETdF9iOBbq_a2qIC5dsA1FI3BD7pUWvVeKAyCNx4JhJpunFjmv1dy8PTryfBJvWV0fuxoYvbHYzfA1QDlmWM1lHOddVAZP-fFKEIcAjBuQqdOb5FCupYEcRtdyq2HWFASRschLkCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار مردم فسای فارس در شب ۲۱۱
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/464872" target="_blank">📅 23:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcRgSAkgG1cDPdqp3E2YuG45hgYYECxQ4Ma0T203A3HmtNdwlBQGxKXuwwRxB5C2iYyMNGfWB7Dg8vMX1La5agLQEWwovPB9IzrggzNioROZ4b3K3bKiCanELnMuL6cANRlUuYNYCtDwgw0IKwXEo23jQvZnhMnBKmcF2O3eiwmMUgB2CXklp_OmBZKorlDl284hLMcyQzyG3KaBz9r3vNFX8xKGws_OANPS_meAIW95BbW5502kLlkttRBpA3uLWO_OqDQDpDDtbML_1tZQxN1rCamWs-uyDCLHCZTACvxNxwJxw8l11OLLj9H-S6Iw6pTMk21W6i-q27EOylNyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjqH3MDIeBwoQDRy9ydsu0mO1l9iEayCPZIYnsuNdOzYT5fMPFJ3YOPipBAx2VjxqO1UeZMzdJeUJLnnO0iyeoZ-hiSvoFlwuSsPPwiXhNUHnm52sZBr5TxjwzUjBN0-RKAyz5m0sc4f7sxFrzx0PU8P21ZuhZvvH5QQfq-4rBk1MN5QVssC1Ivx1jpjt-PofHfKFiEkZSMGp_GOpO2kyCAc8qdU_n01dAjVBQBzIduvfjQg25NFs-mMBMb-LgWsKV-ftK4kK26IWPwHKgpG-Zllfz0HoBbqJpTXzetvvy3dreOLTS_8c3EkJOZFkh7QahjhlkeDAHpG--u10Smd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7-kiIaBGlhbwGVzALUsvjymi3RY6BewI15B2lROOooik9UbyZIqZjgdGKW-_BGJ0xUNiIMJrc84LrtLmfZCfdI5hr5PL_0MVxFsqCtulNrQOu4y5pL8zr7fZlMZZfwBt-ZykbWkk7EJTYm0j-0lNbUWnks4Vgj1kFWcEWSLAO6Acq_IiReGK5bYBh2gJMCxjOpFREBhFt493SuEQEKJgyFE2RwJlk5Wq3hIzCUGXawnGB8D9bjb7tIDd9IO7D6shYQUaI8i3YrLqAGiCUDK7MZRcNzB4CPdUwBgnYy8MrzduqqhWaGO0j4ASJilIBV-5quLYmecsLqu1kVt9mLKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/na5htXu07vD2WuBtum5eyERUgJv22tor3jJyIfhe8YNi93FmqeNpn_jRGovI6zwZsFLAGHak5pt34GDd1QwJ7HMtEI9jMIhi7VPiii09fdLM9IpSuICM3eDGB1EddwB8SZPttfQN7F-oHYMGwt6hUFPr1LodyUwI8HP938-FHJ199QRxoq_x8FcwNF9lCNUg4i8a7Ho0RSWQnQ1f-i08V0Px7VB3ME5KhssUpFG1sBFx7yveX_kn13HbX4iBnWVfwockEhBp5L8sj8zdW3wx3tad2jQUk0YxthYhgiog7-KMmgUvSHUPXP96vGgHyPv46cKEKoTg7QzoRLB-rR9BUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhgwdph2XNaCTDuAndOc5O17Kz13RESTYfbUiZSMguIuqW2JnBRcmLwS9wV5UAgJHGjXhIybyvZlnlPhiuxt1yGTRkle76JTZkT2BWU1Wc26LD4WEIBzt9PeSF_viOIEAKW5f9nlk_ufez4qfMmtZR7ricFQMvAGTmdv0uv1zNen7uu01qdDtUh3HEr3eTdzYIvA2hFR4OtEMLHtyecM0joTP0MwvLPhzHzsgyKBecAwuA5TSLSQa-ceuWUwfUeNBZ64Rp7bKsjOeYbHIyIsCopfSXJ8RqoW6CDEPjOm63NKACylpva6xYnf2DCuPtFaMyQaVIgrd30CE1lEbUqBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUEE4k6lcJFK_rD8_LV8QZPCIJGHE86OZzEU473X1lR7xFM_-LsI-8fUdQAkFLIJ5LSBs5EgE343RSExrQbqcCYh4cOjv0ajofg1eIpLPms_vfjX6c_PDNI0ZVKgJxyZACn7eniMbO77P8n3XuLvesWxTKCA_ZVMGH0h5SiygD0cQ05X8vkrOmPDEQc8q7hCC9ddW6FoiSH3KWLB3majRAh9Np1H9hIUlcNReQ1hnT8ShzsbS-eKRyHY1M2vJE9IsXDC_J1FFaHGtKVlz8Syuac_MLkv6M8OIU5Tni6DZO1rh2_s6zu5Fy6fRScLce0SYhgujgqAWI1-IT1qmkbCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k78lQyOd-t_UtxkF-O7jHkLu9pRz-ga6a4lm7QnqPzFEIGe2QncTQmwNtWpWeoT_LwIU3iYnZI57fk7ZPaIT04Woi684_I8FZCEDzb01yyX07dhT_p53wp8r8jlL06O0kEhm_lTgxy98BfKHVDGJRO0G1CRSO_345R3arUqt8ILilYI9V84jtbudVc7DmYgUn23omUsEmv_A59-tEQdP-WF-nQAZWiZA7lyiHSg6Iw1p_bUGLPOgph3TDp9EHCwRJdFS_k2Ol5ZD_ze1R558BD0W14EV9CY-Uu-tsw1RnTMmp5zRnPXhetSYnOzfBNPDg_6UcD5ZtHIQIiBskd0Riw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت هفتمین شب رحلت آیت الله شبیری زنجانی در حرم حضرت معصومه (س)
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464865" target="_blank">📅 23:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCXPvsrlWDs459yCykvux6hPRRoSQKciag9Xb9MgzkNLUM-UT1Nmtislkv2GTC7-rK_GjxlTxaxDqvzUdB3RMMWzIKpkn03DV64WimoH0YUhIFZbUlDtejGns9k-46tl-yIl5CqQuyT8JdHypdlC9KS_2IP572GvhjNLC0Zo66Fh7J0xtTWt_XUNqwUNq95oMPWrUx9B4-s9LMFbFKk1UASHOUHkGb7NpZFxjqUM9u_flPRw_vHp8ayp9clKtXeeQrQPVWufrvm1I-TaniVWxLM7jFY12r9ofBcW33gm2n8KnMGIazQ1PhwwB3tdNSTO_DLsiXN1q1DX7wE5Cox4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس فروشندگان را پشیمان کرد
🔹
تنها یک روز پس از خروج ۶.۳ همت پول حقیقی و افت ۱۰۴ هزار واحدی شاخص، جهت بازار تغییر کرد؛ شاخص کل ۱۲۱ هزار واحد بالا رفت، ۲.۲ همت نقدینگی حقیقی وارد سهام شد و این بار سهم‌های کوچک‌تر بیش از بزرگان پول جذب کردند.
🔹
شاخص کل با رشد ۱۲۱ هزار و ۴۲ واحدی معادل ۱.۶۹ درصد به ۷ میلیون و ۲۷۴ هزار و ۱۳۲ واحد رسید. شاخص هم‌وزن نیز ۳۱ هزار و ۳۸۸ واحد معادل ۱.۶۳ درصد افزایش یافت.
🔹
امروز ۲ هزار و ۲۴۲ میلیارد تومان پول حقیقی وارد سهام شد؛ یک هزار و ۴۳۷ میلیارد تومان به شرکت‌های کوچک و ۸۰۵ میلیارد تومان به شرکت‌های بزرگ وارد شد.
🔹
ارزش معاملات خرد امروز ۳۲ هزار و ۴۹۳ میلیارد تومان بود که نسبت به معاملات خرد ۴۴.۷ همتی شنبه حدود ۲۷ درصد کاهش یافته است.
🔹
بازار امروز فروشندگان را عقب راند، اما تداوم این برگشت به افزایش مشارکت معامله‌گران و ورود پول در روزهای آینده وابسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/464864" target="_blank">📅 23:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihlPCrOuNzLupueHxI-wOITGqYkI14L094klt-UDBdkh0OnatZVKiQ5Qzzk0Ci6_jvyyeySeotX2DmEASCvwcPznTDrNz6mEXacp8iomP6N25DSM5PfWU7qIzs9VY9tHeNDu2P1V6ewIV2V_2ek4d25hWSSue48sfUlZgjTQOFLLdN82hYingiO6CjaMKy2dYoxErVvODf2vklWcpmX5roG_xjHfsr8AR2IbFdVJHGFv4A16L2UpDHgz6AFxblRYA3WUi5MX6IvRinRZ8j-S-NJEI4SwLKs6ALvlEZEr_6qgGCCmTEOTq6T3fVhKCON1wPrsrLg-O5bi72BXYA68ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربهٔ پليس هرمزگان به شبکهٔ احتکار تجهيزات نيروگاهی
🔹
فرماندهٔ انتظامی هرمزگان: دپوی غیرقانونی و احتکار تجهیزات تولید برق تجدیدپذیر در بندرعباس شناسایی شد؛ مأموران انتظامی ۹۳۲ پالت پنل خورشیدی را که سال گذشته از مبادی رسمی وارد کشور شده بود، کشف کردند و متهمان پس از تشکیل پرونده به مرجع قضایی معرفی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/464863" target="_blank">📅 23:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1PnhfSy7QIsyyHhwvgQNmq0aV7_HSnIuzF_tPERCIBtFKdHPlqGJDErZV15GmwXtY4xOQC9RA3nBjyAjs2Z9okJxRPOCnzSig8M1344oTQD1aLaRQVjvlGu4MJDgopxvyAAjZXUrqJreabXArO3B1VBywrd8RH4DqOGlXi1ChmGe4b-lIn_L5F8IQR7X3b5pfDh6AG_mxeHg0LwQQYmf0Wu_eLaEHU7x3xO20rv1xG42H4-tQZqzg-S1FcHnKnmTgLWPNROv6w2Pr7XxiNl3I6g_R0i75rk2cuBcuQZ4urToDbdWj1zfvskaujScEs_IO2zOwzaAWwg5dDnEltQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
کانال ۱۴ صهیونیستی به نقل از یک منبع: سربازی که در غرب رام‌الله زیرگرفته شد، پسر سفیر اسرائیل در واشنگتن است. @Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/464862" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL8ObSlCddLgAQA3gomivFnnEcPV66Pfy9vdj2w_ZTLACzkXWyYRozZYbmptwCmgFYYYzQ_X-yRY1OlGpxjpAT0a9zqU2_m1dw2SIFEbv8i8tyX9vlMHIo8Chyw672UJshYMxzYw5TnzUL38JX8QflsMmauRH1a2hvUkeQmX5wN6s79b6KazfFdHIMZbLs2PQZ59LmK2UDIlBs_efhM_yQlYrH-ZMnQuWPMXdKnqkU9ZYsvuJFyxOnjQ7M9IGGfgMCyHu2XizyygE-ag3P4TAaHkhKCBQ87edD-BlhmDseGlN_gQ0DdqcLZKDlgZTU0X-W2pLBYFGnfvkdETethgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: ایران برابر هر تجاوزی خواهد ایستاد و هم‌زمان برای دیپلماسی واقعی هم آماده است
🔹
در گفت‌وگو با رسانۀ آمریکایی گفتم پزشکیان و من برای جنگ به نیویورک نیامده‌ایم؛ آمده‌ایم تا زمینه صلح را فراهم کنیم.
🔹
با این حال، ایران در برابر هرگونه تجاوزی همچنان استوار خواهد ایستاد؛ حتی اگر کار به جنگی آخرالزمانی کشیده شود؛ هم‌زمان، ما برای دیپلماسی واقعی نیز آماده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/464860" target="_blank">📅 23:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJf05Wm8GfUK5nuC8Cxn6fz0K5LfZlhVkSpO6yN2n3vN2a2Ebuy5O0AtAKHagKRZowERUu_uajZ_59b25QcYqa4bp1umseijz4etC7uQKqwdvFOeONYZdqOc6IL7CkeT1KTvcsBSK0NALkf-N4JqOl1Z3dI01ql-TdSqVbQx2gxyzIsFCxaNPM01aypUHjadidcWuDbFgmaIWnovBOTfSnJrqstteDSw-hzKjGhUZ1KnDTURxIsNVnyvJv1PEd6nw5L324LRc3mJF0acUp5d8c8kv2K0DaN_m017YpoUitf16ger42qyx_wOL7f4hHlMfKmoF8BnvsQDfTEIP1h1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردپایی از کشتی‌ها در مسیر هرمز نیست
🔹
تصاویر ماهواره‌ای منتشرشده از تنگه هرمز از نبود کشتی در مسیر عبوری خبر می‌دهد. این درحالی است که ترامپ مدعی شده بود تنگهٔ هرمز باز است.
🔹
در آخر هفتهٔ گذشته تنها ۵ کشتی از تنگهٔ عبور کردند و برای روز یکشنبه هیچ عبوری ثبت نشد. این درحالی است که این رقم در آخر هفته پیش از آن ۳۱ فروند بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/464859" target="_blank">📅 23:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
قرارهای شبانهٔ کاشمری‌ها خستگی نمی‌شناسد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/464858" target="_blank">📅 23:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
منابع محلی از شلیک کروز دریایی به یک کشتی متخلف در مسیر غیرمجاز تنگۀ هرمز خبر می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/464857" target="_blank">📅 23:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464856">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fadf46210.mp4?token=YTrxYKiP7DQK7xdj4GcH62kNrjd5F4vBZM6jH3GBobHYMdQtkSo47fXY8UqzQ7RbVr810vHXjxt5DV_hdK6UH3o-mNpB5wYWb7mdcve7ukg0ugLfqJGD0ZqbKheutWnU2D-MUtxHhsvkZyfZQwOAx8jqT8hDVZT_fkxZcy1E9Iw4NohmJXcXlYY_gx6fXnSndNp6IPf0JOgyIdaE28RIfaLDAi3ds6nyJCtOZtX7T4yJlO6xTRtXN6gyB97cz7Gn8yuqL_HRVsz94L1WPQL404ubbGekRjGZIksYG0vmAci9J_lUNK5j6AWwpU6IRFXb0XiFXzfSO4fOBp-839Pm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fadf46210.mp4?token=YTrxYKiP7DQK7xdj4GcH62kNrjd5F4vBZM6jH3GBobHYMdQtkSo47fXY8UqzQ7RbVr810vHXjxt5DV_hdK6UH3o-mNpB5wYWb7mdcve7ukg0ugLfqJGD0ZqbKheutWnU2D-MUtxHhsvkZyfZQwOAx8jqT8hDVZT_fkxZcy1E9Iw4NohmJXcXlYY_gx6fXnSndNp6IPf0JOgyIdaE28RIfaLDAi3ds6nyJCtOZtX7T4yJlO6xTRtXN6gyB97cz7Gn8yuqL_HRVsz94L1WPQL404ubbGekRjGZIksYG0vmAci9J_lUNK5j6AWwpU6IRFXb0XiFXzfSO4fOBp-839Pm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دانشگاه شهید بهشتی: باید گفت‌وگو بین نظرات مختلف در دانشگاه‌ها زنده شود
🔹
متاسفانه دانشجوها حاضر نیستند باهم صحبت کنند زیرا می‌ترسند فضای رادیکال و جنجالی پیش بیاید. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464856" target="_blank">📅 23:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464855">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">منبع آگاه: ادعای آغاز دور جدید مذاکرات غیرمستقیم ایران و آمریکا کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌ کننده ادعای آغاز دور جدید مذاکرات غیرمستقیم ایران و آمریکا را رد کرد.
🔹
آکسیوس به نقل از منابعی ادعا کرده بود دور دیگری از گفت‌وگوهای غیرمستقیم میان آمریکا و ایران احتمالاً از روز دوشنبه آغاز می‌شود.
🔹
کارشناسان رسانه و ارتباطات هدف رسانه‌های آمریکایی و عربی از اخبار غیرمستند مذاکرات را جلوگیری از افزایش قیمت نفت به نفع ترامپ در آستانه انتخابات آمریکا عنوان می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464855" target="_blank">📅 23:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486ef75807.mp4?token=Dkeo85-cqbDLh6IBd4hD_CNT9Om7-MhzKvLa1pa5kijp0bXcfDVNxaGli7LxBpfMk2iQh5WcGXY88n07qupSzPjAXXnkNLdAy0Ra0VKMjqAuqxaQhcRdKgk8Pj5BBf3q3sYKUL7t1_3lOyUgrvqSOeCbeo259nk_shY08mnEOammQT1-Na_32vYLEFC-IGBhQwfx2N-PA4-8pVjXJemy5iyzaCbH3pxMi6Jr9vEzYTSZbPbgaRzVKcmxEc-uLjzrLObSh_NORKrenpKjcNDWuiLyBG7BjdutBOKMy606DAAXp2yQYfCfn4eGJInUx6sGR5G3L4Ik5NYeZvMDUZnd-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486ef75807.mp4?token=Dkeo85-cqbDLh6IBd4hD_CNT9Om7-MhzKvLa1pa5kijp0bXcfDVNxaGli7LxBpfMk2iQh5WcGXY88n07qupSzPjAXXnkNLdAy0Ra0VKMjqAuqxaQhcRdKgk8Pj5BBf3q3sYKUL7t1_3lOyUgrvqSOeCbeo259nk_shY08mnEOammQT1-Na_32vYLEFC-IGBhQwfx2N-PA4-8pVjXJemy5iyzaCbH3pxMi6Jr9vEzYTSZbPbgaRzVKcmxEc-uLjzrLObSh_NORKrenpKjcNDWuiLyBG7BjdutBOKMy606DAAXp2yQYfCfn4eGJInUx6sGR5G3L4Ik5NYeZvMDUZnd-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دانشگاه شهید بهشتی: در آموزش مجازی بسیاری از دانشجویان با کمک هوش‌مصنوعی سوالات را پاسخ می‌دهند
🔹
در تلاشیم بستری آماده کنیم تا اگر محدودیت‌ها زیاد شد از آموزش ترکیبی مجازی-حضوری استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464854" target="_blank">📅 22:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9080f8cb.mp4?token=biFS18jiZ-nGxZ-Qncx-bESOxaI4bwhXKgdUs-IGQzC8Awn3aB9VqZk8TL-hWzDKNfHe1sp6KFJ-xdNmhq3RHMvP6RNrtfK_ApqFk7DF0cwFSzkH-MTB8e2bRb7lzX1tNj3y6R_SQdJgu-nXSyU_qjLBSCaR_5FmDybMe3tsxLtCFfnV4yYebfmBUstjziNVEXhbuV_cnv36uEAE5Q4-khpKEeBrC3tbqMoRaFrHxhJ_KYWu32Rd0XbZ0DyndXRLIa2MGw7PbSxs1Ru65FQpIfmH3Pp7jp5mc4theH86Dk72MAeRebITjPKmIqyxo53pkKD2d_jc3GdT2r7cNARH0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9080f8cb.mp4?token=biFS18jiZ-nGxZ-Qncx-bESOxaI4bwhXKgdUs-IGQzC8Awn3aB9VqZk8TL-hWzDKNfHe1sp6KFJ-xdNmhq3RHMvP6RNrtfK_ApqFk7DF0cwFSzkH-MTB8e2bRb7lzX1tNj3y6R_SQdJgu-nXSyU_qjLBSCaR_5FmDybMe3tsxLtCFfnV4yYebfmBUstjziNVEXhbuV_cnv36uEAE5Q4-khpKEeBrC3tbqMoRaFrHxhJ_KYWu32Rd0XbZ0DyndXRLIa2MGw7PbSxs1Ru65FQpIfmH3Pp7jp5mc4theH86Dk72MAeRebITjPKmIqyxo53pkKD2d_jc3GdT2r7cNARH0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید سیدحسن نصرالله: وقتی ما را محاصره می‌کنید زمین و باد و کوه‌ها و دریاها با ماست
🔹
کسی که به خدا اعتقاد دارد امکان ندارد احساس محاصره کند، حتی اگر همۀ دنیا بر علیه او شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464853" target="_blank">📅 22:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16524661c.mp4?token=KGwgxfwEiYItGVNZiJN4lC3_XD4uuvmN01KY-C9rJQQE_--tb-OnBLMDnKZEgLowpAXA_8qO4hP8yhc-BdOi7COdAAg9ubTQBw3jIlqGjY_I0pw6VTHy_5VL1R1g4T_pBLSUn-v-WF9WByQLVEpckP3LzuM8iuprMaLvGZGyXokrCM3RYhHBFvHP_HGAgbb9CcfvQz8tIt6IJ0x8o6wbfnbX3eP5nzFYL2xJIB1-HD2jxMww9QSrywR8Wl6LtuQ6vUK07XJMuOeTVjqmYyZiqxpTg8U8Wk7yvkXUHCwxBJs6fF7jOp-daf4nx2f8EFXFS1prQQXEC1XcYyP6FNclaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16524661c.mp4?token=KGwgxfwEiYItGVNZiJN4lC3_XD4uuvmN01KY-C9rJQQE_--tb-OnBLMDnKZEgLowpAXA_8qO4hP8yhc-BdOi7COdAAg9ubTQBw3jIlqGjY_I0pw6VTHy_5VL1R1g4T_pBLSUn-v-WF9WByQLVEpckP3LzuM8iuprMaLvGZGyXokrCM3RYhHBFvHP_HGAgbb9CcfvQz8tIt6IJ0x8o6wbfnbX3eP5nzFYL2xJIB1-HD2jxMww9QSrywR8Wl6LtuQ6vUK07XJMuOeTVjqmYyZiqxpTg8U8Wk7yvkXUHCwxBJs6fF7jOp-daf4nx2f8EFXFS1prQQXEC1XcYyP6FNclaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نام نصرالله هنوز در جبههٔ مقاومت طنین‌انداز است  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464852" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXXRDM9Yf3_m3genTuTqvE8tspxj7mHyAZhz0iG4_daE3QGRI2OwXYXoE1HeuVYQJTSCxbBpper4qLJv7DSOysy03c_QOgij5l_dZ9KaTzzFuRW7uPCUi2G3zr1e3xzBrVdvj5HZRhA2zOPrvkXtNrwfEyl4IKebsQOsmW7999NEzlgeQmsI4ZTTrgOhGVEQWe52huApU9MXtlUTmCPKP5GxvmjBVR3u8-J4B7FNuSRztHtNHP2ywlakE9r_KjrZ5Cj06RZiicebwxhfq3DxVp0luXVVGTPUiPkrqvBP3R_KMtREzdCVAC4FIwtuhrcVPFYwYO6o0eqoCG0eN59Cpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو در سفر به امارات با بن‌زاید دیدار کرد
🔹
شبکه عبری کان: بنیامین نتانیاهو، نخست‌وزیر اسرائیل امروز در بحبوبۀ پرونده افشای هشدار ابوظبی دربارۀ عملیات طوفان الاقصی، سفری به امارات داشته و با محمد بن‌زاید دیدار کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464851" target="_blank">📅 22:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6927a198.mp4?token=uGvm228gEat75IPg-e6peNaE5TWH6fo_q0VjxRb5X0HUN6GAZlbc32EDcBNQSB3Ai7g5Jq6kmDpfORg5V_4muxCz9IP6L62cLk1Lc53i5R41cK3FM9tVactmrsfKDwvMHbEI4HAKuJUNf4SenfK968m7JAWC8zpymupdHq8W4L3Cu3K8xjAWDp6nSqJWNrqi2gFPLdv2ikPlMMoGnPC7fN0kn1RvtK4K6zoWElkF8xn7Ye6XIhB2f02zBtep4RNqPHGgXBEaPxwVu4X7XycaFMDhbVb94Axmuxa4xYsg12JNlOp4cePodVSs95CkODFTPspnK6Y14dqMb9LvRs0hnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6927a198.mp4?token=uGvm228gEat75IPg-e6peNaE5TWH6fo_q0VjxRb5X0HUN6GAZlbc32EDcBNQSB3Ai7g5Jq6kmDpfORg5V_4muxCz9IP6L62cLk1Lc53i5R41cK3FM9tVactmrsfKDwvMHbEI4HAKuJUNf4SenfK968m7JAWC8zpymupdHq8W4L3Cu3K8xjAWDp6nSqJWNrqi2gFPLdv2ikPlMMoGnPC7fN0kn1RvtK4K6zoWElkF8xn7Ye6XIhB2f02zBtep4RNqPHGgXBEaPxwVu4X7XycaFMDhbVb94Axmuxa4xYsg12JNlOp4cePodVSs95CkODFTPspnK6Y14dqMb9LvRs0hnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهلت ۴۸ ساعتۀ عشایر بصره به دولت عراق
🔹
یکی از شیوخ عشایر عراق در بصره: ۴۸ ساعت به دولت عراق مهلت می‌دهیم تا از لغو پروازهای ایران عقب‌نشینی کند.
🔹
شیخ ابوحسام الحربی: اگر دولت از تصمیم خود کوتاه نیاید وارد فرودگاه بصره می‌شویم و از تمامی پروازها جلوگیری…</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/464850" target="_blank">📅 22:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464849">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GD9rFJqka5BdAMJCAC67GHtgakPK1b9syXCaF4oUqH5VaF1SbCYwCnUkIkvUHYV5hdGbXDSK2wBppSQpq3BxKjcOUKXJOdw3OOWrcJlrRLbEiF_hh2OkCfzbIAV6l20HxPcEmLh0n-XCvxP2Xg2lQ5meAOQm3UajYfR8I5Hph_jmQEWcdDNKAtwT6gEfSIVTdlSCno0_EtXWXwIN0nQ5i8WphqOJV_Fu_XAtJRMWcnYTFt49eZ4rCrfG6g4bmwL7lmcCNSzUlX4ZWtolvPhGTJAuIJJvzW7qGlqI9fDV2dvr_QND2s435IKux6l3vBiynEsPDO0-m00_FCvzB2QgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰ مقصد بین‌المللی در نقشهٔ پروازی ایران فعال است
🔹
مدیرعامل شرکت شهر فرودگاهی امام خمینی (ره): هم‌اکنون بیش از ۳۰ مقصد بین‌المللی در این فرودگاه فعال است و تنها در روز جاری، بیش از ۶۰  پرواز با موفقیت به انجام رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/464849" target="_blank">📅 22:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464848">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_S_zKRAWXOi8oyI-asDN_Mu5Ovx48jn2gdV5sdYg3ZLu-WK7c_AT6nPutC0FEAxA_BHgfYr7rQh3k-uJxgsEMgPfAfguxiF6od4lIGJf8HI8yfB7OdIxhozIRRp_iOKQJPMP7ffzm6kq98QavsdatE--tt6-Y_TDaEUb7sRLnN0JaITPmrkWykcnCx9kvDb1XfAmurciDCKCDVeDWscgVK1JYtHc2xEZyFXcZR1lp0HiIjmry_xkWgb0QmgMhLY9szeDIGLR28mHUY4dTHAh4KT0jpQJMkTU5En4rRHtWE_otz8l-d-2LQNcvAejdd69NxoMmiI9snaPy348-dttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماینرها سالانه ۱.۵ میلیارد دلار سوخت می‌بلعند
🔹
براساس بررسی مرکز پژوهش‌های مجلس، ماینرها بسته به روش محاسبه، بین ۹۳۰ تا ۱۲۰۰ مگاوات از توان شبکه برق را مصرف می‌کنند.
🔹
از سوی دیگر، هزینه سوخت موردنیاز برای تولید برق مصرفی این بخش حدود ۱.۵ میلیارد دلار برآورد شده است.
🔹
این ارقام، در شرایط تداوم ناترازی برق و محدودیت منابع انرژی، اهمیت ساماندهی مصرف برق در بخش استخراج رمزارز را نشان می‌دهد.
🔹
این میزان مصرف در ماه‌های گرم سال سهمی حدود ۶ درصدی از ناترازی برق دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/464848" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464847">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a0a436a3.mp4?token=HM1FquExpFQdmp4cjo8eB-tpVal_YHOp8quWhqTzpcZa7maF6oirdcslSZGZaZtIaTb8Ww1-jv5L3R8gJz7SjAirtO7XLHtnN4-GCMTe604NvQ8EFjtNZU7wDhJfq8soAHZZIMSNImNaWWkcKKa04AjPBxbHHMcJ7asXKheu96ZRZqZ__iM6iIshsPd6WHKKKV2aRBonuL4tMhfauDTy8Ax6gjIOMuRUwz1XX2t7z5S3Y7VrY9PPAG8ZYzZOhPM1osOEvz_KKo0MYBdikFSWDYlMk3W27lLZGdReJn943VrkAQHnUOrAVWKyixfGXBs4QRDCg9WBBi20GbXjrwQGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a0a436a3.mp4?token=HM1FquExpFQdmp4cjo8eB-tpVal_YHOp8quWhqTzpcZa7maF6oirdcslSZGZaZtIaTb8Ww1-jv5L3R8gJz7SjAirtO7XLHtnN4-GCMTe604NvQ8EFjtNZU7wDhJfq8soAHZZIMSNImNaWWkcKKa04AjPBxbHHMcJ7asXKheu96ZRZqZ__iM6iIshsPd6WHKKKV2aRBonuL4tMhfauDTy8Ax6gjIOMuRUwz1XX2t7z5S3Y7VrY9PPAG8ZYzZOhPM1osOEvz_KKo0MYBdikFSWDYlMk3W27lLZGdReJn943VrkAQHnUOrAVWKyixfGXBs4QRDCg9WBBi20GbXjrwQGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر دومین زیردریایی شکارشدهٔ ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
زیردریایی REMUS 600 یک زیرسطحی خودکار پیشرفته و بدون‌سرنشین آمریکایی است که برای مأموریت‌های شناسایی زیرآبی، نقشه‌برداری بستر دریا، کشف و طبقه‌بندی مین، جمع‌آوری داده‌های محیطی و جست‌وجوی…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/464847" target="_blank">📅 22:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464846">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRH7hzJ66xOLuph8SsrhdzawCEukSiUkJ91_eugiOwFkKInUKfLWQvB-uJTqx29_trKY6iV5XNnsLXX57eUfWFZpRFEWBKVfnwl7uMIDLCos8Zi3mhlEUbqcUwpVuarh1guVpX-qHlz6cUAz2kxwpCFmaX8xIopdCg1xBfVVpbOJKMRBqD1pvFTbWixNXeFv1ifw-9uYHtCX_tF9_0NQTo30EtCt3YUy2tIQnYRSxDpE-3eHrAEtDsW7reSHK26TAa_E6ZAiTQoRtb9RP0hdWFYyO9-2ocqPd3TMwP2RaOU66RpBY2C4BZ0MucjqVKYKxqLbbnWHvW4jYkygdpmvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: دولت‌های مستقل روابط با ایران را بر اساس منافع و مصالح خود تعیین می‌کنند؛ نه دستورات خزانه‌داری آمریکا
🔹
بسنت از اعزام تیم به کشورها برای دستور دادن درباره روابط اقتصادی با ایران سخن می‌گوید، گویی جهان را حیاط خلوت خود میپندارند.
🔹
دوران تحمیل اراده با تهدید و تحریم رو به پایان است.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/464846" target="_blank">📅 22:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464845">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0881e6c01.mp4?token=kvoA6Mo4N_oq5AxyElSQMVbgtgRgQvDoh9AVxw6gN4N_djNKhq55jwOW1v9ftg9ix3pC3BbyXhI-EE3lHK9fM9Lp5gn1iOXLKOGgepkZ9CC0421HBqdw63YnO9gX7ukoCyttjQrArakDl2N4m5SkDMiXseESZGsw3Eeu-1W2hvNuFE9bWcHqoS_h5p9LQm7jMrGvpOHubxlI_KbJgf9ZxcPWEcDC6GB7BBzXaDcZxuOFLsLDAKPuhsyhoPxxsmZmN1OLzQQZx6JxcxqRs1Y6wjWB6WQMvq3p4DcfoFwJp2wkur_PN313yr2h7sDBRnnAn0o_qImtbdPqv7iGQzL1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0881e6c01.mp4?token=kvoA6Mo4N_oq5AxyElSQMVbgtgRgQvDoh9AVxw6gN4N_djNKhq55jwOW1v9ftg9ix3pC3BbyXhI-EE3lHK9fM9Lp5gn1iOXLKOGgepkZ9CC0421HBqdw63YnO9gX7ukoCyttjQrArakDl2N4m5SkDMiXseESZGsw3Eeu-1W2hvNuFE9bWcHqoS_h5p9LQm7jMrGvpOHubxlI_KbJgf9ZxcPWEcDC6GB7BBzXaDcZxuOFLsLDAKPuhsyhoPxxsmZmN1OLzQQZx6JxcxqRs1Y6wjWB6WQMvq3p4DcfoFwJp2wkur_PN313yr2h7sDBRnnAn0o_qImtbdPqv7iGQzL1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دانشگاه شهید بهشتی: در آموزش مجازی بسیاری از دانشجویان با کمک هوش‌مصنوعی سوالات را پاسخ می‌دهند
🔹
در تلاشیم بستری آماده کنیم تا اگر محدودیت‌ها زیاد شد از آموزش ترکیبی مجازی-حضوری استفاده کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/464845" target="_blank">📅 22:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464844">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO_-BPOzL6BNjxI-TNVUzf3V5xtLCw-_eFwiw8G06MF8YYN5KzMsFpNjRNhMLHubhOV-rHLSK6G4nrYMa6ScH6H0MY4Lvy8t3QoPyXGttS-7HEU_-b1TtGDIuO3iOH9ph5z69REodihPBrRK9xSitJHr8fn1E4wYFzhWs7OWX9MzRgKI5l6gHH16YqXgJ5fumTC2J6Fbi8Wb0NUa7oKiuxYF0l704Mbbgf7axsqFIvrox_a7NpeKUz9tRpqbUyxjsOh05TKqV-aLKdjbPBtW3d9saGSS8ZemQFcCjfOlIkIZmtBPUIZ8JfCOd-F4_KBCITn1cXDVFydDk-d5MB4dpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت معتمدآریا به ایران؛ درِ خانه باز است، پرونده قانون هم باز می‌ماند؟
🔹
فاطمه معتمدآریا پس از چند سال زندگی در خارج از کشور به ایران بازگشته است؛ بازگشتی که حق طبیعی اوست، اما پرسش درباره سرنوشت پرونده‌های قضایی و مواضع سیاسی گذشته‌اش همچنان باقی است.
🔹
ایران خانه هر ایرانی است و مخالفت سیاسی یا سال‌ها زندگی در خارج، حق بازگشت به کشور را از کسی سلب نمی‌کند.
در جنگ اخیر او چه موضعی داشت؟
🔹
یک تفاوت دیگر نیز پرونده بازگشت معتمدآریا را قابل توجه می‌کند. در جریان جنگ اخیر، حتی شماری از منتقدان جمهوری اسلامی و مخالفان حکومت، حمله نظامی به ایران و کشته‌شدن غیرنظامیان را محکوم کردند؛ اما موضع علنی و قابل استنادی از معتمدآریا در محکومیت حمله به ایران، کشتار غیرنظامیان یا فاجعۀ حملۀ آمریکا به مدرسه شجره طیبه میناب منتشر نشده است.
🔹
این درحالی است که او پیش و پس از خروج از ایران درباره مسائل سیاسی داخلی صریحاً موضع گرفته و حتی در لندن گفته بود تا پایان عمر به مبارزه ادامه خواهد داد.
اما پرونده‌های قضایی چه شد؟
🔹
معتمدآریا پیش‌تر گفته بود پس از اعتراضات ۱۴۰۱ چندین‌بار به دادگاه احضار شده است. اکنون پرسش این است که پرونده‌های اعلام‌شده چه سرنوشتی پیدا کرده‌اند؛ مختومه شده‌اند یا همچنان مفتوح‌اند؟
🔹
او در خارج از کشور نیز مواضع سیاسی خود را ادامه داده بود و در لندن از ادامه «مبارزه» و «آتش زیر خاکستر» سخن گفته بود. علاوه بر موضع‌گیری‌های براندازانه ، مطالب وطن‌فروشانی مثل علی کریمی بارها در صفحۀ او بازنشر شده است.
🔹
برخی منابع مشکلات مالی و دشواری زندگی در خارج را از عوامل بازگشت او عنوان کرده‌اند، اما این ادعا تأیید معتبری ندارد و نمی‌توان آن را قطعی دانست.
🔹
بازگشت به وطن نباید موجب بسته‌شدن در ایران به روی کسی شود؛ اما در کنار آن، قانون نیز باید برای همه یکسان باشد و قوه‌قضائیه باید دربارۀ سرنوشت پرونده‌های اعلام‌شده شفاف‌سازی کند.
🔸
خانه برای همه ایرانیان است؛ قانون هم باید برای همه یکسان باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/464844" target="_blank">📅 22:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464843">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVKPDnyzsQXohq3Ps8CPGwcDhoIEOZB4uCR-jWALUV2fwGun9JSq6tuFZpj1rkyew4NTkAVvXATXgizV37SMD8iFC_I5GR09ge_q5zZSTJNW2NLGaQnkh5yExiOVHXz6inJNb1wh6LZi0WYWsj6hAJz6Tyd6aB5tCvT325GoCmhOBNAZeZbaicz5ebw9cqGQVAfWmsEpOVnpnsTq2qPiXkI-V7hTPm67umGNuSMp1TiYKGGNny64TFWq9h-dSonZuCSuGZoSJTcHTWYmkmd3QXzBlh6Xwo5dn-JXOJK5ldzzpZU0fSUtR7q2eSHBhsARvpOkGNBiKH9laT5j_v35xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنا و صیادی در دریای مازندران ممنوع شد
🔹
مدیرکل هواشناسی مازندران: به‌دلیل وزش باد شدید و مواج‌شدن دریا، فعالیت‌های دریایی از سه‌شنبه تا پنج‌شنبه ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/464843" target="_blank">📅 22:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464842">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad59e31267.mp4?token=pP4t65dXvjL5Hb1C4F1rfbTv9DJxkrlxuK3xuvQ9uq-U1o0JBjUcmWSKpNisHO-eVUNbRQhgbqWS3kI5pBCQkunwKN5M8Meo1zVbSpM5Dac8pLZQL0R8lCS1kToWDcSZmiT5Y5tLixRxNUP_m1zmYKETSm2ARIqTaCxApihJDlmAXEcE7efPVWStHgOmKlWuGqXUV0eCHwsySyoiLOPI208oZdvTBQslpYTzi5D-diZxTqdLMAhiGUoiN8nsDm5i5W4r1gPmyVBmvx0oZm_tooS0aQZhw45cE949X58pWwgAmBKx43rhWBUqNaBmMdYgS8NO4Ya0qAep6wvn7xHYkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad59e31267.mp4?token=pP4t65dXvjL5Hb1C4F1rfbTv9DJxkrlxuK3xuvQ9uq-U1o0JBjUcmWSKpNisHO-eVUNbRQhgbqWS3kI5pBCQkunwKN5M8Meo1zVbSpM5Dac8pLZQL0R8lCS1kToWDcSZmiT5Y5tLixRxNUP_m1zmYKETSm2ARIqTaCxApihJDlmAXEcE7efPVWStHgOmKlWuGqXUV0eCHwsySyoiLOPI208oZdvTBQslpYTzi5D-diZxTqdLMAhiGUoiN8nsDm5i5W4r1gPmyVBmvx0oZm_tooS0aQZhw45cE949X58pWwgAmBKx43rhWBUqNaBmMdYgS8NO4Ya0qAep6wvn7xHYkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اقتصادی وزارت تعاون: کالابرگ مرداد و شهریور کسانی که نیازمند احراز محل سکونت بودند فردا واریز می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/464842" target="_blank">📅 22:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
در طرح
مسکن ملی
، هیچ شفافیت مشخصی درباره میزان آورده، وام، نحوه تخصیص واحدها و روند پیشرفت پروژه وجود ندارد. با وجود واریز بیش از ۷۰۰ میلیون تومان از سال ۱۴۰۲ تاکنون، هنوز واحد مشخصی برای ما تعیین نشده و هر روز نیز با تهدید حذف از پروژه مواجه هستیم. نه تعاونی پاسخ شفافی درباره مبالغ دریافتی می‌دهد و نه ارگان‌های ناظر پاسخگو هستند. حتی مشخص نیست چه میزان دیگر باید پرداخت کنیم و وام پروژه چه وضعیتی دارد.
وزارتخانه و دستگاه‌های ناظر، روند مالی و نحوه تخصیص واحدهای مسکن ملی را شفاف اعلام کنند
.
🔹
واقعا
هزینه‌های تلفن ثابت و بسته‌های اینترنت مخابرات
برای مردم سنگین شده است. تبلیغ «۵ هزار دقیقه مکالمه رایگان» می‌شود، اما من دو ماه در ایران نبودم و تقریباً از تلفن ثابت استفاده نکردم، با این حال هر ماه حدود ۴۰ هزار تومان و این ماه ۵۶ هزار تومان برایم پیامک هزینه آمده است.
🔹
در بهمن‌ماه ۱۴۰۲، مجلس شورای اسلامی مصوبه‌ای برای
کاهش مدت خدمت سربازی
با احتساب دو ماه آموزشی، به ۱۴ ماه تصویب کرد؛ اما بعد از گذشت حدود دو سال و نیم
هنوز این مصوبه به‌طور کامل اجرایی نشده
است. در حالی که این تغییرات در مناظرات انتخابات ریاست‌جمهوری نیز به‌عنوان بخشی از اقدامات انجام‌شده در حوزه سربازی مطرح شد، همچنان مدت خدمت سربازان تغییری نکرده و بسیاری از
مشمولان در بلاتکلیفی هستند
. ما از شرایط جنگی کشور نیز آگاهیم اما انتظار داریم وضعیت اجرای مصوبه مجلس درباره کاهش مدت سربازی به‌صورت شفاف مشخص شود.
🔹
از زمان شروع جنگ،
وضعیت اینترنت و آنتن‌دهی اپراتورها بسیار ضعیف شده
است و با قطع برق در منطقه یا حتی مناطق اطراف، عملاً اینترنت نیز قطع می‌شود. برای دریافت فیبر نوری هم اعلام کرده‌اند باید هر ۳۰۰ واحد مجتمع درخواست بدهند تا اتصال انجام شود. سؤال ما این است که در این شرایط چه نهادی پاسخگوی کیفیت نامناسب خدمات اینترنت است؟
🔹
چندین سال است
آب شهری گرگان روزانه حدود ۹ تا ۱۱ ساعت قطع می‌شود
و این وضعیت انجام امور روزمره و نیازهای ضروری زندگی مردم را با مشکل جدی مواجه کرده است. با توجه به طولانی شدن این مشکل و بی‌نتیجه ماندن پیگیری‌های محلی، از ریاست محترم جمهور درخواست رسیدگی عاجل داریم.
🔹
من در آذرماه سال گذشته در طرح
پیش‌فروش سایپا
برای خودروی
اطلس ثبت‌نام کردم
و نیمی از مبلغ خودرو را نیز پرداخت کردم. طبق قرارداد، موعد تحویل خودرو پایان اردیبهشت امسال بوده، اما
تاکنون خبری از تحویل خودرو نیست
و مرجع مشخصی برای رسیدگی به شکایت ما پیدا نکرده‌ام. لطفا شما پیگیری کنید شاید مشکلمون حل شد.
🔹
کارکنان شوراهای حل اختلاف
در سراسر کشور بیش از دو دهه هم‌پای کارکنان دادگستری فعالیت کرده‌اند، اما با وجود راه‌اندازی دادگاه‌های صلح و انجام وظایف مشابه،
حقوق و مزایای آنان بسیار کمتر از کارکنان دادگستری است
. طبق قانون قرار بود نیروهای شورا به استخدام قوه قضاییه درآیند، اما در آزمون سال گذشته، تنها حدود ۱۰ درصد از کارکنان شورا پذیرفته شدند و بخش عمده نیروهای پذیرفته‌شده از خارج شورا بودند. از لحاظ حق و حقوق، قانون و شرع اولویت با همین نیروهای خدومی است که سال‌ها جوانی خود را گذاشتند. خواهش می‌کنم این موضوع را پیگیری فرمایید.
🔹
خواهشمندیم موضوع
فروش اجباری در نمایندگی‌های تراکتورسازی تبریز
را بررسی کنید. متاسفانه طبق دستورالعمل این شرکت، متقاضی خرید تراکتور باید یک دستگاه دنباله‌بند تراکتور به ارزش حداقل ۲۵۰ میلیون تومان نیز خریداری کند. آیا این نوع فروش اجباری قانونی است؟ اگر فروش اجباری کالا در کنار محصول اصلی ممنوع است، چرا چنین شرطی برای خرید تراکتور اعمال می‌شود؟
🔹
از شما می‌خواهیم موضوع
تأخیر در پلاک‌گذاری خودروهای سایپا
را پیگیری کنید. شرکت خودرو ثبت‌نامی ما را پس از مدت‌ها تولید کرد، اما اعلام می‌کند به ‌دلیل نبود پلاک، امکان تحویل خودرو وجود ندارد. چگونه خودروی تولیدشده ماه‌ها بدون پلاک می‌ماند؟
🔹
بنده
کشاورز
هستم و بیش از ۲۰ سال است یک حلقه چاه آب حفر کرده‌ام که با موتور گازوئیلی کار می‌کند. قرار بود برای این چاه پروانه و سهمیه گازوئیل اختصاص داده شود و چاه نیز دارای شماره پنج‌رقمی جدید است اما ت
اکنون نه پروانه‌ای صادر شده و نه گازوئیلی در اختیار ما قرار گرفته
است. به‌دلیل گرانی گازوئیل و ناتوانی در خرید آن، بخش زیادی از درختان ما خشک شده‌اند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/464840" target="_blank">📅 22:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2CgAFNaiAqcH33skuPnh5g4PHh-BEf6mnghJrSPy4S-Y1igRZFlQOMDhNZdokcBxkXX6kUkvxXFAEXoJBViYXUzoNicm1eDoXR4IXEPWb_2_jKHUBcp_tEBQ5GqYRyzGhS90youejRPZbRN8TEAZ4SL2-9OuS1hbRWiieu99dRNrYElK8Su0TTL7uiNA8itjpePRqPj-xlaDKN6mHU9QjZ-OWudTyDiaIwoPQ3_-E3RXXUv-Vlsh0MoGmTGdPtGJCg8asumQMM7_CruPOPSir9PzTZJIEOCzzD9XahMMw8f5Dbef7k-kvHnabNTVXpvRtgzm80omU6svWz0pEfbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مانیتور را این‌قدر از خودتان دور کنید
🔹
فاصله مناسب مانیتور از چشم برای همه یکسان نیست، اما یک قانون ساده می‌تواند نقطه شروع خوبی باشد: نمایشگر را تقریباً به اندازه طول دست از خودتان دور کنید.
🔹
برای مانیتورهای معمولی، فاصله حدود ۵۰ تا ۷۰ سانتی‌متر مناسب است و نمایشگرهای بزرگ‌تر به فاصله بیشتری نیاز دارند.
🔹
ارتفاع مانیتور هم مهم است؛ بخش بالایی صفحه بهتر است هم‌سطح چشم یا کمی پایین‌تر باشد تا برای دیدن صفحه مجبور به خم کردن گردن نشوید.
🔹
اگر با لپ‌تاپ ساعت‌های طولانی کار می‌کنید، پایه لپ‌تاپ همراه با ماوس و صفحه‌کلید جداگانه می‌تواند تنظیم ارتفاع و فاصله صفحه را آسان‌تر کند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/464839" target="_blank">📅 22:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc27edcda.mp4?token=pUqxtVG4tWcY0Y3neoOPlePaIUzEAZj-Yv1KNAqhPR87AfG_rk5BaISA1TrVY1K0bINuXJM3o_izCUuaW--MkWaMwW3a9YiCPBOqpMjFKWsZ9MaEa39B7zDCEOs7oCEGDtadIZBSHkKjMHUF18jwbaJCVFznzR66ElQISLcYaTD93dp-GZ_w-OmTvKN1z6eSGXhBYLHQmzfg3fXi847Lwc5SAlOiZf7Tel_YVc6SiO_PcA-nucYxjYswzdEmbW0lG2VdG4TT66_7EK3w6U3W8BsYNGUJXsI9W7lK7ry9Hm-XirWoWhCOWYnLGKmowg67iDyT9k744cZS0sAUuRIkHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc27edcda.mp4?token=pUqxtVG4tWcY0Y3neoOPlePaIUzEAZj-Yv1KNAqhPR87AfG_rk5BaISA1TrVY1K0bINuXJM3o_izCUuaW--MkWaMwW3a9YiCPBOqpMjFKWsZ9MaEa39B7zDCEOs7oCEGDtadIZBSHkKjMHUF18jwbaJCVFznzR66ElQISLcYaTD93dp-GZ_w-OmTvKN1z6eSGXhBYLHQmzfg3fXi847Lwc5SAlOiZf7Tel_YVc6SiO_PcA-nucYxjYswzdEmbW0lG2VdG4TT66_7EK3w6U3W8BsYNGUJXsI9W7lK7ry9Hm-XirWoWhCOWYnLGKmowg67iDyT9k744cZS0sAUuRIkHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«انتقام» شعاری که ۲۱۱ شب در کرمان تکرار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/464838" target="_blank">📅 21:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464831">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdvax4oJ0kbPR_hXk41b3vD-HFXdzNnjWqZt3ZGAWJRGuZmSXq_5xc7g6NoDEVqV52GCVE-DSPwaqTbkXKIrePkoNkdUWY39HxE6D8JBpRgUTVyNINtY11Eli3LJmwif0d9XLpsSQzNTRl-ZOYL4hd1Ea9y40FyxPfs6bDZwEWaAfUsl2HvfH47-nQzRfwcPRybs2MQGVxks0Be-ne5fStZwndbKs7CKZrSAaIBXAlIUwhvVciX7a1h92fPspbd452e9s27o1VOZZi8lx9T294kj-csVMSzE1lrHBXjIswbz4LxXnvfLj3TJ5WbQTeLguqtANmzkHctp-hr5vCkl_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXBBpslbdnbUEmNVYnGQec2Um6iIKV7tZ7H2PtTkzyBnKiZ_qwmpKiTXeegUa5O0j-37wGJOhos8OebGSf-z4ud4JBJ98dVvOmKFqRjVHW_O97HgwWhC8auOnAqIrppyi5XeulRskpUcVLjllXVIRtVPEdSq4f3J5JkTh1YJwlTJr6OojSvn_BDGzc_hbLwXpCwkUIhnk6uRDCo1aTwR42lt9s9IN3SETQITzF6HnS-nFZRDFulNn6v4RPQZf1JRSCtV4uR90-kqTy3L3XgTJxpo162jFAqxfvR4LKcVrLwl1bleRbXA7Z_NnBQPUexqr74BWXYeVpEE9LwwdGwkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8u7WZqeVEFMfjhK041t-7K2o2467_Ksg_OwUlpZ9YXiACRpTr4Uc4mcpg7IYDmyTCb5JNB-9HHUkzpXnlTzZuhBv1qLTFfNJbiaE-bstBhSA-z6b0jtsxUuHSNRWMXxhR8KD1Hh-6mpfNUxvzITLTUxGM8bpsOymR-1yLu1WeigfqxIflvcMkNG_8h3_B9nMdYLqwoV8c3dHQw8Lh-oXTrTEV0LsZx7OicWX6r-fuqeunaYRftwiHY7gVJkozrNNMa2ehZa9ojAvEAGcoR9BfNpPjBxINXpe_uGaVjWU4-YvBAX5CuE0BpXFpuS1oy_DUfFWjTTTrp3SwN0j6_zQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpcp0rVv6oOP3t8uBz2D93W1rCUauwDg9r3c2piZSJUyH-bIO7gRGgHrS_1r-pBw77DLoYeaNxJ1Q6gaUi1QcTDcVARiziRnfnwZgGnQwkdgu4n497SUsyH4DCoZKLXqMmjD_2ajLVFrz2X__og-z4KQ-7hAaPTJfR7VJ60MZlZYAR38xRhLJe3FLqrbhiBvh5Heq08IcsTuEAHXWlplidc41J81Gdd36LTE83VNu2rM4YeFhSEP4yZDrpSd5cU-jfNqPbTC7GRkvjd6q2SzmaPTFxSC3UqvtPUAyFQtfkhb9zDVfHCSVDpfCCQ7zcWq2D4xXEbPow6hA7Hl4u5ScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOPFmcVHjtLeUv-CwC70i01QqxdSaVxq4AaYGNtbBqzVMBbwsG-zZyKoR5Td4xd2zOIeI_Y_iuR422TOdQWWtHQG7nIqaQktviGo6dRsr23xcMNDS2l0mzt5v2CEYKbulBh1fd9sx4DjHrWzHXOf1F6FyF2CnSArkpVSi2WhMxbQ0w0CTQNAGmqc-Q66_LEX_oBeP4G_F6F90fF_FsTWCRcujyokrm6rOW8YJyH3AJ2cxkEKlJGUd7sCroR_64yy3TjNkPov2ynvjOSKc1EFq1WS6RCZlo94eo4KnhyC462FQEI5JgUfgfD_T0A-kedZg04CXr5-EGZp1zLM4V1xxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RsxA9gAC2cUJPuJMatDXvJlbZRytia2DYhss9rfiOwxUH5zCujhRd20kpmz1fzinrFW-lPW7Zq_PBE7Oc0iEo8i-UUNH5DnIJ3_DJucgB4R7V_TG5nOSKHYMmbwjRpRDbLnDGZLmCvpKF0p7zMy3_-h1uZSfy5b8mpEwwwEUClSbxHaJm7q5sW5bZEmHEk7UfH-U4fLpssjbU2f97HyE7X91FGBCiX_AEgyeqDoXnH-04C7_uOfeU-cUP-KxGnSDv9CPkTtLNARL2ruDd7QnEXUD2gLadpFdkW47rpcnpgpR3qNTF-LuRS-zxKXhs3b9kyedgA5naPwOAgiOvYL7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyC4-zbZ5zv3U4fFlUSPwJSHuzEkwlR960E3_Va2yPwcbI-rFbubaHUlJdWObbqaFUQhaPErs0RNC4m1t8rZCn-O-cXalabsFJdlvFyl9YZHc2EvXrNe8aZDi0-dYbPLVdK--PgA5VL75qlY0UAl1MSxW4bRojz90OTU6xd-1TT9gQ0zzhTeXeRLvnz4xbE8wDxq7oace_iFimXDntV1riCAFr3EjXiLn4cu4TngChhIFzFnwBGNyaFrSAULe3yXARvy3OsWqJgcfA0p7M85Yl2aZ5pLGPY1kTv-hIhcEk8uZAvVk3kIvFNXG8tdid_b0O2HVOXXKdV-8pxOXh4UBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیکر شهید ارتشی پس‌از ۴۰ سال تفحص شد
🔹
پیکر شهید علی‌اکبر گندمی پس از ۴۰  سال‌ دوری از وطن، کشف و شناسایی شد.
🔹
شهید گندمی در اسفند سال ۱۳۶۱ و درحالی که ۲۴ سال سن داشت در عملیات کربلای۴  در سومار کرمانشاه به شهادت رسید.
🔹
مراسم وداع با پیکر این شهید فردا…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/464831" target="_blank">📅 21:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-text">🎬
ببینید
🎬
✅
ورود وزیر تعاون کار و رفاه اجتماعی به اهواز
.
🔶
به گزارش مدیریت برند روابط عمومی و مسئولیت اجتماعی
#تاپیکو
، وزیر تعاون، کار و رفاه اجتماعی شامگاه یک‌شنبه پنجم مهرماه وارد اهواز شد تا در جریان این سفر، از بخش‌های مختلف جامعه کار و تولید و وضعیت رفاهی اهواز و ابادان بازدید و با کارگران و فعالان این حوزه گفت‌وگو کند.
@tappico1381</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/464830" target="_blank">📅 21:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZm1ObiOiKXuVpi61iTgow9m9cEDk2GNJ3LxjHh5lWG_2aoXenrzY99CKFCXugjWBejzVzO81vmSJsS01eEDuu1Zi7_N8-I53KE9N_gCO-zOi-sjlNgkwrgtUxDE_zxvzE_vXs9ZT2nrYaSUcTaGWlfh8FNU9IX9Z_43qaF9w0in3X3f0waJ-BLDPADQZFZw-_KV4kPNaVfSN8fg_R_VgA88at5dTsD3zPkyMDXmofXEL7Aw8NsdZmtQ6irRslBhkxPK2Bb_Pk__5yzWXW4b4lq0Iqql3wVkwkTxdpEl4OaAD9IurW0UJDMF1vaDvO2_D6QsX6O6_5HUJtrwql4DMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❇️
سالن مبله برای ختم
❇️
❇️
همایش های آموزشی
❇️
🔹
۷۰۰ صندلی
🔸
پارکینگ وسیع
🔹
تهیه بسته پذیرایی
🔸
هماهنگی واعظ و مداح
🔹
گل مصنوعی به نفع خیریه
🔸
سرو ناهار و شام در سالن
🔹
فیلمبرداری مراسم و صوت با کیفیت
🔸
دسترسی آسان به بزرگراه
شهید همت، شهید حکیم، شهید فهمیده(کرج)
📲
۰۹۱۰۲۲۷۷۱۹۹
☎️
۰۲۱۴۴۰۰۴۰۴۰
📣
امکان رزرو شبستان مسجد
📌
آدرس مسجد
🔻
فلکه دوم صادقیه،بزرگراه شهید اشرفی اصفهانی ره ، جنب بوستان صبا
🔸
مسجدجامع‌امام‌سجاد(علیه السلام)</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/464829" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464828">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/464828" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464827">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU0BHryJvGRcYHQMZYo1oDoBzPFBWtLj07DTJFemwkYtvm43DnNFXVFBxij5xgtvBS7MqkSBzeZqOMVUJ4Foj9Jj_wPUl_Z1rBerzkLxUBHQAnJhNouZp4-VDwxZ8Mz8chDc4tB2Ny-zLKJ9HsXv_zt3vwnO6kacsKALoe20qzRrTllbU0IYDGxsELDxKffH4F1Ph19rLKMLGpihG_fENdPyZIuvtKo_Ii7By58yknoE7VRryiimyw9Q2ycaSqXWuJVLtj1aAUbiWRAgshx0X1M8kkDSUVogYBcPVCuoRm6GdsiWcM8wLCUwC4uMhDrs2I3hCGs4DsozQoE3MV4G1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دعوای سرخابی‌ها بر سر جام لیگ قبلی بالا گرفت
⚽️
مدیر رسانه‌ای پرسپولیس: استقلال برای لیگ ناتمامی که فقط یک هفته صدرنشین آن بوده  گدایی جام می‌کند!
⚽️
مدیر رسانه‌ای استقلال: اگر دنبال ننگ می‌گردید سراغ جام‌های اسنپی بروید! @Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/464827" target="_blank">📅 21:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464826">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb620bec.mp4?token=ZiEHmxWrKXGCP78vOe0gCgpp0KTK1GK3NhRxYMyxtUksd18JUwYOHd_tYQPD0UVjM_1lE9foZie68pBGnSd9m-EgWDwWDla3thOZVpHWlZ3buvwOUiCQ709Z8lidMEefZgYa07dFki80VEcGy0y8hK8Wetr8_utITSDALIxHEsS7cbME4XiJ36p8OWHl_nEV_UpI9hhh0EIw11eIjQN-ZV3jjfm4e5dmp39UoRRc1kvTBTa0Yz5v9iq_FhGM4IZuSquiAO_GP2D8Gx2OwS-DXFmdf1c-tVg9t9L_MIri_kWlvdeFbOw3m9Y0rk9dwZ3gNssSwqSXueA-3jozvO3LkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb620bec.mp4?token=ZiEHmxWrKXGCP78vOe0gCgpp0KTK1GK3NhRxYMyxtUksd18JUwYOHd_tYQPD0UVjM_1lE9foZie68pBGnSd9m-EgWDwWDla3thOZVpHWlZ3buvwOUiCQ709Z8lidMEefZgYa07dFki80VEcGy0y8hK8Wetr8_utITSDALIxHEsS7cbME4XiJ36p8OWHl_nEV_UpI9hhh0EIw11eIjQN-ZV3jjfm4e5dmp39UoRRc1kvTBTa0Yz5v9iq_FhGM4IZuSquiAO_GP2D8Gx2OwS-DXFmdf1c-tVg9t9L_MIri_kWlvdeFbOw3m9Y0rk9dwZ3gNssSwqSXueA-3jozvO3LkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یمن بازهم یک پهپاد سعودی را ساقط کرد
🔹
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی کارایل متعلق به دشمن سعودی درحین عملیات در آسمان منطقۀ الطینه در استان حجه سرنگون شد. @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/464826" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8a74474a.mp4?token=s46zjKT7XR3GLYg3L1b7e87OFdMbx5MMDxHeZIOkqlXatcVeM3-YRLel2QcLpe_szEH3lIDtgQmvHE0Pc2kAHHxFzqtqnQFsdJXzc_ttZy59UtmRJAn9-K9CzV0EJc9pkAaU4DfS-GkxmJ-VawOA5EfLcwTuLQ2NLJXU2wDt5c1JvhtLSEo6WqbZIt3QOVBmiHrFKeI24X_D1uXmpGwCT3AmrGxVVAgD2ZK49OpLtNfPa0LTItMan3e6Ed7hEv15MpQQL5RDQOOxnUOE9mG7gTW_8wkPESRlM6T1vyvpXVfi_Zx0fR3YVFOIX2NGb2PFO7X7wguVvrHwaul9004G04i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8a74474a.mp4?token=s46zjKT7XR3GLYg3L1b7e87OFdMbx5MMDxHeZIOkqlXatcVeM3-YRLel2QcLpe_szEH3lIDtgQmvHE0Pc2kAHHxFzqtqnQFsdJXzc_ttZy59UtmRJAn9-K9CzV0EJc9pkAaU4DfS-GkxmJ-VawOA5EfLcwTuLQ2NLJXU2wDt5c1JvhtLSEo6WqbZIt3QOVBmiHrFKeI24X_D1uXmpGwCT3AmrGxVVAgD2ZK49OpLtNfPa0LTItMan3e6Ed7hEv15MpQQL5RDQOOxnUOE9mG7gTW_8wkPESRlM6T1vyvpXVfi_Zx0fR3YVFOIX2NGb2PFO7X7wguVvrHwaul9004G04i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نام نصرالله هنوز در جبههٔ مقاومت طنین‌انداز است
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/464825" target="_blank">📅 21:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464824">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1SHhftkjm195uLiK79drdStVG6f6SibpLr_vGsff8YbRcuQ7b-BdX_hn7-dN9xtC0Vwevs5GSHW_Fh2iJQfb7rt4gFtbS8TT-jfbjGYVhI1AKfDdAl3OwoTH1mqp5L4fmNjSQiHqSwejO0imxo28_QnSTknLsHn0U9lk72LGBQ1qkjQbVrM5Xa7Yb20cs8MCLT1JPaOdHaepl4zQxs5wDvzC-RvmjooM1S4CEWFFDWf7YngkhyZixcQknVi2vuzVJd9m2lSaiJ5Exiw03ERVMbXXryiVy4Do2oGddeBdG1kX0p3a5bJrg-GZ_piR4e5JGkSG2-7rs0Te_jAKAb78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز نفتکش‌های کهنه را گران‌تر از نو کرد
🔹
فایننشال‌تایمز: اختلال در تردد نفت‌کش‌ها از تنگۀ هرمز، کرایۀ حمل نفت را به رکورد بی‌سابقۀ روزانه ۱.۲ میلیون دلار رسانده و قیمت نفت‌کش‌های دست‌دوم را برای نخستین‌بار از کشتی‌های نو بالاتر برده است.
🔹
برخی نفت‌کش‌های ساخته‌شده پیش از سال ۲۰۱۶ هفتۀ گذشته بیش از ۱۵۰ میلیون دلار معامله شدند؛ درحالی‌که میانگین قیمت نفتکش نو حدود ۱۳۵ میلیون دلار است.
اما دلیل گرانی چیست؟
🔸
ساخت نفت‌کش نو چند سال زمان می‌برد.
🔸
خریداران نمی‌خواهند منتظر ساخت نفت‌کش نو بمانند.
🔸
صاحبان نفت‌کش‌ها ترجیح می‌دهند ناوگان‌شان را نگه‌دارند تا کرایۀ بیشتری بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/464824" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464823">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce62a9d434.mp4?token=HXTtj60ar7UgLA7UmF9Uhmzw-CIcMENHQ2IbIR2zxpo4j3NzbkBH0PR8MUcPuEsv7IVzeavFb2UI79qhgCfqEofFhavLTcBbFrJMXWp0D7d_-QXd-oiAyqhA5R6h2s38J5bljxrehTfVSny0gy8wtPkA2Lq3nqiZFrp8udh-7T5nlUpe2rw1tdAoxJ4yVRUx9sAItE9VUwSKeoxzzKw33QsfmsivG-0mM2N1mf95reT_hYJHEwwdvS0Iul0cLulvEEKDsqVR8oJjtAtfsjJYFZuBHQfy-11kmnrE2O-hG9tTeKn3bRkbsvyzRaPzQEvgEMJVuImSNvrSWXs2txFW7JI3ScMGgYIQLHd1hz_qg6tlldLk6BOrg-GUE0IMdeChpveM2U9fy55Y-Eh_0x7Q4Y_n3E6iu_eZ9yCJXpFoVgusxkrHebwiwf81pv0tc4Tp-2I7J6nXhokk5M_xUEUW9yIR54SHXjm9HX7UMGs07M-KHWxtQf3bvKyCU0o9faMWXxSVkWW28_L7_CrJBNgHB2yYuwv4GZEVTHYv-jxvghCqfrdqWKxlDe9jLq2-AEWA3qSub8rF4qTDB8q_DYus7stxlzOZO5_AYTXsHHjWVekSw0GlGhX0RHFFjKPvGbs81HlGAATHcGtcA8yhZKF8mltU--DgI868-HLCfUNIeoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce62a9d434.mp4?token=HXTtj60ar7UgLA7UmF9Uhmzw-CIcMENHQ2IbIR2zxpo4j3NzbkBH0PR8MUcPuEsv7IVzeavFb2UI79qhgCfqEofFhavLTcBbFrJMXWp0D7d_-QXd-oiAyqhA5R6h2s38J5bljxrehTfVSny0gy8wtPkA2Lq3nqiZFrp8udh-7T5nlUpe2rw1tdAoxJ4yVRUx9sAItE9VUwSKeoxzzKw33QsfmsivG-0mM2N1mf95reT_hYJHEwwdvS0Iul0cLulvEEKDsqVR8oJjtAtfsjJYFZuBHQfy-11kmnrE2O-hG9tTeKn3bRkbsvyzRaPzQEvgEMJVuImSNvrSWXs2txFW7JI3ScMGgYIQLHd1hz_qg6tlldLk6BOrg-GUE0IMdeChpveM2U9fy55Y-Eh_0x7Q4Y_n3E6iu_eZ9yCJXpFoVgusxkrHebwiwf81pv0tc4Tp-2I7J6nXhokk5M_xUEUW9yIR54SHXjm9HX7UMGs07M-KHWxtQf3bvKyCU0o9faMWXxSVkWW28_L7_CrJBNgHB2yYuwv4GZEVTHYv-jxvghCqfrdqWKxlDe9jLq2-AEWA3qSub8rF4qTDB8q_DYus7stxlzOZO5_AYTXsHHjWVekSw0GlGhX0RHFFjKPvGbs81HlGAATHcGtcA8yhZKF8mltU--DgI868-HLCfUNIeoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌هایی که چراغ اجتماع را اول روشن می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/464823" target="_blank">📅 21:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464822">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWcyNjg2_5FC9NcreWLnSDZCldYIZ8yfixpk0RjxceB8-ING-qRycaQbPNdSH5urOk06MZT8vsZgatZQRx02oiUCRUKKxcFKvtXVNHBkqt8sVyyJvgZe2z3O_z5NtRZLrIYRmMeiwH63psF9Rms4QRY3msJiPbcPfmZygTFrcZichQi4kpxclLAzsDW9iz8Hp1RfkMY7uh-5lNfdna15bBb6feRcJE3tfOdQtmZkGBiPNq-aU3dp9TRRwD2sik81HgqhqCXWnese10eeR3TJVUrOZIA9_sqqkiQ0-4ZYC5TiMtCfQGdT0trESjBpZHHkEm12KMfalrulYp90dIr16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد دیه: زندانی غیرعمد با بدهی کمتر از ۴۰۰ میلیون نداریم
🔹
اکنون کمترین بدهی مالی زندانیان جرایم غیرعمد حدود ۴۰۰ تا ۵۰۰ میلیون تومان است.
🔹
در ۶ ماه نخست امسال ۵۰۵۹ زندانی جرایم غیرعمد با مجموع بدهی ۳۷ همت آزاد شدند.
🔹
همچنین ۲۰ هزار و ۶۴۰ زندانی جرایم غیرعمد در نوبت دریافت حمایت ستاد دیه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/464822" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464821">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usUdkpgpkjsiHSKK9dJpoo0S7XP3NmbmtCeIl_TwoP-sIVrgszZW_17QhM3qv0CL4nJpH6C1HaR4mrbezr3Zgacw3PSGeOwaS8C2YPeW5JLZEzghoHHTEgBrjtAUfsDfefEqj1UjV16GnNDN8uw_7HSHbzR6aACF7QEDqRJkHtnRJLDDABol-wQwDcd-SxJRBEuqjtE25JsDTaayRxcZOuvEt8u60Swulq5toPFdu-3xjhLKE3UYmdGKw8wVi5p4DlXcA512mLQLDabCAch4DhcX-eX1v8MZIO3C-c2BZo9p3r73Ba8PMgMBZKrVMQSAtJv5jnDwiytCRuOwrQhYhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای حکم ۱۰ ماه حبس برای رسایی چه بود؟
🔹
حمید رسایی، نماینده تهران در مجلس، در پروندۀ شکایت محمدباقر قالیباف، رئیس مجلس، به ۱۰ ماه حبس محکوم شده است.
🔹
موضوع اصلی این محکومیت، مطلب منتشرشده در نشریۀ «۹ دی» در دی‌ماه ۱۴۰۲ با تیتر «دستکاری قالیباف در اسناد مجلس!» است.
🔹
رسایی در دفاع گفته این تیتر مستند به اظهارات یک نماینده مجلس بوده اما دادگاه این دفاع را نپذیرفته و اعلام کرده وقوع دستکاری در اسناد مجلس به اثبات نرسیده است.
🔹
دادگاه در این پرونده علاوه‌بر ۱۰ ماه حبس، رسایی را به انتشار تکذیبیه در صفحۀ اول هفته‌نامه «۹ دی» با همان قلم و اندازه تیتر ملزم کرده است.
🔹
همچنین گفته شده در جریان رسیدگی، از رسایی خواسته شده بود نسبت به مطلب منتشرشده عذرخواهی کند اما او نپذیرفته و گفته «دلیلی برای عذرخواهی نمی‌بیند و از موضع خود دفاع می‌کند».
🔹
رسایی امروز هم در نطق خود در مجلس گفته: «این حکم را غیرحقوقی و سیاسی می‌دانم؛ با این حال چون یک حکم قانونی است، از آن تمکین می‌کنم و حتماً برای اجرای آن مراجعه خواهم کرد».
🔹
رسایی همچنین محکومیت ۱۰ ماهۀ خود را بیش از حد دانسته و گفته طبق قانون در اتهام «نشر اکاذیب» برای فردی بدون سابقه کیفری، باید حداقل مجازات یعنی ۹۱ روز صادر می‌شد.
🔹
برخی کاربران باتوجه به این‌که محکومیت رسایی برای قبل از دورۀ نمایندگی اوست این سؤال را مطرح کرده‌اند که چرا حکمی که منشأ آن به پیش از دوره فعلی نمایندگی رسایی بازمی‌گردد، اکنون و در دوره نمایندگی وی به اجرا رسیده است.
🔹
در مقابل، آن‌چه از رأی دادگاه برمی‌آید این است که مبنای محکومیت، صرف «انتقاد از رئیس مجلس» نبوده، بلکه دادگاه ادعای مشخص«دستکاری در اسناد مجلس» را اثبات‌نشده تشخیص داده و انتشار آن را مصداق «نشر اکاذیب» دانسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/464821" target="_blank">📅 20:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464820">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy7K9jm5kozhCwseXrR59HVXQh9qwvBgMAW1sKiPnZNDq1DkVLM62mesFvbXfEZdEVZJzoagIS4DdMfjCOvjnTZyxEbhV4FmXCR79gNC5W4tMJU-Ab4pbYf2YqfiX-0-_Z6_tqNZLi4tRdN7LZAbtZAxs7oLXxF2CkZPSSbAPD7bIfAvzOACUyS0UWe9fRo_bYI7EbsEMtcF6nUN9TeplQR9qhdalpAMI3vt0ko_ovQlZSvfUEZX2fR_zgKPDDdv5iiHA9i-dNgLpn6XJbMtCmD2t9QKe7CsmN6L-Nu5dXBi4HnrJ-TSQX-D_AdMw-CqoR22QDS0wSZx4xQ1Ybh-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعلام «حادثهٔ بزرگ» نزدیک پایگاه میزبان آمریکا در انگلیس
🔹
پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست خبر داد و اعلام کرد که شماری از خانه‌های منطقه تخلیه شده‌اند.
🔹
پلیس شهرستان گلاسترشر انگلیس امروز…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/464820" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464819">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eaf9933a4.mp4?token=KbG6yIovxIeoMfRlnlABjpLH7S3GJr3D1QGPna_4q7nE3pDsKgwlIowIBeOFPC_shQr61ik9hvTubuuf8VP7fL1WIjeBZx24wJZARtXrgmKkmkiHwL5omigivVorMlrnSSNKmwtnRigzQLabhx01HSKImlM_i-l_TJgAnnbhDZjlYk7DUdjOzwj_UAiNmdEDImlUki8TmBt-rwpmAbR-wCWyXNrlT66MAic7KcSXHksQzZYyjyYlgK4CthRQtEQF35DZ85Er4jvxXnpW1edM5XoAS9Yht7gzKTNY-A6goAbDZrOGTJL7auVzUfJoNXoOW2fToSDOXNV6ayYi2PQlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eaf9933a4.mp4?token=KbG6yIovxIeoMfRlnlABjpLH7S3GJr3D1QGPna_4q7nE3pDsKgwlIowIBeOFPC_shQr61ik9hvTubuuf8VP7fL1WIjeBZx24wJZARtXrgmKkmkiHwL5omigivVorMlrnSSNKmwtnRigzQLabhx01HSKImlM_i-l_TJgAnnbhDZjlYk7DUdjOzwj_UAiNmdEDImlUki8TmBt-rwpmAbR-wCWyXNrlT66MAic7KcSXHksQzZYyjyYlgK4CthRQtEQF35DZ85Er4jvxXnpW1edM5XoAS9Yht7gzKTNY-A6goAbDZrOGTJL7auVzUfJoNXoOW2fToSDOXNV6ayYi2PQlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شکار دومین زیردریایی ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد: رزمندگان نیروی دریایی سپاه به‌یاری خداوند طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک توانستند یک فروند زهپاد پیشرفتهٔ ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/464819" target="_blank">📅 20:44 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
