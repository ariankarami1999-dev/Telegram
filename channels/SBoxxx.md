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
<img src="https://cdn4.telesco.pe/file/rmx4GoyjeyIPANEXiOM8RG-fzUkdWHrF2z_r9lJ1u3iHMmIc0PEABf-fU0FnKwUl5UK_UMdKeDhA75leLsiJjvvyZUkrwiP24KVCDa_f4DwL23hqj1gw4EcaYy4VabghMu68RQXTgbraZQiwR4aSFAB4GxXwQSrQMj4-JRVgz5tGXrqn1oHjZptaLY3xBPkQ1xC96EXn-2m7ZwcYjKVbHSzudQ97iUiJs01YBh7vZRXq-Ro-qIHYag07rFzUVigERVX9T_Zb5IM6G6cjmDgERfKg5Gv90XW6thUkXLd4Io5BMVkGYfvd_OXmL1tQzHKv399P31CMhYD7afb4ZEVruQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-21133">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ-RiCWPvHtClep5sVkdjuR5dzsp431dN909NoodUMKfYr5CKFbjCGMVic9J0dGaC8xg-Tu0JmY2aIoZJe3dXmjmSEFSEDJ1iYmkbV3f_3-Bls0VLWdYn78h7QghwIrKIx_H4iMq3A1uWlrYDKOBmtwwOyTsEUPOmN1_uqTwdoMU-R0o3SQGDBuNP2vGRHXOcT8e9ZXwQXGNabJiyJslxGoT-Hz7OKgj_acfglyRNiWoiNYhU10-GSfjYSuahHseODFFVGKHAka98ax6Nf6ySmTLB8KUk2-mxpyAvFIzeO0024LRrHzcZZMeHEqyn7PD1CJ54hZEg0WK96fThYWdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.
محدوده  مناسب خرید:
4302</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SBoxxx/21133" target="_blank">📅 12:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21132">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNtmgemx5Php2Srv0sbQ5VSAdfwadHAXCHjloOntVvwsccnHX3r6EKFHcAac415Tb_UUx0LCyQw989XVOVZTrfVC0DGC35XWAWBfftE5mD4fZ06PTllOBsOjOhnUU6HEaPALFTmDg6ctB4i5hSLhm8EqWGP96-n6ZJhpgcw-TYDcxmf1JkCxeF4LKUyO0DtvXBbK_5vy4rTz3bwtxvnjAR0cA-to2c743h0TKqDJz200VOEkLfEpvblt0Mn_671mbG8DiWw_V1SdELQauPed8zf-rbZa6SqNQPAcxDAiILUKFOGqDtWMS9_WC8Ggifh8qCave19lJzsN61R0T4MacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی است.
اما طلا از صبح ریزش سنگین داشته و لذا دیگر وقت فروش نیست.</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SBoxxx/21132" target="_blank">📅 12:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21131">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=N--uga0xjFenRIRJC0vYwJ1wMoyUe45PbVHNT4JpCTxj_UfNZgJEHASImHbW4RObWjTy0nKE-6j25OyNfWKr0wlRLNH49ZehLT4NnRxo_dEFa4V-tjiOs16SJW52aXpU12nC2GS-Q6cACGB2StUyFUTKv-4X3fyaBf60c-iXyfpTst_Ov1Emuh1EjxuVRXTYlkPKZk9OJrtCE-SQGry-eL2J4oZGE4OKQBmGtYFHapTM89e61A3_1zqI9_S802n6QJ2ooknL-AMjb1BiSNcGRNpfO0CM8WK68mushZH673AlxKi4NLOEj6u2Xw7MTG-uKWhUOx68Ff3iMV5Bo-yHYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=N--uga0xjFenRIRJC0vYwJ1wMoyUe45PbVHNT4JpCTxj_UfNZgJEHASImHbW4RObWjTy0nKE-6j25OyNfWKr0wlRLNH49ZehLT4NnRxo_dEFa4V-tjiOs16SJW52aXpU12nC2GS-Q6cACGB2StUyFUTKv-4X3fyaBf60c-iXyfpTst_Ov1Emuh1EjxuVRXTYlkPKZk9OJrtCE-SQGry-eL2J4oZGE4OKQBmGtYFHapTM89e61A3_1zqI9_S802n6QJ2ooknL-AMjb1BiSNcGRNpfO0CM8WK68mushZH673AlxKi4NLOEj6u2Xw7MTG-uKWhUOx68Ff3iMV5Bo-yHYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/21131" target="_blank">📅 12:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21130">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">زلنسکی
:
ما باید قوی باشیم و باید به پوتین نشان دهیم که او تنها در این سیاره نیست، حتی اگر این رؤیای اوست. و به همین دلیل او باید به مردم احترام بگذارد.
متأسفانه روس‌ها فقط زمانی به مردم احترام می‌گذارند که نشان دهید قوی هستید. آن‌ها به ضعف احترام نمی‌گذارند.
طبیعی است که گاهی اوقات مردم بخواهند ضعیف باشند، زندگی خود را بگذرانند، وقت خود را با عزیزانشان بگذرانند و به فرزندانشان عشق بورزند.
اما نه، باید با روس‌ها نشان دهید، باید نشان دهید که قدرتمند هستید.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/21130" target="_blank">📅 11:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21129">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آن دو دیگر (کوبا و میانسوسمار) هم که میبینید ستاره شوم کمونیسم بر بیرق چرکین خود دارند.</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/21129" target="_blank">📅 10:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21128">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">موسسه مطالعات جنگ:
به نظر می‌رسد حوثی‌ها با تهدید شرکای بین‌المللی عربستان سعودی می‌خواهند این کشور را منزوی کرده و مانع تشکیل ائتلاف علیه فعالیت‌های آن‌ها در دریای سرخ شوند.
حوثی‌ها در حمله به پایگاه هوایی شاه‌فهد در طائف عربستان در ۱۷ سپتامبر، یک جنگنده اروپایی «یوروفایتر تایفون» ایتالیایی را آسیب زدند. ایتالیا این جنگنده‌ها را برای پشتیبانی از عملیات‌های دفاعی در برابر حملات ایران به عربستان مستقر کرده بود. مشخص نیست که حوثی‌ها عمداً این هواپیما را هدف گرفته باشند یا خیر، اما حوثی‌ها پرسیدند که چرا آن هواپیما آنجا بوده است.
حوثی‌ها احتمالاً این مأموریت پدافند هوایی را تهدیدی بالقوه برای کارزار تهاجمی خود علیه عربستان می‌دانند؛ کارزاری که عمدتاً از حملات به تأسیسات نفتی عربستان تشکیل شده و در میانه پشتیبانی دفاعی کشورهای مختلف از عربستان ادامه دارد.
حمله حوثی‌ها که به هواپیماهای اروپایی آسیب زد — هواپیماهایی که برای پشتیبانی از تلاش‌های دفاعی عربستان در برابر حملات ایران به این کشور مستشر شده بودند — در واقع اهداف ایران برای شکستن ائتلاف مدافع کشورهای خلیج فارس در برابر ایران را نیز پیش می‌برد.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/21128" target="_blank">📅 09:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21127">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0lAAELHpTmTtydPBQ8d2kf29e1yoJmnNLkM_eJEJXG-XwGA1Og83CwYJ13TiK1hMS3rhpy0pdZWDZOtTgtB1Z6fP3qFcv7db4TCco51LxeJrova_2yV6oXsTnmzdUYo2SEWTt6RZBGCzg1K-WLsd0HM32rOEhNXckf3FMtZBMqNxy3IaWGsKPrC_NOUlFW77sWjW_JeZgEc64pMo1AHvLQbndMIp1J1eukbPv2viXQIsOIBtQL_OtYpQJP8xyektE-TBZlF2giLlibQl-7YD8uRWtjWrg53SaZW5T_jifJcRsfQfzZoPA_iPsT-uoPuktNDZ79ns6ZGaQBEbOZOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/21127" target="_blank">📅 08:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21126">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نخست وزیر یونان، کیریاکوس میتسوتاکیس:
ما در ۳۰ سال گذشته هزینه‌های زیادی برای دفاع صرف کرده‌ایم، اما در زمینه صنعت دفاعی داخلی، دستاورد چندانی نداریم.</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/21126" target="_blank">📅 08:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21125">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
سخنگوی سپاه: نحوۀ پاسخ ما به حملۀ جدید آمریکا از اسرار نظامی است
اگر آمریکا به کوه کلنگ یا هر نقطه‌ای دیگر از ایران حمله کند با قدرت پاسخ خواهیم داد.
این‌که پاسخ ما چگونه است از اسرار نظامی است؛ ما اسرار نظامی خود را فاش نمی‌کنیم اما در میدان عمل نشان خواهیم داد.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/21125" target="_blank">📅 08:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21124">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، انتظار می‌رود این هفته سفری کوتاه به ایالات متحده داشته باشد تا در مجمع عمومی سازمان ملل متحد سخنرانی کند، در حالی که نگرانی‌هایی در خصوص اعتراضات احتمالی وجود دارد.
نتانیاهو قرار است به جای فرودگاه بین‌المللی جی‌اف‌کی، در یک فرودگاه نظامی در نیوجرسی یا فرودگاه بین‌المللی لیبرتی نیوارک فرود آید، که این تصمیم تا حدی به دلیل نگرانی از پیچیدگی‌های مرتبط با ممدانی، شهردار نیویورک، اتخاذ شده است.
هیچ ملاقاتی با رئیس‌جمهور ترامپ برنامه‌ریزی نشده است، هرچند گفتگوها با مارکو روبیو، وزیر امور خارجه، و سایر رهبران خارجی همچنان در حال بررسی است.
بر اساس اظهارات مقامات نزدیک به نتانیاهو، سخنرانی او قرار است بر ایران متمرکز باشد و ممکن است «غافلگیری‌هایی» در بر داشته باشد.
مقامات اسرائیلی همچنین برای احتمال اختلال در سخنرانی او در سازمان ملل، از جمله آزار و اذیت یا خروج هماهنگ هیئت‌های چندین کشور، آماده‌سازی‌هایی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/21124" target="_blank">📅 01:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21123">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/21123" target="_blank">📅 01:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21122">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/21122" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21121">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گویا جلسه برگزار شده و به نتیجه نرسیده!  First Time?!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21121" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21120">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8el29hTFhIdETRUfFzvqxNUEP9gweI4FMHCj5HSxzSiFDxGAWURlQ8Me0IPLN9i0wlAm-j5bjMGTe0THtl_-ezD3aj_1enA2_ngHbuOAV7yJm64C4qq1DNqwRCkQmS7AyTfyipGKB9_l9eN4gmvCIuTAcLtKBjKTnsIdAWRhMfKH3VaKOyOAMAZEDnkUu4tbe9n8GENYV7Vx1WP0-J1ra7-ZcYjPifope1icS8WfWN2GlKpHfZwUT7HRy8kra_XFdXc61EkYpAu1WmKVCLknyL--GiD-V1O3mmzIsI-fzCRrWke2vPS1nSmDC0DbWU-x3RibPOo5sueNTJfuW6TWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/21120" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV3U4Bm9rdpIFRVPiN4JqwyYeurlH_14-O8rBTh-dnk-sXGa1VCkLr0EltJnRHtayLPiDR07ih2e1vKw62J8hdPggt39txERsyu8ZeS_JsagxphzDzHJvlpcDsoBm5OVHnuALFpC78LjShXD3z4i5ZJ7dWqOnz2Bg82srD1Hd9S5DH70JcvU6PB9h8PJIEO2PWJYYzQbE6M3uMXwY2aTwamx4z-6neZNDmedCAMGfmbHdheKl7lE2Ry7Im-0ZChagKIRxci-hfjKgWafRoZ4LeT3_oMROLMBkjnb2IjmYpeiGXMWl3BdXl5suIvWZv1J5q_PAJI57JRTRra2bwd5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/21119" target="_blank">📅 00:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGvUHd8EO02TXG1iQB6MdhfTJzxxx7P176Jl1KWCszK-gTc283FGFq5EF84lYWjLGUL1prGhpTRBxDK1RdSQXdRPIzfT9Oxe-Tp5OdO-bjcNXyu7aT_M3cVRui3yPU5vYi4QyvYgaOCd7d9cbNFsqzCH1vN0qJy_oIaaqH0XVtIhyIQaA-2K-I-kbPMTJ04smIaXo5ob8wRwkREWwZjSLH5XkfGmoIetthQzPHugh2wIuolRvRwU8h60tc1ZZCHhjPnNi89KOZ_mup95dgP6pYlqYpm52V8Jh0IOebNY_sYt1bSgRF3dVwA54e1jH0RBv41FGc1gbLUDLGGlfuiNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUN_CFD — D #SUNRUN  از محدوده ورود دوباره حتی اندکی نیز پایینتر نیامد.  البته هر چه پایین تر بیاید خوب است، این سهم یک رشد دستکم 3 برابری دارد.  همراهان Secret Box در خارج کشور این سهم را دریابند و هم میهنان اسیر در درون مرزها نیز میتوانند روی بروکر WM Markets…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/21118" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtb0C7pHDzjaRhsZG0JWQkDPaOA6mHjU5F6FCSKperm0oTtYTNnfQ8i13bJUV7Q8jADXROjIS92iN_tfZ8N64rajy5AxpXdVcWjmbmgluS8BveEmXQqdCLWPoZBS-mC9II0LkdhkI7gzLQqAMTDQZ_DfkuUgKO6e2R09ksT-vf__MrooOHWnIN0ap9zKO4vQJZo8Mh5JU-h54PUuCETUrvHc-1DiSXQvlpc5L7XJHK4BGLz5UOOYAQ05Xet3c2Uh113_s4BcVdbwz_3Lf0uBGeNIjwSD-mJvnlLzNRSTt522dSglTOordO4JeyQxX000Dkv74ggvh9wj0oa7g1zx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL   دوستانی که درباره نفت دایرکت دادند؛  پوزیشن های خرید ما به هر دو TP پیشنهادی رسیده اند و فعلاً خرید نداریم روی نفت.   تحلیل جدیدی از نفت ارائه می شود.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/21117" target="_blank">📅 00:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21116">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvJTUM_ajja6DgMT6J-eV5-Tty95Zqhj_8aoq219g7rAvbkrTf96Tt6xxGcKsx3R1j3KMgTdmfFEzVDEWnSlol3AuCY0f9rcL-5VQWimgwFSL2dF47YY5O-fyNS04gwgmxVM1vhZHNmfy_0zzHZaJJNn7aucMnOPdZapqIYIxzO8JYO-KEHmIdf77j5DD8cTUShCPD0nQXdqPTL_Zx_UQtqD4npmV1cVmkyOZOXan90vYzuxCUh9wGLxU3cKjL-yvuWxg0qR7bx8suW38YurCR0_9N8TxPJmNzV9MbqDok7ms-HPbLLfzd66dvlwigndROc_0EwKlM9yJJDzQh82GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21116" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21115">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تایید دیدار عراقچی و ویتکاف
صداوسیما:
با اصرار نماینده آمریکا دیدار آقای عراقچی با ویتکاف در حاشیه مجمع عمومی برگزار شد
ابلاغ شروط ایران برای بازگشایی تنگه هرمز دلیل پذیرش درخواست ویتکاف برای این دیدار بوده است.
رفع فوری محاصره دریایی، پرداخت فوری همه اموال مسدود شده ایران و پایان جنگ در همه جبهه های مقاومت از جمله شروط ایران برای بازگشایی تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/21115" target="_blank">📅 23:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21114">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/big8tbY5e-psGLjEkR5impLXyVH_-ASHOUxfgzqaVHCQNBU0tnYnDweyXRxguorQU7AvP7_zTSJXfey8BvHzBbfXWQnBTGWnYHIsUYPE24Kj5i_VG5CpgwhrXrhIB3O8ceD_7X3Bvf_EX7Ue99wNwNNpCm_A2DE78HciBZvSIMeUPBG0Kfsn64qHlmHvoD6RIzP-FBIUnGbVsT7r6btWqY-B7RZmCZcQy4jIVbcKCEX8S_VyNH-B76-alavQZ0HyL-5JYtLKhRysRWhCevJq8gDOwnoNmlv2Am_oNfCF6rbfTlBvKzMbW-s7n5QsaUs1r3hrohz-zsL8M76LLJUZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد بز برای پاسخ به کشورهای همسایه که در محاصره ایران نقش دارند</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/21114" target="_blank">📅 22:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادعاى ترامپ:   ایران در حال مذاکره با ماست؛ روابط با ایران در حال توسعه است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21113" target="_blank">📅 22:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLU3Oeu1uTpStiJSBm5pJpKhp2EY2DjbQbbEXMbAtfnNXYRVzydCur_ADssC6B8NiYo1OVPnT3_7zaKqT3fnfxg7t3JKNSoxwJWSrCukiZLIsElT88kzmiaPSzfzlOMxt4GDByFSzgWfboxfTCJd95Kf5RDvVcVTiW6SaKqSq3MeFkthTO_AceGzAdNlf2C8WvakhdnRkMH34Iz3r5I1hDg_wqEgmHSux69UKFy1grHqYGNVcdtIdqI-Z89r44_XQd7rI2IUlY6hU28k3H1SAapakEQjM9j9tkWHxeAyQzVli-LPjvg0OwrKSfdwcXIdn2zfXD4sf9KWJPMkvVXUHFSY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLU3Oeu1uTpStiJSBm5pJpKhp2EY2DjbQbbEXMbAtfnNXYRVzydCur_ADssC6B8NiYo1OVPnT3_7zaKqT3fnfxg7t3JKNSoxwJWSrCukiZLIsElT88kzmiaPSzfzlOMxt4GDByFSzgWfboxfTCJd95Kf5RDvVcVTiW6SaKqSq3MeFkthTO_AceGzAdNlf2C8WvakhdnRkMH34Iz3r5I1hDg_wqEgmHSux69UKFy1grHqYGNVcdtIdqI-Z89r44_XQd7rI2IUlY6hU28k3H1SAapakEQjM9j9tkWHxeAyQzVli-LPjvg0OwrKSfdwcXIdn2zfXD4sf9KWJPMkvVXUHFSY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روند ساخت اسلحه های دورزن در یمن!
با همین تفنگ های دورزن، حوثی ها صدها نیروی مخالف خود را در هفته های اخیر کشته اند!
ثانیه 29 جالب است. یارو در دهانش قات می جوود اما دارد اسلحه دقیق زن هم می سازد!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21112" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خاویر میلی، رئیس جمهور آرژانتین:  نسیم‌های تغییر به نفع ادعای ما در سراسر جهان در حال وزیدن است.  اخیراً، رئیس جمهور ترامپ اعلام کرد که ایالات متحده در حال ارزیابی مجدد موضع تاریخی خود در مورد جزایر مالویناس (فالکلند) است.  ایالات متحده در حال بررسی این تغییر…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21111" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=uldVzaCDyg5LotEZokyA0q3YxSo8gMW0pOTaphhGUz4zPPaN_ky3iyiUq91CZ7Mh4qm50vyY9Xdx4qtyqm_ZIYa8lfkultyeLbgTM2zzE_JPA8Etv_ObQOtk2BB2Wq1_cIQ_vB2p1w7tW3cJiANXtbQxkC-Cy_IsBVXJh-iYtUTUp5AfbtfDMd37KeIRLVNFG8r9-YdJ2ZyPm5bA4RZ0zX7_cP2yIHDAzLEA-QeblB4pCpcj9oGhfs-PSdgydddCUw-IoSKWtkPLkVL9JrMxE1noNcZqxW_TVCUp_Xe5E_D7u_pMBW8mESJAn_0YSAnDQ5mv1eL6LsIkGanOZDiaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=uldVzaCDyg5LotEZokyA0q3YxSo8gMW0pOTaphhGUz4zPPaN_ky3iyiUq91CZ7Mh4qm50vyY9Xdx4qtyqm_ZIYa8lfkultyeLbgTM2zzE_JPA8Etv_ObQOtk2BB2Wq1_cIQ_vB2p1w7tW3cJiANXtbQxkC-Cy_IsBVXJh-iYtUTUp5AfbtfDMd37KeIRLVNFG8r9-YdJ2ZyPm5bA4RZ0zX7_cP2yIHDAzLEA-QeblB4pCpcj9oGhfs-PSdgydddCUw-IoSKWtkPLkVL9JrMxE1noNcZqxW_TVCUp_Xe5E_D7u_pMBW8mESJAn_0YSAnDQ5mv1eL6LsIkGanOZDiaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:  باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.  از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21110" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21109" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آکسیوس:   تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21108" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آکسیوس:
تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SBoxxx/21107" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:
باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.
از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت بشناسد و روابط سیاسی، دیپلماتیک و اقتصادی با آن برقرار کند.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21106" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !  یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21105" target="_blank">📅 19:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=WV-Ur-x6_aHVABSieVAxDJ0jzTV74YsQtBxVxEDOM5vZJ72FAX16FkfrOjG9JVT8-GLcPtoycnLpG9ChODNl1XD1QICJ_xJcZ88dH9Vn6E21fmFlbg_HJrqBXlBoZd9y3aU-aSWFV_BMq3V7vAARunoc8-J7iAUMoaAMX2nXRurZIkRvCrJGNTb-1WRiLe9AbyWDTl8Jmg77mm_p477wPMpP4nPXUUHz_eqr1gPlwisgsrRqQEMaRJlKeEAQT6w47orl0JO55Epf5Kz2NBR9zPMmiRgg5ZBE-Kb8_WT95eTqysQeL3KXWt0fu2juW79SkqkQBoLy3gOWeTSQ4j8WNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=WV-Ur-x6_aHVABSieVAxDJ0jzTV74YsQtBxVxEDOM5vZJ72FAX16FkfrOjG9JVT8-GLcPtoycnLpG9ChODNl1XD1QICJ_xJcZ88dH9Vn6E21fmFlbg_HJrqBXlBoZd9y3aU-aSWFV_BMq3V7vAARunoc8-J7iAUMoaAMX2nXRurZIkRvCrJGNTb-1WRiLe9AbyWDTl8Jmg77mm_p477wPMpP4nPXUUHz_eqr1gPlwisgsrRqQEMaRJlKeEAQT6w47orl0JO55Epf5Kz2NBR9zPMmiRgg5ZBE-Kb8_WT95eTqysQeL3KXWt0fu2juW79SkqkQBoLy3gOWeTSQ4j8WNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !
یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21104" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ:
در ۱۲ ماه گذشته ۱.۵ تریلیون دلار در ارتش ایالات متحده سرمایه‌گذاری شد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21103" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یک مقام عراقی به الجزیره:
«به فرودگاه‌های عراقی اکنون دستور داده شده‌ است از فرود هواپیماهای ایرانی، از نیمه‌شب امشب، جلوگیری کنند.
اقدامات انجام‌شده علیه هواپیماهای ایرانی مطابق با تحریم‌های ایالات متحده است».</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21102" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21101" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">— مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ترامپ آمادگی دیدار با پزشکیان را دارد، اما باید بدانیم که تصمیم‌گیرنده نهایی در ایران رهبر معظم است و او یک روحانی شیعه افراطی است».</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21100" target="_blank">📅 15:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21099" target="_blank">📅 14:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سخنگوی سپاه:   اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21098" target="_blank">📅 14:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21097" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 28</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 28
سه شنبه 22 سپتامبر  2026</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/SBoxxx/21096" target="_blank">📅 13:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTM3_SOaNnL5YQK4feeqXJrW0LSzcZo-28tN0zqeXpYHyRQNQBPRbbHiBAJqkeIcJFVu0NkX3fHk8u7_bND34oP3WInye477Yyaj4ult5fpcLOBMKB6xFt_fsxEo3pQszqxyd5JxerPB3bCNK0-Ll6eVxzQDH3RXk9RQ6eYUuz8bMZxaa_x8JPpJl-lhfIhvTwI_GXak4QHgFkStoOewcxlX3yYGNTXsHDWbNLwH9RzoqCMgmzHMvSA0S_S9_0h4NP5hV1me8bTRK3qwD-gYP20KRQxvRWqbXBIF_rcqPOGPd62aQ20neCa_5r2Nf_YnRUzwC9B5iTaKWjxBCmHNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfeFG9ZIOat5GbI2FjxVhP6HaudOaTx4Y6qumTk0dXu44pg8r-nDf72IVT_oYsd79eRVsKf6mc-DcFjSobycEYeg4H5Kd5H48mcKpI5k_NGS2t9a6iZp0kgPvDOKDbqNup0SHFlukNV_D2GLdTNepIT8HgXorbmwm58RmMPnnOz6-oW20KZdNySsetOAut0ye-J41-wUKfRVq9AkYtVSE9E5hl0zmJWKpR2ypAZ59xPklbI8heo-Os41q_KPtg1Om9ghzwm3XEfJHtcVLvml4gMhwK44cw5j1vooTAOl-cHRFNiI4aUgOkUM1Qwag1jVomVJO6j9xhFiufE-WKrzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve0CQETQe7JujFm4_7PJvpGcC2R04GI5UhheTybiUEOeY4YOPyffDhW_6ZfLmr47bZdcgPu22docRHDTcG6-G7felfIH_oWAAy_O-lGm3opmeoqndtW1NpiiBx0-hUIqmI-CLcNyPxwN8LxGmz_fwKpoS93tCXaKC9x3PTwbb4gdCVBuhYOSPOhFNumYD83vBaVXo-o-ZeSLDqNUbKtC1BxS0eRVBwCe3HDYZqr-muAkK3xx3Lf8oIud6G_zokCay0i_nUogjGj5YBblU8Fu7kLnQPd0-Khk4tvnfroPgPSQkuhNKqtQfp3HUlNlmbT2bgakcDE5nIby5sZAin7itQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21091" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/21090" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21089" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21088" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21087" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPEZpxayZ8DCnQCZylgS7f9-3Kj5reqy1hJ0VUjldchbGv1EDOIIyoyLo8MUmeH1BijBEefp2dLnEp_IrKvOoIAA64LuB6VJCRyQb6Xu4NWeQlyA4TdjGpcG4_JsVIknTzSZEYJQA-XA0HfQADkca6PcltZX9X2oahjNM-Hgp5HThDojMnP4X_bwrHBOmD4ZMvFV5xflIMqH7kgO9VEiC-V97Up_9hlJvNKXtFuMv2WbjI-umPd4xeA4QbVxhkAzvOfuHbNJ9AkEXu_DdFJwUUTPEc3mMVR3on47uwuDOFiRbGP131UeU4O2_YoqTSx7EqG8TV8h78a6RgswQAW4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/21086" target="_blank">📅 11:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZc_L3xb-Gh0e_FRpzLbGN2TiKjCH0Je2yVcuY_GS8iZsYpbCHOZMNtFatklQxhfn-ij2VBE3fMn6ne4j0aWJTCxSGlyefRMb4M903kVx54SqZ2ufSRtEipa-AUD922w6-XPhZjrke19RFPFHM7-u4JBuhThDLmiyrck1-55vSbc2ibaTKkYIJBQ4U7hH1_Oc_q0nHEIA44NhGttlq4PEP3YnV3MvkOw6bi2H5S0WF1QolPdwxcFTh6m96OeAzAYMS3xwDrerv7wmXafSzryOV40iP42fP45Hjhv_HROuRrkXQs9KqQq2O0r4m5BkCwEb5ryNZH3UpTvojLwo1opcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است. اما نظر به ریزش سنگین طلا، اثرگذاری اش را گذاشته است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/21085" target="_blank">📅 11:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un2XoJFmUjP4rRKkQBOqcaCTODwMwNPyr9a6j7Q64_NgneG_H5gAmCyu1GEmObtpxvPeX_Xae32kGkRYvYE_CvRMd7Ph16iIkj1VWTtqOwewSOp1xqUPoDFs-RS6j1I2x9aw4IkKlNIXprqklc0aoNCIQxiJqYNF6hfwVEmX-PkmuxTLkhlCaTSr9ZuiL-iVhR9ojpt6JGXnvbbp2_tC_9BGto-7hwWHDlfOzmyUyF1Zduq1ooP6CEcTkLp2fozCzxxSEHX7rjkI9ED_4hM1VDGXZTtjI27SYNm8YEABrdIxo_iTgW9lonaQE2Q7wN8FwttoY5BsyVJfbI8Hf6ug0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پله خرید طلا توصیه می شود.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/21084" target="_blank">📅 11:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کاخ سفید، پخش ۲۴ ساعته‌ی «کانال تلویزیونی ترامپ» را آغاز کرد
!
کاخ سفید، پخش مستمر
«کانال تلویزیونی ترامپ»
را از طریق یوتیوب و پلتفرم X (توییتر سابق) آغاز کرده است و وعده داده که سخنرانی‌ها، اطلاعیه‌ها و مهم‌ترین بخش‌های فعالیت‌های دولت را به صورت "به‌روزرسانی لحظه‌ای" ارائه خواهد داد.
کاخ سفید در پلتفرم X (توییتر سابق) اعلام کرد: "شاید همه لحظات مهم در تلویزیون شما پخش نشده باشد، اما اکنون این امکان وجود دارد."
کانال یوتیوب، این پخش را به عنوان
«پایگاه اصلی»
معرفی می‌کند و وعده می‌دهد که مهم‌ترین لحظات و بخش‌های برجسته دولت ترامپ را به صورت ۲۴ ساعته ارائه دهد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/21083" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZQELLtD3zwW6TuaojYY5OEDhp7WEm3Kpzsz3TKyCsVbxzqiHf-hlZbXIr4vPoQnvKf28JOqC1G6gIQrW72s6rJYvuFMQUWA-juVY_uniB8WvUvc-vkNZrMgb6Jb8idJ4_mvNd09F-crzQzl0yPIDB_LD0Wu74kXpMjIYAlX7aou0aXYEZRSuuM-jyqj2W_jGN_kiyf6qkbe25RS_Z7qGk3nV7ytsSkZsf6vIKZzu9Cypw2yvOCCfeZtK6UsgcEDyJzaTTK3leO15mz6uYOFoBYMkAEoDQinaGiynIr2VFpquNQVUyHu59itS1yeb1-iCVWCobVj5IswQ_Yh5eSIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/21082" target="_blank">📅 10:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS14if3DG4DOauBQ2IztQm7tOyfuPydwuSqqjKqFdQqlA0ECkP4jHwcAp7ZFD045x2NsrIKgRazDaktePncqR1KGjlbn3GQsCrwp9zw3PwjQIrftArLNl16I8bKUHzUG9EXh8SStLCdYpB9a-c5ot9EBQ95XzZHzu9CfZLvT8Pmsbv1hWxIF__xN-DYfxakhODyQW3KIn7VnEMsuXXCFBhZ_Io6Sw-KubMsVvxxOa-ES8llpRREyFuar-L3kGd_LoHgzbO-GRa9lAE9F-XhkNnywiLLKI3TnEEmCfqJS4JalRj6NSvCxoVLpn1ZDWOhhni4fjHrbqhctv5x7ob0wRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه ای از جامعه ای سرشار از زور و ریا!
حجاب اجباری بر سر دختر می کنیم تا در بلوغ و بزرگی محجبه باشد اما همین الان مادرش بدون حجاب است!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21081" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
ما آماده‌ایم همکاری‌هایی را که با ایالات متحده در حوزه‌هایی از جمله انرژی هسته‌ای و LNG، حمل‌ونقل هوایی مدنی و فناوری‌های پیشرفته برقرار کرده‌ایم، گسترش دهیم.
توسعه بیشتر صنعت دفاعی — که به‌طور سنتی یکی از قوی‌ترین حوزه‌های مشارکت ما بوده است — هم به‌صورت دوجانبه و هم در چارچوب ناتو ضروری است.
ما می‌خواهیم موانعی را که هرگز نباید بین دو متحد وجود داشته باشد، پشت سر بگذاریم و شتاب تازه‌ای ایجاد کنیم.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21080" target="_blank">📅 07:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJfurY7ViwfZbpPllH4KYDlldx9Bn0euUHnEwmudWFOo8KcTxEKZiNUbzCVb1n5lvoADBvDp2IzXTB5DgFGXS-cyKGUpUr3UC_X7sygDib_ojCo8WhBgETtzvMZ8ftAGLOfwCMPPPtml7lA2GaD_8NLBMdtBePr6rMtWuwkZcyQv4QA9pZvmkFuqfIk6fOsoW1uTl2hzUtj0FFF_AV3aU_jC3vEhFe0C8paxLDa4aL_2vzzlLI_TY7-uUydeRQHRpYoNKy6B2H6QL2Uo8IgG27Go0wlUDFBBLsy4GSE2CIt9pVxDpbciRb6Qe0Z-KCcOoI5jfV4THZ4WYLcCpMhQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
دلار، نفت و موقعیت های معاملاتی گرید از دید موسسه Danske
موسسه Danske با توجه به رشد اقتصاد آمریکا، سیاست انقباضی فدرال رزرو و اثر شوک نفتی، تداوم قدرت دلار و فشار بر یورو و پوند را پیش‌بینی می‌کند.
در بخش معاملات گرید،
GBP/JPY
به‌عنوان یکی از سناریوهای نزولی مطرح شده و ترکیب تحلیل بنیادی و تکنیکالی، افت قیمت تا محدوده 181 را مورد توجه قرار می‌دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21079" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiAuG4mbYCcaPQ9G483xqemqc-D6nL2G_spPDfrc77eOZm-kd6F6AU0U2lTQJPhX86SDJc1_IU54WugyV5Cjz7E7Ob9bOkvofdlESqjYFynyLxC0JRCLgNZUZ5dDiZOr13K7JhpF1cNnaoZd70XL9LMgVIsoIl9Bbm3DocZK-8mLCUSVa3cCehOAjRTkyv3JGEL4yQuDJB2V_v4UMi11R2r9Forj6TWkmH50e-NnFqaoJBDXdFnW9bfz5u-Dd4APH_w_OLmIbAfC5VERDumi-_kfHPC7U0t16JAigZ3gaNcI4INqmkYTySihC6EYsUtCUsEe6AOO9_ofgwy9lHUXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk7yYnTWVoxSpu-f5-erxPvtSEHWpsmu4qMnHR-6VPCoRBOL0jmU9Gw9_i7Nh-9y7nH692xlPZnWdj3DDlx2nFR6uVso_zh85nq_lKlmE0j54f-1kLwgfdzkFsm1PbrvnITbmQqM39n3WojbIxL9ACKYefdJ7gFTPr0wxiEblMn6edg30Gkal8gHhNXF5ZlEi4wsB18ixlr1om05oSXV9-NBhJ29lyZr3Ro52QaO_1DFizEOlSZJOben5bEPel0mVnUcdRbokCVDrJEkd7HmOtCK_YmWTC9k9t4UCm4ZqxuAovsjbAHiaLWmBjSq7uDumVHcO2cYgMjtigP2UGNYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2Rh4vrhhqaKPDcury3fbPbq6F-K9EOatAimz-a7DDyGqrCILwMpbYziTgTymeyJLCBo2tUrP-Z7JXQLbERDONYe9qYxiUNuQOeN6X1tizsaU1Bwm9g1bQVlwNLXeRn9WEt_gfygQ0NcNqtOXG_6C8FkoMoWFJLUjybxJZGqg_8qkHvSWZSnIfWSafkEiFdaMMinUALOlOTLYFdE6kmuTtb946EKlBSaSkV-Zpq7UFyCCkZXO09PeIOFYoAK2VyZ2TMxpGB4Y3B_-o-SeVCheyTBxdb2_7u6jMZt0PsjHfDbJbN8LxR5OKV9LHykDHMUP58Ulq_grtJAAiJeGVtWpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق سیا:
اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت.
کار اسراییلی ها اینطوری بود:
«در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار.
اسرائیل هزاران نفر از این افراد را استخدام کرد.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21068" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubkB2-7Vz0CKuURpOYj-F2LQ_0RkqEQ5jNg2mhgNhZOV6iZiewDaTuSfnqXw9k-27ooWzo0B88H6eEckg5pvhhwptgaEWUeM-kTRkJRVgUzZskfr7LN_e0iMLrHqwY-_AIFuXnaqwSG30yu166gP5gVcG60Epi-_dYFBxjmaVLwYMrkVvONf31yOVYQ4W3I_GOrI21ZpaKwRDQqGnSLThqpAPbpvtrqIXFdPbxKZgLadHoMQ9iarzkv_tlxziopDFLeTL2v15IPSxPmk9nvj87tujvFJccJxNLf3-eMgfJKZmRvBwQVJubNei9PHIddSeFACDZl8ucZnvZIuuGJxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده زیر قیمت منصفانه قرار دارد و لذا فضا برای یک رشد در طلا هموار است.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21067" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPU-wSsF1IFZMtzvbZiurDRQLBp_Y4NFgC5WHTk3HUJoyfo8q_F2tA-m_RqAJWOW-fjqejgUovmPPMtydlqnjMwI8yftsFSwhYCZv09aU1N-n36n28R_QCiA2QiPe68f_Z4pZuJkO9_h1osO62059AQMoUHR2gvOQefNe-Gomvix92f2VVa_5GJ42qw1bDfJD7YjGEXXdqF12sa-FC_-qxo2RQoJWVUvUlqEdlZ6ml6s-fdlpaxMJGm2sCX6-F-Y5QZIu5zperNIg7Mb6wNS-h0TkHOU1EU5MvV83BiZq74C3vZu4ooRvhocYW7w8RRAEn0dQRhT3pDSGqCa7sQoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21066" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قیمت متوسط گازوییل در آمریکا برای اولین بار از
۶.۵۰ دلار به ازای هر گالن
گذشت. از ژانویه ۲۰۲۶، سطح عمومی قیمت‌ها (موزون با شاخص بهای مصرف‌کننده)
۴.۸ درصد
افزایش یافته، در حالی که قیمت سوخت خودروها
۱۷ درصد
رشد کرده است؛ این امر احساس بحران توان مالی را تقویت می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، تمایل خود را برای دیدار با سید پیش‌وا (پزشکیان)، رئیس‌جمهور ایران، اعلام کرد. با این حال، گفتمان طرفین همچنان منفی است. توافق آمریکا با دانمارک درباره گرینلند می‌تواند گامی مثبت باشد (بازبینی یک توافق موجود می‌تواند یک سابقة مفید باشد)، اما عدم اعتماد بین آمریکا و ایران اوضاع را پیچیده‌تر می‌کند.
مِرتس، صدراعظم آلمان، پس از باخت در انتخابات منطقه‌ای هفته گذشته به چپ رادیکال و راست افراطی، سوگند یاد کرد که در سمت خود بماند. به صورت ساده‌انگارانه، نگرانی‌های اقتصادی به نفع چپ رادیکال و نگرانی‌های اجتماعی به نفع راست افراطی است، و روند جهانی به سوی قطب‌بندی سیاسی پیش می‌رود.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21065" target="_blank">📅 11:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4rCFooz4xxmVG3aK30drxeq_27ceRZdnMRC2zcOF9vEhF_WPfPS3iAJo4yuYFRZzh3c3fSnzjQDd61vdX8SLrnqoYxhWwnhWvu_aitfq09loxsShhLflSysEyzuHASUoXXahuJ7Ehieh7qvdvsR_r_cRZmBhwN24g08RsrBfKFffhCgw-jimiTkVFM4rjjNOgmGF6Hzji0Two4jdLQNw3K_pO90QJEZ63AywSwRWqvY34w56v5Nu8EbqekdbpqtepnutzgrpCwK-02GTWubcVsRmqXu5H_VnBel2hs_ZtcP1XDYbwRl8h6eUaJBhDjPG4A-ODMR4GuZs0Vkb0ksQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین میزان اوراق خزانه‌داری آمریکا را به پایین‌ترین سطح در 18 سال اخیر کاهش داد.
چین بیش از یک دهه است که میزان دارایی‌های خود را کاهش می‌دهد. این میزان از حدود 1.3 تریلیون دلار در اوایل دهه 2010 به 618 میلیارد دلار در حال حاضر کاهش یافته است.
این کاهش پس از سال 2022 تسریع شد، زیرا چین نگران وابستگی بیش از حد به دارایی‌های آمریکایی شد.
دولت‌های خارجی، خرید اوراق خزانه‌داری آمریکا را کاهش داده‌اند، در حالی که صندوق‌های تامینی و سایر سرمایه‌گذاران، خرید این اوراق را افزایش داده‌اند.
کاهش تقاضای خارجی، به افزایش نرخ بهره اوراق خزانه‌داری کمک می‌کند. نرخ بهره اوراق 30 ساله اخیراً به بالاترین سطح در حدود 20 سال گذشته رسیده است. افزایش نرخ بهره به این معناست که دولت ایالات متحده برای استقراض پول، باید مبلغ بیشتری پرداخت کند.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21064" target="_blank">📅 10:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ملونی ممنوعیت پوشیدن بورقا و نقاب را در مدارس ایتالیا اعلام کرد
«هیچ‌کس در ایتالیا نمی‌تواند تصمیم بگیرد که یک زن جوان باید خود را پنهان کند. برابری بین مردان و زنان نه در خیابان‌های ما و نه در مدارس ما قابل مذاکره نیست»</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21063" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اقدام بی‌سابقه دولت الزیدی:
یک “عراقیِ ارمنی‌تبار” سفیر عراق در آمریکا شد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21062" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PILa2K8jDoGEGSvRoutiJjeLeV5RKf11EtIK4LTrEdJhbwNOfl3wqvVvB5J50Rp4ezsKleeniBHwlrkkRzSR69S3sF5hX16Kox5NRvDUPBkIycFEjMInMY3F_ObuF17XHzewxXpNri2MyQ3arLz6OJ_yQS1tLQJbVSY9nCp_QIGf33Mz3jekUwd0pExX3WIIndMiydONaWk6Kc0Jami6bAauEobnI3jmXgCIaYceVFb9OICBjPxXc5BkITXay0lth9L4q7c9X5p3iaVhZjabQr9vFvHqdJzIkn9ZOatNJ285BdlMUvluP8A50YP5s5tNsAJfTm4XSvefa-i_xlNpUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یعنی همه چیز دیدیم جز قهرمانی....
هعیییی</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21060" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21059">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21059" target="_blank">📅 01:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=CFloitPIezFkqkkxV87n_T1T2oKAssZRCWrAoekvzUyDWiteq1in1JjMx8I2SxVFkiM9_rTiXw1cIh0BDSLaTDweUO70NctCzqX9cMrC6WHlToQ5pkTq-5VgKlkBgH2Lc15BYlZui_jSfxS2RCZGWpMAL1cWa6QyIb5rbIoykA8zvyA_PhGzVGQDVBh2_lVLUaRvBmSgpPiwakRiqkCVraljmBu_EbgNlwmmMzccYhZoRkmF8MpPhFIqNOBTidCP-7UIpq-nefNM5A3tC49QgdVmBeV2zJ2dsqw1M2QrIKJtwwjiGy1xl86GgiVFiJRy_N67wiTUoyKOegyVhn3c6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=CFloitPIezFkqkkxV87n_T1T2oKAssZRCWrAoekvzUyDWiteq1in1JjMx8I2SxVFkiM9_rTiXw1cIh0BDSLaTDweUO70NctCzqX9cMrC6WHlToQ5pkTq-5VgKlkBgH2Lc15BYlZui_jSfxS2RCZGWpMAL1cWa6QyIb5rbIoykA8zvyA_PhGzVGQDVBh2_lVLUaRvBmSgpPiwakRiqkCVraljmBu_EbgNlwmmMzccYhZoRkmF8MpPhFIqNOBTidCP-7UIpq-nefNM5A3tC49QgdVmBeV2zJ2dsqw1M2QrIKJtwwjiGy1xl86GgiVFiJRy_N67wiTUoyKOegyVhn3c6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/21058" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=VOB6KZH_0SxUWmRtvOdrUel1MR_vlY68D6ixCDDBlf7r_nfx_0B3NgUIaJowWKLpGAsVeKcQSRwFsIdaRP7g0_MwnmHhwdbqKph1SFjY5wkwL3Rj38CFvdmHcr5kudnPHnTu3fc0tM05XNViyMWo29GWTpmiPEnUEtu97WqIh5jfMVRH8j_ZSAUessykUUJixp_qMJclLahZ6YmyLc6ByKz99zY1wBHoWBWl_GntDrwF9jIGaD-xJxqch5Xj7J0XtmciypDWHWBNUjGBw16hSP8zJMbN_W-9kf67nRPqYW0cja0LKPYIijNxDK63GOFBZIDpWMtBNFINQnmcxv4SpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=VOB6KZH_0SxUWmRtvOdrUel1MR_vlY68D6ixCDDBlf7r_nfx_0B3NgUIaJowWKLpGAsVeKcQSRwFsIdaRP7g0_MwnmHhwdbqKph1SFjY5wkwL3Rj38CFvdmHcr5kudnPHnTu3fc0tM05XNViyMWo29GWTpmiPEnUEtu97WqIh5jfMVRH8j_ZSAUessykUUJixp_qMJclLahZ6YmyLc6ByKz99zY1wBHoWBWl_GntDrwF9jIGaD-xJxqch5Xj7J0XtmciypDWHWBNUjGBw16hSP8zJMbN_W-9kf67nRPqYW0cja0LKPYIijNxDK63GOFBZIDpWMtBNFINQnmcxv4SpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستندی جالب از روند ساخت و امکانات شهر موشکی یزد!
بخش عمده اش به نظرم با واقعیت همخوانی دارد اما در بخش هایی از تخیل استفاده شده مثلاً بخش مربوط به نمایش طبعیت و روز و شب برای کارکنانی که 500 متر زیر زمین حضور دارند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21057" target="_blank">📅 01:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKwx2tEwUF9tGo3js0Ml2iCYV_3v1BODV1vfhZ3BYfWjuFgl0EprUGlCVEfnksPZLEHxvaD0TAhiGzd2sGCh3PQ_4GwJX7xg4QCUVzD5yXrqM-6ZZbbbwM_Wrp8_li7E-XIgRhiGqcmVqt87HMDZAKIsLO34BNHEKS4gXPdWbWGSfuurVvod3-VaJOBLKeNJqUuyL6nIlSGzbQCUFQHv_dRFs0zNLL4BXS-iF5ED1qow8kiee5mgyhKAJILTToGguFn693x_F3PbsY9Pl9xHc3MWsA42dcJUCzwcqR2OubJoJtoITvIYHsUunS9K5b15fWQgM6Tsbs7ZA1EdM3rY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21056" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم  که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21055" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7235f04196.mp4?token=TTSPodeKhRoKN-OE_zbHSJwD7lDeOn4-dqzh9JqF49BQ-gwnGadFs2nU1TM8UnZwQudaqnyVrvR0FA58p9-XBmOkdHKj_iiXyULnlZhwypqaEor-eajLsRlxfkCKxMfWvKE0DUAW1bNCRhccjhnt6FXvJbPLxqKWXnMAnpAa9IciGAfHe0BOHOgHwBD6N2AcrnYOBmzIxvlEVNH0cXJ1L72V7MyaKnE6Bg-7moEBAHVR46352A3QGG25yQwTSEzYaRIyt-Nwa5H37kKRY0uPnsoFyW_NkQO2ge6dGyB8mX5d433_e8KDBG7UU2s5_VDFOrRZUkXzmFus7LDtxocWUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7235f04196.mp4?token=TTSPodeKhRoKN-OE_zbHSJwD7lDeOn4-dqzh9JqF49BQ-gwnGadFs2nU1TM8UnZwQudaqnyVrvR0FA58p9-XBmOkdHKj_iiXyULnlZhwypqaEor-eajLsRlxfkCKxMfWvKE0DUAW1bNCRhccjhnt6FXvJbPLxqKWXnMAnpAa9IciGAfHe0BOHOgHwBD6N2AcrnYOBmzIxvlEVNH0cXJ1L72V7MyaKnE6Bg-7moEBAHVR46352A3QGG25yQwTSEzYaRIyt-Nwa5H37kKRY0uPnsoFyW_NkQO2ge6dGyB8mX5d433_e8KDBG7UU2s5_VDFOrRZUkXzmFus7LDtxocWUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم
که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21054" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxQUg9cH53avpwC6zQCoPGK5oM4MyNnYHbCAvRda3xuRP76CBUcvfunYEHNN1CrdquuproRW6gSkwLYBCc3V5fcK0_XYtV5jMRHN_Knwhl_NLCGJ3nImpjH91hzjwk5SsKvQrQWZF81QnOq5HjEonm2k90gKB1AMtlxogT-TfpbyI-WHOurHnj4UOSxceDuRA9LWuTtLt0-7VTIHgahndbjegwFjjK46ILGsUtWUTotcNga2h77tIlH-Z1vl2up5X3s338Pzx5bAh0Gg32cLtjYRsPO1XApiL4vDRP62B9Fw5flsJo8E_qgQUX-O9b2tsHj0m1mjjYoz5f8L9muOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21053" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21052" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1D0KvstajZ_EAx53dECHxYF3qSszF7p3jkIV78BwMg_bUi3RZ_bSJVEuXGhzWuKcQZ6HQlVNPRV4n9rTop00n3IwIeTUvoXY0b2q0oRkhb-N_F8UsBTvG-D7sWcaSp4_7uFiNYYhTMY1einwnmz6B1pWfvLNvyHG63F4nsVHVbp14O3aoHdnTx7AqvMvfWvVk8vmPeV7tuG-738rZJVG-GrsP4P8wDv2isvBCoMpA0dBA58wAHL6GbAHKxeqLqbYCKj0FVgY9YYE_FgQu9Gzj3fVBhe_v4JXqy3AGgpbOeAon3Y7640kH50rpRvtEbjuDZ0Y_UA_0_hzDhJ-ieOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21051" target="_blank">📅 23:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حریم هوایی اسراییل هم بسته شد.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21050" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMYmr3z15Er86Kcf232vgiODvvjy2LhDtMl98V67qLbvb42pfjtcie7Lp3RzaDHU3nynSuTz0z3JzRfwa8wbO9UeCAUEIqB_xr0mJasK_hm2-_ELFoDroC9UVmnrhjvpfW8a2yggaME3NPKQYsxaxm2P7GP4_-LK4Cvpn3yzXx0VmajKNcwQpk7McAivKeuPTjRuhZsZryMIwa8ohaS4ZTSBdmEddJTLnXrKfB6Ywl_4pbeOj6UOhWd6DE_XKTM8mT52s48sDlyWIaIrSVqAh6IHpbFg28UF_kwGo6JfbDkwIJW4K1s9gj9HIpYD-XavNdOqrn27XbNBLMnMAKukiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:   صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SBoxxx/21049" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قالیباف:   هم میجنگیم هم مذاکره میکنیم</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21048" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین  شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.  در بلندمدت، اختلال پایدار…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21047" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQILIJ_zwhq-l8JZ2TEKU5BxcwWPgext3aprnZSrg8_WYgfBPSC3Rm7hIe1HQLtG7KRST7zv6JuZYKNJ_tyvGV2-vKnwU6-qP32N0maX5qWeTFtYLTpMiDHS7CrwPalvJMX4zL_KLR93ztMopCGu9eWCMokG8lWscPlx2w9oE0WtOXF3bU1TYx8y7C4Vdhv_IW1rCADC7qmk3DLwvHA8X7Yn09Eua-f79RtP-Ut33kTH5_-hbFdPnpwiXJUyvIKETcSCoyu_OhMAL9HPHHaPicKdEr5h4eJLqsQ0U4fC41DufuHh7fW8QqaUVoGZzVyjVNSRCKjcR6e_8fVDxFXXfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین
شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.
در بلندمدت، اختلال پایدار در عرضه می‌تواند سرمایه‌گذاری در خودروهای برقی و انرژی‌های جایگزین را سرعت دهد و وابستگی به نفت و اهمیت استراتژیک آن را کاهش دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21046" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ به فاکس نیوز:  برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21045" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21044" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21043" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21042" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21041" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی
#إيران
، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21040" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز:  در این ماه، ایران فرماندهان سپاه پاسداران انقلاب اسلامی، مشاوران نظامی و تجهیزات مربوط به موشک‌ها و پهپادها را به یمن تحت کنترل حوثی‌ها منتقل کرد.  یک پرواز شرکت ماهان ایر در تاریخ ۱۳ جولای از تهران به سمت یمن پرواز کرد و بین ۱۰ تا ۲۱ نفر از پرسنل…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21039" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پوتین:   رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21038" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا:
براساس اطلاعات دریافتی، آمریکای جنایتکار .... بار دیگر تصمیم گرفته است با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21037" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فایننشال تایمز:   عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21036" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21035">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21035" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قالیباف:  جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21034" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
