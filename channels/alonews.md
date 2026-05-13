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
<img src="https://cdn4.telesco.pe/file/ldU5m6jlgZaD6v06j4HiQZB9vCJJC85emLDx58iUQW3aGLrAVwVsGb6zJKSlmBRHiYO_3mILmkJYzPbmY__xDHIJmdKHeX_P9IgFHHlRls-z3Pj-bb1ZUEEBBvWERjptlVmiyU595yRKiACTqitboTCgCMq53rtSZL2GyZ8QjWt1OpfjQIlAwoHNOD1fRkQ2rbFXmJtfXbijds9AGbJp6njZuHH7sZNGJsm5ZqdFzVfzsToI_qcj_PvJl_5eD-UEFQ9ncDe9zfFUMM-GrNJNF4GddPSU2s2oHEso6KpIUu6rc1SS8iVO8pp0X8R9AtVaAS5cmuCAA492EmT29S8PPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 960K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 23:57:33</div>
<hr>

<div class="tg-post" id="msg-119820">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff5j2zs7YNFC9ednVUaGBLSUhiCuw3fgaQCuNnYvfjYfqKPNX_BE39ZIU89facKaK7XWO2BkP982OZ5UeRA8hU0U30EclCjdit4PJgYdxMMXRh6kCbjmePDYRi4DTq85xasWVo-qklKggnRpf8tR7vqTG58HW33Oqa_Lwcrc0CN39s9rKccXaDImGEnfsYHyW3ov3IrhWh6wVKbI6xkyTq8zu9ykgedDyQ111A0r6Ay6Zz4_Cle1JGmdi9pe0n5NhNEzBGeG4qjIIARDHCt__QskoQOqYmW0hv3dmbBXZnJxmXim_iin9WfapPFrx8Wvvk92KgX4zMqGobERbhFPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: نتانیاهو اکنون به‌صورت علنی آنچه را که نهادهای امنیتی ایران مدت‌ها قبل به رهبری ما منتقل کرده بودند، افشا کرده است.
🔴
دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است؛ و همکاری و همدستی با اسرائیل در این مسیر، غیرقابل بخشش است.
🔴
کسانی که در همدستی با اسرائیل برای ایجاد تفرقه نقش دارند، باید پاسخگو باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/alonews/119820" target="_blank">📅 23:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119819">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وال‌استریت ژورنال: در حالی‌که نگرانی‌هایی درباره کاهش ذخیره مهمات ایالات متحده وجود دارد، پنتاگون در حال تلاش برای خرید ۱۰٬۰۰۰ موشک کروز کم‌هزینه در طول سه سال است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/alonews/119819" target="_blank">📅 23:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119818">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزارت خارجه ایالات متحده: امروز، وزارت خارجه به‌طور عمومی پیشنهاد سخاوتمندانه ایالات متحده برای ارائه ۱۰۰ میلیون دلار کمک بشردوستانه مستقیم اضافی به مردم کوبا را که با هماهنگی کلیسای کاتولیک و سایر سازمان‌های بشردوستانه مستقل و قابل اعتماد توزیع خواهد شد، مجدداً اعلام می‌کند.
🔴
تصمیم با رژیم کوبا است که پیشنهاد کمک ما را بپذیرد یا از کمک‌های حیاتی نجات‌بخش زندگی خودداری کند و در نهایت در برابر مردم کوبا به دلیل ایستادگی در برابر کمک‌های حیاتی پاسخگو باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/alonews/119818" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119817">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf0426b5.mp4?token=hah0CVcHDm_EunieI60T19_G43Qot7ZhY7m8hRLwLJivfFFXV0iFxjWr9ikKYeENi6EouKxCUSnUKm31GU_a7khjQka2OWHYSI5gfI1XHqQXQIYkf-m6u0H8Hckx8ABy5SbRV5EXta_wL-LDIigR2ahvHYvgq4lq44FFPKcgPd_ArrEpaSVyGHVjlDuPFwJHt4wVB_GtnKkVS-_buSt6r1yZu5OczxCMd7IfQNlDTg-9_m9EuyNU4nAz42a9N8s5CHjH2E6mFMJQ6TEbnRJvLXdGHtQdMeYm8oPjRoI2YF2GSwPkkZ96H5PCLH-gXCjG1mtsJnh2MtSZv-ZXyI6vmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf0426b5.mp4?token=hah0CVcHDm_EunieI60T19_G43Qot7ZhY7m8hRLwLJivfFFXV0iFxjWr9ikKYeENi6EouKxCUSnUKm31GU_a7khjQka2OWHYSI5gfI1XHqQXQIYkf-m6u0H8Hckx8ABy5SbRV5EXta_wL-LDIigR2ahvHYvgq4lq44FFPKcgPd_ArrEpaSVyGHVjlDuPFwJHt4wVB_GtnKkVS-_buSt6r1yZu5OczxCMd7IfQNlDTg-9_m9EuyNU4nAz42a9N8s5CHjH2E6mFMJQ6TEbnRJvLXdGHtQdMeYm8oPjRoI2YF2GSwPkkZ96H5PCLH-gXCjG1mtsJnh2MtSZv-ZXyI6vmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوین وارش با رأی ۵۴ به ۴۵ سنا ایالات متحده به عنوان رئیس فدرال رزرو تأیید شد.
🔴
جان فترمن تنها دموکراتی بود که از این تأیید حمایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/alonews/119817" target="_blank">📅 23:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119816">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر امور خارجه سوریه: دمشق خواهان دستیابی به توافقی امنیتی با اسرائیل است که بر پایه احترام متقابل به حاکمیت دو طرف و حفظ ثبات منطقه شکل بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/alonews/119816" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119815">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرنگار سی‌بی‌اس مدعی شد: پیشرفت‌هایی در مذاکرات با ایران دیده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/alonews/119815" target="_blank">📅 23:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119814">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: امارات و اسرائیل به دنبال علنی‌تر کردن روابط خود هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/119814" target="_blank">📅 23:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119813">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
منابع عراقی از شنیده‌شدن صدای چندین انفجار در اربیل عراق خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/119813" target="_blank">📅 23:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119812">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه العربی: حزب لیکود درخواست انحلال کنست (پارلمان) اسرائیل و برگزاری انتخابات زودهنگام را ارائه داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/119812" target="_blank">📅 23:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119811">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کیر استارمر ، نخست‌وزیر انگلیس در نخستین جلسه مجلس عوام پس از بازگشایی پارلمان، بار دیگر ورود شتاب‌زده به جنگ علیه ایران را خلاف منافع کشورش دانست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/119811" target="_blank">📅 22:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119810">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm-TflWD9Tf4fJ4xe4nyyTw__rzfmQyU8ETjRCQFPYPlSm0UfcsvrHVlzGUzsAIKhop99q3ZbljuKNboDHvW3Qh0SZ3_hdZI1HjvpR-1OK24pzgszOGzhdHvSf4UQv9YA15szJL6q3iSsFDe1PtaQdng7yP6XubVM-NlihuYSWfp9xpRTtXsT86uOMgYi5eq0GcRjglLYvuguXxiAPlyvR2w-Su67cm1t_OYelRK4IMsx3gjrrUCSJ51ac1EPoB9tzwTTGRpVZYyRcYpejr1j2WPaJdPRhrlit55ray_ZUNUbHfNSKCiR5bMP5yVEgfHDmtA9j2h36U0vLlK9UQBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین رئیس‌جمهور ترامپ را با حضور معاون رئیس‌جمهور رده‌بالا اما عمدتاً تشریفاتی، هان ژنگ، در پکن به گرمی پذیرایی کرد؛ انتخابی که طبق گزارش نیویورک تایمز، نشان‌دهنده مبادله نمادگرایی به جای ماهیت توسط پکن است.
🔴
ترامپ سه‌شنبه شب با استقبال یک ارکستر نظامی، گارد افتخاری و صدها جوان در حال پرچم‌زنی وارد شد — نمایشی که برای تحت تأثیر قرار دادن رئیس‌جمهوری که به جایگاه حساس است طراحی شده، در حالی که چین زمان می‌خرد تا از بازگشت به تشدید اقتصادی اجتناب کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/119810" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119809">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کاخ سفید در نظر دارد که رئیس‌جمهور ترامپ به مناسبت ۲۵۰امین سالگرد آمریکا، ۲۵۰ عفو صادر کند، احتمالاً در ۱۴ ژوئن یا ۴ ژوئیه، طبق گزارش WSJ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/119809" target="_blank">📅 22:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119808">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
جنیفر جیکوبز خبرنگار سی‌بی‌اس:
جی‌دی ونس معاون رئیس‌جمهور امریکا به من گفت که امروز صبح با جرد کوشنر و استیو ویتکاف درباره ایران گفتگو کرده، همچنین با مقامات عرب.
🔴
او مدعی شد که پیشرفت‌ در حال حصول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/119808" target="_blank">📅 22:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119807">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر خارجه کوبا: حمله آمریکا منجر به حمام خون خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/119807" target="_blank">📅 22:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119806">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سوپراپلیکیشن ایتا اعلام کرد امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/119806" target="_blank">📅 22:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119805">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ادعای ونس، معاون رئیس‌جمهور آمریکا: ما درگیر یک فرایند دیپلماتیک فعال برای اطمینان از نداشتن سلاح هسته‌ای توسط ایران هستیم
🔴
رئیس‌جمهور گزینه‌های متعددی دیپلماتیک و نظامی پیش رو دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119805" target="_blank">📅 22:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119804">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خبرنگار: آیا شما با موضع ترامپ موافقید که وضعیت مالی آمریکایی‌ها نباید در فرآیند تصمیم‌گیری درباره [ایران] مد نظر قرار گیرد؟
🔴
جی‌دی ونس: خب، فکر نمی‌کنم رئیس‌جمهور چنین چیزی گفته باشد. به نظرم این تحریف سخنان رئیس‌جمهور است.
🔴
اما ببینید، من با رئیس‌جمهور موافقم که ایران نباید سلاح هسته‌ای داشته باشد.
🔴
هدف اساسی این است که رئیس‌جمهور می‌خواهد جهان را ایمن کند، اما به طور خاص، مردم آمریکا را از داشتن سلاح هسته‌ای توسط ایران ایمن نگه دارد.
🔴
ما به وضعیت اقتصادی مردم آمریکا اهمیت می‌دهیم. ما همچنین چالش‌های متعدد دیگری هم داریم. طبیعتاً رئیس‌جمهور باید به طور همزمان با همه این چالش‌ها مواجه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/119804" target="_blank">📅 22:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119803">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ادعای نیویورک تایمز: شرکت‌‌های چینی به دنبال فروش سلاح به ایران هستند و قصد دارند آنها را از طریق کشورهای دیگر ارسال کنند تا منبع خود را پنهان کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119803" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119802">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از یک منبع نظامی گزارش داد: حزب‌الله از ابتدای جنگ ۴۵۰ پهپاد پرتاب کرده است که شامل ۱۲۰ پهپادی است که با استفاده از فیبر نوری عمل می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119802" target="_blank">📅 22:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119801">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
مقام ارشد ضدتروریسم کاخ سفید: ترامپ نامه‌ای خطاب به معاون خود، «جی‌دی ونس» نوشته که در کشوی میزش در کاخ سفید نگه داشته می‌شود تا در صورت مرگ یا ترور احتمالی وی، مورد استفاده قرار گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/119801" target="_blank">📅 21:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119800">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrBLBezZf3os7AcE6Kntp2XJAzp4VOQ3uP7ng6rrz7Km6-vzROP4cbdEy0iIzsT7aD3kdde-pxlKo2y3j_AxCZDSyu5pjamgUlBeg-x-WZKSA6NXUQ_Yo9sEWhY0YylOVyshXyiR4XqwIxxHhslkUzK5EnAs7xkq_Mj5JRAErrhVsidJH8zBsFonxaXmZTQisjpxXF2tWPKHHw1h_s9PgYWAjvZEAhCuXd-ZBurp9nfN6kOKvCbH0n4XA0_Pe11cT7zTouKNRbEE5c4ddNj2dbte5PypiHGoLGkEIYPwMMzFFARZKOL5xge270fbm0dmqox6bQRWoUnvVcMupdGdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">املت قسطی هم اومد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/119800" target="_blank">📅 21:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119799">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4KInpR4B30rRJizVD2G2nJomGtfZgeBVcGEa-DkjgOBYVP0UGaoLO3Khu7F6Q5TKXFT0Xf-7SbQAjq4YSxKU2yY_3a4l7BiWgQb5NBR0i5znGRhIGqTOqJTZF80Gev3ukjAgj0a6dFyGUJttw_SW075Hr-Md4p1rtLXnOcLiiDmw95dYg2WaI8XFvaO8StiETvX4lIj4sUz3vHqdci1Oc8gG3z5m7lGo3WS7v3zSpxTNbQF7qNuYAAU67n2E-dP1gMz0lazy-SMxrgCzWy8dp5Zlj3lat5YFoBCo07YukEoamlbRcN6ZBKWlSjBC7yW_uwArQy9UnCieV0vadjBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پیراهن تیم ملی برای جام جهانی 2026 رونمایی شد که دقیقا شبیه پیراهن 2014!
@AloSport</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/119799" target="_blank">📅 21:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119798">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر گردشگری: گردشگری پساجنگ جهش پیدا خواهد کرد چون مردم دنیا علاقه‌مندند ایران جدید پس از جنگ و واقعیت‌های آن را از نزدیک ببینند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119798" target="_blank">📅 21:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119797">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
المانیتور: عربستان در زمان جنگ مخفیانه به ایران حمله کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119797" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119796">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
به گزارش ان‌بی‌سی و به نقل از داده‌های ناوبری، چندین کشتی باری و نفتکش مرتبط با چین در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119796" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119795">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d734fbc3e.mp4?token=MoqpWdz_YGNtYWiSWirqIbiiwOX6trBdJpsi3fVs0gy0i5RobI_t0MnQWLmVvgZl42y0TR9APMnggIKv3ds-MY0t17WDkChK7o_FBVDDg_2uXZSOBCpFtfi0G1tfgpzYlNfe3BCocGyHXQBCvlYOPSpUoPQmKinQrVe6arHHH4YpxZ0qdwNxQExG5w4mdKXxKHrITP6sInFmPuOyteIB9s-bKiiBc9d_gPGzdwtO7rvlkbDpg1oinQZYi3IgHD7xYJFHo6y2PwuzXZh_qXOXbjzNdP1Ko-tH7E3as6Pp06infgA7_E7io5oEVjkODO5UsGQNdd5_znEvZL6LZRGRrFLVNSTQdtlhOGv_qUBZceCkWKzCHPgx9LjBqQmBVnw9RaBzni-NkiomEt18IY8wGoOzJWnfQpnenE0X84yXTVWphCr2RFmbOll7pvD08YXtPM4CYC1yXMsM5a47UuMhy6ORPALEs_xBzrWnfT8CVffuM7718nn5V0nB_KoWio_x_zBsYiSHRi9d0NWYOH7NzJufKYapqpipIKsF1s-p2YoH2LyZoIRiBdRZ7dWSCsqCB9uxEasE9a6ja6LBaf-2c_AO8oQRtcr1lnTZ9vklQ8l5ct17BehjxcHWctwGiVwAMgBGLsanvoSrZBaUeC4W4q7_wT0xXatPtVTKbD_J1DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d734fbc3e.mp4?token=MoqpWdz_YGNtYWiSWirqIbiiwOX6trBdJpsi3fVs0gy0i5RobI_t0MnQWLmVvgZl42y0TR9APMnggIKv3ds-MY0t17WDkChK7o_FBVDDg_2uXZSOBCpFtfi0G1tfgpzYlNfe3BCocGyHXQBCvlYOPSpUoPQmKinQrVe6arHHH4YpxZ0qdwNxQExG5w4mdKXxKHrITP6sInFmPuOyteIB9s-bKiiBc9d_gPGzdwtO7rvlkbDpg1oinQZYi3IgHD7xYJFHo6y2PwuzXZh_qXOXbjzNdP1Ko-tH7E3as6Pp06infgA7_E7io5oEVjkODO5UsGQNdd5_znEvZL6LZRGRrFLVNSTQdtlhOGv_qUBZceCkWKzCHPgx9LjBqQmBVnw9RaBzni-NkiomEt18IY8wGoOzJWnfQpnenE0X84yXTVWphCr2RFmbOll7pvD08YXtPM4CYC1yXMsM5a47UuMhy6ORPALEs_xBzrWnfT8CVffuM7718nn5V0nB_KoWio_x_zBsYiSHRi9d0NWYOH7NzJufKYapqpipIKsF1s-p2YoH2LyZoIRiBdRZ7dWSCsqCB9uxEasE9a6ja6LBaf-2c_AO8oQRtcr1lnTZ9vklQ8l5ct17BehjxcHWctwGiVwAMgBGLsanvoSrZBaUeC4W4q7_wT0xXatPtVTKbD_J1DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دیسکوهای ایرانی دبی چه میگذرد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119795" target="_blank">📅 21:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119794">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/119794" target="_blank">📅 21:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119793">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119793" target="_blank">📅 21:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119792">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/alonews/119792" target="_blank">📅 21:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119791">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر خارجه عربستان: امنیت تنگه هرمز اساس ثبات اقتصاد جهانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119791" target="_blank">📅 21:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119790">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ادعای رویترز : منابع متعددی که از جزئیات ماجرا آگاه هستند، اعلام کردند که در جریان جنگ با ایران، جنگنده‌های عربستان سعودی اهدافی مرتبط با شبه‌نظامیان تحت حمایت تهران را در عراق بمباران کردند. بعلاوه، حملات تلافی‌جویانه‌ای نیز از کویت به داخل خاک عراق انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119790" target="_blank">📅 21:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119787">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXa94xXAogV5bc0sBsQhVnStzr0VY408QqjpO7KKX1WBFXBH6f0-LwSOmQtAcsQ18noT-vnWS4oVAnUO1tZI3Hkm-ywi5gpPVSDOVeydNvUlZbDK4yhogOwz5wnKyIkM_STBef7dqQ9rDIF3H9H6l51j75Q5B7TrxEDoU4UOwzozVii5-iwvbCZuft10LEiLssjXLWrxBZEgqlBBTVB46utvDQaUF6cS4LCEIG5U0nFZFKnVL11MDeTb47Jd8LXygcn0JrqPJlFNGM1m0wxBqN3dX6yUN6xZf7VRSHEOsSERwLqHX8JfD6Iz5v6YegxYWGk72wYYpobnc3E7qBsy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP-gegI3qVXBOR8vvJdG2dxmY3Nb8wu4cHYuXEcKZm8JWXCV0Fo0LhiG0CpPRijQ2D-RpayL-80d8OPLoheFZp7Wu9bsxyFzdnGrcXnWsld2wCbD3B3ZQVL4HdlhkPm9ionaK4bO0LZ4pYlP3lmi2qT-Tu1CebX0xcqNSoyD-bQR5U6c_taxHO7p3K-SZy1RZSQa6JIPMOAmFHaKYPEY-PJcsyHWxIGmY_iTZXiDMshFgPAH60HtElribefxFvzWPg5dsR5vD3Nt82STdc8MN_u0T7EpyyZlH-JABfldDS5jw2JtacDl5E3IqYI62T6f6sOk8odjPvSik2C7RRy_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxFpsuQmMpPrR7imQMQqAJTRkh0sYcvroju-JSEXRS6_di84_j1UWHqJt2R6_s3-AhbuoJLuZuB1xjKMhSVcBT6VLq-1YXRHhTKMGAFNiS1oIenSlDKbo27hYoJq4dBvPR4PZ-d1FlqSWD6ibJe7OJlC5AJBayu6PO2CNq1Sni2r6MtIuSwwty_SKHdXEe44mWG3Zp6_dpqRnd27KOZjAavsGsNtTtWRytXyUbVW3oNbAoFpYZtN_RUNH2gCe0lkpaeg64LEi7Lcwnvdj0DTnOBOVK8NpB-AHlwYjsEww_9gbdERthYGzJsDsJv7ZvmpdoxV7ULDfUwwJ8vrp-y2Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سرباز اوکراینی با دوش پرتاب FN-16 چینی مشاهده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/119787" target="_blank">📅 20:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119786">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
هفتمین رأی‌گیری در سنا برای پایان جنگ علیه ایران شکست خورد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119786" target="_blank">📅 20:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119785">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دفتر نخست‌وزیری اسرائیل: در میانهٔ جنگ اخیر، بنیامین نتانیاهو سفری مخفیانه به امارات متحدهٔ عربی داشته و با شیخ محمد بن زاید، رئیس‌ امارات، دیدار کرده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119785" target="_blank">📅 20:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119784">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
هفتمین رأی‌گیری در سنا برای پایان جنگ علیه ایران شکست خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119784" target="_blank">📅 20:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119783">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
عراقچی : کویت به‌صورت غیرقانونی به یه قایق ایرانی حمله کرده و ۴ تا از شهرامون رو تو خلیج فارس بازداشت کرده
🔴
ما آزادی فوری‌شون رو می‌خوایم و حق پاسخ‌گویی هم برای خودمون محفوظ می‌دونیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119783" target="_blank">📅 20:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119782">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اکونومیست: طولانی شدن بحران ایران می‌تواند آسیب جبران‌ناپذیری به کشورهای حاشیه خلیج‌ [فارس] وارد کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119782" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119781">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ارتش آمریکا به دلیل عوامل متعددی از جمله جنگ با ایران با کسری بودجه غیرمنتظره‌ای مواجه است، به طوری که ذخایر مهمات از سال ۲۰۲۲ به دلیل حمایت از اوکراین کاهش یافته و اکنون با درگیری ایران بیشتر تحت فشار قرار گرفته است، طبق گفته یک مقام آمریکایی که با الجزیره صحبت کرده است.
🔴
این مقام تأکید کرد که این کسری بر آمادگی رزمی تأثیر نخواهد گذاشت اما هشدار داد که در صورت عدم تصویب بودجه دفاعی ۱.۵ تریلیون دلاری، ممکن است تصمیمات سختی لازم باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119781" target="_blank">📅 20:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119780">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بلومبرگ: عربستان به اوپک اعلام کرد که تولید نفت خام این کشور در ماه آوریل ۶۵۱ هزار بشکه در روز  کاهش یافته و به پایین‌ترین سطح از سال ۱۹۹۰ در جریان جنگ خلیج فارس رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119780" target="_blank">📅 19:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119779">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
با اعلام قوه قضاییه جمهوری اسلامی، احسان افرشته به اتهام «همکاری با اسرائیل»، بامداد چهارشنبه اعدام شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119779" target="_blank">📅 19:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119778">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا، می‌گوید ایران "به طرز ترسناکی نزدیک" به اورانیوم با درجه تسلیحاتی است — که در حال حاضر تا ۶۰٪ غنی‌سازی شده است، در حالی که برای ساخت سلاح هسته‌ای به ۹۰٪ نیاز است.
🔴
او می‌گوید ایران ممکن است چند هفته تا رسیدن به این آستانه فاصله داشته باشد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/119778" target="_blank">📅 19:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119777">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53f547919.mp4?token=TylopYiPm2iX7vjz3BkcU-GZJ9g4qrbI3iUchlCwibqvFa9bXLufKTRG6hSLfXUgZAhFD1PsjvbOHlZrZVIPVDvFPOmkwjYfLuKSpAdRBu1-U_unxCghY4louN0lJ3SBjNZJ-wNQZB4QYR-YkGdFO0_gkdR1A07Gp-jZ1qGG5x9rh8iPsmQPNlLzXNzNyuU15_LaVivwvSNKlJ9-yeEG860gz3iXDFLrvtHUdhlslFZmjkQ4K69f3jD1Vs1CfpG3v5ZD7xpWt6nFGh92J8Zn7hpWIWrE8L0A2yrbQRhPXoV8pTtpWew87j1J1TXi_J5-HReqRqPV7BdrfTpP2zYosg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53f547919.mp4?token=TylopYiPm2iX7vjz3BkcU-GZJ9g4qrbI3iUchlCwibqvFa9bXLufKTRG6hSLfXUgZAhFD1PsjvbOHlZrZVIPVDvFPOmkwjYfLuKSpAdRBu1-U_unxCghY4louN0lJ3SBjNZJ-wNQZB4QYR-YkGdFO0_gkdR1A07Gp-jZ1qGG5x9rh8iPsmQPNlLzXNzNyuU15_LaVivwvSNKlJ9-yeEG860gz3iXDFLrvtHUdhlslFZmjkQ4K69f3jD1Vs1CfpG3v5ZD7xpWt6nFGh92J8Zn7hpWIWrE8L0A2yrbQRhPXoV8pTtpWew87j1J1TXi_J5-HReqRqPV7BdrfTpP2zYosg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید نتانیاهو نخست وزیر اسرائیل داخل ایکس : ما پیروز خواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/119777" target="_blank">📅 19:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119776">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر نیرو: تابستان خاموشی نخواهیم داشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/119776" target="_blank">📅 19:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119775">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دولت فرانسه از بیم شیوع ویروس هانتا ۱۷۰۰ نفر را در یکی کشتی در ساحل شهر بوردو قرنطینه کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119775" target="_blank">📅 19:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119774">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBfosa3S3fguSqOVxK6DiuljBWhKjm5ifvncVTwW29HIKKlwG1mfq_Gp7OWajA81_sZGf9QB-GK4eGyZEmJs_E8ODfzZLShPIhzooXz9J0gWaOQoGYkWR8PIny4GiCuMFy4PLFF5B_McrBsq4TmnMmA7kDtvJlZgySm3nXWUpuN3euetouNKjLVVAHbhgdYyjMVfaGzdnPZTJb90wJjSwq14deMwslrrnvXH29peKDpDEta55ekNAvlth6-nq4yU8dxqBGz20h87Oddc1Z-6XhvNX8IuuxpWFKkGlnqTrI0AHeZQUQ6WuKpdtBCLw95-1LYCBjJZxyKG0sfpaTypiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی وارد هند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119774" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119773">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
تحلیل سی‌تی بانک: انتظار نمی‌رود دیدار ترامپ با شی جین پینگ بن‌بست موجود میان آمریکا و ایران را بشکند
🔴
بنابر تحلیل سی‌تی بانک، انتظار نمی‌رود دیدار دونالد ترامپ، رئیس‌جمهور آمریکا، با شی جین پینگ، رهبر چین، بن‌بست موجود میان آمریکا و ایران را بشکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119773" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119772">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای امور خارجه ایران و جمهوری آذربایجان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119772" target="_blank">📅 19:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119771">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e876ccef94.mp4?token=u8mdq2_sYSYrEJ_g0OtLReyJ87M--FWWaXkFjf07695rrCB2zekDg8ClLWPZOCpE5lIvMRVFy1C60AxlfQwjL2RUP3E559jalvGoWezywkR2Kvfn82fyHFVBzCPmZXoLnFufY9FGtFI9NKkTOezQOBd3v3y-P0DPLNLlHUK1VprReRXnYReBpnQv3sEF4JrnJBDZClasvtoGE8U5UFeXA7Ew4UQQC-WbQ_ATRckUc97s0k1i6u0ne1BToBLB8brbkw2kCa-oALFQMKCNvyWdtkzJob7vVjz_WvsuNNP0b_vhgzaXCAS9bdzXOB_4gLbOb_aTTVIKd5FR6NukY29bcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e876ccef94.mp4?token=u8mdq2_sYSYrEJ_g0OtLReyJ87M--FWWaXkFjf07695rrCB2zekDg8ClLWPZOCpE5lIvMRVFy1C60AxlfQwjL2RUP3E559jalvGoWezywkR2Kvfn82fyHFVBzCPmZXoLnFufY9FGtFI9NKkTOezQOBd3v3y-P0DPLNLlHUK1VprReRXnYReBpnQv3sEF4JrnJBDZClasvtoGE8U5UFeXA7Ew4UQQC-WbQ_ATRckUc97s0k1i6u0ne1BToBLB8brbkw2kCa-oALFQMKCNvyWdtkzJob7vVjz_WvsuNNP0b_vhgzaXCAS9bdzXOB_4gLbOb_aTTVIKd5FR6NukY29bcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل ماکرون: کل اقتصاد جهانی به وضوح تحت تأثیر بسته شدن تنگه هرمز قرار گرفته است، اما قاره آفریقا به‌ویژه تحت تأثیر است.
🔴
چندین کشور قیمت سوخت خود را بیش از ۳۰٪ افزایش داده‌اند، همراه با افزایش‌های عظیم در کودهای شیمیایی و خطرات قطع در ماه‌های آینده که امنیت غذایی را به خطر می‌اندازد.
🔴
در مواجهه با این وضعیت، باید از اقتصاد آفریقا بیش از پیش حمایت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119771" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119770">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZyHpG1l8_ImIS5K7LD5RpyKmiCmIC5q9G20HeJchWKqp5jUjv0cKPwygIUiNlpr-8al8GxA2OWgSx2IflxXERzR08JYRv8BhBYrytvK8hDrqFdLdWTqUNiWSxnq4NstjT-T4Q7c1PNQDl6YnJXhALVga8EMN3bDmFgnLQI9pC-qVaEbyhTTeUbjODRHnx9g6pJOJIIaGAqsfELTL5lnIyIM8fJDUzFO8sFD2FW06QdaM8NjKHmFabvdAfugvo8S4PDIMjDMKm5b73EKt0Pk1mfsH1Uz-EgIHc7AtuH0SGOZ5XO1A_NTbTtZc1N5kEQOnVOPGQiY3Ed7gTdyHGv-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119770" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119769">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5dae8e894.mp4?token=Uqob9Cmieqas9FMCB1nDbPNH0JoUuD7_0NIGgIAdosjtcnp0AG4p4Nw-YO-4bcV9GtQ-GRe2ID0CQmpu-Lskw8ZoQmnfPl4Mo-E07v_74UMYaJtloJKQuIVw8jyj8BKdOm82UaBCxk0Joh50j64Bh6qeRasDx98O6ktwIvQ78BwLD_zqfbU1syFwgnSca_zMkOq8YFuzYAtBtoESGZMWVauvJjhRfpBD4H-d9niu6tgIO72q55dzy8KPPi1F7bz8RJ3nm0djVhOme1v9IYVwqRK1njZjHmOq-2kmBFH8i-J2fImodQQLogRO9uXkh05YQqcN_k_Ya2oW88YDew1lqQVv8FocQPp0etwxg6NoBcWfIm97L-oKCJg_eaaSEmzaKfUfwKRP59uAn6VMftkUtuXBSoP054VQRrFtm1xwxiYstHmbz8e2_MwMI2csT3uD4IGd6hMw295f1X60w4PwkL5QttecSux7YKyvby7C2291DplMOK4iBU2nhzZEkUNlgkMOEFNrzF1tYYIQwCQy4O0iwqRy9jn59pE-tIFMvVwHuK5lJqJQAvOml_9vUdh4vTHbXy7tLAK0ZKx_5cR48YfH47lxF8L1OeFYIwK9z6vlV15HYhkymOaNnfwcM3SnVY2yPTnGT58lPr_to3ywl8rry_QpTe_dLhTR5oJ7Hf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5dae8e894.mp4?token=Uqob9Cmieqas9FMCB1nDbPNH0JoUuD7_0NIGgIAdosjtcnp0AG4p4Nw-YO-4bcV9GtQ-GRe2ID0CQmpu-Lskw8ZoQmnfPl4Mo-E07v_74UMYaJtloJKQuIVw8jyj8BKdOm82UaBCxk0Joh50j64Bh6qeRasDx98O6ktwIvQ78BwLD_zqfbU1syFwgnSca_zMkOq8YFuzYAtBtoESGZMWVauvJjhRfpBD4H-d9niu6tgIO72q55dzy8KPPi1F7bz8RJ3nm0djVhOme1v9IYVwqRK1njZjHmOq-2kmBFH8i-J2fImodQQLogRO9uXkh05YQqcN_k_Ya2oW88YDew1lqQVv8FocQPp0etwxg6NoBcWfIm97L-oKCJg_eaaSEmzaKfUfwKRP59uAn6VMftkUtuXBSoP054VQRrFtm1xwxiYstHmbz8e2_MwMI2csT3uD4IGd6hMw295f1X60w4PwkL5QttecSux7YKyvby7C2291DplMOK4iBU2nhzZEkUNlgkMOEFNrzF1tYYIQwCQy4O0iwqRy9jn59pE-tIFMvVwHuK5lJqJQAvOml_9vUdh4vTHbXy7tLAK0ZKx_5cR48YfH47lxF8L1OeFYIwK9z6vlV15HYhkymOaNnfwcM3SnVY2yPTnGT58lPr_to3ywl8rry_QpTe_dLhTR5oJ7Hf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: چهار هفته پیش، فرماندهی مرکزی شروع به اجرای محاصره علیه کشتی‌هایی که وارد و خارج از بنادر ایران می‌شوند کرد.
🔴
تا امروز، نیروهای آمریکایی ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، اجازه عبور ۱۵ کشتی حامل کمک‌های بشردوستانه را داده‌اند و ۴ کشتی را برای اطمینان از رعایت قوانین غیرفعال کرده‌اند.
🔴
اوایل این هفته، نیروهای فرماندهی مرکزی اطمینان حاصل کردند که ۲ کشتی تجاری پس از ارتباط رادیویی و شلیک هشدار با سلاح‌های سبک، برای رعایت محاصره بازگشتند، که به وضوح نشان می‌دهد اجرای قوانین توسط ایالات متحده همچنان به طور کامل ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/119769" target="_blank">📅 19:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119768">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس ستاد کل نیروهای دفاعی اسرائیل، ایال زامیر: نیروهای دفاعی اسرائیل با عزم راسخ در همه جبهه‌ها فعالیت می‌کنند. عملیات هنوز به پایان نرسیده است.
🔴
نیروهای دفاعی اسرائیل آماده‌اند در صورت نیاز مبارزه را از سر بگیرند و در حالت آمادگی دائمی هم در دفاع و هم در حمله باقی می‌مانند — از یهودیه و سامره (کرانه باختری) تا تهران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119768" target="_blank">📅 18:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119767">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رسانه ترکیه‌ای: حضور کشورهای خلیج‌فارس در نشست ناتو علیه ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/119767" target="_blank">📅 18:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119766">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پاتریک وینتور دبیر دیپلماتیک گاردین:
معاون وزیر امور خارجه فعال و مبتکر نروژ به طرز غافلگیر کننده‌ای وارد تهران شده است. او اخیراً به عمان و پاکستان نیز سفر کرده، بنابراین به نظر می‌رسد نروژ در حال آزمودن نقش خود به عنوان یک میانجی اروپایی است.
🔴
همزمان، برخی جمهوری‌خواهان آمریکا نظر منفی نسبت به تلاش‌های میانجی‌گرانه پاکستان دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119766" target="_blank">📅 18:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119765">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نفت آمریکا به ۱۰۴ دلار افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119765" target="_blank">📅 18:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119763">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzliwLh79nRr6gsoH5_4SDkT1HYPVUK401OeE782rXJgnUsdBG2I_IkFrl_Kp-6EH4S11zTZQNUNp-cF7KmvNFFKnIiaoVwQKXiYpv_8ar3QLhqB6vuelWYtg2VInn5QNrzB73_4_jFeTDLYgL7NiCNCy4UFmogT4lJishIJ1JX1mfE-PJBoCKLLJSTDdQKlwGDvVs5iPMApv459fjjpt3p9KljGhccbsbffku7GuoL4QGkWfsMKeu1fuxqBJbRwtWvnbcj2tcc_NJ54US8-VU4PDmsZftdIar5oJseeNEYIoM4YtJYvy2KBRfy7tDxdAiMUt5bKnWVGowhyxDEgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d2cac2d.mp4?token=iWe37kQvV5_VBaeJsLmaUbbGK0_4TrDE-zYZfTAmZcsu4hCimtUel-39dojjNBF2e197U1bcVA-CavxgybwbNHTj-ZaVvnkwmb7YQZlMOGTZrpn4tvhkc77bRdWC5S-lHMEP_HaAjb9sBHPx8_0UWnpFJx8sXAeD2thNRUqkE4eQA6ZV09GuwSkkB7iA21TpvnlT9hNhv1xnkvXx1abkh2rj6LMIB1c6KJmb8pukP7SoXk7EdJZWTAQrvAmAZQm6OUSv0fKNRFuVeNG4I7DaqavJvvoNvDAp7_8y6v3UExjVbkyxVcQp53k8U3bgNEFZOHWzthcFHddafTHDAVbnOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d2cac2d.mp4?token=iWe37kQvV5_VBaeJsLmaUbbGK0_4TrDE-zYZfTAmZcsu4hCimtUel-39dojjNBF2e197U1bcVA-CavxgybwbNHTj-ZaVvnkwmb7YQZlMOGTZrpn4tvhkc77bRdWC5S-lHMEP_HaAjb9sBHPx8_0UWnpFJx8sXAeD2thNRUqkE4eQA6ZV09GuwSkkB7iA21TpvnlT9hNhv1xnkvXx1abkh2rj6LMIB1c6KJmb8pukP7SoXk7EdJZWTAQrvAmAZQm6OUSv0fKNRFuVeNG4I7DaqavJvvoNvDAp7_8y6v3UExjVbkyxVcQp53k8U3bgNEFZOHWzthcFHddafTHDAVbnOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل چند لحظه پیش منطقه نبطیه الفوقا در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119763" target="_blank">📅 18:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119762">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نیکلاس کریستوف، ستون‌نویس نیویورک‌تایمز: جنگ ایران یک شکست استراتژیک بوده است که از برخی جهات، ایران را تضعیف نکرده، بلکه آن را قدرتمندتر کرده است.
🔴
هنوز هیچ راه حل ساده‌ای برای از سرگیری جریان نفت، گاز و کود شیمیایی وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119762" target="_blank">📅 18:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119761">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ادعای پولیتیکو، به نقل از یک مقام ارشد دولت ترامپ: انتظار می رود ترامپ در جریان دیدار با همتای چینی خود، او را در مورد ایران تحت فشار قرار دهد
🔴
چین پیش از این ایران را برای رسیدن به توافق تحت فشار قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119761" target="_blank">📅 18:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119760">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq90i89QVxBL261NkHWriINe4uxSMKK4mmwVtB6b8J1LqjTmh-gJNZidCEJ-Ast34WkifP4TcLwsnx-JnKIsyXrM7DgNo0SXD9dcXLmeRrPDv_6xCJwjbS36LkmtctZ0anIafYYlOQrXdoqcZ7xQDAz-6ig44QnobMdcv8svZoqFeNKFiFKmySFnYlvWlGbrxPf_u6yY5DbehhDZ-B3eLg-rFEGT8Z_1zIpC6xR3yLZY87nt5xrINPjZwsPb5OtIrRoPrQcJ_2qVqaVv7tyIuONsOfuBzPa5yJCBqfDiiQ_bg9kphxWbROEPG1Mc_5TsGlFvDXJNgodaHVbeZhFHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا اینترنت پرو محدودیت حجم روزانه برای استفاده در سایتهای خارجی هم داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119760" target="_blank">📅 18:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119759">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اطرافیان همسر مکرون با تکذیب ارتباط گلشیفته فراهانی و رئیس جمهور فرانسه گفتند: بانوی اول، هرگز در تلفن همسرش تجسس نمی‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119759" target="_blank">📅 18:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119758">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696b22878e.mp4?token=InNs-gi-aMhynDl8CIeP2wbihrt5IQdamqZs8Q_xUASNS0o501mn90-E6cdjypD-MYHyKKHP1ntfGPu3Ysgq23zVyYWdARNlCqSo6bJlkS6RCIefjAgMlMYeb1SgFK2k7CAuRr3-gCE4VE4d5XZ5WiECB_xC7Gyb7GMbxL3o0TK9I2kZyM9GrKO79_utfp-S1O7XJptEh31lNmn7nFX_pCKpH18AmbQc5I7paN41zae0SjkNGnJYjzo4y1gNlgekCZ7aqNKu2-EoJ77B7wdBK-eKoU2_RmS5OxhVfUnz_57liNL7DGCYdNYicWASixfZvWZMnJ29BQ17lBuvxie_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696b22878e.mp4?token=InNs-gi-aMhynDl8CIeP2wbihrt5IQdamqZs8Q_xUASNS0o501mn90-E6cdjypD-MYHyKKHP1ntfGPu3Ysgq23zVyYWdARNlCqSo6bJlkS6RCIefjAgMlMYeb1SgFK2k7CAuRr3-gCE4VE4d5XZ5WiECB_xC7Gyb7GMbxL3o0TK9I2kZyM9GrKO79_utfp-S1O7XJptEh31lNmn7nFX_pCKpH18AmbQc5I7paN41zae0SjkNGnJYjzo4y1gNlgekCZ7aqNKu2-EoJ77B7wdBK-eKoU2_RmS5OxhVfUnz_57liNL7DGCYdNYicWASixfZvWZMnJ29BQ17lBuvxie_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور روسیه، پوتین :
🔴
سیستم‌های متحرک نظامی که موشک‌های بالستیک غیرهسته‌ای دارن...
🔴
توی جریان یه عملیات ویژه نظامی به شکل مؤثری استفاده شدن و موفق بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119758" target="_blank">📅 18:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119757">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5371c1430.mp4?token=Bt2JnrQgKf6EndsueXndHJE1iueNQG03XysConIJNKPg3ge4clQ0e5tUHfhJxBPLrj5XG9RPvyY9Jbd1c4ku_dQjbcUmmm_lCv98qUwZuX-vJMukaPSnl7TBcRkadQAJP2v2adiE_1QFT1R10brW0ATfH0EJQAo0hv0QfeeYF268x1Xk6gJ6FOdXOHcj5JCSbbi0dOPWG7KHPbrD9aeRd5nXosU0u8v_xKmM5JagTo7M6bm2NXNrEIYtcEMx0Vd_QssNLu7bGShYq4yvnNimkqYcy5ID2-iOPLtwLOq9fEvlm1oQhzMz7sOLLq2UCd7JdgKWd0_jD69CIn_8LSWnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5371c1430.mp4?token=Bt2JnrQgKf6EndsueXndHJE1iueNQG03XysConIJNKPg3ge4clQ0e5tUHfhJxBPLrj5XG9RPvyY9Jbd1c4ku_dQjbcUmmm_lCv98qUwZuX-vJMukaPSnl7TBcRkadQAJP2v2adiE_1QFT1R10brW0ATfH0EJQAo0hv0QfeeYF268x1Xk6gJ6FOdXOHcj5JCSbbi0dOPWG7KHPbrD9aeRd5nXosU0u8v_xKmM5JagTo7M6bm2NXNrEIYtcEMx0Vd_QssNLu7bGShYq4yvnNimkqYcy5ID2-iOPLtwLOq9fEvlm1oQhzMz7sOLLq2UCd7JdgKWd0_jD69CIn_8LSWnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله ویدیویی منتشر کرده که یه پهپاد FPV تو نزدیکی خربت‌المناره، سربازِ اسرائیلی رو هدف قرار داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119757" target="_blank">📅 18:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119756">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آمریکا خواستار پایان برنامه هسته‌ای ایران
🔴
وزیر انرژی آمریکا مدعی شد: پایان دادن به برنامه هسته‌ای ایران که دهه‌ها ادامه داشته، تلاشی پیچیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119756" target="_blank">📅 18:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119755">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f911d75b16.mp4?token=WlRJnCwSzHPWc8NqF2YKv5laZvvq5BXYRJNSHaYgNY7R7-RJMw1Ekq7xEAOnh-WJ-K94b6u3VNCDdhL-kVniEoQ6utb_vXddyonPzumxIDyXEDhFQWmFlPgnrTWtRuJSRUGJhdhPmNY45B_QebNxMbHj5BKkBEhAodYW2D1I06wfTfsPqQVsZMtLcUG93gJB1DftkfNqJDyKtv7-3QiAnCiEq-Oq6k4yEWTOft1Tsqd1wXJGdgF8tW9VwriBIknV9MjaTlxPy4sjuFSoA_QHzoH4iWmAkaS48p_Xc3h8CzERJgoKLkZgyuUN6kS-6vZlJ9yEb3LetzAOh0u6wOD5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f911d75b16.mp4?token=WlRJnCwSzHPWc8NqF2YKv5laZvvq5BXYRJNSHaYgNY7R7-RJMw1Ekq7xEAOnh-WJ-K94b6u3VNCDdhL-kVniEoQ6utb_vXddyonPzumxIDyXEDhFQWmFlPgnrTWtRuJSRUGJhdhPmNY45B_QebNxMbHj5BKkBEhAodYW2D1I06wfTfsPqQVsZMtLcUG93gJB1DftkfNqJDyKtv7-3QiAnCiEq-Oq6k4yEWTOft1Tsqd1wXJGdgF8tW9VwriBIknV9MjaTlxPy4sjuFSoA_QHzoH4iWmAkaS48p_Xc3h8CzERJgoKLkZgyuUN6kS-6vZlJ9yEb3LetzAOh0u6wOD5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز چینی محکم سر جاش وایساده، همزمان هواپیمای ریاست‌جمهوری، ترامپ Air Force One از چند قدمیش رد میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119755" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119754">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09bfe31db3.mp4?token=cffWY32kORs3ycZezvTzSD2T2tQ2SWbe4jPObMPae1okCKx0S0HeYvHLKZ7HznF3cIeP3KGKK6uC_nl34WxVGvtolJzqI3ud1Ognpaew3ZAENyVGWYJHDXkNN1h-76mGz4H7-7d91i4ODBstC-ZPGeCCjWEOcvHhKu7xf6QgV4C1vj9nItNqU5G9H7eW6wV7T5pnaZ2r2KsAKcSFm4NmkBy-wTPMTuCgStLk_en02nAhGbvSYEpE7klNXkulYjDxHrbIHNaWjvYne5hOOmd-gmLYl02_2TrN0WBvGAGjBAWjSN9u-hgMRDnshHXYKcMkGDAoT8ntwoxqCD9d4AVNvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09bfe31db3.mp4?token=cffWY32kORs3ycZezvTzSD2T2tQ2SWbe4jPObMPae1okCKx0S0HeYvHLKZ7HznF3cIeP3KGKK6uC_nl34WxVGvtolJzqI3ud1Ognpaew3ZAENyVGWYJHDXkNN1h-76mGz4H7-7d91i4ODBstC-ZPGeCCjWEOcvHhKu7xf6QgV4C1vj9nItNqU5G9H7eW6wV7T5pnaZ2r2KsAKcSFm4NmkBy-wTPMTuCgStLk_en02nAhGbvSYEpE7klNXkulYjDxHrbIHNaWjvYne5hOOmd-gmLYl02_2TrN0WBvGAGjBAWjSN9u-hgMRDnshHXYKcMkGDAoT8ntwoxqCD9d4AVNvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: امیدواریم ترامپ در چین موضوع پایان‌دادن به جنگ اوکراین را مطرح کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119754" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119753">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjfCZd2yjQ71uLQkd8KYK-Y6FCdU_L7FenqE1Y0GS-MJbfVYEdZhUyzUhfANWlExb7dgCNXwssVVslki-djjCl3vRW55hgTinDOQrPt94CjoihHCQCfCINJy2Q7cZ8WE-7WkIwScrYM0AdBYpg2p8rJjpjaxuBZkvTeHzOzEeSOphh3E39HrqJAtIFyY1had0xGa1N5Vo-1mTFk_utJGn4h8AYSSgJhlNuGVrfZjGL-XTni0o9wA95kmSGQPqI8vau3c8JLBewBJqzU8VY-FymvY675J7VxlUddWUG6Wg4JQF0KSgiJuel-HpAzKdLU6LjWZBtsXjP-Q8rX3mKw8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استارت‌آپ چینی تصویربرداری ماهواره‌ای، میزارویژن، به دلیل ردیابی و انتشار تصاویر متن‌باز بمب‌افکن‌های آمریکایی در جریان حملات آمریکا و اسرائیل به ایران، توسط وزارت خزانه‌داری ایالات متحده تحریم شد.
🔴
میزارویژن سپس اطلاعیه تحریم‌های وزارت خزانه‌داری را به عنوان یک آگهی استخدام منتشر کرد و اساساً از آن به عنوان یک امتیاز شغلی استفاده کرد.
🔴
در آن آگهی نوشته شده بود: «به ما خوش آمدید.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119753" target="_blank">📅 17:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119750">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDPVuDsPqbdcbIGD0KG-TfEA20zemN_CFJdLccfGnTDuM1wq1VAjZwssvJsYhx2C5izZBcYe4NMTWnZF8gcCKXB-0bXoyGUiES3Un8BwFVrOqhc0a1fpwife7DaGbDnPc_hIH2oKN4HozR3POzvY8QfUhgk-KpYDOJlhVWHJIFR4irkXPIejXQ4d_8fqnOc0nosLEYGnjfyx6ziJCbwdMsgo13do7EiU8JjBF9aZR8axOwJRfYNwFDw7K-FpkwWtqpVgUQ3ZuSXKYd59A5aB7fgfbMMYf9-fXbCQ3LAy-e4hB9C4Q-6cQ-BYOjAo6L6Gq0Vfzdtnf5P0C92P3EJHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZqT7VyBhwTjbmbb9nKTONuw1QjLE3L-K7uiAmjZQ2MDtzbN-aawqYY2f21OCs3jxbQOEKOzSToT9CbPyIP6-vfvzCIsoAIAGCMOC0_VzJyiTLTh6HfWpaaPlvRwFe1BELFlyPUgfbloBMm2ivyftqIpqxwn2ech2ObDrpnsKRWXEbiJupBV_xrcigmp5V-CWkToMqGErKTkEVbQHCpdSjEHtlMe7_n3q4Z011WnvR7_wg6rZK50oQ6krT70DHqsx3I_92AchMNEPpmV7IU9euJOz0d5f1BX33MpVAcrRyqk6B9zm1HeX9ghwOj8pv0PAc9GYp5S59WOOad8SMNOMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af69a990d.mp4?token=gjvHi3j9JR6WkWjYUi118utodwCRQnf_5gGYxED-lVh_lvM06MSOFTPy4xZVZSKfp2NI0bSVEiQKTiUT1CGWrkwtVwA88QU52MnhwpeLJvvd9Vv3ukY9y1HcEe3HpjigzBbzynC_qBUEgFSsS_F6OcwoG9hYZrC7HpiOR6FwvCZv2wqJYbTE-KYfI5F9OM2dkOvSAwTgnyOo3uml_rN0xBZsmXS0eI9b57kSxc4Ic0Lmd0XzqhjSyMgqIXlulJBGMxvQyUtKet5BJajyUrhLURMttL8U8C1qcWruv6b_ua833F7fWaFsjVXukHC2iT0iDSynYvHLI-MzPxzcbbWwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af69a990d.mp4?token=gjvHi3j9JR6WkWjYUi118utodwCRQnf_5gGYxED-lVh_lvM06MSOFTPy4xZVZSKfp2NI0bSVEiQKTiUT1CGWrkwtVwA88QU52MnhwpeLJvvd9Vv3ukY9y1HcEe3HpjigzBbzynC_qBUEgFSsS_F6OcwoG9hYZrC7HpiOR6FwvCZv2wqJYbTE-KYfI5F9OM2dkOvSAwTgnyOo3uml_rN0xBZsmXS0eI9b57kSxc4Ic0Lmd0XzqhjSyMgqIXlulJBGMxvQyUtKet5BJajyUrhLURMttL8U8C1qcWruv6b_ua833F7fWaFsjVXukHC2iT0iDSynYvHLI-MzPxzcbbWwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کتاب جدید یک خبرنگار مجله پاریس مچ ادعا می‌کند که رئیس‌جمهور فرانسه، مکرون، یک رابطه «عشق افلاطونی» چند ماهه با بازیگر فرانسوی-ایرانی گلشیفته فراهانی داشته است که در آن پیام‌هایی از جمله «از نظر من تو خیلی زیبا هستی» رد و بدل شده است.
🔴
حادثه باند فرودگاه ویتنام در مه ۲۰۲۵ که در آن به نظر می‌رسید بریژیت همسر مکرون به او سیلی زده است، در واقع یک دعوای زوجین بود پس از اینکه او پیام‌ مکرون به گلشیفته را وسط پرواز در تلفن او دید.
🔴
کمپ بریژیت این موضوع را رد می‌کند.
🔴
فراهانی در مورد این ادعای خاص اظهار نظری نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119750" target="_blank">📅 17:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119749">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suHyejSsrESdRrzv0T7ljBph1sU1BI6BQKk-lLD_TL_jrIIUapIYRpza7-luKelZkscvc0leqI_cNFE4_DjnmCrwjcr61Flo6ud4VAwZKHIQxG33Sd56b7UgInfUU0sUIgfKy5qZxo0cfvvWX2hgO38J_8XlT1wdfEHLPrE1XLDKIeoLlDjJ0CwuIYx_xLagLw60aqzAJslyvBxiT3FaDneg1XpTKWqhHKpK9dZqtcx6G-q-cFufGxKLmAR8oizHrwiv1n4xgOAD7PonzicdlGJTYDCj7YytAzPX8Ei64c_-6YqLXm2DGqBpVStjYSyMJTbo8MLcz8c1o2JEcefTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بروجردی،عضو کمیسیون امنیت ملی:
دستاورد تنگه هرمز را از دست نمی‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119749" target="_blank">📅 17:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119748">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3813de281a.mp4?token=RpXUKh-f2BLeMW_dzy5Ik0W_Z5MencDNU2YEMTlvt-QfoARXBS2IbvieujRGOSRHGLga3T25c7wvfTNl5RJNfC56XmkkaxaMdC8Pygn67e-qLdURwXSW0Sr7tWM0t3X3AvPaxoxTxkZIBERt1gUwZc82ZmgRXn8QEZHTBTorgNv-OQCYQRzFnFqSw-w3eiKePtXFVChYmtc4HbadYR9rUnhLR4MxWRi6hNXT6-J9rsPBfX5LiuIInP4FIKFjcYsMqUgpcbdWX0t5onGRcAMBsL3ICTQd9RT6OzTlM9Re0sr0DfRu6kxNiaiyGstKDCT0zMuaHjGXK9_LmSoEl9rxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3813de281a.mp4?token=RpXUKh-f2BLeMW_dzy5Ik0W_Z5MencDNU2YEMTlvt-QfoARXBS2IbvieujRGOSRHGLga3T25c7wvfTNl5RJNfC56XmkkaxaMdC8Pygn67e-qLdURwXSW0Sr7tWM0t3X3AvPaxoxTxkZIBERt1gUwZc82ZmgRXn8QEZHTBTorgNv-OQCYQRzFnFqSw-w3eiKePtXFVChYmtc4HbadYR9rUnhLR4MxWRi6hNXT6-J9rsPBfX5LiuIInP4FIKFjcYsMqUgpcbdWX0t5onGRcAMBsL3ICTQd9RT6OzTlM9Re0sr0DfRu6kxNiaiyGstKDCT0zMuaHjGXK9_LmSoEl9rxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من خطاب به بابام که میگه ۱۰شب خونه باش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119748" target="_blank">📅 17:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119747">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل:
جنگ با ایران پایان نیافته است،برای از سرگیری جنگ در هوشیاری کامل قرار داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/119747" target="_blank">📅 17:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119746">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو امروز با رهبران امنیتی در مورد چگونگی مقابله با تهدیدات ناشی از پهپاد‌های حزب‌الله گفتگو می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119746" target="_blank">📅 17:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119745">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SexdJy0pS3Ot71Gm6XKjWHSPnxEsMI0DBaq-eW-Ry42vesJxiH4FebQlPMUgbNxhwWn5BjriW3bhpmx5RfXYL7MPTyf5FGGtzzuWmi4QkmqOKNVAS6aDgAAPlGGsRlTKl5r-ACiqTKX1djkuQHwRzMmLYbywgkY01bk4hqSM91FT3nBgdK8i8MpguPPmr8d6JecJmDOgGVfRuNljVC2yidwgySC-P8AfaC_WR0xpOCsqhIrjwEp_hcU4RtHaXu0EbL-HE8zdQNA6yTWp7iCs7zLKiX_IPBy1Y5_P-guj92TnVah-jFRFDyh3OJ1gIGhPjk23Is_-5udE7MqGr0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس منتشر شده توسط سنتکام از یک جنگنده F-35A نیروی هوایی ایالات متحده در حالی که در آب های منطقه ای نزدیک تنگه هرمز گشت می زند.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119745" target="_blank">📅 17:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119744">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5116963d4b.mp4?token=VuADuCvQDEX2y9ENDVlNlCR-PgChxZfGMEuP5FqRf9ymay6atbmXcxtidmmyH1Lo45BF8dzrjkn3V_fxH0QBGWQ55XFW8MYyalbu-xiTMQNSPgVSWHv4mL-u8bswmIhz3h0IAJSPxyG22a3wurvs9WtuEs7QZw8sqXB51elQkuZn3moVfxtlZR5EdlsgRiJ9zaMBiyVEU19ucMI2D1mVGoKtq6eAEe8MRqSAocY_c22C_qojr1I13ZwwqZEq3q73tb8FX8lm1Z3XpfzKtWZ-wcZvwLH9PaDeCJwUWHQKPYSRvB35CV1wIQOhxC5vGJgqcLgnaf2uQwhV8WlzMOORAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5116963d4b.mp4?token=VuADuCvQDEX2y9ENDVlNlCR-PgChxZfGMEuP5FqRf9ymay6atbmXcxtidmmyH1Lo45BF8dzrjkn3V_fxH0QBGWQ55XFW8MYyalbu-xiTMQNSPgVSWHv4mL-u8bswmIhz3h0IAJSPxyG22a3wurvs9WtuEs7QZw8sqXB51elQkuZn3moVfxtlZR5EdlsgRiJ9zaMBiyVEU19ucMI2D1mVGoKtq6eAEe8MRqSAocY_c22C_qojr1I13ZwwqZEq3q73tb8FX8lm1Z3XpfzKtWZ-wcZvwLH9PaDeCJwUWHQKPYSRvB35CV1wIQOhxC5vGJgqcLgnaf2uQwhV8WlzMOORAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به جنوب لبنان همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119744" target="_blank">📅 16:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119743">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea1c5ae6b.mp4?token=dGWGtSFInapJD-XqqExPMVxT6o-FhL34OzDU1ORhf3LJGcvMqYXNEqw6B1Qw1L-wzp5dy-5v9Y8xlyW3X3bVLwE4gdzp5kvvJwnYwEmJuDgi0OHStURxpFVJA17uIqAKHWVvFquIBFeaVWaZiliUU_2QVHcFjiM1y5UEo_Z4JyebxCLSD5C1ba6KNpwphAbt-tUL8VVK_ot8a1twyZagoOQd6UR4jay7jbB6a_4z_XgPrEjl8o2fr1Ud32B4V6g6rjvC0XVyQFAsUTnJfoBBTd0ERqxpU8JdTgS8ET09q7KZMnGSOr-WYj6L8tHHEIJNqECYTeT1JjPhYWPaOfaW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea1c5ae6b.mp4?token=dGWGtSFInapJD-XqqExPMVxT6o-FhL34OzDU1ORhf3LJGcvMqYXNEqw6B1Qw1L-wzp5dy-5v9Y8xlyW3X3bVLwE4gdzp5kvvJwnYwEmJuDgi0OHStURxpFVJA17uIqAKHWVvFquIBFeaVWaZiliUU_2QVHcFjiM1y5UEo_Z4JyebxCLSD5C1ba6KNpwphAbt-tUL8VVK_ot8a1twyZagoOQd6UR4jay7jbB6a_4z_XgPrEjl8o2fr1Ud32B4V6g6rjvC0XVyQFAsUTnJfoBBTd0ERqxpU8JdTgS8ET09q7KZMnGSOr-WYj6L8tHHEIJNqECYTeT1JjPhYWPaOfaW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌ای دیگر از حملات دقایقی قبل به لبنان
✅
@AloNews
خبر جنگ‌‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119743" target="_blank">📅 16:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119741">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uut7ZdMSlCwmdQ1pu_2NVc2atR3LAZOAunf_MHmgJJDLn5Oo6dK13B-IlaA7qsi7dQ48u5unUrX-yYPTZ94pPRun1PsMnBiKW1naEAp_yBkvT1pcM-CTPP54HHIB-XrrEbRVz2R3KFsL64yCUFnET963sx-bEzUf4pvj7Og4PouW6RbH8bMIRtfNhL_7wR0zvDc-XIlGQ5FjMJQSxQhETpg2GpLk-AU7LHYDphBgxOckIY905VpkUN10SZ7X2QdaevldXV-apvWvcM9rnn1FzF5v_CjN2t6hkUomgoeBYIkiKaU_BT6-kevByo9hbx6_l5tN-a7om7jvczVeS1riwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDThbu1nDpIA1yG_spPnIjlMZBrdx9WxfsBLQtD7hFFXxlcptyEDiToXUHui3tKLq8WLyth7LVIYAIdVNRfRbDYyIAhCSvqLGbxT9lJxvIWlrN8sLSoleTJDgA8ohmWzUoFPwV77_EhseyFgquAIUndTCcKGAT-6nVaixFv8KWAqYH0h1BRpU58mLbmDgn7XDs41nlOyWvgxrGH_RCxyccsdTjMmFJmxjhNjDL83af100Ou517YdEHcUDt-bauel5aFJ6LDDor8JAE5CyBrC_K0BmEsalxj7uF1-OcFYEtVxpIrQil2jyr6eiGg31nfQgTO8bhTg-MkmlccTpipwgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات دقایقی قبل اسرائیل به لبنان.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119741" target="_blank">📅 16:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119737">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9109b4be.mp4?token=nGI5ZJ3YaqtEgalDKwy9Pka8Z59QstRhxUNCQpwFwaZlpfBFsnwi75b3qxTjY8dUUapNFXsI5Bt-bw714dk80mQcCvjLvhQaWnuRDppdvyl6ayfIwBetWsUypnLqaNZUEiTREvEI5MpmwqDH2Nz7hXeuB9gi17B_QHXW7FibqIQOZX2r8C1pfvXdFqDTGzLxl-Az1yNzq9PI21RzW7E7K44K-XqzozkJ-RkVEPnJsjMduuhG1WeB-vfe8yMnJz3OZoh4DwuCGBfHw31ZrGnWTPRUELFcEE_DfcgMwvRHY8w88Vd5VbLiikfiKo5aStxGhoZ68TWxs9_Szd1Mj6IOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9109b4be.mp4?token=nGI5ZJ3YaqtEgalDKwy9Pka8Z59QstRhxUNCQpwFwaZlpfBFsnwi75b3qxTjY8dUUapNFXsI5Bt-bw714dk80mQcCvjLvhQaWnuRDppdvyl6ayfIwBetWsUypnLqaNZUEiTREvEI5MpmwqDH2Nz7hXeuB9gi17B_QHXW7FibqIQOZX2r8C1pfvXdFqDTGzLxl-Az1yNzq9PI21RzW7E7K44K-XqzozkJ-RkVEPnJsjMduuhG1WeB-vfe8yMnJz3OZoh4DwuCGBfHw31ZrGnWTPRUELFcEE_DfcgMwvRHY8w88Vd5VbLiikfiKo5aStxGhoZ68TWxs9_Szd1Mj6IOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119737" target="_blank">📅 16:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119736">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزارت بهداشت لبنان: از دوم مارس تاکنون، 2896 کشته و 8824 زخمی داشته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119736" target="_blank">📅 16:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119734">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YgEfcsnHr5QYp8imd7fi-YFrg9cKNVONLz-vKnkg6zLzxdxo9PG2H9elstiF7bh9y7QdNl5KMrsKmpQePn0LSVDrilCXVUPkN6J9gRi4XBUbnYj0qlG-2JK-aw1RrUxFK78Kb1R8a02NAmIG_J0G_qtZJSG68MM4hl9jjmySxBFpqH7GXK1FRBRyy_q7E49ESrAk5TmUszZyCtQ5M8FXzf5ZOVGL2-H5crnorCj3__bYHejsQ160jYNoUQsOAFh_2W4z4QhA4TaQnbnEcsD6SEgud0ylYs8Ab0iQyKu0RiINR6um2tSroUjlcTquq5X-6pncCLIQxuWoEhJt1xUCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ویدیویی از حمله پهپادهای FPV حزب‌الله به پرتابگرهای گنبد آهنین اسرائیل و خدمه مربوط به آن‌ها
🔴
حزب الله اخیرا با Fpv خسارات زیاده به اسرائیل زده زیرا این ریز پرنده‌ها به سختی رهگیری میشوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/119734" target="_blank">📅 16:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119733">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بلومبرگ: طبق داده‌های ردیابی کشتی، یک ابرنفت‌کش چینی حامل ۲ میلیون بشکه نفت خام عراق از تنگه هرمز عبور کرده است
🔴
نفت‌کش یوان هوآ هو اکنون در دریای عمان، لنگر انداخته است؛ این سومین عبور شناخته‌شده یک نفت‌کش چینی از این آبراه از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119733" target="_blank">📅 16:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119732">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faba46d214.mp4?token=lDHt-p5Bhjnskkc9OidGT5HWKIbFTzzjIxrYmnPIPb_ZSScc2GdO6HbV-_zn0IO8eOBvdcGbuKM1rY6J7LsEUdAcP57NG7UoIOLSXVHo445CZfd60B7BpYOe-grJPdWZl89eHQiDKKRqwuqMJbmfZa6luSlMP-KOXZVWlPePyk3YQwbORpSMvBStowyHmwhHdLdv1irmb-ca78umE6jIElOoEN328dh2R1KMx5EvilBya5j0XrqiSixto1OWVLkM9FvNb52yXaiIPe58aMUR8mS47-1gURgL0xADGvhZeFSXESPgYm3cORqrSNr1dI06-SSmEWGLjGmplZmRV0idPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faba46d214.mp4?token=lDHt-p5Bhjnskkc9OidGT5HWKIbFTzzjIxrYmnPIPb_ZSScc2GdO6HbV-_zn0IO8eOBvdcGbuKM1rY6J7LsEUdAcP57NG7UoIOLSXVHo445CZfd60B7BpYOe-grJPdWZl89eHQiDKKRqwuqMJbmfZa6luSlMP-KOXZVWlPePyk3YQwbORpSMvBStowyHmwhHdLdv1irmb-ca78umE6jIElOoEN328dh2R1KMx5EvilBya5j0XrqiSixto1OWVLkM9FvNb52yXaiIPe58aMUR8mS47-1gURgL0xADGvhZeFSXESPgYm3cORqrSNr1dI06-SSmEWGLjGmplZmRV0idPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدویی دیگر از مراسم استقبال از ترامپ در فرودگاه پکن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119732" target="_blank">📅 16:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119731">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f225f616.mp4?token=vgbQV6uDIHDvYo4aW5ZXXduY7g63GQC-KTDoLSQFGcPvxW94DXr5gw8ugAsaVOUt1XBMTXhJTe4Ii4qjcZYL3zJbbG81OkDV3Ka6zReCpGDIAOxWZfdqOUDUKc_hKpURlOAyMdUFeAppIb8OaKx7PL3YQbaWTXc2zNZeEUanxBUfMiJGWRMk8gFJm70aQ8u6s8tYKIrljoxQ_kSRbuBGrY0TzHZi97rBYshRbI5mCr5w76rOg88GDg5VBLNsyG-D_AWOlvfDzmwe66mRmtbdenlf42NjGvYjl-xUmOZyLwgv3qecS3p3wzlGOHEg-wpBptbjKfqiUs3lnak2waEOpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f225f616.mp4?token=vgbQV6uDIHDvYo4aW5ZXXduY7g63GQC-KTDoLSQFGcPvxW94DXr5gw8ugAsaVOUt1XBMTXhJTe4Ii4qjcZYL3zJbbG81OkDV3Ka6zReCpGDIAOxWZfdqOUDUKc_hKpURlOAyMdUFeAppIb8OaKx7PL3YQbaWTXc2zNZeEUanxBUfMiJGWRMk8gFJm70aQ8u6s8tYKIrljoxQ_kSRbuBGrY0TzHZi97rBYshRbI5mCr5w76rOg88GDg5VBLNsyG-D_AWOlvfDzmwe66mRmtbdenlf42NjGvYjl-xUmOZyLwgv3qecS3p3wzlGOHEg-wpBptbjKfqiUs3lnak2waEOpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال از ترامپ در پکن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119731" target="_blank">📅 16:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjqGiUDD2Rv83hjQehVbqfFYxW2Gg4Eunu_qM5mQ7M_I3OvOHdYdDwtD-_swD0azdHhJWOBKVTWlusg725oM0LwBNynjg3wSNFvVBvEBKfV-_FObpj4DpN03w0gbsIBZr6ly6_jy0nJ-WRphquGs6ix7VMZ6mTgW9hzS0snS26S626CEmLng__Qa6WtLLJQcMECvU2KN0qKkrh79U2YvDvnmS7m9dp45rVts9PaMomLIWbtsqo6VgtoEbs_cGsn60Sy3RMvfqeoFHn9wPheLo6YhU-w3gU5ZMHK2g160klvhtdg1sqHSZ38DIupFm7qAS70t2Eji3QcAN7ALhJGYgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه راس‌التنوره عربستان بعد از حملات ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/119730" target="_blank">📅 16:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119728">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9SZvGGwKVbDIMqBhEuHJJvja0tuwvFnxotzQhI-_WioqWvmTrkWk7MoZ-JfyPZk0PoPCNQXuQYWspMEPNiEfCOV9pHYty0J9gU-EfKWcovcV4lRGbe645w2W9DX9Z3V6bkqmdlBR9SKwv7Yjz4RZyBQUAs4xgURrGa5Fy3yRuBk1vv8_0yPtPZWEXdvSZbs6piJASFu8HsWuTucCqaULNxm6pIhIuMS-1_5AbcJKeZoX-e_s1wN--blyot4acvrT1VPuddiP8iFvReyyEz2NFlsDmZ7PtaocfG2p6K1cKJvkDv1q1g2y_mIFI3V6RzBnFIPYPndkLDSU4f0kVz5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفر عراقچی به هند
🔴
عراقچی  برای شرکت در نشست وزرای امور خارجه کشورهای عضو بریکس، عازم دهلی نو پایتخت هند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/119728" target="_blank">📅 16:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTjlbJQwRF4Ar0v765AtHMHWImM52TEWrRtkD3IE00lR_sFWAhEr6QsDiZO6xjUc0ftYs0TVty68Ib09a0ifqDsb5c3nX53YPTwAUSjwqq5aPU53YsvPnAt-ggv3BTdWC3Bnt9J5LJK6hO4jjYUERiQYT6XNe7HDSE4HR4H3nNuwLHKhWJfOVnpm76b70wOYyPJ8QPl_0z5qCHgnwuXSUf6WDsZnskkS_PEk4lVdRKRrSfr6k9DM-OoTcRjLZdqQH0BnAjou3JI25WnV0tb1a1NSLmkW4NMScjwTQqL7y4ZK0J9ADpn6VqjI18V1SdsapzEZqTTK-LMOEbqb7XuiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نسرین ستوده آزاد شد
🔴
نسرین ستوده، وکیل دادگستری و فعال حقوق بشر ساعاتی پیش با قرار کفالت از زندان تهران بزرگ آزاد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119727" target="_blank">📅 16:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSqkcVz3ZQTWi-PYQ6DpMsPWHb9q7CNIxdcxsm60npojxjAeBruRJJqirCXlp18Ss4-ain-wggPufg2VEG4D_GROft5WDK2qyFNTBCxiQ6C7G21jEHpWttoLQ4ih2kC44KwyqZC9YKQ2OaXPK8eBaKb37JXQ7Jv56tbgmxnyfD-IkQl3VlFg85JKF-c0YhGMQQV7fmkuzds9MbZypvobKngLqaHSSsz18e568KxebTiKsfJ7HMSRx87SE6pvASLRjH0w41J5-AjC7rE0iD_iLnGmo76xfoCKoP_KZRiOfMwWW8Jkgsy0N4hgo9BMJapTYkzd_IKMNNKXzgXUDOVs1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇸
تشکر فدراسیون فوتبال فلسطین از لامین یامال درپی برافراشتن پرچم این کشور در جشن قهرمانی بارسلونا
@AloSport</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119726" target="_blank">📅 16:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عراقچی  برای شرکت در نشست وزرای امور خارجه کشورهای عضو بریکس، عازم دهلی نو پایتخت هند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119725" target="_blank">📅 16:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ پس از ورودش هیچ مراسم عمومی دیگری ندارد، اما قرار است روزهای پنجشنبه و جمعه چندین بار با رئیس جمهور شی جین پینگ دیدار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119724" target="_blank">📅 16:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119723">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزارت بهداشت لبنان: از دوم مارس تاکنون، 2896 کشته و 8824 زخمی داشته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119723" target="_blank">📅 16:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119722">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7CiRp4QHU_ucBcvD-Le1ZCCJrWCDygsxzSsk2wmtHL3xPZRFD38zwWesMlCXoOaVrLv7aU-IgkdZqkSFhkgM-XuvEZlXfYd8FCOaDLJU7TTqcvE7viywSU3zt44G_vzfST_1C9VuNnrUfwELqcV9TlMQ_vKiHRO10P4TxjQb_UDZ05BukxhXkqTTV3CdILaLLOVK3S9VyP4fcxcA6naV-FvR9ITHQnHUWIH5rRQu5oF2m9vlt2vnBDzVZkxl-Lys2GXLRwLeaH0CtMTia0EkPIpNtohbT9Ahmh_daAcoGmgf_Ei_oh8zHUWBGhc6MlNCa8flBLYT79SdOPQx82ukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین عکس از محسن جبارزاده، ۴۱ ساله و متاهل در محله سلسبیل که در 18 دی عازم رزم با دژخیمان و ضحاکان روزگار ما بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119722" target="_blank">📅 16:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
علاءالدین بروجردی، عضو کمیسیون امنیت ملی مجلس: آمریکا باید این واقعیت‌ را بپذیرد که ما به هیچ‌ وجه دستاورد تنگه هرمز را از دست نخواهیم داد و به هیچ‌ وجه وارد بحث مذاکره درباره غنی‌سازی هسته‌ای نخواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119721" target="_blank">📅 16:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119720">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE5-nNIxhbo4SZ-o3Xfxi8qYzkpZARAUlQzRWgCf0eUI8w41bH8hHsX9LbO0twjdcbbleNATwj24r98mahdCzWMX9xP59A8nZG5Pwlfw5IPs73-voYjRCk9v2mWXQRUx6gs5HiltEgZgbvT2A1GHgJD4rJbMRKoXt1hUZGsllbYESPWqhdOxhANoRmtaqEVOj2-NvblYAzSUkBZ4IjIifpgvryetKbBWPLaGYMfNEH5LGmUvoTXviqkfRQDvn-XU_yLROKAXYqXelXe6fC5D7iN3TMMZuSjcfv5ZFqptSHTZSzOcINVQrSfRijnXEuOJdcJWhSpByi495vtzstCZtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امارات در حال نصب شبکه‌های بزرگ ضد پهپادی فلزی در اطراف محل‌های تولید و ذخایر نفتی اطراف فرودگاه دبی است تا در برابر حملات پهپاد انتحاری آسیب کمتری به آنها برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119720" target="_blank">📅 16:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
این وسط تعرفه پیامک‌ فارسی و انگلیسی هم گران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119719" target="_blank">📅 15:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نسرین ستوده، وکیل دادگستری ساعاتی پیش با قرار کفالت از زندان تهران بزرگ آزاد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119718" target="_blank">📅 15:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281fea04a.mp4?token=aHSoUvptJ_UVgHZS5dIynAqcSyFJBqI3kKkYDXhFdp_0QbZ68zKMfpM-f5-JRJ6AOmes5DwMTY7mp8iP7rp88TYL00j18Z3mQ6oPfYOIhcP3HvyrsVPR3RFMgwWIpkw9z92l1LBdLZUHkMGwi_6STxZ6Wcn9yRdFELdkNIIKtkYR9S28UbTHXYpOgeEY3Caf59-34xNheaEwDefKQRUYm3whlvRdKcojhMdRwVSsimzEo5H_-35cdX-2KQjCfAwMyrKE-b0r_hzMngTG1HkiIMaQSkwZYQOYpWetBavvn-ERBj1-lRZzwGai-A1CcsVvPLETx9I6SsgRfpB-3fdsn60GxIQsGeg94rPMZWqgYQ4DtgCfUcnlr4UYSz7GVFvvCmIIR4873YELO44y7ZczRPhRVKSaV9no9x-l-3VcBEhiaI4Zw_xKcuifwwz9z2DbO0xcVovh8xGJkEHtYkmhZ5LN9jv1OvAWrjklzq6C27HxSw_6EvMdkJBA6I-T-0lBGxubE07ThJvkTSSIwDz0fShm1Bdd2m2SDThqBY27dNa12iTgRNQla1xqWd_L6HDTIpp_do_xt1xX0oL6hA10B-kUAisFmTCmxDM7N-vC6NNKjmJzydf_9Y0vHQpxjm8fpiwFi-8P0lqZtgPSeBkKR2S3e68aLfU930M6wEeSCII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281fea04a.mp4?token=aHSoUvptJ_UVgHZS5dIynAqcSyFJBqI3kKkYDXhFdp_0QbZ68zKMfpM-f5-JRJ6AOmes5DwMTY7mp8iP7rp88TYL00j18Z3mQ6oPfYOIhcP3HvyrsVPR3RFMgwWIpkw9z92l1LBdLZUHkMGwi_6STxZ6Wcn9yRdFELdkNIIKtkYR9S28UbTHXYpOgeEY3Caf59-34xNheaEwDefKQRUYm3whlvRdKcojhMdRwVSsimzEo5H_-35cdX-2KQjCfAwMyrKE-b0r_hzMngTG1HkiIMaQSkwZYQOYpWetBavvn-ERBj1-lRZzwGai-A1CcsVvPLETx9I6SsgRfpB-3fdsn60GxIQsGeg94rPMZWqgYQ4DtgCfUcnlr4UYSz7GVFvvCmIIR4873YELO44y7ZczRPhRVKSaV9no9x-l-3VcBEhiaI4Zw_xKcuifwwz9z2DbO0xcVovh8xGJkEHtYkmhZ5LN9jv1OvAWrjklzq6C27HxSw_6EvMdkJBA6I-T-0lBGxubE07ThJvkTSSIwDz0fShm1Bdd2m2SDThqBY27dNa12iTgRNQla1xqWd_L6HDTIpp_do_xt1xX0oL6hA10B-kUAisFmTCmxDM7N-vC6NNKjmJzydf_9Y0vHQpxjm8fpiwFi-8P0lqZtgPSeBkKR2S3e68aLfU930M6wEeSCII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل انویدیا جنسن هوانگ و ایلان ماسک در حال همراهی رئیس‌جمهور ترامپ در پکن دیده می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119717" target="_blank">📅 15:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
میدل ایست نیوز : یک نفتکش حامل گاز مایع که پیش‌تر محموله‌هایی از ایران را جابه‌جا کرده بود، از خط محاصره‌ نیروی دریایی امریکا عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119716" target="_blank">📅 15:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رویترز: پاکستان و عراق از ایران مجوز ویژه دریافت کردند
🔴
به گفته پنج منبع آگاه، عراق و پاکستان هر دو با ایران برای حمل نفت و گاز طبیعی مایع از خلیج‌فارس قرارداد بسته‌اند که نشان‌دهنده توانایی تهران در کنترل جریان انرژی از طریق تنگه هرمز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/119715" target="_blank">📅 15:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بلومبرگ: صادرات نفت ایران از جزیره خارک برای اولین بار از زمان شروع جنگ متوقف شده است و تصاویر ماهواره‌ای نشان می‌دهد که مخازن ذخیره‌سازی نفت تقریباً به ظرفیت کامل خود رسیده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/119714" target="_blank">📅 15:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ به پکن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119713" target="_blank">📅 15:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119712">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سوریه به‌طور رسمی خواستار استرداد بشار اسد از روسیه شده است تا او برای پاسخ‌گویی به اتهامات جنایات جنگی محاکمه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/119712" target="_blank">📅 15:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119711">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
حزب‌الله فیلمی از برخورد مستقیم یک پهپاد FPV با بولدوزر کاترپیلار D9 ارتش اسرائیل در ناقوره، جنوب لبنان، در تاریخ ۱۱ مه منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/119711" target="_blank">📅 15:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119710">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
لهستان : به خاطر حملات روسیه به اوکراین، جنگنده‌هامون رو به پرواز درآوردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/119710" target="_blank">📅 15:09 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
