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
<img src="https://cdn4.telesco.pe/file/hziKWeiA2wK22W0eCCwDIfYEYvGrN46JQv5JJTNpuMkZesU6G1spW-Uq0CFj8I67KPRMvPi5uPOB6Bl-tM2qWXy1z2w2wFc_ghkU8jKKU2yyATISBA923Y76mBimrlSnsPV2EI57QQBAsKWj1V8vXoBb4F3iWO6i3Et-92tnw3bEivn-MHQGja7W5EOpsFCtSiBNA1Mlvs38BIXMJNcXYv8-Ib40jzoYdznJ5a8TR7PUxPWW65UO3aNmVYD3uTCGVeUwY8eAXTW3BxjJzcA1jtecTcLNTRoHJkGBwqW9R3IiM7i6-13yFbdBh7BZHzNPUPpvle6pppxs7WAg_KLMZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 18:01:04</div>
<hr>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp-IFPpLYLD6EYUN64DvswImvVuhq91JoClI4-zw8rXJL3hvZbiuuRpfrYhBkOcxG2gYwl_ZU98LSTH7aRgDZHGqRxss0axx1fOPPFkc5dDJmB6PDsXEypN8ZtjI06GRrYxyLmJJxUIEI79rCcF-W-rT-Ub-FVCMMUtfjn1pYy-LCkqST4dgCam6bchoovX97ste-e1CO_UAeXXH0X8YAZ0v3E5Nj2YssQ9_C0pyFGkFnXgbwcaoEfGnQH2LFzdZAeNqpyeBDd66oFW2rD01tkdAGX8isYX46qrKh-fZwxQH4CWyT9dCfgMQm96rCDmCyhJ6otkrwAYIvzRNhX_mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=m42MWXHAEWCHTqS2cF2gNOGt3uHT3URjGsGSXttOE2Chx_n5nCGnDJlMabVD2d-0SAJdZFeRIsQai8fxSKxE1N9mXHoNkD-0pOuOM0alm6IwsnJoWXb9TW5ZfcuJkzG4o8ieCQg4Wcq2QcyIpsAbrU9lXbEdTZcwT8HEbbxYrBluptcBUn5FMh0QNBnuQZwO2wVTihegIIHCz220rQG3br3GPcOHZE8KsrGzqaIyzrMsqyezGeW__0vK9NnNQUFel-12_6QkwtSuUYTUSvmj7PiMMGlnZg4Or9AQAiLZMk8YhLKqINarNWdvvnCJCnWGDCNI-5VPOpPUDyGbU6rquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=m42MWXHAEWCHTqS2cF2gNOGt3uHT3URjGsGSXttOE2Chx_n5nCGnDJlMabVD2d-0SAJdZFeRIsQai8fxSKxE1N9mXHoNkD-0pOuOM0alm6IwsnJoWXb9TW5ZfcuJkzG4o8ieCQg4Wcq2QcyIpsAbrU9lXbEdTZcwT8HEbbxYrBluptcBUn5FMh0QNBnuQZwO2wVTihegIIHCz220rQG3br3GPcOHZE8KsrGzqaIyzrMsqyezGeW__0vK9NnNQUFel-12_6QkwtSuUYTUSvmj7PiMMGlnZg4Or9AQAiLZMk8YhLKqINarNWdvvnCJCnWGDCNI-5VPOpPUDyGbU6rquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=f7fLfgYFlJalowTZgWZcTJZN-sSTZ5sESgQHdCeGg4tNiENL-XkIRvA6B6uEd7efehGU6ICJCJ4oO_HPvjf_Rr_OP7vMuNkzTYhg8ch68cnT7Bs7o1unjDDvJVHK3gmZXWB92q0PujfdBUubJNak2pLpqwRwpRnp7WUYjtB3zvOAD6g78Bfuc8Vd4-P5WMG-7rV7dlCxSei4QLs5dKTbPtnFUudWm7Z-NV6bNKHWbXdM48cnJR9_OoXbu-8qXSmDxWQaV0qUeeL8rNPPjRAI10yBLyz9i88VMfejb_4lqx52kmf_aYLh21FaR9Lh8EhSJX7u3esrh0B2S3XzlHTgww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=f7fLfgYFlJalowTZgWZcTJZN-sSTZ5sESgQHdCeGg4tNiENL-XkIRvA6B6uEd7efehGU6ICJCJ4oO_HPvjf_Rr_OP7vMuNkzTYhg8ch68cnT7Bs7o1unjDDvJVHK3gmZXWB92q0PujfdBUubJNak2pLpqwRwpRnp7WUYjtB3zvOAD6g78Bfuc8Vd4-P5WMG-7rV7dlCxSei4QLs5dKTbPtnFUudWm7Z-NV6bNKHWbXdM48cnJR9_OoXbu-8qXSmDxWQaV0qUeeL8rNPPjRAI10yBLyz9i88VMfejb_4lqx52kmf_aYLh21FaR9Lh8EhSJX7u3esrh0B2S3XzlHTgww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ZnE4dY4ibWaGHrO7Pj55jNwfUNuMPlf7BUxtWUaids4v_cdncB2v1Gg3xCsA_gnupUL-4FIwWpkySNbRNPGYlu5faVS5quRx1sMNdkK7Cz5Kc0heehWh2jVzE60kOX-4jVwwaJWJnkARFf_Q2DDDGDoj0bnJPATQkpk1Yx90Hcnn8j8sw6oDN_0i5TYmsn0NOWjl5JcW3mwS9oN_QgvCGzwBhfoZJ6L0ulJYaMfsMSaV6jL1Z1A7MDCmOZ0-rNKSkRX2YAWH5uhkr5XnO2q8ByfivRF0Tu4C4Af0egd36Pj2q6tXkmOIagIo6qFG8YvAZdyTFpEkiYa-CFHXTi1Cww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ZnE4dY4ibWaGHrO7Pj55jNwfUNuMPlf7BUxtWUaids4v_cdncB2v1Gg3xCsA_gnupUL-4FIwWpkySNbRNPGYlu5faVS5quRx1sMNdkK7Cz5Kc0heehWh2jVzE60kOX-4jVwwaJWJnkARFf_Q2DDDGDoj0bnJPATQkpk1Yx90Hcnn8j8sw6oDN_0i5TYmsn0NOWjl5JcW3mwS9oN_QgvCGzwBhfoZJ6L0ulJYaMfsMSaV6jL1Z1A7MDCmOZ0-rNKSkRX2YAWH5uhkr5XnO2q8ByfivRF0Tu4C4Af0egd36Pj2q6tXkmOIagIo6qFG8YvAZdyTFpEkiYa-CFHXTi1Cww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=TvWOLLfIEy2U_vkaA4KgEG_FL-Rmz1qDHMBueSPNyhcCoH_wn7W3yseuC1fSdnlCHeIEHKUHbKYMsUGxdmx_UVRJ551MB8L5IrvwndrOcLxPLlOlQRYXCyoh2LNzrPYbHzm6uQPSe--hi9ouZHBuMoEiXNG1LNqKkse3_A2D53l7k615cyiDye0E9pUSYdyo_HH3yt9jWjf1mQFO2uob9YhgK7jUqfDLR9VWXH_mTY5fo49SIXpCAEOO7Lrh8JstDiVXLeiwPesrUvpxhWJFv0fgxJIWT6Bc-25kTZB7DMG83qmSMaOlFzJk8KbMbd82WfqeKh3o86ODAV_E0XJgbKIM8_bPGZnAoclar80j--RXRZRvzpwdeeYeE3gMRxBHb6nTA3L1hsSlyS6ndTpUCM4-IN8VStPhljZzOMDdLqmskVSDEI78Pn80PlaFe-ytZgka8Vu7AOfkZ1ruQxrhd-HgBVTBTVTGpUpb3P8HCdzVvMAX3p5nvoH126sQBhzpSA7hogMnExlNKdvF8T_-TImxqOEPe0XYK-DHvIIqKExGoan9LRfIB8RyYdiq9jAuSoiFsKoNYldSJz5r0d5JwepMRofj9HrTHmeKKV-3sA6yVWH7R4NqgKNj6pfWrsi-h8peGIQJNDrLT5PT3Vx0QMRobqMTl368Kuxfjw6jv7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=TvWOLLfIEy2U_vkaA4KgEG_FL-Rmz1qDHMBueSPNyhcCoH_wn7W3yseuC1fSdnlCHeIEHKUHbKYMsUGxdmx_UVRJ551MB8L5IrvwndrOcLxPLlOlQRYXCyoh2LNzrPYbHzm6uQPSe--hi9ouZHBuMoEiXNG1LNqKkse3_A2D53l7k615cyiDye0E9pUSYdyo_HH3yt9jWjf1mQFO2uob9YhgK7jUqfDLR9VWXH_mTY5fo49SIXpCAEOO7Lrh8JstDiVXLeiwPesrUvpxhWJFv0fgxJIWT6Bc-25kTZB7DMG83qmSMaOlFzJk8KbMbd82WfqeKh3o86ODAV_E0XJgbKIM8_bPGZnAoclar80j--RXRZRvzpwdeeYeE3gMRxBHb6nTA3L1hsSlyS6ndTpUCM4-IN8VStPhljZzOMDdLqmskVSDEI78Pn80PlaFe-ytZgka8Vu7AOfkZ1ruQxrhd-HgBVTBTVTGpUpb3P8HCdzVvMAX3p5nvoH126sQBhzpSA7hogMnExlNKdvF8T_-TImxqOEPe0XYK-DHvIIqKExGoan9LRfIB8RyYdiq9jAuSoiFsKoNYldSJz5r0d5JwepMRofj9HrTHmeKKV-3sA6yVWH7R4NqgKNj6pfWrsi-h8peGIQJNDrLT5PT3Vx0QMRobqMTl368Kuxfjw6jv7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=CRbA9oe1eXeCSz_ytIQzA9lTz1UmSfYGWRXOm6vYiy1BkjccXBoPcbqkwiI-5-7vxrCkwtmSMMAKSZcUnRdd05VjWnGfb1zITElBmjpialSdb80t3qvNBv3IyCYisAtGcI71qa-uBVgI9WD-HS5p8GpaKiXQWHMUkqZ7ZsyYW-8SHxiEit9TZWceueB5JMoacY4BmfR5wjyG_w4b_0NODWdAnOq9IO_Ll0r1-Lex1OnhhA_BdhBoQ2vkJy9w9VLfTVSTHLzt_ehh7UKSKdkEJbuuaUHLJybDV4qx9fcV7k69YmNHRuBfad2C7Gee-KEG4cn6ber09n_UK7HG1DlAuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=CRbA9oe1eXeCSz_ytIQzA9lTz1UmSfYGWRXOm6vYiy1BkjccXBoPcbqkwiI-5-7vxrCkwtmSMMAKSZcUnRdd05VjWnGfb1zITElBmjpialSdb80t3qvNBv3IyCYisAtGcI71qa-uBVgI9WD-HS5p8GpaKiXQWHMUkqZ7ZsyYW-8SHxiEit9TZWceueB5JMoacY4BmfR5wjyG_w4b_0NODWdAnOq9IO_Ll0r1-Lex1OnhhA_BdhBoQ2vkJy9w9VLfTVSTHLzt_ehh7UKSKdkEJbuuaUHLJybDV4qx9fcV7k69YmNHRuBfad2C7Gee-KEG4cn6ber09n_UK7HG1DlAuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgwEm9Q4IwAMIWJ2eIrYpZ8KTYKw0O2SHAJ_VlQWbc1sSFk2sxgecz4nN-WgheF7OASn8w-ROE0krBsnPeH7wd4-67ArT6sLsPdpQwd9NKdC7pyjPdLr8FDoMmKaoF20OugCZOKYNlSTuiZnzm7eGpAWy-NiOxuCDtmk2bd95L6tUMd_W99JhpV5GXHXVLorI0cIwZ_DiPeUkiJGfRl7If_gRFoSfzQuy_ZXF1O1GzLOMzXF49MvJ7BXc-oF8SqMr45TU9L9OdvAd13hsLVRb1UMaXohn4PcXXlLAukShVWFgO8nTU6qHzO1mUWt-0oqkcFGAhwmnWA_KrIuVhvEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZxxCUvw4IY4Smjf28UmKzRNRjl0GFjL4z9wbfAD4ZjXv-T_KYMemi4S-DN_GrznAtrqvv-3-x8UUDHpl-YE80v7QKYrt5qM48lZQiyezO9-f1AO0BG0ILCDMIBkwryz0x_9VSuaF68Ol47Yiqcm7hQWBKpjlePx0IIBtyRWTIgMFsWakzRSUn8bCikjWg3WHQeqMJhpFSUqQjzqxCIstsrQ4FfJnGJ9dGecKVQWu91uKYbbg5O79rpUK_DIU2emNYJBgWzSXId9z4zn_Oc7PzlM48U29zw2hHxCflzg-FSInc9mg97Clkw4m1-wcrhsIlBOQSrDOumbMv9cfPqlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Y3Sq0ge5wkSXwnaCLRVbvLNob5qftXeARuCaX80EIfg0f9DSeu0eZVNrV1GZ0DTxD_qP6mK-4EIiuKnBPv49RP528AmVG6ZQ3cxjXI7FNCgkBc0pqN66wm5KItbp4QDnR_nVqEup3YBzKyQrLmZqWLuacYk5dZR8vSzfCyarIGwpxoIOBZPbiJmE4C6t2eC5Eg7ZrhZ9luUgOKhLzROVH0WzU_JA2SIJ62Jjtob65E4NGu451n8VQTZUhfzqmrRtHPfvVzfW-4m6183ztldQjsFYiu2bRBhVjNG8sJ9foV4GcXv_LWHsM1dF8eNb6JKzdtxgsxU9GwNzuK5izNWp5H9rBwTpYLLuwKMcIpE8rucgx-5o9i3KzABa9bl_p_r3IZdLS8mwJqkRkhEmXvHZO6ZKKDUs8XquKAXxIAjcf1DWVJJDoZjL-qW-qKUe7Oqd-OLWbbyPJSZJYzeuZJduCXeYFeujOZkli7wyURM14cae_E3TX_Udyc4UoQ1ZMMIR0gdZyvpiCpFAYMUvk5Ru2NYaJuWugGY92LA_8mg9n-4uvcNiRkQ2OhVzkaozFExZiI2l03VK5-4DlbD0xOPNo9eyt_OqyoOpJ_Hy3zX4nRjrIm4HF2CuFGoDk07hCj9J11_LYew-6fR_q4L43A3MQKez3hzaUORIUoD07r7ERlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Y3Sq0ge5wkSXwnaCLRVbvLNob5qftXeARuCaX80EIfg0f9DSeu0eZVNrV1GZ0DTxD_qP6mK-4EIiuKnBPv49RP528AmVG6ZQ3cxjXI7FNCgkBc0pqN66wm5KItbp4QDnR_nVqEup3YBzKyQrLmZqWLuacYk5dZR8vSzfCyarIGwpxoIOBZPbiJmE4C6t2eC5Eg7ZrhZ9luUgOKhLzROVH0WzU_JA2SIJ62Jjtob65E4NGu451n8VQTZUhfzqmrRtHPfvVzfW-4m6183ztldQjsFYiu2bRBhVjNG8sJ9foV4GcXv_LWHsM1dF8eNb6JKzdtxgsxU9GwNzuK5izNWp5H9rBwTpYLLuwKMcIpE8rucgx-5o9i3KzABa9bl_p_r3IZdLS8mwJqkRkhEmXvHZO6ZKKDUs8XquKAXxIAjcf1DWVJJDoZjL-qW-qKUe7Oqd-OLWbbyPJSZJYzeuZJduCXeYFeujOZkli7wyURM14cae_E3TX_Udyc4UoQ1ZMMIR0gdZyvpiCpFAYMUvk5Ru2NYaJuWugGY92LA_8mg9n-4uvcNiRkQ2OhVzkaozFExZiI2l03VK5-4DlbD0xOPNo9eyt_OqyoOpJ_Hy3zX4nRjrIm4HF2CuFGoDk07hCj9J11_LYew-6fR_q4L43A3MQKez3hzaUORIUoD07r7ERlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMD8LmlF9dtW_n9ppKxRpI6QEXxtDEOZeKd6k5r9jaHphX7ZuB2x4FOmuvzkpSzuhK3CooFbmgshifVFysRdGWvr4Pna4MnxN2FNp-esexuuFvmYCJAhgcUfSgH8eqhwpQkR6Yg245Us02bJktom1ib5QIBAIa5PgJ5LGU9C9FTumRkNzb41Q-lnnQmJx9sEq1lhVY0nerk_x5bbVpnD0635S6P9iWvAp_YA4V3r5IlbLiTJMlJLQjVjJUpsnEvndrzup1rLMfURtN_cudyC7poMQIUA-PiU7xaE7158WF3QTASLBthMmRX8yv8yfsd6sbX8zW4upsYobqvtIxBRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bktpeOcSqiO1y8wrMjFGS76TDNFgFOe8z0H43rL6IOQEvxD_Mjrvl5eWrxg3AZO4u1ibuKt2ZiC55dscn9YlaE2N24crkobcuJs7gG4Mg7KiAnQl_w-YP2moMIqiQgS7apQiiF-RyNzYz8Zs42yt9p1j-9MYKMzKEgAJ9O9u-re0f_spYjx2oyv_we94tx_YBC7FQEYgHSBEOa0Bdoo0XOURxz7o-cAPaP3EYrfsvkYIYF07qbigmHhA-kqqQ9s3hbnEnRN35giulJEgTjUYFgVABFUNijEs4QoPDQQ2e6j3ZLIQEWT-ytTwea0HHoVnde_C7ZUrvDkZ5nGkV4PXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUQeNRLrEpf41UlBtqR1mLgAOnLA3xOE8IFGqZQx-Pr22yTpxFCfdvacl7VSl3s_X82y0P1hVHdX8yvWcnLTdbxE6Rk02Q_IQr2g3BvIIVshL5I0W1HEdtArN2mQQtXU9yT-AKNM-KUjFlKRf1rKlVWkzhzsneTSgBYA5QqDFti3zQUvSJPKz1LCeXMtmwr8FZ4XUqm0JV9Lji-IYFdlS3nWrTRfjRXxMhY-UWgg7o9Xw76TTW7-HvI9FlW5V-2TFYK2V9uExZ9YJvau1ECT0w3JZ4decL8SNzZzZ4e1vMijN4QLfHmih1E51-la9Ic0yCQRQ2sa5RmXDtobQhwPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTYKelc2mthM_CuD3lg_3G6rxFON8M-xWdp9Z4KN-Bmh2MD0KspehtRlnwJhQRfWJ4JUU7svI8s1HqlWQ0kLrcNTCedd3nVJnJWzVJfQ8FVZK-9M9cRb4noS2q3XPmpxpk1ukWE48KjJXiqO5uq80Y_zaQePONrwNiaa9d7eZAGa2_mSG1pdawHc4bVoTsZBG3mtMG_hxDuFNEfPEoCDa_EIz4xDLWXjO1VsaN29E9anQEvcQJWsNHMztsK-cy7eic1Xw-On0SyPmspGcxc1VM3pQ59Q4E-gsHkc9JEZZGVAY4-7nfCC_H9_Y7FygFcvYeOatOqorPPY6IpE9DQ8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=tDO43I8lDrqPa8XhRkTmXkrxEFDIRao0FjDLd-e_1oJXqfF7rYA5kXMhFbFymcwQBQBVWgQXa1c5LcSi2Xc5prBp1-4xYeJMnI9AiSfPUg81kWXGjqA_8uX2ZpLHSXSzk6ba-pBcuDQLyBiqjwQq8zwrYHBJdI2_28Vqs2WMRX-iUEfN-RQvuQ2i7v_csVtTWsDUG4KaJUq3_REyoRlfw1YRWS8yZ_Gpf0WPSfg9A8yT5FmP_dt3SZ4SuBDxD_Y0kYVG2SkGdhcMrjXfTBsyCz-wISZmJg02YkpEoLnGaKknJIWXZk63DrCU0vNJ7xL1NS48Nmzh12o6Gqq3eXnFE0WgrmgPrKNFsbXqhIwBoGZrbz3D7Xe-O9exbBEZEIoDbh3_gXQ48pyg_fEEhAgoR4AmWeopRkovO8u4xIbTyEtZc6hgTzejYdQ038NuwQMbEQHQCSTWR5GnTmdZEmflLHO6M1ZEdTJ0VtNosJGl-aUWrUejoyNPqKzTdP69CDMtdBW92dvyqJ8j8IPP-f7qYCDfUfjxfwqUSdyhdQBs2fD3DV9zi_R5BA_AWmYbyLKTuLwKbf28ezPTt74VBlBhTYUhPLAA-j011IuU1TnqSlWgYNum75hc0_t-kY8RA_seuYEEHjOHoTZQlMpvoiW2i1cWy2-q19LtpI45_6S2fZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=tDO43I8lDrqPa8XhRkTmXkrxEFDIRao0FjDLd-e_1oJXqfF7rYA5kXMhFbFymcwQBQBVWgQXa1c5LcSi2Xc5prBp1-4xYeJMnI9AiSfPUg81kWXGjqA_8uX2ZpLHSXSzk6ba-pBcuDQLyBiqjwQq8zwrYHBJdI2_28Vqs2WMRX-iUEfN-RQvuQ2i7v_csVtTWsDUG4KaJUq3_REyoRlfw1YRWS8yZ_Gpf0WPSfg9A8yT5FmP_dt3SZ4SuBDxD_Y0kYVG2SkGdhcMrjXfTBsyCz-wISZmJg02YkpEoLnGaKknJIWXZk63DrCU0vNJ7xL1NS48Nmzh12o6Gqq3eXnFE0WgrmgPrKNFsbXqhIwBoGZrbz3D7Xe-O9exbBEZEIoDbh3_gXQ48pyg_fEEhAgoR4AmWeopRkovO8u4xIbTyEtZc6hgTzejYdQ038NuwQMbEQHQCSTWR5GnTmdZEmflLHO6M1ZEdTJ0VtNosJGl-aUWrUejoyNPqKzTdP69CDMtdBW92dvyqJ8j8IPP-f7qYCDfUfjxfwqUSdyhdQBs2fD3DV9zi_R5BA_AWmYbyLKTuLwKbf28ezPTt74VBlBhTYUhPLAA-j011IuU1TnqSlWgYNum75hc0_t-kY8RA_seuYEEHjOHoTZQlMpvoiW2i1cWy2-q19LtpI45_6S2fZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=JcJi3HjpOl6K1wCsjs_5-aSdWLlPPnK1Vg3Wap8wUomlqRzlu0-LUX7X1oxZh7DcdmVQdUaBFBZNWhmD8suSFhv-VYvRVZ09a9V87a8U4jCKeRDXX-IBn7EuPBwn1XKDpZOHIaLOgGW9FRqhGK9Cmt74-uPauYk1XvT-yEXSFfgGGCz_jWidTgczv6cn4tAeHV8WhbK-lBJtgiiuoiBm1IzoRQybGmjkB9HhjkgL6Up5q9jh4UQADUbsW353mddjtake8K3RXwNLuxtxjnc6c_4jAinpLekUJ-DypgKh_j2LN4S3XPL8I44hn7GXdXuvZCurgwDajMLIIspbp0Hfrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=JcJi3HjpOl6K1wCsjs_5-aSdWLlPPnK1Vg3Wap8wUomlqRzlu0-LUX7X1oxZh7DcdmVQdUaBFBZNWhmD8suSFhv-VYvRVZ09a9V87a8U4jCKeRDXX-IBn7EuPBwn1XKDpZOHIaLOgGW9FRqhGK9Cmt74-uPauYk1XvT-yEXSFfgGGCz_jWidTgczv6cn4tAeHV8WhbK-lBJtgiiuoiBm1IzoRQybGmjkB9HhjkgL6Up5q9jh4UQADUbsW353mddjtake8K3RXwNLuxtxjnc6c_4jAinpLekUJ-DypgKh_j2LN4S3XPL8I44hn7GXdXuvZCurgwDajMLIIspbp0Hfrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq_wdvV1tk2dTQGF21H5_OIef3yfbwBn0F43vLv4ZKDt4KVzm2t0G5167z0uSEMgnXj2_gVD51f5HutxojTvHDDZRuwFBgDhJ_up1lgMSximhBibc31BV1H0ngvbMzBgrncuVEZF66aPYNKQAR6eTxkbjHMAOCUKInR_CpDg2912vi_eO-NJj8opgBes3pBv5JCZSfKFHJiFBW8eca5J67nyNDqD4jOM0IXn1oMaB4FJV1RhtHbroJoKzz7iyWckodKvz_a5COQaRWQ1Z9Ja84HNnGrK0YqR_IE97N49hr1XDd1dqbva-hLnAF52TSOPIV7EPXxmQsTwlrXKZIy84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZQbGVW-MRYL6vBoR5HDXoHLqy8L-nS7XsyWmtaKL8QgVQkKNFjUn4upUY41-HsjEyDm7CPZXAoXIT2D3hUivw2qc9FeNtQ084Du3REACeVKub2iQVLmnQcghxFdVojJIklOlxwm-T9B1fU9LZ_Jt4IUM0WYOHtv_Csnhm515zxYAmKMx7RN34Cru2DWcrsMcZXfzHfiOd3TzehQdouaQEqLZYhwvA5d2kP_Bf8QUO9Bfz6dxSQmZRp-AxeGNkJNWyY0IcSRwT6v-F-y2ULVwiXqDrDdaKaEJgPtl0TLQFGC0XfAxlSkjU8h0Y9knXprF3Fbwe6EEwkALRKUfHn-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCko0ahDx8hWjzggGiPlDzGkJE4uAHK4m2bTxmVzG-GJ98BNYdUZk5wkj2H9i4sO10RVjIh0WRtyFzgQ9hBCuT3NlxD96UTvd9g_j0t37jg8an9JabhOhJMQutQ6AfeAo8kbI7iwZMeveECWbXC7pfGmfEMMmxGRfrXF7Z_Ol5-bMnGfPRBsV9rMZAXRzesUaaJP7rVR05zys9p_Mert0pfjbh9vjKQoe3xwkXgqvi8ViV0yIzgBPcNvJc1cf8d5amJnsdK8E0X9xpbbaSpNbkiSG7JfHshyr5NPw-5eIHWhplu1T-1GWw9zGLzbwT7zNBTa3wQZAv9HE9xtqlE0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pr_wQstpWzNmaw7872Do5sgfCA3EgP6UW8dnaW2RhceICAOFiKxWzT_1vLLYwwpwEqkH5P8V9FGtvJyx9JZO1CQrnhKoIyRULGiTz141ep5Zs96ja073BeOpe_oFpGudV__5q4FFHWDb861WLhA9wEgCy4U2EH0tAAkuRkweUxw38oVUVrQxRtxZ5ZfPBfQ7hX8jmkAgaiPQ52MzxqgMrN31oXG5PwK2nTs1TLfGMM1FhD6JdDdd_CDihJdGBvuycFmkVNZH0tMH4xSXbM2JYXbWulp7jVVkMIbQds8L2MYqm-xKMyNaREuZSL3yXciwOd4KEchXuYK6T_TVi4NLlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH_5S45MxowlJZKryRExdDv_YoI313N6BP4WuFfM0_dDBGIXRA_HeUilF1mZm2gQ8rQH96MuD5E6jXvzeXMjnpGwE_-M4Iltpjbsq1UsaFO_Cu4OR1Dg6vmzrn54i8qwQ7OfySz9oCihr7EtQDUDdv5qqv5tF2FQpYCbNajhLzk_hjqyqQDxHyrnnX2aLccb4sKepy6T0SkU1pk3DUfwPSkJU0_nsz-2WlvZHZXGzGBaiuhmpc7r2ooU-BOBMpWX4Y8IWcuOEaQeJw-iG9txi7iz62R3a_9NZljFKOkBx9dYIm6fuYivQNhoikQzw_rNVRt4jtbU5Asb3xPqEWxpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxCwoNl_oWdDFg8K-vil5x_VYLZT5KMJ_2LcGdkly6L30GlSV6L42BRjdHhNE01e1blHGxk5ixpL3esn4eZ_hsehTaSKMeFAblDLS6TuW9CcHeniw1rWho2UepRz2NpURV2FeojzKpjr8LI-dPjF95lkuNuTSb-jTUJeOuIIk5-aGi8GkAvPx4Nut50eXBaxlRYiA7GvYATf2SJKVVYfL4ezg4wtzIB2CQOahiPxVu5f6MT7FD1UZuFryXdIfoE6Lpy3CqvH_q3HohRV58EBJDvs9u73XIMRfEpwA3TFBW2QAUy2qZuBtXrmKaWfYeuRl3AfX8-YK2VxkB_Mi-bCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTJP27xBNrimaOCWsw4qW_w9uYd6tWpqsyeoEtiOw12zjG-SD9AN15C2TGtBvTIPb2jULukfaQOnftkTuo7EL0YnlCWWZaroF_pfypSWfeClgylsOeQe_U0QDc7xtfUHSKOkxBowsgoz16W1lKSr0VV14C8g3POTi011ACt-qxJLRqGaVwJUO3Wl8PbBDW_jL29N-jVk4LSf6SriQ0kLCGD3BK-YjLxz8lcn4iVkR-pRphwG7t1Goj-4StgC0oM1R3gC1x60EKrNxk5yCgarTMl2D6gyufWqq_hNp2NZVgb9sHPVfanAzSbg78AYdyaaQWNF9Z_OEpAE6zF5Fn28uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=RgWK_rj_SasHlkZDXMRjq-sLjnhATCq9uS2MKPWrPxKpnse9MdqEWUzxDvzBjc99BODZ6h6Gkm204XBhkbLFGT-z4kGO5LjwZPvdD8iPIDR38-GWte-awFXwQuNDAgm5MxfNzwRI9F6jtYZhABFcUfahplUzu5DlAoh4KDXru6aZIwv3DgzQ7RzShRNJB7XFL3S3zZ3SrAIvXt8Han20DxoY1On0rgDV-OJzBwSX9W22Wt8hmMJsEdXuB8WlJjvMCL7Ag1HJqH9gDTca3H5H2lWQuuwcd4O2a3q5T0xmBFgYJFgES43E0-U1XyFKeb2aG-sIM0bLlOznInNbGHesAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=RgWK_rj_SasHlkZDXMRjq-sLjnhATCq9uS2MKPWrPxKpnse9MdqEWUzxDvzBjc99BODZ6h6Gkm204XBhkbLFGT-z4kGO5LjwZPvdD8iPIDR38-GWte-awFXwQuNDAgm5MxfNzwRI9F6jtYZhABFcUfahplUzu5DlAoh4KDXru6aZIwv3DgzQ7RzShRNJB7XFL3S3zZ3SrAIvXt8Han20DxoY1On0rgDV-OJzBwSX9W22Wt8hmMJsEdXuB8WlJjvMCL7Ag1HJqH9gDTca3H5H2lWQuuwcd4O2a3q5T0xmBFgYJFgES43E0-U1XyFKeb2aG-sIM0bLlOznInNbGHesAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv8JQNvV9PAemlPh-3RwrKWqmoLpv83Lwc6JwzxXWrG94ruldB3_e-6LIbIVhwvsyM80zbjGX9gwg0sZidQwMyPQsuITKkPwF8JnQMLWp2AeSymmIb3MyUwrDafgzG8sS5Gt7jKv3YejSO4OyKCR34Z8VT42f2KTvYbde9Sllbl7hSDteY1pYdxUkuxmywVOH8Gi4Ye6PcAWyP9zsmkEkQYaoL3YoBeZnze55_WPA07UMsBgrcM0uZDpJ9v1jMAz_kA5u3uEvDa7OMsi5w1hIO06riCjrOmrDrESTkZeGUi89FcOypSDVwQfmnzp7xFWa9eqb-MoHJBuyxElKD9ocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Axn_Ifsv1-hghh_6pzn1n-wR_L1AQMtfkFjrY9qi3BSGbRTwk6WWfndnTy3Uiy3XXEwnKPR19RPV8JJEeC0HmSYUGFBkbP9XcvTvZTp659pAZUd6nFmNvK106livaOzXdrQxgLQWumR-fSUV9V_ce6LzcAcvSv5h0A9n92vHHSc2Cvg617g-iL_DxxpqCkXdVh82rf7ps0Iu91ljBZzVazkcqhbie9FAj2hmtJhMXlnWMmv2mGQG_gETgXAS_99NFOSsvn32B16Zm1Xl3RGnHJwUd4MflXtIBgjgiX5q93FtdGPE1rqGpMwksVeSe0os66NZ3VrYNjVQgTZI9o1s-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Axn_Ifsv1-hghh_6pzn1n-wR_L1AQMtfkFjrY9qi3BSGbRTwk6WWfndnTy3Uiy3XXEwnKPR19RPV8JJEeC0HmSYUGFBkbP9XcvTvZTp659pAZUd6nFmNvK106livaOzXdrQxgLQWumR-fSUV9V_ce6LzcAcvSv5h0A9n92vHHSc2Cvg617g-iL_DxxpqCkXdVh82rf7ps0Iu91ljBZzVazkcqhbie9FAj2hmtJhMXlnWMmv2mGQG_gETgXAS_99NFOSsvn32B16Zm1Xl3RGnHJwUd4MflXtIBgjgiX5q93FtdGPE1rqGpMwksVeSe0os66NZ3VrYNjVQgTZI9o1s-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5xVEcjqfzVG7Udj6iRwpYNQ-o27E0HoraTy3JzgQTOmaBMiG9v1S-kO6XspJADMDfnyVVzd8CD-Fysa6Ugj2iOdq6aqiIEPfFE54iFc08PHIqKNXTLSTNdgDv07LlDTfLOdH84cX5_Sl0Av9MfLPJZfBA4ROiVghtKFdp5SC55VUmzaunQM3n403UJbV8Mogz48SHzkgY16_oEO45M-NwLTJDEIcgqJfj3pVlSLLquf6PiU_LJ0nnT039lhqkJwvljiLhwOoBqIYzF9KY6KruFWr3w0OnjfU7R6JCbP7NZ1Shv6q9cLYEU_QgT5K1E3oWpGJzyWf1bmOE30Bkrg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJp0wvBN2wVTgEseQaa48aGi4x5vg_QyqyfjsyBjwjgb4bHFME1AwXGiLKN-O5Kta-ci10bXHUHwjRgAmNprgEAgzizHadpna3zpEYcZfR4iL6nMqxX_vN6KRHIlOJuE6yDqvsCqNbHIHHYkBxlx8PiQeTMMtoRzSTq4aE-0G1ON_AeO-83r-2blHouXVsMYOb2oDu1VmzZU5ao8aogQP0K25wDXP3jALNDbBCgrL88-8EYYrawaCrzsLyeJRTl18vW8SZJ6vN7RMwN96ninb_hZcCvcwGJyB8x4dIm0yr-qYc2xiNv8IVRIFIADz8Z-IsU8IpP088rRfRVGljAsMPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJp0wvBN2wVTgEseQaa48aGi4x5vg_QyqyfjsyBjwjgb4bHFME1AwXGiLKN-O5Kta-ci10bXHUHwjRgAmNprgEAgzizHadpna3zpEYcZfR4iL6nMqxX_vN6KRHIlOJuE6yDqvsCqNbHIHHYkBxlx8PiQeTMMtoRzSTq4aE-0G1ON_AeO-83r-2blHouXVsMYOb2oDu1VmzZU5ao8aogQP0K25wDXP3jALNDbBCgrL88-8EYYrawaCrzsLyeJRTl18vW8SZJ6vN7RMwN96ninb_hZcCvcwGJyB8x4dIm0yr-qYc2xiNv8IVRIFIADz8Z-IsU8IpP088rRfRVGljAsMPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=bXB_Oees7edOCDvIQXfcGpCp5c-HATfhF_TcAtgs0VeW7kgJ3oQLX2y709Gu7myZkro0321isy5CBbCLoVLdE0KEcHYODWQyr4zPk9Sj1pVx0H8sCsr0ytBCRrXVftbmLC2sXTV_gp8j6DznYPhNq3e9x8xkb4e9QJ7k65i4EHO6t6LAlil9ARRNxBopallkthZiJxpzUH_UjF-EnRgSMXELrEHmMKnn0hWzMD-sFgC2WZxeMKVGu3o6SA-kPoSwH4o2tUd-hjg9Kc5eHHcIste7VOH2Yp3rnBc_a7V13HzjivlWxe1zHz8I9k5DSBt5kaWPy5fOGc_3uskuPLWK-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=bXB_Oees7edOCDvIQXfcGpCp5c-HATfhF_TcAtgs0VeW7kgJ3oQLX2y709Gu7myZkro0321isy5CBbCLoVLdE0KEcHYODWQyr4zPk9Sj1pVx0H8sCsr0ytBCRrXVftbmLC2sXTV_gp8j6DznYPhNq3e9x8xkb4e9QJ7k65i4EHO6t6LAlil9ARRNxBopallkthZiJxpzUH_UjF-EnRgSMXELrEHmMKnn0hWzMD-sFgC2WZxeMKVGu3o6SA-kPoSwH4o2tUd-hjg9Kc5eHHcIste7VOH2Yp3rnBc_a7V13HzjivlWxe1zHz8I9k5DSBt5kaWPy5fOGc_3uskuPLWK-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=vYegWPWD3oPAgSmvUw5Ez3PfzeTO2q7wsFKgFMv98tcMxrwrbuGH8NfcpssreiicHV92TeW0L5c3Ig_YSPwZe9Gnyp2pIyqzgyDqxA9x0WTJ6W-0wzNHqSzL9IZiE0qjdS-_SVGhpJf3WVwSxmifhO1R3vmbmCivs1Ptk-R9H9T3Kav_2wROlrk9rpavr-3GWCQmuPaV6OGWGaeccDKfAgh9xLUlN9Poj0e4wjMjnhfFrcuvZDasrzZ5rEoCZO6995mRx7NE8RmzFnYzyh8bndF8aQOIyUW5Cx-ABkHu5mvleRhx9oGYixgZoChUn7LNEg0mAJqWw_jmM_O5JYLX-S4RubwXRWF1cWpEnImxfwvwk3ulJH-bpr8YAHuf7ONEQNiezDDiEGyodUCNRpQnsdzXUqdf7OVWQWsXbmQOnKByD00XVVpVUbbibCJ8HRRq6r6LF7AlwN5su7yTfIn-0sUQLTe7qkTNR17avJY5xP_4sB6Cm_SJu5_oX8xOVjA5aD-rePG5d6i30Wc98ECaUaNjezWMJJtEr60GQM6wRRkKOe3-HvuVDVqja_QvAzvCixnuaUCi95TNQutJ374V29W2T9v0L7FEDx-PsIE2GaBrWFF-pPNbvEg_Z0E-xYWc1iuQSLcyvcYQ2f6dRRNZACX3yuIdS5dWqNj2bOIg8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=vYegWPWD3oPAgSmvUw5Ez3PfzeTO2q7wsFKgFMv98tcMxrwrbuGH8NfcpssreiicHV92TeW0L5c3Ig_YSPwZe9Gnyp2pIyqzgyDqxA9x0WTJ6W-0wzNHqSzL9IZiE0qjdS-_SVGhpJf3WVwSxmifhO1R3vmbmCivs1Ptk-R9H9T3Kav_2wROlrk9rpavr-3GWCQmuPaV6OGWGaeccDKfAgh9xLUlN9Poj0e4wjMjnhfFrcuvZDasrzZ5rEoCZO6995mRx7NE8RmzFnYzyh8bndF8aQOIyUW5Cx-ABkHu5mvleRhx9oGYixgZoChUn7LNEg0mAJqWw_jmM_O5JYLX-S4RubwXRWF1cWpEnImxfwvwk3ulJH-bpr8YAHuf7ONEQNiezDDiEGyodUCNRpQnsdzXUqdf7OVWQWsXbmQOnKByD00XVVpVUbbibCJ8HRRq6r6LF7AlwN5su7yTfIn-0sUQLTe7qkTNR17avJY5xP_4sB6Cm_SJu5_oX8xOVjA5aD-rePG5d6i30Wc98ECaUaNjezWMJJtEr60GQM6wRRkKOe3-HvuVDVqja_QvAzvCixnuaUCi95TNQutJ374V29W2T9v0L7FEDx-PsIE2GaBrWFF-pPNbvEg_Z0E-xYWc1iuQSLcyvcYQ2f6dRRNZACX3yuIdS5dWqNj2bOIg8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndwWQcf7r3cWsxdWqxVZTxbmiMhQqpCHC6MTWSeKZhNjZI6njhSz_gADux4d_qHSpAaNJUezIxSTIotpO-sEyw-9uV9494KGL3pCGJ_aZKMHv3ujNB-7WYG927N6fNLjv3pmuAT1bh7_ANTqh04K7ikGcDasRXS4kMdIfUGBHBPwpXd-IevlOMXqqf60lTegqYk2Q2drC5_6CjOGmAZhMkcFsAbDapHuXlvSfJG3dYxdVBKUihI-Y6MU9pUsUTQUm4gFaihC4Ozdy9_xSh8mc6pJ0zC-wcSZZPYsstOdh6tfylQFkUuZfgSLpccCaLSzmYwfNf-aZJLCuK6UmF0dEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfyyurP9GxkCjxexy0RENVcVt3Fxsqu-qBzT-abiyRFnb5260gaezaEpPa0qVaal1aFn_Evs7iwrGve_cshKZCkCSvfUzh_ZFRNLr0sDvYSrIPRN1BL4IZyjv5po3X79eJj7G6MgbnKxk7TpSWBBYKdOvYgRn6MGVBJIKFOOuimbgtkX1CgCEq5WSIqxMD2MwDJ3hVfdf_XBM8LplOE29n5TwpjERHE_jIOVGiclpvCx-OupKsueqD6FVIgJ3S0QM2I6IpBXmMvhLFfnMJM4c_9igULFnTiWhI7LqpoTwrHkrxEWpr7pOyfTCE39U6nyrm4vUNEMnRwJUcUQugKrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSeU_nzosbYDwUVAo5IeQyMcvbHnBKRuQWOfvGIq279yaCGMcXilAIOn93sc3T8SvwrQwSsTZiMfp1KMzS-k7fl_oMuG6iIoco_lMSIbz0RNBouXjZA9Ka8dh6IFnND8mAiTEK8C1OZ5E_cBU6nAuNXpeUcyjKkFABaJsdK9qV0eUW2MF-MFyQToQ0ZS2FDlJ4ALQgSPI4fPiqNHaEOFE9a-zPoN5LKZ6ZjUpPSrJxjSE_aahPd63Aqd4DdX3jFE_o7EbXhomQ2rkf31v-OImKjMZkfVrdDuph-u2u6REu-OH4mWjLICYbJaOAKV5dXUxtgnkaLXMbvx1ba9I0sJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFav-k__3P49rQACsDHM1KxQBh2YfA2KgF8YUiY2i_tY7Z0vbb7oj0w57gODUF55wCO0e-z-YG-ESA4W_8RHV8W-039iz-n-wKuBpXFYgoIBS0XfpbfmuWhntkRY9iC24mV0-weTrwBSb-emEYnBtZMZm8kx8AOtGUMUD73EaNODimIxxudnrihXRVxfXnDUoQOR1t-PRrFaZbq0Kwy7yEmUwM39253VDMXHm8_qo9ZWeQw67WZD-E9tJPT9Zzkoax-AxQQ83TJ65vTW2HUuHA1dX-Kyxy5q3dx2eljwvCpZUW1RIzeBVFHAboBzvlpG3PwDRErC9E6Ql4R6u-3k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXvRM7gxy5bHriuAN-317uvY86v1KD48Ksb0TC75kpv2L7YPEw3SB9-oimdOmCjMgFQNBcekh-_GVYiAMhpzA75i3agWTLWjANJXjez9GHB2DBpstgXTSo-Z8zFNGtYjjAaldCQ5PO0GsL3GZTAwaOnVKeqo-HbRvdXLfN90JCublE_i3GnS4PV_wzDhzUk_ISb0PkjtRIXj7Pwt6e6jz7e_xVxDdVDcDpp-FEt3dZB-Hi4JrUtiPr1LOckNBX9MatdAyfZ7WjuvcyBEtQn3wvEd91uQ74rFj_XVkwtAK6c6cPIw36t2m9YgKqYz7aXcOX92qkm8jUIqWq7RSyM6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIyMZjSGXlHU8Oe_DDx7Qb1nB4XY3pYzcQb69sLmbN_d7okxUHRd8vsOPXSNxlC0f-xrbku3_95sTDUwYE91qgpvTbk6M5uczfuf-A0ngpiuSMHNnCs_Et_FeYjH5WlVnmuVpZhqSYVt0pn8ITqJHhM3KSydYXgasVnKqkNwzu7YZDgqYeyrCo8pfqcMfSheIpA1NVxgdSTmsB61rL4F6IQLxdwg_27ALPRbcx7FOopn2Usu40eYl66NCZvj0n646lSu5y8r8FUmLaHLm8L2ZztF3hxmCzgxWbd-N0dtoruCwuqeO8Fzps0YNIlkO_IktaKA14BBmoaIB0Xbsoiw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY6GVNFwOH0555XuojtNsUgQZJO3vzjp0ym3keXoX4GkIDFCK-gW_C_Hf81ONULEn_qiSSsvIQcRnjI8uSALodP9Xesw0k5nVm2hY8fRjajHr8wUssUOFIhXr-Y9eTeP9Ydk7akiPYRF8l5MvnhT06Kv40IewcLwNJ443jB1vqbse0zFCvsI4Ic2SM0YUfUfzel2OpLJDOlYC9J9-RxIO3c37FUBKzFFKcmW9r-_oMhG-aFfSgODB0YYC-vyAzGtA1a9HjNjxLO2v--dIUhVb8UNQOnfV0F8Z-xJ79cNikalsn82pOAvfSlEj9XRTARvcjkQ6CcoVMIzKWgPdDwKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgXJI40fwKDrU4LfklxXhNGlxSDZc89SnQIBuvedvgrz-6iYDh0oUWjPgNvrQtuqnI0ztgiKPx0YO9RtgPXJCNzpVANCffHzwoK1jby4t45m37IhVLbm6Q9M7OSs6fYkgeJyQzcNBZALmbL3qjiLHquhJ8ykk29eInvJi4kY-r4zB3l4nGlEnAoj3ioXEUahOqE1nJ_dKB3B9mnhXWJ-vxEmPc0aryb16jGPchsY0OPyuLrIJfi3uU61Gh3BWs140vVfwYTbrCWzReWsocSG6NLrI-uymp0BvVur_a1ntvatHntbqRVGp2jvjP8ePzSLngUXdAPlCBhc1TXii5QNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzlb-0YaV4RtAuFyl2XY4zv0jePCj_64MN0S7S-Dn8KNWlkm1Bf_2RsAk12fXOYibi8e8CgX_jh0kbsspInfeL3U30Ckz2Nxse0k-Mm_dEVlxqAWtzJZ-8v3mR3ebMYahPQ7cI9pwOzbrfsFyiJXpMYjB63--U5cYOUygVrUienc_060HO-BTyeDbZc5uyNL09QFaCIoABIpa36rm7b80MepIqa-uXYnPTpc48ZqBLtkOe5kPFTQUlLY8HmyWSKS7Q9eY4xXhU6RUn0SAusnkcnvKCTjl6YBpIeddLvnW2dz83z6Lo02VbwfvN4xUGBqaYn9KCZ_BKq5Gx1i0_PEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAo_0t0iOUGBgiCX9QIApSi7e5MSlDpTuXGFb5KoJNNpzxq3AjnEDK4-mehzL_qcqNHfPgN79h_cbWX7AkOPiqTbzcoT6-aLsUQ1PQltYCN9eJ1LtM7xwhY-_AOJSJi8nMb-Uz2R1_kXi6mlERQuDz-B106z1FG8H123cQ5LQ_VtiybRdMAgGO7PBNUT6JWkPXYRJXsZF7zNHKm5Abd1FGMRvA7vVeqEiGC2ROGj2ZGVk8w0zdRMvICp796kPgRd9nBmQOzNwCjk64tR8yJ-0uQxVGrL8AI2CB7zKaE-K-YP1mavHB9Hb0kPQVUq0h1-UMADZeuKwIlBob-JA8xEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJ2rv3sOfAStFWF1-_o3_KyuEGEXTbIdm59WBWiIFdgsWS2L9WjMgABPrkEH3Vuuw4OuiIJRMjd1tSvqem6k1du8IhIReauWLzazXgEFIsLV-cVw-WS5nMmRzGRSRlYf4DSeVvDByrHZZGwF3wZClydxsZnLmnWXZB142YV9K2Ab6bW07ubEXOz9fUiNnf8mFfIqbBHWS0CewzSHj8VP4P7w_64lL1YTAH5DBu2CpvNxdyphaOwqO9UaJ0HtjiuTNBhaiqGYVIf91my1zT7xZcI2iXGzWU7EKuHtkM00z7wUjmE9giWxubaYXHS4xQGtAmTbJf6K2rrN6ChRCBJJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcfKLTs4mDcdGTUaQhOSGPOjGxCQOLtHcItl7cVwLB4O2jAFrNyep_oig-Qy83qmBMbB2DGQD9o_tFo1_5cE9kXfX3h1O-UFJ631VFWxeD49Gfhh0qge5KfPmG8hkWI5xWOC3hYUflrR273uB2dC1fJOnDIRSInfFFfHrLwbnWDDn0HHAFTZnnqpDsklJWJ0T1HaTdb42n1c26xIvXrcNqadJ9QRFMII026fZXf6ifZ2-CiseJiGORIBwDF3lsy10E2pfV0UzVPSUy4UOWGmJ92QN4d_JpjUp0xJ5rZPoSzo8eKw3uFIz8Rb3a4GWYgk8RlJ5pQBQIUMDpFwPr3AJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMLO0wTQILwS8DNPolL9L1hV0vauutJQyxWHyjmVniinJqmT5pjnHhqCMUkXJ861crKfbgRKzS7VE9LE6eZmGv_C8vSmQdjBE366ytYvwU_RYPGJw6gI4b215qShqQREv4AgmsOSwxYASTAXNOBwFITxxKiSMbUZUfWIlLspSZt28IHcShU_h0PuxcXz6EoLbt9sG3ykv-UdeySdJXY96Yjnj7hP3N1ViPokkfsW9rDLYcvB63VtIdOloHINNXnbYwfahpJLDLCPACa16lrzckKkrUVwCWg9vcntQbsaD8R6X3NeKKqXkU16TvOPOQRSto3KKgC7mLLdH5BRxzmKmcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMLO0wTQILwS8DNPolL9L1hV0vauutJQyxWHyjmVniinJqmT5pjnHhqCMUkXJ861crKfbgRKzS7VE9LE6eZmGv_C8vSmQdjBE366ytYvwU_RYPGJw6gI4b215qShqQREv4AgmsOSwxYASTAXNOBwFITxxKiSMbUZUfWIlLspSZt28IHcShU_h0PuxcXz6EoLbt9sG3ykv-UdeySdJXY96Yjnj7hP3N1ViPokkfsW9rDLYcvB63VtIdOloHINNXnbYwfahpJLDLCPACa16lrzckKkrUVwCWg9vcntQbsaD8R6X3NeKKqXkU16TvOPOQRSto3KKgC7mLLdH5BRxzmKmcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=kjcwEtXxBK4hECbsPrw7TL0FwIldMrArH6URr24YK5YymmYXQTVsLmSLs4pAN6pTNFGBsXfGPy188XGGXNM-8DL2cdpqG5fY8YnPSVsCt5m7bhXu8amiN8Wywc-Fp_th8Wltfmyx15rYcqmnzS6U2SXKJGH9ETDSuB37tAz-mLpUvrf6UPXm2_iMGGAfp5NghY_Ox77frG_8lBQv_zAWUL6tBQeACLSz2SnUg9RoLW2aKBu_Dib85QaLjr91wtwWI1S573IL59PcoFqVwA8iwKUkms4z2BAqVvzQt-8vTv8cErNlOw0K0yUNls4CJbSsAx7pSzc_rEvQDbRbGiUM3y3Whpgg0USqLgnDU09DeprWNxN5zzoVldd9AE87KsJXJC7QxtIUKUNZxt0fT9mfltp1YNwzmMGuEIb5t5VubfMcZS7yum7sivZPQxHC5QC7RfQnR4N9bueliSzlsTc3jrL5we4aYjLq5JAXaZ0MxkXGyobSMWyd_3CDvWrzDF_-0D4ZaNOQStnfwlA2GsnWM0GzR2tA3X-nsgk_XzDrdavdtWNcK_nyERz4tN8U5sc_Pi95gYjYFKd-HqyrXEv4SFeV2zGFmN9m5sIIC1MvXvh4ms3qqzS2wlGEApwPcbPwaH5fwITwwiBeqUBuZPPL3mnAaeQEp3Fcm3XmhHdP4lM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=kjcwEtXxBK4hECbsPrw7TL0FwIldMrArH6URr24YK5YymmYXQTVsLmSLs4pAN6pTNFGBsXfGPy188XGGXNM-8DL2cdpqG5fY8YnPSVsCt5m7bhXu8amiN8Wywc-Fp_th8Wltfmyx15rYcqmnzS6U2SXKJGH9ETDSuB37tAz-mLpUvrf6UPXm2_iMGGAfp5NghY_Ox77frG_8lBQv_zAWUL6tBQeACLSz2SnUg9RoLW2aKBu_Dib85QaLjr91wtwWI1S573IL59PcoFqVwA8iwKUkms4z2BAqVvzQt-8vTv8cErNlOw0K0yUNls4CJbSsAx7pSzc_rEvQDbRbGiUM3y3Whpgg0USqLgnDU09DeprWNxN5zzoVldd9AE87KsJXJC7QxtIUKUNZxt0fT9mfltp1YNwzmMGuEIb5t5VubfMcZS7yum7sivZPQxHC5QC7RfQnR4N9bueliSzlsTc3jrL5we4aYjLq5JAXaZ0MxkXGyobSMWyd_3CDvWrzDF_-0D4ZaNOQStnfwlA2GsnWM0GzR2tA3X-nsgk_XzDrdavdtWNcK_nyERz4tN8U5sc_Pi95gYjYFKd-HqyrXEv4SFeV2zGFmN9m5sIIC1MvXvh4ms3qqzS2wlGEApwPcbPwaH5fwITwwiBeqUBuZPPL3mnAaeQEp3Fcm3XmhHdP4lM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEHe2LwrVjGKq756sozCJrSu82CsplAnOoFl5oEmfAeNjMnVrG_SmcsAw1jsltu0H_LMHCwbgjsK_6Ny61zigk0F799Pt4cK8uoZT-ru3YKCHjRu8Idf__PH7G42ztjE-PmwKR4C_0YqNm8BAq6S6C-JxbR460ymBP9oxPNIqePKvhXSL1mGqYjWfGtBKJmeXX1-pSzx1Lq1opgkjbIP2AplPUX6N3A4Pt8QzYw5CBY3CvxZlN97rUCA4YMNOsb4ZeJrIj2z-c5oCo-K02b0pqGE4mUJTd3jUT3NBLKPiTBg_H_t4SUVSnJQaz5-ujRmGalRRMt3atYMxQonuveoPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=k1glI7KEdtXTQjbWyOura4zWKTo57QYi6cg538rWRzmq3J-QY9_YbsTAdheD7urpZflM-w58r2tEuKl8BGAlklH7rrMxAjnhBPU_lKQNWkEwqDwbSUdQVYTclDZjFA7iPY2F9yBIFaAglEDdpZ9MZCdca2Uzet0zdTph7XR2VY3kpZSCIrwvxFXv62wcKYArrioZOzvU7Gk7SvUlpWHf2dvktcecwlnJdMHEIfMN3zG9cgvImMrsff86steeHo2gUO3diVzBvUZE9w_CsJwa_KKUWxSUePJQmbC4uz_bOvMPnHqWpDSBs_AMCHhG6A1iHtwUOi9kzlR89YcYiHDV2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=k1glI7KEdtXTQjbWyOura4zWKTo57QYi6cg538rWRzmq3J-QY9_YbsTAdheD7urpZflM-w58r2tEuKl8BGAlklH7rrMxAjnhBPU_lKQNWkEwqDwbSUdQVYTclDZjFA7iPY2F9yBIFaAglEDdpZ9MZCdca2Uzet0zdTph7XR2VY3kpZSCIrwvxFXv62wcKYArrioZOzvU7Gk7SvUlpWHf2dvktcecwlnJdMHEIfMN3zG9cgvImMrsff86steeHo2gUO3diVzBvUZE9w_CsJwa_KKUWxSUePJQmbC4uz_bOvMPnHqWpDSBs_AMCHhG6A1iHtwUOi9kzlR89YcYiHDV2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=jgRuVmeu4sX0ZkcepCqQW_LwwtvZeVUWwKEsxx45gxr4ABaCSjrP_PiExRivapTH_AQybKT_EaQlqTj638z1nF_tF0s1WV0oQ01a5l7dZ9FIRd_k_SGidt3uLRrsZOSFjwT_TdtwEAz4GrJY94iHIBCMjjvJoTIkbE4FDV-MbhG_gYlcvhq3dw7TYd3UPPT4a-gkuCBidO7BhIf_rNUga_P0od8Od_5HwNhyf0NU6UK-olaPpJWJCDd4tuJe2X3rK9doUz4nxqNs57mOzEqtArkdRM3hBCDYIyJsoYElPsN6CbC-Dp_rA64VJt6gnTPKXjoypNsyEeo01f_wd57Zkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=jgRuVmeu4sX0ZkcepCqQW_LwwtvZeVUWwKEsxx45gxr4ABaCSjrP_PiExRivapTH_AQybKT_EaQlqTj638z1nF_tF0s1WV0oQ01a5l7dZ9FIRd_k_SGidt3uLRrsZOSFjwT_TdtwEAz4GrJY94iHIBCMjjvJoTIkbE4FDV-MbhG_gYlcvhq3dw7TYd3UPPT4a-gkuCBidO7BhIf_rNUga_P0od8Od_5HwNhyf0NU6UK-olaPpJWJCDd4tuJe2X3rK9doUz4nxqNs57mOzEqtArkdRM3hBCDYIyJsoYElPsN6CbC-Dp_rA64VJt6gnTPKXjoypNsyEeo01f_wd57Zkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbmn9SR8lKZDQ4EAB6TCQB1AB-VI7YxX5coCMsWJ-2dKwOR3qz4UTRNKKyUBopCP4vy6LJWqNPU_CuzwSZGgJ9QEa0f0uJN-2iOkbwltASyVNkltk33GMUekRtNi4nJ-pUTf4FO5tiEdLGQ6_bUQSnhluBb3Y1j7zYa9CA33732cJ7JkVNP3Ad4jaZIXqouSmfuFDirev_PKI7k4gTLwD--eA0MDPWGSzHYyE8BsglxwPH_e14i6s7d0ZTNe1zR8m51XsOiLTL3kRMuCy9dHLB7sBPS3D8CetjyBVc1CCdKXNMKTHogdjyyDYbdeOzqiAq8s4eyMuOP0CWqqVLslsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMvQeCUNoswuC6CSoLscGmjbfkfTMZEf6aAhQD9t7S1O16jj_63BaYXEixBloC2DoLa_csUxeNvIf0EmbtI447fziRue9sN2lMIuXvsaCwTDCIIKvONxbmAyrvTqPQgjKSfFGG8dzGX2ZAhJ2lnZ1L9JyKHQVNr6kld6XqEvbo4Yw6mfXYwzjmA65mAr7deyw0MW6-Ex2amae_-qjO5ZTkMNxFZ8VdvKohzQ02q9-vh-ZN9QHLmzK88vbVSYhRFZe8_esDSnR-tnDqgaDvIU6uTrWXB4K6mHFMVB7W6h9hkMys7QeMACnbTSNbN10DhH-IoaRpjGJebNXuZlN8FKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=GRW8hsbfNhj_jTCql8u2_zUQP6igueYtF1hEvK6oN7-M8roVUN14ac9TAAwsMXRGrevKTELNqzpi9kdzOE4n4QcX7HOw052xwgCvW3wlvMoWncQ6wstuuF-8_Ie3qnRecVxylGIlC8IlpW-uTlRZX1uv6LqDy3xBmTsLL3ynqQ0kXFAuUV9JJ6kJE3T3RluaUHucHUzrfjsjbaGAOvOr3RgHFkKttQq-DNhShQIjT74if66tJMfG9UY3pKUVVPHZk-kUPf4U07u6QVVktKZS_dDilIGO9ICuHLgatSMrLQOI-qEvMnUM_blDvVyyMCqUECmyBF48z8ASzctlSmFQZ7BRPeZ202TMKr15FU9qq9WQFvyroWG02OLi6BeYkpwA6s-ov0Y1iLV6jpFfLORpgkR3tEKrh2u5UjHgRI65jXZDH2lozdmpLI5ou75y54FN0yHCwp3ZscmVY3a6irSAJzCJ1MHvH2_wOeZdDhYOXMLIrK4VLk8obD0awoCQyLK6r6-zVHjtSVpAai-Kxb8vxK6QP7M2Ban8OFQE9l_Z_nJEHcEn-PHv7XNDF28gkF5CEdSRykqKpy5jVEG3Oqs0EP8w2enjkNC7uUwC9gQ7bN4GIn3sVxC9q0vyEG10VIoz56OS9X3w61OEN_QsRDv7OzMLcEL-E2KWViFfEGv-4UM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=GRW8hsbfNhj_jTCql8u2_zUQP6igueYtF1hEvK6oN7-M8roVUN14ac9TAAwsMXRGrevKTELNqzpi9kdzOE4n4QcX7HOw052xwgCvW3wlvMoWncQ6wstuuF-8_Ie3qnRecVxylGIlC8IlpW-uTlRZX1uv6LqDy3xBmTsLL3ynqQ0kXFAuUV9JJ6kJE3T3RluaUHucHUzrfjsjbaGAOvOr3RgHFkKttQq-DNhShQIjT74if66tJMfG9UY3pKUVVPHZk-kUPf4U07u6QVVktKZS_dDilIGO9ICuHLgatSMrLQOI-qEvMnUM_blDvVyyMCqUECmyBF48z8ASzctlSmFQZ7BRPeZ202TMKr15FU9qq9WQFvyroWG02OLi6BeYkpwA6s-ov0Y1iLV6jpFfLORpgkR3tEKrh2u5UjHgRI65jXZDH2lozdmpLI5ou75y54FN0yHCwp3ZscmVY3a6irSAJzCJ1MHvH2_wOeZdDhYOXMLIrK4VLk8obD0awoCQyLK6r6-zVHjtSVpAai-Kxb8vxK6QP7M2Ban8OFQE9l_Z_nJEHcEn-PHv7XNDF28gkF5CEdSRykqKpy5jVEG3Oqs0EP8w2enjkNC7uUwC9gQ7bN4GIn3sVxC9q0vyEG10VIoz56OS9X3w61OEN_QsRDv7OzMLcEL-E2KWViFfEGv-4UM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
