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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 03:15:52</div>
<hr>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rkskz-j4x3cRiKbTbaJyCtRUeRPGIeCeNrQ1Obnz3JVvkXpUbNkI-T_R59PmwohAwW5eYJbiy1bEhhkfbZJwEZmIY0eHhUV1Fl2YD1dGh8C9BaFABG3iSziU8k1Yergh8d7oz-ugdwsMuEKdX0dfpEmeBi69Xns-aLDMcr8rbK215B91_aO7ZnmewjYbTWqdcgYtC5_fHgWrXyeJ04hA2GQOtrKWRfr3KV66MKqygqKiwXjlCaVQNAaO07lw_VlgR3vzlyEL2sH59Ypqr6HfC9VULLxSSmaTeHhIOASjallhQ-DGZ53QgqyPECJkptIKXYoJfHFWmcELkYbdwPT0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=X-bE8Z5NK5ymRfbSigJSVBH_gDHuCOxbOe5tq8NsUjYBzdOjnjiboN5PEU-3xEJ6yT-E90mdVJc0JwOesTunZTPr-JUQpgcX8PEPEgQ75kjde2tN6EDH6B2rv2mbZ0nPSvS9goK20qiatn2-5W74BZhfizUQtFl3hytv037yzH4HZoAFt4tWuOk65qYesL8vnsRx8L-9ciHYf6tPtrvojHZSVAoN8d4pshxbW3L1rOUYwcNIELq1BW-YeZm6ENjAAG_rU-ANUSS46RXMM4xmmw-CwFZ4T1DLqAM2Ripvn-NkmvrWw9KFrQ-cEZwBbAWxDj53OeCP5ntJxz_Iwc1Q2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=X-bE8Z5NK5ymRfbSigJSVBH_gDHuCOxbOe5tq8NsUjYBzdOjnjiboN5PEU-3xEJ6yT-E90mdVJc0JwOesTunZTPr-JUQpgcX8PEPEgQ75kjde2tN6EDH6B2rv2mbZ0nPSvS9goK20qiatn2-5W74BZhfizUQtFl3hytv037yzH4HZoAFt4tWuOk65qYesL8vnsRx8L-9ciHYf6tPtrvojHZSVAoN8d4pshxbW3L1rOUYwcNIELq1BW-YeZm6ENjAAG_rU-ANUSS46RXMM4xmmw-CwFZ4T1DLqAM2Ripvn-NkmvrWw9KFrQ-cEZwBbAWxDj53OeCP5ntJxz_Iwc1Q2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE2fAIBXlERRIxNP_ypVuEEMAophK4T00pmS5UhHJ5SWaAQkEf5PnCf9I_JaSvom7uNgagvUUFe0vyHTYylmaigLYTLSEd38cuvXzzMbOy27wFXhVzT-dsjSXGONvViacKZwoZs9NkwRPTcqppoP4aZ-hqZiKBlDWJgBa-TOFYU84625e2YgtD3NS0s0gq1COFfDln7175bUGvjPxLdFI7-rxjcPD8r0DD0eGGuaQNxgf-dO8XkEJ9CsCmc-OhD5VS4Qo9b6p_okRtYYOfhub1Cy77PFQskboIuInms8Iic-wYv58ywA0a9gQlypYRZTvJ8XB5DlOMq-L6X0gEPltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPCc1yKpVOmap01bOdccSEt0yVfbg1tALUPbROUeOmpgJpCH2yF5kKdEmyyYfztD5Hw0XTP-fEnfePF0Ryj0PW5bEVRVawaHa6p725-mKVaL4zsE3f50WVMHhVhYgba-RrgclWsSRTf0e6Z3My2242Ro3wRbnuKDZUrOO8Lpmw3M6Lip2Fqkpano79cCl0oERfEN4G-QA_CDL_N9F7qItHNH6BlIDJigN_3m8J8-lFWEHU1UG7IQ7wSFPPmYA-BDFk2Fy9SpVW2_Upodk8SSZGv08GKA1gpQv6PacEm42q04TGaJFxeh0xt1t2W1fUKg-5b_q3BMwfQaxFLSxGDTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNl5Tfjqilj9PGtk6OD44yOZJq9-PfqplTRmvWxnTsZnkNc4hS--vT87v8cXMNRvFzDMaHORt2kUBPQLoSimcl2D8pupwiq0dHeGAJFbU4xszlQbfSXvGK2TIbV5PL1p3JmS3yJP57vDYo8NIkEM_e3e_gTmfOAJDczEqlagAnmpLypKQPPnJYeoTdg3NYw7UUU3V71srp2dONY-VOZlZBFpaCLnzoKFg2ORT3rL1S_Pg3_obdTI7PH6-GeHIhmtMWErqarfNr9UnD5jPR2ynKY8XH9HmDT6ogScqql45DIFv79x9wFD9JsY_vVPMPCAzj4e8pQviUmiJqQKOyU5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuJ_odOrLtzR7yQCI0BGLislu4h3tvQZiz-fENELOLcbjl8JwNS6uk2ruMvNg3QmZYW-5PvrrMaXwnKESkrRbJECKPGPRUfXTghfrrSxKGJFya0WMno1uC5AY73-LinCnMCHNernYjjhSvWVWJjYGmlAANBdoyGIwuBKHus8H20cwAO1OBYYxCMmJ2-qyElYkO5cnYek1Ojfr7a7BnY4PSBlbhgxI_XVy92kisIz9ha7EdX9obSWiINFpdJ5BD2cENDCUTmI43MDEM-wxAvj9hIbT4odP_tTZ6ps_iDLKACCjEvTtEyU6qRrzH_1zpNvW555qKa9nSA0jhpLjxzQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEQbB47J2zhG2hWTCRpLCQeJ6XaJ4fg166JIiyPyTJvz1LS4rsSAaCgLebPuB7tXCQa6QGE4I0IiDIZt1vW-CIZgjNO4W4-0Uz2yVSdgfzxQL6QELKqPaN0v0oOj3vW0QRNhaO8PE4I-ZHzAHafwCqmfGSdwe19R8ICcouWSr1KW0N4tjMFV2jpzoH-Ch9xLOzfdM_cXChkeTOdZDFtrErF0ySIqlq8d7yIsh_kESgZnU2U94x9HwQBuFRajCF80zUoaRjSYPUEjQqgX7BdDHFws5ykAL5dhPQoU3n8W_G_EUvxOzjAH9dFJxJkm07vR7mSwR8c-VyMJWPy7KFCFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_Etzn-dRanSaUEc7zrD5_LRqA1-IAMW-wv0El6NjJ2C0NY9Ti-WOvswmAiwalvw975gOvo4AmikpcOyPO6TMWr3edIQu88UWaUXSHLLcC_2CcxHczWkrGU3YiCKAUjRo_TzLJjQoUcejQm9XGbWxPjjLXi0JO4oa9StDX3HYVO1T_wpq9gkyWz-j_nnLTZfq1fc9XeFkPefpSgmbGlU9ejtvJxaMiR7L6J7eTawEFTPIc9EgGm2oZHlR2R_0k3GYf0XtGby-YdnrhDWakCg0Sr1xOPv8UmPRK2QXtS3JN5ZlEE1vSrCt2ofhqYKKyijPT9mwaQv5QibwQFYmYafUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=U2GizNJvDOt-yHNdQe2ajo-RYSOpF6DBElEZ_axcUGzKKgB8IGRpuGb5UiZDwZeK15DULmJAsghyKMHOLUjCqdX9aiA383-q9iJYwPNiZRM2CZNlkZxoRthsUYsD_s8d5PxVytDPQuoyTGtOcxm9ZosXv8py1Aqvag9SnVEFh5tWsVgqNMbPWlLdUZNqM2pRSnWb7-NSFliDYVA4rqOacF_sjXLo3-PNkhoXHZFB92Cc5XfGutxjCDIYzMnaMkgTrSBXd3DCga0fiGSAxwyZ9-UB-8dFZhTSVW0qGSs8XvWmGVQyr2cXOeqnkspvCVv0OGdAXwerMyVngfhk17FmIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=U2GizNJvDOt-yHNdQe2ajo-RYSOpF6DBElEZ_axcUGzKKgB8IGRpuGb5UiZDwZeK15DULmJAsghyKMHOLUjCqdX9aiA383-q9iJYwPNiZRM2CZNlkZxoRthsUYsD_s8d5PxVytDPQuoyTGtOcxm9ZosXv8py1Aqvag9SnVEFh5tWsVgqNMbPWlLdUZNqM2pRSnWb7-NSFliDYVA4rqOacF_sjXLo3-PNkhoXHZFB92Cc5XfGutxjCDIYzMnaMkgTrSBXd3DCga0fiGSAxwyZ9-UB-8dFZhTSVW0qGSs8XvWmGVQyr2cXOeqnkspvCVv0OGdAXwerMyVngfhk17FmIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivlYWsWE8pxcKQ4MkAuOtlN1HCsKhq0xtMu6Lob2-6d9gE-gReQCYgW6UsNYtEiuScrQGzY9nrccwXOE2d_dzR0zp6_-SKv0MiYZlSPnOmMwqf6MIt3JbViD4DL2EOeLlZrDS3vNGk0w8xY7f46xJF3Rdj1vyHmPlbe6iizQWJNGqPcagjVqdbEcAGeoMqGgCVDxNV4wZ4lJ2AciRfpZX4ULzCQwEI9PJyT84JKH4sZiJhUHBvkdJEtWRbXybZP4qdY_wJ_jUe58WNsyZ8HQtzMnSg-IVWJDUZJDzgRv5CvRaZovBAwfSEDuNgk6-yMI26SCWiVjg74nZIFV0TVPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7F2PfQ3YfF3n5lZ1UZtqtc-F7bbC76XY8XbPcxn2Gwr-KdSTsSvftmVqmaXojq8WG6-pCQFFKRasS3Sptvio1uDzKAm9Od_PVVORbgCNeHxO5CjX8wjWWsHz_UeA7yFptZKDPLvmugEWdVKTvKAtOOPFF0iNR4CytpPrHi-Fr6H6ywV-dHkj7M8M5tyWI2voy3Agm4zKWt4UWgK6kQ86rGIQZVnQEYGqbFA0q2gPcSMFteB2yHK8OYt-WDZsgjsWJGN20QxZdYhXGpUOtBC95fuOi7D0iBWUDAmMPZFo5cqo3WOsMhHnzlH2lQXcqmrg-S5fKvh4H9Sy0csE4fJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kALGu3oyk29BmNLzUGIn1v7a1SUPn7cjDgawhmzcVGkBYaiKYq10WiRWyOOwELXhO9gmYVgyd2uuJRr90NTDcD7jHqrWI1E1JLFkTFIkqQV5F-87qvpsQ_lP9XrnX76_Fu7pMjst1aXOS4VggjaChBM3TxG0jDxRTdQF6r_NLVuxFkF-K1FbskiCWqqfppLJwA3H5OisQoPQeTNNb6b6hBhDXqsSdFjjNzwL2S9EtD_8UlH_HJfjhxiRomI6fColleBxxq9tHZuSj-_0EYbW927NA1y_jsdnsyq3T3w2NCHX7U5oTb7VxOuC9cpwpod_5Wploh3QCukiw7NeUVGAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7eGCpndhQcyf2hLAR2ds4W7AMMzcUx2FeXU2qaKvT_rZGBBudVlELU0pFeBCg2UfgGgSK8T1Pj2Uqlrypbev2cDFI_lMRFImIBTj8iYjG5745FnSf5aaFJ78toCnW2Vc1W-bhMbUuuHzNT1UkTW11l2QIqYdxdOMGvxcTOAiSKOW2isHbGoKEi7t53XsIiCooPbczKn4rhPNnkggeV31JGTTtSq7Nu0zkk0FJOzlnll9pylDFs7WzlW4A7QxdbZ8hLBfDbneKoLQjoErklFwm4DkfrXTgFhtrIAan_ZMI8T8nuD7MrJZO3Aco-OJQ2aVXPrKxZIEqNZlRvLXS3Y8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgwsCo5_ALNtpdJGfriHJaJ_AmvGMAKeBN1eR5ouDjFt-YNe97Zqv_FFpc7tkSDaVf-SNan_ex2jYzzXGLjiRNrOmfBHpRXQJNKu2E8zQAa63BSgOODR9c9_e8FVWM1HYQWmXck2pn474Zb3HnDFzZctiplkhTkVJSLhsjJan3zvXAKQiItONWlE_KfzVy0eKGy2jWX55HAWoqv3G8gynkOZCcqAWbBcdT2tvmDbFp38hPDl9SyLdEHKeUGe_KZNNqk6jvW5e0vqIfOpqgPmP_q7NJl_qmo5kfic6ehEH0mxYtk8i5_VZfmhMlTmmE-0E3jfUV_uGeAR_BEoM_kiBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYIL-c0G2IN5nMqgvuktU_0eDqNZ-LlWiR2qpJkjs-8drMNnG6BMe9MH4iQTlXhk-mDeZuZjHVyIMQtEgzSYg8aUT_EafXeE-9GefqZQ8Jdf8kIiz5teFk4livqRV4G-WktjJIV7BFPMJ1G1xm-r_v45zw4lc_8FWeJKKAl19D_x5JTosWLEtV01roX-SQsy0JEtofhqgZgq4r6gugQaoU5bJ7xCRDCdYmhfeqsY7dwwSqjcDuc0rVpxx-5Q57QSeBi1mLcJ3Vh7wgNctE1Cc7LgE5bR1RhHqTorsbPI-8rmG9qXo11U500jeRDCkT3Y6AyiIpUy0wm4J5kGXfnz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV9lR1nyMhMrSONneS-w1iqnAXw1Bc2yt8d5VcwqYMezZav2XMFRyM_lx7uPZLC8HB8ymomMVA0F2HniwmV43J4ffkyIWTVp2GVMMpKiqMBqKQVimUoe_vgJIrDrORsYOyBSEuHTAtGJL927nqQWkNhaTuMU9hvnC3zAGwsS2C9rUDryaLlJ8Ey8IW0ifTOR4HFTAQEnz94rUo0vybqizdx_yOxFyDexAgYHnNTQvLTT_1A0jZY-3T5618cNr7-xa_yz0QJifexHILiT0ouSi8-LZ5H1V2W92D1cBtpqZHp2ajjrd7bumvUa6lChv4oTVbXrfZi-TcTTyaK6HtupeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USdMiBqtxv1o2devQUgOAspG-om6YBYkkOeLo_p6EU4741FHtsytr2NTjqtkcYgyPrjeRJQ4h-SLvI00giO5ecvgnK38v6LR7ivWzm9Yaeg1X-og0U61mcJOYUD1IGmjZbiAEsz7tE4Ea7X7wdJ8fpcPR5jbJuW8qrl8B-7dl7GB98sFC9qA7ha-lYDwfOuVf7eW2l10QOJHTADxqjis0hGWOzdAR2DFll_KifCzNTw4mv6IubGVc3yRV6hauj2am-wgoHzuZPZfob5pGNcK0_gGnGsuFoKHqH96lJL_iVRXktprah9VTto1E6oiN8te9PlOinZ724z28oglKpb24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiS0AteFE12Zw_bFYCajxxQuD0alFaiuxY-NALr0-cFWP8V0W--bqlgSMZDlofEgRH4zLMTtME312MAHRy5z0-rsmBUih0sqYlNEasOxFME93IXckCr405drE3Qz0t-gcUwN_KGUdsSP_K1aj7L3M66OzTm2v36y3uAiT5a7m1KSXeGjTZxQLBRQ7Gf68TQByemdLepQWnWOmqHA7gGVMnzEjC6H1GXPOR0wJmCHAFDBC6yk-Vj5_cEIgBHFGW7MZaOcGVqq5WTWFdZUBmKczGqqkQuFH8R0bvQpW8AsYTsCQW18nTeabsbXAU9jWHAqFZsTdikSFoBIKNNOr7w1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=GnUOoKBP8t1XdQsQ45T_oHA_EI3GP8aZ_wQe3Yqw28YrlLsMcwhLwShdM8URJhcTumaEv-SI0aY-2AC3S_3PNPjsOe7DnHXpU9_F1GyzF01rhTg6XvPCbU9KOThjDLXmT6Ok6HTi75rvR5DlSBxy-_lmPT-XW_piKVXHkpn_ygvGp9WeDzwqiNabumUyMmdkKdLA6J03tLEjRwOErYn9vNGXS7KglNS8gnZMovy8W5MYtfVmbPajSwYFDZTzoGk59e-Sgz3sbV2TR1lcKzxjBbpmoEaJ1BcGla8LmaZmXy6sOMndD2c-jlz6dyFQ3iG0zqtTFkvXdhBqaPySwEANeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=GnUOoKBP8t1XdQsQ45T_oHA_EI3GP8aZ_wQe3Yqw28YrlLsMcwhLwShdM8URJhcTumaEv-SI0aY-2AC3S_3PNPjsOe7DnHXpU9_F1GyzF01rhTg6XvPCbU9KOThjDLXmT6Ok6HTi75rvR5DlSBxy-_lmPT-XW_piKVXHkpn_ygvGp9WeDzwqiNabumUyMmdkKdLA6J03tLEjRwOErYn9vNGXS7KglNS8gnZMovy8W5MYtfVmbPajSwYFDZTzoGk59e-Sgz3sbV2TR1lcKzxjBbpmoEaJ1BcGla8LmaZmXy6sOMndD2c-jlz6dyFQ3iG0zqtTFkvXdhBqaPySwEANeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHmt5hDPTgASZ9BQex1RCSp8qTm6kOSr3ACYyoz0B2ZG5gVri8zRhvnzhNRUfY-0Vaz7hr9AMLbSt5GNosAaLXoeR_I23XC3kTjFZYpq4hyvF1ecC8_7uXpCtNuPMzjbue5XH1SBNerONXK7eXhx7HcaX3Iyp1TDI4IUHiY35Y4c_op3heK_2MoETGsWyXNViNbA4J0DTVqVEmU-zejFuurxTqTQlvrsejHuouAPA5hVel0VGZcyjoQOg_cczMjc74HXiShsa055azVsVUEYzqI3YAnykheiGStBg27LqKDDoodqkvSg8-zyxdqCFXTuaJ4D4IT_T__BzQQYOhwWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ3rCfiIiELSjDHNbDX6qGisaS3cC3GljlKIm1276nkVg1jy8pHep1HaF7-b-9WvTn45w87NLhgZD3a7RWJRw7b0oJ1jzuK5iYSBVUOitRbJqesV0vdjp1qlfr_68t1-4CwcYaHC3GFskz_NmqsvM-a1zo85yMdlOag1E8kvUph8TXCIUmF1fkEexSLC04sT8Q9jXmXugo7Fs8wPkUqFJBSb6BC6heuzLwlV1jaLW0qUX0iIalgqb95CFOsMC0I9JTrVPWpMcistj5iGuH4RKwtutn51nsQfOz_Ji_muFiOWu52z2RZ76BGLWuZCypw09cHDxjdgWuqkGk66pFI_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmuVeOTaVqQGjheQoDSlFQB__9ZrsjtZIYNcrFTpRP2soWVhQE8FN068FfbxrH-m1BwmWrZe1aK4eNYb4xp563bI7M8cHmFvVcTiLUvZHpD_uM040siMc3n6Re1ZUAiuJICQBQc2XJXmHiy-wArHjkTxzjASxxmw5TQCNL_e4kNbubmjjEbL10OZOv_ijhVY83eXpzWop6k0K8m7lQB3rPJJ9WTEo7xmJEfGgzWYP_U8xv3VaPXQ2B7Qja5qO6GLAUaGj9GFg4bgA29k-m99jtjN6Z-3e1aCsOGTcyi2X7tpbgMrnA0cTHCOfDBceUIs-wPqKImGN14VcMrTRM-gyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq3k-G6CRP1JiVtpNJs_Jote4P6zBp6wU9P5_v1lH7D6weN9GJzW9s2HP5GXrw0MO5HQDCSTAtll6TEXPijgC2qxKRZpfgFbxl_oZANAtyotL5LhHqM4W5YINpNzRGH8j76Gliz20UuTG7JSJgH59j5HtraZiLBHV8t-TFd3H6bt_8vflTa18sbZYIN30ikVFNM_y-eMEmLIoZp-VDGw2EnsKJ8T3MERqm4QQrIKyshwMKfKY7zi41p0bZf7H1wZ7m8X-yGtCf3LYNwXNY6CZRYEWVk-0noK4HRK4legBl6CskpKwFJL2ueiMFQ6OcTJIJ52m1sLPP_3_aDG9ezkwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=Hq4z_tAO_-MTQAFRkaFtQWZXst-hzRRVjoylvU33iUMdgYofRrUfkX9_SyTiTd6zMqdI4ytS-mqjFlKTyDsUJwWNln02RAa7ukl5-meIfGsw0J_lKnKvAj-geN_WThVRnV5LsZK9II8xdtR6ZLa6RwRaMTUBK-ZtbKTx4P_OELjM3JkGhdX8KDPlbgDqY6iL2Up3Xa9mWRJ2X24W3q-OUqTAMAZgnOvkew-rXw7qqg5Zjqm5q2UdbMl2QPYuCvZf7-nd8yO58H_y8Dao4n8udtBjQ-qkMWV5g3AghpWcHlAKsy4L2YbQTx5vdxhD6QMNp8C2MNXWIyxgfYdQC9i72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=Hq4z_tAO_-MTQAFRkaFtQWZXst-hzRRVjoylvU33iUMdgYofRrUfkX9_SyTiTd6zMqdI4ytS-mqjFlKTyDsUJwWNln02RAa7ukl5-meIfGsw0J_lKnKvAj-geN_WThVRnV5LsZK9II8xdtR6ZLa6RwRaMTUBK-ZtbKTx4P_OELjM3JkGhdX8KDPlbgDqY6iL2Up3Xa9mWRJ2X24W3q-OUqTAMAZgnOvkew-rXw7qqg5Zjqm5q2UdbMl2QPYuCvZf7-nd8yO58H_y8Dao4n8udtBjQ-qkMWV5g3AghpWcHlAKsy4L2YbQTx5vdxhD6QMNp8C2MNXWIyxgfYdQC9i72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=rw-p_xe047ATfjuylWpX1qjtUDhLIwmMaqN6XEr3ii2iV8QGd7Dat9_yc980nS-1AYQefOBvud4PrzO0hAtVwfuEOPq2rxMkzmTd5rgiZFxT35y0mIiqr_-CHOTsVGRyRivTHIp0fbVHAUQMfaQDKIflf-YhhGTnM-KJ5Akl-rBxyO_r6xXlDmE-6l21-LCRHPJWDG0O3qUticN7Hw4m5nY4unLP5sriNd-atteUpcwGjdY-j9OTDWuQl34po2K2Ri0bRuwLCWJOEI2O0x825WxXoBdsTzcOcYE2g7l3BFCd9ounzXODnwByxPzHbpKYeOci-KeQIwVrbgBddXzl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=rw-p_xe047ATfjuylWpX1qjtUDhLIwmMaqN6XEr3ii2iV8QGd7Dat9_yc980nS-1AYQefOBvud4PrzO0hAtVwfuEOPq2rxMkzmTd5rgiZFxT35y0mIiqr_-CHOTsVGRyRivTHIp0fbVHAUQMfaQDKIflf-YhhGTnM-KJ5Akl-rBxyO_r6xXlDmE-6l21-LCRHPJWDG0O3qUticN7Hw4m5nY4unLP5sriNd-atteUpcwGjdY-j9OTDWuQl34po2K2Ri0bRuwLCWJOEI2O0x825WxXoBdsTzcOcYE2g7l3BFCd9ounzXODnwByxPzHbpKYeOci-KeQIwVrbgBddXzl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSY-6DN6bPUUXgmo2YBJ4qvw2yZdChscAHkl_KvzjcZxkkXxrxWRSE8i6uf4cw7EzKpMqIakgHTBoGoHZjXjkiKUI2P-6LEkIFjsheeoXHiRSSAarQfTTIrltodOcreBYbVhqVS7ZcklOpx5cZ_SHDoqJ674IQ_GQsAW-qnQzdP6vBcOY-PmGIoUwFqjv3ABNmVXPXnHWGnchR_UrxL6wVAFpptsVqkeT-Ef8d-SfbsLm-KwZQh9JJw7tAOEEWhQgq4no7B3eSWdtd-pazbwC5xV2GfSUHiVP3NCZmHrONcpS4jz1rju7Z7bGBfNwDLMmbqotmKgvUE7sXGT8dZcHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJjMs4CPzKe3sRRwQQdpbWyK0RQq_06s98PHRyNAWoRSOnDLitdM7021OpetB_3IgbHWDQp8M1ZgdH42kSMQrtxVK9pOMvRh_HuDCU_o4u3q7womDEdObOsPwzd9MNegCytqDq_mynVS8zcG8UPGsd9rw9Q4YTM_S7F1llDZuljliLd1C-2qI4xiJAlAOKJao8MBIT0QukLpbc5qpzFoLSrQbkElOffo-LEsU591dBxZASij0j0th4zBOMtZyUR5wRKCn1n1NiDgRkxbKTM5EkREJsAcV708R2P2XYI8OZiueaFok9AiN4WqSm3eQBxlB47Gx8-YB3E4nM5MPBc45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l51yOX0VlSe-1I7qdak945Ct2opmygrQ6Ib0fgT40zUShKaTD6nOHOOEET4t29QjqqNTqqctkImFvG2wHeeK5B1eYIgZj3vxIulJmUV5ijD4k1OsGXRBmAGXzH4c1BxewynuzLDJhyO6RQiL5TQNjAX6UfdzQnmCK1QUDBUGr5f50IQKqeKS8qEo9fpmm0a0sQkkPgr826zd_7KMgbl8dYmi08-JoLLgQExva-5E4yfDuKkrVT5-TVq4PEs4c-W1qzGQRnT-RaleAHYi1XpswTR1xEuz7ovfKwj5pxY7FqhcsOgPcJTmzzhLDp-e_LoiDWMtxuPUBiClGUg4VbC5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL5nUUOKwvslcaOKKtn6GTiOEn26UH4h2J2FFJJWB8Pk1-2KSlIpHwu65ZUPCfTaH3l0pCge8Aw6QwKxo_XbhE2bFr4NCKEkj_BJSJDmHDNvakvaqRWNZRCahU84n6izNIrkjVShsgeocvk4uM9DKXhnzUUU_6ABnRocMoUrlT8z-fD3ZfueVM-3GTvQnkPdliIAhQ8KkLKwAR7DpFgalQWlbUwAC3L-G0xJIuVTMifgqzlWa5CaMsrb2Cw9UeCfC6gJB4v60lR-jBG154Kv9An3OlHCX8h1reJ5mAHyg7R3k4XH7KnACE4OCpd6dB9wv1VzK25B1E0fclbvipUU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=l2buPP1AlZej47FGPPq34xky54GjRhHYx1SiGHPeavVoprTkV-_UXJTv9sgjTS7D9VlYIbBlZUi0Zhm132zOeLzZPNH1isfOEL1Mbj8eKFRxpDUrcq0qlb_dwA6J4SsmyDYTCHvaxoM05Pb5fny3Il9xkwV4-D7m6nJWYPirzlTIQQbcz_QTvBtXTWT3jmCLRoWKSFdxj4QrWUKFwpxK4IIUoFPzJO5OIr5Tcz7YxoIslDzg5tRI5ESikwMo5WxaUCyxqw_J4d5YNsyp0Eb0yZq5A5xMUJW900_7RX8dS9p0nqsS0cmc0UMeSA4TBzA-ssEp9c7ODTuy4F2pU9dWuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=l2buPP1AlZej47FGPPq34xky54GjRhHYx1SiGHPeavVoprTkV-_UXJTv9sgjTS7D9VlYIbBlZUi0Zhm132zOeLzZPNH1isfOEL1Mbj8eKFRxpDUrcq0qlb_dwA6J4SsmyDYTCHvaxoM05Pb5fny3Il9xkwV4-D7m6nJWYPirzlTIQQbcz_QTvBtXTWT3jmCLRoWKSFdxj4QrWUKFwpxK4IIUoFPzJO5OIr5Tcz7YxoIslDzg5tRI5ESikwMo5WxaUCyxqw_J4d5YNsyp0Eb0yZq5A5xMUJW900_7RX8dS9p0nqsS0cmc0UMeSA4TBzA-ssEp9c7ODTuy4F2pU9dWuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liFWnH2JuHc5tMQg2-sSo6PnQHBFIIqF5Zs8L4Z9rKfpqvIcfikaEP8vXoQky05c18Mjp_cOfV9sXrXo9KN9s7f51CJilc-scLMWgHy9OlRaf3EsbqwXq60H1H2JjP3Oalj3lOE5-RuiGe2p6IvQFYTiDRLxWRGOxVb_ZuMlVKGJn7PktYLSxlTCm0xe4F_mdnHJrgTWM2Cq1INrozw32aGDCYrwb3EbP_MmUhjFa_uEhlqtUxGwtgA0oyPDvq5TaOYUhY9JDRbtGx43BI9-y-AXkBIUCQG7vHVZCjTFFDbGLaFxlwEIdG3ny1WBpEoM27vTtnc8ww1bElH5fvfPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYRihWWNZ5Wz3DkQTcuaxkCtFcb5T4zbuTeteKhPiUxjY8GdUz1avs5MfwP6HVs1Ba2II1PCgDRfjYGf6nOBpL79bKLp_RZM9HKf47oWmPVHBNvHw3eZedG37SMDlQ-cAFDiJ4IqKS8lHuwy-S-ie2wCvcAG4htMgF5EVoNyJIbPxiS5sOOtdbJ61uQGNVNimOjA2Di0BZwln-YS5XXgOWvQ6WKdVvvjOA53coF3GurwhPIVRRJzPSkZwhydyHbAxW37_s3MGU-lKvT4NeFxQSUB17MI_EKOXrsmgazCBogUJW9f3qWwXHTZmsKSEX3NxiTbZoBDbzF7FbyoIKIkkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=oI7antHMKTaaNmIV2x6FrCBWh47LZvdgf6ZRIwJiPdHpudjka5HeNMdlgn9Wf02DesLX6zsOhtQp_cGo7D9xDolXaSdEV1Vf9uEmAcrFoLJNycSBOrun66H3qJTs07W-QSeLbA7Am3Eh-XRp15d6WztEtQoemXVwjZNo7v0ZYkFggFw2fdxFvB9RyvgyjlU11l9IuKh0NjSYgKFq-DwU2aEBZ7wPrVi8F0uL2ZLEBhPs9zWt6w4bhhMq5sJTA3_qRf-e3MVPXCS-Wt29065rL9ekz9KGuAhZkrBLK67F1qMzZ4Jz5Sg_beR_bFLu1AqqDZzP1qZb-2-KRo90-dKpTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=oI7antHMKTaaNmIV2x6FrCBWh47LZvdgf6ZRIwJiPdHpudjka5HeNMdlgn9Wf02DesLX6zsOhtQp_cGo7D9xDolXaSdEV1Vf9uEmAcrFoLJNycSBOrun66H3qJTs07W-QSeLbA7Am3Eh-XRp15d6WztEtQoemXVwjZNo7v0ZYkFggFw2fdxFvB9RyvgyjlU11l9IuKh0NjSYgKFq-DwU2aEBZ7wPrVi8F0uL2ZLEBhPs9zWt6w4bhhMq5sJTA3_qRf-e3MVPXCS-Wt29065rL9ekz9KGuAhZkrBLK67F1qMzZ4Jz5Sg_beR_bFLu1AqqDZzP1qZb-2-KRo90-dKpTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtzseW2ktPHYgvs-7H7U4PHeGSsoSClS2KkT23TSYgNnFSCkKZP2ZCTgoDFcp_YJ4Mvu5IlI8cyDIz59bFyV9QWH1EVshsE2OZwCaVMK8eYgx6BqRuFnYmbq105co27RnwVTRMnvmENLi9rKD-mJHRcDVwvBOp0i9Hv6GgG_KVArvSpTlJ8UaCdeNpXZ2GHdD6rDTLAAbBM3dEksJnZxKedXj6_w-FrZKW2J_zA0CjuObdeg5nfl52ZrrZbhIr51D601zKkRQ9C043R6XT7IWdv_CFIMXQBF_JoF1YkU9rygDJLPLdpi7VZ6nFGKp_JaZixcfx4TRrrS5ANRrlcb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=UpD0hemj1MAox3MBdqz9ltzFq7uOdhEwU1-3xMa94hl6IE2jMHUnEfajJe0hhbig5eBJxu19c3BL198Jy5HNs8BnMhq5DGFz1UkPG9VWlFlucSTWOgqGnP8BSL_W3UvFRAufPc4ZjpeNed2isrg0fjfYRcG-jcFNh30VO6VzQ9PSRzlhp5GrjdaHh-SKU8XKuDvoAnIWMd5zMU7jRqsvJkpU4rF6Chj24RF73CPTN2tZrdDxcn8Xhi6FquaRnUWvM3mg7n3dAC-4bWjqi-6XMpHwh1rmpozfqq2xi6lBrDjiHP6js8PYVt6ZXyvq28QM-X4NYmDBUVjAS5fJHwPGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=UpD0hemj1MAox3MBdqz9ltzFq7uOdhEwU1-3xMa94hl6IE2jMHUnEfajJe0hhbig5eBJxu19c3BL198Jy5HNs8BnMhq5DGFz1UkPG9VWlFlucSTWOgqGnP8BSL_W3UvFRAufPc4ZjpeNed2isrg0fjfYRcG-jcFNh30VO6VzQ9PSRzlhp5GrjdaHh-SKU8XKuDvoAnIWMd5zMU7jRqsvJkpU4rF6Chj24RF73CPTN2tZrdDxcn8Xhi6FquaRnUWvM3mg7n3dAC-4bWjqi-6XMpHwh1rmpozfqq2xi6lBrDjiHP6js8PYVt6ZXyvq28QM-X4NYmDBUVjAS5fJHwPGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=TdLVabYv_iRz7ocz0chLWn6gl1tW3RdRh8ozwA75sxoF1_92CSZPeXgiUib-KwX3bdiairUx6S8pzu_Mkd4460VAi6g8uuv-LNhlPPcyqjU6Yy61UG0tmYzSlYTvZAVgF7WeG-eiz5ot3gtVP12ypuDEv6zVatMGJeYDkIn5X1Km-IzQCXKifJZL8HH95HnCq8sotA8yr4xsBMNsJUvZ7Dx9daJkgZf5bpcG6INxcB9q4d93tLfgT_ASIJjiKeXMLZqCrd1FoTJTvN7Isj3X8i0QFLs4QAUrv8YhzoRSzSWBfEkVt9fS1iYO3RcIX_IZvNgxmyb_aklU-NQFeKdrzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=TdLVabYv_iRz7ocz0chLWn6gl1tW3RdRh8ozwA75sxoF1_92CSZPeXgiUib-KwX3bdiairUx6S8pzu_Mkd4460VAi6g8uuv-LNhlPPcyqjU6Yy61UG0tmYzSlYTvZAVgF7WeG-eiz5ot3gtVP12ypuDEv6zVatMGJeYDkIn5X1Km-IzQCXKifJZL8HH95HnCq8sotA8yr4xsBMNsJUvZ7Dx9daJkgZf5bpcG6INxcB9q4d93tLfgT_ASIJjiKeXMLZqCrd1FoTJTvN7Isj3X8i0QFLs4QAUrv8YhzoRSzSWBfEkVt9fS1iYO3RcIX_IZvNgxmyb_aklU-NQFeKdrzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=mYk1aT1QV2ygGMh9Q08z4kyM5kFZg9lC7oPRAlXL8kiZUf4VV_nReKNl06xPoR4W3y_Bpj1oQSrehoeokcnP3x1aMLuAsgO9-40-LsYEFaze-V2XY2qW_FZkVeNEOjmjUSMNfhezCi-RqyNdpvCYbIBupUj1ADu2rxCuQ8Gh32DXsjhuRv9Z6KDpx6rXoakioFRi4Q19HbgN8xh5uFekyXkE3MW5IfeNjfdiGt0vnfY_rP1TF1rAbYdSsKM2a5faWM7jpJYpKvYFBkW9JZ0ZPTw93k460flWFUjWGzUom4iB7-JegUXygR7VrX6nn01gvkwcelpvXHzHlI3s_U_C2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=mYk1aT1QV2ygGMh9Q08z4kyM5kFZg9lC7oPRAlXL8kiZUf4VV_nReKNl06xPoR4W3y_Bpj1oQSrehoeokcnP3x1aMLuAsgO9-40-LsYEFaze-V2XY2qW_FZkVeNEOjmjUSMNfhezCi-RqyNdpvCYbIBupUj1ADu2rxCuQ8Gh32DXsjhuRv9Z6KDpx6rXoakioFRi4Q19HbgN8xh5uFekyXkE3MW5IfeNjfdiGt0vnfY_rP1TF1rAbYdSsKM2a5faWM7jpJYpKvYFBkW9JZ0ZPTw93k460flWFUjWGzUom4iB7-JegUXygR7VrX6nn01gvkwcelpvXHzHlI3s_U_C2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=KlOf45wFHlzjbZlmgEZfnP31EpdrCoBaRhc7mGaX5Yy_47FNEwkCRlBv0c2imDKabyVNa2dm2IYSxWd-PqkWM2GPiNgQrhp4fAwHzjsde-CCTvYqF12U00l7r9ReCanbWudiIpPB0e9Cmske1C6mAO-NO6rC9mDnth8_9sKFfoNOIaWQgMYuAd8A6T_X56SSj3Ty2hl7QPrpGoVojlJEKZMz-oos6t2WtEYjQpgGxEGN0vZoNLYzES4ITfOkLwEt6OhCK33ZzzLY1zoOn7sqK8CReOcr1OSHkod21RQRpxyGjC2ySF5dSPCPX9Bk8o7JivQ0BuNAA4EkfeAJpeITTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=KlOf45wFHlzjbZlmgEZfnP31EpdrCoBaRhc7mGaX5Yy_47FNEwkCRlBv0c2imDKabyVNa2dm2IYSxWd-PqkWM2GPiNgQrhp4fAwHzjsde-CCTvYqF12U00l7r9ReCanbWudiIpPB0e9Cmske1C6mAO-NO6rC9mDnth8_9sKFfoNOIaWQgMYuAd8A6T_X56SSj3Ty2hl7QPrpGoVojlJEKZMz-oos6t2WtEYjQpgGxEGN0vZoNLYzES4ITfOkLwEt6OhCK33ZzzLY1zoOn7sqK8CReOcr1OSHkod21RQRpxyGjC2ySF5dSPCPX9Bk8o7JivQ0BuNAA4EkfeAJpeITTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=uYPYVSnDiwewKbElyI6o00rLr5DcykS_Jy6za-MGLXhOjcOk3Obo1YXx86y9Nk8-Sbr_Honklex-LdslDFKl7VFGNDD6mlzwqPm9MX1c17fel-QiMQetbC-tAbkV4kYeB5kgAaznTAtc6PbME4_w1VOVJrm-Qy2QpbmVi2p30nmkNZ0nB_Apv2Fc3chv3w1XwnZ-Mkd1F_HM2b8aPGxZd8gT3x0qxfp8HSHGv8OJYhpwbhjjpG1y2cq6eH-f6kdMONan2ebKj4uAtQzMQ63_GCqWYS6PJBGnI5nuiTi4wFilhpqWgKBe-242MweEB-JLCkUgxZqu9eRJ7hrXkIKmUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=uYPYVSnDiwewKbElyI6o00rLr5DcykS_Jy6za-MGLXhOjcOk3Obo1YXx86y9Nk8-Sbr_Honklex-LdslDFKl7VFGNDD6mlzwqPm9MX1c17fel-QiMQetbC-tAbkV4kYeB5kgAaznTAtc6PbME4_w1VOVJrm-Qy2QpbmVi2p30nmkNZ0nB_Apv2Fc3chv3w1XwnZ-Mkd1F_HM2b8aPGxZd8gT3x0qxfp8HSHGv8OJYhpwbhjjpG1y2cq6eH-f6kdMONan2ebKj4uAtQzMQ63_GCqWYS6PJBGnI5nuiTi4wFilhpqWgKBe-242MweEB-JLCkUgxZqu9eRJ7hrXkIKmUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoJuq5EMnOIzY3FjAF44OqLh90kPq7tDzq76YmIjeeI_JS3HJ2KcyhROZM4gNYoTI1i4Z3LBQ4DjpSYpfoT16kZdk1lXNw-Gm6JlUYXXr4Q-jAXhRKYt3GtZDlJbketcL0aF4YdEznrYwhBQnWPwyD2wooHMG19LBhEkLEIhCMr-_ySuE5PmvqPEghXoQezP6MSxFhKJoSDpR3zBPUF0qEGC462wfBwTALDH8EwIr6MoXjkyDUK10-v2j6mkS5GCrGsNqKmaYzKlRPXula5XUE6Pgu4CUy1WdPvkSrTDe-9Q94DtbdeHdXLgacXNDGf__-d6jQEjlik9o-yxKg5Yzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snc2kT-xczq0jM6qDNZRbxmcMA59i2Lil4lWJID2CZDc5DpfwVp0EFhwpQ2VZx41Jeb6E1LVQfGaV1Lj0TCls2TRX0ddcPoeYrxFOgTG-nkMLOa4bV9otKTU5shOwQvlwysuehjENE19GAH6hNMmT3CeRTkdIt4AMDpXjxeEbUAy-9BFPK90OInVYd5WOnwlcSHKFX7fzeo7d_pG1Um4PAEwGWUmzI71DyvCkStRQU3ns9uDVtnk4xH6CcFGFe3Duu7QsIM5biqcqpcvpYJFYV8tba7DsRCGXS1pA50QfjPhOYwECsNNrsYuT5ckkg1XowHk__4PC4EG_A3J0hub3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3BNQZqzy9xU-nqT9xPGFpDoKgr4c34ZavzSEqAEyZLlyHFWn4moJxzDgnFycM31339gGsUqs6EaUMRJZ-BhzdV2SOBudhH5g959LmgEpC9wOKePc0a0yhahg5prPd1z0QBmpVavEkQfsl8L6UA9ciZF-PYvtbo00LEnFG2TomWESd_LNHDayJrZipROgzanur4JReUizy0-bVdewPNkw0_WkLn-w8Rjcq-OvdbR19fcs06Q8MzJTPAvFnF9ipWBNiEcVRiZfcOdoqBNJOZZ94ZKq7tNOvn3-uu0325DvS_gaCTmAAWymJfAR06iXIYlRiP0f6s-nofZ5sf-fZmrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mf7e22STmf3IHfv82wSG--PQd1ZslzNKa0a9OrjeBDFy5o5lruU1hg9A5G0-Y-7vTgw40myHZCgtXmLhQ7oRIKnGV5tyLZ8pPxEUha-bWUNm2kcV9TiOdciljUrMDwCO9xRejwTXqIxf844H-O6v4emsYvO4xx-uOx1yU1BeOjApLZpEmllyW3lS6BVDMbV4lBqH-SwGMtV632wkrNiQq5GHwy-MjO2aDV_V1GpOXoo0rNaJsD_lJF_QEl-M01NpoD6K0G2Sc0jhxO_PMQUUFtY6_reHRkz_rHOgszpzsv_yereRXaMt1JINRENxWbrLREr-OrWrRK2p3GVKKkQzJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=uJQoX-ygYuribDcrbCu3KnozQv767z-GCujbrbWLmJkPEIiw4DyBdYj29ffknN3GZkEQJzDqMTSQRlMWzXoVEK1D9jbnWXmfiTr7l0gX2SH_5oLuwJ95HTge8DC1HbsXlDxGHN-_Ry5KBGQYxPg3VABKwsTiphhBEZz2eRerouTJgYnKqP71OCgUJAmOqwCmmXIPkLTgjbITwTE-Qmg8PpINi51l3Ps8qkZW_dE8w70N7t-nHDm3cV68s_BXKCeOyaJySU0bbAoXG_-unpGwzTs4mUbVDc0VkajtX53lgrDLVPNjjjwbPlz2X4KPASGvoMBmhs2p0wSTgUvvSy11PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=uJQoX-ygYuribDcrbCu3KnozQv767z-GCujbrbWLmJkPEIiw4DyBdYj29ffknN3GZkEQJzDqMTSQRlMWzXoVEK1D9jbnWXmfiTr7l0gX2SH_5oLuwJ95HTge8DC1HbsXlDxGHN-_Ry5KBGQYxPg3VABKwsTiphhBEZz2eRerouTJgYnKqP71OCgUJAmOqwCmmXIPkLTgjbITwTE-Qmg8PpINi51l3Ps8qkZW_dE8w70N7t-nHDm3cV68s_BXKCeOyaJySU0bbAoXG_-unpGwzTs4mUbVDc0VkajtX53lgrDLVPNjjjwbPlz2X4KPASGvoMBmhs2p0wSTgUvvSy11PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=cR05V4Aj-9qhMuak-91cnfhznHBairwUximAggiFGwCD06drfK-wfwxlVOugS_jvRDxI91Xl0FGEHKggFW2DJOGOFj9mSbqzXNdi2CDUutTLUb0zFX46NlQoIX21FRdx_YxNfhln70momZ5BrrduAwrvR0S7GO4LN4LZxJGz-HN7y2K4a43y0Pq7zvCO5ILe5CHpnMZNRMEbwFrBbXAFPA8XqYiL_20apYiXF1aZ6mhTX1h3sQnGx1q1Ppumz0RQrD6puXI9y4_5TRYgIonRb-JTMmDnV6X5CdhfKJR3GOLcQwdDtw1jPTgMVX3aWzHQ0gPVY34neOTsb0dLF_e_kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=cR05V4Aj-9qhMuak-91cnfhznHBairwUximAggiFGwCD06drfK-wfwxlVOugS_jvRDxI91Xl0FGEHKggFW2DJOGOFj9mSbqzXNdi2CDUutTLUb0zFX46NlQoIX21FRdx_YxNfhln70momZ5BrrduAwrvR0S7GO4LN4LZxJGz-HN7y2K4a43y0Pq7zvCO5ILe5CHpnMZNRMEbwFrBbXAFPA8XqYiL_20apYiXF1aZ6mhTX1h3sQnGx1q1Ppumz0RQrD6puXI9y4_5TRYgIonRb-JTMmDnV6X5CdhfKJR3GOLcQwdDtw1jPTgMVX3aWzHQ0gPVY34neOTsb0dLF_e_kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=buKP7p5GlVICqs75JTgien3nm2uA6s7JA4LCuo8Vp4GRA4YaeFT8f16PmTe10OcwJ51fzN0-da_fxmHkJXcWTdaBLdRoCJHUb6ySgeyQ3413D6tI8hNJUn0qN0Ev-B27-AqT2soIF6_KWIHbp3z5ydkDvr0q2I8kPjGTBjiWF-d6Jsfl2m1_na0T6JkXuIxeGrQzP-4SBXjptpe9p4OGIttQFWo76AuqT44bX4Xw0HoRfCoAINg5tKidIfWhaa5Tujk298aUnJhAJOvQvOYkUxJf2LZhyDegg3Al2p3q_d--eQm9wUIQ3EOUoevKSdheQZfDNKIUDH4K_D8STpKGvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=buKP7p5GlVICqs75JTgien3nm2uA6s7JA4LCuo8Vp4GRA4YaeFT8f16PmTe10OcwJ51fzN0-da_fxmHkJXcWTdaBLdRoCJHUb6ySgeyQ3413D6tI8hNJUn0qN0Ev-B27-AqT2soIF6_KWIHbp3z5ydkDvr0q2I8kPjGTBjiWF-d6Jsfl2m1_na0T6JkXuIxeGrQzP-4SBXjptpe9p4OGIttQFWo76AuqT44bX4Xw0HoRfCoAINg5tKidIfWhaa5Tujk298aUnJhAJOvQvOYkUxJf2LZhyDegg3Al2p3q_d--eQm9wUIQ3EOUoevKSdheQZfDNKIUDH4K_D8STpKGvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTY63YrOiLl5azMVFMlcym4mC3PkRyy910R8tgJaBX8kzcz7FHFsKSQlWLlwk6s5kqEECilPyhmVDcwxabkKYGC27Steu1NuEJbEBCKF5G83eKDYL4n-Yzet1Auvj0R7cycmcCy5oAedAtSZxLZGM_bGLyU6n1FBNO2OBeh2S5LJLolkbo9s0EVl1VHYogl0_91F7CjeOEGzruXiluN2JJicbAHcSmix59jMa9-WX5xz4G-WAD9PzpodSqjcCjwywMqLddJGSZWd2K8WHpGcL0hImoGMpfA6MJ87Usi74274FwSfHhp5Ntl5TmNlnI09T95watx7DkOXMK5dXQHIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=rubin6qggCz8i-njsfq6DaOY78Ksxgrdi6qwo52PEG7Jyb3vSN-3eeGhK-Ux6SrzH4Fl_tQQtYEqW0-1HAqSSZtxDplYGL2VlvF6b4ykymp_6kxfE_NEqsJpeQtqGu3gvhyMUp7PEBGlMMU4gx68Ho-wtf1tzn0Im0IBdzgQNvEBxYm9lIikxwsVsKHjePb0NJZ00lW_nYey-yRR2ehQO9srBZfRTQMfvYdom-VwhM0edI2e8mrLdr-jWSk4ikZh1ks9xheJb2vZLKVNv9WexJzADU6hs0KZ1II_eLbrcj5pRhh8MYTi_gWIFTZi-uDB8ulWeHKMRznToh7lH4J-7FS_CwMqn9VLZ9JIW331nT4dbKv3hvYSLowzgUHg0qVhiwBRd4z5lLQVH3WLJlwnelxrstFKEMmvb0HDaQy32ZWtcgAFkKdJdMEFji5vIZofYM_smq2D-Z0r9eg3lP8ASND0WBPCCz1x-AUtd-KpCYogvr64olx3Lr_vEDEvF8VmT4Ai9vQSMouLJGPtI4FPNxqYN-lU7zWWdDJHDOpyL4eqN-5s9UNyLOT2ra_2RjY2Wo2gGLS6JFe-Mthrops22aUA-M3xA8uJke-XUp8TWT67UGCC3zMNx-u8QN4XXprRiKVfawbt3U0NJ7TZTsTNOHF3q5RH6oDBqqnkWzSUvz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=rubin6qggCz8i-njsfq6DaOY78Ksxgrdi6qwo52PEG7Jyb3vSN-3eeGhK-Ux6SrzH4Fl_tQQtYEqW0-1HAqSSZtxDplYGL2VlvF6b4ykymp_6kxfE_NEqsJpeQtqGu3gvhyMUp7PEBGlMMU4gx68Ho-wtf1tzn0Im0IBdzgQNvEBxYm9lIikxwsVsKHjePb0NJZ00lW_nYey-yRR2ehQO9srBZfRTQMfvYdom-VwhM0edI2e8mrLdr-jWSk4ikZh1ks9xheJb2vZLKVNv9WexJzADU6hs0KZ1II_eLbrcj5pRhh8MYTi_gWIFTZi-uDB8ulWeHKMRznToh7lH4J-7FS_CwMqn9VLZ9JIW331nT4dbKv3hvYSLowzgUHg0qVhiwBRd4z5lLQVH3WLJlwnelxrstFKEMmvb0HDaQy32ZWtcgAFkKdJdMEFji5vIZofYM_smq2D-Z0r9eg3lP8ASND0WBPCCz1x-AUtd-KpCYogvr64olx3Lr_vEDEvF8VmT4Ai9vQSMouLJGPtI4FPNxqYN-lU7zWWdDJHDOpyL4eqN-5s9UNyLOT2ra_2RjY2Wo2gGLS6JFe-Mthrops22aUA-M3xA8uJke-XUp8TWT67UGCC3zMNx-u8QN4XXprRiKVfawbt3U0NJ7TZTsTNOHF3q5RH6oDBqqnkWzSUvz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obp4WxzYqdFkhbse0hKtawDekBc1JnG4ffoRNze8Y0EEQE20a3tJir7vc0gmt7ZcIm5zE7Lb9NbFVS0uRwlnCFjnLTmOjty8uMl-orci_svY7mzzed_fZvqRbz1J2sZ9lFoepeF9Bpz0DXlO5wS_VNBovq3Azrr8V1uS04zyWD0_WWUpIAlPc6BQ6ia1Er7D7n_H7awV7b0p3XdhBCKBONRb8wLfbCiywokvd6hWZGflqaxXZyFxdmq8foDlbXmBScW5I_2eNIMUmzSWP8U0e9q_9SQD0gbeAEpz5qrvpxh3Tg3nQA9k9e2DSjOuCjsirYgMjg2VLctkNle4g6wqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=kd0hyLTr9_Q6WbAhcPK3CmV2SMnzMOCRzljMXOUS_Z5LrH_6d3NjFcc5bclwiCdyqUp1cLsTyo3RTyntx2g-u2mEGUdNbRjTL8OrAcYCKKpzOo8J7MVv3ebLAFQkXmt6Ez13NmW3LdBqHWCSeD6LECYM___GvTNtxGnw12ESwf4l9pPa83LcY1PeObkKNaVS2ZrXhGkkBD3WQ4X5Zv-sWso9xF-dlEK0Zw_JKfqCs0KqliqCrMLcOA4xOUeDhMXpP2skEICxtxpUaKSLSeg2enJhbwTUGmdZD6DZo-qG8K9-5cNjEzu_7LGBp49JP4C8ywc3gyIkCx0Sqwnr4ts60Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=kd0hyLTr9_Q6WbAhcPK3CmV2SMnzMOCRzljMXOUS_Z5LrH_6d3NjFcc5bclwiCdyqUp1cLsTyo3RTyntx2g-u2mEGUdNbRjTL8OrAcYCKKpzOo8J7MVv3ebLAFQkXmt6Ez13NmW3LdBqHWCSeD6LECYM___GvTNtxGnw12ESwf4l9pPa83LcY1PeObkKNaVS2ZrXhGkkBD3WQ4X5Zv-sWso9xF-dlEK0Zw_JKfqCs0KqliqCrMLcOA4xOUeDhMXpP2skEICxtxpUaKSLSeg2enJhbwTUGmdZD6DZo-qG8K9-5cNjEzu_7LGBp49JP4C8ywc3gyIkCx0Sqwnr4ts60Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifpYg_PsH5INJf_p_nsNzeUJJRu2eLVEcFQu0-uEPSVu1YGqTjfru2xGCqMo9F7dF4bhockN0O58dpKTSRDEidoGrZTgJ57cpP7fA8Yi-OGHJKpbSOd-C8g9wp3A5sjMc0H85Dxvh139f184VWVnKV1-2Yg6wEWSUYuP_UHgljIqs63ssPFTGxLdEiaLRoJuW4XCVnMba0sOEv6ejubwZ9EyMRqwLCvpBp9M7ydnzDXPQ3sZYcDoa2nPkbDTVFXyhHCiXa72a_vZ2RV94ArDiWeTNqAxsVWI7U04F_T7uu92iEFZuV1WIxtFAz_3zHGuZbav9tFi0tei-prDZdOQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQuwC7cu_98B-6XTN2heJF0V7BDzPTSbbV8wEGX-4r7_4ySnWoX0dHyQ1dGfT4bZzz0S2iRy7O5P0e-juQbDM20ONWa2dHy5WhhR2j7jHAnSqfsInC9LXXa1S2Qzu35igoudhWJh8Y2-6hkqM0UdjQ6YZ-fvp73ivtvCp2jD7qLdEnHm7O-H9wDYdp_k2iynz4fHwRAQzNJ91WNiIsjEyH6sq5zlCzWwNnVFJcaWzPSJ8Rj5RWFvmY78XerRd7Hd4SwbB4-O8gX7jHw0dGpkRePqVxq7e3cN4d2riAFnRNikPuup7Ed5Q5ZjARtwJEzICk9McDTQW-9wamSBxdoaZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmo7lG3x3zQ4GHcVn7X0dhhfpRbTaE7fMIyvjtjfFt5S4qjik0Zekg7-IZwsvHgbrJX83cwPl2OFduAQ7yLXaFrWGXDg0XFm6NGpXRb3CODDmq0jU38UUhh6qBjsGtnIa-Lj_wAY_0XuzYDftwIclD4DH_9rketasL0nYuwqAlIyPZb_-vcmDxWVMWSWY7zsaI0DVWvEs8worsAJzGu76fnK_wToi1daHauOnNgH-u_07WLLKHov0CH5k6t7C12NBKdfz89v7xNeNPp2y5a3OezWDq2h0KtVaYT1Z831r347_UJ8TqzSBek5PjsKiVC6KimFP4Pq4lAvLQF8SDrnVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSQSCacpuWfDCME_VlpV9KUuNwioqodUfI0Melni_o-9oXS7-ZSIkHRvc08DD0vQwmbmT4M5ZsuHOYuS2z9cl12zZSGiLi072SZtTUsRQTkBMid8W0E2ECqhbC1_i1jLPk16q7sjnfAlqu-iOeYBVOObJkKo_WcfsvWqXQivbNyqAMpxKVqihWvtH58pu8YlXTQ37x9Bxzl5ZkABg-hDhLlsvo-fG5APdWA244yf-JIEWOitiikzR0s3KSSeQjH0FArU6_WzqW7Sz_Nvfx4kRwTvcWf9T9zP4WtfJl0LmYtM2limDuqqtBUGf7vL-nTy6pU88Cv24od8XOR4XBpm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpPg6zj08jKGD0Qh5H2pIBjbeO4ptg13mHn0bJQ8O_yGFSOG1vUxSwQRuY41j7Yht288BsWUdBooQCbHVZRHi-nAo_ikQWdkxZy4cWT7kHa1IM9yC_N-34FkYoINFz8hHpjot4-a9L6S6Nbja4tdS6In2kBRye8WKtKLgiYmN7W5pU6VwSG1V4_rCqZ3VyfLbMohiELQPXZSId_4HMgCb0xmIBaeArGQE80wYmkvj4SoFXnZ20Mc7rAhtoaiYChRrsK2fP4SgiyUBAG7ixifEx-VF-ih-1g_ZJXUkh8hj-lZra3ay50us8Lt3Ggrv1KUvIFJrdP1nxQyDExjVeAnAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8e2hypZu2sUPKMUiDqUVcT8rchFSxOnYDHctAfI31TXEjzJP8pQTdOU41zuq4zo8SiIQwINLjKM10rmm5iUQ1G1GtAJUwXgvFGS-WU2_D1o4Bhbs1z_A-n02EAP9GX9So53QorXwAAIrNSvveU7xpXxA6e5JGvNJuwyAjtyd0WDlUETHQGBUwTT1Q6Tqo13vaEPcMsEkiaOHkkQ84IE8NKq1d-CFhOAJAMsH8AS0fn2p0wCGDJ28MM6sNH-SLmCg_S4Adu-zQnzr4PMaFCdAlMlGM5chS6U3mjH8drQ4ICBS9iq1gcCMQ9RVmGbZdzbixFD0Cu8x6tTS6fA2FQ4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NODIW8-lvHjAcHwSZLoEQ7EQXPKTLl4QeaTypTUA81xPVWYOzkaHyTOhWNEIsJcyRzLQNOs02MdXCLhvqf-0s0QvVmv9Ibl6PwKKgQm7I-ZUo1-YmmeK4yq44SLwtmy-CKeRRHwWvqK3BkaSLjzAZt1k2o1jOpbyP7H8XT5p5fpaAWaT_vyTXNPnsC2kh4v_0Xrc6MgGggjacV3PDFBuKzatSIPafCJPB1cID6caehDZrhqPI7uKWyXPsuBhvKBOQBhAZ_RYsrUun6cElqzwtVjYxCUYHQRgN7-ZShZL03xKcPC0bTdTUgu1GCIC6xrrxM_FQ-8ZFv9sAzLAG2F_og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=hzIYg15lj-WNb-hBGou6D1b3BG3i2h_hbhnxQcG4_nJucAcho_S4tmjlEP8gkHVz6WlnmrAsu0C5RHFhsug-fTSG-rOjTvn7Co2sUUirEk1LVz5bLZBpzsUXmlnqzMiKndKDK2dXLSFPjVDsdZopCx1BWdhudwJalgnBdx8mvF_efVvhNFbj3kh9OMc9dy_q26bu5db3NkBEUvVBddged2ym6xtUwCY0sSbuLMHSQo42kXQ0uyTjURBxAsdsMTIWI5yBvosoNQAranazvrOa91Wt2CdBg5OFFlBUrDGKUo4s5N0nHfhDUCB5L-XDlFzEa4Gzc2umhpmb27cmlx1Guw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=hzIYg15lj-WNb-hBGou6D1b3BG3i2h_hbhnxQcG4_nJucAcho_S4tmjlEP8gkHVz6WlnmrAsu0C5RHFhsug-fTSG-rOjTvn7Co2sUUirEk1LVz5bLZBpzsUXmlnqzMiKndKDK2dXLSFPjVDsdZopCx1BWdhudwJalgnBdx8mvF_efVvhNFbj3kh9OMc9dy_q26bu5db3NkBEUvVBddged2ym6xtUwCY0sSbuLMHSQo42kXQ0uyTjURBxAsdsMTIWI5yBvosoNQAranazvrOa91Wt2CdBg5OFFlBUrDGKUo4s5N0nHfhDUCB5L-XDlFzEa4Gzc2umhpmb27cmlx1Guw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR46Fjzzh4bZX2Ji4m5VJZmNPTcG2bQEfN3Hgbm06_jmDW6blP-5GBHlrj6BesOTdD8C5Jca3eMEN6afGPGpAURYllJd_NiBbwMZnVlfyeeYVwUGdykSrW_3DsNusqavqm1h2GpS_ZrBAapFCYzc-yVfV8WuHsSJn-toNfRPdBl1D7-gLZylZDAFqrvnH5gIWRwnoyXDcJp4BNi_GDppt_VNN9nE2qVb9cCfcgNdohBHOfiz-ohxpA_qeZmx-f1O_Ba4WjULlgTJx8k0bvrAR3L1_4K7XfqQS3hOhko1vI3VP-eizjFRd2jQkkmNKds7WnUII3vWhuvLdjBQLa5P0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drIQqO6Eup3mDbkGet3kvZPfmC3XYeylARRD4LPtSYAZ4TXHRuYR7SjZ_KDPvEorMD-M7RA_k028Q1qyN3tTtmZbZctDiySlwmyIjJZL_2VoNGKle6-fMB2NAcpqCa55_cWEMyHnxX0BUDi5Lgr8fxiHJWmyxTGhJdDjLztAT4rhqDYWMNYfw1RLx-qnIrmszeBycTXRkaRGHgxJCODXmO5GX10JelVLZmLAkZtwCiv1-g25nHy4WPtlg2JI0M2mxM3DjkjD6DpiYlzzsnalmMWNOVABnfokvhcpfXOU57KALXJ_LbQ9vD091tUBpmvr8wEAflXrb31qD-tFtE63ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=lNxQCMB7HF5QXF2nhCJizQQaa2rTecc9bbVmGPSdnIYmrXUn6RxzGNq0QLG5dwhMqK8ufe6LrGaWxaim0tlW4hUD0AEXYxX4E0d7iQKmdGfEEfIVsFEfYGSB5o9Ga8OXAMbt_3ZjQYXwjBZ988XhJbooOw1nlLJm-7Ftp8XXTnk42-d30unONZHk6SghpZFR58kGoFy7tSK__JklRnrSbqm1GWnPisLG6Zy-5ztZcUAVOmlEn7ahB0uvOH2jjIQX0CrtgULF6_Z-XVrKkJnX_ylAsWMsSeAHB0ol7BJYKFGdOjhWkA4wBf_RqFt_wZ1mhv3vXocfo2j1x3L6YpKGgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=lNxQCMB7HF5QXF2nhCJizQQaa2rTecc9bbVmGPSdnIYmrXUn6RxzGNq0QLG5dwhMqK8ufe6LrGaWxaim0tlW4hUD0AEXYxX4E0d7iQKmdGfEEfIVsFEfYGSB5o9Ga8OXAMbt_3ZjQYXwjBZ988XhJbooOw1nlLJm-7Ftp8XXTnk42-d30unONZHk6SghpZFR58kGoFy7tSK__JklRnrSbqm1GWnPisLG6Zy-5ztZcUAVOmlEn7ahB0uvOH2jjIQX0CrtgULF6_Z-XVrKkJnX_ylAsWMsSeAHB0ol7BJYKFGdOjhWkA4wBf_RqFt_wZ1mhv3vXocfo2j1x3L6YpKGgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=l2KbiLT-WseQwLBNOc2Fd6fhOCoUkfxsQfvamFdTCSJ-vVuKzWoO0-YRmiSJ7fzHUKMp-4bH3oR7DKi3e2KWpH7P0KbVfKxKbyw1qaw5G0iufd3HJ3Qy6LmzYqdnGJHsK0qtGzVSeO2Heb4otLS6jjURpLM1TQYKXRNTNfUpWvdZb03g0gopfe-GSJ_gVf1YHsQiqRhu-ZdRi_d4KZWSfkddGtc-j6FVFdTHYdOqOg5SQ1cTJ4eB8WWbFg06b9TgZMp3t71dy56HrQAFn0EoisQ0T4pBeldp6qeVnkAjq0JIArBdNH6KNYe6YLeukWfs-zSal7X922chCF1BXNag1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=l2KbiLT-WseQwLBNOc2Fd6fhOCoUkfxsQfvamFdTCSJ-vVuKzWoO0-YRmiSJ7fzHUKMp-4bH3oR7DKi3e2KWpH7P0KbVfKxKbyw1qaw5G0iufd3HJ3Qy6LmzYqdnGJHsK0qtGzVSeO2Heb4otLS6jjURpLM1TQYKXRNTNfUpWvdZb03g0gopfe-GSJ_gVf1YHsQiqRhu-ZdRi_d4KZWSfkddGtc-j6FVFdTHYdOqOg5SQ1cTJ4eB8WWbFg06b9TgZMp3t71dy56HrQAFn0EoisQ0T4pBeldp6qeVnkAjq0JIArBdNH6KNYe6YLeukWfs-zSal7X922chCF1BXNag1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6_PbCm0FiZzL0cBwrcnvWaD-F0omD_P47dEsz7AtZfZ-ahMTkvuS5svZ5CQo9zTw2tO8Wd19VhdomB-9Y1JK2v8rInO_1RDuO6i9XhzJav5W2_kHYLWqaKcg1HCuiku2xHpIteI7qg_FcwwBB4MxarsWBlfMeZQUnnywfC3lj9_C3yKKD6NstsJURjip2N1IdVpTjviXlGBKT31WqUpcNBuZZu2S47mwIzOD_A_91gcNosrNZRWedg87nFmwRidkBoJOVlXc6vUtVy4yGyn13nWxwGmc1dbip4Z7WN3IYeX0TDLrFDP_2dOTJd3Zl6kh3uvMf1cwm5zgVC-xvHBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=ObdEYQszq-94Ffa8XPAmj__WswoY9etpUloP01RVc_OYymUKKdZsA_ofGQ2G2Tjf5ENhNGtTjMVN56mHdoyMbchNzkOEKRR6pdR9E_i5d7c997LltsKML8fsdzNK27Kcc1foN6ZUIU4VUz7qqZSHx4Ml-5qgBmz8wa-5-uShQiEK8Equ7D-sXVdAZIS9_CKldq3WhEFvnbv6S8RDIWX3OVOoaScq7EPRjsWthqUuZLTEGsmwhpW86FIudI84rU_pOPs084kKa74V1L1RNZJTi2H3ebJtXlGvfNcdz_S4D70WkVecGmtHK4Lqd2m0Bc6UBI6gl__daWnPYI5f0PZN4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=ObdEYQszq-94Ffa8XPAmj__WswoY9etpUloP01RVc_OYymUKKdZsA_ofGQ2G2Tjf5ENhNGtTjMVN56mHdoyMbchNzkOEKRR6pdR9E_i5d7c997LltsKML8fsdzNK27Kcc1foN6ZUIU4VUz7qqZSHx4Ml-5qgBmz8wa-5-uShQiEK8Equ7D-sXVdAZIS9_CKldq3WhEFvnbv6S8RDIWX3OVOoaScq7EPRjsWthqUuZLTEGsmwhpW86FIudI84rU_pOPs084kKa74V1L1RNZJTi2H3ebJtXlGvfNcdz_S4D70WkVecGmtHK4Lqd2m0Bc6UBI6gl__daWnPYI5f0PZN4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=VxSBODccGaFaUK5jiD6s5tf6GbXbLR608mZAawwUJRAq94QG-92PxG3C_CIohCc-ylePC1EbaRsBYZdFys52kVTn04y2assvDDjqorELMwL6fII_bbfHUQy4WVtlcSnQ4KtZRYNlFZW9ucg1SMf9Be05ZYLnNow9UsWiUyveB7SKxhMQKHMDZDA643jtpZcsfQ9PNb2k7MjPRZ7uwVdTzPyAO01rOWSS2L_lfxOicO72qAD2ObdIjvY8DMRG6HuH9UObHBzVsavSUfgVZInIeBUicbJeUfrKe99m2dD4gBGOn_QDkFe3SHDsQR_U0YeaFcn-nN92tbOfKDFidUyEOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=VxSBODccGaFaUK5jiD6s5tf6GbXbLR608mZAawwUJRAq94QG-92PxG3C_CIohCc-ylePC1EbaRsBYZdFys52kVTn04y2assvDDjqorELMwL6fII_bbfHUQy4WVtlcSnQ4KtZRYNlFZW9ucg1SMf9Be05ZYLnNow9UsWiUyveB7SKxhMQKHMDZDA643jtpZcsfQ9PNb2k7MjPRZ7uwVdTzPyAO01rOWSS2L_lfxOicO72qAD2ObdIjvY8DMRG6HuH9UObHBzVsavSUfgVZInIeBUicbJeUfrKe99m2dD4gBGOn_QDkFe3SHDsQR_U0YeaFcn-nN92tbOfKDFidUyEOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuJJtt-UwFFU77obIsIWRct7foi_y0BIV8mt0b2dQsilE6JI71TwCP_uKkNUjqZGZFE8lryAdm8fp898RreLzdWv8PBhY7HQ07Lv4RBmp96j4AwQ-uxoa4OPuntlO5LdvGQlUXHMGwA7n78h0VQ7EHbYQsmseUTMCKdRjlADJ9le76dXirlP4G1OCM5uVG6wIt7uVL3kG4C1fxN237Xlpcq5yD34PBKHhUsGUc5YGmx9jRm5vS7ZSl5RfbEyTzk3OVAg_sOapBD3aufOiNHl2DtpS0NgK6hAMr3Kg6dG7iTkVJEB1VGivJ9NN5jwbbmBBkScUZ8eOxxdLAh1c27AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mG-6FWtLhg4SNmVgI7bwIaQJRW-v9mXc5YCMyv82slfNq9vwtypMDpqrs_Q25U2iRockSaVTAeQoRfXOBS4P7VYsw0xOJAmzcISW6PBqHSz83kogGCI9Ms3qLPudqbZd4HdqwFmd0W_U-3V-ZQ0NwEgPYHFMdcyr1X60ABPpZivFxXsovqEdJeY8MGhiAn9onK6uHlfCx7wUFiEyDVviIyE4prffpdu30THf4QgIEfe4bEYUGSTU8t5LXFtq_VBaOFMU9Oxq5XOssRytb4zY5ZpnTSUWveFYbCLaiWQRiYhRm5aMbRLGy8zbb2AjbIMrJW3Enuc84Nb_z13ZGWnmVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPbLHNoVP3CLN-bVCaXnIevJIhh3maGuEJOWx8LJQ5QagUJ-lFnxwL8WmWD7VCmPy4Q0cn-18IzbIYDd0KADanyz-VScqe9LhKclZRj1GylhV-kp9tbWnABYoLoGP1v2PYTWjeMS1o4W575819WhfQXxEnA_n3cSrmxWSQ-QH5MQifw9Xt9Bo4UQ5KWnmDE9nOyeAyf3Z8vOqKUW4HI2ames4gFCxXN0X9vVGWX_p5fOPKFCYw_LrLg3FKbP1mccMyj_OYpZ1WxcXtAohV2x0N6RN1Nw-127y5AssZcJJyT4L82LE7WAuCTpD7dIUr8-cn82ITGjH4O8S3PBSaOYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPjQkWfT9yx5xNL7_xsCpdY-3BQsImxrglyFdKm-ER-N9QjjmVcQ7Mg3hA4SRHvuYWyCwyryRfq0ANyybrxH_MpOL24alqYjxmPjew922_eBgo9DBQ7hXwGOkQBNtzgLoTRdLTPD6M8UXwtKuIzBHzpw3gSClgExGotHLzQz05rv5i7pCR1Q2qFSiWlv9Gll1kM1y_PvkchsYUTwrSMleprfr-2x3WjWWU8r5u8LvaqfYE9Wsz1hUMcPoD66VVyQzYUKp7qf2GuNFUSBge-z3U2cejunv7TDYQgwe4xhhNNm3VYlpgEhDk3geVTSbs2fpWiIqDGGSdC1x60uRhETbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=LskqDN56Ivk6EWH7fCSDM6E4KzCX-PsTJmMXFyxWvI-nxGgYDJaey8UVJLR4XlugDaElnBO2vQ4JVsdn5UzOE83LuCk7LkV-4F5E28Brrr4ygZNzJknMo4FCidKl-q5L5ZzRo7HHGqMfuabKbOFqRII6-T1lNMITyOvGpb4vj9vSnN2zIbK_XVHeIQkPe2BHMsrmIqLwSpkaJ8t6V6beNu072J_vQuvZEf6eVV6TRLCzMntTpje2B2y0Stp1_DfNIDTa4Vz0ep2vfmXdPpH9tQoS0ulFvlqI8YA-p4tLcayunSnxSQG5_uPGlwL8oRUfahN7LmgheJfZa4fGzCPFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=LskqDN56Ivk6EWH7fCSDM6E4KzCX-PsTJmMXFyxWvI-nxGgYDJaey8UVJLR4XlugDaElnBO2vQ4JVsdn5UzOE83LuCk7LkV-4F5E28Brrr4ygZNzJknMo4FCidKl-q5L5ZzRo7HHGqMfuabKbOFqRII6-T1lNMITyOvGpb4vj9vSnN2zIbK_XVHeIQkPe2BHMsrmIqLwSpkaJ8t6V6beNu072J_vQuvZEf6eVV6TRLCzMntTpje2B2y0Stp1_DfNIDTa4Vz0ep2vfmXdPpH9tQoS0ulFvlqI8YA-p4tLcayunSnxSQG5_uPGlwL8oRUfahN7LmgheJfZa4fGzCPFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
