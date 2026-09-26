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
<img src="https://cdn4.telesco.pe/file/E51r2ihFDPB3LIor6PUirMpysPrcwBIoO_7sgc-jKRrXN7QHDOJP1usWsi_NZEAfSbMK5pSpjsDnZfJRvdtBZOrTWE3Vh6Koyn69Uu7VgrFLwoohDiFCAkANjEC5HHqGCe97a9tLs43eXKeGX4X_a87SPJFSlTTCBnsh6XGyNHfqXOSS9iRAb4AoLI-115utW2kXa75XFeEfHRlFldbUzn20S2IHflGBbpbzHcXL3XLT4KOHqH8zdP_dfLV7v51SdEvkBYKY91IK4CCQmZqBi71WjqAL71rHj175Y_qZQg2ojZabDSEpDNrYGqsH3irjPPKPfOQ8SZS5urNkxWFdMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 23:30:39</div>
<hr>

<div class="tg-post" id="msg-464626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a148085b.mp4?token=Ual5ZV1mlXB3Ranln7_1NZ-OVQwBB02KXGjy0LVLJRlmowjHEX37S8eCEjlLpBQRL8oJbYRuZOlfkEbXZKB_6GzcQXs5ARu0L2u_LoRr-45q83mP97Wdw-AjOryFgkkyxOn_MJQQdDtNNFjtklFqCLY1G627QHEYjP1pXdESsaQGmGKqsgfJBSh1IGB0PCtvOndEHo-tTkaB2abUqwUN2qASe-XPzWyRXq1JHYv2x1jEL-18mvGWS2WXsFkA4dyueMbn5csXt7xqPYpSv8Xk5LzK2ci_56zD1ipXhaX25EQHgQuqgm4APmCofQxxrHlYF1f4IkyCs8QAMikX4aLFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a148085b.mp4?token=Ual5ZV1mlXB3Ranln7_1NZ-OVQwBB02KXGjy0LVLJRlmowjHEX37S8eCEjlLpBQRL8oJbYRuZOlfkEbXZKB_6GzcQXs5ARu0L2u_LoRr-45q83mP97Wdw-AjOryFgkkyxOn_MJQQdDtNNFjtklFqCLY1G627QHEYjP1pXdESsaQGmGKqsgfJBSh1IGB0PCtvOndEHo-tTkaB2abUqwUN2qASe-XPzWyRXq1JHYv2x1jEL-18mvGWS2WXsFkA4dyueMbn5csXt7xqPYpSv8Xk5LzK2ci_56zD1ipXhaX25EQHgQuqgm4APmCofQxxrHlYF1f4IkyCs8QAMikX4aLFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
سخنگوی ارشد نیروهای مسلح: آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی محکمی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.  @Farsna</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/farsna/464626" target="_blank">📅 23:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594ed02de3.mp4?token=uBPh4uxojxXH59r4NrU-GUoFHSqHgusITn1F1yEU7B7jcD2SE2IXGSX512TiIXma94XSo0KghAx-gzJzPn718hWicejFQb1j5ljoyhNzf8vI5efPfH16EuCjwhNmsqQO16ANw5vWiG_O_kz4qn-M7lOj2DF-eZM_kgKljd4JkXrGQA_n8fpHb6_s-lxVShn3wVNPQkGkkHa-dsvsdsF4THSPkaxfrb9iAfJVEuOOcbUjfTYBDklkBcto5YCb7AFR4yXA4Mecqmpfen5nLaPFN24KKoYZs9NSIjDUCBDrrZC1tv4bFrdiU_xCvfXJqNnRy4WA5OgoZS8r871SGZPj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594ed02de3.mp4?token=uBPh4uxojxXH59r4NrU-GUoFHSqHgusITn1F1yEU7B7jcD2SE2IXGSX512TiIXma94XSo0KghAx-gzJzPn718hWicejFQb1j5ljoyhNzf8vI5efPfH16EuCjwhNmsqQO16ANw5vWiG_O_kz4qn-M7lOj2DF-eZM_kgKljd4JkXrGQA_n8fpHb6_s-lxVShn3wVNPQkGkkHa-dsvsdsF4THSPkaxfrb9iAfJVEuOOcbUjfTYBDklkBcto5YCb7AFR4yXA4Mecqmpfen5nLaPFN24KKoYZs9NSIjDUCBDrrZC1tv4bFrdiU_xCvfXJqNnRy4WA5OgoZS8r871SGZPj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: از ترامپ و نتانیاهو و دیگر قاتلان امام شهیدمان نخواهیم گذشت؛ این موضوع دیر و زود دارد اما سوخت‌‌وسوز ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/farsna/464625" target="_blank">📅 23:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313b69d364.mp4?token=bnposFo26ybXEdtHCFhn8xb6dvL4dSbw5OCAgdlLYO7Uasg6WbudnUWgrNd-V3Dsq1iO_lugecLHWLrhlKj6_w1VQeY-aZY7nSuBehpPcElp9PCkr6B0qluxzk76C7nTLH6gk-42qj036i5TsrEOL6oGNIQNnjKbXdmtfaXSbFs6n-SGFS8Zv2n7WgectvG-Rd8Da9wsEOofB24xB7G_pcj4xsAUALchxjRgKdGSFz62NW69oL-Y8TT0YqNf6n8MAZqrzMLQcZ6LAb66g-zYzx2icWlpJhxK4wPtTJGGiwBu7z0UECDI_ROJrfsrlD3mFb4bIlPXLbH1nDoq88RfGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313b69d364.mp4?token=bnposFo26ybXEdtHCFhn8xb6dvL4dSbw5OCAgdlLYO7Uasg6WbudnUWgrNd-V3Dsq1iO_lugecLHWLrhlKj6_w1VQeY-aZY7nSuBehpPcElp9PCkr6B0qluxzk76C7nTLH6gk-42qj036i5TsrEOL6oGNIQNnjKbXdmtfaXSbFs6n-SGFS8Zv2n7WgectvG-Rd8Da9wsEOofB24xB7G_pcj4xsAUALchxjRgKdGSFz62NW69oL-Y8TT0YqNf6n8MAZqrzMLQcZ6LAb66g-zYzx2icWlpJhxK4wPtTJGGiwBu7z0UECDI_ROJrfsrlD3mFb4bIlPXLbH1nDoq88RfGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: هر کشتی‌ که خارج از مسیر تعیین‌شده توسط ایران از تنگهٔ هرمز عبور کند، امنیت نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/farsna/464624" target="_blank">📅 23:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2c3d0ca7.mp4?token=Eam5osGOzofmcmh4tkAlt5UR_tyhPBOVtshcyihvDVbFIIeBSqTnGKxOOYNR8lHsBI_KI62uHmdYLa5A_uQJuMhrXLaTm2wdzil4uEOdSs6d37FS438yqkcY2jTWQBDZfcYg4eSSm0akKFaGGP6kMWqesk_Xe1_y3kwbmUZVNQVGGNPBk8t0Uj0g-kiIgV03XiNyoIxl8av1pXjkb2kfr4yyi1D4eeEnZCzRzRHXwiHL_N6OZg_lVutBM2mYgU7TDLEJyWMvgI4u6_o8agt_uAsOIWSp6hwQMgpXW6VJ99wsvG7AtAXnZu1i9AITTTBc-LAQbUgxzdKFF6aK8v-7EYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2c3d0ca7.mp4?token=Eam5osGOzofmcmh4tkAlt5UR_tyhPBOVtshcyihvDVbFIIeBSqTnGKxOOYNR8lHsBI_KI62uHmdYLa5A_uQJuMhrXLaTm2wdzil4uEOdSs6d37FS438yqkcY2jTWQBDZfcYg4eSSm0akKFaGGP6kMWqesk_Xe1_y3kwbmUZVNQVGGNPBk8t0Uj0g-kiIgV03XiNyoIxl8av1pXjkb2kfr4yyi1D4eeEnZCzRzRHXwiHL_N6OZg_lVutBM2mYgU7TDLEJyWMvgI4u6_o8agt_uAsOIWSp6hwQMgpXW6VJ99wsvG7AtAXnZu1i9AITTTBc-LAQbUgxzdKFF6aK8v-7EYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: اراده کرده‌ایم که کوچک‌ترین عقب‌نشینی در برابر دشمن نداشته باشیم و او را سرکوب کنیم. @Farsna</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/464623" target="_blank">📅 23:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoS7YArFJ96qVwrmpeb6vvmu5tvP_1-pTboccVVviZq5dmlxjHHa-dVAd68-8dviyfihJdxx1ArulPXTExQ0bn9Wz-JM4T80GQeqb51EXaGqPEbQR1AP946uPavzYAKR8ZpWAG9gQRTKVAbmd5xtB2toeDB_2cFLw6QRzJ27HG-N4e_pwSmO6KoeU82DcmMS9iUwmmV1OXf_uijGFnUnKulJkWkQbx0HmRHjmNdokWcCwpgrVZGSz8NPrM14-wVyJba2gJu3BpZEvQOftUhcIghU9C3I7Mj7VN3IDmXCRR2B7WsiT9TPomYckcF1TVwSt6VWXfhwcUDga3Ftfc9yAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما برایمان از شباهت‌های جنگ تحمیلی اول و سوم بنویسید
🔹
در جنگ تحمیلی ۸ ساله، مسجدها یکی از کانون‌های حضور و همراهی مردم بودند و در جنگ اخیر، میدان‌ها و فضاهای شهری به محل حضور مردم تبدیل شدند. شما چه شباهت‌هایی میان این دو تجربه می‌بینید؟
🔹
دهه ۶۰، در میانه جنگ تحمیلی، مسجد فقط محل عبادت نبود؛ بلکه در بسیاری از محله‌ها به مرکز رفت‌وآمد و همدلی مردم تبدیل شده بود. کمک‌های مردمی در مسجدها جمع می‌شد، جوان‌ها از همان‌جا راهی جبهه می‌شدند و مردم هر طور که می‌توانستند درگیر جنگ و پشتیبانی از آن بودند.
🔹
سال‌ها گذشت و نسل‌ها تغییر کرد. در جنگ اخیر نیز میدان‌ها و فضاهای شهری محل تجمع و حضور مردم شد و شکل دیگری از همدلی و همراهی مردم به نمایش درآمد.
🖼
به نظر شما مردم در این دو دوره چه تجربه‌های مشترکی داشتند و چه چیزهایی تغییر کرده است؟
🔸
خاطره، روایت یا تجربه خودتان را با هشتگ
#دفاع_مقدس_سوم
در سامانه فارس تعاملی منتشر یا از طریق
@Interactive_Fars
و
@fars_ma
ارسال کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/farsna/464622" target="_blank">📅 23:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🎥
سخنگوی ارشد نیروهای مسلح: هم موشک‌ها و هم پهپادهایمان نسبت به جنگ پیشرفته‌تر شده و هم به فناوری‌های نظامی جدید دست پیداکردیم که در صورت خطای دشمن ضربه‌ای کوبنده به آن بزنیم. @Farsna</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/farsna/464621" target="_blank">📅 23:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910aa6b505.mp4?token=gPCKuC1wHoETQZGNCRMOzAWzy15P5w7IbgqRekyCrtvSai1HOl5xG8ci9czUhxQCrjSmiCU2874-WRB0quCKmL6vAXz3Zlc9CMvUgnhLAICcjWouUsA-We9Y-4aBZfPpTnblU8QySsjr6CIo5VpAbuje8XKiH3iDh5JbMvq6Y6qKEqv0CegL4DB_DwXcc9UuE6pESUOq1vsy94v1QuN9OneIp5dNteyGgmE0FCj95o-NbvpNx79VYi__ncsG-9g-PDGK9w9IvJxUspCbNn2-fwk3eCLvw6UmzcMi_T5JLGOeU7jkuuUKEiuxhdgR5KBG0OrzryyrYoKxb4IPHmRqCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910aa6b505.mp4?token=gPCKuC1wHoETQZGNCRMOzAWzy15P5w7IbgqRekyCrtvSai1HOl5xG8ci9czUhxQCrjSmiCU2874-WRB0quCKmL6vAXz3Zlc9CMvUgnhLAICcjWouUsA-We9Y-4aBZfPpTnblU8QySsjr6CIo5VpAbuje8XKiH3iDh5JbMvq6Y6qKEqv0CegL4DB_DwXcc9UuE6pESUOq1vsy94v1QuN9OneIp5dNteyGgmE0FCj95o-NbvpNx79VYi__ncsG-9g-PDGK9w9IvJxUspCbNn2-fwk3eCLvw6UmzcMi_T5JLGOeU7jkuuUKEiuxhdgR5KBG0OrzryyrYoKxb4IPHmRqCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
سخنگوی ارشد نیروهای مسلح: کشورهای همسایه توقع نداشته باشند که از خاک آن‌ها به ایران حمله شود و ما تماشاگر باشیم
🔹
اگر کشورهای منطقه به دشمن ما کمک نمی‌کردند امروز خودشان روزگار بهتری داشتند.  @Farsna</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farsna/464620" target="_blank">📅 23:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebce47bd5.mp4?token=NtATjtUeY8R0rNhaoPPCxC84zbejK2NHuXuJKTjGoSiHACSFgXHP8ZrFQUEpDZYOUA9ETutbCHZBpMzjG4GSmr5fCiy_OvK3qheD_NTYiXMnbAptq1yzLp6Np6zm0oPDxsmZVLUoQl-UfOMovupubWkWhxt3jB3iYbVyegrGXuusRQGEvgngaAqAXlAhLHwHViIBl2myPrKCm6EJybwnDZA5QQXEPm6QNm9Md9FYFKjtPEpFEOM75Fuhr-wl2I4PkEDVx6dR-hNSpmk-QuwdpXeH1YZbanKa2g0jt0c9JAESpeIuX-Wd_QDYhSPaMlHIjqGHw0YrxBMxmltqXe5s6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebce47bd5.mp4?token=NtATjtUeY8R0rNhaoPPCxC84zbejK2NHuXuJKTjGoSiHACSFgXHP8ZrFQUEpDZYOUA9ETutbCHZBpMzjG4GSmr5fCiy_OvK3qheD_NTYiXMnbAptq1yzLp6Np6zm0oPDxsmZVLUoQl-UfOMovupubWkWhxt3jB3iYbVyegrGXuusRQGEvgngaAqAXlAhLHwHViIBl2myPrKCm6EJybwnDZA5QQXEPm6QNm9Md9FYFKjtPEpFEOM75Fuhr-wl2I4PkEDVx6dR-hNSpmk-QuwdpXeH1YZbanKa2g0jt0c9JAESpeIuX-Wd_QDYhSPaMlHIjqGHw0YrxBMxmltqXe5s6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: آمریکایی‌ها همۀ توانی که برای جنگ جهانی سوم کنار گذاشته بودند را مقابل ایران به‌کار گرفتند و دستاوردی نداشتند  @Farsna</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/farsna/464619" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc560477a.mp4?token=QcNxOv5z1QvDEe_FlNTsqLiXoqROVAz5gyOI6nnvDhdrcvG6t2vlquBmnYcTCTNPEOVMynBCET2DqNxipZZCuPkBbIZSxgf1PAJMJ-Cz_2SrHgnt-8Xr5kXc-E7LlycPoKo5XCkC3cbclPm4r7spQxG1jTN6D8mI5pClNY3u4Q79UipiQE2ZZ6gPDEYiFnukuWr-CPFDZuLsuv8G71-YFcROfrGySAC6T16u5iVvShsxcVs4F8JoKs5Dnn2oTsvIjK1ytSoMHBxjAfIxUf1MQhFdYwUkDG_cfUXSdXkqOmWLo9Nu493jc7mqBIMzRwtTAOJXYmMudxZf6EuTcepr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc560477a.mp4?token=QcNxOv5z1QvDEe_FlNTsqLiXoqROVAz5gyOI6nnvDhdrcvG6t2vlquBmnYcTCTNPEOVMynBCET2DqNxipZZCuPkBbIZSxgf1PAJMJ-Cz_2SrHgnt-8Xr5kXc-E7LlycPoKo5XCkC3cbclPm4r7spQxG1jTN6D8mI5pClNY3u4Q79UipiQE2ZZ6gPDEYiFnukuWr-CPFDZuLsuv8G71-YFcROfrGySAC6T16u5iVvShsxcVs4F8JoKs5Dnn2oTsvIjK1ytSoMHBxjAfIxUf1MQhFdYwUkDG_cfUXSdXkqOmWLo9Nu493jc7mqBIMzRwtTAOJXYmMudxZf6EuTcepr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: حضور مردم ایران یکی از ارکان اصلی ما در مقابل دشمن است  @Farsna</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/farsna/464618" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464617">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b656c15c7.mp4?token=AQrBcw_qTuxpFyMMATIb5PGH6dU-0SDikav0ec-jcemRXrpThvqb5PoV9qxLqOdkEvCk2wRKqpBuCq3rWaoQ7qPzMbEdLCQJVFeN8kVmoWWtIYLdFzP3upq8g58hrcsPis-hM_mJc6OelzsnVQT6Sh7YYp-F43Ll7aTAi0yZclNtqXlnOdIQDwUYSk37PkoZD2kC-b9Ya6JSMtXvKe6Dnn5mOcM6Bq-9U_j8sLv2j_7JQik3JF5-4uhZToFKyx_g-Yokpi-oMkgo2YQjA9B064Fk-xcgbcZQopSOUGk4r7coLee1baEXvZwmsSHqYVr816Y9b1AuNKjbVpO5BsNbMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b656c15c7.mp4?token=AQrBcw_qTuxpFyMMATIb5PGH6dU-0SDikav0ec-jcemRXrpThvqb5PoV9qxLqOdkEvCk2wRKqpBuCq3rWaoQ7qPzMbEdLCQJVFeN8kVmoWWtIYLdFzP3upq8g58hrcsPis-hM_mJc6OelzsnVQT6Sh7YYp-F43Ll7aTAi0yZclNtqXlnOdIQDwUYSk37PkoZD2kC-b9Ya6JSMtXvKe6Dnn5mOcM6Bq-9U_j8sLv2j_7JQik3JF5-4uhZToFKyx_g-Yokpi-oMkgo2YQjA9B064Fk-xcgbcZQopSOUGk4r7coLee1baEXvZwmsSHqYVr816Y9b1AuNKjbVpO5BsNbMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: ایران مجرب‌ترین کشور جهان در جنگ نامتقارن است  @Farsna</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/464617" target="_blank">📅 23:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464614">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vrMGRDguxQ9cLZaYnxPdFB9rwqwp3uGkPhW1wpxoGdqCVgG6lOX-dwl3-Nahtb2r6gAN80pzRhFMcIzgonul2AvjiA-ucPrDi4yt78_QYutdgtrQ7X4WYNnsOkapancEbo1dKqbcAU68pBh27I-KZTPAPt6aGN7AAKv8feJxXar_MS0sGmBl4IzTfs906OcnofGnexnvlD0dF7z0dFUmb5uN3kD0X6uPDxabz0DIQwzQY3pd3JU-XSSoXue0hkRfFBCMksu2uSIzPsDJXodzSfivMaqqw8LvOEhoqU4e2vr7y_jqpaHERQePULsOVAxAiEMlZfvKXuNc-WwHr33lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0dX-IWnKC5uMq19LtsoFpE1cnNgi8X_91xAqw_W-kjlJkeSg_Ky5gPm89PAhTeXVBa7iGXqlSk6t6pVyGjAUVbG6P5cEs53_ah2V3whK4gnKac8Rj90u7bEkJxXoAq6amsh7IBJ8AeFokQajOSKIVEPMtJ6rPN05QFcPtkK25EG5mWFhGdXWlZZ1tW36JKTdeRvQ8sEbOfA6A5D6sWP3JyWZsauMIkrdL_xEINcKWa5SEMDEoX5pUcY981pDr4G3ixZ5q_aRw0zKgiVADVW7G9ih7iISQM0c6xSfjsEfJAMIcjUduXkE4OkNN4vWe39BRjUkKu5LeNUqRnEC1ngCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yykd1_iigYhnJouldtrL7ttODZOYb91zetk_xCqPppYTrI_JVl9urMfIvqXyXDAxJtSudztbkZB65DZzELUtN9O93L-HVMOx4xXKwr0sPmixKhkQZetzZGuXvlaiwhIBlnk1qqQIW1gBp17xEowTlkk9ltbWyrUDqk0zD7q8DneojexJMhv56WZ2-LSbEZwIKDZUveaDy0RABfJJf2h-ifftdXaj_uS8YwMfAp4-jBscvbRG4Z3SSCeLrD0vPN-P3y4z7ck7h98DCudvG8mQ-yeZwIBas158mOboG_Vz5ybchFOiACQ4vm9IkW8aQTefdTGMksxQk55_1ZQxaSRiyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حملات شبانۀ اسرائیل به جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/464614" target="_blank">📅 23:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464613">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab20f1aec.mp4?token=sE4_EeGjHlskXHno5QANHhhxZTc4jkHrLNb952vIzG_q8MliQcWk9EcrxOd5p3IV-BaLhPqXkP5jTcAW1qyV_qDQnGtpGNd7JLfvDxuXEnHAN4rSDIXGy46UYg1Nu1s6hHHJAHP8EJxVbTNmFLIV8oQDTZIkiMWTE0pxVNY3J4UvA1VHmaxo-mb_6t14kUqFFs9aRpvIpTTzSuvRuD5VO5qzy3jASBqQee97m4yUZY3hSMJ63-hkdxzCPNyflkricdrfyb19hP-re4FHPoUpUTznwuHxCC9zpurJunDsZrm8rrus-jbTnMFgk8PmL2KGH5BWOhg4gqn_rWz-KXuvCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab20f1aec.mp4?token=sE4_EeGjHlskXHno5QANHhhxZTc4jkHrLNb952vIzG_q8MliQcWk9EcrxOd5p3IV-BaLhPqXkP5jTcAW1qyV_qDQnGtpGNd7JLfvDxuXEnHAN4rSDIXGy46UYg1Nu1s6hHHJAHP8EJxVbTNmFLIV8oQDTZIkiMWTE0pxVNY3J4UvA1VHmaxo-mb_6t14kUqFFs9aRpvIpTTzSuvRuD5VO5qzy3jASBqQee97m4yUZY3hSMJ63-hkdxzCPNyflkricdrfyb19hP-re4FHPoUpUTznwuHxCC9zpurJunDsZrm8rrus-jbTnMFgk8PmL2KGH5BWOhg4gqn_rWz-KXuvCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: ایران مجرب‌ترین کشور جهان در جنگ نامتقارن است
@Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/464613" target="_blank">📅 22:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464612">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee88ddd6e.mp4?token=tdICPvGhtrrkea23zZVCrdKHbehZTfMmMDO7OCpyrrVs5eYE3GOOLUoy4xvylu2mwneL_L28TaNvRvANvhzgZSDmXFkCoHoMr-sWyfGTDpab66BV7QAZJ0QQuUu-Q9DY1Z9OXLWUvl46bjqmFgN_JLhx3atNjNtQfXcDeMFv8o78nkJh85nXvWTAiOMWwyKbv2H9_fuv7-gFh8NAJ0SJrYX_WedcX_SYW2oIoGbYiJNj_ohulc2A0T6__4a_S-cnCHYxy9CfsvwF917Qq9Zlc7-6IovA7MgVQP9QKuamEHOT-yE7fXgx7KYz7tg4raa8XI8LzuiaIGZ62A_CUtgTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee88ddd6e.mp4?token=tdICPvGhtrrkea23zZVCrdKHbehZTfMmMDO7OCpyrrVs5eYE3GOOLUoy4xvylu2mwneL_L28TaNvRvANvhzgZSDmXFkCoHoMr-sWyfGTDpab66BV7QAZJ0QQuUu-Q9DY1Z9OXLWUvl46bjqmFgN_JLhx3atNjNtQfXcDeMFv8o78nkJh85nXvWTAiOMWwyKbv2H9_fuv7-gFh8NAJ0SJrYX_WedcX_SYW2oIoGbYiJNj_ohulc2A0T6__4a_S-cnCHYxy9CfsvwF917Qq9Zlc7-6IovA7MgVQP9QKuamEHOT-yE7fXgx7KYz7tg4raa8XI8LzuiaIGZ62A_CUtgTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در بازگشت از نیویورک: صحبت‌های ترامپ نحوۀ سخرانی من در سازمان ملل را تغییر داد  @Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/464612" target="_blank">📅 22:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d245dc30.mp4?token=mwR-kjvE-KbI9l1ahFVQrFvUy5wLCl6GsYzYr3fNcz4QEcKDgjHk2oelHjnvGFpGUnaF8JWf22_W_FHhENUnRs1wfizHe9FpLEB9l1OW0H9boRBJwjeFY-rGbstqr6Crff80-T9WHr_g4H350vE_4LPirZQtbOkC4w90qSiNRAOZ5Qp_pn6kCjjv4JFmD0tsDKskjLAPDWI4ZcSWfADLeebhRWuz_W_LEefonjaLu5Efc8v1UNaJLSaL-HJqtFXqK1JZgetMVkpGNT508afmG17qaOI26oFA7YInDVJeRPimMnOAQLAZ_KnwM8hs8tptlXHg2wj1kybXlVtMmT4eaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d245dc30.mp4?token=mwR-kjvE-KbI9l1ahFVQrFvUy5wLCl6GsYzYr3fNcz4QEcKDgjHk2oelHjnvGFpGUnaF8JWf22_W_FHhENUnRs1wfizHe9FpLEB9l1OW0H9boRBJwjeFY-rGbstqr6Crff80-T9WHr_g4H350vE_4LPirZQtbOkC4w90qSiNRAOZ5Qp_pn6kCjjv4JFmD0tsDKskjLAPDWI4ZcSWfADLeebhRWuz_W_LEefonjaLu5Efc8v1UNaJLSaL-HJqtFXqK1JZgetMVkpGNT508afmG17qaOI26oFA7YInDVJeRPimMnOAQLAZ_KnwM8hs8tptlXHg2wj1kybXlVtMmT4eaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ پزشکیان نیویورک را به مقصد تهران ترک کرد
🔹
رئیس‌جمهور پس از شرکت و سخنرانی در مجمع عمومی سازمان ملل نیویورک را به مقصد تهران ترک کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/464611" target="_blank">📅 22:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464610">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
آن‌که گفت هیهات منّا الذّله!
🗓
۲۶ سپتامبر، سالروز شهادت سید مقاومت، شهید سیدحسن نصرالله
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/464610" target="_blank">📅 22:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464609">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6447471c66.mp4?token=DHTYS42GGclTe9rLh_2Ry38MItUE7hMD8xclst2q6WKgQSP6kEMeDNjSgqdCI_r5EAdBWkVY0v35pHrL07fXD6GpY8vDnJNujs__hDB8DcrW518ICptJ293fPEdPOdQM1d36o9bxeTU99TCTjxZysB-vr9ZlcwhxJWI-7yLv36_XspqdKxb2_Iut_vjm7MpULdVDLuYTjWoPtmmv2saPcmCmLA1goU0snU-ZL6VCDuMzspDMYMk76ng1umvVkFyoVZRNMaXgldD5bD8aG089oyXewqq6VP4XSllxms74i2bjh0wkKxixgn7mW1EQDjVBRyVfQ15zfOoFM7YFcau37g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6447471c66.mp4?token=DHTYS42GGclTe9rLh_2Ry38MItUE7hMD8xclst2q6WKgQSP6kEMeDNjSgqdCI_r5EAdBWkVY0v35pHrL07fXD6GpY8vDnJNujs__hDB8DcrW518ICptJ293fPEdPOdQM1d36o9bxeTU99TCTjxZysB-vr9ZlcwhxJWI-7yLv36_XspqdKxb2_Iut_vjm7MpULdVDLuYTjWoPtmmv2saPcmCmLA1goU0snU-ZL6VCDuMzspDMYMk76ng1umvVkFyoVZRNMaXgldD5bD8aG089oyXewqq6VP4XSllxms74i2bjh0wkKxixgn7mW1EQDjVBRyVfQ15zfOoFM7YFcau37g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
🔹
رژیم صهیونیستی که وحشیانه‌ترین کارها را در غزه انجام داده و نتوانسته آنان را وادار به تسلیم کند می‌خواهد ایران با ۹۲ میلیون نفر را تسلیم کند؟
🔹
نتانیاهو ترامپ…</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/464609" target="_blank">📅 22:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464608">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd04dde131.mp4?token=iYkOrJnaKhqmytAotNdrr9VaiW-EnjuS8_1CkP2-cAy-cz40iAcU8uoxafPjgwZx-VFYz4dohJo7gXDZcEUMZomD3azO3au2psR-GbJqkFrga9dxC7BVV8aTw1CHQ7y2BZdMSw4kWV3FbD6RR006I3w8-rhMoHh83sGjQSP-7EEtO4DKeZ3a-Ohr4NPyRA4a6pmRY4P_MARNWmHowssZw1m4lWpX05DEAYsIZpBgzMl7KEBgE9bIQSU1wjBsCks1C5MnwPKx0hY7s5P2iIZ_vVwMs0WYo311BLj-8zHdiYZxdN4AGEbCitby6rSIWKi9DEiiwopDR_UW2JyGZ7_A9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd04dde131.mp4?token=iYkOrJnaKhqmytAotNdrr9VaiW-EnjuS8_1CkP2-cAy-cz40iAcU8uoxafPjgwZx-VFYz4dohJo7gXDZcEUMZomD3azO3au2psR-GbJqkFrga9dxC7BVV8aTw1CHQ7y2BZdMSw4kWV3FbD6RR006I3w8-rhMoHh83sGjQSP-7EEtO4DKeZ3a-Ohr4NPyRA4a6pmRY4P_MARNWmHowssZw1m4lWpX05DEAYsIZpBgzMl7KEBgE9bIQSU1wjBsCks1C5MnwPKx0hY7s5P2iIZ_vVwMs0WYo311BLj-8zHdiYZxdN4AGEbCitby6rSIWKi9DEiiwopDR_UW2JyGZ7_A9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۰شب ایستادگی گناباد پای انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/464608" target="_blank">📅 22:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464607">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8de0a4b3.mp4?token=Gd246c_7L3TTAtkGATYv5qT4hH7kv3394jBKsrE8auUMpoS_ezZQzSg2B5WdJPdo4GPvyOiIn57pzVYMmqNphNd8meE7i6Nxd8OLqR8fxASQUGbtmyHI63DB2v-LOoQEM0Oi6ydW1BjgiODE9gf8Mcu4ShcWkslI5WuMLAux4d6iUWIzRhrih8SHJ1QxwIEwl9Wuc4pFeDwLc5Oby6ma0dNmAoFLwqhxRbsdm3dSnUJGNS9jkKQOaovVvdVHVZw09Gel4Onv3MP8nBMYGjLHKwQHwazoNVjcOVADtilY0sZli5tgC-KSHMTOpMUTuG3oKMuz6X1GL6BK3ro6S9sCPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8de0a4b3.mp4?token=Gd246c_7L3TTAtkGATYv5qT4hH7kv3394jBKsrE8auUMpoS_ezZQzSg2B5WdJPdo4GPvyOiIn57pzVYMmqNphNd8meE7i6Nxd8OLqR8fxASQUGbtmyHI63DB2v-LOoQEM0Oi6ydW1BjgiODE9gf8Mcu4ShcWkslI5WuMLAux4d6iUWIzRhrih8SHJ1QxwIEwl9Wuc4pFeDwLc5Oby6ma0dNmAoFLwqhxRbsdm3dSnUJGNS9jkKQOaovVvdVHVZw09Gel4Onv3MP8nBMYGjLHKwQHwazoNVjcOVADtilY0sZli5tgC-KSHMTOpMUTuG3oKMuz6X1GL6BK3ro6S9sCPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: می‌خواهند ما با ذلت با آنان مذاکره کنیم؛ ما می‌میریم اما زیربار ذلت نمی‌رویم
🔹
چطور باور کنیم که آمریکا که رهبر و بچه‌های مدارس ما را شهید کرده حرف‌هایش را اجرا می‌کند؟ @Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/464607" target="_blank">📅 22:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464605">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325d9f4c33.mp4?token=SwAn9MQJ0CIDTcKta8lJOvqLy0uu8Hfjjy1PYJoK-mXDJrUhNOqumrZrmN4yc81AQmUxxuBGclG1_3Ilr4Yewe1AFXozD8NS5dk6sWz5fk_sqMaDp96rlWqc0VPLH7PFtPEGzM5pRcEROgfO3IsInaxztAxTBEGZfzQgjbU2wJLTIGsthHSFGV2ox7H2njHZ6ovgx0orWNMeYZA5Dywb0fohJ-c5IQ3s1hPxzvENWfR0jZasOD1INVMWHBzNzDmMAw8s4uFsr2lBN7f6BoW9E02ISQB7Vo4Gcim_Nu8XxJoKY0zlFZIGr8tZUQqqW_hS3wTa-7I_O2_V4tyUmli16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325d9f4c33.mp4?token=SwAn9MQJ0CIDTcKta8lJOvqLy0uu8Hfjjy1PYJoK-mXDJrUhNOqumrZrmN4yc81AQmUxxuBGclG1_3Ilr4Yewe1AFXozD8NS5dk6sWz5fk_sqMaDp96rlWqc0VPLH7PFtPEGzM5pRcEROgfO3IsInaxztAxTBEGZfzQgjbU2wJLTIGsthHSFGV2ox7H2njHZ6ovgx0orWNMeYZA5Dywb0fohJ-c5IQ3s1hPxzvENWfR0jZasOD1INVMWHBzNzDmMAw8s4uFsr2lBN7f6BoW9E02ISQB7Vo4Gcim_Nu8XxJoKY0zlFZIGr8tZUQqqW_hS3wTa-7I_O2_V4tyUmli16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: می‌خواهند ما با ذلت با آنان مذاکره کنیم؛ ما می‌میریم اما زیربار ذلت نمی‌رویم
🔹
چطور باور کنیم که آمریکا که رهبر و بچه‌های مدارس ما را شهید کرده حرف‌هایش را اجرا می‌کند؟
@Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/464605" target="_blank">📅 22:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464604">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am5KDUh17EqnfZPgdy2IZwSmrUFGK24OZ7wtHeZCmsoKRMNmN_F9PvqYog4IUH-otCIyXjJhoy7QacK3t4YN5sGDazdWmyv_uwm_7KTe8EgFSbCen5jyncoYu-5njna83-zddyopqkG6Pi7Tofn0oCgJEJX43O4WHuN4bWw_r7vEr6OD_ldyF9xSm8_GxZEujlfWTweEmE0sTd_x-MIkac-AB71hAigQ0D0TWYtWalgw0zxmS6CnrjZyBSYO-EV1UkLSGjcVDZoe4Bbcf4SAjojgdcTlWOnKO7b8IbjyvGktnTcN9-SAdNrq4qsbcknneuIaulZlEkNxZvLogYuCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا اصلاح‌طلبان جنگ سوم را هم به ایران تحمیل می‌کنند؟
🔹
در شرایطی که ایران ۲ بار در میانهٔ مذاکره هدف حمله قرار گرفته، دوباره همان نسخهٔ قدیمی روی میز آمده است: «صلح، مذاکره و تفاهم»؛ اصلاح‌طلبان مخالفان خود را به جنگ‌طلبی متهم می‌کنند و خود را در جایگاه مدافعان…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/464604" target="_blank">📅 21:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464603">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb25a6c32c.mp4?token=sH1_FVmTFTxQNNSJt8CG0LOjAxxMjN2FjRy1_hFwshaGMrVv-xJVsZHtqUCG3PBCE7uQFkNlTUup61AXCCLDBPgfRS1nmvkvoTHZJ3tq9XssJS6T7oizY1Dfm0laph8KvQBB1raX8xg1wBTSw4GbdbiAV3skuoP2Pj77vYzrJdEV37-lHb3jgoz2azLEwEknaUF2664k3esfdi2ISbov9QHfjsdoOzrUDPgfI1O9BYFsA54_Nm_AK1UU6aiWU5aZdatsVR1ZgWZfZ-K4e6LYnoIdmcECLhlyMlrsFTtj_KDZ4DpQNGhLihHq1nUrHMo26zfx1OQP2DuNwvcIeQiAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb25a6c32c.mp4?token=sH1_FVmTFTxQNNSJt8CG0LOjAxxMjN2FjRy1_hFwshaGMrVv-xJVsZHtqUCG3PBCE7uQFkNlTUup61AXCCLDBPgfRS1nmvkvoTHZJ3tq9XssJS6T7oizY1Dfm0laph8KvQBB1raX8xg1wBTSw4GbdbiAV3skuoP2Pj77vYzrJdEV37-lHb3jgoz2azLEwEknaUF2664k3esfdi2ISbov9QHfjsdoOzrUDPgfI1O9BYFsA54_Nm_AK1UU6aiWU5aZdatsVR1ZgWZfZ-K4e6LYnoIdmcECLhlyMlrsFTtj_KDZ4DpQNGhLihHq1nUrHMo26zfx1OQP2DuNwvcIeQiAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روز سرباز در منزل یک سرباز شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/464603" target="_blank">📅 21:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464602">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d6a51cd6c.mp4?token=iOAeM_QwsFYJT_9dWzN5n9gu50aq9-77lU18aa3XN32KMAbbHHmwo1H7R1G3Tl9sxAQbDaLMht_MAds6XTfOQlj5KzuQVxom2yRGRWHSnTplkAYNANqKptGlbL5AcwxWgmMemYOYzweLP3kXnzT__UiJaMV86eizUAmKuPkoLOiZ6cvi7WeD_VLf7OwIOYzhBOhwF_Ks3_T7_RweRtpkPD7Ld1FlOgin8PhB8Rya9BKq8dM3ml-y2ffMJshQhlpHJwya2maZEi-9fJ1jPyKbXm5Z_bRydfAVLG77OlJpo6lP1-i81ds3mETjBWnHnXZzShvBJK2zVYq5IAus3cKd0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d6a51cd6c.mp4?token=iOAeM_QwsFYJT_9dWzN5n9gu50aq9-77lU18aa3XN32KMAbbHHmwo1H7R1G3Tl9sxAQbDaLMht_MAds6XTfOQlj5KzuQVxom2yRGRWHSnTplkAYNANqKptGlbL5AcwxWgmMemYOYzweLP3kXnzT__UiJaMV86eizUAmKuPkoLOiZ6cvi7WeD_VLf7OwIOYzhBOhwF_Ks3_T7_RweRtpkPD7Ld1FlOgin8PhB8Rya9BKq8dM3ml-y2ffMJshQhlpHJwya2maZEi-9fJ1jPyKbXm5Z_bRydfAVLG77OlJpo6lP1-i81ds3mETjBWnHnXZzShvBJK2zVYq5IAus3cKd0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اعلام جرم دادستانی تهران علیه عوامل متخلف یک تئاتر
🔹
درپی بروز رفتار خلاف عرف و شئون در یک تئاتر، دادستانی تهران علیه عوامل آن اعلام جرم کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/464602" target="_blank">📅 21:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464601">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1H4hYPPcaiGEuHLuOnb7o6Guh0ttwDOE69okSuIoLOna_S1C_RhpArlpW3I5QYrZbt_FHuMrnHhtJlgvGh5YNllMbgvHj8hNZ2etjLdMSE4eP2G_deTM-p4jfCE3gc8kvt1CJK0pvXjZ1NP1b-52DzGukiGbyrk0BVSF64ef6L_SLwdc4h_ujeo8sIRSBVt2prrdwbmFO6xZDDgBzq_s8oAk8BCYw94jXc7zeYxCbqsALeXX0Qt7fTjPExe72FGU-R-ngOsswlFnDTYFbfquMhXk8kTwp1iJb8-RcAtVSHThov8CdXy8XF9hfWUTpX5kr2bWN0-q2P2KxBomBguKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر شهید ارتشی پس‌از ۴۰ سال تفحص شد
🔹
پیکر شهید علی‌اکبر گندمی پس از ۴۰  سال‌ دوری از وطن، کشف و شناسایی شد.
🔹
شهید گندمی در اسفند سال ۱۳۶۱ و درحالی که ۲۴ سال سن داشت در عملیات کربلای۴  در سومار کرمانشاه به شهادت رسید.
🔹
مراسم وداع با پیکر این شهید فردا در معراج شهدای تهران برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/464601" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464600">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_J2gB4-MdFOkhA-GOBi_j0PpR7IFHWHu4Td0Bzdii9JdmIxdPF5sTYwl1t9BdJsNg7ts-KcE8q78moYhUDqIF8EIWnYj4D_qeAGQtaJA8BSrW_TUSR4507bm3pqn-pS6XakeafMqgT1d-xOFoRKTzxsyX7AZ9I2qZktawPlY4nyoF7ZZDCcEUTdolaRjOubfotTqzwCtD6WCcL-p7Ik_-Hz5kVqck8BaRRYpPNOjTTOhdQNHcwDh6w6oBYisJCgy39W-vBn8veXwTiJPT9V_fqtC8RBZGsaSJWOxjfSbwvpgb5pOB0BPwgCDl-ZfLdrib22T9H0rR2oZF4kUoejuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: چگونه می‌توان از خلع سلاح هسته‌ای سخن گفت اما زرادخانۀ هسته‌ای اسرائیل  را نادیده گرفت؟
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/464600" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464599">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروابط عمومی چادرملو</strong></div>
<div class="tg-text">توسعه جبهه‌های جدید استخراج و اکتشاف در چادرملو
🔹
عملیات آماده‌سازی جبهه‌های جدید استخراج، باطله‌برداری و اکتشاف در محدوده‌های معدنی چادرملو در حال انجام است؛ اقداماتی که با هدف توسعه ذخایر و تأمین مواد اولیه مورد نیاز زنجیره تولید دنبال می‌شود.
🔹
در این برنامه، همزمان با ادامه فعالیت در معادن فعال، شناسایی و ارزیابی محدوده‌های جدید نیز در دستور کار قرار گرفته است.
🔹
توسعه فعالیت‌های اکتشافی و آماده‌سازی جبهه‌های جدید استخراج، بخشی از برنامه چادرملو برای افزایش دسترسی به ذخایر معدنی و استمرار تأمین خوراک واحدهای تولیدی است.</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/464599" target="_blank">📅 21:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464598">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک کارآفرین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3321f40cb8.mp4?token=fvwr4OKrYOAxRs7sgDrWAO3icyKja3hFa5dP0renKf5052zZnO6qZp0-wLHxoti0j_a2ARQYk4Y6YEacgvILGHOJaIodjYy1h2YenvX2Y3pI2sSdCvIVSFNAYzeSnlGufODMnS0XMCycIArVJWiOdTfRScWbBj92Dhh4ejecxfvaLDyPK8jejyuAZoRO-B3CHvAWTC6Khy5PsYmg3zZepXmWeJo1DxpmCH2cSmeaJgOOeZQkxdh-ga-RJTwd8viVrOw2TAGF4pUZTh8xVrZgWllKtJK35oL9tHvviKdIm7kO3kL8XHFSKWEkks29wAhqOtR3UtzdZ553BUIept6BQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3321f40cb8.mp4?token=fvwr4OKrYOAxRs7sgDrWAO3icyKja3hFa5dP0renKf5052zZnO6qZp0-wLHxoti0j_a2ARQYk4Y6YEacgvILGHOJaIodjYy1h2YenvX2Y3pI2sSdCvIVSFNAYzeSnlGufODMnS0XMCycIArVJWiOdTfRScWbBj92Dhh4ejecxfvaLDyPK8jejyuAZoRO-B3CHvAWTC6Khy5PsYmg3zZepXmWeJo1DxpmCH2cSmeaJgOOeZQkxdh-ga-RJTwd8viVrOw2TAGF4pUZTh8xVrZgWllKtJK35oL9tHvviKdIm7kO3kL8XHFSKWEkks29wAhqOtR3UtzdZ553BUIept6BQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرباز یعنی کسی که پای عهدش با این خاک ایستاده؛ با هر لباسی و در هر شغلی.
🇮🇷
⚙️
روز سرباز گرامی باد
☎️
۰۲۱۲۳۳۵۰
🌐
karafarinbank.ir
📱
@karafarin_bank</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/464598" target="_blank">📅 21:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464597">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/464597" target="_blank">📅 21:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464596">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861b5f45bb.mp4?token=vtTh1FBWcGLYLNmOxqd52T68xDJQWPdwk4wpQiHjX8LT6XP6W03I2vFd0AaLQauL_4qTWN1yjDfvG9q_9endHxmyyxWmiDEjKPMj_oHGccRzOprEYnuqbxO0zv-JmYHR6EOAuLEFwt_b8-kaSdlrpD9x6rdlIx3_SF53APsYVEcqPjdzcjydS7Y0AubN6Z_223b0cLr7ix2bz3PaSFQYdmUdWUcTQNOeOR0gbWI0y_6BOkWCb2gcm12BDR8MsyRAPK9uMTU7hjKY9t9uLNcv3x8UBtS6F7s55-q-qM2cA7PETN81J5WatKZAauihDOJmMqdtwZU18FPenDCffHZ_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861b5f45bb.mp4?token=vtTh1FBWcGLYLNmOxqd52T68xDJQWPdwk4wpQiHjX8LT6XP6W03I2vFd0AaLQauL_4qTWN1yjDfvG9q_9endHxmyyxWmiDEjKPMj_oHGccRzOprEYnuqbxO0zv-JmYHR6EOAuLEFwt_b8-kaSdlrpD9x6rdlIx3_SF53APsYVEcqPjdzcjydS7Y0AubN6Z_223b0cLr7ix2bz3PaSFQYdmUdWUcTQNOeOR0gbWI0y_6BOkWCb2gcm12BDR8MsyRAPK9uMTU7hjKY9t9uLNcv3x8UBtS6F7s55-q-qM2cA7PETN81J5WatKZAauihDOJmMqdtwZU18FPenDCffHZ_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم خطاب به سایپا: اول خودروهای معوق را تحویل دهید بعد ثبت نام کنید
🔹
در حالی که سایپا طرح فروش بدون قرعه‌کشی کوئیک و سهند را برای مالکان خودروهای فرسوده اعلام کرده، تأخیر در تحویل برخی خودروهای ثبت‌نامی قبلی سایپا همچنان محل گلایه متقاضیان است.
🔹
برخی مشتریان…</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/464596" target="_blank">📅 21:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464595">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b6126dca.mp4?token=BJB7o_1--Tptgdh_POUDUdDV0Kc3oM_meXjrHcxXdLP0MpcUuk2YZ4Zd6DARJ2y2XIncsjGnBXZOaOylXiKMVeSrKS8UA8YToQ2FePvMUKQXVG_nCCGL3h1tXbHSq9PbrhmgvBKMBG1Do-9snjQPrG5fbhHiQRiCeZ8wiPjFkVZRIgh1ksGhc7cHtfaIvvwAWCDIbi1QHodk9JRbhPS1BDix316ufiMpVT2wdj6RAXW4IC13ANd-hGRf10gx2oVG4F3i2MM_tAIx5fsM54B0CXHD21L3W1Fn55tGdx6KhsufERGj_jNgHnQkk-K2tyvcEaKbypLLaic56WKNPAIG1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b6126dca.mp4?token=BJB7o_1--Tptgdh_POUDUdDV0Kc3oM_meXjrHcxXdLP0MpcUuk2YZ4Zd6DARJ2y2XIncsjGnBXZOaOylXiKMVeSrKS8UA8YToQ2FePvMUKQXVG_nCCGL3h1tXbHSq9PbrhmgvBKMBG1Do-9snjQPrG5fbhHiQRiCeZ8wiPjFkVZRIgh1ksGhc7cHtfaIvvwAWCDIbi1QHodk9JRbhPS1BDix316ufiMpVT2wdj6RAXW4IC13ANd-hGRf10gx2oVG4F3i2MM_tAIx5fsM54B0CXHD21L3W1Fn55tGdx6KhsufERGj_jNgHnQkk-K2tyvcEaKbypLLaic56WKNPAIG1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نشریۀ اکونومیست: آمریکا از خاورمیانه خارج می‌شود و ایران ابرقدرت مطلق منطقه خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/464595" target="_blank">📅 21:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464594">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9505bf3674.mp4?token=Hnza6JulVz6aCUa3D_VuXzdFL3P8IE8R9-N5oRHAgYGVAM45eKBIUYEfwZqMCR0EAmVM4PrPCE1SwBYPnUu32RX_1G_pWTUsN3bvQKgvetaN8WRa6xG6wEICRNVfJz2Pi1RG85k-JGMxhXRkc8ZcCyGsVWmP4wgC1NPlL5mvqA6b_HMCY5F6Gac0P0kRMlPauC8fNlTV_3jFmEoYIkzwGV2QkqIUN8UZDv_RVRhITZ5ObIOnUMS7-_ZfMOs37g_UEYWIjAUctDZqYh0cFfn5vPE9fPD77YSmK96FYG8D5prVpg8B9pWpXkuecrJCnNoLUJC-oudM_UYu50hR0vU3I4POeRHzNrs_yvAubaEHt4fTPrwOPrgC5eI8EkQDOWgPa4TyC2SQtG9jb3AJikDtnaZ5Tea7mk7HFjZNiZaEueEMdA6CI15-zdz8BbquMOuqcCHTbnyco2WFls_DGEuSnY0qPABg-GzsN9o2o6hKCkAYaRx0J2naMDqOL6QQnF5jjsB7zIq2GDTrpMR3oHfa3FsrHzsEefG3zwhzD6mL_R2urJcRJmbJ7ZQBQw5DQFBX6g8hs9PLKeW2NDwsWSCuh53ObJ-_1TzfwB1nCBOdRp-QOsXZ1EfYg_huN1VM9_l9O46gFlpanKBFLp6soK1N4Y12baqk7IQjE3My0o_VhyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9505bf3674.mp4?token=Hnza6JulVz6aCUa3D_VuXzdFL3P8IE8R9-N5oRHAgYGVAM45eKBIUYEfwZqMCR0EAmVM4PrPCE1SwBYPnUu32RX_1G_pWTUsN3bvQKgvetaN8WRa6xG6wEICRNVfJz2Pi1RG85k-JGMxhXRkc8ZcCyGsVWmP4wgC1NPlL5mvqA6b_HMCY5F6Gac0P0kRMlPauC8fNlTV_3jFmEoYIkzwGV2QkqIUN8UZDv_RVRhITZ5ObIOnUMS7-_ZfMOs37g_UEYWIjAUctDZqYh0cFfn5vPE9fPD77YSmK96FYG8D5prVpg8B9pWpXkuecrJCnNoLUJC-oudM_UYu50hR0vU3I4POeRHzNrs_yvAubaEHt4fTPrwOPrgC5eI8EkQDOWgPa4TyC2SQtG9jb3AJikDtnaZ5Tea7mk7HFjZNiZaEueEMdA6CI15-zdz8BbquMOuqcCHTbnyco2WFls_DGEuSnY0qPABg-GzsN9o2o6hKCkAYaRx0J2naMDqOL6QQnF5jjsB7zIq2GDTrpMR3oHfa3FsrHzsEefG3zwhzD6mL_R2urJcRJmbJ7ZQBQw5DQFBX6g8hs9PLKeW2NDwsWSCuh53ObJ-_1TzfwB1nCBOdRp-QOsXZ1EfYg_huN1VM9_l9O46gFlpanKBFLp6soK1N4Y12baqk7IQjE3My0o_VhyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرباز ایران کیست؟
🔹
مردم در تجمعات مردمی پاسخ می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/464594" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464593">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
منابع لبنانی از حملۀ توپخانه‌ای رژیم اشغالگر صهیونیستی به نقاطی در زوطر شرقی، تمشیط و بیت‌یاحون در جنوب لبنان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/464593" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464586">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGKPkxRqqjGU3iMHKjsAHOy-scg0ElUR4e3K623sG32i3saqO7fQgEyzjL64qJrDw1fAX62JLBW1l5UJ-6mBy57QGTUW36V_DGFlJQHHd827GJOTsM6BXMrst7Z5JNCqmjOsPKgh8igIE690uv_63SWd_7jV75xMfh63Vk2fAb5rlzeag-tRvL_YhtvPPgSpV22pFscLXLqcXVDkIFtlQJ6PkofKitAnIqCLFzU2tJMkx5pV83-1UY27x9jp1Uu4gU61zIbK6smyJraOBLClgbeQZLQ33muh3fn558qXGwP2DxAZ7CnJKY1Xx6bRBfffILIvY9e9AsEGsOhU-FiqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Voql43_1FBmwjv2SZDvQznAD-m-2GjHq33aIU7RcQG6PT31U4X40hdUKbf7Z5BJNIBcL4Jm8l1oEwakJot_gX91fgpx82JZRkjOADW787cMdvJvDMHNSKyuZ4mD056BReauSnqfoxjKEyNOuO_KqkKlwJrQNA3d0kbI1HQz4vuF5GmRlVZyYqv5KCH7pPtuB8YI5Pnh80EGeAFMxJcl0FFM_rr7T5X4bVrAyPt-03bm22rL2mQAaFpdAX0lxUOKHO1zAu84dUm_9URGEulSOckEEHZHUKiWcjaUI32obe2QNSMnytxNt9uf3pL31P_tdbZV0z-Usjr3Rx-dRiol2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6D6QO9QgjavbBJhKwOgVfOrIC4IjnKv8LV85KBInAH11rLIMQTNAKYYI1G_ibpdc-0CC6_-WLJWnTBmq59NqOQMpoBzQAo744pcOVzlfTBPALNy8C0ySRgzzDyBKKDnwfmvs658WhigCbFlIPJZx2AAguJqJ0eT_fPCVAUW5qXq4aLcUdKnzQGmEKuuCU__3fHgQDxUg52CzXW0Wr7HCgSmzIHdRgVbGfuczAYxgnCEVuQGVAwYngePInRvgyXEOUPwOhx1pt1JXND6IFt9rrn93ToBWTgdmg_uT_O9TEsgzbUX5mvNH4BoQRbmO7A9yqGaAek_xksNoujrFzBJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmS0RFj6pltQQ18_H1B1mtAT-tyBmSHRy-2g0uZLNrXNvCRCfHHY0rNUDuITJN_p8tdk0bqfnf31YDWu_3PzutncnwStbQlt7k7d4VAm2P4EYm07Zr6fvB9XP2ZAbvCIkmgPHSHHGA5pbL4HTaB9v1Cr0uZHdI7oGN4nz600HflLjZU2juqWUrMg4D3cbZ1Svtfku2yY5wKCIUnInXPVbUGAHvEIrOgTIqyyPp8Uex6bRzh0JlX7uhH_RQn8VUN5P7hsaWBE01yf2aLDWGeYABMZJYnNA-c4itLH-EPZgWuhqxRpGw15tPnGA2GAC9M5J35_wIx9xixYElh-LpgjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsSukDxJXPfHBq01fkJY50v_ZRM7Udxrnl3pKbRAkc6TiLxNZQPA3ND6txVpHbtRljx-a4Mb69TKD8RbqCz9ijbbXQ-sOUc64Wygc4UFg9tIi8Ox7GWgLzs1bMYp3PEn04vu1grkq1I3Ifv54-Xmal_pD-WeSs8FUT__aqQMAm3QojmR7bHKaQAwi-iOEgueJKzKvrBziI-u-LrW8pJSysEWqyZdfA06J_QR0hqP_QlUkzfId5n3cB4hnO9IzkqGHu_xIDHHLobV4wiuyfBnphhGdxxXdxnC02WtMF2HuSpp9TV0q-tchR4TVPKzuYv7rfkr-Xpu8zN59hKzImQZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0gT-yOLoZEGLKhNaq4Mu9CuQS4uK8JaguNyNvfp5zpxd4kgVktm5-G7ZeiUMyfNGM60vlVqULDNkeYDAE5BNzZV4fQ2m-jcrwxuMn7sEFJDFCKj4gu7VBZGLNF_4Z0A-5gop5EbGnlJNh5EYchivbtzR_kSBtwRfjM4sOirH-RM0C2mI4DXdE9dIAMtpxisajwnyTsIF1Zg4Z3ctDFIX24-HI53F4QcktuKeYxV7e9WXrsRL6cYnafrMs9qeaEGs8RXojZSovlP8wdp7wxlzaHlg7qdOmUZwhR68MvGkvG2qUM48qiOnsQyZDLQRSAoPeHYYfPT8KDBqp_H9TqliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puFFiKeuZXi9ZPTn1DQUa40vCOGHKpTLifwa35S1UMNSwiQFfPyusVVMTpEZtBtgtZDdWNC-bxz7xJlRkbQZ7zR1s31Y0fSwDoHzGvZhLwEIIc-hTaNeAVV6Uu62B4WU9rhPuj5Dwjufylsk73LvRN337DXNaFMCbzMeoJswXR8kpIyXI3o4ibLYJeZt5M6_9XSSweAMKo6F9dBIMsZ7KqasUZn3XQiGfHsennRLlVxllR7XeYAgFk3D7j0UHZRH6vzc4iqW9B88rxacKq6MkDDe64hxMNNE8aZOuokAjP6gaJWMjbaemSnHC3YljLb6YNMYRBfzx0kWK7a2m1h5Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یک قرن روشنایی؛ روایت کبریتی که از تبریز برخاست
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/464586" target="_blank">📅 20:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464585">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0dc7e782f.mp4?token=BtqMGnkAEH_dHtOVOPVcTRhD2W3TTtFdZSaui24kFaFSFB8PeUBuLJg4QaFbHtXw51sl4GdayBSy2X2wxyRpXshZqJNxii8_zt5As4yHTGwdVq2k4sTqoy63-dLYDI0es_hkKZK8S9Hsb0kv8YFXBhUiyYvp4EFkIv9Zct2EN35bpVKaQV-Gpb7iFSY7jX3vSSQb3yRAZw1I8McpOTKzCHUnIx8mz8nl8KuXCwzlGqTqnusPkNhHePvtxQTXClYOTz-OIL4_Gegs5bl6hH5icqZ2dtHOB85zu16I1FoA_9cR8uI3WLvzvlCPAejAxiaEeeoCU6Cwnkhd7FUMXNP5Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0dc7e782f.mp4?token=BtqMGnkAEH_dHtOVOPVcTRhD2W3TTtFdZSaui24kFaFSFB8PeUBuLJg4QaFbHtXw51sl4GdayBSy2X2wxyRpXshZqJNxii8_zt5As4yHTGwdVq2k4sTqoy63-dLYDI0es_hkKZK8S9Hsb0kv8YFXBhUiyYvp4EFkIv9Zct2EN35bpVKaQV-Gpb7iFSY7jX3vSSQb3yRAZw1I8McpOTKzCHUnIx8mz8nl8KuXCwzlGqTqnusPkNhHePvtxQTXClYOTz-OIL4_Gegs5bl6hH5icqZ2dtHOB85zu16I1FoA_9cR8uI3WLvzvlCPAejAxiaEeeoCU6Cwnkhd7FUMXNP5Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیئت دیپلماتیک کوبا حین سخنرانی ترامپ جلسۀ مجمع عمومی سازمان ملل را به‌نشانۀ اعتراض ترک کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/464585" target="_blank">📅 20:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464584">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2hRABXFYRETCZyoUGcL0fEOzLqKNx5yM8WQVNL0-l44bFJH23SAvcsFyfRslGJ5hH4ut3t9pb6Xaz5E1YLfSvQ3eqBPMx1etn13Q9tRV-vzhPozz4-YBK5rslxktd8fqHAGVdU30BqG9pN-4PxNIeThiXNBfqciJfgm31ynJ4J6uUGWWLfA3RJu_V_OpyHjVZ2ClYUJvXOSJ6ci4UNrceyoJElCeQ1lRsCDmCbArQHT93gTogxbR9ybn9Fz6TPDU65Pfw_lpP8tJDRiagHGTtBFOv-8G-NTspAu_Oluv_GpgVQkUC3rLWu33Ikk0WOlufJy6JzjNVPN_A4cp1U5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
واردات خودروهای لوکس در شرایط جنگی؛ بر اساس کدام قانون صورت می‌گیرد؟  @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/464584" target="_blank">📅 20:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464583">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e42be5851.mp4?token=R9s__0TwDxMx396XFQAZgMxVNmhu6ev2P881csMvnS0nFYF6Ol4SMxEOJM_82Um9tIJBhlsLpv5nG_Z7Wc9RzkG37WNUIg-iMV8pWf-o5KoL1imTAxIx8F4f2BoPjlZDj6-twsyT91C2fLPlJAZzlXsj7vLhiKwCbApj0pt6Fx0c-_R9JGmrmO6ZU_lGnVocmsQfS67t_ZIWM_HHFr-GbhqBssZy5VYSG6PgdbqyDOdx9K5VVfvvSz9I8gWVaMExuLtz8alGNwbiPWD5Q3Na0_RKW6ViISASXfe8llPKsEuCd6FObyKgN5xlwlcNc6zIq4Ijhawik-hYHNdqWRQfQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e42be5851.mp4?token=R9s__0TwDxMx396XFQAZgMxVNmhu6ev2P881csMvnS0nFYF6Ol4SMxEOJM_82Um9tIJBhlsLpv5nG_Z7Wc9RzkG37WNUIg-iMV8pWf-o5KoL1imTAxIx8F4f2BoPjlZDj6-twsyT91C2fLPlJAZzlXsj7vLhiKwCbApj0pt6Fx0c-_R9JGmrmO6ZU_lGnVocmsQfS67t_ZIWM_HHFr-GbhqBssZy5VYSG6PgdbqyDOdx9K5VVfvvSz9I8gWVaMExuLtz8alGNwbiPWD5Q3Na0_RKW6ViISASXfe8llPKsEuCd6FObyKgN5xlwlcNc6zIq4Ijhawik-hYHNdqWRQfQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران شکست نخواهد خورد
🎙
نماهنگ جدید محمود کریمی به زبان انگلیسی.
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/464583" target="_blank">📅 20:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464582">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756a67dce4.mp4?token=C7sNtqMxMOppnHSj41K7KccDW3G93VewtqSNC1xrlu-6MdDfIouXZPb8zEKdmHHDABS0ONNrNLIa4qwvuaM-kaTqCIePEE932z7lArgblBoUw2TmblMKwftJA3IL4XNA2aiF-sHkT1pH4eBxSnm-T8dDldmJpLlIW_Duo9PNEMCrorJkgoH53oy6NUluF0WLcgen7r8LF4wAjS0-ymH3qDiPLoV5ZGbiEpaXlDXJ1MKIzR6eLwzuSLetP7eHu9WMAvVFtLspJBdrKm6zO4df8dIxHKXcY8A-7rwIq3p-IxeCLZ5OkFnrb8nFP0FRPG6JZZ25_PKf_d7AIpA7egA7XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756a67dce4.mp4?token=C7sNtqMxMOppnHSj41K7KccDW3G93VewtqSNC1xrlu-6MdDfIouXZPb8zEKdmHHDABS0ONNrNLIa4qwvuaM-kaTqCIePEE932z7lArgblBoUw2TmblMKwftJA3IL4XNA2aiF-sHkT1pH4eBxSnm-T8dDldmJpLlIW_Duo9PNEMCrorJkgoH53oy6NUluF0WLcgen7r8LF4wAjS0-ymH3qDiPLoV5ZGbiEpaXlDXJ1MKIzR6eLwzuSLetP7eHu9WMAvVFtLspJBdrKm6zO4df8dIxHKXcY8A-7rwIq3p-IxeCLZ5OkFnrb8nFP0FRPG6JZZ25_PKf_d7AIpA7egA7XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
بازدید سخنگوی ارتش از خبرگزاری فارس  عکس: صادق نیک گستر @Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/464582" target="_blank">📅 20:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwQsxOX4csa9QM3GrVlK5F5Bvc2WgIjExDjtHySZ1icc2tO4CHMv7pldyhBiMzBZ-ZrCortyOjTpooq6ACUMX3j26JwpZhQp4ToiUP_1eTkzd3fdVjcdzetgD2labOerQ0HUqu-PYq2MkJ-wVFQZrW_KKzDzRwCEHMIWsKK-asRZsh2kHvBKS-5FZCTFAn0wBzwUMsu-tyiKWb1JC90EfoHT5IDHFSE0b32I6-uBz7eb2bRK5GGWZvH6lr7kh59aGzvYROKpM43A5-d1Za5p3hQjuracT8cBadWCWSaEnJ6-_ZbuA7X3K5ViNZLQnI6NtKld1QJl3eYKAEpUh_a2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاوروف: روسیه بر آزادی فوری مادورو و همسرش و تکرارنشدن چنین حوادثی در آینده تأکید دارد
🔹
آمریکا اوایل امسال، با نقض تمام قوانین و هنجارهای اخلاقی با حمله به ونزوئلا مادورو و همسرش را دستگیر و بدون محاکمه آنها را زندانی کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/464580" target="_blank">📅 20:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmr8SY2-kONIyDAZiSuawBPOA19R1mgh4WF8NHh_rNRw90pfMF-9OqnGVboqpqrKHwAqU9Kf2cMYC2Jg-fx9QtWcyyXkUOereBLToCPj1q6u5fWndadKvfdUZqCADyFg4dBNGWnnWkXInYKSYMUyy0ysckbzcMIBwMhfEKqGaDc2zIIt5Nd2xp03IgMCWrxsr8q5PYg4cHunC2mF7mRNqOpUdEWSmwRgymFcvs4HFbVm5ZSegh7ZMRcfgED3xsF_EgBFrIZ-krO70S_BRggbqLWij9ngX7W0JQIXnahmdmOh770JjtlMZvWVnu5y7i8-UiI5mMUy7aUAjxYiaqYg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  لاوروف: روسیه معتقد است زمان آن رسیده که به دولت فلسطین رسمیت داده شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/464579" target="_blank">📅 20:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر خارجۀ روسیه در سازمان ملل: روسیه ترور رهبر ایران، خانوادۀ او و مقامات ایران را غیرقابل‌قبول می‌داند.  @Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/464578" target="_blank">📅 19:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogJw8kCuS-82ibSyH0C886goh464JSsdKY1J-3JndmzjePd3fEooxlUHBSI-X4KY74vdHokzOEOwJHLrK0QjMH5osxs-bDtadSQgdJdKI1qnejVoYIHJmpDQaWVVBzJxqldzl9xxQP4QN3GvmIW2zhscIPqRsgMH5S44nNtjqrLvnPcXSfmsr3Gz8TFjqW12BA8Dm71Z7fKilNXMxJ0usDfnANMZFN3ix55u3B7DAjbeWcu2ghkX8PCL3PYmRUaIBiXmy5SjG608b3PIEZCRpbIdUg3D3Ii_SllY2H_M9V4mGaiotxU2bNkCdS8FyaAUL2Z4BrQLW4AcRkOKhUDu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ روسیه در سازمان ملل: روسیه ترور رهبر ایران، خانوادۀ او و مقامات ایران را غیرقابل‌قبول می‌داند.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/464577" target="_blank">📅 19:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464576">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuIWG3wtpjw3O3nK9Wq5aOyIt79v9h605i1hLpQimqnDHiIy8dAm3lbO5fdbwop1akTx9rtRea_yC8JGQK1z7MYSDEbCyO0BBdy_gCCEM4yxxe4Sf0CnY8cmhjrih_acRsDlLF6mcDsNyTW404KjV8JnKG26eU-lUC7_KT9ov_US5c-DnKaWu0yYjuYsqC-mHzL8AOkw60umeekATt2hfiIgR_a5xoqLb-GUOO-I43xaRryWFcHD41qlwshSZz7V6IKGpNI6Mm1Y7nZ7ooc5rzcr1W_OEC1ALCBFYddmJVSHqS3PfAXfKYAhfDbn4G_gRyTnc3D7lbT0laM68ORj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری عاملان شهادت مأمور ناجا در کمتر از ۲۴ ساعت
🔹
دادستان زنجان: عاملان شهادت سرهنگ دوم مجید بهرامی در کمتر از ۲۴ ساعت دستگیر و با قرار تأمین راهی زندان شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/464576" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۳ فوتی در حادثۀ واژگونی مینی‌بوس در بزرگراه کردستان تهران
🔹
آتش‌نشانی تهران: برخورد یک دستگاه مینی‌بوس با چند دستگاه خودرو منجر به واژگونی مینی بوس در بزرگراه کردستان شد؛ در این حادثه ۳ نفر جان خود را از دست دادند و ۱۷ نفر مصدوم شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/464575" target="_blank">📅 19:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قطعی برق بی‌اعتنا به وعده‌های وزیر نیرو
🔹
هوا تا ۱۰ درجه خنک شده، مصرف برق پایین آمده و وزیر نیرو می‌گوید، ناترازی ۲۰ هزار مگاواتی پایان یافته اما برق طبق اطلاع قبلی در خانه‌های مردم تا ۲ ساعت قطع می‌شود.
🔹
اما این فقط برق خانه‌ها نیست که قطع می‌شود، خالقی،…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464574" target="_blank">📅 19:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdK0N_lX1N6ATUu9Rr35B8uB5ArEWaCNl2IW1YxUvcmR2qq9yBRidkkFu6CCJ0OA8MZHIWQXEvZOkGlX_NMb2s_-ffbA4vGIF98QwAGZIhCl5WYkApNSyo87lYb9iSRMufTwUGx2pD3YSyWySm8gaxXyWaZeYnYVyTsMPvyef5EztcOnws9jBbcokFcFl-XdmLAjuFn_Um-nal2YCjNZIt-XUzkGNBksxftQleSp_apdNNuJXgkQbncn3Zlhu5681QeNiydW7I6Y9jyokvDDVlC1fLhI1DX8fsX0gwRXcE0HVPSmi4qbCc4ffN-R_y8VxsSlZhJ1bmAaP5X6rQvjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبی
:
دبیر سرش به کار خودش باشد
نایب رئیس اول فدراسیون فوتبال در واکنش به صحبت‌ دبیر:
🎙
موضوعاتی را که علیرضا دبیر مطرح کردند، باعث تعجب ما شد؛ به این دلیل که تکلیف فوتبال سال‌هاست مشخص شده و خیلی جلوتر از کشتی، تکلیف فوتبال تعیین شده است.
🎙
فکر می‌کنم عدم مطالعه دقیق در این بخش‌ها باعث شده مطالبی تعجب‌آور از سوی این عزیزمان مطرح شود. مجمع عمومی فدراسیون فوتبال دارای اساسنامه، دستور کار، اختیارات و تشکیلات مشخص است و طبیعی است که اجازه دخالت به فدراسیون کشتی نمی‌دهد.
🎙
برگزاری این تعداد مسابقه، امری خاص است که به سازماندهی، امکانات، بودجه و سخت‌افزار نیاز دارد. برای این ۴۰۰ هزار مسابقه باید ۴۰۰ هزار کوبل داوری اعزام کنیم که اصلاً موضوع ساده‌ای نیست. در کنار آن، بحث امنیت، پزشکی و بسیاری از موارد دیگر را نیز باید در نظر بگیریم.
🎙
این کارها نه دوستانه است و نه خصمانه. نمی‌دانیم باید اسمش را چه بگذاریم. ان‌شاءالله این‌گونه نباشد و هرکس سرش در کار خودش باشد و موضوعات مربوط به خود را پیگیری کند.
📺
دبیر امروز گفته بود: نظام باید یکبار در مورد فوتبال تصمیم بگیرد! دولت، مجلس و‌ وزارت ورزش دارند برای فوتبال هزینه می‌کنند؛ باید ببینند از فوتبال چه می‌خواهند.
@Sportfars</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464573" target="_blank">📅 19:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e665a077a.mp4?token=d2xG4jLgGb5uIC4ptimEt8ZNwAlLEjS3Qsl3-goe8kJDwrcZ6FnUU8bEf_S8jKeWA4M7JjFBnz_907R9dUbX75E7B4BiMPS0NgKE98ERlWQrN9W1zXnJok9iOm4lOHBqxjyOG-2VoVelbmqwpa_1E-tjna8z808IAQSH1MaEM6RWEqBKb9xCXKCNcF9X_5tGokUVh_AEGbNTQVCk6_LyUQBw_f1deOPxLFezdgeCiTCnkLoFqwBmvZlSPVX-DcYMclF80xThZH5vvwcx7VqC_GcUF43o6qX6XCramUktW6DmBFOyiuV8P9abrbDZT1fGk55SKsBTCnE_1xC7Mfz62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e665a077a.mp4?token=d2xG4jLgGb5uIC4ptimEt8ZNwAlLEjS3Qsl3-goe8kJDwrcZ6FnUU8bEf_S8jKeWA4M7JjFBnz_907R9dUbX75E7B4BiMPS0NgKE98ERlWQrN9W1zXnJok9iOm4lOHBqxjyOG-2VoVelbmqwpa_1E-tjna8z808IAQSH1MaEM6RWEqBKb9xCXKCNcF9X_5tGokUVh_AEGbNTQVCk6_LyUQBw_f1deOPxLFezdgeCiTCnkLoFqwBmvZlSPVX-DcYMclF80xThZH5vvwcx7VqC_GcUF43o6qX6XCramUktW6DmBFOyiuV8P9abrbDZT1fGk55SKsBTCnE_1xC7Mfz62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: طبق برآوردها حدود ۱۵۰۰ مگاوات ماینر غیرمجاز در کشور فعال است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464572" target="_blank">📅 19:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlwFai9zHjnkc2iZTXAbQzk3GH9SLDRLNYf5e9_7IlGec1t9nrAnUmGcHGQ20vgGsxyu_E5WvqH4ZsnDKi8goXwBGAInlq1Pr7qu3HsquDvu1cVNRcOJmcKLfa56GXaXT5R7iAezj6wmprG3bQ8TxSNZqX_CKnK2OSVGW4pFXhSLddVoHXfXmuToso8YE1CHTEmlX5KmdjNe6IAZcL0SoBtZEazfwWX6yX6-6AhT23lkY15RMT0h_9x4uUuXzxXnSsZ0V69rG0mb_aaSl_uuVVjDr671S0JE8YFUOL5f1SZ_ibeTCLpGnWraIx18uhs9FS6qEh1zH4k4oIYaeXtzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واردات سامسونگ و ال‌جی آزاد شد
🔹
سازمان توسعه تجارت ایران در نامه‌ای به گمرک اعلام کرد: با توجه به تصمیمات کارگروه ساماندهی مبادلات مرزی، واردات لوازم خانگی از مبدأ کره جنوبی دیگر با هیچ محدودیتی مواجه نیست.
🔸
با وجود آنکه تولیدکنندگان لوازم خانگی کره‌ای پس از برجام بازار ایران را ترک کردند، اکنون مسیر واردات این محصولات دوباره باز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/464571" target="_blank">📅 18:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9u6y2k3rYrUSa5YokufOO4IzPeKda3K9ZJdAAz-L5vZcLd7-MZMhH73pNUyUNhcD2VBb9CeXTQCbtzAyoPpRpfWA_w67MduoSDkiDd_osmoYcPdU-HaDcNBtVL8MbPviYygFrtUfWZhZ-eNdA5oS-Y2WbhyN7ij-xiErU0Y2JipCR3PjbrAIB0In8SoO_SDPsISrjs9F9kTkT_osjYSMLEFT7c2NCPtm8r6fves3fNqpw6zasEbYNyn40ylvEZTfkqVgJSBTRXbQTH68r0HtahxDJh74u5Wqm_qDzclLPQMnSRh5m6tNeqRBPxBsv4MRSvQOjxERQYCuRDD3eQvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولاد اوکراین به خاکستر نشست
🔹
کارخانۀ فولاد آرسلور میتال اوکراین  هفتۀ گذشته هدف یک حمله موشکی روسیه قرار گرفت. این چهارمین حمله به این کارخانه در پنج هفته گذشته بود.
🔹
بزرگ‌ترین تولیدکنندۀ فولاد اوکراین حالا اعلام کرده است که تولید در این کارخانه را از سر نخواهد گرفت. این شرکت به دولت اوکراین اطلاع داد که ادامۀ کار در این کارخانه دیگر به شکلی ایمن و پایدار ممکن نیست.
🔸
بخش فولاد اوکراین یکی از قوی‌ترین بخش‌های اقتصاد این کشور است و پیش‌تر حدود ۱۵ درصد صادرات اوکراین را تشکیل می‌داد. این بخش حالا هم از حملات روسیه و هم از محدودیت‌های تجاری اروپا فشار می‌بیند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464570" target="_blank">📅 18:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-q_tp2rBXWQIORe6zC3XNOF5s4h_8y9WyMrgffrzoKK7O-tYpRT15huU5S0IbkPOz-Qpj2KuljLWxU1N4cawcERMSeDhddm1G64Urj0m1YElt9tQeVEk1UxFmB1IIePjm5UGP_SYvoOQGTSTbNtf72YrT7fqUzdPb6VJMEUpN_Z5BVOZlloz-i6R0j7EoiRnyd-JmossSAeLEo0FXW_ch30iIxZ-QlSBHHqZJQpX7UjmXqX1gl33DbCeaHC21hIIVAouDH5nhZN95G7D7L_CeTrmyPXP8kI1sm3XbOIPxvPPxPVx5fnwo2DeCwI0-GBcUb5SlkPE9xuqKZ8Gb8o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYUCOKFH8c3tRS9IV2Azbn2GXj2TQ8wnu71tiJl0wFO-zTTd8RQP646mSATDWGZWYlqF_GltyVoFAO5A1ybvbWUBhpI9-gnKoDiQGg7DUOrtIKffprFhoK8tWuHtmaeI2EcYCfTm7nup2RWe22-y9-evngmfGI-BTNCYi9NrevgWwCpQwybcCHv2ZPT4p9efX-FktMNvnX92m0CgRkbXigZnW5HtoOQp2dtIcnAQzKkQToLhYUC6NmYdhyKRwPl4cD0NwWiKWeRNbbYqO92e-iIKyFyXbfKmy1d6UJew4SYoeNf5CVCaG3jeOvSc27amLgflaXxkk-Cf4jNUzbUgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6AYRBQRCGTpmSWDwozjPJcIM9Sz1dYK8Xd_ClZn63oyxt7334n_T0pE1QrEMN1gtme-FWW0vOE2JhRMDdsu1JG03E2dl5NXSWJqK4rRxUanevwKr4zMN86d0hnDCxquaHM7OP_eoLKb4ToxEOQHDl-fxIPRNRzKKH62ofJdyCqH9Dlk2vBWn_O-pD20yVzxRnyhuoqAhTUQm-gUusZEm0z1PNTje03pO-5g5W-OoSFcA4hz8ACGW3ZKO7TlgbGFU8SNfX-3xGs21hf-PX_MufzhvGqCzmA5h1bmyMIzbouwLT6M6VDtHLK7cqhbdFAco78dVLw3iE1RtWai8lqOuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عراقچی در ادامۀ سفر به نیویورک با وزرای خارجه مالزی، کامبوج و الجزایر دیدار و گفت‌وگو کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464567" target="_blank">📅 18:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MffYploIMrUBcLeR8ALwZTuPxn6laSgzdOiqSvyR5mXyTJPcG87PS65BcldFCDLIYIGIlkhJ0r-VsHTll9mhsQRVJ7MHTjIIMs3vNVJniShIa5pUCjCzhO_1gRbAQ7xVJgppN8FwMM4KzNZ1C-_ocMjtLHY8glcskDgJFsAFHdIt2GDZ7hkEw4Q3N391rNJjR7AaqkocxDLLDnpGJAc__I67Hkm4BiqidBs58rMCQwUeP8NJ9spAa3Cw-_dBS20vw6txMSVQecZD2jEBpHimwnMBrEwkO5_PBGSsOfXlQs2FY_Gts-OXxxVgiLejhlBp-Msbl7B0R_Ggz7PVVCFlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار لاوروف و وزیر خارجه آلمان پس از ۱۶۵۰ روز
🔹
سخنگوی وزارت خارجه روسیه: سرگئی لاوروف وزیر خارجه به درخواست برلین در حاشیۀ مجمع عمومی سازمان ملل با وزیر خارجه آلمان دیدار خواهد کرد.
🔹
این نخستین دیدار میان مقام‌های ارشد دیپلماتیک روسیه و آلمان طی بیش از چهار سال و نیم گذشته خواهد بود.
🔸
روابط مسکو و برلین طی سال‌های اخیر با تنش‌های گسترده‌ای مواجه بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464566" target="_blank">📅 18:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464565">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9lmL9crkeC6E5CXMStF_jkHR7o4AYMI0-I34L7hN41SF9RcqoD5rZjeJ6HEobErvaxv7HcvE6UHdkoiQTML5Ok7c-y1aYhaxK_BWWAdEm6_woitELjAfsvzKrp1cH7F98z4YDq97Y-2H9UnLoWp-BPo8N3FhdqkKqQ17kd7Drfu34h87Arc3h93jq4USfrVlCIyDk9XMU4hjkMPNY4lONi2KvqrDiSfUCF_Q8dUzt_HbSiK9QRoDya3IN3v39Z2BLrfSOqkaK-2LnEf8Za3H0BJQg4TS8o_l64ZQsRz2FgIW2d41Tt-C_Sq9YiHOFCT6ZkQRBMo6r7fJ5ZOs-PLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح: آمریکا و اسرائیل خطا کنند، ضربات قوی‌تر در انتظارشان است
🔹
سردار شکارچی: اگر آمریکا و رژیم صهیونیستی بار دیگر دچار خطای محاسباتی شوند، ضربات ما این بار سنگین‌تر، وسیع‌تر و دقیق‌تر از قبل خواهد بود.
🔹
نیروهای مسلح مقتدر کشور در آمادگی صددرصدی قرار دارند و از دوران جنگ‌های تحمیلی دوم و سوم نیز قوی‌تر هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/464565" target="_blank">📅 18:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464564">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBJvHbkb-CF1rounlRmlb0WZEpKX-TBTEH4hwLUCphcjBsmoptKtZHTlh2DrfKg0sfnvBVJsm3pgCPlFyEiDLHBKjyAdEFFLuRTAOzZFreRPrScY1ZpTryjOIWs6KIy9Cjvx1YXgWvlaCzrgb2bCd0qZOCSc-aVXw4McRx2hmfVNfRCrzbFx5H4MGg1p7sMeyxZB0DfwELDxzr0wE0q0x2vQfyq1nVbJAsiJp8RykCeVoDi4H2mHV-k-cRQetMo2Ral_GJt4L13Ek7HZ__WX1NrAYWVHT7G-j7gCJY7icRe2_4j-3v4Mxt7bjikdM7Y2bhti9SKiZEA9haCulmARJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرعامل تراکتور: با پیگیری ما معافیت بیرانوند یک ماه تمدید شد
🔹
بدون اینکه بیرانوند خودش به نظام وظیفه برود برای او دفترچه صادر کرده بودند که این غیر قانونی است. همه به بیرانوند گیر داده‌اند، مشکلات دیگر ورزش را پیگیری کنید.  @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/464564" target="_blank">📅 18:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464563">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5713c7e246.mp4?token=AIGvTytFTAb4gf1b9w2T3bgDkZHMPtOf0kf6LabPR_aTXbU8-DrVCzNjvj2oq-8jTg7rulgasfo3ZZduLSe4BE6k9aVaNiGIfJ06Qetqmgt9uHl3h7fKs2We55RPI5iRNLzNPX4Zzf7QTp86RCe5phfxEpLbHI26JsrWXZyiJ0U5z74dIzIESSstApeK5NW5XDidqRGiV6VMCr8O00xeqLpBVJGp5oHNyEi67HXGbgdhuD0hDklT0eBMCddkGrUNoAwTWIaNmO3OxB2DrPw5rOobD43_2H0NPIDcTRP8d5JzbbtVwYQyCZo_3N2WrDasCFCD8wjRk0R7hX5MfEwwwpXjKHkvY04ZX4r-EuNXwnkKxA1lRY4OgHsJdIBnSJKDiM7Q15u98iiSB-8GsEI0nqahAIseSKH6yafSDElomq1AosbHZW1sZCCWlBoaVbNtXRfqtNv9nDX61F9bRa2LK2zDAOXBtw7F_IT_4NdIEp_3sGNZ3RFwzT25J9LiD59Nim7A2vs-qWBajP9ZBDwCrciugDpJLs0Xhq8E_dv3uApnObgtUMjUIQJ0nLB_34NT3IvmANmFEdN3VCtLJnAM1MIK7tw2ITGdtslpkk183Tf3mTv46YsrYBdWHnw0MAk2gWOoxpbYaFbbyzbQnBveU1qattjLGzT-y5nXUKCk6XM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5713c7e246.mp4?token=AIGvTytFTAb4gf1b9w2T3bgDkZHMPtOf0kf6LabPR_aTXbU8-DrVCzNjvj2oq-8jTg7rulgasfo3ZZduLSe4BE6k9aVaNiGIfJ06Qetqmgt9uHl3h7fKs2We55RPI5iRNLzNPX4Zzf7QTp86RCe5phfxEpLbHI26JsrWXZyiJ0U5z74dIzIESSstApeK5NW5XDidqRGiV6VMCr8O00xeqLpBVJGp5oHNyEi67HXGbgdhuD0hDklT0eBMCddkGrUNoAwTWIaNmO3OxB2DrPw5rOobD43_2H0NPIDcTRP8d5JzbbtVwYQyCZo_3N2WrDasCFCD8wjRk0R7hX5MfEwwwpXjKHkvY04ZX4r-EuNXwnkKxA1lRY4OgHsJdIBnSJKDiM7Q15u98iiSB-8GsEI0nqahAIseSKH6yafSDElomq1AosbHZW1sZCCWlBoaVbNtXRfqtNv9nDX61F9bRa2LK2zDAOXBtw7F_IT_4NdIEp_3sGNZ3RFwzT25J9LiD59Nim7A2vs-qWBajP9ZBDwCrciugDpJLs0Xhq8E_dv3uApnObgtUMjUIQJ0nLB_34NT3IvmANmFEdN3VCtLJnAM1MIK7tw2ITGdtslpkk183Tf3mTv46YsrYBdWHnw0MAk2gWOoxpbYaFbbyzbQnBveU1qattjLGzT-y5nXUKCk6XM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنگ آغاز کلاس در سرپل‌ذهاب به یاد شهید «رضا فلاحی» نواخته شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/464563" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464562">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVJwMo8tMhII9JzmiOkBFMvo4uPF3jhLDPVYRVECdvbocAXDM8bKNsElpikeZPoBfByBaG52Z6d6bNOBLOdfsnQG38jKjhN3vh8w3KeBvGEJl6itsp9_WAVNO5o4UVy1hakwRxmGHPs6CWaD1GeFAZC0THOF1DZNHSE6zaDp57eH-UsZYQybLyVvTN-dQ8wDnGBmO68IMJ09bNWURxC3hqvs6pumsL6HFs20q3AE3HOHvMKWNNo1JqAGHgLN96esSGWZCc-MCCg-AAye1WD7DhDqQtQt36n9fAi52L9sPymM5deMq5UpOutrouQyUk-n4zGiPVhVwMExZyBvc7q7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان بدر: دولت عراق باید از تصمیم لغو پروازهای ایران عقب‌نشینی کند
🔹
هادی عامری در میدان تحریر بغداد: ما تحریم‌های آمریکا علیه جمهوری اسلامی ایران و تصمیم ناعادلانۀ لغو پروازهای ایرانی را محکوم می‌کنیم.
🔹
دولت باید به خواست مردم عراق توجه کند و از…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464562" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464561">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH9hiN5Ve0hNqTNAjqL4a3qdh-_omWC4I0Ki_6Rc1BZx-TZCOde3OXe4B4HdwJDjJlCL381OPsGKKYdH5rw0iSJ574ysiM3znm2nSEdo5TvEARaCl8OJpWVHk7jS9KsXuJTtkEWwie9bMC3HSu6xfp1lPJP67QzZIyR4pjtwqHY8y9T5vopIJcJJoHmisrBcgc4tFK2ozhTOQ72QyGvi3DM7d-NWh5wLklWlWz1UHxuI-30FTYNzuBLtLKPzc113PKuiBJEKhZLrs8-sVbSyJrJQRLFqBDruPa0GAq4K2EuFFVPt6zk2EN-GUPFj-4sNZC3JWsKoI_H4b6g5Qjnm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
رئیس‌جمهور آمریکا اعلام کرد که پیشنهاد ارائه شده توسط ایران را که به موجب آن، تنگه هرمز ظرف مدت هفت روز، باز می‌شد، رد کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/464561" target="_blank">📅 17:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464560">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qawJs0BfBIoHBAJcEfZOKiO06tM3_LX1cMHM6tmjllZH8V6VgRg_65flWv_upf_xGPcbVEKrme0EUAJumy6vrhNjKMAi21ZwJTTtqUhSelG79RsqAr1KCJqRBt8xdvIj8EXMw2QQ78EvIkjikQL9Y1hJ4lgPeQiQFKdUtufPI287qjvAjqj4jrS2Kqfrvg7Fk8_qUToPD5XcqyNG0N38NqBL8uSBBiV4FjfleieGmOGtl3-2K6TZyZ1ZWV6GTZeN8M6Yt78Da1o7MKOB-zCJuM83ARytRKsKEfzdS9Ri2EK3Ak-Ek1aT5iuMUNKNWmyvvPFtb6DQZ0NlUjC_DIVgaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مردم عراق در اعتراض به لغو پروازهای ایران در بغداد و بصره تجمع کردند  @Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/464560" target="_blank">📅 17:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464558">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbbfabdbe.mp4?token=psiYwri9pDlsx9rrmlumF67y3ctHf-aNBSjPKS8Lf2JPs-M8f3oOBMx2F-I0oDf4-OaMDDiwbymmAzK_KARJNLhb7LSV-COeXThkp5OzjHFgV2eY4UWKvMm0ZzHMOrYt3C8P9G8LOhEEBJBFB1Ug7Mfoif_gMN-_pV8bB8ZADvyxHeFjLr4ZkUqaEo7UZxt3ySkeW358naO6Erxn_AcNkbg97anhK8kTAPs4jEnTjGHnIIlG9EESK6R_fUAxVXG_QLcJ0bKk2RRbjrYuEsMXUUapGTcbevsJsvTT0gVKiV9i99b076YekMHzQISvsQDWSPe68HulqbwDgKSqEAc4XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbbfabdbe.mp4?token=psiYwri9pDlsx9rrmlumF67y3ctHf-aNBSjPKS8Lf2JPs-M8f3oOBMx2F-I0oDf4-OaMDDiwbymmAzK_KARJNLhb7LSV-COeXThkp5OzjHFgV2eY4UWKvMm0ZzHMOrYt3C8P9G8LOhEEBJBFB1Ug7Mfoif_gMN-_pV8bB8ZADvyxHeFjLr4ZkUqaEo7UZxt3ySkeW358naO6Erxn_AcNkbg97anhK8kTAPs4jEnTjGHnIIlG9EESK6R_fUAxVXG_QLcJ0bKk2RRbjrYuEsMXUUapGTcbevsJsvTT0gVKiV9i99b076YekMHzQISvsQDWSPe68HulqbwDgKSqEAc4XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراض عراقی‌ها به توقف پروازهای ایران بالا گرفت
🔹
«پروازهای ایران را برگردانید.» این مطالبه حالا از بصره تا سلیمانیه شنیده می‌شود. توقف پروازهای ایران به عراق با اعتراض‌هایی در میان مردم، علما، نمایندگان مجلس و چهره‌های سیاسی عراقی همراه شده است؛ تا جایی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464558" target="_blank">📅 17:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uihVaywxY1OSstP2-JA-SQAt8Ltwf0N4ZT3Apa--MNKrhHkUMAPTuiNQyq6rHT_RhDg9H2utYnL702FuyRHr27tCD_E2VovJE6WEB6TjKRmDI9wHJ7ubeRd3y5yaY3L4iaDBuSxIUpBQ9iLrSV6Lbb6zs0F-JGlar_DeuGglu_TWLVcjAeBEaqXGC5U33uACu8NEqZzFX8ShNS1l5Ja6sEMWvwpurOzi6i6UXOtRVwXk4vkzOLlZoLjpAgJpB5Q6OM06ZFI1aEZvZZppPSDVhf72SuDqK8nrRHkCtzeazepMvgeN5aHrRRMB3yB87aLeKjmhkyO62jBFFA8RNrY2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewk_VBQIVDEr-AZfbFs9uFeLmm22p4YvQYHdf-dYMLlYS_Sp1V7ltPuzfRwe7Pp3C0lUPEWRA3G6RkPb-3E1_9gk2yazxSVWKNHphEBxwQAfQaqSBEZpckz6BZkko4dGV3abX_6pEPdWapXRcIz48Rv-Xugt0aOVQilmM0zUbHcHrl88lXYfxB4azbn3ZENsZjJfB2QQMZ0_SB1soLyBw4T-qLzlUagAzfBTnbLeVefiC2WoW4qen1DOJbYRJ5RwpEtUhSBLz6OZkhIBLQeXh9rJkeS2hvzst-mRoVcE-oTRkH_DOhzqrMJqQHoWTA476p6eKTVuE4IbHlMVScFHIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcgQtmMBF-tfH566NR8kDyEsYp02J-m8BkyfJ-o09z7gCs8E-cNtH86M3J1HIrH5bre56V2dXWfDZB6QJ46_pQ0rYLvprCoO5DI3HiWZ6-C4CDG0loHVtAw1imYr3KN44H7jiDLaqbvXyTrs4HuuhawgjyYmpz71jUuWwSNdRmcb16jPU_ohrbjNSQJ6GcVWT5xz_1UY1zxY_-VDxKgBK7SfnUsyZBHgjCLD6uRINXrlYdDqQuvWBnobBGplWNRLjK10AZWzzYdpgPvnkDM25GFkmM9neLMLDCUJ1LQVkr6AMX_EMg7C7Tb1PKmBrjf70GuwQDjbNJfG1rVHbwSpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNxrjRAdXRARGKPNZU7eLHONYFKTDnAaWa5gt6wVn4lpgBaSz364LYh1fHQzJEfj5f9WJqNt6VNepVmY_nzuWrLwVMP-wnULdu-gygNRRTWjgq_aQIW4YsFXdf7iWCQnF3RCRfGoZanSSl5NKzB6soo1WZkLwR1eyNu-qgwMLsrf9q9aJicicDqSyammOPehCT9EsBXPx8p-y1gapYhan9Ppx96WYhmM_VCK71LSDK5CwqGNAgWmw8TrP7XI3e7_DrWXbUmIgX6xgG1mvgZ5KhrtWrFJjvLC29rUqJwEAVQuA6XPyCA2Qb9oPzk7-ydpZ-qts6sujnf3_lq9lLy5bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqfVTvQ7rbBiGNr2TyYHbmGC9Qy8V4PksrFOqdrhn2YGEFWbX8MGPWHX7hVW8cPFpxnhYpFEbIK988NAjtoK6aH9zmC6J8SqNywn2lDD8gKAr5QLM-H_4mnvLMBwqg0VB7L9HQuXWxp8Cv6_DroTOzEgFFymIi5r-mojOAAv36WPZ8ulyYEB1EdJouveuwPr2SSFYB_u05cUP4NRpLCIzEqjjloaSSVQyurcaDN3MsaOpKkcRm-WypSXqvBUFnbhl0ZJKDTYYNZhAVBBdayIFTOELeQgvRdhHdVngT58PNVY3-9icWMUU2Pmdu2XCR5qypOTW1Oe7MJe1A17o-XYzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنواره فرهنگی ورزشی جام ستارخان آذربایجان‌شرقی
عکس:
مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/464553" target="_blank">📅 17:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3deb1c68.mp4?token=JxSR1y3VZ1B7Hj3LsmM8D7kjyMSLpitpXTnEzbhCAk6-WzUNv5mMSmCbtDVrznZbYZMBYUaF_2JCX6CAnYOp3CgSXAalLvPihCoDj0CvpzqzP1zftbi8C0z6AxRoSG_TLOgoGfll5753KQLqYxILlzAaEIoGOru4zLr3cGiBTSR4RBeiwp0TnOWioYH4CkBf9tnCzMWjyGTJ27xva0ugAFNax6RQc-LekhJgdYlW_WJcrZxtA2A0c-8GWvVDIcmsmiAZv3bXsg3z-_2BEaGkMhOEhdoADZOjzDOBK7hPXz-c7ehy9uc4vQTtwgqEwvofHF0AUAGgVAxy0uffU5OxJWz54kgPYsDmakt7UuAlCzL0L0AswvRbpYguAbtQIhZRRKe9eyOxwwNKgwh3W6oyjqiFwSkdXpuBjAiMCgEgWOGHx-XEOyJ78H95fWR2XEnHui5fkkJWFKEFgde2dZxGwwnyZE3XxK32a_LyyENRLpZJOPSYoo-nY1iUCKk8X4aItkhk8aYy-c59GtPcaJKM2w88ufmjeaIIrkrjsQO7PKGnT6vUjShxaS6ZenQ0J5d5sv_8rO29hHhSD_uz2xANmFwe3Ong74-DE0oSIghC3mrrIwykrxXCAYM-GxvXWLmwvnUYX_1y7jJPgTG6Thi67jSMPw5CDTItgabVkRtpcpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3deb1c68.mp4?token=JxSR1y3VZ1B7Hj3LsmM8D7kjyMSLpitpXTnEzbhCAk6-WzUNv5mMSmCbtDVrznZbYZMBYUaF_2JCX6CAnYOp3CgSXAalLvPihCoDj0CvpzqzP1zftbi8C0z6AxRoSG_TLOgoGfll5753KQLqYxILlzAaEIoGOru4zLr3cGiBTSR4RBeiwp0TnOWioYH4CkBf9tnCzMWjyGTJ27xva0ugAFNax6RQc-LekhJgdYlW_WJcrZxtA2A0c-8GWvVDIcmsmiAZv3bXsg3z-_2BEaGkMhOEhdoADZOjzDOBK7hPXz-c7ehy9uc4vQTtwgqEwvofHF0AUAGgVAxy0uffU5OxJWz54kgPYsDmakt7UuAlCzL0L0AswvRbpYguAbtQIhZRRKe9eyOxwwNKgwh3W6oyjqiFwSkdXpuBjAiMCgEgWOGHx-XEOyJ78H95fWR2XEnHui5fkkJWFKEFgde2dZxGwwnyZE3XxK32a_LyyENRLpZJOPSYoo-nY1iUCKk8X4aItkhk8aYy-c59GtPcaJKM2w88ufmjeaIIrkrjsQO7PKGnT6vUjShxaS6ZenQ0J5d5sv_8rO29hHhSD_uz2xANmFwe3Ong74-DE0oSIghC3mrrIwykrxXCAYM-GxvXWLmwvnUYX_1y7jJPgTG6Thi67jSMPw5CDTItgabVkRtpcpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بلایی که موشک‌های یمنی بر سر کشتی‌ها و تجهیزات مزدوران سعودی آورده‌اند   @Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/464552" target="_blank">📅 16:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464550">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bc4eec4b.mp4?token=NEoQJCZnfLvdlN6a28-tEOak6sZlQ-zZv3qlrgG-ScVWg8j2ar4FW14LoIl9ixrbpRYiQoOLkiFbjFPf97aLc3NKf8madXiq10cWcZV1zEmPvHX5bb-6fuWv_GrVgw5aVpxg9oNeWwk7LjB9umkvQYV9qtwTag_nhU2biEL-rQL_Lh4wYUIoQL-dE5X3ePZpvKnhRm0SPib1ryEjo2TCgATBagU2WPuAtANoyxntayMM_--VOjHyq1LaPOCLora0FOsk--TaXKUifPxzFWj6tve29j9mnXqmXja0nn4WL5nd4JEADs46PvEnVFkfbNxa1qiycvU2AXeDJTZs0W7Ydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bc4eec4b.mp4?token=NEoQJCZnfLvdlN6a28-tEOak6sZlQ-zZv3qlrgG-ScVWg8j2ar4FW14LoIl9ixrbpRYiQoOLkiFbjFPf97aLc3NKf8madXiq10cWcZV1zEmPvHX5bb-6fuWv_GrVgw5aVpxg9oNeWwk7LjB9umkvQYV9qtwTag_nhU2biEL-rQL_Lh4wYUIoQL-dE5X3ePZpvKnhRm0SPib1ryEjo2TCgATBagU2WPuAtANoyxntayMM_--VOjHyq1LaPOCLora0FOsk--TaXKUifPxzFWj6tve29j9mnXqmXja0nn4WL5nd4JEADs46PvEnVFkfbNxa1qiycvU2AXeDJTZs0W7Ydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زارعی فینالیست دوی ۴۰۰ متر شد
🔹
زهرا زارعی در مرحلهٔ مقدماتی دوی ۴۰۰ متر بازی‌های آسیایی ناگویا در گروه سوم با ثبت زمان ۵۲:۰۰ ثانیه به مقام نخست رسید و راهی فینال شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464550" target="_blank">📅 16:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464549">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXW2XOA7FUiN64-blK_DNbyFaEt3KwWZI0JzdHlixbR2tWTWjeVZsOWhVW4j-yMBjorX6lfYPhXhYiu1MIfvCAeDjQmyTKpeo8xEUmgPx44ez_l2fO4tsRrr3zL-zX5bgFX3LvaXAeugsSHBytAhzCGeoZyQo93KRltjo5smXFtwkoQuiBMHH1Ic1XYpW8YnSpIjIrk2iKa0v9xfc_NQD-Q_uCG0LnwuE6jQQ2qSCoxmUtjEKwa8zLIZiVB8c18r-bGHdEDJIX876AQDdTbB5ge1K0kZPnkajAZesYsXPt2SWZgHSOBjB3fF2HfnPi7wxfpkf86jwzOe9PiAqn5M7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا و چین برای مهار بحران‌های هوش مصنوعی دست به کار شدند
🔹
در بیانیه دیروز کاخ سفید، یک بند کوتاه در میان توافق‌های اقتصادی و سیاسی نشست ترامپ و شی جین‌پینگ از توافق مهمی خبر داد: آمریکا و چین یک کانال ارتباطی دوجانبه برای حوادث هوش مصنوعی ایجاد خواهند کرد.
🔹
در همان سند، دو طرف همچنین ایجاد «گفت‌وگوی ابرهوش» را برای تبادل دیدگاه درباره مزایا و خطرات این فناوری اعلام کردند و مقرر شد دور بعدی این گفت‌وگو تا نوامبر ۲۰۲۶ برگزار شود.
🔹
ریشه این توافق به مذاکرات ۲۰ سپتامبر در نیویورک بازمی‌گردد؛ زمانی که اسکات بسنت، وزیر خزانه‌داری آمریکا، و هی لیفنگ، معاون نخست‌وزیر چین، درباره ایجاد سازوکاری برای اطلاع‌رسانی حوادث هوش مصنوعی گفت‌وگو کردند.
🔹
در آن مرحله، موضوعاتی مانند عامل‌های غیرقابل‌کنترل، حملات سایبری، استفاده تسلیحاتی از هوش مصنوعی و حفاظت از زیرساخت‌های حیاتی در میان خطرات مورد بررسی قرار گرفته بود.
🔹
بنابراین کانال جدید از ابتدا صرفاً برای خطاهای نرم‌افزاری روزمره طراحی نشده بود؛ بحث از حوادثی آغاز شد که توانایی تبدیل‌شدن به بحران میان دو کشور را دارند.
🔹
هنوز مشخص نیست این کانال چه زمانی عملیاتی می‌شود، چه نهادهایی در دو طرف مسئول پاسخ خواهند بود، چه نوع حوادثی مشمول اعلام خواهند شد و آیا داده‌های فنی نیز میان دو کشور مبادله می‌شود.
🔹
پاسخ به همین جزئیات تعیین می‌کند که این ابتکار صرفاً یک تعهد سیاسی باقی بماند یا به نخستین سازوکار واقعی مدیریت بحران در عصر عامل‌های خودمختار تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464549" target="_blank">📅 16:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464548">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttgxC0C5RszHy_4eK9FI1NTqfFotr3Yl8moAjA4JIZ8VcMMK_aWhZe_fvea4WjT5xUerE3qq6ecR0d6AK1ACeZpGpGxWsYsT7nWubxp8sfkllI6xgVOH_eIgPeXaVPBtZg58OP7YH4NjLNKrJoW_3NSLQF7EfhSiMvHWeGORB0ip0ggocv2sBzCOxeyL5pyCGwW6AjEzWJy2x22aCOaqry7mu-GlrDirsXLHcSDkIrhGLqjHrRk0NJEhjOiXcrg3r99Te9zhQERh-FdYeeweFLOKFhxy1cpzoov_gyCDhX5JGMVriO374TAafDieNX6CEVLuR2aM2Vvfgh2Gy_089A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیۀ دبیرخانۀ شورای‌عالی امنیت ملی دربارۀ برخی اخبار خلاف واقع در‌ موضوع حمل‌ونقل هوایی
🔹
انتشار برخی تفاسیر و نقل قول‌های خلاف واقع از سخنان دبیر شورای عالی امنیت ملی درباره موضوع حمل‌ونقل هوایی، موجب طرح سوالات و ابهاماتی گردیده است که بدین وسیله اعلام می‌دارد:
🔹
۱. ادعای اینکه ایران در مقابل محدودیت‌های هوایی اخیر دست به مقابله به‌مثل نظامی می‌زند، تکذیب می‌شود.
🔹
۲. مذاکرات میان ایران با کشور‌های مربوطه برای رفع برخی محدودیت‌های هواییِ غیرقانونی ایجاد شده، با جدیت درحال انجام و پیگیری است.
🔹
۳. راهکارهای غیرنظامی متعددی برای مقابله به‌مثل وجود دارد که در‌ صورت ضرورت، برای برخی از فرودگاه‌ها اعمال خواهد شد و البته امیدواریم که مسئله به این نقطه نیز منجر نشود.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/464548" target="_blank">📅 16:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464547">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTsJvL_TyMt_SNSjxmTvXBW3C6AGfQ7rOhyZgENVa_V95h5GQ5-oISgL-muWz5ufcQRsKuc_11fwFDtbGGwEV0k7vNSsfrLQJeGFWPI4oQ6n6JUeQz3BYaj5dTxg6IA6of-YOEpmxwYARhZmz7E2iYYKppypk4cSWJCxWHiUdRvpLOvQn_42xFyfFpsxDd69LnA7Oh5NearBBQdXW7RcXqtL3O0EPDKjZE5HJq8m8igVS9WDxu0pgx2pLYUh6yDNI_GW3JemtK0vO1m5iGysZw64IsUZY7t-SWXntz2OF3P3eLckQPUYoJ5CKauJ7g1TbQXZIraihTkovoqaqgqMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: من انگیزه‌‌ای برای شرکت در مراسم روز ملی عربستان نداشتم اما از سوی مقامات ذی‌صلاح سیاست خارجی به من ابلاغ شد که در مراسم شرکت کنم
🔹
من در آن‌جا حملات آمریکا از خاک عربستان به ایران را محکوم کردم.  @Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/464547" target="_blank">📅 16:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464546">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI8Lah2ch6PUOMtmKV1fdDHuden1VEYU0zjCfYnfY_sGsoooaynQjbaKVX-1B7IEHgDSzmWnF77Qej7MmGi_cNHXV0VG5DykvUH8Av4-zw0DXVr0vA-U3WerNx0Jsf_yJJJC6UJbsmPfoHbHT1rcWxK8ORxJ7f1-o8WGb57Ah1VutWvwW3GDfRwN1QpDCQv-iLLsmEYw-jJDbtFcbldyGXJpeh45tTf5yvcgSAizRu1szg6gRaAXblXav5BzZ7IjsIw0-u4ibhnh5cz9jnuDpyaZDK6EWmx1ibqQ80eHBLUEl8bt0exLunep414LNBUlhQU5Q7GMZWdM0TqyR50y7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رودخانهٔ اتمسفری در راه ایران
🔹
نقشه‌های جدید پیش‌بینی هواشناسی از احتمال شکل‌گیری یک کریدور گسترده انتقال رطوبت در اواخر هفتهٔ آینده خبر می‌دهند؛ جریانی که می‌تواند رطوبت را از شمال آفریقا و شرق مدیترانه به‌سمت خاورمیانه، ایران و آسیای مرکزی منتقل کند.
🔹
این نوار انتقال بخار آب در صورت تثبیت الگوی فعلی می‌تواند شرایط را برای افزایش رطوبت و شکل‌گیری بارش در بخش‌هایی از مسیر فراهم کند.
🔹
با این حال، زمان دقیق، گستره و شدت این سامانه هنوز قطعی نیست و به روزهای نزدیک‌تر و خروجی‌های جدید مدل‌های هواشناسی بستگی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/464546" target="_blank">📅 16:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464545">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آغاز عملیات ۱۰ روزهٔ خنثی‌سازی مهمات در خارگ
🔹
بخشدار ویژهٔ جزیره خارگ: عملیات خنثی‌سازی مهمات عمل‌نکرده از امروز به‌مدت ۱۰ روز در جزیره انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/464545" target="_blank">📅 16:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464544">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پروازها به ترکیه همچنان ادامه دارد
🔹
با وجود تحریم‌های جدید آمریکا علیه صنعت هوایی ایران، ۵ شرکت هوایی قشم‌ایر، ایرا‌ن‌ایرتور، سروش‌ایر، آتا و تابا با واگذاری خدمات فرودگاهی به یک شرکت ترکیه‌ای پروازهای خود به این کشور را انجام می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464544" target="_blank">📅 15:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464543">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc4f2efeb.mp4?token=WQhsRvJGZXJP9byVFx2RR4C7fo6ondjjz6nAb6cmozlzg2jlws-6PzG0dReP_HMrL_B5uamtnZqngQUbadBUVH_bv_wi9xnZI1XXZ6zR5D2yt2LUXZyaaYDOdHzzJOmL1DgvRLQUGKNax2tiLi22Nlb1iMT7nUUa1HVHtnvVcnguphfwAy_zItOGNlMAoRbCilns5HyOQpqyGIcjoImhe12EpORPp6OGRi_GN-NHHrpAthu-JFY3h8xEyUKzPzD6kWu2reyJzMkIeDYQuWXsE9xEya5OtALfZfDg65HbQCHyu1SidDes9AMlKjBkW8aOSROiwgzwfk3PqIo7Lm1MTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc4f2efeb.mp4?token=WQhsRvJGZXJP9byVFx2RR4C7fo6ondjjz6nAb6cmozlzg2jlws-6PzG0dReP_HMrL_B5uamtnZqngQUbadBUVH_bv_wi9xnZI1XXZ6zR5D2yt2LUXZyaaYDOdHzzJOmL1DgvRLQUGKNax2tiLi22Nlb1iMT7nUUa1HVHtnvVcnguphfwAy_zItOGNlMAoRbCilns5HyOQpqyGIcjoImhe12EpORPp6OGRi_GN-NHHrpAthu-JFY3h8xEyUKzPzD6kWu2reyJzMkIeDYQuWXsE9xEya5OtALfZfDg65HbQCHyu1SidDes9AMlKjBkW8aOSROiwgzwfk3PqIo7Lm1MTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت نیکزاد از کالابرگ؛ مجلس چه می‌خواست و دولت چه کرد؟
🔹
نایب‌رئیس اول: مجلس می‌خواست حمایت از معیشت مردم به‌صورت سهم مشخصی از کالاهای اساسی و متناسب با نیاز خانوارها اختصاص یابد، اما دولت مدل دیگری را اجرا کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464543" target="_blank">📅 15:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERzDE1_m_YbPpq4Qyx8NymEJ6NZ6ECpw5wXg-5tYTwE2MpTlSjnaWm71ULgdi0uIxs35EkTEjLsnGGyeraA7Hb39tUahhRUy5XppABheBL-AZE_PQf0dwoYjjyO7rYXen1MRGSBFXP2hLa4XaTVXNKJ8GnCa03P1KGWLB0SkfWt38F_o5REfXAXMAxUQIGRHzZYZHsE9jZInjO9WnCgPwKntN_NwUqdWNT0fPh77lXmDoHl4rrcQd5rd16tQa43QyDNKIdwMGwc8YKUaEdANl0vohtH25ESl4jyZ9327OX1pPUDWSjFtKmV0zPrGsK86qeifLpRP5apCLq8D5KPqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR0J7viU3uo4M044TMNiqHVJIosprxsM0tp1tMRR-yWTm-S-skPb1qmj-2xp49ZQL6P_Fa7dUZKf7jPTiFmLNDjNo693_ur_lW6RCuAQyhEasJwfDBVwqItNcgTWTtj87WEt7960psDavvVM2qwBS4vDaNXoznyrYstzMW0E00P3EQv1LRCPu4HE2WF8Ba3Kgem8yrpw0khS84VZ5Q-oRncTlBAgwYgf2jNsvMBdrtgBomE4uoc-U4K1P4IyFNDmAJFFXdhWXzdLBs_Rqfyjuf2SnHz7NbZHi8hYRS9zBXFToBDEnbLpcLYbyXuPdqWSnpY8-HeZ3O3-aivsP2CavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuyUZIpPb7r7LVb-O_ocKX-2HDOYXYM_Ro08y6iL2OHfYI74Onh9e8koKcqm2KcNiT0o4MVGFqVZGkr_zQsBV3GmKlUN2sWx1D_mZBG0gPLa9tFtMFXe8ogjIgPUjVHZs8Miir3evtzr8rat0PLfJN-tUq4bneRVZRj99VgOiVRVIxyPf3q3Atw1rxW5Rab8kEkmmhoqpH-G04BFrj3grBHg3_ptOK-pSjwpEfVaM3rSxQPdyC-89VFi4mayQxTp5w23E7OSx6FpifNqF333fN0Q8EnvfnhXt9CeVpqv1aYmDD3vkGBF1y0xLur_vi7X2bIEH1bqjjengxgq-FQYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr14u1z-lprrB2EUDPadftysEgjDlyYfhP2_ZtHxK3i8Q8LykOjX57CvlLWh5fBiT_B9HAOOT-oTMimtJz1Fn-snEHct6hDP62JOBkFm6L_9IH8LtNfHrQ0HepMZemJ8P_sED1T1rP9OmTL24-gS4Eo_E4eHEUWNmQU4Eif6I8ku_BG7haiqE7ccIt5OB6w2MPWTg0jRnUx5M6HZE2WNJxFNEnHWBlMChXO74KIrgvpnq9ORkkJPP7SiN1HRO3IS0wPTZbnxRhlfIXHopIUt1aztEmmTC9gNzi18RqUqeCD7RK3uySVn7yf5GwRjaaTUrbEBy0nnGXkXZHiNO-05Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGbbE7Nl6riY8gXsZW4uvNgBXb578n5P64FVEtl56s8JK6HlieWQ7K-r833eX7bJTNmAg1_2cuk2Bus4Mnii8pD-B3-8Qh6E0jnUYTYVd0xIhSZOTn_78d9URzHFdeVt9uR2RDgtfZcn21A6uWF25Qq6VMKF4LqbeO00tMQY48wZwM1HRKbFhspYpgP93UVxww1ize5gpcwcBTu1ivym65ErY6yT4uh4GxOGNquqy10K43O6a71G369sUu_gGGUyyOfWu8vDW8y3Hh4woaS2fZ8ChsH__wqjyMQRcJxrl8ywUTHksWKYKGdrZ3qEoqKYclJWWdGQL-1waqMHONP8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVqRF9pr8IQjxlA-XFZ0DTs14LOMqXr3s8Y3ueBdftQTtV5eHNFHBzWipWf89ZHlgynaAydwwGlbnhaxmYhbSKuuF-ddPGvKrlo69DqBWHElZ8caPUuPyu2s1DaNY8994FLkXX9kSzTOUYG7Baztxnk91KPn_3YYpPis4f0IJ2ZcDCD6uCTE82FwOV-xoDMewLCwRwGu2UDh18Uzt8niONqDSTcqCesGCrTd5MF8hI-IN9E-AT4ZsUT2miaQACuTUGTCiS2ypuw0U-yhPC-kAesMaFzvYb01NMnRohQzlFnbIMDFRXqmM2lftQD9lKXdk-a4sLtnfTz7vZMSg6aFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0ESSy8gzY6RZ1aV_7ByjGy8xupWY-g2g31kMaQxagNwZtcufooQdmwH1jtB1mcqZGuuQErUBxKGoVjS42vnscoeK3j6XsPPDYEwZB2AfqBgQrw9a2xLtR2pdAdNWPn83LFXvxSAa1qdr6P3oqj7uTepaS4jpZlLSszOO7ieGO2vQK6eMnRZHfQjivyKk3IbKRACy9zTaiwEDK6SIh2ObwqsLE2kWD-cOHu600fsM18ThaOF6pKlUcq2pVFg2mNj0vkdbUv5IOrvOsq62AykSinX8lZJHaXMRz7QupuDa4cDPGSNpS0c7-GzRTRuf2TfTeHjWL0f81kbeIedul0h3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید سخنگوی ارتش از خبرگزاری فارس
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464536" target="_blank">📅 15:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d427f3b1c.mp4?token=I8cfhxvBhVVklZlZ_P7ATrD6gZaBZ_MMme4ubtzYdEmjF-01cOsH-9H4qcPZ5PFYvnHTyrqvdqC1WFjqCLIQB3xEnZmuN8v0I9sIfqmtYIQxAvgs6kWdxQJiS6Tf7KJch_6y9wbycaVSu0ekP3FlihN27x_FXDD69FkR9z9TYPytbZK5c86C84ArvCU7FeuTjNLfrHps-HFY_5A2yafBWD0RBLNeygvJmAmdgbc8NVrmvT5YK04iDvn3uwcx6AtVa-tH2mAowDD9t5I9gPGixj_uDZ5fZSdG4RQO6LQ_YnPVEFaZjnNSL1fxBFn105vNAwrXEnnFfmqrmxZ5JtNYpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d427f3b1c.mp4?token=I8cfhxvBhVVklZlZ_P7ATrD6gZaBZ_MMme4ubtzYdEmjF-01cOsH-9H4qcPZ5PFYvnHTyrqvdqC1WFjqCLIQB3xEnZmuN8v0I9sIfqmtYIQxAvgs6kWdxQJiS6Tf7KJch_6y9wbycaVSu0ekP3FlihN27x_FXDD69FkR9z9TYPytbZK5c86C84ArvCU7FeuTjNLfrHps-HFY_5A2yafBWD0RBLNeygvJmAmdgbc8NVrmvT5YK04iDvn3uwcx6AtVa-tH2mAowDD9t5I9gPGixj_uDZ5fZSdG4RQO6LQ_YnPVEFaZjnNSL1fxBFn105vNAwrXEnnFfmqrmxZ5JtNYpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طیبی در پرتاب وزنه طلا گرفت
🔹
محمدرضا طیبی با کسب عنوان نخست ماده پرتاب وزنه، مدال طلای بازی‌های آسیایی ناگویا را از آن خود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/464535" target="_blank">📅 15:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464533">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAT_h6oTPSKy1teRS1-dHDCw4xMawhGLGzCCxNew2-nroEG9c_RuTN4WMsmK2vtVMqAlgtelsGmZCm_C5N9fgw3U_tNLWbsEcdc3l2WIDBZy7yFw4hrU7-CQyhBrrcEJD3GC7ugouMY8va9XL1AH5Yjg_73lwhFE0vDwTWUgc6_5ML4HowX5FMA6UwtvG-0mGDmpresntiYamxyobufOvQVzSpM2YX0T5KYcw9yf7uAo2ug4pm25HXt_LAS9HGMp2ucZLu7i-RKbd2KmXQkG4gDEG7_T_lu4VAHwJKDp6ydQzVOQWBCb-zwTQSNGY_gFCvF4-fNTvU8s5z-pg-tlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a037f0aa2a.mp4?token=jyx86R-Fd1U36xi-gqCQ3utwrNlPAK6LMnYqBlvElZ_pYAU5rkhjyiDCrUcIBCgtm3q0B91aJVO-9GC5Qou1So_o7-3JB5WPw_jScJ_WxbdlQrujUVakGljBrL_jq9r48XvfBwLYpJdaBNosBaFalubJNgZBD2n6RXh4Ujn3p1fF_GZ2TyPTcH1DQgK6zQbBMP8aUBPf6uIk6-WU1gCz3sjXK4B6HE9uJz5Ciga1rPUIZN9UJ-dA9BGlpqUF5ye9OO-qvrfHwVbWkW_hy6GEubTQqngEWepPPvb2Y9cmTMizKi3BnToT5y_pe4Fanq5Y-N_faImA4fKl7h2ZBS6XIJdDHwMnjv91ue0b-zWEJ19rHI2ZelPqD1_mjDqbrbZHpxZZJazqT1MVrrs72J5Ijq4g-DmAuFZvXBaUBzHrb3qjyKohbFbuHVyrHowvIXDgonls7COgG4BcJcczNeARnZDXC1sXl_OrjJid2KEWYneTPqfsHVSGxxCG9s684ETxdq73RYXL4ZJVF7P1zFMiaEbTwExKMrrEjr83oPLvvU0_Mp8p-oAZWfVWSOvPMHLSNlO1afFPq5aS9vxRvlqHIFwoE5utHFuIrxwfQ0zYm4EIQVy5nFMhJZK6m9pabaID06SgmbDp5GpjXZcFGEDaY98xa-ib1-ItMUsh7WR3hAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a037f0aa2a.mp4?token=jyx86R-Fd1U36xi-gqCQ3utwrNlPAK6LMnYqBlvElZ_pYAU5rkhjyiDCrUcIBCgtm3q0B91aJVO-9GC5Qou1So_o7-3JB5WPw_jScJ_WxbdlQrujUVakGljBrL_jq9r48XvfBwLYpJdaBNosBaFalubJNgZBD2n6RXh4Ujn3p1fF_GZ2TyPTcH1DQgK6zQbBMP8aUBPf6uIk6-WU1gCz3sjXK4B6HE9uJz5Ciga1rPUIZN9UJ-dA9BGlpqUF5ye9OO-qvrfHwVbWkW_hy6GEubTQqngEWepPPvb2Y9cmTMizKi3BnToT5y_pe4Fanq5Y-N_faImA4fKl7h2ZBS6XIJdDHwMnjv91ue0b-zWEJ19rHI2ZelPqD1_mjDqbrbZHpxZZJazqT1MVrrs72J5Ijq4g-DmAuFZvXBaUBzHrb3qjyKohbFbuHVyrHowvIXDgonls7COgG4BcJcczNeARnZDXC1sXl_OrjJid2KEWYneTPqfsHVSGxxCG9s684ETxdq73RYXL4ZJVF7P1zFMiaEbTwExKMrrEjr83oPLvvU0_Mp8p-oAZWfVWSOvPMHLSNlO1afFPq5aS9vxRvlqHIFwoE5utHFuIrxwfQ0zYm4EIQVy5nFMhJZK6m9pabaID06SgmbDp5GpjXZcFGEDaY98xa-ib1-ItMUsh7WR3hAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش بغداد برای حفظ مسیر پروازی ایران شروع شد
🔹
دولت عراق برای از سرگیری پروازهای ایران، با آمریکا وارد مذاکره شد تا فرودگاه‌های این کشور از تحریم‌ها کنار گذاشته شوند.
🔹
براساس بیانیهٔ دفتر رسانه‌ای نخست‌وزیر عراق، هدف از این گفت‌وگو «فراهم شدن امکان از سرگیری…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/464533" target="_blank">📅 15:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464532">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ff45c108.mp4?token=Hv5VThzAUIKbFX17H--csu4XZivAMwnySELvsGbQrTZkBMoQulcJKkkpeoo-Hj6jpU6NAyvKOm99-VaX8vFSiBgcF3fIy2ohCJNtjbuJYICO0dLl3wnccu-MzxkkNRCU7fuVMkvndHxQICm8ijGIcvAHGdRWbHoV06iTXlRr1ittpsWG1FTZadjx6pT7RP2iekJwevytT8tcc5aylvgQriYDcM13JVvFr_mfApZheBOHwxv2OGVUc517UYoAl0yheZZpR_KT676_u95x3sV1RcUmBIfIG-BmZnERtYazDdYslRa2dNKyoi38GH6-Kh21yV8wbBDLV6aEcSFQrPssVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ff45c108.mp4?token=Hv5VThzAUIKbFX17H--csu4XZivAMwnySELvsGbQrTZkBMoQulcJKkkpeoo-Hj6jpU6NAyvKOm99-VaX8vFSiBgcF3fIy2ohCJNtjbuJYICO0dLl3wnccu-MzxkkNRCU7fuVMkvndHxQICm8ijGIcvAHGdRWbHoV06iTXlRr1ittpsWG1FTZadjx6pT7RP2iekJwevytT8tcc5aylvgQriYDcM13JVvFr_mfApZheBOHwxv2OGVUc517UYoAl0yheZZpR_KT676_u95x3sV1RcUmBIfIG-BmZnERtYazDdYslRa2dNKyoi38GH6-Kh21yV8wbBDLV6aEcSFQrPssVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: تا ۳ روز آینده در بخش‌هایی از شمال و جنوب کشور و ارتفاعات زاگرس و البرز شاهد بارش خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/464532" target="_blank">📅 15:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464531">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e06262d0d.mp4?token=QNb9QUCMmK8ToyPV_uqhruH8shMMWPuHuB_tX_SySTcO5FErdrRmZ_gs1JhhOg5C1EA8m1MUUmTeAnnxWMmCu7t-TYVUfzcd0FmnnxU-W8uqQ6xiTodS88bq31H9MknqZeI3ejPGKEXiyO8y8oE3lEFzLZyeME4Q5lV3fFRC-3ank5k4tvPcwb6FhAg9MZmUcmNbk7h3w1MKa-g1qiaAluaGf4jz9Dj6v8nMgM2R6m--ycTTfbplBAMOkXyxirkOlJjEIUve1TLVvi5z46Sxhdh_OAiUi6agvqGWOYqu3uh2yNGkVLpwPl8Ico-3CTojomLuLxLsOHPzi7AAHvhCaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e06262d0d.mp4?token=QNb9QUCMmK8ToyPV_uqhruH8shMMWPuHuB_tX_SySTcO5FErdrRmZ_gs1JhhOg5C1EA8m1MUUmTeAnnxWMmCu7t-TYVUfzcd0FmnnxU-W8uqQ6xiTodS88bq31H9MknqZeI3ejPGKEXiyO8y8oE3lEFzLZyeME4Q5lV3fFRC-3ank5k4tvPcwb6FhAg9MZmUcmNbk7h3w1MKa-g1qiaAluaGf4jz9Dj6v8nMgM2R6m--ycTTfbplBAMOkXyxirkOlJjEIUve1TLVvi5z46Sxhdh_OAiUi6agvqGWOYqu3uh2yNGkVLpwPl8Ico-3CTojomLuLxLsOHPzi7AAHvhCaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کبدی مردان به نقره بسنده کرد
🔹
تیم ملی کبدی مردان ایران در دیدار فینال بازی‌های آسیایی ناگویا مقابل هند با نتیجه ۳۴ بر ۴۰ شکست خورد و صاحب مدال نقره شد  @Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/464531" target="_blank">📅 15:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464530">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c31ef5224.mp4?token=Bo0kidfitmQncbw5J0LjiLePgOH5z-biCUHTfqdNcQBE7mZsu4M2o3HLm6Qz1_t30fZqjwTtiaOvUbFDYiZcelVbiAk6vsaiDXjbSxvfg7VNzfv9PCNS3LKkgfRywG8vSBekc0c2KTe71abVVRnqOwVn_Xm3GVTwfg09cY7pYHp6fFzU6PoM1N90zOcLOL4mAoRU3jPSHC-ETli_7X8D3z75Fzcn-4nBuPUIjvId-QELB80g2LzHNFP63DTFbk__uf5q7on3CZ4Omq_BT-cc_Mt-FQQOXmC-aH1tzkBzmHhzV6xs1caNIHeiIF0nw3MapSETWY0hJqeMLAr8w5S-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c31ef5224.mp4?token=Bo0kidfitmQncbw5J0LjiLePgOH5z-biCUHTfqdNcQBE7mZsu4M2o3HLm6Qz1_t30fZqjwTtiaOvUbFDYiZcelVbiAk6vsaiDXjbSxvfg7VNzfv9PCNS3LKkgfRywG8vSBekc0c2KTe71abVVRnqOwVn_Xm3GVTwfg09cY7pYHp6fFzU6PoM1N90zOcLOL4mAoRU3jPSHC-ETli_7X8D3z75Fzcn-4nBuPUIjvId-QELB80g2LzHNFP63DTFbk__uf5q7on3CZ4Omq_BT-cc_Mt-FQQOXmC-aH1tzkBzmHhzV6xs1caNIHeiIF0nw3MapSETWY0hJqeMLAr8w5S-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشایی مدارس ترافیک را ۳۰ درصد بیشتر کرد
🔹
به‌دلیل آغاز مدارس، ورود وسایل نقلیهٔ سنگین به معابر شهری از ساعت ۶ تا ۱۰ ممنوع است.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/464530" target="_blank">📅 15:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464529">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac324dbb2.mp4?token=H0zRJ7MUodNrpSEsdRTMyDJvcuZQ4-gRXZECrNJHXyg930Ur9uD8EnVMwZNat6bRfyd-RiFhxvew-C1UNA0zDoDmSN3PhSGuysgzgEnNy1VhI0JssnyOoP3bF5_XhpRkZCJSoMochQ6_u1hgJLPnoqciicjhoCF_hV3vullf4y0L7EBM1ZbXjo0YonHD-LACAV7tgBCkbPIC5IGKFuMLKGkoQD0LN5WthngIuLJfzOqkc-aYUy5EgLpZIQS1ielbY7pzIwrBtaHoEliNNyKE8l3M1QRyg-8EkNze9AnP2KwJAUh8rOB39BPTjQxyuGigif2SZY5mEYv9CywMHasiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac324dbb2.mp4?token=H0zRJ7MUodNrpSEsdRTMyDJvcuZQ4-gRXZECrNJHXyg930Ur9uD8EnVMwZNat6bRfyd-RiFhxvew-C1UNA0zDoDmSN3PhSGuysgzgEnNy1VhI0JssnyOoP3bF5_XhpRkZCJSoMochQ6_u1hgJLPnoqciicjhoCF_hV3vullf4y0L7EBM1ZbXjo0YonHD-LACAV7tgBCkbPIC5IGKFuMLKGkoQD0LN5WthngIuLJfzOqkc-aYUy5EgLpZIQS1ielbY7pzIwrBtaHoEliNNyKE8l3M1QRyg-8EkNze9AnP2KwJAUh8rOB39BPTjQxyuGigif2SZY5mEYv9CywMHasiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پناهیان: فقط یک نفر در دنیا گفته جنگ ۲۰ سال طول می‌کشد
🔹
حجت‌الاسلام پناهیان: اغلب کارشناسان دنیا می‌گویند جنگ آمریکا با ایران طولانی نخواهد شد، اما تنها یک آدم در دنیا گفته که جنگ ۲۰ سال طول می‌کشد.
🔹
این حرف که می‌گوید از مردم بپرسید راضی هستند جنگ ۲۰…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464529" target="_blank">📅 15:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c74129e8.mp4?token=Sa2pTLS-WDa4YkmKRnluuiotqvSBlTWoXwZkOETE-ZMxg91_hyoiYKcdJO0SZaQwVxKl-2Ol_VHhgw4wnX8necHo6AhW8e7YqVTd5KDyf6pw57WsUz7BOekgC4uyX3QmK32jF0rrjaZPBZYyr5QscprMArjwWwEItmIWHPaB3k_tZ2B6XexyZs3uD2wEg6Xs2lqX3gcDiZZ2dX8IA3fwHGvYqw_g_B-7baK8ggnxU0uaMd3Pjg3oRgRLAA5jfMAIZcleDXb1IfFIOS391DIvuiYmhoMoyV4a_w6XKy77vA0gcL4qI4DQENPFXFD7aVOvlOk21HN2s-yXMyCrcvtcwgxezjdRBJBG_189Eqh3gcxcOFiSJmAi2zRTFUU6nWKYZ43FuNHZLLilIxySHjxN6R17wve9dyVhE2XhIK1v_w6cyZGAObLYATq9kWVRq6VpnKg5CJOZWa5BnmhAwpkpEm3BuArJOwCmrazV5uX8f1-k2wo5U9ywpy3cT2bzCb5_il-A2SJ_8N56_Ptn5gnBzFLNW2Lf6v4P8kj2Pqvkxczazdc0SKQbEeSyuvp6km71-dBCgYigwdKEXEpw5QSk-y-jY3Vb_fRktDcKdgnqNA7Tf5y2erFmm6V8xOMrapAo6JnL1ThNf1TOkDNcZ1FRzTTSwdgfavxZAlOLGavVOpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c74129e8.mp4?token=Sa2pTLS-WDa4YkmKRnluuiotqvSBlTWoXwZkOETE-ZMxg91_hyoiYKcdJO0SZaQwVxKl-2Ol_VHhgw4wnX8necHo6AhW8e7YqVTd5KDyf6pw57WsUz7BOekgC4uyX3QmK32jF0rrjaZPBZYyr5QscprMArjwWwEItmIWHPaB3k_tZ2B6XexyZs3uD2wEg6Xs2lqX3gcDiZZ2dX8IA3fwHGvYqw_g_B-7baK8ggnxU0uaMd3Pjg3oRgRLAA5jfMAIZcleDXb1IfFIOS391DIvuiYmhoMoyV4a_w6XKy77vA0gcL4qI4DQENPFXFD7aVOvlOk21HN2s-yXMyCrcvtcwgxezjdRBJBG_189Eqh3gcxcOFiSJmAi2zRTFUU6nWKYZ43FuNHZLLilIxySHjxN6R17wve9dyVhE2XhIK1v_w6cyZGAObLYATq9kWVRq6VpnKg5CJOZWa5BnmhAwpkpEm3BuArJOwCmrazV5uX8f1-k2wo5U9ywpy3cT2bzCb5_il-A2SJ_8N56_Ptn5gnBzFLNW2Lf6v4P8kj2Pqvkxczazdc0SKQbEeSyuvp6km71-dBCgYigwdKEXEpw5QSk-y-jY3Vb_fRktDcKdgnqNA7Tf5y2erFmm6V8xOMrapAo6JnL1ThNf1TOkDNcZ1FRzTTSwdgfavxZAlOLGavVOpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۰۹ مقاومت با یاد سربازان وطن حال‌‌وهوای متفاوتی داشت
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/464528" target="_blank">📅 15:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdaLwDOlnGHZwmreESLWlCbUXRPB8riySaJfgPcoqu9i8uyr6_EuMJJbJxi_-rhHg6HDFZJqWJNeZw2sKFvQk7jDWx9BYIkUTYuYcbVrFIfEaFZF04dEDFsUclOOr-d9KR1rLXjJzAlWqlFDJyERSqhVWwT_a96MoJB-L8CYQyhxA7x8MIChYNpvFmPpHqAM9xJSD_JKmVLa445XnUjqOLxLrZdxoLC9PA530-cr2TILH_cjHC9fGJ70oHXJNLbehInzXz-W8AVqt7oDqTgCJZQFy4173v0ZKZvR9w_WH00zYCLqZCTqRyQ7nYgMUvWmrnKd-_vkIjPlIc2dWZUpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرعامل تراکتور: با پیگیری ما معافیت بیرانوند یک ماه تمدید شد
🔹
بدون اینکه بیرانوند خودش به نظام وظیفه برود برای او دفترچه صادر کرده بودند که این غیر قانونی است. همه به بیرانوند گیر داده‌اند، مشکلات دیگر ورزش را پیگیری کنید.  @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/464527" target="_blank">📅 15:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464526">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
حملات جدید پاکستان به افغانستان
🔹
در ادامۀ تنش‌ها در روابط اسلام‌آباد و کابل، ارتش پاکستان خبر داد که «۱۰ نقطه در افغانستان» هدف حملات هوایی قرار گرفت.
🔸
بامداد دوشنبه ۳۰ شهریور بود که پاکستان به افغانستان حملۀ هوایی کرد. طبق گزارش رسانه‌های افغانستان، ۳…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/464526" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464525">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb470a098.mp4?token=Zjcp6bGabGMY6F5ZuYCWd6nVMhUF_tFr-PZ_541FBgFacdqxcomjydSn38_LavRB-uSauEqlEC8uaMlJ2ep_Xiul5OMyc8mIeLaq1s2XCPZ7GYRTLnedqTUvC5uGIBL_mJCJVBASkCtWevViKV4WCIC9Tl-3VvkHboej5DkmGUXOg-d4KXV3-_WHayzMrCgv7qt9GS9CCxnnORYRstpIJZj8VF__okY6SWMLWaAdGhghVTPwzERycPFsVqNe5i6waJwWb5St3Kwlpg_UEBGSJRESIehkdaJEpJvuqX4fwddFhnmeimjpKVWFx07N-eGgFjigmavg5_52vZfSV-VNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb470a098.mp4?token=Zjcp6bGabGMY6F5ZuYCWd6nVMhUF_tFr-PZ_541FBgFacdqxcomjydSn38_LavRB-uSauEqlEC8uaMlJ2ep_Xiul5OMyc8mIeLaq1s2XCPZ7GYRTLnedqTUvC5uGIBL_mJCJVBASkCtWevViKV4WCIC9Tl-3VvkHboej5DkmGUXOg-d4KXV3-_WHayzMrCgv7qt9GS9CCxnnORYRstpIJZj8VF__okY6SWMLWaAdGhghVTPwzERycPFsVqNe5i6waJwWb5St3Kwlpg_UEBGSJRESIehkdaJEpJvuqX4fwddFhnmeimjpKVWFx07N-eGgFjigmavg5_52vZfSV-VNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجمع بین‌المللی فرهنگ‌های متحد در سن‌پترزبورگ روسیه با حضور وزیر فرهنگ ایران برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/464525" target="_blank">📅 14:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcohvRMcC1NmOWxVu0ZNAD1P79nDeaNh3phfWmn0euek3qnBDP6fqJN6TPonjbwEQYlHaFTdAF3J-YGkTtT4Xqd9iulVwgWCb_YVnh-ixQgpmStEqQW-fQocBStwncv8HQbEjdgvsxQCDixTwvSvv-Sh8hE9ZHkI4XMXoEpVWMbpgWzEEOD7iHE-rgVxaeq7_qrB7_4yBPCuogWsE-R8L02mhnMdK61JitgXwtkk0VLgrhSQdwy_8XqRonN7B4xlgf8Gx3V0KoIsKcia10jZIJzXZiEhshwyaO75ZHflShV5KqqDc_79QSx66P65Jon789LXvE4YMJMwu-xruMosOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVNq5txZtSR-qyFjrfzYJ01yjp6wJk8k6cr3TKjxkHPSneXK4RpeJ-1G3XKei76r2wcMxTdyS2aT9pclPZLbB9V6BVJYDp7osVwponzCp7QYPbDwyjR5AGkZBN7cLrttZbqwG5U9OcMvEY_l9zWdNmuhRPYFsIqr7N4xyosi5VVZzPGo__utXulkGUQsrT1Es6WXlu4EhLLieWZ4q0Xk49VWdRKLwXEv09Bj7K4dkvsoGZWFxRGZ_3whNaTjcGvX30_mnjlsoeGAtuea4g6snyd2fRcrUkGVlW_US3cbco0JEF0b275QGjm2wWUyRUfFd15B-uUhmsIM2-woLAZ78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvrEMs-dm2c_OvjRMNmoHGdanTyNDWkA9LkOTkQa_84dzPqys6SpPZDpDXt7gyocRO3MPNkFD3DIDz-E8HxPi4HilhgwZJ4vvCESW0bz9wDiLh2tSNOe8gq7rIGti81Sj-bedpdNhvU4FD1bQ93fpu4YvzBzeETnS6lveAbmo34MmAnm-lX9qx-61XmfPawGsf4ASKcuGGRS_jRW2-NhjpNHzDhtPR-28__kGj-BmWF6_CZ51B_n5SwE_5U4gaK7zh-x-RsZL0ujBs-BArOWeAh2S3hN6etpvkVk74YWHe3AJnjWXvNC4FaoxxI7qPto83IC24dOcvks_IDSVh4Vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3VY2Lp7dGA6lQBmY0A6vmqHOzGvEcGpgEfTBIug7SaQWjFItF-E_sOWxMzg9IE2df_Cp923iHjfx5eA__FgVX9fO555xdEFonZg-PuTQgUMa2TBPC8tgXofcAq1l_USYFWk8AJvPNjuutf-VytjcU_61dUGfVeepa2PoewE-mei1nlfoHaUFwxoTKLHk-_5AJJZzLWGutwLfhnNNAJMdZd0en16yjm_mfutw-v5JBgj3z2AfUHvLpaiE6CTTmTUcsA9vJvWC86CY8Q3N7lCQw76Tamg0wD1ARBWTCeXCdQi1hkLUltwxG6IJAyQO7QbtbJVVzM7o1PVrySLk8QWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAOByrFxItksumLsCMiibuaRUYP2sb4HnmlsRzI6sPFR0Y28M2en5tLlFWF3ePvwHnAnTwEeYG1p2ZAhtJ-QHmznQ4cPP0woakwjqRWiI3sBV2rot1IaDixazyLeArVwDLqCFf2sQXSHlCgOsTtbvoEOUvAoOf8Wc4H542YwvnYCfpT62soR0LJR1i8CHlChAnH8hcZ6mc4PSxG1pJfHI9shffV_kHlhyuKaoRbVc7nYbf6bCYB6cLDTMSqI_F9bZV60m1N-gtGQMqIVq5sSJGozAdUcqfnWRvtjFMTgTXqzcUyKHr4fcTyvmpAs03XMn3SuNkCaR-RV-puHboXYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i09uNyN1RKhQnifABcCoi3A54H_K0D_pmv7JtRxI4BDSbaHHtNBAb7P7T-0_IbmgmciliFEDuLJeiJjAGPbFRyoJtQY6EhtV2vsEAMKFvUrVP2ylUBIlOXf6CHRb2iY2OJkCKbuZ267mi2YwBfLGS4hQQrqKQibNhDBZ8oH5KnXKrRB9wrthHOrNKVRk3YozegMuPL01a2VS12oMG6CmyX0FqWXQURgsyZsowpsKzgzFDz23ItPaAoBPikeOTrr-ohdXi2mzKo7O2DcraPGARWpP8f71dkgCAeIfG9na54fLGKLiIsf1Tjdmewr4QcfBGtv8KCE-AMz_jFNe8kKFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V99G2gHV68_3xRNQ4yOoPzfn5PwRHqthfyA_Ea5tD7F8OGnRIWALXERUqT7VJjdqbQlr0bjTkrrHAcI2pXzw4nOiRgw96ry5SdYiPN1_86aTq1T_s9yOv5Yqo0jkIPZRy5oeS7a2zbzATz_QVO9Gr-dp4dhAlGA9e0eYxICZcoGL-y6pG2SYadiilQIn15yFnyFptyWs4lH6nRyyRReK5O0lQGRQADgyA00mdj3MUlkH-aQK96Ox-Ig_gJ0LuiwQdRLdwCIfRcIsUx66t94s1bYY7uImFdLKM-I3pgNlcuX4c6M0xmO70Fgct2rM3mjyOthC-QjxgQ3gesUg3xa7YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنوارهٔ سرباز حضرت علی اکبر(ع) بسیج
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/464518" target="_blank">📅 14:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464517">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f860ff88f2.mp4?token=MMACEcgjekQnYlyeas4mI-Ss8o5H896c2vs4Ilkbb61UMOCR4YymC0YNtymBBZsL4Re9AI6cEi63Olj4Pv52TIwizMDk0K8hVKO8sAqlu8fW5I_yoCIOtC-8vq0ytGRhXwFUPqV7_lUPd0zT-3m7DPJuXE99XX620xJ4PG3DSSBsfA8JtiTLiTH46EDhwAxcYgGmUPGSvIDAACgIzNH6mYBHR7FiLd7o2Syb7GnSEdSXwWlOMGrPXxCmTK25UZF4TLchAem3oz-BU2gfTTj6pNi5IKmq0xemsL2XWY8H9p-KIv5fe_xcdMJmZi5lmJtm_1bqKcNFgrNw5Mj1I9pfEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f860ff88f2.mp4?token=MMACEcgjekQnYlyeas4mI-Ss8o5H896c2vs4Ilkbb61UMOCR4YymC0YNtymBBZsL4Re9AI6cEi63Olj4Pv52TIwizMDk0K8hVKO8sAqlu8fW5I_yoCIOtC-8vq0ytGRhXwFUPqV7_lUPd0zT-3m7DPJuXE99XX620xJ4PG3DSSBsfA8JtiTLiTH46EDhwAxcYgGmUPGSvIDAACgIzNH6mYBHR7FiLd7o2Syb7GnSEdSXwWlOMGrPXxCmTK25UZF4TLchAem3oz-BU2gfTTj6pNi5IKmq0xemsL2XWY8H9p-KIv5fe_xcdMJmZi5lmJtm_1bqKcNFgrNw5Mj1I9pfEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکوردشکنی قیمت سوخت دامن‌گیر مردم فرانسه شد
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/464517" target="_blank">📅 14:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464516">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcb7d1c05.mp4?token=NvArU6D9sbXuCGKf1G1k8vxkzldl6AbYT5XbXE4RDet_7Y4JAKv0qF0p5lbntCVWo9hOOXpzfk4tf9FswZ4jYTzPuGiGq-4p-iN4IIa9cNmEx66hiJjEtinKrXC_nzRXjdp6p220IopfLjIHyiPhY4zoe8jqUiFLTxWNnbtB4dySqeGXNz9-RpSd09YR51Xki12zjzuI46d9uAFlGpkHbBcsUk4EUXb3PNJ1ZR6wbxYrZ9jgnrYspNUoPpXeuUnHZ3i5gOb88lv6eNmrLiXjqIj6Bhiv_YZ74ZrRsJqzSyFQqg8szTR78PXI0yIcqy1-nzVzNRrh_rqlit0nrwK9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcb7d1c05.mp4?token=NvArU6D9sbXuCGKf1G1k8vxkzldl6AbYT5XbXE4RDet_7Y4JAKv0qF0p5lbntCVWo9hOOXpzfk4tf9FswZ4jYTzPuGiGq-4p-iN4IIa9cNmEx66hiJjEtinKrXC_nzRXjdp6p220IopfLjIHyiPhY4zoe8jqUiFLTxWNnbtB4dySqeGXNz9-RpSd09YR51Xki12zjzuI46d9uAFlGpkHbBcsUk4EUXb3PNJ1ZR6wbxYrZ9jgnrYspNUoPpXeuUnHZ3i5gOb88lv6eNmrLiXjqIj6Bhiv_YZ74ZrRsJqzSyFQqg8szTR78PXI0yIcqy1-nzVzNRrh_rqlit0nrwK9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت گازوئیل بلای جان زمین‌های کشاورزان آمریکا شده است
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/464516" target="_blank">📅 14:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464515">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56275f475.mp4?token=HRFNfhNZIo82Xx6_V34vtyjmA9PJ0nSOaXNHGHmrvqYYNZw_4-Q9zUG-m4S0tcArRPE5-Dpu4UHm_ZFlcuL0t4t1Mx8wa7IL87Fe8oudeI-qpdSUATxsSmnxAb3wz7yd7KqBcSwhW-ndJGxXJcE7Rp9Vx4ZOk2-lf1riRXfp9ma7-DOWIlkrmhA5wXH2NQH0ekB35gU0IoDEH5NULUf-BbteTGISRz7CqlaTnlNwdRqFGbynQ1cAsLFnlhLn_29Iqp_b7g8oEUXDQ21P_WnCw8J6oRax_5GacBCecTWWWt-QfRtZvC_v9w6GHOGqV0wR0JoGgK_X2_az2UBENf60SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56275f475.mp4?token=HRFNfhNZIo82Xx6_V34vtyjmA9PJ0nSOaXNHGHmrvqYYNZw_4-Q9zUG-m4S0tcArRPE5-Dpu4UHm_ZFlcuL0t4t1Mx8wa7IL87Fe8oudeI-qpdSUATxsSmnxAb3wz7yd7KqBcSwhW-ndJGxXJcE7Rp9Vx4ZOk2-lf1riRXfp9ma7-DOWIlkrmhA5wXH2NQH0ekB35gU0IoDEH5NULUf-BbteTGISRz7CqlaTnlNwdRqFGbynQ1cAsLFnlhLn_29Iqp_b7g8oEUXDQ21P_WnCw8J6oRax_5GacBCecTWWWt-QfRtZvC_v9w6GHOGqV0wR0JoGgK_X2_az2UBENf60SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بخش‌هایی از حضور رهبر شهید انقلاب با لباس رزم در جبههٔ غرب کشور
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/464515" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464514">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bad74a70a.mp4?token=RS-HshM58jLUaotz7UXmIMEFerh4qGYda6vtVxLpncibe6RwdNpt5nz3TtqNLPSFUMD_XMAAohIhDp1uwr5pQ-RifGGyps8LkalMEeFUlFiTBt8ldziPEr7u5PS-aPQXcTl3vCkeRKP6wJ3lZOLf4x--_AqkmPAVM2VBgwHJtE--aoLwVSLEwA1h4QyYmmzY-um9U-V-P4TYookR4p5TfG4nFFtiLJx8N6To_XJ5Zk3nLUukZ1bmTrD97A93BJHSIWKEPw_GCLr4UKTFEJx4RDBz6bkT139LXtejE1U_gp7_ESLekJl6vr-gks9TeCA8EdMYi7ySNn-XxKfhBTw9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bad74a70a.mp4?token=RS-HshM58jLUaotz7UXmIMEFerh4qGYda6vtVxLpncibe6RwdNpt5nz3TtqNLPSFUMD_XMAAohIhDp1uwr5pQ-RifGGyps8LkalMEeFUlFiTBt8ldziPEr7u5PS-aPQXcTl3vCkeRKP6wJ3lZOLf4x--_AqkmPAVM2VBgwHJtE--aoLwVSLEwA1h4QyYmmzY-um9U-V-P4TYookR4p5TfG4nFFtiLJx8N6To_XJ5Zk3nLUukZ1bmTrD97A93BJHSIWKEPw_GCLr4UKTFEJx4RDBz6bkT139LXtejE1U_gp7_ESLekJl6vr-gks9TeCA8EdMYi7ySNn-XxKfhBTw9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: دانشجوهای عراقی به‌زودی به محل تحصیل خود در دانشگاه‌های ایران بازمی‌گردند.
🔹
شیطنت‌هایی توسط دشمن در جریان است تا فضا را برای دانشجویان غیرایرانی ناامن جلوه دهند؛ مشکلات پیش‌آمده در رفت‌آمد، به‌زودی برطرف خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/464514" target="_blank">📅 14:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464513">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4709c66e53.mp4?token=pYmijn4OpXnlYkZXIsiXFWHb-B9Gs6OozvoMut2MPFmuxoi4o9pyYN9FF234utd1MsRpNr7NVsiI8H26cISlu2dNhZC5KjasqmV4Y-IcRwh9cz13x_cJCVYNPLWFNg0Pl9WD40_wPJYK0WryNwERnKnhjRoXQp2QkO8iLXdB4ed1goSjXGU12k6pyOifCwTaS-hJviX18JdFEsZjZ4fcDj0pyZP0z87Gfn5DvN-Od6UyU-wnpKp8tP0_iwf97iPgkS8VZF75duOyRm3DYrNKF_pb_keo7XZ5qd2TlLRzeBlDCM9ntVhw1LpXFFzYdYKXxuM29etyECK1zzjCV-OI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4709c66e53.mp4?token=pYmijn4OpXnlYkZXIsiXFWHb-B9Gs6OozvoMut2MPFmuxoi4o9pyYN9FF234utd1MsRpNr7NVsiI8H26cISlu2dNhZC5KjasqmV4Y-IcRwh9cz13x_cJCVYNPLWFNg0Pl9WD40_wPJYK0WryNwERnKnhjRoXQp2QkO8iLXdB4ed1goSjXGU12k6pyOifCwTaS-hJviX18JdFEsZjZ4fcDj0pyZP0z87Gfn5DvN-Od6UyU-wnpKp8tP0_iwf97iPgkS8VZF75duOyRm3DYrNKF_pb_keo7XZ5qd2TlLRzeBlDCM9ntVhw1LpXFFzYdYKXxuM29etyECK1zzjCV-OI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار ارزی رئیس بانک مرکزی: امکان معاملهٔ مستقیم بین واردکنندگان و صادرکنندگان فراهم شد.
🔹
وارکنندگان می‌توانند در عرض یک روز بدون هیچ صف تخصیصی برای واردات کالاهای مواد اولیه و تولیدی تامین ارز شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/464513" target="_blank">📅 14:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464512">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bceebd13.mp4?token=PcZdXNiHC8UubsTd6NJD4nC5YbedUGG0dCETIT1LZB3iEWl6aLtRDHpyC_3Vv_sRYhOowPStlW82AY9W4oqHmGtNDfFkJnUGr6417ZlfkEvUAn5Ajxf4ZYyP72YrjxsXswSkvTyfTb0OnKbiyLhQY72-rj0qXyJsjOAPVWufaYRXkFh643TSvosCM7iXzWHEnmUMinZahLnnISqP-8Xun3n0vd4XYXQ6hdK_5PSsEKTEmA9wtgsNZQ0Hw_SDKL7SgJZbCIoEQ84aXH-suaThYL0DhK1kcp4eZPa7D1PXn5frUkISKHtVPvRwovVmJbki4Uq2XE9-TATzDRYTOcCIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bceebd13.mp4?token=PcZdXNiHC8UubsTd6NJD4nC5YbedUGG0dCETIT1LZB3iEWl6aLtRDHpyC_3Vv_sRYhOowPStlW82AY9W4oqHmGtNDfFkJnUGr6417ZlfkEvUAn5Ajxf4ZYyP72YrjxsXswSkvTyfTb0OnKbiyLhQY72-rj0qXyJsjOAPVWufaYRXkFh643TSvosCM7iXzWHEnmUMinZahLnnISqP-8Xun3n0vd4XYXQ6hdK_5PSsEKTEmA9wtgsNZQ0Hw_SDKL7SgJZbCIoEQ84aXH-suaThYL0DhK1kcp4eZPa7D1PXn5frUkISKHtVPvRwovVmJbki4Uq2XE9-TATzDRYTOcCIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین کارخانهٔ تولید اینورترهای صنعتی افتتاح شد
🔹
رئیس سازمان انرژی‌های تجدیدپذیر: تولید اینورترهای صنعتی در داخل، روند توسعهٔ انرژی‌های تجدیدپذیر کشور را تسریع خواهد کرد.
🔹
ظرفیت نیروگاه‌های تجدیدپذیر از ۱۰۰ مگاوات در سال، به ۱۰۰ مگاوات در هفته رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/464512" target="_blank">📅 14:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464511">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مدیرعامل تراکتور: بیرانوند فعلا بازیکن ماست
🔹
حجت کریمی: اگر سازمان نظام وظیفه اعتقاد دارد بیرانوند سرباز است، در نامه‌ای این موضوع را رسماً به باشگاه تراکتور اعلام کند؛ در غیر این‌صورت بیرانوند بازیکن تراکتور است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/464511" target="_blank">📅 14:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464510">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فردا آزادراه قم-کاشان ۲ ساعت مسدود می‌شود
🔹
رئیس پلیس راه اصفهان: آزادراه قم-کاشان و بالعکس، فردا از ساعت ۱۱ تا ۱۳ در محدوده کیلومتر ۷۵، برای نصب تجهیزات ترافیکی به‌صورت موقت مسدود می‌شود.
🔹
رانندگان برای تردد به سمت تهران می‌توانند از مسیر جایگزین اصفهان-میمه-دلیجان استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/464510" target="_blank">📅 14:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464509">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/214085d647.mp4?token=tYyYQwx6NMYkeH3wQ0QShwpfG2oNB9FZz0X_cDT0kLV-FpRPaFM-bqDWCzxLhA23VseD0A2Rs-AU9o41W8H8V6MFAIn3gV4dH98gXex-zP8_gPUmMWlu7d6V2E_bRHqsUpwEvyTq9fCCNIp-yLugOrXLzwEQEzgrauqcpHg-Y46bQkeRCjQqiPn0CoKtyNJq01jDh_gCwdVF7t7oxYu5tungjXkYPwmpdVVE9Zyo1vUv4tZ05Hmo3N-awCUodtoKCy4psRJ1indIM9RAOfup09kaMJq0zr38MO1BT0eyBgvj60tqCdl03-6vJGmzEDl25-tbuUKti1CW5uAcWrCqtIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/214085d647.mp4?token=tYyYQwx6NMYkeH3wQ0QShwpfG2oNB9FZz0X_cDT0kLV-FpRPaFM-bqDWCzxLhA23VseD0A2Rs-AU9o41W8H8V6MFAIn3gV4dH98gXex-zP8_gPUmMWlu7d6V2E_bRHqsUpwEvyTq9fCCNIp-yLugOrXLzwEQEzgrauqcpHg-Y46bQkeRCjQqiPn0CoKtyNJq01jDh_gCwdVF7t7oxYu5tungjXkYPwmpdVVE9Zyo1vUv4tZ05Hmo3N-awCUodtoKCy4psRJ1indIM9RAOfup09kaMJq0zr38MO1BT0eyBgvj60tqCdl03-6vJGmzEDl25-tbuUKti1CW5uAcWrCqtIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌های رئیس فدراسیون کبدی ایران پس از نایب قهرمانی تیم ملی در بازی‌های آسیایی
@Sportfars</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/464509" target="_blank">📅 14:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464508">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-Gnic9cCrEaaI-Agg0xeBhjdkdXUuVkjUvlWWNOVulbAoRP1GB_Tk4_48u5OY-io-vZLQcCvY0Y7hLaKZg_umNnGRgADgZy_U9MAA_fQVOd4gqH0dwJbKFLacnVUGQbfDoKca8P_noYfsWACku0bMPTWLHqarJwgntN_39bXHx-baGigxO5BHK2vWEoMDPdiktOMWRP7Gn9hpaKKIU0hjIWJzBWshYKxTpuMIp8veuC76qxrx_eR1AhXgM1NImabn1Hs4ydIlTTtBLriF0hXsla80fT7GutGH-nESgFHwlPxrQNfjh4xtHUm_c20UK9lbWSuNlxS39HE-ekklw9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ وزارت نفت اختیار هلدینگ خلیج فارس را به‌دست گرفت
🔹
نوبت دوم مجمع عمومی هلدینگ خلیج فارس امروز، با دستور انتخاب اعضای هیئت‌مدیره برگزار شد و در نهایت ۳ کرسی از ۵ کرسی هیئت‌مدیرهٔ هلدینگ خلیج فارس به وزارت نفت رسید.
🔹
۲ کرسی دیگر اصلی به تاپیکو و سهام عدالت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/464508" target="_blank">📅 14:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464507">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJW544hHJBGl5L0xkcoSdLxEVhJZLTCijVfAUZFStq4205eyTLVs1WXjT5ujNzb8L1MDfWarAvObdauF4FtfaOX_8oLr3cuD5J9E8cNiMdqGlWHHm2gomAsem1-8FAruMRRWgdSoumMwi2BXJrS0hzsZAfcUtkwZIDaWfViNjyLAyJV0t6AnU6HqEIRrhedMBYs5Q_yzN3JKpSeEFVTK3khxXa1F8btnzSdVZ-nD1Y5PxUpEu9bIwVyIuuoOSKuGYkEblsvLuo3aooFvQ0Ub-G6mxUs41CISJqAyH6cG5SclcZ5hgO7q4indOvHn3HvNfF_bQrzYBb2AewsjZpmCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ حوالهٔ دلار به ۱۷۰ هزار تومان رسید
نرخ‌های جدید حوالهٔ ارز در مرکز مبادله به‌شرح زیر است:
🔹
دلار: ۱۷۰،۶۲۶ تومان
🔹
یورو: ۱۹۴،۴۷۸ تومان
🔹
درهم: ۴۶،۴۶۰ تومان
🔹
یوآن: ۲۵،۴۲۰ تومان
🔹
روبل: ۲،۰۲۳ تومان
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/464507" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464506">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgvH_e4VZgPy6uJy5TedYOB_bjHUUdYYCSKpd0Dx3EZrtPi07gpnpnhBgMErB0v6CqCCHjVFSo9eKKmzf_ISvPdz2Vo7cZ3ubu_cHlVO8J3ocrT2UagVxitPqXmd-UDL64Z9i_BoGpfP04d_GII1KtsSHaIuCRC7LPiSFh1XD-2Yat_KIdHPlKZoKqWzJS4PUqBLQyqu3pzgvw6kWNyLXIs4Iw0cGctX_p7d_P5IhUX_j6JYNvLkorJgZ-qvKZTJElCBtbaN4VxPLERYXvx-UVFUJjQyTBRtAj1r7cK6yzx-CuA3u32U-SaOYZcigZSlna_qh7PQahZz8-Ce0d7OKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: چرا و برای چه باید با ترامپ دیدار کنم؟
🔹
رئیس‌جمهور در مصاحبه با الجزیره: ما دیگر به مذاکرات با واشنگتن اعتماد نداریم زیرا پس‌از هر دور مذاکره شاهد تکرار حملات و تحریم‌ها هستیم. چرا و برای چه باید با ترامپ دیدار کنم وقتی آن‌ها حتی به توافق با ما پایبند نبوده‌اند؟!
🔹
وقتی راه تجارت برای ما بسته شود، بستن تنگهٔ هرمز هم یک اقدام طبیعی است. ما برای منطقه‌مان نیازی به «حاکم» نداریم. حل بحران تنگهٔ هرمز با استفاده از زور امکان‌پذیر نیست.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464506" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464505">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be59c43615.mp4?token=uMsTCbrl6F6v35W8OuFsFjr1VQdgW_0hCQXlFmYKejtHtDZXSk0buBuPkRHHaT7y3ZyET1MzOKJtsv_52Lu8d0J1X7sNX_VgmT5Z2icFjKPqNrWvcUABb7vUd1F3cX-eFEI1T0G25RZLb8XApwGMiUtnTHAGXisgCe48BMPh5z9P2jaOMytYE_VIM-3OfTTwqgoQfJrQQVtNY_TDJ9NpVk8BNsYFJmHDe6CnyqbWxVlJgdCTQ6dmH0AnceykRkoZtmnaFYP4JxhoKgq_LPHcO9d99IGRaEjSBH5FOMhW-oHm4-aQ8aa0EOwOR7s7C0kP6Nfo-VOyg_hmVDUdUJPaSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be59c43615.mp4?token=uMsTCbrl6F6v35W8OuFsFjr1VQdgW_0hCQXlFmYKejtHtDZXSk0buBuPkRHHaT7y3ZyET1MzOKJtsv_52Lu8d0J1X7sNX_VgmT5Z2icFjKPqNrWvcUABb7vUd1F3cX-eFEI1T0G25RZLb8XApwGMiUtnTHAGXisgCe48BMPh5z9P2jaOMytYE_VIM-3OfTTwqgoQfJrQQVtNY_TDJ9NpVk8BNsYFJmHDe6CnyqbWxVlJgdCTQ6dmH0AnceykRkoZtmnaFYP4JxhoKgq_LPHcO9d99IGRaEjSBH5FOMhW-oHm4-aQ8aa0EOwOR7s7C0kP6Nfo-VOyg_hmVDUdUJPaSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عادی‌ترین طرفدار ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/464505" target="_blank">📅 13:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464504">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59e48c05f.mp4?token=HOjhn-Y0ZSdSkQ-hBTWg7l7YKOvOd54cnJrg4JBhEQmdpHDgwHiOHw407aWwg_8RKf0L1IFgKXg5BSBznjGkwupnDpA6k4lGoRAle3MT0Aw2hls32PFvEftmMYpUdcypM2-GJsAsNsHUY5VYmqYBdW9RIZ_CSt9VkLJTzI9uKzTsKGbb4-nzsufsJpWkuIHCzCV6HffjNXkWQAgCOFQU48D3YTBIXdVA6zqYMeodrOAMhNRw6CfxrQkXrDb5TqNfhG2nYIrk_Ra9klQq72A31yRd5mlmV3_8jcBF3UB6dy2B5CYtYjetKhv1TEPBzyN8k7AG8LJj5TmaGNcAmm7bjHrrdea2Ew3kpXe8lk_fyrqeDXinKlLT5B5ynDCpPkwl5tXEvMxuXustjkjpbBtEEP0ZGURC9xseS76oxikGUZQUvC_SVsCJF-Y8hiV3VT892kPZBB5sPiN96Z1paSoqrWwUoa7wyUv2VVkql-ilo_dqLMSKIvzvp1vu-KrUVE5zQhKCA663ZP8yWzhaTT8pgN6TykC4tN0vFMqiVvIqwnu12YWOcapsJJWF0BQ-04diBxCkCq2rKscQGRm9l6EuAIuCmWcXL4Vjf93aJPulzqqJAv5WOx5Orqxnrm9kYPTGpm7u7uGYYOGADY4EgJkApC__NLGnVT5N90gAVx2G0-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59e48c05f.mp4?token=HOjhn-Y0ZSdSkQ-hBTWg7l7YKOvOd54cnJrg4JBhEQmdpHDgwHiOHw407aWwg_8RKf0L1IFgKXg5BSBznjGkwupnDpA6k4lGoRAle3MT0Aw2hls32PFvEftmMYpUdcypM2-GJsAsNsHUY5VYmqYBdW9RIZ_CSt9VkLJTzI9uKzTsKGbb4-nzsufsJpWkuIHCzCV6HffjNXkWQAgCOFQU48D3YTBIXdVA6zqYMeodrOAMhNRw6CfxrQkXrDb5TqNfhG2nYIrk_Ra9klQq72A31yRd5mlmV3_8jcBF3UB6dy2B5CYtYjetKhv1TEPBzyN8k7AG8LJj5TmaGNcAmm7bjHrrdea2Ew3kpXe8lk_fyrqeDXinKlLT5B5ynDCpPkwl5tXEvMxuXustjkjpbBtEEP0ZGURC9xseS76oxikGUZQUvC_SVsCJF-Y8hiV3VT892kPZBB5sPiN96Z1paSoqrWwUoa7wyUv2VVkql-ilo_dqLMSKIvzvp1vu-KrUVE5zQhKCA663ZP8yWzhaTT8pgN6TykC4tN0vFMqiVvIqwnu12YWOcapsJJWF0BQ-04diBxCkCq2rKscQGRm9l6EuAIuCmWcXL4Vjf93aJPulzqqJAv5WOx5Orqxnrm9kYPTGpm7u7uGYYOGADY4EgJkApC__NLGnVT5N90gAVx2G0-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کبدی‌کاران مردان مقتدرانه راهی فینال شدند
🔹
تیم ملی کبدی مردان کشورمان در دیدار مرحلهٔ نیمه‌نهایی بازی‌های آسیایی ناگویا مقابل چین‌تایپه با نتیجهٔ ۵۹ بر ۲۱ شکست داد و راهی فینال شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/464504" target="_blank">📅 13:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464503">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyiCmjmn1x8gCPPiaNDiztZS7Upooew6PzJ6JJ_q8ONfTTNLobQa136-Dr38Om7bwJHe9L9s4r8tELpm-caMOEJb_3mcdnzLMBoewcVcPBVdnRPhhvgTE8mNIOYZPnr-cSaE9Rlvh61-aEyB96yugR4Cna5I9sB-dIMz5WGk1YRGOgeh3LBQ71Q4mbXRao0FKK70Rbz5HmR3AwWlOKKzMZz-h9ckcD4IxR7BkVLsV2sQWil-jDCj6BemK2T9btZOwOis1EtxVenzBoF_EE8Qcd3bWbh84E2HMqNgY-7RdYryRuBIuxO3z7Y9tsZVA0Qg7KpfKnhkr5DEZWaO066UTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیرکل جنبش نجبای عراق: درصورتی که پروازها ایرانی به عراق ازسرگرفته نشود مردم عراق برای اعتصاب در فرودگاه‌ها حاضر خواهند شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464503" target="_blank">📅 13:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464502">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9y-GtcDhYSd3ClyTyuWyfZpmSBV7-KxQ9ScwpTmKQczq3gDA9Iz4KvEf1uY5TIJzw2H1TFCFRerZLrMaJsBdywi8lz-s3oom8YHv97UwwLiqzqJ8R9F9pQGfK5woK1vZ2JaBzClYYovj6pD1rucMJZIRiNgsjm8tVaR42leh4Qz_f0Ps0_xFm7UYysdAbWrVKoh6k74R1ebFLYcHsz9vLHscQNudTnaGDJgaqyhVLzLgbl_irU7Iig-O26jcWIJ55vZTAebHSlUifes6zeUHIeqeqUM81rN_4fNQgexl3m4viDFj3SR9fTLr5fAw_0rBUnZrwzWxfnyeds5VPk3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: تورم نقطه‌به‌نقطه بعد از ۱۵ ماه کاهشی شد
🔹
باوجود تورم ماهانه حدود ۴ درصد، اقدامات بانک مرکزی برای کنترل رشد نقدینگی باعث کاهش شتاب تورم شده است.
🔹
تورم نقطه‌به‌نقطه نیز پس از ۱۵ ماه روند افزایشی، از ۸۴.۴ درصد در مرداد به ۸۳.۸ درصد در شهریور کاهش یافت.
🔹
اگرچه کاهش انجام گرفته، اندک است ولی نفس کاهشی‌شدن روند تورم نقطه‌ای، بسیار مهم است.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/464502" target="_blank">📅 13:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464501">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLdoFploPS_K0nyPVKUnaRRtR_nqbsBJJqyFE7e5PEaabCUMI0Ygsw8mGz28iXovH_eOFLecB-jn61xFI6_BEWSrk33uO_029Km9qwOqh8E6AoEF4JxLglvUitfJdY5yYY7uO3Wcd4ABQYW_pBN68mrv7d_a7MKaKUA7CjmFJGWHJi9tNs4iymKqtLNudWh-HEhOaHAfSe4Oi1-I-OrguWcPawIS05ZUVn0zSrtzdAhla5FETAyfO0iD0fKRemU69TJLTaBCzwmPmM7mmIZfE4xKf31FRZKub0L6HUArIqxRy375SGoFpa_9v1c7XVkqQ18UJ5OLdT1fJuWx0-Mpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنهایی ریاض؛ عربستان به کمک فرانسه چشم دوخت
🔹
در شرایطی که عربستان با تشدید حملات و تهدید علیه زیرساخت‌های حیاتی و انرژی خود روبه‌روست، ریاض برای تقویت دفاع از این تأسیسات به شرکای اروپایی روی آورده و فرانسه با اعزام نیرو، رادار و سامانه‌های دفاعی برای حفاظت…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/464501" target="_blank">📅 13:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464494">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4-O49sePCOEmAUoahogmolhrJaMJ5holfCmwtJ9VOGii60S5IVCwn4bx_S8TLrRrKtpXrtCV32Hs_IvNoeHTVhriWj8D-KiYMS57nuSQ8KoMH-isko-py6ZB2OfYPEhOlVbdU56jMnRidqTdFg4Y4ROvcGVyLDKAETxCdH1o0zyruvqBRzL6i19vDk2F_JWNKTYRia9UwbbVnrnekLSZFoue2JMtzqBWAq8y_hjcBH3KNcv-ZtkiTItbtRxfdxqy2obs1k70QWST68M8MX_6V8eO2yiVZHbxIs1hqJNw_EqnQKwvrq1XCZU58UURJdEhxh9XiJ6zqEurMnvddr_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_FDvVbjvenEnmb91-02e-qDS2auk72R4ZU9gNmV7a-Ch21Ix3FO7zKykaqJG3YZ7m74MmfrhYoipY_Og6w0unOI4A07Jp89J8rl6AONpZ0_KHs4nnjIIFbSzurn0FTiQAGM3lVtsvGj_6hzUg8ewfkDNQtXMdDNB9kEfECEW71PHrDMCB_x114Gc_PP9oD1Yh0FG9ynUK5VUMySZvEVKhRJ2S7QBI_byxj_LgrTIHSgG-CKUxttOKKKLH22BVMce_K6sX2c4An6CheiXpS5x6TAZ9AGPWSr_mCofSGDDP4BJhKcbYYetJ5ewSrHLPcQlNwaW0Eo6n6JlzRQBONdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lv6qYM5p7RK24YfDVxA0LfLPU-89R3pEefiXlYxWKGnYwyLkOIrYuP-fs7a8_V8PtoJo1K6TfYiym07N7vFi3cdcw6jJuCL-C6B0GocZ_u9wum7o2C1I1lGpR8qBtwzWbJQUcrz_mg5KlAQED9GMJjUQEW3YWfSnSbjp3c35XHr2hRIpaSEvvHnx3AqOlNBIlfcFVp9YwI3Rjuqmq4H83evEFVLC7Jigv8URk2y92HEMIecEqMDziyP4ZHNkIHnbqr-sEq1l8G55u-xKP2DYG3dtzChg3-Cgy0IKajPsS7mxNxAhw-StNOBDJiJ5-iD0IG39S5o1H2ESwU4tKTjbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CR90G_4rZzG_n3qTAd5FJPnYw1Lj-tplTZRKqHgome0r3YoaAFn5tOBJZ5l6YYUltyUq0exMHOEDmXKJ0V_xc2pmTMam08w7XfaObOWnYLs3srYOittdom-LIv7LsnQiYgZvnUrIyFn8RZ2DuOqdINCEdpvI1Oee7A_Nzw32MI2vr5_9zVHlQlcjNftSK1A4ie67OfI8gz3gR2uZFlDPYkO-LH9oXmjhMqCwzF3CWhMv6zzVv2X44kLodLuMBqzmaZGhggXWKG8fLfDDyw9YhekESvrxyA1S1h4Y6dNKwhGrSt1HKF5GJgWQrNSnr6DXlWJcrSCtcSH78q2kH4TjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9_g_gsnme1OUxGdMYoFTGI9xt90wod9-AsdLtcs66VGQalsj_UUhb8pAFieRaIIamclkYiTQsjiGVnBgpmysM_sC_6qvzKTeN24EFOhK9yYoMLJYbSBEcuJERic_rYl7vfXl8DtDM14U-m9nDoTNGkjWaBYfvlwH8T-j3S1FxgHY_mERW7P8p2X7pRDCLhXPJ-OagPaVmsjzeDF383ZuZWDcO6vtYOMRJk8D5jHbKXdUfirF09YPjQY-e7ndJBaEKVrIT_NXZPLnSQDnDSYII8nmb6xMuMbeWxH0SW8czCgJqK16CYelyvXsno2GEQU4CxKf0R4qY7ePK3lpOf-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sonMaWya62mf1ToAVw3sRQzst_oS_Y3MNr004Bvu5FhgRitL1yhSVwx3ibA-Ky4Xu70uYwFlVrIaTfXSUgLQCtKwotY4O8hkcrEX8cPOx1ghcHPF2Gu7oNsANvzRlB6LYJxrDU7OyNaaTvmQBWVlbxeqL8HFIzFfC6CRImJx_69jqbgMRMmHVd-ZlneKo934oRlvwsEnGo27If-OtWf5GDOgS2ZiD-9NciqAyy4il18c_p8UkSi6f2XGGxUFdNVsMCP7H6gtqKqs8SKiiPbfM-XGS_OkQ89CCtwPnzxe-izjtxkvGDi4kiSwlJrk8itmxvIw5KWZoWsxNoWVON9z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWjGCMZrqu_vd89eRNKMDu9Ou6lFw23i_KmqI2jlgVl3DNg6YDX-U16rZrTNl_emUvc4Ud1izqP_8ckriIzyiUifRkFeVc_1y6ae6nWtUMVb8D7QB9-qRkN1Fjpd91fnqDedo5AA1wRm4tPCCngHMBHRNdb39m_E9p4iomqRy2A5VKo_Hv0dZlzcTv0pDg_1bPuZ7QsEbeREUsUppbDu3W7uW9FxgKh41F5jQ3UIrIwPsA_xZCL0mAiQ6kRpmhXyOY0Tb5ZGq7R6ABA1AE5_o_VvRYi67b6FH2zau09OlTkXzoGpSbqnAXL-j3kMt56ziamrxK3lZdFSUFp_YxEAEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع باشکوه پیکر شهید «احمدرضا محمدرضایی» در بوشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464494" target="_blank">📅 13:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464493">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb527df92e.mp4?token=lCI0Rl4fAaIkheF3Ty7i-qXUgl08donRzHhMvUPsXKsFVjKwyDNGSCClqFbOuSmTPQJVgQLj5hP40vgOUPjAgyHOD-gsUYhijrFtnhUb6UhpaHb0rvqKGFrIbBeRRRvo54qnDEtgWVKoCGCkJDQvMHfCL8y685SQvs-lHutfqU-imhteBQkFRVaeImxU0I6vNldsDW92NZSv4jFlDb8e_kQkTSziS5x7NsRy3f5wZ0JETf0uQ8NQmd9CxHRsxzK2taA3f0XwX4NAmMXLQ0xwz0cbHByBeN11B2GVoVAk3xfwtH2YwG20NQ7qXaz3ncvCKlH6ajQ3tKsRlS5yozQayw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb527df92e.mp4?token=lCI0Rl4fAaIkheF3Ty7i-qXUgl08donRzHhMvUPsXKsFVjKwyDNGSCClqFbOuSmTPQJVgQLj5hP40vgOUPjAgyHOD-gsUYhijrFtnhUb6UhpaHb0rvqKGFrIbBeRRRvo54qnDEtgWVKoCGCkJDQvMHfCL8y685SQvs-lHutfqU-imhteBQkFRVaeImxU0I6vNldsDW92NZSv4jFlDb8e_kQkTSziS5x7NsRy3f5wZ0JETf0uQ8NQmd9CxHRsxzK2taA3f0XwX4NAmMXLQ0xwz0cbHByBeN11B2GVoVAk3xfwtH2YwG20NQ7qXaz3ncvCKlH6ajQ3tKsRlS5yozQayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوشاد عالمیان به مرحلهٔ یک‌هشتم نهایی تنیس روی میز مسابقات آسیایی ناگویا رسید.  @Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/464493" target="_blank">📅 12:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464492">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1XOZlyrjx0h1sJ3C9FRMxpgcmtkXJ00hAO5eGH79e-xtqfAG4crpvRQjGMAx_tDiH1kZNfhqd-VTjViLrKYoAjQQr6JjWumFeqGMUcRYNWEi7WUiwAHrly3zEmVx92QCCO88gDdeULHi5qMN9LcCnbDq1ImCF-sPUEe6IQdu69AeibB3e3ToSPSjWfD7HSEK8IW9xwoyECbA_m116aqvGsv_wrzBUpX9ShZeM4OHMIR4hm6YdQgwkOx5rw5-kzidS1zjblOl8fY7xqKyf9WrKatZJ6JTVBR7Hi5ss_1FhSiRHDK6hXqGcteuCH1kY3dHJAhyKm8wXAJJ1Ie0RQIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراستی‌ها زیر تیغ افشاگری؛ معیار، بازگشت پول نفت است
🔹
در روزهای اخیر افشاگری‌های متقابل دربارهٔ تراستی‌ها بالا گرفته و این پرونده را به حاشیه‌های سیاسی و رسانه‌ای کشانده است.
🔹
تراستی‌ها در شرایط تحریم برای فروش نفت و انتقال درآمدهای آن از مسیرهای غیرمستقیم شکل گرفتند، اما ادامه فعالیت آن‌ها موضوعاتی مانند کارمزد، رسوب منابع، ریسک مسدودشدن حساب‌ها و نحوهٔ تسویهٔ درآمدها را مطرح کرده است.
🔹
برای سنجش عملکرد هر تراستی کافی است مشخص شود چه میزان نفت تحویل گرفته، ارزش آن چقدر بوده و چه مقدار از درآمد حاصل را به کشور بازگردانده است.
🔹
در این بررسی، زمان تسویه، هزینه‌های انتقال، کارمزد و شرایط تحریم نیز باید در نظر گرفته شود؛ بنابراین افشاگری‌های رسانه‌ای نباید جای حساب‌رسی دقیق را بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/464492" target="_blank">📅 12:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464490">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsHan2uxxaRDsbN850qzgyT707Oa9O_uGKoyrZAtz4x_DoC6FgwygT9s7mroCLCdjI5T4UGF4RRrkvbGWhSTx2vhFtkEHSS8xsdq6jkurthabFw__fRG25cxpv8g42zdWLyk0mZpmVJZvZ0S3fM-huVsaXvkcbdk6woVjBksh07mEG6B1egl6Vydf2SVHBFzQZriwr3cFditsi9a4jJS0OaRml3nMap4_WCTFrG4ES_WGY-QhDrFZAAASTV8Rzhilesm4Lh3ZY_tOwmqwlfdvf4Zp934Nsi63ARcLXayvYPP_GfbKnkUQTfsdI-8FaVLYuecTtg6eHiZZy4vb-5E7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس صد هزار واحد ریخت
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۱۰۴ هزار واحدی به ۷ میلیون و ۱۵۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/464490" target="_blank">📅 12:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464489">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e15321a38.mp4?token=D8pOTbsKOlq49ojhhjkpX8q7Np_QlMsOa6OQW2C4uZ3sLSX_VtmMWPn61KnScGMgl2sxpDyJBSOy75vZAOmYA4FnkIX3lNDQqxcvFqDWmMzT6OdNa1-iEIRqTVivfUJ2fNCuETv3PTnFe6WZVpobzCZjUBXzC-VwX_K7wM4udvu7pUf3NO4Z1g09FMVSitrE7XNTj6O37RUcO6Relkn6h5sicgdLxjTcnW-I6pJXVG_1R4ZQy4h8xSscy9cbJoqnjL1bS6ULvRSzSGTxYbJmsrM0jPfV_WGY1JwsYdswj3u4k425qHgLjPKy4B_TUHOFTOlIrzL3Gp1I2tnRYvpzBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e15321a38.mp4?token=D8pOTbsKOlq49ojhhjkpX8q7Np_QlMsOa6OQW2C4uZ3sLSX_VtmMWPn61KnScGMgl2sxpDyJBSOy75vZAOmYA4FnkIX3lNDQqxcvFqDWmMzT6OdNa1-iEIRqTVivfUJ2fNCuETv3PTnFe6WZVpobzCZjUBXzC-VwX_K7wM4udvu7pUf3NO4Z1g09FMVSitrE7XNTj6O37RUcO6Relkn6h5sicgdLxjTcnW-I6pJXVG_1R4ZQy4h8xSscy9cbJoqnjL1bS6ULvRSzSGTxYbJmsrM0jPfV_WGY1JwsYdswj3u4k425qHgLjPKy4B_TUHOFTOlIrzL3Gp1I2tnRYvpzBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلبان‌های ایرانی چگونه صدام را نقره‌داغ کردند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/464489" target="_blank">📅 12:26 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
