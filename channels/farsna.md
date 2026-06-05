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
<img src="https://cdn4.telesco.pe/file/agAWrVwb3WwMWFHpC5VYGzGUTzPgMHhLzzM2ZoPWhKvwb6YRes-r_4-KFXKC6XPWVJiFXeg7SL22FJnvw1NLOp9c3ueiZ9sulDMSrJaRSK3vNNKvfejItGg-rq3jH2r4C84wWOjAaK42GY3m0B2jcCD0QnZeMKhysxi1UQTiew2qm9w46lUfrnwdfJfhlGxGyb_l7WdS3IKoq_zeyRcDSo7juhL69SGDxc_tpzJPbNuYLAdBNW-0tV_QXfBOleLjIxfm8V5h1m6WI5_joCXYchrhLa-qk9hrZ4eEJSU4LARxledpuM1jYT15wafmvE5IFgJMQgx0IA8T338E01ioVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 03:29:29</div>
<hr>

<div class="tg-post" id="msg-440004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVUoEteBxwrDFNVCNBdWVY40VuHprAySncEdWlZdaUeRoa_SXU4PJRbiU0c-dYCMvzTE8hxI8nYRnBkMOZ4lwUFEmhd15FOJdtDGmmfYyXdxYGSnAPTkaTSau8eK2NqrxuCld6m7ftHqHp-uy6Ckd64uJ2aM7mm_SJtfIxsxm9hbQixFx8qaiMpeZ1bzfkoRHPt1QHN718JmVX4Pu22yAdvqsvarshyWFL2HnzGH8Dz5Da0Q-nULxNoNl3fKzUUuBdNgstLXMGFmfa4dVPR5xz4AHgua4nVv_fmOc2tMCpCvub88Ifn_TwTcocdsAYseqIkd2xl0bcqxbKrL8OkYCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح ناکام ترامپ برای تسلیح کردها در جریان جنگ رمضان
🔹
در حالی که رئیس‌جمهور آمریکا دونالد ترامپ به تسلیح کُرد‌ها به منظور اقدام علیه ایران اعتراف کرده، رسانه صهیونیستی روز پنجشنبه گزارش داد که موساد نقش عمده‌ای در این طرح بی‌ثمر داشته است.
🔸
جروزالم‌پست به نقل از مقامات اسبق موساد گزارش داد که واشنگتن با توجه به تجربه جنگ عراق در جریان تجاوز نظامی اخیر در ایران به دنبال طرحی بود تا نیازی به اعزام نظامیان آمریکایی به ایران نداشته باشد و از این رو، قصد حمایت نظامی از کُرد‌ها و تشویق آن‌ها برای حمله زمینی به ایران را داشت، طرحی که در نطفه شکست خورد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/440004" target="_blank">📅 02:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c3f17a4b.mp4?token=BmIjwf94gWTVPMktwNVQR2yxzvUBTqrHpH22Bp87n0u-Z-BIVOAdUaIWg7p15t9qjlBrq23vsOm5-JSUS-nrNP7-Z8FaO8wdPJM_Sf7yGpC_eXa8YNANkQOlr1oBOZujpkEwuXOQaE7y9w3SYXq-wHDWeiylhUhMedcDtpIU-zuYTTZm4rztUE127YUBCCkr1BpUBihI_FEq_G3iOa4ITBstsCsaZJQ22MlQ3HTChHCMv7QluzoPyTgBLFcdubQ_l-OGwG6Vrmi-AzQWDEZTQSIW01yyhWR_6JA_Z4pfNcbHNS355Yqj0idqyFutlJiOcooUgdPX1PGiKPLwAmEV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c3f17a4b.mp4?token=BmIjwf94gWTVPMktwNVQR2yxzvUBTqrHpH22Bp87n0u-Z-BIVOAdUaIWg7p15t9qjlBrq23vsOm5-JSUS-nrNP7-Z8FaO8wdPJM_Sf7yGpC_eXa8YNANkQOlr1oBOZujpkEwuXOQaE7y9w3SYXq-wHDWeiylhUhMedcDtpIU-zuYTTZm4rztUE127YUBCCkr1BpUBihI_FEq_G3iOa4ITBstsCsaZJQ22MlQ3HTChHCMv7QluzoPyTgBLFcdubQ_l-OGwG6Vrmi-AzQWDEZTQSIW01yyhWR_6JA_Z4pfNcbHNS355Yqj0idqyFutlJiOcooUgdPX1PGiKPLwAmEV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدید سی‌ان‌ان از آتش‌سوزی در ناو جرالد فورد؛ پنتاگون پنهان‌کاری کرده است
🔹
تصاویر جدیدی که سی‌ان‌ان به آنها دست یافته نشان می‌دهد ابعاد آتش‌سوزی دوماه پیش در ناو هواپیمابر «یو‌اس‌اس جرالد آر. فورد» به‌مراتب گسترده‌تر و بحرانی‌تر از روایات رسمی پنتاگون بوده و عملاً توان عملیاتی این ابرسازۀ نظامی را در اوج درگیری با ایران مختل کرده است.
🔹
درحالی که نیروی دریایی آمریکا در زمان حادثه با صدور بیانیه‌ای کوتاه مدعی شده بود آتش‌سوزی به‌سرعت مهار شده و ناو «کاملاً عملیاتی» است، اسناد جدید فاش می‌کند که این حریق توازن عملیاتی ناو را به‌هم زده و سیستم‌های دفاعی و اطفای حریق داخلی آن کاملاً از کار افتاده بودند.
🔸
تصاویر به‌دست آمده توسط سی‌ان‌ان، ویرانی مطلق بخش آسایشگاه و تخت‌های استراحت ملوانان را نشان می‌دهد.
🔸
سیم‌های آویزان از سقف‌های فروریخته، اسکلت‌های فلزی سوخته و تغییر شکل‌یافته تخت‌ها در میان تلی از خاکستر، تصویری از یک جهنم واقعی را در داخل این ناو ۱۳ میلیارد دلاری به نمایش گذاشته است.
@Farsna</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/440003" target="_blank">📅 02:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مشارکت استارلینک در کشتار مردم ایران
🔹
رویترز به‌تازگی افشا کرد که ارتش آمریکا برای هدایت پهپادهای انتحاری لوکاس به شبکۀ استارلینک متکی بوده است. این درحالیست که آمریکا و رسانه‌های مختلف، مدت‌هاست بر روی ارائۀ استارلینک به مردم به‌عنوان ابزاری برای ارائه دسترسی…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/440002" target="_blank">📅 02:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
موکبی با ۱۱۰ هزار پرس چلوکباب
🔹
موکب مائدۀ غدیر ۷ سال است که در روز عید غدیر ۱۱۰ هزار پرس غذا توزیع می‌کند. تمام هزینۀ این غذاها توسط مردم تأمین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/440001" target="_blank">📅 01:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حزب‌الله دیروز چه ضرباتی به صهیونیست‌ها زد
شکار پهپادها
🔹
مقابله با ۴ پهپاد پیشرفته هرمس-۴۵۰ ارتش اسرائیل در آسمان نبطیه، وادی الحجیر، بخش غربی و کفرملکی-جباع و فراری دادن آن‌ها.
انهدام زره‌پوش‌ها
🔸
انهدام کامل ۶ دستگاه تانک مرکاوا در محوطه قلعه تاریخی شقيف به وسیله موشک‌های هدایت‌شونده و کوادکوپترهای انتحاری «ابابیل».
حملات پهپادی و موشکی
🔹
هدف‌قراردادن پایگاه‌ها، مقرهای فرماندهی و مراکز پشتیبانی جدید اسرائیل در مناطق «قلعه شقيف»، «یحمر الشقیف» و «تله العویضه» با چندین فروند پهپاد انتحاری و موشک‌های کیفی.
هدف‌گیری تجمعات صهیونیست‌ها
🔸
موشک‌باران و حملات توپخانه‌ای سنگین علیه تجمعات نظامیان و خودروهای زرهی اسرائیل در مناطق مرزی از جمله القنطره، رشاف، الخیام و یحمر الشقیف.
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/440000" target="_blank">📅 01:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439998">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هلاکت یکی از اشرارِ جنوب سیستان‌وبلوچستان
🔹
به‌دنبال رصدهای اطلاعاتی و کشف محل اختفای یکی از سرکردگان اشرار مطرح منطقه در حوزه جنوب سیستان‌وبلوچستان توسط حافظان امنیت، یکی از اشرار با سابقهٔ این منطقه به هلاکت رسید.
🔹
در این اقدام عملیات مقادیری سلاح و مهمات مربوط به شرور مذکور کشف و ضبط شد. شرور معدوم دارای سوابق متعدد ضدامنیتی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/439998" target="_blank">📅 00:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439997">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrCtCeoyxTqD6z_hAOpT4hANBJjtbhOt09Mzb1ipy4dcEDNd7vjuhM5kNkRu2gYhUPDOCxiOabHtypaDQPyJ3SLpW0w05vXhjqU3kNKrN7rdZDriYyN_ADy9d6CHsqndR39RGHycxydyZiP-yfX9JdiTYjgdjftvE50_ET7QmzLOZsbJ6iISyyZ_jY881jBt0i2LpXSoqVPbig1u9q68jTEquV9zvQ3f2zcFaFqQPZApOgvuiQV0uVmRLsrod9UIWngeJTMumOFFw3KbXAjmIHGiIRzgYE5COGH_j0QNxa8uy5hFK1r-mnEHzsD6yVymQ72LngDIr4PVIELD5oVJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیپلمات کوبایی گفت: جنگ اقتصادی که بیش از ۶ دهه پیش تحمیل گردید، در ماه‌های اخیر به طرز بی‌سابقه‌ای تشدید شده است.</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/439997" target="_blank">📅 00:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439996">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">اعتراف ترامپ به شکست طرح ربودن اورانیوم از ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ درباره طرحی که آمریکایی‌ها برای ربودن اورانیوم غنی‌شده از ایران داشتند گفته که جابجا کردن مواد هسته‌ای مستلزم حضور در مناطق درگیری به مدت یک تا دو هفته بوده است.
🔹
او گفته که ایالات متحده به همین دلیل آن طرح را پیش نبرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/439996" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439995">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac8ba4aaf.mp4?token=hH2ERSDnNv4Vf_22CJpNDC0bc6K4_RkIm5czLnDgtBn99DiBNhGK3g_yITU8CFFBcrienqVa5VGE4VHhMTlVSV4cmG_hb88c4nrNZKH4VoXmlXlYGGA30wxLtwh24IgjdnZ-9R9ZXDe0KE8KLWIDizDjsYYsNFPRuGnQPbtQ7jq7CAQ5FOesdT7tH64XPv3x9eh-y_qSxXvyFKZjO_rO45aij2C5PXPtTzT4t8ZMIJWVIRaDJbJqqeK5bUS0oOu7bbpN8odEpro6aOqf72QrW_Y4T75HoOOh5QnRpmflEM38NR1c-jIhPvHpO5l5spyjRMZO-UqbJ46okeTU_btn-SLLNb6ZJqXPODiANpUYN4mZT6KixpLFVO6xeY-6pPGftLRJN51pF2yeXY1EJpKgujY_WLp7XTSgSzd1QUGWp3rQBB3zEucDHQmWAYiuO07DyxhK18IxtpCcsTPu0iuwnT0iMEKCWpAkNUen0n52SbrR2coebHoQMl3x9sthgP0KPlGm_pB8GigaUQ31W9hh3KJdELTHwzsBchCG8tSsQ51GCbodSBYY5pXX3e94QMpF8SxXaWj14e2jrtXLLJIMRIO_Xr7Qw_jNv2kF8EgE6CLxXRtj2ZPzNVEgpHAvIvWTpk6JcybRN64MSCDK62UANCOXHyvC30figsChdt3tWNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac8ba4aaf.mp4?token=hH2ERSDnNv4Vf_22CJpNDC0bc6K4_RkIm5czLnDgtBn99DiBNhGK3g_yITU8CFFBcrienqVa5VGE4VHhMTlVSV4cmG_hb88c4nrNZKH4VoXmlXlYGGA30wxLtwh24IgjdnZ-9R9ZXDe0KE8KLWIDizDjsYYsNFPRuGnQPbtQ7jq7CAQ5FOesdT7tH64XPv3x9eh-y_qSxXvyFKZjO_rO45aij2C5PXPtTzT4t8ZMIJWVIRaDJbJqqeK5bUS0oOu7bbpN8odEpro6aOqf72QrW_Y4T75HoOOh5QnRpmflEM38NR1c-jIhPvHpO5l5spyjRMZO-UqbJ46okeTU_btn-SLLNb6ZJqXPODiANpUYN4mZT6KixpLFVO6xeY-6pPGftLRJN51pF2yeXY1EJpKgujY_WLp7XTSgSzd1QUGWp3rQBB3zEucDHQmWAYiuO07DyxhK18IxtpCcsTPu0iuwnT0iMEKCWpAkNUen0n52SbrR2coebHoQMl3x9sthgP0KPlGm_pB8GigaUQ31W9hh3KJdELTHwzsBchCG8tSsQ51GCbodSBYY5pXX3e94QMpF8SxXaWj14e2jrtXLLJIMRIO_Xr7Qw_jNv2kF8EgE6CLxXRtj2ZPzNVEgpHAvIvWTpk6JcybRN64MSCDK62UANCOXHyvC30figsChdt3tWNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/439995" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439994">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۸ شهید و ۱۵ زخمی در حملات رژیم‌صهیونیستی به جنوب و شرق لبنان
🔹
وزارت بهداشت لبنان خبر داد که طی حملات هوایی رژیم اشغالگر به شهرک‌هایی در جنوب و شرق لبنان، تاکنون ۸ نفر شهید و ۱۵ تن دیگر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/439994" target="_blank">📅 00:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439993">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc273f3a3.mp4?token=q2fah2bV52Hc9MNxXxxOcr84qsiLC1Anw8UYfNBcE1EQNuG9DmwkJXjixAKTWnm_r-WeEcsY-4mfDf0-lXDRhrjk9sgiFrXlnBZBTx7Iz4XijedrbwGNRgbnasLNIMLVMP2VE8_20iY_ydrOULPR0WG0mWw1-JTz3JUk-jmB5DESfSTkZ0OKTN4Dgj0nLhufeBzmJCH-JS4Og0UWZFofKaELDUc5d_OORwZt5iXrTOtnYkh8jAXGV-TiTR-as0izfNMJyXxiBY1P-LOaICyhzfABMJFcJ63t9JXTHuR1tYPouFHL7VXhpvs1hi3Y56wlMwxlBkeauPqWLB8tf8pAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc273f3a3.mp4?token=q2fah2bV52Hc9MNxXxxOcr84qsiLC1Anw8UYfNBcE1EQNuG9DmwkJXjixAKTWnm_r-WeEcsY-4mfDf0-lXDRhrjk9sgiFrXlnBZBTx7Iz4XijedrbwGNRgbnasLNIMLVMP2VE8_20iY_ydrOULPR0WG0mWw1-JTz3JUk-jmB5DESfSTkZ0OKTN4Dgj0nLhufeBzmJCH-JS4Og0UWZFofKaELDUc5d_OORwZt5iXrTOtnYkh8jAXGV-TiTR-as0izfNMJyXxiBY1P-LOaICyhzfABMJFcJ63t9JXTHuR1tYPouFHL7VXhpvs1hi3Y56wlMwxlBkeauPqWLB8tf8pAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: اگر امارات و کویت با صهیونیست‌ها همراه هستند باید ابوظبی و بوبیان را به عربستان و عراق بدهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/439993" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439992">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5ac33ac2.mp4?token=U2NyX-NaxERSN9az-xjcTzFxG4AxvoT_yaicgThgpHPyf2B8bFVQowXdwMp5mjJUXRe7BmGZ0vPtLfMFYwWUWkm2geFEG9s7Qd6fEeKjNHTFeJSVDm5jLxWKlan9-A-QDzmrzu5UcKXb4IBpgjWOdlwtiqIdvZ_7jxqV93mGn-eWN2vEmP19V0cPreqrTDotfd7CKepCEjAjDPbENDL4b7ohKo5v0w2JIsLHzhwOtADfnIKX-WWKJqpV3vTSGHI_qicmL4T_FCBgFhZD8EClbMqWegOrKTznCR2byqMP3KoYwVQrYjY_J5VUODE1byHC-bvX5AKaSmEkq5YBborJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5ac33ac2.mp4?token=U2NyX-NaxERSN9az-xjcTzFxG4AxvoT_yaicgThgpHPyf2B8bFVQowXdwMp5mjJUXRe7BmGZ0vPtLfMFYwWUWkm2geFEG9s7Qd6fEeKjNHTFeJSVDm5jLxWKlan9-A-QDzmrzu5UcKXb4IBpgjWOdlwtiqIdvZ_7jxqV93mGn-eWN2vEmP19V0cPreqrTDotfd7CKepCEjAjDPbENDL4b7ohKo5v0w2JIsLHzhwOtADfnIKX-WWKJqpV3vTSGHI_qicmL4T_FCBgFhZD8EClbMqWegOrKTznCR2byqMP3KoYwVQrYjY_J5VUODE1byHC-bvX5AKaSmEkq5YBborJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: امیر قطر و ولی‌عهد عربستان دارند خودشان را با واقعیات تنظیم می‌کنند
🔹
اما امارات، بحرین و کویت همچنان فکر می‌کنند قدرت آمریکا مثل قبل خواهد بود. این‌ها فکر نکنند که اگر این روش را ادامه دهند ما بعد از جنگ رهایشان خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/439992" target="_blank">📅 23:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4bba7fa3.mp4?token=S9M1sZVMVl2Hx6OjmmXhIOiwYDqhrZ4y3tRYM62_HypiSRC-FXo5Pl__ylXz-_e8jfguSJmDSbad3dRCULi8aJliz6Dzp29r2Ej6Zxah8QS919B-1_PAJfiH-v_c6GqnpAbkQzi6E_c8IIF32zmFpklOTw9Db3ZyEnYG_TlE79GtbhiWMEWr_K5N-AMx9Y641fhchamP4bzH1IoKWfM9HbuffAyQUZ1NiwreeLGmtGiqycLhfy8G3wq-3i590Ee2oLo-QCTmPr4oOl1d3vku4ZHpjeFzvqH_GFyG0JmqKLxhlGePtpmILYAQbnSqVkwaS8xpvDvag4qs5uidQvyLHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4bba7fa3.mp4?token=S9M1sZVMVl2Hx6OjmmXhIOiwYDqhrZ4y3tRYM62_HypiSRC-FXo5Pl__ylXz-_e8jfguSJmDSbad3dRCULi8aJliz6Dzp29r2Ej6Zxah8QS919B-1_PAJfiH-v_c6GqnpAbkQzi6E_c8IIF32zmFpklOTw9Db3ZyEnYG_TlE79GtbhiWMEWr_K5N-AMx9Y641fhchamP4bzH1IoKWfM9HbuffAyQUZ1NiwreeLGmtGiqycLhfy8G3wq-3i590Ee2oLo-QCTmPr4oOl1d3vku4ZHpjeFzvqH_GFyG0JmqKLxhlGePtpmILYAQbnSqVkwaS8xpvDvag4qs5uidQvyLHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: اگر صهیونیست‌ها به ضاحیه بیروت حمله می‌کردند، با قدرتی چندبرابر جنگ ۴۰ روزه شمال اراضی اشغالی را موشک‌باران می‌کردیم
🔹
اگر امروز از متحدان‌مان دفاع نکنیم، هیچ‌کسی فردا به کمک‌مان نمی‌آید. دست ما روی ماشه است. @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/439991" target="_blank">📅 23:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53fe498cc2.mp4?token=Ag7J4cg4ne7UaXH-s0WA3y1_35lpe8InDuJ1cePF1gdthdyl6H9ZPn-moBxHXkw40pEHIbid8cFMug8L8a3TLCx4502bGJ_pXl2SVhrpzhawRyM3CLGMxIlQyb0COCDlIIZRZSAVsdmk7v4R1ZS6hvUw-SHDpB7JXYjCUd6ecO7-WNMBN-7tKOUivfD0nahs1Wiz5wgdOllxopoTZk0zjj2OnQVz__huTB9mqUYlzDI-mxWsIp62MY051JDBrB4XOg_ynzKUzVFg_OnR0l1GQtA6M-UBAYAVu0IHRPs-gl5ZrALdlE7LTASFUfDMoBqiUtFyXhmzFX_YIaAbypzBmg5Ny0ko8sHKDX13BrMaYv4D1vdQOzg2DKi3Le4qpLbFWauu8YNHvqVBkKAXacUtzdBO0xVVA0kp0EX-DzwGybt2dhFyOzBI45klxNNqTe056IpHM1NusVL5YibxdDoxxOr2mxCrfikABsJbdFdAxcRh1cRdHPMuo3Ao3jtLWyIl_-ERJ_nuP4V15YjrtFZNwlvpxHfSlnLXKWip-XW9PReYyM5XZhspungLEHbVVuZhWG7EWgiyn_6HpgVFU6mxm0IssQR9F4svzPH0iVkVEwkKRpcr9hhglmCA62Qn2Wn7MYtOXT3De5WDMgW2dBKZIhlgVubTYJUOiftONZh0stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53fe498cc2.mp4?token=Ag7J4cg4ne7UaXH-s0WA3y1_35lpe8InDuJ1cePF1gdthdyl6H9ZPn-moBxHXkw40pEHIbid8cFMug8L8a3TLCx4502bGJ_pXl2SVhrpzhawRyM3CLGMxIlQyb0COCDlIIZRZSAVsdmk7v4R1ZS6hvUw-SHDpB7JXYjCUd6ecO7-WNMBN-7tKOUivfD0nahs1Wiz5wgdOllxopoTZk0zjj2OnQVz__huTB9mqUYlzDI-mxWsIp62MY051JDBrB4XOg_ynzKUzVFg_OnR0l1GQtA6M-UBAYAVu0IHRPs-gl5ZrALdlE7LTASFUfDMoBqiUtFyXhmzFX_YIaAbypzBmg5Ny0ko8sHKDX13BrMaYv4D1vdQOzg2DKi3Le4qpLbFWauu8YNHvqVBkKAXacUtzdBO0xVVA0kp0EX-DzwGybt2dhFyOzBI45klxNNqTe056IpHM1NusVL5YibxdDoxxOr2mxCrfikABsJbdFdAxcRh1cRdHPMuo3Ao3jtLWyIl_-ERJ_nuP4V15YjrtFZNwlvpxHfSlnLXKWip-XW9PReYyM5XZhspungLEHbVVuZhWG7EWgiyn_6HpgVFU6mxm0IssQR9F4svzPH0iVkVEwkKRpcr9hhglmCA62Qn2Wn7MYtOXT3De5WDMgW2dBKZIhlgVubTYJUOiftONZh0stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: از نظر من محاصرهٔ دریایی، مثل جنگ است
🔹
ترامپ هرچند وقت آتش‌‌بازی می‌کند تا ایران را تحت فشار بگذارد اما ما پاسخ می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/439990" target="_blank">📅 23:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e8dac35d.mp4?token=nFic5WyQdXFG2sHQdm5HHCLBnWb3y-G3queZQHI7w6pS3dD7oCd7bbGigmrMZl3n3m1R7P86v5ZoitdhXL6b5QnVTfW8ppQTaKyJBaPHUaFq1PXRsYChfvnfiYoUcIxmLI6EktAx6ihzsMeYjQE6zWJ03A8pc7YIcosxcfDwk2V_fr0FefpaC1WzBzq1lI7rLcCc_Q-03ePvj1IG6hsEigORfOzM9kTf4WJXr5qp5dPFfmOYA217M6v3ftGTk31UKz7OoJP-gVXIfgrnuaV_DsxuhM3reZk1M1CXe8qKXR7Vh5n9-kjtURqYWRiL7GpxGv2VykoFn4CjyVXZHHCH83SHqmR_e6S-3d9VNO3bgKrqeoxDgiXNDQ5Ef93-IXAOIZU24nNr2g48eTyTvSKdLZO_gw8Fpk2fCEfB3kbZFnUrZjZWq7vV7FyKb5Z2nKWhPg1CoRYaHdzdf089lokRUKDTsn0SIUX6Ttx9v_oQiDLyh8baFKGB2Az904VqacRBr4qMAb8nPuBbs2qdkDEcp84Q-uE7HULrQ4343nQ6TvM3dmgeY_WPwC58ALs0KYPE3Kbys8tIXwakz4BeKb2kbT8ero77H3bzYBP4ekC8GsCvPpLcyxipZ3hIR1kJz1KTb4-PEoY0n4QKeQR9iIWcd0qjoGFCapTj6kY8JjfZdN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e8dac35d.mp4?token=nFic5WyQdXFG2sHQdm5HHCLBnWb3y-G3queZQHI7w6pS3dD7oCd7bbGigmrMZl3n3m1R7P86v5ZoitdhXL6b5QnVTfW8ppQTaKyJBaPHUaFq1PXRsYChfvnfiYoUcIxmLI6EktAx6ihzsMeYjQE6zWJ03A8pc7YIcosxcfDwk2V_fr0FefpaC1WzBzq1lI7rLcCc_Q-03ePvj1IG6hsEigORfOzM9kTf4WJXr5qp5dPFfmOYA217M6v3ftGTk31UKz7OoJP-gVXIfgrnuaV_DsxuhM3reZk1M1CXe8qKXR7Vh5n9-kjtURqYWRiL7GpxGv2VykoFn4CjyVXZHHCH83SHqmR_e6S-3d9VNO3bgKrqeoxDgiXNDQ5Ef93-IXAOIZU24nNr2g48eTyTvSKdLZO_gw8Fpk2fCEfB3kbZFnUrZjZWq7vV7FyKb5Z2nKWhPg1CoRYaHdzdf089lokRUKDTsn0SIUX6Ttx9v_oQiDLyh8baFKGB2Az904VqacRBr4qMAb8nPuBbs2qdkDEcp84Q-uE7HULrQ4343nQ6TvM3dmgeY_WPwC58ALs0KYPE3Kbys8tIXwakz4BeKb2kbT8ero77H3bzYBP4ekC8GsCvPpLcyxipZ3hIR1kJz1KTb4-PEoY0n4QKeQR9iIWcd0qjoGFCapTj6kY8JjfZdN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: از نظر من محاصرهٔ دریایی،
مثل جنگ است
🔹
ترامپ هرچند وقت آتش‌‌بازی می‌کند تا ایران را تحت فشار بگذارد اما ما پاسخ می‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/439989" target="_blank">📅 23:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcf6abb0f.mp4?token=UtHVsTb2Xiis3c7rYd8GnYAHEr4yEAcWjuup1uqsbJ-6KbaTVTBjS3Yl-N6AoR2oi1eF6tdf2ihjnajMEeQyB2WMoTosssn95v0qJKVcvIRcmpGuNvhns4ZkSWUSfWn4TeSs3EnV9CJlQcLh71sq3mgjegfHkO44tdRunq8d3jkOFbsOannle7niXBxu5b4Sx9gaiKa_H9UMrx_S1ZRZtLT-ym05Qt0rLTdl5ZRgpOVuDap1pc-e6bH3sHP-gnK1XUeqqAEmCZLBLCB6N7v2iKoGVlSZ8ExYlSBgCGmjf3h-bk5eKV0fUloctvGTfTBZj2S6RvBVjxMMiKWLJYzylA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcf6abb0f.mp4?token=UtHVsTb2Xiis3c7rYd8GnYAHEr4yEAcWjuup1uqsbJ-6KbaTVTBjS3Yl-N6AoR2oi1eF6tdf2ihjnajMEeQyB2WMoTosssn95v0qJKVcvIRcmpGuNvhns4ZkSWUSfWn4TeSs3EnV9CJlQcLh71sq3mgjegfHkO44tdRunq8d3jkOFbsOannle7niXBxu5b4Sx9gaiKa_H9UMrx_S1ZRZtLT-ym05Qt0rLTdl5ZRgpOVuDap1pc-e6bH3sHP-gnK1XUeqqAEmCZLBLCB6N7v2iKoGVlSZ8ExYlSBgCGmjf3h-bk5eKV0fUloctvGTfTBZj2S6RvBVjxMMiKWLJYzylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور محمود کریمی، وحید شمسایی و سالار آقاپور، مرد فوتسال آسیا، امشب در تجمع مردم در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/439988" target="_blank">📅 23:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af31942098.mp4?token=gh58CyH2ol00tRBDZ4wwqg2OZXikVBZ-MTNktLkgl5tQdHfYgnniPvFeWxTUQgtsm3_D803fyc8iPtGVGdHewsZJjS_owQ30-jUZob0w5-gGbcJOsx_CjgSqsM-1d1gSJQ0A7cSXup0ciEKR4UJKgFWULbfkXsZ8KXxWEiov671ku10IMFSzP5DtsJPuhGohaC1iQI0wtHm444YzoZlZWGR00HXnVmrhKEIz3r0fnWlb8_9rMq3764teiyP1QhF-c3Zz-ffHwb7qLlQQwNe94esaNsCL-OtbBswKFLknmiZQl1veRDnv-CyBZ7iL1dORyZ4BwASyqI_kfd5hHt_fuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af31942098.mp4?token=gh58CyH2ol00tRBDZ4wwqg2OZXikVBZ-MTNktLkgl5tQdHfYgnniPvFeWxTUQgtsm3_D803fyc8iPtGVGdHewsZJjS_owQ30-jUZob0w5-gGbcJOsx_CjgSqsM-1d1gSJQ0A7cSXup0ciEKR4UJKgFWULbfkXsZ8KXxWEiov671ku10IMFSzP5DtsJPuhGohaC1iQI0wtHm444YzoZlZWGR00HXnVmrhKEIz3r0fnWlb8_9rMq3764teiyP1QhF-c3Zz-ffHwb7qLlQQwNe94esaNsCL-OtbBswKFLknmiZQl1veRDnv-CyBZ7iL1dORyZ4BwASyqI_kfd5hHt_fuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی تماشایی از بازی کودکان در جشن ۱۰ کیلومتری غدیر
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/439987" target="_blank">📅 23:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
سخنگوی ارتش رژیم صهیونیستی: دقایقی پیش پهپادهای حزب‌الله به منطقه‌ٔ محل فعالیت نیروهای ارتش اسرائیل در جنوب لبنان اصابت کردند‌. @Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/439986" target="_blank">📅 23:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOP9eonz1LQCEloOBVkXM9bcULt_lph4PGZXVNVked0m3CIuQTppszcl9kefLDuIRwDY1o-FDy-bK6FVD08gwag-ZBXMfzsnklHuwhHfeyjpkJ-p2O79PVqIAmWUYvg2HYM7emAlntnEwdlulOsgpAAN1T4XZ7bQQubt5EmNOI-lITlwG28joGm9Wx4o5nNPRXRPOpoYsnTT07HdWzS6rlVcRuML57kUiBj9v68kDQfl18h6LLe62cliMzVDQqQZ7-_ebYZeRWg4dEJIEKKRPtcjFgZLRema3pAhwEBa5zGe6MhVenhPihNiJPKSMX9t4dy2DK-3vJHd9kSARFheDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOrDHZzJC0098HxgrbRK5okJ8KXD8UQdBIn4U03rQ_Rhk6IFeiwlqVHI9pAg6zol2ZtFyujei3oFzlgZ15_WLnz-RM8R7yINZpIcgRH3QGV4v_97D95UWnhhc-NP0ajNhSSu2kEgeGUQxhIfx5pnEME0gITEcWXGASv-lJuW9g2LIHe8WKhTxK554jWpZyFYPJWUw90K0XJGNk13sEgdEtM8H8LThv06dPvm1ggy2nSy858ZzcfYoKmkZKS5nqXGuoJHiyUtohq2RqKrRIT_B3tqKM2-ysw3FSgP8kp4AbMhC7JP0t8TnGsxP9KWqVPpvfsMYK14lzASWKqvo6cB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXyTHbWS5k4ik9lkTOMnPdlx1sl2q1qfldZ0ZRz-oVwHFXRqA9K94KyXytdS6mzqPCPp3zG1ptpifHOwOMurB8sKDnwutB35fNPUqThdvz7V_NzjvJZehN2_6_k-We99vgAOnJ-SZFy8Ep8y5XVxOy3Y5v-1W2iXVtqoYxo_PGjTNV7OUv6EgPMYKTnuYihsh3Pg4dmc9tUaDkuCxHyaOpr_Z5Sv2pWlhNmGUcRPkitE2b9FKRcXXOJOK1HjMYT2teITS36iC66boTENygX6RjfZ_jWB-qI2cHNBhglO8NZyuQtXbSJj5reEnLULAeuQyaoFlf2Ql7idFGA4_y4YPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLer-pW2J9DENCXyBvb-4UNHSoGUQo_7Jc9XoeOfZlt_TEvhI7xRx8Fi582QUj_cbvWaMtB-BqI5kpLk-KXAZDeqdkWx4aoVR6gO5myAdoF2W0mOWgujZOZK_Gxx1DZ5Wb0ecu88N6-Lwt7ujpPsamLFvfayQ6ef6XFHgxhBpCgfrDtkFVsYiYgpG2TJo0tBD-500k3WEGDUuKisSgv25UdzuFOh7gqTNGwrpZBEHpb64SMJ0HDFaOqfHnhhpC-XeEXKR4hvxyQyNSKZnl2GWXaYMqV-uRR9tGK7sWfajQoMUT57ou3D5Obya7MFO48omJ4Uaj44ejwOE04l9_mHpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDIfUcujPIS6V3Z7FICEP4iE6ZyU2Nkoob1ptOpLBZFz7LWXk0iFI9vob4xaysmuqMUES9g3jMd-vYp9mET4EKzD-AEVzd4aJtWWkOwF2Z-cCTBBpdHJLG5qlwCyIdNj4zPRltI-LhJvN7TtzloMLNomhYFPb2PFBjNcoH01-KNDmtqzUzAHCP3yDMZqDrGNZZlcygklp_gqFm_keJ9oMcbq6dtxOycjqsLwl9zg2QnVF-hG9XRvlUiqwt-p5dBDz0QRJmFZ03qa_UAM867wXAVwBW1vlRhDp-sfEYf54eHGt3g7f5ZgsWRKTy2omBc7caGyyGdtD4jVtlqZ4En7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hghsyg_v_DYAfRGSQ-zzFNI2nnnqp8KQTikUzZJ0D-r8yJc911S_2qQ-THTlx7mL-KWXWJ9g5P-q7Efj6-NE9zv_w4ioc-VqPJ9HR9xNm03zOv2nhh659Gaoxuq37d0XhxSHxLDZteGvHksRVf03phnbCqFpX1aN03MdgE4l-asq_VjMaPlSv0hm1DsAf2bCu9GziUhJAdASuQKK3St-FMfNrzwV3cXfo_MgQMVOjvkehSvtFRSsWBsunL2erzkY0dXihx5ouBR339QnFYLbyk0iSK7vQzF8EJ31mRtFLUYbVTS3rnDwj1RMl-faZyfebe38CIuRRs1LKraLChnaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh9OV9wLwIWoWnOkDltenffDdkj2Sh-PD3e3LcZva4gRgEAnPi9v4dWNEjuavUHlALBgv9324FWW02NdOo8LdghIahvKCRtY2tl9Mj1rnpJE5tR_HQfoJ6dpdn6zX-kQ-rJi_dMB1SF6ni76M6DZ4l05QZZHvNNqUZVI1Jo6Y4Hq2BzpNbeBifQqqP7eeN9rAfa42H2t72eMeh-1fTdvznF_ChLIGmMQPWj3JXty3t8z_2vNmA1cNqA1C3kX0F6nyFbyNyKRNix0hM6vzehJqU2kENwiXiDJB2eOyuhHFgSYjP5WTnzDw14lRNOGoY2nhuxgYVJanzEOE1CpzL3-Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غدیر از قاب خیابان‌های بیرجند
عکاس:
حسین توحیدی فرد
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/439979" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22c0e31dd.mp4?token=geXk8EoRNrjJZW6TvTqkj-7AibB-_dDJBuyuU6e7Nfxt1DoE609ijyi_nUgGDSXYm9i6t2MdyNciIPVNURI87kLAV49oB_UqUMKp7hYLKK5rU8UHCczPJwSlDbNu9nSxx8-0kjy0qmA7PMPJQz4LYGJGYgA662MtPMfQJ0Hum3QPSmcAQvSNy-iVtCGZKVOGU_IbIGyAZS23E_BOa57zzms__iUpCSc9ZI5ZI0Qgt60xBJPPKfFXIyGl_fFIHFiud5Pf2ElOIk53Q3YTzv8_A0IJzahf5WapPNVNUERM_lHr8hz7BbLX5Cn0tjgm88lF9OtCZ8xNBh_roRrFGGkAzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22c0e31dd.mp4?token=geXk8EoRNrjJZW6TvTqkj-7AibB-_dDJBuyuU6e7Nfxt1DoE609ijyi_nUgGDSXYm9i6t2MdyNciIPVNURI87kLAV49oB_UqUMKp7hYLKK5rU8UHCczPJwSlDbNu9nSxx8-0kjy0qmA7PMPJQz4LYGJGYgA662MtPMfQJ0Hum3QPSmcAQvSNy-iVtCGZKVOGU_IbIGyAZS23E_BOa57zzms__iUpCSc9ZI5ZI0Qgt60xBJPPKfFXIyGl_fFIHFiud5Pf2ElOIk53Q3YTzv8_A0IJzahf5WapPNVNUERM_lHr8hz7BbLX5Cn0tjgm88lF9OtCZ8xNBh_roRrFGGkAzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خانواده فرماندهان شهید موشکی ایران در میدان انقلاب
🔹
تجلیل از خانواده سرداران شهید طهرانی‌مقدم، حاجی‌زاده و محمود باقری
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/439978" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1186b0acc2.mp4?token=QC9ptFIlPiYYBaquGuL7ctwxSZxna7rtYMBJvqmkbvgm0BCAe3A11ac5V3e0gJ0t1YUn2IQtkHsVRAoRCnQ2vDfKP6j31vpFDLY4Ky683r-AjHtoVOT38LlpdZzmOp7HSLle2BtqlRk6cZ76rts2hhaSGyOkyD0scNa8Ij8JJ6KZxfehN_SbI7uqhkAB9WS18EbFDuWIjwO1J896o9EDGqWzWgFt1_6nuUt94L65rQsMhcjtvwnqdI3Nn_YM4w_OYRMACBIhaR6Ewx-uqOg3wC8SNOnLbkt-nOw7EfXnPXfGavVPUx7pYeNX040PL4ch1JVgPTySPiINrgCGI1nsKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1186b0acc2.mp4?token=QC9ptFIlPiYYBaquGuL7ctwxSZxna7rtYMBJvqmkbvgm0BCAe3A11ac5V3e0gJ0t1YUn2IQtkHsVRAoRCnQ2vDfKP6j31vpFDLY4Ky683r-AjHtoVOT38LlpdZzmOp7HSLle2BtqlRk6cZ76rts2hhaSGyOkyD0scNa8Ij8JJ6KZxfehN_SbI7uqhkAB9WS18EbFDuWIjwO1J896o9EDGqWzWgFt1_6nuUt94L65rQsMhcjtvwnqdI3Nn_YM4w_OYRMACBIhaR6Ewx-uqOg3wC8SNOnLbkt-nOw7EfXnPXfGavVPUx7pYeNX040PL4ch1JVgPTySPiINrgCGI1nsKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش بچه‌های تهران به بزرگ‌ترین شهربازی ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/439977" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439976">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde69484bb.mp4?token=sNoDBp9jZBOtrpATMBVd2BEgCiEKnhGACMMP4IFMoTmJUDaKHq0ouAhJHnn6VHDRK52KjCTiwIiG4pg_d1SLQ3lyM-XsEoar1tZTQ3n2PEfhZOysJm1nrsJolOJ8cqEplhL-lRCTt0NtqEZPvcdsk5um5-6-VgHbGMNGwx4rWk-sC-jHw6J7cMFqAZWIJsnZcvt-66lpqm5i63tKJmPPE9JiIOSsv2ggVuuy-l9OxFEQ43N85kTjH_wmA0Oy6sLk6iJEHMmrHhEeeVY-nhpuc30iaDE6NvWDGLd_OoENbCAHZAbFLRtruxd31rv_hNRSdx7SSOfRwHFpO_m-YyjdeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde69484bb.mp4?token=sNoDBp9jZBOtrpATMBVd2BEgCiEKnhGACMMP4IFMoTmJUDaKHq0ouAhJHnn6VHDRK52KjCTiwIiG4pg_d1SLQ3lyM-XsEoar1tZTQ3n2PEfhZOysJm1nrsJolOJ8cqEplhL-lRCTt0NtqEZPvcdsk5um5-6-VgHbGMNGwx4rWk-sC-jHw6J7cMFqAZWIJsnZcvt-66lpqm5i63tKJmPPE9JiIOSsv2ggVuuy-l9OxFEQ43N85kTjH_wmA0Oy6sLk6iJEHMmrHhEeeVY-nhpuc30iaDE6NvWDGLd_OoENbCAHZAbFLRtruxd31rv_hNRSdx7SSOfRwHFpO_m-YyjdeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از اجتماع غدیری‌ها در مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/439976" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439975">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b7cf94de.mp4?token=PMRFvPpq3LOO5N8Pl9eH0eZAGCsExK6xqeQkf5c5x9AKUrrbIVojbry9XGFuzxH1Br1rDrzC-dCJ-AcFaA68w6NnR1sTU3PYP4I8UOVsFzXL3eng_DRuNjIB3gPYbym8ga76FlhLw4bkQmG3BUUPULRxEdYgneHVRHtIrvng_9hoXXIY8RzoTnafMQpD3-_HiBj2FxcF3Nb3Hjhxj3lwTkhBxsuOWynWrLV1JkrsNBVMTrPHAQMhFyiwnPZMyxlS4tPNHwkAagY6P70v5gkfEua3150YFLIRYDdHGsQmAB0EfifVAVtOZyBwhszMZuIFeKyt8wt4Mo55lb2ttpuErg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b7cf94de.mp4?token=PMRFvPpq3LOO5N8Pl9eH0eZAGCsExK6xqeQkf5c5x9AKUrrbIVojbry9XGFuzxH1Br1rDrzC-dCJ-AcFaA68w6NnR1sTU3PYP4I8UOVsFzXL3eng_DRuNjIB3gPYbym8ga76FlhLw4bkQmG3BUUPULRxEdYgneHVRHtIrvng_9hoXXIY8RzoTnafMQpD3-_HiBj2FxcF3Nb3Hjhxj3lwTkhBxsuOWynWrLV1JkrsNBVMTrPHAQMhFyiwnPZMyxlS4tPNHwkAagY6P70v5gkfEua3150YFLIRYDdHGsQmAB0EfifVAVtOZyBwhszMZuIFeKyt8wt4Mo55lb2ttpuErg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام قاسمیان: هرکس که مذاکره می‌کند خائن نیست، اما مطمئنا بی‌باور به سنن الهی است
‌
🔹
در قرآن کریم آمده است اگر می‌خواهید به صلح برسید بجنگید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/439975" target="_blank">📅 22:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f73ed106.mp4?token=obJB56Y-LbFqHX55HnNsDBEuqBKt7VDpfRPFIKUJnasHY0umMRrayz-sj9A_-euzurhThuVIW1FwW8hrpuHgDXeV88EBDZrs0RSeTgfjWGxvtGzWdox57j4Okum_KAT25mv9Di4VBKUiNrHaLaDkJE629CBOJYNm8HJ-12xoRmYdHFXeU9tBxUCcfWampnd8A9k-Vvdv43-hUcb2FOn7kYr4QGF1YmnNM9FNo63xnOgSXnXbbYIW8L4k_-tjQC62i9j-K824ZBngR4H5QAUlI3qmeWm79wnU1cI4p_R3aP4dgpMtwHnnGd-sQIcAa57iEDNijWO4PYigbJcKvPjsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f73ed106.mp4?token=obJB56Y-LbFqHX55HnNsDBEuqBKt7VDpfRPFIKUJnasHY0umMRrayz-sj9A_-euzurhThuVIW1FwW8hrpuHgDXeV88EBDZrs0RSeTgfjWGxvtGzWdox57j4Okum_KAT25mv9Di4VBKUiNrHaLaDkJE629CBOJYNm8HJ-12xoRmYdHFXeU9tBxUCcfWampnd8A9k-Vvdv43-hUcb2FOn7kYr4QGF1YmnNM9FNo63xnOgSXnXbbYIW8L4k_-tjQC62i9j-K824ZBngR4H5QAUlI3qmeWm79wnU1cI4p_R3aP4dgpMtwHnnGd-sQIcAa57iEDNijWO4PYigbJcKvPjsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم شهرکرد در شب ۹۶ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/439974" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔴
عراقچی: سطح اطاعت و پیروی که نسبت به رهبر شهید وجود داشت، اکنون نیز عیناً نسبت به رهبر جدید انقلاب وجود دارد
🔹
ارتباط ما با رهبر انقلاب برقرار و مستمر است و رهنمودهای ایشان در زمان مناسب به دست ما می‌رسد و دقیقاً براساس آن‌ها عمل می‌شود.
🔹
رهبر انقلاب…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/439973" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🔴
عراقچی: ما اسناد و مدارک بسیار زیادی داریم که نشان می‌دهد از آسمان کویت به‌طور منظم علیه ایران استفاده شده است
🔹
ما اسناد و مدارک بسیاری در اختیار داریم و آن‌ها را در شورای امنیت ثبت کرده‌ایم؛ اینکه در چه تاریخی و کدام هواپیما از آسمان کدام کشور استفاده…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/439972" target="_blank">📅 22:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌
🔴
عراقچی: تماس‌های ما با کشورهای منطقه در طول دوره جنگ ادامه داشت؛ به‌طور مشخص با وزیر خارجهٔ عربستان.
🔹
ایران و عربستان اهتمام جدی دارند تا روابط‌شان شکل مناسب و شایسته خود را حفظ کند و میان ۲ کشور پایدار باشد.
🔹
تفاهم مشترکی با وزیر خارجۀ عربستان وجود…</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/439971" target="_blank">📅 22:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
عراقچی: اینکه ۴۰ روز در برابر بزرگ‌ترین قدرت آشکار جهان که مجهز به سلاح هسته‌ای است ایستادگی کنی، شوخی‌بردار نیست.
🔹
جهان به میزان قدرت واقعی ملت ایران، دولت ایران و به طور کلی جمهوری اسلامی ایران پی برد. @Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/439970" target="_blank">📅 22:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
عراقچی: اگر پایگاه‌های آمریکا در کشورهای همسایه ما وجود نداشت، آن‌ها در معرض هیچ حمله‌ای قرار نمی‌گرفتند
🔹
به کشورهای منطقه تأکید کرده بودیم پایگاه‌های آمریکایی موجود در کشورهایشان، بخشی از تجاوز علیه ما خواهند بود و ما مجبور خواهیم شد به پایگاه‌ها حمله…</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/439969" target="_blank">📅 22:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
🔹
ما دیدگاه‌ها و ایده‌های خود را درباره مدیریت تنگه با کشورهای خلیج فارس تبادل خواهیم کرد، اما در نهایت تصمیم‌گیری میان ایران و عمان انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/439968" target="_blank">📅 22:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke9ZGxKums8WAyRxGEzt9jgrY9v1evjWB4AL0PEL-NPOIHg-73oY_JauGPApTqBMDkNk6S0SDxWbZFni1rNnRLaLGTYb0qZMFdn4RtfBRaN22BST34Zi4Soy9CtDq6GfaHUD71USSFC8mlBWqILro5LIx6ZKSIJNqjsSlTt23r87GeXxjyGSKWLm71mIFl3gryt9O17sni021Y16EKN5o3eXPtqqEwZPx3p31o9CQn4AKgzUn6HR1ML1-gqDyo5nfkcsN9qd2iiGWxr_m6E--_HQcmj9HEDij5sSHdd4dyl7x_DaZp1mmV9zrT4wjfD2tNNLR9ZpKSaVBVg7DVe4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افسر سابق سیا: جدی بودن ایران، لحن ترامپ را تغییر داد
🔹
لری جانسون، افسر سابق سی‌آی‌ای مدعی است که مقامات آمریکایی با اتکا بر اطلاعات حاصل از تماس‌های دیپلماتیک میان تهران و پاکستان به این نتیجه رسیده‌اند که ایران در مورد «توان و دانش هسته‌ای خود کاملاً جدی است».
🔹
او تأکید می‌کند خطای محاسباتی آمریکا در باب گستردگی و عمق تأسیسات زیرزمینی ایران در پیوند با جدیت مذکور، سبب شده محاسبات آمریکا در مورد «قدرت بازدارندگی» ایران، بازتنظیم شود و ترامپ در تصمیم برای تشدید جنگ یا اعمال فشار، با هراس و احترام بیشتری، سخن بگوید.
🔗
شرح کامل این گزارش را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/439967" target="_blank">📅 22:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌
🔴
عراقچی: شاید دلیل اصلی در رابطه ایران با امارات، وجود عامل اسرائیل باشد
🔹
دولت امارات با «اسرائیل» رابطه برقرار کرده و روابط سیاسی، تجاری و اقتصادی بسیار نزدیکی میان آن‌ها وجود دارد. @Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/439966" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
عراقچی: اسناد و مدارکی وجود دارد که نشان می‌دهد خود امارات نیز در برخی مواقع در عملیات‌های نظامی علیه ما مشارکت داشته است. @Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/439965" target="_blank">📅 22:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1b0f9a97.mp4?token=uZuoKDXSs4NjkBSMWBIW5W46nhGUEM50iGFRgEVY9F5DG0s6DP3LItksQWPN9GsFFtPOCvuBa3DKA1-OX0hJMvVEqFX5wXF_-rEGsNB7SMhB8acMhyrNt3xJQ0PKNQqCrzKllTxIBu52EoLW3dJD-yCODdnd25fT7XqI_b-otV80FMis700mxtDQWFRtlGjcxSoCFEkLeWc0pyecoTdRKKwGEht0M_3OdyQC-MjFAEbyuszAbV_CHiwCSGYz0gCHK5G6eYKeT9crb20BcTAMm5PpdBNdCR_rjSwj5WBMa2HW0Td2fUh8QQP8Mg10l36olPi2ALN13D75vlDqIj6cyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1b0f9a97.mp4?token=uZuoKDXSs4NjkBSMWBIW5W46nhGUEM50iGFRgEVY9F5DG0s6DP3LItksQWPN9GsFFtPOCvuBa3DKA1-OX0hJMvVEqFX5wXF_-rEGsNB7SMhB8acMhyrNt3xJQ0PKNQqCrzKllTxIBu52EoLW3dJD-yCODdnd25fT7XqI_b-otV80FMis700mxtDQWFRtlGjcxSoCFEkLeWc0pyecoTdRKKwGEht0M_3OdyQC-MjFAEbyuszAbV_CHiwCSGYz0gCHK5G6eYKeT9crb20BcTAMm5PpdBNdCR_rjSwj5WBMa2HW0Td2fUh8QQP8Mg10l36olPi2ALN13D75vlDqIj6cyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نذر مغازه جگرکی در مهمونی ۱۰ کیلومتری غدیر
@Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/439964" target="_blank">📅 22:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439963">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
عراقچی: ما در طول جنگ اخیر شواهد بسیاری داشتیم مبنی بر اینکه آمریکا و «اسرائیل» از آسمان و خاک امارات علیه ما استفاده کردند.  @Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/439963" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439962">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
عراقچی: ما در طول جنگ اخیر شواهد بسیاری داشتیم مبنی بر اینکه آمریکا و «اسرائیل» از آسمان و خاک امارات علیه ما استفاده کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/439962" target="_blank">📅 22:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGIDV1T8bySXmWRWv5PAT-6K5M69wbv7ptU8uMB9lY7PC4mb8Tcl9t9z8gjbV9Qt78ouQNSgeuQ_NQiVEZGEzOr-KJVGSokidW7-eF6XHmT_Y7JMvXas-pFDQ5M6aMAgpY0NrdyR2ADWmrwZpqwEDMsMYUbrqy9gRwaosqYQbEGRzhi9xKLe6Ntj_M8C9_578X7fyFe9FJ6NoYbGLuFHA0tMRDmRjMsG3crO9X9NMw75aW4DmWK_ZXAXsNgm20bDwDA3ExviwM48kAtNnYrYC9Ah5beOxM3Rk8l0l1QlW0LBvUIKDCGSaE6JCu73m9JRf_lmT1OZzYq3-VoREMAD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZpiVNud63P4y2fOGFHAaMxHmLNz7C8IHt0z1cReJ_3TwMsQ9RdqFzR9UcPRgGdIYbOsud2wNo7wJ4FlXftzKF8STawzWNtqeFsRjAXVm1Tm1ZYWyrKorK_Ph_yibp3crX0sVqUvG_LkcY58JxSfU-5dbBr69_M6cEXqSvMccwtaH5iSVAxHn3d9llt0nW8maP0HqihF7aFbEif8qOle6BCP5mbh02LNUCbFs2dljWh8hwtfxwTaR_Vt-th4hA6-8z3WQYo0Nk583iYlb0xNuzf4g_kGgo9rGvNaKX77LKXnnzZuSivzQ47fFSWb4WleGwoxIvOf-vXO_XurFzLt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_16PH5xZwkUS1yD0RRzi7nCMtcD00aIrf1gns9EGtKaSJItZchgjN3sgwyH4NlIESfV337nv4wiTtMqT1voFwpgu1ckz7H7mARM-RCMvqIRKWh1MGcABd1gfRFfnkBqBVvGUyqraQ0QHfYVtpNPZhREwqyWtVV5H3hJ8_19DnJpwQKQBR1nBFcEs6smTUs7F2DlUB2MZCCnQu6GB5jDYli_a9PtdPAbIdd9icgoAnFD4ZqVwAtNmisFLUeAEJASNJbsdRy9IvffBwZplUAwRCc4EnnCVjxMdydGntCI0jdu-JybZlmx0AVSJtOl5gkBpc7BG_R9X_vdsthIoZUb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYIPTQdnO-iyEyR8LPdwmh2dGl9eDrCLeT-SK_BZa65UWLbPM9dN03-T5qGUOnXQqy-pmxgbwI6ETxSGoona-Zv-fByDj8AYOohhe8Qgo08MHWL21PGNYYGYyTa2ZwVhM-WWeYKBMgQzGQvi4tA_D_agYtO3YKujIQAU9lSdInwLa9nJY6wq-YwwFDGBMCYiYfsIv5xo6vOh2XZZ9zFdIlY2bXLK19Jlj4vImjP_StEQNNNAdfUTJwXlwfvj8ZSle45ybcU737S7Z_UVic6Vs_CXOQcOOF5TDJfg2HklTffaAx5yhUzxQFp9iz5FAL5u1sagM3pD4sVQWDHEDN-Ynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqYgwgAeYsFxuHqa-rFEAusDgmWifa9xEIRkmgQCOaf_V3JrmzsMReqwOZ-NYEhdXV4lGcuiPGXdDD3Me8e92jpt3l5TdEGMJ0GkPF4e5nZMo3qB8Jz55hJgBtRDBAMtL_lQVE28S0pE3Jx-kIY95vZ2iWHPbUHTeNMl3fdCnxQP_WhPlM7tB-8PFOwayNdXpVDXuXwr4RlZuuVGd7kxG60gmjRJKI12TZ46xzw_ojJhKFthuKai8HjYuSnVH5BqssL_XP5igxUiWnbkSQkXFq6ALE6B7DX1zIUYHoj72Mo96_pJS1W3g4CCFFdFVTB86mh1flfA_mNFgx65eWh-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kR6Ny3JpB5KGqD2CykYjuXeoLDx-5lYur3HEaF5HAgI33goz4ZUrtsJjeuwykvLjLpSDbLedkMfhoLypKZrVzdU69LtQhb8c3ap1I3RCYSBYazq7FKbOXX683qDW99vVLTSoLWLJdIzuAT_fBAM3WKLthN31rBlIQHvoRX65yJX5uIt-55_Jl4CdU8JyVTEC3YFAEAfX7o9KHP2_xXT9ncvPgLCySSHODod0RgDOmj6VW28mrqlxDc-6OU_eb3-8S0ecuUAlc9W84p63mgnPHb-dhCAmQa8A1Z-Dat7GQeBJIXbUAyc4D_I_b2TtYPXhW06ZkJsEc13qckHvgVThiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSsIbSDh1mkipgghm5WY5J76BkWIvzL45ZTYtJe6NgoTntvQxI7iaLEm2B_YX4ROZaN9hW0pZjtW1NLyW7729orhP1f28pvGzXVPY1CK00ALZj0tCd1NHGRh8eqvAS9FNX33p7LrbyObIHKRgy6K-HpPK8DzD1Fsus9K7mOTONKjOakixLfR7X7FpK2rWvembt2UBWQaCzzHtO8NS-eztn2G99dfTUPGgGlyYfRJD5kuSG6ef64OvRK7ysZCaUSf1aspLfxz4fo99FjXOw-rznUCuVzCLQwMZ71DaXl1gTM3Z9DQN2nDnSRzf5ITQGUkW8g7K7098YgSUT4gg6Cq1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مهمونی کیلومتری عید غدیر در اردبیل
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/439955" target="_blank">📅 22:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439954">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f329b2f60.mp4?token=oFvrEDDiWFpvZ4i-eTYSBMZ4qpPuposgNyztkjRLspMP9KMsQbMEF4eacNkOCV3exJK2_24RynfbLdcMuRVfJCYz52QEBlZuqWBc1L0NEOqZynxwGO4b1REkn3N5KxDplczw0rQiJ0UQaaWwVOt8ypcgCgrDvd3hpuWoz7HNI5c6ndvpjnjw3U0arpjo54ys6pLCZ1Pxn_1SxqK3B_C01E3lOD57yynAxbXGLjvtQPI5Yd4osEmm1xW5FosuAeuDwmk0w69uIt2IsQT2lE6uJq6WGq6VIPXCYXtvJWH8trIzK3uKPpUHLlGVctZkSCkzPVB1n9zRGvmNmhy-LcTAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f329b2f60.mp4?token=oFvrEDDiWFpvZ4i-eTYSBMZ4qpPuposgNyztkjRLspMP9KMsQbMEF4eacNkOCV3exJK2_24RynfbLdcMuRVfJCYz52QEBlZuqWBc1L0NEOqZynxwGO4b1REkn3N5KxDplczw0rQiJ0UQaaWwVOt8ypcgCgrDvd3hpuWoz7HNI5c6ndvpjnjw3U0arpjo54ys6pLCZ1Pxn_1SxqK3B_C01E3lOD57yynAxbXGLjvtQPI5Yd4osEmm1xW5FosuAeuDwmk0w69uIt2IsQT2lE6uJq6WGq6VIPXCYXtvJWH8trIzK3uKPpUHLlGVctZkSCkzPVB1n9zRGvmNmhy-LcTAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بن‌بست وزیر خزانه‌داری آمریکا در پاسخ به سوالات اقتصادی نماینده کنگره
🔹
مایک تامپسون: شما پارسال گفتید که ترامپ پایه‌های عصر طلایی اقتصاد را بنا کرده؛ قبض‌های برق ۸.۵ درصد افزایش یافته است؛ آیا این طلایی است؟
🔹
قیمت بنزین نزدیک به ۵۰ درصد افزایش یافته؛…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/439954" target="_blank">📅 22:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439953">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5e53b53a.mp4?token=nJckf-RXeVWhCehRHI8vpxRDL9A93p4-H8yhBxHCZsCwbnxADjCGnVLgYudP-rU4eFNEl5vYH12FyLEHbJJfpFGwjbvJbvgaILZOEWUMT-eWbKMpYwR12XKjvlGt_EXrqbJ5GgGj3vOLXdqqtsRDVWyeZ9YhhmAvHe1amXS29j2qCOkCYVLbWb2YucZjiEf6hUURV-LeH20vStpqLaahDQxk0bv8Wt8ynEwmFmxNMU5gK25qcR_2H0iG66QkDey82ua_eKwyNfZMzYO4BxZ6xa6X3aygCROXoVMaLUMsUubaM5PXIUfbGsQVicmI-TYx0eVLSIWPMJAF-14rEcdf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5e53b53a.mp4?token=nJckf-RXeVWhCehRHI8vpxRDL9A93p4-H8yhBxHCZsCwbnxADjCGnVLgYudP-rU4eFNEl5vYH12FyLEHbJJfpFGwjbvJbvgaILZOEWUMT-eWbKMpYwR12XKjvlGt_EXrqbJ5GgGj3vOLXdqqtsRDVWyeZ9YhhmAvHe1amXS29j2qCOkCYVLbWb2YucZjiEf6hUURV-LeH20vStpqLaahDQxk0bv8Wt8ynEwmFmxNMU5gK25qcR_2H0iG66QkDey82ua_eKwyNfZMzYO4BxZ6xa6X3aygCROXoVMaLUMsUubaM5PXIUfbGsQVicmI-TYx0eVLSIWPMJAF-14rEcdf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت مطلقه امیرالمؤمنین(ع) توسط مردم در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/439953" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439952">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/827e4e7f2f.mp4?token=BMSuuotkxXlUzKOTt_hqvZpphX_DBS6r6T332tkkU9ex9oFGwJwHBNhl4abCQw8qH7dErLa8UvHhN-pGGPJ8ZfPrgZArJ8Asd5NDapKL6wAAoryn6nTW1-9Et6pJ3mRu1EoxXrg-a-E17ktFc0i-ABlgk8iRWN4ZCix9FF76CbO9vbLwUh1-I0KOGFs8-Et79naOv8RBXQslxVNZeMOIRNrwEMXGUfyyHXQETIK_KdjoUbAHwL41VOGMgrxuxnr1cGCiV4nLdcPBHU8J7VaW8E5ARwgTMeGvYv1gxh9pWk1Kb_-7_kSZA3sDgofkVNnfvMOcZhvwh71aoT7SbShYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/827e4e7f2f.mp4?token=BMSuuotkxXlUzKOTt_hqvZpphX_DBS6r6T332tkkU9ex9oFGwJwHBNhl4abCQw8qH7dErLa8UvHhN-pGGPJ8ZfPrgZArJ8Asd5NDapKL6wAAoryn6nTW1-9Et6pJ3mRu1EoxXrg-a-E17ktFc0i-ABlgk8iRWN4ZCix9FF76CbO9vbLwUh1-I0KOGFs8-Et79naOv8RBXQslxVNZeMOIRNrwEMXGUfyyHXQETIK_KdjoUbAHwL41VOGMgrxuxnr1cGCiV4nLdcPBHU8J7VaW8E5ARwgTMeGvYv1gxh9pWk1Kb_-7_kSZA3sDgofkVNnfvMOcZhvwh71aoT7SbShYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای متفاوت هلالی
خواندن به زبان چینی در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/439952" target="_blank">📅 21:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439945">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLGcw-4yVk0NavROgEibDotpNsG71IRz7zrTA0iy7GnW2IddLLf8UiYZKbc94PQj8rObIX3SCxzJDJgzii79PC85slqENEq3pga9Q_nrIBiXcB1Kqjn9DEf8jsrJRxn9SYENX85TzJS1FSzodfX0D1fr_UjBCL9aAjqDcG3ZB4VcEhpTXCsHZsOMbupL3G5ldYxlzIp74WCOElF-Oph2WQ3-oGNlRYgOOkWWSthy1m_B0G4B7D4l3X4e7ihRbiUk0ZylVbukwIx4x8CJhobo6c7-PnwTMSjok7hm9jfD9osA1u4mKBtQLa76MyKwzbiSSMMThQQ7HJHCV6LR9V-RuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tu1Y7hp3cEttd31PI0yZex42QZscN6OjuxRSebxcCbQ4G1yJxGVvHQPs0zeI_lHosSjRWJXqMQATMhQ2n8iDHLKODvtWJdgcWz6x8vKpXbcASPgRaGhb0T5jMNkNFukFXA0aQNqIc3dlhOmvYMB7wd-QqI-EPvWnRmhpNiXHEEarPqOeGHhT1wkI_VuzG6p2Excr_nYxAlrhLk409h29qdA3_XfdhcUcjd_cu-P9zEuwFxK23yP6eEdu2aIbxZBw-aqRIvhr1exFQvO-VL-FyOCjjqEFb-sKB2_locsHBK-vB4oLzjH0NbMGbr_0GvfC3aKRiki0rf1HEPN9KCJZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hn7TdBzE8cIPUe4rLQVumR1-7BKriNLmUTI9B1jyeUdOCpracTEX_jUXoavSf3E9vH02dIlnVi3hUPlgaIs_1gmzal6wHG1G9b3hExKyu2K0VXgQFegsHkWwZzQrHl9ivt1dbe0vAECIo8wrsWpCutNIv73bF1a8dO95H-FlUOtaSWMM8TDXa1_Swn-fg_yUWAZzq0jvXO77uUMx7QVUaLb0e8wjQBH_sWelZsUfFV-3Gl2dTDf9FZRLTfKvNRzHLJEoedSnNX-FfGhSvyVuxHdZrDboAi8Kk-bSsYxk-j2rVQurBxAlGwtCeBmgKfKXWlfOYomZWoQJFH4GQCO-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpg3PSTixpZG8fEdKWOOn7y4yOcDqtlYJ8q_t8dl4Unha1ouUBjnEVzb091oC1HDTwQPWhfBZ_-hVgvUYHFNsjmupFmiivMxKshToNe1txEApj4FypfBVAJwM4MWwDf7jO9lnQBW18yU8HjnkyYvYjjZYndewmkVBSRyPeOFo-mqdUSD4sphS4UWhFhyTPtS7zvKVhchN9LLhot8KGpy6MGIC17ZajbRvOZFMT8YJpjilCyibbED53rRN4NLM67EDzIs69IFMgnqAg5fHmBCWyd5PppcbRNnugWfxD-p6zzU2V6JlNihyyyVA2UrvTqoDlRQH6GAmTTKYghA2HqM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQ2-jp-gZayZManxjnneFKC6I5phcHq_ik05G6sLy7IAJ-ctjIamcOJMimzw98TGOIVE_5uJFyEn4etCLzDDzrIJsv8RS5286b2uz8bqo4kglqdBf-J1yiKTpq8D0YeYg5tNQkrqQNK96kQ5CcC9N5PGRMtf5QQKCGCelp1MrR9nVU8LmF-PfTGVT8e3SM4UgJUNku2XMuMOxNURmJkxHQZby5TNh6EqyEbwQ2LAic5tR96dIcnoJ45TBTkGCYwH5O2FNrbwEhwcWvbeafAfqSEEbv7yKUugj33ulWsC-25hGFuNZ59Y5kzOOqBestYBwVxASqZyw4-dI3fjN9ruqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKvHSAF7Abw2EwgLyHZbJtN6wnZ4pjfKw7fJIeL-3hwGZCEJm8QuEwL67C1jFYW9da973MvfeWM7xxyiwnb_hKXGbNk9cwvu_3LvbbSnG009C_BgG5Z3HZlnFcRun5huABUcB1hwYsVtu5QNifqK03DmqRb0LpQbD7-YswTYHfj17WgpQvXOQVjtvp4Ww12TV29UvXbJHHcY8K3mB6Emjt0BXAyV-0IN2ekQ6hm2DxFP2AArcUNeKq7mezxleLCzSqGiOT7A239gzrfN-Vjj0l2omTMEr_dXwRWEhB0hwNRNNqy0Q8prZkFJPhPhygYLLP1a5yiFMC5J3QkTYjAdAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5wbt3tvREAsYkvT9rAQEipQAWpTPXi4xyKbgwVB8XAxYVp3HliadkSj0n-Jo__O4JPBBRT_P7Sw56IPwYDKRaysKIy6bOF7fE09R_zxyMPR6HeZNLfjpXEX6Td9NfxzAnvHscOa8bpBmIQ1sWKhkuoVnICe94koVoaMwxSedvY9Bc3KFtr_w1AOKUM89_x_yigv_DmlVOzkI_q8v6a2-fJ5PdB2BrGXO25UpCSDV03Uf5IaTZQiuNkSgu91Dyi0zjXCN8DeAiKYxir13BmBWA13KXoZcBJNH-UKFZLOl58P3c4sLFxx8YylQHqDkYjfzujJA2bUQbyYCzNX0_Fvsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تبریز غرق در شادی غدیر
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/439945" target="_blank">📅 21:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439944">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: غدیر نتیجهٔ فضایل و کمالات امیرالمؤمنین بود
.
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439944" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99590194.mp4?token=voq90FpCeYXn480qy12s4RFQYFCrQWuMDXywBedwGT--1Lx9gOGayjqK7jqrfJyN_8WERWwV2QjasiAGPsaPoV3UpQAAxzYU2YaUpZzRQaYR7ENcVRE4cgiItz_MSIv7Ndx8VSCt1L2xcUDwbxFBZu689-T7StHJi1aoRdRjUH2zlydHRKvoW6qDhUJY-BZRreL3Z4twh5dkF-vlkCbtchvDHFZXMi_egFGkNlJ29Q9YQ4s67uIymBc_1SLA0wNylrVmHD_Vc-OctBrAFPoQ5rWwC5Kep2oTBJBRDem5sEo7akW9zHh73TVZ8Py86kV4RrpxzWVFdhEJ5ftn398bGDW29gCGvc8fy2ueiyQx6ZPGCTdyJ071T7Uw6TTSjU_rGhkQqdtZbdcdGeEkcZAqmRXG2VoZEi6Tz-M7mZiqkXAGThsrdplzEsfqnwmwFMzKblfuzMdjaUlvorUMSx3Jz7k8v0yFstfxAvcLNQd_ayme76hOupOHbjTA63jvsWqzV4GAgmU26aqqGTQTMc6ouItBpUKTkcl13uEbn_0iC48zcgU-fedo4ST2Fi4krmJwi32N7KZyUZ_5kcoLBDCMuC7LMfOoUU86pj6Scjh3RSWqOoOSadImdL3g3_wFw7wyknt2gwKNZKtqMgb3Gg4NZzME1Bs7psFbZ8cp0JrB18k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99590194.mp4?token=voq90FpCeYXn480qy12s4RFQYFCrQWuMDXywBedwGT--1Lx9gOGayjqK7jqrfJyN_8WERWwV2QjasiAGPsaPoV3UpQAAxzYU2YaUpZzRQaYR7ENcVRE4cgiItz_MSIv7Ndx8VSCt1L2xcUDwbxFBZu689-T7StHJi1aoRdRjUH2zlydHRKvoW6qDhUJY-BZRreL3Z4twh5dkF-vlkCbtchvDHFZXMi_egFGkNlJ29Q9YQ4s67uIymBc_1SLA0wNylrVmHD_Vc-OctBrAFPoQ5rWwC5Kep2oTBJBRDem5sEo7akW9zHh73TVZ8Py86kV4RrpxzWVFdhEJ5ftn398bGDW29gCGvc8fy2ueiyQx6ZPGCTdyJ071T7Uw6TTSjU_rGhkQqdtZbdcdGeEkcZAqmRXG2VoZEi6Tz-M7mZiqkXAGThsrdplzEsfqnwmwFMzKblfuzMdjaUlvorUMSx3Jz7k8v0yFstfxAvcLNQd_ayme76hOupOHbjTA63jvsWqzV4GAgmU26aqqGTQTMc6ouItBpUKTkcl13uEbn_0iC48zcgU-fedo4ST2Fi4krmJwi32N7KZyUZ_5kcoLBDCMuC7LMfOoUU86pj6Scjh3RSWqOoOSadImdL3g3_wFw7wyknt2gwKNZKtqMgb3Gg4NZzME1Bs7psFbZ8cp0JrB18k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توزیع ۲ هزار بسته معیشتی برای احسان پذیران میناب به همت آستان مقدس رضوی
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/439943" target="_blank">📅 21:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439942">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3b959105.mp4?token=Lml0nY9V18U5GN8jyXaw0Qa1kowovYjYRi5wu7pwikYD5GihTRPcZo429w88BLNo8WE3X6ctzauBp0LplNx2GJip8fRZmIGLT4lnbIMNpeDep_gSKxvsEWgzHZ7wpIwtCf_69xlsyyLExARa8roeTZ3iIg2-4zxH7xScDyN92333DlkJuTCz96Vi76ivv2qv1NO3yVcYMkuIF0pe9wvLpy8I-2PE2yVZDGNlV4bXKQ4PyEEYP3qTlm6ULoM3HNpDgc0Vh0wWGcdSlFrWe5IegJC7y-0E_8N8jZZlNXPnpnBSKRSJlWGS_F_pXaLcQSTUQvPf70YIsMY2vnDGXKLn_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3b959105.mp4?token=Lml0nY9V18U5GN8jyXaw0Qa1kowovYjYRi5wu7pwikYD5GihTRPcZo429w88BLNo8WE3X6ctzauBp0LplNx2GJip8fRZmIGLT4lnbIMNpeDep_gSKxvsEWgzHZ7wpIwtCf_69xlsyyLExARa8roeTZ3iIg2-4zxH7xScDyN92333DlkJuTCz96Vi76ivv2qv1NO3yVcYMkuIF0pe9wvLpy8I-2PE2yVZDGNlV4bXKQ4PyEEYP3qTlm6ULoM3HNpDgc0Vh0wWGcdSlFrWe5IegJC7y-0E_8N8jZZlNXPnpnBSKRSJlWGS_F_pXaLcQSTUQvPf70YIsMY2vnDGXKLn_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته‌شدن پرچم حزب‌الله لبنان بر فراز برج آزادی تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/439942" target="_blank">📅 21:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439941">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf1709cf3.mp4?token=dSxz6lxgVZe9lasydTgWYZMqbCMa3r1atNSr0wi4kNR-iN6nF1rBRdLe-XI8Ec6alxE2uZz7HUpZL4Ahb0P8jXk4049WnVN4kD5fi3jaSNDOxHDNNdFtcRwAYVQU7PXqZc5oWUiSSbP6IPcGPMScU9ewvbeU9fAvlyOanxNwFeY4d62esffpsSGz_4IvZB8JMPUpPDxeamhpXU0r6SomsdNeB52ufQlNP3UMQioDF56fEB2MbeeGmWmdz-TZ-DDmCaN6r1gilGIiAEYUiSf0Rc3vT_27FeySJ6FAy8S4Opipgq0WjsFR9FyAOAgqmVuO95SL8vVH3-FyGqD6t6ZmsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf1709cf3.mp4?token=dSxz6lxgVZe9lasydTgWYZMqbCMa3r1atNSr0wi4kNR-iN6nF1rBRdLe-XI8Ec6alxE2uZz7HUpZL4Ahb0P8jXk4049WnVN4kD5fi3jaSNDOxHDNNdFtcRwAYVQU7PXqZc5oWUiSSbP6IPcGPMScU9ewvbeU9fAvlyOanxNwFeY4d62esffpsSGz_4IvZB8JMPUpPDxeamhpXU0r6SomsdNeB52ufQlNP3UMQioDF56fEB2MbeeGmWmdz-TZ-DDmCaN6r1gilGIiAEYUiSf0Rc3vT_27FeySJ6FAy8S4Opipgq0WjsFR9FyAOAgqmVuO95SL8vVH3-FyGqD6t6ZmsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از جشن عید غدیر در بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/439941" target="_blank">📅 21:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439939">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1101e99e.mp4?token=Qeh1LRouE2bn0TxqJufub0LMZjfoCCUfHD9ZXMtsNp4Ma02mfhI34kAMhCwPbU0rQmKK0ZlVA37UqaOkJ5gm0C4UdBJScp18GZpUcSXmkmLc2IpVyBrqbfS4Gnn0jiwzLtSqbpkj-lv4ckgVS0QIMthCXLodwpMQbcwxg8xCGwWjZ7WBVQItVQXfLndWeWQ85rC-LPZZu5y9xOXD183xjVoHBBYuv7Zo684yHjr3t0errF6lCDgs2ycMicE_1I8qfktidnD44D_HeMg1E68qB6xkfNTBWXh1_YGt-430xTy5QKodiIeIQw8H1dxI2-xmxa0Ia9GQOibChDJSIc9aXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1101e99e.mp4?token=Qeh1LRouE2bn0TxqJufub0LMZjfoCCUfHD9ZXMtsNp4Ma02mfhI34kAMhCwPbU0rQmKK0ZlVA37UqaOkJ5gm0C4UdBJScp18GZpUcSXmkmLc2IpVyBrqbfS4Gnn0jiwzLtSqbpkj-lv4ckgVS0QIMthCXLodwpMQbcwxg8xCGwWjZ7WBVQItVQXfLndWeWQ85rC-LPZZu5y9xOXD183xjVoHBBYuv7Zo684yHjr3t0errF6lCDgs2ycMicE_1I8qfktidnD44D_HeMg1E68qB6xkfNTBWXh1_YGt-430xTy5QKodiIeIQw8H1dxI2-xmxa0Ia9GQOibChDJSIc9aXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور ارسلان قاسمی، بازیگر سینما، در مهمونی ۱۰ کیلومتری غدیر
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/439939" target="_blank">📅 21:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439938">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09cfe7309b.mp4?token=XHc-lF7378hR2mV5Q0GTE8lz-Y4gcNUQ1lFmrY3C5q_ib6nj6mPJLKSVJ3sbD-xidiHfyued5O6zvJx9ngsdWMnqyP7GB_A8qTFNwtZDvtgOmna91rAtHwyCzquWqeOkLmPqH2Riy7kHS177gxDRFcUOBOVmJnOZv4KF2NQQz9IQMIZQSJoAW2wzmMA3T-eEnb-mFXlFWO_YXxSXpD6M0IQoZ8udwH8dbZRVGIKenOq6yR5G_co1WNYV1spW9yTBk7Z4Ip3izPyzNTyNyoXf7NH-SwskzvkIfvb2FU9S-IOE7tgr5e7H2bZG7xIawd-JMSDtqc5l6Wq4NJq5Wah4m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09cfe7309b.mp4?token=XHc-lF7378hR2mV5Q0GTE8lz-Y4gcNUQ1lFmrY3C5q_ib6nj6mPJLKSVJ3sbD-xidiHfyued5O6zvJx9ngsdWMnqyP7GB_A8qTFNwtZDvtgOmna91rAtHwyCzquWqeOkLmPqH2Riy7kHS177gxDRFcUOBOVmJnOZv4KF2NQQz9IQMIZQSJoAW2wzmMA3T-eEnb-mFXlFWO_YXxSXpD6M0IQoZ8udwH8dbZRVGIKenOq6yR5G_co1WNYV1spW9yTBk7Z4Ip3izPyzNTyNyoXf7NH-SwskzvkIfvb2FU9S-IOE7tgr5e7H2bZG7xIawd-JMSDtqc5l6Wq4NJq5Wah4m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مردم از مهم‌ترین کارنامهٔ رهبر شهیدمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/439938" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439933">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rz41XStE75VB1y5bR7avcXDUHJDS7s4n7u6w_2HdurCknp2QW_rlkjICbCnukTs8lKnR315JgmC9MiFeBauknqaXlSMtRlDPBQxFFaW8y5ZHkskgZX2IZ9uW88Poflh6gxqCjeFR95RG7QYUMy9TbsGIKF4GPkj1mMnaIff_qFANqGeF7WUgdunbRewKlZsIEfnprEkyjnRHdgytuqiICrlxxkSce5yBnG2OvYb5mIpaZGOFI4OaOd9sLKXsYd2ZHfNkLQy8q5MnvvLOPv_TKtMseXpnTCFLq3E77kaDSeMo2OnbBOpB02CHDQQNLKX82KDbNAhJ0de1LxDmTnZi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLmOtg6cT4x1ipprUf8H0ktE_K4_6-P-t5X9KoV-nw2YVuv1fh9wMtXbQvpHwlrYb5SUe6tplonnvDLrf6QHHVcA6JEK-jK8uTLkIEGqzeVdzk7babFYCQk5RuU8dEFAcf7U3FOrNO1k2H3AavDjWuyYA_jdQImyfbLSBKlMVo2G1S_BBOspwbnXueIPu-cEgKkjvmI0WubUtBdQWX02PeTapRDTsLtBX_VqL39dvf084jsBCWDUvwaAH4cagP9KdmCn1tlrINGHIqpVSWRpeKU-3-hhH1B19whRhy95vJGKfdrM1YUyOFEQ_aP9NLfwFj3jaaNSqkHJmzsAdoyfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcQZZ8-LuhKURCsqhxH6UmWXNkW71_SY7nZi8-8TUdCuFMmaS5TFHNT69j72NU4lFwwYgzlQ2oLE1RD6_1PEJnr5vTqFvZkjN0qtIZG-TVIZukkpxwnEjKmCE1yinp_0pQpbmyaxplItey-bLGBz8odKC6WcNj7BZRYKnB17KN97pyYpdl2dszht08FaZyndTP508DW_wmcKKj5wGSmkTiHNNtRivHAwICSmaKOhEFGp1IFbKHvaTpF6EFV_ph4oaoYcSDhBzdTdGw1HyqpiP_PJ4zC7s3sEfZbPw3cPMEgRVo9tUA6vi4HIdZ_Wgu3A3YOAPrhdaPuBI8UlICeCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5LT-ZD7n40hj8oU8v8lIN8Bs3ChhjPnJTTfUlvMFaAFgtvP9_Lt6632xsgXFPlpcUHkpdyrElcoSLS008YLCGFAJPewwb5drvhSrekEZma8zJt0r6caa1d-u155T05noG5Gk5sFsi9MNHoUFhtxliG7IciBlvYhjAW7QCkCdR0NugNjhiwyfFTuH0btWt1DWaywHRXAPTV_98PP1phfaACOlGqD8LaUtPGVAyqM3x-c7Rr1RBZMkVomaVjgUjqrjM9_Wth968OozGPuxVHK1xt0JQjYX5XLQ4_JlxoS8-lJSyYjKawLSHTwUtLV4z9rMrxVjxoY8UD0d3VivaRylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxwhjjZ6wcan_dK6yvHw-FWWSNH6xR2gwNUJcOK_XLrIHBueGhlNby4EvurKNcLro0G6sw7fnYa9l8s6F3-6GfPBT-zQFZ-xpISEofsaxbEeN_7DvzBWjhcwJmxL0CVfl6o-arTeWupGpfxZ9Ir4KIyiUJjqVtAQl6I0859sOCUBvaWDxF-xKzkwofYQcP89QEfdeoHgq-UWdHKyzxqi1vJ_a7eL9Bfc7LyylZsMFyWfqYGCfuSGdNzjNNxk9WcFSHhCkZeye7_d6eCEcOe70LtmM9rhiMqeEkVkoDtawcjb7GVJwm5HIPkJL7vqYuI1iJ-ozuIWK0tCnwPWUYmrAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن کیلومتری غدیر در سمنان
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/439933" target="_blank">📅 20:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439932">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef0f6c3953.mp4?token=HhR0GozBthdpqlNFUN0-u6I9efGxc5yAAdrfDjSzb7q7Cr4U0zBf1hhqUX0cJCHOdwlirFkewmoZSz755u38XY_gL1T-6BtrYp0LvaHNvziVLLXuv-QHSxQXaXebT8_mAfq5XERIwwxIe0LOa4-w7ouK_GT1ryrrEvsmLesdI6R_JoainRNHCeeycMaLfCGkCd9E-SniBTueE1lyww21oF7w7_ggYsgjNHWcXZfOVeXAPHzVCdm3XbQHU0xjWkTR-_tHFD92wLHcJyRvNXVuq90SqzzcCdJ33hYk7oO_8B4lyJ2u6gIkEviJGdSRdkTMEWSlsyGiEh8DMCqSyNrB9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef0f6c3953.mp4?token=HhR0GozBthdpqlNFUN0-u6I9efGxc5yAAdrfDjSzb7q7Cr4U0zBf1hhqUX0cJCHOdwlirFkewmoZSz755u38XY_gL1T-6BtrYp0LvaHNvziVLLXuv-QHSxQXaXebT8_mAfq5XERIwwxIe0LOa4-w7ouK_GT1ryrrEvsmLesdI6R_JoainRNHCeeycMaLfCGkCd9E-SniBTueE1lyww21oF7w7_ggYsgjNHWcXZfOVeXAPHzVCdm3XbQHU0xjWkTR-_tHFD92wLHcJyRvNXVuq90SqzzcCdJ33hYk7oO_8B4lyJ2u6gIkEviJGdSRdkTMEWSlsyGiEh8DMCqSyNrB9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اگر رهبر انقلاب بخواهند به شما عیدی بدهند، چه می‌خواهید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/439932" target="_blank">📅 20:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439931">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e872f355dd.mp4?token=CIsDyjd4iY-3QFgD-Ph6SoSrzwsDF9Zm_nWg40t-k4vG8_LXetGSK8aIlEwhIYHJK3j9FTArhPwwUWRcsqwieBTXmsnl-EYb_xgfPVoocxOPiWZCj5dyqvgiLu1cq7MpuvLOnDPqEIml6ASven24-RWfbZCaJzhYmeUDWoZiEK0dzrso2ny0zzAkFWn5s_zwNG_7jEnjDjGdHtpqWmM9nx5yVkFpP7aL-K5snMImUwCSaaq7fz630NsX4QmwkYT8hEWZbWjByoGfdPsZJ4wSz4H_uR4YZIOETDF0kYVC8PM9NlYqYA9fHsN_oU8pAmaguws_nQ7pa6zE9fRRtvxf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e872f355dd.mp4?token=CIsDyjd4iY-3QFgD-Ph6SoSrzwsDF9Zm_nWg40t-k4vG8_LXetGSK8aIlEwhIYHJK3j9FTArhPwwUWRcsqwieBTXmsnl-EYb_xgfPVoocxOPiWZCj5dyqvgiLu1cq7MpuvLOnDPqEIml6ASven24-RWfbZCaJzhYmeUDWoZiEK0dzrso2ny0zzAkFWn5s_zwNG_7jEnjDjGdHtpqWmM9nx5yVkFpP7aL-K5snMImUwCSaaq7fz630NsX4QmwkYT8hEWZbWjByoGfdPsZJ4wSz4H_uR4YZIOETDF0kYVC8PM9NlYqYA9fHsN_oU8pAmaguws_nQ7pa6zE9fRRtvxf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک پاکبان در مهمونی ۱۰ کیلومتری غدیر: حقوق یک هفته‌ام را کنار گذاشتم تا امروز بیاورم نذر امام علی(ع) کنم.
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/439931" target="_blank">📅 20:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439930">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3ae5168f4.mp4?token=qjlYvVSslSCeimrV1WTO2MnP1OCZ9HYOOxpqj-dEf6m_RG8q6nJoFAGlRLAXk_XcqltSw6-onbDKyLHP6G5XN29a05k6nU5k7Gll8f6BSDGJbxh2DVHuWg68kXRlsdL_BJixryoWyMHaRypd8Yb2x5MBRTE2LE6JKqqUWmc39C35s-mGT3JtVi38h1fbI_rqEtCejo5q0Y_B0c0ylZYRj9e2H5SiVI2Ky2lJd-fXV_O9IKja2PjsyDFn8j0LsLctD4bYeb4gaHLPBVl1mLpfxh-ZwsYJcJLi1-gdaXxIcucGr-EnvWWEQgTEtB5qeoxJYZYysFymo2Ru_AIC62jJmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3ae5168f4.mp4?token=qjlYvVSslSCeimrV1WTO2MnP1OCZ9HYOOxpqj-dEf6m_RG8q6nJoFAGlRLAXk_XcqltSw6-onbDKyLHP6G5XN29a05k6nU5k7Gll8f6BSDGJbxh2DVHuWg68kXRlsdL_BJixryoWyMHaRypd8Yb2x5MBRTE2LE6JKqqUWmc39C35s-mGT3JtVi38h1fbI_rqEtCejo5q0Y_B0c0ylZYRj9e2H5SiVI2Ky2lJd-fXV_O9IKja2PjsyDFn8j0LsLctD4bYeb4gaHLPBVl1mLpfxh-ZwsYJcJLi1-gdaXxIcucGr-EnvWWEQgTEtB5qeoxJYZYysFymo2Ru_AIC62jJmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطبه‌‌خوانی عید غدیر در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/439930" target="_blank">📅 20:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439929">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed5bd2651.mp4?token=l4Khe4MguzlXwgJUvihHalBQDI4R_I_Rd2-5zW5G0jb2b33SmdsrVTe6kJleHjW0abg36DTfbJMueJCcthmdAlcNSJk-cScibXAOiPydbh_rn8oUayIhxAuQ3V6fmdmJdgkTuLY3c9YPAl1CEWwnADjHF-bDvJzypMTq1w4NOK6PnX8z5ossvX_Z6w4STKj9N_ZF5XUfOLf6ND9dp7d4qM2Ex9kP26pfASuWcHTn7BKvFjvuY1qjRJSmZi-VreF-CC4PClTILssOIeJDlMsKWxfv2Urw_H3FJk8dSuR4W_ZOCAjET674wSItby3ufwoKbovkBgRmE8T7RS6u336pwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed5bd2651.mp4?token=l4Khe4MguzlXwgJUvihHalBQDI4R_I_Rd2-5zW5G0jb2b33SmdsrVTe6kJleHjW0abg36DTfbJMueJCcthmdAlcNSJk-cScibXAOiPydbh_rn8oUayIhxAuQ3V6fmdmJdgkTuLY3c9YPAl1CEWwnADjHF-bDvJzypMTq1w4NOK6PnX8z5ossvX_Z6w4STKj9N_ZF5XUfOLf6ND9dp7d4qM2Ex9kP26pfASuWcHTn7BKvFjvuY1qjRJSmZi-VreF-CC4PClTILssOIeJDlMsKWxfv2Urw_H3FJk8dSuR4W_ZOCAjET674wSItby3ufwoKbovkBgRmE8T7RS6u336pwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مغازه‌داری که به‌خاطر مهمونی ۱۰ کیلومتری غدیر، بستنی‌هایش را نذری می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/439929" target="_blank">📅 20:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439928">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
گوشه‌ای از مهمونیِ خیابان انقلاب در جشن کیلومتری غدیر
@Fatsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/439928" target="_blank">📅 20:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439927">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDb-Gys9-_KEbWSid5HsTKX0mz5bFSJ6NWtg40ZxKutBJi8j8ddtoEDldb5LiB3ag4RXbx9z-WaIKwG62aE4-lifM4l4gHs2sZLzdvAsc4eiBGkVGXHXaO3zNt9cuLzEjHvHkWvR___ZNq57EJ11DLjcZxn1iNvi4IKiBB_qNHf8nMjEPhX4WUbvJ85u069VLu26p16xVBeN4_COJVPWIqqP7km6QbgJS8QcgeggeYOnA-eilFudZtmJne8XYYMUMJD-wW40Vunn1Ucv27xaNpH1R-BrmlHXrYEwoUQy_NaER9SEKtC4A2PM1vgJyrLo0fQWNZQrvaJO8QiUT2Tu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور بینش بلور (قیصر) خواننده ایرانی مقیم خارج از کشور در
جشن غدیر
🔹
قیصر طی جنگ اخیر مواضع حمایتی از ایران داشته و پیش‌تر نیز قطعه‌ای برای دانش‌آموزان شهید مینابی ساخته بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/439927" target="_blank">📅 20:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439926">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be575cff4.mp4?token=rr6wtZk-V4IAggspYloYvu_vYr3BXLSd6WNaU0OlOtu_-Lsvl5qTPQ8VlWTAn5PycfERwo43dPaQqjvVOvGK7VP5wOiORu3liSHjhgypRz5O2fEQeHE36DDrZCBh0krD2ezGX0IueYC2D18roPVFzXOvkG62hDH-femgfB3SeGLizMLniv1-8km92-qqaVtyFr5Y2WQpMUdBe0L8T279KgEcqfiB3qbcRupExoz4-5YAq7AE8p2Djpf4a7EUD4mN_miaJf9_PruEd16uvy10gZNKI8gMawbPiIjBTmVS48RgpJ42VSy2GrsxE60H66o9iumgFtPk82FpbKdpdI_8sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be575cff4.mp4?token=rr6wtZk-V4IAggspYloYvu_vYr3BXLSd6WNaU0OlOtu_-Lsvl5qTPQ8VlWTAn5PycfERwo43dPaQqjvVOvGK7VP5wOiORu3liSHjhgypRz5O2fEQeHE36DDrZCBh0krD2ezGX0IueYC2D18roPVFzXOvkG62hDH-femgfB3SeGLizMLniv1-8km92-qqaVtyFr5Y2WQpMUdBe0L8T279KgEcqfiB3qbcRupExoz4-5YAq7AE8p2Djpf4a7EUD4mN_miaJf9_PruEd16uvy10gZNKI8gMawbPiIjBTmVS48RgpJ42VSy2GrsxE60H66o9iumgFtPk82FpbKdpdI_8sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش
‌
زدن پرچم ایران در تلویزیون آمریکا در دوران پهلوی
🔹
درحالی‌که برخی مدام از «اعتبار پاسپورت»، «ژاندارم منطقه بودن» و «جایگاه جهانی» ایران در دوران پهلوی سخن می‌گویند، تصاویر تاریخی سال ۱۳۵۷ روایت دیگری را نشان می‌دهد؛ جایی که پرچم ایران در یک برنامه تلویزیونی آمریکا به آتش کشیده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/439926" target="_blank">📅 20:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439925">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac4c1c067.mp4?token=DNsz8UBwlF6fZgJHTTUMNRch507uzAKi9LODuKUsCVh9ExW8wXSVxziBEXEhpIQiThAboKtsg-4qwRz_nsG6fraedaGLtv8ZBPLCBjwDA-zpyiam1HJPpU90cfQ2byEMLloOxOh0cHVvcUbsSkvDWwCUYYMy2VwWlB0uEJVAcXrlAfpLalqAo_HPcxioLanJK2yRLjOaBYATulxnzOjYRQAB_2CIaWW8-fMUMbPHNfo9ilhxD080kArZahyUXR8lNdn_X4hTwrmwNT61IanFQaYseuBCDFYO-9-_Ga_lbVttni4ZGOUg2jmz3pBkzObkDGW8sIcn5ZT9bZtlAwdA3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac4c1c067.mp4?token=DNsz8UBwlF6fZgJHTTUMNRch507uzAKi9LODuKUsCVh9ExW8wXSVxziBEXEhpIQiThAboKtsg-4qwRz_nsG6fraedaGLtv8ZBPLCBjwDA-zpyiam1HJPpU90cfQ2byEMLloOxOh0cHVvcUbsSkvDWwCUYYMy2VwWlB0uEJVAcXrlAfpLalqAo_HPcxioLanJK2yRLjOaBYATulxnzOjYRQAB_2CIaWW8-fMUMbPHNfo9ilhxD080kArZahyUXR8lNdn_X4hTwrmwNT61IanFQaYseuBCDFYO-9-_Ga_lbVttni4ZGOUg2jmz3pBkzObkDGW8sIcn5ZT9bZtlAwdA3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن عید سعید غدیر در حرم رضوی با حضور آیت‌الله مروی، تولیت آستان قدس رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/439925" target="_blank">📅 20:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439924">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ee52ee10.mp4?token=Trud6t-PjPM1VEboMzew8-ybsoEbs0lx3niAtcvdHLipm9cwpp7fX03r5snDL0LfccAmNcWaaJRVOp9tSTRYeAAvtgd7oX8SMjM1iQAf1CC-t8vyp69kwijslyfV4A7FRFI4ybO3YdoSsqA9ascfBkf26uGtw6rkumzAQeeWkxvBVgLUq0fxIV5tvkZqR7Ti4IdVjaj3AvpXCYPoVdElic9yz3_ufXMcQBePVZzxN_JeeiwhKCd-L_hDAee0-aNZAj45laUIv7BN5jA02RBy7l8vrSrdW7MPn4Y2jParuSOvOIbN9Xvt96wpSIKR0AH4pr0Sya7VhOvAGe4Ym55aow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ee52ee10.mp4?token=Trud6t-PjPM1VEboMzew8-ybsoEbs0lx3niAtcvdHLipm9cwpp7fX03r5snDL0LfccAmNcWaaJRVOp9tSTRYeAAvtgd7oX8SMjM1iQAf1CC-t8vyp69kwijslyfV4A7FRFI4ybO3YdoSsqA9ascfBkf26uGtw6rkumzAQeeWkxvBVgLUq0fxIV5tvkZqR7Ti4IdVjaj3AvpXCYPoVdElic9yz3_ufXMcQBePVZzxN_JeeiwhKCd-L_hDAee0-aNZAj45laUIv7BN5jA02RBy7l8vrSrdW7MPn4Y2jParuSOvOIbN9Xvt96wpSIKR0AH4pr0Sya7VhOvAGe4Ym55aow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو مجلس نمایندگان آمریکا: جنگ با ایران به هر خانوادهٔ آمریکایی ۷۵۰ دلار ضرر زده است
🔹
ریچارد نیل: به‌خاطر جنگ با ایران، آمریکایی‌ها برای هر باک بنزین ۵۰ درصد هزینهٔ بیشتری می‌دهند.
🔹
گویا آن ۱,۷۰۰ دلار هزینه‌ای که تعرفه‌ها روی دست مردم گذاشتند کافی نبود،…</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/439924" target="_blank">📅 19:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439923">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/munrrlSfTC9zZSP2ApV-KqydsphAwJGcIpK78qVgKTRmVYpPMvWbcCd1nGNsqPTg1MyLiJdv-jAEPZxuqgyMaZfUgc4E6r9Uz7u3OjtXbO0a5diKnjnccemL0nLUTW53HYZ0yQTZB8rxXITi7SDf_kI6WDm47jRRM1-QygU0GUYV2JGY0bTIANXyRnjrahZbM3IqrRqVnC6UUompj4MkceXfUHuWwEQtVPoaJk7x6IYD-8ruAjxs8pTZPjq_2_wnK-QY13RjTm7iRfjmNDZXl5RfYFWoAdBx2SUQEEk6FUVBF_U-KcfPv7HPDzNqu4KbXsbxkXPJT4EclMTqpAo4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بولتون به جرم خود در زمینه نگهداری اسناد محرمانه اقرار می‌کند
🔹
جان بولتون، مشاور اسبق امنیت ملی دونالد ترامپ و یکی از منتقدان سرسخت او، با وزارت دادگستری آمریکا به توافق رسیده است که به یک فقره اتهام نگهداری غیرقانونی اطلاعات طبقه‌بندی‌شده اعتراف کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/439923" target="_blank">📅 19:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439922">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba77baa767.mp4?token=F1NEKJxvGTmQTtYfidzNVyuGjekUYsRmLlL7ie9xsVu07ioPx-8VktGEZxC_kWbGABWW5iYUNhDXUmmtzf62Qf1mOUR3nXNTxksWy0n-PmmB83WIzWZmU2A9ZuxJ1X3QwEBggto0bA8VFh2BBu73jQvRLkE8IzqWg1dEIuI36JFvNJw3VTr6qsSisgPyL9X3SZcyodvvB6jWnVPO_tKmnv3seRrefG5H2cj84CTKDFhK5Cn80JOiDFBoAY_iM9Fjvb5rmjDkWRdXh3hELK2GPfF57D1MlxGm1CDCkUGPNWz7YoPuSDjAR5fs0jwsZ2ywHR6fVjOp8T15pKQG2LjhSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba77baa767.mp4?token=F1NEKJxvGTmQTtYfidzNVyuGjekUYsRmLlL7ie9xsVu07ioPx-8VktGEZxC_kWbGABWW5iYUNhDXUmmtzf62Qf1mOUR3nXNTxksWy0n-PmmB83WIzWZmU2A9ZuxJ1X3QwEBggto0bA8VFh2BBu73jQvRLkE8IzqWg1dEIuI36JFvNJw3VTr6qsSisgPyL9X3SZcyodvvB6jWnVPO_tKmnv3seRrefG5H2cj84CTKDFhK5Cn80JOiDFBoAY_iM9Fjvb5rmjDkWRdXh3hELK2GPfF57D1MlxGm1CDCkUGPNWz7YoPuSDjAR5fs0jwsZ2ywHR6fVjOp8T15pKQG2LjhSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن غدیر را این مردها دوست‌داشتنی‌تر کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/439922" target="_blank">📅 19:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439920">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1pLniB1SNy_ncyk9QdiE9OeiDWymQxZlXpSoxwUycJeP2LLjkuCx9b0vtPWfCUxTDC7kdvHtbcWeulinpZ45O-FO3k8R2N-Jehbbzjcp3O6PLJeB3wcKY8P4XaqmjUaopZy9Y7WnnFKo850Y84_MoROdCBmy-9wg3n7-_QIUQTGz3wrb904JW3rNh9izp3GYqOB22BSniZcxf8dRyfVlry5Z980j8c8gK3WJvaEBA_7mJBOUS_hCg4TR-MFWpnGRm9VPOwLmDjAqgWdphYFz02AB_J1ulTKSw1iaTFZrmlj2c7-2CQlnr52ykjLgQBE8pOSjTfjafa5ZFA1HsO8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIV4ZRszbdx2RB1wHe7PewHVz7wVfG5fr_lYNJyhiTgsZElIw75hh8EgYxUG5X6b-J2pqcNMPilJEWJksBCC3YXHH1wgne5cpacTaEGDDS-C3rzLlLtg0djMIRfgVPEvaSvN1xHvkLmX5r2S_QN0e7hrsVbCZLBGv0jc7D1xtOhPayGzOPsV_7I4dhgGSKdyNXv6GrKk8_j6INBlg1It6vSxvanLsz10PdYTSfs-9-iW7uGFZivrV8x_YlB-rKH9-PpR3y-MIiQSvOy9eMxKMsvQhB7H-af6L5xZB0Irv3C5sJghFgaQ8CL-T6TxfjrEMFy6eGvHNEUhur-v7YGBqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کاروان غدیر در مهمونی ۱۰ کیلومتری
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/439920" target="_blank">📅 19:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439919">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6ae89b5.mp4?token=ntnBwvnFcTlUDzTTaMHn2xWOut8raF4HJxIchAwuRm1zSHrNDRX36PDAuk-7uR-JM4_rc92IX89uADoy9bpt0skRdZbGQpHcACTT7ePdgdx3GZnRF4SIOuCF5gaKbQhL2uE7Sebb5stVkgoRCAknrGkX7XyU1yMaYxTeYg5g84J6THIMFqkm5_JsOxsTX18-j2S0ttoCdIUhEavNkOJoQRx0mw2KyxHY2umB2mPdNbod7qwu441R2QmBJE0IDKwKhFkP_APV8l29Tt_N_rJ8MwqrPCbQStba2ig8ds-xRtMl_ahgZZG7shWqQPhCdp5h7Hv3aHqPHTcWoZ7dI8d_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6ae89b5.mp4?token=ntnBwvnFcTlUDzTTaMHn2xWOut8raF4HJxIchAwuRm1zSHrNDRX36PDAuk-7uR-JM4_rc92IX89uADoy9bpt0skRdZbGQpHcACTT7ePdgdx3GZnRF4SIOuCF5gaKbQhL2uE7Sebb5stVkgoRCAknrGkX7XyU1yMaYxTeYg5g84J6THIMFqkm5_JsOxsTX18-j2S0ttoCdIUhEavNkOJoQRx0mw2KyxHY2umB2mPdNbod7qwu441R2QmBJE0IDKwKhFkP_APV8l29Tt_N_rJ8MwqrPCbQStba2ig8ds-xRtMl_ahgZZG7shWqQPhCdp5h7Hv3aHqPHTcWoZ7dI8d_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو مجلس نمایندگان آمریکا: جنگ با ایران به هر خانوادهٔ آمریکایی ۷۵۰ دلار
ضرر زده است
🔹
ریچارد نیل: به‌خاطر جنگ با ایران، آمریکایی‌ها برای هر باک بنزین ۵۰ درصد هزینهٔ بیشتری می‌دهند.
🔹
گویا آن ۱,۷۰۰ دلار هزینه‌ای که تعرفه‌ها روی دست مردم گذاشتند کافی نبود، چراکه برآوردهای جدید نشان می‌دهد جنگ با ایران هم‌اکنون ۷۵۰ دلار دیگر به خانواده‌ها ضرر زده است.
🔹
ماه گذشته، نرخ تورم عملاً افزایش دستمزدها را بلعید.
🔹
اسکناس ۲۵۰ دلاری با عکس ترامپ شاید واقعاً به‌خاطر افزایش قیمت‌هایی که در راه است، نیاز باشد.
🔹
وقتی به این اقتصاد نگاه می‌کنیم، چیزی جز شکست پشت شکست نمی‌بینیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/439919" target="_blank">📅 19:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439918">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9a47b71f.mp4?token=RBKbybXrrTd7PnOETRNGHUSddVCYGw4d8ey8jJa1vrasbJCcAnxNv54v5YDQU4aC9yLmAF0w1CoQT6VKPcZBgzbsknfhJCZP7cigJmOEobeqF6m5W3_cT6NWG722XXfo8ljK7LF6hV_kaPffkBbUl8dw3-KJ773AroeoHDH01MDZEcKvWtDcsJ66XoP_ceMD9AmJhEyXPrg4vSto2oPvwyibi1Q8BU8NEnuNwrBv04igNoociJ9wRlBq434yDa6KalUSzjeB3n2BMrevV5x7OtxOb7huK9gp0EHUOYZ1y6c3hDh39J8HU1qJJmisp7yS2H10ZvUk3hkX3iZ5o_6HCgBAZq-D3ruADO73hl-b7ypqccWXsnNSRB4i7T5E5flA80yimJxNlzkRFeG9AXLrUXDp91Dbqqc5txA8Fd34do-ftfZJ1y8svxnhjDKc6dY48DbbScOqTyUS2CHIp3PQ_pimckeakBzFOYcRj91KSbMOi056M3vZ4XsLZwz8yCG4VXYFo6834frTVQYjc-1ITKkO0KZqKKbLcjtM5MHJQll6_Zi9BMEuIalytSDFdYTk9hhwCJuQqm_QQpfqJE8T-9vlxFVpCyTL-wt7Tb8L6NjK2yUsg0TKDEV-dqJB5x6BlhiTHrqm-8x3gxejbTdFNk68tnL-ocS5ECEnv9mjm_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9a47b71f.mp4?token=RBKbybXrrTd7PnOETRNGHUSddVCYGw4d8ey8jJa1vrasbJCcAnxNv54v5YDQU4aC9yLmAF0w1CoQT6VKPcZBgzbsknfhJCZP7cigJmOEobeqF6m5W3_cT6NWG722XXfo8ljK7LF6hV_kaPffkBbUl8dw3-KJ773AroeoHDH01MDZEcKvWtDcsJ66XoP_ceMD9AmJhEyXPrg4vSto2oPvwyibi1Q8BU8NEnuNwrBv04igNoociJ9wRlBq434yDa6KalUSzjeB3n2BMrevV5x7OtxOb7huK9gp0EHUOYZ1y6c3hDh39J8HU1qJJmisp7yS2H10ZvUk3hkX3iZ5o_6HCgBAZq-D3ruADO73hl-b7ypqccWXsnNSRB4i7T5E5flA80yimJxNlzkRFeG9AXLrUXDp91Dbqqc5txA8Fd34do-ftfZJ1y8svxnhjDKc6dY48DbbScOqTyUS2CHIp3PQ_pimckeakBzFOYcRj91KSbMOi056M3vZ4XsLZwz8yCG4VXYFo6834frTVQYjc-1ITKkO0KZqKKbLcjtM5MHJQll6_Zi9BMEuIalytSDFdYTk9hhwCJuQqm_QQpfqJE8T-9vlxFVpCyTL-wt7Tb8L6NjK2yUsg0TKDEV-dqJB5x6BlhiTHrqm-8x3gxejbTdFNk68tnL-ocS5ECEnv9mjm_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای «علی‌ شیر خدا» توسط خوانندهٔ پاکستانی در جشن غدیر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/439918" target="_blank">📅 19:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439917">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee027b35b.mp4?token=D-d5sLatUTIE9u6QDZTBW3C_uOPxpHtHAYSZjbKatZg8kY8mlDnpyYXSGGJxcz8ScLvP6vMKw0wFn6RifLUz11Niek26BXOXLruyobhnvVWVJTKl30g3eFAX9PRP32baXUMgmLvAm-Nyaa9YlCwG38AO3wBjvbxLWfrBdoCQhRDTECz94YYh3R7ms485XFvQdLopRlJby-R_FMBneOgprl9Nwc7tUqEaYNzkvenBZSl9AjHdhv2CP6rUgEEJzRo4zqOINpMtkZM3VKV0e_PS-3O-H2F5dCqQcPFiQsc_N0H_QU7AFwGbrbu19MZTeh6Awg1cemZlsZUqHjO8vfv_soWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee027b35b.mp4?token=D-d5sLatUTIE9u6QDZTBW3C_uOPxpHtHAYSZjbKatZg8kY8mlDnpyYXSGGJxcz8ScLvP6vMKw0wFn6RifLUz11Niek26BXOXLruyobhnvVWVJTKl30g3eFAX9PRP32baXUMgmLvAm-Nyaa9YlCwG38AO3wBjvbxLWfrBdoCQhRDTECz94YYh3R7ms485XFvQdLopRlJby-R_FMBneOgprl9Nwc7tUqEaYNzkvenBZSl9AjHdhv2CP6rUgEEJzRo4zqOINpMtkZM3VKV0e_PS-3O-H2F5dCqQcPFiQsc_N0H_QU7AFwGbrbu19MZTeh6Awg1cemZlsZUqHjO8vfv_soWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین مهمانی ایران در خیابان انقلاب تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/439917" target="_blank">📅 18:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdtj5s6SEQcwYZy-JrVA4quhAo6nDUzmU9G5vW3IXYFex5dAcRefZ89U4kGhjoCn9w7wJcR9w4l9WI9OM0pKKhwhrjtGZj-xWhZlTh5k_HR5SCSxIgAZtSzYEt9usbJUQT_RWW-0EGli158XTuXVaZ-u6L8DaHpHjITOMTPHIAsx1Z5eKQNgzKnlqKSm-4zv6MYhM1AX8R2CPADjx90UdZvkmMQPoLOEsskRHIEKQY9eqAKUCcw-0voDbXwKmAnBEMZVOL5CHByaveZKOXhT4GjNJ4L8dVLQT4RuCU2YmvcNa-ollmOYytmg2VW5CaOIZm3LX0TkZwgomVaBfMZ04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gs8Se5JkfBpS48NW74h_e_4CryAy1jvVO6TmfN0nZPquqMG1FlIqBfJkH5EIw2gftecyrf_RPsgl3EGBKYaTeetGloaK2nkJoHujZQXVKkIHWY3DBooJH-lWtQ-_GTwaol9Oc45lnAdRIQNvrasdeEs_caUJZEaAz04SVZmoHKnvkPevICLRRmabCctg8wqjabMs7boTgGzoyfeFZ2mXbeU4snY4Fl24O2gFf4u4VLtIcILvG0pqJEHrjuukGQ2uojvXLJt45gHYtKSUbpDbRLQqndlAbkm6DMYPXS-onNNwiuItJd8YLIRkrTIeXPpyCvQ4aqJ3danH4vopnFVoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEDTKhN4ZIpeyHvfCbgjlQ1FqAUxJAvi3ddGcDJkc9xW3hX1dgtu93oTL0yt285kRx2jNO0IYw8RCcUrwwfVb0MZC4TFq23U6o0UqlOsprNo7nnVf4EufXhtIi4A1-gw4PEa4SXdvkcAEB1PzlZzC4uEG9E4s2AIBbgIeQD4Pz5z7bxHbfH3YF5BG5RZGDvjif7zmxDRTGuPvVXVuymb2AnQVpeyITZxwtzsV5xyH4jxwi-LMjHJxIVAZMUIX_6iO5R95O8PraKLcEpoT0k79vIJnp3JrE7nUE7q2ajozycLopXPgWjE5gtGMWxW6kY8jbLqc5igbUcZRy4gvxIjuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nd5tjCNWOwAgc9gfg6t5kDOl4MHd41qnkTcnzBV2GoalAfqqETIgX-V2bUrzJaA1wNIoU0ZBIFHxWs7jSYdxJa32ym2wvRQfbRYIzrtXst9lzCM4Z8HZWcnb5BPyqNxop402SuaCNhcD6CVJQgkGECpPyR0prPjGQG1Ax-rxjojRORUM-1qowkLDeqkc0YTniiIN7xHTOodYA6OJktBYfZxAGQwuDOjLU6Gr55RQTVaUpIRN8kZ9dRdDrzKS68XxsUyK9KMTCPg_YDYKyyIYg7MEaupJZ8uvUJAFOyYvtzSAuD4s63Wjeuc42M3ZcWbL-FTrDa5xom0BxCJRUKKUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVvYzAPzASH3Etyb0lelrU5TiihKOIe-hDoCT93k_YWB1wQkrxCiqItqkyE5XJlJZhD_16UX8OV4O96NK2OdS_W-KZp0c4Ty3lyhT4aNHbVyCzsVG8Z9jOzTcI_6sVAvVxEeS6eiyysZT6EUZaqyFSBFiLs1cDJQrwGltWLbKYloRfpe-E1hLpbPcZs5pNhWuUpIpbKnnYRqRA7FY6tZHxhP6MPBZfLw6B_vogJqdlAAX9MQNmVudQ3umYcuWNjF2rjl53X9jEIxWBrfYJfZFlEa1eU1pL90AZF8sPLWGx-Lh2Uhd5wNQdL3foTToI9PU10LKXSXX7vgzdmhl4yBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIt8kwZT-65u62RLu5Eu6HgcjPA8JuezEkd-t0goVu3iRXL2Y6OzhCj-NBxwvSckbhRBLmJAelazs8No4qCro0RzilM61gNdgyP9y775WDzA52J26DJ3ARRktDa-DoVo6oafPnra84x7CLMGIlSjyoaYsc_lmtfP-pEPv_Abo0CbNKV98P8utVhyFyH46nmtAINZDg9rA-RF-renAOkb-UOzrXTOzEEjFl3xa0ucPT_xtvHfGzEqfHrkMq1IDr_4n5tSG4VapWM8gQCsil_NYNqfyiVQ_itTwfnhtgmaizRQJvk0psZUIkoxzMIrZNqF33HfsCw5LlgWjdzCcHAbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLagfabkjKaKXIUb5ubcUUfq9mgbuJS18Wp5AJB9AkN9qiZR-SkXxROqT_ADqILCMFtaZR4a2dwoh1-NhKw0C1o9cC5PMkQBkUxAZ0fVQ_001Ib6dhjPeFut3OyZJvjse0TDAZt-8WyKX1GX-dAOrHhMWGEblWeDlRMB5l56yYih1Zc5-7J_IQFeTzzXnqhY7OwCNGGTkYfdo12K8vzXZm1mO0sZa-8mvqRI4yzg0dcLmYxr0kI5zdKueKBod7uEQOk24RV1ekLag913K5mWcNQLO4FhWnicBfReKB87QbR-PEhid1r-AyNVdBZjXz5iDREz542cplh2RlCrNcNttg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
جشن ۱۰ کیلومتری غدیر در تهران
عکس:
زینب حمزه
‌
لویی
@farsimages</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/439910" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439909">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6709cecec9.mp4?token=oMafchHvV9hL9K-CniVh7mHOpwpGZE6a7RLWxMfqY5vRSCOOfS-PtTxTLTScjXXKPA1gK-yAXwbiqPocpJF6BDAnzOUBGZdZy03IZ-ig3gfcCzf5LTcErktgUdu3qgTNxONt8mi43O2Qtsdl4BaYI4EIkPZw7k_og-EZbY6-T_9tn5eUop9dgCMF4M5Slo5gIN0-8bGNMqDyJUDM2WeidCKx_rkoWvpo2P1LGyS3EtN0MeF0DXgSNXNk6gvFqZAJzrIq1uhCnrdUEVg1moNggjfnetS8YpuM8IfigxZ4F2o598RVl4GpFQmBLybJ-cWiHuuSpi1dpb1Cw0r9wSvmlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6709cecec9.mp4?token=oMafchHvV9hL9K-CniVh7mHOpwpGZE6a7RLWxMfqY5vRSCOOfS-PtTxTLTScjXXKPA1gK-yAXwbiqPocpJF6BDAnzOUBGZdZy03IZ-ig3gfcCzf5LTcErktgUdu3qgTNxONt8mi43O2Qtsdl4BaYI4EIkPZw7k_og-EZbY6-T_9tn5eUop9dgCMF4M5Slo5gIN0-8bGNMqDyJUDM2WeidCKx_rkoWvpo2P1LGyS3EtN0MeF0DXgSNXNk6gvFqZAJzrIq1uhCnrdUEVg1moNggjfnetS8YpuM8IfigxZ4F2o598RVl4GpFQmBLybJ-cWiHuuSpi1dpb1Cw0r9wSvmlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نذری پیراشکی‌فروش معروف میدان انقلاب در مهمونی ۱۰ کیلومتری عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/439909" target="_blank">📅 18:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScsCB36PDKIE5mgcibBsuPeXK3R5tmJ6jCK2zFSqC9Tpe27ICJFqLQX6W3xZuFoql-oeTvDPbFevWPR_agVVlyFYAk4es9R_M3_8GNFKjEHggtLgJ6jPlLq2o9EAjjOSHDeVeOOmE_gbgF_y38JCKh5m46HBlQe04ou5DBxGEHhjyPthd_vPVN0YiIXu9C2hVbAf_E85UH3jX-SF49rF08ZDsmsmQv6ABRL-bNJs9OdPMKMtV5MrteGAs_mDpwyuWyMAhXV41nx6_-6WuH4GExi7bfbJCBEJoP4Ltln1g4bzDCNZ-z4kFXwOxy-yMhev_Q__Ba_iwpYXBNbbfv-uTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UEe7ko87_2qHL-6ehXmlPkkWHS97-4M2IYq4WUPo2tPzZVHbUQELCDb9_klThueTdq74pxGC5wF2Gh0Ti6_RQmfcJx3HYPWT9uXQ9kDLQYj4vSZGzOTPrsvHy_FLdDFHGOBsZMxHG1sCH8NRJ_Tj1AeqZyfo72Yl1wMSqkXE1TGXtCBiBiu5sUFf4KF3AMLxNIJUqul2DU48J0bX9cMY3NJCAhnr1NFlRkAQiA4nOQ2ajNc2jmfEOgpuS0EwRiE7YJ9O--AepTDP0WZMNSebxTzQBUfD3l3AcaCL6UnEJhR3vpXC5jSGdT-LOAMzS9QupdrkjWMgXcuDxuLmwytqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVAhK609W4Xo8joDoKmha6MteaJlkjorWTrOuVBIL6uOmSVNRAGN9tzJPGpC3Uzh92-a-W13smIH7EcrwsV5r5f-CPgkIJUEvQXN9VKPxcUA0n0NAIRnOVah_PfgEfrlQPmB4jorYE2vGF-WVR7MYKpsop9sJl63lx9uiVq1jw2u-yaEn-Ze0Dp8ekdUYuIiHoZh6CU1uNV1rpj7pP_aShmKpzqDe3Sp9GvND1nIc7o0jZSS8WiArj9L9fYWR1R_X9w7RWIy0CmwSy6nZb3_ITX_tzquOv46btI4S8XLas7lh5csN7asUCPoRiRab2o0EqjjAHxmNb1mLMeX6iM-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDv0GEItw6qylbYEnrYU92l97kV236RjWNiLx8WeNVcjDaoiYfsquh0jq0-9Vlysa5hkdFkGbOTJaSCLYl-11ua59B08K2I4aQKCM6heilzmdd2OnnI-KFvzCuKwAUEAe3rgMiypDCeUcNJsvRjIz-Uh9SYW-tYV1etmaqAnkpiYIHj5-33JxT6CVAmRllcf7LWveK6QfNwYqXUFOxrhuuiuM1t5Z7P-kUCbvaQ-xP2CXQ_Blvpik9aFA4S51oT35YP5XEC48RvxVfd5DMqIo5Z1ADqSH4Ct9GfNLFkwuJ5LsPnOY0Fd0-UptQx__2560oBZ8UILRr_ixveNMHnB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6zgMrtEP9S8tkIGQtMzsROfEwCElG0UvBXizZYT_DW9eP667d6tkCaIm8P_-Bq8q4bowpDY5gE07bNIqBr32a2hm5KPHM64xUD4irDE_ovsgQbaZAR5FoQDMBILiOzGB5Far6jMxGUjWvizLtmlzYjAZP54kUrRlP0dAUONVR1oh2SK9tGs442PswzuBWG-u7dL6y8S-P0E0ZeTgHA2n372kvvptxU1Qzz9jdcuvjzBBbtz1A8KGWBQTub71MdGp43dAsg0tWhj2EwZnDdaxK2ZUo0wP2fpgbFPDvn709d_ttPkoI4Q69INsRe0g_ygX6ivaawoBBVjO_J-WTGyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2dBkJ56JabA5ozMqT8CW9weeApwKR7Gn5-xEH9H9v-7B2EzFlGsp7pPno3ivsJRe9DY-DUMIkCA_00LyJIWoLjfQYgc8ANTt0YwoIOyAyjmFUz_Yj3WFSrdcVxDGbV9Ezzr8YT2XRcU8TzVtVJ4ZKV3k6vWNQi3z4lP1td8Sn4i7MtMfrPGNK83SeqOrERXVx8E9Bd55_BENpjmBz4sbGvWcK97TjefdQlN8jUs27bvlbQbDSX5NEXbSHCRspCffD-X-08_AySyhG4335uHhufEjGBKZctIsnilPk2lmDJGZrV18YPqcxbo0qrR-6IhjTmi5hfz_OOwmsGsaki5Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر رهبر معظم انقلاب و امام شهید امت در دست مردم کشمیر هند در جشن عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/439903" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
رهبر انصارالله: تهدید دشمنان همهٔ مقدسات اسلامی را هدف قرار خواهد داد؛ از جمله مکه و مدینه را.  @Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/439902" target="_blank">📅 18:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea95831174.mp4?token=KDQr13i6ae9wm0ZoDokK3zBcJj-Ca-Wsnft4ZqakphYm3mDsANsB2CsVJPiMVZIt559QZ4-sByGajb6-bYPW0TmuJzmENJSxyXVoOD4tTRXnMwQgrpBBl5J7hQ7zvduy9uLpgaOFa9vACPfaSAwEv5XxL8QBGsqebe6Jw4Z6cCw_DpjCFOGQyJHwZmkNEWukHXo01a0brYiTxl13uSAm0ahpOag26VoKqT0RyLPRyQe42Wz6CJ8dypSvvb8lf8urMH2OroE9X5LhKBjkXo5iC3WQaLfaPgH3Rt5b-c2Y9yd7e5V8dRFR8T8v870FAPD5lFOA7MivZsWoo3vyIMbKjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea95831174.mp4?token=KDQr13i6ae9wm0ZoDokK3zBcJj-Ca-Wsnft4ZqakphYm3mDsANsB2CsVJPiMVZIt559QZ4-sByGajb6-bYPW0TmuJzmENJSxyXVoOD4tTRXnMwQgrpBBl5J7hQ7zvduy9uLpgaOFa9vACPfaSAwEv5XxL8QBGsqebe6Jw4Z6cCw_DpjCFOGQyJHwZmkNEWukHXo01a0brYiTxl13uSAm0ahpOag26VoKqT0RyLPRyQe42Wz6CJ8dypSvvb8lf8urMH2OroE9X5LhKBjkXo5iC3WQaLfaPgH3Rt5b-c2Y9yd7e5V8dRFR8T8v870FAPD5lFOA7MivZsWoo3vyIMbKjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نذر گلس موبایل در مهمونی کیلومتری غدیر!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/439901" target="_blank">📅 18:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
رهبر انصارالله: تهدید دشمنان همهٔ مقدسات اسلامی را هدف قرار خواهد داد؛ از جمله مکه و مدینه را.
@Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/439900" target="_blank">📅 18:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۵۶.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/439899" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۵۵.pdf</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/439899" target="_blank">📅 18:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d459ca0d.mp4?token=baC4Bhb8CQPTTVgIS8TRtzQCjsSNWpR-6xxtVCJSB9_GNqlhiv3IsJbQ2fRLkitfXZv-bMAvY_1EPiiOxU2RQYfESK3DgDSMpcBAkMTba3mkuTf4Wlrre4bXcPG8DmJTm2fkBZPIAiFv7dsmkjSkAnUmzSOd_NsxFYfTMVFDChlEN5135EQ8SjSuwlp1MZOHd7dC4vTq1gKoamXihUiywMhF-9EC2vF--YY8FFD_2P5s6iNRxZg9ShbN5cahGMJVU5-IjJtCRxbtPyNE2brpu7kMGdnqMAINdKL6MGzow5fK1hlKlaw1eOcbyB5otBOoIZofOQVXGDVx4h0UFWWjPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d459ca0d.mp4?token=baC4Bhb8CQPTTVgIS8TRtzQCjsSNWpR-6xxtVCJSB9_GNqlhiv3IsJbQ2fRLkitfXZv-bMAvY_1EPiiOxU2RQYfESK3DgDSMpcBAkMTba3mkuTf4Wlrre4bXcPG8DmJTm2fkBZPIAiFv7dsmkjSkAnUmzSOd_NsxFYfTMVFDChlEN5135EQ8SjSuwlp1MZOHd7dC4vTq1gKoamXihUiywMhF-9EC2vF--YY8FFD_2P5s6iNRxZg9ShbN5cahGMJVU5-IjJtCRxbtPyNE2brpu7kMGdnqMAINdKL6MGzow5fK1hlKlaw1eOcbyB5otBOoIZofOQVXGDVx4h0UFWWjPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم در میهمانی ۱۰ کیلومتری غدیر در میدان فردوسی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/439898" target="_blank">📅 17:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439896">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7hlJ920FkWPkPP3f4yQ_9dH4k-YCharBa_bsTQIbY-aAvHhAbSkRaHhsyCRJFNbX2tl67PdVGWjRcG49MGfuu1IPq1-YCbQYpImlmzfnVjcQhLYFb6XzHUB0l4rZPC8DSKa2DsJpCAixpZS9ro81D-HxzTTwNno2BIbZ0HtMeOwMpsctU7WcUsVBdrNLoYqYyKQBoSsYmBa3tmO0pTRB7-b5LaKcYa20YAdr9xGS3WruolYBdc8H3a5aqUb2E7jKmiS4ym3jMAi1K6ecRaMyBGYgPeEZmi331259yLcXXB8LaINfe7MQRxNnvFZWXMhYtiO5i8fPyWKPxoASfl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۳ محور مهم پیام امروز رهبر معظم انقلاب
@Farspolitics</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/439896" target="_blank">📅 17:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439895">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
خبرنگار شبکۀ فاکس‌نیوز: آژیرهای خطر در شمال اسرائیل درپی حملات راکتی و پهپادی حزب‌الله به‌صدا در آمدند.  @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/439895" target="_blank">📅 17:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439892">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: شرط اولیه ما برای پذیرش آتش بس در جنگ منطقه‌ای، آتش بس در تمامی جبهه‌ها از جمله لبنان بوده است.
🔹
دشمن می‌بایست با فوریت حملات خود به مردم لبنان را متوقف کند، و سریعاً با تخلیه سرزمین‌های اشغال شده لبنان به پشت مرزهای بین المللی عقب نشینی…</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/439892" target="_blank">📅 17:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439887">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2g_bUz16422uWcIHVgA5K-BbuuiNCIaXBv3T5-gpdSSMDZoVM586ciwoBaA1XPVYf50EyjCCXQERa6r_e59VmhcW5JhAN0vAxsKjZmsglysaB9Mr30Mof9H63rA1oRjmKNqui-b2F32dC7JLUNQ55a-BztMFG0_i6Yr6CJlM-zLpIxKGPI9J76GmQ1rpycRgPt5NNq4YOGwRBrb235HhxauPcCYhahD1Pp9wC6F-oERANqqYWyil5EO6wwU5mliSMJSL5_E3KIA3qydWBXl8rzwLWd_Y1_cK2qwTbTK5s6PH1aIzI-VyJZrvJw8QCcSj7mulZsLfWbiTJBJRrwaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5O0TG1Rnuck6N4ubJfUYbxLu0Mv5pBxPwjWmV85OS2v_v0P4_uDWVo47TW8PKHgzQgRuX8gQLoe0BFVFcXmvN6r2WAwSl8lWZp1rq1_CDPP7hYjonexa-hfSFDFav_aSzIbwSrA0IXF0-WwnAhcPG2De-HRJSBYFvCH5ACaPwOTZfwj8WTxUgyYuyi0wCeYs-yO-F9TMeFfRrnlrQJu00BtBTAa5OY2RxJQmZgQumtVyosm5d4uV0w7BhxvQ0ogMWs1YC39aYb4PYWhThCum1PBhEXkxUk8GDhZIaYi-PZA7c2KO7Ky8K4gvBKLnLH6dLhW_ajuVTuaV6FaDXx-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQyjHqaxnmVjthHex3VBBoR9pjkPnNPJJikO7q_Y_D4K2xNl6-ZhVA_BkCicdVmSQYbDi6HbjjWe-GuIxfFX-2DR9bL358Ickc7Y3udJp1K-9AHKIlbPAA0o2AL-YrQYIrg6nuNTUth6ZjC6_e8Zl1eY5qR-5i7UP-S36pMKOD0otcK49EOGsIt7mSZXamIDudQlHMgiI6babEeHTsgbWUfphr7U71wyWu_CD8h8x16w3bSJOIBZ9CDY8UZA267Wl4qrEEiuhyp_5heiyXCcbwfmc_5uG2adztow5GXBBlup5yoStbGfhWLJ1juPx-uUK3xXtPHaW7A838G-dKcjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVTeg1HhxKggAhi_3g4q7g21CuYJfqwZHA_JC67zCt-5j7uLAY1oE-G2ITeLV2DoNPRO9D2FUVblrIAk1crGNLtgn6YqPUSql8ofnEzqXCXT1_GvMVVzJwKSHOyxcjt1H2bYezJ2e2qAO1OdW-22oM8Unwl1DPlNSpuksO-nzT2EVOr4hMzxcFTHU3_ziPxCWW8UQcamFU49DpsScr_WB72H1JtAgg7L5z9MPBqObzThWt9xPZ6ifEsvhCYqAJzjfNpxXzZmlOz29F1Jn-svW-1atC4vIygl53T_fdYye9bA63tSKI571JY2LBd6IF63m8cTDo3GD1cvjrCnEA7Ftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHvZoftfE7jZ9Ml2x_O1Aqx3WmOFJja-vTRzrrgk7Ine-9r9TOC1WShK8ehkNQ8_vyswlMP8uN7rEodz10jkR2vcvOt7WYnfTBMJzfpkHlDNbCUNB_5Unabcbfj4jcslqRLlkX-Bp65zWmcWmXL163TIH7z3zFbWG5jnCDctpzUy48-sAw69iWKe8OwphsYhrLD5K9eWHZ_2aSub9O0V9nNmbpBlI_UdIRNqoVu3mwBAeRfCtinf7k585_dwo3l55aDmbL4SBEhrx_VzDoDOtiGpzW3Y09M7SxHtHWxxvi7RrBFrI67T2-_2N8vxas1ePH0BFZ5HqIWZ-34DLqZr6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عید غدیر در حرم امیرالمؤمنین(ع)
عکس:
امیرحسین ‌رستم‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/439887" target="_blank">📅 17:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: ملت‌های منطقه مردم لبنان را تنها نخواهند گذاشت
🔹
ملت لبنان اجازه نمی‌دهند آنچه را که رژیم غاصب نتوانسته در جنگ به دست آورد را با حمایت رژیم کودک‌کش آمریکا با قرارداد تحمیلی به دست آورد. @Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/439886" target="_blank">📅 17:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439885">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
سپاه پاسداران: دشمن باید با فوریت حملات خود به مردم لبنان را متوقف کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/439885" target="_blank">📅 17:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439884">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
سپاه پاسداران: دشمن باید با فوریت حملات خود به مردم لبنان را متوقف کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/439884" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f91e90be.mov?token=JB_Dvvn-r___DBAHd83cXyVQwHtQZfI5zvYf76W90ntI768atJjxFkWNtpXHn8_TktfVIfWe6KN24C0xmtzMQb9JTFVPU2Rqf2pSv6uzPeHtjl2rTSDLSSHE3Rbo50HWqSOlLthcTcMsav4GDgu70hpdAVkDdzkYT2I9i6Jgdo3BMiPZIrE2iUeoj9EnWFbS-D-bJLLHDUj7XDqP7U6gnD1w8hoPcw_oBdggiujzqMmy9fovsGksqu7DS-n8dvSQw8uAeA6Cn9ourSGcdY805epQoC17S4aIfsBB_p2G-3hYZbD2ewph-87EtVd6TpoFZA3QVdPBIjzeC_Z_Xx-nxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f91e90be.mov?token=JB_Dvvn-r___DBAHd83cXyVQwHtQZfI5zvYf76W90ntI768atJjxFkWNtpXHn8_TktfVIfWe6KN24C0xmtzMQb9JTFVPU2Rqf2pSv6uzPeHtjl2rTSDLSSHE3Rbo50HWqSOlLthcTcMsav4GDgu70hpdAVkDdzkYT2I9i6Jgdo3BMiPZIrE2iUeoj9EnWFbS-D-bJLLHDUj7XDqP7U6gnD1w8hoPcw_oBdggiujzqMmy9fovsGksqu7DS-n8dvSQw8uAeA6Cn9ourSGcdY805epQoC17S4aIfsBB_p2G-3hYZbD2ewph-87EtVd6TpoFZA3QVdPBIjzeC_Z_Xx-nxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی کودکان در میهمانی ۱۰ کیلومتری غدیر
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/439880" target="_blank">📅 17:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae53733e32.mp4?token=aUF_mqD9sD4UGnDF8BOgB1VQX1rONCtV90VAqUQJlmwhyhQ1aYk-fSnjdv48QrAyrFis6sO7AgK97ohH0mVygm3-5tTPoewcx3bO3H74NGn5w0LvEiPLSsPxgvwxzY0cbV53yZ55DfHn3xSUx9ADmwNOHBUQBnAnQ-bgt9iiOuRnzAd4Tipf6PYRCPeHzxzqLHi4OiAPedcF4RpHwQXvOta9FRsU8-NO4RnUzEX_6QlUeRmXv-aMBlRWX8R4cfonhftnlkQs17_ubO-Lqnb0p0lWYYd73dUMt5xyIclm1MmPM94iTVtdELHTscJ1muU5PJA3cQc07O3ZjGWwrxjimg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae53733e32.mp4?token=aUF_mqD9sD4UGnDF8BOgB1VQX1rONCtV90VAqUQJlmwhyhQ1aYk-fSnjdv48QrAyrFis6sO7AgK97ohH0mVygm3-5tTPoewcx3bO3H74NGn5w0LvEiPLSsPxgvwxzY0cbV53yZ55DfHn3xSUx9ADmwNOHBUQBnAnQ-bgt9iiOuRnzAd4Tipf6PYRCPeHzxzqLHi4OiAPedcF4RpHwQXvOta9FRsU8-NO4RnUzEX_6QlUeRmXv-aMBlRWX8R4cfonhftnlkQs17_ubO-Lqnb0p0lWYYd73dUMt5xyIclm1MmPM94iTVtdELHTscJ1muU5PJA3cQc07O3ZjGWwrxjimg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه اصابت پهپاد انتحاری حزب‌الله به خودروی زرهی ارتش اسرائیل در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/439879" target="_blank">📅 17:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv5_s2yNaj70BTsG1n3QrLpHReo2j2SBRtybFvRil6A05Adrrykfa8K68uay6ota5d1FKAHLFxNVrvNI4kosS8Bf2orWOcwSVCaFiib58XG41UGiTlckNDjLxjb73mYqkL-8-FRjarVWvCWzfZ9jqJrIDyHdmgdanT6yJY8XmsiuMpV-82qvzomrmddSeGhHWadgHKMVemb6NwGuLDbSx4NcMbRZLWkj2SurBbhD_QVp7JuXvXtUrJ3LkF4gC7r-odQLuw2LOKY9Q5KmDFFD6jceVj_rgWHowXl0Gj5rBeC0EMLKHsz3pL2IzAnGdfMsh_aejVmSqXI-YpR7zFryqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: حفظ وحدت، انسجام و اتحاد چارچوب و مبنای نظری دولت وفاق بوده است
🔹
با رهبری عالی‌قدر انقلاب تجدید پیمان می‌کنیم که از این سرمایه گران‌سنگ حفاظت و حراست کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/439878" target="_blank">📅 17:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
جشن خیابانی مردم بندرعباس در شب عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/439877" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f1aa555f.mp4?token=aT1rt8o5tTLwIhvvPsFDAnDbILUafkWJ2WY_02Y4pP1pk4Qm-OpEMzOGL5ETLIurSbjzAW_0KLQ2Rhu4HwF37cXM_tH-_MdrjOSbDIxb2qMP9Yz8f-BNJT9QlLFvI5u45gQnuWSmmo3t-EhDeEfCLGH90H6Oh4ALZxhboo1EiKG7kUPD0Ujpfu3e15a3ARfM9dCaWCAXJfSR_5aElUvGtOZgx-_yz8dSmItOo4SC_7kJ44IKkOqQjRUqzDhBDXkfoKZyYOQMqGIHwylagaltMwjiJLFH9Y4i6QdV5zDHfjEplWWZriocaNRG2tIw7gm5dfHefJCv5LGf2l9jT4zTvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f1aa555f.mp4?token=aT1rt8o5tTLwIhvvPsFDAnDbILUafkWJ2WY_02Y4pP1pk4Qm-OpEMzOGL5ETLIurSbjzAW_0KLQ2Rhu4HwF37cXM_tH-_MdrjOSbDIxb2qMP9Yz8f-BNJT9QlLFvI5u45gQnuWSmmo3t-EhDeEfCLGH90H6Oh4ALZxhboo1EiKG7kUPD0Ujpfu3e15a3ARfM9dCaWCAXJfSR_5aElUvGtOZgx-_yz8dSmItOo4SC_7kJ44IKkOqQjRUqzDhBDXkfoKZyYOQMqGIHwylagaltMwjiJLFH9Y4i6QdV5zDHfjEplWWZriocaNRG2tIw7gm5dfHefJCv5LGf2l9jT4zTvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگه بخوای از رهبرمون آقا سید مجتبی عیدی بگیری چی می‌گیری؟  @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/439876" target="_blank">📅 16:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
خبرنگار شبکۀ فاکس‌نیوز: آژیرهای خطر در شمال اسرائیل درپی حملات راکتی و پهپادی حزب‌الله به‌صدا در آمدند.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/439875" target="_blank">📅 16:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5e069b42.mp4?token=Y_lmZYtecQOSXIxtirolr7ikpDsSahxUeNqiZvHeysqcYrO4EkACj-PFdhARom95GI3XdalByoNubKNdPWKWK9CwBq2wNq-QsWt-F2gGuhnG-q1g4IpVLdbTr-CEiiQrKfyHmGQT9Fht1idNjBY4VSp7b3kvshUoXANqWnu9rEscPoN_kc7KFw2lmXiZNv-8JBSJ3GiMZtHdorcsytHBf6ou1TNEtHeooqo_G4Ps4fnA3C2JfLqfKtypwipgUx4SoBkOu507qDxutYUSdESeJStju5oMWKr0ROe8SdScnUbLfBhAmSdWF4x0bEts3YNNkw_sqAdbENor4YY0I96arw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5e069b42.mp4?token=Y_lmZYtecQOSXIxtirolr7ikpDsSahxUeNqiZvHeysqcYrO4EkACj-PFdhARom95GI3XdalByoNubKNdPWKWK9CwBq2wNq-QsWt-F2gGuhnG-q1g4IpVLdbTr-CEiiQrKfyHmGQT9Fht1idNjBY4VSp7b3kvshUoXANqWnu9rEscPoN_kc7KFw2lmXiZNv-8JBSJ3GiMZtHdorcsytHBf6ou1TNEtHeooqo_G4Ps4fnA3C2JfLqfKtypwipgUx4SoBkOu507qDxutYUSdESeJStju5oMWKr0ROe8SdScnUbLfBhAmSdWF4x0bEts3YNNkw_sqAdbENor4YY0I96arw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا حالا از سید عیدی گرفتی؟  @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/439874" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439872">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0631d4a758.mp4?token=NOuVyAjML2TsdHmfg-R9AhpWQ5XPkBcu_PuRtc9twHo-OYCB--BxmeO8n3KeKZ4viaf0kH20KUFWZpZlROXnZePE-cg3Hff8Ym7wSpweG5sIUB0JMAnMysjxT8yvzdvbkYQFOSwuyHbGSv5cmKAgi-VIPNuPoddhQv1c8BYbSehEswSOP6LHia04rdJ0bppXXLPfqEtKnBfza4xk1lzB1Bk6SYKako10kmx6_eUJIrfUBbP2JOzXLRQyTYKSh14rTZuJFd6vlKU1ohTkGfJHIvcZlfotzhrowBLC9j4Fx7ofqsgusCzX4dybheYpQ5pSkz3jjJM7Larq8xrX8f3c0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0631d4a758.mp4?token=NOuVyAjML2TsdHmfg-R9AhpWQ5XPkBcu_PuRtc9twHo-OYCB--BxmeO8n3KeKZ4viaf0kH20KUFWZpZlROXnZePE-cg3Hff8Ym7wSpweG5sIUB0JMAnMysjxT8yvzdvbkYQFOSwuyHbGSv5cmKAgi-VIPNuPoddhQv1c8BYbSehEswSOP6LHia04rdJ0bppXXLPfqEtKnBfza4xk1lzB1Bk6SYKako10kmx6_eUJIrfUBbP2JOzXLRQyTYKSh14rTZuJFd6vlKU1ohTkGfJHIvcZlfotzhrowBLC9j4Fx7ofqsgusCzX4dybheYpQ5pSkz3jjJM7Larq8xrX8f3c0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حنظله مدعی شد: مدیر ارشد موساد در عملیات بمب‌گذاری به هلاکت رسید
🔹
گروه هکری «حنظله»: یکی از مدیران ارشد «واحد نفوذ جدید» موساد در بخش مرتبط با پرونده ایران، در جریان انفجار یک بمب کارگذاری‌شده در خودروی شخصی‌اش به هلاکت رسیده است.
🔹
این عملیات پس از ماه‌ها رصد اطلاعاتی، تعقیب و مراقبت مستمر به اجرا درآمده است.
🔹
آیا دستگاه‌های امنیتی رژیم صهیونیستی جرأت بیان حقیقت را خواهند داشت یا همچنان به انکار ادامه می‌دهند؟
🔹
حتی افرادی که تحت شدیدترین تدابیر حفاظتی و امنیتی قرار دارند نیز در سرزمین‌های اشغالی از دسترس مقاومت مصون نیستند.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/439872" target="_blank">📅 16:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439871">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64842bfe2c.mp4?token=VTecwrWTviBx1QoQyJyOvsFS4a2Ql_TDJomaYJlVAxjjAzgGI-SDZC_gtBNiELDoXt6GENmbMGqy3v4pU83Ahr1GkjIf3tpO_IE_VEwW4FlDy4SK3D1B166mHFIRbrL8ix1zWWNc6s3W4yU4vjicQHjbu2aVU1QiCehcBPBgMC9gaGsaY6VJVHQxPPqcSYmZu3gYS8IK-23ijd8h_cDRyvKESiSF2r6y0YdKSVOx9m8T0g7wnr0KMWvXOFVXHTxwWa4F-jSLR-dk91jW563vxINBPLbXrQrCYd3wICtmsS6qsC0A-Nagwk9-Ta_cUQoPUpes7c19cuvD2b0Td5c85Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64842bfe2c.mp4?token=VTecwrWTviBx1QoQyJyOvsFS4a2Ql_TDJomaYJlVAxjjAzgGI-SDZC_gtBNiELDoXt6GENmbMGqy3v4pU83Ahr1GkjIf3tpO_IE_VEwW4FlDy4SK3D1B166mHFIRbrL8ix1zWWNc6s3W4yU4vjicQHjbu2aVU1QiCehcBPBgMC9gaGsaY6VJVHQxPPqcSYmZu3gYS8IK-23ijd8h_cDRyvKESiSF2r6y0YdKSVOx9m8T0g7wnr0KMWvXOFVXHTxwWa4F-jSLR-dk91jW563vxINBPLbXrQrCYd3wICtmsS6qsC0A-Nagwk9-Ta_cUQoPUpes7c19cuvD2b0Td5c85Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دوست‌ دارید از رهبر انقلاب که سید هستند چه چیزی عیدی بگیرید؟  @Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/439871" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439870">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌ یوسفی: افزایش پلکانی حقوق، هفتۀ آینده پیگیری می‌شود
🔹
عضو کمیسیون عمران مجلس: اجرای کامل مرحلۀ سوم متناسب‌سازی حقوق بازنشستگان  و افزایش پلکانی معکوس ۲۱ تا ۴۳ درصدی برای شاغلان و بازنشستگان که در برخی صندوق‌ها و وزارتخانه‌ها اعمال نشده، هفتۀ آینده پیگیری…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/439870" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439869">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef46a9d7.mp4?token=Rpx8J1iTOWu8JpVuNxXJW7Yy8qEFItpEv1r3jF8OkeW1_br8iTNNsr63nOF_Mt4G7JAhaA6vubreGFYrMqoKrEuSGzeyDFa5TExP0sYlEzbUHr6IcYJvY6Ov1RnG_ngo-i5WpcNjwhHf4zrp7yCy5hINfZBOJ_R09EIXub42Kw6v-CCJgNdowF8gRY3hhyobHKrMTaCD5iT0VK12qxsLXgDX5G5CXwkhfu6PkxSmwXIbj0XPJLzrFn6DFAvz8bhTyn_Md8iHjiW-d5A2aNwc6glBtrGutLWMAqDYuDEz512i0t0_mvItRbUt6ZECufwCSfZFbjOpe9kBHbct-U9uog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef46a9d7.mp4?token=Rpx8J1iTOWu8JpVuNxXJW7Yy8qEFItpEv1r3jF8OkeW1_br8iTNNsr63nOF_Mt4G7JAhaA6vubreGFYrMqoKrEuSGzeyDFa5TExP0sYlEzbUHr6IcYJvY6Ov1RnG_ngo-i5WpcNjwhHf4zrp7yCy5hINfZBOJ_R09EIXub42Kw6v-CCJgNdowF8gRY3hhyobHKrMTaCD5iT0VK12qxsLXgDX5G5CXwkhfu6PkxSmwXIbj0XPJLzrFn6DFAvz8bhTyn_Md8iHjiW-d5A2aNwc6glBtrGutLWMAqDYuDEz512i0t0_mvItRbUt6ZECufwCSfZFbjOpe9kBHbct-U9uog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📸
ساعات اولیۀ مهمانی ۱۰ کیلومتری  عکس: محمدمهدی دهقانی  @farsimages</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/439869" target="_blank">📅 16:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439868">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اینکه خلع سلاح مقاومت شرط اصلی توافق دولت لبنان با صهیونیست‌ها باشد، به معنای نابودی قدرت لبنان و تهدید موجودیت مردمی است که در برابر اشغالگری ایستاده‌اند.
🔹
نتیجه مذاکرات مستقیم دولت لبنان با صهیونیست‌ها از نظر ما بیهوده، تحقیرآمیز و…</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/439868" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439867">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: قاتلان پیامبران در سرزمین ما آرام نخواهند گرفت
🔹
ما با متجاوزان خواهیم جنگید تا آن‌ها را از سرزمین خود بیرون کنیم و تجاوزشان را متوقف سازیم. @Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/439867" target="_blank">📅 16:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439860">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_4Ukf2jaBbsKdzVYix2EsDsQj2Zn358t8or-nWgQKg_du1bGwfP-Qpc4P4zO0A35KlmyBYvoDPqgXQQ8vGIAqTxgl2HwLx_dBU21lUi78n17vghwYQix7MElLhQLs_fYbYa9C1cyMAiZ65T_cTyZrNhH-nfGRBdQ0I2NdFLqkog--skBUvyBZO9a0Uz1zK5PZp5ipDs3_XYNd1_leYxaUWRCKC_CcUQjyNcoeqyPEi2e52d-STQFrc8NtCsfu9xE1OdvnrrZDpajAptDS4dsfMBfsLw0LYYMvbwnu2nqB-qQPcgX5BtrQ2CSRfh0pAVA-a9-Fn5gZMnHDUmct7IAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rl_KBmDgHL8umt7vgvKu05EZBRTdj_NVUisnjb6S8PQE_2Cqx98Yf4G3gHP0y80SJb6VuaLnv4sUOIrt_Fz6GvaZO6LtYs5pICuEt4v-zpgBxs_KV-y9O5prCew1mxeWQx6tdcAle238Ugp6UiSMGvLz1Rd1V5jTAdZo_lQahVcO3kXM90Z_XKIpeCwqdzv2ES2UPEQtn2NbcAlbfcp_ZIZvt76-hoBzH5wmDhWXnMzxQsDdTyVFqg_911DxZgBX56A4MS-EJpXh4TOiNIDbcLeRdoZC-GkJ7SO59lKCmWqs0fhxH42jAcsbgk0EuFABuJxA4kAZFNhE5uajvylTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zs-ActBU4otSR5XGVsvw8J0sglUYH06Lo8S6ux5zpvwSqM8Tn-LQ79IMew6RsgbrnKlqm57RVQs2n1CgqCMridko64dfD_dN0YjUyef4ePEXA4U_GKM7V-_jwhM94ShXkGJpByp269IMD3aM94ctMN7Q46ws7HMVnyR3ZliwaAsEbGdX84yoQKEQcbYBviWhDm4u59gQBWomSy6NPcX5tb6_D6j4sn7KXj-uArYWiOWm2IXTyTJMglU8Cl2Dr-Ubtfvtlz3EFZIfMqg_voC1K6cGFS54OdcMftitQFIJpZ9Px4LYzwn4umw9f0_EyXv8vadaoNS7o6RwzmzG1ESldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNdXJ0YSOLLX8v8YweXdBEQaMybOPAGg5WlGqmaeT6CXMo_z4x7tRm4GYBISzy0-S0fz2XqeJuwzVG0731m4BK1_mIme_wG9WUaWIKdYW4To2HH65dZpHwopZyq7rgWJ5z7ODvIQIM9P3HIjFOEMLMfFOCvBAcWeyrxvF8W4a6o2LXF_z721xxBkiEiT1qCra2bhTkn9uS2sSqs0U29U6A-MTPgjpQ08gzSGWYU0o2QnK12MJ7oHV8QXFGOYH9HaUe-nmV4J4ZkP-ed0zauUlX9lvIPK36WSgZ3NcZZB0KioevhTvMwI3jW2BRri79tcOoLMlp-1bpBPWGuzPHxKAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nlifdvl11um1aYKvprUimk1EJgnfw70vGwTMjOR2KKjTcMQt2fs-gRYTuP7gx8e4xSXjhlhOsjoskaJxbimMtiVnu-TrWG9j61Vlq9mFe3lDPcr3eUO36tg1gXrNrTSaZG9w7N_AhuclUxe0Dory_9oyg_DOyNzFUNehCKywluIF_t0X2ZgQrtyggmwBFPyWalNHLZItihLEYYU9Nci-iAHJimCbYC_K7TX_M0ta4NbapUitTHe4WPKwlHGmH_AHV3J9pvXVYScJJTarY-CRdhs-fRqPGTSL2ojAM_bq4zoac0pb57VyIaUQcjunOOoj9gyYO79hqO6JDwkMBIjBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahRevkSZLM4WrHXh9e6yYrjjP0H_QqETUjAab733fVVBqGxDJeLniADPwvbTg_AfeyNwQnqIrBH1KU8YmvQf42uv_AR2ghjkze9hPseHOXQxfNdObJezLEAN3dtDzz0aTSyFhEVEW3yWhg70vJ6dXnMx_lTwAQi0fohI46jb-lk30osj0SA09iic9KF0kel8KzfJ18oMY-p0JOX5VBR6-CdBLxGv3jGZsuWUgtCX32xrgXIBhu22TEkIlNjqIk6CscnOJ3YCcf8IS3NGV5ffzlqgOyJbE6GzgGnniZRrUnh3YQnWcgxbGXnkGCGMpsVBhamzDZidK_BNmFrryBjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9Wuc3MdZKfhQouhKGcK1d65xpO6mQQnb8vv17_ruGqDV_QGua4yFnK7wCiI5kv-AKxAUsjQXYZLbWnqYEF9I31opERIlgM-FCoEnozpO7Yi7uK4dw96VsKQQtkVJwr99vRyOtN1kKtGYS9t1bC9n4zFfcMmfe_9GQ-4k31KM6k5a0OnaeKJ3OUXPJz8Inhk_fuodpV8HVCK8spHv9l3_I3TW200P9Ctn49asdj1Mls9U1Ebta7aa-8Lyhe43aGMlxqi_mtMAM1fErhRQPLKIZJV964zwhDs0XVTOtLExRHiKu5qRa4q4ofq42wTWl0xLuHEgdS8kVCsvPOqglaGTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
ساعات اولیۀ مهمانی ۱۰ کیلومتری
عکس:
محمدمهدی دهقانی
@farsimages</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/439860" target="_blank">📅 16:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439859">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: زمانی که روستاهای ما امنیت نداشته باشند و بمباران و تخریب شوند و مردم ما کشته شوند، شهرک‌های صهیونیستی نیز امنیت نخواهند داشت
🔸
آن‌ها صلابت و شدت عمل ما را خواهند دید. @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/439859" target="_blank">📅 15:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439858">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: تا زمانی که حملات دشمن ادامه دارد، با تمام توان با آن مقابله خواهیم کرد و هرجا که تصمیم بگیریم و بتوانیم، دشمن را هدف قرار می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/439858" target="_blank">📅 15:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439857">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما به هیچ‌کس تعهدی مبنی بر عدم مقاومت در برابر تجاوز و پاسخ ندادن به حملات دشمن اسرائیلی نداده‌ایم
🔹
تا زمانی که اشغالگری وجود دارد، مقاومت ادامه دارد. @Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/439857" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439856">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: از ایران سپاسگزاریم که با وجود چالش‌های بزرگ خود، به ما برای بازپس‌گیری سرزمین و حق‌مان در مواجهه با تجاوزات اسرائیل و آمریکا کمک می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/439856" target="_blank">📅 15:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439855">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: مقاومت در لبنان از مکتب و اندیشه امام خمینی برای آزادسازی سرزمینش از دست دشمن غاصب در منطقه الهام گرفت
🔹
ما برای سرزمین و ملت خود و از روی طاعت از پروردگارمان می‌جنگیم تا بنده هیچ‌کس نباشیم و نسل‌های ما در میهن خود در کنار هم‌وطنانشان مستقل…</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/439855" target="_blank">📅 15:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439854">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: مقاومت در لبنان از مکتب و اندیشه امام خمینی برای آزادسازی سرزمینش از دست دشمن غاصب در منطقه الهام گرفت
🔹
ما برای سرزمین و ملت خود و از روی طاعت از پروردگارمان می‌جنگیم تا بنده هیچ‌کس نباشیم و نسل‌های ما در میهن خود در کنار هم‌وطنانشان مستقل زندگی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/439854" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439853">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e04083cc32.mp4?token=tP67_gGjF3Lf1gze9GZPHFEwfYoLomGqsxaofNUlNXLXgHybdwBQrcQG_CceKS5LGucruVa42jgDg53S_FIAngOwk9tJ8LlO4NZXYrlYMBAe3qXqa1AYZ8aeUch0Gq4RDOYr_n6L9JRJjC-HYkzEJO2IwCkkT9ulei8ttWO2DSH6yfNI3a8NunpFtL6YOpVeG5Xs5F9w5QQ5XKDkkOcIA8RaO6aonj5cMwtN2djcKuo9_Sy_iJFisMB-Agds3YmOCJv45uquWm0eKYM85j0Yjz9BUhOvO_tBR3HdDVSj3mhijB5CFZR6XWuthGrQ5WeBlipZh4qZAQBV0HShoJoCZmdumCAhXMPPUsaoL21jWp_LbGabEglVLuO--ojIBB4hhZ0EAoZytg1bSsW3loWlNvKxz3-mwLOcj9PN42mZt7Xex4HQva9d3XD3yRPkH-rBaPa4vgTRbQ7NZ3pm3x3X1RWf9x47sIrZY18ovp0K2Rh88c8GdXoa9rEjuhSba-Vmg5LBAlypWTr-0FpF0qxkJ48gx9rfXNjGpsQGHDyDtAyqdbZY_fDl4heE4-Du-Z_imr8UjORV0OB9UOVdDOxXivY9g9eoAxRdWtU-rFIGL3lYV8AlV61CQv0RF4nesoP1YjdGHzo8g6TOGlDGk343_PiwUU2ysnK7hcQR4UiPJ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e04083cc32.mp4?token=tP67_gGjF3Lf1gze9GZPHFEwfYoLomGqsxaofNUlNXLXgHybdwBQrcQG_CceKS5LGucruVa42jgDg53S_FIAngOwk9tJ8LlO4NZXYrlYMBAe3qXqa1AYZ8aeUch0Gq4RDOYr_n6L9JRJjC-HYkzEJO2IwCkkT9ulei8ttWO2DSH6yfNI3a8NunpFtL6YOpVeG5Xs5F9w5QQ5XKDkkOcIA8RaO6aonj5cMwtN2djcKuo9_Sy_iJFisMB-Agds3YmOCJv45uquWm0eKYM85j0Yjz9BUhOvO_tBR3HdDVSj3mhijB5CFZR6XWuthGrQ5WeBlipZh4qZAQBV0HShoJoCZmdumCAhXMPPUsaoL21jWp_LbGabEglVLuO--ojIBB4hhZ0EAoZytg1bSsW3loWlNvKxz3-mwLOcj9PN42mZt7Xex4HQva9d3XD3yRPkH-rBaPa4vgTRbQ7NZ3pm3x3X1RWf9x47sIrZY18ovp0K2Rh88c8GdXoa9rEjuhSba-Vmg5LBAlypWTr-0FpF0qxkJ48gx9rfXNjGpsQGHDyDtAyqdbZY_fDl4heE4-Du-Z_imr8UjORV0OB9UOVdDOxXivY9g9eoAxRdWtU-rFIGL3lYV8AlV61CQv0RF4nesoP1YjdGHzo8g6TOGlDGk343_PiwUU2ysnK7hcQR4UiPJ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ ماهشهری‌ها در عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/439853" target="_blank">📅 15:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8abebd4f70.mp4?token=dJ4lzttERoyuW9CeC-H9fjslKmvR--JKmVjG9sU0JxQzp6J5qrIwRHZsytF8Cglb7M6mZKF-dv9jjKaaoD6kB2v1S87Hxu7vxc25EBuMzarbD3396PtH-8nUf7d6Mv3ysEBWBvj9cSPEVEPRjMYjmHs4eiNVnmASeHUnyOSFtE7Sd-XdMDrCPzUHmA6pFMA8fbBouuRjL2mGFwx4fTEx8OVJlFZ-r_vFUcZ4nr8azAvoZ4Swxzv0sqhLQFnR4Ifv96wOR9gHxtt8zCg1JPdQyX7WDh9m10SAHW1bww1VFnEWd8Eh6-QElAY5Cnq8o1vQ2WFlxoqgVasz8UjxOdAlCoPS3-f_2w1BmskrCKiLvpwKgXr7c5WP6a-CmavfD5_VFugYsSxvip0b-WVo9hpyOVSuF40DpJ8iBAj2S4LS9TvqE6UMmpFk2o03Dxfk5JE3A79Pt7YvH7fYlz2PIwDhhKJlp-mRzyDQuSPCGws_rgW96t8GET15bML2l1FnJOhsTx-UQqYMpRbwWOqYDqWjFPJQFDgz7UqWKzihzS4Ge60OYP0cv_8gnfeCMX4WDVXom-vHLIaMUcuD5r8YQeBJq6CHd5qn7Ge4xOeMe8wf5uOfuvtbqydtdgDRXyW-LA7ZAVpQkuc-217KPQ8T01ps39vsRKti0nLY2T1EXOk37qM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8abebd4f70.mp4?token=dJ4lzttERoyuW9CeC-H9fjslKmvR--JKmVjG9sU0JxQzp6J5qrIwRHZsytF8Cglb7M6mZKF-dv9jjKaaoD6kB2v1S87Hxu7vxc25EBuMzarbD3396PtH-8nUf7d6Mv3ysEBWBvj9cSPEVEPRjMYjmHs4eiNVnmASeHUnyOSFtE7Sd-XdMDrCPzUHmA6pFMA8fbBouuRjL2mGFwx4fTEx8OVJlFZ-r_vFUcZ4nr8azAvoZ4Swxzv0sqhLQFnR4Ifv96wOR9gHxtt8zCg1JPdQyX7WDh9m10SAHW1bww1VFnEWd8Eh6-QElAY5Cnq8o1vQ2WFlxoqgVasz8UjxOdAlCoPS3-f_2w1BmskrCKiLvpwKgXr7c5WP6a-CmavfD5_VFugYsSxvip0b-WVo9hpyOVSuF40DpJ8iBAj2S4LS9TvqE6UMmpFk2o03Dxfk5JE3A79Pt7YvH7fYlz2PIwDhhKJlp-mRzyDQuSPCGws_rgW96t8GET15bML2l1FnJOhsTx-UQqYMpRbwWOqYDqWjFPJQFDgz7UqWKzihzS4Ge60OYP0cv_8gnfeCMX4WDVXom-vHLIaMUcuD5r8YQeBJq6CHd5qn7Ge4xOeMe8wf5uOfuvtbqydtdgDRXyW-LA7ZAVpQkuc-217KPQ8T01ps39vsRKti0nLY2T1EXOk37qM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابَرپرچم‌های بیعت با ولایت در مسیر میهمانی ده کیلومتری غدیر تهران  @Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/439852" target="_blank">📅 15:22 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
