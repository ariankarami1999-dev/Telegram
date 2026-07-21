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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 11:14:42</div>
<hr>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Y5FN2y2Gp3jIIqPX29_9kwh_OLN0RVeq_wBW1jwlVMgCqP1_6xRJa9rhr-QxDo2xiLCwul0h7jTmWbdOD29MmVtQO6XvnJhvKktWSGvOJxagtJckpCNipscIhUjy6AoLYxskpvvJtDqVx-u0vxRznziromuM8DozpdmqPx1GS5YGXuwnJcssUYWDKlJhO6LhdguJ4e5LPFAZ7fouwJOUVbGqEvUQggOrehIncUSU8JGuYLwUYuqtkmGGlOmkqZxtHGaFCGLxk6JvCOkR2r9Kb1r9zusQyADv1Il_AHlbXafyt1Mnz4nmf-WEGdxHmf2oyDbn6dI_UYC2TQiIZbxHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgwEm9Q4IwAMIWJ2eIrYpZ8KTYKw0O2SHAJ_VlQWbc1sSFk2sxgecz4nN-WgheF7OASn8w-ROE0krBsnPeH7wd4-67ArT6sLsPdpQwd9NKdC7pyjPdLr8FDoMmKaoF20OugCZOKYNlSTuiZnzm7eGpAWy-NiOxuCDtmk2bd95L6tUMd_W99JhpV5GXHXVLorI0cIwZ_DiPeUkiJGfRl7If_gRFoSfzQuy_ZXF1O1GzLOMzXF49MvJ7BXc-oF8SqMr45TU9L9OdvAd13hsLVRb1UMaXohn4PcXXlLAukShVWFgO8nTU6qHzO1mUWt-0oqkcFGAhwmnWA_KrIuVhvEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZxxCUvw4IY4Smjf28UmKzRNRjl0GFjL4z9wbfAD4ZjXv-T_KYMemi4S-DN_GrznAtrqvv-3-x8UUDHpl-YE80v7QKYrt5qM48lZQiyezO9-f1AO0BG0ILCDMIBkwryz0x_9VSuaF68Ol47Yiqcm7hQWBKpjlePx0IIBtyRWTIgMFsWakzRSUn8bCikjWg3WHQeqMJhpFSUqQjzqxCIstsrQ4FfJnGJ9dGecKVQWu91uKYbbg5O79rpUK_DIU2emNYJBgWzSXId9z4zn_Oc7PzlM48U29zw2hHxCflzg-FSInc9mg97Clkw4m1-wcrhsIlBOQSrDOumbMv9cfPqlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMD8LmlF9dtW_n9ppKxRpI6QEXxtDEOZeKd6k5r9jaHphX7ZuB2x4FOmuvzkpSzuhK3CooFbmgshifVFysRdGWvr4Pna4MnxN2FNp-esexuuFvmYCJAhgcUfSgH8eqhwpQkR6Yg245Us02bJktom1ib5QIBAIa5PgJ5LGU9C9FTumRkNzb41Q-lnnQmJx9sEq1lhVY0nerk_x5bbVpnD0635S6P9iWvAp_YA4V3r5IlbLiTJMlJLQjVjJUpsnEvndrzup1rLMfURtN_cudyC7poMQIUA-PiU7xaE7158WF3QTASLBthMmRX8yv8yfsd6sbX8zW4upsYobqvtIxBRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJ6rdm-hlmlotnbn9FaHxJ0RX3m0GzYfYxBtckZb0nIVWIxdx7j3lcHH864cKmsuIm0dwzJ_y3pBMEhdxArYfoBASdyluMci6fDXNIOVO2ZfEVlGnnd1FsxHIjDavIXSJWEULKrkwWBJ_fE55yeUvSO5hfN2ybvq2YBoc_Ts1WgzkBvyCkvriILoNLFpkToCbfh2SQfw92mOVU-kT9PVtCbyXf1bqQIwKdbg3ruF2SAB0GRlHHGLSZWBQV6o2sSUAsnod26XixMpiiMLAwZK1FmeCnc55yoqp54QRTdCTecsWubf5pSrh6dfhuu7kojcma0VHqryzf207W9pgS5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlNGoBP_zp4PgiwudZkq5odweOQ2uaMM_6xVDo6Dq8arlPkda4xu-ttOOsPaAoxXXOhN2QCTnYryoFJPK51WUha-2civah0yFAJ50qrdmBcdx1_K0_NksdVS-KAGY2HA-59mMw1ksy4dqE1Ec2JU79SC2_c3OQBDbR46WAQzXLsCNfQuLsauWQ1FY0BsQupo6VvJoGzpedWIyfWGiiAcYBUOp9Mnmmenp-2uSXfTkBWFzCzrKFdwQyDP_eerdTg_IruTjZVfj9qK1LH-K4L7TEeBSDmH36HEwKMgs1_o0-l-Fl8LCBRFh1RGnWpcHIUhMlcughL1qWMcDLfqOC8vBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=V-GfGla_5EIojnHgbsZVg18Dn7lbQv6aozxX24bwMZhC-slIv8wewcWxnS1VrrrkrJOeJ2lXub61RMh7ezzNIBc1ZXsHBfuwcbSJied-hK2oVS5-baLfEqn0OQxcITrwTzsTiL-e_rsya2oGdLRYOqlhu06u8Yv5Z_q4M0QGxxTAvzaPSrJKfrZjsho0EEsw8CbbewhkbvuPJfGR2ToRAnYc5gWomlkwS7Yi4zRpIaqz0iyaJLQPx4Ma1QB5e-JU6rpZs45nfdxinN2EqJOvWq4y2Vg1sc29otF9ICWCOgFniEP5zwXBM5YuzUj_5fkxygDEUlfzPxDq-JOqBYCtSZVTZlMrFgpbRgAcpSQZHkUlDFq8lxhZ-sxa0UGKSUdsqaCWDT8ZWbD_dLkVYXkwVL9F3O2S0mOTvxhAOXww7apzsfJHRR67enkf0DPSD_0Nq8G7LPRObthHmQr6AeSCdlvn4vx1EEKrM8-lDRMLPUPug7rub1e5dX5pc7JPnDRJOsOnF1h3fq8maigf6yTnsb7Hg5e4L3FcrfDM-OQKrqcQf6GKHpk-1-cii_t0eFlC-saaM7yyD4Xr8iEqNL889xHzhXHcs1JYgelUviVZeEdWsB0hGZcfl-vkxowuh13Y8IAcGr5sYsovfpu33nuuhFY0nQSkw2uyzGaHPT6K9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=V-GfGla_5EIojnHgbsZVg18Dn7lbQv6aozxX24bwMZhC-slIv8wewcWxnS1VrrrkrJOeJ2lXub61RMh7ezzNIBc1ZXsHBfuwcbSJied-hK2oVS5-baLfEqn0OQxcITrwTzsTiL-e_rsya2oGdLRYOqlhu06u8Yv5Z_q4M0QGxxTAvzaPSrJKfrZjsho0EEsw8CbbewhkbvuPJfGR2ToRAnYc5gWomlkwS7Yi4zRpIaqz0iyaJLQPx4Ma1QB5e-JU6rpZs45nfdxinN2EqJOvWq4y2Vg1sc29otF9ICWCOgFniEP5zwXBM5YuzUj_5fkxygDEUlfzPxDq-JOqBYCtSZVTZlMrFgpbRgAcpSQZHkUlDFq8lxhZ-sxa0UGKSUdsqaCWDT8ZWbD_dLkVYXkwVL9F3O2S0mOTvxhAOXww7apzsfJHRR67enkf0DPSD_0Nq8G7LPRObthHmQr6AeSCdlvn4vx1EEKrM8-lDRMLPUPug7rub1e5dX5pc7JPnDRJOsOnF1h3fq8maigf6yTnsb7Hg5e4L3FcrfDM-OQKrqcQf6GKHpk-1-cii_t0eFlC-saaM7yyD4Xr8iEqNL889xHzhXHcs1JYgelUviVZeEdWsB0hGZcfl-vkxowuh13Y8IAcGr5sYsovfpu33nuuhFY0nQSkw2uyzGaHPT6K9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=CHxIkao9WDjKrcqfwhUyu1Mb3nkTzMCQgIcueNoc20kR6hxRZdBTfE3SP2IQ-3k0cCd8VphtcTlYRYsC0gQBtmPm3KGsSCHhTp6AQ8tmfVcy2yyc8O4tkS53To2iNCmr3OAQwf511kGJp-0nUOjHfcpgfYOJEgBCtx9U8kz148ekp8SUvvFkp9GRkx7t3q7NQS88wzyy0UsYhuo0e5R8Z2qz-asdXyXDv-9Bkk4zxV-dhyvvuELAyfk7Lq670-Quv-JJddhp2VBbMIIlvSzWGie2k2qxKLN1rAlL8jV6gfo7QPWBav7aQn9ZRuxV3KN0gAhJP6dqaj2JJUTfy0pT3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=CHxIkao9WDjKrcqfwhUyu1Mb3nkTzMCQgIcueNoc20kR6hxRZdBTfE3SP2IQ-3k0cCd8VphtcTlYRYsC0gQBtmPm3KGsSCHhTp6AQ8tmfVcy2yyc8O4tkS53To2iNCmr3OAQwf511kGJp-0nUOjHfcpgfYOJEgBCtx9U8kz148ekp8SUvvFkp9GRkx7t3q7NQS88wzyy0UsYhuo0e5R8Z2qz-asdXyXDv-9Bkk4zxV-dhyvvuELAyfk7Lq670-Quv-JJddhp2VBbMIIlvSzWGie2k2qxKLN1rAlL8jV6gfo7QPWBav7aQn9ZRuxV3KN0gAhJP6dqaj2JJUTfy0pT3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9XI_1mc6oWxs8Prl5W4N2VvDsba8zzsBaFEyTJtgtuiAANswdvATSBvDRE7yE9DU_qPUBC7ROJKGQcyin_HfbHdA-Wbxvpz4BDiUIDVyDeb2iT7KmCuNhT4JT7HFiAN3lVqq2JG3946oE5ziDJ9C5RYenAZlczbKcQsPqdejLj4Spjw1UA1jO4gzlRpeW5jzjpjIhRUDKDPLrNmBfujY_6X9wRr8VBHObZO8422UZ29TjlMrAzYv8MS5HekaABqQvED6Tk40GPjs0BTsNwgAkfPC_Ia5zkqmH1ph5OHsE5firI76A1AL235sCd1AWvJESZI2FetH1VsRjuv9Q9iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQj8n9BNSfHj2cw5lYbPpxpRgEkjVnGnU3_e-k6YGU4KDxybIxMcm6MnY4hSncbXhtcIQIDo2dUbXRulq-xmbHQ9N4uBhyIQv7eQZYUr5szQUhhodOf5fvp_trM6n2iav-xfAtjRQ2lIpDecbhprH0NR1IQTT_DFxx0yhdYWKPXqxyfgJmk8YW_bYjAiAK47XkTbvo4hGX2S4YFDyN3u0k-jWO-fX_Gun-BAZXs9f6fKOWpaipmk0vsIXix_THLBgSGDaJdGwm8WRvO66TJbTrUQv3BFb0oQDS4zb_nEovkMNG-P8ek7IycMdA4OSP6sCqcsDwIoJXha4QeYLRocjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PR1cxUHBDvLDElucSjaeJ7CfcnqPhf2SF27eBOkYHvxUWQ1f8Xx6lwRfDu_TzQ9ZZZn4KO4inHsYpwjqa7cP7e8jqu_nI0cD1BF16Nz6M-zD_ZRIpE0CHFHX1rgQlbFdhLhh3yuVA-1MQJEF8pUHN7dn51qTEEO3p6GwfMrB9lCvQgC-DNCMevz4GcsnGDbv04B-FYDuqVE8t1uGPWG65xFCLJeeXvQWXxkfo82n_dBn5A_RMTtq2liLCBdeXIpkbHrxs_sqz9iOaYO8IiPMHB-wJPztGC9rBjwWKmfDLeTgxkbOEFRSJkVoBHgbkUlrLR2IyhP-YLHrSg2VAioxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmTADiQvwChS_pV7sEVOHUB7GZB68tMRTdEshnLGMRV1nSo4MJO3muNjhjgMTMG_2vrlzSkXUJnpfos7ElhckneiEi2zucGkRcZTADN4oF8PLqUVEBhoywhhsHRoLLmHC9ocO4S39abAjjR4KYVslw9JIdeqRukp2XX_MX5Jc9KGKX01_ADypiozEvtifkL-b0dCTRKM8OfsZKFOeSODYvwM3tM4Em_lzAs0HURFs_DKson5BXLZs_XT92OOClHK52KDVzAhQI8irWB50ffY4P3lQycZsSJrEpijnkzXZ8nJShTTNad7tYaKpNTocYFEhIYKv4ByzNAYzj7PsFerDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH_5S45MxowlJZKryRExdDv_YoI313N6BP4WuFfM0_dDBGIXRA_HeUilF1mZm2gQ8rQH96MuD5E6jXvzeXMjnpGwE_-M4Iltpjbsq1UsaFO_Cu4OR1Dg6vmzrn54i8qwQ7OfySz9oCihr7EtQDUDdv5qqv5tF2FQpYCbNajhLzk_hjqyqQDxHyrnnX2aLccb4sKepy6T0SkU1pk3DUfwPSkJU0_nsz-2WlvZHZXGzGBaiuhmpc7r2ooU-BOBMpWX4Y8IWcuOEaQeJw-iG9txi7iz62R3a_9NZljFKOkBx9dYIm6fuYivQNhoikQzw_rNVRt4jtbU5Asb3xPqEWxpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR8ITFqlJDq3hFOcHAREgGsdh1VSNZl1pkF3mlytJeJk3T_zAXcuiKYteVP6Tqh0G0r5dndob_LAPk51-5NH2v3KM2vREnDLX2daP9A02NRPqely7uPE97YMU5bdf_AeUkWEjafLF18aNuo1TJOB14A1TY6bIdghe5rGus-P8seRrDEOgIZ81Y3uHr968b2OPleXf3SJLHSmijrIQ0s5ISBrMB28oIIKwKc5wlJwyTaLlEqnvqCN5m0N5W3z1d1YMBEazthEJ7arsL1jojLA-pf6TD6w8xsQPCMRapQD9C3af0TxXNif7RRozoaj6SNSv8f_ADH35VvFMpFipTTd5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Aty9EUZVBZDoqiPYie6-q2BRAP5braKtWmFW9d12KyshTwoLab2cJoKwFY85A7sbuW8xFrPtbnSjjdrfqkXMjhBqxs7sIdRLI_x7JT6IQ2xNXLKelwemBes3zICGzpmQHvaKDtDBkIFfsF5sbVlYRifUKbXwP-CdoM9a2iUp0Y3W1nISL5cip6c6_qf0q9Mi2KfdMHL9dYISpDJNxUEu1Gbae2H2ZacT2YJqkwVDKi6GoFTkXdmn1tbilsumBvlK88EfQ_dino6yN3oTK_g1Rtktgh8iOJ85M-o2AeE6J-4YN_0MrKqMdT_L-YJaaAefJsJgVg9o9lu5TSz9xSZkFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Aty9EUZVBZDoqiPYie6-q2BRAP5braKtWmFW9d12KyshTwoLab2cJoKwFY85A7sbuW8xFrPtbnSjjdrfqkXMjhBqxs7sIdRLI_x7JT6IQ2xNXLKelwemBes3zICGzpmQHvaKDtDBkIFfsF5sbVlYRifUKbXwP-CdoM9a2iUp0Y3W1nISL5cip6c6_qf0q9Mi2KfdMHL9dYISpDJNxUEu1Gbae2H2ZacT2YJqkwVDKi6GoFTkXdmn1tbilsumBvlK88EfQ_dino6yN3oTK_g1Rtktgh8iOJ85M-o2AeE6J-4YN_0MrKqMdT_L-YJaaAefJsJgVg9o9lu5TSz9xSZkFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftSNMWwFxm7ISdWnejerwkzQHaNzkiugpntlfrfYLORD1Mlh2AfxIsBdrxQkRIippDo5QVwYvTZCzIMKG5bxsGZu38UIAcdS9tnEZEG7Y1ycfett8IQ8J9U5hOb56jrMH_N4XiR7lSs5fZyypUZHfXIV0YUQLcX-zBnGwbm5f3dxMJDx-WT2A8-bXMqCuE4xmD68lsZ85_jDP1ceZj2tt2TEF55Tv1bEdjQY_NLKmpIuVyiqQJIYYEK72luQObHQDfv-amai4JcLCSZTD8SOizOrQjzl1pc1FNQb3AFb6Yqh5mBO7k13TXbgF4NUMMt8rlJheDHb2Mjy9eupQVtuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ZiqoAi5xtwUcknVbYO0ueJu-7hsqlcFZCBsJUrzLeyDZEOBD05R5-Iz7_jwCLeYVgarGp0bGzHZh0l6nlrVvkATDMZVc3XR3VIykLT0kVwOShLVS7jG236D-d8BxA4ezjEi4XKJL404UI30bGvdOGllGnS1QK-qfre-PaT5_D42-f4qU5oRgLoPoqH6Onu0m_OnGJc0G_9jPeCcEd6MXnu2gsbM4e0uorevN86mHQcxAceLO6MApRC9MBxmQWhklQLYjEtrmxCrZr2bw6e0Jg-FfMxiiQUIq5kwouVdDc1rVEjSnqBtyHEPAPF9vTOHlHiCS1Z51szDtfq2OeoBCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ZiqoAi5xtwUcknVbYO0ueJu-7hsqlcFZCBsJUrzLeyDZEOBD05R5-Iz7_jwCLeYVgarGp0bGzHZh0l6nlrVvkATDMZVc3XR3VIykLT0kVwOShLVS7jG236D-d8BxA4ezjEi4XKJL404UI30bGvdOGllGnS1QK-qfre-PaT5_D42-f4qU5oRgLoPoqH6Onu0m_OnGJc0G_9jPeCcEd6MXnu2gsbM4e0uorevN86mHQcxAceLO6MApRC9MBxmQWhklQLYjEtrmxCrZr2bw6e0Jg-FfMxiiQUIq5kwouVdDc1rVEjSnqBtyHEPAPF9vTOHlHiCS1Z51szDtfq2OeoBCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpojmjzbI8GWzYD7EphT-pit_JpxeIVifnM-gBAEX0UPsvpa-yl1McrlgNKSd72MUGJ1l_x_ij3jSKUwlzzpncjvwywqdMJDsWRlAMLOCCae5AEPKgqyYE_XXcwuzTmIMG0rUcRlFcOfE8dyemSFxz8NOf_wuXl3p8WKtZ70Kemun3OlUUBm-wmZbQYKUb_OPRB-CHbohFiObeDFVcQw5lfFb94OgSRNSDeGmaSi50aKyC2k_4RafUs95WhdMOcaZ3datBCEGUCKbiydYTLRRQHpWriGFCC-zVmGXx1DJmlefMtf80MyN-yZLnKRTPozoM6Xz-uK8uxmRDUUOfiYxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGE7wjtWLdP-oxGgsAR_1B-weB--T8sAjl36QqRJMccTwseof_d8TrkIWpVInWeXvlnT9vP8pdWka7j4ZgrcjIeh8qlr9E1VI8o5-ZTM5rD9oHSQu3_TVBJm90THH0lIMvh2WoeGDXMEzHlcl_yR0dHDvcUnvAPZsJmVPMUHyUaawAmgS_j8rVe6IKtoqoky9jAUDf6B3pTdVQtt5V7mRvroU98T5n1As4w72fduN4iV5GbmDA3J-UU2W9PJRlof7rr5t14cayl4mwg0RQCEqOm6LRe3o6UuhpjCLrsT6O5DVlX_3D08eJq1kx8vuydCFWv3C8N4L3FntBV8NsuvyTRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGE7wjtWLdP-oxGgsAR_1B-weB--T8sAjl36QqRJMccTwseof_d8TrkIWpVInWeXvlnT9vP8pdWka7j4ZgrcjIeh8qlr9E1VI8o5-ZTM5rD9oHSQu3_TVBJm90THH0lIMvh2WoeGDXMEzHlcl_yR0dHDvcUnvAPZsJmVPMUHyUaawAmgS_j8rVe6IKtoqoky9jAUDf6B3pTdVQtt5V7mRvroU98T5n1As4w72fduN4iV5GbmDA3J-UU2W9PJRlof7rr5t14cayl4mwg0RQCEqOm6LRe3o6UuhpjCLrsT6O5DVlX_3D08eJq1kx8vuydCFWv3C8N4L3FntBV8NsuvyTRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=ISSJrXjJ5ZOPw4BozoE0CfzuSqffi0_Be6YTSOZ0289uXtD79Dw5Pu7n5MGqX-nCC2j4op60o1O4BuBUpvdxfqmaQF-4YHvceB4uz5UEk5HK3f08xE1CSFdg6l0HFoONeIR9ovVddhBAf9IdEkW76sGHzvsT2g-RgzTUHDpVF9lsXAq9BwaQsQ9E-wj1ORxKM3naFZfoZMbwSzmA-pb18pvZyN-7Yvd7SjFoSEyUG2_YxMXEUjFZTOKUrx_nSfJwxiipFptIaj3mMoZzBcyXHW9QAOS5122xGOEUJlOLrrmxxnUqSHj5dlXqpkWFit18X5aDa4DkudHoXw01zmJoRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=ISSJrXjJ5ZOPw4BozoE0CfzuSqffi0_Be6YTSOZ0289uXtD79Dw5Pu7n5MGqX-nCC2j4op60o1O4BuBUpvdxfqmaQF-4YHvceB4uz5UEk5HK3f08xE1CSFdg6l0HFoONeIR9ovVddhBAf9IdEkW76sGHzvsT2g-RgzTUHDpVF9lsXAq9BwaQsQ9E-wj1ORxKM3naFZfoZMbwSzmA-pb18pvZyN-7Yvd7SjFoSEyUG2_YxMXEUjFZTOKUrx_nSfJwxiipFptIaj3mMoZzBcyXHW9QAOS5122xGOEUJlOLrrmxxnUqSHj5dlXqpkWFit18X5aDa4DkudHoXw01zmJoRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BWAJf31d9vEQ-MXBbYHrttoyRKOsb0acn9UoX3u2ozIUjVSNnpnC_z1xb_XacVdDuSJd1MEzF2PTMihtH1RS0L_JuTQzek4sO1_rpSQWPqiocmHYnz4OeIacofi8V3hip-cGAq1B1-cNmzZAMK-7t4GVjNrsDsC7UZdvjAJFx_pY1s00hB0DoV2ahH_UgfSMUm4ADuzPaTkNi5zXHOoex5kCdticFzeTfFUZTSOp4w6KhdiFNCC8627zr9eZrBezd-3m0P52b0KAH13TwjVXP_3tcku6Bbya3Qi_9fqfb4uIsjcoR_6jKsQqK2wIb_V582k9eWIF5NPFCry03AcCi_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BWAJf31d9vEQ-MXBbYHrttoyRKOsb0acn9UoX3u2ozIUjVSNnpnC_z1xb_XacVdDuSJd1MEzF2PTMihtH1RS0L_JuTQzek4sO1_rpSQWPqiocmHYnz4OeIacofi8V3hip-cGAq1B1-cNmzZAMK-7t4GVjNrsDsC7UZdvjAJFx_pY1s00hB0DoV2ahH_UgfSMUm4ADuzPaTkNi5zXHOoex5kCdticFzeTfFUZTSOp4w6KhdiFNCC8627zr9eZrBezd-3m0P52b0KAH13TwjVXP_3tcku6Bbya3Qi_9fqfb4uIsjcoR_6jKsQqK2wIb_V582k9eWIF5NPFCry03AcCi_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvlNWzufSPaMakjGNANkZVzBR8RiuoxpwxBVl1QNrLJ_Tg1wS6KQJv-5RUpb3d0B7zWHdZQyv6oGc4YHJcZkBLW0_rOSWcfg5jIQLLkWqm1eyYZPsnRjw_US1xZe6kTnQzCM8LezkwP77gEuVdx6VqsKwSaDFgR6QAZq0tDTJl_u19cCMmj4aR_q8v4HCbBxINAhwujnjIpUYDC7I_EmDlyoNHWGB2VY0gkRsNcdJ-eLxnAdPzaSxEEGoER-58b7S-9sUU4e8HEFHqbYg_e3dDZBvXbQgCJv4w6ea6PEz5LXzEh9q5mmaWAXlfqkkyk4Dz1eRXbWt5N3YrR84NlI0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpsQ9NTLECNeajBCAsEe7FJADye6ArfFyQdmvDrIcu-wz6uaBbF0ko3zXlkbE_UcwxjMDsIhgVH5nyMTpt6KbWWW1r2r8qwUwFRqgSGY7u2yfhVssPvORBexPC8ze5sAiQkCF-FPuPAyLQ2XbLMI52TMiBuaY4E4NFw7-1a4adQoIn9DhDaLuCwkILTqF_9y68z7B8KdGE8ejCWzpM7cFqiExTiME8P9r05GrZyguJReW-8NXS6GHcNf2BLftUton59icR99Hjc2GZZc7zDduHOhM-E8Y1ry-u2AWw4T7xVP07XjVvQUEuMpogKGMKgflD7B9M4GheA4if92_RSKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQBNxNhv8S2V1d943wtKLvT7mS_UXuYbvqt2j8tXmKWH7gV1hPWB_l1Bv5zhHve2D2ohGu0jESQRutKhWYfoYPL005c_WOT6ipVrzsBmhD4c4pILcPNNvb0S-JvOXViW12WphcPKqUwNutbJADbU1EiY6CEkBNA0oK-OyZjMAsmCXXPR8VsXVfeD7a9puM3karOtcHGSGl-EchbHq3e4taIbYtQqv5XRDGQo64GekMUvqFc0W6Kj6-C226GoAyWiKMZ2DapibfUOrjGBXmQUuXg-vdvpbtndJ1Q1Io0nLxkQVctVxNilxPPqaVcX2f88uZTUM0HjADKQLu-uaiIX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7UWyQi_9cAuXJHPlG74OFAcZu00VOFusMb0_xUc9nedTJlxxECwxif-GhvGAWXn2tWk9sIsX6wNwMQ6bufExLNBpYFu0Y8zvZ0VYZvFoTyZ5d4QluR9FC2URcBPb3AhlfJe_j88TiM3qB4hLkbVBpBGvprtvMtsauI9aM3AZWuqZpPSMqOlhQPdaaJQL1IQF4OdGzF7WsF2G7k8M8J5mWXXLqB1NDs00pzNo6VNQmoO3URtff7peX8kHOrul2TgDUDFjhxDa5nGf2jeh_ZZP4RRj6pttuMT-qovnqERwPSP9yIBBjFFPDPpSDgnotRDyaeefSlq9xuwsuJTmmQ_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOxwJLGCPClni7g9jJ-3_B3Xo1rQqHQ5KqCGVCTyTOG7aRy-7-pCkH0Zv77gcg4F5_dGahaKiegclqjHO2S5GQywH3HcR_ZFzUjsqf67LMGq02JBlUBfeN1O23UdXx5tRsipjCzbLsY3n1sGFdvzXzewXgLcVv3vYUMr76RvYzyV2UTWwvZ6yT28Dkr1PX5Pr9Nq1EBbsTN9r9xY9SRckkoPFVIuFltWIRcUyucgF-QsssuaZhoUh7G2--x35jxdhj-5N29Vi-PfPR6HuptEqPlOfvrUlXaJOVvNpKNT3ewLCYqYUKEgkaAUOTP5A1inaYLvyusUDI19T1HBEXEqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwITI2VWaFC23xK4etTQ6JuoX5rQpXvlP_i4B_fuCPn-mae5vZXyvwrGivPUdL6smQD2ev1PHIcNHrLVxLLWwa9QK1sYoH_EuYBaX_3IzAecIi-q7v0U4R39O57-Tqm4LmKXporVQa5I3meWqXWbm5M154FFR3C6Gf77GE-0JYbfgPbEzGeU1F_25aMkQMZm7rKKlC3dU7xhoShvvGEE7RETvuaRTD-N-2brVBD7OZYnx0R9UuInA6_S_tIdymBE-5cKmQXOHHADxos8gvYKOkUCpzSOlT9UNrnVPE68oQx8Rp_1-CRrVIiEZjap1VZ5PmNyBfLh3q_N_otGv2Mojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUAI12hRE7jYQof1spe24ontX5vuB6e2ax_9Xuw1wyfMrk63xTmHu1JGwzx5flOPvCPWoTL4Ecuc5uRb4iH2diheaZd5zGjTpeV9vNTZe55nlZly8dflqEey_C0iWGi0u9dQ7cee21CvL_ekN-iQGmnSTisw2MA92KJXmxSUef07SvKDkH-HR5TGbTI1jTYbcgMewrVQKj_dwQXBdtZ71eZzfzAWX8hFzQUBHfmvNtPQ1pUKgejF2j02Pprjqf0HtHC5Lh6XC0WJDP_DV58kdndUlO77jFc36ysxjIATae8HNGYJ4dUlKPa-BJ8WVaL4id9C8hEVXIvvGVwzWAdhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puRCZMqG7ToGGJ1poOGAE_H0WnjNyj6GXNddC0Xrkw2ET1MxtY1-jLPnM3emqqGFKXQp9RSKP-wDKk1nr0Aidx9w0z3YiN7D1t0HUPudsMl4Wk3gG-BGGIzJ1ucG0_1lSyGiQVnPymfospVeC8C07PgKRjeqkwJR7B3lFbVDzWZkA4txobv-r-CRsGF5Uj1FX0nmNRGBZwkX3jwsoimmapW_gjwhpaZyJBzIfc5dMOx1s1dC8uBb6h0qbNacLL7dzLFKdVmVM5r04Lp5Fnw8qz7kAeaPo7Y8xuu9QUW5GsIQA7XT3446DspnvDsZmN-JEwbBhXOuaHHIg2ZsIPnEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLv9b-tB1IP8amY8fdzPFw_fg_zWXCHLiKaChGqZAfb85xRONC4608yHxMI0I0fdzuNTZDecia4IAiefT5JPCfHMWroo9lSG573IZZj9kXjLJUgplT2dfhYsXk8GNrohT0V-DNAKk5w5p45pYBZNUtinIQ-QEawlRJkzv77LY72SsA5to4T6-1hkFH6-k3F4pmU9AIPtr4cj0ePAYuxQVN5A9BhbxPZbvVMiq_dcw2AKff77kfa5PYr7FsJJC5nK4Y-bD_PjEN0-OQiYuZPOcOxTyJq5BLEc4Z7mYrPzavtPfwwxtLgQvNx_z2NuAb_MPqvnPC7NNYSqtpdw816eaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHBjaqB1Up0pUK4midFkBkQSJpCnRT3qOpTBctoObaF06S5iiMBGmm4ZolcIRqhhmUjHYJRJGE_kw_dyZwNCRruzx9HbMgJHFfFw2Aw56Y_xMJYLorWSorHRzg0xp2i5KfaQihVln0t2FfMXgVPaEHJeogVWYu0CdpbiBoI-FYJUM0RumX_tU_JwZim27KYerHNF9Ao6dk8v40ge49ahhiPt-cNxIYO2VA7X5TfNHrTZl3m7tiCDtx6UnHo6DrLqVgxcoVsP94plKRHXAjNBqm7yCyHQony7W4yMnSch1SlJC7zD_zn_RIv1iczlwCP94mvBIyPZ08rIHLF0qKKPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hppl9F0EkSx0zXvcUcSj0SaGCWWzHbCMQthFcqmnojfoJVc9_R8hH4OnX3M1vw0SpvRqB5ibpUi_vZFWx2aELMOlNDVp06N3phJ9YV4PoHkl3bVQHLlwKzuX1Q7Is0wq2Ne_b1UDADkD4CTP9c46xbICW4xrjcqQu0naj--rDw7CeHIK0RYJxfMZHPGPLFB7r36shU1BdbB140ONUAlQpXwy6j5W-qXMJJVo7OIFIzMls_HTRWcgFduLrNkTd1vNsfZej0rhcAKNvI8n2IC2Up_uprMCMC8nMd77JlVCrB6r9tuYRpG2OoA5DxqJkyvkXBzZAdRPr9A7QFzsyd8-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTViJrKlW7FpDgaRVg2rlBn4TGvv7IkhayKjICuA1HJW_R5w7EV6ke0eMAndkcUFZmxywRQ23Cndxpq7a0ZT8ak6Fo7U5dmuTJH1ZjLYbwuxuHgkxEc0NSQ5RGlefKOfdtgJeZHPbw7rELMaraUbb6FAxAOGexPPcihNsjAE_zXVZQyapLBDo2ANK_nAFg-ISWxVQMnuc68mfF2miwAMdkRL1aJVehzfW09pCK-Workei81-jWrmwXYKuVm9FTC1jvEyPkFRnB8SpLG8AEK8MawVBvH92sRDucsgHy5ssIJssYm62qTZ3cGHvvmYM968s3NO2Cp16ofHwJA7Q0N3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDQg66OnRfACuB4d27XrT7N5k4n2GgQNOv7ku__cHz3ktKPmoTcjyCl0RS7w1lQlgre68MNo2BxJWAHhXoeID6b2IAU0X6XrOKbobI3AAJSue_QbpNdJWSdvAKuCrLDDdYg7Sd6Gs4nkn3zt4zt785cOrTtpi1tAF1yJWyb7hgrgVjih6ASgLlTs3Zsw6AXrafA0KqI7j0UVGwpzYzpu6sO9s6WKrrU6aX7G5QqJcNJdfWDrz8vqJVm8RwTeutsoTtGmDDxCS7QM2bp5Ekfqfs7m7QC4LRSGLgLkAVACGST569as7f8ChWwrOALCBx1cIjurmHzTCq4RhWeK2NIjuf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDQg66OnRfACuB4d27XrT7N5k4n2GgQNOv7ku__cHz3ktKPmoTcjyCl0RS7w1lQlgre68MNo2BxJWAHhXoeID6b2IAU0X6XrOKbobI3AAJSue_QbpNdJWSdvAKuCrLDDdYg7Sd6Gs4nkn3zt4zt785cOrTtpi1tAF1yJWyb7hgrgVjih6ASgLlTs3Zsw6AXrafA0KqI7j0UVGwpzYzpu6sO9s6WKrrU6aX7G5QqJcNJdfWDrz8vqJVm8RwTeutsoTtGmDDxCS7QM2bp5Ekfqfs7m7QC4LRSGLgLkAVACGST569as7f8ChWwrOALCBx1cIjurmHzTCq4RhWeK2NIjuf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=taEHYYRNER9DqDOTN-cxmVspixGtR5sUmEkDF5obRHb-BYTr40UnQUDscDg482w0SIJuPuT8WLp1lJuSykLnU-Mj_BbFiRDtRIN2uUv4YDXABe9UAtfCUkT8QDpOqKLANt81wR2sSUKrRHNEOdIx6e0OYzhtFKdgB3ZZYdpB7hQzgrwYNn4nmCNJVQ_lSrAxTl3XXGoiBX23T5ksj--95675z38tgoqoXfZU_L_jGHhN0PRTT_YzNFfTbXxSBYVzWPQkHeHNGZz_IIgkLSnyK-nwURLwQVltGjMxnkMjZ4hfaSXExajMKDwzGs3z1gjkAh-h3w2n69jODMf5AL1iM4fqOOWN5LyHUAKg5KvCe15hHz9eN5jvlqEuiD7L7vCSzhQIsAXtb7sGNmNLOPcQD79nApkdEa4veYO13SnxU5p0jZ3ThzXihBVs0f-LQnL7eIwYQ6FlQqV2uCxE4Udth4uAXPijJluyVTnQqr2rE4kPVI6dZ30xoYeDknbkt42y521AUnjG_E1-V2pXLQlBThRZLgF-uqfudSQ9TTF0O00xyUrS-U2GNr8uiBGqFLw-t6PaqPDFUqrxw2OW0bZ8bhGIV3IlNKt8onlUCcMaLxKH5o0vmi4AOi96KRda7Exl1hGeVU4twnXTLR5pvGraEErgMx4glqko9paSSqpauK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=taEHYYRNER9DqDOTN-cxmVspixGtR5sUmEkDF5obRHb-BYTr40UnQUDscDg482w0SIJuPuT8WLp1lJuSykLnU-Mj_BbFiRDtRIN2uUv4YDXABe9UAtfCUkT8QDpOqKLANt81wR2sSUKrRHNEOdIx6e0OYzhtFKdgB3ZZYdpB7hQzgrwYNn4nmCNJVQ_lSrAxTl3XXGoiBX23T5ksj--95675z38tgoqoXfZU_L_jGHhN0PRTT_YzNFfTbXxSBYVzWPQkHeHNGZz_IIgkLSnyK-nwURLwQVltGjMxnkMjZ4hfaSXExajMKDwzGs3z1gjkAh-h3w2n69jODMf5AL1iM4fqOOWN5LyHUAKg5KvCe15hHz9eN5jvlqEuiD7L7vCSzhQIsAXtb7sGNmNLOPcQD79nApkdEa4veYO13SnxU5p0jZ3ThzXihBVs0f-LQnL7eIwYQ6FlQqV2uCxE4Udth4uAXPijJluyVTnQqr2rE4kPVI6dZ30xoYeDknbkt42y521AUnjG_E1-V2pXLQlBThRZLgF-uqfudSQ9TTF0O00xyUrS-U2GNr8uiBGqFLw-t6PaqPDFUqrxw2OW0bZ8bhGIV3IlNKt8onlUCcMaLxKH5o0vmi4AOi96KRda7Exl1hGeVU4twnXTLR5pvGraEErgMx4glqko9paSSqpauK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/su6xhIE6IulXeLoZj08wmbcw25uKkLnzAn49LtsVpDX3K8zxkPA2MZ51dJAhxJjtd0l43U5T2oyrumuNBavIa9CGcbSBcYIPcOwl6rAHGvfZQ1i3nzzLvklxhPmEAEWhN3wpRP6rEMGpJCOUb1RYH8q8PWEbBtrzKqclYVlm-ASd0wRaMOtk9VjDdHK_A-fJz8Re4hSuq-GkFP8dA1EBjFNv9xCnfxGDeK8j1bdBlJO46UIxqlyjLukBabOPzYpPm43v7w8OsVUVC1w_F5n3eMJm_-9-4wteMAW2Q0Fycal7-PyZhiTD3T6_JlufHWNPNfZ2DoPu8JeWIrtp0B3ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=Di1aMmmbDlb0akkTiVwGmv_aIR6Raiz9M7AEnXPVeQ2SUl44zfXPJzCoAXKKLbMtp1Ck9yasR6SOygH-6QFRYgge8kzVj5Vvdf3qT2yaRFRA1Lcy2R8bKXD4OpqtZ5fOK07xiPdWZXKSV1Ef8UC2aCulvVoJCo9FwZrDXm7a5jf4eOG7uXgP6JF49yF9i1EEhMmoOTXkH3DKE4Ocx0iLTpZeFQqTwCyuSj2v64WTyo0QmD6cSm4oEdGKnUQam-ixOHR4h_bJzkAkLW2H5X740jNmiSFmpc-ISyz-SukxRfXuN1Q255XyMVPCJI6FuvYqlFaXXLFu35o_L_G4g0fIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=Di1aMmmbDlb0akkTiVwGmv_aIR6Raiz9M7AEnXPVeQ2SUl44zfXPJzCoAXKKLbMtp1Ck9yasR6SOygH-6QFRYgge8kzVj5Vvdf3qT2yaRFRA1Lcy2R8bKXD4OpqtZ5fOK07xiPdWZXKSV1Ef8UC2aCulvVoJCo9FwZrDXm7a5jf4eOG7uXgP6JF49yF9i1EEhMmoOTXkH3DKE4Ocx0iLTpZeFQqTwCyuSj2v64WTyo0QmD6cSm4oEdGKnUQam-ixOHR4h_bJzkAkLW2H5X740jNmiSFmpc-ISyz-SukxRfXuN1Q255XyMVPCJI6FuvYqlFaXXLFu35o_L_G4g0fIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=eRAWexYXQpZMbn9MWPvfjdF9PazDVHvmtVgPQo2kJLAG4hRX1EKncDvBTA5Yrf6vNL2l12vwb56M1KqPdTwu2fPRmPlLe_lTAch4cx1tFR3ygofa_pbqF8vhh6b63__JIX5XlCFdYwobvBLLbtB5v3AfBclclvJq36mOsl-I39nkJK_azMTtYTRNVOGJNF-O9OWkWmYZ3nOpWL7oFfUybUX6EysO5nAbvbLU6LPFgSMStPg57mihIY_qFycFcIrsmQ8xy0zCCuj_CuHuknNjnzN7Y_5qY486kELXKBKoeGdDJlZzc2QPAVDpdnWe1pXBtawHMySc_Wia5QJmp-Cbrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=eRAWexYXQpZMbn9MWPvfjdF9PazDVHvmtVgPQo2kJLAG4hRX1EKncDvBTA5Yrf6vNL2l12vwb56M1KqPdTwu2fPRmPlLe_lTAch4cx1tFR3ygofa_pbqF8vhh6b63__JIX5XlCFdYwobvBLLbtB5v3AfBclclvJq36mOsl-I39nkJK_azMTtYTRNVOGJNF-O9OWkWmYZ3nOpWL7oFfUybUX6EysO5nAbvbLU6LPFgSMStPg57mihIY_qFycFcIrsmQ8xy0zCCuj_CuHuknNjnzN7Y_5qY486kELXKBKoeGdDJlZzc2QPAVDpdnWe1pXBtawHMySc_Wia5QJmp-Cbrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKpZsihL8EDo1iNCS9efxt1ER_hTH6wtlo1uqxyzZ5GL_Fy5OSUHDdgchEepDId3mqV5yBDW90gwIHi3t2dROE4m-8ks7JWgwYQoaNjbC16M752Nvva_5Z5RRqzmblAj_W1wZzJ94eJjCxQ7JF95npSY3faAf2jFSYcoL-XEHNQYtNNbXR0qVv39uqSZ1UITJ1XQE-XlS3k7BHGhV7AN2Y6VY2lvXEY_JRvG1ziUFfftVds3cW2ZKJ58o7Fga-kd7fd4wur__zQ4sA8eRsVHXElLvaIBSjse5FJfaXk-eRgoNe9_fJFgcGU7KMd5hIUYSiJYNRQj62teAUJjbzMd8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgOVfDxnIGIF6E4lTmhzI2xzqwBstm49H7AVqiBimoyzHQxD83VIsVt5xNd1L57ti9psTx_Tws0Re7HQg74KiztqamiiIzsWpGJ7P68uBXOzzFiEm9iZybld2w1GMweBkFrByfpUD-7ePJdoGlAp5RWF4R2Kw5e9M6irnLuO1hxn6ZAORYb4b3wqzS6NVTK9Yezu6m5z-a8l0i8o21rEOa6K0CQ0diyNSHeACPsP2VC6kbr-_ySZdBLGYdJpxALieB-yqoQL-Xvf1AFmAWB1v1LB9SmH-7WpwPCyQ0IdrZ90NIwLOZO3GNDwomQRco5StCrqzN6cpRAATpIjcuCIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=s6mdePvKQutlLtvZCTn_V4dM2-LJsSctU_okR3VFlhCqe3rKAnatA90NKi6O7KoROKHA7m8zfU216zaSo-IEfQZeRI1llHn-FCIjWvQd5saku5pbMFjtrbNbfPyrL3F-3wfoduVEq3LFmmg1ANP9FvZT-OTsBQBVe7lkm-y1wJZoLOMcsRXNWaCXlkQbudz6S7EAenU-lLBOYReEwlu9DYdCOwIYAYJdH5lJdqNOxhaEfB9onNbMSpWI2qbB-MkJfiUSDgsXRNJBNa1PBwA1EUJuF54wPlsfdgPPpv7KOX8aogF0gN0N41yr5f0A1wOymhGSJsQ4bddaiPd34PTKCJiEgL2wOdzlE3bWYfRPQ-MrR55RQmNik7rlWk0gSV9ru1aY3k0il59c8-VQYzqYZ7_zIvrxc5JSA3SggkeN2nlXpLlQfBdHMGwpwVYMsVVxs3YEWHo_jUBBJukglaUftCU8eEghV7pwEYbc0islp6uw5COx4YLmIlxURX-pSfRZz_VZCYO2TajCanq7C32mxNHHOjbexvou21HHGY8XgMJUL1TtaBMqtVSrttKlJSt3Khtp2wOQAb0sjdf_Y7nA2hjHxWwfcokQlnujwRBLIk3APbgf1TKSz51LfM4t0JVdl-lcMw0Mhq8DW1gyOIM1psQdmjGenQT1VfKuTwCPcqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=s6mdePvKQutlLtvZCTn_V4dM2-LJsSctU_okR3VFlhCqe3rKAnatA90NKi6O7KoROKHA7m8zfU216zaSo-IEfQZeRI1llHn-FCIjWvQd5saku5pbMFjtrbNbfPyrL3F-3wfoduVEq3LFmmg1ANP9FvZT-OTsBQBVe7lkm-y1wJZoLOMcsRXNWaCXlkQbudz6S7EAenU-lLBOYReEwlu9DYdCOwIYAYJdH5lJdqNOxhaEfB9onNbMSpWI2qbB-MkJfiUSDgsXRNJBNa1PBwA1EUJuF54wPlsfdgPPpv7KOX8aogF0gN0N41yr5f0A1wOymhGSJsQ4bddaiPd34PTKCJiEgL2wOdzlE3bWYfRPQ-MrR55RQmNik7rlWk0gSV9ru1aY3k0il59c8-VQYzqYZ7_zIvrxc5JSA3SggkeN2nlXpLlQfBdHMGwpwVYMsVVxs3YEWHo_jUBBJukglaUftCU8eEghV7pwEYbc0islp6uw5COx4YLmIlxURX-pSfRZz_VZCYO2TajCanq7C32mxNHHOjbexvou21HHGY8XgMJUL1TtaBMqtVSrttKlJSt3Khtp2wOQAb0sjdf_Y7nA2hjHxWwfcokQlnujwRBLIk3APbgf1TKSz51LfM4t0JVdl-lcMw0Mhq8DW1gyOIM1psQdmjGenQT1VfKuTwCPcqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=tarcikQ9XnVFhHgc2M2kEXb5NIVR2R3KIdyEUOHAJV7D5qJV3S_gdKnLC4ZEXFaLFQLSiX-vuww9W9F27cbtXMgNDjSkA9rqE9zFq3aSXCZQu4bnMzJXZNikHDRch4_zj3dObIEFyuP_Un8PcfvtcOP4EUqB28xAYqdO2S0PYmhPnPdhga018mUiDK2OrjKtf1s3dRJn996lFBTXLUci2TxVsrUStDlUMnSjK6pHhsK0UV1m7x4VEafCDVT_tzJCXiFumKhE9JpM1cVYgzQVqfx1XIYk0ofX2d89C194PcV3w5dm-ZdvlbsU8mavSzDIrHEp8HdCz05JxYBKRG-d4KC8UccieTlCctSsuyDKXvQollyUim3i4mTsaM-MjtD_c8rjjdW0gdbETaRuuCvYx9SRoY2qhpIl-_-r_bq-wPXhJn2Zzt1ky9i2dOautrihBjQPXssjrelfYBSPjQwV6J5hdp98464hhT5S1kQhYX7UBzg8KY37rRUAh3mNi6qxsic3I2GlXPexW7fRReJbX_X7dc1pkgjMV1COmB-cjWrt4ZbfoPjbGENQUs0EUVVzQfaK3H-JJfI5PIbDutIJn_ryJrjgMTSus5f0BDLlXtpm2oaSJ8HSFcyimQFgr9FBAYBquGKpfjF1G8ml0lVDChVfHduLfcZD8liNM9n2xPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=tarcikQ9XnVFhHgc2M2kEXb5NIVR2R3KIdyEUOHAJV7D5qJV3S_gdKnLC4ZEXFaLFQLSiX-vuww9W9F27cbtXMgNDjSkA9rqE9zFq3aSXCZQu4bnMzJXZNikHDRch4_zj3dObIEFyuP_Un8PcfvtcOP4EUqB28xAYqdO2S0PYmhPnPdhga018mUiDK2OrjKtf1s3dRJn996lFBTXLUci2TxVsrUStDlUMnSjK6pHhsK0UV1m7x4VEafCDVT_tzJCXiFumKhE9JpM1cVYgzQVqfx1XIYk0ofX2d89C194PcV3w5dm-ZdvlbsU8mavSzDIrHEp8HdCz05JxYBKRG-d4KC8UccieTlCctSsuyDKXvQollyUim3i4mTsaM-MjtD_c8rjjdW0gdbETaRuuCvYx9SRoY2qhpIl-_-r_bq-wPXhJn2Zzt1ky9i2dOautrihBjQPXssjrelfYBSPjQwV6J5hdp98464hhT5S1kQhYX7UBzg8KY37rRUAh3mNi6qxsic3I2GlXPexW7fRReJbX_X7dc1pkgjMV1COmB-cjWrt4ZbfoPjbGENQUs0EUVVzQfaK3H-JJfI5PIbDutIJn_ryJrjgMTSus5f0BDLlXtpm2oaSJ8HSFcyimQFgr9FBAYBquGKpfjF1G8ml0lVDChVfHduLfcZD8liNM9n2xPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=ixy2qLdwbHlzEPDju_tLPG5BkObpZiygjSc6o3fF-pXr7QkVeNY1Ql_5vtDsKTV3ySQZathmhkla20RYD_NXhH-ZJivV-vzbZwx2dN9mMBU3U0NA9JtSoIjvdu7ohqKSdgIbCdo1xkSgVRhtEG0GF4IVFAc70bwbU81RqG9lO8iDkBXirlpygZkynM6wi-2m_nmZ9yN5-oF_us8WYZRnT2phwbJtC5MZN8LfchMoskfauqZymXMzFa4GylCZm1i1unWKu-YtaXzlsXYkLecI61SHZnSkAWtrw691JprSiGh5KDMIG2EbKmtmJBMNYYcKZInf5E1Mom4jFT2krjZaEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=ixy2qLdwbHlzEPDju_tLPG5BkObpZiygjSc6o3fF-pXr7QkVeNY1Ql_5vtDsKTV3ySQZathmhkla20RYD_NXhH-ZJivV-vzbZwx2dN9mMBU3U0NA9JtSoIjvdu7ohqKSdgIbCdo1xkSgVRhtEG0GF4IVFAc70bwbU81RqG9lO8iDkBXirlpygZkynM6wi-2m_nmZ9yN5-oF_us8WYZRnT2phwbJtC5MZN8LfchMoskfauqZymXMzFa4GylCZm1i1unWKu-YtaXzlsXYkLecI61SHZnSkAWtrw691JprSiGh5KDMIG2EbKmtmJBMNYYcKZInf5E1Mom4jFT2krjZaEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-tggB0KnTXcBt0UgXN96WtXYLJrLu2w8v5ZLEKx801ejYM9RxDVfmzaeD94I07FHNoWU8pbxqKTeS0XvDTqswhwZXuocRX3N5-sapzVR_XgVQymisqUsiFQdg18zUQckoTech00BosHbheCHoyL-IZIrjBUW54QXBH2YIf2be23j6hxEOTHfBjC-hINgTLO2uyHbG1HPVKcpuA7asPyonyBVsCrp28EIOlJnQJleeScBA4uKvl0AwavbjeYRTag0HEZh5P9toUv0s17syb5qqwQcTlzOPVFV0Jiq8cctBgMZ9Ss5lBC-ecJuudLF5CAJX46Z8LFr09JCIgoxwY7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=pxcw6a0WSVQprYp2FVYvMS0HpixGebHJjXglcWsl5CNXM4XEG5EX-K3nTZzh_b_N4GDhRJgM1dpQr0TYIq8SXtHwBko1TjiEhZ9FIs9-ydCYS7EzYdQ-3_Dg11JVNPt1-TlZcjlscU2U3FL2O4j7flzkXjiMc5MVsKM3TiqYggKX8lxTJOYmV_u7sTEXZ3cpKuHTBnYSIOWaBP-TLmIa8Onf8EhBo9WFZzJ_xhOPfh6TdrFkkY4opcxUmFtHXuGN2UFZpfeRltZomO2wnW55aKTXoS_oL5PCv_R0o8YQz73bcgc3OVY7qZkw9m7SFySiTYpwnT9IYKLhQ7YAyGoHkqi6HzCHCSJJk0FOZj8Sw5wg92LRu1Yb_PGiEmHVQoyI3oI-3xPfoHC7k0EbG1lruIx9MIvJvnl7013JXaBRFKwuAjs_BJy25_NeM9HQj-Ny2GXAtph_bVIJOnHtafrtgGIhNCiX7D-m6aUMm5DgpcmeATcvZbAE_xVjFwYmRbYWvWvrcb4HAtN_LVM8J-AFDpHpV0hUdXrd_2cKn8LWF0PgaAXRUeEpbsRdGrWqNxaxAybVEZ1XSleqtK7zl9i6VaL2DVGLZnuxR7r3Qx1u1THn_yxCOSukDZO4su21Ph1eiD2JPW6pzpwXVRP2JdpC0sNJ0-NkwBNh4pf6Uy5Dr4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=pxcw6a0WSVQprYp2FVYvMS0HpixGebHJjXglcWsl5CNXM4XEG5EX-K3nTZzh_b_N4GDhRJgM1dpQr0TYIq8SXtHwBko1TjiEhZ9FIs9-ydCYS7EzYdQ-3_Dg11JVNPt1-TlZcjlscU2U3FL2O4j7flzkXjiMc5MVsKM3TiqYggKX8lxTJOYmV_u7sTEXZ3cpKuHTBnYSIOWaBP-TLmIa8Onf8EhBo9WFZzJ_xhOPfh6TdrFkkY4opcxUmFtHXuGN2UFZpfeRltZomO2wnW55aKTXoS_oL5PCv_R0o8YQz73bcgc3OVY7qZkw9m7SFySiTYpwnT9IYKLhQ7YAyGoHkqi6HzCHCSJJk0FOZj8Sw5wg92LRu1Yb_PGiEmHVQoyI3oI-3xPfoHC7k0EbG1lruIx9MIvJvnl7013JXaBRFKwuAjs_BJy25_NeM9HQj-Ny2GXAtph_bVIJOnHtafrtgGIhNCiX7D-m6aUMm5DgpcmeATcvZbAE_xVjFwYmRbYWvWvrcb4HAtN_LVM8J-AFDpHpV0hUdXrd_2cKn8LWF0PgaAXRUeEpbsRdGrWqNxaxAybVEZ1XSleqtK7zl9i6VaL2DVGLZnuxR7r3Qx1u1THn_yxCOSukDZO4su21Ph1eiD2JPW6pzpwXVRP2JdpC0sNJ0-NkwBNh4pf6Uy5Dr4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
