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
<img src="https://cdn4.telesco.pe/file/D8SVRKDX2tCCo42UXZo82YZccSi1ZnzwhQC-jwFr-aYitVhesNp5M0ZartY1hZcWbUA8A3LFprTU__cLwPM7hJM_AHcIPwRdRuLRlTQguqdMjNylyvahdq9RCT1PEBk_XY-j3gxFcMio_FBRuJf8t0PQHa1qG1hGWq6CXL5u6oM685Xn0L5kveYom6t2Fu3IWffjcBqASEdc3nsxDeD2LsuaWgXqSXrGv8VOr-GkYejwt2B-n0m6YvWBBpGEaN43yVmJbE8ZHksyE9u2EoRNOLF_lZoJwOIvIL8EkUKdsP9qRAHl2meVUdall0vWMdIWM1994hpkXMy083AL4do06w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 948K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 20:53:28</div>
<hr>

<div class="tg-post" id="msg-145446">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نیروهای اسرائیلی با چهار راکت، اطراف تپه «باط الورده» در نزدیکی شهرک «بیت جن» در ریف دمشق را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/145446" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145445">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhSGEPov9Ad6TJsGt9u1MX9URjTNHJxZbR7dPybjE1bsEu73JG3d0Ecm-G1h7xeCIhMkFozFriwwakirpT0iE_PiFl9sPy0iKqiKOU0UUqjSesqC60250wkbt0cTU3MJeMMPP4ZB8Adw1RZL08HtzjG_k_th8l7qh0RUqDGCuerLv8cEP-XG7NZ9lgk0cW9en2xtuPg3Pa9FBh3Z4msa8Yu4qo1qnchpmzDfykPElwqnIGQNH7hLHV_v3RXV3Rlb2s_kFfCqPTDXdfCrhjyVbI19qzeY1orsghzGdh_RnZ9cOgmf3jk5indX764PAQyED33HCck3WhW9Hq1i9Hzb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری های جدید علی کریمی که بازخورد های زیادی داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/145445" target="_blank">📅 20:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145444">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007137e607.mp4?token=HQEG1oodojoqQg2Jo1ZgW42e5D83xL_lTA3Y-r9vVBnt9sz9uXRgbrO8MP76IyoiJ7IL8575PCgdUJzq5cCkiK5YXAKi7W_XwPc5PEHjtQqqCoxxwIlkeK-7nsse3ms7HvnR3TvDHVzWLw_MG7jlUPNhzdBcD3_lGAV5RSe4D7J54sc1aUqdCxxqU7BPRcNqg_aMnAmSgTAe6trHhZ6RODVZwEyEgAD8yHKVAgdgAvSSuWaaObIv1OTybH6MwnJmJS4BpA-hjvJ5nT8kHojp1hSt7m553YxIjqPVx_tPFvWCsS6RnQf6G9WPAQE6kJmFLgf79fvx834IBhPu4tS2BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007137e607.mp4?token=HQEG1oodojoqQg2Jo1ZgW42e5D83xL_lTA3Y-r9vVBnt9sz9uXRgbrO8MP76IyoiJ7IL8575PCgdUJzq5cCkiK5YXAKi7W_XwPc5PEHjtQqqCoxxwIlkeK-7nsse3ms7HvnR3TvDHVzWLw_MG7jlUPNhzdBcD3_lGAV5RSe4D7J54sc1aUqdCxxqU7BPRcNqg_aMnAmSgTAe6trHhZ6RODVZwEyEgAD8yHKVAgdgAvSSuWaaObIv1OTybH6MwnJmJS4BpA-hjvJ5nT8kHojp1hSt7m553YxIjqPVx_tPFvWCsS6RnQf6G9WPAQE6kJmFLgf79fvx834IBhPu4tS2BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به بریتانیا: کشور شما خوب پیش نمی‌رود.
🔴
فراموش نکنید که درصد بالایی از نفت خود را از تنگه هرمز دریافت می‌کنید.
🔴
و شما برای کمک به من آنجا نبودید. کشور شما برای کمک به من آنجا نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/145444" target="_blank">📅 20:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145443">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB74ON7LzHx9-kgrQGTVdBlEaf3pAw-AfYNqRMi0rrBmEe3TCMcA2hOhvRmfZcoUyqYYaMVWKtRNqJ75L2z6DgUn6iG1RFSlPk5uDUc7H3E1W_irA4jcnQPDgQNS30OQmOpZ5cnckxtfcY4TKvxt8QIn3liQ1TzYidhaMrfmltNpUtITs4p8HbCiHbdjHqPJPTAmGFzJ3pW7luPi2VmxEz2nx8pQ6xQhQ9-dz5LneDbeRcKEmSbwYivllZgfbLs-8TpVJ_PNQQmiMnqoA-nHRVxbvDDrVf8KXi_AhD_rWCfBFF7Oh9aWcQDY3bfmpTI40i_2tiZQNM_xYR_SSQfsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف خطاب به وزیر خزانه‌داری آمریکا: «قیمت نفت آتی عمان، بازده اوراق قرضه دولت امریکا و میزان ذخایر استراتژیک نفت را خوب تماشا کن.
🔴
قهرمان! هرچی زور داری بزن که در قیمت نفت آتی بیشتر مداخله کنی! چون کل حرفهٔ تو به این بستگی دارد. یا اینکه به تخلیه نفت از ذخایر استراتژیک بیشتر از حد خطرناک ادامه بده و سقوط غارهای نمکی ذخیرهٔ نفت در اثر کاهش شدید ذخایر را تماشا کن، یا به خداهای نمک تگزاس پناه ببر و دعا کن که چاه‌های ذخیره سقوط نکنند. دنیا پاپ کورن خریده و تو را تماشا می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/145443" target="_blank">📅 20:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145442">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کانال ۱۴ عبری مدعی شده سطح آمادگی و هوشیاری در داخل اسرائیل به‌طور محسوسی افزایش یافته است.
🔴
به گفته این رسانه، این وضعیت در پی نگرانی‌ها از احتمال ازسرگیری درگیری نظامی مستقیم با ایران ایجاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/145442" target="_blank">📅 20:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145441">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سپاه اعلام کرد که هفت نفر را که ارتباط با گروه‌های کرد در استان ایلام در شمال غربی کشور داشتند، دستگیر کرده است؛ این افراد در حال برنامه‌ریزی برای عملیات‌های مسلحانه و حمل مهمات بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/145441" target="_blank">📅 20:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145440">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیویورک پست: عمان به طور پنهانی پیشنهاد ایران برای دریافت هزینه از تنگه هرمز را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/145440" target="_blank">📅 20:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145439">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
هم اکنون حمله اسرائیل به حومه دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/145439" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145438">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
به گزارش بی‌بی‌سی، دونالد ترامپ تلویحاً اعلام کرده است که آمریکا ممکن است در مناقشه بر سر جزایر فالکلند از بریتانیا حمایت نکند.
🔴
ترامپ این موضع را به عدم حمایت لندن از آمریکا در جنگ با ایران مرتبط دانسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/145438" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145437">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل گزارش داد، «اسرائیل کاتس» وزیر جنگ این اسرائیل، با حضور «ایال زمیر» رئیس ستاد کل ارتش و شماری از مقام‌های ارشد نظامی، نشستی امنیتی برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/145437" target="_blank">📅 20:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145436">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روزنامه فایننشال‌تایمز گزارش داد بازار بیمه لویدز لندن انتظار دارد خسارت‌های ناشی از جنگ آمریکا و ایران در کشورهای خلیج فارس به حدود ۱.۴ میلیارد پوند برسد.
🔴
مدیرعامل لویدز گفت برخلاف حملات به کشتی‌ها در تنگه هرمز، بخش عمده این خسارت‌ها ناشی از آسیب به زیرساخت‌های زمینی است. از جمله، شرکت سعودی سابک در پی آسیب یک مجتمع پتروشیمی در حمله موشکی، در آستانه ثبت مطالبه‌ای حدود ۸۰۰ میلیون دلاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145436" target="_blank">📅 20:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145435">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نتانیاهو بار دیگر تاکید کرد : "ما اطمینان داریم که قادر به سرنگونی نظام ایرانی هستیم. این وظیفه اصلی است و به زودی به انجام خواهد رسید."
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/145435" target="_blank">📅 19:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145434">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d448ff03.mp4?token=nX02T68yqBjtu3zCqxGeuCzPqiEZkwpKpuJgZ1U7zLh2F2ebSRx7EFux_EUPGt7DKit88BJfhds2MffrdTV5agPF2DV4KCOTdPzPwYGv6HKlr41Yq79QmCGdSkRCHTYFQ9U5-ycyH7bqbnAk6xEfbhjSY9AF6USbptC7siaxrPAWEH6LNudSaW7t-WXHNcwr4JcOpgop1Vxd2wklZZFeGK6c8kQIN4n9EZL0iZCt7L3JupWh9r5TOuPB6NL0ciFQrW76rL4iZ8tRC6zUdW3H-V5SMj9s9ufjyVr8eeL-MLxwELOB_ua_D6grmdSoVpBGyEyFBfrSvFEiz_Uwp0IOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d448ff03.mp4?token=nX02T68yqBjtu3zCqxGeuCzPqiEZkwpKpuJgZ1U7zLh2F2ebSRx7EFux_EUPGt7DKit88BJfhds2MffrdTV5agPF2DV4KCOTdPzPwYGv6HKlr41Yq79QmCGdSkRCHTYFQ9U5-ycyH7bqbnAk6xEfbhjSY9AF6USbptC7siaxrPAWEH6LNudSaW7t-WXHNcwr4JcOpgop1Vxd2wklZZFeGK6c8kQIN4n9EZL0iZCt7L3JupWh9r5TOuPB6NL0ciFQrW76rL4iZ8tRC6zUdW3H-V5SMj9s9ufjyVr8eeL-MLxwELOB_ua_D6grmdSoVpBGyEyFBfrSvFEiz_Uwp0IOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا، مارک کارنی
:
ما از آنچه پیشنهاد شد یا از دوام آنچه ارائه گردید راضی نبودیم.
🔴
ما نمی‌خواهیم در کوتاه‌مدت به دستاوردهایی برسیم که چند ماه یا یک سال بعد از ما گرفته شوند.
🔴
این امر برای کارگران ما، شرکت‌های ما و جوامع ما منصفانه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/145434" target="_blank">📅 19:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145433">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
برنامه های هوش مصنوعی ChatGPT و Claude و Grok‌ و Gemini به دلایل نامعلومی از کار افتاده است.
🔴
تمام هوش مصنوعی های آمریکایی از کار افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/145433" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145432">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
مدیرکل فرودگاه بین‌المللی قشم از برقراری دوباره پروازهای مسیر دبی ـ قشم ـ دبی پس از ۶ ماه توقف خبر داد و گفت: نخستین پرواز این مسیر با یک فروند هواپیمای ایرباس A320 روز سه‌شنبه ۱۷ شهریورماه انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145432" target="_blank">📅 19:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145431">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
به گزارش سی‌بی‌اس نیوز، چند مقام ارشد آمریکایی گفته‌اند پیت هگست، وزیر دفاع آمریکا، در گفت‌وگو با افراد نزدیک به خود از شان پارنل به‌عنوان گزینه اصلی‌اش برای تصدی سمت وزیر ارتش یاد کرده است.
🔴
بر اساس این گزارش، پارنل در حال حاضر انتخاب مورد ترجیح هگست برای این سمت به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145431" target="_blank">📅 19:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145430">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / پرتاب موشک کروز ضدکشتی توسط نیروی دریایی سپاه از منطقه سیریک، ایران، به سمت تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/145430" target="_blank">📅 19:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145429">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2894def8.mp4?token=qM0m7x9I4p2JwYHsAIdnCnXBlLIPuqPggDNFfDQNp4nP9l-FZP4f63_hb35bcN0xqXCKNJmEMFmVihPEVA24z_RyIkyCKNVE9LtwmZ3Drzz2szFLvA4Dt1sdcX9RJbBv-C5WRVoyVvkJwBT8kulCKFZHFYawIRM_zQba9pdxHPEeBxHmLq8p4JmXEh7TOK09SmyW2gMY73CJQIosSk-0zFuBF20TRm1OWl-p15pijZhitxnirUrmdBFvlLejMRuX03uculqbNddRl_A1sDkzV8-0O7ywd3xdemP08su6GRSGu50-VigyIZ-tmsxlGg8CixuDL7-Yp9GjTmOP_V7eug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2894def8.mp4?token=qM0m7x9I4p2JwYHsAIdnCnXBlLIPuqPggDNFfDQNp4nP9l-FZP4f63_hb35bcN0xqXCKNJmEMFmVihPEVA24z_RyIkyCKNVE9LtwmZ3Drzz2szFLvA4Dt1sdcX9RJbBv-C5WRVoyVvkJwBT8kulCKFZHFYawIRM_zQba9pdxHPEeBxHmLq8p4JmXEh7TOK09SmyW2gMY73CJQIosSk-0zFuBF20TRm1OWl-p15pijZhitxnirUrmdBFvlLejMRuX03uculqbNddRl_A1sDkzV8-0O7ywd3xdemP08su6GRSGu50-VigyIZ-tmsxlGg8CixuDL7-Yp9GjTmOP_V7eug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای مهیب در پی آتش‌سوزی گسترده در افغانستان
🔴
وقوع یک حریق بزرگ در یک فروشگاه عرضه گاز و سوخت در شهر جاغوری افغانستان، منجر به سلسله انفجارهای پیاپی و هولناک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145429" target="_blank">📅 19:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145428">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
طالبان: تظاهرات نکنید، این در اسلام معنا ندارد و اتلاف وقت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145428" target="_blank">📅 19:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145427">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3352446383.mp4?token=Ou-lcDzP_dL3jtcxUQ5CAl85mU9yGcEIxl6DppgWxfN4MuSSx7tLFh6x86cAQCaBj3IafgPtmhYUBDSdVKaPaTNAbx71H_5Ft2PodtrIehPOfYmfNMkOE7f46A1LVvRi_cs7QzLzr0mmcFYNq36alWVAIk2YDvr9NIq_HlKSPd6oxAphP5KB1FfkM8w2CCd_3UNUZDWusp33c-zD_tDwyepUkGboti9wZVxlHgSl_57vrxqaOfIXn_cyl9Rg4y3jjRvVstG1OeqA4jrXPddJQ177wRe-xJtvw5VZ1IcLoqnbMOwwX3u-luUH540NoB5wD11JHd7sDLQ2GU1Lyk0i0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3352446383.mp4?token=Ou-lcDzP_dL3jtcxUQ5CAl85mU9yGcEIxl6DppgWxfN4MuSSx7tLFh6x86cAQCaBj3IafgPtmhYUBDSdVKaPaTNAbx71H_5Ft2PodtrIehPOfYmfNMkOE7f46A1LVvRi_cs7QzLzr0mmcFYNq36alWVAIk2YDvr9NIq_HlKSPd6oxAphP5KB1FfkM8w2CCd_3UNUZDWusp33c-zD_tDwyepUkGboti9wZVxlHgSl_57vrxqaOfIXn_cyl9Rg4y3jjRvVstG1OeqA4jrXPddJQ177wRe-xJtvw5VZ1IcLoqnbMOwwX3u-luUH540NoB5wD11JHd7sDLQ2GU1Lyk0i0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه رویایی را هنوز در سر دارید؟
🔴
وزیر امنیت ملی، بن گویر: امیدوارم بتوانیم مردم را تشویق کنیم تا غزه را ترک کنند، چه با اتوبوس، هواپیما یا کاروان. فکر می‌کنم این کار مشکل را حل خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145427" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145426">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdcaf90290.mp4?token=HjOHFp9hb6xF67q7tloDeI1PwV55RBhEM3fRnU7Kswf7Ut5wxcUFjJqC--jU-daIxjQ5Ep3CdiNV0lmQ3CRNm0-z8Z_afpepQHWcdjZ9oH8QCKhrGd6lhDuvs5ElYIewv6qmV4pXlp6gpNvzQAstS2qQRMJQVQXm_EIGdDvDl5OlR9LagIv30gx6nr8IoqXrDpETLddVMwCve_bBVPz5nMnWQYVKkaCO1e-oxdufPkHOvOSEjPxDoDEPmpHWTUDj3eZe1AZVd3Sg1tIvCxr_XHgg9uA5lqQUBSG1HY-mxi6ZHXNF55Yuu9c5BSbOeYJeYecVYRWwRgbER5VSa4xRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdcaf90290.mp4?token=HjOHFp9hb6xF67q7tloDeI1PwV55RBhEM3fRnU7Kswf7Ut5wxcUFjJqC--jU-daIxjQ5Ep3CdiNV0lmQ3CRNm0-z8Z_afpepQHWcdjZ9oH8QCKhrGd6lhDuvs5ElYIewv6qmV4pXlp6gpNvzQAstS2qQRMJQVQXm_EIGdDvDl5OlR9LagIv30gx6nr8IoqXrDpETLddVMwCve_bBVPz5nMnWQYVKkaCO1e-oxdufPkHOvOSEjPxDoDEPmpHWTUDj3eZe1AZVd3Sg1tIvCxr_XHgg9uA5lqQUBSG1HY-mxi6ZHXNF55Yuu9c5BSbOeYJeYecVYRWwRgbER5VSa4xRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گویر، وزیر امنیت ملی اسرائیل:
آنها واقعاً ده بار تلاش کردند تا من را ترور کنند.
🔴
من بیشترین محافظت را در بین تمام وزیران اسرائیل دارم و وزیر مورد تهدیدترین در اسرائیل هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145426" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145425">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cacff7873.mp4?token=MNrFVler75m_TZu2WyZqky5obJE6TVCS386MLO7Wx7MhFeJFnf6H5SXYFVpzxjgy4C8WC0X6oxqWu1B5dIoDWQ5PShQ7CsZcY8QQX0cSdbV1nlG4tc3n6lW8Xsen9f90u5OF1hF-Zjg4WrECn1Jd5mE1URqsCpgZ5Bn8_8SMYEx-ySDVZ-9ha8gjXBdBddbc1d14TVwTiP8pV_Cu41JA0KACT8Ehr2ZRV2HdOnNIQsmCCKJNGqEaVonLv57TGBd19lA43Q2JpH4_5rq2Ig5XLoIsacYpSqS1IpmVg_HwwEifglgeLTxCx6_QU7Qw3qJIMOT3Kvv15pM7iP9QbskFFWucmukWblFTyHcs6Y1Se4G-g9mJPqDfMwr0BHO1UpiDLea3vcKlLcTGxzoHrRmF-7z8vEuGK6nnsKpXhNpIP-IRTPfU7dSr-_06Di0y2DzrqSrC4vrc77e8lC8XQNdvgYsNQDUwahg8tlFfSu4SW_EuTEniKHz1KGtdCHMZ_z63ApNF7Hlr8xztCvxp1Mb4EnOJQ6TxC3vTZZBe1M2n6TuIuwnRgLmUKpoMyTzQ04DBtD-jkRnKLaCm3Sd3B1mUoHKYhQng3qwPu9Ma8q873G5bMnH9YikG4pOc0swcub_s76G3bJsc5ofbz3LaVvMXkuNzMUHw5P8091_lDoUwv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cacff7873.mp4?token=MNrFVler75m_TZu2WyZqky5obJE6TVCS386MLO7Wx7MhFeJFnf6H5SXYFVpzxjgy4C8WC0X6oxqWu1B5dIoDWQ5PShQ7CsZcY8QQX0cSdbV1nlG4tc3n6lW8Xsen9f90u5OF1hF-Zjg4WrECn1Jd5mE1URqsCpgZ5Bn8_8SMYEx-ySDVZ-9ha8gjXBdBddbc1d14TVwTiP8pV_Cu41JA0KACT8Ehr2ZRV2HdOnNIQsmCCKJNGqEaVonLv57TGBd19lA43Q2JpH4_5rq2Ig5XLoIsacYpSqS1IpmVg_HwwEifglgeLTxCx6_QU7Qw3qJIMOT3Kvv15pM7iP9QbskFFWucmukWblFTyHcs6Y1Se4G-g9mJPqDfMwr0BHO1UpiDLea3vcKlLcTGxzoHrRmF-7z8vEuGK6nnsKpXhNpIP-IRTPfU7dSr-_06Di0y2DzrqSrC4vrc77e8lC8XQNdvgYsNQDUwahg8tlFfSu4SW_EuTEniKHz1KGtdCHMZ_z63ApNF7Hlr8xztCvxp1Mb4EnOJQ6TxC3vTZZBe1M2n6TuIuwnRgLmUKpoMyTzQ04DBtD-jkRnKLaCm3Sd3B1mUoHKYhQng3qwPu9Ma8q873G5bMnH9YikG4pOc0swcub_s76G3bJsc5ofbz3LaVvMXkuNzMUHw5P8091_lDoUwv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گویر، وزیر امنیت ملی اسرائیل:
زندانیان تروریست از تمساح‌ها می‌ترسند. آن‌ها می‌ترسند.
🔴
من می‌خواهم آن‌ها بترسند. من این‌گونه می‌خواهم. این همان حکومت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145425" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145424">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
به گزارش اکونومیست، دونالد ترامپ توافق نفتی با ونزوئلا را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده و مدعی شده این توافق به آمریکا «سلطه انرژی» خواهد داد.
🔴
اکونومیست این توافق را جسورانه توصیف کرده، اما هم‌زمان نسبت به ابعاد و پیامدهای آن انتقادهایی مطرح کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145424" target="_blank">📅 19:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145423">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
معاون امور زنان رئیس‌جمهور: مصوبه صدور گواهینامه موتور برای بانوان نهایی شد؛ پلیس راهور مکلف به اجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145423" target="_blank">📅 18:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145422">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDdWTYJIq3tr_sBHJUafkXsRgl7_5HiiJeacU-k5_GI7RnoF6jhYx6Xb9-lTJFDd8qyvX_HQnA1t7Ji_zinHnce8CvEvV4DHzS0lNG4LZidKEq2FTmEbCP5XTBKV0CsgnNBr3Z7jCrF2KooACvbaZrQXboBXYJg3j81h-b-2azndhyo1nJM8ShYnV0vVcJlE4uIxkXIQMCeTkX_3hQb4hucBQbX1q3aFyVvocUnj5mJRpzeWRtxK1tjuRpDTgPGFgY0Wn_cP7eV-TbnVCM9KE_rN00fjLiV9cSjQlCQ-z8GOtd-DLrMPyjDQhtXGGewZ_qDG38lAqGCaVE08-3i3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «برای سیاستمداران کانادایی، مثل نخست‌وزیر کارنی، خیلی راحت است که دونالد ترامپ را «دشمن» معرفی کنند؛ اما وقتی اقتصادشان فروبپاشد، این کار از نظر سیاسی به‌شدت به ضررشان تمام خواهد شد؛ بدتر از هر اتفاقی که تاکنون برای یک سیاستمدار کانادایی رخ داده است
🔴
فقط تماشا کنید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145422" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145421">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCCIMiCPcMfVqT1GNN_6eMn8ECsru1Ci84seXyeqUnKq9E6D5jIwXY1t9OinD6eRWTyEVt5UpadEoivIl2HwA5HNj4Qnjvi0SRPMpTQ13IltjT4zfbc58Alyd2jdg07gkS0DDDKeTQbXS-WY2Ek3Sz0GW5xo61cB_QkMn7Xp460LBDkHdM5rZYnuOPKCmUq-dOGxanO4joJzBoXH8frA7XmmDjUPqXI3azjmXahy61t7Qdi4Iof2p-bVtqKean_JBLbsh6vZ30raiEiLr1YdMGN5grZYvXJ8prfynSDFEHoFsWWkot3MkAT4q1ifXtJWsABEp1BR9IcCcLAYnxnEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
افراد و رسانه‌هایی که مدام بر این موضوع تاکید می‌کنند که ما هیچ مهماتی نداریم (و آن‌ها ۱۰۰٪ اشتباه می‌کنند!)، در واقع خائن هستند.
🔴
آن‌ها این کار را انجام می‌دهند زیرا ترجیح می‌دهند ایالات متحده یک جنگ را ببازد، در حالی که ما به راحتی می‌توانیم آن را ببریم، تا اینکه من پیروز شوم
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145421" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145420">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: ما مقادیر تقریباً نامحدودی مهمات درجه متوسط تا بالا داریم؛ علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم
🔴
فروش سلاح به متحدان به زودی دوباره آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145420" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145419">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXYEQ1NG6tmzjXgPgH2Usjkl_wMPiIHtUGr-oLsyXlYBbHWXoRkpW9tGfjmCLrdO15UYDbSW0rGbFhxeGypKktJKmGofmc1_j9HA1A-11j4ZCG6bT1mJNlrqs_XUfAYeGCMEVpN34KsuHOSPj6iofE_KbRLbBHVxWJNBmELEHwYAYqCx4IGhRm-RQfBsM330Q3TfanQS_4A0g0gRfTrSfJCJm697aLEqpCJ19eHgzEqwirsJlcYe5B1N8B738xCWxcd8j9wfw5MLio1puHP3bFD0Q0HtNNgyuP_pUmfhWq1W2qJX_Zdg1NWfWiYz2ocZK30RrsjZcgjg41BMmMkCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ما مقادیر تقریباً نامحدودی مهمات درجه متوسط تا بالا داریم؛ علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم
🔴
فروش سلاح به متحدان به زودی دوباره آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145419" target="_blank">📅 18:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145418">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rw-upLGKv8Gr7NYj2hSJGFSYWgfxLmMLziGd8FyySeCwmrIFg6hU9hjQqfTDn_Y4a3sK9cnNkEw8RdtTl9UMO9KacbacJ_YwxUho8T27vTJJNCYxVtW9wv9UazADdI-cbIM69OfNLaY73S_dbhcln8Axpjt-CVPGa34s2WqWP70I1ZbBK20hkwuoM-5U3IrsQM1x6z8N625m2pneh77Wbb0QRuBYpBnrnbn_E5VxWTHw48cLjABKIkBoSjQp_quAO21J_V4M9-cXs6St-DBPJmQPk7ISzbfDiFpRS9-QxbS4FPnGKZdldQIqoLS7y_uRkgv4R9ygGiCTW9j3kEL1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در هفته‌های اخیر، ارتش روسیه به‌طور بیشتری به داخل روستای کوزاچا لوپان پیش رفته و همچنین به گسترش منطقه بافر خود در استان خارکوف در امتداد مرز بین‌المللی ادامه داده است
🔴
رسانه‌ها تصاویری از نیروهای روسی منتشر کرده‌اند که در بخش‌های جنوبی، شرقی و غربی کوزاچا لوپان پرچم‌های خود را تکان می‌دهند؛ همچنین ویدیوهایی از نفوذ پرسنل روسی به روستای کودیووکا نیز منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145418" target="_blank">📅 18:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145417">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رسانه اسرائیلی: موشک‌های ایران به هتل نیروهای آمریکا در اردن اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/145417" target="_blank">📅 18:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145416">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0432593c6.mp4?token=UOdqCNQGRlRdJ1FM0l3hfQa-ncHSu7KbmwPFyJuBMqb1pWGYywEJSZCxZh9sS4yHIGRiRpqBzOIkA-kNgcf1jXQeu4hTcXZuJRzOYK0GoWSiq8maaiHTkbGyfnpaB0EaSePQFUU9SMlP9l5iTWg2cdOBu80zBJdAE6L5cU8m6pUx0LrCExr-emFjgN1uPIF9epMNDaqJ2bDOhyV1LV_xp7oWGg9m844uCC9oG_m0eGth0lICm2HPhVoNcv4RAjUgEKXEWbuCOsGVSgQfdQweD0OzQ8HicMc_ZMk0ZsA4f8SAegSMo70OcPHQa5XIUy_y_6jWM8TvNF48g1sxh498eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0432593c6.mp4?token=UOdqCNQGRlRdJ1FM0l3hfQa-ncHSu7KbmwPFyJuBMqb1pWGYywEJSZCxZh9sS4yHIGRiRpqBzOIkA-kNgcf1jXQeu4hTcXZuJRzOYK0GoWSiq8maaiHTkbGyfnpaB0EaSePQFUU9SMlP9l5iTWg2cdOBu80zBJdAE6L5cU8m6pUx0LrCExr-emFjgN1uPIF9epMNDaqJ2bDOhyV1LV_xp7oWGg9m844uCC9oG_m0eGth0lICm2HPhVoNcv4RAjUgEKXEWbuCOsGVSgQfdQweD0OzQ8HicMc_ZMk0ZsA4f8SAegSMo70OcPHQa5XIUy_y_6jWM8TvNF48g1sxh498eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری مهم از آخرین ویدئوی منتشر شده توسط انصارالله که نشان‌دهنده اصابت یک بمب خمپاره‌ای پرتاب شده از راکت "روجوم" به یک وانت در حال حرکت است که متعلق به نیروهای حامی دولت قانونی یمن (PLC) می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145416" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145415">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92a85e0ae.mp4?token=fYEtdC5Y2vr-2_QNJjgZMr1afNq8sFG5lSGy-WXcvCvmY5Ve4PxXaNeyCpHTUzPy8xF4dvn5p8KdC9tIgwlfBFCb2xBibvFRw34mf2yPlwv4ar6jCV_DErpjUcLu3CW27NFeLquWbgKwogj0CmAwHae8U5rAqgwP60jmw3j9DcD7BO_9E6d2NeuRo96V9VYFatkPFKXyY7zMuz_HLszv-jpSEl0ffV4QVhejvYOXy-Uk8IWDSJf6JvGAXuv29RXMHm8ObB_gbpvG3gXNLqNGW8nN8FgfrhpuQshxOFWjoLuEJlkncNDu43PTeNSLEKUAKpazVacrbhJh3OqYTEpaKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92a85e0ae.mp4?token=fYEtdC5Y2vr-2_QNJjgZMr1afNq8sFG5lSGy-WXcvCvmY5Ve4PxXaNeyCpHTUzPy8xF4dvn5p8KdC9tIgwlfBFCb2xBibvFRw34mf2yPlwv4ar6jCV_DErpjUcLu3CW27NFeLquWbgKwogj0CmAwHae8U5rAqgwP60jmw3j9DcD7BO_9E6d2NeuRo96V9VYFatkPFKXyY7zMuz_HLszv-jpSEl0ffV4QVhejvYOXy-Uk8IWDSJf6JvGAXuv29RXMHm8ObB_gbpvG3gXNLqNGW8nN8FgfrhpuQshxOFWjoLuEJlkncNDu43PTeNSLEKUAKpazVacrbhJh3OqYTEpaKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
گوشی اقتصادی a17 سامسونگ از ۱۵ میلیون پارسال، شد ۹۷ میلیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145415" target="_blank">📅 18:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145414">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان مدیریت بحران کشور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRX58hKgqIMTqJgsMeLfZ1Ve-UB-O7AQCf0BLJa7g66qRnoSAvc1hWAYWVbEN4vZ8-FmfyEgZiuk0tkorJ0YHY31pidJa6ghfmrQqjWROSc6g0t5i7s51GlabouK0cFfTwIuKLgg9xBCjtDcRTyh1CgTkbKiDimHvBsZ_762Ffw1ZauehR5Mb4mxiI0-YnH9jNXoEK3Xrx6MFkT_n4nt60HFXlE9UjjUmG4TgJ2GRaD5Y39E5doq4bJvTfzmijXCpjmzWpU9AGdJgAn-fMkdBF5zTqj1GwaQTFQl78Ec69nNhkoWNdHD3RsHap8OAAd4meiDgjFX5UFbSQRcRvABbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه بانک مرکزی</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/145414" target="_blank">📅 18:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145413">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
جنبش انصارالله تصاویری را منتشر کرده است که نشان می‌دهد نارنجک‌های خمپاره‌ای از پهپادهای "روجوم" به سمت نیروها، وانت‌ها و خودروهای زرهی طرفدار شورای انتقالی جنوب یمن (PLC) در نقاط مختلف خط مقدم درگیری بین انصارالله و PLC پرتاب شده‌اند.
🔴
خودروهای زرهی مورد اصابت شامل یک تانک اصلی مدل T-62، یک نفربر زرهی مدل BTR-40 و یک خودروی گشت زرهی مدل BDRM-2 هستند که همگی از نوع خودروهای زرهی طراحی‌شده توسط اتحاد جماهیر شوروی سابق هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/145413" target="_blank">📅 18:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daad725d95.mp4?token=BD__ohuxccMZv-4WiyFCGlE68KSmkKOavrWdWMM0RMKxC88G29xQqDGu-lisJkPd260ChHwsdr_jciUJlU8N0LEPpMBL222ymzd1CX13EEeLCOKE7fbIVeBn011KANhcfr3XNGeppZeBjoyFOZ9hRlQ2losuH4y08i6LB7BRaouSomsGm6CHOQgWkuNWSjfOr4lBOH7b31fUtx_soZqDBov0wT63NASWfQKT33axeRNXJtKJJOlpq6y_VJsyjLnhPN2vbTucTO3J5Q5YTUt2817iBwxsjOWtIctkaYoip7JVKY-mjVyZyqkGvBq3Cbs5lQKsJhk7YKISQlPPIqKOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daad725d95.mp4?token=BD__ohuxccMZv-4WiyFCGlE68KSmkKOavrWdWMM0RMKxC88G29xQqDGu-lisJkPd260ChHwsdr_jciUJlU8N0LEPpMBL222ymzd1CX13EEeLCOKE7fbIVeBn011KANhcfr3XNGeppZeBjoyFOZ9hRlQ2losuH4y08i6LB7BRaouSomsGm6CHOQgWkuNWSjfOr4lBOH7b31fUtx_soZqDBov0wT63NASWfQKT33axeRNXJtKJJOlpq6y_VJsyjLnhPN2vbTucTO3J5Q5YTUt2817iBwxsjOWtIctkaYoip7JVKY-mjVyZyqkGvBq3Cbs5lQKsJhk7YKISQlPPIqKOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی اوکراین امروز، یک عملیات تهاجمی با استفاده از پهپادهای دریایی علیه کشتی باری روسی به نام "نفریت" در شهر بندری سوچی انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145410" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145409">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یه قاتل فراری تو بیمارستان شناسایی میشه و اینجوری با چاقو چندتا مامور رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145409" target="_blank">📅 17:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145408">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
روبیو: یه زمانی واقعاً این تصور وجود داشت که کل دنیا تبدیل به دموکراسی‌های مبتنی بر اقتصاد آزاد می‌شه و همه کشورها شبیه ما خواهند شد.
🔴
اما واقعیت چیز دیگه‌ای رو نشون داد.
🔴
کشورها و دولت‌های ملی هنوز اهمیت دارن. ملی‌گرایی هنوز واقعیه.
🔴
مرزهای کشورها هم همچنان اهمیت دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/145408" target="_blank">📅 17:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145407">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cceb2210.mp4?token=oWsIR-itLJG0DiW_Wd2mDCR6nLC0hN540KSPKoX1G0IUEdQxSDGMDN13OZKktT6U65yl19QGhpAHccEgFjkZSM-hO6yCfmy1fAjhPxIvupqCyCRf5xVHiSeF838-ZGEzIw0GXrliYPrnjXKWl4taGY8mBH6VKiJviGTahnFNbp7UY1OGx9xP3GwDAOGx8JjYYZk1Itge7-WNjHBvOB2_1VtRXbJq6N1wHjNFP0tsU9c4G5OUtWJntjrzvKQAa-yoXlKRrLFHQpGAfrxGR4vNUJUMNd7fRulMhsp3-4W69yzSeqG7Aqi0qM7PyfY53cGJKXqt_9P8dYJdL6_9490wAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cceb2210.mp4?token=oWsIR-itLJG0DiW_Wd2mDCR6nLC0hN540KSPKoX1G0IUEdQxSDGMDN13OZKktT6U65yl19QGhpAHccEgFjkZSM-hO6yCfmy1fAjhPxIvupqCyCRf5xVHiSeF838-ZGEzIw0GXrliYPrnjXKWl4taGY8mBH6VKiJviGTahnFNbp7UY1OGx9xP3GwDAOGx8JjYYZk1Itge7-WNjHBvOB2_1VtRXbJq6N1wHjNFP0tsU9c4G5OUtWJntjrzvKQAa-yoXlKRrLFHQpGAfrxGR4vNUJUMNd7fRulMhsp3-4W69yzSeqG7Aqi0qM7PyfY53cGJKXqt_9P8dYJdL6_9490wAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: نمی‌شه یک اقتصاد رو کاملاً بر پایه خدمات اداره کرد.
🔴
باید یک پایه و اساس از تولید و ساخت کالا هم داشته باشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/145407" target="_blank">📅 17:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145406">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
چین: به شدت از تحریم‌های مرتبط با ایران که علیه ما اعمال شده، ابراز تاسف می‌کنیم و قاطعانه با آن‌ها مخالف هستیم
🔴
از آمریکا می‌خواهیم فوراً رویه‌های نادرست خود را اصلاح و تحریم‌ها علیه شرکت‌ها و افراد چینی مربوطه را لغو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145406" target="_blank">📅 17:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145405">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه الجزیره گفت که پایگاه‌های نظامی آمریکا در این منطقه، از جمله پایگاه‌های مستقر در کویت، در جریان حملات تلافی‌جویانه شب گذشته ایران، "تحت هیچ‌گونه حمله‌ای قرار نگرفتند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145405" target="_blank">📅 17:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145404">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mwCd2Kxr_-0duFSgGtQULoXEAnn02RyX5ySQCC-Yb5FPQL0SBE9GrXlVJsR8xgkXQ87nDOTcdyhD4NBwU-S6JchjlhnoTpmGfgh2j-svk8ktQaUUUHzlY9vj2UDr8nw_QhyKzOAMTNf2zmiIzNdkUjU4_MfFkZG6HMVRZEPsZwSsYdAUXChs20QviFvZPpIGa6wGXu235W4dOKk_-2pCHHFIzgxUpwSzPOEWdfPlI7fUuUipOQZzYwXlP-SFsEvtHXwkACniK9uK8Hn2JA3IRWxIAVIVK1A0HGYev9tE8CXTtpjH-HnfrsTRRNYRnS0dc9AQ2tKIdHBv9L4brLAXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان حمایت مالی جدیدی از بانک مرکزی یمن متعهد شده که هدفش تثبیت اقتصاد یمن، افزایش شفافیت دولت و حمایت از توسعه اقتصادی و اجتماعی این کشوره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145404" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145403">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بقائی خطاب به بسنت: تاریخ فراتر از خاطرات حیاط پشتی خانه شماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145403" target="_blank">📅 17:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145402">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رویترز درباره ۳ گزینه ایران در صورت ازسرگیری جنگ
🔴
از حمله به تأسیسات نفت و گاز، نیروگاه‌ها و آب‌شیرین‌کن‌ها تا تهاجم مستقیم یا غیر مستقیم در کشور‌های غربی
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145402" target="_blank">📅 17:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145401">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری/سخنگوی قرارگاه خاتم‌ الانبیا:
عملیات های تهاجمی علیه آمریکا ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145401" target="_blank">📅 17:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0i2YufL9jxE-J8Onxcjd5iARFDPY_QNs88gusc4odaEBpSlUqyYe1eMD-cmaahKYyPZL7wMuF7u2oQWjTiyy9ls2vaRnku0zhCRGhQudkqb3njRv6n8EzZg3nCmHddI6xaaYHj-9OJC9dJkrQ86h-dycZaBxou8ghB56O_MVQZ4S8HpNFGUcD7ADSUcD7vxyb9T7mdLC43H59qgqJsrG7jraAbBuKHAkViZRA7qnlbeneAjnnRogt9FNp8GTdOWFujB5iDXBI_WVBMIZibGg4tyHr_tkeEZVeAyxLFXBeK55iXUHbKXX4OL_nwfKgm8BjL88s4sAkrT0zSykxQBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAhcW_vsCZDZLwP9Vl_ux1p-c5-oXJMitLPFiC84MUEcp-P1Tjqctc0THcSbxQvNlf1FOlwDFZdN4yokccxfZf3vGi6h0k_-Q-MQVOMOknm-4EdEhYvGvTc9V1HYDZf2l9kvzLfhj6vHALFjaRb_47-9wjgKpqD1O_oWvQxVmI-_TsvrA1lyitDSi-_QxwibuyhIEWI8d5gTEeaNsVocOHggS7GxISJxVu6fNw61yn6dxhc3HZNkhoagjlEtMJzE99kOZPg23SPLUEpR6cowKlDCcKpXiGQWfVKCjXvpRRVsCU6-FQ0PdXmVq3xSYWtesGQdu-OuvrG9o0jRK_H0tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد انتحاری هدف قرار دادن یک مخزن نفت در پایتخت لیبی، طرابلس، در نزدیکی فرودگاه شهر را بر عهده داشت، اما نتوانست به هدف خود برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145399" target="_blank">📅 17:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c3ba818c.mp4?token=jdc3pxJXikPpubs63zqPs2UUN6-E4gmOqNdRmC0u8683fGx1FuuI1AOhTJRpK_Q3gQlKZD9Ou6M6-0kmXkpQCIM77qeH574kJd2EwfgW749VWHo1fesztTBrJJGt8GaFoEqqD0izTcU81SkLLjC-EjUgJ0ghxjFPOyqUKB6LPVwc67xIBi339BAdyQE3VYYQBc19fEzUovPS30JbtymBZskuZqySQ8K0mv_T45H0t9KqitE26g2FEiOurQZXLVlkwrDnViLA-CtRkwDWPnFUpEiy0CM47k3aXHfwQ8igmSD2ccqTuLI0kFUJykP9-vFQwQtavIIKYO5VWzhL8ZA-gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c3ba818c.mp4?token=jdc3pxJXikPpubs63zqPs2UUN6-E4gmOqNdRmC0u8683fGx1FuuI1AOhTJRpK_Q3gQlKZD9Ou6M6-0kmXkpQCIM77qeH574kJd2EwfgW749VWHo1fesztTBrJJGt8GaFoEqqD0izTcU81SkLLjC-EjUgJ0ghxjFPOyqUKB6LPVwc67xIBi339BAdyQE3VYYQBc19fEzUovPS30JbtymBZskuZqySQ8K0mv_T45H0t9KqitE26g2FEiOurQZXLVlkwrDnViLA-CtRkwDWPnFUpEiy0CM47k3aXHfwQ8igmSD2ccqTuLI0kFUJykP9-vFQwQtavIIKYO5VWzhL8ZA-gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بابک زنجانی: ما تا یک سال دیگه بیشتر زجر نداریم؛ یا در این یک سال از نظر معیشتی نابود می‌شویم، یا قدرتمند می‌ایستیم و از این یک سال عبور می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145398" target="_blank">📅 17:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی کرملین در واکنش به درخواست وزیر خزانه‌داری آمریکا برای دوری از ایران تأکید کرد؛ مسکو روابط دوستانه و شراکتی خود را حفظ می‌کند و توسعه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145397" target="_blank">📅 16:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145396">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7246d9a0a0.mp4?token=DbwUqI4LV0XTmfuYXdrKs9iRg_Ju0oMypEFmA3RvMixmXHGT0aVIzCrqZh-LsBJ0-FOQGQ5JqYv6BdzW5gesldeRQb5R3N10y00CsLGkKlphZAQTCNuDd-Op9Dq0NV4Cb-XG4ETZSMqFwbcHs79cY2YMYdzz061e9NDkY1kU7QhTkQi2ZyD99I-RtwbKXUc-uAm7cFLy7h_jVZ4MzeNN7ECD2H2VNAQiN7PBdh8PQIBlDgfQhwq5XhXR0ZjHZqojPiNip-DbNALKcHHvgsjxEawyyXiHj_02coIttqKlhTM2Sc8udqBEHfb6wvr6oZ1vXa74rGY05SWN3NKGshyatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7246d9a0a0.mp4?token=DbwUqI4LV0XTmfuYXdrKs9iRg_Ju0oMypEFmA3RvMixmXHGT0aVIzCrqZh-LsBJ0-FOQGQ5JqYv6BdzW5gesldeRQb5R3N10y00CsLGkKlphZAQTCNuDd-Op9Dq0NV4Cb-XG4ETZSMqFwbcHs79cY2YMYdzz061e9NDkY1kU7QhTkQi2ZyD99I-RtwbKXUc-uAm7cFLy7h_jVZ4MzeNN7ECD2H2VNAQiN7PBdh8PQIBlDgfQhwq5XhXR0ZjHZqojPiNip-DbNALKcHHvgsjxEawyyXiHj_02coIttqKlhTM2Sc8udqBEHfb6wvr6oZ1vXa74rGY05SWN3NKGshyatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خدمه‌ ناو هواپیمابر آبراهام لینکلن که چندین ماه در خلیج فارس و چندین ماه در ونزوئلا حضور داشتن ، به تایلند رسیدن و رفتن تا پس از یکسال در دریا بودن چند روزی رو در خشکی عشقو حال کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145396" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
معاون ارتش: توانمندی حملۀ پیش‌دستانه را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145395" target="_blank">📅 16:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
یک مقام آمریکایی: پایگاه‌های ما در هیچ کجا، از جمله کویت، در حملات دیشب ایران مورد اصابت قرار نگرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145394" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145393">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بلومبرگ: اگر قیمت‌های بالای نفت تا تابستان ۲۰۲۷ ادامه پیدا کند، بهای بلیت‌های پروازی در اروپا به طور محسوسی افزایش خواهد یافت و برخی شرکت‌های هواپیمایی ورشکست می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145393" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145392">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو اعلام کرد که ۵ غیرنظامی لبنانی در ازای آزادی اجساد یهودیان در لبنان، آزاد خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145392" target="_blank">📅 16:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145391">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
احمد وحیدی فرمانده سپاه: انتقام جان باختگان نبرد هرمز را می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145391" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145390">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پوتین: نخستین محموله نفتی از مسیر قطبی ارسال می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145390" target="_blank">📅 16:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145381">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgeVzeNbjeekI19k2jSbZm9ILeyJZ_vuBo3nvduWyA51j--8YHI4yhcNdJfUgifekpFlyfZsz3EN129ZpEZ13E5xh3FdWr0mbB59ujcfHsfsDPKday-WLgn0CrEo7my43sCl3z74DjPr7HSVLkPv5ESNLdnw6LcK9vbBqAQMU_DtSXoEmH2k1jk09efMA-Dis2JflWfkiKpmaMMZef5oeu8VJ1FKi1AZ4bGQyLwR7dgMDzhJ4grnNepbGdYJb4dVpyQHJj_5AspRPkH6TreBHNjQM4cpsQfCYZQkNWSbd3LP7UdxglJs4J5shWG9eIwJ9ma64_vAuSiEn8AoJ5nJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4abdcbc674.mp4?token=Ie7LMRwxDlWPqfqUXtH0s86E6Y_QOVlZvRbMUE0UacH3FObLSlPgp-Zfq4BHj_rFEKmwFPsDxGYsbYV6pXjewETVumITotOmcrAxiQcMNoPe3Ud96drfMByQoLwXWXsKCeI93zCrDVnobwBP7A_e3nqSdhZgVaE_au3ZEn22oLfbDzeSEjvTjycav0hCUfMxzYS7vR7LRZ29T-gcpvIFIaG1XGKEoHV9rL2nET5HTfenJqOii4SlwFwU5_0CW7saGsDPzGXawNKyfOv48iPigv9WMsfAs_WkclZWRDsdaTJuFS9oXrE9fan5Q58Xc60iXwVwlpOhQv4qsqlzCrOP3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4abdcbc674.mp4?token=Ie7LMRwxDlWPqfqUXtH0s86E6Y_QOVlZvRbMUE0UacH3FObLSlPgp-Zfq4BHj_rFEKmwFPsDxGYsbYV6pXjewETVumITotOmcrAxiQcMNoPe3Ud96drfMByQoLwXWXsKCeI93zCrDVnobwBP7A_e3nqSdhZgVaE_au3ZEn22oLfbDzeSEjvTjycav0hCUfMxzYS7vR7LRZ29T-gcpvIFIaG1XGKEoHV9rL2nET5HTfenJqOii4SlwFwU5_0CW7saGsDPzGXawNKyfOv48iPigv9WMsfAs_WkclZWRDsdaTJuFS9oXrE9fan5Q58Xc60iXwVwlpOhQv4qsqlzCrOP3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای داراویش که به رئیس منطقه برکنار شده، لافتگاری، وفادار هستند، امروز صبح یک عملیات تهاجمی علیه نیروهای فدرال حامی سومالی و شهر بیدوا در منطقه جنوب غربی سومالی آغاز کردند.
🔴
نیروهای حامی لافتگاری در ابتدا به عمق شهر نفوذ کردند و یک پایگاه نظامی فدرال را به تصرف خود درآوردند، اما پس از یک نبرد ۴ ساعته، عقب‌نشینی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145381" target="_blank">📅 16:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145380">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bihtj0XrIk1VGQWFxRFRUzWD2dmCqiQ1kteIqFSgvDMrG9elHFQbimNBOL28Rvq6aSu0k_pkIV1NqguM1X-FTNNKYkB_9Y2iWQh51LYuys-Tp-wB2fiBs0DaKENgRjQl3eYXXmVgKCMtF5mWqtBQ5a1wdZ4VsTg9nD4DVByWf76zbOk17shFVXQFgbdlRTyFt4SiwEKWcP9W1eqYZOWeeKXK47PQlghq2dGiWYS-T7SGCiYGFjIae3EM7lnFIsZiiciiZSkFNLK_HPy8HFqZ5aKoIVMWlV59JagYI7BHJ9x--0tAvaRfjuCG1LJooNEHoJZ3VZNUOXy0zfceDdLlOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش بی‌بی‌سی، دونالد ترامپ، رئیس‌جمهور آمریکا، برای مدت دو روز از تاریخ ۱۲ سپتامبر به ایرلند سفر خواهد کرد.
🔴
قرار است او با کاترین کانولی، رئیس‌جمهور، دیدار کند و قبل از سفر به اقامتگاه گلف خود در شهر دونبیگ، واقع در شهرستان کلر، مذاکرات دوجانبه‌ای با مایکل مارتین، نخست‌وزیر، داشته باشد.
🔴
کانولی پیش از این از ترامپ و سیاست‌های ایالات متحده در مورد غزه انتقاد کرده بود و او را "زورگو" خوانده و او را "ناپایدار" و "غیرقابل پیش‌بینی" توصیف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145380" target="_blank">📅 16:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145379">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سپاه اعلام کرد: در حمله دو شب پیش آمریکا به کرمانشاه، یک فرمانده ارشد موشکی، سردار جعفر کهریزی ترور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145379" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145378">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ff31f76e.mp4?token=UnKW7umI-c3Z-_zdoFY-OIgkpB_Nivj_JsU_mQ7q85a7uGstpeDXVCqDgjhfEuMf5a8utUHjW5hjo6E2OlyUt8PjdnAzQfXpnnYPJMhjrir4BCoj5n2I-5cUhHnLkTRLDVqMfN9k86fRjpv5jIPjcK5eHhuo-t4rGCHRXFpncNPuLrUKp1SgQ5dKv1awqqxHg-yN2voFYAs-gfmThW7r_SPxwlysmme2waHzd5_52L0LX-XvIvJxEjAyuelJKD4aV_ufi24bjWeeObB5Sf_gRbRgzbuRTVXIksSfl2X7QERv95QGJ1dxUZDK1vWncNTXBouW08d88nLxJQyqzujH6HSQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ff31f76e.mp4?token=UnKW7umI-c3Z-_zdoFY-OIgkpB_Nivj_JsU_mQ7q85a7uGstpeDXVCqDgjhfEuMf5a8utUHjW5hjo6E2OlyUt8PjdnAzQfXpnnYPJMhjrir4BCoj5n2I-5cUhHnLkTRLDVqMfN9k86fRjpv5jIPjcK5eHhuo-t4rGCHRXFpncNPuLrUKp1SgQ5dKv1awqqxHg-yN2voFYAs-gfmThW7r_SPxwlysmme2waHzd5_52L0LX-XvIvJxEjAyuelJKD4aV_ufi24bjWeeObB5Sf_gRbRgzbuRTVXIksSfl2X7QERv95QGJ1dxUZDK1vWncNTXBouW08d88nLxJQyqzujH6HSQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاوروف درباره اروپا: برای نیم هزاره، یعنی بیش از ۵۰۰ سال، اروپا منبع اصلی تمام مشکلات و بدبختی‌هایی بوده که گریبان بشریت رو گرفته.
🔴
اروپا منشأ دو جنگ جهانی بوده و همچنین منشأ وضعیت فعلیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145378" target="_blank">📅 15:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
لاوروف درباره ناتو: ناتو باید خودش رو منحل کنه
🔴
درست مثل پیمان ورشو که بعد از فروپاشی اتحاد جماهیر شوروی منحل شد.
🔴
اما این کار رو نکردن. اول، اتفاقات افغانستان رو بهانه‌ای برای حفظ این ائتلاف نظامی قرار دادن
🔴
بعد، وقتی اون ماجرا هم برای ناتو به شکل فاجعه‌باری تموم شد و از افغانستان خارج شدن، تهدید روسیه رو جایگزین تهدید شوروی کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145377" target="_blank">📅 15:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145376">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5ca249cf.mp4?token=mh_fhKh5vm2sY6U2nhF2B2_31SEZVR8MlG6d2Shwr-ixYScHWQu_s8waULZIRN4dFh849uuLADQ417hlF82-sZRiu6WAqYhNox3H7qpXmbbXaZyoLxGbxgRsAayeBzquj4PCZfI1ltEFUxf3H8A1xgFDqnJAJITuraYPqCmv5Cmyl7YJk1bY9YIet6cSHwMwyC02dL6k1BwGsk-427vHXA3juBjRNTvXZzoD8mk2MA7gipkyjV3j5IDBCI9Rf9_zCORFj8Xo6yhmXVVbXtzizjErM9hfZtcsZUjpc8fYF1Wn_QyADqDfg6GyjbA_X-pXEXpQabNqyB9n3bOj39G4TjuOt_ehfwFCzjSESUt9ZewsrV7oouQM18FDmBtU5x1ScnlYSAiOqBXsoUM2Y1w0vap2ykJ9zmLMwQsUwmbqhNEEfjt7iER1x7_L1p3aQSTepScBAN7QS-Z_PKSYhfDyO8rwprwXQfIwMHRHjmcFgXE9GHeTAfVPEUhqqOhNhxag6U7oeOYH_w9RKK9vViayr--_rx63TIXSSOYpfNcZM2B8CkS0K3NmRAMN2aJ177Xr5N5rCBXpGS1LgSNTAxIrOPw4aXM1Ge3-3ZFDLI-WbNvj2SESYTHRl_ebpzV1mB3ajyt4wAy1mAxbk5YkLMoQnOvGyKWEXWQ6BzkXQ64oKrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5ca249cf.mp4?token=mh_fhKh5vm2sY6U2nhF2B2_31SEZVR8MlG6d2Shwr-ixYScHWQu_s8waULZIRN4dFh849uuLADQ417hlF82-sZRiu6WAqYhNox3H7qpXmbbXaZyoLxGbxgRsAayeBzquj4PCZfI1ltEFUxf3H8A1xgFDqnJAJITuraYPqCmv5Cmyl7YJk1bY9YIet6cSHwMwyC02dL6k1BwGsk-427vHXA3juBjRNTvXZzoD8mk2MA7gipkyjV3j5IDBCI9Rf9_zCORFj8Xo6yhmXVVbXtzizjErM9hfZtcsZUjpc8fYF1Wn_QyADqDfg6GyjbA_X-pXEXpQabNqyB9n3bOj39G4TjuOt_ehfwFCzjSESUt9ZewsrV7oouQM18FDmBtU5x1ScnlYSAiOqBXsoUM2Y1w0vap2ykJ9zmLMwQsUwmbqhNEEfjt7iER1x7_L1p3aQSTepScBAN7QS-Z_PKSYhfDyO8rwprwXQfIwMHRHjmcFgXE9GHeTAfVPEUhqqOhNhxag6U7oeOYH_w9RKK9vViayr--_rx63TIXSSOYpfNcZM2B8CkS0K3NmRAMN2aJ177Xr5N5rCBXpGS1LgSNTAxIrOPw4aXM1Ge3-3ZFDLI-WbNvj2SESYTHRl_ebpzV1mB3ajyt4wAy1mAxbk5YkLMoQnOvGyKWEXWQ6BzkXQ64oKrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله بالگرد روسی به پهپادهای اوکراینی
🔴
تصاویری منتشر شده که ظاهراً خدمه یک بالگرد Mi-28 نیروی هوافضای روسیه رو در حال درگیری با پهپادهای اوکراینی و منهدم کردن اون‌ها نشون می‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145376" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: این فوق‌العاده است!
🔴
سوریه خود را به عنوان یک جایگزین برای تنگه هرمز معرفی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145375" target="_blank">📅 15:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiU1Gb_BBgsawa-iA1-ExijmMKlKWvjNDXA-FcTT6o9BPo2kbbqTc8l_MjQCnE2OtmLJtOlx7pqn6E8lruHoElNgxus392dAU3II-ST1gEOUVap6zax5WbMTvnl4lTkyiX_8uFM_dRbtCyZQPBUu-W0GrTDMdl_uh3R11TyUiOzHNXAhPXjVSehg63xOydkdNdBTJeVBzF0LPvmlyAIOT0O-U81XYIECCOLsq_UF241fqkN2f8aFX-v4Lh-rBXgm8v9Zg4kY4fhEp508fUN3j_EfTdjfnT1um7zsRjbZ-NmuF5I9AIXkKywoL79P-yfy3CRRPEyfla5f_qEZwM0Haw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور ترامپ به طور مستقیم متعهد نشد که از بریتانیا در مورد جزایر فالکلند دفاع کند
🔴
وقتی شبکه خبری GB News پرسید که آیا ایالات متحده به کمک بریتانیا خواهد آمد، او به جنگ سال 1982 اشاره کرد، از بریتانیا به خاطر "بازپس گیری قاطعانه" این جزایر تمجید کرد، اما تأکید کرد که این جزایر "خیلی دور هستند" و اعزام نیرو به آنجا "سفر بزرگی" خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145374" target="_blank">📅 15:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145372">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d196d38e2f.mp4?token=X78LCnVTRvWrt6G_42dsj6NldvRhlxAtxKdMlv_QeJTSMw0zO_WwnmEmiPE-fVwy1imbxcsx-oElDsVbscjQjUX-LZcJpyuurpbJwRPWSH0ibWgrnq9E2Mu7kSXOlh-X4YGGQUSgN-BtQ8e4yr-5ndXiWGjLaaE7WaO0u1tXIW5fFmsrlr60Z-F_5QQvtWBvrvqbq9W1QZtfnoRu3bEsMAQOPAPFlffXoUnOXfDL8xSWXVx16os3mCWp7W_0bAUvj8tgQIPLMFWzKb8p9T01khQ3KKi-zNOiJxCetVXgtRg68s4Oe6BvwAa0vxHI412UwAzwhcq57gXrNAst60jV8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d196d38e2f.mp4?token=X78LCnVTRvWrt6G_42dsj6NldvRhlxAtxKdMlv_QeJTSMw0zO_WwnmEmiPE-fVwy1imbxcsx-oElDsVbscjQjUX-LZcJpyuurpbJwRPWSH0ibWgrnq9E2Mu7kSXOlh-X4YGGQUSgN-BtQ8e4yr-5ndXiWGjLaaE7WaO0u1tXIW5fFmsrlr60Z-F_5QQvtWBvrvqbq9W1QZtfnoRu3bEsMAQOPAPFlffXoUnOXfDL8xSWXVx16os3mCWp7W_0bAUvj8tgQIPLMFWzKb8p9T01khQ3KKi-zNOiJxCetVXgtRg68s4Oe6BvwAa0vxHI412UwAzwhcq57gXrNAst60jV8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش‌ها، یک فروند هواپیمای جنگنده مدل SU-25 متعلق به نیروی هوایی سودان در منطقه بارا، واقع در استان شمال خردفان، سقوط کرده است
🔴
هنوز مشخص نیست که آیا این حادثه به دلیل آتش دشمن یا نقص فنی رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145372" target="_blank">📅 15:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145369">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419c823c3e.mp4?token=me_6NdNDwR7N6zueL4UrphpAXJGqG3H1lqt2wqTbtXpdP0maYa9UQYxaXWxZGalU9EHWbqw5ZUMz2CzUXLBR0R_DYN7qSUA3CVhcoHvRQFKI6Zzi3b9OKqnVtutekh4wLo6qVsfCg2psq015HRXuqepMd3ZOTnSqsSnB3A8-ZK84pHX-TkgKondG3VEybZVgxMtgyOoAl5Sq5pTj-_6Gvj9GkfN4gRHmtwCvQ1bavdNKBKtQbBeURZLT_9mN3J3MjoDjfAgikT5e6edNTzd3ZbfDDYO_xcyl_saeg6U8ICm9mEOYdx1jzBkp96MSCyYe8cwrDDt9SEC0vep2gx0yWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419c823c3e.mp4?token=me_6NdNDwR7N6zueL4UrphpAXJGqG3H1lqt2wqTbtXpdP0maYa9UQYxaXWxZGalU9EHWbqw5ZUMz2CzUXLBR0R_DYN7qSUA3CVhcoHvRQFKI6Zzi3b9OKqnVtutekh4wLo6qVsfCg2psq015HRXuqepMd3ZOTnSqsSnB3A8-ZK84pHX-TkgKondG3VEybZVgxMtgyOoAl5Sq5pTj-_6Gvj9GkfN4gRHmtwCvQ1bavdNKBKtQbBeURZLT_9mN3J3MjoDjfAgikT5e6edNTzd3ZbfDDYO_xcyl_saeg6U8ICm9mEOYdx1jzBkp96MSCyYe8cwrDDt9SEC0vep2gx0yWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دولتی سوریه در حال تصرف انباری از تجهیزات نظامی سنگین و خودروهای زرهی متعلق به سازمان سابق نیروهای دموکراتیک سوریه (SDF) در شهر حسکه، شمال سوریه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/145369" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145368">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee52f2348.mp4?token=A9l2FLJq3I2_Yc7UabXtoFB1SQoFqclYs9gikAXW_WOQAbbL__SjaDi7NujEPk9n0CfNhPLFtUxBrxFx_oUoqYk_guN5YKEHkoTrd89A11qM-Gvcl3LVW4SHZucr1NvAn8VkOyZliimUEIHdv4xc5iIn6fxdplVcMpA4gV17k36bnaYxIt0lOyBSdpiNVDTSWyTJt1vSpK1QpGS4nBAZ-2Wte0rTzqDF2-KfIOCLPLqdxQl2GotAk-mcaHnh6O-UoNZsXPUMuZ4XVYcl78X4iTw76teQ80peOMyf-klwMsAk2-KVfmJznDKD5YCtdqLRgtehjYgfmD8XSQ6075Gx8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee52f2348.mp4?token=A9l2FLJq3I2_Yc7UabXtoFB1SQoFqclYs9gikAXW_WOQAbbL__SjaDi7NujEPk9n0CfNhPLFtUxBrxFx_oUoqYk_guN5YKEHkoTrd89A11qM-Gvcl3LVW4SHZucr1NvAn8VkOyZliimUEIHdv4xc5iIn6fxdplVcMpA4gV17k36bnaYxIt0lOyBSdpiNVDTSWyTJt1vSpK1QpGS4nBAZ-2Wte0rTzqDF2-KfIOCLPLqdxQl2GotAk-mcaHnh6O-UoNZsXPUMuZ4XVYcl78X4iTw76teQ80peOMyf-klwMsAk2-KVfmJznDKD5YCtdqLRgtehjYgfmD8XSQ6075Gx8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهرک‌های «بنی‌حیان» و «القنطره» در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/145368" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145367">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: عملکرد چین و روسیه در سطح سازمان‌های بین‌المللی در قبال ایران، تحسین‌برانگیز است، زیرا از سواستفاده آمریکا و متحدان این کشور جلوگیری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145367" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145366">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36aae20471.mp4?token=d0sZc9_T8L6AeWj8ltb2LO6nj53eF5srhLBaRo_bCph9AjRTrDPXnks0jOhLTxuFJJJQ7e9Ua5GXM45qUV4Ole6pmDpdEzwHZkKxZI4l9O0oE8fI3HG_g8-k9hqS8vEyhCzp2boUDQcuPsd_1-mh9xhzdtsO-4njBxRlf_mZsV6T9OrsuHqdrU9mKv65wPPCt16rhRRj0f_O78DdYscKQ-UPCv07cnGHZPqRx7fboNylFKzWDPRGKqEfyKSNEbW2_UtWSFL8BYZ_mJjtj05CX9HTEifNxnxa4AlyM3S0mtx6mjaimVZMltSaovjlNWx4E8xVu635cxfk1Ormv-YBuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36aae20471.mp4?token=d0sZc9_T8L6AeWj8ltb2LO6nj53eF5srhLBaRo_bCph9AjRTrDPXnks0jOhLTxuFJJJQ7e9Ua5GXM45qUV4Ole6pmDpdEzwHZkKxZI4l9O0oE8fI3HG_g8-k9hqS8vEyhCzp2boUDQcuPsd_1-mh9xhzdtsO-4njBxRlf_mZsV6T9OrsuHqdrU9mKv65wPPCt16rhRRj0f_O78DdYscKQ-UPCv07cnGHZPqRx7fboNylFKzWDPRGKqEfyKSNEbW2_UtWSFL8BYZ_mJjtj05CX9HTEifNxnxa4AlyM3S0mtx6mjaimVZMltSaovjlNWx4E8xVu635cxfk1Ormv-YBuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای یمنی کنترل و آزادسازی منطقه الکَدحه را به دست گرفتند، نیروهای وابسته به عربستان سعودی را از منطقه بیرون راندند و به سمت مناطق بعدی، یعنی «مقبنه»، پیشروی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145366" target="_blank">📅 15:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/keHij041w_hJgYKy_ERokMYbVJD3S-9o8RmcMR017GNZ4zAJ0CPoHkb6dcE_KS6oyJ-PgysBRSP128VjihfMtaygq_IQcbbAXr-mrCimLhsYglMqOo54-Pod6l9ONwIOPiJD3PaE01hj6rBxFwvrL82kATAan2dd2vNRB7H_avLpibu1hrLPt0V2lxb-4Lhyy8sXtoFOIO0DrYnvb6fdifuxl9tL0xw55J1uqCc02kpvm6xCdAcvfr9xAwtthB2nWOjdMKHy5zRqEQnUQbmWgRt4Ap9-VTkhvQFwcYS2P-b7DQyaDJpxwQIM-TlS1mPVvC4hkfixXui0ySnoxQiuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nSnHvN0EEHajhSINCTY6UAjlv4KKZC1ssp8DfcB9s18RxuBLRBRU8uu4izotTAdGdpgHP6GHPk3fYeTiGc7ja3Hf9i4AmDOYFdJj-bGbl4yLFxzVf3CbPaf8WzCcTGRZd9kdQjzF2jDesxI6Q4h5uqttxQjitnRKDCH_IU32bGC64tlm0Q2yGkiejuGzaJmZneZFIXzCq4F3pOX37Va1qDgPPxjSi9iPo2YbGFFli0en7-Q7EF-xcUCF-YwrHGGfhqkGlebbnuuwTEcf05VYLin9kxM8VzZfffl7MtYApUD9Ta8nHhSCpZCiKT7ElbxgVu9kvmlMwuKSHUCo2U1wXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=qZi4nCxIZbPw3AOrRXYd0AUQOWA_m1CHmm7Z5Lr6JdG4pDMIZspKCXTv9vDMPuJKOxtVZq4rhHYO7BWF_mZB1evZbwjQkz0jS9KFGdsNPE9eeufXXNQqBMVHOqPOU3BqlS0VJC1JmdzXiIDKXA3eWtI1Grsej2kC0_gSxIWnFGtnU2r7VAdzrX58sRrfZDVqChvIp4JAMbaYz45QjzbduOHaauTKRUps6tCh066k4pO9icGprTr_8XantMh6bFpsC5JogeSAdcJXrXnKeHyoiyTeQWemZbV0hPauilddMr881jQdLcR1M3yB-xvlcAxBcqKpDaf8y8GU2SsFGJiRDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=qZi4nCxIZbPw3AOrRXYd0AUQOWA_m1CHmm7Z5Lr6JdG4pDMIZspKCXTv9vDMPuJKOxtVZq4rhHYO7BWF_mZB1evZbwjQkz0jS9KFGdsNPE9eeufXXNQqBMVHOqPOU3BqlS0VJC1JmdzXiIDKXA3eWtI1Grsej2kC0_gSxIWnFGtnU2r7VAdzrX58sRrfZDVqChvIp4JAMbaYz45QjzbduOHaauTKRUps6tCh066k4pO9icGprTr_8XantMh6bFpsC5JogeSAdcJXrXnKeHyoiyTeQWemZbV0hPauilddMr881jQdLcR1M3yB-xvlcAxBcqKpDaf8y8GU2SsFGJiRDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیرعلی قنبرزاده، بازیکن تیم نونهالان آکادمی بسکتبال پاس، روز ۱۹ دی ۱۴۰۴ در گرمدره استان البرز کشته شد.
💔
مادر او با انتشار این ویدیو نوشته است:
«امیرعلی عزیزم، دل بارانا برات خیلی تنگ شده، جات برای مامان خیلی خالیه. شادی را به گور خواهند برد، آنان که رنج را در ما آفریدند. ما مادران نه می بخشیم و نه فراموش می کنیم.»
🔴
امیرعلی قنبرزاده در جریان اعتراضات، جلوتر از دیگران حرکت می کرد و دست هایش را باز کرده بود تا از سایرین محافظت کند. او در همان حال با اصابت سه گلوله جنگی به سرش، جان خود را از دست داد.
🤔
حرام زاده هایی که طرفدار این حکومت دینی هستن و سرشون تو ماتحت بقیه شهرونداست ، بدونن که در روز آزادی رنگ خوش نمیبینن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145363" target="_blank">📅 15:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145362">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hbk1c1q69e_nM6AAmnh1FaWaorHdCC3niLw-J0ZYRPGpUMHH0LtDQTLCXp5YmULcfkkGe5RqBzVamodlOy8-BG6AH6H3DEvhT_RvRsGy2RtZwODjyuKon6uVZtwaOL1YYyni4mHn8TbeZ-nGGFjLWLXDU46B_G_Dh64eFe9cCrHCxWwXcDJcjVmQKgHdfCkpwJpTnx7cNYXvGqyKzmRrrEZ0uwbu8i0_D23R0rvPMVMF_qBDVIERkX-fo570xY3bXvBE_aYfW6CAu6y3u6UO3xF9LbUfk1QD4E0ftBUaqY0mxoc1jzFwLx3efAZYpvjL7kz_7bEHY3GOdaIGPBYz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: پزشکیان و قالیباف از تفاهمنامه تمجید کردند، ترامپ با حمله گسترده پاسخ داد، الان باید افتخار کنیم یا لذتش را ببریم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145362" target="_blank">📅 15:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145359">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0771d348e.mp4?token=Lj7Luk5YeTxcjLELVXphr9ljqFgc1ny20sUkBqa9ZURfF2AqNW74-KjNZzrvQPyOqMBijbOIM8LPPHe6cc8fy_x_CVh-J0-ELOf81XbRarfsLciSGeZ90bUkOqHm7nu--56Muq0rjdH4ICRubOvGtnTF-5mhKce29vC6mF8c2YVA_eg0NIUW7m2q3K2E1wb588hdIx8QWIxbPRPMONmMtK_Zw8_7nh-4e3HeaSl7O8NLquqkAiCBy1nzqCARKYLnK3LGN6Nq_tgTVRsDSyE0cCn4m1OKfgRDNWiIZlCnglV8sw01GgRywJOR4LGt-3INdGbwpJbQ6w9AqTX-7XBzooYU7AFZKHdMULzGMikq8MneZOCsIx6kofVz8in-1dJqA6sI5UQup2LaILNofSpAlsriOoqWFkwxUGSWNOs0RJGa9flS6z_wNKEhB3OuDSdPRAcOFc3PsKVDDiUJ4J4i5fNAEmjg0Pbqy_5BhR61Muu4FqyX9sbLMdZWWZDbFNbCvfAGJ0yJDSKLSjLhy4Hcp-A_X8as76CO7iXTKj7wgMUqfuACM2dgCaNGt9xipkNygnxrw76aghc6LbbH0-ks3Utoi-W9AFDyFctODcrMpgC_KSDmBTJ2JwYiZPKzKhohlohcVMRsqQdHX_eLNn9j8CJRI5x3fe5cHREeJeXlqZI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0771d348e.mp4?token=Lj7Luk5YeTxcjLELVXphr9ljqFgc1ny20sUkBqa9ZURfF2AqNW74-KjNZzrvQPyOqMBijbOIM8LPPHe6cc8fy_x_CVh-J0-ELOf81XbRarfsLciSGeZ90bUkOqHm7nu--56Muq0rjdH4ICRubOvGtnTF-5mhKce29vC6mF8c2YVA_eg0NIUW7m2q3K2E1wb588hdIx8QWIxbPRPMONmMtK_Zw8_7nh-4e3HeaSl7O8NLquqkAiCBy1nzqCARKYLnK3LGN6Nq_tgTVRsDSyE0cCn4m1OKfgRDNWiIZlCnglV8sw01GgRywJOR4LGt-3INdGbwpJbQ6w9AqTX-7XBzooYU7AFZKHdMULzGMikq8MneZOCsIx6kofVz8in-1dJqA6sI5UQup2LaILNofSpAlsriOoqWFkwxUGSWNOs0RJGa9flS6z_wNKEhB3OuDSdPRAcOFc3PsKVDDiUJ4J4i5fNAEmjg0Pbqy_5BhR61Muu4FqyX9sbLMdZWWZDbFNbCvfAGJ0yJDSKLSjLhy4Hcp-A_X8as76CO7iXTKj7wgMUqfuACM2dgCaNGt9xipkNygnxrw76aghc6LbbH0-ks3Utoi-W9AFDyFctODcrMpgC_KSDmBTJ2JwYiZPKzKhohlohcVMRsqQdHX_eLNn9j8CJRI5x3fe5cHREeJeXlqZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طغیان سیل در چین یک ساختمان ۳ طبقه را ویران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145359" target="_blank">📅 15:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145358">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
دستگیری دو نفر به اتهام حمله مشکوک به شرکت تسلیحاتی در آلمان
🔴
پس از آتش‌سوزی عمدی در یک محل ساخت و ساز در مونیخ، اداره پلیس جنایی ایالت بایرن (LKA) به تلاش برای حمله به یک شرکت دفاعی تسلیحاتی مشکوک شده است.
🔴
سخنگوی ستاد پلیس مونیخ اعلام کرد که بعداً، پلیس دو نفر را در یک پمپ بنزین در ارتباط با این حمله آتش سوزی دستگیر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145358" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145357">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قیمت پیشنهادی هر کیلوگرم تخم‌مرغ درب مرغداری ۲۶۸ هزار تومان اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145357" target="_blank">📅 15:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145356">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aswpZEluXoGJvuTH3olbH4UGagRdQAgi99HFWiwWYYjCj9R7DlAqmnv5PdJMBLBBdH0bt53bHk-O7KPKrfDlZFfpaFapzLnpFMzWGda_Xz5IeYxdpbe0YgFua8lOMmc5FanbFl066DXbZRs0-nhKQ8hIToQgYVYC3NbeG6TW7nOIIPpodeyGHTRJJdAg0Z0Ia07-RzVno1cNxDoOCoalRa_DOJjoDMI75X3TjOa_MalO3rFHJ9LxkrNpkBBMBZLIcxaFMWq4csDVkdihMra1klSkgnxKnbeAK7ktKAdqeolwEassPVXOQw1UBUjFaiIYXHkh2btnCRHOC57K0__NpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ گفت: «وقتی وزیر بازرگانی، هاوارد لاتنیک، گفت کسی کشته نشده، منظورش ونزوئلا بود.»
🔴
او افزود: «۱۸ نفر در ایران کشته شدند!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145356" target="_blank">📅 15:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145355">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUIp5wBlyYpA4xeoJF8kHLGeiFynmyuTmoeX7RVUa-ZC1-z3QLBS1yJQVgcQxud7cIzbSx6TLa_SOJbEl8MudlvHjRnC_Dba6993yKLm4zXTveOC9Z80l91_GpJk-z47ehMujwyr_CMu_bM6IxzwGOC7kCvuf8st5Ao7I5YGd3H50jIQTUHoHMgwN1AL5I3ZHz-KuA1e51X0wRlHcuQYL277cA1bTvAnOUvfXG_IiT2h9roxFAneN_EbEsvzkoKirfY1kyaQZXGKZcvk8EdtUmVketcqTUurNlRIUtsmVMSONQNzvwP3noF6e-m3KTNrwMLz8Lq7ml2BRSefD4cZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،از طریق شبکه اجتماعی Truth Social: حجم صادرات نفت از تنگه هرمز دوباره افزایش یافته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145355" target="_blank">📅 15:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145354">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhDon0aKl2KNoge7SZiVeGTh_qfgN38_DV5oV1eLQTTd2XbLUi1o--CWd1kfJDar5C8mwCInMlV0OPsKmf9yeM3vHIcMLZskgJvPusU8gtnKGb23ZWNBZe_RG1GDfnFwPmK3wZn2Paja6pNvDngbHPloa0Q6-d8dRLVR0F49awu1Rv0q1I7AaNQBy5-Nlup0JNWrOluya8P0oKbO4iVblt-297DQKYEiOeoRNuD9a76zD0mg0gtNk42FkwS5sD-VV7DP7uh7QhbjTJ3tA3Q-Z2EgRb3idPYDjc-XHDckip2BYzn3MxXUL9mt3dxluOVwNf5M5p2GhkG-gjIB7z1FBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: این فوق‌العاده است!
🔴
سوریه خود را به عنوان یک جایگزین برای تنگه هرمز معرفی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145354" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145353">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وال‌استریت ژورنال: توافق آمریکا با عربستان، غنی‌سازی ۲۰ درصدی را برای ریاض ممکن می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145353" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145352">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پوتین: ما به دنبال احیای کامل روابط با ایالات متحده هستیم و رئیس جمهور ترامپ دیدگاه مثبتی برای همکاری سازنده دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145352" target="_blank">📅 14:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145351">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu78B7cfev43KE0uY4fuccUiP9O4f7hNHqS1b8RkGPhjhqcShDXbsYvgz_T1k4Q4JOBeQG4yiii3vtrYE3_7R9GI9rjqXb2-klwTy6mmoOuc91B9lLo_KjdOs7ineQA1TJvypGftFSGGRNq3_TdnvWb4oDXODSZIayRM54SREZhsxzIHKIWYMlNjJKcPYtNDeH46_2Y8kAMawZE9LJ4n-dg26Nuo6MyENH92bTcg1U6mgge38i4-qH3z4ikKl1eYle8wtZ3I02zypiT1C8fmR6O-OTORYpV_JnaA9LPZSoY6XAOH6b72U9-prNZdrSagchgQYWXaCAYdHFt_WIKu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکانت تلگرام توی توییتر: امروز خیلی کیوت شدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145351" target="_blank">📅 14:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145350">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8NN833fAHRfxGJp42-TgQO8BkPOMSXTRxb17hrgrAszWFFj8JFDCVaobT7qR-F-8IIQ8GE7ctgpfDmbv7NmP1Vg55NB0VNW-vQ1BWt_iOXdm0CYfZGa3qX-snbsNhUsjypkfq4XGwPptqng01d0c8cWRoWXNIxSLKhJPfWAIRj4v_IFCedLJAPGhmjzXrJ4Om-aGKMOIFr0oPHUZE7Rmxb2WVy0HoL3y2znT2munOFVBPFAPSFr-95zZee5HKfkP3ttdqhp2q2bAkf7WTLdZl0KSQYzmaXeitU8adc3HVmQZsEp9MONmzvwkedA0FE3riWrFn6cXWXTdOXXlGz1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۷.۲۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145350" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145349">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5af1dcf6.mp4?token=B01a4u9YuLKdbe2mXM4-ETlOKGpx_Npr4wv_AuTX0QGVX9aJXwCAOovbD0_lWc_RKJqBvPuDwM-XpGs7CnZ64ZCiK0JYMXXHk7Qwpz9OGCVJXGPWoC4za0dShIMlto7E3MROfWRqLNYQKiByNuqgkCDzsMGCe0qj0NwBTTn-8GIPeAXoaD3VnZCMxwbfsI2D9J0PeS4KplqIUdb9YGNgCgFIXacQ9tl75F_4meCWl9s-lPeOztlV2jy9yOGpw91u_ROjO37r5v4eG5Ev-Ctu93nVSq8zHj_B4Ub4XRV1VaFl2_jZL6XyTtAsS_-lej-dzEGCIgAY8XAzRA_ht_DAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5af1dcf6.mp4?token=B01a4u9YuLKdbe2mXM4-ETlOKGpx_Npr4wv_AuTX0QGVX9aJXwCAOovbD0_lWc_RKJqBvPuDwM-XpGs7CnZ64ZCiK0JYMXXHk7Qwpz9OGCVJXGPWoC4za0dShIMlto7E3MROfWRqLNYQKiByNuqgkCDzsMGCe0qj0NwBTTn-8GIPeAXoaD3VnZCMxwbfsI2D9J0PeS4KplqIUdb9YGNgCgFIXacQ9tl75F_4meCWl9s-lPeOztlV2jy9yOGpw91u_ROjO37r5v4eG5Ev-Ctu93nVSq8zHj_B4Ub4XRV1VaFl2_jZL6XyTtAsS_-lej-dzEGCIgAY8XAzRA_ht_DAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۸۱ سال پیش در چنین روزی، ژاپن تسلیم بی‌قیدوشرط شد
🔴
۸۱ سال پیش، ژاپن سند تسلیم بی‌قیدوشرط خود را در عرشه ناو جنگی آمریکا امضا کرد؛ رویدادی که به پایان رسمی جنگ جهانی دوم انجامید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145349" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145348">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
عارف: آمریکایی‌ها به فکر ذخیره بنزین و سوخت باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145348" target="_blank">📅 14:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145347">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حسن  روحانی: از رئیس‌جمهور تا مردم، دیگر صداوسیما را نمی‌خواهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145347" target="_blank">📅 14:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145346">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پوند انگلیس به ۳۰۰ هزارتومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145346" target="_blank">📅 14:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145345">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuoEy6eHqpsUZEVVyuvr0joe4vS6ymZaO7e-g4YVjZizQg6fPPaHcTzS1b6Ugk8CjBlW7qgcUc1BIuu1V6SrT007pbN3J-V-4S6LKbbM_yOFdYdU9hds5GbZ4HshDl6gCws0AnR4h907xI_55bDaPDiL6tVXcQ8ty_4Xtt5rji2e5LznHtve-Pzq9gl1r9ab-E9mTcxrSb9mewWosaQMZEZ6etOYzKpAEgBAGNsA3e4X1dd_Xg_6gNJNMILhU18MVCnhxU2cxTl4F9xABIbfqND4Z2EY2r-X0eD2mtIcGVitVKvUn99AE-6Q1K_GgSpbf6n48HykhPfVcuE3dKyClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای باشگاه پرسپولیس تو زمینه انگشت کردن همدیگه ترک عادت نمیکنن
@AloSport</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145345" target="_blank">📅 14:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145344">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#دلار #تتر
🔹
دلار و تتر تقریباً هم قیمت هم هستند.
🔹
کف قیمت امسال رو تو وبینار ریسک ها و فرصت های اقتصادی ۲۰۰ هزار تومن مشخص کردم،که خیلی ها میخندیدن  چه کنیم حالا؟  این موج لگ صعودی اش ۲۲۸ تکمیل میشه انتظار دارم اونجا واکنش نشون بده،اگر اصلاح داد ما هنوز…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145344" target="_blank">📅 14:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145343">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145343" target="_blank">📅 14:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207b7a394e.mp4?token=o6i4GPyvserRvFp7goPuC0r9ewcXj1VpyLEw6zB0Pc6CMYsjOjtML0kdorUTGMo15DbTLNd-dB-OFgYGtne4wrFJtXanqDU4YeAReV5bNTkyYf9SnCK3wiodOeVEFVKiur75ovcypgqVO7-3W9AWhOHh-KBQt8ed7VgP6bXSqAE03_sZDdnSq5KL-a1zO175c6TBr-SyhBfD-KFwRHqwRYvuIWCmUX00x2fxwTQWnaoQcbFn8wvCZUvOTRBMkZVY0frQ1Lo6hADoarxWOJ2P1HIprSspzVDmS1xFw4A8ql8QOHdQQIHq8H356TboDZ9wx361rWwPsvPkigtmXcTTOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207b7a394e.mp4?token=o6i4GPyvserRvFp7goPuC0r9ewcXj1VpyLEw6zB0Pc6CMYsjOjtML0kdorUTGMo15DbTLNd-dB-OFgYGtne4wrFJtXanqDU4YeAReV5bNTkyYf9SnCK3wiodOeVEFVKiur75ovcypgqVO7-3W9AWhOHh-KBQt8ed7VgP6bXSqAE03_sZDdnSq5KL-a1zO175c6TBr-SyhBfD-KFwRHqwRYvuIWCmUX00x2fxwTQWnaoQcbFn8wvCZUvOTRBMkZVY0frQ1Lo6hADoarxWOJ2P1HIprSspzVDmS1xFw4A8ql8QOHdQQIHq8H356TboDZ9wx361rWwPsvPkigtmXcTTOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعطیلی برخی از جایگاه‌های سوخت بغداد به‌دلیل کمبود بنزین
🔴
برخی از جایگاه‌های سوخت در بغداد به‌دلیل نبود بنزین، به‌طور کامل تعطیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145342" target="_blank">📅 14:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145341">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNNTwP7ge9-lasGAHfahbANLHP-2dKdPWFyMYaj14BXn78SFWjU1JpHFE-aMLqu4bdmWdsUNgE2Uq-1Gkbcax8ZwqRhILHOvYjVXy1d4EGub9LWy_-hdSPvbTZVNfY_Ba6STfuZrURHIOtrNbOL7AyprRYluRtnEgLyB7kJLU9afB3dUKipq-CDvC1eXecdDizcGMi2vuGJoOYWMcWT7Wd95k0Tk6l2Z2uT3Zzz0pGhG_ALAHf6LlFYs0FkRfAQ2YiIf9SBdLXAgVUyYFBFHpdA_bwgb6ud6V04GBCVEC3jQxPtZXWu99kZjAwu9jRvBy06oktrApcp_cVJP0Wkw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت ۹۷ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145341" target="_blank">📅 13:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145340">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کاتس، وزیر دفاع اسرائیل، هشدار داد اگر ایران به اسرائیل حمله کند، این اقدام اسرائیل را «از هرگونه محدودیت موجود» برای حمله به ایران آزاد خواهد کرد.
🔴
او گفت اسرائیل «تمام زیرساخت‌های ملی، نظامی و غیرنظامی» ایران، از جمله تأسیسات انرژی، را هدف قرار خواهد داد و ایران را «عمیقاً به عصر حجر و تاریکی» خواهد برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145340" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145339">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رویترز: آمریکا احتمال تشدید حملات علیه ایران پس از انتخابات (۱۲ آبان) را بررسی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145339" target="_blank">📅 13:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDJRluOos0xyQMtB3-BmRLC1bf7Kr69Htizupw-_-8-s0RKKiyapRDLINcSp9nkFFSa1-IDvprDhCDBNX609Ir3qnV7QnymlEAjJXGMrnur5eoaRv35NcCuGso9sdLuf0irpm8i8LM6aXYotRtJjU-9BtUXhJStDlfqlfBBd0ilx14lQ8mueV0J8kzAokn4ecV9S2S8vTCYUWCgK_2Z8PKNDUbIRgqdLq0U7b3XolgUh5-lIcZJEQ5litLDZ1WQGv0BRPo5YT2-Ki0J9pKpCSW8MEE7Ch75cnus5UoMyn6znj5kkJ1sknxmLjw24I0xFF3RvZU8eK5aB7zmDmsjivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای آمریکایی، از جمله یک هواپیمای اماراتی، در حال حاضر در آسمان تنگه هرمز فعال هستند و وظیفه سوخت‌رسانی به هواپیماهای جنگنده را بر عهده دارند. احتمالاً کشتی‌های نفت‌کش نیز در این عملیات همراهی خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145338" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145337">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145337" target="_blank">📅 13:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145336">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کیفیت هوای تهران ناسالم برای گروه های حساس/ بیماران قلبی در خانه بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145336" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145335">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بقایی: عملکرد چین و روسیه در سطح سازمان های بین المللی عملکرد تحسین برانگیزی بود/ مهم بود که مانع از ایجاد ائتلاف علیه ایران شویم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145335" target="_blank">📅 13:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145334">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رکنا: صدور گواهینامه موتور برای خانوم‌ها توی مراحل پایانی قرار داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145334" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145333">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سپاه اعلام کرد که با موشک و پهپاد به پایگاه‌های نظامی ایالات متحده در کویت و امارات حمله کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145333" target="_blank">📅 12:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7xHcvWVg6vgR-QfYaroj2eunAIYcF1iZr4KZg33Ky6KC9kcbYirsfbYNVvdHCGCYCjwkGjeYIxrjELLenxTuYX7J65jYOjuauyBD8B910cVf0ngcZIeIfPwyPp1sgxaa8VZjSPC2f4eni7b5jkeSY7NSgx_VQnWX_oF0YgOqix2hGnXaQZAPKt_KxJpT7sxogQT7Snk4rrpFNJojj3ELS8opjYD_PnxV9fX9hSMCX2PPB6hT5TDtbxPjrOtlGiM7B82OWimX2NBDuHJuTWxSofuDfYurdSZ8GXlsiH5U7IJLX8nbvYkioT5dHPZPOXKrMKFMVF27T4frUFBcN9uUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه تأیید کرد که خرید جنگنده یوروفا이터 تایفون از بریتانیا در حال پیشرفت است
🔴
آموزش خلبانان ترکیه در بریتانیا از ۷ سپتامبر آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145332" target="_blank">📅 12:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
بلومبرگ: صادرات نفت خام عربستان در ماه گذشته به پایین‌ترین سطح در ۹ سال اخیر سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145331" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145330">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
واشنگتن‌پست: پنتاگون دسترسی به اطلاعات طبقه‌بندی‌شده را محدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145330" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145329">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217c2cc494.mp4?token=mIFzmDTRHrSwDsjbYd2DOoK746mBlD6S8wuwaoUtASxfJVJtTsc_VVeTbVtN_plLk2iy5FDEAGx_Vt1OMFkMEobNwauo06wPU5m-Haw5a_rHvM-ou0-U3jg2lnTL82iND1sQnqzweaNzb_KA-DP0taG2IEp8opqqOIia_ecasVnW4RGo_NySEAzX3wXaXD-37Z27ILFlRoVaLf0_Ghr2tCYkcZaNJGy0jkfRYKE4i1Wml_UwlmZWAx2dmTzDIDAyiM1iG6Mok8JUxTTqK0YsbKQDZejbM-kSdSX0xbtjdBR_StGZIxjBopLuR0yKN0HRqDZzxBWCEq3wBlOWVpVhKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217c2cc494.mp4?token=mIFzmDTRHrSwDsjbYd2DOoK746mBlD6S8wuwaoUtASxfJVJtTsc_VVeTbVtN_plLk2iy5FDEAGx_Vt1OMFkMEobNwauo06wPU5m-Haw5a_rHvM-ou0-U3jg2lnTL82iND1sQnqzweaNzb_KA-DP0taG2IEp8opqqOIia_ecasVnW4RGo_NySEAzX3wXaXD-37Z27ILFlRoVaLf0_Ghr2tCYkcZaNJGy0jkfRYKE4i1Wml_UwlmZWAx2dmTzDIDAyiM1iG6Mok8JUxTTqK0YsbKQDZejbM-kSdSX0xbtjdBR_StGZIxjBopLuR0yKN0HRqDZzxBWCEq3wBlOWVpVhKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پیرزن پرچمی: از مسئولین هیچی نمیخوایم نه پول نه چیزی، گرونی و بدبختی رو تحمل میکنیم فقط حجاب رو درست کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145329" target="_blank">📅 12:23 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
