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
<img src="https://cdn4.telesco.pe/file/NUIVp5sXc4mLUFnGkYtWYqTUH0o9d3nRD2hFLP1oWZ4FEQKW7B0vxN-UAoGh85xLLm9Brr4M2QsURcyj1pr8fkrPo98mM7rKVK-od_KhHaoWZLIGjLP_yn6L3V_gbGTK45G6vE4-mQAuwb3OGtpFbvIuHjy7kOE4zUdgjAcgqNBXK2O_1iwERdrolucPb52KqZ916QTxs5ZcKsu75rCUxS0cS081Zf-s_zStKGg6k38xKRHDc92E17Snm1FHSzSLLM7h3gPyNOZH7L4rQ-5XJVkwKK7G_Be9adoEEuBYriLd5uxbszbdZUvuvY8miYXQJqwiE-o7AaZVwXIp0ZwUPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.55M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 19:46:32</div>
<hr>

<div class="tg-post" id="msg-659389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
گفت‌وگوی تلفنی پوتین و ترامپ درباره ایران
🔹
ترامپ به پوتین گفته است که توافق بین ایران و آمریکا بسیار نزدیک بوده و ممکن است امروز اعلام شود.
🔹
پوتین نیز از مهار شدن درگیری بین ایران و آمریکا که می‌توانست کل منطقه را شعله‌ور کند، ابراز رضایت کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/659389" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4a065afe.mp4?token=oYHMvTMiu__6c0pj-LBhf-VTMPQO9OMQ9iCaPTA3b_ZKqVOoGliu04Tn3ZTmSHAQ-Jrjcc2UZZgotfB6xes7nyVdE2BGomdcFyvKOz1Yxm0wHqIGO0Vr9zjDy9qzpFT5VTkHpJQMbl3RiCC0FMljanDT8cucnFXVGJ_2sm4wYDGscgMxaK_G5Yhh0MX3kmyVDJL0funRMIjDYBxQOaueeHO58-rYWTci_YAl98FvKBOAsUC1vUkOkrztiZG9YXxV89o48w0_l4ctmGetMQDRm-YZuovhBBHTM4U7FGtr8CBCF5UxR76vE-Qu0vGR11JRas2yZ4qZXMpadBcnubXofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4a065afe.mp4?token=oYHMvTMiu__6c0pj-LBhf-VTMPQO9OMQ9iCaPTA3b_ZKqVOoGliu04Tn3ZTmSHAQ-Jrjcc2UZZgotfB6xes7nyVdE2BGomdcFyvKOz1Yxm0wHqIGO0Vr9zjDy9qzpFT5VTkHpJQMbl3RiCC0FMljanDT8cucnFXVGJ_2sm4wYDGscgMxaK_G5Yhh0MX3kmyVDJL0funRMIjDYBxQOaueeHO58-rYWTci_YAl98FvKBOAsUC1vUkOkrztiZG9YXxV89o48w0_l4ctmGetMQDRm-YZuovhBBHTM4U7FGtr8CBCF5UxR76vE-Qu0vGR11JRas2yZ4qZXMpadBcnubXofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آچمز شدن وزیر جنگ آمریکا در یک گفتگوی تلویزیونی
🔹
«پیت هگست»، وزیر جنگ دولت تروریستی آمریکا در گفتگو با شبکه سی‌بی‌اس مدعی شد آمریکا در تمام این مدت بر تنگه‌ هرمز کنترل داشته‌ است.
🔹
مجری برنامه در پاسخ به این ادعا او را به چالش کشید و گفت: «اگر چنین است…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/659388" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659387">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پزشکیان: انتظار می‌رود رسانۀ ملی منعکس‌کننده سیاست‌ها و رویکردهای مراجع رسمی تصمیم‌گیری کشور باشد
🔹
آنچه گاها در رسانه ملی درباره جنگ و مذاکره مطرح می‌شود، لزوماً بازتاب‌دهنده دیدگاه شورای عالی امنیت ملی، شورای عالی دفاع یا حتی رهنمودهای رهبر معظم انقلاب…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/659387" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659386">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازارها چند درصد روی صعود ایران شرط بستند؟
🔹
همزمان با آغاز رقابت‌های جام‌جهانی بازار پیش‌بینی‌ها و شرط‌بندی‌ها روی تیم‌های صعود کننده داغ شده!
🔹
حالا ایران طبق این شرط‌بندی‌ها چقدر شانس صعود دارد؟ در این ویدئو بررسی کرده‌ایم
@Tv_Fori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/659386" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659385">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پزشکیان: عبور موفق از این شرایط نیازمند همراهی مردم و مشارکت عمومی در اصلاح الگوی مصرف است
🔹
با وجود ناترازی‌ها و آسیب‌های واردشده به زیرساخت‌های انرژی، دستگاه‌های مسئول تاکنون شرایط را مدیریت کرده‌اند و با مشارکت مردم، بخش تولید، صنعت و خانوارها با مشکل…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/659385" target="_blank">📅 19:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659383">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
♦️
پزشکیان: مردمی که در بیش از ۱۰۰ روز گذشته و در سخت‌ترین شرایط از کشور و نظام حمایت کردند، اگر با تورم و مشکلات اقتصادی پی‌درپی مواجه باشند ممکن است دلسرد و ناراضی شوند
🔹
دولت خود را موظف می‌داند تمام توان خود را برای بهبود شرایط زندگی آنان به کار گیرد.…</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/659383" target="_blank">📅 19:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659382">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
♦️
پزشکیان: مذاکره به معنای چشم‌پوشی از اصول نیست و جمهوری اسلامی ایران در برابر هیچ‌گونه زورگویی و فشار غیرقانونی سر تسلیم فرود نخواهد آورد
🔹
مذاکرات تنها یکی از ابزارهای تأمین منافع ملی است. دولت همزمان مسیرهای مختلفی را برای تقویت اقتصاد و ارتقای جایگاه…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/659382" target="_blank">📅 19:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659381">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVEFxPykYGRdiBB52kbXcEjeS9OqLgrzyu0AyUO0oc9J59C9NTLUQxbmYr8r6iCs3_W1glsQ906rPwqhzXO2Pr_m5SD8WMNJqPigIKLRTCk74Y8oQ_OexN0Z_glXRz3-13cmPfbQ8DvygwsNWS1-y2TV-VAKstMhsaMamKV1vsEmB_KY9IIcdWogNcbQ6Yf15jWiWkNy_ozZBRSDXy-1Jfzz8oVRKTl2SDSLgOWieeHni2Ar61SwjGulGEBIzfCf55ZT01jaLqSpzN7IvOhHgBNMruyVC8d8Eq1vt1om_5gN-eReXtTU4UMJTTIG5S_cs-9hZRy2OlNncgCMZ_2d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پنل تخصصی همایش «نقطه تصمیم» چه گذشت؟
🔹
فعالان اقتصاد دیجیتال در پنل تخصصی همایش «نقطه تصمیم» مهم‌ترین چالش امروز کسب‌وکارها را «عدم قطعیت» عنوان کردند.
🔹
دانیال احمدزاده، مدیرعامل ایران‌سرور، عدم قطعیت را بزرگ‌ترین چالش کسب‌وکارها دانست و بر اهمیت یادگیری مداوم برای بقا در اقتصاد دیجیتال تأکید کرد. یوسف مذهب، مدیرعامل آموت، سیستم‌سازی را راهی برای عبور از بحران‌ها و ارائه خدمات باکیفیت عنوان کرد.
🔹
زهرا مکرمی، مدیرعامل کیف پول من، گفت این مجموعه در شش ماه گذشته تمرکز خود را بر پایداری سیستم‌ها گذاشته و معتقد است باید از دل تهدیدها فرصت ساخت.
🔹
امیرعلی نجومی، مدیر روابط عمومی سپهران، نیز با اشاره به توقف توسعه در بسیاری از کسب‌وکارها برای حفظ بقا، از تأثیر رشد هوش مصنوعی بر کاهش برخی فرصت‌های شغلی سخن گفت.
🔹
صادق شریعتی، مدیرعامل اقامت ۲۴، حفظ نیروی انسانی را مهم‌ترین دستاورد ماه‌های اخیر دانست و گفت صنعت گردشگری با هر بحران بیشترین آسیب را می‌بیند.
🔹
وحید ابراهیمی، مدیرعامل گروه دایان، نیز تأکید کرد حفظ سرمایه انسانی در دوران بحران، کلید موفقیت در دوره پسابحران است.
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/659381" target="_blank">📅 19:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659380">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
♦️
پزشکیان: بخش مهمی از تلاش‌های دیپلماتیک کشور در هفته‌های اخیر نتایج مثبتی به همراه داشته و بسیاری از مسائل و سوءتفاهم‌ها با کشورهای حوزۀ خلیج فارس در مسیر حل‌وفصل قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/659380" target="_blank">📅 19:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659379">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
♦️
پزشکیان: پیش از این نیز گفته‌ام و امروز نیز بر همان موضع تأکید دارم که از بابت قرار گرفتن کشورهای همسایه در معرض تبعات اقدامات نظامی ابراز تأسف می‌کنم
🔹
البته هدف عملیات ما پایگاه‌های آمریکا در خاک این کشورها بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/659379" target="_blank">📅 19:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659378">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
♦️
پزشکیان: تصمیمات راهبردی باید بر مبنای عقلانیت، محاسبۀ دقیق و در نظر گرفتن توان ملی گرفته شود
🔹
در کنار حمایت از نیروهای مسلح، باید نسبت میان مأموریت‌ها، امکانات و ظرفیت‌های کشور نیز مورد توجه قرار گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/659378" target="_blank">📅 19:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659377">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
♦️
پزشکیان: مهم‌ترین اولویت دولت، بهبود شرایط زندگی مردم و کاهش فشارهای اقتصادی جنگ اخیر بر خانوارهاست
🔹
امروز بخش‌هایی از جامعه با مشکلات معیشتی جدی روبه‌رو هستند؛ درحالی‌که برخی افراد بدون آنکه آثار تورم و دشواری‌های اقتصادی را در زندگی خود لمس کنند، صرفاً…</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/659377" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659376">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اعلام زمان تعویض پرچم حرم امام حسین علیه‌السلام
🔹
آستان مقدس حرم امام حسین علیه‌السلام اعلام کرد که مراسم پایین آوردن پرچم قرمز و برافراشتن پرچم عزا و سیاه بر فراز گنبد حرم، غروب روز سه‌شنبه و پس از نماز مغرب و عشاء برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/659376" target="_blank">📅 19:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659375">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
♦️
پاسخ پزشکیان به دروغ‌پردازی‌ها در مورد استعفایش
🔹
بنده شخصاً برای کار و تلاش و خدمتگزاری به مردم کشور هیچ تردیدی به خود راه نداده‌ام و اگر به پیش از انتخابات هم بازگردیم و این باور را داشته باشم که با آمدنم می‌توانم گره‌ای از مشکلات کشور و مردم باز کنم…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/659375" target="_blank">📅 19:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659374">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct_R0Xxzh2FnoQPKlRI7A7DiF2n8ygspGAqjSCIkq-KCPw2nG56maO-aE0JMZzM1Uey-V24s3LD5JhFqNYdjQss0wBzHnaG5Gl-3Ko7kDELL6NOWuMhVrbk2hieybFJIeG7aFHkuOtm7Ch6LOWL5i1Q-Bl0cClGYLI5l2HsohFcadJo600lIX1GMloQLem6IxoLvHr39L1S7yk6Z340PTuNl0dvHjXU5gu2Fcl4x2Q78GPfXU20SVXoNe55iWFRFay1Elnb5AN3sQe3Uf7SBcBPs0NFIbuUJbsIvTSKTiDI5rJ1x5tJu5xfFL2Svj-mNzvNTnRyFDZsjmSbaQOP49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پادشاه خاتون؛ شاعری فرمانروا
🔹
پادشاه خاتون، بانوی قدرتمند عصر ایلخانی، در دل آشوب مغولان به فرمانروایی و سیاست رسید. او تنها حاکمی زیرک نبود؛ شاعری خوش‌ذوق، خوشنویسی چیره‌دست و پشتیبان فرهنگ و دانش نیز بود. قرآن را به دست خویش نوشت و دربارش پناهگاه ادیبان،…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/659374" target="_blank">📅 19:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659373">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
♦️
پزشکیان:  دولت برای حفظ منافع کشور و مردم تلخ زبانی‌ها را به جان می‌خرد
🔹
ما با تمام وجود برای خدمت به کشور و مردم عزیزمان و همچنین آرمان‌ها و ارزش‌های واقعی خود آمده‌ایم نه ارزش‌های کاذب و غیرواقعی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/659373" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659372">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌ ‌
♦️
پزشکیان: [در مورد مذاکرات] حتی اگر نظر شخصی بنده متفاوت باشد، خود را موظف به تبعیت از تصمیم نهایی نظام می‌دانم؛ چراکه معتقدم ایشان براساس دور اندیشی و همفکری با عقلای کشور و در نظر گرفتن مصالح و منافع ملت تصمیم خواهند گرفت نه تحت فشار جریان‌های سیاسی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659372" target="_blank">📅 19:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659371">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
پزشکیان: ما به دنبال آن هستیم که از مسیر حفظ اقتدار ملی، برای کشور گشایش ایجاد و منافع مردم را تأمین کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659371" target="_blank">📅 19:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
♦️
پزشکیان: نقد و مطالبه‌گری حق طبیعی جامعه است، اما تخریب کسانی که مأموریت مبتنی بر قانون به‌عهده دارند به دور از انصاف و مردانگی است
🔹
مایه تأسف است که افرادی که در چارچوب مأموریت‌های رسمی و با هدف صیانت از منافع ملی و عزت کشور در حال انجام وظیفه هستند،…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659370" target="_blank">📅 19:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659369">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
♦️
پزشکیان: در برابر هیچ قدرتی سر تعظیم فرود نخواهیم آورد، اما در برابر ملت ایران و مطالبات مشروع آنان خود را مسئول و پاسخگو می‌دانیم. البته منظور از مردم، همه مردم ایران هستند، نه یک جریان یا گروه خاص
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659369" target="_blank">📅 19:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
برگزاری کابینه امنیتی اسرائیل در پناهگاه‌های زیرزمینی
🔹
شبکه ۱۳ تلویزیون رژیم صهیونیستی از اتخاذ تدابیر امنیتی فوق‌العاده برای برگزاری نشست امشب کابینه جنگ این رژیم خبر داد.
🔹
به گزارش این شبکه، به دلیل افزایش تنش‌ها و احتمال پاسخ مستقیم ایران به تجاوزات اخیر، نشست امشب کابینه امنیتی سیاسی در یکی از سایت‌های فوق‌محرمانه و مستحکم زیرزمینی برگزار خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659368" target="_blank">📅 19:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
♦️
پزشکیان: تحولات اخیر نشان داد که هیچ کشوری بیش از خود ما دغدغه منافع ایران را ندارد و به جز خدای متعال به هیچ کس نباید متکی باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659367" target="_blank">📅 19:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پزشکیان: اگر به وحدت و انسجام ملی باور داریم و اگر مدعی تبعیت از ولایت هستیم، باید تصمیمات شورای‌عالی امنیت ملی را که برآیند نظر تمامی ارکان نظام است، مبنای عمل قرار دهیم
🔹
شورای‌عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659366" target="_blank">📅 19:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پزشکیان: اگر به وحدت و انسجام ملی باور داریم و اگر مدعی تبعیت از ولایت هستیم، باید تصمیمات شورای‌عالی امنیت ملی را که برآیند نظر تمامی ارکان نظام است، مبنای عمل قرار دهیم
🔹
شورای‌عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659365" target="_blank">📅 19:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVX56Cyeu_F1mtIk0dGS4Y05ApS443A_6afWtAmSKdIWft5CXe5f0P3hByXXCRbcl37EWJlliGSlQ335Z_y83-nVok6UuLQmXoZP29YPaCwYtUzY86wdW64LkRd79SZvJuorT1xtLAIlPHEYfSkAt3Hs3JObN2Dxl1SeTcA7TANO53NQKFstwmQnEtLUJUnVNNIyKh4CebgUsHtbhAfYrhtenSzY-ecGVLtg0GZYoj_kOKyQKnQFFKHR9F6G8kBVM_M5cs3QGQyEQk9VN5-7f0nR4pgWjQCYwKrHdsNLjb7glsM2XMi16c-7zfc_cnrLXCkHfRbZlfmw4ANqM1Zwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده هوافضا: گوش به فرمان ولایت باشید و از هر کلامی که اتحاد مقدس شما را به خطر می‌اندازد دوری نمایید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659364" target="_blank">📅 18:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrDbjNKuATXwEo1S4NSJUYDFdt_U3sq3xXXausy0Droo_PAsRjZMHEdrKFbooH_cuO_QxAb0sTtD3E9WI_GsyQ8dchS5c7LvHVwshdtOoGz-fCVKb5q1N9XNe8tBMoBlSjj8LsfCDe6v017L5BDbuDunB1GlELjaV8E7tUzyxTIQ1bPOp-Q8iWSTESN54TGzlERiBr72azwKMsab6Lhho5Ej7zhbEzdW4YDmUlrLZXPBtJDUJf6HmV4ffx4FuLaPtm7Ct7PAVFgnhQim29jgBgtEAC8BbUVGDDLgmnlYXPaTeyftNrRYk4GS74SO_G-yAAMnX4ilJkR8grs_bkakFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659363" target="_blank">📅 18:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOzzWbgWW8mebUfeb9Db4nmhL9Qgx_82juhM2Qi1PguUqf-X_dW-V6pufeU-BY4b4LT9MpuwNnhXVm6tTQ6Q0jcquZXjW8_3M_CFMrQlFUHbG59FscJYiFrPTzaz1Ga_wSQnrAm84GcjJLIhTCWNeFqxXEJ_Ejk8nLEKO0moM7LhBcNrlkTRsue2D-5B80e3JC3jaPkMV_sfmKkp8Q3oA7MYoNhqN94HpNSj597wqjhw9mHQ6KEWBCwkLt1S_uJJTDyAf-bPasP5uuTIEBOS259C1RAW29cNlrzTr0nNuDzkpW2fZrUYLIBGJcuTzOu0pUIrXCazKIgnsJhVMalUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه کان اسرائیل به نقل از منابع امنیتی: اسرائیل با توافق آمریکا و ایران از جنوب لبنان عقب‌نشینی نخواهد کرد
خبرگزاری آناتولی:
🔹
منابع امنیتی اسرائیل در گفتگو با شبکه کان اعلام کردند که اسرائیل به دنبال توافق احتمالی میان آمریکا و ایران، از جنوب لبنان عقب‌نشینی نخواهد کرد و عملیات نظامی در این مناطق را ادامه خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659362" target="_blank">📅 18:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تشکیل پلیس اطفال تصویب شد
محمدحسین محمدی، نائب رئیس اول کمیسیون قضایی در
#گفتگو
با خبرفوری:
🔹
در اصلاح قانون آیین دادرسی کیفری، حدود ۱۰۰ ماده مورد بازنگری و اصلاح قرار گرفت.
🔹
در این اصلاحیه، موضوع «پلیس اطفال» به قانون اضافه شده و دولت مکلف شده با همکاری نیروی انتظامی و بهزیستی، این نهاد را برای حمایت از کودکان و نوجوانان تشکیل دهد.
🔹
همچنین ماده ۴۷۷ قانون با هدف تأمین بهتر حقوق مردم و جلوگیری از اطاله دادرسی اصلاح شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659361" target="_blank">📅 18:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f8e64c4f.mp4?token=RCwZ46AK2gOlYkQTUOD_jJ0v3qgNFrq4n6bo28ZvzB4r6fL5FheFRrSjft35G2IF8W2WV8If0ylePGcT4Z41xMNkjddqs7UE85XOs24ykEZqHQO3YtldQdsLKbOgiSl5RsnmFDxKOXcF3PSLjJF6Fvw9HFnKUdimOjSD3mCqrQREUf0XVb8Rhi9wqsHJn_rX-eulCclf8sjrZrd-L1dxQeHCekL5YAcYil6Unbd7KMjNoRAFuFDRcoMmoiqTjxXoht4gh8QQl5UqPICeXdFPBbiQ_Ov3DDu_Ai5KuRlC5zYXUxdU_wEx5i7ddHTAK5faTyFZf9iia0UdDAQ5wxkFpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f8e64c4f.mp4?token=RCwZ46AK2gOlYkQTUOD_jJ0v3qgNFrq4n6bo28ZvzB4r6fL5FheFRrSjft35G2IF8W2WV8If0ylePGcT4Z41xMNkjddqs7UE85XOs24ykEZqHQO3YtldQdsLKbOgiSl5RsnmFDxKOXcF3PSLjJF6Fvw9HFnKUdimOjSD3mCqrQREUf0XVb8Rhi9wqsHJn_rX-eulCclf8sjrZrd-L1dxQeHCekL5YAcYil6Unbd7KMjNoRAFuFDRcoMmoiqTjxXoht4gh8QQl5UqPICeXdFPBbiQ_Ov3DDu_Ai5KuRlC5zYXUxdU_wEx5i7ddHTAK5faTyFZf9iia0UdDAQ5wxkFpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد ۲ بالگرد در آسمان ریودوژانیرو در برزیل
🔹
۶ نفر پس از برخورد ۲ بالگرد در آسمان درجنوب غربی ریودوژانیرو، در برزیل جان باختند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659360" target="_blank">📅 18:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEjTQc6cjw3xL9P5thdfeAu2fPaswB_Pew9onrKhAbCe1EvRbsmFmr_SxFG7Ak_upCp78HeyJnj32L0d-TUFv7dRTSv_14MxFFR9AKZxevbI1zmEF-Re_4vYa8mJNkNurkNeFnA3abM9E-1Ms7tl6e01OXdYnWCQOJJH_WWTYIq3q8Oil7WsvrCMIO33_304dEAgCUhj2yIiHjehvuK_toFfW0xBLLbsjHGkFIQRNHbwXgQ51vPj7-DvWF2Zj_ey8uXy34Gxs6qhH8SKGYKBpNjFGsNVVj0vdMCpTnfJqmo42S-aGDcul1Wnt5JJSolqz75oCTlBZNolXQe0Nt279g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه / در کمتر از ۲۴ ساعت؛ ارائه خدمات مبتنی بر کارت در بانک‌تجارت فعال شد
🔹
ضمن قدردانی از سعه صدر مشتریان ارجمند به استحضار می‌رساند، ارائه خدمات انتقال وجه از طریق خودپرداز و خرید از  پایانه‌های فروشگاهی و سایر درگاه‌های پرداخت در کمتر از ۲۴ ساعت پس از اختلال، صبح امروز ( یکشنبه ۲۴ خرداد ماه) فعال گردید.
🔹
همچنین انجام خدمات مبتنی بر کارت از بستر همراه بانک‌تجارت امکانپذیر است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659359" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f547678c0c.mp4?token=RnxaMNIVp0DQKrEgbYQKt5SBflHku0WDgYm52fZkWnPSQ9eeXXJw-zD37jarv_H5unZxcg-x6nJN8scu65O6ERMt0mVopec1_HGEMw-97d16oid_WLymBCgaH6vYITTAlCkfHJLh0k-R4v0F5M7Rqtq5Xij5lvW4AXknpLU96jb9OfdlzIUQdPZw7K2XE3JO6Nuy_36ZCIoBI6rDjpHoTByKbxfuxrydjV7NjFbHIS4W4ZDVZruhEnM76R8JCp5w23qPHh-jrtANiTcDoAAJ-WnICAo1qEo_S4DVezvbrIa1gYy8tCDn-uSfCPnHpMB7fXRNpk34S7wC03MZj59ULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f547678c0c.mp4?token=RnxaMNIVp0DQKrEgbYQKt5SBflHku0WDgYm52fZkWnPSQ9eeXXJw-zD37jarv_H5unZxcg-x6nJN8scu65O6ERMt0mVopec1_HGEMw-97d16oid_WLymBCgaH6vYITTAlCkfHJLh0k-R4v0F5M7Rqtq5Xij5lvW4AXknpLU96jb9OfdlzIUQdPZw7K2XE3JO6Nuy_36ZCIoBI6rDjpHoTByKbxfuxrydjV7NjFbHIS4W4ZDVZruhEnM76R8JCp5w23qPHh-jrtANiTcDoAAJ-WnICAo1qEo_S4DVezvbrIa1gYy8tCDn-uSfCPnHpMB7fXRNpk34S7wC03MZj59ULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همایش تخصصی «نقطه تصمیم»
🔹
گزارش ویدیویی از همایش اقتصادی نقطه تصمیم به میزبانی هلدینگ تبلیغاتی رسانه‌ای باران در مشهد، در حال برگزاری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659358" target="_blank">📅 18:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52da291ebc.mp4?token=qw-cFMhQjjwd6G4R-2X330JFmV37B4GxCcEEdIU8aO8pUSxgnT_0ARcEtXsxNDSET3P2JQFcS3YBS_-qCQugYdHDphBE0C8UvHbRMGc11jywcOqKXMjd7XjKKMvpzbXVk7J0yox5f911kTd-_sY4h4mqZb-yKTk8Wg_XIAJ2fSxN183NmpluLKXcVMyaRrF4OChhhA6w_8yZO3fBcSOWS3-8gG4eESAQEeLYBcdWJqCV_QnvkREzCmWgFtQdUZsh9iXJjjdcHmqBk4aTL7FkUexSuDHMaKS5GRw8EpVSwqimbEUAEfOhV6tl44PjDlhkM0n1d__5xLhamUT8tqcptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52da291ebc.mp4?token=qw-cFMhQjjwd6G4R-2X330JFmV37B4GxCcEEdIU8aO8pUSxgnT_0ARcEtXsxNDSET3P2JQFcS3YBS_-qCQugYdHDphBE0C8UvHbRMGc11jywcOqKXMjd7XjKKMvpzbXVk7J0yox5f911kTd-_sY4h4mqZb-yKTk8Wg_XIAJ2fSxN183NmpluLKXcVMyaRrF4OChhhA6w_8yZO3fBcSOWS3-8gG4eESAQEeLYBcdWJqCV_QnvkREzCmWgFtQdUZsh9iXJjjdcHmqBk4aTL7FkUexSuDHMaKS5GRw8EpVSwqimbEUAEfOhV6tl44PjDlhkM0n1d__5xLhamUT8tqcptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آچمز شدن وزیر جنگ آمریکا در یک گفتگوی تلویزیونی
🔹
«پیت هگست»، وزیر جنگ دولت تروریستی آمریکا در گفتگو با شبکه سی‌بی‌اس مدعی شد آمریکا در تمام این مدت بر تنگه‌ هرمز کنترل داشته‌ است.
🔹
مجری برنامه در پاسخ به این ادعا او را به چالش کشید و گفت: «اگر چنین است (چرا) شما در حال مذاکره با ایران برای بازگشایی آن هستید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659357" target="_blank">📅 18:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659356">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oODkHzffYytgrJQzRaTEVTzziai4apmLgHk3J0wuKPnwhoG3V5DqUdoSTNV_gWkhh5wuWw3aqVfyAjEyxzuviEEATzJdgf-0ZpcOL-UCelPQmekwIry78a8-1D_pPsyCgGoKPhodvY3xjbRVmDihxp-8_u4Xlrd71UdftAIS8-_3bLIAfa6ZltugW0K9n6XNecs2tmyjt2TmwiBZyZ-ID29gFjAmJKO2UmB4OhXZBXfiMxu72RiJ84p11VmeynBA6OQlq9iLtqE605zKwDu8sQ3xaEOCpE3RiW1vgrpow6hgchjgJHAiL8plH51ZZGqyfqPkdkfRvXFa9vg_V_xEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور ۱۴ کشور مسلمان در جام‌جهانی
🔹
مراکش، مصر، الجزایر، سنگال، تونس، عربستان، ایران، قطر، عراق، اردن، ازبکستان، ساحل‌عاج، ترکیه و بوسنی کشورهای مسلمان جام هستند.
🔹
جمعیت مسلمان این ۱۴ کشور از مرز ۶۵۰ میلیون نفر عبور می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659356" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659355">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCb7C1LkfquNIehFdciqaHS_zz5Nx4ZEyCvJBi1xnfTNTF-Vg6QJWt9BBmghQ25ACjEyWv4gjkWjzfEs9E0cmidPYVcBD9FlK-x-ldKKOOof4CkpwXMhB6CJUgafsxDHND_LGojB0Kbpa76FF9TOo4YCQ7B9vWjvpjxDrxWpHjaaHpGsYfnPmSsqpIoh1yDH0_xA7MDoa24gUJjz73tAKw4pHtqcIIirrg2VUTH8pd0Ody0dDCXKAGmP6YJ8385HmazqmIJeILvzEcqjfZnCU6RFfcRf9U5j5xpC4_EK90TaphWI1pzgQp6Y24oXhZutM1Yf550XWCKfUqGQEZJIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
ترامپ قمارباز: حمله امروز صبح به بیروت نباید اتفاق می‌افتاد، به‌ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم
🔹
اسرائیل حق دفاع از خود را دارد، اما حمله‌ای که به آن پاسخ داده شد بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندید، زخمی نشد یا کشته نشد و نباید این روند مهم را مختل کند.
🔹
نباید حملات بیشتری از سوی اسرائیل در هیچ نقطه‌ای از لبنان صورت گیرد، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل انجام شود.
🔹
این می‌تواند آغاز یک صلح طولانی و زیبا باشد؛ بیایید آن را خراب نکنیم!
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659355" target="_blank">📅 18:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
پزشکیان: تصمیم‌گیری درباره جنگ و مذاکره بر عهده رهبری و شورای عالی امنیت ملی است
رئیس جمهور:
🔹
حفظ وحدت و انسجام ملی مهم‌ترین اولویت امروز کشور است.
🔹
همه جریان‌ها باید خود را ملزم به تبعیت از تصمیمات مبتنی بر نظر رهبر عالیقدر انقلاب بدانند.
🔹
دولت همزمان معیشت مردم، اقتدار ملی و توسعه روابط منطقه‌ای را دنبال می‌کند.
🔹
با انسجام داخلی، دیپلماسی فعال و اصلاحات اقتصادی با قدرت از چالش‌ها عبور خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659354" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
بیمارستان‌های اسرائیل در حالت اضطراری قرار گرفتند
🔹
منابع خبری گزارش دادند که به بیمارستان‌های رژیم صهیونیستی دستور داده شده در آستانه احتمال هرگونه حمله از سوی ایران، به وضعیت اضطراری منتقل شوند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659353" target="_blank">📅 18:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659352">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای پیت هگزت، وزیر جنگ ایالات متحده: ما در مسیر امضای توافق با ایران هستیم و سوال این نیست که آیا آن را امضا می‌کنیم یا نه، بلکه این است که چه زمانی/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659352" target="_blank">📅 18:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_l5P8JEigYhuScuSKUFf5hOPTel0QrdE_59tvDYx6Tb3m9vNI-zo28v1MG4e0qcUK5xki_iN5oXKakkNqx0dko1KBmoBmHDQAEue16D4cVB39nZwbwKLhkF-2XxM1d59BbSHjjMPkXglk2fLHeUbxgRGiK-ZzKGtjxPBKsRtwGsWAEiTC3RVH7RblsnM3Zne2bsFcPqxhRbvASaPHWeZJoILShtFDwMd98Tif0_0l-r2TeEAe9-Dgz3Wru8T103ZMQF26Ai4sM65UOIID2z-qZ5d76foMR4I-xOu6UkmJIqbN3rUWlqSBYzCLRJmXzH11B-y37HcqFWVTXlBQWBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJZVC3zvt5x1xLiMTZc1ftzgEPAf11umzlNCn1eNFvWzGhjSGCVN3RtW0S8PSMgfQciGVZTRC313SnyFrfb09PTAvdu8GTQGvrENim4Bw6zhhRWj7Jbftw56aHm73vIdPFz79pnqAP5ppMaa5IpuRm3uo0EjuuHOQEUpf_TnF_HckmU2nOLh_EQBFSx_YsHfCvKvni4MOAFFL-BST79LAbm21ll_PUDF16TjZz3x-Uhg4b3vo4b72_O3dz0Q5UxIQ8ndhoOStF0KQyFgB6LG9vrVSnT_hYyKjsaWO1nPbKrXaYp59pwiq98UZwAvK0LhPg-tewg-45jnQM9IsSWENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDBdzbevH2OuNKpMlUOVCSwGLKMrjCqdl5202Pyq89xtrRkw1NX7w7HHdI4YVCP1zgs5D1nvabDn3V55djI6Mb-a9YqDwks56hWrTCey-SC5tR15WADN-s3yA58Enu8vcGGz9ugqVIPOR_3dOExHDwv0UaXnVowZYxWhPFAlm6IcpIHyYmVin4eLHG0Q2-iPpFogui6q5XC5jmC0jNgUwgVzXTyNRdiwxf7Ykn0k51ihblZYM0Ydc3ZShrJ76dTg5SNhWwy3ORQsxXOT8eTUewpvOROfgpR1VXF44_r9LTaHlZhNZuJvwPZwARYbM540uVxkQdO5NByXpoO8VEWzhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پوستر صفحه رسمی جام‌جهانی از کاپیتان‌های ۴۸ تیم حاضر در این مسابقات با حضور علیرضا جهانبخش از ایران
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659349" target="_blank">📅 18:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659341">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svn7KanoTEOA96Eie_YECNuSaF2F5Kfb-vTebPkcvtsFyhbnF8L-8uQoqvR_e8XCwOUApIrbReC4VZFQ6jLZ0CJEYnlYmBPNJQ_Fy2p8fJXKhwIZC8nBlukU6kHliviKxIPWz_w5XOLObhKxu2El6-nWQJvxNKJi3qh4RMhhTR2pt4i5QRsTRZ7RVzG0x1QtKimshCcDaU0Cxxs2HJJI-RZyI-9Ww1KxiaLGO7QtO0ss3E2WKZo48iANgadc1Z1Qde0M8VonLzc8vm58hGMS0FL8yTlmRYQjEbCSDsRGxtx28T3CbpJFdLfz9LOX1ttZoh8o-tZdHL8HsJesNlXnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2z9pUUz4C4L5OQQjZI_jelD_yB79OA1U9p21va3_VGAJV01BQH2JpyrdskyWvBhFviZPucSSAq9zUfeyNfVP6shRKnPnxqQuarJ0WL7JLG1XsHDyfchTNL_uoHrbrTTdgjAMn6Mn2FEPEaOJFZv64nTSQwEKy2iO6b_CoYCN1-N0uej3Qy7cCejoU1Hwxsa5dSqO0KO7QxrrzHfEXLkrBSTE7HvmfeAop-BvbNOSN6pAha9jTGvvZBPXwlL-9AoK236sYkmXMqq2p9xISfG7RFHypw69Sd0uS1olLo9ueD7sdhPQEzOvu3HIxGtFQLgyXXReHduNL4qj_n6TYZLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOe5oaYGxd1id9oqDWvC09NUmL7fZd8ZEKCJ5c5Q6oPRfRDdwCjVboliezURoRm9Ec-6OhO3iFkzAPH9jYKsdzqMQrui378BiGO4oNWvcgnwVlsF3xi3DrDLsSNdbEyF_8TZDa_MzD1OTy7jt83z_KmYWl1CpUiELRC-vvkhJq3H_XLoPK3ZNQWFfM154ZJrJ7v8vyjGHDcWND3UhLzVz9EBRmk93TS-wgdkkUr_q4eyagYh7Up7NLtOd0Gq3P5GCBdxvYg1D2my6PCqdkFkWlYUg_4zQPF-SoanSeZwWMXAu6IWFCe8XiM2XvxU9FiS717HprHzcIyFfDQmquUb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk3_IBtQcGyd-HgiKgKTrSGvKDef7HgeC-6EEVtbumMFzJ9cnIPJMpMx42NywFjG074X6dN3p2kBWm9fYGyrDXp9sVV6Tg1arqMbAAnoXpmIXN0Y3DbYRAt2xKHgf5wT2XMzyvdYqeh3D8ZHOwahQZurxb5BszRWm3noIL2c1rX1Wn7JrM3WE_AE4ffp7q-E6MHYmvPrGnHahqQEp-th2Gh8YHkUUS4vIzbN1kSXU9jzRjl2r4D6BFAQGAEnYC10hjVmbhgGrQ66umie3lwR8OA2mFrDVe9YMMVAJms-26FWqI1z8SH82Kb3vjfpray_RrhMClQ_0JCRmLs4JiGpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrTtRy6kzJj-kB2LXJziCerDYmtCsN7ZNM2Z0IhgMxq9qMZmbGlX2v2dpGZt666xCg1bHY_iuj7y5Cjr_h5k5qkiIOCVWdZDHDCbFKsrOzLlZC3ZWQMmBn-T6VCwZZPn3Ww7Xb3hhURY9M9-PFY5PPcSO9pU1OPmgZmOSpQqpNmbIDW4JaL2iHTQDqB6zBnM7CjX-gO0tond3KYEr01vy4a8VKGadu3REaNv86wjQJ3slLaBORAw5efd2mGj4GVXuuU5YiGtKif-6R2mDwapgZ1eBs0R1v9L59U3XIkTysduRmn6pDTT5f4ZH9To9x7vPR5O71an3cHE7FwnAmB0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeyxzgSnVwR8MJPyX47j4Sxy5R24xiZc9Kb8ewCSuKS_9GE8B-c0Wj2JUHn4CSuOgLN39Wh4NhwXA-0XwGcxINsGNA_uFZqOh08e6CypNc76M5bSm_PSgYCh5yT72ZO2hp7acJYcPTfvAq68Xkvc5_MTVFTeFhZD_HVUxD-i4IpJGEm8eolIbDHhTK1rVtwFyowCF76SmVviBRiIIguOkhhYPuCDnpuTz403o-OWK-K-CfFA1pteJpoiD9q-2m__9ELCJ56MiM8_oRqKn4Bty0B3S1_hdgnpDvCkXLIUuPEGwEMpshbNX906NbKUuCdPlVL4TxK4CrH_iobXcfe1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2IQVFTOU_dnMDkWpHONkZUIHdCEPTjQ6bQRRkTdjoRUD4M9b5O_utAAqQWWd45VFvgodRvdZ_snqpy0T3JyqCIbSawYq20tFkq3B65o42Sg9OAqCvF5HSypjY_Ow2LqCwaTsVMtL4BdSsBdGf6lw0pS2oSV9Urkg_momBOaUDXV9oOkr3FdVCLMRx0b2GVOHA5E_v89WLxoLvjmQ3MsATi7RYHJ3QzWIq-C4SJkrMaaKMkXrYp1MkMB8FLQwNf_Zpoo4vsjj1E_HiIteKSrzl8aLyZVPSvt60JHhMgwZBdANsT6u-nWpwUXj2EsxrBBTQZ07C6EH2xAx-CshN6U5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV5DUkYTSCzGSgzH7qiX7fSxpnqA9F-r3MXAzVkYDEZvn4-Uizct6UXi_Xsb1qT4HHl3bGgNQfkcTkU5j_OKhXdH-pNi6c-aJE3wNYDkLTCXs3j_y8pQnlBd43P61WKD46hK8BP61jC2gLhMVcyqvGyRFvKFsU8bzcZZrHCukTb0qBlpiktl5caH-ghQPPYXDCfxCT3XZoHqDn2vqcz7od52CWCegjHGdOs2CkhQLqgTaXZpjEWSjFmao77A-e2M1AqzvkW2rN437IPigVmeKFrkYzFyYDpsiQ4G4nblyDknE0Fcro-ME8w-6ekDguz3D5yfj0fxhGmadLN6DZ_67w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همایش تخصصی «نقطه تصمیم»
🔹
گزارش تصویری از همایش اقتصادی نقطه تصمیم به میزبانی هلدینگ تبلیغاتی رسانه‌ای باران در مشهد، با حضور احمد جانجان در حال برگزاری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659341" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659340">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nADj-x52yZRm7VNmRBhQndjzx8SGBZgfExClxqMsKIP20CTt-ynTnfQnbVUq6bPgYQYywwGtqpWGTngLXU-pgFZYsNNlUcY6UrWVw60o2epPF3JnCAB8SSpd_C5-lTQlfKxNc1snAJIoIoXG1013LV9jNwhhetvD06PIMJDFibZPmZb-DYfybAgUKOH-YFgQ5oXhW3-sYPDvZCjP_4uA7v-ecH2-iPwU5QdVdA48QeH0crm8dynOkVYGq2CSZe0qQGcPAhPeONSUCqb9mYH23WW4W7DMzqUY16wZ9jn89PVflldXUXH1NzWiN5qUlQ9quFvr_PuPpE1_qF0EsQsByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزبانی زیر سایه ICE؛ فستیوال فوتبال یا دژ نظامی؟
🔹
کمال شرف
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659340" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659339">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dlvetbt8RgT_6VtOWllYATxXrTRACWJD93pmm5YXigc-lWfKLEwF-1pU0ciFnFA1EBgW3yj1CHtDrIMXMgE7AycIQyWm0H5zINmfKDV9M6GZ1CL733iZ1aptsjukYbP57QXV5LP6CKl-pfLN8pGSnZItbQVqD1crgexf9fhOktPGy_f3T-KKliij_4AJvJHDMCAb-NA1HT8FEnioXzzqdvCOPrjDghv7mIisq1JgyYQA3EBD6sQILirpTCubTnUWr3x5HT0e5Xhm9oLZrSGgqapdDPheWFjPxtyiNTyE-HqHVRFuEhqM1bwi2OwbZtlpeNxD2mTYhOhQr9tknlhGfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم‌تر از پایان جنگ، نظم جدید پساجنگ است، چیزی که رسانه‌های خارجی بیش از توافق درباره آن تیتر زده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659339" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659338">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
آماده‌باش ارتش صهیونیست‌ها برای حملات موشکی ایران
ارتش اسرائیل:
🔹
در پی حمله ساعتی پیش به ضاحیه بیروت، خود را برای حملات موشکی ایران آماده می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659338" target="_blank">📅 17:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659337">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
احتمال شنیده‌شدن صدای انفجار در بندرعباس
سپاه هرمزگان:
🔹
روز دوشنبه ۲۵ خرداد، عملیات انهدام مهمات عمل‌نکرده در بندرعباس از ساعت ۸ صبح تا حوالی عصر انجام می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659337" target="_blank">📅 17:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659336">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ae2908bdd.mp4?token=RXdzxyu5GYTRgGDUKWmc-LZEAhpVRKE38t_WBPjgDeUroq_iKdtXkb7uvgSqMCnPcKRTIB9gBw4nnmGMDp47C5ENs5h218sZMtCyau2DpXUYmaeMgBpB0EsBotGbmiMvdd-ba2E4jGEQvnMVibURNUQDSk2Br3UjLmHJ3uJyDHnNr3LgR7Krno0ifurF-42StXEhraozL7V_1P_G1lt-S2KxnXqIRmC0OiDMzB475SvLRbqdM_qdkzlAjkN8W1bP6hgDEVwEf--aLNjJeYMFZ4m-fYrwKVrnSpfEHeVdxDZV4cR1qeL0K-7R3xkg3V7exc-8eBvAlfq2xOkWKmv1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ae2908bdd.mp4?token=RXdzxyu5GYTRgGDUKWmc-LZEAhpVRKE38t_WBPjgDeUroq_iKdtXkb7uvgSqMCnPcKRTIB9gBw4nnmGMDp47C5ENs5h218sZMtCyau2DpXUYmaeMgBpB0EsBotGbmiMvdd-ba2E4jGEQvnMVibURNUQDSk2Br3UjLmHJ3uJyDHnNr3LgR7Krno0ifurF-42StXEhraozL7V_1P_G1lt-S2KxnXqIRmC0OiDMzB475SvLRbqdM_qdkzlAjkN8W1bP6hgDEVwEf--aLNjJeYMFZ4m-fYrwKVrnSpfEHeVdxDZV4cR1qeL0K-7R3xkg3V7exc-8eBvAlfq2xOkWKmv1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمعِ سلاطینِ فوتبال در یک قاب!
👑
⚽️
ویدئوی جذابی از سلاطین فوتبالی که در شبکه‌های اجتماعی در حال وایرال شدنه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659336" target="_blank">📅 17:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659335">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8f70e9f0.mp4?token=ak8_EOkCRlrG2GymuxDCS8sZVJiMldyx6sgPueO-VzKsi-ZRQkjAPPaOFexOCasZ8Lwf4mjyl3YR8_7UgMJkTSZKB2UvizMwo8UtOxdoCJ9yggOmN0YIbgsPUCcx_WRSv9vtJy1otDs6QxJ_4ZIQUPRGaXEd7tQ9RlcqxjTvcFRoLXI4NmFhcmyjyWwkzsolCBS1CN7aO_7YcYUZIRCdNihiQxPU7P_zmLHeOp2_Oh-1XoNi4icdt2KK6rJP40EL76GKGZvNz4_u7WzWIg8SkJoqsRYYk9rfIGrI8N-aJxOaRcqsZBpy09LLupWq9fkvj3pc7XzwhNbyS94OMrmBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8f70e9f0.mp4?token=ak8_EOkCRlrG2GymuxDCS8sZVJiMldyx6sgPueO-VzKsi-ZRQkjAPPaOFexOCasZ8Lwf4mjyl3YR8_7UgMJkTSZKB2UvizMwo8UtOxdoCJ9yggOmN0YIbgsPUCcx_WRSv9vtJy1otDs6QxJ_4ZIQUPRGaXEd7tQ9RlcqxjTvcFRoLXI4NmFhcmyjyWwkzsolCBS1CN7aO_7YcYUZIRCdNihiQxPU7P_zmLHeOp2_Oh-1XoNi4icdt2KK6rJP40EL76GKGZvNz4_u7WzWIg8SkJoqsRYYk9rfIGrI8N-aJxOaRcqsZBpy09LLupWq9fkvj3pc7XzwhNbyS94OMrmBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در چند دقیقه عیارهای طلا رو یاد بگیر #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659335" target="_blank">📅 17:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659329">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRoVGuZAGrlfEPIovcPb2Vu9qg2IMYpCJjms1Sbo5xquGhmemXElxrygSVtjDFsZdPPygeKknw5xI_3_88Wr6VlJ6P1Qpan3na0fscqzIg2dwZvYvgb3-VZkCSf10-FH_ITiOq7WtjTt7QH3FUTaqsMwuna5iZBoAGKP--X2sYOGoTung5xbIxuVl8TEKHi7AOoI7XC87GKmxbDYPsqs-Ax1LDmMZd5yBRc1WMtxNwt1FfESOntLLWaLEBhOVYoHBdSUh0oWW7YGFN72aqL5aiz3hA6264HeUPev0jkAeUnYbL6IHwSLSh-Mc62ZfUlDeth0kM3GIGBQPsK3rgif-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpdMsN9isUIFpZ00acTCsaornVJf3Zk0QixhJhvbAnM5s1iNLCMqt7zQV9yWM9QyxB06Ix419sAhu3JUK0ZHU3VUVZTR51xeYo7C0WwfFTwyE4YhiER9eBh4fZFJxrBnkhGNoh9ie8jGcXduBOEE3X-pJ5boS0wlEGY3lW-xPhycFYM_cfO3JQlT0rPT8wKq67JzyjfEQIlbEaAXz1Lfrymt63uC3OBMgqO-dgPy6I6pwfsMBadUU9ox8m0zmEY0L2mT9O1sg_vNAG072WqLlL7Ud-bS9fRTTZn4B4nJ5-n1ONi1Pxj2ZU5iv86NhIWBSOiFmSDv4Lz-Hqlyqctkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIAXieh3mrYf3_5D0a9ZVpPSyveg9htoVXoq-h0x4MJ1zawLFDjSp6VsWKzj2aL_0dIQ3TRebIev4hS1JIOa9zPMr-Ydv1VDkGVL4Ik37NPm57autQAB_VuDRZjB2OB4ZhXeVW99hCf1FpX-wMSmqrQloxH462OkqeJat-joZ4pNjOtj89Qlstdfu08hI_1uLLs0-uHytZ2QoCaGXgv-3o2lXsTcl4mk_gazfKiEyAM_yA7Uu7pPuw1XmPMNt1-TdgamWf1ydRF2Gvsc2Yydk4CE6vSvXC_R5PG0f3XRm26g8DIB6RXn1FsR4giCWneAxFr-L9UCu_gJAeoi1biO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5U2vpAaWw9810qZWQLsARYfG3XfvnrhVzpQXNmq1bk34XbkHFCKy0D7aEfnQLhXrKoc0PtoSRJ3Aj4VW0dnLUFLFypR433cPU2BbZUB6pEqt4LsfOQWHP6ycVs_g1yKk2hEgz8LDsc2rzBt2aK7bFxVZWc9DjG2Zwr-ErUG2MrLycPXbpf4cv8W6YO0K1Dtca0JCUHPCJKBf4PURBIW4-LUQX6xl7prJ0UdLx2skbIzeyf2xRZ9hpkk5cv8SXhpSo4TCL_3MxY-XFhgFo7X9WbN61l-26d0u2p4fSN3TLB3ZWk3GE5UC81dM9v7BOFBHQ8ZGy12w5v7kYDSRurYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCD3dUE9Ohj6CPr7ObRletMXKebNnVi2h5GX7eN8kx6qKior7oG570gbdGSwLqHefpG9YV1eZ4KRHtijWVXzIIHAOwvpIaA39TdUictu6BR5dcHYwb0DZYxoQb5RFbnXHvWMT3x8HKjhonOmgIYipaa7SMET4OxsbuscKxZFoqMpY1huD_1lLJtxptnvFp0QNoH7y3JQrcw57DGRDSI8vt1EFgV7lBl__sMMUBFkaUFa5q8xhrlefGo3mGAUsssZDv2xXQPkK5HcmN5hQXHKhKnQafvqZTKXLuSzRnjdGjybzOyJ7h_EytlMhVgxyp-gqfn5_YSyypinUIUpJ7SxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfhfFR-u6r0TiEkn56k6HYdb98GYwlFznpUxV0L25k34F0p4O29FoVD_H_Qz5X01vUtkW0MosS69Mc4TfZBhMW6zdjhETh7bAUEHDxOXHTHjGdV7OXyIEtl2PysB_ZJd4ik1ylZC-ugIMgupJN1D5zF_QIh6q8RXb2V8EoLjwcu0Vel5FSJ9_1PwWGD8DiUVBx8XM9MaFshP5gIfg9eoUW5zm0gcuddTe1NgDCdPoe6E7WMkjgD7Ce43lrChGfIR1sq8AUPU5LPBFRSeB6lzz-tRU5s9YuRUQy8XiCIVq_cc7TkkeqD0XSMC7hH-YTjGrCBtVjqcnKlRJbtX0iX2bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همایش تخصصی «نقطه تصمیم»
🔹
گزارش تصویری از همایش اقتصادی نقطه تصمیم به میزبانی هلدینگ تبلیغاتی رسانه‌ای باران در مشهد، با حضور احمد جانجان در حال برگزاری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659329" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659328">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون وزارت کشور: دولت برنامه‌ای برای افزایش قیمت آرد و نان ندارد
🔹
وزارت خارجه لبنان از اسرائیل به شورای امنیت شکایت کرد
🔹
اوباما: آمریکا باید درس ناکارآمدی جنگ را بیاموزد؛ با بمباران به نتیجه نمی‌رسیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659328" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659327">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOj5OjfhbsIUcy_oHDNVWwwV167UEHDObyWIQqd_mxvNvrSslwrkZs6_AXRUkhCn9bsSb_hXS5cD3FIu8v7GyrVxmwh7ASKXrUai1IOK28ZvAKqyULK1vetIWc08jcBd4qV9OvxSbvlAC5DnHomtDehFUblm19UC6Eb7rdnZMSf8zoshKay50w9kJRiNhlia7f91PsRsJfvkpftWUodRB6xo6OwScgdDYZ1exRpAZ9M_I85LHvBGxxNwzZhgJ2oYSlbMFGnkdUlvWWMSNNcCr_8NOR_tPqGqoj-WkDjV6GPjE5aLlLEsV67Ktqkne3nnmkqFheTQte4BeO1i8KeyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال اخراج «تریتا پارسی» از آمریکا به خاطر جنگ ایران
🔹
دولت ترامپ تحقیقات برای لغو اقامت «تریتا پارسی»، از منتقدان شناخته‌شده جنگ با ایران، را آغاز کرده است. فعالیت‌های پارسی فراتر از یک کارشناس بوده و ممکن است بر سیاست خارجی آمریکا تأثیرگذار باشد.
🔹
پارسی، ۵۱ ساله و ساکن ۲۵ ساله آمریکا، متهم است که آگاهانه یا ناآگاهانه روایت‌های جمهوری اسلامی را در واشنگتن تقویت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659327" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659326">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
منبع آگاه: تیم قطری برای پیگیری مذاکرات در تهران حضور دارد
یک منبع نزدیک به تیم مذاکره‌کننده ایران:
🔹
تیم قطری در تهران حضور دارد و تهران دیدگاه‌ها و جزئیات مدنظر خود را از طریق این میانجی به طرف مقابل منتقل می‌کند؛ هنوز هیچ توافقی نهایی نشده و حتی در صورت پذیرش همه نظرات ایران نیز توافقی در زمان اعلامی ترامپ امضا نخواهد شد.
🔹
این اظهارات ساعاتی پیش از حمله اسرائیل به ضاحیه بیروت مطرح شده است./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659326" target="_blank">📅 17:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659325">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f086bda5b0.mp4?token=SIFu3ruAO16ZCOpC4kStbA8jHomt7m9b8gFXuqc-l98e2FyzGqErtH2jPM1YAnQTA9chyamqdzHhdC3mgmw8i-CsURKQfTtF7dfyU_9cDgkyWVETIipyxl_xNQtdp1bH9oTLOCpYJc4Dt49XHIuP-wqbLtmE6zOb1RGgUdgpGTLadQg5oBKQ5M8N3WiAgVlUjYuPMV51HVEaQKRXbc3KLdi1q7T8RCf_MrRX6wtGygYOawDNnz3yF-5dvcnCoTvJP4KeatX2rSvTAJy_vrbQWapGcbAWV0A3deK3dPrl7llG6qcbpJXVzbe-DVOiq5Bwo-3iWVSAIlzNj40iD5utEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f086bda5b0.mp4?token=SIFu3ruAO16ZCOpC4kStbA8jHomt7m9b8gFXuqc-l98e2FyzGqErtH2jPM1YAnQTA9chyamqdzHhdC3mgmw8i-CsURKQfTtF7dfyU_9cDgkyWVETIipyxl_xNQtdp1bH9oTLOCpYJc4Dt49XHIuP-wqbLtmE6zOb1RGgUdgpGTLadQg5oBKQ5M8N3WiAgVlUjYuPMV51HVEaQKRXbc3KLdi1q7T8RCf_MrRX6wtGygYOawDNnz3yF-5dvcnCoTvJP4KeatX2rSvTAJy_vrbQWapGcbAWV0A3deK3dPrl7llG6qcbpJXVzbe-DVOiq5Bwo-3iWVSAIlzNj40iD5utEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد تخصصی «نقطه تصمیم» هم‌اکنون توسط هلدینگ تبلیغاتی رسانه‌ای باران در حال برگزاری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659325" target="_blank">📅 17:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659324">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قول مجلسی؛ امسال در هیچ شهری مشکل آب نخواهیم داشت!
علیرضا عباسی، عضو کمیسیون کشاورزی و منابع آب در
#گفتگو
با خبرفوری:
🔹
امسال به لطف خدا افزایش بارندگی داشتیم و در بسیاری از استان‌ها بارندگی در حد نرمال یا بالاتر از نرمال بود اما نسبت به بلندمدت پنجاه ساله هنوز فاصله داریم اما نسبت به سال قبل وضعیت‌مان خیلی بهتر است.
🔹
در هیچ شهری از کشور به مشکل نخواهیم خورد اما نباید بی‌رویه آب مصرف کنیم و نیاز به مصرف بهینه و بهره‌ور داریم و در بعضی استان‌ها نسبت به سال قبل تا هفتاد درصد افزایش بارندگی داشتیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659324" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659323">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6Zh2aVm4Mxz98O-zBljZGcH2jugDFCr7aQ8IhDUHy-72K8Q3Vs9ecVYQglveyUdRR-Bh4C7TsCXrc29RssrAI1TyEj4OzS5xmFylwJV0MOhp-CvdUlzbMii4NWU9li7U91ihXtYKJVn-h1pokRTUp8NCIEonkjLAsZKpO4987oZHT33Y4tQ2Ijla-Zi4ZmdFrLSxQW7cMCk0IU5oIqyUF-ybfFMlEYoZv79T0Wm3MfbT9pt9UH-NF4pnzpw6OJgw3V7ke4PyGgOtQRcNeZeBexlYPHs3m3-6R3ijbJT4L4hi7duJx1RDfpC6xe3BUuT-2TwoY1tnWoIl_nwjRXztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: فعلاً مذاکره دیگری در کار نخواهد بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659323" target="_blank">📅 17:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659322">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای آمریکا: می‌خواهیم امروز یادداشت تفاهم امضا شود
سفیر آمریکا در سازمان ملل در مصاحبه با ای‌بی‌سی:
🔹
رئیس‌جمهور ترامپ و معاونش کاملاً به امضای توافق در همین امروز متعهد هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659322" target="_blank">📅 17:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659321">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX_sjJSVukP6zzgy3s5f0K5DxkbZGA01G1jjpuIw6QDvY5_HeIzTAwnDgVp6lSJiVDW40nv5a-RO-vIkboxYcJ_WLA9d5x1tFfh07q91JFguqQhP8LMpgUEQX5vL5Qm9uzhsJK3Vjdu_wdNRfIB_KkdMesg9wzxoC_mwhJ5cPWhWcBXrV_c9Euw5NXNUxlQh0TiRAicqreLVbQk8wnlBaLAb5t3o5gtLj3yZ1lks1R0ZZ_2tBTk_SRisfD0dRKAWVWNBXocUX4Okelx8iiNRQwcGEobiHMTZU60zJcoER5m3VKlRky6Utln8N4FOTPJdXLvyxcvNbIvW8tAsznS0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال لیگ ملت ها؛ صف آرایی ایران برای بلژیک، امروز
🔹
تیم ملی والیبال ایران از ساعت ۱۷:۳۰ امروز در چهارمین دیدار خود در مرحله مقدماتی لیگ ملت‌های ۲۰۲۶ به مصاف بلژِیک می‌رود. #ورزشی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659321" target="_blank">📅 17:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659320">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تکذیب شایعه ترور شیخ نعیم قاسم
🔹
گزارش‌ها درباره ترور یا زخمی شدن شیخ نعیم قاسم تکذیب شد؛ بر اساس اطلاعات منتشرشده، در حمله امروز به ضاحیه بیروت «حاج علی موسی دقدوق» معروف به «ابو حسین ساجد»، از فرماندهان ارشد حزب‌الله، به شهادت رسیده است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/659320" target="_blank">📅 17:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659319">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوهشت - دیده‌بان رشد اقتصادی ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d47fdce55a.mp4?token=eA_7mwXpLgIX5hEMiCv1fqgaY3FUZ5T3vIn1lA3YVPSEDERo_CD717pzPE7oBUIfWeK3fKCwGFkdKdLFN6MZJxdBTyiUPlNIkTaEUtugeS4zNigoHtRaxqFmxgl31GnQSV2F07HUdobI-4wyUbLUkU900ODkHGGWhVzmQoGcSM15QuQe8Mdoeg5WJ2NSWfcleC7usflRFf7L5yLAyQ3DjDAFetCWzXhSzbsbFr2CGOWAzQHzy-5KBEHP_l3BYfy6JeCsqTpJhsMmDJG_p_XRk02KgduJoGuWAYh0BTENTdBt41PdVfaDNMCluIb2K8vhwCWKgVBCN8GoyiNT2MFjW0x1wsvAkEZkvYCLPSMScQsB9gKRHNz_2_8fh-MsT0uan6i3VC8zdUEhqIRvsLiu0ScjZLCfAoy_juNLOfe3HWwU4cRKXDMzEQ_DJgH2pXNnxf9T0NAZjswYtlAKg2aaP2sUVk1z9sXFWFXqfvZIgfJ5jGhePwPcOmn6OTF_Jl2DzBmjRU0heemRNaLVrPrxYDC_nc_vvQKWvNoxC2Q9btxh2O6pFhB5Pf8y5cFqtRhCCqP_hEnyN0MIlppXp1nb73gwyA-AqCfgyWG1oDBoFU2eSE_lJIlIfJn7MGozrutmkPb8tvetRv22K48_oAIv_Mie2sKF30lWg7V2IskGOQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d47fdce55a.mp4?token=eA_7mwXpLgIX5hEMiCv1fqgaY3FUZ5T3vIn1lA3YVPSEDERo_CD717pzPE7oBUIfWeK3fKCwGFkdKdLFN6MZJxdBTyiUPlNIkTaEUtugeS4zNigoHtRaxqFmxgl31GnQSV2F07HUdobI-4wyUbLUkU900ODkHGGWhVzmQoGcSM15QuQe8Mdoeg5WJ2NSWfcleC7usflRFf7L5yLAyQ3DjDAFetCWzXhSzbsbFr2CGOWAzQHzy-5KBEHP_l3BYfy6JeCsqTpJhsMmDJG_p_XRk02KgduJoGuWAYh0BTENTdBt41PdVfaDNMCluIb2K8vhwCWKgVBCN8GoyiNT2MFjW0x1wsvAkEZkvYCLPSMScQsB9gKRHNz_2_8fh-MsT0uan6i3VC8zdUEhqIRvsLiu0ScjZLCfAoy_juNLOfe3HWwU4cRKXDMzEQ_DJgH2pXNnxf9T0NAZjswYtlAKg2aaP2sUVk1z9sXFWFXqfvZIgfJ5jGhePwPcOmn6OTF_Jl2DzBmjRU0heemRNaLVrPrxYDC_nc_vvQKWvNoxC2Q9btxh2O6pFhB5Pf8y5cFqtRhCCqP_hEnyN0MIlppXp1nb73gwyA-AqCfgyWG1oDBoFU2eSE_lJIlIfJn7MGozrutmkPb8tvetRv22K48_oAIv_Mie2sKF30lWg7V2IskGOQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
با این رویه تا چند سال دیگه ما قبرستان پنل‌ها‌ی خورشیدی خواهیم شد!
🎬
نسخه کامل قسمت ۲ برنامه
#نمودار
را در
یوتیوب
مشاهده کنید.
تحلیل‌های به‌روز اقتصاد ایران را در
اکوهشت
دنبال کنید:
@ecohasht</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659319" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7171K0_44xhtiuu01CgODpiqM1hvwPvkMqtIWSuihIRDYv1PMo_ZJ1dpIM3hbaQvgMiRNlC9ApHlTSBj3XcrerCKx3994l_ISxYSfKq6DZ_N909D9GsrlolelT-xWmmcG7IwDsAWMXIy6KzsvO56bMsNDRy9-JgVFPeRmv-a5k-9JqF_C5WOP-WXEMx6tZTUboWkogKz4r3nkWyWmHqSAHP_U2-hZW0L6Ln14r-nsYSjkflC3PxXp38BR6GT5lSmEXdzY9YdPyKi168mvTXtQk806Jp2Q-Ce89E7rB1mECvLTvlzNRZhU6tb4zh7T_g0QYMSFCZri_sB6DGvcv_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فواید اهدای خون
🔹
هر روز در بیمارستان‌ها، افرادی چشم‌انتظار دریافت خون هستند؛ بیمارانی که ادامه درمان و حتی زندگی آن‌ها به حضور اهداکنندگان خون وابسته است. با یک اقدام ساده و چند دقیقه زمان، می‌توانیم نقشی ارزشمند در نجات جان انسان‌ها داشته باشیم.
🔸
چرا اهدای خون اهمیت دارد؟
کمک به نجات جان بیماران و مصدومان
تأمین خون مورد نیاز برای جراحی‌ها و درمان‌های حیاتی
ایجاد امید برای خانواده‌هایی که چشم‌انتظار بهبود عزیزان خود هستند
🔸
فواید اهدای خون برای اهداکننده
کمک به تولید سلول‌های خونی جدید در بدن
بهره‌مندی از بررسی‌های اولیه سلامت پیش از اهدا
تجربه حس رضایت و آرامش ناشی از کمک به همنوعان
🔶
اگر برای اهدای خون اقدام کرده‌اید یا قصد شرکت در این کار خیر را دارید، به ما پیام دهید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659318" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659317">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f10a10f9f.mp4?token=kP0ZeIuSipCgqYjFEK9zT-z9zUCF6PbT3FHbfZ_Ws53vRNwctiyoODjT_nJGA-OANOUKXHAPXdx4g3zpCq-AZcWTuZ1XOcvGYRWGatxuLABHETtiEJTIRaovP-T7-3WiF9dkq7Q4lk_Wigi8hKnEsmSjtiFm9VGzCJ8Ow9xHXah29WyZgmFu72nMa_kRK2UBMwc9mxL9-BiN94isMZrvWYI9iIIWpXX0h1_8ukeU5tM54AhDZXKSVVfs-tTgvPjw18SVEwtH6hqHA0bJTXnmA9pzDFx2SNot48MVZT0phuAlzg-4QSo65-cdWYgqnjyAijD772aZWTm_vFymaXJW6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f10a10f9f.mp4?token=kP0ZeIuSipCgqYjFEK9zT-z9zUCF6PbT3FHbfZ_Ws53vRNwctiyoODjT_nJGA-OANOUKXHAPXdx4g3zpCq-AZcWTuZ1XOcvGYRWGatxuLABHETtiEJTIRaovP-T7-3WiF9dkq7Q4lk_Wigi8hKnEsmSjtiFm9VGzCJ8Ow9xHXah29WyZgmFu72nMa_kRK2UBMwc9mxL9-BiN94isMZrvWYI9iIIWpXX0h1_8ukeU5tM54AhDZXKSVVfs-tTgvPjw18SVEwtH6hqHA0bJTXnmA9pzDFx2SNot48MVZT0phuAlzg-4QSo65-cdWYgqnjyAijD772aZWTm_vFymaXJW6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنون تماشاگران آمریکایی در میدان تایمز نیویورک
🔹
پس از قهرمانی تیم نیکس در مسابقات لیگ بسکتبال حرفه‌ای آمریکا، در خیابان‌های نیویورک، هواداران نیکس در «میدان تایمز» دیوانه وار به تخریب اموال عمومی پرداختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659317" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659316">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbe41861d.mp4?token=AoB-U_MILzGMGAbIfpqjjhKEJi-mor_ILEtFAjs9A1PFzRmBJ8AmWzdwoDOx1CjGUhCdwVTAas8eMT4j-IsYUcWQwzPE12DxxyTjw7OYlsNQOtnarAyQ6MH2b9AYq9DW9SuQLodwkDDPLb8PhkY1BV5KL8-fRWkUQHE9opbxjPeoyNdj5sXdmAwJthQZoEdaY3fg3lsYzrk07_uCXf5N-yxgPEW4meCDbOppSy269vKqu4lU1kwPqC-m5CHJF15htxFWh0SVRrSm5rStFapDHPWvZLkLWNpEh9KUGC9stXgZ8SJ5FCB-HU1Q4-G3CDQLWx_xQXg-y_InrJ1a2bDqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbe41861d.mp4?token=AoB-U_MILzGMGAbIfpqjjhKEJi-mor_ILEtFAjs9A1PFzRmBJ8AmWzdwoDOx1CjGUhCdwVTAas8eMT4j-IsYUcWQwzPE12DxxyTjw7OYlsNQOtnarAyQ6MH2b9AYq9DW9SuQLodwkDDPLb8PhkY1BV5KL8-fRWkUQHE9opbxjPeoyNdj5sXdmAwJthQZoEdaY3fg3lsYzrk07_uCXf5N-yxgPEW4meCDbOppSy269vKqu4lU1kwPqC-m5CHJF15htxFWh0SVRrSm5rStFapDHPWvZLkLWNpEh9KUGC9stXgZ8SJ5FCB-HU1Q4-G3CDQLWx_xQXg-y_InrJ1a2bDqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنون تماشاگران آمریکایی در میدان تایمز نیویورک
🔹
پس از قهرمانی تیم نیکس در مسابقات لیگ بسکتبال حرفه‌ای آمریکا، در خیابان‌های نیویورک، هواداران نیکس در «میدان تایمز» دیوانه وار به تخریب اموال عمومی پرداختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659316" target="_blank">📅 17:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659315">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
رئیس ستاد ارتش رژیم صهیونیستی دستور تشدید عملیات تجاوزکارانه در جنوب لبنان را صادر کرد
🔹
ایال زامیر، رئیس ستاد کل ارتش جنایتکار رژیم صهیونیستی با تأکید بر اینکه لبنان در حال حاضر «مرکز ثقل» تحولات است، از برنامه‌ریزی برای گسترش حملات به حزب‌الله خبر داد.
🔹
در حال آماده‌سازی برای تشدید حملات و تعمیق عملیات‌های مانور زمینی علیه حزب‌الله در جنوب لبنان هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659315" target="_blank">📅 16:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659314">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
دستگیری عامل مرتبط با موساد در ایلام
وزارت اطلاعات:
🔹
«علی.ح» که با یک سرپل وابسته به سرویس جاسوسی رژیم صهیونیستی در ارتباط بود و قصد نفوذ به مراکز داده و سامانه‌های حساس کشور را داشت در استان ایلام دستگیر شد‌.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659314" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659313">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d10200809.mp4?token=RCAnypPjww4ZyFEQr9Zj9TjUsZUx-vBMGP6p65bZwaIANsK-eDK4L3OBqrA2oYRYLJIDdwZA9VyIk1XEHQFnjx607T4WB4LLX3A31Fo5ATIjoIh3gqV7rJYE1y0dyF1A5HWB8bCeqPXp_IwK_ba5GnKXkSc6L59_WJ0K-rwKLgiH5x-Ic9PsiiFN-heaDicXrww_GXdVTu66rTj5Qqm5in1r6LnZenQDOYbxD-znc4qZmfOdQMzgD7AnqbGkUUtgDIZ4PfNtnJg7RuNoBIdjz_GTgf8Xj7lVNmJO_rgF-51m1vYNlD1Tyt0GTxIeJ1RQQyipzajBPnOZAehDWDZ7og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d10200809.mp4?token=RCAnypPjww4ZyFEQr9Zj9TjUsZUx-vBMGP6p65bZwaIANsK-eDK4L3OBqrA2oYRYLJIDdwZA9VyIk1XEHQFnjx607T4WB4LLX3A31Fo5ATIjoIh3gqV7rJYE1y0dyF1A5HWB8bCeqPXp_IwK_ba5GnKXkSc6L59_WJ0K-rwKLgiH5x-Ic9PsiiFN-heaDicXrww_GXdVTu66rTj5Qqm5in1r6LnZenQDOYbxD-znc4qZmfOdQMzgD7AnqbGkUUtgDIZ4PfNtnJg7RuNoBIdjz_GTgf8Xj7lVNmJO_rgF-51m1vYNlD1Tyt0GTxIeJ1RQQyipzajBPnOZAehDWDZ7og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم زنبورها پرواز هواپیما در مکزیک را به تأخیر انداخت
🔹
تجمع یک دسته بزرگ زنبور روی بال یک هواپیما در فرودگاه بین‌المللی کانکون مکزیک باعث تأخیر بیش از ۴۰ دقیقه‌ای در پرواز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659313" target="_blank">📅 16:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8df3566a9.mp4?token=kpB6Tc-JcPHqZt1yn2-3IdDt4L1I2UCoDtg_VICnNlOjzKbxaCfRqoVaywXv9CW7qKmMYnomCdhZCzmyfbpyNf2_t_begRmB_6fwZK56IJ3TwM7VZfryMtjCSFLQALffgW4nXGEm9hDxVnr9gLmaTl3y1UvzDbKJ6wO05Xqbz8Qj1dR--8VlpRgbM3v7RiW6ZI9gNX4hZPKOkDec0xALRSpHTh2_rLnuoDrV0bXyN0wLe8C8_N4soFSuQ0AuDx0s2fZ0D2ukY6wG3HwREFPIrh8xO8KCIDtZ5ty0SKBrkZyvysez1elaT_itoBQeq8G-VQklZzRFuqP30NnT2f-PwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8df3566a9.mp4?token=kpB6Tc-JcPHqZt1yn2-3IdDt4L1I2UCoDtg_VICnNlOjzKbxaCfRqoVaywXv9CW7qKmMYnomCdhZCzmyfbpyNf2_t_begRmB_6fwZK56IJ3TwM7VZfryMtjCSFLQALffgW4nXGEm9hDxVnr9gLmaTl3y1UvzDbKJ6wO05Xqbz8Qj1dR--8VlpRgbM3v7RiW6ZI9gNX4hZPKOkDec0xALRSpHTh2_rLnuoDrV0bXyN0wLe8C8_N4soFSuQ0AuDx0s2fZ0D2ukY6wG3HwREFPIrh8xO8KCIDtZ5ty0SKBrkZyvysez1elaT_itoBQeq8G-VQklZzRFuqP30NnT2f-PwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جذاب‌ترین گزارش فوتبال
🔹
پدری که برای فرزند نابینای خود بازی قطر و سوئیس را اینگونه گزارش می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659312" target="_blank">📅 16:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای شبکهٔ ۱۲ رژیم صهیونیستی: هدف حمله به ضاحیه فرمانده واحد ارتباطات حزب‌الله بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659311" target="_blank">📅 16:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
پیام پزشکیان در سالگرد جنگ تحمیلی ۱۲ روزه
رئیس‌جمهور:
🔹
دشمن صهیونیستی با وجود ترور فرماندهان، دانشمندان هسته‌ای و حمله به زیرساخت‌ها و مناطق مسکونی، در تحقق اهداف خود ناکام ماند.
🔹
جنگ ۱۲ روزه نمادی از انسجام و وحدت ملی بود چرا که ملت ایران فارغ از هر سلیقه و دیدگاه، در دفاع از کشور یکپارچه عمل کرد و دشمن را به پذیرش آتش‌بس وادار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659310" target="_blank">📅 16:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659309">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
حمله پهپادی رژیم اشغالگر به نبطیه لبنان
🔹
منابع محلی از حمله پهپادی رژیم اشغالگر صهیونیستی به شهرک «انصار» در شهرستان نبطیه در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/659309" target="_blank">📅 16:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPtlV1iAvEyJmelka_iaxGxeam0Y1La363chwfoAEROpHsg9jztGjbsyHoqRMeylUnD3t8RaIFf9_IYRoI1BH2XCzILdaifyRkRbYtQx_54aaExiwCgt5eFQsWxxdS7t-mMdeECn2P_zwNh3LIG-FjOdVlE5aAALcWMzxJ91Yq1NW5s48K7xKP2YS9kgUAN1ha_slZv9Rl90rLI7My1Wuz93hx2VAda3kpLTnYWsoDXB_GQkeYPxu0Oo8fUTM4xqOdySESj1LVKojJunla7S-oSz0AbHsFj_aitnA_ZVCfZ1IyhKdDm0HMhHKkNvPKxJFPOljjo9ZKUCnyGie_xzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: پس از چراغ سبز آمریکا به رژیم برای تجاوز به ضاحیه، سخن گفتن از ادامه مسیر ممکن نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/659308" target="_blank">📅 16:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659306">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDfqRZkv6j2PqHP1peU7uNFnHcGLNO8Qi9ZqLu3O5hkj6MB5UOvFvg_l-EWv9VPf4OrfShqfl6MgZjL1_EagIw89RC9n1TAj3Pv0GCUlHT23_fp-4b2BlLFWphlCxaPyHV9n2e6XU8S_6O4TJC2-Me_axL7R0OC1TMnXVaZplh8VjTdIIP0wu0K1v_9t-HrxNjpP38CtOTu4apM_M-EkjAOwc-Tsxtl3qT-HoKaoMQSFPLv-1PPekrGNPvy3unH1OG_pHjoRJp37G9rVIgt2w066Yr5-mhUhO883CYptJK5IGCT9nTeki277HsCpB1-dQtxNQdyXnxH5I9hhTjfAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXRCocIws_d0bVqIltTAcig_--8x4n0eaddtqEty6xB8EyTyrzh3ghho8DyUPNpV7VOVuH14ey9vZ304URYhfKiz7KpD1Yza1sTUtYoa4cIvZk6FA4aS_wgLBjpezfv_ik0dF68hYuH_hw3PnCyxzGsyxdNHYq5s59wuBhZGq5fmvmIp7JB0PuJwDPjmL2YIpJK0zmcxTb4KC52dRkkZmNErzIZFoNFucWo-s392ZRcDnD0geiwgC2ZPhEoIYYACuXgc3QstJqp2NUNChDTgXFUFqbBwMsiYbSmYZ9LhQEwKZJgseuNxEh_2E6XwrMAOcmcdXwB2F20_X_tjKrcuZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هماهنگی تل‌آویو و واشنگتن پیش از حمله به ضاحیه بیروت  مقامات ارشد صهیونیستی و آمریکایی فاش کردند:
🔹
ارتش رژیم صهیونیستی دقایقی پیش از انجام تجاوز اخیر در ضاحیه بیروت، فرماندهی مرکزی ارتش تروریستی آمریکا (سنتکام) را در جریان این حمله قرار داده بود.
📲
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/659306" target="_blank">📅 16:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659303">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a4da2cab.mp4?token=t1kT3TOlt-I11k_35OyCDhiQ_yaXGtrjh-8nySz5SJg-yUPmEjomqN8IxrUwxcPlWYvBvshm9sfkPm4X8IUfmVN9ih6gkVKpWMeab3JW_7YbRRTrbzI_r_80xwzlo-x9N1vSuXx9lN3GLaYF3czezMIf2-NzZ4SeS62ZWllPua0gexXpVgAnOgQOEUF0E46NNTHrR6JjteGYZJpq5lt3yALvi6W_V35nsxmO7TnQz9vb2zrkQX0bpBKs9jdlf08mjWtUgxF4dcPcIChLD1J-AVdspBhr_vmGKldxTC2R3kfATq88fzrJ74lycdnbQCSDknJYpMymlY59O1c2PKiB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a4da2cab.mp4?token=t1kT3TOlt-I11k_35OyCDhiQ_yaXGtrjh-8nySz5SJg-yUPmEjomqN8IxrUwxcPlWYvBvshm9sfkPm4X8IUfmVN9ih6gkVKpWMeab3JW_7YbRRTrbzI_r_80xwzlo-x9N1vSuXx9lN3GLaYF3czezMIf2-NzZ4SeS62ZWllPua0gexXpVgAnOgQOEUF0E46NNTHrR6JjteGYZJpq5lt3yALvi6W_V35nsxmO7TnQz9vb2zrkQX0bpBKs9jdlf08mjWtUgxF4dcPcIChLD1J-AVdspBhr_vmGKldxTC2R3kfATq88fzrJ74lycdnbQCSDknJYpMymlY59O1c2PKiB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مکرون: فرانسه در جنگ هوش مصنوعی مقابل آمریکا و چین است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/659303" target="_blank">📅 15:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659302">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای شبکه ۱۴ رژیم صهیونیستی: یکی از شخصیت‌های ارشد حزب‌الله در حمله به ضاحیه هدف قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659302" target="_blank">📅 15:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659301">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c79a541a.mp4?token=ckYgrfiPymZluT8uSSgFRibJGFpyI_3CKVkZT3cfUvMb7f25KPxI12xCj_QpraRa-2sgMlZKnOkxmGL1Ni_8rNvNvkX0tOx40LTbEOidqOHs_I7guBcMR00T7gpCARnPi7e4BwNQ8_kz1AGmli0NMhV78_LNBjcTJqkG9b19EgBAn22HOnhyzypEOUaVKqoqApe6FZaeeGrl9WNXGkfVoTZszQ4KvHMoSkJRfoCt05wpZjHTuXk9A4iUpR5cY086ZdWIG-f-N9ySc0bmPt4Qer51GwJiPOLt1DFIbrJtbeMHBk9VPKarZKCq33CTjPmHS6IV1-CM3bzvTRhwjpbUgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c79a541a.mp4?token=ckYgrfiPymZluT8uSSgFRibJGFpyI_3CKVkZT3cfUvMb7f25KPxI12xCj_QpraRa-2sgMlZKnOkxmGL1Ni_8rNvNvkX0tOx40LTbEOidqOHs_I7guBcMR00T7gpCARnPi7e4BwNQ8_kz1AGmli0NMhV78_LNBjcTJqkG9b19EgBAn22HOnhyzypEOUaVKqoqApe6FZaeeGrl9WNXGkfVoTZszQ4KvHMoSkJRfoCt05wpZjHTuXk9A4iUpR5cY086ZdWIG-f-N9ySc0bmPt4Qer51GwJiPOLt1DFIbrJtbeMHBk9VPKarZKCq33CTjPmHS6IV1-CM3bzvTRhwjpbUgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم درگیری‌ها میان معترضان و پلیس در کشمیر پاکستان
🔹
به گفته منابع خبری، درگیری میان معترضان و پلیس در کشمیر تحت کنترل پاکستان طی روزهای اخیر ادامه داشته و شماری کشته و زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/659301" target="_blank">📅 15:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659300">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu8Yki_WOHMSgQQdJpq2ufvbmX2z0YsZWMO_qapkrTd-bb2lfW-lMe35gxIyvUwErbqjUgt38Ilu0xYr1XG9PAy_upSdfCJFliOUypgZliiXR9SJJL_NEc2WhJn21LqoY9AYZrWbqhXzNSgT5wEhW-hpQZBviEfyNg0TM0zgx68TytI7oHqKNDTsdb2_rFZjFdurLeAsmHHsWZ4lllagMPPTRDNNlDqMPayPkDylxquIGDWCP79qN8367gzcgSuKxaDNeiyIHdMufJnNlswi2ZxezhsK_zZrCrqOXRvLKBuq95gQJbeQlKnYM-nM2W0G6pndw071TcX6y59TSZnp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رسانه‌ اماراتی: امارات ۳ میلیارد دلار به ایران داد تا حمله نکند!
بیزینس‌رکوردر:
🔹
دو منبع منطقه‌ای گفتند که امارات موافقت کرده که در مجموع ۱۰ میلیارد دلار آزاد کند که بیش از ۳ میلیارد دلار آن قبلاً تحویل داده شده است.
🔹
دو منبع دیگر که از این توافق مطلع بودند، کل وجوه مورد نیاز را ۲۰ میلیارد دلار اعلام کردند و افزودند که این اقدام در ازای توقف حملات ایران به امارات مورد توافق قرار گرفته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659300" target="_blank">📅 15:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659299">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbRo5iHqO5hE35xbXQrQS12717Q78RZ8W5Bug78FgGIY4I8a0nPGSU5D2kUkcQZdux-T6HrQtLdyzyzaTtxMhk4jimHrs9ztoXQXOwf1uobg-v5HO58samk5icjxmOPxWSu24T3lpOWnHsbPaPCPY1u3CvDRQAod6pUgmwAW8Io4foXgk1616JafX3H4obnR4CIXDJjDgS1RsIZ5et9_mTdGlwnSdcWe41iGxSRGRWCmOhuQiUkNTfv2PFuoQCvrXqR34WQXmGQdZOxHDJNN6ZZ-BYQcUeiNN4LL73TkAcP5DrlANsuhY83nfnF_hVl8-uHOjtHlVdooeg0i_UtmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کم‌خوابی به خاطر تماشای مسابقات جام جهانی طبیعی است، اما هواداران کدام کشور بیش از همه دچار اختلال در خواب می‌شوند؟
🔹
ایران در رتبه یازدهم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659299" target="_blank">📅 15:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659298">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDdRkZ6_XSpM84jvYSmGCvg9YYG56Tg87Uyoi3ixSFri0zFAzHNEl1YfHOdQWUEpxehsoI9r6N7Yid7KM-cHvGDR3DAdifp73eNl-9tlyAIOW_oo1wuoQUw1Kk-8zTJ9raZrfxQ38EZ8yOUutchwa9U2pihYFqjNQzaXehH0mRKO2jkXeJ_fCgp7iReCk7BZ-14O8dDTkoxmNdtx3f6a93RUaD4dyeOXXi8CN-Mzk8H2bn9ibvxujNPPiqocHLs448Yg95sh9j4x1DrMcCFKR1kLYaibcn5Vwy6ZDQsv5Ntzuvi3xti5pGwW_VeE0H_GXTySrpKZkfFKRtKYggeruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعم نوشابه‌ات فرق نکرده؟ شاید این آخرین جرعه تو باشه
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659298" target="_blank">📅 15:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659297">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566ae393cf.mp4?token=JHRzsgQHmdGwRFgTHFRzNxByefMKT-iHBp8hRRlU6ydJ5z4n-EHwpd4lTIYWy_oEnHcJy5LL3TOsGfF-XmvK12IZtc-CHtRy25A99DhTn0ywRrwHnNlpUPLK9N3JlLByijb9KpAkOsqfked6wHcdRwJrfYgxpSG7KOHIq1g3GBC0hgId8XZlxfUlg0qcJAwJFB-2Tcu61W8BkFC7sQ6jLmU90uFimcNVGbWt7608KMW9afD4VVp5dQV9ELkYVxpkMtU71zURyeH9XYPDqR2HKGG_Mu_PCxSxLCU8MfwWoJ2pX495_0lJomigUbPNqQCCLHZHwBQJOeD8DoGXNhOhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566ae393cf.mp4?token=JHRzsgQHmdGwRFgTHFRzNxByefMKT-iHBp8hRRlU6ydJ5z4n-EHwpd4lTIYWy_oEnHcJy5LL3TOsGfF-XmvK12IZtc-CHtRy25A99DhTn0ywRrwHnNlpUPLK9N3JlLByijb9KpAkOsqfked6wHcdRwJrfYgxpSG7KOHIq1g3GBC0hgId8XZlxfUlg0qcJAwJFB-2Tcu61W8BkFC7sQ6jLmU90uFimcNVGbWt7608KMW9afD4VVp5dQV9ELkYVxpkMtU71zURyeH9XYPDqR2HKGG_Mu_PCxSxLCU8MfwWoJ2pX495_0lJomigUbPNqQCCLHZHwBQJOeD8DoGXNhOhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سقوط هواپیمای ترابری نیروی هوایی هند
🔹
تمام پنج نفر حاضر در هواپیما کشته شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659297" target="_blank">📅 15:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659296">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtTeYuXlw0N3bzlgGbC8wuW1S3ORUCEm7jqnLK9ToY3yRpdhRd8WtO3U55nY55lZK4ThPPxHlpIO4f9cwwtYXU55CIzEzopXZEUKbjCgHfkrM3KPz8mF3C1V577U3JHN2sk4uPzURJZ37lDJD-r6lVNvTW2s10HbSK-K5UVqvJPuzhfMEu-fU3eCwiK2Jm71j-jJkpcDrWCcs9r5F2LFRUPQvK2CgrASKR5xHMZ-XlB84RifORhO9UpY-Vh3oOmcNk6uGxaj2Yj0PhwKsF9wHmTrtEYl0XykdXc5MA_KzEEhmsg8iiOeTM9c9pZ_7Yj7_RgnWjsMtA5ys5ZWiINcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: مگر می‌شود موضوعی به این مهمی، تحت نظارت دقیق رهبر انقلاب نباشد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659296" target="_blank">📅 15:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659295">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
زیاده‌گویی کانال ۱۲ اسرائیل به نقل از یک مقام امنیتی: این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد
🔹
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد.…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659295" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659294">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
آماده باش رژیم صهیونیستی درپی رد کردن خط قرمز ایران  رسانه‌های اسرائیلی:
🔹
رژیم صهیونسیتی از ترس واکنش ایران به بمباران ضاحیه بیروت و موشک باران سرزمین‌های اشغالی توسط ایران، به همه تشکیلات و نهادهای خود آماده باش داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/659294" target="_blank">📅 15:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659293">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHw1ytwNt1KhwnSNONtLcdAfuZK2lWVSnzHoA6Nb2sXr4-Pd21ZaLFGqMTpW7QT4W-sriwTdXab996RbuaDnS4TJvbIHjY6CgXiT52wYUbvYB-EtVjC6VX95-ul-jAQyGgrruPUtGYNDGlVv2837RvFhZz7rUMf5WQwo0hd4YHKxHQjtleoS73HdzIxRaL3PUG1b2XS8hjUV9QEMlbomm65z_wqMt2zScAjaWZe9IRYX2ZwPhoqKS4yF4FbbS304wsG8HZN52vcZWGQmiJXgTDNeLKtg69gGpSyeLckvniKR04PoRBSCCtmPmg6xkPkzx5jUMxe1EshqvHl9HSoweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جاسوسی برای ایران با ۷۴۰ دلار!/ رسوایی امنیتی در اسرائیل
ادعای تایمز اسرائیل:
🔹
یک شهروند ۴۴ ساله ساکن حیفا به اتهام جاسوسی برای ایران بازداشت شده است.
🔹
«رنان بن حایم اوهانا» در دوران تنش‌های مستقیم ایران و اسرائیل، اطلاعاتی از جمله نقاط ضعف بازرسی بنادر، مسیرهای احتمالی قاچاق سلاح و تصاویر اسکله نیروی دریایی آمریکا و سواحل حیفا را در اختیار یک مأمور ایرانی قرار داده است. در ازای این اقدامات تنها ۲۵۰۰ شِکِل (حدود ۷۴۰ دلار) و از طریق ارز دیجیتال دریافت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659293" target="_blank">📅 15:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659292">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSHunX07nqYZpTxnx2Hx3ofa0ntDgttemLrsUIgZj7cax0XKQZtWAokzZKlIR8pbxLvsSSv_Fg_xYJdTDap-t3BMs3QQAeNXgofUpFMg39Byb-Ua9q19pJWpyJzJu5MNA5gyEjfpVPfydwMhVL6OD9jaU0HOFLHezEFZtMhPL-gs6bNiLsFEm7J3HBDjM1EjmrK_MlWNabY-GSoRzDCWLXQAF1MCgDPpWrEHqab4B7EahyhUoS_ip_YnhErMyQdYNXvHA5Q2foi4exLt6wfVf2bOvU3frea-LtqfFpOHX2-msi9oiKOPXkKwPYy5EX11ZA-q7RgxC3STLD3fpnCVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
غول لبنیاتی شستا در راه بورس؛ دوشنبه منتظر «تادیکو» باشید!
🔹
خبر فوری: بورس تهران بالاخره زمان عرضه اولیه شرکت «سرمایه‌گذاری کشت و دام صنایع لبنی تأمین» با نماد
#تادیکو
را اعلام کرد.
📍
جزئیات مهمی که باید بدانید:
✅
تاریخ عرضه: دوشنبه ۲۵ خرداد ۱۴۰۵
✅
سهمیه هر کد: حداکثر ۲,۵۰۰ سهم
✅
نقدینگی مورد نیاز: حدود ۱ میلیون و ۶۰۰ هزار تومان (سقف قیمت)
✅
روش عرضه: ثبت سفارش (بوک بیلدینگ)
💡
چرا تادیکو مهم است؟
صنعتی استراتژیک است‌و سود آوری بالا و ریسک کمی دارد
در شرایط بحرانی کمترین آسیب را می بیند و تاب آوری بالایی دارد. نواوری و دانش بنیان از ارکان اصلی تادیکو است
🔔
یک قدم تا خرید:
زمان دقیق ثبت سفارش روز دوشنبه اطلاع‌رسانی خواهد شد. برای اینکه از ساعت دقیق و استراتژی خرید (سفارش‌گذاری بهینه) جا نمانید، حتماً به سایت
tahdico.ir
مراجعه کنید</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659292" target="_blank">📅 15:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659291">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868f7e306b.mp4?token=ppK0W_AeS7FLr_xySbaXDfYvZNBgo60PVP-yGEXCs4aq7rF_s0-A_8rj0ETefc6fP_DgpsxMRvE2c5CzEekZ9dEULl31_ECj_aanpOsQXto3Cq0Bmv1YKiGEANDHzcEdy-PLHTeF8NOSm37wT5X6K_9Zr_FWrktyNFX__EIphBYaXHfFN8ZlqqPdIeV5IebjSywCk1L6hnznvieVic7Ps4KOkMx6fGCnISf6_JchJvup3_Iq197UHnTKUIWkPIGLPMjGL0ZKJkcs66uLi9ZA4E2B0E2E_r9-HTX6SkLgQa3HJPrilDvedyxpFA9Y1Q-sqaGD__65Aehd4K9COqrqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868f7e306b.mp4?token=ppK0W_AeS7FLr_xySbaXDfYvZNBgo60PVP-yGEXCs4aq7rF_s0-A_8rj0ETefc6fP_DgpsxMRvE2c5CzEekZ9dEULl31_ECj_aanpOsQXto3Cq0Bmv1YKiGEANDHzcEdy-PLHTeF8NOSm37wT5X6K_9Zr_FWrktyNFX__EIphBYaXHfFN8ZlqqPdIeV5IebjSywCk1L6hnznvieVic7Ps4KOkMx6fGCnISf6_JchJvup3_Iq197UHnTKUIWkPIGLPMjGL0ZKJkcs66uLi9ZA4E2B0E2E_r9-HTX6SkLgQa3HJPrilDvedyxpFA9Y1Q-sqaGD__65Aehd4K9COqrqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم حضرت ابوالفضل (ع) در آستانه حلول ماه محرم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659291" target="_blank">📅 15:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e11a7f2f.mp4?token=I8dorTJGax3Oh2xkexlJDwEs8bjAZxwqXCwPKjAJdM4LpW1I_9PO6eFeU_CvMWbLCcuaw-hL3kkbi-KXr_0L_g20YqN11eWd1qniL8AY7jYuIV2E4oz_1SoXLeceOKNLvPdPJs012JeMDzTcxnfqDlbuhc3BJnsMTMIX2SUmdhh_Ll4Nc2_XST4c-XS_XaUJPMtbycNsdoX-6IDtSLTtu53GxPtdKu2ORe-B-2oTiZ7BaONgpXQJr-PPnAvtXnxcKeva3YFpj6BcD0bCjRWuMYxJIFNMylCNwlrP83W7fCu0-ADumYuZxL_6vZ0ZhRyI1wN9m_D9oOFq0j7DUGIuPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e11a7f2f.mp4?token=I8dorTJGax3Oh2xkexlJDwEs8bjAZxwqXCwPKjAJdM4LpW1I_9PO6eFeU_CvMWbLCcuaw-hL3kkbi-KXr_0L_g20YqN11eWd1qniL8AY7jYuIV2E4oz_1SoXLeceOKNLvPdPJs012JeMDzTcxnfqDlbuhc3BJnsMTMIX2SUmdhh_Ll4Nc2_XST4c-XS_XaUJPMtbycNsdoX-6IDtSLTtu53GxPtdKu2ORe-B-2oTiZ7BaONgpXQJr-PPnAvtXnxcKeva3YFpj6BcD0bCjRWuMYxJIFNMylCNwlrP83W7fCu0-ADumYuZxL_6vZ0ZhRyI1wN9m_D9oOFq0j7DUGIuPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حواشی حضور ایران در جام‌جهانی پیش از آغاز اولین مسابقه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/659290" target="_blank">📅 15:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615ef428a8.mp4?token=lNdQ0yqzMN_WTscnN7XwzdbCWdiGw26-2h2HqboLdlHJzDUCCHak7hE2MsCMCUbuE-PNIHlK1cjK8TH0TzPbpkdyC2KTH_UUg-ZxrJW6tuRS3IjuOUR18h2refvMTaxOPRoTaMfkHnEnoIAeOCK0z4XjLs7W-tCuAsl3wkxCzwY9DzxdZ0RJrmkcrAASDqRVrmc7Pxg5AvQIpQUKYxW2fJdFPyH5NiiIYtO_WriN545kJYkTocfoMXKXbqtqA4Nru17viSMvSByqLiz8lRA5YG-V879Nb6G09f0MV06BVK8JIa-Rf68Lyv7K74Cbly0nI1f-V_rgc0SJ1njHosDHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615ef428a8.mp4?token=lNdQ0yqzMN_WTscnN7XwzdbCWdiGw26-2h2HqboLdlHJzDUCCHak7hE2MsCMCUbuE-PNIHlK1cjK8TH0TzPbpkdyC2KTH_UUg-ZxrJW6tuRS3IjuOUR18h2refvMTaxOPRoTaMfkHnEnoIAeOCK0z4XjLs7W-tCuAsl3wkxCzwY9DzxdZ0RJrmkcrAASDqRVrmc7Pxg5AvQIpQUKYxW2fJdFPyH5NiiIYtO_WriN545kJYkTocfoMXKXbqtqA4Nru17viSMvSByqLiz8lRA5YG-V879Nb6G09f0MV06BVK8JIa-Rf68Lyv7K74Cbly0nI1f-V_rgc0SJ1njHosDHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی بسیار تماشایی از طبیعت فوق‌العاده دماوند
#ایران_زیبا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/659289" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659288">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0a7191a0.mp4?token=NF4ZNDyX72fUE1V6RCdcTBnVGLyAO0kHX1XrJTj2DSpTmHUmVeTVJFNBZ9rz4jQHx4AcdWZqxNErPdWYxPByCeln5kh3i2qnpUIM1sbs-m9qo-k58gMQKdSPHag8HJLYKVPxZfcYgpvOcZGFCpV0-GskR6Pm-yOjaPgk41wmDLpPfm1zwQ32k-6VSpJvaRc-rvC6DK3HmXalxChB2V0fOrbDuapt-JQ7pMHXF8grIcf2_b7d_uOObEWcET-t5Yx3js04b61p0n01XVAhQH1Dfy4h-C3NRYxNQH3bJHkJ34XcymVoEZ5hTZqB30kUD6Xc5qBgLyjeOAGUCW07H8qKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0a7191a0.mp4?token=NF4ZNDyX72fUE1V6RCdcTBnVGLyAO0kHX1XrJTj2DSpTmHUmVeTVJFNBZ9rz4jQHx4AcdWZqxNErPdWYxPByCeln5kh3i2qnpUIM1sbs-m9qo-k58gMQKdSPHag8HJLYKVPxZfcYgpvOcZGFCpV0-GskR6Pm-yOjaPgk41wmDLpPfm1zwQ32k-6VSpJvaRc-rvC6DK3HmXalxChB2V0fOrbDuapt-JQ7pMHXF8grIcf2_b7d_uOObEWcET-t5Yx3js04b61p0n01XVAhQH1Dfy4h-C3NRYxNQH3bJHkJ34XcymVoEZ5hTZqB30kUD6Xc5qBgLyjeOAGUCW07H8qKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات  وزارت اطلاعات:
🔹
یک هستهٔ ۴ نفره گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکه اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/659288" target="_blank">📅 15:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659287">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 معمولا بازی ‌های تیم ملی در جام جهانی را چگونه دنبال می کنید؟</h4>
<ul>
<li>✓ پخش زنده تلویزیون و شبکه‌های داخلی</li>
<li>✓ اینترنت، گوشی و پلتفرم‌های آنلاین</li>
<li>✓ پیگیری نتایج بعد از مسابقه</li>
<li>✓ خیلی پیگیر فوتبال نیستم</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/659287" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
آماده باش رژیم صهیونیستی درپی رد کردن خط قرمز ایران
رسانه‌های اسرائیلی:
🔹
رژیم صهیونسیتی از ترس واکنش ایران به بمباران ضاحیه بیروت و موشک باران سرزمین‌های اشغالی توسط ایران، به همه تشکیلات و نهادهای خود آماده باش داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659286" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659285">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvbkCKDip8bDpHn3Zkd82UyGLuikwxE-J-5mTUI3n-EoNg1C6QBQg-0YlJqgLLMZkESleczD0NFaer2IY6b-3oLI_oSVsWB9nRJ6vZwbKI0qgrkO-C4PdZPo8wSwOw2bOdbF0Oj7kDHD5zuCNsX7MUgCOiVKRuI7VhQP4Vo7ZlE55BBWuJkplRsly_SNr3XLuyNzwJBEBokUNXfiCrs6V0hMG9gUn24y9rKAVftBksF9TllaQgLUJ8d_jrgdCUlcrDSf5xM5mylOCrTOXn8fVlLgjzIYJNYymMwOqky8bzb0a5irQ_yv-kkq44kmAjMZRTl2rOPs_U6gCCOrjP9OLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستخط منتشر نشدهٔ رهبر شهید انقلاب در ابتدای قرآنی که ثواب تلاوت آن را به شهدای جنگ ۱۲ روزه هدیه کردند
🔹
بسم الله الرّحمن الرّحیم
شروع در تلاوت هدیه به ارواح طیبۀ سرداران و دانشمندان شهید در جنگ اخیر و دیگر شهیدان عزیز این واقعه در سحر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659285" target="_blank">📅 14:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659284">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به ضاحیهُ تاکنون یک شهید و ۴ زخمی بر جای گذاشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/659284" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659283">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
عراقچی: امنیت منطقه نمی‌تواند بر پایه نادیده گرفتن ایران شکل بگیرد
وزیر خارجه:
🔹
آنچه تصویر واقعی قدرت ایران را به جهان نشان داد، تنها توان نظامی نبود، بلکه انسجام ملی، ایستادگی ملت و حضور آگاهانه مردم در صحنه بود؛ سرمایه‌ای که امروز پشتوانه اصلی اقتدار ایران در عرصه دیپلماسی محسوب می‌شود.
🔹
تجربه جنگ اخیر نشان داد که امنیت منطقه نمی‌تواند بر پایه حذف یا نادیده گرفتن ایران شکل بگیرد. کشورهای منطقه به تدریج به این واقعیت رسیده‌اند که امنیت پایدار، توسعه اقتصادی و ثبات منطقه‌ای تنها در سایه همکاری، تفاهم و در نظر گرفتن منافع مشترک همه کشورهای منطقه از جمله جمهوری اسلامی ایران امکان‌پذیر است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/659283" target="_blank">📅 14:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7piSX4-Fr0yPDL0xtGE_IGIBMBF52HETqJxdaF1QQH4o9dxCy6qXsB7QLj9XQAoUiN_RE_nXKnrpaEu3p0uitVH_CRfyMiYib7L2RZDL5Ak3Lrw0_lGCA9mVBF6_7pgPUgMhUOs7zjr1mZZNVra9Fb4NFPvWq3N9Iz32hrjN6utnVkAzoAT3RNoqBkKu2PpSMj3dFQgoxtEnDA8D_g_x7EZzGGgCKNtQIGIeUASNhdwSVPRH57oF_bRoKV_COZM6z1ZVZT2CBFqvH-8jk6yaqHv9CqoYrlyCYPDjCq0PTttMo5zctUEObvaijgmYosEGwA77DBYFU0HqP7lTyJdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای دیدار با نیوزیلند
🔹
تیم ملی فوتبال ایران در اولین بازی خود در جام جهانی ۲۰۲۶ صبح سه شنبه ۲۶ خرداد و از ساعت ۰۴:۳۰ به وقت تهران رو در روی تیم ملی فوتبال نیوزیلند قرار می گیرد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/659282" target="_blank">📅 14:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📷
سلبریتی آمریکایی پرچم ایران را به اهتزار درآورد
🔹
«جکسون هینکل» اینفلوئنسر معروف آمریکایی امروز در تمرین تیم ملی فوتبال ایران در تیخوانا، مکزیک حضور پیدا کرد و حمایت خود را از شاگردان قلعه‌نویی در جام جهانی اعلام کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/659281" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e288b78.mp4?token=Vx4bJ3LTe_lHj7rnY-13tL3sq3hQEHd8Kq7XnQpZGD-Lk0kKQiZ4I6FQJI65aQeptjgmUaRt1h2otdEHEyhjyVhvSjBYKLfi93HyJUzcGg6fWcjxZ0gRKhQt7kFmUSFmcmgeza6Yg13SnSB4VAMpUKB05OluY8eqqdpVGf_k8LekCw5UaycZUJYGxTQ41ywrGGVwqdLS36Zg8bbMXocAv-F45VyuXlto7dyAZsANMIHwQz7nI9Cw-mNX4mTHDEZcJPrLK3ae--RGgi-v22109Vsoxy_weFNOdVvb5-OFDjCbj8HUG2abJs3v72AWgFAVfhGa__XNIRLs5oAUHlBRbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e288b78.mp4?token=Vx4bJ3LTe_lHj7rnY-13tL3sq3hQEHd8Kq7XnQpZGD-Lk0kKQiZ4I6FQJI65aQeptjgmUaRt1h2otdEHEyhjyVhvSjBYKLfi93HyJUzcGg6fWcjxZ0gRKhQt7kFmUSFmcmgeza6Yg13SnSB4VAMpUKB05OluY8eqqdpVGf_k8LekCw5UaycZUJYGxTQ41ywrGGVwqdLS36Zg8bbMXocAv-F45VyuXlto7dyAZsANMIHwQz7nI9Cw-mNX4mTHDEZcJPrLK3ae--RGgi-v22109Vsoxy_weFNOdVvb5-OFDjCbj8HUG2abJs3v72AWgFAVfhGa__XNIRLs5oAUHlBRbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگۀ هرمز تا اطلاع بعدی همچنان مسدود است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/659280" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تصاویر منتشرشده توسط ارتش رژیم صهیونیستی از لحظهٔ حمله به ضاحیهٔ بیروت
🔹
کانال ۱۲ رژیم صهیونیستی مدعی شد که اسرائیل یک مقر حزب الله را در ضاحیه هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/659279" target="_blank">📅 14:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۶۵۳ اصابت در تهران و آسیب به بیش از ۵۰ هزار واحد مسکونی در دوران جنگ
علی نصیری، رییس سازمان پیشگیری و مدیریت بحران شهر تهران در
#گفتگو
با خبرفوری:
🔹
در جریان جنگ، تهران ۶۵۳ مورد اصابت را تجربه کرده که ۳ مورد آن مربوط به حملات بامداد پنجشنبه به پایگاه‌های نظامی بوده و خسارت مردمی نداشته است.
🔹
۵۰ هزار و ۸۴۹ واحد مسکونی آسیب دیده‌اند که از این تعداد، ۳۹ هزار و ۴۷۲ واحد خسارت جزئی، ۸ هزار و ۹۲۰ واحد خسارت متوسط، ۴۵۶ واحد نیازمند مقاوم‌سازی و ۲ هزار و یک واحد نیازمند تخریب و نوسازی هستند. روند تعیین تکلیف و بازسازی بخش عمده این واحدها در حال انجام است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/659278" target="_blank">📅 14:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به صور لبنان
🔹
منابع محلی از حمله هوایی رژیم صهیونیستی به منطقه «الحوش» در شهر صور در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/659277" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c876708ff0.mp4?token=bDcyoMXB0zPmf270Q3OBfW9tKrpNXoRbvxvb2Sf14zaQb14URiByvhL55BwBkvkc-Sy9Q23QKd5yHfWV5LcABg9vVNqe4S1QtYnI7rzYKUnWYGbmvQ0S879uMs56DnbGK5noTQl7-LJj7sNgrrAd-7kvTHqtnS-lfH10FujlKuxetM348UqdSX5KzQkn24HrymCtv_PgNMyywehdgPVy_JZ_S_uC4sEh2USpiO9vqXhuaNE3msmoVsv9NaE5j9LJ_ZxLT_qKblGeAkR074QGfBn27M6YkhFQMlRWmeUI-aueKW_eLwY_QAJCI6lIj8aD19EdLr24IC8UYYowfJwmDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c876708ff0.mp4?token=bDcyoMXB0zPmf270Q3OBfW9tKrpNXoRbvxvb2Sf14zaQb14URiByvhL55BwBkvkc-Sy9Q23QKd5yHfWV5LcABg9vVNqe4S1QtYnI7rzYKUnWYGbmvQ0S879uMs56DnbGK5noTQl7-LJj7sNgrrAd-7kvTHqtnS-lfH10FujlKuxetM348UqdSX5KzQkn24HrymCtv_PgNMyywehdgPVy_JZ_S_uC4sEh2USpiO9vqXhuaNE3msmoVsv9NaE5j9LJ_ZxLT_qKblGeAkR074QGfBn27M6YkhFQMlRWmeUI-aueKW_eLwY_QAJCI6lIj8aD19EdLr24IC8UYYowfJwmDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سخنگوی ارتش اسرائیل: زیرساخت‌های حزب‌الله در ضاحیه بیروت را هدف قرار داده‌ایم
🔹
حمله دشمن صهیونیستی به ساختمانی مسکونی در محله الغبیری انجام شد و تا کنون تعداد بالایی زخمی به مراکز درمانی منتقل شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/659276" target="_blank">📅 14:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
حریری، رئیس اتاق بازرگانی مشترک ایران و چین: در سال ۱۴۰۴، ۱۸ میلیارد دلار واردات از چین داشتیم
🔹
پنل‌های خورشیدی و لوازم جانبی ساخت نیروگاه خورشیدی در صدر کالاهای وارداتی از چین بوده و خودرو به صورت قطعات منفصله یا ساخته شده و لوازم مربوط به ساخت ابزار الکتریکی از دیگر اقلام عمده واردات رسمی از چین هستند.
🔹
اقلام مصرفی هم در صدر اقلامی قرار دارند که از چین قاچاق می‌شوند./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/659275" target="_blank">📅 14:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از مقام ایرانی:  بر اساس یادداشت تفاهم، آمریکا ۲۵ میلیارد دلار از دارایی‌های ایران را از طریق انتقال مستقیم نقدی، همکاری میان کشور‌های منطقه و خطوط اعتباری مالی، آزاد می‌کند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/659274" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
خدمات کارتی بانک ملی تا ساعاتی دیگر وصل می‌شود
شرکت خدمات انفورماتیک:
🔹
ارائه خدمات حضوری در شعب بانک ملی از ساعتی قبل آغاز شده و خدمات کارتی این بانک نیز تا ساعاتی دیگر برقرار می‌شود. بر اساس این گزارش، تا ساعت ۱۳ امروز بیش از ۷.۶ میلیون تراکنش در بانک صادرات با موفقیت بالای ۹۹ درصد و حدود ۳.۴ میلیون تراکنش در بانک تجارت با موفقیت ۹۸ درصد انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/659273" target="_blank">📅 14:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
حمله به ساختمان ۵ طبقه در ضاحیه جنوبی بیروت
🔹
شبکه خبری المیادین از حمله هوایی رژیم اشغالگر صهیونیستی به یک ساختمان پنج طبقه در ضاحیه جنوبی بیروت خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659272" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
