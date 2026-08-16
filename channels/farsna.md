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
<img src="https://cdn4.telesco.pe/file/C2VyBWeKVzNo7REt-WmcqK-x1xN2Od7WKyKsSrUMI20padjJeqkmStE2eDkI77Gbc4H_dntbDxh8gEJ3jQrrvuqyHMGUr52JPOMJM4SCAfMEillDJcrSwObiXkc_ut5OpzNQO0dbL549Jymadu-MJg_A0LZX2PbLdwCrK29gpRMUwH4FSETeHZx5LoQKMCFAMWJZgY0vcHm1DQneoqK4NWR8QQobei4qcfUAH1gNVzabjnylVg9rkeaBCHg2x6pgbYV28vCXhdhZxRzJWlUjgtA2raNVct5J7RavNoJ5JypcGvttLaMBtQiueIa6LiQQA9Q6mYtMkU6jAHHOIIzo0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 21:11:39</div>
<hr>

<div class="tg-post" id="msg-456438">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGCLdANpIFVNDQeXZkN2-GY4PyPBGaBoBM0pYinVrmqyhZtbKVAGqSYMFNNYY_C5rwPxsroUlL5HxwT3DiiMbdZKMzsfl6YOKBuJbydpCXByBUFqyBayoGNOfC8AkQIqJeonRUGoqi6hlsKnzH2c2soHnq2_WryHiT9R2AsmNeXwQfE4bWMHJK0sJzAb3WxBz5CGO1ZUZA72PAf-6JdSZI5jx9aKOXmVcmloRwdAEByS3PnkpTJSu2E6whKqgWC9Q6h3GiXBJLXVbaQUwq2o2rMTUBeAyxLG5ksmeAyh87BeSaU4-gi1VdvJHM1ccU4MtAMOtW6M_McC5yTlckStRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان فرمانده آمریکایی به غافلگیری از انهدام پایگاه‌ها توسط ایران
🔸
بالاترین مقام نظامی آمریکا در دوره باراک اوباما روز یکشنبه تأکید کرد که آمریکا فکرش را نمی‌کرد که ایران پایگاه‌های منطقه را «نابود کند.»
🔹
رئیس اسبق ستاد مشترک ارتش آمریکا مایک مولن در مصاحبه با ای‌بی‌سی نیوز به بررسی وضعیت نظامیان آمریکایی در غرب آسیا از جمله ملوانان ناو آبراهام و طولانی شدن مأموریت این ناو هواپیمابر گفت:‌ «این موضوع قابل توجه بوده و بسیار دشوار است. این استقرارها بسیار دشوار هستند. از نظر تاریخی، ما معمولاً قادر بوده‌ایم برای استراحت، انجام تعمیرات و سپس بازگشت به عملیات، به یک بندر برویم. حتی در زمان ویتنام، این کار را انجام می‌دادیم.»
🔹
فرمانده اسبق آمریکایی با ابراز نگرانی درباره وضعیت ملوانان در ناو آبراهام لینکلن بیان کرد: «من قطعاً با توجه به آنچه در گزارش‌های خبری دیدم، نگران شرایط کشتی بودم. می‌دانم که فرمانده ناو لینکلن، به سختی روی این مسائل کار می‌کند و همچنین معتقدم که حقیقت احتمالاً جایی در میانه (گزارش‌ها) است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 332 · <a href="https://t.me/farsna/456438" target="_blank">📅 21:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456437">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd38bfd178.mp4?token=ar-T2gdzdRKbzPM8tg6b5PCjr5UmGdWr_8KmJnH1F6Zc8EorLZOgCqFFVa-_9rrV26UM8UsbVKtTYF7UIAH8QFzuj1QVirfNzeFaxWLrn_Lnl0UyE1FyI9KRNZAjd0TcWDxzc7NCrZLKF-0Fb0ZLO38Z9alC2T2kbdV1EQABbX7hdLXElQCUjtN70HvHvzjZg9ZnZnM3924_jSX-ju1eBr8tTLhY0n0fUU6vFzibPQvvtG2OB0SwOdyxoGzu_qf93T3ktJlLGY__d6wf3pZPoK9f5XGpWpJ134Vnwa9blO0eNUWCwwg26eIXLPqEifG6d13erS7lFbkyurie8MX7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd38bfd178.mp4?token=ar-T2gdzdRKbzPM8tg6b5PCjr5UmGdWr_8KmJnH1F6Zc8EorLZOgCqFFVa-_9rrV26UM8UsbVKtTYF7UIAH8QFzuj1QVirfNzeFaxWLrn_Lnl0UyE1FyI9KRNZAjd0TcWDxzc7NCrZLKF-0Fb0ZLO38Z9alC2T2kbdV1EQABbX7hdLXElQCUjtN70HvHvzjZg9ZnZnM3924_jSX-ju1eBr8tTLhY0n0fUU6vFzibPQvvtG2OB0SwOdyxoGzu_qf93T3ktJlLGY__d6wf3pZPoK9f5XGpWpJ134Vnwa9blO0eNUWCwwg26eIXLPqEifG6d13erS7lFbkyurie8MX7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی نگهبان بیمارستان ناجی یک نوزاد شد
@Farsna</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/farsna/456437" target="_blank">📅 21:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456436">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0585e0cd.mp4?token=WIzYl0sHDSg3BL9f4tJsVGg3GbUvU232JTGrlynve50qSUgDOwgct7sG0Vu__urT55aPk3r2N5BUe-Yde9gQkQK8-iqlDE6QkvyW46dK2KYFdH8Plfru_BBZj2iHR2o38_An6mwtB0ulwnIIixlf0gnt1EbBYFwhFD3UokTelO5cXu0QIBIjgaRdo2Pe4ymzvjM-baaoLP2yS79s7DltvHVjvEUOJRdf2xIMCJu5eMuiBNZaOdBnrqqzc9hI6KnILI1lfxvjUSxZj1Rocg0NmpO75Wsx796dJytaU3HKgckSnBwHOkQY4G3U4vUUkx4jxII5bVxaWYubuCKSlPAV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0585e0cd.mp4?token=WIzYl0sHDSg3BL9f4tJsVGg3GbUvU232JTGrlynve50qSUgDOwgct7sG0Vu__urT55aPk3r2N5BUe-Yde9gQkQK8-iqlDE6QkvyW46dK2KYFdH8Plfru_BBZj2iHR2o38_An6mwtB0ulwnIIixlf0gnt1EbBYFwhFD3UokTelO5cXu0QIBIjgaRdo2Pe4ymzvjM-baaoLP2yS79s7DltvHVjvEUOJRdf2xIMCJu5eMuiBNZaOdBnrqqzc9hI6KnILI1lfxvjUSxZj1Rocg0NmpO75Wsx796dJytaU3HKgckSnBwHOkQY4G3U4vUUkx4jxII5bVxaWYubuCKSlPAV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی، وزیر سابق کار: می‌شود هم جنگید، هم اقتصاد را مدیریت کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/456436" target="_blank">📅 20:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456434">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d085f71d9.mp4?token=vdKZ7OJhuvVrSTSIJloHQhbf0z1knvbm5IRirztb85axfT3R9laeHIJB0bUxaBqgMYdekOJ95Rx6f0gzk_W3wc_u4JITgpzLU5Eht-Zi9U7JkpI69G2CKzzTo90UhKWH0uRen6oP6owOgsXBoO4tSUB-4bUhYmdl1gJNJaRDrouMQz47j--ajB7ZGDV-9khGfSnJyv75Qr2D3_KaBgKLNm44fZxcw6JQhtJ2iPdpjmU2nkHAcIrkpExqPAEaCdU5aKhTkbrv4eBK_R4539A39uQOvKh4WwCv_fW2LdpHn4fb0ckQZHbVKgG6urQ8UM8f7tQEg4p3HYFc8r7i2chCLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d085f71d9.mp4?token=vdKZ7OJhuvVrSTSIJloHQhbf0z1knvbm5IRirztb85axfT3R9laeHIJB0bUxaBqgMYdekOJ95Rx6f0gzk_W3wc_u4JITgpzLU5Eht-Zi9U7JkpI69G2CKzzTo90UhKWH0uRen6oP6owOgsXBoO4tSUB-4bUhYmdl1gJNJaRDrouMQz47j--ajB7ZGDV-9khGfSnJyv75Qr2D3_KaBgKLNm44fZxcw6JQhtJ2iPdpjmU2nkHAcIrkpExqPAEaCdU5aKhTkbrv4eBK_R4539A39uQOvKh4WwCv_fW2LdpHn4fb0ckQZHbVKgG6urQ8UM8f7tQEg4p3HYFc8r7i2chCLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظرتان در مورد کالابرگ چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/farsna/456434" target="_blank">📅 20:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456433">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d120771984.mp4?token=bXhtikvOnOA6dpPzw4jHF60tKbM4kFgrHAO7RikMZ7TCaGCgKpPA-rRXx9ozyNDJowtu-8K70ZaJMZ0-xd_jecQcS0vaf84OvRIYCKjX5qRhJz8d5QIpN7slaa0P4lGRNRSo2fXYFbFsi2zVlGLFqnIWQ8NPNTdy5boCzPY4oZroVG33-3EA7iYtqZiPI8tX48evjb_fGUqCXeSMnUGNi4iABzWPnpYiMZEx93mxZBh2bXkyKTRY8M9ELag6kyFjEJ5rtDt3kIpZJP9FLn-ZIEsq03YLhhdxDhv8lYmZejNLn__dnc-v5N3MnBibtjonj8_vnfIMbW8jCBRIe3gcqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d120771984.mp4?token=bXhtikvOnOA6dpPzw4jHF60tKbM4kFgrHAO7RikMZ7TCaGCgKpPA-rRXx9ozyNDJowtu-8K70ZaJMZ0-xd_jecQcS0vaf84OvRIYCKjX5qRhJz8d5QIpN7slaa0P4lGRNRSo2fXYFbFsi2zVlGLFqnIWQ8NPNTdy5boCzPY4oZroVG33-3EA7iYtqZiPI8tX48evjb_fGUqCXeSMnUGNi4iABzWPnpYiMZEx93mxZBh2bXkyKTRY8M9ELag6kyFjEJ5rtDt3kIpZJP9FLn-ZIEsq03YLhhdxDhv8lYmZejNLn__dnc-v5N3MnBibtjonj8_vnfIMbW8jCBRIe3gcqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ فسفری اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات جنگنده‌های رژیم صهیونیستی به مناطقی در جنوب لبنان از جمله منطقۀ علی‌الطاهر خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/456433" target="_blank">📅 20:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456432">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دربی تهران در انتظار تعیین تکلیف میزبانی
نقش‌جهان قطعی نیست
🔹
طی ساعات گذشته شایعاتی پیرامون باشگاه معرفی قطعی ورزشگاه نقش‌جهان برای میزبانی دربی توسط باشگاه استقلال مطرح شده که پیگیری‌ها نشان می‌دهد صحت ندارد. از طرفی سهراب بختیاری‌زاده در این مورد هنوز نظر نهایی خود را نداده و تصمیم شوراهای تأمین و مسئولان ورزشگاه و استانی نیز تعیین‌کننده است.
🔹
استقلال ورزشگاه نقش‌جهان اصفهان، پارس شیراز و امام خمینی اراک را به‌عنوان سه گزینه میزبانی دربی تهران مدنظر دارد و دراین‌رابطه همچنان مذاکرات خود را در ادامه می‌دهد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/farsna/456432" target="_blank">📅 20:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456431">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=jJtr__nOxGyFSacPZwAYK2_dgL9gOPE_iWyk8-55F_EYOZ8mt-fxeM0Mg_ijFruuGQ8DGus0qzBe8ZhG93mBjjf_il7svAihh1wh6-AvWhpfsZOFKIg1Ork7d5xBpcbKhJjIUNjtZowM1SWVjEV05aM1QfdsUK6vNHeNzlvORt1I0___8XkOJCeL4Uphq-fus_9qJoRlcIU-lpZIrPthEB6LiVdrVpIH0joiW44CDLI60wIGK4d968kx830jTITn9BdPohs_9SRr-MvsTBY2LTP0_AhtiG3bcFLyIMIewHgXno-0vnl00q5viCg0l7VU1jCH91LDcj_V6JgE4WnFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=jJtr__nOxGyFSacPZwAYK2_dgL9gOPE_iWyk8-55F_EYOZ8mt-fxeM0Mg_ijFruuGQ8DGus0qzBe8ZhG93mBjjf_il7svAihh1wh6-AvWhpfsZOFKIg1Ork7d5xBpcbKhJjIUNjtZowM1SWVjEV05aM1QfdsUK6vNHeNzlvORt1I0___8XkOJCeL4Uphq-fus_9qJoRlcIU-lpZIrPthEB6LiVdrVpIH0joiW44CDLI60wIGK4d968kx830jTITn9BdPohs_9SRr-MvsTBY2LTP0_AhtiG3bcFLyIMIewHgXno-0vnl00q5viCg0l7VU1jCH91LDcj_V6JgE4WnFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حضور یک شهروند ناشنوا در تجمعات شبانه
@Farsna</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/456431" target="_blank">📅 20:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456430">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f9ee6e4c.mp4?token=a8oDTKd7Z-SPRbsJEeZ_0yHpX-tvxiDDrlGP5vQTgGpCi3p2eeHnac8G41WX8xk9Tc1vWU81aTlzZQIkJ5B98guZRmwYz-mRwn6F6RsZ8aa2RnK90kSkFV05N4A07VAXVO50azY7QJzSWnWNeFPyvyXjKS8RWjpByfiNhRvz9Ub-6ieE-XIEWUsDp29eDbuL7IrcYs3harCoYARz-xK15pCadq1pH9ct5CyfM_qJLV9xCni6YUYW6P9SMQlnv6tR2Lrtih68qPkqpjBmxdeTAVt6R1qLoFgJVCRChK7pGjrGYUPWfFs5SmJLSeADSeaWvVVsgdRhxZkhOjmripvQ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f9ee6e4c.mp4?token=a8oDTKd7Z-SPRbsJEeZ_0yHpX-tvxiDDrlGP5vQTgGpCi3p2eeHnac8G41WX8xk9Tc1vWU81aTlzZQIkJ5B98guZRmwYz-mRwn6F6RsZ8aa2RnK90kSkFV05N4A07VAXVO50azY7QJzSWnWNeFPyvyXjKS8RWjpByfiNhRvz9Ub-6ieE-XIEWUsDp29eDbuL7IrcYs3harCoYARz-xK15pCadq1pH9ct5CyfM_qJLV9xCni6YUYW6P9SMQlnv6tR2Lrtih68qPkqpjBmxdeTAVt6R1qLoFgJVCRChK7pGjrGYUPWfFs5SmJLSeADSeaWvVVsgdRhxZkhOjmripvQ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند هوایی سپاه: در روزهای اول جنگ ۶ تا ۷ پهپاد هرمس و هرون رژیم صهیونیستی همزمان بر فراز جنوب لبنان گشت‌زنی می‌کردند
🔹
با هدف‌قرارگرفتن این پهپادها در ایران، تعدادشان در جنوب لبنان به یک فروند رسید و حزب‌الله آزادی عمل بیشتری برای عملیات پیدا…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/456430" target="_blank">📅 20:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456429">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4eba8a433.mp4?token=mK778hp_V_XCbmBLl1kUhVpFSUf33ugQnj5x2U7SZm71URSsxth4Eq1Q8EvreI_QUqY1jMrZe_UenYfZpEeq44kNbNmSH9rmD4_hYIWphDBETMxkiwEctUE7BFeaIkJwlIQyvc3-W6vPIFcld15nDfuChFk6hyPzFuDldo-bJEhaCFOsIFF8G9ugwbC50NGW3Sg4V-dR25ejgkrOQyUp5Haz7Pi53KpnRMXvs_FP5mJGG8EwTx4A5EVNGD_sfJorr3Q5lBONlJgrgMoUp-2hMpvTRm-YMNFtYDKVncg46tviqeEP_XNL8avmsMV_Pp_LK6R1QjMJPJPktHvXhugD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4eba8a433.mp4?token=mK778hp_V_XCbmBLl1kUhVpFSUf33ugQnj5x2U7SZm71URSsxth4Eq1Q8EvreI_QUqY1jMrZe_UenYfZpEeq44kNbNmSH9rmD4_hYIWphDBETMxkiwEctUE7BFeaIkJwlIQyvc3-W6vPIFcld15nDfuChFk6hyPzFuDldo-bJEhaCFOsIFF8G9ugwbC50NGW3Sg4V-dR25ejgkrOQyUp5Haz7Pi53KpnRMXvs_FP5mJGG8EwTx4A5EVNGD_sfJorr3Q5lBONlJgrgMoUp-2hMpvTRm-YMNFtYDKVncg46tviqeEP_XNL8avmsMV_Pp_LK6R1QjMJPJPktHvXhugD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرواز دوبارهٔ ۲ عقاب‌ در آسمان دالاهوی کرمانشاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/456429" target="_blank">📅 20:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456428">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5744721f52.mp4?token=Ewn5WS17MB7j5kAUJWl0dGfafdGf_sdUz6IsLgJ4pzguSIBndgytlKGLKMVZ3oSx5u4lp405TEBCI6h6fHm4EXxIhbx5NDqkxFM-fx--j-33AA_bg4CsPGzPeBh8EYvpUBBC19dxsQvzdsnRtl5eFGc3HPhfkk3TIskU9r7jhTgNExV_JJxFsaztQXZoNlm1iHNnqC5Hyf93a1xE_imCGrYhrV1xqHcdb4dQjPMFX1fyAr46QZinZwGYuSjok_S9AJzS_7DxGiy9a8vXVEyvhQjnhD5OErsZDrlCu8Bs-VR-rhes_V4NDSWf2Hxh5uN-0cnzPru7BWWG5X76WEJKgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5744721f52.mp4?token=Ewn5WS17MB7j5kAUJWl0dGfafdGf_sdUz6IsLgJ4pzguSIBndgytlKGLKMVZ3oSx5u4lp405TEBCI6h6fHm4EXxIhbx5NDqkxFM-fx--j-33AA_bg4CsPGzPeBh8EYvpUBBC19dxsQvzdsnRtl5eFGc3HPhfkk3TIskU9r7jhTgNExV_JJxFsaztQXZoNlm1iHNnqC5Hyf93a1xE_imCGrYhrV1xqHcdb4dQjPMFX1fyAr46QZinZwGYuSjok_S9AJzS_7DxGiy9a8vXVEyvhQjnhD5OErsZDrlCu8Bs-VR-rhes_V4NDSWf2Hxh5uN-0cnzPru7BWWG5X76WEJKgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک امدادگر از جنگ رمضان: پدرم گفت حق نداری به خانه بیایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/456428" target="_blank">📅 20:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456427">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhjNju2QK6HstkK3Gyo3m9cHIGIKNwHWWj3888dqXnvnW6lGM0Uh7y-9OknP0UEdhwSfaIbBg5w0IW_Xp0sVb62h2KSJax8i-rl0dFiavASStX6GSwmyHkRJYT0nfpo8eh5SdUpCpdwZT-M2WVzmTfeiD_eX9zKa1lUc_IBtybflRfdcxGl0cEKk2F1_FNwMNYFy_w1btdYO12ZAM5Dfc8zXMElOds4EgQwLlCGgyE62oKBMtGNPj7vis9NuoGK_RqJXIWcGtHhyD7dU_NhAqtSZSwbAOJtvNBEI43t_3ntW5nlK78Kxc5dDawcdmVkwZths2cMlAeWPIUqrofN38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه ۲.۴ میلیون زائر در مسیر اربعین
🔹
همراه اول در اربعین ۱۴۰۵ میزبان ۲.۴ میلیون مشترک در عراق بود؛ زائرانی که با استفاده از خدمات رومینگ، بدون نیاز به خرید سیم‌کارت عراقی ارتباط خود را حفظ کردند.
🔹
تخفیف ۳۰ درصدی بسته‌های ویژه سماح، ارائه ۱۰۰ هزار بسته ۱۰۰ گیگابایتی اینترنت داخلی، بیش از ۳۰۰ هزار بسته ویژه روبیکا و پشتیبانی شبانه‌روزی در مرزها و شهرهای زیارتی، از جمله خدمات همراه اول در این ایام بود.
http://mci.ir/-7J70P9
@mcinews</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/456427" target="_blank">📅 20:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIzsQ2zS4FzllfFEDPeKDsNCz4RN8PSqTBI3tnzR7rGmr76_HngouIGEZCveNsSn49lPFiK4v438QqVttLVLKSxE5W53a5Uyma5ePms4v1oBpnVEdYA_F2ZbuPDHgbByrQmtKZ2fZzj1xYfsrCpDuFGSjprLQmWwJGvQZrgMMTu106jmVLQCuiv8T92VNW2-oYu3sGygK_vFj_C9fkJfp8xctcfjucEek50-FvJuJUq1IGSh6sDP8ErTOc0pRJ-rGivfDM8V5Okg7-ZXeqrb79_5yayO1HBsbZUpiyrwWipWrCD7DkMmjOaW7y93y__rWmvvkdc1ZjN26gFIK8GfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔮
کانال مِتانو | آموزش هوش مصنوعی
🔐
محتوای Vip و غیر قابل دانلود
🤔
عضویت فقط با خرید اشتراک
😡
اشتراک یکساله: 1 میلیون تومان
😎
390 تومان با کدتخفیف: fars
🤖
آموزش بیش از 200 موتور تولید متن، تصویر، ویدئو، صوت و اپلیکیشن.
🧠
تا کنون بیش از 110 مینی دوره با ارزش تقریبی 40 میلیون تومان بارگزاری شده.
✅
مشاهده نمونه آموزش ها و پیگیری مراحل ثبت نام از طریق آیدی پشتیبانی:
🎁
@Metano_Ad</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/456426" target="_blank">📅 20:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/456425" target="_blank">📅 20:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzvjw5DdGAmtsSeqGnfZ-zkjHSMJS0VFwJ9FADDDPo9J_ExZEUW0oYjT9CXJRVOMUeXQq2emeA590wcfSqRUXoKVzwczYsRt-RqPy3eRfPt_tVu4ndw7_qbBgqUty5y_P7C87CLAwppIJJHDgHAL-vHzTcNe23fSqP_3swbU9vDf4kj6Fc5WxrllJBH4QSaHU17br6x7Qw07YuxjfwtGRZWaDFbrUTeo-lEHz-WTrwF46__5esk5jxPy3DXwmUBzZQ-3_Ya-gaw4veiUv7a7Spg69d-gZKOgWslyNac5PErquzLtT_xrE2ZlIw1_4tnr37rts3Xz42_EY-ab0vN_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انتصابات مدیریتی باید علمی و فارغ از ملاحظات سیاسی باشد
🔹
انتخاب، ارزیابی و حتی عزل‌ونصب مدیران و اعضای هیئت‌مدیرۀ شرکت‌ها باید براساس شاخص‌های روشن، علمی و قابل سنجش انجام شود تا از شکل‌گیری هرگونه شائبه، حرف و حدیث و ملاحظات غیرکارشناسی جلوگیری شود.
🔹
معاون اول رئیس‌جمهور و وزیر علوم گروهی از استادان دانشگاه در حوزه مدیریت، شاخص‌های لازم برای ارزیابی مدیران در دستگاه‌های اجرایی، شرکت‌ها و سازمان‌ها را تدوین کنند تا این شاخص‌ها برای ارائه به رهبر انقلاب آماده شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/456424" target="_blank">📅 19:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456422">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc4tAbVlhGgI3hfdB2ayTjNU73fBxfhMwasePRntUKae968s_gsJ-2zvHspDUtTK5d79Lve3OV5HE5RFmOkpiXffodSzY39As6Vu0xcmYNyn_hW-e2-cI46wxQ4mXxXJoDT6qG9Q6mGjknsoWBisbnqpog6uf6KKaU0Hdv3iG_5vr0iIvVWpr3fUfIo-BMuOo7NY-adO-lancNSvsENZUJeRWwIPyIKqZcQEqRVV6iRcyknVUXDaYTZg5WMIUNvR_me2zhTz0RgI6p3uJGNDTi9hp2hbnTf8QOpKKQhu2bhOTe2Rxjc35eI2l61tIboHP40LdMPV3URar1zDDZ_-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا خلع سلاح اتمی اسرائیل باید مبنای توافق پایان جنگ باشد؟
آمریکا و رژیم صهیونیستی در جنگ با ایران به بن‌بست رسیده‌اند و اکنون ۲ راه پیش روی خود دارند:
🔸
تهاجم سنگین‌تر به ایران برای به‌دست‌آوردن آبروی ازدست‌رفتۀ آمریکا.
🔸
پذیرش شکست نظامی و ادامۀ خباثت علیه ایران در حوزه‌های دیگر از جمله تحریم.
واکنش ایران در قبال تشدید تنش چه باید باشد؟
🔹
فعال‌کردن جبهه‌های جدید و افزایش سطح درگیری.
اگر سطح درگیری به حوزۀ اتمی رفت چه؟
🔹
ایران احتمالا در دکترین هسته‌ای خود تجدیدنظر خواهد کرد.
🔹
توازن به‌کارگیری سلاح در سایر جنگ‌ها از جمله جنگ روسیه و اوکراین به‌هم می‌خورد.
اگر دشمن بخواهد سطح تنش نظامی را کاهش دهد چه باید کرد؟
🔸
هر توافقی برای پایان جنگ باید مسئلۀ توازن قدرت منطقه‌ای را در نظر بگیرد.
🔸
ایران طبق فتوای رهبر شهید انقلاب، به‌سمت سلاح اتمی نرفته اما رژیم صهیونیستی سلاح اتمی دارد؛ در چنین شرایطی خلع سلاح اتمی رژیم صهیونیستی باید به‌عنوان پیش‌شرط هر توافقی برای پایان جنگ از سوی ایران مطرح شود.
🖼
اما چرا این پیش‌شرط باید مطرح شود؟
در
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/456422" target="_blank">📅 19:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456420">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgUjnmEh2WmfKlB7dWoji2UZHQTQFg8sMZBuNKIIg8G4l1K1d7zekMo_lzcaXy-Tw6sTH6nc6p9vg1vLGVMZArd4Z_8CFTrLym0FDY28_heE7eRpyl6h8B_W-JDWOk9t8Wu-KBkmwQgS6sUfM_1AYFq8MQm76zQg83htiMurbI1KcitMMmSqQZ_xxEOsj2jmWQfw6k8vPVSD0Y9JxKqMdbaKXWDAVlWwlL8GkJA05dkk03-uB7CXyM1hdt_TeVBzI1u6OfBQUT-yuPhdBc6R0z742oWVraWvyijgQMX7TP07rdu-nqQnrCedLp1Yk-HpWG2iG2v34B3f3sGGokZiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگری که به مقدسات توهین کرده بود  دستگیر شد
🔹
قوه‌قضائیه: درپی انتشار ویدیویی توهین‌آمیز در فضای مجازی از سوی یک زن بلاگر، با دستور مقام قضایی متهم شناسایی و دستگیر شد.
🔹
برای این فرد پروندۀ قضایی تشکیل شده و درحال رسیدگی است.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/456420" target="_blank">📅 19:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456419">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZjYjY3jaIwZXN7g8sOtTNZ9lE8VV1k1X-r9JFgx8a0qEGNxl8B4nuhwzvdjc-Je-4EjFkT08ncpNcwvZkhR-uCR_0CktHsbLHYGkoj5K7xT85Z8YEHxp_ntMB1Kc3FRTwNDt50mxqwJvfvAHnD3q1E41CGnEt4LrOs7TvIIgYlSgfimq3AlUg53uprgbFZgE9ZCH0H6a0BWXsdIAI8fRB1toVNQ2TtVTXXGLkwzmN2PKnMDv13PNzpfmQ6a_Qi2yt5td82CQDMarMgwarKNm-lq-x9WIw0dgMm1hcMUOEpISDHqL-oFaAwW5FtRAbe5o-vVTlKdYbzi1z8hD4Djvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ حزب‌الله: با اسرائیل تنها زبان مقاومت کارساز است
🔹
نمایندهٔ حزب الله در پارلمان لبنان: دست از مذاکرات بی‌حاصل با دشمنی بردارید که چیز جز ننگ و عاری در پی نداشته است؛ با این دشمن جز زبان مقاومت کارساز نیست.
🔹
سرخوردگی و ناکامی کامل از آنِ کسانی است که با اتکا بر آمریکا مسیر سازش و مذاکرات مستقیم را برگزیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/456419" target="_blank">📅 19:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456418">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زمان‌بندی وزارت رفاه کالابرگ مردادماهِ ۳ گروه را حذف کرد
🔹
معاون امور اقتصادی وزارت رفاه: از مرداد ترتیب زمانی شارژ کالابرگ تغییر کرده است؛ گروه اول پانزدهم، گروه دوم بیست‌و‌پنجم و گروه سوم پنجم ماه بعد می‌توانند یارانۀ غیرنقدی خود را استفاده کنند.
🔹
این درحالی است که پیشتر این گروه بیست‌و‌پنجم هر ماه کالابرگ خود را دریافت می‌کردند.
🔹
با زمان‌بندی جدید عملا سرپرستان خانواری که رقم آخر کد ملی آن‌ها ۷، ۸ و ۹ است، کالابرگ مردادماه خود را دریافت نمی‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/456418" target="_blank">📅 19:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456417">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bab0f44de.mp4?token=tyW2kDUdRW2Clr4Dqv3q1jvFOtgrbX-Eh1r7FUANRFIOX9zf96rzKty66FyBarg9YqSlFZV0jcK_0hWfAxDodkbEBEHF1LyljeZvWfB39KfgRwMhPg_ecRM-gqf6wW3F5_Hvhp4vqU78N7j4TJyCnG4TO_NT7Wb7WWztY_H3wxDNk3nnawrmmJDB5MjVrYFVcXbmgDdNBmTRZVHY0EbW6aENNcmHOr2cmHIJBvx8qrHuJlX-xJPmBX4dBKxqN1GVbUzkH-IvGBT19fuTySBbD1F5Da4xRblgWej9mgB-i0Rxe4BsgRvJvWFddPozDrlFnNp-fCwzQr_9AFEgrWAkow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bab0f44de.mp4?token=tyW2kDUdRW2Clr4Dqv3q1jvFOtgrbX-Eh1r7FUANRFIOX9zf96rzKty66FyBarg9YqSlFZV0jcK_0hWfAxDodkbEBEHF1LyljeZvWfB39KfgRwMhPg_ecRM-gqf6wW3F5_Hvhp4vqU78N7j4TJyCnG4TO_NT7Wb7WWztY_H3wxDNk3nnawrmmJDB5MjVrYFVcXbmgDdNBmTRZVHY0EbW6aENNcmHOr2cmHIJBvx8qrHuJlX-xJPmBX4dBKxqN1GVbUzkH-IvGBT19fuTySBbD1F5Da4xRblgWej9mgB-i0Rxe4BsgRvJvWFddPozDrlFnNp-fCwzQr_9AFEgrWAkow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرهایی که اینترنشنال بی‌صدا حذف‌شان می‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/456417" target="_blank">📅 19:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456416">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ebb0004f7.mp4?token=AXmoV4r4YB9SaTyR2DAYEBE8FnSoz5TFLuDVtnS6y4-7Pe8hh6dERWkZKffnruWmYZ70Q5sI7gklBO-MpqA138vXvbRfJhZLEgK7CV1GmdR0X0CFg9yk3Yu4Eeub4_IK7_LeJZ_MM_OXwTFVf5FYnfvjVLWMbDM5GHByYuzYXG-k2LRcxk4e1aT3ofSIIrWxtYBaZ5DSTlOQ1Yu8ZOrWWt2yVd9-LhLTgL2AMRkWui1jNTg4VDuyQNByk5sgJVbIe8PO9n7fYDUsabg1bJbVvLK5dcBEHX9IQn7lSGzln415V-gJMFvEizTo_1wHDSV8ovUWMkh3Y-3IznjDzqskoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ebb0004f7.mp4?token=AXmoV4r4YB9SaTyR2DAYEBE8FnSoz5TFLuDVtnS6y4-7Pe8hh6dERWkZKffnruWmYZ70Q5sI7gklBO-MpqA138vXvbRfJhZLEgK7CV1GmdR0X0CFg9yk3Yu4Eeub4_IK7_LeJZ_MM_OXwTFVf5FYnfvjVLWMbDM5GHByYuzYXG-k2LRcxk4e1aT3ofSIIrWxtYBaZ5DSTlOQ1Yu8ZOrWWt2yVd9-LhLTgL2AMRkWui1jNTg4VDuyQNByk5sgJVbIe8PO9n7fYDUsabg1bJbVvLK5dcBEHX9IQn7lSGzln415V-gJMFvEizTo_1wHDSV8ovUWMkh3Y-3IznjDzqskoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنگ ورزش به همایش آموزش‌وپرورش رسید
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/456416" target="_blank">📅 18:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456415">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_whVHsdYRRz3DS0OPh9PzFp_PRMpQlYTmD7ZwB0L4pLMz5OS88nwFo-ikda0ekEBZVUIQRYro5uKKJrMc43VaYSchtIFwGMwR-EbuF2Rrbdy-HDmJi32fp81J9hdbcRWPagzOcc-FwkuGlLJQM-HiV69eK8E-am5_m8Rd8pk2EpHE_nircB9iQ-daQhCSltoTBLjsUmpEn7JGG-dJZT445BXrCZzhe_t9z-tABAb2EObZBwnkNaCnXJ2SSMhcIqtEglYpThxLGU_fAxbKDRKGRK33tW2YI1eFlrZpWLs7fynEWe_4WI_tbl9CmSrByzF78pZXdE508y0BDHp6Tgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌خبری از ۹ صیاد بندرلنگه‌ای پس از پنج روز
🔹
فرماندار بندرلنگه: ۹ صیاد بندرلنگه‌ای که پنج روز پیش با ۳ قایق جداگانه از اسکله بندرکنگ و اسکله گشه راهی دریا شده‌اند، تاکنون به خانه بازنگشته‌اند.
🔹
احتمال تمام شدن سوخت، نقص فنی شناور و یا گرفتار شدن در شرایط نامساعد دریا برای این صیادان وجود دارد.
🔹
تاکنون اطلاعی از وضعیت آنها در دست نیست و جستجوی دریایی برای یافتن این صیادان نیز نتیجه‌ای نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/456415" target="_blank">📅 18:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456414">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هر ۲ مسیر تونل توحید امشب مسدود است
🔹
با توجه به انجام عملیات تعمیر، نگهداری و کالیبراسیون تجهیزات تونل توحید، هر ۲ مسیر این تونل از ساعت ۲۴ تا ۵ صبح روز بعد، مسدود است.
@Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/456414" target="_blank">📅 18:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456413">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۶ میلیون نفر برای مطالبۀ خسارت‌های جنگ به قوه‌قضائیه وکالت دادند
🔹
مرکز وکلای قوه‌قضائیه: تاکنون وکالت بیش‌از ۶ میلیون نفر با درخواست‌های مختلفی مانند خسارات مادی و معنوی جنگ به صورت موضوع محور ثبت شده‌است.
🔹
بسیاری از مردم با وجود اینکه عزیزترین افراد خانواده خود را از دست داده‌اند، مطالبۀ شخصی ندارند اما خون‌خواهی امام و شهدا را مطالبه می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/456413" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456412">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqpaNGk679_UYDwWATBDdiM3usUjyUlFuIr54dIjl73CchdF7km5adT7C7D0jBvbNTnY5YNhXxDtZLLuXl8V9ppRE2Mp9Cye7cDYfef_vQgKURhzjdy_d9tv79X4DCTqcfUycTMWLx89h7rQU-vA_ngbsn3Yq020KTqbOVDYpc_ZmjQ-4mYLz7Yt3BZ23jb3-0tkbTLi30O63HvHLTUJG6oIc0R-ssHn8hvslRA7gFnoUUBNznQsE2tyODqpLYEUa5I1H7onEzYr6pxDP2WabUDCR-b1wUJTsgLC3lqC644en0M77IBQajEqMj4ZNZjh5hZ1jWTgbvGzcV-ds3JmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: هر تهدیدی در برابر سد دفاعی ایمان و تخصص ما بی‌اثر خواهد بود
🔹
بیانیه‌ ارتش ایران به مناسبت سالروز بازگشت آزادگان به میهن: بازگشت آزادگان، نقطه تلاقی صبر استراتژیک، ایمان تزلزل‌ناپذیر و پیروزی مطلق اراده بر زنجیرهای اسارت است.
🔹
بازگشت آزادگان نه یک بازگشت جسمانی، بلکه تجلی اراده تسلیم‌ناپذیر در خاک پاک ایران بود؛ رزمندگانی که در سخت‌ترین شرایط اسارت، مفهوم پایداری را باز تعریف و به جهان ثابت کردند که لباس نظامی، حتی در غیاب سلاح، زرهی از عزت و وقار است.
🔹
امروز، ارتش جمهوری اسلامی ایران با تکیه بر میراث شهدای راه حق و تجارب گرانبهای پیشکسوتان و آزادگان سرافراز به جایگاهی از اقتدار رسیده است که هر تهدیدی در برابر سد دفاعی ایمان و تخصص بی‌اثر خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/456412" target="_blank">📅 18:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456411">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riWsDQuJbY43wU8QsQf4xDJeBEkLjj8AQK25Kje4iW2s9CbBVCOR2IhvLuNN8vDRm_Wbe3TxOaAI8qqCwNyUl4k_G3sdFSCR66w2-_UV-OZKMIWAc7BJZIzOPtPX2I9Q1Dyep7fHg6gVSTkF9joVOFXcxWoMAtYxBtQqpbijoKTM3E4w0BB5lt6rZGwJKYKgAQ9PbTQs10BunmbcN-WL-GssMZqzm4yn0Ml_zk_2GvntQBs1q2SoJqBThrX_cdLpAOvv3a2MXG-EV31bvX9p4cz67HrMAdR2cU9pCy4VAzV8Qb5nWbgsqe0wfX3H0unjtz8WRCfoP7_d72OKf1G7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/456411" target="_blank">📅 18:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456410">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1d1277df.mp4?token=qI2eJ1BgDwYPzd51RM8o5E7STKZcckDg-mxAQ38txautMuxFuSkFvK6xIHnlFZBPdRhxqwoyxROkZVwCb66qVuItiqHLpesySX6rswIK0_QcWWSzK5HxbtBUolkIgLb07yl-lgEd9eC2WuFKXn2Gt7LHZhCD1W8lFbnSqj0EdRfJnjOgNqQVq2ican9uoe8dIRQkAuz-RU3D91-Zg75DSJEE6-wvjVRq4zs67vOiRoi9Y_3g_VoCDkFdmSwV47bHfEAEqd7HPtEfSCCb6zIv0udBfIWd63C_v1JaXTDxohflVJ3s1qEWmyndAzvubXJON-6oDAs875A2HI4uwB76fzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1d1277df.mp4?token=qI2eJ1BgDwYPzd51RM8o5E7STKZcckDg-mxAQ38txautMuxFuSkFvK6xIHnlFZBPdRhxqwoyxROkZVwCb66qVuItiqHLpesySX6rswIK0_QcWWSzK5HxbtBUolkIgLb07yl-lgEd9eC2WuFKXn2Gt7LHZhCD1W8lFbnSqj0EdRfJnjOgNqQVq2ican9uoe8dIRQkAuz-RU3D91-Zg75DSJEE6-wvjVRq4zs67vOiRoi9Y_3g_VoCDkFdmSwV47bHfEAEqd7HPtEfSCCb6zIv0udBfIWd63C_v1JaXTDxohflVJ3s1qEWmyndAzvubXJON-6oDAs875A2HI4uwB76fzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس فتا: در خرید از آنلاین‌شاپ‌های غیرمجاز بیعانه ندهید
🔹
رئیس مرکز فوریت‌های پلیس فتا: خرید از آنلاین‌شاپ‌ها باید از طریق سایت‌های مجاز دارای نماد اعتماد الکترونیکی انجام شود.
🔹
شهروندان در صورت خرید از فروشگاه‌های فاقد سایت و نماد اعتماد، ابتدا کالا و اصالت آن را بررسی و سپس پرداخت کنند و از پرداخت بیعانه خودداری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/456410" target="_blank">📅 18:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456409">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcNqSnniDzkJHEMiA_GMsAA6MT7DnZT7L7kz8TBgP1fn_YAzELenWRdRf1H-YjJzDtbW5G-aRvCWJkCmpBob7NACc3ZOq1GHtoWHMfWMWSGqRGzMbuop9plutKssGd6vchqXramhuNBxqAooLFYlRrC3u40toOAxDXJ2bOsS8RLjGkeip6OuFbF0w4liZrptbP5IA_kZhdzbPi5HALAMKVNp5KnxAMwQaj9aO6kwc_GtnUEnQE74b83_hOVIK7xb33bdAIt4cy5d63H0iA0yq43KO73zbjrALYcMFsixyY3jUnVNAj74OTHZ25UQgAVRzDKw8GLjptAfO6W5ccOiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تلفات مزدوران سعودی در حملات ارتش یمن به مأرب و المخا
🔹
منبع نظامی یمن: حملات به مواضع دشمن سعودی با نهایت دقت، به اهداف خود اصابت کرده و در پی آن، چندین عنصر وابسته به عربستان کشته و زخمی شدند.
🔹
در جریان این حملات، چندین انبار مهمات و سلاح وابسته به عربستان…</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/456409" target="_blank">📅 18:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW-k8DtNRxz3zXNlYgM5mtLxaaZrJG2fXF_cNtrEWDbO5LBah2KtDlF2EBzOPPp9kyXBEjVCsWQRvDCnc6fSAPMXcNyzBr386V-1wzcdYBi2Nbx1B0rsqAQCbwFWZjUYveF5eAZBpuUawQ2BeCAt7YX2_Xx0bcA09eoVDHzqnfXAmHRxpAXW_1nUNI9e130uxgzBaOkyUKlxG03DtR0FBS5imgkgVx4EGMPTK-Cp69G03H0ACoc0R_1No6SsPzuMwrwISrJ6wK7dqp-lW9h63PPw-rJc4UCYwPH1VoldHSuLHT4o5cDJf9la11Wh3wDkkowY16b4S3K6RlRMQtUVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعام تصمیم گیرندهٔ نهایی دربارهٔ زمان برگزاری انتخابات شوراها
🔹
سخنگوی ستاد انتخابات: براساس مصوبهٔ شورای عالی امنیت ملی قرار بود انتخابات شوراهای کشور ۲ ماه پس از پایان رسمی جنگ، که این‌زمان هم توسط شورای عالی امنیت ملی اعلام می‌شود، برگزار شود.
🔹
بر همین اساس، جلسه‌ای بین ما و هیئت مرکزی نظارت بر انتخابات شوراها برگزار شد و توافق شد ۲۴ مهرماه زمان پیشنهادی برگزاری انتخابات باشد.
🔹
با توجه به این‌که مصوبهٔ شورای عالی امنیت ملی وجود دارد و در آن اعلام شده انتخابات ۶۰ روز پس از پایان جنگ برگزار شود، شورای عالی امنیت ملی باید دربارهٔ زمان برگزاری انتخابات اعلام نظر کند.
🔹
ما با شورای عالی امنیت ملی مکاتبه خواهیم کرد و اگر موافقت صورت گیرد، زمان دقیق و رسمی برگزاری انتخابات مشخص خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/456407" target="_blank">📅 17:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQXhd8Wtfgf9KfThpNB8qKouGthQDN_FwhYDWi_ILpP7mqQAdywkbOpkXICar0xZM7y1gRU0EZqpQ_IralhwH9VzmJtjdmXaxTws6urzINWcl7Yzh3xGXkC4mc15k-GeHvO2hsGVyJ8bOwf32WwiQtprSEqQDDeIqS1UijGgABK_geu6Ldosm_J4N5pyVp_7F22hZMO0W6rmC11Aywt-QkYszZJrJ0TsH8zDPoUcWvJi-btp13433hF5VaVesSrUs7YFl9Dk7a415rcdpRYi9_hm72O6fmcrhP4wxF2mKQnrwdPbj4xSVou_tMfqcE9DkaOvZSHPL-ElzG85uGV4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ ورزشی برای درمان بی‌خوابی و استرس
🔹
ورزش منظم فقط برای تناسب اندام نیست؛ بلکه می‌تواند با کاهش استرس و تنظیم ریتم شبانه‌روزی بدن، به خواب بهتر و آرامش بیشتر کمک کند.
فواید دیگری که فعالیت بدنی مداوم دارد:
🔹
کاهش خطر بیماری‌های قلبی
🔹
تقویت عضلات و استخوان‌ها
🔹
کمک به کنترل وزن
🔹
افزایش سطح انرژی روزانه
🔹
تقویت سیستم ایمنی
🔹
بهبود کیفیت خواب
🔹
کارشناسان تاکید دارند که تداوم در ورزش، هم بدن سالم‌تری می‌سازد و هم ذهن آرام‌تری و می‌تواند کیفیت زندگی را در بلندمدت ارتقا دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/456405" target="_blank">📅 17:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBNNpC8m8v0g8zQsZUZADPi80SjzBoICVvlcAkZL7kXvHR7x-wELGR8XH7gVI01tEXaP1U5ygY4uMcqzHa8G28I0pGTD5zZVsoJkrGo06PfLcqkx_jwfrFh7iohdNVgvY4Bdx8rqsZoCo13BQAwZynYhdPd98tSJRcFE7_h0GHNIYg9KqmHo8tLhnfwWqoCA4whU_liI3ySrzSkxvCn2Gvam7ZOEU64tfZq4gFnf6lQP7IE8oVpc4h_Cb1qa3bKj1EO78pykS4dR2DF65do_d5ZL-noHAvM-bEwFvU8epXT2X59a4tvhFL-_01uNTEcHm0mH7usrmv-ZuSnKXZ1zSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهمیه بنزین خودروهای مدل ۸۵ و قدیمی‌تر را قطع نکنید
🔹
با اجرای آیین‌نامه جدید، خودروهای تولید سال ۱۳۸۵ و قبل از آن فرسوده محسوب شده و ممکن است سهمیه بنزین یارانه‌ای آن‌ها حذف شود؛ در حالی که بسیاری از مالکان این خودروها توان خرید خودروی جدید را ندارند.
🔹
در همین راستا پویشی در فارس‌من ثبت شده و حامیان آن خواستار توقف اجرای این طرح تا زمان ارائه تسهیلات ارزان‌قیمت، وام‌های بلندمدت و مشوق‌های واقعی برای نوسازی خودروهای فرسوده هستند.
🔗
اگر شما هم با حذف سهمیه بنزین خودروهای مدل ۸۵ و قدیمی‌تر مخالفید،  برای حمایت از این پویش
اینجا
کلیک کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/456404" target="_blank">📅 17:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4f5e1810.mp4?token=iLrawGJl1eYm0vclYkbQCdup59tcyjmOx-CFmY_SEqjFd5u6zdjeRfgvzz2qxOaYu02IiNPwAWeQknl8j-0zqaF0qtMNg1wWlJr42uyp4vYREilRDrBjVLHlOniFaHNEJk5DWnsrYeY9IEb-HMKJeb9dRnKPulgFlQ7U3Sy08UXN7O6AoeU-LrBTsnN_GKFYAL4gMGstlU044dn_plF1iqTbUEMGx6BxWftmfGSUmAh8Tvdeg9V6AQBiADac54-ol3tj3_whm4Kdyte50_2rZws2QiZ0ir8hk_YaVSnFzM5OwDAlgAg-SA33_2Igx2cptvGYCAytccqCcoEk8RxukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4f5e1810.mp4?token=iLrawGJl1eYm0vclYkbQCdup59tcyjmOx-CFmY_SEqjFd5u6zdjeRfgvzz2qxOaYu02IiNPwAWeQknl8j-0zqaF0qtMNg1wWlJr42uyp4vYREilRDrBjVLHlOniFaHNEJk5DWnsrYeY9IEb-HMKJeb9dRnKPulgFlQ7U3Sy08UXN7O6AoeU-LrBTsnN_GKFYAL4gMGstlU044dn_plF1iqTbUEMGx6BxWftmfGSUmAh8Tvdeg9V6AQBiADac54-ol3tj3_whm4Kdyte50_2rZws2QiZ0ir8hk_YaVSnFzM5OwDAlgAg-SA33_2Igx2cptvGYCAytccqCcoEk8RxukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند سپاه: در حوزۀ پدافند هوایی حتی یک موشک، سلاح یا قطعه خارجی استفاده نکرده‌ایم و ایده، فناوری و تولید تجهیزات کاملاً بومی است.  @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/456403" target="_blank">📅 17:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGSoC6IBBRlARE98sF1htWVs5vNKJ-1ryMbKr2BWcoFeAHVotNQhNrjYu4L_rpDFl5652WYYzFFgFiIb9FWZcYkDlVsX4npBHAIFBROFGy4JqIFlW6jV3SO6EseVuJaPAFF-qAW6IJonBIIh9AXdA_KKVpBYB0N2677gTrOdSR-ePV7b1o2Di2I6sDhZ5qTcmhcddCX2xoMnUIVDJVUvZRcoJIGxY_IAtfJh_0J0pQGGMggcNqRIYZjLjNhM0E4S6WydcPUMoSHucmSC953MilFuFLwBjR71b700wggYRvkKHcPyqM4mnElwCssKfMFgboyLFuwo_piFxh3PmXR7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: اگر میزان مصرف بنزین خودروهای داخلی مشابه خودروهای روز دنیا بود الان شاهد ناترازی در تولید و مصرف بنزین نبودیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/456402" target="_blank">📅 16:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456401">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f607b9ca.mp4?token=gSIFAaf9BJjr9b86uznHKb0tOw3vmU8WvqDJN3fo0Iz3Ds1NrQLtUY4A1t8oX5rkyLiGEyjwyKp4FmNNdFDsUua9EunH5Ls9bcgTv_ZfinMQ5kiCdlXAxfzs508HtVEkV-rK4DkQtayeFlfLBUWhdmGCyphTb2cJ9XvCjUM_8EKkDRxfiB8aoDvctroiX8LQ303g8KHpfRarEWzzeKBlyP8TK-V6T8yUsWut-ufIJkUOgIJiOrpxvIVa7g4_i1rqBzQSOVXREZgKZW136aqnuiSY3zNkO1VKOMw0J-0vsOG7ikqdgbVoWWJ9u3-oBlXwv4QufGRIBxe_dU2tA_k3XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f607b9ca.mp4?token=gSIFAaf9BJjr9b86uznHKb0tOw3vmU8WvqDJN3fo0Iz3Ds1NrQLtUY4A1t8oX5rkyLiGEyjwyKp4FmNNdFDsUua9EunH5Ls9bcgTv_ZfinMQ5kiCdlXAxfzs508HtVEkV-rK4DkQtayeFlfLBUWhdmGCyphTb2cJ9XvCjUM_8EKkDRxfiB8aoDvctroiX8LQ303g8KHpfRarEWzzeKBlyP8TK-V6T8yUsWut-ufIJkUOgIJiOrpxvIVa7g4_i1rqBzQSOVXREZgKZW136aqnuiSY3zNkO1VKOMw0J-0vsOG7ikqdgbVoWWJ9u3-oBlXwv4QufGRIBxe_dU2tA_k3XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرلشکر حاتمی: توانمندی دفاعی جدید به ارتش اضافه شده
🔹
ظرفیت‌های آفندی و پدافندی ارتش به‌سرعت در حال بازسازی است و ما لحظه‌ای را از دست نداده و از فرصت‌ها حداکثر استفاده را کرده و می‌کنیم.
🔹
دشمنان با وضوح دربارۀ توانمندی ارتش دچار خطا بودند و به‌همین موضوع…</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/456401" target="_blank">📅 16:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456400">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
خبرگزاری رسمی عربستان: هشدارهای حملهٔ هوایی در جازان فعال شده است.  @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/456400" target="_blank">📅 16:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8013f9430a.mp4?token=BckzX1liWAws3v5MYIYUlhPkRVmbct9dVMb-7GfmVhLkDldRVXBccKEFieMZ7uNJBiv4UJfAMVkYYGP2qqGoVYaLlgJ5Vr4kPK4H-qn2FZJWJtCPlezADVwkc7XNAkYOzJAEYSJlTK_iYmlG5O3nBtl9Hl2ooC244N696IlcbHLozGPHAfa4GMJpyYmcVSIykCGA-v03wBYLnKA31togqTuffQpOC4HFGHg5uqudSkZNw-3BP4G3GftN77BN80uKtGIMdVc-Fx1gT6TpxQGIZEDJ8awePRTheaVvdhMP472usHh-mZcCDbI20zKjokE3cejX368-LkJ0NV1jKofsrgB58hdd-ustmgb2tZ4QHTKiyA0hP6j1xAmHQ6vMRvE2tdghmm2sMTZyLOIqDAL_2CRSCEc6w8S8QQDxtqlIcNa7XEeFG_fLbQv9_up2uZJeSlRsyf3H9lHsPcAL8oFRDOm2EN40KxszKe7WgaojymXIwDsWCZ1kNvqWSuVg3-HrE2a8zb9VrTar5l7eVUe2vbXoCxML5Dr3r9W14KVUCiEP-Mc55ycHKbShvOyQeJwP97UcUOJv3m3IRq8xaysO6Rxf6ri64RVzzqGfLrgsayPhGnoj73XYkoAHzD0BPlhiOsmhu_WgbnNnlkydU4mP94lvYlQXBfV22M_FRNTY2qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8013f9430a.mp4?token=BckzX1liWAws3v5MYIYUlhPkRVmbct9dVMb-7GfmVhLkDldRVXBccKEFieMZ7uNJBiv4UJfAMVkYYGP2qqGoVYaLlgJ5Vr4kPK4H-qn2FZJWJtCPlezADVwkc7XNAkYOzJAEYSJlTK_iYmlG5O3nBtl9Hl2ooC244N696IlcbHLozGPHAfa4GMJpyYmcVSIykCGA-v03wBYLnKA31togqTuffQpOC4HFGHg5uqudSkZNw-3BP4G3GftN77BN80uKtGIMdVc-Fx1gT6TpxQGIZEDJ8awePRTheaVvdhMP472usHh-mZcCDbI20zKjokE3cejX368-LkJ0NV1jKofsrgB58hdd-ustmgb2tZ4QHTKiyA0hP6j1xAmHQ6vMRvE2tdghmm2sMTZyLOIqDAL_2CRSCEc6w8S8QQDxtqlIcNa7XEeFG_fLbQv9_up2uZJeSlRsyf3H9lHsPcAL8oFRDOm2EN40KxszKe7WgaojymXIwDsWCZ1kNvqWSuVg3-HrE2a8zb9VrTar5l7eVUe2vbXoCxML5Dr3r9W14KVUCiEP-Mc55ycHKbShvOyQeJwP97UcUOJv3m3IRq8xaysO6Rxf6ri64RVzzqGfLrgsayPhGnoj73XYkoAHzD0BPlhiOsmhu_WgbnNnlkydU4mP94lvYlQXBfV22M_FRNTY2qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای محله‌تان را بی‌واسطه به مسئولان برسانید
🔹
خبرگزاری فارس استان تهران در طرحی ابتکاری، از دغدغه‌مندان و علاقه‌مندان به حوزه رسانه دعوت می‌کند تا مدیریت «صفحات اختصاصی محلات تهران» را در دست بگیرند.
🔹
اگر در زمینه‌های خبرنگاری، عکاسی خبری یا تدوین استعداد دارید، می‌توانید به عنوان خبرنگار بومی، پل ارتباطی مستقیم میان مردم و مسئولان باشید و مطالبات هم‌محله‌ای‌های خود را در رسانه پیگیری کنید.
🔹
برای ثبت نام در این طرح رو "
این فرم
" کلیک کنید.
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/456399" target="_blank">📅 16:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌ تلفات مزدوران سعودی در حملات ارتش یمن به مأرب و المخا
🔹
منبع نظامی یمن: حملات به مواضع دشمن سعودی با نهایت دقت، به اهداف خود اصابت کرده و در پی آن، چندین عنصر وابسته به عربستان کشته و زخمی شدند.
🔹
در جریان این حملات، چندین انبار مهمات و سلاح وابسته به عربستان…</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/456398" target="_blank">📅 16:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJTfcxsjdva8dCIJ-NQciuZopk9SShw-ZGTC3pi-WYFeOUXlBzF67-KkIRIef9TtQXlmveOg1GoGF0IhiveVaQDXtnlgeDVD3_7fNoILfK8--f85jOn_Gf_dRxqkTRB8ElDNEAsT00G_ehSeEHIui_fS0fMUdrSxIvPYqY3hoYlPWL-j_ofwKdUGKTnwh_PI8ZPjtf7MKsRzKY1tY0VCrpMICKv8ZblbX3DYvdbJhnBxvLis-rLsYO0Noip1P2BTwVxul1Byx5RxBLRS1oCDWRSrA8sr_2tC7xKkFWd612ff_Jq4EiPlKDanS7OWCUUXwRqywaW1xJmg4mWKABfnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: تصویر رئیس‌جمهور آمریکا، تصویر یک بازندۀ بزرگ است
🔹
رئیس‌جمهور متوهم آمریکا تلاش زیادی می‌کند که از خود تصویر برنده بسازد، اما امروز کمتر کسی در دنیا او را جدی می‌گیرد.
🔹
تصویر کسی که از ترس خود را در کامیون مواد غذایی پنهان می‌کند و دیگر اعضای…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/456397" target="_blank">📅 16:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUL9NNEJiZ08oq4ZyRv2haN4ZM7oDpuRbPYLnbx0HbIohEc8Ws6M4ESWTlFWL-xt7LmzquZNut2OR5ZeO1L7IAkmOl85Y5WLjRkyKwra_E8d_Hut1DifeqkwjK977_yS_5ApB2fHN0c7ww-cBRINeFg_Wf4p2k9a9kH1ag1Ai2_gV05QsH-c1k2XFDkZt95XCVwT5Ld8fbYEUJ54NKHSSJ22IB8hr_kxBOY7wY5jndxb4hKGSFvwvkPjNYX0XrZ6FV_NTsfz4nLyA7R4wacqisZPe8cusMupxs26Ue56EhO-zPTlA-ufDdlvMrdCICrJKlgkJPZdvXhiuAqUSmjf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزهٔ ۵ میلیاردی‌ برای شکارچیان سربازان آمریکایی
🔹
فرمانده‌کل ارتش: با مشارکت مردم، اگر هر نیروی ایرانی بتواند یک نیروی آمریکایی متجاوز‌ را دستگیر کند یا بکشد، ‏از طرف مردم ایران جایزهٔ ۵ میلیارد تومانی‌ دریافت خواهد کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/456396" target="_blank">📅 16:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تداوم حملات موشکی و پهپادی یمن به محل تجمع مزدوران عربستان
🔹
خبرگزاری رسمی یمن امروز به نقل از یک منبع نظامی خبر داد نیروهای مسلح این کشور باز هم خسارات سنگینی به مزدوران عربستان سعودی وارد کردند.
🔹
این منبع می‌گوید نیروهای مسلح یمن در جریان حملات پهپادی و…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/456395" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تداوم حملات موشکی و پهپادی یمن به محل تجمع مزدوران عربستان
🔹
خبرگزاری رسمی یمن امروز به نقل از یک منبع نظامی خبر داد نیروهای مسلح این کشور باز هم خسارات سنگینی به مزدوران عربستان سعودی وارد کردند.
🔹
این منبع می‌گوید نیروهای مسلح یمن در جریان حملات پهپادی و موشکی، محل تجمع مزدوران سعودی را در منطقه المخا و استان مأرب هدف قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456394" target="_blank">📅 15:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456393">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌ شورای مرکزی انضباطی وزارت علوم حکم اخراج رضا دالمن دانشجوی اخراجی دانشگاه شریف را تأیید کرد
🔹
یک منبع آگاه در دانشگاه شریف: حکم اخراج این دانشجو به‌زودی ابلاغ خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/456393" target="_blank">📅 15:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456392">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e548a823a1.mp4?token=mDPVchFCrU1tycCr7196jT1ciLXFHV4dYnKTtmJRT6o98nS_Drdthw3H2eNEAR54bz5mh4AbT7T6fJFe0Rfk8sIVEmVxR7fcjgyjPP8_cG0Tsf5tKZJ0z2B3uM68iq5EsYnahsPKU_Xbr1OZ1oPOTuVROzLlJEmMraM5nksNu5LEkaQJbrHQgmUgNfELXiH_Jj4L8bKhl1t5ZGoZd5N5ajqlgj_OewHNdK2zJ05RDEii8YQqkHqjqazHa0FHC6rgQug85VvdahIVOivPiB4Bm6u321KsmlrUq9C0-jiw4EfA_AlMT7FGM4B6aoj8Faf036HmCrAfvv0makMfBM5D7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e548a823a1.mp4?token=mDPVchFCrU1tycCr7196jT1ciLXFHV4dYnKTtmJRT6o98nS_Drdthw3H2eNEAR54bz5mh4AbT7T6fJFe0Rfk8sIVEmVxR7fcjgyjPP8_cG0Tsf5tKZJ0z2B3uM68iq5EsYnahsPKU_Xbr1OZ1oPOTuVROzLlJEmMraM5nksNu5LEkaQJbrHQgmUgNfELXiH_Jj4L8bKhl1t5ZGoZd5N5ajqlgj_OewHNdK2zJ05RDEii8YQqkHqjqazHa0FHC6rgQug85VvdahIVOivPiB4Bm6u321KsmlrUq9C0-jiw4EfA_AlMT7FGM4B6aoj8Faf036HmCrAfvv0makMfBM5D7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌بابایی: به‌عنوان یک مسئول خجالت‌زدۀ بازنشستگان هستم
🔹
نایب‌رئیس مجلس: برخی مدیران با گران‌سازی به‌دنبال عقب‌نشینی ایران مقابل آمریکا هستند.
🔹
در شرایط کنونی باید تمام پروژه‌ها و منابع کشور را با اولویت تأمین معیشت مردم تنظیم کنیم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/456392" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌ رهبر انقلاب ۶ فرمانده عالی‌رتبه را منصوب کردند
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های ۶ تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
🔹
براساس این احکام، سردار سرلشکر…</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/456391" target="_blank">📅 15:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456390">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
تعویق انتخابات شوراها با مصوبۀ شورای‌عالی امنیت ملی
🔹
رئیس ستاد انتخابات کشور: با مصوبۀ شورای‌عالی امنیت ملی و درپی شرایط جنگی، انتخابات شوراها و انتخابات میان‌دوره‌ای مجلس و خبرگان به تعویق افتاد و زمان جدید برگزاری آن پس از اعلام پایان جنگ تعیین و اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456390" target="_blank">📅 15:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456389">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در خمین
🔹
به‌دلیل خنثی‌سازی مهمات عمل‌نکرده در خمین طی ساعات آینده احتمال شنیده‌شدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456389" target="_blank">📅 15:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456388">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0207f5fead.mp4?token=PilM7eqvY8Z0Cid-NfSQCbZOob8Ocbe6I1KK24t85XxWDME3naYjx6moKMpx8vFARLTkgiNhADv9zj2dC61QWo9uINTqb25F5tn2F0be4Ea-9N2vTyLOxdYR_dSCTZpuZw1pGo00hi9uglG1DNe-Q3s6IdWdvaB_vKCYtcQRN9_JTpavUOT3292J_XHCKziWYmLyvcU4_zO6ygMxl98cCtepMCGDZFJqERTByx6QKi0m3FkFFKawj6iyu9XxicwYTxgjELWS3bbYY4L3irgcUf4xCQQq3qrpQmDP7c2Ht_o2oCo1fQ4YfdO1qtO64izRhtDD2URXKgBplfv8uG6CRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0207f5fead.mp4?token=PilM7eqvY8Z0Cid-NfSQCbZOob8Ocbe6I1KK24t85XxWDME3naYjx6moKMpx8vFARLTkgiNhADv9zj2dC61QWo9uINTqb25F5tn2F0be4Ea-9N2vTyLOxdYR_dSCTZpuZw1pGo00hi9uglG1DNe-Q3s6IdWdvaB_vKCYtcQRN9_JTpavUOT3292J_XHCKziWYmLyvcU4_zO6ygMxl98cCtepMCGDZFJqERTByx6QKi0m3FkFFKawj6iyu9XxicwYTxgjELWS3bbYY4L3irgcUf4xCQQq3qrpQmDP7c2Ht_o2oCo1fQ4YfdO1qtO64izRhtDD2URXKgBplfv8uG6CRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رانندۀ خودروی مرگ به آخر خط رسید
🔹
اولین تصاویر از جانیِ بی‌رحم چهارراه گلزار کرج؛ عامل جنایتی کم‌سابقه که فضای مجازی را در بهت فرو برد!  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/456388" target="_blank">📅 14:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456387">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFWzpuCedKFMfhryv6AWJCUysIYROtBws5Jbze5vSiVIZd5g9GwrV_vv_yf0MjFhbP-mxPMngOJo3BXjyX-mhrAtrTFOUyGcE4sjJ4WAPqZT4qj9fhz1rFOq4IKqo0V9RDVthl_bdsSGw9zsKxa8xcKl6IIEIlKw-lu8So21EfV7w6YHIwPd5e0-ig6lgf_1y2upd0jVAYhelZYhcdi4dB_loiM2C3Ar4o2ACJ1tBeSBWCAicXS6zbsfgcHp8ThBL1nw14Tk3ZvvKHw6BxzuOS7eCObXGBf2p7PkD5m92drQMHDNulqXSJefzEg8DXUkDQObycVZJT6qG9Td8a-NEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تقدیر فرمانده کل سپاه از ۶ ماه جهاد رزمندگان اسلام
🔹
شما در گرمای سوزان جنوب، سرمای ارتفاعات شمال و زیر آتش سنگین دشمن با عملیات موفق آفندی و پدافندی، مسلح‌ترین ارتش تاریخ جهان را به زانو درآوردید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456387" target="_blank">📅 14:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456386">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uds4FCQt6tJwwJ2vs22lv2PKHpILigKU-2jEDhLf9h_RzFWGJl9YZ5iQgpdbHBMT8-_PmGjpZGImiCZSEkwW-ciPm0WvEG2AjbDkQkvqnWP3T4xLjEKcFGVlwwN2cYnJ7RSoqwrRTwk5cVeWgU912CYEY9hFQV2zJ8jlrPAY76PC54B0RxTsAbCtOMMDIb0kxOEb9inKMe6EB9TFxhojT6K16OsSW3SzR9kzx3qHcgE3wQbGa00J8UtWzpXftx0lcVFKV7bV33UmRzINccBzrSGWDiA49oGiOvkPIi9XFmhaL_9pCNT8A_To9D5yFtZUm2XPMv5cMG-9n7nX-wdAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چراغ فرودگاه قشم دوباره روشن شد
🔹
فرودگاه بین‌المللی قشم: پس‌از وقفهٔ ایجادشده درپی شرایط موجود، از چهارشنبه پروازها آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456386" target="_blank">📅 14:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456385">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XydYAd81QwtC1WSb2yVoKSp7kG61dSQZT9eu2b4FwWQ0VJeZrLOqgMN7TBzGvPKNR7J1ETC0I1c1s2eDbaAvNeCVcdoN4_evT9FPpzOG8s2s_BrlpJlnHlogpl94eChnY573ku2h933I-WXCHHuew7-kK36Uv-OU7Pb3NLsbGrYfIC6j7e-jJNTcPjC02z-t11PLgrxh7SaFgyKyc5Wxfy5Wqg37RV5NHgnNU6iyY6y3U37qvhOSu3HPEO57PSJp-GSERT2bBVm3PUcKpj7Qrd9UhfA4EC_1Pqo_B9m3zPorgwJhOS4jCHs7SKbG3M4bmtPsJbgNZern36MbOJlJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزهٔ ۵ میلیاردی‌ برای شکارچیان سربازان آمریکایی
🔹
فرمانده‌کل ارتش: با مشارکت مردم، اگر هر نیروی ایرانی بتواند یک نیروی آمریکایی متجاوز‌ را دستگیر کند یا بکشد، ‏از طرف مردم ایران جایزهٔ ۵ میلیارد تومانی‌ دریافت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456385" target="_blank">📅 14:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حکم قاچاقچیان ۱۰۷ میلیون دلاری صادر شد
🔹
دادگستری آذربایجان‌غربی: حکم قطعی قاچاق سازمان‌یافته ارز به‌ارزش ۱۰۷ میلیون دلار و یک میلیون و ۱۰۰ هزار یورو در دادگاه تجدیدنظر استان صادر شد.
🔹
در این راستا ۳ متهم به به‌نام‌های حمزه کردستانی، محمدامین کردستانی و مصطفی کردستانی که با اسناد صوری و ساختگی از بانک مرکزی ارز را اخذ و در بازار آزاد می‌فروختند، دستگیر و به ۲۵۰۰ میلیارد تومان جزای نقدی‌، حبس و شلاق محکوم شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456384" target="_blank">📅 14:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456383">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e11c685a.mp4?token=BS0KlOBGb-Hgq9UXXtjfuygJm1goWY6iuzE_CP78oIxKyfFVeNhGF3Eh-UBppsmziN0PRa3-3MTlpRaKCXfUUztGUQUebKguOUfDMxvFqzSsVVDAoQQHsoPHyKNHWn3ygIZidCVXNcSlCd1ct8jzTlXzfw4I3M2dQhd1nsLUNSjqqtwJYp05_fSc45HxCJVudPGbAVbUyhAtbC7u1SzDpp_h4crIKW03etMI0F6jBGp1bBntIxS-mtQX7ILT7iLqZQwHmUJdVyYt6JexfNDpnH5rmhN2zgnydwfjhaWHryBNJwUSbR7zsdYjhlAUWhM2fvXum6eFb1YB-uU0QFhdug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e11c685a.mp4?token=BS0KlOBGb-Hgq9UXXtjfuygJm1goWY6iuzE_CP78oIxKyfFVeNhGF3Eh-UBppsmziN0PRa3-3MTlpRaKCXfUUztGUQUebKguOUfDMxvFqzSsVVDAoQQHsoPHyKNHWn3ygIZidCVXNcSlCd1ct8jzTlXzfw4I3M2dQhd1nsLUNSjqqtwJYp05_fSc45HxCJVudPGbAVbUyhAtbC7u1SzDpp_h4crIKW03etMI0F6jBGp1bBntIxS-mtQX7ILT7iLqZQwHmUJdVyYt6JexfNDpnH5rmhN2zgnydwfjhaWHryBNJwUSbR7zsdYjhlAUWhM2fvXum6eFb1YB-uU0QFhdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوال جالب از رئیس‌جمهور: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456383" target="_blank">📅 14:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456382">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b1f639be.mp4?token=lLJtDW_pDPwBe3fvJhpl_1Wt5DmQicLNNIbjSdsvCZ_K_fnxvUK3KCliwymf1quwwdoMSZeGUhqaNJcgrcE_behoPcWldQdP52hsnuDenX0rdMuXljfhiw5DIjKLPCeBqHwFNXrFZR15qLmH0R1MGxmLXh6ApfLkJB6GAl_eerydNBeZXmeSX2uSnWknoH_kmbPEh8JQUWGHbRpApIuKyU3jbjmScjTBM-3pSDV7EA7EDh8k55NuNK7TltH0e7y31xb1YhVKDHwDpt6qtFz_lZ7U8-ZKARFWD0eECXyafzN6J7iKIj6W8Se7kPXLQ-K8sSFX0acFiJKkSo2f7-8iVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b1f639be.mp4?token=lLJtDW_pDPwBe3fvJhpl_1Wt5DmQicLNNIbjSdsvCZ_K_fnxvUK3KCliwymf1quwwdoMSZeGUhqaNJcgrcE_behoPcWldQdP52hsnuDenX0rdMuXljfhiw5DIjKLPCeBqHwFNXrFZR15qLmH0R1MGxmLXh6ApfLkJB6GAl_eerydNBeZXmeSX2uSnWknoH_kmbPEh8JQUWGHbRpApIuKyU3jbjmScjTBM-3pSDV7EA7EDh8k55NuNK7TltH0e7y31xb1YhVKDHwDpt6qtFz_lZ7U8-ZKARFWD0eECXyafzN6J7iKIj6W8Se7kPXLQ-K8sSFX0acFiJKkSo2f7-8iVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوال جالب از رئیس‌جمهور: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456382" target="_blank">📅 14:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456381">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انهدام شبکهٔ انتقال اطلاعات طبقه‌بندی‌شده به دشمن
🔹
پلیس اطلاعات فرماندهی انتظامی تهران بزرگ اعلام کرد شبکه‌ای که با سوءاستفاده از تجهیزات ماهواره‌ای «استارلینک» بستر ارتباطی غیرمجاز و انتقال اطلاعات طبقه‌بندی‌شده ایجاد کرده بود را شناسایی و جمع‌آوری کرده و متهم اصلی دستگیر شده است.
🔹
متهم اصلی این پرونده با هدف سودجویی کلان، این شبکهٔ غیرمجاز را راه‌اندازی کرده و علاوه بر ارائهٔ خدمات غیرقانونی به افراد خاص، بستر انتقال محتوای مجرمانه و ضدامنیتی را فراهم آورده بود.
🔹
در بررسی‌های اولیه مشخص شد که فعالیت‌های این شبکه علاوه بر تخلفات حوزهٔ ارتباطات، مستقیماً امنیت را هدف قرار داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456381" target="_blank">📅 14:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456380">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daKnWTZODKym_EoDaVyqtk9u2Jd_84_0cRM2UlGHuxk-jOxZ5zaN1s2ManNy_rYJwvFgPk7ZPPW1zFA4PtbpmOejIT-wf7jG5ep7w7Lbr5t0E_rPn9-E6RYpCjZ_hjXKwNYv19R3cnNpD9sEx11DMpr-vCY5SvDmqSr3PvE-P-qccYLlVr2A43WFw6zRl3IzJ2wbmORu_vvCcescqHICML-7UD_XiVoYqIJgR24yu8vsxfkoalNs7tougUjcPoSLaCptaVgS17lz-eSBQkzyb1NRZLQ1dp9FlJOJc8eIw1cxUH7u22cnYrxCoD0nH5VCablGNVdE-xAGtEDIcFE0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
🔹
آمریکا و اسرائیل با ۹ هدف مشخص به ما حمله کردند اما به هیچ‌کدام از اهداف خود در هیچ سطحی دسترسی پیدا نکردند، این بزرگ‌ترین پیروزی بزرگی برای ما بود.
🔹
امروز ما در یک جنگ ناجوانمردانه‌ هستیم که در رأس آن آمریکا و رژیم صهیونیستی قرار دارند، اما ملت ما شجاعانه، مردانه و خالصانه ایستاد و جنگید.
🔹
بنده به‌عنوان برادری که به جزئیات کار آشنا هستم با همۀ وجودم می‌گویم که ما در این جنگ هم در بعد نظامی و هم بعد سیاسی به معنای واقعی پیروز شدیم.
🔹
تفاهم‌نامۀ بین ایران و آمریکا سند افتخار و پیروزی در راستای تثبیت پیروزی در میدان دیپلماسی است.
🔹
البته معتقدم که مردم ما حس این پیروزی را به گونه‌ای که اتفاق افتاده، حس نکردند و در برخی موارد نتوانستیم این حقی که مردم داشتند را به درستی ادا کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456380" target="_blank">📅 13:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456379">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3dYg_aTdUpcP9N0Pn786c8JYCWZkTbfAIsHYQPTMe4ULzXDIgVg5tMPO6i-j21btS2xV0UaHdW3zk_jopjDg8HVxjlHmNUQix_C-kSfSSJX10pqAPQk7xeMrJ2NWVzklqXQ-jEzB6dfr1FWG9SzbdLmnRSUfRchPZIqlyBsHcSMAt-IagtnQFt8qtpcxoU7eGLkoyvBf_3kYXBy5rgSUxMXjbHoGbMcOcU_sNlsTTIw4gSoRwxPR3WeS5DFQbGtaq-qQuqmFDqqj2iIPUFywpYwm7JHK3rlDUmkhTdoWtQSYTaMeQeismZl7TH1LfD1oTpBOTpr9WVd31XkSqcvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ترامپ به بازگشت به نقطه قبل از جنگ راضی شده است
🔹
یکی از بزرگ‌ترین مشکلات دولت ترامپ برای خارج کردن آمریکا از جنگ با ایران به تحلیل سی‌ان‌ان، فهرست اهداف بسیار مطلق و حداکثری‌ بود که او و تیمش در ابتدای جنگ تعیین کردند اما با ادامه‌دار شدن جنگ که اکنون وارد ششمین ماه خود شده، فهرست اهداف شامل تسلیم ایران و تغییر رژیم به شکلی محسوس تغییر کرده و محدودتر شده است.
🔹
طبق این تحلیل، «به نظر می‌رسد معاون ترامپ جی‌دی ونس هم اخیراً به شکلی قابل‌توجه از دامنه این اهداف کاسته است؛ موضوعی که تازه‌ترین نشانه از آن است که دولت ترامپ ممکن است خود را برای رضایت دادن به دستاوردی کمتر و شاید بسیار کمتر آماده کند».
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456379" target="_blank">📅 13:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456378">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c0d2f05e.mp4?token=cyJ5wWBT8V3p7qWbiNkV0BziNk0s1OnFkvyc3GNMySAqer0lJEBIn-sGQ8w9zQ8OlVrz9WGpPiNuijFrSHeoDlEf2gAtBQ3I8mwPLBTrJcKQPWFMP0Da-c_Uu3-rSJqL9eS9l43YrXPfrK60pKrNXJACBbgDeHcyPWAGBqmdNMOxjBDZ9cwqgvedmO91AJeeHgzMabHB0-5Es9eQyfhL-KVvBO4zI1gPLRRq1cgLczI6SRO5tNJlUeB0NuDKUatR_UCDtsWeGPmXqr84vtEqGdymUw8s7rlcu8SHdSLec8A0Lw9S91YEgHyJ-ex1-Wy_ZkEO82-Dx16EcnHU-XBZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c0d2f05e.mp4?token=cyJ5wWBT8V3p7qWbiNkV0BziNk0s1OnFkvyc3GNMySAqer0lJEBIn-sGQ8w9zQ8OlVrz9WGpPiNuijFrSHeoDlEf2gAtBQ3I8mwPLBTrJcKQPWFMP0Da-c_Uu3-rSJqL9eS9l43YrXPfrK60pKrNXJACBbgDeHcyPWAGBqmdNMOxjBDZ9cwqgvedmO91AJeeHgzMabHB0-5Es9eQyfhL-KVvBO4zI1gPLRRq1cgLczI6SRO5tNJlUeB0NuDKUatR_UCDtsWeGPmXqr84vtEqGdymUw8s7rlcu8SHdSLec8A0Lw9S91YEgHyJ-ex1-Wy_ZkEO82-Dx16EcnHU-XBZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آفتابی‌شدن ۲ پلنگ ایرانی در حیات‌وحش بهاباد یزد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/456378" target="_blank">📅 13:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456377">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9NCtNrXVCRFx4lzGCL3HIdiH_7cDyeAYMNWO8If0FUNOtzGxT9KheYv1BDvn1TUBgxz7G2vhwTP2UAa2IeAzGqgi-SgA7nkPTIY59coIzaYAv3W6NmXw1edPflcFpRvO5t14KBuV4JJ30-kTKkIuWOv22j79z3WVpxN6FCOkGpUidIW_qGZPOvKBI7e-jOcvcrTtl9DI6jMBcT0188aI-hGEfUgTKRHAxfcEuU_7Ag2Zk-QA0hMmZegmOJvC4h7uuLiBNC-WPzQPJ75Mk76wLDjM0s10MzQ44VLZZykr4A8nbl87yD847LkoKa7YTiJ5lFr10GKz1kXqnpw5GKASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌کل بانک مرکزی برای دیدار با مقامات بانکی و اقتصادی عراق راهی این کشور شد
.
عکس: فرج صمدی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456377" target="_blank">📅 13:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNJJYJZiaKpPW6iOodfOzWvCL4L2g8-dddd_Cr1EOkpfRXdhRisd1yOVyFl0jhJfEAkW7h0gQM1lk8nvqXV-mYtw6RVQG9G8ntTB1J_cN8TNoDpdxMHEXH8_rew2fqugn2jAsvds-aPagE5NU0-dW1QckirMb0VJk86bCap4i-HeZDZvMUYxPRhHn_fU5Zajcjg8Il2nwUK5wfW_QeJNIsUqhZ6NXRpD7AJh2LKIZCnlnNSJp4pWOsxcZKBjOOf2xmqN7NtKrdcEir6EMIyUvAF_KADgZ6lpdWj-3LzT5MiH3gKh7SxaFmJWWbaCCnOfr-5TF8sNwJjZUavBF1tYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدبه‌زندگی در ایران به ۸۰ سال رسید
🔹
معاون بهداشت وزارت بهداشت: امیدبه‌زندگی کشور به ۸۰ سال رسیده درحالی‌که سال ۱۳۵۷، ۵۵ سال بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456376" target="_blank">📅 13:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456375">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fba7c9e929.mp4?token=WNxLJHIeFuIZBHQYD96pPewXRAgDNR19XiHhYoKoujTdRNEhlxDm61ugVHai6-vyVEtrxiGjo4-aY97azc6NJQrgaQV4K5XGcpZduMMlJQTAvnYl5WnS_G9QzHT49AWg-Y3rfG4YYAlPsGXwQIJeXIUbePxj_xZfMDVjL5PxRB9mjwMXMi5A0hB_re3d89SVa4GilERNoztTb_lQ2mbPqQA-hmARwFDSAg29Lfg57Ny_wngUHzP3t8Faf_bjljrgr2VUica5l0j3bY-kgTMQIbPoOnMY3iECtLb3V6F4oRCjKM6UFSbRx3qFjJNhWXO3IW-MaqVLbFKi8qOvpkk1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fba7c9e929.mp4?token=WNxLJHIeFuIZBHQYD96pPewXRAgDNR19XiHhYoKoujTdRNEhlxDm61ugVHai6-vyVEtrxiGjo4-aY97azc6NJQrgaQV4K5XGcpZduMMlJQTAvnYl5WnS_G9QzHT49AWg-Y3rfG4YYAlPsGXwQIJeXIUbePxj_xZfMDVjL5PxRB9mjwMXMi5A0hB_re3d89SVa4GilERNoztTb_lQ2mbPqQA-hmARwFDSAg29Lfg57Ny_wngUHzP3t8Faf_bjljrgr2VUica5l0j3bY-kgTMQIbPoOnMY3iECtLb3V6F4oRCjKM6UFSbRx3qFjJNhWXO3IW-MaqVLbFKi8qOvpkk1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌بابایی: به‌عنوان یک مسئول خجالت‌زدۀ بازنشستگان هستم
🔹
نایب‌رئیس مجلس: برخی مدیران با گران‌سازی به‌دنبال عقب‌نشینی ایران مقابل آمریکا هستند.
🔹
در شرایط کنونی باید تمام پروژه‌ها و منابع کشور را با اولویت تأمین معیشت مردم تنظیم کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456375" target="_blank">📅 12:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456374">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH7wRQS4JrAWmXFzAPt0LBPeqLn_JjEOjOJ6Zd1oz1P8st9qiNDNQGcz_CwJuh8Zut5L6tt5rdeuJxLyxrgnT9XXAiR7NH2OqXa8wmGHDoOpI0ndnmzO7ZLabXI_odHBFO-6G8DcXfJW1PMWkWf9Mg3pqTzbdW38l6jgHOQGRBbwojMmltv2bbi3ePbdPnk7EdZrv5r-Kjf-4olEQctDW5tClYdLESyfffRUjhkpKn-7m10CRi4SsvdaNIIH0gFHoueBGiwauMU0qokCeBaaDeuTwxF0nyH7W4SH4mwQd0ENeGqBhlMucUyWlHyFJzx1288dzxSh8b0q-Kz_yymJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۳۰ هزار واحدی به ۵ میلیون و ۷۶۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456374" target="_blank">📅 12:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456367">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCldZ71L8H1BwEY5CbudEkDHXa9cWwwJZBNaCRbG4ozRzH0KcxmMOIR63S5mEL4COKTenNH_9slYVEu-m1m8JxTRPcKx9WMeTWL8QWbGso8NheEyR8w0kvNUl7RlgbGEzjs4y6X62Qq2n0eTceASxJwcm99c6lREHhM5g3HpaZERwAwZzP07d-m0JbTfLzIvYrD_n_p_oxUZcItf714hiYf8uWn3iCCHTlPoi1urVrIeTYfMMnHbxp0-1e43ZseIy_jNIAVFJyoyaF9r3BWWp0tBWnfLrB3eKVnnnygnY6U6P-sYL_oseWIn3NZyV37G9rIz8bLMfUvGy4bxV51sdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yn7rBpWMoaXXOg04A4SWFBunupDCbmR7U5mUoxH7tjRiJjtA23mTD2yqzwaMtfY7FZ1o4fmDZYsIpYGyGtcbW4oPoYVEsFKqrpIOml9u04tgaXXqem66eiGfptWxCsr627BntFUaBlY1YgYfrTG0LbkLk8_oOWizukc-fw-Wy_gHx9WOHJmxSCxxf8Uv-96yDHu9XxkW7fY_p8gaiqxVARfqNW4LBwJDuoP7sU902Jef0YbQZhAsb3BQiGcdpMmZfB1uLdfCqCOkZnwJIaA0T5HmER6SVD2ScyaYg3TCqhoIb76FCgnLM2ykZdJOiUyOP29FIUfuz-3OeyDrNtjL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rK_brezIVR-SQIn2iPeetq9v2Eb4IU2uyVlTgV0avmO2W3mREfrpZW9RdZ1nzG8I4YzeigRck_hbwKYjskzxbCuGC9LJxWnt-fbScAvh4m2bwoV3oXiLuca1wFnC9-MFMwkIg52Bxcnjskde3xhY_aKlmtylIXV-Pu09iWO_a9KK50HorkjblFayChry904nVzzKY98SFC6mRu1qU54Q7L1qjV-T6OIJx5OyDCZfCsau6k8HxBMamI0lEZEqC9t598XuR41denYDHmAehq0GVs8-lLJiJ4kN-IF3D5VojG4ChQ0EQc4pX43I78lRKEAd1eHv6QRgjoAHoHCtP10v_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_65FR6RijYdjDKJH2GV1zCJ9ltvSLrA_fzxdFASMHJGO8SWfrhG5Zlucd5wN5dtIjAJIsk6oRzlG6UQhDI1_cOuIBJM22JmGP5DpaPxM3y6qhLR-7HE4VHIPniqeonVYt-64781KepLIUAyM8FB7YJaB95QHzXZy7mOdHlnd6-sfVo9aCEdGxH6cSGzOkxaJKFwn-RKslaEu4tlv2LmtQgsGD66phs7S52Qo7JroOiJN4hcBin4RdDekoQ5HlVRHEOmtIcMEu_J1EWVzw6Wnc_fA2PZobvhJPmYcyBoIeLiFUAvpR4XPoFTsdnewwK3ByiMgB2y7rMTJC0lT7m7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYpq0t-8s5J6TcbDubSWDbARCE62voExMBO3Lt6lW6HZb_Thc5qsZWO3LpQWF55vt3z8KocndJ2Kp_SQCXdrwkgh2o9WfCrxKasXIzZKb9yg-UTsZ9HDt6JTuKrINEQJBUZwtAtVWsfaDtBF9MjMrI0vozM-ub4GltSmbPK4cqu8599TRsP6EGwnltQ_LdIO00L86gKyJ3ET6blpR-_QQ7nRyXoRkX_8svsbHCzeB6RnYvAXSXOyvIXDS-5CMfKcOz-IO9zYROr35D7m4VIvuqHNcRk5NECZZxojFAlmnhtsBnN00ZFp8typfB1cna-yv1G57ZYHi3gR7XKKvsgPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dR8ZbT-cr4Z9VVlL5nVjELln4J_ul36FrxX5uxN4wN9UplyuQHXyzV6SU_rb0oaHFqSyrHy_mWGRK8EsZyqE5eCr-4ODnd5wP7Es80d8lkrPxVpenTafotIkNJIXTRdx1qTqBaQlJCXIP71b1Wom3mMckMmxyUV6ESd7FozU1Uy4Eoj7WIgrW71sN5GbX-LqERBKBOW5JfOOrMh6cNqjQrYtBoe-BJudkaHDp5Nrb9pgKjkQfVL6k24mwFH44UZGQyq3Hxm5_g8yJKPWwFerB4oCxB3Q2pa-XpvU4u4Av06mNwZ0JNgaAIshetyh8pzHVb0eiuDMptKoxLDI_Yr8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFW5qeyrpKaA75l5DcKTH4Vphbmb6X7pZJn_188jk-8iIc3AKvhFoao55X6eWkA3z-YxG9YbE0taeDt6pHzDpl781v70fU_b9tB1_8Nn7MWTaCzC9V0VfKwjAqmQtCZ007qKw3wFbbmD9hcpf7_NOze94mcdIsmoMgQ1Pd1W7aWL218g9m3R92Zz_V_hilaMP2R8mSH68LJ4CC7IDsNLbQ9pSgEcYoVctUEa3HA38runzcYRBzFCZLUhO-fuhtwM_pPahJdEH2TnejHYqmmAQ1EWI8E4PiCWk0sL7G4tH6KLn7S2SZJ7wgZ5P6LY_mwXQ3qTXnkCh6csyMqAGHyuPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی هیئت‌رئیسۀ مجلس: کلیات طرح مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در صحن علنی مجلس تصویب شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456367" target="_blank">📅 12:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456366">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smf0OtcZp6tzatUTWy5shz12EYDOQNXl31yZSvRBsfCoKFZEH-9HG_yNnIRshnUf48ZTwfepe7R0MZxwF4LZNsBo1vMmBgHOSaa2RmEuoyD0I9p7oUrZPk2YkEAG--EOriEIB_FYEMUL1q-F2yx_8FnbmGImFXONcmMim_wGG_Fw_1RNDEbsBV8fii8AJ3vY6tLV7cJDpU8rEPNeSiU9ogXT5CEyUwTCZ6KEpHPg9oH8jYApuaWMgAuSNq8wLrcPSog_AA2_1pKUHc5mUSOrsbDthwpi5eDUvtbqq59yuyDJWW9m7ElP3AeRTXki8lO3CRjeIcWlzE5TBorx9JS5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آغاز ثبت‌نام بدون کنکور دانشکده رسانه خبرگزاری فارس – ترم مهر ۱۴۰۵
🎙
ثبت‌نام در مرکز آموزش علمی کاربردی دانشکده خبرگزاری فارس برای ترم مهرماه ۱۴۰۵ آغاز شد!
این دانشکده به‌عنوان یکی از مراکز تخصصی در رشته‌های:
📰
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
با بهره‌گیری از اساتید مجرب و امکانات پیشرفته، بستری مناسب برای ورود به عرصهٔ رسانه فراهم کرده است.
✅
شرایط ثبت‌نام:
📌
داشتن مدرک دیپلم (برای کاردانی) و کاردانی (برای مقطع کارشناسی)
📍
ویژهٔ متقاضیان استان تهران و استان‌های مجاور
⏳
اولویت پذیرش با سنین ۱۸ تا ۲۴ سال
🎯
پذیرش نهایی پس از مصاحبه و استعدادسنجی
✨
مزایای انتخاب این دانشکده:
🎓
مدرک معتبر وزارت علوم
🛡
معافیت تحصیلی
💳
شهریه به صورت اقساطی
🏦
وام شهریه دانشجویی
🖊
امکان عضویت در باشگاه خبرنگاران توانا
💰
امکان کسب درآمد از تولید محتوا در باشگاه توانا( مهارت و درآمد)
برای ثبت‌نام فوری، عدد ۱۴ را به شمارهٔ ۵۰۰۰۱۰۱۴ ارسال کنید
یا از طریق لینک زیر اقدام نمایید:
🔗
edu.Fna.ir
📞
اطلاعات بیشتر:
۰۲۱۴۲۰۸۲۹۴۱ – ۰۲۱۴۲۰۸۲۹۴۲
(ساعت ۹ تا ۱۷، شنبه تا چهارشنبه)</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/456366" target="_blank">📅 12:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456365">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صدای انفجار در مهران مربوط به خاک عراق بود
🔹
فرماندار مهران: صدای انفجار شنیده‌شدهٔ دقایقی قبل در مهران ناشی‌از عملیات معدوم‌سازی مهمات باقی‌مانده از جنگ در خاک عراق بوده و هیچ‌گونه نگرانی برای مردم وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/456365" target="_blank">📅 12:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456362">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bb10a8de.mp4?token=sJ1tMv39RP5KzP04dhTx6omV5vMMCf-9L7OP77pMh23XD0I6uzIlH_8ILi7ZIJKz43i6uFsXmhZQPchJ12s5y2KmOo9Naear-y4AFZ3oSWGRf7FTFuXVCqYZS97lH29zccCisggouwuJFBcRp23wkGAlH321XqlAIeBVunlgbehbTN_Vkdmxcd79lN69XpF3ct8ERBGgUker1gWrd1CNI0QLXq9j1E0PU1OwLuxf9uP4bM0ZHoOCr53wMKH3L0KsB4D-pSQg1YfYwqa_9YjCGDqe0Kbs_V-QqkObiEN1U9lr_mk9aq5QIthdprsTFQWJG2hq1JAOn9ky_qWhNxEQlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bb10a8de.mp4?token=sJ1tMv39RP5KzP04dhTx6omV5vMMCf-9L7OP77pMh23XD0I6uzIlH_8ILi7ZIJKz43i6uFsXmhZQPchJ12s5y2KmOo9Naear-y4AFZ3oSWGRf7FTFuXVCqYZS97lH29zccCisggouwuJFBcRp23wkGAlH321XqlAIeBVunlgbehbTN_Vkdmxcd79lN69XpF3ct8ERBGgUker1gWrd1CNI0QLXq9j1E0PU1OwLuxf9uP4bM0ZHoOCr53wMKH3L0KsB4D-pSQg1YfYwqa_9YjCGDqe0Kbs_V-QqkObiEN1U9lr_mk9aq5QIthdprsTFQWJG2hq1JAOn9ky_qWhNxEQlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ مجدد پهپادهای اوکراینی به مسکو
🔹
اوکراین یکی از بزرگترین حملات پهپادی به مسکو را انجام داد و انبار فروشگاه بزرگ اینترنتی وایلدبریز (Wildberries) را به‌آتش کشید.
🔹
وزارت دفاع روسیه اعلام کرد دیشب ۸۰۰ پهپاد را رهگیری کرده و شهردار مسکو هم اعلام کرد که «دیشب ۶۰۰ پهپاد به‌سمت استان مسکو در حرکت بوده‌اند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456362" target="_blank">📅 12:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456361">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab8c1799f.mp4?token=K26CA_8QQTe95j8Y-J7TkXrwuATSIkzgHN0vNrsW57k8qFATnYLLd-PBsxkMIMrFuICccyzeuNmZGsb2j7AfKTW5g3NwhhQ3VkISSbicPbDdki3K3azThx7iBPzcoXjOZ32ek-jCXQgKbHtcEgwkti3rIp9rU420aA6v0VB5QQPJJSAEkuI7k4tBfq9oVTC8iH24rcPi9a4hrtnwiEmUZYJiWJ_MV4pFmQ9BWGoB6AqfoHOvsxeKrnupqCGcgFZZpE6aBwdqdiIbEtDHHTdKKn0coXEzrwH_ZDlBWMw6GjRAekLEDy3aNOqy9OXFwz5fueg7yRbLN1T2JpYv54Salg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab8c1799f.mp4?token=K26CA_8QQTe95j8Y-J7TkXrwuATSIkzgHN0vNrsW57k8qFATnYLLd-PBsxkMIMrFuICccyzeuNmZGsb2j7AfKTW5g3NwhhQ3VkISSbicPbDdki3K3azThx7iBPzcoXjOZ32ek-jCXQgKbHtcEgwkti3rIp9rU420aA6v0VB5QQPJJSAEkuI7k4tBfq9oVTC8iH24rcPi9a4hrtnwiEmUZYJiWJ_MV4pFmQ9BWGoB6AqfoHOvsxeKrnupqCGcgFZZpE6aBwdqdiIbEtDHHTdKKn0coXEzrwH_ZDlBWMw6GjRAekLEDy3aNOqy9OXFwz5fueg7yRbLN1T2JpYv54Salg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استادیار جغرافیای سیاسی: تصویب لایحۀ خزر خطای محاسباتی بی‌بازگشت است
🔹
کمری، عضو شورای مرکزی جبهۀ شریان: تصویب کنوانسیون رژیم حقوقی دریای خزر در شرایط فعلی می‌تواند تبعات بلندمدت حاکمیتی و ژئوپلیتیکی برای ایران داشته باشد.
🔹
تصویب این سند پیش از تعیین دقیق…</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/456361" target="_blank">📅 12:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456360">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOLb76DvSrtxPZ8SV4Jn40ojphJ_7K09UGGVciQuitufmhbx1s-zdJU4paFOmeLq_63FihTYexzce-1W5Ja9_5Glf-zvNfKtgEJmS--XdVXm95ny3npEfY1VqXJepwJfa2P44s2BADg0R8wI3TmAk3S7S0wFM6ccN8BI5GWix3GhvCIOZVS3muHrNpZBhw05ttLQIf3AAU1t5AsUB7mKehR56-L2fThBO-1grSe9gSyo8inEplLy0-BLT0whi0g5OWCKdFWC7D0FujIjhU5BkSUrcn41N1FvarmSOwUl0b3ZjI5EY2ZXyd8l7I1kd43b-7aWzbSACwMhFjYJQsHg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت عراق برای هفتمین هفته به آمریکا نرسید
🔹
ادارهٔ اطلاعات انرژی آمریکا امروز اعلام کرد آمریکا از اواخر ژوئن سال جاری(اوایل تیر) تاکنون هیچ محمولهٔ نفتی از عراق دریافت نکرده است.
🔹
این درحالی‌ست که عراق به‌عنوان دومین تولیدکنندهٔ بزرگ اوپک، به‌طور میانگین در سال ۲۰۲۵ حدود ۱۷۹ هزار بشکه در روز نفت به آمریکا صادرات داشته است.
🔹
علت اصلی این توقف بسته‌شدن تنگهٔ هرمز است که صادرات ۹۰ درصدی نفت عراق را مختل کرد.
🔹
تلاش واشنگتن برای جبران این کمبود از طریق بازگشایی خط لولهٔ کردستان به ترکیه نیز به‌دلیل مشکلات فنی و اولویت صادرات به اروپا مانع از رسیدن نفت کردستان به بازار آمریکا شد.
🔸
براساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیرهٔ‌ استراتژیک نفت آمریکا به ‌کمترین میزان از سال ۱۹۸۳ رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/456360" target="_blank">📅 11:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456359">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3995b6e7ed.mp4?token=pzjHF_WcRKWv08n_OS7D1NB88BCt1PdKOV96BS0VVjsAZO-U6i-xNrhecpG1JILONqym9No4ZWAnwNSBLdQ_u_hWU_ygwpinFYAsdPBavvjyxiyCacG-ecoy4dLRRMEioJmwQRqKE1BANGOrr9Vavsoky8JHoixKQ6IHotQ0KSQ50t5OtwyPJZEX8C_JQPgNqCiUfWpActsxGslicjti1b-XsfShRInbOR2Y8Ug_1uW68sLCB_xujbKitVqTiD_WDx2i-_icz9PapPLOZYOU2MEL2KRYP8HgoypOy2lPVAywGuPfHUznW5NF6dSgMW0cC-y9O8iSCb-9sQSq9-wmQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3995b6e7ed.mp4?token=pzjHF_WcRKWv08n_OS7D1NB88BCt1PdKOV96BS0VVjsAZO-U6i-xNrhecpG1JILONqym9No4ZWAnwNSBLdQ_u_hWU_ygwpinFYAsdPBavvjyxiyCacG-ecoy4dLRRMEioJmwQRqKE1BANGOrr9Vavsoky8JHoixKQ6IHotQ0KSQ50t5OtwyPJZEX8C_JQPgNqCiUfWpActsxGslicjti1b-XsfShRInbOR2Y8Ug_1uW68sLCB_xujbKitVqTiD_WDx2i-_icz9PapPLOZYOU2MEL2KRYP8HgoypOy2lPVAywGuPfHUznW5NF6dSgMW0cC-y9O8iSCb-9sQSq9-wmQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واژگونی کشتی در زیمبابوه ۷۲ قربانی گرفت
🔹
واژگونی یک کشتی مسافربری در زیمبابوه که بیش از ظرفیت مجاز مسافر داشت، ۷۲ قربانی به‌جا گذاشت که ۱۸ نفر از آن‌ها کودک بودند.
🔹
این کشتی از شهر کاریبا به‌سمت مناطق روستایی و جوامع ماهی‌گیری در شمال‌غرب زیمبابوه در حرکت بود؛ مناطقی که جاده‌هایش آسیب‌دیده است و دسترسی محدودی به وسایل حمل‌ونقل عمومی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/456359" target="_blank">📅 11:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456356">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/447cfe6f37.mp4?token=K7ablQlQnNVSgVy-jz-B7s1C7XSyxahAOy_5nK_nYijF_YSoI_ARZmFerQ77UvkVLW0uUytaNTN99TIi04m_IL2MhRjRtkf5rcClklE37kA_xJt6NrCFoRrIG1kxcMzNsUMCQi0ZEda-nMfZLqNMwpszCza2C-9-mIvYGq8tfQRtuSG-q1328TGqOjn3FiwEKMGLOCCK2BKA3UERyVEXPiLwncYlIb1PQ3IdRYOR5jd6Yfrfe9t9EiamP-9xXSgg5A6_uK49gyGn3OZN9j8CeFRTAnI4yX_61f5ax-ObbtSGRWkaow2HO9vo0V3zRoLQMWQk1l3SO0hQriOoriqT5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/447cfe6f37.mp4?token=K7ablQlQnNVSgVy-jz-B7s1C7XSyxahAOy_5nK_nYijF_YSoI_ARZmFerQ77UvkVLW0uUytaNTN99TIi04m_IL2MhRjRtkf5rcClklE37kA_xJt6NrCFoRrIG1kxcMzNsUMCQi0ZEda-nMfZLqNMwpszCza2C-9-mIvYGq8tfQRtuSG-q1328TGqOjn3FiwEKMGLOCCK2BKA3UERyVEXPiLwncYlIb1PQ3IdRYOR5jd6Yfrfe9t9EiamP-9xXSgg5A6_uK49gyGn3OZN9j8CeFRTAnI4yX_61f5ax-ObbtSGRWkaow2HO9vo0V3zRoLQMWQk1l3SO0hQriOoriqT5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مواجههٔ غرب آمریکا با یک سیل مرگبار
🔹
مقامات آمریکایی می‌گویند که ایندیانا با «بدترین سیل ۳۰ سال گذشته» مواجه شده و سیل در این ایالت آمریکا تلفات انسانی هم داشته است.
🔹
شهردار ایندیاناپولیس و دیگر مقامات ایالت ایندیانا در یک کنفرانس خبری از ساکنان مناطقی که در معرض خطر سیل هستند، خواستند که به هشدارهای تخلیه توجه کنند.
🔹
ماهیت بی‌سابقهٔ سیل، ظرفیت امدادگران آمریکایی را محدود کرده؛ مقامات گفته‌اند که سیل در مناطقی که سابقهٔ آسیب‌دیدگی نداشته‌، مشاهده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/456356" target="_blank">📅 11:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456355">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwFeqNR9RC61wizv5t28swAXS45rbVaB5HY16VAenm10rmEPi3aosFHyKaSlMqLYfwazzlFciF0ZPzciqAu3DOjyDslINwGRfnDj2bZPI-4rPuaRD5YZvyVy4Xytjj5Z256D4ZWs7udmSENgBIEKFZ4fFPWRyyJlF1XxsdfbjuQxgAV53wRcc0XxxE8KCj_z5-CeJZdr_Ir5p9dxqX3qAFA9pXoGt6S6_sRbbhXreUqTbqUjsu1TeyXEfDTaUkIF89bzSa_SM7agnMvLsH5oWUsBCrZaJmHXlZkIesbJMKBD2N6t1b7T1095jkul1RchSvXCXwELh4ZscTF9KMLSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارمزد ساتنا و پایا هم با دلار بالا رفت
🔹
جدیدترین نرخ کارمزدهای بانکی نشان می‌دهد کف کارمزد پایا با رشد ۳۳ درصدی به ۴۰۰ تومان و سقف آن با رشد ۶۰ درصدی به ۱۲ هزار تومان رسیده است.
🔹
سقف کارمزد ساتنا نیز ۵۰ هزار تومان شده و کارت‌به‌کارت تا یک میلیون تومان ۱۱۰۰ تومان و با هر میلیون اضافه، ۳۵۰ تومان بیشتر می‌شود.
🔹
معاون فناوری اطلاعات بانک شهر می‌گوید که کارمزدهای بانکی نسبت به وضعیت قیمت دلار خیلی عقب مانده است؛ چون خرید تجهیزات دلاری است و دستمزد توسعه‌دهندگان نرم‌افزار بالاست باید متناسب با آن کارمزدها افزایش پیدا کند.
🔸
پیشتر رئیس‌مجلس گفته بود که افزایش نرخ ارز نباید بر بسیاری از کالاها و خدمات اثرگذار باشد؛ چرا که اساساً ارتباطی با ارز ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/456355" target="_blank">📅 11:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456354">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVEgwT8wmoS5RMbnbZigNbREGhL3B4tonVpW_Jb-26kKReqyMRvTtrFzUy_kQLVV78SxPcZkKjg8nDgvgpmED9AFh25U4kDAnkuCP6JwFfbtHahwtqhg6cwq3hYQru-Qc2v-GHWbFB88HnOPkXtcGf6LaF4ZggLTiikNgB63jjOkOSFPfKRYyJxZbjakZqzpVV3pua0xJUMnul4ay4Qz1JX28luisVJmuKV3fQt6QdLw8D-xCLlray5S4OZV3Z8O4cFR3CKjRLxREVmHRQx6VHKz0FCZM76f9VNSNpVWAo1cdEUCaMkhKmr_lVeZLJqUrQkhmn34L-1rK82jyOuhLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت‌های تازه از جنگ رمضان در فصل دوم «سرو، سپید، سرخ»
🔹
فصل دوم مجموعه نمایشی «سرو، سپید، سرخ» به تهیه‌کنندگی محمدرضا شفاه، محمدجواد موحد و آرش زینال‌خیری با ساختاری اپیزودیک، سراغ روایت‌های انسانی و کمتر دیده‌شده از جنگ رمضان رفته است.
🔹
در این فصل کارگردانانی چون حسین مهکام، دانش اقباشاوی، مریم اسمی‌خانی، امیر داسارگر، علیرضا صمدی، محسن بهاری، سیدمحمدرضا خردمندان، امیر ابیلی، علی طاهرفر و حمزه علیرضایی پشت دوربین رفته‌اند تا هر کدام با نگاه و زبان خود و در قالب داستان‌های مستقل، بخشی از روزهای جنگ رمضان را به تصویر بکشند.
🔹
این مجموعه محصول مشترک سازمان هنری رسانه‌ای اوج، سیمافیلم و مؤسسه فرهنگی هنری اندیشه شهید آوینی است.
🔹
«سرو، سپید، سرخ» از یکشنبه ۲۵ مرداد ماه
ر
وزهای فرد، ساعت ۲۲ روی آنتن شبکه یک سیما می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/456354" target="_blank">📅 11:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjShD4JZJHIS47OEVtCQyMlE9Vqva6jiR2XfmkkkuANA7EGyyYGHNJNEIeyZOZaMGY7o0de8AWt9-EmskCqBtaQH1ThiAUAQq1mAPC8zYsufqw_--gafnJDdApqggO7a_dwiN6WnxBsadwChyradEkC8v-pG1_iLsYb0xfP6eLG7T80azNV-FEwHqXP-Keb8baYHRLgFghS2VPWhujBJqP6cYA2SCviE_ZquIQ7yqEIcawVBZQko4B4ebxcblTaIm06rthrZjRNlbF6W2qd7H7dDzr41Ev0XsvCXCxK9tB-QnMxPgZsSI3rssLssYvTjYX-maUxya7_9iCLZkzX7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هوش مصنوعی را به مزیت رقابتی سازمان خود تبدیل کنید
🔹
تحول در روابط عمومی و رسانه، از همین امروز آغاز شده است. سازمان‌هایی که بتوانند ظرفیت‌های هوش مصنوعی را به‌درستی در فرایندهای ارتباطی خود به کار بگیرند، سریع‌تر، دقیق‌تر و اثربخش‌تر عمل خواهند کرد.
🔹
دوره تخصصی
«هوش مصنوعی در روابط عمومی و رسانه»
با تمرکز بر نیازهای حرفه‌ای تیم‌های روابط عمومی، رسانه و ارتباطات طراحی شده است؛ از
پایش و تحلیل رسانه‌ها و افکار عمومی
تا
تولید محتوای هدفمند و مدیریت ارتباطات در شرایط بحران
.
ثبت‌نام انفرادی:
📝
ثبت نام دوره آنلاین
📝
ثبت نام دوره حضوری
برای دریافت اطلاعات و تهیه اشتراک سازمانی:
📞
۰۲۱-۴۲۰۸۲۳۲۴</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/456353" target="_blank">📅 11:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/456352" target="_blank">📅 11:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456351">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7Zs90fnjRupka2MVEfRn5IMIwUGMx-G5Fg7SlW9hlPmev-ZigFB-C6IFo1nOlEMdRTLHucBWSmPb2PpP2lIAIZfisyx2Az9BHEc9T6L9Xs7wKvxoRs_BW4tdHWz62dsFNqXc1BF-epziwUk-BvtMEBBvy4VTu43skMWu5Xd59K6eRP81GeXajJE186G_yxGq62euhogFkAvRuizHvhrYCbfCkx1h_k-VmbocVxdUxd6Jv9QnyJkHa42Cr3Wir_tSV6KDdpD45yten6t-o24AaK7r6k5_kJPdCSOPZGlV0SnqjgdVeH6bkcwbIGT8R-vELfot64YNAbenmbn_yMmBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت‌رئیسۀ مجلس: کلیات طرح مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در صحن علنی مجلس تصویب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/456351" target="_blank">📅 11:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456350">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nahUclP2aeHLTY9MgcHXgyXFHDlSVc5NuccAITLo1hMQPErmyn1lfseIEFTwJvqhhcJIeZ6CaU61U9O93T_6Mt0xwQTjR__4fddfQZYCiIXESJ2FgP5MSJ-vNkxfoWZOmz4zS7oLyIt7vlGDM7O2xkPwyxK2q_s5soICmv1uZcRWYN5H2ltprfTMmF2pzaP4JBTh3aZykjcUDYcQFIkK5qodNDkNJOqMjt0bSmpNr6_HcWuYnNshQoGHXvvRTTzu0bJz8-8yAR65iPsGcFb3-kKplg2tna1JMRf2BE5t1R5N_0p5754JztGj50wwstK-ikG8G5cUCCPj4kJaRLxgFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوزویک: جنگ با ایران شکارچی افسانه‌ای آمریکا را زمین‌گیر کرد
🔹
نیوزویک در گزارشی با اشاره به سرنگونی یا سقوط حدود ۴۵ فروند پهپاد MQ-9 Reaper آمریکا در جنگ با ایران، معادل نزدیک به یک‌چهارم ناوگان این پهپادها، نوشت سلاحی که زمانی نماد برتری هوایی آمریکا بود، در برابر شبکه پدافندی یک کشور دارای توان نظامی پیشرفته با آسیب‌پذیری جدی مواجه شده است.
🔹
«آرون داوسون»، کارشناس قدرت هوایی در مؤسسه فریمن کینگز کالج لندن، معتقد است جنگ با ایران ضعف بزرگ‌تری در الگوی جنگی غرب را آشکار کرده است؛ وابستگی به تسلیحات بسیار پیشرفته و گران‌قیمت که توان تولید آنها با سرعت مصرف در یک جنگ پرشدت برابری نمی‌کند. او به کاهش ذخایر موشک‌های رهگیر پاتریوت و تاد آمریکا نیز به‌عنوان نمونه‌ای از همین مشکل اشاره می‌کند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/456350" target="_blank">📅 10:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456349">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQysK2sIMpOQdZdmZp6ZmFEetg0Eye3eOUzSr6n6pp8IOvFcRi83g8VkstnYDTj-32jNKzfdGa9uJnwj59Xk6DQv-CyvWktHzONpiDdkKWarNVDcbkWUhb__1QC52bxkxym1nZkCzUp8MpZg4XRW_q9VW4NdAMwJrwv0Lv77N44v9eZMwke2N_RbY1IgteHEu32yn09PUXgxh8uVwklg3ypmXmscxgZoj3btHn_jct9io8D6HZ1__dwQQmcbd2CB7XnMObYBu1eLYemRHhIigYQIAqeDYUdEGbd6-akzu4jtpVj0kJCqbXnZYh4R5GvlBV-gE6MpfzWC7FqLbKTXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: از شعار انتخاباتی Make America Great Again فعلاً فقط نرخ اوراق ۳۰ساله آمریکا بزرگ‌تر شده: بازده ۵.۲۱۶٪ بالاترین سطح قرن ۲۱م!
🔹
حالا رژیم آمریکا برای تأمین مالی نیازهایش باید با نرخی ۳.۷ برابر سال ۲۰۲۰ استقراض کند؛ یعنی برای هر ۱۰۰ میلیارد دلار بدهی، سالانه ۳.۷میلیارد دلار هزینهٔ بیشتر.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/456349" target="_blank">📅 10:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456348">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ستادکل نیروهای مسلح: تا شکست کامل دشمنان کوتاه نخواهیم آمد
🔹
ستادکل نیروهای مسلح در بیانیه‌ای به‌مناسبت سالروز بازگشت آزادگان سرافراز به کشور ضمن گرامی‌داشت این روز و تبریک آن به ایثارگران و خانواده‌های آنان، تأکید کرد: سرمایهٔ مقدس ایستادگی و مقاومت که از نسل آزادگان به یادگار مانده، امروز به دست جوانان برومند و آزاده رسیده است.
🔹
در این بیانیه آمده: اکنون و پس‌از گذشت ۳۷ سال از آن سال‌های حماسه و ایثار، سرمایهٔ مقدس و ارزشمند ایستادگی و مقاومت که از آن نسل سرافراز به‌یادگار مانده، به درختی تنومند و ریشه‌دار تبدیل شده و به‌دست جوانان برومند و آزاده‌ای رسیده که در لبیک به قائد شهید و رهبر عظیم‌الشأن انقلاب اسلامی در برابر مجهزترین ارتش دنیا ایستاده و سردمداران ورشکستهٔ آنان را به زانو درآورده‌اند.
🔹
این میراث گران‌بها و ارزشمند همواره گویای حق‌طلبی و ظلم‌ستیزی ملت قهرمان و مقاوم ایران اسلامی است؛ ملتی که بیش از ۱۶۰ شبانه‌روز در حمایت از فرزندان خود در نیروهای مسلح، با طنین انتقام‌خواهی خون پاک امام شهید خود، بر صلابت، اقتدار و ایستادگی نیروهای مسلح در برابر زورگویی و زیاده‌خواهی نظام سلطه و استکبار جهانی به‌سرکردگی آمریکای تروریست تأکید کرده‌اند.
🔹
به ملت ایران اطمینان می‌دهیم که تا شکست کامل دشمنان آمریکایی-صهیونیستی در منطقه، احقاق حق ملت قهرمان ایران و تسلیم دشمن، از خواست مشروع مردم و مطالبات رهبر عزیزمان در برابر آمریکای متجاوز کوتاه نخواهیم آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/456348" target="_blank">📅 10:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456347">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دولت ۴۵ روز برای معرفی وزرای اطلاعات و دفاع فرصت دارد
🔹
سخنگوی هیئت‌رئیسه مجلس: با دریافت اجازه از رهبر انقلاب، دولت از ۲۹ مرداد به‌مدت یک‌ونیم ماه فرصت دارد وزرای پیشنهادی اطلاعات و دفاع را به مجلس معرفی کند.
🔹
ایدۀ حذف شرط اجتهاد برای وزیر اطلاعات مطرح شده؛ تغییری که به‌دلیل مغایرت با قانون فعلی، نیازمند اصلاح قانون خواهد بود.
🔹
قرار است دولت برای این موضوع لایحه‌ای به مجلس ارائه کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/456347" target="_blank">📅 10:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456346">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سردار باقرزاده: ۳ خلبان ایرانی توسط قطر به اسارت درآمده‌اند
🔹
فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح: ۳ خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند.
🔹
«جواد صالحی»، «عبدالمجید دشتیان»…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456346" target="_blank">📅 10:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456345">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e832dd9f5.mp4?token=B4zhXrxkmj3VqyspHcoC6uyVmuo5uZouC-MZ3K_IT2hPHhVGiFJBvti3LWIbZKPj8sg2q62gGVJRPdBHl59o9UP-Y7_N7OgPJz9gU65He1oifTKNYW_bI8RC0qnnoKKZpGOg2Y-2hj1giOZ0Gcnl0cXu4OxkkUBspwH5zQdSxuURE2YCrZ1bXVs3q3L53XX080qWgJT9Twv3gbb58bj8EsYaW_R_70dJbMWUE2NlIcUydxFOZ0CQ_9BqO6wHGFlEvehVVxcn-Y_ekUjhthTUcmAr4F43arpzZxZUoM6LhZ4lYnOQY2jeZIJ43lneCebbgXeMV-u61qYJsSWDKAFFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e832dd9f5.mp4?token=B4zhXrxkmj3VqyspHcoC6uyVmuo5uZouC-MZ3K_IT2hPHhVGiFJBvti3LWIbZKPj8sg2q62gGVJRPdBHl59o9UP-Y7_N7OgPJz9gU65He1oifTKNYW_bI8RC0qnnoKKZpGOg2Y-2hj1giOZ0Gcnl0cXu4OxkkUBspwH5zQdSxuURE2YCrZ1bXVs3q3L53XX080qWgJT9Twv3gbb58bj8EsYaW_R_70dJbMWUE2NlIcUydxFOZ0CQ_9BqO6wHGFlEvehVVxcn-Y_ekUjhthTUcmAr4F43arpzZxZUoM6LhZ4lYnOQY2jeZIJ43lneCebbgXeMV-u61qYJsSWDKAFFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ تراستی‌ها به داخل کشور رسید
🔹
تراستی‌های نفتی در روزهای اخیر به‌صورت جداگانه در شِبه‌رسانه‌های داخلی فعال شده‌اند.
🔹
اقدامات رسانه‌ای تراستی‌ها پس‌از آن آغاز شد که رئیس سازمان بازرسی، از عزم دستگاه قضا برای برخورد با تراستی‌های متخلف خبر داد و گفت که «۵۹…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/456345" target="_blank">📅 10:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456344">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3373fb4d8d.mp4?token=B2sIbzG3Lhhre6ZEvnmIo-ZqWGhm4Ruj_mt0oWGjUCMlg3OrGSJmp75-DV3y-OXC9nlZGM5V0iukIT1orkElZK0j6eqlvthD41dX2EK-2mXPj3jxjPb-z3CeRSO-nD4L9WTST3pF1_roFQ_6_J04aOBNT69oFwK1v4kEbPx0OU1Y_Bfo2CP7T2Vy_Ua_HdqDcrX8hLmfLoF_GBUu8EkHACZjuY7YAwuMLO_jTRN8GvhZ0T3ydiUSBbAQ0ltdRi1Bnp8LQlyUqKqnnrxnT2-norRSV3rgnhzeiyjlAk8faNUuzAQ7kAOcHE8lZtIJPr4bLkJ39IcQpojV5dXDEGVvzrA3S38Uqj22hF2bhHVOiFvhx1Or02RSdvmLKN9ixSv7sDJb80PutR6OdQ4n59jlfscZ6gBFFn0AcoovLuzHd7NBSq3v2CCmcJJbFG8np1TIlH3je6igXzVos6bGygh7PtjD-nPXbDKB6n9NbBkB3XCIQgZrCmsFhoVgoM7wz5FVVwMHkelEBYHmrTVa4n0DrunQLqcJqwqJ4raCvESeKP07mat_qdmq3mrenOgRr3O1oBqfjwFvHg-SzyR7ve16CWBdfCQGb7rEpHj7xKDJpGzl1nEZJMrHtbeBsAKMPKJASIE4tr4UH4JZmcx_nsr2FkSQhan5tRjJ6WY_c_igJgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3373fb4d8d.mp4?token=B2sIbzG3Lhhre6ZEvnmIo-ZqWGhm4Ruj_mt0oWGjUCMlg3OrGSJmp75-DV3y-OXC9nlZGM5V0iukIT1orkElZK0j6eqlvthD41dX2EK-2mXPj3jxjPb-z3CeRSO-nD4L9WTST3pF1_roFQ_6_J04aOBNT69oFwK1v4kEbPx0OU1Y_Bfo2CP7T2Vy_Ua_HdqDcrX8hLmfLoF_GBUu8EkHACZjuY7YAwuMLO_jTRN8GvhZ0T3ydiUSBbAQ0ltdRi1Bnp8LQlyUqKqnnrxnT2-norRSV3rgnhzeiyjlAk8faNUuzAQ7kAOcHE8lZtIJPr4bLkJ39IcQpojV5dXDEGVvzrA3S38Uqj22hF2bhHVOiFvhx1Or02RSdvmLKN9ixSv7sDJb80PutR6OdQ4n59jlfscZ6gBFFn0AcoovLuzHd7NBSq3v2CCmcJJbFG8np1TIlH3je6igXzVos6bGygh7PtjD-nPXbDKB6n9NbBkB3XCIQgZrCmsFhoVgoM7wz5FVVwMHkelEBYHmrTVa4n0DrunQLqcJqwqJ4raCvESeKP07mat_qdmq3mrenOgRr3O1oBqfjwFvHg-SzyR7ve16CWBdfCQGb7rEpHj7xKDJpGzl1nEZJMrHtbeBsAKMPKJASIE4tr4UH4JZmcx_nsr2FkSQhan5tRjJ6WY_c_igJgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه رود ارس در امتداد جادهٔ مرزی جلفا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456344" target="_blank">📅 10:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g27On2mcpKY9cyQjkCEE3DfVRuesbiJoGvSRzFbPQoAuleZFUZYOROokj76ngjN7sQTQn1mCTYL3_aITAoXMCBiNN3wRdU7F06-HC6RbSyqH6NBeg78S9C_L6q8FsSbK18ZshPTcZMPu9LlEQMcDqjq3OcK6t9mUeWCV-2UxJqUZl2VIijN7F9W5i9Am2dlbKo5v6DYB3GzoQk2R1n-f5BGJNb2f3pLC1yH_C4K4cFOUGm94NzpR20fBkvRr61i5kr8_tgN6Df_Uh9jQ4fp3KVn8_iS83GXVCkcDCMzLK6kWsIKZd6NzPM3RbUOJ86aQZINGv4q6_7klecGEaEJQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت چهلّم «آقای شهید ایران» در تهران، قم و مشهد
🔹
دفتر رهبر انقلاب: همزمان با ایام چهلمین روز تشییع تاریخی و تدفین پیکر مطهر آقای شهید ایران، مراسم بزرگداشت آن رهبر عظیم‌الشأن و خانوادۀ ایشان از سوی حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای در تهران، قم و مشهد برگزار می‌شود.
🔹
تهران: سه‌شنبه ۲۷ مرداد، از ساعت ۱۷ تا ۱۹، در شبستان مصلای امام خمینی(ره)
🔹
قم: چهارشنبه ۲۸ مرداد، بعد از نماز مغرب و عشاء، در حرم حضرت فاطمه معصومه (س).
🔹
مشهد: پنجشنبه ۲۹ مرداد، بعد از نماز مغرب و عشاء، در حرم مطهر رضوی.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/456343" target="_blank">📅 10:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456342">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9GcQfnMo92Vy0kJkRrVIrOOml--trMCEU2JlPILWxVh_RbKY0JNV6ftKNLUGK3mUl_66QYZl4ekhe80Xthie2WO-MscvkldE14FD0dGCZqwU9Fpd1LwdNY8KkCgrukL0tGITQmEUmGgiDkXHvi3hHbsx1d12osn_Qu6hjVEPDnj5Bf4qy3TUW392YXnTGIaRqY7tlmtieAyHOfeja4vQgkZmpLKFlLVtg70FzUzaj6OmOPjS1dlX07EDAooOQ4e7IkaKXUY8IJi9_WkEwmBd0GVptrcGQfjaYOJkHlxYOMQFpGRBb68WcHpp2mA5AvtLPI1hQrETQsWjJVOjG4F-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گازِ صرفه‌جویی‌شده حالا قابل معامله است
🔹
وزارت نفت از صدور نخستین «گواهی صرفه‌جویی گاز» به ارزش ۵ میلیون مترمکعب برای یک پروژه بهینه‌سازی در استان یزد خبر داده است؛ گواهی‌ای که پس از تأیید میزان صرفه‌جویی، قابلیت معامله در بازار را دارد.
🔹
به‌گفتهٔ وزیر نفت، این سازوکار می‌تواند صرفه‌جویی را از یک اقدام صرفاً مدیریتی به یک دارایی اقتصادی تبدیل کند و پای بخش خصوصی را به پروژه‌های کاهش مصرف باز کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/456342" target="_blank">📅 10:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIwhR6s4Dn8AxCqmVeMg8z_C-JU-y3A4tX7clugWudZFKJwNeIuJyRfi5ghnnGaanDE3w2JrptxGaMVNlLwEjJ5oqLsuKzAiQeKwRVDGYNzS6Qe7rdj0jKTT1JV4VsBAe8AjiGrWkxeau4RVsvh-EUk28rjuNYFFNHxnps1u8o664Ns25OIEqm1WNKSEqSTe3JszbsWLxL978qind6HOTJUoxFwc9ugAjc7SsewNWMvO_oph4FGrP4QYfGbiXhvT8l835Uh4vGFGHrQQOpfVnoHtzvEdntPE_Y3oT8TKV8V1YagLOaf9f8Cr8ICpveBgaLhbG-Odq9Lmdnf2sMk6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxXFCrcTtuwT-nBIXHzMKMPvK2c8n4Bb0t6sxnGdzrsKGJxdjTSt7VMuvIHkBM-w8deXZl7fxVqUWG_-X9XhRo-g-HSTLrjod3mQYgxl4VPT0MChABaIhHA6Avf2HqIDrv1nBRnPzW1-xBkDaqs3jvPjBZJAevlcxstwcUa4Ry2FVkyKYFb-kvTOZlLw5CjSdljAAyzmHddI5692bRr8NkJ1SNnTFJS4y23O-sF3Mmg4LP4xmCgxyNxd_ru8sKPR_gfp-TiwqyJhHyPXwlfe1uOey3XnlxQbv4vkZtOkgT_cR9GjUs78cxpp3S_x-l07NoQYHVGtJOFXlMhea1enXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxNh7Eui6PZEc2xgnbQzhYjsR6M4VfS8cRuQIJ3_ADpAgCWUBAGwzzb5D97rdWHEYD6BKZcjYg4N0rBpYuF7UamnvbsUktbT8-qNmSv8G1vj-rjYVE3kI2-lrv6KfeHjZwvxWYWSVQ6l3mmQWQelreBX5dXhzqXQYqbgrCIA01oMbrM2OJh6bnEP45KTETwDzPAMMA5cfHCBZmIEu3mPfsxLIuncsldUSdPtklNQBRfYESAR8e-rywVyY8PCNapgKsSWcHZklCXSMXujs4bc0F7svWars-oxM91NEiuWVxwbK5a2AJZp2zYgqTgKGtMKAQ-6929qUUSzNImn3cBz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCMZFbjI5SKHR6i92s7_ka9VQe3YlxnF_H823RH0plQSCdKgiMKa9kbIjBQO_2KNgW0CSg7AQbwB3cnILucnjNdThDDSZcwnTFj8wIZ9e1DTU5K2KS400Nf6RFAqlNmcqq7cxo1TNpxrQYxjvavQVR-TNl-1k218gw8DWT76E9-_XvMx3owdejgy2VVVVTLAmqYHnUEOgGpwTT6BMAEJKsSg2V5LLkXT0P8ZbOMCS5203HV9st9T3XB1_519_maSR_XhwC_N2B7j8zFQuNPW-Coocpqknms9H8zRZbO58MN6JIKnba6ftEKF8SFKAS6tztUtMRUOnxys5PDcaxI-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwZFCxog3LhFgEIlGW1ge5DoZetuhm-iXAk_0yzZetjpx8PJcOQzSd7ZtwkuBB9fa_9059xisot8zrULJDiTP8ay9OJMi3dn1H1NmDztojouqEl74TwblBIIc-IX4C_yqrumzUJKR11xy4yAU3U2uDfsKehkFP4rsBHNn8ZDNB9J4btwJUf-afCNnPz7Cmm5QUdow44U7sPCWs4INrWpWqTWZraObsiqb7Hond8eTvZgnW8XGkfMlKB-Ne23HyCZALEUZLKY__YVx2OpqX5lBSZ3L1YVRCvL9JX7wfeOcRx_kKB9KJob8eaOSwUolnL5xTofXuw7A1Bb_RmfJX47OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsxyGWUmUF9dght9E8yQYpOYgwZMCCbHQPmLWq9hRqrqaMzN6DTQidumqwbgwQ3G1VboIShayvDsjwX4BAj-mTlHbTRnCi_aci-kbC3tL1_3-DdqQYDD3wHanId7zpqMsRQRHw7u4Gn2R3aecYD9UAtj7gvfLpq18COaH0gTPYbuA6ueno9gY-5OCY41lmEGMKMbNcWjfkJqZ5pMdSgO1DzB4t9q8h1DM_PVS2CFjZ3dzJg33GLhauiNKONsFjhnA5t3MtVFoo3ePKHlZiCh-v2q5da8Bqgyx_TZvIpcMB7IfoyBWEHCacX8ewyIvupjYqgGfV2kYFNtCuISK0XnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMJQ-kfo8PVyTPK36-J35s4urWXtndSMFJewdF9adiEaOTxjNKaXyhuaHJqg49uExw4gH4445sW38A33A0B4QcWHS3zNYkT369oS8xdda1nEKrs0AT2u6kelM0T2AHEwA5_qc4JXCObsuHAZaUkSYqoR9-oXf2TrNoy-9IIq5vfQPkMSn_m_aiWuPGRbC-bj4SipeNmTj0Yx394bti493-ekgeiC0uixjFFZuV4qAElZl3mF9yki-ooYZbQxgB6Rh4X0f3Bnt7-tD9qyRM5aR2BWKnDPBEdh77cgyowsVtyQGNvVN1Wb2d8oIVlhKwIFEa0tGzhu_Ke08XKizCbzIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تعویض پرچم گنبد حرم امام رضا (ع) بعد از ۶٣ روز @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/456335" target="_blank">📅 09:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456334">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902855335a.mp4?token=uyOyII0bOL_E44pGPBJuinqssf41MMT4jRLoZVoY6KWy9_rVL55YjrxgwvtzkWxj9WX7QaKmmbn9R4eMIQV71Nv7tTCKkh-zOnycgUkI88-27C6XxEO2GJ785QcoSGhpxpDv29MOZGvZxOCCg-V_Xz0MfO7cA80WiccmFS_5S8Go6xeAP9s-PEcef34S298mpUoLH4RHByqFVwTJK9PfObSdvBbqYlUoxyPWxTHCWX_l8wnHhLUEHWowtY5jNoPoBqE36uLSDVr_PehdxXGkoKRHRUjUCD7eO256BJFwtaud-4gA4HIM3CLNjPM_rpA1rOWhncG7KkvwoXxsbwsYbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902855335a.mp4?token=uyOyII0bOL_E44pGPBJuinqssf41MMT4jRLoZVoY6KWy9_rVL55YjrxgwvtzkWxj9WX7QaKmmbn9R4eMIQV71Nv7tTCKkh-zOnycgUkI88-27C6XxEO2GJ785QcoSGhpxpDv29MOZGvZxOCCg-V_Xz0MfO7cA80WiccmFS_5S8Go6xeAP9s-PEcef34S298mpUoLH4RHByqFVwTJK9PfObSdvBbqYlUoxyPWxTHCWX_l8wnHhLUEHWowtY5jNoPoBqE36uLSDVr_PehdxXGkoKRHRUjUCD7eO256BJFwtaud-4gA4HIM3CLNjPM_rpA1rOWhncG7KkvwoXxsbwsYbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیویورک‌تایمز: جهنم در ناو لینکلن از روز اول جنگ شروع شد
🔹
نیویورک‌تایمز گزارش کرد: کابوس ناو هواپیمابر آبراهام لینکلن از همان ساعات نخست جنگ با ایران آغاز شد؛ زمانی که موشک‌ها و پهپادهای ایرانی پایگاه بحرین را ویران کردند و با آن، ستون فقرات لجستیکی ناوهای…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456334" target="_blank">📅 09:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456333">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca8d3f6f8.mp4?token=Ia6bJZ0HHecTOSxaOSJAjIlur6fASImsGwD7FOWpr73laom3Zolls3b0nztrlZmkITe4z-49TRyEg3IYJtboIZN_pNrIkMP3L-9da-k2odAAwPuU0hY50Jgc-yFnW1ToulHbuw4F3vytHVBVXhtJ-xPDZQnpVBttfMdQKGnxMRcBiNW7l2pXX-LyYFN9ajASHQd-g8Phf3B6GSXZLX5dkkBJTIoen8K00t9mcPrj0NJFkDSnVA3TcLSKfsm-xqpC_44aHKLdO8YPJ6bNynmVF98jJSIdah0AQaktPz_FIBhlZ2b4F62PxGU6GwPtUh1xIdu6fg-0RmAkzR5vPkBHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca8d3f6f8.mp4?token=Ia6bJZ0HHecTOSxaOSJAjIlur6fASImsGwD7FOWpr73laom3Zolls3b0nztrlZmkITe4z-49TRyEg3IYJtboIZN_pNrIkMP3L-9da-k2odAAwPuU0hY50Jgc-yFnW1ToulHbuw4F3vytHVBVXhtJ-xPDZQnpVBttfMdQKGnxMRcBiNW7l2pXX-LyYFN9ajASHQd-g8Phf3B6GSXZLX5dkkBJTIoen8K00t9mcPrj0NJFkDSnVA3TcLSKfsm-xqpC_44aHKLdO8YPJ6bNynmVF98jJSIdah0AQaktPz_FIBhlZ2b4F62PxGU6GwPtUh1xIdu6fg-0RmAkzR5vPkBHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعویض پرچم گنبد حرم امام رضا (ع) بعد از ۶٣ روز
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456333" target="_blank">📅 08:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456332">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2a636165.mp4?token=vEbcWCCEowS43FxhHMyZoQRZKzh3iYb3z2JN4tCQr2TKqZDs9sy1bSEU8mM0zfJlKn956JefX__oaLojaWOoc1nB1syPhZtKlDuTJhZ2OZMMJdIEelkNj9vZ8R80AX2dkmP9iL7vjurp2sdV11NC5HSM2GIMaSRcWXEvSEUKbQ3QpMqStX_uL_0DdxES5GCQ1t7DiWeoOmX-Rj7UvTCKOtDpNDe21I5XPF4jd8JbDmwHpYUK6jml3dr590ezjP_8BA5hVmjr_o9p0aqppikSl4eEFMPlcoyXsNU0AY7cobMJtN_-Ms4SmJEYrpr40_LJGNIct3AmgHr6vGPeydyWuzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2a636165.mp4?token=vEbcWCCEowS43FxhHMyZoQRZKzh3iYb3z2JN4tCQr2TKqZDs9sy1bSEU8mM0zfJlKn956JefX__oaLojaWOoc1nB1syPhZtKlDuTJhZ2OZMMJdIEelkNj9vZ8R80AX2dkmP9iL7vjurp2sdV11NC5HSM2GIMaSRcWXEvSEUKbQ3QpMqStX_uL_0DdxES5GCQ1t7DiWeoOmX-Rj7UvTCKOtDpNDe21I5XPF4jd8JbDmwHpYUK6jml3dr590ezjP_8BA5hVmjr_o9p0aqppikSl4eEFMPlcoyXsNU0AY7cobMJtN_-Ms4SmJEYrpr40_LJGNIct3AmgHr6vGPeydyWuzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رانندۀ خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال «شهرام صادقی» در حوالی چهارراه گلزار کرج، پس‌از حمله به مأموران با خودروی پراید چندین مامور را زیر گرفت.
🔹
زیرگرفتن عمدی مأموران نیروی انتظامی که باعث تعجب و حیرت…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456332" target="_blank">📅 08:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456331">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/461a1510f6.mp4?token=H8BhpQ3rEPsvyRFESRCK2Q_GaYJkv3SD_1QLS8cR0lkqIb5CC723QezX5Ezy7RqzC9L6vUhqR1sNNRyOoeSes9raL9oWYZyDgUCmjnKHwAPSKimWXzRmtvtvI52mXcPZoniFz0U3MzP46-0fa3sz9UYzrF1rLhu47zz6cG67g9p7534sc3blrx7SWJn355PgvVTS1spHFIl-0WxholBRl_eA_cSTIdqoZG1oshRz0mLyuZA-nXQOpycS82rLZ2g_PwPsGMZPa3iUeP023YBBy_77YyCaFOKJkz9M_35w13VGa6kpTqyh2-L_qhXp6oFJcAExTeffqVYrSgMNeiRUwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/461a1510f6.mp4?token=H8BhpQ3rEPsvyRFESRCK2Q_GaYJkv3SD_1QLS8cR0lkqIb5CC723QezX5Ezy7RqzC9L6vUhqR1sNNRyOoeSes9raL9oWYZyDgUCmjnKHwAPSKimWXzRmtvtvI52mXcPZoniFz0U3MzP46-0fa3sz9UYzrF1rLhu47zz6cG67g9p7534sc3blrx7SWJn355PgvVTS1spHFIl-0WxholBRl_eA_cSTIdqoZG1oshRz0mLyuZA-nXQOpycS82rLZ2g_PwPsGMZPa3iUeP023YBBy_77YyCaFOKJkz9M_35w13VGa6kpTqyh2-L_qhXp6oFJcAExTeffqVYrSgMNeiRUwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی کور در آمریکا؛ کودکان ۴ و ۱۴ ساله در میان قربانیان
🔹
در تیراندازی عصر شنبه در پارکی در شهر لکسینگتون ایالت کنتاکی، پنج نفر هدف گلوله قرار گرفتند.
🔹
پلیس اعلام کرد چهار نفر از مجروحان از جمله دو فرد بزرگسال، یک نوجوان ۱۴ ساله و یک کودک ۴ ساله دچار جراحت شدید شده‌اند و حال آن‌ها وخیم اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456331" target="_blank">📅 08:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456330">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ارز اربعین ۱۰ هزار تومان ارزان شد
🔹
قیمت ارز اربعین در سومین روز از شروع فروش آن در بانک‌ها به‌حدود ۱۱۹ هزار تومان به‌ازای هر ۱۰۰ دینار رسید، اما همچنان حدود ۴ هزار تومان گران‌تر از قیمت بازار آزاد است؛ این درحالی‌ست که در اولین روز فروش این ارز قیمت آن ۱۲۹…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456330" target="_blank">📅 07:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456329">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVHDkZEX-6QB2srcFbumM10QkkZixMB7AsOFckP0KDwMMRhxFuxnXgnx7YSPHYPaCrW_j3lTNrpqqT_G9rprZH1j2tmYiQyoZqHAUXy8l9y-FZdwtGGb5PN7GhfifVpmuR9BQ8dI3ewd9CvBRdYgKCOnwaeiUpnd1Aq_mPkPQ92nOTQPmrFw1jbwIiM_hdaieAYBoezyKNPhPDHBusCGLxz8c8fHMdf8esqlKSKTlrVxFy24qYrbFpdb55e_Os3ZQDFOERj_GtmUpwkiFkejrbmj9ogd79btTmOOcDSVDUEkiSaLpXmozss-CcizR2sW7RElpwyj86A_5My9Dk04CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای «قابل‌قبول» در پایتخت
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص امروز کیفیت هوای پایتخت روی عدد ۷۶ قرار گرفته و در وضعیت قابل‌قبول است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456329" target="_blank">📅 07:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456328">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3A_OgquxkTitoWe03-40tcphafZ2t1YNTwpLRjz29Syh4bPC-KvA-5O2f6w5V5FcasQOHtVYUfkidyyN2SiPxtvE2POejj031HAnteZhqfRGxpM3GJ1lhtwuX3vxfy3A-begrfGH_bRPFznr7yYK2WG7-gc0UOkxDYOcxAEpuZzS8e8wxFOXFtKZp94UIoyNXvOp8oykMw-wqaZqMjl4OaTFpt0KHfIOgObNCMHnT9mwySFJFx19iyrkOK1dUOHm6EpCNssshFYdlWqHwAEklHSru7upVqjtbbg6LxayDS0ktNOD7loyTFStk4MvJFClmrALZ-6XdekbIUPMDfGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رانندۀ خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال «شهرام صادقی» در حوالی چهارراه گلزار کرج، پس‌از حمله به مأموران با خودروی پراید چندین مامور را زیر گرفت.
🔹
زیرگرفتن عمدی مأموران نیروی انتظامی که باعث تعجب و حیرت حاضران در صحنه شده بود،  منجر به مصدومیت ۷ مامور فراجا از ناحیۀ سر، پا، دست و چشم شد.
🔹
این اقدام سراسر خشونت صادقی که با حمایت گستردۀ رسانه‌های معاند همراه شده بود، یکی از مأمورانی که برای تأمین امنیت مردم در صحنه حاضر بود را هم برای ۳ ماه به کما فرو برد.
🔹
صادقی که پس‌از این حملۀ وحشیانه با آتش‌زدن خودروی خود از محل گریخت، پس‌از شناسایی، دستگیری و محاکمه، سحرگاه امروز به دار مجازات آویخته شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/456328" target="_blank">📅 07:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456327">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqwSR1iv3rQSY7Qll3VD3ibSVQbnc-q4juNjSxIrvpzjU5UTqDIxJIxY2TtLJJ8q63iUghrMB8WaYT4FEBvqwfU2tTiLFLdM9OBRB3vdO-IWwcLgL0LeFcW0bMOtndstXFn9p2fHmSY52CLMgH3G01EGrQyw7Rc-kYJbOTz8gMVHVpwu7VkcWfdAqW_4Stl3DxQ4imP3lLgoxEOI4osFjbx5k7gvTILSrZcX75cwcovHcpFZXfksnRcmePIakFkSa-eU-ESJjHTiDPOhisZyMugqQfHWEIIkZgIDG3hJZAty1JddImLw0BGd9k_C958L-o65QTS7we5shgw_qV1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ کالابرگ خانوارهای دارای کد ملی ۳ تا ۶ فردا شارژ می‌شود
🔹
پس‌از تغییر زمان شارژ اعتبار طرح کالابرگ، خانوارهایی که رقم پایانی کد ملی سرپرست آن‌ها بین ۳ تا ۶ است فردا اعتبارشان شارژ می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/456327" target="_blank">📅 07:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456326">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399a76cffd.mp4?token=FTvtCWxTwobvSS-XlG5Pg3B7qg-ZhQywXA9Y4d9jm72f2fSTlDZ1-_4y-WekWMGA-aTVofathj2z6wvYm7l9v1wWdl-IlyQ1vVNC-vWP7-ayEOdaXuhrPldPjy32wokxgNA3o2df3QGcWAzmxcXXgL6ZWK2V6HzS5XMtmrQUjqKMWbt6xIKWXGLa0RCxwivzwqJLZYG_jC3483tjoy0Gzuzth2fUgEVT1jxi9dKkD6JydF9jaltiaNotM3Ndnf9kp7yRTSjsS9tynxkCxS-a-Y8az-6atLVescjt_-NlEUfOqnJnWWUb5kf0GCSqhvHJBvTf62l0gbSo5n-eLOfvyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399a76cffd.mp4?token=FTvtCWxTwobvSS-XlG5Pg3B7qg-ZhQywXA9Y4d9jm72f2fSTlDZ1-_4y-WekWMGA-aTVofathj2z6wvYm7l9v1wWdl-IlyQ1vVNC-vWP7-ayEOdaXuhrPldPjy32wokxgNA3o2df3QGcWAzmxcXXgL6ZWK2V6HzS5XMtmrQUjqKMWbt6xIKWXGLa0RCxwivzwqJLZYG_jC3483tjoy0Gzuzth2fUgEVT1jxi9dKkD6JydF9jaltiaNotM3Ndnf9kp7yRTSjsS9tynxkCxS-a-Y8az-6atLVescjt_-NlEUfOqnJnWWUb5kf0GCSqhvHJBvTf62l0gbSo5n-eLOfvyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر فلانی بد کرد چرا با خدا قهر می‌کنی؟
🎙
آیت‌الله جوادی آملی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/456326" target="_blank">📅 05:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456325">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حملۀ فسفری اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات جنگنده‌های رژیم صهیونیستی به مناطقی در جنوب لبنان از جمله منطقۀ علی‌الطاهر خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/456325" target="_blank">📅 03:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456324">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96755745bc.mp4?token=KC42En6TifwnpbIaxtylV5M4cZDjfNnJAKHOnTS7ukrvUoCT8cFeZ6XF72Pd8g6sx1XPi2XGDoyLAwKeC1Ye2_0KbK8ixQzT2Ha3LzXTBDBu8vFH2iCYAzgsym_MvCL92LuxZLGKvlUnsJxClIPCHRWSNAz14MZxIrZvlOXiCFeacsdT8QS78BngwRm_kHKTZA2odaxp-qWNJOWmTdogdz79_B-68yWhc9szPByODMY3a92rII0GdDzHEEaTWgAEJmLQ6Z5TMPEtVoFcomrety3J-sXhBE0O8RoIvzzQIWdcNypkZTaPaftSQKtOoSnbFr-dO7ZnyMzKAsqAhi-6AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96755745bc.mp4?token=KC42En6TifwnpbIaxtylV5M4cZDjfNnJAKHOnTS7ukrvUoCT8cFeZ6XF72Pd8g6sx1XPi2XGDoyLAwKeC1Ye2_0KbK8ixQzT2Ha3LzXTBDBu8vFH2iCYAzgsym_MvCL92LuxZLGKvlUnsJxClIPCHRWSNAz14MZxIrZvlOXiCFeacsdT8QS78BngwRm_kHKTZA2odaxp-qWNJOWmTdogdz79_B-68yWhc9szPByODMY3a92rII0GdDzHEEaTWgAEJmLQ6Z5TMPEtVoFcomrety3J-sXhBE0O8RoIvzzQIWdcNypkZTaPaftSQKtOoSnbFr-dO7ZnyMzKAsqAhi-6AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات فسفری ارتش اسرائیل به اطراف شهرک کفررمان
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/456324" target="_blank">📅 02:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456323">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حملۀ فسفری اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات جنگنده‌های رژیم صهیونیستی به مناطقی در جنوب لبنان از جمله منطقۀ علی‌الطاهر خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/456323" target="_blank">📅 01:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456322">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4d889ef5.mp4?token=uiy2Q-NdE07jEfA28h5FcQZYxi2bUj7l0pTOppbt9wmULzy5HJ_wjeafrpYwv7DHalGjtezRdxuNP2WZtIW2kPdydRWCv7bGrDJ4yIp6MM9GRK2Rq1Z-D8V0-t0tDaJtmpYqK-aZ8vmWW7GnYzCsqXe0SXRKdI426tjAFbtg-5Gx-uLZLZsZk43zySYWCgh4uW1Sd_GPF8Tadqb6ysTskvs3cpKdJMDgqxZIFWgfOjax7BHaROec8cNDO82uodIREgNUZZnZUaM4WszmWVaA_fJGocQh7qoKr5dF8S7ta0sg9mB7ls0s5NNb2MLd2N9C3ZCMZLUGOE-Fgnt9D1uMVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4d889ef5.mp4?token=uiy2Q-NdE07jEfA28h5FcQZYxi2bUj7l0pTOppbt9wmULzy5HJ_wjeafrpYwv7DHalGjtezRdxuNP2WZtIW2kPdydRWCv7bGrDJ4yIp6MM9GRK2Rq1Z-D8V0-t0tDaJtmpYqK-aZ8vmWW7GnYzCsqXe0SXRKdI426tjAFbtg-5Gx-uLZLZsZk43zySYWCgh4uW1Sd_GPF8Tadqb6ysTskvs3cpKdJMDgqxZIFWgfOjax7BHaROec8cNDO82uodIREgNUZZnZUaM4WszmWVaA_fJGocQh7qoKr5dF8S7ta0sg9mB7ls0s5NNb2MLd2N9C3ZCMZLUGOE-Fgnt9D1uMVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمی‌ها در شب ۱۶۸ به‌یاد شهدای میناب به میدان آمدند
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/456322" target="_blank">📅 01:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456321">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFEtBG6Zcpx_e1olZ0dzAfpCJJMUjWO7Knacd9mSQvoufWgsVCF9VIZss73icMnK_LOu1R73rhkTBk2epwpNnoCHdPFF_I7-EfpPKpqwLSNN_lvhukcAs0bm6dBL8QrUGvrav4wEC10LTUiUr7RK_d0Rb9yx9MHSwA6C2XaD1-2Nr5cBt-TUWE2f-ZcPVF3EKjIjxvDICeJkorNq6q2lXS7H0BXTpb0VXsIsjSWE1R3k5N2JUp8IY786eBQJRfeSPTAWCJswz_-JFNoZTwMD_KYB8eEhsNyZxx8oKPIlTyAOoUWEDM0XmgM1iY02uS5NKXdf1EOB_zJwkRV0bw6KZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا درهای اتحادیه اروپا به روی ترکیه بسته است؟
🔹
«رجب طیب اردوغان» رئیس‌جمهور ترکیه روز شنبه و در گفت‌وگو با شبکه الجزیره گفت که عضویت در اتحادیه اروپا اولویت آنکارا نیست و در صورت نپذیرفتن ترکیه، این اروپا خواهد بود که متضرر می‌شود.
🔹
اردوغان گفت: «پیوستن به اتحادیه اروپا اولویت ما نیست و اگر ترکیه به اتحادیه اروپا نپیوندد، این اروپا خواهد بود که بازنده می‌شود.» وی افزود که کشورهای اروپایی تمایلی برای ادغام ترکیه در این اتحادیه نشان نمی‌دهند.
🔸
اما ماجرای آنکارا و بروکسل از کجا شروع شد و به کجا رسیده است؟
در
این‌جا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/456321" target="_blank">📅 00:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJ5liyjkor4sRCw4Tr4uHgvckA85PyG9CnUAk9g1Ljsd7B-70RUTaFJd6AQ4sYZarskGY-CRVlhDZqPAP-P50MpQHm_qHmJ2LFxYLVRBbas8faszk70nFhh9xFmXrG3bpRJNqUaja-YQcDv8xNnhOkVwbcsVE_EPGld2JZvnsFUJOFIr6C9Rkn8gkd3lp_sdvj1fuxZO4V9rB8vE96_CZ_DHliJwp68MCdK1-PMQ9b5B9VeI3sAbHdqM1JsF1BzIfJzz4X5PcG7aDKk9ewJ8bYujZDpvpRhphHC5a9P9UO1a35obQYTR9kGMGjlfO3VzTLh2b2uCYvsCTVnrYi5bTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuDa-DoymBHxRyRY1xCKd9fwelc9UPHjUe6_WLgjEkHfTOQmLdGTFPWe_iVQemJnfx4SMJNNJtm503eoeci5imFVJhbM0Krevy3acYvB126O682F7B6UtuDaP1EA3JL5v4MfJX7L4JBmmjzXdNEY4HpPttP55elkOBUAkV3v_C3G05fAIhjhYn41IlUsFRppKuE6Htvz3i0J0VeGFjYXsQYH_ViWSl0VZEgD82WNNZuSe7qDPPmjnMUM5RA0Ov-POVpY-s6Feu0x106GwXsxdzDPYqJUVJfBY4kJGyE9mxaSvMc3XYdA4G2xmdJ5dYF8N3q7w6p48we6YyefXLtsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgmUYk5HTlk_SstJ493ClnUCprOVCJw86woYUYUwpjxJiweKULg9lBkugftA8514_hKVo587H0ADbXi2FAzDKZRQOGkj7EeijiuoGa5uAtpx6DRAVRc-gcZrkzzVdq1jDefh6xEgUaibYdSXSSRfujFhEEC_t2K1U_WUXDS2ihWYuQi9JH4NcCe6P-BvqgHh8KrmfVpX0o66PHNdCONTSW_LoKt25Mua79UtR9lMzqF6Gr6wMUE0oHHy9xIMAFePNH2tOr5KXHe_onsmJM_1kjiuVKc8YmvDetQo0crGhim0uMQQU2Q0hF6kEpexDt3UK--9vpmNkKZQp9oYzohVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d82UjF22_-EidXQBfL5JrchqB1O_hfgk2rmRPbYKaCLil6JwtHtC5y1Tac0ZTS_Uuq2NL4EAJNErPaQsPGfm0YUi8lXWpwRvKXRAZrJJmmL7enmzluEzctr0hX8RMi-E15YP8UuCYwfe_R_jbqy4zuksT1XqBx5cVoQO68c8OdFqjGd0sd0cn37O-7B2zFM6ijWUsxeyOsWAlq4hLda8Gzcc_vdIKrNbsmRcgdTceoV6kVxMba4Lml4c0Vhav-bmSR_0LvWF5ZpBAs4FwWwWX23A3UZu9sVcijZIrFaUnExQYiuy0vLg_Uiu9jXlux1Ucow3J9tSoQgANr2buHGf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4FWHYwWm_y73hR2CuTLtVfgHY4OslAYiAOv-pyyJD5m-KqD36TtocQTsoPbGw45lIvE2WSKIPjX7ShpwP50A_z5-z_VH8VZcioXWOF5lC3SnV_MWmaKCKwo69JXtFdqo3I62t5PhjlZqPqGAEZgQbhept7QZiIuRaeVcB7K6fguTlMWHKkr0baxfP0pn5zvwd4SVGPvxhwv-TrOSqsgXQWQcKtkdyVu3qSyZr0EbTpKBu4EICzNBu0KEOmj1dk3mDNljiYqiwKEeUA5APAJeGLnWAk12rnXaMfje7sJA4zPq436n7FoEWafTEG5aBbpSaAvHRu4JWeji00dVgxUYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۲۵ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/456316" target="_blank">📅 00:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456306">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGxbWC1ceWPBECmshJyteT6YzRN1Ly1_D_Nr9ALg5fzP4gh_TpoYzPaFQYH870lysRUn9Yq5V-UbQllcDywntNCl5GE3Bxxv9AXeHo-h9g-kYF6XDhkW_L5-8x07Vu5mrHc_78ObH3i4DsWUfGDaBA319MME3eWl0GKS-kXp9dreDCaErLBWrPKb1gBclHaqlF9kD58TS8fU3aa30uHIKtZmyWSlv1rxNUVZr4qe4JrcErrWbeYsnWe5_TrjMrtiDMZIQ9zWfgXlMQl6AcruQYPqwgaNX4tRlDEbxrwBTU2Yw1T26hcjaCcg-BZpnyHbr7qHeGf8MM01xl5xlZJ8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K30j0IRyNSBt2WnQurYyKqO-gpR9MpzswaxMmevj9jVas70F2SdpWhiA3x7KrrQprlHWT2xAl0a1cRT1vl72ph80trgZgFdm0KB-7yZxFdAwC3_W26SpJk4yaU028f2z8NgDC0VGKCDFG9sxlGHm6744koFI-JLp5KduhaPMFq9OaiVUwoss5RV5_zXCU2j3KRR64Qh-0fdJXWZ3NUJFIVZG93FCTaZDfCGUgg_bmuG9WkYl2XT0hbGntocWzW8oCzp_K8bRAlftNsaFhJ-CkLeDqTAg8rSdoBr0G-aE1fG9R5ugGGVqem9BJKC2iDXnMXMUU1WLLKjUlAq4pPy_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRUANmJqtnyeZ1P7AfyKcTqJIdUxCMcysBbOnxGM7xDuWP4vQkv1Xdoq7eGULjVkj5a4I_xkO11FKCC3XrxW3FwxEUiwQep8z1CyzpPnlHim8rTduVvvnDDyYRb_QZEiAt2cVDcofTTlWBmLDFAlwlkZsWiVZVUXzMRxrb_0i9kJR5DMZJtGseLJKp5GILfI3ImU9ZAGwqDdLfd-c581z9on5GeO80mmCqRFjbFmzbbjo6kCAbWs5QMF-po3zRWTJJ8-dOEKZQtHkTOua8p4UR4N0lWtqUQFOCJCMXzt9PccqEDGlBJyS5YGQbPA9G0IniS1v6Ll5uWVTVk8c9dPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7dDeVcF2F2SmkQMSI1hZ5p-sFyOvpd6Mkxo1az8SswZJwuNolJ9BsBMFAYKZa7X81Cs1Y0YCIOMnAgiA8fjxp2lsLctwNyk8aYxszmJTHZDvtLspLkRY52xnGYQ_Sa8XG9dYdZlLJVdK5Sjyy4b367ADkph3WrffMsyBCYCEtsYSpRu-YPGVBURIKZZqSSY-LtqlALYoncpkBHLdrAs9cf_HYfVEOFLHninJMErkowhJBR-0q_jCeB9KmixKqMqnrNBv6cKrlONS3FtlHjmgVUjlNEceMKClsc-OOodAKI0Q8yz3vp_3hVwZVbqcO5WueGnDTmUToskXs3_TMjqMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQyu0lruW0pG0UO53dYfCarERTkpV3HnWBkURJK6TWHDlH3TedbiH7Y5JgiGuFJxBKCZriM9sAtwfM7mOCFqnSL_xz_SyqA0QX3vb3SHaVPBukqBXgjOc92UQKk3uETSPsgR-OA8W1Rd8fYVRifejsRP4Tla6hmxXXKkJ7JrR8QVWQqOuNoW5gGHIEzQy0pW9vhrkjlGC4u87qgYq3JBzvZzD8_xOl18wT6bCpdXuWHGtK25fRmS8muQxTvMy7XFbKz-GDY1ANws7XFxangyGOK67pkVuH-vwARJ4nqOKN1pZK6j6gjvz6n05uYgmKUKuHtDNFUzdL7GpQMicrcHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z41_DZ7PunuiAzdbJqzB0_y2e509-d4lFNU6RGbJ-Iw1KVG93DE-f289rMqUBnmpBGDg9y1ejTEyvIcqFyYt7wkl84kg34Q0SG_ktUIUDjjRecda748DSya-rTW3Dh9ks-8nxt-rIq8EEOV7tQZN-lGf77yh55jNiVK3hV1FJqE24ofeIn5XY2EeX17WrE77s1fZIzkAz1Jna54maFil068Y2LOm-xMyPQw7SMsexC2OSdMCtekw3Vlam9JJW7VgcYSajiamYrzuWS7Yy9kpE1CGBogzIXiKU4VTCtsd4dJS5PJj-e_6IjXScNOaNe17-93z0hVVXF7EVIDjbAwTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaiZ4Uq1W0_YcprP-1S0LyoTFEejmdFZfBXuPjj-iU0v1DiGIFi9Zjh_1qqS701ie1K8-YVSGLDTwS0kcw9DBSNAGb0OfVWOFMLyWE-jFzz2yEW2_klao0PGi3udCsjTokXrI5D4VsbpLMHkgwqYyCv11e4RQr7uQgc7puAq1ituLJpRJpeE_CxFEos_ylrEYZTQuq7qGumT2HwST7TBeiIIYQYF989dy0FsLz7O0ah7l4TVJVHeflpT6WSbV_OGlr3zsO5pigW5S3tlQ0Fj1ZWtkPuKllua1_k4SqwsZvUWIgL9xtQhdMhf1wV9mH6_FB46zOx0tDy4Snjkxox_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XB0R4gyCkdPVDOI21S40wtspDpXpwiqT3COKd99oL5omZS4dsMXQefynJRJKr-rq5hbIv-OwzlKWcupF4lO-86nmKw5uPX6fpFV3M-klIIHR8r1vlql7HSuSYEf8SzH1I5i5wchVbHy7NxzkmYxqyVfQY_2E4-Rife3qcvzyzmiuR3KHp3R6NAmadYo2r3G8CmAwOks0FJfT1XfO0C4DZGxfNch3Jmu3VPlVL1Sqfp6pR9zyJcZ8b810qv2e6EILHrhl6SErPy1Y-KddTmX1taDt4vgfhxn90llxyy6B1--VT0-1MXHPB00INe1vKfyIyLW0nMKCYz5Zogw0wxCA-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mu5zFn_YGPjORQusaaaTv1YVgvztBLNumJ71VBmk1VFpQX1U3X5jiUWDsZBy7_nP_OJCtiiFscefP-jYq5NuV8I3On0iXOg76gSo_Mt5eoaWvFrxpuGvPQ4iOIC0I9FJ03Pt_UqMBMw_J9lAUiA2aaOXVqY4apuRqDMhfhdDINy3gAinLQuL37IT5xrFdLV5rRWLqKKKtHXde6Jm1dEHCxJ_0-VD15Uz9b54Ev52gSINdS7oqmXzGEbtfjEQMi7oW6zum9gJ53yxCVR-qKyG_C25h6hEs4JPxf7W65AfixnIfmNNEwKftUG9oXjhHIhkpcC2F1NiLSYZLAN5-bgcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noQaKmJBRltXbSqj9o90Q-osuiRIdEYFyiPvYbt6jHvD5zDgK5T_hT1y4vfEA-OVrSoZ76WmiRdKr_JN7KOlfzqAFGVf1LMupwDEjtAm-dIuE9rvzH1NtAxlmr1eJvin_BQbChsr9_WI39JkGhIEV1bhQR8U1zeUW8cMew4mBgXyUiM9718lKPyFKzQmBCoVhZ1hk2dZdyarha8dFkoRipjMP1k29sXan4l9QxI03R6_QF023t5koQbKO0hRooHAf3K9x0jesTbt-k2JmXshSvr2914QaIKyoCiIhcLKPQJ5YIXvP-HgyglNR_ehqdEs-ROUsMtBoGcDqaVuMfbqJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/456306" target="_blank">📅 00:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456305">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4125379ad.mp4?token=WzCuEXDevOS3qd3KLWX7CRXbElQa1_mY8dl4rcXpOwKvY0mA4Wn6YvllMJYVOb5gNlnfzETuZLK4nR49nNIc1UszBmHJuYs8j1HjbnirkwwF7z6jRnVbyzwtqqoo-Sl1MnIlPPczmKcr7SGdzkYVgTxdrdayepYWg3UGHnuZ3h2cTPwLWoVl987MFQ-heLcEQ1_3gnj6StnF6KlPl8aoMwVewtFV9IE9ukjFzh1241E-g1zFVwCgt3W0OTDIGtlev7RDLYE80pIZYneINR30K4tqd75pLqZwTitNWZdIeSw4piu9LmnZVJbaq5-isRB_hJusYbBC9UNhosxKARYZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4125379ad.mp4?token=WzCuEXDevOS3qd3KLWX7CRXbElQa1_mY8dl4rcXpOwKvY0mA4Wn6YvllMJYVOb5gNlnfzETuZLK4nR49nNIc1UszBmHJuYs8j1HjbnirkwwF7z6jRnVbyzwtqqoo-Sl1MnIlPPczmKcr7SGdzkYVgTxdrdayepYWg3UGHnuZ3h2cTPwLWoVl987MFQ-heLcEQ1_3gnj6StnF6KlPl8aoMwVewtFV9IE9ukjFzh1241E-g1zFVwCgt3W0OTDIGtlev7RDLYE80pIZYneINR30K4tqd75pLqZwTitNWZdIeSw4piu9LmnZVJbaq5-isRB_hJusYbBC9UNhosxKARYZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار صمیمانۀ اعضای ۲ هیئت خبرساز در حرم امام‌رضا(ع)
🔹
دو هیئتی که در ایام پایانی ماه صفر در نزدیکی حرم امام‌رضا(ع) خبرساز شده بودند، در حرم‌ رضوی دیدار و با اهدای گل به یکدیگر، بار دیگر شعور حسینی را به نمایش گذاشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/456305" target="_blank">📅 00:16 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
