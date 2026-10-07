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
<img src="https://cdn4.telesco.pe/file/Yl2RUoYiemKQi5rNNYFyfLcm8o5MhhfneU4uZsocHtX5zEUuhKs9lFOBdlwRxVQNq_gNKGKT4fKfcouyhx3ZdSCt1ukt_EyMyP8R4jnAFp5kbhF6RmT0o7ZlqTTd75DuiPCodm__EHdD5uUuCnTFPxBYgLxnVSrU6unGDo4SYvdl2OYV3EXgZl8EDQAPW1FfO3aws_D_QcEqicv9bksTa7Dv4dHSX7EJ7sz_ACPgwXtiwRhAGsfwS2YUfcwRbACWszHpjR3bW_o4eo9YlRAEtp_xi-OTl-oOSECXoD66xF4FdbIoET0CjhR94NBI_8WCv_uP6Asl1CQ9G9i98iUcrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 06:03:32</div>
<hr>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=FZiUIeJHy4Tsqr0w1VZOypUCTeug2K_FaNq05khBNSAcXKCAvW-ol7rT8oTzcujZpIHPxr-etTbayC4gKdKADVGlJcqabysqJv_mBxy09lwAaqx-C2Ww8cOsBO6nriWrCOMIqciZGCpfgFfFlpCY3X0Bf6lTp0GDWE4rvuAH1zanI0fba3DfQRtu1ul3lEfgGvkRlmzFHAiOzDUwczZvMhTEGVFwzHXJOhD9GMItqqOSanW68QASk6gnljGhZESxUVB_CWzFJbtL0JnTVQzC12FOuSHKhFu-KNPbKVvXKuKYBG1opcBk6RkdKXdE1a28FH75TnqI7cICuGFLSiiC4EwNTYlech5noXVJ3mRBhr0TuiMcFItNQ28I-bn-u92Vwrm-3wDyb-UMOMrfaLOgNGKN5TPd8I36u10PmYxbQpQJReeysPXbkFuMNVAV52H-fjBkVFhvFCEM81DpR7GVnUz0aw8BJB3PMRbO_tME0qr7eNb3wkV0oReM5xsELz8LcK2GWH_Vrzg1---3YLunBKpZDBsSYSJAIIfmvLKw1ShqkUZIpACiPVKgwzESoSi5DTrXJ5kjT7SkpMFvuMdDHypm7YCqAztyk6NbEQ7gbi6j965nsw650NdNG9hcaspam9Rn5Cl0KjjCjjdQanzIvYU9_JQoGVMm77J9SNDU0xo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=FZiUIeJHy4Tsqr0w1VZOypUCTeug2K_FaNq05khBNSAcXKCAvW-ol7rT8oTzcujZpIHPxr-etTbayC4gKdKADVGlJcqabysqJv_mBxy09lwAaqx-C2Ww8cOsBO6nriWrCOMIqciZGCpfgFfFlpCY3X0Bf6lTp0GDWE4rvuAH1zanI0fba3DfQRtu1ul3lEfgGvkRlmzFHAiOzDUwczZvMhTEGVFwzHXJOhD9GMItqqOSanW68QASk6gnljGhZESxUVB_CWzFJbtL0JnTVQzC12FOuSHKhFu-KNPbKVvXKuKYBG1opcBk6RkdKXdE1a28FH75TnqI7cICuGFLSiiC4EwNTYlech5noXVJ3mRBhr0TuiMcFItNQ28I-bn-u92Vwrm-3wDyb-UMOMrfaLOgNGKN5TPd8I36u10PmYxbQpQJReeysPXbkFuMNVAV52H-fjBkVFhvFCEM81DpR7GVnUz0aw8BJB3PMRbO_tME0qr7eNb3wkV0oReM5xsELz8LcK2GWH_Vrzg1---3YLunBKpZDBsSYSJAIIfmvLKw1ShqkUZIpACiPVKgwzESoSi5DTrXJ5kjT7SkpMFvuMdDHypm7YCqAztyk6NbEQ7gbi6j965nsw650NdNG9hcaspam9Rn5Cl0KjjCjjdQanzIvYU9_JQoGVMm77J9SNDU0xo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAAJtGsYhKZ2KbSpP-gz4HwySCzd2d1BcUFVb6GKmvRov4SPbb3C2zfV9TK97aiSc817z2r4rm9jyEux3Z8m6menLemd1bLdqmbyEsRmmI-kNTJi0j6NZxwSVGvMxoQlQSCEILFK8GHtMTncs7Z_8aXgAFXrAsOuwvv67kWPq_-ymLm7A90ZvdRSZUkxBnHmZ8K0W2Xbv1DYQk9SMIvaWuZ6DUw6OI-0Ojz4lFw8Y-ifFtcfzipf9tXyC8A30-tc5wlxbgWd9w2PdOg0Nr5R6kgpbDfFlbDuz18jb6jrwCyAOABX_4GCjoMx3LzlRZ_5CK2YKST1bgg6bnET35PowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ny7ojywhUYJs2hkkdpdFbol6ScxGD8FImhWRLZo66WNDvnxDE7PbJn9ZE1BLH1dea0kPAMVNACmu9344sFbbr-jkn4M6fSVDRrVy8ay6HFyDW2zaNLWAyakAlYYX9aPaOvk8VSCkFa91o7AkgG5s3IXLChKTDf5LS6vGTzdYRcd0TRIuYOBKjvcFvijWSBN_oPtZyq9VXwy-qKp3-pMCoBL3VukfzjvsMaEMZRcxsBZZ4Q2RT-xRYjKkxiL46dz2DwnLRWMHEbxYJARJMpQNSbQLIgcZIK8wZUfBLTGQwQdDsaB76OBQ9MY_6Q9AYu-qEOmtjuVFEe8AtK3FGWGm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uduBcBzBjCvZf8tDwdH79i8oLwN98lvJxPUlzcB-Q4MBIvVpQCnWYUx7Y771I5eBEtcxViVv46PLp41keoXztZn9nepsB5Afg5-frzuBE7geGDhSMAL0fMbUR8g6KGcr-sbnl0QPtfjMCm6SljsL2UD7VkY9kyJ1btn1j3HRlX51b-VuADNm52oOD2_z3KLhZb1acvD0afd0U-jQX9cUWW7Lt-7kzZYfGbjbIAMZaaiYxno6pZMT9qRD2BRZGMbTQEOL3CqwJXYwy_ZUV8YrX-O_D7iSG3UJS2uhmYe6Dv0CCBSA7lm7iSJ_UAo3v083VWDx-q2DahYSQVObVRQFXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQqkbam3U5s3oz4T0wXdwG1PbYUSMNkylB29C9kLYgC0FmTJTwFLJIvjpimyGzsP0WK4rF4nbJdse66j7dQ_BdmoKgN3att5hgV2PXlQMsqMsytWTpk3eA9Xq2wGvLxySsWUuA4v8MRQm-qQK9KUvvuo4hf0sjfgvJAffxOzKgfigTss-HVdc8GiOdUgluZqlcc6hVxMpKyEspQsPH2ImbU6pCHPZ1qtYnaDY_fVECDQzEZnfW7MVXRXo3ML_jo7dpofpib21W5kAQuoJn0WmjF8NB_8nxlusiX3cWBlyk_LkQa2ckd91xHVcZ7LCGmg5aEG4an-lnuwm5YSC7aRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2w6ZUYXRgZKPh4YEBAVWP7xH2zBUszDoKjIF6UWNaro0D7pjG6Lscq0V51Kra4EBShVzmdX-rVRGvGUVY89BeMGhkA_4DlC3zKvtkvXXOeT57HreoUfZoLX94QBRyDlnpi6s8i_tE9hitvuVC1AucGhvUC8cz7i9cn-dIPJk1ozjHk_jqducSWA3FlA5IILSIIxWfrQmJtxghBFAyF8VHf2Wqi2BWjIsbsT8dti2DySuggfB62WZW5zzLBhOBvzpxIcJU5SlDef6iy_bK98RR_9Kv5DH1iRuB4oqpem__Al3x6JJPAGmiRKFk22FvEzNnHlE53Af0HCiD9LYCJMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qt5mRtnA22CDLdKRL4SCGyyNsOdsfsEEV5dy6asyYgkQsYqo1VzvYav6wndgXVufMWXk2cbB3OZ3Y4N9Kr_6HZ2yk5y55y8fcn_e4PuFfcpJLfWI7_iiXf_AFWhV3R8MkIIfKKYBeyk-V8AmYUNIBCZSVdPJoLSgUQ_RO5fk59eT8MNh2HAnI68zLND9FiBi80PCOW_NN5zKOyov1MtZ7dDFHAH20c1bDph5iJ6wAHdqkLKSB50e6sb7DIxK7A-925CU0DcNAm40D2d6BdImABcCzSe7C1Go5MVNojnzEoqe8R6syfSxp3Npb3OLV4sRwFDqDOksGY1s_qeAune1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Yjtga5s5-v1_-EONYmaX96PGT9lYLhbGyPKWZEAebgYDf2--uPJWWDLHGT67hRTnGsQOtPNfJkwsDji9-hA9ZjpUDGLko-Gb1t3f2NdKP63AGa2eI-S6GndZNZXg6UGQ0nkLbyCFcUT9zL1BLJs7IPrfud_jXHe0pf5ktqQCnwbXwnemO5KdsjyvxPp55qt2Fb9cijwJV1aaRVzH4Mlf7fuHLVW5laOq7Ep5E_c2Fp3shcBG8lUlk_qPDZRNA-QdVIohZnz_RqOavBJyZU2NLrXobNGKmEsc37s8y_WVigjSihg7rtkZdiKXIS_UdMyqrZoj7-K68vZ2Y3JpPzdJYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Yjtga5s5-v1_-EONYmaX96PGT9lYLhbGyPKWZEAebgYDf2--uPJWWDLHGT67hRTnGsQOtPNfJkwsDji9-hA9ZjpUDGLko-Gb1t3f2NdKP63AGa2eI-S6GndZNZXg6UGQ0nkLbyCFcUT9zL1BLJs7IPrfud_jXHe0pf5ktqQCnwbXwnemO5KdsjyvxPp55qt2Fb9cijwJV1aaRVzH4Mlf7fuHLVW5laOq7Ep5E_c2Fp3shcBG8lUlk_qPDZRNA-QdVIohZnz_RqOavBJyZU2NLrXobNGKmEsc37s8y_WVigjSihg7rtkZdiKXIS_UdMyqrZoj7-K68vZ2Y3JpPzdJYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=TDf4nQhth07GIWgcIRalT8uVXCBXrLjTNaf-g5QDetRzL8DBZgVNLSTIfW0OtFpCVZxtDj3cFRThcxvxZ-ipwsECMYSxzL5Q--P1YVtVTOf0-iqxtl2hBylOAqubHP2lJtMKbwag-gJr5tgH6JlyNN_630FLfZll0qsGPELSM5MJ5OofcV5etJ1n38br0uxR92g96kBYyoGth0tlZOYjEjAHdKUYApvBv1O6KUbKUs9ey8jVvXeOuWoFHoCu9e8ZSW2s12SQqQfnw6hNRWgKyddxYWSTM34PAYOQyBMr65RJMXRHic8DwcTk-FnsAkgrlqfITrzyyhKeketRfESYHRSREEmmxhTWQuBnIhCAF4JOTBE8IOHK-T4-eLqpx7841aKFGMvoIqQ2h7_CBCZOUwAEagS-J-fiOpOsDn1qJbfLPte-7678RecHN3MyIoxm54mp5UZzTXLe_T53P-FDSXAcpfLo0KhITbJcN0NV8pBuBJnC_toiAyMvsjgRNxm6h8yfbcSVGZCR_wNfeYBcHEbTL65XbHegQ5O3m2hrGtM04TYl-cBS6SkGHMesWyQKP2_18LnAhYJZURCvXUv5mU4KPNCTGsXsHFRGFGmbdBS-hTCShpjdTFhCY_TGSzyrFdWM_IIDjSZq_IJUifWFHGIa7w9pSGgOmWmjAMBL0zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=TDf4nQhth07GIWgcIRalT8uVXCBXrLjTNaf-g5QDetRzL8DBZgVNLSTIfW0OtFpCVZxtDj3cFRThcxvxZ-ipwsECMYSxzL5Q--P1YVtVTOf0-iqxtl2hBylOAqubHP2lJtMKbwag-gJr5tgH6JlyNN_630FLfZll0qsGPELSM5MJ5OofcV5etJ1n38br0uxR92g96kBYyoGth0tlZOYjEjAHdKUYApvBv1O6KUbKUs9ey8jVvXeOuWoFHoCu9e8ZSW2s12SQqQfnw6hNRWgKyddxYWSTM34PAYOQyBMr65RJMXRHic8DwcTk-FnsAkgrlqfITrzyyhKeketRfESYHRSREEmmxhTWQuBnIhCAF4JOTBE8IOHK-T4-eLqpx7841aKFGMvoIqQ2h7_CBCZOUwAEagS-J-fiOpOsDn1qJbfLPte-7678RecHN3MyIoxm54mp5UZzTXLe_T53P-FDSXAcpfLo0KhITbJcN0NV8pBuBJnC_toiAyMvsjgRNxm6h8yfbcSVGZCR_wNfeYBcHEbTL65XbHegQ5O3m2hrGtM04TYl-cBS6SkGHMesWyQKP2_18LnAhYJZURCvXUv5mU4KPNCTGsXsHFRGFGmbdBS-hTCShpjdTFhCY_TGSzyrFdWM_IIDjSZq_IJUifWFHGIa7w9pSGgOmWmjAMBL0zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS7N4fKl3M9dreCbPWAoDCcnOxipuzUPkliKcCk4yyTfpUGeMTTc7Qu-U_o64x-hZsJFXY1_F4GLnlhodQP9E_jPotp46sIyOTeXrKBinO7itc3m2DR8i8-O_hnMJL6NoNu7W-AhbE0HYnmGESwzu3DCrlXOPaYscgUjdpAG9vYOoW7qxacipej0xwZPdNaeVNiODWBSCoF4u11T7aTwaErtUeWQVlXQFmGDxhTfN-HD6vHsz2dRyJlMHKC5vmmK5fV18pfR2pwC22KVAb3egyhWCIYV3LExFU7Nju1nQgGuOmnpOhhMDZQe9LCPBtTAVVBaupv5T0G22gFFJpgUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj4Hr0w5kLXqaenG-JMzGE5P5KwnB_AWxofvIeRrn_5aDZa4ZXqgHYCk5GNnmDkHsYQoeP2uWaWcsQWOVDwAmOwvDLS6_GCs08Fd3z4RWd3sbXSjiAn182OL5_2KhPrdfKuAAEyq4HYej5AX34cK9pZA_Xzwqf5s0OiKgzpf-8tBprHyTIUAVu9fp7LCaAocNlTvwTwTxlvbwEanhjNe-2rUpFwsf-F6jzTgaJio0yacnt7KK_j3kAPiT7ueB2HHbF0K4mB3Yzi87mMkyGr06R_kEtURt9lgIzCPLR2DYWMivFMyIsSN2JvD9Gup1eMZMEY3xHIFy8C1atstTesWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrKIktHTyws60OL4D06RArirZ-kvbLQyqQGVfO-k0IG2nGiwv-Sv4lds8bRv1NY9TyGmxWbgulMGxBJp1B6Ewoju0vsnu52cM5pgVOUktalnXubmqWB7oQumJG2t-cbSH-yMlKhvpvPj-F-Jeje72aw4qi43816TOUgTra-WiFhNEKRoCQVyOY6DRj7WGSEOpJnMLPYktinfvoWcGRx0p9PMbPyGXYQEdkL1_HphTEMvJlXD3NJf5eMYTtsjd9RjcuPbW_HnJ-xZaruUwKfzvqDeQosxsw5Rw1KrmVWZakSw49bf9EEOueYM_aTZQHgmlD2WFYhZ875F_uEq7jRilg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=sWS-t5JNfYI9k6VkIiXGzjqG9OPNIbd72Fc8igD-iBKSCYIf11LhM8X3Us_f-tVHrinRo_qNnAodAc941Ji5Lk_Ff2UPyckcw5ydejDMtmOEF6zPn2N4zJQfQDrGDoY33KZQ8dlM9kvLwzFBGiaKfuonLKZ4VYnnkH6OXzAbb8T-Yu-f87UlgwQOdkQKrH_e7sCQnxRw7yjp9iH7g_NXMUPwvaA-5l10oq4jRfDrKlN8f60P93qII-eS0Nt68qIo3BZrgnUGuRV4wqHlJ2l8kW4Sqxd70o61V7XPQdcgRE2aDhRcUHEwDZ-VBPHuda9Otl4egOvKdl7rM-wWD-R5zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=sWS-t5JNfYI9k6VkIiXGzjqG9OPNIbd72Fc8igD-iBKSCYIf11LhM8X3Us_f-tVHrinRo_qNnAodAc941Ji5Lk_Ff2UPyckcw5ydejDMtmOEF6zPn2N4zJQfQDrGDoY33KZQ8dlM9kvLwzFBGiaKfuonLKZ4VYnnkH6OXzAbb8T-Yu-f87UlgwQOdkQKrH_e7sCQnxRw7yjp9iH7g_NXMUPwvaA-5l10oq4jRfDrKlN8f60P93qII-eS0Nt68qIo3BZrgnUGuRV4wqHlJ2l8kW4Sqxd70o61V7XPQdcgRE2aDhRcUHEwDZ-VBPHuda9Otl4egOvKdl7rM-wWD-R5zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Oi8W6r5DPLVAMzt3cyvqBMQOEyyANe3WNa-tbFmei3vBLhFep5y7Cydu58eR4QNW0_YZwjHobsET0_-QTzr5V56dJrGq9AlgB4sYv5FJIXqwHJA_MVorVYk4wQ63TzwoLAQEcovaisMW8GLgX6-430oN-vxABagHJchTsh1xyAbujKviFP4xR679NCxPv7ldUzFUK1eKr5pvxq_Drs10Vmymvj-BeGIOerV44WjlEBXkQPfHk1udvg0e34rn3UhBvLnMUM-HotJhu8kHB5KCFxFm5bwsRIJKTFZgDUj8XGH4FP_0h9O3N11LaE8CzEGweGKYM-0sTo0049re824X4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Oi8W6r5DPLVAMzt3cyvqBMQOEyyANe3WNa-tbFmei3vBLhFep5y7Cydu58eR4QNW0_YZwjHobsET0_-QTzr5V56dJrGq9AlgB4sYv5FJIXqwHJA_MVorVYk4wQ63TzwoLAQEcovaisMW8GLgX6-430oN-vxABagHJchTsh1xyAbujKviFP4xR679NCxPv7ldUzFUK1eKr5pvxq_Drs10Vmymvj-BeGIOerV44WjlEBXkQPfHk1udvg0e34rn3UhBvLnMUM-HotJhu8kHB5KCFxFm5bwsRIJKTFZgDUj8XGH4FP_0h9O3N11LaE8CzEGweGKYM-0sTo0049re824X4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTVMfcP20XtgqGHxn8wmrjkWjZnUM6lC_Jsi342fq69rauOgz584qUY7KzIyOb1Ce7yX3Ychj6mCwiprU-itDT4oIsvAh1sTAyb1Z65ouNFsgB6qcq2LV2roQuFe0bXy4cr0VUN5-ycbkE0HFRdapE27yO-f-Y04aoQ2w-yIpJjadOZajJaU2eg4FDwFB7-RElBCX5jm0GZ1IKECEiSbvhjSXrS29VUJiqjodI7v92jkFpIP6aJymxUdStZMklc4hwrkCkrbH-t2N693xYUsZ4RdyumDRh8NtSoKB6S-pLIDQxZn5e1-sF1cVc-MwUfvD-b_3pJkcsQtVNp-LPLhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=swqJFUGx4-BlCmuVPUJtHbVSIg6CuYi8uzuVnDWWmiWv-Ve1w-VcEoHSy8ZHahgtaZsQh8GjwnX98Qz5gFYmKvT2Zq3MVHXdfwKi8O3I4MHxwiMxWxKSEX58UZaeiwggL_QXtKfpwNjeU1FDUTgE5ClejeV2VKPt8U9rNsCF-SQPgGkeIObpiatKnr5HiwozWl1xwZ5eop_DMX5BeIhn5-bYgMBK83Xq3aC-C_Yn95OS6p416n_O3DvLhE5nT2BiqCXtwsLAU0NG1ojx40XC3al5qqB8EYa8Ur6CKykWVMMPynrgRFcx2Ks-fkdRRJyyQ7Fsb7CX5yBvi6FwSgxigagRwcAuZei-F8iPrLsQ4M_LAHjqtv1TMcrsaj3SXyJsd5iclxsG7eod7h-hYX6enbMoqXM-c3rP6OHuuq2Roq4ObM9VXpDYE_42RVQ0gzfccptvYUh3uKP56XdRnZ2eEsxe3ZBEiLY0ShToe6FzOd9PJOIq27oABZLUQYmFlhVfik2eLZuhFhMBCV_42_hTcSut1uSf01AabqdSNbON-Dojmuxuglt-ueKnzJOZMyMiAJQ4Fe6Z8BG5l-8LsqVuX90sirOuNyTUiUx6kZtDKaTSxdeMSGrYN5AguqbyBrsemfJwL-iv8QauUTMHha1E8UQeqU8eKYuq2j-5yObhSxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=swqJFUGx4-BlCmuVPUJtHbVSIg6CuYi8uzuVnDWWmiWv-Ve1w-VcEoHSy8ZHahgtaZsQh8GjwnX98Qz5gFYmKvT2Zq3MVHXdfwKi8O3I4MHxwiMxWxKSEX58UZaeiwggL_QXtKfpwNjeU1FDUTgE5ClejeV2VKPt8U9rNsCF-SQPgGkeIObpiatKnr5HiwozWl1xwZ5eop_DMX5BeIhn5-bYgMBK83Xq3aC-C_Yn95OS6p416n_O3DvLhE5nT2BiqCXtwsLAU0NG1ojx40XC3al5qqB8EYa8Ur6CKykWVMMPynrgRFcx2Ks-fkdRRJyyQ7Fsb7CX5yBvi6FwSgxigagRwcAuZei-F8iPrLsQ4M_LAHjqtv1TMcrsaj3SXyJsd5iclxsG7eod7h-hYX6enbMoqXM-c3rP6OHuuq2Roq4ObM9VXpDYE_42RVQ0gzfccptvYUh3uKP56XdRnZ2eEsxe3ZBEiLY0ShToe6FzOd9PJOIq27oABZLUQYmFlhVfik2eLZuhFhMBCV_42_hTcSut1uSf01AabqdSNbON-Dojmuxuglt-ueKnzJOZMyMiAJQ4Fe6Z8BG5l-8LsqVuX90sirOuNyTUiUx6kZtDKaTSxdeMSGrYN5AguqbyBrsemfJwL-iv8QauUTMHha1E8UQeqU8eKYuq2j-5yObhSxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=HwPz_KO7vsXqihbOjpvYL2ezLKdFKe27lGzG90TRKZOEONODR6pmOsbkXn33k2GyDcpR6mqIYTz4bKV4zt1brMMjHD8m4Mj4UXp1hBUxw_waRV9af6TpMhNroGtOjfQ2B74ktNELTJhkHyeMXIpi1k5UG9krTXyG-1hRWtWKPDOi2WHCLI654auZI6NW77JswrXp60_JyEyLPqUiEDl2k8kkbChI11xhCkABlb1FXUWA8O5TRTp3ZNYE_Cph2u6k1MAlfGqNh4f8CpC6kp-9luLJJ-g6UTHshYuQSKXDDNdz8XFdrKcrn5kDUZIlOeQbOFEtykTRWiFOdkWVlKk1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=HwPz_KO7vsXqihbOjpvYL2ezLKdFKe27lGzG90TRKZOEONODR6pmOsbkXn33k2GyDcpR6mqIYTz4bKV4zt1brMMjHD8m4Mj4UXp1hBUxw_waRV9af6TpMhNroGtOjfQ2B74ktNELTJhkHyeMXIpi1k5UG9krTXyG-1hRWtWKPDOi2WHCLI654auZI6NW77JswrXp60_JyEyLPqUiEDl2k8kkbChI11xhCkABlb1FXUWA8O5TRTp3ZNYE_Cph2u6k1MAlfGqNh4f8CpC6kp-9luLJJ-g6UTHshYuQSKXDDNdz8XFdrKcrn5kDUZIlOeQbOFEtykTRWiFOdkWVlKk1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNAIcKFpPGHEHJpONjNvM9jiKKzd72bn_6uywi6iDCDq9oS_yNJGrzUZ49_DaX6I4_sXFzyjNCONbrTUs4Ysqz7QRTfX285U-HifHRJSSXWkAq36NiA4HT-D-mX_5Lp_5GMVxHpe_DpEuEN_p0cIa3IpD64P-la0_d6xMNSZQxJN1T7oTSnNlAFxqpzETXCr1vWBRpyGEDpIoj4plOhvC9fYEwPILMBOAa7DTxPzr_2rGFlIx3oZXBkOAXnn0fOmGpYZCJibmOsuJcosmWc1kqTSjAxqn1E_TMEzsYPV8SYNpCvmSzpyZ3Kf9QJ0etfPH1L2VV-mp4RpH9lewrnVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=HjuRT0lFi_IVa0Rmi1i0UrGjnzuhuugk3_usj0pfnW3qtczg0PX5XhOLLqlqatK1svQ_XA28cMkpjhfGrYlZd4dqQ4O8M1r9vGLQtXJtbjw4lTlGLRkutJ73UWo5HrLDOetIVpl1wBXo-y2fx7vAv6yQbiKyQD_Z18YsyRWWubfirYx0fPfAU1MqCThCdc94jz1UAph2_9zl5hkDgelSmDKvxrOk7Xx4P9bEdaNaiNaPFkZg3VKF-2Hx-AGwf5Ou5S4u1fe03lVoAOn000206NIQir2a23SVOenuWSnkICUZpdG0zLgvxFSNNMKxRhGU8IWcnfO222wqaYO5SXzCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=HjuRT0lFi_IVa0Rmi1i0UrGjnzuhuugk3_usj0pfnW3qtczg0PX5XhOLLqlqatK1svQ_XA28cMkpjhfGrYlZd4dqQ4O8M1r9vGLQtXJtbjw4lTlGLRkutJ73UWo5HrLDOetIVpl1wBXo-y2fx7vAv6yQbiKyQD_Z18YsyRWWubfirYx0fPfAU1MqCThCdc94jz1UAph2_9zl5hkDgelSmDKvxrOk7Xx4P9bEdaNaiNaPFkZg3VKF-2Hx-AGwf5Ou5S4u1fe03lVoAOn000206NIQir2a23SVOenuWSnkICUZpdG0zLgvxFSNNMKxRhGU8IWcnfO222wqaYO5SXzCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Twcf7T3RRCWunnoRcUz4KPEu8UEtItR9ME4E6Axw6--9f59nIfNPiVb1LmH3l7fdsnxEIJOVzfuK4M5W24b_e-L0mxWnIk2aJ3vvErGxtTBev1xjDUBgDag17inIyAeUN-fVC1fzj8nB6HY3Meib1Wlji5FmXKRp-Fnd-LuZRBnWrHJ9JHz8YK-032Ey3iGddIu42ZkWYyQcH8Tu6Eahh6NjDo2LS_s40D4amc_SnNRt0v5E7k9vxjXt6ec3yLa6GfKCbYslfMDIM4N64QIfT3iBPCxw1W6EtyHEjsWDUfu76aFZjJkQ7nEuTiDS4y24A09BSJ9oXpKSeoen2GcQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmgpvCVdrlgAYPl9g1NXtup0E0gsIN-w69b6DyaYZAP65wdD5F0r3VLdpHv5dljGSIJD-IxKh8ZI-S4eCzXOmKw_dq96R3GlX2kJCb1GPPLl9n7sv-WngkVw7G8D5PfroPsM6Qw7KWoSJ4HUhIqfoKGGwbuivmwsQcRfbaS5RJYssdQVj2aqp4-yXGye0CUX65wvK86n1GpJ5uLw7n1dCV08VRFYKoI4Hka162kkobBVTcIpCxXmAN2316E0EFnNBU82uiPDYk5GArswj1dp4y1AWK3jU3h6pLcswUUS7trfO0tJm1Gq9rX24p0hJA7BKjwFxqmTQINxza0W5d8dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Xq_lVZKMQm_NVTSFI6LRe_tepkTvSm1zjhYnpen-bm54MN_ALMkY4MK845NjYx71E1Qi6UTyLwj32A3cyntaeRA1wh6F2k-eqpqVcsDiZkiVOJCYbEd3Ou91Uyiy2kD58iitZXTXCK0bZ3RABxC6jHhPuZAPj_DyHb_S81C25XPY52oPRo67m2ce3yrL-xvkoGjGqVRhbYfn8enTaN-WQel6ON2jTIDVR8v6QeSJmOedwSg3odXL1CC9CX7-VzNip6UwRyoneiqinf5_D3YEZYusid7I1EHO8B_nJqCagCwq9uODe8MTWmDkMKgtEVPZa0iapnpJ9VHXIEiVY-YMVCjlidE5hFvOURKqfUsVlsa0SqwJgbcQ5l2tme80B6ncr-4bzPqsc69MAcELVg-eYLXKLv4xTIVOjgjXpJfo9LE6ZlOsuMbfyMU26NEoIVPc43RBDw3eTcPAF9Ey4rnCC6Be9lcI3VT6j93Bxs4a5lf2_aV9jvl8f8sUnXd_UbxDRaSWVUZJ_hP3bCD-lU_dIa_S3fDr71V_zEK9o4Y6jWzIvpjiYWdf4cX6fgTtqu7rhew-wISX6V4qNfDJ8rYLFUdxFEyYfwNsFVAlK_lmMtaFfm9UnnUbpSpHs8FHiChFWlejGKT1ExUXaJinmhSWn7Dobie-ZGRxHJLrtT9q3q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Xq_lVZKMQm_NVTSFI6LRe_tepkTvSm1zjhYnpen-bm54MN_ALMkY4MK845NjYx71E1Qi6UTyLwj32A3cyntaeRA1wh6F2k-eqpqVcsDiZkiVOJCYbEd3Ou91Uyiy2kD58iitZXTXCK0bZ3RABxC6jHhPuZAPj_DyHb_S81C25XPY52oPRo67m2ce3yrL-xvkoGjGqVRhbYfn8enTaN-WQel6ON2jTIDVR8v6QeSJmOedwSg3odXL1CC9CX7-VzNip6UwRyoneiqinf5_D3YEZYusid7I1EHO8B_nJqCagCwq9uODe8MTWmDkMKgtEVPZa0iapnpJ9VHXIEiVY-YMVCjlidE5hFvOURKqfUsVlsa0SqwJgbcQ5l2tme80B6ncr-4bzPqsc69MAcELVg-eYLXKLv4xTIVOjgjXpJfo9LE6ZlOsuMbfyMU26NEoIVPc43RBDw3eTcPAF9Ey4rnCC6Be9lcI3VT6j93Bxs4a5lf2_aV9jvl8f8sUnXd_UbxDRaSWVUZJ_hP3bCD-lU_dIa_S3fDr71V_zEK9o4Y6jWzIvpjiYWdf4cX6fgTtqu7rhew-wISX6V4qNfDJ8rYLFUdxFEyYfwNsFVAlK_lmMtaFfm9UnnUbpSpHs8FHiChFWlejGKT1ExUXaJinmhSWn7Dobie-ZGRxHJLrtT9q3q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtsUdg9Iz541i6FpyyBdZDQ1DfLmLOGIXPLzawnsQU7hNRc-0W6mVgGqS02H3XKPC1PH3V-aUHtVTmAqs0Nad4vjDfpephshjR_znugkpuR1oo9JSZ094m8SXXot87oUMyudK5SpnplyRsXl1qTYimrMA8UOJXDs5tm5X2EgYJ7W_0l8y8ULXfFElWF0QqD2wpkFM-bdAX-Md_laYdUh-Ysb0qXTtdUJ79ysgzvKJNcl6h5sA1sR1YHJ5dEkuWSA6Epztr8k9BsbGxgh7gpClQeZdELLQXGw0BlSC1Yc8SodZayWl2aTOCfhvWQd1HI73RNcgCDQf9RzmqmdwXQ9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuW8eI0uyJuhOXgk5vL_bhwz5FCh34UvZK6n1Y3eBcTeWB9fGAIdiHi8nViJOQ8iWQG9K17J3mmoc0qPGUu20D-TApEDxDfK0qCtazDNAXtZVIUbBjCuQGT1u8FJ2jJrNBIBDZjEOkgUHOoPJaZrGtezJ32PhpZL7icMRy10cDCnorK2R-RcWuU-fkj8qZGpY2IJ_Nh102Qp1JEZm6wma66yrmT9tM0mjXApQ6hpVrbe8XAGu9VXnP2oTPzhQwOd3oe6aqs3fByUY6NZe-yHkRRiUFh79F2-29_aGxoGxWbZExqz468si19mFvUsmAY8XHGviSitCmsjtilO4H2lxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=NzY9vQ3HGFQ-K8WC7MxpfZLP8WCC7SpYrfv_FJIYwGKfzoSv_G4WgxiG46mNnTrILFKA8PTD86LHer6dUYpvnuwSjJPmAV1OeT3wzQx3nfd9IrxZbFcLV_ekgNQi-IcOB2CdTj-WwRc7HaEhWY4F40XdgMj7sYwlOSLPXux3Bis6SXJnDWWS_XjxMe6nkEzYXLeFvfYHoUQ_KtcxkFl_pBZcAE9BAE_VSSe_toMiaqja1oTnvLtsPt9Owibh9K9bMfkYv65ex8BSLwmaJoiMTL7CtsqYFbFfmTmUa6TOW4ySS7Mz3ffQ1sMEBCdCxenzaR9XT0pFueivSvHkzk0p5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=NzY9vQ3HGFQ-K8WC7MxpfZLP8WCC7SpYrfv_FJIYwGKfzoSv_G4WgxiG46mNnTrILFKA8PTD86LHer6dUYpvnuwSjJPmAV1OeT3wzQx3nfd9IrxZbFcLV_ekgNQi-IcOB2CdTj-WwRc7HaEhWY4F40XdgMj7sYwlOSLPXux3Bis6SXJnDWWS_XjxMe6nkEzYXLeFvfYHoUQ_KtcxkFl_pBZcAE9BAE_VSSe_toMiaqja1oTnvLtsPt9Owibh9K9bMfkYv65ex8BSLwmaJoiMTL7CtsqYFbFfmTmUa6TOW4ySS7Mz3ffQ1sMEBCdCxenzaR9XT0pFueivSvHkzk0p5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=YSeOQL7xXgh6yShu-QcJaxT-Ug5QecEH2LHJ5N1KGzrKit73BskyTSi80tpHs2Dqz6z3OGp6l_4yO5cg6jfxEAR74Khkt52GtjbGIrdGlfsBeVXPzRyg75ZKFv3NEwVucBgwJz8MNckj9U7GkGzMStKklSZxg8UxKGj6q2rHSQDERNEGVJasLP0-d0wCxphnngCg9w-1vf1RMCCtHjeqeWz562OoCZ-3T48Yk9i3UoXzCZ8_e_9rnU3to-sI2xOimnBXEqjhslo1Md4Vwrqqh7Bobxx9lxED17tHQlgGs8Vxx05PI2CeeSZ_7NIp-T5Qdj7jwM1c31Vz1gemddeIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=YSeOQL7xXgh6yShu-QcJaxT-Ug5QecEH2LHJ5N1KGzrKit73BskyTSi80tpHs2Dqz6z3OGp6l_4yO5cg6jfxEAR74Khkt52GtjbGIrdGlfsBeVXPzRyg75ZKFv3NEwVucBgwJz8MNckj9U7GkGzMStKklSZxg8UxKGj6q2rHSQDERNEGVJasLP0-d0wCxphnngCg9w-1vf1RMCCtHjeqeWz562OoCZ-3T48Yk9i3UoXzCZ8_e_9rnU3to-sI2xOimnBXEqjhslo1Md4Vwrqqh7Bobxx9lxED17tHQlgGs8Vxx05PI2CeeSZ_7NIp-T5Qdj7jwM1c31Vz1gemddeIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bXnWyUsxOYcmZORkbVeNavtkFi9uLBrK5DhGTGRHz1KDgk6jpvGWsXcBbVy1ciY-QAm7rOU0TFKIw84CSIsb1870OA0mnSYkdTw1mKtGTTS7qc8cS5S6kbS_XCzf76R7lqawyaxLbRWRb3ycRWp_tQzUV28wa3tGqz1S15BLAS5o_bGVZozd64QAqRZIHihD1wdZlxuyEhjCoB9_gpKePll08cuRTprSXcJFiFzFOk-3bS6Y_qUQj75kfHB5JlavnktwzEj61aooLUfbAy4Fd8KxUsOTCRsV9XqNoDKTDqTLEtcGMaAqsJr5rbadpHY47NGINSFhP0ITZnjQnuPOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bXnWyUsxOYcmZORkbVeNavtkFi9uLBrK5DhGTGRHz1KDgk6jpvGWsXcBbVy1ciY-QAm7rOU0TFKIw84CSIsb1870OA0mnSYkdTw1mKtGTTS7qc8cS5S6kbS_XCzf76R7lqawyaxLbRWRb3ycRWp_tQzUV28wa3tGqz1S15BLAS5o_bGVZozd64QAqRZIHihD1wdZlxuyEhjCoB9_gpKePll08cuRTprSXcJFiFzFOk-3bS6Y_qUQj75kfHB5JlavnktwzEj61aooLUfbAy4Fd8KxUsOTCRsV9XqNoDKTDqTLEtcGMaAqsJr5rbadpHY47NGINSFhP0ITZnjQnuPOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWRt-FV9N0Svlps_5HLizdjB3VuLMGAeBRZfR3_8xUQseXlnNpkMOK7LulOHhd-lg5OVZXrYfiBUOVoQGbzeRpPAOJs7J6V4v_Ai_Q0Q582hMTmLmpU6DZxLC5vHC5tjjfao8JmPhIFm-UqVb4k_Zx0uv6gPAuJt951Y43bDYWzcgbnYiD0m4alYdEGpK_TynPsdfX6pM6-rkbX_IrmrZZ0L5PZglKW67sTWj44lCnLtGCDh2zuLEh9qN5VXDvnrSUc__c6rL5YiRQwSWXGSigckUbshV_kX0pTTNW_2Qp0tXob581jDthTTHk4fIwn_reLVaA2zYEOh0jJ5VuZkZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8CvOkR_rpAhOu_TVSL1KEKze-kGrNU_iA70GIa-ulTV_sHHbsQBj06-SVAqiR7D4CAYU_NTY9v9zmNpFrQiouYXiJ3UIV5jmSQ97-APZprJyS5RxcBoKwaEcgFPwIiCybIbP6ULC8NwbrZnGNzZVqfleXIcGw29S3BEJnXnTXPJH3VLp9TBqgbECIVrktGuvUCPuYOSjZu7npRSrzy-QDMPOVHmAF-4dzIAtFZpXpMJKsqgl8uBdImEB_-aM1pgkEA1NSyr5MTwNI87o-qnw02e4hFImlORwN3dlJEU_KXjTWbVFlK5GJWoeFrZlbj4urL7Z9xeP7TOgwkDh5zREavE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8CvOkR_rpAhOu_TVSL1KEKze-kGrNU_iA70GIa-ulTV_sHHbsQBj06-SVAqiR7D4CAYU_NTY9v9zmNpFrQiouYXiJ3UIV5jmSQ97-APZprJyS5RxcBoKwaEcgFPwIiCybIbP6ULC8NwbrZnGNzZVqfleXIcGw29S3BEJnXnTXPJH3VLp9TBqgbECIVrktGuvUCPuYOSjZu7npRSrzy-QDMPOVHmAF-4dzIAtFZpXpMJKsqgl8uBdImEB_-aM1pgkEA1NSyr5MTwNI87o-qnw02e4hFImlORwN3dlJEU_KXjTWbVFlK5GJWoeFrZlbj4urL7Z9xeP7TOgwkDh5zREavE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ER1wql5uTbrJKVuAZjKH2mwMg8zdqsoSWBJ0aJd6aJSvFqG2JVf9fjdKetiLJ7ihUcQBRhvWcMl3z3hKoNxCiPerY0TqL5lcCN8WjPb_62edBZ8j9_THOg_0qHn7wpB0bFA6iJDxvrLbYH03pM6Awjpm8X6DUIBVOrF7u5dz8ftCD2D3B3xXdkSCzkAItvVisT1wKlDHOuOfRR37_hLNSzGsAwCKPmBLoPl0lPFOrvwaSAi6YAXpdLhUCnkFj92MtI2mLXgUJ8Pyxy4IjaJ5XQ48GYjD6HGPLakvEb9cK8pcFSQ_kDTCCEyEvcaL_PS4TcNKA25DkCiopiowpdzZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ER1wql5uTbrJKVuAZjKH2mwMg8zdqsoSWBJ0aJd6aJSvFqG2JVf9fjdKetiLJ7ihUcQBRhvWcMl3z3hKoNxCiPerY0TqL5lcCN8WjPb_62edBZ8j9_THOg_0qHn7wpB0bFA6iJDxvrLbYH03pM6Awjpm8X6DUIBVOrF7u5dz8ftCD2D3B3xXdkSCzkAItvVisT1wKlDHOuOfRR37_hLNSzGsAwCKPmBLoPl0lPFOrvwaSAi6YAXpdLhUCnkFj92MtI2mLXgUJ8Pyxy4IjaJ5XQ48GYjD6HGPLakvEb9cK8pcFSQ_kDTCCEyEvcaL_PS4TcNKA25DkCiopiowpdzZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vryxmXP3cqyXr7mKlRdB49NArUziKiuPtnEgvK4_7Stq0TfOHhOPSmVwP2-Z8OIpbcGxs-PPz-VyFQoMKo5H8RGVx-dImWEHqhmlUwqDZm16nL_iF8JcZ8WnnI8tnxqun5oiAoQfZWvvGGYO0R-gWbcb-7aCZx_iMxxSdLBlu-6OQyNv-85GdWQwVteMXqyKKeYDgH0HStSbEhBUI7z3VLWsE1YmAb_zAbxy58LXDvu8H2pXYNFKW0QU_N8TYWbMaXogxbuz_DWsYpQ9glxdRxSVDo92tbr10TD05xjAEC47GxcZyO9YPulD4Ac_eDu0VZtnj-OgZIVnrlbpoZIA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Z6gb-2xU5UpjYbzB9oEB5Skk4US_LgdDNjy7c3Wg8l9NsTIIxXiVnk-M8NQcMMlGTTUuiwcEbeTe2nl2ldQneCJ0lg6_Fs2hDl0HVIHqtIfF95IDUV_ms63097Y6vsMqVDSv1YVqdIjbbQs_SOx3UDXsQsUTNwRF2Cur4zskwLVlG5lWCb10pDf3M7D-UTLuP3QCnM1YuG4LEKcUcDJCSkubGp1Kde2FNC6cvifY_v6xxTFwq54WY4tQItNddgSS5m-wAvA6CPnNHOY-PGFr2ukBZwdupDP6w5CVVFeWppcUek5erTDjV4dGRmESenZ0NbYT2x5vMTrAm8cBX8l7nln6eaz8Ks7Pp8V7qB0MEQB4T-6Pn7hIIg7WGqantCUhii04gHtZ5Rc-z73I86SFWjab9dvfr-LQyWgCw888GiIQsn-sPQ7QatsqAVyznEYrZrP4bZw2ySu-a8IqMzvo5_ZVKSg0b4OxcY75X8TW_u5qlO_mfKwSym4ylJojWmiM53fH1c5aJz5dgVgv1cTVOQHGxggUEEhTW17-TOoChy5jLiPhnSpUyQGbupQ_AX1lNiyYyfdj-iAolESzWbFYUSgL8SgbU2gXlVXsmjmAUoroFFaLt8kow1kEp_GSDi3eVmxMQw3HZpmoiT_QMJyAIciKAAweuv_R_KddMBSMrXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Z6gb-2xU5UpjYbzB9oEB5Skk4US_LgdDNjy7c3Wg8l9NsTIIxXiVnk-M8NQcMMlGTTUuiwcEbeTe2nl2ldQneCJ0lg6_Fs2hDl0HVIHqtIfF95IDUV_ms63097Y6vsMqVDSv1YVqdIjbbQs_SOx3UDXsQsUTNwRF2Cur4zskwLVlG5lWCb10pDf3M7D-UTLuP3QCnM1YuG4LEKcUcDJCSkubGp1Kde2FNC6cvifY_v6xxTFwq54WY4tQItNddgSS5m-wAvA6CPnNHOY-PGFr2ukBZwdupDP6w5CVVFeWppcUek5erTDjV4dGRmESenZ0NbYT2x5vMTrAm8cBX8l7nln6eaz8Ks7Pp8V7qB0MEQB4T-6Pn7hIIg7WGqantCUhii04gHtZ5Rc-z73I86SFWjab9dvfr-LQyWgCw888GiIQsn-sPQ7QatsqAVyznEYrZrP4bZw2ySu-a8IqMzvo5_ZVKSg0b4OxcY75X8TW_u5qlO_mfKwSym4ylJojWmiM53fH1c5aJz5dgVgv1cTVOQHGxggUEEhTW17-TOoChy5jLiPhnSpUyQGbupQ_AX1lNiyYyfdj-iAolESzWbFYUSgL8SgbU2gXlVXsmjmAUoroFFaLt8kow1kEp_GSDi3eVmxMQw3HZpmoiT_QMJyAIciKAAweuv_R_KddMBSMrXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_pyC7kPNC3BTdzCbhk_VhwcpAwATXMps89LyBqIFSijWexWiwSSJOnT6_MXGkZlHW01t7kXlLdJ1Uu_u9b0FKEG-MAC0o8z13gOqPJSe3H1Y1Yqx3HjvD7Du8siC281p7lz-jvp9wUtxnMR-2MIUvtTPF4X0ND14wvQubCfBxE6MDcpnqqN0UnZvmq_KCITTs-H-yyMlesN1YVb2s7XvQdwsWcG-ZnuHYpYOWFb2RfMp7WZI1ynLKtTObr0Ru_9pFc2zk8dB5KdB0n2PeIJSkeqsxbKyMlKAz5uESFnwgvRLO-RZ-KMQrEHommhPMfjB-2p88iBBr7nlMuCPfDd-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JHBmpcc4cFmsyvFKnkHS2MEmtTkwU_X9pDVWRzdma6C_Gb6LkQuCOO1Yp8CN3xrsg3zOx3r3rJOxf5YQ1fEJsugCj1UbCfssfwqK8amwauSZabcWmo6cf1FlMCKfQQbbEFBrV-PVDPKvYz9WLjepr8948MezbjCyFlRWTVj7mduFX7tS6kRz6Sg_KoEk3Qx_EOyPKbnBJwikJ_LkZjJMcb274YnUQ_hg05lzOVWnpnBynWNH8EfMchs7QcXqPnu6h9tu84-pNGkoMhxTOG_PrZYmDuZyvb5WN_lns_iCkUQysT5o_7PNclDKz5CpCDOHgbS_ffUgb_0ZxjPoCU0c_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JHBmpcc4cFmsyvFKnkHS2MEmtTkwU_X9pDVWRzdma6C_Gb6LkQuCOO1Yp8CN3xrsg3zOx3r3rJOxf5YQ1fEJsugCj1UbCfssfwqK8amwauSZabcWmo6cf1FlMCKfQQbbEFBrV-PVDPKvYz9WLjepr8948MezbjCyFlRWTVj7mduFX7tS6kRz6Sg_KoEk3Qx_EOyPKbnBJwikJ_LkZjJMcb274YnUQ_hg05lzOVWnpnBynWNH8EfMchs7QcXqPnu6h9tu84-pNGkoMhxTOG_PrZYmDuZyvb5WN_lns_iCkUQysT5o_7PNclDKz5CpCDOHgbS_ffUgb_0ZxjPoCU0c_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMXeiyXsDmgmICocKoEF8MKC7A5xXx3kUD_PSVXGmjtuTRCiky4IaUPCrgh0UaZYfxXotXHw3IuL20ph0IbftHpvq8eTzI1PZmSb0o42ICdGVak8ZfXMyfAlQ6xJAbc6B3Gx_EqjWVKIYzQF79xbMqsWGQQlj28ZaYE6xUe6nBF5EGsle9pA70hpucpHbQ-arwcRxzw20oxzCq5pRh07qufXKVUWCizK1_7ENWeJSsFzk4MIbM3M0QOmvehmKay4hC7B54fIVbn9Dq2hKmVPBabC7irWblAQ7rZuK4448lJhm_cn0fRAuauXCaRE9rBjr-PQprU3rpf0iiUH_EK6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwCEST7ryDQQxAb7IkQ7DTF0urKbuA8dm_DN4wS8GeZwaFs989pMb7AahKZ_PbAsJ7QppMhbN7KHSJ5Ab3L50QmbOW1glDabuCBfTy5nI3DrY7YrRKMm6Wy6Tdfd-zqlnddDcPPHFOEhS7PJNW5MtqGr1UPWeHIpsouzBlsyZWsR1zhvEFBeK51FDlaOpGm_zQ0oo14f5pOIRuDspCf7hLIj6cAo4aMixbNM3wxSItavoEyY-dSdJRq19CRlhqdXCP6inPCBVjWgHrHR0W-rl_qWcVHfcmSjKr6gvrykVeT1C2gkDmozthmqCLSL1tS1X4Oxl4aBH0YooeJ6oY7YdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXbr4vQAHhdCs3y3Ys0voB6Hj_U0fv16D5j5czVUN6uK2l4SWs-634yLxDGufYvlcbWZr2mAJzj9nQrvHL53GtXcNm5DRMwDidTaQ1OLdQpxfS4tahjq4iqkYcMAdpyOLm76yMq-d18wCCbByEixGPjtWnhdPoo5_RXlZDoNLUBgckCX6D-cza03gfSs9mBHqHUY2gM6CO9WavZcM3wH5WxeuXvx1md7Fj5myxcuAlFVWMVDWeb6wrj8ZmaIWre_BupklCRVk2DWiE98vh6dqRSyHBy0FDpUqiNYryYiMn17W0Z_XpYeRElOekej6jvU9GqlMAOZfcLl_007YiNbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=tFtr1oEtFtc5shaVw-9SmTgvqbX9IkAc0OnN_ciC6h-rkWwBtpMYwFnqg3azG3Rnh6XNLXxCCri7FV3Wq-L4_TFBy8k05_-YXJQyj9mHmrmj3wSkvxwXlAHrASKBiIru3MSoCUDHTzAw05XQeks1lBO-f5hlLt-6ZIvG0_nc55eaIbahmUG8e5xGBZSBSzSQILwD8ZbC6o8qucwOclGAkIr7WYXvsAowvN47ICVBvGO03ymXIRcIH3MRx17BlFdaqu2hfFmdB_TBpvD-1NJAo8bohYZCmnQfQ2qbJm06PRk-Fb8JnwgUVvCI727NRXvJWpQuF-3TB9wcDyO_JbmZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=tFtr1oEtFtc5shaVw-9SmTgvqbX9IkAc0OnN_ciC6h-rkWwBtpMYwFnqg3azG3Rnh6XNLXxCCri7FV3Wq-L4_TFBy8k05_-YXJQyj9mHmrmj3wSkvxwXlAHrASKBiIru3MSoCUDHTzAw05XQeks1lBO-f5hlLt-6ZIvG0_nc55eaIbahmUG8e5xGBZSBSzSQILwD8ZbC6o8qucwOclGAkIr7WYXvsAowvN47ICVBvGO03ymXIRcIH3MRx17BlFdaqu2hfFmdB_TBpvD-1NJAo8bohYZCmnQfQ2qbJm06PRk-Fb8JnwgUVvCI727NRXvJWpQuF-3TB9wcDyO_JbmZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlfpU8ulc71dK_XfI7l37RePJfrFnNpVgU25unrb_N5m6-Wab4mLuw9aV710zLguiCf0PdWvCWT83TUJ0pclniuFa3JANt0W7auL8a0VNInAUCZdZa3ayLLwrMRcDGpwpK49rX_C6Bb9rakZVMpozyduvJ1cqYfCFpMVpNcPFv7P7M4rZDYQylHCSBSMV_3-SBC2AsPNlB0k7-UufiKtN-NOPJSgUVDC_-GGayUKpr_wopD_nDTghTmCzKim5RdDz03xfbuGJFSAAGQPfupmBuMEV4LvGcVZ9BmeTCRW0U5th4rAvZFW1PgbGApoy9kUT5lVzp_E75MgA7z3GD2mVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1H6C3wzUYXTQ7UVElsYhERQiDYEHA03ZlUR_ixcSMEM1viYgKUFIDq4qTRsShBStmFe3Iv70NtE2GEIM6WMeipClTBhXm7vXI7mNB2E6loIxVz-Q46L--j5oSD2dWyu1Izi06uVZOfVElmTl18-Tx5IOPqFAoLd4mm11FQSoReCAIDrk8PnjxPiv6ZS3xBx6hNCZVFF2yFN8t9YIOEK3WOy4L552fw7ZE0jfiX-38EA4qs2QsvQvYiF8hpJYH1ZZPk6tUhIk8I3PioV60ub-pUFQwDgRI_AWKPSTFuhKLXrsrwSZK4VU1IJdZL3ac1BHE91-QvhSt9GkN-d5Ejrflw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1H6C3wzUYXTQ7UVElsYhERQiDYEHA03ZlUR_ixcSMEM1viYgKUFIDq4qTRsShBStmFe3Iv70NtE2GEIM6WMeipClTBhXm7vXI7mNB2E6loIxVz-Q46L--j5oSD2dWyu1Izi06uVZOfVElmTl18-Tx5IOPqFAoLd4mm11FQSoReCAIDrk8PnjxPiv6ZS3xBx6hNCZVFF2yFN8t9YIOEK3WOy4L552fw7ZE0jfiX-38EA4qs2QsvQvYiF8hpJYH1ZZPk6tUhIk8I3PioV60ub-pUFQwDgRI_AWKPSTFuhKLXrsrwSZK4VU1IJdZL3ac1BHE91-QvhSt9GkN-d5Ejrflw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=LxRvJUIoLjegcZoW1ocmWtvN_LhBc2SY0r0RsMtryGeTkegH_XtReNu9yfMQa1ZOGpzc7Cu2yBbBnuznSHX4G61aPzyyJkNA1VTWFvJEsOpb4y1f-anz8Itib462hxtcuYpLw-wucyHf4qsBRCiHtrdZ_rSGVW6dquvDSq7GEa-fApZloPbmPNa2xGQqpKfPCBeVzQCZd0uXwTh_M4mMv-Za2__RVyFsKZLC-AACbeKFm54M3O6w6EjVV_l9Zf9rVrqWix4KsXH2Su3_FJi8G8cTUiFaG6ANy0RpD-8uOeD4PA7-K-WxOQKBWKfu8n0Xq8MEYKHesuT8ny4Rwsl6tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=LxRvJUIoLjegcZoW1ocmWtvN_LhBc2SY0r0RsMtryGeTkegH_XtReNu9yfMQa1ZOGpzc7Cu2yBbBnuznSHX4G61aPzyyJkNA1VTWFvJEsOpb4y1f-anz8Itib462hxtcuYpLw-wucyHf4qsBRCiHtrdZ_rSGVW6dquvDSq7GEa-fApZloPbmPNa2xGQqpKfPCBeVzQCZd0uXwTh_M4mMv-Za2__RVyFsKZLC-AACbeKFm54M3O6w6EjVV_l9Zf9rVrqWix4KsXH2Su3_FJi8G8cTUiFaG6ANy0RpD-8uOeD4PA7-K-WxOQKBWKfu8n0Xq8MEYKHesuT8ny4Rwsl6tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=aHwbi-VH2IERLwAbl3ULsHdC2L3yPLurPWYx-HR0xhfnuUIJgPHLLpaB6BZ9QbBonHfb5aQ8YiILRGOEZdqMy9EumyNDKHkiRRUEo68tWiHVSHCA60d1nU5kVD8rO-9eAfQF3GLEh7EMlx5Ef7dqJkD9Oan5NTnVonZTUUon2v6bmjAXP3DYLYaQj3C5W1vGd3UoAgpo0PcIUfoUZiR0y-Djr7yZvvFaoqOoqYwHiD6x-YGvz4_q5K9u0FdsbvUTYLackiepBhh2AP4c4fSuzAjCQIcy47sc3riB9fQPdRQvQowirporerbCjFF-w_BpthbkA2eeHG9eYSDg7P6Nk0LrESnqaOUdlyieRVAF47tVZtybJxxRfVGoSFLXBAmq3fKiZknTBMjunh0Hfn2SmQs-SF-yzbWd72OY0mQI_Gm5mMLMfEcsGG-FDSrHOEKcG5CmQcLM1Hv-3D4xOk3GcTnYRfy2DBO5d1zB_Dm3BkAS_JIUJ8TrTOgr4genocEyLB4hEGoZqdd2rSqnVbqq_6onTYFEOqr0pk7mS4Kaonr8ICM2hnaqIZI_W81wX0Njl2GBxHIFoZS5cO2FIMuh0j4L7cazBQOAHtsWMZ86KUSuw3FeCTfHp5trkZPD6MVk_7nt9aVkxrmGP0qgMx_FxXrxfDDNZK-ERasPQhsHxUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=aHwbi-VH2IERLwAbl3ULsHdC2L3yPLurPWYx-HR0xhfnuUIJgPHLLpaB6BZ9QbBonHfb5aQ8YiILRGOEZdqMy9EumyNDKHkiRRUEo68tWiHVSHCA60d1nU5kVD8rO-9eAfQF3GLEh7EMlx5Ef7dqJkD9Oan5NTnVonZTUUon2v6bmjAXP3DYLYaQj3C5W1vGd3UoAgpo0PcIUfoUZiR0y-Djr7yZvvFaoqOoqYwHiD6x-YGvz4_q5K9u0FdsbvUTYLackiepBhh2AP4c4fSuzAjCQIcy47sc3riB9fQPdRQvQowirporerbCjFF-w_BpthbkA2eeHG9eYSDg7P6Nk0LrESnqaOUdlyieRVAF47tVZtybJxxRfVGoSFLXBAmq3fKiZknTBMjunh0Hfn2SmQs-SF-yzbWd72OY0mQI_Gm5mMLMfEcsGG-FDSrHOEKcG5CmQcLM1Hv-3D4xOk3GcTnYRfy2DBO5d1zB_Dm3BkAS_JIUJ8TrTOgr4genocEyLB4hEGoZqdd2rSqnVbqq_6onTYFEOqr0pk7mS4Kaonr8ICM2hnaqIZI_W81wX0Njl2GBxHIFoZS5cO2FIMuh0j4L7cazBQOAHtsWMZ86KUSuw3FeCTfHp5trkZPD6MVk_7nt9aVkxrmGP0qgMx_FxXrxfDDNZK-ERasPQhsHxUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=EEOFKjglcYhaGnXmhQMpibflBZl-EEGlO-1wFLW74KX-RUBVpSJXK4Rqh-f311UC7SYA3w6uf_o7DDYclsSnFHw6RGWLiIOGBtD_u6fDiIDwA669UZ8IXJy8umRS3VZEKb5qU8zicRGJTCEgR0XmBbG9Q32V0aTzYPJrCTkzz9h8rMam2baILFrUH4c-96tPXlrpJ7541RLdVDgnqLdVHXmPYqi2h5YSOZkcp2bjmsQRPIiOdBkoFTcbxNXHAFBz-iLCV7xBWNQlj93U_d5vCEDdDtQYHnUWfU4yU6aOQZ2sgQtQSxsouAwzJgrimSuEvmJvtb3evyjb7naCXsAEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=EEOFKjglcYhaGnXmhQMpibflBZl-EEGlO-1wFLW74KX-RUBVpSJXK4Rqh-f311UC7SYA3w6uf_o7DDYclsSnFHw6RGWLiIOGBtD_u6fDiIDwA669UZ8IXJy8umRS3VZEKb5qU8zicRGJTCEgR0XmBbG9Q32V0aTzYPJrCTkzz9h8rMam2baILFrUH4c-96tPXlrpJ7541RLdVDgnqLdVHXmPYqi2h5YSOZkcp2bjmsQRPIiOdBkoFTcbxNXHAFBz-iLCV7xBWNQlj93U_d5vCEDdDtQYHnUWfU4yU6aOQZ2sgQtQSxsouAwzJgrimSuEvmJvtb3evyjb7naCXsAEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiDPIa1_xteNGWJv0qr5Iec3bXgwI_tsLYxRNqNPU3YY95Q8wyg6j11vMPg6Qs8O6IHmEXHl1oB-xGOW6eR_1BI-y9JY511y5Pw2tjuthFqUIM3R5M6dC2vMaJ4fHdrdUOVz6wIgPXKp7K9AdCuKq2zGLDA2tp3spopESOyGVc9UVuWhPE9_C1mAnkFyimM8yMFXhoQZHhv0l1XRemhMNTKDzoPZH38Q2ZMYNtAnrdpCp_F9cGXjJ2qJtwkJfvTeMbv-41uX_4jsCpB0GNEEAKBYR0YeodtlxAf1fLeroWsdh48kBCOB5T47IMVCnnf9g2V62BD_9LzlIRbrMLBSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=O39FLlzmahV32Vx2h47AvK_rl8CsG2DYMz1WH1WzaSypiVzXk6dLaMNUVfxI_oKg0bG0XKVZfQAXjeo2T1DYYY4lHF4c0lxgznDI26CMUAXNeDt-oknq_Pg3HaWryOuSQN3VgAA68blqXSikZd7SROU1CikEgFjBk6d_G6roLU6XHyCjSblrdF0D5Bm713XLFPY2yaAvkRbySmenlaisWObnRXYUmWVx0cEw5EE95FLocRwB3agKYQK92hFkyL0BL2AZDQGscY9lrATYZWrJzCyffFMkEWlLXpOVZ0lj1Q0V6gTtfJj2N7gcGUpkT18i3qLq6DTFyI9qkIzbcJJYmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=O39FLlzmahV32Vx2h47AvK_rl8CsG2DYMz1WH1WzaSypiVzXk6dLaMNUVfxI_oKg0bG0XKVZfQAXjeo2T1DYYY4lHF4c0lxgznDI26CMUAXNeDt-oknq_Pg3HaWryOuSQN3VgAA68blqXSikZd7SROU1CikEgFjBk6d_G6roLU6XHyCjSblrdF0D5Bm713XLFPY2yaAvkRbySmenlaisWObnRXYUmWVx0cEw5EE95FLocRwB3agKYQK92hFkyL0BL2AZDQGscY9lrATYZWrJzCyffFMkEWlLXpOVZ0lj1Q0V6gTtfJj2N7gcGUpkT18i3qLq6DTFyI9qkIzbcJJYmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Ulq0Qt5vycSVTJUaQirgxDlWfyBU9UIKY4XtVvckz9iJM4jqK7Jq6gi_0KTotfGso-HFgM8As8Ipqu97aRMx9ymiAoF5wyCCFdVp5jD__M65EORtospUKan470Swy69iqt1EnE8uKhX9tQESZC9uJ0JPFgZEfq1KLfAYkdjKzcGMGXrDKVZwKVfScj5n7IGuKEqJkCvrwSa5bwVpgX-LgKQSEveCmXOHw8uwodnH-YSr0Bt9eSDf_SQasf0A4BVD1UDar-axeOfJqOSsFroaO1Nu8Z72wi55Nv0kfuP6fANHzg3a3rR8cwZLRkzV8nOtmclF3dOuItsO8jSq8m6qpB7s_FaXg2oJXl3DNG730k4yMnES5-hqtLxVUu-TQ7PS0hW5OjvB1uS5fW7X8pch5RZxC02OzhbNYppQdJUKRkR7-qJnYoOeSecFiSTalB3C99zRGuxO3iHN5B9K1EJ3TH-8WaIRCcBVHWqtAMMhgZIcHyaAhZaxpZf8qKmqMvNAhUTeu8Vbky26kqzeya8rQMaU3BLnPsNrGAA56Mw-pp4B9zbnXbUT9-O9dwa8e1s1LO2JPrlN8dfUZSyyxtbmERTwWsUazl_Uy1xxsFP_BMrHP4qGJ83zL-cXDpnb1SphM4xZ0tRtp61F_hW_bVJ2NJNTw2mfgyLIpcFi0nr63BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Ulq0Qt5vycSVTJUaQirgxDlWfyBU9UIKY4XtVvckz9iJM4jqK7Jq6gi_0KTotfGso-HFgM8As8Ipqu97aRMx9ymiAoF5wyCCFdVp5jD__M65EORtospUKan470Swy69iqt1EnE8uKhX9tQESZC9uJ0JPFgZEfq1KLfAYkdjKzcGMGXrDKVZwKVfScj5n7IGuKEqJkCvrwSa5bwVpgX-LgKQSEveCmXOHw8uwodnH-YSr0Bt9eSDf_SQasf0A4BVD1UDar-axeOfJqOSsFroaO1Nu8Z72wi55Nv0kfuP6fANHzg3a3rR8cwZLRkzV8nOtmclF3dOuItsO8jSq8m6qpB7s_FaXg2oJXl3DNG730k4yMnES5-hqtLxVUu-TQ7PS0hW5OjvB1uS5fW7X8pch5RZxC02OzhbNYppQdJUKRkR7-qJnYoOeSecFiSTalB3C99zRGuxO3iHN5B9K1EJ3TH-8WaIRCcBVHWqtAMMhgZIcHyaAhZaxpZf8qKmqMvNAhUTeu8Vbky26kqzeya8rQMaU3BLnPsNrGAA56Mw-pp4B9zbnXbUT9-O9dwa8e1s1LO2JPrlN8dfUZSyyxtbmERTwWsUazl_Uy1xxsFP_BMrHP4qGJ83zL-cXDpnb1SphM4xZ0tRtp61F_hW_bVJ2NJNTw2mfgyLIpcFi0nr63BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIcfiitY2kdkVZ_jvnlBSR5DvoiPGoyhwdfnLOL484_GcBm_5Eowp_9K0-Ok9zw4wyEaBNc-bo-8OCTQ3kjBghU0NQpJd00NPy2fn-nRWoRhbk-HC53A5l9vs0EJ7QnnCP7gNvexIrYF_7efu85hPzZWMtSBlx22quO_EcGs1c3fbIQOkzuqkopZEfCjLJLOJ6NKQm6ySZP1pBPClJsB-vh_xaNpOlrtTYm6m4ljNyG-r584uqjq59HRSThGZ0j8AnQ3TQYTZLvxrtVvPTzi3tbXze8jPdRWHk1tMjKyOADZvdi2v1zQoKEy4ftIb1xYKeXsT48ZDZnYgmUwUDHPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=AiwKi5_JA__HY_Yd5ClE6OInuOA4ZOR_2D1k6sKm-bFy__u7WXCqbYJry9JQ2phSnQ3Vs46DtD-SzRl_7apF4Mcp37nVCL52wJuYqsTq-_YMIfwAgHJWkOFvV0Y9sCzfwTOj8WKYYYphcE4wNEBnjEio57aN-KNkfo89gNfw0Dgbm6-iFKCmFOQa8haGCJJO5szQNCvpvWQTo4ChjrIHPYtvDWZD5MPwwY4chGWh6Kxs22tv9zZScU3OG_oe0wQjRsazc7Vld4obCpqKwdQP1m_IdivHkHVyleHFzLulZ6lpmduLvcD_HrBQAAgKassEeCNeEw9HHYMrPvKRVXcP4ktdJ-IorVJhOJiIkIxElg3K5WwjWyCrc8F3nZQeGA9HyFGa_qF0aqTqlaUBCS9L88yp-FoNG8Sb-aswxYbryaB3XRradcQ6BUPvuHyV8uYKQpvf7bk6th_8u8g1cyxNxuzMmgjtmtLZ9AVgEt-GiVbukqG0c-gxKQtTIgH2hPbPB-skMPycczNTUAxVuY6BoX1MxZLl9PV6bgP0xYXI6yUnawZptjJ4caDdV3ecWzvUNvxPaYu0kRrBi9hCUqDVbeBtg4vHHTSd7M9ekN-r7J_5IpDi0sI6VThe9kQVnalGkgnIZkjrNyPZdXIgJ-zegDk_mV6rv8YXU_-sVHWyMQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=AiwKi5_JA__HY_Yd5ClE6OInuOA4ZOR_2D1k6sKm-bFy__u7WXCqbYJry9JQ2phSnQ3Vs46DtD-SzRl_7apF4Mcp37nVCL52wJuYqsTq-_YMIfwAgHJWkOFvV0Y9sCzfwTOj8WKYYYphcE4wNEBnjEio57aN-KNkfo89gNfw0Dgbm6-iFKCmFOQa8haGCJJO5szQNCvpvWQTo4ChjrIHPYtvDWZD5MPwwY4chGWh6Kxs22tv9zZScU3OG_oe0wQjRsazc7Vld4obCpqKwdQP1m_IdivHkHVyleHFzLulZ6lpmduLvcD_HrBQAAgKassEeCNeEw9HHYMrPvKRVXcP4ktdJ-IorVJhOJiIkIxElg3K5WwjWyCrc8F3nZQeGA9HyFGa_qF0aqTqlaUBCS9L88yp-FoNG8Sb-aswxYbryaB3XRradcQ6BUPvuHyV8uYKQpvf7bk6th_8u8g1cyxNxuzMmgjtmtLZ9AVgEt-GiVbukqG0c-gxKQtTIgH2hPbPB-skMPycczNTUAxVuY6BoX1MxZLl9PV6bgP0xYXI6yUnawZptjJ4caDdV3ecWzvUNvxPaYu0kRrBi9hCUqDVbeBtg4vHHTSd7M9ekN-r7J_5IpDi0sI6VThe9kQVnalGkgnIZkjrNyPZdXIgJ-zegDk_mV6rv8YXU_-sVHWyMQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=miTZ7PMYSurV8z4E_I3P_3rJmEnxohH0Z3xEO4KLA1q9iP5tyKZqkwLAln3tAySBrx0XkqOXfbV1k_9IY8dv9xYP09lYiLexUi3UP_OawWiTcE_UngfJj_tVjwMG4ueAfhzKtTWfL0CoZtscKse2n_sWDPuxyYW-r6CFs91zQeJHKYpfsfeB6g5RcwbJN5UnS1NPaSsS0Hp-wh71zjvghyZC_rkbeWbLKpgSRV9f6XbClHWJvn2G9aeY7ZXX5RrOgTHR8jXPUwS-BZh3NzqT6MzNlYPXlMc7WgI63nBIYI600XpjsQKs5QN_aJQXT76CZ3orUw0GtAvLEI5lPCQJ6bEW59auoWRdndrA3MbCtj3DUsTFwPyUvrKc1vWpc_gL7kYdENHlen1pZq_BkR6ycD3DsWft8O5L_0RMxdRtIwKwT76h2jVBTAVCUzXvkDbFWFw2X7mT_6GTK8J11P-dV4j7Hj2Xh2xIiNtunaXrXBpiHvdJrxRy3um8WPi69yoFRzaqT7w2_5dh4Tckp5IcQOs1oIV7uQCxJOkOIuwYV5GmaSvik4dl0uIPaOnjExjnfquCaH10il9Mn-clE2bbeHJHw2mK0ngZ1BeNsw41Sne3wPL_3j0S3dYxehR6KQpS4HdgXi_dIJ96LwCwH-kqp8GCOrpBYFsemzjkGZzmLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=miTZ7PMYSurV8z4E_I3P_3rJmEnxohH0Z3xEO4KLA1q9iP5tyKZqkwLAln3tAySBrx0XkqOXfbV1k_9IY8dv9xYP09lYiLexUi3UP_OawWiTcE_UngfJj_tVjwMG4ueAfhzKtTWfL0CoZtscKse2n_sWDPuxyYW-r6CFs91zQeJHKYpfsfeB6g5RcwbJN5UnS1NPaSsS0Hp-wh71zjvghyZC_rkbeWbLKpgSRV9f6XbClHWJvn2G9aeY7ZXX5RrOgTHR8jXPUwS-BZh3NzqT6MzNlYPXlMc7WgI63nBIYI600XpjsQKs5QN_aJQXT76CZ3orUw0GtAvLEI5lPCQJ6bEW59auoWRdndrA3MbCtj3DUsTFwPyUvrKc1vWpc_gL7kYdENHlen1pZq_BkR6ycD3DsWft8O5L_0RMxdRtIwKwT76h2jVBTAVCUzXvkDbFWFw2X7mT_6GTK8J11P-dV4j7Hj2Xh2xIiNtunaXrXBpiHvdJrxRy3um8WPi69yoFRzaqT7w2_5dh4Tckp5IcQOs1oIV7uQCxJOkOIuwYV5GmaSvik4dl0uIPaOnjExjnfquCaH10il9Mn-clE2bbeHJHw2mK0ngZ1BeNsw41Sne3wPL_3j0S3dYxehR6KQpS4HdgXi_dIJ96LwCwH-kqp8GCOrpBYFsemzjkGZzmLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=O6rO5xi_dMPgc02hOg8g3Q306dq-_L4jFSwnsDCUtNPTuDuKiWDu_5YGhGAWANr7bW14espy1XV6bUOpeB0WklmIyoUW01mCkNJAh_no-ysFsCxfZiOVuB6Aq3rzzqF_bFxiNT4N_AxVoFk0MfBlZGuYar7WgLUIXc19cco8BT8_wgmzdP-RmY1D5kSN9zyf5bA5XiXjpD3sV0RMnIQOrZiucuophsp_XcuX4dA8CJgn8QWtgVG9-yiJ4XwqewdV-2ljTmSGo1J_36IGPLJ_AQy8L_7sycdoSzdTkv-bJRA9HF7DJ8pmSatuzvtHlRcpC-CFOMMLAp6yeA5sxbNsTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=O6rO5xi_dMPgc02hOg8g3Q306dq-_L4jFSwnsDCUtNPTuDuKiWDu_5YGhGAWANr7bW14espy1XV6bUOpeB0WklmIyoUW01mCkNJAh_no-ysFsCxfZiOVuB6Aq3rzzqF_bFxiNT4N_AxVoFk0MfBlZGuYar7WgLUIXc19cco8BT8_wgmzdP-RmY1D5kSN9zyf5bA5XiXjpD3sV0RMnIQOrZiucuophsp_XcuX4dA8CJgn8QWtgVG9-yiJ4XwqewdV-2ljTmSGo1J_36IGPLJ_AQy8L_7sycdoSzdTkv-bJRA9HF7DJ8pmSatuzvtHlRcpC-CFOMMLAp6yeA5sxbNsTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=tzkZJF9K90_T486iyIDYa6Se_PaqaqlmymrvTnMKvQMx3i-iPEevubd9PL7pVFAl3W12ZXbG4mS26O-62IuW9L9AkZEOYN0yVWMasBlWMsygQkm8kzyOwym6W6WTDmCA9JPCv27pGQ3piB6qvcrrJv2qYMpTMhCy6GyhqhfguGP0m7ECxqs7j6ebE6BinDMVYqW75JfAVYthcMCJUHOEGTXw0DHlB89sQ1Ptvy0WnQAuiYxEzWY1AmQsui1SI5bpRlXRMu44jf_GonDvAa4ukh1z86DpSrPMDFH3XLhQFnZ42FK2tf979APmu2XjxcruiAl1svrA1CIicqN23aRzmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=tzkZJF9K90_T486iyIDYa6Se_PaqaqlmymrvTnMKvQMx3i-iPEevubd9PL7pVFAl3W12ZXbG4mS26O-62IuW9L9AkZEOYN0yVWMasBlWMsygQkm8kzyOwym6W6WTDmCA9JPCv27pGQ3piB6qvcrrJv2qYMpTMhCy6GyhqhfguGP0m7ECxqs7j6ebE6BinDMVYqW75JfAVYthcMCJUHOEGTXw0DHlB89sQ1Ptvy0WnQAuiYxEzWY1AmQsui1SI5bpRlXRMu44jf_GonDvAa4ukh1z86DpSrPMDFH3XLhQFnZ42FK2tf979APmu2XjxcruiAl1svrA1CIicqN23aRzmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=FeYevFBiLM9_mMl7WaybJLcGIjVsVbl6YHdKMa-vhcKHqlbEPrD7h_15K6e_gU9QU-14A6JKxR0dB8v6AP4WiHjz2ANE5UOlglXI3oZP6f3BL9ZEwkhoajFeU_B0hT8_IetDWjladHp9KpR7P5p9IjEO9h8hzOO0Ih-zHciHKKxH-7nyCp9y4tRDi86yTvjLJrh3FeiT96RUW9N5ytguG55J-6XiJ0nU0_S4hfcfkEqhs9BSsqitrozvCqAJ31JJvZ1civonKn5OwJDMkMREwaxDYf2c8JY6UOjqJScX4L3qykfbLeiL8FnOnbrGd55wvseEdU7pPBxe-tSN18Iphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=FeYevFBiLM9_mMl7WaybJLcGIjVsVbl6YHdKMa-vhcKHqlbEPrD7h_15K6e_gU9QU-14A6JKxR0dB8v6AP4WiHjz2ANE5UOlglXI3oZP6f3BL9ZEwkhoajFeU_B0hT8_IetDWjladHp9KpR7P5p9IjEO9h8hzOO0Ih-zHciHKKxH-7nyCp9y4tRDi86yTvjLJrh3FeiT96RUW9N5ytguG55J-6XiJ0nU0_S4hfcfkEqhs9BSsqitrozvCqAJ31JJvZ1civonKn5OwJDMkMREwaxDYf2c8JY6UOjqJScX4L3qykfbLeiL8FnOnbrGd55wvseEdU7pPBxe-tSN18Iphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=g50eDGST2NRhus2_9QOAf47-iXA4w13EzM16yl-IDtzIv4-XtSYVks3qaUAAMg_OzX4exA-5xOJeR2F8AQL2pqQ9gGUo7QrhzAxD2gS7n3HQRKeBR-zENvFx9MqhgqaLTmG-JlST0SHFPGfEP8y834Vu24y2TbrqCtrnDt1ti9sL4OAyd2YA85lHXZUI7adKA31PrXLsll4E2s68_83Lm05LdhKPvPRU93a6bYxEQj1oOgP2ayHaUavgFzNplaTCryOOyULZW3X4vADpKAwCXnvS0u_yQ9pMT1oDoQ1L3ZQeQLTG6bMgv8MX32piS_hHsocq8QkZSkPp1cKVsDNnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=g50eDGST2NRhus2_9QOAf47-iXA4w13EzM16yl-IDtzIv4-XtSYVks3qaUAAMg_OzX4exA-5xOJeR2F8AQL2pqQ9gGUo7QrhzAxD2gS7n3HQRKeBR-zENvFx9MqhgqaLTmG-JlST0SHFPGfEP8y834Vu24y2TbrqCtrnDt1ti9sL4OAyd2YA85lHXZUI7adKA31PrXLsll4E2s68_83Lm05LdhKPvPRU93a6bYxEQj1oOgP2ayHaUavgFzNplaTCryOOyULZW3X4vADpKAwCXnvS0u_yQ9pMT1oDoQ1L3ZQeQLTG6bMgv8MX32piS_hHsocq8QkZSkPp1cKVsDNnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=BEpebGJ-bFwv9hc9SRoWCMKf1fWWpA64Xewpo_rw9H1YdM--fnmwW0At593hU__lWX6HcJ2FqTcZjs5szzkYoUTswO6nHzQ3CdN1nsQSsP7OZW0lFGtGCC1tOrdmoDKiVOjdo2bqXtr3y5lULTC4IKo41lWpvsvmjfailqa8IW3ned3v_fqkA7UjBoBlg58pitmKyuA_3JeQGYP-urOvLn5TTMNXphVN5kH0hUDl72OFpWD6vebne0vxV-eu81zHZxt--VICNOjizcQEuiVOXcgtMtHxfNVPb91vMQ1oVSdZcITN4OnaxUwP08Q2hdKqkuPTS1eC4xJ6E90xOqn7_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=BEpebGJ-bFwv9hc9SRoWCMKf1fWWpA64Xewpo_rw9H1YdM--fnmwW0At593hU__lWX6HcJ2FqTcZjs5szzkYoUTswO6nHzQ3CdN1nsQSsP7OZW0lFGtGCC1tOrdmoDKiVOjdo2bqXtr3y5lULTC4IKo41lWpvsvmjfailqa8IW3ned3v_fqkA7UjBoBlg58pitmKyuA_3JeQGYP-urOvLn5TTMNXphVN5kH0hUDl72OFpWD6vebne0vxV-eu81zHZxt--VICNOjizcQEuiVOXcgtMtHxfNVPb91vMQ1oVSdZcITN4OnaxUwP08Q2hdKqkuPTS1eC4xJ6E90xOqn7_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=YLpV-NQQbVQi67_GDs8lv2zrrOVudd4bYRXk559VSPiZEUFBm8f5yt8tfrqfK54imxoJn8bndhsNpZyC0ej1rkA_oEMHM7riTmGR2O5Ha7PcSfawFtloB_AfoFaWyVcs4LnL9DFASc9qusjL-ZwXYPTrEFZHiI99Xv-3nSMivUaKckRmWfCkv81gr_0qNDelxL6piijzwecFFx5IvtmmA7uxiknYmD2oCmv1dkCTZmzWIt14RkH62rAGyVd3hTBD8s16be5eytEIFJfJ2lB5MI4pd11SkBbzvt3Jr1MJXH2H01lYZ0X6iNBVlFttokHnWh0lXqtLUOJn2La9Yh7huw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=YLpV-NQQbVQi67_GDs8lv2zrrOVudd4bYRXk559VSPiZEUFBm8f5yt8tfrqfK54imxoJn8bndhsNpZyC0ej1rkA_oEMHM7riTmGR2O5Ha7PcSfawFtloB_AfoFaWyVcs4LnL9DFASc9qusjL-ZwXYPTrEFZHiI99Xv-3nSMivUaKckRmWfCkv81gr_0qNDelxL6piijzwecFFx5IvtmmA7uxiknYmD2oCmv1dkCTZmzWIt14RkH62rAGyVd3hTBD8s16be5eytEIFJfJ2lB5MI4pd11SkBbzvt3Jr1MJXH2H01lYZ0X6iNBVlFttokHnWh0lXqtLUOJn2La9Yh7huw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=id71aPA_IRNUVN4Ti5b1dr2U8Cb7axbCisW-mXS36OgmWvxPBT6E5dNxu3_4jOgH82Nz0cmB4KGhr9bUom5tNtxO9YpLQUrQvxNJOCIUV3IdLfusNelYgroUh3GBI1Aei-Il4MuI1S0e2Y2oQMBYa_aaQ4w_cmpmrjQdcyT4LEJPewub32Mx0uBNz3xGfOKfqmyoRFNDlltt43-8jix-L1p6_EYC8xyWjkyxkt50rs5K-n53qsQNpIN88RsnIXITYU-ZUBYVZKnDuAb8gBCS5Z07ZIGlIpNS2yYkdFVNO1QEnQpU7yUbJxvIr1w5HGkJRnuJUiHqzo_C-KOBXUIrbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=id71aPA_IRNUVN4Ti5b1dr2U8Cb7axbCisW-mXS36OgmWvxPBT6E5dNxu3_4jOgH82Nz0cmB4KGhr9bUom5tNtxO9YpLQUrQvxNJOCIUV3IdLfusNelYgroUh3GBI1Aei-Il4MuI1S0e2Y2oQMBYa_aaQ4w_cmpmrjQdcyT4LEJPewub32Mx0uBNz3xGfOKfqmyoRFNDlltt43-8jix-L1p6_EYC8xyWjkyxkt50rs5K-n53qsQNpIN88RsnIXITYU-ZUBYVZKnDuAb8gBCS5Z07ZIGlIpNS2yYkdFVNO1QEnQpU7yUbJxvIr1w5HGkJRnuJUiHqzo_C-KOBXUIrbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpdvrdIas-oHp-H_j8a3f6sZZQyb2AhThkJkoXehZX-B0HwlqwHOc2Cwqk2x74hRC_AiYBbejHE5LBzQkpfGrmbNo-9DBH9et7CPCT8sLbRWAc2JLlFLIXPGpYDIocoD8eeJvqG3GjJBxEBHRbs5JT0djc-ytPNEFkJ_gMpkrOOynfrzfjAE1NQIhnyY-5u8LSmbexaAiP_hIeEAHQDGgkICJq6TxfXSQE7sex8gOvCG1Y9YmxWCPMBEn3TxSoqlURqrG8oyTKOGI9ptdrf7wE5Fc7_Q48TVJI9lAHuNc41DgQw8LQPfPZLTv4Kar7foMYSD0kF3_CH5eQs15goxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=HkUce83VoyTXl9XFwojjAPMPksgwCwQ0wPYMjARQ2EG2ClOfyUdWh_98uMiSDIoxocrqRsqeyYalGx1c0_IGZurm3aoqF1YOHwu7Z6fLv-aUgoz88ZfV5Ac1x55LkidkYdLxLeZLOle37UAXvBWPNPyDupLz0nUDS_JhrzFaLlGDQUL9F1ApiMiteda3QiayK5uPIx_tW7-FZBf0Oq3kPYFaF874eKfHLK1hjySdX5dh9zWzANHtJ6wsG75Jt8juJGtIKHh04de52k2RUogokNJh7vmO22H9ZP25XY-MfX82icCNXWgGvpfSYXRUTPP_fEYLAcA1-GYIq7VXyBpAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=HkUce83VoyTXl9XFwojjAPMPksgwCwQ0wPYMjARQ2EG2ClOfyUdWh_98uMiSDIoxocrqRsqeyYalGx1c0_IGZurm3aoqF1YOHwu7Z6fLv-aUgoz88ZfV5Ac1x55LkidkYdLxLeZLOle37UAXvBWPNPyDupLz0nUDS_JhrzFaLlGDQUL9F1ApiMiteda3QiayK5uPIx_tW7-FZBf0Oq3kPYFaF874eKfHLK1hjySdX5dh9zWzANHtJ6wsG75Jt8juJGtIKHh04de52k2RUogokNJh7vmO22H9ZP25XY-MfX82icCNXWgGvpfSYXRUTPP_fEYLAcA1-GYIq7VXyBpAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XUGK7-IT9zWENGSfbUE5AdH7Ds2OtA7gjf6eVGsaNFxnaq0m59fpLUq1lFGO7cQUMJO3bjeNhpycqDxz2jyb9t5V_sw2c9X7zwHKx8ImR6ApzVfammqDbnKvxqtYydxNJ8y6_48N9_AoQbVL8fsEiGfxfsyrEiVDkFLLhNtZ0R8205NK5NoIvv1qXLJ1L4RSxcGjHRqR1t2uXOFrok2wqdeUnM3D0lI3xBW4Gy0DZ7yWs0XYcF1o-zjEEDJBTyp7hFTJ6W7Y0ouVPwAVwpr0xavIL9L4yQhG0_Tu-VjHgyyEK5dAndXc4wQ5HYWWhnKs3BjKs1pboq70tIYKsGKxWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XUGK7-IT9zWENGSfbUE5AdH7Ds2OtA7gjf6eVGsaNFxnaq0m59fpLUq1lFGO7cQUMJO3bjeNhpycqDxz2jyb9t5V_sw2c9X7zwHKx8ImR6ApzVfammqDbnKvxqtYydxNJ8y6_48N9_AoQbVL8fsEiGfxfsyrEiVDkFLLhNtZ0R8205NK5NoIvv1qXLJ1L4RSxcGjHRqR1t2uXOFrok2wqdeUnM3D0lI3xBW4Gy0DZ7yWs0XYcF1o-zjEEDJBTyp7hFTJ6W7Y0ouVPwAVwpr0xavIL9L4yQhG0_Tu-VjHgyyEK5dAndXc4wQ5HYWWhnKs3BjKs1pboq70tIYKsGKxWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=j0fB_NUx8TOgNBy8tLIeLzUHJKXsudS8F4afgIM7KCNTd1s_KXU00pvic0W-Nvnk6MVqg7SZq9XSrWRBeqCW3zncVS29vHv6V_xo5Zm_VATKtV3z5SCAGAgxL80i3Mf7jQ8xS2-XC8LGC5cU3ZIKkB1_0bgwK2nZa3y5xUYENl2M_Tx9mG_tjjbIxdMpPj2eqFd6gii8bxbARXzSguYRWeVRfSgNNFe6rWmemBR9-t_n0KfuGY_AnXn1qK19IslHUrCRjrxci8As2akj52BOhZual0pHrdL-ySg4gg9hfa3HknydP-vqPCN13gZ9inSGtY-uq09-8jK6f5sWkMp09w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=j0fB_NUx8TOgNBy8tLIeLzUHJKXsudS8F4afgIM7KCNTd1s_KXU00pvic0W-Nvnk6MVqg7SZq9XSrWRBeqCW3zncVS29vHv6V_xo5Zm_VATKtV3z5SCAGAgxL80i3Mf7jQ8xS2-XC8LGC5cU3ZIKkB1_0bgwK2nZa3y5xUYENl2M_Tx9mG_tjjbIxdMpPj2eqFd6gii8bxbARXzSguYRWeVRfSgNNFe6rWmemBR9-t_n0KfuGY_AnXn1qK19IslHUrCRjrxci8As2akj52BOhZual0pHrdL-ySg4gg9hfa3HknydP-vqPCN13gZ9inSGtY-uq09-8jK6f5sWkMp09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=XFPU5Wb8EYqIsH6FLZBJ4BsnOr5oJceaXV-oOthckMKOjEdnV5cW2-T2n5Qqfn-ZDPGqkYUri7Gj6twNozhMbXjSHHfC0ulaGGmGj2aoW7QFMGqxdRlXmUJFNJVOcqvXBCuWu_CLuG3EfnCuGZQGiwx8TuVlpKnbvkQicMqwWoPnIKIZWSJ9iocyN4GHEP9a-Qni27z4DlnbKhWoD9X9sTKhXD-rPEGZmUDLbD_RhZIqfEo36xsZeqz_IevTBGm7BzrFELJtTV7T_H2qYstw0nlhhS_rqNOLTKqjSJtp9zAdWVsBamyOJpw2SbX_anSNwHboGBzY6o9bVZXmgxns2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=XFPU5Wb8EYqIsH6FLZBJ4BsnOr5oJceaXV-oOthckMKOjEdnV5cW2-T2n5Qqfn-ZDPGqkYUri7Gj6twNozhMbXjSHHfC0ulaGGmGj2aoW7QFMGqxdRlXmUJFNJVOcqvXBCuWu_CLuG3EfnCuGZQGiwx8TuVlpKnbvkQicMqwWoPnIKIZWSJ9iocyN4GHEP9a-Qni27z4DlnbKhWoD9X9sTKhXD-rPEGZmUDLbD_RhZIqfEo36xsZeqz_IevTBGm7BzrFELJtTV7T_H2qYstw0nlhhS_rqNOLTKqjSJtp9zAdWVsBamyOJpw2SbX_anSNwHboGBzY6o9bVZXmgxns2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcDV2eVvZJCR_p1IEeF5v7hN6WDTmFRy_UigUpquE8DFRzfFBjOxTcv3PatvM2Q52AqSE0KKC6KQeoBD6ks7iqsL0Kv8G2X8dN_DoS39_nG-2h31mQBVNf8wNChizAfLy2hfO0G8JhM6qgB58V6IQELKA4RMZ7eesJRHE_s9BcccIUPeMWc3k_qQXBMMLSiobnfDEoUTte8uxh9azrYZVwMQl2sNUhoZP9LTMS5juRlDTbzm6Y01DmFop76NGSs6bEEIVvDH-vxSW3eZPwDzddwAPmfg1pK_cS-BlV1ybnozfIDA8dN5xAPzdg8diMYwX1s9DOdPA0rijzzj_ER2Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qy0VQcVz_W7_0mapwit5EJ-16bGQnrLeRbR5IEZFwHHarV2PwCiL2FRCFYutgZf6QrN9LI_ZZnI1HjbfGmiWVaZIQh-XQT5sqNHWs0ZarXJyIfRiHg5MMYWsF6s0xeb4SIAuwON_HMMUOyQhfnvj2n4C0EUp8Hg5RGKpseotDmsd2cJ7Y6-3F79DZx9GpITMLmSNqEN5UXcCvHVDBmJdil6oAurkRo3KcMyc9qfqnhOAx_VMMVaBh1Jjghk1FC1Ayf6zvNZMraRg17oUprIl49g3vrDDvI4Y87OnzHe0Q41ZJ3RXeG9WIJ_6Q6Q3PsRn-Jeq8tVygP8jhc7snp0eGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qy0VQcVz_W7_0mapwit5EJ-16bGQnrLeRbR5IEZFwHHarV2PwCiL2FRCFYutgZf6QrN9LI_ZZnI1HjbfGmiWVaZIQh-XQT5sqNHWs0ZarXJyIfRiHg5MMYWsF6s0xeb4SIAuwON_HMMUOyQhfnvj2n4C0EUp8Hg5RGKpseotDmsd2cJ7Y6-3F79DZx9GpITMLmSNqEN5UXcCvHVDBmJdil6oAurkRo3KcMyc9qfqnhOAx_VMMVaBh1Jjghk1FC1Ayf6zvNZMraRg17oUprIl49g3vrDDvI4Y87OnzHe0Q41ZJ3RXeG9WIJ_6Q6Q3PsRn-Jeq8tVygP8jhc7snp0eGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=mi1frpQf8-wikVZZ0pjpNOJxz0uQNtyKWLVbQoajeRQLksCyrWFgB8fD54bN_90ZWs64-wluOxaml9uOSwhV0EbCmmnjpRbwGrxL0BAqTpcSqG5vFijdGgXs43QELVWrkXGEG8N5GJsvx2Bbe2r00NDQxlY_xPIg14PoehjhcznkB9x1kv-R9dC3fQNZn6T42djDXGYQfu7e2qiITbSPAu_oXIMCE1sTsLqflIDwB6M6STY3tNT6ASkPaf2iS3hgdy413wY51NRUPawcMydxtj7wqsOQnlZiudd_KPUuR34CB_3rD330pH4H3nAfw6BO7EMRI0eW8p4WhHfUP0gSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=mi1frpQf8-wikVZZ0pjpNOJxz0uQNtyKWLVbQoajeRQLksCyrWFgB8fD54bN_90ZWs64-wluOxaml9uOSwhV0EbCmmnjpRbwGrxL0BAqTpcSqG5vFijdGgXs43QELVWrkXGEG8N5GJsvx2Bbe2r00NDQxlY_xPIg14PoehjhcznkB9x1kv-R9dC3fQNZn6T42djDXGYQfu7e2qiITbSPAu_oXIMCE1sTsLqflIDwB6M6STY3tNT6ASkPaf2iS3hgdy413wY51NRUPawcMydxtj7wqsOQnlZiudd_KPUuR34CB_3rD330pH4H3nAfw6BO7EMRI0eW8p4WhHfUP0gSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCSvXEot7041MrjFpEMD6G9aDYH-VmG2SSXkZjKOQ2cVgon3NTyOwV8ggDMkAAMPd6daLxYnkoq1rxDQTpg-ff5H1K_p503tR-6jL9Sgo64cw1tjrt2Cmaj1S8BWldygdxjgR-25vnWYGJGlXc4pw70Rj_hsTHBfgKN6umm32WjzIxgcLaGr-QzEIS4oVKa4lUMPsWf_x7OP9NCCvhckwcw0el84Oxg5WIX9zJF0Vs-a5LBbLwrzkXtCh4qGYucbXKSDp6OntSuuF0najeBhfQtrYontl-2i6KVP1RRgpimUw9hhdRy_UVLoXV5iyz12uRi2OUudZQlF_90To4LWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v0rHBPDOODHE5ZyrwCh0ZskEaHvoYTZGFn_awPmB0oUux9SCzi_02drGd78Ab3nDo8JcCFWYsz4qLsnp9q5vyvAAo-N9ZI-6roACWmu43YZgH-nTYuvn4Liisy_EDKlCRaUUYhgxHRMR8UaLVCe4OIEDYjckOsw2yApIlGc_sOyKFSB56oCbD4nDs2QGcZiKF_4wjmTGy6bXe7SBtGHsIlee5rqop3TcbC-TZh04HImxpP-rztrMAtiYN3mo4bTeYUWqnQ4vbm1H02LgOuCytljEZ_1Vk6jQuz6O2Z6uDih_-jI0_XnWpKlgTW5Gg4GA5KyX7eEv9s4wuYNL3WwUzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=kMyGZKTCHFA61o3gNPYpGZmtNnIVbnpGN-hoEwendH2C7BpvKtF2Cv3vqIHO8NOr_0sg0iegkh1A5VZ98LDy0iHcvVC2ZGp8HKz8yhNoGf2O2ckpvUYughSJKYE4FZfF9G0yCyMmQgp4Q10s4wP7kkHTzApmbPeH_CtXLCiBKzbzsLmfxFUWqSwi-5NylVfLIN1opPsmT-YLLCikdbZimklps0oL8cpkEtb31n_fTHFSODT_J1tM07fLbJNhF_2WUNmkiebeEzUa_R4FWFr0dq9ObBniNk4O4WEzuguJHbNNfBCWnbWf2cG6ww4dMb4Ewp3ydUaRzvm_zYzqTU3wrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=kMyGZKTCHFA61o3gNPYpGZmtNnIVbnpGN-hoEwendH2C7BpvKtF2Cv3vqIHO8NOr_0sg0iegkh1A5VZ98LDy0iHcvVC2ZGp8HKz8yhNoGf2O2ckpvUYughSJKYE4FZfF9G0yCyMmQgp4Q10s4wP7kkHTzApmbPeH_CtXLCiBKzbzsLmfxFUWqSwi-5NylVfLIN1opPsmT-YLLCikdbZimklps0oL8cpkEtb31n_fTHFSODT_J1tM07fLbJNhF_2WUNmkiebeEzUa_R4FWFr0dq9ObBniNk4O4WEzuguJHbNNfBCWnbWf2cG6ww4dMb4Ewp3ydUaRzvm_zYzqTU3wrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNpppmZAUqoobrTCELU2qN-OLHbgOklfv4_FVZ9YVoP1DRuSaugeOmP67CmeWWnaQ6RykV1W29MNM93UzdokgbGsH0s7LfHUR2Wy9n-C5B8TuZaNQo7b2LL0e5P1PyZ8-_KUclqBHcVzBDwMhSGkHE8yZzYYSI4gQJ3utWd3E99vuSnkzDK8I7YEPPxNhiE1gmTiMHdcNOE9Vs3poQ2jkSX_lYX8fJI3f-HKQiT8PZtYAAmk_F03Gy_4Do2S6OpI_v0oNq25FOYd-2bTQp6_UX8xGaqsOIXvz8ugxFLpPjotwrzZ6qhQ6E5-Hf5Ji3_3MTxcRmVK1iNeoaXYcsjbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLSIe3MWQnm9vXRRMoaFC_4mQ7v9XKpEilYxlGywuQkGKz9mDI4-N86NxDCtM7MM3gX8vK2R_JyHK3QQe9fPO12Q7LcOpavoV6G2MrHsV86Pe4YzR5mTXyIaLUF-YMT23i2XmoRjU6qmGa1aqX--WieP31N6PpH3Ek7ne6pxkJZEiAmS6kwNisdSXdADulGHZWg_8cLZoaZzSPYJZLDI0QUBrkGlviJxsiJ7lIM8B5CLeylRjymn9mOEZO-qb7soRj0f4Z_AxZlsjBcRorChnMs2Cacn6fB1b8j74cZ6RDCdf42xHhQsFAEZ4wQG-kikZX5ILE3arvt7X2l3TVlhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POBvAqmktSwyaW8KSTZZp4TyLYsAyXewg77FWhyr02yW1sbJi0p3RrrdfIQHeZRNmf0hX9pYaHuWKCUHlBLWTMY4wU6oNXIZ6f9wmJHann5In6_U59tsPVEIeYaAmDWnlD4Lf0XoSiXNeBK1CVa5ilT60AOzY6Gn-Yu6N_dAwMNjiRkNpvFJbaCpMT0DtJ9BJN5oPRqAZZcUPzMqmloEe9ocZFCCHPKVtFcKJObGQXuptnEdlTjOLq9tKDEIZPLxiXspXoC2hbUkoJ1xOgUO0qf6kfRDmUa1pfVPOZMBlo8KlNMR_TZss--rEksSJ9yyJLZiWtl3dFTCMC3sBSnw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=dKhdOK7fHL77rhtLf4JhSgL6ktFnP1SaViyAtY7gVAT--o1Tu61YUmTCkn7Ew6sIyIZ1u-xH4mKQXfahjDMkECdRaAK4ZQFbLVyi4uP_Q4lF-CbcJnGAftn6wpiRwSWuN3Za-MMNkdK-kwaNubERhs8Syjx9ww6YUC5veeKVw-Nj7sIy789ZpvsfqUwy95xb3-1qV66B1zecyl8_QRDDA-ajtnx9tjg01dYny5k3cORiv6am9TO8WyyIIB8DJQQD2b-RXrbb8pXo0_I4EWfGDjURIec-VuFBhYPFQNFwBMm-hlZAtVmU4uJ96s884fzGCmhJ3lfL7H3CvHMFdzCuHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=dKhdOK7fHL77rhtLf4JhSgL6ktFnP1SaViyAtY7gVAT--o1Tu61YUmTCkn7Ew6sIyIZ1u-xH4mKQXfahjDMkECdRaAK4ZQFbLVyi4uP_Q4lF-CbcJnGAftn6wpiRwSWuN3Za-MMNkdK-kwaNubERhs8Syjx9ww6YUC5veeKVw-Nj7sIy789ZpvsfqUwy95xb3-1qV66B1zecyl8_QRDDA-ajtnx9tjg01dYny5k3cORiv6am9TO8WyyIIB8DJQQD2b-RXrbb8pXo0_I4EWfGDjURIec-VuFBhYPFQNFwBMm-hlZAtVmU4uJ96s884fzGCmhJ3lfL7H3CvHMFdzCuHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=WyQBOvS1k9-dDa69GMz3vru2AZCNNRTkbph-dasjqOvEgUuOnbjWYH8feTF0IAe-3bOun_ginjdHla4zcuGNB0pqIC34VSmVvErVCUEO64rl_PgeWMU5a0I73m3nhPV6ZHp4YpKckMzRPeECfj5hta1tYZ_0u7ZHnmM7F4_vLt71aP2MwYZgCpg5AGa6V9JCh_NqvYEPb1MvrEmPS1UN4Z43lpx86eWVtF5IcfgM4SmzIEEpDm7XK4wLYwtJfuRfgiDNZpAO1IoPo4YmhfQH84PDdwiPIMH_RDENM_7YGr3SM6X_gZzC1y4WVHdcvJp3flKqLkAEBLkRBULmv-OF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=WyQBOvS1k9-dDa69GMz3vru2AZCNNRTkbph-dasjqOvEgUuOnbjWYH8feTF0IAe-3bOun_ginjdHla4zcuGNB0pqIC34VSmVvErVCUEO64rl_PgeWMU5a0I73m3nhPV6ZHp4YpKckMzRPeECfj5hta1tYZ_0u7ZHnmM7F4_vLt71aP2MwYZgCpg5AGa6V9JCh_NqvYEPb1MvrEmPS1UN4Z43lpx86eWVtF5IcfgM4SmzIEEpDm7XK4wLYwtJfuRfgiDNZpAO1IoPo4YmhfQH84PDdwiPIMH_RDENM_7YGr3SM6X_gZzC1y4WVHdcvJp3flKqLkAEBLkRBULmv-OF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
