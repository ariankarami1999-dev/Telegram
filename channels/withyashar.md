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
<img src="https://cdn4.telesco.pe/file/mPl0kQ16Bnyj5Apm836lPyQyevfRa6TWgj8LUv8Y9V_YitnM2dalUzP8xzRqXkghJQ-pyClY7kZTXau95oHlGBt8iyHVTEy7UBzgPOlxT5Jvwp4ZLV7E2av6mU6DmKtTQlWid2aVqPGezFXN_dyogdvgNbuFVK652XTO554vD4ARXwRkNY4tSJRn5bZ3exmQVKOsCBzzExJIK9Jc1Q4eI27jRsT9AzjYe0kt7ajr_suNL26sNcJ8pCfJ7gYvzgY9UF9BcvOd4KYXqTq0a5KzPeNpeC7CvuTdxTqRKBP-1VKHKU1Gi-Mf7rJC-BL7MXPhprGSmbpTjLl6UURtr5qsaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/withyashar/24788" target="_blank">📅 23:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/24787" target="_blank">📅 22:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/24786" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گویا معین هم اعلام کرد بر میگرده بزودی @WarRoom</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/24785" target="_blank">📅 22:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارت خارجه بریتانیا: آمریکا، انگلیس، فرانسه و آلمان در بیانیه‌ای مشترک اعلام میکنند که متعهد به جلوگیری از تأمین هرگونه مواد، تجهیزات و فناوری برای ایران هستند که بتواند در فعالیت‌های هسته‌ای مورد استفاده قرار گیرد. این چهار کشور همچنین بر ضرورت همکاری کامل ایران با آژانس بین‌المللی انرژی اتمی و اجرای تعهدات پادمانی تأکید کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/24784" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آکسیوس به قلم باراک راوید:
چرا واشنگتن و تهران مدام حرف یکدیگر را نمی‌فهمند؟آمریکا و ایران هر دو می‌گویند راه‌حل دیپلماتیک را به جنگ ترجیح می‌دهند، اما رسیدن به توافق از همیشه دشوارتر شده است. ریشه اختلافات در چهار موضوع است: واشنگتن توافقی سریع و بزرگ می‌خواهد، در حالی که تهران مذاکره طولانی‌تر و توافق‌های محدودتر را ترجیح می‌دهد؛ بی‌اعتمادی عمیقی میان دو طرف وجود دارد و هرکدام نگرانند طرف مقابل از مذاکرات برای آماده‌سازی اقدام بعدی استفاده کند؛ فشارهای سیاسی داخلی در آمریکا و ایران نیز مواضع دو طرف را سخت‌تر کرده است. در ۱۸ ماه گذشته، دو دور مذاکرات شکست خورده و هر دو بار پس از شکست مذاکرات، درگیری نظامی شدت گرفته است. اگر تلاش فعلی هم به بن‌بست برسد، خطر آغاز دور تازه‌ای از جنگ طی چند هفته وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/24783" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏امیر قاسمی و رو‌کردن نام کسانی که با سپاه در ارتباط کامل قرار دارند ، آیا نفر بعدی که در ایران خواهید دید معین است؟ گزارشهایی هم هست که در کنسرت اخیر معین اجازه ورود پرچم شیر و خورشید داده نشد و فقط آهنگی برای ایران خوانده شد و در نمایشگر هم پرچمی نمایش داده…</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/24782" target="_blank">📅 22:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0950d9a5.mp4?token=mM6Lv26VsY7xI4JGiD3Xwj9LoXOTzOlAPOq1uk_In_d8C__OOcvwYGHV-D8ywR1qQcRtj0geP1QOqdRblKZ0pUYkY17wlMS5wNgUQFUz4AADG30FSX6Vx-SvJDUIgNdymnr3xhnThfSHbGdl2dI-YK4ao-_jmrXRI-ZljqCbbINhEBJ4m3JIXlxi4A6PqYOgcAa__tDaZ3RTmN7u4Ml5JTu0LkH6qCtSSTzCnBwVUvqd78fRGFAzUmymDgLQBetINzNn97VSeJeBlkOmmN365OLocSLpW7P_D-ERjEHS59k844C1oSoJStdWKAJUwoQDw7mgY1Bv5P1jZlxgW9sDtF_N4gjo82JyyL7rfcmXoDTFANZQZ6HNjsMPtvOX2qYjX0kY6A37uddIyS3mRPU1UmqQTyK7X475VsNSbafpL_rcw7BI1KcD2fJvRZ0cQKn4Jgi5dofXPBjY81B3HlM5z1rdaAED2x8uRwPs8_lQyT44b6hVqJCSxHA_GNRGuVIAr0LPZinw_8ZQG0ZsNCIF9m-2QbSvlw98CpwAN0p0jP_QMIeQ-PlKt3XXZM2DF7fVBcdRky_pJzR4XDOf_2ltNRwEkSy-W5hpueoSJOdESQ88qx3LP9hqtk0YrDt-j6-0EoaaAF6zOnUfPUCy15Xm2_MN2baDEBl1AH31sd7Q2y4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0950d9a5.mp4?token=mM6Lv26VsY7xI4JGiD3Xwj9LoXOTzOlAPOq1uk_In_d8C__OOcvwYGHV-D8ywR1qQcRtj0geP1QOqdRblKZ0pUYkY17wlMS5wNgUQFUz4AADG30FSX6Vx-SvJDUIgNdymnr3xhnThfSHbGdl2dI-YK4ao-_jmrXRI-ZljqCbbINhEBJ4m3JIXlxi4A6PqYOgcAa__tDaZ3RTmN7u4Ml5JTu0LkH6qCtSSTzCnBwVUvqd78fRGFAzUmymDgLQBetINzNn97VSeJeBlkOmmN365OLocSLpW7P_D-ERjEHS59k844C1oSoJStdWKAJUwoQDw7mgY1Bv5P1jZlxgW9sDtF_N4gjo82JyyL7rfcmXoDTFANZQZ6HNjsMPtvOX2qYjX0kY6A37uddIyS3mRPU1UmqQTyK7X475VsNSbafpL_rcw7BI1KcD2fJvRZ0cQKn4Jgi5dofXPBjY81B3HlM5z1rdaAED2x8uRwPs8_lQyT44b6hVqJCSxHA_GNRGuVIAr0LPZinw_8ZQG0ZsNCIF9m-2QbSvlw98CpwAN0p0jP_QMIeQ-PlKt3XXZM2DF7fVBcdRky_pJzR4XDOf_2ltNRwEkSy-W5hpueoSJOdESQ88qx3LP9hqtk0YrDt-j6-0EoaaAF6zOnUfPUCy15Xm2_MN2baDEBl1AH31sd7Q2y4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترابری سنگین نظامی آمریکا از ۲۴ ساعت پیش تا دقایقی قبل…
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/24781" target="_blank">📅 21:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رئیس انجمن صنفی تولیدکنندگان شیرآلات: اگر محاصره دو ماه دیگر ادامه پیدا کند کل کارخانه‌های شیرآلات تعطیل خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/24780" target="_blank">📅 21:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رویترز: عربستان در حال آماده‌سازی برای آغاز حمله‌ای جدید علیه حوثی‌ها در یمن طی هفته‌های آینده است؛ هدف این حمله بازپس‌گیری کنترل تنگه باب‌المندب و تأمین امنیت کشتیرانی در دریای سرخ است که با حمایت اطلاعاتی آمریکا همراه خواهد بود @WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/24779" target="_blank">📅 21:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR-cmAABu8RaWzIHDxE6OA37mOSJMTKcE7TlAMJc-WCNkJ3-qWNIAFJsvNUI69d_PAgSo9ltIP-BTL_CosilqNQTj_qXbCUlTv6KO4_GcjH4ypG1PoBL0gRl2BevoTTDfKgGAdFnvis7de_s_x2q-F2n9g-nEvoLWUk9psKS7qAeWj4HgK2A9pOMWFgoBBb_wF2bi1DJprpCzn8CBjI5VrFQSrBtqqrAoZOcxDwZZTB8_8UxswvBuRA9ZSKpCZaxtwpwl2TrLyyPagcGE7MX5JIVGGoY3wIClQHicM27fRV3TLIS7Zoo2Kevhfc4fNDNSC6YM233Y_CWOkWk81yPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ پی-۸ پوسایدون ، ۵ سوخترسان ، ۱ هرکولس و ۳ هواپیمای ترابری سنگین سی۱۷ هم اکنون در محدوده خلیج فارس و همچنین سوخترسانی هم از اسرائیل به سمنت منطقه می آید
@WarRoom</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/24778" target="_blank">📅 21:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز: عربستان در حال آماده‌سازی برای آغاز حمله‌ای جدید علیه حوثی‌ها در یمن طی هفته‌های آینده است؛ هدف این حمله بازپس‌گیری کنترل تنگه باب‌المندب و تأمین امنیت کشتیرانی در دریای سرخ است که با حمایت اطلاعاتی آمریکا همراه خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/24777" target="_blank">📅 20:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGvKzbuv5wupcbY2y__S4Q7N9mY5X13gErYvf76umDFtOHQcCa3rCCoTw9XAl71NFoL2h18f6kI_PB5K_ppO-tEbkJE7O4ruwy21P2By7YbT2H9cAdaG64b-uG5jTBeqoy-lAvmLe52TEwS9PKw8eWPNDodFVEFmzLeqGMJFBL7xI8Wmduz66ZoLg54iaZgmd3RSFCLPnch4Z1z58ag3RnHmDTvOHth-l2x-fochqqqymj2jvbJ-V14ixga-KK8YUeG6iMpWP4b0_XbXF2PtpG7Pn5q6yTSsOoQ9GbnutHGXRZjlvF8isPd2v7IA05ZjhFHd2a0rN7cycgk_PMsqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان نظارت دریایی بریتانیا اعلام کرد که ناخدای یک تانکر نفتی گزارش داده است که این کشتی در حین عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
یک آتش‌سوزی کوچک و قطعی برق به طور موقت رخ داد، اما آتش‌سوزی خاموش شده و کشتی در حال حرکت است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24776" target="_blank">📅 20:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کوین‌دسک:
سیتی‌گروپ هدف ۱۲ماهه بیت‌کوین را به ۱۱۳ هزار دلار و هدف اتریوم را به ۳٬۰۲۸ دلار افزایش داده است.
این اهداف، پیش‌بینی بانک هستند و قیمت تضمین‌شده محسوب نمی‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24775" target="_blank">📅 18:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c6ae3f3.mp4?token=VMgCTFDPxCySVF9gWhlTl9T0etAGnNWzmouB_vXGBfZYtZZc6nmLtU1Y3rG3lyYuK1Q9rKEaQY4yjecJJeDrVa8OCANHs_IgRJXOm9PrJ8STXollPHH1BvYEm2PvZDxaDRbRIWkVz-Z1OCEHxLDbU7uPIno2-UXrDVH8zYLFe_kf3Y9kJKAm_w5kQPsdHc_m0J_whPSvZUmZm1P5hbsJSsSsm1Y2WV6lP7PnB0ykZHpuNHQeprafxKCV1aqv6O8tNXUtUF9BeOvINzF5v-6NVxtMYE6XdJVYYdigJWlhWf4m9J8IZz3DRYAtaADtxT_4eSapz1Rp5Mqih8Bd567-4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c6ae3f3.mp4?token=VMgCTFDPxCySVF9gWhlTl9T0etAGnNWzmouB_vXGBfZYtZZc6nmLtU1Y3rG3lyYuK1Q9rKEaQY4yjecJJeDrVa8OCANHs_IgRJXOm9PrJ8STXollPHH1BvYEm2PvZDxaDRbRIWkVz-Z1OCEHxLDbU7uPIno2-UXrDVH8zYLFe_kf3Y9kJKAm_w5kQPsdHc_m0J_whPSvZUmZm1P5hbsJSsSsm1Y2WV6lP7PnB0ykZHpuNHQeprafxKCV1aqv6O8tNXUtUF9BeOvINzF5v-6NVxtMYE6XdJVYYdigJWlhWf4m9J8IZz3DRYAtaADtxT_4eSapz1Rp5Mqih8Bd567-4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الکس پیلیتساس
(
تحلیل‌گر امنیت ملی آمریکا، کارشناس ضدتروریسم و افسر سابق پنتاگون
) در سی‌ان‌ان بخوبی استراتژی جمهوری اسلامی رو توضیح میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24774" target="_blank">📅 18:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye7tUR5RATcocHNlsPPwQohkunab7oQEn5qFUpivxBo57p9pOeiXdHcRkUeymKG39voOksb0CRewuN4dqiq9uUudvlzAavZjsn9fdqkPOQXScx7B0izhhTO1VJ9PEZm1CgzfzeZIzvIhHrhRPtAgFagAFtEpzyNPRxbtYE28ClW3TKfUcj9w7JpFMhOSVdcluifkThuOCoIsyqV7wGPzUAULOuWA9-kKg94ABLuJnIRLEXaHRSqJ5_0_kTdL8_bWl6Ne1wn7uEOylDEGbL3FJZMadpgvkEtStOGHhaT43oTFNsT2liHcDzTNDQ3T45aNm5us4jQsfW6YnIyLQHP1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الناز شاکردوست به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس و دو سال محرومیت محکوم شده است. وکیل او گفته این حکم صرفاً به دلیل انتشار یک استوری پس از حوادث دی‌ماه سال گذشته صادر شده و محتوای آن تنها بیان اندوه بابت جان‌باختن جوانان ایران بوده است. به گفته وکیل شاکردوست، در این نوشته هیچ اشاره‌ای به نظام، حکومت یا مسئولان و همچنین هیچ فراخوانی برای اقدام جمعی، فعالیت سازمان‌یافته یا براندازی وجود نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24773" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b731ebb6ee.mp4?token=R6u_w6rAPkQoFiXIgFJvLLdJPOf6PATWSZRQ3jkw_qMB2ObFc3Mr-WNWA2egCP0ktFTOcD4eyMR9O02Ztsc1PeAdqrwhGEd6722BhRqH2jYPYVtp_s7veI86obMVPP8-l0CxS8u3USLXvoHKVdzuLjhwRFjTcQUbkIqCVkdzgEnySiGIxrmTQ9FHMcBWaJwlsR5c-L4Gf7cpwuLVvm3pCzSRa3xHFgcLrP_QbdbdUTDC7-99baSI0eHNi2un2MY0vowzeP5LusXYjNGirp941j5ImA5LeInfzEhDhRlUMiZ0IbbbT8t1KOnZJARn8LdaQW9IH-zwShvQneXct04L50VLc3A2sM2x_BlgJLMKg9RsMyKVtQJAXhJA5Rpd_7ScLUMfDh4QQJuk5FlO2nUEfXMBwqOxZ7YXet2wNBohzdx6jWrRcrosgFIvnIK6rI-x3T404AxrqI6O4s2v7XaWgvNayIp4yq5BDl1vsYh2hPVwu16yEK_qDYF64QiXg1oEO_A3treyUcippRAUw-3KCgFx71v9PFih82fvI6T4J3qKNDzx89fmNsnci6u4zvAe0TTiXoIi0D-jAfhuE3-U2jmN585JS7txH5FlYgK398R-tNlj2MNeRVrCw90_OjsjmKWBWqlaq4O-2FCXXS0-4E4eXyssRcGmxOgTlAzebZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b731ebb6ee.mp4?token=R6u_w6rAPkQoFiXIgFJvLLdJPOf6PATWSZRQ3jkw_qMB2ObFc3Mr-WNWA2egCP0ktFTOcD4eyMR9O02Ztsc1PeAdqrwhGEd6722BhRqH2jYPYVtp_s7veI86obMVPP8-l0CxS8u3USLXvoHKVdzuLjhwRFjTcQUbkIqCVkdzgEnySiGIxrmTQ9FHMcBWaJwlsR5c-L4Gf7cpwuLVvm3pCzSRa3xHFgcLrP_QbdbdUTDC7-99baSI0eHNi2un2MY0vowzeP5LusXYjNGirp941j5ImA5LeInfzEhDhRlUMiZ0IbbbT8t1KOnZJARn8LdaQW9IH-zwShvQneXct04L50VLc3A2sM2x_BlgJLMKg9RsMyKVtQJAXhJA5Rpd_7ScLUMfDh4QQJuk5FlO2nUEfXMBwqOxZ7YXet2wNBohzdx6jWrRcrosgFIvnIK6rI-x3T404AxrqI6O4s2v7XaWgvNayIp4yq5BDl1vsYh2hPVwu16yEK_qDYF64QiXg1oEO_A3treyUcippRAUw-3KCgFx71v9PFih82fvI6T4J3qKNDzx89fmNsnci6u4zvAe0TTiXoIi0D-jAfhuE3-U2jmN585JS7txH5FlYgK398R-tNlj2MNeRVrCw90_OjsjmKWBWqlaq4O-2FCXXS0-4E4eXyssRcGmxOgTlAzebZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مرد فرهیخته ، ژنرال جک کین : مبارزان ایرانی در گروه‌های متعددی سازماندهی شدند و میخواهند مسلح شوند تا کشورشان را پس بگیرند ، هم مسلح کردن ایرانی‌ها لازم هست هم اقدام نظامی شدید در لحظه مناسب بخصوص بعد از فروپاشی اقتصادی
گزینه توافق و دیپلماسی کاملا کنسل است
‏این رژیم باید سرنگون شود..
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24772" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ در‌تروث : «اروپا به‌تازگی با آزادسازی حجم عظیمی از ذخایر بسیار زیاد دیزل خود موافقت کرده است. این روند بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24771" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شبکه 14 اسرائیل: ما رهبر ایران رو وسط تهران کشتیم و هزینه خاصی هم پرداخت نکردیم. اون مرکز رنج ما بود.  ما فکر میکردیم ایران کار دیوانه واری انجام بده ولی فقط 40 روز جنگید و بعدشم به توقف جنگ رضایت داد. دو دهه الکی ترسیده بودیم.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24770" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: مأموران سرویس مخفی به من گفتند به‌دلیل بدی آب‌وهوا احتمالاً باید سفر به اوکلاهما را لغو کنیم؛ نه هلیکوپتر می‌توانست پرواز کند و نه هواپیما. گفتند تنها راه، یک رانندگی طولانی است. از آنها پرسیدم «بیست با چه سرعتی می‌تواند حرکت کند؟» گفتند نزدیک به ۱۰۰ مایل بر ساعت.
گفتم: «پس سریع باسن تپلتون رو بزارین تو ماشین و راه بیفتید!»
این سفر آسانی نبود، اما نمی‌خواستم مردمی را که ساعت‌ها برای دیدنم در اوکلاهما منتظر مانده بودند، ناامید کنم.
@WarRoom
👏</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24769" target="_blank">📅 17:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4d8b2843.mp4?token=cXrBIdbRl0gE0fWw-MQEPq763JHFLig-_4I55Qy57AdCLB3aiLOlFhymdSmcezZVmyHHBsefdHEI6lCe2j1Yft8IYRZvs2v3dWhwTzuotWBalkW3ndmjSEemPz4WOvnb9z0RoNZsVbCdym2MhxOCzTzwvvheY-1S8VNlv5DKC0z-KRM8dSvERz48JmyD2S33HS9q32fo9JYIw9zphIMFRZ63STMJr-2d5MTJrVJhE3jWKL6-kXQlLLapi9cXtiAB-B3Ijp6txvXKtWQQ1co2ScJo4ZzZxhODLPpz2Nrzdh69t0JmdkgNH2X5M5brhE2h8TXJpW6xa3YZs8R1jBISPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4d8b2843.mp4?token=cXrBIdbRl0gE0fWw-MQEPq763JHFLig-_4I55Qy57AdCLB3aiLOlFhymdSmcezZVmyHHBsefdHEI6lCe2j1Yft8IYRZvs2v3dWhwTzuotWBalkW3ndmjSEemPz4WOvnb9z0RoNZsVbCdym2MhxOCzTzwvvheY-1S8VNlv5DKC0z-KRM8dSvERz48JmyD2S33HS9q32fo9JYIw9zphIMFRZ63STMJr-2d5MTJrVJhE3jWKL6-kXQlLLapi9cXtiAB-B3Ijp6txvXKtWQQ1co2ScJo4ZzZxhODLPpz2Nrzdh69t0JmdkgNH2X5M5brhE2h8TXJpW6xa3YZs8R1jBISPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
«هر چه زمان می‌گذرد، تصویر واضح‌تر می‌شود. این عمل، نتیجه‌ی افراط‌گرایی اسلامی بود و هدف آن، سرنگون کردن هواپیما به همراه تمام مسافرانش بود.ما در حال بررسی این موضوع هستیم که آیا این فرد برای انجام این کار اعزام شده بود یا خیر، و هر کسی که مسئول این اقدام باشد، باید پاسخگوی عواقب بسیار سنگینی باشد.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24768" target="_blank">📅 17:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فرمانده انتظامی رشت اعلام کرد یک روحانی در یکی از محله‌های این شهر توسط فردی ناشناس با سلاح سرد مجروح شده است. به گفته سرهنگ عیسی روشن‌قلب، پلیس در جریان تحقیقات به سرنخ‌های مهمی درباره ضارب دست یافته و تیم‌های تخصصی با هماهنگی مقام قضایی برای دستگیری او تلاش می‌کنند. وضعیت فرد مجروح مساعد اعلام شده و پلیس گفته علت و انگیزه حمله پس از دستگیری متهم و تکمیل تحقیقات مشخص خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24767" target="_blank">📅 17:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رعد ‌و برق در تهران ، نترسید
@WarRoom
🫂</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24766" target="_blank">📅 16:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ در ‌تروث: «با خوشحالی اعلام می‌کنم توافق با کره جنوبی هر روز بهتر می‌شود! ۸.۴ میلیارد دلار برای یک پروژه افزایش برداشت نفت اختصاص داده شده است. تولید بیشتر نفت و گاز یعنی تقویت سلطه انرژی آمریکا و تضمین امنیت انرژی در جهان برای آینده.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24765" target="_blank">📅 16:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو: ترامپ از من پرسید «این قدرت را از کجا می‌آوری؟» به او گفتم: «این قدرت، میراث پدران ماست که از پدران به پسران و نسل‌های آینده منتقل شده است.» @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24764" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c997284691.mp4?token=Wa8HU30BVJDiiorl5ShpC40RTMbACYDyaVGHN5dMp6ZBk72I2nHyC74s5ZLMoGQwrADZfv9VuNey-L-OA1ZjFOyxptRLr7ZmIoAwhKX80T4Nq3B0dvqDO1zMgyRyp4gbJi4KVk-ptqHcQTAwix7-HdY3ScpfFgrzQqtze4SY4iiOht-4rYUcx2fPVoSlFEKwwpO1g6ds9hErpju9NRPJMtwgMXZ5kUfRD2GFRTc_b7KeXaA1P78jQ8Ro3xh5-Y_6KNIO-HCOh5hoY2mc-gkVh2xD2ctN_v4tX_o0x5Grpca_uSkRseEYkEFVgD3oORwa--V9L6xENnSpJSfzeX2N5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c997284691.mp4?token=Wa8HU30BVJDiiorl5ShpC40RTMbACYDyaVGHN5dMp6ZBk72I2nHyC74s5ZLMoGQwrADZfv9VuNey-L-OA1ZjFOyxptRLr7ZmIoAwhKX80T4Nq3B0dvqDO1zMgyRyp4gbJi4KVk-ptqHcQTAwix7-HdY3ScpfFgrzQqtze4SY4iiOht-4rYUcx2fPVoSlFEKwwpO1g6ds9hErpju9NRPJMtwgMXZ5kUfRD2GFRTc_b7KeXaA1P78jQ8Ro3xh5-Y_6KNIO-HCOh5hoY2mc-gkVh2xD2ctN_v4tX_o0x5Grpca_uSkRseEYkEFVgD3oORwa--V9L6xENnSpJSfzeX2N5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: ترامپ از من پرسید «این قدرت را از کجا می‌آوری؟» به او گفتم: «این قدرت، میراث پدران ماست که از پدران به پسران و نسل‌های آینده منتقل شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24763" target="_blank">📅 16:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تتر ۲۶۳،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24762" target="_blank">📅 15:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24761" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41835d5d95.mp4?token=q6slaoe557jhrPX8ODEvU15nxDJBZvdTOWAYEPB_yPF1GvKCILtJgVezq0L4GR_WoC2qOxLj2Nr88l4iu18FAa2mjzt0LZ7xADlylL1yoXEMLxpN4ws5JH8uWe4oliTFQR5TT6hQr_6cRB--sDdwAYCwSeuHHz8hSTOw0d-Zf7GK3a9nUY3uWVAk-XubJZDK-RKlYKzoFDlCFwhVmnARx_6q7PFi9_OFMEF8Mv0X4iXjo_yXnKt0FLLRK3bDy7LERt91CMwemflkugSgRMulxGbwFzOyQ2l5NWAqO-VwBp0r5EUdpA6ghZ2PuvFULxjO4Q0zTZvBh81wmFQbrBQfeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41835d5d95.mp4?token=q6slaoe557jhrPX8ODEvU15nxDJBZvdTOWAYEPB_yPF1GvKCILtJgVezq0L4GR_WoC2qOxLj2Nr88l4iu18FAa2mjzt0LZ7xADlylL1yoXEMLxpN4ws5JH8uWe4oliTFQR5TT6hQr_6cRB--sDdwAYCwSeuHHz8hSTOw0d-Zf7GK3a9nUY3uWVAk-XubJZDK-RKlYKzoFDlCFwhVmnARx_6q7PFi9_OFMEF8Mv0X4iXjo_yXnKt0FLLRK3bDy7LERt91CMwemflkugSgRMulxGbwFzOyQ2l5NWAqO-VwBp0r5EUdpA6ghZ2PuvFULxjO4Q0zTZvBh81wmFQbrBQfeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : دیگ به دیگ میگه باسن تو سیاهه
قیصر فرندلی فایر بیژنو میزنه
😂
این قشنگه
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24760" target="_blank">📅 15:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حقیقت یاب
اتاق جنگ:
خبری که با عنوان «ارتش آمریکا رسماً تمرین تصرف و پاکسازی تأسیسات هسته‌ای زیرزمینی را انجام داد» در حال انتشار است،
خبر جدیدی نیست
و مربوط به ژوئن ۲۰۲۴ است. ارتش آمریکا اعلام کرده بود تیم «خنثی‌سازی هسته‌ای ۱» همراه با نیروهای
هنگ ۷۵ رنجر
در یک تمرین نظامی، یک تأسیسات هسته‌ای زیرزمینی شبیه‌سازی‌شده را در شرایط آتش شبیه‌سازی‌شده تصرف و پاکسازی کرده‌اند. این تمرین با هدف افزایش آمادگی برای شناسایی، ایمن‌سازی و خنثی‌سازی تهدیدهای هسته‌ای و پرتوی انجام شده بود. بنابراین انتشار دوباره این گزارش به‌عنوان یک
تحرک یا تمرین جدید آمریکا
نادرست است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24759" target="_blank">📅 15:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مرد خردمند ، مارک لوین : این جنگ هیچ‌وقت درباره تنگه هرمز نبوده؛ اگرچه حفظ جریان نفت دستاورد بزرگی است. فشار اقتصادی علیه جمهوری اسلامی بسیار موفق بوده و همچنین سایت‌های هسته‌ای و اورانیوم غنی‌شده دفن شده اند. اما تنها راه جلوگیری از دستیابی ایران به سلاح هسته‌ای، با داشتن هزاران موشک بالستیک و ادامه حمایتش از تروریسم، نابودی این رژیم است. هیچ راه خروج خوبی وجود ندارد. من همچنان خواستار
مسلح کردن
مردم ایران و
ارائه آموزش، پشتیبانی فنی و پوشش هوایی
مورد نیاز آن هستم. ما پیش از این در کشورهای دیگر چنین کاری کرده‌ایم و با توجه به ضربات واردشده به ایران، به‌ویژه فروپاشی اقتصادی، معتقدم زمان اقدام اکنون است یا دست‌کم به‌زودی فرا می‌رسد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24758" target="_blank">📅 14:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فایننشال تایمز: ترامپ در فکر حمله آخرالزمانی‌به ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24756" target="_blank">📅 14:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الجزیره  : بر اساس برنامه فعلی، نهایتاً تا پایان نوامبر ( هفته اول آذر ) آمریکا می‌تواند ۳ ناو هواپیمابر و ۲ گروه آبی‌خاکی در اطراف ایران داشته باشد.      البته خبرگزاری آسوشیتدپرس نظرش اواخر اکتبر (هفته اول آبان)است @WarRoom
⚠️
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24755" target="_blank">📅 13:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جزئیات جدیدی از دولت
ترامپ
در گزارش مجله تایم :
گروک، چت‌بات هوش مصنوعی شرکت X
، تا حدی در متقاعد کردن ترامپ برای این دیدگاه نقش داشته که
ربودن نیکلاس مادورو، رئیس‌جمهور ونزوئلا، می‌تواند میراث سیاسی او را تثبیت کند
.
در بخشی دیگر تایم گفت ، ترامپ از سوی مقام‌های ارشد مستقیماً در جریان
مشکلات مربوط به ذخایر مهمات آمریکا
قرار نگرفته و این موضوع را از طریق گزارشی در
نیویورک‌تایمز
متوجه شده است. ترامپ سپس با
پیت هگست
، وزیر جنگ آمریکا، درباره این موضوع بحث کرد و هگست او را متقاعد کرد که این گزارش‌ها
«اخبار جعلی»
هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24754" target="_blank">📅 13:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در‌ انتظار تایید : قرائتی ، ورّاج صدا و سیما ، ریق رحمت را سر کشید
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24753" target="_blank">📅 13:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVM5xMtODKH8SlT8sq6cBKUPkMg_NWMTYmq0LdI1nCPdQg5XSDF9DHTeCticmaLnAWQ1OLUvIpH8wzRSQnYwVk9sV7OdxqPGJc4JLyRjOaXsXLMFlENkS4__pWr0TR5uvPZpZxOCN09wKmA0Gxr_8O5F6CS06j8-zYU-BZKXkwDYECBJhUhHO2BIOCjjR__RVysd-OJHAylCG4uzqIAE7vWa4R0-r_01X72GOAAZnKfJFAesIk3qr8yzdW_44S5sgNkfOWs-NHR9y7f3yi0m6_7i9A5Yw6Tou928sWu9WVoQBTFoIWVQ7z6FTZNVTlyDtq2BJYlwIrWda7CN-L0dHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلامیه خواهر عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24752" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بیژن مرتضوی: در جانفدا ثبت نام کردم
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24751" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ:
اینا آدم‌های دیوانه‌ای هستند، که ۵۰ ساله  است فریاد می‌زنند «مرگ بر آمریکا».
جنگ با جمهوری اسلامی خیلی زود تمام می‌شود. ایران با تورم ۳۱۲ درصدی و سقوط ارزش پول روبه‌رو شده است، بخش بزرگی از رهبرانش هم دیگر نیستند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24750" target="_blank">📅 13:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الجزیره:
مایک والتز، سفیر آمریکا در سازمان ملل، گفت ایران همچنان اورانیوم را تا سطح ۶۰ درصد غنی‌سازی می‌کند
و حاضر نیست از جاه‌طلبی‌های هسته‌ای خود دست بکشد. والتز همچنین ایران را به نقض قوانین بین‌المللی و محدود کردن دسترسی بازرسان آژانس بین‌المللی انرژی اتمی متهم کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24749" target="_blank">📅 13:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پولیتیکو:
فرانسه و ترکیه بر سر توافق‌های جدید همکاری ناتو با آذربایجان و ارمنستان به بن‌بست رسیده‌اند.
فرانسه با توافق همکاری با آذربایجان مخالفت کرده و ترکیه در واکنش خواستار تصویب هم‌زمان توافق همکاری با ارمنستان شده است. این توافق‌ها شامل
رزمایش و آموزش نظامی و تقویت همکاری سیاسی و دفاعی
است و بیش از یک سال در ناتو بلاتکلیف مانده‌اند. دیپلمات‌های ناتو هشدار داده‌اند این بن‌بست می‌تواند روند نزدیک‌شدن ارمنستان و آذربایجان به غرب را دشوارتر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24748" target="_blank">📅 13:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الجزیره  : بر اساس برنامه فعلی، نهایتاً تا پایان نوامبر ( هفته اول آذر ) آمریکا می‌تواند ۳ ناو هواپیمابر و ۲ گروه آبی‌خاکی در اطراف ایران داشته باشد.
البته خبرگزاری آسوشیتدپرس نظرش اواخر اکتبر (هفته اول آبان)است
@WarRoom
⚠️
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24747" target="_blank">📅 12:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رویترز: عبور محموله‌های ال‌ان‌جی از تنگه هرمز در سپتامبر به بالاترین میزان از آغاز جنگ رسید. بر اساس داده‌های S&P Global، ۱۹ محموله شامل ۱۳ محموله از قطر و ۶ محموله از امارات از تنگه عبور کردند؛ داده‌های کپلر این رقم را ۲۱ محموله اعلام کرده است. با این حال،…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24746" target="_blank">📅 12:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز:
عبور محموله‌های ال‌ان‌جی از تنگه هرمز در سپتامبر به بالاترین میزان از آغاز جنگ رسید.
بر اساس داده‌های S&P Global، ۱۹ محموله شامل ۱۳ محموله از قطر و ۶ محموله از امارات از تنگه عبور کردند؛ داده‌های کپلر این رقم را ۲۱ محموله اعلام کرده است. با این حال، برخی کشتی‌های قطری برای عبور از منطقه، سامانه ردیابی خودکار خود را خاموش کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24745" target="_blank">📅 12:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">درگیری مسلحانه میان نیروهای امنیتی رژیم و یک گروه مهاجم در یکی از روستاهای شهرستان راسک در جنوب سیستان‌وبلوچستان رخ داده است. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24744" target="_blank">📅 12:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">درگیری مسلحانه میان نیروهای امنیتی رژیم
و یک گروه مهاجم در یکی از روستاهای شهرستان راسک در جنوب سیستان‌وبلوچستان رخ داده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24743" target="_blank">📅 12:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57b1f32b3.mp4?token=h24vERQl7W8o6uVhCuOnCceYDsKHKzWQdsPcoxNvbgXZxYOjbwur4yY7xtdAL_eW5D28czKPqlD-IKoK-idvcxeiEoiRm0KUw6SmANZoc1HCpdUyK-FyQnkgkHaon9nHUdna-nQaFtM2MyJMolifEQxKa4RMJi6roaF9ocX41fCumPCknhhmlY5bKwGghrWUFCRF1iYSzVWshkqm7K3-D-7qjrbZpmjNSGqLzHQXs-IZR8xIHTNN22KX5SEliwK2_W8NhCIRbHTsP45l83tZeFxIG7HfqNi_OrUTs-gfZilfCDXsmGtBOUf_6nrPJClP9xFxJvl1q1K2OYHFEV1W-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57b1f32b3.mp4?token=h24vERQl7W8o6uVhCuOnCceYDsKHKzWQdsPcoxNvbgXZxYOjbwur4yY7xtdAL_eW5D28czKPqlD-IKoK-idvcxeiEoiRm0KUw6SmANZoc1HCpdUyK-FyQnkgkHaon9nHUdna-nQaFtM2MyJMolifEQxKa4RMJi6roaF9ocX41fCumPCknhhmlY5bKwGghrWUFCRF1iYSzVWshkqm7K3-D-7qjrbZpmjNSGqLzHQXs-IZR8xIHTNN22KX5SEliwK2_W8NhCIRbHTsP45l83tZeFxIG7HfqNi_OrUTs-gfZilfCDXsmGtBOUf_6nrPJClP9xFxJvl1q1K2OYHFEV1W-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت‌وگذار یک دانشجوی عراقی با خودروی آمریکایی دوج چارجر در همدان، در حالی که تصویر تروریستها؛ علی خامنه‌ای، قاسم سلیمانی و ابومهدی المهندس (جمال جعفر محمدعلی آل‌ابراهیم، معاون پیشین حشدالشعبی عراق) روی بدنه آن نقش بسته است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24742" target="_blank">📅 11:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd60bc703d.mp4?token=PzB_4jDcGlSF2k7S7howBAohAjO6QEdLDnfo43UybFLAxpBPQIBMf9s1P8TAnUNd0GGx0OxMVODF34L-D8b58z-XmaWzezdsj-PecM4AiUdKl0nWCTCSP0SuuLzvrrF2eulZLjXMKr45_KtdOom2Yi-7hF9-LVFB8tvyKHknfuZ_9VGK4qjDzn9DFV6uuy9ZiR6mChrzr0YDHfofy48l-pZyAOGTVpWcbwMAUR4nPrsZkRCeizpLVa9q2y-0JCgkzuhbz5-b9qkMlf9LGEUv3iM1m-Vn42EyT2JW4z5l91kETQ3UI3Ci-ns6k0v7j7a6ecLJPWGSQQBRsgBDtmKcUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd60bc703d.mp4?token=PzB_4jDcGlSF2k7S7howBAohAjO6QEdLDnfo43UybFLAxpBPQIBMf9s1P8TAnUNd0GGx0OxMVODF34L-D8b58z-XmaWzezdsj-PecM4AiUdKl0nWCTCSP0SuuLzvrrF2eulZLjXMKr45_KtdOom2Yi-7hF9-LVFB8tvyKHknfuZ_9VGK4qjDzn9DFV6uuy9ZiR6mChrzr0YDHfofy48l-pZyAOGTVpWcbwMAUR4nPrsZkRCeizpLVa9q2y-0JCgkzuhbz5-b9qkMlf9LGEUv3iM1m-Vn42EyT2JW4z5l91kETQ3UI3Ci-ns6k0v7j7a6ecLJPWGSQQBRsgBDtmKcUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکسیوس: به نقل از یک مقام آمریکایی گزارش داد که گروه آماده اعزام آبی‌خاکی Makin Island و یگان اعزامی تفنگداران دریایی آمریکا (MEU) سیزدهم، پایگاه دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند و انتظار می‌رود تا پایان نوامبر به منطقه…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24741" target="_blank">📅 11:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: ایران رادارهای پیشرفته‌ای ندارد و گاهی اوقات سعی می‌کند مین‌های دریایی کار بگذارد، اما ما معمولاً آنها را قبل از اینکه بتوانند مستقر شوند، از بین می‌بریم.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24740" target="_blank">📅 10:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رویترز:
نیروهای دولت رسمی یمن اعلام کردند طی حدود سه ساعت،
۲۰ حمله هوایی
علیه مواضع، نیروها، خودروها و تجهیزات نظامی حوثی‌هادر استان تعز انجام داده‌اند. این درگیری‌ها یکی از شدیدترین تشدیدهای نبرد میان نیروهای مورد حمایت عربستان و حوثی‌های مورد حمایت ایران از زمان آتش‌بس ۲۰۲۲ محسوب می‌شود. حدود
۱۹ جاده منتهی به استان تعز
نیز به دلیل درگیری‌ها بسته و مناطق اطراف آنها منطقه عملیاتی نظامی اعلام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24739" target="_blank">📅 10:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نیویورک‌تایمز: به نقل از یک مقام امنیتی غربی گزارش داد که ایران حدود
۱۰ موشک کروز ضدکشتی و ۳۰ پهپاد
به سمت تنگه هرمز شلیک کرده است. به گفته این مقام،
۴ نفتکش هدف قرار گرفته‌اند
؛ هرچند آمار فعلی سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
۱۳ مورد
است. جنگنده‌ها و بالگردهای تهاجمی آمریکا برای مقابله با حملات ایران در آسمان تنگه هرمز فعال هستند، با این حال
برخی پرتابه‌ها همچنان به کشتی‌ها اصابت می‌کنند
.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24738" target="_blank">📅 10:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آکسیوس: به نقل از یک مقام آمریکایی گزارش داد که
گروه آماده اعزام آبی‌خاکی Makin Island
و
یگان اعزامی تفنگداران دریایی آمریکا (MEU) سیزدهم
، پایگاه دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند و انتظار می‌رود
تا پایان نوامبر
به منطقه برسند. این گروه شامل ناو تهاجمی آبی‌خاکی
USS Makin Island
از کلاس Wasp، ناو ترابری آبی‌خاکی
USS Anchorage
از کلاس San Antonio و ناو ترابری آبی‌خاکی
USS John P. Murtha
از همین کلاس است. این نیروها
۱۰ فروند جنگنده F-35B Lightning II
و حدود
۲۲۰۰ تفنگدار دریایی آمریکا
را به منطقه خواهند آورد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24737" target="_blank">📅 10:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آکسیوس: به نقل از دو مقام آمریکایی و یک منبع در غرب آسیا گزارش داد که آمریکا برای حفاظت از زیرساخت‌های نفت و گاز،
یک سامانه پدافند هوایی MIM-104 پاتریوت
به قطر و یک سامانه نیز به عربستان سعودی ارسال کرده است. بر اساس این گزارش، یک سامانه پاتریوت در
یک تأسیسات کلیدی نفتی در عربستان سعودی
و یک سامانه دیگر در
یک تأسیسات گاز طبیعی در قطر
مستقر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24736" target="_blank">📅 10:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3218939c94.mp4?token=QXmP98IgcvLm5PYLmdgqo9Exnv3r24gV4-nqaHqiCqCs9H_tQLnpiIryyVCTDMX6BL_XU6qpGhDDkMEvkXm03GBttX19jMhCBDk4nCm_DHclUuXBGfSrCChShtlLaKhbiVk6-S7fFTtCymM0YjHWtJ3-Hb0gY2i9fwLeP1RfyioBv8bIy-nsytqwC627KJ45r37Rry87zsrbaxj8Atx5xPWdVe-iy4-ri5HWzXLqEr-VzAxNgQTznVeWAdJnpV4mfpYkNyCf_a2wZarcsAXH172hs8ZAFMC1mg4fIo_Lou0wadNVHvtYS03gYG84qFvlxcAiv69ozGhppH375NRdvYUDZmu5YmAjKMNsyjP4SxCwTMKM0-TPKOcdRg6OwBPIwvZXd4WM6534QkaFeYAmM6kgSKoiMhfzsWAbjBzASgwYfQcdvBzIdUdKVlt2k1JfsBXd3EgaswijMeJlZC0VkTXfb5tGS56r7jwRla3lZzMB6vLmnf8neVUkxGIfvUg0a6yrtYdE22Q4_A3zjVa-IUm4UIBkMHH5s450LSlbS6fKcGBcFZ8av1qY72h6cacXdkycs_vngRTZ-Dtk9KjuHNQ6QDJYtcPEISGbq4mmSDzw8p-sdZpRwFjaBZSc5ll0H9NxrNy6yVol3fd6rYxl-gWgli2hnRHSQQEVlqu41Lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3218939c94.mp4?token=QXmP98IgcvLm5PYLmdgqo9Exnv3r24gV4-nqaHqiCqCs9H_tQLnpiIryyVCTDMX6BL_XU6qpGhDDkMEvkXm03GBttX19jMhCBDk4nCm_DHclUuXBGfSrCChShtlLaKhbiVk6-S7fFTtCymM0YjHWtJ3-Hb0gY2i9fwLeP1RfyioBv8bIy-nsytqwC627KJ45r37Rry87zsrbaxj8Atx5xPWdVe-iy4-ri5HWzXLqEr-VzAxNgQTznVeWAdJnpV4mfpYkNyCf_a2wZarcsAXH172hs8ZAFMC1mg4fIo_Lou0wadNVHvtYS03gYG84qFvlxcAiv69ozGhppH375NRdvYUDZmu5YmAjKMNsyjP4SxCwTMKM0-TPKOcdRg6OwBPIwvZXd4WM6534QkaFeYAmM6kgSKoiMhfzsWAbjBzASgwYfQcdvBzIdUdKVlt2k1JfsBXd3EgaswijMeJlZC0VkTXfb5tGS56r7jwRla3lZzMB6vLmnf8neVUkxGIfvUg0a6yrtYdE22Q4_A3zjVa-IUm4UIBkMHH5s450LSlbS6fKcGBcFZ8av1qY72h6cacXdkycs_vngRTZ-Dtk9KjuHNQ6QDJYtcPEISGbq4mmSDzw8p-sdZpRwFjaBZSc5ll0H9NxrNy6yVol3fd6rYxl-gWgli2hnRHSQQEVlqu41Lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره عملیات«چکش نیم شب»: بمب‌افکن‌های ما از میزوری پرواز کردند، رفتند و برگشتند؛ ۳۷ ساعت در مسیر بودند و سوخت‌گیری می‌کردند. ساعت یک صبح، وقتی ماه نبود و هوا کاملاً تاریک بود، همه بمب‌ها را رها کردند و مستقیم رفتند پایین، روی این «کارخانه‌های مواد مخدر»… بمب‌ها مستقیماً از مسیرهای هوایی به داخل این، اِمم، کارخانه‌های مواد مخدر رفتند؛ واقعاً همین کاری بود که آنها انجام می‌دادند. آنها هسته‌ای و مواد مخدر بودند. آنها مواد مخدر تولید می‌کردند. این کارخانه‌های مواد مخدر/هسته‌ای به‌شدت هدف قرار گرفتند.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24735" target="_blank">📅 10:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بیانیه وزارت امور خارجه ایران: تهران
محدودیت‌های اعمال‌شده بر تردد هوایی میان ایران و عراق
را محکوم کرد و مغایر با منافع و مصالح مشترک دو کشور دانست و اعلام کرد این محدودیت‌ها برای
هزاران مسافر، زائر، بیمار و دانشجو
مشکل ایجاد کرده است. ایران همچنین خواستار
رفع محدودیت‌ها و بازگشت پروازهای دو کشور به شرایط عادی
شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24734" target="_blank">📅 09:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: ما نمی‌خواهیم ایران را در هرج‌ومرج رها کنیم و بعد رئیس‌جمهور دیگری بیاید که شاید کاری را که ما انجام دادیم، انجام ندهد. رئیس‌جمهورهای قبلی باید خیلی وقت پیش به ایران رسیدگی می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24733" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزارت دادگستری آمریکا:
اشتون حامد الابودی، مهندس برق ۵۱ ساله و کارمند وزارت انرژی آمریکا، به اتهام تلاش برای ارائه حمایت مادی به
انصارالله یمن
( حوثی‌های تحت حمایت ایران ) بازداشت شد. او متهم است برای ارتقای ارتباطات این گروه، تهیه تجهیزات پهپادی و قطعات ساخت مواد منفجره اقدام کرده است. تحقیقات از دسامبر ۲۰۲۴ آغاز شد و در سپتامبر ۲۰۲۵، الابودی به مناطق تحت کنترل انصارالله در یمن سفر کرد. او همچنین با یک منبع محرمانه FBI که خود را عضو انصارالله معرفی کرده بود، درباره
ادغام سامانه‌های ارتباطی و راه‌اندازی یک مرکز ارتباطات سیار
همکاری و برای تهیه تجهیزات آن کمک کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24732" target="_blank">📅 02:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24731" target="_blank">📅 02:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">😥</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24730" target="_blank">📅 02:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ درباره جنگ با ایران: شاید پیش از انتخابات پیروز شویم... آن‌ها موشک‌هایی دارند، اما ما می‌توانیم از پسِ آن برآییم. ما می‌توانیم از پسِ آن برآییم. آن‌ها موشک‌هایی دارند، اما تعداد بسیار کمی از آن‌ها باقی مانده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24729" target="_blank">📅 02:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68630ecc4a.mp4?token=ikkwKrr3HvTDkloJtiJ4QK4pOrDxuhxOihR-x2_D109RMZsK_mGNvB8_a8nV7i-AFVv2XHQA1p-yMsn0isJlrc1e5zDzi0JnlrLK7-UtIRhkhuoCfeVgXwyWL6foyVL2JnOI8P_T8srYW_L7xYqpN7Y8qozhdT8_X9s8lGOihQ4_JMixZ0a4IJs_SPW70SkyhCRLn6EeTA8UEN-QQKEpEtpnxNsnSuBaDavNP1KHmrc1d7ZafttwFYVMMXev5n4VggacEw-ByDZP-key_YrQ8OKcDcA854_xXIZ-w8oLn-donKaU0fmBlRxa3adTjI4Q8JDwTtbTUlyevRVmqjggQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68630ecc4a.mp4?token=ikkwKrr3HvTDkloJtiJ4QK4pOrDxuhxOihR-x2_D109RMZsK_mGNvB8_a8nV7i-AFVv2XHQA1p-yMsn0isJlrc1e5zDzi0JnlrLK7-UtIRhkhuoCfeVgXwyWL6foyVL2JnOI8P_T8srYW_L7xYqpN7Y8qozhdT8_X9s8lGOihQ4_JMixZ0a4IJs_SPW70SkyhCRLn6EeTA8UEN-QQKEpEtpnxNsnSuBaDavNP1KHmrc1d7ZafttwFYVMMXev5n4VggacEw-ByDZP-key_YrQ8OKcDcA854_xXIZ-w8oLn-donKaU0fmBlRxa3adTjI4Q8JDwTtbTUlyevRVmqjggQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر
»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24728" target="_blank">📅 02:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cb6b4532.mp4?token=pLfXcduXChgpOEFIpksZN79A7nuBVmDRe_DTN3SbD9xMTzzYFKGBjQIyxV-YdUL-lMozHX_wcnAb-DHOWoCBMlFH8YA7q47oNYVBJOKMDuoGWb1PqCAxGZA1gI4DbvjiYPEuwskIhLTXkzK61msH16hOuJjuPgzsvaVOYXD1qDf5_nvls7-iuAI8FCOPNQ4iVN3QmTt0Jc0j7gGiIJdTN48Q4bjLNwVJS7ljneZiXDI7d4dai41Z6nV9ysO0I86xkg4iPVdx9ztmLTjmpTHN-Hq5SMDEZkUArK0gRcRgZbmyx3q9XHc3XZCrR-OkDwFb9gizhoxt9rM2IMejrdBrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cb6b4532.mp4?token=pLfXcduXChgpOEFIpksZN79A7nuBVmDRe_DTN3SbD9xMTzzYFKGBjQIyxV-YdUL-lMozHX_wcnAb-DHOWoCBMlFH8YA7q47oNYVBJOKMDuoGWb1PqCAxGZA1gI4DbvjiYPEuwskIhLTXkzK61msH16hOuJjuPgzsvaVOYXD1qDf5_nvls7-iuAI8FCOPNQ4iVN3QmTt0Jc0j7gGiIJdTN48Q4bjLNwVJS7ljneZiXDI7d4dai41Z6nV9ysO0I86xkg4iPVdx9ztmLTjmpTHN-Hq5SMDEZkUArK0gRcRgZbmyx3q9XHc3XZCrR-OkDwFb9gizhoxt9rM2IMejrdBrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره اروپا:
«به آنچه برای
اروپا اتفاق افتاده
نگاه کنید. آنها دارند
زنده‌زنده خورده می‌شوند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24727" target="_blank">📅 02:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65aa2c1d6.mp4?token=hI13hEYclUqmOU0WBxwMcIuCqhCn5jzCtX8gXgPgFn8Do_ICr2pejJkjSx_PtU4tZTjlQfNy_x_sHIKcWbWooPTpVfPy64Cgxp9SeG5tLtVLr6gNNdqUDH-KMWili5UCimjOlqML9S4q3Pju7inw0B7gCzs_miWnHnIDiaZ31sa8qsKPCYb-gIp_EyCVdfV8kLKGY3z5yPyS2aqRPXTFWTfudxi7mVGwsc4ka37HlvU0YEXBJI2Z8YSS4F4Nn0YwO4Tbu1Rp3MjhJGO63DCU0NHTGpi1lDrBkSxsVaIj9Y1voQfm5N8FtKby0coiYwJloxiuHDMXrCj8FJ8C0Y8egg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65aa2c1d6.mp4?token=hI13hEYclUqmOU0WBxwMcIuCqhCn5jzCtX8gXgPgFn8Do_ICr2pejJkjSx_PtU4tZTjlQfNy_x_sHIKcWbWooPTpVfPy64Cgxp9SeG5tLtVLr6gNNdqUDH-KMWili5UCimjOlqML9S4q3Pju7inw0B7gCzs_miWnHnIDiaZ31sa8qsKPCYb-gIp_EyCVdfV8kLKGY3z5yPyS2aqRPXTFWTfudxi7mVGwsc4ka37HlvU0YEXBJI2Z8YSS4F4Nn0YwO4Tbu1Rp3MjhJGO63DCU0NHTGpi1lDrBkSxsVaIj9Y1voQfm5N8FtKby0coiYwJloxiuHDMXrCj8FJ8C0Y8egg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«آنها یا
کاری کاملاً درست و عاقلانه انجام خواهند داد
، یا
برای مدت زیادی دوام نخواهند آورد
.
وقتی با آنها
توافقی انجام می‌دهید
، این احتمال بسیار زیاد است که
به آن پایبند نمانند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24726" target="_blank">📅 01:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d52bcff0.mp4?token=H09undLos5aIVYtAJ9wRNCvkh5PxVL8WjVRR3z7RHp88pOokOnvRMX-KU5x3LlybUrYiziNbIeiBTjs3vhbd1r24R_xho_KbPg1Ec2kp2f5dk7NeSYxRU2jx-xkamaAYGkp8piHB2S79Re0847neL0Ys8vWZUMH_TpU5u8FHO70K0xWh9bJy40pmI0vMY6OWK9M1AJVkKTOI9Gxeu84Lmtvxi3BBTl3ELxmLoW9en8TXpOjcTYIWQGulazXmQ2X9Pvd8mkqoCbJ1CDcQM6EK6kloIG3Q_64OaTFJntt4-osvXoGPNWD-EcQE5vpxNJbNfUJ9RX6B4hCSUIi_jAIDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d52bcff0.mp4?token=H09undLos5aIVYtAJ9wRNCvkh5PxVL8WjVRR3z7RHp88pOokOnvRMX-KU5x3LlybUrYiziNbIeiBTjs3vhbd1r24R_xho_KbPg1Ec2kp2f5dk7NeSYxRU2jx-xkamaAYGkp8piHB2S79Re0847neL0Ys8vWZUMH_TpU5u8FHO70K0xWh9bJy40pmI0vMY6OWK9M1AJVkKTOI9Gxeu84Lmtvxi3BBTl3ELxmLoW9en8TXpOjcTYIWQGulazXmQ2X9Pvd8mkqoCbJ1CDcQM6EK6kloIG3Q_64OaTFJntt4-osvXoGPNWD-EcQE5vpxNJbNfUJ9RX6B4hCSUIi_jAIDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
« کسی حاظر نیست آنجا رئیس جمهور شود ، رؤسای‌جمهور ایران
دیگر در کنار ما نیستند
، اما ما تلاش می‌کنیم با
فرد فعلی
با ملایمت برخورد کنیم.
(منظورش رهبر هست)
بالاخره در مقطعی باید
با یک نفر وارد مذاکره و تعامل شویم
، درست است؟»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24725" target="_blank">📅 01:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eaaf7693d.mp4?token=uHcmHDRDYgF98-LXIiLTfnJzOpQfS7haY9bOatC1fIpUrZkuxcCgeWJk0nvl4IBD_UIRIsj8VIl-LIPWHQfK4rvBpd2vMEiB3tSafuxDTCKj9boLEkYKEKdOO15Wry1mDnWug0Bs4Oe5jvv3btzuOh3ZxKwOskNVl3nqYymzmp60Rp9QshE2Lr9ytaGO2Mfs1q0EqBtCXGizCxLR9RlAty7KU93X0EpBNMgQXzWtDjxgilcXcx6MCsE9B1dZXmTxtUfk41QHD14XMGn6-HQw5qAyOQOdO7ifclqjA2-O6e_5fLvfgsBq3AVO4P7j5vhUanJEb2WhqpAv8BL04Lb7XEvC-_QnXdRI8GIfTxl-1XiNnQqHCYtTB1Z3zzz6ujzWiA66sMcdWNTsFIySBvqLt_gpX0NvKDv6ohkMhb726Akcoi3bGBPAzbFNK-SlZ__1UBPK0tmHGukl8n_PTlRKirLFgfG1rZmn9B7iEf_fjJEKBAP_HxZk7uDLdU24oBGpEag1E8Ftab6RVBOm4YrelmAoUdrZWtgr8idhwCw-yoRctCjtZDhLzK0LkkWz-b4gIu8Ynn8N7o1FNXsExJLJWsII6ORfrFSZWXokM_EW3TdHjJDxCucddqlUK2f0b7tE0_iYxEWNALcmLgLjsuigZ7lb5slVxNt66Yh4jwDrze0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eaaf7693d.mp4?token=uHcmHDRDYgF98-LXIiLTfnJzOpQfS7haY9bOatC1fIpUrZkuxcCgeWJk0nvl4IBD_UIRIsj8VIl-LIPWHQfK4rvBpd2vMEiB3tSafuxDTCKj9boLEkYKEKdOO15Wry1mDnWug0Bs4Oe5jvv3btzuOh3ZxKwOskNVl3nqYymzmp60Rp9QshE2Lr9ytaGO2Mfs1q0EqBtCXGizCxLR9RlAty7KU93X0EpBNMgQXzWtDjxgilcXcx6MCsE9B1dZXmTxtUfk41QHD14XMGn6-HQw5qAyOQOdO7ifclqjA2-O6e_5fLvfgsBq3AVO4P7j5vhUanJEb2WhqpAv8BL04Lb7XEvC-_QnXdRI8GIfTxl-1XiNnQqHCYtTB1Z3zzz6ujzWiA66sMcdWNTsFIySBvqLt_gpX0NvKDv6ohkMhb726Akcoi3bGBPAzbFNK-SlZ__1UBPK0tmHGukl8n_PTlRKirLFgfG1rZmn9B7iEf_fjJEKBAP_HxZk7uDLdU24oBGpEag1E8Ftab6RVBOm4YrelmAoUdrZWtgr8idhwCw-yoRctCjtZDhLzK0LkkWz-b4gIu8Ynn8N7o1FNXsExJLJWsII6ORfrFSZWXokM_EW3TdHjJDxCucddqlUK2f0b7tE0_iYxEWNALcmLgLjsuigZ7lb5slVxNt66Yh4jwDrze0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«ایران
آماده تسلیم شدن است
. ما همین حالا می‌توانیم
خیلی راحت پیروز شویم.
»
من یقین دارم درست بعد از انتخابات ، شاید هم قبلش
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24724" target="_blank">📅 01:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ویولن بیژن در قم فعال شد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24723" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a86dcf7b.mp4?token=XxF2doq_LqusAtqxpoaPG-_iEtmUDj3fuYY22zzSR5qf9cvioGmpd5HrqVv6jDyK89gdB7r33X0LctUYcQaNHtVNeeMch0aVG4SvbHIjrcHKko3r4xBHO1oz21yFnGi0sgTpADn2XikENZq3GwiuChhveVwme6_PTglW7H2-XNl6nND5fj45tw3Q-e0v7nGUjGoRPjqW29ugjZxA83pY6fRY89_Y2RdQkcWeIpovSH70JkI3espr01sDY2U53iHiDPJ3UpWwu0c3cl3qVlkchXXbLwThrZA0-x4B4Upt3prSkVC0BZG5isV7K1_0ml1Fykn3rx_x8CnDNAZtZ_DSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a86dcf7b.mp4?token=XxF2doq_LqusAtqxpoaPG-_iEtmUDj3fuYY22zzSR5qf9cvioGmpd5HrqVv6jDyK89gdB7r33X0LctUYcQaNHtVNeeMch0aVG4SvbHIjrcHKko3r4xBHO1oz21yFnGi0sgTpADn2XikENZq3GwiuChhveVwme6_PTglW7H2-XNl6nND5fj45tw3Q-e0v7nGUjGoRPjqW29ugjZxA83pY6fRY89_Y2RdQkcWeIpovSH70JkI3espr01sDY2U53iHiDPJ3UpWwu0c3cl3qVlkchXXbLwThrZA0-x4B4Upt3prSkVC0BZG5isV7K1_0ml1Fykn3rx_x8CnDNAZtZ_DSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری سان : پلیس ضدتروریسم بریتانیا یک شهروند ۲۷ ساله ایرانی سیتیزن بریتانیا را به ظن آماده‌سازی اقدامات تروریستی و ارتباط با توطئه برای هدف قرار دادن پایگاه هوایی RAF Fairford دستگیر کرد. یک مرد ۲۶ ساله بریتانیایی نیز تحت بازجویی قرار گرفته و دو ملک در…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24722" target="_blank">📅 00:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رویترز:
قیمت نفت بیش از
۴ دلار در هر بشکه
افزایش یافت؛ پس از اعلام اعزام
سومین ناو هواپیمابر آمریکا
و تا
۱۰ هزار نیروی اضافی
به خاورمیانه، همزمان با توقف صادرات فرآورده‌های نفتی چین به خارج از هنگ‌کنگ و ماکائو، نگرانی‌ها درباره
کمبود جهانی سوخت
افزایش یافت.همزمان، محدودیت‌های صادرات گازوئیل از سوی
روسیه و چین
و تحولات مرتبط با ایران، فشار بیشتری بر بازار سوخت وارد کرده است.
قرارداد دسامبر نفت برنت با
۴.۳۷٪ افزایش
در
۱۰۲.۳۱ دلار
بسته شد. همچنین گزارش‌ها از
هدف قرار گرفتن سه نفتکش با پرچم لیبریا در تنگه هرمز
حکایت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24721" target="_blank">📅 23:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbEJ5GeVLKs_fsajw_TiJmSdqMn493fNx6ZnWsg7PzLRzClEwajyVZa921Tu8glw19K0whu10YcYJhg4_N6CFwXQDhBGUeJ3kcTRYrnlH0g6A49iMjPc4euQntRRIdCdTVhnyJoPigqe3DXUS6MrwychzmuUPdN8wjOx9pbG56tZ6v7RKb6Wo3MHjre0jRu_kUYKZnNPYo0ptMrJbZ-gUnbhUl3bEivO42wiXwG5iiktaqPi5zpn4lM29GnP-XnG3gj_g8xyCsZSoMTBtiLRjZbOuUdFoDUxbjZgpj_RfA55hADqQNehYAuy6xOgpS9OISad-Y5bcqA3SdPWLF8DQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجرات دریایی بریتانیا
:
یک نفتکش هنگام عبور از
تنگه هرمز
با یک پرتابه ناشناس برخورد کرده و در پی آن دچار آتش‌سوزی شده است. این گزارش از سوی یک منبع ثالث دریافت شده و
خدمه سالم هستند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24720" target="_blank">📅 23:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فاکس‌نیوز: ژنرال بازنشسته جک کین، تحلیلگر ارشد راهبردی این شبکه،
آغاز عملیات نظامی جدید پیش از انتخابات میان‌دوره‌ای آمریکا(۱۲ آبان) وجود دارد.
کین گفت ترامپ در حال بررسی زمان‌بندی چنین اقدامی است و عملیات می‌تواند پیش از انتخابات یا پس از آن آغاز شود. او همچنین گفت
عملیات مخفی موساد علیه ایران در حال انجام است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24719" target="_blank">📅 23:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacacbd314.mp4?token=gxzQP0D1Fv_IMjGPVHtrOC-Zt4qavop7wzYvq8pusnjTFAJSGGCzBOt4FQrYzPfMZBtgvZfcNBLxY6cscdd3e6EObaDDBDZ4SuG8w6TqB_jAX6BcGkjO8FVkIWFRQH1HAqY0WT-OjAHhRPxXOTfn4maRPkE2Mg35CJ7PYD0-CVSI4VoqmEVnmzjg6IXh9DSSqMdQO5XElvu7KTVNQmYVYmZ5O08kGl2TVZyLigljTirRawvEoa24JGtYEQ2AuDA0FOKfNUpA2vOSWJucs5T-BeAgVW8NL5MpJirOQUjNzV18Dbz-p-lZ8NFlNwHw9E1uZ9MUQ3iPiE8U5jVKP0rPUUhtCOjR79HNf3bGCYli8VZP9AMsL65T4_yHtSU1EmSxY1j5UitCqlavsuqs7VmoPyNKGRDDqsJkgd5Q2neXM5e7i8zPejmTyNHJpVQyff8o_4b71aytxoyYl7xRft7ZyFEGkq6659K7Kz274uQ5zsfxfVj5-NPTBpOIPP8NgSoAjWGJnkwDwmm1xVon5RvAkqbCz2HCy_TuSuk6_VGigQ7NJcbPt7nZDgHfesS1_RGnNblWBhcwTj3GwVk-bQHvYG5lUbHMiwSC7zUgTSSDpd_1VNBAWXbvZtWSH_ZD8kkOjR9a42MlboD924uf4xJFmc0dmAZIDp1aICxaTCkBSq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacacbd314.mp4?token=gxzQP0D1Fv_IMjGPVHtrOC-Zt4qavop7wzYvq8pusnjTFAJSGGCzBOt4FQrYzPfMZBtgvZfcNBLxY6cscdd3e6EObaDDBDZ4SuG8w6TqB_jAX6BcGkjO8FVkIWFRQH1HAqY0WT-OjAHhRPxXOTfn4maRPkE2Mg35CJ7PYD0-CVSI4VoqmEVnmzjg6IXh9DSSqMdQO5XElvu7KTVNQmYVYmZ5O08kGl2TVZyLigljTirRawvEoa24JGtYEQ2AuDA0FOKfNUpA2vOSWJucs5T-BeAgVW8NL5MpJirOQUjNzV18Dbz-p-lZ8NFlNwHw9E1uZ9MUQ3iPiE8U5jVKP0rPUUhtCOjR79HNf3bGCYli8VZP9AMsL65T4_yHtSU1EmSxY1j5UitCqlavsuqs7VmoPyNKGRDDqsJkgd5Q2neXM5e7i8zPejmTyNHJpVQyff8o_4b71aytxoyYl7xRft7ZyFEGkq6659K7Kz274uQ5zsfxfVj5-NPTBpOIPP8NgSoAjWGJnkwDwmm1xVon5RvAkqbCz2HCy_TuSuk6_VGigQ7NJcbPt7nZDgHfesS1_RGnNblWBhcwTj3GwVk-bQHvYG5lUbHMiwSC7zUgTSSDpd_1VNBAWXbvZtWSH_ZD8kkOjR9a42MlboD924uf4xJFmc0dmAZIDp1aICxaTCkBSq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : ناو یو‌اس‌اس جورج واشنگتن (CVN 73) در حین حرکت در آب‌های منطقه‌ای خاورمیانه، عملیات پروازی انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24718" target="_blank">📅 23:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترابری نظامی خیره‌کننده و عجیب آمریکا از ۲۴ ساعت گذشته تا همین لحظه… @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24717" target="_blank">📅 22:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b502de34b9.mp4?token=qnnvJ422C3ZNyV3UMrSvfUGFx1Uk1WXuaP2h3k9bdA3LSIUwECWi7930fHnmCsDZZPSkFq6A6hxXllbkmvfYTQWDvpqOIeBDCXaCyYnseXEUKJzKkMMkjbvuMRVKPbFcFYG3arjcbeJ-hBbBIdbSDBIeVyQtaMxgIdgaQW1t7gTKyjzHjPZ3kQbxiuWwFOADKjzJR1UQGMCWmdpgKP1ngWVquZb9JPATJYehEX0rhD8PF-Bhhhe9TgGfbkPueMlbFtkuZMVPBszc4YmISKLzfyhFmSqA_K2X8Wi-oQPYfe9MzRuSnezT6h3W3jTTimbmeqgUsrmzoli0y12Cnh6VwXJUAUtyWlpnOlKBUahteqjYHkR5lkowNlNA1Aq6X_7T4RBz7g7dYTZxse9WgfoXaU7M-oAJyugSJfJoeSbuY853nO07UwfBsElrKtqUkFVF9cUZ9hj4F3us_PdzIKtvHqNsRK0YrwkgnKJmciqwIgxPBx872QONPlTtdk9AChypPhAvfKWLEer7fRfEQJLzu_7Wq6nUJV0R6dDhNg7uxqlasX5Y98G15NCCxPW4vJ2Ab-rsmLdeVlRuM1vcMoAQGTr6T_SfSWENpRiv_-1qMdHlJ-b6eOH6EyOS2_4WpuGk8VLgBbCrB8HcmNMY7HMNvdivbcYp3QnS0i4HtWG39b0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b502de34b9.mp4?token=qnnvJ422C3ZNyV3UMrSvfUGFx1Uk1WXuaP2h3k9bdA3LSIUwECWi7930fHnmCsDZZPSkFq6A6hxXllbkmvfYTQWDvpqOIeBDCXaCyYnseXEUKJzKkMMkjbvuMRVKPbFcFYG3arjcbeJ-hBbBIdbSDBIeVyQtaMxgIdgaQW1t7gTKyjzHjPZ3kQbxiuWwFOADKjzJR1UQGMCWmdpgKP1ngWVquZb9JPATJYehEX0rhD8PF-Bhhhe9TgGfbkPueMlbFtkuZMVPBszc4YmISKLzfyhFmSqA_K2X8Wi-oQPYfe9MzRuSnezT6h3W3jTTimbmeqgUsrmzoli0y12Cnh6VwXJUAUtyWlpnOlKBUahteqjYHkR5lkowNlNA1Aq6X_7T4RBz7g7dYTZxse9WgfoXaU7M-oAJyugSJfJoeSbuY853nO07UwfBsElrKtqUkFVF9cUZ9hj4F3us_PdzIKtvHqNsRK0YrwkgnKJmciqwIgxPBx872QONPlTtdk9AChypPhAvfKWLEer7fRfEQJLzu_7Wq6nUJV0R6dDhNg7uxqlasX5Y98G15NCCxPW4vJ2Ab-rsmLdeVlRuM1vcMoAQGTr6T_SfSWENpRiv_-1qMdHlJ-b6eOH6EyOS2_4WpuGk8VLgBbCrB8HcmNMY7HMNvdivbcYp3QnS0i4HtWG39b0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولادیمیر پوتین: پیشنهاد انتقال اورانیوم غنی‌شده ایران به روسیه ارائه شده و این پیشنهاد
همچنان کاملاً روی میز است
. اما سپس آمریکا موضع خود را سخت‌تر کرد و گفت انتقال اورانیوم تنها باید به آمریکا انجام شود. از آنجا بود که ایران نیز تصمیم گرفت موضع خود را سخت‌تر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24716" target="_blank">📅 22:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بلومبرگ:
عباس عراقچی، وزیر امور خارجه ایران،بطور غیر علنی پیشنهاد داده است که تهران در ازای
کاهش تحریم‌ها، دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به تمامی تأسیسات هسته‌ای آسیب‌دیده ایران را از سر بگیرد
. این پیشنهاد در چارچوب تلاش‌های دیپلماتیک برای دستیابی به توافق میان ایران و آمریکا مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24715" target="_blank">📅 22:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24714" target="_blank">📅 22:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24713" target="_blank">📅 22:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش زیاد از ایست بازرسی های پی در پی در شهر های ایران مخصوصا کرج
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24712" target="_blank">📅 21:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">(پدافند) بیژنه غرب ایران کرمانشاه فعال شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24711" target="_blank">📅 21:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60239b6687.mp4?token=jXesyPWoCVIWcparwItPnsnwKqfHxZu8xwpO6urENg3_gTcX_Ev_MaozIX4uH7YS2WPcGmrQ9ZUv3RamVSkZUH0RF6XmFYL_mVfjkG2tRcVNHV_M2VXeNVIG7YHnvsADISPBfZrBamyKiqi1rnDEIzWeulJK02CqLptUmz7d6YehN5zJyLTZaqn2BKHsuwdud_7FlF7fKnmjrkL9fUWSBaBeQrz1w0-C44esPEk4fbfSeJlZvdgi31eQP2hH_gSBWm2EhHy38FkoUec7sZo0AkWX2xFlksJ5BoD0EfR7U3GodUXHDn8Q5H8FZqIJ4KyoV-NBdAPxhs8QQBYvdqXCjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60239b6687.mp4?token=jXesyPWoCVIWcparwItPnsnwKqfHxZu8xwpO6urENg3_gTcX_Ev_MaozIX4uH7YS2WPcGmrQ9ZUv3RamVSkZUH0RF6XmFYL_mVfjkG2tRcVNHV_M2VXeNVIG7YHnvsADISPBfZrBamyKiqi1rnDEIzWeulJK02CqLptUmz7d6YehN5zJyLTZaqn2BKHsuwdud_7FlF7fKnmjrkL9fUWSBaBeQrz1w0-C44esPEk4fbfSeJlZvdgi31eQP2hH_gSBWm2EhHy38FkoUec7sZo0AkWX2xFlksJ5BoD0EfR7U3GodUXHDn8Q5H8FZqIJ4KyoV-NBdAPxhs8QQBYvdqXCjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌تروث پستی از اعتراضات ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24710" target="_blank">📅 21:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24709" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تحریم‌های جدید علیه ایران، بخش‌های خودروسازی و راه‌آهن و شبکه‌های تأمین‌کننده و حامی آنها را هدف قرار می‌دهد و با هدف خشکاندن منابع مالی جمهوری اسلامی اعمال شده است. وزارت خزانه‌داری آمریکا امروز ایران‌خودرو و سایپا و همچنین…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24708" target="_blank">📅 21:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وال‌استریت ژورنال:
دونالد ترامپ به دستیاران خود گفته است که انتظار دارد
پس از انتخابات میان‌دوره‌ای نوامبر، بمباران ایران از سر گرفته شود.
مقام‌های آمریکایی می‌گویند هنوز مشخص نیست حملات احتمالی در چه ابعادی انجام خواهد شد. در همین حال، آمریکا در حال تقویت نیروهای نظامی خود در منطقه است و یک گروه ناو هواپیمابر دیگر نیز در راه خاورمیانه است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24707" target="_blank">📅 21:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">BTC 85000$
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24706" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مقام اماراتی به کانال ۱۴ : ارزیابی‌ها درباره اینکه ایران این حمله را سازماندهی کرده، در حال تقویت است. کاپیتان هندیِ مجروح نیز برای درمان به امارات منتقل شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24705" target="_blank">📅 21:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmypDcRtTzyvE5QSAD077lmzR6a3WT4WXN3Lf1tfKN6kNai96lPbYLukqpE015tnoVZwyU1CMH2EbBnWO22iZ8dEo_3wITmmmgO_IxiXRYiUlqzcVTLAJQdHmu94nDYEDk4pVfgOZf-sWU1WdXo92Klu1l48OUodBMntfLNtbO1pe3Ywf-57BNSvlFxcnYLMoyCtaeVu-QElWso_K5CwY9176Azg7Zo81yM-p3gW49hplrJhRFar7dI8DmugjcTsnoggaD-IySDvdOWDZtQkqRQS_xdmMkEBhYOko0cxrmpC7uHNBcTTx8bfblFwt8ev6Yy4LlTaIRrJGZEBHPv4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث سوشال: من بارها اعلام کردم که از بین بردن
تهدید هسته‌ای ایران
۴ تا ۶ هفته زمان می‌برد، اما من این کار را در یک شب انجام دادم! بقیه این مدت فقط برای اطمینان از این است که وضعیت همین‌طور باقی بماند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24704" target="_blank">📅 21:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تحریم‌های جدید علیه ایران،
بخش‌های خودروسازی و راه‌آهن
و شبکه‌های تأمین‌کننده و حامی آنها را هدف قرار می‌دهد و با هدف
خشکاندن منابع مالی جمهوری اسلامی
اعمال شده است. وزارت خزانه‌داری آمریکا امروز
ایران‌خودرو و سایپا
و همچنین چندین شرکت خارجی مرتبط با تأمین قطعات، مواد اولیه و خدمات این صنایع را تحریم کرد. واشنگتن می‌گوید این اقدامات بخشی از کارزار
«عملیات طرد اقتصادی»
برای قطع منابع مالی حکومت ایران و افزایش فشار اقتصادی بر تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24703" target="_blank">📅 21:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8939ddc2f8.mp4?token=vGK_CrC1_qXAiiyB0Mf_frEjx21i2at_EHkuWvLGPp_P43xR44a20aETnHC_G4bPKrdRaui7l_dDNjWEqDz7Of1qMkiB8OmDhSKJSbYfcr0IRX8-MRnQyJ5FfUphks-9WDwxwjXyn2U1jOikqIAMnejy9XViqNniTJBvKypNxQ-VvonqGpvF36TyOoiMLTXHxqIjSzYEcRCyO3V95YlJEFWlUDAkRY8hkISm-1IPs__X6sJ_fCw8Umwjs2jPGthApGvaQOnfSqYm-uGalYqYMTI5INzpVkCC_H1v42HIStMHCwb9VBBdHS7RVX6s869Wb0gcOgiFHouKgNNO0WxI6BGWJeR4GqExkkJWOEPXuBEHfh-Jnykvptt1aIL-53mwxc9SWK3-nYmE0OwZXJHmydEv95KWe7-oehe2K4q7i-yUqLxNqQUJkACF6VIlDiyZJzyW3bflDxsWgpCSu7aqkSozLlQ05IG7CBE5uOwpvymr3J0m9vpVlV39uzbcz7eDunhT-mDWoZeN_YNJX_3fqHFq9w6vsM9Zb95NrIiYcL42uHP9peLakYM8AQotZBkOIwzad5Cx2DaoJtBetTEqdm-6y9vN0PKlflJnju4RANOHsGoC425h0owpaunBYBMLWdlpiMcrtMcfxsCO59BGHHg07rmsOGVptaYOakGrRjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8939ddc2f8.mp4?token=vGK_CrC1_qXAiiyB0Mf_frEjx21i2at_EHkuWvLGPp_P43xR44a20aETnHC_G4bPKrdRaui7l_dDNjWEqDz7Of1qMkiB8OmDhSKJSbYfcr0IRX8-MRnQyJ5FfUphks-9WDwxwjXyn2U1jOikqIAMnejy9XViqNniTJBvKypNxQ-VvonqGpvF36TyOoiMLTXHxqIjSzYEcRCyO3V95YlJEFWlUDAkRY8hkISm-1IPs__X6sJ_fCw8Umwjs2jPGthApGvaQOnfSqYm-uGalYqYMTI5INzpVkCC_H1v42HIStMHCwb9VBBdHS7RVX6s869Wb0gcOgiFHouKgNNO0WxI6BGWJeR4GqExkkJWOEPXuBEHfh-Jnykvptt1aIL-53mwxc9SWK3-nYmE0OwZXJHmydEv95KWe7-oehe2K4q7i-yUqLxNqQUJkACF6VIlDiyZJzyW3bflDxsWgpCSu7aqkSozLlQ05IG7CBE5uOwpvymr3J0m9vpVlV39uzbcz7eDunhT-mDWoZeN_YNJX_3fqHFq9w6vsM9Zb95NrIiYcL42uHP9peLakYM8AQotZBkOIwzad5Cx2DaoJtBetTEqdm-6y9vN0PKlflJnju4RANOHsGoC425h0owpaunBYBMLWdlpiMcrtMcfxsCO59BGHHg07rmsOGVptaYOakGrRjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال 14 اسرائیل: «این عملیات برای دستیابی به سه هدف طراحی شده بود: کشتن تعداد زیادی از اسرائیلی‌ها، آسیب رساندن به روابط ما با امارات، و آسیب رساندن به خود امارات.»(زیرنویس فارسی)
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24702" target="_blank">📅 21:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8e632d84.mp4?token=cKKc2YjAmlShpoANJiNo5K0XK3rLPYz_KsqF50De25cKhcP-CHXpu-Wa3RDdARKC1KDo93NxKMd7DQ4MexjM4M5cvKexfeGS-YFc4re8UyX5qKz4x79SjCvAybkUcn_NnImajBQ-rB5oYjvQ8QR7rFGkHp4_n2GDY4gDtDtW1HYBWaUxXGoGFzQcwOgWIrnSKpGnXqtxcyBpc1Wz7x_neWg0iHuN3aDKP0EikjbG8-xDPPfXtHiSUGVCddBef1P9YFLQ8-BYKNWbuIYmigFxQZ1n6WPzxITILmQ_yvUp0gE1YxNCxWPmt7cRc6qU6CiPJcol6oKsh3zgEIyg_mxS4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8e632d84.mp4?token=cKKc2YjAmlShpoANJiNo5K0XK3rLPYz_KsqF50De25cKhcP-CHXpu-Wa3RDdARKC1KDo93NxKMd7DQ4MexjM4M5cvKexfeGS-YFc4re8UyX5qKz4x79SjCvAybkUcn_NnImajBQ-rB5oYjvQ8QR7rFGkHp4_n2GDY4gDtDtW1HYBWaUxXGoGFzQcwOgWIrnSKpGnXqtxcyBpc1Wz7x_neWg0iHuN3aDKP0EikjbG8-xDPPfXtHiSUGVCddBef1P9YFLQ8-BYKNWbuIYmigFxQZ1n6WPzxITILmQ_yvUp0gE1YxNCxWPmt7cRc6qU6CiPJcol6oKsh3zgEIyg_mxS4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوکی از شبکه فاکس: این خلبان فلای دوبی ممکن است توسط سپاه پاسداران منصوب شده باشد، یا به نوعی دیگر افراطی شده باشد و سپس سعی کرده باشد هواپیما را سرنگون کند؟
ترامپ: ممکن است، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24701" target="_blank">📅 21:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee9e6e4bb.mp4?token=PcKM8Z6oLG64XFpqsariEPJZaDIrkxXEoFEtMf1iPYziS7-0l7FPeQX6qCX0dea8AcPE_KZSyHDxT7KGgRGDDm5BN96IDt5pAG2ywOFRpL4qKiOd3i1BIFqkrPCqzwnw6RGHN1xGVluc4JdaRSQK2eTmrM6zY6vGJvhFQhbqFfLvSqdnoI8QneGbtAOI13FZRNPkgAGAWwXYmwiBopkyjQ1D8fsKIdN_Bi7O0eP8c0xYaOB2UtnxpHx4La2U4tbGwOTvujbRgFJyl_DmPTgYJaLn9I4AqlPHTJ9xZfCymsZgFPkqcdOgJWdwWkOxQejC5z_2x2WYeb_Yjb1_6DJhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee9e6e4bb.mp4?token=PcKM8Z6oLG64XFpqsariEPJZaDIrkxXEoFEtMf1iPYziS7-0l7FPeQX6qCX0dea8AcPE_KZSyHDxT7KGgRGDDm5BN96IDt5pAG2ywOFRpL4qKiOd3i1BIFqkrPCqzwnw6RGHN1xGVluc4JdaRSQK2eTmrM6zY6vGJvhFQhbqFfLvSqdnoI8QneGbtAOI13FZRNPkgAGAWwXYmwiBopkyjQ1D8fsKIdN_Bi7O0eP8c0xYaOB2UtnxpHx4La2U4tbGwOTvujbRgFJyl_DmPTgYJaLn9I4AqlPHTJ9xZfCymsZgFPkqcdOgJWdwWkOxQejC5z_2x2WYeb_Yjb1_6DJhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سوال که آیا ایران در حادثه مربوط به هواپیمای فلاي‌دبي دخیل است یا خیر، گفت: "به نظر من، با توجه به اطلاعاتی که دارم، بله، اما ما در حال حاضر در این زمینه کار می‌کنیم."
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24700" target="_blank">📅 20:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5221c8193.mp4?token=RDwtlz3_zfO-rPH6vlNvafQA9Mw1lkdUZLoxbWnw4VWidyLasO5A7TO1gJZlPhaHWWDOsupJ4e8GeGRlms0I-QxoMbcU6tj0NL9oAWRI5Rz9-1KGZ-jXcespDeEcUJmCwYIRxSGcR9mT6hrDFl64mV4Vt4PYZ07x23hsONUhwTp059wP8mQYUBVadkhQnSp2u9azIGroaokFFgZC1XoupGK_CttACwrt3QatpnnfAk0uOxQLlrfJS__aTN-DNyqMN0RG0VVCZRP9xp1USa2OMUsVrICfc2uEhBoF5Fha428LQzyC3aJctpXWt5zjEsgEfrwd7OPRnijqUBr3LCbX6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5221c8193.mp4?token=RDwtlz3_zfO-rPH6vlNvafQA9Mw1lkdUZLoxbWnw4VWidyLasO5A7TO1gJZlPhaHWWDOsupJ4e8GeGRlms0I-QxoMbcU6tj0NL9oAWRI5Rz9-1KGZ-jXcespDeEcUJmCwYIRxSGcR9mT6hrDFl64mV4Vt4PYZ07x23hsONUhwTp059wP8mQYUBVadkhQnSp2u9azIGroaokFFgZC1XoupGK_CttACwrt3QatpnnfAk0uOxQLlrfJS__aTN-DNyqMN0RG0VVCZRP9xp1USa2OMUsVrICfc2uEhBoF5Fha428LQzyC3aJctpXWt5zjEsgEfrwd7OPRnijqUBr3LCbX6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای شرکت در گردهمایی انتخاباتی جمهوری‌خواهان عازم اوکلاهوما شد. دونالد ترامپ، رئیس‌جمهور آمریکا، پنجشنبه ۹ مهر برای حضور در یک تجمع انتخاباتی جمهوری‌خواهان در شهر دورانِت، اوکلاهوما، به این ایالت سفر کرد. این مراسم در چارچوب انتخابات میان‌دوره‌ای کنگره آمریکا برگزار می‌شود و ترامپ در حمایت از نامزدهای جمهوری‌خواه سخنرانی خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24699" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین تصاویر از خروج خلبان هندی زخمی پرواز فلای دوبی با بانداژ سنگین و کمک‌خلبان مهاجم با دست‌های بسته منتشر شد. نکته مهم درباره پرواز دبی–اسرائیل، هویت خلبانان دوم جایگزین است که عربستان آن را مخفی نگه داشته. هواپیما در آسمان اردن و نزدیک…</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/24698" target="_blank">📅 20:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d65db6813.mp4?token=BoFqKQeHOqNW_H4_M0RwPj83cKmnpwgW8HqWCNaIYSuAQtcuH3BWWVHFoy9RiAJeYsyZIfMplz5mKgjez877--yW5QzI0aKbOM9weTPPNR_R1YvtJkbpOfwvJUmV4BkqPNlSPXKfDuedWqJxi-9xWJG84oI-NtSmquGYoeVemazcQ0C9wYDB1P51i1dmIltv60lNMBkSCUSwfHYV-KHbC-1bAAKFY3ebq4nsAR0RLb1XKzA5ozGHZaxKHjWGZxoPSIC3Q_7E7OHuVZZkaILUDjW_UAdCCxXeX3-gAThhUy8_RT0ZHBPc_JYnQ55o_cYxmC4073ITdlAmliIjjC5NIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d65db6813.mp4?token=BoFqKQeHOqNW_H4_M0RwPj83cKmnpwgW8HqWCNaIYSuAQtcuH3BWWVHFoy9RiAJeYsyZIfMplz5mKgjez877--yW5QzI0aKbOM9weTPPNR_R1YvtJkbpOfwvJUmV4BkqPNlSPXKfDuedWqJxi-9xWJG84oI-NtSmquGYoeVemazcQ0C9wYDB1P51i1dmIltv60lNMBkSCUSwfHYV-KHbC-1bAAKFY3ebq4nsAR0RLb1XKzA5ozGHZaxKHjWGZxoPSIC3Q_7E7OHuVZZkaILUDjW_UAdCCxXeX3-gAThhUy8_RT0ZHBPc_JYnQ55o_cYxmC4073ITdlAmliIjjC5NIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : «در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چه نظری دارید؟»
ترامپ: «هر اتفاقی برای ایران بیفتد، برای نیروهای نیابتی آن هم همان اتفاق می‌افتد.»
@WarRoom</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/24697" target="_blank">📅 20:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7973c43baf.mp4?token=JJxFO10gMikAP12k37cqUMxArbTIpNDTetyKQvcngWy96iQdkrb21cX1_R3GbFo3CjwKLXC1-afSX8jXWIhL0y41NMHkEy9vgoInk0QOQgSeSqCDO8mw9bKATR5ZCH-BT0H3F5NAp_dGX6rC9ieVSgot4NHlj1FYdlkszAYEtSfeI71JuiBojRBN2Rgn5w18DjQXnrsaIurdwKDh2PGzFsnPSRcSSPjIPXLlRV7P4ksAbzvav6fZ4mM-3MKIFC952DblYJAb1fxU_rP_SvW5dxWZue_kZzzyFtpYCIYC25c0gIIPQbLBH6xeLQRVXDb8gXGpD-jFUGwfn0L89n3Dog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7973c43baf.mp4?token=JJxFO10gMikAP12k37cqUMxArbTIpNDTetyKQvcngWy96iQdkrb21cX1_R3GbFo3CjwKLXC1-afSX8jXWIhL0y41NMHkEy9vgoInk0QOQgSeSqCDO8mw9bKATR5ZCH-BT0H3F5NAp_dGX6rC9ieVSgot4NHlj1FYdlkszAYEtSfeI71JuiBojRBN2Rgn5w18DjQXnrsaIurdwKDh2PGzFsnPSRcSSPjIPXLlRV7P4ksAbzvav6fZ4mM-3MKIFC952DblYJAb1fxU_rP_SvW5dxWZue_kZzzyFtpYCIYC25c0gIIPQbLBH6xeLQRVXDb8gXGpD-jFUGwfn0L89n3Dog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: به جرئت می‌گویم که صددرصد مردم,  از جمله در سراسر جهان , با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/24696" target="_blank">📅 20:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین تصاویر از خروج خلبان هندی زخمی پرواز فلای دوبی با بانداژ سنگین و کمک‌خلبان مهاجم با دست‌های بسته منتشر شد. نکته مهم درباره پرواز دبی–اسرائیل، هویت خلبانان دوم جایگزین است که عربستان آن را مخفی نگه داشته. هواپیما در آسمان اردن و نزدیک مرز اسرائیل بود، اما دو خلبان جایگزین تمرینی به‌جای فرود در مقصد ، مسیر را تغییر داده و بدون فرود حتی در اردن، هواپیما را به عربستان بردند. نتیجه این اقدام، نجات خلبان تروریست عمانی و جلوگیری از مشخص‌شدن اسناد این عملیات بود. یکی از دو خلبان بریتانیایی بوده و هویت خلبان دوم اعلام نشده؛ احتمالاً فرانسوی یا اسپانیایی باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/24695" target="_blank">📅 20:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314c1f7963.mp4?token=bVCwnBupzmNoXT-sUcKWFC9LZXccAjqxbyQOn_3XwcZaWmmOTVB8NoGyyGPUUuQ36bj67c0yMe3TH_NQbLAKBUIWqO8zA4asRpLDG78rzdSeiB9KEz69IczibrXqkTADvps5FUIAkmIV18nKqtuz8b0FOO6terJf4zMtdujpi9mB2ayJdabaBtdhfyY90c6KxyzMWffUezX8c5PEfufauy7D5s6J5jP3xh16oewpxGTmrC6EjEvF75yTS2aK8WSONfvTX3czPQ7-GL8pya9l6fpLuq1N2KBk02v7YorNKOEtHZUt50uj4RVKitPrV-2QoZETtsZXEBhhhKSxsLiVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314c1f7963.mp4?token=bVCwnBupzmNoXT-sUcKWFC9LZXccAjqxbyQOn_3XwcZaWmmOTVB8NoGyyGPUUuQ36bj67c0yMe3TH_NQbLAKBUIWqO8zA4asRpLDG78rzdSeiB9KEz69IczibrXqkTADvps5FUIAkmIV18nKqtuz8b0FOO6terJf4zMtdujpi9mB2ayJdabaBtdhfyY90c6KxyzMWffUezX8c5PEfufauy7D5s6J5jP3xh16oewpxGTmrC6EjEvF75yTS2aK8WSONfvTX3czPQ7-GL8pya9l6fpLuq1N2KBk02v7YorNKOEtHZUt50uj4RVKitPrV-2QoZETtsZXEBhhhKSxsLiVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: اگر ایران پشت حمله به هواپیما باشد، آیا شما علیه آن اقدام تلافی‌جویانه خواهید کرد؟ آیا ایالات متحده تلافی خواهد کرد؟
ترامپ: آنها ضربه سختی خواهند خورد، نگران نباش. فقط از آنها بپرس؟ آنها می‌دانند چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/24694" target="_blank">📅 20:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcf1464cf.mp4?token=CqimjhIVnLQDBmakR7750VhZEg3kYgNIGtl0oi4_DPQOp0Y4aa4FZFZ9rcKHAPBROw3Iuh27yfK_n9yMCJZPo2BkGWlqRf6UjUID-9lFehRTLuOBnm0Ows08khwSMY-AcwOm9wHFrZkLQ__r-1s1anMvJadO3JFUGq1VBG6MSyTi0N963amak5qWAnUAtANUTSbFTKUu-eed8HodkBVRYVv7rXx70dTQ2lzM-o-3EnwMIneY-A9hTaGYkhRz9bCtiW-699hoSIhQiih3Hd-m9bINehb9NOhzHQUvsFOkMXyLlidArp0JhxsHRfH1u6r74oFnyzYo9bxJjhbz52YVqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcf1464cf.mp4?token=CqimjhIVnLQDBmakR7750VhZEg3kYgNIGtl0oi4_DPQOp0Y4aa4FZFZ9rcKHAPBROw3Iuh27yfK_n9yMCJZPo2BkGWlqRf6UjUID-9lFehRTLuOBnm0Ows08khwSMY-AcwOm9wHFrZkLQ__r-1s1anMvJadO3JFUGq1VBG6MSyTi0N963amak5qWAnUAtANUTSbFTKUu-eed8HodkBVRYVv7rXx70dTQ2lzM-o-3EnwMIneY-A9hTaGYkhRz9bCtiW-699hoSIhQiih3Hd-m9bINehb9NOhzHQUvsFOkMXyLlidArp0JhxsHRfH1u6r74oFnyzYo9bxJjhbz52YVqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و نخواهد داشت؛ آن‌ها نیز پذیرفته‌اند که چنین سلاحی نداشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24693" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e638a4cc.mp4?token=h8PQNmtKlj124kPa1g1fWbzrjcNoEUB6fb6_UqsWaETMFmWLZuBpCldSzhXavfq4gEfuvVas99c3ttNywosqUxmlHo6v0h4w-SCUjX698rDRKd9qeH3x3JanUNi0E6XwMz5oU0VVL0vusGS40SEd4_21uPK5N3hmrQzDQH01AmtWrcu_1bh6vEwZAJXVbqq9rTf4N9-cUlE-QurRaZEvSH245EKZQedCWfj0DjVwgpRKcet4Iio4uPCf4xdEk0-gMx5IR_kPUl2dGE0TzKFqV-2QQ90-oBmYl0KFAgf540XDYq0uWPDCwK3WUU4JMMSv83anGlsXSIOaw0tR4FhYiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e638a4cc.mp4?token=h8PQNmtKlj124kPa1g1fWbzrjcNoEUB6fb6_UqsWaETMFmWLZuBpCldSzhXavfq4gEfuvVas99c3ttNywosqUxmlHo6v0h4w-SCUjX698rDRKd9qeH3x3JanUNi0E6XwMz5oU0VVL0vusGS40SEd4_21uPK5N3hmrQzDQH01AmtWrcu_1bh6vEwZAJXVbqq9rTf4N9-cUlE-QurRaZEvSH245EKZQedCWfj0DjVwgpRKcet4Iio4uPCf4xdEk0-gMx5IR_kPUl2dGE0TzKFqV-2QQ90-oBmYl0KFAgf540XDYq0uWPDCwK3WUU4JMMSv83anGlsXSIOaw0tR4FhYiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نرخ‌های بهره می‌توانند رشد را کند کنند. ما خواهان رشد هستیم؛ و رشد موجب تورم نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24692" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1487770b48.mp4?token=IT3QQzqrBc7ukLLYqXOHZvElfpjDK-SDAd3hNbatvcp3CaOpfoL192ekzQwtk9bw2icTaHH4Glrlk9BLUbecuETjwwwBgZSUH2KzyAoaWRiY72ndRFS70vVecebyLfb1vi7Hf_DXwdvRfELsih3JuhSKpOvLLYR6yRbnYakigucluw1J59ETI7KS5z2VaSGbf0nfdRtOEfug5bFKHZnR0bkLOGz1_q-IjKY1EY_rVIRNfrq1gYy6g6KCJRxHEifSvSQZOOEhmpKhWY4jbuH82iBMHk31efHy2wWaG8iTXwBHR_AzD93K6QYWE21AUW2iDJci2vS2oU_3-aWw2Y9RPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1487770b48.mp4?token=IT3QQzqrBc7ukLLYqXOHZvElfpjDK-SDAd3hNbatvcp3CaOpfoL192ekzQwtk9bw2icTaHH4Glrlk9BLUbecuETjwwwBgZSUH2KzyAoaWRiY72ndRFS70vVecebyLfb1vi7Hf_DXwdvRfELsih3JuhSKpOvLLYR6yRbnYakigucluw1J59ETI7KS5z2VaSGbf0nfdRtOEfug5bFKHZnR0bkLOGz1_q-IjKY1EY_rVIRNfrq1gYy6g6KCJRxHEifSvSQZOOEhmpKhWY4jbuH82iBMHk31efHy2wWaG8iTXwBHR_AzD93K6QYWE21AUW2iDJci2vS2oU_3-aWw2Y9RPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24691" target="_blank">📅 20:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری سان : پلیس ضدتروریسم بریتانیا یک شهروند ۲۷ ساله
ایرانی سیتیزن بریتانیا
را به ظن آماده‌سازی اقدامات تروریستی و ارتباط با توطئه برای هدف قرار دادن پایگاه هوایی RAF Fairford دستگیر کرد. یک مرد ۲۶ ساله بریتانیایی نیز تحت بازجویی قرار گرفته و دو ملک در لندن بازرسی شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24690" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/24689" target="_blank">📅 20:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ: موضوع ایران می‌تواند به انتخابات میان‌دوره‌ای آسیب برساند
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24688" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
