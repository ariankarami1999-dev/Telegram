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
<img src="https://cdn4.telesco.pe/file/A7_ipOrasgL6qWx2wBYGUP7FhyKFDXrn_lp_YRXtgF9QItVtaKUlb8mCq0vDqY2UiIYGl3-q-0Cn3mC1Zf6YzEwsue30rqbHWMdsaloYTPMp8SQsI8IIcoGJwlA0vj3WXxNChL79y_MuFS0iB5s3C5mDoYeSQGG6L0zBjYs52LCVTwNc6BbJGZL7Hq4aAMjamWnibdH-zFFTpeVXc205_Oom8x1xQcqlFjPUwPYXQ5Lwg_BM5gXH6VeRJyRqIV7UZaNGfxD6LbdYu_KsdqmmOLuh9qvg3Hr63m-3Ye5ZrE-sKW3WNZJ3Q_KFNcFUoecuJopG4jjx-qcxHLRxPJ5QIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-21432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حملات سنگین حوثی ها به تاسیسات نفتی آرامکو در عربستان</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/21432" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21431">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">— پلیس بریتانیا دو شهروند ایرانی به نام‌های رحمان صالحی، ۳۵ ساله، و سلام احمدیان، ۳۶ ساله را دستگیر کرده است که متهم به توطئه برای هدف قرار دادن جامعه یهودی در منطقه منچستر پیش از یوم کیپور هستند.
این دو نفر به «آماده‌سازی برای ارتکاب عمل تروریستی یا کمک به دیگری در ارتکاب عمل تروریستی» در منچستر، در تاریخ ۲۰ سپتامبر یا قبل از آن، متهم شده‌اند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/21431" target="_blank">📅 08:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21430">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC3i5pST81T0Bs3LYz5JPjnxK_bbp0YrxTQmMKXtXMtAvWV3ydqTlrFNb4inuTqx3geC_jli4fVUt42AzN_MWmfJx5i5KzKE0FEt3U5NW41nLBOcNZOD1dVp4BjH9-W3GYnCUKz7lPcThGMwfWKMyut7pqEvBkGuCwzAuSnxffD9LXXglYECypUXPbl5X2S0q-UNvpZPGnlcUwlMjCVuuUm1A6hlZFHxd9Na0YNkPUo5u_eDRjPfggaxD_StpSyFTGIyr-1rBjtrRPtPZH3gMAuCEFfaZoneUPHiiTyJiewAf9eykuah1HhNbwYd6WxQpCLU0qaKY-vFu1N6lnaXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21430" target="_blank">📅 02:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21429">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ادعای جدید ترامپ:  یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود  به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.  ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21429" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21428">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ادعای جدید ترامپ:
یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود
به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.
ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد و این "کارخانه‌های مواد مخدر و هسته‌ای" به‌شدت هدف قرار گرفتند.
بر اساس گزارش رسانه‌های آمریکا این نخستین بار است که ترامپ به طور مستقیم از "کارخانه‌های مواد مخدر" در ایران به‌عنوان یکی از اهداف حملات هوایی آمریکا نام می‌برد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21428" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21427">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">«چرا جنگ می شود و چگونه؟!»</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نشست لایو لغو شد.  در یک پادکست مفصل، خواهم کوشید اوضاع را از دید خودم بررسی کنم.</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SBoxxx/21427" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حمله با سلاح سرد به یک روحانی در رشت؛ ضارب متواری است</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SBoxxx/21424" target="_blank">📅 16:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21423" target="_blank">📅 15:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21422">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21422" target="_blank">📅 15:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21421">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=g4Nc6vcgPQ3AYF-ugE6slskcbpF8ulAvrd6zfQJbt_4WQMIoNty2q_YGAkGnjFTeI6Se0cvvt1Ixq1VO4Ni5yx4suI6n2k8gZ5U4VwNeja3CXI3HmPfdoMPqWUi3TxjcdFK5hNEQUDU0RBVi_f8a0-1q_e5l-dSzXTxkktoDZstN1tMYKp7c0zx7hnlcgfe5pSOaz3kRZrfUHRIw3HxZngR7t1XO5fXGcBJ1I91a8X4_iN7K2Ewhlw-okmJHMy_bNIvxQUa1VNvgAs7gnggzNOkajhvuz7VWo1KbfCwoM-3H0tplcsdvX7i6vjRCPMZRTZ_ZG3UQ2Zp7s25t6aMagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=g4Nc6vcgPQ3AYF-ugE6slskcbpF8ulAvrd6zfQJbt_4WQMIoNty2q_YGAkGnjFTeI6Se0cvvt1Ixq1VO4Ni5yx4suI6n2k8gZ5U4VwNeja3CXI3HmPfdoMPqWUi3TxjcdFK5hNEQUDU0RBVi_f8a0-1q_e5l-dSzXTxkktoDZstN1tMYKp7c0zx7hnlcgfe5pSOaz3kRZrfUHRIw3HxZngR7t1XO5fXGcBJ1I91a8X4_iN7K2Ewhlw-okmJHMy_bNIvxQUa1VNvgAs7gnggzNOkajhvuz7VWo1KbfCwoM-3H0tplcsdvX7i6vjRCPMZRTZ_ZG3UQ2Zp7s25t6aMagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21421" target="_blank">📅 15:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21420">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21420" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21419">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">واشنگتن پست:
وزارت جنگ آمریکا برای اعزام 20 هزار نیروی نظامی دیگر ارتش آمریکا به خاورمیانه آماده می‌شود.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21419" target="_blank">📅 13:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21418">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صداوسیما:
درگیری مسلحانه سپاه با تروریست‌ها در راسک
برخی منابع از درگیری مسلحانه میان نیروهای امنیتی و عناصر گروهک تروریستی در یکی از روستاهای شهرستان راسک در جنوب سیستان‌ و بلوچستان خبر دادند.
نیروهای امنیتی در حال پاکسازی منطقه و بررسی اوضاع هستند.
تاکنون جزئیات بیشتری درباره وضعیت عناصر تروریستی منتشر نشده است.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21418" target="_blank">📅 12:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21417">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFgRsgY37SrdABBx9JzkKd-OHmmG-mSlqLI8jKyXWnKXGH87VsC7khf3yNYHrMSgxguXXNwpzsJJM23zc52HkusUJFExoNN6YKKNNpqj4PTfZZY2CPFD2R_R0ESZMbN8D6jSnRhg2raxozXzEXHpk2BbYlfxhe8XYSdZ1Vh4R5YfLqY8UZ52ZgBoZ3aiTe2XNCnS0bXYw0qwaLn2h4DazUpvQvu4OLyZ4aeLyDCvrbP--UxuyTmOdb92Dn_kIboHp7klwlEj6okMBVVRXr7rUa9xQFPoAsuEWKR0gK0OUtNufCWbc0F-utahTQhSDn9ES-95jDuLnjkuB63ZbhnDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21417" target="_blank">📅 11:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21416">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGlNcaCp_kNyMH0aumecEDsJZVjUuADIv8yx0Sp-D14XOt3VX3kyqJHRueImEJwzZf1DU3y_sBeynl68eoNHDZjwkh8GpO29TDM_W0eXDRH9LTCqRQzRJZt2Q9Qd9enwFa6QEMbyeHG1a8M-6vKQIsemQCkwaQFvkOig4iyHzBgXt7L-Y_keLCnAlccZh83epOCNJQesrr9Rbrk-_cWyMCPC7EBrzNuk_wXvZaOIqbLMsAPQXQyg9NLE3AB6gWGtz7i3Ogj-TLbhqg9lGb9N1pYWJuxT1n8Ips0kWEPTZzn-Ti40Qcx4iCz9dbVwur4DLl5CwvVoapT_4ubczNjzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC هم تغییر خاصی نسبت به پریروز و دیروز نداشته است چون عملاً قیمت همانجایی است که دیروز بوده</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21416" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21415">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOfVEIp3Jqr101KQ8h9ERSZ5uC6QaQYavmzDzPf_Cg_gDaBguoBC4JwOQaAMSZFbCSugPbbyA4Zgfs6oRvSQL8nAbrfYr8jplMXTwYdZ9CXTS6MT6TYU1O0HEpBHxGvF2VbX1BPLN_ouBjYkJ0mWSEONlRf6IXAzU7g_LHQz-Bggy6DKVZ8pEXll2ELcQzlSw2lg9E4BzoitP8Q70AegnrDwJV02xz1a0fyJPLt8-tVL7TK0GAb4wt5jfzgEGumYOcmjk9dCY9cF6px-hQeSh1EiAiv36AqApF0FbP5sp1ZUTegmFTbm1yQqjnPlHwQXqkvnDbfXqMdi9yffKIajZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسط به بالا قرار دارد.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21415" target="_blank">📅 11:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21414">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگر دوباره به پایین برگشت، تنها روی محدوده دوم ۴۱۴۸ ورود مجاز است.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21414" target="_blank">📅 09:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21413" target="_blank">📅 00:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21412" target="_blank">📅 00:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51530cf576.mp4?token=KaZSmvxMXNTZp4oF_8pEEGnkBTIB6EcRKsask1QSS0UkMGhhM3bNljTJ8rXL3Sxd3hSYJOv2mqURIsgh8KD61dTZQV8Qjp0DS4IxWYhaLcIDOKOS3tHNnoW-5y79bsH_dxSW31_Xo3TDXk03F3X8GFYR8v5PrUR8u3Nab70qVO8Cm8XTBXk-jF5i86YiKpOtkpf-M2BjsmSEmV1RabiiYtHmWJJLB5f7yThYtnKR4RGhvyBUOF44ATZUZ_RDsScNLlFMRRCslBg8hNri4fWJQ3uQWw08ZdhDzXXhbO1Ped4CFOKxZ7YQ5mGhjhvWjH7nppcWj5Nr9DqA-i-zlOkuPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51530cf576.mp4?token=KaZSmvxMXNTZp4oF_8pEEGnkBTIB6EcRKsask1QSS0UkMGhhM3bNljTJ8rXL3Sxd3hSYJOv2mqURIsgh8KD61dTZQV8Qjp0DS4IxWYhaLcIDOKOS3tHNnoW-5y79bsH_dxSW31_Xo3TDXk03F3X8GFYR8v5PrUR8u3Nab70qVO8Cm8XTBXk-jF5i86YiKpOtkpf-M2BjsmSEmV1RabiiYtHmWJJLB5f7yThYtnKR4RGhvyBUOF44ATZUZ_RDsScNLlFMRRCslBg8hNri4fWJQ3uQWw08ZdhDzXXhbO1Ped4CFOKxZ7YQ5mGhjhvWjH7nppcWj5Nr9DqA-i-zlOkuPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SBoxxx/21411" target="_blank">📅 00:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارشگر:
«آیا ایران در حادثه پایگاه هوایی فرفورد دخالت داشت؟»
ترامپ:
«به نظر می‌رسد که بله.»</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21410" target="_blank">📅 00:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادعای وزیر خزانه‌داری آمریکا:
جمهوری اسلامی در یکماه گذشته حتی یک قطره نفت هم نفروخته است!</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21409" target="_blank">📅 23:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هدف قرار گرفتن شرکت آرامکو در شهر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21408" target="_blank">📅 23:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مقام ایرانی:
ادعاهای بلومبرگ در مورد پیشنهاد هسته‌ای ارائه شده توسط ایران به طرف آمریکایی در جریان گفتگوها با میانجی‌گران نادرست است</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21407" target="_blank">📅 23:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سوپرنفتکش ۲.۵ میلیون بشکه‌ای در تنگه هرمز هدف قرار گرفت</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21406" target="_blank">📅 23:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
معاون وزیر ارتباطات
:
اگر استفاده از استارلینک گسترده شود ، در مواقع بحران مجبوریم تمام برق را قطع کنیم تا مودم های استارلینک هم از کار بیفتد؛ چراکه حکمرانی اینترنت را نخواهیم داشت</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21405" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مقامات ایالات متحده به الجزیره:  ناو هواپیمابر یو‌اس‌اس تئودور روزولت به همراه گروه ضربتی خود، پایگاه سن دیگو را ترک کرده و به سمت خاورمیانه در حرکت است.  تا پایان نوامبر، ۳ ناو هواپیمابر و ۲ گروه ویژه حملات آبی-خاکی در اطراف ایران مستقر خواهند شد.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21404" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:  به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/21403" target="_blank">📅 18:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21402">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ:
به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21402" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21401">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21401" target="_blank">📅 17:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21400">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تا نزدیکی محدوده دوم ورود آمد.  پوزیشن اول را اینجا با حدود ۲۰۰ پیپ سود تسویه کنید</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21400" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21399">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#FairValueCurve  نمایه FVC تغییر خاصی نسبت به دیروز نداشته.  محدوده های مناسب خرید:  4165 4148  تارگت ها:  4187 4213</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21399" target="_blank">📅 15:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21398">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyAIOQdQ3mj697q_dMu7XD7LNs46Fjgrmk676FXkAHP60n_JugGVdOM6im6H9b2PMMlvpzqur5HFy0tWs0_2ClfHPYMFNhKOM7aeo2E4TSCGpCxqRonwiIWbXpRfSZ73fHDlUC7tUUc-2bh7YX9EKouOvrNOpN0PBxPhFKfBazs9Dhd-xSGtqUUJIBUafIpVxH2j_w8BMaTAWUG-fPV5igzCtkNFM0hveYgoCPqwQt1KbhTYpOkEDQlnATjsDKacsG3R1PwzaZRHeFt7PV6nu14xG7twRy2nO8QjrV4ktCqfvI81u5bvwU21xSgleTCDMYdCkEhxNdGx6gnODmn13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیآمدهای نظامی امپراتوری ایلان ماسک</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21398" target="_blank">📅 14:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21397">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز:
مقامات دولت سوریه و نمایندگان حزب‌الله در سپتامبر به‌صورت مخفیانه در ترکیه دیدار کردند که نخستین گفت‌وگوی حضوری شناخته‌شده میان این دو طرف پس از سقوط بشار اسد محسوب می‌شود.
این مذاکرات که با تسهیل‌گری نهادهای امنیتی و اطلاعاتی ترکیه انجام شد، بر کاهش تنش‌ها میان دمشق و حزب‌الله متمرکز بود.
سوریه به حزب‌الله اطمینان داد که برای تسلیح‌زدایی از این گروه، مداخله نظامی در لبنان نخواهد داشت، در حالی‌که از حزب‌الله خواست قاچاق سلاح از مرزها را متوقف کند و سلول‌های باقی‌مانده خود را در سوریه منحل سازد.
حزب‌الله تعهد کرد که در امور سوریه دخالت نکند، اما پاسخی مستقیم به این درخواست‌ها ارائه نداد. هیچ توافق نهایی‌ای حاصل نشد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21397" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21396">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IMG_9826.PNG</div>
  <div class="tg-doc-extra">4.7 MB</div>
