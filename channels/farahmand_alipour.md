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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 13:46:06</div>
<hr>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgwEm9Q4IwAMIWJ2eIrYpZ8KTYKw0O2SHAJ_VlQWbc1sSFk2sxgecz4nN-WgheF7OASn8w-ROE0krBsnPeH7wd4-67ArT6sLsPdpQwd9NKdC7pyjPdLr8FDoMmKaoF20OugCZOKYNlSTuiZnzm7eGpAWy-NiOxuCDtmk2bd95L6tUMd_W99JhpV5GXHXVLorI0cIwZ_DiPeUkiJGfRl7If_gRFoSfzQuy_ZXF1O1GzLOMzXF49MvJ7BXc-oF8SqMr45TU9L9OdvAd13hsLVRb1UMaXohn4PcXXlLAukShVWFgO8nTU6qHzO1mUWt-0oqkcFGAhwmnWA_KrIuVhvEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZxxCUvw4IY4Smjf28UmKzRNRjl0GFjL4z9wbfAD4ZjXv-T_KYMemi4S-DN_GrznAtrqvv-3-x8UUDHpl-YE80v7QKYrt5qM48lZQiyezO9-f1AO0BG0ILCDMIBkwryz0x_9VSuaF68Ol47Yiqcm7hQWBKpjlePx0IIBtyRWTIgMFsWakzRSUn8bCikjWg3WHQeqMJhpFSUqQjzqxCIstsrQ4FfJnGJ9dGecKVQWu91uKYbbg5O79rpUK_DIU2emNYJBgWzSXId9z4zn_Oc7PzlM48U29zw2hHxCflzg-FSInc9mg97Clkw4m1-wcrhsIlBOQSrDOumbMv9cfPqlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMD8LmlF9dtW_n9ppKxRpI6QEXxtDEOZeKd6k5r9jaHphX7ZuB2x4FOmuvzkpSzuhK3CooFbmgshifVFysRdGWvr4Pna4MnxN2FNp-esexuuFvmYCJAhgcUfSgH8eqhwpQkR6Yg245Us02bJktom1ib5QIBAIa5PgJ5LGU9C9FTumRkNzb41Q-lnnQmJx9sEq1lhVY0nerk_x5bbVpnD0635S6P9iWvAp_YA4V3r5IlbLiTJMlJLQjVjJUpsnEvndrzup1rLMfURtN_cudyC7poMQIUA-PiU7xaE7158WF3QTASLBthMmRX8yv8yfsd6sbX8zW4upsYobqvtIxBRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJ6rdm-hlmlotnbn9FaHxJ0RX3m0GzYfYxBtckZb0nIVWIxdx7j3lcHH864cKmsuIm0dwzJ_y3pBMEhdxArYfoBASdyluMci6fDXNIOVO2ZfEVlGnnd1FsxHIjDavIXSJWEULKrkwWBJ_fE55yeUvSO5hfN2ybvq2YBoc_Ts1WgzkBvyCkvriILoNLFpkToCbfh2SQfw92mOVU-kT9PVtCbyXf1bqQIwKdbg3ruF2SAB0GRlHHGLSZWBQV6o2sSUAsnod26XixMpiiMLAwZK1FmeCnc55yoqp54QRTdCTecsWubf5pSrh6dfhuu7kojcma0VHqryzf207W9pgS5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlNGoBP_zp4PgiwudZkq5odweOQ2uaMM_6xVDo6Dq8arlPkda4xu-ttOOsPaAoxXXOhN2QCTnYryoFJPK51WUha-2civah0yFAJ50qrdmBcdx1_K0_NksdVS-KAGY2HA-59mMw1ksy4dqE1Ec2JU79SC2_c3OQBDbR46WAQzXLsCNfQuLsauWQ1FY0BsQupo6VvJoGzpedWIyfWGiiAcYBUOp9Mnmmenp-2uSXfTkBWFzCzrKFdwQyDP_eerdTg_IruTjZVfj9qK1LH-K4L7TEeBSDmH36HEwKMgs1_o0-l-Fl8LCBRFh1RGnWpcHIUhMlcughL1qWMcDLfqOC8vBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcdmousp0lVeyaVGAmZ5EDquZe0KQ9zsmf3709S9R8ZeqxtePuTSnNDAXcUPwqbAAHKBQKXZoHHu6oJIzGuV5VAaxi6cA8wfLbAkC90h-w-mFZ0wmt0C1zNKC9k96TcPCgbpciThDLa1s3KfYo5z7IEPaWiO-1RTu3ArcS4W1HrK-zznAeqajy7Q6N_0RRiLmoTvJOSRDxyf4LVOc46SHTMfwNXtXFyVocMmTS8i8HJtNIexcnsZAnW38YOKd0WH_uonoTL1Ni_rhglNN_gL0JzM6KI-YEtIWActCDCfmGzrOVtwMoeUrxGjQBw3tbZkS35k7lSzsqbSnnbqfdYzMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=RRhHN60ZfhBNc8RJGl4Gyro93H2X8SnGbTFuSmZKFKgAMUgyy-4Tc3MC7ADERK2MzYqPXUKnKG6-pdnb6EwUYPAc_6zCcqFF7a2S9tABuD4HG__sfivy9fvF7ggyl1OevcsAFiU_65i_DZUDrM-AmgPZytxnRoBb1AtSga_oGGYmbsx44a2eECfpBBxfdz5v18SRwBcJ2nE7lR2Pk01yKXYlY7TjBhTswM7y1F1on5uMZiID7VOU4tqfoZE0Z0rRQuWcEzvgHXlJ912EQFqERNIYVrJEsX-w48SAyhEZQM8PdFJ6wYxBUnHoUEGGvVMRxps93IZYqSysScv51hHSoDHAWe3Y8RAjPCrxbRUXo2V_Bedit-tge2vVd_UjR2l9zTYOpbMnhhnrW-89KCbltqpg_SGuZlPjl88b_s-b59zlnDBno4nOuIoKrtWycBg2Of61pTZ6BWhtr7T1Y9yItMIZLci0_6ZeKbkZgiZxz0d8rGBp4nvSv5XzVHXcC4zS20Tq30HrfeVkZsXm_q1YEvjBdtbLgtzXvHrwM_Dzj56HReuMKac2DWNRBQjJHX9Tfuk_aHJ0q3YRSoX6iOKk_DTMvWDeQGHavOM-sMNSkp6nOy499KI3J2VNeDmtJxPNz9uwYCGvimLs4tgGpC23tABrbTzkBcCdI-13YijRXm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=RRhHN60ZfhBNc8RJGl4Gyro93H2X8SnGbTFuSmZKFKgAMUgyy-4Tc3MC7ADERK2MzYqPXUKnKG6-pdnb6EwUYPAc_6zCcqFF7a2S9tABuD4HG__sfivy9fvF7ggyl1OevcsAFiU_65i_DZUDrM-AmgPZytxnRoBb1AtSga_oGGYmbsx44a2eECfpBBxfdz5v18SRwBcJ2nE7lR2Pk01yKXYlY7TjBhTswM7y1F1on5uMZiID7VOU4tqfoZE0Z0rRQuWcEzvgHXlJ912EQFqERNIYVrJEsX-w48SAyhEZQM8PdFJ6wYxBUnHoUEGGvVMRxps93IZYqSysScv51hHSoDHAWe3Y8RAjPCrxbRUXo2V_Bedit-tge2vVd_UjR2l9zTYOpbMnhhnrW-89KCbltqpg_SGuZlPjl88b_s-b59zlnDBno4nOuIoKrtWycBg2Of61pTZ6BWhtr7T1Y9yItMIZLci0_6ZeKbkZgiZxz0d8rGBp4nvSv5XzVHXcC4zS20Tq30HrfeVkZsXm_q1YEvjBdtbLgtzXvHrwM_Dzj56HReuMKac2DWNRBQjJHX9Tfuk_aHJ0q3YRSoX6iOKk_DTMvWDeQGHavOM-sMNSkp6nOy499KI3J2VNeDmtJxPNz9uwYCGvimLs4tgGpC23tABrbTzkBcCdI-13YijRXm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=ssscLKhiT8ri0eiBsNNlFwEpmKWqIKZaShI2GTXbg9LNXWT3O3YoSm8btR4LmrkadcMdp28ucbsXN1OivlDeEAXY6wRLbeVfwfwJF3PimcOIAnA29idaYiD5dYRuqcUU_1RASF9zcwZTScQY7lCp4OB4sH500giNE4G2_X_TLqJkLOOjzSRHkdqZ-A_UJH0AqzcIqg0sCwYdT10o0auj6-81GShd7cUw5uf3z6z_rHmzUBmOqSQ0rpyNsKbzwYJTGzj_2pRlbNcCmpptz93LxRMKeBPl6ns_h59mMVHmBd_mDM4fMUgTifUrdTxIpnBzIakWjBg8TUFxb7RvsF4ifQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=ssscLKhiT8ri0eiBsNNlFwEpmKWqIKZaShI2GTXbg9LNXWT3O3YoSm8btR4LmrkadcMdp28ucbsXN1OivlDeEAXY6wRLbeVfwfwJF3PimcOIAnA29idaYiD5dYRuqcUU_1RASF9zcwZTScQY7lCp4OB4sH500giNE4G2_X_TLqJkLOOjzSRHkdqZ-A_UJH0AqzcIqg0sCwYdT10o0auj6-81GShd7cUw5uf3z6z_rHmzUBmOqSQ0rpyNsKbzwYJTGzj_2pRlbNcCmpptz93LxRMKeBPl6ns_h59mMVHmBd_mDM4fMUgTifUrdTxIpnBzIakWjBg8TUFxb7RvsF4ifQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWNRxsAF0rUvELZUUXsYTGv3UXunPVCDuc9_ZduLUyXujFpOAUXe1Va8wloP-oMMSHst8beos3UaWZ-Z2x-Mbem9BW2KwSbKGW3UuoC67c-R26ne4t45qGIuct32oMAphEJXABqdZXFEAFvIRF70E5qrCSoslJ8BvbFlo-6h_AiAZOOfk59kIPRD4MdBp1T_NpnwDox7vLPPe4L9dhnbFi2k3NvRj7qabe-o3qqjswbH45DpXMzlOtOCve9ea8yIw-FALCPI8B0z1G1pLh7RzDOsOmF3VGR5esbiPpRQgWmyIPFsGnygicZi_thJANcwBSz6FdgP_LNfYCWdsPPamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhU-rluI6f7XFBmKX8sK-VQGJI_ZpzDorVf3w_OvNBpKHPfA5VdyUKk-nefiVFaBnP1o8PkNvKWiIy6f7TBExz3ixPrfCbqDicRPUelav_lBSmW87pN078Qnd_-4DuJN3tpcsUwB-HrxKbkr7b7NbPH691doDtLRSTG7rPjXzE6GrH0FuUqHYxFGezmJQOS62A82uD7TICFlxKPQ9QzRlm_BFH5HG4mRBlVn0cjqkf-PCUEhvr1ZTxi02t-DPRwdXUtJxdaz4LEC1JbEcN3lRe4akhENdTVsg1B9pEhUzPE5sY4bHaYUXK8C70U8rgW7q8muTN-OX8FYai8hEpYPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uar0AZ_fkaQKX8zJjbi1AXi9_PD2Q4g8jZij7CLMfAHfY1Cimd5cd44_u-Rv2le4q3sZi07ri5A7ecGwnRuNZN16u-UFdy4TvW35n4KJBofOZvR9mRTCnHIf_d0X8z3DmZ07uHOHL6qYvQmaCKbdfbghpTwHiXjv4MJ_HQi8imeDgRsbNJwerieAAjVOvlw-ECWpTYEEg6pjIdznRDMgBNcGQCTGd6cedE5IoL7IhO7cA-siMt_oJpAPqxPk0a89x3JPq572yMjxaacYAlth9nRqrUS3oqtZl1nE-DiBij9Zu1hthaqbV2yb7aUTca5XWVGoqAdBtHpDzrxyWve1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEjc38OFpXd9kvRGz2vfRcNklWS-UpfZYaowL2PQAE8pq7UV4Mc3NtkWmbp04DsVEdNjuZXpuEqj1QhJMzUVTgcmfAtWPt6SLFQlK8uCD6hApUZEc3ahmwKiZeECfv7H9uReKFRvKIGv0xuoNk-MIE-Ku-K2yfdNA7LHudZPD30Y5tfTPCQ3nBQY6OhKGazoFsCltWbO2LcDD01pizwz195QJtHeh4C8jaSReyoeZQQ-PmIvcB9UPt6ou6agRh2BJ-GaIIBaSjrAL8Fw8pV_WchF5-ARc4CYitn2YjgmUWYNpqpU3Ehe48LwZGRxd8ONwNFohjdRkNWBfXVLd27m3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH_5S45MxowlJZKryRExdDv_YoI313N6BP4WuFfM0_dDBGIXRA_HeUilF1mZm2gQ8rQH96MuD5E6jXvzeXMjnpGwE_-M4Iltpjbsq1UsaFO_Cu4OR1Dg6vmzrn54i8qwQ7OfySz9oCihr7EtQDUDdv5qqv5tF2FQpYCbNajhLzk_hjqyqQDxHyrnnX2aLccb4sKepy6T0SkU1pk3DUfwPSkJU0_nsz-2WlvZHZXGzGBaiuhmpc7r2ooU-BOBMpWX4Y8IWcuOEaQeJw-iG9txi7iz62R3a_9NZljFKOkBx9dYIm6fuYivQNhoikQzw_rNVRt4jtbU5Asb3xPqEWxpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTJP27xBNrimaOCWsw4qW_w9uYd6tWpqsyeoEtiOw12zjG-SD9AN15C2TGtBvTIPb2jULukfaQOnftkTuo7EL0YnlCWWZaroF_pfypSWfeClgylsOeQe_U0QDc7xtfUHSKOkxBowsgoz16W1lKSr0VV14C8g3POTi011ACt-qxJLRqGaVwJUO3Wl8PbBDW_jL29N-jVk4LSf6SriQ0kLCGD3BK-YjLxz8lcn4iVkR-pRphwG7t1Goj-4StgC0oM1R3gC1x60EKrNxk5yCgarTMl2D6gyufWqq_hNp2NZVgb9sHPVfanAzSbg78AYdyaaQWNF9Z_OEpAE6zF5Fn28uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv8JQNvV9PAemlPh-3RwrKWqmoLpv83Lwc6JwzxXWrG94ruldB3_e-6LIbIVhwvsyM80zbjGX9gwg0sZidQwMyPQsuITKkPwF8JnQMLWp2AeSymmIb3MyUwrDafgzG8sS5Gt7jKv3YejSO4OyKCR34Z8VT42f2KTvYbde9Sllbl7hSDteY1pYdxUkuxmywVOH8Gi4Ye6PcAWyP9zsmkEkQYaoL3YoBeZnze55_WPA07UMsBgrcM0uZDpJ9v1jMAz_kA5u3uEvDa7OMsi5w1hIO06riCjrOmrDrESTkZeGUi89FcOypSDVwQfmnzp7xFWa9eqb-MoHJBuyxElKD9ocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ciACWeGWNt74W6ypfyY2NNYVfj-kio-UnhoCWEUETUzUuBnpXZXzpRRjpKvLysHbRodICly_8QwkVTe-8-HKUJj1ewbrmunsGrAoXw9LVWiCi2yHeJYL2ZmYIMXz8nqsozhCXDx8s7DYx31cTnPvKsAxjP5aodQ_D7JGsLGOhP8qoiCtO0QFSMmGntSMN9asY01vEwbkpGG6fHP8Smh9ZVZRgtxYM53ZmF1hDxQReovpDhYhDCfr2Uh3_y6zmoz6SnH-FT2pE1mR6uHIJrUe820a275wChFrtQYbS-Fx0D1k2akd_QULKO1MNtjh2BVGAfX65oJ4oBi1NFgXP4d8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ciACWeGWNt74W6ypfyY2NNYVfj-kio-UnhoCWEUETUzUuBnpXZXzpRRjpKvLysHbRodICly_8QwkVTe-8-HKUJj1ewbrmunsGrAoXw9LVWiCi2yHeJYL2ZmYIMXz8nqsozhCXDx8s7DYx31cTnPvKsAxjP5aodQ_D7JGsLGOhP8qoiCtO0QFSMmGntSMN9asY01vEwbkpGG6fHP8Smh9ZVZRgtxYM53ZmF1hDxQReovpDhYhDCfr2Uh3_y6zmoz6SnH-FT2pE1mR6uHIJrUe820a275wChFrtQYbS-Fx0D1k2akd_QULKO1MNtjh2BVGAfX65oJ4oBi1NFgXP4d8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqKEKJhxxadATF0yUvtw3mQQDWS0HJMMnRIkYLpwDKH4JDMiVznGn6qLAtU1BEztMIO2KOzel4e2Kzw4sundvncg8Ky1tA1k1bA7HmXAO5gtce1s94xTps2FTk3yJhH6-GP4S30lFLyQRYJLBPtgNL9WiMbAHT1HbjE7F01a40dfpQzdaZConzZn4ChTUX2KwTRgElkpirmxVrIIK2Ybs5wrhDiOzw8Wb5VR4JGr_GaPlf0bb_O3TxaESSLcCBamLUarhYlXR1b_KMiGjLhkdmFkCIgWtAqZcNDshD1wFBjHLEyYuKmTRuIMPIug3Fz5Y6zaqLySMgNn30a-OEqnGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGE35kkjM-rJqilsdwo5Tu44o5KwlXMHEjThSyJJOzexk99KFDk7wI_7rtlHFtIoxySOK88SPpSgV70ZiomeYu02Ut6NkCTWW55PyiKC5QK2MFe3ofOkMG1Z81mxSTqIdPULZmqzA2JOJJbIOZez8smFjiJechkoPzG24IFQSJIFxhMdBcaHOQ7ARfILQMckh8GvXngm82mp1_PM4XbKUnpFDHs5S_ZYuAWnfUXtgDffaO-mDeHxUIPrroypu8XCfogwPL6jDO6pQsBuDByJLuq9C54Uc7RSLALDWdzcOuTZkZpAKG5VbarbfKOE6RT0MzVFgx3cirFxYPI3IFxak86o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGE35kkjM-rJqilsdwo5Tu44o5KwlXMHEjThSyJJOzexk99KFDk7wI_7rtlHFtIoxySOK88SPpSgV70ZiomeYu02Ut6NkCTWW55PyiKC5QK2MFe3ofOkMG1Z81mxSTqIdPULZmqzA2JOJJbIOZez8smFjiJechkoPzG24IFQSJIFxhMdBcaHOQ7ARfILQMckh8GvXngm82mp1_PM4XbKUnpFDHs5S_ZYuAWnfUXtgDffaO-mDeHxUIPrroypu8XCfogwPL6jDO6pQsBuDByJLuq9C54Uc7RSLALDWdzcOuTZkZpAKG5VbarbfKOE6RT0MzVFgx3cirFxYPI3IFxak86o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BSu6gTSLNSngeaDbke6qSUdDnGunCbvXKeY1NlwTPTujPpgmbupr5q3-sHRzT1uyEoZThJz9q0NIG0o3iIjpvYdy1D2G-_OeE-KmvrX7M2frn0Kk97fI7ha5zbRGjtHsLBQVQk3Zg6oL7iMKLSUgGLC-0FDmh9uy-j8n7u0xnbMRLfOMj6t4GvxO6pqjOq3FbUPoFhh1HRDxCgtT6oa_cYGvbreNVQPvGP45KUbwlOy39MqqxqGqt86aoUGgBTdzcngI8Gdws6A-024pXJBs-ujjBntpD4_IyRruQpj__gT53834VFWjZhByrzEnvskYXBd1gvWxpIOER0pOQAE5ma0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BSu6gTSLNSngeaDbke6qSUdDnGunCbvXKeY1NlwTPTujPpgmbupr5q3-sHRzT1uyEoZThJz9q0NIG0o3iIjpvYdy1D2G-_OeE-KmvrX7M2frn0Kk97fI7ha5zbRGjtHsLBQVQk3Zg6oL7iMKLSUgGLC-0FDmh9uy-j8n7u0xnbMRLfOMj6t4GvxO6pqjOq3FbUPoFhh1HRDxCgtT6oa_cYGvbreNVQPvGP45KUbwlOy39MqqxqGqt86aoUGgBTdzcngI8Gdws6A-024pXJBs-ujjBntpD4_IyRruQpj__gT53834VFWjZhByrzEnvskYXBd1gvWxpIOER0pOQAE5ma0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndwWQcf7r3cWsxdWqxVZTxbmiMhQqpCHC6MTWSeKZhNjZI6njhSz_gADux4d_qHSpAaNJUezIxSTIotpO-sEyw-9uV9494KGL3pCGJ_aZKMHv3ujNB-7WYG927N6fNLjv3pmuAT1bh7_ANTqh04K7ikGcDasRXS4kMdIfUGBHBPwpXd-IevlOMXqqf60lTegqYk2Q2drC5_6CjOGmAZhMkcFsAbDapHuXlvSfJG3dYxdVBKUihI-Y6MU9pUsUTQUm4gFaihC4Ozdy9_xSh8mc6pJ0zC-wcSZZPYsstOdh6tfylQFkUuZfgSLpccCaLSzmYwfNf-aZJLCuK6UmF0dEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfyyurP9GxkCjxexy0RENVcVt3Fxsqu-qBzT-abiyRFnb5260gaezaEpPa0qVaal1aFn_Evs7iwrGve_cshKZCkCSvfUzh_ZFRNLr0sDvYSrIPRN1BL4IZyjv5po3X79eJj7G6MgbnKxk7TpSWBBYKdOvYgRn6MGVBJIKFOOuimbgtkX1CgCEq5WSIqxMD2MwDJ3hVfdf_XBM8LplOE29n5TwpjERHE_jIOVGiclpvCx-OupKsueqD6FVIgJ3S0QM2I6IpBXmMvhLFfnMJM4c_9igULFnTiWhI7LqpoTwrHkrxEWpr7pOyfTCE39U6nyrm4vUNEMnRwJUcUQugKrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSeU_nzosbYDwUVAo5IeQyMcvbHnBKRuQWOfvGIq279yaCGMcXilAIOn93sc3T8SvwrQwSsTZiMfp1KMzS-k7fl_oMuG6iIoco_lMSIbz0RNBouXjZA9Ka8dh6IFnND8mAiTEK8C1OZ5E_cBU6nAuNXpeUcyjKkFABaJsdK9qV0eUW2MF-MFyQToQ0ZS2FDlJ4ALQgSPI4fPiqNHaEOFE9a-zPoN5LKZ6ZjUpPSrJxjSE_aahPd63Aqd4DdX3jFE_o7EbXhomQ2rkf31v-OImKjMZkfVrdDuph-u2u6REu-OH4mWjLICYbJaOAKV5dXUxtgnkaLXMbvx1ba9I0sJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goD-OwaBoDaI9N_IpAatjOXKhiscTRrqJ6czHZMhpXYo63-FfMYyaT-rKhkDHmsaB517P4DVNHzsmC0mUnUetYtUAWN_LYgUF1isIrwuCzsuIQZZbRHQNFtZH_58LNOfbw8J6ieyy3-yiTnHhzpncn2t_O-jmVaXam3Q3bMz5oYZp-b7T9gVVnPQtTHng9jisIRozRXGG5hJMUZb_2APqMgdPZ4JN3Nz7eIekBS_D-keC0G4PAsP4CNQT8h-pz1J1iIOT9CsOOItw4YuQ-JE3wd8-Q_rAW_WSXyT-VkoHXu421iucsKgsj4rJXZgtM1DRaGM0qrAUr2pJtlVoXLdmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrRYa2jxP_m_zl2Csz3tDmXSnquVvj5kBodaKT_XhVYeUPxO5k4IwiQYmFyXI_cII84gASxQ4WBvVOHtgAacHMg402AVVpGVZ5LYuXgdIWKac0B_inyghw1tVkDq6bpCe-QdXZt5OyHzvY1rGAF6De2wXoA_AaPSW-6tvug-lR7Iyw-HV-reksOC6y1tvQlEmunnpKTTwWhZpKg7hA7JXYBUHCHFU7FE539fpxnxXPGRRTukNwsTlVTF4e2kxGIL2J_Hbpv2LFkX54vPiXUAUH3UZykVQahM6x7hFbleXTYxb16GLjaTw6Fh4dB7qN_fSf6vSNEERU5TuoygUzqNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0W1qAeggYdlA74qk0rH31kwtLXT9ABbrAPvSTu9s0yLDJ_Sf2tnXedrqdNCdDbbgAkJFuscrpkUBO6V4oqX32X_mP7XMJBlcPIQlA75tZXV8sIvChQoKcYjr4pxPk0uQgvRQAIlY-gbCo_XlTuoTBj9uVO6a3jxK_HVHqTdBioBfCoadZyvkuDvvhAez_KbAoPvUhHUjwNEy2NsHe7cTbXhvil-UCl0iybY5CL2BPf-CkXBhe8y3_Usng3aBVB_k1EKBxDZ5G_NikVRVvzhwBN38kvKbTZ5mo4Az3NtAREoBV-80WWYyMtqr3C37kTMoTdxMJLTZib7z-1W77WeNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyulpprQe6w5B2fwYaFw8HuMQo38-o2voW3RMWzMIOgYf6lKOzL-jSxTdBhp7RHC_AAYaF1zTb8YXe5MSzuV0Z3yE-JzOzHML3TdJuxYz12PAQrtwtXZRDnUHWXkX_nU688K-0Rs1IOAW4T6Kq3l4w51gGXmMs6QE4w20qK3rMJRakDVGg_nasipP0F76-7g9Oy3SY1WWiqVTZUAWH5QdrvLM_XQKCALtLKuCjtno3jXlNDCMJObkFkFf56hzGmrOxxg-CLyqNZaSTh5iVb2ggmU6Fcq6MwvqLGqFU3h9EB5z1v9fj5upbHowN1PIPiemvLf9URYWXDPSDduinJi4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZdb8uIGuzJ9e0_h6piC_OTsQBTF0vmGCOl625W2abVWUGOaxPy3Qu8gIDPwuNKDjuWz40pD5EMux5o0SVaw0Rh_XJjVfGQlYqfH_yUYu8FvTsVos08_9IwgKqXpC4atJ9eduMEaSnIWIo3q8kqHK1Sn7XBGrjMcHQZ1iC-1KtyAqJf5DpF6y4_Rfk9tYF3YHu9FnSh0-VFuDWU5w1I2QvZ657IRz_fbJo3uxRZ1ZXeVoqrCReFJs5XzakisdAApj0lrQw8bkHOgR13umrUSsozkX1yhj4Hzj4Gv95tltOt5efnGoOz-dfW6HqPXJXc5X3oJQmqtghPXDFUkzXu6pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtZyJlQLGclCJgtRFpD0KsHzD-f2jho4RRCqI9z7tQnKaKp-npbTnQ7nzgugdfT81y3lzMWlLw1vtVzRyjz7jnHiTMyl9eYWrVNmiseKZst9RTId5M8M2nYu4YehRLAHB4glxBV9Q4Kos-mqJ1_5BbykvhxeRSspv9sZDRds0eleJEqZimLptAnuPUI-6kQ2CagSka2yg4ckiQgU4zur9II5OmiKmHzWZYlPXSPQ54j9lOVr_K9UKUAQm4q5CU26pftTrnEl6o8XIi4urwuROhBmp49ijdGd_L8caHayQ8TrIsN04VRO3EXDFdC8FDxGypjlvgr_20ZrT2EJAyn8ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT14eTDEvOYFGYDlUdOozHzreGEu1RsqKjPHQy4z3yX8n3XpF7P96JDwXWqyb9rZvASIln0OBOYfLvkA4CE2nl5kgOrhAsCK7NsmZ9oyDJDIcmG8oplJmMgaIk7torJcMg882kHII-YmGtGjgfB7MR5PWy5YMqChIX5SWkg5FxvDi5GyZoedyk6JIB80dOIykJGvZSEEvPrR0XPOsc8ghMRLETOQ8JRFZeMtKVIDxwVq_0EBuF-ojs6Cmr-_1qW4R5zBgvlaLF-lyWJcqfE9hn8Rrk1A-Zr_zXEOlUpEUGCYfB78I0By3bT_wrJ_GPwmzCq4UvZgzEb31y3DvAuSeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEpLQbTQdyyyhcamn0C8CjlvS9s003wJpbHtSxJeiNRcIYVzgiMLSrH1V0V_mQvSpnOjeU7nfENa9zlj7R218vn8kldlFqQ1YLx-AU8-a_lE7tVeNppVjR6chdQ7VmdFDmg-_xTUi17KQWKwJWAnxUKp2VgdDkGj9GUlKm5GAsgz8F8OVa8VA1PBtUue9kVVEPwi-J-u-lZyTzBpeUsa-I_oGx-RMQ7Nnczw8vHfN2OzVoYGuXDRiXRXASOvWgR6rbtVm1s76xMnvB1hjuFakOVvLGZu0xmytMmY4Dky65a_hE1x7YQoVBsGaOBF7WbbipiBeSm2LPndLENHPSwcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQuX7QVTpmyQrgkQgbTmgw5gd0kVVy8d_vOvbDJ4I2PjokVumX-_latcCXWGnCaT4YgW5kaRykK7MqFACcRaaaVk7iyoc2_wsk34FA_zRDSEMUC5c7EmZcKxpdlNpV4VCVJrLOGWtqWx45xY9LIVhLkeyapJB9DFJc6lIlpi3-X_6n31hKGMM6eD5SnYFUT3M9jzJ7MzbggrLV9i00dI8M3_882-KVYuWlmt0oii0_3eUXEcdcSUafsrlr5iFxdEB7Rhiuq16lXrRakFbT_S5Rmq8ODqutiRu1vDkNnr9svVbIzuTRJl4ICC3qZUcuCp5D0A0FPQUZ4FtyVkGOZOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMEoGVHEx63nh2it0_b2ha9Pk6_ASsiwot2b04m8NqgyFIApGn0mpNQhLqT_gceIPbnKuzD2FNqLHt0XH7UrS7T5TVcCa0Nj0vTTS5E4ymb9bpN3IGvjuP-Mo5R1nBBv5ApxBev3HY-H7UmGLLhAECnYk-KkbY6LVtCx4nc97bnghorPLjK6p602Fk5PZj5d7XYmusDqnzr4Qrz9WkVzCtEix_6i3CGyuzV_JGYEVDOhLST3UkR2IXgUyjELqrCanfqjIpO1Tuv5WscxdNutTnJf2pH86kPsgZylWHsNtYscEvsMKV3fFbBEJfsVpbUk8HukLsahwCpLoahPOCggY_UY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMEoGVHEx63nh2it0_b2ha9Pk6_ASsiwot2b04m8NqgyFIApGn0mpNQhLqT_gceIPbnKuzD2FNqLHt0XH7UrS7T5TVcCa0Nj0vTTS5E4ymb9bpN3IGvjuP-Mo5R1nBBv5ApxBev3HY-H7UmGLLhAECnYk-KkbY6LVtCx4nc97bnghorPLjK6p602Fk5PZj5d7XYmusDqnzr4Qrz9WkVzCtEix_6i3CGyuzV_JGYEVDOhLST3UkR2IXgUyjELqrCanfqjIpO1Tuv5WscxdNutTnJf2pH86kPsgZylWHsNtYscEvsMKV3fFbBEJfsVpbUk8HukLsahwCpLoahPOCggY_UY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=nCpR9ufPzzyYmBL-kyM_Sin4lr_SyU0kFCLDB9lZYEixPyhXwR4d3dxc4S4U_ErzLGq55GkMuocuJpbI4TjQHjyifLCQC16SWhJhmfxPwbRO32ufJ_OlWdH5TVqec2LWyuNBXt_j1_Nbx4w3ezQHjKM2yLQucTNuE2ndyHH6oq6Xw3nrA-Y2Mo8-BJysANsoaCl5xPf7LijP9K0JLQ0D0s2yFR-StnMIzebxH4BHUgOHav_C3hImMtySlv1_giDmV4Va9v5K3texKQd732fbdUz4pYDpJIY5AxLimyj97zRjfRYZcRK-83H3AzoC9wZzg7uqqtHwo4sfaZnI0Vs8_RsJM4YfxdD8GQAuz7StwbJlb4DQDOYunNk7yicZz1T2KXEw0xRZN3-Br5VqsEmwwajFYvOqYkgV7ALJ-whJN6ACirSrFQ8bJEkNrd3w9MkphoR_fBu5DulbJzv8Z47uGICFdmQJ4fGQA0GikR71VS4Hn13p8gcKEJ4OLdQAXYfQZepZYZOJw0FiYN8OSjk-E3hVjbJL0Ryau_Aq_4CppvpBnCp6Xty80mPrG3XR3PWzDZDg0Nnrg1mk4e-ylgk_f1BiIr7wV9lRhjR96gyMWAzuDpIOJLCiUfFJ-wqaNjQ45be4RIRIa_GtevgVx36X6ZnqzdfIYoPmv6HB12wqidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=nCpR9ufPzzyYmBL-kyM_Sin4lr_SyU0kFCLDB9lZYEixPyhXwR4d3dxc4S4U_ErzLGq55GkMuocuJpbI4TjQHjyifLCQC16SWhJhmfxPwbRO32ufJ_OlWdH5TVqec2LWyuNBXt_j1_Nbx4w3ezQHjKM2yLQucTNuE2ndyHH6oq6Xw3nrA-Y2Mo8-BJysANsoaCl5xPf7LijP9K0JLQ0D0s2yFR-StnMIzebxH4BHUgOHav_C3hImMtySlv1_giDmV4Va9v5K3texKQd732fbdUz4pYDpJIY5AxLimyj97zRjfRYZcRK-83H3AzoC9wZzg7uqqtHwo4sfaZnI0Vs8_RsJM4YfxdD8GQAuz7StwbJlb4DQDOYunNk7yicZz1T2KXEw0xRZN3-Br5VqsEmwwajFYvOqYkgV7ALJ-whJN6ACirSrFQ8bJEkNrd3w9MkphoR_fBu5DulbJzv8Z47uGICFdmQJ4fGQA0GikR71VS4Hn13p8gcKEJ4OLdQAXYfQZepZYZOJw0FiYN8OSjk-E3hVjbJL0Ryau_Aq_4CppvpBnCp6Xty80mPrG3XR3PWzDZDg0Nnrg1mk4e-ylgk_f1BiIr7wV9lRhjR96gyMWAzuDpIOJLCiUfFJ-wqaNjQ45be4RIRIa_GtevgVx36X6ZnqzdfIYoPmv6HB12wqidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXTzjmK6o3pCCLghaQyBQOVkR0vvCC1Mepiq5KRGjOGsyjPautB1vAVufZ8sC8XCtKzd8OBAm7guutDEJD9dn-iG5ovb8OoC4mnN2ydLsJOydKp9Y4E6bM8NcCgwyVM0_x7UZlTwrxyY-AVYiT9RiRPkurZxhw01CmAmzKe0dyB7cR0r30gNW928eLyHelvAw_MKLFfNaDEhdbrYW9QJQDv1BnxVim5sAmXR3JFUfWdEGOYixnil3_tOC4kTOPvQ72tEUbj-2XlLlliSvM6zGSOGHgHCPWOK7Lo6f1I9oyg1xEN4_UqX7H0XgvIws5YIjIM0yFyZT6_U3-HRbUI4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=NUwnj3xsnW1DEbvIXQ9PN99zShfbK2CEn3CokM6ijTsdzMXQvjW6goJFAZw6rEPJfCBEpbXdIS-cBgLNUbOAzqNlve51xaxjJRt4yoPKaNwtLIvBya5S-OOwi1OFQSENtj7vX5SG5_i6yXqXdGzfmDeHlA2GKdmGTUM-CfIXX7G1Z4zIL-nTlAdinjMMxyPHwN8un6qMat8ihaeKMlCcvJa-rBWbF438PKGGi2No8TPFAcBrYYT9erQSQsdqlz9uG2ZBZhIJjYWGQJiayBZArgNoVdNReeGLavxiONPrS6L6YgGp4zOOcbe7hXh-JMf7ZRhIkaT3snXeTj3urDwvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=NUwnj3xsnW1DEbvIXQ9PN99zShfbK2CEn3CokM6ijTsdzMXQvjW6goJFAZw6rEPJfCBEpbXdIS-cBgLNUbOAzqNlve51xaxjJRt4yoPKaNwtLIvBya5S-OOwi1OFQSENtj7vX5SG5_i6yXqXdGzfmDeHlA2GKdmGTUM-CfIXX7G1Z4zIL-nTlAdinjMMxyPHwN8un6qMat8ihaeKMlCcvJa-rBWbF438PKGGi2No8TPFAcBrYYT9erQSQsdqlz9uG2ZBZhIJjYWGQJiayBZArgNoVdNReeGLavxiONPrS6L6YgGp4zOOcbe7hXh-JMf7ZRhIkaT3snXeTj3urDwvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=fbR1TPkpl0s-0q8G-ixWSCcCBCIsrb3dmUf2ABrmkPzAjwubEmcCu7BWm8H05Hc_9gIZtvF2ed-S_MJuw6YHCYJlUiWgRNXupxhbisiyOJmOJjKPbuSsA4beP6Z0lUfK-_vjjiXm69RhgfnP6_WXVEb0Z8fvXYhIxWJUkxLFd_NifS0VGt9fguMHiVZDGNDsU4jyNeG87d04Wgaf1Bd6LQ1hEc_qKno9AQDcrE6bnGvfIrJ0GmfN7270h65C1Z0Oii6o7YRJRVjnm15hxxmv0UwdIAWj_iQP-GCeGX_UEtFrLVdHuoujHAJk69LgUiMSAQDkH-saxtlNhf6S6YTzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=fbR1TPkpl0s-0q8G-ixWSCcCBCIsrb3dmUf2ABrmkPzAjwubEmcCu7BWm8H05Hc_9gIZtvF2ed-S_MJuw6YHCYJlUiWgRNXupxhbisiyOJmOJjKPbuSsA4beP6Z0lUfK-_vjjiXm69RhgfnP6_WXVEb0Z8fvXYhIxWJUkxLFd_NifS0VGt9fguMHiVZDGNDsU4jyNeG87d04Wgaf1Bd6LQ1hEc_qKno9AQDcrE6bnGvfIrJ0GmfN7270h65C1Z0Oii6o7YRJRVjnm15hxxmv0UwdIAWj_iQP-GCeGX_UEtFrLVdHuoujHAJk69LgUiMSAQDkH-saxtlNhf6S6YTzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA4IwJCIinXO5nWRzNQLnNLhkjQ32Hq8RKxebq18E8Hs7MGSYL_pEYY4ufUtI8A-nRlvFrcs9FxcyP4rELT3DeOfsn-0_ZiYpMreVf72kZvqrCtyTwcOFoZWQgB7aAGSS_voomDshVVAsq6LC-pq8cIpkS630NPE9FKMyxWuB4MJmNI6WagjhhnNp0Ci2IPH_fP-3c9rC8ulZFGuhxcpzdPoF3tW1S5PUN3mzT1bPrv7UJ1pimiVZ4ELIDxm2TM7SyktTiDuM4GlU-zwryc1LDY7y94JGVVFCdTJx-2eEQbURXT9E56GQt8ilyjvvOykPfjNtnhmapPlra98jXeWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhjfhsJ140qky_Z9MSXR4C2cwXn0q6REbkXwdIlWpOqZgd1HTL3eD30BHHjsQ1oz1u6G8iWcRP08vX5Hgx_n5IpzdfUVqnCysDYKfgX6V0BmqGszz0H58TM6i8egTNvPlL-epmy4fe3R21meELqroweB3myD5cqDew6Notz_Xg321PQJFRqldrW309VWly7m7_GxFVlj1WA72eAiSXQVDxnvr35F9uwnydf1RN8XGiNmSCAiuOfjiksUvzGqqwjPCbO0MJzxAMdbl5uaH8joKCDlG6g1rSHwbBZSlC9eNlz_kal6F2_VU4Jr3cI8x0TGR9u5BTNCu53G3qkI7F4h-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=aYtsn25yrL5zjS7o_vbrwPoa5tCGY8eBa2wPXrKGZB6IgC_tZTwsevxL-vpO6lZACIHQ-0lFlsYsmCavdIkPZiD-JYr3XADsefFz260hr8NmaQNB8sCxwFjK12RI9Mk_khxjdabUaak7Ys9XTyeQRTCDfjVAzvK7c9tKlMRGonke5vA1KCGHkIi-womt7Z5aO1Ws032Bdm6MTd2xnHfguvQH6APTlzkdp3CkpZjMAfveioEfC9kxH-Exl_baFg4ZMDutrxUsFeuFODiW3yagmlUbRvmENTXIMVoH0oIsmjsx8fEHEIw8__1ji3af7etIhKkNRU5aRZHu-R3xCcRiSzTMQTLwyp9FCuL6HccFzIVq8uuBzlW1Y2K8ftpx1MNKx4dahRtgp7W3MjTC4Lkxov13SPfv6TKlMyCveOYPDlZI-9u2lVOK0i0Y7TGZvfJ-XT5WlvFFxdaYrySxoSeEZ7ZVe5Asae_loYya1ZcshOqx-mK8TBP-_1NX6_hdKIe_Wl3xHg2W2G8cvk4yjJjCT6PgZK0D3fPzXSNdi2lvLop-zQxliwHlL_77RyV1hpKO_EeIskkfSgh3mT-TJnyBvezdZRVfn04aIo5xdUm4VmraoD1rhe-6Euzi60noo5S5VcmVplU6ZQW617lR8GrzFXbB1Tc21HaF9MofU5T9r_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=aYtsn25yrL5zjS7o_vbrwPoa5tCGY8eBa2wPXrKGZB6IgC_tZTwsevxL-vpO6lZACIHQ-0lFlsYsmCavdIkPZiD-JYr3XADsefFz260hr8NmaQNB8sCxwFjK12RI9Mk_khxjdabUaak7Ys9XTyeQRTCDfjVAzvK7c9tKlMRGonke5vA1KCGHkIi-womt7Z5aO1Ws032Bdm6MTd2xnHfguvQH6APTlzkdp3CkpZjMAfveioEfC9kxH-Exl_baFg4ZMDutrxUsFeuFODiW3yagmlUbRvmENTXIMVoH0oIsmjsx8fEHEIw8__1ji3af7etIhKkNRU5aRZHu-R3xCcRiSzTMQTLwyp9FCuL6HccFzIVq8uuBzlW1Y2K8ftpx1MNKx4dahRtgp7W3MjTC4Lkxov13SPfv6TKlMyCveOYPDlZI-9u2lVOK0i0Y7TGZvfJ-XT5WlvFFxdaYrySxoSeEZ7ZVe5Asae_loYya1ZcshOqx-mK8TBP-_1NX6_hdKIe_Wl3xHg2W2G8cvk4yjJjCT6PgZK0D3fPzXSNdi2lvLop-zQxliwHlL_77RyV1hpKO_EeIskkfSgh3mT-TJnyBvezdZRVfn04aIo5xdUm4VmraoD1rhe-6Euzi60noo5S5VcmVplU6ZQW617lR8GrzFXbB1Tc21HaF9MofU5T9r_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=ghwsTIYTgJQx8V7jsLB2hN89WjYXW4x0TrTj7MQ6hPYj4_vQw4H6Z15SmbeLzolfLYB_MHynBPRb76-amSpF32FvhVDqW_wFlmRBXo_9Ctn8yJ5tEQ_8hiPKoCX8HPOlzsVP6EVxglw6o0lOf-Rnizi6hXqM3gvYRgzd7TCVu0DJx6qf2A2K7rDQDlgiigPCMyFaTF4HGX0_f1u6bbkxYUfDay7B40wy0SlrBPucM6grKx1UYN9c0afEaXr7wPofQRG4p00EFANgbE87c9SooT6S3p3HK32zVxZsVnxTc-QzBg16lDm_3aUoPYX1wnEJyVY96_R3qR8kew5dAKbWulana2FEqPI6fnocEYT-kxKzYIAG-qVDXX41RRBxGTrhLYzy3Hhd0Xg0selj5hr7OqYaxxrhYhjzUw7iVb23sACzcpFubcSw38HIklYEFznD1IrnyEATdrDVZB5NtUawHQuEO9neSGq-wUfsn6WAUQbIQTuNlrL0PiVxtOEojxzTSCmWnfUreac3GKVQmYcdl0EziTAVGkZd94LkiU-t4TEZ58DNTOPgXPFvI2EBn-eBRnbDU4rEFwCbeubzBXjA4tQXg5V_Bg9YPqUCWfXLUKYEPFJA3Xt2Z5pn87o-PhHobPo25GSw917AOvk5cJJhQTLbkE5dHN0m_hYvmljEh9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=ghwsTIYTgJQx8V7jsLB2hN89WjYXW4x0TrTj7MQ6hPYj4_vQw4H6Z15SmbeLzolfLYB_MHynBPRb76-amSpF32FvhVDqW_wFlmRBXo_9Ctn8yJ5tEQ_8hiPKoCX8HPOlzsVP6EVxglw6o0lOf-Rnizi6hXqM3gvYRgzd7TCVu0DJx6qf2A2K7rDQDlgiigPCMyFaTF4HGX0_f1u6bbkxYUfDay7B40wy0SlrBPucM6grKx1UYN9c0afEaXr7wPofQRG4p00EFANgbE87c9SooT6S3p3HK32zVxZsVnxTc-QzBg16lDm_3aUoPYX1wnEJyVY96_R3qR8kew5dAKbWulana2FEqPI6fnocEYT-kxKzYIAG-qVDXX41RRBxGTrhLYzy3Hhd0Xg0selj5hr7OqYaxxrhYhjzUw7iVb23sACzcpFubcSw38HIklYEFznD1IrnyEATdrDVZB5NtUawHQuEO9neSGq-wUfsn6WAUQbIQTuNlrL0PiVxtOEojxzTSCmWnfUreac3GKVQmYcdl0EziTAVGkZd94LkiU-t4TEZ58DNTOPgXPFvI2EBn-eBRnbDU4rEFwCbeubzBXjA4tQXg5V_Bg9YPqUCWfXLUKYEPFJA3Xt2Z5pn87o-PhHobPo25GSw917AOvk5cJJhQTLbkE5dHN0m_hYvmljEh9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=vLU-XqM6RBWaoXF_8h3EAxFRF68HDJ1PZJ7D48yXB-L63Jj6MXdMSFekgp0Fba6cX6ZZXD5fdaxJz5Nr9vXOYGMfo4g6Hb56oaUAEmqaZSsFDqhuuQzO795joOm5qR3r3zlZgcI1ilK83RlOnE4lHdgvf5nH6O4IQV-8-WabTAGXvUc0twEBWO-YpfvHxZCIhf9DyL5PVSjNXvndzYohEtJL14hHW2lxSrOwt53tKDocVYqgFqy6JBo9FRjSrVE6rCwYESic_wKNfVJBGildj9LoL-6u1xkGH8yxoumuDwTqnOVOkljlKAcwWoEsrciXki2zPjy7y96NO3JvGQPPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=vLU-XqM6RBWaoXF_8h3EAxFRF68HDJ1PZJ7D48yXB-L63Jj6MXdMSFekgp0Fba6cX6ZZXD5fdaxJz5Nr9vXOYGMfo4g6Hb56oaUAEmqaZSsFDqhuuQzO795joOm5qR3r3zlZgcI1ilK83RlOnE4lHdgvf5nH6O4IQV-8-WabTAGXvUc0twEBWO-YpfvHxZCIhf9DyL5PVSjNXvndzYohEtJL14hHW2lxSrOwt53tKDocVYqgFqy6JBo9FRjSrVE6rCwYESic_wKNfVJBGildj9LoL-6u1xkGH8yxoumuDwTqnOVOkljlKAcwWoEsrciXki2zPjy7y96NO3JvGQPPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
