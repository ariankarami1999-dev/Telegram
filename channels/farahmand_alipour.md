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
<img src="https://cdn4.telesco.pe/file/b9s-RN8kRvW2RVoF1QoeuwceXtl7CZItLZb9Wb3h4ESIhgY-m25D8oAx56M3RRAv2w0qo_XjuYFkt_gyqELFmkmf_ainJUQ6FAsuYACNQ_KIXk1HevwSedC4IR91bOLorpDoC9r3XX1ljl-dngP2BYgwyATi5_PcboQQgS7yffHR4RgZcosNmWZ2JqzSv6cshEOvucud1Ezw4eXmiAOkmiefQ--JvEBflNmoh1FlfnZvg7rXIzGpAt1ks1Ei8aW0-sbV4NpOZPi2dwgpdJ66X54QpiJbTSzwhj8QHto8I-QSEHzSP6qAE4vVS_AQNYCWdLuzKMrJudc7w7wI7m5y1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW6ht1rM0z0qXldFm0P5j7hIP8Z0cHh1z3HpkOu-ZFLqPzs1TextuNY4bqgYyszVwc3cG8nv6GGXRQlnmowvJha5F3mF_ifvs5oEQxvunkiPAMjdKhFijzcYOmXPI4e9s7yYPGEyw6lJHP1WuRm-ADyOdXSy8AqtfsIyiVSyILncGJb_bavSPjBq0d43WQjQaQSrAPCKOt94nmJuiTvmnR8xfRxiKh0JrM4hdGVhQes-yW23RuMn6bDc1rMoTotvmQMnNZg4OkLO2TY8ssgfhDWrjEa64njfABOoO1FUGBeKSTAnT3p_2xdjQH2GGp6vB5iSiVgdLD-fEE0JW4ntcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dryqg5dzwce35UWuXMd-L7cxlkB5-d8QhO59xSWLD4wXvjZz-IzLQNrb3K6lZBnznnIqtS8xpxtp8Cbfetnq8lqWlX2SNCMlmlSQxFvs-by3xcwVXfaeCF5k2U8TENuIxB518DVj3B8y54Vax8k1-4r9Aru-dtMu0pCzHIirIt6bjT8OXINoek8QCP9w8Elw8xgmHaNKBd5d4TF0Kf-M9y3oW3rmTktJGBRP0vt9OTI8uNr8sLwEnIsLw89QkU_CMBq3eJvWE0ZJD_5JU8WDBN-y9IB9HNu5IU81eFbxkHAO7yTq0ATkRrX_wBGpCZRxS5dr1CSR0uT2Emj_saiEJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=gyjn5QvcuIjSoX_UwijiRUhG8Iqp7iXp_4cmSCXoEBBCV2FFE_opoBU67KB0s9vjKLtCAUFZsMcws8QrwyoKPtq_56vO2PPDIsNh-1-gYKA3S1fvb7fctFxUal5hSn88cjv-U5ePnUq3lICL4zsiJmGctf2EskrMZCY7AimCOYABzMyteu49t1aXsPxBIGed-Y35RLxOKqshvQZe2MvR43bYmDDyIldenRS49qEroZuelXTK7_EyIT-tV1JH1g_wKylw7jMNO_rMt35Of45Njf-1W8V_tQ5B81kM9ctRthDINm-AkT1OdffltppzxwATrEdernGErTTEDrmH24pCzYv91VtPgbMAoDpQXo117HwxZfR6xSxqpi9E6vh7-evwjDHzjHYijnZwZjsokCiwJJMrX8HzwgYpSKum6vr7TaVZNHvHhAVK0_Fgc0DXMsY3EFRHtPnew0o02v-pKbrbaS9BK50BaA30WornYviDzn9jZ2049hq_8bpbDEdcT1WKVFGrOFfTs8kVq6iIA2Vs-MZfXVwiRqgNdigUqzGV8-BCz5Cm97GsQEbOaHD_l76TRcB4MNy25ChSRci7Xs9skwm7s7cT22pgjINxbE1Y8JJLpwbvLh59uURMsIpO1mKGfVu-KQq4FHW6qH5ep2ErnHUmMkrwazwcwnxcGg2BgwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=gyjn5QvcuIjSoX_UwijiRUhG8Iqp7iXp_4cmSCXoEBBCV2FFE_opoBU67KB0s9vjKLtCAUFZsMcws8QrwyoKPtq_56vO2PPDIsNh-1-gYKA3S1fvb7fctFxUal5hSn88cjv-U5ePnUq3lICL4zsiJmGctf2EskrMZCY7AimCOYABzMyteu49t1aXsPxBIGed-Y35RLxOKqshvQZe2MvR43bYmDDyIldenRS49qEroZuelXTK7_EyIT-tV1JH1g_wKylw7jMNO_rMt35Of45Njf-1W8V_tQ5B81kM9ctRthDINm-AkT1OdffltppzxwATrEdernGErTTEDrmH24pCzYv91VtPgbMAoDpQXo117HwxZfR6xSxqpi9E6vh7-evwjDHzjHYijnZwZjsokCiwJJMrX8HzwgYpSKum6vr7TaVZNHvHhAVK0_Fgc0DXMsY3EFRHtPnew0o02v-pKbrbaS9BK50BaA30WornYviDzn9jZ2049hq_8bpbDEdcT1WKVFGrOFfTs8kVq6iIA2Vs-MZfXVwiRqgNdigUqzGV8-BCz5Cm97GsQEbOaHD_l76TRcB4MNy25ChSRci7Xs9skwm7s7cT22pgjINxbE1Y8JJLpwbvLh59uURMsIpO1mKGfVu-KQq4FHW6qH5ep2ErnHUmMkrwazwcwnxcGg2BgwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAP2_SuzT4o8HAjzuGT6aEAmtk1kifKUrGw4E5Rlb5gle6YAcvxoGOhRwYyM21PS5Y3P8eM_TKmZ1P0jeV4tisVvGxspPn9MiRWTB0DhY7sYw6Top_6WKFu9opVPpxRXcNflmF6-8EfhqJHXVJN8BJk8WqQ825J0ZcCzB5yuq_O6eq9iuXx_yc4wvISCFqQ_NnKP9JkjV-rHP7nmsm05_4thJdow8pMBjPC3zQmjJmkdQ0S0Cxkw9qS_nOC_eUs0PqQthzfDlon7iOnn3EySDnPZ0ydbtb1Qs1k5ayN120wL5lysQVIf7k0X4IYY_CSKh1kKLTPNxHjTu-J9T7ChhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ_V_etrGfX7y_KWGMZ2OHhzQdWetYlZtFD39SYZPXxf0ddF_wh-KERjWdaeKfaEwipgVCkeaIkLgnFrADXoF1sqDkXalciAEkC9hxCMxtSBoetTs8FbCalCRb76bUoQa1WI7izA7OVZwCgds5rG-mdL9q20In7IXjCSNWN6ufuok2MPz_i-eLOm1DkBbJ1_hs877IVJ2IYIwuMJjHOQ1hz2jO5p7Qs4BrYBFfrJ8Qcbj893Lb1qoCaSMEmUqwPMpxlmzVvAe3sTg1w8736ggJsmw6G2J5hq5qWV9SPB2ykTpPp0NT2ujqA7NYE_-QMFdm7GFCG9hmF0VSnWUJxL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=pnYYOFK4y9NRx_dATbU2AoMAPJdFj8nPm3Zs5XRJQhGDkFYI7UGV9JtLgjBT6RKDXcrAvNkZzF1pGo3zuMEevA2Em_ktvieFGLMk5TiH0a3Kf8ZwE6C6GPhQEc6ZQkNQX51LU3byoBX6vzDretl5NfDYj9srREuVB1j9AMNIKoYdBAUn8o7K6A4f0eFayaFL1_GddKmv8uB24ynJ8SBjoFUUCq6Aa14VvJ9_r-n0A4BLbq9G5a0vhX1NWZYi1_2KMYTDf4LiqNm3ZgzwN0h2ld_p67HBdvJfMs88iAurlfVJJj3Q3KUcWsZifHSWLNtCBYt74OwIza5mZ0ATa9GP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=pnYYOFK4y9NRx_dATbU2AoMAPJdFj8nPm3Zs5XRJQhGDkFYI7UGV9JtLgjBT6RKDXcrAvNkZzF1pGo3zuMEevA2Em_ktvieFGLMk5TiH0a3Kf8ZwE6C6GPhQEc6ZQkNQX51LU3byoBX6vzDretl5NfDYj9srREuVB1j9AMNIKoYdBAUn8o7K6A4f0eFayaFL1_GddKmv8uB24ynJ8SBjoFUUCq6Aa14VvJ9_r-n0A4BLbq9G5a0vhX1NWZYi1_2KMYTDf4LiqNm3ZgzwN0h2ld_p67HBdvJfMs88iAurlfVJJj3Q3KUcWsZifHSWLNtCBYt74OwIza5mZ0ATa9GP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=iSPd0K-xBr_hin5snjZEfSjIgOpRS1sZmneVAbf2rqC0knCRfHLllRfWaneqtTImIIWNVWbiS8QfIGQ63pdIOjIPo1Rrvm_O1cmiZy_LcvaJ7pMSoFht_LwHkN3LKKch3E3g9XQhfHBzwxzQZ2P3EydsGtmrZaSCQho2OyqfC_7EdHNtUjzqX-Vys6XbTO354qVwpSYDy9dhV3mtLIZ7n57kN9lO1vz6Alpm5BZA-1NQNs_F4665qW-rVMBszndRtHvJT68SohA_ODWCVDpz371c1_rXU5kJe8CEs1t6FgMhvodcrRIwVOTudbqKe4lnAFSonpGajPGnoDT0d21H1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=iSPd0K-xBr_hin5snjZEfSjIgOpRS1sZmneVAbf2rqC0knCRfHLllRfWaneqtTImIIWNVWbiS8QfIGQ63pdIOjIPo1Rrvm_O1cmiZy_LcvaJ7pMSoFht_LwHkN3LKKch3E3g9XQhfHBzwxzQZ2P3EydsGtmrZaSCQho2OyqfC_7EdHNtUjzqX-Vys6XbTO354qVwpSYDy9dhV3mtLIZ7n57kN9lO1vz6Alpm5BZA-1NQNs_F4665qW-rVMBszndRtHvJT68SohA_ODWCVDpz371c1_rXU5kJe8CEs1t6FgMhvodcrRIwVOTudbqKe4lnAFSonpGajPGnoDT0d21H1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=t7NrXgUd34IgNm4sRvA463VAdceqBWdAN3rhxcLe-yHWcnkf87nTyRl0bxLYnPHETYhDvBngvaeoimCE2gyCxCy71_fqSIbmHrimrqAvx_FnsPhipRYAIEOT52c_teu4C2a-qFx3Vw6btHkF91mk0gnB4NQSwCNhsr8YTWpyF_hOmhOH4qkXrSpvSw_uA3BqlS-Q3aSfpvdg1rEdJ-8dpgh3v3tJTku8k7ni_qDVNuUt40wl3hqlnAg5QVUr2HqpSOUanQuJwkpcf-YvCrz91nBy8I-x7h24169u2EPBxCwnEcMfTTikeIYl1PUhCYkNIkZ1ij2AlfzWdIJmRQ0d4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=t7NrXgUd34IgNm4sRvA463VAdceqBWdAN3rhxcLe-yHWcnkf87nTyRl0bxLYnPHETYhDvBngvaeoimCE2gyCxCy71_fqSIbmHrimrqAvx_FnsPhipRYAIEOT52c_teu4C2a-qFx3Vw6btHkF91mk0gnB4NQSwCNhsr8YTWpyF_hOmhOH4qkXrSpvSw_uA3BqlS-Q3aSfpvdg1rEdJ-8dpgh3v3tJTku8k7ni_qDVNuUt40wl3hqlnAg5QVUr2HqpSOUanQuJwkpcf-YvCrz91nBy8I-x7h24169u2EPBxCwnEcMfTTikeIYl1PUhCYkNIkZ1ij2AlfzWdIJmRQ0d4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av-evXXpTzoGtnm26vJgdujpiQ7boD82rJ78OoRrxjATLKzNU515ylj0CDyJsyFQsAaN2ShMXHNUojIESXB37q4AErKFgRA_jtu7-udzRfhc2K0wpfJNb5qCwQd7YoFc4CsflFA0451GWDdr9ehfoD7uxCy-fjxjIoFwvYVJFxghPFI2gIEWIiBKst-qJHYeacP1hTIieIeVJV7XZonSCyKkiltYT41d89CYI3epiTNHfdcT1NLTncvQ_Xn9_odu_BrEqhOzKLp--Cza7yDJyJhUG1NDfnHzsC9bug1jO8X91j4McKphnDjav17vls7DXUYNgBKYuHOY1t0yldl2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JGQD50MK8Z9Jppz0vpr45BcvIQPTbyF4E6UFEgzXIQ8yNvkZaDLr38zaywfkoogZHYZGjZIM_RxjvXtbKn0aIQGJFBddZ0rmKMuCtdVasdjsVqUOWBvLrzQNrmZcAGT1CUHJAwGMDNzosNoiemdvngE4i_WBm2xwzmySREYuYqoly3rdLgS0YFylevKtUbfu8fPq6RH1VC3vJ3-Al5exQPFHlcNRekpnCfOkJcWmwWKLEW9SXzk_-V4_y8uwyqzqVyaXscQtMn-cooo40tma3CVAuBl0KD83_KI5kjckGsfTPGcR3F_J1VN7eWMvjj9dMaXedg_JOwoRZU4RIzuUGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JGQD50MK8Z9Jppz0vpr45BcvIQPTbyF4E6UFEgzXIQ8yNvkZaDLr38zaywfkoogZHYZGjZIM_RxjvXtbKn0aIQGJFBddZ0rmKMuCtdVasdjsVqUOWBvLrzQNrmZcAGT1CUHJAwGMDNzosNoiemdvngE4i_WBm2xwzmySREYuYqoly3rdLgS0YFylevKtUbfu8fPq6RH1VC3vJ3-Al5exQPFHlcNRekpnCfOkJcWmwWKLEW9SXzk_-V4_y8uwyqzqVyaXscQtMn-cooo40tma3CVAuBl0KD83_KI5kjckGsfTPGcR3F_J1VN7eWMvjj9dMaXedg_JOwoRZU4RIzuUGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=iVVc5sGXBeFQzX5y9yqR1eXnI687gS4mET0gHPqltHHnOujaG49awrGRbWHBuXZq_dYfQ76-Lk38bZLjYwTcOeucJLlm2gEFJEvW5_nAqs-6mP7JR5s8Rf7oqHaU_CI95QQKwpWo6wmFX-_AcMDM3rXZ63QzaVpq_ud0ehsi8zDlRvMIBa_szJ60pfuYMCTXzttlNVtKBLKR8MdbzM5zaYX1n8fraCMlNf1F4yGndJCG_RDq8p4iGyI49Xw-cYIhSDxiX7l8RuYN83odCY3wW9f1tQQLSP4w2dAvR701wPAst1sYjXfF_jrQ5-adAMaUY_zTTWe95ZBkKAjYV-Rd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=iVVc5sGXBeFQzX5y9yqR1eXnI687gS4mET0gHPqltHHnOujaG49awrGRbWHBuXZq_dYfQ76-Lk38bZLjYwTcOeucJLlm2gEFJEvW5_nAqs-6mP7JR5s8Rf7oqHaU_CI95QQKwpWo6wmFX-_AcMDM3rXZ63QzaVpq_ud0ehsi8zDlRvMIBa_szJ60pfuYMCTXzttlNVtKBLKR8MdbzM5zaYX1n8fraCMlNf1F4yGndJCG_RDq8p4iGyI49Xw-cYIhSDxiX7l8RuYN83odCY3wW9f1tQQLSP4w2dAvR701wPAst1sYjXfF_jrQ5-adAMaUY_zTTWe95ZBkKAjYV-Rd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC3_JxbXGqKTUz_-sOOIdPEcLtDdhvWYQydlhVg_6fTVf9gCqItna8H1L7uuRasH5zQFIXnyISzT1j8PuSCzYIvJqKTFcvmnwWS-9HnOTOJhopay2UhEQO_zwvda2SftcV2jSr0NHFEtokQOfIwwnPaQjOIh4KVWjJG-0qrfr8bqvJOUtl1vauK7DC1tqJnQ6FXoIGus4L7Co2SnT-zgs7TrijI3_TlXCtBGc5tNbROU0qoFu2L6dxZgVehSNyTgHP-Qwiy6i5m7U0uDehJqirThCDeqM4B_va4QG7_lxMGfurzo1g_QLfgXDb9vj5Jq7hnPhihMYLRjb5MJ2QQsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=F80YAteDkrotsMtx-s8S8lkcerB5rtCwWCBu1fFQYowuKChvg5Su5sTnKi_z-uMdkGFiF6SpWNJazdE2Xt8LTnQwPyd1tYpvOctv_gvEYQltK63kDrXRjdSXFrPbh-8As6fOcZBbX0SgoF2R6zeg_OZnrKybVzxDlcN89jN6ysycIsu76ZHTJHegPtn9OjzPO7jMhQ3X8fSrnxLPnXzZsyYyyrIWuwOgOyGA33yjzHptMfHel5RL-au-RyVdy9WPnSYMesz4BTUrEgWRvUdC_A6cJGcVB2zTCsX8Z7Tg8NwH0td8_cjzzc-MKV8Va-QGTPMtj1udMIDXyKM7SP0aLDMs_TwBHyZ7_bmKdUYerpMhuTBIn4-FyEPAnMbVPemWrAGiw4yJsOMRuNKMi5By75GqfF_UFN-R2i0ZZNNujFMaSOvfEpk3AxgzCseD8SgL6ZgOlwqnHoQkWociEetCKekIFWWfWR1cE8hUWbvKPIhdO6olaN2X3HP4a4H0fbg2U_tP-mQObzac8DUovvWdyIj_BVsQMYeGlXRPYBzBixUUShcsTR4HIoWTzyl5Fz10DyhtpllFPhUq4iwSWdGEW1ymhZT4caSNhRDzT2OQAv7CuPPlC0AmQ162vHLRaTFnOwzXXTZfrRNPLYQkeQkikFAgQi501RftGw_ip8UMpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=F80YAteDkrotsMtx-s8S8lkcerB5rtCwWCBu1fFQYowuKChvg5Su5sTnKi_z-uMdkGFiF6SpWNJazdE2Xt8LTnQwPyd1tYpvOctv_gvEYQltK63kDrXRjdSXFrPbh-8As6fOcZBbX0SgoF2R6zeg_OZnrKybVzxDlcN89jN6ysycIsu76ZHTJHegPtn9OjzPO7jMhQ3X8fSrnxLPnXzZsyYyyrIWuwOgOyGA33yjzHptMfHel5RL-au-RyVdy9WPnSYMesz4BTUrEgWRvUdC_A6cJGcVB2zTCsX8Z7Tg8NwH0td8_cjzzc-MKV8Va-QGTPMtj1udMIDXyKM7SP0aLDMs_TwBHyZ7_bmKdUYerpMhuTBIn4-FyEPAnMbVPemWrAGiw4yJsOMRuNKMi5By75GqfF_UFN-R2i0ZZNNujFMaSOvfEpk3AxgzCseD8SgL6ZgOlwqnHoQkWociEetCKekIFWWfWR1cE8hUWbvKPIhdO6olaN2X3HP4a4H0fbg2U_tP-mQObzac8DUovvWdyIj_BVsQMYeGlXRPYBzBixUUShcsTR4HIoWTzyl5Fz10DyhtpllFPhUq4iwSWdGEW1ymhZT4caSNhRDzT2OQAv7CuPPlC0AmQ162vHLRaTFnOwzXXTZfrRNPLYQkeQkikFAgQi501RftGw_ip8UMpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8h07SDZCghdJ1L3mDdCIGltfFvcCZwupC-1nVWzT8fBeLyr5QFgsZSQSyaXKf28tFa_uansJ1dh5O0bYn7xAFFU-m6BG4m0FHVL9uTGIEdyVN1TMRiP9Tgdm2iAZloGgyKy5frDBnyCqz79KCBnEgDdEfvnAym1tKngHgvGDi4Y25HMyzhmJKl8_XZwYKbe0le-oQ6h9d1a0DDHcdGTMs0yaqqvUak50dTELJL5oHj7KR2AmDXTXQzKXScs0Q4LVnCGvFWsTLCefbj__ZH-8tcdI8dcFCR-CrqbuNM0usoVq5t0Gw0hYIIs4e1WDgaBHQuB8iFzAnn1_BTSsecMpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=E1CD7FqnfBD-WEx49GI3eYsYg8G3gXVsde0BJpBapxtd1bY64KNUAj-xk_GmnVqwVaWUCcxJJqYv8tTjeT8f3FnJMvsvq69PEcDysdWdLHa54OfXejpk3X86qW0WLdNPq8Abnq7iWFzZRS3PLZqADp2jQl8pbAWnQf83BZFa4qmH6FoVeHoyRCVGoomhoAgXNLFznUfheVN3p9BoUjbi-EKpYobPwcsVTTptDLUsuOAZe8at_C2PR33yFF33vFRKweoTf1d92nLTYDfkAJeL8GfqWtHrjBUgo9kUJ20ukQEg9lGl1T5Fb_-JVj2MhI0iMEpRYTWPSGCWIMaSsyOhlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=E1CD7FqnfBD-WEx49GI3eYsYg8G3gXVsde0BJpBapxtd1bY64KNUAj-xk_GmnVqwVaWUCcxJJqYv8tTjeT8f3FnJMvsvq69PEcDysdWdLHa54OfXejpk3X86qW0WLdNPq8Abnq7iWFzZRS3PLZqADp2jQl8pbAWnQf83BZFa4qmH6FoVeHoyRCVGoomhoAgXNLFznUfheVN3p9BoUjbi-EKpYobPwcsVTTptDLUsuOAZe8at_C2PR33yFF33vFRKweoTf1d92nLTYDfkAJeL8GfqWtHrjBUgo9kUJ20ukQEg9lGl1T5Fb_-JVj2MhI0iMEpRYTWPSGCWIMaSsyOhlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_PU8BlKUDENRxYic1rkG6NRtoJdfPyyxOv-ywGmZMTmcsqSYZAX_3oLbfEKyGS8L8aIYjz90HBhGmaNQNjVIMuSr6jkwI8BFydKIgXdjVirijWqSZxZoxubE_OuwMKgbKpsYZtRgto8LOTsM7G1jxSiHLZ6yM6TLEVjUi6nC1zP9YZ3B9NzaVTxGNDQWXGmInYtEPYNfuxe_5tRkcmWv_qA4rCWAWI5t1ZeK5HnvWTqYNGIrq2LpA23dzAywXAHE6GB2nKFA2RqZK7wJAmJWBn-P0R0Zp9jrcKGZMAT_mwVgikKi-_UaNFDw4CUgzXXKMQs4I1ft0NbNlgBbVECGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-veMVy6cbTuqcOpwBpr7hnGBCMxjwXaqeq-MgRK8bN5knAu6DkBVZ0Rs3MZ4jyJY9wX1MXgRVaxRHug5cMwg6E3XuKT_riUIkrZK4Don6ATqFxWkxhfg4otGzxPIs_eyu5Ke20bG8ya_A0oK6W_jOOLnE7tXQblaeh7WYe2BdLWCZoY11gNsKg6EyZLN3hzFtBcmlFBW_zxdJF1yJXmnagfFZhuCq9vJsmlqN4cVIUM-Gkdlz2S4zO27BHcdV6VlOKTA43CFfcwQ6YTT1SE6FSs_Bi7dAmXIdkilRzJ-SxbPuQ9FE54g8s9skzxTIk7TPROk2Cu5Sob5up3MbUorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuiH1lCF2Q7dCYdoQX5YwmfDQJp5AEMgB6dKw1eKDAxvUeyMP9tF_6dn7q1niF9k99MlA2J1iLKWok2ZsDvAMWHotdefapQ4TVtaNhJyh5ybejVFW8pa1QwokHB8f2dE2yODgM6pkJwF5Xs57CP7sGKKGL5Kcy5xcWT0fkYewv8nCP6N3hKcfcjcL-gnatLB1QG8Vm4huXDrlAnqmq4J_cipCfg__DYrH4zv-ldhXWb48n6lY9h2OwlhSEO_mVwqoHVutKL7eIGP7yguahhXWZKKpjmBG_e561vQSSY2l3MPyhjBNDpTrJ9PcklOQPchbDobYJcZxhnwgC9vIt8ieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=KAdDhuH-kZyiDxtIDHs2O9dxmKeWnLYpXQCGYJtRsCGEUxZG-8iX32zDASwXh3Xp0aG26_QsJZA0CrNiwJ0v0-7VlrKQJURikGU21UxW659uK45dcYo71andR6yZidMhUEQVXR6z-QjlOS03Mg-ehA4FyGIYV8Y2AbHjauJyaKRT2W3gmBMhYfrv8aKdh4sOghz8Jcj45gZJmVlbSju-gu7XNsPgaedG5bd_q483RM6OIC77yU7L1OABtrJajDYYwCU3D6CUWaeior2lPamYWgbYXUuwBLshfXIzbqdJQbdmeuoYz0HA0QN3NGMODT4imMoG5-jl1LBIhZvnRcz-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=KAdDhuH-kZyiDxtIDHs2O9dxmKeWnLYpXQCGYJtRsCGEUxZG-8iX32zDASwXh3Xp0aG26_QsJZA0CrNiwJ0v0-7VlrKQJURikGU21UxW659uK45dcYo71andR6yZidMhUEQVXR6z-QjlOS03Mg-ehA4FyGIYV8Y2AbHjauJyaKRT2W3gmBMhYfrv8aKdh4sOghz8Jcj45gZJmVlbSju-gu7XNsPgaedG5bd_q483RM6OIC77yU7L1OABtrJajDYYwCU3D6CUWaeior2lPamYWgbYXUuwBLshfXIzbqdJQbdmeuoYz0HA0QN3NGMODT4imMoG5-jl1LBIhZvnRcz-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj2Eisy3bJhk5sWgrualYDDjluQSjKYwsupGCT9CbLhP8OA8DdkF2DCpafU5UlByz14gxQ_pUH8YDwMvZRGozDsFpP7owSe-K02W4XlJvDWkawhC_Fc4kyrf_fILuDy75-y0ejI1JwmNQ1vaKGKwcg7J1YaYlKQK9pQup2yStBauUYe_PjaouX_cZSJSft1Yyjw642pp-HrqJd_nOn5fP8sXDmg1QFg3tqAYr1VK1AtzD9rgsjDgXmNPYplO8kxSZCdZxRTNL0__E-fStMsu3bY1NDQIV2v_BBPmcm_gNQApH_9PqKszam4kUFdqmocDYhkCNVzeFa1UbPu_bJVI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1lLFqwZSrz6nmJy069CCh1Aunna7z-Is-Iix4GBgTU4yB9-EEAdWmZNSPalPm4BqV0ypccyzBJvMEoQFbJsHCDFTXEIGOBAWIna0QGCrcYxAYOFcM0RRlAsucomIE3XxeibcA_JMBGMUfqtd0cVXfu_o2-2DaGBnQImu44bAq7ZGz7ywKlc7kyomi3bbOrf9XYK75B6dCwrTzFPMdqxNgXiWEBfMeeUxKBpG4RJDBwdjU770YZdVVvdHPNxkBdhyBvenytP1HZmT4JzjPizQFZGMBA9M7yUPZLDs67YUelpRZiMFDI7DrqKGixj31lLt7bL5Ju927tyay8yo1QlsQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1lLFqwZSrz6nmJy069CCh1Aunna7z-Is-Iix4GBgTU4yB9-EEAdWmZNSPalPm4BqV0ypccyzBJvMEoQFbJsHCDFTXEIGOBAWIna0QGCrcYxAYOFcM0RRlAsucomIE3XxeibcA_JMBGMUfqtd0cVXfu_o2-2DaGBnQImu44bAq7ZGz7ywKlc7kyomi3bbOrf9XYK75B6dCwrTzFPMdqxNgXiWEBfMeeUxKBpG4RJDBwdjU770YZdVVvdHPNxkBdhyBvenytP1HZmT4JzjPizQFZGMBA9M7yUPZLDs67YUelpRZiMFDI7DrqKGixj31lLt7bL5Ju927tyay8yo1QlsQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=SQQ7XurHL12GNGQQzoLE5PmbWbUZm2ycSoK4D5EjhACLhd8PdVo1qx5lY_boLg4XCxWGQQPMMjbz8F8r-X-c49cCytgO6CmfRosFNnyrgOvaKz0HbTfpJzBYmTAWxOGqyZw8ojKlbtC9sRw3g4RwL7hiEYdEj1G92o6a3uiqcANQbRJuGPAsycmtNQhjHiq051R8vSsG1g31TO8yJYbWg93uEaqX51Y9I1nnPCacIpMj0-uyAQd1AjLDrkcZ8BptqWaaIGiUmTZuyvKt29hTH8mkujWqRqyP2mBKqyo-cuTnels7nlH44AduazHU6hlQrbSjKvjcTPzA6nXP9x7DiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=SQQ7XurHL12GNGQQzoLE5PmbWbUZm2ycSoK4D5EjhACLhd8PdVo1qx5lY_boLg4XCxWGQQPMMjbz8F8r-X-c49cCytgO6CmfRosFNnyrgOvaKz0HbTfpJzBYmTAWxOGqyZw8ojKlbtC9sRw3g4RwL7hiEYdEj1G92o6a3uiqcANQbRJuGPAsycmtNQhjHiq051R8vSsG1g31TO8yJYbWg93uEaqX51Y9I1nnPCacIpMj0-uyAQd1AjLDrkcZ8BptqWaaIGiUmTZuyvKt29hTH8mkujWqRqyP2mBKqyo-cuTnels7nlH44AduazHU6hlQrbSjKvjcTPzA6nXP9x7DiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=DkyvYXn2WXUbmp22HJFgevoTIqgTsIaSG0OqJn1tfnkymYpOPQATdNWqTMZ5zLPQkbVSnxE0kUdCwlVueiVe5FlOxPNLsnmxuqdpbTRqaHD3oFWP8jORpZ6O0vGcwyX-CyMJLrW4GqbMNNaV6ELWqXTqLX6VPFT3N4aIexZLpeUYIyg0k5lwmioygDu9CbDHUA9lbSyurpBZl-7h2D423mV52fa5B0H18o0eXeLN1Q39LcGiQmAsXDsEuFqWAWsi_fkmsiKn-7mAM8d4Qun9Sg72BYFYmaCGPhkdBeQPFj6Y0caQXlIJymZOnRtyLcoOV4I2OcmjnNs2b6IW6rFhhINgzobgHtgNZ8l3AOajX7DfDgU8baxZvuKKLghcP2awhli5M2pns-ICmd3S8sGdEt6pKdHUkAK-UCr6WW5YiKb3jqPmrg1ZESdKfsJHhaLeQuIieBPGTfyGqY64H-lXVg9G3Vmd7tZaFTzAuWyL16x2HknjB40oL6ewhBty6Q0ls8rR6HJT7S0oluVwww3sfHXGGnlsdIVzXgEIUKjYYuNCA2YC8N7Q9hgf-ELtS6LM2KlO5s_Ul7RKOG9Nud9nEuGq6U-hQrXbFYTfmCLQfscNVLlanDnaWCImnRE1XwfrAgarFSULP8r51Ukww7hyVuX3uTrS4S0oD9atmc7v6Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=DkyvYXn2WXUbmp22HJFgevoTIqgTsIaSG0OqJn1tfnkymYpOPQATdNWqTMZ5zLPQkbVSnxE0kUdCwlVueiVe5FlOxPNLsnmxuqdpbTRqaHD3oFWP8jORpZ6O0vGcwyX-CyMJLrW4GqbMNNaV6ELWqXTqLX6VPFT3N4aIexZLpeUYIyg0k5lwmioygDu9CbDHUA9lbSyurpBZl-7h2D423mV52fa5B0H18o0eXeLN1Q39LcGiQmAsXDsEuFqWAWsi_fkmsiKn-7mAM8d4Qun9Sg72BYFYmaCGPhkdBeQPFj6Y0caQXlIJymZOnRtyLcoOV4I2OcmjnNs2b6IW6rFhhINgzobgHtgNZ8l3AOajX7DfDgU8baxZvuKKLghcP2awhli5M2pns-ICmd3S8sGdEt6pKdHUkAK-UCr6WW5YiKb3jqPmrg1ZESdKfsJHhaLeQuIieBPGTfyGqY64H-lXVg9G3Vmd7tZaFTzAuWyL16x2HknjB40oL6ewhBty6Q0ls8rR6HJT7S0oluVwww3sfHXGGnlsdIVzXgEIUKjYYuNCA2YC8N7Q9hgf-ELtS6LM2KlO5s_Ul7RKOG9Nud9nEuGq6U-hQrXbFYTfmCLQfscNVLlanDnaWCImnRE1XwfrAgarFSULP8r51Ukww7hyVuX3uTrS4S0oD9atmc7v6Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=PKlXhExc1E7SbAiZtpQkdPNE2uWU_5zNMAz56A81bSz_hWFvMCM8sEWtWOEQoK6O-sVI6ycuDs-UG1t4Vw37fgiENF0AUey0qDQWEQtY4cS7Qm8bfRT3kQCBzQerY96wIOObOiVT1qdUA-_x5r3PnB-y-W6ZYihAA2dAFDkudAgL174sWstbOzMGtfmE-q4caBPLMg4P1F6FUmF8l-T50fyykpoQttl-hH6tLdyMK_PgQ6cLmnilCsVlVkIL1NpHGizYJgO0TUbp2lMmXBb1VEfWV5KWimacn06EvsQAf1T1aQk2aFQppoda_f1bqnHaBqz-U5kM31FrQTEJQHBcsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=PKlXhExc1E7SbAiZtpQkdPNE2uWU_5zNMAz56A81bSz_hWFvMCM8sEWtWOEQoK6O-sVI6ycuDs-UG1t4Vw37fgiENF0AUey0qDQWEQtY4cS7Qm8bfRT3kQCBzQerY96wIOObOiVT1qdUA-_x5r3PnB-y-W6ZYihAA2dAFDkudAgL174sWstbOzMGtfmE-q4caBPLMg4P1F6FUmF8l-T50fyykpoQttl-hH6tLdyMK_PgQ6cLmnilCsVlVkIL1NpHGizYJgO0TUbp2lMmXBb1VEfWV5KWimacn06EvsQAf1T1aQk2aFQppoda_f1bqnHaBqz-U5kM31FrQTEJQHBcsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoStUCrC19BVOtNt7x_oE9CeONPBki9WGLxenJTkcnBecT8iz6cFYgeDHC7oaXlaWao15RU14u9103-0G-bBwTR1K3swqbqmpQ4l5DBt9G-hH7I7uAsriTN2YuZWF-m3hwHl9JcGFZZxKr9dag96w9NWrjw9jHaMvNSS0md_d3LOzy3nJOTai0VRsKx_Pb26TeZzRe3fV7jZyEwpxhZiL-wzxybxwqb03Z84xGt-CASJS1LLbB9B3QgWtWJUzOFxPcaIpoCEg-S6WyAFYsQwAgPJYzXgeZyYlciHyN55dZUL6Ze_-VTStQGJ3LUEE8xa7hoBAemK4ze_4u5iaKshxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=j-BP7CIvLkfEeFNoPtgq73CsGRpTNDvXwYtXP8eWWhIVhcJthfSjUJlCE-9NdwW1Mnp7Uz3nwdmu8MiI77Z1JPGn8kM_pP55pO09DXQGD1YXjhTQiM_a7DmJk7SIBCuVOrc4tP2y_YSAPm1ASXCjX4tHRGxjjIfEIFHfxFx_maPGQUfUHlVLBiPKiJ5VcyLxPoisRDpkpvk9rVsTlpLMfYHHSpXCIa8vGvhbaXbgf-iX0KXnrPQF5EiwTUjvOj47Hxf_YRB5uF-mkNLu5w34jvBSR-cSiGwoM3t4LKfPTd-kdkzzisZE2klOGZrWnw8qwM_XSEwOJFNHSAViu6n_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=j-BP7CIvLkfEeFNoPtgq73CsGRpTNDvXwYtXP8eWWhIVhcJthfSjUJlCE-9NdwW1Mnp7Uz3nwdmu8MiI77Z1JPGn8kM_pP55pO09DXQGD1YXjhTQiM_a7DmJk7SIBCuVOrc4tP2y_YSAPm1ASXCjX4tHRGxjjIfEIFHfxFx_maPGQUfUHlVLBiPKiJ5VcyLxPoisRDpkpvk9rVsTlpLMfYHHSpXCIa8vGvhbaXbgf-iX0KXnrPQF5EiwTUjvOj47Hxf_YRB5uF-mkNLu5w34jvBSR-cSiGwoM3t4LKfPTd-kdkzzisZE2klOGZrWnw8qwM_XSEwOJFNHSAViu6n_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=edix4ofLLtjLdvFW011CFbkrBAXTHLzY3G9a8Sb8EoItzsEGJihFjy2B4lHzGJLqxa8AE_oqodeecX0Ek8WwcGF80LFJsPQINr3m2Hag_dCKbUWi66zpXjapZMs8nx42Pqveor3qT3iWT36q9LNN1GAw9Xu0CBM3kmmg30jrL3X54ofwEtFtky2dndJz906UEut6ChTkA65nSI80kEmXHH0yniQzXybtqag7QHu7d4emz6Sh-xCO2-Ks_RV8pZ3fNSviYaR0BALnAWf4C3r-ca4FlGcQODs0EIRTvC_HImsDrMXhH4C9Ye4R2RHYym7Cp49Wyqu7zXsG8nqS6-B9aqk_RdaCs7xy0ogBkzaXUYznvdB45DpPcYgKyvOiOlnDbhmT_0r3xQQxG5F-RxcO8qMogbjKns9OC0Mfv4vYuuOisz6pgDQu5Crcf3GiqwnJG2S8KSlP28ModMzBu825vWPym_-Ins1j4s17AbjrGbuGayI6lxZT__3Z6FjFUfzMXaoPKqTxZeBQHH5EuiX0_ZtEMtO0jiHo044d-QrvXm2VZSzQAU18yidE3lqQMAlawARTAUmD8XLnqa2LSBNiIAMkmI9C9ehnMHXOv4PMbRjM3oNK4xcPg3y_8V50tXkGtq6kJklaCnl10sDbSf4gxX5Jue_N1QooNkPX1RB2wR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=edix4ofLLtjLdvFW011CFbkrBAXTHLzY3G9a8Sb8EoItzsEGJihFjy2B4lHzGJLqxa8AE_oqodeecX0Ek8WwcGF80LFJsPQINr3m2Hag_dCKbUWi66zpXjapZMs8nx42Pqveor3qT3iWT36q9LNN1GAw9Xu0CBM3kmmg30jrL3X54ofwEtFtky2dndJz906UEut6ChTkA65nSI80kEmXHH0yniQzXybtqag7QHu7d4emz6Sh-xCO2-Ks_RV8pZ3fNSviYaR0BALnAWf4C3r-ca4FlGcQODs0EIRTvC_HImsDrMXhH4C9Ye4R2RHYym7Cp49Wyqu7zXsG8nqS6-B9aqk_RdaCs7xy0ogBkzaXUYznvdB45DpPcYgKyvOiOlnDbhmT_0r3xQQxG5F-RxcO8qMogbjKns9OC0Mfv4vYuuOisz6pgDQu5Crcf3GiqwnJG2S8KSlP28ModMzBu825vWPym_-Ins1j4s17AbjrGbuGayI6lxZT__3Z6FjFUfzMXaoPKqTxZeBQHH5EuiX0_ZtEMtO0jiHo044d-QrvXm2VZSzQAU18yidE3lqQMAlawARTAUmD8XLnqa2LSBNiIAMkmI9C9ehnMHXOv4PMbRjM3oNK4xcPg3y_8V50tXkGtq6kJklaCnl10sDbSf4gxX5Jue_N1QooNkPX1RB2wR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGBRiUhT_nyRd4kzQe3hIWkjqSZSMP2o_dmz4306boQE_CoFldGXXk3uNlgYB3lE3X5-2TxP0eNDipiGh5t9isLIW7-DPuCe6thGyyXU29zZwEjmkFZz7V325_RL0oBGLAvEgIQRKFjM6sM3wyFQrxFaB1IpVS4FnHYCyaWHA38WEInEMSLeungeq798UsZH002QBpou8sT2dcbN5pSYIfgs-vCOPSDyYxsWVaMwaTDlgAgDA2WcgBl0T3fQ2mOoay5i6Zftf8a0_1Sz0hPCN0XNcjWWq9bPsyzf2R__8CsJDo0RAUEUJR9Z7YlKqNvpoYfIDdvcEd7qGGt996ATYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=lmaT7xpSBIJQj3c2sjV8JEKQ1bt_tZjqQuuzJI_3YcLdT54fh25-Jqq3PDN4I_ZxYwRZqQGmS0-qnHkSXCHU_1T322SpA1uoCLH1jyrwl4KU1Mwjc4aeFOfni7aReKAWoOfcc0cXYX5mqJ0hipOo-v8ECrZuqFKS_L0s0q3M_Eqns_UZZ70OZFCo5RFNVbjyvNMDLtZ9NR34Jcl_qG1uQMJ-b9WpzE-2iOokUjE4J2MJrCKhT6K7T0CPUeRK-KW5gGx6g4ajQURn-xuPs1mvfnq4tTOwFx0cHbjj0zqRbPX2_8G2ad0RoxkSglDmjo_ZgnrsHCvdNk91M_5Td0Kp3ZsnUneUyDeS7zCUhm76hbX0GzLfZ6F4yaQNpC8RyVwGWehLsPGWbGHG79H62pyLh1fqmQmh8E7nJL65pndGwqnvkTtH2u3pICRTEkN44nDY1V7ZQ8P80M81mv7uslK5Scz1NftCjcQ7KEzwtOXqR_qKPVPbIeLh2QZlO9lj5Vsms7ZHvh9ykJArvdi93vmx0nAZ1VDWu-jpjRa2aN1OG9TiGl6S42NUs9bbTzFSjHLIhAPfP1Zu0SAmasZf9OuD6BHqMUMsp0UWIml88-m27Xs6bVRrLhXTEHJba_U7fQGQQLj-YPcoes1CAzTbDLUAoaL9i5OfHheE_Z6G4H7rrkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=lmaT7xpSBIJQj3c2sjV8JEKQ1bt_tZjqQuuzJI_3YcLdT54fh25-Jqq3PDN4I_ZxYwRZqQGmS0-qnHkSXCHU_1T322SpA1uoCLH1jyrwl4KU1Mwjc4aeFOfni7aReKAWoOfcc0cXYX5mqJ0hipOo-v8ECrZuqFKS_L0s0q3M_Eqns_UZZ70OZFCo5RFNVbjyvNMDLtZ9NR34Jcl_qG1uQMJ-b9WpzE-2iOokUjE4J2MJrCKhT6K7T0CPUeRK-KW5gGx6g4ajQURn-xuPs1mvfnq4tTOwFx0cHbjj0zqRbPX2_8G2ad0RoxkSglDmjo_ZgnrsHCvdNk91M_5Td0Kp3ZsnUneUyDeS7zCUhm76hbX0GzLfZ6F4yaQNpC8RyVwGWehLsPGWbGHG79H62pyLh1fqmQmh8E7nJL65pndGwqnvkTtH2u3pICRTEkN44nDY1V7ZQ8P80M81mv7uslK5Scz1NftCjcQ7KEzwtOXqR_qKPVPbIeLh2QZlO9lj5Vsms7ZHvh9ykJArvdi93vmx0nAZ1VDWu-jpjRa2aN1OG9TiGl6S42NUs9bbTzFSjHLIhAPfP1Zu0SAmasZf9OuD6BHqMUMsp0UWIml88-m27Xs6bVRrLhXTEHJba_U7fQGQQLj-YPcoes1CAzTbDLUAoaL9i5OfHheE_Z6G4H7rrkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Q58zCOO7U07mATtjgQLQUEbX-IwLplazJmzIb45YeU_s3pWR_tZ_c3XG3EqjkzyLDNn4JLHwMl43yreRyPt72gXnr9OPKarhmRW00P8JH1fn-1LDkQjNTELEaziqobZMfVYTiwAQgf3GA1Jk_L5Ng-zwq_R1RiWkcr-EZq5_H9MajRUt_tDbxfvtEpSksarRMmaprQ6aY27BNDcVgxx39OcEq-uHf5eAsqR6E9UdAeXjKxnqxquCoNrFzaeS6rPOtrBKxVq3ug9mYBUFojJyArJ3HRMi6jE59qSq8cRB_jV1_AqO-ikrWvOCc-c1ijAEGkkJu9D2hI27h2ONipcGvlvLC9MRCqgzQceODmYxMxsBbRdlCjjkV0FAbxUuCBL-cZ_B9SIyjDD2PgZg1aMUTXQSaJJEJ_dGVnmgBEE7oQTtHfy5ecnH_Jif2dkqMPo6sxZNDFNSO5eC3D9wK1l_A0BcFfpYzfco5PgXzxASbysEtadtESZlQgCx-nk1nwpDuwvnkRwc5viVd4d52TerBktWdhbDXuu-5DSRVVilb5dHsKO7kcWnqRh0LX2X-cG_gE-mu6QIVqGWXQJpdZKxOjgtPolGcYgIO7Z4kTJBTdnyddYprPZSUkYVWfOEOtDcEt6I3xBvSY94op2Ce9NuaR8VVODArtQb-A8v6m1IdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Q58zCOO7U07mATtjgQLQUEbX-IwLplazJmzIb45YeU_s3pWR_tZ_c3XG3EqjkzyLDNn4JLHwMl43yreRyPt72gXnr9OPKarhmRW00P8JH1fn-1LDkQjNTELEaziqobZMfVYTiwAQgf3GA1Jk_L5Ng-zwq_R1RiWkcr-EZq5_H9MajRUt_tDbxfvtEpSksarRMmaprQ6aY27BNDcVgxx39OcEq-uHf5eAsqR6E9UdAeXjKxnqxquCoNrFzaeS6rPOtrBKxVq3ug9mYBUFojJyArJ3HRMi6jE59qSq8cRB_jV1_AqO-ikrWvOCc-c1ijAEGkkJu9D2hI27h2ONipcGvlvLC9MRCqgzQceODmYxMxsBbRdlCjjkV0FAbxUuCBL-cZ_B9SIyjDD2PgZg1aMUTXQSaJJEJ_dGVnmgBEE7oQTtHfy5ecnH_Jif2dkqMPo6sxZNDFNSO5eC3D9wK1l_A0BcFfpYzfco5PgXzxASbysEtadtESZlQgCx-nk1nwpDuwvnkRwc5viVd4d52TerBktWdhbDXuu-5DSRVVilb5dHsKO7kcWnqRh0LX2X-cG_gE-mu6QIVqGWXQJpdZKxOjgtPolGcYgIO7Z4kTJBTdnyddYprPZSUkYVWfOEOtDcEt6I3xBvSY94op2Ce9NuaR8VVODArtQb-A8v6m1IdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=RKGaGppZPTimVHXgXvJFnxJjRN9AscRHaIdIUHIwbf8Jf_qL2c7V9Emgw3-Qg68RXzIE3vml3nPufG07xGPMgWP1pmDl6DB59DvFXr6wk75g0Gb0AItx9r_fRZqH7oJz_BmUqS2q7X-mpIlSsd2c5tdRJHMPACfZlcDb0IpVoH9bBri0kFbr08HcTsKMqfnup1OLcM4Zqj8ETgWOi5wwtB7Lhh0TMOnAohb9LsDzsonilS4VQsw4Amqj5ROe60gult0HCVzQtrulL6uNWQgXT0OshIKY5ZpV98vw7gOTjphQ2dMmcG28Z18QwxZHTc6u_k8_ttRRbmkA2TfAbMtWJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=RKGaGppZPTimVHXgXvJFnxJjRN9AscRHaIdIUHIwbf8Jf_qL2c7V9Emgw3-Qg68RXzIE3vml3nPufG07xGPMgWP1pmDl6DB59DvFXr6wk75g0Gb0AItx9r_fRZqH7oJz_BmUqS2q7X-mpIlSsd2c5tdRJHMPACfZlcDb0IpVoH9bBri0kFbr08HcTsKMqfnup1OLcM4Zqj8ETgWOi5wwtB7Lhh0TMOnAohb9LsDzsonilS4VQsw4Amqj5ROe60gult0HCVzQtrulL6uNWQgXT0OshIKY5ZpV98vw7gOTjphQ2dMmcG28Z18QwxZHTc6u_k8_ttRRbmkA2TfAbMtWJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=RpaMavqqxa3TpfyjmqQD1l3h7RiB0vkyXMgj8Kxfukzc6lyvGn3DBZxFTdYEOtXO5En9s2fDrqwdVig_PKXk5t85EbrdXxKn_oCVEPbykklY1vF9E1cGztQIdEAZlbvi5CiCMorOtjZTNxXwqhHpIx-XyA599qLCxlxLARGdWeuXmJMCh8whfY4Y2jKNgRe_watHCuY7aerJ3fEyOqcoTPnjc-QxCQ_R1R3h88KPGw5euIk69yIhYnQJIrQyWsb83VIYUqIdQC6KyOOH3RRB4zjE2GkukenTMdIx2w3xnxdHCnN8J9YaR2kOlb1-XU-gTe6kylEMCG7rgJDoQ_taUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=RpaMavqqxa3TpfyjmqQD1l3h7RiB0vkyXMgj8Kxfukzc6lyvGn3DBZxFTdYEOtXO5En9s2fDrqwdVig_PKXk5t85EbrdXxKn_oCVEPbykklY1vF9E1cGztQIdEAZlbvi5CiCMorOtjZTNxXwqhHpIx-XyA599qLCxlxLARGdWeuXmJMCh8whfY4Y2jKNgRe_watHCuY7aerJ3fEyOqcoTPnjc-QxCQ_R1R3h88KPGw5euIk69yIhYnQJIrQyWsb83VIYUqIdQC6KyOOH3RRB4zjE2GkukenTMdIx2w3xnxdHCnN8J9YaR2kOlb1-XU-gTe6kylEMCG7rgJDoQ_taUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=hIH7AthEXbyrPlqUsUsbfa_hLoq7XEoXmWICbS4CLMs-_2ijgvx3O4IbKl85l1mACqeueaLOsxb9t52Bj63loXYHsIwnJM3XaN6dWyE6lEIbEV5b1fZw10C1e7eDj-ipcI4U8uH7oBmm0YxUIii3vT-he8lBnZ4k_oKEzwzAJXboppS1Nn4EbI3aAv2W5zkB7OxELHthI3xLRXolq24_JkgGX69TD9nmNfQLMs2BtzvHeKtWGNaZ2wwOKVPNzH7Hi6osSUGvq9QkuOMP38dv90PM8AbuE-JL_Laea4-DVFuMUVsWaQ8SUL39lIVn-i0eGb4Jqm4kRSN_F2bN8farVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=hIH7AthEXbyrPlqUsUsbfa_hLoq7XEoXmWICbS4CLMs-_2ijgvx3O4IbKl85l1mACqeueaLOsxb9t52Bj63loXYHsIwnJM3XaN6dWyE6lEIbEV5b1fZw10C1e7eDj-ipcI4U8uH7oBmm0YxUIii3vT-he8lBnZ4k_oKEzwzAJXboppS1Nn4EbI3aAv2W5zkB7OxELHthI3xLRXolq24_JkgGX69TD9nmNfQLMs2BtzvHeKtWGNaZ2wwOKVPNzH7Hi6osSUGvq9QkuOMP38dv90PM8AbuE-JL_Laea4-DVFuMUVsWaQ8SUL39lIVn-i0eGb4Jqm4kRSN_F2bN8farVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ejPaIkgnDcwX02qciE-gLhJuwBLYexl98irVIYwTpvyL1JhwoyrIsntQW_sruUYpPY-b6k4vtGu5wBIvUpMfv_wa9nlGbka3MXHmR-qUAmNJeO2JoX-Iy1m1SG-jd9ioPneiKwGqNC4ZFU_WDRqfHmHaR2DFAr0xrCoR8IuTwm_KUAyegZXwjl-I8pjvG22-7uTlHWpeVEToAh77uYObzJC-LXfFzuFO-Mq_Ferygrv662--pyw2kScLhq3soii2U2hKCeA694-Y_YwpbNHeSHhl5nvbMp2TjfQdZm1UrAkL9QcjZ4BcqotimgzJxYNDwlHwtYIA6jimw2ywEL43rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ejPaIkgnDcwX02qciE-gLhJuwBLYexl98irVIYwTpvyL1JhwoyrIsntQW_sruUYpPY-b6k4vtGu5wBIvUpMfv_wa9nlGbka3MXHmR-qUAmNJeO2JoX-Iy1m1SG-jd9ioPneiKwGqNC4ZFU_WDRqfHmHaR2DFAr0xrCoR8IuTwm_KUAyegZXwjl-I8pjvG22-7uTlHWpeVEToAh77uYObzJC-LXfFzuFO-Mq_Ferygrv662--pyw2kScLhq3soii2U2hKCeA694-Y_YwpbNHeSHhl5nvbMp2TjfQdZm1UrAkL9QcjZ4BcqotimgzJxYNDwlHwtYIA6jimw2ywEL43rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IgatTNuME2vuk8UDxKEcDnr1Vk1aVH2zYNDN9BZ_PT4tDXbpP_bOcYpj9gmtiJ5Kvvyo-yUaenYhERCzcvAPrH3l81bKyL_yaZWtSLXzixf1GnF1SnRNNFhAaLUN04wM0yNjs62aYCXjjnLEz_KFNuij5FaNEWiq6EwY-_BDy_5qARHB785NfmaZoKIGRWWC0r1CoqMl1_o26PQfCVCh2lCj4pw3sPdCVdmTHkUO4ddS8LG07uvKOUP3HHcIfcDAyJnj2quQCROCKHIRw1Zk7ituEbIVpkCv6mSHF8aeydDNbivtPE0gz8UZZ-Gx-8joa-M6tm3EiqGavFHh88ZpAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IgatTNuME2vuk8UDxKEcDnr1Vk1aVH2zYNDN9BZ_PT4tDXbpP_bOcYpj9gmtiJ5Kvvyo-yUaenYhERCzcvAPrH3l81bKyL_yaZWtSLXzixf1GnF1SnRNNFhAaLUN04wM0yNjs62aYCXjjnLEz_KFNuij5FaNEWiq6EwY-_BDy_5qARHB785NfmaZoKIGRWWC0r1CoqMl1_o26PQfCVCh2lCj4pw3sPdCVdmTHkUO4ddS8LG07uvKOUP3HHcIfcDAyJnj2quQCROCKHIRw1Zk7ituEbIVpkCv6mSHF8aeydDNbivtPE0gz8UZZ-Gx-8joa-M6tm3EiqGavFHh88ZpAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=VtGqbEIG7Pddu54Ihu71cxdcEjKNiqPIdy08cR9n-3bUqNhb12qUZlDp6eXGpzBusdP5iD0zyahPdGFGsCET5__XLLgen9eV9DHkJuTZ5qqZQ54poDTwhHgMEsMy4fiUrdZCTPibZYNk9Yf4TY4vdVWwxshaFDqTNtr0GCAMwE2xpwwSTW7zw6DlyF029gU49bT984YaN_JOIDX-lTIq8iJ35KeSN24Iyzm_S-H3TYYWaPvukMjIMq6_brQW4HVw5Us0dVHci59Rr_vnIzcpdD4qByoMAvYxygN3jx8TjIvvvZKkevCLwJ3tfM01uSdd_QmW-0xe6TFvM_mIZMsSQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=VtGqbEIG7Pddu54Ihu71cxdcEjKNiqPIdy08cR9n-3bUqNhb12qUZlDp6eXGpzBusdP5iD0zyahPdGFGsCET5__XLLgen9eV9DHkJuTZ5qqZQ54poDTwhHgMEsMy4fiUrdZCTPibZYNk9Yf4TY4vdVWwxshaFDqTNtr0GCAMwE2xpwwSTW7zw6DlyF029gU49bT984YaN_JOIDX-lTIq8iJ35KeSN24Iyzm_S-H3TYYWaPvukMjIMq6_brQW4HVw5Us0dVHci59Rr_vnIzcpdD4qByoMAvYxygN3jx8TjIvvvZKkevCLwJ3tfM01uSdd_QmW-0xe6TFvM_mIZMsSQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=UgmpfNXkZAHJ_TSxkOKTHhQO7gl9coqhqgbvjTWI2EXjidfhJ9oh7czEGW6BneFM_UPsNnBDfVzOOfyz1chTKEzj11cEY6uXXQU5x8C9L9oQuGIf1X9VlyOVECX_pUKhH206gjP0P8eGtQr4IBXPrtfZjVAnacKDJr1t2A_QW5dABBWh6J1rPHHdxJnRP0tC1kLffN-u94ENtlU5g8_N-CaBFRiR5aKeJvnkRuk3dZ0Y5m35FAsNTVqXMGvk6jFH2rkAGr137mWQYBuK7sKebZwYyHFQL5k0LNLBbtib19Ijuyk9EeP9Vs90_T24oB8me75kn92h18YtbjyIAQB2PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=UgmpfNXkZAHJ_TSxkOKTHhQO7gl9coqhqgbvjTWI2EXjidfhJ9oh7czEGW6BneFM_UPsNnBDfVzOOfyz1chTKEzj11cEY6uXXQU5x8C9L9oQuGIf1X9VlyOVECX_pUKhH206gjP0P8eGtQr4IBXPrtfZjVAnacKDJr1t2A_QW5dABBWh6J1rPHHdxJnRP0tC1kLffN-u94ENtlU5g8_N-CaBFRiR5aKeJvnkRuk3dZ0Y5m35FAsNTVqXMGvk6jFH2rkAGr137mWQYBuK7sKebZwYyHFQL5k0LNLBbtib19Ijuyk9EeP9Vs90_T24oB8me75kn92h18YtbjyIAQB2PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfJ7QFMGgRVJ5RSwbOMeuYEk5ioNBUq2LkXkJwZi_P3pMW3ulgIBpz--4XhsmfWFX-7Gz-en-LS73zdLRUgsmOaPLh3Cf3pKqX1u2WHQR0bZE8ET0yDSmZqaGSLBRxNgu7j-Q_lFJhS2FzCaxSWnhqFXbdzWWYaqzhIIsGs7eq9BtsiSmUBrIqcBtLMIWFym4sH0_y-ENj6O2v9W8TQSl-rASilLxVCxQlAibM77DNJ6iSiAsxeagEcrBQWkkGWkTacVimh5tZO_vmcuELvy87zCB3EXlBX-vDc7Onn7Zdd2Z7QGo-JE1rDe0399M_qUAD20s9cvDycbwx60juPbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=DCWmRRWDWCTCbVXPOmIoV735PBs9XqwbtrjrYewxMw4IggQPdbWqyjHCzpBKnYnJ2SEJFy-H5ut_peJzKKLNldjMTfk5_Xdh9KFt1asuJZ_GuvKTDk0BvThC8M6eiiUPoZv1thVCMMuk7R9avpO5RUnPGVSu9Pa-iyNlc9ja0g1tLUNEyibP3UuURoRqoiW-ej9yhQrn8lmavvrI26WcuNTAHr64dl-Jptsqu3CeK0XCtGnKnmmapZsP3cxxff27gRNwLIfc93IJXjSpA14IGB2qJuTwze7lbVbn-EtEEE1MwFy7UA1hzbV3ff05eCSrtVGtpb_Gt_VDuvEQGrEP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=DCWmRRWDWCTCbVXPOmIoV735PBs9XqwbtrjrYewxMw4IggQPdbWqyjHCzpBKnYnJ2SEJFy-H5ut_peJzKKLNldjMTfk5_Xdh9KFt1asuJZ_GuvKTDk0BvThC8M6eiiUPoZv1thVCMMuk7R9avpO5RUnPGVSu9Pa-iyNlc9ja0g1tLUNEyibP3UuURoRqoiW-ej9yhQrn8lmavvrI26WcuNTAHr64dl-Jptsqu3CeK0XCtGnKnmmapZsP3cxxff27gRNwLIfc93IJXjSpA14IGB2qJuTwze7lbVbn-EtEEE1MwFy7UA1hzbV3ff05eCSrtVGtpb_Gt_VDuvEQGrEP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=gRC3HpM1_1UqAZPTJ0haA4wfIYx6obKwr-xWm90OXH4C7dnlJbsMc-yqXXt-YTs3VAMA8aux2rsv9dyfVhJhIhW4dv63b4pCrox-5IZYwHzaafiM8qYqVFqP-kbwOckPLbJJr5fAgllRljsnsLuM9iA3krFt2CuCfeCcjpIjgkAC7KgHdifZXlyxpkffrmPThM7hQxI3le0jVuMxLtgRMajoVZWuQB8s2pscqsHnb5OWszb6Y6ZqKi_hwmQcH2vT4xpNkLCUQwJLVpcfFpRgiRqA1Im_6FcuLT4cvJ4tEAZ783gGLkaxa9afoVz0Rxn8y1y1PCukPNsb6mAEv8NogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=gRC3HpM1_1UqAZPTJ0haA4wfIYx6obKwr-xWm90OXH4C7dnlJbsMc-yqXXt-YTs3VAMA8aux2rsv9dyfVhJhIhW4dv63b4pCrox-5IZYwHzaafiM8qYqVFqP-kbwOckPLbJJr5fAgllRljsnsLuM9iA3krFt2CuCfeCcjpIjgkAC7KgHdifZXlyxpkffrmPThM7hQxI3le0jVuMxLtgRMajoVZWuQB8s2pscqsHnb5OWszb6Y6ZqKi_hwmQcH2vT4xpNkLCUQwJLVpcfFpRgiRqA1Im_6FcuLT4cvJ4tEAZ783gGLkaxa9afoVz0Rxn8y1y1PCukPNsb6mAEv8NogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=lLRyJOSbhti7uDcwMlyCuXHYnlOCaNj_tEASwbRixCzeI_Cw7OmG6skMvYgCipWBBKXWIilIVtf3pI9GcUdFXEQMuKlcy7A0RV_WjTsphjrxjThMt37D1FEMif6uFDglx3pXcKsyh4hkJPmcQ2XAOnbJ-dcKCb9udt3-BdfOCY2IHKYqymV80B0n-Cze-xHSpz-G4rXHOJ85FY5ZjYUMK10gUNqwXrtSuxWlA5FjuHrt9AOZlqtQtOLGlG_17-rmJ_gcpwi5fjiqJD5O73hwa2Z48Cn2VN47lv3jC4TEn7_d1bg1Jdv3Ljh01GiAC26w2uKdfVtqPbBGnOTDO4g4xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=lLRyJOSbhti7uDcwMlyCuXHYnlOCaNj_tEASwbRixCzeI_Cw7OmG6skMvYgCipWBBKXWIilIVtf3pI9GcUdFXEQMuKlcy7A0RV_WjTsphjrxjThMt37D1FEMif6uFDglx3pXcKsyh4hkJPmcQ2XAOnbJ-dcKCb9udt3-BdfOCY2IHKYqymV80B0n-Cze-xHSpz-G4rXHOJ85FY5ZjYUMK10gUNqwXrtSuxWlA5FjuHrt9AOZlqtQtOLGlG_17-rmJ_gcpwi5fjiqJD5O73hwa2Z48Cn2VN47lv3jC4TEn7_d1bg1Jdv3Ljh01GiAC26w2uKdfVtqPbBGnOTDO4g4xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=O2FVXleVnMTLFkAd9p-5Un_eKc8OAWk7CqJO2D71JlE_8RuOfRO3JnQHuRoJkL9EH9yF42oCnVBNBzN9iqyTglmJ1ex1GPizEICpt7K_A43HMc8eXYEskndcVXDyNHG23iPyy_2GeSYpZxVsZOKRM_BEzFmdnga2Ssrw3lPV50urEP6hRN2PstLswV8EM0BHCa9_VcFocGpoCes-ouI7o9HinlEBZUqoQQLHWgOChbsYoakCMD3BIc6Esklb4JMMAxEEN-ekWSLuy1Z6gGDacXRTA6z5YVl7wMYaTlOBhXrpiuXsKdajrcqoJMPledG18n71xDI-5eLefEFFruZWcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=O2FVXleVnMTLFkAd9p-5Un_eKc8OAWk7CqJO2D71JlE_8RuOfRO3JnQHuRoJkL9EH9yF42oCnVBNBzN9iqyTglmJ1ex1GPizEICpt7K_A43HMc8eXYEskndcVXDyNHG23iPyy_2GeSYpZxVsZOKRM_BEzFmdnga2Ssrw3lPV50urEP6hRN2PstLswV8EM0BHCa9_VcFocGpoCes-ouI7o9HinlEBZUqoQQLHWgOChbsYoakCMD3BIc6Esklb4JMMAxEEN-ekWSLuy1Z6gGDacXRTA6z5YVl7wMYaTlOBhXrpiuXsKdajrcqoJMPledG18n71xDI-5eLefEFFruZWcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuWGEw3OHYjI8cDBtpDqUYphRZwE2E6ocWH3P3v1Fa1DTyxYBK3vV8RYVQPTZaGdEVBMPwJzrwASGveoD6YGh_PdfH6rpzd9TlqYLD9kuqsWdk1XONHEr_CzeBu9SnAUGpSp67297bYVHkZbz5ptcMuVqwHhHX62mewX4kKtK4b2WlrG6ZkCV0EVXLcctsxo8jsPJEZYgCWsi4BUW03R-9pIoRlECjFU2GExa3k_NQ8HFsxnQCY3yIgY9Q8oDbjT7nv53305EwciwZ6SVq1EBJNPsvlUYrjvC1UCldirqqMAkWHQvNTJ9LSCucEGH6L59KStxzM2KFZ3XUfoLGel0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=N_02K_4Wy71pAX75kpwVPFXs6EcibebArQMa30mLEFXZz3NcNI7ZDBcEILc4ZLSEzSuNajyF7MtxB0yYjD1bOzrUouJBA7Md-zZFblZVNCPnffwqYDHLxXSjqn5NHqkVBINHu0fZOGv7bh-beDliAy-6Kqkq1VbGCxKEuO9V7q8ADqSqZMmS4XvI1Kw7R1iy-uCHqZRGayVo3ljY4K43AVTM4V_zRVHcnpPkJ7uemCCl_YJRa500zogYXisAuPfSLylqAyYy6_grNd7ZVzS7xaU-n5ZaVTKMLWYQOWtuJjiQ0NaecQoCws5a598K-IBIQE9hl9-GKxjSZ1WQn0miqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=N_02K_4Wy71pAX75kpwVPFXs6EcibebArQMa30mLEFXZz3NcNI7ZDBcEILc4ZLSEzSuNajyF7MtxB0yYjD1bOzrUouJBA7Md-zZFblZVNCPnffwqYDHLxXSjqn5NHqkVBINHu0fZOGv7bh-beDliAy-6Kqkq1VbGCxKEuO9V7q8ADqSqZMmS4XvI1Kw7R1iy-uCHqZRGayVo3ljY4K43AVTM4V_zRVHcnpPkJ7uemCCl_YJRa500zogYXisAuPfSLylqAyYy6_grNd7ZVzS7xaU-n5ZaVTKMLWYQOWtuJjiQ0NaecQoCws5a598K-IBIQE9hl9-GKxjSZ1WQn0miqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=m5UvQbvHYwMgb1lt_RS3UwyywcZWfMGyHDKEVpoUmbq_EuCwspxcqb2VlSPfF5dPaj3qxnfzjY4a3KpDKPkWxLTrwbRyghfh_okA5X7isFWweXfhQp0r6pYT0uiF2iRw1Ul7tBJ-JHQnb5fkOAdklnA4-8mu13m6zsNPKrza-4MQ4NlmW0Szcr7Sr8H9t2TOBUIEod3oIPuQsSxQgigqu45ujgs45mvwV8E1XvJFzjeqI556kT23w-u8KSBQ8oN0f0AHl90OMps4Ftvhi3v8GaChSJoPvSTsx8Do42BdFHI07x8NC61HG1qreL4dfcoY1E3hM2_r5HEKyLGLPe9GIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=m5UvQbvHYwMgb1lt_RS3UwyywcZWfMGyHDKEVpoUmbq_EuCwspxcqb2VlSPfF5dPaj3qxnfzjY4a3KpDKPkWxLTrwbRyghfh_okA5X7isFWweXfhQp0r6pYT0uiF2iRw1Ul7tBJ-JHQnb5fkOAdklnA4-8mu13m6zsNPKrza-4MQ4NlmW0Szcr7Sr8H9t2TOBUIEod3oIPuQsSxQgigqu45ujgs45mvwV8E1XvJFzjeqI556kT23w-u8KSBQ8oN0f0AHl90OMps4Ftvhi3v8GaChSJoPvSTsx8Do42BdFHI07x8NC61HG1qreL4dfcoY1E3hM2_r5HEKyLGLPe9GIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VC0GHcCBMInt4i1vQda8o_Yns0U14gXrUVKZ-Slimy9L8CStS2mvkCU1Zls1nQtM__0sUwvWSsWnpSeW9gDkgGY_Nr0BcgRXijLyFzY0uimghYGGixnZEbOmgCcpS1un78oUMfAAvzwIYPTg2ABNdIxhoaJS2rp51KRkoIxZJb06DxmwQJMr_4zIHo5bwiBdHGisciXcvD91ZdWrHMNOcaAQNCarHrhdgIGED1drGKqbZ4a_zGyTkiFqvCCyrWNGes7V2PnyrItD957Bh1x6_BQAFXhKm8S9OSpXYqpGQQ9Hwl8j9FZHJn9ORx00ynxOxcwKYn4bfrKomjeiK21WJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqyK18JryIvEZ1xcOLAtkknxiJNft6s-VNj0Un4YSHZNrLgt72dD5v1I1pgjP_Dq_YEBJarldt11hdywgga4CmLNJ2NWU4Y3hL9HeRM_yn61zrQrqBJlsppamWTSwpIb6mQwk8RQ8vv-gQHfWT4_x5kOgLUpWAbLYxrd2-lP9LwvNXYK07lyqvF0mFeA_ImtXivvtl5wDfc7OpVYYFa5zjVODRIndQoQ8rK1y69t86YE0ZApAhfPxLl9BUCZXMWOo7YGB71JBjfEuZGCUjkS4QZHf0f35AuW-sPSSI2BejWxk-lVS0bDW8JfM6xiAvKzeCkpslcBpl_AeBjmEojM-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Vl2KL1cfcMMigkaFEerLZlWothlbXwWbSI0H_4h7HzjWTr86_bxbBDcFI-t5O1_FqL_dE8h9ufzgLcfooSz7rFMmiGMW8rafM2cnxhwp7ikWKTN5i_nFswc7Egw13eNgOm5Eux9RBEYISTtSHuo4DIBWqF2wEWRhHx9Icpz4zz5nVhCx1yoeiB2I3hoIqnjvGvm9tHS8x7Wj70wJmQPNGTRA3Avxq72haMF9chMSMSPIo4YqGWST3ug_hWciGvX1BbNVQCXJvzta8gycqVRkXGR_Y1BK5utD7mm7v4x6znzzrMbclMy1Rm0FULyLWchfj5Gux7kezsUza_A9CTVRqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Vl2KL1cfcMMigkaFEerLZlWothlbXwWbSI0H_4h7HzjWTr86_bxbBDcFI-t5O1_FqL_dE8h9ufzgLcfooSz7rFMmiGMW8rafM2cnxhwp7ikWKTN5i_nFswc7Egw13eNgOm5Eux9RBEYISTtSHuo4DIBWqF2wEWRhHx9Icpz4zz5nVhCx1yoeiB2I3hoIqnjvGvm9tHS8x7Wj70wJmQPNGTRA3Avxq72haMF9chMSMSPIo4YqGWST3ug_hWciGvX1BbNVQCXJvzta8gycqVRkXGR_Y1BK5utD7mm7v4x6znzzrMbclMy1Rm0FULyLWchfj5Gux7kezsUza_A9CTVRqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luGa16i_6hcZdE-iE3clUQImOt_iuwgGFsmGoTvDz5UAqTuOjZ8AQwZE2p3rjJRY-Pu2WdKmEeMOyTmyMwu71JBGtNCWW3-5NR__X0XQR_GVykqL4Jflbbe13Ay9zYpA81C27X1LpEdS5ujUrlBmB1onNlrdNcxXrMpnh5V0Jfsw_cS6jHjUzU0-R1ax0SAWzJpK0ES5GQqROxuVRmfXspOaz3J9wMBulAdFv-8tHTQ2TVOM2kedtG2e6vAsss30jd8NL-aQu56hIJ4fPvXOyZZoz7TvlH57dK7m2BG4MmvX7zw9FhZY2FOfXYmwhwaWW-WYYYoFxdL7j70f9HmRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvsD8Su3ROC3YxI3ktY4JUxRzwN-k2txOKtB8m7hVWvQ372aZnqhci9BWdd0UQymV7ANOE_0hWesm3zcdc5GVWfu6HyANmGT5PqSPPQ02TkSqmnFcJHZLBFsvjBvL3pCJUFowk1hPr9RtDUNMs3Oz3e_qVvEJA6FfraHSy9uQMUpVn0i7qA3nE9QT05MGeYHfpnahg-jkt2RGMw4NhupfUKq-yAWsK4Fv4L8h0nUMOUicsS8vEbYVsIKQRukJtJmfwUe1Hg_eZugqYQOkXdAcUNwm_BgkrXdcemtloPt62voovsqjRp-DI-DF0VZvsOTal5C6_iaGU6hFpSyS_xArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfy1PmpxCykSoO-fIoMElv5eLr4lmPasA0iGAygad4FtacXVzhabK-yoYE7UT89bPOk3tj9niwqEzZ48_tLccqPo2u3ip5G7dfKLM0dW8xhvOXD2r8ggJ9ok25tZd3K4AiR6E2vylSoBJy3lXJoknlWeS8PP9GGlpL-JSyMD-0iydBoWp4VsHhUtThukfwvNPtZL3RFp_ZwirARUxd2-t9r-aWSUHm1BraR_9XY3a24ZqyW464w4ry39RRaoaXT6sYku5Ms_dk2Owd-0rWo0fN1r9CpW3lFJu6oxwlQN-fjtGYQbrynHDPUyEA7dsU_zVfRdIdHrWTio5k7hm5fGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=VFFYVNnooIf0MyREg6MywWJ-e9-q5RQ3DXnkA3ZhlazU2i6ukX1qz878H_gwOfkffYmx-TRwOUCxBy_y7e7wNMzvLh6wwwRE6rOsNbHtw0cbm3_NaT5fW75EvPyknkqzEpchVwyrgg9QeuZeXkUACuKj3BGf2rNy4TqcbtWfsYBxNpG2CxRD6dXGY3YOAPdtxgvwNqp-eO-z9jM4H4dW8UK6QZpEDK8Y22mpt_M-kOd7IOaj86Mesny4XdNz_JOClr_Jf-YMTyuZrQZAuApUf0DYbV5ODhbJnJRv4NkBYfRd-JT1J8pEvgReN5bbwcnqXNlYFuJeuH3pxs_-vjaMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=VFFYVNnooIf0MyREg6MywWJ-e9-q5RQ3DXnkA3ZhlazU2i6ukX1qz878H_gwOfkffYmx-TRwOUCxBy_y7e7wNMzvLh6wwwRE6rOsNbHtw0cbm3_NaT5fW75EvPyknkqzEpchVwyrgg9QeuZeXkUACuKj3BGf2rNy4TqcbtWfsYBxNpG2CxRD6dXGY3YOAPdtxgvwNqp-eO-z9jM4H4dW8UK6QZpEDK8Y22mpt_M-kOd7IOaj86Mesny4XdNz_JOClr_Jf-YMTyuZrQZAuApUf0DYbV5ODhbJnJRv4NkBYfRd-JT1J8pEvgReN5bbwcnqXNlYFuJeuH3pxs_-vjaMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=btWlM1doAV3vhg4Bm5hulwOUt6z0qSnmSA-YYhyKI9H0-RbVIdj8Ya_MrNJopPM7OMS5XACqCAqzcMD3gqiH6FswGK27f9FxoVoOxk98o_AqDcZWgKbWumKNJ8TPUWURzpWTPaTaH6fogyFBGP1_-H6c5maJBPCR62UIaBvmFq9z1B4aEsSvSb2209zCEY9GetBQIJFyEtZMjnVNEGQIp6Wa0dmMdagG3ubsLVGsWA5UnmIbVLMGXgwmanp5yY2ZsD_9j6WhONurUQ9Uamnm4fkdAV0gggcEZsWFJQpJEZgItdZpxLARZ6J32COnRi5kLIjJNa7PUObXEJ-ZXvSTRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=btWlM1doAV3vhg4Bm5hulwOUt6z0qSnmSA-YYhyKI9H0-RbVIdj8Ya_MrNJopPM7OMS5XACqCAqzcMD3gqiH6FswGK27f9FxoVoOxk98o_AqDcZWgKbWumKNJ8TPUWURzpWTPaTaH6fogyFBGP1_-H6c5maJBPCR62UIaBvmFq9z1B4aEsSvSb2209zCEY9GetBQIJFyEtZMjnVNEGQIp6Wa0dmMdagG3ubsLVGsWA5UnmIbVLMGXgwmanp5yY2ZsD_9j6WhONurUQ9Uamnm4fkdAV0gggcEZsWFJQpJEZgItdZpxLARZ6J32COnRi5kLIjJNa7PUObXEJ-ZXvSTRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=vcoltnJVFsyNJwv0wMKhjujWQjqFTGC0bsDlKgaHNgbPTv2CUqOd8f-UHL19UiJ0VleujeuhLSrJChxZqSz_yUDkIg8AWLu7oYEpovgnaH4IAD9eebxzuvYCK6hHFEzF_YwLZmmwFrgx8G4ftuu0qy8ArLEXF5JFidxW3Br4k-rR3GHQLjb671S7QvQgG2CK8SM4n-7lAt-8xMl5xpvMzDx7koJxwR7nSVcENpJb9_obHTj_KBWkK2c8r49_y-4J3MivRejtaIHqH8zjezrNZC2ZOm7rQlgeC-2PGYQVZeD-MknE-W5UcCx63wO4jfDIiMYUGpRAumCNKXv0pcKv0DYGiEAZKNRlZRo-VVK6CzMdLgt8_gOXb-kBWyyF6En26Cv-1i6itJj_vyQDZ2tNQ6a-rurgL3hgcBJQnqxcQj-vS-dq5EfhsL1lIksHUKIszm4yFnagZGY2oun9yp0vpmz4VTvGwMX0W2cDczxi68u06KPP0cApHESHiPF-g-sbl9Df5RUwBSC2qVaTm_gvQWBxFqoYfdDqqSvYgCj10yuUNgn4mBilFYwiePtcfk87w1srtHSNsTi6I0zdHaEdivtcRJzKCSTtSRxlCLBUOAiYtro5Qe52QXI-64LlAAWc_AjauKiPzvPXnpA77IMftQQeE4XwW7lQHtUCG6pVOBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=vcoltnJVFsyNJwv0wMKhjujWQjqFTGC0bsDlKgaHNgbPTv2CUqOd8f-UHL19UiJ0VleujeuhLSrJChxZqSz_yUDkIg8AWLu7oYEpovgnaH4IAD9eebxzuvYCK6hHFEzF_YwLZmmwFrgx8G4ftuu0qy8ArLEXF5JFidxW3Br4k-rR3GHQLjb671S7QvQgG2CK8SM4n-7lAt-8xMl5xpvMzDx7koJxwR7nSVcENpJb9_obHTj_KBWkK2c8r49_y-4J3MivRejtaIHqH8zjezrNZC2ZOm7rQlgeC-2PGYQVZeD-MknE-W5UcCx63wO4jfDIiMYUGpRAumCNKXv0pcKv0DYGiEAZKNRlZRo-VVK6CzMdLgt8_gOXb-kBWyyF6En26Cv-1i6itJj_vyQDZ2tNQ6a-rurgL3hgcBJQnqxcQj-vS-dq5EfhsL1lIksHUKIszm4yFnagZGY2oun9yp0vpmz4VTvGwMX0W2cDczxi68u06KPP0cApHESHiPF-g-sbl9Df5RUwBSC2qVaTm_gvQWBxFqoYfdDqqSvYgCj10yuUNgn4mBilFYwiePtcfk87w1srtHSNsTi6I0zdHaEdivtcRJzKCSTtSRxlCLBUOAiYtro5Qe52QXI-64LlAAWc_AjauKiPzvPXnpA77IMftQQeE4XwW7lQHtUCG6pVOBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=oEv99vZVRXUPCXiy611379HK1a0Cf3TmzygD4VN0J64DCumRXak9QLtGzkmWl6e3FOLRAJACg38AzRA4KCAgWKehFw_dbQQFcXH3iG-543S4-P_SuBjZWuTVxVRARpytuKyCET8NrSWzb7Cj-7oifcbyZ3KfdT9uH-gnbeJCsE431ohiM3f2nKzQsmleD_YYtusU0O_CZUnk6_cuxlHdzjWuGLxOKCPBcvtKKQ8Om7vITTojDPvmzjiY8R0h0SJuV7KzEqwXagxGeRXPQoLouDb6hg7DZabjEsd__80E5dyAh-IGKg8SMncrG4zJPDFwmndfWo_hFs9rXNdub64pyk9DSFtgWq1UAnV6HQI3RY_eR3M6WBAwxIujQW8OsqXNN8bktpOlPiJIwuUa_FzxyRUZd6ZJEALzlzUJUFPZ9OeN0WTw2W-qK0k_FBcv7JQNIB1j9NrGh4nOJkj96FIsA_7YrDts2NPSMlgPxq9T2msRwU8I-wqPn9eHtrbomf3Kjm5e7EeBFqHUD6ev-1YjTmG3jKbe1KOjlrqYGQ60CKGU7N3-DBCzpRaShJTvGWRqL1xoFPnjhMCO_frAxngtsghWj_S2D3dLHB5qonjaFZvpPnVIosk2rsQYCT0w8tMm3tPJLDORsyW13PlCRLcz_Tgqc38TK3jXg4bIR7dUUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=oEv99vZVRXUPCXiy611379HK1a0Cf3TmzygD4VN0J64DCumRXak9QLtGzkmWl6e3FOLRAJACg38AzRA4KCAgWKehFw_dbQQFcXH3iG-543S4-P_SuBjZWuTVxVRARpytuKyCET8NrSWzb7Cj-7oifcbyZ3KfdT9uH-gnbeJCsE431ohiM3f2nKzQsmleD_YYtusU0O_CZUnk6_cuxlHdzjWuGLxOKCPBcvtKKQ8Om7vITTojDPvmzjiY8R0h0SJuV7KzEqwXagxGeRXPQoLouDb6hg7DZabjEsd__80E5dyAh-IGKg8SMncrG4zJPDFwmndfWo_hFs9rXNdub64pyk9DSFtgWq1UAnV6HQI3RY_eR3M6WBAwxIujQW8OsqXNN8bktpOlPiJIwuUa_FzxyRUZd6ZJEALzlzUJUFPZ9OeN0WTw2W-qK0k_FBcv7JQNIB1j9NrGh4nOJkj96FIsA_7YrDts2NPSMlgPxq9T2msRwU8I-wqPn9eHtrbomf3Kjm5e7EeBFqHUD6ev-1YjTmG3jKbe1KOjlrqYGQ60CKGU7N3-DBCzpRaShJTvGWRqL1xoFPnjhMCO_frAxngtsghWj_S2D3dLHB5qonjaFZvpPnVIosk2rsQYCT0w8tMm3tPJLDORsyW13PlCRLcz_Tgqc38TK3jXg4bIR7dUUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=JjFNFBrC08zdwi934DeXV22zt4lvB1vdjmOXVLJMEmYMYhgowhkcuaGA700bCLA2oE49uEI30wIuHQsvmSNVi9-tjZpopAUtZVbinqLNwUX7okUPql2uZN_60UsEMwjuVcsrooxQAWwNzIYB-Q40mhj3_qGTKSPrJtXmVN4zz4AYour6RfeDG03yASp3hWHvWtCPWm6D7DSBJYgfmupgKdHXiWh5sDjVKit8U0M3fg9EWSrFr8_O0fZSvSX0PU4VuABu38W72oJGkXGTopw8mCZ3UNzEvt1vsn0ydnmS0d_kQQHmlLQctpahJaJiX3BMbw3iFQES8Hla9ueFRGCYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=JjFNFBrC08zdwi934DeXV22zt4lvB1vdjmOXVLJMEmYMYhgowhkcuaGA700bCLA2oE49uEI30wIuHQsvmSNVi9-tjZpopAUtZVbinqLNwUX7okUPql2uZN_60UsEMwjuVcsrooxQAWwNzIYB-Q40mhj3_qGTKSPrJtXmVN4zz4AYour6RfeDG03yASp3hWHvWtCPWm6D7DSBJYgfmupgKdHXiWh5sDjVKit8U0M3fg9EWSrFr8_O0fZSvSX0PU4VuABu38W72oJGkXGTopw8mCZ3UNzEvt1vsn0ydnmS0d_kQQHmlLQctpahJaJiX3BMbw3iFQES8Hla9ueFRGCYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoA4a1Am_2eASZ1Zmyed1JTOcmVRVSVZ9TARKC-hl4tzfaHgVd52w1vhxyaulDVvWrjsWzmMdWih-WHZEvU7ZulKMjzhV6V2oitZRVRxb1thHl5AMYRZuXaekrjeWhMQKRmRM2CC2wKAtS-COnaOHmygIXCz0l3im7Dj5bpwMr7Gu647vBhY6wzoFC0lI5GSQIDnFyOkyV1JfmTWHmrvcqZZMBdjneXqshW3RvtAln70WaU2fDe8m1FFKhkVod7zw8nAbTGOUSIaiJgYiDQVYYcctF0XHzPITmw0PXf7asoDLDMhaz1TM8Ki3LGRLgu_r6o-zYBYxFbOcUOsNePy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=jDHdrBIQajH6znBVV1oW-HM1BLPp-lvDsz3Xdfkte-u4X0EqpK2YKSNItfiZzZexLrQodteYy0bq7102ucX-El4SsovGCBVroiNT1rj6CiPGb_-SBswa3FLPrUghnUObV4-UVZwdlYo3vjrYy0p6dGaYZfy02vqTMQv9ZAU9qyeo93m832xgUCpH2ofd7QfrcSOYAHPf0FDHhWALVMfokT4tVTXBZXCzR7N14ywz9nG610xhAtxKOCIc3x1FJOzVugRL5De40wgS_Ve7SshAjdkD8b7GewcX3jfVkQEI4WEj5gv00omdOqO7Gau9KMSZhSGpDdreN6qsekHzaus-RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=jDHdrBIQajH6znBVV1oW-HM1BLPp-lvDsz3Xdfkte-u4X0EqpK2YKSNItfiZzZexLrQodteYy0bq7102ucX-El4SsovGCBVroiNT1rj6CiPGb_-SBswa3FLPrUghnUObV4-UVZwdlYo3vjrYy0p6dGaYZfy02vqTMQv9ZAU9qyeo93m832xgUCpH2ofd7QfrcSOYAHPf0FDHhWALVMfokT4tVTXBZXCzR7N14ywz9nG610xhAtxKOCIc3x1FJOzVugRL5De40wgS_Ve7SshAjdkD8b7GewcX3jfVkQEI4WEj5gv00omdOqO7Gau9KMSZhSGpDdreN6qsekHzaus-RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ByAv1DPlgY-xgQ_ml2ymt1iIut7q2-2Cq5FvxW3cFt2bAq-QZ_gfnpujWfMN3D7lMUYnkT4YWgWQrvbw91N4aurogcHbnk43mYPNmH9SF3-jrAMqc8vRbmFDcj6Fy7Wt2lO9M8ttOGsrShljxtYf_0nJHs991F0U4wjaulrRa8huBpqqdexss9TV1nGBstAOQhl_8WLrKD-1yx5TTS8U8-oo__4fRYpWhag5aXCUIig3qJ52UGodNUCydwoo5gQCZM5NJyMHQXeDbcDNfXfXQb2wnVyX7Q_-1rEeb3IOLQtB-LlRewuOoHRje-pGEf58Ng82DqXSrdC5SQgjTt6cuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ByAv1DPlgY-xgQ_ml2ymt1iIut7q2-2Cq5FvxW3cFt2bAq-QZ_gfnpujWfMN3D7lMUYnkT4YWgWQrvbw91N4aurogcHbnk43mYPNmH9SF3-jrAMqc8vRbmFDcj6Fy7Wt2lO9M8ttOGsrShljxtYf_0nJHs991F0U4wjaulrRa8huBpqqdexss9TV1nGBstAOQhl_8WLrKD-1yx5TTS8U8-oo__4fRYpWhag5aXCUIig3qJ52UGodNUCydwoo5gQCZM5NJyMHQXeDbcDNfXfXQb2wnVyX7Q_-1rEeb3IOLQtB-LlRewuOoHRje-pGEf58Ng82DqXSrdC5SQgjTt6cuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyXWAWGKYulEel8zLN4GUETGKnxOvAWuem0KVSh4BvLVAt6V662PQ2fHaQUVJtf8Jb6Jk93qVzSKOfa7Lfgso2_cy-MsuTwxJ999nu8SS3Cd2k2mv1gUtcTcYaBZl1cc4ttt_z-Uhd2l1zEgSdR9QCOen32W-0a2beCix_27s_RzZLoqPo_Ch6IcQyKLyqzP2BCTVY_CQM8AFv8syO02VV40JJwKKyHWgYH0h6_MuYgVVtRD_CF7KsIXQFCOr9grUNhirUawS3Vrrhda1JQh8WqrfY1NYaQgtFwQLJnw0lnGIAbfWcZfqPzQsAKevkcYzhtmATRs2ctVyaXG0lRYFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i10ZNMN6NUIJggmeCHMD0tlUmHpNTej5DXoWucYh-XkZdaOuJ2TgyUvevJ_6yFgANcd2_WC-InfrmJtwL-4ORf8aTDSaGSDqtv-yhTKxL6diZbMHMAzQPwMZFcEoD1fK_RffyIy6QQgpm3ei0yFhglnNRDRnqAYndeD2oZY90gsiHoFacSuLsRdPcx_oOHeHCnzv0oIFIznZNhwPNPkxKydHj5L0klYyRdUj65zsHiHo5FwPczTp6dATeKSjUprhXyWZeyrtw9HcL2AjFVfY6OtTqBptiTkfCPYSKoF-vWPOfEl-3SG7trRpHspze0AqzVs0QYYmSIbNyRhNiWN9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZU-HklmfJvzXX0XS5kLmHfV5kchSYuJIQvVAocrm_nKXJy_wU249B1h0Dw7VtQEmUZu0c4wU8Zjgj2aOXdgVe9R2dwQTFHfYRT1hzh5NVsOeoSD6x__pA-I5uNWMS-Rb2yggrvVZX0nGcK1hX2bq7tSze0OFB5G6ejPax_e2hArOKOtDVCwOzRq5yG5LZuILS9Sm58g0cteCqt9PRi7x-66U2c5X--v7psH-EXurJPHX0EU-FGX6W3H6UlxWxJS5KQG7M-LB7LkBed384Xf066JG0uq3YkJzRIxpN50lvB5CLVDTk9lKbsRx1w7A_1cRNRsQko_bFDHx5NsT1zl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNkECXn_SqIMJztWeCV3HOaUUULvapF6wS15I9eDHjoLjepJE9RcfeILCnJl2bL5fVC0CMsCf_RXC_EL8JR9ognw06cYBJgElSogibGqT-tPTEXRtiwj2A_livn9u2s8aW_T3UkomJEOD1jFKHwO_9SLIcpb1r52Ra4c2IZlAA65bQlHfavdNvaMsAmH8cBPGYiBCVC0frg_nc0my3lYWQ_Hyzdm-dV9ykaOSyfyp40TExKkbv40fjnHnD1-7T2q-1g9jQPxcNg8dGLbn-3Jef6gBUWsGdplZWNKMllMT124nM8T_9h4msrpD18AGGEJkX6amrgdlH7JLKQkf91LEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILFQ_SDi7-nic-MsFz6qhFB5IlZ73yZkHsK6mgl6jWItYrhFI8pexg-GYZjaM3ECl6pxIESwu_NJ8dYcvWZesqlA5Bx6kQhl7VwQCSdBvYmG5ID6GC90qhHRqB6y6pY3ccA7dEbKcLW-rMLa6QUVkf2-GoZjnytuxWxrBzwqZbBmJZGpVCRX3cgBy2EIWN8nuphWLzccHYD965wrKmVAM1wgcRFD_cQU8KLMOmN8Y9DWkNWs1hLC7_R4N4op4WqQwxNyuAR73aFLf1KYGaVsXCUyLKkvzSLt8DZIy9G4OrsQRpV9Layj7aZRO8sYZ7S7UQS3fiKI5SsroP4K7iE44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-LakZMLPoft2_a98AWsN80O9lz4oMqmt9OeHMhO0VqUDSfYILBh1uiC5lXkAkgs0KOLs8Kcf2TZ9YOiq2Gc-1EtVHrbE9_BU6Rl5HxOvTG6mIj3CHvM6WoO-r_ZXBAMLLxQrSmqtTmYlXiIqjWMvsABtNfmjr51y0uQ4u3u7Dn75UqMRYAQCbSuI_IAiJJD5_0zVq_AfybArNDj8uudNuOHMH7_VF-6sUsH8LgKfnSLy8FT2wuwpDlllCT3Z0QbBmj87xptiEqRDvHsyYtEcPkT4Wf9zzJ_9xr94cFf01agDWBr3nUKGWXXC3irMLaNAP_8BdOQXObXVFK2ZR2DhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3A3l1xyIrKX0O431-SlKKIkMEZUZ1e8_wQ6ux9hGLxQQb8oizb_a-5iusyWeu6nTHf2uKq3dnrOIGE6mFkf2OczKBnpCsovdaoWsmgFFGiFFSKlidbhmg1Z-LE2W0qPdaa2K-iSVYD0JzE-HKZwfgRyvx1rzmnQMSVzou7uh94CwvkwUSgVleaEcmmNC7OAbWNEC9uHTQk52uNYmyudztHHJgN7M6HbbSP8X-TFcmw1km40mz2Fuo9kC1z2DZKvdx23GtkjZBl0DJos0r_yPfUwvLY_LO5PyZH8WDCkaRWmIYWF6QYEKLippniFdOhoL7upEKTwZxbdg4kFS3grsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz4Yu9vrWkSzbmwSzy4coQyF0nK43ydfJAmYBVxH8g_cCuwPY0hvSpMj5-RwUvywGnfxETxJ3FBkT4nTZpu7BOXCFu9NywjGlIQdxMv9z1LZrkehKT4QqxPH4AelPPnHeY3D0bUK2g8uOUyiSgSHhbtgWpnrx0_TYVn2X3FY0Aas56VRT-b-H-Lo_i1z_T2YYZglF4tiLLhuAdDfKxsvLUKJ1xcil86FeZ3_5D74DLEm0_xCTvDkYyskT5FIuijfnie8T2vKA3-vPC5WsQZxhhRKqZzhg_BcujbjCtEqEbDAFeCYilMM4HZkhlNaK3C9YuyOmlNs4_uMcerkt34tGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JptPfDAplFIEcxTp8F5U63ZqNTfRXxJwNUzQBVe7ZKK_g2SXTd_Se-5l-58xQID8vefJbptT3BBDb0sJRAPcFmEwetmO4J2SFiJBDo5bRpUv-Koibij2rQskINzFdSGvI1VQG0cKZi-j6Tp8Q2zN70KCrCR3lwesqYvlMnJ6tKFTRzYyICPCsSL-YlDtqrmZTNQB8MfpAEvuyckMZt8W8-OCiHkY4YaBNVpllWtAZNUhf1zhvNW-iw1h6N3KEUNMMi5SmclhnvZCnYxd-gUMg5rSWj_wfy1esT5JH05bra33xZ77eaUHplbTgTyvs0jVIvwk2FoYuuFr8CTCtm_tUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfj8W_5Eh-NmRLidrCIIuCmRKY6ywx3hFKgfKjucuPXEb2fJRQE0b8tbnisB6b6e6wDVRcVJ0WZDeTp9RWs97r4cNtGFro72qORoaNWONLoJcckx97fznFsRWeKAmftdeCEIhhmrtpv0j7cEqOYxOX591yeXlAzKNFhGDINwhobZCZ2hlulhZUwpmkoD8xhptPrxJtP5GKXJJQWUGDKflZX0Hd4WAWUYM9ntHB44ldH28nY3EFNwQNVCw4xHvewKKa7BQ5SzUbAOPuCtytChLoZ8tZ7wwF9gTv8MTQoPxLLqyh_iI0Z5Np0o7EhfeTZngPutg2-VmFsh4whWuIQW-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=B5oZGGi-5AUmffFOrH2VFehZ8qCjbljS5fbQFWHwwkQBhZfX84iCyHqnAgMQrb-UqQxhnt9CF4SYN-AcEp5F_oZ3NwqOjpRHWUur3_Xg_BOeor6fbKWNmAy5SPvQ79a-s40ODQjTvxkMgLGTo3IT-DCq28HZpL05EtVSXYTzruG-xXEExp0roeIZiuI0dYanDc5OaJX8TkuYkcoFjMHmZMvi-E5UftDk9iVDiGlwlUklVBW2S_UHKNg3YBE7AF3R3_-naX-yxfxpY7MmxmgU5mlRpDUd6KG-hbGiIclw79ilDLr8nVVNY1Yud8XxukSz1Pm0qB5d7n6OqdjEh3f9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=B5oZGGi-5AUmffFOrH2VFehZ8qCjbljS5fbQFWHwwkQBhZfX84iCyHqnAgMQrb-UqQxhnt9CF4SYN-AcEp5F_oZ3NwqOjpRHWUur3_Xg_BOeor6fbKWNmAy5SPvQ79a-s40ODQjTvxkMgLGTo3IT-DCq28HZpL05EtVSXYTzruG-xXEExp0roeIZiuI0dYanDc5OaJX8TkuYkcoFjMHmZMvi-E5UftDk9iVDiGlwlUklVBW2S_UHKNg3YBE7AF3R3_-naX-yxfxpY7MmxmgU5mlRpDUd6KG-hbGiIclw79ilDLr8nVVNY1Yud8XxukSz1Pm0qB5d7n6OqdjEh3f9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKkkZJBcSeC3rdaXTndmn12-aL8M-GCpnCFpakeJQB44rzmxbadQwzvErtYRaxVpSmWKc3Na5zpcsFqRlU9Rka5j4OAWmM9SznXbPVlrR9DG5aZnK1-v9aOcrtQ6Sr0Vqc3TtuDvdJ2UyrkAqsBHTAKibE74QpC1ZO2jVMmygGDyjnuZzzuR1NcoC7EPINpb7ocUZKjFYZi3EqozewmrsPW9jIBsBaIHxFwQUwxIs7NiCAmGtYbmkCgk-yZF5PYJQ307v1-Mo-S4z2rB4LEG_Np413wYVaBEEk1ucZKMT6rCoe_K0sfWHsIOliwqmtQ1nw5vAG1P9GvobMJuvMMerw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVB9YOc7Iblg24x06V7kSOqCyYd-rcfsUFJtWEaxx_4_VaJiExplsRqwcSPT0t-8Pv3p8iZ0FKTayikh_Dvm6VOeHjTr07Lvf8ONTBeXPt4YsOewceCfQgFdyZc3IXeIAptcpmYbWMEdfKwn11j5Wx4GxyS5CwXuVi3jbGvajXEkW0_Uo1bgvNHng4c-GGsLE95nmLgrHQv42eqHbQ6h2xBfNW2_U3mj1alufk5uJyy-7JE5TaA1uw450WLK44D0qV4BYk3s9KaF8Zog-Bv-3IAs9-wj18fEOQUcbazrujpV6sBdOnnczjyWS_pK1P_N4DmY35670kKQ9-9aZAAemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Hj_4ZHRdiZ1D4qk_I7-lC4M1Qw2QmuhDAw4KTpc1v9ep-ElHIf62z43H3-C_WEGGccZvYA9yCmOw-OhjxPIbH6PiV0SiyiMyyAxxh8txsKEzCN655nknZT1LdhG3spU1qyA2t4YHoe2E_PveXxH9AQww7a3rzIj9sOqwXRxAwGg5S64w22-_UErZGby8YZCLn1wQWViYQe0cmb9NYcbeoaDNGutcDlyOSSpdEWt2o7u9YvHcl8eAGxic648lJY0JKVIuLrAe0JXYqwSqasQJSULsShJt6lIAH5xab2B1PPSVix7eNBQwCR571uMM7BS2RAdOQnmfkHPRt18h4t7FLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Hj_4ZHRdiZ1D4qk_I7-lC4M1Qw2QmuhDAw4KTpc1v9ep-ElHIf62z43H3-C_WEGGccZvYA9yCmOw-OhjxPIbH6PiV0SiyiMyyAxxh8txsKEzCN655nknZT1LdhG3spU1qyA2t4YHoe2E_PveXxH9AQww7a3rzIj9sOqwXRxAwGg5S64w22-_UErZGby8YZCLn1wQWViYQe0cmb9NYcbeoaDNGutcDlyOSSpdEWt2o7u9YvHcl8eAGxic648lJY0JKVIuLrAe0JXYqwSqasQJSULsShJt6lIAH5xab2B1PPSVix7eNBQwCR571uMM7BS2RAdOQnmfkHPRt18h4t7FLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Vvl_Nl4EI1akK58sELDRD_RHAb1va12jfhRuUkbOIhiA2IDdMa8rdMt1XHlbA9myF-pUywiWPqL4XMV6Of68zZ-BWulG6UJRNijSTluld-1IUEaqTVu5E7GnaOZ46LYIscy-eb6e3SO3fJ2B7ALOk9WKY_MVsDNkLrRUSdj4sdpfeJo-iMWEd_fUDzoYuyC2lnkza-NsTxDeAumnokgXfNMBQj8fckqOSAMaNuX5zCiE0I6Rzx9gIjOqzzaNfN6qIg-I2oHhW4QIg7m04X-A5aGbfl-s_7-UdWXOWo8bUzLmsVEF992cWARgfxPt6UbIHsPBQoaaKP1-iPYGQcL0Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Vvl_Nl4EI1akK58sELDRD_RHAb1va12jfhRuUkbOIhiA2IDdMa8rdMt1XHlbA9myF-pUywiWPqL4XMV6Of68zZ-BWulG6UJRNijSTluld-1IUEaqTVu5E7GnaOZ46LYIscy-eb6e3SO3fJ2B7ALOk9WKY_MVsDNkLrRUSdj4sdpfeJo-iMWEd_fUDzoYuyC2lnkza-NsTxDeAumnokgXfNMBQj8fckqOSAMaNuX5zCiE0I6Rzx9gIjOqzzaNfN6qIg-I2oHhW4QIg7m04X-A5aGbfl-s_7-UdWXOWo8bUzLmsVEF992cWARgfxPt6UbIHsPBQoaaKP1-iPYGQcL0Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
