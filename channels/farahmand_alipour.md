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
<img src="https://cdn4.telesco.pe/file/c9IHvvgiUOql85Mp2U0LhY78Npxybz8jdvQEnceRas01p4Z9zjxt4QDJNn_c3z3gWUR1Xcvc8ZfE5fjv8w9kYzlp_ivXfSNSz6t1JuaMn1cKgYne0mZZkbNrRK299eCqe8zTq3Y5T3ey67EA0auh2FwX0eI3neHq9fy_fHXEfW4q5kMWXXpJPeeZVQi4n8HoXPMzpSCpdqsj9jAFOOzrV2Mks3I7OKcFz_zlqFpg7yxY-VObYj0slF826BQUGJX0OaVrRwrpnGQ_Sc9EsGkaN2sKzOFrmhb0p3_lbqb2x2CfcxxrSNSLScmS3vWfaQibLfg2a0Hz9wDST8Gt0BlQOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAAJtGsYhKZ2KbSpP-gz4HwySCzd2d1BcUFVb6GKmvRov4SPbb3C2zfV9TK97aiSc817z2r4rm9jyEux3Z8m6menLemd1bLdqmbyEsRmmI-kNTJi0j6NZxwSVGvMxoQlQSCEILFK8GHtMTncs7Z_8aXgAFXrAsOuwvv67kWPq_-ymLm7A90ZvdRSZUkxBnHmZ8K0W2Xbv1DYQk9SMIvaWuZ6DUw6OI-0Ojz4lFw8Y-ifFtcfzipf9tXyC8A30-tc5wlxbgWd9w2PdOg0Nr5R6kgpbDfFlbDuz18jb6jrwCyAOABX_4GCjoMx3LzlRZ_5CK2YKST1bgg6bnET35PowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb-Aq-MuR1ioIxY9UVxe-g9f0yD0WUcdUPQC3g8ClTnizhJxtZRaFV7CuOU7HIdLzVNFTKJPnbDikY2N-aQdNuXOKTwTqC-AuqunTzhCT785J_ACoCs7KkzkB4Fj_lWi75BlThQIDdNsl1cCznHHBPwZdn6coBzuv1eKX-9vlVAU8JmrK37eH1OETM2C0nK0HwxQP4unvp9xw5u49QUgGFaek3hIWOxLddSUXLDI2cHImCb7rgijqpqY1g2YeqMKKo6grWQ_e-tuaymQyhkK-PTut5MPDDcTHAEIM63ErIE5f7lowo06UXF81KFlwvNpLk5jfPLwipf14yaw1FZwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA4Bro3et5FxCJ13_Zeyi8c61spkjNBJGI5i7VcTrHX_DYTlqY7AhMIalBAZgNQGl6p4TBzUdTQtuNflLuXPpBwbGMRfyOO6D0lE9QNFZ6Zlcp8x1hjo4WYcJbipLjr2OqlHzvZOqhxcQFHIAWnbEADkdlyVxPFZaAyzaKOm1Xc9J4o-G0WC2Zu8albXnqRTBaJEWUTZqoB50CBVmn0h4ZevxpgBp6SmKMslX2O4ERlXj3mN9O3OQByWkcJURcJCkUKYN7VIGiSH_8KYZzmdKjU86Jt_F0nk0KsqDS12rtZFPtpFvXnYYtRJU3NlUtSkZadXSRKvuv46uY-Q3uPuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=seQWSGo_aNCMGWJ4lHrVl52CS5jx8BPnPH4Kd6QH1W3OnxNon5YxnIJ5DD65RMsbvmd3XrcavsyUAtU8Ce6T_rP91v_9HH0WoRDuVhNZkPgHEy7Q1eAVpMAFIZMwCxlwEXpTNUwu6zLTSqDuh97LttrPr0nWuS8frHyJgxCsf-zImq017rpHuZ9QsA8BfHr-CYMIGgS8fMA1jEFVfWXGWXo3M6pLDh8tvLcQeEJS03b83qEKx2NF2guqJpDzwBJTi61c4mBwSd3K9aUOlogxJnWJohHVUKqWaOom7_4iE5yjEkL0sSfyMdJRLwN02p1MNTX6PzvFmAsoK9VV06tEHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=seQWSGo_aNCMGWJ4lHrVl52CS5jx8BPnPH4Kd6QH1W3OnxNon5YxnIJ5DD65RMsbvmd3XrcavsyUAtU8Ce6T_rP91v_9HH0WoRDuVhNZkPgHEy7Q1eAVpMAFIZMwCxlwEXpTNUwu6zLTSqDuh97LttrPr0nWuS8frHyJgxCsf-zImq017rpHuZ9QsA8BfHr-CYMIGgS8fMA1jEFVfWXGWXo3M6pLDh8tvLcQeEJS03b83qEKx2NF2guqJpDzwBJTi61c4mBwSd3K9aUOlogxJnWJohHVUKqWaOom7_4iE5yjEkL0sSfyMdJRLwN02p1MNTX6PzvFmAsoK9VV06tEHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=pN6ce55uOGGjFbSUMU-FjFFpgfO0G5xGeG2J3itNfCH-E54yc8qPh3jg-4w38YqfKWJFsRAmFNrWSPMR8j5CkkJJTZRvEFG-YA37RtHN5_9cNW9pnNEFv-iI80ho6dMY_57biL3HemchlZ7USLgFglA0fYlUNDzfTZYNgpk_LgAKOpPYh6KI3AhwCkB4gF5Hz1vKYP4rIxQ-_1JqbtERfR3uI7Ik3U-i_wNzBqmOaJtdsHLSoXKgDyuhybVTmzQMyusKgo2kJpMHvt9DoNp_L7xCGSWVy2uZLHeomR7WOH9P6ECQmvwIGmcQz7O34nh9BocLtQpswno9isRmQwrQjmdLCsBPYnkjznhp1NEUQgOpgiWpRkgmhGWZUQ8-Gz1kAQZ89SUpxpcd-heSUTCZbT3ayqQwODv2C88iyejSVP8XX93asyokTgioAGTdNXqCLDYnLvaw5JC4v3CyCvj-kYiI1I2pwZbVy3po_jxOepuxtt5uS2syJXh_o9i9ZT43vUlmefaifphnpszfS_eyH6k6BvtNLla7PGuohFTQJptrxMqFCdE25I9egv-R7Z3QODFuKkdQoRzdBEhmGDoEB_mSabIOVu8gUEItDJTnbTCLcIm7IkmfmKWLpe8A7WfyELgpbkkBWUEKrqllcgHCWPjziFI7U26k2iDUDTIDixE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=pN6ce55uOGGjFbSUMU-FjFFpgfO0G5xGeG2J3itNfCH-E54yc8qPh3jg-4w38YqfKWJFsRAmFNrWSPMR8j5CkkJJTZRvEFG-YA37RtHN5_9cNW9pnNEFv-iI80ho6dMY_57biL3HemchlZ7USLgFglA0fYlUNDzfTZYNgpk_LgAKOpPYh6KI3AhwCkB4gF5Hz1vKYP4rIxQ-_1JqbtERfR3uI7Ik3U-i_wNzBqmOaJtdsHLSoXKgDyuhybVTmzQMyusKgo2kJpMHvt9DoNp_L7xCGSWVy2uZLHeomR7WOH9P6ECQmvwIGmcQz7O34nh9BocLtQpswno9isRmQwrQjmdLCsBPYnkjznhp1NEUQgOpgiWpRkgmhGWZUQ8-Gz1kAQZ89SUpxpcd-heSUTCZbT3ayqQwODv2C88iyejSVP8XX93asyokTgioAGTdNXqCLDYnLvaw5JC4v3CyCvj-kYiI1I2pwZbVy3po_jxOepuxtt5uS2syJXh_o9i9ZT43vUlmefaifphnpszfS_eyH6k6BvtNLla7PGuohFTQJptrxMqFCdE25I9egv-R7Z3QODFuKkdQoRzdBEhmGDoEB_mSabIOVu8gUEItDJTnbTCLcIm7IkmfmKWLpe8A7WfyELgpbkkBWUEKrqllcgHCWPjziFI7U26k2iDUDTIDixE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5-jpsk29h3OrBJSiKzb420bjm3JJ6WCdAFVr6B5ulZtEmiKlt2Vuph1QeWlLn-veYkcMLMKxTzePbqdB30ScC4kTJE59P4FXd6pTakHEo3OtSBG7tf1kE75l6HEMxR10qh8UJ1VmauKIsbnB8zYcSm5Ml3gC1ioQeJ60sBF1B2zdirt4sCo0y-EpkcRg9YmYQXGsgO4zXpS8TrXDQQPyyGgT14IKwnh4VssCb6St2Toj34pTG0bTn3LTa4sIy0u0beKvDdwN0G_UuI3N-W2mgOftt0z_9W1ufTIq6Y9g8-B2oB97XhwSHAbOXuC_gkmYTGT_kSx0VsIuPhCfQ6jlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUNT1vGtLrTOKirN-fzO-COi1SC6TC2-mkMfV6lIlZ9eeDgd4lsvukJOU0uVfJqnK8XIg7W3kKJi5y_ZRTFlk5QO_jjvD7ecCVlrJsf2-ostwU3zo_Lf-fvv1YEZXL9HB9EjQRD-wO93CqVC2g30J16Lao2JnGxcTHmQVR13DR5vFmDJIWHxd7JeaXnITmUal4bDFqbGdq-vCX3zRnGYV4rRZ_D2Ajh3TrV4DTX1xlYUBwHTkyJ2ZW6xXUHBgirTC3Uz7m4Pa9Cn7AVq0wGNORn8C-GWEDzJbCC5RXxQ9jLIXzSZ9Ac4WOFXB-vSs2rxp2WTsiuh3d1iT2GQoMVGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfhHzxgnECylmpHTdf7SrNRHfSca80OjJkHCNQMwFrEu9PXXgCqkF_MR60zIlEisuLe0G4NPsNs66AyQ1PBh2Cm-tOYeHlUFZcm0AONTUdWEvYYSF281ugmHB0cJqVLsjt3rW5wtEQm56TdSg1v7PUQgF3wlegHH1NTkQ0Cko5soY5q-3sIZor70N02_jvHyhAwfYBVY43xY6lZ3OLo491bhOoyCRvsOAwxZ50sD2u-HVAMUHSZId3O_gcV7EPnxAgfxY60gp6-i4ZR-Lhhkgtt7Ldpz5OnnrcVvu51owCgr46jSibnkTUGTm2npmDXjdbXEDD3XPppQeOmb7iI0XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=UQGw0TFwy3yV9XsdOfeWAAKQ98_ISh0KpWoRb1KT2YQOFKH85xMEN3gZ78khKLfTlF7-6f0TVuqYD2xWfpo7cymhZ7Nc682HSvvBTSt1oGkVassZ8DkC67Hxo3_G4rxn1FlNYiMiYAeqp7LrOLPzLYEp2-mRBNJyhXNeJZZVi7wcJUZpht8zz5Xm_Jvb2JFf8U9Y5BrDb4Nj9Iz6q00uHdoRlfyvzuu0jIKHr9NKU_TTgISAj4Qa4UC-1iQaPDjRjeI2G0JJL23nxzKLdQEih4hIB9ndN14qWoRyMI6FC93kHG8LcLfjtEsUHlwBBXpDv-pvmL8wn42wDuQUzvxKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=UQGw0TFwy3yV9XsdOfeWAAKQ98_ISh0KpWoRb1KT2YQOFKH85xMEN3gZ78khKLfTlF7-6f0TVuqYD2xWfpo7cymhZ7Nc682HSvvBTSt1oGkVassZ8DkC67Hxo3_G4rxn1FlNYiMiYAeqp7LrOLPzLYEp2-mRBNJyhXNeJZZVi7wcJUZpht8zz5Xm_Jvb2JFf8U9Y5BrDb4Nj9Iz6q00uHdoRlfyvzuu0jIKHr9NKU_TTgISAj4Qa4UC-1iQaPDjRjeI2G0JJL23nxzKLdQEih4hIB9ndN14qWoRyMI6FC93kHG8LcLfjtEsUHlwBBXpDv-pvmL8wn42wDuQUzvxKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=nNrgY-4-RODjfyU4IIyngf1jj-h2OQDcZWq-jL7KUbtKsQENvsljmobSSt_xwyX04zFfcGR2TvVNi35H0VjsnztGQ2y7a-wAN_gQTYcZ5WsivmkaIH4HNFujG30qQktu4U424D5g9Uuqu1xHKRlxwY25B_9pYeHk0fGu4p2pAJO0A9YISsSI7Dqk07x-TJYSWkfQTNCWE5ChPPLuTKt7f1mm-CbbU8nQBgoHQriuYWjTHQdR9LKxGipG4FQZF4Gzt_T10ujIjXuKFvGLmtGrJEp2HpTSjKOAVrWeog_ujvZ2YSUSQyuStznnblR5ekO-pIFEVmh0ylTrmkl68ZNUsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=nNrgY-4-RODjfyU4IIyngf1jj-h2OQDcZWq-jL7KUbtKsQENvsljmobSSt_xwyX04zFfcGR2TvVNi35H0VjsnztGQ2y7a-wAN_gQTYcZ5WsivmkaIH4HNFujG30qQktu4U424D5g9Uuqu1xHKRlxwY25B_9pYeHk0fGu4p2pAJO0A9YISsSI7Dqk07x-TJYSWkfQTNCWE5ChPPLuTKt7f1mm-CbbU8nQBgoHQriuYWjTHQdR9LKxGipG4FQZF4Gzt_T10ujIjXuKFvGLmtGrJEp2HpTSjKOAVrWeog_ujvZ2YSUSQyuStznnblR5ekO-pIFEVmh0ylTrmkl68ZNUsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVCHQrgepFoqwd82Ti6K2E24Rns8lh7PMLVamjYBf_Su31SF0rhNGCtUep8b14MuhE6gkrHBG7rgIjmtLcM4Uc-_jF6hlHZ2MIRlls-9B9QXa02u2sK2SYSbz4YiYU0isvqLFxgTVy0w2Hl0usAbci9eswEChqrT5L5PdUyLLSHQpyoVxBrHCcovwUAsZxr3P-a8oa5cj7e0ow7uA0F4oT7aFJ4Dnx1TcDC-is6EtOcDDRWYBlqogqeATK0e832KrLWORIX3eHha4AiX4AKuo5xVifOihV5-d0gI596TNYRBU0gJ4bzIYDrqfwvW8wFGcK0Ui2fCljcnc3tRWiFNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=oFiY4aKrssPjb0Fq0c0oAwlHynUtXqr_7viZ39hVjDiTL5VBWI_SThwOZoZQ3APNnFfU6yp7x7vKxxdR86nKYp5kBpB4QpjeyOeXbvj0_NN-nQepBkV6ONoG40m3RRliaNUA07vz1CEuvZc6cDKVVadxaeaLylJthyMP96i7YyV1OZQxrWCS3-UwPsg79Xs34bK82V6QnMPknrRr38N8CUT9QkFey5hEVrZl2uQYcJ3TM0Fl4pOfQ8htmcrIaO9yslygszmp5oXvTcCXz5cqanIrkanmb8zngch115pr3vyDFEghRUeYYgcdGRL-uZBYUUu04Lp81ivPFtoZCTwdkDEE9E3MNxu0_JYU7MLytHAxb9Wd37ml0WE4UJhXSjHjxTH7EG8QRgIkbL0Ji33B5yjZKfg78PdRjbfCLPSHp_9ninSArMvoZihgZbDncayC4gtWmqw1lRuD_6watYoE-sJTck2IHER__0Vq9Z6-gkEpzuJk2Q3nh1L_lF5_fO3xyl2oHwrQTz0UHbBAi9Xlpty5OG62EYsb6Zro_rLukzLkL8Q-QZy3Tqiw_dvdG8G6Wenz-VPaTIZ1MJ2j3bSAgx-_O34UuNuIAyJqQIvHyH8ZBtnTHMISQ4RH8qosPeyvXDct3NaD37wdVKsHjg-h0tA1y-GGySbgSR7RQfsKTbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=oFiY4aKrssPjb0Fq0c0oAwlHynUtXqr_7viZ39hVjDiTL5VBWI_SThwOZoZQ3APNnFfU6yp7x7vKxxdR86nKYp5kBpB4QpjeyOeXbvj0_NN-nQepBkV6ONoG40m3RRliaNUA07vz1CEuvZc6cDKVVadxaeaLylJthyMP96i7YyV1OZQxrWCS3-UwPsg79Xs34bK82V6QnMPknrRr38N8CUT9QkFey5hEVrZl2uQYcJ3TM0Fl4pOfQ8htmcrIaO9yslygszmp5oXvTcCXz5cqanIrkanmb8zngch115pr3vyDFEghRUeYYgcdGRL-uZBYUUu04Lp81ivPFtoZCTwdkDEE9E3MNxu0_JYU7MLytHAxb9Wd37ml0WE4UJhXSjHjxTH7EG8QRgIkbL0Ji33B5yjZKfg78PdRjbfCLPSHp_9ninSArMvoZihgZbDncayC4gtWmqw1lRuD_6watYoE-sJTck2IHER__0Vq9Z6-gkEpzuJk2Q3nh1L_lF5_fO3xyl2oHwrQTz0UHbBAi9Xlpty5OG62EYsb6Zro_rLukzLkL8Q-QZy3Tqiw_dvdG8G6Wenz-VPaTIZ1MJ2j3bSAgx-_O34UuNuIAyJqQIvHyH8ZBtnTHMISQ4RH8qosPeyvXDct3NaD37wdVKsHjg-h0tA1y-GGySbgSR7RQfsKTbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=mD0V0OS61ejMqXUhFyyyF5hfmpnB-SgrCbC8Q8sK4WWLGTaLqUazYiYLr53_xD7ztbuIGKU6roLxwlvuAN3_h2R49FbQG7epJrvMt1Ra1lfUCQ3uTe98IoDr3H4ieukzONRl70rmdPlILf-R-bLk2lLAUrUPPotDBynxTZhTj1j5vYLd8Gy5_1oEwyttP0A7h1veTk5vL96jxW0sRxwUr-0gCmt66yjAU9IEifa3iLWfD5yjIpXwpxHcjq-DGBmsy9Cs7uXhOCHyF-6qsfY7KEGo7tnNRPuvvVRpgZjIHKAwSsa4pXSPt7kFc0b_hLH5VfXOMk7o0y0zgt1h0Zy2tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=mD0V0OS61ejMqXUhFyyyF5hfmpnB-SgrCbC8Q8sK4WWLGTaLqUazYiYLr53_xD7ztbuIGKU6roLxwlvuAN3_h2R49FbQG7epJrvMt1Ra1lfUCQ3uTe98IoDr3H4ieukzONRl70rmdPlILf-R-bLk2lLAUrUPPotDBynxTZhTj1j5vYLd8Gy5_1oEwyttP0A7h1veTk5vL96jxW0sRxwUr-0gCmt66yjAU9IEifa3iLWfD5yjIpXwpxHcjq-DGBmsy9Cs7uXhOCHyF-6qsfY7KEGo7tnNRPuvvVRpgZjIHKAwSsa4pXSPt7kFc0b_hLH5VfXOMk7o0y0zgt1h0Zy2tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-qhc-TcC21g2nLgyd6YkUrAW_Dj5izKrF9MokSELkzXRueUCv2VLqcs_SSeQ4-rEcBJHmoWoQDlquBUGNBdvCtFAF5UnIVyrNg6aQPNCsbdFUPyfdpTxpG4bdKMGHhyzqPE7qSrSYSxBVQ7WxA9T8uEiLMrYmTIbQC1WH_L5iJnsbvrsCY_TYALGKoREg7t75q5F3GKajedeAHkDGFyK-O87_I0BV7kLNIMk_3ugBUVaoRjwpgYWgn9aQJbRYhE1S-8prgrvnoDdxeo8OEryeEc70X0yQuv-tiUofY0x03CN4GmOmtdmFV7O6p-6kSPGolPRQlmkTKxpm28xWRbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=SrKYNl5M2MUI1pm87FuRBRZ5GnE4cza3pxZl5dr3btqXilUbDq2wM6oS4Cye6CSfy09_tTRH0qhy2Z-uwkjI8xwf2bkq-18JbGtZ1fm_kBlNlavSe5638_IyqY7-FLL9hTOvmj06RKthHM9wOCsQWxwJSuo_hTpG9RyStfgP3U5vk5SlxeJqnsQBTCHCQy60rH7p50sID_MSHBB3xaJ6zd6ulZZ1ACyKCorWhZdid5zEek8AaZLRYZPHjt6OZld-Wz35eeMikdadT4DSkOsyBkrh4BAPvk_r-UE6akrTryTTTgMx6tBtnCCnV6LUQiP2_JHvhalxigpbC6NdYQLUOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=SrKYNl5M2MUI1pm87FuRBRZ5GnE4cza3pxZl5dr3btqXilUbDq2wM6oS4Cye6CSfy09_tTRH0qhy2Z-uwkjI8xwf2bkq-18JbGtZ1fm_kBlNlavSe5638_IyqY7-FLL9hTOvmj06RKthHM9wOCsQWxwJSuo_hTpG9RyStfgP3U5vk5SlxeJqnsQBTCHCQy60rH7p50sID_MSHBB3xaJ6zd6ulZZ1ACyKCorWhZdid5zEek8AaZLRYZPHjt6OZld-Wz35eeMikdadT4DSkOsyBkrh4BAPvk_r-UE6akrTryTTTgMx6tBtnCCnV6LUQiP2_JHvhalxigpbC6NdYQLUOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVkus07TLAkjv5tew8d0FSNoagOIv4iFByx242kAeQ93MEayJt_AykcEfbp6_gNZlOfVj1bzh1VsefVwbgE795I86dGeiZNGVVMcZ_tBWqJCrovrPKfcKYE8jRhjgoXNZLNT7e5vVanT4Vdbf_PEuk9junvp1aCFI06a3ijo9IoBFZxRs0kLQnj8QshxfYfX2VYzCU4zESl3TqDGFUBgRIDMNMeeJDzPwmIWjNB9k__zkuFJHsTUAr_T1E-uVBz8y2TWsdeqku2TJq_PZu_giWKww3riuwmLC7P_uKsgVvk7mZ0W_DDv2-TF0-NmjOEMxhBvmzRCPCT58sGxC6cQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxRViGzgPIIgC62E29aRDaOwNs7JZZsVtn11_FlKUFZtCXB2QUPxWiaTmbHAgO2ZPuqCf17e2QA1-QrVER_AOIq44IaFthJ6LSpfeu3FR_m4aCYBMfG_oUDRiUbL0I4hRl7MRhSE0A3k4z1TK8tWLwYAK5om-GfkD4P4dJDggh5barTCLESEBoCtaf-aF2EYohunr69ppL00RX8u9VcLVZibDhCfmO6c7r5ATyJhunmSIpzo-zo-DaEEzw6DVAHS765rU-BR6ZDPkjBPKZjQnXR4Xq6Wv2OXc_K6y39-Hh_cNWFc-A_fItp5RtlXXInZ4zTBSt3yrZfSJ01izMwnDg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=AyN_2Taa5vT6gMSm_rVIQNp6GJv5qnfWWZz5Xb3AGa94oITukhfcx_vfeFpUaehzBnDihfH4B35OLDd2yt_oNujgk94xGuzFt2WRLapJXQ4ba5SZ-UQvlYsBlv2yxUbbfzU3JnyjUBRXW_-cVCvRVqSAgfdb2KeOgC7tCZCTLcJIggnkvW7VZpnhXKhpGtWzQMU-eiOuSnwd6JGMMtff5HynWk_hFy91JK271pMFFKMiuTcr5Fk4fYk3aBJldbxlR7Fuh-fKlVe-guo5FCUFnwChBZk9ygctpcNf15uvyqiW5z8riPAoS4KgMJtHm2u5-XLucWgig-hR0LDfna0CzJo9Wid2JYsuSOv0yuGDkGe6XgimEe5X3USY6UF9y4nHRX6M6f_DG2rxC6hvsnyIbaCUst1o1273dRrXYCPQ3Y4AO71cgSTjhvvSCcDOhjSllS-uzmJeaKs5WnjYFrA55l_KGeg0jURYUMqA-6BlPLNZOwOXC6jFQmPmL97oR8xW7K3LCBpDiQ94i_b4EVwnC3k9F9klh2-QyEFjuz8ipewQX0OzSmq482t6bugYccUJSmzkUYutdEO_fLX4GOowRo_xMu0RPO1jhYqtoC0gb8eeJ5mbPomslfO1mrXzYluAYIs4OMevYBJtFWmZEliWYPnL9wF2reCkeUOauMdR7ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=AyN_2Taa5vT6gMSm_rVIQNp6GJv5qnfWWZz5Xb3AGa94oITukhfcx_vfeFpUaehzBnDihfH4B35OLDd2yt_oNujgk94xGuzFt2WRLapJXQ4ba5SZ-UQvlYsBlv2yxUbbfzU3JnyjUBRXW_-cVCvRVqSAgfdb2KeOgC7tCZCTLcJIggnkvW7VZpnhXKhpGtWzQMU-eiOuSnwd6JGMMtff5HynWk_hFy91JK271pMFFKMiuTcr5Fk4fYk3aBJldbxlR7Fuh-fKlVe-guo5FCUFnwChBZk9ygctpcNf15uvyqiW5z8riPAoS4KgMJtHm2u5-XLucWgig-hR0LDfna0CzJo9Wid2JYsuSOv0yuGDkGe6XgimEe5X3USY6UF9y4nHRX6M6f_DG2rxC6hvsnyIbaCUst1o1273dRrXYCPQ3Y4AO71cgSTjhvvSCcDOhjSllS-uzmJeaKs5WnjYFrA55l_KGeg0jURYUMqA-6BlPLNZOwOXC6jFQmPmL97oR8xW7K3LCBpDiQ94i_b4EVwnC3k9F9klh2-QyEFjuz8ipewQX0OzSmq482t6bugYccUJSmzkUYutdEO_fLX4GOowRo_xMu0RPO1jhYqtoC0gb8eeJ5mbPomslfO1mrXzYluAYIs4OMevYBJtFWmZEliWYPnL9wF2reCkeUOauMdR7ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSvjznB1s-V7h6t_MMXymQJ2Ac1yBgdztjFI3dukiZxCo0rTG7PguTF3495-5pwoHn5LNUZM47leb6jh02y0g28c9mZ-X1qm11N-oG8QN390sjSU51ZkbSFcpNJmfEWINWTzm8pCyJcuolMJqiQ-3YkB1SGimJCdOQnPG319tR9mszIuT03jVuUBb4M65Z6DqXLTN2KsqXBwWnwPxKvYZ_Uc88QQ7rarNjU7h8Eirghe1sOhCEEVJTFGIq47oRMA5er6_sppWT-QQcxdRY3Lul5QtZw9OpA0PDwCisyx34xo-LZMfm1goPy26rKavYk4nGcCsKhzmoyoXMrS6FXn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvLmUp7tVNx9MT38IyL6o7BjAmmBFXX3OnDFMGMzmjUZynYUgHSP-A7Qlq-f-B7VfrVAm0TGdR_x703S6DXwDhtxkMIMFvo72k9iVrDLXFIrfaDkz6aBYzxmYiKakVXotqma62miiHnXyk094nC7cr_UM_26KUFl1j6N1UKHPiN57R6NCkT13a2m8uBzZFTOiIZUkbvxTou4scfKLlxO95rcvXbay3sv6j3JjOwXHl7msMhaKkQwNXrXIJfDiKx9v8cs_S8kqTPUDO-ydJMV3a-V9J9eJWRYgjC4464mcy9fO-CuAcT2K_6As_-xJj7YvX8k00OWShPDq3V0DHQ_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Nh4U2rUUrrzcp0cV9VaZRoSTkPXGJ-zyEqqQZL4neM8lhPPKAAdppthVamD4DAv4PZK8nD0DH1v5sBSUyJ2OU4Upx0nvwrZXchLJruj50hjs1tNUU0rSL2EadoXN-Nml5r_ZbTPIi74NMwug1UBXez0BeZk6B3hWu1rBtfvsMpAOHiIBHMJ8w4cC0SKkBHBGBF1nPx4GAVcUkmf2sa1BPvLhQ7nTOTpYc_Aodx7vJv-Xg78EbBJyhljW8IuLqZROO9OFcif2lV2Qpb5PoMo7sIsEvamp3SUcptKr-a1tHB-VqTUMtecUnbha9omN1n1mJFhaaEvBp8Z-SSv-VOSDxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Nh4U2rUUrrzcp0cV9VaZRoSTkPXGJ-zyEqqQZL4neM8lhPPKAAdppthVamD4DAv4PZK8nD0DH1v5sBSUyJ2OU4Upx0nvwrZXchLJruj50hjs1tNUU0rSL2EadoXN-Nml5r_ZbTPIi74NMwug1UBXez0BeZk6B3hWu1rBtfvsMpAOHiIBHMJ8w4cC0SKkBHBGBF1nPx4GAVcUkmf2sa1BPvLhQ7nTOTpYc_Aodx7vJv-Xg78EbBJyhljW8IuLqZROO9OFcif2lV2Qpb5PoMo7sIsEvamp3SUcptKr-a1tHB-VqTUMtecUnbha9omN1n1mJFhaaEvBp8Z-SSv-VOSDxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=OKFOiUOtUFIJJ6sf2k_t-_kUj5nWzuT4InrfbLfAqm1oT6yVcOq9yjX4risqrDopdq4HdQNHm39l2uXMOOSmHjeTUdGIuDLUCCT58s31nD4buanciF-OESw5eVDSoqd9-E35HUaceRBgCdjyPNjoZIwIDyUH612ddGSLwx17aMErQQNPQNMsYZyCcuASdtPDVweLMnZLWcU2HqYE0V1d7-X-RSMsoV0vTvWh-J_LfZVojK3taNKB8t6brjDFWKq77RXuKe97fNDsftnBhh5a7bKn1cO_euMhMItozUaSSuPnzZY4mR_VDJBrbxHBG-agSrKolvp5z2v4BoiK7AOyPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=OKFOiUOtUFIJJ6sf2k_t-_kUj5nWzuT4InrfbLfAqm1oT6yVcOq9yjX4risqrDopdq4HdQNHm39l2uXMOOSmHjeTUdGIuDLUCCT58s31nD4buanciF-OESw5eVDSoqd9-E35HUaceRBgCdjyPNjoZIwIDyUH612ddGSLwx17aMErQQNPQNMsYZyCcuASdtPDVweLMnZLWcU2HqYE0V1d7-X-RSMsoV0vTvWh-J_LfZVojK3taNKB8t6brjDFWKq77RXuKe97fNDsftnBhh5a7bKn1cO_euMhMItozUaSSuPnzZY4mR_VDJBrbxHBG-agSrKolvp5z2v4BoiK7AOyPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=GkDj3Kz-iIIC49_y9oqA8wJ2mxkm_cUjgypXSHOxZ50hdnG1fDcIlu37rOa92YOMYZjEtgFy7Ng2VTLOzCW7qYZ5R9RZsQ-hhoay5EqxXnXa9ivq6uZRuhjTMhcXNpwFE4fC3KFiFIdrnhWNfFcJDPN6AK6JAQtYX9Ka5hLcSMDXK9FONNEZZIWOLacS9loRaaY3BpqrhvgvrBQDx_3UQ58zD1nfymV87rcukAZNchLw9z9Fui9WcStRQsNOFeQfHM8n4VqL3aGklsmlPeTFxUpnY5xcVJPwfAHdHuUnx0lDork-9KxHt-WtEElxPDcbPpDikTnjtNes9no6IuORFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=GkDj3Kz-iIIC49_y9oqA8wJ2mxkm_cUjgypXSHOxZ50hdnG1fDcIlu37rOa92YOMYZjEtgFy7Ng2VTLOzCW7qYZ5R9RZsQ-hhoay5EqxXnXa9ivq6uZRuhjTMhcXNpwFE4fC3KFiFIdrnhWNfFcJDPN6AK6JAQtYX9Ka5hLcSMDXK9FONNEZZIWOLacS9loRaaY3BpqrhvgvrBQDx_3UQ58zD1nfymV87rcukAZNchLw9z9Fui9WcStRQsNOFeQfHM8n4VqL3aGklsmlPeTFxUpnY5xcVJPwfAHdHuUnx0lDork-9KxHt-WtEElxPDcbPpDikTnjtNes9no6IuORFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7RZOZiU_PcLP97-XKiXMgpoRsP12-1ylqviJ86lrkzJh14BUvJq1dMEu5aQCvVvRCOsv7ESXMKwbDUM02zMdzbA29tfhJuzl1I2kVI3YaFitzdienNE-87QQ2DaNWg4K7KvRcmcS5kaR3BIQ4OvCaqAGqLTPx-KweJefLapcUVov2o7tdNjRVXavqHu844KwMIfBOdzkefTQ-DNkDprF4CH54zP1SPfiifyiJ_e8aN8VUes1ZUzA7jKxLxOsG_JsunR6MYRPzw4RxczXHk1cc5nEptqd0AU0Oiymq6EsYmr_n36ojZAMlxUwfP7mf24Mm41vVWS4prdh0kscu_yYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DeuvilNrvHkCoVfhTBJorfwfleRprhvo1ogc1AfjNtqi5hkpvMDA3uHZSEtXh6Udd3ztlpKpI-mBsmQJTBIxHj_g2aQWba2QEvV3fYafpzOf65JgpJgUfkNV4bV2FYjhWTAukdMhXRwIX9ocrssJPJu-c_Q4HoALaNsw48YhLm3Hi0LZaWTPjJ571EagaLEaLHyOPMaQNy_CIE_7dA6dnCfhhVqpEgbsI1rkt5eQzboD14RHvUDzTg0pTSUufvBTba2ax8k8FEjY_zZuwt_TZWu94PVu1HF6Xn2npFI__n34ybt4IeNLBVHHndsln7ffnnmO8q-2o6hjD4awhHfLoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DeuvilNrvHkCoVfhTBJorfwfleRprhvo1ogc1AfjNtqi5hkpvMDA3uHZSEtXh6Udd3ztlpKpI-mBsmQJTBIxHj_g2aQWba2QEvV3fYafpzOf65JgpJgUfkNV4bV2FYjhWTAukdMhXRwIX9ocrssJPJu-c_Q4HoALaNsw48YhLm3Hi0LZaWTPjJ571EagaLEaLHyOPMaQNy_CIE_7dA6dnCfhhVqpEgbsI1rkt5eQzboD14RHvUDzTg0pTSUufvBTba2ax8k8FEjY_zZuwt_TZWu94PVu1HF6Xn2npFI__n34ybt4IeNLBVHHndsln7ffnnmO8q-2o6hjD4awhHfLoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QMpsuRk97s9lr9uGO8R6oee9aC4ExOTxoSEHuCM8dzq_tdyY7oLgantlhANRwJ_k3BQutgYx41uu1dP6s8_1Jz3s22U-shaUNhQVWylpj-WxdxFB7-JxYGr_bGNX9hwXrqP2wa-dDKHI10pJMg6cMdKOY5fxhfg1i6SUPkayexLDEmBqKOV7csH06PyUPtNBFskFg0V7ZkLGz6uRw1qo-_Gv_Mb-ugXMc-s58PUbF3KIGpeuvRvi5_twjMb7pQEfnV30CZtlznB-3yeVzosiLyIBuDZmulu1SGoUFJlhxHpSD1mdH3Wiu3Rvximi6paf8ATTOc10BnV7f4E7b6OjgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QMpsuRk97s9lr9uGO8R6oee9aC4ExOTxoSEHuCM8dzq_tdyY7oLgantlhANRwJ_k3BQutgYx41uu1dP6s8_1Jz3s22U-shaUNhQVWylpj-WxdxFB7-JxYGr_bGNX9hwXrqP2wa-dDKHI10pJMg6cMdKOY5fxhfg1i6SUPkayexLDEmBqKOV7csH06PyUPtNBFskFg0V7ZkLGz6uRw1qo-_Gv_Mb-ugXMc-s58PUbF3KIGpeuvRvi5_twjMb7pQEfnV30CZtlznB-3yeVzosiLyIBuDZmulu1SGoUFJlhxHpSD1mdH3Wiu3Rvximi6paf8ATTOc10BnV7f4E7b6OjgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teE_Lg5UQEgGYJHjJ5Df5U5pOJhURECQBW_0K1lOUObZK7ypd4bo5BbEv0P-G33Vaotido9U94yeyHLYGuQk_wORedLxC9V2KQjyj9J1ZUMPEwdG9sjDYa6dCRARnaA6Udmf5mQP2uOgUl-jdYrzfPgR48x9vVGmU9Mc6jpRnQj-iEyGKyR_-AKAudTbz2yM2cDlGpNCOJGSggMGhTj4PSDo2vggv5a6XnHKgRnZNw-BvtWU72q0C42o2acIqh_XHqiXymzVfmEXbU7kEl7ytGgREY7YS3kPpDF3wiiwD1i69BAJy2KkTRR6FgSHYUV_Ldp6mR1VLehsKBCH-WGbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=hBaDkF2bm1_D3yNtXzMzzs1N3CweP-Z1uKq070SKbj0WYvrFZ7Y5A6GX9hN2UoaocrFhCLoxvF34mt023heh1HQdZXmu3yHCQoIfZ-Sk_nK4iRh7HXV8hgsUFqG7cK4Ut5ZAcMR3CCqRNJrhrbeMsxh3f9lIRkFRGMI4wAXH1jfxR4k--N6luhzMLY_Sdfbh8wSWU8U8KapYJB75KspRcsdlKrcMDwaoH_AnWkf8gJW4qbN-SZdTGJaLI81SkLePcSqft5aE6Gr6ifK-rzc8YN8b9HPk6w9UyvzK9633IRFukDGXeGlXUX7E4JVGa7bXyxULDC2SMajlrfYfH8YJR7rmr3weYIeGNNLdKTjZXL8bcH8-paICbdsvsJEEuV5sqsd8V25hWq3zx2QCDb7zOoN93wfCvk0d1JtoGj1gK98fwe2XJS5UfJDq9KPmKPPS6Vz5CLTMSHvjbLTyq1WR7R0GE05QyQPFnSIppAMdFLbTMyefOk5WLRkP_94UGZSGkng04FUWiTrypcr8mVVs1VZuDYyrJT4OgtyWPn69NcA7hnohXy0haWfARk8MSKZG_Y5bnASmEI1oIP-cq7yt3YjXe2yxhbo5Xibzpjbu-M0izFhw1fn0vQZltUheCENdKBg_fo809uvwjZjwgQuEBuB_bKR59VErpheCVjdx-v8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=hBaDkF2bm1_D3yNtXzMzzs1N3CweP-Z1uKq070SKbj0WYvrFZ7Y5A6GX9hN2UoaocrFhCLoxvF34mt023heh1HQdZXmu3yHCQoIfZ-Sk_nK4iRh7HXV8hgsUFqG7cK4Ut5ZAcMR3CCqRNJrhrbeMsxh3f9lIRkFRGMI4wAXH1jfxR4k--N6luhzMLY_Sdfbh8wSWU8U8KapYJB75KspRcsdlKrcMDwaoH_AnWkf8gJW4qbN-SZdTGJaLI81SkLePcSqft5aE6Gr6ifK-rzc8YN8b9HPk6w9UyvzK9633IRFukDGXeGlXUX7E4JVGa7bXyxULDC2SMajlrfYfH8YJR7rmr3weYIeGNNLdKTjZXL8bcH8-paICbdsvsJEEuV5sqsd8V25hWq3zx2QCDb7zOoN93wfCvk0d1JtoGj1gK98fwe2XJS5UfJDq9KPmKPPS6Vz5CLTMSHvjbLTyq1WR7R0GE05QyQPFnSIppAMdFLbTMyefOk5WLRkP_94UGZSGkng04FUWiTrypcr8mVVs1VZuDYyrJT4OgtyWPn69NcA7hnohXy0haWfARk8MSKZG_Y5bnASmEI1oIP-cq7yt3YjXe2yxhbo5Xibzpjbu-M0izFhw1fn0vQZltUheCENdKBg_fo809uvwjZjwgQuEBuB_bKR59VErpheCVjdx-v8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cthdH6sCvVH8dhKZ-oP_KMj9V6CAhRbg4CkPxQ8jDa35PK8eYI7rZKhb1Dw-73upnLXqo1igMb5f2MssIZTkPi_fonDJymfjWTBo2d1A16bfcSX7D_yGqyRTTnCLHfLihepeFTT1KkihLos95_TqqSb-Yz7HamBQeHlX30cyDzcVNIz9FOGyf0IubtwBUjf540XnexoCOghvX9o2qSS6232l_N2PmJKiEZ0FgInY3xMHW_xxe8fAOPtlMoRb_E7LxzXvLxPrOyoywuOUhLdb0y6Pw5ZB-x8_8Savaw7BmwPRt3hNclf9jzKiPLq422vLeXCPdRq5BgQiM0nCeQkjuA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ObQfwWlLx3g-DDSJJcYLeTJ-zPQwym9I9-1xnVep7UQmw3ivIc5azyA3isLsn1qFgpP2Newvnud6kkqoBMTaHQwlFXkvEtRpQWawItSy0-UO0vi73jnpcy80yAkoZ1YGcv2_1RBpQH7aHCbDJxzCI5jmxKyIJXD6Hx3Svo4J2lIKnw0VaxD-6hYux29_rV_eqUq4SqO-Qt4FqK4WDY2HcsEH2-Qbi-xKXKUMT3QcnWP4HFEhNa2q8QucOmSZszgLy34NxeWMzcTPcKZGwAmlvFTA0YkqsXMVP_NEDGrGkZ_P1mUflWV-IRNQiv1xZ0ZBIfVQrXWwa6LVcln4BkwNeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ObQfwWlLx3g-DDSJJcYLeTJ-zPQwym9I9-1xnVep7UQmw3ivIc5azyA3isLsn1qFgpP2Newvnud6kkqoBMTaHQwlFXkvEtRpQWawItSy0-UO0vi73jnpcy80yAkoZ1YGcv2_1RBpQH7aHCbDJxzCI5jmxKyIJXD6Hx3Svo4J2lIKnw0VaxD-6hYux29_rV_eqUq4SqO-Qt4FqK4WDY2HcsEH2-Qbi-xKXKUMT3QcnWP4HFEhNa2q8QucOmSZszgLy34NxeWMzcTPcKZGwAmlvFTA0YkqsXMVP_NEDGrGkZ_P1mUflWV-IRNQiv1xZ0ZBIfVQrXWwa6LVcln4BkwNeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHiCsjb9yr0V4xCXvGzwU_UF2TFlRZZJgrOV9bf2jGtyw3FZGj0k_IE7tekj8qs8MKH0GSv6MYHcU-DA4FdqBKSRpCB2suZLikyvppdNH2joXZNKGfPnW3TmETwUKQCDLXtEasOsW3Dh-tuF3FYNlE0lxf0E0WT3HvHHq70HeZqlXjY5au4d9sUl3BOtB_nDjtdn5lshG-CVudrkpKdti7r4y0Ad7B_Hmi1PK8Tjle_MwPpovEYhfYksbmH8nIPdrr3CmnHT1eqhTEWGBZ-4AuE3ITburvP8GIrLnWy3LYdrwo2ZZDvlaGqiRqscBsnJssTX17WZ9qWEsEGgDw64pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM3fHUL69ZujckF6t9zMB_LUvEgFOIX9CI8T-BXQnX4yHXzlMpaxS_PDVRzCVFi32jygE-1lo6JRLihimzFCNhAJYyudZtPZav1jFokEWOBEf3m2NeCmaGwCnmpupzDOpkiCGHMMbZiODB12TJv9RAq_V8UCTx9oulQF6h1XplqTyvIuAvkcWxbZuq6sME7msj9wcHtPXCmOThqplcSnNKiyg6YUEisqjxxwXHcCZ3gMwfXYbi6TZ0Um19w3MulP4Iop314HV2GTVRQ0Bta7ybGj4uIgV5G4DEFYv9QzFjINJS9rGuzhAYpKWYrvK5F62lnMPMD3j8Xti8aI0V-DuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDYopq3A7ySLAD-Cy_I1akS6Xwa9ybfGpbsf4OxwMhi7U08V5MwhGI7O30QQkKVGpfYmsAoDRqQTSnJy0nQ-VuSlzl3_e1QXfRjPAly04FLxhssCfQksBvH6JQwwBwWGHB-1-8gT7g8eChOuc7-qxC6XH0UKzspNDQKrpY2lNreC8rah25CgoPgew4oSc82Dx3x7Yracc5vgStP-R6yGdw0nmllb8L8jqv_KjoA8AaKTyTq2G8LU_SQzetR_cc2FMhV_xGDCuExBwX76M3nRyEUix5sPd0NvX3VVgrEtHEpl-llnszGMa0t0Crj-K0PTcP0wHhIY8rwnO2ozcPlVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=M5Dx3CKkJUgTcb8OZyS4CvZHtcIf7YLQP35ZlWndpPAllfXf2VocfxIKkmofGp9gfVXHJ5M_UW8XaeAVzuI_cJ8SS4OJtXT1v00LydCcEiqHLG3yqxJvKwLITnXHwobXIXOjDqsrA26T0uenBWKWh2MQdfIjMqiTfCCdA-tNJ60oB0rgkIAUbLRQyFj5aoXb_STbpbw_g4tuSv1AQbi0-265h5SYBesuZeH6jIfBq8q0HrIrDHwGx6NJHIsYlnmfhUCOowWGonxznc4FqleS1jn5mTBccjJqd03r2Idsi0T5UqtofpcstWfRvKPEqphXMntrjCV8QAXxm7VBv4Faww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=M5Dx3CKkJUgTcb8OZyS4CvZHtcIf7YLQP35ZlWndpPAllfXf2VocfxIKkmofGp9gfVXHJ5M_UW8XaeAVzuI_cJ8SS4OJtXT1v00LydCcEiqHLG3yqxJvKwLITnXHwobXIXOjDqsrA26T0uenBWKWh2MQdfIjMqiTfCCdA-tNJ60oB0rgkIAUbLRQyFj5aoXb_STbpbw_g4tuSv1AQbi0-265h5SYBesuZeH6jIfBq8q0HrIrDHwGx6NJHIsYlnmfhUCOowWGonxznc4FqleS1jn5mTBccjJqd03r2Idsi0T5UqtofpcstWfRvKPEqphXMntrjCV8QAXxm7VBv4Faww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2wPF71O8i_E78WcsodYoZ813YgVW8-dRO1AikLod5atrc7PfhkR_uigJzFVbDey7-U4PMOlsuKnkM0mlbh0MRLo8KsYN7_iRpYAmNpkYgMyXl_mmzP95QFnZD4vxWuJ_tuCL5zZwiNTQivW1iIzBYWBgyce8kdIRrvKflmcCjj28sj0EAOf-9OQWP3db52xnVTAeyIvTirbAfKnqwWn5N4WxsGb_4HJreYVcY3W7zAhL1suBqDtT2TlwgUmnzN5y14Ck6t8q7Ybs2ohoDReAQoOAvj9Ds4xLYrHWt9kILRcQqVb29MZE0kSec_WYEhfr2EX9iZfYh3fLFXBvoC-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFI7Dd51WzzvB0Qpy0D5OM3Sr8bIas9e4YJO2gto39Np_F6EsZf3hq2Ja3Ty_ePUFOrPUpAUGHssfZFUYJFEDhb1X4qBI9NOMzdjYO2tocR2zpHSjdPPjwm_e_DwjPQvFdV-bMI-iUacOog3-ZQwWpeR_2dK1_DhF15bydN1EW7zkNueynn90KNefesVYRCVF73Oep5hb3uXdMPiul9SOkPdhHBCNMFGkmI6WZ-W4onZHX_1d9DmYLaVaXKKsCOCIcR3XYzX6li4a0l2-_XYLlF-HrQFEaNhayZHlrNCS__LsikRFEuadkAO57wL3yEg8DF9EPBRbiAyvuThcO1l4Gvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFI7Dd51WzzvB0Qpy0D5OM3Sr8bIas9e4YJO2gto39Np_F6EsZf3hq2Ja3Ty_ePUFOrPUpAUGHssfZFUYJFEDhb1X4qBI9NOMzdjYO2tocR2zpHSjdPPjwm_e_DwjPQvFdV-bMI-iUacOog3-ZQwWpeR_2dK1_DhF15bydN1EW7zkNueynn90KNefesVYRCVF73Oep5hb3uXdMPiul9SOkPdhHBCNMFGkmI6WZ-W4onZHX_1d9DmYLaVaXKKsCOCIcR3XYzX6li4a0l2-_XYLlF-HrQFEaNhayZHlrNCS__LsikRFEuadkAO57wL3yEg8DF9EPBRbiAyvuThcO1l4Gvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Kj1TSggP8eJEV9y2o7538OU0kMeGTCo0Yo1cn9u6oFl2BKnpEqn4IdaU1DpmzZ4WC5Ib1mV5I_PMsvp9tHgpjlvUJqBQEgq8WpDMdSvIS0DspANb14JtyddNIF10c12ZLnSVU-MZTuMwnAuGFHn1St5n3vhnGlqGMcj88gH40tNaK-kGZKQ6xJvOIyOTIBvdBlsFhjXOaSRIC-2AzKPxnM_BHh_BshjyFQaqIQBOWRGG2u0vfy_QZFbDpRM1pqQZ12gSCAFvgKTXVlS0LURw-PXi6KUDM0zChqvVmDAdddqho1peCGp6m6q8goSDxYdQhxUGZl8i6ssym5yPIg54tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Kj1TSggP8eJEV9y2o7538OU0kMeGTCo0Yo1cn9u6oFl2BKnpEqn4IdaU1DpmzZ4WC5Ib1mV5I_PMsvp9tHgpjlvUJqBQEgq8WpDMdSvIS0DspANb14JtyddNIF10c12ZLnSVU-MZTuMwnAuGFHn1St5n3vhnGlqGMcj88gH40tNaK-kGZKQ6xJvOIyOTIBvdBlsFhjXOaSRIC-2AzKPxnM_BHh_BshjyFQaqIQBOWRGG2u0vfy_QZFbDpRM1pqQZ12gSCAFvgKTXVlS0LURw-PXi6KUDM0zChqvVmDAdddqho1peCGp6m6q8goSDxYdQhxUGZl8i6ssym5yPIg54tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=MjQxD-diDuPmsovHKVEznLdg3bBYvU7-oEOglD-LnMocyCRi-oWY5DabijDwM6bZlj11AG1quW1MAuwuFueKh1ghpeHfmHZPruHp0cX_7aPClo3SaqfZ6z-f4mp2SCIVCiixkyt_r8a4DqxhzGBAzLrP-9ISRWRVkl0Fyc-irq8gpFe_8UQiUGgazKnm9BasDHBbxOBBizaJXNeEltN9lOmteClQIK1yf8dtRl4F9ivGjsADmQMvWiA9m6CwEUOfYyOEPXz87px3znlG7uyuldDqLU0jpGAbEjCrtZyYAzugBTZnC1PaniA6d21ocFxWS8kCw5kBG75B6IUZcsOAlmxk_wBZ_QtN0PWMSduVadDxcwfM7ckX_Tc9fCO5qNTLJGxyERpngS4n4qacHobRP_Tjsb2MZfvpoTsiGcYBJCR3OmK06KoXy8q7T0IzxlFU0IJz14QvUgqHB34z_joH6TvXka03D5J8Cxj_YtEbuamZBl1c4Lt1YstIXUSOckdfbmsbkPpBcUT60ZlB19V9S1gWv8cZ31SWgBz4Iqk1Ttz82Q41FPtE-o3MSG2RkopUQ_8p2sgulVWwGeRRnuZBnAhhx8dX7lKVEyg-Yzo9DdMeDgRgcBsw14c0Y485LhT-uvAR-84f28-7MQS4IRs0wPM2EO_5sgWDdFcAhRJj5s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=MjQxD-diDuPmsovHKVEznLdg3bBYvU7-oEOglD-LnMocyCRi-oWY5DabijDwM6bZlj11AG1quW1MAuwuFueKh1ghpeHfmHZPruHp0cX_7aPClo3SaqfZ6z-f4mp2SCIVCiixkyt_r8a4DqxhzGBAzLrP-9ISRWRVkl0Fyc-irq8gpFe_8UQiUGgazKnm9BasDHBbxOBBizaJXNeEltN9lOmteClQIK1yf8dtRl4F9ivGjsADmQMvWiA9m6CwEUOfYyOEPXz87px3znlG7uyuldDqLU0jpGAbEjCrtZyYAzugBTZnC1PaniA6d21ocFxWS8kCw5kBG75B6IUZcsOAlmxk_wBZ_QtN0PWMSduVadDxcwfM7ckX_Tc9fCO5qNTLJGxyERpngS4n4qacHobRP_Tjsb2MZfvpoTsiGcYBJCR3OmK06KoXy8q7T0IzxlFU0IJz14QvUgqHB34z_joH6TvXka03D5J8Cxj_YtEbuamZBl1c4Lt1YstIXUSOckdfbmsbkPpBcUT60ZlB19V9S1gWv8cZ31SWgBz4Iqk1Ttz82Q41FPtE-o3MSG2RkopUQ_8p2sgulVWwGeRRnuZBnAhhx8dX7lKVEyg-Yzo9DdMeDgRgcBsw14c0Y485LhT-uvAR-84f28-7MQS4IRs0wPM2EO_5sgWDdFcAhRJj5s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=c1w2AAi1TeCMFZOtuub0e6-1lkdDOSJm7-SQKTDKbEdkQ5xm2yCYWdyofRO8NsqwvMoE_B5-3XDWDnXxvfX1f7ZHlOYC1JGWEjlakFHtnfFkpa5O06QuHbrmZAhGfT8H4Ud_QtU6jeDowcZS6S14R1EzpyDpifBAbla3JaTzOUWZXM6Bi_7bYrvRaWxJlygbISFe2mv7z3sr-dQ4wauP3iAWfZWeJfX6jz6AZANeIrIciT4IIlIpheHkBqoR435xOdB7KrDzV5eea5Iq41_FllI2k9HMaPbKtXm0v_e-YyHJVbleUFmdORPoFRoU42Y81zoWFs_CDLoVvOiqN2MslQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=c1w2AAi1TeCMFZOtuub0e6-1lkdDOSJm7-SQKTDKbEdkQ5xm2yCYWdyofRO8NsqwvMoE_B5-3XDWDnXxvfX1f7ZHlOYC1JGWEjlakFHtnfFkpa5O06QuHbrmZAhGfT8H4Ud_QtU6jeDowcZS6S14R1EzpyDpifBAbla3JaTzOUWZXM6Bi_7bYrvRaWxJlygbISFe2mv7z3sr-dQ4wauP3iAWfZWeJfX6jz6AZANeIrIciT4IIlIpheHkBqoR435xOdB7KrDzV5eea5Iq41_FllI2k9HMaPbKtXm0v_e-YyHJVbleUFmdORPoFRoU42Y81zoWFs_CDLoVvOiqN2MslQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfaprHreRt5vOOxHjHfVy5OR65NlT8jfzvdyn2sUzJ8W2u3nPW3o-mLQ17rj0I5icTC4vpG4CZoCI1pQsi5R5piVU5MRjbIh5An6IThL85F2GxPyqJWHT1E_ISUgSY5r-n0YAx6t-THwa8Ft-W7IIaV4d5KO3u8dB2rHNIwUTAMT64aCKj6CDvs8q8gwgNyQPmKosGYsBu46cdxwhZxhUP8WcBUasxEd5eF7ZflfC8sxm0k5sE2TBM56beyhDv_Yaoijd6XyClaMRw-LYofVpvtoZ_ajgrWBdCYZBsGLjcwnZLuV53ajbgpesYDZUq2EAwi5GZUg-xua4Y9Au7A4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Wq-fqZH3xz3mwR-ZEnyCpp-vyq3Xv1eLgKfXnROhF09V7X329a1zXDgux0Xd9I_Bfju30SoZsiIwLBK3xfSqkybju1rlqjVeQZfxMAWv2E_eBYGJ055hsM4pBS3i3zT4aPKx5CZuY2CRz1ImcKiKobjYnb8KhP3xHj0AUJSUz4F0M2ePTfJZ75TawL7UgzgkyylbmwauRFuAWkufCbP9YYdn7y_6e022UOICOTaMnFOnOs238eKMNYqrHjFAyHL7s2Mhp583jBVj_pv7d-J1yWcUheAgeYzyCGbxTaYT5dDnf7TPw3excOKsjwjW5LBeu8MHCHQ8ceH5R7Ge0um_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Wq-fqZH3xz3mwR-ZEnyCpp-vyq3Xv1eLgKfXnROhF09V7X329a1zXDgux0Xd9I_Bfju30SoZsiIwLBK3xfSqkybju1rlqjVeQZfxMAWv2E_eBYGJ055hsM4pBS3i3zT4aPKx5CZuY2CRz1ImcKiKobjYnb8KhP3xHj0AUJSUz4F0M2ePTfJZ75TawL7UgzgkyylbmwauRFuAWkufCbP9YYdn7y_6e022UOICOTaMnFOnOs238eKMNYqrHjFAyHL7s2Mhp583jBVj_pv7d-J1yWcUheAgeYzyCGbxTaYT5dDnf7TPw3excOKsjwjW5LBeu8MHCHQ8ceH5R7Ge0um_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=aSwTYevswB3IppyJAM2AkJ9nOM7mT8q5FfbuvLJj46stKRGvuPXn7ZTGADjB0yoyK1UhBPr54JU7nuZ2S386uZrrtHwHJZ6uHjCr1CeRmiXArsynJhPZ3n1A7EqiV52ZpM1_wZzQ5bOWJRR1Srmcov7lUsjxpB7aldKkqU6vBupDvh9Z5dHze7H7astAQ_VcMPGRIDjyTIrYplxh3cw_qs9a9i64mUkX34Wh80TT7C1CD7bwKSk9N0MEKKe_XTe_Vh31tCC5-Kp-HHo7jkFlEmfNyoNl0fu2M0VyiXqzjJxPnz9zOwqfVusIKABuMVzd92sWwvTJIF4zqQkZJ2MrkImZcWpMy_82Rmkr9euQGrjkQKuDwhfwTBLrz7xszsgMSww6LKcmsV1KyQzk53roRokDOP1DiAbhiAfuhbnw-1jOictX_Bdej26j_GbzJsWwt6dswfHoDDd2O3WmzKHLK3i5ZQ42BeOkYoSkidwLVyDdGPJW2WOpSn-94KeqZQLFZgST_dW3eZBnNC-BqqXGichiLvqKNeFz_ONgecHlG69qDqVpXIsD_U9kSq_Znfdnz73ZV5ll9QfpcS6AVyk-wJsk5BkTLwP8xOPoFee3rEI0pTH2X7MYrZWhh1cVlVpWQ5w2Fxr30pQF3PMHihes08PSv9HG1JB6lm_-CqKpe_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=aSwTYevswB3IppyJAM2AkJ9nOM7mT8q5FfbuvLJj46stKRGvuPXn7ZTGADjB0yoyK1UhBPr54JU7nuZ2S386uZrrtHwHJZ6uHjCr1CeRmiXArsynJhPZ3n1A7EqiV52ZpM1_wZzQ5bOWJRR1Srmcov7lUsjxpB7aldKkqU6vBupDvh9Z5dHze7H7astAQ_VcMPGRIDjyTIrYplxh3cw_qs9a9i64mUkX34Wh80TT7C1CD7bwKSk9N0MEKKe_XTe_Vh31tCC5-Kp-HHo7jkFlEmfNyoNl0fu2M0VyiXqzjJxPnz9zOwqfVusIKABuMVzd92sWwvTJIF4zqQkZJ2MrkImZcWpMy_82Rmkr9euQGrjkQKuDwhfwTBLrz7xszsgMSww6LKcmsV1KyQzk53roRokDOP1DiAbhiAfuhbnw-1jOictX_Bdej26j_GbzJsWwt6dswfHoDDd2O3WmzKHLK3i5ZQ42BeOkYoSkidwLVyDdGPJW2WOpSn-94KeqZQLFZgST_dW3eZBnNC-BqqXGichiLvqKNeFz_ONgecHlG69qDqVpXIsD_U9kSq_Znfdnz73ZV5ll9QfpcS6AVyk-wJsk5BkTLwP8xOPoFee3rEI0pTH2X7MYrZWhh1cVlVpWQ5w2Fxr30pQF3PMHihes08PSv9HG1JB6lm_-CqKpe_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0ZeqH9GeWRZ6RbpiF2LWBQ7wElrBDwz7JMa10vlwn7cd0y1KcPlW0KIgPRJOFHQ82AAahSo9dWngvM9sWIVe0LmoY9-hmEbl3I1I2aOYAp5RTHCr8RernskVyk-wdsxz6LzDNvNySXqw5v29b13TLHd0HEPBg0CsCXmwcn1YMBtKS-fYdOWY_szabUpY1b8q2wxeHQBm4u-AvjXfN50iC24gFGtK4foxeBOtqDarwraC-MZt2V4FhRdOHVmVKY_JkxmVkRRLsThJXQbnRB_0MKvZaLrg550yS1d2uNfyTJCGhda_xJ7WYK1Bg7Qhtyy8DsnsC77mU_Lo2r97DF-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=q7pyKzqUPL2U7Acss5__kxEvEGusyNHTnRbXhDWOD3HxiHZ4vFhQEmml86mxE9Cd-bsoQrPCcRpvJd2F-xBC-eR-L2tRpAP_Euff07P0T9DxUHWLFLdVasNajHSi0MRtsue-OAVIyTlqUOWDaNp0t2XpLseuRYxKnB5B2dMVhlU8RPs8RGb1KLR69l7TllfL0ah3HaWQO6IXBEVR6X9XHitv9RmxhhyGWor0kvhKoHXgx9T3zDnSiNOCJzsULmPzK6rfewvo2KGLyl5BBIw-9ak2yUF0vc52lB-wQjBVMrsvg7iHPAWxFu_YbrtvZJx1vmbPr4PUjGsU0PCkdyzj7gagHBo1hpV-ZPAL6-qM5WkyAH_kzXZO3TAFP4AWJ_Z4OkRv5rh7ZTjS-TGqIC9qztY8tXnpFe7Nb8gFSFKpqKB0xkPcrd5z894OSML-KMJd11qtuvjwnEEcOlz4zzg9K_DC5OwLBR64lruZ6sss7-ulq6QUmn4_aCmJQGhgNsfGNe5qLh1GxOEjlDgFvgEDb8O1aO4Bv2CEgIwGW80uBhZLfLMY2aCgDjB7KhFXJuNW0dMC3w8iwIHcC-NtHdlBODocWEZI8rTGke6neRstO-IcXbIi5aHpENOF4KjDJOqeHVq3YngktDoRep_9xjJ1GYJAg11fVccvS-UzIKrJbAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=q7pyKzqUPL2U7Acss5__kxEvEGusyNHTnRbXhDWOD3HxiHZ4vFhQEmml86mxE9Cd-bsoQrPCcRpvJd2F-xBC-eR-L2tRpAP_Euff07P0T9DxUHWLFLdVasNajHSi0MRtsue-OAVIyTlqUOWDaNp0t2XpLseuRYxKnB5B2dMVhlU8RPs8RGb1KLR69l7TllfL0ah3HaWQO6IXBEVR6X9XHitv9RmxhhyGWor0kvhKoHXgx9T3zDnSiNOCJzsULmPzK6rfewvo2KGLyl5BBIw-9ak2yUF0vc52lB-wQjBVMrsvg7iHPAWxFu_YbrtvZJx1vmbPr4PUjGsU0PCkdyzj7gagHBo1hpV-ZPAL6-qM5WkyAH_kzXZO3TAFP4AWJ_Z4OkRv5rh7ZTjS-TGqIC9qztY8tXnpFe7Nb8gFSFKpqKB0xkPcrd5z894OSML-KMJd11qtuvjwnEEcOlz4zzg9K_DC5OwLBR64lruZ6sss7-ulq6QUmn4_aCmJQGhgNsfGNe5qLh1GxOEjlDgFvgEDb8O1aO4Bv2CEgIwGW80uBhZLfLMY2aCgDjB7KhFXJuNW0dMC3w8iwIHcC-NtHdlBODocWEZI8rTGke6neRstO-IcXbIi5aHpENOF4KjDJOqeHVq3YngktDoRep_9xjJ1GYJAg11fVccvS-UzIKrJbAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=T78JWADO-7sUSoMGXt7Z39Opz4KKpPsNTcTbJbQ_2rqZwYoIF9tFp-JDqq_xkJYLNqijCl8K8Ic5HUUdi60kJV5PYNf-X5xnWTiig3bqa42vkXtPC-9nghh_3NNuROVg6dHvyXa089xAPSPIGY92SjnnVVtJa_ClSZjABWILpLF-SX3VPExrtkh1aGjr5p_igSl4PWa767Z4-MhiymCmP7ugZzJGKevYcfw-8NQJiO5OfwVirqe_OrX11YN_oXJ0g_l4BHNxictaBrrH-XWIN2-BEnh-V1rpPsd_AYgaBv_KUDQUkHUCZ5JLiM-AOD1Q4m8V1vnlvrk8HmlJyebomF1bk2kOTT1xbb83hWBiDGka07p603XsZ1sdwCuOihIjkezoixQyyWAF5G9GOBv3VOdNgCdAIedUmTNnizJIaYaxWs2mk4I34q80b08UjZf9CfE1SPLwICoRygIyjlSkdyB9wEDYnApK9KA3Xb3piRT0objzvWREsCr_m-6FWJkmxRsJwKxJSV_IWBmSWFovXUELHGcWwSL8H-5JS8aFyne_8X-pJ642eO-0na40zr-gpPVv1YnY57tMLTDqIvwOiGSm1hmnopu2yWCIUmP4OtR1KFkhfR_neKkuUV2aNCRD6_tBCX4mzNHrs21eMaeBo1st1m9pxp3KMJMFcLAEhuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=T78JWADO-7sUSoMGXt7Z39Opz4KKpPsNTcTbJbQ_2rqZwYoIF9tFp-JDqq_xkJYLNqijCl8K8Ic5HUUdi60kJV5PYNf-X5xnWTiig3bqa42vkXtPC-9nghh_3NNuROVg6dHvyXa089xAPSPIGY92SjnnVVtJa_ClSZjABWILpLF-SX3VPExrtkh1aGjr5p_igSl4PWa767Z4-MhiymCmP7ugZzJGKevYcfw-8NQJiO5OfwVirqe_OrX11YN_oXJ0g_l4BHNxictaBrrH-XWIN2-BEnh-V1rpPsd_AYgaBv_KUDQUkHUCZ5JLiM-AOD1Q4m8V1vnlvrk8HmlJyebomF1bk2kOTT1xbb83hWBiDGka07p603XsZ1sdwCuOihIjkezoixQyyWAF5G9GOBv3VOdNgCdAIedUmTNnizJIaYaxWs2mk4I34q80b08UjZf9CfE1SPLwICoRygIyjlSkdyB9wEDYnApK9KA3Xb3piRT0objzvWREsCr_m-6FWJkmxRsJwKxJSV_IWBmSWFovXUELHGcWwSL8H-5JS8aFyne_8X-pJ642eO-0na40zr-gpPVv1YnY57tMLTDqIvwOiGSm1hmnopu2yWCIUmP4OtR1KFkhfR_neKkuUV2aNCRD6_tBCX4mzNHrs21eMaeBo1st1m9pxp3KMJMFcLAEhuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=A5oyASwrsFN_OFAZA0bQIAeQ0igQ_Pyb0Q9svvoiPWIVhyWnZBnQS_XhmorzzD2xVfyXa2RVtzWsbtj8cXVbM_N5JC2Oexq8_oIMu5a_tOlo36PMhUcYVWtp2o41zSf5G9LtvYHAz8EKUH7ilzJHo14NZu5WjUVtcVJ4z4GEBOKGyD5h1XGZ4PgZr0gzt2ze53bIaL7KR8GO26NH270LL1_I5jYibS-KfXcUzTbXpiyY__LIxdQZA1kJjEtPI2iECg1LZ3Aqz4DQVbfJOUzkJme-AbgfugWuuPah2R0-6y0-S_NkdGA-MB7JDNLY_aj2FrrYHwmiw83W3VCFS244BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=A5oyASwrsFN_OFAZA0bQIAeQ0igQ_Pyb0Q9svvoiPWIVhyWnZBnQS_XhmorzzD2xVfyXa2RVtzWsbtj8cXVbM_N5JC2Oexq8_oIMu5a_tOlo36PMhUcYVWtp2o41zSf5G9LtvYHAz8EKUH7ilzJHo14NZu5WjUVtcVJ4z4GEBOKGyD5h1XGZ4PgZr0gzt2ze53bIaL7KR8GO26NH270LL1_I5jYibS-KfXcUzTbXpiyY__LIxdQZA1kJjEtPI2iECg1LZ3Aqz4DQVbfJOUzkJme-AbgfugWuuPah2R0-6y0-S_NkdGA-MB7JDNLY_aj2FrrYHwmiw83W3VCFS244BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=W_zZ55Qw9vkOInk9mp8fo9kMIA2zZYqIOvT_9Bv0q0maLD7BK52Ro94vrv04fAATamFWdoCWKDtuvs1isPcTINW-1JLvAYbGjX3b-s5TftenqGrH0hxhFvCUXpZA-B7rHHcLH58TXqyhhBYO_rqD-8mFj0TBq1N7K1qxk94BEdhyRnpzQdGJUjqriVByXpj87vkct1bqgMvbyw1agIzivaPXYd0BvJruzs1MsVTEesqD7Jz8wKiqE55DY1UAkthyHCq-Rhdh_gC6DUs_C0aGS3zv0lDhCkz4pBnQv5hyOr27MuArsNzJ5w0HO_MPY_mmrwjeYS5FmKiFbz2wbdOLPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=W_zZ55Qw9vkOInk9mp8fo9kMIA2zZYqIOvT_9Bv0q0maLD7BK52Ro94vrv04fAATamFWdoCWKDtuvs1isPcTINW-1JLvAYbGjX3b-s5TftenqGrH0hxhFvCUXpZA-B7rHHcLH58TXqyhhBYO_rqD-8mFj0TBq1N7K1qxk94BEdhyRnpzQdGJUjqriVByXpj87vkct1bqgMvbyw1agIzivaPXYd0BvJruzs1MsVTEesqD7Jz8wKiqE55DY1UAkthyHCq-Rhdh_gC6DUs_C0aGS3zv0lDhCkz4pBnQv5hyOr27MuArsNzJ5w0HO_MPY_mmrwjeYS5FmKiFbz2wbdOLPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=BGIal0dvxIfH81Js4JCZjYbUw_jI0CGKkoXdt8T2ok23XN9I_JNs1vGVO2Hw3U5zBuGH44zZzLRkKpz2w5T7caX6RC4psp-lgnkyr2YXNbKrMTYCiM0wRYArir-a2GnjizFHzLBn12Vn7cy5QFXs8n-iXGZBgrYqQ1rapyS5xn9wNP_VlsZ0IDf2woLcD0P3J5WCrg-Xx3GmraqGaTWrg8CCSb7Qhka1MBZWXsGPY7fl6p9XoKks-Cae_DIghnwSiMx1nseTn0iF7t2OJt8kFefzaQCQnVWWWu__lzguv4TQWvrIR6QpIT4Gbm8Xeqy9WdPx8EXsqzivGtPgx-8yPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=BGIal0dvxIfH81Js4JCZjYbUw_jI0CGKkoXdt8T2ok23XN9I_JNs1vGVO2Hw3U5zBuGH44zZzLRkKpz2w5T7caX6RC4psp-lgnkyr2YXNbKrMTYCiM0wRYArir-a2GnjizFHzLBn12Vn7cy5QFXs8n-iXGZBgrYqQ1rapyS5xn9wNP_VlsZ0IDf2woLcD0P3J5WCrg-Xx3GmraqGaTWrg8CCSb7Qhka1MBZWXsGPY7fl6p9XoKks-Cae_DIghnwSiMx1nseTn0iF7t2OJt8kFefzaQCQnVWWWu__lzguv4TQWvrIR6QpIT4Gbm8Xeqy9WdPx8EXsqzivGtPgx-8yPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=JRRjC6-VHvI6EIr2H3IbHMw5HGZ0oCbqfvNzAFUI_0hfDQthw3iC23jKCv9Q_mNh6uXnf_7KMCjZKRO8qYw7hs5u8gPjnrHu2vZlg6cZmQm-E0Z7e6MJKwUyNOxL7sKQZbmvHiANT7hlo-h7yCI0Z4ld3tgsynu8PKh5H2epFSr0XYB8VqTQ1cJItXWUNwal6Jijq6Pg41hCpb5tmDxProRuAswuAqKyoDRjXco8PiyjPvx_FClnVH4tf5Pch0Sie1I2dPegVR-pdM2jKisgILCKFTRNLfHN4seuZkr0eGLxlmrj56tEWP99EFTYMSKT0KOGtcwT-E3FJn4Cvpy8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=JRRjC6-VHvI6EIr2H3IbHMw5HGZ0oCbqfvNzAFUI_0hfDQthw3iC23jKCv9Q_mNh6uXnf_7KMCjZKRO8qYw7hs5u8gPjnrHu2vZlg6cZmQm-E0Z7e6MJKwUyNOxL7sKQZbmvHiANT7hlo-h7yCI0Z4ld3tgsynu8PKh5H2epFSr0XYB8VqTQ1cJItXWUNwal6Jijq6Pg41hCpb5tmDxProRuAswuAqKyoDRjXco8PiyjPvx_FClnVH4tf5Pch0Sie1I2dPegVR-pdM2jKisgILCKFTRNLfHN4seuZkr0eGLxlmrj56tEWP99EFTYMSKT0KOGtcwT-E3FJn4Cvpy8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=hqDwgbl2UYiOLpEGWubWkSAxKkVY75he19TdFHoSec_pBDzZtZ-TRWYeIwkPnQRBei1irS32t8Y2RE8nHmzERNuMMHxAr2oM9MnPv3gHO9oy2WXFHPUg8d43v34-Z2suiniPxfD7bLoTOmRG6QDdvVv1uxgazAcIDC2h8e5NOxWLsyTRzsxKTVSIdLRrpqt1xoAQ_t1TUWhxn3fgiy1k4tq2mSYz5UjgREh--ZlfZp84qP68sgi6M11mlMTFYF027cWUQIFiJtjuyGUlNNXptq3iJhde5aAv073pV_FFK0cBntCWyN7tzlbEHXOGykBo6ajOng4-DKHweI0CV6tzcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=hqDwgbl2UYiOLpEGWubWkSAxKkVY75he19TdFHoSec_pBDzZtZ-TRWYeIwkPnQRBei1irS32t8Y2RE8nHmzERNuMMHxAr2oM9MnPv3gHO9oy2WXFHPUg8d43v34-Z2suiniPxfD7bLoTOmRG6QDdvVv1uxgazAcIDC2h8e5NOxWLsyTRzsxKTVSIdLRrpqt1xoAQ_t1TUWhxn3fgiy1k4tq2mSYz5UjgREh--ZlfZp84qP68sgi6M11mlMTFYF027cWUQIFiJtjuyGUlNNXptq3iJhde5aAv073pV_FFK0cBntCWyN7tzlbEHXOGykBo6ajOng4-DKHweI0CV6tzcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=TECcyCf0wdKMQ21jAu0LCJ01YgS9GnCUGbFFFBaYFbxB8WC-_YJ1L2cB-DkykCtBZPezlBxMBvc02mlhQbjtpoSP6I75OjzTaImfsVeEKWla1dROqWD16lRqASZiqmp7FBtfEB7Skg-iq8F5tH9G9qRYV2V8Ul1YTSfHAIMZuAZN0s-HJbSWXJpZu7lai8sJSV9PU90TxQ5e-6wY3dwjprrPwW49ZpNoxE_1xCUgiiYko0R6AIGwi7AiuYAc7cLCbMQPRlY752ImgImOo4YoSIrBownXmOVNCOhvOovVxiPO7bNk8Hmd5EUS6b4i8oShx_2fqQunEy7bTp7pYGUx3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=TECcyCf0wdKMQ21jAu0LCJ01YgS9GnCUGbFFFBaYFbxB8WC-_YJ1L2cB-DkykCtBZPezlBxMBvc02mlhQbjtpoSP6I75OjzTaImfsVeEKWla1dROqWD16lRqASZiqmp7FBtfEB7Skg-iq8F5tH9G9qRYV2V8Ul1YTSfHAIMZuAZN0s-HJbSWXJpZu7lai8sJSV9PU90TxQ5e-6wY3dwjprrPwW49ZpNoxE_1xCUgiiYko0R6AIGwi7AiuYAc7cLCbMQPRlY752ImgImOo4YoSIrBownXmOVNCOhvOovVxiPO7bNk8Hmd5EUS6b4i8oShx_2fqQunEy7bTp7pYGUx3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=G-0ysod4gUBPo3SNU7Ey4aNFTo6QvwyWIrnxRiPD6yTc4QUd4twGg4mjXLA_KlRGZlh3yuI0F5-z7mXbMwPw35ur7UL5s2pu_p9rDYEYeP3hVfHO7v3u7gUgjCzXPtyxjo7wyQ3PDtw9Vja7w_lUrJv9WWKFCE9f1fkTlhhQNZ7U9KNHf7vkjQgL5hOFAvGE7iVtMT5MUE65gVClfmoHEs0PjMNUggcMg2TiVFH2lW_BjSvdpD6PIcxDQ-pUq3jJUucjWwjHVjUZS_U-sGwAMYAY3z0Jj01UZO3j5haQ-Le0WgFra8MCXcMP2OUhbzCpgcOijJ0im1uxiR14qEnrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=G-0ysod4gUBPo3SNU7Ey4aNFTo6QvwyWIrnxRiPD6yTc4QUd4twGg4mjXLA_KlRGZlh3yuI0F5-z7mXbMwPw35ur7UL5s2pu_p9rDYEYeP3hVfHO7v3u7gUgjCzXPtyxjo7wyQ3PDtw9Vja7w_lUrJv9WWKFCE9f1fkTlhhQNZ7U9KNHf7vkjQgL5hOFAvGE7iVtMT5MUE65gVClfmoHEs0PjMNUggcMg2TiVFH2lW_BjSvdpD6PIcxDQ-pUq3jJUucjWwjHVjUZS_U-sGwAMYAY3z0Jj01UZO3j5haQ-Le0WgFra8MCXcMP2OUhbzCpgcOijJ0im1uxiR14qEnrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3kZiPD78-l8B9sZYJUDHoGNs5OldQheVfzaJAXrqWP7zcpYCLYKE8TQ6w3vpI8WhAalOW24HzNWXis_xxerhH3tB-DPe6ZMwbkhFN5iqJzjgf9NzmD1b9BZYkevk7lkp4sGxmH1Hop4j9CRLzftsgmVH96U89Y1YPrSaJqGtFhD5ADTGOKK797f0j8CkKxmxQPmUw6HLy4ubMqrgzsF8RsmT3oKBHrnC-IGry0xNLgDBUuS9T117ZLzagI0EIFlJGRSHXTq5zp58F6CHEdcZnrquFI8Nl4vE7mwtBqZiwOP6La3wH91NXiqJ1FCbdkam23anLtzlAxOrIrsLahurw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=a-ef645nNPOiKA3gVEhoJouZgXPpDPfhxncwv8nWw0TEdtvbDRD1Y2DHKwQ_SzE2k4HzdB1nbkPnHvlMqZEA6YWgLSItSNYM_5aoZXKJuxsUEjdmJkKy_YyW1fcjOq1Z8Jq95pT17H5C7dchnVv3Odx3I6MTkXGwp5rSAmKEoU-Zf3mcaXugsoSUtJlEunwglCUVpms8hz91OM2BAp8CXs1FtvRJSBUmJ1jY2R19JVCQ8w2lavewRYdRhAirA62F4xHNr1VN4w3ioQ-cJHhI5NPqtm_prUM9X798NKxoWVF5k1QzE2V18oh36Uo0NViEslWS_n3RCSPm5JpOA_Myzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=a-ef645nNPOiKA3gVEhoJouZgXPpDPfhxncwv8nWw0TEdtvbDRD1Y2DHKwQ_SzE2k4HzdB1nbkPnHvlMqZEA6YWgLSItSNYM_5aoZXKJuxsUEjdmJkKy_YyW1fcjOq1Z8Jq95pT17H5C7dchnVv3Odx3I6MTkXGwp5rSAmKEoU-Zf3mcaXugsoSUtJlEunwglCUVpms8hz91OM2BAp8CXs1FtvRJSBUmJ1jY2R19JVCQ8w2lavewRYdRhAirA62F4xHNr1VN4w3ioQ-cJHhI5NPqtm_prUM9X798NKxoWVF5k1QzE2V18oh36Uo0NViEslWS_n3RCSPm5JpOA_Myzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=snrGpMcm96o-fzL_Ea9kzoBc9TsisJiJCHvb9cjOTI37hGcAs2cuIKaO9t-7jixDxQNPexMqZ-dS_DIl_cIG1PoLtOoT_AUXE9rlSio1L5_LnH-avRdptU1YTeaFDvr52dFnkXw_-g-TSpvUvyRhuQu-XAdxkR0ZAzV7diYeMAJ_12N73v9jxodjPt8zcyrGnf1OX_JxrH4T9aW0fgiMcx5RMueh5VxZvNnXEyW2pf6CgqjoYuzjrDa0YRbmCx2VMH4Y2JeD9QlDI8g5rWaeMadUxIdEchxVoNzS0WvARKPD3AWNeFOLsdM86xrufxxH8e5u1-yRv-oESLxB92ZfTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=snrGpMcm96o-fzL_Ea9kzoBc9TsisJiJCHvb9cjOTI37hGcAs2cuIKaO9t-7jixDxQNPexMqZ-dS_DIl_cIG1PoLtOoT_AUXE9rlSio1L5_LnH-avRdptU1YTeaFDvr52dFnkXw_-g-TSpvUvyRhuQu-XAdxkR0ZAzV7diYeMAJ_12N73v9jxodjPt8zcyrGnf1OX_JxrH4T9aW0fgiMcx5RMueh5VxZvNnXEyW2pf6CgqjoYuzjrDa0YRbmCx2VMH4Y2JeD9QlDI8g5rWaeMadUxIdEchxVoNzS0WvARKPD3AWNeFOLsdM86xrufxxH8e5u1-yRv-oESLxB92ZfTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=I3-3q3sVspm3dmOjUgLkMpHo53_whXR_c0BYlQLvvrbbaP9IkKWAvdE4GwIR2rx-XvyifCE8DJjE3kkvyuQ-XrpBtAEdzdufBIDXSq8jAqVx05zAzdbA6rOzJbumb0SrCeTs47G4dT4FB91YcA-HEs4cPa3UR2Z23bCwhFMQFOmXeskZLDIG6BMjr0DvdZYx4Z8ZjzGQWSjP3fWv4q3kVvJbUXGQom6N_0rwxXgken8NfSp5stZCWBbgxgvrRfUJJPfmb4ARmipFIxzQHSS6GwfGKQtbiu7MIlJxFFK0Ug29fp5wyd6O_ZkPioYgRt7xxxTJ-BQojVb4o2T8_F5xwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=I3-3q3sVspm3dmOjUgLkMpHo53_whXR_c0BYlQLvvrbbaP9IkKWAvdE4GwIR2rx-XvyifCE8DJjE3kkvyuQ-XrpBtAEdzdufBIDXSq8jAqVx05zAzdbA6rOzJbumb0SrCeTs47G4dT4FB91YcA-HEs4cPa3UR2Z23bCwhFMQFOmXeskZLDIG6BMjr0DvdZYx4Z8ZjzGQWSjP3fWv4q3kVvJbUXGQom6N_0rwxXgken8NfSp5stZCWBbgxgvrRfUJJPfmb4ARmipFIxzQHSS6GwfGKQtbiu7MIlJxFFK0Ug29fp5wyd6O_ZkPioYgRt7xxxTJ-BQojVb4o2T8_F5xwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=pH84uuySpvBv8jVAO3m8EIy3x-eumWmAWVYDEILdPiAFvw5CP1hYgI1hGRgEbhNmI0qm5M2Am3Gtk1Lxt54HcoTDHL1tbfZovP77jeAJGfJNd0iQqrUinlIGm0CTBrKoNRceoUNCIxBE9207NUacKKaLHNRNLolNNx-dFkEFkgPt1aigK3KT8KYLUkoZNboTp7QKsWoalFgeQBlwuGRB_xA5d9zbAzLPgDUzJ5wjlBy5vH33dMWvYxHPb1iSAdmUnRf_Cdrvjk4JJA8t4zPbHE5x0Koaj0x3T_n4oe093eck-fkYY1oL0fv1v7Oliuf8c4frnr61syjLX_Q0lKXcOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=pH84uuySpvBv8jVAO3m8EIy3x-eumWmAWVYDEILdPiAFvw5CP1hYgI1hGRgEbhNmI0qm5M2Am3Gtk1Lxt54HcoTDHL1tbfZovP77jeAJGfJNd0iQqrUinlIGm0CTBrKoNRceoUNCIxBE9207NUacKKaLHNRNLolNNx-dFkEFkgPt1aigK3KT8KYLUkoZNboTp7QKsWoalFgeQBlwuGRB_xA5d9zbAzLPgDUzJ5wjlBy5vH33dMWvYxHPb1iSAdmUnRf_Cdrvjk4JJA8t4zPbHE5x0Koaj0x3T_n4oe093eck-fkYY1oL0fv1v7Oliuf8c4frnr61syjLX_Q0lKXcOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL5R5QHBg0QLZLU1ybRPxuCnPyOyFhgaU55agNDtMivor4DuoWOTQdE66oXgk6F7FxelCmrpptsYfYGtsbuFgOvdkrdAp1DlO1OLpe9UhWAKhFyKAP6r7oJXB8zcYk1NBKVJMRso56JdYDGFcEX0OvIMyMs_g5fqKs7CxHNlRvzGlB-C10hhWAPMm9CY7WT73-TYl6nnGWKHpOpzbhnDdRN_jtahIxYv5ZtAc7TZ7No5vCYN5ZzVpVU011fBOJ6zVENhAIP8Dgw8x5Yzqisai0ftyPD1dW8fcZww1fAcdpyCoAffl5SnfWD6jBZ3s7GrRYHFQEeGXjM6-_hkXqJ0gw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ZpjtkSSpX5E0BbhKF39OQhaQPbBzT3PpX6LDlK76Mu64oCewEX40CtyvY-0t8imXfxz8N69sIjQE1vIJrwdyoiT6WBZzZd1FXQduJehDHpM1BQbYFSsCGwtH7kKJJUFvq1mvAgPLi8xw4ugErpzOV-SXMX7CiB2QHj31ToYjhrue163Z5uwZrBgZD267_WceS69wEGb_gWijD9uwbNCy---RkB8U7a4v8yS0zq-WEu4vwFrYDKqO-aKHP_2FcPRic092snItvRKc49ai4rH2sVlFhreBpJUS4UYux9ixISOyq3Ls-WS13u0nmgbEaBq-YpC-8qsz8nrRUFemGEw_tjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ZpjtkSSpX5E0BbhKF39OQhaQPbBzT3PpX6LDlK76Mu64oCewEX40CtyvY-0t8imXfxz8N69sIjQE1vIJrwdyoiT6WBZzZd1FXQduJehDHpM1BQbYFSsCGwtH7kKJJUFvq1mvAgPLi8xw4ugErpzOV-SXMX7CiB2QHj31ToYjhrue163Z5uwZrBgZD267_WceS69wEGb_gWijD9uwbNCy---RkB8U7a4v8yS0zq-WEu4vwFrYDKqO-aKHP_2FcPRic092snItvRKc49ai4rH2sVlFhreBpJUS4UYux9ixISOyq3Ls-WS13u0nmgbEaBq-YpC-8qsz8nrRUFemGEw_tjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ceJ2u0WZlhPR2j3Rw6GrLbc1PW-F4Pbx232H3_5pL7iWxwxUkLr0-FzJixBbqITjTk_BMgx9vMeKZj7lPe8ZG832-O8qdExizG6s9l4bTGxlNoPJBtk6E6IOppyfAobEj0VHlbSxWRQII7VKTsi61himB_UNKiwYCzZPoBWMXHZZukPipdvDxfCOKYYE_Yk-17_0VDZU1EOF8aqDMDbZPY2GZbk6amN9xFRJplV-pug-9pyXOPINaIko6JjldqjVL51Uk3ykkKZfybNk2Pr_5me0dH__t-BIFtZtwbsnOawl6CWra4cO2iB6HdEb-gHL2Pzzksfau09Lc77t6j1ynQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ceJ2u0WZlhPR2j3Rw6GrLbc1PW-F4Pbx232H3_5pL7iWxwxUkLr0-FzJixBbqITjTk_BMgx9vMeKZj7lPe8ZG832-O8qdExizG6s9l4bTGxlNoPJBtk6E6IOppyfAobEj0VHlbSxWRQII7VKTsi61himB_UNKiwYCzZPoBWMXHZZukPipdvDxfCOKYYE_Yk-17_0VDZU1EOF8aqDMDbZPY2GZbk6amN9xFRJplV-pug-9pyXOPINaIko6JjldqjVL51Uk3ykkKZfybNk2Pr_5me0dH__t-BIFtZtwbsnOawl6CWra4cO2iB6HdEb-gHL2Pzzksfau09Lc77t6j1ynQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5534ITMZKT06m9Zhyc2n-GFx8MUHzYHSPCy5hHJ1ZnZmxQRgCXWk8EMN-hDQ4eyfLE5xzXsS8bmSn4EqGKfu6Wi_Tbt0lOVzdNW5z7DJ3SLlB8q9cuIyDDShAddVafMNRNzbRKLH8OKgCoaG2qud1aRe_2dtThBVm2WQjiFg4egoTn9O8NHDN9RDrXwNh7A0e7G2tVlAF6zFMiE2fI9V2SwFv6hj1GRhYPP7p-pKwn9AIMR14BlrDTRnbqsN36gD_oSJ8XvbAWb8DXiJrcpEWvMUagRVirrnvykHwuFzHqtiFASo9vwCMm5VruS9TiDzfGDtO86W_BVj6GPVeUrEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBuG-SXlmN5IlYZDZJIH7zoE-1-Stp13FOvQKpqMJKKlkUBWw2mk1OI_o9OpEE92m0aE1HBvDB8NlaynSZ1Sr7I9myaI2wDG5Cjm5wNVi6WmqVgwOD_F67FTftQcD6ZVIfoPcLjaMHI5I1wRP4iKY_bRWRfvOQUwBW4mIewHFsZ6tscmgLjZy10UfuR1FxOQKcW8j_fUilOV0WrnrFJuVgVGEl2IKgQPWfEAgKO5iIT0KuL1a1A8jL7Jg4VmMeZm3_e0DlCV3tu-sPRsatUKVZboMS6R1m41y0IGccPQJR5RTvyItP8hmDIO80_ikO6AKGBH2zvOAwEqOunnRUB5-w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=hs2K-uxWtBG0yYV7-yE02WNbqRTLS8iCFiGD8mPUlEsKKu7Cc4k8v38dfVc-qjR_T8DAckDqN2JqxWnuAsQmOgdP5fTmulwYjqjEUddld1CqeuKiLaI4ccZ3Jr5xIEb6_Kr5EWNDSmjIAET5rRkBe5ibsC5qFBAcXobGrB75E3SvF4S208ebKR1Oc-8WSkmm5yMku9hmuuSjtYE09LGvpC8pshBax8cX4L-X5qApq_ewYICHH8YTeO7oxphyXikZgS18I5wey2-cmi1sLkcXK3OWvXXzVPFt7iiUJSQ3cBDzZRLYdpH5lt1I5nAqYpON9-CooA7IipLcnn3vB51Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=hs2K-uxWtBG0yYV7-yE02WNbqRTLS8iCFiGD8mPUlEsKKu7Cc4k8v38dfVc-qjR_T8DAckDqN2JqxWnuAsQmOgdP5fTmulwYjqjEUddld1CqeuKiLaI4ccZ3Jr5xIEb6_Kr5EWNDSmjIAET5rRkBe5ibsC5qFBAcXobGrB75E3SvF4S208ebKR1Oc-8WSkmm5yMku9hmuuSjtYE09LGvpC8pshBax8cX4L-X5qApq_ewYICHH8YTeO7oxphyXikZgS18I5wey2-cmi1sLkcXK3OWvXXzVPFt7iiUJSQ3cBDzZRLYdpH5lt1I5nAqYpON9-CooA7IipLcnn3vB51Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJcd3HRNnyOk0xx_j9XyQqeJQX_JbWFnh7DlRkv8Pn6l5QTJK2iLq7187X-FPcR9IUuiZnWowXEgCgct49lfVGVJEiCJ1P6UG8lGlVHLqXXqUzm2P2TZjTYLF80Ajz4KYT4Qe96SHyUdmIA7GfU2uRdYmdkSitejjqztMIwXx1bJQTPsUuP0AkwduQ0rP5rOhGHROC5xKTWwdS32G_TQwtdfgOho1sCQ6nfbScc22fwUe96Z7IF-x0VSDjfveVBw-i-k1OhcZerGlNDNbPRVHIFVdWcShSW_Axxs0ovx4RPLCfbUOsMlStSkZSAZAyZ3GahUQRy8KjA3By6WO6gtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYy4NFdFmEjzR9uC9i5HoSqUbaBIuJlAgg74Net1iv2KQsQC47CuDYWj5bSF76S1OEowXcpph0zKbmhX2hjZhzPKcyJMz5ajCjDopOIqdMByk-FcxiZ-yEG3pTUfP4TW9S4yuyM56tdawpES3crmWSIISjHj4w0M1e7yq6l9-sF0NX4IMGkXITyaJl74mOKXqZK7qaC6ZheK0pjk5meZWZtqugXtvPifegkAcXJbr9WYI_9yzyrwiKrH5g6EpoBB8T3htxnv9iDuhhUI5WPR2ghk_xosqUga8uvYbhoYOY8XVQDv5QVSp5LPjm9qKG0NRzYWEjafE5IUfO64pDuGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/br5zswfKn1KeJ6MiyrYNmvsT2TqjeK0r1MhIApnbRH-4MTQnOLRQo1MbD8XSx91izl7UxE4k4WQdWiuIwO0BMdGWGn6Rz_TVPcsv_Is5kJkpRxKYWUfuqMDDZSwzceQ0oMuuOrz7okoYL7Gy19sMbEYhzgSWulXKa3V8J3gFZtZtCSzfMJyj_ciGIpQL0DCMjdfxCiPD7gZqSBmf_w5oRB1HEP578-FKJ4NZDnLYsxCpqQ_d277s2s1DWVa-tGhNrhaQQGGwkRSvInBx4sjtrnGOhS9JXwmIIFblKW1GzM5mppV89qMNx2BPD4szbCtbRShxIxnri3C0v-knLPtXGQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=lCCbONet5mDLgWKimnygFIlAcCP2W3idPX1IFLRrKen7QCd-6y7AJTrQva6t9rcCiye9GvRgcI60Lb1ID0Hbw-G7IwaJ9Cl8edS6_HgfpBPzcw7zjDmpXAWmLRG-QrvtOG_oLSqipKfM3L6wNof_ZcLSwg-aa_BdKv0I_ZCCMmkc3lOp-3Mt4QUt0xYmg8NR3bn1oxMa4EYEBoMXQHKWUHSMR3r-ueU-ZIigz7w85RlXxC47u12Mp1_FtRa4yQ7m5_IfrpGwnGaBR3CZgiOItqX4EKKeK3paQOnIO4HahFk_tFKDQOHdaP4Ix33pfUxl41bBDlTY5HOHaeRSWb1vCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=lCCbONet5mDLgWKimnygFIlAcCP2W3idPX1IFLRrKen7QCd-6y7AJTrQva6t9rcCiye9GvRgcI60Lb1ID0Hbw-G7IwaJ9Cl8edS6_HgfpBPzcw7zjDmpXAWmLRG-QrvtOG_oLSqipKfM3L6wNof_ZcLSwg-aa_BdKv0I_ZCCMmkc3lOp-3Mt4QUt0xYmg8NR3bn1oxMa4EYEBoMXQHKWUHSMR3r-ueU-ZIigz7w85RlXxC47u12Mp1_FtRa4yQ7m5_IfrpGwnGaBR3CZgiOItqX4EKKeK3paQOnIO4HahFk_tFKDQOHdaP4Ix33pfUxl41bBDlTY5HOHaeRSWb1vCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=s2Y_BG-7Mc7tBRz6vTuezkFjOt6QQoghLjeXqtzKnGJa2clKD1PLFiexOx7TNpOQvriXu4QoCu1gUQC4TZXf5Yt1zrk5cywom96-atPretX4Z1RqtQp-pmbua1VecjKU7htQbQe3F5cznzBkgXBRUTWbWs65mE9qYP0Qdng2c1XUadhHZVyvC4AMcMZM_W9A6FWa4GQZhYhgahfVNslFSWMMU-t8emb2Eh1WZ378UwVouDDEBjIvcTiG9nuDgfbe0OT6iNGb8T6h8rqgcHhsrk1JTd4JB_VtbMnDQsS6vIivi9RrKcBDyPuxcmTv5KCyZHzrVt5P_iY_XBFkxyqN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=s2Y_BG-7Mc7tBRz6vTuezkFjOt6QQoghLjeXqtzKnGJa2clKD1PLFiexOx7TNpOQvriXu4QoCu1gUQC4TZXf5Yt1zrk5cywom96-atPretX4Z1RqtQp-pmbua1VecjKU7htQbQe3F5cznzBkgXBRUTWbWs65mE9qYP0Qdng2c1XUadhHZVyvC4AMcMZM_W9A6FWa4GQZhYhgahfVNslFSWMMU-t8emb2Eh1WZ378UwVouDDEBjIvcTiG9nuDgfbe0OT6iNGb8T6h8rqgcHhsrk1JTd4JB_VtbMnDQsS6vIivi9RrKcBDyPuxcmTv5KCyZHzrVt5P_iY_XBFkxyqN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
