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
<img src="https://cdn4.telesco.pe/file/qZ56AOlXhUvrOLPS3BEEowQ4vTD8Z93rzct9qH55HgSHL8Zamo3NOOgRdznCbLGkKxHILm85_KD7w2EfCLG-ctjAf4tFEFKZRHKkcNWtkqrx2se6nTbnZzvyQ99YQ-O_9eWYhaHJj0_KKkNYgrHhiqYTM2txEazgdqGX6OsGsX6eZX-OfuOh6qYFHz-TROmu1V1FN4NbP-QT9Pu_TXCXSvyAn6VI2ZWfrvpMOEa1guwEeCGyXoSATZLXsYnsKgizsNiy2YhRsn_dSRI64LGewkva3TvoZirNS7Wyc92iquzm1iLfd_37ZNlIkHV6E-vkMFixfFxcxWRcwVrORpkjQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 03:15:42</div>
<hr>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkyWtRLOCY65LnbQzjFFDhXGQpJ_hSPrZJUWFli0w7YfJayvAtpCTwr8SJE9kik-RsoxBJLIhv4yC3Q5jHnvr0FzUYFXyc1FRx5jUYfUqD1htR0IbE52RoFXP1hgrVevHgAhBNUNDcfoTWVr94MrE0Y20wZr3g4yE8Wb6MwXa0AMpuwS_smCx8fuCKhfPo0ftNAV-fsgQ-7AbjfJQvKNOvwWGRX2wj1sa0aTdIpKv4fGalnxZ_zh6jjqMsZqAvpshbQiskCHgAl6XnHphozSFGh2DZOJBONNhZka8SsEe4jbuHR4FLLOml66H7CUb1kjiGr2NHmz28es0D09U7ukdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=vwKHOsMvVY-naIey9ttnobViQfZ07lM1G24_42GRkeUKm-mLSqqlWYEZhCpvvyUCbgsDhBeR7iNZqaFg4g02wKAQvDImdBkAJNGu7twoOwXS8TmlU83nGxyQOe4VFhIKXSp460pNTqU362FWKyE0qMVJrS8HvG-jgCl3e4JGvV7NdgDsgj0e2XF5OeJP71qTnGavaMw_-SkdzD8Qn_RJzvmZO7HI6BeUx1yBVTWyP9le-PI191GQWNzN3kQx0t-PUcXE2fq27mJhAIRW43TTK5U93Tx-k__Rj1SmBQXi_EK6YLNPhnH2a2CIohpf99V1J3jr67h0kN9zINNZDiynmomMdstUMxaxbD-3nyYDHMNJDh2i_BulPI1sgG8DZu5cSyHaHXojFEpJNHamwrm8ThKNxWG8-ASRRrlJKskYBNmo02zn6ILxLpFXLQNGycgXRcgLRXBaf2WBgDRkYhCNFyB5BM5Adr1KANHK-pTUQsmyrcx9GCYZ5s02qB7F6XxCO_2KVpdhwZ9X6UtWk8ENlTymy6uZPwsLqgMorDYEIWbYwLok1onYomY-7CXf998bpNZV_WbX2szqi3B0Sg41M5qfPXbfEE2a8MDGcOlXKku8dCUPEfEryKdoepPq3MR9VkDUBH0L6FqsewMIJrF-y87-z_xWRY9VAEyr_k8vPCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=vwKHOsMvVY-naIey9ttnobViQfZ07lM1G24_42GRkeUKm-mLSqqlWYEZhCpvvyUCbgsDhBeR7iNZqaFg4g02wKAQvDImdBkAJNGu7twoOwXS8TmlU83nGxyQOe4VFhIKXSp460pNTqU362FWKyE0qMVJrS8HvG-jgCl3e4JGvV7NdgDsgj0e2XF5OeJP71qTnGavaMw_-SkdzD8Qn_RJzvmZO7HI6BeUx1yBVTWyP9le-PI191GQWNzN3kQx0t-PUcXE2fq27mJhAIRW43TTK5U93Tx-k__Rj1SmBQXi_EK6YLNPhnH2a2CIohpf99V1J3jr67h0kN9zINNZDiynmomMdstUMxaxbD-3nyYDHMNJDh2i_BulPI1sgG8DZu5cSyHaHXojFEpJNHamwrm8ThKNxWG8-ASRRrlJKskYBNmo02zn6ILxLpFXLQNGycgXRcgLRXBaf2WBgDRkYhCNFyB5BM5Adr1KANHK-pTUQsmyrcx9GCYZ5s02qB7F6XxCO_2KVpdhwZ9X6UtWk8ENlTymy6uZPwsLqgMorDYEIWbYwLok1onYomY-7CXf998bpNZV_WbX2szqi3B0Sg41M5qfPXbfEE2a8MDGcOlXKku8dCUPEfEryKdoepPq3MR9VkDUBH0L6FqsewMIJrF-y87-z_xWRY9VAEyr_k8vPCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCuEmpr3xJps0BI_5WVV0aPrOGnF2iM5X3vZIef-H4OxXquXQoZHk4PgjInmactwtKEOKzoYVoVSDxSymLEBHSCS6PHNyRm4Deoc_OI-yJ52ywQKnGuuNwykxWCEwDq0SM1D7pJ9pDGdEst1dEQuBEhi9oapp_Pd37ViRtv8CaUXhmdO9uH-CH-2XKYjo2eNB4T6vl_lrJo_dEImaaV9z12jSkBYv9LEZPye3rytFm4Xmji-5kOUvYPlxnCcxUbhCXadAA8sJTnygac63gU8m0fwokrpuuEROAVPC2-6827pE1FdlheVUF3AVcqG4X73Eqi-Vh8hDCOIqiLnWR0SgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=buTYCjKvH5q8ubsoFkyczlXNKGqZWPoOEY63HQnVj4okQ0OpIzAglVAlEL2PZctoPvymVNDeDrBVVEonkkRYjEtlS_qy9WA2pvSq3DxGYsEil0cPaFEouzDs9KpV06GJp_8vnnrF120-fV0feq-YFefwJBXJgA9dqz1LZXLcXWLWB4JR_pGyg_lZk9_idVB_qlqTcjzv00aE8mEjpRxzgSlRBzQq_SXqFs4GpjjN6bJnPSIVlTUsev9RE2Ppq82KG6xJaX-Kzy1VjDMRXItLjCGv7XeQajVlcEbSoFJY0HB8YNMRYbPmbyIVLb28pwOuFbasKMIrWzWV-lXeoEV_WzKBR1iexkIeZENmt1cfbc4rqfHpPl4VbIVEyhfmZh9MP0vFvpA1HKCVzJlJed7BmV6idt6qWOW10Rgiq7HITw_IibpVbNN9RuTshx9MmSJ1ZnLLXJJ8Yq_8UC6UFjO-6J-Vr3w6Kb90QRH2Alvv5bxiuqCZ-SV2jHbvrUQ0XocNbvjRZFabf7pnkpqVQB2ZgzMEjV17HTuwotPh6jDup87Caa9beq1-lulV330IzJkYM8CaIQrZQ9DP4hCW_VArJ1PcD1z-ugit42z3oSrYKrhkfDd__YeD1nvqPOazPjdJQqLS8vG0Gs-FFDpGgFfo8_XgytxPZGYxE0YiEG6SFvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=buTYCjKvH5q8ubsoFkyczlXNKGqZWPoOEY63HQnVj4okQ0OpIzAglVAlEL2PZctoPvymVNDeDrBVVEonkkRYjEtlS_qy9WA2pvSq3DxGYsEil0cPaFEouzDs9KpV06GJp_8vnnrF120-fV0feq-YFefwJBXJgA9dqz1LZXLcXWLWB4JR_pGyg_lZk9_idVB_qlqTcjzv00aE8mEjpRxzgSlRBzQq_SXqFs4GpjjN6bJnPSIVlTUsev9RE2Ppq82KG6xJaX-Kzy1VjDMRXItLjCGv7XeQajVlcEbSoFJY0HB8YNMRYbPmbyIVLb28pwOuFbasKMIrWzWV-lXeoEV_WzKBR1iexkIeZENmt1cfbc4rqfHpPl4VbIVEyhfmZh9MP0vFvpA1HKCVzJlJed7BmV6idt6qWOW10Rgiq7HITw_IibpVbNN9RuTshx9MmSJ1ZnLLXJJ8Yq_8UC6UFjO-6J-Vr3w6Kb90QRH2Alvv5bxiuqCZ-SV2jHbvrUQ0XocNbvjRZFabf7pnkpqVQB2ZgzMEjV17HTuwotPh6jDup87Caa9beq1-lulV330IzJkYM8CaIQrZQ9DP4hCW_VArJ1PcD1z-ugit42z3oSrYKrhkfDd__YeD1nvqPOazPjdJQqLS8vG0Gs-FFDpGgFfo8_XgytxPZGYxE0YiEG6SFvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCt7WIrLk9WsA3xTCbmCtVYMf4at1GEaIJWUrO6AW9EehlpTuUZ_OS-ZgIvNLH7pcDiCE5noJ6AxaXaPhMGulo7Rx21QXZfJBTS89omPt0JbTzw6IAB2REBdntuvlvL6p2gzZh8MZfVidoBp59YM2ivec11yKBp30L_Z07kgfuMseKomYfzPnJzMbBKp8Yjg8PEG9KwvZFiq6BkUcOX_PNrEUXTTJT6N_heB89fe0NrrASVHG8e7DifOZqgKdEIxmi5DMJCG3s6TqaADRjFAhfeNBebE4t3CB7xf8ZOnUuP6HQkV70fGMc9EvPmHFSZcs-S-Yt3VIiE1VC8D0vn2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2sHqPSbj5b9BCU1zsEcrqxrAKtloocIis0uVnUTlFXj6Sp27iF9qp6isfUZZqlQnEVlPVYWjPzLBPFIvMhEevb8j-n1XReyXtEdWGSBCQfs-_URV_0eOMYMOh9uycmnVXwGb5jFBAC1B2vf64gM71jELP_YLKzIpzrSKSyRC80U2wezd_1JjcqtuDG_34gZAUEJPWOXrrAY1Aebof_30oMmE5DDIkpq7TMyMOFNpxNNUb4MjgWGfvMuV0DETtzJBqnzrHpL9kMabC-DHwPRRxJkTVRJ329RwYqr9yZRd5GMOqPsQDaWdaKf5vGewXHQqx569siLMipIYyh0ELj9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8DN9iWdtXBdbE_bG2eHrpNOOhPojTyFnuQsG6JnjoUvhu_eljsqsuN-T2wy3--a9YTYTJ4gKgfpHNsBkWmUfuT7wHQek4Yhv3LYvRO9DhWE0AUVOCjONUovjCPhAYitEZo14N3ob_aP8Ti4GKiqraVFw6oTzDbwgViZugcRHRfF14wT-JVzN9H_t2167O0UvuDQRMdq_YmiV49A7xb13kgUiXVsNiw7TLFYSgDZuIuM_AMWrnhe2IiUwmQoB4gHrxXTUnvB6lWNwbIjc9mo4LORCgxBX241CY4c40P40U_s-JTiqAVqP5NmyCb_-DAqzMr48RjDpMUH05F9854-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nun28zV9hk6rViVhsf8x2VJJl4kf14X9D5NOGbh8zLyDif1ASk---rlltJ07jkY04o0fHtvIY0bl7-MGKP_hlZw_MbdfbEhHS4wayztzVM7nqYXS1S1Qs91Vo3R7ZC6LqKjw-sC49gVeZNiIWp1dmSDkpXlXbrkpcdQf-Rzx-PzuA8bm_fJmxO0ulMqDvMaDcgMGNewQd9BNGw6IHkC4AkMNxyeTIu0rgW8L1VUkneIdhp1-h0IrnJ1m2057JCjPPYZFjpZiYHKYJx6kGbj1dEX7ik6LLlcQGr92QHqJDy4KiILUWqYCl_po2HaApXpssQGEnvNnRYxPZEHu4sqLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHKJyduvpIBH48jo_93TNvmk-IwE4yMr-Y86lQDb5ICi_eacJTco4ylwU2WUQQvYo1nEwh_Kkr6bUeaaYRimOU7qeMfzpf00043fyUKnbwHdrBVsfe1KsVUnYKZUhfDBAYLZ94TJFn8BzlC7j-d22WPAdD6BJSWVl2iNz7fSasmNQpCrP18ST3bFvVdLOsFvAaLKSs6CHzWcISciySeEAPpfF3rY2pwYdRb52biSILaER15bGmIz-XvBjS7znfXkUioFLYIN7LDpwBYYPjOeurNs7ifjFsKZNL8tt_kMuMs6SvV6mGU_cCiUNA9i3oXTZOdI9AbQbURXZ84kHOiVtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBGntGnbwnAF_8IpvBTbtlh-O1u2srNnX2f7YB-QH1ob7nemXs0pCk1yK9_aXXokwuWBJi5IdLnu3tkaJTrnulMTN6t3g6QQxXcYpGRFhIiqNWXoFbOf8z0-vivyNxFFAo-Ag5zvUu-Hn_4nVvTVQS2aKnwEdgEgW1yyy6NWImlidw1hXx37wgR9LDuYrcriGy8iHBs3MDRRxWNCSd-nFAuFSBlA-oYU1yMwaSr10ye2WTwU-1yal7tJMtYv0GybR4FQ1zbI5SCugpxYllkIfQz0BIJdNHJ9VEWk07JItzN3RaA_gjL1ApJss6gWGBEw3IlWTWpEWoXit_cHH4ASqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkK4vIbPkg9VOo9PaI7IN66Rq225LCBAQadKkFI0WUTunnIg_OnIwbhWHGpPta0gRWpcydovWBhBZb_2O_edXo4KHl_SOrZN17ji_RR2sD9suLfvX-AzA50RNIX40tDDzm2gcAYE4fSlcCnM4LBSuTR8ye_tZvrrv_FYH9uetP0Kna_ycwZQkiMuxRWB1M-QPMqbz0lM-FYTXAH1W-roYuD9hoEcTp5oJn8R2r11V9_eejR6vCJYeny0jIRiqqM57U9k5a_E8IEdBv9Mu-02ry3S-8vcEUrX0N_Tl6Vq5KdMvV9Euq8qaPyqAg4y8xzNq_D-mx-iV06Z6CvdZ1vMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TG0DAt9Ltb_yhBRYoztspTT_S-EoSHr-CG_Gsx7icmMDA3t6mHRyQ7s0XCMSqjbkn9NMTp_XmT0tJjY1hwiVIvCUEzKDhpWEca8xsSRCIJ2E6j57H1bhO-j_WWvBand0eSm6yo-GlH42fzsuztXDxpWvYyhjkzvwpCXi1SHr7qEGVBVAmYmhT_1jnNA5EkG69gk0nD9pu8GBPMQvSEeP54WRWBXtPf17dBMYoN-pvRLSQthqghNOMZPoWFvGksJUEMmvC0L4_hC57wn4-dJzlSf78DHMMAcgjGP1l8SLxNjv09Rhbo-mIo7dbxGeW05E31x06g6jA71960IdBJCPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOZFfA_iCILwtm3-xdClbZPZ2xHYx7aQtjF2xH6OzKB8XycAd_6_ryCzKdvc6VbVDZ13RySjIv2SF1DqrNJoMw8m_nhPOO4wkdRj-S3AsWmhpI3eqxTnnzMYhP6Bt6f6lqqy9DRgEwCara7sbjNMDMZHWB-iW0n3SqJvZ7yf3Vs3CU3dhCgUTj4Nr33Uv1bmZ9eCLOSb8CNLSJtntPaLVrTNx-8eM3DWYVV7HQj12_PNVZMfSm-6cil2knLOTEM9U9o0_8GuPQTJLNAgFMQFvFYa4z14HMsvO3adcBsxMoBpPN81MZ9HbxNaGrzhmz1Kem76HOT8Yfal9gCQh-yX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6iTnHZoYscmniUE5D7lLtKRBZY6D5DtmgvSC2Yqvrg_Yj2dj1qnCdt4UsdNp8zC-JBKi-AxvdQFrhCUmoo0zr_UTz_GDBvQrUGeTMOlt3JuZpETi73l-yCTf31H0iTpk6aJubtWTpg2EvsEU6ru2u7dXX3u3uDfk2O9yb2kRL9eDpBoSC_GC7ShEJiZc7ELagUK9BjVNucEb27qwk9vN_rvd3kOmo4jfmFjqjJIrRL7Sv12YeHE3tk8xtQzRiDhF_sbGXtlgUSmX25LewYu8TYPp9c1ll7z0btSY9Z39stjEOXxN5q3boDyHXLx-_GqV7Vr9-MClc9TbfGSBf9oAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ7w_RWHFzTukpk5-vJZQf1ywQlUwn1Zb9eEB6tS6iv-HG0KEcqY9Aa3GRaawhe042loCXIPYl5FyndZMzxwWIySRzQhwAtqGfdbiSOtFkVtJRkiG06ZU3VtaGf5zfcV_aMMrIGDjZvzJ6jF9WVwIPOhcNeB0hw0ezAYgzuxgpLcZip0wdXqXtmFa3GmVQ8o2coKClgM0dqFeBM1K9WuKFB4DKUBLR_v0ZQrgZJd2M91zLmVs7yCs-vR37ag4B-af08YqOQ_LKvB_xwlKLJq_FMmBwY4io_03J1QHafl0Ij9V6DcwnINWSS9ZV-teVIPM3GtvGIFYWfC0Y-JGwnkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebiYuA7G7i4N-dGu9cXfbQvznNvXqBmOfnspIGhrFQDpLMLPixVCcRGISY_u_wZeqO_Dkr8KLIyswXUZfN8e69yNqiXcabJlcaKwnBQS2mEyvaDOVLC57yOxh78_3f_-8e2wEq4-0KALEM9H58XOD0pgHOEH_4CweSPJKMB_8nyuNHdXQ_ysWA8x0aKTFJfGtbhhV_jJCNXA6CwN7AyBNqf_NzGc4Za_v3kh3W04Y0YBkf7TmPxR_xSdMvHqqmyoMi140tjPj5DMyFw5DLIIPDtGh2UmORAh8zs0wrJoDgn5cqqSQ74FUeTH3KXPe_OcsHnvP9TW5kD0X-arcTaAiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYyOXDMTWRVsiMX0r3pQabmM0XmoZ3061Xo1ulRurOgBBKVL0J9kFIij3PFkgsmi_ImrgVwt3pNxXfVM1zM79CR-0FhDkPH2SUtlBUAA8wzkGXfGQBoN7Q775cb31Ae274unWF-dc8yQGWcSNhQsDYg9F2f5WYywsv2tRVjT3V1LorBIDaWp7muqhVZQgx9zffyQnrw4_S-dyvnWKIHR7loUq7RCzIj6mCAvp7mkC1vNzrgAG643rHomhumW_Hqh_WG9LttAgxw2QVtT5bAn_xIG9ZsgzKoDYi8iF8MU4KlVbQ_3lSFHlMJ8kLKSiI6anAkZAt9IK9DqyYLOGgjgCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YynI9Tg6Pxb9BKLS1MZC_KIpit4GBqcLuK2oyA9pE9HGiwWJPdkZ1lbJ43aORSkgCmc0bi2Xy0i0QqA8S2amJJt_PXXavAWanHpEpZH3fwYCTjSwI_9M4w4sGlHyAz4Oyq0-LkiYRqq8q8AZBJ3N1I89wMMnbtvOpAcvPn6EsdRi4fb81od9HQKPEfx6SWPR-cY5kXaALUrxNPu-BxwauI_xgforZLzDPsXuBNbZyNGjFa2T-2Sbd06Wj3kijJP1eMCunmqxzArkN7ozZKAtvm1BNihAqBVppf4auWwxdy4SZCGT7U9EsDtb9EDzMPGnAr0ioNOseiTCOCR1lzxAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBXrfKd11SJZQXptoQzn3UbNcv0RLhWxRJJMozsLD9ugcuTuzsUIBYgY1SVbgB-AptYuFiY9PEBDUplfU4Mz4bJCo1ZVqk8oqk8JfEdCj5weiezVXB-mdEhyKkpK-LJRjRHO2HHV1KAq660O9QnpsPgs9QxxEDIvgG-tnjMKH-_DILT3zQSyHaDXAS9nU4-wWdBBmQr4FkOAYH1B7SGXjLoAEWTYwijhLUQ47TlrYb88QAi9A27CUuXfoY0TA66HcsdMHKKrRbgA_kF2lvfHBFThtrGScwsWXe3i4AkA7-h9apWXf7NH3GUWmNVjdqG1nG-Kc6SJ14G4gKuSbbbIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGWqyDz2kjhxtiCgb5R-rPVZxCDn-PUGu7gfbGBhfRYDOIORDzcsFQdjdEanUnuFGy13rrWwcwfHNSwKGLpG5VJEpAKi8fPmuiHgVXWOc3uoGJNxa-_sTueLeMW1CaENsRTU1FsufgPUH_OqbeHdrsxGEt6BcflDl3ZmHzFbrFazhuXhDZUtDlLqJ5JpfYjTQsrQ6aCnHkmGK8IBi542bCywhrJu9ZdjxpauSuT0K-DeEa5yshBKTKp3Z4ZYiNz8vYXSZXhZg3xFwiQ0fQUmw6UYiuEj6Xz-Gn1IbWG7kmPTuS8fOD5SLMeXKeo3Wes1Vc1tSIvAMVZ4lIMxaZdQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KH9fTvN13nnY72_n-uo_q5XVTnILneZ2gVx3QXTfYMpB0igfAGlhr3AMiQu-YlHn7pCAKyQmMCeeCW5zW54ieS1T20ygLRbikpUQOb8ZHyBG8ZEWWWsq-dM3bNOMDBd3EwP_zn8Y-AeRpxNEkoQB9uwhzIFqyRt12gdyVjVE2xWUfM_tI0FbhEkcRkgVlBwBKcGv2EFD0aVOLYdzXWi55mThDHydtRpnzOND95iNE3TU49vE8V8AYYNnvwWy_dmq1Ov4Fgytg2pxzDUgfhpyzWg-S6n3S6qnWCUEYAymNZhy-SxcYlPz1_ZPNlCcwv7hYHYhkdTEDkhNKDrqRL9-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbAtIxfbrAp8rIgpCJXpZTiqsaBMqPm_OQqcF7L4o2fBKab2wv2GFQuq4rzbs5dA-6-1pk6OeexU_IFQcth9G4vZ3LMLJp8yTJ4W8X_0H3cxWtV2Rnoa4KlCBhpkYEqTfzLURmTnnB5o9dcd68Xvo984RFB1rF95z_X-cr9L9sQZOWF7BomhRYEAxTi_w4gCohbjr5KWz8DPtNewpFcEh5a_bERv6sQTVPkT9Pg8vfNampyyWpn-t8ePGF0eCuX1gJ3ZaxFN-5w6WW78Ivh7DYxFwdn-6mNUOfsqUwOuKOKCH48anL-5AKTjoDIplR5Gq6z9dBnx_HhKwaVx2-cnoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFZgA94GZm-Ls_oD_65Qgi8fIP8HvINGhZJhwkomuqcBQ2oKMV5DZ5hZyyAz2GCGG4B8b888fq651A3qNWKWlc174zFZDw7wZ2NYImecAZ7Yc98BNY-lernLvyzufjIf0AtysHg7BdI2Wkzk9UNU7psD0qHZml6X1sUwU_rak4Wh4UZJ4K99EUnAv2dZxkLVQX4VHdzX7JQ6R5Bih6guywL0cSKTC3-v6oGmSZ3520g_ZgIWdFvKvIuUhyHcHLBpLT8Eo5zP2-7RJjEcckgZ0vkJ856Hbqjo_iUZqYz52qOKY40ZBufbbKyTUfPrwH51xo5F7sgjTWtxdWsfQSVR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQNRVXZJ9z3VOo-Ptyc72ug-Xvq2a3c1JcQi2YSNt4g7NZPyGmInVnhDvPY7OnjYUHjbkvD4D0JYun5CEzigfyEXp-XPzUN-4vofZwnm_iWoZisp4gTAESF94WcqE_CRDpnQI4Hm4ny63zWZNX2Z9RT8e84xwkZsSX_4UjNcqaRT6u-KMPSxla8tMzlCV0FzUUjq0-8f-W8PbZofTGv25NQunZNCaD9ilkBtPu6m_CyJ3G73WoreL3tk_4O6apPrHav4LrtHaYswfxP1_vdKugjteZEEQqRdtNRmBfP5HKMqIw4XdmJPzlYp9JbXOoBMqiw3e6yJqQ3AhoBnLp4Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgqwHDjvRW8GxZm4Z6udOAvvgXhOanxzFdXKPWrFYEBTrlsU0tO_Krp2E4CJJ7DCkw0mvBm78aG7D-FiC88Ob1_u2Ey2Zvz10cwsnzVeN930HVhnu0wXWe351cCH6pJxDGJ33TqEhqK2NlySDEsNSOT3tTgJvrSkBat8FtQEbHEqiv2OBrSyLxnjq_bmMSCHYFgGyTrQgx0-d_SuKWp5LGcpE8PEdzWeRqAGv4_hqIhSWL3lWTkgvvy-u7vO5ySbrXwtqFrZqVtRN2LIZSMMU-3vZwqYUZox4ukOwryv1N6OAIpKWZSiHWl_8uH3gIIXTH4gFkcOs8beVJPH4Imj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II7l2wJxedLCA1f43pxujgXSXKs8VYOOz3NhhQODLW0Gkk8Rci7xqh4KnEPoQvo85m5PCfW5Kxms2FxYcAGyjJYTCy-A6FHFQVPb07fR0xVIafHoNoLkreshs0T4UhUCsVM2mOQFGxq3_5B7qU8IKWo20HLdOfKgSQ0aLT7dnkOXhCrf96v6B7xvs0M6T4S6GvU6dCludTLkUGIZpPhbFUDXFmLnX_wIf81josYrdcOoZ9KpClhmNvqvgIQJBlEICbbw_R-qDo9_r30mf9syqeWVZ77LD2FE9VAZAxbULsM1iDjdTHQTcnho4exH2EWJhpgEmSjOaXksaawAXbJbsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZGuAaiT0vsVJ67f9uIhRaf4IyQVxqx7u_ELBRBktUSy791erv8CL7m7YYo6mw0N4-mut7NRrJCxARHbGU8eL0_6dcCgbHsGzGOO-aExHj7JURaTbxfNpzivMSYvhKNY0JeFL5WhaA0Pd0NlJ3daIHKgf9j84wSeMU-HhaIMpEWrjibircG4JuPWKqLoAaCLbY4TArQcS_hbHU516KGmmwRZRDQTEVnvDvoLsd-n_dHRT3RS0QPY_BM6rBOhxCXVPJBU5S4pKCO-ZFAjfs4bxUOHAhWiCZ4EXRfA1WP8p3_EMp4juUt-XESrf37qKhoEcuEpz2U2eK_Y-mYGyvapag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKg0J9ueVvvWxeIXoCgRJFPi-9Vh3MpT1JBqMLXSyNZd3tZYMimZPIeo9HTNtEtAZ_gb5odHxcV8YwJWuJuIG7jWNlSZ97Nd1pxwksSc3f-vrsSCEDHx7So5M0I3seXojJISuWdI8xYLvf2Jy75K3T-qUVrYNNnYaJTPPTZQMACCUWlkYFsPAXkr0RSlgGhi3jQPOZCI_mg5jzl6U6s_RjpNFiiYSbtigW5dUUZSscROdlDh-GIAqt5q-sL9BqJM8LVTJdIJUAPuQg3gIOYaJz4PWX1PPAnLzTujcCp0F0LPxfDquTH7Z3nHha4ZT5xRzCDTCKIO147fn_geeRxrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLymW1f63xAdScPbThzPq_PbPGvvz0jp1JuFl13iT2nrWfNQo4NXLW0r0fPu9eL6FwE5aouKmC8oWSPjTPSaFXx3CVjv3NWHFbbvFY6P5NVGpppbNZFhSEeN2_FW8nJaNYxdJHAmDfai3UO56MR1rlq9DaCnn9Lgl-3pnoAbmvN5ecwT6-htuXmtrmyxdrwX4XJdbYngvwnDwMTteHArI2q7ZmLm4GdcFqRVbU2Z_H0-Zj9tpX-GkmAVH6QiYzhYYbeA5FLiyLICtb8-7sU_gPSITMvdYrBvUx6luHFQE2x4sYMQq8RSzCBVetBXE2YI7UnBF9l1GNMZyqJCW6mmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMOAXwaYj7iS397H4VOSi5Md7CrQgdZD7-hmkmo_MjsWd8CsxSvQgyv6Q0XOfyUnlZ8U1WCLYSAdBweTfLmQIbl7Ce1jou5MDDS2Mm5WZrOJ_EFKyqnghpItF53mAzn9V0LuJ-XySzDicP8zON8yTDcsyZt_CuC_Dwa_GUPYUNBNj57x6qxdAmLj0Nh73VPMHYZIK8RdOJbBYaE7zrevqYcPyR8wAlXih0lamjjB1L8iya12-QEsrhxomv0TvXAi7Wzmx9G-WQ59SEqhpSB-LXGD_FTCJ4858oI58kzqniqDKlJpbd_ocCFArhVsnptOw4j9WUCTQKwkIIhdRcjrKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS8M6XPp_AZ_U0AqJDsQTHCsENLCxv715okaDTscsy1wyqGzTanIDvFHd8mGrBmZKB7ev07Bc6a-uQO7Z8mn1_7rfugj3Y9WCLXqWA-7Svg8KCSBsRcwOwStTh8BHdFZJB49P49sZcVflBdNY3nf7Oy9wO3wiFBqhClgPE7dxY3C6JTHVlPNTUok1jYNfqxW3zXNmEFAK8ogRohf_dABh-4JmSvTJztVKFp7GViyrcX-MXwfd4QrU-nJlOnmK8QH8ldu_w3RvrBMrka9NXRjPDnhf1x8YPK2GdTa5FkyD7A67mGTLJWhRwmbjTtqOHD8kpOz3MyChQWD2ndogZGkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHoUp7cJB_ILYixherzJ94ROHBcJn7huRDcvTBoDHPpQdX-vd4NRV8BHm07-G_FepiPKV9kGI4RH2mwz9OQo2U1cCxk9Vky1-zNysXa9ectSbCR8N4xUrKi2BD3LEBHR6o76L7meQszNPDGRzYgEwePZ5ToU5m8Wqp1sz7UHeREMgDWa8MSZ2x8-tiYH5Y39uEJRQgczGYcz3vttLxW2gq8MOlDoZOq8EIZLQEpSjd-0GYA1LRRF8XFnl4xeiJFJhneebC8GPNGU68iQmHv9GS_Lm4AM8Qo-DoZLUklyrPNC3arhU3JdAw6FqRS1f6a1d9LdqqcJga0or-m9YNKHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0x_yj-nimFSUPsTHhwkXTmHFw0MWiNGpTzSFamE4nZdZ8wPMp75Y1TTSo09dhVE2xBEmbGIpQoQrVItyeLnP-Z_pdoI2BiZXHUWbVAxhugkuc67QgSLmamnAtVF0xK2JZLoUNnKnXJeQA4BIOLA396m09MENb_qqhMMtqfQzUFPmKrvVuXwfSKGC5HTqllr4OfCnhGzANOeWD5t2RRMeB_hlBrQiaPu-igzjSrvznrhuzvC9G4Pk4tdxfWqVEeBUERIcyObXWdkY0yPOQvUPgNeGxX4fStysKlwngB5Kh5PDnfEUtVbdAZ7Grz8kPg5ujZP1-EW9zSqP14Vl7ilcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2umynLi0Wyfle6S2ytyuCYWJ6fZ-n76W7recCx_20RAEi_SuaxNrNCOKqm_jMvs5_Ug_b4Z2J3j_rxplf8oux_WZak_PthUYtcOs_ICXCHKkcFHEBuM3SZCana31cE5BaXAI5oHw6naUxLear9C6PThjEnrIoshIzVKPSmbnj2zlg9ncG6OpRORw_uRNq8_lJEgv25LWpyh0Ecuqjyssg3TcaECedsiRemlJbRb6RopKhPI-J7vbApVqygbiwHKU59J0YNUcPunzm4S6vIqZUhnVNbjvmwH3kwKuOCtO5QGqrzg_NatMpdLVzyLi1jCLorou6v7puBKKBXZTJqizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF1OBVglZTgbD1xiEMI1dxDmJIy7jDBb834SLi_2owVULcOm1-onLoskIj_MnLi_LJSNPQeQpCspOcQOwRHJbWIlT4RpYNczLhTI-7GolWwncPnfHfK6KDTAi890jFL9EJ7V7jvSZrFmSb4DLT3kOGSy0v2jDkGOJKNc5l9P1mVUlRkBqPc_XidOSgquiP3eHe-Ns2vvvUACwyw6li2nd9SPrJz1kBSFwF2DkcISz0QhPltDGTQCRXTtgvvuK4nJryh4ljUB3R607qAQV5NCOzHI765iEeU2MHS3wuvkMmoBhw7NwicSP8jQHoZfp5adz3kwXG9_XHzSBa64BmRrgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-WatpXff2LwPPucgWpFyRDMgKSVZRWXcSOh9t7XVFw1ZRire97_KzinKioLDHq4RGau90X5ZuQICSk0zsudiE7qbqYZ0wSUJOXHUCI4wXBtRTOvR3k7Rzv6x4IgHqCnICm027w4PFb7rJTe175c8pE_hqJ0sjdQbn-rAt8zNr0xicRazCgdH2gm6688dpCPZpaT_LaJfBJ_Oe_Qz8ySLJlW-ompgouEpw9WIALwt4ym7jjPTuQZmhzF6GNLwysdwIIX_0pRXSzHgmUBowp9vOGPXtEm5jUDIsvTK59INWb9cuDWY2MFqmSRkksk6rG84M4R3jlYPnyNXQ8-MOEqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmeDeSKgCoZ90OMk4HbFGtQ2rMzreOqS1I-vtrqF53fHSbF30TSvwQp6kKmTRzJ1IHFQlMbtUOu4hXcpE-jnKjAYs1aENvUzNdWzc7Mu7LBwMerheVQvJKjIj1HeotwEGbtz8LUro1OUNgVc4Grrrtnk1zplJQHq8mRfu3L_kCSKGoZBNRO8Z7EbHsiZ06oBYIqta-GiFcXTU51Yyo29pKgIEgad20Ap6fSxHQMJKHKcDTNlaXzmJbjGoluO4stZsNxqeS0QzMJ4h44cbTCZxB14m-lTtuOEzA_lLL1muKCe-JkN1fDrW-YOVHXTY0zq9T1CbQQf5S79tERPzjqg_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHdoYrhcvFiC0dULYynK62gQvYc8X41kTv96_QuYiTzOjBEljcvK2L8dDT7DvtonipCHfEo_a4H43B1JGNhXHc_l0x4PBkqJPYe_Asj9N7onTwTGLz5Iz-00V8oiIWEu3K3Nxlk1rKaOYEJkrdQDyWPzB-khnmGBXJDupNbJITIAgJP8qZ1o_-vvoPf4MQ-6_XzGwyi9I8v_SUGfoHz6a_R9R5YcRCfy9CrfCfeSib_l0JEIIeRP-ynA5M2OmKcGgfQQxpoB7mXe0uVF_6lG_6ALkKkKT03z8pgAU146nhYLTUmW2Z31m3X0ID6Xn1feIXD_w1qPBI4giFofRaoWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=CVmCkaIgJVk6qcEr6lXzlqdV82BrF2GvDTeX_IaVlq86JMRjsgfy9F376w_z064GnMv7EiXabL352Xmd0RXgYT41xIzeL0bnmG7NRPyVwPI1oLvfhTOQcDICwO7KDvbz9MiY6lpVGrOFkWFX3hOK_OQrmSZW3xeWuaxXIWu12QIaXZxUeJ1_wsd6obBC44JTCybOTPjDPgzva9CC13G6LQ6V_0vxnkBduxojOEaQA5yxUnmL9lWyYfBcse68eD8daYjFnwtmKhIJL2owJOMfVYyGZgVfWiSU8PoPHXlw7UHAMWDG3QE1hfV4Cx5QOxahLCVcEC_d4cpCkvcNjAa8bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=CVmCkaIgJVk6qcEr6lXzlqdV82BrF2GvDTeX_IaVlq86JMRjsgfy9F376w_z064GnMv7EiXabL352Xmd0RXgYT41xIzeL0bnmG7NRPyVwPI1oLvfhTOQcDICwO7KDvbz9MiY6lpVGrOFkWFX3hOK_OQrmSZW3xeWuaxXIWu12QIaXZxUeJ1_wsd6obBC44JTCybOTPjDPgzva9CC13G6LQ6V_0vxnkBduxojOEaQA5yxUnmL9lWyYfBcse68eD8daYjFnwtmKhIJL2owJOMfVYyGZgVfWiSU8PoPHXlw7UHAMWDG3QE1hfV4Cx5QOxahLCVcEC_d4cpCkvcNjAa8bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1O-PDluxzmdMy8tbVBaQFve7NVzbwg72x5LjkDB1IBEax-e0IG__38Zj3inrVVX5Zs-ANjOOWPej1GwjOVlCx7hFrinNkrmim9ctH2q8Kjx1Z1OeMFmd-Bwx8GS9GIC5HCU5UEOyfCcxgpC6pRUg2zireBT42eLN6YnGmPSiU5SW0l4NOVh3vCkXHlS9vjv-oPfE2QFw_bbn7KSOKva9tdRPNlax-Fcnr2ZLLweKz4UJ05TszeHL8245qTmiE37Jtk7oYnv9lqh1mZcrkP8UiQCrvG9rqb_e8wyjY44ZRHGel6Hh3qH5o6wNNC5KXG2-bMlRB0u_e8ViccHBTZG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=ODYafw1DT79utv-safjnjYlbXJPmaK2jxs0ZoAc-OU_pjic28XRVNYbZsy00NtxBdAD8E9_Xo_WjZwVAToI2CQkBFJ52t2OiS5Wt-gcvGOq8TV38Rnvo465cVFN-fVALHSX6ydDhoY0xwa6bHns1bsSBdmSe7qapBdAHKgxQz0E0d2zj6pGmuW4EoNlWKUSa8WC4NWlaqmIDykjihE2jaSeYbVr4kUqTqB0d9VNDzhQOuejJ31djod0k-30EH92aYTsJ4f8WVSxhoFM03pq70h6l-DWtll69P3SsqRJRI9Nqi2iJD0tGlTSpUS87uHa3TYnJJwSTj6aACQboQES-7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=ODYafw1DT79utv-safjnjYlbXJPmaK2jxs0ZoAc-OU_pjic28XRVNYbZsy00NtxBdAD8E9_Xo_WjZwVAToI2CQkBFJ52t2OiS5Wt-gcvGOq8TV38Rnvo465cVFN-fVALHSX6ydDhoY0xwa6bHns1bsSBdmSe7qapBdAHKgxQz0E0d2zj6pGmuW4EoNlWKUSa8WC4NWlaqmIDykjihE2jaSeYbVr4kUqTqB0d9VNDzhQOuejJ31djod0k-30EH92aYTsJ4f8WVSxhoFM03pq70h6l-DWtll69P3SsqRJRI9Nqi2iJD0tGlTSpUS87uHa3TYnJJwSTj6aACQboQES-7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUVfGreNL5nljE7VnlI0OyiFcIe1H99kwnm6rsrlUtRNFHSAd_-M8rU2UmF-I6tRi2D3vHhFHkXFFEShPmMku5M07LIlwy-3Zl0C_kusJ-zWhFzv0rPzkKc9Z1CDP3xkFIOdnoTc4LuuRJCOLdAXjZmMx0L61oBN_EJ3dAx9OnVXqimQ_sPvpNsIB1eRyaPhpf1mMHXsK4i97EcmXl_gBvd_pEGetb0dMTLrlfs0TmzKAicITW70qOJdvkOzdCZnbm5aOTfAkSitSZBOjOXrO_-gD310M-EnrLDNh23tM_HJIXnaK6b_LU4DdncPawb1nrEVKMHAvLXy54RW6nIjvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDAIP4rVpqPpPOgdxXU0LP_-r9zVjBF5w3Wdedz9ubg2G9up-MXKIJSVQ8nOulHfEBUACeSR-y-h9DQ82JnOrofWvpPT_ZP5zks_0x8NxkAMf85z9U8rfltfvUxbzwFd3gsxvaD35YGn3LcUIB0wS-vk8zjsbjl4FGanPTE--mCz9c8yT-BS1vHWtMQdbXMb07cgBwf1PIvowkOKmA6Pm21Q2ffth3gJNyPVh2M6yjWN-NzLIwIuVQiaYEORcCHXIWJvmOIr7_ujgK9oSzpqivZnEwojqoMRbRRbqN3qTg4msMyjyWARJPspJV-6HWur9hP0BNwDqDPMCTVBtKQPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=Tyzn8wtBPicGpf-RqvO9QxIeBN2u807LREErZaH8nsBRl1bz3LneqbaDRUbRNGzDuMiZPAJK2qI309z_uEOx9V_LmJxjEw-XfTd9KbUOO7h7SFKzei2xleqdoaph3YZSi5aFFC1emkFP7EE9uhJjtwk5owSpNuvbinv1f_ZVQBAi0jsVbCzMPqAPsyX-TRrwiqrAT6GrtTZW_8AG8wV29TuY6EfTluJSUxyRTOyTIXv_S3dSbHNZwEouDnedivBW2q1DXru-ZoaW10F2abUSRuALcSQPvIe7SucgOWdSnFYNyRUZSKVGf75gjsK8sEzpwQjKcaglSMo7QqUy5Ej2nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=Tyzn8wtBPicGpf-RqvO9QxIeBN2u807LREErZaH8nsBRl1bz3LneqbaDRUbRNGzDuMiZPAJK2qI309z_uEOx9V_LmJxjEw-XfTd9KbUOO7h7SFKzei2xleqdoaph3YZSi5aFFC1emkFP7EE9uhJjtwk5owSpNuvbinv1f_ZVQBAi0jsVbCzMPqAPsyX-TRrwiqrAT6GrtTZW_8AG8wV29TuY6EfTluJSUxyRTOyTIXv_S3dSbHNZwEouDnedivBW2q1DXru-ZoaW10F2abUSRuALcSQPvIe7SucgOWdSnFYNyRUZSKVGf75gjsK8sEzpwQjKcaglSMo7QqUy5Ej2nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZw0JQMxfC7hKoWaeswDFGdvoPlYJbWBdDZHoOfFoqZIKKMCfeDO1PjLd3ucL86K2OzwlbEeUlmm_jNuJs5TM_Ry4PKNmvorzGxK0DSKoHV16gCm6oFb4KdMWTFmbTJujDflMlfyZ6HArYuOpuRYCNWTITm43rJtXkfHzDr73IlubBoJI9vsbA6Gj1TvwQqRLNxyJT5QwVT3_zAiUV-7eOGVn_JG0Fh4xrU8vPctGFE00OmT8kz5Qu_AscbrvCm6kGvXSv2DMTjk6Wwnt1rF3Ztq_CMMlPRCoyqSinYagrcn5pC_-M7R5Wy4zeEFJ1ujUES2-y43ry42OTNp84SyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtMX_NKQuiyfgiIvnhSK0BbdllAwgtkeKGWmAQ-lFntMAREqmiRalRKilKWpJcvivPWbVeQKLMt_eVoneNAZQSABDemVndCmgWrzCd3eVBKH7rwtQtaHBYIb4tO7D-AX2tkCUQTw22uoceLuEYHcwavrPPbFQBqnW5Y9ZMiYYSnZNY20FULnsBMoy-pO4ApLoVroDfzXUV6PNniYvSpqPOc4_z_YVCbkzmVzFmWr6m2d5AinIcdBTSjh1kSTq1-UxlqearixZ_FhxOv50Jp72JP7bVUhS1yZurm0zPtXfNCPJf0hEurq9fx9Q997dZhz_AoWZY3bMFo14oJG5JdHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2uCTLpta-mWlKrbFEgvJlv-XBT77-0WPbeceClkdOprkfhWPqutbmQNjyw5gtf3mPS3TZdLCeHY77Kmv5yUWFS-cqUdq-tb70UqPIYuLagUp-_Ssy9N6-49DSxfvu2SssxREuDOvOaOBvWMbR7y2LRaHHqE_Gv7tdTDgpVWTLQ3dbCxWIXhPDxi1vHRwNiFVAG42m8z21rRwNBHwtHZPMBpheA2QumVfFMmwz6ornF33ekpNDFCfeo7yMXEkbbN1SYw3_oZJ2ViEjT58LysGoLF-kP3a0NhmwIFEeQYKVpHc_SjtAZVOmq1kBLAam77BFKlfqIjI1F-7dkiU9wQZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=jnL3nfy4xdLtDooUOF1uxqxhPY_VRccDStCCSd7valNiWN164UjP42P4oPKehpLjGL9O3l_ud3v4Dp57UaYHbRmtG9WwY3Ab-dj1FrRv0m1TeQudnEGel40VYQSdjqZmk5KY9OBD4VIgO56aq_89KABlDeTyexvm-q93TsAFXPYiliQ_DS4GjD3XT8sRjH0Qd1kMRrZUjnWyCnLO-TKAqqiOyljVvvklIZ_pEu97DNnbhy-w15MDYzXm1Ap4boBgVAgc82xtSgeG-0WRUwnPDj1PexW412xy6hTeSVEXYJZtZpymWZDtV0QlUDLNQB8VS9GYS69dPR6rTEtmyof_-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=jnL3nfy4xdLtDooUOF1uxqxhPY_VRccDStCCSd7valNiWN164UjP42P4oPKehpLjGL9O3l_ud3v4Dp57UaYHbRmtG9WwY3Ab-dj1FrRv0m1TeQudnEGel40VYQSdjqZmk5KY9OBD4VIgO56aq_89KABlDeTyexvm-q93TsAFXPYiliQ_DS4GjD3XT8sRjH0Qd1kMRrZUjnWyCnLO-TKAqqiOyljVvvklIZ_pEu97DNnbhy-w15MDYzXm1Ap4boBgVAgc82xtSgeG-0WRUwnPDj1PexW412xy6hTeSVEXYJZtZpymWZDtV0QlUDLNQB8VS9GYS69dPR6rTEtmyof_-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=oFn-AwhhIjYRgKLy7gGHVsb6zglW7FdL402XtL62uwfgTIUfgfUivmjqtbstGELb2zZXZllr3YptEhW9mAeWe5fOO1AeVz-T6rVN8Mtx4TmZcQM3wIRQIjeEfVMAuJcOEoIBhiU59C9lcEBYzRygh4uN3Hnok32DvNRW5CMBGIqiJ_CN3k7GIhBB9w4ZGCRXubAVoKm1gA4jL6COWmwH8MLHuAqT0eGm1dr_xCMikrPlr6MhWQgE_HfAorVt5J1XYOuSWfdEveScNCZiwi4SM43ZE0dX2HcqNi3X0IfC9PnLAE_Yd_FnUpTctWINK4RlUC9wZVeIKGElHtQiX6u5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=oFn-AwhhIjYRgKLy7gGHVsb6zglW7FdL402XtL62uwfgTIUfgfUivmjqtbstGELb2zZXZllr3YptEhW9mAeWe5fOO1AeVz-T6rVN8Mtx4TmZcQM3wIRQIjeEfVMAuJcOEoIBhiU59C9lcEBYzRygh4uN3Hnok32DvNRW5CMBGIqiJ_CN3k7GIhBB9w4ZGCRXubAVoKm1gA4jL6COWmwH8MLHuAqT0eGm1dr_xCMikrPlr6MhWQgE_HfAorVt5J1XYOuSWfdEveScNCZiwi4SM43ZE0dX2HcqNi3X0IfC9PnLAE_Yd_FnUpTctWINK4RlUC9wZVeIKGElHtQiX6u5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J34AFOELR9JhhH91uXSCr9FuuMQpSfDmrlrZttlXgyu_KluBqrt9EN46hGUFhQ8TdugXrxcoeHkTzHgJSKeIwyc3nnfr38h2Cz2XE1HGl3oNtDttraELOMfLrWBRiAlTDQN6zpLe8fRdPWu3f5OSGDs9moSAD4_J4XZiZq40cEketPZXjaXkYwTOk48DawFCpG1DotIQNzL_3d8ooQkDe5TG8iQ1vIYzEq1SOTIursKFJlR0qtEU6LCxJHd0a-JK9q4WQmtaEfgdAuNLIPGBmQJWeC9J2GHKPIdNKxK0BbduGUm6p4bPks1uweNjepQDiN4-wReECI9zMTACUghlTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCZAAFOjUmwlKVmHWuE3xBv9cetb5wReqPnAp5IokvECzRdeJPiEowUU3c5KbU_PXzQZpH-a_H_YNvE8v7BHPM7NvYT7JeY6BtUWcD-IjMUuZ7XMl8w421N-KtnN5CqFnwbeTyVZHzb_zqNb8TbnxHSU7QcxP8T75sxzStYMsRezaBnQOONZps1IZjoIw_gf6ualhzAd67fs3VugxRRcJa_JkS2w7UsV08le4WgmlpoMWDX0yZNPjjcJX3r9BttNq_8znQ0bm9Iwlpk4JgLnSsSt9_T8cDYHvRZwjE3TBneGohw0PhCVDI7M-SSXtovf4tZwqWsHT_RJLcuJFOwRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmNcRsoGr-K3LlKJTg-afn9Bqtpor5msfn1voKuMsj1Md8_CCjKRCuf9bmv1PQKuGR50nh1f5cc-rku_ajLKjnBJ1RAlb7QrdEf2CM1xG0HSGFUPPHwnaicF-SPxWVpA92vkUprNqKsGfvQSX42YSm0SM4N4jj1CFkRu4lXG4ORQSHwe5vnMxuJVkpi7lbXzTfPTlAY9w6f22pW9VcWg_uzBa7zylZOWNk71vVBFY5D3MPa-Ce9XUixCd7oav11evpId3-Q33cfBYWvJfYMlpZVv_rjBjjB9Rxo_rA4PzfaH5q8dwOmLUAV4TDJQEc-TvR4YUVUBMDQ0G7SBVeFZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b44o-gM92L9s8QiIdzim2IEo4b_mkcevyzhJiD4330MWbZCl5fpBvyc35q0G14VTpTVMhuz-ICQoSa9K5mi396KKzaLjGGHPFMSBU1GQ7kee08NKsLfK8Zzj8f49CCCFCC2VzAEYjDi8mbmZwGZ5eAhmWxUw8E8AqmpaYv0ix15gf_R2uNtK-1rHdxpKqwyoly0Aek6CIRPtldp1d4QS60A7WFG3jQO6-fzJr4rWl2oEwdn3vYCRxVpNSXlD4DuO7fBuNMXWujnRNCbxjvDpxQHaW4neWd4ujs-A8FocUejKrBugBuoikEWBoDv9XvQ8xUeAiks8J64O8Tk9-G17jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNORDpQWpd-w_ARZVN-gbupbhnSr_gf1uiokad8sE1Nwp4iDJj9lIi_S3NqSffzfazNw3dWfM4DlchARoZjylLXe-dqMKMUUAP84-Yn0ISXC8b-s821vDo85foOjd94fC6-vzFjB6jAye5Fq11s9W6QxIwXVxBYeYV37zwHnv-Y3UDo8JTHRs4rg0SngFDZ16kwLs7GFw7Fb38OtDszgSRW4Q75RCVIogarVmyWs4I-iS4WdjnExe0wOMjh_bjOGNAAMmVUInxySU2o2iHBjzo186ucnuaxqKOa2g0jLJoWYzgPH7hNGAwHv4VRpE1ePNwAMrnZlAzXfDvTnAhm9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IICSdv-gv6-rxTh5B5e4shMfOt-OCtgZq-R9RWD0sVxJw8fxrB3pJe5YZMtVHO3JJNhHzIVGpDy_pVGmdyVJI6ngXL_fThLQbi8FENQaJ6KhliOKwzF7TkLmJ-02enP5IsTEEenyx3RomtcthW8dmR797ed2FKPBu-a7Z6YzyWyOVeHY7Fj-2HMlK9I8AtRNzoqPA9AgYQ_xxHZfhOkjGLU555U6OJIMmvCIRURzIUv4D8VWhcK8_UU_l591ytxgre8jT7sPlJrVU4quPCZKTZOoUQmPEJBP5UsxGyCr0_4tkLapgCoBho4kgrTWfcYLUEfEPt0FNhzld12o-0PUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqzHY_tldXs6TxEeFDOYdGh4YJF8rFpNWMiXjtGqrecZTI1PI8m7JcTHXdG7OPpEW9FTyI5xhF0PJolV7zMkT4hVWxh3ZF7KODlCBN3GHUwdHIODcNThjwGWEPwCW-hrSKjwmUPGzNl3tz4CD_GkVzopC4bk3KRDq8Xx17bRFXeA1z0jbxOf7gdIRW_bB0bw08G9A9MaYsvkPejr8tE8O14g1im50_e8H8SfxzCYyZeILnfFY38W0qXHhQTk8qa6oXmI0gUKDhTLnAMtM8Ji8uRdhD5o3tKYKVToO6n596Xwz_Sadzs8yA2hA-FFLPCoc2zEUqX-0__BL5fwTZZhfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=bGnmVO579Mn8Y6_quedqpivToyGRhlYOlF7rzJuKQBpjBjDyhlYPyxxDxzNJs1GOrLj0LrbhLrZ--CYJAD9kh6WJ5IifhAkOmhADaHZrdEQ7fzIGWIEeqet5ER3lfdamkRH2rtAQixm3trcIU8pqK6HD5M44CI-2Jwe5-s_9M1617GetjgSN1TvBbdAgXy57dR-PcK9LttTpS3rT75bx0uCtuTfK6Sn4g49kkhTgNe_iv_olH6rbm-5PkEtjZYZH1TOfyWy5u4U91flDBMGEwnRXfv-HrCuc_-jyoxho6sUAvIH_WDqzam9aP8KGjzOsIiaRaWrlvD5a_hXJ5N1rtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=bGnmVO579Mn8Y6_quedqpivToyGRhlYOlF7rzJuKQBpjBjDyhlYPyxxDxzNJs1GOrLj0LrbhLrZ--CYJAD9kh6WJ5IifhAkOmhADaHZrdEQ7fzIGWIEeqet5ER3lfdamkRH2rtAQixm3trcIU8pqK6HD5M44CI-2Jwe5-s_9M1617GetjgSN1TvBbdAgXy57dR-PcK9LttTpS3rT75bx0uCtuTfK6Sn4g49kkhTgNe_iv_olH6rbm-5PkEtjZYZH1TOfyWy5u4U91flDBMGEwnRXfv-HrCuc_-jyoxho6sUAvIH_WDqzam9aP8KGjzOsIiaRaWrlvD5a_hXJ5N1rtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=eaUHtEgJg5kgQ44a93uc9nhpKQRp66XbdMKZpCcvPG35w2c7grFO1SSdmEvPeT-5cDGiJ2KibGse_m3cuXsvJBCirYjONjBiS_9Y6nhrFTtqWyyWjrZ98eX-F8_RYgTTLhuosdPJdQm-l-JxsVS5jbxprNpF5q85tPQvzR7CirgHSTABjNk80piQU4p4PzRqKhJc3MN5uuSHjW5QabUFN2LPBZpmp-KLxhCtZCfpuyZB07OuiBjyhWIK_pkxB4Sb3h5DafuLuHs9fA0DaENQH-6FYz-_ec6edWLEPFmTkWwYIu1amPuwHN78Qhxhdokqx7ml5WPQ9KeyWnm_xQ22yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=eaUHtEgJg5kgQ44a93uc9nhpKQRp66XbdMKZpCcvPG35w2c7grFO1SSdmEvPeT-5cDGiJ2KibGse_m3cuXsvJBCirYjONjBiS_9Y6nhrFTtqWyyWjrZ98eX-F8_RYgTTLhuosdPJdQm-l-JxsVS5jbxprNpF5q85tPQvzR7CirgHSTABjNk80piQU4p4PzRqKhJc3MN5uuSHjW5QabUFN2LPBZpmp-KLxhCtZCfpuyZB07OuiBjyhWIK_pkxB4Sb3h5DafuLuHs9fA0DaENQH-6FYz-_ec6edWLEPFmTkWwYIu1amPuwHN78Qhxhdokqx7ml5WPQ9KeyWnm_xQ22yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=lVgjwybxgseUniF1FLfNXidPnMyS2m5lw4A4x0W2-hcQTb9SGymgOw1Wr5jXU-a-lpl4h4pLhLPAmIK62ne4r4Rfs0k-4wKrKqNOxcmKMibeQ4godmwMakP8F1cs79GEgBozjaVE1WqcrhARfQqrnWu5cAS27GcIyILvNyFpGBVpy_LhJAccdyi_5QL4sTBzeFRv5vuGDfGdYV_wlIDlWLRAoJjVTwKldpwLg1QNnjj5D4jC_DH_e5CNrsxaQzFTalzvOY4anIPRuNALjAnxS1xpxyQoWfuLAyg7uUG_2exqrc7HEMmeRMNomAuiQ7UZ2o1QgAYOw7B58OAStBXe1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=lVgjwybxgseUniF1FLfNXidPnMyS2m5lw4A4x0W2-hcQTb9SGymgOw1Wr5jXU-a-lpl4h4pLhLPAmIK62ne4r4Rfs0k-4wKrKqNOxcmKMibeQ4godmwMakP8F1cs79GEgBozjaVE1WqcrhARfQqrnWu5cAS27GcIyILvNyFpGBVpy_LhJAccdyi_5QL4sTBzeFRv5vuGDfGdYV_wlIDlWLRAoJjVTwKldpwLg1QNnjj5D4jC_DH_e5CNrsxaQzFTalzvOY4anIPRuNALjAnxS1xpxyQoWfuLAyg7uUG_2exqrc7HEMmeRMNomAuiQ7UZ2o1QgAYOw7B58OAStBXe1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=kcDSo7BlpnyPVLrs9CcjQMKlxnPNzMoCv8bMA1jmGphrW_vYNPDLkr1IzleJQAICcJOGZ7JV3zeggTI4q_yWUnL1FQwuL5caGR2hsC2n62bsHxa55FcP4L-XRm1_itNKMZlon5TwVr9ahHTn8RilC4_lTa5gE0504Wsqq0GdhargGftQKnEzok3mFW0bqKec7U7TYIqMlFR_uI7X67mOf7jSR6qlLTJIBGeXMMZv1Sy8VHjRt5gQ_gZ2PWxoM14xM78u0v9eabVtocSmMhzgPgc-z9jUkmsWMtY8pDxVZelDmMZ3_X7IVAdin_b4D8owdKTRZ1FBVTz4k8q-PiJHzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=kcDSo7BlpnyPVLrs9CcjQMKlxnPNzMoCv8bMA1jmGphrW_vYNPDLkr1IzleJQAICcJOGZ7JV3zeggTI4q_yWUnL1FQwuL5caGR2hsC2n62bsHxa55FcP4L-XRm1_itNKMZlon5TwVr9ahHTn8RilC4_lTa5gE0504Wsqq0GdhargGftQKnEzok3mFW0bqKec7U7TYIqMlFR_uI7X67mOf7jSR6qlLTJIBGeXMMZv1Sy8VHjRt5gQ_gZ2PWxoM14xM78u0v9eabVtocSmMhzgPgc-z9jUkmsWMtY8pDxVZelDmMZ3_X7IVAdin_b4D8owdKTRZ1FBVTz4k8q-PiJHzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=mkOQ5-7HHA5PIxv-DLvoxJjs6jklY2wyjKQ3UQWNPk5GSoPkAIGN9F5xD1uVePbTeQ5Ir5GFztuJwXvnluikGuzF6sLJwjiCnxTl-NnJ_p8P39sDcTNBUO4OpCNE8OCwQVhPTSgRYGIyGQneyDZJ7UATfoWaXSg8nAlqrRElFEmmXgAV-tDYDpimtOn8W32LSmrgq8Du1Owh05hDsrNd8hnqErgqLcHUDE6qBmdJbihIdiDMQV1KCetp5yApLU-yp4BLe9kQGvv5icbNKSf0sSMd9bG9i2HXjOyAWTZftb-Np38PKEvSfiHNV_p_s1yM-oS6WXN-UeQoApf2ydubLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=mkOQ5-7HHA5PIxv-DLvoxJjs6jklY2wyjKQ3UQWNPk5GSoPkAIGN9F5xD1uVePbTeQ5Ir5GFztuJwXvnluikGuzF6sLJwjiCnxTl-NnJ_p8P39sDcTNBUO4OpCNE8OCwQVhPTSgRYGIyGQneyDZJ7UATfoWaXSg8nAlqrRElFEmmXgAV-tDYDpimtOn8W32LSmrgq8Du1Owh05hDsrNd8hnqErgqLcHUDE6qBmdJbihIdiDMQV1KCetp5yApLU-yp4BLe9kQGvv5icbNKSf0sSMd9bG9i2HXjOyAWTZftb-Np38PKEvSfiHNV_p_s1yM-oS6WXN-UeQoApf2ydubLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=Wb6Ahk8LzK8DCrTEG2FHiAyl-BMhmMD-_5tiZhBfvg8MbeVm5Vhyuri5JGHVgJqBeN7Rhv2ppU1LaIfPqyGy4y5vohYHzoAw-uQQP7ga-zt275nUWxcZuTxzOWEg5ZtO4TFKmb7UDKZKL7aR87ifmTdDdli3ZciwAendpVKBrfxHoAan3Ya1k9Bk2srgdWllHgHeOMpWvw4WueVF67yBvBzf5_-1a7eOkvlZjI4TV3QGbPzgKo9QqfgxGMXXk8nQgCKyRIwv7joFKvLHG8YXLBlUlXT3wY3HkRUkDJ3K8CRBeu11qVUU60Q11U2WoccpXdtoHHVC40l4Si6Us9B3Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=Wb6Ahk8LzK8DCrTEG2FHiAyl-BMhmMD-_5tiZhBfvg8MbeVm5Vhyuri5JGHVgJqBeN7Rhv2ppU1LaIfPqyGy4y5vohYHzoAw-uQQP7ga-zt275nUWxcZuTxzOWEg5ZtO4TFKmb7UDKZKL7aR87ifmTdDdli3ZciwAendpVKBrfxHoAan3Ya1k9Bk2srgdWllHgHeOMpWvw4WueVF67yBvBzf5_-1a7eOkvlZjI4TV3QGbPzgKo9QqfgxGMXXk8nQgCKyRIwv7joFKvLHG8YXLBlUlXT3wY3HkRUkDJ3K8CRBeu11qVUU60Q11U2WoccpXdtoHHVC40l4Si6Us9B3Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Axfiei7r8Ad07CZXkV95wl7RILViwqF056mJBxVEd1C24HxUkw8ZKw398-Mw-zALu0HivA_NVanmTGQ5cG416LbWg78uOGxbMZozXxkP5Xvue120Hk_3xAH9K3xMIPxwFlqWrPmpKjG-BN-_dJwzWACr4ffjo13XouadTq7zDIg34dD5ur-vgeaAes0IAn5KlVbliYeRMgG1Vo2VEh3-fZn3WTCo3T86IAIB__oRYOn59hXYbbtmX6iQgybpvvA8ivDsQGNsHz4VWVv3AL6b3ZXCxSno35RcwqecTHqW2tfNeDxs55r3XQlc_ZRM-wTgOkaxj2XjMNoLMR1854u1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Axfiei7r8Ad07CZXkV95wl7RILViwqF056mJBxVEd1C24HxUkw8ZKw398-Mw-zALu0HivA_NVanmTGQ5cG416LbWg78uOGxbMZozXxkP5Xvue120Hk_3xAH9K3xMIPxwFlqWrPmpKjG-BN-_dJwzWACr4ffjo13XouadTq7zDIg34dD5ur-vgeaAes0IAn5KlVbliYeRMgG1Vo2VEh3-fZn3WTCo3T86IAIB__oRYOn59hXYbbtmX6iQgybpvvA8ivDsQGNsHz4VWVv3AL6b3ZXCxSno35RcwqecTHqW2tfNeDxs55r3XQlc_ZRM-wTgOkaxj2XjMNoLMR1854u1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr-s7C0Ek2868BPgJV5s-EYDX29TZ5Jga8__m8aC1D3ATG32RjgelZj4jEE4_ysbuR8Xo9KtlHJI9hepNPICeOWtfbcPNusa2LFUxLvWQp6X6i2Go8amRsTO0k9E3iR41cw9sSPdFtFUL7DD8WPW6wPGm_lhUFZW81HbsDiRnCYlhbGz8qTmIINZpd3Eo9Q8e-W8npVqeFtGptw1mDOn22_stVZJeuHJ0FFOiKJrr2RyIgRDid-pIqUMDJhioRUmAJxw9YHsCboDt8ST3u93T6jGG5aijcIy2eRL4n5ti0D2S24IaunpD01YP84sjUDapUf-numat0OsVTor3SidEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=Fv0lkNDYDXP4AQtsdwmg7l4GHbAMSyUGwP2oYAKyQDjoDZsPfUwyUsdsKHHnyAFmweF2Ec9hS4pUeAB3nUwgejFdmG4wAglJfWgrd7OvDHpWGZ4EyPryGzs7SWJTJmk04D1UKRNlXej-j6dHOfgGwsBeCRdqVHd0Hhtxa77UzwqKQlnj1DPqRnz74rAkLAgeJJBBmh6g8sPhsRhLY7mjtuQnMRfkwGh6PzRps7F40GMQGqGthnSO6_BEGWcvnlkwJx9KGWtCakTArvTBf9bcIvsHGlV1Y8NfEIFi3NCshUSqxgqiPEQ4Hxj1DB62VSxWFJri0tW-tSZUr11idhGVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=Fv0lkNDYDXP4AQtsdwmg7l4GHbAMSyUGwP2oYAKyQDjoDZsPfUwyUsdsKHHnyAFmweF2Ec9hS4pUeAB3nUwgejFdmG4wAglJfWgrd7OvDHpWGZ4EyPryGzs7SWJTJmk04D1UKRNlXej-j6dHOfgGwsBeCRdqVHd0Hhtxa77UzwqKQlnj1DPqRnz74rAkLAgeJJBBmh6g8sPhsRhLY7mjtuQnMRfkwGh6PzRps7F40GMQGqGthnSO6_BEGWcvnlkwJx9KGWtCakTArvTBf9bcIvsHGlV1Y8NfEIFi3NCshUSqxgqiPEQ4Hxj1DB62VSxWFJri0tW-tSZUr11idhGVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVOr0exWTlGtgmU3tT8v9OiARPImp-re3Qhy3HOI4C0t9CB6YsZffcBrTkGyxRhxsyTZuZ6bjr51phFHsyk35xcbUSq3-Asd477_tr8fnXNQ1PMMorygLtbniYL6Q-6mDoqj64Nvbj6RMoZt_54rXy0rWZmKpCk6xnS0NXLW8_Tu0r148II97g_jspTTXSVYA6FHZzRWZ-XwrrDAxeA2xKWOEVP22LtpX4PdbK8yv1W_QitO7M5iczP9G3Pg6GxkK-2xaxuFe__yvk29-x4StF7Ut8g_sExOkZLRmdilgPaIfxWqJFb9E3FiISFCv69m7BYVZ-_NmGnX6I2kQ_gvgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX5VZwK_W6b7GXCntJSWYm0_OtkMVOPEsBx9gCxPkglEOapwlCrq1kiDfpMZ5W0sjJmVqthHLbsh2-tOB-kXoAcyc1ZsBKTfD5MonCYNvf3kF8NWqB5AX14mSR6aWNFge15JGEGaxjU6fjNnwsCrSaN_wZOCDCfDdzuep3NebYaHxPBTnv5aOPQc-jt4RObygXAVGmzYVAkH-i8wz1fN-x_ejLVhCEG5RkSE_V3eeJlJoBWwGSD_d6GWapes42qDaBEkxiMRGXsRw-QA3e8Qkn1NReSVu7Dlf5uaxOS90TeMJD7LOQ7majlAjOhRPd2-I9emtpBxDoUXTLJ5YhBfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWidkawijRt53BvIRrpTJx3sDMdJXypxbxncWEN8RB070qlonCgMj7NmRnQslbbDWGGpR6H_6gzLQ_qwOaMYt-BQtYgMx3ykWoG6Wqik0HmI9rWt0VvG0DUsZ6TRYwDhnl9nE6XZBK7lntECFa-Eno2R09vF9dc-l8lhy8cbLstwuKDrOn35Ijs33U1WGXn4v4geFnC3tYOJgRovvqjWHSOuZ3eCCO4SudpNi8p1uCnxKwmgLWU8cgFdoxPl7uGjd39ByMhjOOcUvbq_JnAcUx974E-wOf-7vD-8a4GGdz9v2nhVZ4WEvfsZqz2Fa6OWZId9ua_a72PwWk2Jmb8Dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEtnS1yt2MEDNt5BvxawvstdqDGOR7lXwoFZjPduBo_8ejL95pxWVfA1Jb1MQhy63NztoCvc1i4HpZlso3Ml7koES9yoFP2r0lQcdclB1QSWoutokbYXVPoGIt9RBYmSPYLrtdqJy8cTBveeJA7S5bBv8Rxcg48pEE-N-LacUw5Uagvx_r-zah46LwxTrKd59dl7naokcXLYPHIiRgUMEXmTzeXyFmQagBn258AkzFqzq5NoZ_3ex36_gjLEbcYba4ftBWOg-fcOuvG0wZDW-ua3vKjMd6Dx_b_REl_u8s89zliXJieulkQu45ajwcVCJ5VJxshYU_H6rNYPY01g3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=J0lm1DyqCSp1k_14bG0zi3dniRbZKcn5CPIdpAHE-tq4N0GRWDfJClzs-5Vu5ZgaeRCKRi-MEvkyIuISyiOuI6-ukcV-_vrcNp039kOpp8KlJR3Ew9vA0o4Cw79sOY1aIHXXn9-iaLEywhY5ltUAB_ObioWVYZojfPs1klQNbfYI_dBf2wSh72WP1GdEMztrzWMmMjtXQU7_78St_aIbEL9KbXDAIexvbyfiCybq2CuYb9dIo8NI0J0YO39kGy87eGub6FHsMGIp2yzXxrM7zcdrccoCH3n1EI3MoJPEksxA3bbYBz6w37G2g3sT3c1dT7PF7KOgyUxhHXWcdT7O2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=J0lm1DyqCSp1k_14bG0zi3dniRbZKcn5CPIdpAHE-tq4N0GRWDfJClzs-5Vu5ZgaeRCKRi-MEvkyIuISyiOuI6-ukcV-_vrcNp039kOpp8KlJR3Ew9vA0o4Cw79sOY1aIHXXn9-iaLEywhY5ltUAB_ObioWVYZojfPs1klQNbfYI_dBf2wSh72WP1GdEMztrzWMmMjtXQU7_78St_aIbEL9KbXDAIexvbyfiCybq2CuYb9dIo8NI0J0YO39kGy87eGub6FHsMGIp2yzXxrM7zcdrccoCH3n1EI3MoJPEksxA3bbYBz6w37G2g3sT3c1dT7PF7KOgyUxhHXWcdT7O2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr1d-gV0g9CpP91Ji0KSgF0QtMo9p6IsYt7gKQjKBzk1rF6OTiA2Xsymfvpr5LGqXPhi2vQJcmVj8Mas_rjAfmY_ZEHVLsXlUM0EGIHCwmhQcVNvtphrv2suBXmfupfkmeP9GyuP9QrniWFxhMmZ5zSM_QtT1MT2o-uMUy77SjT7-zn21CsDpHAk0E7VZP07YlRckwsqTra2km064plH2VyLx4uuewkT8wWdwNehy840WyC2_k9ptZT8P7p7M4bkahTznZBfSUHVcziKyEZ1Q-yJqSXb_VzFd3X_fBwjAwy6hnoXFJNcHS9OHGa5SYO3hJWIlfzWDmu2WSoKF0iZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Wx_OMZcOpk5ckvzcQ6ZRDwhTk5mGrXyF758dwU3xYMz2RQT_4wCAEPDmqvmEw-yh49uvIYGLmkRkJFNN79G5FMlzeW4LiJEQRr5nMNMRcx3d_g4C7zq0gGEh1MRZlthXk2qI4gVCJTljAuob4Bts-DClLtEPSfqa5kuQcRNEe_h9qQ8oV54oGQBb3SufB0-qReqZl_7iO44VT8RLVgRvY7db38iCbi76ESDK_gnmr0g0iREbN8CG9yBtDjUg_xLFeuVFFbmneZ-WeuKYNYXcE65V9kz-1A68-lOTS60Pla7wF49Keq0mp2H-hShNyeMPyfYZU2RK1nd7_u5oEq7amA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Wx_OMZcOpk5ckvzcQ6ZRDwhTk5mGrXyF758dwU3xYMz2RQT_4wCAEPDmqvmEw-yh49uvIYGLmkRkJFNN79G5FMlzeW4LiJEQRr5nMNMRcx3d_g4C7zq0gGEh1MRZlthXk2qI4gVCJTljAuob4Bts-DClLtEPSfqa5kuQcRNEe_h9qQ8oV54oGQBb3SufB0-qReqZl_7iO44VT8RLVgRvY7db38iCbi76ESDK_gnmr0g0iREbN8CG9yBtDjUg_xLFeuVFFbmneZ-WeuKYNYXcE65V9kz-1A68-lOTS60Pla7wF49Keq0mp2H-hShNyeMPyfYZU2RK1nd7_u5oEq7amA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=mXwgRakuL4wRPr55iYEIIgLtNfKyFmhVuggixHdZkWHE6kSri46YAmCP4xPrkk61hpEYDq0sU6RhkPrOiFLVJcRQylId2gbGmvNMEgwMVEmR090SPXw0ryAxidzfCIn-ypcEyiRUG39o0EOM0l7qbSvZP-1LCCvINyIQw_vznSXf2nKlmN1xsJLmWkJaasnDw73g1U6Q0M1G7SKkqSRNSye-Wa8hw047fpetUru8GMJGhLTx_kYfjahJiFojPctonwr8hRPEuW_ByMhOlQcG_ifcaYT8G7rhV5dfZL01W4vUYKWU_ny2dpnN_UYbUAwt040NNfFama4qdXWQr-fJbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=mXwgRakuL4wRPr55iYEIIgLtNfKyFmhVuggixHdZkWHE6kSri46YAmCP4xPrkk61hpEYDq0sU6RhkPrOiFLVJcRQylId2gbGmvNMEgwMVEmR090SPXw0ryAxidzfCIn-ypcEyiRUG39o0EOM0l7qbSvZP-1LCCvINyIQw_vznSXf2nKlmN1xsJLmWkJaasnDw73g1U6Q0M1G7SKkqSRNSye-Wa8hw047fpetUru8GMJGhLTx_kYfjahJiFojPctonwr8hRPEuW_ByMhOlQcG_ifcaYT8G7rhV5dfZL01W4vUYKWU_ny2dpnN_UYbUAwt040NNfFama4qdXWQr-fJbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dackddLdtolxJnJPe0Z2IOcaMspHB4aG5E7xFy7eyqXv7MkftGOjDEd4QILS4HsQ9P8QjHPFtx4TxJf5AYmUW-KXuHkBqScI5Bse9XbPCUv7EFkgZkbGwqJS3pYka-ZzKsLWtwsG_nFwG0TYP-B_z5ia2JpsI5ZpEWPsKw9pk7kAmhHdhMPStTEooDO_wus8Um2JoEGSDkMebhjtZkoLOlENHHYykMRqsU4aFGVWT2zY-YTtPhkIFgK3RKd6m0Ibni9NgKbG-CIMa6WA7M7DIkQ_WAKE_izsE1_eLlMxYyMGzI_6ySyisW7m4lU1gGHM3R2Z1jsaV7BNk6kseSy9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r69nlKggGVPo8rgKbmn3zb_KF2KfHfdtL2yHz5gwHd_y1J6OmsxCZC67p_D2FqERaM35a4jKhlKdhr7qfJWuCFwbhvgek0Z57KtOe32mWLHv2zOv0C6IC5x-IWnAFwR-A_63Qjk2q5wIOYQ1Ylj-PgaieYXUW3_fLtP2TyRd-o6ZlHmpidWXG246V8ggK8knvDcde-oQxF_roeEGnnIT4xJHtXQ9g9Vs9dHtHXngEFJYrATA-So2sWwwSONp2OeEsjgv1Pa8NXYRu9p04JUa59Uu_QvPFNSLBw-Rdpzwek-KFPvD6HUuIzvpvpn1U5aWWbTnK24m2g108UGcoPtzSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1UtZ4Q7S6BeH3X3YeDTa7I7uRhpfpKrCeLzCa6OAwWuG28ZpfvhXR53lk_pLZ-9XzkpNFBNhHyWec2t4ldAn50dW2bEqyu5SkMalXRS0g9VJz-5-Bq02LXF5zyot_xV4rH4dLVt8klwIZ7bISNs_KZOjoGBhOHRIlq0pUsklsxle5hfaeWwajH7HNIodlb0NuU83DV2fVJI9MZ2aU4AI5jWE3mS1AuEK5BeiXy9QeQGSovVk_-aDSkDp0O5Ud_CJNLqD_ppbZ2B2546A0jOoE4z9050odXcId5BKUX3Lj18CP4eoPL7Z_lHs1Sjv6gYP3LCSinckm5MFw56Pue4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
