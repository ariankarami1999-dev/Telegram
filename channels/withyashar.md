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
<img src="https://cdn4.telesco.pe/file/SX3EEjUqyRk0XgPufYLRM0eIJ7yH0Jn2SVJiQkGetc7ixWVP1_DdnyoMoxP4Ctk9apbB1F-fbCqefpHDA80371W-9NKi_zLXXQuiaPgBQhBMQtbjA8z_30Bao8ifhoM1Dc7JwjvBlV-20BL_VZbjeY54JvvrEECnqApiql1eKYtGBiLZfvN8UBZr6OT1GqjHqLuN6RsZB56XESAAMx5UPKnJHY_QD0n4mispqbDvJ7yup2Z_ZIze5l2VrgEVgNDrXvNoxXIA7XBOYh73Zc1p-AoxQvNxFQDUbpFY7x7NKmPLGgee9A0OCmFlhzsEhwol4VmJEKUP1qREjzMSN4wFGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 439K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 13:43:38</div>
<hr>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هم اکنون منابع محلی در اهواز گزارش دادند: ستونی از تانک های مدل T-72، متعلق به تیپ زرهی 92 ارتش در حال حرکت در بزرگراه آبادان و اهواز، به سمت آبادان مشاهده شده‌اند و به نزدیک ترین نقاط مرزی می‌روند
@WarRoom</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/withyashar/20240" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش انفجار در شاهاباد، اسلام‌آباد غرب ، استان کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/20239" target="_blank">📅 13:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری سی بی اس : آمریکا در حال بررسی یک خاموشی گسترده در تهران هستش که باعث عدم جابجایی گسترده موشک ها و تجهیزات نظامی همچنین از کار افتادن برخی پدافند های پیشرفته ایران میشود ، مقام آمریکایی فاش نکرد که این خاموشی گسترده ناشی از حمله به نیروگاه خواهد بود یا حمله سایبری
@WarRoom</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/20238" target="_blank">📅 12:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">براساس گزارش تحقیقی رویترز منتشر کرده، یک صرافی ارز دیجیتال، به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است. این صرافی یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به صرافی بایننس و فعالیت‌های…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/20237" target="_blank">📅 12:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش ویژه فاکس نیوز از فاز بعدی:
وقتشه رژیم رو تموم کنیم، عملیات پایان حماسی
@WarRoom</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/20236" target="_blank">📅 12:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شنیده شدن صدای انفجار در کویت @WarRoom
🚨</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/20235" target="_blank">📅 11:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرنگار نظامی خبرگزاری عبری‌ والاه:
یک نشانه دیگر از تشدید قریب‌الوقوع تنش‌ها در خاورمیانه... ایالات متحده خواستار احتیاط و هوشیاری و خروج شهروندانش شده و از آمادگی برای احتمال لغو پروازها و بستن فضای هوایی، از جمله اختلالات در ترددها، خبر داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/20234" target="_blank">📅 11:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرمانده قراگاه خاتم : ایالات متحده با سرعت فزاینده در مسیر ایجاد یک جنگ منطقه‌ای گسترده پیش می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/20233" target="_blank">📅 11:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ادعای کانال ۱۲ عبری:
نتانیاهو موفق شد ترامپ را متقاعد کند تا حملاتی را علیه بخش های انرژی ایران آغاز کند
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/20232" target="_blank">📅 11:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری ای‌بی‌سی نیوز:
دو مقام آمریکایی گفتند که برنامه‌ریزی برای حملات احتمالی به ایران به طور جدی آغاز شده است، اما این برنامه‌ها ممکن است در هر لحظه‌ای تغییر کنند.
یک منبع دیگر نیز گفت که حملات احتمالی با مقامات اسرائیلی مورد بحث قرار گرفته است، اما مشخص نیست که آیا اسرائیل به طور مستقیم در این عملیات مشارکت خواهد کرد یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20231" target="_blank">📅 10:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرگزاری صدا و سیما : منابع خبری از حمله پهپادی به کویت و وقوع انفجار در این کشور خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20230" target="_blank">📅 09:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات آمریکایی: ایالات متحده قصد دارد در اسرع وقت، احتمالاً در همین پایان هفته، حملات جدیدی علیه ايران انجام دهد. @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20229" target="_blank">📅 09:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات آمریکایی: ایالات متحده قصد دارد در اسرع وقت، احتمالاً در همین پایان هفته، حملات جدیدی علیه ايران انجام دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20227" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ممباقر قالیباف، رییس مجلس گفت: «در روز اول جنگ در ۹ اسفند، ما یک‌ساعت بعد از بمباران فهمیدیم که رهبرمان کشته شده است.»
او ادامه داد: «تا ما توانستیم سران قوه را جمع کنیم و لاریجانی هم بیاید، ساعت هشت شب شد، آن جا تصمیم گرفتیم اعلام خبر مرگ رهبری صبح فردایش باشد. بعد این جلسه هم سریع پراکنده شدیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20226" target="_blank">📅 09:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ساعاتی پیش سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از یک حادثه در فاصله ۱۱ مایل دریایی در شمال‌شرق لیما، عمان دریافت کرده است. افسر ارشد ایمنی (CSO) یک نفتکش گزارش داده که این شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به اتاق…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20225" target="_blank">📅 09:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em3bqRC4podHhaFQdT1NnhEZnJq0Q01JMw51ksCYFBFotdg2QaQ5ikAM1NDEkbBojD1XFgiFfWGLZEFeQgZoTYsIvBAApqYcjdodrQwdZU4fqJKiWS2ZYXHGXM31GQBdE2QfOyuPYnhuVri2St8G75ed-w2g9PEs4-PZtAtSrENEdgJACnohubhkejdy0LAIH821TA2am-fdqQW3ugv-dqe_4d6zbwnX7GVbAW8L-URuZ6T0EL-UWtl0aJD-NzmnnmA3uGSpXEV9JOlzq3yP9IOsMtT3AEV2faXzV7Mr5cONuQYBKridexWntyytHg9gOh2kgIGv0QnwblW6KH4VMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از یک حادثه در فاصله ۱۱ مایل دریایی در شمال‌شرق لیما، عمان دریافت کرده است.
افسر ارشد ایمنی (CSO) یک نفتکش گزارش داده که این شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به اتاق موتور شده است. این نفتکش در حال حاضر خارج از کنترل است و گارد ساحلی منطقه در جریان قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20224" target="_blank">📅 09:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا به فاکس نیوز : فکر نمی‌کنم رژیم ایران تا کنون با رئیس‌جمهوری مانند ترامپ مواجه شده باشد، چون واقعاً اقدامات را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20223" target="_blank">📅 04:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEObPe0WdDvc_dVBruFjk_K3iU6Doi5HeszEWWnNo6p2Np8x5nWkf-erM2MnSvKKaYtkMx3G2tHzYWIMO06t-2OQGlWC78fkKoub22OClISK2wbYV7mNzvKIJH-uzQsS9TXTHGctTD5IWyuvT__ZVkDUBMAITLPDRx_WGAOXzX_lUIn8WQuLnc4EiM1AU0jSLCHHDCa58traTiPoCRBYubhlrKYub2KOAGRTRoEY85xiyokMuQTWBMgPTfMwYC9Tn3mETFrtj6VPZnKcsqC5C-rkcY8GFT338XKrkohyxQXefwsuzX8jmF5evvqNPPEGfjOXWjirz1rBDqlfuIsWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7dee0280f.mp4?token=D9cpYrbeCWpwUPJK8HLYcWYqzJGPD9n5dag3MIw9fY8tF9pBsZFtmNIZtGrLsFEHWINuA7q3EoSqePUsJuuNM7NJhUTMWqf_SvIDSWvw6lr3VpL5eqJqgoRG3tFCaKfVPgGaGCptnCoxos3qQPeQepI1RiejzMbLZDHvJ1winjx9iH6_OGRk4-t92P66Jj_RxmR8AHxmzTxJy0idDNzcwVI9d5L2aTiCNC3bbY42STYBy8IvMGXoNQNx1HK8QMHDxQbFd_e8sLNKbI__FsGhEkCnwKDeHB1A5kEWEYoV8fsbqNmifoc5SG3V5Bw9k9PBdz0o34R3Vh6KcHPkz0j7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7dee0280f.mp4?token=D9cpYrbeCWpwUPJK8HLYcWYqzJGPD9n5dag3MIw9fY8tF9pBsZFtmNIZtGrLsFEHWINuA7q3EoSqePUsJuuNM7NJhUTMWqf_SvIDSWvw6lr3VpL5eqJqgoRG3tFCaKfVPgGaGCptnCoxos3qQPeQepI1RiejzMbLZDHvJ1winjx9iH6_OGRk4-t92P66Jj_RxmR8AHxmzTxJy0idDNzcwVI9d5L2aTiCNC3bbY42STYBy8IvMGXoNQNx1HK8QMHDxQbFd_e8sLNKbI__FsGhEkCnwKDeHB1A5kEWEYoV8fsbqNmifoc5SG3V5Bw9k9PBdz0o34R3Vh6KcHPkz0j7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری i24news : ارتش اسرائیل با ۷۰۰ تن مواد منفجره ، شبکه تونل‌های حزب‌الله را در زیر کوه بوفور نابود کرد. @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20221" target="_blank">📅 04:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏وزیر خزانه داری امریکا: ‏"بزرگترین بانک ایران سقوط کرده است."
‏"دارایی های آنها را در همه جا مسدود میکنیم این پول به مردم ایران و آمریکایی‌هایی که توسط رژیم ایران آسیب دیده‌اند، خواهد رسید."
‏"بانک مرکزی مجبور شد پول چاپ کند، هزینه تورم را متحمل شد. اکنون آنها تورم ۱۸۰ درصدی دارند. آنها قادر به پرداخت حقوق سربازان خود نیستند!"
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20220" target="_blank">📅 03:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اکسیوس : یک مقام آمریکایی از دلایل تصمیم به حمله بزرگ آمریکا گفته است که ایران در روزهای اخیر «بسیار تهاجمی» عمل کرده و برخی مقامات آمریکایی از سطح بالای تشدید تنش از سوی ایران غافلگیر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20219" target="_blank">📅 03:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVZ2tSnwi-R4uAFKvIQ--0zQqg2e745Vy05T0dCfaztwwRO_VBZHwQxEZWlZInHIr8MjODB9HVb173F_5-0FDjt10_a29iPe20EyOcTw19VUEm99aPzUMnUBqRQMa3a_IIUCKaz8VCHXm6oJ2sfGazDUCLAZgCqUqCVHKjniZOHLRpYYmU8aItr8s4ueCtaE4znqsxzZH2Hrp92F0xUOVXSi9yhYwIW8RW_73Ry2MOKpcyrAWfty3wrtNJmu8oe9B0DlP_VQwXpuYTuJy_BpYtABpPr5mIiqFEp3ssHRhR_TYTzQmY5DQg55AwXuHWmBBM8xGAHP4mHGindncInCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، بعد از جلسه کمپ دیوید، عکس خودش را در این مکان با چهره خندان منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20218" target="_blank">📅 02:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سی ان ان : یکی از اهداف ایالات متحده، هدف قرار دادن سایت هسته‌ای کوه کلنگ عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20217" target="_blank">📅 02:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شنیده شدن صدای انفجار در کویت
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20216" target="_blank">📅 02:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20215" target="_blank">📅 02:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2lIMbwPuViomzJTgvyS5VmJuWmVRCO37w7uzXEBJOE9h31bTnl3bGxlHfoxS1IYMUC2XH6pOikdaFQjva4ZxCdZOOgxyUD6w6ni4sGMIlEDKCRJCWq_mQHQ_Jl5nmoyW07jvlwEEsG9IARug5JeLVTFklrPhu7kQzrommrTI9NW5WcngVlJpY2ZgXyrI5ACkG2IaSackpXuXa7F-G3jm0kfm-Qrlk9QGFrGiZBuNTZfokWZMAkIYVwOgGIxNxB8KCwLSQoS43zp_CB2w4oyoPaHpEvEHa7q25aL-Kjd4RUo2ZDDWUH4HBz7vFzj-xjz_1glMYDwXZxV9_pDIKaq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : با ترامپ دیدار داشتم، نمی‌تونید تصور کنید چه بر سر رژیم ایران میاد @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20214" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20213" target="_blank">📅 02:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تسنیم: یه آشی برا آمریکا پختیم که یه عالمه روش روغن داره
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20212" target="_blank">📅 02:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ادعای آکسیوس: اسرائیل نیز برای انجام حملات علیه ایران به ایالات متحده خواهد پیوست
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20211" target="_blank">📅 02:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فعلا پوتین سنگین کی یف اکراین رو داره میزنه
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20210" target="_blank">📅 02:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سی بی اس : مقام های ارشد آمریکا امروز درباره قطع کردن برق تو سراسر تهران گفت‌وگو کردن!
هدف از حمله به این زیرساخت‌ها، تضعیفِ توان تو ارائه خدمات و اداره موثر کشور عنوان شده...
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20209" target="_blank">📅 02:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مطمئن شوید که چنل تلگرام و اینستاگرام رو عضو هستید. در صورت قطعی اینترنت، تلگرام تنها پلتفرمی است که با ضعیف‌ترین اینترنت هم میتوانید اخبار را داشته باشید.
حتما چنل رو پین کنید تا بالا باشد.
🌐
@WarRoom
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20208" target="_blank">📅 02:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت جوریه که هر کسی بخوابه ممکنه سکانس پایانی رو از دست بده.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20207" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک مقام ارشد امنیتی ایران اعلام کرد:
ایران یک طرح جامع برای پاسخگویی در صورت حملات جدید آمریکا یا اسرائیل به زیرساخت‌های ایران، آماده کرده است، بر اساس این طرح، اهداف احتمالی شامل زیرساخت‌های حیاتی در اسرائیل و زیرساخت‌های انرژی آمریکا در سراسر منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20206" target="_blank">📅 01:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شبکه CNN: مقامات گفتند که ایالات متحده در حال برنامه‌ریزی برای انجام موج جدیدی از حملات علیه ایران در همین آخر هفته است.
دامنهٔ دقیق حملات و اهداف احتمالی مشخص نشده است. هر دو مقام آمریکایی هشدار دادند که تا زمانی که حملات آغاز نشوند، امکان لغو آنها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20205" target="_blank">📅 01:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مارک لوین : با ترامپ دیدار داشتم، نمی‌تونید تصور کنید چه بر سر رژیم ایران میاد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20204" target="_blank">📅 01:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رئیس اتحادیه کانفیگ فروشان : ما با تمام قوا آمادهیم و سرورهایمان را تمدید کردیم.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20203" target="_blank">📅 01:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سی بی اس :  آمریکا و اسرائیل در حال آماده‌سازی برای سخت‌ترین حملات بمبارانی علیه زیرساخت‌های انرژی ایران هستند ، حملات ممکن است از همین الان (آخر هفته) شروع شود اهداف شامل نیروگاه‌ها و پالایشگاه‌هاست اما ترامپ هنوز دستور نهایی صادر نکرده ، اسرائیل با آمریکا…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20202" target="_blank">📅 01:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اکسیوس: یک مقام آمریکایی می‌گوید ترامپ به طور جدی در حال بررسی حمله به اهداف انرژی ایران در عرض چند روز آینده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20201" target="_blank">📅 01:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کاخ سفید: تهران تفاهم نامه را نقض کرده است، بنابراین رئیس جمهور ترامپ بیکار نمی ماند و پاسخ حملات و اقدامات ایران را می دهد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20200" target="_blank">📅 01:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us4j7vgOyMUaXpEYvYLBXqpt5cA5b-FU3go2j5YKHpoq0RHqB73iM8TACeb4Y1kpLlJnXIQTUHu-NuZG-XXus_8CTZSrxqJ2mcTE9ktYfAduMiXpjdb76y8fVj2I4kD2e8JeRvGSAS5fjk2rix0CEMqBfou2fO4TTPR9tRPlEQNEZ0uaBM5vxdjnCKw4_9UDW3rRgyWFd-IiqrMKLedhf2ra2hj87vW0IdnaohNEsy7sN95UHWVznKos9Q3NVMdCALf7T2SmUiWDqHMaUYBMGaNwzQdUt_MP-DsFLqj47cezvskKOs4_QFCQkX8Z6ycGun9LO9-mX8-l1N-wRUMlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت جورنال: رئیس جمهور ترامپ دستور اجرای مجموعه‌ای از حملات را در طول تعطیلات آخر هفته صادر کرد تا تهران را مجبور به تسلیم شدن کند. @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20199" target="_blank">📅 01:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اتاق جنگ با یاشار : تیک تاک ، تیک تاک ، تیک تاک  بینگ ، بینگ ، بینگ ، بینگ @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20198" target="_blank">📅 01:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اتابکی : بیاین دیگه ، بیاین ….
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20197" target="_blank">📅 01:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سخنگوی پنتاگون: وزارت دفاع آماده است تا در هر لحظه دستورات رئیس‌جمهور ترامپ را اجرا کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20196" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jangal bedoneh risheh (iG @yashar)</div>
  <div class="tg-doc-extra">siavash ghomeishi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/20195" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20195" target="_blank">📅 01:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار شبکه i24 news: همزمان با انتشار گزارش‌هایی درباره آماده‌سازی برای حمله به اهداف مرتبط با بخش انرژی در ایران، یک منبع آگاه از این گفت‌وگوها به من گفته است: «رئیس‌جمهور دیگر صبرش را از دست داده است. این حمله می‌تواند رژیم را در آسیب‌پذیرترین نقطه‌اش هدف قرار دهد. تصمیم نهایی در آخرین لحظه گرفته خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20194" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتاق جنگ با یاشار : تیک تاک ، تیک تاک ، تیک تاک
