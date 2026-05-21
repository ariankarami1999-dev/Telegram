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
<img src="https://cdn4.telesco.pe/file/Bqts-PwZnxJ9QlbJ67L8oIDIo2vRmJD05MP6hwYgUE37HQAyNQ2j4wUIg2bPK78xgIBooHyrV0UBcjLMEq99moXcP2574sWykJ-4Q5XHmWjU1bWsqZskCbSEpGZRVd_L5je93S5pbfg49b-SDxoy6yilrCBqChw-EUjeSAUFIeWTb6AdR9ViNyTQy8qHd9ImhN-M3EJ1IAUZ0M0Ri8PTEAaxMcbOJRUkYwpRBHH8rIEFQGrn1UUa9Y_wnwEm1K2hVB2af_vhSIjOE4oUczZxmozppS7UZe0F1xOHZ8FeHK12aflg5pAowqTyEPitzDX8W-J-d8TkN5VOYevgC-TZZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 10:14:44</div>
<hr>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=M2XJ-CFxXvdTufFAOfQYhlRxHmFxut-mysbLd5z6bYEi3YvmypNJJei2F4uGwJsmA2mpQZOYy2xyYGkZcLCEHsR7nK6i9GTqfSuS6qfYWFLaUOQAQwqTd5jAbPz-R5NvhsyNv6jKu6YjX-rA_tUsnLYKVu5BbQhldk3rWDLmOa6iH5F1D4I30GdNdCLKgaZfEChxNQvnB4mR0QeXqyx8sMT367j_wlftvsEjnFm3eCdTCjf9SIY8k8KbkDbtRdAdrZgrTcxnKXYCSoGYP56LhJCkU2l1WTeCQvRswoWmbqw-9f0w0Y-YCSjjXpHhSpKlPfbIA0FYPjDrSaJCFXZ2EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=M2XJ-CFxXvdTufFAOfQYhlRxHmFxut-mysbLd5z6bYEi3YvmypNJJei2F4uGwJsmA2mpQZOYy2xyYGkZcLCEHsR7nK6i9GTqfSuS6qfYWFLaUOQAQwqTd5jAbPz-R5NvhsyNv6jKu6YjX-rA_tUsnLYKVu5BbQhldk3rWDLmOa6iH5F1D4I30GdNdCLKgaZfEChxNQvnB4mR0QeXqyx8sMT367j_wlftvsEjnFm3eCdTCjf9SIY8k8KbkDbtRdAdrZgrTcxnKXYCSoGYP56LhJCkU2l1WTeCQvRswoWmbqw-9f0w0Y-YCSjjXpHhSpKlPfbIA0FYPjDrSaJCFXZ2EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rkskz-j4x3cRiKbTbaJyCtRUeRPGIeCeNrQ1Obnz3JVvkXpUbNkI-T_R59PmwohAwW5eYJbiy1bEhhkfbZJwEZmIY0eHhUV1Fl2YD1dGh8C9BaFABG3iSziU8k1Yergh8d7oz-ugdwsMuEKdX0dfpEmeBi69Xns-aLDMcr8rbK215B91_aO7ZnmewjYbTWqdcgYtC5_fHgWrXyeJ04hA2GQOtrKWRfr3KV66MKqygqKiwXjlCaVQNAaO07lw_VlgR3vzlyEL2sH59Ypqr6HfC9VULLxSSmaTeHhIOASjallhQ-DGZ53QgqyPECJkptIKXYoJfHFWmcELkYbdwPT0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=X-bE8Z5NK5ymRfbSigJSVBH_gDHuCOxbOe5tq8NsUjYBzdOjnjiboN5PEU-3xEJ6yT-E90mdVJc0JwOesTunZTPr-JUQpgcX8PEPEgQ75kjde2tN6EDH6B2rv2mbZ0nPSvS9goK20qiatn2-5W74BZhfizUQtFl3hytv037yzH4HZoAFt4tWuOk65qYesL8vnsRx8L-9ciHYf6tPtrvojHZSVAoN8d4pshxbW3L1rOUYwcNIELq1BW-YeZm6ENjAAG_rU-ANUSS46RXMM4xmmw-CwFZ4T1DLqAM2Ripvn-NkmvrWw9KFrQ-cEZwBbAWxDj53OeCP5ntJxz_Iwc1Q2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=X-bE8Z5NK5ymRfbSigJSVBH_gDHuCOxbOe5tq8NsUjYBzdOjnjiboN5PEU-3xEJ6yT-E90mdVJc0JwOesTunZTPr-JUQpgcX8PEPEgQ75kjde2tN6EDH6B2rv2mbZ0nPSvS9goK20qiatn2-5W74BZhfizUQtFl3hytv037yzH4HZoAFt4tWuOk65qYesL8vnsRx8L-9ciHYf6tPtrvojHZSVAoN8d4pshxbW3L1rOUYwcNIELq1BW-YeZm6ENjAAG_rU-ANUSS46RXMM4xmmw-CwFZ4T1DLqAM2Ripvn-NkmvrWw9KFrQ-cEZwBbAWxDj53OeCP5ntJxz_Iwc1Q2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=hE6U-cWVPxbSljVXkGPnAusHXe-NsIGjfyHO3kbNk5q8PqmasMPkwq2yuoqYcmbdxUeS9V6q3aj756bchTN-xWS52CkZWyz6LhD4a9FxdA5KnPDFCefKPCxHEybA4KKXGX0PsybxUowE_sN3LCZIPOKVMPcW7rIW92N8GRUipJlGZe-Q8DDQ9OuKmYy1L2o2biR0DkZJJWyLUFGaberYjeIRlK4mB_mAUimJR6-mOqwxyQfD13UjhtQP-ieIh9vW_-DOc8lpe2lZs_hxv3bZ31ZGtmHuQDxGxcJl0PKu_yft5ebatlLLpUKnpYSrKFRI3i1W2sn42okQhSrgh-ig1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=hE6U-cWVPxbSljVXkGPnAusHXe-NsIGjfyHO3kbNk5q8PqmasMPkwq2yuoqYcmbdxUeS9V6q3aj756bchTN-xWS52CkZWyz6LhD4a9FxdA5KnPDFCefKPCxHEybA4KKXGX0PsybxUowE_sN3LCZIPOKVMPcW7rIW92N8GRUipJlGZe-Q8DDQ9OuKmYy1L2o2biR0DkZJJWyLUFGaberYjeIRlK4mB_mAUimJR6-mOqwxyQfD13UjhtQP-ieIh9vW_-DOc8lpe2lZs_hxv3bZ31ZGtmHuQDxGxcJl0PKu_yft5ebatlLLpUKnpYSrKFRI3i1W2sn42okQhSrgh-ig1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkVkzyC_uRz7k4O9z7HFCLYPdU8GRwMxGMq71CuV2Mq1FMMpneLMpqm8pIJ5rFeugE5Y0RsPBuGr1EtR8Pto9BDB18r4lStNGhDuOcklYiI7qVnEQ5BG7XXFcUabOdYK1z625KXo-jabWy0VpSUxfqC8asJtthCwWRDYQSVBwZ8CxfAQlnYwkxFu5aamDZzgy3B6425krwk9waSE9b0C4euubzDrRPbNM8YobE_-gH-r9Lrb2cENUfyHB6oOrSxt2ZIl_ajYKyTN_XlYGzQUsGA9pC4s8PI1zoyLfzfVceSyn0z1T2K_wwu91lGBUuKjXZzgzOw46gj9iplJp187Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE2fAIBXlERRIxNP_ypVuEEMAophK4T00pmS5UhHJ5SWaAQkEf5PnCf9I_JaSvom7uNgagvUUFe0vyHTYylmaigLYTLSEd38cuvXzzMbOy27wFXhVzT-dsjSXGONvViacKZwoZs9NkwRPTcqppoP4aZ-hqZiKBlDWJgBa-TOFYU84625e2YgtD3NS0s0gq1COFfDln7175bUGvjPxLdFI7-rxjcPD8r0DD0eGGuaQNxgf-dO8XkEJ9CsCmc-OhD5VS4Qo9b6p_okRtYYOfhub1Cy77PFQskboIuInms8Iic-wYv58ywA0a9gQlypYRZTvJ8XB5DlOMq-L6X0gEPltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPCc1yKpVOmap01bOdccSEt0yVfbg1tALUPbROUeOmpgJpCH2yF5kKdEmyyYfztD5Hw0XTP-fEnfePF0Ryj0PW5bEVRVawaHa6p725-mKVaL4zsE3f50WVMHhVhYgba-RrgclWsSRTf0e6Z3My2242Ro3wRbnuKDZUrOO8Lpmw3M6Lip2Fqkpano79cCl0oERfEN4G-QA_CDL_N9F7qItHNH6BlIDJigN_3m8J8-lFWEHU1UG7IQ7wSFPPmYA-BDFk2Fy9SpVW2_Upodk8SSZGv08GKA1gpQv6PacEm42q04TGaJFxeh0xt1t2W1fUKg-5b_q3BMwfQaxFLSxGDTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNl5Tfjqilj9PGtk6OD44yOZJq9-PfqplTRmvWxnTsZnkNc4hS--vT87v8cXMNRvFzDMaHORt2kUBPQLoSimcl2D8pupwiq0dHeGAJFbU4xszlQbfSXvGK2TIbV5PL1p3JmS3yJP57vDYo8NIkEM_e3e_gTmfOAJDczEqlagAnmpLypKQPPnJYeoTdg3NYw7UUU3V71srp2dONY-VOZlZBFpaCLnzoKFg2ORT3rL1S_Pg3_obdTI7PH6-GeHIhmtMWErqarfNr9UnD5jPR2ynKY8XH9HmDT6ogScqql45DIFv79x9wFD9JsY_vVPMPCAzj4e8pQviUmiJqQKOyU5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voSaj_XHIKxwXKJbpoqlkKABMHIp7dUoXyL8KEI_vpZ4w4BpVZc6NvGGQTiDM4pOq_8klvDzdOffnjzhThlDdrHMVEeBh7j-901QCtUarQzF3iSoox56DYltIOa4Zg168N9i9XPGDzBKFKvybYzq1Tw4WO9hqlV58r1h8jzFCILh1H_S49k_-mXffavVNqk3jUr7IgZ5s50QdPhxmKOz2tD7DPsVO17VxhBoroh54q8zqNnsjaEgkxlGCsnjxtH3UbrE2o8_3sCfwJjf6EBW0aYfX1J74eBh7z220UNwwdsj9z6Tjkqr4ajB3OfRBGP5ECcmp2GY3eiHfgaJmpvCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBgQrmWL3dcjgPvunfJESUJBXHAWC4jgyE66VH9xWa4zkH11tw5le-8zIn0zRiANKjGOZw5b-4GK5UaozjcDNlHQLALXSm_364AG_MZS8iUDyrhN-wE1cFR0USzBZn73eRDtBwcNX0zc2_s7b5GhuET3uGe9wO-8TBAMO4-03fZKtTdNMyInlmdkhUZ89XhsKOK7O_lhKJ7Y0pviQXLiDFIPejgfxo2YM16M-esEKJoC3RcpQOGqw0JaadyFmu1aLOIaahpPjLV-5ienWwSspI9ywTcAcjnBq9Y8pkllh0nhi7u6lI5igHhoe0CmunkPo-Bm0unCeoOTqMianM3EgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRBplwyQa4mkRVszeIGTApQA6mpApsl2BMLEJgFmPqzbHFTVDu0yYEc2PuU4-0buJ1ZA_u2XvUxF7gKkK_tBBdhjFySn2Cvrk_8dW2Uj7vv_cLTUlHsIVa_5UtEJok6OB-KWF2SOFig8f9ZS2VWmlhwC-TuO6dd0HiNaJczGqoyo0Wjq3C89zI0zl3YfrvqwpajDSO2KuLYsJGgioUlwk0IeWKpL2eAizaSepkhqtpnWDnuRGY1E3k6o-wNXMtiQgUVbsVtBGBYZGDLEGw7K83ezsIzqU8VjWGIRH9DogeLZ40bTpJRAGkx37SJLhAPK4Q4VQMizmUxHkGuESPdgUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=FPvQM9Ppfg8VpWgpcxPvAAD2G3OFSxx-zyQ866n_kH8zxuemggj6hZ-8pgEWr40VYJYhN9QzajxAh5Y0boawiEnFJCahfHod782iniN6Bphl72mxvT2kkge9ZF3FALgYHosbR3P3wZx1kvXR19a6E9ljXJwrQKAI6oVKnScCtJ03hBZ1RreDQz8k16QT4UAfro-SR5vSOynqf56bFUdnrfYYUgI-83cgiu9wgvuM7D84u7SMvSi_VtFlI7vzioJrOssCxGK0Agg93mYeGHRcNQfcNK4raIyrGaHbxl9Mi9gw9jnevR4TsFPp-kNmRkAroAW3QMzo3CS_r0Zu4Dx2tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=FPvQM9Ppfg8VpWgpcxPvAAD2G3OFSxx-zyQ866n_kH8zxuemggj6hZ-8pgEWr40VYJYhN9QzajxAh5Y0boawiEnFJCahfHod782iniN6Bphl72mxvT2kkge9ZF3FALgYHosbR3P3wZx1kvXR19a6E9ljXJwrQKAI6oVKnScCtJ03hBZ1RreDQz8k16QT4UAfro-SR5vSOynqf56bFUdnrfYYUgI-83cgiu9wgvuM7D84u7SMvSi_VtFlI7vzioJrOssCxGK0Agg93mYeGHRcNQfcNK4raIyrGaHbxl9Mi9gw9jnevR4TsFPp-kNmRkAroAW3QMzo3CS_r0Zu4Dx2tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEW1hzSVrainpPjRISZkwfBFxw1gtgmKEGpM8qPB2OUj1KF15suiMrvzuw8QPaw3t0GL78txQXSd7FElNJMsbtKLNVkHl9BUsowfd2krJne5WMVzdYiY5e5delR-lowIK5ZNSrj5N_ho6I9ephK4X5MxV38F9Si7-FqeSqngB30JG6GFmANsLJa-4z9pT_K0QK5uy2Qd643igKn4skCYWKM9GDuDedqSzTnzRwf53Uy6uKq3NcnecEEsZD8PcI2xFmZUDI5WGksNghi1gJmzphVvF5Uee44MDqRYF5TdmQdLH60m4_7l2RRddyvTzS2bMYG0y1C8ZEMY9dIFKbf5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEIzza4_9lXqdHUmQAK29B72M_ohaGg_yeype30dn_JTt3ZcpJUtN3NXYFeCeLx63N3sWsj5-fwD-fyfATyVrO2F4OBUC33T_q4jkpXtP4tOtymQEIiNUdHjKaC-cwYPebZumgmz8XEdsvmwQamHNx-ED5xh16g-cSRFh2N6M6C57chn7J7iQf5nKew8NWzxedQ3Mu8CHw4VaJdnfkGf9sBHonhFOHzwOS_eo0qSjbknSynBnKSOFQjerW82M4zZ75odeBvUTq17JEq2717f9_AbTx9Gn92cqvOszTrNET8sFjS1ugnxdBPmCewOYH4_F4jL_k6p7SA_mgA__OkUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS02juw4EyFNCWKPCl6Pbi6GLO0L3O4kxClw2c78wCfMHe6O49fnHy-VEiYr1U6sXq7TedmZRFcsN-zKrp7_rrSD_CNZbNF--UZTnxJ1CNlrDL0g-FGGjsTG5sBWyYhx_qJL7ZfZJDSpJ0Pt0OWSQwPggbU9ikHdlrPj9uVQso07iyca7x2pnRGF0kplxBIQmrtbknaWFfCxiA1Hpsy6uDks2h1Oe9Ti6FyrLUmxnuMwFwlovsLo11MK_38LoEs8n6Ph6fxRRmJXu4vNVBgQado5-1uMyNryMCnzYtfrkDuHt4RyLIaKg_txKPTNorrQEVuZlAh6xsdqNkZ47mDOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOVeiGFVYU40yZdlVYjO01eW-e1_rW_V8jsO0tj7wDLYbYolH7lecK1Qrexm-qnJ9yLG4wlhGb765j9SSQW4ZEdqsSNN0-2qkc2ztTPjsW_PUG--rKLIx1ZL3s6BkHwG6JPvNwZ997Q0LhSZ0gj3fTpMpl0DUjSDFC4mdHA8DYpt6HDlWVEyGVHMhe-nukkSI8YwasUP0n0cZWdbI8ziwQdVgOJzpo5Gp5zUp0DTRfvjtwUL1qZZkJ3ZgVV7jsadA-Cp4u71bY6wqXBoIKS-UZmLEUHiMyzxqudt6Oz23SRmR91TqMq0nwEh-4eZHGfYW0OI1ygucUJ6dA79Qv5Fyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=SV4k64h-WansMo9TZOu-lXWKDMCwxuGZ0xkYX41z-Tqr5XHHAkRdDuCahQf0un0hUNq2tNxKFHe9K8f5PDEkHzhh-sVU6L_OmPP2DSDT0LMJrXX6JZkVGkclzdcHRZHzdugP9JAR-CCDG5nE3euwqHJr32Ey4Nd33AxvjUyc4ZoGKzcOVQIIzQWQesCD4VnVfptIR9EP8W8E9xgBt29RCbKyubPsBrtD3nPjnriJh3uAmIlZvEw_ANh7PfJiElnr4ubosQEvFS8F7ydZa-r_gHaHtt3Kaf65LGS_3DD1mMY3kbn-HPrxhX4QiVofyCDRKq1i8gJDcglkHL-HmHa9pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=SV4k64h-WansMo9TZOu-lXWKDMCwxuGZ0xkYX41z-Tqr5XHHAkRdDuCahQf0un0hUNq2tNxKFHe9K8f5PDEkHzhh-sVU6L_OmPP2DSDT0LMJrXX6JZkVGkclzdcHRZHzdugP9JAR-CCDG5nE3euwqHJr32Ey4Nd33AxvjUyc4ZoGKzcOVQIIzQWQesCD4VnVfptIR9EP8W8E9xgBt29RCbKyubPsBrtD3nPjnriJh3uAmIlZvEw_ANh7PfJiElnr4ubosQEvFS8F7ydZa-r_gHaHtt3Kaf65LGS_3DD1mMY3kbn-HPrxhX4QiVofyCDRKq1i8gJDcglkHL-HmHa9pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgwsCo5_ALNtpdJGfriHJaJ_AmvGMAKeBN1eR5ouDjFt-YNe97Zqv_FFpc7tkSDaVf-SNan_ex2jYzzXGLjiRNrOmfBHpRXQJNKu2E8zQAa63BSgOODR9c9_e8FVWM1HYQWmXck2pn474Zb3HnDFzZctiplkhTkVJSLhsjJan3zvXAKQiItONWlE_KfzVy0eKGy2jWX55HAWoqv3G8gynkOZCcqAWbBcdT2tvmDbFp38hPDl9SyLdEHKeUGe_KZNNqk6jvW5e0vqIfOpqgPmP_q7NJl_qmo5kfic6ehEH0mxYtk8i5_VZfmhMlTmmE-0E3jfUV_uGeAR_BEoM_kiBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYIL-c0G2IN5nMqgvuktU_0eDqNZ-LlWiR2qpJkjs-8drMNnG6BMe9MH4iQTlXhk-mDeZuZjHVyIMQtEgzSYg8aUT_EafXeE-9GefqZQ8Jdf8kIiz5teFk4livqRV4G-WktjJIV7BFPMJ1G1xm-r_v45zw4lc_8FWeJKKAl19D_x5JTosWLEtV01roX-SQsy0JEtofhqgZgq4r6gugQaoU5bJ7xCRDCdYmhfeqsY7dwwSqjcDuc0rVpxx-5Q57QSeBi1mLcJ3Vh7wgNctE1Cc7LgE5bR1RhHqTorsbPI-8rmG9qXo11U500jeRDCkT3Y6AyiIpUy0wm4J5kGXfnz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV9lR1nyMhMrSONneS-w1iqnAXw1Bc2yt8d5VcwqYMezZav2XMFRyM_lx7uPZLC8HB8ymomMVA0F2HniwmV43J4ffkyIWTVp2GVMMpKiqMBqKQVimUoe_vgJIrDrORsYOyBSEuHTAtGJL927nqQWkNhaTuMU9hvnC3zAGwsS2C9rUDryaLlJ8Ey8IW0ifTOR4HFTAQEnz94rUo0vybqizdx_yOxFyDexAgYHnNTQvLTT_1A0jZY-3T5618cNr7-xa_yz0QJifexHILiT0ouSi8-LZ5H1V2W92D1cBtpqZHp2ajjrd7bumvUa6lChv4oTVbXrfZi-TcTTyaK6HtupeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USdMiBqtxv1o2devQUgOAspG-om6YBYkkOeLo_p6EU4741FHtsytr2NTjqtkcYgyPrjeRJQ4h-SLvI00giO5ecvgnK38v6LR7ivWzm9Yaeg1X-og0U61mcJOYUD1IGmjZbiAEsz7tE4Ea7X7wdJ8fpcPR5jbJuW8qrl8B-7dl7GB98sFC9qA7ha-lYDwfOuVf7eW2l10QOJHTADxqjis0hGWOzdAR2DFll_KifCzNTw4mv6IubGVc3yRV6hauj2am-wgoHzuZPZfob5pGNcK0_gGnGsuFoKHqH96lJL_iVRXktprah9VTto1E6oiN8te9PlOinZ724z28oglKpb24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcxOPGajLacLKLHhrZaIBQTV-DNtm3R6yDgzKSAsOmelGsiQ5nfDEWwq51zoHYCOMCcQ4EUTlid2CFiqQJ__6PMdK59sHUL7oJcvEK2OROew_hB7tCMmYYMQgmc2V8MpNS7lUD6Qd1On8jzkyrDaBSaj-X2dfKRqlCFFIGp_Z9RAOyGZodv1lzdz48yp5DytOImTKapVA5pAXw8PYwmGZAUvMnzjLXMEmxOMXByncOhhRrib62Tu92_zPUv9izlMfNCQpKBPmemD8hjORsST3v3a5hGkhBLAZPLGwL3g3kdObfA8n_lsCPUlXo84wYQVNkcq9Tfi6TNKssmzRebl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=GnUOoKBP8t1XdQsQ45T_oHA_EI3GP8aZ_wQe3Yqw28YrlLsMcwhLwShdM8URJhcTumaEv-SI0aY-2AC3S_3PNPjsOe7DnHXpU9_F1GyzF01rhTg6XvPCbU9KOThjDLXmT6Ok6HTi75rvR5DlSBxy-_lmPT-XW_piKVXHkpn_ygvGp9WeDzwqiNabumUyMmdkKdLA6J03tLEjRwOErYn9vNGXS7KglNS8gnZMovy8W5MYtfVmbPajSwYFDZTzoGk59e-Sgz3sbV2TR1lcKzxjBbpmoEaJ1BcGla8LmaZmXy6sOMndD2c-jlz6dyFQ3iG0zqtTFkvXdhBqaPySwEANeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=GnUOoKBP8t1XdQsQ45T_oHA_EI3GP8aZ_wQe3Yqw28YrlLsMcwhLwShdM8URJhcTumaEv-SI0aY-2AC3S_3PNPjsOe7DnHXpU9_F1GyzF01rhTg6XvPCbU9KOThjDLXmT6Ok6HTi75rvR5DlSBxy-_lmPT-XW_piKVXHkpn_ygvGp9WeDzwqiNabumUyMmdkKdLA6J03tLEjRwOErYn9vNGXS7KglNS8gnZMovy8W5MYtfVmbPajSwYFDZTzoGk59e-Sgz3sbV2TR1lcKzxjBbpmoEaJ1BcGla8LmaZmXy6sOMndD2c-jlz6dyFQ3iG0zqtTFkvXdhBqaPySwEANeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=aqCJCBd4D50QvzJgDC_uoGj-D6PTP-KAz31DEAWcOluvJKyzxyFBuTlZJQpYBkKioUm0EkRQi0Hn84p_O4wHm3CsPNjv6YtH65lwYGwIo2jyj2DKbQX8yRy9bbNqVESyLPG0s07u9g-9Djn2wTwURtrYAYe7VmC8W7shRJY2qkDk0E4GEK6fyS8Sb7jOOuWYPac513x41PyIRj_PBHAmV08VFu29ELU9pM8aKJdKQX0FCX4ihlYENkL5gdaEizcGE_ZpL7_tN_7E9i2u9ZD53uggj30Bu68L22DVBuQkyalgswqALr7IO85i7ql8DOjM2GvizADy1RxpKr-lOj5WCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=aqCJCBd4D50QvzJgDC_uoGj-D6PTP-KAz31DEAWcOluvJKyzxyFBuTlZJQpYBkKioUm0EkRQi0Hn84p_O4wHm3CsPNjv6YtH65lwYGwIo2jyj2DKbQX8yRy9bbNqVESyLPG0s07u9g-9Djn2wTwURtrYAYe7VmC8W7shRJY2qkDk0E4GEK6fyS8Sb7jOOuWYPac513x41PyIRj_PBHAmV08VFu29ELU9pM8aKJdKQX0FCX4ihlYENkL5gdaEizcGE_ZpL7_tN_7E9i2u9ZD53uggj30Bu68L22DVBuQkyalgswqALr7IO85i7ql8DOjM2GvizADy1RxpKr-lOj5WCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHmt5hDPTgASZ9BQex1RCSp8qTm6kOSr3ACYyoz0B2ZG5gVri8zRhvnzhNRUfY-0Vaz7hr9AMLbSt5GNosAaLXoeR_I23XC3kTjFZYpq4hyvF1ecC8_7uXpCtNuPMzjbue5XH1SBNerONXK7eXhx7HcaX3Iyp1TDI4IUHiY35Y4c_op3heK_2MoETGsWyXNViNbA4J0DTVqVEmU-zejFuurxTqTQlvrsejHuouAPA5hVel0VGZcyjoQOg_cczMjc74HXiShsa055azVsVUEYzqI3YAnykheiGStBg27LqKDDoodqkvSg8-zyxdqCFXTuaJ4D4IT_T__BzQQYOhwWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBptXuR_BkBQb7brsehX44FTGaaBJOEWXCeRI187KwAMKB2ymjqy-sS3FbGGNAkZxDVWjbC3KbWZwYM2_gZorpZsreLKCp79_kdEbr7zwZWCrp-mf9FlaydgXtAxA1Vf8RLTigHVESzzBio27l7RAfttQsFEwoTLXkZfqEyjo_ZogOh5vDwv1PcRU8ldupFOIgCmWvp6hlDg3Xc_qpgAD2zLuyIXZ7yiOqL0HDE7ftIyDqbUTLVc-lgn0HEpwyemn3y1iLAM0wWh1B89Lk5uGrG3C3EbeJmNHKLo-aEmiXthvi8aO-zD8lgrcd91PXm1gy41Tzm7j3p1-pzlVj8dmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X971e5ynR_cJ8u4nr0Xe0qArhYTKh6TI--eKg1kZOPZiy8eskv_HBr-p57xFIdd09YKlIowx0FmxbO0Nn2eqORfFZ6hfpExL4UMwQ_HBm0SIlQhd59Cgan96Rms0bW_ldCvON9dQlRIyEBqz62uXioz61l_UB5egnH5erUee0yAFHahgtJMNCSYvjD7TAAMv806UcwvCHXh-xuSRlBZOIxKOCggZWAzhtKnXAzPHJFK11FgBUK-YwRcq53FyJsK522T4ijl_eihgWU4K38Gp7yWMCrY5S6h1MGh8RzaWw-EcBGRS_xTNY190MBCjm_oNz3Q5msRrciQBSNJ7JbRxBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gsy8VktP25ctQX1eaF2OdAJCJ7Nr2r5zc8_ovoOWEv4C9nyuY1lviiwRK_mY_5S88vay5I7MHNGY_UWwuUwl6ykyCyKK3YlkZVJuDMlGQEzR4CYm-qKmbn3Oy44JPL7NKTqJKxp1FxjRLTvrqQLEPbxurBZ5PU5taZFdOZVyN-X24D3rWABpw7AtIa11nk9G0MWFwCF2TyunQ3Jb4ndcApsDf_gHFJ23w1vcr-nYZ6J-JMjo0OuDlXhBCOr3Txl6uBGGJXLOz2ct4qPVR7nhkE0c85DJTiJ7EmUOBB8ZsdVg_CvrnuZ0tNbDg-YyBebdfEZN5I0XaovYpG5CdEKkHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=UZrg1Zqbcjkqiy9x5qKsckkPwc7wa-EHK279B5ofW8coN899unk1XzkSge3kOO3yelRpg8m5Kny-Kr_KqEVPjsZixksZNCBc3Droy5rKgTWIt2bgObbOhbZxmY1NL5CowYuWS0TMIFm3Tg1_R6p2Q2156hW9ZUZEjOHDaAz8Hr_3DlAbxAlLmRPo_X5TgkPj7Ck4kwaM_k7cxOsR0gEns70rjobaopgGDZ55dLdgua9xcysb7PqR6XrtJOoHlUKYjYcA6JxeeOqkN-2qCHJUQOxwzI5sjsEaPjAIkrnp1mwm6vEek6VuhTYVIZcb9IvizUjOLjtOBbDKuCYEqWEZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=UZrg1Zqbcjkqiy9x5qKsckkPwc7wa-EHK279B5ofW8coN899unk1XzkSge3kOO3yelRpg8m5Kny-Kr_KqEVPjsZixksZNCBc3Droy5rKgTWIt2bgObbOhbZxmY1NL5CowYuWS0TMIFm3Tg1_R6p2Q2156hW9ZUZEjOHDaAz8Hr_3DlAbxAlLmRPo_X5TgkPj7Ck4kwaM_k7cxOsR0gEns70rjobaopgGDZ55dLdgua9xcysb7PqR6XrtJOoHlUKYjYcA6JxeeOqkN-2qCHJUQOxwzI5sjsEaPjAIkrnp1mwm6vEek6VuhTYVIZcb9IvizUjOLjtOBbDKuCYEqWEZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=TnoMLS_hJgh1IPhRWg2OLvNUM-nqBLeKXD1msTHxtTwwbhZg1UNaU4zSz9pVxofGRiLRrFopVH4sas988zgfu_84_2Xb5da1KFiBjoCU8V0iQIi_X6iEw0Rrl4oQKnL5Vhw-TaKyvRlXjkzVqL9AmUK9vlB1ndF0tJr07sY4svKhJC573c6rEW5foBOkHwiIDpSaiCm8TpPrJB0L5EYIVkx44QQHEThng8MeNcpMtgEXtjaMYOO20EkMe5TnPYp_e_OjtaFOvzVjzP4xA96fLcsoshuAbiTdd7EkkT7nq_gJl67xP-pG-pObJyUbOhLLcrnK3lYFdUrGkYirPMVV7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=TnoMLS_hJgh1IPhRWg2OLvNUM-nqBLeKXD1msTHxtTwwbhZg1UNaU4zSz9pVxofGRiLRrFopVH4sas988zgfu_84_2Xb5da1KFiBjoCU8V0iQIi_X6iEw0Rrl4oQKnL5Vhw-TaKyvRlXjkzVqL9AmUK9vlB1ndF0tJr07sY4svKhJC573c6rEW5foBOkHwiIDpSaiCm8TpPrJB0L5EYIVkx44QQHEThng8MeNcpMtgEXtjaMYOO20EkMe5TnPYp_e_OjtaFOvzVjzP4xA96fLcsoshuAbiTdd7EkkT7nq_gJl67xP-pG-pObJyUbOhLLcrnK3lYFdUrGkYirPMVV7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yc15flOOco147dfTdm70Dg-i7lSlMwvSboHzVN6GZTs227gBGN9Tl-pDla9IfOQZ9se1-N6bFRfd37cs8qXUVVDD8hUhY7w57qRMkbfXD8Yge1GPVFx032KoxAjj4-LW6V9uWrVoBX3WA_iuAaC4b4o39fuj1pDh48Ss3bnDOFiZ47SPmg_oSLQPoe7DecnUUJPdPQaKBsNOQ3Zf0J9fIdGatxdLsChrlAGlAI4r6PpgL05AATvW-mY34NGFuGmqDB4pNPuPh2KBnOSn_9pYYf5skZ8naLTHR9mQggmh6O0udWUQJqMQilgYEcbz6LSrQHXbJA6H2qZmM0gkbIooLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSRImt2FkmvqH_LFNs8QEVM--Ttv-d-EJBX-CPuDv9O6gYlDixOzGxn4tg8yd8OY9deUrjcYxiUrv5I2ks4o3zRd1YaCtpn1Ih6aKKebeRsTCdHITESPbUZWGD_tkwnRkeHejfVdZZumGW6botp4v1IvX4r64tfaqz1Lm7YxYhnnZBHyztpF4v0ymLICHjqSXchc4HhNQh6h9_5f0WRgG1g9R0eSXet2Rp4_dksloxGDNfImwWTAFPcIzgy8Z9vNVP6v_An0lqpz8XAyv2pIKrjZ6yLg1IbrBeQbdCtknVgdg_db9yfOLP41dMMc8ljUCBF5n1A170ihW7xmb8AM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObI4IoqoVOfecV9C9CojmY29l6W7dafjUF9UyDB29xNhSv6NDTq45aEeQH_DwMY42GGL5wY4_NKcA2bcknliVmKRAb8IcwH0eby5Jj24NxUM9OUl3uYCkf-NmJGsICZJY2CoE2kjq8Zt8PylhtJXRh2h8BBSDEjgXYZI8S3L1RQjZjrugmFPV4TLbnhX1dDkBUtYQVGVYkc8E74-teYs-VLcFqoKb6fhecJfvA8N_vjCq6DvqJvzJU3BiOJz4N0axxxtdJ4izyFgzWePLsEdSL_jaCt7c5tONMsFFXNHCAAdCHATB5oz-IvpDOfZsSBKbgW3Bl6YH1O-CMRW6miIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNIOEdB9e2URg_HleKMjsuvk-NtC_v8iVwTVDUXOom-KXZc9AeRIXUhChjxv-fKffnZzXNdIQFBwbLYHCsBUp4aLdhCvWj98gWYNtABMpfbzDWAW-Ccke4eTK8Q2Zou42JIFfApoeKC0rWs7wg0OnRX24y9iE2I-zMa5OWFoKjoua4XFxtqfIrSyK_bxfbnLOlcIx1Gc-Q1m28Ob4ZCZZqi22fGlAJlbBcTjaVXGvzhAro5lousJhYPJJJMDa7HJom6uTGknsVHDq3DfqYpJ1Zv7yuG4chWxs_e1I5oTfpGAo8koK0ov-a-JmmR_jxDva0QxvXG_Bv8jvBeHlNFOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=WVJBW1T23uJ_2wXeV_JsdC4pI-kLhnrIeRmHIyW-GFYAiS7lqtVowZcJ0rS82Z9KIHpP0KORQGp5N6PwqN6EaqBe8lmGmvHlRb9B5J0IAKjm8yYSGds4w9l0VqvR7rRHUzOBnB5cV-ApNc6ZZTe0-HVL2rNVL2Ugzot_SZ1r9O_mqp90R3ojzHJBYLYkbahNb9aUoGk_GIc1_O2sDyOp94JCwR7__3knLFfLQbwZIYhRbUfveWNrULQ9tDSCdahnO3MtxCO50vM8CTjPui6Kn06JUcK5GZSGsJRpUiSd9K28_RarwNb7UYsP-ijXB_tHeijs34LjTQi5YygDlrX19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=WVJBW1T23uJ_2wXeV_JsdC4pI-kLhnrIeRmHIyW-GFYAiS7lqtVowZcJ0rS82Z9KIHpP0KORQGp5N6PwqN6EaqBe8lmGmvHlRb9B5J0IAKjm8yYSGds4w9l0VqvR7rRHUzOBnB5cV-ApNc6ZZTe0-HVL2rNVL2Ugzot_SZ1r9O_mqp90R3ojzHJBYLYkbahNb9aUoGk_GIc1_O2sDyOp94JCwR7__3knLFfLQbwZIYhRbUfveWNrULQ9tDSCdahnO3MtxCO50vM8CTjPui6Kn06JUcK5GZSGsJRpUiSd9K28_RarwNb7UYsP-ijXB_tHeijs34LjTQi5YygDlrX19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxnY0gSMIYHsJ_1tJkVTo4J9cXZ_xae6HrnudmjXPXG0k_ySBg73Ya7GI7QuVFnr0m1VZ1kmrmCqgaIIRzK7WIv6Hsjzuslk5VRMPrP1tb5TmmEDCGBVmfDWl1NIpihGeimVcZn8kDmnQJBBsAGX-T5DVDEQSL9UIbKm5xVPcuStp7cgRmGf_IiwS97nwojsM6dDQ7ebcr7-ylMbyAivcZDWP7CdvY8DLdvutPDyaiHkq9BV5x5CyeO5JMogbinM0U0sKQPwYaDNPOoxIIoyv2zt5nEJRNInc4kydIOt6g0eR2q6yWHhV9qZ5aM5YByX3aDfNhvyA299EH5rDrcnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G26Zr_BCeI0CeYC3C-upqbDAEntCairjMvSCn23YTnVR1ksLGdn2r7-NuYWzfAMAxHIPPOV1cvXtsuA8ffoR9gO1opEN60mlEHZrR1qkW8SNiplqeKfVOEA6rcEaxu6aVXSDSfa3B_5PCu-URVscQ7wbnXBMiqGFktpUOq61-OWpDs7KnJrvD-HuK2GPERYyTglX9ksR6Xd_av3R9ElpcAmBBRyd-CeJu3onGYl5YPe3GezIu5HZz75FCGbiSwvbugZl_vQXgdI3U-5d7lkd-vy9wVqI5rq0MWmMbAGspOKe6xjN7n0YRVzpPazPUCzlKRraAb-SkNeZWiX_bcsL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=UxCdiG0OfzgMzNLeLNjpZWILTuQZCnw0Xew95K4mhWgoKvF8bXFGiSpUzO4IyJ2VwZ6WLKi_drAZTX8w9SIQhL0vkff_VmGJZ37MNg3ipgund0RyaHAwp5hzwV4Zbsu7nLbZNBt3ccfV-GT0mjoBKUXzMq1BESI4PsJe2aYItI4Rv6lUtHSUDWdEu4PVVO5qFMNARtRbQ5_mCERrXfqujP57dzi7J7cxTda0kNuVHIrBVA35W1gb5wFb_80oW4n3jiRgtBxqp8-ozO6VWQhC2tynYVjuAWSDVpmA5_f5b4eNefCguiUpuikQ9Nkse7IIeBJLl5GgxNPRBbL62I-Wdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=UxCdiG0OfzgMzNLeLNjpZWILTuQZCnw0Xew95K4mhWgoKvF8bXFGiSpUzO4IyJ2VwZ6WLKi_drAZTX8w9SIQhL0vkff_VmGJZ37MNg3ipgund0RyaHAwp5hzwV4Zbsu7nLbZNBt3ccfV-GT0mjoBKUXzMq1BESI4PsJe2aYItI4Rv6lUtHSUDWdEu4PVVO5qFMNARtRbQ5_mCERrXfqujP57dzi7J7cxTda0kNuVHIrBVA35W1gb5wFb_80oW4n3jiRgtBxqp8-ozO6VWQhC2tynYVjuAWSDVpmA5_f5b4eNefCguiUpuikQ9Nkse7IIeBJLl5GgxNPRBbL62I-Wdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn9EEoj7nws5Xm48F2bHlRjQN6kCmAU2kDMSKYPDwT2xT2nqfgapQWOIs2ZdwuYDoVTVz9ehcuFaE9cHEmv50PqgAs5Gogeo8rH1tcbxlXKiX9noeiI1bCzgkG2X6hyHQWRCEqygAIAD6A3ve-en-kSJGtX-D3sQPdzB-0gZkXXdKQEt6pFywR88myR1xyGRW6lZIuXTvVnyEGVcD297OYjCgLSg-Pi941MwWp73CCSdIZMm79hVFM1UIfsOBPsbujWS6bw1FinTO1GV8BldlfGEQFFdzViN8SjGwykFtqFlHWOt2GkTcSDEf4HsCIkKZAkQBvfk1J3ub_SH3IuXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=SDBbioPpJEJ51K3br9SL8vHhfE62xO9f4jOTz4szbIEhAiHSBuwsQOps3A83DAQvdgDDttdX68O-m_FjG0qW9geLdFyEsgaZxQB9xx6Yof9h7aUyz5B-seEUptzk4WnR15HB7kOLtUoxAQ39gH8LGpt8r1vN3k6N3J-1v51Xeo_I48ulWxTDJk6X-ErEhYNWBpnORfe3cYwR84tZXsQt_v6G_d052HE6uidrE06nuIL2ml2YiKiHR7TbKJg8oyZJkd7nlC7wnJbM01BEZddVXae8gMSAgSocIUoIUI6zUAStFAics47UmktvNwiBacYIIKbaKM5JeNpHTQh1FtUiZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=SDBbioPpJEJ51K3br9SL8vHhfE62xO9f4jOTz4szbIEhAiHSBuwsQOps3A83DAQvdgDDttdX68O-m_FjG0qW9geLdFyEsgaZxQB9xx6Yof9h7aUyz5B-seEUptzk4WnR15HB7kOLtUoxAQ39gH8LGpt8r1vN3k6N3J-1v51Xeo_I48ulWxTDJk6X-ErEhYNWBpnORfe3cYwR84tZXsQt_v6G_d052HE6uidrE06nuIL2ml2YiKiHR7TbKJg8oyZJkd7nlC7wnJbM01BEZddVXae8gMSAgSocIUoIUI6zUAStFAics47UmktvNwiBacYIIKbaKM5JeNpHTQh1FtUiZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=pLbVDvImmENqJipZY8BKcuYk9ZiJZcyvIw1hSX0DonBR9pwfbLa35Ty0iJPUmARtuVs5hYt44yCC5_r-aRs5t3bM_Zu1ik2RwkRDOt3B2Eu_jGTedME56aHKKFq8MEopffbMq2f0zPtbM1sA3VE9Y6MGNu0cu6f4kbllYETy7w4ircDiG9iJuGPL8wgg9tEkfjAHOcADt4pQGfigM3reZL33KOcQyPF9PoWps1EziCM0vhOWnU3jfDaIWvNd7bEJpkZt4izgTxVGx6LQA2d8ld1C0lfwCclGWWcgi6Z5pXkIVkYjo3u2usJ3rQXGlWiHkr1MzvWB_7kn6JmxBxabuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=pLbVDvImmENqJipZY8BKcuYk9ZiJZcyvIw1hSX0DonBR9pwfbLa35Ty0iJPUmARtuVs5hYt44yCC5_r-aRs5t3bM_Zu1ik2RwkRDOt3B2Eu_jGTedME56aHKKFq8MEopffbMq2f0zPtbM1sA3VE9Y6MGNu0cu6f4kbllYETy7w4ircDiG9iJuGPL8wgg9tEkfjAHOcADt4pQGfigM3reZL33KOcQyPF9PoWps1EziCM0vhOWnU3jfDaIWvNd7bEJpkZt4izgTxVGx6LQA2d8ld1C0lfwCclGWWcgi6Z5pXkIVkYjo3u2usJ3rQXGlWiHkr1MzvWB_7kn6JmxBxabuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=ZMxB_6K45GNZV-J_zheuq4r3-aY-Fprnp-MTl5iS6wYD8cxpbdAUP22mXM5FmRCtG7ZOijXkH7HTgegLafStowYLB2oXsKZdu2rh9rFYfoaxfCawVUKccH1g6B9OVQAoWwEeDo3weJFJ81PdS4aVabCjR_F-59c77scc9nECBLuXB4cTU2K8-tOXh668C1NvjAT5B1-9AepYsxTIJOGTCwBb0ei_5VgHxc7kT52QuOzbR_vuPWWBJ9wBrHrYt2S5QLgPABwr4IT9-l89IvaGjfSHFkKcblfJ_82I_cXrybsM_725viib30C--yGZi3AcVxOkLJCanWX3h1-XM_GfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=ZMxB_6K45GNZV-J_zheuq4r3-aY-Fprnp-MTl5iS6wYD8cxpbdAUP22mXM5FmRCtG7ZOijXkH7HTgegLafStowYLB2oXsKZdu2rh9rFYfoaxfCawVUKccH1g6B9OVQAoWwEeDo3weJFJ81PdS4aVabCjR_F-59c77scc9nECBLuXB4cTU2K8-tOXh668C1NvjAT5B1-9AepYsxTIJOGTCwBb0ei_5VgHxc7kT52QuOzbR_vuPWWBJ9wBrHrYt2S5QLgPABwr4IT9-l89IvaGjfSHFkKcblfJ_82I_cXrybsM_725viib30C--yGZi3AcVxOkLJCanWX3h1-XM_GfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=tHCD9EN1wOg3yk60d4ni_eeqAPBOzXRwcaUUaoxYfz3P-ae5Rcu4UsZgTJ04SbIWX9gKPgLWVMzqcHRDVzX9eos_hz4vz7gsuSAESnzmdVegNauo9TDLQRqa2eDHffhG14V75VPCL7AevNp0f_F9DwCy-dZjDAdlk2OibyIdNPmyGIisacYHB4LfXJqU5yKMO8Xig66yXj7zBk1f-RYtnjiAFSKKSxIrRjC7vt8q5t3XRU3HtoWtCABEVRFMBM77XGik8S_gCDTkUOII7JSGYfBwUhdlwC5Ar7crfJ-Qk6IB9TislYHo_NWtCSyBycFnqdRwMLl72xROlLXE4j-DnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=tHCD9EN1wOg3yk60d4ni_eeqAPBOzXRwcaUUaoxYfz3P-ae5Rcu4UsZgTJ04SbIWX9gKPgLWVMzqcHRDVzX9eos_hz4vz7gsuSAESnzmdVegNauo9TDLQRqa2eDHffhG14V75VPCL7AevNp0f_F9DwCy-dZjDAdlk2OibyIdNPmyGIisacYHB4LfXJqU5yKMO8Xig66yXj7zBk1f-RYtnjiAFSKKSxIrRjC7vt8q5t3XRU3HtoWtCABEVRFMBM77XGik8S_gCDTkUOII7JSGYfBwUhdlwC5Ar7crfJ-Qk6IB9TislYHo_NWtCSyBycFnqdRwMLl72xROlLXE4j-DnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=tVAEaYP4-s5g7ohqgr180KkCGhSua1DolkGneXLf9zgCskXkcfKIfxyGDD-jCNC9HG_cPDejyzfeyw5RYzA-BlZI6Y_3U2Uqsnwl2ldR7mI-8mICazCj1Qe8204-umLC7O5WHfAMj3M-umkkM__rOEXbugs1hSXAkHH3036gpUBb5o3i8-0pEUDdI-rVWGY-WrfBOhzUGA2jE8X1sOV6CMgOSbwhr-zH6Bi6S4conck_Ddeq8bf0ZEVHnk3hpsDjIZL72TLuDROhAqnV-_7y7TsN3hQoN3JpHOJS916qg-hKXt2ihH-YMVA-Od5LGk74nnfghXLn7Ua2CXxxw-Vd6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=tVAEaYP4-s5g7ohqgr180KkCGhSua1DolkGneXLf9zgCskXkcfKIfxyGDD-jCNC9HG_cPDejyzfeyw5RYzA-BlZI6Y_3U2Uqsnwl2ldR7mI-8mICazCj1Qe8204-umLC7O5WHfAMj3M-umkkM__rOEXbugs1hSXAkHH3036gpUBb5o3i8-0pEUDdI-rVWGY-WrfBOhzUGA2jE8X1sOV6CMgOSbwhr-zH6Bi6S4conck_Ddeq8bf0ZEVHnk3hpsDjIZL72TLuDROhAqnV-_7y7TsN3hQoN3JpHOJS916qg-hKXt2ihH-YMVA-Od5LGk74nnfghXLn7Ua2CXxxw-Vd6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoJuq5EMnOIzY3FjAF44OqLh90kPq7tDzq76YmIjeeI_JS3HJ2KcyhROZM4gNYoTI1i4Z3LBQ4DjpSYpfoT16kZdk1lXNw-Gm6JlUYXXr4Q-jAXhRKYt3GtZDlJbketcL0aF4YdEznrYwhBQnWPwyD2wooHMG19LBhEkLEIhCMr-_ySuE5PmvqPEghXoQezP6MSxFhKJoSDpR3zBPUF0qEGC462wfBwTALDH8EwIr6MoXjkyDUK10-v2j6mkS5GCrGsNqKmaYzKlRPXula5XUE6Pgu4CUy1WdPvkSrTDe-9Q94DtbdeHdXLgacXNDGf__-d6jQEjlik9o-yxKg5Yzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm7J8aoltze5Hr58rVjIPQYzcdq5dFGX24lAqpSR5qGSp4mOdGvtv7xIaRhIWYwas5_WNMN_K4mBFNx2mO0E4x4U1vb8ghtxwTZ0PIEhHHfXoS3j-9j1g5kCw7Jtt5cXrKrJeM_7wKLKT-mTJ6XUUmM69ko84NGHCC6aTvDR2A39smBbZFTGqk23wxsgiKu7sK8co0VjhM4c-NXVaAt-qLsSMnBnfNBntxQi7DSC49sN4SFAxugYJA87bBZbwneifyNK7AZ3UnBmK_4A9yCEy44VFJ46zCKFun8qriVFdNgJlUzUX5ANpJ7oSFG0U01ZOfH9jpEo1M3An0tYlPQ0pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjMy_11seBCK9erS88XRQQ27SbfrIffLZbrwtRjPmcq0DMXGcMQhLDwv4cpjxMNkvqeBz2CFyV9_1BjfzUIeZEaMZHoUvN9lYnFltIIiX9lFTHp3iAxFrLjQhi8qM6D4hl-fI7MHP9bCTTeooctjovJZ-Sb6lNLAShxYfr1Se3fSlxzakBxpFPXnqyyYmz4Ii-LAamqJRXqdf83Yf4i7Z2BlBR_0BCcJy0P-2EGIi_5DVJzZtrX73iED9_6IhIIA6WNlpPWrp5IbkNhexBi37qCGeAuHSqhxpVhPxA6MMkQta72jG1ofYKJ1M-iRvD0cUISmTEzrtUCGx64xJlWJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mf7e22STmf3IHfv82wSG--PQd1ZslzNKa0a9OrjeBDFy5o5lruU1hg9A5G0-Y-7vTgw40myHZCgtXmLhQ7oRIKnGV5tyLZ8pPxEUha-bWUNm2kcV9TiOdciljUrMDwCO9xRejwTXqIxf844H-O6v4emsYvO4xx-uOx1yU1BeOjApLZpEmllyW3lS6BVDMbV4lBqH-SwGMtV632wkrNiQq5GHwy-MjO2aDV_V1GpOXoo0rNaJsD_lJF_QEl-M01NpoD6K0G2Sc0jhxO_PMQUUFtY6_reHRkz_rHOgszpzsv_yereRXaMt1JINRENxWbrLREr-OrWrRK2p3GVKKkQzJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=LjAHGAw1omq5hClfWLpZjZkr0mNq0MuXDEHQbmwqmCHG2an3NH34D96ZsHZASvC7S_7RDoN7XkdxRFYHvSD73fxeHqs_IbgZUfWBSu5eb6qw6A-AAV0hwxamqXf5cMpz4jSMQjBO2hQekX-Hv13idvSNKLM4q7acw5BCvfxXMPjqFH8OZVnUKrtqDUfIbxaGadqBV0heBtEoAv8yQXqfSSP0UB5NUzT8bwEiDmKhzsPK3yYh8fIbLcD8k5typovtxs4SLH-6-k2j2pLOErFJHJXkH1vL03ndde1QPFaZxt4FSxxKvXZnLVh8AsQpi6wanXCurxbEmnDXCMtbOLsJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=LjAHGAw1omq5hClfWLpZjZkr0mNq0MuXDEHQbmwqmCHG2an3NH34D96ZsHZASvC7S_7RDoN7XkdxRFYHvSD73fxeHqs_IbgZUfWBSu5eb6qw6A-AAV0hwxamqXf5cMpz4jSMQjBO2hQekX-Hv13idvSNKLM4q7acw5BCvfxXMPjqFH8OZVnUKrtqDUfIbxaGadqBV0heBtEoAv8yQXqfSSP0UB5NUzT8bwEiDmKhzsPK3yYh8fIbLcD8k5typovtxs4SLH-6-k2j2pLOErFJHJXkH1vL03ndde1QPFaZxt4FSxxKvXZnLVh8AsQpi6wanXCurxbEmnDXCMtbOLsJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=mRNYHdlJT214el-UkYIHemJttJ14Bv5qm9VI8sM410mKoovftwsgO9DoIGQmR9mAvWJux8Hj7hfBvXCaQ0p-TwW6wVnjOjgxM_fxTD5vDkbdJzeGvXF-5HIZdDs6C9OOl8CHdEdAVlevV7vPTuaYlgqnDZL2SdceGgmCPN9lFxPO9P5FDQd08ZHHsk5A2oIUjlZgj22x3H_1Y3FFfR7P2KmmSG2kPD3_9l8Shx-Hx7VQcF6RoyjHja5EiJXqprXVd7V8sr4XLrxMsNYNEUxzoEB0u9r4-bN9Q8EAO946S7NVNsx5omLR08iiSX6SrADVQSLWvaIt_KYa_G7IMHDO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=mRNYHdlJT214el-UkYIHemJttJ14Bv5qm9VI8sM410mKoovftwsgO9DoIGQmR9mAvWJux8Hj7hfBvXCaQ0p-TwW6wVnjOjgxM_fxTD5vDkbdJzeGvXF-5HIZdDs6C9OOl8CHdEdAVlevV7vPTuaYlgqnDZL2SdceGgmCPN9lFxPO9P5FDQd08ZHHsk5A2oIUjlZgj22x3H_1Y3FFfR7P2KmmSG2kPD3_9l8Shx-Hx7VQcF6RoyjHja5EiJXqprXVd7V8sr4XLrxMsNYNEUxzoEB0u9r4-bN9Q8EAO946S7NVNsx5omLR08iiSX6SrADVQSLWvaIt_KYa_G7IMHDO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=qo2ZyTPtHzkfeVyaLhTfspRcFYjKaKceEIb8mXFiLWy6cUoqZlJivaVOQkeMx5-Lh4ZjW70kaLVYzirHA7LGvb05c6O_5J_SX7q6eHJOQSZKia4wTqNpZNRfvfHEfAextcnSjHEoAbQTZaI8te0-6D0HpUVqmpgpudvqmdcsqu4bk0uZjDtrD-Km-Eip7ciuhjxGfy7kjo5yez78Zvdb4NaQ7sRNIkfpvZwXVFfcMnVu0gvRlcNIjM3rhFtWllzvqV8L7HR0RYgR1R7UyL1kiH0EwgSxxB_vg9X2cT4IFa2F3H0BHqPgBNSLiW2aIcQ8sklfaG-nLBeb9j3tI0N0yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=qo2ZyTPtHzkfeVyaLhTfspRcFYjKaKceEIb8mXFiLWy6cUoqZlJivaVOQkeMx5-Lh4ZjW70kaLVYzirHA7LGvb05c6O_5J_SX7q6eHJOQSZKia4wTqNpZNRfvfHEfAextcnSjHEoAbQTZaI8te0-6D0HpUVqmpgpudvqmdcsqu4bk0uZjDtrD-Km-Eip7ciuhjxGfy7kjo5yez78Zvdb4NaQ7sRNIkfpvZwXVFfcMnVu0gvRlcNIjM3rhFtWllzvqV8L7HR0RYgR1R7UyL1kiH0EwgSxxB_vg9X2cT4IFa2F3H0BHqPgBNSLiW2aIcQ8sklfaG-nLBeb9j3tI0N0yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf5BIDaQiLFVw7aLrcoruFXfqIRqshK-Vkxuj4UaU6H9wTXXsl1v3fqnFbgwUI8tQxY9mL5bEZLpAxtW0ct29UDK7zpPW-Vo6-E_QKaht47JwkJah1J9EaCygtom1zab8sj3N8A_win7-Cswu-ibVkjf9QRrIOR1ULedkKJc733OPEHyMN3V9o7aNrALKufPdCMX9yMczuD7OBPfWkK1UBctVmbvS-gtY8xraLEKpzb_ACeZBVPLsQjel5_td5DdKwUTL_Q7Yn7O9JjuN-DkNaF6KuffIJpjiLzPnEdFJQ6NErpEZiiB2cawP4bBpjJylapgFXYK1Y9LMPWZbZtZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=jmTC3nPX3CSqHLo9F0SiDBsfgnFcvZVTqY1H2yxXGvY_gQwdcmfWIIYzhLFE2YkUytpaugCjb5ZoCRncVNQkeAXvqT-LMu98FpswzgqdBEFz5Unkoil7OPCR9VAqKeXqocGw5nuO_G0MtiHm0aeb9puxrGZFjWiOyJPUCx0OnPNQECtmBvscQeLk2-tQKemrsByAXEWRcoiItW5Z43J1U3rURU1_JT5flZetEePCJqcyKQApBr2CHT6C_btwvBYrCjKAy9l_IVLj50V6CqVfTEUOhb4KdIGNgGbAgkoRmntg0BFCed9ukH9ReHndnY0Xjl-bpb9IxffC6FYVYjDSK5NLV7xVpDyHaOi0JjU6jNzxk8SzGzV3X0Ov-8BwBFi_Dbbd-77jLUyD3lgnPr23ohM1a3Vmvf2zCzWZAVqcRap5z4c5L_LC9fgmwX_n5mEo-kTc_PpeLVHmcB7uXYohkGsqi5gOE0wFljhV-Cy1CHZx5ao-eMX6jXijCgXsIUvzYgudV94CHr8frHlJGlhyY5Ggy3JxlaF-72M22-6VL-p_3Ao0PFrIRKRrc4SQGXUeNodz6epjyrv7k-K4a3dCJqbkgcZ3oF50uvWP0eY6A2HE-Cc1XfSmcsAlUkNFqogeYCo6DilxwpLp3ZTzeCAY0V53x-KYfUCXdI6eAubGq6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=jmTC3nPX3CSqHLo9F0SiDBsfgnFcvZVTqY1H2yxXGvY_gQwdcmfWIIYzhLFE2YkUytpaugCjb5ZoCRncVNQkeAXvqT-LMu98FpswzgqdBEFz5Unkoil7OPCR9VAqKeXqocGw5nuO_G0MtiHm0aeb9puxrGZFjWiOyJPUCx0OnPNQECtmBvscQeLk2-tQKemrsByAXEWRcoiItW5Z43J1U3rURU1_JT5flZetEePCJqcyKQApBr2CHT6C_btwvBYrCjKAy9l_IVLj50V6CqVfTEUOhb4KdIGNgGbAgkoRmntg0BFCed9ukH9ReHndnY0Xjl-bpb9IxffC6FYVYjDSK5NLV7xVpDyHaOi0JjU6jNzxk8SzGzV3X0Ov-8BwBFi_Dbbd-77jLUyD3lgnPr23ohM1a3Vmvf2zCzWZAVqcRap5z4c5L_LC9fgmwX_n5mEo-kTc_PpeLVHmcB7uXYohkGsqi5gOE0wFljhV-Cy1CHZx5ao-eMX6jXijCgXsIUvzYgudV94CHr8frHlJGlhyY5Ggy3JxlaF-72M22-6VL-p_3Ao0PFrIRKRrc4SQGXUeNodz6epjyrv7k-K4a3dCJqbkgcZ3oF50uvWP0eY6A2HE-Cc1XfSmcsAlUkNFqogeYCo6DilxwpLp3ZTzeCAY0V53x-KYfUCXdI6eAubGq6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlm9FfaPY14TURLqKuVQjYLJnKJiUQoEjqq-XAqTOoc3DtQmwRAb0DbVvrcR0I1Y98bEcx9QNj_AiVCAHTSVfImhDCUQDWbTs-zPuekDoBAiXWip1MTCnfpVEInmcmjz63qIrZf0fFwQXoDBL4tNztzQ0Qus7X_af4kh79KZRl50w7QVArljYgZx1XZHwzqGhHunoeTocOfDsAL5Its5-F9VjlI10l9LMcPC69kB3_G50BKU10AFpO7nPVKoMUkLNNffEoxQhZ_bhDjUCK4NKQircMdGTTnL9Gh1LRwrpvT5eKOedAxP0OfrglqXJ5xP6SOjMPtvBQ4A8xk6-Q1b_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=kyqewBewXukODSbpjcjD-xJ92k_fVSgqlAAtAx_d-wRJQUhuFnCcqquKNwgcofkJnN-BHqFZL_d_rDWm3f6LsJdBDYloGjk0kDPot-nnlmE6Byx3_A3haR0UPu9h3cl5foX1R6IvgoqnIQ9ZHG-6MX5Jj2YyRhHtavba-KP8kZESMnrMTQoR3t3so-RqZ9vZBEsjIBWec4E4KDTdXIcRomz5Gorfoux6831kClmQo4qi3tIBg1mkOtzJ0vvqfPr6DBAzYrIoU7dnfET-RuTjUHA5gdaOwpCLy8R-pLwWGbSqJ9NhSNSRyX5K98KgJ4L4EUfntBPayb5cQoCWt6gEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=kyqewBewXukODSbpjcjD-xJ92k_fVSgqlAAtAx_d-wRJQUhuFnCcqquKNwgcofkJnN-BHqFZL_d_rDWm3f6LsJdBDYloGjk0kDPot-nnlmE6Byx3_A3haR0UPu9h3cl5foX1R6IvgoqnIQ9ZHG-6MX5Jj2YyRhHtavba-KP8kZESMnrMTQoR3t3so-RqZ9vZBEsjIBWec4E4KDTdXIcRomz5Gorfoux6831kClmQo4qi3tIBg1mkOtzJ0vvqfPr6DBAzYrIoU7dnfET-RuTjUHA5gdaOwpCLy8R-pLwWGbSqJ9NhSNSRyX5K98KgJ4L4EUfntBPayb5cQoCWt6gEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifpYg_PsH5INJf_p_nsNzeUJJRu2eLVEcFQu0-uEPSVu1YGqTjfru2xGCqMo9F7dF4bhockN0O58dpKTSRDEidoGrZTgJ57cpP7fA8Yi-OGHJKpbSOd-C8g9wp3A5sjMc0H85Dxvh139f184VWVnKV1-2Yg6wEWSUYuP_UHgljIqs63ssPFTGxLdEiaLRoJuW4XCVnMba0sOEv6ejubwZ9EyMRqwLCvpBp9M7ydnzDXPQ3sZYcDoa2nPkbDTVFXyhHCiXa72a_vZ2RV94ArDiWeTNqAxsVWI7U04F_T7uu92iEFZuV1WIxtFAz_3zHGuZbav9tFi0tei-prDZdOQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOlorg-HAq8bO253zMbj7_wkHEeH0mf56aDHvM50bveJhuJNb4nENnT7wmAUnUSi50Omy5oCvtH00zuHJYb8RWZ63dpnI_2BqQGrJRNspFO2zkedUHP7AfTGEhQyEkQVPy-MgBqg8gzNoYOsl7YMCFz-JOUlvdI5QRLqXs1WTOfKE0ihAurGPSCsQkp4Nb2vasqrLnDDcoE3Pjqn6l5fd1KOL3NI9hYV8HvsDmI9PJagubURfm6QOKKZJUrTsnoSv1mEDNI0zd2h3tR50X0BTlMvuoWeSloLCVNQ3SfXGjYXc8zoV0iLtA7vCnLp_D1fVA8ZORuPyuRMV_IV2-t52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkZTjvhpALJUZeWEpwRsNg3AnxzBGn7bce3jS3tnT3HO82kmeL7-5MAQ0kIiMrGIlOcuX8nvwwW021IViKfrW2-uJ_OegmWSKrqrfnuBaU4czNLlXGtqS4SfU5G82aWTkvCzTa4aJSKNCr65hpRfRB9gSRRMLJ6n28-TejBYzV6B-xaOAZ2HrNdbVVmRiPaHtPHHQDgyuh0nF62haiHD7DUKBLOcdmO-zl2BSsfCCQfTQ811p23axe2sonFJGOSBd6TjjHPsmkV5IMpVfTiKMBOxxzcek06lP0NG2EeClUCMRMigav7nU86MMYfjje5TkBJGHQgjTXa1yglZIyYqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et964QJ21Vo5TUL3oQ8c4Y_YpdlwDaw-Yl6Fm-je5dSnMqIwRfr_IK4w7QWTZvGG3zTdvDH_z8hTHHR8Z_kybxTGoiu8GBcCcZeV0mZVPDjzEY1Ng9cehNxEYDblmxRyKmFs4GU6JUQmvPhQGd5pnNMy4mlWNuAE7AuV5VfKHjwrTjPV5xZ82S08N8LhhElvIxG30I_vorrNqYJH-JKUKNGZOVUH6aVAE7EIs6ThJJTEo2CoM046n7SzIa4HONmhhjn1RDgzAbxBhkY0mx2aLpHCfbzmG3DnT4EFHyk7SUXj_aTRPKZVZpMxAP-vTzYE8AFrlipJsjgoFd7RtA89IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpPg6zj08jKGD0Qh5H2pIBjbeO4ptg13mHn0bJQ8O_yGFSOG1vUxSwQRuY41j7Yht288BsWUdBooQCbHVZRHi-nAo_ikQWdkxZy4cWT7kHa1IM9yC_N-34FkYoINFz8hHpjot4-a9L6S6Nbja4tdS6In2kBRye8WKtKLgiYmN7W5pU6VwSG1V4_rCqZ3VyfLbMohiELQPXZSId_4HMgCb0xmIBaeArGQE80wYmkvj4SoFXnZ20Mc7rAhtoaiYChRrsK2fP4SgiyUBAG7ixifEx-VF-ih-1g_ZJXUkh8hj-lZra3ay50us8Lt3Ggrv1KUvIFJrdP1nxQyDExjVeAnAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYVcSpy-2-p6C-6DDMe7BuyI1zr9ynKSx-HxDlVCZVewtzcYl5imQ6qkf5_zxY1aclOQEr4vH-pPHrSbLTK-JrH_AaCXe8d4RXF8gwmjYvwxp6xQlKx-gUgP19lgpK7V28vW3PpEYA9Ltlo-rWl1-oUrR_l2FjwTQcJx6M1QeRV-Wq_YLQouKLX7-fHC4PBmRRLXV8x5jJmz1xdW66Ex-cQmyw1h17xvT9SEc2CcYtVvHxaqXwrACr-ptFxBdEE-QGdyn8XXJorxA9sxF-m1qQVc7yXFYz9u7CtXzCAhYMe6hU3rV2kjwO1dgtRChtDquWJkIAlxLC350tH8E93u8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZE5jBE5LlL2Paeph4dmQrs_v6dnA95V-u1AyFGsvy_XsrFnE2XzhhzOzWqkKBjq6aIiSLl0WKG4GEe-Wb1abkB9KkJrPjB8lC6vjkhj_4cCvbPVoSm1QQRc2bnikBfOVfCyIL0wZVI6uZvG9Qj4oGEw6wlksRA07bt-y4gqNMccXvJhxVT2EoRz4cESdxn03S3ORbPKurFz-yLK6KVLiN_8fOdFlAsHkvaqXodXmu7h2LNmNkjBguRZtGiIaXkzRi-O8aEpTnww8enQNYPVwxVSqcmFnnlyBpx8BoIj1bHcDEfjfIPPo8_2kKqlBFJEcE9dGTUfwkjZh8685vtx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=YrCfFToidAzY_2UH8ImMzn-ILC0KrF2MdkaVQoUeMkitKC7uRYstEc2i4IiuvsaKWRW6eVzUNaXCvmUhAQ_0tPIM_ojVSXZwuDZR2Xw9sr1Ug0ZkgKB8EdyKw_N7UTOnIsPghoiCH3LKuPKujG13OrXb3wciZSYxv6Qru71UejEfyJZYhUPkTNHksDJ-L9YzEuOWHmUJBNZER5qkBM8GMiFigjkdxjOkWM36QjcBbHf5W8CAoj8iCNul7Y4cwXoekxk-nSAFhnUemvlm07KN63GGtt6U3fqUnA_Ez9iYtWhG5ibPrURRU-unhZl1gA-JXuEuldiof64vYWRxPMfoig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=YrCfFToidAzY_2UH8ImMzn-ILC0KrF2MdkaVQoUeMkitKC7uRYstEc2i4IiuvsaKWRW6eVzUNaXCvmUhAQ_0tPIM_ojVSXZwuDZR2Xw9sr1Ug0ZkgKB8EdyKw_N7UTOnIsPghoiCH3LKuPKujG13OrXb3wciZSYxv6Qru71UejEfyJZYhUPkTNHksDJ-L9YzEuOWHmUJBNZER5qkBM8GMiFigjkdxjOkWM36QjcBbHf5W8CAoj8iCNul7Y4cwXoekxk-nSAFhnUemvlm07KN63GGtt6U3fqUnA_Ez9iYtWhG5ibPrURRU-unhZl1gA-JXuEuldiof64vYWRxPMfoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paRpeVT-8cd0YZWPJy1JQSmaTKdp-AG-U2AoITaOD27KVtqPqtM2ZCIK0ak384T8BRwoua_gLvkUjVoECF7ORbWzL-DpwbC5Qfi-tFhYjGCjLLXseimw4aQKs51ifOIVzqQ9Hidvs6_7b9qp5Nta5daubJTVQVtT9ZfNKsS1yqiZoaNApltUekg8eM6HleFXlP0GvgAXIv6u9bwvdjHvDfa43D9tV-kZHVBwXdPhYn0mR95bfoUOJ_Nn69O8OUucQaU06irL875miFUtx2fK9IRLJ5MTcI3uHLDzDYsk3PPvh7jtWDbVcMFiaS_eTuiqSSaxIusNhejvPK3zsWvQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyi4WqFX-BfYkrMSAQV0f1nS8jPcFT7eEJGcRyJ2EZLFYve_92-SvtJIwlaZK4othb7HPajH1GhX3OGCyBZxkCfwwa-8-V0DtDbFYw9I-u0YIXKi0oVl9vMrJc4rB78WHtCsGXgHigkOiryKu53I68BXjItT9v03RmSdzM5TzvipWgup3eEwkAvpmGWANcM7VWajc_VOkjzchWgfhDhbnE9-IpTgbd-guC2lXjatLPmqws4xL9RLsa1MqFgFeURzXJaL-O6Qapm5pZweHLSKQYdLUTISGgzeAxAAfcs8PMqB7dZpAhpIjkbGPmMSBGzhqt8JbOOm7PZL0hpRsBUU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=ZRwL-qxfDc3Qbkjo573e7R-Lw8RVxs2h_dgtD5hQgTA69KJtnt2JMhT1zBkOtPYSyLtg-aarQ-OSap3EtNvdlf_fWkCvbyLl9KFRAf_EXN7i0mEtdDJsLaTV-AsUMr5S4FISaWewPLQPl5USrVICCmEpvr7XpBNfE4jgO7WRipplwctzDpk4ESsJhwOnFh5a9lb_3K4IsiHST5_o4pf39hP1rUFSwXtj0PzpHq3NGk8DU1JNhL6ieZ1dXvvk88HvGqIqPGivUq47fqePMtD7qunms72_Bu11s0zkcArg8GoIVbZDbn7o1zVsPA9cGSGG38deuyAJXm7OusRyfZE6PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=ZRwL-qxfDc3Qbkjo573e7R-Lw8RVxs2h_dgtD5hQgTA69KJtnt2JMhT1zBkOtPYSyLtg-aarQ-OSap3EtNvdlf_fWkCvbyLl9KFRAf_EXN7i0mEtdDJsLaTV-AsUMr5S4FISaWewPLQPl5USrVICCmEpvr7XpBNfE4jgO7WRipplwctzDpk4ESsJhwOnFh5a9lb_3K4IsiHST5_o4pf39hP1rUFSwXtj0PzpHq3NGk8DU1JNhL6ieZ1dXvvk88HvGqIqPGivUq47fqePMtD7qunms72_Bu11s0zkcArg8GoIVbZDbn7o1zVsPA9cGSGG38deuyAJXm7OusRyfZE6PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=KN_2TjusXIC4z_La_OJ85i_mGmN8tkW923Vz-X2CMpwQ3qNIkwzmYLDcnsPl8DtME2fKiBf2EZnkJ1aQTmIt4zouaTfKO7qhzTh5rQd4QZE8L1fuq6VcJqaSXsfthgR7fpG3Lrcz4z47Jwxyp-pDPgyVgjXJkR4ygGlBfFKAQjC5xZn-eVYsS82Qd0hcwnrwGM6toeSVYzE4w5CTDYTi8zjvVpZFBGXyLw-REV7BokrKqSvBJISZ-iawd0xqbpRCe-gGi7VuDMmzMZVpoj5IGWo7niwBmxTKuvFp2C_E1lJmBPVfpOYaz3ye3PnFFEFtfXQYwTszBoIbx5qy1bWY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=KN_2TjusXIC4z_La_OJ85i_mGmN8tkW923Vz-X2CMpwQ3qNIkwzmYLDcnsPl8DtME2fKiBf2EZnkJ1aQTmIt4zouaTfKO7qhzTh5rQd4QZE8L1fuq6VcJqaSXsfthgR7fpG3Lrcz4z47Jwxyp-pDPgyVgjXJkR4ygGlBfFKAQjC5xZn-eVYsS82Qd0hcwnrwGM6toeSVYzE4w5CTDYTi8zjvVpZFBGXyLw-REV7BokrKqSvBJISZ-iawd0xqbpRCe-gGi7VuDMmzMZVpoj5IGWo7niwBmxTKuvFp2C_E1lJmBPVfpOYaz3ye3PnFFEFtfXQYwTszBoIbx5qy1bWY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB1TBi5KQ8-TleBjJAWHAYnz1TnC-9vnYRZYRz6nIJonFgoiaR8GzWDXlXJ1d5k-kpJ5S_oXwNT5dJmgGN9jM4wXoJrB0taPb8ATZogtZsWqARl1UAdeBkCTREnbT_Z4vYZI2PoWAL-Y0KaHJcoQewZTP6dBMEOK8o5bwKncDJPUyZtzMv1A6PKFo8dHylACH94-6aV8g7sIGQblzroVvmI_srBF89znh0VJNOeokKU5rplGfCoca70LzPDEfQqKYkKlr7a-d__nJxIfUhESan6TL1vI8jIZHhx9hBwm1_uIqnUqS0xVg_k_7iIPloGS29Sf5CW1XgEVgEUpKNh_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=Z3QygOrad4HfFLoSBfHfR0yxR1DTPZcf_rblqM8ex61Ixq9VOCnBFNguLajp-Gbua-o_1XvxuAJA79G7SwKTfxyE1BzfRrlTC1i_GyIFexwpbbLqalKJKdyo8VmfhgMqxszx_NBQgpgTZbdOB6NhsWm1jhTJ_hvA-HPlYhL0KOZ0FTKOMiBJ6FzV-JBik8wVZJ3s5s31YWo3R5sdr6BvF6WjUanALVi_zdjeIsuHHJhN6uTUAtiiSShvoGnSI8Jm_FebKDQbwMsFEVTfM6U2cbRZvUAkAj7-YLSH2R4tI-awroFEDDwEy2Ysr5-_IOYCbOXvq2PxElZ2xZ3PuUoG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=Z3QygOrad4HfFLoSBfHfR0yxR1DTPZcf_rblqM8ex61Ixq9VOCnBFNguLajp-Gbua-o_1XvxuAJA79G7SwKTfxyE1BzfRrlTC1i_GyIFexwpbbLqalKJKdyo8VmfhgMqxszx_NBQgpgTZbdOB6NhsWm1jhTJ_hvA-HPlYhL0KOZ0FTKOMiBJ6FzV-JBik8wVZJ3s5s31YWo3R5sdr6BvF6WjUanALVi_zdjeIsuHHJhN6uTUAtiiSShvoGnSI8Jm_FebKDQbwMsFEVTfM6U2cbRZvUAkAj7-YLSH2R4tI-awroFEDDwEy2Ysr5-_IOYCbOXvq2PxElZ2xZ3PuUoG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=E8u7Qc1-pUaw8LnJtdN8m6h0-c3BjMhsbV6iitH2XT8dDOLnD4TZgaDzkHGPvTSoMV4NVreSDfq76jV_9UEL0cCaS7L1ut0VRSPregVF1MpQ4GemJw3c1L-JrboKlevt9rxtnUCjuXJFrDxOdc7mD3zSGEOZ4YR1t_Yb-1FdA-3o2v1wEXut8rcFZatFy6sXqfozdEiWA7--YyIvqVRHg9BBA7aWfItJT4dChvQGotoLDtOsq-pmZ_nasopfVn1f5isCsTZrac_NX0fVzIHQA_hpV9UPuD30AQVmTlg1LllN_cozvK67julapnQ7s-GooRIZqDCc9-O3wvTr3yidEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=E8u7Qc1-pUaw8LnJtdN8m6h0-c3BjMhsbV6iitH2XT8dDOLnD4TZgaDzkHGPvTSoMV4NVreSDfq76jV_9UEL0cCaS7L1ut0VRSPregVF1MpQ4GemJw3c1L-JrboKlevt9rxtnUCjuXJFrDxOdc7mD3zSGEOZ4YR1t_Yb-1FdA-3o2v1wEXut8rcFZatFy6sXqfozdEiWA7--YyIvqVRHg9BBA7aWfItJT4dChvQGotoLDtOsq-pmZ_nasopfVn1f5isCsTZrac_NX0fVzIHQA_hpV9UPuD30AQVmTlg1LllN_cozvK67julapnQ7s-GooRIZqDCc9-O3wvTr3yidEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk3EYGTSItsf5gBhe8HRETY85b4dU9oMsD8L2hAxwKNNG7Sql7GO0R4dYPZpoufLwoW_EMnlgK90YK2t5ud3phan7iI-6Xgs8pfnnJesfE6dIn0DtGSw7NrS5ps98t5nqWk-KN1YbH4wBHv9E6riVH9J523es3qj8HllJ8NEDx5Z0XOYIGp5K_VwhY76p4CMCJC3OyRNZ7LUHv2fgVwL4wne4CHS1FXGRVKJWaSlRy7K9fcBzBG02k_QzczyaMUc3v_p8xJql0gauWCoSq5-jvUhcWaXP8TfKmgY1N5jt1Y1uCQ_R9KVsZGYLM2YJ6o791CacjihrnH6CZdFZ4yQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3bDUCu_N8FyI4YGENFNE3ieuJ81cK9f7M0hIjUGBdALyJDceY-NnzZZVv83whBtVOKivaa-qE6uCvV2GawIgIHtywucsZZ7suAhjVg58g6LwrMfL8WdT2fuilMBwJNlH583n83OdESRx2j2tfAawoC4jKJdAG39IUr3hFIQLYoPZbGsbIBrD_2XLXxLLDc3pYJ2xPyS9T8q9k656X61BwYuAvPNCApPZSw2PSgW46XEYEDTz__edXeFDxZ47OHZE48DY54r1uLrDn-w5CfMbu_9AA5jC8eGB0kU8lK6pXnduGJUQM0vXkH28H06H_Ld8IfIaUVzM-w5u2bRu2XR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFMsn0KsBBgUcYN92es1SQh_cxD48wDTWbyZVLa_q-td__xTYP2anAZahTJO97O8qE8P6PoLKu0mEDEshqgOYHLocCdxIgQjfS6AFYAV6ceZlljlMrl-CEaJb_hF_gr8TQzeAz-4Q_gEPVKR-4YNWrXnY_qZP2EdOXlaQ11HWqWxaXC_1zyDgJk-wdTxIPcBPrWrgiLOvjOwsGZI5jaGC0d8X_RLMTMzwttE6St_Yly9awDIqflgp0SrJA0K4Xe0TXygLtWU4D50GLAPfieh3Ys4PGTs0wLH5Nirel-KzD45OPIfwkF0p80cQA66lJK4J1T6iebcSdeSREb6cyfLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfjUUdh9v6JniYuvHfCl75Ab1QtU0h-6bK69oedWMdBdbtUDfyvbxdq44jFVRUzYfYBSFilgpOOccnZ59DlTdgRhyrHV7FNdWm--aZUDama7vhEln7x0i56B6si2pb0BX044fjGNfyCYB9N2duHp1Xi_JzxUVo08su1c2Lnz1OHSuD2FYi2ILSwIF5uPn8qdr1UzedZqci-Wm16vUqEj93uV43GayF-MufghfeWgXwz1_f4qDhwm2kGWkSClJMpgeih14sC8lgPeektPogfPaR1ioJimHxmTwlTKeyp6LS-sWPzxPdyt6GZRAFPsYUCQbEGvBDaelelSqSb8ZXVJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=fsMqh5tKrGnpAjIJPbvMLeA0JkC7olAoMvvQApOlz_Ea1RxfdyRDrYSRTtyttVx-ro8yqSBpxFWJZdtivaad7mFsxLzrImKqshTZCyhB_3dT8-U_hTE6A2_qroLTL4mfLOUSrIm1BWa5q3d-6XPwDDetDeIoJRHOAxZNEPoSb0Kt2vL3SBOZVh5TODhl4eAkhmQhCf6qBFLY3El2q6tYjXw7rrgTjKrM-NnIjwrAMgIK9tJEt4cSUwZJ2sUP9v9CdiaKt4kSKSG-GdnqkkwOW47MFq9tPNu7q7fBF2vkeirA0jHFa-_q86iAGxYmsH3Q2U0IanTsb9WOJ6qp36YWag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=fsMqh5tKrGnpAjIJPbvMLeA0JkC7olAoMvvQApOlz_Ea1RxfdyRDrYSRTtyttVx-ro8yqSBpxFWJZdtivaad7mFsxLzrImKqshTZCyhB_3dT8-U_hTE6A2_qroLTL4mfLOUSrIm1BWa5q3d-6XPwDDetDeIoJRHOAxZNEPoSb0Kt2vL3SBOZVh5TODhl4eAkhmQhCf6qBFLY3El2q6tYjXw7rrgTjKrM-NnIjwrAMgIK9tJEt4cSUwZJ2sUP9v9CdiaKt4kSKSG-GdnqkkwOW47MFq9tPNu7q7fBF2vkeirA0jHFa-_q86iAGxYmsH3Q2U0IanTsb9WOJ6qp36YWag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