</div>
<a href="https://t.me/SBoxxx/21396" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali_SharifAzadeh – Podcast</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21396" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21395">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Podcast</div>
  <div class="tg-doc-extra">Ali_SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21395" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_445
🗓
October 1, 2026
✔️
تحلیل گزارش دیروز شاخص خرجکرد شخصی مصرف کننده
✔️
ارزیابی وضعیت تنشهای مربوط به ایران
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21395" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21394">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">درگیری مسلحانه نیروهای انتظامی با شبه نظامیان مسلح ناشناس که از صبح امروز در زاهدان شروع شده طبق اخبار تاکنون ادامه دارد</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21394" target="_blank">📅 10:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21393">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21393" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21392">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPcCP8zEhXb2_6Yd1aIue49xxUqnl0wga-_-2WEhZhFNjiQX6Ne2h2Y1kNL3AP2-o0QRSo4f5rZ-VONh3WOnyVU5gwhqDEwQx3YglMUogNPGbmsXpeq61_XQXAEQ2stYh5b8PQPoRb9NFhgV1yT1CqtRgnRRBJCYLQx1MM2fEg1kaDAFyr6LITzQv0v0UvLUTnM_i1Faxi0NTlwvFywhiJZEX6_4t-lvvkmEiMOqj-V0KtWcRMl4rqSEVGYo2hBBcsTOdwWuqlfm8krR6yqRTcwmy2N9BnAwAw8c_iwZoI6_DyOg_PBzs0KD3hzDEwjLp7sGB09hqTfn8Crdqio_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC تغییر خاصی نسبت به دیروز نداشته.
محدوده های مناسب خرید:
4165
4148
تارگت ها:
4187
4213</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21392" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21391">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY6IJu10fOyLPb8kfwiywalOEyPk55rAclWtLeLLs3PuddJZxAMVZSFeTYG3GZE88wSSfL6UFYQcUthm_beEcOmKpONaOlXzL6QoihH0p8VdFlf9nqUaoaMkevc7zdMHCzrwrNZjVnsODlgvvwWZeb7_QF7n1rIa7XUvG3t6P2cAGI7OFBLlQ8nia_Xc_GAtpK7tRbzFmYv_GDSOjN7ySHL_TX9eV63khXUM6iGeTGHokBJwazZTAQtunYB6UImIkfA0QbwXFRJHojcRCCcf1IzIahab6NunbANcCnkYf4KYjMa9CijXN8Nd6h826JDx56e8uMR9mWvSjF8_fTy3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در اصلاحی ها توصیه می شود.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21391" target="_blank">📅 10:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21390">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اکسیوس:     روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21390" target="_blank">📅 10:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21389">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اکسیوس:
روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21389" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21388">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ادعای عجیب هگست وزیر دفاع آمریکا:
امروز دستور دادم ساختار عقیدتی سیاسی در ارتش آمریکا تشکیل شود!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21388" target="_blank">📅 09:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21387">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfZ7hM58GXTEK1oCkhi9CzVQn4QAPyfal41m9pVv7CCPSWibaMid0DXyh6Z1JZzeCCRFT57X2PCGV322LbKgr7-CMj_5owRlHk8yu1wykSKKJrsYLkP9V4GLugtA3oMnZ5AR0XTVCIECRaKosBuvC1G5E_1jOpbESKfxXZgc9tQ50YqFxj-suUn0e9Z9t9DC3xIkyMuo9QNav8MCs8Xu6np8FneAljCnal9sykWfwE4g7soAX2ld06yrGnghgGOcuxT5P9P5tlASgSjibX0lFk4d8S-ERMimdGtIPUjsFLgZMWmOFT73UZY9Au9jEmmFy6AEBNYVHMCLhdr89j2WyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تحلیلی بر گزارش PCE دیروز
گزارش PCE در ظاهر Dovish بود؛ Core PCE به ۳٪ رسید و احتمال افزایش نرخ بهره کاهش یافت، اما تورم خدماتی همچنان چسبنده است.
مصرف قوی و پایداری Supercore نشان می‌دهد فدرال رزرو هنوز نمی‌تواند با اطمینان از موضع انقباضی فاصله بگیرد؛ بنابراین پیام PCE برای طلا کوتاه‌مدت Dovish است.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21387" target="_blank">📅 09:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21386">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ درباره ایران:
به‌زودی شاهد اتفاقاتی خواهید بود.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21386" target="_blank">📅 21:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21385">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMywUutkk8XiWlDRscZIB5SyXzFwY4tK64zIVPPPndkDbuV43C3020YMVZ1qtNhFfrhISMT8nPCHdD0MJNun4_kp9ArxtFJrLM9fa69SZRGf6ZuQ5xEY8XvbUSqM0sMmwC1FxVXqT8Yzlr3Q8PpcJ8NpsOkqDN741IVX0wBQYof-lThxlfwvu3Zjq73diY02O5zUmgqpU8TwTghM9z7a5GwkEgFZ2kn5Ype-W2fIMoopV53sP5Z_0E8yY1NspvXDJJAEWoubs4HTvggzHAaEwfIJokp3h3ou8rlwqPpIByhMfYjdCqPuBgs8uk362NN1OhrUeRCltZ9QvTVDkbigvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به توپوگرافی یمن دقت کنید!
آن مناطق کوهستانی در غرب این کشور، عمدتا دست حوثی ها است و از علل شکست سعودی ها و متحدینشان در ۱۰ سال کذشته بوده است</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21385" target="_blank">📅 21:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21384" target="_blank">📅 20:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
دبیرکل ناتو: اروپا باید به ایران حمله می‌کرد
دبیرکل ناتو بار دیگر از حمله نظامی علیه ایران حمایت کرد و گفت که به جای آمریکا، اروپا باید چنین حملاتی را انجام می‌داد.
روته در گفت‌وگو با یورونیوز مدعی شد: «صریح بگویم، اروپا ظرفیت آن را نداشت که توانایی هسته‌ای ایران را از بین ببرد. ما نمی‌توانستیم، ظرفیت آن را نداشتیم. در ۱۰  سال می‌توانیم و باید این کار را انجام دهیم.»
دبیرکل ناتو ادعا کرد: «این کار را نباید آمریکایی‌ها انجام دهند. ما باید آن را انجام دهیم. همچنین باید ما باشیم که به وضعیت حوثی‌ها (انصارالله) در دریای سرخ رسیدگی کنیم، نه آمریکایی‌ها.»
‎</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/21383" target="_blank">📅 20:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka3E5TlrdQVnmvwG4QL0K0aVST5malQ4pPg_RLN-ZvjN92ZlwXZTTtqiLtJ5eXQrXTxAKBPInfFlU8jSOqGzMvIfuaLlatObB0tBFgoB5Z3l8494sNV4N2EuSoTNT5XOjNMPziIzvousnBaT_P5k67mAqPaKjWoZ2dMMREAZ7R9w8M4QKMdVHdae1u4y2CrrZeXGxsOUN68z4dLDpvndMn26CFX5TjX5GHslL93ZQXidvPdja-0S5zicH5WDVbDUI2Ie72f82X_GL5Utu5yUrLHUcuj9fJSXrnVEm2X1sI0bVgouZ_UI1WZOrjbIHmmGhPC4G-ks7edfSUXzekbMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21382" target="_blank">📅 19:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21381" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21380">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:  فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.  بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21380" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21379">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21379" target="_blank">📅 19:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21378">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حالا آنهایی که دلار را ریال کرده و در بورس بردند برای برگشت به دلار باید تا آخر پاییز صبر کنند!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21378" target="_blank">📅 19:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21377">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نامه بانک مرکزی به تمام صرافی های دیجیتال :   هر کاربر فقط روزانه اجازه خرید ۲۰۰۰ تتر را دارد</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21377" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21376" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی خطاب به امارات:
میزبانی از قصاب غزه پیامد‌های مثبتی ندارد/ از جنگ اخیر درس بگیرید و از آغاز جنگ دست بردارید</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21375" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">— لحظاتی پیش پرتاب یک موشک بالستیک ضدکشتی از فارس، ایران انجام شد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21374" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21373">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21373" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21372">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به همراهان ما روی ۴۱۸۷ سیگنال سل داده شد و اکنون نزدیک حد سود نهایی در ۴۱۴۸ هستیم</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21372" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21371">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شکست جعلی که در سقف کانال روی داده، اتفاقاً فروشندگان قدرتمندتری را تحریک به ورود کرده است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21371" target="_blank">📅 18:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwzwfjdHL0ar-cP0BVEkJa2AYFaCLOLC0P_eDh6F_7r6mFd-gORQCwAqCT-xgUKxgStOvkqLp9aIMUvWUoAanCY5KBHT_4vaTEJPKc9dGh-8FB6qq14bUeoVBGmA7cwPYXnf_4rQbp3_KMyfOeCOFpwqxPDwVlZSktUXu1XhqQB8k8SlpT3wvIlJueBDPGQ26vg146OMBp6bChmST7Y4j-Dmk7D9QYeOtGV2_xT5eEHfQwgeTIMLuGi6MGRLorb9R1HZC4_iQ1VzQKmzN-RYUVo8uHqijJgHcrm4D0v6S7yoRhsefay3TpPpH97FyNzoR3Q2eeN0-iK7tAH7Ip1PZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21370" target="_blank">📅 18:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyLWw2ac8ijoX60lJD90JWjCC_HkJzTFjRy44L43ZWaJiv5XLzlODHH2J80uV-ZAAaF08t23crl35Fnc8YKghx7EV8TvjpzvXCa9I1uSJZmuUh1B2XnJ3vi5nIXzEWi8juMBqLvaPym4gCV8WQrzns3uauontdWsa4XeWMXWI3cWYYdV1eKPq2dwzlsO6opc_U21mFO2yxtOUD8wZPJd3efzgK3vUhGHmqXHoRJFV9Ybc3Heu98OJpTkKFo4P7ZBxHuptErMVnc0t1TuVo0NcojYwUsEE0mq2DXZl5f4kItXLwy3NDNHoq1oSC0qSSozHo6TL5u3mIUdOV2CdnaeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول سناریوهای قیمتی</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21369" target="_blank">📅 18:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21367">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sunrun_RUN_Democratic_Congress_Scenario_2026_Revised.pdf</div>
  <div class="tg-doc-extra">84.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/21367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21367" target="_blank">📅 18:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21366">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21366" target="_blank">📅 18:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21365">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=kvaNFvziALax-f945z-DfotOYymUNKjRCJJhkAWGhZychaEWtl31IhanhRe-GZBJi51HswSTj5QjyMQbVQo75AYiso1rqwWoz4dalpyGSu_gsqq1XODU0NiKEFJARQOEUpc7I0Fp3UqqVXQQ9c6hdqhN9t9dhMDELSPSxQRyne6q5N_NSdNTYRnQS-mhuHZSaIectKPp1lL0wx7uURPSsURURJlhULHqu3SzFyMfJaTwgjI3FRXb0yQFavMDBairUI6z4j8uy1R9M5Rp2OihKBH__jDCr4Qwqrv8vDrYf4aYoUyzr76DTsiELg0001Z_2M_ZNQqEk4Zza8w_sdpzMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=kvaNFvziALax-f945z-DfotOYymUNKjRCJJhkAWGhZychaEWtl31IhanhRe-GZBJi51HswSTj5QjyMQbVQo75AYiso1rqwWoz4dalpyGSu_gsqq1XODU0NiKEFJARQOEUpc7I0Fp3UqqVXQQ9c6hdqhN9t9dhMDELSPSxQRyne6q5N_NSdNTYRnQS-mhuHZSaIectKPp1lL0wx7uURPSsURURJlhULHqu3SzFyMfJaTwgjI3FRXb0yQFavMDBairUI6z4j8uy1R9M5Rp2OihKBH__jDCr4Qwqrv8vDrYf4aYoUyzr76DTsiELg0001Z_2M_ZNQqEk4Zza8w_sdpzMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی    این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21365" target="_blank">📅 18:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21364">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این چه پاییزی است که هنوز پایانش نرسیده!  نکبت ها تخمهای خودمان هم جوجه شد از بس که در بحران زیستیم!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21364" target="_blank">📅 17:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21363">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:   جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21363" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:
جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21362" target="_blank">📅 17:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21361" target="_blank">📅 17:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhkwYeFcTwQKd519y7Lm2-jD26u3XDW6q9epQqWR-mOgSWTWGBIqRo_MHI6h0c2zg0LujyVP1cGYpV9pX-6FedYTvUSklQJkRSPvJgYNZtOZzycrUnwlTvTwVLLZ7M7J3cq411WLJXud_h98ttPfdImMhlcGXF7y5tidGhssO4XGZu1_-TKG7LuIkGhjIcd3DDTi6TmX5j-W0yuCeoBOqQKpj64qnyUlD0b5ZgnceucBLPQSsjdkbpjoUpvRbH4YDQfpQQrqmv6nT9h9xqreIC6mjJoIPjYMoQqVZRR4v0KzfASc7hSmeNhgykqxB8lrym80VacSnS7nyVBiwc-DRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21360" target="_blank">📅 14:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فلایت‌رادار از تغییر مسیر یک پرواز دیگر شرکت «فلای‌دبی» به مقصد اسرائیل خبر می‌دهد
بر اساس این گزارش، هواپیما در حال بازگشت به دبی است</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21359" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در فاصله میان حباب منفی تا ارزش منصفانه قرار دارد  در این شرایط، فروش در مقاومت توصیه می شود:  یک مقاومت همین محدوده 4197 الی 4203 است  بعدی 4257 است (احتمالاً نرسد)  تارگت ها:  4182 4148 4124</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21358" target="_blank">📅 14:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فردا ساعت ۱۳:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد  لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21357" target="_blank">📅 13:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21356" target="_blank">📅 12:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21355">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارواح عمه تان آخر هواپیمای در حال پرواز هم جای دعواست؟!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21355" target="_blank">📅 12:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21354">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY5N6efI8_u-8wMbYr8y6aBLEIiRksASaHu4c0y6tpuaAwycEmvhzOayguaSlr6Lnxzsg7niYfs_FeesM58JD17zzWU8twmOnOVDpeQd4Gst93f6zwvRrAqr_dJm4hO-lBtAb0FxLCQccWn8lNH9Zke94KgDcQeraJAnnK9D2OxlE9dgCvGzLIoeEbezbgM04EgflW7bwaVNWiDlcV5OhDVz4DyWuhxUB8cc8xPihtE7xg_IE_PUBLCXX9TAC96fAYzxj59uZ-yWR5g3oDobVB6yoj6-c9E7mVaod6-zYPax6-Dh0e_BrEA0KBe4axvpB0y895FgJegZsIyrQnaSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در فاصله میان حباب منفی تا ارزش منصفانه قرار دارد
در این شرایط، فروش در مقاومت توصیه می شود:
یک مقاومت همین محدوده 4197 الی 4203 است
بعدی 4257 است (احتمالاً نرسد)
تارگت ها:
4182
4148
4124</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21354" target="_blank">📅 12:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21353">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqtJ0j-Ws8PAioL5cW7ypkfew3w8TCro2jt5NqY4gGbhQrNDQxY-H3gA-zTreVBZ83VMueETyoTa_e65Es2yU-ekL1hEOT8saygZQmiVRNTS13ditxAGRTuOdpg0dvBoYY7V28ywdznon5StXLRs9-G7N6jDJq1lQ7LMm-o2fB3wUxqNLFByHEXdmxSl__xgGZgVFEGT2CoDek9LN-3vqImAI_ZKpbnwJIEqUTVxlaGjTIUa0qjXi2xLQLRUPoi4rFmJUjobx7Z3SdoYH4RJ-o0cGvxDdNmbVQklpPOu4ZlSg8Gi7O9EgMqteN0bwtxnnHFuqttXBX10vjljt_tMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21353" target="_blank">📅 12:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21352">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f193b66f88.mp4?token=ALeNu8azB-Yas0OtJPtScyZm0sxrfmQl-1dAVmFZYnHn4fA97gvf4FeKv-ERai8Xz2jRnR2nW2FmdJSM3v8DXqaQcZSJ-muFMfYgRkzIu630LXHxnktIsvsSUFEf-t6Ddh-pD9s3HOB-rzRjXegj_ZEnmiCBRl18n_yu4x8x-d7BlLfxBBQQjeka5r5nOYNjeX_mjSMqceW3lVyCEgH_g2NGuQO-T6KlIqNszTBa2Glvoi0IJZFVpEmqoEJUWoenK24x7BULRAT1nQX3OCVtIGmDog_8GY28aERRHqFXxil08nDQt3wTfDmcyLdrUvBxukdldTfQpS9wtlkSc-bf6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f193b66f88.mp4?token=ALeNu8azB-Yas0OtJPtScyZm0sxrfmQl-1dAVmFZYnHn4fA97gvf4FeKv-ERai8Xz2jRnR2nW2FmdJSM3v8DXqaQcZSJ-muFMfYgRkzIu630LXHxnktIsvsSUFEf-t6Ddh-pD9s3HOB-rzRjXegj_ZEnmiCBRl18n_yu4x8x-d7BlLfxBBQQjeka5r5nOYNjeX_mjSMqceW3lVyCEgH_g2NGuQO-T6KlIqNszTBa2Glvoi0IJZFVpEmqoEJUWoenK24x7BULRAT1nQX3OCVtIGmDog_8GY28aERRHqFXxil08nDQt3wTfDmcyLdrUvBxukdldTfQpS9wtlkSc-bf6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین خبری بود که در ۹۳ سال گذشته از سمنان منتشر شد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21352" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21351">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بانک مرکزی گفته از امروز به هر  کارت ملی ۱۰ هزار دلار تعلق می گیرد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21351" target="_blank">📅 10:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21350">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IMG_9815.PNG</div>
  <div class="tg-doc-extra">4.8 MB</div>
