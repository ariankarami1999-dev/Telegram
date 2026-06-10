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
<img src="https://cdn4.telesco.pe/file/qnH6093dB_hs3kqc-xb5tae1zdvzf8ZwKfmLvvu3f1cuy2soWhVY4ETnxN8aUCZujewDMFkJsTdLhXRfJYzyANT0so94L6_czv7SBgI0EcioNjzUS79gFwyPBmXEF2qVGtd56_U53fsuOTlrE1rO9oBUL7n_QCiqxvKMIt1Q9ehHhPjnvBVm2RrakBpY7Fdt-8WjVw_Rx-q10o_Ns4aFH-bNugGMvms0FEo-KXQPNNjkZ1pjIKpIbrgkC0ImQ4cU_f8CHObHXL8k5Km3Q3Si-8RQsPGOjiqq2zsFR7-XiF8THE8CsSRtP_zImB6Uazf_FfeNiW2g1GjlrDWGednmiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 14:36:43</div>
<hr>

<div class="tg-post" id="msg-441133">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
قالیباف: جنگ‌های تحمیلی اول، دوم و سوم به جهان نشان داد که مسیر فتح و پیروزی از دل ایستادگی و شهادت می‌گذرد. @Farsna</div>
<div class="tg-footer">👁️ 54 · <a href="https://t.me/farsna/441133" target="_blank">📅 14:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
🔴
قالیباف: با وجود شهادت فرماندهان و دانشمندان در جنگ ۱۲ روزه، نه حرکت علم و دانش در کشور متوقف شد و نه توان دفاعی و بازدارندگی ایران کاهش یافت.
🔸
فرماندهان شهید و دانشمندان کشور با سال‌ها مجاهدت و ایستادگی، نام خود را در حافظۀ تاریخی ملت ایران ماندگار…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/farsna/441131" target="_blank">📅 14:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/441130" target="_blank">📅 14:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/441129" target="_blank">📅 14:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad86abac7.mp4?token=vOg5B_luQMRmu3A3-auXhHOdWoNW950DXDqpq9C5zypEMCuXVOtQBdgXGV6WdZ-_x3FYRdRKx_OyyiJakyWOB1_h61DhAz0EF-ws5td5sIDRxINz5qBclfeCGEr6eYRwYfsN7bThKtgaOL41MkDGqZEoCK6BdljKDa9W76lr-ZE1t1MD8jPPqTrNyQMnDOj4vLHu1bONVpLKhbnoXtD5HxbKPyAFSzxAFxrLsrlf6midWpyRRQKP0Z6S4Awyf_inAX1duiQOLtI_KokLdHT_JgSLwmUG1rhxhGHXtl_RCLwSxKgoPw0TtN45O-enxM65y8mmNOB4fVZzQAryaKhi7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad86abac7.mp4?token=vOg5B_luQMRmu3A3-auXhHOdWoNW950DXDqpq9C5zypEMCuXVOtQBdgXGV6WdZ-_x3FYRdRKx_OyyiJakyWOB1_h61DhAz0EF-ws5td5sIDRxINz5qBclfeCGEr6eYRwYfsN7bThKtgaOL41MkDGqZEoCK6BdljKDa9W76lr-ZE1t1MD8jPPqTrNyQMnDOj4vLHu1bONVpLKhbnoXtD5HxbKPyAFSzxAFxrLsrlf6midWpyRRQKP0Z6S4Awyf_inAX1duiQOLtI_KokLdHT_JgSLwmUG1rhxhGHXtl_RCLwSxKgoPw0TtN45O-enxM65y8mmNOB4fVZzQAryaKhi7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: بررسی‌های ایران مبنی بر همکاری اردن با متجاوزان به کشور ما، تنبیه اردن را درپی داشت
🔹
این رویه شامل کشورهای هم‌دست خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/441128" target="_blank">📅 14:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
خسارت دشمن آمریکایی به تاسیسات آب‌رسانی سیریک
🔹
مدیرعامل شرکت آب‌وفاضلاب هرمزگان: زيرساخت‌هاى توزيع آب‌شرب شامل ۲ مخزن بتنى به حجم ۵۰۰ و ۲۰۰۰ متر مكعب با تأسيسات مكانيكى مربوطه مربوط به شهر كوهستك و ۱۰ روستاى بخش بمانى با جمعيت ۲۰ هزار نفری در پی حملات دشمن…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/441127" target="_blank">📅 14:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoP2gfh_TRBsuLckTbJrRsN3F2Wv9afzIYGAfrnScWvDvmE7ns_WL9QgfR8YUyLdn5ctUy1qjhHkw2AXNxxomCcGJmAcAOjdmocFF6bchX8gc1D6kbsEjOMezLSpHKKtbhNA_4-YVIMWqmpnSeLhmp95Oz9vVVOaHgBt2ED-G_AjlU6yd1OylixeYSoqYhrPxvsCcYf70H5DFoSw-BrvEagOxnZFfthNDaiWgncvvWyTLxrbYWiWP6VXVZuyJKY9KVsW1oDA-sLNXWd-h__DFUPX6rSc_cuRFgHNptztmbWX59sXkFo19QNYXN6rAWL70TmkM1VUw-BuD8MIQFArJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام آشیانه و انبار پایگاه‌ هوایی رامات دیوید بر اثر حملات موشکی شب گذشته ایران  @Farsna</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/441126" target="_blank">📅 14:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1117278651.mp4?token=In4IOJTWBhQGH0vF3M0D0TD9oFyVgCr9EPhPfFgibykPhWZHsyaDecPq8vLPRVaasSV1kiQIaJD_lR0YRZxM70OofdChfu1mPeI3Om1HdHFFxGYZpOQrrNKlYrzltoCwy6tU6kY9QEXBz6b8Pz4CViPn_OtjR99KlLsCtwqL5DM9ftP5w8mZR_TsZRermPObT6j9DCDXcVXi2gohSOERXUpKRIQVI-gKQeC8IzZMyCuscklk13FizztfZznZ1i04uTUi-a9g5P-Nl1-BQMSMv0gEWI37iKCNXjrRSW0sotwL0DTCK9ry8fTY7DQrnomFUD9R57lDtwlXf6PnKbmAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1117278651.mp4?token=In4IOJTWBhQGH0vF3M0D0TD9oFyVgCr9EPhPfFgibykPhWZHsyaDecPq8vLPRVaasSV1kiQIaJD_lR0YRZxM70OofdChfu1mPeI3Om1HdHFFxGYZpOQrrNKlYrzltoCwy6tU6kY9QEXBz6b8Pz4CViPn_OtjR99KlLsCtwqL5DM9ftP5w8mZR_TsZRermPObT6j9DCDXcVXi2gohSOERXUpKRIQVI-gKQeC8IzZMyCuscklk13FizztfZznZ1i04uTUi-a9g5P-Nl1-BQMSMv0gEWI37iKCNXjrRSW0sotwL0DTCK9ry8fTY7DQrnomFUD9R57lDtwlXf6PnKbmAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی حزب اصلاح‌طلبِ ندای ایرانیان: ایستادگی نیروهای مسلح در ماجرای لبنان هوشمندانه بود.  @Farsna</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/441125" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">️انهدام یک پهپاد متخاصم در آسمان خوزستان
🔹
یک فروند پهپاد متخاصم توسط شبکهٔ یکپارچهٔ پدافندی ایران صبح امروز در محدودهٔ روستای چال بلوطک شهرستان اندیکای خوزستان منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/441124" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9de031baa.mp4?token=QGCwv9M_pkj6YIHiwT2ujs3r1iOZK1RIQKwkMrgyn5VTmy6rRtEXHCidZgA3E-yjTgemcGrBr6As0N67eWyShQXeOJIWwZQGD_07SOS8sY-xAIb8QT-fiLUOeu6CKf0oMUH9ynA6Tv32hgIX4OedV8zyBgevArNTyN7eafsAAZ1hbOiUwvg_4gETktg9iLG9SeBqYYx9SNa1bkMDtNzsy3c3TzKMnrAKT3tE7Gu-lS448r2RyW-H2CROSJjFoIU9sFsuwIWdoKd2zG39xkrM1f147F3e_GwOtSJJ1VCC7mbkbhF1Nr94skRd03eWqQMULfmCSp1fCfcT9Mifr5QrxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9de031baa.mp4?token=QGCwv9M_pkj6YIHiwT2ujs3r1iOZK1RIQKwkMrgyn5VTmy6rRtEXHCidZgA3E-yjTgemcGrBr6As0N67eWyShQXeOJIWwZQGD_07SOS8sY-xAIb8QT-fiLUOeu6CKf0oMUH9ynA6Tv32hgIX4OedV8zyBgevArNTyN7eafsAAZ1hbOiUwvg_4gETktg9iLG9SeBqYYx9SNa1bkMDtNzsy3c3TzKMnrAKT3tE7Gu-lS448r2RyW-H2CROSJjFoIU9sFsuwIWdoKd2zG39xkrM1f147F3e_GwOtSJJ1VCC7mbkbhF1Nr94skRd03eWqQMULfmCSp1fCfcT9Mifr5QrxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هدایت‌های رهبر انقلاب پشتوانۀ اصلی مدیریت بحران‌های کشور است
🔹
دشمن که از مواجهۀ نظامی با ایران ناامید شده، تمام برنامه‌ریزی خود را بر ایجاد تفرقه و دامن زدن به اختلافات داخلی متمرکز کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/441123" target="_blank">📅 13:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6361ab1ac.mp4?token=K2l2cY62DsjW6iApYN8RYLwTtSHCQOPXzkUjbYhRvBqa7hnEVnbRqimEgjtstXeV07jScyPhtD6SqjFYToc8te9GlLRIkEgWHaG8Rq7uhDeOq5HU0YY7pVqFll-H43_JQ83nx1O_aageyiSTDUAg43OY0uOzifqvmTnl4dxYmNDe7_qTLDh3goUC9UsaAbRlVuEalklwPLWnPr_raZFqgyVSfBCp4AK4xkW5s9IkHCQt8AHPZH062BwfcTSN3HiCdWITh-rz0cnf52DDXeze2Ugdq2_kLiwGmL4bpi2OpxTxKCcpLbDyzjLF2bY2KvTjB84S1BBBzjJ4gWXW9qfusw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6361ab1ac.mp4?token=K2l2cY62DsjW6iApYN8RYLwTtSHCQOPXzkUjbYhRvBqa7hnEVnbRqimEgjtstXeV07jScyPhtD6SqjFYToc8te9GlLRIkEgWHaG8Rq7uhDeOq5HU0YY7pVqFll-H43_JQ83nx1O_aageyiSTDUAg43OY0uOzifqvmTnl4dxYmNDe7_qTLDh3goUC9UsaAbRlVuEalklwPLWnPr_raZFqgyVSfBCp4AK4xkW5s9IkHCQt8AHPZH062BwfcTSN3HiCdWITh-rz0cnf52DDXeze2Ugdq2_kLiwGmL4bpi2OpxTxKCcpLbDyzjLF2bY2KvTjB84S1BBBzjJ4gWXW9qfusw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: بررسی‌های ایران مبنی بر همکاری اردن با متجاوزان به کشور ما، تنبیه اردن را درپی داشت
🔹
این رویه شامل کشورهای هم‌دست خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/441122" target="_blank">📅 13:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a594dfda42.mp4?token=oRrBJaIrz3DgbtM661TJgtGV2Rixp4gc3o8qhwufFYAzQJGATbQthKO4z7s0WUpYsgTy3XNwcHNyTnLcZcJBtm3LcvjrqcYwAEDqZUdDU9JIf_GLMObrhILzTjJN8fs9Ng1gKd1eIvMzibSluv70P19QBr1qoeYZev05nQkwqk4Ihj9Gi-Smq6W7uAg3e97wF1FbTK0-26lXFJy9AuXKsfnT9ObWPhzVpsg6v9IcT-IcRh7t1AzG9mxjOiaKzBV_svtKlvxpf47pNX1eAhPA9c_VWkZ2yTj3adQ2-AkjpTfwRnI0NUeuhc3XNU6bUfgQkkx4zU_aJVIyiXBtNfUiVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a594dfda42.mp4?token=oRrBJaIrz3DgbtM661TJgtGV2Rixp4gc3o8qhwufFYAzQJGATbQthKO4z7s0WUpYsgTy3XNwcHNyTnLcZcJBtm3LcvjrqcYwAEDqZUdDU9JIf_GLMObrhILzTjJN8fs9Ng1gKd1eIvMzibSluv70P19QBr1qoeYZev05nQkwqk4Ihj9Gi-Smq6W7uAg3e97wF1FbTK0-26lXFJy9AuXKsfnT9ObWPhzVpsg6v9IcT-IcRh7t1AzG9mxjOiaKzBV_svtKlvxpf47pNX1eAhPA9c_VWkZ2yTj3adQ2-AkjpTfwRnI0NUeuhc3XNU6bUfgQkkx4zU_aJVIyiXBtNfUiVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: امکان ندارد دشمن یک کشور را با هواپیما و بمباران وادار به تسلیم کند
🔹
غزه با آن کوچکی را ۳ سال است که نتوانسته‌اند وادار به تسلیم کنند. ایران ما را هم قادر نخواهند بود و قطعا تسلیم نخواهیم شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/441121" target="_blank">📅 13:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441117">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=j2jUCW32xenfPfbBbNMkyd_JNDWQPt5sKhpTz27lNGmCKGXZuVxsTpRFayKPyDRe83hFh3psim-BknTDuwmvmdR6fwmH1OR_SyVKxv8OAFSBS-vl-SkyGvrePOwmocXkmbTY7mHhDSVzi68Qqybn1RB5nWwRTMSJ8XUQX3-JCuiLT2hr8UX8XTjuXK8_9vzvtLHJ7t6IzsZsG6uAPBqywIonK2ZII9GHaIDpLv6pbR_8g6Czt7iV2kkR9ZPbj8_ESFnNufTS36HTJg1VMw0T1W-4nnAYbstiAEPEwFViJHXd6HFOEnH2bN1_XEOtzFWvyuaZyEiO2d0LRF6Ox017uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=j2jUCW32xenfPfbBbNMkyd_JNDWQPt5sKhpTz27lNGmCKGXZuVxsTpRFayKPyDRe83hFh3psim-BknTDuwmvmdR6fwmH1OR_SyVKxv8OAFSBS-vl-SkyGvrePOwmocXkmbTY7mHhDSVzi68Qqybn1RB5nWwRTMSJ8XUQX3-JCuiLT2hr8UX8XTjuXK8_9vzvtLHJ7t6IzsZsG6uAPBqywIonK2ZII9GHaIDpLv6pbR_8g6Czt7iV2kkR9ZPbj8_ESFnNufTS36HTJg1VMw0T1W-4nnAYbstiAEPEwFViJHXd6HFOEnH2bN1_XEOtzFWvyuaZyEiO2d0LRF6Ox017uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدمهاجرت در ایرلند شمالی خانه‌ها و خودروها را به‌آتش کشیدند
🔹
پس‌از انتشار تصاویر حملهٔ یک پناهجوی سودانی با چاقو به یک فرد دیگر، اعتراضات خشونت‌آمیز ضدمهاجرتی در مرکز ایرلند شمالی شعله‌ور شد.
🔹
صدها معترض که بسیاری از آن‌ها نقاب بر صورت داشتند، در چند نقطه از پایتخت ایرلند شمالی که بخشی از بریتانیاست، تجمع کردند و در جریان آشوب‌ها یک اتوبوس، چند خودرو و یک ساختمان به‌آتش کشیده شد و ساکنان آن مجبور به تخلیه شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/441117" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441116">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0411677642.mp4?token=IuIyhbjQW3-Ii_GTZlevvodP8J9ZB9Ll0dBANByIdPMt5Rvkn0wC147g58kMKQYi9xj6NitEgZq3jFWnqrGYiHZ3ve-EOmSzqakSiJ1jnl0OrhwgJAlhW9C3ehwIUNhLMpjRSd9lpuFanr0kErUJG6q4Svv4rlaLw6hNPoAA5m0ELlhH6ikPE486yPDGd97E_o9XsS6l7wsGUwnjlYeL0QttLNQio4H9HEIC4IwZucWef5tG0r2kn9RIJBJZghcN0cjOHAKgIeqXqCnPldS9HwCaBzrHq4n-M3nPGwMbSwus7_HDrJmXX6pQ2UjUBywEbJDUe7UBMy0OcGCSsIZbbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0411677642.mp4?token=IuIyhbjQW3-Ii_GTZlevvodP8J9ZB9Ll0dBANByIdPMt5Rvkn0wC147g58kMKQYi9xj6NitEgZq3jFWnqrGYiHZ3ve-EOmSzqakSiJ1jnl0OrhwgJAlhW9C3ehwIUNhLMpjRSd9lpuFanr0kErUJG6q4Svv4rlaLw6hNPoAA5m0ELlhH6ikPE486yPDGd97E_o9XsS6l7wsGUwnjlYeL0QttLNQio4H9HEIC4IwZucWef5tG0r2kn9RIJBJZghcN0cjOHAKgIeqXqCnPldS9HwCaBzrHq4n-M3nPGwMbSwus7_HDrJmXX6pQ2UjUBywEbJDUe7UBMy0OcGCSsIZbbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید از حالت نه جنگ نه صلح خارج شویم
🔹
دشمن باید خواب این را ببیند که ما در برابر تجاوز آن‌ها کوتاه بیاییم.
🔹
وضعیت نه جنگ نه صلح برای کشور خوب نیست و باید این وضعیت را از بین ببریم.  @Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/441116" target="_blank">📅 13:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441115">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aba412f0f.mp4?token=gQctVdp1nYTbhQCzMp5tCcx_mxC4MkmWnrngd1F2UeK3w79MWMTqrG8xlwlQxxFYFphhmZRtc9shmEETEPGytvNOqvk5wuON2XN6Cif8AgEBDb5T6uVT-Q957LwrmoyepoKHrqByYPKNXCxeUb3w98YuSju_TVvGi9N-0LQWeg2ZVa8fD3T9auTxUm5fgIPenBfcZNlZDotSts7Zkn7ljnE-CbfMc-n9pc7EmxL8oHTVEeihl02joqyPA1lkHdnAzL_dRCLIUWK6B90jL4iNyVf0DVxtIxT2WbfM1FiHTFG4tbhUX1E0KF5l7rbUSjZSI7py9zryZx49mpowXMiNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aba412f0f.mp4?token=gQctVdp1nYTbhQCzMp5tCcx_mxC4MkmWnrngd1F2UeK3w79MWMTqrG8xlwlQxxFYFphhmZRtc9shmEETEPGytvNOqvk5wuON2XN6Cif8AgEBDb5T6uVT-Q957LwrmoyepoKHrqByYPKNXCxeUb3w98YuSju_TVvGi9N-0LQWeg2ZVa8fD3T9auTxUm5fgIPenBfcZNlZDotSts7Zkn7ljnE-CbfMc-n9pc7EmxL8oHTVEeihl02joqyPA1lkHdnAzL_dRCLIUWK6B90jL4iNyVf0DVxtIxT2WbfM1FiHTFG4tbhUX1E0KF5l7rbUSjZSI7py9zryZx49mpowXMiNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید از حالت نه جنگ نه صلح خارج شویم
🔹
دشمن باید خواب این را ببیند که ما در برابر تجاوز آن‌ها کوتاه بیاییم.
🔹
وضعیت نه جنگ نه صلح برای کشور خوب نیست و باید این وضعیت را از بین ببریم.
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/441115" target="_blank">📅 13:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441114">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbOa7Ke7Py77FXiofdpMWSzlc0ZH8C_7zsCtXiWsStx-FOMfwGYf0wi3jc784I8VUsH_SXm2hYdrW9pnDS0CFOmmNLTHScHRuLDeFe3xhRmfLuaVSdN6vWXiQGYMPmpIw7TA2CotYKGBp23QF7xxsybRtWKU6-kwnBB0ntQpcoi7_I09EHcIuh-GVmW4fQSZiMuMRIK7vz4Xmz2eh6sTMEw5HcWCF2s7f2DhlV88CWSUApVnuwwIg2Q5o2rUSKgBqRQ53tlEsf7XJeVuL1sRg8yzGyappInoMI7EkNoeNDk4HKhlSkmq2adpNjQ6kiPzkQfpkO7NCocrCPyEM2dKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکی تنگهٔ هرمز
🔹
سازمان تجارت دریایی انگلیس: گزارشی از حادثه در ۲۰ مایلی شمال‌شرقی صحار عمان دریافت کرده‌ایم. موتورخانهٔ یک نفتکش ‌آتش گرفته و خدمه در حال تخلیه‌شدن هستند.
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/441114" target="_blank">📅 13:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441113">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Rl2_W4uISLpe3TLHwrYkdLiOG3LWNgspcuUBfmlMQwLvT7T16Y7INp16GQZCgfT1zQ84Y5Ylpl8oMIehvCXGmw0kxlNAM7iwn6XrUAOYQBi9Zb_RS9C-BSlQELqR2x9c_YQ-n0ixM7VnbGeLjivaMWchxjqH6O73ocrZTtjM8W-ZLbKvwD-mdxXadPgF8w5Ki-EepjP6GYzz5frhByouts38HMS5RrQNMKQZut0aR8S_vGAFjr0VppBiMY5euoylvpJ_pcRHC0I9FTQnVg8HSgjs2yEpu1sFtxqihHhNKnTCtII7A8KrQXShAK9utGUNiyxLsO8ub9sXr_kiHyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«از سرگذشت» محرم امسال پخش نمی‌شود
🔹
نجفی سولاری، تهیه‌کنندهٔ برنامهٔ «از سرگذشت» در گفت‌وگو با فارس گفت که فصل جدیدی از این برنامه ساخته نشده و امسال تنها گلچینی از فصل‌های پیشین از تلویزیون پخش خواهد شد.
🔸
«از سرگذشت» با اجرای علی‌اکبر قلیچ، جزو برنامه‌های مناسبتی و گفت‌وگومحور است که محرم پارسال فصل سوم آن از شبکهٔ نسیم پخش شد و با سوژه‌هایی متنوع مثل شهدای جنگ تحمیلی ۱۲ روزه، توانست نظر مخاطبان تلویزیون را به خود جلب کند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/441113" target="_blank">📅 13:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441112">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
منابع عراقی از آتش‌سوزی گسترده در مرکز اربیل و شنیده‌شدن صدای انفجار در نزدیکی پایگاه آمریکا در اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/441112" target="_blank">📅 13:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441111">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e6704a05.mp4?token=uWJ_OpN5m2l81FJuvuOrZYknrdxih32M6x-BblbV0s7H8eA3cE_d9Myswqj2Z6nC0Z7Ft4o-zvLbv_ZklsWhZyRI74paE42D7S_cCLJy38BL0ZMk3_zlcc3e_nYRSsOMf0bVq0Px5DVDqkTTYw0bKsFbGYi8zT3ePQTnvjLH5s-Qhpw4hkj8xvetDJ-dL8d-6iGuG39iyXIZ1mNHr9U0UErMo5BdJRQqSGeIIEQH3xHRvz6yi6bkL-nxXngBiZSZZVK-fYbQzoYrbopiqcblOiGWzBAnf3EywiilViGOocilyHMQvLvhTY_YPryBPjwSZ1p1qow5WVGyyG2h163o0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e6704a05.mp4?token=uWJ_OpN5m2l81FJuvuOrZYknrdxih32M6x-BblbV0s7H8eA3cE_d9Myswqj2Z6nC0Z7Ft4o-zvLbv_ZklsWhZyRI74paE42D7S_cCLJy38BL0ZMk3_zlcc3e_nYRSsOMf0bVq0Px5DVDqkTTYw0bKsFbGYi8zT3ePQTnvjLH5s-Qhpw4hkj8xvetDJ-dL8d-6iGuG39iyXIZ1mNHr9U0UErMo5BdJRQqSGeIIEQH3xHRvz6yi6bkL-nxXngBiZSZZVK-fYbQzoYrbopiqcblOiGWzBAnf3EywiilViGOocilyHMQvLvhTY_YPryBPjwSZ1p1qow5WVGyyG2h163o0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبدالکریمی: جریان روشن‌فکری همواره در پی تعمیق شکاف حاکمیت و ملت بوده
🔹
عضو هیئت علمی دانشگاه: روشن‌فکران ما امروز از غرب‌زدگی به غرب‌پرستی رسیده‌اند. این جریان در یکی از مبتذل‌ترین دوران تاریخی خود قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/441111" target="_blank">📅 13:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441110">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxS0dIV57f1KraP76tXI1fWlvzUT_sbPgbWVqVg7fWdfXDTYHrsWvk7fZmgEu_OjJkCgRABJx6ASyrmyMyIyLtrnp3lAh8dfZKjtNIq06-YEV8GKzO_unP6sb23P8JHCzrlExPQv4T01SbvlZDng0DCNKIszd1vRLhMicOgeFZUUQac9pXoaZgT_UT0ZBcmXuASUrc-s_3tW4oo47utOOa7pT7JGbzWjdgfV_i12A_3W0O37oaa5pts0ySx8rlzRMGZNjmxPVWkgR-iUp-lHutqMUfH0_vXye0eU9NP5jZ-GVAGyfJZYSE2hVNgzrGKWPFxcJM3wVdF9p2UUpHe4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رِد بانک؛ با ارائه مجموعه‌ای جامع از سرویس‌های بانکی، سرمایه‌گذاری و هواداری فوتبال، تجربه‌ای متفاوت و یکپارچه را برای کاربران سراسر کشور فراهم آورده است.
🟢
در قالب طرح «رِدبانکی شو»، کاربران جدید پس از دانلود اپلیکیشن(دریافت از آدرس:
https://red-bank.ir/download
) انجام احراز هویت و افتتاح حساب، مبلغ ۱۰۰ هزار تومان هدیه افتتاح حساب دریافت می‌کنند.
🟡
همچنین هر کاربر می‌تواند با دعوت از دوستان خود از طریق لینک اختصاصی، به ازای هر افتتاح حساب موفق، ۱۰۰ هزار تومان پاداش دریافت کند.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/441110" target="_blank">📅 12:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
شمارش معکوس IPO فیروزه آغاز شد
شمارش معکوس برای عرضه اولیه
#وفیروزه
آغاز شد! در این ویدئو با رامین ربیعی، مدیرعامل گروه مالی فیروزه درباره چشم‌انداز این عرضه و شرایطی که فیروزه در آن عرضه اولیه می‌شود، گفت‌وگو کردیم.
00:40 - دو دهه اخیر فیروزه درخشان و سخت بود!
01:11 - تاب‌آوری و استقامت فیروزه ادامه‌دار است...
01:50 - ارزش‌گذاری فیروزه چگونه بود؟
02:17 - دارایی‌های ارزشمند هلدینگ فیروزه
04:00 - داشته‌های پنهان و ارزشمند گروه مالی فیروزه
03:58 - رکورد مشارکت در وفیروزه شکسته خواهد شد؟
🛒
شرکت در عرضه اولیه
«وفیروزه»
در تمام کارگزاری‌ها با ثبت سفارش خرید از طریق سامانه معاملات برخط امکان‌پذیر است.
💎
گروه مالی فیروزه
سرمایه‌گذاری، برای همه مردم ایران
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/441107" target="_blank">📅 12:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/441106" target="_blank">📅 12:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk-TumZ2Z8W5FZ6A4mvjryIsugsU8muffV4Fa9P27sX_kgjOI45KkJ6CE4M_ftnexDJvmGfXgxPM3LlzolVBMv80gABrHnhlFH43swA8weKvef7aPSnvEgyzJLo0qHbnEOLnAUCdQIwCJ_IBhraKuF-_BengTyUUmBGNogdiXpQ3o-Xi8je99UPtBo-Uth--RHBknJGpfWa7mBh0YTM9-N9BwI8pr6XqH5rYqV9q5nPuzfTfbDr_M9m9eL-QtHILIGikB8rPujNMtdrHKxKJ8TxhQmE1oBpqhu-XeFQEzGPK1HpuEJMNxLkVP7C8icpl7elQjMowDbamLBX6hr7Srw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس رکورد جدید زد
🔹
شاخص کل بورس در دقایق ابتدایی معاملات امروز با رسیدن به ۴ میلیون و ۶۰۲ هزار واحد رکورد تاریخی جدیدی را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/441105" target="_blank">📅 12:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f13cb69a.mp4?token=lozXPAIZzeNpVm40Io9uMm1GftcR2RqhlMEGEJ5sEDL1rdBy65w_R4LPVqEoblXnMouIvwU39IsCnCM7uQY_i-9jo5Eh7AKw_JxUz9jUZ2FDTdH7XXyhSW_2MXDEMSqNgucKAug2HIPUCIcz0kvFtHODZhvpTlsXwGPcTT-hLuEzelVGoV3-dcHrF7tgzjd73fU7nhLfmwGPst_qbnycm_EvZoHkNcjLjmSQ-iVg_cUL2FTffI5j7nwzLKkA9AyFlcRAsFqT9yYVcUpdGoie_bCk5IGCNE7Xvy2S2o3zRBnr8lYtFGEk25uxrDbEXWno3OgBHoaUBY3ZUK9tFS-wwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f13cb69a.mp4?token=lozXPAIZzeNpVm40Io9uMm1GftcR2RqhlMEGEJ5sEDL1rdBy65w_R4LPVqEoblXnMouIvwU39IsCnCM7uQY_i-9jo5Eh7AKw_JxUz9jUZ2FDTdH7XXyhSW_2MXDEMSqNgucKAug2HIPUCIcz0kvFtHODZhvpTlsXwGPcTT-hLuEzelVGoV3-dcHrF7tgzjd73fU7nhLfmwGPst_qbnycm_EvZoHkNcjLjmSQ-iVg_cUL2FTffI5j7nwzLKkA9AyFlcRAsFqT9yYVcUpdGoie_bCk5IGCNE7Xvy2S2o3zRBnr8lYtFGEk25uxrDbEXWno3OgBHoaUBY3ZUK9tFS-wwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعرخوانی سید حمیدرضا برقعی در جشن مباهلهٔ آستان مقدس مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/441104" target="_blank">📅 12:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
انتصاب اعضای جدید هیئت‌مدیرۀ مرکز خدمات حوزه‌های علمیه با حکم رهبر انقلاب
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای، طی حکمی اعضای جدید هیئت مدیرۀ مرکز خدمات حوزه‌های علمیه را برای مدت پنج سال منصوب کردند.
🔹
بر این اساس، حجج اسلام حسین رحیمیان، محمد جعفری گیلانی، محی‌الدین مکارم شیرازی، قدمعلی اسحاقیان، محمدمهدی حقانی و محمدحسین احسانی، به‌همراه نماینده مرکز مدیریت حوزه علمیه قم، نماینده حوزه علمیه خراسان و رئیس جامعة المصطفی العالمیه، به‌عنوان اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه منصوب شدند.
🔹
جلسه تودیع و معارفه اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه در روزهای ابتدایی خردادماه جاری با حضور حجت‌الاسلام والمسلمین محمدیان معاون ارتباطات حوزوی دفتر مقام معظم رهبری، دکتر ایروانی معاون نظارت و حسابرسی دفتر مقام معظم رهبری، اعضای سابق و اعضای جدید هیئت مدیره مرکز خدمات حوزه علمیه برگزار شد.
🔹
در این جلسه ضمن تشکر از اعضای سابق و رئیس مرکز، براساس نتیجه رأی‌گیری از اعضای جدید، حجت‌الاسلام والمسلمین حسین رحیمیان مجدداً به عنوان رئیس هیئت مدیره مرکز خدمات حوزه‌های علمیه انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/441103" target="_blank">📅 11:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLsILYsPxtvQ9LNHO4LnM13oBdiKUosP_3Ei0EAy4Ee9WPbW88uKFa4hF60x96ZrHukg50cQWl-dSfn2-bZ-BVHaVJ9tV2U_HhAtKHG5i96iOUMyEaw6c8z-4ElyM_0gUnKdMwtHLYKjbAjVeP4bpgcF7KMDY8Nzom7DXZ-EUxjU68hQNSDav-jOXpLcP5FX6QtKbPI_MdBNfyu6F1kA2utYDy0T44kof6857mXDzd54XWRA-wsFxWqKu-yGupB6uar9tIC82n6UXHwfK7Yk_qrPAE91dwMij9AM6duemOVJNU0pUb1r3NAuhv7eStMR8EOY5W32nvjHIt2lS7KRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه،…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/441102" target="_blank">📅 11:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYnJY8OSGoPKDy8d-eW1408mlI6Ux37fFFVB_WBXNfJ2-6NKuxRmuUgTlUG8dojt6xeXLITnj5M5S30W-7C085otlGDHJdW2W7ASIPyoOLVGr36_eDNHiCBL3kys3mPxcDDZt4822l1vHh6SgXUWbcURTBEcoscbBQnetVuHNJDcVfjVxgCyFbyMF0elO3UARAMtSMsb9yAA9sbK16S4EnosqM8ixbOPYbwMcuhbSjXayrch_aIPKJ_cBbRRk4U9Zo9BogKESbNe7wrRHdT1eZRJ_T3n3OmUo0lClwsAmYWJzwB8cZF_gl4DzhPSVNS-g1n4LvJx-Sdm_B9RoYH7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واگذاری فجر جم و پارسیان متوقف شد
🔹
هیئت وزیران با واگذاری پالایشگاه‌های فجر جم و پارسیان مخالفت کرد؛ دو مجموعه‌ای که در مجموع بیش از ۲۰۰ میلیون مترمکعب گاز در روز فرآورش می‌کنند و سهم مهمی در تأمین انرژی کشور دارند.
🔹
فجر جم حدود ۲۷ درصد و پارسیان بیش از ۱۰ درصد گاز کشور را تأمین می‌کنند؛ موضوعی که به‌دلیل اهمیت راهبردی این پالایشگاه‌ها در امنیت انرژی، واگذاری آن‌ها را متوقف کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/441101" target="_blank">📅 11:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a85b1410e.mp4?token=DDvuCEa8vgqqFEOcEwmW5X6mPYQzg0Nou7R83Rr2zVBrVkn_xOtmSxjUTR_Jyg6aopFdcy7tW9V4GibqyOYkZ8367Vj63wyJvOZKYyACa63Wm23m_kjtIcTrI7m8KPPuGCs2V1wqA4WGTGhjR0DBX1oylXOFpuqZw8r0_IqjjrjLh5VbNWVeEuyM7uiaUz7WadHqyO0ux3vAzaXztYPkx9hFoUM4FjGzPKSSUIgkQSBOagP6SfZv7Jq5Fu1j4YSxPa-RNHZS6aFf3e18fXpYCkCDLNvAq7IMs2CmaLgYz2qNEdM136r3hrPHxLxlCT7X0vUAPgiCI4I3JnNA8QXEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a85b1410e.mp4?token=DDvuCEa8vgqqFEOcEwmW5X6mPYQzg0Nou7R83Rr2zVBrVkn_xOtmSxjUTR_Jyg6aopFdcy7tW9V4GibqyOYkZ8367Vj63wyJvOZKYyACa63Wm23m_kjtIcTrI7m8KPPuGCs2V1wqA4WGTGhjR0DBX1oylXOFpuqZw8r0_IqjjrjLh5VbNWVeEuyM7uiaUz7WadHqyO0ux3vAzaXztYPkx9hFoUM4FjGzPKSSUIgkQSBOagP6SfZv7Jq5Fu1j4YSxPa-RNHZS6aFf3e18fXpYCkCDLNvAq7IMs2CmaLgYz2qNEdM136r3hrPHxLxlCT7X0vUAPgiCI4I3JnNA8QXEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
🔹
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/441100" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iARFisp2zF2i6v9lJE-Y32rmR4Hig4As3kYpz6QR4dc9uDO1wAUZd1lA7epgT3klhg7UD4DRxOTVwQlYOWQ2Eao5MSp_nhIy49NEnRZRbbbMQXszBckR1FjxbjaEtdOEnjwlgaJoX4ncJSGLZ5qc3DcIAHKybcvo89HjRQg_WtFR_kEZiIq8OKRS8_01usSR5kFhKDFOuGwrKuFxSOBL-Q4Tsk5YPN_FAjiUzFOA8Cp-2P750C5Q6Pz_f9s-aPdahOnpVL4zlPloZfYDJcuAoYD2TRB4YjIGqpHN1_jaAZTGcgqKCSXJCVaoHLo6W_rgC-SNj54ZK19VVnomeZ3YzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ia9n264r1xSc1PsUNKY-Sas237ZMlx5S-1MtdxHoZCPQj0rC37NG3pyyJWPkpHrwEHTK7bNkyJ4j2LutCjgStEuWCt4wBpm0cYGq3k9j6zYl9hssSdmaXg_T0XPQHPhhigFFYd1svtO5fro2FVaUk5R-wfgHznRrdVjZdHCYSgdz-RQ6B9QmswlNtt0D3jM22XzkAFOXM9onSbQal_NBoeQcM8mWBibYKWMWu1e6VHWAbbk1ruu4loYnrGsgyFwZAgEeqPZxwwLJ5uHMLQc2EhWK1o87k_oDlNxzHYZ5f60R7jFIBAos6farQWVp_GBEYIOGJ5t5_CSktHrBwc2ytA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایندگان ایران در فوتبال آسیا مشخص شدند
🔹
کنفدراسیون فوتبال آسیا به‌صورت رسمی جدول تیم‌های صعودکننده به لیگ نخبگان و قهرمانان فصل بعد را منتشر کرد.
🔹
نمایندگان ایران در لیگ نخبگان استقلال و تراکتور و در لیگ قهرمانان گل‌گهر سیرجان اعلام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/441098" target="_blank">📅 11:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFnwUZS2lueo3KRLgslndOdZEZ6O3G45AmvgngvjPp2yijapAZCY3bsC-Pj5o4dARV0i6eM8SWJJdcnqKUeBHpINc3IH2vwr89o9Z-psCipF4TZyLjlMCOzQPGzClI7LmsTbe3RZwn8j-697294FXQgoRNIjvlEhwYbjXnWGXQFZtMoqQyCHufwfQQqhcPFGurnik_NbuU6WNnU7Wbb38yIXcU4UbwIRgZ-ggUzGLiz2ZdgYdpHMbUvvdDF3VWMpCyM9lNaVBSWs1BcF6iyuoYxUk36tUGauuTDdXVeSZJcMXUl-e1r2etUFVcDBexptpZuh-ObQTItG0PRX4VYjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwlX3YNL4My78wVVHdbbxS79PBfe_8O1_f-UIa3zbiXuPMYijhRV4AYogTADX6opIZw2Hf7rgHQE6sR_-eS1hBbYRA1NgpPapi3KLqpzB-yRP3eQLsbmUJOD6VcWlpOjUknUkCdXjCLVUBzuDqbssWygvlnVzK3JGV_cKiBANgtb__dm3rFwawpFjFN5PRB7ovh2Z8pS_6uQf9yWxPgNXoG1nr_FfBRcBiSJa6rSZSLQZzYXK0PrzenMX5utiqqV_t_UaqW29NZxMuVviaNkf3rmpdATIMOQiAXEy8XhSMXbSf7dyjyga2aUX6TE0d2ENqfBXMFhwt41o_EKtTVrTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هلیکوپتر آپاچی آمریکایی مایه تمسخر ترامپ شد
🔹
در پی گزارش سرنگونی یک هلیکوپتر آپاچی آمریکایی در نزدیکی تنگه هرمز، کاربران خارجی یک سوال اساسی پرسیدند و آن این که هلیکوپتر آمریکایی هزاران کیلومتر دورتر از مرزهای آمریکا چه کار می کند؟
🔹
بسیاری از کاربران با اشاره به ریتوئیت پست ترامپ درباره سرنگونی هلیکوپتر ارتش آمریکا در نزدیکی تنگه هرمز در صفحه رسمی کاخ سفید این سوال را مطرح کردند که اصلا چرا باید ارتش آمریکا در نزدیکی مرزهای ایران که هزاران کیلومتر دورتر از مرزهای ایالات متحده است،‌ حضور داشته باشد؟
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441096" target="_blank">📅 11:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a856502fd2.mp4?token=SxoTUlTs2Gs74QQAuKt3WfcIgoFb2D3_TX9JVLc9rxyG4klPC8JHUx3Uh4ulvMLThFmJITvPDTOYS-OwII_njtHtau_5-VSLuHFXjazCGGdnu6Sg0D66s8ZmNZxkLvbE-T8AG-yFikvWONYzEJF38v6WCYJTBLLlkRhPsNRzuXZhT94yP8PNx5CKrhNderIooyvTOy7c-gP0SfxZdcNr28Mlc65JY1GOhIrCpZ-puH_T_mN1sp1LY4YRj57ZkjRtjB5oqnYG3-oA3I6YcxdUOsTRfxZSzTSYglqOxwHjrdSVRQ2ZRQnTOjs3Wn6iXsgjnYpdocuAuLGGOSc-rWOZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a856502fd2.mp4?token=SxoTUlTs2Gs74QQAuKt3WfcIgoFb2D3_TX9JVLc9rxyG4klPC8JHUx3Uh4ulvMLThFmJITvPDTOYS-OwII_njtHtau_5-VSLuHFXjazCGGdnu6Sg0D66s8ZmNZxkLvbE-T8AG-yFikvWONYzEJF38v6WCYJTBLLlkRhPsNRzuXZhT94yP8PNx5CKrhNderIooyvTOy7c-gP0SfxZdcNr28Mlc65JY1GOhIrCpZ-puH_T_mN1sp1LY4YRj57ZkjRtjB5oqnYG3-oA3I6YcxdUOsTRfxZSzTSYglqOxwHjrdSVRQ2ZRQnTOjs3Wn6iXsgjnYpdocuAuLGGOSc-rWOZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترخیص ۵۱ اتوبوس ضدآلایندگی از گمرک هرمزگان
🔹
رئیس‌ دادگستری هرمزگان: با پیگیری دستگاه قضایی، ۵۱ دستگاه اتوبوس ۱۸ متری مجهز به سامانه‌های ضدآلایندگی از گمرک ترخیص و به ناوگان حمل‌ونقل شهری کشور اضافه شد.
🔹
این اتوبوس‌ها با هدف کاهش آلودگی هوا و روان‌سازی ترافیک شهری وارد چرخۀ خدمت می‌شوند و ظرفیت جابه‌جایی مسافر در هر دستگاه معادل یک واگن قطار شهری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441095" target="_blank">📅 11:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز، احتمال شنیدن صدای این انفجارها در صفه، بهارستان و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441094" target="_blank">📅 10:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441093">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35603f2115.mp4?token=dxEnDbEAiZJaJkH5rEqyUWVf6WL4RwsLcxLvTAQqkSQun_dKdvCc3AoZATeECwEnRQfdskUk5NRxsQLhHkxGhybL12KI1tDHktnXNhtu5fEzVdzTHh15QQ0rWoWI9J2EFRMrAkpQDPWjro05JXOQqKIvwuhgd1kXYVJbDgYOcN3d9vtqaeRKi9s0WlpIxM__wJj7Vv19-8Ba6xLpfylhZfgZOdV-95WmYAi124JZhofLqUFhwgXxqLdvhfH3IEyuQHB7wUwh3reiry1grio76OT2S1-e1DMZD50SNRnCv-O0wIWSEUI8By4RGqrtYWyTaKavXXcyksZx1Jo7YOE6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35603f2115.mp4?token=dxEnDbEAiZJaJkH5rEqyUWVf6WL4RwsLcxLvTAQqkSQun_dKdvCc3AoZATeECwEnRQfdskUk5NRxsQLhHkxGhybL12KI1tDHktnXNhtu5fEzVdzTHh15QQ0rWoWI9J2EFRMrAkpQDPWjro05JXOQqKIvwuhgd1kXYVJbDgYOcN3d9vtqaeRKi9s0WlpIxM__wJj7Vv19-8Ba6xLpfylhZfgZOdV-95WmYAi124JZhofLqUFhwgXxqLdvhfH3IEyuQHB7wUwh3reiry1grio76OT2S1-e1DMZD50SNRnCv-O0wIWSEUI8By4RGqrtYWyTaKavXXcyksZx1Jo7YOE6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس
🔹
دقایقی پیش صدای چندین انفجار شدید در بندرعباس شنیده شد. هنوز محل دقیق این انفجارها مشخص نیست.
🔹
همچنین ساعتی پیش، دو مخزن آب در بخش بمانی سیریک هدف قرار گرفت و تخریب شد.
🔸
در ساعات گذشته پدافند در مناطقی از بندرعباس و…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441093" target="_blank">📅 10:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441092">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">توقیف اموال ۴۷ خائن به وطن در خراسان‌شمالی
🔹
رئیس‌کل دادگستری خراسان‌شمالی: تاکنون اموال ۴۷ خائن به وطن و افراد تأثیرگذار در شبکهٔ کمک به‌نفع دشمن، در خراسان‌شمالی شناسایی و توقیف شده است.
🔹
۴ نفر از متهمان مقیم آلمان، ۶ نفر مقیم انگلیس، ۲ نفر مقیم فرانسه، ۱۰ نفر مقیم ترکیه، ۵ نفر مقیم آمریکا، ۲ نفر مقیم کانادا، ۲ نفر مقیم ایتالیا، ۲ نفر مقیم استرالیا، ۲ نفر مقیم عمان و مابقی مقیم دانمارک، اسپانیا، قطر، امارات، چین، اسکاتلند، قبرس، یونان، نیوزیلند و کشورهای دیگر هستند که دستور‌های لازم در راستای توقیف اموال آن‌ها صادر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441092" target="_blank">📅 10:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441091">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCcGxpDN316qA8qqcs3ylFNP4LCxv4LQFnOeUpjZaANjzlBhPHb8Rll9GaOwhLAr9fYupbl2H7WfoUk6d2t7FhojYNT6IjiOygSAlubEbW7W0jmIUpJERLDt5e9KH1JmavBqosGexRUl3FsJC_mfCXMb2Nnjhh1dG5BegC-pbmlbzK76J7CsVhEtcH2Wavgq3nETwevJvw8_tFmCTWDDpGXMTUieEuai2j3jqcAm2Upv2UHLqn3RIwx1Fcb-VThtGEswb41fsdcuWMMAXXYaS0n9IYR6hjeng-aR9xAv6khtnc2PrxJVmWdM60EzpGz_VbfeRLjWliL_UfpdAhU28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اولین سالگرد شهادت شهید نصیرباغبان فرمانده اطلاعات نیروی قدس سپاه
🔹
پنجشنبه ۲۱ خرداد ساعت ۱۷ الی ۱۹ حرم حضرت عبدالعظیم (ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441091" target="_blank">📅 10:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441090">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تماس‌های خانگی رایگان شد
🔹
شرکت مخابرات همزمان با افزایش ۴۵ درصدی آبونمان تلفن ثابت، اعلام کرد مکالمات درون‌شهری و بین‌شهری به‌صورت ثابت به ثابت برای مشترکان خانگی از ابتدای خرداد رایگان محاسبه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441090" target="_blank">📅 10:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
تصاویر شلیک موشک‌های سوخت جامد و مایع دوربرد قدر و عماد و خیبرشکن به‌سمت اهداف آمریکایی در منطقه  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441088" target="_blank">📅 10:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b52068ab5.mp4?token=Uag9Rgj8ROeB0-fqX3G_37E4uTU74Wg-hSqyIPquRXcrxA_vzik0IhqZuCN_yD_3PElrq9JWHhVBEl7Va6SHUPXYWXDiYdXYa4TLLo8N-KIsAHm6YnVgUHlkB12HsZ0W53TxPb90dRujKnbPHXUa53CzHfiwYjUjuT2RcPoAqsxMdzXod5v5EMzXDB91poGrzbUhwCj0bVUpcaFR1zz1U-XECI_57bQpshCDfguHIXsK8hpOseGOsNgGhoGW8qLzIzVxp2urMsbAmk82MSm7CT1HjXhzKEo2bJHrmpuYRJP-8QETqvwgyH_ZO-ntqLeHyBbL2YPQBFLoyD51o8-IJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b52068ab5.mp4?token=Uag9Rgj8ROeB0-fqX3G_37E4uTU74Wg-hSqyIPquRXcrxA_vzik0IhqZuCN_yD_3PElrq9JWHhVBEl7Va6SHUPXYWXDiYdXYa4TLLo8N-KIsAHm6YnVgUHlkB12HsZ0W53TxPb90dRujKnbPHXUa53CzHfiwYjUjuT2RcPoAqsxMdzXod5v5EMzXDB91poGrzbUhwCj0bVUpcaFR1zz1U-XECI_57bQpshCDfguHIXsK8hpOseGOsNgGhoGW8qLzIzVxp2urMsbAmk82MSm7CT1HjXhzKEo2bJHrmpuYRJP-8QETqvwgyH_ZO-ntqLeHyBbL2YPQBFLoyD51o8-IJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سگ‌های بمب‌یاب محافظ کاروان ایران شدند
🔹
سایت DifCorrupcion مکزیک: ارتش این کشور به‌دلیل تهدید احتمالی از سوی دولت آمریکا علیه کاروان فوتبال ایران برای پیشگیری از خراب‌کاری از سگ‌های بمب‌یاب استفاده کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441087" target="_blank">📅 10:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEtkqT13huTDRp8mZka69XczTLo46CPWiR06A5yfhWHuH_95wrcCQf3H1ALZWpQBMq8PFEIqebD6cFSgSguqqAwCQiZQJGKbdtyP9UvlwsbHCmgvdzaPrPh3ZSiRu81BhkAycPxakf1x6PSchJuHVn7SqZlwxvEmCJmBxNCD8NqOCPyKgvddGEoMiT7bxRXj1iivE5NBneaTleF4Z0qwAsxipmJgiDy9SzbfzTw2WPJIa3_-7wW0ADNMiFlIk65nX6UuDKOP-PtiDT5pPlFfhyiFf5QqMB7bXcdIkLi_jIyOrO7QOh93BIo4C5Y6ENfayu7kp9AhPfvdEZWrfBNzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی کل سپاه: آفرین بر شما مداحان، شاعران و هنرمندان متعهد
🔹
۱۰۰ روز از درخشش بی‌نظیر ملت مؤمن و شجاع ایران می‌گذرد‌. بعثتی الهی که جهان را شگفت‌زده کرد و زورگویان مستکبر را در مقابل ارادۀ ملتی بصیر و مقاوم تسلیم کرد و ان‌شاءالله پاداش این ایستادگی بی‌مثال،…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441086" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMqQ46t0gCSNmVsOGggIwVeYXsohFjJ9ufWJnVLrFhynkbor4Q_2SAMcj4CR4M_9FeOMb_MNI6_ZX-K0Uq0rvbc2Ybxc0cVKkPuVtVncfjpml1fjG4KBjEXuMGQQwjkZQqBcCJ0VXwenYTUvD61oOiEdARbET2ijfpNJpi8SbQuxxipFATbxVkc_X90c0vHQE-wQ_Pt7qZQmx3DJv5npUWfnnpRlXJyPHpYonIh5uzgR9Brg2WMNXEpF5voxkdrPaRjFrKERT8TaBmrslPd8hI9fKrcESyC2XTLovRUzdeVH4Uu_Z5WNj8eL_LjdgXk2Gez7AH1SH5M1b-m1RY3qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکیِ باب‌المندب
🔹
سازمان عملیات دریایی انگلیس گزارش کرد که یک حادثه در ۸۸ مایلی جنوب غربی بلحاف یمن اتفاق افتاده است.
🔹
این سازمان گزارش کرده که «یک قایق با ۶ فرد مسلح به یک کشتی باری نزدیک شده و تبادل آتش بین قایق کوچک و کشتی‌های باری رخ داده است».
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441085" target="_blank">📅 09:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پلیس آفریقای جنوبی: در پی تیراندازی افراد مسلح به یک سکونتگاه غیررسمی در شرق ژوهانسبورگ، دست‌کم ۱۲ نفر کشته و ۹ نفر دیگر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441084" target="_blank">📅 09:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
با تصمیم شورای معین شورای‌عالی انقلاب فرهنگی، تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد
🔹
همچنین شورای معین با کاهش تعداد دروس امتحانات نهایی پایۀ یازدهم به ۶ درس برای کنکور ۱۴۰۶ موافقت کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441083" target="_blank">📅 09:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1at-aQusV56WwzuebISDAL-ymkkX1SaXmGOH8-WNWJHzAKWvzi6pDEypdZXoR2nAuFiSmB-8uYuLMbjmFirbpAsEmRpnHnbKLAVsgzQ7Kgba4n-MfA7umyGmmA0HcydfCzWgeegMwD9JwpJxSY3ZiUnnTLk9ydG6-jXx8ETX1U9EJKb4CgJd5cg5_FjwJ2qiHoLGe5sEAjTXekUIXGIh381-VdMfm8r02zuWvp1GFPRd3_V-HBleT576Eq5LIyn2tgtFoncYGjFbgX1kStms8vdbXztNqZpVInPsAf6raUtRctFC3ohIGD-5FkUMbqXZ11QU3jDwaITwIbTTpg_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس رکورد جدید زد
🔹
شاخص کل بورس در دقایق ابتدایی معاملات امروز با رسیدن به ۴ میلیون و ۶۰۲ هزار واحد رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441082" target="_blank">📅 09:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441081">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f500d34d.mp4?token=dD5GXdCNuxUQHeoFJghXtpj74MEB1t0FeQo8wDNzcEqmX_b4zEkbT1nDnZcc7h-WZK03WMj6OZYJVZR7ODIhJDjtjdT-A9tUOqe5oB-ndsz4jQZALulgPlZ3mzS-FExIVjYmkMLgPGGsGp4g8QFkQjCxOc2ePRWFQXEqbr30uyNEpFQpqM_3YvejsHU23ZsgUTxsC_lmoEceTWYs5UFFmIcb0k-7p-Nvn5o2fcq7Pldo4CJp7mia4P-Y9vsqorBhLWU0964nCKLB7PuWPiP8Sp4WXYLAv2dLikwO05sP-6lIHeA5hPNDRYnof0ijy36qd5wpq9_wbPbxcFqYHEnBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f500d34d.mp4?token=dD5GXdCNuxUQHeoFJghXtpj74MEB1t0FeQo8wDNzcEqmX_b4zEkbT1nDnZcc7h-WZK03WMj6OZYJVZR7ODIhJDjtjdT-A9tUOqe5oB-ndsz4jQZALulgPlZ3mzS-FExIVjYmkMLgPGGsGp4g8QFkQjCxOc2ePRWFQXEqbr30uyNEpFQpqM_3YvejsHU23ZsgUTxsC_lmoEceTWYs5UFFmIcb0k-7p-Nvn5o2fcq7Pldo4CJp7mia4P-Y9vsqorBhLWU0964nCKLB7PuWPiP8Sp4WXYLAv2dLikwO05sP-6lIHeA5hPNDRYnof0ijy36qd5wpq9_wbPbxcFqYHEnBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوان روستای پنداش کاشان با نصب پنل‌های خورشیدی به درآمدزایی رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441081" target="_blank">📅 09:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441080">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf04ab66a8.mp4?token=HNR1H22FmtgANVvfI8TPTsZ4Zez8mLjxH6tsZmR0siMHwUpT341zKIVzJoa7PU2YQjyEyYsQXSmRKi0C71UccWUJn-zLQVvruhDd50w52Ut65CPj8Q1KBygVZ-Ikfz4v6EyWLLD-K-TucIW9W-AFCxYOFilUSYIWtocvzP4HDiw0wAJl8ah_LRdfiRhASEdKmmWA-Jbr7P5ua6BZNM-cs2ABs8F9zb3RrAtlzD9AIKnEq6JqnZT2uA8KDduFymc8970-PIi-27GiuQ4LUXbfVYjZr_inKpc-k6EpqC2W2oh9CtSzLHQZLd83mc-BTXwUUOdrD7EgW03TVutYPLEofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf04ab66a8.mp4?token=HNR1H22FmtgANVvfI8TPTsZ4Zez8mLjxH6tsZmR0siMHwUpT341zKIVzJoa7PU2YQjyEyYsQXSmRKi0C71UccWUJn-zLQVvruhDd50w52Ut65CPj8Q1KBygVZ-Ikfz4v6EyWLLD-K-TucIW9W-AFCxYOFilUSYIWtocvzP4HDiw0wAJl8ah_LRdfiRhASEdKmmWA-Jbr7P5ua6BZNM-cs2ABs8F9zb3RrAtlzD9AIKnEq6JqnZT2uA8KDduFymc8970-PIi-27GiuQ4LUXbfVYjZr_inKpc-k6EpqC2W2oh9CtSzLHQZLd83mc-BTXwUUOdrD7EgW03TVutYPLEofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تگرگ در شمال، گردوخاک در شرق
🔹
هواشناسی: امروز و فردا در آذربایجان‌غربی و شرقی، اردبیل، گیلان، مازندران، گلستان، ارتفاعات البرز و شمال خراسان‌شمالی بارش باران پیش‌بینی می‌شود و در مناطق مستعد احتمال وقوع تگرگ نیز وجود دارد.
🔹
افزایش سرعت وزش باد در غرب، جنوب‌غرب، جنوب، شرق، شمال‌شرق و دامنه‌های جنوبی البرز طی ۲۴ ساعت آینده می‌تواند باعث خیزش گردوخاک و کاهش کیفیت هوا شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441080" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441079">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LukE1ckRZqU8GCj-vjJ3sQd70Yh2gujS81vMYRF6cUxS1BNolBrdTEG3veSSSEYCKfTWjOEAhh5f0_vT7ssho3p9IKw4ald4hWcieZQj8inrCBVDk98ufjcjp9fR06BQVJW5GqHE852Grzyn1Y7qTYWjjW5NBlVjHr7AoPpSMwJbucfao0V3wcXgA_ErQ-pUWFZWaFxyMeswFjOYtm5a7VLWXRhFFWWoCjiAPnRtrqrYwG7k7Thn6HYq2_2R1KuaCCsDHDWBfAs6NDpTrgSwPuMPbVZyHy8RESqpIWWWfZab7lfpKdDly_tV_Bd0Lub_t2UNDeJlnBZopxPYAVDLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی عراقچی با همتایان ترکیه‌ای و عربستانی
🔹
فیدان و بن‌فرحان نیمه‌شب دیشب در تماس‌های تلفنی جداگانه با وزیر خارجهٔ کشورمان آخرین وضعیت تحولات منطقه‌ای متعاقب حملات تجاوزکارانهٔ آمریکا به مناطقی در جنوب ایران را بررسی کردند.
🔹
عراقچی در این تماس‌ها ضمن محکومیت تجاوز نظامی آمریکا و نقض حاکمیت ملی و تمامیت ارضی ایران، بر حق ذاتی دفاع مشروع برای پاسخ متقابل نیروهای مسلح مقتدر کشورمان تأکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441079" target="_blank">📅 08:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff164d2d4.mp4?token=rIvBnFmKA59HOUaWIM00tqfcfUgEz6UjR6PaSIiGTFosIC70e3hz4R9izIXjQqnZViP8tdgyF7wl-igMqB0VOOlZ7onLnl1lRYPPewjicnNwJpJ_ovDFVQ3Ej0eU1LtlJkdpX9OdvOqTQpqi8-7wjQxe9n_n5vdKefwECzcUV8nlyrKShDVFNpCgY7fXj14uDUXrhT5efQRuubFX97aSh7oNIJ7A8Yzggq1F_MODF0KdSddM-Qb5I0zKB_CDuA5McN8SXKRh2FcNJo_9xmn1gHc7oNP9Q5Q1vW2P25c7L9C9o3xR_Bk5QjapDQE2lWOwbwqdrUqFOSlIn3xVlrJv7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff164d2d4.mp4?token=rIvBnFmKA59HOUaWIM00tqfcfUgEz6UjR6PaSIiGTFosIC70e3hz4R9izIXjQqnZViP8tdgyF7wl-igMqB0VOOlZ7onLnl1lRYPPewjicnNwJpJ_ovDFVQ3Ej0eU1LtlJkdpX9OdvOqTQpqi8-7wjQxe9n_n5vdKefwECzcUV8nlyrKShDVFNpCgY7fXj14uDUXrhT5efQRuubFX97aSh7oNIJ7A8Yzggq1F_MODF0KdSddM-Qb5I0zKB_CDuA5McN8SXKRh2FcNJo_9xmn1gHc7oNP9Q5Q1vW2P25c7L9C9o3xR_Bk5QjapDQE2lWOwbwqdrUqFOSlIn3xVlrJv7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی پیش از اصابت موشک به اهداف آمریکایی در بحرین   @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441078" target="_blank">📅 08:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-9IW9Mta4wgxac4FreGfIeSquTT4tdSDgVqHvIk2uZpY0O8QmTnaaMVe53JHy0dDAR8DxyWHN7UPZMg7-vjTpGzJ2X8m322RL8l__l6BE3ABALUq6dWV1aOeTPesHe-P9nJ9QN2NyjWrAUB2UgfylLAzEL9LR0NwT5bWhDKRjvvYufd3fuB6u6u9pGmfqw7x0_1BKqnVUkvboGHzgR80mlYGG3fhW04U1zHItAHO9Rg4jCsUgqrNQt1lzcPaFG_B0oLmC6hLGGfSM3u9Me1zXQJedOoibRh1JckUlN5Vr_akvPTVHA9YmN2eWIWu7IkArz_kuYW-buzWfCXAFgaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه: در حمله به مبدأ تجاوزات درنگ نخواهیم کرد
🔹
رژیم آمریکا در اولین دقایق بامداد چهارشنبه به بهانهٔ سقوط یک بالگرد ارتش تروریستی این کشور بر فراز تنگهٔ هرمز حملات وحشیانه‌ای را علیه مناطقی در جنوب کشور انجام داد که نقض فاحش منشور سازمان ملل و قاعدهٔ بنیادین «منع توسل به زور» در روابط بین‌الملل است و هیئت حاکمهٔ آمریکا با این اقدامات تجاوزکارانه بار دیگر ماهیت جنایتکارانه و جنگ‌طلب خود را نشان داد.
🔹
نیروهای مسلح مقتدر جمهوری اسلامی ایران در واکنش به تجاوز نظامی آمریکا به ایران و نقض آشکار حاکمیت ملی و تمامیت سرزمینی کشورمان، پایگاه‌ها و دارایی‌های آمریکا در منطقه که مبدأ این تجاوزها بود را هدف ضربهٔ شدید قرار دادند.
🔹
ما ضمن محکوم‌کردن شدید جنایت آمریکا در تجاوز نظامی علیه ایران، بار دیگر مسئولیت قانونی و اخلاقی همهٔ کشورهای منطقه، به‌ویژه کشورهای حاشیهٔ جنوبی خلیج فارس، برای ممانعت از هرگونه استفاده ارتش تروریستی آمریکا و رژیم صهیونیستی از قلمرو و امکانات آنها جهت طراحی، سازماندهی، اجرا و پشتیبانی از اقدامات تجاوزکارانه علیه ایران را یادآوری می‌کنیم و هشدار می‌دهیم که ایران در اعمال حق ذاتی دفاع از خود، از جمله از طریق هدف‌قراردادن مبدأ حملات و پایگاه‌ها و امکانات لجستیک مورد استفاده برای عملیات‌های تجاوزکارانه علیه ایران، درنگ نخواهد کرد.
🔹
ما همچنین بار دیگر مسئولیت سازمان ملل، خصوصاً شورای امنیت این سازمان و دبیرکل را برای صیانت از صلح و امنیت بین‌المللی و پاسخگوکردن طرف‌های متجاوز خاطرنشان می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/441077" target="_blank">📅 08:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441075">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358fade751.mp4?token=JYENn0n8bj95MAX97DHr8zcVNlCmTugDxsdaZQTXuKDRiJQBzAWDCuKnBhE1i7QWWq2uFzgNKC_z55IRgi_OXgITnMoPPp5Wl9LY6hkQEqUkRQ63uK0BGptCzmK9jnkftTrquyNeQCihO3xrYVccgClwYJgn8w0ewk762KvHZG1QHPx66iDP8kQMQ5Jzh4BV5Ljj9pQsG5FMY8kmS5hUOPhrQupvlVIlF0EhC-WFc8LLVfbFXL3WvaRrEwCAWqqX9XqbQWbkWTKaQOkLd3fPZ4rJ7wJAx4a7ZqjF5_F8HY32QbAmi-P-HQVhiYtxxPhOK4kGiOqmsjBj6GHrYsrwCYH7XuTnQpvatUF3aodEkEthRINQJlVxs7y1wR4K55Vxq-KFtmn83ihlEh9f1Q7g0_6shhm13A1UOx5H4ONcB3HragCWFTQmKOyRfle5aaq_c-A5UTWcy6FGAagy8owW34m8qJJFLzx9JcRt-Mga_-r1HeleyN4d0zKVPeXLqdMHUSqbd_5yhpMVzZKi20TZaXQMeFxK2meHDTMmN88xrRX0H6GsV3132JjnOZhZRECMmU65pm653frMHVTVDI5EKB9QNT3VfljEQlS6nfKpTc6PQdCKto3r4W0UesPtCPyCv3Mc9xteWmGWYyFQw5ktrQ_HvRpbVPSEVtU2QkIaN_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358fade751.mp4?token=JYENn0n8bj95MAX97DHr8zcVNlCmTugDxsdaZQTXuKDRiJQBzAWDCuKnBhE1i7QWWq2uFzgNKC_z55IRgi_OXgITnMoPPp5Wl9LY6hkQEqUkRQ63uK0BGptCzmK9jnkftTrquyNeQCihO3xrYVccgClwYJgn8w0ewk762KvHZG1QHPx66iDP8kQMQ5Jzh4BV5Ljj9pQsG5FMY8kmS5hUOPhrQupvlVIlF0EhC-WFc8LLVfbFXL3WvaRrEwCAWqqX9XqbQWbkWTKaQOkLd3fPZ4rJ7wJAx4a7ZqjF5_F8HY32QbAmi-P-HQVhiYtxxPhOK4kGiOqmsjBj6GHrYsrwCYH7XuTnQpvatUF3aodEkEthRINQJlVxs7y1wR4K55Vxq-KFtmn83ihlEh9f1Q7g0_6shhm13A1UOx5H4ONcB3HragCWFTQmKOyRfle5aaq_c-A5UTWcy6FGAagy8owW34m8qJJFLzx9JcRt-Mga_-r1HeleyN4d0zKVPeXLqdMHUSqbd_5yhpMVzZKi20TZaXQMeFxK2meHDTMmN88xrRX0H6GsV3132JjnOZhZRECMmU65pm653frMHVTVDI5EKB9QNT3VfljEQlS6nfKpTc6PQdCKto3r4W0UesPtCPyCv3Mc9xteWmGWYyFQw5ktrQ_HvRpbVPSEVtU2QkIaN_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای «محمد غلوم» مداح سلب‌تابعیت شدۀ بحرینی در اجتماع دیشب میدان انقلاب تهران
🔸
دولت بحرین اخیرا تعداد قابل‌توجهی از شهروندان این کشور را به بهانۀ حمایت و ابراز همدردی با مردم ایران سلب‌تابعیت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/441075" target="_blank">📅 07:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441074">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">طالبان: ۱۳ نفر در حمله هوایی پاکستان به افغانستان کشته شدند
🔹
سخنگوی طالبان افغانستان: در پی حملات هوایی ارتش پاکستان به سه ولایت افغانستان، دست‌کم ۱۳ نفر کشته و ۱۴ نفر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441074" target="_blank">📅 07:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441073">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
لحظاتی پیش از اصابت موشک به اهداف آمریکایی در بحرین   @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/441073" target="_blank">📅 07:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441072">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsJ9DbCc1PLW6Fb25Z70QCcKb8ksJMcldG5Gkk_tI8RYojq9dr4btwFYkS_PzCQNaSW6n2e0nrheH2-7fLJohnZZeOi1EEpPwY9xLilj2WaVSJHZW-vGneSCnMbu3ufzLhDFyva_Dn6HFFx1oFWXPnPvFzg1Dd2o2RqQzauO-H1D1A5OB9r2lckwkj0o9CQsa8xxXGyXeD1V3w73pv4UDa0IhdofLy5ZcT5hyER6YcLqfT-b33icupFsNVME8Taw743n0nMHq9J8VdJMyZ9OhchV6_i0KtQ0hcYSx1L9INLpKipthRoUEAF4Szg52r-SP-KVhyim4jRZzJFmuFlm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۳، ۴، ۵ و ۶ شارژ شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/441072" target="_blank">📅 06:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441071">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667c81d9ef.mp4?token=ZRxYgZetpCc174LohoPsJJyE9pPHldrK2kJS4AxZhsQDqkXuG7gg8olpf21vvnaeBmQlvWLDlx0tUzXgNS7gQ9hbL8F-0OH-DUmMf5JOqNLqA24qMw0g88M9y4lFv_9WdXbVPHsFLSVYnBJDX5LWbX1qXTheCFL35F2NiLY6UHvjuw8HeP8UTbgRkSPjtOheE-k55qNz5w0BtuKFvcFRAyMCM8mYa1b2P66TIijS4t3vn3hXDkWiqSEgcOBanrhonXq32Q7COiT6RMH7pHCqSdzaXnBZVKwyDuBCSxroUK5qStkMuwVHDfa5yV5fb4Xd1IXqsFC3DFk7E6lnKX_JwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667c81d9ef.mp4?token=ZRxYgZetpCc174LohoPsJJyE9pPHldrK2kJS4AxZhsQDqkXuG7gg8olpf21vvnaeBmQlvWLDlx0tUzXgNS7gQ9hbL8F-0OH-DUmMf5JOqNLqA24qMw0g88M9y4lFv_9WdXbVPHsFLSVYnBJDX5LWbX1qXTheCFL35F2NiLY6UHvjuw8HeP8UTbgRkSPjtOheE-k55qNz5w0BtuKFvcFRAyMCM8mYa1b2P66TIijS4t3vn3hXDkWiqSEgcOBanrhonXq32Q7COiT6RMH7pHCqSdzaXnBZVKwyDuBCSxroUK5qStkMuwVHDfa5yV5fb4Xd1IXqsFC3DFk7E6lnKX_JwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدیوی منتشرشده در منابع عربی از اصابت به پایگاه آمریکا در بحرین  @Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/441071" target="_blank">📅 06:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
منابع خبری از حملات هوایی رژیم صهیونیستی به شهرک‌های النبطیه‌الفوقا، حبوش و کفررمان در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/441070" target="_blank">📅 06:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441069">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9e8f3330.mp4?token=uiSFhoEoSmsa4QMHGBfQC_4VDmBX4i56GpBdzhk0n_ExpQGlF5wQQw-_WBtkr3PyfCqPnhwvuV0Qf3EfvMm4C1IGf2vX59-4PQMGaQ_szrMg56_2Fqsx_CG4J_fCokwu_wtcvnfl--fMsluHpz1vh6ZwVKfiZMrnaGAcYRlf5YADmlAkaHkkc7GPxUw7gCfHNrlUJfBfG18cJRk84MnqCtWFuKpr_nEJdG44c7fX1e2wZzt7NstgAXsmssgeXkHpJfU5lshfJzLK5p1BpWqxKtkiC08n1s7u-nA-fPRq0pZht3m_sPl3XL6LnoZEH6W5nwFtgW0MozsRA1oNHLZElw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9e8f3330.mp4?token=uiSFhoEoSmsa4QMHGBfQC_4VDmBX4i56GpBdzhk0n_ExpQGlF5wQQw-_WBtkr3PyfCqPnhwvuV0Qf3EfvMm4C1IGf2vX59-4PQMGaQ_szrMg56_2Fqsx_CG4J_fCokwu_wtcvnfl--fMsluHpz1vh6ZwVKfiZMrnaGAcYRlf5YADmlAkaHkkc7GPxUw7gCfHNrlUJfBfG18cJRk84MnqCtWFuKpr_nEJdG44c7fX1e2wZzt7NstgAXsmssgeXkHpJfU5lshfJzLK5p1BpWqxKtkiC08n1s7u-nA-fPRq0pZht3m_sPl3XL6LnoZEH6W5nwFtgW0MozsRA1oNHLZElw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وقوع انفجارهای جدید در کویت و بحرین
🔹
به گفتۀ منابع محلی، پایگاه‌های آمریکا در بحرین و کویت بار دیگر هدف حملۀ هوایی قرار گرفته‌اند. @Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/441069" target="_blank">📅 06:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441068">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
وقوع انفجارهای جدید در کویت و بحرین
🔹
به گفتۀ منابع محلی، پایگاه‌های آمریکا در بحرین و کویت بار دیگر هدف حملۀ هوایی قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/441068" target="_blank">📅 06:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441067">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
آسمان اردن پس از حملۀ موشکی ایران به پایگاه هوایی «موفق‌السلطی» و تلاش‌های ناموفق آمریکا برای رهگیری موشک‌ها
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441067" target="_blank">📅 06:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441066">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: ۴ هدف مهم از جمله آشیانه‌های جنگنده های F35 در پایگاه هوایی و مرکز فرماندهی کنترل ارتش کودک‌کش آمریکا در الازرق اردن مورد هدف قرار گرفت و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/441066" target="_blank">📅 05:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441065">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: ۴ هدف مهم از جمله آشیانه‌های جنگنده های F35 در پایگاه هوایی و مرکز فرماندهی کنترل ارتش کودک‌کش آمریکا در الازرق اردن مورد هدف قرار گرفت و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/441065" target="_blank">📅 05:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441064">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441064" target="_blank">📅 05:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441063">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/441063" target="_blank">📅 05:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441062">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ef1e3afd.mp4?token=WaekKBgrmElh80WBxUEjK9B4PZYKC4j2ve960A_-LXW2-axk0TToE-UsZE_xLUwOeGkm45GlQK2LNJuFOFHPpM1-CoDdu8Mk-eQ1FRMQw4hMPy3SrphTNvot2ftQ5vVjUKkGbGYTYQDoYNurr_Se4daLwciiTIv8qhkzV1NJnwDdyFB1HuOCaHKCX8Hx0R85Xd84gX_yASsyW-bcrvXER79vvlQVrnFy1fG4FqOlLazTFqPXfJ96c5DOR3ErKMEukD7Zo7QBc3srk2_0KFktGDLDyyE4Zf7zuH7zmwSWNBPWFBxMEYzQkPUroIbcqntQHRqOa0I0oEcJiB49QStQoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ef1e3afd.mp4?token=WaekKBgrmElh80WBxUEjK9B4PZYKC4j2ve960A_-LXW2-axk0TToE-UsZE_xLUwOeGkm45GlQK2LNJuFOFHPpM1-CoDdu8Mk-eQ1FRMQw4hMPy3SrphTNvot2ftQ5vVjUKkGbGYTYQDoYNurr_Se4daLwciiTIv8qhkzV1NJnwDdyFB1HuOCaHKCX8Hx0R85Xd84gX_yASsyW-bcrvXER79vvlQVrnFy1fG4FqOlLazTFqPXfJ96c5DOR3ErKMEukD7Zo7QBc3srk2_0KFktGDLDyyE4Zf7zuH7zmwSWNBPWFBxMEYzQkPUroIbcqntQHRqOa0I0oEcJiB49QStQoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: ناوگان پنجم دریایی آمریکا در بحرین هدف حملۀ پهپادی قرار گرفت</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/441062" target="_blank">📅 05:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441060">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد
.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/441060" target="_blank">📅 05:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441059">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/441059" target="_blank">📅 05:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441058">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/441058" target="_blank">📅 05:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441057">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/441057" target="_blank">📅 05:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔹
روابط‌عمومی ارتش: در ادامۀ عملیات مقابله با شرارت‌ها و مزاحمت‌های ارتش تروریستی آمریکا برای ساکنان جنوب کشور، بامداد امروز، ارتش جمهوری اسلامی ایران در اقدامی متقابل، با موجی از حملات پهپادی، پایگاه‌های آمریکایی و سامانه‌های راداری ناوگان پنجم ایالات متحده را در بحرین آماج حملات خود قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441056" target="_blank">📅 05:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در منطقه مورد حملۀ مشترک ارتش و سپاه قرار گرفت
🔹
قرارگاه مرکزی حضرت خاتم الانبیا(ص): در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانۀ واهی سقوط بالگرد خود، برخی از پایگاه‌های آمریکا در منطقه هدف هجوم قدرتمند ارتش قهرمان جمهوری اسلامی و دلاورمردان سپاه پاسداران انقلاب اسلامی قرار گرفت
🔹
ارتش جنایتکار آمریکا بداند در صورت تکرار تعرض به جمهوری اسلامی ایران، حملات سهمگین و گسترده تر علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441055" target="_blank">📅 04:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441054">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
🔹
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان پدافند هوایی نوین سپاه قرار گرفت و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/441054" target="_blank">📅 04:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441053">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
سپاه: ناوگان پنجم دریایی آمریکا در بحرین هدف حملۀ پهپادی قرار گرفت
🔹
روابط عمومی سپاه پاسداران: رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک، سیریک و قشم را مورد حمله قرار داد که به یک دکل مخابراتی در سیریک خساراتی وارد آمد و دو مخزن آب بخش بمانی این شهرستان منهدم شد.
🔹
در پاسخ به این حرکت شرارت آمیز دشمن، رزمندگان نیروی دریایی سپاه ساعت ۲:۳۰ دقیقه بامداد ناوگان پنجم دریایی بحرین و پایگاه علی السالم کویت را مورد حمله پهپادی قرار دادند.
🔹
درگیری‌ها ادامه دارد و پاسداران غیور ملت ایران در حال پاسخگویی به تجاوزهای دشمن هستند و در صورت ادامه شرارت، پاسخ‌های سنگین‌تری در راه است
و ماالنصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/441053" target="_blank">📅 04:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441052">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس
🔹
دقایقی پیش صدای چندین انفجار شدید در بندرعباس شنیده شد. هنوز محل دقیق این انفجارها مشخص نیست.
🔹
همچنین ساعتی پیش، دو مخزن آب در بخش بمانی سیریک هدف قرار گرفت و تخریب شد.
🔸
در ساعات گذشته پدافند در مناطقی از بندرعباس و شهرستان جاسک و قشم نیز فعال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/441052" target="_blank">📅 03:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441051">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ایران میزبان اجلاس خزر می‌‌شود؟
🔹
کاهش ۲۰ سانتی‌متری تراز آب دریای خزر به محور اصلی اجلاس کشورهای ساحلی تبدیل شده؛ نشستی که قرار بود با میزبانی ایران برگزار شود، اما به‌دلیل شرایط جنگی به تعویق افتاد.
🔹
لاهیجان‌زاده، معاون سازمان حفاظت محیط‌زیست در این‌باره گفت، پیشنهاد شده اجلاس یا در کشوری دیگر برگزار شود و یا به شکل برخط انجام گیرد.
🔹
وی تأکید کرد که جمهوری اسلامی ایران همچنان بر حفظ جایگاه میزبانی خود اصرار دارد و تمایلی به واگذاری این مسئولیت به کشور دیگری ندارد.
🔹
با این‌حال، اجرای هرگونه تغییر در نحوۀ برگزاری اجلاس نیازمند هماهنگی و تصمیم‌گیری مشترک میان کشورهای عضو و همچنین بررسی در وزارت امور خارجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/441051" target="_blank">📅 03:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441050">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cth0OVrW6qdzxbHUPafDCRBURGFrWh6WQq3cor-o4DAoSXag-qo631rd6yVzpKx6KDYKK5u6mK2vhKZCZ9bA7XKZD-_iHH0nuVRIYfADLPsksPsva2x35HTumMSywd1_oWqNuFRJQj5Jz75qmPhrCp4-8O7kqt9kyv7zWVuXyqm1imzvqgvr-7m2cL9gvMp1lftTPWCAbGSQTxZ3qyI6vCEfOKZkg6qawimXhoXRK1vZyK44iqP-8qqYQYOaCZnX7Y6SCGk5TkvExpXdD03uFLVZoMFT1yhQlllArPohwCDEQRUubYc9zQRH8yM6-f2vFGz7UedF1k_p8eQys167Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجاوز مجدد آمریکا
به جنوب ایران
🔹
یک مقام ارشد آمریکایی در گفتگو با شبکه ۱۲ تلویزیون رژیم صهیونیستی گفت: «موج دوم حملات به ایران همین الان در حال وقوع است».
@FarsNewsInt</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/441050" target="_blank">📅 02:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441049">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🖼
گروه هکری حنظله: آمریکایی‌ها درصورت هر اقدام علیه ایران باید جنازه سربازان خود را از مخفی‌ترین پایگاه‌های خود خارج کنند‌.  @Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/441049" target="_blank">📅 02:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441048">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp8B2tU8nVa1UeYD9AM_0toJ0bt0ZIx_JFTqqlq1jf6zX-4ekzTvJ1qfJIuJToilDpKDHbAL8yBUbLW6gyP3asG48gBMMPMWuzdjTuaBNEKDBE0F9zF3D2cB591dbZSHeVl-1ql2zhiqVo20cp1tnMcFppBJprw0BQuoCfTxOWlN-Q-vfhF53TgJhPlQLA59OQ4TzNK73WUa5zH56XzhB5UzR1yyIq6dDGd4xD26LJEq3SqPuyii5ISbW_kuI6Ld6PkaYrwvqicW5UZhPM9houtcP00RfOkRs-4-T-ehSGvF_9PoPwBHGUAerbI3tC37IunmccpW3GZkxIFzaupv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: اگر می‌خواهید در امان باشید بهتر است منطقۀ ما را ترک کنید
🔹
با وجود شکست در میدان نبرد، ایالات متحده یک‌بار دیگر تصمیم گرفت عزم ما را آزمایش کند. نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نمی‌گذارند.
🔹
اگر می‌خواهید در امان باشید بهتر است منطقۀ ما را ترک کنید.
🔹
تاریخ خلیج‌فارس در مورد سرنوشت شوم بیگانگان متجاوز داستان‌های زیادی دارد.
🔹
هرمز در آب‌های بین‌المللی قرار ندارد، بلکه میان ایران و عمان مشترک است و هزاران مایل از سواحل ایالات متحده فاصله دارد. مرزهای دریایی کاملاً روشن و بدون ابهام هستند.
@Farsna</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farsna/441048" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441047">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef134277c9.mp4?token=eKfL3NIlihzplI4ROnTz_Vy0Q8APMW4ZEqaVWhiUi92UeABiMRezb14vhxMSVJ8EGNvetU_KKXf8bBkJxcDUtusY-cWxxlpLjSU5gEigSsKvVyJDnAIruQmKlMPa0Lci12odQdpEDV5JdR8roQ-hqgE_-3Imoi4hjUuiqTbL2Uq1eepFnviCVuyX6amgCFWBI65Q8-RLehUkLHc22EtSC8qOHHXYNqh06ngo6ryI6vnh4v5gF3-RFlWjQr7_18qeuwtYjFTMQNmXc2FRKCHa7wnabyNRXrzwYmwM6EKB4np9qEsvUrwVqHYZuHxkx_zq96KxYpl3CrzMI3Kilz9uPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef134277c9.mp4?token=eKfL3NIlihzplI4ROnTz_Vy0Q8APMW4ZEqaVWhiUi92UeABiMRezb14vhxMSVJ8EGNvetU_KKXf8bBkJxcDUtusY-cWxxlpLjSU5gEigSsKvVyJDnAIruQmKlMPa0Lci12odQdpEDV5JdR8roQ-hqgE_-3Imoi4hjUuiqTbL2Uq1eepFnviCVuyX6amgCFWBI65Q8-RLehUkLHc22EtSC8qOHHXYNqh06ngo6ryI6vnh4v5gF3-RFlWjQr7_18qeuwtYjFTMQNmXc2FRKCHa7wnabyNRXrzwYmwM6EKB4np9qEsvUrwVqHYZuHxkx_zq96KxYpl3CrzMI3Kilz9uPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در مناطقی از هرمزگان
🔹
دقایقی پیش صدای چند انفجار در مناطق شرقی هرمزگان از جمله در کوهستک و سیریک و میناب شنیده شد.
🔹
هنوز منشأ و محل دقیق این انفجارها مشخص نیست اما منابع محلی از فعالیت پدافند در برخی نقاط استان نیز خبر می‌دهند.
🔹
سازمان…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/441047" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441045">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_oNrdFMuaX_4wVDM8myGNpM32NSmIRU7VypUmiflPrjd-Ytfto-1TOE7Hvf5eWMVKmyDp5BeDTQEAaykUt3PwNRVGfeq8oeMajPoVLSgZO8jiNvh_d9PETTKCSolD9_S7pz6yGYN2PmM4-d1yDtNzdvJ5DIUDwVITPZKRnDzvTBvWanMz2bj7v-PLZ-EQ1CgEPPLfYWJceJFueNEPL7_AHfWDTuVkRtTcyCF5EnATY48UxPRTVZxFAWu9soMe5KZyG-u5Reo-dtWpyOdaA9EKYuR7r-uToZRuXui_SSSBiPyJoi-M6F2nmgUIIzvY96wH0V1k8U8l2lC95ymuft9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ عراقچی به شورای حکام درباره پیش‌نویس قطعنامۀ ضد ایرانی
🔹
وزیر امور خارجۀ ایران در نامه‌ای به اعضای شورای حکام، پیش‌نویس قطعنامۀ ارائه‌ شده از سوی آمریکا و ۳ کشور اروپایی را اقدامی سیاسی و از روی بدنیتی خواند و از اعضا خواست اجازه ندهند آژانس بار دیگر به ابزار سیاسی آمریکا تبدیل شود.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farsna/441045" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441044">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پرواز جنگنده‌های صهیونیستی برفراز بیروت
🔹
منابع لبنانی از پرواز هواپیماهای جنگی با سرعت زیاد برفراز پایتخت لبنان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farsna/441044" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441042">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در مناطقی از هرمزگان
🔹
دقایقی پیش صدای چند انفجار در مناطق شرقی هرمزگان از جمله در کوهستک و سیریک و میناب شنیده شد.
🔹
هنوز منشأ و محل دقیق این انفجارها مشخص نیست اما منابع محلی از فعالیت پدافند در برخی نقاط استان نیز خبر می‌دهند.
🔹
سازمان تروریستی سنتکام دقایقی پیش اعلام کرد که ارتش آمریکا حملاتی را در ایران، در پاسخ به سرنگونی هلیکوپتر آپاچی آغاز کرده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farsna/441042" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441041">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: حادثه بالگرد آپاچی موضوع جدی نیست
🔹
ترامپ به وال‌استریت ژورنال: حادثه هلیکوپتر آپاچی موضوع جدی نیست و خلبانان سالم هستند. @Farsna</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farsna/441041" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cc9_MU_A4Hc92XRMALele2PBfgxVZihIHH9YOfVKLJSYPdo3A7rrmCsHUUMIulgccVQkvcYxPx6bKMIavXlhJdm-pvB5b1F16ChjpvDpl9D6oY--38tB9cI6bSYnLaRof58rRl_mhAANYS8JcAZNFK3hV09b9KtluJteBEWFd5n_uU5j8NfRf-HZGJsrkXgZLHxik-lgn1kygjs1dJCpe2bGdtAIefrs6IH-Pgfu3LNtvdegFoELDHa0SG7_byvaEww_eYAWkBxjfLuqlzHr8p3Jr9OjQnIT09f_J4et82xfwlTsETywp64tblTJfq1ZSpPcdW-O20oibEL7FdsBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwaTLtho6hKb1O7loPyDginaRt3GqPp7UlEvFKcEA5aMZpr2lnaRPfBd4KtK0xfix2IjO2QcXidIDOTQjDn1d9q7oDAE0FhYmHZAWipx_iRx876Ie5Jln9cvefOXgQQUSHdn1RsIvjmo84schqKf3vP7h_RlmZbry5rGkJ3HKTsn0EWE-GPRI43o5pXPc_tBnUCn29k4s1HRWNjviNcZOkYkHGRm4gqJnF1kG9RjjFlvW3kdRIj9SfDNaRy6OemyIegeZCIhcShGCnpHIFpYLnC4qG4HBsc0ubJhw1WFUOzgKtfKznQ_TdF0hUy9kXHvScb2hddJ9n-d7J4un8tQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jK9ZfQHgWy5sjbcTqQlixN3e8Ozc5-ac4VNNNtK4wYbu0NXYkIPlKyXbu69fpRcgYFfUS7F3P4FdNkogdPIEJ6SA3uh5Cm1FAdVyv4UYwhN5NIlY_Xu1IDkt-xZNGpxybEJP_3bTcrOero6Y2ygEBNe1GuMSgp96Wj_rLJVxBZGrcxqWxKk9NQhIHWB9al6sDAs-3caeF7DNvG7CXB6wFcUdj6blFirk7D6TsIqtzbm-TkBNQ4KQThQU-4K89z6Rw_bkR6onun_osdjlpu8P8v1B9SBfoEOD_CfZ_9WhkeaxHONMy9WclTPsMuiDdUdvWHJOLLwc9G2nsKVfnXQfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F07O1RYSYkx18BmAIYM8_9tF-F5EtPhS1_QCED331HFFuxgkNnreQoXSPjXVck1Ph3YZ_pphmuVEdtN86KtQJV-reDWWf58cpv39Pl26lWy85xmdaEbk1XUzrZnyAEg4TuJLEkUpBIykJUnhnCAqgQ0G1bVgONihtmgWOQoOIQQdBuJxLkekYSUGvILuWCJM1o0dkvpcPCI8oI_MUBRuKWYxSWjnZbnWgZadIpN3rStBPZIpA1lkH5xIQz5vPub5_sgjvqGpcaTX72WfvcYf_sUeBG-XuH0qotZIR9HbeJqXEiRG1s_0H7DxvFdC6aAgNVhFjOLKk3WZGVZotygbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHA6ZZevjiaWaxYTcutrI_KR0pyoCJuUpcyeancggpuGDh6ceEU52fI25JtoFy4BYYsC0zvIZUHC-_d2nynCrVE_wuOov506PnWLKaEow96c3umqCvqk_8LXlBb7BzhsDAF-UJhc1CSDGHbqlVDuRsHs2jHGNYQk90_OFDvc2Zq5e4LJJqrJe2pIlgddgrwZHNkeCAmH9hHmOY0-xKoXlbp8W9OGjIb97paSLgJf_407RXQM_D_6-U5JX9cZzwCQr0cPfPslBWVOjQPvVSASt8w2Ii8PCtWOihM7UEi4Iikuudc-6WeS-lndcWy4g-QVkRZf4sNi8VtJksYw75j1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KER1S3IcwpY8WQOT7yaVGEbbrs4ZHk1dqURCsTP5J8RGZteoqNI9_YO5TC0_t8l6CgjI1jVkw5941XicTV3RnJv79471XeiOShjzMO5F3VM2AwJLceI4gwtjDdBw6Dh_wB226PPIQ6mP2dOzmwgVd72xYOSfaoMcB64J-dEOa3Awu4TF5arfdli-NCKQuVCUfIvWWEMC0MwO8ijoI1cTeq09tyJiu9NLxbi3SXjA4cHfIBhH8tt4rYBj2XEBT15rpPF2bi56IS4pxxSrX90EvbuqX3XdxEUkWMXTFoHiLGBfKUSkuEmErPzhEKpVMsqCu8Yg8J3fTiAvRi2it7TFoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۲۰ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farsna/441035" target="_blank">📅 00:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLp8b1U3KDs1NSfi2pSw_XL_dJa13JS4EUKV_o_LcEQxk_sE2BRy6Kr3u2_lLZr5kWwLY4vFEMnoSxW0AcJEw7BpfZ06sO_ufHDL6EIwVoRfruyC8KDUAeyFhhKb6d7QUYekV4j9_KjysPTuL343fhWaV5K6lJyv0OMkaIx7hqX_sD7LwTssivzz0BwxJKmqhCHkVDCUYiJiWvJ9MDF5GSpezLgnG3vESwFqvq_-O21t-u349l1Oi1Tlhezo1J1VzTR4UUqypZnzY3S2ap5e5R1Xz2o4i1WYTiumq06-if0gxDBH6o1Ap4MVnTyJEs7tQJkhPCe4wAfenrx3eHDu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stGIGQWOWDSjelp_4VeYYuPES-l1Iiwzo8N9s0bNgU0q9VPyoVRdV71ZcTokdDjbHcRP6xDkCKsKXVNuSkhh4SChs73t6HvtU6GLD66PXh8lIGf6DS8r0drjpjVDjbBWmIeQdXhJuaE2y_dFmKEdmEeAShXm-MQLSoezZ7-8TibXhtLJ-PPKIwrS0J-Sj9_RAJPLY41kM-gSn6ik48FDEn_jPftRjNdcvmAWKOYlN0VDdBs0PeEUPtvbp2bY4p2gxwwfGBFp1K3RZijDc981JsRVIJK8yEFZrofCH9xrlHSeaQTh025ENOWlUGN2rPTfDGi0I3h1_SN-ouh3HW3Oqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dp2IfYxtXG0ayADCZsm_eFkdCsaCEnL-RdEe09AycMYLjxevDRLp2j5CyuPmvaqNAKIs3-CNq6zD3y9oM3gpd8jEOp5aODbe3niKwTJYfmqPB4swDGVrDeh6qHS_XErCQXnbvpz9PfqEbmRIXb0k4RjTM3JpylwKUMk2paAA0oNKZWxCMhQhJndXrOGmTRfkXwM_IEHoxcRspRCxv1nGubwMGDotTjR1arMzAwRvn6lXoQ3LG9cXc-PqPZaQNe1axdhuvmU9Xfn6cX2Iu-PGMl2bqVUx1qCLWiRiDgJtTonua9uj8BWX1vyjPPNmkxAedh_CK6Ym3OVwc-YecNNzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4axi7XzmYmBNNYGzDKRjSW1aUDJmbpkZxyFEL6Q4VzhvY8v4Dd7DT3-WSKDOVo6iYdqTx0sAJW8Oc4uen3Hzt89wd5T-QgnpOxo-ZzGmRbiVZPbynsfRSG2-0q7by8he71MNakud4xPRIiHIzpXGwhvv0R2T2_pJ4olElcaG4qTyl9ed81WCYXNfOcbFnzeMxgM-Uuqy4KfqB9TbpJANS4VvwfB7Jqkf_CYbSFrVj2Dn9kntK37uivV9PE8en1AKU-JkZdsjdMexmbqQIbjNhwmpO1yado27fz5bdJ-Jpo5NP2rh2TuOXiCPdtyPhYPPb2BRNvxq1XQHLxQM5_ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMONUT2gE3ZccucnprtFO0t55mYlgKhd8CPJow9ooYzFsGP5EjyKVMnCSgPs3uaVEX7KVfZhTmFBQs_LzlfLEC25T_EiHkKiFoJlpR7MWjrRBYMTJcBc680s-_9t1o6yAHe43UuF9Ep8zo2yXvmE_Iyf57h8UXRmAuFM0yslez4rO_AkmOIku6fXSkPO1qs--TAw5m1RvOeqiKiKbQUO4C80Cd0fdsx1GiRuChsJKkPtwhyVVdCiUJsIY67PGT6Zw2BsmIrVwYcfH5chkeq8zz_3N0ScshS5i4Y5EvXV0urFqMTnDlEIxdg9ibjiHT6BfT3XND55yGooScxvhFHj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvNPnkuKbwbYZ6f0Gg8LwBPyncciBEKN3DsC7xXgPBw5BJvjsEm0uJqZvlL7WZ9HXo72kQGiQSUOMoDhSEP51O9JPGZd2dTZ1NDIk6Mvsd_pDbLt9MTR-_ZsBRk8jqiwcQD3xZUwmsBeAEd0zs2eP3iyUNytmwcuiVvqzDjb7VwM7Uu8T4-vLiouPrSm4pLkpePNy9LlLegqPFSUtDgWntHDHMpnbcQH1xvssdJQXrmAvIq2FmU16GwdOISsbvdeFqWFitbx8bJuM3eHnMwfN64GYYG3X2oinlRhu_wol1fhM1qmA5oeQfJafJcIwcu77ahfSeQyI84O26yoGfSLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJBgc4If1IQ0Xy7-dDBDxKGjt6rOaRV4vlxwoYyMGZajYyspxABl07VgchFxlTZvrxorm46ZLqFEC5huY5H9g1xAiCsnMCJfBkgGcgWwjkyhfOjn5g74Lj3EatB-J8kPCq-366aNXsZ2iZnvgAp-xUXyhDB8WQ_bX49gfq4wlzsLDy8TugN0Cr2c_WjLHjmzLDQIqVqyGGDJRKE2I642_t-eiete6XJpSbiaYsrYDmt9SXIqxChzghJTlwcAVJTy7u1g2IFVdf30P37hi5kSaph39UHIRn7cfF9MLq_HDpcyxfaPN-cuZklmlfVB6aNJX1egVy8o_My7tvI12osZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Or-UNRBmTn80WOqKhb38QB6N1L77VDx_kRuOebo6lQtI38Tvd2CamNd85kdrvH83gQazgm8VSxO9gA55U3CNNiznAEq1UJms8EdfYU0zhe5BuGGabrAq2j2QSMqLNyxKNmNLuByMhDCbvuRsToah0BtniKcUvp5MECO015r0aINMcu6l79Mt21zR7pMNpIkMlRXBA-WiHugy8lIesa3fwXw9kMq-eM2codFJV9ZA-W4fCh8iEvDT96bDzVm2h0V5Db6-TnVk23jM4imL5wvTfOFjh-HSHBd9cLQstOSsjL3Q80xRqCd-aY4N_P75X6OcmscxXtpNEs0riAThpjwEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxfcdlAHtXRVeMAfS-vEmVh0bvTLNOAy5vp7DYGYJPsMSfQhj3sy6wf_ZD3tSnR15tGl0VoLRRK3xn1CsP-LHvkD_y9rRaQxzFgARrTD__1m8XBAWBnCG348ESpnGH3Y7Kf7K8hUy_8O9JERb-1EB4O6tD8sb4K0ecsK1aLb7KmKkgpVwBDjrKq_s8QYVqfACvXkxAXB_xppn89S_Xh7Ds-ZsI84kTHyiUbe4rihLAgqjq4G_quYRlHiKu2Q0JWOix4eRaSqDXU4XR4j-Hc99RHnUKwLCgIeh4NtJWrICjZ3nvyrHDF8F-vbXPY6FGy6x7vou35v48AgZ0tbpG4ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d72ZfOP5zP93lCLDe5sZvxaQrzdy06DedGeJ_tG0u2-BDU4VHbFMUBmkpdsyA2FWwRbs3dZaKWq88JnZd8c6X5tdTs8sCouXqlGTiTxhf8HK1GVAeebdQC1emTFABZ3Djo7vJ-W77GLJpVzyw5cQXn7x_Bj6b_AeHPJIctBYq2MAivqzc09Hiv90WEOuadYCa_xofAJXagwo0m9mPLmGhWj50y_gU07ty--DtQzRGP5AAov7ZW0ukl9OEHtUgh5se7MrljlC6JP6EZ_kNMhvRDURwq5GEpasexw6lz6PSY_py9oYAulH0sm-ULrYPHjrP5afNC3MElGh_0SFDb3mTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/441025" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شلیک موشک از جنوب لبنان به مواضع صهیونیست‌ها
🔹
رسانه‌های صهیونیستی می‌گویند در پی شلیک چندین موشک از جنوب لبنان به سمت شهرک‌های غصبی در شمال فلسطین اشغالی، آژیرهای هشدار فعال شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/441024" target="_blank">📅 00:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reBNlBhimjRez7RZNxV8hQYts4vjNgb3jYrjCYI0N6WyjP_B7RrdeT-LemZjccF5621rfFXvEc7LwomLhE-7GbKMsXnbvyMNnSD8wknR3THLeTgR1nOT3JaWpV4G_BTgwo1ooH3TZa-MKdE4ULiSjy_YWbuqEsZTEIs-54A_mfy_JVWXtZdLaEJR1xqkVyxoDigI0JWnqEIh5OcDArsbihIG94Boo0kigWHPEIYp2v6zkWHK6ahLLsfvF7DxxPAYyb4_tEAbNrZVeXJq1VaPedrKQjIiKlVt7mSM-0D_GTYgixjnaWY1YSpqogvr-vGymSuV5ENYyPzlM2pHsCxnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک از جنوب لبنان به مواضع صهیونیست‌ها
🔹
رسانه‌های صهیونیستی می‌گویند در پی شلیک چندین موشک از جنوب لبنان به سمت شهرک‌های غصبی در شمال فلسطین اشغالی، آژیرهای هشدار فعال شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441023" target="_blank">📅 00:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس این حکم، این دانشجو به اخراج و محرومیت از تحصیل در تمامی دانشگاه‌های کشور به‌مدت چهارسال محکوم شده است.
🔹
از جمله اتهامات مطرح‌شده علیه وی، لیدری تجمعات غیرقانونی، اخلال در نظم دانشگاه و اهانت به پرچم مقدس جمهوری اسلامی ایران و مقامات کشور عنوان شده است. پروندۀ قضایی او نیز در قوۀقضاییه درحال رسیدگی است.
🔹
همچنین برای ۶ نفر دیگر نیز حکم بدوی اخراج صادر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441022" target="_blank">📅 00:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441021">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/689b02f0cb.mp4?token=KgCNxsJQ65MP5eQekz0A734cR6NmqhWRnQiktzZWeADdjf7zFBh_JCRLT3LRG3N_rntzgQbKYAbUXZzmnYYiDH_U1nLJzz0D1oSd1w2F_ghCPEwtbhQeu9Di5qx1YuDESRmoAlV2YKnR0ftAgMI2yVbtGIw9T5loUiIUTFhkKHLwL9d_9RQIFUCc-B23zfgE1WDyAVnj4dB_-qNCYIGPk5iaWQZ4hNr9TFeLjF-Uv4ApJPc0DBw3IXutQxSpXpk3u5mjNqSXqF8JGeIDSBTnY0G63jm6m7epyyRIgAeIQIblxgYLUd4i9mtP90tl3pWVffz5oiyv9I-1JNJRFh1ICg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/689b02f0cb.mp4?token=KgCNxsJQ65MP5eQekz0A734cR6NmqhWRnQiktzZWeADdjf7zFBh_JCRLT3LRG3N_rntzgQbKYAbUXZzmnYYiDH_U1nLJzz0D1oSd1w2F_ghCPEwtbhQeu9Di5qx1YuDESRmoAlV2YKnR0ftAgMI2yVbtGIw9T5loUiIUTFhkKHLwL9d_9RQIFUCc-B23zfgE1WDyAVnj4dB_-qNCYIGPk5iaWQZ4hNr9TFeLjF-Uv4ApJPc0DBw3IXutQxSpXpk3u5mjNqSXqF8JGeIDSBTnY0G63jm6m7epyyRIgAeIQIblxgYLUd4i9mtP90tl3pWVffz5oiyv9I-1JNJRFh1ICg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید باران در ورزقان آذربایجان‌شرقی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441021" target="_blank">📅 00:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaEgvyn0_49Qz62C8rDqyod2JAtZuOlppNzy7ZsV4ucWhsOq5j9G0ONNVhPKoAzVP7GwYl_ufbi58nPgGNK_rn5bACztl_ywWF3dS4EvJdoLERcLyE8iH0B0a4RAQKysmBq2REWpa7IShRxcTBUOu9cin9UhEKxtUXffSCHVjFlZ02Qe6W-_ttxW9eW7s_kM_9HKxx8GAmrnyRi9vP2BJWbPjGhqBSuLJKvZljHmXyrSqoFRndkh46iKnjSvR2_OkCaAIZHVq-mN-SrT61m2Y_9xF1W90rTMjn5USLa2Rjn2pVx6fG3DWen7J4KR5--O1uxI4i9pm-3iJM4U28GIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSaen3f9fYgcQ851K44halvUPw33N3LmHtzPAAt4FECRJeEempYUECoAxEMfuVtacF__rj9CwNnuXXobD1E2IS0lUkbKbec5NNHnIeG4xNhBFhhCyszE2K2cofTcyiVB9Nb_aN6Dlw9Ek9VpnppOnEAG6mVtjFc2ID-IvjpjKQ_RR27arbUuYCnt5PA50G_b1440A9WyDX2i8621qQNMb-oDnndu1l-YHoGC2G9Oug9ry6D-dpNmX-ZocLCfbgue0dGY1VyKeXQwGkrObq0NlqwUV7qMWhlJbhjIyAtFBQ5ph05chx-eQs7HAC0H2OJuI-f4JjPKCqcvUgkmg2zY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2tHF8PDoTgoUsigAPuKdSylu-8FMM5WixjbU3_BsfGnd5bkw-4CdfVFH9lE5m7v_j9xUETub_clNQ8ET_1J6ZWkP--w3lPRNF8nDsUEvld5vv6v7rnYvC-vwyrM1hXZznGEzXxxLMmHUJQmeCu526hoO1IXXaczeF4a6QhX_4jtICAN-PjRvR8khbk2rjD4hyV0g5pBYDugS5F5Tf2BYKZJZbYQ_EKp9RxKo2CQvh3QO4WHfp3ENRWpJN4nitTOWPJ13IhGELnbKvSrj5YatdGLoZgZA-9eWSmc2K2ljyo6FEAu1WnXj2C30dmr9kgbCV2ZZ_ruqo-nfYkG1-3HZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C983_1BEnH0sY9YLLgHodAIXVH5Nu-BBayBfGAjsfxBxvEm3f2CXExPNvWSE4lMTlGYDN1zXgNUHaWSHRIOv4ryJKjaHmye2BZjrG66InbJc41tjykthH8NAgyR6Im5YtcxrTPQEXitNiuVdcd7gCPJ51rqDTvT0eHNzdbJcdwYwol63mTnjuzBJEK0fmSvPGxSpTK6rFuaq-W3ogCyWRUZdW6p6pUPhdMeKnh5AmkUbqPpUiCuLA7UIwOC5S0n6W3CZpGQcA1jWfAD6dQgriaoktFCr-fxB__p0hjGv-TWU3DK-2hVSaRSNBotK_v6qfN82umo8WU9Zq7tTS8qVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m670SNomfj8JlnlyFXciQg-MTk56Z8Z3EZTGSKKWBQdWfAbAIRZzCcRtABbAUXeXOPgd-f5U7vQH6W2umS5VK_WHtXztHF-fYm8d7nJd9OD80Bn758nnm-k7igx1qopEvgCuGUNwHs9KjieBqSRIL4PoZsJsicXaixYX9UGPaYQvVM9e-sLCqCujM1BFqpL04i_1JhjRGbVR5Lx-YutwjzqK0w-cJ89VJBYiLUTd4hA7WmOFR6ItV71tKfDwJck4nfvyyDBRW_uTwkfjo-wb6olePRngVjkP9MfYvqHguAvdiEHuUvoWycJQfA8EOdBdrxii9Wl8oqXLX6pCZa0sNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCPORwnAPAx5OS_xtpOTQLtIF4svfH136ywULZ-lEYx0IJ0Ztam2aDd4ettf06iuscVw0Lju1RmWBcVsKVq_lgeDWUEwTcM-m5qLNrFNrF8sq9XEGeYmQ_PtbDzFtX7zOJwniHWeLwrbO_Rv9DCbZ7GqnkfuIhrErK1xSmnGyPSZP7j8kMWJq4PGNZODDiMw9uF-cWuT-8H4l1zZ0-SW6jx8VUp2qutMiTTbE867Z7QJ-pAX45pSIHSEFah3g3qIcs6RSPc8ZtgWmGOUtyZKMHC3Pui8tf1WDThH0Y-DVmJ2J0CPJbHElW-SwEfQpLR7OtOKjlPlpHiLoAvSpFs_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmqC3qwUEGreutj2VsuKvwVhI0H2LtYTXeZRj0LVHrg6elwW-gyARV_6QdkNSyyb7I-o4mOa6aoUC2tJDcb9Rc7H2PDbO4E8vWvyRzF-T6HrN_fK3m5jpVIwEFFE2pNN6krl6vv5Fbzyp6nO0xjxqmRdb3LaIA3ZDz0M4Rozv1RuvtjJKOrCj9lCPkwHVppW-lAW0nPOk4Sq_-YRXtmCBv5d564OGAo4Htms2VW5vE56qQBddd9us8FHga-8ojD3zDi8A3IPD887E-0vvJpL-c_PsX8PUe08Wg1Q2iCKREiwilrtBxbcqYe2Z-lGaDvMO-5gyZcQgy1BXI3kku0Q_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم تشییع ۲ شهید پدافند هوایی ارتش
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/441014" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441012">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5sqlbh4gruNWWsbbsjHOs_dIol-Hqcgxgw5h-yZL3ZGj0bIubYJZbNTniXJvAkl5wHFqOvZJ6pVO1uRq3Kes3v_8Koinwv_0zO0P4iTC4tO-OMyMSwn_L1LdTUKl1IDgZ_rwDa8KEsWOyvSeHLQ6kNkeIxN1q8GarcrID0HTxIVcN7m-veowSiH1EJFqswj_GYGAh3taEI9m0Dp3tu9X00eM93MYvMIbRIzMoI13K9a-5_NpDQv0PhiSDjOI4Py-i2cIsp9QOGhk427KeS9C9zIQ4rfKnVXt0RJVaDtn90yEKLYd01EL2k3I0lAqQvFGMIcBX8B5rXGqS_e6l5yhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای ترامپ: ایران بالگرد ما را ساقط کرده است
🔹
ترامپ: دیشب، ایرانی‌ها یکی از بالگردهای بسیار پیشرفتهٔ آپاچی ما را درحال گشت‌زنی بر فراز تنگهٔ هرمز سرنگون کرده‌اند. آمریکا باید برحسب ضرورت به این حمله پاسخ دهد. @Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/441012" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441011">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جلسه شورای امنیت با موضوع تلاش برای احیای کمیته تحریم‌ها علیه ایران
🔹
شورای امنیت سازمان ملل متحد در حال برگزاری جلسه‌ای برای بررسی احیای کمیته تحریم‌ها علیه ایران است.
🔹
این جلسه با توجه به آن برگزار می‌شود که سه کشور اروپایی مهرماه سال گذشته ساز و کار…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/441011" target="_blank">📅 23:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441010">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">جلسه شورای امنیت با موضوع تلاش برای احیای کمیته تحریم‌ها علیه ایران
🔹
شورای امنیت سازمان ملل متحد در حال برگزاری جلسه‌ای برای بررسی احیای کمیته تحریم‌ها علیه ایران است.
🔹
این جلسه با توجه به آن برگزار می‌شود که سه کشور اروپایی مهرماه سال گذشته ساز و کار موسوم به مکانیسم پس‌گشت (اسنپ‌بک) را علیه ایران کلید زدند.
🔹
قبل از اجرای برجام شورای امنیت در سال ۲۰۰۶ کمیته‌ای به نام «کمیته ۱۷۳۷» تشکیل داده بود که وظایف مهمی در خصوص اجرای تحریم‌ها به عهده داشت و بدون آن اعمال محدودیت‌ها و ممنوعیت‌ها علیه ایران عملاً ممکن نبود.
🔹
نماینده روسیه در جلسه امروز با برگزاری این نشست و تلاش برای انتصاب کارشناسان مربوط به کمیته ۱۷۳۷ مخالفت کرد.
🔹
نماینده روسیه همچنین یادآوری کرد که دستور کار شورای امنیت در خصوص برنامه هسته‌ای ایران پایان یافته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441010" target="_blank">📅 23:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441009">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnftqcC-v6FaCpjOyDLYnUROUhl8JXSVgHC8vuzQ4PFQUhg2kul_Yoa_3dhcxXfUB3LpfYLenFpxSm00tHK-3pwWOcqcjfm4Dxl-rBCcC6yMgpeijq7hPTshDnXY6halTFGfePOk-CsCS285y2MMNG0TzYRILGJIkEzr4bBKgNkq-lMIDZ6qchCYsUdDNIEGUCvZJGUCYPA2bscPIgDnn2B7Gd95PcLb7hfInmhx7QqQmnrtNFek34UXauHoz9niSrzCbL3jxAcmdeJcpT44FETCKdr6z3zdp1PO57xXzhlrUX4ObjjO6ULF44HzY06YPozGSxxysVXWabad9baj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ارتباطات طرح خودش دربارۀ وایت‌لیست اینترنت را فراموش کرد!
🔹
ستار هاشمی، وزیر ارتباطات، امروز در نشستی با صراحت از لیست سفید اینترنت انتقاد کرد و آن را طرحی «پیچیده از نظر فنی» و «آسیب‌زننده به نوآوری» خواند.
🔹
او تأکید کرد که با این مدل مخالف است و در بخشی از صحبت‌های خود با طنز گفت: «در جلسه با طرفداران وایت‌لیست، به آن‌ها گفتم ماستتان را بخورید».
🔸
این درحالی‌ است که بررسی‌ها نشان می‌دهد ریشۀ این طرح به مصوبه‌ای در بهمن ۱۴۰۴ بازمی‌گردد؛ جایی که بندی مربوط به وایت‌لیست اینترنت، به عنوان پیشنهاد وزارت ارتباطات ارائه و در طرح گنجانده شد؛ موضوعی که به نظر می رسد ستار هاشمی آن را فراموش کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441009" target="_blank">📅 23:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441008">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEDK3Ck344tTa6VDzb4YeiEfVg6Vxg9bNS87N_xsHhR_RrX8mzw1YzmiRh9b5R4BoMhOHd6lpoQj1uP5M-t_Pcum_ejFDRbsGdQxZpMhV0-2uHRDm51O3i3xLu-tvTLyUJfaRwABF_pk0i5AP9QrgielSMKiEk_N-kFB9Yh-aDE5h-qhcJp5U2oAKZqJkPJ0SZmLFNKp9w7uDU0PWNi-ewxGfDFm2LZYdxJuqd6kY-p0ZJbQ6hXJTbPDYtw2uCXRcElvGHoEayGieln4hlmDAp_sGj7OLKS_9FdwEFZEC32oX0n6OneM71YgHko1opKWwqXXh6K3meSvlSWlZ_Aqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محیط‌زیست بخشی از منطقۀ حفاظت‌شدۀ بهرام گور را به یک معدن واگذار کرد
🔹
شورای‌عالی محیط‌زیست محدوده‌ای در ضلع شرقی و جنوبی منطقه حفاظت‌شدۀ بهرام‌گور در استان فارس را به‌دلیل آن‌چه رفع مشکلات شرکت گوهر‌زمین عنوان شده به این معدن واگذار کرد.
🔸
منطقۀ حفاظت‌شدۀ…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441008" target="_blank">📅 23:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441006">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyabvQPlEbmxdk0lv_hDt1EbVEfifZjkHuvI-vJLrLFDdtncsIZO47GZfKUSwk_9aUbiCj1_O7qiBuDFt-EhSS2cam8l9Z_Y5pgA0DpK_g6EK9IXB56lti5-OLVZd-ojxM3ihEDnQnEgEW6QkM9ayZOAh4prd1AjbH_CPScoBvQZNgiKJMhaz9R-EyZ05bSTnB_UuNF80tBOBxcRcxI44MrhTBR3ZeKwnnQ-EboXBks-bk_1Duj3t3weWTpJjjETaAFwe8nStg_yuWY62lobHINRByy5TPexb9l_0dHf_9eLuTBaex4G0VDI-D4fkJVGOOPUhjSZzKCZUUtkmqOhRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdoiM2--s4XbYaFpeRMeSg7A0CSdomJfBSbYUSsInhMRXSnGY63yvZClcJBK8eQz031nXp4nfEP1x2ScR-QLrmuPS6fjX_7jf0u2FU9peTghzwx79mLig7Lh5y2BRsSdToI5189dKgWlYMbekFStP3LmkdEuwYgZTUdvK_pKZYR3m9KOpXTQkxKM9uVqOjfDqrGOlw6gVl34aZs5l3d6u_0CT8CluzXqJY9uyLsamuSfZK4-Ghsubo1xoo6CJA2sa8jT3N66LclCOMWeLaQN1TEj97ZF9KIXPIVrMOaBoXj7COawUoOVp52EoKpGDkPZLCi57z4iJkJfLI3t40B2_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جزئیات عملیات نصر ایران علیه اسرائیل
اهداف مورد هدف قرارگرفته:
🔹
پایگاه نواتیم
🔹
پایگاه طبریا
🔹
فرودگاه نظامی رامات‌دیوید
🔹
مرکز پهپادی تل‌نوف
🔸
همچنین در پاسخ به حمله به «مجتمع پتروشیمی کارون»، «مجتمع صنعتی بازان» رژیم، هدف حملات موشکی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441006" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441005">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43976cbf1.mp4?token=Ys1IbFHjGaON5Kfm5iX228KCaIjDAceHPcUPIX3uTQeHwAxFqRwFG-eV1nFkyWl0GZOprdwbVYsmJ3xDxwaSyZym7C1SxY-IlMJsMHVPusRNWg68tumho_yuC7gqelH9dS9RPVetuiU6fanAZlPc8PJfF2AIFgez1xFh4BPdsYXPJs9czP2T3Qt_CZz6kLf7rT1V2DtuCfy4X9EHBmbu7fdVQgfsLjkUzGrl6TycDz50-SLDl4l5b-MjiXh0gqDAO5u6KTHZA8xhLsMA4Prn2gEeR5SIXIisnQbER81OJfcax1CFOrq2js8nZ68DeSEdLm30fyJwM_Iai3Jaa7iXBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43976cbf1.mp4?token=Ys1IbFHjGaON5Kfm5iX228KCaIjDAceHPcUPIX3uTQeHwAxFqRwFG-eV1nFkyWl0GZOprdwbVYsmJ3xDxwaSyZym7C1SxY-IlMJsMHVPusRNWg68tumho_yuC7gqelH9dS9RPVetuiU6fanAZlPc8PJfF2AIFgez1xFh4BPdsYXPJs9czP2T3Qt_CZz6kLf7rT1V2DtuCfy4X9EHBmbu7fdVQgfsLjkUzGrl6TycDz50-SLDl4l5b-MjiXh0gqDAO5u6KTHZA8xhLsMA4Prn2gEeR5SIXIisnQbER81OJfcax1CFOrq2js8nZ68DeSEdLm30fyJwM_Iai3Jaa7iXBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم شهرکرد در تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441005" target="_blank">📅 23:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441004">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa0e7109c.mp4?token=kM9XL3DYLhLLif5kF2Ia9uNz5toRq-IlOHILjond3CrXeOXsTQD_rH5_lF1YsVej1qDDqAm-QhLdzNCeA3USpkYKWj6AKhKt6bexJajQO05qQEQlhfuP_isVZFXCq15zi38swHtz-iAnHmm9wXt3vlgIZOBK8Gm3O_unDaVpjCc8s8wkDtWWiCZmXw03mDgmy_zx81DROiHVpiXUZIdhS_z9UTWyQKtm7upYMVPLPEUEusclfOc4s9Y0xdgViDREtgtPpADRLaCAmOblQUpeLWNWuoyMcuqevgdycViSgAe7OPZliScULaRAqY61EeafVFi2-snCe7VqNrTpqXqSFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa0e7109c.mp4?token=kM9XL3DYLhLLif5kF2Ia9uNz5toRq-IlOHILjond3CrXeOXsTQD_rH5_lF1YsVej1qDDqAm-QhLdzNCeA3USpkYKWj6AKhKt6bexJajQO05qQEQlhfuP_isVZFXCq15zi38swHtz-iAnHmm9wXt3vlgIZOBK8Gm3O_unDaVpjCc8s8wkDtWWiCZmXw03mDgmy_zx81DROiHVpiXUZIdhS_z9UTWyQKtm7upYMVPLPEUEusclfOc4s9Y0xdgViDREtgtPpADRLaCAmOblQUpeLWNWuoyMcuqevgdycViSgAe7OPZliScULaRAqY61EeafVFi2-snCe7VqNrTpqXqSFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با رانندۀ نیسان معروف جنگ رمضان  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/441004" target="_blank">📅 23:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441003">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaZlbyeJHhv3yeKQBVN1uDE5CoIDJLCycNYu6vzhnnls2BnY0JNH8575CKsHwDNQwTNshLs131JDmhLREhXCVcn0AoGwU583UkbUfp9koLWV9vfLno_9BsFgvBk4W8-QGhIl__4BIHKwpsWULPxtsDpRJbAG-yY-BINLs4Ll4vR-4ZHptq0v9sdCZDstHwPSSUylK9KQ1_amxMLLEc2LPewO6-EWmeTzxKmWTPGLZ9RSnP3KD0sSQHlRP5KfLDjuiFzCb26GdxYY16pi6ZsaT3HNgfT2r5V5zsuIgrHMBv6StHhjvv8w5QGznaByeacBjcOyM7MnZjVyDA5oDLzDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفادهٔ آمریکا از استارلینک در تجاوز به ایران، هند را ترساند
🔹
ایندیاتودی: هند روند صدور مجوز نهایی برای آغاز فعالیت تجاری استارلینک را متوقف کرده است.
🔹
اقدامی که به گفتهٔ منابع آگاه، مستقیماً با نگرانی‌های امنیتی ناشی از استفاده از پایانه‌های این شبکهٔ اینترنت ماهواره‌ای در جریان جنگ اخیر آمریکا علیه ایران ارتباط دارد.
🔹
مقام‌های هندی نگران هستند که استفاده از تجهیزات استارلینک در جریان تجاوز آمریکا، پرسش‌های جدی دربارهٔ میزان کنترل بر این شبکهٔ آمریکایی در شرایط بحران‌های ژئوپلیتیکی ایجاد کرده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/441003" target="_blank">📅 22:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441001">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">یک منبع آگاه ادعای اسکای‌نیوز درباره پیشنهاد جدید ایران به آمریکا را تکذیب کرد
🔹
یک منبع آگاه نزدیک به تیم مذاکره کننده ایرانی در گفت‌وگو با خبرنگار سیاسی خبرگزاری فارس: پیشنهاد جدیدی از سوی ایران برای آمریکا ارسال نشده است.
🔹
اسکای نیوز امروز در خبری اعلام کرد که تهران پیش‌نویس جدیدی برای طرح صلح به واشنگتن ارسال کرده است و گزارش‌های اولیه نشان می‌دهد که طرف آمریکایی آن را «قابل قبول» می‌داند.
🔹
پیش از این هم العربیه با انتشار خبری مدعی شده بود که تهران با انتقال اورانیوم غنی شده به یک کشور ثالث موافقت کرده، که این خبر نیز از سوی منابع ایرانی تکذیب شد.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441001" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441000">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
رسانه‌های عراقی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441000" target="_blank">📅 22:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440999">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsDY4D_jDBcISvCSlyvBzN2SR-TUPbf5RFICSYBttc45t1OFwRuva7f4QEj8MFWox4UMLqt5JUUSJSVefDC5lWNsTqcEOjPWH7SyPBAIETWS6vBQTHrEmyZnpoX6KueyoQ2dsV2XS2EbEW5NZPpRWbWYKmsSXMPIlAwaDGDrD48yN8rQP1UGJfqRVS8lOM7wf4Ze5B_57fvGdk6rcINDCHOf2k2IwsX48tkfO9UIcaUj5FIA-xlY-eaUQn-20Zs5cQ6NYgl9JEu8I8qCXg9F3kvPnrd4D84hN3xISBRanVX2dKbyQNObl2NVhc8uvm0_v-4Z3Lt-_wb84FOi3NfQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نصف نفت ایران را خواهیم گرفت
🔹
وقتی از ترامپ در مصاحبه با ABC پرسیده شد که آیا آمریکا در بازسازی ایران پس از جنگ کمک خواهد کرد، او گفت که کمک خواهد کرد اما افزود «ما نصف نفت‌شان را خواهیم گرفت.»
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/440999" target="_blank">📅 22:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440998">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
فریاد حمایت از لبنان در ساری طنین‌انداز شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/440998" target="_blank">📅 22:19 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
