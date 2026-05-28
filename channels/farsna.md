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
<img src="https://cdn4.telesco.pe/file/hbooY9dfmkyLpEOMui0V-GmznAQ-wIBT-ZaKHTpn812B_UlRaK5cfoiHvUQSdPnoZy1iyB_c7Zato7jeo-axPVZWcpZjY0HSRQr0HTxzDiQXpmFZU0PSAK-EIAXA6EwZC4xqHRi7zDIuC77G57uWAxec9VCaZZOGH59-JmUrz0thtzJ9qoDbtswma5QIyCYWR7cTJ-2bM45KGtMMuJxwhMcYtgL4JtGx6tIoKT9ITkHKsrWhEdXuLaVznIRWzjFRSkcj5GM7NbDbDJGxNtZmr7cdofDoHsFz_b1LhLQ9DrmhA5YgYzSuxjkGDrZV8mXnggXmopXKBYMsti_cTzNrSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-438440">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: جامعه، پیش از هر چیز نیازمند مشاهدۀ نشانه‌های واقعی امید، مسیر باثبات و چشم‌انداز روشن از آینده است
🔹
لازم است مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد.…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/438440" target="_blank">📅 14:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: نمایندگان ملّت تمام توان و ظرفیت خود را برای حکمرانیِ هم‌افزا با دولت سایر دستگاه‌ها مصروف کنند
🔹
در این میدانِ جهاد، صندلی نمایندگی، به‌مثابه‌ی سنگرِ خط مقدّمِ تحوّل در مسیر پیشرفت کشور، قلمداد می‌شود؛ لذا شایسته است، نمایندگان ملّت، با اتّکال…</div>
<div class="tg-footer">👁️ 371 · <a href="https://t.me/farsna/438439" target="_blank">📅 14:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438438">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: مجلس نقش مهمی در اِعمال اراده‌ی مردم دارد
🔹
مجلس شورای اسلامی عُصاره‌ی ملّت، مُظهر مردمسالاری دینی و رکن قانون و قانون‌گذاری در جمهوری اسلامی است که نقش مهمی در اِعمال اراده‌ی مردم دارد.
🔹
اکنون با سپری شدن سه ماه، از دفاع مقدس سوم، عیار باطنی…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/farsna/438438" target="_blank">📅 14:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‎‌
🔴
رهبر انقلاب: از تلاش‌های آقای قالیباف، در راه اعتلای کشور قدردانی می‌کنم
🔹
عید سعید قربان و سالروز افتتاح اولین دوره‌ی مجلس شورای اسلامی را، به همه‌ی ملّت عزیز ایران اسلامی و نمایندگان محترم مجلس شورای اسلامی، تبریک می‌گویم و به این مناسبت، از تلاش‌های…</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/farsna/438437" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438436">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: لازم است، مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد
🔹
آیت الله سید مجتبی حسینی خامنه ای در پیامی به مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم : در مقطع…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/farsna/438436" target="_blank">📅 14:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438435">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">131.9 KB</div>
</div>
<a href="https://t.me/farsna/438435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: لازم است، مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد
🔹
آیت الله سید مجتبی حسینی خامنه ای در پیامی به مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم : در مقطع…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/438435" target="_blank">📅 14:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438434">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم منتشر خواهد شد  @Farsna</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/438434" target="_blank">📅 14:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438433">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم منتشر خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/438433" target="_blank">📅 13:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438432">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bdcd9a40.mp4?token=eLJ-pUxPV-1Cdp5iux2pVys-wvmhRIew1E8fc-zRyS_II6OOvTnlAfJ9WjMCngrLkwvdVCkC4-SvMTY4Xui-dTgTRJuzUTZQroYdwdrTG0-up_kDsSHSs9Cj4mDE7V4MgYyyWm94HgUXBqV7XU1YslAHBKknsTgTrDl99EFmU5Uv1QC5lTD51rrMJJ4WoWFDFVNs1Q2VDnJJNHO_d-qILm9HziXiMcq_ThK27-1wue5j68YrGo4b-m5DBNbWwhrWNYLkig-JzBDfu8lfEzUnbt_CRIgOSlf7LYgNDvoCdXdJFX70F4mNs01kb6TLu5Zw_ZjeBcq4L4UMCZOMrcXA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bdcd9a40.mp4?token=eLJ-pUxPV-1Cdp5iux2pVys-wvmhRIew1E8fc-zRyS_II6OOvTnlAfJ9WjMCngrLkwvdVCkC4-SvMTY4Xui-dTgTRJuzUTZQroYdwdrTG0-up_kDsSHSs9Cj4mDE7V4MgYyyWm94HgUXBqV7XU1YslAHBKknsTgTrDl99EFmU5Uv1QC5lTD51rrMJJ4WoWFDFVNs1Q2VDnJJNHO_d-qILm9HziXiMcq_ThK27-1wue5j68YrGo4b-m5DBNbWwhrWNYLkig-JzBDfu8lfEzUnbt_CRIgOSlf7LYgNDvoCdXdJFX70F4mNs01kb6TLu5Zw_ZjeBcq4L4UMCZOMrcXA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ بررسی طرح رایگان‌شدن مترو و بی‌آرتی در شورای شهر تهران به هفتهٔ بعد موکول شد
🔹
سروری، نایب‌رئیس شورای شهر تهران: با وجود برنامه‌ریزی قبلی برای بررسی طرح حمل‌ونقل عمومی رایگان در صحن امروز، به‌دلیل ارائه‌نشدن نظر نهایی و کارشناسی از سوی یکی از کمیسیون‌های…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/438432" target="_blank">📅 13:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438431">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8xACVKqlTyYOY2nMCYODszH1xBQILhwK4eIJWPM_NthR7tQD8VDC68v4ZsRYZh3usV-vcyNJa34dnE0qIEl1-UhYnC_ULMkCQt3gD9HxAxkCsaDwu297LtSAf32Nbbsplid4Tiqrgg-eBgzDLcfOiVodEJtKLrPsXoR3Hwe1Aj9sF4IcPI8_k8iRkkvBxolsrzwhSUmP_H8NEIG3C-QOLJtcRUKpaq0fpa-35i8TDW9YQKWp_0YQIEsyjEiEi3tHKH455KW7TD7BoVY1zRadKYb5yo7FedSsgDOAzAduu9UUkX9qW-S8tJl2ZhOtKwucG1-fI05zJsqGlR-jnR-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت ستون دیجیتال ارتش آمریکا شد
🔹
رویترز: وزارت دفاع آمریکا اعلام کرد قراردادی ۵ ساله به ارزش ۹.۶۹ میلیارد دلار برای یکپارچه‌سازی مجوزهای نرم‌افزاری مایکروسافت و دیگر شرکت‌های فناوری امضا کرده است.
🔹
این قرارداد، تمام خریدهای نرم‌افزاری پراکنده میان شاخه‌های مختلف ارتش آمریکا، جامعه اطلاعاتی و گارد ساحلی را در قالب یک قرارداد واحد جمع می‌کند.
🔹
پنتاگون می‌گوید هدف اصلی این طرح کاهش هزینه‌ها و جلوگیری از خریدهای تکراری و پراکنده‌ای است که طی سال‌ها در بخش‌های مختلف نظامی ایجاد شده بود.
🔹
این قرارداد شامل سرویس‌هایی مثل اشتراک‌های «مایکروسافت ۳۶۵»، ایمیل، ورد، اکسل، پاورپوینت، خدمات ابری و مجوزهای نرم‌افزاری داخلی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/438431" target="_blank">📅 13:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438430">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1793d0e1b.mp4?token=bkTqVOeCuKqaH1q8qsZRY1if9znGfHBknpd5KD5UOC7vEccRI3oXUGVXoijtLs6ce_6PS1ZYR5G9FKBtFKDLvErM4B5YqPkt0skZo7mQwKWJIQMFeGN6gu62Yb9eSs0L4HD9chd4mwk526JMvSllBAm2VG-n0xQ_BeJdhtNGZdKHE7O4BNpBm7fPrYK4e-TCFHNKHoDNVKfN5gTf73ctlsp5GBcJiNlLDDC0_kiYRSafX6N9Mnj4TFzShK442RIJiNLbCymDb1eC3Z5UsYXQ6s98b35Ay5nWF5Qi2up3IxRGznYB87hpTKgVlThc7TStXNaNbBNJZuAMZuq72IEZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1793d0e1b.mp4?token=bkTqVOeCuKqaH1q8qsZRY1if9znGfHBknpd5KD5UOC7vEccRI3oXUGVXoijtLs6ce_6PS1ZYR5G9FKBtFKDLvErM4B5YqPkt0skZo7mQwKWJIQMFeGN6gu62Yb9eSs0L4HD9chd4mwk526JMvSllBAm2VG-n0xQ_BeJdhtNGZdKHE7O4BNpBm7fPrYK4e-TCFHNKHoDNVKfN5gTf73ctlsp5GBcJiNlLDDC0_kiYRSafX6N9Mnj4TFzShK442RIJiNLbCymDb1eC3Z5UsYXQ6s98b35Ay5nWF5Qi2up3IxRGznYB87hpTKgVlThc7TStXNaNbBNJZuAMZuq72IEZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین از ساخت نیروگاه هسته‌ای در قزاقستان خبر داد
🔹
در جریان سفر رئیس‌جمهور روسیه به قزاقستان، توافقنامه ساخت نیروگاه هسته‌ای توسط شرکت روس‌اتم روسیه در قزاقستان، به امضای طرفین رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/438430" target="_blank">📅 13:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438429">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgrCDBwYB5Kv53LCP-SOgnyQ7FT3UKAjPPn271Hu1_OTVQEl3rmc4Z0NEUotbsDCqj6FPxCOkSSoTUmxtUCKbFwhXlGDcl2EEldaBjNA9r-XSJoou36vNavtOTlHv2wyYsMdU5jj9PMNwqxlMzNPi_7EiDp4vqCYYmdgIOsW_EJPprBXBFKV55oSU4ZOiT8CZElRDKUKHfF--wVcESqIbMElN0EjCzGQtA4nYt_nK-Ia5o1HT7P3QSeNZ50QZpxpAmRx-qcT-BnTRdtbLtfN5ROPz3TY6ieM1eojHvE4ZtR5vTs4iKXWmJObJ6uprvAKnhZBmNJta8SN51s0hwAX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دعوت محمدرضا طاهری از مردم برای شرکت در مراسم یادبود شهدای خانوادهٔ قائد شهید و رهبر انقلاب
🔸
این مراسم از طرف خانوادهٔ رهبر انقلاب پنجشنبه و جمعه از ساعت ۱۶ تا ۱۸ در  مصلای حرم حضرت عبدالعظیم حسنی(ع) برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/438429" target="_blank">📅 13:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438428">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">توقیف محمولۀ سیگار و عینک قاچاق در مرز
🔹
فرمانده مرزبانی فراجا: مرزبانان پایگاه دریابانی بندر لنگه محمولۀ ۹.۸ میلیارد تومانی قاچاق را کشف کنند.
🔹
در این عملیات ۳ ميليون و ۸۱۷ هزار نخ سيگار خارجی، ۴ هزار و ۳۴۶ عدد فریم عینک، ۳۲ دستگاه فن کویل و ۱۳۴ دستگاه لوازم برقی آشپزخانه قاچاق ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/438428" target="_blank">📅 12:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438427">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6cb621aa.mp4?token=AMlioCWRZdhQVhVImeOR_4xkyhfMelWWfn3CIk3Ls4EJadPDno8nfH4LQd3A3A018eedag2MTU8kdWb3kL2iIZ-lP6FJlDIPvCSulibRYQfQClqtDE4vg98IqSF11i8pFAaYdQIw9tOGQe6S7Klxh9aN_iAPmTs9fwj1qr43ncaUxW9-6YKKvZl2wCriBiyFpa0HnebNno-GEYLHxf68zDb8wx-LTq3ohJtQAzL4hzG6MoZQAaK_RCnapTd5ywUhSNloV5WcmlkzUCNMvGOwYdqONsxaJs-0M7KLio1aSH-RPCAOwWPBzdy800KNT8tuTQ_G_05hdwojR6BGCPgR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6cb621aa.mp4?token=AMlioCWRZdhQVhVImeOR_4xkyhfMelWWfn3CIk3Ls4EJadPDno8nfH4LQd3A3A018eedag2MTU8kdWb3kL2iIZ-lP6FJlDIPvCSulibRYQfQClqtDE4vg98IqSF11i8pFAaYdQIw9tOGQe6S7Klxh9aN_iAPmTs9fwj1qr43ncaUxW9-6YKKvZl2wCriBiyFpa0HnebNno-GEYLHxf68zDb8wx-LTq3ohJtQAzL4hzG6MoZQAaK_RCnapTd5ywUhSNloV5WcmlkzUCNMvGOwYdqONsxaJs-0M7KLio1aSH-RPCAOwWPBzdy800KNT8tuTQ_G_05hdwojR6BGCPgR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صفر تا صد سامانۀ «باهم می‌سازیم»
🔹
شهروندان می‌توانند با مراجعه به سایت
BAHAMTEHRAN.IR
یا ارسال عدد ۱ به سرشماره ۳۰۰۰۱۱۴۱۱۱ در بازسازی شهر مشارکت داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/438427" target="_blank">📅 12:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438426">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2EDKe_ZfW8UTbDb-XQu8klcoLkaIEeZk270_vE_E6EVMm1Lw_0hsE5PInER262i2YhtisK8TO3stjqlGgfeZmvmFrseNCVDgXBvAeuklb_SwlNbez63-KkhKBC-HOZlKx_sai1P5vPSgOFzbH7R8Vdsh-E1RSxvN-c4sDLg6B4V98GcdkznIjkujnFWEVl7QKUQIde02uGeBjDRXrkYJFlmkBva1BO2BepMdV5gHpAxYCEWbIE_vXvdrn7FUZAk5TnhArz3KKSHTkd5ZilG8T3az618ZLWi9j0HlfdRHLBg7yT7I3f7dn-1HgXmOOB38oQVuJzPoVvffx7u3jzycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏥
اعلام آمادگی بانک صادرات ایران برای نوسازی و توسعه زیرساخت‌های سلامت در انستیتو پاستور ایران / تأکید اسکندری بر حمایت از امنیت سلامت کشور به عنوان یک مسئولیت ملی
🔹
در پی خسارات واردشده به انستیتوپاستور ایران در جریان جنگ تحمیلی سوم، سرپرست بانک صادرات ایران به همراه اعضای هیأت‌مدیره و مدیران ارشد این بانک، با حضور در این مجموعه علمی، بر اعلام آمادگی بانک صادرات ایران در روند نوسازی و تأمین تجهیزات تخصصی آن تأکید کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/438426" target="_blank">📅 12:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438425">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh04jJ3WLALPELnmRYP2l0D2saaPfZBI5JDyRo6SVRsluvlDUkU6JBv2mJPFtX60TKtzjToOnJGMbiWdEZsoIHk90Ea9kWRwF5FHxFVtd86OlEQkzFZxVMW7sPcmdS3dxkl4SGo4yTZwL-or1DSrAt4BgKjgY25HY9J8gGDCZ0Jxm_nxMszEtRM1m2lmhb4fzghcWi3J253b_jc7k-1nNscZ0vTevKwy-G6N699WPmasO7pSZ1kalRFVtd-YtGtnZo8FblG2DJJ1CiVyt5aGvtCErPLliT8ewK5rrQ8U3UN8Gu7cNnPvn8MddT8BPTCf3l1TB_6gGayF4oZ7BY299Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر فوری: کوچولوها مهمان ویژه پارک آبی اُپارک!
🚨
💦
فقط تا 15 خرداد!
📆
میتونید بلیت هدیه اُپارک مخصوص خردسالان رو دریافت کنید
😍
🎁
برای دریافت بلیت هدیه روی لینک زیر
کلیک کنید
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/438425" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438424">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/438424" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438423">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptDTye80h7Al4vKM_q8lE8aOcudSWi6D58fiaLBaMeqjZ17SRxaCuMSogCaHml1GmkJ2rmVQnVwABvl1YR-N-g9_X9hBhYoZsNuWnAZY3berNrKgxDLleJcL89XcaeL-rPcYDV4o2O_hDUkIDwEVoZ5AY5uKsARD1YVyUP9-8O_97b--LVjP_jzb1Dy2ud-y1THU7J-lHBievf2IINumExDVp5nNkhuIlQB_kNnlhmpS1sja1e8CulydhPzh3fq1lOP4FeQ_cg9deMpMo-R46mDY7Bb86DQZ67TEsjLzha8w3_B3bhmTbvj_sQI6b6Kro-rmmcJG0iRs6ah4faVWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قوه‌قضائیه در زیر بمباران از صیانت حقوق مردم دست نکشید
🔹
رئیس‌مجلس با قدردانی از پیام تبریک رئیس قوه‌قضائیه نوشت: قوۀ مقتدر قضائیه با مسئولیت حضرت‌عالی و تلاش سخت‌کوشان عدلیه، در زیر بمباران و تهدید دشمنان دست از صیانت از حقوق مردم و برخورد قاطع…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/438423" target="_blank">📅 12:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438422">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
رسانه‌های صهیونیستی: از صبح امروز، ۵ پهپاد حزب‌الله تجمعات ارتش اسرائیل را در جنوب لبنان هدف قرار داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/438422" target="_blank">📅 12:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438421">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGH7NsayxW-2ngzZPhgMCWhIpjogzm8MYK23f3aNQpJdtfnyQPTj4LasH8onxH32kzHmCso3lSyFhQvmx2aWw92ZECi5x-sPabcQgMO3KBZGIbbkkWvUUl2OF_CHmL7YAAFRDCCtmbtwTrd1IssfZweEdkUZEz7ojc2CuzMq-k2AUgSAXrHdV4aVJnhvt_Qd-8w9QNf5BTLIDsd0PnxLDSGR7XW7S9S7wEjJ-KinpL0VA8OKzbb-0wiF15Pvsg7yZnEhU8iOTMs1kcWddGQkkKmYP85m3FOJNoRPfAhEFDyHbGYn8yMvpfomUmBCxRyo_9ZS8askK0bcJ0tWsyhRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ابراز نگرانی سناتور آمریکایی از وضعیت «شوکه‌کننده» ذخایر موشکی آمریکا
🔹
سناتور آمریکایی مارک کلی روز یکشنبه در مصاحبه با شبکه سی‌بی‌اس از تجاوز نظامی علیه ایران و مصرف بیش‌از‌حد مهمات آمریکایی در این جنگ انتقاد نمود.
🔹
وی در این باره اظهار داشت: «پنتاگون…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/438421" target="_blank">📅 12:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438420">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ837PLW6PyA2LuzeRIIgAJqEBCm6Xub91LGoZQmNF5VrGp5LxXV0EW4g8A8Dk-a3u9-hmnUA1KlXxHLNrRlErB9wYY7igpu-v5HghZESMUsiS8USlP0JStnHUJBW0tRxFDwB9B0bdaf891h3lMrmFnWRvSxgr3sAJoy_2V1weB9ldfuYE0dq-1xHuC3KPPgcd46QwUrdN2vau9dfU7-immVvhmFXTI72rM1ir_tWqobeKhuOXtLeIg6ZhSwIWIcQVVZS5_i7PnWakcsL5cDTION6zZfVpWOuxHl8Ly2N9bu6z5hFDEd1H8E221iZVqMg3fuXMYY8elB141fZDSxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره شمالی: تحت هیچ شرایطی به ان‌پی‌تی نمی‌پیوندیم
🔹
سفیر و نماینده دائم کره شمالی در سازمان ملل متحد کیم سونگ، امروز در بیانیه‌ای تند و صریح اعلام کرد که پیونگ‌یانگ «به هیچ وجه و تحت هیچ شرایطی» به معاهده منع گسترش سلاح‌های هسته‌ای (NPT) پایبند نخواهد بود…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/438420" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438419">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwUGt4P_b4LhgmOQuoP6sCOCU4CC44fvge7iHwKCqZNxuDpf43Xjm8H5zuBGjltFvzNlEKPPZ1xH2d0OEDsWi-TBtBFZRQ4TAt9HX4yWwMRab8NHwP7CYrmxOR6kck-VRA9goAB7Ckw66vFCluZtwlKY8qX3eyC3Wm_P7X2LroYgFYS_5i1n085kXDaOIi_DoVxZ1W1FiFdO5yCOS3eHqlideiddrL7siexgEOZEbj9CjDgR-PCeNhXq_ythSUw8zRi9BWHjBAYsQEqBH5dEsUG5GCPDb4oE0Ews7SF5ry1Eedr_fdDqTdkur1XYfHnALfmQp-Iwkl0zhgYw1rmGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌ها و وزارت راه علیه ساخت مسکن
🔹
در‌حالی‌که حدود ۱۶۲۰ همت از تعهدات بانکی وام ۶۵۰ میلیون تومانی در قانون جهش مسکن هنوز پرداخت نشده، وزارت راه و شهرسازی سقف وام مسکن را بدون ضمانت اجرا به ۸۵۰ میلیون تومان افزایش داد.
🔹
براساس گزارش رسمی دیوان محاسبات کشور، شبکهٔ بانکی طی ۴ سال منتهی به شهریور ۱۴۰۵ مکلف به پرداخت ۲۲۲۱ همت تسهیلات در قالب قانون جهش تولید مسکن است، اما تاکنون تنها حدود ۶۰۱ همت از این تعهدات عملیاتی شده و ۱۶۲۰ همت، معادل حدود ۷۳ درصد تکالیف قانونی، همچنان پرداخت نشده است.
🔹
بسیاری از کارشناسان معتقدند وقتی وزارت شهرسازی هنوز نتوانسته (یا نخواسته) بانک‌ها را به پرداخت کامل وام ۶۵۰ میلیونی ملزم کند، افزایش سقف تسهیلات به ۸۵۰ میلیون تومان بیش از آن که اثر عملی داشته باشد، نوعی بازی رسانه‌ای است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/438419" target="_blank">📅 12:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438418">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHAPgSkBiu_UpQ0Qis4mcB2xngBz8D9kuU3VpcZBCXB4JGEWPW05R3gHs3cBqS9ZKrAH71vOp30-LhK3UsK2WnscQCENxPGbpfL0DZSQvgLn1v8do1UHIvFCdYv9RHT4rz14T8YZfqa8tCfde_TDa3wa4UKEHjqxVpQeZ0wYV5J6k8EzUFx-SrafO8Eg3W6OUbNcnYpQ3l8AaMsNZpcFU8CDq5FepPM9WUhskwJWzBNKraiu6WwTev0tuYkXyUIkXprEbdQw4l2L6l_FL-ZIhvkaK_eyG5KNJTIIObMc9OUtJvoQQc2U44cI_PDFuS76jOW7NASRcTogd46tnzZjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریفان ایران در مقدماتی جام ملت‌های زیر ۲۰ سال
🔹
حریفان تیم ملی فوتبال جوانان ایران در مقدماتی جام ملت‌های زیر ۲۰ سال آسیا معرفی شدند.
🔹
گروه A: کره جنوبی، قرقیزستان(میزبان) فیلیپین و  لبنان
🔸
گروه B: ازبکستان(میزبان)، سوریه، هند و بنگلادش
🔹
گروه C: ایران، ویتنام(میزبان)، کره شمالی و فلسطین
🔸
گروه D: اردن، تاجیکستان، بحرین(میزبان) و افغانستان
🔹
گروه E: عربستان، قطر(میزبان)، عمان و هنگ‌کنگ
🔸
گروه F: عراق، تایلند(میزبان)، امارات و ترکمنستان
🔹
گروه G: ژاپن، یمن، کامبوج(میزبان) و کویت
🔸
گروه H: استرالیا، اندونزی، مالزی و لائوس(میزبان)
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/438418" target="_blank">📅 11:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438417">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X91s43iffBzsFbqd_oZPFPbx66UyXzYxD3pPxpKhIirvD84xm45bm-7ir-VKQS35IA1bg7Fzfg8Z7QbFuHavRLaC1OLphB4aM2KTdMjg1aSCkBwcwXzna4GB_n_ThAlbRasebcYkv2IEJAsSncOD2hYO67_MHMXsPHl_5F4YNywyzGv8aX42DXvkZVghVo1EZSv5KIwMqh2HrvzDxurXYUUkKcr0GF_PniDJMQ_Pzb6ZMNXuvbGr7HCYq3skhL5-uzHZyF9ZmTze09OpirJVxBXnG_4lDEhN95TWY9tvzihM5yjQ7eJncX78O7LwaWyk6RlecJgFb054Ob7dcDnIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل در فهرست سیاه عاملان خشونت جنسی
🔹
به‌گزارش جروزالم پست، سازمان ملل متحد نهادهای اسرائیلی را به فهرست سیاه کشورها و گروه‌هایی که در مناطق جنگی مرتکب خشونت جنسی می‌شوند، اضافه کرد.
🔹
میدل ایست آی نیز نوشت: گزارش‌ها و شواهد گردآوری‌شده از سوی گروه‌های حقوق‌بشری نشان می‌دهد که پس از آغاز نسل‌کشی اسرائیل در غزه، خشونت‌های جنسی ارتکابی توسط نظامیان و شهرک‌نشینان اسرائیلی افزایش یافته است.
🔹
سازمان زندان‌های اسرائیل در فهرست سیاه ۲۰۲۶ سازمان ملل قرار خواهد گرفت و سایر مقام‌های این رژیم هم تحت چارچوب نظارتی برای احتمال شمول در آینده قرار گرفته‌اند.
🔹
نمایندهٔ اسرائیل در سازمان ملل متحد در واکنش به این تصمیم: به‌دلیل این اقدام، همکاری با دفتر دبیرکل سازمان ملل، آنتونیو گوترش را متوقف خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/438417" target="_blank">📅 11:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438416">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTYELMmrz1fgFX_5WPMSb-ACGSvkmntOnuNK2XZM0JmNXIQPmASygzLq3Q6Uk4sdnXlRVIDN1_CJ0i5QGdKYvFWqdLyxmTL5wdGbq5MQMpn7_rt59l62Pr4RVDSYpid1cmxs1Maa0qArz2uix0-mPqADAHSAzY7lzzUpNqJHtm17XR14NGczgCNqaLJd_r_eV7xih7Mg0MJflLrUoe4Znv5MwrgyyGE0hB_nNmm_c5TBQl_3jGqAW1df1ukfadnKW5HNOYs7crXMqoTOg1LCWoFctCI2j2BvzNih1x_3S39d-AlFNsfof1xT2w3aC9KWx0IZ_oWjXh7ajAHW0kLPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی نقض آتش‌بس و لفاظی‌های تهدیدآمیز آمریکا را محکوم کرد
🔹
سخنگوی وزارت خارجه: اقدامات تجاوزکارانه علیه تمامیت سرزمینی و حاکمیت ملی ایران، نقض فاحش حقوق بین‌الملل و منشور ملل متحد به‌شمار می‌آید.
🔹
شورای امنیت سازمان ملل موظف به ایفای مسئولیت قانونی خود برای پاسخ‌گو کردن متجاوزان آمریکایی است.
🔹
نقض‌ مستمر آتش‌بس ۱۹ فروردین از سوی آمریکا، به‌ویژه تعرض به کشتیرانی تجاری در منطقه‌ خلیج فارس و آب‌های آزاد و نیز تعرض هوایی به مناطق جنوبی ایران ظرف چند روز گذشته، بر عزم ایران برای اتخاذ همۀ تدابیر لازم جهت دفاع از حاکمیت ملی و تمامیت سرزمینی ایران وفق ماده ۵۱ منشور سازمان ملل است.
🔹
تهدید به «انهدام» کشور دوست و برادر یعنی
عمان
که همواره نقشی سازنده، موثر و مسئولانه در قبال صلح و امنیت منطقه داشته و طی سال‌های متمادی در مقام میانجی روندهای دیپلماتیک، مساعی جمیله خود را در خدمت صلح و ثبات منطقه به‌کار گرفته، نه تنها نقض اصل بنیادین منع تهدید به استفاده از زور است، بلکه نشانۀ خطرناک دیگری از عادی‌سازی قانون‌شکنی و قلدرمآبی در روابط بین‌الملل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/438416" target="_blank">📅 11:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438415">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRGY2P0_HxO5e7qYbPateNnWlK2AZMLi1K7gqs3IhB-TcSx7uyJDYv736chsMHpdZlaPab1TX2rB-zh_NEve3ZVFmS-poK6HLUq4-kLCidbWLep2o9VjyBPjHETR1ZQMjlG2fF595JBPQdk6ZdgKx2cTYhD2EzNGF0OsN62M8FdghKqTwO5jOGm5REXdYH7yI4WMYk5EKqHq1yWPeaxtr14QycMKFe86fIOFd17TKeDvNP8dALqzLQ4tu2ktcElcVRdNM1Nz5IOLhYfB6RGG0UpTlJXsXowRPePOM9NM7v1Lldcq7XsV3xJM46KaGNAg6F512k8fSaPD8Pn_NLjuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمارانی که به‌خاطر قیمت، دندان‌درد را تحمل می‌کنند
🔹
هزینه‌های بالای دندان‌پزشکی و تحت پوشش نبودن خدمات آن دلایل اصلی عدم رسیدگی مردم به دندان‌های پوسیده‌شان است.
🔹
طبق شواهد، حداقل هزینهٔ عصب کشی یک دندان، ۶ میلیون و ۸۰۰ هزار تومان می‌باشد.
🔹
اگر دندان کشیده شده باشد، هر واحد ایمپلنت به تناسب کیفیت جنس آن طبق تعرفهٔ مصوب ۲۳ الی ۳۰ میلیون تومان قیمت دارد که در برخی از کلینیک‌ها این عدد تا ۵۰ میلیون تومان هم بالا می‌رود.
🔹
اندوکراون یکی دیگر از روش‌هایی است که معمولا برای پر کردن دندان‌ استفاده می‌شود. انجام این نوع روکش بین ۱۱ تا ۱۳ میلیون تومان برای بیمار هزینه دارد.
🔹
پر کردن با مواد نیز یکی دیگر از روش‌های پر کردن دندان‌های عصب‌کشی شده است که ۴ تا ۱۲ میلیون قیمت دارد.
🔹
به‌طور کل میانگین هزینهٔ درمان هر دندان بین ۱۵ الی ۴۰ میلیون تومان است، بدون اینکه بیمه‌های پایه ریالی از آن را پرداخت کنند.
🔹
طبق آمارهای موجود، هر ایرانی حداقل ۶ دندان پوسیده دارد از این رو تعدادی از مردم با ثبت‌
پویش‌هایی
در بخش فارس من خبرگزاری فارس، درخواست تحت پوشش بیمه قرارگرفتن خدمات دندان‌پزشکی را داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/438415" target="_blank">📅 11:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438414">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42fe08de28.mp4?token=be_TXoLsAWFlnNmfcyliKI4hmsrhpLWIuaMyPAZMDa-ulMPZZXXCWKhtY3em4oHT6OC4nyB4mpjuBt-frh_Aqr6XZ1xlEe_0-NsW44HyxaopVWxOfE-GpCRWm5-exRxirbUpEWxAJK7hqiC61Okc9a6lJj8UdLqAkKnlnxMKpD7C1X_DPeLSZsFEPPRnmDwU9Q16HyeS0jqanE-n2lWFCcCXLu8evaqDlHom89MN-eRE9NaI7w2oD6JXZN8YqNebPkb_Ar0goM4HQpJkUz1GJPyk8Gr16TMrA4eiw4K7pNSyF4rfA0fReglHduhw4DkdSdpMCET3iINK5LVa-nS3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42fe08de28.mp4?token=be_TXoLsAWFlnNmfcyliKI4hmsrhpLWIuaMyPAZMDa-ulMPZZXXCWKhtY3em4oHT6OC4nyB4mpjuBt-frh_Aqr6XZ1xlEe_0-NsW44HyxaopVWxOfE-GpCRWm5-exRxirbUpEWxAJK7hqiC61Okc9a6lJj8UdLqAkKnlnxMKpD7C1X_DPeLSZsFEPPRnmDwU9Q16HyeS0jqanE-n2lWFCcCXLu8evaqDlHom89MN-eRE9NaI7w2oD6JXZN8YqNebPkb_Ar0goM4HQpJkUz1GJPyk8Gr16TMrA4eiw4K7pNSyF4rfA0fReglHduhw4DkdSdpMCET3iINK5LVa-nS3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
سپاه پاسداران: به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
🔹
این پاسخ…</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/438414" target="_blank">📅 11:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438413">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2Rc1qJOWpJS31T4CWKgCcceqyK8ENkN1GZftsc6R0vyVzTsPBnNWPKfsiZ99EJjZ9JLYCNTMq1SjWq9_xu0DeZLugmjhD_4zDJGA1HNejt-qCsO8DzUkCMbsgVvkN9R-oxOc23nwiwxnZf65Hf5zoM5_3H9rsiqgl4C0b1PGFcPB437OE07IIDCwUH1XrxLfQgStacVdvbZkYXIS5N4Fdh9sjAJh4num7u2JWA2H0bARiAJoCHw9Ov3h7LUjXpLGWDWRm1Kui6rNpNqYU3GQr1V4SThnHd4Js24hFLP-5xo80r-1gac1Ym4WTxvjE-AZPkAbbiwjKWle5w7UFatjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تبریک اژه‌ای بابت انتخاب مجدد قالیباف به ریاست مجلس: دکتر قالیباف حقاً و انصافاً در جنگ‌های ۱۲ روزه و رمضان در عرصه‌های میدان و دیپلماسی جهاد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/438413" target="_blank">📅 11:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438412">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hem8v-iO9WAGE-8WkUBCaWNwokwVSRPBIhlk8j4OOmJtQfcCMzi2ZZv5W68MD7aO5zCYOwSU55SKE2Y_J2Cvc1Itr3REmGqa4-RymHTuoJIO6D2xTaCZZzRzUg5UHz5IXfnRSlT5c3Poh-ZexGR_zddVswThj7CbozDYD53YprbiXZy5J38HwlX6LohvT9JslzUDX-DmgWj9HsB3YFonzOt-t5-ozTRa2K88Py63iRYarJPY1jCkFBKdibEHHObyvEr-E1vdDYc7DaL0x5pHBKvGlFNu2Aqo3l0f_RNXchKg_IciPzTlWh9U0hhhXUPZ7NBIpYcLAdjDqZ5k-oLKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک پزشکیان به قالیباف: این اعتماد حاصل حضور شما در عرصه‌های حساس خدمت به نظام و ملت ایران است
🔹
بی‌تردید، نقش‌آفرینی ارزشمند جناب‌عالی در دوران دفاع مقدس و پس از آن حضور همزمان در عرصه میدان و دیپلماسی در جنگ‌های تحمیلی اخیر در صیانت از عزت، امنیت و منافع…</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/438412" target="_blank">📅 10:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438411">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFPvDGBizfrWbqcvfIHKN8MAcvIewCilZvocN6QDSAV5oEqkfzs7gJGkLiCc3t3VmUks_V7nO7Z5ZWm7MJNDoP0dVQQlfdPB7R75J8IeWivHZWB8NV72wAqh8dir2xaqAq4H7hfiRoJaF5-pGqlorQWsJ_rb7uOeTfRB_W5Y6YSGzE79ElLL8PtRs40fvf-TsCILIB0-EnGIu-ECPuZgFKJEjYpx66odiHNXRRxWGB2c6oF_r_L9HQ2IW57hCmcms8-3JIJHDbJHdZ8OWoMs3l-bvj5t4-wD3DysrjIqS8fky97UP8uE2VK2nEThzpjlz1Krk94fZqukeOcEUjBxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: شهید شیرازی تجسم امانت و ولایت‌مداری بود
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا با حضور در منزل شهید شیرازی، فروتنی، تواضع و اخلاق حسنه را از ویژگی‌های برجسته آن شهید برشمرد.
🔹
سرلشکر عبداللهی: از همه مهم‌تر و به‌یقین، شهید شیرازی مورد اعتماد و امینِ رهبر شهید انقلاب بود. این امانت‌داری در حساس‌ترین پست نظامی کشور، نشان‌دهندهٔ ایمان راسخ و بصیرت راهبردی ایشان است.
🔹
حضور و مشاوره‌های آن شهید بزرگوار، با توجه به اشرافیت کامل ایشان بر مسائل نظامی، امنیتی و راهبردی، همواره راه‌گشای مؤثر در برنامه‌ریزی‌های کلان نیروهای مسلح بود. همه فرماندهان – اعم از ارتش، سپاه و فراجا – از وی به نیکی یاد می‌کنند و او را الگوی مدیریت جهادی و ولایت‌مدار می‌دانند.
🔹
مسیر ایستادگی، استقامت، صبوری و مقاومت، وعدهٔ الهی است. ما در برابر دشمنان ظالم جز این راهی نداریم و پیروزی نهایی از آنِ صابران است. در این مسیر، بی‌شک صبوری و شکیبایی خانواده‌های معظم شهدا می‌تواند موجب افزایش روحیه رزمندگان ما در جبهه حق علیه باطل گردد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438411" target="_blank">📅 10:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438410">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8405a51a28.mp4?token=YCt4G2JaypC9rI-KfrLlEyZ4XlI_uwc_wZV2ITWl7cBiJUHbN6DU5iQEVNup4a7V3Vu_YmoNz37Uo73ODwHpW4KGppaUJsZm7hDKBsDRPkTjg-wmwGSUdl_cvxi2GbXL4RFINE2lcaveqEnKdiMcPsKw4ADXfJDoyb0sVk0yiK51lwx6RCmB0_4x7pj-UeFALVG1kJqUhVgSENjgyziPwL558gVNpOqcPbY0po3mndhViCWrfCqQop_cU9ucpz17-hsa4eDzQkWtJXWecFUT9pz49swaNK7ymYxkjac9iyo7VnJZikHuONE064dQWAm9i7sf00ktf6XWdFj9MHbicA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8405a51a28.mp4?token=YCt4G2JaypC9rI-KfrLlEyZ4XlI_uwc_wZV2ITWl7cBiJUHbN6DU5iQEVNup4a7V3Vu_YmoNz37Uo73ODwHpW4KGppaUJsZm7hDKBsDRPkTjg-wmwGSUdl_cvxi2GbXL4RFINE2lcaveqEnKdiMcPsKw4ADXfJDoyb0sVk0yiK51lwx6RCmB0_4x7pj-UeFALVG1kJqUhVgSENjgyziPwL558gVNpOqcPbY0po3mndhViCWrfCqQop_cU9ucpz17-hsa4eDzQkWtJXWecFUT9pz49swaNK7ymYxkjac9iyo7VnJZikHuONE064dQWAm9i7sf00ktf6XWdFj9MHbicA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فواد ایزدی: ایران نه غزه است نه لبنان
🔹
کارشناس مسائل آمریکا و بین الملل: پیشنهادم به مسئولان این است، من اگر جای آنها بودم اعلام می‌کردم که هرباری که از این به بعد به ایران حمله شود تنگۀ هرمز یک ماه بیشتر بسته می‌ماند.
🔹
اگر با این نوع حملات به‌صورت جدی برخورد نشود تهدیدها ادامه دارد.
🔹
ما به آمریکا امتیاز نمی‌دهیم ایران نه غزه است نه لبنان.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438410" target="_blank">📅 09:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438409">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b67c9b9a.mp4?token=m39xial_m58wAciVIuxH02kOYIZV_oduDXYH_0pBaCFxEpm72kfBYC9QTVBngbrzesjfEIO3N8PCpBaM8MJMP4FgAUIpkzqbMW1Vnj4bHKPu_sPM7w4Mg8rl75JH5UONaY4YE558yNIVHNLu_oJs_ImxtcO1dXDlCAtgDv9ruF8WV9crYXfv95Tyvli3akedIx6xX65yKD39mbnr_ZSh7qE5yDLpF4vg18U31a6lWc0OGaw55UTglTuxDGWXOQ49MH3JLdYxtQdQIE-3ibolGRLtE3HzuGjljdjh4-TQUjv8Rui5qIqOg2mcq1PbIOpS6GOfVWlWpNCsIv56F5oelg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b67c9b9a.mp4?token=m39xial_m58wAciVIuxH02kOYIZV_oduDXYH_0pBaCFxEpm72kfBYC9QTVBngbrzesjfEIO3N8PCpBaM8MJMP4FgAUIpkzqbMW1Vnj4bHKPu_sPM7w4Mg8rl75JH5UONaY4YE558yNIVHNLu_oJs_ImxtcO1dXDlCAtgDv9ruF8WV9crYXfv95Tyvli3akedIx6xX65yKD39mbnr_ZSh7qE5yDLpF4vg18U31a6lWc0OGaw55UTglTuxDGWXOQ49MH3JLdYxtQdQIE-3ibolGRLtE3HzuGjljdjh4-TQUjv8Rui5qIqOg2mcq1PbIOpS6GOfVWlWpNCsIv56F5oelg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاری کویتی در محضر قرآن رسوا شد
🔹
قطعهٔ «عاشت یدا ایران» با صدای یونس شاهمرادی قاری ممتاز ایرانی، در پاسخ به آهنگی علیه کشورمان که مشاری العفاسی قاری مشهور جهان عرب خوانده بود، منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438409" target="_blank">📅 09:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438408">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTy_PRZ8PzOoE5PpgkqM_RATtWceoS9ME9x90C2WZOs6l4w7nX4J7oBmNLCB_yBuJ4UPyy7Fwm0EkvubfekhuR1LvOjSUb4-Ey0kVZZRRaBeCW_px7aGc41Z_Loh1oX4WiSsFVFBwHnlV2cVyW2GCCpb5A1xqcWrrlI_QOPwVE18FyrslbmbHgQCtjjaVYblqyZ1BTha4xcjU1vEkC5EGz3Q3BSDCBr0_DTTUPbcPOkqLWE9qgFicsOuKOj0N0MwlWshjmd6v_k7HYaOA2e55QklZVyx5nedlOt7Wk-NOr1STeaVUarx0hBTPUOVY9-wcmD-Ki14mZt9m_uDvkRX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت به ترامپ، بوفالوی بنگلادشی را نجات داد
🔹
یک گاومیش آلبینوی نادر در بنگلادش که به‌دلیل موهای طلایی و خاصش به «دونالد ترامپ» معروف شده، پس از مداخلهٔ لحظۀ آخری دولت، از قربانی شدن در عید قربان نجات یافت.
🔹
این حیوان ۷۰۰ کیلویی برای ذبح فروخته شده بود اما مقام‌ها بعد از پدیده شدن آن به‌دلیل شباهت مذکور، با ذکر نگرانی‌های امنیتی مانع این اقدام شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/438408" target="_blank">📅 09:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438407">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350d4094b6.mp4?token=rZegTYq268IqKw9pWIBzV-V07pG426KdCHPscfCLl4VKY8JvmGBTbQhNG-wHRCBiqCDQxXspG0bh2bwlmchNKAxjoOMQOPYMfpHkKuz2Lt60u0y50FE9hH2JGndCSFX4MRxzrGr3oXDnYO8kZC2Nz5n6rbQ2OVOnS-x4Rc925Isavr50ITK7XWfjnj-HkseSLGp5PESmwfitsi6SN8B5Q971onzbvPNhNXrAoOXRdvBS0FUcL7Ddqvp3iVf5977rW9-zLYZr0C1A3sMwTaiWwYus2Lc0UMgdt58V-ekASUxz9042liUlaEE2uzW0s_iyigZsQRTE3LjMv9eHm27MNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350d4094b6.mp4?token=rZegTYq268IqKw9pWIBzV-V07pG426KdCHPscfCLl4VKY8JvmGBTbQhNG-wHRCBiqCDQxXspG0bh2bwlmchNKAxjoOMQOPYMfpHkKuz2Lt60u0y50FE9hH2JGndCSFX4MRxzrGr3oXDnYO8kZC2Nz5n6rbQ2OVOnS-x4Rc925Isavr50ITK7XWfjnj-HkseSLGp5PESmwfitsi6SN8B5Q971onzbvPNhNXrAoOXRdvBS0FUcL7Ddqvp3iVf5977rW9-zLYZr0C1A3sMwTaiWwYus2Lc0UMgdt58V-ekASUxz9042liUlaEE2uzW0s_iyigZsQRTE3LjMv9eHm27MNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گُلی که خانم
ضعیف‌الحجاب به آقا هدیه داد!
@rahbari_plus</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/438407" target="_blank">📅 08:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438405">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f4b20d15d.mp4?token=g5lTDMRklXXlAEhKx2BneA7voSNtReNou1p47MXnxP9HQ2rdsi0ebFmREEb5YQ-eIK-eJbRFYwRkOoQJXQtsmtrNmYScQy03a8gUIwnSBGs2aogi0rpdnJ8BXH8wwvtoes7WjESN8fir4evk_oEWVWtKi0Ao4I2MVlZTBGUGKsekexi__zpc0-TjyVRV0aE09zSudCupYiS-BFbblIVFRTzM2RwUnKPPvPowe1SBxE79mDWBr8QR0nHyZAS2lSZ9k67Q0FtM9VnNkMwrILtpZg78R4u2nPkqf9zgkDUKhcGf_ahuaH9C_uRVwdsdh898_sSYgMkzUjko5H_UzasrTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f4b20d15d.mp4?token=g5lTDMRklXXlAEhKx2BneA7voSNtReNou1p47MXnxP9HQ2rdsi0ebFmREEb5YQ-eIK-eJbRFYwRkOoQJXQtsmtrNmYScQy03a8gUIwnSBGs2aogi0rpdnJ8BXH8wwvtoes7WjESN8fir4evk_oEWVWtKi0Ao4I2MVlZTBGUGKsekexi__zpc0-TjyVRV0aE09zSudCupYiS-BFbblIVFRTzM2RwUnKPPvPowe1SBxE79mDWBr8QR0nHyZAS2lSZ9k67Q0FtM9VnNkMwrILtpZg78R4u2nPkqf9zgkDUKhcGf_ahuaH9C_uRVwdsdh898_sSYgMkzUjko5H_UzasrTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز و فردا در کل کشور دما افزایش خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/438405" target="_blank">📅 08:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438404">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج‌فارس، در فهرست سیاه آمریکا
🔹
در ادامۀ دشمنی و مواضع ضدایرانی آمریکایی‌ها، دولت ترامپ از تحریم سازمان تازه تأسیس «نهاد مدیریت آبراه خلیج‌فارس» خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/438404" target="_blank">📅 07:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438403">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
سپاه پاسداران: به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
🔹
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع‌تر خواهد بود و مسئولیت و عواقب آن با متجاوز است.
و ماالنصر الا من عندالله العزیز الحکیم.
روابط‌عمومی سپاه پاسداران انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/438403" target="_blank">📅 06:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438402">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ماجرای درگیری شب گذشته در شرق هرمزگان؛ تبادل آتش بین ایران و آمریکا
🔹
منابع خبری به خبرگزاری فارس گفتند که صداهای انفجار بامداد گذشته در شرق هرمزگان و حوالی تنگۀ هرمز در نتیجۀ تبادل آتش بین نیروهای مسلح جمهوری‌اسلامی ایران و نیروهای آمریکایی، و فعال شدن پدافند رخ داده است.
🔹
براساس این گزارش، چند فروند شناور آمریکایی تلاش داشتند بدون هماهنگی قبلی از تنگۀ هرمز عبور کنند که با واکنش به موقع و قاطع نیروهای دریایی ایران مواجه شدند. ایران پیش از این هشدار داده بود که هرگونه عبور از این آبراه استراتژیک منوط به هماهنگی با مقامات ایرانی است. این شناورها پس مواجهه با نیروهای ایران، ناگزیر به عقب نشینی و بازگشت شدند.
🔹
در پی این اقدام آمریکایی‌ها به سمت یک پایگاه نظامی شلیک کردند و در اطلاعیه‌ای رسماً به تجاوز به خاک کشورمان اعتراف کردند. با این حال، ارتش آمریکا بلافاصله اعلام کرد که این تبادل آتش را نقض آتش‌بس جاری نمی‌داند.
🔸
گفتنی است تا لحظۀ تنظیم این خبر، جزییات دقیقی از میزان خسارات احتمالی از سوی منابع رسمی اعلام نشده است.
🔹
در دو روز گذشته در پی ماجراجویی های ارتش امریکا، درگیری‌های پراکنده‌ای در آب‌های خلیج فارس گزارش شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/438402" target="_blank">📅 06:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438401">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuyspg2NMW2T2L6M_UuyvuWCzRW76czSJpcGlml5AzBBW9m9L-ETXXbYuyroPecNK-cf_RemMRWSvvh8tz_qJrp5JIeXIyT4N07sFIqhb7Mh_lRnVT1ooolZK7LHuk0YmEgAV-hpADY6oEaZss49w_YZF5qS-v2vyJYwvPEu684p9Cy9w5-5FwvqRPlmiuT-y5-JcB8CLUgaTO09Zv7VgZKi91ZbX-XFMPl_0xS0bkZ1qSG2Euwhf4pXrQz7nRS-mDWB-pr5SMPwSzxS2LxLAXlfzGNs5fcTHKlIsoTFtrYOG9gqCL3jojQ9wGDed_rKcGi3bD03AyeTaE-461Dfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بازداشت برای وثیقه، با سامانۀ جدید قیمت‌گذاری برخط
🔹
قوۀقضاییه: با راه‌اندازی سامانۀ جامع وثیقه، دیگر نیازی به ارجاع پروندۀ وثیقه به کارشناسی و بازداشت متهم نیست، و قیمت‌گذاری وثیقه به‌صورت برخط انجام شده تا در صورت کفایت، پس از توقیف سیستمی، فرد بلافاصله به منزل بازگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/438401" target="_blank">📅 05:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیمۀ کامل معلمان مدارس غیردولتی اجباری شد
🔹
محمودزاده، معاون وزیر آموزش‌وپرورش: با پیگیری‌های سه‌ساله در مجلس، مصوب شد که معلمان مدارس غیردولتی باید به‌صورت سی‌ساعته و با بیمۀ کامل در ۱۲ ماه سال تحت‌پوشش قرار بگیرند.
🔹
عدم رعایت این قانون تخلف محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/438399" target="_blank">📅 04:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm4HjlrXyEPW8Z4HG99ZI5vRQjaqpsKf8KeZAG4l_GKlbyXzAb9HzTIVWD98VrW9IFTVRUPaCtMicTXeqs_bzx8vUnNXCug4uQJAPYWp8eaSpLeATmyjEwLOesHD4bF6mU-l7Afsjb34T76aQT3OJJ2RMUYsFKeYdo7N2_WSTrRxducQOGBP2Ywn3yQkm3j7kumd9CmfwUEgyUuC5OjB4_5g0NsasgS5IDKrdCZBmMemPMFYzDour6orogvvAaJxJi7irgytovS2QIUqHSh1qlmzSmwomTK7SeGL6yvlAgZTKvxjqEiYYi8ErNlr56YOpDguyDVtWQrBSDc5jCpP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lj3kqKv_FJnSSTiz0pUaKNDK4LXgURVzHMXDiqgETso0rhD-0mCDErXrSwoNLYMK3XL6k36BjWGjlOpnCOL1HyCPjtsqs0raQ2hCXIb9WUepi8b4lU2pLxQR7KrKGq-BmJS8xxzU7f9K02OHBbF6nHya6XnkHUOSR9GJcuu_YSjKeVi1XbBJYGTNFHvytRjVPUBx_KW6eg8ZL7OS3ES04T_yvlWMGyL9CYyF9J8GAb0HIpUw3mosP0cQbDWLLobK4mg3bTP0EdSg-0eb7AbMJIqCAph72IyE0EpcJHUONa2MwUlhmm2Opr246EbES4leD8CQVo6hNodLhg_N0VShmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbY6pNF8VRyXMuNwWuCBQz8_29x0_hhLAv2m1VmrZlY8cV4wp36-PorWo-CmyKNE18NQQCC4bP9Fqf1eXl4ZfJCi2FBICYvhXAKB1nHVza3Iog4UYTcFNcvRlVzTg7EtdHHHScha1V6-LcRG_Y7cL3OflH7rax5kyjyhi7CtEe7uJMnU9csq0fln37uth_CXS6_udZF6GuGQUHQZrZT-gE4_hMyd_lDW3qNOUFdaRfXKmzKMp_iMcW9dxhGxdahcNdXCAQvSRDh1gDGhgXuqMzZNEObQAFCj9yldn1v3zkbxz36Oz65tpyDov4g_UG38fnIx9TJzg4uYW38fTxplcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptx16LX6AXYqW4F9TNLfhd_AVecDCXniNadXGKMkAgpzgKlvv0JrB8bdmG5H6d_tdR8utDs3FLXDkgguF0WS_KnhoRqsZ1hYAeDjairGHA68dz7TTCum66OlR1FM2BftLFpnrIabIetYm0GG88uGhibaB2u065hiH1hbMIo-6XPdDSFyei1Y-hfgoVOHEdidCP3ByuHfWeX-q45-uHLd57RuKwEd-flC9JlORfMI_MUMyss086IF4xuvBzPq9wWSy0A0cHDZu3OgpeDWOsKs0X8kxWoPekt9imqK5sLLfwFWsy9arh5N_6ZodFUFxDOguL9iT4o3JuiMaLgrvkOo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bye6yJJp5FjJGmjdsGHCGeTB72m9oLacBws_T7zW7ByBNjH5G1l9suKIBjvbsSn1KVYFVjubY4u6L4aQj5QwgE_UAnI9KIaFXeXAzLsdmLIXPX3FyjWXPDbFtI7Xk-noHPJ8e3tQhG4tl7t22S2J-bclm8a-r4DddNkn4w08hXbkSlsXMtvTW5r7bGtxsRRKvWK7ofUC6Tz2FUkrZ5k08GYqcgDg3kSU_58K9wnamwawpHpS328wBCnyWVERG5MHy2kafmSPA5FVb08v4rQxLkNmeYb38NjX2ggCw84nsIlC3RYWvVCVEMeUY_o8GGo8ZPH_kq6mIrXOujBsY_dz7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسیر ۳۷ کیلومتری تندرستی در منطقۀ ۲۲ تهران افتتاح شد
عکاس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/438394" target="_blank">📅 03:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438393">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBfbJbYvBbhJS5rXriMSwdw29dxlZ1IlKlRlQeTjO8otLnpUqRdLECv2r4xdR7UHptD2MDUciSqKvlmRNwRGTGfCUbGTxSu33t2NLijYjNvDGGgyv2lbsztzXk110O-0asEZpoh8HfHgdVDklZjE8LereCy1muVbEpccdKeSnWcw0HY2A8ItqTIZEqe100Ah6C1M0TmQ6eAdEoAJ1dhVMhNT3ldeNAQN788HEW75cCUmCg038WCUFpYqBtHBS-uZF3nrxW9hr3UN-vM48K3FBLOwXP0wBPzFdKRwPrN0e4tPHyP8Mmr6ywd2u3rZ8hDw2IWpgQQ89busMvdpxsH48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیّران در سال گذشته ۱۲هزار زندانی آزاد کردند
🔹
ستاد دیۀ کشور: در سال گذشته ۱۲ هزار و ۶۹۷ زندانی مالی غیرعمد با مجموع بدهی ۴۷ هزار میلیارد تومان آزاد شده‌اند.
🔸
هم‌اکنون حدود ۲۱ هزار و ۶۷۸ نفر در انتظار حمایت خیرین هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/438393" target="_blank">📅 03:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438392">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
🔸
طی ۴…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/438392" target="_blank">📅 02:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صدور احکام جدید بازنشستگان تامین‌اجتماعی، از هفتۀ آینده
🔹
تأمین اجتماعی: صدور احکام جدید بازنشستگان از هفتۀ آینده به‌صورت رسمی آغاز، و احتمالا تا ۱۵ خرداد به پایان خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/438391" target="_blank">📅 02:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
🔸
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقۀ هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
📝
اخبار تکمیلی متعاقبا منتشر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/438390" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438389">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
شب هشتاد‌وهشتم خروش جان‌فدایان ایران در قزوین
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/438389" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438387">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1180119de.mp4?token=VW1kG_7Xr8O5Gpk3eZYYlejyto6ukiL2idg4y0ZBMq8Gf2mYCR7rBo8Dg8Bhy3coq7_rNflwvYnF4EPdfTGWaiEfmRt_8GGFA340cdudJyAMy6KUxRA-1-TY1QqNQop6RtrniBEPWit6KGvE1ohsw_ggvIwlsEqtEGHfLob7tkFIvhrC1pg9DST3A71orAYWI0WGP-Sey99hqLaOHrmFbQIqx6WmbUIz8DHKfIUe8ZBFuq7Tl_vXAMnaqzO7GuOAeTXE8eFTc-8CNW520XvZFqkvoCa88Qtw-t4pG1zW83xW6sJ8mHVUqV2x90riyKFrPLxh8tR2_EjdBvZTeXvNEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1180119de.mp4?token=VW1kG_7Xr8O5Gpk3eZYYlejyto6ukiL2idg4y0ZBMq8Gf2mYCR7rBo8Dg8Bhy3coq7_rNflwvYnF4EPdfTGWaiEfmRt_8GGFA340cdudJyAMy6KUxRA-1-TY1QqNQop6RtrniBEPWit6KGvE1ohsw_ggvIwlsEqtEGHfLob7tkFIvhrC1pg9DST3A71orAYWI0WGP-Sey99hqLaOHrmFbQIqx6WmbUIz8DHKfIUe8ZBFuq7Tl_vXAMnaqzO7GuOAeTXE8eFTc-8CNW520XvZFqkvoCa88Qtw-t4pG1zW83xW6sJ8mHVUqV2x90riyKFrPLxh8tR2_EjdBvZTeXvNEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات رژیم‌صهیونیستی به شهر «صور» در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/438387" target="_blank">📅 01:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
شهادت فرمانده ارشد کتائب القسام تایید شد
🔹
جنبش مقاومت اسلامی حماس رسما شهادت «محمد عوده» را تایید و لحظاتی پیش، طی بیانیه‌ای اعلام کرد: در سوگ شهید قسامی، فرمانده بزرگ مجاهد محمد عوده (ابوعمرو) که استوار و سرافراز در میدان‌های جهاد به فیض شهادت نائل آمد،…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/438383" target="_blank">📅 01:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeZI7IdwfNJNXEMyZKNNIxOOg-XQdJBR0beQR7hMB-Eol4eDzJV502iWvAh5WOj0UfS22ineAASehc0wIlpfDkiwBwiG6h6tR69fL4piSZ8_apBpkDxD6ctLgTXs5PoWpbbwyqnO_mmb1f3oPAHblLEegviD0r4EyHTMJSryx1ppSyXZvozNARPm_vm5MjyxLerVkd1jN5Q1iOn9SsD6ljxUNG5fNBpCdlqb8sabqIxBGncVyjQhUcqmdg1eTQrtG_rXjx5-8Fvl0-vOYXj9Qz16tGLKT0MsO7YHaehP8vCW6eErpwulnBdkaRvX9c69vt91CFvFjjb4NaQ0M1Ft6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً خبری از خط‌زدن مصدومان از تیم‌ملی نیست
🔹
رسانۀ تیم‌ملی ادعای برخی رسانه‌ها مبنی بر خط‌خوردن هادی حبیبی‌نژاد به دلیل مصدومیت را رد کرد.
🔹
رسانۀ تیم‌ملی دربارۀ این گمانه‌زنی‌ها نوشت: کادر فنی تیم‌ملی مطابق با زمان‌بندی و مقررات اعلام‌شده از سوی فیفا، تا آخرین‌مهلت قانونی برای بررسی شرایط بازیکنان، ارزیابی‌های پزشکی و فنی و درنهایت انتخاب فهرست نهایی ۲۶ نفرۀ تیم‌ملی فرصت خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/438382" target="_blank">📅 00:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvEr55GalstLgDGtbihdkaaAJat3ZN_h48Tl69ocgiVTjnTnoHa1xvXCcpFURvNbZHHDr1AZr_HDhSKvmGj-PgMrFC1f1ZpN72RFm-163muwt16xIyJhnppocSHGb-ssakiHlKGpalzMvfn48DCmTiK6F-tf_uBmtNS8zz74p_HiM1qJPRHJ_wPiAI2uxsxYKEsV4zg8FFtgWqOj7_6gnnv1VjTlG02FCd49sJzZBsxVC73qZRfZf70W9CHAa9dmyxl7ouazSV4moUJy7wdnjrXRpLmaiIVslWIleuZXunmjDnb8kcgcMqClgqq7Og6c9v9rTbcfZemRRwf91JphGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند پرداخت خسارت خودروهای آسیب‌دیدۀ جنگ سرعت گرفت
🔹
بیمۀ مرکزی: تاکنون خسارت بیش‌از ۶۶ درصد موارد ارزیابی‌شده، به‌طور کامل پرداخت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/438381" target="_blank">📅 00:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438380">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYKRRypSbrJGlimsULL5iEsGmcRYJ6sN3CAgmSYsGitHQMeOF9RXy2KqBqHDuBjDYjrCkAWBZ9WWKdmfK2Etwp_lpwZAmAWsDAEIM3xQDgejg8GZ4-TLks2OMHg3ZfpOIKCFoKtlIYD4Udb1ekbXXBxyuPDMiWZ0vnsdumeAQYol48Rb3XxUxyD2KThJKhTk_N739DyxUBJZ_wFErO6_zVwqF07Av8nrWNrVDmOOwWQHoNKfzGj3Nh2D3dM0yTZasb_cnIs5LSBEiPXq-bhEWq3snIC9ncl7rDtAEcP164R045SwBxuJ2ZVCxFvw0WiBcog_3uXrRIEQKqTRGFFVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دزدی اثر انگشت از عکس‌های سلفی
🔹
کارشناسان امنیت سایبری هشدار داده‌اند که هوش مصنوعی می‌تواند امکان استخراج اثر انگشت از سلفی‌های معمولی را فراهم کند.
🔹
براساس این گزارش عکس‌های با وضوح بالا که در آن انگشتان در فاصله کم‌تر از ۱/۵ متر از دوربین قرار دارند، ممکن است جزئیات کافی برای بازسازی اثر انگشت را در اختیار مهاجمان قرار دهند.
🔹
در سال ۲۰۲۱ نیز پژوهشگران نشان دادند که تنها با یک تصویر از اثر انگشت، نرم‌افزار ویرایش تصویر، چاپگر لیزری و چسب چوب می‌توان نمونه‌ای جعلی برای فریب برخی سامانه‌ها ایجاد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/438380" target="_blank">📅 00:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438379">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVimRDScxu_nRF7sRfULDznYXT-LRspR_nJIhIT9lz-Pg-HzX4xMkMSIdPMlYp7ENxw1lm2MIqvcipaYpEw0tmyGThFdI_NDku7Bu4W1nD16Sf4w3qwub3MYsY55LnKKni9HWNKNRU3XODpTsdctauCMrhEj0Z9Xa7716xvjfJl_V9NA8GF_XGfvF33GUR8SV6xYhdwAlJ-4YcCJrz0Tit-JZ8Yf5xzMdlewUaHumdYDU-SLrKHFcjdzKNy75DJSkxLXkRxErNh3tiZhpXECfAllwb33sEMwsoN5XX_gTfK0Pov3ysT8nCsCNKu1SkoNvwCB8BZwp84omONbmnEqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یخ ابهر و سلطانیه
🔹
روزی شخصی ساده‌لوح نزد مولانا عضدالدین آمد و سؤال کرد: «یا مولانا! یخِ ابهر سردتر است یا یخِ سلطانیه؟»
(ابهر و سلطانیه ۲ شهر نزدیک‌به‌هم در زنجان هستند).
🔹
عضدالدین که از بیهودگی و سردی این پرسش شگفت‌زده شده بود، بی‌درنگ پاسخ داد: «سؤالِ تو از هردو سردتر است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438379" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438378">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
تجمع هشتادوهشتم مردم آستانۀ اشرفیه این‌گونه بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438378" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438377">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271065f03f.mp4?token=TfPs_9W-8yPP_rYOdaBILk6iki-JAYLXfGvsE06oAFpjEyGjE_DHauquGVgVKzJHbs0NjqM2sXC-2pkUtFw17QSQFZlJMhZA27QtvW0SOh-flfPhuj5p5xJG1qF_uQWowUNio24yNObkyxv4mpebSDAM0bsPdvE4Fnr6L4uCUisfc49tio0bEsj40PiYkmKZ7vAuDDHEV5iU3algOW2vgkLvxUINYwDKKeFHQIkQKsDZ98vtPhJTF7a5neSYYQ9WFJ5VjZta5SLbe9Dpu-nEFW4LnicaCgRZXN7T7Q2XSUbTA3aRe4P24g1cn4inMDjsC9ZTpysRIJl4JRiuGpdR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271065f03f.mp4?token=TfPs_9W-8yPP_rYOdaBILk6iki-JAYLXfGvsE06oAFpjEyGjE_DHauquGVgVKzJHbs0NjqM2sXC-2pkUtFw17QSQFZlJMhZA27QtvW0SOh-flfPhuj5p5xJG1qF_uQWowUNio24yNObkyxv4mpebSDAM0bsPdvE4Fnr6L4uCUisfc49tio0bEsj40PiYkmKZ7vAuDDHEV5iU3algOW2vgkLvxUINYwDKKeFHQIkQKsDZ98vtPhJTF7a5neSYYQ9WFJ5VjZta5SLbe9Dpu-nEFW4LnicaCgRZXN7T7Q2XSUbTA3aRe4P24g1cn4inMDjsC9ZTpysRIJl4JRiuGpdR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع مسلحانه مردم در هرمزگان
🔹
مردم شهرستان رودان هرمزگان امشب سلاح به دست در تجمعات دفاع از میهن حضور یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/438377" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
تجمع پرشور مردم کاشمر در موج ۸۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/438376" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عضو تیم رسانه‌ای هیئت مذاکراتی ایران: سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود
🔹
سعید آجرلو: براساس پیشرفت‌های فنی که در قطر رخ داد، قرار است بلافاصله پس از تایید تفاهم میان ایران و آمریکا بخشی از دارایی‌های بلوکه‌شده ایران به‌صورت غیرقابل برگشت در دسترس بانک مرکزی قرار گیرد.
🔹
در بطن تفاهم ۱۴ ماده‌ای چند اقدام ملموس و عینی گنجانده شده که برخی از آن‌‌ها این موارد است:
🔹
در دسترس قرار گرفتن اموال بلوکه‌شده.
🔹
معافیت تحریم‌های نفتی، پتروشیمی و مشتقات آن.
🔹
رفع محاصره دریایی.
🔹
اگر این اقدامات توسط آمریکا انجام شود ما وارد مرحله دوم خواهیم شد و در غیر این صورت اساسا اعتمادی برای ورود به گام‌های بعدی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/438375" target="_blank">📅 23:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5501a453.mp4?token=oxfbyk60D0CTQrv7vGugor3ySExOV6IQ19vt3nqb1HVlWq5Ew-ElAu_WAW1aZ91Y0Q8ARbYyDNN77o1m4RSBD6OhairNMJ22d62KWxRBdbVOSwzz_95jwEI93s1o6lIP-_TdmPtzQQByMyDtg1iWlOe8UBxBnKaI9HkwZnA9j53FkG1sHUem3Z930y1X_AkrRHt9lWUvi0aqWxBH2QBXTW6SL8tPiGnYFcaaT5ONJdKmV4QOlnVb0Wt_pBHa2Nk0KkbZjG11Bt_XGCju8Tnao5ypghxovQjxcx0RF0cqdOrgnfP3Dhl_c0dp4zYLz9NnVmmd6Y3vvtKpW3oOcQjYHEAku110m1K878e3U3f3tN9UPhaNRLP0UlS5KPk-V2mBG-xhfaVkTYp4k51O9t9DBoEZkNOQRyY2amvFBb3Vl8hOZhgYcb1VP3LOiTE8na8_3pB078WViP0QMxMPal6d2_6KWUVmH_xc75ct2tSG4RhvhxdTv2VXfVEbSK8-lGtMiIDhxul4YLIGIrbn8twVWGsMzSbwHL5U0gOXhpXNNy_xPSGSLirS-YoG-RPpfk_VlgqTfclHxoEZ-ZV48iO8Qw1tkh-FCDJQ3ZRqr75jqQkCag7Lna8GY-B3Wpqug7LD7Q5LCJLn5iDN2wFmDdIlkdHKRAbVKXBRP9chMFPgjnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5501a453.mp4?token=oxfbyk60D0CTQrv7vGugor3ySExOV6IQ19vt3nqb1HVlWq5Ew-ElAu_WAW1aZ91Y0Q8ARbYyDNN77o1m4RSBD6OhairNMJ22d62KWxRBdbVOSwzz_95jwEI93s1o6lIP-_TdmPtzQQByMyDtg1iWlOe8UBxBnKaI9HkwZnA9j53FkG1sHUem3Z930y1X_AkrRHt9lWUvi0aqWxBH2QBXTW6SL8tPiGnYFcaaT5ONJdKmV4QOlnVb0Wt_pBHa2Nk0KkbZjG11Bt_XGCju8Tnao5ypghxovQjxcx0RF0cqdOrgnfP3Dhl_c0dp4zYLz9NnVmmd6Y3vvtKpW3oOcQjYHEAku110m1K878e3U3f3tN9UPhaNRLP0UlS5KPk-V2mBG-xhfaVkTYp4k51O9t9DBoEZkNOQRyY2amvFBb3Vl8hOZhgYcb1VP3LOiTE8na8_3pB078WViP0QMxMPal6d2_6KWUVmH_xc75ct2tSG4RhvhxdTv2VXfVEbSK8-lGtMiIDhxul4YLIGIrbn8twVWGsMzSbwHL5U0gOXhpXNNy_xPSGSLirS-YoG-RPpfk_VlgqTfclHxoEZ-ZV48iO8Qw1tkh-FCDJQ3ZRqr75jqQkCag7Lna8GY-B3Wpqug7LD7Q5LCJLn5iDN2wFmDdIlkdHKRAbVKXBRP9chMFPgjnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم نور مازندران در موج ۸۸ تجمعات ملی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438374" target="_blank">📅 23:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438373">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPxADsO9Pi3uTn4RcOZw6RKXu1nzl-lUMSbGUVMG0zhNk3n01UnhkZhwEal7CMtVufXhf4iqiivELHs4Jna_h2-tEIinB_FO8HciAfA5jlZL0Vnsff46U0Q3J6Q2r7JMGVQSuq3CBkAybInUn3ITHwI6OdarPoJnlrUm5EaGQANcRM1Uvr8GczYcPhI8WxfWQ6wZXIJn6Zh_M14udw6E17mEPA37tSzYquZ901WBuIBV3-e62E0wVFaT-9_y4c2AUFYqZRX2U-3bPnZw6asTpGlkXluOIrQxjSurpJtQX0xb-4wDCezxAHaxC88vxvNhclHIScKeOBODTTTggZTB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعودی‌ها از ترس جنگ خانه نمی‌خرند
🔹
گزارش پلتفرم «انترپرایز ایام» نشان می‌دهد پس‌از آغاز جنگ علیه ایران و درگیر شدن عربستان در آن، ‌‌ حجم معاملات مسکن در کل عربستان ۵۳ درصد و در ریاض ۸۳ درصد کاهش یافته است.
🔹
گزارش‌‌ها تخمین زده که بروز تنش‌های نظامی، هزینه روانی اضافی ایجاد می‌کند و  خانواده‌ها را به تعلل و به تعویق انداختن تعهدات مالی وادار می‌سازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/438373" target="_blank">📅 23:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438372">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fad9f09d9.mp4?token=AxUr1FgLFe2FeYFi0fNPUIqRMOOPMPG2zMNwQiQ6fk6VWmw4iKgPlGW-2bjz8x8X4YkbGktGNOuFXPT0vaVL1_eGMxyYPBJjJO42_2CI_absaN5pQsWVXHZ8ZU-IdPBxbsW4VnASKoHbdEurYnYlfbKlntWRFZrCZebLY7j8lh2lpPOFRkcjuaBdIl3VPNf2Doe4t15-wQPEMpYW9QXB0smvEepzj6KvV1Y55NjMEdwWWzBxo-fNPJRODzoHPTK1pXT0n8qgqtTME3lvMVggKlEwR5wshqwqLzp9TVVccKAnzqM1S0UBRtAyY5ARwUzjEYgtJ6vqP09z5gAZkf1sag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fad9f09d9.mp4?token=AxUr1FgLFe2FeYFi0fNPUIqRMOOPMPG2zMNwQiQ6fk6VWmw4iKgPlGW-2bjz8x8X4YkbGktGNOuFXPT0vaVL1_eGMxyYPBJjJO42_2CI_absaN5pQsWVXHZ8ZU-IdPBxbsW4VnASKoHbdEurYnYlfbKlntWRFZrCZebLY7j8lh2lpPOFRkcjuaBdIl3VPNf2Doe4t15-wQPEMpYW9QXB0smvEepzj6KvV1Y55NjMEdwWWzBxo-fNPJRODzoHPTK1pXT0n8qgqtTME3lvMVggKlEwR5wshqwqLzp9TVVccKAnzqM1S0UBRtAyY5ARwUzjEYgtJ6vqP09z5gAZkf1sag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان ایرانی به قرارهای شبانه در تجمعات کف خیابان عادت کرده‌اند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438372" target="_blank">📅 22:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438371">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d15d5b129.mp4?token=GCasLifVb3NeQsy578BTik1wbeZg2zWVZ8q6E-e6laGEdcKu6a7J8NmQNm4QMoxOrwaE3J534ifpHmkDgpDU2m71lsURpKqZgkClMtFsUJ0GT-ORhScCle-IPCPmZgKk88fFXzTxE6_58_YHc_Ckfs6vPH39bjdBQCDp4ptwDhQxGJ5yI4Gb6BaKtoK-sFsfCc2b-sEMu8zdfG_5MxA_DkaLrHkyGOQvgNrITJ7TEx4-Pfd7n2Uql7upy_8xllkSeum7NS7e-KHKLMM_syCjkr0jLjxY6w89kH9ERqA3uedWI2eKIy-agvFs8RxyKaMy6w29rE6qEMXYqFqNP7gtiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d15d5b129.mp4?token=GCasLifVb3NeQsy578BTik1wbeZg2zWVZ8q6E-e6laGEdcKu6a7J8NmQNm4QMoxOrwaE3J534ifpHmkDgpDU2m71lsURpKqZgkClMtFsUJ0GT-ORhScCle-IPCPmZgKk88fFXzTxE6_58_YHc_Ckfs6vPH39bjdBQCDp4ptwDhQxGJ5yI4Gb6BaKtoK-sFsfCc2b-sEMu8zdfG_5MxA_DkaLrHkyGOQvgNrITJ7TEx4-Pfd7n2Uql7upy_8xllkSeum7NS7e-KHKLMM_syCjkr0jLjxY6w89kH9ERqA3uedWI2eKIy-agvFs8RxyKaMy6w29rE6qEMXYqFqNP7gtiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تراکم جمعیت در اجتماع مردم گناباد خراسان رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438371" target="_blank">📅 22:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1u4nbIlIpFVa0ccyXlcAEZe36-EeKMD0memFJXwm5mCcuGOZ-IloBAMiQUrtpTS6zHB7uNcUiMyOlVy6122-rVKW7YAXvkPx6U6v1WALdw9Exnl0HVKxRVVvfZyO26hUtz9GYAMo21cW9H4m1W_zmhR23fxYDOzYTYx8UqvH6N16AyTRs9j5lkFKwZt1d1ctOUpuTKiKiefBT8-p-sZ3MDhjSIaeaHsjpFAxs4hlIKlvHzhQXK_jCxGVha7i8LsmpTkq-FiQScODCrkn7KOU3l-MR-XcBjotd8VCYGcVs7RDIPSbix4eaYFEhPsEIcX7NmP6t5XN9I1s0Gfe6OImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز مطالعات آمریکا: بازیابی ذخایر تسلیحات آمریکایی حداقل ۳ سال زمان می‌برد
🔹
مرکز مطالعات راهبردی و بین‌المللی آمریکا امروز در گزارشی نوشته: پیمانکاران نظامی ایالات‌متحده دست‌کم به ۳ سال زمان نیاز دارند تا ۳ دسته ذخایر تسلیحاتی که در جنگ با ایران استفاده شده‌اند را جایگزین کنند.
🔹
این ۳ تسلیحات راهبردی موشک‌های کروز تام‌هاک، موشک‌های رهگیر پاتریوت و موشک‌های پدافندی تاد هستند.
🔹
با این شرایط نیروهای آمریکایی درصورت بروز درگیری احتمالی در آینده با چین، با کمبود شدید قدرت آتش مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/438370" target="_blank">📅 22:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
لاشه موشک آمریکایی در اجتماع نیشابور
🔹
این موشک در جریان جنگ رمضان در نیشابور عمل نکرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438369" target="_blank">📅 22:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77acb69f2c.mp4?token=H8PoI_xrjaPCGJ8hUw1nMV5964YswrxL5YQbFPtF5730kt7QDMtinEPlomDJ4BdO8vNZN-WhjwmnTqjTh9nsI2JylUekpsLjqOLdkqsv_WM22wkCYN_Y2-GZAskTCwHuaABwePUDRV4SGUPI4gRAVBMU1DEMY15mJ9LBFLllQtOvCWu5SDgw3QEKkRD9NYJr3vjMAbfWT1OB4JC6ebNbnS3VWlKIgWAUb5LwV-bdvIrbe4w0DUEGGHNqaS7_Q8lEu9f17-jYExiOYyQlLhwmI0VLudFwtb5SanHeDeET4JeJB-Pzh1wt7LNg2b5yw-8O84jQmU1dI4ZZ0LV5iO6hEBceFtcGNVcJyVVs9gk4Pk9ldtp7CCF5ZrBMVuENEjw0srbzMn2GUv6H9BlccRPvaK_iEDau1mXGVdVlvTNJHO3gIpqKbF85ibfjifzcxpNpPk4XA9RGH7Wpagug6CREJLaDue5enzbXBn3L3JaQtpYkMlo_ercKDFgKKajpSTBDOkD2qvSn-XE3U_OTBmwF0CLVDA-PdgsKW81wtmuLc5ljt1TiPP5TRt0I2j-B5gs_p4sqss_uGv1pNfw9OJh-0d2xBTWEA_bteVoYXiGXj3YQeE6meN-ZRZmymOzt_fGG4Jf9LOdUt9mxUR2MtWHmH40LM-yXho8gBnSuvLIkT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77acb69f2c.mp4?token=H8PoI_xrjaPCGJ8hUw1nMV5964YswrxL5YQbFPtF5730kt7QDMtinEPlomDJ4BdO8vNZN-WhjwmnTqjTh9nsI2JylUekpsLjqOLdkqsv_WM22wkCYN_Y2-GZAskTCwHuaABwePUDRV4SGUPI4gRAVBMU1DEMY15mJ9LBFLllQtOvCWu5SDgw3QEKkRD9NYJr3vjMAbfWT1OB4JC6ebNbnS3VWlKIgWAUb5LwV-bdvIrbe4w0DUEGGHNqaS7_Q8lEu9f17-jYExiOYyQlLhwmI0VLudFwtb5SanHeDeET4JeJB-Pzh1wt7LNg2b5yw-8O84jQmU1dI4ZZ0LV5iO6hEBceFtcGNVcJyVVs9gk4Pk9ldtp7CCF5ZrBMVuENEjw0srbzMn2GUv6H9BlccRPvaK_iEDau1mXGVdVlvTNJHO3gIpqKbF85ibfjifzcxpNpPk4XA9RGH7Wpagug6CREJLaDue5enzbXBn3L3JaQtpYkMlo_ercKDFgKKajpSTBDOkD2qvSn-XE3U_OTBmwF0CLVDA-PdgsKW81wtmuLc5ljt1TiPP5TRt0I2j-B5gs_p4sqss_uGv1pNfw9OJh-0d2xBTWEA_bteVoYXiGXj3YQeE6meN-ZRZmymOzt_fGG4Jf9LOdUt9mxUR2MtWHmH40LM-yXho8gBnSuvLIkT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرم بهمئی کهگلویه‌وبویراحمد از تداوم حضور در خیابان می‌گویند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/438368" target="_blank">📅 22:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وعده وزیر نیرو برای پرداخت وام به دارندگان پنل‌های خورشیدی
🔹
وزیر نیرو: تسهیلاتی برای استفاده از برق خورشیدی در بانک ها درنظر گرفته شده که با معرفی وزارت نیرو، بانک‌ها تسهلات را به افراد پرداخت می‌کنند.
🔹
همچنین اگر مردم با نصب پنل خورشیدی تا ۱۰ درصد صرفه‌جویی…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/438367" target="_blank">📅 21:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83bb7216c.mp4?token=gGEtxNmhEGDKUYQ2Oc-0CkXT-KIolPu-C_oO_pTjrPLxfzAkEhFvsPB9526qO1WsPx2osjC3CvaZ6OndCrBU5wqQ3AC9uXLwdmlv0gktWAxIxoyfVKWQ2KBpnuTIFVME4V1ETVUW2aATBu4Vrwu5BmOUATrzyft4gsxAuh7EEpwst_-Ldet29KhHItD7dVnTT2QyN-aagm-pYj_wxV7ZkJkO6V3iOGbUDmRzfbP5h75C2vy2SRTuJ60b03Yyj-6WcdzCPRBKtqQzzbfcPw6pofDXuOWA_WqoK2hvdwe0a4fd7ylSM60DkpC1emu_rF8HhsWQKd_d400ug6to-e9o2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83bb7216c.mp4?token=gGEtxNmhEGDKUYQ2Oc-0CkXT-KIolPu-C_oO_pTjrPLxfzAkEhFvsPB9526qO1WsPx2osjC3CvaZ6OndCrBU5wqQ3AC9uXLwdmlv0gktWAxIxoyfVKWQ2KBpnuTIFVME4V1ETVUW2aATBu4Vrwu5BmOUATrzyft4gsxAuh7EEpwst_-Ldet29KhHItD7dVnTT2QyN-aagm-pYj_wxV7ZkJkO6V3iOGbUDmRzfbP5h75C2vy2SRTuJ60b03Yyj-6WcdzCPRBKtqQzzbfcPw6pofDXuOWA_WqoK2hvdwe0a4fd7ylSM60DkpC1emu_rF8HhsWQKd_d400ug6to-e9o2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتادوهشتمین شب ایستادگی مردم ایران در میدان خیابان هم فرا رسید
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438366" target="_blank">📅 21:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎥
ویدیویی از عملیات هماهنگ حزب‌الله در جلوگیری از ورود لشکر صهیونیست‌ها به شهر حداثای لبنان
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438365" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWg07jghq8Fgpx9urVxLDV8rQ7ScgapuSFXjReevtSl4-xIGiVjK7KeNYNLroQ5xg-Dn9pcGEs0iCMUgSDzUi99vsMT8kckQ2DukD_kVWuWAabOeuXNswoegS0WDNBwVm_UiBJNxCPOzE__75c8swV5aE-DTxDaakB8e3621a6boWMrf4q7zBgS251tYTwqUgIOeqYdFJ1oM_-Snszs59OsM3waSJpanTAcalPbjcJptcZsaES-hiafut-kuT3YLEYP6mZBq-LxlAo78sGKam7pQMrwkPMw86sPwTu3oq5CTsDDvfeqh0XrqIti8tUNw2TZBcpVS0OcsAcZLB7foBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ عمان را تهدید کرد
🔹
ترامپ گفت: «تنگه‌ها به روی همه باز خواهند بود و تحت کنترل هیچ کسی نخواهند بود. ما آنها را تحت نظارت خواهیم گرفت.»
🔹
او در ادامه گفت: «عمان هم مثل همه رفتار خواهد کرد یا اینکه ما منفجرشان خواهیم کرد.»  @FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438364" target="_blank">📅 21:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d124275e76.mp4?token=fL7OntDp-Z2nosXL7GsKCNUO1Ehl1G6tc6R2x15ifKVt59DDVYGJM6Wp-wgPj6z-ij76S4qtJH_7Eqs2nic-kMxleQPMQpAKYo3Avatui6isjRsBGG1DilnRc9gWsWlscW5m0-9Y29imlNdActvkM-Dfl4ZMo5jI5lZgT0ny1wlUdY28G4YAZezmPUwyyln2WyoBvvNjAGwWqBl6UvDAyGutlVsFeiuC5gQvbOgzrpx4cG9Gi1lLE30QX2LIUZTXStpqg_JEituX8x0h5RtjqLF4X8agVIwyrlODMcSPBtd-8Y4Jt48P7Sm4_7OvMeWSvXeEDrs6JD0ylPrphsgf3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d124275e76.mp4?token=fL7OntDp-Z2nosXL7GsKCNUO1Ehl1G6tc6R2x15ifKVt59DDVYGJM6Wp-wgPj6z-ij76S4qtJH_7Eqs2nic-kMxleQPMQpAKYo3Avatui6isjRsBGG1DilnRc9gWsWlscW5m0-9Y29imlNdActvkM-Dfl4ZMo5jI5lZgT0ny1wlUdY28G4YAZezmPUwyyln2WyoBvvNjAGwWqBl6UvDAyGutlVsFeiuC5gQvbOgzrpx4cG9Gi1lLE30QX2LIUZTXStpqg_JEituX8x0h5RtjqLF4X8agVIwyrlODMcSPBtd-8Y4Jt48P7Sm4_7OvMeWSvXeEDrs6JD0ylPrphsgf3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ عمان را تهدید کرد
🔹
ترامپ گفت: «تنگه‌ها به روی همه باز خواهند بود و تحت کنترل هیچ کسی نخواهند بود. ما آنها را تحت نظارت خواهیم گرفت.»
🔹
او در ادامه گفت: «عمان هم مثل همه رفتار خواهد کرد یا اینکه ما منفجرشان خواهیم کرد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/438363" target="_blank">📅 20:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438362">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8583938fe.mp4?token=IAPB9fraLQiQwmd3vwO27LGbChSSchc1s-uG2A9mnh1yZ7HhWe0C1rikLpzDNtIkj1hb-z_uLAYP87ztlHyvAlaVshaRUQY_5MJIJXvf-2TzYNTfirvGg1XJcvvJPZfRrdpg_3JUjvDxrIlD-uPJKaHQ4AQGUpdl1VSHK9rxo9SHOrFB0WDSibph3wxRC-r44_hOu_ObXGhEV5ZonhuqJWIhIAlWdh0DSB31IRfqS8Ws9KT2OL9qvibyjOHQVQ7mXQGSabrpOXYhjh1ddD6_-vGA0OWRsbLDr99ehvOlLNTZCuTULCq-HDyUjXqQK-TmzzNIb0OK4a4rlZriIsKVYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8583938fe.mp4?token=IAPB9fraLQiQwmd3vwO27LGbChSSchc1s-uG2A9mnh1yZ7HhWe0C1rikLpzDNtIkj1hb-z_uLAYP87ztlHyvAlaVshaRUQY_5MJIJXvf-2TzYNTfirvGg1XJcvvJPZfRrdpg_3JUjvDxrIlD-uPJKaHQ4AQGUpdl1VSHK9rxo9SHOrFB0WDSibph3wxRC-r44_hOu_ObXGhEV5ZonhuqJWIhIAlWdh0DSB31IRfqS8Ws9KT2OL9qvibyjOHQVQ7mXQGSabrpOXYhjh1ddD6_-vGA0OWRsbLDr99ehvOlLNTZCuTULCq-HDyUjXqQK-TmzzNIb0OK4a4rlZriIsKVYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده ولی‌فقیه در سپاه: در طول جنگ می‌توانستیم اقدامات سنگین‌تری علیه آمریکا در منطقه انجام دهیم اما چون مردم خاورمیانه آسیب می‌دیدند رهبری موافقت نکردند. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438362" target="_blank">📅 20:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438361">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3117b79c.mp4?token=NIUbz8868eflD071tWkcsFbE_8VFKrjIJrz3qKEFlvj4w5Jwv41-bQ55t5MNLFK5YKdh-qeO0qylbD4nNEzcepFI6AjguxK6W0j3NuZf7yD2rhCYJ1sqEhhN-ob8KbUtasraGOUU979MYQEU0RkeZ9BB9goMH_enHUYFWacWx_-zG4nlPh5t_NbmvapHdSxxL5-esc3Bwg4asL793D2H9y_Dtm4S37UWn1iFTEuncA6Ws93-UJRyWtyd98SMWSPrUGrHq8O2tgfeOdHBrrGxzCEhjpzZL7J_A9lM584h5hHuUsWc_34gIy3Et2CZWwk-Z1Lyoo67gqx7HPJi_IRVJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3117b79c.mp4?token=NIUbz8868eflD071tWkcsFbE_8VFKrjIJrz3qKEFlvj4w5Jwv41-bQ55t5MNLFK5YKdh-qeO0qylbD4nNEzcepFI6AjguxK6W0j3NuZf7yD2rhCYJ1sqEhhN-ob8KbUtasraGOUU979MYQEU0RkeZ9BB9goMH_enHUYFWacWx_-zG4nlPh5t_NbmvapHdSxxL5-esc3Bwg4asL793D2H9y_Dtm4S37UWn1iFTEuncA6Ws93-UJRyWtyd98SMWSPrUGrHq8O2tgfeOdHBrrGxzCEhjpzZL7J_A9lM584h5hHuUsWc_34gIy3Et2CZWwk-Z1Lyoo67gqx7HPJi_IRVJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده ولی‌فقیه در سپاه: نقشه دشمن این است که ما را مقابل هم بگذارد
🔹
هم کسانی که مذاکره نمی‌پسندند و هم کسانی که مذاکره را یک مبارزه می‌دانند بدانند که دشمن می‌خواهد ما را درگیر مسائل داخلی کند.
🔹
اختلاف‌نظر همیشه وجود دارد اما وقتی فرمانده بالادستی یک فرمانده…</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/438361" target="_blank">📅 20:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438360">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0848db393.mp4?token=nSvPbmOmrEHqRUHmMebRL3rIhAWkkuGmcBrWKZuk1xTyvxS8l-uDbfOI6YsyCi0bomDGie5WPHTB6iqvghAG6sj0t_ehhYPyvk1wl5bn4BgIXK0WFKIuKWMYYQQ0gbbFrS5Xp8cA9gSKtvnMuKc4cpdZJO8mEnzyr9r0KpIFGovtr8or66qw-b_98JFV7YoGnCFgNlP7VYdemvgFBzPFZCEDyq2qvRX8mDJMR25VSxgr0X8Yh0LP6A77dVlBg-S6TTeGTh5e-mRiaCFmly8DggZSjPOhF9QPoSuQBuXIydhWlNgNw_44bPyVGmM16nyvAa_yTo1iRN8jUdKeu-FPcyr3pH0ybXAd-fZYgc3BX2Fo5NnA6iuEQFAy1xq70cTykUJ85l4uSfTBUViEyA2DoU6EdGnaAEudz6p83_m5Wzr0Ximb-gp61ZIf6J-pDur6uIbdN_SSnV0LhCUvU-Z4fllZOQuQjDDF63Lhj-zuTeV1dv8nDNU94iR3u_LM_IrCxL9XCr-Psmix_omT_YwSDQDrje3hXozaBCheucQ8GI1QuSBPWilvsem1hEkhvYtB0pXD-LpzcTze8eyw2bN1WiA665l_loxp58dX7mO7nzOvZdMZ9nf3vgwD5v-lhjBc3_oosLlhbybR43P-6kVMzf_GM3rshAt66cGbe6mFPmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0848db393.mp4?token=nSvPbmOmrEHqRUHmMebRL3rIhAWkkuGmcBrWKZuk1xTyvxS8l-uDbfOI6YsyCi0bomDGie5WPHTB6iqvghAG6sj0t_ehhYPyvk1wl5bn4BgIXK0WFKIuKWMYYQQ0gbbFrS5Xp8cA9gSKtvnMuKc4cpdZJO8mEnzyr9r0KpIFGovtr8or66qw-b_98JFV7YoGnCFgNlP7VYdemvgFBzPFZCEDyq2qvRX8mDJMR25VSxgr0X8Yh0LP6A77dVlBg-S6TTeGTh5e-mRiaCFmly8DggZSjPOhF9QPoSuQBuXIydhWlNgNw_44bPyVGmM16nyvAa_yTo1iRN8jUdKeu-FPcyr3pH0ybXAd-fZYgc3BX2Fo5NnA6iuEQFAy1xq70cTykUJ85l4uSfTBUViEyA2DoU6EdGnaAEudz6p83_m5Wzr0Ximb-gp61ZIf6J-pDur6uIbdN_SSnV0LhCUvU-Z4fllZOQuQjDDF63Lhj-zuTeV1dv8nDNU94iR3u_LM_IrCxL9XCr-Psmix_omT_YwSDQDrje3hXozaBCheucQ8GI1QuSBPWilvsem1hEkhvYtB0pXD-LpzcTze8eyw2bN1WiA665l_loxp58dX7mO7nzOvZdMZ9nf3vgwD5v-lhjBc3_oosLlhbybR43P-6kVMzf_GM3rshAt66cGbe6mFPmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده ولی‌فقیه در سپاه: نقشه دشمن این است که ما را مقابل هم بگذارد
🔹
هم کسانی که مذاکره نمی‌پسندند و هم کسانی که مذاکره را یک مبارزه می‌دانند بدانند که دشمن می‌خواهد ما را درگیر مسائل داخلی کند.
🔹
اختلاف‌نظر همیشه وجود دارد اما وقتی فرمانده بالادستی یک فرمانده واحد است همه از او فرمان می‌برند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438360" target="_blank">📅 20:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438359">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای رویترز: پزشکیان با نخست‌وزیر پاکستان تماس گرفت
🔹
خبرگزاری انگلیسی رویترز به نقل از یک منبع در دفتر شهباز شریف، نخست‌وزیر پاکستان مدعی شده که او امروز تماسی از مسعود پزشکیان، رئیس‌جمهور ایران داشت.
🔹
مطابق این ادعا، شهباز شریف ابراز امیدواری کرد توافق میان واشنگتن و تهران به زودی تکمیل شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438359" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438358">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4501e83e61.mp4?token=pDKsO7f31Y-V4IbVxWOV1XFta-g9zXsklehvv3EPWcW6ZYIEwE8mub-RdelkFwamqBeiM_5CWBhMGP2gNLPzpUKBuSlHu6m4GT6NaNX37NhxE1vzlxfJUUeSafE5wmsbT4HCsQJxyKqtzNR5iFlQrMSFadOEr6HDh-wjUn4YVjvbJrc3WsaYm7uCQx4oJ5WuxpITXoPM9v_fJiFf1mTaDEAn3gDYI9sTsaZApmFS0QTNYDXNBmF5HDLR8-IsDrk9ofVL8sc0hQsgjF4AwS7wvjBBL4e2550hFYEYKueN0DX9WmZaOrCYbZyXD9UMEuxVAr_iXnBrsz0KQuDR2e1cPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4501e83e61.mp4?token=pDKsO7f31Y-V4IbVxWOV1XFta-g9zXsklehvv3EPWcW6ZYIEwE8mub-RdelkFwamqBeiM_5CWBhMGP2gNLPzpUKBuSlHu6m4GT6NaNX37NhxE1vzlxfJUUeSafE5wmsbT4HCsQJxyKqtzNR5iFlQrMSFadOEr6HDh-wjUn4YVjvbJrc3WsaYm7uCQx4oJ5WuxpITXoPM9v_fJiFf1mTaDEAn3gDYI9sTsaZApmFS0QTNYDXNBmF5HDLR8-IsDrk9ofVL8sc0hQsgjF4AwS7wvjBBL4e2550hFYEYKueN0DX9WmZaOrCYbZyXD9UMEuxVAr_iXnBrsz0KQuDR2e1cPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما به نفت نیاز نداریم؛ ما به تنگه‌ها نیاز نداریم؛ ما به هیچ چیز نیاز نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438358" target="_blank">📅 20:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clBIAS8IYlTJGxZzomMoU8cqR1t1R6tWkm0sChcGphq5MRwUSCtIJbYtfKGB3r05raZi-OBs8S5YU1Lej2sqSpkZVR2rAWWiGWiD-4G9NikWFPpjW2zMl2LDEVDmmlI742r3_gjjbYGbbiRu7JUAF8C2SQ8-aUxj1SnSmf22_hy2j5nB5rZ3Brd7EhYiXGBVdzLhcAsJWOnSW210XNKTjQrzFTM6Lf_lfqvLMzWplM5PzHfkIsl4xnikMrBV9_5XfMyrme_qS9fD8UP44_eDhIFeo6YhqaEgFSf4nJHahqBo4WBKh02Jmr3RYx54zhKoz_gPdSHRoi8ZXmD0ckWfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1ZN08h5pGxR8bS_22IzawHu7_kEDR23gpgLudr8PfTypJ1D3h09eFK3zEX8R192dpXT7Iv9I2uk6YH9kbL_4_zy-ez541whE_PS4Lags7W8PEN6OaV1Ce-LtAOrJfzIKU4ZG2OeJe6vXuo2qDaVOpPYHJNw603QRmLXjxaRe9qLcy_d8dp8ZoetA-k2yjcWbWFM1PSKA6lAPw5NTqWvYsiGNmcgGcoXvBqoa_q6qVPMJi5QLyV-UHQzzinWnbczJpySe0N3ie5vr_MMlsXb5Pxk-p2-_Wvyzr_kIXB0TYb11EOCcerAEEYabWq40kZEhOdZ_1tLHnVaw0bNHICi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJMtEwbam7qUrcPxwdufTxGGiFk4UPrwFkFNNVpBN3k5Abo65TwxYwuoCKXb2nv-WHDV21QoGSj1yuDn-OqLWS8IRJjhhYFENhrYYD9KbJdrucpZWjObHFfakS9fJ9HJ4LllhBboIFV8FGdsqVPORAg_O7kWD-WaOazx4rTIll1cEG2Gtu8lSSyCkKprms_mHWpyLshFahOF5nNjfflaIZDuHCkxD9UYkXnLoZNBCmiLDNmBLahCMjbnmJGyUY9Tppt15ad6MmQkoJVHiwiDc7gisAkkEjpzZLikU1Ma8q2peGfyB3Jd-iEbRnr2zZCZDw8KZI_TlTXHVCjffM6yCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwc7Jey_7g3VbubhdfXakw7c2v0LbpXBOkwjzE9tOH0oQwKSDdR3DdULQBA96sMqMdhOXU2tSqSSS7mE-vpsErPn9M7R7z0NpzQC6UMg-3ImxEjUKTKbA19U_2wI-jlEZ9Cl5u6gstMaVMMI5e-S2Tgb7ESYL4smZAmSTQH6pggFh6fJEDn98Wz26JsT-SNbOXhZHs_vyyybh50uc8IUmyqWloVyPMvIQi8dIGyMmg_wuk7F8AxLW3ysGb05saRg4BIpiwxgXMx9PHcAW8iOBNaxrPr7rQqm-1fdiOzqlkCbz7Z_cKiJXw0xmBQguU_ydtm6SUpe0_7PlkIaADZOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anjqkTR6SibJiP_0ejfaxvyJ6luuKssjxJF-YBQ03buqJJ0GwTPH9hTW2ZGKW403ZysIK_qLmaBBPPvWHdO4c_J7n7bQx_ado2ZUId1kfVSGN1DlljhimCmrOP6I_hoHS9ZUeZuR4iMS1-_9tzPGg6HhAO6d7LVBkb0r0bNBLmjur5gODnZ2wQybzRtyx9dYB7qeTKkQrulCMecucNLMxJHmOh5Gn9g1cHvZ16ezlwMJRHwodwRM_YlXJt_lBGjj4VGKH7S5IFNCIAQvouR4wMA2ciy-kOVyJFNNJzo-xJdHFAnbicc7W_YU54IpbxvLbmBUxKPGYCbBXketsadiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWD89FnbdbrOA9VeX880zFKEZHegc5iJzcuQZQAPJrpwd3Le0wtqsYBF7OyGioYn5FB3ynZQrj7rsO4VO0JU-_5QVXaHSMGw_j_JEKnZkT7O35abEpHa_9MFk8USzNBXVZtl4qx5Me_1Duu5s8DfVa_crg0eqRY5kvYogwKV8iIHNb0hAyPyGQ7sLLUyf4GS0v9Y0GxhZUZ1OfyLVpTDLP2xB-Uaaol4fgXM3UpdodG6clxa5D2dSsmLhH770UkcqmQwMEiGdvbPwbfUY8LWMLl4ckx3FXIhRG90oRCKDTrFijpLzbTgSfRvneXszBKNK7Qdy57-0GqWml27BsJC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_68ouEqfu4OuW2zEp0iHSoxV2Oja7tcQM1p8JmNp8xcR3aZvCqdPYxjPYQ7JsE_RvlubRk5FLO8EcQAIFBeoUML9Ov7WDWxCqQHcxB2RpKWxOl2v9LyMA-Ar7OalgTuTGV0mVE6QZ5KyI7mfk07q--EbdQdKfYXYTgtI4w_XXlftyAe7tN2-J68xJ9HdSPW9p4WU4D0brwNQhRHEJFhAAAA93-UHRaL2RXhP33LKYa6jCnzMAx0vflXW8Hj-cBNi2-cOGgEa4GvXyEROZCmd3jBRlHWNMAjLotUXqT9VWxyrDdJQEErrVLFlwth9jDyvbbXt0LpTVFRNBO5jF2TvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز عید قربان در اردبیل
عکاس:
حسین حسین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/438351" target="_blank">📅 20:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHRcPsDyvzMwup4-FKk3KvBAtPs1Mlz57s9gM52c6DsCxWsMZsOQ-bltLZRz1HrHItkJdLlo4z4T2SLmnrP_mLruxI27fQbRwTgzUc7IvAn2DJkXVLKtt4W6h-eYEekTpZZHdF6fdsKx-3WaHdryir1I8b6Q_FGQ8qJe4JD7kl4F8rom9cCosufYsP0ZxPcb3sg2htwjKcwWpE9ZzRQR-uSsfViFw4uxWlkJVsVjX0zRNJV5BKPmXFe6NFBnBOI5gpkjxpgIZf_KFBbw6NuaDI71BiXUiV4M1cnjw9Ud_J_-7954FvKZcFsTV4NVXmERkiPdL1NUTwamnh2VK9e68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تحریم‌ها در ازای واگذاری اورانیوم رفع نخواهد شد
🔹
دونالد ترامپ، رئیس‌جمهور ایالات متحده، در گفتگو با شبکه تلویزیونی پی‌بی‌اس گفته که ایران در قبال تحویل دادن اورانیوم با غنی‌سازی بالای خود، هیچ‌گونه تخفیف یا لغو تحریم‌هایی دریافت نخواهد کرد.
🔹
وی گفت:…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/438350" target="_blank">📅 19:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbxZHNsUOnm-FiJF3zsdlFHFIleMNU1O8TsFhxd4GZa4TWvqvBZfWlgKzQTz4cmi908sKYYnNBzsFM4mkj_Wa_wFDVh87KhQizhza6ZWHKgndsn6TKZmTtvo6EAV5GlJj-h_fu4fghlUrxWXhnIosVzstSxw3Yoo3omUlfmNPS9FM5TYgAo7kMriuzNtjRhvOzoMgjjlSAfRsji7hS7YYIY2hgFs-FhW5NadWOGCVASOwSEpIcYFpwQqN9HiG8v3030Eljo_xFJgBdLD3DkeyB8zmizUG9WVU9y-GX6Bvrg1cD_Lau45AMJDnffiGEddjwGsT2nZGfBBimfaicmTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تحریم‌ها در ازای واگذاری اورانیوم رفع نخواهد شد
🔹
دونالد ترامپ، رئیس‌جمهور ایالات متحده، در گفتگو با شبکه تلویزیونی
پی‌بی‌اس
گفته که ایران در قبال تحویل دادن اورانیوم با غنی‌سازی بالای خود، هیچ‌گونه تخفیف یا لغو تحریم‌هایی دریافت نخواهد کرد.
🔹
وی گفت: «آن‌ها اورانیوم با غنی‌سازی بالای خود را واگذار خواهند کرد، اما نه در ازای لغو تحریم‌ها؛ خیر، به هیچ وجه این‌طور نخواهد بود.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438349" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFSlGkbpiuC7wPyhGM0NqJTskuQ1NKPGrwzSQn_j8_B2gfxMoICjTQSM6DAceDncmRrZU_pn7Qh9XTTZtlie2R6lVuI4Q4B7h07lcZUL3PWzdeYS7Zm9pFwdAGnc_PfahssI-Kg9H0lNqDxm2YqKIWO43znDsQ2VUBtXGCdstavlXHRrDIiWnqRphCEbUxGys7yYyJpMJS7168wsAOXfkkXLpnx6zeS09ogvoK1gR_h84DKQ0HpWAl3MFv1ZzNMN1-3_D9HFa7b_AF2FhovDJMqQexTrXNsA7iCUr8z9BXVQxWyzv03bmPnVMVlbUUJI5APP7QJIjj9KMwW0gLcunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نشریه تلگراف: ایران فقط درصورتی با آمریکا توافق امضا می‌کند که ۲۴ میلیارد دلار اموال بلوکه‌شده‌اش آزاد شود.
🔹
ایران گفته نیمی از این مبلغ، یعنی ۱۲ میلیارد دلار، باید بلافاصله پس از اعلام تفاهم اولیه در اختیار ایران قرار گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/438348" target="_blank">📅 19:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438347">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
احتمال اعلام یک‌طرفهٔ نهایی‌شدن توافق توسط ترامپ برای فشار به ایران
🔹
منابع آگاه می‌گویند دونالد ترامپ، رئیس‌جمهور آمریکا، احتمال دارد در ساعات آینده به‌صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است.
🔹
این اقدام از سوی ترامپ با هدف اعمال فشار و القای توافق به افکار عمومی، پیش از رفع کامل اختلافات، ارزیابی می‌شود.
🔹
بااین حال، یک عضو تیم مذاکره‌کنندهٔ ایرانی در گفت‌وگو با فارس تأکید کرده که هنوز برخی موارد حل‌نشده باقی مانده و تا زمانی که همهٔ موضوعات مدنظر ایران حل نشود، هیچ توافقی در کار نخواهد بود.
🔹
به گفتهٔ این منبع، ایران درصورت رفع کامل این موارد، رسماً نتیجه را اعلام خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/438347" target="_blank">📅 19:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
حزب الله: در ساعات گذشته ۱ تانک مرکاوا، ۱ نفربر نمر و ۴ مرکز تجمع سربازان متجاوز اسرائیلی در جنوب لبنان را هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/438346" target="_blank">📅 18:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438345">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a455f364f7.mp4?token=AERuQO1RtghvyxfSKS-0rS2EOBJzwo93A83b1eqFy5Wl3dRZy_UmuvtZiH4V_3jbqCbhgwIbC8deQ6lWMOWbZGaMTXuofLl7vT1CUvnLfHVJdvi5HyLDtVzgjStngGeISsWvOGPzLKZ-YuNyoPZiJOKerzMP-4zN6ikiatFvaPNgjdMNUDzHFsQgHm_H8KxLZicYXHENbEmBokJ0HzuLzhTPiRHhFbng7oZPS9yZ0MM_VERfx2JGasl6CsYNABilazfBSbnLQZoZnYhZLfQATlX8bGZP88UXJa6oLvtEtof5fnzR_wE2j_qxTRNkFiPbEwYMhtGhSDLExPU8puKjZwQ2XZ1dgfuQGHAZ2k7ajFVzdmJEiFQ_dvyhf_cOKCugMEoMQij_yRgoUq8sAgTtDv7stsW6Wqg_UPHZT8xIUNRBrzhWNozl6UjDA91duX4hkQhxtRZSsMpQc63yDfDZaJU92sTITfnEryzRgUnpbLtpVLCwbMKCY8dZSnuucvmBn-ZDIJHcwEySxDiK9FLk_imcSCpJ4bYhOhcQ97hX0h3e6Rd0svCSPFPT5sfGzxRtzkgafkdv03_d4V7vMmPdXKz4J_8Vh_L_DTPtp3qbcESNFLbhWdP27ntuepqiUn1PYfLsHIsUYyKSSJywBX90BhMDGzbf8QhXEH1upLXNQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a455f364f7.mp4?token=AERuQO1RtghvyxfSKS-0rS2EOBJzwo93A83b1eqFy5Wl3dRZy_UmuvtZiH4V_3jbqCbhgwIbC8deQ6lWMOWbZGaMTXuofLl7vT1CUvnLfHVJdvi5HyLDtVzgjStngGeISsWvOGPzLKZ-YuNyoPZiJOKerzMP-4zN6ikiatFvaPNgjdMNUDzHFsQgHm_H8KxLZicYXHENbEmBokJ0HzuLzhTPiRHhFbng7oZPS9yZ0MM_VERfx2JGasl6CsYNABilazfBSbnLQZoZnYhZLfQATlX8bGZP88UXJa6oLvtEtof5fnzR_wE2j_qxTRNkFiPbEwYMhtGhSDLExPU8puKjZwQ2XZ1dgfuQGHAZ2k7ajFVzdmJEiFQ_dvyhf_cOKCugMEoMQij_yRgoUq8sAgTtDv7stsW6Wqg_UPHZT8xIUNRBrzhWNozl6UjDA91duX4hkQhxtRZSsMpQc63yDfDZaJU92sTITfnEryzRgUnpbLtpVLCwbMKCY8dZSnuucvmBn-ZDIJHcwEySxDiK9FLk_imcSCpJ4bYhOhcQ97hX0h3e6Rd0svCSPFPT5sfGzxRtzkgafkdv03_d4V7vMmPdXKz4J_8Vh_L_DTPtp3qbcESNFLbhWdP27ntuepqiUn1PYfLsHIsUYyKSSJywBX90BhMDGzbf8QhXEH1upLXNQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وعده وزیر نیرو برای پرداخت وام به دارندگان پنل‌های خورشیدی
🔹
وزیر نیرو: تسهیلاتی برای استفاده از برق خورشیدی در بانک ها درنظر گرفته شده که با معرفی وزارت نیرو، بانک‌ها تسهلات را به افراد پرداخت می‌کنند.
🔹
همچنین اگر مردم با نصب پنل خورشیدی تا ۱۰ درصد صرفه‌جویی در مصرف داشته باشند از ۲۰ تا ۳۰ درصد به آن‌ها تخفیف داده می‌شود که خود نوعی تسهیلات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438345" target="_blank">📅 18:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438344">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9O0t_6aNmzlQuqGXCduwYNUzvCZPU0zXBCj7DGDA0IXSu87tAQwLnMdFpmD2NLgk1EpaE18D3XNiLYGtyQsjaaGWU4Yue9I5xkrc49dvMsH5NPkrYgqSIsLX4KSg6kPwuC3rP8dRQCR1wR0pW1eNm7Z1Khr1xHaMrULAZnkZgyfAwRbdVAk7IB8BANlVzhJzMVRiRwnzL2vCPp_5-q3HisjJ-ZanhGjCjl-Gsd7fZmbfIg_obcEfx3nrAUK0LV5npiq5_8AzAtyiwCdFPETU_43a7easMHPtkFpS9DxAQb7ieeSFiiQVHsxK8u4b_SKb3mzpfztcKX48Vdz_e1v1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین نظرسنجی از مردم ایران دربارهٔ مذاکرات
🔹
پژوهشكدهٔ مطالعات و تحقيقات دانشگاه جامع انقلاب اسلامی، در یک نظرسنجی‌ از مردم درمورد مذاکره با آمریکا پرسیده است.
نتایج این نظرسنجی به‌شرح زیر است:‌
🔸
کاملا مخالف: ۲۶/۳ درصد
🔸
مخالف: ۲۲/۱ درصد
🔸
متوسط(نه مخالف و نه موافق): ۱۲/۹ درصد
🔸
موافق: ۲۴/۶ درصد
🔸
کاملا موافق: ۱۱/۷ درصد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/438344" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438343">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مهار آتش‌سوزی در فرودگاه امام خمینی
🔹
مدیرعامل شهر فرودگاهی امام خمینی(ره): ساعتی قبل طبقه سوم ساختمان اداری گمرک فرودگاه دچار حریق شد؛ باحضور نیروهای آتش‌نشانی هم‌اکنون آتش‌سوزی اطفا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438343" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438336">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHaDNqGCd7sjBb-oZEvrmuLR7VAXpaxMZxuaHmzGz0FkdYTQ6BxzZNwwbnwGbAy7B7zZEZQzWqe_-MucGQNMvZDY7kQPKX43xQom5KQiK2eMO1GiNWS-yMiLumGOigV5Dbp07siOfWC0YwFAPBhdHltYGyeZoTUZD-PpR-k6EE3H1d2IErxFclODfWZKMx8rqcXFsvQdfREsm_zKTA7r_Aqk-b9in2EIhDlpsJ3c2ft7x--3-NdceCi-SmZIvNCOidPUy4gF1N013_FRDkw7XSLDKphSpVcywmRW_PAIykVVi_uDTG5PGij33KGON07HttlEtnLNmf5kuJ4qEWG10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqYlM8mASXVOXSlhCd568rM7EuscYJsjmAhVBE_G-Dk0Q80aqlQ2wPSQXH_iiN9VH4xsjQuW0qade8T036PtCCpU0ZuKOcQA88mhkyvSHnpbEPLnu3vYpEEU1WcrzbA_vUA_7CPAXs97MiBuCjF1ewU2Mo_IKXWTFOQoiB7u570sCSq8tWp0OIKXNCPN3fOV5yzPfRqgf5TU1fuhOGlqpN_z1MJyhEM02eSwcSblQtfAtacWewLJVTFZ22ulG-P9zt_so174LTwQB7BU16BtCrnNObQS3npUxu0SZ1yI7HGmN9BgzSkldAZ5lEV_K0HJppIA-XzrwKvUVUmYP3iFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wen8nngyzAhrXSXP7BsAcndg25i7V4PGx7EBfam9orERM462L9V-cxyQOsyD5VNDoci73ZE3gpT2tbZ3kaJPJDXeYpUo3kLGK6H25AjHeSR-gYcBT83UNEZVQU_3gHTVQyNMZBJwDPIirSinsus7RE1ZdUoRrNcQaeblzabxCbzZUiOFX-CmC0AUDXNRNubu-m7mJjKMafOCbVTMGzBcorYxsOKlCbXh1yNvVNFp3jqkwb25_g3tS_U_x-hUh5iChOx4LSkH0XZ_Gf1S2SK5HiOmLQ2h_50VYWSJAdtegFdncsiVV9MwoJjDZrKjM9yatNTAYNhQ4YtXYQZU-v_nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JH2tD6_ks_GSH-yfSf8p1rQMslqOlO1x9hBguSkPyhEL-CIYq3GFhtGh_ZpBqkfq8TX0xmTswVD4ak9f0-IDW6ybdK3cae0yzdp77qDDzJu1ybn5gNYlpMmqgzEyeM9VTBQhr54nXWgj2ug_3Kff03TA1x67_VGNtVr25duPHvlCE7RMtHn8v1juJobouUc5FqQX0dLCu3sNaCgtUU2vZvYPKpsos9r75gPl7feDFA7oseehDVkufF8fzAMPCmQAxVXbSQW83wLSfBMz8keV-UMojlY_-pZjkEOG8h4ViLsK2RqTGPcFp8Ym8C1NYH3xq3GMgSPTd1nkOF1Y-vSSRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTATaPerdj6hz6_eG642OGr2AaYN17B1dXraZyH9qn9IZy9Hv9k_KjDQAXrd7i8kWMMvs19xKu-xJG4Tnj8Ycl5rsT5dUngNN8cono8_6RCpyjjt7SgkFZpJeO-RjbQg-fT8MMq3N81pciPgz8cRpxjabekNTQU-y4asjFJ9kZDBrHboS9ZjXdx3eG6Wh0RbZ8XCKZ3XNAi339KUfRkw0Ab8MVMllq8UsUIW8HROX2eWcK1fkC-F_Rgv1-dmyQvrajgSEcll5kLoKZ0FhnPnG8eW4hWDn3Nk0WfgUE2O0gGHal14L1j30jC96yOtgmyErQLFiRk6yx3h0GSlSis_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldvguRAhlhudX8kdZO2FODO_bDMytTGfh2OLSbBv306IHk01Fm2O_xnL7e_lKwt5ENv5_dnEQA5A2Mnn49MZAYeYodXt7hJT_trTuUsGhDDaycLwkkIzzxUBS7RtRfLSKxkwwU7pNiItft7Q1zv5SOH4aARgV4r8sCI-7e3CVjZK0P9zFPPjsfEBRiE-cU8Z2zrtnhovkx4mJeJIfJA64cvfWuCSylc3jOj6BVF3ODp10mn0-LCa6Tdo4e_B7oLFIYJtBD4bARLugqCwRsJAf0sLzw-5E23GfAOvhiohqPRLImbiAEROy8PSBok7O1eoSBHY20Eef-s02INQf3njuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-X0TT1pHLbawOtzddaOVSvW6SVvwdF-vbbUOj_M5EmAWRXVsZXch7ndigCMxJ1EqU1J2t_EEAEZO3tRYpeEG3hehUNfeGPsRMWkpZEi8gCCJElMw7fbnBO7025miaB84702UteeF9ELHS_EIK_6lbIiC1OaerEdIRTPctLosQmE9lWFQMcmukUKWrR8gZ0o33kQMESd-AdtgA4WDsGMiKgSeQL6u-daEJbwILy02QOScJOhEqq9QieQ_rRb7WcR71noLiH_vGJ0h1sshOtUt940PEtY8QIsbNy65fwkIFnA6t7S0HUKsVd6VGiAo7i4h1gyLIAPivOtLyrAeP4x8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز عید قربان در حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438336" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438335">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4db406e91.mp4?token=aCrFWSJzMMkg3_QrqbON_WP4kMWID3IJdlTbtlR5KOhA6WwNQrZcEeyTGAH6ODwyqAa1jwiDUsCrJ3psou6adKGaPV3jCijrrH93y6y4QCz4yFO1ebMGjCbko2-5zv5nv0JQPmaEJsBmApUThh-I2CtrTE0aDcnTNrtQtmzwbm7LS-jplfAIOP5yvW6NN4HxaExh7vKy7iGV3-N4jtyGvF4VwIkcncWNIDPccUT-JpytkVDelC5XKzsuzY923xmK225HQyLTOWmseRKXPQp7Ttoo1f1joIOt5uebnyRiu7qjdQgoxdSX5Z9lcuO5e0gqFy2F43rYivfnXX5hWm02ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4db406e91.mp4?token=aCrFWSJzMMkg3_QrqbON_WP4kMWID3IJdlTbtlR5KOhA6WwNQrZcEeyTGAH6ODwyqAa1jwiDUsCrJ3psou6adKGaPV3jCijrrH93y6y4QCz4yFO1ebMGjCbko2-5zv5nv0JQPmaEJsBmApUThh-I2CtrTE0aDcnTNrtQtmzwbm7LS-jplfAIOP5yvW6NN4HxaExh7vKy7iGV3-N4jtyGvF4VwIkcncWNIDPccUT-JpytkVDelC5XKzsuzY923xmK225HQyLTOWmseRKXPQp7Ttoo1f1joIOt5uebnyRiu7qjdQgoxdSX5Z9lcuO5e0gqFy2F43rYivfnXX5hWm02ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز تخلیه شهر بزرگ صور در پی هشدار ارتش صهیونیستی
🔹
پس از هشدار تخلیه از سوی ارتش رژیم صهیونیستی برای ساکنان شهر بندری صور، ده‌ها هزار نفر شروع به حرکت به سمت مناطق شمالی کرده‌اند.
🔸
شهر صور طبق سرشماری سال ۲۰۱۸ بیش از ۱۶۰ هزار نفر جمعیت دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438335" target="_blank">📅 17:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438334">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بازگشت خطوط لولۀ پتروشیمی‌ها به ظرفیت تولید قبل از جنگ
🔹
آواربرداری، تعمیر و ساخت بخش‌های آسیب‌دیده واحدهای پتروشیمی به پایان رسیده و اکنون تمامی پتروشیمی‌ها می‌توانند با ظرفیت قبل از جنگ تولید داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438334" target="_blank">📅 17:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438333">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8HAqinqwt6_cQzXbHlsO1fC0oYNKKBOSiUiV_X_PnpIG8CFztnYtJ-UD5RaO7uLgJ7Dx10cd9h8Sy5C3IT3ryW3ju6-iXtAqAdC_BQhKTn3bFzmM3nWisJB0pPhdyE1ccgoiN2OWd_kM-sx5bTNTX7WwlAq_xuRZ7jdHQt3QvmWa5J3LP9StMB21wCEEBg0mynHtpAOsG_iTqLdyImb3L-67zZ5CxWBc-ZgclumT4EA-CQMPvnZW_4ahknUvwwclbLfj0o7PkPp7-51vrgiF84dko7QWw_MmnqxSKJKeuqvVg3ipAfJTIp1JFnrxS6hm45Q-LuJLEJ4lZ_YGrBETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط ۱.۴۴ تریلیون یوآنی بازار سهام چین
🔹
کمیسیون نظارت بر اوراق بهادار چین امروز اقدامات تنبیهی علیه کارگزاری‌هایی که یک تریلیون دلار پول غیرمجاز از این کشور خارج کرده بودند، اجرایی کرد.
🔹
با این اقدام بازار سهام این کشور ۱.۴۴ تریلیون یوآن از ارزش خود را از دست داد.
🔹
۸ ادارهٔ دولتی جداگانه به‌طور همزمان بیانیهٔ مشترکی در حمایت از این اقدام تنبیهی صادر کردند.
🔹
این یک تصمیم هماهنگ در سطح دولت چین بوده که در بالاترین سطوح این دولت تصویب شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438333" target="_blank">📅 17:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438332">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کشته و زخمی‌شدن ۸ نظامی اسرائیلی در جنوب لبنان
🔹
رسانه‌های عبری از کشته‌شدن یک نظامی اسرائیلی و زخمی‌شدن ۷ تن دیگر در جریان عملیات پهپادی امروز حزب‌الله در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438332" target="_blank">📅 16:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438331">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833385620.mp4?token=n8D47rm_O1udGeqRQoLBhrirSLRMGx25eVi9TMd4dKA7CEdPyKPrMNoKEAK8-Xqb1_vW1rJ7NrurYWqaJDLm2k3xlygz7pYCZlVWsD3pw5qhfnnX2cIfnXw27uQbez3rMXUdGePhw4ZkTWPFIG_JcRqG5oHNDhX6hODgYWGYeSN1BO9_B73um8ZzDEtFd_CYE3Ydkf40K1c9DlBOsQARBCv3Os-PJZSVGt1UtrxlZ7xptHK3-RsvudqXbusrgQEnK7O28BmNQ_aXVmFpnqPN24wKQbHHYzfALmTgCAT3VmVslDISwqrqaIV4a_E7Z-K3MojKuDj6Tqxbcqm49z6h3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833385620.mp4?token=n8D47rm_O1udGeqRQoLBhrirSLRMGx25eVi9TMd4dKA7CEdPyKPrMNoKEAK8-Xqb1_vW1rJ7NrurYWqaJDLm2k3xlygz7pYCZlVWsD3pw5qhfnnX2cIfnXw27uQbez3rMXUdGePhw4ZkTWPFIG_JcRqG5oHNDhX6hODgYWGYeSN1BO9_B73um8ZzDEtFd_CYE3Ydkf40K1c9DlBOsQARBCv3Os-PJZSVGt1UtrxlZ7xptHK3-RsvudqXbusrgQEnK7O28BmNQ_aXVmFpnqPN24wKQbHHYzfALmTgCAT3VmVslDISwqrqaIV4a_E7Z-K3MojKuDj6Tqxbcqm49z6h3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مذاکره‌کنندهٔ ارشد پیشین آمریکا در برجام: ترامپ با یک جنگ اشتباه تنگهٔ هرمز را به‌روی خود بست
🔹
شرمن: این جنگ نه‌تنها هیچ مشکل هسته‌ای را حل نکرده، بلکه تنگهٔ هرمز را که پیش از این باز بود، به یک بحران تازه برای آمریکا تبدیل کرده است.
🔹
قبل از اینکه رئیس‌جمهور این جنگ انتخابی و نادرست را پیش ببرد، تنگهٔ هرمز باز بود؛ آزادی کشتیرانی برقرار بود.
🔹
اما حالا خود او مجبور است تمام وقتش را صرف این کند که بفهمد چطور همین تنگه را باز کند و محاصره‌ای را که خودش ایجاد کرده، بشکند.
🔹
حتی وقتی این مأموریت انجام شود، حداقل ۲ تا ۳ ماه طول می‌کشد تا قیمت بنزین پایین بیاید؛ آن هم در شرایطی که هنوز مذاکرات هسته‌ای واقعاً شروع نشده و هیچ سازوکاری برای راستی‌آزمایی یا پایش توافق، از جمله پایان محاصرهٔ تنگهٔ هرمز وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438331" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dArlIblQ71qZe9_0EuIvTTXIxY-GRqVInqMu7RDKoqSdVFkjvP0ffAGGHDT96hc1zvzTBzZtqICRodcUn75nZwRjcf71maBFhLix9xnCdTtjkp6E9WPnzmmH31Bv1SUqRLHm0uBqN3OEDoOyymrXL0OSJ5c5mTwQgxTQX9ZdZ4mon20VRxY-Bc9fsMguMxH_2_XP5djRZRTVGPCTWf-2TcVpWqcZdWPUAGkqDyjJAAfBODZ3lFtw9hi_eQR5PjfEmc22D0Ug_eXKQoXaAH1yT-Tkl-XTQUtDDL5vA6kOgWkjnLs0__D6wRPELs4MLAQuew8SBDvc0xlJfUkLLg47dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی الصدر دستور انحلال سرایا السلام را صادر کرد
🔹
رهبر جریان صدر عراق، امروز دستور انحلال کامل «سرایا السلام» و «پیوستن آن به دولت و مسئول کل تشکیلات نظامی» خبر داد.
🔹
سيد مقتدی الصدر با انتشار بیانیه‌ای خطاب به نیروهای خود اعلام کرد: «به دلیل مصلحت عمومی کشور و برای جلوگیری از خطراتی که کشور را تهدید می‌کند، بر خود لازم دانستیم که اعلام کنیم: سرایا السلام به طور کامل از جریان شیعه ملی جدا شده و به طور کامل به دولت و مسئول کل تشکیلات نظامی می‌پیوندد».
🔹
وی در ادامه تأکید کرد که بخش‌های غیرنظامی وابسته به سرایا السلام باید به «البنیان المرصوص» بپیوندند، بدون اینکه هیچ مقر، اسلحه، لباس، نشانی یا هر چیز دیگری داشته باشند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438330" target="_blank">📅 16:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438329">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE1DY36yyYMQMzCZamy09XBAQzlo0ZqlBQplEufkafsUcVNUCi_om7njgAJSm3MrH8W4PBRYzSJtJvtwl1pBPQzR6lG5Nk3n9TfNeiMKj9bDEUupj8tq0YG_5ZTIHR3KUSHTbfImJ9wfCdmsdKF63P8EN92uznWDog1Pk2YL4IZtla4Rcy54l7Qcw7OIQKLJkOjn0IIRmMJorjH8nVWjxlx82Wj4JPudebEbJmNwclbzkg_Rhu4KjnJndLGqojHL9FL57UTkcMtV68fxHfkk5F-lCEUh590umotKpo1DCFj9zdCquPf93zHYov5GmddENL-55NUnZnFWofzIkda5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز هم در خالی‌کردن ذخایر راهبردی آمریکا رکورد زد
🔹
جدیدترین آمار نشان می‌دهد که دومین رکورد بی‌سابقهٔ آزادسازی ذخایر نفت راهبردی نفت آمریکا (SPR) در تاریخ اتفاق افتاده است.
🔹
هفتهٔ گذشته هم آمارها فاش کرده بودند که بزرگ‌ترین آزادسازی ذخایر راهبردی در تاریخ این کشور انجام شده است؛ در آن زمان هم ۹.۹ میلیون بشکه از این ذخایر کم شده بود.
🔹
حالا آمارها نشان می‌دهد که ۹.۱ میلیون بشکهٔ دیگر از این ذخایر کم شده و سطح آنها به کمترین میزان در ۴۳ سال گذشته رسیده است.
🔹
ذخایر راهبردی آمریکا با هدف کنترل بحران‌های نفتی ایجاد شده و از زمانی ‌که جو بایدن برای کنترل بازار در زمان جنگ اوکراین از آن برداشت کرد، واشنگتن هنوز نتوانسته این ذخایر را به سطح قابل اطمینان برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/438329" target="_blank">📅 16:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV2pgoa8L8iB4amJuO2QMeqOijeOALWFHtA-9gi9RAR3Y0LbyRqzKXAIJFNgJ-hiNW_ccYqavk-uLk0HppcGwj74e_2DEpchopCgD8-KvKePNOqz8WzcxxmS52yVAzKrwoZbWrzVy83OJsDl80MLSR8u7HJx_QteqIYusrfdCQAs072845Teg2PvZ3Ai9FpreMSQnA9zomYrC8BGS0hJVSHX7Sdc7EU_xubzIznVCXNO14oo-H9uN-Ux3q1E0QohPNFDcyZI-G-e1GSQP6ZeHbK_CUNnoQIhbS6qCgyMzA1l17oclKCKJ-orHlOwSaJmqrjxfO9DbYWQ_uOpRcDFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزام صنایع به تامین حداقل ۴ درصد برق خود از انرژی‌های تجدیدپذیر
🔹
معاون برق و انرژی وزیر نیرو: مشترکان خانگی برق که نسبت به دورهٔ مشابه قبل ۱۰ درصد زیر الگوی تعریف‌شدهٔ وزارت نیرو برق مصرف کنند، تا ۳۰ درصد قبض آنها کاهش پیدا می‌کند.
🔹
همچنین مشترکان برق اگر نیروگاه ۵ کیلوواتی خورشیدی نصب کنند ۲۰ درصد از قبض آنها کاهش پیدا می‌کند و اگر تجهیزات ذخیره‌سازی هم نصب کنند تا ۳۰ درصد از پول پرداختی قبض آنها کم می‌شود.
🔹
در سال جاری بر اساس قانون بهره‌وری تولید، صنایع مکلف شدند حداقل ۴ درصد از برق مورد نیاز خود را از طریق انرژی خورشیدی تامین کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/438328" target="_blank">📅 16:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzmcCqWGA9dOblFQcG232lVSHcMLVzv46_E_4pSTLnd7qTIY3Qaxzog_tkb1bWtI5ZBk7vn3xEjipuQj5FWEbRU_MyQix4jDo7xu-2ZbIE5Kc78yYhPL8dIdU6TB_RxzX_oyDyTV33E2fj7dqpll3tWDQruMNN1ETMHV_UwxZsPgrZr9EKqgBTGnsxiBZGcbHc3AXie7KRKQAopzveQH6sOXdwj6mDD0F_W-jDx97kTdvUZPRFBuvIu4A7dQdj_8cdx0HyyR_2nCL39lbcJOLGdhbuEtetOIkyJ5kcTpe3osdTX88HofqSGvreClOTfp-mZaxpbFL3HcmWj3zohxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی وزش ‌باد و گردوخاک در تهران
🔹
هواشناسی تهران: امروز در برخی ساعات، وزش ‌باد شدید و گردوخاک به‌ویژه در نیمۀ جنوبی و غربی استان پیش‌بینی می‌شود.
🔹
این شرایط تا جمعه شب نیز در برخی مناطق ادامه دارد و در ارتفاعات استان احتمال رگبار و رعدوبرق پراکنده وجود خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/438327" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438326">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18422de433.mp4?token=YgtuGwekCVZmNlLa_uj3myRI-o55ryP9UOTnIFePmmS4vk9OjV7iFSRIsFNQBZCuj7b-Izt8pZmMCh1Z-YdwrYxDeABm7V00j6ERsFRE5UCdkBSWxHhrLQb0b8jrgjtTEI96AO0rrDeZeP8JyXN2Uah96UnhisLy-BjyaGZ33kUmE0Rrp0urKHeSca5j6SShrPPtwUFXlR-LuA6YySTs6uo_arvF5EIH0CfGWhXDxipG0DgZawy1YDQ8O6JXzS1ZKH-MNpQg8dikE_aMsLnz4UNIKUGVUxefW2CmazO_ifUn515ZFRNLbrzzJXh7SqxnFJNKIUhJrF4Dp4Z0s2nCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18422de433.mp4?token=YgtuGwekCVZmNlLa_uj3myRI-o55ryP9UOTnIFePmmS4vk9OjV7iFSRIsFNQBZCuj7b-Izt8pZmMCh1Z-YdwrYxDeABm7V00j6ERsFRE5UCdkBSWxHhrLQb0b8jrgjtTEI96AO0rrDeZeP8JyXN2Uah96UnhisLy-BjyaGZ33kUmE0Rrp0urKHeSca5j6SShrPPtwUFXlR-LuA6YySTs6uo_arvF5EIH0CfGWhXDxipG0DgZawy1YDQ8O6JXzS1ZKH-MNpQg8dikE_aMsLnz4UNIKUGVUxefW2CmazO_ifUn515ZFRNLbrzzJXh7SqxnFJNKIUhJrF4Dp4Z0s2nCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک گنبد آهنین رژیم صهیونی را صید کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/438326" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438325">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBvRa9T-aBHto9i78p8gl9FbC-wrjsLECERlqvvB0P2kpefFoItGTLGS_JM_eBgDBn7J-3VcxDTeK5F6xeNwuXDkyr0k2P6O0HBHE-OKZPxkkjfmIQ6KjMJFoeXBOpjC8VvqaYLcLzGeBUkhEApq8UbhnUg07cbFwIw6xrzS6x07a0bTXvPsDRnVFyCaaheLfTTIk7lfbP37ecP9DoqdV-EKtEkxYKOb_tR_t8Hguw7wGH9gJX1gcsIM_HMC5QZB3y8eNg1dFwSTVIbqwb5REy-D-3OvjUW5zZJHsvTR76rew4-mJ6AE2danwPt76kLuCJu3FYyqd0UHyQg_4vgxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ جدید وزیر جهاد برای تسویهٔ مطالبات گندم‌کاران
🔹
وزیر جهاد کشاورزی با اشاره به تحویل حدود ۲ میلیون تن گندم به سیلوهای دولتی از ابتدای فصل برداشت، ابراز امیدواری کرد که سازمان هدفمندی یارانه‌ها در روزهای آینده روند تسویهٔ حساب‌ها را آغاز کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/438325" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ae0b9d8f.mp4?token=ofxOtEln4bSFxBAMyyUQx6R8ijSRGjssPDTCksZLPCfeFNtILvIh6rn8s7C0hku-eCoZx0OaEmpe_Wq2V_YOe8zAAZ6JG-okGsSyjMAdmQFuv-inqskRi2vLctZcFTlTLLKZ-bAUtamGkt-WKEo4abcY_BJQT5p8mX4vdGfWTLq-yVCJWXqPJJrXyw20MW9te7s7ul_1LL6lW7RWuOeGog1nrr6AvvXv7TdhAfSq2HkIlymI0D_Z2FEV7zSTt4XTkOCjRHhBfaI4rUr6qdaBJbOiD7ZFGb9PXkBHRUY4N5KD3qSLMqUhqCmU3u7F4sH45Rf6eNj-abeGv0eyFjdBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ae0b9d8f.mp4?token=ofxOtEln4bSFxBAMyyUQx6R8ijSRGjssPDTCksZLPCfeFNtILvIh6rn8s7C0hku-eCoZx0OaEmpe_Wq2V_YOe8zAAZ6JG-okGsSyjMAdmQFuv-inqskRi2vLctZcFTlTLLKZ-bAUtamGkt-WKEo4abcY_BJQT5p8mX4vdGfWTLq-yVCJWXqPJJrXyw20MW9te7s7ul_1LL6lW7RWuOeGog1nrr6AvvXv7TdhAfSq2HkIlymI0D_Z2FEV7zSTt4XTkOCjRHhBfaI4rUr6qdaBJbOiD7ZFGb9PXkBHRUY4N5KD3qSLMqUhqCmU3u7F4sH45Rf6eNj-abeGv0eyFjdBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامه‌نگار فرانسوی: موقعیت ایالات متحده در برابر تمام متحدان اروپایی و آسیایی‌اش متزلزل شده است
🔹
پس از جنگ اخیر یک حس آسیب‌پذیری نسبت به ایالات متحده ایجاد شده که وضعیتی نوظهور و بی‌سابقه است؛ جهان تازه پی برد که قدرت بازدارندگی ایران تا چه حد واقعی است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/438324" target="_blank">📅 15:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438323">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9d2be9fc.mp4?token=l96YsUjJ_ZlTl5F-UaLYiMMK-t2KZdywVMc2L7JPkjAIrYm1Z5SN_vBEZpCYZYnluOVxuDsF1_QTGncb0kU3smQp0sg8UoiYtlOjKMAvWJ-Q4LRhlFnDCLIGoSeGIrJjPdj_BYPZa2ImQjiWbm0kle2cwUBiO-wO1NtB_MuoXajX2KNrmYplecNfwXQWVCsQLc3thGBgRCHmMIBSODYwSUmNIluzjlMGqEsLpbgN4nOkLUmvaduHjC09ph2MAhoVBdUEn_O5dLokDw1e_DbayZUUG-6_sLN3oIGjDqAEss_kELf6FIHo0OgOdOdOxen4D190Hcx5NV7wNtPUurE0wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9d2be9fc.mp4?token=l96YsUjJ_ZlTl5F-UaLYiMMK-t2KZdywVMc2L7JPkjAIrYm1Z5SN_vBEZpCYZYnluOVxuDsF1_QTGncb0kU3smQp0sg8UoiYtlOjKMAvWJ-Q4LRhlFnDCLIGoSeGIrJjPdj_BYPZa2ImQjiWbm0kle2cwUBiO-wO1NtB_MuoXajX2KNrmYplecNfwXQWVCsQLc3thGBgRCHmMIBSODYwSUmNIluzjlMGqEsLpbgN4nOkLUmvaduHjC09ph2MAhoVBdUEn_O5dLokDw1e_DbayZUUG-6_sLN3oIGjDqAEss_kELf6FIHo0OgOdOdOxen4D190Hcx5NV7wNtPUurE0wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
نیروی دریایی سپاه: کنترل هوشمند تنگهٔ هرمز با اقتدار درحال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438323" target="_blank">📅 14:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438322">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e3296af9.mp4?token=tJuPAoyvc5LvhLEkpXV_35nLiihxcop4B9M3MQnR2CaQWXVazujh86XbV85UFXGaFXHVUqlTucZNrpl7H77WcUyW2vskiUYVTJ4wQ6od4w-YH32jx-BE_tYSJ-mxX-GeuIfIXnCEVVeJmlz-IaEacKrqJeXAoX8Dx6sg4KiLyKgX2T6TalGRUXiY9YLNye8jiK3sCbs4axMre753V3EXqKemmaLzMwWDz_kdTFoV5fYRwdGJhb5-_Dbk9g5V3xTiubTcfb-dovstM9zCeOUOmc_0Jy9dpZRZWyjva4_d4GVxI5ekv6hHuj6ZKPrzjcAGX-M1UKBGABGwyGPpf41HVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e3296af9.mp4?token=tJuPAoyvc5LvhLEkpXV_35nLiihxcop4B9M3MQnR2CaQWXVazujh86XbV85UFXGaFXHVUqlTucZNrpl7H77WcUyW2vskiUYVTJ4wQ6od4w-YH32jx-BE_tYSJ-mxX-GeuIfIXnCEVVeJmlz-IaEacKrqJeXAoX8Dx6sg4KiLyKgX2T6TalGRUXiY9YLNye8jiK3sCbs4axMre753V3EXqKemmaLzMwWDz_kdTFoV5fYRwdGJhb5-_Dbk9g5V3xTiubTcfb-dovstM9zCeOUOmc_0Jy9dpZRZWyjva4_d4GVxI5ekv6hHuj6ZKPrzjcAGX-M1UKBGABGwyGPpf41HVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: جنگ اصلی در میدان اقتصاد است
🔹
رئیس‌جمهور در نشست با اعضای اتاق بازرگانی تهران: هرکاری از دست ما بر بیاید انجام می‌دهیم و آماده‌ایم تا تسهیلات را اصلاح کنیم و کمک کنیم شما مبارزه کنید؛ چون اگر شما شکست بخورید مملکت شکست می‌خورد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438322" target="_blank">📅 14:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438321">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdec731a71.mp4?token=qLvXYB23oO8CNmh7OYZZ1YmAY4fl00S_GoBXizaGUZcY3RbW_Uz9swlDBM6LiOGzn70OzHspUBsuVEvb6GBMUCcz_4PqUhJqbX5T_JicOjOMvFZUNI3n3twXKrAuecVf1LVxx9zbvlx5YOlxFCRG3EfMq-iu1i8jls5ks5VMGW0_uRFlfZIA_STAXkW6CSNnDnQYltZphbs37KTae3RfChSfeCvPKl8bmX8fjyzOpz3EfEiOzeoWhweGtUhvtB7SsWBk_Ff4AWod_1Y097iUYxom1GIfboPptV9f_Bhb0eNV9glFgPVcI4wQ-8qQ5I0L7xZerfZ_aZDBDVlFvtNw54DQCE8COyrcRxHukobg12iIh9_d2J3ohzWpDmqPMDDXtbt6x1rvcEhi5C2lV5qOS4CQ5Y3ZL8T-7apsfDEPvvyv2hXi3MEu0YJKDiaGBejJTu13N6MBYaLlmQg3pWuuFj6uu4JaXSt83ikU5-uzvXeBbJ9mXMwJqUAs--c5l15bf8PuyGVqjs_qoQr64mmYh-hesvq4Gpp0qy4Ho0vZzXe0Kqgdi1dgEx9Uee8yC1oN5IHFyoGJ2Y7HxRY4nQW9b4jLVEm07fB9LkYI2hfvfGltABECSIkRCxHqu8S_MR2vZZpJHu83qsAZS05CeItFgK8r-bJln1eVjbdrZGwioIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdec731a71.mp4?token=qLvXYB23oO8CNmh7OYZZ1YmAY4fl00S_GoBXizaGUZcY3RbW_Uz9swlDBM6LiOGzn70OzHspUBsuVEvb6GBMUCcz_4PqUhJqbX5T_JicOjOMvFZUNI3n3twXKrAuecVf1LVxx9zbvlx5YOlxFCRG3EfMq-iu1i8jls5ks5VMGW0_uRFlfZIA_STAXkW6CSNnDnQYltZphbs37KTae3RfChSfeCvPKl8bmX8fjyzOpz3EfEiOzeoWhweGtUhvtB7SsWBk_Ff4AWod_1Y097iUYxom1GIfboPptV9f_Bhb0eNV9glFgPVcI4wQ-8qQ5I0L7xZerfZ_aZDBDVlFvtNw54DQCE8COyrcRxHukobg12iIh9_d2J3ohzWpDmqPMDDXtbt6x1rvcEhi5C2lV5qOS4CQ5Y3ZL8T-7apsfDEPvvyv2hXi3MEu0YJKDiaGBejJTu13N6MBYaLlmQg3pWuuFj6uu4JaXSt83ikU5-uzvXeBbJ9mXMwJqUAs--c5l15bf8PuyGVqjs_qoQr64mmYh-hesvq4Gpp0qy4Ho0vZzXe0Kqgdi1dgEx9Uee8yC1oN5IHFyoGJ2Y7HxRY4nQW9b4jLVEm07fB9LkYI2hfvfGltABECSIkRCxHqu8S_MR2vZZpJHu83qsAZS05CeItFgK8r-bJln1eVjbdrZGwioIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تردد بیش از ۲۲ هزار زائر کربلا از مرز مهران
🔹
مدیرکل حمل‌ونقل جاده‌ای ایلام: در ۲۴ ساعت گذشته، ۲۲ هزار و ۷۱۲ مسافر و زائر از پایانۀ مرزی مهران تردد کردند؛ تردد زائران بدون مشکل درحال انجام است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438321" target="_blank">📅 14:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438319">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a82e25df.mp4?token=pmIxqYilpdJJ281pJ5UGQSKYIgKQeB8cT4iowp1oEaqIjgjIQueZvizhiiO9RMkwUenTbUDnfzRKHGDvrpWj8neGX3l6CRj7s50IUxOkXO16OswX0l3RcnZeicn74s6E5CPno8MX8V02VlifPSYioiBDj_4SvxjVH2loMnQZGOo3NfpG0pf4HnWHjExYhN_XsY6427evw86UJk__8DB8GksWCIaZ0Fmz8lOJEXm3XQ9JbQubmVkbuB3TCZd-bGFL01CdAIL5G7TK673L0aL3DWwexBE7-bd_7sVJzxZ0_3bW9MiEZS5Z9vncWfCte5DO7w3amAk54G3Ytw9kSAKLgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a82e25df.mp4?token=pmIxqYilpdJJ281pJ5UGQSKYIgKQeB8cT4iowp1oEaqIjgjIQueZvizhiiO9RMkwUenTbUDnfzRKHGDvrpWj8neGX3l6CRj7s50IUxOkXO16OswX0l3RcnZeicn74s6E5CPno8MX8V02VlifPSYioiBDj_4SvxjVH2loMnQZGOo3NfpG0pf4HnWHjExYhN_XsY6427evw86UJk__8DB8GksWCIaZ0Fmz8lOJEXm3XQ9JbQubmVkbuB3TCZd-bGFL01CdAIL5G7TK673L0aL3DWwexBE7-bd_7sVJzxZ0_3bW9MiEZS5Z9vncWfCte5DO7w3amAk54G3Ytw9kSAKLgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس یادبود شهدای خانوادهٔ قائد شهید و رهبر معظم انقلاب
◾️
شهید زهرا حداد عادل
◾️
شهید سیده بشری حسینی خامنه‌ای
◾️
شهید مصباح‌الهدی باقری
◾️
شهید زهرا محمدی گلپایگانی
🔹
پنجشنبه و جمعه ۷ و ۸ خرداد؛ از ساعت ۱۶ تا ۱۸
🔹
مصلای حرم حضرت عبدالعظیم حسنی(ع)  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438319" target="_blank">📅 14:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438318">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEbjxsn4fIZsv0qyCTFAwcphMeuxhb2rFCfy9qdMF0IA4Rlw5XGZHLn3AZ1XIyCktZPO6TDuZQNyvAFt-pmM1_Vng21uEfDJhXTV5YDUSRvGpzLZUb0W-dXb-QYxolzMoxgIRb8VL_n4qOJOSZMOY1NrXkIrWqbyQzpthIT4e2EpI1PRVlb1DYtnlIiC8WY8e_JZCdginstsgk0rBAy2fkb10HS_fdq1fwjXgEaKOHNS-XHO-hFg8LKUkC9TIGAJxeg7vF6VR9o3uPM0aHnQAP28b1aZ0k0nR0IFfwgeKwhlRLm-1WG4Jotirlg--l6vwadF39OoSVS69z_-xqGHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای پزشکیان به سهمیۀ آسیایی باز شد
🔸
سه‌شنبه شب خبری مبنی‌بر ارسال نامه از سوی پرسپولیس به رئیس‌جمهور برای دستور و دخالت در مورد انتخاب سهمیۀ آسیایی منتشر شد.
🔹
امروز سرپرست مدیرعاملی استقلال در شبکۀ ایکس نوشت: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438318" target="_blank">📅 14:15 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
