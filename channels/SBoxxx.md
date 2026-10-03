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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-21437">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">1-USA 2-PRC 3-N/A 4-IRI</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/21437" target="_blank">📅 19:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21436">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">1-USA
2-PRC
3-N/A
4-IRI</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/21436" target="_blank">📅 19:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21435">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهوری آذربایجان  : «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/21435" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21434">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهوری آذربایجان
: «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/21434" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21433">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ادعای بِسنت درباره ایران:
برای اولین بار در تاریخ، از زمانی که شروع به استخراج نفت کردند، این هفته هیچ نفت روی آب نخواهند داشت. آنها هیچ درآمدی نخواهند داشت.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/21433" target="_blank">📅 18:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21432">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حملات سنگین حوثی ها به تاسیسات نفتی آرامکو در عربستان</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21432" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21431">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">— پلیس بریتانیا دو شهروند ایرانی به نام‌های رحمان صالحی، ۳۵ ساله، و سلام احمدیان، ۳۶ ساله را دستگیر کرده است که متهم به توطئه برای هدف قرار دادن جامعه یهودی در منطقه منچستر پیش از یوم کیپور هستند.
این دو نفر به «آماده‌سازی برای ارتکاب عمل تروریستی یا کمک به دیگری در ارتکاب عمل تروریستی» در منچستر، در تاریخ ۲۰ سپتامبر یا قبل از آن، متهم شده‌اند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21431" target="_blank">📅 08:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21430">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC3i5pST81T0Bs3LYz5JPjnxK_bbp0YrxTQmMKXtXMtAvWV3ydqTlrFNb4inuTqx3geC_jli4fVUt42AzN_MWmfJx5i5KzKE0FEt3U5NW41nLBOcNZOD1dVp4BjH9-W3GYnCUKz7lPcThGMwfWKMyut7pqEvBkGuCwzAuSnxffD9LXXglYECypUXPbl5X2S0q-UNvpZPGnlcUwlMjCVuuUm1A6hlZFHxd9Na0YNkPUo5u_eDRjPfggaxD_StpSyFTGIyr-1rBjtrRPtPZH3gMAuCEFfaZoneUPHiiTyJiewAf9eykuah1HhNbwYd6WxQpCLU0qaKY-vFu1N6lnaXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21430" target="_blank">📅 02:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21429">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ادعای جدید ترامپ:  یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود  به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.  ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21429" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21428">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ادعای جدید ترامپ:
یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود
به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.
ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد و این "کارخانه‌های مواد مخدر و هسته‌ای" به‌شدت هدف قرار گرفتند.
بر اساس گزارش رسانه‌های آمریکا این نخستین بار است که ترامپ به طور مستقیم از "کارخانه‌های مواد مخدر" در ایران به‌عنوان یکی از اهداف حملات هوایی آمریکا نام می‌برد.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21428" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21427">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">«چرا جنگ می شود و چگونه؟!»</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نشست لایو لغو شد.  در یک پادکست مفصل، خواهم کوشید اوضاع را از دید خودم بررسی کنم.</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SBoxxx/21427" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21424">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حمله با سلاح سرد به یک روحانی در رشت؛ ضارب متواری است</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SBoxxx/21424" target="_blank">📅 16:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21423">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21423" target="_blank">📅 15:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21422">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21422" target="_blank">📅 15:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21421">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=g4Nc6vcgPQ3AYF-ugE6slskcbpF8ulAvrd6zfQJbt_4WQMIoNty2q_YGAkGnjFTeI6Se0cvvt1Ixq1VO4Ni5yx4suI6n2k8gZ5U4VwNeja3CXI3HmPfdoMPqWUi3TxjcdFK5hNEQUDU0RBVi_f8a0-1q_e5l-dSzXTxkktoDZstN1tMYKp7c0zx7hnlcgfe5pSOaz3kRZrfUHRIw3HxZngR7t1XO5fXGcBJ1I91a8X4_iN7K2Ewhlw-okmJHMy_bNIvxQUa1VNvgAs7gnggzNOkajhvuz7VWo1KbfCwoM-3H0tplcsdvX7i6vjRCPMZRTZ_ZG3UQ2Zp7s25t6aMagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=g4Nc6vcgPQ3AYF-ugE6slskcbpF8ulAvrd6zfQJbt_4WQMIoNty2q_YGAkGnjFTeI6Se0cvvt1Ixq1VO4Ni5yx4suI6n2k8gZ5U4VwNeja3CXI3HmPfdoMPqWUi3TxjcdFK5hNEQUDU0RBVi_f8a0-1q_e5l-dSzXTxkktoDZstN1tMYKp7c0zx7hnlcgfe5pSOaz3kRZrfUHRIw3HxZngR7t1XO5fXGcBJ1I91a8X4_iN7K2Ewhlw-okmJHMy_bNIvxQUa1VNvgAs7gnggzNOkajhvuz7VWo1KbfCwoM-3H0tplcsdvX7i6vjRCPMZRTZ_ZG3UQ2Zp7s25t6aMagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21421" target="_blank">📅 15:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21420">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21420" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21419">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">واشنگتن پست:
وزارت جنگ آمریکا برای اعزام 20 هزار نیروی نظامی دیگر ارتش آمریکا به خاورمیانه آماده می‌شود.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21419" target="_blank">📅 13:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21418">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صداوسیما:
درگیری مسلحانه سپاه با تروریست‌ها در راسک
برخی منابع از درگیری مسلحانه میان نیروهای امنیتی و عناصر گروهک تروریستی در یکی از روستاهای شهرستان راسک در جنوب سیستان‌ و بلوچستان خبر دادند.
نیروهای امنیتی در حال پاکسازی منطقه و بررسی اوضاع هستند.
تاکنون جزئیات بیشتری درباره وضعیت عناصر تروریستی منتشر نشده است.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21418" target="_blank">📅 12:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21417">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFgRsgY37SrdABBx9JzkKd-OHmmG-mSlqLI8jKyXWnKXGH87VsC7khf3yNYHrMSgxguXXNwpzsJJM23zc52HkusUJFExoNN6YKKNNpqj4PTfZZY2CPFD2R_R0ESZMbN8D6jSnRhg2raxozXzEXHpk2BbYlfxhe8XYSdZ1Vh4R5YfLqY8UZ52ZgBoZ3aiTe2XNCnS0bXYw0qwaLn2h4DazUpvQvu4OLyZ4aeLyDCvrbP--UxuyTmOdb92Dn_kIboHp7klwlEj6okMBVVRXr7rUa9xQFPoAsuEWKR0gK0OUtNufCWbc0F-utahTQhSDn9ES-95jDuLnjkuB63ZbhnDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21417" target="_blank">📅 11:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21416">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGlNcaCp_kNyMH0aumecEDsJZVjUuADIv8yx0Sp-D14XOt3VX3kyqJHRueImEJwzZf1DU3y_sBeynl68eoNHDZjwkh8GpO29TDM_W0eXDRH9LTCqRQzRJZt2Q9Qd9enwFa6QEMbyeHG1a8M-6vKQIsemQCkwaQFvkOig4iyHzBgXt7L-Y_keLCnAlccZh83epOCNJQesrr9Rbrk-_cWyMCPC7EBrzNuk_wXvZaOIqbLMsAPQXQyg9NLE3AB6gWGtz7i3Ogj-TLbhqg9lGb9N1pYWJuxT1n8Ips0kWEPTZzn-Ti40Qcx4iCz9dbVwur4DLl5CwvVoapT_4ubczNjzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC هم تغییر خاصی نسبت به پریروز و دیروز نداشته است چون عملاً قیمت همانجایی است که دیروز بوده</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21416" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21415">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhopTHNDoXQ97FlGchd2XWBGB8S-okZpy8GMfWUavJwsRxxBgQ8V6EdQbLmtZj8gXqkT_eYDniiaTb2xguGoaLC0iTenNbtN5wQwc9rqWMSeC_HyOxTOSEg_i-gGHIrZ1l2P-1mdGO8p3yXyhoKspj7xStdZx6tNdnvCvhuxZ85DODxj1kgAQSdMybu7XGyDf6O9NxyLyAi_fDPWyOSzEMbpsc6OqtNrjiNgQo1AEcQP_IAG5WAviB2uJG-vGl0grGL89dxlL6-cs1KaqZkZE05HtOeOcrzSfAqrNS0A8XOwniwwYhmGhyj_-EpRUmc2_oHrFRNMSmfCUirPJRF5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسط به بالا قرار دارد.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21415" target="_blank">📅 11:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21414">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اگر دوباره به پایین برگشت، تنها روی محدوده دوم ۴۱۴۸ ورود مجاز است.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21414" target="_blank">📅 09:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/21413" target="_blank">📅 00:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21412" target="_blank">📅 00:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51530cf576.mp4?token=oOwOV_NtOlNnuoem57P0wQhFFIyZuMaVgHhriLMpiQ7r7pW4MtU96qJtIW2zQ-teZJaE_hJDwhaBE1PyLE9tQhqD456UYQyGEwx1oxQeDmkY1644CgAheG-1Kmp6iF58XKaZHcjj41w58Oh8tDfelisxlzVOhtrGgq3rAsK-j1Km9qtGGfBrujAZOFwgA97ZZDB9g4E0fabUU_be28OA5EavfGDVLhJsZfy3OfSLcGkh1zNahmoEOALLlYIR7yQWp2XxA0eA8Z_szjw6vULnuYOAMuRXAraujTlRm2CyJLvGMWpW030F6e0JFKre99ifpx0QVWNL-s0KmoD8LbugkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51530cf576.mp4?token=oOwOV_NtOlNnuoem57P0wQhFFIyZuMaVgHhriLMpiQ7r7pW4MtU96qJtIW2zQ-teZJaE_hJDwhaBE1PyLE9tQhqD456UYQyGEwx1oxQeDmkY1644CgAheG-1Kmp6iF58XKaZHcjj41w58Oh8tDfelisxlzVOhtrGgq3rAsK-j1Km9qtGGfBrujAZOFwgA97ZZDB9g4E0fabUU_be28OA5EavfGDVLhJsZfy3OfSLcGkh1zNahmoEOALLlYIR7yQWp2XxA0eA8Z_szjw6vULnuYOAMuRXAraujTlRm2CyJLvGMWpW030F6e0JFKre99ifpx0QVWNL-s0KmoD8LbugkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SBoxxx/21411" target="_blank">📅 00:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارشگر:
«آیا ایران در حادثه پایگاه هوایی فرفورد دخالت داشت؟»
ترامپ:
«به نظر می‌رسد که بله.»</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21410" target="_blank">📅 00:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادعای وزیر خزانه‌داری آمریکا:
جمهوری اسلامی در یکماه گذشته حتی یک قطره نفت هم نفروخته است!</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21409" target="_blank">📅 23:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هدف قرار گرفتن شرکت آرامکو در شهر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21408" target="_blank">📅 23:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مقام ایرانی:
ادعاهای بلومبرگ در مورد پیشنهاد هسته‌ای ارائه شده توسط ایران به طرف آمریکایی در جریان گفتگوها با میانجی‌گران نادرست است</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21407" target="_blank">📅 23:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سوپرنفتکش ۲.۵ میلیون بشکه‌ای در تنگه هرمز هدف قرار گرفت</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21406" target="_blank">📅 23:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔹
معاون وزیر ارتباطات
:
اگر استفاده از استارلینک گسترده شود ، در مواقع بحران مجبوریم تمام برق را قطع کنیم تا مودم های استارلینک هم از کار بیفتد؛ چراکه حکمرانی اینترنت را نخواهیم داشت</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21405" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مقامات ایالات متحده به الجزیره:  ناو هواپیمابر یو‌اس‌اس تئودور روزولت به همراه گروه ضربتی خود، پایگاه سن دیگو را ترک کرده و به سمت خاورمیانه در حرکت است.  تا پایان نوامبر، ۳ ناو هواپیمابر و ۲ گروه ویژه حملات آبی-خاکی در اطراف ایران مستقر خواهند شد.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21404" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:  به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21403" target="_blank">📅 18:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21402" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21401">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21401" target="_blank">📅 17:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21400">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تا نزدیکی محدوده دوم ورود آمد.  پوزیشن اول را اینجا با حدود ۲۰۰ پیپ سود تسویه کنید</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21400" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">#FairValueCurve  نمایه FVC تغییر خاصی نسبت به دیروز نداشته.  محدوده های مناسب خرید:  4165 4148  تارگت ها:  4187 4213</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21399" target="_blank">📅 15:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks8mC2RXezVGl4myYc_jwogy_eKBFf4-pKG9008H2aVZLnnPdWkfc6alnztzhhvIRonWrClqW1ViEKSq-Z8PAoQqqg5Qm_Ot7Csx59jYRkaD1T3yWeG0JY0wj4E1btJd6JfPnFNabhIBiXxiE-oTqtfkIEU0pAif8CYCRfKWI9FYzrLnJbzIr7cvEanPn_cPomrZ-tBYTk4IWN_43XNOdyZfQfL0jWHgLWLeEpVN1hnk4RK7x91QDOKmBuZLOZBVQ6k_O7W6onI3Rya5kfxrk91qsU-clGsai2P4zDETtsAjOm0VtYU5FwOr-PJqbyMcXFtHt51H_1RKolNAEAWQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیآمدهای نظامی امپراتوری ایلان ماسک</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21398" target="_blank">📅 14:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21397">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رویترز:
مقامات دولت سوریه و نمایندگان حزب‌الله در سپتامبر به‌صورت مخفیانه در ترکیه دیدار کردند که نخستین گفت‌وگوی حضوری شناخته‌شده میان این دو طرف پس از سقوط بشار اسد محسوب می‌شود.
این مذاکرات که با تسهیل‌گری نهادهای امنیتی و اطلاعاتی ترکیه انجام شد، بر کاهش تنش‌ها میان دمشق و حزب‌الله متمرکز بود.
سوریه به حزب‌الله اطمینان داد که برای تسلیح‌زدایی از این گروه، مداخله نظامی در لبنان نخواهد داشت، در حالی‌که از حزب‌الله خواست قاچاق سلاح از مرزها را متوقف کند و سلول‌های باقی‌مانده خود را در سوریه منحل سازد.
حزب‌الله تعهد کرد که در امور سوریه دخالت نکند، اما پاسخی مستقیم به این درخواست‌ها ارائه نداد. هیچ توافق نهایی‌ای حاصل نشد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21397" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21396">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21396" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21395">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21395" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">درگیری مسلحانه نیروهای انتظامی با شبه نظامیان مسلح ناشناس که از صبح امروز در زاهدان شروع شده طبق اخبار تاکنون ادامه دارد</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21394" target="_blank">📅 10:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21393">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21393" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21392">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qevis8fbB0DA90LWq9gIjpfZCxDXFRHh9PqmcjCcX9fLGQlBMR4PKCDXGoCcBu4TS15KKORfOZgWc6C0Db5jmTqu8p3_esmxy7-ivZhURGawWbGapnq20SxzlfsSFzP4FUVEJaFh-bHVcB7dOnewCAvgPJ99FVnnP1PdQMW8GNprkHrb0FAAFc9798UxuUUvAcgnI0eKVBvfajrJLl6csVP89qPhtC8kxFHVETgYRpLA0gU9pF_lngau_EwST66R28h2NEkjhY3awGqOs79D8YIAeMbR0FcKCgAm74TP127yoNYUNW0EospN6VF9M5-tznz9dEo9HKEmybY9NlUi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC تغییر خاصی نسبت به دیروز نداشته.
محدوده های مناسب خرید:
4165
4148
تارگت ها:
4187
4213</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21392" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8GPhdcoPGJmwEn2S1QX9Z2X7OESnRgDAa9GNQf_z_cgHIlf_0Hl1L1ahT6qLOvnLZdYfbpPPNwJgLf82C-14yTusexj_8CmKLBUETwbm5DBKY5vw4krla8SDjZoD5Pcc5hNZgWddtNCG-xONs4I7DMdk9aJfIal-4EOCIxCR6rnVWQ4DIT2VhoFvFPAZ8My9l1GzuYIp17pQ_GofLQj03x7_PVGSWr1przH9E_XzGRyhRpkWgmxw4d8ZQpYlaSEJcMV-9i9J3qkxHCsY1M06DfnWrJhUM09gCkvT27pHGMl5k-XBub5oS2Pwr3xdIOeXGHBNNl7-axgTNN9XOjLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در اصلاحی ها توصیه می شود.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21391" target="_blank">📅 10:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اکسیوس:     روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21390" target="_blank">📅 10:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اکسیوس:
روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21389" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21388">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ادعای عجیب هگست وزیر دفاع آمریکا:
امروز دستور دادم ساختار عقیدتی سیاسی در ارتش آمریکا تشکیل شود!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21388" target="_blank">📅 09:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21387">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL-JkHHPL2P9PPO8BGEf0UBgt8AYFbgDEJWJfx-5nudBdjMlnCO7SXW_jFutEpbQX_hTzb5jkC6M7JShayOegTjeqkhlP0C_JHgc9dcbT3f-3WvQSzcVHo9NTVhRbb2n73mWZZR89dlFdIuIDBjq3_olzg9R56Tb7QAOEcnHSo765UfCJzCD3p7uDPBT7WM4Xsw6SQlZLApV_t--VeFm4Rv6nYdYEPW3n9ZxcPmIjDUyFV6u21yOoSiLYyNJxKiYKcwYmaESQkUwGfpDXbPU9aKXP4MS7o_MaR29jBJfos22fV1bFiaZ1_q2PqoSOsPImLfeUkkHk1OjpACid0t7Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21387" target="_blank">📅 09:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21386">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ درباره ایران:
به‌زودی شاهد اتفاقاتی خواهید بود.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21386" target="_blank">📅 21:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21385">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcg80zF3Zzwe2JPan_teIU5obq-nDeC58scLkEzRzYM-t4PRJxZv3hBa9DeG0w-RIpXqGtsGtkEM0GyeEWHNlsnWEgrCFwG4SUf-v9-PZ4OPH_eco13KPFrKIBFE69vgt73P6ohaiEul5qLIlPIRMPYd6NDXjXpSNky-fzKS0-6j_2p0HkXX_EkvrIsnKdSKQz844fY5L5jbuwgB1nnAbRXz5u7txaIN7iAuHgBrBZ-UbWv-UouDKji-6Cpeu-_oQURwJxJQW_C4dzvgChLRAk3tpkr-UoBmN3JnQkw-nCoZXMxqIYZWrcQiF5P7hxZhYutBLRX-E7DKYrB2_rYWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به توپوگرافی یمن دقت کنید!
آن مناطق کوهستانی در غرب این کشور، عمدتا دست حوثی ها است و از علل شکست سعودی ها و متحدینشان در ۱۰ سال کذشته بوده است</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21385" target="_blank">📅 21:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21384">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21384" target="_blank">📅 20:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21383">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
دبیرکل ناتو: اروپا باید به ایران حمله می‌کرد
دبیرکل ناتو بار دیگر از حمله نظامی علیه ایران حمایت کرد و گفت که به جای آمریکا، اروپا باید چنین حملاتی را انجام می‌داد.
روته در گفت‌وگو با یورونیوز مدعی شد: «صریح بگویم، اروپا ظرفیت آن را نداشت که توانایی هسته‌ای ایران را از بین ببرد. ما نمی‌توانستیم، ظرفیت آن را نداشتیم. در ۱۰  سال می‌توانیم و باید این کار را انجام دهیم.»
دبیرکل ناتو ادعا کرد: «این کار را نباید آمریکایی‌ها انجام دهند. ما باید آن را انجام دهیم. همچنین باید ما باشیم که به وضعیت حوثی‌ها (انصارالله) در دریای سرخ رسیدگی کنیم، نه آمریکایی‌ها.»
‎</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/21383" target="_blank">📅 20:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21382">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EanEDztnnLxFj9z5TwHaO3LoC7G0FBsJX72TR8dFpr_Xob53_QMkJDDE2a3AxqyPJyy22-iZsXLs-W66C7LviAluilRKEK6tfAbJ4HiV4kGxXaV7g5eqtWkAczGZuCz11goLfASGknrVu66JRUU5dQm6LNcWODGHzKCETNpR48rIzhq2BT1BUCInju86QtyqrAHkYuDSI_ijsvliaZ9wlJ8S-6p8CzKbg8-AMsByVlticoq2KdVcUWYHhxlTqeYRPaRV5AMS6PzyXpw7LG46kSTxw-nveXErpJJCEgMvCDxbHALddDoJFG0FlA8CWInb_5Gg6TELOJPgFHmrOeGwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21382" target="_blank">📅 19:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21381">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21381" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21380">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:  فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.  بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21380" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21379">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21379" target="_blank">📅 19:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21378">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حالا آنهایی که دلار را ریال کرده و در بورس بردند برای برگشت به دلار باید تا آخر پاییز صبر کنند!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21378" target="_blank">📅 19:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نامه بانک مرکزی به تمام صرافی های دیجیتال :   هر کاربر فقط روزانه اجازه خرید ۲۰۰۰ تتر را دارد</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21377" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21376">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21376" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی خطاب به امارات:
میزبانی از قصاب غزه پیامد‌های مثبتی ندارد/ از جنگ اخیر درس بگیرید و از آغاز جنگ دست بردارید</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21375" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">— لحظاتی پیش پرتاب یک موشک بالستیک ضدکشتی از فارس، ایران انجام شد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21374" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21373" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به همراهان ما روی ۴۱۸۷ سیگنال سل داده شد و اکنون نزدیک حد سود نهایی در ۴۱۴۸ هستیم</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21372" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21371">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شکست جعلی که در سقف کانال روی داده، اتفاقاً فروشندگان قدرتمندتری را تحریک به ورود کرده است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21371" target="_blank">📅 18:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4JuenB34rCB0JUmUfPGlUDxKjh4pqC74-Y9Xsy_Aj6VoCz4bzTDUPOwe7WJiuwxOguQOchgpaTOr8v10A4R6tK-vxZExeQ5Znv7iQ217jcR0rmoQiNbPEHrgFBJDyODm8aUKdiGsEzG5KMa5FxuE5hPIEc-p8ZPyEHYjGaLrRmpmCspQS54UjtTV3CvFLae8qSzA5-xOTnZPqkRS-_8cIDsARX6ka3nA0FGN9mmXjQWnf0T0n8Nu6YXlfSZlc1XRZ2yF1qVBYZRrDrpN516g3pmKGAUKMBSo5y2JH73oSEL43Jqf0kSpRS0u2ukhycwrqByVzz-0bz2FpbQ_RwhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21370" target="_blank">📅 18:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21369">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vifi1PE27ug1l4RDmqj1hUKl8WpcAqOsDARYZZhFLSMtCiaZ68tEdZs43MOSVNtWJ9ytUaYz4jILqoKnsXQcm0PhQlRmuV61Q9tM9Mtfx3Md6I2zdiLNqhFfopW5knzSGnCvQo1bff8A0I5iMR-KiW2BJFFOirqzohU9jEhq8Y1cCyP1_xgnrxxduDh4c5kNNUqy9VTj_RW7D9KVJ46UWj1e3yuAo5A9t4v_NjmXynsHMEg8ccllBZOQBy-QK3JNAAKIPqZDhDJeCxrWvPUSBH-_asAj7CoZIm2gYJZNJGmciQIjOEHECv3-9ThiwmqBqyhPt01zyhUW17GedBTIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول سناریوهای قیمتی</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21369" target="_blank">📅 18:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21367">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sunrun_RUN_Democratic_Congress_Scenario_2026_Revised.pdf</div>
  <div class="tg-doc-extra">84.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/21367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21367" target="_blank">📅 18:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21366">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21366" target="_blank">📅 18:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21365">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=ZafcZDZt_vdZT9-1OYJv_Xwuy1oJQ7MDji220XQYeOWGbXbZjnFxSmLuj7SiCdAX2WlFyMkswRjMN432BK1vWEiF8F2yhy1Yn8oqb8WZfzy3o5Q8Maio96tg1a4bCCg8wmSgkaAmvUxymLGAbMsVt7lXvR2vVli3lNo6WSE6ItYmFVqXr3PWb8T8uV_mZtbzQvvzKbjVhhj9IoZmM2zpVLPwz-2wAPyeZxW3XSczKTs13_Lsac8mFFtOv_QA5gEABqVBk_kahg58kGZYOy-2Hk4-Ja3ce9NNsMYYqNf3j-i7Df6snO5C_gFje8muwVtCwimALE4_uCLq0UQs7Ezldw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=ZafcZDZt_vdZT9-1OYJv_Xwuy1oJQ7MDji220XQYeOWGbXbZjnFxSmLuj7SiCdAX2WlFyMkswRjMN432BK1vWEiF8F2yhy1Yn8oqb8WZfzy3o5Q8Maio96tg1a4bCCg8wmSgkaAmvUxymLGAbMsVt7lXvR2vVli3lNo6WSE6ItYmFVqXr3PWb8T8uV_mZtbzQvvzKbjVhhj9IoZmM2zpVLPwz-2wAPyeZxW3XSczKTs13_Lsac8mFFtOv_QA5gEABqVBk_kahg58kGZYOy-2Hk4-Ja3ce9NNsMYYqNf3j-i7Df6snO5C_gFje8muwVtCwimALE4_uCLq0UQs7Ezldw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی    این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21365" target="_blank">📅 18:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21364">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این چه پاییزی است که هنوز پایانش نرسیده!  نکبت ها تخمهای خودمان هم جوجه شد از بس که در بحران زیستیم!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21364" target="_blank">📅 17:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21363">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:   جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21363" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21362">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:
جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21362" target="_blank">📅 17:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21361">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21361" target="_blank">📅 17:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21360">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgxNoKKAd56-uoYzabIQfcqYRTudvMo4-wHLJSs0us3R9ykW0cx8PQspASFKif9p91Zj0J2Ofy39wxtQM8oJZpkFMGi7WEwOJ2X-roK1TlICPxTyaj5xiVcqdHLtrHldgOBo37JdR763UzL1D-iotbDveJsLThLuwAezZXPkmIfcFKzNXdp3ESi9UhxByJ1xAKW-qtuquktn_fTMFz2O2hKkUGs3YeceAPLuZs_1nRL2VaNyH_DYtU6u0wfcHQCbd5wdKbQwyMDfwSht7ToaUeLpq8lEJr-HtrlSNZj3KmQgO_30rf_OW0c6sNBKB3KO4lGElhZYGkEwEWkNAjytJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21360" target="_blank">📅 14:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21359">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فلایت‌رادار از تغییر مسیر یک پرواز دیگر شرکت «فلای‌دبی» به مقصد اسرائیل خبر می‌دهد
بر اساس این گزارش، هواپیما در حال بازگشت به دبی است</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21359" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21358">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در فاصله میان حباب منفی تا ارزش منصفانه قرار دارد  در این شرایط، فروش در مقاومت توصیه می شود:  یک مقاومت همین محدوده 4197 الی 4203 است  بعدی 4257 است (احتمالاً نرسد)  تارگت ها:  4182 4148 4124</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21358" target="_blank">📅 14:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21357">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فردا ساعت ۱۳:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد  لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21357" target="_blank">📅 13:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21356">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21356" target="_blank">📅 12:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21355">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارواح عمه تان آخر هواپیمای در حال پرواز هم جای دعواست؟!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21355" target="_blank">📅 12:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21354">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RETnYg0Hie_Hw4K3MCap_IHuQHceVUmyUpXQnIXVft9QOnD1aqFCesgYcTgCuZkW334RP46hlrx4OUJmGkOqkx0bNJSg7bb2WEump9_UcGoaHP4z1UJ2vD7G2oWQofSYprQDhOE3gJ7vubcrPFn_rLMR6poiNMV6gdZclACa2mxvjIZkunkY7QOtmP7KXENsWo8E1gRp8QRB5WQh5-Abu7DJ8yO0oEckR5OVaGSwgfEoTPfk6eBFLLkR2iI-ZSzpNT7ojmKeh1XIw_sAgl4ktjvObexMNII80N_WU8VXNHCFnVmbtclPoacpKHWUarBFUUidwk978QFNSiq14Y4n9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در فاصله میان حباب منفی تا ارزش منصفانه قرار دارد
در این شرایط، فروش در مقاومت توصیه می شود:
یک مقاومت همین محدوده 4197 الی 4203 است
بعدی 4257 است (احتمالاً نرسد)
تارگت ها:
4182
4148
4124</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21354" target="_blank">📅 12:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mR2lg6qNwrVn2J_LE2Cqs-tG1YAB0qOLOaDo217y2-VjQiwuKBY0M73GdsSeEXK5hLJsnSHci1b3cyNW6fszqhszX3B-NGXw8__DAiTmLXiPusUb8pFXYO2gw2O2QarKlYDW1VRsWfUhFnEM8nNfVmuGauA3gG6yXwIBX34XTGoiV6jRUF6xnNVbqSq984IrOtDk-DqAdRH2-BANsN9DQe70s0dUWGoIyZCUo65rlE5j-4VVrrTwFbqpUUFiGnyQVjHuZ4apf7VbI7ouqJVdvYsEjB93gBNSuyRvOJj64iH5H5Ieo95njSPprKz44WHozgUwDZE9OPl3AHdP3S2yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21353" target="_blank">📅 12:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f193b66f88.mp4?token=PBpNvrtF8Sigab72NQyan6AuV8TXuVV2PivRTrdJtPbhLsT3VSPrGfaOqLgqBE9CVYYBJMFo3iAdY-4KV3JpJ8h-OjpJ9S4NTcSl8HmD4uEeSVs23m1o03zfy4dzJg-V8FvW1XDDrNSoTkKtlY72oXmq3W_TKdXocNjug4etn2M0b11SyZDJHv6l93Y31O1_5FTPVEvzLb6azY658eubY_j-UBelV-_B5hnd76jza0wvCIT3HhxE0qpaOlbl_4wlUQjkHNgrB_3zq9LdQELPbI3RV56CXmuklkBis_o4hY_mCZ3T5-rq3GDgDYJU2_TIxJKUVhOlFV6s91fwVpT96g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f193b66f88.mp4?token=PBpNvrtF8Sigab72NQyan6AuV8TXuVV2PivRTrdJtPbhLsT3VSPrGfaOqLgqBE9CVYYBJMFo3iAdY-4KV3JpJ8h-OjpJ9S4NTcSl8HmD4uEeSVs23m1o03zfy4dzJg-V8FvW1XDDrNSoTkKtlY72oXmq3W_TKdXocNjug4etn2M0b11SyZDJHv6l93Y31O1_5FTPVEvzLb6azY658eubY_j-UBelV-_B5hnd76jza0wvCIT3HhxE0qpaOlbl_4wlUQjkHNgrB_3zq9LdQELPbI3RV56CXmuklkBis_o4hY_mCZ3T5-rq3GDgDYJU2_TIxJKUVhOlFV6s91fwVpT96g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین خبری بود که در ۹۳ سال گذشته از سمنان منتشر شد.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21352" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بانک مرکزی گفته از امروز به هر  کارت ملی ۱۰ هزار دلار تعلق می گیرد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21351" target="_blank">📅 10:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21350">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21350" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21349">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21349" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مادر… ها!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21348" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">— واردات خودروهای لوکس خارجی را آزاد می‌کنند — دلار برای تقاضای وارداتی رشد می‌کند — خودشان در قیمت ۲۶۰ تومان دلار را به ملت می اندازند — با پولش سهام ویران خودگوه و صایپا میخرند — مجوز را لغو می‌کنند  — سهام خودروسازها صف خرید می شود</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21347" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">— واردات خودروهای لوکس خارجی را آزاد می‌کنند
— دلار برای تقاضای وارداتی رشد می‌کند
— خودشان در قیمت ۲۶۰ تومان دلار را به ملت می اندازند
— با پولش سهام ویران خودگوه و صایپا میخرند
— مجوز را لغو می‌کنند
— سهام خودروسازها صف خرید می شود</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21346" target="_blank">📅 10:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه‌های اسراییلی ادعا کردند علت درخواست کمک، دعوا بین مسافران بوده</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21345" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مقامات اسراییلی منتظر نظر کارشناسی کاپیتان شهبازی هستند</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21344" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کاپیتان شهبازی:
با ۲۵ سال سابقه میگویم؛ علت این حادثه این بود که سوخت هواپیما گران شده و تصمیم گرفته شد در مقصد نزدیک تر فرود صورت بگیرد تا در مصرف سوخت صرفه جویی بشود</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21343" target="_blank">📅 10:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مقامات اسراییلی منتظر نظر کارشناسی کاپیتان شهبازی هستند</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21342" target="_blank">📅 10:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Middle East Core</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21341" target="_blank">📅 10:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هواپیمای «فلای دبی» که از دبی به مقصد اسرائیل در حرکت بود، در فرودگاه تبوک عربستان سعودی به زمین نشست.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21340" target="_blank">📅 10:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هواپیماربایی در مسیر امارات—اسراییل!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21339" target="_blank">📅 10:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هواپیماربایی در مسیر امارات—اسراییل!</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21338" target="_blank">📅 10:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21337">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آکسیوس به نقل از یک منبع آگاه:
هیچ پیشرفت ملموسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها خواستار مواردی هستند که واشنگتن نمی‌تواند آن‌ها را بپذیرد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21337" target="_blank">📅 02:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21336">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بوئینگ مسابقه F/A-XX نیروی دریایی ایالات متحده را برنده شد و با شکست دادن نورثروپ گرومن، قراردادی با ارزش بیش از ۲۰ میلیارد دلار برای توسعه جنگنده نسل بعدی ناوهای هواپیمابر نیروی دریایی را به دست آورد.
پیش‌بینی می‌شود که این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین F/A-18E/F سوپر هورنت و EA-18G گراولر شود.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21336" target="_blank">📅 01:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21335">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فردا ساعت ۱۳:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد
لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21335" target="_blank">📅 01:31 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
