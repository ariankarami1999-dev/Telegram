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
<img src="https://cdn4.telesco.pe/file/nFutMZfjMrMT3yVCbXjtQ-e2zPnVYKJKXiy9tVp4mU3NybvMEWqBlNE7-N6ZgEOHYYoeSfjKUAUVA7EeCNzDhXbkLiD_hSqnRIrdFTexqbB772YkSS4C0QSFF4zbt7IcUwCuK3H0QFwuuHfI97nURvzHwe3Ci2u4KLwJmOQUsgd714ZYD9FdVkmQZiLfTphEDtMqBYOm3xNINCtEQ2e5wazvoNxe4qeBgK7W6XFM-zKvIm3HVIitroARjIzFDhNqUKStTIKD_aj7J9apa1K1zIAVjEOsKJDypKpgaXzIW_-peq5FgsP3Y8Z8wA_p4lKGo0nGEntvDR4oob9swOjMCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 19:55:01</div>
<hr>

<div class="tg-post" id="msg-18369">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ در آنکارا:
شرکت‌های لاکهید و راین‌متال از همکاری خود برای ساخت سامانه‌های موشکی تاکتیکی ارتش خبر دادند.</div>
<div class="tg-footer">👁️ 316 · <a href="https://t.me/SBoxxx/18369" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18368">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -   تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/SBoxxx/18368" target="_blank">📅 19:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18367">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -
تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/SBoxxx/18367" target="_blank">📅 19:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18366">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بر اساس بیانیه روابط عمومی ارتش ۸ نفر از نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در پی حملات بامداد امروز رژیم آمریکا به بندرعباس و بوشهر به شهادت رسیدند.  سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم…</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SBoxxx/18366" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18365">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYHVQOxLXAX_Tm3QR6_Qd0DIaSeEROK1tQJcYp04ZpML90zKoCmoCMvyfdJilmd15TmH0MoUswAjq76UWvIzrgdgR5cEKs7IJRYryDR3Y5M0AzBb-DulWvB_-P3dZK-KK112bVYezx3ZgK7EG4-h3jaSM1GGkjrSup02p8EY0p8VIm_VdkkIn8nGPXy2ILrSJKKgGA2rb-_IsKE3fRH4ieqUrOPv9CcezHk1t-kiN6WmhTzYwJe5QQbgFVkTOxNBUKlw_FKZAWdEB0OUmWlzpvV7uV6gQjmMEyegu5xgUt6ssjtabDjtzdvlB1LoTn86JTfDdc_eYR2kaXWFRwKDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس بیانیه روابط عمومی ارتش ۸ نفر از نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در پی حملات بامداد امروز رژیم آمریکا به بندرعباس و بوشهر به شهادت رسیدند.
سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم امیرحسین قاسمی، استواردوم علیرضا زارعی ثانی و استواردوم علیرضا بالیده از پایگاه شهید عبدالکریمی بندرعباس و ناواستواردوم شهاب امیدی بزی و ناوی محمدجواد روانفر از منطقه یکم نیروی دریایی ارتش، در این حملات، به مقام شهادت نایل آمدند.</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SBoxxx/18365" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18364">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ درباره احتمال اعزام نیروهای زمینی به ایران:
«چرا باید الان وارد عمل شوم؟ زمانی وارد می‌شوم که یا آن‌ها کاملاً از بین رفته باشند یا توافقی حاصل شده باشد.»</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/18364" target="_blank">📅 18:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqyS4znHnCzzOIgym0BPjfnKTXTV299sLgScUWM9nbn60GXjdSGALjcG6NYbMlbiCbGQbKJiKLZhKJ7IyI40bLIqyn4PxrrZTOtS3U23tjl3wI521UhKS5GlhG4QhOA7CJ1d7jyawO2A9q8hjsmz37cfoLJ508Fmo_YNMM4DdN0TJKuOu7gnPaIlrI2SmL_bfOOAeG0Kp0OVoslxvQ_2eifGzZMj6RJbATT2O-_uUHJmxtYBtGJBqpRLqNu4frImmApd2rV6OaVpBmr26Rr_KsxAcT3WNknveXdI7SQiS2HdQEokG8ZGsxR17-OSVpah5VBCGiQ7BRdO5PXisNbOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در سطح بسیار بالا قرار دارد و ریسک گریزی آشکاری در بازارهای مالی جریان دارد.</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/18363" target="_blank">📅 18:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18362">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zaq3aNBFsPe3mR0NBWWxKTN4vA5H2GTtUO7owXrTvW-_yefn6ojXsaFkisLO8eYt1Y6kkQ9DVSkNw8KqCjVlf14-psWSxmg_U4H0PnqnTYt6J3BX29YZaf_NUtFd2TNOuGlhJ0zlvll9LirazTkAzBPQCx-NJNvB8I5KI-nQ-iUHRTulSG5u1XJXIBY48M20oCBgwcU5MUSKOfAoBNT2q4YYfINNPEn-X3WV6oZd99FIeMJycuu4cSBRwhUazAoACIUXdLteYCkiJWlhTFI3J3FiY26wjKZWSopuetk8NQxy9_rEhgyih5EC_WuxOScm7L-NpLGI5yf5flm6cvgy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/18362" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18361">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏یک مقام امنیتی بسیار بلندپایه اسرائیلی دقایقی پیش در مصاحبه‌ای اعلام کرد:
«دور بعدی تقابل با ایران، آخرین دور خواهد بود. ما از ابزارهایی استفاده خواهیم کرد که تا به امروز به کار نگرفته‌ایم؛ موضوعی که حکومت ایران برای بقا در برابر آن با دشواری جدی روبرو خواهد شد.»</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/18361" target="_blank">📅 18:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18360">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">— دونالد ترامپ:
«به نظر من، اسرائیل نیروهای خود را از جنوب لبنان خارج خواهد کرد.»</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/18360" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18359">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/18359" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18358">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ فکر می‌کند اسپانیا عضوی از BRICS است !  در دوره دوم ترامپ، مشاوران و نزدیکان ترامپ قطعا نقش برجسته تری خواهندداشت.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/18358" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18357">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ:
جمهوری‌ اسلامی ژاپن دیشب ۱۱ تا موشک به سمت ناو هواپیمابر ما شلیک کرد.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/18357" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ در مورد ایران:
احتمالاً امشب دوباره به شدت به آن‌ها ضربه خواهم زد.
به آن‌ها یک اخطار کوچک می‌دهم.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/18356" target="_blank">📅 16:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18355">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیروزی های ارتش طفرنمون روس ادامه دارد…
اوکراین می‌گوید امروز یک جنگنده سوخو-۳۵ روسی را در جبهه شرقی سرنگون کرد.</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/18355" target="_blank">📅 16:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7979bdf1.mp4?token=u9VDc4jzB6N0js-IcecYYS4ai9WzbyTgmtgBsMNpbA6eMr9sb4QI4TD8IeveiqB-hEHHqTtpSGiqNmmaDgjI6CLiWGqrsamRi2-f_0AWbNL8bBQWDOb7CruzPeBdwEt97UVOP5PXQd3vNLSSv-7uxmkrHrc--58phO1LxFR56FB9W7xoETOItc8mn-9k7ai_DvZNj99C0jJIKE9DvA8qBqAnYxgGpVP0pbOoTFotIjHtn0PTeXNf40oNo5TbIrn1ozGrzDO4s0bkwF-5SwbXMZM9AalNNkVHTTBKhnA6i2rPlkGE25znLSi3a8gm1Jex_FZoTtJIFPbpaHvC06ANhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7979bdf1.mp4?token=u9VDc4jzB6N0js-IcecYYS4ai9WzbyTgmtgBsMNpbA6eMr9sb4QI4TD8IeveiqB-hEHHqTtpSGiqNmmaDgjI6CLiWGqrsamRi2-f_0AWbNL8bBQWDOb7CruzPeBdwEt97UVOP5PXQd3vNLSSv-7uxmkrHrc--58phO1LxFR56FB9W7xoETOItc8mn-9k7ai_DvZNj99C0jJIKE9DvA8qBqAnYxgGpVP0pbOoTFotIjHtn0PTeXNf40oNo5TbIrn1ozGrzDO4s0bkwF-5SwbXMZM9AalNNkVHTTBKhnA6i2rPlkGE25znLSi3a8gm1Jex_FZoTtJIFPbpaHvC06ANhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بح بح!  موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/18354" target="_blank">📅 14:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">باور کنید برخی هستند که  مطمئناً این چرندیات امثال شریعتمداری و رسایی را ترجمه می کنند برای ترامپ می فرستند.  شریعتمداری و رسایی اگر هدفشان ترور ترامپ است چرا خودشان اقدام نمی کنند؟!</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/18353" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCsRGzYZFdcKijaJ25_RtEv2OUALBWNonJo448NMQHA76OLeUu69nLKWtLhH8qD2yydvg-0FsiGug8tcCOrQqODabfJQfhiiENHa4lIcFTnvVBlSkb4wlu5YcXbt1PEvRH8-ysXzT1F_gUXtP_ZcvtCEXgiiLeD3Gy7jhdV3swqL9jq2TzufE6UA9cx2zjrJ6IvzjXnNovIC8Us3PNzZWNV2xncwTdKBcAJ8eSnVkvq7nKKe45pW3STaWbtK8CgNY--aaH7EJ-Wik97XGtRtuLkhRZ-xovsOqKZ1WeP-OnLjMlJhZED-On8lmilMRrL3PtrpmTWHpbGy1U0dG-z9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/18352" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18351">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تا این لحظه،
هیچ منبع معتبری
(از جمله رویترز) خبری درباره
هدف قرار گرفتن نفتکش آمریکایی شورون (Chevron) در دریای سیاه
منتشر نکرده است.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18351" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCo_0gH3OREM3UI-b4m42x0vDPaonl-diiGOvLBlBU7qlbbxtrUr8B0o-rTWuDneZgrW7i4NXFX6MgfpUArKmXR0kBd0Y6nFrSk-2ORfM9_ojRb0LzULfr46gJfcIb9kOwVkuaKW2mIa7LaO5_jIWFunidtDD7Xuv8laMGextHJu2UAN7FNsCIIMHmGnAsUwn6OpUia00MSFEiGPWO3SiiAt4oto6awJ1BibiHwZNu-TZYQyK-ZQCZ2ORjtUmpKOHPEt85JFoBwNABeK8mUCf5xPdgsEi1teUIkMRmAuZlPxHkjcoH-fPEaAIHFbFRxrfbbsdzKUp_1QzjGU8h9RDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت برق کویت خبر داد که درپی برخورد ترکش‌های موشک‌های شلیک‌شده به‌سوی این کشور، تعدادی از خطوط انتقال برق آسیب دیده و از مدار خارج شده‌اند</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/18350" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18349">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارت برق کویت خبر داد که درپی برخورد ترکش‌های موشک‌های شلیک‌شده به‌سوی این کشور، تعدادی از خطوط انتقال برق آسیب دیده و از مدار خارج شده‌اند</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18349" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18348">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74a7b8d5.mp4?token=IGu7CqZVIPVgz4BCck48yOx-HPFnQ_LFrq9eCCdf-Xf_UEKOH8a5IFNN1JIOv9JwAVr5VMnQzCRPdKmfqVnmIZxnfzwb9MffUHFeJtDmCyxcrc9BL2MeVDB4swQ8rn4VGIbsiGqYE8IK3IbKga4LahL00vbjhtb3mrT1PFBR2E-zsaf0MYIxgtRV70vgaupTlrHvkFUmbi5BhqV8APg84DMQmjPvKgEuDIL5nWIfP89npF1_7FNsCQBY8lA3niMbVKlJh3DV1KhBX9wsnVe5qYOaoZkTBOkKYOZ-jNDOtYnuaAmPeiDDTld0ry4GJ2ocvhl0JcBr9owJ53IDfBw8Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74a7b8d5.mp4?token=IGu7CqZVIPVgz4BCck48yOx-HPFnQ_LFrq9eCCdf-Xf_UEKOH8a5IFNN1JIOv9JwAVr5VMnQzCRPdKmfqVnmIZxnfzwb9MffUHFeJtDmCyxcrc9BL2MeVDB4swQ8rn4VGIbsiGqYE8IK3IbKga4LahL00vbjhtb3mrT1PFBR2E-zsaf0MYIxgtRV70vgaupTlrHvkFUmbi5BhqV8APg84DMQmjPvKgEuDIL5nWIfP89npF1_7FNsCQBY8lA3niMbVKlJh3DV1KhBX9wsnVe5qYOaoZkTBOkKYOZ-jNDOtYnuaAmPeiDDTld0ry4GJ2ocvhl0JcBr9owJ53IDfBw8Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18348" target="_blank">📅 14:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عراقچی را در ایران فحش می دادند در عراق بشدت بزرگ داشتند!
فکر کنم عراقی ها چون دیده اند فامیلش عراقچی است فکر کرده اند ولی خب.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/18347" target="_blank">📅 13:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:
«ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18346" target="_blank">📅 13:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18345">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان درباره تن ماهی پرسیده بودند؛
به نظرم زود است و می توانید از مرداد هر هفته پله ای بخرید.
تصور می کنم هنوز ذخایر نفتی آمریکا پر نشده و انبارهای مهماتشان هم.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18345" target="_blank">📅 13:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18344">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فوری | اردوغان: موضع قاطع ترامپ در مورد تلاش‌ها برای دستیابی به توافق با ایران قابل تحسین است.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18344" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18343">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ :   تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18343" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18342">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMM4jv8BaYPFwqazlb9-B7-Tu0S0EYu6Sg6pbYyDzDJPsfMnW7cXdvDdE0aekpKNqnuh5BAioJx1AahO43StSz_dvsXkOrTO2A-7k9ZxSwDzouuYfVitXt_XZJO1A7fcayCRCM2OsyEBfxhO9Pi1wWFB5pTZ4Od_WjGXCAn5Owg9OqOAQzZT179tTuDsi2SI8C2j36hh4cZoNBVbuyhIe6OYxhyl_jkdQ5rzn-b9DfqXSbqBkPUbsUxUwltOu11aAXv_gD_z8VSaJXzNdNfZFgQnlTzJaPVN4aptiFby3EkoDgJNi9FgC1rKCpw0QTUSis4aFRP5AVC82QpETxfV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولانی به آنکارا، ترکیه، سفر کرد تا در اجلاس 36ام ناتو شرکت کند.  قرار است او با ترامپ دیدار کند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18342" target="_blank">📅 12:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18341">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/18341" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coA3ZLg-jsIGVI7Hft1851PRN1gjNKFnUwipm2xb1UPcf-imKTp16HiJmhHaelQCOWxB3RBIRKkHty1Be2BK9jOGJXdIitTGRQJEyBYAYARR9GDE39a_4PUljaZTOONdoz5Q9_H_GVXWpsEQSyy_UQSofHmdj0w8pspecTl3RC84_tI3XwZtMPPQO_fm1_SmXfFVvS7yxlCIku4Ur64qK7IlfsKDg5RZXgW6bMlslhDKugvNc8eMyUfji172gai13vxcgHubf8EeJd6A_c20NRka3ngva3r-lCD1u4-R4X3FOabyhylxnEFPhRYfgI24rLVnN6oTcz6_Rl4ADB2gOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پهپاد آمریکایی توسط پدافند ایران سرنگون شد.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/18340" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وقتی در اجلاس ناتو در ترکیه این چنین صحبت می‌کند یعنی یا به من کمک میکنید یا گور پدر همه تان !</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/18339" target="_blank">📅 12:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18338">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:   با اسپانیا حتی صحبت نکنید. آنها کاملاً ناامیدکننده هستند.  آنها آدم‌های بدی هستند.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18338" target="_blank">📅 12:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18337">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید  همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18337" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18336">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این خبر از دید من مهم است و می‌تواند منجر به ورود باند جولانی به لبنان بشود</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/18336" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18335">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:  آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.  شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18335" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18334">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvxX-90jNxAb6QpuyfRg6kA7Ls7KAvlG20Xt4ZxMs6bsAuSdgt7aWhm0Bo5V_EnTEIHPKq-1wAmRDYWlWYVflm_xwoisHjCydsWpCXcfJjJ8QK5lDq7oNXCeIfi-I1VPuxHBDplJxsrw9d45pkAstVxQQKQIU464KWogdErb6qkQ78WsLK4iWKQ8rBiQsuZ67FFYYiFj-WBsfVFk25kuaYdOYQ7TaOMDmvpqh7ATZbgWp_Lls1rZKBdJKTlisklqxZhsDp-74eCvBjt1-lF1MS09kbFPFAZcu1VcZP1e9MOiTYhYvGotJb7YiCL6_YHa6sNdcnTRgvC3i8G-Sn21ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در سطح بسیار بالا قرار دارد و ریسک گریزی آشکاری در بازارهای مالی جریان دارد.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18334" target="_blank">📅 12:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18333">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ درباره اردوغان:
به نظر من، اردوغان هم از ایران خوشش نمی‌آید.
اردوغان شخصاً فردی عاقل است، و به نظر می‌رسد که ایرانی‌ها رفتارهای غیرمنطقی از خود نشان می‌دهند.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/18333" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18332">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:  آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.  شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18332" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18331">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:
آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.
شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟ چون آنها نمی‌توانند قدرت را به دست بگیرند، زیرا کشته شده‌اند.
آنها آنها را کشتند. هیچ‌کس نمی‌تواند قدرت را به دست بگیرد، زیرا آنها سلاحی ندارند، در حالی که طرف مقابل مسلسل دارد. و سپس آنها به کشتار ادامه می‌دهند. رسانه‌ها این موضوع را پوشش نمی‌دهند.
من به مذاکره‌کنندگان عالی‌رتبه‌مان اجازه خواهم داد که در صورت تمایل به صحبت ادامه دهند، اما من این موضوع را بعید می‌دانم.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18331" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18330">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ :
تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/18330" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18329">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مواضع جدید ترامپ درباره ایران:  «آنها یک مشت آشغال هستند. من اصلاً از آنها خوشم نمی‌آید. ما وقت زیادی را با آنها تلف کرده‌ایم. آنها بی‌کفایت هستند. ما فقط باید کار خودمان را بکنیم. آنها می‌خواهند رهبر ایالات متحده - من - را از بین ببرند. من سال‌هاست که نفر…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/18329" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18328">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مواضع جدید ترامپ درباره ایران:
«آنها یک مشت آشغال هستند. من اصلاً از آنها خوشم نمی‌آید. ما وقت زیادی را با آنها تلف کرده‌ایم. آنها بی‌کفایت هستند. ما فقط باید کار خودمان را بکنیم. آنها می‌خواهند رهبر ایالات متحده - من - را از بین ببرند. من سال‌هاست که نفر اول فهرست آنها هستم. ما باید سرطان را زود از بین ببریم. من اینطور احساس می‌کنم.»</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18328" target="_blank">📅 11:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18327">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">️خبرنگار:واکنش شما به حملات اخیر آمریکا به ایران چیست؟
مارک روت، رییس ناتو:به نظر من، این اقدام کاملا ضروری بود. ایران، آتش‌بس را نقض می‌کند</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18327" target="_blank">📅 11:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18326">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صدای انفجارات در بوشهر</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18326" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18325">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سپاه پاسداران در پاسخ به حمله آمریکا، یک حمله هماهنگ موشکی و پهپادی به ۸۵ هدف نظامی ایالات متحده از جمله ناوگان پنجم، پایگاه هوایی علی الصالح در کویت و بندر سلمان انجام داد.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18325" target="_blank">📅 10:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18324">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18324" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18323">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRbf_OvDBC115rgbDje1IjhUAfFxqsyklGW_T9QLrDnt_S_wgSPOyIM8k5j6Ou52z_d04TkYLWIcSJWcmOp0uh6naAckxiQysQk2wRIASVTDRtsomcIIy81ZM6guA2UygzEDLFIX1E-YuTwQLKn1CTRpXyo7kogvOdf_m1q3lKCC7mx7lBGXpgQeXMYdFp2LKccJ8u8e4c5T4xCqXc4fca8ietbb_wpOTSvJLt1kk8SvGJNK70dw5HjjU6QiyEZP6UwueaEQJ4dC6C_fvWy_KdCEOJDmsSbUIL5tflbczgHETWFDVuQzDzLqQsI89O8nDJfEQd7PB852A9lEw-NiQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18323" target="_blank">📅 10:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18322">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">CNN:
وزیر دفاع ایالات متحده پیتر هگستت‌ در روز سه شنبه سفر اول خود را به اسرائیل انجام خواهدداد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18322" target="_blank">📅 02:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18321">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK7zu0NcRwL3RFvRKmoReGpgAK5hb1NR2CYVjmpM3_v4nYqIqtH9XcK4PG6Z1_j7FC-yzJ6rnmSIkG6JES5W8eY1L4pNNAGTN2IhNyx99noiRdBrwJANky6NA4s5vgI2wfjNuscauMRChKCv6QW5lWefmr-ufD14qFLD43HwOrh6QDi4NzyEW-wskP9s7o3yyDhPwkrFhQFskdT_j9PHmAYqZkIm4IoEruInLKr8QJG8pfe87Nh-WjnHTzt4tAsTiyEC4wtHk50Bg3C2YVjutym8-X-Rp_E_3N0WO8V_DjRGzNghUyPKB5Gz8SdoV7pTU7YeKWqybGrHxv_sCJsyBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!  ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18321" target="_blank">📅 01:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18320">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حملات ناوهای جنگی آمریکا در ایران، اهدافی مانند سامانه‌های پدافند هوایی، سیستم‌های نظارتی ساحلی، موشک‌های زمین به هوا، موشک‌های کروز ضدکشتی و محل‌های پرتاب پهپادها را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18320" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18319">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مقام آمریکایی به CNN :
حملات به ایران برای تنبیه‌ست!
نه مقابله‌به‌مثل؛ و این حملات فعلاً ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18319" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18318">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZWUvysY3GMDhSdkaH2n4rACd5K87QHDYl5hBXjnUNC5W5kKC3hYAkeFhdaHR09WSNllCO2r_J6lLYero0lCgMF9_NChWMknV12D30DyhiLvzfK0v6HC0sITbRFeZfL-RtRMwWLlz9TDKsp_TeBuFK5JP7kUkVqXLWbyLAgRauSMM0MqeQtLNvZQ04NUKVBCnaiHkf802biMWgVuP1WVd_kAi0iogyU_EjFpWa1HrNjXal9A9XkaTL8MryFJjMLe98Kr3RKJbA7HiCA1xQ9Yplu9NTNZb-SM3JzbCYLtfBegOP4ixRhDiRnSFQlxgSE499wuCCgAlJJQK1WR4y_H1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18318" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18317">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=vtnAmdawbNq7mjfK7FYRytTUwG3wRz3r_C7JT28o8ScnPFEs2N8pYkvSu2XS7Wb3fXEA2PzROnf9EPG966dC8YjzxukVzK9pBlOntIWI2Ia3SroDaPtBYfKceSMYropg_vVPZjZWwEkEVNzzR-BAzxAV0TG7AR9jbc-PLNas5mH1xrcS9oaOu2UbL2Iv2CW6xLQfRXqBbqNNtADZGwtNSifBjNIHkJlEr6yuk9f0nVjf52kSZbvhmfS8do6a6JUotx-T_nwhGjqJeiYktzZMhuRb5pgMqrMf9LlbwPwZ0p9T-BIs0JNyLN_Gw8-EXZ1z5jil5Lj6_N0AyGh8EN3YxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=vtnAmdawbNq7mjfK7FYRytTUwG3wRz3r_C7JT28o8ScnPFEs2N8pYkvSu2XS7Wb3fXEA2PzROnf9EPG966dC8YjzxukVzK9pBlOntIWI2Ia3SroDaPtBYfKceSMYropg_vVPZjZWwEkEVNzzR-BAzxAV0TG7AR9jbc-PLNas5mH1xrcS9oaOu2UbL2Iv2CW6xLQfRXqBbqNNtADZGwtNSifBjNIHkJlEr6yuk9f0nVjf52kSZbvhmfS8do6a6JUotx-T_nwhGjqJeiYktzZMhuRb5pgMqrMf9LlbwPwZ0p9T-BIs0JNyLN_Gw8-EXZ1z5jil5Lj6_N0AyGh8EN3YxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی انفجارات پیاپی در بندرعباس!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18317" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18316">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نفت را بای داریم پدرسگ ها</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18316" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18315">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18315" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18314">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18314" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18311">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!
ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18311" target="_blank">📅 01:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18310">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGHUQqzlvWYl00uKcJ9mxifnLePfjlDrCfIEkPP7PHoeVijXr6RuEFsfjTgQYQCMm0bMHWW3CYWRuuNN1Sf_KDG_5_dCQERPZXcfwTy1o9Kc7-zDBd99gpKsjNQOYdBRUUxyAioe0QA48UzgnnuP3yUUb5eNhW9fKiGFNMH1WBRfG2_wHquqkuLb3_MXp37K3DYu9qX0ogaulDrQYRPW4imJkrm4uVlF48k8sVc5dRnsjtUqX1ILu27uG9MQw3EI59E3KAH6f_N2UNthmwwiC4pNwW4N2Uprb7UYhmAK_pZSaXfSlzYmDDlNt97AsfbLBvtn4YLlOoiKNjHMMEJkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه دکل سگ جانی است خدا میداند</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18310" target="_blank">📅 01:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18309">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E77iu5-44pfFdwmfch__ILD_RfWJieeQsVgSQE0boFrffPpO8kQiWlcEJDPMbOnK0qQ9m4sF9y44JtdSjhc3x60PEULWmK6zK0Bc2BB67VygogHMCUGQf3edxJu3VR-W4P8xTgQO1T9BxBWWRF6Shz3Gsvu0UHre-foxWwhqaOGrjf9blAp38XoHMlcIrtdApFmGfpHXxni6ikn4yswzOm7WT3LogM_LG9FLGj1ZtcDqomuw-4hBptNx0VnibBSF6m_1_fu8n9E6RkJV1Q_ai4Zk06-Si-A8yl67ZO6KELFWQ5qc8RugXwJmpoROAKAzvV87KpqohN3hRHgTxBOXTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویری از انفجار در پایگاه دریایی سپاه</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18309" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18308">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">باز  هم اشتباه محاسباتی منتهی باز هم از طرف ما!  بارها دیده اند ترامپ اساساً اهل محاسبات نرمال و عرف پذیرفته شده و اجماع-محور نیست باز خریت او را تست می کنند.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/18308" target="_blank">📅 01:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18307">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">باز  هم اشتباه محاسباتی منتهی باز هم از طرف ما!
بارها دیده اند ترامپ اساساً اهل محاسبات نرمال و عرف پذیرفته شده و اجماع-محور نیست باز خریت او را تست می کنند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18307" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18306">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اژدهای بندر را بیاورید ببینیم منشا صدا کجاست</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18306" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18305">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گویا ارتش آمریکا اشتباهی یک هواپیمای پاکستان را زده و سقوط کرده است</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18305" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18304">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سنتکام می‌گوید ایالات متحده پس از حمله ایران به سه کشتی تجاری در تنگه هرمز، حملات گسترده‌ای را علیه ایران انجام داد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18304" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18303">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">منابع محلی گزارش دادند که آمریکا به یک دکل مخابراتی در محدوده سیریک حمله کرده است</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18303" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18302">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18302" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18301">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسراییل هم شرایط را مناسب دیده و شروع به پیشروی با زرهی در جنوب لبنان زیر پوشش آتش هوایی کرده</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18301" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18300">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18300" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18299">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.
فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.
سپاس</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18299" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18298">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آن 2 بند اول هم که از هنوز از تنبان توافق گشوده نشده صرفاً در برابر بازگشایی تنگه هرمز بوده.   به زبان ساده تر، یعنی ایران تنگه هرمز را بست که از کله زرد امتیاز بگیرد، اما او یک محاصره دریایی در پاسخ اجرا کرد. حالا ایران امتیازاتی را که می خواست نگرفته اما…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18298" target="_blank">📅 23:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18297">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دکتر محسن رضایی:   کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18297" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18296">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دکتر محسن رضایی:
کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18296" target="_blank">📅 23:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18295">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر خارجه ایران:   کشتی‌های تجاری که مسیرهای هماهنگ‌نشده‌ای با ایران دارند یا دستکاری ردیابی کشتی را انجام می‌دهند، با خطرات مواجه شده و تلاش‌های ایران برای تسهیل عبور ایمن از تنگه هرمز را مختل می‌کنند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18295" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18294">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یکی از این تعهدات  این است که کشتی هایی را که از مسیر عمان میگذرند میزنیم تا بفهمند مسیر جنوبی ناامن است و از سمت ما رد شوند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18294" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18293">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر خارجه ایران: ایران در حال انجام تعهدات خود بر اساس تفاهم‌نامه در مورد اقدامات لازم برای مدیریت تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18293" target="_blank">📅 22:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18292">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18292" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18291">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18291" target="_blank">📅 22:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18290">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ایالات متحده مجوز فروش نفت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18290" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18289">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRed Lion Corps(M)</strong></div>
<div class="tg-text">بازی فوتبال تیم مصر و آرژانتین، چیزی تو مایه های جنگ یوم کیپور برای مصری ها شد. کمی اولش داشت خوش می‌گذشت بهشان که زمین و زمان بهم ریخت</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18289" target="_blank">📅 21:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18288">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بح بح!
موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18288" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18287">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار سی‌ان‌ان:
«ترامپ در حال بررسی دادن اف-۳۵ به ترکیه است».
نتانیاهو
:
«این تعادل قدرت در خاورمیانه را نابود می‌کند. من این کار را نمی‌کردم».</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18287" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18286">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18286" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18285">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18285" target="_blank">📅 20:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18284">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=MJPlZyC31zqjcUDCSvblwqEpRh27xCvLps-q343cSx4rsav9goI8Mf9tojCWrWs7MIZErLMkOppMnw758ODmUqCUjzrwOw--UfWHqsqq5gxe2tjgv9hsznLZqTe3CDkyTF1IiIsIKRSjSv6JBn6EHodjWuinjwvmP4WSYl4ccaKmZ2Ucfd7yUFZz5wPKYFR0SdYxdKDHu-qM3aTRBCm15jaPOWnzjn2Esre-J-2h7s_VQhuMmDr0RPXrirFP8oh5wP21gBoSXXJLYNb6WCS9la6dTyObpexVKXEd_y7UVxwGFJv7Fc3t0R9KeZ2wFtPOCkJmsUbRjzQPP9w8q6sKQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=MJPlZyC31zqjcUDCSvblwqEpRh27xCvLps-q343cSx4rsav9goI8Mf9tojCWrWs7MIZErLMkOppMnw758ODmUqCUjzrwOw--UfWHqsqq5gxe2tjgv9hsznLZqTe3CDkyTF1IiIsIKRSjSv6JBn6EHodjWuinjwvmP4WSYl4ccaKmZ2Ucfd7yUFZz5wPKYFR0SdYxdKDHu-qM3aTRBCm15jaPOWnzjn2Esre-J-2h7s_VQhuMmDr0RPXrirFP8oh5wP21gBoSXXJLYNb6WCS9la6dTyObpexVKXEd_y7UVxwGFJv7Fc3t0R9KeZ2wFtPOCkJmsUbRjzQPP9w8q6sKQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک تروریست و یک شیفته تروریست در حال امردبازی</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18284" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دبیرکل ناتو در مورد ترامپ:  من از این مرد خوشم می‌آید.  به نظرم کاری که او برای ناتو انجام می‌دهد خبری عالی است زیرا، بله، یک تهدید روسی وجود دارد، اوکراین وجود دارد، بنابراین ما در هر صورت مجبور بودیم در اروپا گامی برداریم.  اما او چیزی بود که برای ایجاد…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18283" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">روته، نماینده ناتو در آنکارا:  ما روز سه‌شنبه در مجمع صنایع دفاعی، ده‌ها میلیارد دلار قرارداد جدید را اعلام خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/18282" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18281">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th0dKjwmjZYGZfX5yfgBzavShBKVba8aoVBL1Z8nF7n4nNpCBV8uJ93St8EwmRvYbFH4M8Gmrz_94tOlSKRCOWPvGN8mgcww0Gx8nW9F77qV5fle636TZ9H_cHl87OvBXcu1hoSyrycqI_qIn5ggeZJ2o5Yi56vEG3wSSsKXEas57hR6b67reeL0iVeNwOBVyzQDHUGX3eCXH9uuddxOYNt0aG9vYcD6rbSFglONooQXpc_LBYTPeQ3OwxnAx1yrUKBosq7vL1y021A-1HkPLV1e98KRFJ2E3C_SYZ61yODvX2YY6OyGD9GAKwhBK3naPIiY7tl3RYGaQMbTiPs24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18281" target="_blank">📅 18:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18280">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUGyQaxWY0AZiSYjvEoEfKYgRmaSxmAHK76nfgYtiVgrSOy8N-Xcn6F7dtGWGGpbHTJoG8uavPqFi89ffTGlmrufJ49p--nb8wmfFPRc0KSMrnkP5kPcLJiMqiulDC3olfILahRq0BJfXrrRb7xqk1FeTuq_tkrCEEKkDuFLGVTfEI-7Fv4CeizXQ-SBhRgBFEuLuJpPvpdH1HfcK13Ohrz9wJ92VLTtitfGhfnHnatXOLF-DAVebeV3uIyTpOxKfcBvDqEsotAKmpfaXyVkeHwTxzC-N-ofc7R89z36uw49MjD68i8g9J-0ls0bfbwd_xMBqsTrMTui_1vwKyUGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">90 درصد این دولت ها را زردپوست هایی تشکیل دادند که از دید چهره و ریختار هیچ شباهتی به این دلقک های اردوغان نداشته اند.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/18280" target="_blank">📅 18:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18279">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سیرک جدید اردوغان!  لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18279" target="_blank">📅 15:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18277">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujwVWUvrfWcxK50uVqxV4vO2TREZ4j7ZVDTNyf80TQUrvOd_a9CEshlJCBCL_TrRZG4C1lQ6CR5jgeOflYb4awtnVWaEGea3vwb8yRQlETpp8TJjEblKwmcXGEDPFdtmdzt8gZGP75z59m3VtGGFTePEI3Ndb3WB92IqLaiS9AgdlUxQANBPKyMe7XVWke71GkUmv5vYTwwRkjM9-gEpM-RxmaWWLBcYB-7Yso8LcMPdfoWNWCWLTZNyZPRC-IPVfqt4zD78ioaOYe42VRcQ_MEPbSA2qFPCfm8Pe7rYDoZ-18hvLkg4N-Zjx3ZVRDbv1JKBd2ciQtIgk5Rnb0uqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVatNYihG6lcM_nBQS1HMD7PQN268_-ZHR0hXEKqj7NtydX9OKX2bIPPcAOk-XqUQSO10zNj8ZoUJ5j3H5mdfYkEZ50c4MlI0cURH7nIINZ5PC8h8Ep0rQoJdIKVo0JSAKX6k3V_OF4C0Ppb0QtR-vBtQzZwWcPoD8nyPDLB5IPa8aiSlvsUGpsPqllJzuPtLiOCBv9FfduWWAdFBmHqdKRA-u0YbiYnoNT_TgTO2NpfhjqWphi-0GkTOT0n1YkQFHPwt5CjIp4_TakL312YSJxyW_hpMP8ou4ztpjTdK7r8HadfHiOrLPkwJQJNyWgdW_BqHz976alNqJezHYK9rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جدید اردوغان!
لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18277" target="_blank">📅 15:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18276">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18276" target="_blank">📅 14:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18275">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18275" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18274">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18274" target="_blank">📅 14:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18273">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR1Ch_q_v-1CdN3AVyLg63T8h04s5gHv27lJGFNw8HSiHp7CtqJWzgstDssORiFTzth-PNwwCHU0CHS82g9bsVRn7UL90BG9UzlW1TFrXdgE6F9ynJTKwDOIqIXj2_2fI9W8VACYMFKlTyAzDQQnlcGsXXnvSxVoUniWuhN8Pel3uwmkwiv0Rk3xtoablP83lBophSL_0toIM6yh5ncggiIRzsn_kP3OASgr6REM7iTbjpuZMjQ-czJsTXJhuBdP4Z-wQTURyWDc4PYjvbh4wmXB17b54hfDCzhE3nA5DPSyemW6E-67PjO21ssDftywDxG8NTSu9GK0-4CZJAKaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایه کشتارهای قومی بر اتحادهای ضدروسی
تنش‌های اخیر میان لهستان و اوکراین نشان می‌دهد که حتی نزدیک‌ترین متحدان نیز نمی‌توانند از سایه تاریخ بگریزند. در حالی که دو کشور از زمان آغاز تهاجم گسترده روسیه به اوکراین در سال ۲۰۲۲ همکاری‌های نظامی، امنیتی و سیاسی بی‌سابقه‌ای را تجربه کرده‌اند، اختلافات مربوط به حافظه تاریخی بار دیگر به سطح روابط دوجانبه بازگشته است. مصاحبه اخیر کیریلو بودانوف، رئیس اطلاعات نظامی اوکراین، با شبکه RBC-Ukraine نیز بازتاب همین واقعیت بود. بودانوف در واکنش به آنچه «اقدامات نابالغانه» لهستان خواند، تأکید کرد که کی‌یف نباید با واکنش‌های شتاب‌زده تنش را تشدید کند و امیدوار است پس از دوره‌ای از افزایش تنش، دو کشور به سمت کاهش تنش حرکت کنند.
زمینه این اظهارات به مجموعه‌ای از تحولات اخیر بازمی‌گردد. در آستانه یازدهم ژوئیه، سالگرد
کشتار ولین
، فضای سیاسی لهستان بار دیگر تحت تأثیر مطالبات مربوط به بازخوانی گذشته قرار گرفته است. هم‌زمان، اقدام اوکراین در نام‌گذاری یکی از یگان‌های نظامی خود به نام ارتش شورشی اوکراین (UPA)  واکنش‌های تندی را در ورشو برانگیخت. برای بخش بزرگی از جامعه لهستان، UPA  نه نماد استقلال‌خواهی، بلکه مسئول یکی از خونبارترین فجایع تاریخ معاصر این کشور است. در مقابل، بخش قابل توجهی از جامعه اوکراین این سازمان را نماد مبارزه برای استقلال در برابر سلطه شوروی می‌داند. همین تفاوت بنیادین در برداشت از تاریخ، بار دیگر شکافی عمیق میان دو متحد ایجاد کرده است.
ریشه این اختلاف به سال‌های جنگ جهانی دوم بازمی‌گردد. ارتش شورشی اوکراین (UPA) در سال ۱۹۴۲ به عنوان شاخه نظامی سازمان ملی‌گرایان اوکراین شکل گرفت. هدف اصلی این نیرو ایجاد یک دولت مستقل اوکراینی بود؛ دولتی که نه تحت سلطه آلمان نازی باشد و نه اتحاد جماهیر شوروی. اما در کنار مبارزه با این قدرت‌ها، UPA  وارد درگیری خونینی با جمعیت لهستانی ساکن مناطق ولین و گالیسیا نیز شد.
در سال‌های ۱۹۴۳ و ۱۹۴۴، نیروهای UPA مجموعه‌ای از حملات گسترده را علیه روستاهای لهستانی آغاز کردند. بسیاری از مورخان معتقدند هدف این عملیات‌ها حذف جمعیت لهستانی از مناطقی بود که ملی‌گرایان اوکراینی آن‌ها را بخشی از سرزمین آینده اوکراین می‌دانستند. اوج این خشونت‌ها در ۱۱ ژوئیه ۱۹۴۳، موسوم به «یکشنبه خونین»، رخ داد؛ روزی که ده‌ها روستای لهستانی به طور هم‌زمان هدف حمله قرار گرفتند. برآوردها نشان می‌دهد بین ۵۰ تا ۶۰ هزار لهستانی در منطقه ولین و در مجموع تا حدود ۱۰۰ هزار نفر در ولین و گالیسیا شرقی جان خود را از دست دادند. در مقابل، عملیات‌های تلافی‌جویانه نیروهای لهستانی نیز به کشته شدن چند هزار غیرنظامی اوکراینی انجامید، هرچند از نظر ابعاد و سازمان‌یافتگی، بیشتر پژوهشگران معتقدند خشونت علیه غیرنظامیان لهستانی بسیار گسترده‌تر بوده است.
همین گذشته، امروز نیز منشأ اختلاف است. پارلمان لهستان این کشتار را رسماً «نسل‌کشی» توصیف کرده و خواهان پذیرش کامل مسئولیت تاریخی از سوی اوکراین است. اما در اوکراین، اگرچه بسیاری از پژوهشگران وقوع جنایات گسترده علیه غیرنظامیان را می‌پذیرند، بخش مهمی از جامعه سیاسی همچنان UPA را نماد مقاومت ملی در برابر سلطه خارجی می‌داند و با اطلاق عنوان «نسل‌کشی» به این رویداد موافق نیست. این دو روایت متفاوت از گذشته، امکان دستیابی به یک حافظه تاریخی مشترک را بسیار دشوار کرده است.
با وجود این اختلافات، بعید است تنش‌های کنونی به فروپاشی همکاری راهبردی دو کشور منجر شود. لهستان همچنان یکی از مهم‌ترین مسیرهای انتقال کمک‌های نظامی غرب به اوکراین است و امنیت دو کشور به طور مستقیم با نتیجه جنگ روسیه و اوکراین گره خورده است. از سوی دیگر، ورشو نیز به خوبی می‌داند که تضعیف اوکراین، فشار امنیتی روسیه بر جناح شرقی ناتو را افزایش خواهد داد.
با این حال، تداوم این اختلافات می‌تواند پیامدهای ژئوپولیتیکی قابل توجهی داشته باشد. نخست، شکاف‌های تاریخی میان دو کشور می‌تواند انسجام سیاسی جبهه حامی اوکراین را تضعیف کند و روند تصمیم‌گیری در اتحادیه اروپا و ناتو را پیچیده‌تر سازد. دوم، روسیه همواره تلاش کرده است از اختلافات تاریخی میان کشورهای اروپای شرقی برای ایجاد بی‌اعتمادی و کاهش هماهنگی میان آن‌ها بهره‌برداری کند و چنین تنش‌هایی فرصت مناسبی برای عملیات اطلاعاتی و تبلیغاتی مسکو فراهم می‌آورد. در نهایت، اگر ورشو و کی‌یف نتوانند میان ضرورت‌های امنیتی امروز و اختلافات تاریخی دیروز تعادل برقرار کنند، یکی از مهم‌ترین شراکت‌های راهبردی اروپا ممکن است با چالش‌های فزاینده‌ای روبه‌رو شود؛ شراکتی که حفظ آن نه تنها برای دو کشور، بلکه برای معماری امنیتی کل قاره اروپا اهمیت اساسی دارد.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18273" target="_blank">📅 13:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18272">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/18272" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18271">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18271" target="_blank">📅 12:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18270">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHsKEEbUAV_RqsxTjxWl7-Lkh57PCVbhNtvr9vkcjf-Onen8HKpOp0BoTWuNQSJorP3cLJpCHZVr9zucGcMbfg8AhwX8dQBaJCvNtpCrKjky30iNKaVZ5zjg-6ASZ55OLpR5a49T6VrQEpkdhDSFbRQfKeVRztSs1AO2Fd4emfW0Ief42LT67i_6aLxTGtUh7n43wC2pt4U9s-vTiTTrlnZGFK7HM1YgFoKeEXCyKGUo3Kfq1VU3KoC73FLbVxvryok52ZdxIuQtFy-SLmTbv6EUaRLrR4Lzc0rYKAvFILJLFHKVpbEI_ez7puRtrkkBGcpNjeSg3xlAk6k6IdoGKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟
هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز دارد و میلیون‌ها درخواست روزانه کاربران، فشار بی‌سابقه‌ای بر مراکز داده وارد می‌کند. نتیجه این روند، رشد سریع مراکز داده و افزایش چشمگیر مصرف برق آن‌ها در سراسر جهان است.
این تحول باعث شده است که انرژی از یک عامل جانبی به یکی از مهم‌ترین چالش‌های توسعه هوش مصنوعی تبدیل شود. در بسیاری از کشورها، شبکه‌های برق برای تأمین نیاز مراکز داده جدید با محدودیت مواجه هستند و شرکت‌های بزرگ فناوری سرمایه‌گذاری‌های گسترده‌ای در نیروگاه‌های هسته‌ای، انرژی‌های تجدیدپذیر، سامانه‌های خنک‌سازی پیشرفته و طراحی پردازنده‌های کم‌مصرف انجام داده‌اند. امروزه دیگر تنها پرسش این نیست که چگونه پردازنده‌های سریع‌تر ساخته شوند، بلکه این است که چگونه می‌توان انرژی لازم برای به‌کارگیری آن‌ها را فراهم کرد.
در چنین شرایطی، توان محاسباتی به یکی از مهم‌ترین منابع راهبردی جهان تبدیل شده است؛ منبعی که می‌تواند بر رشد اقتصادی، پیشرفت علمی، توان نظامی و رقابت میان قدرت‌های بزرگ تأثیر تعیین‌کننده‌ای داشته باشد. از این منظر، رقابت آینده تنها بر سر منابع انرژی نخواهد بود، بلکه بر سر تولید توان پردازشی نیز خواهد بود.
همین مسئله موجب شده است که پژوهشگران به دنبال الگوهای کاملاً جدیدی برای رایانش باشند؛ الگوهایی که بتوانند با مصرف انرژی بسیار کمتر، توان پردازشی بالایی ارائه دهند. یکی از جذاب‌ترین این مسیرها، رایانش زیستی یا Biological Computing است.
مغز انسان نمونه‌ای شگفت‌انگیز از یک سامانه پردازشی بسیار کارآمد محسوب می‌شود. این اندام تنها با مصرف حدود ۲۰ وات انرژی، وظایفی بسیار پیچیده مانند یادگیری، تشخیص الگو، تصمیم‌گیری و پردازش هم‌زمان حجم عظیمی از اطلاعات را انجام می‌دهد. در مقابل، آموزش یک مدل پیشرفته هوش مصنوعی ممکن است به هزاران پردازنده گرافیکی نیاز داشته باشد که هفته‌ها یا حتی ماه‌ها به‌صورت مداوم کار می‌کنند و انرژی بسیار زیادی مصرف می‌کنند.
همین تفاوت چشمگیر باعث شده است که برخی مراکز تحقیقاتی، امکان استفاده از نورون‌های زنده، بافت‌های عصبی و اندام‌واره‌های مغزی را برای انجام برخی وظایف محاسباتی بررسی کنند. هدف این تحقیقات، ساخت سامانه‌هایی است که بتوانند از ویژگی‌هایی مانند پردازش موازی، یادگیری تطبیقی و بهره‌وری فوق‌العاده انرژی در سامانه‌های زیستی بهره ببرند.
البته این فناوری هنوز در مراحل ابتدایی قرار دارد و فاصله زیادی تا کاربرد عملی و جایگزینی رایانه‌های مبتنی بر سیلیکون دارد. افزون بر این، مسیرهای دیگری مانند رایانش فوتونی، تراشه‌های نورومورفیک، شتاب‌دهنده‌های اختصاصی هوش مصنوعی و رایانش کوانتومی نیز با سرعت در حال توسعه هستند و هر یک می‌توانند بخشی از نیازهای آینده را برطرف کنند.
با این حال، یک واقعیت بیش از پیش آشکار می‌شود: در عصر هوش مصنوعی، توان محاسباتی در حال تبدیل شدن به یکی از ارزشمندترین منابع راهبردی جهان است؛ همان‌گونه که نفت در قرن بیستم نقشی تعیین‌کننده در اقتصاد و سیاست جهانی داشت، ظرفیت پردازش اطلاعات نیز می‌تواند به یکی از عوامل اصلی قدرت در قرن بیست‌ویکم تبدیل شود.
اگر روند رشد هوش مصنوعی با همین شتاب ادامه یابد و محدودیت‌های انرژی به یکی از موانع اصلی توسعه تبدیل شود، احتمال دارد پژوهش درباره معماری‌های نوین، از جمله رایانش زیستی، از یک حوزه صرفاً دانشگاهی به یکی از مهم‌ترین عرصه‌های رقابت فناوری تبدیل شود. هنوز مشخص نیست که آینده رایانش بر پایه سیلیکون، فوتون، سامانه‌های کوانتومی، نورون‌های زنده یا ترکیبی از آن‌ها خواهد بود؛ اما آنچه روشن به نظر می‌رسد، این است که رقابت برای دستیابی به توان پردازشی بیشتر با مصرف انرژی کمتر، یکی از مهم‌ترین رقابت‌های علمی و فناورانه دهه‌های آینده خواهد بود.</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/18270" target="_blank">📅 12:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18269">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdfuO8lnjISodfOCL9VRPf6P9meOyrdyCzPj-2JTAbb8PFyxgA7kZuPHdOlIU1Y_XFcijpTseZtV3cZngU_b6FyVECcpCWO7-mXJsWpKOXnMRkWQvnlGJ5iB_GzmhGdHkZZDF2ipB9ccMbPgsvV-OkEYuGloieDFgwJznWGHrqgZCUo88y7p5oaw3nCBR3Bd0jVMt4XyVdOCM0lhzvB8w2OPnmNdMpV8hSOsAd7A2C7AIf9cfG7ey-dYT4zVcGTwlMi-UxKAQzj4yuQz--bz7CbUmC3983WGNChaVqAm2qQDcPSVa9FVUKTgjlnjsoJFoyGZKw0OGdhEvwi7XPlFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای پرشمار در دمشق نزدیک محل اقامت شیفته صبیه رفیق بهزاد.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/18269" target="_blank">📅 12:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18268">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0QYNSKkK93T3DZ4yCHs1GqgTg2QvlzEkaqNi5NEVqaeOSbOAE9lx6bbDxS29WaRw0XmeAqBlI0uZpVrX9bPQv0NQ8ZFWoLwrnT40MNMGVoZpUw1ca4cN4o4u2BDX_WUypxdOJVp4A-KQDrOxR3d55A42iQAzUA4lVKEWFYrXKe8uPioyiUxRY3OE_yuk9A6KoyIlB_1mlWc9fXCQw2wmUhDHfB8oiTwGAiHvLe5_vF9-IU7gSU0BxC_HRjsCQBfGyMjUalbpaO2qnGS6NLV7jfJ8wab0Pxw8qsWaOV35LFaYGX44vnvpmWXh42s3YAvxVVU7ysfc54CYGvqSiGvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهید لاریجانی اصرار داشت با مال دیگران داماد نشوید ولی خب.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/18268" target="_blank">📅 11:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18267">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">راه‌حل شاید ملانیا باشد!   تهدیدهای تکراری ترامپ در مورد تخریب ساختارهای اقتصادی و زیربنایی ایران در صورت شکست مذاکرات، تنها کارکردش این است که جمعیت اصطلاحاً خاموش کشور را به حمایت از جمهوری‌اسلامی و بیزاری و نگرانی از آمریکا و اپوزیسیون وابسته به آن، ترغیب…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/18267" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
