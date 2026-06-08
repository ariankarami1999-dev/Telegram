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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 23:33:16</div>
<hr>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG5RMPS_pTLU1v55QAEFcOksdt2MfA7CYcCGEFpWS8Ac25UcYO0gKrxRZdSC2igAug2ZmexHtUlStFEntaJB4Y-Iz9oTJZKqDXmUDrQhC3upjVLXQZJIStqDmxO2pX5o-GZRX3Yt9aauVon8reczj-JZS5l-wYydKjBYrQOf8b3hV9097fs0EXp1A_n6P_ef68qWSUpO5f4vW4xfP3jWNUW9I6RIib9LFki_icXCDjecrqDUs-TvVnI0gvnVBGp0lUK2Vu0wnVPqKIy7Jl1QLB4Kl3xdbMoiQXAqYOAsJNOONxszM-ETxuNcxnbJiBi-j4uyEOZFxmE9VS93VG-x5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAT5Yo62vOWr3odIdejd4zKBzhTgEZ7K1oMlwMqls1VUENGPYGZSClaIkx156X5UFWNUh8sPY70XU8ootnu_9hDyFYTewwZgnzwC5sG64ijS6_j1bwpCveEdlZv1NYVJgcVqKLYTmhm_d_exTz9lCUH8Fs4bXGJitqNGqAb5HW_kmyt271r7Ub9qT-w9xs0U7PGWxIgLWr5eM-juAHq7STGuV4iK_ZsBdyk7JiJMzh-Kc9UQVrXrW7iJ00aVycRYBFBDLg0dljil83-G3Mex_TjU1XD2d80aStWT5pj3i770Y3MTJfIHov5eEi0b3BhjhPJNv1mo4dcpc5GLr4IUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKLcjLtymkdAPjcMUa41LF_UH1rSbwYCEJAtHXbJuBEVZ7iioIqic9oa516HOBFJHgQBopzOEx8qqfuIN71VeCB_Y4ixJl1FZ8uSCa8epcFyK77ZPxppk9tTYGq6TZX76sHUqU_P80ezjeEZUtWfSGhrQvkcQJJbrMKpEOAi00p-Gt_tK51Ra7Yfap7vXkmdV2R9cSwNWpZwfK0itbFdjIi42Qu2gRU1kIwDyr3CirkcyJEeDHgB39A2-9WPQowhXSLtT3K0QWg8xOkjaEEPzHtgPbJkLrR05kImstWsQ-HZPNWRpEiIujVGw3out5F5jG0Iw3qF--Z2ImNgJNEPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSI6XhpcKhhyX-p4jUn3coWb6WKpydoMhMi7mOO16YKillKOdrHM-6XRWYluAVn4hMh5CRSV49uugBKzhEm9A8pAONk2iHxv8bGf0_W44BB6C7tTDjg5wQqUj1FoKJOor7iqXGIgXyV4gCd0v1KmTdTI29zhB_5QDooB_eCELZgD6YCE7ubjiKnefDgHTlDeeoLlYkFKvKDWRxkxcmgyyG_l-aJ9sQp-YTVtaAY2zJ2f8z_aN9kR6pTc3Qu0Y7K5I-FmthVkrF8p7qKAb_pj-ROWk00UAQsSCaiiXBFT2IE-kAk0WoWO1K1n66X1AyO9lf6xs5ZX7a2K7l3iM0r5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cf3PHh3LtMSh_zqSPUpUCbFpArE58y2EZBDd3XBrKfGl7acfotyUSb9BJIkQ7Xz8SZ-nHyWzRRDsP48UkH4KYpcgokq73jrbnJnuN-sHC-hADvwAOEZxPUNR1CAqeVvc0bzgL0JYyybxeFCQAk0wvOvNumPJhttHPbgQ9Kgh539E7MZW1B1yaRmJzZyAhEpXInQM2n3z2slnuB1tb-ETkY0AePZv18xGW70nWcSt32BPIVtgndQjaSJG5LSrS_gQPs_ZUbT-sHZxuyv-kNegwEs7yh_7kmKf-7m50pBK8vhki0dcem-QpIvUDtXoj6Z1NNRHNENnK208F8Bf9aGATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-IdRHS2E1ilfJj-RAzHx3GTRIoC7AmweePIbohu2q-lhiuHCo0TPEjmomAv7rSvf7xP5U2ZP2SSdHGZxZfw_s_MP6NOvNQ0oJBLlhqMFHvflqZlensXogQPNJGD0VY-ax07bYrxUDGpvM5u0TZJrqTQXuPKj3aPC0KybNxIjWVfmVulZHuWZokT8fnnVsPfwHpE2HW8uYQhLFNzXgCqEyiRixp6oSuFM8zYwLgcZ394fxpKundMxunN8zzTyLDjuy8nACOjIWLX99idLCsbhA6YNGws7fUIa-2Rm_Xuy2oj24c5P6HoR6Ku6CJL7ULRuvf5OXgwL4ETUywZDXjPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_-ck1ufxBY7ZlsBptoEAQUX49M66JszI8t3DtT1bzIEVbwRQ5Ql76ij2tF8Dn09EhtT5s3N6jBEKT-NBzQvAwp8vfbb_o6Z4cSG40EuEZRQuOPItAV2YCx3r3bEYaVQLiNPPJBotwrHZel5t7-G9KeNgYe3LHym4xRfxnwmitdcix3fqoaTHY7eoJNu4E-JGQn6s4OUhx175H9vayJuhPde-cm-pHBw6--jqjGJqu3Vb3nV6sD6_-oFiLSHgC9DLBxE7Zxk5AYDoiB8XVWiFwcguenxEUdeN-_xtKebZNQc2C_HmBzO1tx58_Tr00Bu4evoQEd7qheHWxrqaovEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVEpKpzefv24HNvTX5WPOts6AI8vIxlpk6u1y51VcfFYnPy1mbzhBSct228iZVxSM-ClxEndrptFtG8LXL9mUpEUsT2CllJljLDT_KgHV95zutrmoN5bT9fo8Pj_fsTHjQHNKj0KHfJgcc62q-4P66-rzclKE3Og4AZo98ysfu76_5trIJeI5hud_C75qCznyLGQApN-nrPVVr2CFTFNjkczHQg_9J7sRv7uYmkIzRo75xb-f-jkqIIk7tcdV77EseKyB3OE7Ctvt2SD6G9P_YhbFlvUD_IieL9qfouBg6upJIH2YxlOkZ_P2S0R4V0I7d1bRkimVpP3mlr5hfas5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=uMY8BdPSs1Ipv1q5igd611iMWpw1dSdNxLHx_8P7C2JtiVnDfFvFTZngvSigy8fpghKEhNk7DV_HosicWErWotiSWeR9RJp5GMrMBKKyjgVoDOAceAeBlJk4QDfcIGTPTr8F5NW4T7kuM5g2YI52Ep-LPYg7LVfHEaTNUbSRF8IezugXQHaIgqjgBM_doQoDgDJNbuVPsh6bDqcXij5Iy1yha2Wxn3fVeniQuexNUmU0IZ6GBd-3tKA3zCe4ot519ktW--DBPUxraAMD8ZLOhJyLZkYXSa0coehdig2NS4TAHaNSywSyS-B0xXcZMcyPio-QGX3KG7o-bQRS4lg9Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=uMY8BdPSs1Ipv1q5igd611iMWpw1dSdNxLHx_8P7C2JtiVnDfFvFTZngvSigy8fpghKEhNk7DV_HosicWErWotiSWeR9RJp5GMrMBKKyjgVoDOAceAeBlJk4QDfcIGTPTr8F5NW4T7kuM5g2YI52Ep-LPYg7LVfHEaTNUbSRF8IezugXQHaIgqjgBM_doQoDgDJNbuVPsh6bDqcXij5Iy1yha2Wxn3fVeniQuexNUmU0IZ6GBd-3tKA3zCe4ot519ktW--DBPUxraAMD8ZLOhJyLZkYXSa0coehdig2NS4TAHaNSywSyS-B0xXcZMcyPio-QGX3KG7o-bQRS4lg9Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBLn0_VXl_bdyZd8TDD0zeNRI4Hejvy_rHqAOl6oNHF6ocy_unsj7zsXKTuK4Ro50MS77t57FGVb1OAGo6iZPtl98sOOaRCIXFMndploc2uos4YyxNk0b7VkbzSs_6BOfqadjGE0qbk9J21I7rKetmLn8GmiwUcIqjvOYetQxIrJARJM70hlB6G-oxJj5Q_hrk0FiDx9F9mFKk79jwEuIT0Q0g_vw1YgNXbtDM_AG1ps9PK7nST7SqvuGq9cWxt5w9TiyvT3bICF_-qDY7HlBDJ_laMwQoL4a7l47tC5Yk4c7zVTvsOeNsMTJiw1lTzuPp7PVo49fKSksUQktB3lwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDSoSXETNR4NgiQNRbyxWyymDHVDrdb-VSTEweUmae0lYFPYtJeMOYCahJapx5jG6v0UYDn7s_mFKKQhS6qLicN0AbnLZ7BKialYNkOa2Kyo-vz_54ySigO_M-pWjemNWtxCWPw3uZcwsQlRkb_9JCjeat6BsLoWp84ovpbM5MrhBP-afMkEehd052JeKAnMm3QyE6Aac_c9Edj-5zAZvC3omUz7aQiFtgbVJldkZWqOd0du7mc-vHa52hPfJQrtq0i9gIjlxUBmpdNFZS11BODhM9o8GbXqzdEFRahMXUQPsMysjEpxiCKTaPn7Yyt1hvzfKbixL9gwBjBc4EZjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sedNSVUZHoV4qv5PYNL3TbMMaOZMgeeGXcUiIJ0TdXmygqlYtD-LMsw3gRFztRDPGDK5__a_jfAsS6lqP3yDqKzHP4oW6BiBpTwo-D5S1xkQIgH1YyG3tGu6XEmA8ZsGJtmR2vfO-BiHOZNBTlZ2DNZuLXT9sZInL87aI-xX9brWeBotj4KCh1_WovjwxhkJLlMo4VOVyTtBVN46ODUOG7o8LglVHawgvWTw26zKdxm5oWc5iexlgzrYUIGIuA0pQyd2TYZ4JztV1iW3Ywy1kSbes9lNCvP6uj02K3NhsxCH82n088yKguIhbkxxRm6tYc9zsRG9wCrvFsB7g0Kkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw9SFhcJL-oBHtlTm7pioaqmoOv0bTcKMVfTE9MqWzwfzfYMe779Ob72uNwe_fiGT17-s-GNDlczLSYuAbauzfQH2vdpkM1nN53YVF7R-UXkFpXOdCPKrv-87bG9x6QvNF97knF7C2qlXxt4WqrkSialsIlZI-cReeJiw73Ki6boK8LbmwBqnGMdb--HwVmxhf6sGmEDeL86jrNM-ocfOJ9TeYOmgtIJls1ibvsyVKpgS8arUUV9P5JI_4ZtZ0OjM3wAjypRGtEg4W_2NOKW-rlcjogWrngjazrEHcWl3fcO5zq5TcsLVF7LUoCc0zsXidg4Kv1QtJSzODgxaWOHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmbZncRt5kQbDkyotAydnQIzYSxt3mHKqNuPeR0v26g85FtuhhaUl7jxGX89-hk0DqoGVifnXHlI6KI9T9Ua0YfCZDhrsRv7S7yjSQxfo1ewRj8vPB3xtqTOtGUGM5evxKr0FkLKIaxHaBnpBuPKXslQL9o0t_WUbP82T7bH0ke4W8lEpYoZIINFUK3eXNo-n8821IrTUFFd7Ggd_MbxV_QiC2pvW5CBY0qmhTGEFVkX6t5tBAkONZ8nLIVOxZiSaFv2zLca0_DRbyHOdq1k5mHfygnZZGRs-AGilmTVe9sL7wijN5IQyfgeQoEl95-jgMoElP_7XB-9bd0mvuuiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQArR5gIJLsXXdySX_sKub7WHuv7OZAjXz6LbtUpYJHQENznOkTX6CkuYQ5hDaMAs-G11uMtYtk9sJKlunmzkO_z_WuETwzP1-H95rwxdOz1PjVbXCqswEQd_TAH11J27kzUw8mnBlXPGVtIjaE9uCl6SiAuOJQ0556sJF6RfiBsbGfmtQ_-PVIBhGG5t0kQVBvO1H3lFks9xAK3ABe2Hpcz-COC8-bzbvOQANfOfvo7PbjN9Z5pwyC68OsPfYnv7F039cnDAtSEkMeFPwfGRNRGcyqOn_A7DOaYh2In1S6b4ZKGgT23sTTyqwzKnoGKdisj6OhSVkZFhNchaSU-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOJqOYv9ceGcd0Dc9F2DWGtJU1ww50s5OA7ZUe72GVRIQuIMsabEizaI7dJT_AFkWLqPx9LGeUdTti1ORyIUeMrM2mVCWR3iLX-7ShFXLjAksa-VrDzQmpb0YuEETP1oGo2t7LpxC_MrlsbsXyvTzsiKsM9X9s4WmgLZ2cyVTPjEmytVbXMx4i-tIwhwv7T2sjGSFutgSwcUeCjQp20GWq37Gcx9nFurwRF1hR8Mfc_M-0kRJzJINUKSYQJ5dsO4ONGT6VFPPzK41woqeZ-FAf6MRWMPqK0vjLl0un0tr814P9niYxxIAv0Cf4kGVw_mrPOO8yHkDNkkOHbv7Du2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL_OOYiF2cJcI9qAH4iW7DgeORU8UJZPysExuLUl3sF_0H2JkgP_ts2phE5jcFIbffblhTciTvEUEVOR7aWWrzJe8Zz60aljd2v1S1htPrXe9KAj912jXW_YC6e9eRw-nneHgM35NRiGBIfdz3YdwcAi6Wd4_AwUrRhYS0hRBL86A37LvrANbcXRmGTMOMQiup6SCtWZd9L5-2JBEC6_VpNdITEKNMQARvmvgqlg8pMczIXZ2Q22IT0_tAVeZcIst0QGv8gxhJyqa4fbEtl9eexIArMRT1HSR0cEairXrlXZi1pi0uT7t_P2suTuLuF0sN8Y0SKh6wO5HJv62_jcEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vu_mymGXnxPGdFRXEuiNeXFfFAuTY6SuEN86IvbAcO1ddFF7oZowVhCUuz3r48-HUSxIZhY7B-Bo3pUujt_scRvkZ2NMAzBRiHcdRvCf4K6dJXNXn48LTmvrC5OaVmOnwMXSFsFna-EYEMY2xMEwxp0BSEEsoeRHVPQzn9ezc3q5Ygz5KyO5dmUvjuE0gCLSyB0iTvN3rD8vSOj57DnymyXjd7sqlH8r38uH6VGohCVHJHeQBiU_pjS0_-8ozCl9JUlwdG6LzoRg11lqNC2WON2tNCpIT_H_QiVJw5wW0Ur7HB4g9hDgxT7bIplOm0EPOPBdauNMppziWJ5Q4ssVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=o_W08ZoLQjLXG_ASPzgZOUwSPybr1gCfla9m-hQ85wIzozl3Jz3VPVFnNXxa_7w06EQENWiIdtYPUkbJAVKEYI_Ml5KtO4TE8nDXzRLW6FBks1QVZwpWiMHOqpPdRWtnKHopJGB4gLXGcfsGWEe7PvUnzY8_lflWIeB8krS93ymfVtHTSMsI8BMAikElaylAfALhukyj7ht_DDyjekhHVyv1Smlsn0tuCEMgYst7nimiaAMxG1O7SboH2qkUmAD3O1c_idM5WDSfEAp_5LZ9IvV4-9UFMIUobTwF9qBlXyj5dixswOwYx4oFnMgpbzQnzcjgfv_i0uVdKSpz4Ceulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=o_W08ZoLQjLXG_ASPzgZOUwSPybr1gCfla9m-hQ85wIzozl3Jz3VPVFnNXxa_7w06EQENWiIdtYPUkbJAVKEYI_Ml5KtO4TE8nDXzRLW6FBks1QVZwpWiMHOqpPdRWtnKHopJGB4gLXGcfsGWEe7PvUnzY8_lflWIeB8krS93ymfVtHTSMsI8BMAikElaylAfALhukyj7ht_DDyjekhHVyv1Smlsn0tuCEMgYst7nimiaAMxG1O7SboH2qkUmAD3O1c_idM5WDSfEAp_5LZ9IvV4-9UFMIUobTwF9qBlXyj5dixswOwYx4oFnMgpbzQnzcjgfv_i0uVdKSpz4Ceulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=osHuuGtaUyj8qVZNcqDvm1wDfKzh2nBD5r0C10e9Sta4ABcIUEIRwuIySIEdDTzk7eSm8qj5p7kcLphuDY_PzRtP0SmjGCNDj3jMP5vssyRl-FchOoOV-C95wfAkDY0Q6y0kM4BABwfs42HHibhjJGZek5CVVjAPeV-0KfQV9h0crBTJ3bO7c-ZoxPQJ7ZVwYenAbA08a8D6cn8q0w75V8igXzTmhbIaSIR4GjLIaCCzidr3CCZIid4BAUSEKEquhMRy4TQwKa553Wqk4DkIt4GZSDZDCIJ6EGVQUe_gnsVVHU3-7xFYHNjuO4DkMD-OR1Pi9Ne7mf_rrJv7R3hnpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=osHuuGtaUyj8qVZNcqDvm1wDfKzh2nBD5r0C10e9Sta4ABcIUEIRwuIySIEdDTzk7eSm8qj5p7kcLphuDY_PzRtP0SmjGCNDj3jMP5vssyRl-FchOoOV-C95wfAkDY0Q6y0kM4BABwfs42HHibhjJGZek5CVVjAPeV-0KfQV9h0crBTJ3bO7c-ZoxPQJ7ZVwYenAbA08a8D6cn8q0w75V8igXzTmhbIaSIR4GjLIaCCzidr3CCZIid4BAUSEKEquhMRy4TQwKa553Wqk4DkIt4GZSDZDCIJ6EGVQUe_gnsVVHU3-7xFYHNjuO4DkMD-OR1Pi9Ne7mf_rrJv7R3hnpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=YlUfo2wEe8-haYJXk_ro3SH2cmr_gmJpOJVblWokw13GjuJvFyHRH7ekAUtM_BTeDRyOoInJ7h13omQ22ONZfV3rqJFdSyWafSnG51HldHoi1tqjoD8wUzHCHlZsrJWg43lqQ0BE0VSbz_RZXoyz0X-HJ4ox_hUl33LQQPftouWe5iXYmjaacW1nFoMGESpDi6Q7lcLOUa9-DV_YMOrqXwcDHGxNdCyHEcP-e3tKVShYnjLeoY3YbJYBAa6zgdlNZbAr5pcFIPlKbcYYji-dXIHDRQyZZeOha6Lkxlo4pN5RS9GKytplEVcI03qEoilOVw2VRCM494fc2GUaqlL2tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=YlUfo2wEe8-haYJXk_ro3SH2cmr_gmJpOJVblWokw13GjuJvFyHRH7ekAUtM_BTeDRyOoInJ7h13omQ22ONZfV3rqJFdSyWafSnG51HldHoi1tqjoD8wUzHCHlZsrJWg43lqQ0BE0VSbz_RZXoyz0X-HJ4ox_hUl33LQQPftouWe5iXYmjaacW1nFoMGESpDi6Q7lcLOUa9-DV_YMOrqXwcDHGxNdCyHEcP-e3tKVShYnjLeoY3YbJYBAa6zgdlNZbAr5pcFIPlKbcYYji-dXIHDRQyZZeOha6Lkxlo4pN5RS9GKytplEVcI03qEoilOVw2VRCM494fc2GUaqlL2tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7AF4VmRvmtkMqBajRc8WDg4VGlqMMSNzBsGRtGQfKATkBje_A20Yln0LVtzGF08__txZil6aUcz4cXaZiYJ2Y9-0SJJUPZQBKzD-VCFulnRVKvQOw36ZxKpFaoYip1jVnPXPuowzmXIzsbwjoZLOMg5_k1NPRg_BQhtIrEff_CpL5oVnVBjuEa8mcO3IC3YyU9PvdyA2rsC8uNicwaH8vkxvT7YzYi0gq9sBD7nPKxb8CVEI5IjcWFHfaO-nVfhEOY3fERZrXT7hdPrbjoDbxhy3Nf_LAsOE7JVcu2BnQRc0-dF8hv4OsqkAUdS14InjJ8UMP9qjtImDMwrgPf0vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNJy1lBFnLmBIkzGXD0SfzwDfuyteRqirfhbPNCySCqeMpu0uPrIPSXtMiW2qr0HHJoCG2-GAFtH47wHmML-trfP6cf0ezEzbHuf4LIUp_AmPtOurSOxWANEd6jWIKirxTHl9TRaG_QRt3_JJOm-NrcWrbbDxY6Ji3g0PlZdf8ggCFD34E9hjCvFSltHs1valS0yj4nePG-LC_5xzT9QAS1ePsM5S-X8BIb0NiSypLLb1Ve9Mxh4XP3XbQcdN7nS6dUxoSy3RsbBcMNkhUngb13jgTu737k6m4FoFHWLWy-0aP_PCtNkLQ2tR6xsRiTDbzqxjJcH8m9jIKCRcJh7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtOqQPqDW5UwRDqqORVIjqQ_ANh57oHfCYxGTONl3LpX5eG4XllvDMNb8dFDkkZVIS78tX5kUsmR41b6FRQGhERfg2_EdU3iEE9lp_LzCk8iGNq3CqNTSY2xIWTLbmmloNnBmlgRH8qYQwAwtM6qTczMnEBXdCRD30jpvxYWKO5L21xfLCm1VNY6fGS5553W7Nru4b6nK6VmWgVHfoYeMj94Vcp1lwWx3kgQLcHYbzJuAt9MZAQFEyqDEI7XG43gWThmeLnWdAIBsjfbEV8cqSJg408hds7prUp8zwVOXKrM1jCJRgMcj-gBU-M4b1fg7QW3yW5_i-ii_Uz0XICp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH9bCZVb83ytnvn1guoD1vFGKaqs27pAIAHn_X93Uvg3A-HS2yELf4AKR0z_I4s3sMUUI-l06KRaPZf2VZ42cRubrvP0dL3GUKaPFreLmh4yOCvy47ulB4cS48Y2b4oipmhQibdk_LHIXiLJNa0F30EY62mjpb035rRdajfPAJgvtes5q4YkPOWEaAtsjDKL_eA32Cj_FjLq9HTjyV_xBUVcXahbEc-DKlV9FIlg4lyoDBucdg7k6AjM8RCd_tfKdWFRU-avbD4k4wG2EEuEfBPLOAHlG5v5NW0FEVrJFGcc8PrbB9g-YrO7tA63tIWe4rJRtG40hf6Iw-Pt0lsYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD_Q0n4bz9mh3ApEj7xo_WxPfFU65tarIpML7GiKxbIEnhONchgciYgJ18kYjpvHgEk3KYv6nYxUbsVGJo6FjsN09s5bqpPcLnddvinuLXuJj8uriqckRsKpvjF3FyMKQ_T_0njxbngmfNp06Fem5falnLzNR8mRa4gwPyXm2RKEMsg83dnm4YEfVih8EQfeOwzMit2h2p0Uxvj76l4AuMPj4GFwF7BTnPgpd85UncH3vrQLVV1tBTe_Dw7kq6roe80YWZ2S9dRC1JIm5temJhdSvDbmmbv6Yjk4lcsLt00ce5EKKFd24pOVL4HtI3TjWMu9dM2UflYGmPi6FYEYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIzEGx39tqdVjeWnRd2sJRO7VYsgy79ngZKEGSnpbTVsjeP4KQxPzszSe6B-lr_hmFy0youmOUYZfOP29UTb8w3bD7Hi5KIcXG-T4j6VKTeC8fZmL7yZJBdkJ3ks0Eos5PletRkafFGWHQH_2r6yenCo6NdLAEs9HQuGKz86vUOAmPYlZu7V1OoGu59KVOwumHYZlvL6XXO3hxNHHi7IYDR2XglSffcZvJG4m-Jq3AFFEPe_7hzCP3bMux-VKIxLyDg6Ef9BQpajPXsAgw7em1IyzZ_IgE-EjEmDjyt8MTjuBYmEfkdAUaMUkNy339N7nsDSIzN7ai6z21O8KozYLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ5L5lkhrYQ4GgFLbRM9H8240SX5xyzSTQcu1dpUJAGh8DrB1rygioc6CBJ1F8aW4J7HutX_zeOOzmeajlSAqswCPY_yUmimAtlECupjl0uM3MVUlawDnPcg8YGFLKdU4ruqiOCOcz_TlG9gbYjBFQBFt9yUc4RpTIKjPpbXgMi39mWSbr-iAvPpB7rCPTPnzdanh2Ud2rPFIGeB4CkXJABAhGnQ-9UxuJMGyMNHTjO_zG2e4gbEft7xkYL9vxyFhNB2JHsV3m2hBojFAmTmMaHHwy1bMAPSjKCLHSn4W5LeO7wBL6BL1stjbWQvaQfgDIZZNx58YZHcvQAiV7F0Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GH_o3v6b6g3rbBnH-k5Ccn3nqqRmTL7e_wL9WYWTQfeBZva6oCjVOkRlhQMo6Ncql3R_KSxMCkqSckHHUU2B0bqfPdfM-2oJ1r93iMoPNPHksGZsTprMHvQrSlAkUkR7GeTA3r_2zFbI8ZDfodWF0wdFHxMh42GuvjaqPIUxIAnqNVJr6xxNzLx1SHcFjzgW72C3h_l5ToEzGixIQzoKFGhuBjrKOxSMJKwgTr08dGJoEA1BSs3-S0yMNy7uIZybNs_2mGIMORj4B-ZhyQ_qY7M4zYRCFPDh9GgC4-QBnAjHvSgoRbQYcx_wHcDL6BaA22iNSgekaflXiwyIRauNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxNiWVwdEt0YeeHsEp4OAF_dWSVeWWl45A8QOhxLTkMcc3HGJZZKeMstTvNILfHtnGJgzmVegNNvwJSnkPinDLnm9RnOsPCf4BctEo_N5E_IKMXSGcSOx8h7yfaexjX44P9JXwknpN5wJTSSWbNI4QGqWg5Dj-mTV-bIkEd0Fzcy7LjvAGiiN2yQf4-jo02n6aP6T-BTh_9TaRQQ0bsVIkfgp6qPuIF9tsWfDoHlphxNwkkqRzTiNJtQbuC3QpTDlevA1q2pOf_wt8tKJ0Bv4_9LSpIKk-gikd4CEIvHPvGr9tHBhHSIJGeq5N6XWzA6uBXHO2TEhrXF-SeweyZ0Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=vm7JNJTfnYPgL3J3cLm9SLYcXHSpzE8ph1d4YZ9pf_nS1aEJq-jGZwfahJJ7BzvQn2K_jxQtTxci1ben4S7AYKWSe0qHyxhHyagx1FeY5u3gunZFRUDazntZYNIHKykA858sFSjo5b2KHs5GLM9LnBprE72n0wh6WHa_-oIJJ0NYmuApfLxyD0DDDKPIKeme6EyPi-a0k8BITQhWX54tNwg9f6GkI90wu42P1ztLSZpXw0F3bcUkyiGKD2dI5_dMEebfwD0Y-OYvFaoofQz5XarF4OFA4zE1enjR7akUiplpofBP2EkMX7wqFc2aT0uPdShVPpAzKDaveGlVtnzNoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=vm7JNJTfnYPgL3J3cLm9SLYcXHSpzE8ph1d4YZ9pf_nS1aEJq-jGZwfahJJ7BzvQn2K_jxQtTxci1ben4S7AYKWSe0qHyxhHyagx1FeY5u3gunZFRUDazntZYNIHKykA858sFSjo5b2KHs5GLM9LnBprE72n0wh6WHa_-oIJJ0NYmuApfLxyD0DDDKPIKeme6EyPi-a0k8BITQhWX54tNwg9f6GkI90wu42P1ztLSZpXw0F3bcUkyiGKD2dI5_dMEebfwD0Y-OYvFaoofQz5XarF4OFA4zE1enjR7akUiplpofBP2EkMX7wqFc2aT0uPdShVPpAzKDaveGlVtnzNoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/coyNhvVCwK-kV7JIkoZpObpnxBWtUhbs9TMyW9AElbr3qO81QBs60OTxmJASfbODc2bAMogcoFvFVao31IZJ2HTJkszdoaSrO8bJBStPo_6mEbPw7Eh7J5DEVfT-Kqbx77VSf7qBSl7rTDMqProQtrKbCyrxR_Y3i6BzwYXVFTo7WYKV43EWXHKuVKaPqBT-mHCfQaXspsYcx43zRDVsj_M06ldBtSsjHuxgN7cJyRWmbhYXWSoTU3h3lwq8biHdUgm6mP4cCkac7ZvOwGOcCWTbPXuUo58DpKR5QW8jovST7lnXzeW04HQib0FQadIKIOthyd0pn9RTnFQ6vv7MKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5eOyfxSLojy-DXE5YsIE5hm8lCwCpmPEO5FKtZGdUagHmwyjwm4HU1ItTjqRKbStmn6g0Nbvicij3PJvtb39pHZHAUgVnGO_vB3Pq2P-NAc7hiNu6H1G-5qQ8eyHRc7P_7dFyzykTDcaQRJf6NW79PTZukGiTVFKoLKS5J5JJNwa7U7IE14h37xsHXs2fmE1bas3ZiDLbSUelGVYvuNKSZw7fn6EjMss3gd1QX8ONWZLgIIZb-tqBPg1qIvIKv6vlLH0DMd_71HhC1zKaCK7oZC9n3RFb2GIx0rgUjIQfABwkdvJO5Oajbcp3PKWdWV7Nm3FnZp059-v2Ody8vpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Go01oe137t9IcPZnC0ovOq6kzgKtPfH4KTrSTsc1M-fEu_xSLOaysipJ3p3Squvn13JWobmZSWl2-EKAdQVNJwqTeNFYEd5FQHpyOCrjW-EKY2uU9V7km0UqFSujm8APGLVbPDdK27XQgdooDo9zp4sg9ROsVxO58DiHtzu822ln4Th5NTAbPfA_iJa8L6gMkKCuDLxLAposhCpsErDZxfJD4EzxDLl4SVhzz8Ft8GI41Siy07p_UHW9KUbRCn6wmRq8zz4TWt1Mu8P_w3IWteQBtPhdi8ISrE2hUoucRFueyKR625Y-Xtf_v1r1ydyE77Gkwq66B3RTzbSSxfSnsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkzSuQ287hvpkl4hYbM_-ZsKZZHpZi1T5OKXqiUYeO-HtjQZIaPiSyXqgc0LvNbrNpn_Qps2Ua11khH1pyM_zHlDgJHRXB8HmEJy8VE_JyI6nGhS0LsqvgF0NYwO5geiiq9rD0yJNPR0lvunCHlzME0gq97owHUnUW33VAnjhkVQGB0vZkzZDfPRDYj7yd3aIAkQ6LNe54JPiTxs5bFgmt3-czLJwhkAxapZBEdZQDRllVS4YZ0enVXSSzt-xQPCnZ216WA2NfjefRzXLD5wwC3PIn6vnyKduJKkrZDOvvFKOt5b_WYSCAh2-uBc7PsX6KI228Zf2v0-V4xE3zQcQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=f5MC152PakN10vceRFG0bNsVPwIAgfUPE_2b7mSXAWgcphOnWhIXusLV_YHlpf_XZdqRS91W8zGXstzTH-NE6cUbDFGc-ov4lOb58tHWvi1ACl9reSAqLtMwmZt3otBpTNxOF_DayqsuDOAFyL2KPshS-479ymJ5wi8KNhEWF3HpQSKfKbK4Jpoww-mt8dczSbCL4OH_qRHzWbQ4tWhqkgGAAVmnjUsnrxqLimOjwfR2xL0njuKeQgkGJGjLdrOM5Lr39SQ5Sfi3rH-DCQfXVZmpfSCuSvUMpOq_Sb0YWVLT6lyVe0-vnpj5bLYr2alhcPdCpngdmkv1IQ1Q1bLbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=f5MC152PakN10vceRFG0bNsVPwIAgfUPE_2b7mSXAWgcphOnWhIXusLV_YHlpf_XZdqRS91W8zGXstzTH-NE6cUbDFGc-ov4lOb58tHWvi1ACl9reSAqLtMwmZt3otBpTNxOF_DayqsuDOAFyL2KPshS-479ymJ5wi8KNhEWF3HpQSKfKbK4Jpoww-mt8dczSbCL4OH_qRHzWbQ4tWhqkgGAAVmnjUsnrxqLimOjwfR2xL0njuKeQgkGJGjLdrOM5Lr39SQ5Sfi3rH-DCQfXVZmpfSCuSvUMpOq_Sb0YWVLT6lyVe0-vnpj5bLYr2alhcPdCpngdmkv1IQ1Q1bLbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJKeS4T72d8w7I2SlubTT8lB98fqNByE2oNVijLBLwRELx5vZ76tvMgbUr8sw9yiS-XmYX0UG890AK_mxYoRexGT8iquQ6EXXjo3fropFOJUCUdUEHs4KHe84DZfuJh7zr9vVT2SyWR64cl8B_JpOmRagS6zhgqrqJPcI_THxsMfozs6jhpMSSLpDaHaEk-e3IDvVhef0jaHXatt0MZab_Ga4gsUVllMn_JxLvlfqtTgrulQoTfol9nX72ghHm6XKxiBqxuReEBe4no28FdmaLMBibbrXM-IX3240Xxjed73F7-PmR4IpLz7urtsZhCgVkfrA8Dnem4sZoHYm6aIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=qcWtPHoXS-a9d55qy-TMmKBWhb2LhzXoeb594GbnBqocEQNsz_WLihNt2LWDEqnJy8JJTcFkAOYpkcqmTPA6lne5wWBF6pIGGIMe5phO0ZcAozq6Zv09F0d5duU-qLU3j9OYUO4CAHhtvgjPe30mSuLWMRAatGcHM5W-SC1MixhDq0CMR7FeghjtiSfKFqpWI6Lj3RMDoAvNCvwiaHKoqu5tACJ_Fyw62tIs1iQ8pFPBuZVUjGzH3P-R_g1vKPkGHQ9l7MWcZmLs5qYagbSrrW_EB8jdljkEc7vNgJxG_cDOqPlmK7DWJA6eY9sKUp83VE1G91G-0eBNJ4qXmAEl4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=qcWtPHoXS-a9d55qy-TMmKBWhb2LhzXoeb594GbnBqocEQNsz_WLihNt2LWDEqnJy8JJTcFkAOYpkcqmTPA6lne5wWBF6pIGGIMe5phO0ZcAozq6Zv09F0d5duU-qLU3j9OYUO4CAHhtvgjPe30mSuLWMRAatGcHM5W-SC1MixhDq0CMR7FeghjtiSfKFqpWI6Lj3RMDoAvNCvwiaHKoqu5tACJ_Fyw62tIs1iQ8pFPBuZVUjGzH3P-R_g1vKPkGHQ9l7MWcZmLs5qYagbSrrW_EB8jdljkEc7vNgJxG_cDOqPlmK7DWJA6eY9sKUp83VE1G91G-0eBNJ4qXmAEl4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra3J7ukQHR81Xwsjq0DtG2QknpiKH01dQnH07uQSTPA6BvYEaQ3TJVBsEk1J9_m7TMVTfWjIILdY3tVUMMmDpSL506K4cATC1xh6Yi_L27kqLF-3gSCMeHEeuwqbIhXg5glVgmtAwdX-ee5knsUrGe3cJORc0-BjveOFF8Hc8V51XhiREvTOQWx_QEnN_W-dS5grFxZiIgnz0EMhkiC3WcEX7r8oUOpA5bH1abmKtYB3QjEYljF5stRkfA234oDWfo79edSB7l4D4zvU2eKabiYd-NGY-UpHWZe4IgOgHjO-SFO8hyNwmMm9yHjOySBPFm0yUJzIRNm0EL4gg44YKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm1Yx-oKqB2T9Q9l-PrvY6D3TUz2155Iz558hxqEHJ5vzAiWaisTLiWmiWiARDS0HfxNizGzs9Oq1uyI_3zovtZkXT-nU03i2bXKEaQP_hO4ObgKCC-lDtfQNd6gGAuO57VuBSQctat-eN7V7LFuBwtyFdyIEoPEA3784nhf0mR-kZi3wqigXaIE7ggxOLUFSVWaKfC8eXYDW2toGNFMouwjXXRmIVONV8JtAujTEjX373P8fwHeRPfUiBGPZFv-njYqEiS3fRV9ZPozGNZ-x8MisbM7D70IiQwlgobD3jkvaRZd1AvOD-P_KBOk8cle-SIxc34lWJFD5WsC4R8CJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=BzlOiyIS9-K1rh0kjHd1aIQN3IOUUCxskICwfmHyyyKIxwCW79VvVLdt95JtqwzCinkybtxCsPtcqXuaz_3zziiwD1tPvCFZKFdKcwbNlkc2z_phQlXfJszXcwfBsNpRZkuKKTBLtXcgRLnxhhIRweoX1e60nKBziaWwfyasH-PyxxwHQB4Rmqi8GTPhzoWWgXPyaVCiAVBKbIauQL8znF5LyKLNXO2pvN4OCI4fnS69PcwygO6E21xE6StxXFbWgDqVoXGsXx0dS-exQhrU0yOxfF7-h5Dfcxb-xNZyTJzli8E1etrnnUtfu45prQiG_M2fo-ze-AJerR66IotXAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=BzlOiyIS9-K1rh0kjHd1aIQN3IOUUCxskICwfmHyyyKIxwCW79VvVLdt95JtqwzCinkybtxCsPtcqXuaz_3zziiwD1tPvCFZKFdKcwbNlkc2z_phQlXfJszXcwfBsNpRZkuKKTBLtXcgRLnxhhIRweoX1e60nKBziaWwfyasH-PyxxwHQB4Rmqi8GTPhzoWWgXPyaVCiAVBKbIauQL8znF5LyKLNXO2pvN4OCI4fnS69PcwygO6E21xE6StxXFbWgDqVoXGsXx0dS-exQhrU0yOxfF7-h5Dfcxb-xNZyTJzli8E1etrnnUtfu45prQiG_M2fo-ze-AJerR66IotXAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ1n9LIFRfVNHd1nYACVXBUxwZClrDz_-RjDB_fRKI_XlA1VKyGybUiRTuE76gkIFn9w7Pg8dOEB0THBtaMfog9-oR7hCryJlWblTFf23JofqpGsIUDOmya897wkGQ6hyo1OimLjcdqjKiDX-u8UXFbgOBbt7Vba8TI3Kpk0mROciHgQolX0irLKRjJBUYGSkmPnub5w8fKxQoilhUaUUUOoZomjmqZa00qj5zux0hc2HqtfrIZNA9htntUFte6GmTax1taKhQDUviXMNE0lASykrADxTsNH9fGif0tZFXEzF9CNZU863uiK_pILlGsQBvsI3VnE2WK6JYgieDQUlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=DmZGu1C4ZKkYYRyKlawL7X4ZhkRnHO62ocg3cFrx_gpCRcCeHYkQOE0ktXT8ozfDRoeREZApKTli2SCyLGrqjy-os4F0ryr8eUiJ6Su0RQV2xV3atjNHG3GYzCVK7hZ7xURtaCsyREMTy30pUxiPHoh_zpBRH9K9bvxJKcZdKgP0y0fVVcUQyslRAlhj7OH7C2d_R_tvdCvmvghRGakvDqcI_8jTX248z3U0pMy4DhhZLwaL77pFsMkhwaFHjqGBjD51EOzbwRkiNmtEixOs90zMimQ8l2n6IqyNQTfLn2VKUCaR7DUDG8PbfXhrbjU6AU7VLQI9bYt_T9n_5ddbLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=DmZGu1C4ZKkYYRyKlawL7X4ZhkRnHO62ocg3cFrx_gpCRcCeHYkQOE0ktXT8ozfDRoeREZApKTli2SCyLGrqjy-os4F0ryr8eUiJ6Su0RQV2xV3atjNHG3GYzCVK7hZ7xURtaCsyREMTy30pUxiPHoh_zpBRH9K9bvxJKcZdKgP0y0fVVcUQyslRAlhj7OH7C2d_R_tvdCvmvghRGakvDqcI_8jTX248z3U0pMy4DhhZLwaL77pFsMkhwaFHjqGBjD51EOzbwRkiNmtEixOs90zMimQ8l2n6IqyNQTfLn2VKUCaR7DUDG8PbfXhrbjU6AU7VLQI9bYt_T9n_5ddbLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