بینگ ، بینگ ، بینگ ، بینگ
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20193" target="_blank">📅 01:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وال استریت ژورنال:ترامپ در جلسه امروز تیم امنیت ملی خود در کمپ دیوید ، دستور حمله نظامی جدید آمریکا به ایران را صادر کرده است @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20192" target="_blank">📅 00:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سی بی اس :  آمریکا و اسرائیل در حال آماده‌سازی برای سخت‌ترین حملات بمبارانی علیه زیرساخت‌های انرژی ایران هستند ، حملات ممکن است از همین الان (آخر هفته) شروع شود اهداف شامل نیروگاه‌ها و پالایشگاه‌هاست اما ترامپ هنوز دستور نهایی صادر نکرده ، اسرائیل با آمریکا…</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20190" target="_blank">📅 00:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سی بی اس :  آمریکا و اسرائیل در حال آماده‌سازی برای سخت‌ترین حملات بمبارانی علیه زیرساخت‌های انرژی ایران هستند ، حملات ممکن است از همین الان (آخر هفته) شروع شود اهداف شامل نیروگاه‌ها و پالایشگاه‌هاست اما ترامپ هنوز دستور نهایی صادر نکرده ، اسرائیل با آمریکا هماهنگ است اما مقام اسرائیلی می‌گوید از تصمیم قطعی مطلع نیست همچنین بحث‌هایی درباره پایان قبل از باز شدن بازار دوشنبه وجود دارد،این طرح در جلسه کابینه کمپ دیوید مطرح شد و برخی دستیاران کاخ سفید مخالفند اما پنتاگون اعلام آمادگی کامل کرده همچنین بحث قطع برق تهران هم مطرح شد!
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20189" target="_blank">📅 00:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار اطراف اهواز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20188" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسپانیا: مهاجرین غیرقانونی به مال ها حمله کردن و در حال غارت کردن فروشگا های لوکس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20187" target="_blank">📅 00:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سنتکام : از زمان ازسرگیری محاصره بنادر ایران، مسیر ۳۰ کشتی را تغییر داده و مانع حرکت دو کشتی شده‌ایم
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20186" target="_blank">📅 00:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مجری : در مورد ایران، آیا ایده‌ای دارید - یک ماه، یک سال؟ چقدر طول می‌کشد تا آنچه اتفاق می‌افتد حل شود؟  ترامپ: همیشه سخت است. ما ونزوئلا را در کمتر از یک روز حل کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20185" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsvySuIl4lZlNLZHsW7bWrYNrkAaE1NExjSsbqytNkbszJR6lIqSxjnqEoUpgXFPtPGtYN6BttEcSJf7e28yxJ4soV6_5Z8hDYyf-cRXRRW3njqyUkozjko1FkZPA2XMR8-sNzdTIrRswjT3HoIGloEpzePuaTpz4OA0pbNxWlT7HsuMbLBHiV8ov3nEuT4R2GPX9gCo997Uk06NRGPD3q1BOBXVlOQn9Vq5nKeU2w0jRctGx2CpzD2X4_qWcDssxYBA9c35PPqIBmthJ3_H3-qqxk4CRl78Wyq7xUuUdRtaIvQ8zc695jkgFafx9Rp8SqfinNpUDmj5tpPRrd0TfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان اسکله پل بندرعباس
ارسال مهمات و تجهیزات به قشم
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20184" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش صدای انفجار غرب بندر عباس @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20183" target="_blank">📅 00:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb09e50276.mp4?token=eNmVM6OIItIWPBPbBdpub1eHhUAxVGVxA65qD1oNqoXPv7I1CeIMHZQaRFtssgGm8pzTMskHpktC2SE_XufwuYDIQodfMOZ6IdkyJOflItRc-Y7BIAoKWMewI-5YTpBp1JZvbDeuxbUgfDZ30YexjcRqyEcsghDv-25m1d0QJpmJMAD0PSdgd-wNnoXaHBcG5JfLsgvC9s6Pf_J83PRXgoMXEI2p4WmB1v82xuQm-yXMTWTI2pWuUD4lPPhra1ZDACKJNKscZY9iqrZt0ARfB5v7jZJp-TSzO8StLIxZDrKKiesr_ahcG3YcTw1AQ5yvW7ozkNgyCgIW_OdGnxiErw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb09e50276.mp4?token=eNmVM6OIItIWPBPbBdpub1eHhUAxVGVxA65qD1oNqoXPv7I1CeIMHZQaRFtssgGm8pzTMskHpktC2SE_XufwuYDIQodfMOZ6IdkyJOflItRc-Y7BIAoKWMewI-5YTpBp1JZvbDeuxbUgfDZ30YexjcRqyEcsghDv-25m1d0QJpmJMAD0PSdgd-wNnoXaHBcG5JfLsgvC9s6Pf_J83PRXgoMXEI2p4WmB1v82xuQm-yXMTWTI2pWuUD4lPPhra1ZDACKJNKscZY9iqrZt0ARfB5v7jZJp-TSzO8StLIxZDrKKiesr_ahcG3YcTw1AQ5yvW7ozkNgyCgIW_OdGnxiErw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: در مورد ایران، آیا ایده‌ای دارید - یک ماه، یک سال؟ چقدر طول می‌کشد تا آنچه اتفاق می‌افتد حل شود؟
ترامپ: همیشه سخت است. ما ونزوئلا را در کمتر از یک روز حل کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20182" target="_blank">📅 00:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار از دور در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20181" target="_blank">📅 00:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار سکنج کرمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20180" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حوثی های یمن
: ۸ نفتکش سعودی مجبور به تغییر مسیر شدند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20179" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ در مورد ایران:
می‌خواهید همه چیز سریع تمام شود؟
به دیوانه‌ها سلاح هسته‌ای بدهید.
خیلی سریع تمام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20178" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش صدای انفجار غرب بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20177" target="_blank">📅 00:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8900ed7e3.mp4?token=Bw4kRQijJzIH5LhuFnduXYKFwJu3RVdOeeOrHMtHCf387EL7yB_zPAkjjF1KmxO1DsqsLm6jiuqVgkgyUxS7d_JLyHUKf-ZXJMXARwSi5xOvCH4Lq2SACi5Ly7NNcIeTJQlKNHB-Zp6-xgoh4LFcLDJ3uikcVwpM3EcwPNARlnuvgJG055JZraHJg59yoE8NIcSyq6qVgBa3qLDD99tpi8wuFd0uVs1A1_CrOGCWPZI_tqUqkvjqd87P7tmChdFiS4BKmLHCjHWs4PkmoojC00wNIYmMCmIpsRak-ua3N3bkeqcLwQl2yWmxFZ_sX_U5xCUA1skyVj5KzQwuCdn-6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8900ed7e3.mp4?token=Bw4kRQijJzIH5LhuFnduXYKFwJu3RVdOeeOrHMtHCf387EL7yB_zPAkjjF1KmxO1DsqsLm6jiuqVgkgyUxS7d_JLyHUKf-ZXJMXARwSi5xOvCH4Lq2SACi5Ly7NNcIeTJQlKNHB-Zp6-xgoh4LFcLDJ3uikcVwpM3EcwPNARlnuvgJG055JZraHJg59yoE8NIcSyq6qVgBa3qLDD99tpi8wuFd0uVs1A1_CrOGCWPZI_tqUqkvjqd87P7tmChdFiS4BKmLHCjHWs4PkmoojC00wNIYmMCmIpsRak-ua3N3bkeqcLwQl2yWmxFZ_sX_U5xCUA1skyVj5KzQwuCdn-6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران
:
من در حال انجام کاری بسیار بزرگ‌تر از چیزی هستم که گفته بودم انجام خواهم داد.قرار بود وارد شویم، توان نظامی آن‌ها را از بین ببریم و بعد خارج شویم.
اما بعد متوجه شدم اگر این کار را انجام دهیم، باید نوعی حضور و نظارت مستمر وجود داشته باشد؛ وگرنه آن‌ها دوباره همه‌چیز را بازسازی خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20176" target="_blank">📅 00:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdg0cgFhVz1GjYJAgTDisSiir7PhtDd7Oe5SzrmID7H9LKw5vNPvqZS_6bM717Z7eBYAFjA8U7P7TJw1-aDdIvgEDtuvvORvhkNnfgChcxSnj_5H2rVwORrPU5dH2iGiVgIc3MGM2KHUS4JPPcVAU69-LWtj_Koxr9bCqvo2EUpEm2VsjXU9m2Q4RVaf9m9lX_xp-UwvR4DB4z4uC3pBrAUOHSw3VBJkTbCZqYnh1H0ud8upglc7u0TkoTG3EQZbQAC6KQmkGEgi_F2ELxmLzVd-aeLxvUdmI_8YVdKJZjT_z2wmrn2zuFaHIBzOf5sOJ6vosyekepoySYUsjsjbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس تحلیل داده‌های پروازی، دو فروند جنگنده F-35A Lightning II نیروی هوایی ایالات متحده آمریکا با کد دم LN و معرف پروازی TABOR71 و TABOR72 صبح امروز از پایگاه هوایی لیکنهیث (Lakenheath) بریتانیا به سمت خاورمیانه اعزام شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20175" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8Fm_qMgJOCri9tjp6wsaLmeWWXJN7lOWrgPKXQa1Cfujnf7Ijd4Kg12SicJuzaUVD_Odfn3YzLLZFRH-fuj1w72ZT6bDT_jb0SuDfOpDYKZz12NVR1KGrXrWiExwa8ZpqF-i9x0ny7bIu7YjhmPQnKi1M04CF8Ml_2xIBTgmAgQDq6t55P5frFXzAOLCqZcC4gzHke1WOtQvLrdTuhAo8Y-pN8fZMbT3ujo-0xp7Has_dDvDQMxAdjBA3UHp54Bu8Zr_HEN5rxAgYSLWZohsH-HJb232f0wBFoLKhIMzNfWg6D8eAnFydPz0CUimpDpQfXuR63Uvyf4M1EqdvE0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش فعالیت سوخت‌رسانی هوایی آمریکا در خاورمیانه همچنان ادامه دارد؛ طی ۷۲ ساعت گذشته دست‌کم ۱۲۲ سورتی پرواز توسط KC-135 و KC-46 ثبت شده (میانگین روزانه حدود ۴۱ مأموریت) که حداقل ۲۱ مورد آن در خلیج فارس و دریای عمان انجام شده است. این سطح از فعالیت نشان‌دهنده حفظ ریتم عملیاتی بالا و توانایی و آمادگی کامل آمریکا برای اجرای حملات دوربرد، گشت‌های رزمی و عملیات شناسایی بدون اتکای کامل به پایگاه‌های منطقه‌ای است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20174" target="_blank">📅 23:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b1ce5038.mp4?token=iP1eqVFS54puXydSQDBsaZpfxNTS2pm9E_Jk6-mkQm2-ePVviuZ5byNaR_7LQX4-ODuWt943k8A5TxlD3U53koleS9z_4p0TMhi7R2Vv_7VPzX2aMqA5tk9YYs4sZfpb9cRvmjua9jYWHYN_8byH-xXkI3_bjkph48QrkwQEl5VVYRBIvMHzPtYabnxJZlNFS_MqeV8K-UslxqewWXTD1Ck4dstPMMIIqQjN80g1HabQhlYnpK5iU2-CTxUByyDjoSnrRV-JmlwyXTLphbo_aEgWT1dmLFJsv1TyRMadxA1tT-tiBtUlcQaluzEfJ2TttabsjR28vkn9DvCZLxDUdlT9a15DKy1Qsl_TunSRh0IZsV1Gm1JmQ2ygubCMX8mSJ59zmiEntAtFUTTYO6CcgRYh0U2uIDHGa2KXgxXLQeZOVsuYwZujUe1icW-BQJrndFacwMUT0Cp-P1Tt95MYkiZJ1LG9B9TI28Z7IbtCDgHwqlB31RnJFKIAOZmkqejNXMdNX6fgGdOI0COkmra2XY6CO8BECM5YIGcS1QlIVoqBjtkVk0FMYCh6mb1u0LV25502lBaK5LiHDe44gx4IgwiyQ2B98xUuEA-IAX0W1kvut9UBONm1NmA2AmnM1dXbrvcySxczI6rkJlUSN7s-8U6JTt7cqqyAj7zXgX89xzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b1ce5038.mp4?token=iP1eqVFS54puXydSQDBsaZpfxNTS2pm9E_Jk6-mkQm2-ePVviuZ5byNaR_7LQX4-ODuWt943k8A5TxlD3U53koleS9z_4p0TMhi7R2Vv_7VPzX2aMqA5tk9YYs4sZfpb9cRvmjua9jYWHYN_8byH-xXkI3_bjkph48QrkwQEl5VVYRBIvMHzPtYabnxJZlNFS_MqeV8K-UslxqewWXTD1Ck4dstPMMIIqQjN80g1HabQhlYnpK5iU2-CTxUByyDjoSnrRV-JmlwyXTLphbo_aEgWT1dmLFJsv1TyRMadxA1tT-tiBtUlcQaluzEfJ2TttabsjR28vkn9DvCZLxDUdlT9a15DKy1Qsl_TunSRh0IZsV1Gm1JmQ2ygubCMX8mSJ59zmiEntAtFUTTYO6CcgRYh0U2uIDHGa2KXgxXLQeZOVsuYwZujUe1icW-BQJrndFacwMUT0Cp-P1Tt95MYkiZJ1LG9B9TI28Z7IbtCDgHwqlB31RnJFKIAOZmkqejNXMdNX6fgGdOI0COkmra2XY6CO8BECM5YIGcS1QlIVoqBjtkVk0FMYCh6mb1u0LV25502lBaK5LiHDe44gx4IgwiyQ2B98xUuEA-IAX0W1kvut9UBONm1NmA2AmnM1dXbrvcySxczI6rkJlUSN7s-8U6JTt7cqqyAj7zXgX89xzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند جنگنده اف-۳۵ با یک حادثه در پایگاه هوایی میرامار نیروی دریایی در سن دیگو، ساعاتی پیش آتش گرفت. تیم‌های امدادی حوالی ساعت ۱۰ صبح به وقت محلی به دلیل دود غلیظ به محل اعزام شدند. علت حادثه در دست بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20173" target="_blank">📅 23:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">روزنامه نیویورک پست، به نقل از دو منبع، از جزئیات بیشتر طرح دو هفته ای ژنرال براد کوپر فرمانده سنتکام گزارش داد عملیات بمباران گسترده و طولانی‌مدت علیه ایران تدوین شده است.
این عملیات، یک بمباران مداوم خواهد بود، برخلاف حملات محدود و شبانه‌ای که در دور قبلی درگیری مشاهده می‌شد، و از مهم‌ترین عملیات‌های نظامی از زمان آتش‌بس هشتم آوریل خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20172" target="_blank">📅 23:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20171" target="_blank">📅 22:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20170" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20169" target="_blank">📅 22:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نظرسنجی شبکه 13 اسرائیلی:
62 درصد از شهروندان اسرائیل به توانایی ترامپ در جلوگیری از پیشرفت برنامه هسته‌ای ایران اعتماد ندارند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20168" target="_blank">📅 22:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واشینگتن‌پست: ترامپ نباید به توصیه‌های جی‌دی ونس درباره جمهوری اسلامی عمل کنه.
به نوشته این روزنامه، تهران از مذاکرات برای خرید زمان استفاده میکنه و آمریکا باید فشار نظامی و اقتصادی بر جمهوری اسلامی رو ادامه بده و از ازسرگیری عملیات علیه ایران عقب‌نشینی نکنه.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20167" target="_blank">📅 22:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGv6SUdhLNSCrRH1IUnRu7Tnsha6rilBl06nbk_WiV2tUOXKMO8TixHH_6A4s2wBxZ4mR3hxJZNU5652WuxuQYx5JVVmy-USQScK47E_q232DqIHnLwQvFgeJHQSQghL1XG1dGwCNSjpTs6CA1Y8fTftQ3mHsonHWkEeMG6ipp4de__skkcrL7hdimVAMpTMTgGSgHz8E1cqH_mC1Rqfym5dMg7cmkeiiTrqWUHKil5GMs9L0j2XoRD03xpMxNih3-ihU2-1oxa81VV92gICuO7yoDNi6pynQ7SjxFqdkSJbkEc945LMwSNpDVYelAjCvlCIODSY1G1oswwPI217gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش تحقیقی رویترز منتشر کرده، یک صرافی ارز دیجیتال، به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است.
این صرافی یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به صرافی بایننس و فعالیت‌های استخراج بیت‌کوین و بانک مرکزی ایران مرتبط می‌کند.این شبکه قمار فارسی‌زبان که متشکل از بیش از ۲ هزار وب‌سایت است از جمله توسط
ساشا سبحانی و پویان مختاری
، دو اینفلوئنسر ایرانی تبلیغ و اداره می‌شود که ارتباطاتی در سطوح بالای حکومت ایران دارند. تحقیقات رویترز همچنین نشان داده است که سپاه پاسداران سال‌ها پیش کنترل بزرگ‌ترین وب‌سایت‌های قمار قابل دسترس در ایران را به دست گرفته و از آن زمان تاکنون از این وب‌سایت‌ها برای انتقال حدود چهار میلیارد دلار به خارج از کشور استفاده کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20166" target="_blank">📅 21:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d306e1b0.mp4?token=gOnoO7u0t967EAs1e9RKJYHx3IIZMbaic7fYXPfCAGiaRFYVrzoYYF5T37Jfz3KMvRfaRNQIB6mNPMWYdlzrAgxCBYgOeRVIA5nM0oJpY99L8NoKZS3DTCvtXP-CekqiRw1y25fv-mcIrRp1SJDmeipX7CyPFfkGeT0y3XBg-8tcR-cdJXjHb3JwXqd63J861SeUR7z9m9RBYwQcf38BdI6JMxV83ZjLiLuorrkB06B4VHyBBxu_BkGfiPH_7EzLye3yVwMOf6v1U_ZjWHBnngy-R6znMuZaltghI3uaJU1PIHy0SF3cVdYEMxVInDjagtC3UB4V2rI7ozxybzPwVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d306e1b0.mp4?token=gOnoO7u0t967EAs1e9RKJYHx3IIZMbaic7fYXPfCAGiaRFYVrzoYYF5T37Jfz3KMvRfaRNQIB6mNPMWYdlzrAgxCBYgOeRVIA5nM0oJpY99L8NoKZS3DTCvtXP-CekqiRw1y25fv-mcIrRp1SJDmeipX7CyPFfkGeT0y3XBg-8tcR-cdJXjHb3JwXqd63J861SeUR7z9m9RBYwQcf38BdI6JMxV83ZjLiLuorrkB06B4VHyBBxu_BkGfiPH_7EzLye3yVwMOf6v1U_ZjWHBnngy-R6znMuZaltghI3uaJU1PIHy0SF3cVdYEMxVInDjagtC3UB4V2rI7ozxybzPwVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: میدونید موشک هایی که ایران به سمتمون میندازه رو چطوری رهگیری میکنیم؟! اینطوری: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20165" target="_blank">📅 21:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vumot26EMyf-PoVSEwKXaPdmAInpfE2nfwatRuUyUVF38FCfXPH84c1cz9EOhKZ3juoUVOyogjgbs0ilcBxo_LrLC8ufcoRLEjdtZ98BfvtN72w1THo7K7XHMcR0NFtTbRuwgi9KUyHzc3Bh1kRjtPhZ0AHYmfSeWxpRmV-y0AUe06VyKXAXPRtLfcOtkQ99NgYqM99d6FnT5cluXyjMxM7e40SzG0suB1ah0Q3--2dfvt2DFuzNtwIBowvGbDR5hxz1LKfjNxDcTNZKSkMaQinc0zmIF3oFKEtKkYiBnKS4QHPpjBhWGknMFvBSh0BMcZK6rgWPZQziI1GOsWpDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای، روز گذشته یک ناو هواپیمابر آمریکایی(بوش یا لینکلن) در ۳۴۰ کیلومتری بندر چابهار ایران مشاهده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20164" target="_blank">📅 20:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c77f1bbbfa.mp4?token=P2n-1WWxg14tyHROg1-fpk8kqhLKYLEum--oVyzB7NryR3oP-FGmykXu1aLCxSHgTg6YPOYfOx3L2too1GQYXZf_j0sV2VHKDaLVDd1Vr3osY6q-MFUqC4Fu0U7lh8hg4Ht-fbSLejY0SESVOYeqWmXroM3gK-eibGK86n-AAg1OHKXWHxlxXkg-rJm1-op-3B1YL5s2qwpfwUOS0Ko6lLjDgCddrXfdDOmBRPC152QJW_kf04zrIzQAggtF1QLH2gassnX7Llcp9QBu1ZQUX3A09vv8MRIItftz5KAwpOpj_BsHAXs4lgcSuddS7yG2druBrNILbQ8eB8M4iVhwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c77f1bbbfa.mp4?token=P2n-1WWxg14tyHROg1-fpk8kqhLKYLEum--oVyzB7NryR3oP-FGmykXu1aLCxSHgTg6YPOYfOx3L2too1GQYXZf_j0sV2VHKDaLVDd1Vr3osY6q-MFUqC4Fu0U7lh8hg4Ht-fbSLejY0SESVOYeqWmXroM3gK-eibGK86n-AAg1OHKXWHxlxXkg-rJm1-op-3B1YL5s2qwpfwUOS0Ko6lLjDgCddrXfdDOmBRPC152QJW_kf04zrIzQAggtF1QLH2gassnX7Llcp9QBu1ZQUX3A09vv8MRIItftz5KAwpOpj_BsHAXs4lgcSuddS7yG2druBrNILbQ8eB8M4iVhwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید ایران هنوز برخی از توانایی‌های خود را حفظ کرده است. آیا آمریکایی‌ها باید برای این حملات پی در پی آماده باشند تا زمانی که ایران به سادگی قادر به حمله متقابل نباشد؟
ترامپ: آنها کمی قوی‌تر خواهند شد، شاید الان، اما ضعیف‌تر خواهند شد.بله، مطمئناً. شما همیشه باید هوشیار باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20163" target="_blank">📅 20:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f7a15aa5.mp4?token=ULZXH9lpXf7vPWSNUILHYhA4oPh_DeJa0UBjc87ildJoEjiHU8h2QHeOeaLDE2fzCUzXTldNzGxGt7RFTWAGfkMMdLu-SVTdXV5D6I0nMH4tr-eMvUshZ8s4kEzxaLXZvQNdoQDXFB9Ob4x4tHwriu2AU0q-JNvlEm0SeTbkOaA1f7woJjz-zr_aGU6EIv1Q-MSUKQwX6Pi8Fb3_LwrVZBJShuv8fOu9Wl4qVaXMhcmD1amp8nRDbYRmfVYoXSquyz1K2NOxhYkyIkqCRnW7EB590O6ORODtN8TFd40E_L-NoA5yJvn8ONnnAP0JsITFCLFsNENb7Oq-ol2dVDaksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f7a15aa5.mp4?token=ULZXH9lpXf7vPWSNUILHYhA4oPh_DeJa0UBjc87ildJoEjiHU8h2QHeOeaLDE2fzCUzXTldNzGxGt7RFTWAGfkMMdLu-SVTdXV5D6I0nMH4tr-eMvUshZ8s4kEzxaLXZvQNdoQDXFB9Ob4x4tHwriu2AU0q-JNvlEm0SeTbkOaA1f7woJjz-zr_aGU6EIv1Q-MSUKQwX6Pi8Fb3_LwrVZBJShuv8fOu9Wl4qVaXMhcmD1amp8nRDbYRmfVYoXSquyz1K2NOxhYkyIkqCRnW7EB590O6ORODtN8TFd40E_L-NoA5yJvn8ONnnAP0JsITFCLFsNENb7Oq-ol2dVDaksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران:
رادار؟ «رفته.» رهبرانشون؟ «رفته‌اند.»
و بعد جمع‌بندی نهایی: «همه‌چیز رفته.»
همه‌چیز... رفته. همه‌اش... رفته. رفته که رفته!
آخر هم با یک بالا انداختن شانه گفت: «البته، باز هم به جنگیدن ادامه می‌دهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20162" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f38497106.mp4?token=qPftiVh_-VAv33t_QPMSE1bgVBo8j3Nt3LHBAKb98SwwnZegyWoHrCsy-UEleycctEzrEinmlEMAu6ldDb0pFQYXj338NfiCyH-gXASOaAPmZXQQsA-4a9ptyGGS8b9OLuZYnH93Am-lSNImoEVOt1RDvbNA0GVe6HGjK8SNrwzKoGCMp7Kzlu5tzqEZNwlqm7255ROCdJz1K6Zo1Iy-HnEEAO7Q05ZmC2eabf7WnCpRlcv96xQbDGmu03TkjKB4RPddpMY5cBTTTxTptiqV5feNfxyoCYamTTNIuRInpqz_tZFOY2ljRetpuz0b9wbpIYArVhODi1qS8P9ip7H78g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f38497106.mp4?token=qPftiVh_-VAv33t_QPMSE1bgVBo8j3Nt3LHBAKb98SwwnZegyWoHrCsy-UEleycctEzrEinmlEMAu6ldDb0pFQYXj338NfiCyH-gXASOaAPmZXQQsA-4a9ptyGGS8b9OLuZYnH93Am-lSNImoEVOt1RDvbNA0GVe6HGjK8SNrwzKoGCMp7Kzlu5tzqEZNwlqm7255ROCdJz1K6Zo1Iy-HnEEAO7Q05ZmC2eabf7WnCpRlcv96xQbDGmu03TkjKB4RPddpMY5cBTTTxTptiqV5feNfxyoCYamTTNIuRInpqz_tZFOY2ljRetpuz0b9wbpIYArVhODi1qS8P9ip7H78g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
ترامپ: «هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20161" target="_blank">📅 20:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: موشک تاماهاک باورنکردنی‌ترین است - می‌توانید از یک درگاه عبور کنید، آن را از پنجره یک خانه عبور دهید.
هیچ‌کس چیزی شبیه به آن ندیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20160" target="_blank">📅 20:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ
: اگرچه نیروی دریایی، نیروی هوایی و پدافند هوایی ایران تا حد زیادی از کار افتاده و تنها توانمندی‌های ناچیزی برای آن‌ها باقی مانده، اما تلاش‌ها برای تضعیف بیشتر این توان باقی‌مانده همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20159" target="_blank">📅 20:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حقیقت یاب سنتکام : سپاه دروغ میگه !تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران آن را کنترل نمی‌کند. هزاران کشتی طی چهار ماه گذشته از این آبراه بین‌المللی عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20158" target="_blank">📅 20:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8367cad8.mp4?token=t6C3SP4RutXH8scC14ST5kHc-945jbri3BancosqioYlknxyrdWOEzleGwMUS1VR1kmQuJfYW_s_fe_igDrZhYCjWCfjb733rcWx_jDLIACQgc6gfFC9vNpYs196JeI7lEiXMS4h2qnjLkL3VIp5b3cjKO0yWX2oHheOJ9CWK6bZJHGHSHrvy2mbSrgSByhrw_CkfIBov9QrXWfcuMF0U0h0L1IFxx3nE8Y9N22hRnWVdVf_OHgfqQMltoCuUX9PvZBM58-5MzTkOsKR6TDi7cHc0AFKUUF07x8y6pqjl68eQqDGwdrQfU32xvTdkqL-yDjFcqVC7icU_WjG1SSUelvpKDwiHtvjwJO2Us2_cKsdKDKP7teAyK5sASdQjtJd2kxZwIKjcMnk7BX_Sq8FprouQXYM2fR3r5UwvoJT9qDOdArvUQSFL6UFkv42hKl1fZ3Z847x2w1skm2kGNDc7G01b0oOILhO9vkIUp0Era9LfLx5itn6tt16GslqDoGf0cW_JC1sjBNr5RB6jeOYWBWjC77AMfr6foJxwHXWs4aMfhMK8IMQxfQKqYRGzStbUtP8dq9z5WIJc3ZE44USuuc5mO3TocXc0fREpJO0BtE0blo0bzz3aNSMiVjj_RK5Wu7KM3oB2T_06FvVGta10PVRKpUcVBjpsFiUFJGdCzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8367cad8.mp4?token=t6C3SP4RutXH8scC14ST5kHc-945jbri3BancosqioYlknxyrdWOEzleGwMUS1VR1kmQuJfYW_s_fe_igDrZhYCjWCfjb733rcWx_jDLIACQgc6gfFC9vNpYs196JeI7lEiXMS4h2qnjLkL3VIp5b3cjKO0yWX2oHheOJ9CWK6bZJHGHSHrvy2mbSrgSByhrw_CkfIBov9QrXWfcuMF0U0h0L1IFxx3nE8Y9N22hRnWVdVf_OHgfqQMltoCuUX9PvZBM58-5MzTkOsKR6TDi7cHc0AFKUUF07x8y6pqjl68eQqDGwdrQfU32xvTdkqL-yDjFcqVC7icU_WjG1SSUelvpKDwiHtvjwJO2Us2_cKsdKDKP7teAyK5sASdQjtJd2kxZwIKjcMnk7BX_Sq8FprouQXYM2fR3r5UwvoJT9qDOdArvUQSFL6UFkv42hKl1fZ3Z847x2w1skm2kGNDc7G01b0oOILhO9vkIUp0Era9LfLx5itn6tt16GslqDoGf0cW_JC1sjBNr5RB6jeOYWBWjC77AMfr6foJxwHXWs4aMfhMK8IMQxfQKqYRGzStbUtP8dq9z5WIJc3ZE44USuuc5mO3TocXc0fREpJO0BtE0blo0bzz3aNSMiVjj_RK5Wu7KM3oB2T_06FvVGta10PVRKpUcVBjpsFiUFJGdCzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: چه کسی از دولت با ایران صحبت می‌کند؟
ترامپ: آن‌ها همیشه می‌خواهند صحبت کنند... استیو، جرد، جی‌دی و مارکو درگیر هستند.
گزارشگر: ایران می‌گوید مذاکراتی در حال انجام نیست
ترامپ: ممکن است مدت طولانی درباره هسته‌ای صحبت کنیم و سپس آن‌ها بیرون بروند و بگویند: «ما هرگز درباره هسته‌ای صحبت نکردیم...» آن‌ها فقط کاری می‌کنند که عصبانی شوم
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20157" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ درباره ایران : آنها هفت ساعت درباره موضوع هسته‌ای صحبت می‌کنند. من می‌گویم: چرا هفت ساعت؟ این کار را می‌شود در پنج تا ده دقیقه انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20156" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ درباره ایران:ما می‌توانیم به توافقی با ایران برسیم، اما من به تدریج اعتمادم را به آن‌ها از دست می‌دهم، زیرا آن‌ها دروغ می‌گویند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20155" target="_blank">📅 20:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار : طبق روال تمامی جمعه‌ها از هشت ماه پیش تا کنون، امشب بیداریم و نوشیدنیهای الکلی و غیرالکلی را نوش جان خواهیم کرد.
امروز بیشتر خاص است چون ورود ششمین ماه میلادی شروع جنگ هم است
@WarRoom
💥</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20154" target="_blank">📅 17:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر خزانۀ آمریکا به فاکس نیوز: محاصره‌ی نظامی و اقتصادی ایران متوقف نخواهد شد و ما در سراسر جهان به دنبال اموال ایران خواهیم رفت.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20153" target="_blank">📅 17:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌  اتفاقی راجع به ایران قرار است بیوفتد @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20152" target="_blank">📅 17:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌
اتفاقی راجع به ایران قرار است بیوفتد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20151" target="_blank">📅 17:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ در مورد اتفاقات اسپانیا:
واقعاً افتضاحه، ببینید وقتی آدم نادرستی به قدرت برسه چجوری یه کشور رو نابود میکنه. این تصاویر رو بخاطر بسپارید، اگر دموکرات‌ها دوباره به قدرت برسن همین بلا سر آمریکا هم میاد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20150" target="_blank">📅 16:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ امروز در بحبوحه تشدید تنش‌ها و ادامه جنگ با ایران، جلسه کابینه خود را در کمپ دیوید برگزار میکند. به گزارش رویترز، در این جلسه علاوه بر مسائل سیاست خارجی و جنگ با ایران، پیامدهای اقتصادی درگیری‌ها، به‌ویژه افزایش قیمت بنزین و نگرانی‌های سیاسی جمهوری‌خواهان…</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20149" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حماس در بیانیه‌ای اعلام کرد با مرحله دوم چارچوب آتش‌بس موافق است، اما تأکید کرد که فقط سلاح‌های سنگین (مانند راکت‌ها و موشک‌های ضدتانک) را تحویل خواهد داد؛ آن هم مشروط به خروج کامل اسرائیل از غزه، تشکیل کشور مستقل فلسطین، بازسازی غزه و پایان همه اشکال تجاوز.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20148" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0TWcKkr28z_bHsJYZ6N7GEvvqC2SlRSYv1YuDGZajR1rOHKwxU0tSMi0KmI0t1zcwSRd5-TS3BshCh23lznFLYqIQiMyoRl3FlbSHtpx4mZ59zkfU1FIB31OImSSi0f5SQpkjW0BMn5GP_VJSIPGWUjnFuDTRs7ien7zP4yrlzxMnwK46NhxaZ9d6jpcI9qEjRV5vvZn_3I3b4-mIYwqjkDw0zRUIT02nRMXxa3VoGKLh1ItZS4oJEjhZBiLFNLYNgb9UrLP45E7EFqAKwdFiOScO7VjwdJYkAFCyFW69pZ7FmsgPR1IU6MlO3b4AlQ6ks1v2KbbSwYn8GMKkxG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر سند محرمانه افشا شده از تعداد واقعی ثبت نام کنندگان در پویش جانفدا  که 8,311,811 نفر بوده و حدود 2 میلیون نفرشون نظامی و حدود 6 میلیون نفرشون بالای ۵۰ سال و ۸۸۵هزار نفر زیر ۱۲ سال دارند !
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20147" target="_blank">📅 15:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ امروز در بحبوحه تشدید تنش‌ها و ادامه جنگ با ایران، جلسه کابینه خود را در کمپ دیوید برگزار میکند.
به گزارش رویترز، در این جلسه علاوه بر مسائل سیاست خارجی و جنگ با ایران، پیامدهای اقتصادی درگیری‌ها، به‌ویژه افزایش قیمت بنزین و نگرانی‌های سیاسی جمهوری‌خواهان پیش از انتخابات میان‌دوره‌ای آمریکا، مورد توجه قرار گرفته است. این سیزدهمین جلسه کابینه ترامپ در دوره دوم ریاست‌جمهوری اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20146" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر دفاع اسرائیل ، یسرائیل کاتس برای بار هزارم : اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20145" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کويت: از بامداد امروز هدف حملات پهپادی ایران قرار گرفته‌ایم , خسارات فقط مادی بوده
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20144" target="_blank">📅 14:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJdeHmy4MxItKBBTmC5amGnKnKSAJv_Rs2zilEctnstZyVwHOy1kT1N26cfUhH6WX0IAgjaIBY1ULvvr8kzKZJI5aqYIhgqW7QJdKjitCWvNuAcFPbofO9Z1bP0H1v4RElVksrayBKPSlYlwuUrZmc7EnHrDVnMyp2ctY7NL3Bmpte_S9-02MK6Mc-2NKvGT0uSmGZEHisLrMlD4tHwpQIay80VFr6ENfI0DJI0gEFBtRKUmDLaQGD_NAxR7lFNAgNSvI8ETdmScajIdLsihoxoK8guQKibTVLTMLDOlRAW49V_ZW0eaJrJWD0AblwvDk3NaGRJSGikHlRwjDi66Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون تنگه‌هرمز یکی از کشتی های هدف قرار گرفته توسط سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20143" target="_blank">📅 14:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd52784122.mp4?token=fh7UCHtwssweu5naNBe-nCJWqmrp5Bd2sGysFzl7Tc4qIOK4kQPsnYdDtdvqZwevqWxF1wb88l38VRhYEgH4iSNG48c-GpgG9yY955dARyLjHj6QDKmrbuClCKzT63YfZOwC0wXC1av9iUnJ3pHWQ4VnDrivcZpoFW9UqC6eQ2QUMLqFtg0_hTwOhMs_d3HWHcrChgobWAvniaXz4cSFFPdX2HiStHfKdElOv4g38tvr6WYyLQuuG-ZdLULoLUnoa_9CZzUuPoVMl34l9gl3Tmav5-0Khov8XBC4ZzysOzNxnkauIh5XE1GZU5F7YIw3QomZTLHZOuabY1ZE_IESfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd52784122.mp4?token=fh7UCHtwssweu5naNBe-nCJWqmrp5Bd2sGysFzl7Tc4qIOK4kQPsnYdDtdvqZwevqWxF1wb88l38VRhYEgH4iSNG48c-GpgG9yY955dARyLjHj6QDKmrbuClCKzT63YfZOwC0wXC1av9iUnJ3pHWQ4VnDrivcZpoFW9UqC6eQ2QUMLqFtg0_hTwOhMs_d3HWHcrChgobWAvniaXz4cSFFPdX2HiStHfKdElOv4g38tvr6WYyLQuuG-ZdLULoLUnoa_9CZzUuPoVMl34l9gl3Tmav5-0Khov8XBC4ZzysOzNxnkauIh5XE1GZU5F7YIw3QomZTLHZOuabY1ZE_IESfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی آتش‌نشانی تهران: دود مشاهده شده در آسمان شرق تهران، مربوط به حریق ضایعات و فضای سبز در محدوده جاجرود است
حریق در دره است و آتش‌نشانان در حال اطفای آن هستند.
@WarRoom
یاشار : چیزی نیست بی بی داره آشغالارو آنیش میزنه تو دره دید نداشته باشه</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20142" target="_blank">📅 13:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085ee0b373.mp4?token=mrcwFFBLsVAenDCJZh4jzXNWEWs__C3REWmX_tg-g05i_QKh-6nWaoAktzi7dkAEHhvug-UWYRjYgMm7Cy1XnOakIR52IIAyqsNvynosBst4l7_528Vt1LBYq34W3ySgflYYdpT4RojMBHdWFaKo_fFg1YYJuwspKbsfYiCXpx72XULfOoM46nGELDP-HG8W5sf47xKQo8cgM-DzxM3J1T9mrSMSVUcEfHBe8FjlyTejDOVFh7qihlivJAxEaB2RXN2UjXPCw_FZr_e0yBB8Q_IE-YaH6KUUR4R6szJCOjXgMkM9YuwMxg9S5bGW9sStesfbifGzCCv6r7DEr2mlVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085ee0b373.mp4?token=mrcwFFBLsVAenDCJZh4jzXNWEWs__C3REWmX_tg-g05i_QKh-6nWaoAktzi7dkAEHhvug-UWYRjYgMm7Cy1XnOakIR52IIAyqsNvynosBst4l7_528Vt1LBYq34W3ySgflYYdpT4RojMBHdWFaKo_fFg1YYJuwspKbsfYiCXpx72XULfOoM46nGELDP-HG8W5sf47xKQo8cgM-DzxM3J1T9mrSMSVUcEfHBe8FjlyTejDOVFh7qihlivJAxEaB2RXN2UjXPCw_FZr_e0yBB8Q_IE-YaH6KUUR4R6szJCOjXgMkM9YuwMxg9S5bGW9sStesfbifGzCCv6r7DEr2mlVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران ستون دود بزرگ سیاه و غلیظ در پشت سد لتیان
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20141" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20140">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به گزارش تلگراف،
آمریکا و اسرائیل در حال بررسی گزینه‌ای جدید برای افزایش فشار بر ایران هستند که شامل «محاصره زمینی»
پس از ماه‌ها حملات و محاصره دریایی در تضعیف تهران است؛ این طرح بر اعمال فشار به همسایگان ایران از جمله عراق، پاکستان، ترکیه و افغانستان برای بستن یا محدودسازی گذرگاه‌های مرزی و قطع جریان واردات و صادرات تمرکز دارد، به‌طوری‌که به گفته یک مقام اسرائیلی هدف آن است که ایران عملاً از تبادل کالا محروم شود، با این حال ژنرال بازنشسته آمریکایی شان مک‌فارلند این سناریو را «تقریباً غیرممکن» توصیف کرده هرچند معتقد است در صورت اجرا می‌تواند فشار اقتصادی شدیدی وارد کند، ضمن اینکه احتمال دارد طرح مذکور بیشتر جنبه انحرافی داشته باشد تا توجه ایران را از اقدامات واقعی بعدی منحرف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20140" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20139">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcrpUkRAtXRf6A14qagPVRLXCSUABIU3ommc2PK59QwBbZGGwZFB9NP-v60VQ3_cq6RJt0bQARDEVbJ4FzAbJe06SGSyVCIPY-eJnAT4YdtIcMkZv4Hb_aoUmKMTPlPqgmjgKvVzK4yRgCjw6cTvCrn2rEfnELgkltIwtMGu2GQL-mSnJdBZAfGzkONNlwbeqjYhC9jnrDrkSOVhHt6kj6GDLrfzjjZjWABiDNXu-3U7PVcOcNMDVVHu-Fb4E73Lsocjn3d3hJNHFu17-6be_sKPgDN_2_PqC-y0_8CfTihkqUxfhvPYQ_C4wFqNXXaxnaB1-1CnX8QYae5RGiWDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر سوخت‌رسان KC-135R نیروی هوایی آمریکا با شماره 8017-63 پس از ماه‌ها سکوت، دوباره فعال شد. این هواپیما در پی برخورد مرگبار مارس ۲۰۲۶ بر فراز مرز عراق با تانکر 0347-60 با شناسه «ZEUS70» آسیب دیده بود.8017-63 که با کال‌ساین «RCH169» وارد منطقه شده و پس از فرود اضطراری در تل‌آویو (LLBG) زمین‌گیر شده بود، اکنون با شناسه جدید «RCH564» سیگنال داده و در فرودگاه بن‌گوریون فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20139" target="_blank">📅 13:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20138">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnCVTTZ1FTkjlSuATL70JTqkikTkona1mdxTENCzLisFMmHgHyQ6Zx2S5o1OBHyVLa7kAmvxmZ68biVmJC5DgCK-XyQOtUYllU65ZnTT9e1Mr5cn5E8R6lxfXwTtVKsXX4xysnFpwxcoVctXzpHjPZjTIgfVuQe4UBqbQBbqalS35jRI8FNYUdz4DHgE8MJcimb9mdGHfqqdiAi5NRP6vrHBnUNTX-QMDWmxYvnAW4FNGHfRfvflu4d6-FqHjVecwq5Ux8Vyw_jt9hLedCtAzS2kH-NGTS5-P_JYipJbffBBw78jkAPTlKoSA-ee2TSXFdsgcTOdAryYtaGS8PY8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اعلیحضرت شاهنشاه محمدرضا پهلوی و انور سادات، رئیس جمهور وقت مصر، هنگام تماشای یک  مانور نظامی در تاریخ 28 تیر 1355 در منطقه علی آباد قم.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20138" target="_blank">📅 13:02 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