</div>
<a href="https://t.me/SBoxxx/21350" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali_SharifAzadeh – Podcast</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21350" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21349">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Podcast</div>
  <div class="tg-doc-extra">Ali_SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_444
🗓
September 30, 2026
✔️
دو گزارش نسبتا ضعیف اما کم اهمیت از اقتصاد آمریکا
✔️
تحلیل مواضع اعضای فدرال رزرو
✔️
دلایل عدم ثبت سقف جدید برای نفت
✔️
بررسی تقویم اقتصادی ‌روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21349" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21348">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مادر… ها!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/21348" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21347">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">— واردات خودروهای لوکس خارجی را آزاد می‌کنند — دلار برای تقاضای وارداتی رشد می‌کند — خودشان در قیمت ۲۶۰ تومان دلار را به ملت می اندازند — با پولش سهام ویران خودگوه و صایپا میخرند — مجوز را لغو می‌کنند  — سهام خودروسازها صف خرید می شود</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21347" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21346">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">— واردات خودروهای لوکس خارجی را آزاد می‌کنند
— دلار برای تقاضای وارداتی رشد می‌کند
— خودشان در قیمت ۲۶۰ تومان دلار را به ملت می اندازند
— با پولش سهام ویران خودگوه و صایپا میخرند
— مجوز را لغو می‌کنند
— سهام خودروسازها صف خرید می شود</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21346" target="_blank">📅 10:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21345">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رسانه‌های اسراییلی ادعا کردند علت درخواست کمک، دعوا بین مسافران بوده</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21345" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21344">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مقامات اسراییلی منتظر نظر کارشناسی کاپیتان شهبازی هستند</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21344" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21343">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کاپیتان شهبازی:
با ۲۵ سال سابقه میگویم؛ علت این حادثه این بود که سوخت هواپیما گران شده و تصمیم گرفته شد در مقصد نزدیک تر فرود صورت بگیرد تا در مصرف سوخت صرفه جویی بشود</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21343" target="_blank">📅 10:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21342">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مقامات اسراییلی منتظر نظر کارشناسی کاپیتان شهبازی هستند</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21342" target="_blank">📅 10:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21341">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Middle East Core</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21341" target="_blank">📅 10:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21340">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هواپیمای «فلای دبی» که از دبی به مقصد اسرائیل در حرکت بود، در فرودگاه تبوک عربستان سعودی به زمین نشست.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21340" target="_blank">📅 10:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21339">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هواپیماربایی در مسیر امارات—اسراییل!</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21339" target="_blank">📅 10:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21338">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هواپیماربایی در مسیر امارات—اسراییل!</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21338" target="_blank">📅 10:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21337">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آکسیوس به نقل از یک منبع آگاه:
هیچ پیشرفت ملموسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها خواستار مواردی هستند که واشنگتن نمی‌تواند آن‌ها را بپذیرد.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21337" target="_blank">📅 02:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21336">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بوئینگ مسابقه F/A-XX نیروی دریایی ایالات متحده را برنده شد و با شکست دادن نورثروپ گرومن، قراردادی با ارزش بیش از ۲۰ میلیارد دلار برای توسعه جنگنده نسل بعدی ناوهای هواپیمابر نیروی دریایی را به دست آورد.
پیش‌بینی می‌شود که این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین F/A-18E/F سوپر هورنت و EA-18G گراولر شود.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21336" target="_blank">📅 01:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21335">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فردا ساعت ۱۳:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد
لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21335" target="_blank">📅 01:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21334">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تتر = ۲۵۷ هزار تومان!</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21334" target="_blank">📅 00:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21333">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روس‌ها همیشه موقع مذاکره ایران با آمریکا کرم میریزند</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21333" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21332">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">برخی منابع روسی از احتمال قریب الوقوع جنگ با اسراییل خبر می دهند</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21332" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21331">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برخی منابع روسی از احتمال قریب الوقوع جنگ با اسراییل خبر می دهند</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21331" target="_blank">📅 23:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTWuX7btO8w9Ic6SJoi7dAddXYSzgTuNBmVouV03_KhyAQBqvSl6RMqwxIQu1ulD8egJ6KF-h0KFxjdrU47kQ6RLnNhDPQ0wEBB-o72oYzX9a4624RYAUWLiR8eWYDwk_WRq2od9q9DAz_TuOH-qIrZRCMNjdgGdCKcMIwWlbuuJFIt5DKG4H1go_X0eWysMcf4lVBLpvrG6ljwRiwv19XnZ_JEmvmRex6gW15O-Al9JCnaB97_6--w-fkqa7bUGiVXLZuhO81vPL4G18WNA7Y-30tn2Xo17OgVwjF7y6p8lO28_OyO_gOO-gx20LXFjsapZpVYTAECfvr_M1kImeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SBoxxx/21330" target="_blank">📅 22:29 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
