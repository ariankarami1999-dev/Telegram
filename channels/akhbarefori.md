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
<img src="https://cdn4.telesco.pe/file/FgUkLoYSNrrEMpnQmIh38a6wND7OXXNxnBcjHY1ff0ky9HFvZ3y6dXyrlKCI3Tcq5GX0KRumJZ1lpZcszQM9LrmfxJV23b4Q5Gp71IgGFhEFIDkx9Gv8FU7yqsOY5aUk0xgGP4mWhCUoMNwI4ex0GWowMTmEWPkmA3_-hTB0RyJDqD2jUAAHDkhxBhT7Zjyx8aNDhaVeq2UU54mMqSOWKg4_NF0o_v_2cD3otR4vU2bWR7guo1766zGr0iIg3Sxe5kwuf_VvAUeLvW1K2XBjGIRtoAPFWXAkaCANW6YlcesESPIz9WWJN3LRq-x5sJCoUpcNshNJtkFLARfacFnL9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.99M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-692030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ترامپ درباره ایران: آمریکا و ایران حتماً مسئله را حل خواهند کرد. ما به هر شکل ممکن این کار را انجام می‌دهیم. این اتفاق خواهد افتاد
🔹
این کار به‌سرعت انجام خواهد شد. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/692030" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
التماس ترامپ دیوانه از سایر کشورها برای منزوی کردن ایران
🔹
من از تمام کشورها می‌خواهم که به ما بپیوندند تا ایران را به طور کامل از نظر اقتصادی منزوی کنیم، تا زمانی که از حملات خود علیه کشتی‌های تجاری دست بردارد، از برنامه‌های هسته‌ای خود منصرف شود و از…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/692029" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای ترامپ در مجمع عمومی سازمان ملل: من در مورد انتخابات مطلقاً هیچ اعتباری برای آن قائل نبودم و نخواهم بود. این موضوع حتی به ذهن من هم خطور نمی‌کند
🔹
تنها چیزی که برای من اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست پیدا نکند.  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/692028" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای ترامپ در مجمع عمومی سازمان ملل: من در مورد انتخابات مطلقاً هیچ اعتباری برای آن قائل نبودم و نخواهم بود. این موضوع حتی به ذهن من هم خطور نمی‌کند
🔹
تنها چیزی که برای من اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/692027" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692025">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ترامپ: فکر می‌کنم درست بعد از انتخابات میان‌دوره‌ای با ایران به توافق خواهیم رسید
🔹
من باید در مورد ایران تصمیم بزرگی بگیرم. آیا با آنها معامله‌ای می‌کنیم که به آنها اجازه دهد به کشوری بسیار بزرگتر تبدیل شوند، یا آنها را کاملاً نابود می‌کنم؟ #Devil
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/692025" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692024">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
دونالد ترامپ: ایرانی ها موشکی ساخته بودند که قادر بود اروپا را هدف قرار دهد و به آن بسیار افتخار می‌کردند؛ امیدوارم اروپایی‌ها این موضوع را درک کنند
🔹
هدف ایران این بود که در پشت سپر موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند. #Devil
🇮🇷
…</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/692024" target="_blank">📅 18:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdsT038y706EgDPxRHJEffL4u9Y4je0CyR1lLtHQaUxKJ2fcoBV1PeQDy6bxJGiU4Lf827ucrdqfkZyq6y90gfhUH53mWdvTsj0xEIvshpXsdNuOV7XvPoiZ5z51b6_cc1lSdmkM8TLz45TP2cnlRVgq13G_yKJJHEmP4uUhEzOqnukZLJuZzfKOks_yLu_lIiOfWj1RZh2C5_lKxx6O4wf8O66D2qhmozbPLJZRu_pXyhJ6F-WkVH0WBFAG6t8M0Fi2Zyi6jm02NZ4uXsokOBfz9yiimqwfbaED_W4Hg9WIY2YXuDkGdY6K1Ng-i40pZAEwdDkl8DlgnaNHIbxKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دکتر «علی محمد خانکی» به عنوان معاون مالی و امور شرکت های بانک شهر منصوب شد
⬅️
با صدور حکمی از سوی دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر؛ «علی محمد خانکی» به عنوان معاون مالی و امور شرکت های این بانک منصوب شد.
⬅️
به گزارش روابط عمومی بانک شهر ، دکتر «علی محمد خانکی» طی مراسمی با حضور دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر و جمعی از اعضای هیات مدیره، معاونان و مدیران ارشد؛ به عنوان معاون مالی و امور شرکت های این بانک معرفی شد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/692023" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/692022" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879fa5c0b0.mp4?token=OwI0vwp8zQVb6nXLGUI7P86PKQuYsJH-Pyl6Pb43gALsy89FYr4MU9PfB3Q0XA-SWm8KfS6AIiKvS_-VLrsohPSJ0EW0cybazKk4ttP1RCkDKssjXFQjdCIY8aYFctpew9tGgYj-SBz4BhKWS3Xl0lXK_OGMmPUChirMV6iV8Bqid9O2zCON0JHcVpbddS2HXkjaMMs25B6Llq00Ab4RVR6Upi09AO8rcNkJnRhIv3uqH2XWSsSaTNcU9eY04Ff9PY0TOOeJAsN8sU3yc5ljas7jpldt-9fYGaFm9_5hla336JaNxLO8MAEJ8eFOEmLf2S1vCY3cCNWhyCG_6Ud1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879fa5c0b0.mp4?token=OwI0vwp8zQVb6nXLGUI7P86PKQuYsJH-Pyl6Pb43gALsy89FYr4MU9PfB3Q0XA-SWm8KfS6AIiKvS_-VLrsohPSJ0EW0cybazKk4ttP1RCkDKssjXFQjdCIY8aYFctpew9tGgYj-SBz4BhKWS3Xl0lXK_OGMmPUChirMV6iV8Bqid9O2zCON0JHcVpbddS2HXkjaMMs25B6Llq00Ab4RVR6Upi09AO8rcNkJnRhIv3uqH2XWSsSaTNcU9eY04Ff9PY0TOOeJAsN8sU3yc5ljas7jpldt-9fYGaFm9_5hla336JaNxLO8MAEJ8eFOEmLf2S1vCY3cCNWhyCG_6Ud1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام:
هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/692021" target="_blank">📅 18:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-GJthSlUsU7p9Qt69pNKNnrlLMxqbigTdm57B5lEaU_Pota1JXgDrDlsj2b1Dzju3kyfPmbQERXqAZ9Mgy4Zi5QF6iCksCRmE9VVUZp3PG4w6vWc5Zv6oST65b8mRh1cYZGg2M6t8eX2_HWq50fYZUqXkI3S_iBnTEc9crnXQATQKjcF9sOLQ7SkeoReIRXtHoOit9e4g267dEXO_8_aXfjjyBFSHmnyQEc2xLsczZgggUOmZyvrMJcvfd2qtprSKNLBMx4wRGGVSx1fhxgw224O1MBwyyxA7bkw3lfjbVVnKi_1eroKx9uEBk9OqYAZt1W1mq9U2ZXdIx9SEv6PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برتری صنعت داروسازی ایران در منطقه
🔹
۱۴۰ کارخانه در ایران محصولات نهایی دارویی و ۸۰ کارخانه مواد اولیه دارو تولید می‌کنند و ایران در تولید دارو رتبه نخست غرب آسیا را دارد.
🔹
حدود ۴۰۰ کارخانه نیز در زمینه تولید محصولات جانبی و بسته‌بندی دارویی فعالیت می‌کنند.
@amarfact</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/692019" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
معلّمان، شایسته‌اند که مورد تکریم همگان باشند
🔹
ما همه وامدار معلّمان خود در هر مقطعی از دورۀ‌ تحصیلی هستیم. این قشر عزیز و محبوب که اغلب با خالص‌ترین عواطف شاگردان‌شان مواجه می‌شوند، شایستۀ آن هستند که در مجامع و زمان‌های مختلف مورد تکریم همگان باشند.
🔹
مناعت و قناعتی که نوعاً در ایشان مشاهده می‌شود، مسئولین امر را نسبت به وضع فعلی
#معیشت
ایشان قانع نمی‌سازد، و ان‌شاءالله با برنامه‌ریزی حکیمانه، برای بهبود آن تلاش مؤثری به‌عمل خواهند آورد؛ خصوصاً اینکه این مقوله فراتر از انجام وظیفه‌ای قانونی، امری است که از دل برمی‌خیزد.
✍
بخشی از پیام رهبر معظّم انقلاب به ‌مناسبت بازگشایی مدارس و دانشگاه‌ها | ۳۱/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/692018" target="_blank">📅 18:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692016">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oovb-LaEUfjpVg80hhPvjgORzZXaawmwIX00GRhYHBoZXKs7VvpJRFi1TKn7kn0FZYMFFjAEoPSWnZAlQfb-rF3V9z-3DSM8u39mm0q7IVyG3cKIVdfipfwIKlxfrgt47ApFQNf5dTW6OlUGm5J16YETdcM7REZL4Pmng3VUAygfY6QngcBxOKVuiZjakXaUQhqq5S2kKn4gUYAVso_I66Oc7Ei4PHrr0UxyRfhQl9xX3d8geHQN-_tWyoLiS5bc-xLErbJ1gyisfqtnhqNS_ch5vt8ovMNgVzX_hPNLC55BWqbUMGaftkZd-Pj61qEenm4jEXPPwzCnmcIHZr_Fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آستانه سال تحصیلی جدید یاد دانش‌آموزان شهیدمان را گرامی می‌داریم
🔹
امسال روزهای خاطره‌ساز ابتدای سال تحصیلی، برای ما غمی از فراق فرزندان سفرکرده‌مان را تازه می‌سازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/692016" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692013">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
♦️
رهبر انقلاب: فتح قلّه‌های پیشرفت، مأموریت تاریخیِ دانش‌آموزان و دانشجویان است
🔹
مسئولیّت امروز دانش‌آموزان و دانشجویان، سعی در مجهّز شدن به علم و تقوا، امید و اخلاق، و دانایی و توانایی و زدودن پرده‌های جهل و تاریکی است تا آنگاه که با شکستن مرزهای دانش…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/692013" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692011">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
♦️
رهبر انقلاب: فتح قلّه‌های پیشرفت، مأموریت تاریخیِ دانش‌آموزان و دانشجویان است
🔹
مسئولیّت امروز دانش‌آموزان و دانشجویان، سعی در مجهّز شدن به علم و تقوا، امید و اخلاق، و دانایی و توانایی و زدودن پرده‌های جهل و تاریکی است تا آنگاه که با شکستن مرزهای دانش و فتح قلّه‌های پیشرفت‌سازِ آن، مأموریت تاریخی خود در جهت اعتلاء ایران اسلامی را به انجام برسانند.
🔹
این مهم در جایی صورت می‌گیرد که خانۀ دوّم ایشان بشمار می‌آید. از این‌رو به این عزیزان عرض می‌کنم که لازم است همواره از حریم‌های آن به بهترین شکل صیانت نمایید و با ارتقاء هر چه بیشتر سطح آگاهی و بینش و تعالی رفتارها و منش‌هایتان، آن را کانون پیشرفتگی وطن خود بنمایید.
🔹
از فرصت حضور چند ساله در این مأمن دانش و ادب و نشاط و امید برای خودافزاییِ هر چه بیشتر بهره بگیرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/692011" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEgLtnQBpm9f7-pO_NRMQjaM_45LuehPB0TDYHpElsoxxWn8W9WhqnDMWNMnLXMWBn7aQief41IWp77fMt8ZCejVPbON7RApP92PhjvcwjUNkD9LU1OhYuLgf_oKXQc6T2SwLV6WQtyFHpCTfxAZSzb81UAVByGDPlTjPqryNDnezOCwOw86TEsTGZhR25UJHSYZJPftbmsxEiCjLbGfySHAuSxFw43O47V7RvZZDfCizbYIp4OiJek678xF7NRS3SSGRNwKIjmSP3E-JmhSndZFhILg6UFSv-djtCkoJYxhwRPPwMJRcQVZZj1mOA62OusRFPP7t0N5wOHU76qLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه بیش از ۴۰ نماینده به عارف برای بازنگری در ممنوعیت واردات لوازم خانگی
🔹
عضو کمیسیون اجتماعی مجلس، از تهیه نامه‌ای با امضای بیش از ۴۰ نماینده خطاب به محمدرضا عارف معاون اول رئیس‌جمهور خبر داد و گفت: نمایندگان خواستار بازنگری در ممنوعیت واردات چهار قلم لوازم خانگی از مسیرهای قانونی تجارت مرزی هستند.
🔹
احمد بیگدلی تأکید کرد: پیشنهاد نمایندگان، جایگزینی ممنوعیت مطلق با واردات محدود، کنترل‌شده و قابل رهگیری است؛ به‌گونه‌ای که واردات با سقف مشخص، ثبت و رهگیری کالا، رعایت استانداردها و پرداخت حقوق و عوارض قانونی انجام شود.
🔹
بیگدلی گفت: در این نامه از معاون اول رئیس‌جمهور خواسته شده است موضوع با مشارکت وزارت صمت، وزارت اقتصاد، وزارت کشور، گمرک و کمیسیون‌های تخصصی مجلس مجدداً بررسی و نحوه اعمال محدودیت واردات و حذف استثنائات تجارت مرزی مورد بازنگری قرار گیرد.
🔹
در بخشی از این نامه آمده است: حذف یا محدودسازی این اقلام در رویه‌های قانونی تجارت مرزی، ته‌لنجی و کولبری، نگرانی‌های جدی برای مرزنشینان، ملوانان، کولبران قانونی و فعالان اقتصادی این مناطق ایجاد کرده است./
ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/692010" target="_blank">📅 17:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای وزیر امورخارجه آمریکا: برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم
🔹
روبیو: فکر نمی‌کنم هیچ جلسه‌ای بین ترامپ و رئیس‌جمهور ایران برنامه‌ریزی شده باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/692009" target="_blank">📅 17:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7861846c96.mp4?token=Da6B4DiUPIkgnaHmRjw5FUIcisoD9FSE3VULXL-l6sffMOIYZefbgXx00Rwq1D4_XlVduxNSo7Yzb-HKeYmTDKF1yKpukIxMT8HXii9Po2zV0VFJuuJFbSXWfuKZJbHRfPKVZPTfZNs-ox6hhpy97hGTeTxfDYVTbBMKzBv88Yv-lILyebjYPYcP3vkSMHMDjrk-WVyYN5UoiBuFUqz8tW6LrhjnZ_LetsbsszZOIDMgI4Rx4kbGGirhjxk6VxFsJBYNGiAGVdibARvT0K0J7yab04O1M-3lt_rQ0hQrTAnOxNYDG-3moxYGGHpISlkyiGuPCY00C6KfdUVYVbowig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7861846c96.mp4?token=Da6B4DiUPIkgnaHmRjw5FUIcisoD9FSE3VULXL-l6sffMOIYZefbgXx00Rwq1D4_XlVduxNSo7Yzb-HKeYmTDKF1yKpukIxMT8HXii9Po2zV0VFJuuJFbSXWfuKZJbHRfPKVZPTfZNs-ox6hhpy97hGTeTxfDYVTbBMKzBv88Yv-lILyebjYPYcP3vkSMHMDjrk-WVyYN5UoiBuFUqz8tW6LrhjnZ_LetsbsszZOIDMgI4Rx4kbGGirhjxk6VxFsJBYNGiAGVdibARvT0K0J7yab04O1M-3lt_rQ0hQrTAnOxNYDG-3moxYGGHpISlkyiGuPCY00C6KfdUVYVbowig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ممدانی، شهردار نیویورک: نتانیاهو در صورت سفر به نیویورک برای شرکت در نشست‌های مجمع عمومی سازمان ملل باید بازداشت شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/692008" target="_blank">📅 17:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از دیپلمات‌ها: فرانسه با هماهنگی واشنگتن، تهیه پیش‌نویس قطعنامه‌ای را در مورد تشکیل یک مأموریت بین‌المللی برای احیای دریانوردی در تنگه هرمز آغاز کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/692007" target="_blank">📅 17:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
معاون سپاه: در طول ۴۰ روز جنگ، ۲۳ هزار اصابت و شلیک از طرف دشمن داشتیم که بیش از ۶۰ درصد آنها به مجموعه‌های نظامی، به‌ویژه تونل‌های موشکی و پهپادی، اصابت کرده
🔹
پایگاه موشکی داریم که در طول ۴۰ روز یک هزار اصابت به آن صورت گرفته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/692006" target="_blank">📅 17:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692004">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ممدانی، شهردار نیویورک: نتانیاهو در صورت سفر به نیویورک برای شرکت در نشست‌های مجمع عمومی سازمان ملل باید بازداشت شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/692004" target="_blank">📅 17:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691994">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTxshoYKEkYqydDakpG7yJXD_Xi25YkAjsmV5cdIwJlwXMyAYm1YPULZR0raNfxLoIOj7_0AqEPOKCzBoNZ7I4KYO04YlnKNtGVA4mz9An5PPRatctpaK8153v7ulkNLBCzZh0ubBMgdD6WUiTVAnjn3WESOTCM5PjQvbbw7jaO7_YzLj384lkRluqKH9dhoaIYTTa0HLLgUGeuNhMMiGROfzpPgWinBd_TbynwLZBoQr3yfC24X_rh1hXt7P7vt0iD9_0h1php65EGKGihsg9k41Uxc8zfGsDca_OB8awPJTVqS3NaErlSSSoJVkDLqhr5lsj3C20HKiIxJuvEGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d83XkxgI6h54r3PlvpQ1Tz7yRgn8VKiDbVkYan9F7gOXjxODN-a_AA_5mKDXu3jVM2rLLyekl8xTJRsoizvqEVPxW_yya5kpAeimv19bQ6XOu7nAmovpPr3YGddky93oaNnNq8RfqzAPfXX6ZOp82Twlvb-CChAANmGb_P8_t6Zt7gEE3p18o0Y7AjXK9MHNvn1tCVBEpQDggRcBx69iWJUUXYkqHKLN1QVNXR_nTSXVSdyEH_8MHh4POVRK6Y8p9DV3glu-fjma9udS1ZgXu00WKHmQNc3tQvv_XcZ6hGsjt4NqFcLxCumGG6EaFn2_p_AOZdrm3dbXBTj6I-NzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhg-Vz8_QL_Eo5KUEsX7zVoh_vo12huDUfPTEufkHpUJtLsqb03VkNwjpncqocg2fgFIxpSWOAX0SkDafrskLcFslPEC26rvIJo1EWJ-my0vll8-OIEMs7muUJ-NL6JCGw1r7xtFug1xmc4Ko9ZliS2qdLKkMDeMjyKe9jY2jhM85-Y7GTVEYb7Wnv1nACWmYszg0L4t_xkiFztM7nVSakUPK6fHLdSiXEjT0Diak9QEIRMVjDZduYXMPBKWSCtSPeI6Ukhaowqwef-MhJe56Wo3-DTC9pcKK8SUeE9xZdmUZ-dBR5KukoY6w4J0f4rHpUY0J_G-0ZjGVTfxL-SF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqU4QBwTgH5iIQFgdmyLsHyujEdAMUXCPHXXis_T8K7hUzEuiFIvvteYaF210kLrAHAL3SmDYse2xvRZL63ef2104lVxMZVRDn-tMY6irwBgKhghX-5ejbWgY4WQS_qnxKlXJA2a-N3ULdDUyKcakFUxDUHWOcCYvapH91KYszbd5Iz9nCbvJHtAtcP_5cEOhRKD8w3t4IQImKlpFt4gutuTs-dqaIWcdA2_SJ0QScEBdnEiwdR23-1VqZaSOpJX8jfr5o1SPlvy5U_09YKvd2qBlWRSyNykolPyUp4Jtr5saJTGqWsBVKl14cFfHmw0RKNb-Pn1kwhUiKoVgxk-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhSbHt3Hwlfissavey_jCuK0I9-Tkl0pv2KnWIfivCSUbdLwwPhA1mA-v1RZ-C5YUj04YhH_vdwwLW9DjtOcW8BxLD9Z4hjpcbvVUea9TgF8X23Hl6etpHzBt2_MpNZ3k0vSa0MUeTYcMqCdeyeJR9kCxmdX42S9NQyRiB_n6Ev7nGryhVYOHWt2mBTS2C9j0ARuOHppzEYpvWpZ68fmpiC5kY8JXunEFi4KXReBl3ujcsWy0MowwtLeVum73pPDYsG4hnMYqaAM90uKer7hq006qhUrEKHT_W18lxEPZ3C03K-K6BDgytD3WpKCpoaG8A96Wsd03rXdQ0c35lEVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-1B2lLnC8lPVgt0idexKTjFiRBwwGZjIAquJb71dTnbohcIxe1u4VScdDaOtTLUIKP9_Z079nvNcgTKInUa_46-anyo1V_eAqdCg4gtPHVc8Wtg7sPKOAuliZ5EFDjPyZlcCDVYV2nTK_6HBQtiKjqKDx3n8Me6Fas_Z3Co_q-GTLK2_drzs5FnmEyV0DmNGAEYCvWKxQ1lX-Ov_ddrxm5xb5WbedKdmUF7C-Zi1ipf-yn8XZIJZCM-YSHAYCj0KbNw0IbQgsqgtWxRhDrvIbDW_FNooO0uQCX46fpr7Fi0uCCwBkOGfTIfRraddU8QSpZyuAuLVZF3Nm2Be_Tl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sS-VDRZwlLasMU6GxJY65tMS3n5ZIbIIaERPY2yL4RxR2kwah_K3WGlm1dn9zSJh_8m2snnlESX_ai2lj7LM8N2Qy1vbXIs3h0bsXbgqFmIltI8GbcS5h2I9j6KkQ2qGumThAFQjRIJssg6Hg51jdY4FFxykUJYq2Spr06nKEUM8lRzqUX6qICZ90D1YTW0VCTNRNLAEPgMMIAeLWyNsMUTvt4E9hTiPB2Xyo0WzM-6RokVVozPwRqK9I_h3tER3Mz5ZVjIso_RYBQzT1HuuBhXGf0NI-IyciekaO_DdzlehcgeoOViv67SDvB7d86fb4uJzBVfXuPW45rKMYm07Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPJQsbcZs1kUA-Yg2YIgU4a4ARxpcg7nCMR1aqlB7ozM13tuofpQcxSjUPqhmvmA847YtM13jdY9oj77Qyasg_35SxFyhYz5d839X2mI6q2bqhUuokSWRszz2tGz_8nwMEUOUApG_lAW1r4XhWKzdXRuxNiwwpAc5_mU-WZERXyQgQEdrH2ea9MNI9CcHEjdhlB2cw_2hH2Zoj3jD4jG7o1g97aHx4G94O_pxzdHZOZdajxlPHr0Au-n9XHSRCsq4Y3UXeOH7KodoJi8-Mzmjq3qBDOYWBTajFqS_MsII4-_sL6W77fNlZCuyOqVMEDoTm09X66tMbriKTP-bfvAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVzXVJvMOu0xaTqUfHL7GCp6zUe0XGBn6X-Q_nTrZ_O1NCU8oPG30n45sa6Cswc8pP6N75SCnxx5AXWYwfl0ugxW8nJWDlpTBamrkaeSx6TtrD1qXqR2tAvQNNy3k9h7XyJMNOqfbZUhCCshZy7WoaHFBl3P5Bzs9RjC8AY4CZXpbMdkbkJHxtURl6sKjZD1JRiCYjzn89nHmhUpi-41HtvnUSCSTA3rvUZngubJ_6YdLD5HTQ3JT0Kj6khtWnmQHRAcpNqEBMep88ELpdUC0cX1YqXsbBlrQNyk9AnyvzK-avKZo7nXb8PUkwcUyDyP18qKAEB_ECi1FHqJXbmnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4mEqo_TKtoW7zQG0O_jwaaNCZ7PffuVnro1IOXjaDxy2u8ndAC5rvAL6d8HwrYj_FRQj1VmkvBLzGlgj3KvrygdyNgtMJvt2xjwYlkAcucXXhlUHlbiby5ey2tIKHVVs7be4R1P8XnuzmAVGZnSmNSn2OO5whAkq-c21TYgYPNvoNlwVznUEUsNPqBm7FF_XQZOP4uiygrCFAzTumXf7uoTjs9Xo6CZ_Vgj-iCANr0CV70Sz6H_AThwzft3-gL1uZvZxVb1jTce40goB_nOZYfn3e3Ij2URmqsCI-7HbTaVw52jnTgSY4wh2VLpcHpNbdxt-Y1H8TFWtQjarLVWVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
دغدغه‌ها و هزینه‌های سنگین تحصیلی و ثبت‌نام دانش‌آموزان در سال جدید
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/691994" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
منابع عراقی: تاکنون تصمیمی برای ممنوعیت فرود هواپیماهای ایرانی در فرودگاه‌های عراق گرفته نشده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/691993" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691992">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be5e47fe60.mp4?token=IGTqXAWKwKnsoTtpLFQ9BKO0XJddiCA1ogrWQWQ7FEIRA-xbClOgTDZ5skcSEzwVS2neimW6mc1i9ryNOhUHbnk1acPSm-ff0L3N__kdb-8ZtErYF8P_NRHSwkfTvLqq8dpV-4YlqEfhl8nNKcC1rIwtf2szyzwgeNzRDxxQbiYjCTnY83qGkjv1hGcDhAtmEl2GirC0LvYIKfxChQ8uxwEt1xo05cYOq88D14PnJFTe8BbxMp5KLhKWfrZrVF2nqCoENXecFxErgyHGppx_DNgJNobXnNP0cRx0Avn552IPrh62jAVn9AMsKjynDTtdoGKrT1JSHWRJgdhTThy7WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be5e47fe60.mp4?token=IGTqXAWKwKnsoTtpLFQ9BKO0XJddiCA1ogrWQWQ7FEIRA-xbClOgTDZ5skcSEzwVS2neimW6mc1i9ryNOhUHbnk1acPSm-ff0L3N__kdb-8ZtErYF8P_NRHSwkfTvLqq8dpV-4YlqEfhl8nNKcC1rIwtf2szyzwgeNzRDxxQbiYjCTnY83qGkjv1hGcDhAtmEl2GirC0LvYIKfxChQ8uxwEt1xo05cYOq88D14PnJFTe8BbxMp5KLhKWfrZrVF2nqCoENXecFxErgyHGppx_DNgJNobXnNP0cRx0Avn552IPrh62jAVn9AMsKjynDTtdoGKrT1JSHWRJgdhTThy7WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «آقایان، آیا امکان دارد که با هم ملاقات کنیم؟»
🔹
ما با آن‌ها به شکل بسیار متفاوتی برخورد می‌کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/691992" target="_blank">📅 17:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691987">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff20afa1b.mp4?token=iwz6Hn2A6vZNrH7GC2UOLKOOt8i28qgmLFJg3bKEv6AgjBgej7_Qi8SWpkVe2cPonn5PRcC-d0Uy0viH8Fz0sycUoUf9Y71MeZxLE3_c_atLc0HG9sntpyxrUkif4ob63l5_Ci1dlXlBIQSTsDlnuurWbWhhmSXTl-14-bqZCpDq4MqNtWrhcLlBqZq5MU4R5XqmqZbL7pW2NGFyKjico_4oChDKselPXFUO69_4d6K_Gloz3BIu_cwZBIM_SJU3tt6_uu0Pqijsrr2aaZ9fhTI07A40E7Y-kjPAjQ6gUHWvyPUzpfKaDd5-Kp3HC5X2FgtVI_usJTt8UOgztJ84GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff20afa1b.mp4?token=iwz6Hn2A6vZNrH7GC2UOLKOOt8i28qgmLFJg3bKEv6AgjBgej7_Qi8SWpkVe2cPonn5PRcC-d0Uy0viH8Fz0sycUoUf9Y71MeZxLE3_c_atLc0HG9sntpyxrUkif4ob63l5_Ci1dlXlBIQSTsDlnuurWbWhhmSXTl-14-bqZCpDq4MqNtWrhcLlBqZq5MU4R5XqmqZbL7pW2NGFyKjico_4oChDKselPXFUO69_4d6K_Gloz3BIu_cwZBIM_SJU3tt6_uu0Pqijsrr2aaZ9fhTI07A40E7Y-kjPAjQ6gUHWvyPUzpfKaDd5-Kp3HC5X2FgtVI_usJTt8UOgztJ84GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروی BRABUS BODO با قدرت ۱۰۰۰ اسب بخار و شتاب صفر تا صد ۳ ثانیه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/691987" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691986">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7015ede6aa.mp4?token=icWciV8_1ma3r7GRsLxnSlh7jB5KOEcmJAq518akwbiDNzwNOsuDbY23dsvmG13n5wFBDZExkOpTVfzrx0TqOk59sLxBo2T6tUO1Kc7RajwjM8f0rVPvKsYcu5t6Ahb38EW6qg0NOy6MoXWiUsZk2fWcmwQ_DFm6gU9m9L4dbU1S1sZgMZK9kLbghYfQqrUSVYbudrDLUcE6-u281Z0eg4wwqZVHRwYCkjTlk5qyZdeiIbEWjGS0agLB_8Uh34eclqh-xGxNbTFq4C63iOdcBQCQ9d8pn2e-4tQKr91hTMU3XsCZhvGxa2Z238iInPAYzM09tFcYNV6-ostugSNugiHXi9H1cIHMdNS698LoCS5Wux3b5SB2bm8iszAMg29f8rJ3McTsxM0TBcCetd8stQ4xIDqRHeeExcgYDj6QP-14JmYR_Kt7Z6iT7UHsXdJX6XO_dNCajXvH_nsSu1BzCqxkZNIr_Ez652WBhD3uHh8L7bTQBNJOmH74NkvQM6OfNOI2RMi7YaN6jQdoMxr3xgsfM9BOJazJpIUOXPW47suFhx2eV6L5zNYp1t1ZpwUIAN7te7HteJiV9VuZlLIhzAP9EzDOLgbhffvqFpI8Vh9vSQrWv_qwY-nQVRNwXzWKXrcRVmbhNJVVyu4JAvNalni6wDYo59fCuEcVGPZTHpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7015ede6aa.mp4?token=icWciV8_1ma3r7GRsLxnSlh7jB5KOEcmJAq518akwbiDNzwNOsuDbY23dsvmG13n5wFBDZExkOpTVfzrx0TqOk59sLxBo2T6tUO1Kc7RajwjM8f0rVPvKsYcu5t6Ahb38EW6qg0NOy6MoXWiUsZk2fWcmwQ_DFm6gU9m9L4dbU1S1sZgMZK9kLbghYfQqrUSVYbudrDLUcE6-u281Z0eg4wwqZVHRwYCkjTlk5qyZdeiIbEWjGS0agLB_8Uh34eclqh-xGxNbTFq4C63iOdcBQCQ9d8pn2e-4tQKr91hTMU3XsCZhvGxa2Z238iInPAYzM09tFcYNV6-ostugSNugiHXi9H1cIHMdNS698LoCS5Wux3b5SB2bm8iszAMg29f8rJ3McTsxM0TBcCetd8stQ4xIDqRHeeExcgYDj6QP-14JmYR_Kt7Z6iT7UHsXdJX6XO_dNCajXvH_nsSu1BzCqxkZNIr_Ez652WBhD3uHh8L7bTQBNJOmH74NkvQM6OfNOI2RMi7YaN6jQdoMxr3xgsfM9BOJazJpIUOXPW47suFhx2eV6L5zNYp1t1ZpwUIAN7te7HteJiV9VuZlLIhzAP9EzDOLgbhffvqFpI8Vh9vSQrWv_qwY-nQVRNwXzWKXrcRVmbhNJVVyu4JAvNalni6wDYo59fCuEcVGPZTHpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوره CEO performance  ماهان؛ آغاز یک مسیر متفاوت برای مدیران عامل
۲۶ شهریور ۱۴۰۵، رویداد معرفی پنجمین دوره CEO Performance ماهان با حضور  مدیران ارشد از برندهای شناخته‌شده برگزار شد.
📍
ﺑﯿﺶ از آﻣﻮزش؛ ﺗﺠﺮﺑﻪ و اﺑﺰار اﺟﺮاﯾﯽ واﻗﻌﯽ
@Mahan_MBS
• ﺟﻠﺴﺎت Insight ﮐﺴﺐ و ﮐﺎر ﺑﺮای اﻧﺘﻘﺎل داﻧﺶ و ﺑﯿﻨﺶ ﮐﺎرﺑﺮدی ﺑﻪ ﻣﺪﯾﺮان ﻋﺎﻣﻞ
🎯
• ﺟﻠﺴﺎت ﮐﻮﭼﯿﻨﮓ ﺗﺨﺼﺼﯽ و ﻣﺴﺘﻤﺮ ﺑﺎ اﺳﺎﺗﯿﺪ و ﮐﻮچ ﻫﺎی ﺑﺮﺟﺴﺘﻪ ﮐﺴﺐ و ﮐﺎر
🌱
• ورک ﺑﻮک ﺟﺎﻣﻊ ﻫﺮ ﺟﻠﺴﻪ ﺑﻪ ﻣﻨﻈﻮر ﻋﻤﻠﯽ ﺳﺎزی و ﻣﺴﺘﻨﺪ ﺳﺎزی ، ﺳﯿﺴﺘﻢ ﺳﺎزی درﺷﺮاﯾﻂ واﻗﻌﯽ
🖋️
• ﺟﻠﺴﺎت ﻣﻨﺘﻮرﯾﻨﮓ ﺑﺎ راﻫﺒﺮان اﻟﻬﺎم ﺑﺨﺶ ﺑﻪ ﻣﻨﻈﻮر اﻧﺘﻘﺎل ﺗﺠﺮﺑﻪ زﯾﺴﺖ ﺑﺮﻧﺪﻫﺎی ﺑﺎ ﻋﻤﻠﮑﺮد ﺑﺎﻻ
📝
• ﺷﺒﯿﻪ ﺳﺎزی اﺗﺎق ﻫﯿﺌﺖ ﻣﺪﯾﺮه ﺑﺮای ﺗﻤﺮﯾﻦ ﺗﺼﻤﯿﻢ ﺳﺎزی اﺳﺘﺮاﺗﮋﯾﮏ در ﺷﺮاﯾﻂ واﻗﻌﯽ
دوره CEO performance ماهان؛ مسیری برای توانمندسازی مدیران عامل و ساختن سازمان‌هایی با عملکرد بهتر.
@Mahan_MBS</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691986" target="_blank">📅 17:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691985">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLQYvibGCkLjc6vb1emvoiQ4qs9lBTtf50n29n7d6QWo8H2hsplJEbawndXnpIUN64ZxHkt_TF4iSwH1OIJ-eoBGzzSFO-JulIKro-NYPqo3SKK7OCttQX9cVlwrhMk0FkYY6wTf6fiImbQ9j8VZRnzaNi14R3dh6BaKifDqwROwQ3JpGEF0_OJ7NYJ9IG1SGts394KxBJ1r8wGdHJ1NeC8jO74ZKiWz3CCkrmcIb9K2AJrDHhcd6CQTDjdDnDhXuxKqmpiB2vthwNc3TtysHHv9nvrORxWyKT57O4FyOFaQwu8ZAUZdv8_UBI_1OBAn5VBx_oB84cy1KT0juB1_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📞
نوکیا 106 مدل 2018  ساده، مقاوم و کاربردی
🔋
باتری ۱۰۰۰ میلی‌آمپری با شارژدهی طولانی
💾
پشتیبانی از کارت حافظه تا ۳۲ گیگ
🎵
پخش MP3 + رادیو FM بدون هندزفری
🔦
چراغ‌قوه LED
📱
دو سیم‌کارت/ مقاوم در برابر پاشش آب
📦
اورجینال + گارانتی + اقلام کامل جعبه
🔴
قیمت 2,590,000 تومان
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/fast/63670/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/615/180124</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/691985" target="_blank">📅 17:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691984">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: ترامپ به مشاوران خود گفته اگر «شرایط مناسب باشد»، مایل است دیداری با مقام‌های ایرانی در حاشیه نشست مجمع عمومی سازمان ملل ترتیب دهد
🔹
هنوز مشخص نیست که آیا ایرانی‌ها نیز برای برگزاری چنین دیداری آمادگی دارند یا خیر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/691984" target="_blank">📅 16:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691983">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8405ae9d51.mp4?token=jfwGn8B7QXOb3CKXd8rCtuyqSyYv_i_cGOtNuI8F54VsPKHUiJ_dmosRoSqrdxHWqLGb7KwevxXhUBvfsfbxwYoQDk7S4i-AE0hm3EWn8IJ12q1Gxd-WXEyGpG-vw6xefjyHrcIPlvLcOybPkKxEk3RqZJfJA3iTqHFmg5u11iSMNbLW57q6TEnpEPI_vhoUBxtqZ7L6LLBelG-pNzm5R3Rq1zdHVl0Upq4yPqqsNr1wMDlRVNRTeeEnNL1uktjBFITri70OxypxW1V7F4dWL_27vqPcIGFBYIbkkEeKrJmrvirfFRiVYQvTYgwRCsU3IFXoxfCeQjYROCQ9IMXF4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8405ae9d51.mp4?token=jfwGn8B7QXOb3CKXd8rCtuyqSyYv_i_cGOtNuI8F54VsPKHUiJ_dmosRoSqrdxHWqLGb7KwevxXhUBvfsfbxwYoQDk7S4i-AE0hm3EWn8IJ12q1Gxd-WXEyGpG-vw6xefjyHrcIPlvLcOybPkKxEk3RqZJfJA3iTqHFmg5u11iSMNbLW57q6TEnpEPI_vhoUBxtqZ7L6LLBelG-pNzm5R3Rq1zdHVl0Upq4yPqqsNr1wMDlRVNRTeeEnNL1uktjBFITri70OxypxW1V7F4dWL_27vqPcIGFBYIbkkEeKrJmrvirfFRiVYQvTYgwRCsU3IFXoxfCeQjYROCQ9IMXF4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یمن تصاویری از شکار مزدوران سعودی را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691983" target="_blank">📅 16:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691982">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf4be7f92.mp4?token=HTTLVu8MKRLGDOS19jwY0l7_zhZZtVhP_k6aJV_Zeugut6a-7QGX3nkgUxB1xv_b_2NVzUaJT35SwzOdc3tmgSpziik_YewfM5gJHQ1yaf0Eu0GOCMxzr8MEUvJoTMV83QMj37n1T_SVcz4pijcb9Gmu6XcXtqiDYHUkg4aCiSwvO6joG0EGfywDVGOqHy6cdiyxpCVKrCQ9CJyAfRlU06sORY9xNaZUqyNq9ROVYICFoFv8oZmHrEOKoTBG60JFjpJzRQ-UNiUcNGFAI3FMo8M5WvhBKOGwC0qvTWxpd8QSo2y1vhirdivE1PA6wRrvyo0cwiVQexQhpa-DH2KhZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf4be7f92.mp4?token=HTTLVu8MKRLGDOS19jwY0l7_zhZZtVhP_k6aJV_Zeugut6a-7QGX3nkgUxB1xv_b_2NVzUaJT35SwzOdc3tmgSpziik_YewfM5gJHQ1yaf0Eu0GOCMxzr8MEUvJoTMV83QMj37n1T_SVcz4pijcb9Gmu6XcXtqiDYHUkg4aCiSwvO6joG0EGfywDVGOqHy6cdiyxpCVKrCQ9CJyAfRlU06sORY9xNaZUqyNq9ROVYICFoFv8oZmHrEOKoTBG60JFjpJzRQ-UNiUcNGFAI3FMo8M5WvhBKOGwC0qvTWxpd8QSo2y1vhirdivE1PA6wRrvyo0cwiVQexQhpa-DH2KhZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز شناور ماندن کشتی‌های غول‌پیکر؛ چطور این همه وزن روی آب می‌ماند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691982" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691981">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
منابع عراقی: تاکنون تصمیمی برای ممنوعیت فرود هواپیماهای ایرانی در فرودگاه‌های عراق گرفته نشده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691981" target="_blank">📅 16:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691980">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
وزیر بهداشت: کرونا نیاز به واکسن ندارد و شرایط تحت کنترل است
🔹
کرونا مثل یک سرماخوردگی در کشور همیشه وجود دارد و راه مراقبت هم این است که مردم توصیه‌های بهداشتی را رعایت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/691980" target="_blank">📅 16:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691979">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2qbkgHArHstl3FT0P49JLjtrywMKiv8EAIZWQmwRxI5i-WBt19LjxRf--dWC3R7sj6nm7woAkGhwPJhhsG4OBO1o4GGmNrrh2QqOSAmN9G6XZ2CtXmsQiB1Ws-Bot64TIkhOYVKhvBIrAywjGx4zgdQ2Oul_8Ba_endS0BOE42jutf1yZtImbsz1wWC1Myga3OhEewH5ybAytWPjUEbXMyHuX4r8MUGj_Zl9-VU_-zaR1l-0tH6lJnc5WswLSLHBlRhZYreymbPyXYIU1pZwONlccBkl2nROwOeYFa-xSXk_Q19iRRdN0tn7rnrmHQEyy-UN6ZA3ttp8EGEmJx0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای اکسیوس: عراقچی خواستار دریافت تیم حفاظت آمریکایی در نیویورک شده است
🔹
بر اساس این ادعا، پس از بررسی تهدیدهای مطرح‌ شده علیه عراقچی، قرار است تیمی از سرویس امنیت دیپلماتیک وزارت خارجه آمریکا مسئول حفاظت از او در مدت حضورش در نیویورک باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/691979" target="_blank">📅 16:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691978">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgPRW8EMdUX4VKuxkhjrYuMpALAjt1rHaTmZsuYmgnMKp1QIh1Yyt_ca6yDY7wrXnNnZeDyOfzDPstk0QXH8nOf6AaLMvguSZBeVfROcUrYSkW0JFivEn7yWIR8sVJV0kcy5Ncjpso-A7solTNvMgCD8e19thaO2_bc3QwLuHJ6Fr6Ak3HevZJXMbNMzDHbLRwP4HjcN3AM1jYyjOEXny6r1Ptd1FXGKa_3boWS5KYGrxMG1aJVsQw7J3HeghCy_MIfX5HHJu6RaBhHsmnlrVNunQQJ5UCqmmft8ZCxuCUIijCiKD_zo8_NbfnDSX_ps_sdJhENEKx7maDktM6W-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوازده عادتی که ممکن است اضطراب شما را تشدید کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/691978" target="_blank">📅 16:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691977">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104b583a2f.mp4?token=RoOPazSzNs7wPSfG8a_1F0H2fiUERSYJPWG3YiJ6OoPBfpspwlRABPLql8QINNEJo_azQhrKrwTpXAFNEF8yh0Gh1HBnFO6CmNK9AYMm7kr2eWbeYT7ySOUcMY67Ch3EcKX1oHwZrD9ldxdKA8VzvN1A__5HVKr2LdipW18-58seMmR2DbHgViE056E5ZVuT-_d2B-mHFs6DWYcqeNsALO325yqG2wtmRFIiU4DmLF9oYiAeLWOFc1dbz6sTcgYhTj9QOJ_2QSCGrdW_km4YixfhFkacW3BabunqFxvgcnOBHqhF4QacjcE6fnvK7ymyGAD8Pob7tPOK-t5SpPUAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104b583a2f.mp4?token=RoOPazSzNs7wPSfG8a_1F0H2fiUERSYJPWG3YiJ6OoPBfpspwlRABPLql8QINNEJo_azQhrKrwTpXAFNEF8yh0Gh1HBnFO6CmNK9AYMm7kr2eWbeYT7ySOUcMY67Ch3EcKX1oHwZrD9ldxdKA8VzvN1A__5HVKr2LdipW18-58seMmR2DbHgViE056E5ZVuT-_d2B-mHFs6DWYcqeNsALO325yqG2wtmRFIiU4DmLF9oYiAeLWOFc1dbz6sTcgYhTj9QOJ_2QSCGrdW_km4YixfhFkacW3BabunqFxvgcnOBHqhF4QacjcE6fnvK7ymyGAD8Pob7tPOK-t5SpPUAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هادی‌زاده، کارشناس مسائل بین‌الملل: ترامپ به‌ دنبال ساخت تصویری ضعیف از ایران است؛ جهان می‌گوید ترامپ شکست خورده اما او می‌خواهد تصویری نشان دهد و بگوید که ایرانِ شکست‌خورده را پای میز مذاکره کشانده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/691977" target="_blank">📅 16:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691976">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ef500ead.mp4?token=GZ1LjqCQ_pN9i1wqMIxplw5ZBh3Pfh0V1Q0W9ULK060iWJLfmKO2PFm5tUhskZyVoh7h_TPi4HqZl9xetZkDEWK1yvckOG5D5MSPQUhaSTw7yNDowWh5sr0vg7d7pF8Kr1xUT6aud7yZM6aPkTLQscv_FDjirT3x9lt8VmUKNGVi6dYw1iWkbB_PKg55GOwWCT-H3PsRwys5TbcLkVPv6d36j-soi1NBHe-wVFLrxrOX_Xk4C3u5qB6ZGh2hNlhXFk5n4X3im0RdMTGPt1aNSVvL0NAXiQICBR5Labgn_cDM4Osr6GWgy8pmculuUOE190Fm_ja0MBKXOJ4lg5rBB2FjCd1Md4F46_iEaaMuTyiihFtFGWeIbBKs46MCRgrMExOqT57BX-qIxfdIuWK7gcpqYMK21DpiMl6UGKHKIg6jQ8lLNXoZaqq1u5Lt7WY4jwNiMVmV9oswj46WB7vdNoc1wGaLOyvSftrTuK8DprSGjIR5M8Qe3bKUoG81oaZhMuOgJLnhznXFxAlgQtInoUHuuixCsNukWSi5difvylydR4nCjK6dZhox5Msd8lA2D2P_9haAHCJ4J2aqbj086z8ASPW1q6T2SJqdpNrj5Fpiak02j32kGg9ETQwfQyCcWGYgDoDrFQ_KEDjP1hdUQlzDqCyJlmzvHmasJT1u-q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ef500ead.mp4?token=GZ1LjqCQ_pN9i1wqMIxplw5ZBh3Pfh0V1Q0W9ULK060iWJLfmKO2PFm5tUhskZyVoh7h_TPi4HqZl9xetZkDEWK1yvckOG5D5MSPQUhaSTw7yNDowWh5sr0vg7d7pF8Kr1xUT6aud7yZM6aPkTLQscv_FDjirT3x9lt8VmUKNGVi6dYw1iWkbB_PKg55GOwWCT-H3PsRwys5TbcLkVPv6d36j-soi1NBHe-wVFLrxrOX_Xk4C3u5qB6ZGh2hNlhXFk5n4X3im0RdMTGPt1aNSVvL0NAXiQICBR5Labgn_cDM4Osr6GWgy8pmculuUOE190Fm_ja0MBKXOJ4lg5rBB2FjCd1Md4F46_iEaaMuTyiihFtFGWeIbBKs46MCRgrMExOqT57BX-qIxfdIuWK7gcpqYMK21DpiMl6UGKHKIg6jQ8lLNXoZaqq1u5Lt7WY4jwNiMVmV9oswj46WB7vdNoc1wGaLOyvSftrTuK8DprSGjIR5M8Qe3bKUoG81oaZhMuOgJLnhznXFxAlgQtInoUHuuixCsNukWSi5difvylydR4nCjK6dZhox5Msd8lA2D2P_9haAHCJ4J2aqbj086z8ASPW1q6T2SJqdpNrj5Fpiak02j32kGg9ETQwfQyCcWGYgDoDrFQ_KEDjP1hdUQlzDqCyJlmzvHmasJT1u-q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انواع صندوق‌های بورسی چیه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/691976" target="_blank">📅 16:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691975">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ساعات کاری جدید فعالیت سامانهٔ چکاوک اعلام شد
بانک مرکزی:
🔹
ساعت پایان واگذاری برای چک‌های عادی ۱۰:۳۰ و پایان تعیین وضعیت آن‌ها ۱۳:۳۰ است.
🔹
همچنین برای چک‌های رمزدار و تضمین‌شده، ساعت پایان واگذاری ۱۱:۳۰ و ساعت پایان تعیین وضعیت ۱۲:۳۰ در نظر گرفته شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/691975" target="_blank">📅 16:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691974">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011d4f8d8.mp4?token=KoU_ncyNwlKFXTKPY8M4HAIgCUxoDLH6asj7pQ7zF57YrZKMvwyEkzNzCnrm_0Z6HnAoPnELVkW66r-BgUdWkr0T8s15oy-MWVYhUJ-pqZO0o0YIhosFNO2KvQpVQIkxLJOhNOdHwQ4uyS5KDkyk2fKNuCc2WFlsS3EJnCplfwOCEAObqbss3nKdOQqz41M20DL1drVQY1XiPF2cB9c3eL6HIpSJuCfcSemT37wbjHSC3CNWSv_3l-5eMHJnK3GR6CXU0rZS0083gGRo56ZGqnJNbXhci3YJ7pmS-peyYbVVIMKB_nl8v_yTmzFtxusvjEKMPCT93zOQz_c1EtSVsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011d4f8d8.mp4?token=KoU_ncyNwlKFXTKPY8M4HAIgCUxoDLH6asj7pQ7zF57YrZKMvwyEkzNzCnrm_0Z6HnAoPnELVkW66r-BgUdWkr0T8s15oy-MWVYhUJ-pqZO0o0YIhosFNO2KvQpVQIkxLJOhNOdHwQ4uyS5KDkyk2fKNuCc2WFlsS3EJnCplfwOCEAObqbss3nKdOQqz41M20DL1drVQY1XiPF2cB9c3eL6HIpSJuCfcSemT37wbjHSC3CNWSv_3l-5eMHJnK3GR6CXU0rZS0083gGRo56ZGqnJNbXhci3YJ7pmS-peyYbVVIMKB_nl8v_yTmzFtxusvjEKMPCT93zOQz_c1EtSVsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سریال فرار سلبریتی‌ها از قانون؛ این‌بار به بهانه اختلال روحی!
🔹
تلاش دروازه‌بان تیم‌ ملی برای معافیت سربازی با ادعای اختلال روحی، بار دیگر بحث فرار سلبریتی‌ها از قانون را داغ کرده است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/691974" target="_blank">📅 15:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691973">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c66c1f1262.mp4?token=uG4UFpyY7YgCfj-Uw-AkTbPtOEkVtEJFn4TtessVyzuIMzQOlfdel52reOXvD-bItGDhFAf3a6Y_y31dQ8qypiXaJL4LK8rh2ZJTAA8B_Kpbx3MZXDSxctPT17GLplWc5Cod2QeNiuGHZiJcINGKPiHeD-Ilnyz8z1jjqXt96oyvUcRfO67vDetSWHdNyiZBzYcER109ZrG8t-k5eb2jgz0na99kCtRrC-XVUCLLRSOej_TrfFLWOylT1X-P5y9_4-hTG4llnwWAcCXViWY-9awzbri-OxbeKZsGXP5oNr456hyQKHk0INj4I_TZZnT8wvZHXC0Xkjw5r3OWyC0RTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c66c1f1262.mp4?token=uG4UFpyY7YgCfj-Uw-AkTbPtOEkVtEJFn4TtessVyzuIMzQOlfdel52reOXvD-bItGDhFAf3a6Y_y31dQ8qypiXaJL4LK8rh2ZJTAA8B_Kpbx3MZXDSxctPT17GLplWc5Cod2QeNiuGHZiJcINGKPiHeD-Ilnyz8z1jjqXt96oyvUcRfO67vDetSWHdNyiZBzYcER109ZrG8t-k5eb2jgz0na99kCtRrC-XVUCLLRSOej_TrfFLWOylT1X-P5y9_4-hTG4llnwWAcCXViWY-9awzbri-OxbeKZsGXP5oNr456hyQKHk0INj4I_TZZnT8wvZHXC0Xkjw5r3OWyC0RTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدونستین جنین‌های فریز شده کجا نگه‌داری میشن؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/691973" target="_blank">📅 15:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691972">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9SaFTbhmtaeAcXX70cvMmbdEacqHwjEkq2wRfXBQIBzD0DMlC6lZL75a_stwz8qSjRB8-JMaKZfrmgT0Z997-Xy1uoP5K-eY3Xbh6xzXfkDYhZYVDK_8SYMZlH6PtxtKNBmM8JXyKOznb4Lub5OC17zs8M-63xJ7xo3VZOHx9A-vBop2lwM-4LolG2sl2H7yjR5buR3e7fWTb82l93xG5HS7ZSZ_PGJmvcjLgdcP8jC1C8YsrlRUrU7tLs8L82S39gfFCjq-0D2WdhX2e8HzCu5L8Z0o6SAtplxVBhnFsZwxSsDWBVjMse2fY-WskvOMEa2jdbTRp-sBai6LR8SgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تامین ۱۰۰۰ لپ‌تاپ برای دانش‌آموزان مناطق کم‌برخوردار/ مدیران ارشد دیجی‌کالا، منتور دانش‌آموزان می‌شوند
🔹
هم‌زمان با آغاز سال تحصیلی، دیجی‌کالا مهر با همکاری روبی‌تک، مؤسسه کاریار و مکتب‌خونه، کمپین «هرجا که تویی» را با هدف فراهم‌ کردن دسترسی دانش‌آموزان مستعد مناطق کم‌برخوردار به ابزارهای آموزشی و فرصت‌های یادگیری دیجیتال آغاز می‌کند.
🔹
در گام نخست، تأمین حداقل ۴۰۰ لپ‌تاپ و در یک برنامه یک‌ساله، تأمین ۱۰۰۰ دستگاه لپ‌تاپ برای دانش‌آموزان منتخب هدف‌گذاری شده است.
🔹
در کمپین «هرجا که تویی»، کاربران می‌توانند با مشارکت در تأمین بخشی از هزینه لپ‌تاپ، در فراهم‌ کردن ابزار آموزش برای دانش‌آموزان مناطق کم‌برخوردار سهیم شوند. مشارکت‌کنندگان همچنین از طریق داشبورد اختصاصی، امکان پیگیری روند آموزش و پیشرفت دانش‌آموز را خواهند داشت.
🔹
«هرجا که تویی» با همراهی کاربران ساخته می‌شود؛ هر مشارکت، یک قدم برای نزدیک‌تر شدن دانش‌آموزان مناطق کم‌برخوردار به فرصت‌های آموزش دیجیتال است.
🔹
برای پیوستن به این مسیر و کمک به تأمین لپ‌تاپ دانش‌آموزان، به کمپین «هرجا که تویی» بپیوندید.
روی لینک بزنید
👇🏽
mehr.digikala.com/madrese-besaz/#map
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/691972" target="_blank">📅 15:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691969">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سمینار آبِ ناب مزدافر مؤمنی قسمت اول</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/akhbarefori/691969" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
آب ناب؛ قسمت اول
سخنران: مزادفر مومنی
🔹
00:50 مؤثرترین روش در صرفه‌جویی آب
🔹
08:30 فرکانس بالای آب موجب حیات و زندگی موجودات است
🔹
10:30 چرا با وجود فراوانی آب در سیاره زمین باز هم می‌گویند آب کم است؟
🔹
18:30 خوردن گوشت حیوان توسط انسان باعث آلودگی آب می‌شود
🔹
26:05 آب، علت جنگ‌های آینده از نظر اقلیم شناسان بزرگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/691969" target="_blank">📅 15:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691968">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سخنگوی وزارت آموزش‌وپرورش: تمام دانش‌آموزان اتباع امکان ثبت‌نام در مدارس دولتی را دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/691968" target="_blank">📅 15:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691967">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deac79a361.mp4?token=OcSlzJdZCM0izdaSsJDkWUEMq_AnJXrCj7P8z1Ez0IUQHmO7RFH1dShimEpaJwT4CrBELQYeG9MufEu7knTNakLPZY2rfHRvUwM8WvQXQzEgPUpVng63Vsj1GcVszR87DFC54c0RaPY-KBVXq4fTp-M5AdcyXAsM1ytLaIycEXaNk_-XZu1Ecq27eS-rPOIEUlH6E5PdA4WljxarEqEC2WQglyccaqsqq2Jd_8JS0nrWPqlNyZDQez6CZ-df24bNwuXkCqJHAd71Ae7_eom2xknZtINlZgkvWZQhW3cdyk4niHgVCYM9hQfyujI_ncb4eCPlvyWoYeNefxf13QvKxWL0sUU-NrzcKhxq-gfJCdZwQu-d8sHDPSVcFajQotsfd63T1XiiHoMXIBUMEvHj5KHmYv0Ut5PHekoAt4qc4_72cGxc0qajBhsEJZ-tBcJq_1uPrQjs1BF7dAhfOy7758UG_4KKRRvuJ8gBHsMkuG6CxfmA8UZkzpA6w0l_fIP-AGQHXYyMprguRU9Sr6wt_rMaXjlkUly0iZCpJneY7K7WIuX_djdie9mM2o2e5iV8c_NE0If_BVnsTzZaTCn1CiS4pc6Qx2uu3XLE_AFtrx4Bwhuvo4ClpNXzTiW7m-pJPbxFzx9-jRjJDINXox7AgZlGJdV73c8HCri2BN2fY9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deac79a361.mp4?token=OcSlzJdZCM0izdaSsJDkWUEMq_AnJXrCj7P8z1Ez0IUQHmO7RFH1dShimEpaJwT4CrBELQYeG9MufEu7knTNakLPZY2rfHRvUwM8WvQXQzEgPUpVng63Vsj1GcVszR87DFC54c0RaPY-KBVXq4fTp-M5AdcyXAsM1ytLaIycEXaNk_-XZu1Ecq27eS-rPOIEUlH6E5PdA4WljxarEqEC2WQglyccaqsqq2Jd_8JS0nrWPqlNyZDQez6CZ-df24bNwuXkCqJHAd71Ae7_eom2xknZtINlZgkvWZQhW3cdyk4niHgVCYM9hQfyujI_ncb4eCPlvyWoYeNefxf13QvKxWL0sUU-NrzcKhxq-gfJCdZwQu-d8sHDPSVcFajQotsfd63T1XiiHoMXIBUMEvHj5KHmYv0Ut5PHekoAt4qc4_72cGxc0qajBhsEJZ-tBcJq_1uPrQjs1BF7dAhfOy7758UG_4KKRRvuJ8gBHsMkuG6CxfmA8UZkzpA6w0l_fIP-AGQHXYyMprguRU9Sr6wt_rMaXjlkUly0iZCpJneY7K7WIuX_djdie9mM2o2e5iV8c_NE0If_BVnsTzZaTCn1CiS4pc6Qx2uu3XLE_AFtrx4Bwhuvo4ClpNXzTiW7m-pJPbxFzx9-jRjJDINXox7AgZlGJdV73c8HCri2BN2fY9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشکوه رامهرمز؛ کوهی که قرن‌هاست می‌سوزد و افسانه را با علم به هم وصل می‌کند
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/691967" target="_blank">📅 15:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691963">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMzR-rkFSJ7QC1-jS7_swVGbBSlqPqxGqblxMzv-QzRgNd0G_6uWXv00RNBPxcQdR6wARmb_h1iMBLOpUltrx1z3EDdSl4QG_3G3kyY2X9AOl4tmX-2BKVNixqkRKty3Yy2iR8Y96VOOJCSsEttBPM6rag2_89191DPBxVEJs5_PhlpDFWbTT6lpVEdMyoiNhI7IMd1VZfVGgdCPvocCiIjewSQAzIHcqQ5wvpCxz4C50dTLR3yUwucjlkVdyeEhrb0okLSms6FHPsoFib-mIOyDo8sC1c493UAubVphWTAkaVMvyY2yUVqIc89eE7u64SwFH8xsVDx5rDxI9Cdacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEM_wJVz00j63KO0zAoz79w1jXeDau-OCoYC1Z9zW-1WbpI4MpB-JtIaG7rmf4hauJ2wTLwVmajGl_v_9UfIy3b0UsnVZha_Cw0rE_2HjztsKfaF3O_PZaRoWv836bQ7QmsZ4eUQyLWLNgSvMWOXl_B9IBM2Ol-danjgXfsB0cRMytfS4dq10ij8M6ahTd2sOstef6etDU900JrytG5DPVgdcpuVc5Mpt5VLGq8IWcihWN1ZoDX1pXr8co-TMZX76DqJdOc8Q-5Tnloui8S2aNIyvn6nQv6U3zhJQNflYsZVXGi6KvllMVfctBYVvsnMbjEu-e8q3uhyAYVWCkq8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fct7wwEP8BMXJ6Tq-FVcRmRi_C1Do-7VuPNHw5HJpG-xzsVV1SEQrFlEPIkT_MfFyfSOj9gjUAAnQogzj7YWEC1mtBgNYpRBtiIuzuSmJnEjvCANs752jU2QXA6cjAblMXX7dsdCqI5K12zmqZkz-BIMZbZR3mEFC0gmPeiSMucY3D6jI_S9-ntX2Z-pauUw0K5wmsyZvW_3SDvnqiCBtFebuAdQ_QHqlZThEuxQFQbUeB4TU38HSZa_pGDgmQP1HIKKq1_qTOzevDt97-Ava7zXG1g95s5V_26OSC2MgDqLBXFZL-dLli_qGK69UaUipu-e8TK9g2Ijluf_iVxG8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YS4R-eoNhNNtPjZaOtpjQwVk_y1nB7uHD5AGSGZZQpZQYadhj2_PSL5I7Dbi6Cb5eBRpQVms0sSFyoHsj9VKBUNde7hyvPs_9SUJl1P4UgBZVj4_aLtPMzE_tUrAwYmvOcgWLSybLP45tmW8jdEeyK-VG_uTRCFQo5UEVfa8ihBbJ82eL-URJvRLupQgOx0xjGtsZlm35mgzQ61h4yAihfc6_0194lqlplzRxnB8CWKPFmPLOe65zQRbO5NniUuBAVQRpTOAgsq_y0ma3aygc949us2axN0Ddg0s-DmD_JzWQHmhjTMESC2bTNzAG5FnsExwoxbZ1Een8ddEb4QEZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حالا به این فکر کردید وقتی بنزین می‌زنید، دقیقاً چه مسیری را طی می‌کند تا ماشین حرکت کند؟ #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/691963" target="_blank">📅 15:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691962">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
فارس: منابع ایرانی گزارش‌های مربوط به توافق‌های مربوط به بازگشایی تنگه هرمز را نامعتبر و فاقد صحت اعلام کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/691962" target="_blank">📅 15:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691961">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رئیس پلیس راهور فراجا از امکان تردد خودروهای دارای پلاک مناطق آزاد کیش و قشم در سراسر کشور تا پایان آذرماه سال ۱۴۰۵ خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/691961" target="_blank">📅 14:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691959">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14c48f3fb.mp4?token=MDyoJgH7Aun5ROxSrAn8kTOrN_MvB_S1Fmxwrx1Vd-ZHO1tY3X5vFVtU7JYqy3MM5rieAK-IToaEwqGw3S036N1voyoiMVq1Q5_2pGZDY1BlNJsjpI8jdxSe3iZO-7dR3f2mL4FXsqmU182rNVFoRLazVcJDHGWXo3PolsCX70oieHDKlOuNxw6sU5UKAp0cD_lXMRk42lk-v-mc3Sk-6EP0wKZc_kfWhj5aWqXOnJ-YpWiQFjS33RezGz6tf95gfg_nJmyRdknzXr2_4YxNWqljr0OQldTff0Bu5nYhdb53akGtaFh9CUu_ee5pdaIOzPs3XTGNQxCxkdrTesRxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14c48f3fb.mp4?token=MDyoJgH7Aun5ROxSrAn8kTOrN_MvB_S1Fmxwrx1Vd-ZHO1tY3X5vFVtU7JYqy3MM5rieAK-IToaEwqGw3S036N1voyoiMVq1Q5_2pGZDY1BlNJsjpI8jdxSe3iZO-7dR3f2mL4FXsqmU182rNVFoRLazVcJDHGWXo3PolsCX70oieHDKlOuNxw6sU5UKAp0cD_lXMRk42lk-v-mc3Sk-6EP0wKZc_kfWhj5aWqXOnJ-YpWiQFjS33RezGz6tf95gfg_nJmyRdknzXr2_4YxNWqljr0OQldTff0Bu5nYhdb53akGtaFh9CUu_ee5pdaIOzPs3XTGNQxCxkdrTesRxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر امورخارجه آمریکا: برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم
🔹
روبیو: فکر نمی‌کنم هیچ جلسه‌ای بین ترامپ و رئیس‌جمهور ایران برنامه‌ریزی شده باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/691959" target="_blank">📅 14:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691956">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9ebfef7e5.mp4?token=npETWn5PzK5kWF-L7RsoX360LFvtqDw-v1intfS8twTlMB2u7Vx9qExi_2wNsazWwYefq1UK8LPh9d0svwj55V8u-D0pzXXRUagotCKwjE6nDUhAXNWr9aEWDj9yZB1WQ1bx9ZqI-HccTtOfXxXiJCjVlzbRS0ujh6C4hxoLwCZjFR5Sh7oSBG7dSXmQ7QYUTs4N8x978VGYssuuZpzN3UK7nVfAAOZ-Idvzrv1FTqnLjnvP7D3JcjfVSLJCn7hA-8-9IoJSK0Jjua1S2O5dcbce0nR4JyzSslcx3oqv47imWMIkDxcYJA4HzvnoUzbmwtUchhlZ3Vu7ILEnOXJmlJisEde5FSH0R2oShYgWJ6002gg9uwkhYsVI4yanjX9DXymAmC7lrVAA3APjgkZWhCpeCsOuJM5t6h89Pm9gFN4ko9-rTHVZ9-6q5O5YIXiFRRPetUMLcdGdWNXaRPRkEfu2yngWWzzqsM20X6CSUbJUxntVGV3qmsOulEJ5PCuBh_IODU4xQ4xSRAlv-VtASwUw8JWYPeAVIZZ7vWU8_8MomRTPqg5pNZBzZC0KEii0RLcAj5lrP1DnReKkv1-ZBlbGt-mSKLSQtumnmXRuZk89D5kExC9tGYJPXfDZ7VBZk-FilFWXPJJnlSE-l27ol0U5Xwa_EVc1RrOZEHfiXgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9ebfef7e5.mp4?token=npETWn5PzK5kWF-L7RsoX360LFvtqDw-v1intfS8twTlMB2u7Vx9qExi_2wNsazWwYefq1UK8LPh9d0svwj55V8u-D0pzXXRUagotCKwjE6nDUhAXNWr9aEWDj9yZB1WQ1bx9ZqI-HccTtOfXxXiJCjVlzbRS0ujh6C4hxoLwCZjFR5Sh7oSBG7dSXmQ7QYUTs4N8x978VGYssuuZpzN3UK7nVfAAOZ-Idvzrv1FTqnLjnvP7D3JcjfVSLJCn7hA-8-9IoJSK0Jjua1S2O5dcbce0nR4JyzSslcx3oqv47imWMIkDxcYJA4HzvnoUzbmwtUchhlZ3Vu7ILEnOXJmlJisEde5FSH0R2oShYgWJ6002gg9uwkhYsVI4yanjX9DXymAmC7lrVAA3APjgkZWhCpeCsOuJM5t6h89Pm9gFN4ko9-rTHVZ9-6q5O5YIXiFRRPetUMLcdGdWNXaRPRkEfu2yngWWzzqsM20X6CSUbJUxntVGV3qmsOulEJ5PCuBh_IODU4xQ4xSRAlv-VtASwUw8JWYPeAVIZZ7vWU8_8MomRTPqg5pNZBzZC0KEii0RLcAj5lrP1DnReKkv1-ZBlbGt-mSKLSQtumnmXRuZk89D5kExC9tGYJPXfDZ7VBZk-FilFWXPJJnlSE-l27ol0U5Xwa_EVc1RrOZEHfiXgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار آفتی در میوه‌ها؛ لارو مگس میوه چگونه داخل بافت میوه پنهان می‌شود؟
🔹
مگس میوه می‌تواند تخم‌هایش را داخل بافت میوه بگذارد؛ لاروها بعد از تفریخ از بخش داخلی میوه تغذیه می‌کنند و گاهی تا زمان برش زدن میوه دیده نمی‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/691956" target="_blank">📅 14:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-text">✨
طرح ملی «زرین تأمین»
🟡
از دارایی مولد، تا تأمین سرمایه‌ای پایدار
🔹
بانک رفاه کارگران با طرح «زرین ‌تأمین» درگاه مشارکت
«صندوق مولد طلا»
را راه‌اندازی کرده و از این طریق امکان
خرید اقساطی و ثبت سفارش طلا به‌صورت ریالی یا مقداری
و بازپرداخت بهای آن در
۳ قسط ماهانه، بدون سود و کارمزد
را فراهم می کند.
🔹
بازنشستگان و مستمری‌بگیران عزیز تأمین اجتماعی می‌توانند با مراجعه به نشانی اینترنتی
refah.zarrintamin.ir
اطلاعات کامل این طرح ، نحوه ثبت نام‌ و مشارکت در آن را مشاهده کنند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/691955" target="_blank">📅 14:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691954">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bee54af77.mp4?token=eRzoRrw0scaZj3LOmqiNnGze5eCSpcwPc8A0MOwpR4sLu7rhyAmg_hcfTttgAeiwyiTrstmja4LyIxIDKJkBF1JMj6fo176ec3QSySBwvWMkePbXpP-suPpue350IUMakJZbUAMU3aOkjTNL2PydFMktC80gSSr0lDmuYZ5x3bk7TflyM_1ddoF8PByD3rbK_UiDrLFutyRuet52btrcO8NM3R1jpYiLDWwHNlSLS8j3AY6fqrImaclm9N9UZspgIce1H5Aijhg2NgeRNKks0N83o8v2odd0SIi9MC05OvyonKMDKjGgAVAH6q7phXccIMAELBrzHfDtsGNu6rpteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bee54af77.mp4?token=eRzoRrw0scaZj3LOmqiNnGze5eCSpcwPc8A0MOwpR4sLu7rhyAmg_hcfTttgAeiwyiTrstmja4LyIxIDKJkBF1JMj6fo176ec3QSySBwvWMkePbXpP-suPpue350IUMakJZbUAMU3aOkjTNL2PydFMktC80gSSr0lDmuYZ5x3bk7TflyM_1ddoF8PByD3rbK_UiDrLFutyRuet52btrcO8NM3R1jpYiLDWwHNlSLS8j3AY6fqrImaclm9N9UZspgIce1H5Aijhg2NgeRNKks0N83o8v2odd0SIi9MC05OvyonKMDKjGgAVAH6q7phXccIMAELBrzHfDtsGNu6rpteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شایعه دریافت پورسانت مدیران مدارس از شرکت‌های تولید لباس فرم!/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/691954" target="_blank">📅 14:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691953">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6631247d.mp4?token=Rs8YG1V4Rf5a2oNVU42SJ5m-50X2cLMqU357VccIPUT4sQKhb3hqKwTQRfF2GvKdC1Vze8R08Q5Srp3P4sPUAMIAV6Rtz3PZkzBXoKPUs4rmHz7RdmcNObw5vb39RlhMvLt-wNN7_0NMdRmaNOFvzFlmJX0ycgoSKd9zPEyEyHXK2_lai3RCJJXkRaIb0gDxiI8oexfW-ZWjUBnCX8sJF9_K6qWGJ335HbVCFre8WDkNp6HYjAeYk4Jb4C6NFjUF6eBKtUpNFBBGlG2AXDLEXDBDL3KF_8ViGExaALctkMVcyF2c0amuo0uOme2HAOXvlNGzGhrBhJR2tI6F-myDvHpk-tisGvKB4LzSK4x851nH38-7Vc5-NrD7apIzwRi86UKIYQde1qrojtSNYoHbhUYEs_qEOi9bgIC3ycZrJjoZbH70WrJQ-LIHoDO4yClx95fvmsTnCKjhUkzLi0b7paBitb8En61wHvFyc0tWvpiZwIuG9nh8MrDidSmbxebOdIYVaPieH4dYnq9el_MGVgbGcsT2SLVbW3TlK3PLWatMt4NUP_4-nOPaET2M0MmgMLSJ3GMmVsk6CTgBBelMqNtQj2obeAHW6_NHmCu2tY6asMMxOZtmsDOTMhdEW0ai56CbOEzjuMGYnJWDchKvDQVf_lIjpngiINC9l1EZKUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6631247d.mp4?token=Rs8YG1V4Rf5a2oNVU42SJ5m-50X2cLMqU357VccIPUT4sQKhb3hqKwTQRfF2GvKdC1Vze8R08Q5Srp3P4sPUAMIAV6Rtz3PZkzBXoKPUs4rmHz7RdmcNObw5vb39RlhMvLt-wNN7_0NMdRmaNOFvzFlmJX0ycgoSKd9zPEyEyHXK2_lai3RCJJXkRaIb0gDxiI8oexfW-ZWjUBnCX8sJF9_K6qWGJ335HbVCFre8WDkNp6HYjAeYk4Jb4C6NFjUF6eBKtUpNFBBGlG2AXDLEXDBDL3KF_8ViGExaALctkMVcyF2c0amuo0uOme2HAOXvlNGzGhrBhJR2tI6F-myDvHpk-tisGvKB4LzSK4x851nH38-7Vc5-NrD7apIzwRi86UKIYQde1qrojtSNYoHbhUYEs_qEOi9bgIC3ycZrJjoZbH70WrJQ-LIHoDO4yClx95fvmsTnCKjhUkzLi0b7paBitb8En61wHvFyc0tWvpiZwIuG9nh8MrDidSmbxebOdIYVaPieH4dYnq9el_MGVgbGcsT2SLVbW3TlK3PLWatMt4NUP_4-nOPaET2M0MmgMLSJ3GMmVsk6CTgBBelMqNtQj2obeAHW6_NHmCu2tY6asMMxOZtmsDOTMhdEW0ai56CbOEzjuMGYnJWDchKvDQVf_lIjpngiINC9l1EZKUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قیمت بالای گازوئیل باز هم صدای راننده‌های کامیون آمریکایی را درآورد
🔹
با پول زیادی که بابت گازوئیل می‌دهیم، حتی یک باک را هم نمی‌شود پر کرد. اینجا ایالات متحده و امپراتوری است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/691953" target="_blank">📅 14:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691952">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/574fad36fd.mp4?token=Lum0nawBGBfK-uF1I-etS9ctFnliyMelkPWl62dTd83R7Ex2Xm8tMJLtczyALVE1Mc5nP0jYOkWb384QCtQMzz4AaICdmFitu3Ngp5Rc1bb_MpkBaPhsCqOCU0Hv_gzNkrYEXR0ZpihtGAemC2zgOOt2OGWuopLGyea-Hss0LA3p77YWg-vQhgfgAw4d2z8qApXsLQBhDwbNyq143ntkEw2xlJFJPuN87ogNpi3JddZ8XW0gjin74DzSacSYklmy3g_peRRGHSJwKxxOOWQavWw6-uTbM2oAVbxlIlzQoR-1osgvocwR7imFecOq8F_oLfl2rNRdvjQc3LZgeqJY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/574fad36fd.mp4?token=Lum0nawBGBfK-uF1I-etS9ctFnliyMelkPWl62dTd83R7Ex2Xm8tMJLtczyALVE1Mc5nP0jYOkWb384QCtQMzz4AaICdmFitu3Ngp5Rc1bb_MpkBaPhsCqOCU0Hv_gzNkrYEXR0ZpihtGAemC2zgOOt2OGWuopLGyea-Hss0LA3p77YWg-vQhgfgAw4d2z8qApXsLQBhDwbNyq143ntkEw2xlJFJPuN87ogNpi3JddZ8XW0gjin74DzSacSYklmy3g_peRRGHSJwKxxOOWQavWw6-uTbM2oAVbxlIlzQoR-1osgvocwR7imFecOq8F_oLfl2rNRdvjQc3LZgeqJY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی اسماعیلی نماینده شهرستان میانه در مجلس خطاب به محمدحسین بهبودی: پاچه خواری نکن آقا!!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/691952" target="_blank">📅 14:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691951">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511a009592.mp4?token=jcs63BTsLD2e0QzhxrL6pMoMjnDKIJ7_Ikf9LvbRyucEnGaP2yPzLo3mZXa-nHtzJ_Gt9cezLN6TMFJgjQYO6C71THHH9mngwVEjUZFh7ha0hqGCuHMYC65t3WxNAfPRUz0Ge-fEBn6jxFrOiBMy0L5ZzOYIRBmDhOVByd9GImpDdQgD04MbNCyHc0kTUcn_OpAQrtSl4bAUOMCSl5y3TU8PHlJ1ZQEyJqj1cLgO3HqezvM5DnnNx0JfQcuNPbclZzMpeJL3eeq04jdQbhk9dj5sANNDERze0n708EQfNSKBcuM5vVlfPE3NvQcXi3FkmXJbDNceIsgN-A28cw6vsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511a009592.mp4?token=jcs63BTsLD2e0QzhxrL6pMoMjnDKIJ7_Ikf9LvbRyucEnGaP2yPzLo3mZXa-nHtzJ_Gt9cezLN6TMFJgjQYO6C71THHH9mngwVEjUZFh7ha0hqGCuHMYC65t3WxNAfPRUz0Ge-fEBn6jxFrOiBMy0L5ZzOYIRBmDhOVByd9GImpDdQgD04MbNCyHc0kTUcn_OpAQrtSl4bAUOMCSl5y3TU8PHlJ1ZQEyJqj1cLgO3HqezvM5DnnNx0JfQcuNPbclZzMpeJL3eeq04jdQbhk9dj5sANNDERze0n708EQfNSKBcuM5vVlfPE3NvQcXi3FkmXJbDNceIsgN-A28cw6vsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتیجه خودروسازی به نام تولید داخل؛ تحریم باعث شد نتوانیم خودرو داخلی تولید کنیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/691951" target="_blank">📅 14:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfceacc339.mp4?token=q1yyegcwpyMEimdpT_Q1BC0asJ-6Uexhf-hN0DgDhLhcOdz6jt9m8o05f0N-k9yfiMYW0vemTYKcgC4l522NvG_DtlfkqOVorUQMYl2w6JEV1YoQXHDKrIlq7JDMamNrQBFAYgX-VZ1KBwF47JZ134zNnhvykRDMMz1xUcR-tTczzis7rPV-EIGGbDUpL2FbqBglApPtN44HUhlTYkuK5nJxhdpgxniQPMe2UCRJuL3ouc3o7soUoHtSawRBKozNfshPywZH08xNlQie6XRXxaWy9eV2kBnxDlA_E7E8bdmuB7ajrQ4mzmxm5y57auRQ_7WaV968T8xxlL759ievmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfceacc339.mp4?token=q1yyegcwpyMEimdpT_Q1BC0asJ-6Uexhf-hN0DgDhLhcOdz6jt9m8o05f0N-k9yfiMYW0vemTYKcgC4l522NvG_DtlfkqOVorUQMYl2w6JEV1YoQXHDKrIlq7JDMamNrQBFAYgX-VZ1KBwF47JZ134zNnhvykRDMMz1xUcR-tTczzis7rPV-EIGGbDUpL2FbqBglApPtN44HUhlTYkuK5nJxhdpgxniQPMe2UCRJuL3ouc3o7soUoHtSawRBKozNfshPywZH08xNlQie6XRXxaWy9eV2kBnxDlA_E7E8bdmuB7ajrQ4mzmxm5y57auRQ_7WaV968T8xxlL759ievmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترکیب رنگ‌ها، استایل‌های پاییزی‌مون رو شیک‌تر کنیم #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/691947" target="_blank">📅 14:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seY3Mv9uX45u5p0bF7Rvp6DF0-gT4rYSjrfo-5ExwmA9FcwGGw3oxi5wSoL_5LuJ2baXZI1ORFStFBmN-piWwwabAkxIMV1ArUuWNwoLjnfO1uCtoB8vew4xQtucTxCLFOLTO-McBcrVSrzbvR74tbgEMXEkq_GInXTKELKg65hYJVWR1Dwudg-MaWDoTnneRMBQD2bh10q3abxcg25K4YpLQzH4Vcb06LbEFG9J7pcpTyOsxjKMMPMdQW6JIpsKwLnEjDPa_m8S6sxoOXLM1WNuvW2dUncoBl_zxwHHSEfxPe2QG5st6PsVUuoqMFpAVtMNvuhEKcnWfNHQDTAqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
پذیرش دانشجو | دانشگاه علمی‌کاربردی فنون و خدمات هوایی تهران (سما پران)
فرصتی عالی برای تحصیل تخصصی و ورود به دنیای صنعت هوایی!
🚀
🌐
ثبت‌نام:
www.sanjesh.org
امکان ثبت نام حضوری در دانشگاه
📢
کانال تلگرام:
https://t.me/unisamaparan
📢
کانال بله:
http://ble.ir/spatc1
📞
تلفن تماس:
☎️
021-88101220 | 021-88101218
📱
09998886666
#ثبت_نام
#دانشگاه_علمی_کاربردی
#فنون_هوایی
#سما_پران</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/691946" target="_blank">📅 14:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691944">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810030d60c.mp4?token=aQZNlzKIs0FLAQ54iv1OUDrlBDvKc379QQlHeEOKekWzbL0vRBlL9Gm_zmrQtrpJVrTm75-Fam1a10dA3LzxXMJznOfclm8qvxKMgv0rMjGc45IhJh3qaVquwWdX6yL3JUeXiyYDpUBk6NgU1nQQ8Q4wsmeqcNuyacW6K8saOwM4FlwVJlFRXMBM6v6vaFKH0wHkE2ufxRnGFsjI4J22jXpbH8uwbGTH45L00MyYjJNvmcPqXHKek4uHAajtEKBDgf-2sXdgfmjeKTyNQIkduTIleXUfakJbkMXl8Reamo5kCr9mIi9bV5xM75OTPRdfm8AsAS9bx5WeXVjea34vUzckQmmOOgLHiCsT1AHKEk9uBKt58mCoIEgtOgf3zY-GfUTmUoCrqwJoK29LKnAtBEaI1PuWYCwlGt_DMjj_dV5FhSJYUj2sClFiXKUFuifPu_Ol3KXikQL15MCSg11PU4TQhIzh20bzACg5SAz_tL1T6ic2B5KT6esqSqMsMkl9pq886ZCX8yXCS5Dc93YVC7W-qwVHzvbTWIBOV9ry66pcNbGGnfosLuDIHy_i-JyP_z3gbBEvXu5Q65jMl0RFmIC9nrPmw1VnAnNl3NHifQnk0LJwTF_nmz999JozUsNQAvMFotrbau45Uyr2Nf5OGsrmj_QauGrrcbnF-xFZ0do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810030d60c.mp4?token=aQZNlzKIs0FLAQ54iv1OUDrlBDvKc379QQlHeEOKekWzbL0vRBlL9Gm_zmrQtrpJVrTm75-Fam1a10dA3LzxXMJznOfclm8qvxKMgv0rMjGc45IhJh3qaVquwWdX6yL3JUeXiyYDpUBk6NgU1nQQ8Q4wsmeqcNuyacW6K8saOwM4FlwVJlFRXMBM6v6vaFKH0wHkE2ufxRnGFsjI4J22jXpbH8uwbGTH45L00MyYjJNvmcPqXHKek4uHAajtEKBDgf-2sXdgfmjeKTyNQIkduTIleXUfakJbkMXl8Reamo5kCr9mIi9bV5xM75OTPRdfm8AsAS9bx5WeXVjea34vUzckQmmOOgLHiCsT1AHKEk9uBKt58mCoIEgtOgf3zY-GfUTmUoCrqwJoK29LKnAtBEaI1PuWYCwlGt_DMjj_dV5FhSJYUj2sClFiXKUFuifPu_Ol3KXikQL15MCSg11PU4TQhIzh20bzACg5SAz_tL1T6ic2B5KT6esqSqMsMkl9pq886ZCX8yXCS5Dc93YVC7W-qwVHzvbTWIBOV9ry66pcNbGGnfosLuDIHy_i-JyP_z3gbBEvXu5Q65jMl0RFmIC9nrPmw1VnAnNl3NHifQnk0LJwTF_nmz999JozUsNQAvMFotrbau45Uyr2Nf5OGsrmj_QauGrrcbnF-xFZ0do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آوازخوانی برای یک خانواده فیل؛ کنجکاوی‌شان دیدنی‌ست!
🐘
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691944" target="_blank">📅 13:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691943">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9gkBNQoK1Gf60x_O8HFyY-oyAZVzyFcbbz2N2bJ26xlb4suTQFn1jf5eURGSDBhpF_TcRDRaEa8088Aci6C8ze07pom7HOGxQt2qLAaGFLbYRGpB1JPfC6rFe_yaTP3xdD1FvRFRPGKOEw40xRvYKuVchmpOCf4jmJSY_u4883__EwiTzj20J4pGh-xPE3vmVHvCzRt8Jduu0sy2XlC54DGArigu7hZkwm716eImn4VFll894CtrlG7dw2DLUVzFewdpBE1-Rciw3N1_GQso6lPjJb9F1mCjHIkxCY08R19e8kpTPMbx4pa_Qjbp8MP83JbuYZQj9p0aoQpq_Vdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خبرگزاری کیودو به نقل از یک مقام ایرانی: تهران پیشنهاد داده است که در صورت برداشتن گام‌هایی از سوی واشنگتن برای کاهش فشار نظامی، تنگه هرمز را ظرف ۷ روز باز کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/691943" target="_blank">📅 13:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک مقام ایرانی: هیئت ایرانی در نیویورک اختیار کامل برای احیای دیپلماسی با ایالات متحده را دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/691941" target="_blank">📅 13:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای یک رسانه ترک: عربستان خط لوله نفت شرق به غرب خود را دوباره عملیاتی کرد/ احتمال ازسرگیری صادرات از بندر ینبع نیز وجود دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691940" target="_blank">📅 13:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691939">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
خبرگزاری کیودو به نقل از یک مقام ایرانی: ما احتمال دیدار بین روسای جمهور ایران و آمریکا را رد می‌کنیم، اما پیشرفت در جهت دستیابی به توافق امکان‌پذیر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691939" target="_blank">📅 13:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
احتمال مجازی‌ شدن مدارس در برخی مناطق جنوبی کشور
وزیر آموزش‌وپرورش:
🔹
در کل کشور مدارس به‌ صورت حضوری فعالیت می‌کنند؛ ممکن است در بعضی نقاط، به‌ ویژه در حاشیهٔ خلیج‌فارس، مشکلاتی وجود داشته باشد که در این موارد استانداران تصمیم خواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691938" target="_blank">📅 13:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef0379982.mp4?token=J9447GZpZ5klQMlsFGW8-0xf7vNzBXcU1h3C06wzfw8OtmDfm4RdctFQ_0IBvng2PFUAAb7xIUMFnGimHsllangMblBBkhNnsyW5GItsSfO-EOFt7OfcMWotjLHLFJXuwFWUUAB4ynrAYOYeoihKwXVYBW61kXFjub4fWqUXKxDC9x9B8qjqVQhkZdgXXTi-vSTMmIOpbjM6Wx_aw-dyEaWpexsyCtf6P5sTp6K1KU4C7UoeRmFYDkl7VsfHwWyx-us8f8IB8Fbv-3pzm4x-vliF7nnICwgEXySoUS7iV_8keGVCMbtNWrnrPPLodObT1_Eu1sp4-F072sQd-WuarA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef0379982.mp4?token=J9447GZpZ5klQMlsFGW8-0xf7vNzBXcU1h3C06wzfw8OtmDfm4RdctFQ_0IBvng2PFUAAb7xIUMFnGimHsllangMblBBkhNnsyW5GItsSfO-EOFt7OfcMWotjLHLFJXuwFWUUAB4ynrAYOYeoihKwXVYBW61kXFjub4fWqUXKxDC9x9B8qjqVQhkZdgXXTi-vSTMmIOpbjM6Wx_aw-dyEaWpexsyCtf6P5sTp6K1KU4C7UoeRmFYDkl7VsfHwWyx-us8f8IB8Fbv-3pzm4x-vliF7nnICwgEXySoUS7iV_8keGVCMbtNWrnrPPLodObT1_Eu1sp4-F072sQd-WuarA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با کمک این ترفند، در نور آفتاب عکس بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/691937" target="_blank">📅 13:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691936">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
خبرگزاری کیودو به نقل از یک مقام ایرانی: ما احتمال دیدار بین روسای جمهور ایران و آمریکا را رد می‌کنیم، اما پیشرفت در جهت دستیابی به توافق امکان‌پذیر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691936" target="_blank">📅 13:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691935">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWgd0koilSaG99M1Pbqsau6ijuCsKVo1LV7KoA3Ul1DQZ3zP1otv4jSCNxR2oXWL71RIp0Px13Z-dirD8dyX47XAEhI0c_0hFAWfq7oCzto5iXgyxDcHo76beeEI0TQlPxr92bpj8inGoQB14Hwrx0fiaP7IyR8eu4iJ8mflqN3ptk1LJ3Q-drLMg3HaHhbRg6N5ppg59ErVeYp7wNDwxPaC9R9PtnTnWwBQ8zWBUgoYI_0-nvbpkyI5xEdJE02wBzxzCFCD-WKfImL8kFEdm5yg7yqGPbTzGLPFtKGDRWOj56v1Er-LAsm6jPNjbCmP8bT_xVJngIvFUe2l4Vooew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۴ شهریور ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
اسکناس آمریکایی در جریان معاملات امروز روند صعودی داشت و به ۲۳۳ هزار تومان رسیده که حاکی از شدت گرفتن روند افزایش قیمت در بازار دارد/تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/691935" target="_blank">📅 13:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6093fc394c.mp4?token=bGMbezdxhmjZSxtAoZJo7oY90NEiNlWzVPKX-LWKwfZ2ohJcTTiBPjF-5lDouI8_iRvFoPV9-dQ93zTKujndfQ5Y5Usmi8H1QVJKSwI8kWT78bmjrEiyNF4v7kWCn1wdtP7_BM6BwmaL-QNwkYw8YRYQ2K38mXjowyKMHLFzvQTj5Ya7A7_WuuIfmWiH3XkuFjgzPb_2iZZWdUkedOrg04E1EYlJXoWe742_VyCIzPCERTWXfVeZa25rdMrs0PjRJZfbDXd8G4WUS_1N9EE0yWfOY5zvOdNzbGHcuzRZLGkv5nszknbdLbHQWHqhNf1UjhfQaKzN6wqBKV3N5dFW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6093fc394c.mp4?token=bGMbezdxhmjZSxtAoZJo7oY90NEiNlWzVPKX-LWKwfZ2ohJcTTiBPjF-5lDouI8_iRvFoPV9-dQ93zTKujndfQ5Y5Usmi8H1QVJKSwI8kWT78bmjrEiyNF4v7kWCn1wdtP7_BM6BwmaL-QNwkYw8YRYQ2K38mXjowyKMHLFzvQTj5Ya7A7_WuuIfmWiH3XkuFjgzPb_2iZZWdUkedOrg04E1EYlJXoWe742_VyCIzPCERTWXfVeZa25rdMrs0PjRJZfbDXd8G4WUS_1N9EE0yWfOY5zvOdNzbGHcuzRZLGkv5nszknbdLbHQWHqhNf1UjhfQaKzN6wqBKV3N5dFW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعات موشک به‌جا مانده از جنایت آمریکا در عروسی سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691934" target="_blank">📅 13:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691933">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای رسانه قطری: توقف پروازهای ماهان به ترکیه، عمان و گرجستان  العربی:
🔹
هواپیمایی ماهان پروازهای خود به استانبول و آنکارا را از امروز، ۲۱ سپتامبر، و پروازهای تهران–مسقط را از ۱۷ سپتامبر تا اطلاع ثانوی متوقف کرده است.
🔹
گزارش‌های جدید همچنین از توقف پروازهای…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/691933" target="_blank">📅 13:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691932">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: بعد از ورود به مجلس، نگاهم به خیلی از مسائل دقیق‌تر و بازتر شد/ برخی می‌گویند امروز «کافر حربی» شده‌ام
جلال رشیدی کوچی، نماینده سابق مجلس در
#گفتگو
با خبرفوری:
🔹
در دوره نمایندگی‌ام صریح بودم که این بلا سرم آمد. در این شرایط مملکت کسانی که مسئولیت دارند در جایگاه سختی هستند.
🔹
در سپاه هم که بودم مواضعم همین بود؛ همان موقع هم با فیلترینگ مخالف بودم. اصلاح‌طلب یا اصول‌گرا نبودم و چیزی که به نظرم درست است، مطرح می‌کنم.
🔹
برای من همه موارد رد صلاحیت را زدند؛ عدم التزام عملی به اسلام، ولایت فقیه، قانون اساسی و جمهوری اسلامی. من از نظر برخی، آقای کافر حربی هستم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/691932" target="_blank">📅 13:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691930">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c721b268.mp4?token=gaQsX6EPG67ts6NGIeZzRnFqFf6QNfC-BD5f8SccaSANpmwZC3zDhDBkx0NnIqgGm2DnabktsUPCxpaAXm4ABAm8YR9pNX8nqkqABH9gD9tumKguNDRDp3Wt6CwXFeiK1lgyby5V3C9aQUXg6KLufoSN4ySMghDQ4t3fUYaJKIKAY-mw_HeDtNEDKDQ7owNenpJYWr6jd3Is3y9EhVIU6Konc84rJZKg8i1D0HqRo-kBcDDtGZS1wAss_z6D0kzswwXuHPJfQwUD2ffXlg8PobXUNJfAuGmG5EQ4NXYJRijSCIa19jK8oKgjHKDH24U3YLGzIunsvQGUDvVtK2MNaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c721b268.mp4?token=gaQsX6EPG67ts6NGIeZzRnFqFf6QNfC-BD5f8SccaSANpmwZC3zDhDBkx0NnIqgGm2DnabktsUPCxpaAXm4ABAm8YR9pNX8nqkqABH9gD9tumKguNDRDp3Wt6CwXFeiK1lgyby5V3C9aQUXg6KLufoSN4ySMghDQ4t3fUYaJKIKAY-mw_HeDtNEDKDQ7owNenpJYWr6jd3Is3y9EhVIU6Konc84rJZKg8i1D0HqRo-kBcDDtGZS1wAss_z6D0kzswwXuHPJfQwUD2ffXlg8PobXUNJfAuGmG5EQ4NXYJRijSCIa19jK8oKgjHKDH24U3YLGzIunsvQGUDvVtK2MNaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز ارتباط احساسات و سلامت
🔹
قدردانی
فقط حال دل را خوب نمی‌کند؛ بدن را هم وارد حالت ترمیم می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/691930" target="_blank">📅 12:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رئیس فدراسیون کشتی: حتی اگر به یک نفر ویزا ندهند، قطعا تیم کشتی را به آمریکا نمی‌بریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/691929" target="_blank">📅 12:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691927">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
سخنگوی سپاه: اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/691927" target="_blank">📅 12:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691925">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
معاون ترافیک شهرداری تهران: استفاده از سهمیهٔ ۲۰ روز تردد رایگان در طرح ترافیک از فردا تا پایان مهر ممنوع است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/691925" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691924">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
خبر لغو پروازهای ترکیش ایرلاین به ایران تکذیب شد؛ ترکیش ایرلاین ۸ ماه است به ایران پرواز ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/691924" target="_blank">📅 12:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691923">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiJ7UpwVYK-sYROIhvDd6q61ySyyfkXOuilFg6xWP6dBymrgE9sLaApasYuHMRuRdVqfQmLnH2ffpuK9b6IUt3EzJ2_NW54Ke5l6ZmYq_hoDAR798nWCroDMgsXF2nFLBAzf34YQA22KS_c0UIQz36QofNLAQIwMPXUGAgmK9uRVEwANdEnzo72zztnNb8LM5BOwS-03uvcYym4AfgXCRr2uAvTYFo4v2M0hcC5iRaCy827LO-kFd_f7PqvkWdov6KRtockONPXpIhKqwFKn2k4C5Boj6t_X3lnnxRscCPjpYsdw9UrsTs_HFgVutVIHvIP0Hze1nTT5jGA-J8iOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرکاری کاکل‌فرفری؛ پرنده‌ای با استایل عجیب!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/691923" target="_blank">📅 12:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691922">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
افزایش پرداخت حق‌التدریس معلمان
وزیر آموزش‌وپرورش:
🔹
میزان حق‌التدریس به حدود ۱۸۰ هزار تومان برای هر ساعت برای معلمان شاغل و حدود ۲۲۰ هزار تومان برای همکاران بازنشسته رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/691922" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691921">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قالیباف: امروز با موشک‌هایمان بدون محدودیت، به هر هدفی که بخواهیم شلیک‌می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/691921" target="_blank">📅 12:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691920">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سخنگوی قوه‌قضائیه: کشتی یک سرمایه‌دار صهیونیست به‌منظور جبران خسارت‌های تجاوز آمریکایی-صهیونی توقیف شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/691920" target="_blank">📅 12:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691919">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3A7gTGCYG0n40qsI3-bLaFUPI7trcvb55ThwxlY1tcUAh5la4gtSmi5V9n96OeaUdxvnekFqadoTu7vPKn0sV53_btH6ixXCRLsjdgG0Xh7zvZBZuecUfKkGqJq6COZJJQMNDIBOxqW3OJUoyoMeb1bOLTn8c6Hg54C33oAv-5hc3Gk0BmfBfo5_lp6bwVP8qsy7SqMisPW7bLKNBCZgHKATs0L8OokkknH59G_VE9sPbzxHt4VmW2gzXVMRb1Zq3CPze1VB5f0bGBgteh-3t1Gg7NWARMhdt5wBE9vd7LcQ--70f8PfRx0H5YFi_kRBBxmLc4Mxu_nryVr449StQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاسبی از شلوغی پمپ بنزین / ۳۰۰ هزار تومان بده نوبت بگیرم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/691919" target="_blank">📅 12:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691918">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قانون جدید رضا گلزار در پانتولیگ؛ هیچ زن و شوهری نباید شب‌ها با قهر بخوابند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/691918" target="_blank">📅 12:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691917">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6354ee8937.mp4?token=Mkdiqn83uQMesr4oFl-I5aThrmjKqeJUWModpi2gQ82mlPzaG6nXPj_lXVDCTHYbzrAWCLCtnTaDfJnsTs5mKLxlbnQ2ASS2PJy1_g7fDbL59V8Apo88j_gXI_aFaC4NvMbIWvfTtOVNhQjQciowTp6rjrKCRs2s6c-QK-L8mxvz1FIO0TYRNcLH8cEYt8zzTtYsozum_2dTgfNbFHpreOXse1UXBuzZpwOA3-6RV8EQRTsviUsEscF1zgVt5rVRLRQ_Bf432lX3Ergc4LmhQEF_ps6x_S5XWutVryxUp-VW0eb_nEUe5cj3igRbBDgR_GiOcle6Rd2yZcalEp1VgyztgYOKumb0ysBMtgPh8RWk0XNZvIdpttb8LDoH-bWo-W6_wi0Ci5cU8_svAJI29MY68ZEJ8_p5_D4GFWHL6cbcAOnF_Ht1yg4HUJuvmrKyJWa97G-6PdnAZF2RyNcmdYY_toZo7KN7TSToV3YQpGqbd-vJNDvGgIOnF2JGq7cAnk5BH_TQg9VwlluUXJBcK7ae110OTJrfH4eFu0K0SA3mPxeI7xgd3O2zV3z8OeYYgIKoN5w8Bl05KQQ-Jj1zbuvfK5RhpuecmnKp_yVVw8cbJUeSnkUeG7or9Vwl5JsqwFSsCNRsaSuqK_GqIin71Q3Az2A2caZ6tlQbJ6ou2ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6354ee8937.mp4?token=Mkdiqn83uQMesr4oFl-I5aThrmjKqeJUWModpi2gQ82mlPzaG6nXPj_lXVDCTHYbzrAWCLCtnTaDfJnsTs5mKLxlbnQ2ASS2PJy1_g7fDbL59V8Apo88j_gXI_aFaC4NvMbIWvfTtOVNhQjQciowTp6rjrKCRs2s6c-QK-L8mxvz1FIO0TYRNcLH8cEYt8zzTtYsozum_2dTgfNbFHpreOXse1UXBuzZpwOA3-6RV8EQRTsviUsEscF1zgVt5rVRLRQ_Bf432lX3Ergc4LmhQEF_ps6x_S5XWutVryxUp-VW0eb_nEUe5cj3igRbBDgR_GiOcle6Rd2yZcalEp1VgyztgYOKumb0ysBMtgPh8RWk0XNZvIdpttb8LDoH-bWo-W6_wi0Ci5cU8_svAJI29MY68ZEJ8_p5_D4GFWHL6cbcAOnF_Ht1yg4HUJuvmrKyJWa97G-6PdnAZF2RyNcmdYY_toZo7KN7TSToV3YQpGqbd-vJNDvGgIOnF2JGq7cAnk5BH_TQg9VwlluUXJBcK7ae110OTJrfH4eFu0K0SA3mPxeI7xgd3O2zV3z8OeYYgIKoN5w8Bl05KQQ-Jj1zbuvfK5RhpuecmnKp_yVVw8cbJUeSnkUeG7or9Vwl5JsqwFSsCNRsaSuqK_GqIin71Q3Az2A2caZ6tlQbJ6ou2ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کشاورز خوش ذوق ایرانی  ۲۴ میوه مختلف را با یک درخت پیوند زده و اسم این درخت ۵۰ ساله رو دوستی گذاشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691917" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691916">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LurXYw-j4-Z9eMZ44wI-JZ3EMBa9i_s3RW-Qi6VngFGyPdSxLe1wrH1sKFB6mAcl8PuBGWd0MOMwotBdNt40GobBmg3BGiJzJebFXSJjltE12UOwxoHuY6x7NjNfi-zkugwWteWRtzB-2fBEB_vVdTmv72shKBdc5LHgRyf9MBmDc4VkN-0MStny3Ec7TVyXe5Iwea4j0ilorjCJTKcQXvy8vh6bR19kGQfz1SJDo3SwL-Fh82vdauP-dn94puMi5a2N70NYD8A0z_9uLrIo1cmmF8bqSQBh_4reFOg73qxgZBPpU5ACH45VdaF16GTC2FJPxdgi_nR8MRLFrw2MtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نعمتی طلایی شد
🔹
مرتضی نعمتی در وزن ۷۵- مقابل داود نزمیرادوف از ترکمنستان با نتیجه ۴ بر ۳ پیروز و اولین طلایی بازی‌های آسیایی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691916" target="_blank">📅 11:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691915">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
اردوغان خواستار لغو حق وتو در شورای امنیت سازمان ملل شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/691915" target="_blank">📅 11:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691913">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2849bc42a9.mp4?token=WVzf8mH9_JQOOgK1KsnPT6jMfS5YBUEMCRO9ZfrGqQMtdyk5YkXjzU9BdPazMq39kuwLdS6s5aPSc4XF5w9U9XaXNyfKB3BoiOcVfSr8TPSI74xD8HWR4Gv5HqpBTKSFVg3au1WZxd7dJJ5c29tsCirkKGgldy8lVehj82A-9k8eNbP5RnL7fBb98bNaUPuDU5WavdjVAehfg_HMaqZ-2NmLjSi-CMqYjbc5ZoR9bPiaVMh5-g5KacM6FTC8Y7SPzyS6SP7NeTCcAbdJ7pml_zZhyLQbIbKEcLutiScN-IRosP1RRHZi_c2F8eJm35jUpOWXlt1Wv9LhFixPr_BZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2849bc42a9.mp4?token=WVzf8mH9_JQOOgK1KsnPT6jMfS5YBUEMCRO9ZfrGqQMtdyk5YkXjzU9BdPazMq39kuwLdS6s5aPSc4XF5w9U9XaXNyfKB3BoiOcVfSr8TPSI74xD8HWR4Gv5HqpBTKSFVg3au1WZxd7dJJ5c29tsCirkKGgldy8lVehj82A-9k8eNbP5RnL7fBb98bNaUPuDU5WavdjVAehfg_HMaqZ-2NmLjSi-CMqYjbc5ZoR9bPiaVMh5-g5KacM6FTC8Y7SPzyS6SP7NeTCcAbdJ7pml_zZhyLQbIbKEcLutiScN-IRosP1RRHZi_c2F8eJm35jUpOWXlt1Wv9LhFixPr_BZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر گردشگری: پزشکیان در سفر به هند با هواپیمای اختصاصی خود، ۱۰ تن مواد اولیه دارویی برای کشور آورد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691913" target="_blank">📅 11:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691912">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سخنگوی سپاه: مذاکره به معنای سازش و صلح نیست؛ بلکه صحنه دیگری از جنگ است
🔹
اگر مصالح ملی ما در این است که در کنار جنگ، مذاکره هم داشته باشیم، باید مذاکره کنیم. آمادگی صددرصدی برای جنگ، به معنای نفی مذاکره نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/691912" target="_blank">📅 11:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691911">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8205dc702.mp4?token=a2U5-5kpAzfeLZoWKk8jY-J286smTCkDN9u7VYtB50txcoM7wfnZWa1ZsXyHz4jjY9zZikdhPk9Wrb48zRPTQdLmj3QNvGuWHu2mCGuod8iqNBYZN5qzuHUrBZ0jNGrL9GIQFTE9guY_Ob7S7RA8gr3OFBuATO1ICTEdhh6-kEPRfvkCFMD6YsLuP3DZAdfa6zOrWuHJKUJnZOEt-mUWgJ4IYgkcES-rt8cFcktEMOE5n64l_l2ZmxMYX8Agk800kZvwIKNUtQ1LIs1X2KOrsm4axw_c8IZPmDNId86BZR5yPwS_ZaT4lATiARzYs1MH9sFiVHFo2r4AmHtUblCuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8205dc702.mp4?token=a2U5-5kpAzfeLZoWKk8jY-J286smTCkDN9u7VYtB50txcoM7wfnZWa1ZsXyHz4jjY9zZikdhPk9Wrb48zRPTQdLmj3QNvGuWHu2mCGuod8iqNBYZN5qzuHUrBZ0jNGrL9GIQFTE9guY_Ob7S7RA8gr3OFBuATO1ICTEdhh6-kEPRfvkCFMD6YsLuP3DZAdfa6zOrWuHJKUJnZOEt-mUWgJ4IYgkcES-rt8cFcktEMOE5n64l_l2ZmxMYX8Agk800kZvwIKNUtQ1LIs1X2KOrsm4axw_c8IZPmDNId86BZR5yPwS_ZaT4lATiARzYs1MH9sFiVHFo2r4AmHtUblCuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غمگین‌ترین زنگ مدرسه دنیا به صدا درآمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/691911" target="_blank">📅 11:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691910">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFjsx31liqXYtMI1E1ua1lQv1dLE9vKzoY6X_kcxDkBnNxnGbKJf6Y6y8tcAfhyDF5RvVl4ISs4wp-AxQRwjwGjydn3ba2cNDzd7RdBvEzknVyBlrLNvNlaJmGkNK06A3uyyyuBojn_ofWNw4MaQMOhLIX-50LHZUgDS6GIVVNmZKSsdVuOA8zI83xZdWtD-FkUZ5Q-b4DVojGl7L9YPOtV4KiG_0Pa0v4dLE67WAxC6L2L12xwWniPR9ePM4dXKULGPpSP4DezIBVAxUD-xgTyC82UunR_pLPxHo1cFr1fVo0kFFZsO_cAscH7tXOijOSm8JVKzhJ5Auq98UUD5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک_سوغات مشهدالرضا
🎁
مجموعه‌ای دلنشین از یادگارهای معنوی حرم امام مهربانی‌ها؛ هدیه‌ای ارزشمند برای عزیزانی که دلشان هوای مشهدالرضا دارد.
✨
مشخصات محصول:
▫️
قطعه فرش متبرک حرم رضوی
▫️
عطر خالص حرم رضوی
▫️
تسبیح ۳۳ دانه فیروزه‌ای
▫️
مهر تربت مشهدالرضا
💰
قیمت اصلی: ۱٬۳۹۷ هزارتومان
🔥
قیمت با تخفیف ویژه: ۱٬۱۹۰ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691910" target="_blank">📅 11:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691909">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba18746ff.mp4?token=n6-8Dm3mf6rDlSy5OvwSCjv7nFO9WVlmB5pDZsgqy5S2oWEyDeu8R6EcEPlX8ZdNFJkqgYzSVKfwkRDx-OOzhzNlbsZoOaMqS9fWb-BuEjFJgTUtO3q2UIQx_D7OttnAKXMqJkLchLxnHt1jvUyKK7xMvC2Vl6-4Boewbnu6Zrk5tr7JaE4xuPibdg7HMptrGccZUG2z1v8hz_pRIz24b04ZPFOW8b8aDD83uOGJ0xK6b6rP3dpMVSdTrPC1PcAmgpdJ3Lp-fxKB9hePTVMI4NUfa5pILiX5JI6on2vP04ROvtPYoaLyJy9b5NfCBmJe6VYOCbmQF000-eoGVmH-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba18746ff.mp4?token=n6-8Dm3mf6rDlSy5OvwSCjv7nFO9WVlmB5pDZsgqy5S2oWEyDeu8R6EcEPlX8ZdNFJkqgYzSVKfwkRDx-OOzhzNlbsZoOaMqS9fWb-BuEjFJgTUtO3q2UIQx_D7OttnAKXMqJkLchLxnHt1jvUyKK7xMvC2Vl6-4Boewbnu6Zrk5tr7JaE4xuPibdg7HMptrGccZUG2z1v8hz_pRIz24b04ZPFOW8b8aDD83uOGJ0xK6b6rP3dpMVSdTrPC1PcAmgpdJ3Lp-fxKB9hePTVMI4NUfa5pILiX5JI6on2vP04ROvtPYoaLyJy9b5NfCBmJe6VYOCbmQF000-eoGVmH-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لحظه‌ سرقت موبایل یک پاکبان در مشهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/691909" target="_blank">📅 11:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691908">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
دادستان تهران: با شناسایی حساب‌های بانکی و خودرو‌های متعلق به ۳۹۴ تن از عوامل ضدانقلاب، بخشی از اموال آنها توقیف شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/691908" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691907">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJWLypyDf2hJS-yWuoXhoGn2Y070cooJbtimZGwDhsp-HFigVKz79uucWgbiZo4TQDaZSEXgcEz-z4ZCalbFeBvECXz90c3HJ6gWNzbCqrVxn33AuhSD7rpxYSwjWdKXlWj9wwO9oNNJIv8t9gbF-DWaUfPKVIrN6WYpQ70-wacCwe2fiRJszIAI05_PeTbmXpBBOFxXOLlSuHzIRbRqEgjBsRtlRti9jPm4196OQErKmpoJgWSuLZCznh0nSEL9mZ5z8O89Me7WQoqVeC306_pZP3cto6MiAS7-iRhqofFxYqwZi89DZGAKBOCfmvSIeLzSKs7hdJhdPJUN_9CBOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حامیان فلسطین در سائوپائولوی برزیل، تابلوی خیابانی را که «دولت اسرائیل» نام داشت، با عبارت «فلسطین آزاد؛ از رود تا دریا» پوشاندند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691907" target="_blank">📅 11:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691906">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ثابتی عضو هیئت نظارت بر مطبوعات شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/691906" target="_blank">📅 11:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691905">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سخنگوی سپاه: مذاکره به معنای سازش و صلح نیست؛ بلکه صحنه دیگری از جنگ است
🔹
اگر مصالح ملی ما در این است که در کنار جنگ، مذاکره هم داشته باشیم، باید مذاکره کنیم. آمادگی صددرصدی برای جنگ، به معنای نفی مذاکره نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/691905" target="_blank">📅 11:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691904">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189a5c88d1.mp4?token=XCEgT1zf46UaL6mx0d5ipxNTpOw24o9cQP7wjR1JesP5AKv6DSw6fYqNbjaRhiYekNl2ccqRIFwwmDOiVDcDKINSaM5hXMmUFWNRaoB4qiLHaOte7W6egdZWqKr_VS86XAXatGr0pmARVGb6uv2aIzeGOz0RfM1JaHsiKobK9OdlojeLOLo9z3nIDxSQ_gPPmWIJ6PsDz3uaPiFjDLvpNox3V7xaYt-2RS1qrUkB9s2-ogdm8Yml7y_gHNnfATr9e0goLkfHjAxg9kWZ8z_YvyTFV_qV0dXS5NGo5-JXqIYgQER4Apql40CDezv72jR83hr8NNOcF28lU6G50qa_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189a5c88d1.mp4?token=XCEgT1zf46UaL6mx0d5ipxNTpOw24o9cQP7wjR1JesP5AKv6DSw6fYqNbjaRhiYekNl2ccqRIFwwmDOiVDcDKINSaM5hXMmUFWNRaoB4qiLHaOte7W6egdZWqKr_VS86XAXatGr0pmARVGb6uv2aIzeGOz0RfM1JaHsiKobK9OdlojeLOLo9z3nIDxSQ_gPPmWIJ6PsDz3uaPiFjDLvpNox3V7xaYt-2RS1qrUkB9s2-ogdm8Yml7y_gHNnfATr9e0goLkfHjAxg9kWZ8z_YvyTFV_qV0dXS5NGo5-JXqIYgQER4Apql40CDezv72jR83hr8NNOcF28lU6G50qa_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان باز به سبک اصغر فرهادی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/691904" target="_blank">📅 11:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691903">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2fcba08.mp4?token=E9SJ3ezd8cutqOhkfeKnwBE8mQc2C6VF5Ori7a7578LFL_2HbgX4N-BsQauIu566Q42kDceY-GBL1QosdrJ0xbeaYjkLzR17yBRjyjlDD3I2MfYZbAevwJ2ee_XDduKdfIkNyJqJ2PNHBb0EiLrpKi-pEhdZ6XmlPplahTdTaiziP8mZ-rSjQs1IPUPP-olfV-uMoCywzqpQQX-uZrZz-zblAV1ii7T_lABpjid7vVW9zG2yasHiU8TxM5hh0EVpVwfSsIpmhm03DrVs_dl1pr1fKr-tIG6ueHT-EVlL9s_F4nswDHg_AMWag2EWq_NaQ-H-L98tJGiQ3MGXmKF5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2fcba08.mp4?token=E9SJ3ezd8cutqOhkfeKnwBE8mQc2C6VF5Ori7a7578LFL_2HbgX4N-BsQauIu566Q42kDceY-GBL1QosdrJ0xbeaYjkLzR17yBRjyjlDD3I2MfYZbAevwJ2ee_XDduKdfIkNyJqJ2PNHBb0EiLrpKi-pEhdZ6XmlPplahTdTaiziP8mZ-rSjQs1IPUPP-olfV-uMoCywzqpQQX-uZrZz-zblAV1ii7T_lABpjid7vVW9zG2yasHiU8TxM5hh0EVpVwfSsIpmhm03DrVs_dl1pr1fKr-tIG6ueHT-EVlL9s_F4nswDHg_AMWag2EWq_NaQ-H-L98tJGiQ3MGXmKF5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر گردشگری: پزشکیان در سفر به هند با هواپیمای اختصاصی خود، ۱۰ تن مواد اولیه دارویی برای کشور آورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/691903" target="_blank">📅 11:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691902">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای
نماینده آمریکا در سازمان‌ملل: تلفات غیرنظامی در درگیری‌ها عمدی نیست و ممکن است به‌صورت جانبی رخ دهد؛ پنتاگون همچنان در حال بررسی برخی موارد است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/691902" target="_blank">📅 11:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691901">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
چین: با تحریم‌های آمریکا علیه شرکت‌های هواپیمایی ایران مخالفت کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/691901" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
بیانیه ضد ایرانی گروه ۷: اقدامات ايران که قابل اعتراض هستند، یک الگوی خطرناک از تشدید تنش را نشان می‌دهند و هشداری برای وخیم‌تر شدن بیشتر درگیری‌ها هستند  گروه هفت:
🔹
اقدامات ايران تهدیدی برای تضعیف تجارت بین‌المللی و ایجاد بی‌ثباتی اقتصادی جهانی است
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/691900" target="_blank">📅 11:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837e110056.mp4?token=OC3PlL8Rfc-hkBWb4db75HArRF0RWlX8QgL0idJ52n7ff3FbfYRrVgcCITIGL4TxvbuJ5ARbTXBU4ASOdobKWAw4yhk4bJZlX4mfLpxFOmNPWardyPZlu_V6ufaI73UbhajibzbWXN8pCkIlRSQJ9rSXsM2W2xAKFma8fnLt1pCTqE3h9tPV5RuCbuakFMokKQ6i_D0wlRPelImj9BG434lfxXbB5gt_FVIwnCbP5cbK7sz5DsyL9HFLIoEFbO5rCBukYExu1D0LC8axwz5HJPFYWMPDAqgh_c9thrdV8xtYce3hiz9UDTzHzqpwgCkivBULioG1Zceq9xk6j-NVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837e110056.mp4?token=OC3PlL8Rfc-hkBWb4db75HArRF0RWlX8QgL0idJ52n7ff3FbfYRrVgcCITIGL4TxvbuJ5ARbTXBU4ASOdobKWAw4yhk4bJZlX4mfLpxFOmNPWardyPZlu_V6ufaI73UbhajibzbWXN8pCkIlRSQJ9rSXsM2W2xAKFma8fnLt1pCTqE3h9tPV5RuCbuakFMokKQ6i_D0wlRPelImj9BG434lfxXbB5gt_FVIwnCbP5cbK7sz5DsyL9HFLIoEFbO5rCBukYExu1D0LC8axwz5HJPFYWMPDAqgh_c9thrdV8xtYce3hiz9UDTzHzqpwgCkivBULioG1Zceq9xk6j-NVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​
♦️
صحبت های مستانه مهاجر درباره جدایی از پژمان بازغی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/691899" target="_blank">📅 10:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691895">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTsHIw-17fkZmmaqEjboT0Y3DmzAmIeMsRrOfnVBFr3sOCxhlhhYIZHg3BFDJkeLHHzzvEf4c7yeFg03MCaxb6lUTNxhdGf7Zoaq24ShodtFrQZX_mahtBdTmfPUcyG1O0k5vUaZNWHPbJdqH-1y_g5osXWFgnNsxrKHMpXRkgfBuVmWFlt6xshbC19jAXHowP8DGXlxz-l95Jp9YEWmJBl9-ESLt642YTIEU6QFlikIGXMcPyZiwaiVt3uUVLAXm0kk4fGuO-_wpKgDmLE7MWhyYIh-fGX8WVP5sp9CE2bGglFoiuyLm-iEax0cosau0W5OUI9mOAqzi6G6N4PdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tylj3miEqA3Io14g3jY1wMZnQGClpCsfFBNSIj9dPSwo_Bev26cNsWdZoVw-EMXkx0d5GOuIJpN9tSmiqQR-Qv6qXFBqSXG90ncKZ0fslTyiURXDEOXefe9__gSvOiDIA6KAQu1FR7w37cQQZF-3FLWRNEhmWRo5o0PJNgXNM2gNepvApst_eZ8JOG0x8YwUnd-Gfqaz3_bYCRzc6_DdtrhSmOGNtLD2516jtoJPlwmWwV7hJ6aSegl4Mnlp6YL5vKFofu7npO4ygnIZNWrfFHa5LuUeb11aT6u-j3qYmsgKWMHyJEC14ARMo47CRuYnYqL2EOwbhTDRXd_BAGk2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-8CGyxBTQw9lSka0dl89gJTgH3gz65Q-yp_HbHkLwNrLmnyQiagk9kRQMIWu0JgqBg-GaI5jNpQDIcKiei_2uXKwUcyhCIBx4mBr2iWXxBIH2Q-bqbD55qEBhLJGt3q-Tf_CXVgRSTha8V71eO88jNCulwvWdmw3aSEQpDZ3_Mhk5qbKq3PSH2CH2fO8ep8R1HrYb5C07u8EdBt48vWa0yqgb1K6ZDJwuAJe9iuJDtFjdaGrURsqZUmtBGjIut2sRbxLsHebjwTDI2j-gr8vBOuiLz2inQ_Y2GGkJPV2sTAQrNLEDIL2N3BE6Z-RXtaAuI5rdjfQHxlGXfdaPftkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری دردناک از آثار بمباران آمریکایی روی صورت دانش‌آموز میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/691895" target="_blank">📅 10:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
پزشکیان:
دشمن در تلاش است تا تمام راه‌ها را بر ایران ببندد تا این کشور را وادار به تسلیم کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/691894" target="_blank">📅 10:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691893">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ساعت رسمی کشور در پایان شهریور ۱۴۰۵ جابه‌جا نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/691893" target="_blank">📅 10:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691884">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vyJKEBGUprN4nY42kKsqCZjq7YQvGnLDZczXypRFT9N0KrXGUTEpa412V7rAdDh6T4qkqMgqepv-cll5tgPikzR9WrJfEhyBreCbGReAAtDTw501JcWTh9rgU8z-1qqhB7QHEyGmAYquInW9UsutfR1mfTsM4g4mRz6LDCJk0RKArOBVgUY9GswJ1z-xf18wxgVVzEVmtJPCsySKPgn5TQjmKuG77FaEbhLaD10Rpk80R6sOalv_0lTGL5lShJSi8C7Xqt18zhDaDvvqFRjckBXbboKC5a4bDMbNYSvtU4BVDQq55_laOKJCpflYBsuPftmUk3BbKhq7WZ57BoveSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qH7RhxH1sxAdWjUPVGfK6gwwBDjNneHtzPCgmCEc_gw7p_H1Qg-flPTxHr2PoudU84Skh3IcY84k854WWmVV6eK-ZL3tEqUcDI2p4L_AGyQt4sMxAMPwL_RJ3RDZ676RBKEkbbnqi0iLzvlrjjlGysCjElPW8QHdDvcoetDJNLCa9Pr7Ymkg4Uf-KguERz0j7tVW9Tgq-7G4-w7HCwylPOVzBfbWClr1QFYKLcRvHorSoGp7wS6qJYM4KsyJC3h0RvTtq0UMaStrKy-s_0MrWTpDnlnwK2B-LRXqqULCujSxYxP25SOqGq1Ikomec869-zQnoY966Pv_8J5cF913_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bnFxmMLDs8Zc81KZerJNEtIaDXWl4qUwX0wZdnc6tBZerVgiQiwfNFsNtx2vzICrLAI-IfFmNadJ2PqoJuV7zR_EyyXSSz5vIrYPmX166QweuaiApeBcn-8oKhHltAXBrInY-sZG3nhg_RWMfynNy2v_xGHrKXTeJTaS3RBzK-S2X6cijea3zfTduWCa5tT-7X3q4NGTvL7Ts6fdl-pCAEZsE4e9lDK_7hEVzUXwd2F2_Rt-Z34GC9OiifDrwKASH-yKE3Sd5wZy2ntF3Lvicawu4yDwrKOunkJZ3gFB2aOlJvLeyCOceiZ5kNtR0SxMlacrVWj20mxO4PdHeUMKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X-lo_hvWFR8LPxd6fzSDbzq9be4__yUzIT9PDjw9_5xiMEJEFoP6UgJZhSA1o0VThfxDBBrbXVgqz-W0TrbYFHa-5A1zI5lH-pEQG4GIZYNNw7qvoojyjjBwTW5rqzBXzcZZhkCKHiaEkm9D49loMWG5xfHZuktUUNw09dtzu2qBlrNqabMCGCfVxEivcP8s8WbuxJTtmR4rSi_9D-jUhYYGxYW3M-ErR-67KIKRbCJHaM171GJGaKAGwzGAp83XMmDShS-_K_Rc8VCu80selU08b8FNptIzC-yT0csAlb3oaxa2fvqzeIGijQh9InguyjHaOZlHc3mBbXz_VjPCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B8QejVGbDF0CsiWM7tQfjXJoqxZJtmaRMO0KfLiVTNpsVKHNNAqE7Kw_dhWRmwSMYdT7-ASqHJCJjJQpYltowTnWgpwvWPOensAdkZLLwObBm9dMHI-LVERcO6ZlCyxDWrcEzKRWZHZk28-44zv4q3LlUkmjYX9yc0zu6Mo5d0qYXIXT0qeWlXoOOmEoNuhDYZCG7bEZH_5anWjrdRiAuRK0F9J6_C-nZlCFLw5Nu1-HzR03L_-iagHYB8RL19c6ocg6aIctXwXGiglcwHM8zIawv82J_hfSYAD7MkzclR_p5bIwcinNsaTSNOW-ybdBwmkZek_Oot7mtNcbUkIcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JbGfiNwL_mjOXsITCXEBHTJWtlM5uVcAvhR2rthqk7SHI7RuKB5aoWP8gzzANtXdIGQKOj_HH2zp5p2aAo36Urb9qKIGqoY6b_paqKsQMk0U9Fex9iNXEkqDepPvIpvP4fOQbeTZmw2t_qTJOMxfH-AlquhK-5138LRkKviHzfNGVVW3vwhMM8ar3qhbh-X_7iE6q_89DcUu9vYVO8uIcGlY-cbF0FfCxpbgOxqdPm_08fn0NNFNT20ePuyEek7lAuD2EsAHTO_NEV8Cnyn2-5mDVBSWaeo7q9jd2U_IYwW6Zp4lQWdpepACy18-Te578MrZk4G4pbkigNhOqNHI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zfd3ZvK0I1bTPHbhk8T9RJ3DWVs7mkeQi4AZ6QAGZ_6QmwuQOhyYSJqPubzXSuNCmzKE3XyVHFEZdFi7RtYSfRbQ7J1Rje3elfTptJKfD0iWX9ENjI2Hx1EhLLuw9xA5-iLKjBzdxGWHKuEaiIq1DiGhhdDCXh-9uDRxjmB6Ycmm6x0e_xYRVC190YjgB0Czytd2TB1-TRoXKdCJ3AOExmiutSFTABvicHWpve04BIkVH48xzASHz6AOHxzHAmkdQQq2MHiJk1b3ghtmKVkx2CHf3TTPFiEWIHZzD_s6IpHQxjyQ8IeholaNibdjl0OOzHRtQ69CWhgemQEhqdTBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g1OcXlrQTrWg98xVFQBVY1AJ-v2VkQf1zQzoYn7oOROTYW1XgvRUa5kTElXolrQ-iNlN7QJqVFF02Pz8bZzlyMKRTllkASgWuh6jSLko3e5MzXiuMQNwgkeo3NhH3V1Vm0dhy7Z4BNtHbqH6Fi7ghcToNLENY2UjlNGPT6849JEOWMcrr5ibVt_VoOzk1675d_5X3Tqm6mKKKvzryeJWBppf-oC7sgU8iTcoOHzY77o0QwNehPcCIcQhx6SC3Lsvon5TpXMppNuw2LP2W2BaDbXgtFDFD5AmxE4O6YrfPwjkdUv-PZexQ6z_SFj780m8_5bAP_EyPAHVRfJV5y04Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jKPvsjgL55N40EUNCyHoHTOK7A_L3zKHffyc7BR_boJOF0kPV4bbAykPMWWfUQfwEoGnrpskvNtqFiYeM6g1WCHQ5Mi9hJI2vK5w5cq48uCjWLQjINPY0lT4Nz3KrL67V2fKwQp08QUh7yxqOW7FlKK7hFy2oCJuYIALb1jgH8kxU_1gaHmTTyz2z2YEhBF0bbAmZii5g9e8FtefcBbVGxE4asXmybAwcaRF2WhXN3zBbHSRoJ1Ae1EP4Et2CfC16_fX78ihNX98EfYoZp_fCcR8gYUbWZRopwLegGK6KSp9x2fa7g1zak4X0TDE7y8vW0-chbTkhfCbkntVVRn12g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برای سلامتی هر قسمت از بدنمان چی بخوریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/691884" target="_blank">📅 10:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691883">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3dfa4e80d.mp4?token=L69yc_VVugj-DCOFQa_ndw48saIn6eOU_NzzRN4AdKwZCgAmTuQI26QN4z0uX-Ak_jpL8rq9mM93wP2jSJ-CstLpu6SgzWE3DWWOCm3acdtFdundAwufHn7pVBjl0-ITgr3hogzGMutoD7EBu8ufzqc832AwTtmUiAPCrN6G0bJAHI3k584E61nPVI-XY4kS7AUmMPUU1m4FMEM5i-1uwfpI7XK_M4mKpT2IrImBVcJB_NVILzB4gl6-IgzY2WLjVnwENzbOY0rpSfN3Um65Uld8Ift79CVTJdZVFZLlU3DQZ_w9_BT5SNgj3t8_j70glDcHByGtkqC1DxcZrDEa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3dfa4e80d.mp4?token=L69yc_VVugj-DCOFQa_ndw48saIn6eOU_NzzRN4AdKwZCgAmTuQI26QN4z0uX-Ak_jpL8rq9mM93wP2jSJ-CstLpu6SgzWE3DWWOCm3acdtFdundAwufHn7pVBjl0-ITgr3hogzGMutoD7EBu8ufzqc832AwTtmUiAPCrN6G0bJAHI3k584E61nPVI-XY4kS7AUmMPUU1m4FMEM5i-1uwfpI7XK_M4mKpT2IrImBVcJB_NVILzB4gl6-IgzY2WLjVnwENzbOY0rpSfN3Um65Uld8Ift79CVTJdZVFZLlU3DQZ_w9_BT5SNgj3t8_j70glDcHByGtkqC1DxcZrDEa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورت میشه اینا دورهم جمع شدن؟!
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/691883" target="_blank">📅 10:19 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
