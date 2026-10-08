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
<img src="https://cdn4.telesco.pe/file/hgceMWAT122iPwAdIOtCRGVtVs7losBDqiqgP5xPJ8YosinKnAHbZEbbnwvSZX8_4YP8CksmxwuM9arcAYgHRYdyqxsgtpJrMK6YNf81evqxdCNsmhfj-e4uXZnqHc8UNIFqy7hsOQgaAFAK79xmNIwWGSRVCBYDzwJdwB7e7xL3HQDItrN3w_cmqqApcpJ1BqhrWbaQ81yG6R2TtikLvQXYxK1t98y_iYf6UZdqTNKsu6TSOUi_OT3KjC6cRABUlIGluyMgza3pbe3TUX_MZIAFYl2swIiHVetGRCXXbRl5Ne8J1RZMez7Ha9Ki19YQCgH4GzrifqCSQsXKTHA3fQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-25198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش ویژه فاکس‌نیوز : گزارش‌ها حاکی از آن است که پنتاگون به «فرماندهی مرکزی ایالات متحده» (سنتکام) دستور تایید داده تا تدارکات لازم برای عملیات‌های رزمی گسترده و حملات علیه ایران را نهایی کند؛ گفته می‌شود که این برنامه‌ریزی‌ها پیش از انتخابات میان‌دوره‌ای…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/25198" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش ویژه فاکس‌نیوز : گزارش‌ها حاکی از آن است که پنتاگون به «فرماندهی مرکزی ایالات متحده» (سنتکام) دستور تایید داده تا تدارکات لازم برای عملیات‌های رزمی گسترده و حملات علیه ایران را نهایی کند؛ گفته می‌شود که این برنامه‌ریزی‌ها پیش از انتخابات میان‌دوره‌ای در جریان است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/25197" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا : دو مرد لتونیایی است که در نزدیکی پایگاه هوایی سلطنتی مولزورث بازداشت شده‌اند. پلیس متروپولیتن ابتدا آنها را به ظن ورود غیرقانونی به یک مکان ممنوعه بازداشت کرد، سپس هر دو را طبق قانون امنیت ملی به دلیل ورود به یک مکان ممنوعه با هدفی مغایر با منافع بریتانیا دوباره دستگیر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/25196" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/25195" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی آمریکا امروز در یک نشست مجازی با شرکای بین‌المللی حمل‌ونقل دریایی درباره وضعیت تنگه هرمز گفت
افزایش تلاش‌ها برای تضمین آزادی کشتیرانی و تردد امن کشتی‌های تجاری ضروری است.
دریادار برد کوپر، فرمانده سنتکام، از حمایت مستمر صنعت کشتیرانی و نهادهای دولتی آمریکا تشکر کرد و به خسارت‌ها و فداکاری‌های خدمه غیرنظامی در پی حملات ایران اشاره کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/25194" target="_blank">📅 18:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6hnJzi0fq9Bsu6VaVdDxk2OZCdD5G1nxVDZ4vpz-gjviJn7sgDeUv7nFFoGBcQLIbA26b_eAWLINfrXsSSGMPDrYnLDCZJl7Ht8lN1vMMpt8uBjJkKc0Wab3bK6rPweL8OiucVA5GOg0ga3L7n46vaS9IFCuAITS5w-sKO0XygPZIbigmse_d8w6YCMgQ1W2mpQzJiIh-zGLDuioDZEVeEg7mFnV--ri2m1xVEn2qb-g1nJp7SjmLLrTuAlzr65BIPMAaJyHdmbNmSm1uYAWSdLUmqEqU1G1yH3Co0K7htiJ7tNXeUhL-qaPexkfCckhd7SWAx8aD5FgU_akOcrPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان نظارت دریایی بریتانیا (UKMTO) گزارش تأییدشده‌ای را از یک منبع معتبر دریافت کرد مبنی بر اینکه یک تانکر حامل نفت خام، در روز سه‌شنبه، هنگام عبور از تنگه هرمز، مورد اصابت یک پرتابه قرار گرفته است.
هنوز هیچ گزارشی مبنی بر وقوع تلفات انسانی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/25193" target="_blank">📅 18:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/918015a856.mp4?token=DoYc3_WSlNFDWopqTOLTWGfEY00By0thoj97_RavG1v3iyZbkJZmWpYZEEcyteJWDldUjXU2h85AgwY95_IJzYio510W4t62BKRZjAK6ZwH9zXr0B_jMLjBvgrOWYUCknbgGE2LwtnaLZvdfNz6IfbI6QMZ94rxGXp4zhxn9fD40pwDS4FZdPcUcuOJGZvXDW935u-IMAtBVJQbIXep80cvJPMiDEQk-f_PZJZ3WklR2FSA0DYMm0MnwQRLGRcVd9E1AE2904ddvtufDAQLeYGSHQP2K9PUCSqFNPWu29lsoemFUeC7vARi5MbV5wWqlLOcb8L3ou5xq4EtrlPDOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/918015a856.mp4?token=DoYc3_WSlNFDWopqTOLTWGfEY00By0thoj97_RavG1v3iyZbkJZmWpYZEEcyteJWDldUjXU2h85AgwY95_IJzYio510W4t62BKRZjAK6ZwH9zXr0B_jMLjBvgrOWYUCknbgGE2LwtnaLZvdfNz6IfbI6QMZ94rxGXp4zhxn9fD40pwDS4FZdPcUcuOJGZvXDW935u-IMAtBVJQbIXep80cvJPMiDEQk-f_PZJZ3WklR2FSA0DYMm0MnwQRLGRcVd9E1AE2904ddvtufDAQLeYGSHQP2K9PUCSqFNPWu29lsoemFUeC7vARi5MbV5wWqlLOcb8L3ou5xq4EtrlPDOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
می‌خواهید مشکلات را ببینید؟ بگذارید به لس‌آنجلس حمله کنند یا به جایی مانند سن‌دیگو. بگذارید به یکی از شهرهای بزرگ ما حمله کنند.
به این می‌گویند مشکل.
@WarRoom</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/25192" target="_blank">📅 18:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4309370e.mp4?token=WPe9EWJq31TBcMOJtWcbn3Fhoe15aWsx7sEX9aJuHYqnbsjB02aB8b9BE9eb7PsEyAuRpsCwwx4Jbyf_6tRDN-js0pb_9TBioiu-T7z4-BSnMjHNXxuTlyETUPx5hiG9yzZYdFuwOb7cSNfrpCUfsajzeEBZ-QI55LHgHIjUoULLq_IZLIu0KRLk4vUPp0oRZjyvXNUY9lHSTT54dgqKwdnee1VlSsplmoxAgxhyJRPl3MaIn6oadYTbQRI72EQnUJF7J9AdnJ3Rm5qZByjjIjcvZqYfQqIzEv5iCydNZf9gsjoMnfmu9eybfTADNfKVvCq_jKAaJ8dAVR2fOuJU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4309370e.mp4?token=WPe9EWJq31TBcMOJtWcbn3Fhoe15aWsx7sEX9aJuHYqnbsjB02aB8b9BE9eb7PsEyAuRpsCwwx4Jbyf_6tRDN-js0pb_9TBioiu-T7z4-BSnMjHNXxuTlyETUPx5hiG9yzZYdFuwOb7cSNfrpCUfsajzeEBZ-QI55LHgHIjUoULLq_IZLIu0KRLk4vUPp0oRZjyvXNUY9lHSTT54dgqKwdnee1VlSsplmoxAgxhyJRPl3MaIn6oadYTbQRI72EQnUJF7J9AdnJ3Rm5qZByjjIjcvZqYfQqIzEv5iCydNZf9gsjoMnfmu9eybfTADNfKVvCq_jKAaJ8dAVR2fOuJU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
ما ایران را به شدت شکست داده‌ایم. دیگر تهدید سلاح هسته‌ای وجود ندارد.
آن‌ها در حال حاضر در یک آشفتگی کامل هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/25191" target="_blank">📅 18:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af618364fb.mp4?token=YI4zOvV56XUB5ZPD7gJvgBUDVkMaYbbOnTzvTwXMIoM6UkqJqBCaB8a4nLRd9TdwVXRkYri7cQIX5aBfMf9604CcNnFVBPfnJVMMyyJH7BEFXftbVjv2C7iq-Otz1S42S20_nLI9mRKPExwG8zQbO-hX-zDMyxuC7faFW4VPlgvbHyY5766m20R92iNOZ-zz59km0PZJN8tbM_NYhsjCjx_hPh-9xsIfYxkHlc_i9Fqb8eDB-HxK9fUnS7eg6Wxb1PjQBi2PJB1fyMWBstF5cszNySLkK7O-QyiD6vmqaCcT-MzMckdQrr3lfgtA4RzPX5ertq7mUTWqgkrHyaYmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af618364fb.mp4?token=YI4zOvV56XUB5ZPD7gJvgBUDVkMaYbbOnTzvTwXMIoM6UkqJqBCaB8a4nLRd9TdwVXRkYri7cQIX5aBfMf9604CcNnFVBPfnJVMMyyJH7BEFXftbVjv2C7iq-Otz1S42S20_nLI9mRKPExwG8zQbO-hX-zDMyxuC7faFW4VPlgvbHyY5766m20R92iNOZ-zz59km0PZJN8tbM_NYhsjCjx_hPh-9xsIfYxkHlc_i9Fqb8eDB-HxK9fUnS7eg6Wxb1PjQBi2PJB1fyMWBstF5cszNySLkK7O-QyiD6vmqaCcT-MzMckdQrr3lfgtA4RzPX5ertq7mUTWqgkrHyaYmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
پیروزی جمهوری‌خواهان در ماه نوامبر برای برنامه‌های شما چه معنایی دارد؟
پرزیدنت ترامپ:
خب، فکر می‌کنم این به معنای میراث است. فکر می‌کنم بسیار مهم است. داشتن یک پیروزی واقعاً تأییدی است.
@WarRoom</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/25190" target="_blank">📅 18:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رویترز: قیمت نفت برنت امروز بیش از ۴.۵ درصد افزایش یافت و به حدود
۱۰۴.۷۵ دلار
رسید؛ نفت WTI نیز به حدود ۹۲.۲۸ دلار رسید. تشدید حملات به کشتی‌ها، نگرانی درباره هرمز و درگیری عربستان و حوثی‌ها از عوامل اصلی افزایش قیمت‌ها هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/25189" target="_blank">📅 17:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e36deea25c.mp4?token=WahQbrJUTC7eK1VuAnjZZRDcqXkP9szkFqUxV6KSuebRY8x4MeeJvwXsz25Z16qY7BwjKApQ7Zx03mUitDjrwrW4G8rNQK4WN8WPSddHtsdrm2ZvdvI3EjZ2gqcLmeOLUPxHc1FsN0G1AUlKm6duqFI2c5Clzr_XJFMMFb-OOPdMdMygIv3Y8TtLpaXbea8d6HtIYz00m631ZTaIvDhKYcTXJnqZQ-OvUfdKmFu2cAti_hsoNeHvUvxQe82OobiobSvoVwW6_73qTzx5ApgQXIJJkSdoF3z2DBg4QsLlCVrfw4ST0at14kjWoKiwgNfNiA_iJbqGAa8GRneZ7lDzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e36deea25c.mp4?token=WahQbrJUTC7eK1VuAnjZZRDcqXkP9szkFqUxV6KSuebRY8x4MeeJvwXsz25Z16qY7BwjKApQ7Zx03mUitDjrwrW4G8rNQK4WN8WPSddHtsdrm2ZvdvI3EjZ2gqcLmeOLUPxHc1FsN0G1AUlKm6duqFI2c5Clzr_XJFMMFb-OOPdMdMygIv3Y8TtLpaXbea8d6HtIYz00m631ZTaIvDhKYcTXJnqZQ-OvUfdKmFu2cAti_hsoNeHvUvxQe82OobiobSvoVwW6_73qTzx5ApgQXIJJkSdoF3z2DBg4QsLlCVrfw4ST0at14kjWoKiwgNfNiA_iJbqGAa8GRneZ7lDzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو: حکومت ایران مجروحان اعتراضات را در بیمارستان‌ها می‌کشد
حکومت ایران وقتی معترضان زخمی می‌شوند، وارد بیمارستان‌ها می‌شود و آن‌ها را می‌کشد؛ گاهی حتی پزشکان و پرستارانی را که آن‌ها را درمان کرده‌اند نیز به قتل می‌رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/25188" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز:
خطر حمله به نفتکش‌ها در اطراف تنگه هرمز افزایش یافته
و هفته گذشته بیشترین تعداد حملات از آغاز جنگ ثبت شد. ایران به کشورهای منطقه هشدار داده هرگونه تلاش برای ایجاد مسیرهای جدید صادرات نفت در اطراف هرمز را اقدامی خصمانه می‌داند و احتمال استفاده از موشک، پهپاد و قایق‌های نظامی برای جلوگیری از این مسیرها وجود دارد. در تازه‌ترین مورد، یک نفتکش شیمیایی در نزدیکی قطر هدف چند پرتابه قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/25187" target="_blank">📅 17:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548fb32aef.mp4?token=aPSv8MEITAwkqPYT8-p7eKd2rCYe9T7as0zM4uUiju0L9yapwYiB4e6fHlot8yjriAkSlH4bl1kFcO2LottfUho8Ex-Yrf2I1tUuhdR0vqEF8PeUeQ1BnsY7-69v_lyHzAVK1CRp6jYZLHXy8_c2q9SjjfmKCUHftACdkRDPJM_p5ZcCrLzaw2u-AA3r_CbGMf6E2Gc8BH1n-Ikrgew0naa4yixoe3m-BWZb75cHnuev9oV8wrUseluaFzl6pqADha9ldullUIqqnoT_OsqSPfNeI-YSXB5B-LR2KJ2S6qSfSGlS3auv3tw5DnPfXzviHz4ggi1Y1gqb9FlLcl1e5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548fb32aef.mp4?token=aPSv8MEITAwkqPYT8-p7eKd2rCYe9T7as0zM4uUiju0L9yapwYiB4e6fHlot8yjriAkSlH4bl1kFcO2LottfUho8Ex-Yrf2I1tUuhdR0vqEF8PeUeQ1BnsY7-69v_lyHzAVK1CRp6jYZLHXy8_c2q9SjjfmKCUHftACdkRDPJM_p5ZcCrLzaw2u-AA3r_CbGMf6E2Gc8BH1n-Ikrgew0naa4yixoe3m-BWZb75cHnuev9oV8wrUseluaFzl6pqADha9ldullUIqqnoT_OsqSPfNeI-YSXB5B-LR2KJ2S6qSfSGlS3auv3tw5DnPfXzviHz4ggi1Y1gqb9FlLcl1e5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا :
هیچ کاری علیه ایران وجود ندارد که بخواهیم یا لازم باشد انجام دهیم و نتوانیم آن را انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/25186" target="_blank">📅 16:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر امور خارجه، چپقچی :
روند مذاکراتی همچنان ادامه دارد و از طریق میانجی‌ها پیام‌ها در حال رد و بدل شدن است.ما طرح خود را که تحت عنوان «طرح هفت‌روزه» ارائه کرده بودیم، مطرح کردیم و دیدگاه‌های طرف آمریکایی را نیز در مقابل آن شنیدیم. در حال حاضر مشغول بررسی دیدگاه‌های آمریکایی‌ها هستیم و فکر می‌کنم ظرف چند روز آینده پاسخ خود را ارائه خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/25185" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اتاق جنگ با یاشار : ناو هواپیمابر هسته‌ای روزولت قرار است برای نخستین‌بار طی حدود
چهار سال
وارد بندر
یوکوسوکا در ژاپن
شود. شورای شهر یوکوسوکا روز چهارشنبه از مقامات شهری و شهردار خواسته برای ورود یک ناو هسته ای آماده باشند، اما
نام ناو، تاریخ دقیق ورود و مدت توقف هنوز اعلام نشده است
. ژاپن قرار است فقط ۲۴ ساعت پیش از ورود، اطلاع رسمی دریافت کند.
ناو
USS Theodore Roosevelt (CVN-71)
و گروه رزمی آن در حال حاضر در اقیانوس آرام هستند و برای یک
استقرار طولانی‌مدت در خاورمیانه
به سمت غرب حرکت می‌کنند. بنابراین
روزولت گزینه اصلی برای این توقف  کوتاه ، یوکوسوکا محسوب می‌شود.
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/25184" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">BTC 82,500$
🔻
@WarRoom</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/25182" target="_blank">📅 15:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دلار و تتر ۲۶۸،۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/25181" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مراسم خاکسپاری جاویدنام علیرضا رئیسی که همراه با علیرضا سپاهی حکمش اجرا شد @WarRoom
🖤</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/25180" target="_blank">📅 15:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز: هفتمین مظنون پرونده طرح ادعایی حمله به پایگاه هوایی فرفورد بریتانیا با پهپاد آزاد شده اما تحقیقات ضدتروریسم ادامه دارد. پلیس بریتانیا این پرونده را مرتبط با یک طرح احتمالی با حمایت ایران بررسی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/25179" target="_blank">📅 14:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک‌تایمز: اسرائیل به آلمان درباره افزایش خطر حملات احتمالی مرتبط با ایران علیه پایگاه‌های نظامی آمریکا، به‌ویژه
رامشتاین و اشپانگدالم
، هشدار داده است. ارزیابی‌های اطلاعاتی احتمال حمله با پهپاد را نیز مطرح کرده‌اند، اما تاکنون زمان یا هدف مشخصی برای حمله تعیین نشده است. هم‌زمان، تحقیقات درباره طرح ادعایی حمله به پایگاه آمریکایی فرفورد در بریتانیا ادامه دارد و مقام‌های بریتانیایی به احتمال دخالت ایران اشاره کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/25178" target="_blank">📅 14:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1a2241b4.mp4?token=VIvF89fvIV0FGkhAV0DnB4MIbBKni4wkg2o2St9UgkBkilgLFCz8Sg953veIcmW-TuqFNphiopwVxSSpKRMKJtry4XgVY09WHB3bv45J57aMCf16X-EHHKs8KuWzXb06FcjCo9gW9W52t5RgN53Xbgs85qepltOM3wdwiPT1U74I0sW366cDG4OW55zy7KGAb02AWhbGOljDxv3hsiQsvwCzWMuoEe1LSV1U_W7MpEOZieVqqilvKGJdTxHkNYdv86eyEiYnXn5Mj1zxyCV1MZ6XqbfiUmGwAuCKC91tvg1lzdKvNthHNVj2iHvKL9hVdp4Ml4jVPMPT66dKn9W4Jhhw3bYqcGYH4AoG_HFBi24X3I4clxcUvrgGHFAitthJCme6_83cuEz9NS_UawKKEaSKSxyqNLUJuC54W80yEE-bp9RK7immmOgRuK16d6umHz-EP4fhlVMUtnCMISH9bUoEo1N8N4JancrYChZ1xxnNB7ypimHcF1kuD-NdhnKVERytDuX7ltF10Id4eQkjHKKD4aV_8cqVT91wl-BkhMKq-SwsihLZkcCRDlIThTAJMsar_hHSaGKBpK5V-G_lnjJECFN5Ih475RSlSOra3YZKHETZkPc4amFHr3rQqEq7io8OnsdyCv5a_lKizqWDQduuLfEm9O3AKyiloh5wDPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1a2241b4.mp4?token=VIvF89fvIV0FGkhAV0DnB4MIbBKni4wkg2o2St9UgkBkilgLFCz8Sg953veIcmW-TuqFNphiopwVxSSpKRMKJtry4XgVY09WHB3bv45J57aMCf16X-EHHKs8KuWzXb06FcjCo9gW9W52t5RgN53Xbgs85qepltOM3wdwiPT1U74I0sW366cDG4OW55zy7KGAb02AWhbGOljDxv3hsiQsvwCzWMuoEe1LSV1U_W7MpEOZieVqqilvKGJdTxHkNYdv86eyEiYnXn5Mj1zxyCV1MZ6XqbfiUmGwAuCKC91tvg1lzdKvNthHNVj2iHvKL9hVdp4Ml4jVPMPT66dKn9W4Jhhw3bYqcGYH4AoG_HFBi24X3I4clxcUvrgGHFAitthJCme6_83cuEz9NS_UawKKEaSKSxyqNLUJuC54W80yEE-bp9RK7immmOgRuK16d6umHz-EP4fhlVMUtnCMISH9bUoEo1N8N4JancrYChZ1xxnNB7ypimHcF1kuD-NdhnKVERytDuX7ltF10Id4eQkjHKKD4aV_8cqVT91wl-BkhMKq-SwsihLZkcCRDlIThTAJMsar_hHSaGKBpK5V-G_lnjJECFN5Ih475RSlSOra3YZKHETZkPc4amFHr3rQqEq7io8OnsdyCv5a_lKizqWDQduuLfEm9O3AKyiloh5wDPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم خاکسپاری جاویدنام علیرضا رئیسی که همراه با علیرضا سپاهی حکمش اجرا شد
@WarRoom
🖤</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/25177" target="_blank">📅 14:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله مسلحانه به مینی‌بوس حامل کارکنان نزاجا در بلوچستان روابط عمومی لشکر ۸۸ زرهی نزاجا: ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، در محدوده شهرستان نیکشهر مورد حمله مسلحانه قرار گرفت. متأسفانه در این درگیری…</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/25176" target="_blank">📅 13:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnj84vRq1SDIz7rm8OxaLmB1u_zqZFmfrNvXLOppNYop6rnDwijWYZEawYFHO9XztY88CZaCueENpOUa7EIBa-Es6kCKOa0vPld9tq7P9t-It-1lsFD3FoWT9V-etaDmfprP2CwKH3y_LCeVASWJr6eZxuqkbjZKHKBSulvywF3Bqe08XYlFX9BeG5SkK3JNxQMzE-9V7jGEVR0nJBVLw2mfvWk9PgYt08LH7raJvfj7Iqc6-HVSLEB2qfAx11GwMO_32TsTpYoaeCQqF0DLjUxuFppmh7w0HbGT9XYqW9dzjAcSQ4ZN5f2A8QUYUOPHG3QVtQc-R2BAKgn9yRR5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : دیروز ناو هواپیمابر آبراهام لینکلن آمریکا به سن‌دیگو خانه خود بازگشت و عرزشی ها آن را به تمسخر گرفتند، ولی نکته مهم و شکه کننده که دیدم در این ویدیو و آنها باید گریه کنند این است که نشانه‌های انهدام(کیل مارک) ثبت‌شده رویش حدود ۱۰۵ پهپاد و ۳۴ ناو جنگی را در این ویدیو نشان میدهد عملکرد قابل‌توجهی برای تنها یک گروه هوایی مستقر روی یک ناو هواپیمابر.هگست وزیر جنگ پیشتر گفته بود که ناو لینکلن و گروهش ۶۴ ناو جنگی ایران را نابود کردند (بیش از ۲/۳ام نیروی دریای ایران )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/25174" target="_blank">📅 13:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbKDPHX7tbSF7K8nsIVp47HtZxu9zU3AaAhB3Sb5DlslEKmKLTpXYhdvZ0A-n-IOQn3wb7zIpF_WjwDWkvAGYC0DMmRI5kDd1lHWxzQ3JCa1rbTn33C7rcXVIIFiacUoIhESZIMT4szGtST0u57f3LbdgmcmD0LZru1awJiRaxt8G4AhU_4KGtR5DvCBmgzkHt4Hfjk2GszoOXP6U3T81R4vthIuGG310kLV2cDQhlT1MnSBhBmokJRBjgOdNajx8n6-KUJeUxz06vbvDLi_ZELkFT4LYLWSRCidU3UwEw6OnEhaihF6M9UKASP4IPU1Q8eqvpHW3bdM9R-kK3bO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pimJ5ePx79DvpIJLxx9XGSpszWAkfHx7bUEuuweh0k2YcX_zlH3Wi7nNsUq_sEkRvZ702cmOmB3N--FYpxBsx5RRg3HHL7MsELo7q3VSsr1z1RKgISGE4NVUcxfsiofgYPHJ9XVIO_PCgy5ScIKEnomDi7iQm5VYVbWaojcu9y3iLhx8gRL_zUcb9w3nAatj5Y8ZUOZz81kRsb1XZxlv0TOsndEcFrzzmxEyfdvtDTXXVjJryScLJ-GLoABSxvh3rZQYdreoZE70PygvbbkJI4Gxu0erH17lS-dhsDofa6uKRyaCrSXOOjPB0hMjPo9Vuveqn_7n-l1uCbEV3R7q7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-mm6bI6z4hMJugM_PprsBATpmBrxAnNxI1nwWEVUeRTB1T3BlqSjFA9RD1zeL2RcCqqiE1aA28oKilDmxOhGw4O3l01w9gbmQ93ZuAXmWlt52AXCO7JeE3lxWj_XGQl0RZxvJVyqU-Wc-7n9CGoK1dxXk94eYqr49GhWb2GOWas09hlt-EShipjPVP6y4H-l42NA2Vr5UKfvlSgNlTIQkrIObaKRE-hFWU_T0erd1dMD-khJCvIbe8JOzSiSYPVdEX6XRuFxuKPtzko1THYw_n7f8ASQZ-sFnSD6ZynRCOCd9AvBbbovZ4mxKyXhAnx3HHFMUuOsURtky-2bE7bIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1aAzHfdwWPyLRHJXDlwBDgdQJLt5P_cKIJtlkrY94bvFuDft8QqdIhl1gRzHRd7xWy0bEVUaXMY0W3w4F3n7kpdzC9FDOFTB5-KwSuu0O7dHuMLMpE5lAeistEgB8ncgnHpJr144Be0pILCeRsJrw8ZZ_3tMSuaG2ZH4IGI5H9TJTuoo81sFyxihWXLwe9O40A8Mz-dK4DLR62kt-RW8yeZc1IFUqfVHzzkvG9EHfvDp7ojA2HDeXDNS_CCA1vGr7K3Ypc8IeInmw3RHS2AckqnIwsFXsbpjgCqeDniBrWN_pyGFroRcVHwl5iPNpI25uFo0Hz2zcRuGHGplfCa_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک جنگنده
اف ۳۵ سی ناونشین آمریکا
از
اسکادران ۳۱۴
تفنگداران دریایی، با سه نشان انهدام زیردریایی در بدنه مشاهده شده است؛
زیردریایی‌هایی باید از کلاس غدیر ایران باشند.
همچنین روی این جنگنده نشان‌های انهدام
یک نفتکش، یک ناو جنگی، یک پهپاد شاهد، یک قبضه هویتزر، دو پرتابگر موشک و سه سامانه راداری
دیده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/25170" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مرد خردمند ، مارک لوین : به نظرم سخنرانی
روبیو
حال‌وهوای سخنرانی یک نامزد ریاست‌جمهوری را داشت، هرچند این بدان معنا نیست که او در این باره تصمیم قطعی گرفته باشد. این سخنرانی تفاوت آشکاری با نوع اظهارات و سخنرانی‌های ونس دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/25169" target="_blank">📅 13:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMD65rc3c-XJKJpfuyXBYqQ2V9kMZmVl9WaOCMivhrX_BJN1dzrinJZTVyxg_qys4yryG_xitE8WHjndvqoWOOTFKjIBo7eWawbN7ezroNJeern_JZD8ejFI-I4IabwV1de_UUc-g282_iXETE9x5Xber7vlhjTlXdYA6uB-WYtSRE3Du9z5rYNB3YFCha33saUc3PblkRCgKXsxkLM8slsMa5IhpoI6aZq6Glc8XDdom7dWRxUFYT1rDrh_BlYYt0R5PlQ2WWCVu6BH7XJ8VBMqItPtMmHi8IWRWmFxiHwyiNxouAVoQStjz_pZ0kZsdYYt8LILIV-7aACWdG9EkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ مهر، «روز مهر از ماه مهر» و جشن مهرگان و پیروزی داریوش بزرگ بر گئومات مغ و آغاز شهریاری او فرخنده باد
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/25168" target="_blank">📅 12:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حمله مسلحانه به مینی‌بوس حامل کارکنان نزاجا در بلوچستان
روابط عمومی لشکر ۸۸ زرهی نزاجا:
ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، در محدوده شهرستان نیکشهر مورد حمله مسلحانه قرار گرفت.
متأسفانه در این درگیری یک نفر به نام «محمدرضا اوکاتی» به شهادت رسید و ۳ نفر مجروح شدند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/25167" target="_blank">📅 12:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6614110b.mp4?token=DoUf_NNhBQfKBRhT-SlF-Pr7kdx0ANyp70pXLE1HylSq-DC8fHT5BlzNKXl7HyEsHSTQxUtWbleup3cEtyGBYJfr0P2LBZPnyu7_-FTPEwad8USDHyueUIGtbeh2yjaC4FoCzLKq_0RS-YwnRX3bruhiw1xFLAQGbAAJmnfled9b1g39cQYa_myUDN1ypniigxLsWbNGDJUhaY-EG_ghVVlo1qzpghEbHFOgFuLD_VX3I3h-A87jW4VeViEvIUB-IOmOM3VJxrGZ9_M-__o_HuCOCL0bCcGvNfpPtsAjO_h5-suGeItNtH4gOzMBBY0vp-8QK1bQPlzaYemrb7AwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6614110b.mp4?token=DoUf_NNhBQfKBRhT-SlF-Pr7kdx0ANyp70pXLE1HylSq-DC8fHT5BlzNKXl7HyEsHSTQxUtWbleup3cEtyGBYJfr0P2LBZPnyu7_-FTPEwad8USDHyueUIGtbeh2yjaC4FoCzLKq_0RS-YwnRX3bruhiw1xFLAQGbAAJmnfled9b1g39cQYa_myUDN1ypniigxLsWbNGDJUhaY-EG_ghVVlo1qzpghEbHFOgFuLD_VX3I3h-A87jW4VeViEvIUB-IOmOM3VJxrGZ9_M-__o_HuCOCL0bCcGvNfpPtsAjO_h5-suGeItNtH4gOzMBBY0vp-8QK1bQPlzaYemrb7AwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : زنم بهم گفت یه لطفی بکن، کلمه vegan رو درست تلفظ کن!
‏من میگفتم “وِیگن”! از کجا باید بدونم چطوری تلفظ میشه؟! من استیک دوس دارم!”
@WarRoom
😂</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/25166" target="_blank">📅 12:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز: ایران ماه گذشته ۲۰۰ میلیون دلار به حزب‌الله لبنان داد تا این گروه به خانواده‌های لبنانیِ آواره‌شده در جنگ با اسرائیل کمک مالی کند.حدود ۵۰ هزار خانواده که خانه‌هایشان تخریب شده یا امکان بازگشت ندارند، در اولویت قرار می‌گیرند و به هر خانواده در مرحله…</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/25165" target="_blank">📅 11:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رویترز:
بیت‌کوین فقط امروز ۱.۳ درصد افت کرد و به حدود ۸۲٬۲۶۵ دلار رسید
و اتریوم نیز ۰.۸ درصد کاهش یافت. رشد دلار، بازده اوراق و قیمت نفت مهم‌ترین فشارهای کلان بر بازار رمزارزها هستند. حدود
۵۵۰ میلیون دلار معاملات اهرمی
در بازار کریپتو لیکویید شده که بخش عمده آن مربوط به معامله‌گرانی بوده که روی رشد قیمت شرط بسته بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/25164" target="_blank">📅 11:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اکسیوس: پنتاگون برای احتمال ازسرگیری عملیات گسترده علیه ایران آماده می‌شود
منابع آمریکایی و اسرائیلی می‌گویند در صورت آغاز عملیات، حملات می‌تواند تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران را دربر بگیرد. این موضوع پس از نشست چندساعته تیم امنیت ملی ترامپ در کمپ‌دیوید و تماس‌های اخیر او با نتانیاهو مطرح شده است. یک مقام پنتاگون به اکسیوس گفت:
«وظیفه این وزارتخانه، توسعه گزینه‌های نظامی و ارائه آنها به رئیس‌جمهور است.»
یک مقام کاخ سفید نیز گفت ترامپ در هر زمان همه گزینه‌ها را در اختیار دارد و آمریکا به‌دلیل کنترل تنگه هرمز و وضعیت اقتصادی ایران، در موقعیت قدرتمندی قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25163" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
پنتاگون به
فرماندهی مرکزی آمریکا(سنتکام)
دستور داده است آماده‌سازی‌ها برای احتمال
ازسرگیری عملیات‌های گسترده نظامی علیه ایران
را تکمیل کند.
بر اساس این گزارش، حملات ممکن است
پیش از انتخابات اسرائیل و آمریکا
آغاز شوند؛ با این حال،
دونالد ترامپ، رئیس‌جمهور آمریکا، هنوز تصمیم نهایی را اتخاذ نکرده
و
هیچ تاریخی نیز تعیین نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/25162" target="_blank">📅 10:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شبکه NBC به نقل از یک مقام آمریکایی، یک مقام خاورمیانه‌ای و یک مقام ایرانی گزارش داد که
ایران و آمریکا در ماه جاری میلادی در نیویورک، از طریق میانجی‌ها درباره برنامه هسته‌ای ایران گفت‌وگو کرده‌اند.
واشنگتن می‌گوید هر توافقی باید موضوع هسته‌ای ایران را نیز شامل شود و ایران میگوید خط قرمز است و اصلا
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/25161" target="_blank">📅 10:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تنش جدید اسرائیل و بریتانیا
اسرائیل در واکنش به تحریم‌های بریتانیا علیه شهرک‌های اسرائیلی در کرانه باختری، دستور تعطیلی
کنسولگری بریتانیا در شرق اورشلیم
را صادر کرد. گیدئون ساعر، وزیر خارجه اسرائیل، این اقدام را واکنشی به سیاست‌های «خصمانه» بریتانیا دانست. اد میلیبند، وزیر خارجه بریتانیا، گفت لندن حق اسرائیل برای بستن کنسولگری را به رسمیت نمی‌شناسد و بر سابقه نزدیک به ۲۰۰ ساله این نمایندگی تأکید کرد. امروز تابلوهای کنسولگری پایین آورده شد، اما یک تیم محدود بریتانیایی همچنان اجازه فعالیت در ساختمان را دارد.
سفارت بریتانیا در تل‌آویو همچنان فعال است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/25160" target="_blank">📅 10:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: ایرانی‌ها آماده‌اند هر کاری را برای ما انجام دهند تا از آنچه در حال وقوع است جلوگیری کنند، با این حال، توافق با آنها واقعاً گزینه‌ای نیست که من ترجیح بدهم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/25159" target="_blank">📅 10:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1LkfiNs_7v34w59Sp0mG88rAJT0QrDFyJX7uxEe0iTKWColD680i3U1FsuIvxWYY5cMGhM4ReAJztNijbptJa-iAZqacvKGQrF0krBNSmpU6y_3pwaEqlY2PEDhP0qwLW09E8-tPa7qLbrPVq3vK2VphanOy9f2i_U7-6zymGYyZcQCy4auq_14pVfRmZ6BeJEmUuf-XAL2Z0eaobw4cTQmWxosMRTZDb9rbpUjCQ0Psn2vzNld0OuCNOCQoUOG7W0chbJNybdQcuxC3B-3vdc4pw3lRnQo1JlqY0567vzQgRtd8uyRyRCUorSpj2tZkJwQa04AScUSyLvjgVkgaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «انتقال نفت به سطح پیش از جنگ بازگشت!»
@WarRoom
حجم انتقال نفت خام از منطقه خلیج فارس :
قبل از مارس: جریان نفت در سطح میانگین و طبیعی خود (حدود ۲۴ تا ۲۵ میلیون بشکه در روز) قرار داشته است.
ماه مارس: با بسته شدن و انسداد تنگه هرمز در پی تنش‌ها و آغاز درگیری، حجم انتقال نفت افت چشمگیری پیدا کرده و به کمتر از ۱۰ میلیون بشکه در روز سقوط می‌کند.
ماه‌های بعد تا سپتامبر و اکتبر: جریان صادرات نفت به‌واسطه استفاده از خطوط لوله جایگزین زمینی، مسیرهای دوربرگردان و پشتیبانی ترانزیتی روندی صعودی به خود گرفته و مجدداً به سطح میانگین پیش از جنگ (تراز ۱۰۰ درصدی سال ۲۰۲۵) بازگشته است.
@WarRoom
یاشار: چنل های بی سواد همه اینو زدن قیمت نفت
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/25158" target="_blank">📅 10:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjwrKd-ufVq11Kg-fvLMI5zjFsT44DRHZDwcKtoHJ7Jc02XGrHk8g_XZmYmtvJ5PWqm63pcp0l2fTLocCwvWNHHNxE8y0mYvsHDNaEuFvs0Iaq4fzfeLzW-xof-sP28L1E6eLOM7IV7JkLVe-bdCjaskHMrCP9XdpyeemmVB98O9tl5SDryfs22n1pn_FTKOlrc-pAwo_vUyIr49t1bA-q0rpxBOpCYQhf2N1Olq_0h-kFZyk-KtDmO6DYDqME0MfwbugVNodqxDGv4oUfrijmkwep24oSMPEgyOojCmgSvBT-B67YvLW-7XTDyKhK3yIUckfK4s7fvDilEYKvG_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس ۳۰ دقیقه‌ پیش صدای‌ انفجار‌ شدیدی‌ اومد … @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/25157" target="_blank">📅 10:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بندرعباس ۳۰ دقیقه‌ پیش صدای‌ انفجار‌ شدیدی‌ اومد …
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/25156" target="_blank">📅 10:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71094a656.mp4?token=l5pRLwZ7Cv8K8peru3cR-EIhGDKJg-Y_lTj1MpNZadPO-DyYAUV6_Xqy3T76gFvgveZ2K4FaiX8gzXt6jo90IYlAYHoJVx0E84_L0hqh3Ps0ptqVvLJwOKSSZravtn-w5zN3MxB47M8N9KfE2dw3x-Ju0WssHuSeOjvpzhroQfKMFIC5VeVdZbiyr2E8Ayn8aiPYFQsQDTl__lQrTzsUayoI-Gl_q17PnOI9CGGT0pFlLrBqKqTmP4VT8WxY2X1wRkm-HfVi_zTWEDdghiVRYzoTJ9vcaiKJwO8X_lUM8jh6D5BxTpZFC9KIyq5AMGii3md9B9_mJ1mn8VWw_5kGzhTP8rM8iBPzGkB7uWCeHgStDuHEd-WoGtNeWlNlgPG5oFrmZ0taExriTVPihhfL_cqapW9hBHsc0nBC9rruUcmsALhaqUur9wSHOyXSCo9ZqRIJxSTp23hrJNgCDb20wqUTpQCRJVwKU9g3R6ctiGEeT9qgdrtgd0SZu1CwHXS5Ac-DbFL4_GeFVMl3ZROQ3Cw-pmfsUcgjIrR43kJ4EO-Oh1Bu_BkOrrayXNXOjWhUUsZ_0U_c6D2wNWHACcrfw2HzTo8-hp_VUSM_AZMgeMONXTQ8-ebcRKZjCqcq8t4myjE936IQq5LWh4blo6dLd5ES38emKM_4hJwvIQoHoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71094a656.mp4?token=l5pRLwZ7Cv8K8peru3cR-EIhGDKJg-Y_lTj1MpNZadPO-DyYAUV6_Xqy3T76gFvgveZ2K4FaiX8gzXt6jo90IYlAYHoJVx0E84_L0hqh3Ps0ptqVvLJwOKSSZravtn-w5zN3MxB47M8N9KfE2dw3x-Ju0WssHuSeOjvpzhroQfKMFIC5VeVdZbiyr2E8Ayn8aiPYFQsQDTl__lQrTzsUayoI-Gl_q17PnOI9CGGT0pFlLrBqKqTmP4VT8WxY2X1wRkm-HfVi_zTWEDdghiVRYzoTJ9vcaiKJwO8X_lUM8jh6D5BxTpZFC9KIyq5AMGii3md9B9_mJ1mn8VWw_5kGzhTP8rM8iBPzGkB7uWCeHgStDuHEd-WoGtNeWlNlgPG5oFrmZ0taExriTVPihhfL_cqapW9hBHsc0nBC9rruUcmsALhaqUur9wSHOyXSCo9ZqRIJxSTp23hrJNgCDb20wqUTpQCRJVwKU9g3R6ctiGEeT9qgdrtgd0SZu1CwHXS5Ac-DbFL4_GeFVMl3ZROQ3Cw-pmfsUcgjIrR43kJ4EO-Oh1Bu_BkOrrayXNXOjWhUUsZ_0U_c6D2wNWHACcrfw2HzTo8-hp_VUSM_AZMgeMONXTQ8-ebcRKZjCqcq8t4myjE936IQq5LWh4blo6dLd5ES38emKM_4hJwvIQoHoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ، درباره ایران:
«همان‌طور که قول داده بودم، اطمینان حاصل می‌کنم که ایران هرگز به سلاح هسته‌ای دست پیدا نکند. آنها این را می‌دانند.
ما به‌زودی از آنجا خارج خواهیم شد و خواهید دید که قیمت نفت مثل سنگ سقوط خواهد کرد و قیمت همه‌چیز نیز پایین خواهد آمد.
این عملیات بزرگی بود که روسای‌جمهور قبلی باید طی سال‌های گذشته انجام می‌دادند. باید انجام می‌شد، اما هیچ‌کس حاضر نبود مسئولیت آن را بر عهده بگیرد. ما چاره‌ای نداشتیم، چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/25155" target="_blank">📅 09:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7d98ccb1.mp4?token=XgR2KttOkxh6PlREEj2WOxp2rmTgYo6pHYC6dkXcE7AZ5xTeulk63vnSwQfdNQHqR7tliZep1O5KAqgl7WtSkp8ke3Sy8EMMd0aOA46mXBIHwFuXyal52wKDIKkCnDj0kDehcCvxx8bjzSNDfqYwxGko7DG2pWXpnADtBG2xOli1SvqhmOzs6vJ2c01s_aGBTTBdiNQH_rGXe-a06jeJwP88N1p8r_iA4U5KKMNjCKvppKHZoJk7euHui3j47eLlQD5ZpLECtUlXzuQupNvVxypcITxp3KU2iH9c6A3qvYWj1K1p9XJVqQuPBZmsNavS6zDqV9q1uUarUtOQw0Ce_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7d98ccb1.mp4?token=XgR2KttOkxh6PlREEj2WOxp2rmTgYo6pHYC6dkXcE7AZ5xTeulk63vnSwQfdNQHqR7tliZep1O5KAqgl7WtSkp8ke3Sy8EMMd0aOA46mXBIHwFuXyal52wKDIKkCnDj0kDehcCvxx8bjzSNDfqYwxGko7DG2pWXpnADtBG2xOli1SvqhmOzs6vJ2c01s_aGBTTBdiNQH_rGXe-a06jeJwP88N1p8r_iA4U5KKMNjCKvppKHZoJk7euHui3j47eLlQD5ZpLECtUlXzuQupNvVxypcITxp3KU2iH9c6A3qvYWj1K1p9XJVqQuPBZmsNavS6zDqV9q1uUarUtOQw0Ce_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : استیو ویتکاف در حال کار روی توافق با ایران است و عملکرد بسیار خوبی دارد
فکر می‌کنم این توافق واقعاً چیزی نیست که من بخواهم انجام دهم، اما آنها حاضرند هر چیزی به ما پیشنهاد دهند تا این درگیری متوقف شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/25154" target="_blank">📅 09:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfd30d3c3.mp4?token=OXk8iO-BB-Q27feQrHwnTFfEDCrwcU9l4bqpQlIYAMxKLrnnyLk2D_GX71x9w_M1jHjv2BGD1IJTxXgNzAsfP2L4gxj9RQcGVMLjUnfetfJLmlGAJulsg8CHmMxBdlJ-vr-soNvbQU4mCtp6uSfn_DnooyH531qbduIBGdWBTvadKJF7y7xcV9SHrAqLEvSK0i6ypMUNEEdfa6vu3PW1eTxTz_DC6sPMwSObh8L5KI0yvddhUs3QgoP6VVezZoj1cGHgq6-mrswYU7T8WM593F5nh8GSuZgOvaLlQk-nrD6QqAE3UoUn1ZRRLF4GytN1LeLxzGMc2SLeoNo6zO3TiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfd30d3c3.mp4?token=OXk8iO-BB-Q27feQrHwnTFfEDCrwcU9l4bqpQlIYAMxKLrnnyLk2D_GX71x9w_M1jHjv2BGD1IJTxXgNzAsfP2L4gxj9RQcGVMLjUnfetfJLmlGAJulsg8CHmMxBdlJ-vr-soNvbQU4mCtp6uSfn_DnooyH531qbduIBGdWBTvadKJF7y7xcV9SHrAqLEvSK0i6ypMUNEEdfa6vu3PW1eTxTz_DC6sPMwSObh8L5KI0yvddhUs3QgoP6VVezZoj1cGHgq6-mrswYU7T8WM593F5nh8GSuZgOvaLlQk-nrD6QqAE3UoUn1ZRRLF4GytN1LeLxzGMc2SLeoNo6zO3TiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«می‌خواهید تروما و مشکلات را ببینید؟ بگذارید آنها در مسیر، یک موشک به سمت سن‌دیگو یا لس‌آنجلس شلیک کنند.
می‌خواهید صحنه‌ای وحشتناک ببینید؟ می‌خواهید مشکلات را ببینید؟ بگذارید سن‌دیگو یا لس‌آنجلس را هدف قرار دهند.
ما اجازه نخواهیم داد چنین اتفاقی بیفتد. ما از شهرهایمان و کشورمان محافظت می‌کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/25153" target="_blank">📅 09:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c79099a6.mp4?token=sjF1btiINkcooEKYrLJjZyHIPA_lQ_yVHFTmfT8PRJYOYT6u-lojv3cfFjT3CcDxR6pYy0uB_RPoXmsbE-AcAHmD-xMtn0gmCv396Mn3jv9IUPVfB5Lohzycf6WKvykJSymt9mtYak3TAU4LeZOm11jYtbqSiqcCCpATEfI4OmQs0-Q9snDQc6kPDFVbxJRRqXsgAfLTceTQZQUOquwnAWj2gnfFsDWhHfuFShIF_W-wNLBP7hAZlSg3RwyfCRaLMSg96YGuyEnh_ckvuVpTe1qDG46_VCU7xzk-4So-VRZ9D5uxpEZoI-ciAV-O1qh1ubrdqpkt00Bsc7gqJJXO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c79099a6.mp4?token=sjF1btiINkcooEKYrLJjZyHIPA_lQ_yVHFTmfT8PRJYOYT6u-lojv3cfFjT3CcDxR6pYy0uB_RPoXmsbE-AcAHmD-xMtn0gmCv396Mn3jv9IUPVfB5Lohzycf6WKvykJSymt9mtYak3TAU4LeZOm11jYtbqSiqcCCpATEfI4OmQs0-Q9snDQc6kPDFVbxJRRqXsgAfLTceTQZQUOquwnAWj2gnfFsDWhHfuFShIF_W-wNLBP7hAZlSg3RwyfCRaLMSg96YGuyEnh_ckvuVpTe1qDG46_VCU7xzk-4So-VRZ9D5uxpEZoI-ciAV-O1qh1ubrdqpkt00Bsc7gqJJXO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ : در سه شب گذشته، ما بیش از هر مقطع دیگری در تاریخ تنگه هرمز، نفت بیشتری از این تنگه خارج کرده‌ایم.»
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/25152" target="_blank">📅 09:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef85cb34d.mp4?token=vLpQ7VXRjlhHt2QeLn8re-B8zLbewU0vR18YtkJFs1QpKyttSJotVP1oohaop4E9usUFH068EuuNAqZSO9u-Ges_3IY81mWlJP44TJNZzJp1r2-qPEFHG_o10FnHdmYpmCd-FrgyJQs82kIMcAbjA2cCc9Tb4tsrggJ7g4dqhaDtYwaJ2iIWTpLtW_SrpQFZQe2Le8w4chr4mhWGIFtNCYiH91Wcw070lGenmwZAOV-70zRjuKqXvv9KaqhA0GYyt7X8pMMQqlvam_v_4mMRtLl6Vf6nzPFCjt9akpMGYsTA-Qu7xwxc_5uBxwNhd7OV_bHAWkwDTLGqZk3YN_7YzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef85cb34d.mp4?token=vLpQ7VXRjlhHt2QeLn8re-B8zLbewU0vR18YtkJFs1QpKyttSJotVP1oohaop4E9usUFH068EuuNAqZSO9u-Ges_3IY81mWlJP44TJNZzJp1r2-qPEFHG_o10FnHdmYpmCd-FrgyJQs82kIMcAbjA2cCc9Tb4tsrggJ7g4dqhaDtYwaJ2iIWTpLtW_SrpQFZQe2Le8w4chr4mhWGIFtNCYiH91Wcw070lGenmwZAOV-70zRjuKqXvv9KaqhA0GYyt7X8pMMQqlvam_v_4mMRtLl6Vf6nzPFCjt9akpMGYsTA-Qu7xwxc_5uBxwNhd7OV_bHAWkwDTLGqZk3YN_7YzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«جنگ خیلی زود به پایان می‌رسد. آنها کشوری شکست‌خورده هستند.
هنوز کمی روحیه و جسارت برایشان باقی مانده، اما زیاد نیست؛ اصلاً زیاد نیست.»
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/25151" target="_blank">📅 09:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی کاخ سفید : رئیس جمهور ترامپ از روند فروپاشی اجتناب‌ناپذیر ایران راضی است.
ترامپ اجازه نخواهد داد که رژیم ایران مانند آنچه با روسای جمهور سابق اتفاق افتاد، او را مچل کنند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25150" target="_blank">📅 02:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، روی ناو یو‌اس‌اس آبراهام لینکلن: ایران هیچ‌وقت نتوانسته راهی برای عبور از آبراهام لینکلن پیدا کند و طبیعتاً هم همین‌طور باید باشد. خیلی خوب بود که ناوگروه شما از ابتدای این مأموریت با نیروی دریایی ایران به یک توافق رسید؛ توافق شما…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25149" target="_blank">📅 02:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14526f5af7.mp4?token=XRL1KaNJqkZudMSpG9atWJCJL9MTPHsDMkurWRy4fShPVqAUnEvexWqil7woUH-RPm3qXCviFC9H0bEOs9SCFnRbPD55BFoVYj-WllhrCbpML7jCif_jvghpXtJV3bz9mgEzX6-AyRnc2tS8FkA3BlEpkn6rnKea4_Db83MJUKscjl9uj3MO2nuMAe9HbfHoINWZaroi_okAYOEZwBWQyOx0UQCstIJoHQMFCkEZtIBsp6vmcZu9WSCriEfKnOqvpaa9m7NsWBGrvEuVRp1J_rDU_uR2ztH2akrv6KJ6b_IbK5kxQ7SQEF7HpNrvPlgRuNfGdgrdR1VeRO3CeHphPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14526f5af7.mp4?token=XRL1KaNJqkZudMSpG9atWJCJL9MTPHsDMkurWRy4fShPVqAUnEvexWqil7woUH-RPm3qXCviFC9H0bEOs9SCFnRbPD55BFoVYj-WllhrCbpML7jCif_jvghpXtJV3bz9mgEzX6-AyRnc2tS8FkA3BlEpkn6rnKea4_Db83MJUKscjl9uj3MO2nuMAe9HbfHoINWZaroi_okAYOEZwBWQyOx0UQCstIJoHQMFCkEZtIBsp6vmcZu9WSCriEfKnOqvpaa9m7NsWBGrvEuVRp1J_rDU_uR2ztH2akrv6KJ6b_IbK5kxQ7SQEF7HpNrvPlgRuNfGdgrdR1VeRO3CeHphPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، روی ناو یو‌اس‌اس آبراهام لینکلن:
ایران هیچ‌وقت نتوانسته راهی برای عبور از
آبراهام لینکلن
پیدا کند و طبیعتاً هم همین‌طور باید باشد. خیلی خوب بود که ناوگروه شما از ابتدای این مأموریت با نیروی دریایی ایران به یک توافق رسید؛ توافق شما این است که
اقیانوس را با هم تقسیم می‌کنیم، اما نیروی دریایی ایران سهمش کف اقیانوس است و آبراهام لینکلن سطح اقیانوس را در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25148" target="_blank">📅 02:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCY3RUXeubalpnuMnT53enmS7kh6-XjwqjCaqzDzkqo7aA4ON0xMeObUfRWZ09wRxxbVE7fY42S4IcNX_1yyvzU7_23zjU79nmpD-VX_jgQWmVkDCTy-ssTDE2lDeiA0QeC76KIC3Hn9ARhFlKJt48_199fw1Of6PLhtqajuamcKxCalKyM0fC5EoIX5RCIAkfrGGfWvU2BN5CAy8HsSUDo2ayXU6ryCELqtebgIadMtVpaiX39qkqZZguHDky4b08QhVIEmwtdyi4Tys4wTqqSYOtxgW59g8oKIOaM5Ay31zxkACoMv13ni4abS8ADcIToJ26pySkpyPmjTNfmNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت‌یاب سنتکام :
ادعا:
امروز یکی از ژنرال‌های سپاه پاسداران در گزارش‌های رسانه‌ای مدعی شد که «تنگه هرمز بسته است» و ایران «کنترل کامل آن را در اختیار دارد». این ادعا
نادرست است
.
واقعیت:
در حال حاضر تردد از تنگه هرمز ادامه دارد و کشتی‌های تجاری حامل کالا و محموله‌های انرژی، از جمله
حدود ۲۰ میلیون بشکه نفت خام
، در حال عبور هستند.
ایالات متحده و شرکای منطقه‌ای آن کنترل آشکار تنگه را در اختیار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25147" target="_blank">📅 01:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25146">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس به نقل از سه مقام ارشد آمریکایی:
عربستان سعودی و سوریه در حال بررسی
اعزام نیروهای ارتش سوریه به یمن برای مقابله با حوثی‌ها
هستند. چندین یگان سوری برای این مأموریت در نظر گرفته شده و شمار نیروها می‌تواند به
۱۰ تا ۲۰ هزار نفر
برسد. این موضوع در دیدار اخیر
احمد الشرع و محمد بن سلمان
در ریاض مطرح شده و هدف عربستان، تقویت نیروهای دولت یمن و فراهم کردن امکان عملیات زمینی علیه حوثی‌هاست. با این حال، هنوز تصمیم نهایی برای اعزام نیروهای سوری گرفته نشده و مذاکرات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25146" target="_blank">📅 01:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ در تروث: سه سال پیش در چنین روزی، یعنی ۷ اکتبر، جهان شاهد یکی از تاریک‌ترین و شرورانه‌ترین روزها در تاریخ اسرائیل بود. مردان، زنان و کودکان بی‌گناه به دست تروریست‌های حماس به قتل رسیدند، ربوده شدند و متحمل وحشت‌هایی غیرقابل‌تصور گشتند. امروز، ما یاد تمام جان‌های بی‌گناهی را که از دست رفتند گرامی می‌داریم، به بازماندگان و خانواده‌هایشان ادای احترام می‌کنیم و به یاد گروگان‌هایی هستیم که رنج‌هایی غیرقابل‌تصور را تاب آوردند. من بی‌وقفه جنگیدم تا گروگان‌ها را به خانه بازگردانم و آن‌ها را به عزیزانشان برسانم؛ و این کار را انجام دادم، چه برای آنان که زنده بودند و چه برای آنان که جان باخته بودند! ما هرگز ۷ اکتبر را فراموش نخواهیم کرد. ما هرگز قربانیان را فراموش نخواهیم کرد. و همواره در برابر نیروهای ترور و شرارت خواهیم ایستاد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25145" target="_blank">📅 01:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0adcb3b11.mp4?token=VuHGAwO51GTiCNpoTTX_YROQy98vcp-pDT0OcjES4-vfXx_mHKiOTEn5RcE2uCyD8CIyvz7UT5aG59RsmY-YqS7dFQhLxHCB5COt0Ep8B0saFuFY0g7GD9vMD-xDN5qye8G3fZJZXYijl_YYhYF8LN-CLHau1JdyemVqGPmfU871psLkGT0df91IAAgSeFnC-1bb5wHEuF4iQqP6c5_6sPwZZL7sYlKQOjk0vMqkmuMtwyRc_-Xgvu2q90vxZo-oz-C_daSMrLdsNDK5ucGUcN_MnsZgGnq_O2KZXTiWaqvKPYgylOqr0OWiMBguZmJCNjVjM705e53sUx4-NxzJxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0adcb3b11.mp4?token=VuHGAwO51GTiCNpoTTX_YROQy98vcp-pDT0OcjES4-vfXx_mHKiOTEn5RcE2uCyD8CIyvz7UT5aG59RsmY-YqS7dFQhLxHCB5COt0Ep8B0saFuFY0g7GD9vMD-xDN5qye8G3fZJZXYijl_YYhYF8LN-CLHau1JdyemVqGPmfU871psLkGT0df91IAAgSeFnC-1bb5wHEuF4iQqP6c5_6sPwZZL7sYlKQOjk0vMqkmuMtwyRc_-Xgvu2q90vxZo-oz-C_daSMrLdsNDK5ucGUcN_MnsZgGnq_O2KZXTiWaqvKPYgylOqr0OWiMBguZmJCNjVjM705e53sUx4-NxzJxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25144" target="_blank">📅 00:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران اعلام کرد که پاسخ ایران به پیشنهادات مطرح‌شده توسط آمریکا از طریق واسطه‌ها به طرف مقابل منتقل خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25143" target="_blank">📅 00:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: مشاوره‌های ما با عمان با موفقیت انجام شد و بر سر هماهنگی‌های مربوط به مسیرهای امن به توافق رسیدیم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25142" target="_blank">📅 00:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی نیروهای ائتلاف: ما 82 هدف نظامی متعلق به شبه‌نظامیان حوثی را در استان‌های صعده، الحدیده، الجوف و مأرب منهدم کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25141" target="_blank">📅 00:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25140">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به قول شاعر نایس پرفیوم
😼</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25140" target="_blank">📅 00:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af54a6283.mp4?token=pJByQgQUlPz6V6Z85Vd6iFLmBoglF9CKq1d_so5SfD7phzLy92Ft9GKeQX65Z8PVmLaqgQB-6Ty_LtKEFv76jPQook44ZqXA45q27b6UXmZHW68p2ytfe42q6XvB7LQ61KZi46xK8YgSNTfmxftpaxFFLy1JMjeEAYHyDs1khiTZifl-tNOLTHsJzKhM_Tk_EMSz6GAOWhegXdHh4cXROpQzA1L_awY3YW1U6Vl-X9c0j_CNo8cUGcAclS_RuEgDJQ5bpXpM-mZ81beHxPdy720EzhuV9_D5D4uDzxR2Xl3-pX2xVIdgPcWNqZt3FJTlVcszVKdAoy0js0Z8zJr5pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af54a6283.mp4?token=pJByQgQUlPz6V6Z85Vd6iFLmBoglF9CKq1d_so5SfD7phzLy92Ft9GKeQX65Z8PVmLaqgQB-6Ty_LtKEFv76jPQook44ZqXA45q27b6UXmZHW68p2ytfe42q6XvB7LQ61KZi46xK8YgSNTfmxftpaxFFLy1JMjeEAYHyDs1khiTZifl-tNOLTHsJzKhM_Tk_EMSz6GAOWhegXdHh4cXROpQzA1L_awY3YW1U6Vl-X9c0j_CNo8cUGcAclS_RuEgDJQ5bpXpM-mZ81beHxPdy720EzhuV9_D5D4uDzxR2Xl3-pX2xVIdgPcWNqZt3FJTlVcszVKdAoy0js0Z8zJr5pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25139" target="_blank">📅 00:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25138" target="_blank">📅 00:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25137" target="_blank">📅 00:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df53d80fe4.mp4?token=IDeXktgMxf5aJGwe0lWjgcSu_D9ZWHw8jt_uea4znruJbDyQJDdh8Pxnhcpx_lnJYdi9s0oOMcW5bp6U3mlfTJpqgJToAuIWJbSvdQ24AyGd_R2VbnP6UykakHt-7pcIa7qrh2jyd2ViOFQuQSRc6TzQK7Od8dRYM2ishVQ4jhpfEaYNIQsp46TXJ_CDlmCcbuL0BJVh_ezNLMZmBXB5I1mIC-68emL8MctpZ6rRmcyT7JGtEXA2bKjAzwtaC9XbTWPnQZMItb5yM1LNP3j5nmqHplEQJE2ANsg7pRm2rmA5y2PdYzx7mSH1mvFEYY-2ZSZvF193yQ0GBvTKP3ONPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df53d80fe4.mp4?token=IDeXktgMxf5aJGwe0lWjgcSu_D9ZWHw8jt_uea4znruJbDyQJDdh8Pxnhcpx_lnJYdi9s0oOMcW5bp6U3mlfTJpqgJToAuIWJbSvdQ24AyGd_R2VbnP6UykakHt-7pcIa7qrh2jyd2ViOFQuQSRc6TzQK7Od8dRYM2ishVQ4jhpfEaYNIQsp46TXJ_CDlmCcbuL0BJVh_ezNLMZmBXB5I1mIC-68emL8MctpZ6rRmcyT7JGtEXA2bKjAzwtaC9XbTWPnQZMItb5yM1LNP3j5nmqHplEQJE2ANsg7pRm2rmA5y2PdYzx7mSH1mvFEYY-2ZSZvF193yQ0GBvTKP3ONPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلانتری گلشن تبدیل به گوهشن شده , درگیری ادامه داره
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25136" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سیستان و بلوچستان درگیری های شدید گزارش میشه ، همه هم شکل و لباس هستند و حکومت درمونده شده ، نمیفهمه از ‌کجا و کی میخوره
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25135" target="_blank">📅 00:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سپاه خون دماغ شده دکمه پرتاب آبگرمکن از بندر عباس رو هی میزنه ، تنگه صدای ناله های شهید عججی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25134" target="_blank">📅 00:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25133" target="_blank">📅 00:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25132" target="_blank">📅 00:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرگزاری صدا‌وسیما : حمله مسلحانه به مقر انتظامی در گلشن  بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن سیستان و بلوچستان مورد حمله مسلحانه قرار گرفت. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25131" target="_blank">📅 23:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQcUrbKFTRt6qwcQuFsxisQ4xmYMZn1vvWE0XbEJGTzePho50PSAEVWCahEtNQC1QFOLNJFsrrwkG2gfXJdVLWzZdbwrpfZQySWzE8L4A4_I2ApOCeQyq7ufiAxn7oreBrEaRvZwFghU2DSvh_uLSAR5OidEz1fSQQ0YrfO5Rp8FHjW_tCHzAYvcU0jgNTpNcg6rXIpKPuTaDVLIUFDmM2sqdCG3D-24fWtVB69SO2_rbJ0VVHp6Xuo7m-r6LS23KNMmYaFIs8lJdPjqTzw6Q58hwZ9tDUWNNYxXXbbIg1GDXCWmw0wt24hD4PQrFs4WmYLZupeo3F91T1ztPXHasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع یک حادثه در فاصله ۵۱ مایل دریایی شمال «مدینة الشمال» در قطر دریافت کرده است.یک نفتکش گزارش داده است که هدف اصابت چندین پرتابه قرار گرفته است.
گزارش‌هایی از تلفات انسانی منتشر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25130" target="_blank">📅 23:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXbhlBwAyar5tA4fWA4V8e-nLDWEHx6SDxAp5vQ97YtkTuyW7bzhJdXN13BaYWunNDFJHV-fS9PL5vIBeTxa0ZTcW-W5S2o5lbr-q804HlBMHNv9bBCSejYrrp57i_HmQEak2Xwe_7Cs5iNlmjT7uEC7AtOofB2eGEQ2XZXXGM1lt_JF9jest6yaeNoTeNGU-ys0kWTZ0OrK7pbr2rAY2AqP8dcf1Qsiv0WZnIXQSAnMiUlhLituqeZBQBIiHnPyB_oCyEIl-Lm1619bW1xidwfJgnwf6rzZENXs6j_JGJfLCfP_OMXFFCtYK_VitWVtScUOAoWdeVl51gEW6PAtFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون نظام وظیفه: اگه لازم باشه برا جذب سربازای ۶۰ ساله هم فراخوان میدیم
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25129" target="_blank">📅 23:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25128" target="_blank">📅 23:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال 15 عبری: ایران در روزهای اخیر شلیک به سمت کشتی‌ها در تنگه هرمز را از سر گرفته است. ارزیابی این است که حمله‌ای از سوی آمریکا انجام خواهد شد و بنابراین ممکن است آنها بخواهند ابتدا حمله کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25127" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c43a91ec.mp4?token=pOmz1cDB36zHEtKK2LiEL9C5QQjmMUmucwExJ3CNIHqr9xlSXS0d5ehpTxakdeAWIIV_IOHXmhHslyKCZPk_BHlismyxtOXAi-shg7RGrVA4EamSQNZ4X4mn0eFMVRRW7cdBId9aP0Q6K1_lmk7dfj67rjacvS4A1AxYNsLg4wQ7-rEJ5NNlQ4Dw3jFNRM3_bJBo1qxI3Tn7nWxb4ozTI6IvBYQw_39r9CTFyy7u_67VMQIvzOawlKJ0Lv6jNcrs92CXr83C_l5C9mQpdFypOT0heeZVwSLPspJ1AOPDzoxwc_gEQTAA4BmtZkxpTPSy2v9pstw60Cuqj5SetGkhIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c43a91ec.mp4?token=pOmz1cDB36zHEtKK2LiEL9C5QQjmMUmucwExJ3CNIHqr9xlSXS0d5ehpTxakdeAWIIV_IOHXmhHslyKCZPk_BHlismyxtOXAi-shg7RGrVA4EamSQNZ4X4mn0eFMVRRW7cdBId9aP0Q6K1_lmk7dfj67rjacvS4A1AxYNsLg4wQ7-rEJ5NNlQ4Dw3jFNRM3_bJBo1qxI3Tn7nWxb4ozTI6IvBYQw_39r9CTFyy7u_67VMQIvzOawlKJ0Lv6jNcrs92CXr83C_l5C9mQpdFypOT0heeZVwSLPspJ1AOPDzoxwc_gEQTAA4BmtZkxpTPSy2v9pstw60Cuqj5SetGkhIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران:
فکر می‌کنم داریم خیلی خوب پیش می‌ریم. داریم ایران رو خیلی بد می‌زنیم.
اون‌ها هیچ‌وقت سلاح هسته‌ای نخواهند داشت، و این خیلی مهمه.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25126" target="_blank">📅 22:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhdJGsWOxQDYHD2C_9RrVQzTW8Qz3EUK92WD9MXOz2tQmFQGmkyFdEWbQT--HrPofrMs-ghIVJJMyKlyiQFuSCS30CeL95IdneQ_Q-sJEzJ-FIu6YVdoOPqxmNh2FWfTpYt-SZO4AcDf60eeX1kUig6gYeGwSLncmiUkcc90Ba_Mk4WrhIRPjNV8H75VJyCQKwJkkqRGduK7vxPjP84uPtvGoCgSkhivrGJr_4vKZgcSo2Tf3mAJ10O5PU8vCED8y703AzDhVoM2JVk7UN7pCYQTQ6vMo-odY7gXE53zYooC-eBE6_zcknFtdkM78kp-zAQruGtABsi4wAUdAKZ4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
این هفته، گروهبان ارشد تفنگداران دریایی آمریکا از نزدیک شاهد نحوه تجهیز نیروهای مستقر در خاورمیانه به
قابلیت‌های پیشرفته پهپادی
توسط سنتکام بود.
تفنگداران دریایی به
کارلوس ای. رویز
، گروهبان ارشد تفنگداران دریایی، درباره استفاده تاریخی سنتکام از
سامانه‌های پهپادی تهاجمی یک‌طرفه کم‌هزینه
(نمونه آمریکایی شاهد) توضیح دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25125" target="_blank">📅 22:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دو منبع دیپلماتیک منطقه‌ای به i24 نیوز: احتمال دارد تهران یک حمله پیش‌دستانه را آغاز کند، به دلیل نگرانی از یک حمله آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25124" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آتلانتیک:
احتمال دارد که ترامپ قبل از انتخابات میان‌دوره‌ای، دستور حمله دیگری به ایران را صادر کند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25123" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فاکس نیوز : خنثی شدن طرح تیراندازی در «مال آو آمریکا»
مقام‌های فدرال آمریکا اعلام کردند یک
طرح تیراندازی جمعی با الهام از داعش
که قرار بود مرکز خرید «مال آو آمریکا» در مینه‌سوتا را هدف قرار دهد، پیش از اجرا خنثی شد.
شیخدون عبداللهی محمد، ۱۸ ساله
، به گفته دادستان‌ها با داعش بیعت کرده و ابتدا قصد سفر به خارج از آمریکا برای پیوستن به این گروه را داشته است. بر اساس اسناد دادگاه، او قصد داشت در یک رویداد در
۲۴ اکتبر
تیراندازی کند و هدفش کشتن
۳۰ تا ۶۰ نفر
بود. اف‌بی‌آی پس از آن او را بازداشت کرد که طبق اسناد، وی از یک مأمور مخفی(آندر کاور)
یک قبضه AK-47 و ۲۰۰ گلوله
خریداری کرده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25122" target="_blank">📅 21:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرگزاری صدا‌وسیما : حمله مسلحانه به مقر انتظامی در گلشن
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن سیستان و بلوچستان مورد حمله مسلحانه قرار گرفت.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25121" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ درباره اینکه چرا شایسته دریافت جایزه نوبل صلح است:
من شاید جلوی
نابودی کامل جهان
را گرفته باشم، چون ایران هرگز سلاح هسته‌ای نخواهد داشت. اوباما این جایزه را گرفت، در حالی که هیچ کاری انجام نداد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25120" target="_blank">📅 21:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b83a25ca.mp4?token=Y4Ei-kKwEdVftq8pAakIu6xTgjTndeJ7avNVW9miBuuH97ZV4LRwjG4VFS3rHbLsD0ondTLhlh3bMLSf60TaNZ0Waz0_s5-KqdQm8UsFPfvv3r4E2rEqi0BetvEiAxYCjEG3utpguqrzWtPaCIGdfhME_EkNQAlhPZ0Lz74uCYMgAkCDBBjA07t9yavZhCNYbQW9B5VzzxltzZClG4mYy9HidkK9kgqqGkgdIC_wEPOammskY3w-NmiJzsJ4g5Hrtkbs_9PnHgbj1JP-H4qYtgqcXYmeNJ3YmhNQDJ1Dy52wV5CT04fb4XAnyis06jvx67oPeByEedxSwNMFCa5vnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b83a25ca.mp4?token=Y4Ei-kKwEdVftq8pAakIu6xTgjTndeJ7avNVW9miBuuH97ZV4LRwjG4VFS3rHbLsD0ondTLhlh3bMLSf60TaNZ0Waz0_s5-KqdQm8UsFPfvv3r4E2rEqi0BetvEiAxYCjEG3utpguqrzWtPaCIGdfhME_EkNQAlhPZ0Lz74uCYMgAkCDBBjA07t9yavZhCNYbQW9B5VzzxltzZClG4mYy9HidkK9kgqqGkgdIC_wEPOammskY3w-NmiJzsJ4g5Hrtkbs_9PnHgbj1JP-H4qYtgqcXYmeNJ3YmhNQDJ1Dy52wV5CT04fb4XAnyis06jvx67oPeByEedxSwNMFCa5vnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار فاکس نیوز: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: ما اینطور فکر نمی‌کنیم. به‌زودی متوجه خواهیم شد، اما فکر نمی‌کنیم که اینطور باشد
روس‌ها می‌گویند که این موضوع کاملاً تحت کنترل است
پیتر دوسی از فاکس نیوز: آیا همین حال و هوایی را که در آغاز کووید از چین داشتید، اکنون از روسیه در مورد طاعون هم حس می‌کنید؟
ترامپ: خب، چین زیاد چیزی نگفت و روسیه هم زیاد چیزی نمی‌گوید، اما آن‌ها می‌گویند که کنترل آن را به شدت در دست دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25119" target="_blank">📅 21:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333de74250.mp4?token=ljvTdvGj9zVPNGzc0_eHaTbuD6Pk8uU3KpqDWyVr5LIPf2mYwNMH9igCmi3Pz4DkBqgDc6Mxis3N0vwcmmaIkhyiY-cclA4nfByU4K_8Uu2c2Qhz_Ni3XtGgBEXz9YGniLasfgEyYG92V5htJFKJ05hPzawO7DD0IWOQW-okKt-1oL7dVH3TFtT3cWK_YR0KAugdtT3E3SYmTktgZThW_4R_ZnzKU5rVsM5sU9Aux6jQp1WsmcWT4YUZ9FEA-0vFrYWH3WfnhlkCXJLn6JHZxtYQzahECAZ-NQi_CJumc0ijBDfuHfl8jSiGJZX8TfQcACLgkTJcAFhNpll_Bctal63sEZ2TNLGQTOGP0RGnlFENOCPSymfij_VEjDCodBHoQPsRFOhpFf0wbFyUWRUNiYWwNmd7MoUxs2k_ZzLZaLSaoap_quGfMaGhmSioK8BcpUQ_th4RnQLVWSlEWhBq_8QjMUQLbxQ6Z99FNF6mm327FDwJ_PDYv0uw7zC6LykN-R9UHgDcjkyY1uVQ7LzXJdKBiKaYisCY6zBWmPFVzwYaVDjzGMBQGCVulK_44GsrHKCkTK_MJDVYo9Tb2YBpmDxoGx16gFLS2WKYv-ZcY7o8zC7UzAXyn3q-e5Ow208BjVkdqEvUIBb7mlTt1uy2pEeNPXgGKFAzv8cCNWZUouU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333de74250.mp4?token=ljvTdvGj9zVPNGzc0_eHaTbuD6Pk8uU3KpqDWyVr5LIPf2mYwNMH9igCmi3Pz4DkBqgDc6Mxis3N0vwcmmaIkhyiY-cclA4nfByU4K_8Uu2c2Qhz_Ni3XtGgBEXz9YGniLasfgEyYG92V5htJFKJ05hPzawO7DD0IWOQW-okKt-1oL7dVH3TFtT3cWK_YR0KAugdtT3E3SYmTktgZThW_4R_ZnzKU5rVsM5sU9Aux6jQp1WsmcWT4YUZ9FEA-0vFrYWH3WfnhlkCXJLn6JHZxtYQzahECAZ-NQi_CJumc0ijBDfuHfl8jSiGJZX8TfQcACLgkTJcAFhNpll_Bctal63sEZ2TNLGQTOGP0RGnlFENOCPSymfij_VEjDCodBHoQPsRFOhpFf0wbFyUWRUNiYWwNmd7MoUxs2k_ZzLZaLSaoap_quGfMaGhmSioK8BcpUQ_th4RnQLVWSlEWhBq_8QjMUQLbxQ6Z99FNF6mm327FDwJ_PDYv0uw7zC6LykN-R9UHgDcjkyY1uVQ7LzXJdKBiKaYisCY6zBWmPFVzwYaVDjzGMBQGCVulK_44GsrHKCkTK_MJDVYo9Tb2YBpmDxoGx16gFLS2WKYv-ZcY7o8zC7UzAXyn3q-e5Ow208BjVkdqEvUIBb7mlTt1uy2pEeNPXgGKFAzv8cCNWZUouU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل: حماس همچنان از بیمارستان‌ها برای فعالیت‌های تروریستی سوءاستفاده می‌کند:دو عضو حماس که از
بیمارستان کمال عدوان
در شمال نوار غزه خارج شده بودند، بامداد چهارشنبه شناسایی و کشته شدند. به گفته ارتش اسرائیل، یکی از آنها در حال
کارگذاری بمب‌هایی بود که از داخل بیمارستان به منطقه خط زرد منتقل شده بود
. فرد دوم،
محمد طموس
، تک‌تیرانداز شاخه نظامی حماس بود که هم‌زمان به‌عنوان
کارمند امداد و نجات
فعالیت می‌کرد. ارتش اسرائیل مدعی است حماس در هفته‌های اخیر از بیمارستان کمال عدوان برای فعالیت‌های نظامی و بازسازی توانمندی‌های خود استفاده کرده و این اقدامات را
نقض توافق آتش‌بس
می‌داند. تصاویر عملیات نیز توسط ارتش اسرائیل منتشر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25118" target="_blank">📅 20:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتاق جنگ با یاشار : صدای انفجار در حیفا همه را ترسانده. ولی هیچ آژیری فعال نشده. در نتیجه نظر من این است که از آنجا که حملات سنگینی در جنوب لبنان در حال انجام است، به قدری که جنوب لبنان را بد زدند، صداش حیفا همه ترسیدن یا سونیک بوم خود جنگنده ها بوده
@WarRoom
این خبر بروزرسانی میشود</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25117" target="_blank">📅 20:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رویترز: آژانس بین‌المللی انرژی اتمی می‌گوید پیش از حملات، ایران
۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد
در اختیار داشت. پس از حملات، ایران میزان و محل ذخیره باقی‌مانده را به آژانس اعلام نکرده و بازرسان نیز هنوز به سایت‌های هسته‌ای بمباران‌شده دسترسی کامل ندارند. آژانس برآورد می‌کند
بیش از ۲۰۰ کیلوگرم از این ذخیره همچنان در مجتمع تونلی اصفهان باقی مانده باشد
و بخشی دیگر نیز در نطنز بوده است. رویترز تأکید می‌کند که
مقدار دقیق اورانیوم باقی‌مانده مشخص نیست
و بخشی از ذخیره نیز ممکن است در حملات نابود شده باشد؛ بنابراین نمی‌توان گفت مابقیِ ۴۴۰.۹ کیلوگرم حتماً از بین رفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25116" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">توییت جدید
🚨
🚨
🚨
🚨
https://x.com/yasharrapfa/status/2107855000521293885?s=46</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25115" target="_blank">📅 18:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رویترز: ایران ماه گذشته
۲۰۰ میلیون دلار
به حزب‌الله لبنان داد تا این گروه به خانواده‌های لبنانیِ آواره‌شده در جنگ با اسرائیل کمک مالی کند.حدود
۵۰ هزار خانواده
که خانه‌هایشان تخریب شده یا امکان بازگشت ندارند، در اولویت قرار می‌گیرند و به هر خانواده در مرحله نخست حدود
۳ هزار دلار
پرداخت می‌شود.این نخستین کمک مالی قابل‌توجه حزب‌الله به پایگاه اجتماعی خود از زمان آغاز جنگ در ماه مارس عنوان شده است. انتقال پول از طریق واسطه‌ها انجام شده و این واسطه‌ها حدود
۲۰ درصد کارمزد
دریافت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25114" target="_blank">📅 18:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صدای درد و دل تنگسیری و سلیمانی‌ از تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25113" target="_blank">📅 18:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbBTQfLBbqxXmr2acVLik_sEddmKfGR3OFiYaPM1ZDi7BfCfmLiuB9bSQ0gemGsgNvTFmRuf4YqHF9iLi06iJXn6zXn0cryt9vakYaQZ_-1uSrICxgSiBapvPzAdtoVGsFiTdvWz_C-Zr4ynQgG44kkmw69mdGx5T7KxUj23KWv3i_5K_dEQFLxIhm1N-pjRYehFsTEYzoOfg6blgx2C155Rbwe_Cttuym6AA8Plivk5Xh14uUHWDKPp29rbmbTEEI0egXp2ddfGutN69s7SpKFcenU8gIixsGt7ivz1TI4P1xA0f7LqqQhp8BbakykvlqVSjY9nPVWAtngADgof5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد نیویورک پست از عکس تروریست های حماس که یک دختر بی گناه اسرائیلی را که در فستیوال موزیک بود کش‌ته و حمل می کنند
نیویورک پست : تا همین چند وقت پیش، اگر به آن‌ها می‌گفتید “یهودستیز”، برای توصیف این بیماری روانی‌شان کاملاً کافی بود؛ اما در سه سال گذشته، امثال آن‌ها آن‌قدر از خط قرمز رد شده‌اند که این کلمه دیگر اصلاً نمی‌تواند عمق لجن و پستی آن‌ها را نشان دهد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25112" target="_blank">📅 18:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317b1bb05e.mp4?token=g09xbWRrQo3XAK7eyCSrDBZW70aqrE-x5jyueDij9AFp2DDE2Mq9wwGdDMq4-e1RDX8ySZ6FeYHk2rVSFI2asfkX48YXuS-4YM6AvC-PGJyJz3-0ZHTORmVS79UfMEJqn-ZquHmeb5DV68ERcLBeIRLZ1yOPd4b34kavm7V9D21Y6GKWQ0kD_g4g0yAu7x0kQBhxXHvluLC-ZtmuTWqpm0fiWcdGYvJ5qSwpORlVrxBUH4xNkSvVEBeP1ELBcLDnvzifMI8xFnAWQ69n0_IbMtLBdKGaLmzI207FX-wCe-L1STt87hnnRTFzuymKDql7E75rsIuJKgqqay4ysslK2AW8k1BlufNDiiAt_JzgA8mtJKVbRKeRUUQ2wyP8izvo2ZutlbO1WSgpIJo6E-i-4TC9ToeMC3-OggNoEYM-5lhxoOS5t1JBqCQQyP1T94ehg6pqLdjZhKEQMNfDRXyjWy4ssCwO4f_11kYIw8DD4MRqIVT6Y4ZOt5DTHcaqNnp5o4OdCtasyMdSi5BYs9eOfCn7e4l-QCLF-gAwHknB7Nw2VxYaRj5WmMqA2tO9qpzvWowrLk9F6xLmbkZICF8u5yEYN8OYPCrg-e0NiKYMgyheQgJIhuDwxNEmCnfPcoWIGMB4ANzqqpHlGetPoq0KyagjNuzFyKTwYaR7R-gtNBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317b1bb05e.mp4?token=g09xbWRrQo3XAK7eyCSrDBZW70aqrE-x5jyueDij9AFp2DDE2Mq9wwGdDMq4-e1RDX8ySZ6FeYHk2rVSFI2asfkX48YXuS-4YM6AvC-PGJyJz3-0ZHTORmVS79UfMEJqn-ZquHmeb5DV68ERcLBeIRLZ1yOPd4b34kavm7V9D21Y6GKWQ0kD_g4g0yAu7x0kQBhxXHvluLC-ZtmuTWqpm0fiWcdGYvJ5qSwpORlVrxBUH4xNkSvVEBeP1ELBcLDnvzifMI8xFnAWQ69n0_IbMtLBdKGaLmzI207FX-wCe-L1STt87hnnRTFzuymKDql7E75rsIuJKgqqay4ysslK2AW8k1BlufNDiiAt_JzgA8mtJKVbRKeRUUQ2wyP8izvo2ZutlbO1WSgpIJo6E-i-4TC9ToeMC3-OggNoEYM-5lhxoOS5t1JBqCQQyP1T94ehg6pqLdjZhKEQMNfDRXyjWy4ssCwO4f_11kYIw8DD4MRqIVT6Y4ZOt5DTHcaqNnp5o4OdCtasyMdSi5BYs9eOfCn7e4l-QCLF-gAwHknB7Nw2VxYaRj5WmMqA2tO9qpzvWowrLk9F6xLmbkZICF8u5yEYN8OYPCrg-e0NiKYMgyheQgJIhuDwxNEmCnfPcoWIGMB4ANzqqpHlGetPoq0KyagjNuzFyKTwYaR7R-gtNBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوش بدروسیان: شما در سازمان ملل گفتین روزی که خیلی هم دور نیست، مردم ایران آزاد خواهند شد. منظورتون چی بود؟
نتانیاهو: «دقیقاً همون چیزی که گفتم؛ جمهوری اسلامی سقوط خواهد کرد.»
شوش بدروسیان: می‌تونین زمانی براش مشخص کنین؟
نتانیاهو: «بله، می‌تونم؛ ولی ترجیح می‌دم علناً زمانی اعلام نکنم. مردم ایران در زمان درست و وقتی شرایط مهیا باشه، بلند میشن و این نظام رو سرنگون می‌کنن.»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25111" target="_blank">📅 17:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ممباقر ، رئیس مجلس ایران:
«برنامه دشمن بر انجام اقدامات خشونت‌آمیز در داخل کشور متمرکز است.این برنامه و راهبرد دشمن نشان می‌دهد که اولویت اصلی ما نیز باید تقویت تاب‌آوری اقتصادی و تأمین امنیت داخلی باشد.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25110" target="_blank">📅 17:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مرد خردمند ، مارک لوین در‌ اکس : من طرفدار پروپاقرص رضا پهلوی هستم. @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25109" target="_blank">📅 16:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25108" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSh</strong></div>
<div class="tg-text">اقا یاشار این مرد خردمند که اول اسم ایشون همیشه مینویسید  چیه</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25107" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25106">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شاهزاده رضا پهلوی: به مردم اسرائیل: در سومین سالگرد ۷ اکتبر، در غم، یادبود و همبستگی در کنار شما ایستاده‌ام. ما هرگز کسانی را که به قتل رسیدند، رنج خانواده‌هایشان و بازماندگان این جنایت را فراموش نخواهیم کرد. جمهوری اسلامی که حماس را مسلح و حمایت کرد، همان…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25106" target="_blank">📅 16:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اتاق جنگ با یاشار | تحلیل بازار: برخلاف برداشتی که ممکن است از حرکت امروز بازار ایجاد شود، ریال ایران فعلاً وارد یک روند پایدارِ تقویت نشده است و آنچه در بازار دیده می‌شود بیشتر می‌تواند ناشی از دخالت ارزی، عرضه دلار و اصلاح موقت پس از جهش اخیر باشد. هم‌زمان،…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25105" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری فرانسه:
همزمان با نگرانی‌ها درباره مرگ یک کارمند  آزمایشگاه تحقیقات طاعون در روسیه و پیغام آمریکا برای کمک ، مسکو نیز در جواب اعلام کرد آماده کمک به آمریکا برای مقابله با شیوع بیماری‌
سرخک
است. سازمان نظارت بر بهداشت روسیه اعلام کرد این کشور می‌تواند متخصصان، تجهیزات آزمایشگاهی و ابزارهای تشخیص و پیشگیری در اختیار آمریکا قرار دهد. این نهاد همچنین از تشدید وضعیت سرخک در چند ایالت آمریکا خبر داده است. در همین حال، مقام‌های روسیه می‌گویند تاکنون هیچ مورد تأییدشده‌ای از طاعون در میان افراد در تماس با کارمند جان‌باخته پیدا نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25104" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hruFExSSRlbAW8s9z5gufxq7a3f0saJoeJm5ytjhUx4nzNlc6dzvSiRBECrdEySrd768y8Fbi-iimwRBb5_HIGX1VEs7bAFB7njkzPC9Ce6jGbOewzdfdMXAKXY40yu66Bv0nqnAetripy-Wls0JO-cpzj4StA2QnwRRmPPcka8jfuewLHXan_ND_ZMWhZnT8lGP5-otBkcTRQdupSATS5UbSchFBJFvGMcRzpwSpMwD96NaRsBwG0cpjFfIXsRUc5tqEOK9Zu0HOBTipqthUzH8uTm_4rfmioIU7NFL7nEpNeMkr-ThvREmGKMM5gUhOx3r9mZWJlVYqItRJx9iKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:
تالار «کهکشان غدیر» در قم پس از حضور علی دایی و همسرش در یک همایش خصوصی و آنچه «عدم رعایت حجاب» و «هنجارشکنی» عنوان شده، با دستور دادستان قم توسط پلیس اماکن پلمب شد. طبق اعلام قرارگاه امنیتی سجاد، حضور افراد بدون رعایت ضوابط در این مراسم موجب اعتراض‌هایی شده و برای عوامل برگزارکننده نیز
پرونده قضایی تشکیل شده است
. دادستان قم نیز تأکید کرده با موارد مشابه، به‌دلیل «شأن و منزلت شهر قم»، برخورد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25103" target="_blank">📅 15:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایران‌آنلاین:
مسعود پزشکیان در تماس تلفنی با ولادیمیر پوتین، زادروز رئیس‌جمهور روسیه را تبریک گفت و برای دولت و مردم این کشور آرزوی سربلندی و شکوفایی کرد. دو طرف بر
تداوم و تقویت همکاری‌های دوجانبه و راهبردی تهران و مسکو
تأکید کردند. پوتین نیز ضمن تشکر از پزشکیان، بر ادامه همکاری‌ها در چارچوب
معاهده همکاری جامع راهبردی
تأکید کرد و گفت روسیه آماده کمک به تلاش‌های دیپلماتیک برای کاهش تنش‌های منطقه‌ای است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25102" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسکای‌نیوز عربی به نقل از یک منبع نظامی اسرائیلی:
اسرائیل فعلاً قصد عقب‌نشینی از جنوب لبنان را ندارد و بازگشت ساکنان مناطق موردنظر نیز ممکن است سال‌ها طول بکشد. این منبع مدعی شد در بخش‌هایی از جنوب لبنان، در جنوب «خط زرد»، همچنان زیرساخت‌های حزب‌الله وجود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25101" target="_blank">📅 15:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏دوستان و همشهریان ⁧ عليرضا سپاهى ⁩ بخاطرش ماشینهاشون رو گل زدن و کاروان جشن دامادی راه انداختند و با سوگ می‌رقصن…  @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25100" target="_blank">📅 15:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز به نقل از یک مقام ارشد ایرانی
:
هیچ مذاکره‌ای میان ایران و آمریکا
درباره برنامه هسته‌ای تهران
در جریان نیست
.
آمریکا ابتدا باید شروط ایران را بپذیرد
تا مذاکرات هسته‌ای امکان‌پذیر شود.
به‌رسمیت‌شناختن حق غنی‌سازی ایران از سوی آمریکا خط قرمز تهران است.
ایران هرگز از حق خود برای غنی‌سازی صرف‌نظر نخواهد کرد، اما جزئیات و نحوه غنی‌سازی می‌تواند در ادامه مورد بحث قرار گیرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25099" target="_blank">📅 15:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70eabff49d.mp4?token=WkEDypRAKJbj_Ndp3bmz8qf3dslpaPrRVEO16pBONpaCUfOn8U4hRghiXQxEE50BxiRqn5SqjYZPrnDV7OI2ArZc1GufDQ0WfG4weCP-4mMUrb7uMY2rWwNXP428pqW6L8jph1ZGd_tUgJzqE2LquN1vCXX9irHylk-IICI9nlCoCLwcjRUQaIv8bgjj5I_diL5FIKEydbH6ADqBRsqpIT5ROoQYye7zku5L2hfnQdIXl406OqBeoecZiO-s3OOV1P3WH6a9w3l-EIuWd-PcXzfpLOvh0dfWMMUsQBdgEkZlB2WiYoadXgMijoxvTuLUmSNyhzL7mqdTtm9-PrZBZg9uqugXc2D5Y6RgyESYky8CK5pz_SGJqILJQv0V3NN1zeDxBk-YQZcbLllKB5OIKT-1ME6dhiBqbbHZZR5qeezmcQurWvXOaGOn_0P6x48Rve48Y2WSMZOwQeFjHm76Q3EtP8lFIuYGJlvt1hoASrQlm-gyDpkJ8bypeVLuvv5wE4jOHcaomiPTfu0iWGa3RLsCZGqb5BoHMkcdfHfODmxhcDfuH9KOvEOEe4GwQmLkvel4xIdhNM6O6vjqbSkp8JwpFFbUynW7L4J6UyvmbVKePIxG0yzuEKX7F6IHb91yVKaQmnaz2Yss2B3mYThfHBxlgE4pfpcO62TUo1G2S0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70eabff49d.mp4?token=WkEDypRAKJbj_Ndp3bmz8qf3dslpaPrRVEO16pBONpaCUfOn8U4hRghiXQxEE50BxiRqn5SqjYZPrnDV7OI2ArZc1GufDQ0WfG4weCP-4mMUrb7uMY2rWwNXP428pqW6L8jph1ZGd_tUgJzqE2LquN1vCXX9irHylk-IICI9nlCoCLwcjRUQaIv8bgjj5I_diL5FIKEydbH6ADqBRsqpIT5ROoQYye7zku5L2hfnQdIXl406OqBeoecZiO-s3OOV1P3WH6a9w3l-EIuWd-PcXzfpLOvh0dfWMMUsQBdgEkZlB2WiYoadXgMijoxvTuLUmSNyhzL7mqdTtm9-PrZBZg9uqugXc2D5Y6RgyESYky8CK5pz_SGJqILJQv0V3NN1zeDxBk-YQZcbLllKB5OIKT-1ME6dhiBqbbHZZR5qeezmcQurWvXOaGOn_0P6x48Rve48Y2WSMZOwQeFjHm76Q3EtP8lFIuYGJlvt1hoASrQlm-gyDpkJ8bypeVLuvv5wE4jOHcaomiPTfu0iWGa3RLsCZGqb5BoHMkcdfHfODmxhcDfuH9KOvEOEe4GwQmLkvel4xIdhNM6O6vjqbSkp8JwpFFbUynW7L4J6UyvmbVKePIxG0yzuEKX7F6IHb91yVKaQmnaz2Yss2B3mYThfHBxlgE4pfpcO62TUo1G2S0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرویس امنیت دولتی گرجستان: یک شهروند گرجی به دلیل
نگهداری غیرقانونی مواد هسته‌ای
و تلاش برای فروش اورانیوم-۲۳۸ بازداشت شد. به گفته این سرویس، فرد بازداشت‌شده قصد داشت اورانیوم را به یک
تبعه خارجی
به قیمت
۷۰۰ هزار دلار
بفروشد. مأموران امنیتی پس از دریافت اطلاعات درباره این معامله، تحقیقات را آغاز و این فرد را بازداشت کردند. مقام‌های گرجستان ملیت تبعه خارجی را اعلام نکرده‌اند و تحقیقات درباره پرونده ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25098" target="_blank">📅 15:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/25097" target="_blank">📅 15:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">در پی انتشار ادعاهایی درباره آزادی یا عفو امیرحسین مقصودلو (تتلو)، پیگیری ها از وکلای وی نشان می‌دهد تا این لحظه هیچ ابلاغ یا سند مکتوبی درباره آزادی، عفو یا تغییر وضعیت قضایی تتلو به وکلای او ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25096" target="_blank">📅 14:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رویترز به نقل از مقامات: ترکیه، کمک‌های دفاعی و فنی به عربستان سعودی ارسال کرده است تا به آن در جنگ علیه حوثی‌ها کمک کند. این کمک‌ها شامل سامانه‌های پدافند هوایی، اپراتورهای هواپیماهای بدون سرنشین، و همچنین اطلاعات، نظارت و شناسایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25095" target="_blank">📅 14:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRYuYbTdsm6Oj9wRhBJE_xEAcwFTlsjYwfQIG1qB02V6LYPOzPqpSeq_AMZ3bHX5x9KL_JHLynnOJ7HaRMLiyWVfqfK3UmtCAP_lHjRZoqZhQ8qIF4r8cnP6fxpe6JtDLZE1ZRbUiQl5W4A_WGvSWlhfsM44pJlT_fgqjDKL1gSyBtfxTt40Ebbh1nF2ViJLHhZEmB_mfjXOLCwbhNlR5bDIFpwHVSIhZwDgQHjmjpu6QvQH8YY4Bha9tSHi3psUrkKUHMt1lrWDm1nCD79szFdGZLp7ifrzB2bO63FHeVt9OG_g6WRia9fyA0JPgJQOAGptg0q03Tz8Vy1tS_F6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند جنگنده F-35B Lightning II متعلق به تفنگداران دریایی ایالات متحده، هم‌زمان با حرکت ناو USS Boxer (LHD 4) در منطقه خاورمیانه، از عرشه پروازی این ناو به هوا برمی‌خیزد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25094" target="_blank">📅 14:33 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
