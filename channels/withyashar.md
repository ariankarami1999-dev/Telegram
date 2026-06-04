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
<img src="https://cdn4.telesco.pe/file/qegKs_oH9UrZBAiWNu7PKcQtxTfNNHILGM3gdaCLan3ZppQO-vG4P2GLsejpQPZUaJcF4kkq7WTfZq5xTEARqmqpkq-5tU0KJ3waPitG75qyz4gzipOxlzWgGXK7pmXaMGW_HVzPOWIxLxW2-GJEtiFLnuerOiqC_13OcVnZhY6u5YGybXQlPLGpBSLFqa7NF8GrOGx1tPvCB2LiTtd4TjUzqMOeLxL9oBAUs0o15p3pby2thxDoz3ykATkrNBi1YiTdcr8cYtwOQswxIyzGtzQJbn3Ppa3ErV6o9k6cwzuZ926j6szXsuWudU2Smnfsq6dz3Om0IcCP68Kh7TUbJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 288K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-13477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فیلم جدیدی که حمله هوایی آمریکا به پل B1 در کرج، ایران، را در طول جنگ نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/withyashar/13477" target="_blank">📅 13:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال ۱۳ اسرائیل: «کابینه امنیتی اسرائیل امشب ساعت ۱۷:۰۰ تشکیل جلسه خواهد داد»
@withyashar</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/withyashar/13476" target="_blank">📅 13:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وال‌استریت ژورنال : آخرین پیشنهاد ارائه‌شده از سوی ایران نتوانسته رضایت کامل دولت ترامپ را جلب کند و هنوز اختلافات اساسی بر سر برنامه هسته‌ای، سرنوشت اورانیوم غنی‌شده، رفع تحریم‌ها و آزادسازی دارایی‌های ایران باقی مانده است.
وال‌استریت ژورنال تأکید می‌کند که تماس‌ها و تلاش‌های دیپلماتیک همچنان ادامه دارد ، ترامپ همچنان به دنبال توافقی است که از دید او برنامه هسته‌ای ایران را به‌طور مؤثر محدود یا برچیده کند. در مقابل، ایران خواهان امتیازهایی مانند آزاد شدن بخشی از دارایی‌های مسدودشده و کاهش فشارهای اقتصادی پیش از پذیرش محدودیت‌های گسترده‌تر است.
اما مذاکرات هنوز زنده است و کانال‌های ارتباطی بسته نشده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/withyashar/13475" target="_blank">📅 12:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وال استریت ژورنال:
«ترامپ به مشاورانش گفته است که جنگ تمام‌عیار با ایران را از سر نخواهد گرفت، مگر اینکه نیروهای نظامی آمریکا کشته شوند.»
مقام‌ها می‌گویند حملات مکرر ایران فشار بر رئیس‌جمهور را افزایش داده و تردیدهایی درباره دوام بلندمدت آتش‌بس ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/13474" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انتقاد مارک لوین از تصمیمات جدید ترامپ:
جمهوری اسلامی شاید نیروی دریایی و نیروی هوایی قابل ‌اعتنایی نداشته باشد، اما همچنان سپاه پاسداران و یک رژیم ایدئولوژیک دارد که شکست نخورده است؛ ما ملت ایران را برای سرنگونی رژیم مسلح نکرده‌ایم. رژیم کماکان در حال شلیک موشک های بالستیک و پهپاد ها است و هنوز مشخص نیست این تبادل آتش بخشی از مذاکرات است یا نه؛ هرچند در نهایت، چنین مواردی قابل راستی‌آزمایی نخواهد بود.
به نظر میرسد ما از نابود شدن سازمان حزب‌الله لبنان ممانعت می‌کنیم؛ حزب‌الله، قدرتمندترین نیروی نیابتی رژیم ایران میباشد که در 40 سال گذشته آمریکایی‌ها را کشته است؛ همچنین حماس به جای خلع سلاح، در حال تجدید قوا است.
این وضعیت برای آینده و پس از پایان دولت ترامپ، نشانه خوبی نیست. من فکر نمی‌کنم چین کمونیست که بزرگترین تهدید برای ما است، تحت تأثیر قرار گرفته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/13473" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9960590f00.mp4?token=K2Cah7hF-thfU1--dyqz8X3_znMpaWKv0EpgYDPsJc1P6W8oN9nlPAvPpahXTmgolNN2PKM2dHshx3gXe6Hlw2mO7KyvoDhVNP6z0P7JVGOdduOyiLdczlbIv-84UHsUve4GRfQ0xCzAZRhPI_JmHO-KGWDSSgA1oEzWJHm1UhFB_Ty-N9huMwIEfrhw3KI3N5gwL1KRHhScUbawqjkqlbFDKfWH_qKhKNbaR8OsMFyIG9NuG3EpZlYwRKwOPAj1Mmr4q3C7GMEzYb5TzVzkFM4il6lEIwa2Kx-q90NKiYIg02HFiAwnWUKfMcHncPITyK46smADD2CgSkm0WdPppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9960590f00.mp4?token=K2Cah7hF-thfU1--dyqz8X3_znMpaWKv0EpgYDPsJc1P6W8oN9nlPAvPpahXTmgolNN2PKM2dHshx3gXe6Hlw2mO7KyvoDhVNP6z0P7JVGOdduOyiLdczlbIv-84UHsUve4GRfQ0xCzAZRhPI_JmHO-KGWDSSgA1oEzWJHm1UhFB_Ty-N9huMwIEfrhw3KI3N5gwL1KRHhScUbawqjkqlbFDKfWH_qKhKNbaR8OsMFyIG9NuG3EpZlYwRKwOPAj1Mmr4q3C7GMEzYb5TzVzkFM4il6lEIwa2Kx-q90NKiYIg02HFiAwnWUKfMcHncPITyK46smADD2CgSkm0WdPppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری نیویورک پست
: آیا آیت‌الله (مجتبی خامنه‌ای) همجنسگرا است
ترامپ: بله.
مجری
: واقعا
دونالد ترامپ: بله، و فکر میکنم خیلی احترام براش قائل هستند.
@withyashar</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/withyashar/13472" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">در مراسم سی‌وهفتمین سال به درک رفتن روح‌الله خمینی، پیام کتبی منتسب به مجتبی خامنه‌ای خوانده شد. در این پیام آمده است «نظام سلطه پادگانی به نام اسرائیل از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/withyashar/13471" target="_blank">📅 11:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@withyashar</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/withyashar/13470" target="_blank">📅 11:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
@withyashar
🥴</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/13469" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :  شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.  برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود @withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/13468" target="_blank">📅 11:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf4ERZuVaBlX5L_q2itKFSKkkWRo7AY01_XTs4XP4z7W2K-ckHync098xtZDhxYH14tuI5q6GSilkks21-Xi-gAU7BAMqOQE-r8K3lsJxD8YsUq54bvjk7VlxKpAjQRucctk55n3pjr_uS1I8RLkGxgjLPWVk5chrN78sCxw6lORkwNXNNSmJ9yKbxy2QkHh2CmbThHt93ls5hHM6781pLzLdFRHTsSm-gLSxKt5jdJLXy-uJgRpQM3l-JVAtSd3kMcqpLxlcHuDyR6_HklObSYIxNhVMa4LwfERzkXXC5mdt2nkhLgdlQmoo_zBHSD040iTBlfnO7rUPj9Dp8QJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد پیدا شد
@withyashar</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/13467" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/13466" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gILwgO078qvl3WodSlCbH14cggp99bRruauRbXWcXx3POUtiOMpyyuez-u10T2Ih4BvJa6XgsKd5cCHglbzq6nujGN68F9zhJoxMTZhj8ddP1jTGBteOZPWAuScRZYCP86KwcPj8FPBwZHOqMgej0scI82FCOEwfQClOkuymn9XU9kzuVmJHxqCnESJrQfZRq20fmBhrGW_t2AYKGSIqmnyTObkpsnVIg_LT_Cbq4HrIysMzunvhzhAmCXTKyqmCZqGzi-gwFYsB3CmevarekIzkH1rPJwzxEwlG7iVJhSkRhIODRohP_GTToFrRyRGydIF7alrlwuslzlZ3gxReVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/13465" target="_blank">📅 11:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مقام اسرائیلی: ایران تصمیم گرفته در صورت آزادسازی اموال بلوکه‌شده‌‌اش، بخشی از آن را به حزب‌الله اختصاص دهد.
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/13464" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جنگ ترامپ با ایران و اختلال در حمل و نقل نفت از طریق تنگه هرمز، ذخایر نفتی آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۴ رسانده است.
برای کمک به مهار افزایش قیمت سوخت، آمریکا میلیون‌ها بشکه از ذخیره استراتژیک خود را آزاد کرده و همچنین صادرات به اروپا و آسیا را افزایش داده است تا جایگزین عرضه از دست رفته خاورمیانه شود.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/13463" target="_blank">📅 09:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=ehEQhBdS60-b5rL0MoLo889NYf6SKbmgKPzSxlzMVn6VhpdWoiEBIw43fBp5HecLCobMoGeewuXEFx_QesUbbj-YvySSeGpqC4mxnH0tVQBBPSg7A0y2kCU6FwJp3eL9tn6ZQ_SB8EbmXDXdvCjynNd7Sr7jHq4gp00lxZJYin8hkkxrkLS0RbxMECEQrXnERHP4c0CYAxk3SYUBuhbXO6KjvdfRxfLTaFpFqaHKV0ze9HTxbYEu_WwgocimS13ASyZFvE_arKs_tctD1q_4XL4moMVH6lHwB2eespxAUZpRMpH19FPePWh57dIQRw79Xb3V1G6D_r_fjit_QfzuVTo7LMkt-XQuDdU4xGFy3jfME_LjT01oa1bqGL5zDR0U7YKkobTL2LGSFI_NTj8m4UrzkC1_cxEgv5YRs05xQ8mvkg2kzVmvLj1micUpF2Rg3vlh9IidEjin4jWFx0xxy7JY1Ml1_vrWWUSMGVngikqoOa9mBZ7gekQhFaU74UEJkES2FFnwY7qmQrhXyObblGXTlnQpvnjnYmcGvhuRN5_Sk3VGjTOswS-FmXkL45GYfvbfORZt1DSiupohmTFU-N3IdFbnZyixlUw6xORBIelmbycQxfIQ9cXmVj-UjIX4tz3nkkQCBjGti0yezTCNYXr26Fsqg5O-JgtqZ6uw-E8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=ehEQhBdS60-b5rL0MoLo889NYf6SKbmgKPzSxlzMVn6VhpdWoiEBIw43fBp5HecLCobMoGeewuXEFx_QesUbbj-YvySSeGpqC4mxnH0tVQBBPSg7A0y2kCU6FwJp3eL9tn6ZQ_SB8EbmXDXdvCjynNd7Sr7jHq4gp00lxZJYin8hkkxrkLS0RbxMECEQrXnERHP4c0CYAxk3SYUBuhbXO6KjvdfRxfLTaFpFqaHKV0ze9HTxbYEu_WwgocimS13ASyZFvE_arKs_tctD1q_4XL4moMVH6lHwB2eespxAUZpRMpH19FPePWh57dIQRw79Xb3V1G6D_r_fjit_QfzuVTo7LMkt-XQuDdU4xGFy3jfME_LjT01oa1bqGL5zDR0U7YKkobTL2LGSFI_NTj8m4UrzkC1_cxEgv5YRs05xQ8mvkg2kzVmvLj1micUpF2Rg3vlh9IidEjin4jWFx0xxy7JY1Ml1_vrWWUSMGVngikqoOa9mBZ7gekQhFaU74UEJkES2FFnwY7qmQrhXyObblGXTlnQpvnjnYmcGvhuRN5_Sk3VGjTOswS-FmXkL45GYfvbfORZt1DSiupohmTFU-N3IdFbnZyixlUw6xORBIelmbycQxfIQ9cXmVj-UjIX4tz3nkkQCBjGti0yezTCNYXr26Fsqg5O-JgtqZ6uw-E8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد.
@withyashar
😟</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/13462" target="_blank">📅 01:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=ERroE_uyBC8EKHmgrTUmigJGtxhGg4F5TbX-UHjimZ3EyWsPCVKpRqkuOr4HYHhsoRtvAMww_dnuArUP73Ux5iwBNh1i2QHqFyjf6M31k0-zd_yh8odiDU4gS7FLFLICAH8qu9px9ZyC1vWFbGQVJBRzNzPcBzUMJYIYIF1SDQ3CO1K1Fxt_k9bKKTK5CAPQRq23mKY38JVQk8ftmZCxQTlWA1FMUX5afuQjsxpEYL5oIOEAwRqgSlHYkZhdg0QTljbTRaobRp177rQpOFdDRp0tLrRmJx7hP3a7dEtgoWK5coFX-Hyd_novUhlOabe4xoUwa_CWqiiE6pNMLCzNPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=ERroE_uyBC8EKHmgrTUmigJGtxhGg4F5TbX-UHjimZ3EyWsPCVKpRqkuOr4HYHhsoRtvAMww_dnuArUP73Ux5iwBNh1i2QHqFyjf6M31k0-zd_yh8odiDU4gS7FLFLICAH8qu9px9ZyC1vWFbGQVJBRzNzPcBzUMJYIYIF1SDQ3CO1K1Fxt_k9bKKTK5CAPQRq23mKY38JVQk8ftmZCxQTlWA1FMUX5afuQjsxpEYL5oIOEAwRqgSlHYkZhdg0QTljbTRaobRp177rQpOFdDRp0tLrRmJx7hP3a7dEtgoWK5coFX-Hyd_novUhlOabe4xoUwa_CWqiiE6pNMLCzNPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
چهار جمهوری‌خواه به نفع آن رای دادند.
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/13461" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">داداش اون بحث خیلی طولانیه اون میشه زمان ریست فکتوری طوفان بزرگ ( که با داستان خیالی نوح میشناسید ) تا اینجا بدون که قبلش تمدنهای بسیار پیشرفته بود روی زمین ، باشه برای بعد از آزادی
😂</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13460" target="_blank">📅 01:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from00:30</strong></div>
<div class="tg-text">درود ولی من‌میرملاس لرستان رفتم اونجا دیوار نوشته هست‌مربوط به 12000 سال پیش</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13459" target="_blank">📅 01:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یاشار : دمت  آقا دایی ، مردی ، خواستم تکمیل کنم که عدد
۲۵۰۰ سال
به طور مشخص به
سابقه پادشاهی شاهنشاهی ایران
اشاره دارد، نه به کل تمدن ایران ،
تمدن در فلات ایران ۵۰۰۰ الی ۷۰۰۰ سال حتی بیشتر سابقه دارد
@withyashar
😁
🙌🏾</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/13458" target="_blank">📅 01:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
‏ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/13457" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دو منبع مطلع در مذاکرات به i24NEWS عبری:
مذاکرات بین آمریکا و ایران به دلیل اصرار ایرانی‌ها بر آزادسازی پول‌ها، «پول نقد»، از میلیاردهایی که مسدود شده‌اند، حتی در مرحله اول، متوقف شده است .
در روزهای اخیر، میانجی‌ها تلاش کرده‌اند در این موضوع مصالحه کنند اما ایرانی‌ها بر دریافت پول در همان مرحله اول، در چارچوب توافق کلی، قبل از انجام هر اقدام واقعی در میدان، اصرار دارند.
مقامات ارشد آمریکایی تأکید می‌کنند: در ابتدا پولی آزاد نخواهیم کرد مگر اینکه ایران گام مهمی در مسئله هسته‌ای و هرمز بردارد و همچنین توافق کلی بسیار معنادارتر باشد.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13456" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvpiD6NhnH-7mmLY2V9a6KWzJVrjl2tIebkimHhxa7RE-HvtHUjrLL1qmTXgseJJ4inMu122-GIS69mZsbQSy63srSlp2STXpbNpwHFxUpogu1xOYToGlPGTSuf8sNSueOflK-oMgkH6Ndg3e1X8nbZZSAL9fcipOPQB9OAVlvUmngBflS-EHF3nfSvMUWlOy4obXuVpd-NKzHS-6hj8FJcF3czy9jRw4-5Zpsfu05R82XN4vrGhb2OL2QE6170SXagGo8VFCHeiBFb66cGW6mmm3RSYViHvzO_KdjEFMc78OxahLEUNcVPzbeREeDepuv8hjDuNbBC5I_WHyZYRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات آمریکا
جمشید قومی
، شهروند دوتابعیتی ایران و آمریکا و مدیرعامل شرکت «فرار پرداز رایانه» در تهران را به نقض تحریم‌ها متهم کرده‌اند. طبق ادعای دادستانی، او طی بیش از یک دهه تجهیزات شبکه، امنیتی و رمزنگاری ساخت آمریکا را از طریق واسطه‌هایی در دبی به ایران، از جمله سازمان انرژی اتمی و وزارت دفاع، منتقل کرده است. همچنین متهم است حدود ۱۵ میلیون دلار درآمد حاصل از این فعالیت‌ها را به آمریکا منتقل کرده و با آن یک عمارت ۳۵ میلیون دلاری در کالیفرنیا ساخته است. در صورت محکومیت، با حداکثر ۲۰ سال زندان فدرال روبه‌رو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/13455" target="_blank">📅 00:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منابع العربیه: پیشرفت‌هایی در مذاکرات لبنان و اسرائیل حاصل شده است، اما هنوز توافق دائمی به دست نیامده است
اختلاف بر سر سلاح‌های حزب‌الله همچنان مانع اصلی هرگونه توافق بلندمدت است
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/13454" target="_blank">📅 00:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:
ما در واقع برای اولین بار با حزب‌الله صحبت کردیم. نمی‌دانستیم آن‌ها صحبت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13453" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ : تنگه هرمز فوراً باز می‌شه وقتی من یادداشت تفاهم رو با ایران امضا کنم
تنگه هرمز باز خواهد شد، مین‌روب‌هامون اونجاست
زیر آب هستن، خیلی خوبن، تکنولوژی‌شون فوق‌العاده‌ست
ما مین‌ها رو جمع کردیم، بیشترش رو پاکسازی کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/13452" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستان خواهش میکنم دایرکت جای کامنت دادن به مطالب نیست
😟
خدایا به چه زبونی بگم ؟ بفرستید برای دوستون و باهاش‌چت کنید ، به بچه آدمیزاد چند بار میگن</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13451" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرنگار
: شما هفته قبل گفتید آمریکا می‌ره داخل و مواد هسته‌ای دفن‌شده رو در هماهنگی با ایران بیرون می‌کشه. آیا ایران واقعاً با این موافقت کرده؟
ترامپ
: خب، بستگی داره داری درباره کدوم روز حرف می‌زنی. این چیزها خیلی هم بزرگ‌نمایی شده. من خودم هم اون رو یه‌جورایی بزرگ‌تر از واقعیت نشون دادم.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13450" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a531a29092.mp4?token=G-0LBpEib7Ul2FDagvzCOttCsX_l3hmLbj832sl3GqGfW8gNQbD4uHlMpiKRVaZudOQ_WFn1-I4xtj57WtXrDgtNz4OQseDNRAdqoFINnuw7ISBIsqDZ782-frnV4Uq2m1np8csdBvfCKZa4J251_J0vu7Blk7i7S4lUBTyrojOC3fWTfXow0e-bQ9o1rz9b1OqCPQxnu4hx3WIDKPW_dBBQbI_DEcuJ7Dr2ai-eP8p_x__1ma556G5XEqcLE-Z6Y_x7GHKv6u5pqip1NBaW7_QgenxaNGFetDm7frT-71UzrZkSQ-PuevrSRi8KYgPFFDE-i6kXGqbCbNLx4_sT8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a531a29092.mp4?token=G-0LBpEib7Ul2FDagvzCOttCsX_l3hmLbj832sl3GqGfW8gNQbD4uHlMpiKRVaZudOQ_WFn1-I4xtj57WtXrDgtNz4OQseDNRAdqoFINnuw7ISBIsqDZ782-frnV4Uq2m1np8csdBvfCKZa4J251_J0vu7Blk7i7S4lUBTyrojOC3fWTfXow0e-bQ9o1rz9b1OqCPQxnu4hx3WIDKPW_dBBQbI_DEcuJ7Dr2ai-eP8p_x__1ma556G5XEqcLE-Z6Y_x7GHKv6u5pqip1NBaW7_QgenxaNGFetDm7frT-71UzrZkSQ-PuevrSRi8KYgPFFDE-i6kXGqbCbNLx4_sT8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما می‌توانیم دو یا سه هفته دیگر ادامه بدهیم و همه را از بین ببریم. انجام این کار خیلی آسان است.
اما اگر بتوانیم چیزی را روی کاغذ بیاوریم و مکتوب کنیم که بدون کشتن همه، همان نتیجه را به دست بدهد، ترجیح می‌دهم آن راه را انتخاب کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/13449" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13448">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=G4NyzB478YdIJX7BynEGNbDmWtI9Qy9mRjXz1bWE1dYgpLIW3NzYf2t1v98ZamC3pgkKGY1HRapwfIq7hK5Au4EP6Pt9CWW5yzkq8MSI2yfB6u9mSk1vteE3aIMkyQj673VchVY45QUzPxq_U2OIebk-4UMm6sMPddrvRyxZxvreEr-IBBSM3xi6Xg_wEGNgMSLHA-M5BLCflt61saLN61zIuufLGbJYyf9NsjWD5rIL7K7ERDLax7Rxvsj97SYmUDBRNyf0ZEV2lzyqN4xN1yg-_cdfrgn9tJAKbJEK-w3FEjBRXyEtF7FWnnFPc7Niwuv3hcrmYc5yMvlvIUlh6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=G4NyzB478YdIJX7BynEGNbDmWtI9Qy9mRjXz1bWE1dYgpLIW3NzYf2t1v98ZamC3pgkKGY1HRapwfIq7hK5Au4EP6Pt9CWW5yzkq8MSI2yfB6u9mSk1vteE3aIMkyQj673VchVY45QUzPxq_U2OIebk-4UMm6sMPddrvRyxZxvreEr-IBBSM3xi6Xg_wEGNgMSLHA-M5BLCflt61saLN61zIuufLGbJYyf9NsjWD5rIL7K7ERDLax7Rxvsj97SYmUDBRNyf0ZEV2lzyqN4xN1yg-_cdfrgn9tJAKbJEK-w3FEjBRXyEtF7FWnnFPc7Niwuv3hcrmYc5yMvlvIUlh6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در آن بخش از جهان«خاورمیانه»، آتش‌بس زمانی است که شما به شیوه‌ای معتدل‌تر تیراندازی می‌کنید.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13448" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13447">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درباره حمله ایران به کویت:
برای هر چیزی دلیلی وجود دارد، و ما به آنها ضربه‌ای سخت زدیم... آنها کمی تحریک شده بودند؛ آنها در حال پاسخ دادن بودند.
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13447" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13446">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ : مذاکرات عالی پیش میره
می‌توانیم جنگ را دو یا سه هفته دیگر ادامه دهیم و همه را نابود کنیم اما ترجیح می‌دهم این کار را نکنم
هر اتفاقی ممکن است برای ایران بیفتد، و رهبری ایران سه بار تغییر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13446" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13445">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش انفجار‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/13445" target="_blank">📅 23:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13444">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:دیشب و پریشب به ایران حمله کردیم و ضربه سختی به آنها زدیم
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/13444" target="_blank">📅 23:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13443">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G25B1ggMkFyCqIKDtIefiWwyaar1kyIqWjoZU4rl9wXpZHlenpd03rvALIKB5BKJMq-dPafJsU8Q1mYdoWYnwtwaKBZW6h_wBfKX_5o5MO3LxOHwQKU_OExJTez1kvCYXQGzLNeq10PsQaixMwSyum4cU4gWcbeAZ8cDtrLKBMvFns9n00f6OuX5q-Hb44Ug2R7UCVv6Yg1xUf9OTLMsG2kMc0N709ATHidQcGUJDQyeuVJe4-kKtGBc2WtojioKnigv9HHIeyHB-RMV9KuQlRhHgSmL2ZNWtUKpxHRoqkjqjbrv3VwljS9oihaMYIUqWZ6KBEJOL_nCXnEOlFNFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات بین اسرائیل و لبنان به زودی به پایان خواهد رسید. به زودی اعلامیه‌ای از سوی ایالات متحده منتشر میشه.
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13443" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13442">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دفتر بازرس کل وزارت دفاع آمریکا در حال آغاز یک بررسی (بازبینی و تحقیق رسمی) درباره «عملیات خشم حماسی» (Operation Epic Fury) است؛ کارزار نظامی آمریکا علیه ایران که با هدف برچیدن تهدید هسته‌ای تهران انجام شد.
@withyashar
این آغاز یک بررسی یا بازرسی رسمی است، نه لزوماً افشای تخلف یا شکست.
Office of Inspector General (OIG)
نهاد بازرسی داخلی وزارت دفاع آمریکاست و معمولاً پس از عملیات‌های بزرگ نظامی، نحوه برنامه‌ریزی، اجرای عملیات، هزینه‌ها، تلفات، رعایت قوانین و عملکرد فرماندهان را بررسی می‌کند</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/13442" target="_blank">📅 23:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پدافند شهریار فعال شد
🚨
@withyashar
اینو دیگه دوستم اونجاست و وارده</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/13441" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13440">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCF0S8oEiy5c4EenUitpa5rxcweaCCqrpOPvqC9C-J-iDmIfq0dHrFO5c8LRxsYwS_UKQBUuigfkO7hTxEv4dVzNX6dMU89yyQLecKQu4EbDjMDB23XUZ0tsZ1kwrUY3kuSnDD-f27vqg2bvui6J3edfnTYlx1FYmuGir-19WMX9RfrzYnJX-lgEAPNlXnby-HTZ6pifjtWHdKMsoj4rbta_oruZ3oczTTtWlVo_mWtZCtqAyVPEQfW21s_0QZMoUWfAkbumskF0XBx54icMbqLu95FU4OToHsrl7sMi6MIQecZ1rSO47UzkOKAvulDPR8SL_wu3E8zdZSqRjVQrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بلافاصله پس از یکی از سرگرم‌کننده‌ترین شب‌های تاریخ آمریکا، یعنی مسابقات قهرمانی جهان UFC در چمن جنوبی کاخ سفید، به اجلاس گروه ۷ در فرانسه خواهم رفت. سوابق نشان می‌دهد که اگرچه در طول تاریخ طولانی و پرماجرای کاخ سفید، مبارزاتی در سطح بسیار پایین‌تر در این کاخ برگزار شده است، اما هیچ رویدادی حتی نزدیک به این، یعنی بزرگترین مبارزان جهان، قهرمانان جهان، برای مجلس عوام در نظر گرفته نشده است! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13440" target="_blank">📅 23:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13439">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت کشور بحرین به دلیل خطر احتمالی آژیر خطر را فعال کرد و از شهروندان خواست به نزدیک‌ترین مکان امن بروند.
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13439" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13438">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی ساعتی پیش یک ناو جنگی آمریکا را در دریای عمان هدف قرار دادیم @withyashar
🚨</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/13438" target="_blank">📅 23:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13436">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رویترز: رسانه‌های ایران گزارش دادند که تهران به یک کشتی نظامی آمریکایی که ادعا می‌شود حامل «مرکز فرماندهی و کنترل» بوده، هنگام نزدیک شدن به آب‌های سرزمینی ایران در خلیج عمان حمله کرده است
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13436" target="_blank">📅 22:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13435">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=teCDv7PhckqGEFHypB38QeNQMAoW1dVfdnQjDMxHPpEaCZQ9N5Q0OGpP0ymZUKLvPzAQemALVuthkh_mCa7gCMUWdeLnhch9OAWsvEEVHji9UPSPpRk_euN1KwX3xLpwdLyQszd-ADA2boxPFnc4Sn1FOjEGvcCW0TsEx8pEl88O9GI6hS1xosGWN_p0fUkzuv2AassDJLaw5dATdMoWpeF_8dOhLQWczSZ-HFv365e23SUVKbojUhJOM1iFbPThBDsKh1Y70soAl8sIPYoAs3W_LLQAopbs8mCEZrpvxqZRgJOKctvb0priT5dD2NnjYY5yRZ7U0Zm-qNSXKsLfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=teCDv7PhckqGEFHypB38QeNQMAoW1dVfdnQjDMxHPpEaCZQ9N5Q0OGpP0ymZUKLvPzAQemALVuthkh_mCa7gCMUWdeLnhch9OAWsvEEVHji9UPSPpRk_euN1KwX3xLpwdLyQszd-ADA2boxPFnc4Sn1FOjEGvcCW0TsEx8pEl88O9GI6hS1xosGWN_p0fUkzuv2AassDJLaw5dATdMoWpeF_8dOhLQWczSZ-HFv365e23SUVKbojUhJOM1iFbPThBDsKh1Y70soAl8sIPYoAs3W_LLQAopbs8mCEZrpvxqZRgJOKctvb0priT5dD2NnjYY5yRZ7U0Zm-qNSXKsLfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی امروز ویدیویی منتشر کرد که نشان می‌دهد ساعاتی پیش موشک‌های ضد کشتی از کنار ساحل به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/13435" target="_blank">📅 22:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13434">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الجزیره: ستاد فرماندهی مرکزی ایالات متحده ادعاهای ایران مبنی بر اینکه خسارت به ترمینال مسافربری فرودگاه کویت ناشی از موشک رهگیر آمریکایی بوده، را تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/13434" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13433">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad▪️</strong></div>
<div class="tg-text">سمت منیریه پدافند که داره میزنه
یه صدا انفجار ام اومد ۵دقیقه پیش</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13433" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13432">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پدافند تهران فرودگاه مهرآباد فعال شد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13432" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13431">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤬</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13431" target="_blank">📅 22:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13430">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فارس: نیروی دریایی ارتش یک ناوشکن آمریکایی که قصد شرارت رو داشت رو با موشک هدف قرار دادند  @withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/13430" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13429">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پدافند پرند فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13429" target="_blank">📅 22:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13428">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش هایی از پدافند غرب تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13428" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13427">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فارس: نیروی دریایی ارتش یک ناوشکن آمریکایی که قصد شرارت رو داشت رو با موشک هدف قرار دادند
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13427" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
بچه جنگ شروع شد
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13426" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omtngy-WWVw--j79bDvoB8FSXLB4IBSloNnBhMXKUVavsbCRxyZplvENrbF28mDPlpUwluI17l1gBzYDz5SLNd8CLIhItm5ExtlYonbs1vuZJOQBujgnZameuKklpb_W3PA9QKR-ukLR77jatSnD_udPAEnfuXEbP5ycbzDHnPIOfoC7aLXEgFkVyuWuTxieLZAtqz03e5bElTYMDnbnrluXQk8qiU7jnRcSLVDfbcPUnZuh9XJmOAmgoJh9HE4L0-zleV4ZhbeuQEgNng1St7x5_TiW9y_hA3AHVlqb6-xbaIiU2P13LgJCP2YlcWA20BTt-GJ0ZAP3lGSRlyNoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های داخلی آخرین عکسی که از حاکمان سلسله مموشیان در ایران کنار هم بودند را منتشر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/13425" target="_blank">📅 22:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اتاق جنگ با شما : پدافند شیراز ساعت ۲۲:۲۷ دقیقه فعال شد!
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/13424" target="_blank">📅 22:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تسنیم به نقل از عراقی: ایران آمادگی کامل برای ادامه جنگ برای مدت بسیار طولانی را دارد و ما از توانایی‌های نظامی لازم برخورداریم.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13423" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عراقچی: در حال حاضر هیچ روشی در مذاکره وجود ندارد، اما پیام هایی با آمریکایی ها رد و بدل می شود
دو روز پیش پیامی به آمریکایی ها مبنی بر لزوم توقف تجاوزات اسرائیل به بیروت فرستادیم
تماس ما با آمریکایی ها قطع نشد اما پیشرفتی در مذاکرات حاصل نشد.
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13422" target="_blank">📅 22:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0NQZwKTsMPbFJHnPuGzFX-fPfZx0WXWEUOCmpQDF6Wtrb8aa2ANHeQ8F15p54Bd5SZs1KyfQ11fjhtAcJliUuUw-xpCtg0rqQDLofPTaKSiSxUhXohg5OqlQ00n5hQnI2OhbOkI57bPYmVTynkHoCOl0dV0C0aWxFu16gOlaQNgeL2DXRnUtqn5bcOYJ6Ia25iGgWwTB9g_66CKqXge7IvistOcrHaJer5gT3aOq566AaAck-n5kRosIpudVWsJR5Vr37X1Iulfv09QyidmW4PaXqWrpXupUmcV3u4KfIdBrIEhcczM1PBFePwMGsBodjil4YXyuvF_sqjBKwJc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع خلیل زاده با ارزش نزدیک به ۱۰۰ هزار یورو؛ کم ارزش ترین بازیکن تیم ملی فوتبال ایران و یکی از کم ارزش ترین بازیکنان کل رقابت های جام جهانی فوتبال ۲۰۲۶ خواهد بود.
خلیل زاده همچنین با ۳۷ سال سن پیرترین بازیکن ایران و جز ۱۵ بازیکن پیر کل رقابت های جام جهانی خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13421" target="_blank">📅 21:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یکی از اعضای تیم مذاکره‌کننده ایران به خبرگزاری فارس: ما هنوز پاسخ خود به پیش‌نویس تفاهم‌نامه را به ایالات متحده ارسال نکرده‌ایم. ما وارد هیچ توافقی که لبنان را نادیده بگیرد، نخواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/13420" target="_blank">📅 21:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانال 12 اسرائیل :ایران پیامی به آمریکا فرستاد که هر حمله‌ای به بیروت منجر به شلیک ده‌ها موشک به اسرائیل خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13419" target="_blank">📅 21:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سخنگوی ۳پا : تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است
بررسی و تحقیقات ما در مورد اصابت ترمینال مسافربری کویت نشان می‌دهد، نیروی هوافضای سپاه هیچ شلیکی به سوی این هدف نداشته است و تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13418" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwS1Ig-pFvlWWx_oHjkVFPrsaYCvgd5BgRLpC27wHbf4gq_FWOCOSR4tkp3XjnzXlcfteQfJSK1ViyHAvSJ7dZd3cYUILkHmqyHd0auJNkbONu4oUhrGQn-G-Lgd7l_y0kynLX3JjWGFVSkEeQQEF7_1Ot_CYgQlG0al8GScrfvPQe-q_Z6dH1iUIpWAtFWBJMg154XaWEnXE1pzdr9FGmZT-mfZx7MBijOdrxMaVdAtMYHPy61VQJefubFLaOKGfnkosfR3KgcI1RIO_9MRQ4KUVp2pK8TkBJCZ3AuaFo8Kygwm6rt3wgqoC0BgFtuZ_i2W_Yo4nPsqPfMdYTNrDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :
شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.
برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13417" target="_blank">📅 21:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عضو تیم رسانه‌ای در تیم مذاکره‌کننده ایران: دلیل عدم موفقیت مرحله اول مذاکرات اسلام‌آباد، امتناع ایران از ورود به مذاکرات هسته‌ای بود
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/13416" target="_blank">📅 21:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو:
اسرائیل آماده است. نیروهای آمریکا آماده‌اند.
ایران با آتش بازی می‌کند.
@withyashar
شمام آماده اید ؟
😁</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13415" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13414" target="_blank">📅 20:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یعنی چی ؟  منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13413" target="_blank">📅 20:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromR</strong></div>
<div class="tg-text">یعنی چی ؟
منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/13412" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقامات اسرائیلی: تخمین زده می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/13411" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ادعای روبیو، وزیر خارجه آمریکا:
ما دیگر حملات مداومی در داخل ایران برای تضعیف ارتش آنها انجام نمی‌دهیم، زیرا جنگ «خشم حماسی» تمام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13410" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تکذیب شد
😃
🤣
خاک دوباره پس زد</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/13409" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/13408" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/13407" target="_blank">📅 20:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">sample : yourname.warroom</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/13406" target="_blank">📅 20:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه ایده جالب دارم ویس میدم …</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/13405" target="_blank">📅 20:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">https://www.instagram.com/reel/DZIVRzvuaUf/?comment_id=17892109731481781
به درخواست شما متن برای بانو نور هم کامنت شد</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13404" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدای مشکوک به انفجار از غرب‌ تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/13403" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با یاشار : ما الان با دو بخار مواجه هستیم، بخار هسته ای و بخار خامنه ای
@withyashar
پایان چالش رو اعلام میکنم
🙌🏾
🤣</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13402" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی در گفت‌وگو با شبکه اسکای‌نیوز با بیان اینکه از موقعیت مکانی ذخایر اورانیوم غنی‌شده ایران که در جنگ  سال گذشته هدف حمله قرار گرفت، مطلع است.
او ادعا کرد که این مواد همچنان در همان محل پیشین قرار دارد اما دسترسی به آن به‌دلیل خسارت‌های فیزیکی دشوار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/13401" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💩
تاریخ برگزاری آئین وداع، تشییع و خاکسپاری علی خامنه‌ای اعلام شد   ۲۰، ۲۱، ۲۲ خرداد؛ وداع در حرم امام‌ خمینی  ۲۳ خرداد؛ تشییع در تهران  ۲۴ خرداد؛ تشییع در قم  ۲۵ خرداد؛ تشییع در عراق  ۲۶ خرداد؛ تشییع و خاکسپاری در مشهد @withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/13400" target="_blank">📅 19:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">💩
تاریخ برگزاری آئین وداع، تشییع و خاکسپاری علی خامنه‌ای اعلام شد
۲۰، ۲۱، ۲۲ خرداد؛ وداع در حرم امام‌ خمینی
۲۳ خرداد؛ تشییع در تهران
۲۴ خرداد؛ تشییع در قم
۲۵ خرداد؛ تشییع در عراق
۲۶ خرداد؛ تشییع و خاکسپاری در مشهد
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13399" target="_blank">📅 19:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e72ba1695.mp4?token=b7ODzHM-OPASyl-qFnjUHHvjtn1QIHfI06GLDZRsVO72XOD9Z1YUQyHiPewRRSdvxJ2ILF5iQoR8Ic-r5beZzzFvk1jZ5UOxtLSv5B0w8FoDwOdbnpxz0Nf-71a7nP5q_dYyLLriQtG076COnq3my63ga0BKZik8_sFs0bT6yek1pXOMn1lL9R82wwfIZVMUdlSiTpvBmI3zEDRFnBZlaLGEqUftlQLEmDBi6zc8qT0IWqYl0qBd9Jx8VbqbFG26VEqTCp5cWierapehF7blUzLg5WOVL7A-SHUxTVaj95xYKbm7C1X0BKwQmBWvy7li1V-RhDfdpZxoY45Q_bSGiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e72ba1695.mp4?token=b7ODzHM-OPASyl-qFnjUHHvjtn1QIHfI06GLDZRsVO72XOD9Z1YUQyHiPewRRSdvxJ2ILF5iQoR8Ic-r5beZzzFvk1jZ5UOxtLSv5B0w8FoDwOdbnpxz0Nf-71a7nP5q_dYyLLriQtG076COnq3my63ga0BKZik8_sFs0bT6yek1pXOMn1lL9R82wwfIZVMUdlSiTpvBmI3zEDRFnBZlaLGEqUftlQLEmDBi6zc8qT0IWqYl0qBd9Jx8VbqbFG26VEqTCp5cWierapehF7blUzLg5WOVL7A-SHUxTVaj95xYKbm7C1X0BKwQmBWvy7li1V-RhDfdpZxoY45Q_bSGiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه عباس چپقچی:
نیروهای مسلح ما در حال انجام حملات دفاعی به سایت‌هایی هستند که آمریکا اجازه استفاده از آن‌ها را برای حمله به کشتی‌رانی غیرنظامی و نقض آتش‌بس دارد.
هر عمل خصمانه‌ای با پاسخی فوری و قاطع مواجه خواهد شد. تحریم‌ها و جنگی که نتوانستند به هدف برسند، با جنگ بیشتر به دست نخواهند آمد.
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13398" target="_blank">📅 19:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پست جدید پیج دوم شاهزاده کامنت رو گزاشتم
🙌🏾
ادامه میدیم تا جوابی بگیریم
https://www.instagram.com/p/DZILMCsFoyR/?img_index=1&igsh=ZmZzNTQ2NHMwN2x2
و این پست
https://www.instagram.com/reel/DZIOnXHRKuy/?igsh=MWkzYmpzN2pjMmgyYQ==</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/13397" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/13395" target="_blank">📅 18:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مجری: چرا نمی‌تواند آمریکا فقط تنگه هرمز را باز کند؟
نتانیاهو: خب، می‌توانید، اما به مالکان کشتی‌هایی نیاز دارید که ریسک مالی برخورد را بپذیرند. از نظر نظامی ممکن است، اما ساده نیست
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/13394" target="_blank">📅 18:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d25386882.mp4?token=NwvzwVYa5ZGFhw-9D5VA2t3X-heY-SNmK5lACQc1Xmg3qG4SJfUDJSsh70Eom0MoufQOmpvC2qfnzn8GvAB2t57eUyeINKBDNhjHpztYR8BkA6p6lDttW24dU7WlQDj7wpO0HnJfJsJVLHfcPnZFybSJS_P2J-adohhjxj4cMuCnHwngsZU-PQtxqeYzkydP3M05Yme61oBgOBN3saKMxHGSa8Pm10EXj5LZTEj6mWNmUS746trcJB_E6LlfnP2zY5cZ1Q37_M7p4-f4dbWPfh16FsLF8XgchH5tOvQ-FD3VoYDAGeRqazxrdHJbBZTbLlHctYOmaEki5COM_1H6gqjdzQ-XhXcfZA2_rPNQkbYceXN-KyIdSEmE3kcEXBByTL9VTkSPHYmoN3rUmYwUvTSzM7oTcCBCwFuKi1bQkYU7hThlYG7Cgt3wbBQ033kNzGirxusdMoEIE3bx57e0qDRMC-vyrMe5ZQ1v4oyffaIm-cARQKFlN-LeTPR0nEWzpl9stDRYsJQZ7ZN8E2CIzPeG7RO85VRSBCCTI3EET1KLVR-kVMJpdkLxP33jVDXZ4oxVaVPGLOCqZMGX3PGqYCiKfrzroKZMYUuyn6u0HHeOpIWeDWfUx-sAUk_SRjloyKHwnWcALX1YrNsIk2vOARCLDz39p6PoQBD52ZOhBU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d25386882.mp4?token=NwvzwVYa5ZGFhw-9D5VA2t3X-heY-SNmK5lACQc1Xmg3qG4SJfUDJSsh70Eom0MoufQOmpvC2qfnzn8GvAB2t57eUyeINKBDNhjHpztYR8BkA6p6lDttW24dU7WlQDj7wpO0HnJfJsJVLHfcPnZFybSJS_P2J-adohhjxj4cMuCnHwngsZU-PQtxqeYzkydP3M05Yme61oBgOBN3saKMxHGSa8Pm10EXj5LZTEj6mWNmUS746trcJB_E6LlfnP2zY5cZ1Q37_M7p4-f4dbWPfh16FsLF8XgchH5tOvQ-FD3VoYDAGeRqazxrdHJbBZTbLlHctYOmaEki5COM_1H6gqjdzQ-XhXcfZA2_rPNQkbYceXN-KyIdSEmE3kcEXBByTL9VTkSPHYmoN3rUmYwUvTSzM7oTcCBCwFuKi1bQkYU7hThlYG7Cgt3wbBQ033kNzGirxusdMoEIE3bx57e0qDRMC-vyrMe5ZQ1v4oyffaIm-cARQKFlN-LeTPR0nEWzpl9stDRYsJQZ7ZN8E2CIzPeG7RO85VRSBCCTI3EET1KLVR-kVMJpdkLxP33jVDXZ4oxVaVPGLOCqZMGX3PGqYCiKfrzroKZMYUuyn6u0HHeOpIWeDWfUx-sAUk_SRjloyKHwnWcALX1YrNsIk2vOARCLDz39p6PoQBD52ZOhBU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: ترامپ شما را «دیوانه لعنتی» خطاب کرد.
نتانیاهو: گاهی اوقات، مانند بهترین خانواده‌ها، ما این اختلافات تاکتیکی را داریم. همیشه راهی برای حل آن‌ها پیدا می‌کنیم.
می‌توانیم صبح با هم اختلاف نظر داشته باشیم و تا بعدازظهر اقدام مشترکی انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/13393" target="_blank">📅 18:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d950e42b.mp4?token=P4l5qQrKtmmt6f7n36tvnfSMhbZ7H6D1Wzjt4GULlo42IKZIIeVBLiQKmHjU5chZZ_M3cI2_zuXuA0f_h_4ymUuVZt9-EOvPcwGqMBYTAiRCzjFGW2GbWBgyzIn5qjCfD-cTuyAuR-KbxzqbMCw9eMn37vDtoN3pHbTp73GJzwJAQc8q93p_CzuW2lONtGqCXlrS4JmdWHyc4ywwgwg1dprlTQ36S2b8wd5oeqCy9f34NbB1jH7gmwrf4Kuy6srMcU7rE_ejdUB-H_4zDjfZ0DvwcJ2xKidQcH6aJeCrXYm1nuFQDB7Eya6kHCP4GbtchlaEX0_xZhZ3notkgfE4GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d950e42b.mp4?token=P4l5qQrKtmmt6f7n36tvnfSMhbZ7H6D1Wzjt4GULlo42IKZIIeVBLiQKmHjU5chZZ_M3cI2_zuXuA0f_h_4ymUuVZt9-EOvPcwGqMBYTAiRCzjFGW2GbWBgyzIn5qjCfD-cTuyAuR-KbxzqbMCw9eMn37vDtoN3pHbTp73GJzwJAQc8q93p_CzuW2lONtGqCXlrS4JmdWHyc4ywwgwg1dprlTQ36S2b8wd5oeqCy9f34NbB1jH7gmwrf4Kuy6srMcU7rE_ejdUB-H_4zDjfZ0DvwcJ2xKidQcH6aJeCrXYm1nuFQDB7Eya6kHCP4GbtchlaEX0_xZhZ3notkgfE4GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: مردم ایران خواهان روابط خوب با آمریکا هستند و خواهان روابط خوب با اسرائیل. این می‌تواند اتفاق بیفتد.
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/13392" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مجری : شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
بی بی : چرا این را می‌گویید؟
مجری: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
بی بی : این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند.
ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند و این تغییر نکرده است.
اما این اتفاق دقیقاً در لحظه‌ای که ما بخواهیم رخ نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/13391" target="_blank">📅 18:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو به ان‌بی‌سی: وضعیت در ایران تمام نشده، اما ضعیف شده است. ما و آمریکایی‌ها آماده‌ایم در صورت لزوم اقدام کنیم.
اگر تشدید تنش لازم باشد، آن را به ترامپ واگذار می‌کنیم و باز کردن تنگه هرمز از طریق نظامی امکان‌پذیر است.
ترامپ در حال بررسی چندین گزینه است و ما هر دو روز یکبار با هم صحبت می‌کنیم.
ایران هنوز با حذف مواد هسته‌ای موافقت نکرده است، اما فشار فزاینده‌ای وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/13390" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روبیو: سکوهای پرتاب موشک ایران آسیب شدیدی دیده‌اند که منجر به زوال قابل توجه قابلیت‌های آنها شده است.
ما می‌خواهیم شاهد تغییر در ایران و حکومت مردم بر آن باشیم و دیگر تهدیدی برای منطقه نباشد.
امیدواریم که ایران جاه‌طلبی‌های هسته‌ای خود را کنار بگذارد و حمایت از تروریسم در سراسر جهان را متوقف کند.
«عملیات خشم حماسی» به هدف خود یعنی شکستن سپر سنتی ایران و کشاندن آن به پای میز مذاکره دست یافته است.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/13389" target="_blank">📅 18:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روبیو: امیدواریم امروز بین اسرائیل و لبنان توافق صورت گیرد
وزیر امور خارجه ایالات متحده:
رهبران دولت‌های لبنان و اسرائیل در حال حاضر در مقر وزارتخانه ما برای مذاکره دیدار می‌کنند.
ما امیدواریم که جلسه امروز بین لبنان و اسرائیل به بیانیه و برنامه عملی برای مسیر امنیتی لبنان مستقل از حزب‌الله منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/13388" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiezQ7ZHZHl92zZCEUCct-dH66jVuD1zduaIUICo59dyK5gok7DhQaPt1mbgNFkLLVMZR6EJbxriBuABhz9ZlqOXET1MIpx1I_CbFxKa3PTLb4QHvFwOqKgO1K8VRghwl8odvrd7B_XNg8hWD6WBhDt89P4-aG-Se6FWamyv4EOBEUaNxTaeBBkmEQfvEnjFs14E267-Ghnlgk8pkQJAJn6YdDCAEl9qGmDcVkJiWEWBtSvnSuCG2-36SSfPYOH4Olu9gZU7uGFH1qkSMoTlyjyu2ZPGvWH6b3sg6znD6tDI_u5cGauu--3aoHeuUSHj017ceUpc9ebW8E6I0uoN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز: یک ابرتانکر VLCC برای اولین بار در چهار هفته اخیر، نفت خام را در جزیره خارک ایران بارگیری می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/13387" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وکیل شخصی نتانیاهو، مایکل رابلو، به عنوان بازرس کل دولت اسرائیل انتخاب شد.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/13386" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کویت در پاسخ حمله جمهوری اسلامی ، دو دیپلمات را عنصر نامطلوب اعلام و اخراج کرد.
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/13385" target="_blank">📅 17:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش کویت: ما 13 موشک بالستیک و 17 پهپاد رو شناسایی کردیم.
یک فرد هندی جان باخت و شماری از افراد زخمی شدن، همچنین خسارات مادی سنگینی وارد شده.
به دلیل حملات، امروز 5 بار آژیرهای خطر به صدا در اومدن.
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13384" target="_blank">📅 16:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">️بیانیه نیروی دریایی ایران:
فقط مسیر تعیین‌شده ایران برای تردد امن در خلیج فارس است / شناورهای متخلف هدف قرار می‌گیرند
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/13383" target="_blank">📅 15:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ : ما خیلی خوب با هم کار کردیم. من «بی‌بی» رو خیلی دوست دارم و همکاری خیلی خوبی باهاش داشتم
می‌دونی، ما تو شرایطی بودیم که اون نخست‌وزیر زمان جنگه و من هم رئیس‌جمهور زمان جنگ هستم
ولی در کل رابطه خیلی خوبی دارم. با هم خوب کار کردیم، نتیجه هم گرفته شده
همیشه هم همین‌طوره. بدون آمریکا اصلاً نمی‌شد انجامش داد، همه اینو می‌دونن. ولی ما تونستیم
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/13382" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdwITiT1Vy5Outdf07XFo4vV7-4npiP_ck4Nr-Tjal3e1wixWHi7Te1gbwHpDt7IQN6pbSa_m4S1yWVQeQRjtYEfIZWufZ3S8IEacl7ToBGHZcbNCyA70TWIMHWXLepPEj8_ExDdz_U25aQ0v9VVG3uxc6Pbbqkpsogvq7-iEOdQpxIiqWAfDC5-DOoetr-g9DBu5Not9Zm3O9aW_aComlGsmttUaZmYCh6c4H41iyxXrxKeE766H_Bflu6k8Gc2V_ElZsdaSNi-dvTt30_943RC1hkZY3VgE_Y7EPQ6Lj_h63z114OVHXcR9dnSzdTv56ayMyuKllv8zKkow403yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در پست جدیدی در تروث با تلقین حس مخفی‌کاری و چند چهره بودن در قالب جیمز باند مأمور مخفی شکست ناپزیر ظاهر شده
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/13381" target="_blank">📅 14:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyvSnw4_1bhcfG6JVA87o7y4sxw5MxLtV3ebZd-aIYjq3hBeTmfl2c0o1D_enM06G5teSW-QNjbTpp0M-JiR68zlIKl57PQUlZlrb5oOJOOxzYZKu0vwtlSEptFYh6yZ5Ipmbo_IemsQ7AoPiLmhsHPtOHEZksUWev0_P3E24H4WakJE5j5yUs5K46M3GaQE7jHg6h17YOcd_NBV3F6S23lXL-6enutYOWr5s3GnRFEA-RWMy1Xg6x9KMZOJk_1yKZQPFYNCuI_8odMiSp-b0U3SbetvavHwrAECgDg-4Fx7eYnDBADQGQ4cPvmCIyeGcrNF_fcDtlZIbwaZR_seVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان تحرکات سنگین دارن
جهیزیه را میارن
🎉
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/13380" target="_blank">📅 14:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:  من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم. دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود. هر دو بسیار با استعداد هستند. @withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/13379" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:
من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم.
دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود.
هر دو بسیار با استعداد هستند.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/13378" target="_blank">📅 14:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درباره ایران:
ما نیازی به حضور نیروهای زمینی نداریم. با بمباران، بخش زیادی از نیروی نظامی آن‌ها را نابود کردیم.
آنها نه نیرو دریایی دارند و نه نیروی هوایی همچنین سرباز‌ زیادی هم ندارند
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/13377" target="_blank">📅 14:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ایالات متحده به تازگی یک جزیره کلیدی ایران را بمباران کرد.
این یک تشدید تنش بزرگ است.
کینگ ترامپ با ملاها بازی نمی‌کند و آنها دارند متوجه می‌شوند.
اوضاع به سرعت در حال وخیم شدن است.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/13376" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
