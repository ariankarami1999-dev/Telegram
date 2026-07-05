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
<img src="https://cdn4.telesco.pe/file/QB2CxLwPBFIUgX9LU8AuAHjfVE4ZUugFVRPKJ2lLpZz0PWdrsbC9_fBaYuIB6cXXTAsaZRIoh271hOhyqzeiyZAPymb-v4FKLVdxF630qou_-apPfZuTFTesCccIfSnpSBwtFvLQeFsW6pkHfjPnKz2d7VQoaBpwutT83YBnjssCDUjjWlC0uVgvQSRnAVU4WxC_SIvVJlHtiPQa2qAq-flMU-NJHgei2BDnxzHaEebjwWb2BE-Qs9ka-ZNcORnDdDwDW7N9RhXa8vVSDPMad-HijIqBx8rim5rWgh5_JC45YSiRj8V_tYSsqNXD8RKVTHoTVA1n6tDHOEfIYccbTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 20:27:24</div>
<hr>

<div class="tg-post" id="msg-447193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927fb2214c.mp4?token=mKKWXmxUfPtv5qfvauUUcfSj1w2wvOm7wOhrH0bj2yupvkE3-XFSv8jkMg4ZSWw7nZqMmAm5vTYIIeuQxLEqfEBuOCfq4b8z2EyTmWxdGYZFoGWWugWPsP5EFxvtPHCw5az140zEsgbxJF58zwsLzT_jfbhcpnlh3cDAoyFs23JlcZXXKRbwBO3JKCU-TTB4PF5tHHu5wOGRGHWOZ5TYnCZm0NFbeJ_Nr3ct_vRhRAexAZNx5WWS-aqkBFNi5V_erVbafkRKdJ0n21e7k49MWVQgpOOU13VDNfEZlcvCCRL502XRtrIGd3dbxkaoEU0t-yVZDFdH9QEE5bTeMOgI6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927fb2214c.mp4?token=mKKWXmxUfPtv5qfvauUUcfSj1w2wvOm7wOhrH0bj2yupvkE3-XFSv8jkMg4ZSWw7nZqMmAm5vTYIIeuQxLEqfEBuOCfq4b8z2EyTmWxdGYZFoGWWugWPsP5EFxvtPHCw5az140zEsgbxJF58zwsLzT_jfbhcpnlh3cDAoyFs23JlcZXXKRbwBO3JKCU-TTB4PF5tHHu5wOGRGHWOZ5TYnCZm0NFbeJ_Nr3ct_vRhRAexAZNx5WWS-aqkBFNi5V_erVbafkRKdJ0n21e7k49MWVQgpOOU13VDNfEZlcvCCRL502XRtrIGd3dbxkaoEU0t-yVZDFdH9QEE5bTeMOgI6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در مجتمع تجاری در خیابان الظلالِ بغداد
@FarsNewsInt</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/farsna/447193" target="_blank">📅 20:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5b2b7dd7.mp4?token=pxQnw4jZz1d8-nou97v_aAR-QYl8dj4wXwoHfaePuRLhxHhM1-aw8OpuGu2jjYM4A3893qGmV03KgkTflKIsnr0bR5Qr6MxTqIDL_H5ONNJnRWLx-66CVj9LwI72ZxCkgoQJBc1ESAiYw6dDHL4FvaD6SVLLBgz25d0NaMJi_wWIFfAwupR_39m8SsNU-8YNeCz3N0qcoQl2WpPs04WbwX08xr9KIqqbj3BV7h4FS4u6GbTgTcBMe7S_R6elbWmGBT4eEwiZlgo0BUL64Vj4e49NHk74PWMO1E67d6J9f3RSmvzRQgKIz_lx3xscAkr7aRcVEprkLJi7CHLlrl4j_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5b2b7dd7.mp4?token=pxQnw4jZz1d8-nou97v_aAR-QYl8dj4wXwoHfaePuRLhxHhM1-aw8OpuGu2jjYM4A3893qGmV03KgkTflKIsnr0bR5Qr6MxTqIDL_H5ONNJnRWLx-66CVj9LwI72ZxCkgoQJBc1ESAiYw6dDHL4FvaD6SVLLBgz25d0NaMJi_wWIFfAwupR_39m8SsNU-8YNeCz3N0qcoQl2WpPs04WbwX08xr9KIqqbj3BV7h4FS4u6GbTgTcBMe7S_R6elbWmGBT4eEwiZlgo0BUL64Vj4e49NHk74PWMO1E67d6J9f3RSmvzRQgKIz_lx3xscAkr7aRcVEprkLJi7CHLlrl4j_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
برنامۀ وداع در مصلای تهران به‌دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد.  @Farsna</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/447192" target="_blank">📅 20:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c554448e2a.mp4?token=mVgvuWNU8ZVNe_OHP1PGvfia4uk8nHvowjxZG4-xxPhg_YZnbu27O2rz7X9FrF9WdSgaO7mnywhs8NQJcN8VgfDKpe_SLUqlJOewSsh8ZbqqrxK0QxofDY5bqjQ4aelwXa0nqxxrACcgGp-iwRJ72dnkLKW3cN_HuSs7V1RY77n0aC0E6Sud2UKnqAbjc-XQH8wh68JCTeXI5524lAbUcOPWRI3U1Ul6PoftTAHRtNDR6CsBYMqK-z54cnC-vzgc3bHuEHaqugzN9vrit1G5c6Wd38ra8Vj47Aaf-UUGuUo6UNYWez5b-DIBP1HsUKrCr8kywR07gcAmYrzAvNrHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c554448e2a.mp4?token=mVgvuWNU8ZVNe_OHP1PGvfia4uk8nHvowjxZG4-xxPhg_YZnbu27O2rz7X9FrF9WdSgaO7mnywhs8NQJcN8VgfDKpe_SLUqlJOewSsh8ZbqqrxK0QxofDY5bqjQ4aelwXa0nqxxrACcgGp-iwRJ72dnkLKW3cN_HuSs7V1RY77n0aC0E6Sud2UKnqAbjc-XQH8wh68JCTeXI5524lAbUcOPWRI3U1Ul6PoftTAHRtNDR6CsBYMqK-z54cnC-vzgc3bHuEHaqugzN9vrit1G5c6Wd38ra8Vj47Aaf-UUGuUo6UNYWez5b-DIBP1HsUKrCr8kywR07gcAmYrzAvNrHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما برای وداع نیامده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/447191" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5ebf4ec7.mp4?token=qwP9Hg7n3xhP-kP1BBmkaCbY2etJU_zxocmDL-L0tbLmUCFz5EgFW3or00lJ5cjBJfDOLGEpfKfTIOKUwkLgCf2-NxoF4C05cojptvjGEuEsS4FirQ41CRK54qG-3cO-xBrquO9FKiydpYIpwuXW4tA4eLw91gYBeMaO-9RELKKOPOn5vbuqOVsLNenH0LwGZTG1etOn6RmIgZv7nRzV-ntfhDm0s5WQrE8Gi9Lf4okhVVNj8zrCLsu_p4esMCoe3beu6mh_ozk1_YMKsxFtKNe2HERURBdt07v_7w23_AxiBTu_GnM1DfejVUr5p20LxOseLvrKWTNCLT5629AIXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5ebf4ec7.mp4?token=qwP9Hg7n3xhP-kP1BBmkaCbY2etJU_zxocmDL-L0tbLmUCFz5EgFW3or00lJ5cjBJfDOLGEpfKfTIOKUwkLgCf2-NxoF4C05cojptvjGEuEsS4FirQ41CRK54qG-3cO-xBrquO9FKiydpYIpwuXW4tA4eLw91gYBeMaO-9RELKKOPOn5vbuqOVsLNenH0LwGZTG1etOn6RmIgZv7nRzV-ntfhDm0s5WQrE8Gi9Lf4okhVVNj8zrCLsu_p4esMCoe3beu6mh_ozk1_YMKsxFtKNe2HERURBdt07v_7w23_AxiBTu_GnM1DfejVUr5p20LxOseLvrKWTNCLT5629AIXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت «کالا والش» فعال رسانه‌ای آمریکایی از ابراز ارادت ۲۵۰ شاعر ایرانی به ایرانی‌ترین رهبر تاریخ
@Farsna</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/447190" target="_blank">📅 20:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMt-1kSf79d6Q7Ny0mKwXzZuRPK95RBfLeXayA9392eaf2Cek4pDF7Vzw2X4lW_FDh1ZcvIZuXO-H9hrjLxbsM09XkwwHxmooBtXo7Pw82dIKvwg2HA3SbVZ8JFpjr-KdeQqI6-P-DSYWMOURLbxB8rRC42dd6fEMdSInNsJeQmQm7mvnmFczFYwnN1_GWQJ-0VFZfCqcHjg7OXbLlYwFMTXPEB9LddAwZKvn6WaZ96O3f4oKvyXz3fUQRI2uCLJcBPshp-CILDJ4FvJvyYpJHb5cUPxAK1qr9quh6gKZ31UAzzrF0CGsIPk8EZ-vEMGM5_qR2X1nrA5QDdR-N_OYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تشییع رهبر شهید در قم
🔹
کمیته اطلاع‌رسانی مراسم تشییع رهبر شهید در قم: مراسم از ساعت ۵ صبح روز سه‌شنبه ۱۶ تیرماه با اقامۀ نماز بر پیکر مطهر در صحن مسجد مقدس جمکران آغاز می‌شود.
🔹
پس از آن، مراسم در بلوار پیامبر اعظم(ص) و مسیر منتهی به حرم مطهر…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farsna/447189" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v56tesAjcQVpj23rsEUZ9YgC2U29ZcYO8qEZ3YJ2Jd7xQ-0O2durMy4bXb9TMt__CXKIYj5h2xUlc2Aa8CQ53lI7N0JK4YbAzbSP8qBmFwV0rLjEHDGK96jBcot58jkJZDH8pMvfcnfLsWDwd19tafSIlww6aofB_niDCvEePEsJhXoGjxmwJ1bcx3rp5r5tcYNnog-7z9rT2Nzo4cUhtfAmZrKluSsmuozRRf0YSnQWxW0dbMnU2mU-RmXnmvE1f_G1yRGDdenDQsc2lZjVTXmzI28iFM-aDeWhbeYGUh5Btpo4U-dz1PQxBmNLZpIeIKVqZwi0je3fCqbRSFRoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ننگا به‌ ما اگرکه ز خونت گذر کنیم
@Farsna</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/447188" target="_blank">📅 20:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43e570ac5.mp4?token=VwbfyWlct2M0-mvt_HagXJO9nNqzOZ-E8CXqPJcptXbIBKXxzfJJ7ECR9Km755952f9YsDHV2DMw_RmWTJxcEDU9JOpBLo8faHBKaSFZpEoZnzQOxKHqP6Ye60S3O3VQfdrY4SR24IpsW58yUkS8-MYMcx01FpgTjwSQ1qmkpNYHGbvzisYo4lU5ZmKAeWvKkg1VqVly5I5o3bens8-N9grEbep7hzEj7P_ZR2EN1QeWuKlzzGL4DLnYg6A2sJgt13XcXNkVCOwCjcjIMDnwdTV9j9y06EC3Cawrx5CiWgYuXSPqppKW2fmRNbQarvd8VRDeyLD8RbG9s4oubtyNtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43e570ac5.mp4?token=VwbfyWlct2M0-mvt_HagXJO9nNqzOZ-E8CXqPJcptXbIBKXxzfJJ7ECR9Km755952f9YsDHV2DMw_RmWTJxcEDU9JOpBLo8faHBKaSFZpEoZnzQOxKHqP6Ye60S3O3VQfdrY4SR24IpsW58yUkS8-MYMcx01FpgTjwSQ1qmkpNYHGbvzisYo4lU5ZmKAeWvKkg1VqVly5I5o3bens8-N9grEbep7hzEj7P_ZR2EN1QeWuKlzzGL4DLnYg6A2sJgt13XcXNkVCOwCjcjIMDnwdTV9j9y06EC3Cawrx5CiWgYuXSPqppKW2fmRNbQarvd8VRDeyLD8RbG9s4oubtyNtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین اذان مغرب در مصلای امام‌خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/447187" target="_blank">📅 20:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447185">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d485518.mp4?token=PVeeZxdhwWsb9xC__XnePIfFLVX0G9Sdtuql3MMUQNKX4SGDUgVuMnR6NiaMKYROJJsSvtSiJBNLYq4YBG6bgYqI_4fdudYC7n6tk5PLDj7gsqlU2sqOabEFv0WyGXy5spNTGGZMUqlqC9E2PLnutFY2VE7qpGSQMOWRdz65j66bvmYzKkgmloLi_HduMHgnu77X6-_sQAhU-ntx5EzXv0LokPHprjub8dqaanDHn-5veOwWWx9-50VdBNJRjJeropLnBGUc9QX0vk01wNeFx8NMtpfsmXatBipI1pbUO90hH-AACviZVtGdsu8TdOAZPyZm_Teo9CsuyCC_PUBotA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d485518.mp4?token=PVeeZxdhwWsb9xC__XnePIfFLVX0G9Sdtuql3MMUQNKX4SGDUgVuMnR6NiaMKYROJJsSvtSiJBNLYq4YBG6bgYqI_4fdudYC7n6tk5PLDj7gsqlU2sqOabEFv0WyGXy5spNTGGZMUqlqC9E2PLnutFY2VE7qpGSQMOWRdz65j66bvmYzKkgmloLi_HduMHgnu77X6-_sQAhU-ntx5EzXv0LokPHprjub8dqaanDHn-5veOwWWx9-50VdBNJRjJeropLnBGUc9QX0vk01wNeFx8NMtpfsmXatBipI1pbUO90hH-AACviZVtGdsu8TdOAZPyZm_Teo9CsuyCC_PUBotA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم | لحظه ورود رهبر انقلاب به حسینیه امام خمینی(ره) در مراسم عزاداری شب عاشورای حسینی  @rahbari_plus</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/447185" target="_blank">📅 19:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447184">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67407e3e61.mp4?token=vbfuV9BBV54MLxbhM29F-8jwUqrl2Asvo2OZ9diG9n20f4IaQQIhG4-eNtD4bz4agm8-kcnm_dOyIcJxzWCgMKtk5374breKEEmvQY6eG8fvsRYtNsL7KHCnI0hNf_wnOG6O8rFJQornBFC9qBjTaTBet6k9Euv3oGOcfB-4MkAZR2CiRku5kFc4zmjISEecs6_i9sQcLtTkMVOexqsDAVyH845L_DhxXPa81WoiZUyzm0TTLs80lOzr3J6IhBqgVKPTQlgKFAJ_K94j6QEk2oSbsrZ5-nPRNLHUIkFilqI4v6gSgoMbH6lqppZ7_uPMx1-JOxI-P94GWUrFsQriUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67407e3e61.mp4?token=vbfuV9BBV54MLxbhM29F-8jwUqrl2Asvo2OZ9diG9n20f4IaQQIhG4-eNtD4bz4agm8-kcnm_dOyIcJxzWCgMKtk5374breKEEmvQY6eG8fvsRYtNsL7KHCnI0hNf_wnOG6O8rFJQornBFC9qBjTaTBet6k9Euv3oGOcfB-4MkAZR2CiRku5kFc4zmjISEecs6_i9sQcLtTkMVOexqsDAVyH845L_DhxXPa81WoiZUyzm0TTLs80lOzr3J6IhBqgVKPTQlgKFAJ_K94j6QEk2oSbsrZ5-nPRNLHUIkFilqI4v6gSgoMbH6lqppZ7_uPMx1-JOxI-P94GWUrFsQriUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ساخته‌شده با هوش مصنوعی از چهره‌ها و صحنه‌های خاص و غیرمنتظره مراسم امروز وداع با رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/447184" target="_blank">📅 19:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447183">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjep0KPlwOUdVV_xKMJ2o1QQThwEWjKtxXEa4vQoMvPOmmdIM7o59wtBsEOSGwtCi70ivyMSIZFhZLRzIy0pBhUnnanQ52X935h6HygGBw1Wv15sHY7OcdRR51grbETs0AzWu3ZrdGdklQgW3sncPcW4xJVmXbQDc2D6Ogr-qh4KsU0UYLAZ9-cCe4WUwZW80aYXcQ_E_zMGfxYSKbOfdzg1SMei7Imay8zrUguoXagXCVoclcbvr3rjGQVuIcmDg8gUqszDM2z5ldvkqPsys1j_cNRcvBG_ojq1yzz5JIzrZTuRGMceF2LZMyj_sEpj7B7h_Avk1f49kQzk7JTHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بازدید مدیرعامل بانک رفاه کارگران از موکب های این بانک و شرکت های تابعه در مراسم وداع با پیکر مطهر قائد شهید
🔹
مدیرعامل بانک رفاه کارگران با حضور در مراسم وداع با پیکر مطهر قائد شهید، از موکب های این بانک و شرکت های تابعه در این مراسم بازدید کرد.
🔹
دکتر للـه‌گانی به همراه جمعی از مدیران و کارکنان بانک ضمن حضور در این مراسم در محل مصلای امام خمینی(ره) تهران، از نزدیک در جریان خدمت رسانی این موکب ها به عزاداران قرار گرفتند.
🔹
مدیرعامل بانک رفاه کارگران طی سخنانی در حاشیه این مراسم گفت: اندیشه‌های رهبر شهید یک جهان‌بینی مبتنی بر کرامت انسانی بود. ایشان همواره معتقد بودند که اقتصاد، ابزاری است برای تعالی جامعه، نه هدفی برای انباشت سرمایه. بانک رفاه به عنوان بانکی که نام «کارگران» را بر پیشانی دارد، بیشترین قرابت را با گفتمان ایشان دارد.
🔹
دکتر للـه‌گانی تصریح کرد: در بانک رفاه کارگران تلاش کرده‌ایم آرمان‌های قائد شهید را به دستورالعمل‌های اجرایی تبدیل کنیم. از حمایت از تولید ملی و اشتغالزایی گرفته تا طرح‌های رفاهی برای کارگران و بازنشستگان. این‌ها در واقع پیاده‌سازی همان نگاه کلانی است که ایشان به عدالت اجتماعی داشتند.
🔹
وی به انتخاب حضرت آیت‌الله سیدمجتبی خامنه‌ای (حفظه‌الله) از سوی مجلس خبرگان رهبری به مقام رهبری انقلاب اسلامی، اشاره کرد و گفت: این انتخاب نویدبخش تداوم مسیر عزت و اقتدار میهن عزیزمان است. بدون شک شبکه بانکی تمام توان خود را برای تحقق منویات رهبری در مسیر اعتلا، آبادانی و شکوفایی اقتصادی میهن عزیزمان به کار خواهد بست تا تحت عنایات حضرت ولی‌عصر (عج)، شاهد سربلندی بیش از پیش ایران اسلامی باشیم.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/447183" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447182">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/447182" target="_blank">📅 19:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447181">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5764e1d53f.mp4?token=vwLvIqEfIGTcT8tUy0Iw3TIQjXEYcQcvNIG5WrYpsWomG1IBkI_yUPzcVR5lzjvIIU1TEbxUnq6LCAbjA9V4y6l7VVBY74FSwVYOdYl99Luzqpg8mruVzh69avJFR2e6vM4i280pgMq2yTHLJ9uCKW1mxRdXKC5KeMuASXPx_e_7o5fwZBB3gyNMpOzF3oonGEhLe91OyfDpS2VEjyXL0T9NE3b0UKKdJ1qd-xQBy51xCoN4DHO9AbUK1z8LdsSqnyzDWl2-DBmMCm9c0k2L2eNPiApb-2vz7BzDBcNrV2Yi26HtsVUKPcOWCVkWV-hlYrJ1Ybrsn426hsliVt5Ddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5764e1d53f.mp4?token=vwLvIqEfIGTcT8tUy0Iw3TIQjXEYcQcvNIG5WrYpsWomG1IBkI_yUPzcVR5lzjvIIU1TEbxUnq6LCAbjA9V4y6l7VVBY74FSwVYOdYl99Luzqpg8mruVzh69avJFR2e6vM4i280pgMq2yTHLJ9uCKW1mxRdXKC5KeMuASXPx_e_7o5fwZBB3gyNMpOzF3oonGEhLe91OyfDpS2VEjyXL0T9NE3b0UKKdJ1qd-xQBy51xCoN4DHO9AbUK1z8LdsSqnyzDWl2-DBmMCm9c0k2L2eNPiApb-2vz7BzDBcNrV2Yi26HtsVUKPcOWCVkWV-hlYrJ1Ybrsn426hsliVt5Ddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رهبر شهید از آخرین دیدار و وداع
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/447181" target="_blank">📅 19:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447180">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f3b783ad.mp4?token=VPAOK2NCmIro_XW_Ty_hWG-33957ACx1nDhFtVwfgvSVQb9bQIGHz2dg0SbBk50zRMN5QNib0J46bGUV8VmAyuafe_-bEVJEE98UuE-80v4w_I18kVyJe35wyfD9jX_auklpTYySCgW5k_zXlYg--D9zjTdK0CNSGrPxuexIfTVTQtcvqAkc9ikeYRc6Vdg-2Zz5gBSzj5l0lXzqksTmx-i_JpM0-iun1nbYkLpaquNHwhXTCpThsgHmhvD7Ga_iCSGqGvgUKEgKgiVyK23PbQnjz_LFF1ncAvhN16sb69EV__qwUDf6rY2N3NUKyRg7Z32eUhUYZIedUSuUwFgNuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f3b783ad.mp4?token=VPAOK2NCmIro_XW_Ty_hWG-33957ACx1nDhFtVwfgvSVQb9bQIGHz2dg0SbBk50zRMN5QNib0J46bGUV8VmAyuafe_-bEVJEE98UuE-80v4w_I18kVyJe35wyfD9jX_auklpTYySCgW5k_zXlYg--D9zjTdK0CNSGrPxuexIfTVTQtcvqAkc9ikeYRc6Vdg-2Zz5gBSzj5l0lXzqksTmx-i_JpM0-iun1nbYkLpaquNHwhXTCpThsgHmhvD7Ga_iCSGqGvgUKEgKgiVyK23PbQnjz_LFF1ncAvhN16sb69EV__qwUDf6rY2N3NUKyRg7Z32eUhUYZIedUSuUwFgNuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاضر بودم ١٠ بار بمیرم اما یک تار مو از رهبرم کم نمی‌شد..
.
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/447180" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447179">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ca1bcfcdc.mp4?token=hMlybOekSZkO1dXq2XGmFsKwW4n8dfRa0QJshjDoEETV6OKLjzTDDRhCVXLBPReGClNyb4ADq1ZRwh5qJDjJcj6TumWC7nuUTFF7ZMovyC9iYCue0k57bRh3aEchcxgdzjMwvy0Xe0NyoDmT2Y0vCON5_yixDMRDrq5OrmX-JCMLShqvQi1iRhkbD-IL3zTJFi0Yuqm1yJgeN-jFciqhw5HhZbDZWAjmwvSp0Zb89pDZdYKWSX0sC7AyCeua3O2PWz_tH46Lqb6IyD3SyLjgXO3YZnBHLeNnS3GUuV35e0Cvp2cAHBfUXv80sxK64bN-GQeS0-wsk87J5a5pVvzTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ca1bcfcdc.mp4?token=hMlybOekSZkO1dXq2XGmFsKwW4n8dfRa0QJshjDoEETV6OKLjzTDDRhCVXLBPReGClNyb4ADq1ZRwh5qJDjJcj6TumWC7nuUTFF7ZMovyC9iYCue0k57bRh3aEchcxgdzjMwvy0Xe0NyoDmT2Y0vCON5_yixDMRDrq5OrmX-JCMLShqvQi1iRhkbD-IL3zTJFi0Yuqm1yJgeN-jFciqhw5HhZbDZWAjmwvSp0Zb89pDZdYKWSX0sC7AyCeua3O2PWz_tH46Lqb6IyD3SyLjgXO3YZnBHLeNnS3GUuV35e0Cvp2cAHBfUXv80sxK64bN-GQeS0-wsk87J5a5pVvzTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین قول‌وقرار حسین یکتا با رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/447179" target="_blank">📅 19:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447178">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4wO8b8Pb8RwUt8RUt6gyaRYjozdFEMKa6VVnH70A-tFaVjvnp6WV9s5QXA9yrWgPswng4Ybo7k-JiJw_d4tYRQ6mhuP7SsiDnWllMJdOKje0BWQMWXUojNTSlI0EzBEoEKmS3sQtzDt9-0krZo2_63xG5vof24Fe9iviPVqrfqA9Db8WCEGo1V-eiuSqL4Ht0osqRoNKzt6YJNExULJTPw8yyBbc3IcGMMKzeFL0PS6loO9q5KdsiF6cumY4w9lMOI4GMgYoL4H3ynw3L05seo0NH_hrgpQpTt-R-ucg6z82lycBSt3TwRV1H3JSO9PletWzsNO2OK90j33FEmbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌قضائیه منصوب کردند.  متن حکم رهبر انقلاب اسلامی به این شرح است:…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/447178" target="_blank">📅 19:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447177">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
برنامۀ وداع در مصلای تهران به‌دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/447177" target="_blank">📅 19:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447176">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک استان دیگر عراق روز چهارشنبه را برای بدرقه و تشییع پیکر رهبر شهید ایران تعطیل کرد
🔹
استان مثنی عراق، نهمین استانی است که روز چهارشنبه را برای تسهیل مشارکت مردم این استان برای بدرقه و تشییع پیکر حضرت آیت‌الله العظمی سید علی خامنه‌ای، رهبر شهید ایران تعطیل…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/447176" target="_blank">📅 19:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447172">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ikqEI2Zgav3TABhPr8Exre2soVAevZjpA3Y70V0F9m8pCpplaVkJOQnBc-Dja56M9xZns0-SeiNZuH-FXNlV9awKlWyErTDEnl9cBv2m09JPcJUe0Hm6n0oPd_AYUeG2r9T_U9bfDy8wsxelzBjGvTY_4ENvnsG5JiSKwHjog92pJl9qKSjct337hAR4IYwXSCNfG914Pu5jqkgS7-TG5oJsOwVlzaui5OJF_y_nU3fE_qc9OHlRyptROLvdbnqA0OlsALrstXkudHFDwOWKA3SwdgVkOxl22DJUU52wm9ZKAUt8ElgM-5v1uHdMBl30ZWHR-1XVZLpgI4iszy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌قضائیه منصوب کردند.
متن حکم رهبر انقلاب اسلامی به این شرح است:
بسم الله الرّحمن الرّحیم
جناب حجت‌الاسلام والمسلمین آقای محسنی اژه‌ای دامت توفیقاته
🔹
با قدردانی از تلاش‌های ارزشمند و صادقانۀ جنابعالی، به استناد اصل یکصد و پنجاه و هفتم قانون اساسی، جنابعالی را به ریاست قوه‌قضائیه منصوب می‌کنم.
🔹
مجموعۀ مطالبات مطرح‌شده از سوی قائد شهیدمان اعلی‌الله‌مقامه‌الشریف و نکات مذکور در پیام هفتم تیرماه ۱۴۰۵ اینجانب، راهگشای تحول، شکوفایی و دستیابی به قوه‌قضائیۀ مطلوب است.
🔹
امیدوارم با همت مضاعف جنابعالی و قضات شریف و همکاران ارجمندتان در دستگاه قضایی و دعای سرورمان عجل‌الله‌تعالی‌فرجه‌الشریف، ملّت بزرگوار ایران از نتایج آن بهره‌مند شوند.
سیدمجتبی حسینی خامنه‌ای
۱۳/تیر/۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/447172" target="_blank">📅 18:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447171">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571f3614bb.mp4?token=dTvisllvuiE9TJFUqmQSVUMALfkmNZwGWktPXsdxpBfN5so7NCcd2HhJQgywmVANxk3qGpvypl6b2BVVs_1kBnQkv1Kkmo8CIf0jfQ_XNGOHPG9CwXGKzUOT1b7GyVvn2NHiLuQ0xNdcqMS6z0ncaYd16V3BuSrBA1HO9YFBGFGzuZBepCn8d044LanbTa-Sq73J04V6asyrkUPHU3IYHjiLegYDKlcOGuOwoimHPwzK1i0MGsiSc-4xlnxuOebxJTvwPVBsmBBEnMs8FQmh3cPSUf5aWkas_6cuuX_Y7px07HM08mHZ4lx2jX-rmx04dK0cau7dZxDGetWdguRhhbIukRvdamQFuPti331JPEcU86VgeVODNlghjYT8NyBrCvvAfHdGdX7dSRysri00khgh_-_2uCs9gN6uffLetnSEZhpi5Np4xl8FaeY0ydVSpR3eJSLNSBMAaUpAMEKCu4kQZd70UsgRMnJ4UBJtZ6kUkAMThxDPe1qD0qug11WE8s_NG4uNBRjuJMKPJ0J3rtbB7HCdjykitLcwE8hozMDSeTWHJ5_2zWJHuBfh3-7DiB4H1wcttBWUIZAAkjYWHl1wDK4XmjPCpzN0aXTcOQF-7JEdx9FTHsPydJO3JjQ9APE51SbXG1OO9rfU_ukpqJRYVZPxXm9jYuc551tu0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571f3614bb.mp4?token=dTvisllvuiE9TJFUqmQSVUMALfkmNZwGWktPXsdxpBfN5so7NCcd2HhJQgywmVANxk3qGpvypl6b2BVVs_1kBnQkv1Kkmo8CIf0jfQ_XNGOHPG9CwXGKzUOT1b7GyVvn2NHiLuQ0xNdcqMS6z0ncaYd16V3BuSrBA1HO9YFBGFGzuZBepCn8d044LanbTa-Sq73J04V6asyrkUPHU3IYHjiLegYDKlcOGuOwoimHPwzK1i0MGsiSc-4xlnxuOebxJTvwPVBsmBBEnMs8FQmh3cPSUf5aWkas_6cuuX_Y7px07HM08mHZ4lx2jX-rmx04dK0cau7dZxDGetWdguRhhbIukRvdamQFuPti331JPEcU86VgeVODNlghjYT8NyBrCvvAfHdGdX7dSRysri00khgh_-_2uCs9gN6uffLetnSEZhpi5Np4xl8FaeY0ydVSpR3eJSLNSBMAaUpAMEKCu4kQZd70UsgRMnJ4UBJtZ6kUkAMThxDPe1qD0qug11WE8s_NG4uNBRjuJMKPJ0J3rtbB7HCdjykitLcwE8hozMDSeTWHJ5_2zWJHuBfh3-7DiB4H1wcttBWUIZAAkjYWHl1wDK4XmjPCpzN0aXTcOQF-7JEdx9FTHsPydJO3JjQ9APE51SbXG1OO9rfU_ukpqJRYVZPxXm9jYuc551tu0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانشجوی نیجریه‌ای: مردم ایران دمتون گرم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/447171" target="_blank">📅 18:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447170">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa5a4fb9d.mp4?token=f4X9NVxRD8UwxbBnbsdksBcDpwuavotzKm0NxUF6DSCKhtdXtMqjg8e5j3qWlzxmUEmsuJ1WW8ejCE5Jis8e-ll2OvqBzP-wZ1Nnxwqm_Ci5mW8N8Rz226bYNONQ1acBevgJblg7_G9pbkcvBQD5ZqG-5Dmcilh0vpptJc-GfnYZuGRuYSPrfBoRXFUQhmv0Wk8tnKAOsg4mxcd6yyyu3sOqlsd_1VPDVql_6V22jmKGuTr_AxhHWySFqupIaKQvJeFla5cD4ktNZtxUSL9jix8DUlo7ALKntAL12G85tElEJBhWVRAl7-SY2XK2QYY4xQExF2X6w8SqwHyNUDRznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa5a4fb9d.mp4?token=f4X9NVxRD8UwxbBnbsdksBcDpwuavotzKm0NxUF6DSCKhtdXtMqjg8e5j3qWlzxmUEmsuJ1WW8ejCE5Jis8e-ll2OvqBzP-wZ1Nnxwqm_Ci5mW8N8Rz226bYNONQ1acBevgJblg7_G9pbkcvBQD5ZqG-5Dmcilh0vpptJc-GfnYZuGRuYSPrfBoRXFUQhmv0Wk8tnKAOsg4mxcd6yyyu3sOqlsd_1VPDVql_6V22jmKGuTr_AxhHWySFqupIaKQvJeFla5cD4ktNZtxUSL9jix8DUlo7ALKntAL12G85tElEJBhWVRAl7-SY2XK2QYY4xQExF2X6w8SqwHyNUDRznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پناه اباعبدالله، زائر کربلا
◾️
نوحۀ وداع سیدمهدی حسینی برای رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/447170" target="_blank">📅 18:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447169">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b7196f32.mp4?token=mS2YULWkSRLoBaVSaRcGwCbD9YZmdAC-CEcC48l5WZDuGwoLHYHQpm726a73EC36wXmDUw8JsV7TLVHGcW3t0BREYcMalF94GC2GtEzJAuLrJhmrvIqJymCnylv2Gh4HjvB2EwoNSZV6KhZm6dm_XEIy3Tp9BXxiUU1Dz7TXo9UdrKjnJ48BbDi4-TDSI3kOrOdA4ZaeEnyfbIn1-FtveA-unab8zYuJzB1052Y9MxpEHMmcKBzP0YIj8-F2AdiRwMZC02toOuu7e7GHuU2Poj63JO8JsWLSMT8G-IdhPfNXddFwvJuyRA-5NDWEJJLzL4gwPMD4hQfvQTz5IyR05g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b7196f32.mp4?token=mS2YULWkSRLoBaVSaRcGwCbD9YZmdAC-CEcC48l5WZDuGwoLHYHQpm726a73EC36wXmDUw8JsV7TLVHGcW3t0BREYcMalF94GC2GtEzJAuLrJhmrvIqJymCnylv2Gh4HjvB2EwoNSZV6KhZm6dm_XEIy3Tp9BXxiUU1Dz7TXo9UdrKjnJ48BbDi4-TDSI3kOrOdA4ZaeEnyfbIn1-FtveA-unab8zYuJzB1052Y9MxpEHMmcKBzP0YIj8-F2AdiRwMZC02toOuu7e7GHuU2Poj63JO8JsWLSMT8G-IdhPfNXddFwvJuyRA-5NDWEJJLzL4gwPMD4hQfvQTz5IyR05g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقهٔ ۲۵۰ شاعر پارسی‌گو برای ایرانی‌ترین رهبر تاریخ
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/447169" target="_blank">📅 18:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447168">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d6aad76b.mp4?token=Stz3eb2lAYeMqwWIRUAmixZoyOptoPOH5zVnGbImoiYtwZ1tBXkY8jPHmmnbZeh4m-G62KOU8Z5m6C-iSkRTl6KiJ4GK09zSv1QFi6m6dzBMRo25ej06iRAq6Vz2UlEUt1jEEvZzhaUP4mBDZeYWFHTxq0mhoBlTF656o2hhlj5yi7rqsn7afQ2bSDIC1f7bpyIck6tDHI83ZhpwXJiDj1pvLTryIMw3DUQGwY8tgnfnQddvc3_DMxbv3FiadXvMWFHlt7dhI67CWnpcEqPWxbmfwi_ZEwQ8ydDRnHwtjCqpOdIshFtVxvizfhfzFLpCCzEuwBqjX2nrFbfskhHdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d6aad76b.mp4?token=Stz3eb2lAYeMqwWIRUAmixZoyOptoPOH5zVnGbImoiYtwZ1tBXkY8jPHmmnbZeh4m-G62KOU8Z5m6C-iSkRTl6KiJ4GK09zSv1QFi6m6dzBMRo25ej06iRAq6Vz2UlEUt1jEEvZzhaUP4mBDZeYWFHTxq0mhoBlTF656o2hhlj5yi7rqsn7afQ2bSDIC1f7bpyIck6tDHI83ZhpwXJiDj1pvLTryIMw3DUQGwY8tgnfnQddvc3_DMxbv3FiadXvMWFHlt7dhI67CWnpcEqPWxbmfwi_ZEwQ8ydDRnHwtjCqpOdIshFtVxvizfhfzFLpCCzEuwBqjX2nrFbfskhHdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک سلام برای بدرقه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/447168" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447167">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjdN9IYlc3YtEW2Qw8n_Cr6dvT7euaHx3bWEHu4Vc1mR5oF24bx7jYc-PCEI-PHgMvZmpHUkViqASQhHQqRygsAdPWgJzGwVtj9Uxf2jvJtFDOi0GTxDM28HLzyyivddQH9ZIxJqcFxEMFoazEVwx7JMxWk4J8I3MdCELP8DFLAu0NCKb-w_X9CEqak0dFs7h6AUC8qPCNogMc-T100FkqI-KyXtnW1JtgpCVrfNclg75AYo9tCC7NIZRyANj0Fx2g3xKj7l2NVDGzRMXuqrTkQzuv8PlFtwtkmDmkVKupysBjT6YwfM-3sZap-FQ_DVkR-MR97-_Eips8OvXOzOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آیت‌الله عاملی: شرکت در تشییع رهبر شهید به منزلهٔ کشیدن دندان طمع دشمن آمریکایی-صهیونی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/447167" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447164">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خروج ۱۱ فروند سوخت‌رسان آمریکایی از غرب آسیا تأیید شد
🔹
هم‌زمان با انتشار گزارش‌هایی دربارۀ کاهش بخشی از توان پشتیبانی هوایی آمریکا در منطقه، برخی تحلیل‌ها این تحول را ناشی از بازنگری واشنگتن در ارزیابی خود از تاب‌آوری جمهوری اسلامی ایران و واکنش‌های احتمالی تهران پس از نمایش گستردۀ انسجام ملی در مراسم تشییع رهبر انقلاب می‌دانند.
🔹
درحالی‌که گزارش‌هایی از کاهش بخشی از ظرفیت پشتیبانی هوایی آمریکا در منطقه، از جمله خروج تعدادی هواپیمای سوخت‌رسان، منتشر شده است، برخی ناظران معتقدند این اقدام می‌تواند نشانه‌ای از تغییر محاسبات واشنگتن باشد. یک منبع نظامی به فارس گفته است خروج دست‌کم ۱۱ فروند هواپیمای سوخت‌رسان آمریکا از منطقه تأیید شده است.
🔹
عبدالرضا صدیق، کارشناس حوزۀ نظامی، معتقد است آمریکا پس از دقیق‌تر شدن ارزیابی‌ها از پایداری و تاب‌آوری مردم و نظام جمهوری اسلامی و دریافت گزارش‌های متعدد از حضور گستردۀ مردم در مراسم تشییع پیکر رهبر شهید انقلاب، دستور عقب‌نشینی داده است.
🔹
به‌گفتۀ این کارشناس نظامی، آمریکا پس از دریافت گزارش‌های متعدد از خشم گسترده و کنترل‌ناپذیر مردم در مراسم وداع با پیکر مطهر رهبر انقلاب، نگران واکنش احتمالی ایران شده و در صدد کاهش تجهیزات گران‌قیمت خود از منطقه است.
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/447164" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447163">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374c4ece7c.mp4?token=XTd4w2sRsyz8YWrRY8c_AMJqdmPC6LCmU4Y-R8ZAoH79w2JwGfUAiOH-_n9k_ecmvESl9QbjOY7N4144MvaVexYS656bPI0OSprxP34UEmACu-2kSBfmF8DTp4foFn65d9EJjwX0Zrd3VYwJJP_pDAfZEmbg2MEjHDZwZ6GQNY1Bn2io7pxXnMh_febiRIc_qcX_sXejgij0XC3tZCjCr0ozH1y-4_TH90E2kHK10d7SJRndC_-RSAeWZgsK24Y4Hjcm2vXBlYxY_sbWAaCxxlRRw-R-brt2tu_eBr9_Tm1fc91OO4PPKezX6Z3lWZoaZmmjNY9ecYFGcCRAjyakUZQzp5KtORGjzn5E2LuupS2LvJ29jYwXvT6JRaSFfqdqMDkvatSFDrPDZrjKnFfBYSYrcrEgCySvxZl-aW8D_-7coXqET6jS9rMmeKU3SoP0ZB1EqftCNgoypGdHyS0ghglJ9iQq1nzm8hSX81LiYVHrD5CL8810zFUgC6O8KH8wKW6XUHCA8SBcpwEViVqr2DyVr5J4eV_0J6aKKeNHpbcvtZBn6EtOTpasjoJ-YWAA2xs9pi1HMN51JeDl6dRQuZsrFTSgPSsjXWcT-GYUOGCFuANTKi5bCgVR58wGv04bxC1CPtEPyjJrKz_9-2_6YYlasFn-bPcPKwYXxm3P3cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374c4ece7c.mp4?token=XTd4w2sRsyz8YWrRY8c_AMJqdmPC6LCmU4Y-R8ZAoH79w2JwGfUAiOH-_n9k_ecmvESl9QbjOY7N4144MvaVexYS656bPI0OSprxP34UEmACu-2kSBfmF8DTp4foFn65d9EJjwX0Zrd3VYwJJP_pDAfZEmbg2MEjHDZwZ6GQNY1Bn2io7pxXnMh_febiRIc_qcX_sXejgij0XC3tZCjCr0ozH1y-4_TH90E2kHK10d7SJRndC_-RSAeWZgsK24Y4Hjcm2vXBlYxY_sbWAaCxxlRRw-R-brt2tu_eBr9_Tm1fc91OO4PPKezX6Z3lWZoaZmmjNY9ecYFGcCRAjyakUZQzp5KtORGjzn5E2LuupS2LvJ29jYwXvT6JRaSFfqdqMDkvatSFDrPDZrjKnFfBYSYrcrEgCySvxZl-aW8D_-7coXqET6jS9rMmeKU3SoP0ZB1EqftCNgoypGdHyS0ghglJ9iQq1nzm8hSX81LiYVHrD5CL8810zFUgC6O8KH8wKW6XUHCA8SBcpwEViVqr2DyVr5J4eV_0J6aKKeNHpbcvtZBn6EtOTpasjoJ-YWAA2xs9pi1HMN51JeDl6dRQuZsrFTSgPSsjXWcT-GYUOGCFuANTKi5bCgVR58wGv04bxC1CPtEPyjJrKz_9-2_6YYlasFn-bPcPKwYXxm3P3cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار آفریقایی: باید بگویم ایران برای دنیای اسلام قاطعانه ایستاده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/447163" target="_blank">📅 18:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447162">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b99a21b25.mp4?token=rIAwqZKJLisZB_PNw6ZvOoxhU92g4NgXkis1rCNnotYCRVXBS15nTeK5Nqle-fWCMQg9QippRiCR--u-96a8hQW9Is6XMde5zv8U4gefRRI0I5p0AaTHmgfXfJjFGAUJshwl2vS3uaePnwmO5qUHKGmTxl8KsGkMX7ontQrRhZNrdNm-MIpkxt56FpBsrpRt7Qiv7qFkQQmXDzkZ2rrS1aAXu1cGFJkWShjFdzsgX3J6tkWVBG1qprE3REy36szgR_hDQFx7h4Eiid9aXSy1CNWG11r4Mi-bL3UIBc7Zl0yPtk1prOQ9wu956BiE8nKvcddZJpZDLSZrV82PmcbjjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b99a21b25.mp4?token=rIAwqZKJLisZB_PNw6ZvOoxhU92g4NgXkis1rCNnotYCRVXBS15nTeK5Nqle-fWCMQg9QippRiCR--u-96a8hQW9Is6XMde5zv8U4gefRRI0I5p0AaTHmgfXfJjFGAUJshwl2vS3uaePnwmO5qUHKGmTxl8KsGkMX7ontQrRhZNrdNm-MIpkxt56FpBsrpRt7Qiv7qFkQQmXDzkZ2rrS1aAXu1cGFJkWShjFdzsgX3J6tkWVBG1qprE3REy36szgR_hDQFx7h4Eiid9aXSy1CNWG11r4Mi-bL3UIBc7Zl0yPtk1prOQ9wu956BiE8nKvcddZJpZDLSZrV82PmcbjjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ هوایی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار: ارتش رژیم صهیونیستی شهرک النبطیه‌ الفوقا‌ را در جنوب لبنان هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/447162" target="_blank">📅 18:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447155">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZcPjVFot6-0cq-muKRTOPEfApGpK80s6H58w2W2z0F38YSNvOCCcioCq0J2EoYi_Z0XJqhJo3yPalSHSOZLpqzOiyafzP7u6T9NQP3M1XlC99E1AY0HIwpH4S9j1d7vvqxDZSt9fnHxiYzwJR1RhLngkzKUIJM4pHvaj_leQSKnyaro18a8w7QcuMAn0PxR3AVSVuZNxsgvWzULAR_7foc1PvPYA5DeUWPxYToJZ9uza6YAhnHGSyBzQvhMhYllQ2-S_15zItXPN6MJRM9FRCQeGIyUbtb7m9yb2-RTU8oP-6qT9nVE8zyHaN0P173Jy7Y9pSvTZDWGcjTdYV-Q5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlaFnoAlUgmSzDhiCidfgp1FeLZnbX8qT3xDMmk93urLujKes2EQ_4SF4TA0ZfAbOJwB0EVbTN4DSFh7vAEwXRWpdbAlleeMqSiWZB882KW9NRvoBwbwLtBHXix9kpPlOlYKm1arTfEB4RS14cBmU22XLUVuhIcBbTd1WhBv-bBdmrlqfQABRlXz4sSTZL0hC_Yjp7kMiuMiI6bI8JY4E4kt9-0ejcvkiF0vlOsAcAD8dKLsQbwRkM-FbOalhCn5W69vj2tytbJxarXsczNfn5FFTFlFFmS1LyEiJXdH_bXPUb-ug0qhL04UUBUAezlwemqCKo_8m3mN_5EDXhSdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBxoeDf5Zz-L9TwcQ82d7dRvrH3Pyyu9AhFzYp6uaJngyVJBxHedn-UCS3obAc9xQZqFZ4_AmmZksPFc6Ys_UGeJEB_pCkWRtHuFxmR5WJpSmovfn0ij_jqYbO9Rr1L9nou_pdKiLg3Xhjf9hfJN_7XC3P4WgXTVm2XI-q5_haSJxPn_wc2w9ee-x6YrPgVT2ocU0yraeRLN3jXablgEyVYWyNl5Qne3DyyCEzlwsYaHj80aykJIU9TOC_Rlp9PFeUzssi-zY0Z051BoYiuzI-p1-89qfcunNC70bCBWGhj_CbDqxblS9s7MO-C9WuNHA31yNDVtt_UDxN239AscpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pca6YI1MdWOtYQjQUuLSeEc0DfZGdkqZX37imyl0bMBu9uSJvoxB0twoQfWowyzbMMHtQaFSAZcJzC-qdKrhzVTusyvpwD-uvfcQp1PC4I2gu7NDlL-ck9Gfnt1OimfsKwKrBXBubDKPGL02JsFvCr2Thn4DYRf3YGtMIcN2lJPWp-v3Ygs88WM91jXbvfkRL2mLUEEM0mI-TEMjSz20zmNX2IESHeK-HqMUhyicjCcr3cvTpBWcufMwQjXR8HIrOP8T-pO0AelvdVVR4TVfVc2sEBLAbhsUrJw7Ho8dcajbwWPI_Cm1c871YgspSagZT_8tNErUaMUJ6BdPg1FCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXLsiiwBICuKLvT0bPkvt0j6UJCTBhmqhhV2o2gYUnbAJ0daGXMnQSdWno4MozjtAjLCG2AvCzWlZzUBWJg6C1K_ew7AA-2zxXs_zIkNN6lu1OcuLBFAl2oxGPzmFilNssm2RApZeLpRKtSLRlrkFA-0iTlJntHMlVlUXSfno9xtEjKXSa3ybGvHsR9TbtjpCBz355O0mkQCJu6_t0PF8sg1jkNY99A79N-LjGWsOxEK5W0VeMGgKSOtzc1mjb7C6Sv7DO_a6Js651VsO_U8JfvxxBgnhXaQThRhof9untrQpU8DQze5QdKjydLtHQsX1q-_NTNRFoDylOylSUs0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6l98uIa5_ZdQt0TuTomctl1Pt3mmffw90k4Vmq4hitgI_h3Kc4zhtUcZTIBrgRk6OcNXfSWq5TZuFM52GqhTsgVXvbrKq82L0d3fmmjazKsq15uTL5Wj0dmwibqSjyF8v853dN1ozKMtKYZtziG1BqZmTdfUyHos6IlzClhAn-rpZgOfOy9eYzxmvHQcogt358rJzwPR1h8OrrmRR39AtOWPJp5wsFRFo3HzcSvtwZFkxUqrF9hrWm6WSKFZsruRm0C-LszqtdKF6oLOGi_rjeP5Jyo-zidmj27PL6epOsZFzNv8KMUMAi0a4i6_KehhwASEWUciG_Sj3VgHlIVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFaVwefkv8QCLH7d3lf42bPNoi20_MP-la1e27D2L3ldyM-4hCInivFJHBxgh4YLru4oan-eL-FEPH3ETqoauItEUHfpR_-oSUQSeaLshiSn0qHPpR53FdvJKq-H0oND8IBywq9QWbYZKBzz04Mjub7qP2QbMNWLGNJZ-i7R3lx89fFt2h8oKdeOd6Itpg_f3x5yp6oOLMDh7HMgIDe9kgEDnecBdRiAsujn76hdk5pw8qJQ0vr0Z5aUtmtuEaRtfZOw9rHbUoJa6piGi2uLJM1O5k-QsQFa5RIjKAOAgq5Uq9ra5FItwoHtgC3Xa41c_xQqWjTMvK4jG2HWuuoJqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجلی وحدت امت در نماز بر پیکر قائد شهید
عکاس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/447155" target="_blank">📅 18:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447154">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZaok-xJzaDuSmkpwGFI1ffD1g5OTR8f93ITtgoplYXjwy4jUZsAO1NwZVlcMkSyAXfCMzjt0PvhMFa-42hQwp6wltO68266fSBMAelzpgca-MZA8nOyy85d9QSq9IETmROrSJnFHcBotmVO7ASLagK6N2sP5b3PtS5Oc75dZVN1RPdVLmuOniKMkCqel8EvNCvcBKaPsopoi30sWV20W976KnYOq2lPlPeG9EkKNsW0HQZT2BM865E_FkiLgLbD1JLR-tSIY91u5tpyD3y4mGvOwEENhO0ZMoceCR9vGMjEmtX_Jn-HBAyuivoxe31fj_wGOMuuC8IcdiCwvgbBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دیپلماسی به دنبال تثبیت دستاوردهای میدان است
🔹
رئیس مجلس در گفت‌وگو با‌ محمد درویش، رئیس شورای رهبری دفترسیاسی حماس: دیپلماسی و مذاکره باید بتواند گره نظامی را باز کند و دستاوردهای رزمندگان را حفظ و تثبیت نماید و این مهم زمانی محقق می شود که کشور در کنار دیپلماسی، آماده دفاع باشد.
🔹
در آن شب که رژیم صهیونیستی به ضاحیه بیروت حمله کرد، مذاکرات به نقطه تعلیق رسید. به طرف آمریکایی تاکید کردیم که تمامیت ارضی در کشورهای منطقه و خاتمه جنگ علیه متحدان ایران در گروه های مقاومت، باید جزئی از تفاهمنامه باشد و به متن اضافه شد. امروز این تفاهمنامه در حال اجراست و پیاده‌سازی آن سخت اما شدنی است.
🔹
ما با آمریکا صلح نداریم و اسرائیل را به رسمیت نخواهیم شناخت. طبق رهنمودهای رهبر معظم انقلاب، به مسلمانان و جبهه مقاومت کمک می کنیم. این کمک، در صورت نیاز با موشک و اگر نیاز به فشار سیاسی باشد، فشار از طریق مذاکره است.
🔹
رفتار دولت‌های مسلمان در این شرایط بسیار مؤثر است. امروز آنها متوجه شده اند که همکاری با آمریکا و اسرائیل برایشان امنیت نمی‌آورد.
🔹
همه ما باید با خدای خود صادقانه عهد ببندیم که برای جهاد و شهادت آماده باشیم و همچنین آماده شکست دشمن؛ هر کدام نصیب شد، فوز عظیم است.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/447154" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447153">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0881a318.mp4?token=heSRQcR1hCQYtpHAk26A_yY7jrSPiXoE2j4o-0xT0GfJ60YjAg3llcVHORAodY3ul9AVTzdTcz7QTgPEYI1wMXnN4VpFUr9Moa70dEpwRocDfHb9ESGWAExFcCE3PuBaaN3NUl-9Sahkx2JtyhQzMzcNPlSEJTtVJ3A4LoTF0boai1-7JsTWDnLfbAnwwO3iwlgIHxomhMw-9Xq4fR-GI-LrN3QjfZqbKIZNWfNetPW5bT3uDtDuKtHs30NJiUSNBBkkaEXHAjSlObvoZq0nAnInGRa4BoMUyqk4Jbpnw-6VdQUw8S44qydOrX1rJVSm6qLLm_t_GVw0y5n3ckftZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0881a318.mp4?token=heSRQcR1hCQYtpHAk26A_yY7jrSPiXoE2j4o-0xT0GfJ60YjAg3llcVHORAodY3ul9AVTzdTcz7QTgPEYI1wMXnN4VpFUr9Moa70dEpwRocDfHb9ESGWAExFcCE3PuBaaN3NUl-9Sahkx2JtyhQzMzcNPlSEJTtVJ3A4LoTF0boai1-7JsTWDnLfbAnwwO3iwlgIHxomhMw-9Xq4fR-GI-LrN3QjfZqbKIZNWfNetPW5bT3uDtDuKtHs30NJiUSNBBkkaEXHAjSlObvoZq0nAnInGRa4BoMUyqk4Jbpnw-6VdQUw8S44qydOrX1rJVSm6qLLm_t_GVw0y5n3ckftZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال خادمان موکب میناب ۱۶۸ از خانواده‌های شهدای دانش‌آموز مدرسهٔ شجرهٔ طیبهٔ میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/447153" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447152">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277794b746.mp4?token=Vtk4lV82nkzd4UQ4JwfMfGSAhHqkof8qGMJ5Ekt13kYSstZ2OmsVzCXmJPUx3b6nC0lb96l_jTDF3sNxCLv_6sCYgWd8OKvuCMr-RbJq1G39v0mLG0cZDT0ZlFLBqjzuHUI35BnfjMo1fitHizJj_aL2DtzXONcSW8zckFBbntsFsKi8mdhRfAP9w8qfJLJAmpYT3Ke52zg-KktFnkOj51skaGJjNTmbuUBSGRL8tIHcUo4g4mdubLGHMskuROmbdH54Y8DTz-4OY8BwLYWMzGTBaA7Ec13ScckKRXmRnFb8HzOVRIPRm1ppVy-r8V-6KRrXQ4kYK29LFYmX9DknKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277794b746.mp4?token=Vtk4lV82nkzd4UQ4JwfMfGSAhHqkof8qGMJ5Ekt13kYSstZ2OmsVzCXmJPUx3b6nC0lb96l_jTDF3sNxCLv_6sCYgWd8OKvuCMr-RbJq1G39v0mLG0cZDT0ZlFLBqjzuHUI35BnfjMo1fitHizJj_aL2DtzXONcSW8zckFBbntsFsKi8mdhRfAP9w8qfJLJAmpYT3Ke52zg-KktFnkOj51skaGJjNTmbuUBSGRL8tIHcUo4g4mdubLGHMskuROmbdH54Y8DTz-4OY8BwLYWMzGTBaA7Ec13ScckKRXmRnFb8HzOVRIPRm1ppVy-r8V-6KRrXQ4kYK29LFYmX9DknKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بلاگر ایتالیایی در مراسم تشییع: ممنون ایران!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/447152" target="_blank">📅 18:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447150">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/987972e43e.mp4?token=V2NTXTURYuzW6aYMLSlISfW-DpxsJ8mOlVZfoaeplEeAav5cd_e3m9HC0yl2xy_xqRdxLo9J6sNev6KaB6niNmZMd6UwQc_DjXJVpSBYfmXLWZJh4je_PLuctzPfpV31sM6Zz-6PeQd_B5leMq5Ld9nGrJ_s63oypcetPr2KMAfgy0BkPJ_OR2sss3vvDpmrWmpjwB0TJCGLre-a0OXcnsy6imv5HMdK_Wp5DFXxTGc1EY9fJtDIDPRRj5k6Xwfn59X_1ukrwWSd-Ttmtk6rOWZnL7trz_hen79R5d3IaMCECSnsM3tJ65gnvZV_Cwbr_Tl_0zQA3YOXUlaCojKx4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/987972e43e.mp4?token=V2NTXTURYuzW6aYMLSlISfW-DpxsJ8mOlVZfoaeplEeAav5cd_e3m9HC0yl2xy_xqRdxLo9J6sNev6KaB6niNmZMd6UwQc_DjXJVpSBYfmXLWZJh4je_PLuctzPfpV31sM6Zz-6PeQd_B5leMq5Ld9nGrJ_s63oypcetPr2KMAfgy0BkPJ_OR2sss3vvDpmrWmpjwB0TJCGLre-a0OXcnsy6imv5HMdK_Wp5DFXxTGc1EY9fJtDIDPRRj5k6Xwfn59X_1ukrwWSd-Ttmtk6rOWZnL7trz_hen79R5d3IaMCECSnsM3tJ65gnvZV_Cwbr_Tl_0zQA3YOXUlaCojKx4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماز بر پیکر رهبر شهید از زاویه‌‌ٔ خاص!
@Frasna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/447150" target="_blank">📅 18:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447149">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgfWSJVERcJuz8oLTzEe1Advj14UbenSEJU3LbvpE1OQvZ125di0hkxYlckuMICnT_E0yoFSQjC3SC7V3IeYnIjbX75CYYkLnQvLqqgPi8szorMrOtT3zMnVIzFnbsHYjgPMq8TSUSvebjm18NoPtju0JFmA0nvjjMH_OjVHRsXuGP9IfxNGD4ARBU5OOusfS7p5G73GM8p1ph8TQ-PT1ymrrqZk0TLB6X7hzjO-ffMl4SCaN-3h8n1qvGgguiNcVkELxFrB2iTikYH64t65Yanhjtxbb_VPKK_sOuueGau1E5GaJOfU43hqzoPG6Yqm8HlL6X0tFX3tPvl2nLQGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ازسرگیری تجارت دریایی ایران و قطر
🔹
اخبار رسیده به فارس نشان می‌دهد پذیرش کالاهای صادراتی ایران در بندر الرویس قطر پس از حدود ۵ ماه توقف، ازسرگرفته شده و مسیر دریایی بندر دیر در استان بوشهر به بندر الرویس قطر بار دیگر فعال شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/447149" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447148">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754eb983a3.mp4?token=fE_ufwBbUZkAE8SHcL76dsweBP1Wu_1Tuq7RYMcibk5gWbDwdITUMQvj-dyhqe8n61A__xUsYoIdQgGQtpBJH8W6qzSTPQe-6DnSGUPMoJJGMB7EsgHOfxzQqWsULvJem6AJjrI3dN3ex7TOKBTIvaDxTSIQvexVh6Z1medj4yk89mE2ji_yWSK6R2Yjn-cKpcjv6kGrONDXfn6Xe0CgaH7thPih8_LDVeP_2XGZAyRhIijsqQf6NBgSpDruh7xsfMIS8f5HZ7kyVE9dU6TUWoAZeA-oOrUGapdHcOrF6JjsBIlBQ9yVSFRMAFPOPnZYZiwyJRgCcjDqpauTTpmSFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754eb983a3.mp4?token=fE_ufwBbUZkAE8SHcL76dsweBP1Wu_1Tuq7RYMcibk5gWbDwdITUMQvj-dyhqe8n61A__xUsYoIdQgGQtpBJH8W6qzSTPQe-6DnSGUPMoJJGMB7EsgHOfxzQqWsULvJem6AJjrI3dN3ex7TOKBTIvaDxTSIQvexVh6Z1medj4yk89mE2ji_yWSK6R2Yjn-cKpcjv6kGrONDXfn6Xe0CgaH7thPih8_LDVeP_2XGZAyRhIijsqQf6NBgSpDruh7xsfMIS8f5HZ7kyVE9dU6TUWoAZeA-oOrUGapdHcOrF6JjsBIlBQ9yVSFRMAFPOPnZYZiwyJRgCcjDqpauTTpmSFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم نماز خواندیم هم گریه را به آغوش گرفتیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/447148" target="_blank">📅 17:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447147">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
پنجرهٔ متفاوتی به مراسم اقامهٔ نماز بر پیکرهای مطهر امام مجاهد شهید و شهدای خانوادهٔ ایشان در مصلی امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/447147" target="_blank">📅 17:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447140">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMKSrWcvShq78oZujgAeBjIJ-R6nR6_RhqyYP-rmaThTwaJOhGZDJT535Wh4QfcVfVVZgUuvN-AaIJBLaa61L3lO8lPvKM9_HJr-xkjMjQPYQcSOTQBxaKyd74wFTupPxuqLa1fwabLFkzOXVZS7JesoZ3tNa7ej904XAXwH51t_KeS-U3HuTsN7xq-Ru0Xpc6IwAXlcs2lb1mS_iPPOU9WmCEv_KkSszGS5_xUemdkqrQ0sNz3pwjLzATU57HRuVJI2M2UEz16PjaOEsMYkAGkbqUq9GN8oz2GYUAlhScIUSe6nk5G4OFUIFk43izun2S_JIgsIp1zup1z6osJOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnHbafTRtkqFGjEo-2avukC109iChsmOUzYMdb12lgdyGqS0R9ReNpg0BvsEuhrd7ytWpxqPb6OVwaOjN3-WKb8NEdGgPj1N6lQcj4VWcUmGI0aEgezsO6c-gCvAV2BHoRHkpSfmUaz5u6lrTpYTawhyB-LD7LkETikV59x-vhIIMwknKfC71SC9kdBZeXrr4xG4vgkLA9Q5u88iJUpI_ow7QDNJhVrFVzPMeDUEaDQqjMc35mDTGiARVWd2AaYsH-15kgUyWpSH12qVtzFyHJA2S0AvrpFHDChcDvuaQwvnuUgpdCzjf5_3HkFHEUnHYumsdtC014VyM_aytCnZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvDJ3V0Tt5ykVzCUj4FBhq0EglNTk4Tmq3reUMt6Z0mu64t6r8F7ccPCHgwQuk5YjIic5FQ03hlYGlAVH9JPs6bd_Vz0Xuaag6gHRZt1Acz4QwB5lnAAdzl-VDlGN1S7wtKavhlPjHRcLDibWf3ejsGbbujRRGIRhIqLcKbjRucuovXda606M2BCeOI89AjnnlWSmbCg4l4SfHA3_ZfLsjV364Zl7WeuyN8zwzq0x6ntAkznQke4J8QMuSckJdml6fh2A-h6uShl0EcvLdIii80_fuyjfVzhgAIkk-mdjAPOb9nQUAf_8GLkz6M259rgmLJGix0kRagVhbvfTNLlVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLhjNclcpVXlH0iYkkm_W3jwxUw97a02SoVy0eEpWNnfvpM8ZjjfFo7YsPW49F7e9speqsFL5JoHH5ZpyOCUGiPp_U_MnfhWxbruUTxARuPimvVwXTIwVcXv8B8ESRH09jLR6dwoNJAc-lUTDP9w89EDX2R3sl8-g9Pdx8dNBjtUeHo-179_oXGqmoKlFwC3b8t04tIxw0RzLKdOeQDIN0lyPw8oYttmNFjUiFIQXrjYroOv0o_ageiRNCUoCQsWZcmL01HX9Qba1BwfYR48SEJguBiIBe1RrhgWP0gRfJLYY_AZIOqbN1EL5cZY6p9zUGeUZ6HsO5bfZoKVpltuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDrnmEQxNK8zj6GHne-e1p0YbXdyIKVBckOHiLLYCjaz2dF0LL8GqTw01vpw8J-J_XQ4MWlqQBp6PTWjEHvD0G9YKqhnrrCKHo03nSJyU-L9wzudd2--HCE9zAaSNP7fncqhGz4g3FkkBSkVYHDSGi6UsrQX6wKoCqfAgR_Cr84c9PM8QwTl8WxgbjnmN6lposk2SeirFwi8DIsLMkWQ-3lMtXK7Pm3VdOb8ar0A9czYgWzbjobZZdt5i4sGjcYXCNcmT1sjVNqPwyh5v4uk-k5ZxqjsHHkQrN9tL6j2FYxBS_qvmUDhYKg62r-WB6AKVLHZUOxDz492fRBXDOgETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNQ300qgON-BDME0lIFDJ7C-jl85bOSX_riu7tNu0L7N6--6L2u7AjuCMs4li8CDV4mUohR3cZYj0smukesHpnRckE1XeiyymYU-KOWvzZoM5MX6o9WgBznvTzZZGihZ7meIPnRjOe_yNktKKiMZtyhZKSCCmgmufyQRR0bxHtix2Ea0VfuTdDmjD2Slp1XJvlCl7wmldFSR1amBaNjdpry9u8g91jE9NR5cldZG63_AXnh6Gb62g_hCuW11v1gJLio2-AVOCEk5b-oBi20O5fszbIsoG5xEwfdWusx7fL8qUke4xMj4Lymfs33uuyGE-S9t4m1viBn6T0uf1iEMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLr45V-942qwa5ogYWFsrxmzAKE7L402rYvFKwi2I99zzWDOVCHtLthJjGiQ3de4NpuOKoOPDBBiFoPkyVM6Cj6_FoctshEezB-V_jXYW-VwWzKwtrXJF1n_bArlXpoEb2BuTytcnGGOFfIu07POsY4dDfp4Sk5t3tMOgjvj7LWjEbRT_LPR2o3-H0xHHhbS7oYS9GZ6N84uAZAJCOv4MxR4xPXOZhNxVc_KSRwq_UaPtVC3jTTEj8eUdH-A5nXlsyEH9wan4hWC6J_F0UttstnZK-G14jI1WP1RCT7_j0CSwAHtxRwPaBEZw0Xhc0xa_hu1lmwIKKpcVWcH8gJAiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجدید بیعت مردم با آیت‌الله سیدمجتبی خامنه‌ای در مصلای تهران
عکس:
زینب خدابخشیان
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/447140" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447139">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab59e643c.mp4?token=Tyi53QbeyrHnyJcOYfh7F44mYDpa2YR3cGZCV0AOeK72XJKVsMx1fLrPEfamXITZw2BfkGcjMbb5pkL4UBuJScEx7sSovB_2xwlJoO7BumpuUblupNHcdEjF46HSPPTWb7_zjLwfMPu1T8H9lTzXDxbwmDApnpc_8U9m1dyNs-ztZwrM5ViJV9MZ_e_a-yePUWHBNYGn4gSglu8CSgF9Ese00jfJw3fHkGV478q1C7e8aW_KCpMYIQ4N7AmQS0XrzUhcRjzPROqzU29PwTwQ66xefPgP3yIXWmAcNuvhTN3cD-VCzx6ASQ6tRj-738BsGzXGPaVqVZp8z2jc-XfQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab59e643c.mp4?token=Tyi53QbeyrHnyJcOYfh7F44mYDpa2YR3cGZCV0AOeK72XJKVsMx1fLrPEfamXITZw2BfkGcjMbb5pkL4UBuJScEx7sSovB_2xwlJoO7BumpuUblupNHcdEjF46HSPPTWb7_zjLwfMPu1T8H9lTzXDxbwmDApnpc_8U9m1dyNs-ztZwrM5ViJV9MZ_e_a-yePUWHBNYGn4gSglu8CSgF9Ese00jfJw3fHkGV478q1C7e8aW_KCpMYIQ4N7AmQS0XrzUhcRjzPROqzU29PwTwQ66xefPgP3yIXWmAcNuvhTN3cD-VCzx6ASQ6tRj-738BsGzXGPaVqVZp8z2jc-XfQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقا، «مثلی لا یبایع مثل یزید» یادم میمونه
...
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/447139" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447138">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شورای هماهنگی تبلیغات اسلامی: مراسم تشییع رهبر شهید روز دوشنبه، ۱۵ تیر، رأس ساعت ۶:۰۰ آغاز می‌شود
🔸
مسیر تشییع شامل خیابان دماوند، میدان امام حسین(ع)، خیابان انقلاب، میدان انقلاب، خیابان آزادی، میدان آزادی و بزرگراه لشکری است.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/447138" target="_blank">📅 17:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447137">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65944687e4.mp4?token=UzoCBa3K4Cfrpf0cdqqeiiRqIz1e1YxTCeKJbqpfnp8tBvTKVdJTlRACyI_8BWT2lBC8lXSDWzcxIQZ5fU04TJ2QqM3Z5t6tSMskDgQhUpE8u34Pqb8d15W2GLtI1bHY7bDT1ZQTnFq4VF-W2ldTJagrRFsmqR43lBGvqNTEalmKF8H0OU7WyAMIQAIMUJkZU_q44idYNDkWzDoeIsrvu1P0bLvMsBvhlfmMrgB9f-O_6B7PuWNrZsG8JJJsMMB8yTj2ZkE3WgTGhUclM73P3Puf5KI6DwL9_E2jXFOMonG6WAIJn2fUcP0lDU7GgqL5GFNEGNjdf92FCRlyuZE7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65944687e4.mp4?token=UzoCBa3K4Cfrpf0cdqqeiiRqIz1e1YxTCeKJbqpfnp8tBvTKVdJTlRACyI_8BWT2lBC8lXSDWzcxIQZ5fU04TJ2QqM3Z5t6tSMskDgQhUpE8u34Pqb8d15W2GLtI1bHY7bDT1ZQTnFq4VF-W2ldTJagrRFsmqR43lBGvqNTEalmKF8H0OU7WyAMIQAIMUJkZU_q44idYNDkWzDoeIsrvu1P0bLvMsBvhlfmMrgB9f-O_6B7PuWNrZsG8JJJsMMB8yTj2ZkE3WgTGhUclM73P3Puf5KI6DwL9_E2jXFOMonG6WAIJn2fUcP0lDU7GgqL5GFNEGNjdf92FCRlyuZE7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای هیهات منا الذلة در مترو بهشتی تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/447137" target="_blank">📅 17:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447136">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
بدون اینکه کسی از او خواسته باشد، این خانم در مصلی مشغول جمع‌کردن زباله‌ها بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/447136" target="_blank">📅 17:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447134">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7ec7d63b.mp4?token=hqozgW-UIT5GD6wU42eg-j3yiMzUPKvolKFlaBg0jp7DrqwB41PkJr8PHWBCNXN86r8fLTJ-6dwUVzMA1L7b3oejVJstTz0h0rzERlVCZUfHxS6_1UX3FpqJge931PEIqyLoa394sZjkPJ-01sUX5rG3ZKZoJa56CFo7CwsCsMGfwK-69S5OaMernUVcYr4XEcFGXtfenVUSuWyWKTVL_dJKPUSQVK8q8VXuac5o_LuFMBEgPqNAFJ9a6UbV3SSghDnZ6hFWpwQdg3SImsK6DiiNp4iNQs_za8Xf5teNirAzi5rBlBDhihvV4q07qrrCu8aAvZtDNdR0D2BryE3VUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7ec7d63b.mp4?token=hqozgW-UIT5GD6wU42eg-j3yiMzUPKvolKFlaBg0jp7DrqwB41PkJr8PHWBCNXN86r8fLTJ-6dwUVzMA1L7b3oejVJstTz0h0rzERlVCZUfHxS6_1UX3FpqJge931PEIqyLoa394sZjkPJ-01sUX5rG3ZKZoJa56CFo7CwsCsMGfwK-69S5OaMernUVcYr4XEcFGXtfenVUSuWyWKTVL_dJKPUSQVK8q8VXuac5o_LuFMBEgPqNAFJ9a6UbV3SSghDnZ6hFWpwQdg3SImsK6DiiNp4iNQs_za8Xf5teNirAzi5rBlBDhihvV4q07qrrCu8aAvZtDNdR0D2BryE3VUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر رهبر شهید: داغی سخت دیدیم اما خدا را شکر آقا سیدمجتبی هست
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/447134" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447133">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700dbb08b4.mp4?token=ILzNBvq1gBClS_pRmwxJal7nolh26JfpNDE1UHYl8ORgGDKEB_atIpGn9OpYvVzYKDwkf3yy7Vzeig643P5R9gqiU5Idoc6HYj-KpV55SQwFyzfmD3DUCqT_JLE_5RQAJmKmb2T5YWV3FlxftRxgXgUoky6hhYCM8iV674qwB3baeUvyzGSLZ7xRzjE5Eaps06kOXjPnHaMtTr-0cjrcm9c_BV45P_FZln_y3lGOuSSjXOVUb4a8brO-LUHj93V79vmzQIItSx2hNWrNjCW-xFmkHBiyTS-HUAgCSekcVwCrrBPc5toNSX28-Qh52oh7dd4GyrNgBWr2HeGnpYbhfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700dbb08b4.mp4?token=ILzNBvq1gBClS_pRmwxJal7nolh26JfpNDE1UHYl8ORgGDKEB_atIpGn9OpYvVzYKDwkf3yy7Vzeig643P5R9gqiU5Idoc6HYj-KpV55SQwFyzfmD3DUCqT_JLE_5RQAJmKmb2T5YWV3FlxftRxgXgUoky6hhYCM8iV674qwB3baeUvyzGSLZ7xRzjE5Eaps06kOXjPnHaMtTr-0cjrcm9c_BV45P_FZln_y3lGOuSSjXOVUb4a8brO-LUHj93V79vmzQIItSx2hNWrNjCW-xFmkHBiyTS-HUAgCSekcVwCrrBPc5toNSX28-Qh52oh7dd4GyrNgBWr2HeGnpYbhfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرگی زاگربلنی، اسقف اعظم کلیسای ارتدوکس قرقیزستان: رهبر شهید مانند پدر امت بود و با چشمانم دیدم که ملت رهبری را مانند پدر خود بدرقه می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/447133" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447132">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b151d9ab0.mp4?token=j2dwmM_amOxj_LVla4p-ro4kcwkguhMKUr5T04qXpn1M7HPTZfTzpA9gobm7QNXoREKEAWdO31govbuP0EA0HlvtY8pp1gw32MGk1pYmB0pyLD8bTLNv_dBZcLVpKeTmxlEnoBj1nCKH1ipNxbvFdbg5d9QvS7ax9orGcLszTeK2l3Sx0vPryHPHYyHrCBgfFVjX7b6kPklmcIlhocSGC3Nultxm7lq9fqOK8bC6uJRnujTo_g9UoRL_JDu48r6YPmo5h_d_5vsls2masCTEOnBHq_VptlqN86JBZ1bwcA_kSbnoTQZL99nWtVfZ4yAnNGxm37BSADa3FFV4sgof1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b151d9ab0.mp4?token=j2dwmM_amOxj_LVla4p-ro4kcwkguhMKUr5T04qXpn1M7HPTZfTzpA9gobm7QNXoREKEAWdO31govbuP0EA0HlvtY8pp1gw32MGk1pYmB0pyLD8bTLNv_dBZcLVpKeTmxlEnoBj1nCKH1ipNxbvFdbg5d9QvS7ax9orGcLszTeK2l3Sx0vPryHPHYyHrCBgfFVjX7b6kPklmcIlhocSGC3Nultxm7lq9fqOK8bC6uJRnujTo_g9UoRL_JDu48r6YPmo5h_d_5vsls2masCTEOnBHq_VptlqN86JBZ1bwcA_kSbnoTQZL99nWtVfZ4yAnNGxm37BSADa3FFV4sgof1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقام رهبر شهید را چگونه می‌توان گرفت
؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/447132" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447131">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594503be2b.mp4?token=po4VlMSvtTnlJKY6c-hTA-njuRN-XLDrtyaEOPq13gzvFOM5VGxVxnriaOgvONiCw5gHJtgtoVGFIfhxhSAEuRAD_eSb1Y2xoesy57a_ZD6c5-_nch8ejhRRJG35d7pZNKoEaTvPMOdhLAiBJowCUUWZ9stAgK8-gmM47yzbfokWMCBpoqlsy9kMmUV6Hn4G4bJFHedHtkJWn3GyA1iEABKfDZEb0RqpYI8CzR66xH-A8T8jdZCM4YwmG2Cz8SkxfKd4lP6OEKJgCfEB-Eu6WT4pPrFrVLyYrMmLkZDm_S4nw2wwlF_5pagw8ffyWMf8Hj6iHWY2ICRDgK4W_fl54A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594503be2b.mp4?token=po4VlMSvtTnlJKY6c-hTA-njuRN-XLDrtyaEOPq13gzvFOM5VGxVxnriaOgvONiCw5gHJtgtoVGFIfhxhSAEuRAD_eSb1Y2xoesy57a_ZD6c5-_nch8ejhRRJG35d7pZNKoEaTvPMOdhLAiBJowCUUWZ9stAgK8-gmM47yzbfokWMCBpoqlsy9kMmUV6Hn4G4bJFHedHtkJWn3GyA1iEABKfDZEb0RqpYI8CzR66xH-A8T8jdZCM4YwmG2Cz8SkxfKd4lP6OEKJgCfEB-Eu6WT4pPrFrVLyYrMmLkZDm_S4nw2wwlF_5pagw8ffyWMf8Hj6iHWY2ICRDgK4W_fl54A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری شبکه سه: ملت ایران تا زمانی که نفس می‌کشد، میناب را فراموش نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/447131" target="_blank">📅 17:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447130">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شرکت راه‌آهن: فروش بلیت قطارهای فوق‌العاده برای تشییع پیکر رهبر شهید انقلاب در مسیر تهران-مشهد و بالعکس از ساعت ۱۷ امروز آغاز می‌شود.
@
Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/447130" target="_blank">📅 17:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447129">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ff6552d9.mp4?token=YWzF2j2DWcOMOg5rsaVJ5mt1aocfqKdZoRQ1MCh9c9X-YuJnoxgG48val-88dxyVoczjkblZ7arm8iT2rxPIRC9VHCmNF9vGJ4BWMyqkRHADAvJnuUsys97AOvcNEsSkHgkIO0WPw2WMY6srWO_q9L9ZYX6yvEvl7SqNXQPIhMtAHUNxdS_fuzvILr5mrRWgnMq3eoFfVAVBDFU04MQsS12FMCFxS5dPsdCA8BlEQHA2dzW76adbuYVyCQJau3DHiUKiOSfdA3hyaYSo_GPRMlzBXD9FsP1sBVle5u2jeqKKH3qCLpC0ehn37WHRoAjonQUJzPLdrbdfJ2qJ3_LVfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ff6552d9.mp4?token=YWzF2j2DWcOMOg5rsaVJ5mt1aocfqKdZoRQ1MCh9c9X-YuJnoxgG48val-88dxyVoczjkblZ7arm8iT2rxPIRC9VHCmNF9vGJ4BWMyqkRHADAvJnuUsys97AOvcNEsSkHgkIO0WPw2WMY6srWO_q9L9ZYX6yvEvl7SqNXQPIhMtAHUNxdS_fuzvILr5mrRWgnMq3eoFfVAVBDFU04MQsS12FMCFxS5dPsdCA8BlEQHA2dzW76adbuYVyCQJau3DHiUKiOSfdA3hyaYSo_GPRMlzBXD9FsP1sBVle5u2jeqKKH3qCLpC0ehn37WHRoAjonQUJzPLdrbdfJ2qJ3_LVfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تهران آماده میزبانی همه جانبه از میلیون‌ها هموطن/ تأمین گسترده و مستمر آب آشامیدنی، یخ و مواد غذایی برای خدمت‌رسانی به زائران رهبر شهید
🔹
شهرداری تهران، ضمن اسکان زائران، در حال تأمین اقلام و توزیع آن با رعایت دستورالعمل‌های بهداشتی در پایتخت است.
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/447129" target="_blank">📅 17:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروابط عمومی چادرملو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9396129178.mp4?token=VO8USirzZDQonRqkK8iucPi74R4x3dOnm0C_6fy1ABQ3U_1OhPSGGwQWwBSPC6y7DIlMpcPaWPQpBYQZgwLNhopyTrxuMNOWTVXolc5K3m1SHgRUA5H7ve90P6WiOMqCxKbGNjg-PzLPWDAQGEprtZiRSxwAqX0RcjOGKRv0u0pDo0i-VV_8FOZ910C6rEEvMOUNl4vjZxY_RYFSMp6W_IsTF08JkwFGVb1dU4klpk1bpB-nGo4MT19j-CfWjRHLDaMQsNIn5UukiiGdjD5GTxWexAW2mrN1kokj8AuNKzXB1nZh3AugeGzihh21VyNYk-llANUci0hsAXU08TsYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9396129178.mp4?token=VO8USirzZDQonRqkK8iucPi74R4x3dOnm0C_6fy1ABQ3U_1OhPSGGwQWwBSPC6y7DIlMpcPaWPQpBYQZgwLNhopyTrxuMNOWTVXolc5K3m1SHgRUA5H7ve90P6WiOMqCxKbGNjg-PzLPWDAQGEprtZiRSxwAqX0RcjOGKRv0u0pDo0i-VV_8FOZ910C6rEEvMOUNl4vjZxY_RYFSMp6W_IsTF08JkwFGVb1dU4klpk1bpB-nGo4MT19j-CfWjRHLDaMQsNIn5UukiiGdjD5GTxWexAW2mrN1kokj8AuNKzXB1nZh3AugeGzihh21VyNYk-llANUci0hsAXU08TsYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ببینید
میزبانی فرید دهقانی مدیرعامل شرکت معدنی و صنعتی چادرملو از عزاداران آقای شهید در موکب چادرملو واقع در میدان ولیعصر تهران</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/447127" target="_blank">📅 16:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447126">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/447126" target="_blank">📅 16:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447125">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBCAJ9NGNOc9iKkPzbOY1QMUpqRa_W-HNZEZ1OgbLZcf6BUDSjR69nfhE5M3nVuQyaz_U5tr27orqiYEkA6Q_3WT1sHpndgO5tgZ_dkCy3tHMnIO9DLNJWmvAxAMmK2I5_DssmwUVILzGiN8PZBwltOEfaVV31ggYSEsrDUkJrny0_DsJSUlUp_huPUjtyOuZN6CdmbM22n5cjmgSujX2raVfcMTjd3NjcWzzd_S_6hJWddPSDERJdAbicGzDDGlk9Dd4iBd_Q1R8WS1Q4a9xNetipPW5OC4pfqKgVNX-NagY5Eh2S41AHbyw3SumcmyD7RRWid6J1nQleU41sCw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارمان اربعین بود، وداع نصیبمان شد
🔹
«دلم نمی‌خواست هرگز آن لباس را بشورم. حس می‌کردم ممکن است عطر آقا را از بین ببرد یا برکتش را. نمی‌دانم فقط دوست داشتم همانطور توی کمد لباس‌هایم بماند.»
🔹
«خیال می‌کردم سال‌های سال باید در مسیر نجف تا کربلا نوکر زائران سیدالشهدا(ع) باشم تا شاید روزی آقای دلتنگِ کربلا را هم در همان مسیر زیارت کنم، اما...»
🔗
ماجرای دیدار این موکب دار با رهبرشهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/447125" target="_blank">📅 16:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447124">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bdb70b516.mp4?token=ac2Jr-o8yCOf6b6GM16Om2S1wa8BuLGy5HKfwOgcehsn6en2KMwBZfVZL68F_k4ntjCK0VqToBaA_pZpV0h5PfwURXvDp6Te78sxoxZOT8GACnEdcCpNvrs42Yos4x682u5ne66IfpeLg1DYPpNDkkFRnjTJOgx45dhqrmeuh_Stte3ikIMaqX5Sh-rKbyGuuw7e_3yhVqqv_9KiSj83O6FpKWh6Oh_vQqfuKcCxMvN68jzgKUhdCGiE1R2f1vID4pVFAAvBocJdVaoN5J_-DyjHq029S98ajvwoAqhT14J5rofcS80cKYsUT0BFAh1oP1-VtJqDxBtQMV3xAgLanYI2hvQrXa36LPNpB8zWAylpLM0_CuqABCgwUAg2KkWnowvli2-4qlsJRkRnMmk5E2MbpSa5gNLCWmoQRID7DU6yzCvgNXFiGyBDIg62o9bKgH0kN3LJU02MZgtic7voUi1OYlGIg_5gYoiLVg4ybrl7LUj_PYFvBmSGLNKt1Fufqf_23FcfvU9gSDP6RlABgPqNd6f97C0ixLgfKQCxue1cWPbQLqqhyZrWDjnQI7jxGTHUPJko5QZqhcTG-bx1h8Md6ueFeotqkp9-1QOnu3UeEP9o526Jg2XHod4mm3EfdfOAcMQwOh8wi0ayD4AwZ21mh2MNVHfnqB5QHS1ERh4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bdb70b516.mp4?token=ac2Jr-o8yCOf6b6GM16Om2S1wa8BuLGy5HKfwOgcehsn6en2KMwBZfVZL68F_k4ntjCK0VqToBaA_pZpV0h5PfwURXvDp6Te78sxoxZOT8GACnEdcCpNvrs42Yos4x682u5ne66IfpeLg1DYPpNDkkFRnjTJOgx45dhqrmeuh_Stte3ikIMaqX5Sh-rKbyGuuw7e_3yhVqqv_9KiSj83O6FpKWh6Oh_vQqfuKcCxMvN68jzgKUhdCGiE1R2f1vID4pVFAAvBocJdVaoN5J_-DyjHq029S98ajvwoAqhT14J5rofcS80cKYsUT0BFAh1oP1-VtJqDxBtQMV3xAgLanYI2hvQrXa36LPNpB8zWAylpLM0_CuqABCgwUAg2KkWnowvli2-4qlsJRkRnMmk5E2MbpSa5gNLCWmoQRID7DU6yzCvgNXFiGyBDIg62o9bKgH0kN3LJU02MZgtic7voUi1OYlGIg_5gYoiLVg4ybrl7LUj_PYFvBmSGLNKt1Fufqf_23FcfvU9gSDP6RlABgPqNd6f97C0ixLgfKQCxue1cWPbQLqqhyZrWDjnQI7jxGTHUPJko5QZqhcTG-bx1h8Md6ueFeotqkp9-1QOnu3UeEP9o526Jg2XHod4mm3EfdfOAcMQwOh8wi0ayD4AwZ21mh2MNVHfnqB5QHS1ERh4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پرچم خون‌خواهی سرخ امام شهید در کنار پیکر مطهر رهبر شهید و خانواده ایشان  @Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/447124" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447123">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f095ce01.mp4?token=nxPWP5L3bSMkrKa0s7q0ShQpD88rIzdRjLQhmWkciJ_Dm8KFsLohX9x8aK5FHV0WO4ZdkDRWfIhO79sesyD_HtiOjsnKb1P2EIaOBqJceb29t2buyiJgh8sdZr5l90oz4C8mMuGZfaSMYdJ1Op1itnD0qOuQVGLLk_tfyf2TPUxadPOlyAhY4V7OkVyWRNGJ6bDBVd2b7dE-GZNBqqVApCmrjuavIAbEQxgbz0cPNoD87GhM1SL6fGQYrVH_wE6wmYcscA50gBJZemytJWq7wjIUGgZjDAKTe3jc7RCrsiESRm62BZpYxTeysDW-qDRLrj39JVhcn7tBeYyOh4ExBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f095ce01.mp4?token=nxPWP5L3bSMkrKa0s7q0ShQpD88rIzdRjLQhmWkciJ_Dm8KFsLohX9x8aK5FHV0WO4ZdkDRWfIhO79sesyD_HtiOjsnKb1P2EIaOBqJceb29t2buyiJgh8sdZr5l90oz4C8mMuGZfaSMYdJ1Op1itnD0qOuQVGLLk_tfyf2TPUxadPOlyAhY4V7OkVyWRNGJ6bDBVd2b7dE-GZNBqqVApCmrjuavIAbEQxgbz0cPNoD87GhM1SL6fGQYrVH_wE6wmYcscA50gBJZemytJWq7wjIUGgZjDAKTe3jc7RCrsiESRm62BZpYxTeysDW-qDRLrj39JVhcn7tBeYyOh4ExBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پرچم خون‌خواهی سرخ امام شهید در کنار پیکر مطهر رهبر شهید و خانواده ایشان  @Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/447123" target="_blank">📅 16:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447122">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWKCso7_AX3WrQJfaiYFbj7l7xQyF7Cf9RGYXpjqfiJeeqyGyihiB2oea_hZR-A5S8Cgw-980ZsxB9RxkvILim9t_WEBYXsIGHuMqtVO0_IzM4RQq6aXAiWVOopGiWVI4WqqJXlerrpBDAGKg3cNb_3102rwk-4XuzVR4SICc6ls4zTBhfIRf67W-sfElAVUntZzjD95ToH7tYFNPRovPxZdAjjguAYHBxOLqQhQuTMsc3ShfRGoxsFLcgxOjnbz7pAW0biaxKD33hgD1q5AiFVd1a9GVnvBbkg8rZUe4NECJ24ypDaqyiOa8xmkO2hfQInlwOvXFJSDWbWBnL5nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ما شیعیان قاتلان رهبرمان را مجازات می‌کنیم
🔹
دست‌نوشتهٔ عبری مردم در مصلای امام خمینی(ره) تهران
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/447122" target="_blank">📅 16:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447121">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593b30b738.mp4?token=RM7-6Jy-YtSo9_-w8yCStdsYMM8u7E5EUamX6ognb1184MLNkFL8xmUS7c6ol1-m3dhSKQuqc5skmiXHK-8GFkDInNW5TBQWBXTP3ixWml3UXu9xZ8pEq42lGSQ_ZiZwABtR2RJJEUuIHwHwLVJmTU9ZJ8bDakMRwqQSw_LTcSr5hpysMYYayHEWOwOF3rhcwUF6dYwm8cQpzDhqw3CbDNdl_JpCVayn7r0Ysj2leHtNqEX-6BzLl-FRCKYKdvdgrV4i37etwcdEkpryGAqx93NbnPzLwqrp0htRn0p8bSKDkOKn9qQo11hFe-xBHwgMzEXPed3nhp4bzZJB40C7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593b30b738.mp4?token=RM7-6Jy-YtSo9_-w8yCStdsYMM8u7E5EUamX6ognb1184MLNkFL8xmUS7c6ol1-m3dhSKQuqc5skmiXHK-8GFkDInNW5TBQWBXTP3ixWml3UXu9xZ8pEq42lGSQ_ZiZwABtR2RJJEUuIHwHwLVJmTU9ZJ8bDakMRwqQSw_LTcSr5hpysMYYayHEWOwOF3rhcwUF6dYwm8cQpzDhqw3CbDNdl_JpCVayn7r0Ysj2leHtNqEX-6BzLl-FRCKYKdvdgrV4i37etwcdEkpryGAqx93NbnPzLwqrp0htRn0p8bSKDkOKn9qQo11hFe-xBHwgMzEXPed3nhp4bzZJB40C7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانیِ مقیم روسیه: رانندهٔ فرودگاه مسکو به ما گفت حتماً برای تشییع رهبر شهید به تهران می‌آید.
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/447121" target="_blank">📅 16:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447120">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79867cbe0.mp4?token=XS3EsMz2A44IEvV11VJ1qTSxGWTDPFdXFFA2KXElGzG6MHCX8oVUIvRj9Fv-K2gaBPuThDz2R5S3TLF8gDXBznLjdxThwSUEcoTRANzrpEcU0bqZrwTn2hgdrPwzb29OjJDFMZAltlsA77Tm8Dn2FTOZlnkeHvWikjzldkl-VRHafi9F_1_-eQW-eT1BqtrYxQegAKOVXroubFGjm8mZIIJ4CCmBU0yjHu2hvqVDeru_zlp8CZ4OXNZSr4clh5CYxU4y2X23Dg5WE4odWp4bz2AAgpGEPS7dEWChn44YA2Kw4G80lW5J6hTTNPTEKqiP1t4A9DQbZbaqpPGqMb0a0ULmEf6CDPiSlYMMgpBphzOGVmtWlNGWVPTvPt5IVdtD5yRrgAB7AgmZ9bWTizl4sNK1JSiO_tGUXUQTW49E2J4n6nqVqP2CcLp4FL3P7OVzDtEdSjgOR5gudkf2kDwqeqvU68l4zW2IccXH2bJEcm7WxgPNRySCowNpVlVmg_YauXVYJACzG6BoajMI3zl-R6Wu45WRuO9qZX2AfAnUl6obqAprnx9mg2-ZGQTTQxJh5fFIPfl8mx4ETcjRcIsgLTJZoq7qz2NQyRvT3YLb-OwvwEROqUdsHbn4B3uC4-rXGp-1wkF1jb4Gg-xrdj1he6dZYpI05i_93Cwx7Oy0nR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79867cbe0.mp4?token=XS3EsMz2A44IEvV11VJ1qTSxGWTDPFdXFFA2KXElGzG6MHCX8oVUIvRj9Fv-K2gaBPuThDz2R5S3TLF8gDXBznLjdxThwSUEcoTRANzrpEcU0bqZrwTn2hgdrPwzb29OjJDFMZAltlsA77Tm8Dn2FTOZlnkeHvWikjzldkl-VRHafi9F_1_-eQW-eT1BqtrYxQegAKOVXroubFGjm8mZIIJ4CCmBU0yjHu2hvqVDeru_zlp8CZ4OXNZSr4clh5CYxU4y2X23Dg5WE4odWp4bz2AAgpGEPS7dEWChn44YA2Kw4G80lW5J6hTTNPTEKqiP1t4A9DQbZbaqpPGqMb0a0ULmEf6CDPiSlYMMgpBphzOGVmtWlNGWVPTvPt5IVdtD5yRrgAB7AgmZ9bWTizl4sNK1JSiO_tGUXUQTW49E2J4n6nqVqP2CcLp4FL3P7OVzDtEdSjgOR5gudkf2kDwqeqvU68l4zW2IccXH2bJEcm7WxgPNRySCowNpVlVmg_YauXVYJACzG6BoajMI3zl-R6Wu45WRuO9qZX2AfAnUl6obqAprnx9mg2-ZGQTTQxJh5fFIPfl8mx4ETcjRcIsgLTJZoq7qz2NQyRvT3YLb-OwvwEROqUdsHbn4B3uC4-rXGp-1wkF1jb4Gg-xrdj1he6dZYpI05i_93Cwx7Oy0nR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما با آقا وداع نمیکنم
...
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/447120" target="_blank">📅 16:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447119">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b921516321.mp4?token=dJ7oXLdInghMU921_s0Nhn55kJ4S4dIOkUFKt1HQP4CXhT_IlhbIif9glhEl2_5jG5mqnhm8aHpeFGWF7hds3EGGj5udp1L8k8WcGw56HLbJzseI4CKvP8d8SnzUU2t4CghanHezwT9mVwa_VA-jUb8n8Ww0Pvz5wd_s7OuCDpW7IN6hz1_smVe6fBPP5InTCNA2fMBzpZon1e5hc8KxqN2Q0bq5JELbNPTRUflZS_eMFHxI_lRM1M_-eogzewfWJnrjkg0Iy5jFPfQUo77gpWE6U0UQBLTqlYP-SgV1q_4XaVx44pgvdSgECjv8VZye5ewlfJlTHo2HBzKtp_0DAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b921516321.mp4?token=dJ7oXLdInghMU921_s0Nhn55kJ4S4dIOkUFKt1HQP4CXhT_IlhbIif9glhEl2_5jG5mqnhm8aHpeFGWF7hds3EGGj5udp1L8k8WcGw56HLbJzseI4CKvP8d8SnzUU2t4CghanHezwT9mVwa_VA-jUb8n8Ww0Pvz5wd_s7OuCDpW7IN6hz1_smVe6fBPP5InTCNA2fMBzpZon1e5hc8KxqN2Q0bq5JELbNPTRUflZS_eMFHxI_lRM1M_-eogzewfWJnrjkg0Iy5jFPfQUo77gpWE6U0UQBLTqlYP-SgV1q_4XaVx44pgvdSgECjv8VZye5ewlfJlTHo2HBzKtp_0DAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدیوی ساخته‌شده با هوش مصنوعی از چهره‌ها و صحنه‌های خاص و غیرمنتظره مراسم امروز وداع با رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/447119" target="_blank">📅 16:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447118">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLOU2dJqZEIuzxjaCz4TDgLJcc-tza2c-Quhj4Up1n9fRCoH6V6hueSPqld9jAUL7ULnQT10YIoElVwpgI3UILFmi0nfIUJEMERZDXYtZFM1OV3jZx0DtzcE1xxeJaPxNPDHxMmVfEbcH2uBCpDkDycqjs6FrlAdkREMu0DCgmXaoBe3c41PZh53I5HSw8nNDZecYMNYum94JfZgciuaEOvSvAb16LU-PuH3QUquGkYmlpdPCHZsgStnwQnEVwhXm2-DRfVDePc-huB6NspPWgYbgC_6iqtpDGEK4PuKB7_h5NVrXwpPE6nL5s76eV3jPJZPIWlzw14kmkwslU8hCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا! بچه‌های میناب زودتر از همه به دیدارت آمدند
🔹
«حول‌وحوش یک هفته قبل شهادت ستایش، مادر دختری تلویزیون نگاه می‌کردیم، حواسمان جمع سخنرانی آقا بود که یکهو گفت: «مامان ما می‌خواهیم بریم اردو پیش آقا...»
🔹
خنديدم و گفتم: « مگه می‌شه شما رو ببرن پیش آقا؛ تازه من نمی‌گذارم تنهایی بری، اگر ببرند باید با هم برویم» گفت: «شما نه! ما دانش‌آموزا، بعدشم معلما و مديرا، مامان باباها نیستند!»
🔗
حرف‌های عجیب ستایش علی حسینی پیش از شهادتش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/447118" target="_blank">📅 16:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447117">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q03UZLhisKAOOWiNfgt3kL3p9kteWiki5KLHnN3wmwGy4GB5i14ifddaB2zgjHRVqDk8dT--KmCcA5_Yz_L7e8PYUR9EE_0R34birLEq2m9sx6WmDkMCXaHEsHlfq3Nq14KWsFLdsk0gL-fblSJ3BQQwYtiDZjWDOf-b90hZ6rH068aek-c2uB-LBP424ZeZowwuhtKuC2-zr6iyGQZKdjYcxDFkCQZb70bpGvmtO3wW5u93KaeFfIjrBZXMZiDi5dNDfUl15t-m3TNtP9J02XE2BTLu4Mhh4D0-5YHVHBJghszTYdQ_VTbn50Rvs1oPi_qwJJm8ZOqDTG_1mLiRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون فرهنگی و اجتماعی مرکز رسیدگی به امور مساجد تهران: همۀ مساجد تهران با آغوش باز منتظر مراجعۀ میهمانان مراسم بدرقۀ آقای شهید ایران هستند.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/447117" target="_blank">📅 16:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447116">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb48eac0e8.mp4?token=HJVeaP8_R0HT4TyQPbq1FWUYIiCwKsul4unjNhEEKPZyW4z0JgH1_F8SeZoMu-kabltMEBWoTeNnTgnK5n18Dj_w1T4mxWuI7p2tULedEJRb-lt52KmjnuEjvh9aSs8wjbsALtfCExKZtsDduIv3Mahski6AzZfSbfO1kOSwEXYqoqZ3hmENukiJaGpmI5WnF-ydH6pHUvNE8BjQWS26NljhMC2nhC3dN_YeVJVNpkqRsFUdFtbpyCHFBvRfMqLkMo4stvwiu8AelcCrJrkFi0-bpQaiGy0B9sWuYJCzrA5blc-Y3yoKgG4CU7OS6ogEmeJaauXZzktS1ZEGVKJZrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb48eac0e8.mp4?token=HJVeaP8_R0HT4TyQPbq1FWUYIiCwKsul4unjNhEEKPZyW4z0JgH1_F8SeZoMu-kabltMEBWoTeNnTgnK5n18Dj_w1T4mxWuI7p2tULedEJRb-lt52KmjnuEjvh9aSs8wjbsALtfCExKZtsDduIv3Mahski6AzZfSbfO1kOSwEXYqoqZ3hmENukiJaGpmI5WnF-ydH6pHUvNE8BjQWS26NljhMC2nhC3dN_YeVJVNpkqRsFUdFtbpyCHFBvRfMqLkMo4stvwiu8AelcCrJrkFi0-bpQaiGy0B9sWuYJCzrA5blc-Y3yoKgG4CU7OS6ogEmeJaauXZzktS1ZEGVKJZrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازمانده حمله اسرائیل به کشتی آمریکایی: پرچم شیطانی اسرائیل را در روز استقلال می‌سوزانم
🔹
یک بازمانده کشتی یو‌اس‌اس لیبرتی، در اقدامی اعتراضی در روز چهارم جولای (روز استقلال آمریکا)، پرچم رژیم صهیونیستی را به آتش کشید و از سربازان کشته‌شده در حمله اسرائیل به این ناو تجلیل کرد.
🔹
وی در این ویدئو با خشم می‌گوید: «من این پرچم شیطانی را در چهارم جولای می‌سوزانم!» و در ادامه از «توماس مسی» به عنوان نامزد ریاست‌جمهوری ۲۰۲۸ آمریکا حمایت می‌کند.
🔸
ماجرا چیست؟
🔹
یو‌اس‌اس لیبرتی (USS Liberty) یک کشتی اطلاعاتی نیروی دریایی آمریکا بود که در ۸ ژوئن ۱۹۶۷، در جریان جنگ شش‌روزه اعراب و اسرائیل، هدف حمله هوایی و دریایی اسرائیل قرار گرفت. در این حمله ۳۴ ملوان آمریکایی کشته و ۱۷۱ نفر زخمی شدند. تل‌آویو این حمله را «اشتباه» خواند، اما بسیاری از بازماندگان و تحلیلگران آن را اقدامی عمدی می‌دانند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/447116" target="_blank">📅 16:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447115">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2838ae2b47.mp4?token=N0bj88YDUnBgeHxDRWOA3pEkwzQe3Ud9sqGYF1uWhlZH0YFEuiPqH5b88bPwaoJtoHRFk_RsTh8pkQomwkk0puQSkYVFRnhpRjqOZHwBDQojrwSlByjVqyvTBHj8IvZOw5y9ZnRFwuIJ9-eAh5Zk88dcNMymLB_aG54X4H9G4HM8uL0BiTeujO4Qgi_vCamOFk4xHnuNU5J4UWUA0w-5iCYZUUhSguKk4p1LfOJ__6yI9sq6xuXOLpjZcygEG94un92L3nFD3PdtO4CrZ5czf4UX1jFwTL6wowx2msZvWjkHYtgV5Lpj8K3KNrAW8kFVn47BC26fAMBQkCQVaELRkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2838ae2b47.mp4?token=N0bj88YDUnBgeHxDRWOA3pEkwzQe3Ud9sqGYF1uWhlZH0YFEuiPqH5b88bPwaoJtoHRFk_RsTh8pkQomwkk0puQSkYVFRnhpRjqOZHwBDQojrwSlByjVqyvTBHj8IvZOw5y9ZnRFwuIJ9-eAh5Zk88dcNMymLB_aG54X4H9G4HM8uL0BiTeujO4Qgi_vCamOFk4xHnuNU5J4UWUA0w-5iCYZUUhSguKk4p1LfOJ__6yI9sq6xuXOLpjZcygEG94un92L3nFD3PdtO4CrZ5czf4UX1jFwTL6wowx2msZvWjkHYtgV5Lpj8K3KNrAW8kFVn47BC26fAMBQkCQVaELRkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌وطن مقیم ترکیه: پس‌از شهادت رهبر انقلاب و ایستادگی ایران در جنگ، با غرور و افتخار از ایرانی‌بودنمان سخن می‌گوییم.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/447115" target="_blank">📅 16:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447114">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMRhzujBI7BkHEiqwE0TdWZpQuYiPAUnwCUzJqJ6ZoxA3jPye3SRzNUzg5CHgKBqGL_QmdQGM2xNEKfiORHVR1grIZhJpqzh-cFvwfy0zeNUBMZnAQ9LuShyuOEmInGOSVAZAu8spDJ16BJTH0f7T18Zjz5O0j0lrmSlVzSMHWORtuBNvY87gnYch7ZfqQ6wmPqQ6v2NOmR8CzAO3jzgi3dqgvyOCnUebHIzxWIGa52I03Gcx-HLdPUkBbUoDtiRiNveigIzRIYdZOrE6byqqvoajvBxsZ2dbRO36eTdsHbNIE5H8DGQ715aYM_lJGg67iW2RJzqC_jJnNsrVYQ0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پرچم خون‌خواهی سرخ امام شهید در کنار پیکر مطهر رهبر شهید و خانواده ایشان
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/447114" target="_blank">📅 15:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9200c8b77.mp4?token=Vq13vacJ24D6Y9NoitxuhbBeINFPlQIs1WWd96HY4_-G0hRVbIV5RDKXZmLiDvf4GvIttYv00mbAX2R6I67_zD57i7eyN0xILgpJcEkbZlItJK4Jn_x5dYsVvb2si9odS8yFJKfY_Jentq9kIj_of-OG8dtK__6JsE2aDTP9a0X5K3uQy-4vJXDxkC_TRyabVWfEJ1eMnHl57khFxt9hcrc9Op7Kmis_ue61naJwvW-_frlfljKrI5QWGOBn3_snKFho3X_KrEJryWXagQXRPDoqOBLQNygrkJmy8-e9aIE1lLJIZzeOql-ZjvJa-2CuLCQQ-9Em-WTxRVRNoPadAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9200c8b77.mp4?token=Vq13vacJ24D6Y9NoitxuhbBeINFPlQIs1WWd96HY4_-G0hRVbIV5RDKXZmLiDvf4GvIttYv00mbAX2R6I67_zD57i7eyN0xILgpJcEkbZlItJK4Jn_x5dYsVvb2si9odS8yFJKfY_Jentq9kIj_of-OG8dtK__6JsE2aDTP9a0X5K3uQy-4vJXDxkC_TRyabVWfEJ1eMnHl57khFxt9hcrc9Op7Kmis_ue61naJwvW-_frlfljKrI5QWGOBn3_snKFho3X_KrEJryWXagQXRPDoqOBLQNygrkJmy8-e9aIE1lLJIZzeOql-ZjvJa-2CuLCQQ-9Em-WTxRVRNoPadAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ايمان قياسى: تمام دنیا درحال تماشاست که رهبر شهید ما چقدر طرفدار داشت
🔹
آن آدم معلوم‌الحال توییت زد که فکر نمی‌کرد این میزان جمعیت را ببیند.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/447113" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرودگاه بندرعباس پس از ۴ ماه بازگشایی شد
🔹
فرودگاه بین‌المللی بندرعباس امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از ۴ ماه وقفه، فعالیت عملیاتی خود را از سر گرفت.
🔹
پروازهای مسیرهای تهران، شیراز، یزد و مشهد به‌تدریج به برنامه عملیاتی فرودگاه اضافه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/447112" target="_blank">📅 15:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447111">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752606bfe.mp4?token=ubSbyQoHiiMpW2hrtrLfT_LIVpCJ0kI_HWMW31yYhKUI8Z9CDbrjCIPjiwIvCCTXRo8hl5OPk902TXpikLS5NnieYNkQlto2egCENqCoK2Q_6bKALvkH3Xjs5I9ct91m_rxEaomK43jPdE5hgQaHsnPRG6Pco63bGQuGX3EoP8_pPgo1gWeteMMiOM9Ypd9_G_-FPWImN6A8Mf88iiR4bkuzhyxgVYeKlLOB_CkyOviwultZ_ZUMF5tbRqE_gPjpPz3IV8_Y9YQHLwkP0ajtd3WfvkGvvrcHX_QrhNCjrF4ICn6A-ZNaa3AKn69LBdguuTTEZcx_cK1WITBsLwEO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752606bfe.mp4?token=ubSbyQoHiiMpW2hrtrLfT_LIVpCJ0kI_HWMW31yYhKUI8Z9CDbrjCIPjiwIvCCTXRo8hl5OPk902TXpikLS5NnieYNkQlto2egCENqCoK2Q_6bKALvkH3Xjs5I9ct91m_rxEaomK43jPdE5hgQaHsnPRG6Pco63bGQuGX3EoP8_pPgo1gWeteMMiOM9Ypd9_G_-FPWImN6A8Mf88iiR4bkuzhyxgVYeKlLOB_CkyOviwultZ_ZUMF5tbRqE_gPjpPz3IV8_Y9YQHLwkP0ajtd3WfvkGvvrcHX_QrhNCjrF4ICn6A-ZNaa3AKn69LBdguuTTEZcx_cK1WITBsLwEO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مادری که تنها یک آرزو دارد
🔹
مادر یکی از دانش‌آموزان شهید میناب که برای مراسم وداع به تهران آمده، می‌گوید تنها آرزویش این است که فرزندش امیر در آن دنیا نیز همراه و هم‌نشین رهبر شهید باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/447111" target="_blank">📅 15:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447110">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0t3qTEKRXhynbAJdTkJqLmJ0krlmgRr5Za2YIMc-Jyy1F5qCLD2_Sq_L9U_4ema2lIc8MFt35JZtBUgocnmejyL85uJWEqr48X71jcWRFkbA_NThB3TEDavGhz8oX-yreQm7szq7pPYvfLyJZvkTVFW_vGpGNLKYqj5s3BCXst27UihI2Hx8yPPGEIFL4wZ637m-7uEqmW7Av3ozho2G5CBUbfVTbb7r7Npqatvf3c_ACl-15QKyWqyykBe6U9Yy_y6TxeE4G-DjmdD_21XE7OrpoK8kcr8pDMlqbkwiBDlkILPz2aFL8rGM5uWyHuzDNQ3YMCmL0BHr9ZG8kRN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«أهلاً بأهلك يا سيد خامنئي»
🔹
«وقتی رهبرمان حضرت آقا به دیدار امام حسین(ع) می‌رود، ارباب به پیشوازشان می‌آید و می‌گوید: اهلاً و سهلاً بک یا سید خامنه‌ای، یعنی به تمام افراد خانواده‌ات خوش‌آمد می‌گویم.»
🔹
آخرین سفر حضرت آقا به کربلا سال ۱۳۳۶ بود تا امسال در روز چهارشنبه ۱۷ تیرماه که پیکر مطهرشان برای وداع راهی کربلا می‌شود؛ یعنی دقیقاً بعد از ۶۹ سال حسرت.
🔗
قصهٔ دلتنگی‌های رهبر شهید برای سیدالشهدا(ع) را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/447110" target="_blank">📅 15:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447109">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7823b63ea.mp4?token=dm2lJJA3UGOhq9pn_P_sqnBtLNkyyHjWO7FEucJrYMok7J0A36OphzB611EKiw3JqosRofwBs3FV33qbZVnSE9IKiKxmlQils_IobQTVmYAXOOxPTOFEMAK8AsP0-5rKOchxIfbjl9hpBR2GQxY4KhenErdEW-iWTLyc9hNmNug-wSlCAs0sJ-FRnfEjjgZQmAeMkV_gzh6yXOGHcrDglanMMMd_ws0nSBLzY59cYfq9XbTmAuTc9secuvlaot8-2PDBGn4Q9tasoe7Bfl3C8rcdhaupnpOxFdTtzOwV2QIXQTDaDvsIEqK4mAtykhTu_bbDuV0SlyF7p6RqbsxpRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7823b63ea.mp4?token=dm2lJJA3UGOhq9pn_P_sqnBtLNkyyHjWO7FEucJrYMok7J0A36OphzB611EKiw3JqosRofwBs3FV33qbZVnSE9IKiKxmlQils_IobQTVmYAXOOxPTOFEMAK8AsP0-5rKOchxIfbjl9hpBR2GQxY4KhenErdEW-iWTLyc9hNmNug-wSlCAs0sJ-FRnfEjjgZQmAeMkV_gzh6yXOGHcrDglanMMMd_ws0nSBLzY59cYfq9XbTmAuTc9secuvlaot8-2PDBGn4Q9tasoe7Bfl3C8rcdhaupnpOxFdTtzOwV2QIXQTDaDvsIEqK4mAtykhTu_bbDuV0SlyF7p6RqbsxpRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هموطن مقیم روسیه: فرزندانم در روسیه دانشجو هستند و با تمام سختی‌های موجود، بلیت تهیه کردند تا خودمان را به تشییع رهبر شهید برسانیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/447109" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447107">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgnLt8xq24H5OAVsvJfRzZkGfm6jczp-IpzHpABWr8XwuVBEYkPwH2HO6kxAxoQ8P5eKV2vZM6CQBoYXKhHvreF-j58PnaPGbngkjBNcLJcapw3GWmjR2Vetiv6RW6guc3TRcYsfLfPATVGp0t6UoyYyvViihuTMKUQAI2nUUMJQkasJ7HxI0FtboCmsWJeUvUfZlWlcmmZsliAiGxEdn9h8bPOLqp7TgtE9ixdjeUYBBDuwsPEf7lwKnPneJzVrN-mbVd7XV2NvxP062uQ0tdUd_fqJuiO2MmZklMHc6X5k0oiMQRyIdk3dlYBxUQx-FiqP0zc3v9SQColKz9x2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی تارتار به‌عنوان سرمربی جدید پرسپولیس انتخاب شد
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/447107" target="_blank">📅 15:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447106">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il0kwBYIVhEeqGXRuKCRoh4vVOE4CgWbK2xcXWzF9IJHH4pnNUymj7o7H2VLjC9LSL51Yb-UDAAxUsQmZSVEQNKb6ZRNSXC1dSJ4zC9XpR5A3Be7Q0reQmFUWjkx-vmuYMoKN-6GgHhj2lxhk5TLkSTLCZbDm5CbBIR_KdxBiO5F96KxA9wo0sWXPpiMJ6fC5I206R-UfGDrOFR4J_naFNHMcGaphvqlIRosMG9iRHgWJdUEKXNH6dywOEirtW0Yyvlvi9iKUsoTGPbOuITYiFsuLBkOCzehUrNk1zMHTSMHXhK_Kc69XIiivk9ZJspYG1tCvfup8QK-F89QzR1GWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایی از مراسم اقامۀ نماز بر پیکر مطهر آقای شهید ایران در مصلای تهران  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/447106" target="_blank">📅 15:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447105">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125ff3acff.mp4?token=hwLypEhXckZTX5T4zd5ZqyvOrxwFTCMbTv4_khFKyLqXaq1uQPtYCHl1EuSTgMNPt4cJMhL-SWhNC0jvWXBp1Dh3Qg4o214P6HdZgwR2SGtSx1DHAM3pqzlSBsItLGC5vlGHR-6BLMo26dHWktBxTHTf5SsaF54FBt1EC9pSpeejnZRr7S3J3Us4lrXpj6yjZyajOk2F-5XuSHixQerujGItwKAc_qYUfVoN84425Z_Fjrb5lZ5RJMbhVm3INjDMRagDpRExvLQVV3sM7wIaTtGcQWjjCdCP3HHIBTEgDXYxWyRV_9_35bPOpFxy0lcK0XGyMdUOENesuaWgukN6zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125ff3acff.mp4?token=hwLypEhXckZTX5T4zd5ZqyvOrxwFTCMbTv4_khFKyLqXaq1uQPtYCHl1EuSTgMNPt4cJMhL-SWhNC0jvWXBp1Dh3Qg4o214P6HdZgwR2SGtSx1DHAM3pqzlSBsItLGC5vlGHR-6BLMo26dHWktBxTHTf5SsaF54FBt1EC9pSpeejnZRr7S3J3Us4lrXpj6yjZyajOk2F-5XuSHixQerujGItwKAc_qYUfVoN84425Z_Fjrb5lZ5RJMbhVm3INjDMRagDpRExvLQVV3sM7wIaTtGcQWjjCdCP3HHIBTEgDXYxWyRV_9_35bPOpFxy0lcK0XGyMdUOENesuaWgukN6zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این بوستان یک‌شبه تغییر چهره داد
🔹
همزمان با آغاز ورود زائران مراسم وداع و تشییع رهبر شهید، بوستان رازی تهران به یکی از مراکز اصلی اسکان مسافران تبدیل شده و هزاران چادر در این بوستان برپا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/447105" target="_blank">📅 15:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447104">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3b8409e0.mp4?token=bMoXEGmBnBSreu6Vd9cvyiU9lq15T_OTxT1hFENCdUN8vkoDpTD3yqjIAKFh86zbWjx9VSXO1DUAK7i951HQs9m3DpkryiIYc6ckm8eYBPIs7vKpiPQnrVd2VrXKwPydT5QetSg3lsYXjkNmWGdX6QuCqMLe8uKRjdYKwJQMN6KMGxFfbyLAK2VoqffoK3EN3Z4Hi5v-dtzS2-IGW01U2F2z9x8qxf9lnJwte98fc-5r32iGozq8-rIc10fvDOe1nXFU4U1OYDSTG8ui4J58rDP-X4vTuUH003ISzKFk9qJvkv8Q4zXVPWnScSCwe5mJPAXRH-45Z7Xdmo27bNFWRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3b8409e0.mp4?token=bMoXEGmBnBSreu6Vd9cvyiU9lq15T_OTxT1hFENCdUN8vkoDpTD3yqjIAKFh86zbWjx9VSXO1DUAK7i951HQs9m3DpkryiIYc6ckm8eYBPIs7vKpiPQnrVd2VrXKwPydT5QetSg3lsYXjkNmWGdX6QuCqMLe8uKRjdYKwJQMN6KMGxFfbyLAK2VoqffoK3EN3Z4Hi5v-dtzS2-IGW01U2F2z9x8qxf9lnJwte98fc-5r32iGozq8-rIc10fvDOe1nXFU4U1OYDSTG8ui4J58rDP-X4vTuUH003ISzKFk9qJvkv8Q4zXVPWnScSCwe5mJPAXRH-45Z7Xdmo27bNFWRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگم، دلتنگ لبخند آقای شهیدم...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/447104" target="_blank">📅 15:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447103">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqeVvm6knHl3367DNmdxf6tFPXdX8RgBytv20_G2UhIqMCxdNvi1kUfleIJjEv8eNOUsHfMWpel2fb-416R-fuFF02TLN5TRF9BnrpbyIzeomFtOSi9TkKgtpkd9Zcd5eodVpkoohMic8cpNh72qYuFSDzbGl_G4U6T5VHfm7NAzmUUj72DOSlrqKsdf7OVJRRzdCTv2x94m3mFX1MWaFsotTvimBSX3u-7u2XMZyexmN4Jc_O2VIY1gclTsFIS6n6G3oMLbpqFMTyasUBKA4E8Ho615Ey9b5h6wb5UvcmH4aNikN2Dw-Z8so8qAgguox5SHrsIbWRVXGy3chzwmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ حرم رضوی: در راستای طرح اسکانِ زائران تشییع رهبر شهید، تا اطلاع ثانوی تمام پارکینگ‌های حرم امام رضا(ع) تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/447103" target="_blank">📅 15:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447102">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5a210eb4.mp4?token=Cs4Truh3rgSnSvWkf3MXMUONnWUDAiIhF6MT-BbZXru1JB2yU0E93ZiyjViOrFDGXAUFfDkqD4JHJm60UmEeT2CaUGAeeWTAqZDpQVhPQERMnJ_r7g69mbhUHXX5DfPcwZnx7xOzKnkFqU_kN4xBL76s3WZwmcAE_1CaUI3yUT8O_obS8kuMWPoyU15oVj9HbEwPDdLvpEZr_JtpOLHxHYskx8CeAKBXF_CDMIb_twXxgtyWa8b8bOKkGQ1a_N-RiucndiuyqVp__1acgvznG1G3Lk_QuzkqL-U0gA6bNGGFcpg-fydX_U8PZRlbL56Eod0jGAtkGNmVDcXcvCWo7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5a210eb4.mp4?token=Cs4Truh3rgSnSvWkf3MXMUONnWUDAiIhF6MT-BbZXru1JB2yU0E93ZiyjViOrFDGXAUFfDkqD4JHJm60UmEeT2CaUGAeeWTAqZDpQVhPQERMnJ_r7g69mbhUHXX5DfPcwZnx7xOzKnkFqU_kN4xBL76s3WZwmcAE_1CaUI3yUT8O_obS8kuMWPoyU15oVj9HbEwPDdLvpEZr_JtpOLHxHYskx8CeAKBXF_CDMIb_twXxgtyWa8b8bOKkGQ1a_N-RiucndiuyqVp__1acgvznG1G3Lk_QuzkqL-U0gA6bNGGFcpg-fydX_U8PZRlbL56Eod0jGAtkGNmVDcXcvCWo7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حیرت تحلیلگر آمریکایی از حضور پرشور مردم ایران در مراسم تشییع رهبر شهید
🔹
کریستوفر هلالی، تحلیلگر سیاسی آمریکایی که در میان جمعیت عزادار در متروی تهران حضور یافته بود، با ابراز شگفتی از شور حاضران گفت: عشق مردم ایران به رهبر انقلاب و انقلاب اسلامی باورنکردنی است».
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/447102" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447101">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75d22ba7a.mp4?token=AQvbCL2wJREm368wlyebxitp8oCQ-g4qapShUIxROth27V3Z3taY0U9zR9Rxr4F_mHUVs4A3BQjA272kQxbOC6QzprR0e3WqKdyB_TXHA6CXiJrxdMbScaAzRoh2OdNaxWGDIvjzpA3ktjUzEBs51XDiZ6gJr-SBkydOsBg2oRhKt5pjWOBq060WJ13tMwyLt9ucNjNemOXCLdZENlk3DqrC_EtsrMNpUSRXmOYfpD1BRxawxrwUxpMEDPlUKsAeihthZnHhh_7X7nctCRMGMv_JFH-K5tV8CxQJiAgpo5LJcTawtNHc4sV1AaXdGmZ5Nf119hM5h4argV_yoL6hrmyGNgJiONDej84CVuE1j02B-7JemhnG3tOp-2UWlch8f3CILfYveQ66KFbO4lisLJ3sabDfH9NtX_6cLOqHrNqrr1xZaysXCkRBwi_GA0_ovT7uhoMfCfz_I6f0HI6Tm3uUyBfhDEXhUMjvtf1jNP2z_vIvGgorb7K6qxNpTTTA7DF9L0G0Pkwwtv5YqDyRmIxLHQk4Wxgw-r4yZzhus7-z7PDxfbUh-08R79McQEMZAE8DNEmmq3CxXJb-2ypUvKH7_qv7K_6RtGtWmnODavPYHOtLkSwUQiXXHsJ816sPwFkT34hPcxB1UDdDIvcuDZPDWc9oq_7usP11AOM6MY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75d22ba7a.mp4?token=AQvbCL2wJREm368wlyebxitp8oCQ-g4qapShUIxROth27V3Z3taY0U9zR9Rxr4F_mHUVs4A3BQjA272kQxbOC6QzprR0e3WqKdyB_TXHA6CXiJrxdMbScaAzRoh2OdNaxWGDIvjzpA3ktjUzEBs51XDiZ6gJr-SBkydOsBg2oRhKt5pjWOBq060WJ13tMwyLt9ucNjNemOXCLdZENlk3DqrC_EtsrMNpUSRXmOYfpD1BRxawxrwUxpMEDPlUKsAeihthZnHhh_7X7nctCRMGMv_JFH-K5tV8CxQJiAgpo5LJcTawtNHc4sV1AaXdGmZ5Nf119hM5h4argV_yoL6hrmyGNgJiONDej84CVuE1j02B-7JemhnG3tOp-2UWlch8f3CILfYveQ66KFbO4lisLJ3sabDfH9NtX_6cLOqHrNqrr1xZaysXCkRBwi_GA0_ovT7uhoMfCfz_I6f0HI6Tm3uUyBfhDEXhUMjvtf1jNP2z_vIvGgorb7K6qxNpTTTA7DF9L0G0Pkwwtv5YqDyRmIxLHQk4Wxgw-r4yZzhus7-z7PDxfbUh-08R79McQEMZAE8DNEmmq3CxXJb-2ypUvKH7_qv7K_6RtGtWmnODavPYHOtLkSwUQiXXHsJ816sPwFkT34hPcxB1UDdDIvcuDZPDWc9oq_7usP11AOM6MY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماییم همه مشت گره‌‌کردۀ رهبر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/447101" target="_blank">📅 15:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447099">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/196556812c.mp4?token=Rd7RkfDiCg6IFcZYiYwR1nGjDuTMyoc_j5KKsZE9wYl6HlDxvIh9RVtwVSaJLa1WYxg7gA1YBzqfGRCoTAtHnHhJhBTvw9Q5xUpa7tdUCZUMI7hNAf_G7mNcHTRZTZIAdGZpf7iElbVFfvGNcFkHrLoTsZALi555PGKJ1tcLixjYkOCgbyrEBUvR0VheQ3Ex-70smgF0NZdR4AmGKRI-lY6zLouc5IbvLNsuNZL3Qh5CsuukvoqZae2v-gkWLPYCNwQu719Mp7TbtyGKq29tcISEo8LRYfKuo1cmn8L3kVvNl3VEeI3tsogXwluZz9IZ427jE1XmFxrxrTWr_KaSI3FiNVyjT5tPKbEWUoLbr6CNUaj1WFSehb3eFRzGiX2aXnuIuZV0Njd6IbgLw4_jNdtzNW-gn2ottra1NBI1FYa5cKNht-LZPmocdcskiT-dgG3BYhYfStJ5a2g9ULG1JXwOVoUkDjzTlwSHZ8ybXl0hcULtxx50DkX7vxRe1DP5uGHo616sKOE3UzP0mz_zz7NP5nL2QMKthJCvJeFGVmhv65QfesZTYAusqG193ciPvt8n41Zfwa-RptGkFhVvrbHZjuDIHvse-1IpJT2jkZxpUDjmPIC-LDGzy-f5wl9YWq56RpmUpn_VIl7eA4ZJ24xQw3uoKzhgVHz9LEORh4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/196556812c.mp4?token=Rd7RkfDiCg6IFcZYiYwR1nGjDuTMyoc_j5KKsZE9wYl6HlDxvIh9RVtwVSaJLa1WYxg7gA1YBzqfGRCoTAtHnHhJhBTvw9Q5xUpa7tdUCZUMI7hNAf_G7mNcHTRZTZIAdGZpf7iElbVFfvGNcFkHrLoTsZALi555PGKJ1tcLixjYkOCgbyrEBUvR0VheQ3Ex-70smgF0NZdR4AmGKRI-lY6zLouc5IbvLNsuNZL3Qh5CsuukvoqZae2v-gkWLPYCNwQu719Mp7TbtyGKq29tcISEo8LRYfKuo1cmn8L3kVvNl3VEeI3tsogXwluZz9IZ427jE1XmFxrxrTWr_KaSI3FiNVyjT5tPKbEWUoLbr6CNUaj1WFSehb3eFRzGiX2aXnuIuZV0Njd6IbgLw4_jNdtzNW-gn2ottra1NBI1FYa5cKNht-LZPmocdcskiT-dgG3BYhYfStJ5a2g9ULG1JXwOVoUkDjzTlwSHZ8ybXl0hcULtxx50DkX7vxRe1DP5uGHo616sKOE3UzP0mz_zz7NP5nL2QMKthJCvJeFGVmhv65QfesZTYAusqG193ciPvt8n41Zfwa-RptGkFhVvrbHZjuDIHvse-1IpJT2jkZxpUDjmPIC-LDGzy-f5wl9YWq56RpmUpn_VIl7eA4ZJ24xQw3uoKzhgVHz9LEORh4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقۀ تاریخی امام شهید
🔹
این روزها، تصاویر، روایتگر داغ یک ملت است و هر قدم، روایت مَسافتی است که مردم از دورترین شهر‌های ایران، پیموده‌اند تا در آخرین بدرقۀ فرمانده و رهبر شهید خود، حضور داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/447099" target="_blank">📅 15:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447098">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe0ef585a.mp4?token=VyrLRbZ8nCAo49FUJilL5aXeAm0rO37PfQfKSqBQy1NwwmmT979w-I1DPdTM710c-OYpSj7SFT2L-e_e-vNzk5BJl4D5POkQ2CIYQTrkQymVcU48-8t1tGLxqBkERW0MmfRGHYhirf8P0XIz4rvg36aqFSmzQx9YiLuUloIMhhKyf_rsMgg5wM3isB4rO1PR8Qwj08Q6GXaQQlzJ7-yq2ssouiNfvAAWPIJ8Ae1O6sYDPzlMn3Fp0wgbiyQ7pSjeSXrWdfNLz7qmPqiGyzF3tqkz5ButI_dsUHKz46tHOU2BAae6mc6dZ1GLI40bO7K9phzOnW_V0sprM5F8Zy0lwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe0ef585a.mp4?token=VyrLRbZ8nCAo49FUJilL5aXeAm0rO37PfQfKSqBQy1NwwmmT979w-I1DPdTM710c-OYpSj7SFT2L-e_e-vNzk5BJl4D5POkQ2CIYQTrkQymVcU48-8t1tGLxqBkERW0MmfRGHYhirf8P0XIz4rvg36aqFSmzQx9YiLuUloIMhhKyf_rsMgg5wM3isB4rO1PR8Qwj08Q6GXaQQlzJ7-yq2ssouiNfvAAWPIJ8Ae1O6sYDPzlMn3Fp0wgbiyQ7pSjeSXrWdfNLz7qmPqiGyzF3tqkz5ButI_dsUHKz46tHOU2BAae6mc6dZ1GLI40bO7K9phzOnW_V0sprM5F8Zy0lwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات مسیر تشییع رهبر شهید انقلاب و راه‌های رسیدن به مسیر
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/447098" target="_blank">📅 14:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447094">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOQr2W0fHkEyeaCEULL7Cdi4CcAMXCY21z5_2Gn1c0tqQlzDU_0SmpW9QKhrDQGuUz6Ep6HB-RdivFQE0qCFqZQgRu2Ly2d6N4YaeRds_eyxLkCuoEPPXwC3q8NOspN300JPZNTi7_fdvEKOMlZ85ycibXpkcIcNuhvg4vjL1TEXXqHmfFm3SP62oALGs2QgOqQdIWRapqOJwqgP1rormT-n8_6cxRpKfWn37NW_4H6VieWSPv1gk5QUSBmNlEkOoXeiRm7RNUyAjwkFgRkFa-HysVM1DZX4-_PTZg5XWrces21SRkrwsqfkYPZAk57YcsG-yFLPmemc54BXEp6e2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k19lyXW6Yvnp6QdCUqH0LI_oSUs9v4EnvCdtSXxHaQD-mmJKc2Mts-8i-NvmYTqcIGrEyMDhmvDHwp0NIvl29QyeeiDVmleeiXyNcv2k2Kki6DiANXPNZ0Go7GVbeWbBuaFO-1cLHgztTxf4Wx_ZFfkdVPVJgsmVbNnA27lnB4PWTRzgSsUidY9uzccBG8E-0yYk3PG33azsnD2_2gKR9QvlXHLZy5fwFj1kGpX1lytwBCcUE-WIfRgiOEUkLlr8EWbICM99DpbMvgdfV-V3L_SAiBfiXMKDmLZvaaQJXxqGA0gGExXYo4r9rpSSEoDo6asUsSbSycqeqyX74K-rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jMzTNqq_lOLC_XRf4qPWE8yj3kV72dhDvn_cENlNCKWCUI5Squ6SYzwEmVuOtnebXBCqlY7RHRnB7v13aLt6I3_7HJJp24nMPbq2nVHXHFCVFHyKnb-lmYYrszS7bawY9BT5ouyZ76dhGzTUaWR17RWfIn6BqeKKndQgbaRy5a8inKWpFIa34E498EbDUHkVEf3XZfwCpTkF0RpCBFgMXMRh7UExkqI-ongsfizrUhWAIyeO2rpBBAvClx_4oQVA4RGD9R_prLUy8bD6Zphq13QxkRKAKPHYu1vY1a2Lvciq-iV_9EwcDwwsvGslI9yTyfpYpzz6Y6PLZVujKS0Dcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hp_xTwIqPEEW1iO75E2Hh7MMKThQB9LJYFa8Q1RUoLrkX58ifDWykyojHOWtUpssP4SriChizHoxXpZMbO2wNO7cHQHfU0s4ucMASecDG0f8cVd41MeLhqRbn5dxzrc_z9czmxTorsYcxkwG1jHiBHMecSvC_vZCfnhLmuXuxQUIzyAiRbNHe57stJTBOc5tfoQFUidzKmrv-b0IdeUMAxobTdXH2WJ_uGCCnvg_p_Wt5haaQIaIsIHDInVuPfCl8_SDiY_-E888fY1rF7QtteJteyHmjMnaPkYOcB4eD_R_TWWzCuNxr8UIBQYEHm9N7Oja7ffBvT4hdKCt_qjQHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور سردار وحیدی در صف نماز بر پیکر امام مجاهد و شهید انقلاب اسلامی  عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/447094" target="_blank">📅 14:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447093">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cbee8f7d7.mp4?token=QV_EU1eVzNu8peJ2Je3PiH-cX1KO-zoLsVxSJHRQZz39E_gNqHRwWOTorHxBPIe3g8tqBFyaAnaPfQ_XAOKaWBp_u2Fo1HXubmJMMHKHLULe83yW4m8X3XnxvaoYpgZ6sgzlMsUzkUaLQnjVtnmwZE4V0wLOcp-KXp0bUA2ANmLOmHJweYhGWnScYa_vFUPw5NldRr9J39kAXN-WGLCkvBP3R7BWopkp0LYqrvcJpIZw-AAwV3jPAmWqHBbIkAWbkZ27VLVEkZRkLtB5BjyFkLbVm3Y5wHZgEzBHvDGDCKAXdyTF5h4MIjVVz-uohHQEfuwLi8f5HYCxpdyjHCd-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cbee8f7d7.mp4?token=QV_EU1eVzNu8peJ2Je3PiH-cX1KO-zoLsVxSJHRQZz39E_gNqHRwWOTorHxBPIe3g8tqBFyaAnaPfQ_XAOKaWBp_u2Fo1HXubmJMMHKHLULe83yW4m8X3XnxvaoYpgZ6sgzlMsUzkUaLQnjVtnmwZE4V0wLOcp-KXp0bUA2ANmLOmHJweYhGWnScYa_vFUPw5NldRr9J39kAXN-WGLCkvBP3R7BWopkp0LYqrvcJpIZw-AAwV3jPAmWqHBbIkAWbkZ27VLVEkZRkLtB5BjyFkLbVm3Y5wHZgEzBHvDGDCKAXdyTF5h4MIjVVz-uohHQEfuwLi8f5HYCxpdyjHCd-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از لحظۀ ورود پیکر مطهر «آقای شهید ایران» به مصلای امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/447093" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447092">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de39fe86b.mp4?token=S9MWY4VcKJNUa1QYkAqWN9Ry98DBn56s4aV6B6fU343QFdQKNMLumTHY_-ZCrdkylaAhtAOrakE81b0BvH9Ssk8_P6uE5KZeg0o2HleqxfePhTL-k3IADXurSHIGXwjxTutMM_VhR7j2tlo_LhlACynCq0Yyiuk3Vx_E-xT3WtaIS3AJDvhwKBpzJTXp-3SpL54ZqBHlIps4ZOtPSdvViC7HVfFtfVX_sxNshLrCae-Re6Mn-pysNHlQQrNJ6vqGC_wiu55JRHVFqJ9cPG6wPFnNB8VQ1qyxNK2tdJDmWWVlNPso5jetsFrjZgeYe7bzA9_M8rMo7k-6Z_aaD_Y5RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de39fe86b.mp4?token=S9MWY4VcKJNUa1QYkAqWN9Ry98DBn56s4aV6B6fU343QFdQKNMLumTHY_-ZCrdkylaAhtAOrakE81b0BvH9Ssk8_P6uE5KZeg0o2HleqxfePhTL-k3IADXurSHIGXwjxTutMM_VhR7j2tlo_LhlACynCq0Yyiuk3Vx_E-xT3WtaIS3AJDvhwKBpzJTXp-3SpL54ZqBHlIps4ZOtPSdvViC7HVfFtfVX_sxNshLrCae-Re6Mn-pysNHlQQrNJ6vqGC_wiu55JRHVFqJ9cPG6wPFnNB8VQ1qyxNK2tdJDmWWVlNPso5jetsFrjZgeYe7bzA9_M8rMo7k-6Z_aaD_Y5RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظر فعالان رسانه‌ای پیرامون شخصیت قائد شهید امت و حضور میلیونی مردم در مراسم وداع
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/447092" target="_blank">📅 14:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447090">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9yZtKN4E1SSCVFjiwXTf9-tCWuFwnkfsuuokCz42Tphed_JiZnAasnEYdm-mKN3MqjDW1hVutIOGwODZafBlfcrkWihrTf3Xj-G4UNXUdIsKtcTmRRiko7o0UNz3Mb8Nf0cK_Y9p5xBUpIYh43e1x4GFmE0M8Vgn3zxrLOwOfh0Usk0LHAyiX8bhclnPeIDT4UzX2Znidov9PEZmMw-1ZlyRspACxZz5dBJBniXO2h6uMut3jSPdxVBbZDhplWLwMhpjyc1FPsy1ybhtuyAlReMFoOTBEFv-sMucK7l9xN8kPOwm7Hi7EwFdJPEkRvQdxR-s1_3-G5pHQZOD6Aqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQ3Fx02BZA-YVKIT9OH-JRsx432JhO-Iu_AL_FR4UVMpohuh0C744mywXU3A6hU5O78P7hcq4FyP3bCJka1pWISgbupiZlFbt_tsbY2LcbKY_lMBRsk3D12iiijylaIiZFVmC2rX91Ti_Y9NtIxe7qZ6SnFu6yMas8TILKcRIK3DlmQp2g5kDTVPyrYH9qDLrXeenU6FLNrM0GcVg3Zo0Jl_FsxPq4UfD4kXnYm1MDwzrc32PnnezGRcq6kI8A1gxqOGVnx3QuKSMxBwCNF1jcBN6eV7olsajSS8sVacg__yR4ysLJdNvRTZwkGxA5krNu2SMlM-mykSJR7MqsJ8vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کتیبهٔ تشییع رهبر شهید را این زن نوشته‌ است
🔹
روایت نوشتن کتیبهٔ عزای آقا را تعریف می‌کند. حرف‌زدن برایش سخت است؛ لحن صدایش غم‌اندود و کلماتش لرزش دارد. حرف می‌زند اما منقطع و با مکث!
🔹
حاصل کارش یک کتیبهٔ سیاه ۸۰۰ متری است که امروز همچون بیرقی سربلند و ایستاده، مقابل یکی از درب‌های ورودی مسجد جمکران آویزان شده است.
🔗
ماجرای شنیدنی توفیق کتیبه‌نویسی رهبر شهید را
اینجا
از زبان هنرمندش بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/447090" target="_blank">📅 14:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLcqLnFR0sJAiy2eJeVQGMXOTtQQ3MkLmZ-t5gmqR7hBqOMGUmiD3NJ-aue2VbH-yzAJMR6_jBGYtNmcLPcIRzJQu_Gn18aq1xkMVKkWBQRjrWqQ3nCEToBW_P5-090gX5uCEiC8cXgkQJJdQEB0OVXncXH7w-KUBy57j7X4LQfgEbKQmAdEG_HhPqW-H-GVmQggSBwM-QXbPXFP8FmHaLVRof_bfMKO676tiLwbvt5Pf5VF19ldURxMIdEF2MfOPYUxoMkpZMnR0URLjRk9ZrklWJCKIo3JGM_6saoixNJL23yt0MaROfY55xQtvqKcdTyEhJv957n3PNhSfxWVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
وزیر ارتباطات صربستان از ایرانسل بازدید کرد
🔸
وزیر ارتباطات صربستان که به‌منظور شرکت در آیین تشییع رهبر شهید انقلاب به ایران سفر کرده، از دستاوردهای ایرانسل بازدید و درباره ظرفیت‌های همکاری مشترک، با مدیرعامل ایرانسل گفت‌وگو کرد.
🔸
در این بازدید که ۱۳ تیر ۱۴۰۵ برگزار شد، علاوه بر وزیر اطلاع‌رسانی و مخابرات و سفیر صربستان، مدیرکل بین‌الملل وزارت ارتباطات و معاون رگولاتوری، حضور داشتند.
🔸
در جریان این بازدید، گزارشی از دستاوردهای ایرانسل در حوزه توسعه زیرساخت‌های ارتباطی، گسترش 5G و فیبر نوری ارائه شد.
🔸
مدیرعامل ایرانسل، با تشریح راهبرد گذار از Telco به Techco، آمادگی ایرانسل را برای اشتراک‌گذاری تجربیات و توسعه همکاری‌های مشترک با صربستان اعلام کرد.
🔸
وزیر ارتباطات‌ صربستان با استقبال از گسترش همکاری‌های فناورانه، بر توسعه همکاری‌های آموزشی، پژوهشی و اجرای پروژه‌های مشترک در حوزه ارتباطات تأکید کرد.
🔸
همچنین، گزارشی از فعالیت‌های گروه اسنپ و مجموعه ایرانسل‌لبز، ارائه و از مرکز ارتباط با مشتریان و مرکز عملیات شبکه ایرانسل بازدید شد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/447089" target="_blank">📅 14:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTcqtYnzyMhaTXI0RFadOQAY0qL_7t4KrSAYVCEx1N6MQ6GQxC25Gy-_YHoKW6nY7zb4W_V5iLF-z9JauPjavFDHZSMSmK_TFpRvkYFlZKnSDmH5UTZ7qMQFnV9Q0DVuoKLq1hu3jkdnpAa9gF8W8t1Qb6W3RCsoh7rXYDZXGJZAWLyN8MKyHEz19Trf16Z04Xm2Xrn5DV8pZfk1j6mDwAF1AGvrHeo6eVfITI3-8c7uDN8kSzxszqM72_D466E6o1-quwqnp7eRXnrMA29wo6uRwfkFsvaK0xygKQKSeya4a3NbFfFv3TpqB6d5UiZJMRw-kD7ose28AjmwpNC88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالان اقتصاد دیجیتال هم در مراسم تشییع رهبر شهید موکب‌دار هستند
جمعی از فعالان داوطلب اقتصاد دیجیتال، همزمان با مراسم بدرقه رهبر شهید ایران، با برپایی موکب در مسیر مراسم، آماده میزبانی از مردم و دیگر فعالان این حوزه هستند.
وعده دیدار:
میدان آزادی خیابان برادران رحمانی جنب شهرک شهید فکوری
موکب فدا
https://www.instagram.com/mokebfada?igsh=MWg5bTV1dG5nd2IyYw==</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/447088" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/447087" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsRr-0d0s5FwnqgKKuGWKFClzDs1YJ67w7p5EOnmReuSE_4LzRIrKWdqeM6V-WlRGCHboANRwdVQ9S5xCVTH02fvnmcPhhe24rp_YUao2FMWZW55mwXyrIkbWGM41doiw1rn2j0X-AFpfJ1JRTF68tV-mu0dCJnhP1gLXtDKTCliKov4ONqITGCcK0XGNnO4OK6m0cKWHqjn4lTJ8GrYcfJU1LAZCXwCAOmM6oGtOm9cdE2hLTF5bSlhkD8iT7Ow3q_gFBjZoO_usAX-FpgoemBQlnorCq6YpcjRG6qMhZel3WeEkyrYAi5ocVQgWspYmDpo4pfjjo5i_jmdfkaDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایی از مراسم اقامۀ نماز بر پیکر مطهر آقای شهید ایران در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/447086" target="_blank">📅 14:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447085">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07640df198.mp4?token=ImIZRhsKb9UaQvy6NNQHzWjWv0gpX6Ofx9OXPXdHg5SwsScewtinpGqr06qIIZaK3nFpmROFM7P3r0JjNTVkFGLh0QknKOSgHwOowXZBvykvaEw4LjWvVB3RqMzTJwb_XD-qsY9rgfHlwWi8jokYVbkK2MaNYh24WV2P39aUcE-LIMwp6GyE6o18DZ9tdcEWzAMgsjwe5D-b6EB9LewwyYaIOkUvLRtKG5_aWDbFH_C7t7o1RlFxPegEl-NMJUSYjWoqdEO9ud2Cw3_EdfQFrLLhlN1ajEhHzcKrPr5PmJa45x3WWyjr2-Pky7akFJ9vX_1aMDM32KR3UOVbohGfzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07640df198.mp4?token=ImIZRhsKb9UaQvy6NNQHzWjWv0gpX6Ofx9OXPXdHg5SwsScewtinpGqr06qIIZaK3nFpmROFM7P3r0JjNTVkFGLh0QknKOSgHwOowXZBvykvaEw4LjWvVB3RqMzTJwb_XD-qsY9rgfHlwWi8jokYVbkK2MaNYh24WV2P39aUcE-LIMwp6GyE6o18DZ9tdcEWzAMgsjwe5D-b6EB9LewwyYaIOkUvLRtKG5_aWDbFH_C7t7o1RlFxPegEl-NMJUSYjWoqdEO9ud2Cw3_EdfQFrLLhlN1ajEhHzcKrPr5PmJa45x3WWyjr2-Pky7akFJ9vX_1aMDM32KR3UOVbohGfzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام‌های جهانی یک مراسم تشییع
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/447085" target="_blank">📅 14:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447084">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f18a51cf.mp4?token=pGT73vwSHMx_k-WQnfV-eCxK77t--YvIXdmuNZrSd1nMbbOLzGTPhp8QGHgnscSstvsT--2-lcOw6pqeZZeI9k9PIXAcZZR1Rd7GGWl1sBtlWpCamH14wJzixIll5-adVXUPhDPiEYFXxxV_ypdtjVq22_esB-C1YwNmy0adKeiASDRAI0cELn9mQR3nY1tnzLyVFCR-pixeFj3egsoqooTXSmI9GMcfLi6H2-7-UIlLSTYMUGide_x3hxce2cA6HwdAHpAR1rgfoD2lMM1TnqUs0CBj7biRHKxBqb77J9qMmMckeFIvMU6cX5A2Z_2EjOroW_BzgF7aCC3DypWwB6NW4dO_tIx43l4Oy2zZVLe9btgBmXVnJrt00CEjS-mRZsrw7lv-9xajVVy9gWaLwUsf-uu5POy6WLE2mgd-KQ5QRcGd0II1HxDaNBEVCg82WL7dx0hVFXuwKHni1Z79_Tx3s_PmuBgFBYepxTJWpofvDL-qX5SIX6OtRhI3YkIuZdHeuLwDn3fI-_saKif3nf98409Wu8PIfCbtvAU53tUY2YNzmbHbYjsQDRLFAkv7BXp5pe7ZgAuNg89jYPhyNvkWHaYUPy8uSo3OHqg0p8DGpoJ5cXqZzFPY_YVZ4iYzc6p0m-AAk5LEhUlzIlxzSA47O4ySjSJtKQrQb7iX2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f18a51cf.mp4?token=pGT73vwSHMx_k-WQnfV-eCxK77t--YvIXdmuNZrSd1nMbbOLzGTPhp8QGHgnscSstvsT--2-lcOw6pqeZZeI9k9PIXAcZZR1Rd7GGWl1sBtlWpCamH14wJzixIll5-adVXUPhDPiEYFXxxV_ypdtjVq22_esB-C1YwNmy0adKeiASDRAI0cELn9mQR3nY1tnzLyVFCR-pixeFj3egsoqooTXSmI9GMcfLi6H2-7-UIlLSTYMUGide_x3hxce2cA6HwdAHpAR1rgfoD2lMM1TnqUs0CBj7biRHKxBqb77J9qMmMckeFIvMU6cX5A2Z_2EjOroW_BzgF7aCC3DypWwB6NW4dO_tIx43l4Oy2zZVLe9btgBmXVnJrt00CEjS-mRZsrw7lv-9xajVVy9gWaLwUsf-uu5POy6WLE2mgd-KQ5QRcGd0II1HxDaNBEVCg82WL7dx0hVFXuwKHni1Z79_Tx3s_PmuBgFBYepxTJWpofvDL-qX5SIX6OtRhI3YkIuZdHeuLwDn3fI-_saKif3nf98409Wu8PIfCbtvAU53tUY2YNzmbHbYjsQDRLFAkv7BXp5pe7ZgAuNg89jYPhyNvkWHaYUPy8uSo3OHqg0p8DGpoJ5cXqZzFPY_YVZ4iYzc6p0m-AAk5LEhUlzIlxzSA47O4ySjSJtKQrQb7iX2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز فرماندهان کشوری و لشکری در بدرقۀ آقای شهید ایران آمده بودند
🔹
امیر سیاری: تا آخرین قطرۀ خون آرمان حضرت آقا را پیگیری می‌کنیم و همیشه فکر انتقام در ذهن ماست.
🔹
سردار رادان: برای ما سخت‌ترین روزهاست. امیدواریم این وداع توام با سلام باشد.
🔹
جلیلی: آقای شهید به ما یاد دادند که این حرکت پر شتاب ادامه پیدا خواهد کرد.
🔹
آیت‌الله اعرافی: شهادت رهبری درد جانکاهی است. شهادت ایشان معادلات دنیا را تغییر داد.
🔹
رئیس مجمع تشخیص مصلحت نظام: امام شهید با خون خود کشور را بیمه کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/447084" target="_blank">📅 14:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447083">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61adb805f9.mp4?token=g_KdflN65rJQKsrFiQDx84F3FwjbZMRi8lIQQpmL-h-HAey9gasKxS4u5mQofCvk7ZXmQK3nGrRRd_-LUC4Jyr5jdYVmU2dBHC5QfzkK06WJYZJ3A0JfFyontCeIWqCunLNRNskEFcqnwUg3NPhfFw_L4aOrn-w6-6EYxCuXQvsSBU72daJNF2h5OphtFI38nkAvF0FHQYn43tKC9cHf_hokvtGjpyUL1YG_BHzJw-tinc9BI1S88aRJGoADvtQd7XNsIKMYdEuic6_ljLsyyBgZg3yoo1YTkhmr_4d0ShvVNiIHwF44gvj2d-yBqiJjV_O5Ds2hN6fe_jMJFU_cMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61adb805f9.mp4?token=g_KdflN65rJQKsrFiQDx84F3FwjbZMRi8lIQQpmL-h-HAey9gasKxS4u5mQofCvk7ZXmQK3nGrRRd_-LUC4Jyr5jdYVmU2dBHC5QfzkK06WJYZJ3A0JfFyontCeIWqCunLNRNskEFcqnwUg3NPhfFw_L4aOrn-w6-6EYxCuXQvsSBU72daJNF2h5OphtFI38nkAvF0FHQYn43tKC9cHf_hokvtGjpyUL1YG_BHzJw-tinc9BI1S88aRJGoADvtQd7XNsIKMYdEuic6_ljLsyyBgZg3yoo1YTkhmr_4d0ShvVNiIHwF44gvj2d-yBqiJjV_O5Ds2hN6fe_jMJFU_cMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: قاتلین امام شهید به مرگ طبیعی نخواهند مُرد و نظام انتقام خواهد گرفت
.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/447083" target="_blank">📅 14:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447082">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ed427cde.mp4?token=WgxA-p5mgMumIqW-tvwvNQ9o-oydxaH9H9N2RNvgSWMrFAzSf-I4OKpeLLa5eypwSF8ogbz75gAzRcHD5XcQPY0kPhwtso4Ac880RtpVPE2rnQ3kF_NfZAj3m0eAsjB83AIukSNSboFJ6WfNa_gV8yoiimN3Lj5MMrrhDbJbMBZu7NkhLsN4UZQRhzBPeZ68x1U1L7RW70eRkdTya_ziiqr48gxBRLWI0vztQeNJatd4DvqyswMriDcPFn8qkKWF8trHpZ7JNc0DTaHkPi6JOq9tsMuzlF0enBe3w1KvZvUjyUOhZiXfzP9TJZivlZRAzecheA8X0TMltGskYBfXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ed427cde.mp4?token=WgxA-p5mgMumIqW-tvwvNQ9o-oydxaH9H9N2RNvgSWMrFAzSf-I4OKpeLLa5eypwSF8ogbz75gAzRcHD5XcQPY0kPhwtso4Ac880RtpVPE2rnQ3kF_NfZAj3m0eAsjB83AIukSNSboFJ6WfNa_gV8yoiimN3Lj5MMrrhDbJbMBZu7NkhLsN4UZQRhzBPeZ68x1U1L7RW70eRkdTya_ziiqr48gxBRLWI0vztQeNJatd4DvqyswMriDcPFn8qkKWF8trHpZ7JNc0DTaHkPi6JOq9tsMuzlF0enBe3w1KvZvUjyUOhZiXfzP9TJZivlZRAzecheA8X0TMltGskYBfXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار قاآنی: امامی که یک عمر مجاهدت و مبارزه خالصانه داشته باید هم چنین عاقبت به خیری داشته باشد
.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/447082" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447081">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6562a415.mp4?token=bpxZ1JgRz9n65TegGb_W8OeeED0TfCS3wa_wCdlBhwPsLvJ2cKsm8WSmzlEJiTxx1G-kN6qzLB6bQgnK_NjdmzC0-pq23fdOHVDqba5r9Q-gbknvJHR0i4qZKBREELCNMsQpAMOfurTylWnYPBdU_BTNHaQ6DNTAn_RXYI0ycpRTAdkUQtxZ02ETWtGptEUYOEeuIt6WSBsiiE4IQItSnCVexzyM-wX0rMeA3E8XAN-BnG9xS7myC2ffMgSNCDXv3JiDXPyCacp5c5VYPolXU2kxcdrrLmNHAd81xcRMg96Dp1PfMJCXjdLnULmNZkERydF6xQ1IUoYLXo2ivqx7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6562a415.mp4?token=bpxZ1JgRz9n65TegGb_W8OeeED0TfCS3wa_wCdlBhwPsLvJ2cKsm8WSmzlEJiTxx1G-kN6qzLB6bQgnK_NjdmzC0-pq23fdOHVDqba5r9Q-gbknvJHR0i4qZKBREELCNMsQpAMOfurTylWnYPBdU_BTNHaQ6DNTAn_RXYI0ycpRTAdkUQtxZ02ETWtGptEUYOEeuIt6WSBsiiE4IQItSnCVexzyM-wX0rMeA3E8XAN-BnG9xS7myC2ffMgSNCDXv3JiDXPyCacp5c5VYPolXU2kxcdrrLmNHAd81xcRMg96Dp1PfMJCXjdLnULmNZkERydF6xQ1IUoYLXo2ivqx7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون‌اول رئیس‌جمهور: مسئولیت ما برای پیگیری فرمایشات رهبر انقلاب پس از شهادتشان بیشتر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/447081" target="_blank">📅 14:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11a1f635c.mp4?token=Mvb-qoRYfYYRVxSJfSBRQqITeXRvEwz2svKH8Ur_BlyAf4EzkkJR679Ujubc1ZImW5zayTLzsuqReipBp98tTVVItouMafSG-JBA0nZbhSSr9_wOTUEJPOjX-gHVYSzyrBYtopGW9HCd0brgey3-rKPJEjmkDtSL5uzFmLkNhvHIRddz3r66coCYXglzWUemgu4lZVWx3jPjGGP7Q0Osj1EktzuW6NA3afep-5Fat2ltFHhxDjd9uM858Ep63BPKtWd-XcNh-q8tAyZ20SwgJWLbNcDZ6FUw_g1eO-xBt0SN18BTp6qQqRQ87uuIJMqePCTqwj00ZFQAH0qcPMMyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11a1f635c.mp4?token=Mvb-qoRYfYYRVxSJfSBRQqITeXRvEwz2svKH8Ur_BlyAf4EzkkJR679Ujubc1ZImW5zayTLzsuqReipBp98tTVVItouMafSG-JBA0nZbhSSr9_wOTUEJPOjX-gHVYSzyrBYtopGW9HCd0brgey3-rKPJEjmkDtSL5uzFmLkNhvHIRddz3r66coCYXglzWUemgu4lZVWx3jPjGGP7Q0Osj1EktzuW6NA3afep-5Fat2ltFHhxDjd9uM858Ep63BPKtWd-XcNh-q8tAyZ20SwgJWLbNcDZ6FUw_g1eO-xBt0SN18BTp6qQqRQ87uuIJMqePCTqwj00ZFQAH0qcPMMyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف‌های ناگفتهٔ مردم در آخرین دیدار با رهبرشان
@Farsna
-
link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/447080" target="_blank">📅 14:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71a9da034.mp4?token=OinTVWz2AKCjGUf3D5W3A0MpcHlPlVkj9SL0HHJLwLyglQO25TJeS68D3gV-CWlWtgoxGlWxiQHIBjK8CIKe8qFhP8fPCabTaVZehiGImXlNLM76KwBW65QmG8kytPTfmBDpoM_VkTstWTgaX3UiiDllqVF4DfDRjlQPAmHRFw4ilkuwLY6SWQsFx-EPZctebkMZB8XsHuTkSOyajhEcBVP_gYnfm2xs_vXnmWaeJ3FVN_mliTheX66tvYo6MIjbjhEUgxF862u8xZOmyxrG72qlZD4tG_ulInxlA43UQqnLlq6h7vG_I9xowuZrw-KYmZbOtVXvAPOSf-uQKUM6vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71a9da034.mp4?token=OinTVWz2AKCjGUf3D5W3A0MpcHlPlVkj9SL0HHJLwLyglQO25TJeS68D3gV-CWlWtgoxGlWxiQHIBjK8CIKe8qFhP8fPCabTaVZehiGImXlNLM76KwBW65QmG8kytPTfmBDpoM_VkTstWTgaX3UiiDllqVF4DfDRjlQPAmHRFw4ilkuwLY6SWQsFx-EPZctebkMZB8XsHuTkSOyajhEcBVP_gYnfm2xs_vXnmWaeJ3FVN_mliTheX66tvYo6MIjbjhEUgxF862u8xZOmyxrG72qlZD4tG_ulInxlA43UQqnLlq6h7vG_I9xowuZrw-KYmZbOtVXvAPOSf-uQKUM6vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: قول می‌دهم راه امام شهید را ادامه دهم.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/447078" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cae1968d.mp4?token=KR75R5YCs2YIYo2f7G_5GMBpftPYOBZTudNTdsv0NgH3OJTXt7SJpzY55hKoMUoYjNTnKVvBttQNJCT9MXRJaWgPiL4utd6CLxhlMjFhRklhnRuWCpVzGl3BeX3dobPglQlVMR2tyqFdY4wuVRfARZjyVsgObZg2eJcbnbZk1NMSVLfckqOxUqGSV02YlKfvLZWUZNYh6qn-JAPg257AigKY1OyYOdb7tRvvG67bmLdo8GnHnhBLxtu8xvCo5MB0RDr_LUPBUAdoTCyISVp7Eev6otGFMKCfXw_MfITyamLfqvAJYHGVXRKNDuucA_PXKFm_CYI9DVyv0oYL6dMumQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cae1968d.mp4?token=KR75R5YCs2YIYo2f7G_5GMBpftPYOBZTudNTdsv0NgH3OJTXt7SJpzY55hKoMUoYjNTnKVvBttQNJCT9MXRJaWgPiL4utd6CLxhlMjFhRklhnRuWCpVzGl3BeX3dobPglQlVMR2tyqFdY4wuVRfARZjyVsgObZg2eJcbnbZk1NMSVLfckqOxUqGSV02YlKfvLZWUZNYh6qn-JAPg257AigKY1OyYOdb7tRvvG67bmLdo8GnHnhBLxtu8xvCo5MB0RDr_LUPBUAdoTCyISVp7Eev6otGFMKCfXw_MfITyamLfqvAJYHGVXRKNDuucA_PXKFm_CYI9DVyv0oYL6dMumQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: رهبر شهید ما بعد از این همه زحمت و رنجی که در راه هدایت مردم و انقلاب کشیدند نباید اجری به جز شهادت نصیبشان می‌شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/447077" target="_blank">📅 14:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32971e599d.mp4?token=SEU8AqKgcmW6rTabTCEg9bAvRzt4FyY3lIi6c5ksC4Opxjj1RZJJ0uu4597RpYt-pSMYm8_WPxrasrQRWtpuYwRNLyr1mYxSd_qNsuz6C_SNxqOOhNzIxspr_t43P2Y9n8CW4WGutgFfbBdpvIr5sXqfeuF6tYnIo7rXMOi1PWaF1SzhrjG2-xY0FjykJJ7ECM-uja9Zseq6EAtz8a-H6bDMDrLvrgvohnI9CjReTnhk9roLjqYIyOM8affup1p0oHzY_agE99eGjsIAHH-G8unCdtrbNQzhZmHrKCoSXcHu_ZsgJdN8nIW-erGqggWtumBipcYrPX9RU-7oxLTJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32971e599d.mp4?token=SEU8AqKgcmW6rTabTCEg9bAvRzt4FyY3lIi6c5ksC4Opxjj1RZJJ0uu4597RpYt-pSMYm8_WPxrasrQRWtpuYwRNLyr1mYxSd_qNsuz6C_SNxqOOhNzIxspr_t43P2Y9n8CW4WGutgFfbBdpvIr5sXqfeuF6tYnIo7rXMOi1PWaF1SzhrjG2-xY0FjykJJ7ECM-uja9Zseq6EAtz8a-H6bDMDrLvrgvohnI9CjReTnhk9roLjqYIyOM8affup1p0oHzY_agE99eGjsIAHH-G8unCdtrbNQzhZmHrKCoSXcHu_ZsgJdN8nIW-erGqggWtumBipcYrPX9RU-7oxLTJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: دعای آقای شهید از ملکوت باعث سرافرازی ملت می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/447076" target="_blank">📅 14:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9da0d4b20.mp4?token=PuyrJpV1JnF4lKinFlppO1YAK4Y51yjK1IvJaqeV83-vIO7m2SRKx2U51NRhiBIpMH8GxALa1okPz130EX_GjMIorSI1P94Xn8J2K8TRaq6Hb_g5d5xZt2AMywbbV4GryCrLcR_g9FHc-mVDWG80XdKC7HnjtxRRrkLBvniDDc9vHF9efvojEPQiZl_Ne8DKEsD_2WUvhuyemObk3ZsvnDVY0NW7r97X_0Hev11i1wp7EDVLOvUfyYvsSFKH8DDSDzq2snX_IoAdYvZa1HJ7nv0T9p9BABPGGO41iHVS6jTpCwmWWUDY1xZuiH27ltx8tF6AaZreZS52PLT-0FQyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9da0d4b20.mp4?token=PuyrJpV1JnF4lKinFlppO1YAK4Y51yjK1IvJaqeV83-vIO7m2SRKx2U51NRhiBIpMH8GxALa1okPz130EX_GjMIorSI1P94Xn8J2K8TRaq6Hb_g5d5xZt2AMywbbV4GryCrLcR_g9FHc-mVDWG80XdKC7HnjtxRRrkLBvniDDc9vHF9efvojEPQiZl_Ne8DKEsD_2WUvhuyemObk3ZsvnDVY0NW7r97X_0Hev11i1wp7EDVLOvUfyYvsSFKH8DDSDzq2snX_IoAdYvZa1HJ7nv0T9p9BABPGGO41iHVS6jTpCwmWWUDY1xZuiH27ltx8tF6AaZreZS52PLT-0FQyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده‌کل ارتش: یقهٔ کسانی که رهبر ما را شهید کردند رها نخواهیم کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/447075" target="_blank">📅 14:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3083582b70.mp4?token=qLF_rSmtq9sj9X2IhMDqdRGLP2F2SeGM1pIlqX-TqZY88GEXbVpOdPUp0d5IWlwoqT1S_Ax-UCQp5wjma5gF5vvohJEYn0ruuA8AYPio1riZHbl24I9F1bVoN9bop72UnRzZlHTvgpmdhnfYOaK0qkRCjQPHXXqnW_qZJhxIo5XZQUOYEXa7Q0GI29nPZyC5_Hflv_-jnxHMMzJnFbM9PCDDIty9felfNrZQ8dpMhdhWSShbKbCouW1blh6VJALoFpXgks-mw0BxJWoRotm0rDQySbI78QDUoAyBWu1talCv_lUUjzo61sARmWSVaEunNaRtnt5e51aMiRqKZFHZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3083582b70.mp4?token=qLF_rSmtq9sj9X2IhMDqdRGLP2F2SeGM1pIlqX-TqZY88GEXbVpOdPUp0d5IWlwoqT1S_Ax-UCQp5wjma5gF5vvohJEYn0ruuA8AYPio1riZHbl24I9F1bVoN9bop72UnRzZlHTvgpmdhnfYOaK0qkRCjQPHXXqnW_qZJhxIo5XZQUOYEXa7Q0GI29nPZyC5_Hflv_-jnxHMMzJnFbM9PCDDIty9felfNrZQ8dpMhdhWSShbKbCouW1blh6VJALoFpXgks-mw0BxJWoRotm0rDQySbI78QDUoAyBWu1talCv_lUUjzo61sARmWSVaEunNaRtnt5e51aMiRqKZFHZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از مراسم امروز نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/447074" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d975d4917.mp4?token=top2XncKAawPE4WzvgiJcDfBvwk_15TVXU4oE0kSqrd4WVIWg6YGLTob1H79coyM_gzfE5N6KNpiR_1DJQQ41UOu94JoOAwVO8GbjGi9WvbeJAknJiOgRj9wE1BpNTs11ir9e3PU60-fZGGDwI1JjpNMsX6LpvuwMnQvRvolMNiQE_WFa0jjv7umcW-tbEX4d-bvskF7ZIGGqG0eT_bhq_O31Jd2wApnmJlela7u7RUiakGGI-Nc_5tk7IGOXFQUtUVimj2PpO-CiaM9sIbGBGn8vYyzFUddXaEG8gRqlkXVv6TRRY42WRL4Kka6dWuSOf7H-rEFN6LKTS75CcCwqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d975d4917.mp4?token=top2XncKAawPE4WzvgiJcDfBvwk_15TVXU4oE0kSqrd4WVIWg6YGLTob1H79coyM_gzfE5N6KNpiR_1DJQQ41UOu94JoOAwVO8GbjGi9WvbeJAknJiOgRj9wE1BpNTs11ir9e3PU60-fZGGDwI1JjpNMsX6LpvuwMnQvRvolMNiQE_WFa0jjv7umcW-tbEX4d-bvskF7ZIGGqG0eT_bhq_O31Jd2wApnmJlela7u7RUiakGGI-Nc_5tk7IGOXFQUtUVimj2PpO-CiaM9sIbGBGn8vYyzFUddXaEG8gRqlkXVv6TRRY42WRL4Kka6dWuSOf7H-rEFN6LKTS75CcCwqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله سبحانی: آیت الله خامنه‌ای با خون خود درخت انقلاب را سیراب کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/447073" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5i-bYXBt5uM8LlYhp-Ru-O8U9huv4-LpxOOqBZZjiKPQbkeBxbYhwPcS6h4uNBXVpZMQXd6I2gZa0pl5vMq7DeniLNqPj1MaSQAxyan_bb7HXhMiuubC6O8RottSOoYQg2CcZ0yGDvl21xrQx3YojZBA5TxnCeqcIoFq5PzQ8bYJhVmnWz_2c3PoiqU4L_YZNopLtU4E_Do14TnsNNiTDmgZadIZhaiFpIEZ2YsTUZpwSanou8SxLRO7C_zLgBDjj2omiErNgIvnaiyyoZAxR1VkKa_HmwdkjLTIVm-QygnaRemgMYuSZf692d-a6VFP1Q5OEVh870fBCGoCPFN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پویش ملی «آخرین دیدار»
🔹
جهت ثبتِ تاریخی وداع با رهبر شهیدمان، از کلیۀ علاقمندان دعوت می‌شود روایت‌های خود (عکس، فیلم و دلنوشته) را به شناسه زیر ارسال نمایند.
🔹
شناسه ارسال آثار:
@akharindidar_admin
🔹
هدایا: شرکت در قرعه‌کشی ۲۰۰ جایزه نقدی + بازنشر آثار منتخب در صفحات رسمی پویش.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/447072" target="_blank">📅 14:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447070">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzb_oIHtDKJK0aH4_u4NSQWcea6v2FSxbAkwoOfyWNoWbh1v3RH0CREkGeepdcVnNGpiL8b6OztAtNitU7aQCChTwxJLlR4U3PXbECuRgKd8CW71zR8D2MZMT8znqQCFeodLUyuwno9bwRXZ8zZiZU-XD1pzzHDSEstaskY9n-5-DbfCTjAOhCthcvGdlZJy210BM7IKqXSztbtYxdXyQu8yd6S-NAMrLq504h-qmj97WXRhabniIxD_ncRQl38EOa-SRU_YdK9dzyQKUZx7wRkDWuaENhib2gPzH7WOyri4NUrV8oHxB8KQMhPt3yhJMEIcKLUi5OiR977mNKM47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: ملت شکست‌ناپذیر ایران امروز یکپارچه فریاد یا لَثاراتِ الحسین(ع) سر داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/447070" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447069">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59349603d.mp4?token=L-7frFWr8aC_vD6nwLqJXakRw4tUj60mvCHrfzD5JoHZr7R-ZES1FIeRVu9p9uLRCLkRhTtD5Afh7Ol31loo0xQnmlsDTqDU0z0KHWrkiEbMPBF1ofFGMOVkBRqnj0MKC4xM0_VNvrMO4gqNtumg59UCPKPz-CIqWFD7p6Sv_b-NkWN1QsCHcAYaVJa7vMQn9I74A9uetHW3FWvLLl5hKlkxi-FBq13Z50KYl9twjtn04sUwhunCBrEgx7bqpR1s0_r65CRxvDYxeRFxBjScVAdHqgIljJgw4qsAQjBMNLHI0bTaalP_DC3Aafd8fBkhC_WNPhKeG_83Ru8oZVi8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59349603d.mp4?token=L-7frFWr8aC_vD6nwLqJXakRw4tUj60mvCHrfzD5JoHZr7R-ZES1FIeRVu9p9uLRCLkRhTtD5Afh7Ol31loo0xQnmlsDTqDU0z0KHWrkiEbMPBF1ofFGMOVkBRqnj0MKC4xM0_VNvrMO4gqNtumg59UCPKPz-CIqWFD7p6Sv_b-NkWN1QsCHcAYaVJa7vMQn9I74A9uetHW3FWvLLl5hKlkxi-FBq13Z50KYl9twjtn04sUwhunCBrEgx7bqpR1s0_r65CRxvDYxeRFxBjScVAdHqgIljJgw4qsAQjBMNLHI0bTaalP_DC3Aafd8fBkhC_WNPhKeG_83Ru8oZVi8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی متفاوت از نماز بر پیکر رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/447069" target="_blank">📅 13:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447068">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a53e7bf830.mp4?token=MAiDpzqM-w_82Jb1j4_k4VZ4RI5XqhnpeGeNNWQeRHqkFWGVZtCNZjBLv59hRI8-rMQvt754MNwvHrO_jXInElmt83On17tBAxjjzHP-wjO0b9PeHKFnwQcmvP9p85rvxKbSPHlCPxxrWl3DLxP-U9CjKXutde7J9ZiVSvoyPAdI7XtZ9xT_H6ipeTnPdXa-bFk0tQXgQsWDrSB52djbAIFjfXA92nv3Lhm5qK79CGxCkz7PlYa-tw7p0NdpQo5vNAi5WsQ_pTUZ6PhcvXT-K3pBTpuxafMNZJ9f_f8EsqkqCehPj4N9VdNSBzKtlUKUXZj145bCYTFjofIJ1JdC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a53e7bf830.mp4?token=MAiDpzqM-w_82Jb1j4_k4VZ4RI5XqhnpeGeNNWQeRHqkFWGVZtCNZjBLv59hRI8-rMQvt754MNwvHrO_jXInElmt83On17tBAxjjzHP-wjO0b9PeHKFnwQcmvP9p85rvxKbSPHlCPxxrWl3DLxP-U9CjKXutde7J9ZiVSvoyPAdI7XtZ9xT_H6ipeTnPdXa-bFk0tQXgQsWDrSB52djbAIFjfXA92nv3Lhm5qK79CGxCkz7PlYa-tw7p0NdpQo5vNAi5WsQ_pTUZ6PhcvXT-K3pBTpuxafMNZJ9f_f8EsqkqCehPj4N9VdNSBzKtlUKUXZj145bCYTFjofIJ1JdC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم نماز خواندیم هم گریه را به آغوش گرفتیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/447068" target="_blank">📅 13:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447067">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uncg4hasd6Iv765-yZtvfJ99NNsuMmhD6ItmwgBVg1ZrPYL8DAjGGh8JNF_jhQjB7dJ54Ap6RJRmcJWlYCRw798hsxowrn2rBaVU-QbTYb1FEBi7u1aQNJYbObctAbdn8OBGvsw6h_vfjDgi2RloQbh441T7kbQGcspPj5U30X44K268ncAwml7QlvWyvyPPCFP7MykX8PyJQOmpPPp9KPPkJAZQcSLahsQwDreGjPNvAXpnwS9MZIbZ78uRbilGc3aT3d59b5lKBxIoWjRhBluocQEQI8AiC-_h9pPCIjLj5FyjJrChFdSERydzrkjERMsyW06YHn1e4Pesk4l_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای‌عالی امنیت ملی: مردم در وداع رهبرشان دو شعار را فریاد می‌زنند: مقاومت در برابر دشمنان و انتقام خون رهبر شهید ایران
🔹
این چند روز چشم‌تان را به ایران بدوزید؛ این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447067" target="_blank">📅 13:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447066">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89bddb803f.mp4?token=tcLtiX5M_Fz13AFiXFTgDjXfb5fqV7BJVF6ya8ho4UfA473C2ZkY7fdy0fM5PPwR0soXolULDBFSPo2kHykjTBRNT-52dQ6sv54pcxASKikOsQJLM7U3O5LEVAS1HjpOQB4fy66p_KRP4bwIqbu1XJ1YKU42lupoU-ewX49witi4TF88mS9hcWEqU_rzNxmmkIioEt81HEIpVjSiDvHanD9xzy-rD8h233CZhDd4NoXNX2BJlEBfgVesK5nFF0LrMgvswDT_27uF-rC8K2VK2WY_MZ6pQ9BWGEPhZ6F1Jmy0wd9vhUlfCyS70cOROmVhE95Y-ahYt1N1i7ED6Ae30w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89bddb803f.mp4?token=tcLtiX5M_Fz13AFiXFTgDjXfb5fqV7BJVF6ya8ho4UfA473C2ZkY7fdy0fM5PPwR0soXolULDBFSPo2kHykjTBRNT-52dQ6sv54pcxASKikOsQJLM7U3O5LEVAS1HjpOQB4fy66p_KRP4bwIqbu1XJ1YKU42lupoU-ewX49witi4TF88mS9hcWEqU_rzNxmmkIioEt81HEIpVjSiDvHanD9xzy-rD8h233CZhDd4NoXNX2BJlEBfgVesK5nFF0LrMgvswDT_27uF-rC8K2VK2WY_MZ6pQ9BWGEPhZ6F1Jmy0wd9vhUlfCyS70cOROmVhE95Y-ahYt1N1i7ED6Ae30w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هموطن بختیاری در وداع با رهبر شهید: انتقامت را می‌گیریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/447066" target="_blank">📅 13:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447065">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_4qQFfAFxm-jIqm014jTsY5Hq8XzfItO23Mt00yLInwbN4ib7psGqWVGvMeEtf6hYJjpEmX6rmD_ACmKP3lJwrnZHR20SpZGxXT-9W2hxUm70HXmvif0slsZBo0R0s6vzVXNll04h7ts7SRzSnSuzRZlyakLrsu-Xn5LMdbhPIpK_4nvrPFARktpwEmTrV7dBLZDFh8lCh52E-AcFBP0QUOA_fsbNZKX_TNdvVcSWdN_IzgUbFojKUTeGUZq0Gjt_C_5irRHS9ctYzk4Y1_IYp_75tSkvbWrfGwFD3Mr_mB1lu0UfdybGSuIdq-l5SdNbR-AOKeyimMiqmbNUpI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار اعمال قدرت سپاه در تنگۀ هرمز
🔹
نقشه‌های منتشرشده از تردد شناورها در تنگۀ هرمز هم‌زمان با حضور نیروی دریایی سپاه، نشان می‌دهد ۸ کشتی از ادامۀ مسیر موسوم به «کریدور عمانی» منصرف شده، یا مسیر خود را به سمت آب‌های تحت مدیریت ایران تغییر داده‌ و یا به‌طور…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447065" target="_blank">📅 13:36 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
