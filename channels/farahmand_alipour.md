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
<img src="https://cdn4.telesco.pe/file/LwVhhoeNiDAe7HKkaMgAjFJxme7TH6Ljr8xjrIAEfAxDv6mk0nIYUY02JxlpJwPjarQWsg_Wp07Pq1jRQM6R-fNe6npJlFcYlyBJfKa51QkWvplNOaRi6KZhy0coCntnIg0XQ7I4YNV_iP5s5EsmEMqKUxYOfleJisRqtYcOaGM0rkB5ZjoapxO-q71TFmQ1Ot-jpRuWft4zPkAVBHDE9HXu7eFc_9e-pUMsddskOWm0wmxXj6eZmwuXjv68VBHSb49DM2uGYt-JYF33k8s0DpwdOPmAQqq3AX_hOvRHw--i_snRzM-ognOtdAkzXBgEWY-Q7mhh2rEqz6J0kWwC1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 03:12:55</div>
<hr>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG5RMPS_pTLU1v55QAEFcOksdt2MfA7CYcCGEFpWS8Ac25UcYO0gKrxRZdSC2igAug2ZmexHtUlStFEntaJB4Y-Iz9oTJZKqDXmUDrQhC3upjVLXQZJIStqDmxO2pX5o-GZRX3Yt9aauVon8reczj-JZS5l-wYydKjBYrQOf8b3hV9097fs0EXp1A_n6P_ef68qWSUpO5f4vW4xfP3jWNUW9I6RIib9LFki_icXCDjecrqDUs-TvVnI0gvnVBGp0lUK2Vu0wnVPqKIy7Jl1QLB4Kl3xdbMoiQXAqYOAsJNOONxszM-ETxuNcxnbJiBi-j4uyEOZFxmE9VS93VG-x5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAT5Yo62vOWr3odIdejd4zKBzhTgEZ7K1oMlwMqls1VUENGPYGZSClaIkx156X5UFWNUh8sPY70XU8ootnu_9hDyFYTewwZgnzwC5sG64ijS6_j1bwpCveEdlZv1NYVJgcVqKLYTmhm_d_exTz9lCUH8Fs4bXGJitqNGqAb5HW_kmyt271r7Ub9qT-w9xs0U7PGWxIgLWr5eM-juAHq7STGuV4iK_ZsBdyk7JiJMzh-Kc9UQVrXrW7iJ00aVycRYBFBDLg0dljil83-G3Mex_TjU1XD2d80aStWT5pj3i770Y3MTJfIHov5eEi0b3BhjhPJNv1mo4dcpc5GLr4IUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKLcjLtymkdAPjcMUa41LF_UH1rSbwYCEJAtHXbJuBEVZ7iioIqic9oa516HOBFJHgQBopzOEx8qqfuIN71VeCB_Y4ixJl1FZ8uSCa8epcFyK77ZPxppk9tTYGq6TZX76sHUqU_P80ezjeEZUtWfSGhrQvkcQJJbrMKpEOAi00p-Gt_tK51Ra7Yfap7vXkmdV2R9cSwNWpZwfK0itbFdjIi42Qu2gRU1kIwDyr3CirkcyJEeDHgB39A2-9WPQowhXSLtT3K0QWg8xOkjaEEPzHtgPbJkLrR05kImstWsQ-HZPNWRpEiIujVGw3out5F5jG0Iw3qF--Z2ImNgJNEPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=etHA__5-FmUpF8kVamL_oL0FpVgls-DcdJRLqjGhIx-9pdZ_nb4XPmMIYXHNmzm0hx5Gj-ElPWJwFUayrGZmhnyj1qbZNSt9E7cWjFttr1JiVwkBsis4I5anWUctnVeyiegHClmxnfHw8aoU9KZo_0xUsSDYaS9A83wyBaXn13K81HYZW8sO7or3KFHpsZDPZ-UmssQpmLE8dw40uyNtoBLPrJ38Xny4FTwh0Vyu-vCpDkofgz20oqYw9ui3u0zo6FQkllh4oIJn6AA5XbpyE8M3Z8Zh7VISsYtOBJh_Ja6utQqRyo94UeZ6lLj-gNvuV1Aaes1klmDZQpj1AW_izQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=etHA__5-FmUpF8kVamL_oL0FpVgls-DcdJRLqjGhIx-9pdZ_nb4XPmMIYXHNmzm0hx5Gj-ElPWJwFUayrGZmhnyj1qbZNSt9E7cWjFttr1JiVwkBsis4I5anWUctnVeyiegHClmxnfHw8aoU9KZo_0xUsSDYaS9A83wyBaXn13K81HYZW8sO7or3KFHpsZDPZ-UmssQpmLE8dw40uyNtoBLPrJ38Xny4FTwh0Vyu-vCpDkofgz20oqYw9ui3u0zo6FQkllh4oIJn6AA5XbpyE8M3Z8Zh7VISsYtOBJh_Ja6utQqRyo94UeZ6lLj-gNvuV1Aaes1klmDZQpj1AW_izQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSI6XhpcKhhyX-p4jUn3coWb6WKpydoMhMi7mOO16YKillKOdrHM-6XRWYluAVn4hMh5CRSV49uugBKzhEm9A8pAONk2iHxv8bGf0_W44BB6C7tTDjg5wQqUj1FoKJOor7iqXGIgXyV4gCd0v1KmTdTI29zhB_5QDooB_eCELZgD6YCE7ubjiKnefDgHTlDeeoLlYkFKvKDWRxkxcmgyyG_l-aJ9sQp-YTVtaAY2zJ2f8z_aN9kR6pTc3Qu0Y7K5I-FmthVkrF8p7qKAb_pj-ROWk00UAQsSCaiiXBFT2IE-kAk0WoWO1K1n66X1AyO9lf6xs5ZX7a2K7l3iM0r5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=BnbsKhzi1uiA3fFYbM5vHbN9SoHA2KZa85c430MOdIBFwKFZgibmk-5rJUdnhxgfUA1YGHrpxkt4y13S786SmoDPbd_gj0T4Fqv2j1o5Jf4uf95LTrIyRX1ArVoacB7eWbQs67HN4LwB9_8YlTdvRxcQ7FK0_aupNDYXgfxwj6fEPFzrnRpQB1I8-wGZzT0b0T-xMoC8bzOiHK8JLj02Uz9YTiwPb-csYvIvLOX0bxYSs_WuyPTGpzNZPUOAAU-y8hHtSeVe4g5djfoWnFwTqBArRnh4Gt8GOT-1Vc6ksZ3dpZ0B_Wvdn3-Wxx2Bvyl9VsnDji7q-syjshAiPZEQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=BnbsKhzi1uiA3fFYbM5vHbN9SoHA2KZa85c430MOdIBFwKFZgibmk-5rJUdnhxgfUA1YGHrpxkt4y13S786SmoDPbd_gj0T4Fqv2j1o5Jf4uf95LTrIyRX1ArVoacB7eWbQs67HN4LwB9_8YlTdvRxcQ7FK0_aupNDYXgfxwj6fEPFzrnRpQB1I8-wGZzT0b0T-xMoC8bzOiHK8JLj02Uz9YTiwPb-csYvIvLOX0bxYSs_WuyPTGpzNZPUOAAU-y8hHtSeVe4g5djfoWnFwTqBArRnh4Gt8GOT-1Vc6ksZ3dpZ0B_Wvdn3-Wxx2Bvyl9VsnDji7q-syjshAiPZEQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=nChgvLDRQG6hVrZjQid8Sho2Smxds428ZMx0CnzlEM3cQzG6WKWQEqadQWyIXUb0Upu7a_H2EtRA8rX4rjHEkV0Kpo2GrguudkfJss0LXWfkDgOodvDz9mOs7XDHSin7t-IthzAahVXJZVjML797RIvssLmc5hb9XMt6bO5NsCrrqrCi4aiZpcIR8TKzFPVMHKSqS0sqVqX-WfyQFI3BtrP8mIf-LSO70l-dpscbenMabzWvO7utE0r201AvFEQVEtH7P1mr89WXESwQu47xuvf7zhg5aOqaVm4fKrCJWtTXgaydetzrXDigPZ0zjFhOdZjk8yrYY5C3M5WeB03WdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=nChgvLDRQG6hVrZjQid8Sho2Smxds428ZMx0CnzlEM3cQzG6WKWQEqadQWyIXUb0Upu7a_H2EtRA8rX4rjHEkV0Kpo2GrguudkfJss0LXWfkDgOodvDz9mOs7XDHSin7t-IthzAahVXJZVjML797RIvssLmc5hb9XMt6bO5NsCrrqrCi4aiZpcIR8TKzFPVMHKSqS0sqVqX-WfyQFI3BtrP8mIf-LSO70l-dpscbenMabzWvO7utE0r201AvFEQVEtH7P1mr89WXESwQu47xuvf7zhg5aOqaVm4fKrCJWtTXgaydetzrXDigPZ0zjFhOdZjk8yrYY5C3M5WeB03WdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cf3PHh3LtMSh_zqSPUpUCbFpArE58y2EZBDd3XBrKfGl7acfotyUSb9BJIkQ7Xz8SZ-nHyWzRRDsP48UkH4KYpcgokq73jrbnJnuN-sHC-hADvwAOEZxPUNR1CAqeVvc0bzgL0JYyybxeFCQAk0wvOvNumPJhttHPbgQ9Kgh539E7MZW1B1yaRmJzZyAhEpXInQM2n3z2slnuB1tb-ETkY0AePZv18xGW70nWcSt32BPIVtgndQjaSJG5LSrS_gQPs_ZUbT-sHZxuyv-kNegwEs7yh_7kmKf-7m50pBK8vhki0dcem-QpIvUDtXoj6Z1NNRHNENnK208F8Bf9aGATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-IdRHS2E1ilfJj-RAzHx3GTRIoC7AmweePIbohu2q-lhiuHCo0TPEjmomAv7rSvf7xP5U2ZP2SSdHGZxZfw_s_MP6NOvNQ0oJBLlhqMFHvflqZlensXogQPNJGD0VY-ax07bYrxUDGpvM5u0TZJrqTQXuPKj3aPC0KybNxIjWVfmVulZHuWZokT8fnnVsPfwHpE2HW8uYQhLFNzXgCqEyiRixp6oSuFM8zYwLgcZ394fxpKundMxunN8zzTyLDjuy8nACOjIWLX99idLCsbhA6YNGws7fUIa-2Rm_Xuy2oj24c5P6HoR6Ku6CJL7ULRuvf5OXgwL4ETUywZDXjPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=LTUb9b5mqE0hl8kEKt3kILNwYvXrlo95PxWNDOp84XNG_IvZViwK6bCvucKxh_6CwcrtnurzOrbh9URrqx1PmZDcim4uIu5wsbjJz0VBugS5h9lYpKfKUX6m8PBX5i52x0B9rv0epik24RucTRON3wIM5iBqSostxJeJdA6bXft6ay2LMKuAGOyrpRQ86DDHPbq5m2ZUzvfvNnuAwukqDIxP5yKtPO4eXxwpLAOUHyjebwUPrwB0wihs4hO6S9IKPALqV7jKpwjuhZXyufF-NzcXGH_LZM5OzhVn1XN6niSRFfs9K1dLnzSSMuyYRzF9FkG1MGWEctNiKhGE56MB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=LTUb9b5mqE0hl8kEKt3kILNwYvXrlo95PxWNDOp84XNG_IvZViwK6bCvucKxh_6CwcrtnurzOrbh9URrqx1PmZDcim4uIu5wsbjJz0VBugS5h9lYpKfKUX6m8PBX5i52x0B9rv0epik24RucTRON3wIM5iBqSostxJeJdA6bXft6ay2LMKuAGOyrpRQ86DDHPbq5m2ZUzvfvNnuAwukqDIxP5yKtPO4eXxwpLAOUHyjebwUPrwB0wihs4hO6S9IKPALqV7jKpwjuhZXyufF-NzcXGH_LZM5OzhVn1XN6niSRFfs9K1dLnzSSMuyYRzF9FkG1MGWEctNiKhGE56MB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_-ck1ufxBY7ZlsBptoEAQUX49M66JszI8t3DtT1bzIEVbwRQ5Ql76ij2tF8Dn09EhtT5s3N6jBEKT-NBzQvAwp8vfbb_o6Z4cSG40EuEZRQuOPItAV2YCx3r3bEYaVQLiNPPJBotwrHZel5t7-G9KeNgYe3LHym4xRfxnwmitdcix3fqoaTHY7eoJNu4E-JGQn6s4OUhx175H9vayJuhPde-cm-pHBw6--jqjGJqu3Vb3nV6sD6_-oFiLSHgC9DLBxE7Zxk5AYDoiB8XVWiFwcguenxEUdeN-_xtKebZNQc2C_HmBzO1tx58_Tr00Bu4evoQEd7qheHWxrqaovEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=ANCxAohvnPaLSBu--SUDgSJFGCcEY6nAo-LaLnNQakA9dGoEITbdM7FOmERBBZYH4kZMe-Z0Vg1YsCykQFf9MBnuiEZHX3XzeG4vCpJ4PbU5gUWIFcNAKshBnobAlwsEdxdGXB4ZHKUW2LJFKu63qJXl8KHK9LXL08JmXEoeKDPDJmSY7lPTej9vM0e05RXvE6LKhaDpFFY5nuWAU5h4x0a6yAW_ocMaFna1FY7wZGC6dqMNws9OvtJYiIhLDoIaZQzOXogPdZFPhIgXc1EHGOeVZ8QecY9dCSuHS3rwyB0-NR3A9YkY0Llguc0NflbH83qN1NRG2t7Ti-7PJVqN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=ANCxAohvnPaLSBu--SUDgSJFGCcEY6nAo-LaLnNQakA9dGoEITbdM7FOmERBBZYH4kZMe-Z0Vg1YsCykQFf9MBnuiEZHX3XzeG4vCpJ4PbU5gUWIFcNAKshBnobAlwsEdxdGXB4ZHKUW2LJFKu63qJXl8KHK9LXL08JmXEoeKDPDJmSY7lPTej9vM0e05RXvE6LKhaDpFFY5nuWAU5h4x0a6yAW_ocMaFna1FY7wZGC6dqMNws9OvtJYiIhLDoIaZQzOXogPdZFPhIgXc1EHGOeVZ8QecY9dCSuHS3rwyB0-NR3A9YkY0Llguc0NflbH83qN1NRG2t7Ti-7PJVqN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVEpKpzefv24HNvTX5WPOts6AI8vIxlpk6u1y51VcfFYnPy1mbzhBSct228iZVxSM-ClxEndrptFtG8LXL9mUpEUsT2CllJljLDT_KgHV95zutrmoN5bT9fo8Pj_fsTHjQHNKj0KHfJgcc62q-4P66-rzclKE3Og4AZo98ysfu76_5trIJeI5hud_C75qCznyLGQApN-nrPVVr2CFTFNjkczHQg_9J7sRv7uYmkIzRo75xb-f-jkqIIk7tcdV77EseKyB3OE7Ctvt2SD6G9P_YhbFlvUD_IieL9qfouBg6upJIH2YxlOkZ_P2S0R4V0I7d1bRkimVpP3mlr5hfas5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHOZ6DefukFaYQLmGloo4jeo5efsf7B_oNQhFIFavLunB8XIW0JFCuE9CqkeTR-JCZABZCPvLQC2qeY_EUyC2PWAJqrNAm9L8kZPZKNaEXXvSSbgG_PMYGm3ZiGcZ8KiTjjPvB0LGutEReldyoVvmg-qvZFChRxRJRqGo3oPJg_gU2VwCiuCXWx2Z2NSdbHey6_f5c3ka1m28X9WPrapzLyhuv45pUUFpu8a8giC_Yv8AM4K4Q1WRv28sPh8-UUmY0ixlYntHqDuCA7u5DIw3jy7BO4fFEg4F4xAbI144Ta3yrXx7B9NSyEG9CyCwQcBqtjfs76SHxmo14z_2Axt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ7qoNOTSu9Nhq6nTApljJXOW9rblBoiSHqAvhSsDtrnmksg_iWoNubBsD1Z4jUvV115d55pUNIj_MknerFJaDeyY_WaEOgX3VeYcEKmyxFQ96CLlQy_6zZw0SNSJb9v_K-MnqR7Rkf1x_any9EeUH1fKsNNB7lGbYczDlzCiLM209QppVoEm0xCCT_wWb0TiuG4YMJcCJ6TimKiRpwOvh1NgrLj0Sj9zxspH1USNIbO5CRJpZ88P9Jjg6ZW27-99OMreJ652tybo_FzwDv7jcZq3AbONhGE-z8D7RFdRjoXeAc3CQ5OnQcdqjRnXhTZyMDSnjeqo9qQ1QB7mhwJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJC-pxmGx1TNPNF5s4YqH2abVJxFuWjiq-psVwHDhzR5BShbahgmPEMx9xr-C-pGXJmi-QpK1kRMSFNBHaWyDbvXyu8qNy-jfBlm2cjfzBRmIoDc_4mjXf4oPJ-4HNjnMkvT8A0OEWYsRnMY_eStX4uqp9j2zNFxmRFDcjf4B1IfCmZItgtEFtrcblLEY1puFuKusoIIad6nQuAs1WNW1KdeA0s_nkvIm2HOIyMjK9Ux4hM_AHvpo0oxdi0oHinMK_l_b0P3NWs-DtBSe11o5ZO4Iho90O5JdbNk9frSdw7E45GragN876ed9TwKOQ5NeZ4qaAFp5z55K-sxMgXWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=uMY8BdPSs1Ipv1q5igd611iMWpw1dSdNxLHx_8P7C2JtiVnDfFvFTZngvSigy8fpghKEhNk7DV_HosicWErWotiSWeR9RJp5GMrMBKKyjgVoDOAceAeBlJk4QDfcIGTPTr8F5NW4T7kuM5g2YI52Ep-LPYg7LVfHEaTNUbSRF8IezugXQHaIgqjgBM_doQoDgDJNbuVPsh6bDqcXij5Iy1yha2Wxn3fVeniQuexNUmU0IZ6GBd-3tKA3zCe4ot519ktW--DBPUxraAMD8ZLOhJyLZkYXSa0coehdig2NS4TAHaNSywSyS-B0xXcZMcyPio-QGX3KG7o-bQRS4lg9Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=uMY8BdPSs1Ipv1q5igd611iMWpw1dSdNxLHx_8P7C2JtiVnDfFvFTZngvSigy8fpghKEhNk7DV_HosicWErWotiSWeR9RJp5GMrMBKKyjgVoDOAceAeBlJk4QDfcIGTPTr8F5NW4T7kuM5g2YI52Ep-LPYg7LVfHEaTNUbSRF8IezugXQHaIgqjgBM_doQoDgDJNbuVPsh6bDqcXij5Iy1yha2Wxn3fVeniQuexNUmU0IZ6GBd-3tKA3zCe4ot519ktW--DBPUxraAMD8ZLOhJyLZkYXSa0coehdig2NS4TAHaNSywSyS-B0xXcZMcyPio-QGX3KG7o-bQRS4lg9Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=B1-I0jHvkIHM9HDoJaFfQ6OdTEnWbnT0MF1IO2w-vAivFbmVob4Tb1zajD0oKqBtGVaM1YaV9FdUomL2j05lp4ftCs5sJU-DlbbH9d__uw-YZE0rHuLhCyW1bf2wsA1dzjqHz4wO4uyfEReviDMn4B8nv1YPMOyKyqWWXXA0UCV57svJ917vSLEKCTGmFK77stC39pqz_gGCcaXgQKieN5enDMh3-vMqj7iIirj86yw9XjxmsbllCi_y_5TYi4435xWgmZsow-Q2PZ6bb9yIlstuCu3YtAD15yu6PUw-FECUVILqQfJVc9jkL5Yf71ppY4TonW7NvAqJA-up_o7Pgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=B1-I0jHvkIHM9HDoJaFfQ6OdTEnWbnT0MF1IO2w-vAivFbmVob4Tb1zajD0oKqBtGVaM1YaV9FdUomL2j05lp4ftCs5sJU-DlbbH9d__uw-YZE0rHuLhCyW1bf2wsA1dzjqHz4wO4uyfEReviDMn4B8nv1YPMOyKyqWWXXA0UCV57svJ917vSLEKCTGmFK77stC39pqz_gGCcaXgQKieN5enDMh3-vMqj7iIirj86yw9XjxmsbllCi_y_5TYi4435xWgmZsow-Q2PZ6bb9yIlstuCu3YtAD15yu6PUw-FECUVILqQfJVc9jkL5Yf71ppY4TonW7NvAqJA-up_o7Pgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBLn0_VXl_bdyZd8TDD0zeNRI4Hejvy_rHqAOl6oNHF6ocy_unsj7zsXKTuK4Ro50MS77t57FGVb1OAGo6iZPtl98sOOaRCIXFMndploc2uos4YyxNk0b7VkbzSs_6BOfqadjGE0qbk9J21I7rKetmLn8GmiwUcIqjvOYetQxIrJARJM70hlB6G-oxJj5Q_hrk0FiDx9F9mFKk79jwEuIT0Q0g_vw1YgNXbtDM_AG1ps9PK7nST7SqvuGq9cWxt5w9TiyvT3bICF_-qDY7HlBDJ_laMwQoL4a7l47tC5Yk4c7zVTvsOeNsMTJiw1lTzuPp7PVo49fKSksUQktB3lwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDSoSXETNR4NgiQNRbyxWyymDHVDrdb-VSTEweUmae0lYFPYtJeMOYCahJapx5jG6v0UYDn7s_mFKKQhS6qLicN0AbnLZ7BKialYNkOa2Kyo-vz_54ySigO_M-pWjemNWtxCWPw3uZcwsQlRkb_9JCjeat6BsLoWp84ovpbM5MrhBP-afMkEehd052JeKAnMm3QyE6Aac_c9Edj-5zAZvC3omUz7aQiFtgbVJldkZWqOd0du7mc-vHa52hPfJQrtq0i9gIjlxUBmpdNFZS11BODhM9o8GbXqzdEFRahMXUQPsMysjEpxiCKTaPn7Yyt1hvzfKbixL9gwBjBc4EZjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6pZkdBztC0xQK7xYoPEq_IeP605cq4wn4o_lkivn0P4m9LgG_cdkxpyHUHXAxZkwhqbADFOXIUVcuVOe-kS5fMbW9-mqIIy3pET-pkAYYjIzEzVLaj_h0W9gZsdhwSztJ0tWhM3wAr52BMRQa3bajoeA4KvKA7SruF2PUqifv1pB7llUTWO_XLoZFqxx9wrbGnFiigUL-OhNAeyjO7mXWIMG-j4XxYGj5KzJXDvEKtZO4qLCbmizhjqUxDfLZbIJOclNd2Q-O5kLkY1yPayLVtA7hpYHS3SLy6WakjJ_NP7MRj0fgdBW18GvlRQPpHlT2O1LaqNH6FCMw_3Fh1aFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoyrDPy5wp6wF2ym2O-Nz4xBfgiG3SAbWncN-EpDxoZu6SF-E2eyf58XmFfCI-W2sICB0y3Iv3peXftL6PYCgQExWo7QVek3e6WAgeXKdo-xyBhZwXVZUk0ChaSL4_IibR0wqCK6eA0dgG2-Lo4ZmTiPn1TESVdVMytJKiNlY-8TcGAVfWPYB_wp8R6NGlW90fDl7WC6_SJPWqG2EZmAxT6lKNfUYekMTeeNwGGybG9N2Rg-P0CIQJhxZdlt-O1zFoVivFCfNup-F7wFgKCkbPJKMeQsq3vvfZTnFJBDUtZktSRBYNAVkyzsfh1tcMf54swCWJm0HDH_gfmT8egA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRODhy3toWYD60fvWB8hDHCYWEGLWjps58uF9XyJTB3kkqiPmHAF0MG0X8Fqvgw1BrLUUJAMd5utr6TQxICnN39s5nMD8r-VCYMa9ankWej9Tz58why7Ac2r7yOWx4V40iyQZ62ZuurU1-ij5sEIqfrpJb-Hte_9BHl08aON4yHfArWkVLmW6eYoPX0jFgQbVpxBKRG9jUliRNfCupsxqrGN3lqRQ4NqOTP5Phft2FYWSIGftGBlFP1H1zHwb5xQ3Vt0hbU1qhovxkhQkTdZKeMXtoibxIcYZtBBedple2b_-nPDf_6ytPy-juOeD34RF0q3h6VuviVmPK3VhYhpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is23AqTlP0NvEfTtTKepvunr7GCRvIODloMd2L7pEkfq1Ggf6_TBra6SqfRYXZM_mXeWmq8MGDVK2F3V5UFf3sroKBrVZrYLu9VOt_l-mf8m1YdLLRekOD7TF91oaHhIWHxs8wvhjLWUMuXfJCN9pkrnZScrBRTKmSgXuekv5zbCBSiLF0_H0J43F-3BKT6wjsVNrxn1mK2zyRM3x7Du1z-b-HaTjvxFeuZBVdJiGu7ebQPx6xaVUV-erKd6IJKUDf4mzgmAsa1QFJJ0JAi1eggfqIYSCnl6S70P2KfBoqyu_GU70xLO17DupsQR8dmFV-qucb638otT-Lct83xA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsGa42lfFpoRAMDqgYhgGk24QA0LdVz60YnKqnCuQ0TS47-l9AEyT879q6SQzjNECGhYA5OokW27SVpv98OL3WSiF-is7LSUlX5VB_MLQtAIL1BvID3o935ts-lTvVUy_iopWONlf8d9ZhUvRM5IOiXXqUnbOaXvkcF64l2-XtvaAcCXAFWedgmRiIEuQv-j8IwSsDYmYTbPN7haXsxgZXc3rWueWWrRAMrW1-N740-DkLBIGCBkFJhYOgAO3b0ZnvLt2bj6a8mQuUUsT4t9XCKJzz8IOCFHCkW7p39y61aS9QQDz-1iewnNtjUxa7U3vWFCPQqsp6pRHWRvKHE0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GryuHQC4pzGYrCOWajqJKHPVjrq7Zv_MSOBOmlmES8fNhA3PHX6B_eMsm9h-kpTqwMA_pjS5gpoCRET0Y4xhv2PP6TuBCthS93K5P8wd2tDVY54Me2f-b_slaen465daJC6LOu38yo-LE7CcAIdPM0neCb-o9wG4OB0dINhSFi9BX2FOjPnZaILkZRv534TSSVc_bsXBefsAWd-xGlLsC_0WQO5rjoCrAvm3S-oTgcx1ZQL-58_fqhjBi91qEjfLTi23wyzTVrmNPZMmL2t3pt156GkuQUNGSE-HzZNavd5a_16EpJADikYw4PablRxQhPNH9aFC6houbERiRi_-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdKwYcRhdcAvEYl9tpMubf2JSWWqFZnMUM7qbRVCh15ZjJTXCQSsetv0bSYL3XNJEsO27P32KpvYJbabTv7A7NofGwztwiL_4Whfl846GhHQc7clXk8QXzKslIMYZ7Mlv1l8D_bj4j_BzWQRt_KLIrThiYUxUi5o7BBKdUPvInjTLNue7oxfSxzEnt3luhRRuNst3YbeJJXjUvi5nTSBNRfQOt8xf6DCbk9XI7DHI--tFK5Pw6FajAdiOmBO-MK-iL8VlRNVYRyChbvzgrr2ObbOkeM88Qom8nd5NhOFOPNDSXcurW62AV3KryeBw_rVd4Ock3nTmkvLNe1iglxhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=Dag2h5qE0_ugTtdTTLe9Mh81WoQtm6jwatsJTENtZjknM7ZG-g1POuALTux_JLsd5dZ5Xr3C34bBmtftL71J5sirLMGhDi5ShmOKikhPdKYdvnrJcu_QlgCS9nnR3U_FK1rzQOb85cDT31JjaSYEvnddpAWHlsHbiWqIVNdeuc_aLDNP53sU_Wj3xb5CFfFax4hUcsmyuQYAiKWtk9tWQRp8B3LUBFyS2zrOSM-cebNKuFa09ZFJH53AhdONWizBSmaoB8_3jtRHayLkaxp7xntT_dEGz0XzOQot4UZYpDQtgTRpRRONXmcM7vQpNoky8hk_18Yr9BMV1i2aYoEMpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=Dag2h5qE0_ugTtdTTLe9Mh81WoQtm6jwatsJTENtZjknM7ZG-g1POuALTux_JLsd5dZ5Xr3C34bBmtftL71J5sirLMGhDi5ShmOKikhPdKYdvnrJcu_QlgCS9nnR3U_FK1rzQOb85cDT31JjaSYEvnddpAWHlsHbiWqIVNdeuc_aLDNP53sU_Wj3xb5CFfFax4hUcsmyuQYAiKWtk9tWQRp8B3LUBFyS2zrOSM-cebNKuFa09ZFJH53AhdONWizBSmaoB8_3jtRHayLkaxp7xntT_dEGz0XzOQot4UZYpDQtgTRpRRONXmcM7vQpNoky8hk_18Yr9BMV1i2aYoEMpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=sF2gdsScRfMvJeYszpLfn5OcBlEfor9NkZW656SZhPfEb7knRm0CKqs_rDl2NxWrTgkePEnWQ1sexbqfDk5hHo9f3oHeu_JzLyPRJRRdKe8xhb8y4sKFUrGNut8dRQkBYmKeO22Of91u-YZg2TqgHjlMpSxl1kTtE5TFBHP_Z1Hdzq_BIGywnguJE23nkS1zTjgp9-Rqf_1IMvOQjd-395Lw1lcfhbt_KaXvbfwpuHSeQLFGbJC60Th31RkLgMt6n6MLgl_zJjpEOs547tyGGemo2LB5cxsQktBr1OWYsADZ6bSb4fa5xcg2fnZXnPN1Yh0Z2kbXEFfQ6nYAucDSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=sF2gdsScRfMvJeYszpLfn5OcBlEfor9NkZW656SZhPfEb7knRm0CKqs_rDl2NxWrTgkePEnWQ1sexbqfDk5hHo9f3oHeu_JzLyPRJRRdKe8xhb8y4sKFUrGNut8dRQkBYmKeO22Of91u-YZg2TqgHjlMpSxl1kTtE5TFBHP_Z1Hdzq_BIGywnguJE23nkS1zTjgp9-Rqf_1IMvOQjd-395Lw1lcfhbt_KaXvbfwpuHSeQLFGbJC60Th31RkLgMt6n6MLgl_zJjpEOs547tyGGemo2LB5cxsQktBr1OWYsADZ6bSb4fa5xcg2fnZXnPN1Yh0Z2kbXEFfQ6nYAucDSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=mgYtcd-9rMjPAtzcpCeY9VjKw22OHMJVblHd5NxxdJgOZmvt6VZJ64IZa2uj4GUTD7g7FMm0nIsaH5EeFk8SUD0jt6dmNFv9omgYF-oIUKh6Kvsth8oJL1QRifgsNh7ImA-5s-k8a6dcjOgIDJU3KlQ7H7_J7RGQo-XTvd2bAUPA6dQLnKXBReKu53W3WzXx1RY4Zk8x3n_Dg33FfQjEh1wdG1DckaNCd00KVu9I22BZ0EJObu_DEQZgRuuhbYmC5MEFmRYzlYce8BTi9zN9_DcIvW9duWIODi8Yg8WOo3VwkhWuPdiD0yU3N6DklqI00Az_2NLq45wkW4r5HE7g-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=mgYtcd-9rMjPAtzcpCeY9VjKw22OHMJVblHd5NxxdJgOZmvt6VZJ64IZa2uj4GUTD7g7FMm0nIsaH5EeFk8SUD0jt6dmNFv9omgYF-oIUKh6Kvsth8oJL1QRifgsNh7ImA-5s-k8a6dcjOgIDJU3KlQ7H7_J7RGQo-XTvd2bAUPA6dQLnKXBReKu53W3WzXx1RY4Zk8x3n_Dg33FfQjEh1wdG1DckaNCd00KVu9I22BZ0EJObu_DEQZgRuuhbYmC5MEFmRYzlYce8BTi9zN9_DcIvW9duWIODi8Yg8WOo3VwkhWuPdiD0yU3N6DklqI00Az_2NLq45wkW4r5HE7g-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT9X0pYrzuOf5a_mKmBaP7TUMXPPgNLzmIQSzArJtStQ-MP4wkSup7hyvlipOdfaV9HHavLBSmrjT4w09Cr2YSxG5lfx_E302xTH3s2K2A5qFZux2bAXCe9PpKyINj4HdQ3WPbRgcuv5mEvbmiukAAKOeSe3EbGo2TAkAnva986caIKUgKd4kzJJ1L8D7J5rfzZ6f_tdcwCTtpnTgZig808_vPbMLbSjQGTO5SgRdyQFZwIUc-cJugJAcczeYXgpSIN78gO-OyR5ICuOHKz-Y4OjueVfNETzgFiUT-n6C1g9GUnLOeNiV6m1T-CnHsUarwIVneWKxbnWR80opvRQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccmFx3TFoSCjsPPilRGoX71dQcw4AN0lpUvap9mjeojF0BJRisziT2mbY7ZUt4qzdid-q1qO_Y-CVENNbsgHYnfg1VPK5C4MqCKLuksjv52srOvTGVng-Mc8vDnGyT321COiHt8giRz3easBNh2aAj7_E-m-LKw50WUmyGKYjScJWSXJP-FkoQ6qBXDOaMrvZ6Jcr8f7HMbvrsVaO3Hn4XjD3FS4c5FXI4JhvSZUZCJGPVq3tbAYxxJ9YkP8GU25rfI52Ti4DYWY1QXl_sDBQv-AqGiWeGiKafWLnp6BinN-MqMN0EdarRY8m59av1qOj62WbaUMkDkJJd_xqYjixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVphOZ0yWCZZOCbRbIn04hdEY5HjB6piQYag1coAM1FjStw-MhcFO6IyjkuiZkqXz0cf04uET2vPYkk5z8B91lJ30PNfcaHeRHVU1lFqdL6FnHaFv4WDayFrVO70uYcbsJkLwpS8tEGmRLWZ0f2uptBTLhNhhsI7lDTgsxvWXjhKcyPYqaIst5SMZHRup2ktJlg5CSgKCd-WQlJsOlVNfBkiNk-U4cDZzUgwq6rQS9lPu7TwCCPrBkTubiLbivscxuSrhhXTR6ToB9j4HC39c1YP5JBuohuRc_GHZoqRA7Gh6M3RKUSmCULrBkWV5xridmzWKIKlXRPDDwIwehVGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzQ2qFZ4KG0G1-HgCYXTZ42ksah3Egxiog6QHe4aDcNHA3pN7AAUvE1TVBXJUuyK3QdAw3dWg4OStWpkfd_c_iKLijOXTAnKf32N9c0xa87I6fPIGr6RtGZ2MMrT4mEgTxNnh2D0lvhDH0rciKNvH23Ivz98ao6R90lZtgHeqx-0y38OFUIIBWS_cHal1Lev2JMmNaIq9HiM1UHzXyEESZIQHj48YMJi8I5VHgzFwfnYZbzAVBZlsCd445k0FdC-0C-sWiimV7BjX5L2UsjFLUXnUUV4DCQuKMja8rBMv4C8nzCyHK8_CeYvxMxsYtBpgICkkJQ5Mb9E67BN3wjdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEzREQry17Edg4WdNNTIeyGuCc7pZzTeFeCVXMtTVZh8bNqY4aSAuQyzvr3FRy5izJL_JI5LNzS2gj_gfOAg7o-B-4A4zmu7ElZJDIfO3xT4Kn0GrSct07x1hJHP0AqBe8M78f7ulWpTwFBh7s4SKiJ9Xr5VmHaX9R7XViiQI8jULjnzn-o4y2Uykwed3zP3ij80-vw8dz0hIjgB79bWGwFowDeKQP_wCuBmLaOk2Yz1yu8ds1SaQUwDl0nahMHG7IgBFC08oS7hP4lqA4PgEMP7rAlVEVWr9XWB-M_0J8OlOymCnKIcYAGdEJhvS103jX_NVCA4tp7N-jehSfzVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG6q6p5FWLKQ8CP05Ce3GJI1UzWXbVk0qrFQVaR3yOz6PM1q5ye2B_tPwQBR12A3eDGTojXgUSAp7MRAY4LE_Znhpv8Xp2Cck3lr8Qyo05-G5T1TpMIWTK0xtv_3wjT3l0J54qDHd_tPe9QNSXZD7-cYhNixqSbA8FyYgvTOue59Qf-hAZg7BKJh7MVl3CsIqI4vbfKHUkmMrXl2txnhXrQWNHrI6vdEgxzRQKTIVxu1wmuHL-XebCFWDXldec7sf_mDiK-3jpN6_RgMOnTqP91olsq3qLLrj-OH0kb0szWurwVKNsg6D6HXrnDQv_R4-sRKoWN2VNJCpFmrVIPVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23eOmGfIeQv3gzGO_hSNVs0xiwztHAN-vJY5Ez4HQwBhD67JnNBQq0DhRkieHwgHYNiGTNT6Q9SsaoSqawGIbQUOxybbqMPvQVjRRv77b6JNntL3sUozziOQgOzzFVbPq0wgOK-dpdSW9-9irPmhK3WCAB5laKty1YmpF1QmQS0LiVUWZc59LhNUz8V-rfjXXbjuAIsweu90gRelFZkInEQAAAJ7EpSiAF20bjfEgLcmNrwNE-hbOz07lYroFEgGnJuypT7jzoWvf_3moUbHxQ5uutUxQvlaYY0Y8XA5kSrj8brlwfecf2Xor5VW4Oxa95qHpcFaB6vJGYqjrELyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyYA2ViqpMrON2IrPJSDBftodDPz6I8YYY1l9DlIQjoXuv4tjPUpsVXbQws8BczeFDyqd0ggpGFvBN973eFcXlAEpGgNOg1RAA9hT3XYgqSh1O-TizarBstS77iKmfnnf43-3L_eQk60CvwR5VU9wIsPasqj1cVJCLsifOSCPKT5BV2x19_C8xYRRqxfYx8lUl_XY_HwKBR633iRcXiUlGOTPEujr_OIJ0Nd7d-27yksmD2t566gSr9USD-5R0cEmxiG67lW1uWXoCETr3iZWprTHbiMM5H4kosn09dsB0VaCbHgkH4qskifPdpS_eyXVRmd3RI7slYfDQDYbeNkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FS25gltkI1S_CYGqb8vCipSXk-c72HQcWSRG1XcMmGKh9iSH3xumSoFq3XPV4S9EnT_N9PLYO-IhciKNY8yVPqd942ZM11ZGpNguV_J3Ah1sxFwraHjg5iKkN9IkLhRrrLJTvojQVaZIw1enr7HtKDt_VnEVK3rBqHqerWzucK4kkhSmRQbPEG8DLH79vLz4oLwSBdA93R1xPj_2XA2VbTHHuQSrPMF6ZTOKjNmWVTDm9RTsrsCD1UIjrw16YxCmCJswWsjNyEsL1Sw1zWhQ8D6rl-2uUVNnWJutGAB0w3QvoBJemCsLryrssbUb37qomYPXEHqOFpGyujH3TxksEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=g6Z3Cq-TvOMhtchRHXdgWqvuxN289UW7bIBkrLQTNJsJ8ydplaT5zSQK4gx0cfGA4Q_4CdYqwzHGBVKxYcfAsRKcDzkU1hLpjXRCZtD7TiIBzh4_tDKZb4g2h1IMR2E6I1UIfl2WMSlRb-k4YTFe028-8xRiwofFRE02fs872aluJQBA9zecJ245mv7KAxmN3HPp4LMg0qC3omMrpdMaU74jYltLh29CjGnPa59IchgEzSj--tr9EsKJAfvL0kQBCqap46VfppL-JOKFhbgfAuKwMZUAT-gpI9XhNGr6Wvhw5JTF202r3OarCHfZzi5u-SLzChYw3IR_c5ivqHdW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=g6Z3Cq-TvOMhtchRHXdgWqvuxN289UW7bIBkrLQTNJsJ8ydplaT5zSQK4gx0cfGA4Q_4CdYqwzHGBVKxYcfAsRKcDzkU1hLpjXRCZtD7TiIBzh4_tDKZb4g2h1IMR2E6I1UIfl2WMSlRb-k4YTFe028-8xRiwofFRE02fs872aluJQBA9zecJ245mv7KAxmN3HPp4LMg0qC3omMrpdMaU74jYltLh29CjGnPa59IchgEzSj--tr9EsKJAfvL0kQBCqap46VfppL-JOKFhbgfAuKwMZUAT-gpI9XhNGr6Wvhw5JTF202r3OarCHfZzi5u-SLzChYw3IR_c5ivqHdW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IyHC1vwVBy9z7PxaH2mXcR8oViUvA_CHbutnyowVoQx77T6HX6NS5YTg3Qe9AT9q6kBmbJJO9S8lVoi6Akmn-yD06cRh0j9_9HN5fz5KN1JR-RvFnCHEOps8Ts5MfF1tquEK9NRJgZTtZjhs3i51nzU9BTa3Dv1SebNmCSfQAkPdNwWAcJsa2QKMWVM9rkyxdt5U96FBP5ZspTvPVG-MpB7Yt0voWHC3eCZyiS3qXNyyUl4xz5zyY0GmVsi6ebO8Cqe9RPBlU8xv7nhCa-tAj-xXLHhLkVhsxLmNtqpcHgRWxsQynK3it5S-OsdTnGsnPBTzwS3Cu4k3heg27FA1pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2br2_T0OgfhkdU2RdxS3QD1AotqVRQMvMJMRruUu1AItewpugxRtsda3dW6o1OrTUjuu5ZfxBBNXvTIvGXyQOMMYc3ycZ54W23cbWL7hxpj6vluOHXumseTwMydXQAoR5UiIWwlkmxNY1UJSnqweIvgkof541in2Z3IW11JIMywXQ7xbBqg2qxC24CMDt0maUv7UEE9oNAiDwefvEBhZcqDwyeYNTTR_M093jRvsqAzUydbthkcjor669lxcA9fGMHiYJvOJzsDOdz8c3Yxzp5tQEx9LZsa4HqQLL6g6thKlsaiS62ZRRaixpnJqUorlDNLIewXBTu-QlLp2FCYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkjxlvDTXmYx50axfAD3xkswsU0Duz_oAMRtTHXNLsfpsqY_9XudnetGbtRGFrQ8q9y0puv4lj87ghqBd9reAKQtrsufHNBC8yYj0tPsp72ld1mu8j-RPaJUsEFiaahUFgbCqQovE1UcA-YjFNcehIMMEorGR614WZIxO9qUenbHCh7rABQB21sg_OiHKs04KeGj36dUdz9uWNKCOknpxLnhcR5WB5r1ZoA8agYWW5QZPxVQe8y3MeWyVoQmruvkheorxZBVdwGv7E3eNwtqPJqOxJ3ZJdh--rj9Ud_G8pkWnr__YrfRos_absjd83JEHIIk1mjcX5EL2RiO-30DUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ho1cVACqjPj920V0l2p9BtX2uZSGjDM-OO5JhXtZxHNuG_OSEeaCVjscuH8M-VTKowuuDge3GiKn8RulVqzNtaHIt_GOzpHX34GXasX9dilS3I3TQVf7-m8mqad7q_vTuRa2D85KxXArgikLSzCCRsZMMPTCR4dh1HIKl_RXzY0P_l9wC8AI2Zn5GtzIidrhPJsvLpV4GRszltrAQCYUoayN8mzw5qJH9XEANpd-O9ApCAo1HyVSxqKSvM-DFBw-K59vY8A8s3n-kuhhq4U1OwxPzmSOyzmeo2O7AD5i9MgL-5poNVd2qzDLlZx2k3hJ4e12sXTocU7tJEHUL89Lpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=i7jcrHGerPSXfLxNNOpUEhckWzxd3y3LosY1MMsb0rdzatK_Aum7hWN0WbOR0AFVevCgzdG5s-GvIayqT0yrUvQw3MM_9FnPEllCCuVvaQ83ROBk9cYu3JHj8-VTzLtT66NKqlrXfZdVYWi_BSZhD8AXLAuWwGiCX-AZvLK_iVmmGMcZgZVfbiH37yz9etwa_qEj1KsnrpU2jB1CfAEldJURumhPICpSbUZEgQwFB-IznMNyKlmWp1PcI5H89GMesnu_8mERY6CDPr-Y9gTzs-mcsV3-DliYiG5mrZ0LqdMlrKFFeILimMhsqSYLhHBqwskr14SA2q1qC4wpWmIgnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=i7jcrHGerPSXfLxNNOpUEhckWzxd3y3LosY1MMsb0rdzatK_Aum7hWN0WbOR0AFVevCgzdG5s-GvIayqT0yrUvQw3MM_9FnPEllCCuVvaQ83ROBk9cYu3JHj8-VTzLtT66NKqlrXfZdVYWi_BSZhD8AXLAuWwGiCX-AZvLK_iVmmGMcZgZVfbiH37yz9etwa_qEj1KsnrpU2jB1CfAEldJURumhPICpSbUZEgQwFB-IznMNyKlmWp1PcI5H89GMesnu_8mERY6CDPr-Y9gTzs-mcsV3-DliYiG5mrZ0LqdMlrKFFeILimMhsqSYLhHBqwskr14SA2q1qC4wpWmIgnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz0RaIaUnGpglEx0bXS--M1lQX8Q5LujQb9HsapHZCBoHr0cHMRzJ-6KVzaAi4jOj5OsoIaNNA2yyLDSxwo8dTJ0_5QyOzZlQY41T2wGex8n45L0ldbLU8T09D8CI1lChHtX7J2c45VrpZqZ7SHPcuvAxoV1eP4JM0I_BAGtIEyyF-zwe9TZVJ_a6N4CtOefGP8hHAnnHGG0Nh5cgXjHeI-lMR4mWnuZjWOWUHCuuTlW4ePAloOI1dMTJSamJXx3tzl498FQ_GffP6o_o50FM9gVIk8Xs-PHsoTjnzX9Cm9vUxuz_ws9aq0eQPVdZNnoBcVm9pZNYlph6dOQXi4buQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=Udr5TvyjeMarc7rS7gQNr1Wpvt28XIeUwcLaOpbMJiCZoA7J4bAMtm7uF8WhNj-isfanon7w6M0aD_TbCXoBjtSnPhceXggCVJVmegf8HMW4shn7mLprp_qZTCo8TSEBIMiN0zrNWb7dkb2ttyPtbWHss4ou7EBit4DWYppwyw1ymIDtQAvCdbkVDvziemBi7KXPubWLg_8DrvN9slcr38E14HigrsWcdosSSV588azLZmfF1fBjPCny-g1bd5t6ssTvR-fPadUhKc84qkTNxmSnV_xeSq_LYdrHdwY7p16fEVQTo0PhTecR7QdUFh_mbe77jXvNo98Joyg5r0WP8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=Udr5TvyjeMarc7rS7gQNr1Wpvt28XIeUwcLaOpbMJiCZoA7J4bAMtm7uF8WhNj-isfanon7w6M0aD_TbCXoBjtSnPhceXggCVJVmegf8HMW4shn7mLprp_qZTCo8TSEBIMiN0zrNWb7dkb2ttyPtbWHss4ou7EBit4DWYppwyw1ymIDtQAvCdbkVDvziemBi7KXPubWLg_8DrvN9slcr38E14HigrsWcdosSSV588azLZmfF1fBjPCny-g1bd5t6ssTvR-fPadUhKc84qkTNxmSnV_xeSq_LYdrHdwY7p16fEVQTo0PhTecR7QdUFh_mbe77jXvNo98Joyg5r0WP8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys7tiv7bUlWhI3v9YVc3WsWN7dfXC9QCfC1TIpRyuNEImldKykPnKthWsNXukFaa99IONIzEivfG7cal3pYGXJHjF1WKHf3XJl_xDdYM0nVm0DwkFK7GRahrx-9CWqGveqiGi5S9vsvKuNY7curEWQkpw1B7W0UHxTBZwGC7MCq-8zQfkoSNNQhjR3R_JrFBkD_Zhm07pDYkd3j41nzLPTCCOL24uqOb5AF7pjDKtf56mONoiIaOMO9fpYjueSKmWMbLCsNqyq6HAek7dwDjoiFdU0-hQ8YDX_3q5IH_7vOcBachVIMZfxYiDekxrmz5sf2iW0GF-FQtmGE8iMH_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4k1YugGPX5Rh1QvH1H8YZrruigD2_EYyEGdQyMkNvBeCHUL-ANCTwIwwCcWhVLBcZFqCApL-JlFPYmkEGLYnkP5CppDIYiG_ZgfCbDH2wI3zBgP9VYE95NZhl9R-N1pPaoWgcWGjFi9BbY_eLIrlKhQlJcDHdunVkyyMvt-ok2nDWPsTXkr6WRufKC0aaCjP4wap3of4qE465Y2A_7_KsuFzwTO6e_2M7f9m_fnJpIJSg5Mi-yQeIwNDt1q0amNBwR3f-QMRk0pJ0-fNz-QOzRdr9Ajs-n2nrVAmH_2I43YSmHlSJOgZ_OwlHaa4gQxyZOz138rUBqVd7uty5iJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=qoQnYp8IT7BD_sdAhjyZQWkzZlE6iAc8dS79CQE9dQk55853u93foDwWRnbLpYk0Vk9AM1jjmtUiTCXQlVSLpft8loqUQIMX5E_KAHDP3U8DG6qE53pXwFFfIU6ZUalMtgxgZ5-iFkH5EEgJb7Tp1HaRCTiB2YhTbWwcGD6WF6BGSnjmGnxC-ubEd0EhXzt2XokvvGw9Ckc2Tb0PugFQikVLa9UBZzH5s8nXt5SHxNnwAqA_W3GSVIz9mfocpsQggn1e0j4BJbkLWEIUdtYnOV6H7LfPrtNL-ApKhtQS-APb7DZyxhnkKNeTakhpYePR29-yVi8RYRttwyo4MrFaKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=qoQnYp8IT7BD_sdAhjyZQWkzZlE6iAc8dS79CQE9dQk55853u93foDwWRnbLpYk0Vk9AM1jjmtUiTCXQlVSLpft8loqUQIMX5E_KAHDP3U8DG6qE53pXwFFfIU6ZUalMtgxgZ5-iFkH5EEgJb7Tp1HaRCTiB2YhTbWwcGD6WF6BGSnjmGnxC-ubEd0EhXzt2XokvvGw9Ckc2Tb0PugFQikVLa9UBZzH5s8nXt5SHxNnwAqA_W3GSVIz9mfocpsQggn1e0j4BJbkLWEIUdtYnOV6H7LfPrtNL-ApKhtQS-APb7DZyxhnkKNeTakhpYePR29-yVi8RYRttwyo4MrFaKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J02GmSzAt_q5Drmju2LqP7csx1q8Vk-dFJ0GdEWBOVyzhHnfwqqpg9xqU1WIpyKXC9KopqxJIrg5xqOLji3YC7-Mw1rMZXNxBJD0Dsl-rUnfKNr6BF-O65sekR0puE4a_6AnoN-t35pPxMJmwy_s7HEO0J8exbx0SRQMLWxo5nR9X1CM6Xgk8KJe3pvQPA_hMWIoBwiR_CrlRtsQPDisyOZoYPUHNJ9VgKQ1uINiX78rUWWxqN1M6hKT_HDd0Eaxagxx1iVxi9wJuPWXRsQaPjy4TQb298_RCJykj1_j0tE2Lu3gvylY3Ko1mI6ODj4jFfDvstbaW5vIFz-SoG22Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
