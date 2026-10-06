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
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAAJtGsYhKZ2KbSpP-gz4HwySCzd2d1BcUFVb6GKmvRov4SPbb3C2zfV9TK97aiSc817z2r4rm9jyEux3Z8m6menLemd1bLdqmbyEsRmmI-kNTJi0j6NZxwSVGvMxoQlQSCEILFK8GHtMTncs7Z_8aXgAFXrAsOuwvv67kWPq_-ymLm7A90ZvdRSZUkxBnHmZ8K0W2Xbv1DYQk9SMIvaWuZ6DUw6OI-0Ojz4lFw8Y-ifFtcfzipf9tXyC8A30-tc5wlxbgWd9w2PdOg0Nr5R6kgpbDfFlbDuz18jb6jrwCyAOABX_4GCjoMx3LzlRZ_5CK2YKST1bgg6bnET35PowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Ij7HXiFjyww4rYngEUTpjlh2cF7y_oMnysAD8q0DQh6V-OhijGAcNDAnPAmsSOJ4LNALQ4c0f3jpLyM9UPhxfFRVYXyr54BR8uDr9nKXZHp2d3D4NY4mNnFend7g0peT3jUVUcOlGe3kV3-DxQ4IEFnwqJN6_M-dWZLB_Y5JuIWKOmvIjbU4UyMcCftTGun8m4VrV0ZWe1ofDwgLAxIesIeJey80K38llzPSt_iKofFTqT5nTkIvK1ea3H4fcLNKYwDOr3yo4dbCaRWJGm9hJGH8xEuaJv39YOLojPlaCt-WIlcHOLcm2z3-iIIeVVfCwInY7fElO2lYF3vrF8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDvLJZJAJOt61Vmq1Prt9I2XuEyJ_CgnRvM6yaPheaPo0p7nrgWc6604D1BqyXzl87y9Grr475lcUCdlbPYnLdq1u8pkJBhMTDDecbJ9JO5LiFfC7Khsq6C0Pj-l10zicHFtshMgG15t3lDHr35WZ1jwSktl_Y6XvH4Uf0yXTIW61bVqwWGITRzDgXRmzfTcPcDRwLFgqRy_ov9G2uMUf1LxlbZ_PcRhvaWtJIq2urJaKWANSIXkCoB3umLTJGqUg96QwNbiJuMw0Iej7tXN_zi1-QJSv00hw4_1LYUDOkuQhiAet0TrNjwnFjsHSexPgdeMtBWJFCeDGE1rdeHtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Gr0-mfBHmdYwCwqmgUqCLp4op9z0bJih5vgk258xsVw9G82DVS5VBfErTb5mZK-jtlVoCBULkw7eomIlJAptXETc2KMkQzujMBmVQ21k8cnVbtALQIIqnhzS7Zr9w8L1c9nODdpSl6LzCRFaQmcQEuM06CW_WZS4nogR_dLKNHuj0n2TJf0ap7cFRH714rPx7xaRaGlEOQMEFL7eGOB-JeG5PVA0TzRe272tOCcl23niE2eCFFKw4rQ4ujyBXIGpigXW60S2upnVLqQ2yDEwnASqpH4Ap0dn7u1BmKFJFQdErJNITOSLHsgSLzEWWK44oW9oGdH3mEO8TX27tjr-5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Gr0-mfBHmdYwCwqmgUqCLp4op9z0bJih5vgk258xsVw9G82DVS5VBfErTb5mZK-jtlVoCBULkw7eomIlJAptXETc2KMkQzujMBmVQ21k8cnVbtALQIIqnhzS7Zr9w8L1c9nODdpSl6LzCRFaQmcQEuM06CW_WZS4nogR_dLKNHuj0n2TJf0ap7cFRH714rPx7xaRaGlEOQMEFL7eGOB-JeG5PVA0TzRe272tOCcl23niE2eCFFKw4rQ4ujyBXIGpigXW60S2upnVLqQ2yDEwnASqpH4Ap0dn7u1BmKFJFQdErJNITOSLHsgSLzEWWK44oW9oGdH3mEO8TX27tjr-5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=n4JHXY1yWEJ_BYJC8EATvOh7ZCARMNAh8e4jfwczvUeVZEXIVy735x7rSm9vfeCtaOZWA9Cecu2B1KOSef20JWV2LACpALAIGfi_6sC9kBV-wN6xnCEQCsALYyN4z6e57W8Hw_AWz2rYhlQSeDk8labEuIY8j2aAdLjt2yxcQ4MX-wNqRJ01E0J1LvaoKwRlgpXHOKq3ZrWWnvAQeyPkduCmczv0quE4hl4lXUDjat11iqlUDkHyVsNIYSvef6axwKtagQPJjSUdUQVFzZYwAIhFSHqxq4YN_6IwFECPu0_EUbjjYfozkfElBpGJGiIGK1hgSwrIFImEff9i2StinajVyetFw7nDk2tRdX-DamBqJHOM4s-k5PGwK0VdiO40uaIAyUSjoPs7BXrFbhfyoe5QggeR5Xa2fwvSy06gstl5iMGu-0mC-RS3fteUDYbymFObEY_8h2PKTjLit2SV5NGvme_jwiuyg5PMKsEDjA8b6cKwH38pZR5XSYZJElRhKlncc1AO0TGDUzHsHI85exmrJfs75umbxTRcKSV2GD0ktGchePLQk5UouAU4TRongUEcXi_SHg4h5Qae9C-scQ-6zcPmyXrjkSZvs7RZ1mEB_sGbZMLAzeVFJR5w0xokquYxRMjxWC4HCZ3yZRtsrV1cA4tXqxHR0F1iFSfT6BM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=n4JHXY1yWEJ_BYJC8EATvOh7ZCARMNAh8e4jfwczvUeVZEXIVy735x7rSm9vfeCtaOZWA9Cecu2B1KOSef20JWV2LACpALAIGfi_6sC9kBV-wN6xnCEQCsALYyN4z6e57W8Hw_AWz2rYhlQSeDk8labEuIY8j2aAdLjt2yxcQ4MX-wNqRJ01E0J1LvaoKwRlgpXHOKq3ZrWWnvAQeyPkduCmczv0quE4hl4lXUDjat11iqlUDkHyVsNIYSvef6axwKtagQPJjSUdUQVFzZYwAIhFSHqxq4YN_6IwFECPu0_EUbjjYfozkfElBpGJGiIGK1hgSwrIFImEff9i2StinajVyetFw7nDk2tRdX-DamBqJHOM4s-k5PGwK0VdiO40uaIAyUSjoPs7BXrFbhfyoe5QggeR5Xa2fwvSy06gstl5iMGu-0mC-RS3fteUDYbymFObEY_8h2PKTjLit2SV5NGvme_jwiuyg5PMKsEDjA8b6cKwH38pZR5XSYZJElRhKlncc1AO0TGDUzHsHI85exmrJfs75umbxTRcKSV2GD0ktGchePLQk5UouAU4TRongUEcXi_SHg4h5Qae9C-scQ-6zcPmyXrjkSZvs7RZ1mEB_sGbZMLAzeVFJR5w0xokquYxRMjxWC4HCZ3yZRtsrV1cA4tXqxHR0F1iFSfT6BM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJe05PJ7A46GzVUCD4KqP48C-rWT34D6Ccv4sRoHTBRaAYW2YXhhnJicZvYnkFGk70tOblWHdDT-rhWimsZ_vIxYdHWA25oANwvmL9XlMbrYJa-KRQ9hqdiQ4s40SX5MzlhyGTOgcuQQCgvVVRIpnuKi-03vVPirN6R70kF-UjPp9yqEg5PSe4E8xWKL5EJp_2hBZJr4jy7PGA9YC6jpvNrhTDZf0Ab-dhlG7jhO6MKaC4806-0-nhc3WHlEyR--Ll3bVNMN44bHGEYf_o-G1IBbjjtfKFaZlfIJqX0VE9UuEmRL_Yz0YKV6ytog3rDcDv2bZm5FCP__26pk4Z_D6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdF9GBlzS-WXjkWXTlS_Pao1ga5ee5TscpLypvjFyeISCg7lPRtldxjAt1XBGwiDzrzll3lM0w04nn_W8NAHEgY40JAwEce2Xv7krDrN2LY9EYd0-_3KyuTtUh4jw6tEX-VSBDclFMvBoRzLNgzRh2MMA-DCZoq2NwhgGyH3qBN6vOWqNOQAZzv6MD2sDRQ2GhZrG6S0anHgSD7Kov2VN0hYSY-qgw9vdeoq5E-kifV3TH_3GnooV3-lwY7gxH44efSz0UAYJAsk4BRIDIOZdHpiLx5UgT1HoFkww94k-hx6N3FwwPA4yGSv_eL5xhjr0mhXhIBWwzkr3efWk6oUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9oji-CWwGnWn7MsYKRYNa36Gi6dC-6olib5RGXHE3BBTmYP3mNgsjkx3NTaEv8YExgK6-B7h7mEFRY5ChqWQrvJ_eIVOaywToTTeHNeyO-CHrcS9o6bs0z5yf_tKFPsgPMKw_dEARRNmOddowEr6065mDV4TmBTDK7N71aqCfzYxFam9G9Dgudr-5nlN28SLzItSPmqPgmZpTs2IcNAqtBCQ1xTf2wP8G6ORCt_hnaLKMgs76flW-8oV3-zcILbSRJ3S4hxC9yiX8JWwyXl0AJ1TT-XFM8McGPt_dbaODDs3McNq9UcfyosgSYeB1jS3F6Zvrfh3RoM6O5yps29HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=llB1hKHpsKs4ld4yYRF3eYDFBz-j126b6tor34C7P5-EX88VFNQF26VLqutGPLnbdpWshNDQ5RIRhFf4U8RKIJ1ZLFXx_ue4yhsRNnbhcFe9UjkKq_6JxPHw0r72S_ANIwmY9XaF8tI4uA2NxhXEXA9i5tCuSLk-LAH1tU5kOD-M2_3X6It5MxkUqWdzN-4pXq4Q_H-bhCEhYjI5YiBsBKQO-mXs8M_bRKA4r_v1lrom7apo8S6YLp2KkqbyPS7s3EecVzDrYAsRM6Id7r9Ouxb7T4UOSY-x-TED0A1DJXfKfMwLgHIjRTQ9V-Yuqer3q_OkFEVkiKyf-2HXgglhoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=llB1hKHpsKs4ld4yYRF3eYDFBz-j126b6tor34C7P5-EX88VFNQF26VLqutGPLnbdpWshNDQ5RIRhFf4U8RKIJ1ZLFXx_ue4yhsRNnbhcFe9UjkKq_6JxPHw0r72S_ANIwmY9XaF8tI4uA2NxhXEXA9i5tCuSLk-LAH1tU5kOD-M2_3X6It5MxkUqWdzN-4pXq4Q_H-bhCEhYjI5YiBsBKQO-mXs8M_bRKA4r_v1lrom7apo8S6YLp2KkqbyPS7s3EecVzDrYAsRM6Id7r9Ouxb7T4UOSY-x-TED0A1DJXfKfMwLgHIjRTQ9V-Yuqer3q_OkFEVkiKyf-2HXgglhoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=nEv_9fuA6Lw7KcA1Eol-lk2U75gL5oIEwEbtmhOWW0KNzZ88MgBf7XlKqVdYWS1e0fx5kuaIesQEzAOVkzIZ8RXbsncJHKBnTJZT8aUXQC4jiER8Tq0fiuOo5Vo5m-rxCeg3XzNg8jFrD1aSRe7xR4nyK63AWLYXo_g7AGeUIrv1QMvHW6An3CUT8TdrHKbq7Tsbc6Yx3U2kQvWJayO34znn9pRrH8UDP-p_FAcsEpNQLN74mA1bCLB0tSk4ASdoP1Z9RJiPDsskUbunew_mHSKF5aeiACF96945xnTVlAv4hfzZUIFUk4SWIQ8jBLbS4m6JWORwJOvQGnhZhPE_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=nEv_9fuA6Lw7KcA1Eol-lk2U75gL5oIEwEbtmhOWW0KNzZ88MgBf7XlKqVdYWS1e0fx5kuaIesQEzAOVkzIZ8RXbsncJHKBnTJZT8aUXQC4jiER8Tq0fiuOo5Vo5m-rxCeg3XzNg8jFrD1aSRe7xR4nyK63AWLYXo_g7AGeUIrv1QMvHW6An3CUT8TdrHKbq7Tsbc6Yx3U2kQvWJayO34znn9pRrH8UDP-p_FAcsEpNQLN74mA1bCLB0tSk4ASdoP1Z9RJiPDsskUbunew_mHSKF5aeiACF96945xnTVlAv4hfzZUIFUk4SWIQ8jBLbS4m6JWORwJOvQGnhZhPE_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX8LMr7sdZfoxZZjN4JqJ8RG7-fvIj36PGdMl6JVSFsQQBNHu2ix8yFPqhiyeONGei4YVaNcSuAMvgQl0ZZ6ln11pAdi_Faj-a2X_9LXIhrSzVfJhtZWeE1XeIN2DYQtvm-aCKnKzEiuuJvRUMNCyfrKOTMNIWfWnqP8Sa7k7ikrNEvo0TOaS5B4UNd3Xg5u06AHP7ajZgQWjVicSqCtbtY7Ej6SHbYu5J7tca6bNBowZUIbSo6YgHwejzyVfbFq8wcWX9yDWJ5ayox4G31tbFonpQPYONmwY2X3--EkECcKSCcJDKLl8RRE1xNlv45o7fkH5J7b3e4dqAd2RSuH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=S0ClfKBxY3bsesA-S-sCuQqNFHSuEP01XoUqAx2wU0S1xwqyxl6NVsoZkOtFXJJ_6WC2FsHq_JOhI3jVt1GajYZyYTTX5x7_VrK9V0LrctGnjqbqje0UaolgjFA5LQgUnPawW-xS_JeKKRmedJNJtmQOwLTv5q22zlXMLUYZwzpl3yv9I9R6nGpQx2QtH5QmPDflxHxlkMrAksyeG5iF9EB7MiWH-3WWgvvp4ffYElck1gkmZWEQQ3QiHusCEwtQJqw85NKUNthtkwRyY2Hi5VkwA-0zI7sQs3EqyfuYbgFA1m6h2xmOcs6tFjs0ddralaLPuxwjU4HXXCCYIO-m3huDhvP5KSARIxfiewhhgXCj37jo6KeiMzIeIviiRnO5SrHWGJokoO8zh3gEEtjom-pkqtqK_crScm9sYcQu9IhZX2G5cgXWPUnAddLZXbEUanRzg8bh2ASaEyayiB3JlBNbIu5Qa7aNw7MdjYiO8FiV_Zp36hpA58KlImvU2uCG2REP2T3n5vFv1Sp0Ec7nD0y83rFPmXuKf99-dRgef4mMtBky5JG7jKNR_xf7caJfAWikmBC3isaTq0nkfubzxauw7GmrcoJ56HfbQ1MZWvQnSpJdE9WDKnt8BP3SmFs-8ki_v1ZXi5fV517ISIHNWjNQu7narcPTZKgn9zx8TF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=S0ClfKBxY3bsesA-S-sCuQqNFHSuEP01XoUqAx2wU0S1xwqyxl6NVsoZkOtFXJJ_6WC2FsHq_JOhI3jVt1GajYZyYTTX5x7_VrK9V0LrctGnjqbqje0UaolgjFA5LQgUnPawW-xS_JeKKRmedJNJtmQOwLTv5q22zlXMLUYZwzpl3yv9I9R6nGpQx2QtH5QmPDflxHxlkMrAksyeG5iF9EB7MiWH-3WWgvvp4ffYElck1gkmZWEQQ3QiHusCEwtQJqw85NKUNthtkwRyY2Hi5VkwA-0zI7sQs3EqyfuYbgFA1m6h2xmOcs6tFjs0ddralaLPuxwjU4HXXCCYIO-m3huDhvP5KSARIxfiewhhgXCj37jo6KeiMzIeIviiRnO5SrHWGJokoO8zh3gEEtjom-pkqtqK_crScm9sYcQu9IhZX2G5cgXWPUnAddLZXbEUanRzg8bh2ASaEyayiB3JlBNbIu5Qa7aNw7MdjYiO8FiV_Zp36hpA58KlImvU2uCG2REP2T3n5vFv1Sp0Ec7nD0y83rFPmXuKf99-dRgef4mMtBky5JG7jKNR_xf7caJfAWikmBC3isaTq0nkfubzxauw7GmrcoJ56HfbQ1MZWvQnSpJdE9WDKnt8BP3SmFs-8ki_v1ZXi5fV517ISIHNWjNQu7narcPTZKgn9zx8TF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=HHUHgcMZzG4KWgaB7N14DUhmIeRnEYHujHSfH1fkOsywGq7LnfUBCAquOqmE-D6jxYGGeTOGoxaV1RRWrMMIW5JqfMB5KrLUZ2_fyCnzujC6cuZ-Ba-XwjF-dhG7GRfAPUE6bxM2pWCAYEPOTC97h5ni0WARSHrpkET8LfV0OvV64CJRbkt54j6a5-6c6rlLUKZ-95RVM4Iw7e8kTWiuW0fbqVu08qUu7Lk4Gzzv6uU1hHQW2ONC31QigtOUEPiHaoP7mHigZzW8KXD3XXkmuNjXXVq96PhcDQHjoK8jVM-vmBZvt0H3IKdhxhKkhHJSGj42s-6UfnNru27fjvF7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=HHUHgcMZzG4KWgaB7N14DUhmIeRnEYHujHSfH1fkOsywGq7LnfUBCAquOqmE-D6jxYGGeTOGoxaV1RRWrMMIW5JqfMB5KrLUZ2_fyCnzujC6cuZ-Ba-XwjF-dhG7GRfAPUE6bxM2pWCAYEPOTC97h5ni0WARSHrpkET8LfV0OvV64CJRbkt54j6a5-6c6rlLUKZ-95RVM4Iw7e8kTWiuW0fbqVu08qUu7Lk4Gzzv6uU1hHQW2ONC31QigtOUEPiHaoP7mHigZzW8KXD3XXkmuNjXXVq96PhcDQHjoK8jVM-vmBZvt0H3IKdhxhKkhHJSGj42s-6UfnNru27fjvF7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTplYhrZazfJDb5RaE4Yx7AJiaBbUDHQBqZ4Ht6eRCtjb0AmUih3VFJvwW2QdSpE3yT4T_lYLjxPFYhmFM76c8NhVv4jh913vxfI4l0C06pUGfV_mxZSs26QboVVkS8ka5JTQkRbufSV3r0HXoM8llpu86Ep3A4YFV26pGnSpCYe-d19yJP2jd2P98Z6kjd5YpPw6yEvao0QgwMzqegrQmK0N2GauVQ8-b5tZIE1ifxdjLFd0q4KiOHW1H_aOZtvhFYTYHC3eb2o0hYOlHFU59MFA7ACBEIISrFQtkZ-E7Sr2LPR3408t0FeoVXpa0z9zgwQeblCqZfmfCMnNUhR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=vvAe83sSiIX6ZTx8gDVvF2oOZjd36Izqj5p23F_arI-IIGPkl1D_n_WV3iqrtHhcweus5SE_b9JYQEADiJtg6xiKg6Y8Cw5QlSYrtWi1t-9wHgwyehT9yoq2ga2wJDRBh19ya6VKt0IcCBFBQg4xD6yRy9pRKfAqDl8oKsgSEmmfideKLVrYo6_d-xH51MSt7OXMiNegU3qKa-mFFgUXm_Rfrr5p_CYWEdthUvqkV1DYErpSI4FYuOSEPtiyy-wni5aYpMTbCQSzvpZMbhnN-rT1fLFnnr4tqV3IAMTF-Akwc39-_DDzE_KUWlTUnDGo8idJ5MotrUYdEZq89Bj7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=vvAe83sSiIX6ZTx8gDVvF2oOZjd36Izqj5p23F_arI-IIGPkl1D_n_WV3iqrtHhcweus5SE_b9JYQEADiJtg6xiKg6Y8Cw5QlSYrtWi1t-9wHgwyehT9yoq2ga2wJDRBh19ya6VKt0IcCBFBQg4xD6yRy9pRKfAqDl8oKsgSEmmfideKLVrYo6_d-xH51MSt7OXMiNegU3qKa-mFFgUXm_Rfrr5p_CYWEdthUvqkV1DYErpSI4FYuOSEPtiyy-wni5aYpMTbCQSzvpZMbhnN-rT1fLFnnr4tqV3IAMTF-Akwc39-_DDzE_KUWlTUnDGo8idJ5MotrUYdEZq89Bj7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8RDhsofK8VNHSux9Eaj18P2TT9HnjYfScRlnBv8VmNeiWK4C-0NFTD6CJgE_s8iEhfkzJLesH82A6aDnW6wWNeo_hoSlVGgP1YBXXDeyA6p5N5jzLtfO4wU_GHphQeKxvdG72d78mUtemcbO2dBCoz7V-vjBJBbUW0UoGAz1pvMSdEAJ5RFi_gJ45M8pT3U0u5XmOZxmw9RklmTyU-dbdvkAyKd8C5GZHoY0wuQUqaxPSJxwFg_IZ0MVPnAryJimv9dCqrVTESEj7rMw2SLg8KFx8TwkzsIoZTCKsDquOCxCxLyH8EEAOoQ23IB2LUNn4FrpAHugbNRI99DehLG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCZ-DV3uNAXidaOwXkYEIbsHESJlshDvFBYiL54OSzNI7jYI-qb2-CFrwQzIsTrMp1t4QU49oPeNKO5C7vc_em0D2FATEngOvqnZdKdo4xZN3SFFjsw_nAof-0QnVmMvOcrc7K6tGnk_EJC3iTpI2rVC-rwhyTTId8rQ47ImDxszj7Q_IMbNCoTikh_UCifPIQhHna6PANYWi7Aj3iykhKm0GA5QhiRljdNrB4GSeycxKYFOaaBOsdYeeTjuYEqEBss5coJuWd46NUnltJiWFclGwWXGG5LtffNeaohKu_Wdw1wTAQKZrdrKWhm_1-PKVSbUWiPLAPB4LKwQK7HELw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=DLGgq-7COnfEVHMbI5QVcUwpZcCfXigiFDpSCkz7GAYdhcW44qT-ELiqECVlviS_dO256kzJ88otfOBxsIMkJ9reXxkzcUOqgbV90vGzrDOMIFQm2k-DU2387kKkBkBaLw3jgstpfGvfHiqlwJxlVTHWARniXbNiAF_wOl-7v40y8Sf0HDkBK_VkjDpKwMYeDzreLbhDWm1F4uHCPkSIfG5w1CC-u1524dYpwkKayC2RvpPSUVkn3Unb5gAMpjKrodBX3a0jHbAj6oYXQc53WiNcWemq1PuVWRkf8shlDjbNcgaUwqtO4MfV13rdPXgGft9z1ihtwwzmYxFvgAwZ2S1PTN9OvuTuuDzXwRcA5aqJCa-MyR9Maan1clOAgm3BeKcWpCR73GryhCQVtzg9OodtnYQS9var9Adcanv-DXtNharSuO2mV2G9dhI18uVlR53P_KeSJMSZQFZk6T36Oa1aprbUbaQgsvWhVKv6MhTTGztM_u_OOQ6omu-41jsm3g9Gm8TnHXAOPrHfIaEVU67jpnnA1F7c3WdWmcqhWsjWG41R5j8Y9OB7jSyjGBkQliX6GzTYM0XSInBNRTYVpgE4Su2VFIJ3kIjcTagk4JLE4fVeXzbuf6Du0jrMuf7XBkUAhJbt0gFLlvYTvXrHNR5AFAdeXU2cN3r7eEq_vJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=DLGgq-7COnfEVHMbI5QVcUwpZcCfXigiFDpSCkz7GAYdhcW44qT-ELiqECVlviS_dO256kzJ88otfOBxsIMkJ9reXxkzcUOqgbV90vGzrDOMIFQm2k-DU2387kKkBkBaLw3jgstpfGvfHiqlwJxlVTHWARniXbNiAF_wOl-7v40y8Sf0HDkBK_VkjDpKwMYeDzreLbhDWm1F4uHCPkSIfG5w1CC-u1524dYpwkKayC2RvpPSUVkn3Unb5gAMpjKrodBX3a0jHbAj6oYXQc53WiNcWemq1PuVWRkf8shlDjbNcgaUwqtO4MfV13rdPXgGft9z1ihtwwzmYxFvgAwZ2S1PTN9OvuTuuDzXwRcA5aqJCa-MyR9Maan1clOAgm3BeKcWpCR73GryhCQVtzg9OodtnYQS9var9Adcanv-DXtNharSuO2mV2G9dhI18uVlR53P_KeSJMSZQFZk6T36Oa1aprbUbaQgsvWhVKv6MhTTGztM_u_OOQ6omu-41jsm3g9Gm8TnHXAOPrHfIaEVU67jpnnA1F7c3WdWmcqhWsjWG41R5j8Y9OB7jSyjGBkQliX6GzTYM0XSInBNRTYVpgE4Su2VFIJ3kIjcTagk4JLE4fVeXzbuf6Du0jrMuf7XBkUAhJbt0gFLlvYTvXrHNR5AFAdeXU2cN3r7eEq_vJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdERvQJ0LYa6qhJ6bmSutJwFsQ3U-grOxJq5uY81YLA0MOf_bldpR-DiI2_sBBkBf1wHzIwlgaVrZh_wbjtJC5ztZQO0jwIJ86KhVQO4yf1CQ3Q-2mNvWeJdLbBfcApGghizMahOeV4couymnBPCT5_QALbGFmN_zPCtyNee3Q8h0ecxugmSK2PxQmQCH0qnQLv1rZA44_h5CwFGcYPnjWfp1An8jZsvPO2iMy29g0WssG4Z4SfxdRCcEB7hUsyO_6ZsyPHe90AQTh3CxIBatGcb6tCGJVAuLD_yJzqzG5YXcjoA8kcWOOMKs0XXdLQ1v0vFNgsiz1nUxfEihDTR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN_CD3w-t3WPJMdDxF-qdaIVhc3V1jw2ADe8r1D3Aebg7R-qkdMz8yRPdBgXwAonCnexXo4JLrZQr0vySlH66CxtuUO7GkJmxQgz8xLk1Flcc6Zjs201eqFpKotsJdTBn84WjRs7HOEojIyvthrtpykpvBRrQ4B5gJRkR62ey5lW_ctXCGz7flsV20mXU0L__B7au_npvImca2XniPygrAdPbFboTTNaoIXKaxy-7yAA_49XECzRNuEWx6lKrolKNVlAIhY3olDV68FiR30K0z8T5k3lrdbgFHmLWtAd-w0v7N0vYzdgzw0Dm4-qmMv23WyXdhsEzwivyHpdYwLIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=AGu3oXz6Ybn5ZrHxCIX-Acelj2y031hj44IbR-BKPcrsrkzuNqoy5fVC0GQffw1HnjWHwwetEEGm7aNJIQ8Xiu4NdUnznX41V4nL29sZWtY45H6OSBI5d4U5L2tJGW7RJH8zFROKDNw1y8MC7qZi_rwiAK3oHUpX8tAbbfbo1ggGE5gMacLUNBDcJ6YHMrq4oR4IcL2zkJ9PJNAk0u1BsRDF4qyhz5o_oM_mNPhZECo5Q2LLIYyCR52oNNHGJMIJkk29tc6eeSGT5dxl3B5DdgUybJY6A9CtgWJffmeFxuMS521laJGL42xvrW6ggCxHs-u-SwgDU4I1Gvd8wlfWXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=AGu3oXz6Ybn5ZrHxCIX-Acelj2y031hj44IbR-BKPcrsrkzuNqoy5fVC0GQffw1HnjWHwwetEEGm7aNJIQ8Xiu4NdUnznX41V4nL29sZWtY45H6OSBI5d4U5L2tJGW7RJH8zFROKDNw1y8MC7qZi_rwiAK3oHUpX8tAbbfbo1ggGE5gMacLUNBDcJ6YHMrq4oR4IcL2zkJ9PJNAk0u1BsRDF4qyhz5o_oM_mNPhZECo5Q2LLIYyCR52oNNHGJMIJkk29tc6eeSGT5dxl3B5DdgUybJY6A9CtgWJffmeFxuMS521laJGL42xvrW6ggCxHs-u-SwgDU4I1Gvd8wlfWXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=bKfoTFQqJfkgLsZhukhXayxISZ69WhTU4LF4ivY4BgQPb8WSeHQ0jqjvJxfpsCIQlymB6OEOjV4TgJUnM4OPVN2rPsC3FPdYkH7hvjR7dYC4x4DLzwa-APqpxEe8ThV8R78RFW4HslITZxHNFAn5caz1ePLeb53LnYa5QZKxmvWsJqO4-DGYxcsHh0ly0F1DLn4_BlOy0tfZIHWdiVYI_6L6okt6RQ9fjmLAg0nRtvTEJIqDY4HrnLquxn7K71JQPhYd2Vtj7RBdiXYxB-nmWLcx5oZsiyCycUQUCZrAP7PfsccUIBOA18v9NI951M1Wy2rlZX4f-Xi9gs2KtJvfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=bKfoTFQqJfkgLsZhukhXayxISZ69WhTU4LF4ivY4BgQPb8WSeHQ0jqjvJxfpsCIQlymB6OEOjV4TgJUnM4OPVN2rPsC3FPdYkH7hvjR7dYC4x4DLzwa-APqpxEe8ThV8R78RFW4HslITZxHNFAn5caz1ePLeb53LnYa5QZKxmvWsJqO4-DGYxcsHh0ly0F1DLn4_BlOy0tfZIHWdiVYI_6L6okt6RQ9fjmLAg0nRtvTEJIqDY4HrnLquxn7K71JQPhYd2Vtj7RBdiXYxB-nmWLcx5oZsiyCycUQUCZrAP7PfsccUIBOA18v9NI951M1Wy2rlZX4f-Xi9gs2KtJvfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=UWpV5LN9glJ_Qdt4-Z6EfCLX7XwM_HtawtJvgQB2FDgUMxe4kCe13O9ldIiXnZiG1A9Ww8sgCmqh09KbkP9ttVeiQD_XvdbETTz7W5lqtMf4HQm7pqEmKnlACBhGIHCMbsVSP2x5qSTREBK_pCN4wOBlx5jtUi4-NY3IawVmjeb4fG6owXgJm09VnBFsHnlfsRwneS159C3BLx8T4QvuunlgDhnyRhKb8m3v3qnaUcT8SRDSnoj9XkteNLd7lPU8uUWv3dDIFLrvOLT2Z8LGJeeVBqElEYbaxvEr_-cybz9HI_jSzILnbp_W9ZbBt6Jdasz8_v1EtUtrTNFqgimSGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=UWpV5LN9glJ_Qdt4-Z6EfCLX7XwM_HtawtJvgQB2FDgUMxe4kCe13O9ldIiXnZiG1A9Ww8sgCmqh09KbkP9ttVeiQD_XvdbETTz7W5lqtMf4HQm7pqEmKnlACBhGIHCMbsVSP2x5qSTREBK_pCN4wOBlx5jtUi4-NY3IawVmjeb4fG6owXgJm09VnBFsHnlfsRwneS159C3BLx8T4QvuunlgDhnyRhKb8m3v3qnaUcT8SRDSnoj9XkteNLd7lPU8uUWv3dDIFLrvOLT2Z8LGJeeVBqElEYbaxvEr_-cybz9HI_jSzILnbp_W9ZbBt6Jdasz8_v1EtUtrTNFqgimSGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc4nb08EYAdN_U-ycBDqdd3zLw7yGIGuJYmz3m19twOkJOlvCNLzdfStwwRgWh8VeZETJp4tm_E2HlSq7URpPs1g-WCuWu0U_n5xPZ6Ufz-6NTgazCw7L5g4R_by_YT5bNDV9WoXF-zVzcK0mPQ2tH9WgOCpOpIuWjZlYyDsp8MRgU2G_MkJGbtDv8-aIhpwoBkEfGpxef5U8tuRqNHOuKFOOTNWniExe1sVAYNLcjGig_yTkQ425zL7ZhH9Ro7k3UwRQtjwWHeA1x7Ntgmj-FBOQYUZSR0sPXKOE-FjW1xBSnyXqIo_WftbP5vlc7rMsy89S2LooqV-YeJ5ZjSr8g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DRaCG_cqXJXpr7FivLf7-OJOqGSr462glX7NCN49fb3TTLf7r0j0nMGxesd9GiejcipBz5tNVQiwW64lRnfcDndmBtExwD9E2xBN5IO_gOx97WS9LqPQT8JpbSzASdBwo5TlN42_oczvxaNdtE8GBTDT70v6rzBBrVYhQn36lzK25mPjgB8TyaQU1pwIEuUQMbPhUYSlgET_nVMx28UwgvLM7mccj2eWnYv6QRtLzMOKpJ9aWkLb3X8ZCGXXuvADNlvTvIQqM2HSC8JRbSGl8nPUrizr4XK_FCuR37vdQkirtcVAKNbD0AYmH0A04HrLJdcwT3CBPeGkCpWq2MzKco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DRaCG_cqXJXpr7FivLf7-OJOqGSr462glX7NCN49fb3TTLf7r0j0nMGxesd9GiejcipBz5tNVQiwW64lRnfcDndmBtExwD9E2xBN5IO_gOx97WS9LqPQT8JpbSzASdBwo5TlN42_oczvxaNdtE8GBTDT70v6rzBBrVYhQn36lzK25mPjgB8TyaQU1pwIEuUQMbPhUYSlgET_nVMx28UwgvLM7mccj2eWnYv6QRtLzMOKpJ9aWkLb3X8ZCGXXuvADNlvTvIQqM2HSC8JRbSGl8nPUrizr4XK_FCuR37vdQkirtcVAKNbD0AYmH0A04HrLJdcwT3CBPeGkCpWq2MzKco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=A6_MfreKnCii_nlbJpCw7EaQakukcAax_svWocWoludG8BOs9GmaXdeoOwSrVQAQuFoNtBN-MlaRKuRhC_8-D6AHHJmRkYpG0uvVoyxKRBh3ES8FrDilo5awXWhl8tWY8cLQ2uusfZDWo9woM-FFnGFKtqH4Q0ChKJwE9oxPBGEMPTeG7_L86pSdVw_-vUIkSlWYGz9hP9vzI7H2c1jPeScFBAfKOJDtkZF2qxrlgDXQ2p0MVUf7JXbCDGrlwYqukIAx0XSNQOY3Yt4WNKB349YU9RoMVBligVkh5BmZGop091t3lOfxOGD3rjhoT5XYAGDLOTY3X2gbB7qaCZrGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=A6_MfreKnCii_nlbJpCw7EaQakukcAax_svWocWoludG8BOs9GmaXdeoOwSrVQAQuFoNtBN-MlaRKuRhC_8-D6AHHJmRkYpG0uvVoyxKRBh3ES8FrDilo5awXWhl8tWY8cLQ2uusfZDWo9woM-FFnGFKtqH4Q0ChKJwE9oxPBGEMPTeG7_L86pSdVw_-vUIkSlWYGz9hP9vzI7H2c1jPeScFBAfKOJDtkZF2qxrlgDXQ2p0MVUf7JXbCDGrlwYqukIAx0XSNQOY3Yt4WNKB349YU9RoMVBligVkh5BmZGop091t3lOfxOGD3rjhoT5XYAGDLOTY3X2gbB7qaCZrGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHuiuvVfJxiWoM1Uorx3aOVZy6jCQPFgNYBVYFClW7wxuCj7kyFQ4RmJJ2uKIEdrnLSFKfaXUzlFVJxEZwdEz-AEL1I5cWVu6xFjHRzeiq4jKd5fqyjFNOVD4y_Hl19gug52pbyhiOjG0kNBdcqeEBkXAKCP3Lu5b7XYx7AuheyMvyGS2bqYGuphl62NkKKrVf7iBvngIdDuo4JHNr2MTYoTjSynCxda_JPY2j1zewuwJUshgbRgw5Yy4RGz-0yNmADw_F4AiLZoY7dJkityL0PNwcytCSoFU1QPb0D65bfQaVQC9OQJ_fh0VdPkG9Bv8Ip9G99ZEX2LXtTznAp-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=PiKRdEDVhZSNMbrhvDoHNcMJZgNdV7OElx-v_o62t9_Jn8gc9OAo3fhPkB9D3lPiQDsJRoLCBCL3TG2ffGR0VCQTHu4znEx5YPBI9qjIbOcEVrDoke_msj1hvc29fzgO8B7SYbUP-JxJsfJ9Dbh_F-ffwLlAxc8EV7FWlUPZ4F2L7LgxDOgnwuQuJ3wT1MehYn3UnPB8Yi8USvmFqTnF6qJIa8O3byXNgsgsobIwj5li6iGzkLKkPkxD6itcpUerSRkQ63DSNY_OrPqvE0lCdtHs6ANImwe9N52jcPxDF8iwZSaufd8INcI98URWyPWYHCq7vNKK5LalR-RWXyXj_wbMFIMhvP4SozCisrIvzLg2-Yxjm1huWEFz0rLDilzE07nAt2Ro7MWnihWjMhWqrQ0qFqL3nvuV1BxcvRLjaKTX1_gTtUVVWCorwI_-vJLGTj5fHpYjvsQdwogmYIX012Vpm7p5Lf3XIBDgThBQrd3n47GQtXuIGFqpBvjq0pUI5USaU2h2fG-ucBwup-fYhiRgXReoBIsmmA4sLzClrqTNxRuXkcaQMHXGLwm_vpNOzKEbPOB6URNA1fkVPgz8aYzMla5I9AwkaETUjFGFfVSfzciA8AdblxkATdjdIfJSsL4JCfn5iFR8BCb2rY_WciEV673EZ572Sw1OrOXSeKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=PiKRdEDVhZSNMbrhvDoHNcMJZgNdV7OElx-v_o62t9_Jn8gc9OAo3fhPkB9D3lPiQDsJRoLCBCL3TG2ffGR0VCQTHu4znEx5YPBI9qjIbOcEVrDoke_msj1hvc29fzgO8B7SYbUP-JxJsfJ9Dbh_F-ffwLlAxc8EV7FWlUPZ4F2L7LgxDOgnwuQuJ3wT1MehYn3UnPB8Yi8USvmFqTnF6qJIa8O3byXNgsgsobIwj5li6iGzkLKkPkxD6itcpUerSRkQ63DSNY_OrPqvE0lCdtHs6ANImwe9N52jcPxDF8iwZSaufd8INcI98URWyPWYHCq7vNKK5LalR-RWXyXj_wbMFIMhvP4SozCisrIvzLg2-Yxjm1huWEFz0rLDilzE07nAt2Ro7MWnihWjMhWqrQ0qFqL3nvuV1BxcvRLjaKTX1_gTtUVVWCorwI_-vJLGTj5fHpYjvsQdwogmYIX012Vpm7p5Lf3XIBDgThBQrd3n47GQtXuIGFqpBvjq0pUI5USaU2h2fG-ucBwup-fYhiRgXReoBIsmmA4sLzClrqTNxRuXkcaQMHXGLwm_vpNOzKEbPOB6URNA1fkVPgz8aYzMla5I9AwkaETUjFGFfVSfzciA8AdblxkATdjdIfJSsL4JCfn5iFR8BCb2rY_WciEV673EZ572Sw1OrOXSeKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcP2QZHyUBzjH0lmCU7Xu5doVbkmP5R9yCA9eYDoC32Ubb5t4aPfU7hfkUCxPBecqC8NUXf3ovm2ckEjbyHVkASH-HTmTR4PxRp_uZNCcxQ0--LEfLIetfXVkZn8lZ6hPMLdKamcKipJIBdt4FeXnR0_lC0fZjM7lMGhX5eo3WTANGrbojriqH6lSTqxEcjIFTQQPLV19tMvSt1gkBjWYCC_w4cEAP4VIHE0IupdB6JPQ-x3IQ4_MIHBoZ-Q5ZB_dxlLiilK6RU7QvZZbJFoiPzUyly1FRJklylafDsxH_hPJwDwdhOv7Tl_9RccVNq_ri6xxtjUSudhs9HaYDXMTw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=DnujxkRcC2xH6MpPU9cUOpnp-gVXlWpVTdmNQ0maKuIQkhvxPi1mpYEtxIQgeJ5u710DxGho0u5OMYOaT0DtJxSqamwbK9fctsidK8nFXtBxCqQiSFKWMzLpzhchCpXe8qpazl2yoQJ2UEWGRzV190ekjOVPBs8UWy31xDrk0ReK3Jx_arH8dIV8O2wLGl_j9pb0gYYcFPml7rWP-A5SvwsKFUMQMt-HF0Gg89zab_D5sjEvJOJpidli8fdn9pSZ16SZea6TCkCqQ6-t8yAdIcbOmKTZZ6g224TYbrMHW0KhDm2pMp-4gehUgAz7NklZsYcBPfF7-ewrMpfYe5YdjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=DnujxkRcC2xH6MpPU9cUOpnp-gVXlWpVTdmNQ0maKuIQkhvxPi1mpYEtxIQgeJ5u710DxGho0u5OMYOaT0DtJxSqamwbK9fctsidK8nFXtBxCqQiSFKWMzLpzhchCpXe8qpazl2yoQJ2UEWGRzV190ekjOVPBs8UWy31xDrk0ReK3Jx_arH8dIV8O2wLGl_j9pb0gYYcFPml7rWP-A5SvwsKFUMQMt-HF0Gg89zab_D5sjEvJOJpidli8fdn9pSZ16SZea6TCkCqQ6-t8yAdIcbOmKTZZ6g224TYbrMHW0KhDm2pMp-4gehUgAz7NklZsYcBPfF7-ewrMpfYe5YdjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9dmh4_4NtLYBeB9r1PSRaXXDS5bxIZYBpglbLw8Y8FVqpY32VIRRx94Z-AVUe08aB0OI88eSybggGcByaVB7s_lvW8R6ozR1D8SGadRtUikw8_mKPrphrfQiCBGdo19D3-T5_DPx5vHH16XEwVCHyviAhLQE8cbPbLNu3RtWWHbbvjWzDcKHDofsEYNiQ2Hzmnnm7f6QFhksl07Yhcm74IR96Kl9XLt7LLetIpLCX2j3JWpPJykIsdR_tSX-OcXXSuLFJS3PLH8YmuLy2lb9NVbVykBy_ZUGwKsNtbplUm-itJSNOyP_RI0Y73Ei8-8N8rIfR9EUMDRri5WUKUIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmcZ6iITbD9VkcaiMyINdTwens4iYCRGyf1HE7p4Di0nPTlCHDnq8dmo_rstPpzW7g9Ipxg5vtFZkqsRki5RkIFt-MJOx7hu4ESVi5JJZt_zN2a3AJ4seZQ0G3U0tr1u_aR93YSGiVG8kESgw3GnI2mlvbJ6P1KGlSOnR_bsdrxvWPe8B-QyT-bztVkDqLxjwx8jd6nH82-jxXRtzObrqaaupgtxhWbTQCBbqcYNEOPHakpMu-z9Qb3NTQhI7DWKvrJsriUNIt9dAzH6Z-j0R-Hg9WzXsdQ_PGdeKI5V8XPmyA20hm0NEZA6VyvHxd_3Xj3LnT3HmdBN6lE4FA200Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYSHJ1DR6ixrPWhuy9XwaEuT6dJqJf9SZtObwBBQj--_lgKnFGPklV94yDlg9jsrI4EtjYm9_tS1cqg2Ck9mzmdNOrlNe6xAbx8R8pXNgDN4BUAxGA6IUx48HC7Eg4Xg34EnQYn4zn9cJZj_OCzsYxY1IjutCgERBQkjK7RtGB0s_Yq5pFZMz9ty8qdps55LpQMNeBLXje16tfeKIyRp78sjgOZeHeP6PxNvS1teVMCKT1lMK0z0n_ic4sxcGWTBN8_jZUfTxfPfdxn9zm-QGIRVam9f2cIw_hAqI3YIlFx3e7pR3hmgNDNWzyOMO_lJqegtZMCQxc3AiSXlKDHf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=oGfy0EHL4awUbgUmPnGkiO1qghtYUUlkjN45DD6S0IRKf7RghSSx0-zHFM-iljMdPOgRGTxuLccDAaf1fKS3UoMD4nzzD11HTIw0Y6x7_QPI4GlpmwVWlPp8X8sBX5a_2u0_c1I9rEpAG-J9qcZbTbnjAH50u1f_ClcsHWAY6BH8YZ5Ax0W-MhZlYk5zDRi4dPG2jejTq2AVSn6ksPiI7LmMYqsIcEk1ABwTMuflOJIRzTcCBSTDfmbt3gLQKDKNshwQ135JQVPSz_cOY6Pa52BvhHP-5jrrxzU4vWamnJ8vNO2OcQtWy-3LcuRn8K618Dxct63NenmyoDH29IXI0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=oGfy0EHL4awUbgUmPnGkiO1qghtYUUlkjN45DD6S0IRKf7RghSSx0-zHFM-iljMdPOgRGTxuLccDAaf1fKS3UoMD4nzzD11HTIw0Y6x7_QPI4GlpmwVWlPp8X8sBX5a_2u0_c1I9rEpAG-J9qcZbTbnjAH50u1f_ClcsHWAY6BH8YZ5Ax0W-MhZlYk5zDRi4dPG2jejTq2AVSn6ksPiI7LmMYqsIcEk1ABwTMuflOJIRzTcCBSTDfmbt3gLQKDKNshwQ135JQVPSz_cOY6Pa52BvhHP-5jrrxzU4vWamnJ8vNO2OcQtWy-3LcuRn8K618Dxct63NenmyoDH29IXI0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8Pwqy6X9GZbP42VoiZpM0o8A-CBueML1w0SU15sVcz5LEh4BEJBUFVd7H3HtDEYPz0EbnSxlmgATF38FfC8yCcYncsTQLa7prs4rN_p-Bx2MdYix88eSBx_QRjvKNBIdloREHiJGqNGa7TiklCAdZas2zjO4UHPmBHKoNIfhaAe4ql20RxZrFUg3roabND9iAQ0Rikz1uC9vPxue4HgdkoyBKMb-Dl2UJXiEj52SM90msTi8W7RNX6VLrTa2HnlCzP3O75leTk7ciLy3K5A5I2bqIq0x3UC_AF5zjl45AklFlsU1RPXcX8k8fjPEQ3B9P96pFeGqtKIQGbKoIu4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uux-CTsvfCY7cMvGgPkq4ZVULeImbLaRuCb55LdPTHvL8XqKKCbCnvHQdBObEccFeIbiTkNHQR5ZoC3eSmB5p8LyrEABSu5fcUJZGIEaHqD9k34xX6onz32MmtRTvxQCa26AFnZnZdNBTFDW_ucpIGIt47YuvLzvSfwDoBLHGm1B-gKPjBQC4AtltL0ymCZKIauX8J3MVEp54gK_rmjBKAu3HhuAChbScteuA2VcCdanP5bzjHvA3yOs_fS9_gW_p8Y847R2ZOFcevtde_bSRBhcwuScxTCqCshtkGCxk-RkXbxZ3ifCyM3sXQjtRE7sl21hrVArg_99dwUcMfvNR__Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uux-CTsvfCY7cMvGgPkq4ZVULeImbLaRuCb55LdPTHvL8XqKKCbCnvHQdBObEccFeIbiTkNHQR5ZoC3eSmB5p8LyrEABSu5fcUJZGIEaHqD9k34xX6onz32MmtRTvxQCa26AFnZnZdNBTFDW_ucpIGIt47YuvLzvSfwDoBLHGm1B-gKPjBQC4AtltL0ymCZKIauX8J3MVEp54gK_rmjBKAu3HhuAChbScteuA2VcCdanP5bzjHvA3yOs_fS9_gW_p8Y847R2ZOFcevtde_bSRBhcwuScxTCqCshtkGCxk-RkXbxZ3ifCyM3sXQjtRE7sl21hrVArg_99dwUcMfvNR__Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=v6M9yNx3Vo7XH4ac2xZTq0FOz8LW68QG_z59V1bx30-TPku0iM0yfV1Pxd-JLUdcQG2MA_1HWg4agoHUDvOtQlWDTXKCGqTU0poGtbNtoK6Oa_56wWLndzcCcaSROqKit499gJ4Ux3CicOpUbl-7u-A3r9uBfMNwnC9XGng1t-9z56bK3bvkctBaAmBkZxpiQRH7uWO6Xzzgz6V63d4pGIYeLXGmoQNNJHT6e6Wmm5PlGNiLWgasmMRHEiy00bE9c9SOEYD7DlnpVEk2CNIGZvepXGUo7AKbGobMZi4cusODX34-arzaChYn63OuzIpwIZIWCn2GZDzkMMoflgz2nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=v6M9yNx3Vo7XH4ac2xZTq0FOz8LW68QG_z59V1bx30-TPku0iM0yfV1Pxd-JLUdcQG2MA_1HWg4agoHUDvOtQlWDTXKCGqTU0poGtbNtoK6Oa_56wWLndzcCcaSROqKit499gJ4Ux3CicOpUbl-7u-A3r9uBfMNwnC9XGng1t-9z56bK3bvkctBaAmBkZxpiQRH7uWO6Xzzgz6V63d4pGIYeLXGmoQNNJHT6e6Wmm5PlGNiLWgasmMRHEiy00bE9c9SOEYD7DlnpVEk2CNIGZvepXGUo7AKbGobMZi4cusODX34-arzaChYn63OuzIpwIZIWCn2GZDzkMMoflgz2nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=rSYCi5Il6wh98tUyBCZN5rMROtw7-wbgZKPNyl8dhtOLb0wlxA8NaNIpkbBKVFCBwTM72iQmvsYaU6KwtIgr0bJ-r97FZvezGN7tbpi3jEDhJdtI3Y18JZB3GcOdt6Yr5l0ks6dz5Hkq51gV9qommfyM13I1u8AtQ_PbEDP3bYN1A1rFhd5oxX-LROyUyEbqB80IEEy2aGT6wmANQW-8pkwYz-3H6sfuZ9XRNiXqYdEKvp-KpoXlhVacgZ7gVd0pEqwnucSLBOg5fnbBS8yPBPw8IZrIGH4JCuEoo67pbYvMcS6YRGyyh_N7EZceLrOnQSrlM97qUP4T2HfexETCajAy5ue5Y1cbpgCBAZslmascZnxUaRXmNJ-gBr-1rGj7VhgLhcHIp5xR8uOxEbf0DhfA2yAyjdD-_pkNEki5lxOJjntimi7rEaD-5AjnbJLCzRKZdAI3KKIEl_BiTjR1EFHs4GwXaEbIh_vnKMVQ_7ZEdzVGhoa370iMqP7XMJpUDn9_eJb-GsuvoJbksC7QbKFz0TjX41SX01wtKOz2XVvwu8ezDVgDXdklXhug_veTFZ9I3jDkdjkQraE7wfHltQ00b-AswExh0j28xwQc-1zciCRc8Ul3PVM9MEhQ_i-DRk2VqcvWplbPeh4tlxZ8BlMlnL_6wNNUU5iCBU7yiIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=rSYCi5Il6wh98tUyBCZN5rMROtw7-wbgZKPNyl8dhtOLb0wlxA8NaNIpkbBKVFCBwTM72iQmvsYaU6KwtIgr0bJ-r97FZvezGN7tbpi3jEDhJdtI3Y18JZB3GcOdt6Yr5l0ks6dz5Hkq51gV9qommfyM13I1u8AtQ_PbEDP3bYN1A1rFhd5oxX-LROyUyEbqB80IEEy2aGT6wmANQW-8pkwYz-3H6sfuZ9XRNiXqYdEKvp-KpoXlhVacgZ7gVd0pEqwnucSLBOg5fnbBS8yPBPw8IZrIGH4JCuEoo67pbYvMcS6YRGyyh_N7EZceLrOnQSrlM97qUP4T2HfexETCajAy5ue5Y1cbpgCBAZslmascZnxUaRXmNJ-gBr-1rGj7VhgLhcHIp5xR8uOxEbf0DhfA2yAyjdD-_pkNEki5lxOJjntimi7rEaD-5AjnbJLCzRKZdAI3KKIEl_BiTjR1EFHs4GwXaEbIh_vnKMVQ_7ZEdzVGhoa370iMqP7XMJpUDn9_eJb-GsuvoJbksC7QbKFz0TjX41SX01wtKOz2XVvwu8ezDVgDXdklXhug_veTFZ9I3jDkdjkQraE7wfHltQ00b-AswExh0j28xwQc-1zciCRc8Ul3PVM9MEhQ_i-DRk2VqcvWplbPeh4tlxZ8BlMlnL_6wNNUU5iCBU7yiIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=OSc263EXzBJ72hpP6sJQ5QdWPPh_f_LnX4RpwXJdc2JjvnCKKD1AqAEPpqoIHyKlUP8JOCwPS2J6H0c2xORSNNyw3OACSE1HXX1zF2K2a75ptT1jB8CukDt7-yVcqbnEW3W-albSWvaoZLgJuJBwdDkPEWyr-oTqkOv4NoQp0r-SuaYkGV9WMsQtfpxkNAshWBUkG8Altdr6yquVhLV3q4a0ipxT9uJkX1dz394qBVhtRm7mzCgjYfaqcxjVztsLpxl-x1q07DY_iIlyaEf-rxO5xTc6YS9Sg8767usqDgqJ-H35JZXvS-gaGwjcL77gwyIqpfHuHJ9VVDyyG5eXPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=OSc263EXzBJ72hpP6sJQ5QdWPPh_f_LnX4RpwXJdc2JjvnCKKD1AqAEPpqoIHyKlUP8JOCwPS2J6H0c2xORSNNyw3OACSE1HXX1zF2K2a75ptT1jB8CukDt7-yVcqbnEW3W-albSWvaoZLgJuJBwdDkPEWyr-oTqkOv4NoQp0r-SuaYkGV9WMsQtfpxkNAshWBUkG8Altdr6yquVhLV3q4a0ipxT9uJkX1dz394qBVhtRm7mzCgjYfaqcxjVztsLpxl-x1q07DY_iIlyaEf-rxO5xTc6YS9Sg8767usqDgqJ-H35JZXvS-gaGwjcL77gwyIqpfHuHJ9VVDyyG5eXPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3zAd8AH_RIi_qsDwvxTPeQOw8q7xCpz0NO5WWS-2kU1cfchux3HLQ3dzEd1SGlIFbjIZ_XpkIgJBbAF3Kzhoz-AYLaRvkeANuOK5EXWi0wEFjhoMG-U6QXeTQrEheTNEWBoEpMTmOUhRbJQSFzJsPh2Igpg7ghgins_edix0QbmWRZ9TxMtjcNnqFeLZHIXfPkXTw8AlQLH-oDMF9XZlVaw20EJF7HfByJIVlz4YeS38l7CzQozb7lskxqVHm8yQ-1u_zdNBj2mPcHctoSUxbiwVdsv1SMbI8SN2V4gCk64qWIsY5mJBtkpGzbUjpNGLbb0FlfnB28NHD0d2qX9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=ljZqXpqkaU01hDf1up9fkd_aLz82EPuf5olGBnG5J7ljb-x0WHqoRR-KCqrhGxoQOGfnbi_IcQR4JRA2S7BHVlxsq11ULBoYdP1xM3VmO_SjkYDZkUmYuOFTtBg04oKkUBR5dE5Ur5C41MDubwEZcG8qHSYkkNjJ1txKGHoWWFtWf1eZC1cMKX0IUuwWvgRYwdLT1gZVnKI8e3jI16MSObvofTpWmLtLX7_29-OvCk2ZtDpEFsrjNxFswaKNsHljM2O0bUUpQ3o_wKGhj5cvEPZ1sr0x8jBhYK9TBq7RsFdMlqkWiirkllDQ45JBhSPUmezXypmXX5wm7JdgwtRF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=ljZqXpqkaU01hDf1up9fkd_aLz82EPuf5olGBnG5J7ljb-x0WHqoRR-KCqrhGxoQOGfnbi_IcQR4JRA2S7BHVlxsq11ULBoYdP1xM3VmO_SjkYDZkUmYuOFTtBg04oKkUBR5dE5Ur5C41MDubwEZcG8qHSYkkNjJ1txKGHoWWFtWf1eZC1cMKX0IUuwWvgRYwdLT1gZVnKI8e3jI16MSObvofTpWmLtLX7_29-OvCk2ZtDpEFsrjNxFswaKNsHljM2O0bUUpQ3o_wKGhj5cvEPZ1sr0x8jBhYK9TBq7RsFdMlqkWiirkllDQ45JBhSPUmezXypmXX5wm7JdgwtRF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=mepb0wJQ-pppPK3TcecwauliS_80KjdpZRfYjkvSTnZA7kmfWoqLE6oAHQLvAeWY396Um83ffmilWA9ehnHjBLl0xaWkNzH_fQS6x3Q07G4eIJ8q2ghwhS5RfTCFHorNn28Rf8GzfbMmu06THIiZCMTQkV991K5n3xbUSOQvsI_2j1qQqnzr663E9MNS8aYVNnGtRdkBao63ETCTg_pqijJ0AwJ50Fg0bDkDC7ay6gUMcGe2BCmwuo8-8Q2LGMLjUb0liUHTJDdENchGFa1iVZJ4qQ_yoyzSJIK2p6Rc0T4s5sz8PwS8h5xRYMR1wKsLkdwZNpfUAKpr8tOmDDnvSomgZEJtO-63USjXYdd428USkqFAzs8xpu716M_mGspes9sDQ5LOuC6r8xkpplJPynZMACYevLq1fvfTYoZQ-lkSuF-0d2iqWGRdqdRpNTXvezZyqD_KAosOWyb8hRx6yfGorR0Djvwh_-4_ZmKXDKLm0QqnAZxIs9MVhK0hnG7NEprcTXxUAK0xoieApOEdFjWdMcwNSV-wAveRlZceqElINh4RhMsVpqnUzZYahFgwlfWDNc2Egi9bh_6vsKSdAYHVBkOgaZ0TvYwAJlJBB7e6GcyvLh_G7omWinG_NfKvzF0l8VHlkX_hM2EGFc043MbCOGyVM2N-cC9EEe-swQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=mepb0wJQ-pppPK3TcecwauliS_80KjdpZRfYjkvSTnZA7kmfWoqLE6oAHQLvAeWY396Um83ffmilWA9ehnHjBLl0xaWkNzH_fQS6x3Q07G4eIJ8q2ghwhS5RfTCFHorNn28Rf8GzfbMmu06THIiZCMTQkV991K5n3xbUSOQvsI_2j1qQqnzr663E9MNS8aYVNnGtRdkBao63ETCTg_pqijJ0AwJ50Fg0bDkDC7ay6gUMcGe2BCmwuo8-8Q2LGMLjUb0liUHTJDdENchGFa1iVZJ4qQ_yoyzSJIK2p6Rc0T4s5sz8PwS8h5xRYMR1wKsLkdwZNpfUAKpr8tOmDDnvSomgZEJtO-63USjXYdd428USkqFAzs8xpu716M_mGspes9sDQ5LOuC6r8xkpplJPynZMACYevLq1fvfTYoZQ-lkSuF-0d2iqWGRdqdRpNTXvezZyqD_KAosOWyb8hRx6yfGorR0Djvwh_-4_ZmKXDKLm0QqnAZxIs9MVhK0hnG7NEprcTXxUAK0xoieApOEdFjWdMcwNSV-wAveRlZceqElINh4RhMsVpqnUzZYahFgwlfWDNc2Egi9bh_6vsKSdAYHVBkOgaZ0TvYwAJlJBB7e6GcyvLh_G7omWinG_NfKvzF0l8VHlkX_hM2EGFc043MbCOGyVM2N-cC9EEe-swQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trQR6Iqlz6zuPbaTRivxlv8-gNwjQUIakTG3v8roGECQsYrHusw1h8eOc2pINGR2iR_-ZD8BwVqtMCMZI7zsdFKrEUrFj0i_NW5_xAOqRnmoLgTIw5x9dVXSjRmKuT3voFtKjRwBzTfg0VwtI5y9_1_2W4XvO471o-Zi5S2Rp3it-r4W7IuZ-jQpwTsBN5yG5SU0KnQ7s-BK-j3KcJ9lPeEsqSB76si9dgFF6N2FK-goK4DBo2AhyZhb76Mo-Z4JFYnGVnyhJSb7umV57hj4zSMSd7SRp13uGd9oHDGkhn6BHpzZEgABuJjfMT3mX06TF3VQBxDGgA96ls6GgU3k7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=quwLqI1mJGD8ZQMIR-CtKyZe3OtCIMYXWMzOfYXefbvW95iIVSn6t3qgf8pGDl_ACDnhRPhYHl0JXw9jNU9UPJIoGmHdupvqs-1i09wJHFLXwjdpyEs40MJTvIrQ5ZxvlPRDrZ2z2sbQYJIhJ3PZ8FJMBGGbsIdhwguVUMKyj6T3dN3QgtlCtBb5W84_-1YwEprUjWD3dODy2zCrridtqEFo88thXZ2CouK50UO0lSWjf0QcBFrLMlHppFdON8PSHEVsBVk6nRKLYM3ilZGSPWPm5_fc2gS3hy78CoH8ObLfH1BJWwy4mQUi8jneGqe9YHXjVT7seb4mGxsCJLqUtJ0ygSHbDUI2_nYuAEi4I9Pnryc4ylsBgTRYOTlktKZ0Aba1hxtcscuQ8icRqlgjqJBMkrTtEyJoG76RLZva0UqqFhKF4wG6whSiFJnDSO7qCjQSe1nrqLQTc5mlvGBiONX9whtB2bL6clCDhvcHpeWyvn-MbRlizw7hvgYRQ9vGOZNeWDpGCP1gEid1nRPxV_fXh-Nj2tixztkPGynwQ503JhhoG4NC5Gez21_cXRTQRlAkhRGw-PcmdKy1LoClTizuj0wLiv1K1koEidcwgh04PrdRuY7wrYe2aAFmQ0jMIfa7CgMIXnl96WjxWDctzdA130HxkmLpHLLxFMSCTh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=quwLqI1mJGD8ZQMIR-CtKyZe3OtCIMYXWMzOfYXefbvW95iIVSn6t3qgf8pGDl_ACDnhRPhYHl0JXw9jNU9UPJIoGmHdupvqs-1i09wJHFLXwjdpyEs40MJTvIrQ5ZxvlPRDrZ2z2sbQYJIhJ3PZ8FJMBGGbsIdhwguVUMKyj6T3dN3QgtlCtBb5W84_-1YwEprUjWD3dODy2zCrridtqEFo88thXZ2CouK50UO0lSWjf0QcBFrLMlHppFdON8PSHEVsBVk6nRKLYM3ilZGSPWPm5_fc2gS3hy78CoH8ObLfH1BJWwy4mQUi8jneGqe9YHXjVT7seb4mGxsCJLqUtJ0ygSHbDUI2_nYuAEi4I9Pnryc4ylsBgTRYOTlktKZ0Aba1hxtcscuQ8icRqlgjqJBMkrTtEyJoG76RLZva0UqqFhKF4wG6whSiFJnDSO7qCjQSe1nrqLQTc5mlvGBiONX9whtB2bL6clCDhvcHpeWyvn-MbRlizw7hvgYRQ9vGOZNeWDpGCP1gEid1nRPxV_fXh-Nj2tixztkPGynwQ503JhhoG4NC5Gez21_cXRTQRlAkhRGw-PcmdKy1LoClTizuj0wLiv1K1koEidcwgh04PrdRuY7wrYe2aAFmQ0jMIfa7CgMIXnl96WjxWDctzdA130HxkmLpHLLxFMSCTh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Kd6kNWUX8vlXIFfd8YDr74RZuwicwct6pu4073DXMHzjt6tH9_ALpX0u7Cc7s6zPel_3SJmBfCsqt4dDyV2cvf-WqVYZTw8zmM3u_jWrMbQ7LLBhKmiwazjcaTzw1gcDcnepzpmYA6UWLGYafPGKugp7jhL23KRFP9trRGpg0sQfOmCx5FK-rdc0n_Zm-Fl3vs0RB7wLEcVewQP8E-qyLlLQ3DNfRwtHmzIjKA70XFU3oolxGQrv3N17zsfQZaeGlAnnwHIVCE8n47mR8geB-pOmvHWSSWXi0RVus-NOrWgeuVYCO03vfsuKgZaOvSxe8Nll7EurLGtzOUkz05vteU2OI9RTDwMX1SGF1T3RDfSjB4O4GOyyjBLFoC-TVxVpooMbcui2vAbGfwoldqhcshqpyZObNnguwWJQEjovM7XXdHmhM-bulHcSXoClXCXtVw-uhfn6dsoXJXRVmo1HivXjreZGqGDgf-0-eASCK8dGMdrIwij3b21F_3rQtqg0tBcC3LZHWsiBOB-wDeqSlPnYiyzzuQ2KCOKVIEeBZboVp75hOBmeCIhQ4Ae9Kg-1fr3J4Uo33xqXNCn61Lf0ipS1gqyhJqBrhJvk0cTTMuWR_2tzoEgsIfXhplSLcWM7SvGl60oh-g2E0629anKPCnabKNM0darP0Bbb5GDmnHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Kd6kNWUX8vlXIFfd8YDr74RZuwicwct6pu4073DXMHzjt6tH9_ALpX0u7Cc7s6zPel_3SJmBfCsqt4dDyV2cvf-WqVYZTw8zmM3u_jWrMbQ7LLBhKmiwazjcaTzw1gcDcnepzpmYA6UWLGYafPGKugp7jhL23KRFP9trRGpg0sQfOmCx5FK-rdc0n_Zm-Fl3vs0RB7wLEcVewQP8E-qyLlLQ3DNfRwtHmzIjKA70XFU3oolxGQrv3N17zsfQZaeGlAnnwHIVCE8n47mR8geB-pOmvHWSSWXi0RVus-NOrWgeuVYCO03vfsuKgZaOvSxe8Nll7EurLGtzOUkz05vteU2OI9RTDwMX1SGF1T3RDfSjB4O4GOyyjBLFoC-TVxVpooMbcui2vAbGfwoldqhcshqpyZObNnguwWJQEjovM7XXdHmhM-bulHcSXoClXCXtVw-uhfn6dsoXJXRVmo1HivXjreZGqGDgf-0-eASCK8dGMdrIwij3b21F_3rQtqg0tBcC3LZHWsiBOB-wDeqSlPnYiyzzuQ2KCOKVIEeBZboVp75hOBmeCIhQ4Ae9Kg-1fr3J4Uo33xqXNCn61Lf0ipS1gqyhJqBrhJvk0cTTMuWR_2tzoEgsIfXhplSLcWM7SvGl60oh-g2E0629anKPCnabKNM0darP0Bbb5GDmnHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=KiPluqJtwEpwxCj7qyDSUNooGhuon6U4Q0u6EFrv_aH4zFtSXrpJ8XKOA_rtN-k3gJyvQJl2pkeQWyw7IyiiXwXpCVkIUw_BoDQjO96WOcp_C_utCpeZKSTN-L6R75DZ0BwwfdURQPLK8YkJu7-T_yniqUtU4ZqWuWTkwCB2GJHAdpBDYAaAvel4JzFIAn35jueQn7LqIIIAXZVU2NvUC0hTbWknYZjH68LUVnzggbzKr3P_jxDEdAcx-OV6AeuAzEJtWnRcmlZqK-0qdLwOJ278rVjtR3RKatnF6_fePqF2d9og5Wlsi4EA3XaY0ej7sLgO19e6tGGMZnAmS6E3fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=KiPluqJtwEpwxCj7qyDSUNooGhuon6U4Q0u6EFrv_aH4zFtSXrpJ8XKOA_rtN-k3gJyvQJl2pkeQWyw7IyiiXwXpCVkIUw_BoDQjO96WOcp_C_utCpeZKSTN-L6R75DZ0BwwfdURQPLK8YkJu7-T_yniqUtU4ZqWuWTkwCB2GJHAdpBDYAaAvel4JzFIAn35jueQn7LqIIIAXZVU2NvUC0hTbWknYZjH68LUVnzggbzKr3P_jxDEdAcx-OV6AeuAzEJtWnRcmlZqK-0qdLwOJ278rVjtR3RKatnF6_fePqF2d9og5Wlsi4EA3XaY0ej7sLgO19e6tGGMZnAmS6E3fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=B2hJCjyh7Sert5oTyVZbytddhSOwsUZqjOIgEGbV7i4mQ2t6zBYNlHO4wceagfJ3fdBmWz9NJYWMP5d5xYBp75X77g8xfuvkOz8rtaVN6ZMj8XXGSlvZ5kIisyTaE6NjrPyPuy8WskbgPBO2ptzBJuPRo8CSPQ92mXoK05aq9py7lsUuL-x_Ey01MLP0qcwvw5BaqwApPBFy8_H0RFY2zRks9dHB3GJ1CJNY6X4rgQJTRflsTJtj1IEtgdY-qP4jupYcGbkMueTTRXhU6JPAMWC4BRpE0WEg-hDbowqO_-6Sznspry41tGRwwHGzqJPGrU8y_VuDtCruwbtv4Iyulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=B2hJCjyh7Sert5oTyVZbytddhSOwsUZqjOIgEGbV7i4mQ2t6zBYNlHO4wceagfJ3fdBmWz9NJYWMP5d5xYBp75X77g8xfuvkOz8rtaVN6ZMj8XXGSlvZ5kIisyTaE6NjrPyPuy8WskbgPBO2ptzBJuPRo8CSPQ92mXoK05aq9py7lsUuL-x_Ey01MLP0qcwvw5BaqwApPBFy8_H0RFY2zRks9dHB3GJ1CJNY6X4rgQJTRflsTJtj1IEtgdY-qP4jupYcGbkMueTTRXhU6JPAMWC4BRpE0WEg-hDbowqO_-6Sznspry41tGRwwHGzqJPGrU8y_VuDtCruwbtv4Iyulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=q0jd1klRDS7AogYnXXrnTzSY5TBbwtMmJ1Xc-och9g3f2mwUsL_zMEU_CGbzpR5h69gLHOay1KEuJxqrKQNLapHJEuzXheIoRtIyjQ4D96eRBSiN7Mv6lX4Oyk4tFC4U5qxtBd7xI2e3vY3rQ3PATPX4DWLpxJe3Y4sxuUXa43MUJFE_j04Dgvn0ErzqXxN7q_kh-OwpwiLRRhJSfzKSStuca7OmdtSFJ3Ua4SPss8RdKMGnqSKvzowXb5qAVsqzrOojzi460fWYtyxtJR8XmamI-m8d8i4RCyoepKejBheEnBdDP76T5zxtnANKzslLWhX9TGawh5O111sYUGZuvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=q0jd1klRDS7AogYnXXrnTzSY5TBbwtMmJ1Xc-och9g3f2mwUsL_zMEU_CGbzpR5h69gLHOay1KEuJxqrKQNLapHJEuzXheIoRtIyjQ4D96eRBSiN7Mv6lX4Oyk4tFC4U5qxtBd7xI2e3vY3rQ3PATPX4DWLpxJe3Y4sxuUXa43MUJFE_j04Dgvn0ErzqXxN7q_kh-OwpwiLRRhJSfzKSStuca7OmdtSFJ3Ua4SPss8RdKMGnqSKvzowXb5qAVsqzrOojzi460fWYtyxtJR8XmamI-m8d8i4RCyoepKejBheEnBdDP76T5zxtnANKzslLWhX9TGawh5O111sYUGZuvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=IxTF3j78LAKkZ86DWB6tYM11EfkZqTDJQcRnBehM_OUGEUYiN0049JEX3jJusUZFrT-9TFEMAINUGVpukMTEMs2wgd8UX1Gr-lY79aFrXsDUP4m27IgIE1Kv9_JZt1-MU1MFLmoZ_Rhpn3VBbHHdTuosRyfZP1aaUK4dQ5HwQX3elTDpl1G_1umaOS_-9FC7lj-4ep6KbpwwNLHQ_Jq8IwIH2gei6_JH9otPoAyOoeGzoKF11h4tUCSOtYF9Fuo-_gwroRo1ZPve-z5miza1odPLa-d0857yJbo4Mmpe1fCpcGodKpJw6uzOO5tx_fiinOzROfDYHZHLYkKYXxyW6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=IxTF3j78LAKkZ86DWB6tYM11EfkZqTDJQcRnBehM_OUGEUYiN0049JEX3jJusUZFrT-9TFEMAINUGVpukMTEMs2wgd8UX1Gr-lY79aFrXsDUP4m27IgIE1Kv9_JZt1-MU1MFLmoZ_Rhpn3VBbHHdTuosRyfZP1aaUK4dQ5HwQX3elTDpl1G_1umaOS_-9FC7lj-4ep6KbpwwNLHQ_Jq8IwIH2gei6_JH9otPoAyOoeGzoKF11h4tUCSOtYF9Fuo-_gwroRo1ZPve-z5miza1odPLa-d0857yJbo4Mmpe1fCpcGodKpJw6uzOO5tx_fiinOzROfDYHZHLYkKYXxyW6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=pChn0DdvmX6fbVfDgFzZNlr_dXfPnV8iRZmcSY0oscd-wdPZub3YuURT7PQCoikOpqaL5CeHsYoPansEM6XDeo8Cu9oIc_zFgXdzdaWFHrnHCesXBsCMCdE6RxiowwVSY0krQaf0sL7dVpgErMO1WptPn-qJxbavh9aXa3hXs2GdVYSevwZhtoGOSz8DNE3WD3cGRCaveXnM4Lbcw3CuN50FvONxiEl8QaJX6AUKVjyrDjt5lj-79h4peZ5VzqnlwOmDii9F6M8DS7trGmEmzZkq5s5a-JNWKw3TDlDokm-jZvaKka8cih76gFYTsF5bhUPiXWa_tLy5Skeh4V4JKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=pChn0DdvmX6fbVfDgFzZNlr_dXfPnV8iRZmcSY0oscd-wdPZub3YuURT7PQCoikOpqaL5CeHsYoPansEM6XDeo8Cu9oIc_zFgXdzdaWFHrnHCesXBsCMCdE6RxiowwVSY0krQaf0sL7dVpgErMO1WptPn-qJxbavh9aXa3hXs2GdVYSevwZhtoGOSz8DNE3WD3cGRCaveXnM4Lbcw3CuN50FvONxiEl8QaJX6AUKVjyrDjt5lj-79h4peZ5VzqnlwOmDii9F6M8DS7trGmEmzZkq5s5a-JNWKw3TDlDokm-jZvaKka8cih76gFYTsF5bhUPiXWa_tLy5Skeh4V4JKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=qKpSmveWmymTC4ETnaW8act51ONMqstjRYY9WxUVRYopDUfpks0v1YaitC3MoIS19EVxV_uwMlY9uQIhp0C4JKvMrwRoUS6j1G-Bx5WFF14tyuL6V6O0_iTtWcv4oG33T638J7tEPlPcZjCRy2RQ_7Km6hadr3w_Dnaq4ud2hrIhiKalhd1gs4G2DlJIDMcM-cDIVzOINOyx7A7hv5NOwj_41e-7zZwThUeORadxtj65C1mr2Y3pegv_YaCjZH4UoKrPzERBp1zHMF0oInGMUONxpp0v9xlQR3poa_8fU2F3a-fGvDAp9UR8ebnDcfG5V2dQIX_lPepFc7i8bKNO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=qKpSmveWmymTC4ETnaW8act51ONMqstjRYY9WxUVRYopDUfpks0v1YaitC3MoIS19EVxV_uwMlY9uQIhp0C4JKvMrwRoUS6j1G-Bx5WFF14tyuL6V6O0_iTtWcv4oG33T638J7tEPlPcZjCRy2RQ_7Km6hadr3w_Dnaq4ud2hrIhiKalhd1gs4G2DlJIDMcM-cDIVzOINOyx7A7hv5NOwj_41e-7zZwThUeORadxtj65C1mr2Y3pegv_YaCjZH4UoKrPzERBp1zHMF0oInGMUONxpp0v9xlQR3poa_8fU2F3a-fGvDAp9UR8ebnDcfG5V2dQIX_lPepFc7i8bKNO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=l8G7Gj1_usUDs0RpnVIa0teCfjX7uq4lt-UaiPVJpUw_U_I6Q4VWcnHJOwFtHah17OnD3HA_JGO69Q1ueGQGY69F-DhnA9ja7By3VGAqrInKjTPFa6Z1T-pjQwr96yaQTzRr0yg6KacAqiy7mxF-s6wvpJnZXgJLeecrlXEJIWJA4P_8r8IcnePBtcRBwqi-hlBPNzmaF6Z-SE2GO4tmo58e7f_IK-cIxEQ_9nDR7ObaVAjCc8d05VuYPcVI5XxIyM7ljn0JYrq1phatMTPnCzvCrcY7G9kctl9XHV8CudPGt_1fIYoM6mhrum3yWzNrvBuOCwpkfQ9lEBnOA2pvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=l8G7Gj1_usUDs0RpnVIa0teCfjX7uq4lt-UaiPVJpUw_U_I6Q4VWcnHJOwFtHah17OnD3HA_JGO69Q1ueGQGY69F-DhnA9ja7By3VGAqrInKjTPFa6Z1T-pjQwr96yaQTzRr0yg6KacAqiy7mxF-s6wvpJnZXgJLeecrlXEJIWJA4P_8r8IcnePBtcRBwqi-hlBPNzmaF6Z-SE2GO4tmo58e7f_IK-cIxEQ_9nDR7ObaVAjCc8d05VuYPcVI5XxIyM7ljn0JYrq1phatMTPnCzvCrcY7G9kctl9XHV8CudPGt_1fIYoM6mhrum3yWzNrvBuOCwpkfQ9lEBnOA2pvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyKWCk1kXAtpILH-th7-X1-cOZCRlNKdL_ObkItLmFrozAeSPBnJynKJc8gCn371KRIriRVCkukFNQtSPNqLlK1thkVi7A8NzMILcDDfR44kyzwil3OWPr-dPYyoeimPq2ohkgfoYQS1WiFpvfUu73roqYx6fzdQyQtj_ypgsr6-L7wMuio-zGMEDvhajQR65Lqv67Jl8M52NouFjEQ6gWp6uP6uv6gR95_RXHQqkD0rmAMt3nr6HQ0WK-rHWksyzB-IQYM6eZBN4Y9yjzUpJ91y3BA8Hh6Hu-IqasAOrwK9IZ9OjgTMjyQ8K2BGXIYn1DokUcEvtisAR9eFIqlX8Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Y6b0C1N6hZ_lx4I1XuaqoO9mRcIIzdU_mENKlDZ-4ZGEoOdomjWqBUIUKR5EkjvW4jKgeJxqRrhEe0MYIc8F5YRwRKlOkGNew6x3aL6BYG4OE1ih1SSqj4VIHL6lYWtd58gy7Qg8vpGYRNZmtRByVDphzOa8bCfGDvJ9pJltRJUIgveo0Sq8tnuFdDqI06Vk2lR20W5lHZ72VLVL0xarIOF9LrS93Le30Q2-CUfegCf976avIwYhK1HcErtazI-quD3vHbgdDYk8dKeVH3i_yw4L35TNEtt8vJCf_Dyr0k3kwu1lz4vbIAe-DvIAlWqOnxuHloA9yW_sxqtc8lpf7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Y6b0C1N6hZ_lx4I1XuaqoO9mRcIIzdU_mENKlDZ-4ZGEoOdomjWqBUIUKR5EkjvW4jKgeJxqRrhEe0MYIc8F5YRwRKlOkGNew6x3aL6BYG4OE1ih1SSqj4VIHL6lYWtd58gy7Qg8vpGYRNZmtRByVDphzOa8bCfGDvJ9pJltRJUIgveo0Sq8tnuFdDqI06Vk2lR20W5lHZ72VLVL0xarIOF9LrS93Le30Q2-CUfegCf976avIwYhK1HcErtazI-quD3vHbgdDYk8dKeVH3i_yw4L35TNEtt8vJCf_Dyr0k3kwu1lz4vbIAe-DvIAlWqOnxuHloA9yW_sxqtc8lpf7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=eNFLNuhZNCTs7kqcD3SQ2j1BCWNcPHD5-uf4TWNBUDW-Y3lUG61Adx02ST5CElSMiypju2hceJVM5ue-g0XOhBp3OSzrpiIkZfSpOH57X3aXEocxT8EbQCtfXuaR6Yukp5m6Fg721fuOLBtfE3-5SFK1vpRq4vZ8Cp24S9lIcRzbo-xLM6yvBj_-xJrclW_Vqlj9zabrTKcUUsltRj2zrTkuYRV_iG3zeQcDYmH3USwf-_-ZBjyfVQ5-Q51YimmeVtFma-r4tP5-m4EQwWWtDd8PtCIybwPq5LJG2AcVt2AGoifoaxwwyoXIc3BfUxNtbtC5mDrWQrB8Re4mrqsASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=eNFLNuhZNCTs7kqcD3SQ2j1BCWNcPHD5-uf4TWNBUDW-Y3lUG61Adx02ST5CElSMiypju2hceJVM5ue-g0XOhBp3OSzrpiIkZfSpOH57X3aXEocxT8EbQCtfXuaR6Yukp5m6Fg721fuOLBtfE3-5SFK1vpRq4vZ8Cp24S9lIcRzbo-xLM6yvBj_-xJrclW_Vqlj9zabrTKcUUsltRj2zrTkuYRV_iG3zeQcDYmH3USwf-_-ZBjyfVQ5-Q51YimmeVtFma-r4tP5-m4EQwWWtDd8PtCIybwPq5LJG2AcVt2AGoifoaxwwyoXIc3BfUxNtbtC5mDrWQrB8Re4mrqsASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oeilH_2d8ts0AG1cvXG7ps75oqJQRt0nP21W2fhsoWDWJ-zrP_Lpem-goP__YiWlMJ3zzG2O7XdenPFV0S0c4DLcRKR4By0tJHR_6wbYx9sIeFi6-mHiE9sB-EeBVayLMZ1EfoGDJ4XaswZ298TWJhoObS_6ADTj8dpCGOuk8W2ONmKduSirFh_AvA--IMw4F7hrvXIK8zScL4ku6GexQr6yiOA9gpOAvTqwGUfZZuNutTerHsa5QjKkgU9OSBievnTjMhaLjhRD1ufTu1qiVWxdqklVrCI-kl2oYMwYB_9oT9m7N1Tdaabr85t1rBdL7BkNJb6YM5WbOvxUIOpLeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oeilH_2d8ts0AG1cvXG7ps75oqJQRt0nP21W2fhsoWDWJ-zrP_Lpem-goP__YiWlMJ3zzG2O7XdenPFV0S0c4DLcRKR4By0tJHR_6wbYx9sIeFi6-mHiE9sB-EeBVayLMZ1EfoGDJ4XaswZ298TWJhoObS_6ADTj8dpCGOuk8W2ONmKduSirFh_AvA--IMw4F7hrvXIK8zScL4ku6GexQr6yiOA9gpOAvTqwGUfZZuNutTerHsa5QjKkgU9OSBievnTjMhaLjhRD1ufTu1qiVWxdqklVrCI-kl2oYMwYB_9oT9m7N1Tdaabr85t1rBdL7BkNJb6YM5WbOvxUIOpLeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EIBn3Kvc52CwGsUN_uFvHa7Raj-PLj1O4IvnetDnqbtF1pEXMUh5Q7h2zcT2TiT9LrcbqtztUs1xR7er5HQSS-obFM2WiwQh9pskbj50VUHLcz5dJKGH1bmDpdMIYOvlu1duhZV4qi520mi9-MHclGEXEoBBLnmsHHnDicCA-l3as7T7jtY8FiDFKo9RHBSy2l9XT0Drt9WUXRxTS04VpYlO5_hDVYDjRjgavxDzT9ek7tEgAAolk-4kBY2AKcCaDDxbbLEFwO34KsJCy1dFRjNQHYSEbDZAdWIYE84SUjcHx6f2ogIJTyu8aNuuk-Mg4PHFeSQpZBJUTxGWv4q0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EIBn3Kvc52CwGsUN_uFvHa7Raj-PLj1O4IvnetDnqbtF1pEXMUh5Q7h2zcT2TiT9LrcbqtztUs1xR7er5HQSS-obFM2WiwQh9pskbj50VUHLcz5dJKGH1bmDpdMIYOvlu1duhZV4qi520mi9-MHclGEXEoBBLnmsHHnDicCA-l3as7T7jtY8FiDFKo9RHBSy2l9XT0Drt9WUXRxTS04VpYlO5_hDVYDjRjgavxDzT9ek7tEgAAolk-4kBY2AKcCaDDxbbLEFwO34KsJCy1dFRjNQHYSEbDZAdWIYE84SUjcHx6f2ogIJTyu8aNuuk-Mg4PHFeSQpZBJUTxGWv4q0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFzMmqD4ztb9JPuJo-wdoMLO1CuNpbIgp8CgCVmRW9BQbF0qB1rQOs3qkef_T5VLfCDCi1v-JeCJ6bGPgZw_kWAiA-7EONUwXz_l-cBkhds60_rmvE4rU4D61twxd1V2pDtkygQYCl30seFlRG-Qkeux8gNY5gB2TYuAOcgDdool4VUX7QEzuqW0C2x7IZ2xLV6RImqHain3F71wWpG9u9xY3o5L-C4iLunul_43G_XsD44LuTMN18unC-vS8z8qQVoWsj-vyOmX4WWUel18UQBBzRv9fC5Oz8g2FCu7yq5HzA4r4R_nbRnCpeVeo-uvmU3j4V5J6VAFVzNvd6Sfgw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Wktu53c0GvvL4k1EOqi8d5FynWLRr-L7oBbyWIKlCjYzwU5AKkSVbm85J6Lpb3MbrJfNXsENwyoRudlh_rXgdy91gFGIlmYK6vptUQ1tW1v5crKCu2_azXOuh5Ag5pbzkJyIGlcfxcIuRvT4wKQFOejVU46Nzs7rwWCxeZ8uEe82S-nBH4oJ_HXTj2J7MDhaRjm03bHnK0KfOVj5l1KVQYWxy4bLWYyBpVgPlClem_zKq0Jv4BxAoaFH6FV64FiS25mFgD5surGZjiCKlxM8PrFE6usv4oVP4VJsA1iCvhTUjdi37Fxw_LgEwF3IDEthxCshzaSdb7Jx3PvjlP5luTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Wktu53c0GvvL4k1EOqi8d5FynWLRr-L7oBbyWIKlCjYzwU5AKkSVbm85J6Lpb3MbrJfNXsENwyoRudlh_rXgdy91gFGIlmYK6vptUQ1tW1v5crKCu2_azXOuh5Ag5pbzkJyIGlcfxcIuRvT4wKQFOejVU46Nzs7rwWCxeZ8uEe82S-nBH4oJ_HXTj2J7MDhaRjm03bHnK0KfOVj5l1KVQYWxy4bLWYyBpVgPlClem_zKq0Jv4BxAoaFH6FV64FiS25mFgD5surGZjiCKlxM8PrFE6usv4oVP4VJsA1iCvhTUjdi37Fxw_LgEwF3IDEthxCshzaSdb7Jx3PvjlP5luTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=eGUl0nOhfLLsDEFlvY98A9hpY92bHwCSQcOh9Nuvuu7vAWPL_IVy7Xsb_BOvAV3oju_K9awtdzmCzFE0GDwBdWI3wydSsgodEVZtbOzH2vg1lJQIiai-txSpLIboWhWpfPK0XWtQY2nTf08FUwcmhtDul85rrSTVrSjnF3-m-oAlouwJXcB7hZx9Qb-LBnGpFFrctEhQOY-Sh8cMoQyDAvY3ZX5ZDE4kwiBSRPgivtAdOQzYCI8IqKEyUbB5dz2Sk8B_G5fHfqcT4jafPqnt8kDtG560S9jBgnrJpAhkmaaClt_qQ0Qbn_rMx7q_g2C1tffb_SsDca7iSykNswvP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=eGUl0nOhfLLsDEFlvY98A9hpY92bHwCSQcOh9Nuvuu7vAWPL_IVy7Xsb_BOvAV3oju_K9awtdzmCzFE0GDwBdWI3wydSsgodEVZtbOzH2vg1lJQIiai-txSpLIboWhWpfPK0XWtQY2nTf08FUwcmhtDul85rrSTVrSjnF3-m-oAlouwJXcB7hZx9Qb-LBnGpFFrctEhQOY-Sh8cMoQyDAvY3ZX5ZDE4kwiBSRPgivtAdOQzYCI8IqKEyUbB5dz2Sk8B_G5fHfqcT4jafPqnt8kDtG560S9jBgnrJpAhkmaaClt_qQ0Qbn_rMx7q_g2C1tffb_SsDca7iSykNswvP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1nQCoCPc1J7QW8_T2YOsDvbXUm_A9SrJhV-jrG15chf6g2KzWlVN3lghl0IUbproHxNhdpliwLKjMYIRIngyDw5kPhtUEnvbpTv-k2AS24CygKPzqBhXqmJhjnVnYpdNV-Z1hTYr8-hCqPihHqx-aBzRfIqK-kH_75z8HdO2EdlKwj_4Mxp6aO2RjPuKaFYq6lCkE9ItNdUGLDyWhtME-wdlaWhlZxUUuWVcPiwE_fyBa_tjIwL98D6lzwUnGfrVI6dW8OmeSDPNyeoHNEqdt7ULkpNkOb5nuqV1gZAqtM_f6vCFruQW3EdHYq1IAFX8E3tThExprkftSq_N9NjuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xx5NqsyfUx3kNvGNdtIRC_Dz3VDUUobwKDva619g57tfkljLo2vR0KpBP6SfaysDdiDRnNelpq17cddQGcDjc120JN0-FHJ-QSmYq5jnFWUuvg5O4Exy9ysCTxXqErB3Rqjl082obY247L5b_qhoPu6OiQnZx40yfoHFPOI42qmwtnJWECndEb1VmS8CRJoPn5V3fRS-zHGSpBUZ8cDz12Lg8TY-UqXXfTcS9Zz4N9Adxav4n3NDkzv0jekws-W9eXfo0tCS4jOgw4kRyIDwceGyCCm1_WB5O3lPQJVI4fo5wECi_qjlVND2N0S94VQBZOb7S5HOOo67ylPtv7_CzA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qmHLB1dB2whjJXvQhdCxDDu8F7Y4SxO2Bfis08oG3JZPVDiMCtf9W-9GEyvUzlAKmpFwBnTKX67dEIvmVZA2rmWXw_v3Ti7dpjHgu3JjFTp_56sPuc46Ur3yDkgaWd_Aync3DN4jVM7wYzp4vnEcjX0PL7wwiinAogbKncKHF6gT8Bwoe4L1jwgXSiHYcwqr9-1LWcwbVxZMdnDVSjNJTK-_SJ00RMGM0ghMqYu6ESTvQ6F92Z-7GYlzNG1KutZLfS9UidXGi9ZCQ5qyjU_kIK6V6aWupbfwu3G_IWjocJIwLaSkDoX0x2eByE6EIeX7yAw7EhXwtxCQFGlrBNFYSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qmHLB1dB2whjJXvQhdCxDDu8F7Y4SxO2Bfis08oG3JZPVDiMCtf9W-9GEyvUzlAKmpFwBnTKX67dEIvmVZA2rmWXw_v3Ti7dpjHgu3JjFTp_56sPuc46Ur3yDkgaWd_Aync3DN4jVM7wYzp4vnEcjX0PL7wwiinAogbKncKHF6gT8Bwoe4L1jwgXSiHYcwqr9-1LWcwbVxZMdnDVSjNJTK-_SJ00RMGM0ghMqYu6ESTvQ6F92Z-7GYlzNG1KutZLfS9UidXGi9ZCQ5qyjU_kIK6V6aWupbfwu3G_IWjocJIwLaSkDoX0x2eByE6EIeX7yAw7EhXwtxCQFGlrBNFYSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TipKkdGOkVwLqGiuSxzhwXpm_QHg8nkznj3jmz8v-mi_JWcB0KtHUO-xk5TRBszpAaLK2qHX7pFFnLQjikJYnhJAZNy10KFkHSL8vCY35G0YS5xgI3uZPrNWWxlb1zk1kcJ0WU8xNoiNHv2ZvIfHXpPLbFGs8mFr_SjLyuNNftM2gz5cL-aYsu56D0qQ3swO8FX86Q8D312RwJlrcrVVkI431mneqBR3k49m7Hw-I1iPlzOISeOVBEBSBL00Is3TStR1PLUuHiCrQvXdmvJ76u0FzXUdpDRr3WFuCjVQfR9ol1zDv8fV7_paDYTnGyNR2bCOjoQVeu2tXcUMIV-VKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLB_j9pTfoZCjJExQHIK2_0VDTQO6quLLBd98NMQV7c5sxxcTqg3N86yV0iF8OP97dDgAsL2VTXplSZPxJiD8tjYEI8OyYEys0IUjOww3pbYs86O8CEUEE6feLFdtUxKE9a3R9QZed5mcL6QLeIdrI6zne5DDhlvo_sMN9_nU1ephV0Q12z1-0Sy8VV7LDeRQ60zBUOi0R3llcjVZuYC84z0qHId9j81T1utN6eEbL0JFIxVynvTyBZFdAunF9KsSwwZFDI92ySs77XONHEHyJl1OuSgK_UhPP4pqUl-UTVpopWQ7k_fanZZggGRlIfxLhTZp2uTuonyDi8JrVo9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayBDBCfj9N49weHnxmjV2yGUpeCyG5Z42W5zUDUcvYwDcwTMFQQip2j4Mfit9RXFradDuufTSNXm33Msq5Ox0uLJ_4fsHop4iVtNt1fy7imM5_mF0x9MST9-qVh4LOhBEYLgb2cJtKmyPSV4M3XQbDjpXABilcA10Yl_YijIF2J7RZto0-5Xk797mLEnEid5-bcLC5AHAAlhDXSMy-csAPO7sgZQ7NESFIt7H0zQI7UyZGapMDVayBISsPt_quqZozfArmqzobSMixE0pJbb8ANMcNERHooFhQjujPxVtd6HatdkcQbUxwC3672b1Oruxg5qyCo7POGVx5zRE0ZMlw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MRGDgORZSHeFRR6uZeY3bNPaMTm7qgw0baMeVEgbo6Vi_ODjgHxEJL6NI3G-dJ4uDDIZhgeUe3bjjNLP6HGwjJN1GMQSyyDET613lF0KDSe22owK7-NeFq5ka3tcSlIo1cdRZh4K5OmytFJs_U5MzR6Fzr6PyKoxMKQLxOCS2OE3VULszj3o7pn2TbUtPhVz1uSNtId0XMCqxdNXpkvq8yEE_IWE4jLxIW8pfeqnc3B7_Ob6hmnauTqemNieyaUm7aXGZLArswvcOfvKO9F4dOKXmSO4zkq3YudsbubQMvEFK3IkZCONu5titcg7mtvcwjiSlkch3UdYj-avSo6jdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MRGDgORZSHeFRR6uZeY3bNPaMTm7qgw0baMeVEgbo6Vi_ODjgHxEJL6NI3G-dJ4uDDIZhgeUe3bjjNLP6HGwjJN1GMQSyyDET613lF0KDSe22owK7-NeFq5ka3tcSlIo1cdRZh4K5OmytFJs_U5MzR6Fzr6PyKoxMKQLxOCS2OE3VULszj3o7pn2TbUtPhVz1uSNtId0XMCqxdNXpkvq8yEE_IWE4jLxIW8pfeqnc3B7_Ob6hmnauTqemNieyaUm7aXGZLArswvcOfvKO9F4dOKXmSO4zkq3YudsbubQMvEFK3IkZCONu5titcg7mtvcwjiSlkch3UdYj-avSo6jdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=FwnwqbJEyxrQwXPBYUCBhPO_2byzc5aLFz11ukAkrjiMFWvkB5dzVh36ExEuR_16vL4PzMjR_UQo9vvt4AH4grtuXttArusRfDddobAaQT5djMPFipkzmh2fsuwD4u9CpTQkIugPqj1LijsJSiUsy-aQagyJdBHlC26S8DdQCZrxcSE8JrnIR8r608CGK1gwIfmnSkETMiLzV_htlssAbYMx_6pP9L8rsurWHF0YzFDSzMsZcqkeTK_aOavn_VnAVoW3J89QjpueIawFE5SGpTychdDAakJED5sn6fy3ex02U1jvlmJMGBQwMZ84PrjbsvMmGU1b-owcgJr6SB4qqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=FwnwqbJEyxrQwXPBYUCBhPO_2byzc5aLFz11ukAkrjiMFWvkB5dzVh36ExEuR_16vL4PzMjR_UQo9vvt4AH4grtuXttArusRfDddobAaQT5djMPFipkzmh2fsuwD4u9CpTQkIugPqj1LijsJSiUsy-aQagyJdBHlC26S8DdQCZrxcSE8JrnIR8r608CGK1gwIfmnSkETMiLzV_htlssAbYMx_6pP9L8rsurWHF0YzFDSzMsZcqkeTK_aOavn_VnAVoW3J89QjpueIawFE5SGpTychdDAakJED5sn6fy3ex02U1jvlmJMGBQwMZ84PrjbsvMmGU1b-owcgJr6SB4qqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
