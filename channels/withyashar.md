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
<img src="https://cdn4.telesco.pe/file/lr9f_otbrPj4_En1k4O8Nkif7nM2ut8BCm7VFx3V1MTOkuciNRwFOEbdLBf17VFczuC-gMsftoqXLK3FEDxUBsc51OUd8bBp5jnQl63KJ4ZAZplsoePIaPGmyIi5RRO8blX1aGu8esPVQRaNI9XLNtCYROePcDN2GUvjEp5EQ7_-driR6v2jxBE7OlPm_1IaDGyjHjJQZ91jlrSAx4UeVEghaQPh9PpF8z2h2Sz8L_ILfhyLz3HClCoovi3n_vqu6yCOGqMvsYj3ZqQow-DhKygIQwnvd8IBJhHl8QZqmYstWIjGCODRuMuDXhG3lKW7orT6LJxfF5zNBqvFHmiKeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 20:56:09</div>
<hr>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال ۱۳ اسرائیل : فرمانده سنتکام، برد کوپر به مقامات اسرائیلی گفته که در تلاشه تا جنگ علیه ایران رو از سر بگیرن چون معتقد است که این جنگ موضع ایران رو در مذاکرات هم تغییر میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/withyashar/20939" target="_blank">📅 20:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سنتکام قصد دارد یک نیروی جدید پهپادی به نام
«فالکون استرایک»
تشکیل دهد؛ نیرویی چندملیتی که نیروهای آمریکایی و کشورهای منطقه را در یک ساختار مشترک کنار هم قرار می‌دهد. هدف این نیرو استفاده از
پهپادهای تهاجمی یک‌طرفه
(پهپادهایی که پس از حمله به هدف خود نیز از بین می‌روند و شبیه مهمات سرگردان یا «پهپاد انتحاری» هستند) در سه حوزه
هوا، سطح دریا و زیر آب
است. این طرح زیر نظر فرماندهی عملیات ویژه آمریکا شکل می‌گیرد و بر تجربه گروه
«اسکورپیون استرایک»
ساخته می‌شود؛ گروهی که طبق این گزارش، پهپادهای آن پیش‌تر در عملیات علیه ایران استفاده شده‌اند. سنتکام اکنون از کشورهای منطقه دعوت کرده به «فالکون استرایک» بپیوندند تا یک
توان مشترک و یکپارچه پهپادی در سراسر خاورمیانه
برا عملیات ایجاد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/20938" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از تنگه صدای پول های بلوکه شده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/withyashar/20937" target="_blank">📅 20:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش صدای انفجار‌ سیریک ، پرتاب موشک/پهپاد به سمت تنگه هرمز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/withyashar/20936" target="_blank">📅 20:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXqjPTjk22XmfkOfF8ewFi5QXgh9Nj9fgATA5YoqaWl64eFUm88-kZZlcQ6yHkIN2YHHo6cqnFNIdxrxHNnCmQQcRh0R886I7I0nAq4iMH8Tf4n7z-dV5fPYJrfoXmw6xTYbyCrjbo45h3EHTRS_4VGjDWTaDhmtqFaSJMTUUIoUazWgVV_KeL8qRr05HptLj7-iAhwjcwe1UFgIQFEGQIchfmZXl26MjmRnNnq2BPy6RNydUfNQoKwFJh-jGuY-EXGEwleBtgmw2rn8eHJhoHkeVp8U-OpUI_Ztc8_USF-34-Bbua7SXaJOkg6wZkvAKC7004hy7SGI6elH9zwvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هگست وزیر جنگ ، امروز در پاناما و پس از دیدار با خدمه ناوشکن USS Gridley گفت :
محاصره وابسته به حضور یک ناو یا یگان خاص نیست؛ نیروها می‌توانند یکی‌یکی تعویض و جایگزین شوند و بنابراین از نظر نظامی آمریکا می‌تواند آن را برای مدت نامحدود ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/withyashar/20935" target="_blank">📅 20:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرگزاری حوثی‌ها «سبا» به نقل از یک منبع نظامی گزارش داد که حوثی‌ها با استفاده از دو پهپاد به پالایشگاه شرکت آرامکو در منطقه جیزان عربستان سعودی حمله کردند. همچنین اعلام شد: «این حمله در پاسخ به نقض حریم هوایی یمن توسط سعودی در مناطق صعده و حجه انجام شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/withyashar/20934" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانال ۱۴ اسرائیل:  رئیس ستاد کل نیروهای مسلح اسرائیل ، ایال زمیر، به وزرای کابینه اعلام کرد که محاصره دریایی ایران بسیار موثر بوده است. طبق ارزیابی‌های اولیه ایالات متحده، مقامات ارشد اکنون بر این باورند که تداوم این فشار شدید اقتصادی هم‌زمان با وخامت سریع بحران مالی داخلی در تهران ،مؤثرترین راهبرد برای وادار کردن رژیم به تسلیم یا زمینه‌سازی برای فروپاشی آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/20933" target="_blank">📅 19:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">@WarRoom
بالون</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/20932" target="_blank">📅 19:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=nDqgVwJakJGq0_h1SG4_dPGwFx2uRPdj20xU8eJqoB8AY39wkcYAeQRXaROKTpbj06Mwt8aPy83QAljsjkCphul_KAB_1hX1C9hkse1k4ZxjXavv3XkMgZXZK_h4Nzm2rTcPZG-X9--58nan4Xn-lxlNh7jZhJEcBRv3aJy4bUm-4w5FRL9nSvwq-2sKrUsgTuNMbPvjmHhSCJd4uW0ZC2-JziLKkZke3OTHjLbqBIrtlhMt9QhNSfL6n8g2D2u6hH2BUvJ7jO6aURfNsaIApNzPSZ_OxB4ZRUaJzt8cN73YSzHAzSVaCMVxtpJ4fVSNgqRRH-pETY-Px_bX5BahYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=nDqgVwJakJGq0_h1SG4_dPGwFx2uRPdj20xU8eJqoB8AY39wkcYAeQRXaROKTpbj06Mwt8aPy83QAljsjkCphul_KAB_1hX1C9hkse1k4ZxjXavv3XkMgZXZK_h4Nzm2rTcPZG-X9--58nan4Xn-lxlNh7jZhJEcBRv3aJy4bUm-4w5FRL9nSvwq-2sKrUsgTuNMbPvjmHhSCJd4uW0ZC2-JziLKkZke3OTHjLbqBIrtlhMt9QhNSfL6n8g2D2u6hH2BUvJ7jO6aURfNsaIApNzPSZ_OxB4ZRUaJzt8cN73YSzHAzSVaCMVxtpJ4fVSNgqRRH-pETY-Px_bX5BahYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/20931" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩ https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/20929" target="_blank">📅 19:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وال استریت ژورنال : ایالات متحده در بحبوحه تنش‌های جنگ با ایران، ناو هواپیمابر جورج واشنگتون را به خاورمیانه می‌فرستد
@WarRoom
یاشار : خیلی عقبید
😁</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/20928" target="_blank">📅 19:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a73c9be9f.mp4?token=Kylxd7HBamU5Mp2RkLhtv1Cwea-MgUyWe_VL2K3gCztVST8fBG3SwpQ7D-JTR7DE3JKNw5iDtvSPnRxudlCwYumaziQYgxCzAvq_BGzQCIBK1db1qnVdgx60xiZe8IwQiHEyvhbzuGy0iTRT7JRt_n4WcvJOUSkwu9ksKsoSmwAofeRf5dnJJHjrlNuA6-zBCDdQeguBqxFKzBXPJBCUhNtuXRgUlsIDviIWPwz_y3Sm8GTbuCpF__JycMYmzoSlYxVOvCZi-dbaTVLs8bYCQZT0ZmS0NaHUb2e7ozJt4YfYMinXfK47j0FZhpr_OG6ZORMmPJESwxzRD2qII33RvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a73c9be9f.mp4?token=Kylxd7HBamU5Mp2RkLhtv1Cwea-MgUyWe_VL2K3gCztVST8fBG3SwpQ7D-JTR7DE3JKNw5iDtvSPnRxudlCwYumaziQYgxCzAvq_BGzQCIBK1db1qnVdgx60xiZe8IwQiHEyvhbzuGy0iTRT7JRt_n4WcvJOUSkwu9ksKsoSmwAofeRf5dnJJHjrlNuA6-zBCDdQeguBqxFKzBXPJBCUhNtuXRgUlsIDviIWPwz_y3Sm8GTbuCpF__JycMYmzoSlYxVOvCZi-dbaTVLs8bYCQZT0ZmS0NaHUb2e7ozJt4YfYMinXfK47j0FZhpr_OG6ZORMmPJESwxzRD2qII33RvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رابرت اف کندی جونیور:
دانا وایت گفته که او هیچ‌وقت ندیده ترامپ آب بنوشد. او فقط نوشابه رژیمی دایت‌کُک می‌نوشد.
او از هر آدم دیگری که تا حالا دیده‌ام، انرژی بیشتری دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/20927" target="_blank">📅 18:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جمهوری اسلامی از طریق ترکیه به سوریه اطلاع داد که در صورت دخالت ارتش سوریه در لبنان علیه حزب‌الله، صدها نقطه در سراسر سوریه، از جمله کاخ ریاست‌جمهوری، با پهپادها و موشک‌ها مورد هدف قرار خواهند گرفت.
یک تحلیل اخیر هم صراحتاً می‌گوید ترکیه واشنگتن را متقاعد کرده که از دولت احمد الشرع(پیش‌تر با نام ابومحمد الجولانی)در رویارویی با حزب‌الله در لبنان استفاده نکند.
@WarRoom</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/20926" target="_blank">📅 18:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏اوپک: افزایش تولید نفت کشورهای منطقه در حالی که ایران درجا می‌زند
‏گزارش جدید اوپک نشان می‌دهد تولید روزانه نفت عربستان سعودی، کویت و عراق در مجموع طی ماه گذشته نسبت به ژوئن حدود ۱ میلیون و ۶۴۰ هزار بشکه افزایش یافته، در حالی که افزایش تولید نفت ایران تنها ۲۶ هزار بشکه بوده است. پیش از انسداد تنگه هرمز حدود یک پنجم نفت مصرفی جهان از این آبراه عبور می‌کرد، اما کشورهای عربی حوزه خلیج فارس اکنون با استفاده از مسیرهای جایگزین در دریای عمان و دریای سرخ و روش‌های دیگر، صادرات نفت خود را ادامه می‌دهند. در حالی که همسایگان ایران ظرفیت تولید و مسیرهای صادراتی خود را گسترش می‌دهند، صنعت نفت ایران زیر حاکمیت رژیم جمهوری اسلامی عملاً از این رقابت منطقه‌ای عقب مانده است.
@WarRoom</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/20925" target="_blank">📅 18:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOnir-aNQ8T0X_Qsx_Raiurato1Q3WUtFV1JyZoqjUNAhUYRLXdzHhYLM2xhyreM98cgi2DUb2xZ01v5jxaCKdzdGhHDkYUkIlUCh0Rrb45cdoBiNCQTYJ-ForHdRzW_CJyLykqrTipWwasyhe0voWc1TLUUk7OtboLYYQkXURqd0ijDezgz9F_MgQaHBbPoW0E-6Ndju8FuqwH3kYCRaKHNDP4BzvQtTP9EEOsOe9U-p4FRH4rhkFwg6TS7-jOm62tcB_3IMOL7on5K1g7PnVLcwUZPsQ2M4XEsrK9MlId_8rboLE6hbFsCNsVfkAOAmowDCDCXwvTot4O-gJOqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩ https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/20924" target="_blank">📅 18:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-YJSk9BImT_uMsgGSu5FYJqQn-Nq06UuJjN_WF0B1Bdf-5B6hyLnz6GHj0AEj6Nb6kHUw50LkmcES_mv2fxJCS6xZt2x8XK9CMxN5gz-MiQF2JUZueNdn0J3-kdOXreRZLsQhyuOYhRentEe5AVm-sRWec-WvcYPgVURcrWPWg6gEPaFJE9VLoWFfRe-S3ukpEL50hHU7Wjn9vLtG_Ja-2BgJgSttguX9-iCscGYasbBXO87PbbW7ZhZ2nIFjOAEYV_j-b82bSIpY7L6p-WGEy6fvzr3FdFxMcgHYtz9znrKf0NcD45jNeiToTsRkdgyLWC11OfWoT-ly26GogySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عروس معصومه ابتکار(شامپانزه دیوار سفارت) که اقامت دائمش در آمریکا لغو شده، وکیلی حرفه‌ای گرفته و از دولت آمریکا شکایت کرده، به این امید که اقامتش برگردد و غرامتش را از اموال بلوکه‌شده بگیرد. او نامه‌ای خطاب به مردم آمریکا نوشته: «من عاشق آمریکا هستم، فرزندم فارسی بلد نیست و مادربزرگم در اشغال سفارت آمریکا فقط مترجم بود.» استدلال نامه و وکیل ایشان این است که فرزندان نباید به‌جای والدین مجازات شوند
@WarRoom</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/20923" target="_blank">📅 17:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGFzm7RzALSXcHPcXzmvH-9hF_Haemoxog_UcNRXCaNAvdkil5m81_29wl1HpoqYzCaeym45bP4slfeVdjChS8kSdr-qQNioWCjjRxzHjo3gPGAkZCej1Cwvr1MLIFc8v8xnOWSgt7tOyGoQy6ji6WrwGmyk601lFZTUxEHIOnDtrt6ztfGDL9ap1L1kS1RxMoj0C-ut4Uk4M0eIlFmVjuU7ZrmWURMBlo5fS7t3yOk3y58ihIRfBUeqk1EgKjZ4Dz96ry_jhAlBv8v4seaENkHGijai1__j5_PbXH8KaX6l4wJsbzpgtX907hddXdPa0PfWfQoantgRic0hFEdUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواب بودم ، پیج روزدن
دیر برگردوندم
🙌🏾
😂
instagram.com/yashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/20922" target="_blank">📅 17:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76aaa280.mp4?token=MYmDDcuJZnHBI0i6fnK1XA2p8Ly4vu2qxnd40hLo4KbGH9xjjuJye7Mc3aKhLKR3Nx1kEYE1cu4ybMujm_rW8VfRMcgj-9QGFjfqXlsFBqwcBqomYcDgr6CyEP_JPs0L0OvPkKY88d9v5a1rmVwUigb5a6ifyrNBYN6drvYgX_TYjgrfRrM48JloOMLiMw3hrZA2gNVOAHevcqtcES1ssbwg8y1JbfIPrCj7ojOXxR4d5YKZV4pqFzGTpBRqtTRdUHoAMYHR7vKGGLq06cmx6pOXIUdRzT_FIiBeuOBNYlLsaIg0nZfUQICCNEpmVvDIUXFynBa1BaVSz-u9DtgqBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76aaa280.mp4?token=MYmDDcuJZnHBI0i6fnK1XA2p8Ly4vu2qxnd40hLo4KbGH9xjjuJye7Mc3aKhLKR3Nx1kEYE1cu4ybMujm_rW8VfRMcgj-9QGFjfqXlsFBqwcBqomYcDgr6CyEP_JPs0L0OvPkKY88d9v5a1rmVwUigb5a6ifyrNBYN6drvYgX_TYjgrfRrM48JloOMLiMw3hrZA2gNVOAHevcqtcES1ssbwg8y1JbfIPrCj7ojOXxR4d5YKZV4pqFzGTpBRqtTRdUHoAMYHR7vKGGLq06cmx6pOXIUdRzT_FIiBeuOBNYlLsaIg0nZfUQICCNEpmVvDIUXFynBa1BaVSz-u9DtgqBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
ما داریم مطمئن می‌شیم که یه مورد دیگه مثل این، یعنی ایران، نداشته باشیم
@WarRoom</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/20921" target="_blank">📅 17:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR3vQoymHg8lrGjZHSZbEgsyNxXgloAdQnPntstxUn2xugeaitzo90yzpeuF_Von0hmbkmRhrALDMv5B98vfgWL58Gm8ACNJB1if0WrZjugJOEzEeetDaQJ0SnA4l83YR_QL35YP3QwTvt2OXtV6O2sScwvmP7sizTQUioyTwN75N2HBLsHGEP3C4DGnWxO7YeDq4keRdh4kub8hkyX3t8lY3OF-Z8zeVHNaO1rkwEvUAN_Do4rzmA4FZ2C6YKd3DGCsqoWSahGDosvm_n9-g4VrXwnlIUewvzEC5yBIuPAbplFsYPhJGlBax4aL-WbGKIBY9JmUyorXcWE3GmSTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته کنعانی، مدیرکل حفاظت محیط زیست ایران، سطح آب دریای کاسپین به پایین‌ترین حد خود در نزدیک به ۲۰۰ سال گذشته رسیده است.
کارشناسان می‌گویند یکی از عوامل اصلی، روسیه است که با ساخت بیش از ۴۰ سد عظیم، رودخانه ولگا - شریان حیاتی اصلی دریا - را مسدود می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20920" target="_blank">📅 14:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgKW6a3-WJ0v6o3oYOz--6an1SioyoOy8MvdkNzsLLiLGbzQ_WkFa3JR8eMrlZ8TkHgBAxUF09zGr5ffzBPJQHTRlKgcFweKObW63hQfOY26EhKQraJ5fHqeZtVQ9TWj8vYvWPf4bM_YWm2VHwiTMoHl23PVu7rYSeoLcjqWQ4Jldcp3MRH2JI-b5HXbLnAtZt7PFhzgpWHOu64usAy1GEbynj4t_xoVTs483a3n5fZ4YiE6jN0VpQyUbmFegpbDtdO11JA8Oxt38lKvfWqGcixKUIj2lDjy2O3m2b8yHyNb0J4ZP0BDCcgfRI2PYgR-bfzZXnld1xxsgOvnqpW9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرگرد ابوالفضل حیدری، نیروی هوافضای سپاه ، امروز در یک سوء قصد با موتورسیکلت در زابل، استان سیستان و بلوچستان، به شدت زخمی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20919" target="_blank">📅 14:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96bba2676.mp4?token=JRWWltp14gjeajGApxnxxkKNO_EmLOQNPmwm3KrAAcKc2hYAbmU_7vUC-Vv_C74ea24fve8bAtwPmSyOGqydAsqyh9sCg1gMLiIIo88MgpSr7AesVkzM2uM7sFc0NZ6spH4g3x-pjQIylnPC7YBBWHTCbC64embHq8hzyLJJyl5KXjd6SpCXxvzC30cLr50n2x5rTGacwtipLQXgRX2zMUWL-IJQ_ai2EcMEV2hDR5d6CIBytFkS2DhTrAt_sY5S41F55Ot37VCs2Q56a8EIJYazXTWrufk5rnPJvteQNWcfFvy7VxclI42lG4uEdbvv8GAjseK2cwEM_8MB1roWCCkG5NsWunIRcFTx8LStwYInAGmu6k4cUo6sv0_ym5Hi9jJ7auVhekkBLBOFCSaQi_7GL9Px1hzee9kkvbG4H-HBQnNqiijgTqqU8nAWzXdzZ_FMRMDF6BCVgjh6AZr2g_OO4fsN_3wCmMPkIVnxuvlHbRgiT64tfhHpUgwprCB3QdCN0eht0v5G9TEfFdRDLyT3YMuJgNmCPHh_M_tl0WMpuW8cBusQ8pbY2HCj_dcWXD91LgDQydYMzueYNKn4HGrJjDe0pb7qHHMEJ0aF3d3aWJGEDd_uZYrc7fiAjl_n1Y4RsF9YCzsomQtLOD8kpofvyYzC4MW4AM9bwjM-rf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96bba2676.mp4?token=JRWWltp14gjeajGApxnxxkKNO_EmLOQNPmwm3KrAAcKc2hYAbmU_7vUC-Vv_C74ea24fve8bAtwPmSyOGqydAsqyh9sCg1gMLiIIo88MgpSr7AesVkzM2uM7sFc0NZ6spH4g3x-pjQIylnPC7YBBWHTCbC64embHq8hzyLJJyl5KXjd6SpCXxvzC30cLr50n2x5rTGacwtipLQXgRX2zMUWL-IJQ_ai2EcMEV2hDR5d6CIBytFkS2DhTrAt_sY5S41F55Ot37VCs2Q56a8EIJYazXTWrufk5rnPJvteQNWcfFvy7VxclI42lG4uEdbvv8GAjseK2cwEM_8MB1roWCCkG5NsWunIRcFTx8LStwYInAGmu6k4cUo6sv0_ym5Hi9jJ7auVhekkBLBOFCSaQi_7GL9Px1hzee9kkvbG4H-HBQnNqiijgTqqU8nAWzXdzZ_FMRMDF6BCVgjh6AZr2g_OO4fsN_3wCmMPkIVnxuvlHbRgiT64tfhHpUgwprCB3QdCN0eht0v5G9TEfFdRDLyT3YMuJgNmCPHh_M_tl0WMpuW8cBusQ8pbY2HCj_dcWXD91LgDQydYMzueYNKn4HGrJjDe0pb7qHHMEJ0aF3d3aWJGEDd_uZYrc7fiAjl_n1Y4RsF9YCzsomQtLOD8kpofvyYzC4MW4AM9bwjM-rf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏اظهارات کم‌سابقه سناتور تام کاتن درباره راز وقایع مرداد ۱۳۳۲ در برنامه هفتگی پربیننده مارک لوین در شبکه فاکس‌نیوز
‏«اوباما ادعا کرد که ما نخست‌وزیر منتخب دموکراتیک ایران را در ۱۳۳۲ سرنگون کردیم. این یک افسانه کامل است. او (مصدق) نخست‌وزیر دموکراتیک نبود. او اساسا سرنگون نشد...
..(برعکس)، مصدق کسی بود که سعی کرد قدرت را تصاحب و به طور غیرقانونی حفظ کند. ولی باراک اوباما با مغز استخوانش باور داشت و بارها درباره آن نوشت و سخنرانی کرد که آمریکا برای دهه‌ها تنش با ایران سزاوار سرزنش است و برای همین هم به دنبال توافق بهتری نبود.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20918" target="_blank">📅 12:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل، ایل زمیر، به وزرای کابینه در مورد وضعیت اقتصادی ایران گفت: تحریم‌ها علیه ایران بسیار موثر بوده است. بحران اقتصادی در آنجا رو به وخامت است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20917" target="_blank">📅 12:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سناتورهای دموکرات کنگره آمریکا خواستار بررسی شرایط ناو یواس‌اس آبراهام لینکلن شدند؛ این درخواست پس از گزارش‌هایی درباره کمبود غذا، خرابی لوله‌کشی و بحران‌های سلامت روان در طولانی‌ترین مأموریت تاریخ ناو مطرح شد.
سناتور روبن گایگو نیز خواستار بازدید رسمی و نظارتی یک هیئت دوحزبی سنا از ناو برای بررسی شرایط گزارش‌شده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20916" target="_blank">📅 11:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20915" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvZZCWQgkqaVytujAk2BxfHjVeUTQnaXK1F1lFKULCaMBnT02A9-V4fnponE4XubItGxAEI-cnw-Lf6i3UXb2WEycLE9U6qnfchLHQtD7T-s-0WeIc8JW2880_NTScOXEFpmlogu5d6gVJ_c27DckNQsgRS7fnI1nYRbwPOPgQ33Mw4ZqrO2xf_4RuMHlA4LBQo21bomHXrQkOoSNzX8PD6NwziyfLUkT_9B8AYH1eNu3WzyDIDA2HR7Sng4o1bHN41kAgHSCuryt96rsHFOO2Bev7PPZvVq-_cVyvaiqIzW6xyoHMQN20MQL5jqkNENWk87hx-0rc-k1ESUo0heIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩
https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20914" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20913" target="_blank">📅 09:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20912" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شب گذشته از ترس شروع اعتراضات و انفجار جامعه افزایش قیمت بنزین هشتاد و هفت هزار تومانی در کرمان، کمتر از یک ساعت پس از آغاز اجرا متوقف شد و قیمت بنزین به نرخ قبلی برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20911" target="_blank">📅 08:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال‌های عبری : خبر گران شدن بنزین در ایران باعث شد خبر انتقال پنهانی طلا و دلار به ایران، در حاشیه قرار بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20909" target="_blank">📅 04:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیت هگست، وزیر جنگ : رئیس جمهور ترامپ، سوءاستفاده را برنمی‌تابد. ما اینجا برای بازی کردن نیامده‌ایم.
شهروندان و ملت‌های ما شایسته و منتظر اقدامات واقعی و ملموس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20908" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی امروز کشتی باری «ولا نوا» با پرچم پاناما را هنگام حرکت به سمت یکی از بنادر ایران در خلیج عمان متوقف کردند. پس از بی‌توجهی خدمه به هشدارهای آمریکا، یک بالگرد MH-60 دو موشک هل فایر به اتاق موتور کشتی شلیک کرد و سامانه هدایت…</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20907" target="_blank">📅 23:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ در تروث : کارولین لیویت، سخنگوی فوق‌العاده کاخ سفید و یکی از مورداعتمادترین دستیاران من، در پایان این ماه از سمت خود کناره‌گیری خواهد کرد تا بتواند زمان بیشتری را با فرزندان خردسال دوست‌داشتنی و خانواده‌اش بگذراند
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20906" target="_blank">📅 23:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">@WarRoom
ترامپ پوکر باز</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20905" target="_blank">📅 22:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20904" target="_blank">📅 22:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=PIB1B-lxF11sjV3qDIExv4XToXE48yHaUBqbVjGHZvAHmv63cjdzEGDwUn-7RMQ1vn8Gg8faaVAE96nUXgpErGDLdHM0MrfzvX7veoWNYM5WFxpkFfTKOp3PLY0awdXg4x-67nFUJxMW5NnE3RhDFvqmkjGVZX6_yDjzedMPuyXYfEvSS9Hb29Z8jWiceiz8jz4HLUfyo5FkyfhXkGj57pEi2ELXfFaT72kXM4dbARjInJIqye2gAfwhs_kaOoAoYlw6thaLTKW9M_ijCcF_9nkg2m3hK0XnOilwolq_FSEGRnLpXtonOVbwkR5wQDkChW9qfy-5iJmiGq5jKBdhtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=PIB1B-lxF11sjV3qDIExv4XToXE48yHaUBqbVjGHZvAHmv63cjdzEGDwUn-7RMQ1vn8Gg8faaVAE96nUXgpErGDLdHM0MrfzvX7veoWNYM5WFxpkFfTKOp3PLY0awdXg4x-67nFUJxMW5NnE3RhDFvqmkjGVZX6_yDjzedMPuyXYfEvSS9Hb29Z8jWiceiz8jz4HLUfyo5FkyfhXkGj57pEi2ELXfFaT72kXM4dbARjInJIqye2gAfwhs_kaOoAoYlw6thaLTKW9M_ijCcF_9nkg2m3hK0XnOilwolq_FSEGRnLpXtonOVbwkR5wQDkChW9qfy-5iJmiGq5jKBdhtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20903" target="_blank">📅 22:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدای موشک اقتصادی
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20902" target="_blank">📅 21:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">طرح امتحانی بنزین ۴ نرخی آغاز شد!
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
نرخ سوم: ۴۰ لیتر با نرخ ۵۰۰۰ تومان
نرخ چهارم: ۸۷,۲۰۰ تومان
این طرح هنوز به طور رسمی کامل اجرا نشده و اکنون محدود به ۲۰۴ جایگاه سوخت در استان کرمان میباشد.
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20901" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۱ اسرائیل : با کمک ماهواره‌های روسی ، حملات حوثی‌ها به عربستان سعودی و نیروهای آن در یمن هم افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20900" target="_blank">📅 21:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گاردین به نقل از چند منبع : ناو هواپیمابر «آبراهام لینکلن» پس از حدود ۹ ماه مأموریت مداوم و ۲۵۰ روز حضور پیوسته در دریا، با افت شدید روحیه و فشار روانی خدمه مواجه شده است. خانواده‌ها و برخی ملوانان از مشکلاتی مانند محدودیت غذا و آب، اختلال طولانی در شست‌وشوی لباس‌ها و دست‌کم یک مورد تلاش برای پریدن از کشتی که مهار شده، خبر داده‌اند. نیروی دریایی آمریکا نیز در حال آماده‌سازی ناو «تئودور روزولت» برای جایگزینی لینکلن است، هرچند زمان دقیق این جابه‌جایی به دلایل عملیاتی اعلام نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20899" target="_blank">📅 21:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏وزیر دفاع اسرائیل: من به ارتش اسرائیل دستور داده‌ام که تمام اقدامات لازم را برای حضور طولانی مدت در منطقه امنیتی لبنان، سوریه و غزه انجام دهد. ‏ارتش در منطقه امنیتی لبنان، سوریه و غزه برای دفاع از تمام اسرائیل باقی خواهد ماند. @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20898" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مشاور ارشد قالیباف :آ مریکا و اسرائیل برای یک حمله نظامی پیش از انتخابات سراسری در اسرائیل و انتخابات کنگره آمریکا در آبان ماه،آماده می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20897" target="_blank">📅 19:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر کشور پاکستان در ایران به عراقچی، وزیر امور خارجه، اطمینان داد که "توافق دفاعی مکه" به عنوان یک ائتلاف علیه رژیم ایران طراحی نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20896" target="_blank">📅 19:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42557aaa83.mp4?token=YgMOmdXaMHhF0oxIgr9NUXyB_zDIMT4ltloPWlG2Ab718AXoNsTyNkBYFyLYnhy9xZB4OxTVn_l0p-ynbvTR0T_lahI7RnPG_Nrosjn-ciEoE3_J3RMwOeIH0gKW87TpOMegZ7qltYXxpRtcwcUN6mP_FbSXe5Z1nVOFnUoJ4ZJja1_VzMTc1IBXg-aN-QFwvUckc51uH0gwuVi5ykHlWDY1gL-Cb67PcAS9Cs0Y180KWKWfkUA1Knqz54nJt67-KXozqkmUiv9qsEQ7IJR8TAdXspQ__azYj9Hsr4QzUNIBsH54hS-Cq_wbZtblfzrj7KNg1or2ayoOMWbzVvFzYxhqO_8Q__Pf_SWt5QWeit54cQ-WjI3JW13FsagNBO_C8iIgtO0_NMm1A5bC99p6VSa-ToDpCZTYeclVZtxhnsu-bFZcRuWDq_bc-ghtuxNOeVdotwxpEb4mECsYLPyTOQVxlNiSb0ocYKM5S8wbqEuReAAiV8VrgzDqd_hWEFGZDBMT5DZoOuiDiVVbwnimEhhEgq3109C05rLsGrc8ubm8_JHI6QB0fEGHgUQIRluBFTa1rHSfWESHvLtGOQIih4WwJrMo7DVooc0fmk2hlXPY4Mm2s7NCMeNt3WpmnFIhzq3rs2SB7CX3qgl5r_kHB61gH6IB3eIC6iGrBZtKwSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42557aaa83.mp4?token=YgMOmdXaMHhF0oxIgr9NUXyB_zDIMT4ltloPWlG2Ab718AXoNsTyNkBYFyLYnhy9xZB4OxTVn_l0p-ynbvTR0T_lahI7RnPG_Nrosjn-ciEoE3_J3RMwOeIH0gKW87TpOMegZ7qltYXxpRtcwcUN6mP_FbSXe5Z1nVOFnUoJ4ZJja1_VzMTc1IBXg-aN-QFwvUckc51uH0gwuVi5ykHlWDY1gL-Cb67PcAS9Cs0Y180KWKWfkUA1Knqz54nJt67-KXozqkmUiv9qsEQ7IJR8TAdXspQ__azYj9Hsr4QzUNIBsH54hS-Cq_wbZtblfzrj7KNg1or2ayoOMWbzVvFzYxhqO_8Q__Pf_SWt5QWeit54cQ-WjI3JW13FsagNBO_C8iIgtO0_NMm1A5bC99p6VSa-ToDpCZTYeclVZtxhnsu-bFZcRuWDq_bc-ghtuxNOeVdotwxpEb4mECsYLPyTOQVxlNiSb0ocYKM5S8wbqEuReAAiV8VrgzDqd_hWEFGZDBMT5DZoOuiDiVVbwnimEhhEgq3109C05rLsGrc8ubm8_JHI6QB0fEGHgUQIRluBFTa1rHSfWESHvLtGOQIih4WwJrMo7DVooc0fmk2hlXPY4Mm2s7NCMeNt3WpmnFIhzq3rs2SB7CX3qgl5r_kHB61gH6IB3eIC6iGrBZtKwSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏وزیر دفاع اسرائیل: من به ارتش اسرائیل دستور داده‌ام که تمام اقدامات لازم را برای حضور طولانی مدت در منطقه امنیتی لبنان، سوریه و غزه انجام دهد.
‏ارتش در منطقه امنیتی لبنان، سوریه و غزه برای دفاع از تمام اسرائیل باقی خواهد ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20895" target="_blank">📅 18:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امروز،
۱۲ اوت ۲۰۲۶
، آسمان شاهد هم‌زمانی
چهار پدیده نجومی
است:
صف‌آرایی شش سیاره
شامل مشتری، عطارد، مریخ، زحل، اورانوس و نپتون که پیش از طلوع خورشید در امتداد بخشی از آسمان دیده می‌شوند؛
خورشیدگرفتگی کامل
که اوج آن حدود
۲۱:۱۷ به وقت تهران
خواهد بود و در ایران دیده نمی‌شود؛
اوج بارش شهابی برساوشی
که از امشب تا بامداد ۱۳ اوت ادامه دارد و در شرایط مناسب می‌تواند ده‌ها شهاب در ساعت ایجاد کند؛ و در نهایت
ماه نو
که یعنی ماه تقریباً بین زمین و خورشید قرار می‌گیرد و از زمین دیده نمی‌شود. نبود نور ماه باعث می‌شود آسمان تاریک‌تر شده و شرایط برای تماشای برساوشی‌ها بسیار مناسب باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20894" target="_blank">📅 18:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbtQg9MLl9RTM23nofmW8ryiYKg_V6ZT2Rd5ffPGwJurPJKG5hoYe347w1V3rhF_6PzON3VBBmyJiViOg50ulp4QrcA7okTa53EOeqSMICWplAreshNRVmeYzABypqH_NA-mhkAFQ9MxNC1YD0QgPrBeI7q41AJRhc7731VxxsYEZBKsOQFa5y7Q92yfOD2O-mIAtp-HNmPGrG4fNUtapAcTIhVbH9EpJx4qDlBKgY2BD8zXIWxycHD7FWHDwFi5HN4BLf5l8F8syko-Qg4n5q9ixItdTpNo6S5Axhc3G3fcpnDoV0sN9_gO77qHPT4J4aXzDL6EULc0tM2_sgMQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد! محاصره دریایی ما از سوی همه «دیوار فولادی» نامیده می‌شود و ایران هیچ کاری از دستش برای مقابله با آن برنمی‌آید. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق دریافت نمی‌کنند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است و «رهبری» آنها، در بهترین حالت، نامطمئن است! آنها پولی ندارند؛ کشورشان «ویران» شده است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر می‌شود! ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. ستایش از آنِ الله باد!
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20891" target="_blank">📅 18:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7908fd3c.mp4?token=YHs4kgs2rSwOy5lGMdDS5_18QKMKfaK1htCmAyxsorVZ8geAjNrXG98_4wmmAz80-_dqVakm5P670rsT-CAHBbpryiwwkMd1n4x32nsESGwGzTDxdkIR3v5YI2kKV6c94tlYH-ArGbnL7M2xPkGpIVNmHR34lMpJOgPAS4w0liI2RMrLbFJ-01RoctUSDJw7sGyARy-8S-HD3Oy_NBcRTe_jxSej0UjJDlL3qYm7eu24pr2gOa1K1jxLXOvpWg7eewVNfrSe3tHk44PFk0fK8Ux1TJ3X3Y-WqA7-SmxzrmEwcrRjRGVveVfXSXY37o7EUDc2ZHqb1tktKhq3Pg4o5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7908fd3c.mp4?token=YHs4kgs2rSwOy5lGMdDS5_18QKMKfaK1htCmAyxsorVZ8geAjNrXG98_4wmmAz80-_dqVakm5P670rsT-CAHBbpryiwwkMd1n4x32nsESGwGzTDxdkIR3v5YI2kKV6c94tlYH-ArGbnL7M2xPkGpIVNmHR34lMpJOgPAS4w0liI2RMrLbFJ-01RoctUSDJw7sGyARy-8S-HD3Oy_NBcRTe_jxSej0UjJDlL3qYm7eu24pr2gOa1K1jxLXOvpWg7eewVNfrSe3tHk44PFk0fK8Ux1TJ3X3Y-WqA7-SmxzrmEwcrRjRGVveVfXSXY37o7EUDc2ZHqb1tktKhq3Pg4o5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منم مشکلات زیادی دارم ولی برای شما شاد هستم
😍
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20890" target="_blank">📅 18:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20889" target="_blank">📅 18:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش CNN: وزارت امور خارجه آمریکا به دلیل تنش های احتمالی به سفارت‌های این کشور در خاورمیانه دستور داده است تا برنامه‌هایی را آماده کنند که به آن‌ها اجازه دهد با تعداد محدودی از کارکنان به فعالیت خود ادامه دهند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20888" target="_blank">📅 17:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6ab93f52.mp4?token=GSl6re5HWK-hhFG7yfpnweiT1GNNaF9lx2Unea9uDE70Tp6mJvkJ0Vw97mM2G-tD_uV1yadKgJFjcTu6miiPHLIuxgsKxUsSsUduZfCsJqb8eCFu61Je0iNMb_PMLpVq0FdCy61jZTqquUAOg2q4EtjZdmnXop7WQ1cn-eoN6GOUqTEzKswwe99COJvscW_-HACfvUMpxkzi6Zg9s5-bWK85R7-hYSGKegdgzrC9QP_c5giJonqN-c52ucQO2sevFvucok9uesbzSVJXpxeRAI3-04xauQvdKVH09As9eJ7JEFYjCVeYq9BK6IYQsvXqLmkt1aBO8YCgq8IWTiQg5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6ab93f52.mp4?token=GSl6re5HWK-hhFG7yfpnweiT1GNNaF9lx2Unea9uDE70Tp6mJvkJ0Vw97mM2G-tD_uV1yadKgJFjcTu6miiPHLIuxgsKxUsSsUduZfCsJqb8eCFu61Je0iNMb_PMLpVq0FdCy61jZTqquUAOg2q4EtjZdmnXop7WQ1cn-eoN6GOUqTEzKswwe99COJvscW_-HACfvUMpxkzi6Zg9s5-bWK85R7-hYSGKegdgzrC9QP_c5giJonqN-c52ucQO2sevFvucok9uesbzSVJXpxeRAI3-04xauQvdKVH09As9eJ7JEFYjCVeYq9BK6IYQsvXqLmkt1aBO8YCgq8IWTiQg5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری پی بی اس: چرا مجتبی خامنه‌ای در طول این جنگ هرگز در ملاء عام دیده نشده است؟
محمدرضا نقدی: استراتژی متعل به اوست. دشمن ما جنایتکار است و به هیچ قانونی پایبند نیست.
مجری: آیا این به دلایل امنیتی است؟
نقدی: طبیعتاً به دلیل امنیت است. مطمئناً دلیل دیگری وجود ندارد.
مجری: آیا او را دیده‌اید؟
مجری: بیایید این موضوع را کنار بگذاریم.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20887" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7137b6f963.mp4?token=SX6hsH2_PicrAVSnpNRxowTE8k7jAQakSWx471M9oNJTUxcr07UzcVDl4tweDwFUpESn1E3MVqIb5vlyUjQSDTBPDfYVPRmaPSk9zN4R8pjXMWh8mwzF6zzf-8QyI4W3VSYZwt-ZcA3x-8lA2YXir3REJyQIg7O_g9bJX2ERZffjiMhKM8nCrtNmkHSyLYyCP1MWVLNQayL-dV7vC_qjB4iGWetSi8WVDPhLf0zoOvWVa-GStx_TaodZneSDzqunXKlf4HHD6b078JU6f58fpS6zDrchVk5Fm3oaM5yHpjC-G3nauOrU2V7kAHV5JLTDd20w6o_VKLp9EuuOgxrZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7137b6f963.mp4?token=SX6hsH2_PicrAVSnpNRxowTE8k7jAQakSWx471M9oNJTUxcr07UzcVDl4tweDwFUpESn1E3MVqIb5vlyUjQSDTBPDfYVPRmaPSk9zN4R8pjXMWh8mwzF6zzf-8QyI4W3VSYZwt-ZcA3x-8lA2YXir3REJyQIg7O_g9bJX2ERZffjiMhKM8nCrtNmkHSyLYyCP1MWVLNQayL-dV7vC_qjB4iGWetSi8WVDPhLf0zoOvWVa-GStx_TaodZneSDzqunXKlf4HHD6b078JU6f58fpS6zDrchVk5Fm3oaM5yHpjC-G3nauOrU2V7kAHV5JLTDd20w6o_VKLp9EuuOgxrZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری آمریکایی پی‌بی‌اس : آیا هدف ایران این است که این جنگ را طولانی‌تر کند، شاید تا زمانی که آقای ترامپ از قدرت کنار برود؟
نقدی، فرمانده سپاه: ببینید، ما باید به بازدارندگی برسیم تا دشمن هرگز جرات حمله به ما را نداشته باشد تا بتوانیم با امنیت زندگی کنیم.
یک راه این است که این جنگ را تا رسیدن به دوره بعدی ریاست جمهوری ادامه دهیم و فرسایش ایجاد کنیم تا اگر کسی بخواهد به ایران حمله کند، بداند که هزینه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20886" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYbPQLEGlLikQLVpdOArMjszrOLByHUvMfNZ_EohZ1COULaxmRfSalsr2RhsSDGi1czlcLn4WyNuCQj86hbbIneenSwkuIAVe74Vr8LuIUw6JKqiDtQMp4h4EVIIf1MNK1DdIMIh9i_-dRMy0o8UqZkrStz3A39t0IZMIAbTHl5bcvmi9zN5GrC6fzsPvBYrruKq0-dYiqco-TvCy8KDtLlDqGmOLLBJ8dLCL_LFzqN_1JrK8tz8YhzETDFpBCvuBFvgenNWwo-T66s1-P4X2XoYAj5b878RU5HgYrguTQeMdxSb44ghXkjScuQv5Yyo2oMoTpRA_Qn33mZjIVcR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهلوان آواز ، «ایرج» خواجه امیری،  خواننده قدیمی در ۹۴سالگی درگذشت
بخش بزرگی از ماندگاری صدای ایرج در سینمای پیش از انقلاب، به ترانه‌هایی برمی‌گردد که صدای او روی تصویر
محمدعلی فردین
است. ایرج خودش گفته بود در
۲۶ فیلم
به جای فردین آواز خوانده است. در مجموع هم گفته بود برای
۱۳۵ فیلم
خوانندگی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20885" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجار های جاسک رو اعلام کردن کنترل شدست ، هم اکنون باز‌ داره گزارش‌ میشه
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20884" target="_blank">📅 16:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">«الحدث» به نقل از منابع آگاه گزارش داد که اسماعیل قاآنی، فرمانده نیروی قدس سپاه، در سفر غیرعلنی اخیر خود به بغداد با رهبران حشدالشعبی، گروه‌های مسلح و چهره‌هایی از ائتلاف‌های سیاسی عراق دیدار کرده و
پرونده حصر سلاح در دست دولت
را بررسی کرده است. طبق گزارش‌های تکمیلی، قاآنی از گروه‌ها خواسته از هرگونه درگیری با نیروهای دولتی جلوگیری کنند، اما هم‌زمان با
تحویل کامل سلاح به دولت عراق موافقت نکرده
و بر حفظ توان نظامی این گروه‌ها در برابر آنچه «تهدیدهای آمریکا» خوانده شده تأکید کرده است. دولت عراق برای تعیین تکلیف سلاح گروه‌های مسلح خارج از نهادهای دولتی،
۳۰ سپتامبر ۲۰۲۶
را مهلت نهایی تعیین کرده و پس از آن قرار است با فعالیت مسلحانه خارج از چارچوب دولت برخورد شود.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20883" target="_blank">📅 15:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پزشکیان: جنگ کنونی از قبلی بسیار پیچیده تر است و دشمن قصد فروپاشی نظام از داخل کشور را دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20882" target="_blank">📅 15:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری آناتولی به نقل از منابع دولتی پاکستان گزارش داد تفاهم‌نامه قرار است در ۱۷ اوت منقضی شود. به گفته یک منبع نزدیک به روند میانجیگری، دو طرف موافقت خود را با اصل تمدید مهلت به میانجی‌ها اعلام کرده‌اند، اما هنوز درباره مدت دقیق تمدید تصمیم نهایی گرفته…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20881" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری آناتولی به نقل از منابع دولتی پاکستان گزارش داد تفاهم‌نامه قرار است در
۱۷ اوت
منقضی شود. به گفته یک منبع نزدیک به روند میانجیگری، دو طرف موافقت خود را با اصل تمدید مهلت به میانجی‌ها اعلام کرده‌اند، اما
هنوز درباره مدت دقیق تمدید تصمیم نهایی گرفته نشده و تهران و واشنگتن در حال تبادل پیام برای تعیین بازه تمدید هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20880" target="_blank">📅 15:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک منبع ارشد ایرانی به رویترز گفت:
هیچ بحثی برای تمدید آتش‌بس بین آمریکا و ایران وجود ندارد و در عوض، مذاکرات بر بازگشت احتمالی آمریکا به توافق‌نامه تفاهم (MOU) و یک جدول زمانی برای اجرای تعهدات متمرکز است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20879" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش صدای انفجار‌ در‌ جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20878" target="_blank">📅 14:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند. ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20877" target="_blank">📅 13:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بلومبرگ : ایران در دور بعدی جنگ، به سمت یک وضعیت نظامی "تهاجمی" پیش می‌رود. این کشور در حال بازسازی ارتش خود است تا آن را انعطاف‌پذیرتر و تهاجمی‌تر در برابر تهدیدات خارجی کند. این اقدام، در سایه جنگ با ایالات متحده و اسرائیل، نشان‌دهنده آمادگی ایران برای یک رویارویی طولانی‌مدت است، حتی اگر درگیری فعلی به پایان برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20876" target="_blank">📅 13:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیویورک تایمز: در نزدیکی اجلاس ناتو در ترکیه شخصی با موشک دوش پرتاب شناسایی شد!
نیویورک تایمز گزارش می‌دهد که تهدید ایران که ماه گذشته باعث تبادل مخفیانه هواپیمای رئیس جمهور ترامپ شد، در حالی آشکار شد که او در آخرین روز حضورش در اجلاس ناتو در آنکارا، ترکیه، در 8 ژوئیه حضور داشت.
سازمان اطلاعات ایالات متحده چندی  جریان اطلاعاتی دریافت کرد که نشان دهنده یک تهدید موشکی زمین به هوا علیه هواپیمای رئیس جمهور بود، صرف نظر از اینکه کدام هواپیما حامل رئیس جمهور بود.
همچنین شخصی در نزدیکی اجلاس ناتو با یک موشک دوش پرتاب مشاهده شد، در حالی که عوامل ایرانی دقیقاً می‌دانستند ترامپ در آنکارا کجا اقامت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20875" target="_blank">📅 13:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سازمان بین‌المللی دریانوردی:
نشت نفت از نفتکشی که در شمال شرق جزیره قبلیه عمان به گل نشسته است.
انتظار می‌رود نشت نفت از نفتکش کارولین بیزینجی به عمان برسد.
بادها دسترسی به نفتکش به گل نشسته در نزدیکی عمان را محدود کرده و عملیات نجات را به تأخیر می‌اندازند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20874" target="_blank">📅 12:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بلومبرگ
:
سامانه دفاع موشکی «گنبد طلایی» آمریکا نخستین آزمایش‌های اولیه خود را با موفقیت پشت سر گذاشته است.
به گزارش بلومبرگ به نقل از یک مقام ارشد نظامی آمریکا، این مرحله از آزمایش‌ها شامل انتقال داده از حسگرها به رهگیر و همچنین ارزیابی سامانه پیشران فضاپیمای رهگیر بوده است. به گفته این مقام، آزمایش عملیاتی گسترده این سامانه برای اواخر سال ۲۰۲۸ برنامه‌ریزی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20873" target="_blank">📅 11:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تحریم‌های آمریکا، صادرات نفت ایران را محدود کرده و باعث شده بخشی از
مشتقات نفتی، از جمله قیر،
به‌جای صادرات در پروژه‌های آسفالت‌سازی مصرف شود؛ تا جایی که علاوه بر خیابان‌ها، بسیاری از کوچه‌ها و جاده‌های خاکی نیز آسفالت شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20872" target="_blank">📅 11:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مذاکرات ایران و آمریکا درباره تنگه هرمز به نقطه اول برگشت
خبرنگار الجزیره در تهران:
مذاکرات ظاهراً به نقطه آغاز بازگشته و توپ در زمین واشنگتن است؛ تهران ممکن است به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20871" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=YfljZLyWIcML9MTFjkcBmDblUT76nGefAfclnibR7Zoympp0Y3zmeun80Zy4UzXiqq8B_yLTYFGFELjIldH2be4L3-Qtnx8v5U1hholbk-ZxxuM85h6uG8v3bAm0o-Gu8NemgUR6ypIrFPgpYJiPrnNDGjuJhYregx7-FxLczj3byb3PTAd82TXuJWekhoMhPg6LW0afCniMwocCEjev4b8W9-Fi4kWmP0-kGpKQ1JZOO7MjYgEmtDo8GifiE39bgGBKPQ7m5Pihxm8owc79JW6DzU0qH4AqFZ8C4FQ79cVxRhz-uVJrBQXMv37PYYDU3tar5K7gbnQY2vWLHsluAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=YfljZLyWIcML9MTFjkcBmDblUT76nGefAfclnibR7Zoympp0Y3zmeun80Zy4UzXiqq8B_yLTYFGFELjIldH2be4L3-Qtnx8v5U1hholbk-ZxxuM85h6uG8v3bAm0o-Gu8NemgUR6ypIrFPgpYJiPrnNDGjuJhYregx7-FxLczj3byb3PTAd82TXuJWekhoMhPg6LW0afCniMwocCEjev4b8W9-Fi4kWmP0-kGpKQ1JZOO7MjYgEmtDo8GifiE39bgGBKPQ7m5Pihxm8owc79JW6DzU0qH4AqFZ8C4FQ79cVxRhz-uVJrBQXMv37PYYDU3tar5K7gbnQY2vWLHsluAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ : «من از طریق سرویس مخفی و ارتش اقدام می‌کنم. آنها می‌خواستند من با پرواز دیگری، با هواپیمای دیگری بروم... من هر کاری که آنها بگویند انجام می‌دهم... حدس می‌زنم تهدیدی وجود داشته است. من واقعاً زیاد در مورد آن سوال نکردم. تهدیدهای زیادی دریافت می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20870" target="_blank">📅 09:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e3f3981e.mp4?token=s1Ke3El_WjD5PlLYW3S4ppFYDAwaR71Cjh-WbFHg_mZ26F_sqRPv4FV2lrwFb0ycThK3nYGsAfLIU-7zrcLGiwWh-qXUb_uv7BFR9E1kGANcdJ4FTPi6HAZKW-OOsL1T0Ojuez0VO96kSwL1f_UdCzLDnPgh0VbDvBmt81rMGVHE7pudqHNXnfSORHvCo2xH7pTz3XcVLXpd0C7WqpKvn_mrMICtiXvEEnAD9G2ZYTizHhPEpL-YS4JWHK2R5xkWC2WEUkMcV8u_5y9gi4A-mwly_9WIta8pyNdFoB5cO0EqBcAPPWsATXw12KiY-XwfcAtp_ytUNjXGOML1S5OxmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e3f3981e.mp4?token=s1Ke3El_WjD5PlLYW3S4ppFYDAwaR71Cjh-WbFHg_mZ26F_sqRPv4FV2lrwFb0ycThK3nYGsAfLIU-7zrcLGiwWh-qXUb_uv7BFR9E1kGANcdJ4FTPi6HAZKW-OOsL1T0Ojuez0VO96kSwL1f_UdCzLDnPgh0VbDvBmt81rMGVHE7pudqHNXnfSORHvCo2xH7pTz3XcVLXpd0C7WqpKvn_mrMICtiXvEEnAD9G2ZYTizHhPEpL-YS4JWHK2R5xkWC2WEUkMcV8u_5y9gi4A-mwly_9WIta8pyNdFoB5cO0EqBcAPPWsATXw12KiY-XwfcAtp_ytUNjXGOML1S5OxmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
من به ایران اعتماد ندارم، چرا؟ مگه فکر می‌کنید به ایران اعتماد دارم؟
من آخرین کسی‌ام که به ایران اعتماد می‌کنه مدام به من دروغ گفتن، الان ما کاملاً کنترل تنگه رو در دست داریم
اونا کنترلش رو ندارند، ما کامل کنترلش می‌کنیم، مال ماست، شاید یه زمانی کاری بکنن و اون‌وقت کارشون تمومه
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20869" target="_blank">📅 08:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ
:
تهدیدهای زیادی علیه من هست که شما ازشون خبر ندارید
هر رئیس‌جمهور تأثیرگذاری تهدیدهای زیادی دریافت می‌کنه، رئیس‌جمهورهای بی‌اهمیت تهدید نمی‌شند
فکر می‌کنم شاید من تأثیرگذارترین رئیس‌جمهور باشم
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20868" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ
،
درباره نامزدیش :  دوست دارم دوباره تو سال ۲۰۲۸ نامزد بشم، ولی قانون اجازه نمی‌ده
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20867" target="_blank">📅 08:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ درباره اینکه چرا خودش با ایر فورس وان پرواز نکرد ولی خبرنگارا پرواز کردن : نمی‌دونم، اتفاقاً فکر می‌کنم هواپیمایی که من سوار شدم بیشتر در معرض خطر بود
خبرنگار : چرا؟ ترامپ : چون فکر می‌کنم همون هواپیمایی بود که احتمال بیشتری داشت هدف قرار بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20866" target="_blank">📅 08:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edfa0f08c.mp4?token=YWaRX89IHfkn4O54cwV1pzJXdjKmoGPArDsn8GyFiBmt0jDcUr5GuoeYlaLxrEXLk_ss5zFGazVOnHPwcJXC7-fJXOEqOOuN6MsAhjG3lYiQXrEXTTU-5suNYquHqudccfLVe7nUGEUw8A54pPYAffyo4Tm7NOfQi-EuV-EOnZ7oIRAKyWN64BO_kemmkblp1hn6vITRLVWYibegZLIpQzWGz8TtdRVPzyL5eHsY1bn10U9nFlm1qzv0RKujq1fhaVD9bAYsQHfs0X34_dMmcDOsoxQJeXkAJ1PQrqnr9tGNoILc3If_3R4-6PnAi8tFqxjYQSQu2fHHGMLL62RYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edfa0f08c.mp4?token=YWaRX89IHfkn4O54cwV1pzJXdjKmoGPArDsn8GyFiBmt0jDcUr5GuoeYlaLxrEXLk_ss5zFGazVOnHPwcJXC7-fJXOEqOOuN6MsAhjG3lYiQXrEXTTU-5suNYquHqudccfLVe7nUGEUw8A54pPYAffyo4Tm7NOfQi-EuV-EOnZ7oIRAKyWN64BO_kemmkblp1hn6vITRLVWYibegZLIpQzWGz8TtdRVPzyL5eHsY1bn10U9nFlm1qzv0RKujq1fhaVD9bAYsQHfs0X34_dMmcDOsoxQJeXkAJ1PQrqnr9tGNoILc3If_3R4-6PnAi8tFqxjYQSQu2fHHGMLL62RYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
اوضاع ایران داره عالی پیش میره ما کاملاً کنترل تنگه هرمز رو در دست داریم و نیروی دریایی‌مون فوق‌العاده‌ست
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20865" target="_blank">📅 08:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">زاکانی : آقا مجتبی داشت تلویزیون میدید یهو تو اخبار شنید رهبر شده
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20864" target="_blank">📅 08:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=Syl9DoHwuJf2oVzWgDffchlRNkpPNMcSRSWEr3hTxHcf24K6RcBsffnBAlxeKjA_XrS7X7AIy2E0CJEF6yC3Xk9KgohrBwDVXk-aVwnHHv4ZmmL4oVB9Z0FO9pIO2uC4X5FQT3UDuy3U_UrYlRcpMjUlV3VBxhNPXmo9JRH0RlkAM0SWQFXxDEMPB7i_x_WxYrWnqtQH_QkHf54KEIOWhilbmO6CWPvhP6-SAzO1UH8DdLd1fEwp0f-JcfEJ9cKJAbuuqmkW4aGakWwvexjYyXpxtlT73r6GOqoV0wQ5EfSgK6g4MaDQxHFxXtzt24dmnAmkQ-21z4ax-hhK3c1qeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=Syl9DoHwuJf2oVzWgDffchlRNkpPNMcSRSWEr3hTxHcf24K6RcBsffnBAlxeKjA_XrS7X7AIy2E0CJEF6yC3Xk9KgohrBwDVXk-aVwnHHv4ZmmL4oVB9Z0FO9pIO2uC4X5FQT3UDuy3U_UrYlRcpMjUlV3VBxhNPXmo9JRH0RlkAM0SWQFXxDEMPB7i_x_WxYrWnqtQH_QkHf54KEIOWhilbmO6CWPvhP6-SAzO1UH8DdLd1fEwp0f-JcfEJ9cKJAbuuqmkW4aGakWwvexjYyXpxtlT73r6GOqoV0wQ5EfSgK6g4MaDQxHFxXtzt24dmnAmkQ-21z4ax-hhK3c1qeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در محل بازی‌های میهن‌پرستانه:  به والدین نگاه می‌کنم، آنها به فرزندانشان بسیار افتخار می‌کنند. و من به گروه افراد حاضر در این اتاق بسیار افتخار می‌کنم. عشق به کشورمان را می‌بینید. کشورمان هرگز بهتر از این نبوده است!
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20863" target="_blank">📅 02:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چیزی نیست رعدنیاهو بود غرب تهران
😂</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20862" target="_blank">📅 02:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش صدای رعد و برق شدید</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20861" target="_blank">📅 02:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بلومبرگ
:
دونالد ترامپ موضع خود را در قبال ایران سخت‌تر کرده است و این امر، امیدها را برای دستیابی به توافقی جهت بازگشایی تنگه هرمز کمرنگ‌تر ساخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20859" target="_blank">📅 01:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش ها از درگیری تمام عیار زمینی میان حوثی های یمن و نیروهای نظامی وابسته به عربستان در شمال یمن.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20858" target="_blank">📅 01:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آمریکا 2 هزار گیمر رو به‌خاطر تصمیم‌گیری سریع و عملکرد خوب تو شرایط پراسترس ، برای برج مراقبت فرودگاه‌ها استخدام کرده
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20857" target="_blank">📅 01:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=HApLhOSbgQiWH7IbMrYTujsuQPAp8eYDFloMQf-5P5H7kn5qAR_y6EonJJS9o-PQPrCQ72gCofKJbEpk-mDM6QFVlyv8AFx8mQZdmqZhqxKgHHGX_2sqCs_td9isiUI_72RAXRlcEftrPrfaIkDEboNOjaisk51ZDzAHqrNvFQbSwUBydYPzHVjiFro1howVtZdFFqpFyMaTh_kmILq1S9lrSF3xz40XI_JZqyVEe2k-C4b7h8iH1hFYxGLuLthH_TRzm696rckFBOy0K1f1Qekk-Y5TW6TUeXsBcmotWY1w_w0JrYnEMWmVx-17J7E0J2H2PO_nAB0jHpsWYBRlkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=HApLhOSbgQiWH7IbMrYTujsuQPAp8eYDFloMQf-5P5H7kn5qAR_y6EonJJS9o-PQPrCQ72gCofKJbEpk-mDM6QFVlyv8AFx8mQZdmqZhqxKgHHGX_2sqCs_td9isiUI_72RAXRlcEftrPrfaIkDEboNOjaisk51ZDzAHqrNvFQbSwUBydYPzHVjiFro1howVtZdFFqpFyMaTh_kmILq1S9lrSF3xz40XI_JZqyVEe2k-C4b7h8iH1hFYxGLuLthH_TRzm696rckFBOy0K1f1Qekk-Y5TW6TUeXsBcmotWY1w_w0JrYnEMWmVx-17J7E0J2H2PO_nAB0jHpsWYBRlkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ برای شرکت در رویداد
Freedom 250 Patriot Games
(رقابت‌های میهن‌دوستانه ورزشی ویژه جوانان آمریکایی به مناسبت ۲۵۰مین سالگرد استقلال آمریکا) عازم شهر ژنو در ایالت اوهایو شد و سوار هواپیمای ریاست‌جمهوری
ایرفورس وان
جدید شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20856" target="_blank">📅 00:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش ها از هدف قرار گرفتن ایست ‌و بازرسی نیروهای نظامی توسط افراد مسلح ناشناس در شهر مرزی خاش در سیستان و باوچستان ، بر اساس گزارشات داخلی 4 نظامی در این حادثه کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20855" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محمدرضا نقدی، مشاور فرمانده سپاه، گفت که «این سازمان باید برای انجام عملیات هوشمند در خاک دشمن آماده شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20854" target="_blank">📅 00:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم  @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20853" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMdQwTo0Ws5Wm4cYbTWBxMPiCIdyYppXrt2_QSk4fxT-UYSmc20TWN85I92xXQ9mN_mOL-DDWCgSSUCdAA7V_FFdWa5tBweLEZG0UHGGrKYG7Ej3GkbsdNKUG-xdZBl34PtHvru7IMa370Xh0NBb4hegpDMvHH4C7dWY97UwBVIGVtr6qz5ufM2qsh6yQzIr-gQeYm7iRjiDaSvp2fDhgZvu5lsh_eCQtvmsfX311Vjz7frF4allx7tczhspRvs0667q_eObE0c0IxPtmsiZbk9qdEmZQwh-kgu2H_WIe6qSNfaOBWP9Ec2snnHXXpAgXPukEyI9UgfyCXuE_xlNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20852" target="_blank">📅 23:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">باراک راوید , آکسیوس : امید به توافق میان جمهوری اسلامی و آمریکا در حال محو شدن است
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20851" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVlrNaw_ESSXF0n3uUNLl5-Gpm12Agpyfxq2S4e5cfkNXGiUDokXIy0YVNzbQHeWnohcN0WoGYwwL3doDXX7bVBEMY4oDorfANWUss7hjMZa4kfP8JoY8YzJg4stnVhUTxl09dlpsnyCpasQXX7hfCHN0srwK452xmE2GNf-MM8mgkqTOgfJG-Uo0At4tYwWzbc9QbopMRvwcyXZ4x3kv8BHKE13ZGhq01mC0E-uBNfVYkJpDo7V20LYfgrIeouASL_mkxogymMTLX1P92N32Ll_ZmMFi59AW0-HAsunduyfQTG7NiPDlPnQbIDol4BjEgO8tQ5dGONLVXJkVfe8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی امروز کشتی باری «ولا نوا» با پرچم پاناما را هنگام حرکت به سمت یکی از بنادر ایران در خلیج عمان متوقف کردند. پس از بی‌توجهی خدمه به هشدارهای آمریکا، یک بالگرد MH-60 دو موشک هل فایر به اتاق موتور کشتی شلیک کرد و سامانه هدایت آن را از کار انداخت. سنتکام گفت تا ۱۱ اوت، ۵۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را سوار و بازرسی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20850" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA B</strong></div>
<div class="tg-text">یاشاار
جون هرکی دوست داری زارتان زورتان و حذف نکن از ادبیاتت
من هم توهمی دهنم سرویس شده
از وقتی نمیگی برکت از جنگ رفت
🤣
خداییش جدی میگم</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20849" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سازمان دریایی بریتانیا: فعالیت‌های سپاه در تنگه هرمز در طول 48 ساعت گذشته ادامه داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20848" target="_blank">📅 22:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دونالد ترامپ در چارچوب قانون اختیارات جنگ آمریکا (War Powers Resolution)، با ارسال نامه‌ای به کنگره که ۱۹ تیر ۱۴۰۵ امضا و ۲۲ تیر ۱۴۰۵ به‌طور رسمی اعلام شد، از ازسرگیری عملیات نظامی علیه ایران خبر داد. با این اقدام، مهلت قانونی ۶۰ روزه برای ادامه عملیات نظامی بدون مجوز جدید کنگره آغاز شد. این اقدام به معنای صدور مجوز جنگ از سوی کنگره نیست، بلکه صرفاً روند قانونی اطلاع‌رسانی به کنگره و آغاز مهلت ۶۰ روزه را فعال می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20847" target="_blank">📅 21:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20846" target="_blank">📅 21:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">من با دیتا های اپن سورس تحلیل میکنم پیشگو که نیستم ! هیچ تاریخی هم نمیدم فقط احتمالاته اگه انقدر حساسی  پس از الان رو نزدن حساب کن  ! اگه حرفه ای هستی پس ویس هارو گوش کردی کامل روحیات منم میدونی و دیگه سوألی هم نداری که هی داریکت بدی</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20845" target="_blank">📅 21:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20844" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Mousavi</strong></div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20843" target="_blank">📅 21:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20842" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20841" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ اعلام کرد که رابرت گیلمن، سرباز سابق نیروی دریایی ایالات متحده که در سال ۲۰۲۲ در روسیه زندانی شده بود، پس از گفتگوها با ولادیمیر پوتین، آزاد شده و به ایالات متحده بازمی‌گردد.
ترامپ گفت که روسیه موافقت کرده است گیلمن را بر اساس «ملاحظات انسان‌دوستانه» آزاد کند و «هیچ مبادله‌ای انجام نشده است».
ترامپ همچنین گفت که اولین درخواست گیلمن یک «همبرگر عالی» بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20840" target="_blank">📅 20:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ : ما بر پول ایران کنترل داریم و کنترل کاملی بر آن اعمال می کنیم
ترامپ : سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20839" target="_blank">📅 20:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اسرائیل و ونزوئلا پس از ۱۷ سال قطع روابط دیپلماتیک، توافق کردند که روابط کنسولی خود را از سر بگیرند و یک کانال هماهنگی رسمی ایجاد کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20838" target="_blank">📅 20:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797367122e.mp4?token=j4PyPPliH_kzHwGy9hLgiGPcYTnomj52b3n6w5qz0IBC1kecqlEoo-0rvW7iCkck6QYBOXtKXVldBW44En5Q87WvYRFmV_URP5sRCKdcTK0chM_92oQd_KpR14xfh8jtuWXAacHQ9G1VwWIrgV_quUAuybqKtJFYVPwc_8OTGMOUENeogce5E48rv-i2L0zCU-jPkv6Mn18Q5pUWBJGQpc63v7unBd-iqzSLvm07GJ13IOtMiCL8KQQozthQakOo98LrYvhmt3yc8EC5T0n0gHH43UrDYeNPA8WJbnxi5-KeG0gTM3af2mgUJT_BoQPAS_sGE4rJPPn5QoSM03ab0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797367122e.mp4?token=j4PyPPliH_kzHwGy9hLgiGPcYTnomj52b3n6w5qz0IBC1kecqlEoo-0rvW7iCkck6QYBOXtKXVldBW44En5Q87WvYRFmV_URP5sRCKdcTK0chM_92oQd_KpR14xfh8jtuWXAacHQ9G1VwWIrgV_quUAuybqKtJFYVPwc_8OTGMOUENeogce5E48rv-i2L0zCU-jPkv6Mn18Q5pUWBJGQpc63v7unBd-iqzSLvm07GJ13IOtMiCL8KQQozthQakOo98LrYvhmt3yc8EC5T0n0gHH43UrDYeNPA8WJbnxi5-KeG0gTM3af2mgUJT_BoQPAS_sGE4rJPPn5QoSM03ab0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20837" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رسایی : چونکه نمیدانیم اسرائیل کِی حمله میکند مجبوریم جلسات مجلس را مجازی کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20836" target="_blank">📅 20:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پست قبلی بی بی پاک شد این پست کارای اداری رو انجام بدید
https://www.instagram.com/reel/Db6BHf7MYhi/?comment_id=17896725462373851</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20835" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
