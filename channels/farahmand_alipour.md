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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.</div>
<div class="tg-footer">👁️ 195 · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKLcjLtymkdAPjcMUa41LF_UH1rSbwYCEJAtHXbJuBEVZ7iioIqic9oa516HOBFJHgQBopzOEx8qqfuIN71VeCB_Y4ixJl1FZ8uSCa8epcFyK77ZPxppk9tTYGq6TZX76sHUqU_P80ezjeEZUtWfSGhrQvkcQJJbrMKpEOAi00p-Gt_tK51Ra7Yfap7vXkmdV2R9cSwNWpZwfK0itbFdjIi42Qu2gRU1kIwDyr3CirkcyJEeDHgB39A2-9WPQowhXSLtT3K0QWg8xOkjaEEPzHtgPbJkLrR05kImstWsQ-HZPNWRpEiIujVGw3out5F5jG0Iw3qF--Z2ImNgJNEPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSI6XhpcKhhyX-p4jUn3coWb6WKpydoMhMi7mOO16YKillKOdrHM-6XRWYluAVn4hMh5CRSV49uugBKzhEm9A8pAONk2iHxv8bGf0_W44BB6C7tTDjg5wQqUj1FoKJOor7iqXGIgXyV4gCd0v1KmTdTI29zhB_5QDooB_eCELZgD6YCE7ubjiKnefDgHTlDeeoLlYkFKvKDWRxkxcmgyyG_l-aJ9sQp-YTVtaAY2zJ2f8z_aN9kR6pTc3Qu0Y7K5I-FmthVkrF8p7qKAb_pj-ROWk00UAQsSCaiiXBFT2IE-kAk0WoWO1K1n66X1AyO9lf6xs5ZX7a2K7l3iM0r5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cf3PHh3LtMSh_zqSPUpUCbFpArE58y2EZBDd3XBrKfGl7acfotyUSb9BJIkQ7Xz8SZ-nHyWzRRDsP48UkH4KYpcgokq73jrbnJnuN-sHC-hADvwAOEZxPUNR1CAqeVvc0bzgL0JYyybxeFCQAk0wvOvNumPJhttHPbgQ9Kgh539E7MZW1B1yaRmJzZyAhEpXInQM2n3z2slnuB1tb-ETkY0AePZv18xGW70nWcSt32BPIVtgndQjaSJG5LSrS_gQPs_ZUbT-sHZxuyv-kNegwEs7yh_7kmKf-7m50pBK8vhki0dcem-QpIvUDtXoj6Z1NNRHNENnK208F8Bf9aGATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-IdRHS2E1ilfJj-RAzHx3GTRIoC7AmweePIbohu2q-lhiuHCo0TPEjmomAv7rSvf7xP5U2ZP2SSdHGZxZfw_s_MP6NOvNQ0oJBLlhqMFHvflqZlensXogQPNJGD0VY-ax07bYrxUDGpvM5u0TZJrqTQXuPKj3aPC0KybNxIjWVfmVulZHuWZokT8fnnVsPfwHpE2HW8uYQhLFNzXgCqEyiRixp6oSuFM8zYwLgcZ394fxpKundMxunN8zzTyLDjuy8nACOjIWLX99idLCsbhA6YNGws7fUIa-2Rm_Xuy2oj24c5P6HoR6Ku6CJL7ULRuvf5OXgwL4ETUywZDXjPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_-ck1ufxBY7ZlsBptoEAQUX49M66JszI8t3DtT1bzIEVbwRQ5Ql76ij2tF8Dn09EhtT5s3N6jBEKT-NBzQvAwp8vfbb_o6Z4cSG40EuEZRQuOPItAV2YCx3r3bEYaVQLiNPPJBotwrHZel5t7-G9KeNgYe3LHym4xRfxnwmitdcix3fqoaTHY7eoJNu4E-JGQn6s4OUhx175H9vayJuhPde-cm-pHBw6--jqjGJqu3Vb3nV6sD6_-oFiLSHgC9DLBxE7Zxk5AYDoiB8XVWiFwcguenxEUdeN-_xtKebZNQc2C_HmBzO1tx58_Tr00Bu4evoQEd7qheHWxrqaovEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aClTm4qfiUfdz8oh6HdUlAPdggj7VQqZbahR2AYUzf8-JfLcy9zXqhQFIRrGkiNjMPK9Kppw0dplx7K1c_h69ydz9X8Zw6yhL4znt8lzTxNUlX4hgWs_D8gCCgWGW-V8jg5faGZvfh4CaXZD4vnxNc3FnZuCwtoIUQ_1ihg42W57Rj722hZj80iHOTGVfqSJt-PJgguWXqWAFL_Fcy8QLDz5Lc5YAFopH0DsCdcv2DIGRli8HpgU_uTBDMIv8BXZnWOH-3I7jIHXSjorF_d34z5WE45SLe1bykavhmi5MjhjnXWKqnnHAp2B9s6Fmm4zH8w2xhxEKbrbO9sWdiDbtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heePX2bwR0h_r8zrwE6nulmAnmsGGXfh3MZ4KaA9wkGRHdK60wfrXdkjnIGIvEuCnURIbSNj-9CFAnzLkyZ7hu7lXi6qkMtZAvkHnXuWZGcYDS6vTEQhzzPFX7p799Rnl36a7xiaj5n7RgxAz-PGPNOhzXjkmTUzF2d88zLzknhZOQTT34zwcvO8Rh1D5vKxi1fzsrwz_hXPFpiNVyQb3Q6uWm5Cc9eq_rRe9B7PLy83C9sCNMkzYs_2k3D59j3VhJQPNWwqbjKqWa8YkPov7eTHQurTVBaD_gBN_11Z9D-OrPKvmkRQP3-i95lOBZfq7c4GQCoAu_D9vYEviMj-8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePmOqx-rDrmMOH-4avLm2n1e_kQcgi103vUW-nCZ8-HJ5jHur9pXpuunKNSELw3_s-KosfRGaHMYn-1fnht5XINUSd7J70q59JWHXLBjNfj82AQUuCeDRoYWN1tfGgSboWsyCXXgWj4zJGNfdSwGfOjPpM0t0v_qF2u8mR_SsYFvs2uQ-rpHPtJ5bKFo0UVqd6a95ZgunomCo4j-v_l_mbaiDu3-3G577c3XIpwh9PP_sVRg1_bRBtfNMLSKrQwI1sI0T9fsxrAGGwbDZvD1TnZUG0-rjHq_D7xctVoXdLo5EbxdzkfLixwFV3x9Fk6191udw8W2joM4CyJjCVIFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDsuC4nXRyynjJ6bruPfkk6zIiZTMd1w1q7u4lgC5uh6QVj2P_rRiGoIUo5yrTvEIb1piJbUEO4SOqf1aYdLP8s8gPHIAdxnurS5ftBqu9-RVZbCpoPk2eqbNON3hx2p1-eECBi-9YuUa5nis-EVD4n4s3obu2_z0bguW5YPPcijB--MXc2kehYs17fajspLbyWyzvZacIPYCGo4szKl1-HZ1rgjuT_KstK-wmXwaINZuABfxTaN_xkB4U3bASs9DyFoDARXbWuIZcwW7DgJohUeyW2IRiI0A7TjH9hre-zLxIk_xGobQTFVMo3chc8oXoP5txM7kVr4hQveN5QNDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=TY4zC-UqqtYAJ3Qx1ddBw3CCLiux1NsR1VOWRx0IOzDzDRAghhp4QbmR5weXuhXGNqUn_mNi7mQPdOXyf0NA1fh4opKLj-dPwqJ_cYuSJbaHJIYk1HB8V5fGeGfHGnq6rRACQ2pw6ZTsF57A50nZdbkybXh5ufTyG21_apL0ePq6rgSK8YTyEU-T7ssFHeeFDc7Nnlb_MYhv_mM973ya9DJjejQT-E1Kqkb338VFwTnvPvcEFFBNn6psoe3gS90rIBu5PVRLu8SyGRwg8XZErrakcjYhtdDCGxron0uMe7Hn41c2Z8paw-ZNnzx4wj4FMhO2SaecW0g9bLK4aggrXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=TY4zC-UqqtYAJ3Qx1ddBw3CCLiux1NsR1VOWRx0IOzDzDRAghhp4QbmR5weXuhXGNqUn_mNi7mQPdOXyf0NA1fh4opKLj-dPwqJ_cYuSJbaHJIYk1HB8V5fGeGfHGnq6rRACQ2pw6ZTsF57A50nZdbkybXh5ufTyG21_apL0ePq6rgSK8YTyEU-T7ssFHeeFDc7Nnlb_MYhv_mM973ya9DJjejQT-E1Kqkb338VFwTnvPvcEFFBNn6psoe3gS90rIBu5PVRLu8SyGRwg8XZErrakcjYhtdDCGxron0uMe7Hn41c2Z8paw-ZNnzx4wj4FMhO2SaecW0g9bLK4aggrXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=A1DHJ9j1n5VUetRSvtIowbME2BHtblnkGyZSUdEh5w7aVdtvr8BG1L7q4c5ARg1bucAl5UnVUdEvOr-9HCIT1v4yw-luS-1KRbEFWfkfZwVr4BTRYXilEZgTHIMH6WB4Ux0YaZR465sOTTPYkrogNHw21OQXgPh-bdmUYCm7qFUBSGm_FoyybClt6VCYhWrxNIgVh8Mqwb-jbImaGw0Ql5tj64lrCQGobxBw5HiRz8Q3ke89s70fCQpz6u39Nxn9M_tW2sORSsX-huQsA_tmXUPJzTE9HaWru7p8goGT0rOgT2vE2_Ow4u_Uvrrt9c53bJ1nPCOz8Qa7WLeQK_Fiyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=A1DHJ9j1n5VUetRSvtIowbME2BHtblnkGyZSUdEh5w7aVdtvr8BG1L7q4c5ARg1bucAl5UnVUdEvOr-9HCIT1v4yw-luS-1KRbEFWfkfZwVr4BTRYXilEZgTHIMH6WB4Ux0YaZR465sOTTPYkrogNHw21OQXgPh-bdmUYCm7qFUBSGm_FoyybClt6VCYhWrxNIgVh8Mqwb-jbImaGw0Ql5tj64lrCQGobxBw5HiRz8Q3ke89s70fCQpz6u39Nxn9M_tW2sORSsX-huQsA_tmXUPJzTE9HaWru7p8goGT0rOgT2vE2_Ow4u_Uvrrt9c53bJ1nPCOz8Qa7WLeQK_Fiyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7win5Ty_5mvnzVkEY3K9xq7ZiFS7zbmw9Zbjtqal-NAYT_yY0zMiTVuVRjDh0OiL9f0cSrF0xb_MGnrddUIyY-Mi5UJRtKOVvfMF8iJMKXx3WpTnchOz75Z0YkMpzca00BjL015FOY4Ih98h6AxbwV3Jfc4o3uLyyWS_Xza4m7S4vvIje5lVvaK4-80cHVnUCQZ96X8cvlSrKTy1DkITE8djYVW4qSuITYfvdrqMdXzYVzJJejazRgzipxuBiG2GHRC_KrkE8sdRM7PnrsWPH8oenP0lOpCmTWfgXNSJxIFsPAzI3Q7WREc9R7Lr79CsPhLerSmk-fegzuEjVfNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTmUC67IrokGXG0Dtcwz6rGCo2Yg_e4uTGUTA8qT-zT7DexUJMEyp54t8N-1cK0WzoUnlgDgPvtKSqKKQHeJugBF1vIZnrbvW7TCiDaXK1ox711inAdkGrKJ92Psb0A9rsCork3zVyb4JYBVLBPb2_UQ86AquyGsnNocHQa53EcjcztTT7r12O8ef1IdQOOF5BqrJWk9aa-eCQZXToLVeO2NZ7Y578SMfDs_zThRIrAZqjU5_1wnSqajjaEbo-PNZ2Err0ZGjjsCxvV4cdt_sxbwmDQoQwBBa70VCWIFTpXJkycG5aRKMjttFuqopvy3lKZD9hHzNYN-PlWL3p8FUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwcXOYrytgvARbdlIk1JPlJP2pDEMik70Cg7DaeHMgymLojyyT9BuPeZ84dhnCIBtcPyEZ1J9Jss8dESCpzzX4As53wGY4FZrFY5GduBZYrPBEIgK57rL5q44ZIJECQCCl0gA8R32QUWhbBL6MAUoZLhgJ_HOrK4aVV5AAeO67OfDz5q7h2bpxnIc9euagZSNnBirUi9GYTq83QBYvmkU8B_kBvSGNjebJ1tYVMPu7YvnMEr0Vwd8mYafTm8wXH_GiYexBgV8PHX8NEt-VgntVprG6imsHOTjrBHP4ml39iDEiAQGsIwh1DeUTD7RT2wi6_nZq20abdyNUgxQK8Whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrwFqlLf_75iB4ouDztm9OAA0tnsmhZ67ug9xHobKLLB1-TbSNP5XrbZsIjQOCGoN6fxpXgVUyBDr3iHxH3Ew5S_aemvswDC3bFYiYF6-qM75d55nIG6yszhdntHARdXWTMGBdDx2BSjfdrw0WJfcPv4JyWrQ4UqLfm1eEmVo1Uk6N3ryQFFo7gUcenzVxJHK5lfPjVhFo-rsah4kSWjQVFcWSZvES9E6RCbvTL6Wf0rFv1DRGkJKksTJXvSyW8-PTMxxd9IF9lhorsucyucaXQ58uV3o12Pt7SDIcQaITbnCHDbgJi3E3oqnLLYfBCCSOStVEm8LemvQ7hxbDWSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdeDZfLYGmeU8qOYAgsavY4MABxGWHocHXSUkmS9LdqJAfu3wGv-ImNMzAnza0ZqjA_FveQoU_o3B6Kzl9ypPFDsMCPHxxPFNjX-J_K8CCNQl8iDRnjsBdAZ-6a5zCioyP8ZmXUUCobfjDejgJXMBxh-1MVXGsBu1X302qSna27LAUi4fgVGRhGqHaq4PuP0_u0ngYhRIRO6syZ_RH5niDKw0dbyRnWyfosKDkWseo1Eg2PzACrS9x0Ul6b9oXzDpcCr32DMQlCYYZ4tnZoHmAu1BMERKmTLa0SmUmatXPqWJcg9dfSXmsiR4kVquk5fe495C0giX4L4T6W-blKlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH1CrZkb7NwZxx_by47n6C_vPN5H673Z2hrxB2p-Mi6RVF9VIRh4KxI6U9U3iLGv3kiWaV3xNrPvwYtUEuxQ42rTlhatCbklz5BqupCfHUY1hq3uvCVdb5RcU73G9jp-fFRjcvxeGgf77v21EsAmPKVa6oDh3E5BL0k02mUFeP4ByUS5qOTC0TcyRjeDNcQQ5eXMoWZTOTzBB8czHJGZ52p3zb-e8ftSrW5ZmLOuP5SAinH1BTub3xaGq4AbUtIgdVPf1K7QMCofOy3Ojq3kZXoifyqEtFv-755T1HVDVWpq11Kei5EvukXSAFlv58xadBs5NkRNVdHY3MxK8c0M_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmFkwHgUH6UmRNgRt3_XUK0Cpc_Glp1sYd0-MOMFwJS31FSP-EKtnh56_-gFB4BDY8V8OTXCC_pPbHSfr6aCwsGqsCm6q7RmFGG_wr59NxnaKY5fidcNiKed7l1bTXJ41Jwdq1u_VMw5i3l6bw2YIRdDsKZtG9tnj-PkyKsk1POsOlqqKM_0YryQeuIMKCyEKHsrulEchnfKt9omGHPhTrX2wu7vAf8kH_NsR2zLfpBscPrfLml65ybinyTaOtvXKFjOkAHRqaHECy20EjByMUzxeIp6zycvx2lxpp9PpBld2x9I5Czzj98dt1c85UlZuzVhaJZOZ_f0HUrJNubz2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IknhXhwEJgudo6Vqo3vD33KNEe3AQz9whuuTq3iQXXQXkkwztkUNRH1RG3qqFCNkBp25oIHm_XkW0cnoK0YJwBMXgKq6sD08EhPxRq4fU0Pul0YXafLE05hQlqKFnvUIPaFfb2J3ufTbTyJvdo6sSDz1zTz4tD2083sR40NipJde-e57s3Y16zv1rfbnD54408g0eha1EKuKRPOtLh0UPcuglOy56y0l3JQQ-yPWvTyDXW3oFcvvjzCYaE0ZmLflX7DC-O01z90_2sUCgxBI17tfym-n3e6YEBSB55bVu5wydeQngNu6c8Y_pF1nIalAoUO-7v513UDsU58hUk8Y2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUEUDYAPWuoOaebQPLUf-rT88sI3LMfhYBYblwPvuSjwymK9KYn5vZFDw0wxJEQSphHbq_mPhoSSzSmdLjI9IzG3H8r00y7v_XjUkP3OFZBcd3qkiGBCX0PJde-byqNruoIHBp96KBzBEP0C6SG3xg_2M3PMULuD-dZ0WZLm8ND5D-_JIaAJl01PgInGTZerMBpuRmhOuKoNHei-rPxU7-GXlnU3GqaHwXi6u3xClgQquNzks0-waJJzmhX-4LLPnrKN8PmCQKffHHGISNb8Zpotbh78dI5Rew4KV4fyL8L98HZoyuRKvpfVSoEDwLLFyn06mY7YEmNTF00ky-knEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=YYD7hGqc3ybukLstaf6er22YGp9OCw4ElH41bXvzA3FNZssJelFs9Q3hTi3uA3-6bly_qGh9kc87ISY7dEhi81z0Fcfq7yCvFv4Q_rFTayT053wg38-YrKaqN67Re8mzZNZgdHLrv0eV6aIsPNYN8bRofPm6PWG8mY2QmGjQINyx_gdn0rxK3tQivdC446oHwJRCzMFHyhs04ADe6GceiDENyHgbE29WswXLYl6WCK2vPR0rSObM54KfsvFnRiC0KIP01gb3jnt8Pb6gupsURPBvEb9Wo217qB_l6mczbAG0vjvqKgmM69xbzNpGV28BW4LfW9aYML8IsuibQcceAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=YYD7hGqc3ybukLstaf6er22YGp9OCw4ElH41bXvzA3FNZssJelFs9Q3hTi3uA3-6bly_qGh9kc87ISY7dEhi81z0Fcfq7yCvFv4Q_rFTayT053wg38-YrKaqN67Re8mzZNZgdHLrv0eV6aIsPNYN8bRofPm6PWG8mY2QmGjQINyx_gdn0rxK3tQivdC446oHwJRCzMFHyhs04ADe6GceiDENyHgbE29WswXLYl6WCK2vPR0rSObM54KfsvFnRiC0KIP01gb3jnt8Pb6gupsURPBvEb9Wo217qB_l6mczbAG0vjvqKgmM69xbzNpGV28BW4LfW9aYML8IsuibQcceAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=Hd-7i_oE-cVWNqbRfdqpzxQFt-HHAdSFgAetO47hfR5de8NIi4DrXpTskw3OGVXGHhaMm_MGN9PwIOng-WnUsKpTimnX1YZF6ddB4gMsTpeOKb0Sv9ybML5hcdCd3zLZV_35NSdJxCmfWHOJkUg9M_3fYNzEt5QdASq0TQ6ItOM8FP6WaOX3UUgUsgTT3j0FvUG9NjzLWjf_qoOkvIQaAJ7GN_AhgbE8HxVpGk9TUcC2JNjZVcKl1uc5bt0EqZ19QYOO41GE-mAY0yYX8eMt_VX35zvKGtbu2yhRZgyJlk-7X87g6Ei1ig9XMRs281Jm5gcYxUv9XO5M2Uai91S4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=Hd-7i_oE-cVWNqbRfdqpzxQFt-HHAdSFgAetO47hfR5de8NIi4DrXpTskw3OGVXGHhaMm_MGN9PwIOng-WnUsKpTimnX1YZF6ddB4gMsTpeOKb0Sv9ybML5hcdCd3zLZV_35NSdJxCmfWHOJkUg9M_3fYNzEt5QdASq0TQ6ItOM8FP6WaOX3UUgUsgTT3j0FvUG9NjzLWjf_qoOkvIQaAJ7GN_AhgbE8HxVpGk9TUcC2JNjZVcKl1uc5bt0EqZ19QYOO41GE-mAY0yYX8eMt_VX35zvKGtbu2yhRZgyJlk-7X87g6Ei1ig9XMRs281Jm5gcYxUv9XO5M2Uai91S4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=TAweiZPi0cPneftYq7GySfaIDwmtvBo1tmqKoZgXyMGdcwPs3hJVqNzsw2-7cBwPJuCTRzdc7Kh-LqiAbYhH9rKe0MZbj25IJiJ1Fku2YJ28EAsz8iPQHTIp6ANIp1poyEI87xyytTuxZq3NyQSVBiKdcN8viPIyuS7f5CqUTuPzdy0sGUZPsuQp-n3bMjqKgxMslasEcKQx-MeT9lrHLZmxPj-5zDCzRJjUTGNXmzKz3mivC1qdsVgNR0Abk5qZUC6Zio3S1pyr0leYceUHDpaZhDs0ZBP2xs227c8cDfV1Lh4KRcjEQFyt_xMsCIw68sea-GRM0EowEG-VwwplNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=TAweiZPi0cPneftYq7GySfaIDwmtvBo1tmqKoZgXyMGdcwPs3hJVqNzsw2-7cBwPJuCTRzdc7Kh-LqiAbYhH9rKe0MZbj25IJiJ1Fku2YJ28EAsz8iPQHTIp6ANIp1poyEI87xyytTuxZq3NyQSVBiKdcN8viPIyuS7f5CqUTuPzdy0sGUZPsuQp-n3bMjqKgxMslasEcKQx-MeT9lrHLZmxPj-5zDCzRJjUTGNXmzKz3mivC1qdsVgNR0Abk5qZUC6Zio3S1pyr0leYceUHDpaZhDs0ZBP2xs227c8cDfV1Lh4KRcjEQFyt_xMsCIw68sea-GRM0EowEG-VwwplNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVesK_dHfBkxGD_y7jUcXfe-B-6bylUP_zCRUhFe5IbEC9nkUddcY5rTlHl2yJN9vPKRKRcJwDUSkXP1gCLM1wUoC4r4US0bPv8Mn8g6b8FXz4ZtzHAHJPqycnv-2CwOwKOkIwMuaY1bvvQqQ39GLWxlSa-n84vsiVEAc_3aWXGRqFNvYrx_Qtw1pIFGc8ksQD9ey_ZaDFUXKyMn9H5OkF07sg8U1mM5-ziovKlZPHpa5qt1NRRvpmj66kHjE-Bh6TSZiw9Z7datteuLSlkM8GaUEQo9CSDN6UK-nBKrx906xAc4ffhHNBH2OVRU0fNt3HX66gF5fNNttM_uZjN5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mchg0-E4eyu1eVJWeAKLIplswn_4eX6g_JjVAXjowFWMv9qNEc8WG7y8XkVPDUH0jv-tLdnQDUdcC2k3xrc6tT8miZlEqhKsC1yLAgGr34ioa43QAxI4tUiVIodwTCH4wr51kWSOWbFt1n6JUEtppVJwzE3Jyu80NWqM8vKIP7fbe_aDP6vbUc5h6gPF8mbHMiVAc4S5BHtBIoax_kdKrdwS0Y2YXbs9hSzymF_eLaLFOuu_zJ_ETpZrMOgObSI8leIHG21FWdsn0_ZZ8OF_dOSJX5BrRcglob562CCWPZBw408LugzzOF613Fxkmcl5nejI47-DSyQbpWc1RdkTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV_Vpuzr7WkxN4OC0MrMygOTGqlaSbJWrMel77JHMB9fH52-417mp3JSZxhywbzy-NJht_iR3dYz0N7hmY9pxu8FausyZ26a6uoSvLSAQdGtxfUQ_KqzLVn0KEhNl8v7SxQzxwDC2MgfFDQ37FIXRXOomeW8jcLftWNETtBrOCuILlbsMscW79NUeC9C0noeopb5IEoTFTf0iXzAKJ56Qi8MR9_SPiWHCchv7KiHO3VGa2-H85sJomLDdae4r2tdTBby6Yor4BGCAwgZHgFUprs6B6AnHNCf_jqMcZYGG3gokBPNOPVT-NK6suZa6o0joKlRkd_npRtkwAxLkzv42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwMn_k-sOA4M-y2QiOJ4aWUZk8thQdhbEEZTjAmTwvOHUO0AZpx6gSU0LYzX-MXydy_Cex8emqv3iVFkpSVLXlcqHcO4BSrXXFBY6wPsAiFTI6PlyW579QHUe2w1RILjGfRP2rU4Koo7Eo6GDoTWSai5yEUxE7whXc1-_f6ynX6NmFDcYAPmo2jlZFMeL5HQfVhUfVmRKgEczqM7FpihNYvxC7pjXw7UppuUQrKQ_VShwb4PpKaV1fdky9ljnsnOBukACcvbMPis0z3KyYmUYE3UqyBWrbEZyjloOOzaXw06CQwf6Y8ws561FQOrCtxR-luQ2cPB2vmJUxSEnlZ2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAkqnAnAu1yflJFIEHETtYUs4l9dANlMDBXWbhEvZq85huKjy3mbzLK74HWuPqEIFMpmp2Mat7GGkEWxVlp7AnZyBuQvvQ3BgFKT0NEpO1IRBpBZilH4MRWZwe3ZfDtv89-o7-wyKynFeqC7oWGJO4GRKfzgPNjXLfAlPabGrp0jv3CENNrHdeOqFq2ufpQFeg4Rpvk9py5VaKMBdYf_XRfIYeLMOxsMWBcjgUWlBiF7tCkWrzMHtT7ifM_lWj4i96Qca0ZB6xrCUYB1eCEQH1U4GjpSIB-rKhBGr7eA1UcWabT0ZVkUka5SoZimrRMv3iuBVZCAEq7dkh_tD4hlqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZvQ4bSNhEeQC9lSEtLnQEf54UE7W2dob-r4zWwbeb68dwkvSfPbljzp8BQ2n-TUDB9a-_OwxJjVcNQ9dqB_e44f7NqQ3WQRoCEnJY7hztS0X0UyOaivBhl-fTYiYSJc6dHKGqzHsgNHUSjJjMgqyiZ_I_T_IYY1VRIx3FjjdQQES7i47TuWvtpXQWtfdsYOuBzz2HpA0CEX4_XuP9v0aIVpfZmfLu4sbp9scrwTHRUv1kpfHjjcDFMVHfMIy29KJKnjFkwgJHWOZ6vreboTSIyYQ2D6KTWpXynt45263ZrpXOCA0015RglrylFSXRFL92Q07nq5gr3MvJ1HUt9p-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um8vsQU9IG5Ua36evmQ2fkH_EEi32Vff6Zd2eAdQmr87vVJ4YFa0F5MJNMDU43n1othpDCgwd70WRxpKODwzoCxNIkZ3QvarZsCSE4SVf_lNbj-Zrr9WbaOQ1plxiZd1hi18EV-BgtYIOd7qN9M4QFS3S_Kl4YYHOEaWCRy6DLg77hPi1HlRYmo0fI_SBb1m24sI-Lyjk2TO4APu1sZ2l3Lgovc0-vyL_OYWkBcPettLD0DQ01IMDc0SxDrt9RVbV-HFl3WVxuBVyKiE9X_Zr7agnhSB6pTThGrZ_8mFPJH1-TFMTwmMZsosfj42YgCTzdw157yK2OjRzhgxU4nczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGq6fsDusIRHfghJqGxVG9krr-_V_DnGJrczppTQQ7t9io2Bk8dhs2-ig6lnrB13Uos90hvAb6rEtBnsIPvyXnAvRkE1UutcLniTEe5vDTB-HuuRsyDDGW0te3oguNpvmgwfAJmc6YwJFjvZpBAZCBsWb0IKRkHo_bpu5dA6dWirBqfDSHt_0t6hSJUytGWPRc7M29PE0QuxKgkaBRIiZ6O7rmjU0p75vVgPbhD6EBfbgrvy_ePJlxn0LgCzmwTP2E1GFcnKQi0_m-JmkvJgqpD2P3u1_Oqs3U3J7MBZesyndeOaMW9yHP_79STn8D4utSLsOf-V83cHihAtDmNNHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqKzq-OmBrgEmcH0iSIw0N7CI8CuqKqv-HAvyubVaJVMlrSefMVL4wrxdtgSwQjZuUaJCL7juFtThN5ViNqfdAk6GT0YWkvBJsxmSOZWoY-c83E2PDNjZbAqM69DSoLvDaQGhL3TrWar_SFtYk_xPACYm81UUwvet310sRnZ180xy4pAaWGyWo8v3w8BeqnFE9wBrOwUDXl1nKXS9hmDQkN1XugBnHeKpDl9rZ3BYyLtUmFobDND3-muijmOoE1SRzmAGlAWNlSS6nM57Ep_lGA_sMi21Ty3mT1Lz7FoaTGwReY5j1Totp42q16rH2vLjPE23mpY0HYXfCc3V1eDmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=HU7P6i-5IWo0l4aW1sQj67YmKO8ySHV5JoOa-wf0s5nEQYaXSPDJ5WaaexdXujIETZeBKQ_jtlgOVunsB-SjSlnxcX9_6WQVXwNhgOHAY99NKCV966eso1p_ag7yUGPol8VSmVNU1hwxivyFZo0Kdg9sOnF27fcWt_L7xEj9KbO6QjLDWZPZdOxj8VB9jj349-YxrGkmqzK5EJHAl7vPKchMN6MPwaj2hMFnrpHdRdBmzZ2sckn4kxbqVw789gykZc3O41yqBKfsimCFyWF3rkxjnw0LE5LkkSaQ1sS5LFloFwy3hSPcpWcaPTYbx8R35EjLDwCzfUfxV9IOHIVjtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=HU7P6i-5IWo0l4aW1sQj67YmKO8ySHV5JoOa-wf0s5nEQYaXSPDJ5WaaexdXujIETZeBKQ_jtlgOVunsB-SjSlnxcX9_6WQVXwNhgOHAY99NKCV966eso1p_ag7yUGPol8VSmVNU1hwxivyFZo0Kdg9sOnF27fcWt_L7xEj9KbO6QjLDWZPZdOxj8VB9jj349-YxrGkmqzK5EJHAl7vPKchMN6MPwaj2hMFnrpHdRdBmzZ2sckn4kxbqVw789gykZc3O41yqBKfsimCFyWF3rkxjnw0LE5LkkSaQ1sS5LFloFwy3hSPcpWcaPTYbx8R35EjLDwCzfUfxV9IOHIVjtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtDpzY_934SWBKalv7oEreAzXA8jak9eWtpyv8GwUtDykfzbJhSH1uwcVP4kpcuagH_TsFkNB4aaF3j_qA2U1vaW-m0MpJVNVbE-MuFY0BYD9MNtlyu1zPauJ0TBqsL8R6lFK4CD3jJjkwmTlxgdyk7kP_BU6LPqCGSuh3A1c2nslxNs5syhW75releI-5KBlZdpLYTSyacfnq3nEPJzbxIxoZIWUqINW_CVO6ysNF5uGXkBYkXWK0egXsb1I9y98lowW81dWiWsDmg0ByIqBTCbFGEsMcsuFFfcdWXW9c-ex148i9AeG4aSxtB1zLLgN0RIMbb4KQtNwQJo9LTBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRv-Pw0Y_5bOn08ZRxVUWyZDLVe6TLqbcFaRp58UFl5XwEbz7F4qB6laVIgYX87Cjd8_3ZRmqGQvd-m3r7JF3RPBnYCww0s1KN1N1EuyWMKKVPxOO_R9hWKPoloF_OaLfSPJuGsUlu5hfMuH_2R53FsiveI2369_XaQ4K5xkNfr8CriojIYLbRHuMOUiH7Wi3CGVCMjn88GFHCzHNOTR_EZgKlvjHjm5Y-SbKkjUBRldBdTp1kk33zTl6tcuGB9pQxoZOaBBzCZoEveJ0kZeUIAkCIhu51sHMPm2-DuQZJo9t_us5xv-G0ISWUzUJWoQ-c_NQCk4bcNnHRku_o6tnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TdnQR289si6pdq4rKc2F_J07chNw_9gCRfFML4OGT1gLPa2W7xPwkhm-f1A54fIFlcQjLszmpnAZ6mElGtM63PB-VcXC3GY_5l_fGnZQtJ4CZsgqdXwSHWAqw6ISCo-9kniZKEHr1KQRimBvj1hZ7Dh2lkqOKXaXy9TgzW7mHvWP7oXN7FZltg7mvnpq2o7sQ_H2hw-y7359y5aaP2jgfajd8_0YEPAFX7cyJu6jt9VYvLmu4t00kcqUYgwMLXit582W_EWxvTTH5bGSJXeNaEdb9-lFXNOPa8IGAvc8x9DIHAUgqjd5mKmLOlXqCn6x0zbhfql9kIfoosBbPwBWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/seSb-zn4EEBcAfyub7LwPebpI0BkYSCWbO64pmBF2qNTvlr6EhhWs4pFcD5INmLiG1P4MnFRp-jC6QX1FLtOcyiZSJCX7HyY57MSaQbTcMvCFBsRaH-OiKqB9lbnbKaR6MDzR5F6WLO0158MzpdHm-UNhwa9KzHsCDQs66Lyn9wj-zf1rIUDz6_xsfNcwPGFRQj6sN_LAUW0KmPB65jFzSlXyskXO8Mo8oESNqzo-KMHCUYfSY20GKWw3jRgKZuloWXZY5xEPC2E4rYsj4PbbnsP1fqyRIOxgpzw2O4ToPM5Cy-eymNqkb9D7o7vOFM_IA0-YXsKQr8LdBoPlpXqIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=d6yZacJ9cQdvpzL8R0SElkw3MgpF0dWWSd583j9gcc2h7XrdyjWYr_uZTzrTpNfppoVy_HG_e4qBuIkGVvO3Gq1MVUtlu4PBzhUmCr3u8GoZj-e9VnxkUlSGkTlkMl3rJ0-kYPtt9UQJuVWxetOddo5ufyubT-7_JDo9ePFANLYW8OMGcO_XqIxmUgaEiY1j9KrX1pZgUOxrUipL6OniOBWp62cz2EEQcC4b_chJMirjM-KLaEbPAfvneDmVd1LsPt2h8M--SPZSXPaRRJhFIVkFAH2evD49dIgaMAOyF2Rg-JCgkmJEG41URP0ZK5QdM_V9xS-VlVaaEQ6-x7MnaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=d6yZacJ9cQdvpzL8R0SElkw3MgpF0dWWSd583j9gcc2h7XrdyjWYr_uZTzrTpNfppoVy_HG_e4qBuIkGVvO3Gq1MVUtlu4PBzhUmCr3u8GoZj-e9VnxkUlSGkTlkMl3rJ0-kYPtt9UQJuVWxetOddo5ufyubT-7_JDo9ePFANLYW8OMGcO_XqIxmUgaEiY1j9KrX1pZgUOxrUipL6OniOBWp62cz2EEQcC4b_chJMirjM-KLaEbPAfvneDmVd1LsPt2h8M--SPZSXPaRRJhFIVkFAH2evD49dIgaMAOyF2Rg-JCgkmJEG41URP0ZK5QdM_V9xS-VlVaaEQ6-x7MnaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfYkY3FuQ3w1TCQSTUrYdMrnR8v7_WmxRpUSZvp8tp5C-bWKJ5dX4EjwACoTaO71hSBJdMjEESXwcEfw0CLbnzmdhR4e1-_tZnAIgZuclqApj2NHbERyAwSHnoz3HPWa7CMymwDVJzIdXyvkginiN1Gp5g35ME4jzcoceS0-smSONeGXwwti2xePSV5yH30CfoSjyl0wUy9VKvOO9o38fW7dUm8_3_wGSm8CQTQ8Zkoxl1NQAZhfz0I0DqsKz9Js0Uw1i67xgDgiMU-U_ThqE0gcMw_Phl7JJoMPQfwUyDeqYrgfCjkzr_fiokPkkEHJLi3NU1fA2fgIvFHF4RiBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=J-sjfgMoLX-O02c9VQxZk54xTdf5W2lZhiodWTd9WhQs5lf8RPsILTuROv01hTE1rXaFdVBOGVEhmvOpcgCRB88r1PvFzR-l12XatT1ybh_ed4y9X9XBQvidPwJyys7NNne_0i9h-sOHRMlDfCZxxlxSgzhAbifC0BGmSCE5ahiBHkVkZrDU2MS6Y-UFbWoiBv-QPP51oQBk2M_qFHP-zzjgKtpUBItVOSvHLs2UC9oqkcSSCVmGqrOYTHtq6-gwcGZYMBGUUb-8c4erqWWA4GQBQvAohI85kfOVJdpj-_PHZCozw2PBHJnWx8riVGbGBhNqGERZQRx5cE1zzCNDIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=J-sjfgMoLX-O02c9VQxZk54xTdf5W2lZhiodWTd9WhQs5lf8RPsILTuROv01hTE1rXaFdVBOGVEhmvOpcgCRB88r1PvFzR-l12XatT1ybh_ed4y9X9XBQvidPwJyys7NNne_0i9h-sOHRMlDfCZxxlxSgzhAbifC0BGmSCE5ahiBHkVkZrDU2MS6Y-UFbWoiBv-QPP51oQBk2M_qFHP-zzjgKtpUBItVOSvHLs2UC9oqkcSSCVmGqrOYTHtq6-gwcGZYMBGUUb-8c4erqWWA4GQBQvAohI85kfOVJdpj-_PHZCozw2PBHJnWx8riVGbGBhNqGERZQRx5cE1zzCNDIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGKwsIsm_lJYhWnWbMVOnGjGBI8pxLsy4XGkWBwaIZRcsidJU0G3Gj6Bh21nyYYPAFHj9Y-I1Ma48SAwALyxAI6fqyIPofN4OuZnvv4uU_bpP4wuBzymPA35v8QMv3iCK1H2TvczhgGc0WuNcVMGSJ8l2kD1OQlrcPnMNH6OZ71LuoLJfSh9s3sjJl8Zf0JPbCBMYD6uLOPE5f5k-vCdmH93SyB3thwxHhUpzfqhY0vhxNAgcJQHDGYirC-uRxZIRkWz87DZ7LqFG61rpJ_44v0w9QwiU5Y2t_b4wZVFPKoq79ucfSUkXZaYN_OtF-qlAnYoGOVIz4phI8WuR3zJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVn3XqUz5fOIl3JmEsryuvJuWXvJ23PuWxuUNrCvnVwG4v3g9kkv0nBbxmGNECbe8uxEwPdv9JWK_DYQ2bTwjSuhPOxOdVZjbYtGMopJ8n7J4vimqPETF-Z5eVtpQnpQ9JMp3xEZwBowSbKzVoqZg1gG2sE5tLNef2noX9nBjEUxTfpafrRX02Q6qywcqGfcUNUA3pKiqsv9HbcrlzOE6vGJbGIEWTcbe0IlbFtzppcnre73StOIDYZ1LmIHR3ms2TigwweV-6L3ZI_JBwXOk7ujdSerNFYjx_dLfncm9JL1sZi2cAXN-myFifaWMxCpzthEjauME-y8tbt6Q4WOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=IMTX6NtvxjrF3dNEjre71yDUK1qMWR3gpS2o_adgI6lSE6CzK8ENlMJ-zYG1S-m-ropQt3kGbuzLk0LCVlZ-CYJDBmz85YKZcylOGu6cbz8wD2ZRx4EU5gRov8DDPdiEp1bdl4BEako2tA4JDCPxKu3Srb0zYACpMSCLonkDnZKTKequusQ8w0uZ0Gl6OOkSBUC4kggUnEcUWu3vKH-l8Ino577U2B8Nwqfn_Vqj4atH2jM0rGu883y9633zV1rpDIdw8qU8vnXoR-_vE0IJlxTONaRwAk7VNLVK-v6QJV9nHKe2pkLxGZPbN5wZMgE_quO5KjhnvgeIzy1aMxWNcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=IMTX6NtvxjrF3dNEjre71yDUK1qMWR3gpS2o_adgI6lSE6CzK8ENlMJ-zYG1S-m-ropQt3kGbuzLk0LCVlZ-CYJDBmz85YKZcylOGu6cbz8wD2ZRx4EU5gRov8DDPdiEp1bdl4BEako2tA4JDCPxKu3Srb0zYACpMSCLonkDnZKTKequusQ8w0uZ0Gl6OOkSBUC4kggUnEcUWu3vKH-l8Ino577U2B8Nwqfn_Vqj4atH2jM0rGu883y9633zV1rpDIdw8qU8vnXoR-_vE0IJlxTONaRwAk7VNLVK-v6QJV9nHKe2pkLxGZPbN5wZMgE_quO5KjhnvgeIzy1aMxWNcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sISRQKc5P6MSBKfCv9nGtUztxn_m9GV6ODwitfo9NwNT7tvQrLMYf02QuboxcGWP1wb6oOZ5mj9InfZ0WkByXigxTuu4FnH29Kk07ba_-xttrY_p4OeSgMQop1mXRpC1kjjmipQPGMiPSys913GdIQJGwN33AmMZNAUO6KcgSx788cDUI5T34HhxpzwqcbrymWphm5WX1aTDkWyfM4HDlwoGtQ9Yqe0VqGwRJFUttcf_FtBudaMBEJryMFfL2OI1loba5PaOPMwu1Vj-lO7XY067zA7H9BS_7WAVR5YcIrIFBvBulxsM3PwCqyH4_5iHy6rOzWFTt2ftKfoLCu3nEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=MyMCR1THiFhycaH4EVhFLmXR5q4BXgPpGISTD-lI9J1ALNPCOhS7X0bhSg6dXW_Rq0MmCkj4ESv5KFovNQc4PCeEkMsADeAgteCuaeuExMP5Uq7pqHykXpUywor7ZxaDyU-kAox2zkEOJAC7zcksR0sH0zg-IwQQ2fhzv0Z2szCdvZ0DHC8TsdiiOcS3uiR0j5LAHi9PxQFoqE64_LRLemnK5fZ1z0RE-br5etdW3qU9nuOCDB6PZYATUKUnD20LRX7RjPLDH8OExYVxtgbQbbLEMK-_XT_-S-jfupRNJYn2RuZHoV4aHb2xH4nZlLRDaXPZ0ydwXCkx00YA2jZh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=MyMCR1THiFhycaH4EVhFLmXR5q4BXgPpGISTD-lI9J1ALNPCOhS7X0bhSg6dXW_Rq0MmCkj4ESv5KFovNQc4PCeEkMsADeAgteCuaeuExMP5Uq7pqHykXpUywor7ZxaDyU-kAox2zkEOJAC7zcksR0sH0zg-IwQQ2fhzv0Z2szCdvZ0DHC8TsdiiOcS3uiR0j5LAHi9PxQFoqE64_LRLemnK5fZ1z0RE-br5etdW3qU9nuOCDB6PZYATUKUnD20LRX7RjPLDH8OExYVxtgbQbbLEMK-_XT_-S-jfupRNJYn2RuZHoV4aHb2xH4nZlLRDaXPZ0ydwXCkx00YA2jZh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPlbZYyOmVwVMytfZuaXHFG6InhMc1LyLEhGlqptCvmAFyNs7QidFHjhxfV5vvhPuSQhNj6Vk6VCKgp2LGhatlksvbU5YUlx8B2pRP_aullWXohxDEMN4HFvOvNtIYyni6PFJ53uayIIzRU1bN8ANmuRkOW_rS_WR_qBXjnc1C29DHAXAZkmZ7L0XLtqn4GDLpVTlYDdkry59vmT4P7gsbj3QHzF1smn_9BeRWgZjJwXC0Z0IkMW9nNtzwtXQrfHbkjglp3d_ssiGDm-uPdSZmFI1fujDI1okwKQLdq7CfZl6Mfs6jKYPoMEHcF68WasnvOQrD8qisQ2rI0Tnt0UFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
