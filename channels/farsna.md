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
<img src="https://cdn4.telesco.pe/file/BtMVHioafcblr0vb-bN2CO2-05L0-WY5d1EccOgFgi8JhHuqcPg4kq0Ey6Khu03H0uPkLyQuT4DdFRj-tdWC8t3BNSfxhL-7wG5cl4xJhdiR5EdnHBhX3UD54z_gxxUf1u3rcrCqbUw5nRgpiKe9dPZ_BEx_1bAfzGYt8lab2iny2cHjXJdWR-7PhLrvGKLiaoJjwliEkUIFrcXw5Bf-v1Ix37SzhWbrWgdGjy5YvhUt6CMVETPpk_36efT8RPjrgLUz6ED6rtFr3l4RKVNzbmBu3uTRKTc5DYiHdjw9cLMh1JKw86laChrS2WTHsZ8fitIvwqkUEOtjLxz9X6ja7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.87M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-464552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3deb1c68.mp4?token=JxSR1y3VZ1B7Hj3LsmM8D7kjyMSLpitpXTnEzbhCAk6-WzUNv5mMSmCbtDVrznZbYZMBYUaF_2JCX6CAnYOp3CgSXAalLvPihCoDj0CvpzqzP1zftbi8C0z6AxRoSG_TLOgoGfll5753KQLqYxILlzAaEIoGOru4zLr3cGiBTSR4RBeiwp0TnOWioYH4CkBf9tnCzMWjyGTJ27xva0ugAFNax6RQc-LekhJgdYlW_WJcrZxtA2A0c-8GWvVDIcmsmiAZv3bXsg3z-_2BEaGkMhOEhdoADZOjzDOBK7hPXz-c7ehy9uc4vQTtwgqEwvofHF0AUAGgVAxy0uffU5OxJWz54kgPYsDmakt7UuAlCzL0L0AswvRbpYguAbtQIhZRRKe9eyOxwwNKgwh3W6oyjqiFwSkdXpuBjAiMCgEgWOGHx-XEOyJ78H95fWR2XEnHui5fkkJWFKEFgde2dZxGwwnyZE3XxK32a_LyyENRLpZJOPSYoo-nY1iUCKk8X4aItkhk8aYy-c59GtPcaJKM2w88ufmjeaIIrkrjsQO7PKGnT6vUjShxaS6ZenQ0J5d5sv_8rO29hHhSD_uz2xANmFwe3Ong74-DE0oSIghC3mrrIwykrxXCAYM-GxvXWLmwvnUYX_1y7jJPgTG6Thi67jSMPw5CDTItgabVkRtpcpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3deb1c68.mp4?token=JxSR1y3VZ1B7Hj3LsmM8D7kjyMSLpitpXTnEzbhCAk6-WzUNv5mMSmCbtDVrznZbYZMBYUaF_2JCX6CAnYOp3CgSXAalLvPihCoDj0CvpzqzP1zftbi8C0z6AxRoSG_TLOgoGfll5753KQLqYxILlzAaEIoGOru4zLr3cGiBTSR4RBeiwp0TnOWioYH4CkBf9tnCzMWjyGTJ27xva0ugAFNax6RQc-LekhJgdYlW_WJcrZxtA2A0c-8GWvVDIcmsmiAZv3bXsg3z-_2BEaGkMhOEhdoADZOjzDOBK7hPXz-c7ehy9uc4vQTtwgqEwvofHF0AUAGgVAxy0uffU5OxJWz54kgPYsDmakt7UuAlCzL0L0AswvRbpYguAbtQIhZRRKe9eyOxwwNKgwh3W6oyjqiFwSkdXpuBjAiMCgEgWOGHx-XEOyJ78H95fWR2XEnHui5fkkJWFKEFgde2dZxGwwnyZE3XxK32a_LyyENRLpZJOPSYoo-nY1iUCKk8X4aItkhk8aYy-c59GtPcaJKM2w88ufmjeaIIrkrjsQO7PKGnT6vUjShxaS6ZenQ0J5d5sv_8rO29hHhSD_uz2xANmFwe3Ong74-DE0oSIghC3mrrIwykrxXCAYM-GxvXWLmwvnUYX_1y7jJPgTG6Thi67jSMPw5CDTItgabVkRtpcpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بلایی که موشک‌های یمنی بر سر کشتی‌ها و تجهیزات مزدوران سعودی آورده‌اند   @Farsna</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/farsna/464552" target="_blank">📅 16:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464550">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bc4eec4b.mp4?token=NEoQJCZnfLvdlN6a28-tEOak6sZlQ-zZv3qlrgG-ScVWg8j2ar4FW14LoIl9ixrbpRYiQoOLkiFbjFPf97aLc3NKf8madXiq10cWcZV1zEmPvHX5bb-6fuWv_GrVgw5aVpxg9oNeWwk7LjB9umkvQYV9qtwTag_nhU2biEL-rQL_Lh4wYUIoQL-dE5X3ePZpvKnhRm0SPib1ryEjo2TCgATBagU2WPuAtANoyxntayMM_--VOjHyq1LaPOCLora0FOsk--TaXKUifPxzFWj6tve29j9mnXqmXja0nn4WL5nd4JEADs46PvEnVFkfbNxa1qiycvU2AXeDJTZs0W7Ydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bc4eec4b.mp4?token=NEoQJCZnfLvdlN6a28-tEOak6sZlQ-zZv3qlrgG-ScVWg8j2ar4FW14LoIl9ixrbpRYiQoOLkiFbjFPf97aLc3NKf8madXiq10cWcZV1zEmPvHX5bb-6fuWv_GrVgw5aVpxg9oNeWwk7LjB9umkvQYV9qtwTag_nhU2biEL-rQL_Lh4wYUIoQL-dE5X3ePZpvKnhRm0SPib1ryEjo2TCgATBagU2WPuAtANoyxntayMM_--VOjHyq1LaPOCLora0FOsk--TaXKUifPxzFWj6tve29j9mnXqmXja0nn4WL5nd4JEADs46PvEnVFkfbNxa1qiycvU2AXeDJTZs0W7Ydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زارعی فینالیست دوی ۴۰۰ متر شد
🔹
زهرا زارعی در مرحلهٔ مقدماتی دوی ۴۰۰ متر بازی‌های آسیایی ناگویا در گروه سوم با ثبت زمان ۵۲:۰۰ ثانیه به مقام نخست رسید و راهی فینال شد.  @Farsna</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/464550" target="_blank">📅 16:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464549">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXW2XOA7FUiN64-blK_DNbyFaEt3KwWZI0JzdHlixbR2tWTWjeVZsOWhVW4j-yMBjorX6lfYPhXhYiu1MIfvCAeDjQmyTKpeo8xEUmgPx44ez_l2fO4tsRrr3zL-zX5bgFX3LvaXAeugsSHBytAhzCGeoZyQo93KRltjo5smXFtwkoQuiBMHH1Ic1XYpW8YnSpIjIrk2iKa0v9xfc_NQD-Q_uCG0LnwuE6jQQ2qSCoxmUtjEKwa8zLIZiVB8c18r-bGHdEDJIX876AQDdTbB5ge1K0kZPnkajAZesYsXPt2SWZgHSOBjB3fF2HfnPi7wxfpkf86jwzOe9PiAqn5M7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا و چین برای مهار بحران‌های هوش مصنوعی دست به کار شدند
🔹
در بیانیه دیروز کاخ سفید، یک بند کوتاه در میان توافق‌های اقتصادی و سیاسی نشست ترامپ و شی جین‌پینگ از توافق مهمی خبر داد: آمریکا و چین یک کانال ارتباطی دوجانبه برای حوادث هوش مصنوعی ایجاد خواهند کرد.
🔹
در همان سند، دو طرف همچنین ایجاد «گفت‌وگوی ابرهوش» را برای تبادل دیدگاه درباره مزایا و خطرات این فناوری اعلام کردند و مقرر شد دور بعدی این گفت‌وگو تا نوامبر ۲۰۲۶ برگزار شود.
🔹
ریشه این توافق به مذاکرات ۲۰ سپتامبر در نیویورک بازمی‌گردد؛ زمانی که اسکات بسنت، وزیر خزانه‌داری آمریکا، و هی لیفنگ، معاون نخست‌وزیر چین، درباره ایجاد سازوکاری برای اطلاع‌رسانی حوادث هوش مصنوعی گفت‌وگو کردند.
🔹
در آن مرحله، موضوعاتی مانند عامل‌های غیرقابل‌کنترل، حملات سایبری، استفاده تسلیحاتی از هوش مصنوعی و حفاظت از زیرساخت‌های حیاتی در میان خطرات مورد بررسی قرار گرفته بود.
🔹
بنابراین کانال جدید از ابتدا صرفاً برای خطاهای نرم‌افزاری روزمره طراحی نشده بود؛ بحث از حوادثی آغاز شد که توانایی تبدیل‌شدن به بحران میان دو کشور را دارند.
🔹
هنوز مشخص نیست این کانال چه زمانی عملیاتی می‌شود، چه نهادهایی در دو طرف مسئول پاسخ خواهند بود، چه نوع حوادثی مشمول اعلام خواهند شد و آیا داده‌های فنی نیز میان دو کشور مبادله می‌شود.
🔹
پاسخ به همین جزئیات تعیین می‌کند که این ابتکار صرفاً یک تعهد سیاسی باقی بماند یا به نخستین سازوکار واقعی مدیریت بحران در عصر عامل‌های خودمختار تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/464549" target="_blank">📅 16:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464548">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttgxC0C5RszHy_4eK9FI1NTqfFotr3Yl8moAjA4JIZ8VcMMK_aWhZe_fvea4WjT5xUerE3qq6ecR0d6AK1ACeZpGpGxWsYsT7nWubxp8sfkllI6xgVOH_eIgPeXaVPBtZg58OP7YH4NjLNKrJoW_3NSLQF7EfhSiMvHWeGORB0ip0ggocv2sBzCOxeyL5pyCGwW6AjEzWJy2x22aCOaqry7mu-GlrDirsXLHcSDkIrhGLqjHrRk0NJEhjOiXcrg3r99Te9zhQERh-FdYeeweFLOKFhxy1cpzoov_gyCDhX5JGMVriO374TAafDieNX6CEVLuR2aM2Vvfgh2Gy_089A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیۀ دبیرخانۀ شورای‌عالی امنیت ملی دربارۀ برخی اخبار خلاف واقع در‌ موضوع حمل‌ونقل هوایی
🔹
انتشار برخی تفاسیر و نقل قول‌های خلاف واقع از سخنان دبیر شورای عالی امنیت ملی درباره موضوع حمل‌ونقل هوایی، موجب طرح سوالات و ابهاماتی گردیده است که بدین وسیله اعلام می‌دارد:
🔹
۱. ادعای اینکه ایران در مقابل محدودیت‌های هوایی اخیر دست به مقابله به‌مثل نظامی می‌زند، تکذیب می‌شود.
🔹
۲. مذاکرات میان ایران با کشور‌های مربوطه برای رفع برخی محدودیت‌های هواییِ غیرقانونی ایجاد شده، با جدیت درحال انجام و پیگیری است.
🔹
۳. راهکارهای غیرنظامی متعددی برای مقابله به‌مثل وجود دارد که در‌ صورت ضرورت، برای برخی از فرودگاه‌ها اعمال خواهد شد و البته امیدواریم که مسئله به این نقطه نیز منجر نشود.
@Farsna</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/464548" target="_blank">📅 16:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464547">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTsJvL_TyMt_SNSjxmTvXBW3C6AGfQ7rOhyZgENVa_V95h5GQ5-oISgL-muWz5ufcQRsKuc_11fwFDtbGGwEV0k7vNSsfrLQJeGFWPI4oQ6n6JUeQz3BYaj5dTxg6IA6of-YOEpmxwYARhZmz7E2iYYKppypk4cSWJCxWHiUdRvpLOvQn_42xFyfFpsxDd69LnA7Oh5NearBBQdXW7RcXqtL3O0EPDKjZE5HJq8m8igVS9WDxu0pgx2pLYUh6yDNI_GW3JemtK0vO1m5iGysZw64IsUZY7t-SWXntz2OF3P3eLckQPUYoJ5CKauJ7g1TbQXZIraihTkovoqaqgqMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: من انگیزه‌‌ای برای شرکت در مراسم روز ملی عربستان نداشتم اما از سوی مقامات ذی‌صلاح سیاست خارجی به من ابلاغ شد که در مراسم شرکت کنم
🔹
من در آن‌جا حملات آمریکا از خاک عربستان به ایران را محکوم کردم.  @Farsna</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/464547" target="_blank">📅 16:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464546">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI8Lah2ch6PUOMtmKV1fdDHuden1VEYU0zjCfYnfY_sGsoooaynQjbaKVX-1B7IEHgDSzmWnF77Qej7MmGi_cNHXV0VG5DykvUH8Av4-zw0DXVr0vA-U3WerNx0Jsf_yJJJC6UJbsmPfoHbHT1rcWxK8ORxJ7f1-o8WGb57Ah1VutWvwW3GDfRwN1QpDCQv-iLLsmEYw-jJDbtFcbldyGXJpeh45tTf5yvcgSAizRu1szg6gRaAXblXav5BzZ7IjsIw0-u4ibhnh5cz9jnuDpyaZDK6EWmx1ibqQ80eHBLUEl8bt0exLunep414LNBUlhQU5Q7GMZWdM0TqyR50y7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رودخانهٔ اتمسفری در راه ایران
🔹
نقشه‌های جدید پیش‌بینی هواشناسی از احتمال شکل‌گیری یک کریدور گسترده انتقال رطوبت در اواخر هفتهٔ آینده خبر می‌دهند؛ جریانی که می‌تواند رطوبت را از شمال آفریقا و شرق مدیترانه به‌سمت خاورمیانه، ایران و آسیای مرکزی منتقل کند.
🔹
این نوار انتقال بخار آب در صورت تثبیت الگوی فعلی می‌تواند شرایط را برای افزایش رطوبت و شکل‌گیری بارش در بخش‌هایی از مسیر فراهم کند.
🔹
با این حال، زمان دقیق، گستره و شدت این سامانه هنوز قطعی نیست و به روزهای نزدیک‌تر و خروجی‌های جدید مدل‌های هواشناسی بستگی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/464546" target="_blank">📅 16:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464545">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آغاز عملیات ۱۰ روزهٔ خنثی‌سازی مهمات در خارگ
🔹
بخشدار ویژهٔ جزیره خارگ: عملیات خنثی‌سازی مهمات عمل‌نکرده از امروز به‌مدت ۱۰ روز در جزیره انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/464545" target="_blank">📅 16:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464544">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پروازها به ترکیه همچنان ادامه دارد
🔹
با وجود تحریم‌های جدید آمریکا علیه صنعت هوایی ایران، ۵ شرکت هوایی قشم‌ایر، ایرا‌ن‌ایرتور، سروش‌ایر، آتا و تابا با واگذاری خدمات فرودگاهی به یک شرکت ترکیه‌ای پروازهای خود به این کشور را انجام می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/464544" target="_blank">📅 15:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464543">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc4f2efeb.mp4?token=WQhsRvJGZXJP9byVFx2RR4C7fo6ondjjz6nAb6cmozlzg2jlws-6PzG0dReP_HMrL_B5uamtnZqngQUbadBUVH_bv_wi9xnZI1XXZ6zR5D2yt2LUXZyaaYDOdHzzJOmL1DgvRLQUGKNax2tiLi22Nlb1iMT7nUUa1HVHtnvVcnguphfwAy_zItOGNlMAoRbCilns5HyOQpqyGIcjoImhe12EpORPp6OGRi_GN-NHHrpAthu-JFY3h8xEyUKzPzD6kWu2reyJzMkIeDYQuWXsE9xEya5OtALfZfDg65HbQCHyu1SidDes9AMlKjBkW8aOSROiwgzwfk3PqIo7Lm1MTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc4f2efeb.mp4?token=WQhsRvJGZXJP9byVFx2RR4C7fo6ondjjz6nAb6cmozlzg2jlws-6PzG0dReP_HMrL_B5uamtnZqngQUbadBUVH_bv_wi9xnZI1XXZ6zR5D2yt2LUXZyaaYDOdHzzJOmL1DgvRLQUGKNax2tiLi22Nlb1iMT7nUUa1HVHtnvVcnguphfwAy_zItOGNlMAoRbCilns5HyOQpqyGIcjoImhe12EpORPp6OGRi_GN-NHHrpAthu-JFY3h8xEyUKzPzD6kWu2reyJzMkIeDYQuWXsE9xEya5OtALfZfDg65HbQCHyu1SidDes9AMlKjBkW8aOSROiwgzwfk3PqIo7Lm1MTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت نیکزاد از کالابرگ؛ مجلس چه می‌خواست و دولت چه کرد؟
🔹
نایب‌رئیس اول: مجلس می‌خواست حمایت از معیشت مردم به‌صورت سهم مشخصی از کالاهای اساسی و متناسب با نیاز خانوارها اختصاص یابد، اما دولت مدل دیگری را اجرا کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/464543" target="_blank">📅 15:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464536">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERzDE1_m_YbPpq4Qyx8NymEJ6NZ6ECpw5wXg-5tYTwE2MpTlSjnaWm71ULgdi0uIxs35EkTEjLsnGGyeraA7Hb39tUahhRUy5XppABheBL-AZE_PQf0dwoYjjyO7rYXen1MRGSBFXP2hLa4XaTVXNKJ8GnCa03P1KGWLB0SkfWt38F_o5REfXAXMAxUQIGRHzZYZHsE9jZInjO9WnCgPwKntN_NwUqdWNT0fPh77lXmDoHl4rrcQd5rd16tQa43QyDNKIdwMGwc8YKUaEdANl0vohtH25ESl4jyZ9327OX1pPUDWSjFtKmV0zPrGsK86qeifLpRP5apCLq8D5KPqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR0J7viU3uo4M044TMNiqHVJIosprxsM0tp1tMRR-yWTm-S-skPb1qmj-2xp49ZQL6P_Fa7dUZKf7jPTiFmLNDjNo693_ur_lW6RCuAQyhEasJwfDBVwqItNcgTWTtj87WEt7960psDavvVM2qwBS4vDaNXoznyrYstzMW0E00P3EQv1LRCPu4HE2WF8Ba3Kgem8yrpw0khS84VZ5Q-oRncTlBAgwYgf2jNsvMBdrtgBomE4uoc-U4K1P4IyFNDmAJFFXdhWXzdLBs_Rqfyjuf2SnHz7NbZHi8hYRS9zBXFToBDEnbLpcLYbyXuPdqWSnpY8-HeZ3O3-aivsP2CavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuyUZIpPb7r7LVb-O_ocKX-2HDOYXYM_Ro08y6iL2OHfYI74Onh9e8koKcqm2KcNiT0o4MVGFqVZGkr_zQsBV3GmKlUN2sWx1D_mZBG0gPLa9tFtMFXe8ogjIgPUjVHZs8Miir3evtzr8rat0PLfJN-tUq4bneRVZRj99VgOiVRVIxyPf3q3Atw1rxW5Rab8kEkmmhoqpH-G04BFrj3grBHg3_ptOK-pSjwpEfVaM3rSxQPdyC-89VFi4mayQxTp5w23E7OSx6FpifNqF333fN0Q8EnvfnhXt9CeVpqv1aYmDD3vkGBF1y0xLur_vi7X2bIEH1bqjjengxgq-FQYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr14u1z-lprrB2EUDPadftysEgjDlyYfhP2_ZtHxK3i8Q8LykOjX57CvlLWh5fBiT_B9HAOOT-oTMimtJz1Fn-snEHct6hDP62JOBkFm6L_9IH8LtNfHrQ0HepMZemJ8P_sED1T1rP9OmTL24-gS4Eo_E4eHEUWNmQU4Eif6I8ku_BG7haiqE7ccIt5OB6w2MPWTg0jRnUx5M6HZE2WNJxFNEnHWBlMChXO74KIrgvpnq9ORkkJPP7SiN1HRO3IS0wPTZbnxRhlfIXHopIUt1aztEmmTC9gNzi18RqUqeCD7RK3uySVn7yf5GwRjaaTUrbEBy0nnGXkXZHiNO-05Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGbbE7Nl6riY8gXsZW4uvNgBXb578n5P64FVEtl56s8JK6HlieWQ7K-r833eX7bJTNmAg1_2cuk2Bus4Mnii8pD-B3-8Qh6E0jnUYTYVd0xIhSZOTn_78d9URzHFdeVt9uR2RDgtfZcn21A6uWF25Qq6VMKF4LqbeO00tMQY48wZwM1HRKbFhspYpgP93UVxww1ize5gpcwcBTu1ivym65ErY6yT4uh4GxOGNquqy10K43O6a71G369sUu_gGGUyyOfWu8vDW8y3Hh4woaS2fZ8ChsH__wqjyMQRcJxrl8ywUTHksWKYKGdrZ3qEoqKYclJWWdGQL-1waqMHONP8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVqRF9pr8IQjxlA-XFZ0DTs14LOMqXr3s8Y3ueBdftQTtV5eHNFHBzWipWf89ZHlgynaAydwwGlbnhaxmYhbSKuuF-ddPGvKrlo69DqBWHElZ8caPUuPyu2s1DaNY8994FLkXX9kSzTOUYG7Baztxnk91KPn_3YYpPis4f0IJ2ZcDCD6uCTE82FwOV-xoDMewLCwRwGu2UDh18Uzt8niONqDSTcqCesGCrTd5MF8hI-IN9E-AT4ZsUT2miaQACuTUGTCiS2ypuw0U-yhPC-kAesMaFzvYb01NMnRohQzlFnbIMDFRXqmM2lftQD9lKXdk-a4sLtnfTz7vZMSg6aFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0ESSy8gzY6RZ1aV_7ByjGy8xupWY-g2g31kMaQxagNwZtcufooQdmwH1jtB1mcqZGuuQErUBxKGoVjS42vnscoeK3j6XsPPDYEwZB2AfqBgQrw9a2xLtR2pdAdNWPn83LFXvxSAa1qdr6P3oqj7uTepaS4jpZlLSszOO7ieGO2vQK6eMnRZHfQjivyKk3IbKRACy9zTaiwEDK6SIh2ObwqsLE2kWD-cOHu600fsM18ThaOF6pKlUcq2pVFg2mNj0vkdbUv5IOrvOsq62AykSinX8lZJHaXMRz7QupuDa4cDPGSNpS0c7-GzRTRuf2TfTeHjWL0f81kbeIedul0h3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید سخنگوی ارتش از خبرگزاری فارس
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/464536" target="_blank">📅 15:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d427f3b1c.mp4?token=I8cfhxvBhVVklZlZ_P7ATrD6gZaBZ_MMme4ubtzYdEmjF-01cOsH-9H4qcPZ5PFYvnHTyrqvdqC1WFjqCLIQB3xEnZmuN8v0I9sIfqmtYIQxAvgs6kWdxQJiS6Tf7KJch_6y9wbycaVSu0ekP3FlihN27x_FXDD69FkR9z9TYPytbZK5c86C84ArvCU7FeuTjNLfrHps-HFY_5A2yafBWD0RBLNeygvJmAmdgbc8NVrmvT5YK04iDvn3uwcx6AtVa-tH2mAowDD9t5I9gPGixj_uDZ5fZSdG4RQO6LQ_YnPVEFaZjnNSL1fxBFn105vNAwrXEnnFfmqrmxZ5JtNYpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d427f3b1c.mp4?token=I8cfhxvBhVVklZlZ_P7ATrD6gZaBZ_MMme4ubtzYdEmjF-01cOsH-9H4qcPZ5PFYvnHTyrqvdqC1WFjqCLIQB3xEnZmuN8v0I9sIfqmtYIQxAvgs6kWdxQJiS6Tf7KJch_6y9wbycaVSu0ekP3FlihN27x_FXDD69FkR9z9TYPytbZK5c86C84ArvCU7FeuTjNLfrHps-HFY_5A2yafBWD0RBLNeygvJmAmdgbc8NVrmvT5YK04iDvn3uwcx6AtVa-tH2mAowDD9t5I9gPGixj_uDZ5fZSdG4RQO6LQ_YnPVEFaZjnNSL1fxBFn105vNAwrXEnnFfmqrmxZ5JtNYpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طیبی در پرتاب وزنه طلا گرفت
🔹
محمدرضا طیبی با کسب عنوان نخست ماده پرتاب وزنه، مدال طلای بازی‌های آسیایی ناگویا را از آن خود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/464535" target="_blank">📅 15:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464533">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAT_h6oTPSKy1teRS1-dHDCw4xMawhGLGzCCxNew2-nroEG9c_RuTN4WMsmK2vtVMqAlgtelsGmZCm_C5N9fgw3U_tNLWbsEcdc3l2WIDBZy7yFw4hrU7-CQyhBrrcEJD3GC7ugouMY8va9XL1AH5Yjg_73lwhFE0vDwTWUgc6_5ML4HowX5FMA6UwtvG-0mGDmpresntiYamxyobufOvQVzSpM2YX0T5KYcw9yf7uAo2ug4pm25HXt_LAS9HGMp2ucZLu7i-RKbd2KmXQkG4gDEG7_T_lu4VAHwJKDp6ydQzVOQWBCb-zwTQSNGY_gFCvF4-fNTvU8s5z-pg-tlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a037f0aa2a.mp4?token=jyx86R-Fd1U36xi-gqCQ3utwrNlPAK6LMnYqBlvElZ_pYAU5rkhjyiDCrUcIBCgtm3q0B91aJVO-9GC5Qou1So_o7-3JB5WPw_jScJ_WxbdlQrujUVakGljBrL_jq9r48XvfBwLYpJdaBNosBaFalubJNgZBD2n6RXh4Ujn3p1fF_GZ2TyPTcH1DQgK6zQbBMP8aUBPf6uIk6-WU1gCz3sjXK4B6HE9uJz5Ciga1rPUIZN9UJ-dA9BGlpqUF5ye9OO-qvrfHwVbWkW_hy6GEubTQqngEWepPPvb2Y9cmTMizKi3BnToT5y_pe4Fanq5Y-N_faImA4fKl7h2ZBS6XIJdDHwMnjv91ue0b-zWEJ19rHI2ZelPqD1_mjDqbrbZHpxZZJazqT1MVrrs72J5Ijq4g-DmAuFZvXBaUBzHrb3qjyKohbFbuHVyrHowvIXDgonls7COgG4BcJcczNeARnZDXC1sXl_OrjJid2KEWYneTPqfsHVSGxxCG9s684ETxdq73RYXL4ZJVF7P1zFMiaEbTwExKMrrEjr83oPLvvU0_Mp8p-oAZWfVWSOvPMHLSNlO1afFPq5aS9vxRvlqHIFwoE5utHFuIrxwfQ0zYm4EIQVy5nFMhJZK6m9pabaID06SgmbDp5GpjXZcFGEDaY98xa-ib1-ItMUsh7WR3hAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a037f0aa2a.mp4?token=jyx86R-Fd1U36xi-gqCQ3utwrNlPAK6LMnYqBlvElZ_pYAU5rkhjyiDCrUcIBCgtm3q0B91aJVO-9GC5Qou1So_o7-3JB5WPw_jScJ_WxbdlQrujUVakGljBrL_jq9r48XvfBwLYpJdaBNosBaFalubJNgZBD2n6RXh4Ujn3p1fF_GZ2TyPTcH1DQgK6zQbBMP8aUBPf6uIk6-WU1gCz3sjXK4B6HE9uJz5Ciga1rPUIZN9UJ-dA9BGlpqUF5ye9OO-qvrfHwVbWkW_hy6GEubTQqngEWepPPvb2Y9cmTMizKi3BnToT5y_pe4Fanq5Y-N_faImA4fKl7h2ZBS6XIJdDHwMnjv91ue0b-zWEJ19rHI2ZelPqD1_mjDqbrbZHpxZZJazqT1MVrrs72J5Ijq4g-DmAuFZvXBaUBzHrb3qjyKohbFbuHVyrHowvIXDgonls7COgG4BcJcczNeARnZDXC1sXl_OrjJid2KEWYneTPqfsHVSGxxCG9s684ETxdq73RYXL4ZJVF7P1zFMiaEbTwExKMrrEjr83oPLvvU0_Mp8p-oAZWfVWSOvPMHLSNlO1afFPq5aS9vxRvlqHIFwoE5utHFuIrxwfQ0zYm4EIQVy5nFMhJZK6m9pabaID06SgmbDp5GpjXZcFGEDaY98xa-ib1-ItMUsh7WR3hAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش بغداد برای حفظ مسیر پروازی ایران شروع شد
🔹
دولت عراق برای از سرگیری پروازهای ایران، با آمریکا وارد مذاکره شد تا فرودگاه‌های این کشور از تحریم‌ها کنار گذاشته شوند.
🔹
براساس بیانیهٔ دفتر رسانه‌ای نخست‌وزیر عراق، هدف از این گفت‌وگو «فراهم شدن امکان از سرگیری…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/464533" target="_blank">📅 15:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464532">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ff45c108.mp4?token=Hv5VThzAUIKbFX17H--csu4XZivAMwnySELvsGbQrTZkBMoQulcJKkkpeoo-Hj6jpU6NAyvKOm99-VaX8vFSiBgcF3fIy2ohCJNtjbuJYICO0dLl3wnccu-MzxkkNRCU7fuVMkvndHxQICm8ijGIcvAHGdRWbHoV06iTXlRr1ittpsWG1FTZadjx6pT7RP2iekJwevytT8tcc5aylvgQriYDcM13JVvFr_mfApZheBOHwxv2OGVUc517UYoAl0yheZZpR_KT676_u95x3sV1RcUmBIfIG-BmZnERtYazDdYslRa2dNKyoi38GH6-Kh21yV8wbBDLV6aEcSFQrPssVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ff45c108.mp4?token=Hv5VThzAUIKbFX17H--csu4XZivAMwnySELvsGbQrTZkBMoQulcJKkkpeoo-Hj6jpU6NAyvKOm99-VaX8vFSiBgcF3fIy2ohCJNtjbuJYICO0dLl3wnccu-MzxkkNRCU7fuVMkvndHxQICm8ijGIcvAHGdRWbHoV06iTXlRr1ittpsWG1FTZadjx6pT7RP2iekJwevytT8tcc5aylvgQriYDcM13JVvFr_mfApZheBOHwxv2OGVUc517UYoAl0yheZZpR_KT676_u95x3sV1RcUmBIfIG-BmZnERtYazDdYslRa2dNKyoi38GH6-Kh21yV8wbBDLV6aEcSFQrPssVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: تا ۳ روز آینده در بخش‌هایی از شمال و جنوب کشور و ارتفاعات زاگرس و البرز شاهد بارش خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/464532" target="_blank">📅 15:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464531">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e06262d0d.mp4?token=QNb9QUCMmK8ToyPV_uqhruH8shMMWPuHuB_tX_SySTcO5FErdrRmZ_gs1JhhOg5C1EA8m1MUUmTeAnnxWMmCu7t-TYVUfzcd0FmnnxU-W8uqQ6xiTodS88bq31H9MknqZeI3ejPGKEXiyO8y8oE3lEFzLZyeME4Q5lV3fFRC-3ank5k4tvPcwb6FhAg9MZmUcmNbk7h3w1MKa-g1qiaAluaGf4jz9Dj6v8nMgM2R6m--ycTTfbplBAMOkXyxirkOlJjEIUve1TLVvi5z46Sxhdh_OAiUi6agvqGWOYqu3uh2yNGkVLpwPl8Ico-3CTojomLuLxLsOHPzi7AAHvhCaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e06262d0d.mp4?token=QNb9QUCMmK8ToyPV_uqhruH8shMMWPuHuB_tX_SySTcO5FErdrRmZ_gs1JhhOg5C1EA8m1MUUmTeAnnxWMmCu7t-TYVUfzcd0FmnnxU-W8uqQ6xiTodS88bq31H9MknqZeI3ejPGKEXiyO8y8oE3lEFzLZyeME4Q5lV3fFRC-3ank5k4tvPcwb6FhAg9MZmUcmNbk7h3w1MKa-g1qiaAluaGf4jz9Dj6v8nMgM2R6m--ycTTfbplBAMOkXyxirkOlJjEIUve1TLVvi5z46Sxhdh_OAiUi6agvqGWOYqu3uh2yNGkVLpwPl8Ico-3CTojomLuLxLsOHPzi7AAHvhCaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کبدی مردان به نقره بسنده کرد
🔹
تیم ملی کبدی مردان ایران در دیدار فینال بازی‌های آسیایی ناگویا مقابل هند با نتیجه ۳۴ بر ۴۰ شکست خورد و صاحب مدال نقره شد  @Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/464531" target="_blank">📅 15:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464530">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c31ef5224.mp4?token=Bo0kidfitmQncbw5J0LjiLePgOH5z-biCUHTfqdNcQBE7mZsu4M2o3HLm6Qz1_t30fZqjwTtiaOvUbFDYiZcelVbiAk6vsaiDXjbSxvfg7VNzfv9PCNS3LKkgfRywG8vSBekc0c2KTe71abVVRnqOwVn_Xm3GVTwfg09cY7pYHp6fFzU6PoM1N90zOcLOL4mAoRU3jPSHC-ETli_7X8D3z75Fzcn-4nBuPUIjvId-QELB80g2LzHNFP63DTFbk__uf5q7on3CZ4Omq_BT-cc_Mt-FQQOXmC-aH1tzkBzmHhzV6xs1caNIHeiIF0nw3MapSETWY0hJqeMLAr8w5S-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c31ef5224.mp4?token=Bo0kidfitmQncbw5J0LjiLePgOH5z-biCUHTfqdNcQBE7mZsu4M2o3HLm6Qz1_t30fZqjwTtiaOvUbFDYiZcelVbiAk6vsaiDXjbSxvfg7VNzfv9PCNS3LKkgfRywG8vSBekc0c2KTe71abVVRnqOwVn_Xm3GVTwfg09cY7pYHp6fFzU6PoM1N90zOcLOL4mAoRU3jPSHC-ETli_7X8D3z75Fzcn-4nBuPUIjvId-QELB80g2LzHNFP63DTFbk__uf5q7on3CZ4Omq_BT-cc_Mt-FQQOXmC-aH1tzkBzmHhzV6xs1caNIHeiIF0nw3MapSETWY0hJqeMLAr8w5S-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشایی مدارس ترافیک را ۳۰ درصد بیشتر کرد
🔹
به‌دلیل آغاز مدارس، ورود وسایل نقلیهٔ سنگین به معابر شهری از ساعت ۶ تا ۱۰ ممنوع است.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/464530" target="_blank">📅 15:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464529">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac324dbb2.mp4?token=H0zRJ7MUodNrpSEsdRTMyDJvcuZQ4-gRXZECrNJHXyg930Ur9uD8EnVMwZNat6bRfyd-RiFhxvew-C1UNA0zDoDmSN3PhSGuysgzgEnNy1VhI0JssnyOoP3bF5_XhpRkZCJSoMochQ6_u1hgJLPnoqciicjhoCF_hV3vullf4y0L7EBM1ZbXjo0YonHD-LACAV7tgBCkbPIC5IGKFuMLKGkoQD0LN5WthngIuLJfzOqkc-aYUy5EgLpZIQS1ielbY7pzIwrBtaHoEliNNyKE8l3M1QRyg-8EkNze9AnP2KwJAUh8rOB39BPTjQxyuGigif2SZY5mEYv9CywMHasiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac324dbb2.mp4?token=H0zRJ7MUodNrpSEsdRTMyDJvcuZQ4-gRXZECrNJHXyg930Ur9uD8EnVMwZNat6bRfyd-RiFhxvew-C1UNA0zDoDmSN3PhSGuysgzgEnNy1VhI0JssnyOoP3bF5_XhpRkZCJSoMochQ6_u1hgJLPnoqciicjhoCF_hV3vullf4y0L7EBM1ZbXjo0YonHD-LACAV7tgBCkbPIC5IGKFuMLKGkoQD0LN5WthngIuLJfzOqkc-aYUy5EgLpZIQS1ielbY7pzIwrBtaHoEliNNyKE8l3M1QRyg-8EkNze9AnP2KwJAUh8rOB39BPTjQxyuGigif2SZY5mEYv9CywMHasiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پناهیان: فقط یک نفر در دنیا گفته جنگ ۲۰ سال طول می‌کشد
🔹
حجت‌الاسلام پناهیان: اغلب کارشناسان دنیا می‌گویند جنگ آمریکا با ایران طولانی نخواهد شد، اما تنها یک آدم در دنیا گفته که جنگ ۲۰ سال طول می‌کشد.
🔹
این حرف که می‌گوید از مردم بپرسید راضی هستند جنگ ۲۰…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/464529" target="_blank">📅 15:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464528">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c74129e8.mp4?token=Sa2pTLS-WDa4YkmKRnluuiotqvSBlTWoXwZkOETE-ZMxg91_hyoiYKcdJO0SZaQwVxKl-2Ol_VHhgw4wnX8necHo6AhW8e7YqVTd5KDyf6pw57WsUz7BOekgC4uyX3QmK32jF0rrjaZPBZYyr5QscprMArjwWwEItmIWHPaB3k_tZ2B6XexyZs3uD2wEg6Xs2lqX3gcDiZZ2dX8IA3fwHGvYqw_g_B-7baK8ggnxU0uaMd3Pjg3oRgRLAA5jfMAIZcleDXb1IfFIOS391DIvuiYmhoMoyV4a_w6XKy77vA0gcL4qI4DQENPFXFD7aVOvlOk21HN2s-yXMyCrcvtcwgxezjdRBJBG_189Eqh3gcxcOFiSJmAi2zRTFUU6nWKYZ43FuNHZLLilIxySHjxN6R17wve9dyVhE2XhIK1v_w6cyZGAObLYATq9kWVRq6VpnKg5CJOZWa5BnmhAwpkpEm3BuArJOwCmrazV5uX8f1-k2wo5U9ywpy3cT2bzCb5_il-A2SJ_8N56_Ptn5gnBzFLNW2Lf6v4P8kj2Pqvkxczazdc0SKQbEeSyuvp6km71-dBCgYigwdKEXEpw5QSk-y-jY3Vb_fRktDcKdgnqNA7Tf5y2erFmm6V8xOMrapAo6JnL1ThNf1TOkDNcZ1FRzTTSwdgfavxZAlOLGavVOpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c74129e8.mp4?token=Sa2pTLS-WDa4YkmKRnluuiotqvSBlTWoXwZkOETE-ZMxg91_hyoiYKcdJO0SZaQwVxKl-2Ol_VHhgw4wnX8necHo6AhW8e7YqVTd5KDyf6pw57WsUz7BOekgC4uyX3QmK32jF0rrjaZPBZYyr5QscprMArjwWwEItmIWHPaB3k_tZ2B6XexyZs3uD2wEg6Xs2lqX3gcDiZZ2dX8IA3fwHGvYqw_g_B-7baK8ggnxU0uaMd3Pjg3oRgRLAA5jfMAIZcleDXb1IfFIOS391DIvuiYmhoMoyV4a_w6XKy77vA0gcL4qI4DQENPFXFD7aVOvlOk21HN2s-yXMyCrcvtcwgxezjdRBJBG_189Eqh3gcxcOFiSJmAi2zRTFUU6nWKYZ43FuNHZLLilIxySHjxN6R17wve9dyVhE2XhIK1v_w6cyZGAObLYATq9kWVRq6VpnKg5CJOZWa5BnmhAwpkpEm3BuArJOwCmrazV5uX8f1-k2wo5U9ywpy3cT2bzCb5_il-A2SJ_8N56_Ptn5gnBzFLNW2Lf6v4P8kj2Pqvkxczazdc0SKQbEeSyuvp6km71-dBCgYigwdKEXEpw5QSk-y-jY3Vb_fRktDcKdgnqNA7Tf5y2erFmm6V8xOMrapAo6JnL1ThNf1TOkDNcZ1FRzTTSwdgfavxZAlOLGavVOpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۰۹ مقاومت با یاد سربازان وطن حال‌‌وهوای متفاوتی داشت
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/464528" target="_blank">📅 15:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464527">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdaLwDOlnGHZwmreESLWlCbUXRPB8riySaJfgPcoqu9i8uyr6_EuMJJbJxi_-rhHg6HDFZJqWJNeZw2sKFvQk7jDWx9BYIkUTYuYcbVrFIfEaFZF04dEDFsUclOOr-d9KR1rLXjJzAlWqlFDJyERSqhVWwT_a96MoJB-L8CYQyhxA7x8MIChYNpvFmPpHqAM9xJSD_JKmVLa445XnUjqOLxLrZdxoLC9PA530-cr2TILH_cjHC9fGJ70oHXJNLbehInzXz-W8AVqt7oDqTgCJZQFy4173v0ZKZvR9w_WH00zYCLqZCTqRyQ7nYgMUvWmrnKd-_vkIjPlIc2dWZUpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرعامل تراکتور: با پیگیری ما معافیت بیرانوند یک ماه تمدید شد
🔹
بدون اینکه بیرانوند خودش به نظام وظیفه برود برای او دفترچه صادر کرده بودند که این غیر قانونی است. همه به بیرانوند گیر داده‌اند، مشکلات دیگر ورزش را پیگیری کنید.  @Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/464527" target="_blank">📅 15:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464526">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
حملات جدید پاکستان به افغانستان
🔹
در ادامۀ تنش‌ها در روابط اسلام‌آباد و کابل، ارتش پاکستان خبر داد که «۱۰ نقطه در افغانستان» هدف حملات هوایی قرار گرفت.
🔸
بامداد دوشنبه ۳۰ شهریور بود که پاکستان به افغانستان حملۀ هوایی کرد. طبق گزارش رسانه‌های افغانستان، ۳…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/464526" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464525">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb470a098.mp4?token=Zjcp6bGabGMY6F5ZuYCWd6nVMhUF_tFr-PZ_541FBgFacdqxcomjydSn38_LavRB-uSauEqlEC8uaMlJ2ep_Xiul5OMyc8mIeLaq1s2XCPZ7GYRTLnedqTUvC5uGIBL_mJCJVBASkCtWevViKV4WCIC9Tl-3VvkHboej5DkmGUXOg-d4KXV3-_WHayzMrCgv7qt9GS9CCxnnORYRstpIJZj8VF__okY6SWMLWaAdGhghVTPwzERycPFsVqNe5i6waJwWb5St3Kwlpg_UEBGSJRESIehkdaJEpJvuqX4fwddFhnmeimjpKVWFx07N-eGgFjigmavg5_52vZfSV-VNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb470a098.mp4?token=Zjcp6bGabGMY6F5ZuYCWd6nVMhUF_tFr-PZ_541FBgFacdqxcomjydSn38_LavRB-uSauEqlEC8uaMlJ2ep_Xiul5OMyc8mIeLaq1s2XCPZ7GYRTLnedqTUvC5uGIBL_mJCJVBASkCtWevViKV4WCIC9Tl-3VvkHboej5DkmGUXOg-d4KXV3-_WHayzMrCgv7qt9GS9CCxnnORYRstpIJZj8VF__okY6SWMLWaAdGhghVTPwzERycPFsVqNe5i6waJwWb5St3Kwlpg_UEBGSJRESIehkdaJEpJvuqX4fwddFhnmeimjpKVWFx07N-eGgFjigmavg5_52vZfSV-VNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجمع بین‌المللی فرهنگ‌های متحد در سن‌پترزبورگ روسیه با حضور وزیر فرهنگ ایران برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/464525" target="_blank">📅 14:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcohvRMcC1NmOWxVu0ZNAD1P79nDeaNh3phfWmn0euek3qnBDP6fqJN6TPonjbwEQYlHaFTdAF3J-YGkTtT4Xqd9iulVwgWCb_YVnh-ixQgpmStEqQW-fQocBStwncv8HQbEjdgvsxQCDixTwvSvv-Sh8hE9ZHkI4XMXoEpVWMbpgWzEEOD7iHE-rgVxaeq7_qrB7_4yBPCuogWsE-R8L02mhnMdK61JitgXwtkk0VLgrhSQdwy_8XqRonN7B4xlgf8Gx3V0KoIsKcia10jZIJzXZiEhshwyaO75ZHflShV5KqqDc_79QSx66P65Jon789LXvE4YMJMwu-xruMosOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVNq5txZtSR-qyFjrfzYJ01yjp6wJk8k6cr3TKjxkHPSneXK4RpeJ-1G3XKei76r2wcMxTdyS2aT9pclPZLbB9V6BVJYDp7osVwponzCp7QYPbDwyjR5AGkZBN7cLrttZbqwG5U9OcMvEY_l9zWdNmuhRPYFsIqr7N4xyosi5VVZzPGo__utXulkGUQsrT1Es6WXlu4EhLLieWZ4q0Xk49VWdRKLwXEv09Bj7K4dkvsoGZWFxRGZ_3whNaTjcGvX30_mnjlsoeGAtuea4g6snyd2fRcrUkGVlW_US3cbco0JEF0b275QGjm2wWUyRUfFd15B-uUhmsIM2-woLAZ78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvrEMs-dm2c_OvjRMNmoHGdanTyNDWkA9LkOTkQa_84dzPqys6SpPZDpDXt7gyocRO3MPNkFD3DIDz-E8HxPi4HilhgwZJ4vvCESW0bz9wDiLh2tSNOe8gq7rIGti81Sj-bedpdNhvU4FD1bQ93fpu4YvzBzeETnS6lveAbmo34MmAnm-lX9qx-61XmfPawGsf4ASKcuGGRS_jRW2-NhjpNHzDhtPR-28__kGj-BmWF6_CZ51B_n5SwE_5U4gaK7zh-x-RsZL0ujBs-BArOWeAh2S3hN6etpvkVk74YWHe3AJnjWXvNC4FaoxxI7qPto83IC24dOcvks_IDSVh4Vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3VY2Lp7dGA6lQBmY0A6vmqHOzGvEcGpgEfTBIug7SaQWjFItF-E_sOWxMzg9IE2df_Cp923iHjfx5eA__FgVX9fO555xdEFonZg-PuTQgUMa2TBPC8tgXofcAq1l_USYFWk8AJvPNjuutf-VytjcU_61dUGfVeepa2PoewE-mei1nlfoHaUFwxoTKLHk-_5AJJZzLWGutwLfhnNNAJMdZd0en16yjm_mfutw-v5JBgj3z2AfUHvLpaiE6CTTmTUcsA9vJvWC86CY8Q3N7lCQw76Tamg0wD1ARBWTCeXCdQi1hkLUltwxG6IJAyQO7QbtbJVVzM7o1PVrySLk8QWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAOByrFxItksumLsCMiibuaRUYP2sb4HnmlsRzI6sPFR0Y28M2en5tLlFWF3ePvwHnAnTwEeYG1p2ZAhtJ-QHmznQ4cPP0woakwjqRWiI3sBV2rot1IaDixazyLeArVwDLqCFf2sQXSHlCgOsTtbvoEOUvAoOf8Wc4H542YwvnYCfpT62soR0LJR1i8CHlChAnH8hcZ6mc4PSxG1pJfHI9shffV_kHlhyuKaoRbVc7nYbf6bCYB6cLDTMSqI_F9bZV60m1N-gtGQMqIVq5sSJGozAdUcqfnWRvtjFMTgTXqzcUyKHr4fcTyvmpAs03XMn3SuNkCaR-RV-puHboXYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i09uNyN1RKhQnifABcCoi3A54H_K0D_pmv7JtRxI4BDSbaHHtNBAb7P7T-0_IbmgmciliFEDuLJeiJjAGPbFRyoJtQY6EhtV2vsEAMKFvUrVP2ylUBIlOXf6CHRb2iY2OJkCKbuZ267mi2YwBfLGS4hQQrqKQibNhDBZ8oH5KnXKrRB9wrthHOrNKVRk3YozegMuPL01a2VS12oMG6CmyX0FqWXQURgsyZsowpsKzgzFDz23ItPaAoBPikeOTrr-ohdXi2mzKo7O2DcraPGARWpP8f71dkgCAeIfG9na54fLGKLiIsf1Tjdmewr4QcfBGtv8KCE-AMz_jFNe8kKFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V99G2gHV68_3xRNQ4yOoPzfn5PwRHqthfyA_Ea5tD7F8OGnRIWALXERUqT7VJjdqbQlr0bjTkrrHAcI2pXzw4nOiRgw96ry5SdYiPN1_86aTq1T_s9yOv5Yqo0jkIPZRy5oeS7a2zbzATz_QVO9Gr-dp4dhAlGA9e0eYxICZcoGL-y6pG2SYadiilQIn15yFnyFptyWs4lH6nRyyRReK5O0lQGRQADgyA00mdj3MUlkH-aQK96Ox-Ig_gJ0LuiwQdRLdwCIfRcIsUx66t94s1bYY7uImFdLKM-I3pgNlcuX4c6M0xmO70Fgct2rM3mjyOthC-QjxgQ3gesUg3xa7YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنوارهٔ سرباز حضرت علی اکبر(ع) بسیج
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/464518" target="_blank">📅 14:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f860ff88f2.mp4?token=MMACEcgjekQnYlyeas4mI-Ss8o5H896c2vs4Ilkbb61UMOCR4YymC0YNtymBBZsL4Re9AI6cEi63Olj4Pv52TIwizMDk0K8hVKO8sAqlu8fW5I_yoCIOtC-8vq0ytGRhXwFUPqV7_lUPd0zT-3m7DPJuXE99XX620xJ4PG3DSSBsfA8JtiTLiTH46EDhwAxcYgGmUPGSvIDAACgIzNH6mYBHR7FiLd7o2Syb7GnSEdSXwWlOMGrPXxCmTK25UZF4TLchAem3oz-BU2gfTTj6pNi5IKmq0xemsL2XWY8H9p-KIv5fe_xcdMJmZi5lmJtm_1bqKcNFgrNw5Mj1I9pfEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f860ff88f2.mp4?token=MMACEcgjekQnYlyeas4mI-Ss8o5H896c2vs4Ilkbb61UMOCR4YymC0YNtymBBZsL4Re9AI6cEi63Olj4Pv52TIwizMDk0K8hVKO8sAqlu8fW5I_yoCIOtC-8vq0ytGRhXwFUPqV7_lUPd0zT-3m7DPJuXE99XX620xJ4PG3DSSBsfA8JtiTLiTH46EDhwAxcYgGmUPGSvIDAACgIzNH6mYBHR7FiLd7o2Syb7GnSEdSXwWlOMGrPXxCmTK25UZF4TLchAem3oz-BU2gfTTj6pNi5IKmq0xemsL2XWY8H9p-KIv5fe_xcdMJmZi5lmJtm_1bqKcNFgrNw5Mj1I9pfEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکوردشکنی قیمت سوخت دامن‌گیر مردم فرانسه شد
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/464517" target="_blank">📅 14:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcb7d1c05.mp4?token=NvArU6D9sbXuCGKf1G1k8vxkzldl6AbYT5XbXE4RDet_7Y4JAKv0qF0p5lbntCVWo9hOOXpzfk4tf9FswZ4jYTzPuGiGq-4p-iN4IIa9cNmEx66hiJjEtinKrXC_nzRXjdp6p220IopfLjIHyiPhY4zoe8jqUiFLTxWNnbtB4dySqeGXNz9-RpSd09YR51Xki12zjzuI46d9uAFlGpkHbBcsUk4EUXb3PNJ1ZR6wbxYrZ9jgnrYspNUoPpXeuUnHZ3i5gOb88lv6eNmrLiXjqIj6Bhiv_YZ74ZrRsJqzSyFQqg8szTR78PXI0yIcqy1-nzVzNRrh_rqlit0nrwK9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcb7d1c05.mp4?token=NvArU6D9sbXuCGKf1G1k8vxkzldl6AbYT5XbXE4RDet_7Y4JAKv0qF0p5lbntCVWo9hOOXpzfk4tf9FswZ4jYTzPuGiGq-4p-iN4IIa9cNmEx66hiJjEtinKrXC_nzRXjdp6p220IopfLjIHyiPhY4zoe8jqUiFLTxWNnbtB4dySqeGXNz9-RpSd09YR51Xki12zjzuI46d9uAFlGpkHbBcsUk4EUXb3PNJ1ZR6wbxYrZ9jgnrYspNUoPpXeuUnHZ3i5gOb88lv6eNmrLiXjqIj6Bhiv_YZ74ZrRsJqzSyFQqg8szTR78PXI0yIcqy1-nzVzNRrh_rqlit0nrwK9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت گازوئیل بلای جان زمین‌های کشاورزان آمریکا شده است
@Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/464516" target="_blank">📅 14:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56275f475.mp4?token=HRFNfhNZIo82Xx6_V34vtyjmA9PJ0nSOaXNHGHmrvqYYNZw_4-Q9zUG-m4S0tcArRPE5-Dpu4UHm_ZFlcuL0t4t1Mx8wa7IL87Fe8oudeI-qpdSUATxsSmnxAb3wz7yd7KqBcSwhW-ndJGxXJcE7Rp9Vx4ZOk2-lf1riRXfp9ma7-DOWIlkrmhA5wXH2NQH0ekB35gU0IoDEH5NULUf-BbteTGISRz7CqlaTnlNwdRqFGbynQ1cAsLFnlhLn_29Iqp_b7g8oEUXDQ21P_WnCw8J6oRax_5GacBCecTWWWt-QfRtZvC_v9w6GHOGqV0wR0JoGgK_X2_az2UBENf60SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56275f475.mp4?token=HRFNfhNZIo82Xx6_V34vtyjmA9PJ0nSOaXNHGHmrvqYYNZw_4-Q9zUG-m4S0tcArRPE5-Dpu4UHm_ZFlcuL0t4t1Mx8wa7IL87Fe8oudeI-qpdSUATxsSmnxAb3wz7yd7KqBcSwhW-ndJGxXJcE7Rp9Vx4ZOk2-lf1riRXfp9ma7-DOWIlkrmhA5wXH2NQH0ekB35gU0IoDEH5NULUf-BbteTGISRz7CqlaTnlNwdRqFGbynQ1cAsLFnlhLn_29Iqp_b7g8oEUXDQ21P_WnCw8J6oRax_5GacBCecTWWWt-QfRtZvC_v9w6GHOGqV0wR0JoGgK_X2_az2UBENf60SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بخش‌هایی از حضور رهبر شهید انقلاب با لباس رزم در جبههٔ غرب کشور
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/464515" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bad74a70a.mp4?token=RS-HshM58jLUaotz7UXmIMEFerh4qGYda6vtVxLpncibe6RwdNpt5nz3TtqNLPSFUMD_XMAAohIhDp1uwr5pQ-RifGGyps8LkalMEeFUlFiTBt8ldziPEr7u5PS-aPQXcTl3vCkeRKP6wJ3lZOLf4x--_AqkmPAVM2VBgwHJtE--aoLwVSLEwA1h4QyYmmzY-um9U-V-P4TYookR4p5TfG4nFFtiLJx8N6To_XJ5Zk3nLUukZ1bmTrD97A93BJHSIWKEPw_GCLr4UKTFEJx4RDBz6bkT139LXtejE1U_gp7_ESLekJl6vr-gks9TeCA8EdMYi7ySNn-XxKfhBTw9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bad74a70a.mp4?token=RS-HshM58jLUaotz7UXmIMEFerh4qGYda6vtVxLpncibe6RwdNpt5nz3TtqNLPSFUMD_XMAAohIhDp1uwr5pQ-RifGGyps8LkalMEeFUlFiTBt8ldziPEr7u5PS-aPQXcTl3vCkeRKP6wJ3lZOLf4x--_AqkmPAVM2VBgwHJtE--aoLwVSLEwA1h4QyYmmzY-um9U-V-P4TYookR4p5TfG4nFFtiLJx8N6To_XJ5Zk3nLUukZ1bmTrD97A93BJHSIWKEPw_GCLr4UKTFEJx4RDBz6bkT139LXtejE1U_gp7_ESLekJl6vr-gks9TeCA8EdMYi7ySNn-XxKfhBTw9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: دانشجوهای عراقی به‌زودی به محل تحصیل خود در دانشگاه‌های ایران بازمی‌گردند.
🔹
شیطنت‌هایی توسط دشمن در جریان است تا فضا را برای دانشجویان غیرایرانی ناامن جلوه دهند؛ مشکلات پیش‌آمده در رفت‌آمد، به‌زودی برطرف خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/464514" target="_blank">📅 14:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4709c66e53.mp4?token=pYmijn4OpXnlYkZXIsiXFWHb-B9Gs6OozvoMut2MPFmuxoi4o9pyYN9FF234utd1MsRpNr7NVsiI8H26cISlu2dNhZC5KjasqmV4Y-IcRwh9cz13x_cJCVYNPLWFNg0Pl9WD40_wPJYK0WryNwERnKnhjRoXQp2QkO8iLXdB4ed1goSjXGU12k6pyOifCwTaS-hJviX18JdFEsZjZ4fcDj0pyZP0z87Gfn5DvN-Od6UyU-wnpKp8tP0_iwf97iPgkS8VZF75duOyRm3DYrNKF_pb_keo7XZ5qd2TlLRzeBlDCM9ntVhw1LpXFFzYdYKXxuM29etyECK1zzjCV-OI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4709c66e53.mp4?token=pYmijn4OpXnlYkZXIsiXFWHb-B9Gs6OozvoMut2MPFmuxoi4o9pyYN9FF234utd1MsRpNr7NVsiI8H26cISlu2dNhZC5KjasqmV4Y-IcRwh9cz13x_cJCVYNPLWFNg0Pl9WD40_wPJYK0WryNwERnKnhjRoXQp2QkO8iLXdB4ed1goSjXGU12k6pyOifCwTaS-hJviX18JdFEsZjZ4fcDj0pyZP0z87Gfn5DvN-Od6UyU-wnpKp8tP0_iwf97iPgkS8VZF75duOyRm3DYrNKF_pb_keo7XZ5qd2TlLRzeBlDCM9ntVhw1LpXFFzYdYKXxuM29etyECK1zzjCV-OI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار ارزی رئیس بانک مرکزی: امکان معاملهٔ مستقیم بین واردکنندگان و صادرکنندگان فراهم شد.
🔹
وارکنندگان می‌توانند در عرض یک روز بدون هیچ صف تخصیصی برای واردات کالاهای مواد اولیه و تولیدی تامین ارز شوند.
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/464513" target="_blank">📅 14:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bceebd13.mp4?token=PcZdXNiHC8UubsTd6NJD4nC5YbedUGG0dCETIT1LZB3iEWl6aLtRDHpyC_3Vv_sRYhOowPStlW82AY9W4oqHmGtNDfFkJnUGr6417ZlfkEvUAn5Ajxf4ZYyP72YrjxsXswSkvTyfTb0OnKbiyLhQY72-rj0qXyJsjOAPVWufaYRXkFh643TSvosCM7iXzWHEnmUMinZahLnnISqP-8Xun3n0vd4XYXQ6hdK_5PSsEKTEmA9wtgsNZQ0Hw_SDKL7SgJZbCIoEQ84aXH-suaThYL0DhK1kcp4eZPa7D1PXn5frUkISKHtVPvRwovVmJbki4Uq2XE9-TATzDRYTOcCIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bceebd13.mp4?token=PcZdXNiHC8UubsTd6NJD4nC5YbedUGG0dCETIT1LZB3iEWl6aLtRDHpyC_3Vv_sRYhOowPStlW82AY9W4oqHmGtNDfFkJnUGr6417ZlfkEvUAn5Ajxf4ZYyP72YrjxsXswSkvTyfTb0OnKbiyLhQY72-rj0qXyJsjOAPVWufaYRXkFh643TSvosCM7iXzWHEnmUMinZahLnnISqP-8Xun3n0vd4XYXQ6hdK_5PSsEKTEmA9wtgsNZQ0Hw_SDKL7SgJZbCIoEQ84aXH-suaThYL0DhK1kcp4eZPa7D1PXn5frUkISKHtVPvRwovVmJbki4Uq2XE9-TATzDRYTOcCIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین کارخانهٔ تولید اینورترهای صنعتی افتتاح شد
🔹
رئیس سازمان انرژی‌های تجدیدپذیر: تولید اینورترهای صنعتی در داخل، روند توسعهٔ انرژی‌های تجدیدپذیر کشور را تسریع خواهد کرد.
🔹
ظرفیت نیروگاه‌های تجدیدپذیر از ۱۰۰ مگاوات در سال، به ۱۰۰ مگاوات در هفته رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/464512" target="_blank">📅 14:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مدیرعامل تراکتور: بیرانوند فعلا بازیکن ماست
🔹
حجت کریمی: اگر سازمان نظام وظیفه اعتقاد دارد بیرانوند سرباز است، در نامه‌ای این موضوع را رسماً به باشگاه تراکتور اعلام کند؛ در غیر این‌صورت بیرانوند بازیکن تراکتور است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/464511" target="_blank">📅 14:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فردا آزادراه قم-کاشان ۲ ساعت مسدود می‌شود
🔹
رئیس پلیس راه اصفهان: آزادراه قم-کاشان و بالعکس، فردا از ساعت ۱۱ تا ۱۳ در محدوده کیلومتر ۷۵، برای نصب تجهیزات ترافیکی به‌صورت موقت مسدود می‌شود.
🔹
رانندگان برای تردد به سمت تهران می‌توانند از مسیر جایگزین اصفهان-میمه-دلیجان استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/464510" target="_blank">📅 14:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/214085d647.mp4?token=tYyYQwx6NMYkeH3wQ0QShwpfG2oNB9FZz0X_cDT0kLV-FpRPaFM-bqDWCzxLhA23VseD0A2Rs-AU9o41W8H8V6MFAIn3gV4dH98gXex-zP8_gPUmMWlu7d6V2E_bRHqsUpwEvyTq9fCCNIp-yLugOrXLzwEQEzgrauqcpHg-Y46bQkeRCjQqiPn0CoKtyNJq01jDh_gCwdVF7t7oxYu5tungjXkYPwmpdVVE9Zyo1vUv4tZ05Hmo3N-awCUodtoKCy4psRJ1indIM9RAOfup09kaMJq0zr38MO1BT0eyBgvj60tqCdl03-6vJGmzEDl25-tbuUKti1CW5uAcWrCqtIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/214085d647.mp4?token=tYyYQwx6NMYkeH3wQ0QShwpfG2oNB9FZz0X_cDT0kLV-FpRPaFM-bqDWCzxLhA23VseD0A2Rs-AU9o41W8H8V6MFAIn3gV4dH98gXex-zP8_gPUmMWlu7d6V2E_bRHqsUpwEvyTq9fCCNIp-yLugOrXLzwEQEzgrauqcpHg-Y46bQkeRCjQqiPn0CoKtyNJq01jDh_gCwdVF7t7oxYu5tungjXkYPwmpdVVE9Zyo1vUv4tZ05Hmo3N-awCUodtoKCy4psRJ1indIM9RAOfup09kaMJq0zr38MO1BT0eyBgvj60tqCdl03-6vJGmzEDl25-tbuUKti1CW5uAcWrCqtIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌های رئیس فدراسیون کبدی ایران پس از نایب قهرمانی تیم ملی در بازی‌های آسیایی
@Sportfars</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/464509" target="_blank">📅 14:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-Gnic9cCrEaaI-Agg0xeBhjdkdXUuVkjUvlWWNOVulbAoRP1GB_Tk4_48u5OY-io-vZLQcCvY0Y7hLaKZg_umNnGRgADgZy_U9MAA_fQVOd4gqH0dwJbKFLacnVUGQbfDoKca8P_noYfsWACku0bMPTWLHqarJwgntN_39bXHx-baGigxO5BHK2vWEoMDPdiktOMWRP7Gn9hpaKKIU0hjIWJzBWshYKxTpuMIp8veuC76qxrx_eR1AhXgM1NImabn1Hs4ydIlTTtBLriF0hXsla80fT7GutGH-nESgFHwlPxrQNfjh4xtHUm_c20UK9lbWSuNlxS39HE-ekklw9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ وزارت نفت اختیار هلدینگ خلیج فارس را به‌دست گرفت
🔹
نوبت دوم مجمع عمومی هلدینگ خلیج فارس امروز، با دستور انتخاب اعضای هیئت‌مدیره برگزار شد و در نهایت ۳ کرسی از ۵ کرسی هیئت‌مدیرهٔ هلدینگ خلیج فارس به وزارت نفت رسید.
🔹
۲ کرسی دیگر اصلی به تاپیکو و سهام عدالت…</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/464508" target="_blank">📅 14:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJW544hHJBGl5L0xkcoSdLxEVhJZLTCijVfAUZFStq4205eyTLVs1WXjT5ujNzb8L1MDfWarAvObdauF4FtfaOX_8oLr3cuD5J9E8cNiMdqGlWHHm2gomAsem1-8FAruMRRWgdSoumMwi2BXJrS0hzsZAfcUtkwZIDaWfViNjyLAyJV0t6AnU6HqEIRrhedMBYs5Q_yzN3JKpSeEFVTK3khxXa1F8btnzSdVZ-nD1Y5PxUpEu9bIwVyIuuoOSKuGYkEblsvLuo3aooFvQ0Ub-G6mxUs41CISJqAyH6cG5SclcZ5hgO7q4indOvHn3HvNfF_bQrzYBb2AewsjZpmCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ حوالهٔ دلار به ۱۷۰ هزار تومان رسید
نرخ‌های جدید حوالهٔ ارز در مرکز مبادله به‌شرح زیر است:
🔹
دلار: ۱۷۰،۶۲۶ تومان
🔹
یورو: ۱۹۴،۴۷۸ تومان
🔹
درهم: ۴۶،۴۶۰ تومان
🔹
یوآن: ۲۵،۴۲۰ تومان
🔹
روبل: ۲،۰۲۳ تومان
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/464507" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgvH_e4VZgPy6uJy5TedYOB_bjHUUdYYCSKpd0Dx3EZrtPi07gpnpnhBgMErB0v6CqCCHjVFSo9eKKmzf_ISvPdz2Vo7cZ3ubu_cHlVO8J3ocrT2UagVxitPqXmd-UDL64Z9i_BoGpfP04d_GII1KtsSHaIuCRC7LPiSFh1XD-2Yat_KIdHPlKZoKqWzJS4PUqBLQyqu3pzgvw6kWNyLXIs4Iw0cGctX_p7d_P5IhUX_j6JYNvLkorJgZ-qvKZTJElCBtbaN4VxPLERYXvx-UVFUJjQyTBRtAj1r7cK6yzx-CuA3u32U-SaOYZcigZSlna_qh7PQahZz8-Ce0d7OKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: چرا و برای چه باید با ترامپ دیدار کنم؟
🔹
رئیس‌جمهور در مصاحبه با الجزیره: ما دیگر به مذاکرات با واشنگتن اعتماد نداریم زیرا پس‌از هر دور مذاکره شاهد تکرار حملات و تحریم‌ها هستیم. چرا و برای چه باید با ترامپ دیدار کنم وقتی آن‌ها حتی به توافق با ما پایبند نبوده‌اند؟!
🔹
وقتی راه تجارت برای ما بسته شود، بستن تنگهٔ هرمز هم یک اقدام طبیعی است. ما برای منطقه‌مان نیازی به «حاکم» نداریم. حل بحران تنگهٔ هرمز با استفاده از زور امکان‌پذیر نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/464506" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be59c43615.mp4?token=uMsTCbrl6F6v35W8OuFsFjr1VQdgW_0hCQXlFmYKejtHtDZXSk0buBuPkRHHaT7y3ZyET1MzOKJtsv_52Lu8d0J1X7sNX_VgmT5Z2icFjKPqNrWvcUABb7vUd1F3cX-eFEI1T0G25RZLb8XApwGMiUtnTHAGXisgCe48BMPh5z9P2jaOMytYE_VIM-3OfTTwqgoQfJrQQVtNY_TDJ9NpVk8BNsYFJmHDe6CnyqbWxVlJgdCTQ6dmH0AnceykRkoZtmnaFYP4JxhoKgq_LPHcO9d99IGRaEjSBH5FOMhW-oHm4-aQ8aa0EOwOR7s7C0kP6Nfo-VOyg_hmVDUdUJPaSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be59c43615.mp4?token=uMsTCbrl6F6v35W8OuFsFjr1VQdgW_0hCQXlFmYKejtHtDZXSk0buBuPkRHHaT7y3ZyET1MzOKJtsv_52Lu8d0J1X7sNX_VgmT5Z2icFjKPqNrWvcUABb7vUd1F3cX-eFEI1T0G25RZLb8XApwGMiUtnTHAGXisgCe48BMPh5z9P2jaOMytYE_VIM-3OfTTwqgoQfJrQQVtNY_TDJ9NpVk8BNsYFJmHDe6CnyqbWxVlJgdCTQ6dmH0AnceykRkoZtmnaFYP4JxhoKgq_LPHcO9d99IGRaEjSBH5FOMhW-oHm4-aQ8aa0EOwOR7s7C0kP6Nfo-VOyg_hmVDUdUJPaSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عادی‌ترین طرفدار ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/464505" target="_blank">📅 13:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59e48c05f.mp4?token=HOjhn-Y0ZSdSkQ-hBTWg7l7YKOvOd54cnJrg4JBhEQmdpHDgwHiOHw407aWwg_8RKf0L1IFgKXg5BSBznjGkwupnDpA6k4lGoRAle3MT0Aw2hls32PFvEftmMYpUdcypM2-GJsAsNsHUY5VYmqYBdW9RIZ_CSt9VkLJTzI9uKzTsKGbb4-nzsufsJpWkuIHCzCV6HffjNXkWQAgCOFQU48D3YTBIXdVA6zqYMeodrOAMhNRw6CfxrQkXrDb5TqNfhG2nYIrk_Ra9klQq72A31yRd5mlmV3_8jcBF3UB6dy2B5CYtYjetKhv1TEPBzyN8k7AG8LJj5TmaGNcAmm7bjHrrdea2Ew3kpXe8lk_fyrqeDXinKlLT5B5ynDCpPkwl5tXEvMxuXustjkjpbBtEEP0ZGURC9xseS76oxikGUZQUvC_SVsCJF-Y8hiV3VT892kPZBB5sPiN96Z1paSoqrWwUoa7wyUv2VVkql-ilo_dqLMSKIvzvp1vu-KrUVE5zQhKCA663ZP8yWzhaTT8pgN6TykC4tN0vFMqiVvIqwnu12YWOcapsJJWF0BQ-04diBxCkCq2rKscQGRm9l6EuAIuCmWcXL4Vjf93aJPulzqqJAv5WOx5Orqxnrm9kYPTGpm7u7uGYYOGADY4EgJkApC__NLGnVT5N90gAVx2G0-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59e48c05f.mp4?token=HOjhn-Y0ZSdSkQ-hBTWg7l7YKOvOd54cnJrg4JBhEQmdpHDgwHiOHw407aWwg_8RKf0L1IFgKXg5BSBznjGkwupnDpA6k4lGoRAle3MT0Aw2hls32PFvEftmMYpUdcypM2-GJsAsNsHUY5VYmqYBdW9RIZ_CSt9VkLJTzI9uKzTsKGbb4-nzsufsJpWkuIHCzCV6HffjNXkWQAgCOFQU48D3YTBIXdVA6zqYMeodrOAMhNRw6CfxrQkXrDb5TqNfhG2nYIrk_Ra9klQq72A31yRd5mlmV3_8jcBF3UB6dy2B5CYtYjetKhv1TEPBzyN8k7AG8LJj5TmaGNcAmm7bjHrrdea2Ew3kpXe8lk_fyrqeDXinKlLT5B5ynDCpPkwl5tXEvMxuXustjkjpbBtEEP0ZGURC9xseS76oxikGUZQUvC_SVsCJF-Y8hiV3VT892kPZBB5sPiN96Z1paSoqrWwUoa7wyUv2VVkql-ilo_dqLMSKIvzvp1vu-KrUVE5zQhKCA663ZP8yWzhaTT8pgN6TykC4tN0vFMqiVvIqwnu12YWOcapsJJWF0BQ-04diBxCkCq2rKscQGRm9l6EuAIuCmWcXL4Vjf93aJPulzqqJAv5WOx5Orqxnrm9kYPTGpm7u7uGYYOGADY4EgJkApC__NLGnVT5N90gAVx2G0-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کبدی‌کاران مردان مقتدرانه راهی فینال شدند
🔹
تیم ملی کبدی مردان کشورمان در دیدار مرحلهٔ نیمه‌نهایی بازی‌های آسیایی ناگویا مقابل چین‌تایپه با نتیجهٔ ۵۹ بر ۲۱ شکست داد و راهی فینال شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/464504" target="_blank">📅 13:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyiCmjmn1x8gCPPiaNDiztZS7Upooew6PzJ6JJ_q8ONfTTNLobQa136-Dr38Om7bwJHe9L9s4r8tELpm-caMOEJb_3mcdnzLMBoewcVcPBVdnRPhhvgTE8mNIOYZPnr-cSaE9Rlvh61-aEyB96yugR4Cna5I9sB-dIMz5WGk1YRGOgeh3LBQ71Q4mbXRao0FKK70Rbz5HmR3AwWlOKKzMZz-h9ckcD4IxR7BkVLsV2sQWil-jDCj6BemK2T9btZOwOis1EtxVenzBoF_EE8Qcd3bWbh84E2HMqNgY-7RdYryRuBIuxO3z7Y9tsZVA0Qg7KpfKnhkr5DEZWaO066UTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیرکل جنبش نجبای عراق: درصورتی که پروازها ایرانی به عراق ازسرگرفته نشود مردم عراق برای اعتصاب در فرودگاه‌ها حاضر خواهند شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/464503" target="_blank">📅 13:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9y-GtcDhYSd3ClyTyuWyfZpmSBV7-KxQ9ScwpTmKQczq3gDA9Iz4KvEf1uY5TIJzw2H1TFCFRerZLrMaJsBdywi8lz-s3oom8YHv97UwwLiqzqJ8R9F9pQGfK5woK1vZ2JaBzClYYovj6pD1rucMJZIRiNgsjm8tVaR42leh4Qz_f0Ps0_xFm7UYysdAbWrVKoh6k74R1ebFLYcHsz9vLHscQNudTnaGDJgaqyhVLzLgbl_irU7Iig-O26jcWIJ55vZTAebHSlUifes6zeUHIeqeqUM81rN_4fNQgexl3m4viDFj3SR9fTLr5fAw_0rBUnZrwzWxfnyeds5VPk3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: تورم نقطه‌به‌نقطه بعد از ۱۵ ماه کاهشی شد
🔹
باوجود تورم ماهانه حدود ۴ درصد، اقدامات بانک مرکزی برای کنترل رشد نقدینگی باعث کاهش شتاب تورم شده است.
🔹
تورم نقطه‌به‌نقطه نیز پس از ۱۵ ماه روند افزایشی، از ۸۴.۴ درصد در مرداد به ۸۳.۸ درصد در شهریور کاهش یافت.
🔹
اگرچه کاهش انجام گرفته، اندک است ولی نفس کاهشی‌شدن روند تورم نقطه‌ای، بسیار مهم است.
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/464502" target="_blank">📅 13:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLdoFploPS_K0nyPVKUnaRRtR_nqbsBJJqyFE7e5PEaabCUMI0Ygsw8mGz28iXovH_eOFLecB-jn61xFI6_BEWSrk33uO_029Km9qwOqh8E6AoEF4JxLglvUitfJdY5yYY7uO3Wcd4ABQYW_pBN68mrv7d_a7MKaKUA7CjmFJGWHJi9tNs4iymKqtLNudWh-HEhOaHAfSe4Oi1-I-OrguWcPawIS05ZUVn0zSrtzdAhla5FETAyfO0iD0fKRemU69TJLTaBCzwmPmM7mmIZfE4xKf31FRZKub0L6HUArIqxRy375SGoFpa_9v1c7XVkqQ18UJ5OLdT1fJuWx0-Mpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنهایی ریاض؛ عربستان به کمک فرانسه چشم دوخت
🔹
در شرایطی که عربستان با تشدید حملات و تهدید علیه زیرساخت‌های حیاتی و انرژی خود روبه‌روست، ریاض برای تقویت دفاع از این تأسیسات به شرکای اروپایی روی آورده و فرانسه با اعزام نیرو، رادار و سامانه‌های دفاعی برای حفاظت…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/464501" target="_blank">📅 13:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4-O49sePCOEmAUoahogmolhrJaMJ5holfCmwtJ9VOGii60S5IVCwn4bx_S8TLrRrKtpXrtCV32Hs_IvNoeHTVhriWj8D-KiYMS57nuSQ8KoMH-isko-py6ZB2OfYPEhOlVbdU56jMnRidqTdFg4Y4ROvcGVyLDKAETxCdH1o0zyruvqBRzL6i19vDk2F_JWNKTYRia9UwbbVnrnekLSZFoue2JMtzqBWAq8y_hjcBH3KNcv-ZtkiTItbtRxfdxqy2obs1k70QWST68M8MX_6V8eO2yiVZHbxIs1hqJNw_EqnQKwvrq1XCZU58UURJdEhxh9XiJ6zqEurMnvddr_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_FDvVbjvenEnmb91-02e-qDS2auk72R4ZU9gNmV7a-Ch21Ix3FO7zKykaqJG3YZ7m74MmfrhYoipY_Og6w0unOI4A07Jp89J8rl6AONpZ0_KHs4nnjIIFbSzurn0FTiQAGM3lVtsvGj_6hzUg8ewfkDNQtXMdDNB9kEfECEW71PHrDMCB_x114Gc_PP9oD1Yh0FG9ynUK5VUMySZvEVKhRJ2S7QBI_byxj_LgrTIHSgG-CKUxttOKKKLH22BVMce_K6sX2c4An6CheiXpS5x6TAZ9AGPWSr_mCofSGDDP4BJhKcbYYetJ5ewSrHLPcQlNwaW0Eo6n6JlzRQBONdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lv6qYM5p7RK24YfDVxA0LfLPU-89R3pEefiXlYxWKGnYwyLkOIrYuP-fs7a8_V8PtoJo1K6TfYiym07N7vFi3cdcw6jJuCL-C6B0GocZ_u9wum7o2C1I1lGpR8qBtwzWbJQUcrz_mg5KlAQED9GMJjUQEW3YWfSnSbjp3c35XHr2hRIpaSEvvHnx3AqOlNBIlfcFVp9YwI3Rjuqmq4H83evEFVLC7Jigv8URk2y92HEMIecEqMDziyP4ZHNkIHnbqr-sEq1l8G55u-xKP2DYG3dtzChg3-Cgy0IKajPsS7mxNxAhw-StNOBDJiJ5-iD0IG39S5o1H2ESwU4tKTjbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CR90G_4rZzG_n3qTAd5FJPnYw1Lj-tplTZRKqHgome0r3YoaAFn5tOBJZ5l6YYUltyUq0exMHOEDmXKJ0V_xc2pmTMam08w7XfaObOWnYLs3srYOittdom-LIv7LsnQiYgZvnUrIyFn8RZ2DuOqdINCEdpvI1Oee7A_Nzw32MI2vr5_9zVHlQlcjNftSK1A4ie67OfI8gz3gR2uZFlDPYkO-LH9oXmjhMqCwzF3CWhMv6zzVv2X44kLodLuMBqzmaZGhggXWKG8fLfDDyw9YhekESvrxyA1S1h4Y6dNKwhGrSt1HKF5GJgWQrNSnr6DXlWJcrSCtcSH78q2kH4TjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9_g_gsnme1OUxGdMYoFTGI9xt90wod9-AsdLtcs66VGQalsj_UUhb8pAFieRaIIamclkYiTQsjiGVnBgpmysM_sC_6qvzKTeN24EFOhK9yYoMLJYbSBEcuJERic_rYl7vfXl8DtDM14U-m9nDoTNGkjWaBYfvlwH8T-j3S1FxgHY_mERW7P8p2X7pRDCLhXPJ-OagPaVmsjzeDF383ZuZWDcO6vtYOMRJk8D5jHbKXdUfirF09YPjQY-e7ndJBaEKVrIT_NXZPLnSQDnDSYII8nmb6xMuMbeWxH0SW8czCgJqK16CYelyvXsno2GEQU4CxKf0R4qY7ePK3lpOf-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sonMaWya62mf1ToAVw3sRQzst_oS_Y3MNr004Bvu5FhgRitL1yhSVwx3ibA-Ky4Xu70uYwFlVrIaTfXSUgLQCtKwotY4O8hkcrEX8cPOx1ghcHPF2Gu7oNsANvzRlB6LYJxrDU7OyNaaTvmQBWVlbxeqL8HFIzFfC6CRImJx_69jqbgMRMmHVd-ZlneKo934oRlvwsEnGo27If-OtWf5GDOgS2ZiD-9NciqAyy4il18c_p8UkSi6f2XGGxUFdNVsMCP7H6gtqKqs8SKiiPbfM-XGS_OkQ89CCtwPnzxe-izjtxkvGDi4kiSwlJrk8itmxvIw5KWZoWsxNoWVON9z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWjGCMZrqu_vd89eRNKMDu9Ou6lFw23i_KmqI2jlgVl3DNg6YDX-U16rZrTNl_emUvc4Ud1izqP_8ckriIzyiUifRkFeVc_1y6ae6nWtUMVb8D7QB9-qRkN1Fjpd91fnqDedo5AA1wRm4tPCCngHMBHRNdb39m_E9p4iomqRy2A5VKo_Hv0dZlzcTv0pDg_1bPuZ7QsEbeREUsUppbDu3W7uW9FxgKh41F5jQ3UIrIwPsA_xZCL0mAiQ6kRpmhXyOY0Tb5ZGq7R6ABA1AE5_o_VvRYi67b6FH2zau09OlTkXzoGpSbqnAXL-j3kMt56ziamrxK3lZdFSUFp_YxEAEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع باشکوه پیکر شهید «احمدرضا محمدرضایی» در بوشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/464494" target="_blank">📅 13:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464493">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb527df92e.mp4?token=lCI0Rl4fAaIkheF3Ty7i-qXUgl08donRzHhMvUPsXKsFVjKwyDNGSCClqFbOuSmTPQJVgQLj5hP40vgOUPjAgyHOD-gsUYhijrFtnhUb6UhpaHb0rvqKGFrIbBeRRRvo54qnDEtgWVKoCGCkJDQvMHfCL8y685SQvs-lHutfqU-imhteBQkFRVaeImxU0I6vNldsDW92NZSv4jFlDb8e_kQkTSziS5x7NsRy3f5wZ0JETf0uQ8NQmd9CxHRsxzK2taA3f0XwX4NAmMXLQ0xwz0cbHByBeN11B2GVoVAk3xfwtH2YwG20NQ7qXaz3ncvCKlH6ajQ3tKsRlS5yozQayw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb527df92e.mp4?token=lCI0Rl4fAaIkheF3Ty7i-qXUgl08donRzHhMvUPsXKsFVjKwyDNGSCClqFbOuSmTPQJVgQLj5hP40vgOUPjAgyHOD-gsUYhijrFtnhUb6UhpaHb0rvqKGFrIbBeRRRvo54qnDEtgWVKoCGCkJDQvMHfCL8y685SQvs-lHutfqU-imhteBQkFRVaeImxU0I6vNldsDW92NZSv4jFlDb8e_kQkTSziS5x7NsRy3f5wZ0JETf0uQ8NQmd9CxHRsxzK2taA3f0XwX4NAmMXLQ0xwz0cbHByBeN11B2GVoVAk3xfwtH2YwG20NQ7qXaz3ncvCKlH6ajQ3tKsRlS5yozQayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوشاد عالمیان به مرحلهٔ یک‌هشتم نهایی تنیس روی میز مسابقات آسیایی ناگویا رسید.  @Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/464493" target="_blank">📅 12:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464492">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1XOZlyrjx0h1sJ3C9FRMxpgcmtkXJ00hAO5eGH79e-xtqfAG4crpvRQjGMAx_tDiH1kZNfhqd-VTjViLrKYoAjQQr6JjWumFeqGMUcRYNWEi7WUiwAHrly3zEmVx92QCCO88gDdeULHi5qMN9LcCnbDq1ImCF-sPUEe6IQdu69AeibB3e3ToSPSjWfD7HSEK8IW9xwoyECbA_m116aqvGsv_wrzBUpX9ShZeM4OHMIR4hm6YdQgwkOx5rw5-kzidS1zjblOl8fY7xqKyf9WrKatZJ6JTVBR7Hi5ss_1FhSiRHDK6hXqGcteuCH1kY3dHJAhyKm8wXAJJ1Ie0RQIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراستی‌ها زیر تیغ افشاگری؛ معیار، بازگشت پول نفت است
🔹
در روزهای اخیر افشاگری‌های متقابل دربارهٔ تراستی‌ها بالا گرفته و این پرونده را به حاشیه‌های سیاسی و رسانه‌ای کشانده است.
🔹
تراستی‌ها در شرایط تحریم برای فروش نفت و انتقال درآمدهای آن از مسیرهای غیرمستقیم شکل گرفتند، اما ادامه فعالیت آن‌ها موضوعاتی مانند کارمزد، رسوب منابع، ریسک مسدودشدن حساب‌ها و نحوهٔ تسویهٔ درآمدها را مطرح کرده است.
🔹
برای سنجش عملکرد هر تراستی کافی است مشخص شود چه میزان نفت تحویل گرفته، ارزش آن چقدر بوده و چه مقدار از درآمد حاصل را به کشور بازگردانده است.
🔹
در این بررسی، زمان تسویه، هزینه‌های انتقال، کارمزد و شرایط تحریم نیز باید در نظر گرفته شود؛ بنابراین افشاگری‌های رسانه‌ای نباید جای حساب‌رسی دقیق را بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/464492" target="_blank">📅 12:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsHan2uxxaRDsbN850qzgyT707Oa9O_uGKoyrZAtz4x_DoC6FgwygT9s7mroCLCdjI5T4UGF4RRrkvbGWhSTx2vhFtkEHSS8xsdq6jkurthabFw__fRG25cxpv8g42zdWLyk0mZpmVJZvZ0S3fM-huVsaXvkcbdk6woVjBksh07mEG6B1egl6Vydf2SVHBFzQZriwr3cFditsi9a4jJS0OaRml3nMap4_WCTFrG4ES_WGY-QhDrFZAAASTV8Rzhilesm4Lh3ZY_tOwmqwlfdvf4Zp934Nsi63ARcLXayvYPP_GfbKnkUQTfsdI-8FaVLYuecTtg6eHiZZy4vb-5E7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس صد هزار واحد ریخت
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۱۰۴ هزار واحدی به ۷ میلیون و ۱۵۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/464490" target="_blank">📅 12:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464489">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e15321a38.mp4?token=D8pOTbsKOlq49ojhhjkpX8q7Np_QlMsOa6OQW2C4uZ3sLSX_VtmMWPn61KnScGMgl2sxpDyJBSOy75vZAOmYA4FnkIX3lNDQqxcvFqDWmMzT6OdNa1-iEIRqTVivfUJ2fNCuETv3PTnFe6WZVpobzCZjUBXzC-VwX_K7wM4udvu7pUf3NO4Z1g09FMVSitrE7XNTj6O37RUcO6Relkn6h5sicgdLxjTcnW-I6pJXVG_1R4ZQy4h8xSscy9cbJoqnjL1bS6ULvRSzSGTxYbJmsrM0jPfV_WGY1JwsYdswj3u4k425qHgLjPKy4B_TUHOFTOlIrzL3Gp1I2tnRYvpzBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e15321a38.mp4?token=D8pOTbsKOlq49ojhhjkpX8q7Np_QlMsOa6OQW2C4uZ3sLSX_VtmMWPn61KnScGMgl2sxpDyJBSOy75vZAOmYA4FnkIX3lNDQqxcvFqDWmMzT6OdNa1-iEIRqTVivfUJ2fNCuETv3PTnFe6WZVpobzCZjUBXzC-VwX_K7wM4udvu7pUf3NO4Z1g09FMVSitrE7XNTj6O37RUcO6Relkn6h5sicgdLxjTcnW-I6pJXVG_1R4ZQy4h8xSscy9cbJoqnjL1bS6ULvRSzSGTxYbJmsrM0jPfV_WGY1JwsYdswj3u4k425qHgLjPKy4B_TUHOFTOlIrzL3Gp1I2tnRYvpzBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلبان‌های ایرانی چگونه صدام را نقره‌داغ کردند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/464489" target="_blank">📅 12:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464488">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pd4cWMLnK900eXnKt6ZZpXHNkD0MKqDF1RYMjiwSaRApr53Gi05CYaVZDf1P_s7-1Prnw12kHtmwd4mnIMof_uaQ6ZssIuwva4iixnIEoBo1faBVThEff7e-_wSRWPOoZZ_E7f0hAa95tMa29cd5hNkx_ieQx2ml1ITuo8Tbb7dXZfMV-yAFMVDJSAxQFrtl97_SSPlQwqG-y394cXPuUiKzTcTkpJgs3cgjK6-5blKfjXKf5iccYjmBy7DSu7UYXhBnc_zZjT4bSlSPqKvcVNArEYU7xg0YwGdrbn_dVXraa954o9vKHkjLBcda7GIexJDKKLnqWoBoB00zx9T2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای عبدی پس از فاجعه در ناگویا
🔹
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد.
🔸
تیم ملی فوتبال امید در آخرین دیدار مرحلۀ گروهی با شکست سنگین ۴ بر…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/464488" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnazBk5Z1N3fCPfaIqpPhLmb17kq9-dwrfGUw1NIb3p_51V1JJNOKMDGNR3_E1J7-4dkTzdHY_8_qcHBb1mhC8XSF4-hIx4cHIyHYw9LyCBQ9JECfG6VF9oy5hV4R12EZ7QhH7HEoO8stoOIXRjCxAPym69OlPuoN1sEzWoD7nJfNX16d9oZYgFEIKKFNDOZ4EWDawiqGCYieeUsHVElDmP7h9dljfNs3zhY761RN-DPJFsaEkA-IgA0zsKz3lqpBUv43NH4mdBKgvEHDPNQxg8VnKq9SbVjsP0JNVC3U8vvulWfqnTdNEmeLhg9C_bcDYNB0I4zM3N4LL9Fv3tc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبض سوخت چینی‌ها سنگین شد
🔹
براساس سازوکار قیمت‌گذاری سوخت چین مصوب ۲۰۱۶، افزایش قیمت بنزین باید ۸۳۰ یوان و گازوئیل ۸۰۰ یوان به ازای هر تن می‌بود؛ اما دولت چین برای کاهش فشار بر مصرف‌کنندگان، افزایش را محدود کرد.
🔹
با این افزایش، قیمت بنزین در چین نسبت به آخرین نرخ پیش از آغاز جنگ آمریکا و اسرائیل علیه ایران، ۲۴ درصد افزایش یافته است.
🔹
قیمت گازوئیل نیز به ۳۸۵ یوان به ازای هر تن افزایش یافته که نشان‌دهنده رشد ۲۶ درصدی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/464487" target="_blank">📅 12:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464486">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/465672a0b4.mp4?token=Z5tW97gQ16UAMBcb-xC5-7-N0P6Ca9zKbVVpVN4SSdpqub8DjhS7GYk2pgTaBIjAAWO2FYub3bX-5csLa44OWnubtB2WCnyq9ewJ6WTOUHov4c0yvAnZ-CBNQ6qq2vBn8gGKwzx-RLUlTpIRxZ65Pxx11TzP4hDCEsbDJ8rGDJ94lLdM5mIFSYBQuxjg0lvqNjkzr_jrJ9g0U4KKuxeRBiz3fyOofR9ctur-qmUgfSyWmNY7acE2AnTRqSRAR5oHBew6FYJ3QW_ThRSoSZ7v3QWvQTUc7BitVSu4jtD9DBDWmhN1m25g1k3kg2Ii1TChk5MGYPAwN2QMk97-cpJvbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/465672a0b4.mp4?token=Z5tW97gQ16UAMBcb-xC5-7-N0P6Ca9zKbVVpVN4SSdpqub8DjhS7GYk2pgTaBIjAAWO2FYub3bX-5csLa44OWnubtB2WCnyq9ewJ6WTOUHov4c0yvAnZ-CBNQ6qq2vBn8gGKwzx-RLUlTpIRxZ65Pxx11TzP4hDCEsbDJ8rGDJ94lLdM5mIFSYBQuxjg0lvqNjkzr_jrJ9g0U4KKuxeRBiz3fyOofR9ctur-qmUgfSyWmNY7acE2AnTRqSRAR5oHBew6FYJ3QW_ThRSoSZ7v3QWvQTUc7BitVSu4jtD9DBDWmhN1m25g1k3kg2Ii1TChk5MGYPAwN2QMk97-cpJvbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی از بازگشت بخش عمده‌ای از ارز توسط تراستی‌ها خبر داد
🔹
پیگیر بازگشت ارز توسط صادرکنندگان غیرنفتی هم هستیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/464486" target="_blank">📅 12:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575b99c7ca.mp4?token=cWnfw4p8vR-_iqRI0LrE5A_okf5sDKAViNjcO6spK0jO-bLhTOoplGFKKsBaaQ2iAn9oXT-FWslYX6Ssv0V8JEUZqd522SHeuxduoE8q5kF3fCmMc9I3ZXVA4rNxTWErC4ma_tyUbVAdFeUMQj500qDGw6ZHaLnXsqWkbduGQv_OZqSR26qgytht04prwo4OBnyBaoF3qIKG0C-hjpvySfH5m3HERjFm9o0IMQozDgcOyNkFhfg4Gsb1OQmWvQoLq16yIkQ1U1iHlbhID-zt2GIX-sAXFBQyaOGfSjj-k685NLqDHu7n3o-ZWY4ZG7E1vU8OOT5C2GYX96fTHaySog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575b99c7ca.mp4?token=cWnfw4p8vR-_iqRI0LrE5A_okf5sDKAViNjcO6spK0jO-bLhTOoplGFKKsBaaQ2iAn9oXT-FWslYX6Ssv0V8JEUZqd522SHeuxduoE8q5kF3fCmMc9I3ZXVA4rNxTWErC4ma_tyUbVAdFeUMQj500qDGw6ZHaLnXsqWkbduGQv_OZqSR26qgytht04prwo4OBnyBaoF3qIKG0C-hjpvySfH5m3HERjFm9o0IMQozDgcOyNkFhfg4Gsb1OQmWvQoLq16yIkQ1U1iHlbhID-zt2GIX-sAXFBQyaOGfSjj-k685NLqDHu7n3o-ZWY4ZG7E1vU8OOT5C2GYX96fTHaySog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: وقتی آمریکا به آنچه تفاهم کردیم، عمل نمی‌کند، مذاکره کردن چه مشکلی را حل می‌کند؟  @Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/464485" target="_blank">📅 11:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464484">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d750122962.mp4?token=inVzIIrTM0tbHRIoihSm3-EdNCtYGi4h_melNKHVoHdK6gY0aOYgyMPBIxxYG7vO0UESPbZtI6ZlRvfmiWB8bb_BFQUDAUTblEdGUYAvD2L7Q03DNMp-PcS9HANZkhqnYPqG96RX_-bkto7XTw0VweRw-fxH0ts8uoODa1PSnm2tdGoQ5GYe48qPo4utimA5hwySsoAoCopXjSEizmbcgnKYfBPn8LD13rMyb0LEXVvSqV8vZT8RyFV5SHpFFCasATSOKGDsBuYSydOjnWKto8xMuJXWfsgfqmQkvQuhiWBZrxhK4X8oHA_-Eo93Gj1V7jltu2BxAo8frd9e90is4rD790rdeialyPA7nAb_EBrGnrkxiAC-p19FiPoymCpD7MMAlzVpOFsl9DQuKnKlHbeymuz39wpQ91PSjZK3KFTWAJPaOvnMxYjLXfOZJ2LfuFi7ZXeaTcCi3J8_iP-AWwCwltdyseehlFXcnewSTjdOpBdQb__Rcg_-MzcOEM8hrzVNSZT2PR9uxFFUT90M0Rm8Nh_QTzsE4qgjBu9USLyh5zR-xQ8s6o3sXeHeNR-xeQeryNYpEoQa81WDtOlx11s-0DH2suHPtDSYz7CJvVwu9uk1Uq1c5-BUG2EOuw-JrL0djY1RIIiJvSZ7sKETvHwRuCgkkA_iw1cv26Y-EbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d750122962.mp4?token=inVzIIrTM0tbHRIoihSm3-EdNCtYGi4h_melNKHVoHdK6gY0aOYgyMPBIxxYG7vO0UESPbZtI6ZlRvfmiWB8bb_BFQUDAUTblEdGUYAvD2L7Q03DNMp-PcS9HANZkhqnYPqG96RX_-bkto7XTw0VweRw-fxH0ts8uoODa1PSnm2tdGoQ5GYe48qPo4utimA5hwySsoAoCopXjSEizmbcgnKYfBPn8LD13rMyb0LEXVvSqV8vZT8RyFV5SHpFFCasATSOKGDsBuYSydOjnWKto8xMuJXWfsgfqmQkvQuhiWBZrxhK4X8oHA_-Eo93Gj1V7jltu2BxAo8frd9e90is4rD790rdeialyPA7nAb_EBrGnrkxiAC-p19FiPoymCpD7MMAlzVpOFsl9DQuKnKlHbeymuz39wpQ91PSjZK3KFTWAJPaOvnMxYjLXfOZJ2LfuFi7ZXeaTcCi3J8_iP-AWwCwltdyseehlFXcnewSTjdOpBdQb__Rcg_-MzcOEM8hrzVNSZT2PR9uxFFUT90M0Rm8Nh_QTzsE4qgjBu9USLyh5zR-xQ8s6o3sXeHeNR-xeQeryNYpEoQa81WDtOlx11s-0DH2suHPtDSYz7CJvVwu9uk1Uq1c5-BUG2EOuw-JrL0djY1RIIiJvSZ7sKETvHwRuCgkkA_iw1cv26Y-EbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندۀ قرارگاه عملیاتی شهید سجاد سراوان به شهادت رسید
🔹
قرارگاه قدس نیروی زمینی سپاه: سردار سرتیپ پاسدار حسین ظریفی، فرماندۀ قرارگاه عملیاتی شهید سجاد سراوان، در جریان عملیات مقابله با تروریست‌های مزدور دشمن و در خط مقدم نبرد، جان خویش را در راه امنیت مردم…</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/464484" target="_blank">📅 11:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciQCbl-q4YgrVE1Gw68pLkyUuT6hLn48oxutp3mDZ24s-pbu-5-9vM1Y64te_P5BUNJa6PyFbzhJdYEDjo76DJabgK7p9TgG8SZ8QG5BMF-eTgqy0pizuHCo83XvZ7TQi-wjkngODxIOZxZt0NUfMhD3g04MY9FQxw3_td0CE47sZF_0Cz-3c9iPUz0Eh_xpxaJUZpPZuUbaMj_w17bhRvDOEiqx93zIZ8UP2R3hwMTDdwWUTYP1dNaHZ09J4l3-MzpHsc3Gv6x3eGBumDQekcLQiO3ZSbefM1dolGJL9Aa1d7cxj9NGeRJS7VjS7ZcymPhQ7h9NZIAI4C05p4yD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرق آسیا بی‌توجه به تحریم‌های هوایی علیه ایران
🔹
مدیرعامل شهر فرودگاهی امام خمینی(ره) اعلام کرد که  پروازهای به شرق آسیا از جمله چین، ویتنام و مالزی برقرار است.
🔹
مسئولان هوایی می‌گویند که ایرلاین‌های ایرانی در حال مذاکره برای باز کردن مسیرهای جدید هوایی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/464483" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723913721e.mp4?token=nD1tWVA9PgfjvfCwyQ7_JSAPqWfc2qh6rZNKmEZxGidd89Ss1b3SpX8NV1rODAFk84c7YNQitntSANoXqYG76w2U3b97sy5fystPuA-RH8tI6jpuLPXDZgIvlN0VkDfNvYCFaEriG6kYRjZ7Ac9_JyPiWUkukruFmRf_XXhJ_audGklMUdEQq20mUKHRXe5MHPHTsaTyR7-5mocejPIQ5SveF1Q-WXkZb_H5F5U6AfKo_zjAl_43VuVsUdE_I-XKuz5e-tEd-elFyZ46al37kFWSBpW59Ho1vW3ZVmXISQvM4CNFqGdWyeIAibLv9yEprLWc9grFz0K9Byy8VC7Fow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723913721e.mp4?token=nD1tWVA9PgfjvfCwyQ7_JSAPqWfc2qh6rZNKmEZxGidd89Ss1b3SpX8NV1rODAFk84c7YNQitntSANoXqYG76w2U3b97sy5fystPuA-RH8tI6jpuLPXDZgIvlN0VkDfNvYCFaEriG6kYRjZ7Ac9_JyPiWUkukruFmRf_XXhJ_audGklMUdEQq20mUKHRXe5MHPHTsaTyR7-5mocejPIQ5SveF1Q-WXkZb_H5F5U6AfKo_zjAl_43VuVsUdE_I-XKuz5e-tEd-elFyZ46al37kFWSBpW59Ho1vW3ZVmXISQvM4CNFqGdWyeIAibLv9yEprLWc9grFz0K9Byy8VC7Fow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های تایلند زیر آب رفت و ده‌ها هزار نفر گرفتار سیلاب شدند
🔹
بارش پیوستهٔ باران از عصر پنجشنبه تا صبح امروز در پایتخت تایلند، موجب آب‌گرفتگی جاده‌ها و تخلیهٔ اجباری برخی ساکنان شد.
🔹
براساس اعلام دولت تایلند، تا امروز بیش از ۸۴ هزار نفر در ۲۱ استان این کشور، به‌ویژه در مناطق مرکزی، تحت‌تأثیر سیل و آبگرفتگی قرار گرفته است.
🔹
تصاویر و فیلم‌های منتشرشده از این حادثه، بزرگراه‌های اصلی بانکوک را زیر آب نشان می‌دهد و رانندگان به‌دلیل بالاآمدن آب ناچار به رهاکردن خودروهای خود شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/464479" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akrPeH7neXHCccYQU_-girRf9NsoFgKSE28W9O4xmHV8mozeDV95-SjDq8eWVBew6zb3oCSiyXzRVln30nsP1OFEU4sjXqVyDyt_U2Qw6KAuEMk4bwGUbOzcKVoHabxQIWvyW3bO96CpUuRDPKboiNvRIqEragtw2tT_8WqAik4cj8O6t-38Qh-7i1ZfzI-jXDESmmy_MAHgebJmFG9DbmIM3ZlKIzc2jcRclCESsNAzSaHP8kylWIa7ZDEt4XtozOrdFBginlmoB5RBPhS2XheK0d_cGMcp4-Z2a1vDzaIWrxc8xeFqYXcJG5TyuxdBJ1iD-j9jJQtw9AWMRhWl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیدان رئال را شوکه کرد
⚽️
«وضعیت امباپه خوب نیست؛ باید به مادرید برگردد»، این اظهارات تلخ سرمربی فرانسه بعد از مصدومیت ستارۀ رئال است.
⚽️
دیدار فرانسه و ترکیه دیشب برگزار شد. امباپه گل پیروزی تیمش را به ثمر رساند اما بعد از گلزنی مصدوم شد.
⚽️
فدراسیون فوتبال فرانسه اعلام کرده امباپه از ناحیۀ تاندون زانو مصدوم شده و بازی‌های فیفادی را از دست می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/464478" target="_blank">📅 11:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSDUxNx3uc-ioKQh0hJD-4Xrcf9CGHmvys22wUWZsI6X5QC2NO6UNqjSna9FLN_XJIeghcMKbOVbBsZ3fVHsTFZndAd9F7WP0Cbi52595Yd68Nr7QO7gyoi5K7HyPzo0o9Qxhx1NYFy-aHS3K-cpUH9RFKkVDE7TbqMj77oFG_D3x5v-udSLLTtUBmV4SiEQIrDcW4oL30_wqeB0e_1zT83SOAFP3kb3X6pmgMZX3TAlpfQIvU2CUzolSgsvPaocEexPsRMLzhLPX84WsG_yoFlZrBLm8E11qszuc1eabCJkutjMbAi72Vhdo4T5mvR2ozxHSZU5XYZu70jAls0rSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvfACsnrxyzc2uc9I3cD6u0Om9bV-aHLV4Sg2aT9b2Rg9oHrvJ6fv3cBnj4zvlPYiDFyXHPqkzEGaB-tEz9GV6YzUlbQF27EINo6evbYQDPLYvU664Brjt8rL69BhkENMtVJtjDJZcaqvepIYzFEjOC2VbuGu9eNhRyFD74nK593KqZfXFdfeRnlIOS3bwZOi_-Bf2EfLj8f08ZBT-nLMjTZgNAlzeDt-7BJ3tsX_CfBhnP8VN-OSck39zuH6CBbsQQ4QwVQj2FVlc-HSsKPKVOcgMhWNE73lGgYMH2OPa16M-pgkuWJHAVtcsY_zXvogCLZ6wZHSU9aX-YyzUuXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_uJOsBTIIsh5ELUekILodiwc9PvUmt-6hAAbyKouNNTtFF0UuRk3SGMV_KizyCA2G1k-e7izYZ9BUjfCh4wz0dFgv6vXe0lqKmECtVbCWk15rs1-Uz7iDgaPCX6kdReRQxdwee93VCtsfF0uQYXsfwJl4IMBH-kfYJ6EWLy-TIwnc-oPoq22p6fbdX9I-47jkvACEUDrL2U9og10iML6ztlbUL9LAM0ROk3gWCEX-QGQOfc1HKUNw149sdLciAw7fIhZrcWQDyXpV6xU2m7aT6t4fGDsmDU7p9heuXfcFLuEScTcTUusJ_Y2EprIPYFBFe8TYsSJLe37Z6oq3EqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfw511SJl_9vAg5sHjxEeFiRI9jgWh7dzVAUs7fM7LAlDjQ30v6Y9COeKqPKFz1z64ld4C88Tz-pG00b-CMqGFYJ95JRW2zRgmTkrJisZTPrdaN6vqFXoEMCyNBaY_OCsIhU1CVkRLQC1WRWgXADOjRfhTv_KSTy-RzZDVvry18o3LGemTcvUKgDoHLdd5q0auerlMDSQuXq8wNpuwTXDTF3m308PMOj9KM1UNn0F99K37jkuGEU0XEJmtIGy0vVZkD-kY43B7Bhu_EEnU52IiRRTF6J2tN8qSATgf5XPby48xEo2aNY2gNBrpCKNCkEQ6M0UKuxhuJSw6dg9hU1fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4CwSyfIBdFe5jdLkyz7b23DWGwd2BeM0oAet3eheFcavolAT7EFO_d_4t6RqqzLWDTLLXpuxskwXOBxJM9AhhJP5ruD1iItC7X8O5C-9JghJyqRhoGw64vUyi9iFOyZJuViULFvldv4LDGw0IE_gtAoDfdS81dpm8E3AQvXyI8-_yI4DdzZRuxCiG1s61-KGIsQlGHU9yR6EsNx8-C45MaMEFDcazqSeITtDUujo9E-z5MsBbcOFQeyDvZMgHtO_8HxtQ3iI64GifaMBhQvk2TuSmgjG6ZYerZuPt2S89EfTTTDqHsLehRZPjtB-zUYKRcFi0V-uwOdjRF-VBHf6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtLP6d7Xe04nGjb09CASCFu8BwMW9D6sToeTHpiKmZazxdu2dPqylfwdexjrm3IoN0qVMUEcv2mAFVYaEyCsZfdrhxIOVI83_zXk2FHpAvXQSUIvK1Dze55Vx43t324TGLzJ2NDJ-_w5GYp637Vf-kFz5SKbGEOwKagpoz_Uar8NXzQQvo3xo9LpypMMl-rozpMr3r4sMrHrMqUE0jfO_31bkxO_75G5sRp66daqjipEm4XtGYbtl_uEt_YpdxMJozYwkvTqurnAe3vvC4UHuNw5Yz_vBbqKhIaDXDIIUGNZAwLDG_W9KV049YGyQoezaME9lSS2Xb2KfbFGmsz1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6ncRX2hieGZxFj4ConSUsQWrnQ2G3xlw3M0r0QYhhaGhL1qRavaP2z2-NW8nougbsoxmeuUL-rV2Lg7-WtR0EoatG0e2ByRTpSK6t6alLElQJXFq03lNUR1BzJyF4R_j4yMghTRVrl04hhg8nNgtzO4wLw9xg-0kndASAFp6WWHDGtZv-De75VIqic7vPJTsk4K53k9ngLX4zO5EpImeWzkeTL5rAxJ9U2X_dM38xKtAdx07SbkMggJJIhJyaxvrHgIpls_Avnv_rTjiwkRiDozHC2OZ5f7Yk3T07LX_rgaKvJ7MZ43EWwOkzruM_2RAOEhfepOSimpC6XpCImrCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
از بمب سنگرشکن GBU_27 تا شاهد و رعد
🔸
در باغ‌موزهٔ دفاع مقدس زنجان، آثاری از جنگ‌های ۸ سال دفاع مقدس تا دفاع مقدس ۱۲ روزه و دفاع مقدس ۴۰ روزه، از جمله بمب GBU-27 سنگرشکن و تجهیزات شاهد و رعد، به نمایش گذاشته شده است.
عکس:
عرفان تقی بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464471" target="_blank">📅 11:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKamd9FdqjwqgYVF4RNHN5noiNzaTIfVsbY-fQ0CEd_QdT3pxjbrSUfq3TYp4KgIeNe2u_I_d9lnENNL3E9cKU1PaJnMd1nICmNfyrIKHwFoJC4m4mRaDSbf5LO0aFcdboSL2Vv3rEdPY-LgQuloba75RbEXAol-C86d0Ot9_yP03lRbA_4j0CbVM843m0FQZ-BYS-UyPXRvec5Jc8qLrHcvqEaKwrp4RdR2fNaF233wg_cnHHWtSRkeWpC7I4aq0SPiXDWhsJ2R2XAB3tmb8Pqsrr8ASxLp5EbHAXrN4BkCtC2ufe2cV3UN6eVv3yvjQa_S1_ObOsvw7gaX_HvTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانواها گران‌فروش‌تر شدند
🔹
با وجود هشدارهای مسئولان به پایبندی نانوایان به رعایت قیمت،‌ بنابر اعلام سازمان حمایت، شهریور ماه، آن‌ها بیشترین تخلف را بین اصناف داشتند که گران‌فروشی در صدر این تخلفات قرار داشت.
🔹
۲ ماه پیش بود که دولت قیمت انواع نان را در پی اعتراضات نانوایان ۷۰ درصد گران کرد؛ با این‌شرط که قیمت را رعایت و کیفیت نان را بهتر کنند.
🔹
حال شهروندان از گرانی و بی کیفیتی نان می‌گویند، یک شهروند تهرانی می‌گوید که قیمت نان سنگک دولتی در یک نانوایی ۱۷۵۰۰ تومان در دیگری ۲۰ هزار تومان است، آنها مالیات را هم از مردم می‌گیرند.
🔹
یک مشتری دیگر می‌گوید که تعداد  دولتی پزها نسبت به آزادپزها بسیار کم است و مردم را عملا به سمت خرید نان گران‌تر سوق می‌دهند، اصلا در آزادپزها هم قاعده و اصول ندارد،‌ سنگک تا ۵۰ هزار تومان می‌فروشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/464470" target="_blank">📅 11:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=Wj7pfTtOWuCWgGQmT7WzvX6tzqBHeFGBOrVead3s1wgXIYyDivvFwH8Vb_MiFViaoJXmN2vtXe_Q_qtqAZUnwq8c3dQ14KNw226V2ep05b2mWu4bi4cDnUhgIGUBLOSdwr-iaNsgDL2LcLGYlcR8KQfMvLRFOE8jVBHAsPjPBh7ygOaqJ4bBquZoKo3GANXuf1yV2no_HG7a9XP4I8GneENp2-j_N2zy7vHEj1hQPTcSIBmAWklbRbzQKzA1Ht5wUzyoc4zTqwggaEn3eGOtViLS50f-PvkqSVDovSWX3OAXk-1o5Op6lAOMsWfO5H0Yx8zy1yEokfZZtOgxvrBdpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=Wj7pfTtOWuCWgGQmT7WzvX6tzqBHeFGBOrVead3s1wgXIYyDivvFwH8Vb_MiFViaoJXmN2vtXe_Q_qtqAZUnwq8c3dQ14KNw226V2ep05b2mWu4bi4cDnUhgIGUBLOSdwr-iaNsgDL2LcLGYlcR8KQfMvLRFOE8jVBHAsPjPBh7ygOaqJ4bBquZoKo3GANXuf1yV2no_HG7a9XP4I8GneENp2-j_N2zy7vHEj1hQPTcSIBmAWklbRbzQKzA1Ht5wUzyoc4zTqwggaEn3eGOtViLS50f-PvkqSVDovSWX3OAXk-1o5Op6lAOMsWfO5H0Yx8zy1yEokfZZtOgxvrBdpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تکمیلی: ۹ فوتی و ۵ مصدوم در برخورد اتوبوس و تریلی حمل میلگرد در محور بیرجند
🔹
هلال‌احمر خراسان جنوبی: شمار کشته‌شدگان و مصدومان حادثۀ آتش‌سوزی ناشی از برخورد اتوبوس با تریلی، به ۹ فوتی و ۵ مصدوم افزایش یافت.
🔸
این اتوبوس از مشهد به مقصد زابل، و تریلی حامل…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/464469" target="_blank">📅 10:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464468">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=CZdVB_o4s2G_YnSZSP8r4yo256aQPw2pI50Kcuja-UEV0FtxI3X50cTxM8CoT5PZtzDSqmyI3sMFvnCUN4parUGUmicGEcRR7ROeObc7t1UnhQ4zzBSAErVtoN0A6hgDgoGrQFwOwWNRBQO_nSMDmKT1Whpj86TubLQvLA8GV1zUD1cd87-CcIK4Vw_8mLtiLWiE--sSf-XUHR8e4lCxTjWwar6IufjeP2yAYYZ7Nqzbpiz7TrQUfTtn-1ENUAcyYFb8PdZW1ZbJXZyw3pLKRUqBOZ3IJRa11pXcz6gQOQxBtQUdFw5LOoXVxxgGrry3i_YI_xDwEQj5GjC-eKsKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=CZdVB_o4s2G_YnSZSP8r4yo256aQPw2pI50Kcuja-UEV0FtxI3X50cTxM8CoT5PZtzDSqmyI3sMFvnCUN4parUGUmicGEcRR7ROeObc7t1UnhQ4zzBSAErVtoN0A6hgDgoGrQFwOwWNRBQO_nSMDmKT1Whpj86TubLQvLA8GV1zUD1cd87-CcIK4Vw_8mLtiLWiE--sSf-XUHR8e4lCxTjWwar6IufjeP2yAYYZ7Nqzbpiz7TrQUfTtn-1ENUAcyYFb8PdZW1ZbJXZyw3pLKRUqBOZ3IJRa11pXcz6gQOQxBtQUdFw5LOoXVxxgGrry3i_YI_xDwEQj5GjC-eKsKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: در دیدار با رهبر انقلاب ۷ ساعت روی زمین نشسته بودیم و گفت‌گو می‌کردیم
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ خبری سی‌بی‌اس: در دیدار ۷ ساعته که خدمت رهبر معظم انقلاب بودم، ایشان هیچ جراحتی نداشت.
🔹
ما روی زمین نشسته بودیم و گفت‌گو می‌کردیم، ما چون عادت…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/464468" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464467">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL-5RQPaF9ivvPDYx0PQmiADEORG_I_JyJFPii1cXjR3weWJ74AosoSJwjVqavcBTQjRTUqtTCy-sY176yBIv6WD7hnFod5mRCh1hgpIpCvsTZoSszUfOrfmF8MZ9rVI7IlZFYs4RtWYIjjxQW7kX7YDM2uIY98ih2RBe5QBMWm3jsHQTME7NIpQ3kbWcOkLF3jMEhGGyiAytQ6adIFIfwC-yPAIwcewkAoxVUtT54UgsXRCIVSZxyND3tyfuOh1EOEM1JHn69akgOHX6KI_BQ-AFKzt3TNfzWuM16LTxrDaZsytBiirV08BsBJsFBsW32Ckpr5aGn0a6AScwr3ADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیرو دریایی سپاه: اگر تنگۀ هرمز در اختیار آمریکاست، بسم‌الله!
🔹
معاون سیاسی نیروی دریایی سپاه: ترامپ در فضاسازی رسانه‌ای خود مدعی شده که تنگۀ هرمز در اختیار آمریکاست؛ اگر چنین است، بسم‌الله. یکی از ناوهای خود را به فاصلۀ ۱۰۰ کیلومتری نزدیک کنید.
🔹
آمریکایی‌ها…</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/464467" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464466">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnABBPVzlvRvCOWmoiSLfcEZakqUYb_rg1xD-sExVHYCus0xrpXi_corGIEjQLbkLa8R_19LsPJ495HSssZhgpplVeXSI6e7s6xIfqtljltM6JULyva3EFyI9a9exdFD8jyNiADjYvHeWhtzrLHdyxxdm6zj_sx_s9DLH-giqsjWZmDWlyao4GpKmAswrI38MLjdWkpole6RVcoyrtjtC59QkWfhbclD7O5g-OuEzoNMgOYRhjiIQu8-hTP1uj6QBfgkwliIGj6qFR_t6M05TrWc-sgLnpU41sn9T0dJdmzuCHRTA8szAfw2dnk316WZS4pHLzeVv-KFZdsOmKqEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش بغداد برای حفظ مسیر پروازی ایران شروع شد
🔹
دولت عراق برای از سرگیری پروازهای ایران، با آمریکا وارد مذاکره شد تا فرودگاه‌های این کشور از تحریم‌ها کنار گذاشته شوند.
🔹
براساس بیانیهٔ دفتر رسانه‌ای نخست‌وزیر عراق، هدف از این گفت‌وگو «فراهم شدن امکان از سرگیری پروازها به دلایل انسانی، شامل درمان، تحصیل، زیارت‌های دینی و منافع غیرنظامیان» عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/464466" target="_blank">📅 10:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464465">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTOb9zir82UBV2SfNYiuNKF3QXCy8D10aJ2XZfwdsYddncWGr0W1CWmX0OZO_3yXZheSbEtvDgQ98ux8Sk5IaIxpffwjfiX2coREoGXOhZO44VVhYdVC36P7HKd3lOu7kxiFa650i9BFw7UL8FXYxXppO-iVXXPLJV7iY9UfH-m1o4YCZdF9paUpCJr_NeisTuz62T49MCCl0tRdUhKAtfiYwcTdd02AeAlRCGAv9_Uyi_enLFuxkyu7ToXdrVI4OcuEv1-UhTVTiWgLV22a6oDH3tHxDda9_GayvuLDy1g4CcQyYzZ4LdftMdAqTmjcqB_4vQcVUjT7ntvi0Yx-7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: سرباز جوان ایرانی جان‌فدای ناموس و وطن شد
🔹
پیام رئیس ستادکل نیروهای مسلح به‌مناسبت روز سرباز: سربازان عزیز با شجاعتی کم‌نظیر در میدان نبرد جنگ تحمیلی دوم و سوم حاضر شدند و با تقدیم جان خود، از جان و مال و ناموس ملت، آرمان‌های بلند انقلاب اسلامی و میهن عزیز دفاع کردند.
🔹
حضور مؤثر و مقتدرانه جوانان سرباز، موجب ارتقاء چشمگیر توان دفاعی، امنیتی و انتظامی کشور و افزایش عمق بازدارندگی ملی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/464465" target="_blank">📅 10:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464464">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3c43e28a.mp4?token=USUc9nwR6rubl1E7_v_XdBb7-2AfcpxpkjvzuvUrlJONjrM4F473xvBsg-qZV2d2IaFX7FPhEx-v4dJwn5BzaTSLfB4gU1Wallm7EaoneL7YlbDtO4U0Vt_KF9I6KcyJpMMcjysbbEzbNQ_igqlZb-55LCFXrj8-UIV2z5AmPRD210rNw5wpJedsJy0nlLvuPrggJTIHQcwBwEzpsX8zBmqSB7kOEi3tAtTxANKCzo-XeiD7bVJT2Jh2dStlAuVBYrpItFMEOeyXH4kYo1P_Juc-azLTFsFOIalmUrlcbWjeAD1cB-Kh5mujxw2CTlqWWN7uy7NxTftk06v2-rttJIqmvcQ4vJWJYrNHrDJ1vpD2ENPNJgNEJksRiXOl1CoqfXS-oljdT7OtU6etPDCJz0HGKEhQzICypsMgLwEEXh5nyZmLybk0hjitxAiUgZoj35Plllu5lLNwvybpHFoZYs1kGTkt52-8nZ34YhklZKC2gRmM48EZPC_AjVuBqpuPJ4ZFKKlE9bZ8wcwDE-3xXcQ22wRICe9mktAmOdsbB6fDMfThCBw7gnv0-_UaPWj0dFEMsNUy5h4_48gu3qdG_It9pStKRWlHHrylAtBsXW_UquQwBHziRbveL_Uz54vIExRmb8yM1BUybbHG1zTZEgHH4T4Eu1SRUaJorWZd7tE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3c43e28a.mp4?token=USUc9nwR6rubl1E7_v_XdBb7-2AfcpxpkjvzuvUrlJONjrM4F473xvBsg-qZV2d2IaFX7FPhEx-v4dJwn5BzaTSLfB4gU1Wallm7EaoneL7YlbDtO4U0Vt_KF9I6KcyJpMMcjysbbEzbNQ_igqlZb-55LCFXrj8-UIV2z5AmPRD210rNw5wpJedsJy0nlLvuPrggJTIHQcwBwEzpsX8zBmqSB7kOEi3tAtTxANKCzo-XeiD7bVJT2Jh2dStlAuVBYrpItFMEOeyXH4kYo1P_Juc-azLTFsFOIalmUrlcbWjeAD1cB-Kh5mujxw2CTlqWWN7uy7NxTftk06v2-rttJIqmvcQ4vJWJYrNHrDJ1vpD2ENPNJgNEJksRiXOl1CoqfXS-oljdT7OtU6etPDCJz0HGKEhQzICypsMgLwEEXh5nyZmLybk0hjitxAiUgZoj35Plllu5lLNwvybpHFoZYs1kGTkt52-8nZ34YhklZKC2gRmM48EZPC_AjVuBqpuPJ4ZFKKlE9bZ8wcwDE-3xXcQ22wRICe9mktAmOdsbB6fDMfThCBw7gnv0-_UaPWj0dFEMsNUy5h4_48gu3qdG_It9pStKRWlHHrylAtBsXW_UquQwBHziRbveL_Uz54vIExRmb8yM1BUybbHG1zTZEgHH4T4Eu1SRUaJorWZd7tE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌بازی مردها از روزهای سربازی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/464464" target="_blank">📅 10:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464463">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac74ce7bff.mp4?token=nQ_BshpGh9U0Bo8nZmCRlOTf_yRPPrJNDVQ53xIH5ygFH0gqwqvM4q9Yd_O0DHPOzMeu8Rsx-DoFpOgPmaejtqbDzPOSxoAdnhEGWkbXMrQ2kh1xWiZElTaTabgbGXge56aaYHqnlk2fmY8rZSDeYXavBouKVVTCIkluE5smkyOd-rQK84fkzPNiZPH--kb6CUPh7VQN8HjI7WpgP4c63GbhQtesJYzC6kZxNBrmcWY8qXuAxqcYXDOMr0yOUmzt8SybmyOu9Ww2tamxmneZbTRkYkG_58JCUrSqWeREjtUkEAO4uVSowMzJpgHqjjQGqAb50y74rMHzRDI7pEL_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac74ce7bff.mp4?token=nQ_BshpGh9U0Bo8nZmCRlOTf_yRPPrJNDVQ53xIH5ygFH0gqwqvM4q9Yd_O0DHPOzMeu8Rsx-DoFpOgPmaejtqbDzPOSxoAdnhEGWkbXMrQ2kh1xWiZElTaTabgbGXge56aaYHqnlk2fmY8rZSDeYXavBouKVVTCIkluE5smkyOd-rQK84fkzPNiZPH--kb6CUPh7VQN8HjI7WpgP4c63GbhQtesJYzC6kZxNBrmcWY8qXuAxqcYXDOMr0yOUmzt8SybmyOu9Ww2tamxmneZbTRkYkG_58JCUrSqWeREjtUkEAO4uVSowMzJpgHqjjQGqAb50y74rMHzRDI7pEL_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: آمادۀ گفت‌وگو هستیم، اما قلدری را نمی‌پذیریم
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ خبری سی‌بی‌اس: ما هیچ‌گاه به‌دنبال سلاح هسته‌ای نبودیم. آنها رهبری را شهید کردند که براساس فتوای ایشان، ساخت سلاح هسته‌ای حرام است.
🔹
از نظر اعتقادی و نه از نظر قانونی، بدین…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464463" target="_blank">📅 10:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464462">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMf9i4Z3b3bPh7emeZcCclBskXMYXFE_PYfa98donRQHvHJKxSOJ8FVUPtwz_c8jCdCiPcU7tmqoj8o0PaQDV-wusE7AfFfuWuWrG3UB1IjitL8PbwEyf6hMO-nISKCJJry35s8K5HWht4p9XK_q3MrDJHLSPSMTKCuiQf9huzNt1Zuv12Ro-U3U0N6blEdpIYZbK7ezUXrPzZdxSG_3C0Uz5HhPWvBbWwNvbFg6snQ3wSMFvStPYWe6BXulf8sTyaEBTrbvniTyN02JIXXoQvmktX0Hju-xXMCh5WoWsOL1HiakBrMwCQLuDjKzFyWDmYk-KI2x-khTonXJCy6TAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیت افت صادرات نفت ایران به چین
🔹
بررسی روند صادرات نفت ایران به چین نشان می‌دهد حجم محموله‌های نفتی ایران در آب‌های نزدیک به چین کاهش قابل‌توجهی داشته و موجودی نفت ایران روی آب در این منطقه به حدود ۲۰ میلیون بشکه رسیده است.
🔹
بر همین اساس، میزان واردات نفت ایران از سوی چین که در مقاطعی بین یک تا ۱.۵ میلیون بشکه در روز برآورد می‌شد، اکنون در برخی محاسبات به کمتر از ۱۰۰ هزار بشکه در روز رسیده است.
🔹
کاهشی که می‌تواند بیش از آن‌که ناشی از افت تقاضای چین باشد، به کاهش عرضه و تغییر الگوی فروش نفت ایران مربوط باشد.
🔹
باتوجه به تغییر مسیرهای انتقال، شیوه عرضه و آرایش فروش نفت ایران پس از جنگ، به‌دلیل مشخص نبودن کامل این «آرایش جنگی»، امکان استخراج رقم دقیق صادرات وجود ندارد.
🔹
درآمدهای نفتی دولت هم نشان می‌دهد بیش از ۱۰۰ درصد منابع پیش‌بینی‌شده در بودجهٔ ۱۴۰۵ در نیمهٔ اول سال محقق شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/464462" target="_blank">📅 10:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464461">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVtszxlFhdtAWC5ZOsr6fdyjp0E0EDKxiFmFmjMEIF1i-F9nLkoQd_VyyyQ89pHVDNtczt7637Al3bi6uDahH2PX3_2bTjQ9ai0W_APUc4txQlzOI7Mgcgw--1Tj3Z4ZESai_xBv7VvvED20JQbZ8XyUETbM7S4h5eARh-_GPtVcV7n3WoFsd7gV7PFpKu7ojYG1uWPX-7tIC2jWJW6XPvqy4GKMFr9xVDf6MQtaoJzneJR6yCsh2toFhVvDOrrx8BiSNWr19BoujyJBkKQwA5x9V7OmE3CeIp2Ky2rzsfJojVvFPIUPo9vYGrpcCitcLhtWhPClInGUWvmsi0b_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔶
شستا پیشرو در سرمایه‌گذاری و خلق ارزش در اقتصاد ایران
در میان ۲۷ هلدینگ بورسی کشور به لحاظ شاخص بازدهی از ابتدای امسال تاکنون، عملکرد شستا و هلدینگهای زیرمجموعه افتخارآفرین است.
@tappico1381</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/464461" target="_blank">📅 10:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464460">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2fMNeK1qwHubgLhfjLmK44UxQ3tckMccxrD4j-j6YjM3dRjH1rDO-XHfRmTGVOmPB0rJm7O3iwfGBzOF6FmU_oUKY9hfR2iHCci5icV5WeyW9s0gB1mksQpSiI3Ml42zmXhDWf5i3LeKx-_-VaaGqxa6v8cQPNG14MlUBmAzgIqADG9sLSY8Ud9HmTwNl2Sux9xaNonrmd5CFNdYlV-7o5L4on5ymdUX9RlDs29aOhmSr6XUvxteBqtrnQtx0i8iTl7p-y8ZQzWmwjvKL3X3fhj8NFxvUmso1DijFjbDxHnBLpg8ZHVGXsKdlq30vh5dXE4JNbt09qJsaFABpGNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/464460" target="_blank">📅 10:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464459">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/464459" target="_blank">📅 10:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464458">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK7V6d2KmhwqWSwWbG0_nb078NV0wf3CUCdgzV0yUKA6zzQy4BEY3ryS75YbDb3OvwEHEUty5Zn6ojtD-CKornC-avxjGOe2jon2Hrlw90FFpUpDTmNN35AzC0MVztgwRnLMBg_4CXzPUr7Su7y1OKiqDykn2UWP0GzdCpSgo6cxP3tEuFV6QoGtjs18jouXsVS32XRQ0UvAJDknfBnj3fKAoaf44BERTFtsuc10QpSMzL6AMw3iM2dItTzilzKuISo-WmjfZn0e1HEscpVeIcMLkfVIZDCLm-Wf2YfmL8H7jjASYOm7TRZaPkRpn_RuFgxZtnbu9RDTd6TQkOY2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: آمادۀ گفت‌وگو هستیم، اما قلدری را نمی‌پذیریم
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ خبری سی‌بی‌اس: ما هیچ‌گاه به‌دنبال سلاح هسته‌ای نبودیم. آنها رهبری را شهید کردند که براساس فتوای ایشان، ساخت سلاح هسته‌ای حرام است.
🔹
از نظر اعتقادی و نه از نظر قانونی، بدین معنا که حتی اگر در ایران کسانی باشند که انگیزۀ ساخت سلاح هسته‌ای داشته باشند، از نظر اعتقادی حق ندارند به آن طرف حرکت کنند.
🔹
آمریکا این چنین رهبری را ترور کرد، ما در حال گفت‌وگو بودیم، تفاهم کرده بودیم؛ چرا حمله کردند؟ قصد آمریکا این نیست که مشکل حل شود بلکه می‌خواهد حکومت ما را ساقط کند. رهبر اسرائیل در سخنرانی خود می‌گوید قصدش ساقط کردن حکومت است، نه گفت‌وگو.
🔹
ما با تمام وجود گفت‌وگو می‌کنیم، اما قلدری و زوری را نمی‌پذیریم و نمی‌پذیریم که ما را به تسلیم وادار کنند. گفت‌وگو می‌کنیم، اما چرا در حین گفت‌وگو به ما حمله می‌کنند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/464458" target="_blank">📅 09:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464457">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSVaZt7T5jJaqzdrp3ta6MosUZjEsSjddzdA6Q5alYvcMuWbGLBMcfn0f1Uu-Sh82JwKXd-bsp4rTjfGRY2wQmaaivmQO87XzODc9552Dtffs-VQx_TRtstK96bu-M1xs7GVeXFBhZTs2GTbl0whQi7ouUXjm4Ur5JIjuPM6BMw5U4_BYCQWg2BXtzyy7OJ6krEw4D5nJiCA54L5MYdVbbcVxbZOnXRbN4C5q7TymvkzrmT3eTlIj8ezmfnMsSOK7cmqeh-tPK6-we3amQ1-4mptsPB66b7tUElk3swWk6S5y-vPXMkbe9DYPFxS4bO8XP7IkbGdACxOGlZrJEx1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط محاصرۀ‌ دریایی شکست
🔹
«خط محاصرۀ دریایی آمریکا شکسته و عقب‌تر از حالت اولیه رفته». این جمله اکانت Open Source INTelligence با نام مولو مانیتور است.
🔹
طبق اعلام مولومانیتور از ۲۶ روز پیش تاکنون، تصاویر هیچ یک از ناوهای هواپیمابر یو اس اس جورج اچ دبلیو بوش، یو اس اس جورج واشنگتن، یو اس اس باکسر و ناوشکن‌های کلاس آرلی برک، در تصاویر ماهواره‌ای سنتینل-۲ واقع در خط محاصره دریایی ایران یافت نمی‌شود.
🔹
براساس این اطلاعات، آمریکا تصمیم گرفته تا خارج شدن از تیررس موشک‌های ضد کشتی ایران عقب‌نشینی کند و بدین ترتیب خط محاصرۀ دریایی را که تا یک ماه پیش در خروجی خلیج عمان قرار داشت تغییر دهد.
🔸
حدود ۲۶ روز پیش اوایل ماه سپتامبر، نیروی دریایی ایران برای اولین بار موشک قاسم بصیر را آزمایش کرد که تمام دریای عرب در برد آن قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/464457" target="_blank">📅 09:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464456">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اکسپو ۲۰۲۶ گرگان؛ فرصت توسعه یا نمایش بزرگ اقتصادی؟
🔹
برگزاری رویداد اکسپو ۲۰۲۶ آسیای میانه در گرگان می‌تواند فرصتی برای تقویت ارتباطات اقتصادی گلستان با کشورهای آسیای میانه باشد؛ اما تحقق این ظرفیت نیازمند زیرساخت، برنامهٔ راهبردی و تعریف دقیق اهداف اقتصادی است.
🔹
کارشناسان معتقدند صرف گردهم‌آوردن تجار و معرفی محصولات صادراتی آن هم با هزینه‌های گزاف کافی نیست و باید مشخص شود تفاهم‌های تجاری پس‌از نمایشگاه در چه بستری به قرارداد و سرمایه‌گذاری تبدیل می‌شود. همچنین موضوعاتی مانند حمل‌ونقل، گمرک، استانداردها و زنجیرهٔ تأمین باید از پیش تعیین‌تکلیف شوند.
🔹
از سوی دیگر، گلستان و استان‌های شمالی باید از رویکرد صرفاً صادراتی عبور و به‌سمت ایجاد صنایع تبدیلی و چندملیتی، تشکیل زنجیره‌های ارزش منطقه‌ای و نقش‌آفرینی در امنیت غذایی کشورهای آسیای میانه حرکت کنند؛ در غیر این صورت، خطر آن وجود دارد که دستاوردهای اکسپو به چند تفاهم‌نامه و نمایش محصولات محدود شود.
🔹
اکنون پرسش اصلی این است که «آیا اکسپو ۲۰۲۶ می‌تواند به بستری برای سرمایه‌گذاری، تولید مشترک و توسعه پایدار اقتصادی گلستان تبدیل شود یا صرفاً به رویدادی پرزرق‌وبرق برای میزبانی از تجار خارجی بدل خواهد شد؟»
🔸
این رویداد قرار است ۲۴ تا ۲۷ آذر در نمایشگاه‌های بین‌المللی گرگان برگزار شود.
🔗
مشروح این گزارش را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/464456" target="_blank">📅 09:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464455">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZY4bmjTXw9DxO6JaDFcRVgfrRR64CZVyg0uOXXxKVBa80P1qFwsfosx6ucJLcOy3R780uezhmjw4a-VIQb0AJYugS93uf5HDGdxCGhpZIW53sRy65rrTbyyaEbo0HqolCozo71gihHzJi-NE2aDXatJXp2JxOg5re57AoeOckFnIRDGzHEYu24knkjhaWrpLvQkKatOAaG9N_gZ6Adsyu3eH98YyfUR8C-lTlbJARMwJ1d8HgbN8ECi1donP_VHAiC0F52CHuOVPArnZLveoLElu_2MeZ2tC0OnWRoFsUXQD2jSQTw-F09uwFkI1d-6Xj9lEcjKUUTLXu7rUGHRxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اثر واژگونی یک دستگاه اتوبوس در مسیر همدان به ساوه، ۱۱ نفر فوت کردند و ۲۴ نفر مصدوم شدند.
🔹
پلیس‌راه استان مرکزی علت واژگونی را «خواب‌آلودگی راننده» اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464455" target="_blank">📅 09:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464454">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boSHPOL19UAltQJU9QAQODoqUuQMKBzQZLTzNOr5XycI5yKW3h-GRH1KQLGBWpkM8b4ADVz8bT1eX7H9hDVQVzyd32-Qb47vt0hIG-xzhB_cJuJ7vGuRiYzWIZx-eAabr8s45mwcDpp8WwYQchbyhyKXMQh4XjPxAEYAv9dRCSyTD6EXKZoGliaEfN1AStfpJkoyiOsl-wnloiDRgLqCkBg0VpnbJ2u-B-0_N_FQCKoXy04JMCiADM-3FHtKqS8KACvavtNwMShu1qUdrijDJ2vR2xQViT3-xLfpZ7ioP84bSTh7ApYrCEJlXf4SVpYwAINZZhpOZPbTxz98RuiOug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختران کبدی ایران فینالیست شدند
🔹
تیم کبدی زنان در مرحلهٔ نیمه‌نهایی مقابل چین تایپه با نتیجهٔ ۲۳ بر ۱۹ پیروز شد و راهی فینال شد. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464454" target="_blank">📅 09:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464453">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6660dc271d.mp4?token=tHsb3FC7AcZq7c7bvrb7DngIdXVomh7yGOggmzk_CqFNKTlI3gApT0_vxGVF_9TyFSj4auT0wEwHYSi0q1Y3Ys8arNld6o1UHWexZcWXI7zfUIFERYI26AJKR1Xh_ClBc4VJeoCtmsEeSD4XN3PaKA_iMOl4XASNGKqp6V6lcMSQ2vPrVCUl2FdDp2kTjf8E_HUcsrLtDWOS1C1fLaKXMpTpIOhg4eduS2SVjtxKF7oZD0kZ54rbOOpS-De7wCpihd61AO_e0OPsnVpPc-gkVeUAGnQpS6vomv7Hu3jY1mfCU8THzWSz30Hzls3sbN8Bug0T2ULR9G3f_GrBKS_uWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6660dc271d.mp4?token=tHsb3FC7AcZq7c7bvrb7DngIdXVomh7yGOggmzk_CqFNKTlI3gApT0_vxGVF_9TyFSj4auT0wEwHYSi0q1Y3Ys8arNld6o1UHWexZcWXI7zfUIFERYI26AJKR1Xh_ClBc4VJeoCtmsEeSD4XN3PaKA_iMOl4XASNGKqp6V6lcMSQ2vPrVCUl2FdDp2kTjf8E_HUcsrLtDWOS1C1fLaKXMpTpIOhg4eduS2SVjtxKF7oZD0kZ54rbOOpS-De7wCpihd61AO_e0OPsnVpPc-gkVeUAGnQpS6vomv7Hu3jY1mfCU8THzWSz30Hzls3sbN8Bug0T2ULR9G3f_GrBKS_uWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آدم‌هایی که خوب می‌خوابند ممکن است آلزایمر نگیرند!
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464453" target="_blank">📅 08:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464452">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئیس‌جمهور به نیویورک سفر کرد
🔹
پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
🔹
براساس برنامۀ اعلام‌شده، سفر پزشکیان به نیویورک تا شنبه ادامه خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464452" target="_blank">📅 08:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464451">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مذاکره با آمریکا و الفبای سیاست برای آنهایی که خائن نیستند
📝
شش گزاره که برای فهمیدن‌شان نه دکترای علوم سیاسی لازم است، نه تجربه دیپلماسی!
🔹
گاهی یک مسئله آن‌قدر ساده است که توضیح‌دادنش دشوار می‌شود؛ چون آدم نمی‌داند از کدام بدیهیات باید شروع کند؛ اما ظاهراً باید شروع کرد.
🔸
یک؛ اگر کسی با شما مذاکره کرد و وسط مذاکره به شما حمله کرد، یعنی «مذاکره» به‌تنهایی مانع حمله نمی‌شود.
🔹
ساده بود؟ یک بار دیگر: مذاکره کردید؛ گفتید آماده توافق هستید. حتی گفتید حاضرید در موضوع هسته‌ای عقب‌نشینی کنید و از ۴۰۰ کیلو اورانیوم صرف‌نظر کنید.
🔹
بعد به شما حمله شد. نتیجه خیلی پیچیده نیست؛ صرف مذاکره جلوی حمله را نگرفت.
برای فهم این جمله نیازی به نظریه روابط بین‌الملل نیست.
🔹
دو؛ اگر طرف مقابل با فشار از شما امتیاز بگیرد، ممکن است دوباره فشار بیاورد.
🔹
مثلاً طرف مقابل فشار می‌آورد. شما می‌گویید برای اینکه دعوا نشود، امتیاز می‌دهیم. او می‌بیند فشار جواب داد.
🔹
حالا سؤال کلاس اول سیاست؛ دفعه بعد احتمالاً چه می‌کند؟ می‌گوید چه انسان‌های خوبی؛ دیگر فشار نمی‌آورم. یا دوباره فشار می‌آورد تا دوباره امتیاز بگیرد؟ سؤال سختی نیست.
🔸
سه؛ اگر کسی از شما می‌ترسد، باید کاری کنید بیشتر از حمله بترسد؛ نه اینکه بفهمد شما بیشتر از او از جنگ می‌ترسید.
🔹
خیلی ساده: اگر دشمن بفهمد با ترساندن شما امتیاز می‌گیرد، انگیزه‌اش برای ترساندن شما کمتر نمی‌شود، بیشتر می‌شود.
🔹
چهار؛
صلح خوب است. رفاه هم خوب است. سلامتی هم خوب است. هوای پاک هم خیلی خوب است.
اما سیاست با گفتن چیزهای خوب اداره نمی‌شود.
🔹
وقتی می‌گویید «تفاهم»، باید بگویید سر چه چیزی؟ ما چه می‌دهیم؟ او چه می‌دهد؟ چه تضمینی می‌دهد؟ اگر زیر توافق زد چه می‌شود؟ اگر دوباره حمله کرد چه؟
و مهم‌تر، آخر این امتیازدادن کجاست؟
🔹
اگر جواب این سؤال‌ها را ندارید، هنوز «راه‌حل» ارائه نکرده‌اید.
فقط چند کلمه زیبا گفته‌اید.
🔸
پنج؛ به کسی که درباره نتیجه مذاکره سؤال می‌کند نمی‌شود گفت جنگ‌طلب و بعد مسئله را حل‌شده فرض کرد.
🔹
فرض کنید کسی می‌پرسد «خیلی خوب؛ مذاکره کنیم. اگر دوباره زدند چه؟» پاسخ این نیست: «شما جنگ‌طلبید.»
🔹
می‌پرسد، چه تضمینی داریم؟ پاسخ: شما مخالف صلحید. می‌پرسد: چه چیزی بدهیم که دیگر چیزی نخواهند؟ پاسخ: مردم جنگ نمی‌خواهند. بله؛ مردم جنگ نمی‌خواهند. حالا جواب سؤال چیست؟
🔹
شش؛ اختلاف انداختن داخل کشور، دشمن را ضعیف نمی‌کند.
🔹
کشور «الف» می‌خواهد به کشور «ب» فشار بیاورد. کشور «ب» متحد است. برای کشور «الف» کار سخت‌تر است. حالا کشور «ب» دچار اختلاف می‌شود.
🔹
یک گروه به گروه دیگر می‌گوید شما کشور را به جنگ می‌برید. آن گروه جواب می‌دهد شما دارید کشور را تسلیم می‌کنید. جامعه دوپاره می‌شود. حالا کشور «الف» قوی‌تر شده یا ضعیف‌تر؟ باز هم سؤال سختی نیست.
📝
حالا همه درس‌ها را کنار هم بگذاریم:
فشار آورد، امتیاز خواست، مذاکره شد، باز هم حمله کرد.
🔹
حالا نسخه پیشنهادی چیست؟ مذاکره بیشتر. اگر دوباره فشار آورد؟ تفاهم بیشتر. اگر دوباره تهدید کرد؟ نگذاریم جنگ شود. اگر پرسیدیم چگونه؟ صلح خوب است.
🔹
اگر پرسیدیم چه تضمینی دارید؟ سکوت. اگر پرسیدیم نقطه پایان امتیازها کجاست؟ سکوت.
🔹
اگر پرسیدیم چرا طرف مقابل باید از ابزاری که برایش نتیجه داده دست بردارد؟ باز هم سکوت.
🔸
اینجاست که بحث دیگر بر سر «صلح‌طلبی» و «جنگ‌طلبی» نیست. بحث بر سر یک سؤال بسیار ابتدایی است:
آیا واقعاً سازوکار فشار را نمی‌بینید؟
🔸
عنوان این نوشته عامدانه قید دارد: «آنهایی که خائن نیستند». چون اگر فرض را بر حسن نیت بگذاریم و فرض کنیم کسی عامدانه در مسیر منافع دشمن حرکت نمی‌کند، آن‌وقت یک پرسش دیگر باقی می‌ماند:
⚠️
کسی که دوبار نتیجه یک مسیر را دیده، اما برای بار سوم همان مسیر را با همان استدلال پیشنهاد می‌کند، دقیقاً چه چیزی را هنوز متوجه نشده است؟
🔗
شرح کامل را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464451" target="_blank">📅 07:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464450">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هوای تهران ناسالم شد
🔹
شاخص کیفیت هوای امروز پایتخت روی عدد ۱۱۲ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464450" target="_blank">📅 07:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
محیطی‌زاده: قبل از بازی کفش‌هایم را بررسی، و مجوز را صادر کرده بودند
🔹
ملی‌پوش هفتگانۀ ایران، فاطمه محیطی‌زاده پس از حذف از رقابت‌های بازی‌های آسیایی ناگویا به دلیل نوع کفش‌هایش، نسبت به این تصمیم اعتراض کرد و گفت پیش از آغاز مسابقه، داوران کفش‌های او را…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464449" target="_blank">📅 07:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
تفنگ سه‌وضعیت بدون فینال
نجمه خدمتی با ۵۸۷ امتیاز در رده دهم قرار گرفت. شرمینه چهل‌امیرانی با ۵۸۳ امتیاز هجدهم و فاطمه امینی نیز با ۵۷۹ امتیاز سی‌ام شدند و به فینال نرسیدند.
@Sportfars</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464448" target="_blank">📅 07:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نفتکش‌های ایرانی دزدیده شده شناسایی شدند
🔹
۳ نفتکش حامل محمولۀ ۶۰۰ میلیون دلاری منتسب به ایران که به ادعای تانکر ترکرز توسط آمریکا ربوده شده‌اند، شناسایی شدند.
🔹
این سه نفتکش در اردیبهشت امسال واقع در دریای عمان ربوده شده‌اند.
🔹
بر این مبنا نفتکش مجستیک ایکس…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/464447" target="_blank">📅 07:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stADwwZNpvBsP5Hu8tiE-1sKmlkJ_n-zxR8_Kf6YE5ZNMUwzNesypkB6BlFFI1dfTu1OjvfOJkU0sz5_OH3lqDvG4SR_5pWCHaIJxM2UUdjI9qgClJ3uvn2vFmCCkTOdVgde-zd9gbH7OfL5sKtS-T_9LfCrxs_F37Gb13DdT8PaOhPQ5h5vWgbwR_BjQIHa9GdS38SrT944bHrv7THoeoolaruSfT-W29XA_T4fUEP9nMpG8-WiTOP40-N_P-4nXvbRfAKNScJUkMXDz5DZrmxZpNKW5zMknTg85RvLWpN6CXHOz-MgWo80QmRHIkeT7W1-Wsc3ji9knKFGcCvDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنهایی ریاض؛ عربستان به کمک فرانسه چشم دوخت
🔹
در شرایطی که عربستان با تشدید حملات و تهدید علیه زیرساخت‌های حیاتی و انرژی خود روبه‌روست، ریاض برای تقویت دفاع از این تأسیسات به شرکای اروپایی روی آورده و فرانسه با اعزام نیرو، رادار و سامانه‌های دفاعی برای حفاظت از مرکز انرژی «ینبع» وارد عمل می‌شود.
🔹
رئیس‌جمهور فرانسه در این‌باره گفته نیروهای فرانسوی قرار نیست در جنگ میان عربستان و یمن مشارکت کنند؛ و هدف، فقط حفاظت از یک تأسیسات انرژی مهم است که امکان انتقال «چند میلیون بشکه» نفت از عربستان به بازارهای جهانی را فراهم می‌کند.
🔗
اما هدف فرانسه از این تصمیم چیست،‌ و قرار است چه تجهیزاتی به عربستان ارسال کند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464446" target="_blank">📅 06:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2TiIrs618-QMCpShfC3gZw2qXM6aziFvSOUJT7ek1Yu9cjuSXXPN-tW07qh9ZxYBlZJ5R3ZmhfPkP_RIhTiAbfoNt3vjYeSatZXqcUHq1o5iYbKZFW0iYUASjBbsKkxULmMUW84pGlw5YeZXWFwX0S-RHAp14brs1EILSJ_yt7LHTDkZ10V-d2ATONEaLLqIc5bZ3nZKtVR6n_RSDVOpDjYBb65-MeXCoVZ2PYxJ-vVmyNiYr89hG1I73I7iZxDXRX1d_AiRq2SVB8LOuUc1kVNWulBgqrXWiHv3DVVzkSjIq72YES7GG7IrIbqRBCBAFuIv5XhAfoQX_i59StmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیک‌تاک دادگاهی شد
🔹
برای نخستین‌بار در آمریکا، یک دادگاه در آلاباما موارد مربوط به آسیب تیک‌تاک به سلامت روان نوجوانان را بررسی می‌کند.
🔹
آلاباما می‌گوید طراحی و الگوریتم تیک‌تاک کاربران جوان را به استفادۀ مداوم سوق داده و آنها را در معرض محتوای آسیب‌زا قرار می‌دهد.
🔹
تیک‌تاک این اتهامات را رد کرده و بر اقدامات خود برای محافظت از کاربران کم‌سن‌وسال تأکید دارد.
🔹
نتیجۀ این پرونده می‌تواند بر ده‌ها شکایت مشابه علیه تیک‌تاک در آمریکا اثر بگذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464445" target="_blank">📅 06:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9vCtos10AH3OZBm1v8WhA5zj0dwoBh6i4085CSEKUu-4yMVX_TdmjQklQqqul1lLUrzc1_mxQ7oOsH9cHl2NqbB9WCwxx2gSRUAFh_yUhOFTRAK0Bq91t9MBmIOjTRuOeHnIXknryNJ9rDTXAXqDSw-a8yaSAzE51-UJpV3crFEO_tqE9kZ8GhD8bsun-0ylgVr-xMQrJJ198LK8i6jxU2jaTXZxVYrk3LxOUhvSatgJsnD37k0HECnNL8tW8OjZTA2dbTUa6lp4ketQ37g8uZFmwv1s3I0RiDkMNFpClvc45z91lc6BrmNJ8WJdG8ejCRZ1Hkf5YuRc_w5LxzY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به فضا می‌رود
🔹
گوگل قصد دارد نخستین ماهوارۀ آزمایشی پروژۀ «سان‌چر» را به مدار زمین بفرستد تا عملکرد تراشه‌های هوش مصنوعی خود را در شرایط واقعی فضا آزمایش کند.
🔹
این آزمایش مقاومت تراشه‌ها در برابر تشعشعات، تغییرات شدید دما و مشکلات خنک‌سازی در خلأ فضا را بررسی می‌کند.
🔹
هدف بلندمدت گوگل ساخت زیرساخت‌های پردازش هوش مصنوعی در مدار زمین است؛ جایی که پنل‌های خورشیدی می‌توانند انرژی مورد نیاز این سامانه‌ها را تأمین کنند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464444" target="_blank">📅 05:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0578016e29.mp4?token=Bj_lZ4otikPOQLR6yI86t1jSwPgvT-6TYDenRSl0VdSufL4Sn7OT5hQB_7DI1lMkmY5shE32m05uidDRTEeMTh7ESbKLeUDagJl5ZbiybkAK7vtvwsJL6eIH8I3JsyUbppxBaDnSJMC0apvjtqTHVjwXK9CHdktOmaBkeJwwjObwh_Nlezfre6rRA7M8_GcBjCaksRHHHmsmXRK7Ckk4P53Dk2gh1p35sgJQSTGdQhhYgAFovwusVnnhltg0ALDA8twNmC_pr3aHnDrU7KTWUk72ATTGJXVlV9XiXWhYr7I87FbaJBrDA4w5pRDpYTXbwzR_gMG5Py2L-IPlk6oR6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0578016e29.mp4?token=Bj_lZ4otikPOQLR6yI86t1jSwPgvT-6TYDenRSl0VdSufL4Sn7OT5hQB_7DI1lMkmY5shE32m05uidDRTEeMTh7ESbKLeUDagJl5ZbiybkAK7vtvwsJL6eIH8I3JsyUbppxBaDnSJMC0apvjtqTHVjwXK9CHdktOmaBkeJwwjObwh_Nlezfre6rRA7M8_GcBjCaksRHHHmsmXRK7Ckk4P53Dk2gh1p35sgJQSTGdQhhYgAFovwusVnnhltg0ALDA8twNmC_pr3aHnDrU7KTWUk72ATTGJXVlV9XiXWhYr7I87FbaJBrDA4w5pRDpYTXbwzR_gMG5Py2L-IPlk6oR6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قویدل و کارگرپور فینالیست شدند
🔹
پیمان قویدل و تانیا کارگرپور، نمایندگان ایران در کایاک دونفره میکس ۵۰۰ متر بازی‌های آسیایی ۲۰۲۶، با قرار گرفتن در جایگاه نخست  مرحله نیمه‌نهایی، جواز حضور در فینال این ماده را کسب کردند.
@Sportfars</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464443" target="_blank">📅 05:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">منابع عربی از شنیده‌شدن صدای چندین انفجار در منطقۀ جیزان عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464442" target="_blank">📅 04:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN3PPoRSCYn0MYXmUODfeHTMP7-W8FWUrBrwLQ-cj98jtcXLN_vp2RY7aT_mgPN8J7JzCa1ZMfxHWBxvm1SOA4q89C5adm7oWBDL4nMu64palbsEWXMxqbeZamirvvr1zv5Jxy--Op4EzHUf4B4_mt80Xkg8MiVGrMLP1LhebklVUvysF4vw5N9b2emASiMkOwuYi4GwfLoTBwcN20ETWRikWC6WcB3vDKWDeqXG947PCuWx2MlT_D0pLSE8bYTQYgAr8ZVOf9GyqI2A3bKvb2vi47lVKuHar0O6702eOuw-UXVdlV7msZkOMzsdFOea_5zXAxk0RRrhSdhbPLov5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RW0l29iojYkJYt556X19zIKVAxDeRiDXs85lur93a4uzweDEvFrRsUAC22c6M2LlWQTbTxWEK-pj2t-aDJN4Qce2mhnDsqzKxrqvATWv7PlJinrqNomzDCPmft102-VenDMGLUGA0nflMc41eAzji8EZnxLTrUEMA4U5J2MBsGNZc4a8_puIpdX3xrksrOFp4uk0oMRnuAVRUvV0ddW1uwoa9FwljaxdmudWd24mAOmg1tp-Y7e47BCy7Gj53kUYwGu9qRLaxe_ibbT4gUeXc-veNWn6YoCRM3Ckdtg44heI9PolZk5GsDgLuOjRCN3jgJvmITOdNoGUZykOCfn1Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تغییر عجیب جلد مجلۀ آمریکایی در طول ۴۷۰ روز
🔹
تنها ۴۷۰ روز زمان لازم بود تا طرح جلد مجلۀ اکونومیست از «پایان جمهوری اسلامی ایران» به «پایان حضور آمریکا در غرب آسیا» برسد.
🔹
در این مدت جنگ ۱۲ روزه و جنگ رمضان به ایران تحمیل شد و سنگین‌ترین فشار اقتصادی تاریخ به نقل از وزیر خزانه‌داری آمریکا در دستور کار آمریکا علیه ایران بوده است.
🔹
حالا اما مجلۀ اکونومیست که در زمان جنگ ۱۲ روزه طرح پرچم ایران پشت موشک را کشید و نوشت که «عاقبت چه خواهد شد؟»، طرحی از یک سرباز آمریکایی شکست خورده روی جلد برده و تیتر زده است که «وقتی آمریکا کناره‌گیری کند، چه می‌شود؟»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/464440" target="_blank">📅 04:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464439">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4db251178.mp4?token=shfFjLvFPmLfVSMa-bpomarCrda8-Iq0RbkPUGOUcO1AkeGQdWIQj2aeHlOt5fHkGclTVaMEQLE-E1eYhciBs3rz89q96mhLaoLQesWt8TYbtW2gJEBDzchkjYfzXAX-EehvMwt1GOa-AMnpwZx4UzQvgFONtWAtl5khHza3kLhq9Q93neDLN5gNiR4CW2EoWARHTkU-jWtf-iGZBYHfIQ9Q3oBpsbvTS8XkTX03_0bWR9VBuin8P-v6ms5euEHciMePt-SVE1osynlb5l6AjDQ34Pdht9r_YGgY3rNWO7gwNL-4NEnvkVTiNccbvjV0_am_zgus-zaPKZ0jnUrLPxYi66blIygkkdbHUqPq0scVhDhahNvfNEAHJ48dK_-gQgy23uRewuUOw1gBnbt_vPbYx5nXfyl4h8LrAXEXYYd0BLkiHeIUYSeK3rGWm6drWSff3wJ6tCBRBEE2hHkXh3YQDRT8AUev1NAg4dN0JcQAYnTKeUNaVbZL2y8NqSBFNreZ2TaJqAVV98DBjdKc2rgt-8qxKPZDM0JnAv3bs_nKQuCfJXxZjQR3C2VNuIxpVdJAthnYv6vbRHQ_H9GnqsDygSX4kB_LjCl_KSZloVR9jomUgWoLvREO8Z4k22zBbnv1rIiTy7FTnN-K6nPmLwvw7apoQtQC8Fn2pbSFC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4db251178.mp4?token=shfFjLvFPmLfVSMa-bpomarCrda8-Iq0RbkPUGOUcO1AkeGQdWIQj2aeHlOt5fHkGclTVaMEQLE-E1eYhciBs3rz89q96mhLaoLQesWt8TYbtW2gJEBDzchkjYfzXAX-EehvMwt1GOa-AMnpwZx4UzQvgFONtWAtl5khHza3kLhq9Q93neDLN5gNiR4CW2EoWARHTkU-jWtf-iGZBYHfIQ9Q3oBpsbvTS8XkTX03_0bWR9VBuin8P-v6ms5euEHciMePt-SVE1osynlb5l6AjDQ34Pdht9r_YGgY3rNWO7gwNL-4NEnvkVTiNccbvjV0_am_zgus-zaPKZ0jnUrLPxYi66blIygkkdbHUqPq0scVhDhahNvfNEAHJ48dK_-gQgy23uRewuUOw1gBnbt_vPbYx5nXfyl4h8LrAXEXYYd0BLkiHeIUYSeK3rGWm6drWSff3wJ6tCBRBEE2hHkXh3YQDRT8AUev1NAg4dN0JcQAYnTKeUNaVbZL2y8NqSBFNreZ2TaJqAVV98DBjdKc2rgt-8qxKPZDM0JnAv3bs_nKQuCfJXxZjQR3C2VNuIxpVdJAthnYv6vbRHQ_H9GnqsDygSX4kB_LjCl_KSZloVR9jomUgWoLvREO8Z4k22zBbnv1rIiTy7FTnN-K6nPmLwvw7apoQtQC8Fn2pbSFC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در گرفتاری چندبار یاد امام زمان(عج) افتادی
🎙
آیت‌الله مصباح
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464439" target="_blank">📅 04:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464438">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNhp4Sa1HpgXRE8iAkfXIC18qtba9PYVeCuE0l0of1FUgLoYbcN84Uo4cfErajDo-vWRSR20jM-vVOiPtbKwtLBFrpz_jM9fKPNgm-kAqiWDR6mJ1AorUoJF_SKQ9xzBAAd4gI2jFUE2F_y0gyyYNc0tDgCGJtOtYeZ_bB9JXZeJWKWhnMp0SZEwwt4HBtVreL-lqYeO3ue9ZE3ISFn_6-IAJ1qlIplOvxpfKxAsC2-u2UgGsoxCBH1kFLArajH98TW0rwCYBh5sIMM3I7KCNWacBIuRG9cQNMdY9PSMkAhVNY1MGC6bTAjw5DmzIRZc3xWecMPtWwbL0JGT7IRRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتائب سیدالشهدا: عراق نباید بخشی از محاصره علیه ایران باشد
🔹
دبیرکل گردان‌های سیدالشهدا در عراق، با انتقاد از محاصرۀ ظالمانۀ ایران گفت شایسته نیست عراق بخشی از این محاصره باشد.
🔹
الولایی گفت کشوری شعار لبیک یا حسین را به‌عنوان رویکرد و موضع خود برگزیده، باید موضع و صدای خود را در تحولات منطقه بیان کند.
🔹
وی از نمایندگان پارلمان عراق خواست دولت را ملزم کنند در برابر «دیکته‌های آمریکا» تسلیم نشود و با الگو گرفتن از روسیه و چین، با محاصرۀ ایران مخالفت کند.
🔸
طی روزهای قبل، دولت عراق تحت فشارهای آمریکا پرواز هواپیماهای ایرانی به فرودگاه‌های این کشور از جمله بغداد، سلیمانیه، اربیل و نجف را به حالت تعلیق درآورد.
🔸
پیش از این دبیرکل
جنبش نجبای عراق
نیز گفته بود، درصورتی که پروازها ایرانی به عراق ازسرگرفته نشود مردم عراق برای اعتصاب در فرودگاه‌ها حاضر خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/464438" target="_blank">📅 03:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464437" target="_blank">📅 03:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آتش‌سوزی اتوبوس در محور بیرجند-آرین‌شهر ۳ کشته برجای گذاشت
🔹
پلیس‌راه خراسان جنوبی: در پی برخورد یک دستگاه اتوبوس با تریلی در محور آرین‌شهر به بیرجند در محدودۀ پسوچ، اتوبوس دچار آتش‌سوزی شد که تا این لحظه سه نفر جان خود را از دست داده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464436" target="_blank">📅 03:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2zUezQzYu7sNBzV-ASxSafi6CctrtgYFItG8XRh4jh0tfG9BWTg56DKp2eakl-9bYEbyKeVIWyu0yFV3pi8XylJ3nvLGN5iCpBddtgDt2Yt-ByaA-2Xbzgc449Dz5le-Zg9Y0FpsEyqOVwaKfg4Zb7VvEtbv1VBxJ5R6nx7zHRpio6VaMQh2uVQKRQ2URJbtLylRfssoGZ3FCXYr44CkzRHhJildGZQIWv4JRrZQWvU_7quMoip__cHSQzq2Zg8YbmjtZpOVbneRAgX2hsGCYNiKuEY_szIPoFMuh7t4rZtQoDUB5SKQMURqy7XDgbLg4uJ0wl6GAyrB9AJLjuQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست اضطراری فرماندهان نظامی ترکیه، پاکستان و عربستان
🔹
عربستان سعودی، ترکیه و پاکستان در نشستی با حضور فرماندهان نظامی خود، دربارۀ حمایت از ریاض بر اساس توافق دفاعی مشترک میان سه کشور گفت‌وگو خواهند کرد.
🔹
بر اساس بیانیۀ وزارت خارجۀ عربستان سعودی، این کشورها…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464435" target="_blank">📅 02:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464434">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB96kUIckwWf4UXz66MVnAOOcw79iJgNgYFUDcKL6dUNYRmy7qtPgjuKmKfwVSxtbBFyK9oTOMIriE1Nl7VwsuHoeX96ZymM2lOhiWZdRQETIpS3cDJkA8rKxkISx2nXPJLjKhviJc666U8X_f4wuum56y3gYvKzlUpF7_13q2xkCdOwH1HvUzjoAYEP6x16W38mXHMMb0b0uOoMoJ7vjB8MWQMjYVTgUE3V5rn2dLJ88FFAgG-zmFXdaqOvk8X1CrbrNZ4kTgDckK7InM1VvxCj4ZewqjQ4ZuQLzHTV1wKVqQ7H7qDj9APkuWTCg0qaAJnBNTXm4UhPDimxzVnHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوکار: از غنی‌سازی ۶۰ درصدی کوتاه نمی‌آییم
🔹
رئیس کمیسیون امور داخلی کشور و شوراهای مجلس: سطح غنی‌سازی حق مسلم ملت ایران و جزو حقوق بنیادین کشور است و هیچ‌کس نمی‌تواند این حق را نادیده بگیرد.
🔹
آنچه امام شهید نیز بر آن تأکید داشتند، این بود که ما به دنبال سلاح هسته‌ای نیستیم، اما باید از برکات و مزایای دانش هسته‌ای برخوردار شویم تا ملت ایران بتواند از ظرفیت‌های این دانش استفاده کند.
🔹
غنی‌سازی هسته‌ای در سطوح و حوزه‌های مختلف، از صنعت و پزشکی گرفته تا کشاورزی و تولید سوخت، کاربرد دارد و در برخی حوزه‌ها نیز می‌تواند در تأمین نیازهای راهبردی کشور مورد استفاده قرار گیرد. بسیاری از کشورهای دنیا نیز از ظرفیت غنی‌سازی و فناوری هسته‌ای استفاده می‌کنند.
🔹
اینکه گفته شود نیازی به غنی‌سازی ۶۰ درصد نداریم، دقیقاً همان چیزی است که دشمنان می‌خواهند و ما باید در راستای احقاق حقوق ملت ایران، از این حقوق دفاع کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464434" target="_blank">📅 02:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464433">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بحرین: پیامدهای بسته‌بودن تنگۀ هرمز از منطقه فراتر می‌رود
🔹
وزیر خارجۀ بحرین: پیامدهای هدف قرار دادن کشتی‌ها در تنگۀ هرمز و اعمال محدودیت بر تردد، از منطقه فراتر می‌رود و بر قیمت‌های انرژی، مواد غذایی و زنجیره‌های تأمین تأثیر می‌گذارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/464433" target="_blank">📅 02:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464432">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آتش‌سوزی اتوبوس در محور بیرجند-آرین‌شهر ۳ کشته برجای گذاشت
🔹
پلیس‌راه خراسان جنوبی: در پی برخورد یک دستگاه اتوبوس با تریلی در محور آرین‌شهر به بیرجند در محدودۀ پسوچ، اتوبوس دچار آتش‌سوزی شد که تا این لحظه سه نفر جان خود را از دست داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/464432" target="_blank">📅 01:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464431">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منابع عربی از شنیده‌شدن صدای چندین انفجار در منطقۀ جیزان عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/464431" target="_blank">📅 01:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464430">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHAvhovWGZPLldg3_DJaknz71-XbzYSGW-3Jdi1ZMPY78Pj7dlFRc0SWofyHBjhtomMZZ2qBUDf7bmhKxhf9M6Gxm3MjYBzHKwMhE7yXOMdKoGmqlZVmkambh47jqZdmQ--TuP8XiNlP88sRoEzj1JCc81mgHZFrVj92MoRdiKJUA4LYFMCpcfkKC3k7pAAICvHXtfCaYB8ndeZDFrl6dxoh_qqJ9-ZoBSx-EEIcEo7byTLEVTz9htwc6SM9dvGmJHUfYgdrk2EU6IhvPqQDuAxN9zdYi_dxdpl4cBcSdm7398WwyEhLKN9dOuyD15kar1R_CSDZzB-mXSkjmNUSbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن پالیسی: قمار عربستان روی ترامپیسم شکست خورده است
🔹
نشریۀ فارین پالیسی در گزارشی با اشاره به تشدید حملات و محدودیت‌ها علیه مسیرهای صادرات نفت عربستان سعودی در خلیج‌فارس و دریای سرخ، نوشت: ریاض با یکی از دشوارترین مقاطع امنیتی و اقتصادی خود مواجه شده، ‌ علی‌رغم هزینه‌های هنگفت، آمریکا نتوانسته این کشور را در برابر خطرات امنیتی محافظت کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/464430" target="_blank">📅 01:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464429">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c1cbe1b.mp4?token=GLm25Ta61i_yptQVx4dK1FM8AIm7-TmmSz-ByZWfJtTbWwfGkUVb36MXn35FRgVsubuJPyY15ZBG8xX4zNmq81hM_dZhfaShfT7PGBX4BBIygMUrdyWNL4wi4XgGnPy_0rcJ7dR-wb-QpMblEsDMfO3lkLMhIp8qhg1XorNjoQxNy_1fRe298xmFbIXlRjzmcBsxYaX3eZSgS6y6w4-WegGu2_zVjd0rzkpL3s1QylsxCmRnjYunr2YqqqcfJViR8FjZehjUNJ9dbxCT02aFceWZqoj63XtBdlfieSSauS7gCyGmVpMf2Dt1vpenPQeIb-WUaMYhUZ67wgCSRISoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c1cbe1b.mp4?token=GLm25Ta61i_yptQVx4dK1FM8AIm7-TmmSz-ByZWfJtTbWwfGkUVb36MXn35FRgVsubuJPyY15ZBG8xX4zNmq81hM_dZhfaShfT7PGBX4BBIygMUrdyWNL4wi4XgGnPy_0rcJ7dR-wb-QpMblEsDMfO3lkLMhIp8qhg1XorNjoQxNy_1fRe298xmFbIXlRjzmcBsxYaX3eZSgS6y6w4-WegGu2_zVjd0rzkpL3s1QylsxCmRnjYunr2YqqqcfJViR8FjZehjUNJ9dbxCT02aFceWZqoj63XtBdlfieSSauS7gCyGmVpMf2Dt1vpenPQeIb-WUaMYhUZ67wgCSRISoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محیطی‌زاده دیسکالیفه شد
🔹
فاطمه محیطی‌زاده نمایندهٔ کشورمان در مادهٔ هفتگانهٔ دوومیدانی مسابقات آسیایی ناگویا در بخش پرتاب نیزه، به‌دلیل استاندارد‌نبودن کفش‌هایش دیسکالیفه شد و از جدول مسابقات کنار رفت. @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/464429" target="_blank">📅 01:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464428">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
🔹
المیادین از حملۀ هوایی رژیم اسرائیل به شهرک القنطره در جنوب لبنان خبر داد.
🔹
همچنین منابع خبری اعلام کردند توپخانۀ ارتش اسرائیل، دره زبقین در شهرستان صور را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/464428" target="_blank">📅 01:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464427">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvHAhR-6iHuawt5SDCTmdwCZmP5wOhrMDuJJ_hqTrcG_-ztlGiuLyQ5_jJIevJIjgnGS8zaWEinqXnP4brU-dZtZkiGXNm6tVUcUpkBYHFcf_nzkHLdyZ5mAiC9mQXPXzvf44eSV39Jx0xpznZNu92-LK5Lpx6pxUxya0LMEtHhOnPU9sNNxtqcq-Bsi2p67UANcKaDu8NpscVz2oipuw-5aANi10mp39bYGdIuko0FZnEEIjywi680LqyEttgVAq0rzQRVddWFO2LL5s1OkBQt1KL9QxvAFx4TdEsAYVXSmPzo9k_f37z1Uc4RxuOrMCZs9nX3yhZbWuxpKrr2OoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام سردار سیدمجید موسوی به ملی‌پوشان تکواندو در آستانۀ اعزام به بازی‌های آسیایی ناگویا
🔹
امروز، هر فرصت برافراشته شدن پرچم مقدس جمهوری اسلامی ایران، آوردگاه و میدانی برای نمایش عظمت و ارزش‌های ملت متمدن و مقتدر ایران است.
🔹
ضمن دعای خیر و آرزوی موفقیت روزافزون، چشم به راه شما با مدال‌های رنگین هستیم. پیروز باشید.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/464427" target="_blank">📅 00:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464426">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌ عراقچی: نمی‌شود کشوری را بمباران و محاصرۀ دریایی کرد، اما انتظار داشت کشتیرانی آن منطقه به وضعیت عادی بازگردد
🔹
ایران همچنان به کشتیرانی ایمن و امن متعهد است. با این حال، امنیت دریایی از طریق اقدامات نظامی بیشتر، تهدید، محاصره یا اعمال فشار اقتصادی قابل…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/464426" target="_blank">📅 00:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464425">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌ عراقچی: ادعای نزدیک‌بودن دستیابی ایران به سلاح هسته‌ای دروغ بزرگ است
🔹
اتهامات جدید مطرح‌شده دربارۀ برنامه هسته‌ای صلح‌آمیز ایران، ماهیتی سیاسی دارد و نمی‌تواند جایگزین ارزیابی‌های فنی و حقوقی شود. این ادعا که ایران در آستانۀ دستیابی به سلاح هسته‌ای قرار…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/464425" target="_blank">📅 00:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464424">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عراقچی: ترامپ و نتانیاهو از تریبون سازمان ملل تلاش کردند جایگاه قربانی و متجاوز را عوض کنند؛ آمریکا و اسرائیل نمی‌توانند اقدامات خود را تطهیر کنند
🔹
وزیر امور خارجه کشورمان در جمع خبرنگاران در نیویورک: در جریان تجاوز آمریکا و رژیم اسرائیل علیه ایران، بیش از…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/464424" target="_blank">📅 00:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464423">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عراقچی: ترامپ و نتانیاهو از تریبون سازمان ملل تلاش کردند جایگاه قربانی و متجاوز را عوض کنند
؛
آمریکا و اسرائیل نمی‌توانند اقدامات خود را تطهیر کنند
🔹
وزیر امور خارجه کشورمان در جمع خبرنگاران در نیویورک: در جریان تجاوز آمریکا و رژیم اسرائیل علیه ایران، بیش از پنج هزار نفر شهید شدند که صدها تن از آنان را زنان و کودکان تشکیل می‌دهند. ترور رهبر معظم جمهوری اسلامی ایران و شماری از مقامات ارشد سیاسی و نظامی کشور، جنایتی فاحش و نقض آشکار حقوق بین‌الملل بود.
🔹
مناطق مسکونی، مدارس، بیمارستان‌ها، تأسیسات انرژی، اماکن ورزشی و فرهنگی، زیرساخت‌های حمل‌ونقل و دیگر اهداف غیرنظامی مورد حمله قرار گرفته‌اند. کشتار بیش از ۱۶۸ دانش‌آموز و معلم در میناب، حمله با بمب‌های خوشه‌ای به ورزشگاه لامرد، بمباران منازل مسکونی با بمب‌های دو هزار پوندی و حملۀ موشکی به یک مراسم عروسی در سیریک، تنها نمونه‌هایی از این حملات است که مستند شده‌اند.
🔹
با این‌حال، رئیس‌جمهور آمریکا به‌همراه نخست‌وزیر رژیم اسرائیل، از تریبون مجمع عمومی تلاش کردند واقعیت‌ها را تحریف کرده و جایگاه قربانی و متجاوز را معکوس جلوه دهند. ایالات متحده و رژیم اسرائیل نمی‌توانند اقدامات خود علیه مردم ایران را تطهیر کنند.
🔹
آمریکا حالا محرومیت اقتصادی را به ابزاری برای مجازات جمعی و اعمال فشار سیاسی تبدیل کرده است. این کشور عامدانه خسارات شدید و قابل پیش‌بینی به مردم ایران وارد می‌کند و به‌طور مستقیم حقوق بنیادین آنان، از جمله حق حیات، سلامت، دسترسی به دارو و غذا را نقض می‌کند. این دیپلماسی نیست؛ اجبار و تروریسم اقتصادی است. این اقدامات، نقض آشکار و مستقیم اقدامات موقت الزام‌آوری است که دیوان بین‌المللی دادگستری در سوم اکتبر ۲۰۱۸ صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/464423" target="_blank">📅 00:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464422">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c__o_4Z5H3CGUa40b55n2JA6i1P454Ie9gvVKjFCYsDftJ7fiIiB4xuLdrG10Jq0cU2kWXTl5d741kWiv1g3ymm_EatyjuBFaWoUgppjjtDWydSmvc7Bj9F0xe-b31DLXNQNW3IWbhikk6LS2aXfNFnOOhrZvs_AwoJ17aV9N3CubOYVl3RvedibdA3t_6r1W6gLHtXuJmeaTiZYjrTLUn9wAwSrVJyIM8ftRrjMjExsc7pLfMwdKUv2PLGDGRh75tjPrac4y2wVzWAbgie2gLtK6zAgUWhP8Tr7WGejQkLLsomlnIUQz4rYMjXRD6u3SKRQl7kbCski5tSkPeKHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما می‌کاریم تا دیگران بخورند
🔹
روزی انوشیروان ساسانی برای شکار به صحرا رفته بود و گردش می‌کرد که مرد پیری را درحال کاشتن درخت گردو دید.
🔹
انوشیروان به او گفت: «ای پیرمرد، تو پیر و سالخورده‌ای؛ چطور امید داری که زنده بمانی و میوهٔ این درختی را که می‌کاری بخوری؟» پیرمرد پاسخ داد: «دیگران کاشتند و ما خوردیم، ما نیز می‌کاریم تا دیگران بخورند.»
🔹
انوشیروان از این سخن بسیار خوشش آمد و گفت: «زِه!» (آفرین).
🔹
از آنجا که عادت انوشیروان این بود که هرگاه کلمهٔ «زه» را بر زبان می‌آورد، هزار درهم پاداش می‌داد، بلافاصله هزار درهم به پیرمرد دادند.
🔹
پیرمرد گفت: «ای پادشاه، آیا هیچ‌کس را دیده‌ای که درختی بکارد و میوه و ثمره‌اش به این زودی به او برسد که به من رسید؟» انوشیروان باز هم خوشش آمد و گفت: «زه!» و هزار درهم دیگر به او دادند.
🔹
پیرمرد ادامه داد: «از برکتِ توجه و نظر پادشاه، این درخت در یک زمان ۲ بار میوه داد!» انوشیروان دوباره شگفت‌زده شد و گفت: «زه!» و دستور داد دو هزار درهم دیگر نیز به پیرمرد بدهند.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464422" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
