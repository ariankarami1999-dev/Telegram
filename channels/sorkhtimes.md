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
<img src="https://cdn4.telesco.pe/file/E-OcL4P7bJyGlQtDSdi-_oeVWOcY2_lNXFBzTONyXw4Zr1IeXISXO9KuspDUehmEiGTG9xai_Q9eDHnIhgzPtUiP6iynWdt-deR-Hisq2ANbyJPjlKGcoENLOYEM6xzcE5E1zmvWssd1lfWYsmeHmnWb1d7LXw5PEKyIT3mt2yOPw92t-8hIfm2HOIHS9dtybQykUerx4k_dy6jfgaJgOMwwvwfTrEGY2L-HUG5KlSdkHzdr0DMvU4_rBBjsn7aurP4TQoaSsEKkwr1K7KKIXwcG3lCozipd3A064KDSggKtv464x2CA9IHk9x6K_2K5IM5Bpoya3_-8JsGAO50kzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 22:28:39</div>
<hr>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/136507" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/136506" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9FoWSJ9g287eR852lJWcnWgaGxDFjxWcdsLCJFRMyvO2x6aEGcT4EF_eHvh7t_SHkaquzQbNLXWYLTkwpZSQqsRyfpw0qRCYuM4XlyXM51sOXAXnBkmePki_vGvcYHKeuHlv-JTB9m1vy84DvWy5wtMzhduZZnBxFXBJeKn2_e6KVlTqaU9T8O-7_HLwlC0b88hJ8-eHlu2g1Ju6PYoOWk9ROk5IhN1nlvQZo7z-LZ6qilDMd1-2E34KHRg2gnXWHLsF8yk2pBgcjFjEDEKB5vAokKRBIVIp3OpK4A4JVBWZzrEgSYso45QQRkrvsEJe8cSZcVpqXdSiZkHCbh1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/136505" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/136504" target="_blank">📅 20:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
پورعلی گنجی هنوز با پرسپولیس برای جدایی به توافق نرسیده است
🔹
گفته میشه این بازیکن زیر بار کم کردن قراردادش نمیره و کل پولش می خواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/136503" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/136502" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
تکمیلی :فرهیختگان: استعلام از فیفا اومده و مشکلی برای انتقال نیست و احتمالاً هردو قرضی رایگان تا نیم فصل + بند خرید با تیم راهی ترکیه میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/136501" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtN6YitsY3BTuuTLnR8Roa38WO7betkSgmJReTvUDDyas8PMK6-tLycwCZa7F-FCQ2vAqGl6OQ7q7LzVSvGg6m3IoNJTFGQPF4kqV6kzbRsZO-kS-j1kqDfX-T76QkNi5EtEbaSX9LHBwAFP8KLvTjnVPSVXBjzk9ATKnEee9O6cozXNhBWOXZ0uCKCpCMdR9DtrWKeZhYP93yAfalxyxNfWlNnsUGBzMPVhERaoZfBX_D0Kc8ZX-bQt92gc4WRsCo2QnZ_Pc44rLoWeHl8s9fdggLJdMR1soWz1nTSXadO-XtDPGukVbc972T5Z3D18p7deqzpwgLPiqe4qg-6NNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طاهرخانی:
❌
میلاد زکی‌پور با ارسال پیغام‌هایی به بعضی از افراد خواهان پیوستن به پرسپولیس شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/136500" target="_blank">📅 20:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/136499" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbV-0VQJlemGnJ-OA4cNDRogoU54wQ8R2fonYd4So-bFlO4VvlTkiOdvhFxLEgNAbJvko5cCKzewXSwc0qoCAFm4R-hl7-CL-qTXT4CkhPPLE4GxTofc756AnzBRBfX9HxxSDuKGCwb9kckczp4aRU4FzDsVNJua12V0AaNotjy_mP5Y4TtlgQuuCDcKgAU1u2c0MzBxZ8Srtc9p7DrxJg76-2WRszCsGH7gm9wJJcwzQvW_5lhaIMXH26JcFPaiElQ4ByZwBNacaThp3apWjH0WP8chgw-wcumqg_DU6upmwxHPcNzmi_cMOcR1d_gobb-tShlVKnbJjJJAIa09ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@ARON_TIP @ARON_TIP
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/136498" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
❗️
به این ترتیب با وجود رد شکایت باشگاه پرسپولیس، همچنان موضوع اصلی پرونده محرومیت 4 ماهه بیرانوند به قوت خود باقی است و این دروازه‌بان در شکایت به دادگاه CAS خواستار لغو محرومیت و جریمه مالی خود شده است.
🔴
🔴
شنیده می‌شود هنوز علیرضا بیرانوند در موضوع شکایت…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/136497" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136496">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
🚨
خبرگزاری تسنیم: عادل فردوسی‌پور نباید از علیرضا فغانی که از رضا پهلوی حمایت کرده، تو برنامه خودش دعوت می‌کرد و همین باعث قطع برنامه‌اش شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/136496" target="_blank">📅 19:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136495">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/136495" target="_blank">📅 19:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136494">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
پرسپولیس فعلا با احتیاط داره از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نمیده، چون دیرتر از بقیه بازیکنان به تمرینات اضافه شده
❌
❌
کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدومیت های پی در پی نداشته باشه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/136494" target="_blank">📅 18:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=K7-sA7qkklzBVozb0v4pNQb0wBjSb1_tvEfVDlxpNI_bJIJf7hyV3REj0adn2xXja8kOslyw0lEZ-vC4q3jZy7S7IjtwkSWaHf-Ypflf38EPPcFken8QzrMkoxcvhXsAzjQR_Cq8T6vCuAZNlptK5L0zGu6vnSqg6a9sRG8ITuk9mSu2VcSDK92b7hC_-dlPkUgwGmcN6uG-jYs4LHW1hN4kAosL6NBf04cu2fYnp-pr69hYVpvC9FZQp1s_j2DERAqqpokbn9Sd-0AGUC8fSzUAWu3HqtgmK1tUqxMa5r0DVEvcfBGUgLE5V0xlXYIYmcfMjrIF_S4mSUHTY6ZPyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=K7-sA7qkklzBVozb0v4pNQb0wBjSb1_tvEfVDlxpNI_bJIJf7hyV3REj0adn2xXja8kOslyw0lEZ-vC4q3jZy7S7IjtwkSWaHf-Ypflf38EPPcFken8QzrMkoxcvhXsAzjQR_Cq8T6vCuAZNlptK5L0zGu6vnSqg6a9sRG8ITuk9mSu2VcSDK92b7hC_-dlPkUgwGmcN6uG-jYs4LHW1hN4kAosL6NBf04cu2fYnp-pr69hYVpvC9FZQp1s_j2DERAqqpokbn9Sd-0AGUC8fSzUAWu3HqtgmK1tUqxMa5r0DVEvcfBGUgLE5V0xlXYIYmcfMjrIF_S4mSUHTY6ZPyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/136493" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
#فووووووووووری
🔴
پرسپولیس در آستانه جذب دانیال ایری و کسری طاهری
🚨
پرسپولیس از فیفا استعلام گرفت و فیفا اعلام کرد مشکلی برای عقد قرارداد وجود ندارد
📰
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/136492" target="_blank">📅 18:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
باشگاه پرسپولیس برای جذب کسری طاهری از فیفا استعلام گرفته و منتظر جواب فیفا ست تا برای جذبش اقدام کنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/136491" target="_blank">📅 18:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
🔴
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/136490" target="_blank">📅 18:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
ویدیو باشگاه پرسپولیس برای خداحافظی و تشکر از کمال کامیابی نیا
❤️
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/136489" target="_blank">📅 18:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136488" target="_blank">📅 17:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
🔴
تیم فوتبال پرسپولیس فردا برای برپایی اردوی تدارکاتی ارزوم ترکیه عازم خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136487" target="_blank">📅 17:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فووری/منابع عبری: ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/136486" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/136485" target="_blank">📅 17:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
ترامپ:ما اصلاً کارمان با ایران تمام نشده است
🔻
ما در حال حاضر قصد ترک خاورمیانه را نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136484" target="_blank">📅 16:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136483">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
پرونده شکایت پرسپولیس از بیرانوند و تراکتور که دوساله طول کشیده به علت عدم پرداخت هزینه دادرسی توسط cas مختومه اعلام شد!
🔴
🔴
مدیریت درویش و حدادی:)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136483" target="_blank">📅 16:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
دیدار تدارکاتی پرسپولیس با نتیجه دو بر صفر به پایان رسید و پرسپولیسی ها با پیروزی به ترکیه خواهند رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136482" target="_blank">📅 16:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
پرونده شکایت پرسپولیس از بیرانوند و تراکتور که دوساله طول کشیده به علت عدم پرداخت هزینه دادرسی توسط cas مختومه اعلام شد!
🔴
🔴
مدیریت درویش و حدادی:)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/136481" target="_blank">📅 16:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
فووووووری؛ با اعلام کاس، شکایت پرسپولیس از علیرضا بیرانوند رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136480" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136479">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
شکایت پرسپولیس از بیرانوند و تراکتور رد شد
⏺
دادگاه عالی ورزش (CAS) اعلام کرد شکایت پرسپولیس علیه علیرضا بیرانوند و تراکتور به‌دلیل عدم پرداخت به‌موقع هزینه دادرسی رد شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136479" target="_blank">📅 15:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136478">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
ارونوف تحت شدیدترین محافظت پزشکی
🔴
🔴
پرسپولیس فعلاً خیلی با احتیاط از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نداد. چون دیرتر از بقیه به تمرینات اضافه شده، کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدوم نشه.…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136478" target="_blank">📅 15:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136477">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
بی تفاوتی علی دایی درباره استوری بیرانوند؛ فقط سکوت
🔴
🔴
علی دایی صراحتا به دوستان نزدیکان خود گفته است که قصد ندارد جواب علیرضا بیرانوند را بدهد چرا که اصلا او را در حد خود نمی‌داند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136477" target="_blank">📅 15:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136476">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❗️
قلی زاده: فکر نمیکنم تو ایران برای تیمی جز پرسپولیس بازی کنم ؛ چون قلبا پرسپولیسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136476" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136475">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136475" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136474">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
امروز ساعت 18:45 دیدار پلی‌آف مابین صنعت نفت و مس رفسنجان برگذار خواهد شد تا هجدهمین نماینده لیگ برتر در فصل آینده مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136474" target="_blank">📅 14:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136473">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352f2979cb.mp4?token=r9prUNUW9UJ5Bbip-PyZsDJhTTULIeMELSuAwu0CVakLh8TGoad_xFvPDUTPmu2xdlwr_ja5KG-YKhvM2khg-4kyBZR833MuSKurRAMUi8eNJr73lFMlnOdAHk8_xyyDS-P2RI31OBq-60H4Q1mHsg35ZVHKiCZEU5v9jaYcos4w7jjhVh9pjZHGGONiP0--SkDP09iR_q_nxA-5wbvK_ZpRgBfrgwfxgnhBP4j_zZ2qkBTLrBq-fhT9iVX369GNFnty8ylJ8aI8WVl0GkzBLoL9JUPxyGczIh8_xzk6dT3Vat4jPH03MqbFpMGBYuV81Wri9tblW5uJHF3nOUdeaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352f2979cb.mp4?token=r9prUNUW9UJ5Bbip-PyZsDJhTTULIeMELSuAwu0CVakLh8TGoad_xFvPDUTPmu2xdlwr_ja5KG-YKhvM2khg-4kyBZR833MuSKurRAMUi8eNJr73lFMlnOdAHk8_xyyDS-P2RI31OBq-60H4Q1mHsg35ZVHKiCZEU5v9jaYcos4w7jjhVh9pjZHGGONiP0--SkDP09iR_q_nxA-5wbvK_ZpRgBfrgwfxgnhBP4j_zZ2qkBTLrBq-fhT9iVX369GNFnty8ylJ8aI8WVl0GkzBLoL9JUPxyGczIh8_xzk6dT3Vat4jPH03MqbFpMGBYuV81Wri9tblW5uJHF3nOUdeaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136473" target="_blank">📅 14:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136472">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/136472" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136471">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/136471" target="_blank">📅 14:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136470">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136470" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💛
آپدیت جدید اپلیکیشن اندروید MelBet
❗️
🎁
کد هدیه 100 دلاری:
giftcodeir
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را فارسی کنید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136470" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136469">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.Melbet.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
giftcodeir
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136469" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136468">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e636d7ab2.mp4?token=gXQrO97oDsP4_STgIuLVp0aBf_Hbav6YHAQLJwDRN23ktu8gcZ7mAjj_7o3auF5WK3Jh9NKd66kHlgruzKUCuk4EMO31OeSrd6GiWVK3_qdZS_4IBbPEVbM0nxbYnu2TMapEYU6QQh9-wbAgnthWCO3TYbBJmil6nEwStWwYxchUKmiMmyFyzZ1gcQM8wQENPZuzFmTTAeTk3IYuCyzyp2kfccSso_1kNo0Ip-b6Ev-W_KGTWlYQym-iBSzBC42-2rDH86VJMRFhfV3J4U5_9pAuFS3wpO7ezOCUY4dMBg1mXr_qJfDOrigCyblsZQqECvwziUF1Q-SoWs3PUnJb7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e636d7ab2.mp4?token=gXQrO97oDsP4_STgIuLVp0aBf_Hbav6YHAQLJwDRN23ktu8gcZ7mAjj_7o3auF5WK3Jh9NKd66kHlgruzKUCuk4EMO31OeSrd6GiWVK3_qdZS_4IBbPEVbM0nxbYnu2TMapEYU6QQh9-wbAgnthWCO3TYbBJmil6nEwStWwYxchUKmiMmyFyzZ1gcQM8wQENPZuzFmTTAeTk3IYuCyzyp2kfccSso_1kNo0Ip-b6Ev-W_KGTWlYQym-iBSzBC42-2rDH86VJMRFhfV3J4U5_9pAuFS3wpO7ezOCUY4dMBg1mXr_qJfDOrigCyblsZQqECvwziUF1Q-SoWs3PUnJb7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فنرباغچه اسماعیل کارتال با این گل زیبای تالیسکا بازی رفت پلی آف لیگ قهرمانان اروپا رو برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136468" target="_blank">📅 13:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136467">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚩
🚩
قلعه نویی منتقدان تیم‌ ملی را بی وطن و وطن فروش خطاب میکنه...
❗️
❗️
❗️
🔖
🔖
خاک بر سر فوتبال این مملکت، که سرمربیش قندلی است...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136467" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136466">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
در ابتدا مدیرای باشگاه قصد فروش اورونوف رو داشتن تا فصل بعد ازاد جدا نشه ولی تارتار خواهان ادامه‌ی حضورش شده و جداییش کنسله/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136466" target="_blank">📅 13:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136465">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⌛️
⌛️
فووووووووووووری
🚨
لیگ برتر به صورت رسمی از 23 مرداد آغاز خواهد شد.
🚨
همچنین جمعه 2 مرداد مراسم قرعه کشی لیگ برتر برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136465" target="_blank">📅 11:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136464">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641375cfeb.mp4?token=lPa5Jvs3GzMKkOXbwm0yYMrZeI1F_C8kcPozr9It5TKgz4bNVVeRp2CQzLNll8GdxmsIINkKxDD8EKby8iYtagGPH8aWmhFcvvYtrAiKEHMtnSB44ykYvZcciQXZJRSu03xeYHi1KgsRw4D78ozuF_tXU_OEYq1G0Zi3Pe_zsGMi5lnSwmpxcqdsp5CeiaZcW68qBEl9rh4VTjvKMHMsfnQpc-8rLXH12aZT95_J7X0ZWcJ_-JFi4EtdcgC1U2ChYIYA3EjPrjPcgAp3pWbGYqkgYQnc829xNnFJcagK7zXnEojHOa1aOVH23um2alx1WC_U8Sg2alg4zHejIrZ6xl6YTMAYhmfF6sSImcOHk_4OnSissYLswZ-5SUF4D0oextjgxeEkmYRggh1mcizbJP0i0NVCQ-OuyzsfLquMZ4Sym2VUdvlSjfeFU5AJ04BbTkLKRKqnLU93shd4P7gxIXnSGMWBV9otr_CCo58OjL6Tq7IG0eOiUuSaseCmk5GHXHho0gn8exEXoWc0feOmcmOk3M22N7W9cMr2D49uf4VNSf_89liMYqZXNr5rGl6LcNsVL-WgF3-yTK5usFb5odYsyZvfQQoRa_YY_fRPi5x4EFW305mSKlzepxgdjPeSbeFMZ7bgCdKIzeTatQeEq1UaEqSbiy2kPUpZpkP-mNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641375cfeb.mp4?token=lPa5Jvs3GzMKkOXbwm0yYMrZeI1F_C8kcPozr9It5TKgz4bNVVeRp2CQzLNll8GdxmsIINkKxDD8EKby8iYtagGPH8aWmhFcvvYtrAiKEHMtnSB44ykYvZcciQXZJRSu03xeYHi1KgsRw4D78ozuF_tXU_OEYq1G0Zi3Pe_zsGMi5lnSwmpxcqdsp5CeiaZcW68qBEl9rh4VTjvKMHMsfnQpc-8rLXH12aZT95_J7X0ZWcJ_-JFi4EtdcgC1U2ChYIYA3EjPrjPcgAp3pWbGYqkgYQnc829xNnFJcagK7zXnEojHOa1aOVH23um2alx1WC_U8Sg2alg4zHejIrZ6xl6YTMAYhmfF6sSImcOHk_4OnSissYLswZ-5SUF4D0oextjgxeEkmYRggh1mcizbJP0i0NVCQ-OuyzsfLquMZ4Sym2VUdvlSjfeFU5AJ04BbTkLKRKqnLU93shd4P7gxIXnSGMWBV9otr_CCo58OjL6Tq7IG0eOiUuSaseCmk5GHXHho0gn8exEXoWc0feOmcmOk3M22N7W9cMr2D49uf4VNSf_89liMYqZXNr5rGl6LcNsVL-WgF3-yTK5usFb5odYsyZvfQQoRa_YY_fRPi5x4EFW305mSKlzepxgdjPeSbeFMZ7bgCdKIzeTatQeEq1UaEqSbiy2kPUpZpkP-mNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در اتفاقی عجیب، محمد خلیفه به سبک رضا درویش بر روی خودش کت انداخت تا دیده نشه و از ساختمان باشگاه استقلال خارج شد
😂
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136464" target="_blank">📅 10:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136463">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYNZ7QuSmrHf_VliUsjXT6PCvdjn3D7fnAqMp8ex2KDTFMmK3kbl0NQWiOWcq-EhjUYogebOMIgbCUNHhCExtuO7x0h2OUH6tAAE1EnNeQ4Xs6wrYuAfKG4uEub8E7gjLXAtlsw0LbKPb9Ljp8F6j270B8U_azsPULY_POBxO1y1dTuSvZbRewpHkCsWvV-G_revLjbNnmCxMgzDxRGobQCQQGiw_NeFpMWR7H5V8u35LwLjRZZ6-5nSA5PeIg7GdhzU6SZgcs5JxQ36qcDD5idu_8odUrz9KmSwJQ2Y0KsH8Uvsz4miqM1KZ98PfcTpOgdKkajHOYldQWjTYBRSGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شرط پرسپولیس برای جذب کسری طاهری مشخص شد
🔴
🔴
پرسپولیس به نساجی پیشنهاد داده طاهری را تا نیم‌فصل به‌صورت قرضی جذب کند و سپس با همان مبلغ پرداختی نساجی به روبین‌کازان، قرارداد دائمی او را نهایی کند. حالا تصمیم نهایی در انتظار پاسخ مدیران نساجی است.
🖍
✍️
خبرگزاری…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136463" target="_blank">📅 10:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136460">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❤️
🟢
مروری بر مهم‌ترین لحظات دومین مسابقه تدارکاتی سرخپوشان؛ دیداری که با پیروزی ۲ بر صفر پرسپولیس برابر خیبر خرم‌آباد به پایان رسید
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136460" target="_blank">📅 10:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136459">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
سید جلال
:
❗️
هیچوقت به رفتن به استقلال فکر نکردم و نمیکنم به بقیه بازیکناام میگم اینکارو نکنن.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136459" target="_blank">📅 10:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136457">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
تصاویری از بازی دوستانه امروز پرسپولیس و خیبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136457" target="_blank">📅 10:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136456">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136456" target="_blank">📅 10:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
وحید کاظمی داور دیدار پلی‌آف لیگ برتر شد
🔴
🔴
وحید کاظمی، قضاوت دیدار پلی‌آف لیگ برتر بین مس رفسنجان و صنعت نفت آبادان را برعهده خواهد داشت. این مسابقه روز چهارشنبه ۳۱ تیر از ساعت ۱۸:۴۵ در ورزشگاه شهر قدس برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136455" target="_blank">📅 09:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136454">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
دیشب و بامداد امروز هم طبق معمول انفجار شدیدی در جنوب و بندر عباس داشتیم و برعکس روزای قبل تهران و اکثر نقاط تهران صدای پدافند و صداهای عجیب و غریبی شنیده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136454" target="_blank">📅 09:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136453">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
کسری طاهری و پرسپولیس یک قدم تا یکدیگر فاصله دارند
🔻
مدیران پرسپولیس در آخرین پیشنهاد خود به نساجی اعلام کردند با انتقال قرضی کسری طاهری تا نیم فصل و سپس امضا قرارداد دائمی با این بازیکن با همان مبلغی که باشگاه نساجی آن را از روبین کازان گرفته حاضر به خرید…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136453" target="_blank">📅 08:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136452">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136452" target="_blank">📅 08:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJhpUjjkYKEGsL9lU4lsiFulbjWBuurYXwniFOe-8yXBVVFVJND5b5PQb1mDQYWzYCU37OtMFPaWarvFgd8OED0-isOff7G1bhYQEpDpU3PT0iq280xwLvcjqzgKRU_S-8TaISk1kqLRvtfy21xURE-YDBEGSrtGoYyw7HsfzXkRQ8-XJ6-e8hLbgygPFq91X_nrqD-Z9Rmqt4G2YDGRzhA6Rw4ElLRljQlmE2xbv9stqSWDyeYTS0DlJkhOgnBoQ_NFEcUKxf4_HFb48zHiT1OZeTvNEZHLjwMRczYZMFLvusshximyDZICwXqRz98zBH1w1m-8VFv8rkA81JGhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136451" target="_blank">📅 07:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136449" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136449" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYjA2_FRU4tXqaYmqRAsPB4CUkDDfLg2Heg2gwZ7j8Wh-_IZH_n4DaFFbZlkq-E66flc0TsLi4SEMENr7BCHgAT8X8QXvt8TQEmf3SUFYAFC563rPJD5bbJQ3WWkuHsymjk4Rn__sSAltjPcKZJrQsfOWPOiFPdy43oZ2qFYzYn7bLh2PlpDlz5vYuEbLhIG8YXFSpKUphAgx3BdvbgyoNgAN4PTDfgQTCkN2MkXDDA0uLQNkJNtxk52dRUPifk_7qUV6dg3jdVj92xih0T3TQ-k4MoxYf5SXmMWsl60uuRZzqk5esLLkqyq1aC1ezn7I0E0U8CD--YX8sheLJoS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136448" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فرهیختگان:
🔴
تارتار یه وینگر تکنیکی می‌خواست، اما بعد از مذاکرات با یوسفی، هاشم‌نژاد، لیموچی، کوشکی و چند گزینه دیگه، مدیران پرسپولیس به این نتیجه رسیدن که محمدامین کاظمیان رو حفظ کنن و روی خودش حساب باز کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136447" target="_blank">📅 00:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
دیروز تو بازی دوستانه امیررضا رفیعی بازی نکرده و گندمی جوون نیمه دوم به میدون رفته
🔴
به نظر جدایی رفیعی قطعی شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136446" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmPXS3vlKJeMYaOTur9v6yM8d2cKYMDX8w0M3tFJTsZdrbYf0oZzDsHkA5oJo8DTurd8lANgLwK0FXJp-g3xZccEsAdrzO74Ke6n3o29tVJhi0r4gS79H5F_XAgXhaIuXakc_ONB6D0G3mnSh8E7hO_DU5_reKRHfbchVy8CJyt7EN1zm55XSMYTCVy3Ti2tX3RhDaSBp53x61zpBB90h8SnGk9TOmGj93gHk3-gB3EG5zvkorf5osj9kIeM0VdJoMfBIhQJQzN9kWxcwIaaXjgllCQsRDrvgkvIb6pk_EKt22vLJfdwMjNWH20mSB6sB9GJxVLcojAlxKT4z2PHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ
🔴
جنگ در افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
🔴
جنگ در عراق: ۹ سال، ۴۶۰۰ کشته.
🔴
جنگ در ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔴
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
🔴
جنگ در ونزوئلا: ۱ روز، ۰ کشته.
🔴
درگیری نظامی در ایران: ۴ ماه، ۱۸ کشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136445" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
🚨
🚨
فرشید حقیری: محسن خلیلی گفته کسری طاهری مصدومه و پل میشه و کنسله. دانیال ایری هم چون پل میشه کنسله
😟
😟
😟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136444" target="_blank">📅 23:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
رفیعی خودش قراردادش رو با پرسپولیس فسخ کرده و حالا دستش بازه هر تیمی خواست بره. احتمالاً هم راهی گل‌گهر یا شمس‌آذر می‌شه و اخباری جاش به پرسپولیس میاد.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/136443" target="_blank">📅 23:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Niff1qEcHjAQQii1tbS20uEYGreYQXdA9QICcRQTid2Kd9NZ7NNh6GFd-geuHWMTXfFLvSt4U1hi2qCb33kItdq9Qy7upgnwk5RlXnppz-ynpSFBy6rrAxJPMCS4-SKXbCRDEsSjrtDELBkm13K-MXv4j7x6wmCfHwfjd56bWYoXQS9KDs-htuOVRHyPe_xZgvvorqZEiXdSdDTOKus2CqClEtHSY4_1Fextwype7qjNS1y63fk9R0gFNkTXd8cEIXF2jEk-DDsvh42Om3XSuCVrQ30qEk_SQ-BQ531UE2CIVdBXyKXt7l-Qse6d3KflK8ErR3UR-Z66M98p1d4_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووری/منابع عبری: ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/SorkhTimes/136442" target="_blank">📅 22:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
تعریف و تمجید مهدی تارتار از فراز کمالوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/136441" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
🚨
🚨
فرشید حقیری: محسن خلیلی گفته کسری طاهری مصدومه و پل میشه و کنسله. دانیال ایری هم چون پل میشه کنسله
😟
😟
😟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/136440" target="_blank">📅 22:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APx_uokrA12pG6PRdNUKC4WNwy4Pb3uUWbFlGj8OFKxQfms50toeJSeK4CGxVTTiH0A9XdVE_6KtXw0QwGqZ2pIikuqq7mobGOKt_ncvnGxmvYv7RvhOTNyvjDTS3vCJ34bf6vgTduvFslVYT8vh10bgI7TVdrKTnnUcSEU4AqmNExCXwTnAQ0ybU8Y0q9hFpqsGL1fZ9dK2tbQ4pkC5QwK6rNxDKZBO3Xaz-E1E2pR0uPecVMBTEAyTnWQXSR3BAN6aYyOIcHXNqrVg54wIoDPPoK5BuVZ2ZpReEEatmmJnUMFFZ2LyKNtds6GZOoIprTJSw1kMfkKSaPaHFYGDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از بازی دوستانه امروز پرسپولیس و خیبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/136439" target="_blank">📅 22:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136438">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
🚨
خبرگزاری تسنیم: عادل فردوسی‌پور نباید از علیرضا فغانی که از رضا پهلوی حمایت کرده، تو برنامه خودش دعوت می‌کرد و همین باعث قطع برنامه‌اش شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136438" target="_blank">📅 22:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
حمید درخشان: آبروریزی پرسپولیس قابل جبران نیست
🔴
🔴
به قدری عملکرد مدیرعامل پرسپولیس ضعیف بوده که قابل گفتن نیست. پرسپولیس به تیمی باخت که کلاً دو جلسه تمرین کرده بود و این شکست نتیجه مدیریت ضعیف است.
🔴
🔴
نوع مدیریت حدادی باعث شده تا تیم بزرگ پرسپولیس زیر سوال…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136437" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136436">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136436" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
جدیدترین آپدیت اندروید اپلیکیشن 1XBET
🍏
برای آموزش ثبت نام مخصوص کاربران ios اینجا را بخوانید.
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
بدون فیلترشکن
از اپلیکیشن استفاده کنید</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136436" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136435">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvwUrAjiJCtQTWxwujVRwI1FUp1Xe99DpbopH1pwaGepb5PnzoOAWnfzEt1s2FDpee4OykD8ndOV664lextW3y7U6UdkT0aT6oX01gqlmVMzhFkX0exKxaF06_wWrWoKMRCkkNFF62umZU5-uqLQMHj3oFPPi1exCU02rZGR_o8T60_Fu_2PllOEfzy1Gw260P1SAyLSZEi-7Azn233qOkxj0QHaWz_t37vyguAYrMCQ4u0RjNdTfs51245ep5LxPgcoBlFLt7NszQcrGZQnXt76r75ecfOUDmKci6_mOOThyLeGdSaMGNps6tv-NgfNTkKMw1gVxZW4tZ4qrzJX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
وان‌ ایکس بت برترین و خفن ترین سایت پیش بینی بین المللی که به کاربران ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
vipfarsi
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر بازپرداخت هدیه میدهد.
☁️
اگر نمیتوانید وارد اکانت خود شوید به ما پیام دهید.
🔔
آموزش ثبت نام و واریز
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🔑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136435" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136434">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
#فوری | ترامپ:
🔻
ایرانی ها هنوز چیز زیادی از ما ندیده اند، ما تا کنون بسیار مودب بوده ایم.
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136434" target="_blank">📅 21:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136433">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
حسین قدوسی: پرسپولیس درتلاش برای کاهش مبلغ رضایتنامه‌ی محمد مهدی محبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136433" target="_blank">📅 21:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136432">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
شنیده ها:توافقات با محبی صورت گرفته.. واریز رضایت نامه به باشگاه اماراتی انجام بشه رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136432" target="_blank">📅 20:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136431">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
#فوری | ترامپ:
❗️
بدون شک ما کوه کلنگ ایران را بمباران خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/136431" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136430">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
❗️
فوری/جرزوالم پست: ترامپ پیشنهاد قطر و پاکستان برای آتش بس ده روز با ایران را رد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136430" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136429">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💥
امیررضا رفیعی با استناد به بند‌‌ در قراردادش عدم بازی در 10 درصد بازی ها عصر امروز به صورت یکطرفه قراردادش را فسخ کرد و بدون توافق با باشگاه در تمرین دیروز باشگاه هم حاضر نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136429" target="_blank">📅 20:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136428">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
پرسپولیس با گل های تیکدری و سرگیف ۲-۰ جلوعه  پ.ن تیکدری فعلا تو هر دو بازی تارتار گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136428" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136427">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akn6jt2XivhmCPnG0P29wGeGobFqrAotny-oXvG31FBahW4oqPuL5ivQBdmFTZgDF0a--VxeISfogFUcjX4M5N4EtFzoikvD27KUxrKYWgXakTxhGmnS6HZ_zTpIO35tgW33bpEhrCadjtGV_WEmLpwydWAHlSzHUnfRFiFH4_RmN5bMfcVGiWgnFHomfSnRcr6zxdZjSsM9JpxqtQbLRgh5AfxzqNgX-cI4ghWnwTL2C8OAoSIf0gA4w_F0QLcCyrdoSupwRp3jznhciP3dRC0A9z8l4VM5fhg3O6OzDjzkiXdkeNwreM2u3APnf6L8e2yno8GCDTiOEDyOcUC7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده ها؛ مهدی تارتار لیست بازیکنانی را به باشگاه داده و به آنها اعلام کرده مشکلی با معاوضه نفرات با بازیکنان مدنظر وجود ندارد
🔴
امیررضا رفیعی
🔴
حسین ابرقویی نژاد
🔴
مرتضی پورعلی گنجی
🔴
دنیل گرا
🔴
تیوی بیفوما
🔴
یاسین سلمانی
🔴
محمد امین کاظمیان
🔴
علیرضا عنایت زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/136427" target="_blank">📅 20:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136426">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
پرسپولیس با گل های تیکدری و سرگیف ۲-۰ جلوعه  پ.ن تیکدری فعلا تو هر دو بازی تارتار گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136426" target="_blank">📅 20:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136425">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از تسنیم
🚨
تراکتور در آستانه نهایی کردن قرارداد محمد قربانی قرار دارد و نماینده باشگاه تراکتور هم اکنون برای انجام این توافق در دبی حضور دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/136425" target="_blank">📅 18:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136424">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
یه جریانی تو باشگاه هست که می‌خواد پورعلی‌گنجی بمونه و بدش نمیاد با رفتن ابرقویی، جا برای موندن این مدافع باز بشه.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/136424" target="_blank">📅 18:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136423">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
فوووووووووری از حسین قهار
🔴
حسین قهار: هدف از مازاد کردن ابرقویی ؛ بازگشت مرتضی پورعلی گنجی به پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/136423" target="_blank">📅 18:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136422">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
پرسپولیس از دقایقی پیش تو یه بازی تدارکاتی به مصاف خیبر رفت
🔴
ترکیب پرسپولیس تو بازی:
🔴
پیام نیازمند،
🔴
عیدی،ابرقویی،کنعانی‌، جلالی
❌
خدابنده‌لو، باکیچ،
🔴
تیکدری، محمودی،  عمری،
🔴
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/136422" target="_blank">📅 18:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136421">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس برنامه دارد کسری طاهری را به صورت قرضی جذب کند و در نیم‌فصل با پرداخت رضایت‌نامه او را از نساجی دائمی جذب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/136421" target="_blank">📅 17:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136420">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فووووووری: دانیال ایری به پرسپولیس پیوست /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/136420" target="_blank">📅 17:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136419">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
تارتار برای اینکه پرسپولیس از فرم مسابقه دور نشه، خواسته تیم هر هفته یک بازی تدارکاتی داشته باشه. بازی با خیبر خرم‌آباد اولین بازی این برنامه‌ست و باشگاه هم دنبال حریف‌های بعدی برای هفته‌های آینده‌ست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/136419" target="_blank">📅 17:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136418">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
دانیال ایری به پرسپولیس پیوست/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136418" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136417">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
پروژه جوونگرایی نساجی قدرتمند تر از همه تیم ها در حال اجرا؛ مجتبی حسینی سرمربی نساجی مازندران شد/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136417" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136416">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
✅
سیتنا : علت فیلترینگ سایت فوتبال ۳۶۰ چیست؟ پس از مجموعه‌ای از شکایت‌های صداوسیما علیه این رسانه و در پی افزایش فشارها پس از برخی برنامه‌ها و گفت‌وگوهای اخیر فردوسی‌پور، از جمله مصاحبه زنده با علیرضا فغانی، این تصمیم گرفته شده است
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/136416" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136415">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136415" target="_blank">📅 16:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136414">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
❗️
به این ترتیب تارتار هر سه گزینه اصلی خود برای پست دفاع راست، یعنی رامین رضاییان، دانیال اسماعیلی‌فر و آریا یوسفی را از دست داد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/136414" target="_blank">📅 15:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136413">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWVG_9_mfKR_oCkRyKptVgflJqZ9Y619xGKr0n_CQzTqCyGspdSWolBfDZhwfTIdTKGAxy5KEWoWaFXUPF2iMhqUhzLQdBtYDuP_khGcqJhICQNFwfJZdNBz_VvG0cX8X_sZF9bWjUEEna_Ehri4xIR6s-u6RPLPKGBKvSls1KTNl5PiGiBXlAOAzVkPuEqgI0GsQ0oA1H9OIJP_GaM_v5Y_yIsEESEv5siZGbn-V32D-OhH9BCrlVVcOyk3T5Ogir1vX2Ud1G9GDqCIIQZvlhU63VLbvwAt517wyKebLvbpBvty5OIh47xq4Dl_Oq0vIcAPUhcnfkaXktHHF9k2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا کوشکی پس از بازارگرمی و افزایش نرخ قرارداد با کیسه تمدید کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/136413" target="_blank">📅 15:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136412">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
محمد خلیفه عصر امروز با حضور در باشگاه استقلال قرارداد پنج ساله با این تیم امضا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136412" target="_blank">📅 15:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136411">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136411" target="_blank">📅 15:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136410">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
جزئیات اولیه از پیشنهاد قطر برای برقراری آتش بس:
🔹
۱- پایان جنگ و برقراری آتش بس
🔹
۲- تنگه هرمز تحت کنترل ایران به مدت ۱۰ روز باز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136410" target="_blank">📅 15:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136409">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
مهم ترین خرید های پرسپولیس دانیال ایری، محمد مهدی محبی و کسری طاهری خواهند بود/ خبرنگار فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136409" target="_blank">📅 15:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136408">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136408" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136407">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN0VOtB2V_JqiVM-mkwn5cozppV7MzQ0uRO99BaGA0-gDb5am5OwW_US_UuMSQUKK36HLhbHD5XG6xMBqCATmpqhojXHeVKzOk0agkVVolenKZsgVsP9HkNnsB1xThxxUW_quh5gQYLVT52KMVgEl1CwdsjeYOlGs15cn7FgGnNyzjLAONCCSRQKzWqUhH90KAHmTY3SU71VY3P-jaH6PtwBgyYOA6XkmlMKMz9oTpTilZ_glrOoic6FYh_ppbv8ObnUvVtBJAkgXgqbMMYB2E8mCyySXXIV3zspZlsLFxuy5P9tyoPAv8fuZKtXjATnFajc7kFJlZvmQmKfnZZEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
➡️
JOIN
JOIN
JOIN
JOIN
➡️
JOIN
JOIN
JOIN
JOIN</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136407" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136406">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
💣
One Signature. One Earthquake
…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/136406" target="_blank">📅 14:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136405">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
سایت و اپلیکیشن فوتبال 360 ( برنامه عادل فردوسی پور ) چند دقیقه ای هستش که از دسترس خارج شده و خیلیا احتمال فیلتر شدنشو بخاطر حرفاش علیه قلعه نویی میدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136405" target="_blank">📅 14:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136404">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
🔴
شکاری با استقلال مذاکره کرده و با باز شدن پنجره احتمال جذبش بالاست و اگه الان باز نشه زمستون یاغی میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136404" target="_blank">📅 14:12 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
