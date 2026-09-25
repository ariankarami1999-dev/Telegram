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
<img src="https://cdn4.telesco.pe/file/ixCl_7hTwlV-GdJeN2zUWdxaHdnA9WeV_9_KlDpPCwBlEW-TrUh61Iu2p18HP83kaL_wrPp95HsTLIml63xGg5fbGvWc9Glvx113zT4voOkr-KX0Y2A69VIuuvgEsC6eIMTh4mzll80bV7pHsatYqG5ehHxav5sIgitZuuTtzcvE5eGnAU0YHlohFufNXxp9PY28wHOBb0vwF1a7gPY7LD73ye1hGbwIkob6uYt2dSfew1Qb4nJfFkZheBtqFSjvPCm7hlkQHj_jElyfhEVli7BjopthXgQ-zstfV-a0cjPtWR066aSUJgxOf4-8RH1nXgOGzJapB5Mi4Xlqc24IrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 03:12:51</div>
<hr>

<div class="tg-post" id="msg-72289">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/news_hut/72289" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72288">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-9MH0AtzBdScDv-jn_UQm9QGyhNIuXQ2gMYIYd9KgdhRjFQ1e3EOlRdKSU3Sm3grD3nqoXN1aIrrKzcuJZCVQZUCpGQYvT8vXpGkBP4-mdURauSVgDGuYxXEpWVph2JCXZ1apkbirk7B-Qle6EuIw-Hpfr6uyIrGNVwppxo-bODMgT4oCr3P6i4T9fCo5T8aH8_1QGNc1kQcn29hN5rVELcRZMpKGLgwO_GxtRMxz87O1wrA7C5W_jwDVg5sBkGa_aELgElpCsvDvQdU0W5lN43QabhSbk8HIPIt_1Qb7q8603SaoZjATYB7dy4aRXvaD7GeJl0I3clGMVaoT9JDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/news_hut/72288" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72287">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Peu0lwctsQotAiI9QSZSpSns6HdTr1VFuaYDUNeiO1U7QcKX327jmmNdr4Y7ynJKGFoYpJZgiP2GMySFWM5DHEURL_U8P68Z1BS3x8dxkO1Yfyj494E3pjMfgRIlrkKxAC76Rl45BwT-FqlUAgtymEurJ8Gz3Jalbp3rRbuhoQFk0cBaj6oBAptUFOumngcHwHF0goBTpa80tvbuUyStR27LBuptuU5KVemmKteLPezsjxEi-b_AlCbpJ7w_69vzFrfkgY4Bmgn-06oap-U1M1KifITiZvnpDZVo7ZTi7dlg77zhEv1mi1SHI7NUGJtMbVN9y72slWQqMf9ftMUwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه توی ریاضیات و بخش توابع مشکل داشتین؛
این عکس به بهترین شکل تابع f(f(x)) رو نشون میده.
@News_Hut</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/news_hut/72287" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72286">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:   طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه. در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه. توپ در زمین آمریکاست.  @News_Hut</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/news_hut/72286" target="_blank">📅 00:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72285">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=nxrdOz2uppmfe9Ewm-P-jgRG2zcqUxuzf3yMAh0wxhoggz4FyjrHaH-APkdywRSf3XlVLSk8tuycxXTcaJiHrKWKm-lFLDKB-fvj5KXI4HC8Xri1b0u-SLyjlkQZ2Nxo_L87N6qSGMT5_BJSa_D1EMu7RBSv0cKmQCwB7S3-9ANIVHbFhB7ggNf9DDdqS-Qx6gRz88yD311kdW8MyWDmRGaCSAo4TCm9BKtt4P-y7j9HIVHg3KduKTCitz0d9mEP-M6JBnM57yeZ5bwmxLohilGUa3h4CcDAPV4MCv6YQ2qFOcEin7SMBeq5QyI_q0FO35MIuU5YP1mzalf4zFaxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=nxrdOz2uppmfe9Ewm-P-jgRG2zcqUxuzf3yMAh0wxhoggz4FyjrHaH-APkdywRSf3XlVLSk8tuycxXTcaJiHrKWKm-lFLDKB-fvj5KXI4HC8Xri1b0u-SLyjlkQZ2Nxo_L87N6qSGMT5_BJSa_D1EMu7RBSv0cKmQCwB7S3-9ANIVHbFhB7ggNf9DDdqS-Qx6gRz88yD311kdW8MyWDmRGaCSAo4TCm9BKtt4P-y7j9HIVHg3KduKTCitz0d9mEP-M6JBnM57yeZ5bwmxLohilGUa3h4CcDAPV4MCv6YQ2qFOcEin7SMBeq5QyI_q0FO35MIuU5YP1mzalf4zFaxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:
طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه.
در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه.
توپ در زمین آمریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/news_hut/72285" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72284">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=Suyg3Vj8un1TdN5nNyAwzHFy6lu4R8osdv2kVFfpIuGguGokskOsyhBswbF37CSRRulxsf6O9PAfYNNWPr2Ov1OyB4-lBLjYjLQzeAUi4SwhMGEBct-ov_xzGFoBb0Oc7z83qSTDoz6t-T3DhBnFxYw0DqBCYekVYwIfUq3ge2ALna-EOwsy4c_DQKSKKYgLcT8d3HCHVOfqv1tcG33pHEjLPKd53RNz6hMgVhhmnZm3GyoAU8V016yyJcqw1cTYHsUsdPhj1REPBk6UIaGknyAzKPC_mYGhwgsLI1AMjr_lGkZAuhEYmOZn67eoIKXTC9T9c84K9jjIDjamKvIDaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=Suyg3Vj8un1TdN5nNyAwzHFy6lu4R8osdv2kVFfpIuGguGokskOsyhBswbF37CSRRulxsf6O9PAfYNNWPr2Ov1OyB4-lBLjYjLQzeAUi4SwhMGEBct-ov_xzGFoBb0Oc7z83qSTDoz6t-T3DhBnFxYw0DqBCYekVYwIfUq3ge2ALna-EOwsy4c_DQKSKKYgLcT8d3HCHVOfqv1tcG33pHEjLPKd53RNz6hMgVhhmnZm3GyoAU8V016yyJcqw1cTYHsUsdPhj1REPBk6UIaGknyAzKPC_mYGhwgsLI1AMjr_lGkZAuhEYmOZn67eoIKXTC9T9c84K9jjIDjamKvIDaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن جدید «بی-۲۱ رایدر» (B-21 Raider) ایالات متحده، پرواز آزمایشی خود را بر فراز کالیفرنیا انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72284" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72283">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری فارس به نقل از یک منبع آگاه ایرانی، گزارش‌های «اکسیوس» و «الجزیره» درباره دور جدید مذاکرات ایران و آمریکا را تکذیب کرد و مدعی شد که هدف اصلی این گزارش‌ها، تأثیرگذاری بر قیمت نفت و ایجاد ثبات در بازارهاست.
این منبع همچنین ادعای الجزیره مبنی بر اعزام کارشناسان فنی ایران به نیویورک برای شرکت در مذاکرات را رد و این گزارش‌ها را نادرست توصیف کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72283" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72282">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eda15604.mp4?token=iWQd06fs_xGfFEwv46rd4sXpPQmI78TMSGEvzpCedcn69b77q51TebedHx-BhzzoD_PV2Anu4x01R7_fmBc29YYH80cfWcSkQvk9_3g4AsCbI3jAviv9ViV_lrgpbvvJUnpNzDPGNx0v7DKnPaZJDdTl4V9HEPaCa5rL9JPirffcte8aNzhHyMsdVi8kLhSQORe5JD--W18HxEQ5Bu-lQ7iVkHf-zGeAav6VkLQiVIOQ8a2T_6MTARfYDYRjv1EMzvb0fM5oj3i2mvnLNmk00qRr98IPnNXSlU-ChOVEzM2dmGkNd3frFD7HP0b4OM52FAhuIDe7wTOXEVic7rnYBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eda15604.mp4?token=iWQd06fs_xGfFEwv46rd4sXpPQmI78TMSGEvzpCedcn69b77q51TebedHx-BhzzoD_PV2Anu4x01R7_fmBc29YYH80cfWcSkQvk9_3g4AsCbI3jAviv9ViV_lrgpbvvJUnpNzDPGNx0v7DKnPaZJDdTl4V9HEPaCa5rL9JPirffcte8aNzhHyMsdVi8kLhSQORe5JD--W18HxEQ5Bu-lQ7iVkHf-zGeAav6VkLQiVIOQ8a2T_6MTARfYDYRjv1EMzvb0fM5oj3i2mvnLNmk00qRr98IPnNXSlU-ChOVEzM2dmGkNd3frFD7HP0b4OM52FAhuIDe7wTOXEVic7rnYBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال باشه چرا به یه جمع دخترونه میگن خانوادگی ولی به یه جمع پسرونه میگن مجردی:
دیروز ، رامسر به سمت جواهرده
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72282" target="_blank">📅 22:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72281">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=k2Fxw3p8BSe16t4wFwZLWygrPLB23EI0H4MNC1clxYRrfnrs00LSkFrCyPkLJ-6fgImgoszl8wL090lhSMSBGc9sBbn3cnaBuLD2gEhR_f56-4Wb0OmvjfR2gHboSDMp2MYnzyLWGQAdUNnEvp6a4sKh8zq2WGKwlpvsCI7Jwa0Nqdu78ml6wGNC1OHGbSeBocyePSJLbXD_uBrvnrlOUgVGAkFMLxHlZTNcG690x4f8fPf6ekBpn48ylom3HUPXVMLH2rR3cxzXbqP6QxFZDYADn_W3XArMQpZAGiBhFnf0pc_bvr7nD9YAXIAzuI6dqxk-gp3au4TZWRKr0Ds5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=k2Fxw3p8BSe16t4wFwZLWygrPLB23EI0H4MNC1clxYRrfnrs00LSkFrCyPkLJ-6fgImgoszl8wL090lhSMSBGc9sBbn3cnaBuLD2gEhR_f56-4Wb0OmvjfR2gHboSDMp2MYnzyLWGQAdUNnEvp6a4sKh8zq2WGKwlpvsCI7Jwa0Nqdu78ml6wGNC1OHGbSeBocyePSJLbXD_uBrvnrlOUgVGAkFMLxHlZTNcG690x4f8fPf6ekBpn48ylom3HUPXVMLH2rR3cxzXbqP6QxFZDYADn_W3XArMQpZAGiBhFnf0pc_bvr7nD9YAXIAzuI6dqxk-gp3au4TZWRKr0Ds5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه در حال اتخاذ تدابیری برای محافظت از پالایشگاه‌های نفت در برابر پهپادهای اوکراینی است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72281" target="_blank">📅 21:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72280">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:
ایران حتی در صورت پذیرش پیشنهاد تهران برای بازگشایی تنگه هرمز از سوی آمریکا، هیچ‌گونه امتیازی در حوزه هسته‌ای نخواهد داد.
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72280" target="_blank">📅 20:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=n-hP-pTSXZS0KmjgfJDAhjFkMEa8aBOyISM-PxVe-72yOW7sJXt7FtevctddQTbKog2Q-RLZu0dkSho5sI9LG0SgMEKpSNAsJtKg1W-2V975SeigLI65zxSQEPwYUbrzg11N5fL2BeXDQ8sfsgo_vjDcfr0S-fR2my1dWHg9FKxbPni96sqCVA3P9VkYz24mElRero58A93FJvqWvT9FR1MzT4ridC2sOOtbbK2Mhvt2j_vyJYeFDgQ_UovCcQ5V3DY0KyJ2HQiaZrRMOKhcD7kUMRRxNorRecaEVspGinwOQIiMk4dPhKOR0np2Y2kuLfTjDYwcfHuMxVrv8xRVoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=n-hP-pTSXZS0KmjgfJDAhjFkMEa8aBOyISM-PxVe-72yOW7sJXt7FtevctddQTbKog2Q-RLZu0dkSho5sI9LG0SgMEKpSNAsJtKg1W-2V975SeigLI65zxSQEPwYUbrzg11N5fL2BeXDQ8sfsgo_vjDcfr0S-fR2my1dWHg9FKxbPni96sqCVA3P9VkYz24mElRero58A93FJvqWvT9FR1MzT4ridC2sOOtbbK2Mhvt2j_vyJYeFDgQ_UovCcQ5V3DY0KyJ2HQiaZrRMOKhcD7kUMRRxNorRecaEVspGinwOQIiMk4dPhKOR0np2Y2kuLfTjDYwcfHuMxVrv8xRVoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی نتانیاهو یه شوخی برا میلی رئیس جمهور آرژانتین کرد و اونم یهو زد زیر خنده
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72279" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=KKJAMZnHHWWUU4jvYUNrbFpYlKMNicBTh4G8AD7K9eatQlRZDzqRiEOhSxSi_EDZS-78MrVsztggf8pkxR-iM1vxDZyaZp6ZmFuzMFd6DqfL7Mesz3rYOQqW6dHk0QGoIuSjqcERH2ZGYDbNVST9dnCwcfy6EWggYdNYpjPuhR9bp0xD5kHFj7YORmK3PazsvBR5rDT-GfBLekskKdgbFCdsoAttYMIPhpSmL0oQ0YyLm_xFjGNGXYcGqcTRBbkQDNwRKPnks3lA63nGdglbLJutDVLIbK611_7yCl9Oh7YTI60n9K4Y3D6-mhuCw3xTFR_xxYRFZQo8LaWGBdHFBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=KKJAMZnHHWWUU4jvYUNrbFpYlKMNicBTh4G8AD7K9eatQlRZDzqRiEOhSxSi_EDZS-78MrVsztggf8pkxR-iM1vxDZyaZp6ZmFuzMFd6DqfL7Mesz3rYOQqW6dHk0QGoIuSjqcERH2ZGYDbNVST9dnCwcfy6EWggYdNYpjPuhR9bp0xD5kHFj7YORmK3PazsvBR5rDT-GfBLekskKdgbFCdsoAttYMIPhpSmL0oQ0YyLm_xFjGNGXYcGqcTRBbkQDNwRKPnks3lA63nGdglbLJutDVLIbK611_7yCl9Oh7YTI60n9K4Y3D6-mhuCw3xTFR_xxYRFZQo8LaWGBdHFBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای ۲۴ و ۲۵ سپتامبر (دیروز و امروز)، افزایش فعالیت‌های ترابری ایالات متحده در ارتباط با خاورمیانه مشاهده شد که شامل هواپیماهای ترابری و پشتیبانی آمریکا—مانند مدل‌های C-17، C-5M، C-130 و KC-135می‌شد...
تدارکاتی در جریان است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72278" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=CR5jOmyiLlZ518y6qce0cojp2nxnQnNFIUXmsm3AqpLohfQ6buOm_RPg9EQd7xtKwx06oP2CJMAEMuYgzBddeBwKw1OsKk_y1XNnPwEK9EEVTpNm9cbD6yFJDnxjW5y0tW3Wlfe_NG79DoDSl0ubVKnQP9e3CiVxLbLqvdZnwy_Xlb46CiHxoAl-PUA_iK2ImQ7Trr9qy_AYvDFbb5SJxp7tbcTId2v0ZJY0grPz0Sh0k6YZNxyUNc70xt6AHpAZMXElT_RwWwTAmCvz9JMJlHuR14XPbEYRvZQnUQwlSDJUyMjgOoI-YcO0yKSqBkbcbg3YAJP28lTaOre6d2OBaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=CR5jOmyiLlZ518y6qce0cojp2nxnQnNFIUXmsm3AqpLohfQ6buOm_RPg9EQd7xtKwx06oP2CJMAEMuYgzBddeBwKw1OsKk_y1XNnPwEK9EEVTpNm9cbD6yFJDnxjW5y0tW3Wlfe_NG79DoDSl0ubVKnQP9e3CiVxLbLqvdZnwy_Xlb46CiHxoAl-PUA_iK2ImQ7Trr9qy_AYvDFbb5SJxp7tbcTId2v0ZJY0grPz0Sh0k6YZNxyUNc70xt6AHpAZMXElT_RwWwTAmCvz9JMJlHuR14XPbEYRvZQnUQwlSDJUyMjgOoI-YcO0yKSqBkbcbg3YAJP28lTaOre6d2OBaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شی رئیس جمهور چین میگه عکس روی دیوارو ببین؛
ما خیلی برات احترام قائلیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72277" target="_blank">📅 18:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=GB0WDZ6SS51PP8xIAoFA1MwrADOf5E5EWrXB8XX8bBy9o8TVvxkF141B3-FLBPvziAP9rVegPmDJ0aWHMZGn62s3zU4N6QrfTUaBJGPSiR_x25sAAcUWF_7Y085bGQpaUxxNkMr_rdT8r9Ie7TDAi_PpUE2E9yubh8oQTFF7VWde3d6kHYj7MbvbuLeQb-ISzGwM-js6ckBClNVqwRrpBZywp4ElM51O5D7cT5tD7LRtbi2PaLiCDUCZjiS53kZKfkGk_H4EGqNOoyniWMTOH63bxO_zHtl6vJUqJVuH-J3hQMyvdOY5wkRCH2c0HLEgl1LmHiFQE6AqIrF7fzfdjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=GB0WDZ6SS51PP8xIAoFA1MwrADOf5E5EWrXB8XX8bBy9o8TVvxkF141B3-FLBPvziAP9rVegPmDJ0aWHMZGn62s3zU4N6QrfTUaBJGPSiR_x25sAAcUWF_7Y085bGQpaUxxNkMr_rdT8r9Ie7TDAi_PpUE2E9yubh8oQTFF7VWde3d6kHYj7MbvbuLeQb-ISzGwM-js6ckBClNVqwRrpBZywp4ElM51O5D7cT5tD7LRtbi2PaLiCDUCZjiS53kZKfkGk_H4EGqNOoyniWMTOH63bxO_zHtl6vJUqJVuH-J3hQMyvdOY5wkRCH2c0HLEgl1LmHiFQE6AqIrF7fzfdjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده با این شرح:
مردی در مشهد با انداختن 100 میلیون از امام رضا شفای همسرش رو طلب کرد ولی همسرش شفا نگرفت و درگذشت و اونم برگشت تا 100 میلیون رو پس بگیره
😑
😑
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72276" target="_blank">📅 18:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72275" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzNejnkF-pFGWQZz6vcup8nrO6bov2KgLG23_fCE_ND3yEH6pDfoTJAQwPoTWI891F-hzhlXqZRa6w6BYi7KfAoBLwLG5goTGOVAPP4uu4gd-29Mn0bkDUztcje8IkjTvyz0egsMByEORD0_AgNexTcVdvINJSBNoRzyNLfBFiX6-S_ztV3-YRQSooHawhY5dyE0Z8fym3OXtlY5PnKxquHCHEOBmskgbEHwclJEHC8-5tsUp9cDhfddBi7C7RTZc-Qi_hJI6koVzheaqytjMrmSJSpWUi-KUkKOpVbg7Ml4qPWqBEvwK9vIPo4UqzAMHNu9bV5jaz0aT8IrAzJmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72274" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=VswouGp2dgT1EYXIaF-GeoO_WN-dryYPQsHkKgl7-wQPpudq3FvgPgWHClyTZggVs1lNLhQoS3kPJ_GuBT3m4akVdsdJ4wPtdHqVOL2fNsXseDl4bq7GKa4Opi52HIom-DNL4HsDoxB8mUmHEL4oTa52iNnfV-Y_0ncmPN4_QTcp0uuBe94XddGM99Cvwi9TEKlA4MXMUQef_7QMRvg1dyTnDM6aDteY8PG5_xTm4m5f2nkJhdkA8j48vPjBU3psY63eifd2KA56LxrXam60O5-K7utYF8XbRtngMaheA7VJxqgLpGWre9Xn5aPIaggRMeEqqu5gbgohvODALFWZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=VswouGp2dgT1EYXIaF-GeoO_WN-dryYPQsHkKgl7-wQPpudq3FvgPgWHClyTZggVs1lNLhQoS3kPJ_GuBT3m4akVdsdJ4wPtdHqVOL2fNsXseDl4bq7GKa4Opi52HIom-DNL4HsDoxB8mUmHEL4oTa52iNnfV-Y_0ncmPN4_QTcp0uuBe94XddGM99Cvwi9TEKlA4MXMUQef_7QMRvg1dyTnDM6aDteY8PG5_xTm4m5f2nkJhdkA8j48vPjBU3psY63eifd2KA56LxrXam60O5-K7utYF8XbRtngMaheA7VJxqgLpGWre9Xn5aPIaggRMeEqqu5gbgohvODALFWZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی گسترده در یک کشتی حامل خودرو با پرچم یونان در شمال جزیره میکونوس
این کشتی ۲۹سرنشین و نزدیک به۲۰۰دستگاه کامیون و خودرو داشت
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72273" target="_blank">📅 17:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=vSffitEXfSKrcCpSegrztS-VcWXRWGiDqmeRYkCpR9p1dA8wOGnCXqjY8WglGZbwOUjzbLrb5BFBBv2mlJzW2Ar-_TEbOGd7_AGo44yxrHuX102XMmig5iEBtyfbA3nm2ZRqQZFf0CzklLIdxdw1iqf8P6cehmfqm9KYv769jFuqd2K-IncOLoU3r4YzS6sD2wqwBM7JKdqaqEXlgqIwGv-ZSxabWYRtfBwzbcUYmEkpnG1EFbDWtjT4r3oSZN6ICjNpAqUjJJzaDN93ZwdYJ774ULEsbv2sWIHEiIM_yvEQTtBz5RhGihwoZyNphNiRGLqJfslrSVNAWmc9o1iTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=vSffitEXfSKrcCpSegrztS-VcWXRWGiDqmeRYkCpR9p1dA8wOGnCXqjY8WglGZbwOUjzbLrb5BFBBv2mlJzW2Ar-_TEbOGd7_AGo44yxrHuX102XMmig5iEBtyfbA3nm2ZRqQZFf0CzklLIdxdw1iqf8P6cehmfqm9KYv769jFuqd2K-IncOLoU3r4YzS6sD2wqwBM7JKdqaqEXlgqIwGv-ZSxabWYRtfBwzbcUYmEkpnG1EFbDWtjT4r3oSZN6ICjNpAqUjJJzaDN93ZwdYJ774ULEsbv2sWIHEiIM_yvEQTtBz5RhGihwoZyNphNiRGLqJfslrSVNAWmc9o1iTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی در سازمان ملل اسامی کشور هایی رو که حین سخنرانی بنیامین نتانیاهو سالن رو ترک کردن یادداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72272" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=ELwO2j6r9HBAhGCetSrbLowzcxj-WUUHphEZDx0et_1U9SuYIboWNN9LWVd66-KdVsNPbZZ3_wYUPvdUvTo1jzvuEWB_3-VYK4nWdbWeyFQ5OTwteB5nvcsDYz89IVNv3EQmd3wFBYJlTPlFhatWqNQLQ0rCXqZwcOT8dhGgBYvYTBWgh0U-4K0SFuodY6SJtQ5hCggp1GxD0TjBmOMWY6JQy8fWzpJm4qWWFalRAHrmc7PzRzY9PzGbk9I78gqPYvNH96SE3JV8wYmwAWqrRjvEKPGi-wi1kdYMqXgxsSPGB-2KjEpBzIhg-rOgUz85iKrJFPGggum5ysg4Owr1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=ELwO2j6r9HBAhGCetSrbLowzcxj-WUUHphEZDx0et_1U9SuYIboWNN9LWVd66-KdVsNPbZZ3_wYUPvdUvTo1jzvuEWB_3-VYK4nWdbWeyFQ5OTwteB5nvcsDYz89IVNv3EQmd3wFBYJlTPlFhatWqNQLQ0rCXqZwcOT8dhGgBYvYTBWgh0U-4K0SFuodY6SJtQ5hCggp1GxD0TjBmOMWY6JQy8fWzpJm4qWWFalRAHrmc7PzRzY9PzGbk9I78gqPYvNH96SE3JV8wYmwAWqrRjvEKPGi-wi1kdYMqXgxsSPGB-2KjEpBzIhg-rOgUz85iKrJFPGggum5ysg4Owr1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پزشک کودکان : امروز تو تهران ی دختربچه ی ۴ ساله ی بسیار زیبارو آوردن پیشمون با خون ریزی شدید واژن، معاینش کردیم و کاملا مشخص بود بهش
تجاوز
شده، از پدرش پرسیدیم میگه با واژن افتاده رو جاروبرقی درصورتی که دروغ میگفت و مادر بچه وقتی رفته بود بیرون این کودکو با پدر کودک و دوست پدرکودک تنها گذاشته بود...
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72271" target="_blank">📅 16:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6YNoaxrszibr1JU9AevuOw5Dr1q_pQLlTDY2_qXOBG1KU2arxSx1QuzKpISqZiOvtbIR40v3uYDzIhFRncI5uyjXmerKpoOxl7avcNyYMLP38z6PpQ5Wo__st-mNJNeLVrk_HL1QghygGsfjQ9uG_chB9uesp1kzcplh63Wj5_fOHqs4-8Bqhs3Z2B9HOiwUtku1l6DU0LQ4qqhoPYeZnyHjSR1q9BtGGtGK-RxUMTlFB4JyHkZRObr3KtkzJS7Iwpaq2I7ekGWh1kaG79SgO37iQpvkk6Tp4Osx3oAWCQDl-zBGu97nSLGfXMCEaxf7-PZCz44lFzdVJ31EsWheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=KeAT6xmxHd7Ao8Qq_7lqF5q1HGZ-53FMxw_h4C9yz-sDywstCb-Cp9KRzS43ekbKlXdS3yuzblBPTAB5bofvA3lc9w7KDyj3QFixI4VhsymI___JYeL3j4ypWa3nSmrPV55T74l-Nr0Zu-MxQKiE0QXbeT1mTuUkBovTagOsYVckyTQC_i0_CXL1Z5ag33O_B5QrFMYP3UMtdP5aPVo59zCVnHVdAWcxILO6D-oSk90eKuso8ykbcYesGYTNQPe1oukdk0RBSxtB-tLsYfjadoAbL8_aS4JbZyykGU-WnufM-_CDu-L5ynI9rLOlPHSNxGqDDlOpQdmZC4pDGRNW_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=KeAT6xmxHd7Ao8Qq_7lqF5q1HGZ-53FMxw_h4C9yz-sDywstCb-Cp9KRzS43ekbKlXdS3yuzblBPTAB5bofvA3lc9w7KDyj3QFixI4VhsymI___JYeL3j4ypWa3nSmrPV55T74l-Nr0Zu-MxQKiE0QXbeT1mTuUkBovTagOsYVckyTQC_i0_CXL1Z5ag33O_B5QrFMYP3UMtdP5aPVo59zCVnHVdAWcxILO6D-oSk90eKuso8ykbcYesGYTNQPe1oukdk0RBSxtB-tLsYfjadoAbL8_aS4JbZyykGU-WnufM-_CDu-L5ynI9rLOlPHSNxGqDDlOpQdmZC4pDGRNW_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای اوکراینی به چندین تأسیسات صنعتی در روسیه، از جمله پالایشگاه نفت «پرم»، کارخانه «ایسکرا» در اولیانوفسک و تأسیسات «وورونژ‌سینتزکااوچوک» در وورونژ، حمله کردند.
پالایشگاه پرم که یکی از بزرگ‌ترین پالایشگاه‌های روسیه است، در پی این حمله دچار آتش‌سوزی در واحد فرآوری «AVT-5» شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72268" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که یک موشک رهگیر به سمت یک «هدف هوایی مشکوک» که بر فراز جنوب لبنان (منطقه فعالیت نیروهای اسرائیلی) شناسایی شده بود، شلیک کرده است.
ارتش در حال بررسی این حادثه است. هیچ‌گونه آژیر هشداری در شمال اسرائیل به صدا درنیامد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72267" target="_blank">📅 15:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72266">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=dnUkFoKNLYMJ-kEZ7dcwWefejFIyRorlcE4dl9rSjQoa4X-owFFnlE4Fh0W_MauzpHKcbCutZnIRMt7PeEAQNrqTYYsT-ee5S__cROvjA1R6Z1100jgN4dWmeaZKBbQCXAg-0Q-UHEcS1yETsl1EYjbgluhDLPASc_Ke9XIm2l3yc6_1ceytpBbQLR3Phelx8ocKp-NPswGWjPkl7On516KytYaNENGPXMFC9ZTI8INCZ2feNdS7IyZd0yqebNUclDPuAlu1t2_C1SeuyOjY7YO_G4KMIOFH8aJ9K6jWMmKqraFwyZi56kTV1ZxTZudKOKeJOjv4Kbn9yEs1YweW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=dnUkFoKNLYMJ-kEZ7dcwWefejFIyRorlcE4dl9rSjQoa4X-owFFnlE4Fh0W_MauzpHKcbCutZnIRMt7PeEAQNrqTYYsT-ee5S__cROvjA1R6Z1100jgN4dWmeaZKBbQCXAg-0Q-UHEcS1yETsl1EYjbgluhDLPASc_Ke9XIm2l3yc6_1ceytpBbQLR3Phelx8ocKp-NPswGWjPkl7On516KytYaNENGPXMFC9ZTI8INCZ2feNdS7IyZd0yqebNUclDPuAlu1t2_C1SeuyOjY7YO_G4KMIOFH8aJ9K6jWMmKqraFwyZi56kTV1ZxTZudKOKeJOjv4Kbn9yEs1YweW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از پزشکیان پرسید که میخواید بمب اتم بسازید یا نه اونم میگه نهههه نههه اصلا،
بعد بهش میگه اگه بمب اتم نمیخواید چرا اورانیوم رو بردید زیر زمین ۶۰ درصد غنی کردید؟
گفت اونو که میخوایم رقیقش کنیم! یعنی غلیظ کردید که رقیق کنید؟! بمب نمیخواید بسازید؟!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72266" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROqAPsN_vPouGQyLQdRSu1P081EYtSRuULd7yd9LLWaWdoLoTUYHzcq6Xm1O0EupPzqviiKP2YhAqDbe2ZMfKRi2IjiBQ8TBp0q6sj0_8RofM_YczPhne5NR-GKXCCuMvBtlxkcl0ZYxBkqux98yc-1PfHwDpNAZXDLqsQgMBYkjGtyd5BNCwZ6g9EmjeoZq-yHTqmIcSBEIDDvNXG-A8wuAtEGG7RCo6KsaRlFhnf_lEwZ35D5IIf-kFY8MZWuBcNuHDtyyRZE1nJG-0GGR2vAmSEcSsBJ2ubIlPO7ZnV11-O8vth_pHguDd9x0c-8TyLP9lpSVmXr4-3nvrqGcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طرح جدید ۷ روزه‌ای را برای پایان دادن به جنگ پیشنهاد می‌کند؛
به نقل از نیویورک تایمز و به واسطه وزیر امور خارجه ایران:
• توقف کامل تمامی خصومت‌ها، از جمله در لبنان
• آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران توسط ایالات متحده
• لغو تحریم‌های نفتی
• پایان محاصره دریایی توسط ایالات متحده
• روز هفتم: بازگشایی تنگه هرمز
• آغاز فوری مذاکرات هسته‌ای
عباس عراقچی، وزیر امور خارجه، این چارچوب را علناً تأیید کرد اما جزئیات تمام شرایط را بیان نکرد و اظهار داشت که این طرح تا حد زیادی مشابه توافق ماه ژوئن است.
نکته مهم اینکه او نگفته است که عبور از تنگه هرمز برای همیشه رایگان خواهد بود؛ در چارچوب توافق ماه ژوئن، امکان عبور رایگان برای مدت ۶۰ روز پیش‌بینی شده بود تا در این فاصله درباره نحوه مدیریت آتی آن مذاکره شود.
ایران اعلام کرده است که آمادگی دارد این طرح را حتی پیش از موافقت واشنگتن اجرایی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72265" target="_blank">📅 14:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=lfowCFvWSfaVJsOyxu9-uz4IU8oOwrjdHNGSHawu6NBvlcpqnnR2waytU26ELVai56Buht7UUyPKY4ohPBVXPIFtfVR7Xc4O6pq346q7pxvZbwNgGHDqDMjuo68OgeG-_OKgRrnUQ1SVSdeMD7OkWbP2il5zGe-sfA0kfhB_lebcNT-aktUpshXCgKd5H77Xlnd6IlScj40eJ5XLXuPLKVpv1BJHj9Z0b4zHWRebNnww6cTdbOYh_PGtgZ3eZ21bossZd-Hylt9N3pp_nHMbvL51dxZen_dgaEZcHynvzltHMOxmvJ6A-wiXWM_vrunJFBJMT3nyPxdP3Ac2TthqeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=lfowCFvWSfaVJsOyxu9-uz4IU8oOwrjdHNGSHawu6NBvlcpqnnR2waytU26ELVai56Buht7UUyPKY4ohPBVXPIFtfVR7Xc4O6pq346q7pxvZbwNgGHDqDMjuo68OgeG-_OKgRrnUQ1SVSdeMD7OkWbP2il5zGe-sfA0kfhB_lebcNT-aktUpshXCgKd5H77Xlnd6IlScj40eJ5XLXuPLKVpv1BJHj9Z0b4zHWRebNnww6cTdbOYh_PGtgZ3eZ21bossZd-Hylt9N3pp_nHMbvL51dxZen_dgaEZcHynvzltHMOxmvJ6A-wiXWM_vrunJFBJMT3nyPxdP3Ac2TthqeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم #hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72264" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72263">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وال استریت ژورنال:کشورهای حاشیه خلیج فارس در مورد تلاش‌ها برای از سرگیری مذاکرات ایالات متحده و ایران اختلاف نظر دارند.
عربستان سعودی و امارات متحده عربی از دولت ترامپ می‌خواهند که فشار اقتصادی و تحریم‌ها علیه تهران را حفظ کند، در حالی که قطر برای مذاکره، از جمله پیشنهاد توقف هفت روزه درگیری‌ها برای بازگشایی تنگه هرمز، تلاش می‌کند.
عربستان سعودی با اشاره به حملات به کشتیرانی خلیج فارس و اقدامات حوثی‌ها در یمن، استدلال می‌کند که ایران باید قبل از هرگونه توافقی با فشار بیشتری روبرو شود.
قطر و عمان از بازگشایی مرحله‌ای تنگه هرمز و یک راه حل دیپلماتیک حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72263" target="_blank">📅 13:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P6SF-ooWJDKIy2vswV6mBVMcMuciguKrNG0wtoZjyqfYNx_IUd29xlGtepAfIj9-vpQF9qc9ZJgFFFqE5Qf8_Rqv9gQnQ5cbhMz4N_-Q5px33g45Ac9z1fINpEpYjkdtZLAl60Q95ZRnRJ9a15e9X7LGYlAUoIimlnvXRcvkON0jA7QWgr3lHRWW1q61mF1UYnbR3sH4E-mfassHybyvG5bP5HQFtqiLrEyNIJf_CvMOuK0tmaCDJcPG69jsFepaYMkYyhUtW7H9se4sQLBiqIz8TzgE1VHiTVE1h7XS1hTTRsZwaVkrBaLvSe3g0UFWZKOlkWDD3ydGsldDfxEAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZVNIs29jpewDUHb_IXa7fs_atEjJynlIfPA2tRX7mkhrp3kgiH5o_rXfDsnCg--8lifaICFth-VFZqiD5jTTzrRpSmjR2a-eSpX4dcjv9VJSb5tA7fRo4S-yAoRrT1N1yFEvPT1OHzH64uQUkytIUK1uzSoJ9V0nyGWFKwqU3sedCKKo9x4riB3wM16gTihNzRrtzEr7o1QcZBblahKKCmrl926w4v-eSnj2-dAVf7Gl01UTps6LUXuFn3Y6ePlHcvlmTmik9-l_WuWKQnvh_8DaaVp9fgP9BpaekJOAFBYu7EnWEz9tQE-ufymZM_Nz33B23sBSVZXX9cDPNXROWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gjFnm2U0jRRrJ5avULf5DZNTUktOd9JYNIMiU90j_6k1YibnpVwcArAJz7e3w55CPloIVwLCwlPzPb5SV9jXgdG6y2Sq6gXMIWvRofx-rBhW969sCdyikpUffHYOlSfJNduZgAT0mc98m-3xARaeRcRabhYvaeWpMjmGSaT60ZTdKXm6h3ksIEOydHfyxLZQETzu3rpB3_9fnLTZo8A-eECBTt7dsWpm23fSRbdeLVKFwONIJTAQwga3s5LkiPcSO8YJ-m7YRL9Q0Q59TnEz5LDjwTGB44KMeMlxCubJgFtG9N1RPOKOyjkU9UE4yvg5ujvqpHLnpsPzntjwTSTtoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aopbI8R00m8duGMYPFkrv8mLqo-Vq36zq7c9CmQPjZpJi8K5wIMowTAMASX70Z9X5DqAJjF6JiLlARaSQMstQVCH23G0YOhTizEVzG2iA9a0SOVp52l8K81SW2lBuYz5kqTBwu3RYqAF1sDPmdUsBA2ISOxsuQmB-oJZwKuxiw6DfMxEspIkyJV8EcDiqbE3Ok5pVxWY_OqIudLWujwmoLLimjG9IopNltwcbtGHhUSLBorAyTIGOT5T8Rdzym1eMwFIKgrXawP2gr0_DeevUNJ6WKvEXh1C7nZc3fEUL5wFILJEdPwvQCuZS9nBKKFbO5ocgZjqZVwxCPp9-JULRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگولی ترین دانش‌آموز امسال معرفی شد
این دختر کوچولو به اسم
گندم
لقب کوچولو و کیوت‌ترین دانش آموز امسال رو از طرف مردم کسب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72259" target="_blank">📅 12:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72258" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72258" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X34z499UA6W5eWICMpDLf_hvc_rp3V3v1IjciMzi0BkkJNxOcV0nTXiiYGvDzxw5HIo549qVpr5krDhrq6GeBtBVrvTZeqkf8SFEkndPRrmaCxw1PXrNx-Ic13R1o_Ciskon4hLs1iU0T2VoHRnMP7xr-IBtEbEh9eP32wEaGCiCWwnjb2FzCOpVuJC1e_HkQWe3TkhIEWvqgWw7QyrGuHCA9WRVtKuLNqg634qVWxWcS-AqPUfz3jATKRt00MKdn5o65HrhUBuNmcAgJee6PGNsI1a_WAlzSxPgPvQgTI5uly969G5ZH0qC89VvkihyCM74fbrWX6ohafpjr16sBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72257" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E98R6fisouTEtcsoMjnnPL2r5nV_2E4t3hBiSYdvVBNVmV65wJjMm42Xh67nyesE4Yml20SQ1Tv0XTP7vBq0ckfthDBISCCmI83gP7TVJ8CrhQTXHMk7rVe4vYLzbyMGzdUH0oSLGlKprxtbgn0Mp-vQlm73E-VRpM8Ed5jyGp8CdpWoq5LQhd4MRYUWzXZiFXj9JrTu4v_eqShOLyI5qJUKUgHHyFX_x8Q0Va-EhJ-4r6CwmXm2HU8levUFR_EzH31Zs9VavwDi1nzPQKml5jLUOqzEIJ3JWGCbWPo_fE0wYu8HKgslpXtuQJxF8lzCsxGXl5STxO7vIwk6dgn3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
مذاکره‌کنندگان در حال بررسی توافقی مرحله‌ای هستند که بر اساس آن، تهران در ازای کاهش محاصره اقتصادی ایران توسط واشنگتن، تنگه هرمز را بازگشایی خواهد کرد.
این مذاکرات با مانعی بزرگ روبروست، زیرا هر دو طرف خواهان حفظ اهرم فشار خود هستند: ایالات متحده کنترل فشار ناشی از تحریم‌ها را در دست دارد و ایران کنترل دسترسی به یکی از مسیرهای حیاتی انرژی جهان را.
ممکن است ایران در ازای دریافت امتیازات اقتصادی، از درخواست خود برای دریافت حق ترانزیت صرف‌نظر کند، اما همچنان خواهان حفظ کنترل اجرایی بر این تنگه است. کشورهای حوزه خلیج فارس با هرگونه ترتیبی که به ایران اجازه دهد از تنگه هرمز به عنوان اهرم فشار استفاده کند، مخالف هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72256" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSsLa7t_QloWFs09jHFhrdM1KnGCVezu-c1pPyfK2hzCrcHAq5CYh7832wYRd-V_EjXCOXQPisnUx9SMF_8jYtAdEDxwydtB8JV_M6U9R-vO6uoPB0sYPbA77T8ZMxMbVq5poCwqvzWE1UUGbBpJ60FcSgqFP8VOea3eIl44yxoQ69wzWdBKBD2Gw6NBZcxnpGKOEjZoaYU7hk_Z5WjxcVjHqPM3ocC0YkVP3sEgrJ7XvIWeLWplLcbqprjz9OMAyMju6bQxsHBdtzUvT5ABXdwvgaOjwPmTJ29K7Xl3wkzBnpLX0i1WRqHrDxPj5kdQ1kZvFWhSmH44bd4l8h5kfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=jRkefrYhomiW4bp8ofYDj2eYhuFyvapZdbI_0JwPoI8c-yhvwWHwCKhlWiM6N8Vm0Z7OBdTX4JPw9zTBsvsjfpy0Dl_i7GjzySBAGWegXQbhSpY0qfO1o2eVs3JUEzHEYMCHv4bfQJmYRk_logwFMCPkLxF-4ljXQrady2TdNqlmnH5hoqvMUOIvfAcbpQ2uwG58ymCITF2zxZYELxk4FSW8GEtU_wkzq3xdNkSNkwNeJYTSyE1t_aPrK8b2Lo8pbBqCpCf4C5-bebgNhrwcmn55rnothJXcbZPjJdNw-xjwMAOB2hvRU-4cCt02P_2QsLyK5ObbbOS1kxeDtRzmnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=jRkefrYhomiW4bp8ofYDj2eYhuFyvapZdbI_0JwPoI8c-yhvwWHwCKhlWiM6N8Vm0Z7OBdTX4JPw9zTBsvsjfpy0Dl_i7GjzySBAGWegXQbhSpY0qfO1o2eVs3JUEzHEYMCHv4bfQJmYRk_logwFMCPkLxF-4ljXQrady2TdNqlmnH5hoqvMUOIvfAcbpQ2uwG58ymCITF2zxZYELxk4FSW8GEtU_wkzq3xdNkSNkwNeJYTSyE1t_aPrK8b2Lo8pbBqCpCf4C5-bebgNhrwcmn55rnothJXcbZPjJdNw-xjwMAOB2hvRU-4cCt02P_2QsLyK5ObbbOS1kxeDtRzmnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نایا:مقام‌های فرودگاه مانع سوار شدن مسافران به پرواز شرکت هواپیمایی معراج ایران از نجف به مشهد شدند. این هواپیما بدون مسافر در حال بازگشت است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72254" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=bpyPcLj6oYBaihR0YZ2Sy4jiI14lVU7zhkKrrif9NgRkHBNapfFnmRW0tZnhhWizGYuOCxyaAnuEoU-dAKSWw2K5EpAtGIFLqQW-BbPj8iEjJOS27sZnXks5iBuA2jmTX3MxDVa7bg2UYpekFL2OELwtX2bucPmu1ryX3P1PWjyQWhlk-RhYNTYDo1eCzK1_r_uuT3Xuom-ICc5jwMqN-xa9349LoR2YMAeiVvh-OWOBaVlaFUW0J-Cp14UWXylEmptOl-xaz7bZ9ddYis8ZsWiIcXsX322Nifr9FuW-7xvPfXIQT8AeSLj_hckcUMzk-FxteQiYdDtNNBlSyq6K-rkNILD3B-fRKHr8gCkasTszDaDJaCxBcYZi88XheaOsT-57fSJHvP9sW_iaL2b6tLUgYpCBfBf2bdV_ekKs0TIN4oCVLRF1Addvy9M6c_hgMGwXPJipQeckoy3e8oRkz_GxYv1sP70h7jRIEVz5Q-KSzeOsQu4GcL1posp68t5Z9AWtNwj_m1kNgMSX1iGtq5e90cjY4dDVVsE5ZSyhwy4MgHq3502dF1mZDoGQqbOyumSk_hITz8BPwlK9Fx6tsMqMvG1xqYUgBNJ0PLhubWq-J8yGIjZXPgZyUfLSOS4FYsYEy1kiTDR6OPslYK_1deCjNmeL9424Rj9gaOaCjGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=bpyPcLj6oYBaihR0YZ2Sy4jiI14lVU7zhkKrrif9NgRkHBNapfFnmRW0tZnhhWizGYuOCxyaAnuEoU-dAKSWw2K5EpAtGIFLqQW-BbPj8iEjJOS27sZnXks5iBuA2jmTX3MxDVa7bg2UYpekFL2OELwtX2bucPmu1ryX3P1PWjyQWhlk-RhYNTYDo1eCzK1_r_uuT3Xuom-ICc5jwMqN-xa9349LoR2YMAeiVvh-OWOBaVlaFUW0J-Cp14UWXylEmptOl-xaz7bZ9ddYis8ZsWiIcXsX322Nifr9FuW-7xvPfXIQT8AeSLj_hckcUMzk-FxteQiYdDtNNBlSyq6K-rkNILD3B-fRKHr8gCkasTszDaDJaCxBcYZi88XheaOsT-57fSJHvP9sW_iaL2b6tLUgYpCBfBf2bdV_ekKs0TIN4oCVLRF1Addvy9M6c_hgMGwXPJipQeckoy3e8oRkz_GxYv1sP70h7jRIEVz5Q-KSzeOsQu4GcL1posp68t5Z9AWtNwj_m1kNgMSX1iGtq5e90cjY4dDVVsE5ZSyhwy4MgHq3502dF1mZDoGQqbOyumSk_hITz8BPwlK9Fx6tsMqMvG1xqYUgBNJ0PLhubWq-J8yGIjZXPgZyUfLSOS4FYsYEy1kiTDR6OPslYK_1deCjNmeL9424Rj9gaOaCjGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
خبرنگار:
ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
غریب آبادی:
ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
خبرنگار:
ولی با ⁦CNN⁩ رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72253" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=nK7S_HCIrIuVbOd-girvKIzKqZUt4AczvDimmNyMxvmOxQcZY3cm0Y7EQEzmx6DBWsDzXmfuqvuq184j_R68ISHaXPsgJZrgVDnfqynPfZdl2QSGpZFyPgePZ5DfLF1FbDlyfDm46IJvTDcfDCQ7Tm3deRZHXBXdJlXx6ZUUrlX7_RT42c4uxS000AKxSTt5rLFeJ46oNvjhQUfCsMnO5qKWYw5t5v6y9JjghRvEgcpH4F-hJx2CghZf0yvOECezMi_OXnznTxg7mbYHoZ8Rcl8r0uKOr-w1HlLnzAvXVGXMhLPqn2jO9LBTpSpL117wJDx4zHpFhVMQ2Q59G7Ml1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=nK7S_HCIrIuVbOd-girvKIzKqZUt4AczvDimmNyMxvmOxQcZY3cm0Y7EQEzmx6DBWsDzXmfuqvuq184j_R68ISHaXPsgJZrgVDnfqynPfZdl2QSGpZFyPgePZ5DfLF1FbDlyfDm46IJvTDcfDCQ7Tm3deRZHXBXdJlXx6ZUUrlX7_RT42c4uxS000AKxSTt5rLFeJ46oNvjhQUfCsMnO5qKWYw5t5v6y9JjghRvEgcpH4F-hJx2CghZf0yvOECezMi_OXnznTxg7mbYHoZ8Rcl8r0uKOr-w1HlLnzAvXVGXMhLPqn2jO9LBTpSpL117wJDx4zHpFhVMQ2Q59G7Ml1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس سنا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق، قطعنامه‌ای را که هدف آن محدود کردن اختیارات جنگی ترامپ در قبال ایران بود، رد کرد.
چهار جمهوری‌خواه — شامل سوزان کالینز، لیزا مورکوفسکی، رند پال و تام تیلیس — در حمایت از این قطعنامه با دموکرات‌ها همراه شدند، در حالی که جان فترمن تنها دموکراتی بود که با آن مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72252" target="_blank">📅 10:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSkTBl13ybZBPD7pvni8-6MM0WPDUcS8HvZPGwrUsT1oIXxauli7jbLCdoFMfThETu7acGoNbVJlqIJvZzkXpxbMimhkjt7OyHhyCPYK-wvKunaCn5QP7De8jAVUER2NpJ5y_7EY8YLU58_iR5JnYzCVR2v8sWJVb4z0W_9prYNto2j4-V9XF6xJFi0-0OKWwBPmY0vfriultxkbvLWwE1oThEWT3IABiiO9EJ9jT12b1LUpVcHmFcM2ILgLhn-8uG9b2x9ary6gEnDl58v524YhdAFxSOykhF0k24QaFBce-fC_nSywM3eNW0A9q03TSJQrw4xwedi23oI5y9BtOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی‌ نیوز:
مسعود پزشکیان، رئیس‌جمهور ایران، اظهار داشت که تهران خواهان احیای توافق آتش‌بس خود با ایالات متحده پیش از انتخابات میان‌دوره‌ای ماه نوامبر است.
پزشکیان گفت: «ما نمی‌خواهیم کار به انتخابات میان‌دوره‌ای بکشد. ما خواهان آن هستیم که آمریکایی‌ها پیش از انتخابات میان‌دوره‌ای به تفاهم‌نامه بازگردند.»
پزشکیان همچنین اعلام کرد که ایران برای بازرسی از تأسیسات هسته‌ای خود «آمادگی دارد» و هرگونه تلاش برای ترور ترامپ یا خانواده‌اش را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72251" target="_blank">📅 09:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72250" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=M3BzZw25-1mRr31yKRQ6-Pa5c0iHq0FidFyyoRmcQNh9T0stvES2Y65xaJwj4snCIKR3gChxJ7KT4E-bKp39RRJJVRTALCW9SF4hkUnex0F8lDJhFk649aoFbfNYDa60OGf1LlPpp1HGN2_k2zdTu2xS09YY6OINyI-WlMBEScszOGOcVJYQTS5vAW3cxYVsTGPvESjph4Yh0wXosWlCsoIyWM7gr1qgq60ya43XiWWWaYSRJen17HtGeAkUPOoY1Pww2J2De5c1cKyv5QN6lx4WDUALmAMgxdYixZT-9ilGKD8u51qWkEhzHByTiKQbgE3j17mArIEvltSbXsgq6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=M3BzZw25-1mRr31yKRQ6-Pa5c0iHq0FidFyyoRmcQNh9T0stvES2Y65xaJwj4snCIKR3gChxJ7KT4E-bKp39RRJJVRTALCW9SF4hkUnex0F8lDJhFk649aoFbfNYDa60OGf1LlPpp1HGN2_k2zdTu2xS09YY6OINyI-WlMBEScszOGOcVJYQTS5vAW3cxYVsTGPvESjph4Yh0wXosWlCsoIyWM7gr1qgq60ya43XiWWWaYSRJen17HtGeAkUPOoY1Pww2J2De5c1cKyv5QN6lx4WDUALmAMgxdYixZT-9ilGKD8u51qWkEhzHByTiKQbgE3j17mArIEvltSbXsgq6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جناب نخست وزیر پیامتون برای مردم ایران چیه؟؟
بی‌بی نتانیاهو: ما با شما هستیم نا امید نشید
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72249" target="_blank">📅 08:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">با این جوابایی که پزشکیان به خبرنگار داد باید منتظر موج جدیدی از حملات طرفداران افراطی جمهوری اسلامی و تندرو ها به پزشکیان و دارو‌دستش باشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72248" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پزشکیان:
- انصارالله مسئول اقدامات خود است و از ما دستور نمی‌گیرد.
- ما اورانیوم غنی‌شده ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) واگذار خواهیم کرد.
- ما به تمامی تعهدات خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای پایبند خواهیم بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72247" target="_blank">📅 07:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=i2O1BU5I0ghevFCrd-YQOqkObxPuFfdgjOUdZkf7bNd-pQVT_QaVQPVg3oslomV4b-_xyaDMfLzLXfTIPgS2d4UwhfGJqlzSwgXwA8zAdeCA1wM5_XHLm2DUwlA6Top5a3eU7g7Mvk3QaRpX1_VZdl_gJX4AFpyX6KLgNS11CSHhANEwaAGMXapjYQ9jcyVeMBmimdhRIr0bfIG8_5rImYm84_H9KtMJV-a10ekQwA8HYXJBQInBBRsZSg2pmRvyWnE42w9uyogxFCapjex97PDesgl4C0CdNAwV6z32qBOpWKUKJB8wYkcD7tfPMxq51aU-3w0o2kxqXmrbhdC7Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=i2O1BU5I0ghevFCrd-YQOqkObxPuFfdgjOUdZkf7bNd-pQVT_QaVQPVg3oslomV4b-_xyaDMfLzLXfTIPgS2d4UwhfGJqlzSwgXwA8zAdeCA1wM5_XHLm2DUwlA6Top5a3eU7g7Mvk3QaRpX1_VZdl_gJX4AFpyX6KLgNS11CSHhANEwaAGMXapjYQ9jcyVeMBmimdhRIr0bfIG8_5rImYm84_H9KtMJV-a10ekQwA8HYXJBQInBBRsZSg2pmRvyWnE42w9uyogxFCapjex97PDesgl4C0CdNAwV6z32qBOpWKUKJB8wYkcD7tfPMxq51aU-3w0o2kxqXmrbhdC7Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز:
آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72246" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=p48ArVrv7S2rzpLH0TL5HaBoz8H9eTAIrJGPKsHBGAdD0pjOywrYu6jtgkrrl98P6G2d3WPYMX_mostqehBkXA4xiezsWjMbS6pee1-R9czxccMNlT37zhEDnrO1uZhQK9K2o4yr00omEDKSvsGtMVDThtWD1KSNn5sL4sk32fu8cjN-4L8W1QFTVkd6Ez8Est9OtlI2-TdlCOdrTVWAaDggy0VqB3prB3xdfrcrVli057AcL8j1YUm6SuuXGjs-SlNzUoYRDUQM0FlKDEi2_VyT5Cl79kZIP-rcqBtvlbJlvFTlrXS_u7e3Vkjzbf47-EC-v8ddjoSEVXMBbkLnAon3d9Wxo8V4zDxmY1ZBHbb7EP_BaHZeQ-5akR7ZFc13YZxLoad-B615KYi9j0XiFFbrczxk-TYKVcwadF288ZcJPCj_GghgesminQRLvvVzxHiCEqvoWAPbzJtBR3r-4m1s0V0M_scYgZWK5JHhCJh6F2-nY0QIeXVS71cvHjC1fF7JnW9aIpfxp1F4mc63__vFHExMskQEg_SOygFslTMZijBej-BxFf_D10Ypee90JWCiofQ9uePAB2DJTjdEy9TXRBVgBXOLlLq-bXwvmhnmpqTkeDCo9EeXW6WlhoTdQ0klaZEN3kACkXGX5_ZPenOF8PIHuJ4RDAq0QVk0ois" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=p48ArVrv7S2rzpLH0TL5HaBoz8H9eTAIrJGPKsHBGAdD0pjOywrYu6jtgkrrl98P6G2d3WPYMX_mostqehBkXA4xiezsWjMbS6pee1-R9czxccMNlT37zhEDnrO1uZhQK9K2o4yr00omEDKSvsGtMVDThtWD1KSNn5sL4sk32fu8cjN-4L8W1QFTVkd6Ez8Est9OtlI2-TdlCOdrTVWAaDggy0VqB3prB3xdfrcrVli057AcL8j1YUm6SuuXGjs-SlNzUoYRDUQM0FlKDEi2_VyT5Cl79kZIP-rcqBtvlbJlvFTlrXS_u7e3Vkjzbf47-EC-v8ddjoSEVXMBbkLnAon3d9Wxo8V4zDxmY1ZBHbb7EP_BaHZeQ-5akR7ZFc13YZxLoad-B615KYi9j0XiFFbrczxk-TYKVcwadF288ZcJPCj_GghgesminQRLvvVzxHiCEqvoWAPbzJtBR3r-4m1s0V0M_scYgZWK5JHhCJh6F2-nY0QIeXVS71cvHjC1fF7JnW9aIpfxp1F4mc63__vFHExMskQEg_SOygFslTMZijBej-BxFf_D10Ypee90JWCiofQ9uePAB2DJTjdEy9TXRBVgBXOLlLq-bXwvmhnmpqTkeDCo9EeXW6WlhoTdQ0klaZEN3kACkXGX5_ZPenOF8PIHuJ4RDAq0QVk0ois" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
خودِ آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا حکومت ایران را سرنگون کند.
اطرافیان نتانیاهو اعلام کرده بودند که نیروهایی از استان‌های کردستان و بلوچستان به مراکز کلان‌شهری نفوذ خواهند کرد تا حکومت را ساقط کنند.
آن‌ها تصور می‌کردند که این ماجرا سه روزه تمام می‌شود و حکومت سقوط می‌کند؛ اما حکومت استوار ماند و منسجم‌تر و متحدتر شد.
حتی کسانی که به دلایل گوناگون در برابر حکومت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72245" target="_blank">📅 07:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72244">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=jPfcUtanSNySZFLOZuBaAQSDMgMLNcKhkOW9bbJkty1yC-J4m7ZQZYafhqf4aitANnz-_CblzzECDABIK2T5PGNheueLD5BOcHSf7g74vuv2MsES9PHN2uxPtWyIoxw01LznGZLd519KTxE54WZ7eJ5Euhxdc-ZJciHdD5wdR7VrY3_C7aYhk84EJ3dwfhs2Yyub9W5Fmw2Qcrn12J_FxcG1bN1AhdLihPBkRGn4MeeOXPqA3xNV7kw56HSrR1W7kpHIyor6iQMtVxFsp0yrCFDEjAxjkzVzlmhUZkVwMq32m_DBTG6Ye63X6zukz_MHJ8PGfzvGNx9J6xj-U8rBFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=jPfcUtanSNySZFLOZuBaAQSDMgMLNcKhkOW9bbJkty1yC-J4m7ZQZYafhqf4aitANnz-_CblzzECDABIK2T5PGNheueLD5BOcHSf7g74vuv2MsES9PHN2uxPtWyIoxw01LznGZLd519KTxE54WZ7eJ5Euhxdc-ZJciHdD5wdR7VrY3_C7aYhk84EJ3dwfhs2Yyub9W5Fmw2Qcrn12J_FxcG1bN1AhdLihPBkRGn4MeeOXPqA3xNV7kw56HSrR1W7kpHIyor6iQMtVxFsp0yrCFDEjAxjkzVzlmhUZkVwMq32m_DBTG6Ye63X6zukz_MHJ8PGfzvGNx9J6xj-U8rBFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر (از شبکه فاکس):
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی مدارس ما را هدف قرار داد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، قطعاً نیروهای امنیتی شما شهروندان ایرانی را کشتند.
پزشکیان:
خیر اصلا اینگونه نبود.آنها تروریست هایی بودند که توسط آمریکا و موساد و کرد‌ها مسلح شده بودند.ما به مردم عادی آسیبی نزدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72244" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=NmewJH88I7z6y2Q5OWx244-6QMMsDeWS505-9_umt6Wpn2Bz_PuRoDReNkTHo9nzCMeofBwqjIUdcdt0KJaUOzM7xecycOukfnVCEexq9bD-e_4_zdfT5Xliw09pOM9CMIxrmY5G57KW46IIS35I3IGt7xbaOodA8zUjMh6KezxRtF1w5HTfjcMRQBJNkCmMb8nLIjLCh57qAGns0IsBSyzuCvWeDKA9y4D0KY9FpBkEJyWHwNxfWkTyOPYtmZh5p14WLSHj7GI2t6XWz1v0rTMoNRkAHEOqnKEvyp9Y_5QXEtrERMe0fexQd_SLcEfBNpHS64Zujtc40VZgOXyNvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=NmewJH88I7z6y2Q5OWx244-6QMMsDeWS505-9_umt6Wpn2Bz_PuRoDReNkTHo9nzCMeofBwqjIUdcdt0KJaUOzM7xecycOukfnVCEexq9bD-e_4_zdfT5Xliw09pOM9CMIxrmY5G57KW46IIS35I3IGt7xbaOodA8zUjMh6KezxRtF1w5HTfjcMRQBJNkCmMb8nLIjLCh57qAGns0IsBSyzuCvWeDKA9y4D0KY9FpBkEJyWHwNxfWkTyOPYtmZh5p14WLSHj7GI2t6XWz1v0rTMoNRkAHEOqnKEvyp9Y_5QXEtrERMe0fexQd_SLcEfBNpHS64Zujtc40VZgOXyNvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
رئیس‌جمهور آمریکا اعلام کرد که ما تروریست هستیم.
اما در واقعیت، همه به‌راحتی می‌توانند تشخیص دهند که ما قربانی و هدف تروریسم بوده‌ایم؛ با این حال آن‌ها می‌گویند: «نه، ما چنین کاری نکردیم.»
آن‌ها حقیقتی آشکار را انکار می‌کنند، اما در عین حال ما را به چنین اقداماتی متهم می‌سازند.
ما خواهان زندگی در صلح و آرامش در منطقه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72243" target="_blank">📅 07:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=KMRjQdnoy7a76F6ZH3I5yFAlOqx_amO2s5ND-IaxBc76SP_yXjiVECd-GWiTkufPjUSLeZiER4uv4M_j_glJqydkWp_Fey3liAh0BVPPfcqAOJriDX0q05dzNkrdSbJsfzT7D8ER596R31rmqP6WhnQNqw5Pw9iNv46wgIZfYcJhgCzWw-unXoYusBZCnxxXvdR7j374uzbUpShwbmMWPNxLMBsq7PspbkBGA0mqqOMjtq-UcIksjt9K3_WThyHkufsVvmHWZN6lbGqQl8twgMfi3c1CrtCyP9UD_gqH2_i4d30ALRKjyiZ3EFkRDWdbUgvp6ny4ifG2IPgT-7KiJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=KMRjQdnoy7a76F6ZH3I5yFAlOqx_amO2s5ND-IaxBc76SP_yXjiVECd-GWiTkufPjUSLeZiER4uv4M_j_glJqydkWp_Fey3liAh0BVPPfcqAOJriDX0q05dzNkrdSbJsfzT7D8ER596R31rmqP6WhnQNqw5Pw9iNv46wgIZfYcJhgCzWw-unXoYusBZCnxxXvdR7j374uzbUpShwbmMWPNxLMBsq7PspbkBGA0mqqOMjtq-UcIksjt9K3_WThyHkufsVvmHWZN6lbGqQl8twgMfi3c1CrtCyP9UD_gqH2_i4d30ALRKjyiZ3EFkRDWdbUgvp6ny4ifG2IPgT-7KiJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما تا آخرین لحظه به مقاومت ادامه خواهیم داد.
بله، قطعاً مشکلات اقتصادی داریم؛ اما برای بقا، از هر سختی‌ای عبور خواهیم کرد و ایستادگی خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72242" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=H3CSXcOCZPdNbMVcBRmq5jfpn-rLJNFkIOUH3V8W0XHI3ZAcqwWLiA05rnfAJFPp7uUxqdaNaYpRv9sh7DdKAroNUq4SHRsph6AHxhAaL6-FKZmPVagCYY32gr582lR21mJZt6ZiJ1Fvz7FOyS04FDeArrHjGljZPLrJfMhO4R310d97MTHS-WIoAUo8EeouHlLUGfZobmoNSbuBNoQ2pwXDNudGwtx2nIUFHpCQN8Naj03L1PGUjj4Hdf5RfGGb5vZpWk66ZH0-wtBkAlzgCHwnzzbSmUzAldsOHIqUlu9vZ4GpzOgic789yAN5ys6bk5kYGyqP7W10drR4bWWUWH0Clufo3zhcOpMQvTfOcwOR6QUTePbc5v_Y_Tecggut2cJshPuVqjhkNN4DQvk-FeN1iFSVdrxXJqSem5usGAJPRh5RmTtQk20AAsoGBJem3VAU0qnGmUJUYWdrhw07GVP0qVM1Xks8xQuwVE0Xt1WV5vUHsFvZ0X_tauTNWoFtDmFmW-rWxTf3l0tyQfSmI6Ubnk96ZiuXmajccZOvPvSPtqBxhwTvATUFnHizhIG_ELwG-kcThOoE16XuaJfu7xxdU3qVk6_ry2WqC8AiAr9MILGeouGy3kd7uO7hBgZ1_20qxJowQGtUMumRhq8DTmmuZA7AavHUvO0Nab8KTj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=H3CSXcOCZPdNbMVcBRmq5jfpn-rLJNFkIOUH3V8W0XHI3ZAcqwWLiA05rnfAJFPp7uUxqdaNaYpRv9sh7DdKAroNUq4SHRsph6AHxhAaL6-FKZmPVagCYY32gr582lR21mJZt6ZiJ1Fvz7FOyS04FDeArrHjGljZPLrJfMhO4R310d97MTHS-WIoAUo8EeouHlLUGfZobmoNSbuBNoQ2pwXDNudGwtx2nIUFHpCQN8Naj03L1PGUjj4Hdf5RfGGb5vZpWk66ZH0-wtBkAlzgCHwnzzbSmUzAldsOHIqUlu9vZ4GpzOgic789yAN5ys6bk5kYGyqP7W10drR4bWWUWH0Clufo3zhcOpMQvTfOcwOR6QUTePbc5v_Y_Tecggut2cJshPuVqjhkNN4DQvk-FeN1iFSVdrxXJqSem5usGAJPRh5RmTtQk20AAsoGBJem3VAU0qnGmUJUYWdrhw07GVP0qVM1Xks8xQuwVE0Xt1WV5vUHsFvZ0X_tauTNWoFtDmFmW-rWxTf3l0tyQfSmI6Ubnk96ZiuXmajccZOvPvSPtqBxhwTvATUFnHizhIG_ELwG-kcThOoE16XuaJfu7xxdU3qVk6_ry2WqC8AiAr9MILGeouGy3kd7uO7hBgZ1_20qxJowQGtUMumRhq8DTmmuZA7AavHUvO0Nab8KTj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه‌ای بیاورم»، اما هدیه‌ای که آن‌ها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
آنچه آن‌ها واقعاً به دنبال آن هستند، دامن زدن به وقایعی در کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72241" target="_blank">📅 07:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=aDWcM50sacqFt05YMAPyxHIGG0gUCav443v3Q5dWfl2MabGyn0Mm8ur5WUHchAfvMZKDCJEmemGlGyYocJVRQpRZr10nsncQL8iDJQMIVCHGLJkw6RYCRqECLR38f9ZPdZq18bONzggLfmu5tkokXONJzkggGr9XIlcgwjyGE6F1Np8qgKIJZaLJOuDuU4lfw1Ao9giKkyyTNU8SXkkENc65IQJjLM8zpJScFhfb-hSTv0J9oGkJWt_n6DI0dZRebICLj0aGX15pwWt0gagg5PqsGAwbwhya9yl5OEWxojxgAQu6vPYUjPKlw8GXxjPQ4AHLjafkmomtZyHbU4vMww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=aDWcM50sacqFt05YMAPyxHIGG0gUCav443v3Q5dWfl2MabGyn0Mm8ur5WUHchAfvMZKDCJEmemGlGyYocJVRQpRZr10nsncQL8iDJQMIVCHGLJkw6RYCRqECLR38f9ZPdZq18bONzggLfmu5tkokXONJzkggGr9XIlcgwjyGE6F1Np8qgKIJZaLJOuDuU4lfw1Ao9giKkyyTNU8SXkkENc65IQJjLM8zpJScFhfb-hSTv0J9oGkJWt_n6DI0dZRebICLj0aGX15pwWt0gagg5PqsGAwbwhya9yl5OEWxojxgAQu6vPYUjPKlw8GXxjPQ4AHLjafkmomtZyHbU4vMww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت فعلی آمریکا بخواهد در چارچوب حقوق بین‌الملل به توافق برسد، بسیار خب.
اگر نه، چه پیش از انتخابات باشد و چه پس از آن، برای ما چه تفاوتی دارد؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72240" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72239">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=arko8QocafeTC_ZLWRQ9yy4ZdqE-QV7lH2qAMPVGDXrOyB4Eh0XKkquDZtHB_d20Pd8x2OxBy7oiE3MxlpbgQgbs_AhPvqKRZmTuQd7FCcKbtBFZMOFntxmQepsORZC6seIA32PpG2FTU48ShukWYrxXAmZEC3lyAZT2c3xThyHTSkwMzJ4RaixFGAPpSieF_bsWTSHx3TZfilqhtkQxQJJMuyCVUSHsGKtC9nBztDZIt1tRzkA6gj9r3u35oGmXzUbjNN2NbHDl1Hk94ISayXikuTwI2W33gym1Ap2vx9J6RPvXNvvMRaLtfKcqz4TWEVLE5dvfgYw3GLvEZW_8ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=arko8QocafeTC_ZLWRQ9yy4ZdqE-QV7lH2qAMPVGDXrOyB4Eh0XKkquDZtHB_d20Pd8x2OxBy7oiE3MxlpbgQgbs_AhPvqKRZmTuQd7FCcKbtBFZMOFntxmQepsORZC6seIA32PpG2FTU48ShukWYrxXAmZEC3lyAZT2c3xThyHTSkwMzJ4RaixFGAPpSieF_bsWTSHx3TZfilqhtkQxQJJMuyCVUSHsGKtC9nBztDZIt1tRzkA6gj9r3u35oGmXzUbjNN2NbHDl1Hk94ISayXikuTwI2W33gym1Ap2vx9J6RPvXNvvMRaLtfKcqz4TWEVLE5dvfgYw3GLvEZW_8ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما هرگز به دنبال جنگ نبوده‌ایم و نیستیم. من عمیقاً معتقدم که انسان‌ها نباید موجب مرگ انسان دیگری شوند.
قرار است ما موجودات برگزیده خلقت باشیم. وقتی می‌توانیم مسائل را از طریق گفتگو حل‌وفصل کنیم، نباید به کشتن یکدیگر متوسل شویم.
اما با اقداماتی که اسرائیل انجام داده، آن‌ها این جنگ را به ما تحمیل کرده‌اند.
با این حال، ما خواهان ادامه آن نیستیم. این آمریکاست که باید تصمیم بگیرد آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72239" target="_blank">📅 07:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72238">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f631e90489.mp4?token=LdDQ2Xu7VxtUb8_9m904YtHNpVb6CUVNkdQP-WWFG_D68fybiai5bI1dvCaybuziZ1rFFPkWwyH3VYVXPKqqNcsgT8W_zDbP_8UTZtgcbhscCryMJrfTb9MkSSmyoDv2QlToQjSqMI92jfm7exORuir_TxbDJAWZm-y3fbJFhyd47PlrtwrmHUeB_FJcQl7y1kGBYmgI537EH-rigAjZSEH09of2kmvEtvK9cuacOx7jB-O2aNcx7ZcQK49qNLLJ1BwNCX9RcdZ79FdvvlzQ6pXMvPLinTTtqB0Ynn_Knktk5WD3M6eYCXnpA2qejfzdLMMVJMEJGdF4sTgq0c4HSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f631e90489.mp4?token=LdDQ2Xu7VxtUb8_9m904YtHNpVb6CUVNkdQP-WWFG_D68fybiai5bI1dvCaybuziZ1rFFPkWwyH3VYVXPKqqNcsgT8W_zDbP_8UTZtgcbhscCryMJrfTb9MkSSmyoDv2QlToQjSqMI92jfm7exORuir_TxbDJAWZm-y3fbJFhyd47PlrtwrmHUeB_FJcQl7y1kGBYmgI537EH-rigAjZSEH09of2kmvEtvK9cuacOx7jB-O2aNcx7ZcQK49qNLLJ1BwNCX9RcdZ79FdvvlzQ6pXMvPLinTTtqB0Ynn_Knktk5WD3M6eYCXnpA2qejfzdLMMVJMEJGdF4sTgq0c4HSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
یکی از مشکلاتی که با آن مواجه هستیم، مسدود بودن منابع مالی ما در چین است.
ما حتی نمی‌توانیم پول خود را از کشوری که به آن کالا صادر کرده‌ایم خارج کنیم، چه برسد به اینکه بخواهیم از آن وجوه برای پرداخت به طرفی دیگر در گوشه‌ای دیگر از جهان استفاده کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72238" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72237">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=Jhv4DqqUxZ9fqqrYuF-f6rJk-6POv-Qs7fdltu3UqdBM014y1Ocov1Hh_lweNWgoNGUkxG5EVmLyhv2WEifEhwH8_mKohZfmcrnZYi0VBGyBcaL_qoCqQqcVBTFqK3aEQE-9hDOZFmmeXkOYLS5Wg7QcdmWgnfJz5XVwhCS8pw8l22vwpDUNehUz-7BrNIBNIyNF_QBwiiCwTzfESHZXhbr0ou6hlwMyt4q3kqM483aAtQgpAOUiAgHOrYDAAUGx1mU2MO_o87lbPdZiZtUrK3tF3HLiRT5v_9NnNqPNhwl4IFKchBjkaO1t9JEg3ZYJHjfy8KNVwkHGGFm4IIqnnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=Jhv4DqqUxZ9fqqrYuF-f6rJk-6POv-Qs7fdltu3UqdBM014y1Ocov1Hh_lweNWgoNGUkxG5EVmLyhv2WEifEhwH8_mKohZfmcrnZYi0VBGyBcaL_qoCqQqcVBTFqK3aEQE-9hDOZFmmeXkOYLS5Wg7QcdmWgnfJz5XVwhCS8pw8l22vwpDUNehUz-7BrNIBNIyNF_QBwiiCwTzfESHZXhbr0ou6hlwMyt4q3kqM483aAtQgpAOUiAgHOrYDAAUGx1mU2MO_o87lbPdZiZtUrK3tF3HLiRT5v_9NnNqPNhwl4IFKchBjkaO1t9JEg3ZYJHjfy8KNVwkHGGFm4IIqnnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با خبرنگار فاکس‌نیوز:
هر کس بخواهد اعتراض کند، کاملاً حق انجام این کار را دارد.
ما با بسیاری از این کارشناسان گفتگو کرده‌ایم. اما تبدیل اعتراضات به ابزاری برای تقابل (مسلح کردن معترضان)، مقوله‌ای کاملاً متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72237" target="_blank">📅 07:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72236">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72236" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72235">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9v64Hvkp1ld1gyBV-VTq90PFWcA71w5Se_ShMUcI0n2YA3DqHgrVOSoqx0nIVlY-fPJsWNmrtT1UcLzKd4oPuI7B1ThgZfyY9kk9E2e5LIL7ftxVTU4xT8N47OLwG7nbVlyAAHN8POZA17S7UzsbOlY2hWodTgFzCyBhp_em0frlm3Dgi4z10B2-sxe5HxMq9tkffMYHL1xa6OtrHAnzP5kudEVDY_B9PBop060DsfExNiHSKD10ftY1lzDSMOfzekWVMzoOpIybRyXsVlaPdD5D8Qsf79wjbfM4RbWsrRCpVN84d7Na9qFHEW4QjOKpv_k3-HMCeKyHBPcTkkTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72235" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72234">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25201994ac.mp4?token=Su-Uwt4yq7tCz5LOprILQIirBTHB4gtuLY6-RsxUq8yc4PZ5o8NyR-Cdg3xiw3Pn15jfDuStLzzqfCQwCSxDqW071MpmNEigErfEtZsFW5G-5NRl4_8BGEoygPWyR97czVKWlEO97PBKmSAtsR_0gKhSzr-EZtZbHGsZubS6z6p7-X-Phplw2vtAaCve8P8miGYSCru3Xv31Umn7TFRjwfsdqF4-A6cZW6QUUkA3POOP7f7mzyb1YxU7oavWqN8gwoYAtNYZdA0EGgUvfQHlHkR0ZcGp4LfxeScOBiGIH3v33TNa6c24PXR590PUyiBLd1zt8Wa5zoR6eRSebv0Prg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25201994ac.mp4?token=Su-Uwt4yq7tCz5LOprILQIirBTHB4gtuLY6-RsxUq8yc4PZ5o8NyR-Cdg3xiw3Pn15jfDuStLzzqfCQwCSxDqW071MpmNEigErfEtZsFW5G-5NRl4_8BGEoygPWyR97czVKWlEO97PBKmSAtsR_0gKhSzr-EZtZbHGsZubS6z6p7-X-Phplw2vtAaCve8P8miGYSCru3Xv31Umn7TFRjwfsdqF4-A6cZW6QUUkA3POOP7f7mzyb1YxU7oavWqN8gwoYAtNYZdA0EGgUvfQHlHkR0ZcGp4LfxeScOBiGIH3v33TNa6c24PXR590PUyiBLd1zt8Wa5zoR6eRSebv0Prg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
🇮🇷
🇮🇱
🌟
نماینده اسرائیل در سازمان ملل دستگاه «استارلینک» را به نماینده اعزامی تهران داد و درباره «کمک به مردم ایران برای سرنوشت و آزادی با این دستگاه» صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72234" target="_blank">📅 01:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72233">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=n8aIhFr9gIzRUAG2_UNC9Uy2PA2adYQ0oC8kucDCH18_CNLscyOPTdxKnAZLZXKHHbTxTOiANWPhKI5NG0mhjJuID6xuOUomI7KGRZxh0su72nBAWlxt20Z3e_n7yzlaxnM0Lee5rQ8F5ruLPlFUidpmDNHTF6jgnAhC6MugKe9k3YHbkf1nOzUaMEy0KcuFYj_aw7sai2YS79GpQqybs7lIYfrRpPFwjeANLd0J1WZim4pYGmd8w6IUkXRbCnipZYOvHMAXSfu5wqq8YOZ3rfTR_zNToGxWSHMjG9xOBZzLujrumhTpaNwO4oddTUf9CEgJAOZVWtZT18TYylr9fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=n8aIhFr9gIzRUAG2_UNC9Uy2PA2adYQ0oC8kucDCH18_CNLscyOPTdxKnAZLZXKHHbTxTOiANWPhKI5NG0mhjJuID6xuOUomI7KGRZxh0su72nBAWlxt20Z3e_n7yzlaxnM0Lee5rQ8F5ruLPlFUidpmDNHTF6jgnAhC6MugKe9k3YHbkf1nOzUaMEy0KcuFYj_aw7sai2YS79GpQqybs7lIYfrRpPFwjeANLd0J1WZim4pYGmd8w6IUkXRbCnipZYOvHMAXSfu5wqq8YOZ3rfTR_zNToGxWSHMjG9xOBZzLujrumhTpaNwO4oddTUf9CEgJAOZVWtZT18TYylr9fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستربین ۷۱ ساله شد و جشن تولدشو با صدای بانو هایده جشن گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72233" target="_blank">📅 00:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72230">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=pU5w3mES8U1wg7Teikny6-H0SohT1XiBmiHxvDavgOkC45vOtl28c7LbftROIrw0CgqtesKK22aUMmL725DXE6OB5jPdQbpJq1y73QMiBmnZuYbd9IUlgEPwvaQQ-N4KY0jHpxwBRt9yfwWKLbCXGygEd1BV42np0-dUD8agr8a22f2PobkFwCVKTtXOd9Fq0SqFacOE0URpNO7WNrA1m4EZMW64vnR-o8A-bnGw_vBUdtZrIawE26cEqSf6s_osI0vzsl3sG5dnPlgB1pru06F41NyhXP33CAGpRVuT220qPo0SX6M9n5QM9aGhLvYVBIUZvYAHZf_9xgYb-5T1Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=pU5w3mES8U1wg7Teikny6-H0SohT1XiBmiHxvDavgOkC45vOtl28c7LbftROIrw0CgqtesKK22aUMmL725DXE6OB5jPdQbpJq1y73QMiBmnZuYbd9IUlgEPwvaQQ-N4KY0jHpxwBRt9yfwWKLbCXGygEd1BV42np0-dUD8agr8a22f2PobkFwCVKTtXOd9Fq0SqFacOE0URpNO7WNrA1m4EZMW64vnR-o8A-bnGw_vBUdtZrIawE26cEqSf6s_osI0vzsl3sG5dnPlgB1pru06F41NyhXP33CAGpRVuT220qPo0SX6M9n5QM9aGhLvYVBIUZvYAHZf_9xgYb-5T1Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جالب رئیس جمهور چین  به اقدام ترامپ برای جاگزین کردن عکس بایدن با «خودکار»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72230" target="_blank">📅 00:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72229">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=XGwo-i9d5Bpmag0YZ-nosaK64plvntYfFM0DW4haMUtTiBX4RayxKYefdwtxUpElpEpQ7y5Dn9fkVATiZA_1dYJXISKOlzJzsefxBP0ahQhTkLWtCxQQDGa06gXGp2bhJD5jfj61eFnqnMSD3PNZVgoRPX10cQ03zgQzIjxzEviUahtgs1H7mareLya9nGpYpM_cyiS0AXCriaicegyidOq2zGuQf2ZO6gWfLs0fdM2zyP8A4dSANKL7uL3252n5-YAlbxxp7TUf-V5Rs7G2kWNm9LDwLRaCsP85LalgXdMSBVUrPh-gcKu0_gh_qbxi2-lHL_sfd3q0J-EHIC_oUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=XGwo-i9d5Bpmag0YZ-nosaK64plvntYfFM0DW4haMUtTiBX4RayxKYefdwtxUpElpEpQ7y5Dn9fkVATiZA_1dYJXISKOlzJzsefxBP0ahQhTkLWtCxQQDGa06gXGp2bhJD5jfj61eFnqnMSD3PNZVgoRPX10cQ03zgQzIjxzEviUahtgs1H7mareLya9nGpYpM_cyiS0AXCriaicegyidOq2zGuQf2ZO6gWfLs0fdM2zyP8A4dSANKL7uL3252n5-YAlbxxp7TUf-V5Rs7G2kWNm9LDwLRaCsP85LalgXdMSBVUrPh-gcKu0_gh_qbxi2-lHL_sfd3q0J-EHIC_oUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این تحرکات لجستیکی و نظامی آمریکا باید توافق رو قطعی بدونیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72229" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72228">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عجب دنیاییه، پزشکیان رفت سازمان ملل از مردم غزه حمایت کرد، نتانیاهو هم رفت از مردم ایران حمایت کرد
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72228" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
می‌خواهم از شما بخواهم که با دقت به حرف‌های من گوش دهید. روزی خواهد رسید، و ممکن است این روز خیلی دور نباشد، که مردم ایران آزاد خواهند شد.
این رژیم خبیث، به دلیل دروغ‌هایش، فسادش و ظلمش، سقوط خواهد کرد. این رژیم ستمگر فرو خواهد پاشید و همه ما در آن روز جشن خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72227" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
این یک دستگاه ارتباطی استارلینک است که به مردم اجازه می‌دهد به حقیقت دسترسی داشته باشند، آزادی اندیشه و آزادی بیان را تجربه کنند.
به همین دلیل است که رژیم ایران میلیاردها دلار برای سانسور اینترنت هزینه می‌کند.
آقای رئیس جمهور، من این دستگاه را پیش شما می‌گذارم تا بتوانید آن را به هیئت ایرانی بدهید.
بنابراین، وقتی آنها ناگزیر به ترک کشور شدند، آنها نیز می‌توانند آزادانه داستان خود را در رسانه‌های اجتماعی بیان کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72226" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72224">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو: خدا باماست
سخنرانی تموم شد
#hjAly‌</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72224" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72223">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو: روز آزادی مردم ایران رو باهم جشن می‌گیریم
#hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72223" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72222">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو: یه روزی که خیلی دیر نیست، مردم ایران آزاد می‌شن
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72222" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو: نیروی مردم ایران، آخوند رو شکست می‌ده
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72221" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: شما مدافعان قلابی حقوق بشرین
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72220" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72219">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: وقتی آخوندا هزاران معترض رو کشتن شماها کجاها بودین؟
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72219" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72218">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو: آخوندا می‌ترسن که مردمشون استارلینک داشته باشن
#hjAly‌</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72218" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72217">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=oWkj-rfJGWEDZfadDkukA5KeQTl0T4CT1DqwvYy3KkMkkuFV_TWYe9iT6j54-kLBdfwH-JBP1Uv7seoCveFa79NcUVUHcGdGbnNNhoMbc-kB9G4hlgn1p-r0kLR8ZVfggmcdK1W7cL_CG357iRLTDDS4w3xq5bTaEA-rX8hp8YZ8QTNsqd-FUIL_yc98nZbLkgRC5tQOSJ30afEY1JkNW5RUgXLwE54KyJoWWnxNSGs48c8DBQEd0CpaFALWYfn-_kN5YDOcOu8rg1LegwNf2XjolN4Y7CCac0l19_e7p_fJAWqbzkMzrT2jGg16qEuekGuvdOUhURYcjoQ8eNcy6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=oWkj-rfJGWEDZfadDkukA5KeQTl0T4CT1DqwvYy3KkMkkuFV_TWYe9iT6j54-kLBdfwH-JBP1Uv7seoCveFa79NcUVUHcGdGbnNNhoMbc-kB9G4hlgn1p-r0kLR8ZVfggmcdK1W7cL_CG357iRLTDDS4w3xq5bTaEA-rX8hp8YZ8QTNsqd-FUIL_yc98nZbLkgRC5tQOSJ30afEY1JkNW5RUgXLwE54KyJoWWnxNSGs48c8DBQEd0CpaFALWYfn-_kN5YDOcOu8rg1LegwNf2XjolN4Y7CCac0l19_e7p_fJAWqbzkMzrT2jGg16qEuekGuvdOUhURYcjoQ8eNcy6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
اخلاقی‌ترین ارتش جهان؛ ارتش اسرائیل (IDF).»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72217" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72216">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو: هرگز نسل‌کشی نکردیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72216" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72215">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو: آقای ممدانی تلاش کردی من نیام نیویورک، دیدی کیر شدی؟
#hjAly‌</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72215" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72214">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو: کیرم تو ممدانی و زنش و دوستاش
#hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72214" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72213">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو: ما کلی واکسن و غذا به مردم غزه دادیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72213" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72212">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو: اردوغانِ جاکش، تو هیچوقت حاکم قدس نمی‌شی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72212" target="_blank">📅 21:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72211">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتانیاهو: کیرم تو ترکیه
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72211" target="_blank">📅 21:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72210">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو: کیرم تو قطر
#hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72210" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72209">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=g5RZsXMr9PTgZufFETycWl-jpHnOIwVogKK4rQqjrJJJZfqhcIkjtifoCfBwe1d0KzaW2Nw21eiOmDTJ67IquTnZvocBHhXLXYVsPmhWs8HOrnfSyZnUA-rDI2MR6es-m7fxKr-nnmXvt5FRUQAh7OVjEjNa8_79V0_5C-SE-zblxLExrag1XU_LSjlDKITNU8Db0IyaU7IqArcbyhTGOfzRQ-eC7QiZt3WirCX1dd75Ok1YrCtf-e49ScxgCyxSWkKYqpCRfuFmhaalPMyvkj-wRNBB3vhJJZTKFf5nQwsRvWHgNfWinH7gtxEawRvP68MQXzemt2EErRs_6kNCig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=g5RZsXMr9PTgZufFETycWl-jpHnOIwVogKK4rQqjrJJJZfqhcIkjtifoCfBwe1d0KzaW2Nw21eiOmDTJ67IquTnZvocBHhXLXYVsPmhWs8HOrnfSyZnUA-rDI2MR6es-m7fxKr-nnmXvt5FRUQAh7OVjEjNa8_79V0_5C-SE-zblxLExrag1XU_LSjlDKITNU8Db0IyaU7IqArcbyhTGOfzRQ-eC7QiZt3WirCX1dd75Ok1YrCtf-e49ScxgCyxSWkKYqpCRfuFmhaalPMyvkj-wRNBB3vhJJZTKFf5nQwsRvWHgNfWinH7gtxEawRvP68MQXzemt2EErRs_6kNCig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
با دوستان آمریکایی خوبمان، ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را در هم کوبیدیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72209" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72208">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJm2BVEvTkACmqMHGmHd5lD8nyp3h_YeTdHowhpte5X1tXvyqBTm2u34qS4Lav2_A7S63OFXx6bN-UlPFRB65p9JjPccj0IMkDcFOsOjSKk3nFumjLGBaI6M43Ad_VoV0x-o69VeLm-a3y-tAD6ef8FoWD-YnAz8u5IbwUwnOos-ZvuWV-LmeW0h9oSlCUMLq-mBen7aG7lBJCfODuzh7q8MKDKnJz5cO3bXuafhKOonvBZXegvDN67osbnqBBZecdfjBy0fO-1soT9wENZR4cTBbhISX8HUuo1enqZfAvy74af1Xnpga9hK82xn0SV7K8Ol2ispkO0Zp-cm_CMFczB78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJm2BVEvTkACmqMHGmHd5lD8nyp3h_YeTdHowhpte5X1tXvyqBTm2u34qS4Lav2_A7S63OFXx6bN-UlPFRB65p9JjPccj0IMkDcFOsOjSKk3nFumjLGBaI6M43Ad_VoV0x-o69VeLm-a3y-tAD6ef8FoWD-YnAz8u5IbwUwnOos-ZvuWV-LmeW0h9oSlCUMLq-mBen7aG7lBJCfODuzh7q8MKDKnJz5cO3bXuafhKOonvBZXegvDN67osbnqBBZecdfjBy0fO-1soT9wENZR4cTBbhISX8HUuo1enqZfAvy74af1Xnpga9hK82xn0SV7K8Ol2ispkO0Zp-cm_CMFczB78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
آنها به زنان باردار تیراندازی می‌کنند و خانواده‌های کامل را هدف قرار می‌دهند. البته هیچ‌کدام از این موارد در رسانه‌های بین‌المللی یا شبکه‌های اجتماعی پوشش داده نمی‌شود؛ هیچ‌کدام!
آنچه پوشش داده می‌شود، گروهی حدود ۱۵۰ جوان کم‌سن‌وسال بزهکار هستند که می‌روند و سنگ پرتاب می‌کنند و درختان زیتون را قطع می‌کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72208" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72207">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو: هدف فقط پیروزیه، همونطور که داداشم یونی گفت، ما مجبوریم پیروز بشیم
#hjAly‌</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72207" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72205">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو: دم ترامپ گرم داداشیمه
#hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72205" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72204">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو: خامنه‌ای دیگه مرده
🔥
🔥
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72204" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72203">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتانیاهو: این پیجر های تو دستم رو می‌بینید؟ حزب‌اللهیا که خوب یادشونه، با همینا دهنشونو گاییدم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72203" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72202">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو: خدایی کیو دیدین مث ما که تو هفت جبهه همزمان بجنگه؟
#hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72202" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72201">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهو: مث شیر می‌جنگیم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72201" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72200">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نتانیاهو: سال‌ها پیش داداشم یونی تو جنگ با اعراب بهم گفت ما پیروز می‌شیم، الان من همینو می‌گم، ما پیروز می‌شیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72200" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72198">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو: اسرائیل کوچولوعه، انگلیسی های جاکش که خودشون استعمار رو اختراع کردن به ما می‌گن استعمارگر، کیرم دهنتون
#hjAly‌</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72198" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72196">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو: ما به کشورای زیادی کمک کردیم، یسری از همین جاکشایی که الان رفتن بیرون هم از ما تشکر کردن، کیر تو هرچی ریاکاره
#hjAly‌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72196" target="_blank">📅 21:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72195">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: نابود کردن تاسیسات هسته‌ای جمهوری اسلامی سخت بود ولی انجامش دادم، اگه این کارو نکرده بودیم همه مرده بودیم
#hjAly‌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72195" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72194">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتانیاهو: نمی‌زارم آخوندای قاتل به سلاح هسته‌ای برسن
#hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72194" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72193">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو: کیرم تو جمهوری اسلامی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72193" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72192">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72192" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72190">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!  این سخنرانی تا دقایقی دیگه آغاز می‌شه #hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72190" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72189">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHMp13g7fofsfic0vpbiw3goJFwvzTd6VSASuSlheHusx2_3Y6D0IgjIWxtsWIe7JJKwF9RiDwfFqQh4BCHyTgdRhXbFi4JLkciTQ9LSctncy9wmTrHjCofPii9aBZEDHqKy-Ry-adpiqzH7PyeAKkVXhlusAVOLO6MdQnveZTAehy2Bo5zrIP8AIu31DXL67E0qRYLXXRAdJzJOuS-OKGG90Hmc_lGvPnZ74TF8hMm6Q9vmLDpaqOnreav8iCylF2d9MCHOsh6Nbe_HwTDUO8rylAqBYECDpouHxUU3QuymFCMucoh8Gd_Mzh2ZSMtZ3YayyGzEizcWZFYfenkTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان درحال مصاحبه با فاکس‌نیوز آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72189" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72188">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=jKZFUmwjvDI3qSeZ_y5bdfBZv2jDSx5Z6Z5gNfMfSWpD6_NZ3ic2oWf0Zj_3QXcTm37kfLgDS2x-RYagSIAIhJTARshLsEZF3E-xcVieI0zrZmcv16Bdkqx1eB3xYlqKmZYKXoOWliLbVPjro0C_POsnFHFHLubzdjV1JhI3OKEwWRLwtTGbdPBzQdpAxHHJNh4ZST_MWQgtpHnbaszcwc8U_sh_K1S08a7Z1rzJ9hqJ0IjY1YSZJDDzC4LaarwhLUwaGt2T0jUvCK3KhGhGR8OnyvCPxQfH7wbQ9reNpKbnNaYeohOf2Adr2GXNRggRAihPvNp5Mue0eixjfZkuvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=jKZFUmwjvDI3qSeZ_y5bdfBZv2jDSx5Z6Z5gNfMfSWpD6_NZ3ic2oWf0Zj_3QXcTm37kfLgDS2x-RYagSIAIhJTARshLsEZF3E-xcVieI0zrZmcv16Bdkqx1eB3xYlqKmZYKXoOWliLbVPjro0C_POsnFHFHLubzdjV1JhI3OKEwWRLwtTGbdPBzQdpAxHHJNh4ZST_MWQgtpHnbaszcwc8U_sh_K1S08a7Z1rzJ9hqJ0IjY1YSZJDDzC4LaarwhLUwaGt2T0jUvCK3KhGhGR8OnyvCPxQfH7wbQ9reNpKbnNaYeohOf2Adr2GXNRggRAihPvNp5Mue0eixjfZkuvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوزوی‌ها به روش خودشان برای بهبود چهره روحانیت در اقشار میانی جامعه کارزار به روز شدن راه انداخته‌اند؛ آنهم با «جوانگرایی»!
یک آخوند مبلغ، طلبه جوانی به نام «رضایی» را به شهربازی مشهد برده و از هر فرصتی برای مالش و ملعبه با او استفاده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72188" target="_blank">📅 21:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72187">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=W5IBcNqCV6iY7giYS383fzq1BJw8QlgzXgnObwInd7yZWF3nysJPoknYRIyyLYpBGODgD3HzM_J6UWBm-00bxVqSXQ7ii6c1DmFwQzwghjQx7nM5ncToK-YuzOH6erVr3pFFK4T7VYgdkUiGF0JN3xJELACXs3EKvBSV06ThJZNhflJigqVtgO-1t7pIAkP-LCLlQgxOQrBG_HsusiW17UlFPxKPLZ6zcuVpWruy7FIvrgiEUpXwD8auWgS4-ZWGsSl2fkbiyZWMvua6n_r7Lzv6tHIk1zHbeGS65-0r946mWdTDPR0LMw8fW812TtXmOU9B3eBjyPGNJrCtr2G_oZJyI0xs_5tlYwnNmoo_VT13AFi1FFYInkLU4EcECEd819JNFAsNy6zW1TPnbm2MLo_FvJjrZ0ER6UqqYI1wGTGLBtX_GSqrdoKfOJPpJNq8SGvE4_bu0hKH6YgDh4d3QvaXXtYsCqS1GQ4RZXu23aUpFO4TfaAYSxzgGTaCBme8IODtZssw98tn8s2oDEz7lhl08apH2-CmuuFya05v5A2Wbg-EFmkIew39JJXYdtJ1sClw8gBsrBDP_3dfaoa34EIyeEbDP62Mtfpjuno6Qt5gcB3qVD4U7gzw6TzWdmOvARs4oYoZsNaPWmSrpkOwAnBQ__Oac6u_HyggREMiYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=W5IBcNqCV6iY7giYS383fzq1BJw8QlgzXgnObwInd7yZWF3nysJPoknYRIyyLYpBGODgD3HzM_J6UWBm-00bxVqSXQ7ii6c1DmFwQzwghjQx7nM5ncToK-YuzOH6erVr3pFFK4T7VYgdkUiGF0JN3xJELACXs3EKvBSV06ThJZNhflJigqVtgO-1t7pIAkP-LCLlQgxOQrBG_HsusiW17UlFPxKPLZ6zcuVpWruy7FIvrgiEUpXwD8auWgS4-ZWGsSl2fkbiyZWMvua6n_r7Lzv6tHIk1zHbeGS65-0r946mWdTDPR0LMw8fW812TtXmOU9B3eBjyPGNJrCtr2G_oZJyI0xs_5tlYwnNmoo_VT13AFi1FFYInkLU4EcECEd819JNFAsNy6zW1TPnbm2MLo_FvJjrZ0ER6UqqYI1wGTGLBtX_GSqrdoKfOJPpJNq8SGvE4_bu0hKH6YgDh4d3QvaXXtYsCqS1GQ4RZXu23aUpFO4TfaAYSxzgGTaCBme8IODtZssw98tn8s2oDEz7lhl08apH2-CmuuFya05v5A2Wbg-EFmkIew39JJXYdtJ1sClw8gBsrBDP_3dfaoa34EIyeEbDP62Mtfpjuno6Qt5gcB3qVD4U7gzw6TzWdmOvARs4oYoZsNaPWmSrpkOwAnBQ__Oac6u_HyggREMiYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇱
🇮🇱
شماری از نیویورکی‌ها در اعتراض به حضور بنیامین نتانیاهو در این شهر تظاهرات کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72187" target="_blank">📅 21:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72186">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!
این سخنرانی تا دقایقی دیگه آغاز می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72186" target="_blank">📅 21:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72185">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90322c0135.mp4?token=KbQX0ERmxHjm1g_HPd9OWw8j9hkoin50CVHTaJaYrNJ4ZEtD6RBZkClDx_gnHEaQmuqsHijFAy7fZSnWH9ghG-0t9s_cpys7s2HaCDZGygB5puqMeh8XN4hOK4Idf9Bvmx_C-BadZgGI0N_aCjPXnQAqF7Sh030eLvhSc8aA3zrbj9a8zF06Ta_s5Cmnvk5clcyA5o0D5GYaLQeiuHI05uiDbrM2OrFcPPXNh_PwFtyp6gRxnbR9EDuI91jxkAkd5svZfHgVPKqI4GWGOL3bikCRD1HSfNZVQYWCXQVF-2Fg0Mt2eVcdVayKTEBWiMbTSOmAk7T_FwllcHjptW7MwYhKG-cgXlPGCSycb3q8xltV1SYOxpdaYKihTgZl6p5Bw9DQh5NjI6W-n4d-0Klm2qsyQLYxyRTk6vRUuWrogDBIMSQhIekVZES-EZ-cA-zyj0EJqjGQvwMJYDzyVTN-VmEa9OC0I73f6niDenwtafe5KhQ0k_YU_DWo_EbGd-DOCey4DmfL2D7Drz8uJvIEMbSSvnyJ1q8rU8TMziE_efKh7bJrb_IEhb8NX7n9m8eEgsCrpKQO5WPTFEIG8CmORtz2K_0hXoKj4bCSEKb-toginoilCZNiXIEzKxG8cIiWcuqwMHqSldhil2ZPZt24srmpn0EsvI1yguhW8fjKoIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90322c0135.mp4?token=KbQX0ERmxHjm1g_HPd9OWw8j9hkoin50CVHTaJaYrNJ4ZEtD6RBZkClDx_gnHEaQmuqsHijFAy7fZSnWH9ghG-0t9s_cpys7s2HaCDZGygB5puqMeh8XN4hOK4Idf9Bvmx_C-BadZgGI0N_aCjPXnQAqF7Sh030eLvhSc8aA3zrbj9a8zF06Ta_s5Cmnvk5clcyA5o0D5GYaLQeiuHI05uiDbrM2OrFcPPXNh_PwFtyp6gRxnbR9EDuI91jxkAkd5svZfHgVPKqI4GWGOL3bikCRD1HSfNZVQYWCXQVF-2Fg0Mt2eVcdVayKTEBWiMbTSOmAk7T_FwllcHjptW7MwYhKG-cgXlPGCSycb3q8xltV1SYOxpdaYKihTgZl6p5Bw9DQh5NjI6W-n4d-0Klm2qsyQLYxyRTk6vRUuWrogDBIMSQhIekVZES-EZ-cA-zyj0EJqjGQvwMJYDzyVTN-VmEa9OC0I73f6niDenwtafe5KhQ0k_YU_DWo_EbGd-DOCey4DmfL2D7Drz8uJvIEMbSSvnyJ1q8rU8TMziE_efKh7bJrb_IEhb8NX7n9m8eEgsCrpKQO5WPTFEIG8CmORtz2K_0hXoKj4bCSEKb-toginoilCZNiXIEzKxG8cIiWcuqwMHqSldhil2ZPZt24srmpn0EsvI1yguhW8fjKoIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇺🇸
🇺🇸
🇨🇳
دونالد ترامپ درباره شی جین‌پینگ: «شی در زمینه سنگ‌ها متخصص است و عاشق گرانیت باکیفیت است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72185" target="_blank">📅 21:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72184">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=HdGC-mxli4MtxjFTYgQ8XtuDsw0ODjhZuHylTXykLMQk74m8FaxX3sWVuDXLJ2G__1Jih-LVcpVcbPY56Vs43kJdlNjoioT8miE9VLxxk0ZGN9CbalUgkoac-_GHpgDGR1gPvdbqADkdq7B3WTeoOrGkDtXQ0BDphCyeb0MYAkMJ9IlZ_Aht99mrsa5X238sgVZ6VRj5hKMcfaHOhcgR9q6Qmslidml5t966A7U_BABdO5rPAAx6NwrhMufDlC7o1OR0k1jyzZpSFY7BC1LnL62U16FZFGYjDjACTTa5lF7_ROqmo95JM6u76nG3lJ02enaKLSBo-fveBugmBqI9O2ULRf-jpwnGSnNxxVy6v0DMVTKukp9eE7d1smKQHzJlWsultFVTAau9Xe__5CD_qIwUSl74ODG32j93AQlM8lTJyn6ZFCbzPQPBYHIvbo8BHLEbecWvQvRTfKFD8c80viuNg9lIQPDezb6c3734GJUKSlGcKD27vJjfF5TdjlvYsZhD96hUwd1Luq8qN5pN65ov77BqiQaY0eR7EAuAFyMqSQAn3lTP6OoVllGCBYrUjAfyqVDYz0yCJDMpPvm39usSFtBIVnUMx-pW0GnDBeCobWVw52KIgdI-PdrIsmDCSnVCnm2rjtwBOWJEOhQ3UCoIRkdl3HzTYVpm1aoLlv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=HdGC-mxli4MtxjFTYgQ8XtuDsw0ODjhZuHylTXykLMQk74m8FaxX3sWVuDXLJ2G__1Jih-LVcpVcbPY56Vs43kJdlNjoioT8miE9VLxxk0ZGN9CbalUgkoac-_GHpgDGR1gPvdbqADkdq7B3WTeoOrGkDtXQ0BDphCyeb0MYAkMJ9IlZ_Aht99mrsa5X238sgVZ6VRj5hKMcfaHOhcgR9q6Qmslidml5t966A7U_BABdO5rPAAx6NwrhMufDlC7o1OR0k1jyzZpSFY7BC1LnL62U16FZFGYjDjACTTa5lF7_ROqmo95JM6u76nG3lJ02enaKLSBo-fveBugmBqI9O2ULRf-jpwnGSnNxxVy6v0DMVTKukp9eE7d1smKQHzJlWsultFVTAau9Xe__5CD_qIwUSl74ODG32j93AQlM8lTJyn6ZFCbzPQPBYHIvbo8BHLEbecWvQvRTfKFD8c80viuNg9lIQPDezb6c3734GJUKSlGcKD27vJjfF5TdjlvYsZhD96hUwd1Luq8qN5pN65ov77BqiQaY0eR7EAuAFyMqSQAn3lTP6OoVllGCBYrUjAfyqVDYz0yCJDMpPvm39usSFtBIVnUMx-pW0GnDBeCobWVw52KIgdI-PdrIsmDCSnVCnm2rjtwBOWJEOhQ3UCoIRkdl3HzTYVpm1aoLlv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به مقر سازمان ملل در نیویورک می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72184" target="_blank">📅 20:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72183">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=oNIsLiszlycqdcB2cKVDlrqR700GXprowOBUDV277om-GF9tjXz4Xj-UuexSH3ZRjMm3SoFUP4nDbL7NFA-fFla5K10gc1B_DbVjUsKgwsXVSB_IMhmH6VThCptp0g7tKTBEdqN-5GwQHasEmlUx8EUQgJ0bGO0hWja4Xgw17gSxHKNeu5r31vfPEaLaKR7cdnSjsKTxfVpwNy8d0q0ay6M13ohEElVv6Ie5aGzTCTYMfHboBcIW_-VDxQhP4FcVI9tglqNJTBjccAJGmA1554Zo09xe9QM6GG7WrI-imxjISHRQMVLXAVH1JSaSEuPtcaVy1WKgF9yaN2x99v5633cuiZdjF2HGKzYzzq0LY_EiNaffca4t1mG4yEPV7vDHwF49N8L2PT4xCUZEJrj60AEJ4aP_-tS9hhzXRdVz9lp-CZWRpK4SATLobIaNIj4ptxiD6n1XGHX5P7GQOyDJaHnvkFE-46904fN-47Y-AAv7ilxwpmdlP3pXSWoAYp4SyHdBLOXBp5rtR6FuKPWHjWl6PwZlOaDgiLvtyl6Afy3esJSk5kfrj-GwxgMhxHje2Ttc066t0A7nD0F59XawtHJF5CpcktPopF03c1gUFP_nSDRzdvVvS2AF0ogsgWJWHWLyywitYtWnLOWgHVEwextmV1UP2xPKpPpCW_gp9wU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=oNIsLiszlycqdcB2cKVDlrqR700GXprowOBUDV277om-GF9tjXz4Xj-UuexSH3ZRjMm3SoFUP4nDbL7NFA-fFla5K10gc1B_DbVjUsKgwsXVSB_IMhmH6VThCptp0g7tKTBEdqN-5GwQHasEmlUx8EUQgJ0bGO0hWja4Xgw17gSxHKNeu5r31vfPEaLaKR7cdnSjsKTxfVpwNy8d0q0ay6M13ohEElVv6Ie5aGzTCTYMfHboBcIW_-VDxQhP4FcVI9tglqNJTBjccAJGmA1554Zo09xe9QM6GG7WrI-imxjISHRQMVLXAVH1JSaSEuPtcaVy1WKgF9yaN2x99v5633cuiZdjF2HGKzYzzq0LY_EiNaffca4t1mG4yEPV7vDHwF49N8L2PT4xCUZEJrj60AEJ4aP_-tS9hhzXRdVz9lp-CZWRpK4SATLobIaNIj4ptxiD6n1XGHX5P7GQOyDJaHnvkFE-46904fN-47Y-AAv7ilxwpmdlP3pXSWoAYp4SyHdBLOXBp5rtR6FuKPWHjWl6PwZlOaDgiLvtyl6Afy3esJSk5kfrj-GwxgMhxHje2Ttc066t0A7nD0F59XawtHJF5CpcktPopF03c1gUFP_nSDRzdvVvS2AF0ogsgWJWHWLyywitYtWnLOWgHVEwextmV1UP2xPKpPpCW_gp9wU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز یک بمب‌افکن رادارگریز B-2 و چهار جنگنده F-35 Lightning II بر فراز کاخ سفید در جریان سفر رئیس‌جمهور شی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72183" target="_blank">📅 18:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72182">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D9TtZ9R5LBWKWDjKIpkl_bwjIOEjy8LcAoB5cYYPPUoUr_HN3WQ8CCpbi8vgORRiBNjsN3Tlf9r9s3rnKbMOllsyDKnLjE-0Jmivce-vI_8tHknqie0Ks8bld99WjY5mG4z50ZlwE8qRy1_i_sr2-NayVx2IQ7F_HhEuZhePkkHRk-zJDxvj-HEmdPygvTb2q-cUOlIoW-LcY9goOMsym9VRN8H4bgY8HlAjKZ4-2P_lGZmQHk0xPAXHraGo9AIbG_RbDNoLZ1ApJp1C-yU7fqNpEEcH5QjfZoKnOlGvAbtevQS1AFQe6QjWNDhN14XlI9d8DgmFRD_rnxOipJMmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز گزارش داده است که نزدیک به شش میلیون بشکه نفت خام توقیف‌ شده ایران به ارزش حدود (600 میلیون دلار) در حال عبور از اقیانوس اطلس به سمت خاک آمریکا است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72182" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72181">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrGHC2ufYCujZgIWocmXPWzyfOsV4op3QN35EcgFpCP2zUU7hz7vIH7Rvyuz9mxpQfi5xKmNfEx1qACGGH_WCmCnEeKULZdzed3jT87bs92bE86BOZXZXwRhe3SslXg6685IesXsAXuHJq5qB-WDcdmv0pepQ2uSz9TyE9JcUHeRDceMnEtUFzQv3EjeOK29Hn04D-qkWI6dPnwzb_-Z8PHr3Uk2qzfnTGpzYgwUf9FBY8L22-uboOLfovHUzYm9ULhxlyGOnyA-6SYIkpUa6tHLB9YPKmF8In9ShAxmYO9K1FfJ5HNU--0IFJMZ9mvX6BfRSqstT1tLw2yCjWVxn14Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrGHC2ufYCujZgIWocmXPWzyfOsV4op3QN35EcgFpCP2zUU7hz7vIH7Rvyuz9mxpQfi5xKmNfEx1qACGGH_WCmCnEeKULZdzed3jT87bs92bE86BOZXZXwRhe3SslXg6685IesXsAXuHJq5qB-WDcdmv0pepQ2uSz9TyE9JcUHeRDceMnEtUFzQv3EjeOK29Hn04D-qkWI6dPnwzb_-Z8PHr3Uk2qzfnTGpzYgwUf9FBY8L22-uboOLfovHUzYm9ULhxlyGOnyA-6SYIkpUa6tHLB9YPKmF8In9ShAxmYO9K1FfJ5HNU--0IFJMZ9mvX6BfRSqstT1tLw2yCjWVxn14Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از شی جین‌پینگ در کاخ سفید استقبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72181" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72180">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72180" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72179">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwaTUJxgFrJ_652FnjDCzgxMe060c3qO5xKzIUJ5hxBm5spn48Hgce76Jp9Ekg1mK7Wnr4hplHtvJfWPps4ezEkq2EsILSqlV4YktaVDI9yVBiTUNp5VBH7gP8gKFG4ay7PtYCE5gomt70m4A7d0x78Dxbl9SyUQ96WrG5D8gVaq0cuSUc4qextz8XW4xSzg0nPpV59rzQMlOFcXUHZwymI-XsanlFKIlr78TyBMEAsHmbSmZeK-WgPnPZXoav4kWq9s94T23gbCcAJyGAcbkuUGyOE1vuvS2PW5mJbjIKDEPIfF9As2VHhs_DWwBXFbzXPGxXt1UKYNfr9PkyN1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72179" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72178">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEq05Rega_mwk3kkGwDkGVj9oTcPwY6qZyTuptouRV_r5fYDl3mV9p4bJ76h5-jwdFdJ3eRSVKgH5WDwdcLj1KJSoAdZOcX0lc5oSsrBWk3chAh5hPOcn4TLLZr4eY93ossR2k_nvcFliCDsiEbzRv9RLzwRbP9DTr6J_wqsrMvQaOf7WTdIcC4fsukhTTGZGB7xJ2mMKGG3q6U-w7x3nbrUsC9XCgHcXPlvEkhRAzHoX0zJYMagZEmlcxbL_xuZjBsHpbUoYnKaJ_O62F9821ILrG-VzlEB8TeCWPF4lH3S3w2MUsoMaqB5X2sdoteBMBWGdrzqquoz8yoFCHhIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو برای شرکت در مجمع عمومی سازمان ملل وارد آمریکا شده است.
او قرار است امروز در نیویورک سخنرانی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72178" target="_blank">📅 17:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72175">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0oVuE7bInVfMngJer6Nj44i1Vine4mLuOnmaNOEWOghmDwFWRj4RwZmnX2FI9jiBvbcRrW-H1u-aSw6t2LAZjXuEH25V_hYUI2irnOgtFO-abpIP0SL_Hf8_dLWiuyIoSL_APpLXU1iYjQgQNM3BIPQlRmVNKtILSgBlJRxr2gat5XN_ni9lLgdJ8N9arZJgW5V0YAWe1FGEfu1es9-GPYQkJAt8mCfYu4dM9TArlzS1CRPxdX30YmV_ECFCqJi7ttMtXsY73zwXeX6chM9WlVk0Tt4N7h7p8G6IrTh9t6uX8M6Ft85A9uCasKlruSkSOjWh7ZEF96uYLS6F0UxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8FxmGIj1x0wgUEm37eSOevNA8ADERWNJeKokh8L53-zlgHSH5DSq2MP588Hvr6XHSXQwmGMHDTil59NJo3RBekpDT69VOEkj5mGRnRhDqF55VWGkxd5KDy8ZYZSVSNTGf4Jg1Y28HQ4mt7ef96SfN8tB1TjEL9Gjvmt7LP9yat59oI5WMDLteTwKiiQ7bYlHUknYjAcCSQKFz33WLMmfcPSYpa1wWqO5t2Y8TnvoxlOh1rLbaQdoZkd9cf1ECGkaXTysGr9CnUfJ5OB5uaecxbsYJHnA94fBP6qq0p5KlliRLiEOTbqAmA3KcScXpZhf5zHoZiikV7P58dOclSpXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=s1PoiEVcUhwx5ofrNBqJuWiLcy_bKszRajPao6eAbYp761Lgu2qlnjPpCQGeM83EBPCqhPxd5c_kgJGJrVGYk7IozYepOfo0hjYjHnxydZVVaezQOTvuuVmPgOZfN8XNAkN80LTfS6IAMojMZBq2cyyDFOpiZd5ph0FisfATHAqTfnmLbELsQ5TXYLWQ57iJzKPhNaBBPaqepIh1ISC_ixT_2PU5TT6CXmdUWkC4ovTCG11KcZxvZZ8_MZZRo8yjWeMHKzjTRvDE7dq7oSIERGYE_en3CYwX7nA2Mpb0Sg9f94PBgtYTfAr1IAjbKwpsCJEM9rrh08kDsoKt6Xq6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=s1PoiEVcUhwx5ofrNBqJuWiLcy_bKszRajPao6eAbYp761Lgu2qlnjPpCQGeM83EBPCqhPxd5c_kgJGJrVGYk7IozYepOfo0hjYjHnxydZVVaezQOTvuuVmPgOZfN8XNAkN80LTfS6IAMojMZBq2cyyDFOpiZd5ph0FisfATHAqTfnmLbELsQ5TXYLWQ57iJzKPhNaBBPaqepIh1ISC_ixT_2PU5TT6CXmdUWkC4ovTCG11KcZxvZZ8_MZZRo8yjWeMHKzjTRvDE7dq7oSIERGYE_en3CYwX7nA2Mpb0Sg9f94PBgtYTfAr1IAjbKwpsCJEM9rrh08kDsoKt6Xq6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل منطقه «کفر تبنیت» در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72175" target="_blank">📅 16:57 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
