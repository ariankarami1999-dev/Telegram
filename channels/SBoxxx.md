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
<img src="https://cdn4.telesco.pe/file/aYLsSkJqCX775jxd-LIct-m1OcXMFrAqZBTsImVIA2OqVLCNAzdSdwDdrG9mWZgxnMl16j-0lVLFULfh_tVlDbnUKGg_b2n71ktSYk0zaBDeCq2HHfdwVVDbss82rWzFH6dclEWCvPgr8wbd0Omlz9OUF0tgjMsOayWJ43bkhp68d_CSTlBCgYFgXcfjbKF6JOPXPXHcboN-WKlEU7WkrBKvSdLUWkhgkqL6Ml2EolbZFE-ZfKSMzDC47LutCt1H0UW7ZaPzl7PT2dapnDdU8gaxvV_c3fBFGFL8nALSNAcRz9kmlEz0FXFQvjb8SpqkoGx9Z-P4HeG7RqjrVyF55A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-18665">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SBoxxx/18665" target="_blank">📅 15:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18664">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به نظر می رسد زمان حمله نیروهای مورد حمایت سعودی یا امارات به حوثی ها نزدیک است.</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/SBoxxx/18664" target="_blank">📅 14:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18663">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :    تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SBoxxx/18663" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18662">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :
تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SBoxxx/18662" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18661">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/18661" target="_blank">📅 13:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18660">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/18660" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18659">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/18659" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18658">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvcIyyd2Q__rRdJSHnF3aZNtDfOnaCZiAtPk2E3bq0ciVcHjbYyJSMQwUwXMVbZ7ON9r0pnlkAf9SVIIjJKAeORcu_ChP_5TaAi7XyTKMp7bpo0vHtfgZ6a5ON1Y5RbvEzS-OIwRKztBPz1mOk-f8UyJsgXUzWOxUThzv2jS0GL1t68D-j0Q660SJlIXWFwqk9LmZfW0LGrhk_MVNPxmhlIOkvosXeUf14o5ji3y4wTiphF-1MJYk_Xota-Ylk2e3gKRHMTRCKnU-f9KGUfEsyRyBqIdT4ahslOJ6BlsOmOFbJ-tCQUUNeErb51VptzslQsHojdzynn1YGLq4RHHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.
زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.
اکثر این پناهگاه‌ها برای اهداف روزمره مانند سالن‌های ورزشی، زمین‌های بازی، استخرهای شنا و حتی فضاهای تمرین برای گروه‌های موسیقی راک مورد استفاده قرار می‌گیرند، اما می‌توانند به سرعت به پناهگاه‌های اضطراری تبدیل شوند.
منبع: The Times</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/18658" target="_blank">📅 12:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18656">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=ghouzx5HHj4Tzdp1WtZUzIE2kAG_fgUvzWuHnVenq1gvS4JgHdoYUfvSh16JyntBd86r4AvhP7KDNPAsZqe30QZzvEjqrQbOGq-97Q8z3DpXGBXorZO_nigBslbTpW65R_XzyAJ-UwsqRY_x3bXN3aAEFi3R94w4MPB2-BuF1wqgKkF7DOGI3vEFgNOvIocSzsIBznCB2eWcBNd961K9r5-X32rmM632IBtfLKw4x4-j1xrLTtC_2wQ5UGWbgPP8MIk8_bXQf_6Lb3s3YlkBWvBDAQ46zyZsvcSwXgWq5m1AtldDSkOTyWLYdcvJ8xZ_xZql-eF2Sa3yIuk9PePOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=ghouzx5HHj4Tzdp1WtZUzIE2kAG_fgUvzWuHnVenq1gvS4JgHdoYUfvSh16JyntBd86r4AvhP7KDNPAsZqe30QZzvEjqrQbOGq-97Q8z3DpXGBXorZO_nigBslbTpW65R_XzyAJ-UwsqRY_x3bXN3aAEFi3R94w4MPB2-BuF1wqgKkF7DOGI3vEFgNOvIocSzsIBznCB2eWcBNd961K9r5-X32rmM632IBtfLKw4x4-j1xrLTtC_2wQ5UGWbgPP8MIk8_bXQf_6Lb3s3YlkBWvBDAQ46zyZsvcSwXgWq5m1AtldDSkOTyWLYdcvJ8xZ_xZql-eF2Sa3yIuk9PePOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قاسمیان: شما نباید بگید آآآمریکاااا بی دوووووو ، باید بگید آمریکا بی دو. یعنی باید با تحقیر بگی
✍🏻
exxon
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/18656" target="_blank">📅 12:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18655">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/18655" target="_blank">📅 12:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18654">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/18654" target="_blank">📅 12:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18653">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=u_rbwdTj-lUOM8nl4-ckzIeWGaZT99gzkIXQkABpp_Tfi833--DXxXuSIg5SNKwwFs7Zd9l-3X7bLrnrVYsIjToMeRHgXSlAzhyOH8QULlTu_O1W4N_WmYDR58wIWeG6PWGV7af17kweAtSFwgFDe0E38OYC5irjjd4lx9YbYcfePTw2-X3QgNpDbQEMNJBLxgIJg2Xk7EPMZkKDmiB6ZXMISIBb4e4kTasE8wG7AnJyBtBzslczRoJbx5eW1k_O-KsWTKOypNwgMkof1PFt9Gdx7vQRUMaNoolq7MgEK-SNBTcOTWt8HpSlgRxDVK19u1aToJzhFxdSD_wE30R1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=u_rbwdTj-lUOM8nl4-ckzIeWGaZT99gzkIXQkABpp_Tfi833--DXxXuSIg5SNKwwFs7Zd9l-3X7bLrnrVYsIjToMeRHgXSlAzhyOH8QULlTu_O1W4N_WmYDR58wIWeG6PWGV7af17kweAtSFwgFDe0E38OYC5irjjd4lx9YbYcfePTw2-X3QgNpDbQEMNJBLxgIJg2Xk7EPMZkKDmiB6ZXMISIBb4e4kTasE8wG7AnJyBtBzslczRoJbx5eW1k_O-KsWTKOypNwgMkof1PFt9Gdx7vQRUMaNoolq7MgEK-SNBTcOTWt8HpSlgRxDVK19u1aToJzhFxdSD_wE30R1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/18653" target="_blank">📅 12:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18652">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:   «پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی…</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18652" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18651">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayLIkfIx1ooRdBC4H_KvkjQa2MZGRocfeveaDyXp2isMHSQMuBiov8cOP5JNuyLA7-gn2g3VzZaQz9RlUbfOngtTgViPg6z8VoNg882iaLRuzn-QgoSDehpjHsWUdACxaugL9GQEaeDVwc3zwKoJuqGCcGEBZ3aaWmjtcPXlZBs2gQqkdQtEXX3e-qW0D3IvjoVHlvUyGtiDJkDriLKTz5cVJGEZdnPM9uxH_3o3dvQHFcFYyDE8IrLACO-YLE84J57MJ0erAGT-9NYV6WFbGm3YLpS5NukWukpFm8Vc9vNTym0tr4ZFtumxIvwybuNzTmm1FVbYflIIiP28m73W-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:
«پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی جهنم کنیم.»</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/18651" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18650">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9aEH-peW-N-PtvNRav7sQUDO39cso2QuvMf8Z3Mt8fysfN2n0FsO2Dsr6tozV9Y6BfjkZdBlQYa5_5MY3vw9mOlPxNNVg6vTb6KxgnsHKPXyptgkFviNdgnXnwcuZMnZfkbHabPus0SWATLcikpercr77-x1bMu4zbroundlD-iA7lGTKZox622qdOX5_jXuWIwfxipJw9P1PvRmBl-x9qBBk-53WOcjHMSXkH1KvE9zEBcA0sQmImSLYQgS54jTtgMlr2YYEqUykfUsIHXHyIvzPS7-nENbXphgIp0ZTjnmr9SmA9GTs5QXOnSl10ZmJ2k0LIxhc_rMROTNBymvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/18650" target="_blank">📅 11:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.  هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/18649" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران در مورد فوت لیندسی گراهام:
عزرائیل عدالت را جاری می‌کند.
برای چنین فردی که میراث زندگی‌اش سرشار از کینه و حمایت از تجاوز بود، چیزی جز یک سابقه تاریک در ذهن مردم باقی نخواهد ماند.
مرگ این سناتور پرخاشگر و با دهان گزنده، قطعاً قلب هیچ فرد آزاده‌ای را آزرده نخواهد کرد.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/18648" target="_blank">📅 11:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به نظر می رسد نیروهای آمریکایی دیشب از مهمات ویژه برای تخریب تونل‌ها استفاده کردند تا یک پایگاه موشکی زیرزمینی را در نزدیکی شهر دزفول، در پایگاه چهارم شکاری نیروی هوایی  مورد حمله قرار دهند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18647" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18646">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام:
موج دیگری از حملات را علیه ایران به پایان رساندیم
تامپا، فلوریدا —
فرماندهی مرکزی ایالات متحده (CENTCOM) در ۱۲ ژوئیه موج جدیدی از حملات تهاجمی علیه ایران را به پایان رساند و با استفاده از مهمات دقیق، ده‌ها هدف در چندین مکان را هدف قرار داد تا توانایی ایران در ادامه حمله به کشتیرانی بین‌المللی که از تنگه هرمز عبور می‌کند را تضعیف کند.
نیروهای CENTCOM به سیستم‌های دفاع هوایی نظامی ایران، سایت‌های راداری ساحلی، توان موشکی و پهپادی و قایق‌های کوچک حمله کردند و برای اولین بار از هواپیماهای جنگنده ایالات متحده، کشتی‌های دریایی، پهپادهای حمله هوایی یک‌طرفه و پهپادهای حمله دریایی یک‌طرفه استفاده کردند.
تنگه هرمز یک مسیر دریایی حیاتی برای تجارت جهانی است. ایران کنترل آن را در دست ندارد.
نیروهای ایالات متحده برای اطمینان از اینکه آزگان دریانوردی برای کشتیرانی تجاری باقی می‌ماند، حتی با وجود تهاجم بی‌دلیل، آزار و اذیت، تهدیدات و اعلامیه‌های خودسرانه مداوم ایران، آماده و مهیا شده‌اند.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/18646" target="_blank">📅 10:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18645">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آغاز خاموشی‌های برنامه ریزی شده در کشور!   مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:   این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/18645" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18644">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آغاز خاموشی‌های برنامه ریزی شده در کشور
!
مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:
این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/18644" target="_blank">📅 10:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18643">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3qa8sbUT3oN76nmpYpv-9gZbB8CcTDPoEk0-RCuK-I1ci5U25eS07vKFl93CkOAswjfYTlAltyR2bPYU3k3NHiEG3e-XlYHePLgatQjOX7Nbg0zRQOFXsnJvNCJcSysmZT0SsAajOXV-OHdJb0-oSrmX1R8wm2oZ_yVq5P2C8vnj159eEZbZig1C2GU-wr1dSIxwrBjHln8-BpsoZ1RXzp_dY3LcCaKq6-9Jl-W7eVq0m3TqFbLcMtvF9Vg7U-76YyTyeU2c0z-eTaDhu_cfJNDwunXguO5pd0kDAgd3A7Qj8zYn4mNgGZ0f3IheZrOgfidLQh2fZLpwTgPyGAbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18643" target="_blank">📅 09:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18642">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 6
دوشنبه 13 جولای 2026</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/18642" target="_blank">📅 09:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18641">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/18641" target="_blank">📅 09:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18640">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/18640" target="_blank">📅 09:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18639">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frjksNYnjzZtJCjGXP_JEw_VzsWLcmdC8OnG__8GLoouOLyrgegahpTKxwE9WvaC-JMx103zn-tvnZ86h2J7Yw26OwaLnVbh-fztljar3QUEtNfqsTrFtsNdSD27VYf3b0B0LI4wcb2rwO89j96sNU4T2j2OvE0ea2fGJNQ3if-K_FTjvQohR9MlyPTuzgSuYJmmZZG80KCZp9jPvhmUlx8wHKLhf9abijxLdHPk17vp00l22kFfbEFkOffWmY_KMSpZrUHTPdlL1nvuT2wTqSTT9wMn_eiTMMdNKzw15GgRTznSpiobfFl2aoRpc6qkVme-2kCuiGgvueZT_iyYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گستره جغرافیایی حملات دیشب آمریکایی ها</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18639" target="_blank">📅 08:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18638">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">— سپاه پاسداران:
«در مرحله چهارم عملیات «چشم در برابر چشم»، نیروهای زمینی قهرمان سپاه پاسداران پایگاه موشکی زمینی به زمینی ارتش ایالات متحده در کویت را هدف قرار دادند و دو پرتابگر موشکی هیمارس و انبارهای مهمات را آتش زده و به طور کامل نابود کردند».</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18638" target="_blank">📅 08:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18637">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد که برای اولین بار از شهپادهای دریایی انتحاری  برای هدف‌گیری دارایی‌های ایران استفاده شده است</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18637" target="_blank">📅 08:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18636">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.
هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18636" target="_blank">📅 08:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18635">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آمریکایی ها دارند با هیمارس و از کویت، شهرهای خوزستان را شخم می زنند!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18635" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18634">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMqw2isu9uvoblZFWPiQzvyUFN3fllO-f-UHoHs94ED8XwS7dcED7EXBuOQ8cj_4EHnBWHEeR-7wCa9chWn5KuIUMnezdLHiTd1osR1Y7kFKDvPjMw05-WkHw2BAk--qNaIpJC03lQaxNPWRSrGA7TlRebyzxcgQQLEUSGVirsz7RVbyZIFLlj7AnEZHm94nOGX9MUdlIotOZJ31vAMAHClAXMoydJ7kvcx6y_g1UKfhqWr7Whr-KjU1o90U3tlc8tewmJKwc_v7nOnNWN7PUHZgb6SEo4fqcI-1Nb9Ci1nHVph7M82XtXH2gxdUdju2UnOopvA1OmvF0JU4h-7J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربها وقتی میفهمند دوباره ما برای آزادی قدس داریم خودشان را میزنیم!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18634" target="_blank">📅 02:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18633">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:  با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18633" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18632">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:
با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را به خرج دهید.
در صورتی که هرگونه سامانه یا سکوی پرتاب موشکی در نزدیکی مناطق مسکونی خود مشاهده کردید، لطفاً در اسرع وقت آن منطقه را ترک کنید. همچنین از پایگاه‌ها و تأسیسات نظامی آمریکا فاصله بگیرید و از نزدیک شدن یا عبور از اطراف آن‌ها خودداری کنید.
از تمامی شهروندان و ساکنان درخواست می‌شود این مناطق را فوراً تخلیه کرده و بدون هیچ‌گونه تأخیر به مکانی امن و با فاصله مناسب منتقل شوند تا جان و امنیت خود را حفظ کنند. ما پیش‌تر بارها و به‌طور صریح به حاکمان شما درباره خطرات ادامه این مسیر و به بازی گرفتن سرنوشت مردمشان هشدار داده بودیم.
با این حال، آنان تصمیم گرفتند به مسیر تبعیت کورکورانه ادامه دهند و تصمیماتی را اجرا کنند که نه بازتاب‌دهنده اراده مردمشان، بلکه تحمیل‌شده از خارج از مرزهایشان و در غیاب هرگونه حاکمیت واقعی است. بنابراین، مسئولیت کامل تمامی پیامدهایی که در نتیجه این مسیر به وجود خواهد آمد، بر عهده آنان خواهد بود.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18632" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18631">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتکام:
ساعت ۵ بعدازظهر به وقت شرقی امروز، نیروهای فرماندهی مرکزی ایالات متحده آغاز به انجام حملات بیشتری علیه ایران کردند تا توانایی آن‌ها برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که به صورت آزادانه از تنگه هرمز عبور می‌کنند را تضعیف کنند. فرمانده کل قوا دستور این حملات را برای پاسخگویی نیروهای ایرانی صادر کرده است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18631" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18630">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18630" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18629">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجاراتی متعدد در نزدیکی شهر سیریک در ایران شنیده شد: تلویزیون دولتی.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18629" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18628">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=GN4m7Vm8AkIQ7uil_-jGh90QyEV6yenjUbRNAu81_x6poMa74bKm6khYHdTvjnOZUIjAlu5pSPokdsCk4GP11yUe5uwBbue2mJIkFhKXL11L3IPHmngzyNuy3xMsXEpZZsmQ00wNBHOgr1p5Un1CM8xrTLVAH-zZ8GbDAMbq0LbmtMZvitQ7Htx42ZYNvnV9gDgRdEnN-bVxbFZ9itnhbR3HNTqnImnfxrR5T2raK203qevIc_CNjoP9zmgwJ0R0_jlj3P86-X2upXruK0iQj58pNno6zQX5FNN7fI2Kb-LFQ3egMIH1l6SaSPS-l0zGkyc5loCms6FdyQ1sLngy_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=GN4m7Vm8AkIQ7uil_-jGh90QyEV6yenjUbRNAu81_x6poMa74bKm6khYHdTvjnOZUIjAlu5pSPokdsCk4GP11yUe5uwBbue2mJIkFhKXL11L3IPHmngzyNuy3xMsXEpZZsmQ00wNBHOgr1p5Un1CM8xrTLVAH-zZ8GbDAMbq0LbmtMZvitQ7Htx42ZYNvnV9gDgRdEnN-bVxbFZ9itnhbR3HNTqnImnfxrR5T2raK203qevIc_CNjoP9zmgwJ0R0_jlj3P86-X2upXruK0iQj58pNno6zQX5FNN7fI2Kb-LFQ3egMIH1l6SaSPS-l0zGkyc5loCms6FdyQ1sLngy_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18628" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18627">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سنتکام:
🚫
ادعا: تبلیغات ایران امروز ادعا کرد که سه نظامی آمریکایی در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✅
واقعیت: هیچ گزارشی مبنی بر کشته یا مجروح شدن نظامیان آمریکایی در این منطقه وجود ندارد. تمام پرسنل در وضعیت سلامتی هستند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18627" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18626">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18626" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18625">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این هم یکی دیگر!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18625" target="_blank">📅 23:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18624">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پست جدید ترامپ !</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18624" target="_blank">📅 23:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18623">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_FkUujY9QTfrTUpcwxEC-9zBhDwlUL_GYacqQKasxRp8LURMyh8OjYdb_LLFpXncOr_83GT4dtIccv6xZwQtyRVIUzWHnTMbu3djdlpbMS6DJ8WhbMOJ0o2dNIPcafFia5S9ub-nHc4bZEN4so1DrArt6x9eV3vtA3q3YalxGBi_vqDm0oNEtcN2mieqY2SlCAU0Zx_q9gHTjYwIsquuia3-5I13Ax6AMZ0SQxC_hEm9eNoA1eG-8n9-bUUdyiaL2tKmcv9waIl52upWo7NKegRJVjucuGDdt-Ud62TjVd9ywQxeA62GLZZZQdbZ4FAnCaFW6aFZwDiBbCdyGfOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ !</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18623" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18622">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TesCO57q7__Cj76KRByiBZjtGmuoFyEgyYhqIff-wPfb8UHXlyTl3ZBJgi5mCTIBTk9iKSwNty4r474YkSP3jpMSozxaKWC-WqC8TiHwV2b6RBW9k71DUxrJHQK4Kx5GojSbN2pj9sgJLQpwZk3GW1U1pY1gnFVxwVyiBPFPfzJdT14hJSl0lKBl1Qbj1Lc_rsRziAHKKFrMiVfzD0cf29eFm4h51MDeVsQ6Mg0g6bSQAg8QFYCOHjUMU108T2XeStaeHT2mcupkNvR_XDwaq4tctTyQDR0sqsXRQYNMTTplE99IiVci9fa8U_p0Qa3FBRDY2Xs1sonAiYu3zCF9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.  ارزیابی‌های فعلی حاکی از آن…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18622" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18621">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">منظورشان همین هفت هشت هواپیماست.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18621" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18620">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjZD8oMDKAunFdBBqAYRumxXfdeGD2jcYvsyNWLMP3qqe7b8r5DlsV2yTpzqpwhwde97SnVyMD9bm7YAiFpcXN0sknXdmiyejEJGw75_y5Mor9OM7SJ7GvRk6johrSLR9LDIreu1hUBF8aLkmyEW5OapMflN9Tg8eym1h_9Uwr12ePqjYIjlDyhDSgAS_Aj54shf6Cqh8SGpIoL8Ra6FSFokWTbQFESRTo7e2fq5tgQ5a4IEojzLqfRryETCWnqCAz57u51shQRaB_7g5T91bwl2ysXSaaPY2tcVBCnW0wCjIwAhEa99I0wDovfxTrCXjPhY0kL_W4URe-SkM-CCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده های ارتش جمهوری اسلامی ایران بر فراز حریم هوایی مناطق مرزی غرب کشور به پرواز درآمدند</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18620" target="_blank">📅 23:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18619">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آسمان کشور در حال کلیر شدن...</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18619" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18618">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خداوکیلی این چه زندگی است....</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18618" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18617">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHWNGk71IgrEJGXn8i_LkuFuniyTx3ZvcAJB-aCuBith8UqSmvHO1UBENDP-2it3pBzLZlryfEcmqPqcI5MfvHg-ihdwtoZS4nlW1mpl0xKiamZ-m04EXFB1TFneTsJCW5K03HPE_rF5qWKhy3GctCiWoYQGBgRWhOoIsfcNyS9qKwj5o2dLOtJomyPzwzuXQPiDF2aaAcQHkP9O1UVD_PojwLU1pZ92ZeErGV0tcPRd_aGxoWqlfgWM3C5fG1YP6kUD4Q4_cDuR6t1KC8DyIgtiqN88YM2LkCGyC00jdfy1Dkz7TMkXT72kvm4wB-hsmPsVos3uvLLwqdyg23T8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.  ارزیابی‌های فعلی حاکی از آن…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18617" target="_blank">📅 23:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18616">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.
ارزیابی‌های فعلی حاکی از آن است که احتمال حملات نظامی در دو تا سه ساعت آینده وجود دارد.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18616" target="_blank">📅 22:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18615">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18615" target="_blank">📅 21:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18614">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لازم به ذکر است که جناب خضریان عضو کانال ما هستند و پوزیشنهای سنگین Long روی نفت دارند</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18614" target="_blank">📅 21:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18613">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گفته می‌شود ایران در جریان سفر ترامپ، رئیس‌جمهور آمریکا به ترکیه، تلاش کرده است او را ترور کند.
اطلاعات ارائه شده توسط یک منبع خارجی که به مقامات آمریکایی در مورد این توطئه ادعایی هشدار داده بود، باعث شد تا در آخرین لحظه، هواپیمای مورد استفاده رئیس‌جمهور در پرواز بازگشت به واشنگتن تغییر کند.
— یدیعوت آحارانوت |</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18613" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18612">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تکرار حرف مدیر Secret Box از سوی دکتر خضریان:  علی خضریان، عضو کمیسیون امنیت ملی مجلس:   مسئولان دستگاه دیپلماسی ایران در دنیای موازی زندگی می‌کنند  آمریکا و ترامپ می‌گویند که ما از توافق‌نامه خارج شده‌ایم و آتش‌بس تمام شده است بعد مذاکره‌‌کنندگان ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18612" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18611">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اینها هم رسماً بیکار هستند. خود ترامپ دیروز گفت از دید او آتش بس تمام شده و دیشب آمریکایی ها جنوب کشور را شبیه جنوب لبنان کردند آن وقت اینها می گویند این کار نقص بندهای 1 و 5 یادداشت تفاهم است!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18611" target="_blank">📅 21:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18610">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.  به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18610" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18609">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ادامه پرتاب موشک از ایران</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18609" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18608">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSA6EKZZwKQhFa_FHQKrfBIyUa0Su5OpNm5YTK2kKsubHv2EdI4FI9t6GNawDXLA8MWO597m-jruX-yRFyioOBs6pTvm5ztCBNoMPOS9VMKw3mvhKd5SPUdhbUvMOylkDFj43ApFnOY4mekL3LsSIqHdyh3pYemSb8UbVrqOb0QhlcsjgnPs-pofHtm45QGUuDbQFbQmgqAePl8BYormjRzAd4hyIvHHwvmDUZl9gdjxjMZdo_KuGxPTK_xaW1eniVtGAM7c2awjXxw8-yY-AOofEeEbIEyrVctzlq8J0d3qdT251CwShCjWjIft1HhWT4LBt9d7O1pgLHM__nW8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی این حرامزاده هم دیشب سقط شد
مردی که قطر‌ را به مرکز ترویج تروریسم اخوانی تبدیل کرد و از حامیان اصلی حماس و القاعده‌ در سوریه هم بود.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18608" target="_blank">📅 19:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18607">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18607" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18606">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دود غلیظ پس از برخورد موشک های ایران به جایی در کویت</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18606" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18605">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18605" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18604">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18604" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18603">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok_7S7ViC0d_Y5RCG9Sf6gIP6Q1k4YIpqWC8AnOnDKJBjQKefgAj5L5AVCrijidtzlF10Gq8HR8Jc2hrCr-4nBQnLzRcLF-CdKvn_Q_SxFZ8CS_71xNgeR39DLmEiuJptJoEPCRYv5XYPPxLKyx39QfaeIWzjYjuXuyJHAe6qRnhWuhPSbRrevSgIZ6NIjhm0KMTz3Gi9lc1MMhPTMUdearq1Lo3IQwAXQPFwV2S7E_U_Yt4xA5Z8DR45ONImkQiaBBjCsu_B6_bv9y4WFjpMZB8H-GnarmjJQ_F9vWNGfHAT0HXQwV_ncCR9-Y0UDQ9q0iJnV4eGh4ZaoBEphN16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18603" target="_blank">📅 19:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18602">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18602" target="_blank">📅 19:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18601">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.
به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18601" target="_blank">📅 19:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18600">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.
همین</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18600" target="_blank">📅 19:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKqFYKiBCnogo9KVocR_0sG7Jm_Td-nSLc1VFpfboLKBhzaoG85Z80QUEsQAJdX52W6ntu-m5jGS289wy9M-y7GNs3lLE68t9nX8DtiBMwuGUlZ0nEcgj56TEvMzgVBW5EMCuQ1fwQbr0skNBczSAxovRMJuKa-sBxSXKGbwcYgGlERTw6Nt4Wal1r0pQ9pUDpEcWrQ5unAGAORt_nZ_H9r_BGEdUvAel_I_5Ooca0bWOwwqxxcrBVjkwtBQhUfNNvK8QHzRZDj01EkyHD9pvHuQz-Vaj8j-WwJ0athB04YKyiqaQf4WDMQe8QosRrxLc6KazVxJc9q_GzziOYz12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18599" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18598">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18598" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ :  آنها (ایرانی ها) دیروز با توافقی موافقت کردند که از نظر ما کاملاً ایده‌ آل بود،دیگر هیچ برنامه هسته‌ ایی در کار نبود و از همه‌ چیز دست کشیدند  اما پس از آن، اتاق مذاکره را ترک کردند و کمتر از یک ساعت بعد، یک پهپاد به سمت یک کشتی شلیک کردند</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18597" target="_blank">📅 17:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرنگار: تنگه هرمز باز است یا بسته؟  ترامپ: «تنگه هرمز باز است و من نمی‌خواهم در مورد آن صحبت کنم چون می‌خواهم به یاد لیندسی گراهام باشم.  قبل از تماس تلفنی به شما گفتم.»</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18596" target="_blank">📅 17:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18595" target="_blank">📅 17:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18594" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZpzq95mwc_Ggo5qXJbqUQqvVvqX1OpnAqro9YXf1QA-rKugnoHVG_Dq7SvWUsf3xvZAfwjh-6KwjTMZ2oR7e9IZNvR5dqhInpAMR7mqSHOH57v1sVMy4Cy1HzBJA1J9-t5jT30eFa7asGgwi2e45u-QBGlkFjmSnVouG1x9MtQvQbLEdlV5UHCka9i0WgzgfmvcxwaXiYDu1BKXJKUW71_F-CBvIcodjTbmvJegcYlRVFv2l7SS40EhFq8Gq2MLSN277ueBB8ptCHyURrY88cVd-kkqy2egfZAmvOPsn5tpKqt6jjl1L3bE5bvX_fZzJiJH3TEHomE6_mtWeo0YJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18593" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان یک آبراه بین‌المللی باقی می‌ماند. نیروهای ایالات متحده مستقر و آماده هستند تا اطمینان حاصل کنند که این وضعیت حفظ شود.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18592" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">توانیر: کاهش ظرفیت شبکه برق به دلیل آسیب‌های گسترده‌ در جنگ
‌
مدیرعامل شرکت توانیر:
حدود ۴۲۰۰ مگاوات از توان شبکه برق کشور کاهش یافته و بیش از ۲ هزار نقطه از شبکه دچار آسیب شده‌اند.
با وجود فشار مضاعف گرمای تابستان بر شبکه، عبور کم‌چالش از روزهای پیش‌رو در گرو همراهی مردم است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18591" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJRCEN6Bwd_9Ugm-uP2y6ImCPE7hhTkNBURSVckFXpVlaQbWuZg5biLNx-mqvl7jLyvPyuN4md_vmh0_JD1LJ9xfVwxhgA-Fh5uA7W0CSVOkGmmvP2xjHDnyaavsLeMHR4tjZVK_5d6K7ZbCvU3An22KDtPX46DIoRElIE_G_jfKFXXv7nrcAlQhJHoVjiXa02D3iMer1a6gzfEPI5Yr0gNaWItPSVCMT4yXdFPi9oL91sCtQRdDVCgMxNwGOo8KFuZcnttZMAkJS9QrGZRNUjHxRl0BYGfbZZ6PW31VKY42CA6VHwQpfhLJr_rbIx5xz1wfPqwZrjYCdEnkSMfqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان:   ما از ایران درخواست می کنیم به ارزش های اخلاقی و فرهنگی که دو کشور را به هم وصل می کنند، احترام بگذارند</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18590" target="_blank">📅 16:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18589" target="_blank">📅 16:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18588" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18587" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تنها راه نابودی اسراییل این است که با آنها رابطه سیاسی برقرار کنیم و بعد عباس آقا را بگذاریم سفیر دایمی مان در اورشلیم !</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18586" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18585" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18584" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18583">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یک شهروند هندی پس از حمله ایران به یک کشتی تجاری در نزدیکی سواحل عمان گم شده است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18583" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18582">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">من که قانع شدم.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18582" target="_blank">📅 15:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18581">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عزت‌الله ضرغامی:   علت مرگ لیندسی گراهام دیدن تشییع جنازه میلیونی  امام خامنه‌ای بوده.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18581" target="_blank">📅 15:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18580">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18580" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قول میدهم هر ۱۸ نفری که گم شده اند هندی بوده اند</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18579" target="_blank">📅 15:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18578">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق گزارش‌های دولت منطقه‌ای که به رسانه (SCMP) استناد شده است، دو خلبان نظامی چینی، از جمله یک فرمانده تاکتیکی ارشد، ماه گذشته در حین تمرین‌های پروازی خط مقدم کشته شدند.
پکن که به ندرت تلفات نظامی را به‌طور عمومی افشا می‌کند، علت مرگ این دو خلبان را اعلام نکرده است و هنوز مشخص نیست که آیا این دو خلبان در یک حادثه کشته شده‌اند یا خیر.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18578" target="_blank">📅 14:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18577">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=p9ztJ-b1ZSzgPUH6NHoWtnUvKqidPak8uJWBzT3omQHB3xVw2dFYcwfzu6pg7KjiCNkOgHhi9MsqbiwDhJ6_2M4zC0DO2L9M8BxEFGDsB--_HVbwOXlKV-t_goiGrtMPoB8o5IDCgGW8KQDb4NspA2FNuWkEqNZLxHkBOmlIQJebuSIaqTvx4pW9bf8cjyKhhPLjJnRcWU2HYcyGJgG6nsvCHZZJ53PuzTOVqsQQgOVELe8yyUA9rMiJVegYGssL0u_50SqZEukzoZljZY-q7hMteZ0rx8uPWzYizEqM2y13YIHCtk73RAVMRle-toVhiWM6pYklixQJtt-_5UcHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=p9ztJ-b1ZSzgPUH6NHoWtnUvKqidPak8uJWBzT3omQHB3xVw2dFYcwfzu6pg7KjiCNkOgHhi9MsqbiwDhJ6_2M4zC0DO2L9M8BxEFGDsB--_HVbwOXlKV-t_goiGrtMPoB8o5IDCgGW8KQDb4NspA2FNuWkEqNZLxHkBOmlIQJebuSIaqTvx4pW9bf8cjyKhhPLjJnRcWU2HYcyGJgG6nsvCHZZJ53PuzTOVqsQQgOVELe8yyUA9rMiJVegYGssL0u_50SqZEukzoZljZY-q7hMteZ0rx8uPWzYizEqM2y13YIHCtk73RAVMRle-toVhiWM6pYklixQJtt-_5UcHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر جام جهانی در ایران برگزار می شد!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/18577" target="_blank">📅 14:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18576">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLOOGjZY8yl2tleTFszx7j_QA739fu0KM0riI0Xb-UyDlCfVBM3VpWnYY93hSG1_GG6IqaGqS4q_yMRsvc3wontfV_WPNiYIRjMZubb3dxmEvwGYkyhNkZhqaIO8bDLO81r60fbS-490vD8Q5UEeLucHVC4JkbCN_HmteTIlG9p9AjGdESz79WETZZsH-2yyOHzMCvuOqa9Lde5pjpKF2YN33-E9fgEpZIVONYhoUhi8ztGYwkwKQUYOPUreS89Y5Pk2OhOhuEm32I8u6DUaVfDQnput9_LKJ-kUfaDw8yOugzLxHY8L6p0RDqLJmp6VRoTNboBioP2MXUcB30whPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18576" target="_blank">📅 13:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18575">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18575" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18573">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو ممکن است برای شرکت در مراسم خاکسپاری سناتور گراهام به ایالات متحده سفر کند، جایی که احتمال دارد با ترامپ دیدار کند.
منبع: i24</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18573" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18572">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گراهام همین چند روز پیش در اوکراین بوده؛ جایی که اصلاً بعید نیست هنوز عوامل اطلاعاتی روسها در آن حضور داشته باشند.
مسمومیت با پولونیوم-۲۱۰
(در موارد شدید) معمولاً طی روزها تا هفته‌ها پیشرفت می‌کند. ممکن است فرد دچار ضعف شدید، تهوع و استفراغ، اسهال، آسیب مغز استخوان، ریزش مو و در نهایت نارسایی چند اندام شود. این روند می‌تواند طولانی و بسیار رنج‌آور باشد.
مسمومیت با عوامل عصبی مانند نوویچوک
معمولاً بسیار سریع‌تر پیشرفت می‌کند. علائم می‌تواند شامل انقباض شدید عضلات، ترشحات فراوان، تنگی نفس، تشنج و اختلال هوشیاری باشد. بدون درمان فوری، وضعیت می‌تواند در مدت کوتاهی بحرانی شود. فرد لزوماً مدت طولانی هوشیار نمی‌ماند و ممکن است به سرعت دچار کاهش سطح هوشیاری شود.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/18572" target="_blank">📅 11:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پسکوف سخنگوی کاخ کرملین هشدار داد که در صورت تهدید موجودیت دولت روسیه، از سلاح‌های هسته‌ای استفاده خواهد شد.</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/18571" target="_blank">📅 11:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18570">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملات ایران به کشورهای جنوب خلیج فارس ادامه دارد.
امارات هم هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18570" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18569">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
نحوه عجیب اعلام خبر فوت لیندسی گراهام  توسط گوینده شبکه خبر :
🔹
«به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✍🏻
CAPITANO
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18569" target="_blank">📅 11:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18568">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080aef9062.mp4?token=gLA1fvFw2xVGqc39XGi5Q-K4WW3MVdahe4HnqDt0InCYQ3MNuJJsG8UgoeFSsnO5tRdyxLto_qiPJ02KsSQugmbiv_2JTpJHqOORSOvvr6Q5Omv_PjNybzFEr78LQ-Edt1uYr7-l7Wp-veiRSssg8Od8KRjyla-XceAxGq5CzKzgKvLTEcW3KnAq4iPEujsclOI5CUt62bOjRN7Q4iTvZN-a6qdNerVNMSDqJlQQsa72KmcIHZgr2NfQZ-l7emRbmZiVfHeR3oHljMYY97OQN_cwRHv0vDX1WtKSvL91hkTaEWvjQ57wWMWnCzDBcAFIHI3Nj8FNKcSZEKxIR3ZXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080aef9062.mp4?token=gLA1fvFw2xVGqc39XGi5Q-K4WW3MVdahe4HnqDt0InCYQ3MNuJJsG8UgoeFSsnO5tRdyxLto_qiPJ02KsSQugmbiv_2JTpJHqOORSOvvr6Q5Omv_PjNybzFEr78LQ-Edt1uYr7-l7Wp-veiRSssg8Od8KRjyla-XceAxGq5CzKzgKvLTEcW3KnAq4iPEujsclOI5CUt62bOjRN7Q4iTvZN-a6qdNerVNMSDqJlQQsa72KmcIHZgr2NfQZ-l7emRbmZiVfHeR3oHljMYY97OQN_cwRHv0vDX1WtKSvL91hkTaEWvjQ57wWMWnCzDBcAFIHI3Nj8FNKcSZEKxIR3ZXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نحوه عجیب اعلام خبر فوت لیندسی گراهام  توسط گوینده شبکه خبر :
🔹
«به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✍🏻
CAPITANO
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18568" target="_blank">📅 11:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18567">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ:
سناتور لیندزی گراهام، یکی از بزرگترین افراد و سناتورانی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود. به شدت دلتنگ لیندزی خواهیم شد!!! جزئیات و مراسم به دنبال خواهد آمد. بسیار غم‌انگیز! رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18567" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایران بزرگترین حمله خود را از زمان آتش‌بس در سراسر خلیج فارس آغاز کرد و موشک‌های بالستیک و پهپادها را به سمت دارایی‌های نظامی ایالات متحده و تأسیسات لجستیکی شلیک کرد.
اهداف گزارش‌شده شامل پایگاه هوایی العودید (قطر)، پایگاه هوایی پرنس حسن (اردن)، ستاد ناوگان پنجم ایالات متحده (بحرین)، پایگاه هوایی الظفره (امارات متحده عربی)، سایت‌های نظامی ایالات متحده در کویت و مرکز لجستیک نیروی دریایی ایالات متحده در بندر دقم (عمان) بود که ادعاهای اضافی مبنی بر حمله به کشتی‌ها در تنگه هرمز نیز مطرح شده است.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18566" target="_blank">📅 09:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18565">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لیندزی گراهام، سناتور جمهوریخواه آمریکا، درگذشت!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/18565" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMdY5ThMvc8SB0AN9S95s3it0dqaTqPjIOj6M7DgRboFCgvurQmDEGTFucLhxfvchutsG0WuROiSzRlErgMwU3vA6ZX0OmjIGhKl5CVD8M7X2i1cVlOhCeeC79nKh2d6lhMLN6FZoNIE7xm0sqVKLCUl-GgotGepPUXMqfU7A4JXOGeEgusnyuSLd-LTViri0kZV6A3FXIaHKH0Wjq-M1H7IAiarjF-aqeZaWuy28ILzefqK3mdq0tST6LmCqbsl7xFr0YCceCpag0KSxiChZfv7lIYIYJ2QiIr8pveW4KqU4HnzKNfjppPkpv5GvdY1VRHjACX1-rPWc0d4ZRL8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعییی
شب خوش</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18564" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
