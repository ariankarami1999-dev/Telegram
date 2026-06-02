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
<img src="https://cdn4.telesco.pe/file/uLkXeXO4RWujorMk8WxK6RAuuFB7teL52l-z4S4JD70tXtO41_xd1fFgLYf0P7Q5essV7eR4mmYMg9wqga4wuu90tgzvDbxD0_K8BPNIviaJQCip1CfzO7mk3U2HK-I0rAAQ-cvqjoEMIAFAT3WBaCpb-VT-y9IVrEyquCKn7Uha03O5QQYryQOREF8BoAE_3hDUr4UD6ybkCHkum7HDDq3AvcsxwUarblzh4uwAKcIAi12HeeBdg-VeaWRY9oA0rjYhr-9Vof78RCrtkxujEoOItk1tGPTzr4WughFpOc9Y6uoaBrdX5g6a-3hQ-BlcRnDXALqvibERuOrZKvsLhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 53K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTeacher</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE7Yqswfyh8o7IY8hflWjn_PQRQ2wWraiQLU92UMgWQLFs5ZcZyM4BuetUossIcbMqUwhg4TpiDntzx3OCWJG3UkR07-aRHyXVzVWCc21vLbu-ap7aZMq4FqnZYuFhp2LOyk5pgxCKsNMjHuEc9SlJnkQnY4VCNU4zMILX8woLyqGvHqDjwiBuKiCDy5Sw3US25rw0iKwEc5E-MdmqRpu45aRMwtFG3dRDKSvdHmLo2doM6S57oXpHINuVtrHRRbDwWPiMwzgkY5rqsu0jJ-_1oF_XFMdEiYIXvucjth4OBZv2etH_N8yA_8KNbr5ip6NTLI8X2gcZOYGw-hBL2PLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍💻
اکثر برنامه‌نویس‌ها دانش فنی فوق العاده ای دارن اما مشکلشون انگلیسیه!
🚫
چون نمیتونن:
▫️
توی میتینگ راحت صحبت کنن
◾️
داکیومنت‌ها رو سریع بخونن
▫️
توی مصاحبه خارجی خوب عمل کنن
◾️
یا با تیم بین‌المللی ارتباط بگیرن
برای همین کانال «لرنوبیت» رو ساختیم؛
آموزش انگلیسی مخصوص برنامه‌نویس‌ها و بچه‌های تکنولوژی
👇
🔹
اصطلاحات واقعی دنیای برنامه‌نویسی
🔹
مکالمه کاری و میتینگ
🔹
داکیومنت و کامنت‌نویسی
🔹
آمادگی مصاحبه و کار ریموت
Debug your English. Upgrade your career
🚀
🆔
@learnobit
🆔
@learnobit
🆔
@learnobit</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2649" target="_blank">📅 21:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDPwDzwDKNmxE-skCwO55vs64twvutK_hQbBSGxq6KrDLAPX5B1HskDCQ6aYFKQAt6DBWJsdCcTN1YCiO0mVQu2EM4Z3f_Bj_tbHqOACkGHSELYIEY1rEV14OEMwSJ0hgnSn0j8fZu63Q9lPutttER46I9PizjL4NCVWuBgKEDtG6FliVvdRKW74KY6JDbuSPL1hptoBdWI44oKs_d65sTuNCB5rNSroW1vKtY21pyOPtSDtNkLBtZbXk5ZZmvO6_V6-Xn8JfYonk6p1Ss22MYaYlDmUoAH_89E94Twt2DO3MKtmLUldwSvrr-qjhbPsG9yGAP7FOwfVI-C6M7LiEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی GenyConnect؛ جایگزین مدرن v2rayN برای مدیریت پروکسی
نرم‌افزار GenyConnect یک کلاینت تونلینگ و VPN مدرن (با کاربردی شبیه به برنامه محبوب v2rayN) است که با تمرکز بر عملکرد بالا، حریم خصوصی و کنترل دقیق ترافیک طراحی شده است. ویژگی مهم این ابزار، وابسته‌نبودن به یک پروتکل خاص است؛ به این معنی که می‌تواند به عنوان یک بستر یکپارچه برای موتورهای مختلف تونلینگ عمل کند.
🔹
مسیریابی پیشرفته:
امکان تعیین مسیر ترافیک بر اساس لیست سفید، دامنه‌های خاص، و حتی مسیریابی در سطح اپلیکیشن‌ها و پروسه‌های سیستم.
🔸
سبک و شفاف:
این ابزار با کمترین مصرف منابع سخت‌افزاری کار می‌کند و اطلاعات کاملی از وضعیت شبکه، لاگ‌های زنده و آمارهای لحظه‌ای ترافیک را به شما نمایش می‌دهد.
🔹
انعطاف در پلتفرم‌ها:
برخلاف برخی کلاینت‌ها که فقط مختص یک سیستم‌عامل هستند، این برنامه به صورت یکپارچه برای
ویندوز، مک، لینوکس و اندروید
در دسترس است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2648" target="_blank">📅 21:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOfLF0v88Eq-LPpMlzIFOlokGhG9M--NsOCRmDNbUGXfECqQ8SBT9aSHip5O4dMYaKRCg4dDwKQFMjwWkZh8fVF_qWlMHMNfB_LS6FDWPgp_zfBm11UTyONC4YwQRKfX0BKCQ0nTRvatvhz6dm22Ut8PotfCNfmUsPT93hfWlQJ6Z0ew6YAaeWwSrSHwE1Dx2oO_WqM4g8TyLS7D2RLvi9Fmmyiqyq58AdZEziB-d0LQZZKbYI27GsEKHvgE3yUnZsOIOswFQrBg9x3pBxtHH-mPZY3nEiG6XGqM5K7X8UkkyKjO_ZEn5eQ7X1B42qzGGkzf49R-5ZkqLdmUZE5SLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تون‌کوین به (Gram) تغییر نام می‌دهد!
پاول دورف در کانال رسمی خود خبر بسیار مهمی برای کاربران و سرمایه‌گذاران شبکه TON اعلام کرد. بر اساس این اطلاعیه، ارز دیجیتال بومی این شبکه قرار است با یک ری‌برندینگ بزرگ، نام فعلی خود را کنار گذاشته و به نام اصلی و اولیه‌اش یعنی Gram تغییر کند.
نکات کلیدی که دورف در این پست به آن‌ها اشاره کرده است:
🔹
بازگشت به ایده اولیه:
دورف یادآوری کرده که Gram نام اصلی ارز شبکه در اولین وایت‌پیپر این پروژه بود. او این اتفاق را بازگشت به ریشه‌ها و شروع یک فصل جدید توصیف کرده است.
🔸
زمان‌بندی انتقال:
فرایند این تغییر نام و انتقال، حدود ۳ هفته زمان خواهد برد.
🔹
نام بلاک‌چین تغییر نمی‌کند:
با وجود تغییر نام ارز بومی (از Toncoin به Gram)، نام خود شبکه بلاک‌چین همچنان TON باقی خواهد ماند.
🔸
قدم چهارم از یک نقشه راه:
این ری‌برندینگ تنها یک تغییر اسم ساده نیست، بلکه به گفته دورف، راه را برای اتفاقات مهم بعدی هموار می‌کند و قدم چهارم از یک برنامه ۷ مرحله‌ای برای «عظمت دوباره بخشیدن به TON» است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2647" target="_blank">📅 21:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIb620C_mJPsKZWbYCupPY3vmNJikFUUYbGiElFSoGZtvEDu-2WrHEY2EzcptpLW0DGBxgyfNfw8va0rYT45s0uRakg7-btsotNM7i_98Ynarrpf7iPAQUfRhyhsxvvpEh9eRnobcK_VT75q_J8k3CsCgPtl7L2943Zsnc1UUv4yJAPlqzaoUaogC5OXCa1glAqMHS0X0jMvO3YvUGGhpaNLuO4SXHuLDl7juIWLPZuNA2fiKIN-RpPUJNaPoIhaEoAwVg0Pb3X_XXdhLPAqo216vbZ6PLgnpRkXqhQqjl3zTwxgxbZyp4W7O7S2gqnZsxKkQ95V6bA77ILmiD-aEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اسکنر IP سفید کلودفلر با نوا رادار
🔹
نوا رادار یک
اسکنر IP دسکتاپ
است که با Wails v3 (بک‌اند گو + فرانت ری‌اکت/تایپ‌اسکریپت) ساخته شده. این برنامه رنج‌های IP کلودفلر را از منابع متعدد اسکن می‌کند، تأیید پروتکل واقعی (TCP + TLS handshake) انجام می‌دهد و IPهای سالم را مرتب‌شده بر اساس سرعت تحویل می‌دهد.
—
اسکن چندمنبعی
— ۹ منبع IP قابل انتخاب
—
تأیید دو مرحله‌ای
— اسکن سریع TCP → تست عمیق TLS
— مرتب‌سازی بر اساس سرعت
— قابلیت انتخاب پورت
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/iaghapour/2646" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IP List -- @iAghapour.zip</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/iaghapour/2644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
آی‌پی ها و فایل html مربوط به ویدیو
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/iaghapour/2644" target="_blank">📅 20:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYjKXc05SXkq7ebfsGabTPqk7Emq5mzHyGvhPujEBf8z0F7zIrWcJA3myvJKl05LRkXUqJfy33kwsb1vsPJfbj0MpRpwjhpdXK-YWmqY-e7KjqQawR4bB2aqQREseUwTrNNYdidOQhk6fXMNs3rnH7W7Pt3EwdncHzN6g193pTSGXyc7E34YVYNd9A7T-_AbApLj9l1kAA0uhMVHrfQUf5_rJs4D2N6AuR35nCCb34RvEAW1nJuWV7oN0_GvzSpgTrKGKXbMTnTWE-kmuDHt816bf-ozLTDPC-A4kHOyD7Ndvm5zD0oSs4yI_Y4IRaLCTxWgjwEgHa7tKwC9Zb3YNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر (تست شده)
🔹
در این ویدیو به صورت قدم‌به‌قدم بهتون آموزش دادم که چطور با استفاده از Cloudflare Workers یک فیلترشکن کاملاً رایگان، و پرسرعت برای خودتون بسازید. این روش کاملاً تست شده و می‌تونید به راحتی روی گوشی و کامپیوتر ازش استفاده کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#رایگان
#پروکسی
#نوا
#novaproxy
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/iaghapour/2643" target="_blank">📅 19:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tffRvpP34OBDuAndqW8SHSEhlh4-sIhIrOnbQ5Qi18_xGmHTUYkCss61_j7niCi6kgYx3_OLASKHRkrdbe0B_6Ug9qzmyUt8yRHOzGrYqnl-DEH0QWFy1tyHHdXzgKVP68KrcihGXjBkQ4hIbun5drAu0WP4p6PdySofGZoACaPHkf2I_9c6MGwAURO30tbLzsCTzWv-GlzW5parnlbKOI20W7yqEI5zx6RFoiCxT4CrO80SNrWgw63l3ItebMXpp86Ydg0OQJUtGMa4iAUgiBqrVNE6ygWksufhfoleYgw0cm2sSldDDhVtxhMV74GAZF3UUoM8JbyhIz__TDGarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ ویندوز ۱۱ منتشر شد؛ پرسرعت‌تر و هوشمندتر!
مایکروسافت به‌تازگی آپدیت جدید ویندوز ۱۱ (نسخه‌های ۲۴H۲ و ۲۵H۲) را با تمرکز بر افزایش سرعت و هوش مصنوعی منتشر کرد.
مهم‌ترین تغییرات این به‌روزرسانی:
🔹
اشتراک‌گذاری صدا:
امکان اتصال هم‌زمان دو هدفون بلوتوثی مجزا به یک سیستم برای تماشای فیلم یا گوش دادن به موسیقی.
🔸
دوربین مشترک:
دسترسی هم‌زمان چند نرم‌افزار به وب‌کم بدون مسدود شدن تصویر.
🔹
افزایش سرعت و جستجو:
ارتقای چشمگیر سرعت منوی استارت و اجرای برنامه‌ها، به همراه امکان پیدا کردن سریع فایل‌ها با جستجوی تنها دو حرف.
🔸
پایش هوش مصنوعی و باتری:
نمایش دقیق میزان مصرف پردازنده عصبی (NPU) در تسک‌منیجر و بهینه‌سازی مصرف انرژی لپ‌تاپ‌ها در حالت استندبای.
این آپدیت با رفع خطاهای ناگهانی و بهبود سیستم امنیتی Windows Hello، تجربه بسیار روان‌تری ارائه می‌دهد و در ژوئن ۲۰۲۶ به‌صورت خودکار برای همه کاربران فعال خواهد شد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/iaghapour/2642" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/iaghapour/2640" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4C6gOs_HcowsGdkkNb9FuvHBl_o1o7iNnUezZVCHnSG2KDFU3hfE17paBXrPe3wBA474eiIiqAjCisyDaFtHfO8AHfflpjCXhPeqeQKZAxTLoo2kJrINyIvxrhJBCuYpnkDNfPuB8ZonrDUUu_S7BU8FYWRwnX6H14YvZB0DH_YaFBV3EngNu96sMfenDWQ3uV9M1CBCj33La_iVLNeLGKqMW0IAp23ZpAD-X_jrauWBgT8_7HjJ-825an1AuyqjAuhS77OE6tV0NCqE_g0073n1_9povZoKOOoCLE7aXXxnXP_URFDroTx6Rnaa4LJTnbd8uKAHZuNfxJVZkJF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران در حال برگشتن به تلگرام
😀</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/iaghapour/2639" target="_blank">📅 20:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💢
وضعیت اینترنت جوری شده که وقتی نت ملی بود فیلترشکن ها راحت تر متصل میشدن!
راستی گوگل پلی و اپ‌استور در دسترس قرار گرفتن و البته ویندوز آپدیت و...</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/iaghapour/2638" target="_blank">📅 20:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/iaghapour/2637" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2636">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
بچه ها میگن انقدر پهنای باند دیتاسنتر ها پایین هستش که اکثر روش های تانل که اجرا میکنن سرعت بدی داره یا دچار قطع و وصلی و اختلال زیاد هستش.
خیلی به روش تانل بستگی نداره بیشتر مشکل پهنای باند ضعیف دیتاسنتر ها مربوط هست.
امیدوارم در روزهای آینده وضعیت بهتر بشه.</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/iaghapour/2636" target="_blank">📅 13:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">میبینم که رو فیلترشکن ها تخفیف زدن :)
هر گیگ رو 10 و 20 هزار تومن دارن میفروشن :)
پولی که بعضی از افراد به جیب زدن تاجر ها نزدن. طرف داخل سرور ایران سایت فروش فیلترشکن داشت! قعطی نداشت. بالای 10 هزار ممبر داشت. اوایل حتی درگاه ریالی داشت. بعد بعضی ها انتظار دارن ما باور کنیم اینا به جایی وصل نبودن!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/iaghapour/2634" target="_blank">📅 21:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
چند خبر کوتاه از رسانه ها
🔸
معاون وزیر ارتباطات در پاسخ به زومیت در خصوص زمان بازگشایی اینترنت سیار نیز گفت: «امروز اینترنت همراه نیز وصل خواهد شد.»
با توجه به این اظهارنظر باید منتظر بازگشایی اینترنت همراه تا پایان امروز، سه‌شنبه ۵ خردادماه، در دسترس کاربران قرار بگیرد. هم‌چنین، طبق اعلام‌های قبلی، تا فردا روند بازگشایی اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴ تکمیل خواهد شد.
🔹
نت‌بلاکس بازگشت بخشی از اینترنت ایران را تایید کرد؛ سطح اتصال به ۳۴ درصد رسید
🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/iaghapour/2633" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/iaghapour/2632" target="_blank">📅 18:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینترنت بین‌الملل وصل بشه یجوری از اینترنت استفاده میکنم اختلال بخوره دوباره قطع بشه.
🫠
گوشی باید آپدیت بشه.
ویندوز باید آپدیت بشه.
لینوکس باید آپدیت بشه.
برنامه ها باید آپدیت بشه.
و...
حس میکنم شما هم با من هم نظر هستید
🫣
😁</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/iaghapour/2631" target="_blank">📅 10:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
این روزا انقدر شایعه و خبر بی‌خود درباره وصل شدن اینترنت پیچیده که واقعاً حس و حال خبر زدن در موردش رو ندارم.
با این حال، سعی می‌کنم اسکریپت‌هایی که زحمت کشیدید فرستادید رو حتماً بررسی کنم، به هر حال از دست رو دست گذاشتن که بهتره. راستش با این وضع زندگی، اصلاً هیچ انرژی و انگیزه‌ای برای آدم باقی نمونده.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/iaghapour/2630" target="_blank">📅 21:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzHNsrBEFHXCKq9o5ofWblx3RWG66g1tvcfiOoEOcRLdT1O2fzwwJKceH4N4d9Zro8kob9H4lmianOrHnRf6e1PI8t9VLSvzKJ2OC5Dxl-4Q0VaxmsYEWAfy2IJmCqDh7f2izkdvjTQl-L7_L8ibuXdZfBzBwCF7o4Zv4cW1TGkoTmOokcCw9X_swCWiaRySJB5pVlWfxWmOLM3bfHxh9n6QWXQg_Ff-T1P07fvlF9qEg9mk6_Ly507maxvUAvrBfu3Fq5tvnFujFAmj4yvWMVp5xXFenwa47XxO86u9-XgUnOEDxNd-tkGBozLLf5iXv7iRa1_KFLpD5_NXpWJzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت جدید کلاینت اندروید GooseRelayVPN
🔹
این مخزن، کلاینت اندروید GooseRelayVPN است که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد.
🛠
پایداری و رفع کرش
‏
🌐
رفع کامل لو رفتن آی‌پی (IPv6 Leak) با موتور جدید tun2socks gVisor FakeDNS.
‏
🎛
پیاده‌سازی کامل Quick Settings Tile.
‏
📊
نمایش کاملاً دقیق سرعت و حجم مصرفی.
‏
🗂
اضافه شدن حالت Bypass به بخش Split-Tunneling.
‏
❄️
رفع فریز شدن برنامه در پس‌زمینه.
‏
📜
اصلاح پرش ناگهانی اسکرول لاگ‌ها و بازطراحی کارت وضعیت اتصال در صفحه Home
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/iaghapour/2628" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
رکورددار تاریکی دیجیتال: ایران طولانی‌ترین قطعی اینترنت جهان را تجربه می‌کند!
روزنامه معتبر اسپانیایی «ال‌پایس» در گزارشی تکان‌دهنده اعلام کرده است که ایران با گذشت حدود ۸۰ روز خاموشی دیجیتال، رکورد طولانی‌ترین قطعی سراسری اینترنت در تاریخ یک جامعه دیجیتال را به نام خود ثبت کرده است. این محدودیت‌ها که ابتدا با توجیه شرایط امنیتی و جنگی آغاز شد، همچنان ادامه دارد.
طبق گزارش این رسانه و به نقل از نت‌بلاکس، این وضعیت حالا حتی از قطعی طولانی‌مدت اینترنت میانمار در سال ۲۰۲۱ نیز فراتر رفته و زندگی میلیون‌ها ایرانی را در بن‌بست قرار داده است:
🔹
آوارگی برای یک اتصال پایدار:
ال‌پایس داستان تلخ افرادی را روایت می‌کند که برای حفظ شغل خود مجبور به مهاجرت موقت شده‌اند. مانند معلم زبانی که برای رهایی از اضطراب قطعی اینترنت، با هزینه ۴۰۰ دلار در ماه به زیرزمینی تاریک در ارمنستان پناه برده است.
🔸
ضربه مهلک به کسب‌وکارهای زنان:
تداوم این اختلالات، آسیب‌های ویرانگری به مشاغل کوچک وارد کرده است؛ به‌ویژه کسب‌وکارهایی که توسط زنان اداره می‌شوند و حیات آن‌ها کاملاً به پلتفرم‌های آنلاین و شبکه‌های اجتماعی گره خورده بود.
🔹
فلج شدن زندگی روزمره:
از کار از راه دور و تبادلات مالی گرفته تا ساده‌ترین ارتباطات انسانی و دسترسی به اطلاعات، همگی تحت تأثیر این محدودیت‌های بی‌سابقه مختل شده‌اند.
گزارش این روزنامه نشان می‌دهد که جهان در حال تماشای انزوای دیجیتال جامعه‌ای است که شهروندانش برای دسترسی به ابتدایی‌ترین حق ارتباطی خود، ناچارند هزینه‌های سنگین روانی، مالی و حتی مهاجرتی بپردازند./ دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/iaghapour/2627" target="_blank">📅 16:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocjf5gRZcEEz0tBl76wQMoMoS6asLTcGPwxa-S070ULd5F0rY_jXI6snsgDHzuZ4grORVtHdfUGMhgNa-ogck0pgdkh135MI6YgfVen8wu3yj9tim-hc-ivJSsL1PWV99uSzPxI1NdSKdhcDuf0aILJLPAW91icfX7nNlidznjUt4RnA0ajBwxv2uplZbYZANEMacmv-Rhs9Eg90eVPXv0aOO9jpAhZppZHYmcbpO2iWowJ74PLMGgENoMfTkJZN5Qle3E6NWZvniTjzD9aN0KvvSAfqmEwnagnNRlh1_A12nwxsHloAtCNPUhSHzh9kdMn3Xp3b5PLHZL002Hylzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پروژه XPlex؛ راه‌حل هوشمندانه برای جلوگیری از قطعی و پکت‌لاس کانفیگ
اگر از کانفیگ‌های v2ray استفاده می‌کنید و پایداری اینترنت در کارهای حساسی مثل آزمون‌های آنلاین، جلسات ویدیویی یا ریموت‌ورک برای شما حیاتی است، پروژه جدید XPlex یک راه‌حل فنی و کاربردی برای شما دارد.
منطق این اسکریپت ساده اما بسیار کارآمد است و به شما کمک می‌کند تا یک اتصال بدون قطعی را تجربه کنید:
🔹
استفاده هم‌زمان از چند کانفیگ:
منطق کلیدی این پروژه این است که اگر چند کانفیگ v2ray داشته باشید، اسکریپت به صورت هم‌زمان از آن‌ها استفاده می‌کند و ترافیک شما را روی کانفیگی می‌اندازد که کمترین پینگ ممکن را دارد.
🔸
خداحافظی با پکت‌لاس و تایم‌اوت:
این ابزار برای افرادی که کارهای حساسی دارند و ثانیه‌ها برایشان مهم است طراحی شده؛ مثل شرکت‌کنندگان در آزمون‌های آیلتس آنلاین، جلسات کاری با خارج از کشور و...
🔹
هزینه مصرف حجم:
باید توجه داشته باشید که به دلیل ماهیت کارکرد این ابزار، مصرف ترافیک و حجم v2ray شما تقریباً دو برابر خواهد شد که بهای به دست آوردن یک اینترنت کاملاً پایدار است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/iaghapour/2625" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭕️
نماینده مجلس: ۹۰ درصد مردم با قطعی اینترنت مشکلی ندارند!
علی یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس صراحتاً اعلام کرد که اینترنت جهانی فعلاً بازگشایی نخواهد شد و مسئولان به این نتیجه رسیده‌اند که اتصال مجدد آن به صلاح نیست. او مدعی شده که با پلتفرم‌های داخلی، احتیاجات اکثریت جامعه برآورده شده است!
این اظهارات نشان‌دهنده اصرار بر ادامه سیاست اینترنت طبقاتی و نادیده گرفتن نارضایتی‌های عمومی است:
🔹
انکار نارضایتی‌ها:
این نماینده مدعی است به عنوان نماینده مردم، مراجعات مکرری برای اعتراض به قطع اینترنت نداشته و ۹۰ درصد مردم هیچ مشکل عمده‌ای با این وضعیت ندارند!
🔸
رسمیت یافتن اینترنت پرو:
به گفته او، تا کنون به بالغ بر یک میلیون نفر از افرادِ واجد صلاحیت (مثل تجار و دانشگاهیان) دسترسی به «اینترنت پرو» داده شده و هر قشری که نیاز داشته باشد هم می‌تواند آن را پیگیری کند.
🔹
کوچ اجباری به پلتفرم‌های داخلی:
او مدعی شد که ترافیک شبکه‌ها نشان می‌دهد بیشتر کسب‌وکارها به پلتفرم‌هایی مثل روبیکا و سروش کوچ کرده‌اند و تنها یک «اقلیت ناچیز» باقی مانده‌اند که آن‌ها هم بستر مشخصی برای پیگیری دارند.
در حالی که مسئولان از پایداری وضعیت فعلی و رضایت مردم سخن می‌گویند، بخش بزرگی از جامعه، کسب‌وکارها و متخصصان، اینترنت طبقاتی و محدودیت‌های فراگیر را تلاشی برای حذف کامل دسترسی آزاد به دنیای دیجیتال می‌دانند. / زومیت
پ.ن: اینا نماینده کدوم مردم هستن؟ 90 درصد مشکل ندارن؟ عجب!
حالا فارق از اینکه این ادعا از اول تا آخر دروغ هستش ولی من قبلا هم خواهش کردم اگه مجبور نیستید وارد شبکه های داخلی نشید! اگه مجبور نیستید لطفا سیم‌کارت پرو نخرید! اینا واقعا فکر میکنن مردم به ایتا و بله علاقه دارن! متوجه نیستن خیلی ها به اجبار مهاجرت کردن! در غیر اینصورت کی این اپلیکیشن ها رو به تلگرام و اینستا ترجیح میده؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/iaghapour/2623" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
دوستان عزیزی که درخواست معرفی افراد معتبر برای خرید فیلترشکن دارید؛ طبق بررسی و نظرسنجی که در
این پست
قرار دادیم، با چندین نفری که از سال‌های قبل همکاری داشتیم صحبت کردیم و ازشون یکسری درخواست‌ها داشتیم؛ از جمله ضمانت بازگشت پول و اینکه مبلغی رو به عنوان ضمانت پیش ما بگذارند.
به همین دلیل ۹۰ درصدشون قبول نکردن و فقط تعداد محدودی پذیرفتن که هفته پیش یکی از اون‌ها رو بهتون معرفی کردیم. بازم اگه کسی از افراد قدیمی شرایط ما رو قبول کنه حتماً معرفی می‌کنیم.
افرادی که به ما تبلیغ می‌دن می‌دونن چقدر تو تبلیغات سخت‌گیر هستیم حالا در هر موضوعی باشه. بیش از ۳۰ درصد کسانی که پیام می‌دن، چون کانال قدیمی یا کاربر زیادی ندارن یا سایت معتبری ندارن، با نهایت احترام تبلیغشون رو اصلاً قبول نمی‌کنیم.
🔹
با این حال بازم سعی می‌کنیم همین یکی دو تا فردی که می‌شناسیم و شرایطمون رو قبول کردن بهتون معرفی کنیم؛ البته اگه خودشون دوباره قبول کنن تبلیغ بدن :)
ممنون میشم افراد جدید برای تبلیغات در زمینه فیلترشکن فعلاً پیام ندن. شرایط رو کامل در
این پست
براشون توضیح دادیم.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/iaghapour/2622" target="_blank">📅 21:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭕️
اعتراف رسمی دولت: ۷۰ درصد مطالبات مردم، رفع محدودیت‌های اینترنت است
معاون اجرایی رئیس‌جمهور صراحتاً اعلام کرد که طبق نظرسنجی‌های نهاد ریاست‌جمهوری، بیش از ۷۰ درصد گلایه‌ها و خواسته‌های مردم به محدودیت‌های اینترنت مربوط می‌شود. او تأکید کرد که سیاست پایدار کشور نباید بر مبنای فیلترینگ باشد.
نکات کلیدی سخنان معاون رئیس‌جمهور درباره وضعیت اینترنت:
🔹
تصمیمات اضطراری باید تمام شوند:
محدودیت‌های اخیر به دلیل شرایط خاص امنیتی و جنگی بوده، اما تصمیمات دوران اضطرار نباید دائمی شوند و سیاست پایدار کشور نمی‌تواند بر محدودسازی بنا شود.
🔸
اعتراف به شکست فیلترینگ:
تجربه عملی نشان داد محدودیت‌های فراگیر ارتباطی به نتایج مورد انتظار منجر نشده و استفاده گسترده از فیلترشکن‌ها اثربخشی این محدودیت‌ها را از بین برده است.
🔹
حق آگاهی مردم:
اعتماد عمومی مهم‌ترین سرمایه است و مردم حق دارند بدانند محدودیت‌ها بر چه مبنایی اعمال می‌شود، چه دامنه‌ای دارد و تا چه زمانی ادامه خواهد داشت.
به گفته قائم‌پناه، کشور به یک تفاهم ملی در حوزه ارتباطات نیاز دارد؛ چرا که آینده ایران متصل و فناورانه است و دسترسی پایدار به اینترنت، پیش‌شرط تحقق این آینده خواهد بود./ زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/iaghapour/2621" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpdTSQvJ8DYMtP-RzpkPRNY3FhpP9Y8WbD4tqhbIrF5XfMNRsXhhheKOfal9mVmX_-OXqZRDjVlBWlmzXYZwetQw-KM-FmI_tIrDKOJh-1fQxNCUJIisyQ9CiLaLHaRKiBBJuOf7pzx6CIN85hctDpp3rFeqLfHxuJNWR5qL2Jzmdqjb3zr3CaUwm2NSgs-lak-qaU1g-WAw8QhI8VGiXkVAi76Say_BmL9-NE8r_Jiqo4lByRB-ys86nS9y8FUg7aPiSxY_X0w_IT50xdMCo4pP5Rs8V1Cf1uu3ZOsL4gDkkXz0zru_bYXfQSa2OJ-ti7yCPaquttVWtHoylX7W7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
بحران خاموشی دیجیتال؛ ضربه‌ای جبران‌ناپذیر بر پیکر اقتصاد و جامعه
🔻
بیش از ۱۹۴۴ ساعت خاموشی دیجیتال، تنها قطع یک ابزار ارتباطی روزمره نیست، بلکه یک «بحران تمام‌عیار اقتصادی و اجتماعی» است. در زمانه‌ای که در سراسر جهان حتی چند دقیقه اختلال در اینترنت زیان‌های هنگفتی به بار می‌آورد، تداوم ۸۲ روزه این وضعیت در ایران، آسیبی عمیق به شریان‌های حیاتی کسب‌وکارها و زندگی عادی مردم وارد کرده است.
در واقع، تداوم این قطعی طولانی‌مدت نشان می‌دهد که حفظ حیات اقتصادی مشاغلِ وابسته به فضای مجازی و نیازهای ارتباطی جامعه، در اولویت تصمیم‌گیری‌ها قرار ندارد؛ رویکردی که پیامدی جز نابودی معیشت هزاران نفر، فرسایش سرمایه اجتماعی و آسیب جدی به بدنه نوپای اقتصاد دیجیتال کشور نخواهد داشت.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/iaghapour/2620" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0EbZtyBLhnTPuZ9AXYDefq3P-H9ifE2jyjDCv13moevdiR6qDqrPYVclQHqqsaeAy0Mg7SvMRaWDbFIrQKZQPIOFdHadomhdcwh_TFklobBzlu60lLOo3HrgdL-1M_TUW4h8LYaTKp__mH6X31n2tj4ecR4cF4jrln-NAthQHKj8BlySuexSlm-Td1G1H6PRBCGFPuvXWNLQ-huu2cWMmAdGL--L8-8Uyx4t4BhSvuteREaNdy5dQ4_DCm8os_4Oh2cu3skwPu44YwKqmZckuweQtWIf040O_03w-VLImoBUlaBUTq84OS4dXrV43DmYrnmAF74_RCEV9OOF0c-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شگفتی گوگل در Google I/O 2026؛ معرفی جمینای ۳.۵ فلش با سرعتی باورنکردنی!
در گام نخست، مدل جمینای ۳.۵ فلش عرضه شده است؛ مدلی که با وجود طراحی شدن برای سرعت بالا و هزینه کم، در کمال شگفتی توانسته مدل‌های پرچمدار و پرو نسل‌های قبل را در بنچمارک‌های تخصصی شکست دهد.
🔹
پادشاهی در بخش ایجنت‌ها:
این مدل با توانایی برنامه‌ریزی بالا، می‌تواند چندین ایجنت را به صورت موازی برای پیشبرد پروژه‌های پیچیده و کدنویسی مستقر کند.
🔸
سرعت خیره‌کننده و کاهش هزینه‌ها:
ساندار پیچای اعلام کرد این مدل با سرعت پردازش ۲۸۹ توکن در ثانیه، حدود ۴ برابر سریع‌تر از رقباست.
🔹
شکست رقبای سرسخت:
جمینای ۳.۵ فلش در آزمون‌های تخصصیِ مربوط به کارهای ایجنتی، امتیاز بی‌نظیر ۱۶۵۶ را کسب کرده و عملاً رقیب سرسختی مثل کلود سونیت ۴.۶ آنتروپیک را پشت سر گذاشته است.
🔸
همچنین نسخه قدرتمندتر یعنی جمینای ۳.۵ پرو در ماه ژوئن ۲۰۲۶ رسماً عرضه خواهد شد.
جمینای ۳.۵ فلش هم‌اکنون به عنوان مدل پیش‌فرض در اپلیکیشن جمینای و بخش سرچ گوگل فعال شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/iaghapour/2619" target="_blank">📅 09:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWVO6H732CMCNSZAPq1DXrppcXCmILr6IZ-36LWUYqha02nG_PtYGPfl1DLJBD4oGvvbpjvMLDsiS5x00Pj57DaEBpTX0uXxk8f545akQrcMLQZRIIprmdp9dHpLpnkpRwy3zjXabO2SmHRfXg6QrmrJ5nKavc2ItkszHNvIpmhI72M8HZvsIAXFT1LEy7_xSEXwZEWYqT76oZrL8xn7Pv-Y8HP_4G-hPQLIrO5mGj3RM1jrvCB1nyJgNOciU8tL5KqLHD7yBagGfGU7f4EWB2I4b11Rm0vcCcMBUs_coUx3cQky-htXsMZ83BI-ehogDkyV49N9YTHia6ABlMrwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دیگه پول فیلترشکن نده! آموزش ساخت فیلترشکن شخصی و رایگان با سرعت بالا
😎
🔹
در این آموزش قدم‌به‌قدم بهت یاد می‌دم که چطور بدون نیاز به دانش خاصی، یک فیلترشکن (VPN) شخصی، امن و کاملاً رایگان برای خودت بسازی. این روش روی تمام اینترنت‌ها جواب می‌ده و سرعت خوبی برای تماشای یوتیوب، وب‌گردی و … داره.
🔗
تماشا ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#رایگان
#novaproxy
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/iaghapour/2618" target="_blank">📅 16:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">از هر 10 نفری که که تو اینستاگرام وصل هستن 8 تاش دختره, 2 تاش هم پسر کانفیگ فروش
🥸</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/iaghapour/2617" target="_blank">📅 17:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHySNvDwxaU_vq5rRugLkHQ_a-_FfBjObwGELD93AmZJ1feehD0yRgsdu_2AsVnExzWFpWHGuvZyuC-_OsCJcbIcTSp4hx1zmUK-swoNBpGYtnJgFpABlpOnPdgFdURjFZ25tLEDAdkF18MswgkPDq_PC5YzVXUmz9laIn16q1X1nzUW59CnE1LjIPOyDPG82s9rQJbKj8DaYsJ80OPV5YxRrAMCsalaa_I__syfp90N_tIswm9OVwtXXOyriCCJDCKrw2atXW79cugacr49O8BHeWGRPDM3UqgV8hcVDN98ZXNSbYaH1kQ7KGOEDfVK_CxfB6pYCdh9tlLYeyyklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش نصب ساده و آفلاین 3X-UI روی سرور ایران + SSL (+ معرفی قابلیت های جدید)
🔹
در این ویدیو به سراغ یکی از بزرگترین چالش‌های این روزها رفتیم: نصب پنل 3X-UI روی سرورهای ایران همراه با سرتیفیکیت به صورت کاملاً آفلاین و بدون نیاز به اینترنت آزاد! همینطور سعی کردیم یک معرفی ساده از قابلیت های جدید این پنل داشته باشیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#پنل
#xui
#3xui
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/iaghapour/2615" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕️
بحران در زیرساخت فناوری؛ سقوط درآمدها و خطر عقب‌ماندگی ۱۰ ساله!
اختلالات اینترنتی دیگر فقط یک مشکل ساده برای کاربران عادی نیست؛ بلکه به گفته رئیس کمیسیون شبکه سازمان نصر، تیشه به ریشه‌ی زیرساخت‌های فناوری کشور زده است. این وضعیت نه تنها درآمد شرکت‌ها را تا ۷۰ درصد کاهش داده، بلکه باعث فرار متخصصان کلیدی و فرسودگی شدید تجهیزات شده است.
🔹
سقوط درآمد و انفجار هزینه‌ها: شرکت‌های حوزه شبکه با کاهش درآمد ۳۰ تا ۷۰ درصدی روبرو هستند. از سوی دیگر، به دلیل اختلال در مسیریابی و افت کیفیت، این شرکت‌ها مجبور به پرداخت جریمه‌های سنگین ناشی از نقض توافق‌نامه سطح خدمات (SLA) شده‌اند.
🔸
تهدید امنیت سایبری: محدودیت دسترسی به مخازن اصلی و سرورهای به‌روزرسانی جهانی، ریسک نفوذ و حملات سایبری را تا ۴۰ درصد افزایش داده است. در واقع، امنیت سایبری قربانی ناپایداری شبکه شده است.
🔹
تخلیه ژنتیکی تخصص: صنعت شبکه با بحران خروج نیروهای کلیدی مواجه است. تربیت یک متخصص ارشد سال‌ها زمان و هزینه‌ی ارزی سنگین می‌طلبد که با مهاجرت این افراد، سرمایه‌های انسانی چند میلیاردی کشور به راحتی از دست می‌رود.
🔸
عقب‌ماندگی ۱۰ ساله: ادامه این وضعیت، ایران را با شکاف تکنولوژیک ۱۰ ساله نسبت به کشورهای منطقه مواجه می‌کند؛ شکافی که در فضای پرشتاب فناوری، جبران آن تقریباً غیرممکن خواهد بود.
زیرساخت شبکه کشور به جای اتصال طبیعی به اینترنت جهانی، در حال حرکت به سمت یک ساختار جزیره‌ای و فرسوده است. اگر ثبات پیش‌بینی‌پذیر به این فضا بازنگردد، شرکت‌های بزرگ فناوری به اپراتورهای ساده تجهیزات قدیمی تنزل پیدا خواهند کرد. / دیجیاتو
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/iaghapour/2614" target="_blank">📅 10:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTQ0deSKt2ZK1qLQaFlb_6k3u6cku-kEggP-gndMHMCucifOdXTlenHgm8S6ffR2AunGlSyGq0G2sjkKEabjWVVd4kUpClyF5VpF3qEcbAX88rtelWwV1vJ-UPfLwN7zBfyc3mX44HSjGezEAVjpD5gJMW9QlPSaReWRra-0lCKu-4g3aC8k7FryVD5ooMap8aTLysL4CYyNYJp4XmdFUYjGITL7qxmc4QLlJz2yoa24VOAM3qCQ3vsRiA0n92ES6_QORu9wOGfaT4U1RtBP_7cYnWpNI5u5u7RK8r4bDVEEiQJfeU5nrlcZLSE2OobUY36fKyjke7bL3gXmO5F5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
حرف‌زدن درباره‌ی قطعی
#اینترنت
شاید فوری اینترنت را برنگرداند؛ اما
#سکوت
دقیقاً همان چیزی است که ادامه‌ی این وضعیت به آن نیاز دارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/iaghapour/2613" target="_blank">📅 22:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/iaghapour/2612" target="_blank">📅 17:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/iaghapour/2609" target="_blank">📅 19:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
سوپراپلیکیشن ایتا اعلام کرد امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است!
کاش تلگرام بیاد از شما یاد بگیره :)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/iaghapour/2608" target="_blank">📅 12:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✍🏻
دوستان عزیز، همون‌طور که احتمالاً متوجه شدید، در یک هفته گذشته به دلایل مختلفی فعالیت ما کمتر شده.
🔹
در این مدت پیام‌های زیادی داشتیم که درخواست آموزش «روش جدید سنایی» رو داشتن. وقتی بررسی کردیم، متوجه شدیم خود ایشون زحمت تهیه ویدیوی آموزشی رو کشیدن؛ بنابراین نیازی به آموزش مجدد  نبود.
🔸
برای اطمینان بیشتر، این آموزش رو به چند نفر از دوستان دادیم تا تست کنن. بیشتر افراد موفق به اجرا نشدن، اما یکی از کاربران تونست متصل بشه. طبق بررسی‌های ایشون، این روش به‌شدت به رنج آی‌پی‌ها (هم سرور ایران و هم خارج) وابسته است. مشکل اصلی اینجاست که بعد از اتصال و مصرف حجم کمی از اینترنت، ارتباط قطع می‌شه و باید آی‌پی رو عوض کرد؛ هرچند آی‌پی قبلی بعد از ۱ تا ۲ ساعت دوباره قابل استفاده می‌شه.
🔻
متأسفانه در این بین، عده‌ای بدون این‌که تست درستی از پایداری تانل بگیرن، شروع به آموزش کردن که نتیجه‌اش فقط ضرر مالی برای کاربران بوده. چون کاربرا رفتن سرورهای گرون قیمت رو خریداری کردن که البته تعداد این افراد اصلا کم نبوده. (نمونه‌اش رو در عکس ضمیمه می‌بینید).
🟢
در مجموع، به نظر می‌رسه این روش هنوز پایدار نیست، اما از بچه‌های تیم خواستیم تست‌های بیشتری روش انجام بدن. اگر خودتون هم مایلید آموزش رو ببینید، می‌تونید مستقیماً به کانال یا گروه سنایی مراجعه کنید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/iaghapour/2607" target="_blank">📅 22:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭕️
خلاصه اخبار چند روز گذشته
🔸
اینترنت بین‌الملل به گیمرها ارائه می‌شود؛
ثبت درخواست در سامانه همگرا (اینترنت طبقاتی)
🔹
دولت و مجلس به دنبال حمایت تازه از پیام‌رسان‌های داخلی (رانت و فساد جدید)
🔸
نماینده مردم تهران در مجلس:
درباره خسارت‌های قطعی اینترنت جوسازی می‌شود. (حرف بیخود)
🔹
معاون رئیس‌جمهور:
اینترنت بین‌الملل حتما وصل می‌شود؛ دولت قصد دائمی‌کردن محدودیت‌ها را ندارد. (حرف الکی)
🔸
برآورد انجمن بلاکچین: خسارت ۳۰۰ تا ۷۰۰ هزار میلیاردی از قطعی اینترنت.
🔹
معاون رئیس جمهور: محدودیت حجم و گرانی اینترنت پرو برای جلوگیری از استفاده غیرضروری است. (عجب بابا عجب)
🔸
قطع اینترنت به هفتاد و پنجمین روز خود رسید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/iaghapour/2606" target="_blank">📅 18:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-z2Mco3VGCbbKlCP1311Bs4jxVbUQusilc-XcLZ06V3Tr7t8qAhqirz1L5QyoduZaRhiqmnAK9Jmst4sMM3Y2UgndX29sUj9VBMV03_rmhxwibh7gVUSNqxGphdZlkvOAaulbCDTmhp5PuwrmpgTVZY0JBhbDPNWEkQ8vvWJhswNWbon9Svptxqup1UXQLCMLfjZXrx8ajlgWrSOZKBs-SmZx4QDFd3hW18MhnMj7R17nDEknDVBoIkenidHhcuBhKQ7vHzShQ9in9-kdGeWMQVhZpdfgjUD6ZI3U_XpoAGWBwI5y-yacNwnozA2monvk0djEGzB3b9nIwdUUBhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
با اپ TunnelX در ویندوز از قابلیت Split Tunneling استفاده کنید.
🔹
اپ TunnelX برای زمانی ساخته شده که کاربر نمی‌خواهد تمام ترافیک سیستم از وی‌پی‌ان عبور کند. با این برنامه می‌توان فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگر را وارد تونل کرد و بقیه ترافیک سیستم را روی اینترنت عادی نگه داشت. همچنین در صورت نیاز، حالت Full-route برای عبور کل سیستم از تونل در دسترس است.
🔗
دانلود اپ از گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/iaghapour/2605" target="_blank">📅 14:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✍
آدم راننده شوتی باشه به مراتب اضطرابش كمتر از کسیه كه شغلش تو ايران به اينترنت وابسته هستش...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/iaghapour/2603" target="_blank">📅 21:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2602">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
آپدیت بزرگ و انقلابی پنل 3x-ui (نسخه‌های 3.0.0 و 3.0.1)
بالاخره یکی از مهم‌ترین آپدیت‌های پنل محبوب 3x-ui منتشر شد! در این نسخه‌ها شاهد بازنویسی کامل رابط کاربری، اضافه شدن قابلیت‌های مدیریتی کلان و بهبودهای چشمگیر امنیتی هستیم.
🌐
۱. بازنویسی کامل و سریع‌تر شدن پنل (مهاجرت به Vue 3)
رابط کاربری از پایه بازنویسی شده است! این یعنی سرعت لود بسیار بالاتر، طراحی مدرن‌تر، صفحه لاگین جدید و بهبود چشمگیر تم دارک.
⚡️
۲. آمار زنده و در لحظه
: با جایگزینی سیستم قدیمی با
WebSocket
، از این پس تمام آمارهای داشبورد، مصرف حجم کلاینت‌ها و وضعیت سرور به صورت «زنده» آپدیت می‌شوند و دیگر نیازی به رفرش کردن صفحه نیست!
🌍
۳. مدیریت چند سروره (Multi-Node Deployment) -
🌟
ویژگی طلایی
یکی از مورد انتظارترین قابلیت‌ها اضافه شد! حالا می‌توانید از طریق یک پنل مرکزی (Manager)، کانفیگ‌ها و اینباندها را روی چندین سرور دیگر (Remote Nodes) مستقر و مدیریت کنید.
📱
۴. رابط کاربری کاملاً سازگار با موبایل
: داشبورد، لیست کلاینت‌ها و بخش لاگ‌ها حالا به صورت "کارتی" و کاملاً بهینه برای نمایشگرهای موبایل طراحی شده‌اند تا مدیریت پنل با گوشی بسیار راحت‌تر شود.
⚙️
۵. خداحافظی با کدهای JSON و تنظیمات آسان‌تر
فرم‌های ساخت کانفیگ (Inbounds) کاملاً ساختاریافته و گرافیکی شده‌اند. دیگر برای تنظیمات پایه نیازی به دستکاری JSON خام نیست (البته تب Advanced برای حرفه‌ای‌ها همچنان وجود دارد). همچنین مدیریت DNSها بسیار پیشرفته‌تر شده است.
👥
۶. مدیریت گروهی کلاینت‌ها (Bulk Actions)
امکان انتخاب گروهی  کلاینت‌ها برای حذف یا اعمال تغییرات اضافه شده که کار ادمین‌ها را بسیار راحت می‌کند.
🛠
۷. امکانات جدید Xray و Outboundها
اضافه شدن پروتکل Loopback، دکمه
Test All
برای تست همزمان همه Outboundها و ارائه گزارش دقیق از تایم‌اوت‌ها، و همچنین خاموش شدن امن هسته Xray.
🔒
۸. ارتقاء امنیت و نصب راحت‌تر
➖
اضافه شدن سیستم امنیتی CSRF Protection برای جلوگیری از حملات.
➖
اضافه شدن گزینه
skip-SSL
در اسکریپت نصب (بسیار کاربردی برای کسانی که از ریورس‌پروکسی یا تانل استفاده می‌کنند و نیازی به سرتیفیکیت روی خود سرور ندارند).
➖
اضافه شدن صفحه مستندات API (API Docs) در داخل خود پنل برای برنامه‌نویسان.
و بسیاری از تغییرات دیگه که میتونید در
این لینک
مطالعه کنید.
💡
نکته:
برای تجربه این تغییرات فوق‌العاده، پیشنهاد می‌شود هرچه سریع‌تر پنل خود را آپدیت کنید. (توصیه همیشگی: قبل از آپدیت بکاپ فراموش نشود!)
✍🏻
با تشکر از ثنایی عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/iaghapour/2602" target="_blank">📅 18:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
عصبانیت سخنگوی دولت از انتقاد خبرنگاران از قطع اینترنت
فاطمه مهاجرانی در نشست خبری امروز خود به اعتراض خبرنگاران بابت ادامه قطعی اینترنت واکنش نشان داد.
سخنگوی دولت گفت: «در شرایطی که رئیس جمهور آمریکا اعلام می‌کند آتش بس به دستگاه تنفس مصنوعی وصل است، پاسخ شما چیست؟ کشور در جنگ است. بپذیریم که ویژگی جنگ، امنیت مردم است.»
✍🏻
پ.ن:  خانم مهاجرانی اگه دوباره عصبی نمیشید خواستم بگم کاش به فکر امنیت اقتصادی مردم هم بودید! کاش به فکر امنیت ذهنی و روانی مردم هم بودید! کاش یه فکری برای چند میلیون آدمی که با قطعی اینترنت بیکار و ناامید کردین هم بودید!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2601" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
نمیتونم خبر رو تایید کنم ولی میگن:
— افغانستان اینترنت 5G آورده.
— عراق تلگرام رو رفع فیلتر کرده.
— سوریه هم که ویزا و مستر کارت و...
این که ما درگیر فیلترینگ مسخره هستیم واقعا گریه داره...</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/iaghapour/2600" target="_blank">📅 09:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سلام خواستم یه نکته کوچولو بگم
فقط بحث کسب و کارهای کوچیک نبود
فقط بحث آنلاین شاپ ها نبود
ماهایی که ۴ سال تو دیجیتال مارکتینگ بودیم توی طراحی سایت و سئو و اتوماسیون کار میکردیم هم کاملا ورشکست شدیم
نه از ۹ اسفند
ما یه بار جنگ خرداد زمین خوردیم تا اومدیم بلند شیم از جامون و داشتیم اوکی میشدیم دلار دی ماه سر به فلک کشید و بعد یه قطعی دیگه داشتیم که خیلی ها بهانه کردن و پول ندادن آخر دی ما هیچی پروژه نداشتیم حتی بهترین کارفرماها اومدن گفتن کار شما خیلی خوبه ولی ما واقعا پول پرسنل رو هم به زور میدیم نمیرسه به سئو
بهمن اومدیم خودمون رو جمع کنیم تیر آخر رو اول اسفند بهمون زدن
دفترمون رو تحویل دادیم
نیروهامونو از بهمن تعدیل کرده بودیم
و الان چه جوون ها و چه پدرانی که بیکار شدن
منی که تمام تخصصم همیناست
یک متخصص بیکار محسوب میشم.
©️
پیام ارسالی از کاربر shafikhany</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/iaghapour/2599" target="_blank">📅 01:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✍
حدودا 500 پیام بررسی نشده از 2 روز پیش داریم که پشتیبانی تا فردا همه رو بررسی میکنه.
جدا از بحث بالا، از ته دل آرزو میکنم تو این روزهای عجیب و غریبی که داریم می‌گذرونیم، حال دلتون خوب باشه. می‌بینیم و حس میکنم که زندگی چقدر برای خیلی‌ها سخت شده و دغدغه‌ها چقدر زیادن.
امیدواریم هرچه زودتر این روزهای سخت جاشون رو به روزهای روشن‌تری بدن. هوای خودتون و دلتون رو داشته باشید.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/iaghapour/2598" target="_blank">📅 03:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYJXTcX10e_Q389iDthVarZwU5d2Ap4N6FwLdXJL0WDpdXsKuK77NmFTMhbVmVZyxxps1fdXWncP0Z_7gtkPzuar53kqFtbRyGxoiwXPq5Dn81v2Wb1wcQN8zbQ4yJgy7dluXDgYj5yGMwGoAkrcgPr3-nhAfyAC1CHCZyCC5By2Ql-qulaMhsqSn6GIrGQY9zMdGFHCx6mXyzFST9Upx-EomAeEBcNVB38cJ7U6X7Vy8HbghM-k_7TFmXavIHYdZgSZweILhAbXas8a-BxvLvbF19dn0XKsVjhNI8gsiwvwwASdndi53lh4j5RflweeWJalMCl5AzT05To19KZwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت ورژن 0.10.0 سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور ایران خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
توی آپدیت جدید سانگبرد با فعال کردن قابلیت Remote channel، میتونید پست هایی که تو یک چنل تلگرام ارسال میشه رو، به یک چنل توی سرور سانگبرد خودتون استریم کنید.
-
📡
قابلیت Remote channel
-
🔗
ساده سازی سیستم Invite link
-
🎨
بازطراحی بخش ساخت/تغییر کانال و گروه در UI
-
✨
انیمیشن build-up پیام ها در چت ها
-
🔔
بهبود عملکرد push notifications
- تغییرات گرافیکی اسکریپت نصب آسان
-
🐳
پشتیانی از TLS با سرتیفیکیت self-signed در Docker
-
🔧
رفع باگ های گزارش شده
-
📄
اضافه شدن نسخه فارسی فایل readme
🔘
اگه به هر مشکلی خوردین، حتما تو گیت هاب یک issue باز کنید و گزارش بدید.
⭐️
اگه از پروژه راضی بودین، با ستاره دادن تو گیت هاب از پروژه حمایت کنید.
🔹
چنل پروژه
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/iaghapour/2597" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
ساده‌ترین راه برای دور زدن فیلترینگ با تانل DNS
اگه خانواده‌ شما هم داخل ایران برای اتصال به اینترنت مشکل دارند، این پیام ممکن است به شما کمک کند.
این برنامه یک برنامه‌ی  گرافیکیست که کار با آن بسیار ساده است و برای اتصال به اینترنت هر دو روش MasterDNS و VayDNS را پشتیبانی می‌کند.
👈
لینک گیت‌هاب
👈
دانلود
اپ
📖
آموزش کامل MasterDNS و VayDNS
▶️
آموزش روی یوتیوب
📱
آموزش KevinNet DNS
▶️
آموزش روی یوتیوب
🔄
آپدیت‌های جدید برنامه
در صورت وجود هرگونه مشکل یا سوالات مرتبط با KevinNetDNS میتوانید با آدرس ایمیل زیر در تماس باشید:
©️
متن تهیه شده توسط نویسنده اسکریپت KevinDNS
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/iaghapour/2596" target="_blank">📅 23:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭕️
ادعای عجیب نماینده مجلس: با ۴ هزار میلیارد تومان ایتا را به سطح واتس‌اپ می‌رسانیم!
رئیس کمیته ICT مجلس در اظهارنظری جنجالی مدعی شده است که فاصله میان پیام‌رسان‌های داخلی مثل ایتا با نمونه‌های جهانی مانند واتس‌اپ، تنها در کمبود بودجه برای خرید سرور خلاصه می‌شود. به گفته او، ارتقای این پلتفرم‌ها هزینه چندانی برای کشور ندارد.
این نماینده مجلس معتقد است که پلتفرم‌های داخلی از نظر فنی کمبودی ندارند و تنها زیرساخت‌های سخت‌افزاری آن‌ها باید تقویت شود:
🔹
بودجه برای رقابت:
مصطفی طاهری مدعی است با صرف ۳ تا ۴ هزار میلیارد تومان برای خرید سرور، می‌توان کیفیت ایتا را به سطح واتس‌اپ رساند تا توانایی پذیرش بدون مشکل بیش از ۲۰ میلیون کاربر را داشته باشد.
🔸
هشدار درباره جاسوسی سخت‌افزاری:
این مقام مسئول همچنین به موضوع استفاده از بیگ‌دیتا (داده‌های بزرگ) اشاره کرده و مدعی شده که آمریکا قوانینی برای جاسوسی در لایه‌های سخت‌افزاری و تراشه‌ها (حتی پایین‌تر از سطح سیستم‌عامل) دارد.
این اظهارات در حالی مطرح می‌شود که کارشناسان حوزه تکنولوژی، موفقیت پلتفرم‌های جهانی را فراتر از صرفا تعداد سرور می‌دانند و مواردی چون امنیت، پروتکل‌های رمزنگاری، حریم خصوصی و نوآوری‌های مداوم نرم‌افزاری را از عوامل اصلی برتری آن‌ها به حساب می‌آورند.
یکی از کاربرا زیر همین پست در دیجیاتو کامنت جالبی گذاشته بود:
مامان‌بزرگ منم با چند میلیارد نیکی میناژ میشه!
پ.ن: حالا فارق از این حرفا داره میگه اینا دارن از کاربراشون جاسوسی میکنن برای همین ما باید اپ های خودمون رو داشته باشیم... من حرفی ندارم.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/iaghapour/2595" target="_blank">📅 18:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-GfCOlNFG-0wJGVq4SnlPARysm_mgMFtCmiePAFW2X_xvCJ03JiTlzOaTH4KcTnSLDZX3uPp4gpa6RLdOsaxp4E_Zc2cdNVXySsxSLG4AhouVfwIOG6sjkbd_C4E9n3jPvEr6MGj2Xih71U1qE_zVreGk7tT_OpNP4f7yLic0E9UnX-aa3c2O-XMeyQQIJFPBHAN-uLCLedFml1eaSVUr1yQH2IFiOMdCp3i6kYctFxwqSN8Yo6E2aAU0urx1xnMpIG-HEossvz3fJsjxH84MNx03RGeRcIs6CtuBgpazPY7k6MgzLTz-gEdbDSkY5qQAJXVOuoywNTIxlUtcI9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ایران 11 هفته در خاموشی دیجیتال!
هیچ‌وقت تو زندگیم فکر نمی‌کردم یه روزی برسه که این‌جوری تلخ، شاهد از بین رفتن زحمت‌ آدما باشم. ۱۱ هفته قطعی اینترنت واسه خیلی‌ها فقط یه اختلال ساده نبود؛ قصه پدر مادرا و جووناییه که با هزار امید یه کسب‌وکار کوچیک راه انداخته بودن تا خرج زندگیشونو دربیارن و الان دستشون به هیچ‌جا بند نیست.
تا همین چند وقت پیش با کلی استرس می‌گفتیم کسب‌وکارهای نوپا و خونگی تو «مرز نابودی» هستن و همه‌مون چشم‌انتظار بودیم زودتر اینترنت وصل بشه؛ ولی الان دیگه حرف از مرز نیست. خیلی‌ها کل سرمایه، جوونی و حاصل سال‌ها تلاششون جلوی چشماشون دود شد و رفت رو هوا. کاش دردی که افتاده رو دوش این مردم، میافتاد رو دوش مسئولین...
🆔
@NetProPlus</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/iaghapour/2594" target="_blank">📅 11:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#فیلترینگ
به ما تحمیل شد,
ولی
#اینترنت_طبقاتی
رو شما باید درخواست بدی تا بهت بدن...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/iaghapour/2592" target="_blank">📅 18:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxmBQMSF8Lefg9SLC0D-p9uNnUoA3etvCPOpZiwntOYvQ3Xp_zQq-ZQLxxs_6zxzZacJXfWIVp4IQdxYCTtubPGedNpA6DFPQzewg_z1gGWtUdHGT7uUorVDLdThzLuWWL6H6ESEjMRKabCTMGlE-KcWGhrwuChmKr2AUXhDG9cPhRaOa6GaAjeUhYSkglZ-8L0sBUeywn2ze8OlNkgcRmzTbEoYM3x_kI0gZmRHM4UX_6E9zQdtltCV3O3IFXXje9cGgBb_Oa5US2zthmHRSTnGyIoorJMQASQtSNmnOs6tZ0nrCJ2wgU8GQfNITj0pLSnpEaf_YfEujLD2FBmJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ تلگرام: ورود دستیار هوشمند به پروفایل شخصی!
تلگرام در آپدیت جدید تمرکز ویژه‌ای روی هوش مصنوعی داشته است. در ادامه مهم‌ترین تغییرات این نسخه را مرور می‌کنیم:
🔹
ربات‌های مهمان:
فراخوانی ربات‌ها در هر چت یا گروهی، تنها با تگ کردن آیدی و بدون نیاز به افزودن آن‌ها.
🔸
منشی شخصی هوشمند:
قابلیت اتصال مستقیم یک ربات به پروفایل شخصی تا در غیاب شما به پیام‌ها پاسخ دهد!
🔹
تعاملات زنده هوش مصنوعی:
تایپ و نمایش لحظه‌ای پاسخ ربات‌ها، به همراه قابلیت جدید ارتباط ربات با ربات برای انجام وظایف پیچیده‌تر.
🔸
امکانات جدید برای کانال‌ها و تولید محتوا:
قابلیت محدود کردن نظرسنجی‌ها (بر اساس کشور یا عضویت در کانال)، مشاهده نمودار آرا، و همچنین ساخت استایل‌های متنی سفارشی.
🔹
اضافه شدن قابلیت انتخاب فونت از سیستم خودتون (میتونید فونت وزیر رو نصب کنید و استفاده کنید).
با این به‌روزرسانی که شامل جستجوی هوشمند ایموجی‌ها، ارسال بی‌صدای پیام زمان‌بندی‌شده و رفع ۲۰۰ باگ فنی است، تلگرام قدم بزرگی برای ادغام کامل پیام‌رسانی انسان و هوش مصنوعی برداشته است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/iaghapour/2591" target="_blank">📅 14:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
مومن‌نسب: فضای مجازی به هیچ وجه نباید به حالت قبل برگردد
حالا این آدم انقدر مهم نیست که دربارش صحبت کنیم ولی خواستم بگم این همون آدمیه که چندسال پیش تو صداوسیما میگفت من خطرات اینترنت رو میدونم و اطلاع دارم یک نفر با 2 گیگ اینترنت حامله شده و پدر دختره با گریه اینو برای من تعریف می‌کرد...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/iaghapour/2590" target="_blank">📅 11:35 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
اطلاعیه مهم: معرفی فروشندگان کانفیگ
طبق نتایج
نظرسنجی اخیر،
قصد داریم فروشندگان قدیمی و معتبری که از قبل می‌شناسیم را یکی‌یکی برای خرید به شما معرفی کنیم.
📌
قوانین و شرایط مربوط به فروشندگان:
—
عدم پذیرش فروشنده جدید:
در حال حاضر شخص جدیدی معرفی نمی‌شود؛ بنابراین لطفاً در قسمت
«تماس با ما»
برای معرفی خود پیام ندهید. افرادی که معرفی می‌شوند، همگی پیش‌تر در کانال ما سابقه تبلیغ داشته‌اند.
—
تضمین خرید شما:
مبلغی از پول این افراد نزد ما به عنوان امانت می‌ماند تا در صورت بروز هرگونه مشکل، بتوانیم مطالبات شما کاربران عزیز را پیگیری کنیم.
—
ضمانت بازگشت وجه:
این فروشندگان موظف‌اند در صورت لزوم (بسته به شرایطی که خودشان به شما اعلام می‌کنند)، بین ۴۸ تا ۷۲ ساعت امکان عودت وجه را فراهم کنند.
—
قیمت منصفانه:
تمامی این افراد تعهد داده‌اند که نسبت به شرایط بازار، قیمت‌های منصفانه‌تری برای کاربران کانال ما در نظر بگیرند.
— معرفی فروشندگان صرفاً در زمینه
فروش کانفیگ
انجام می‌شود. هیچ‌یک از فروشندگان معرفی‌شده مجاز نیستند پس از معرفی، در کانال شخصی خود تبلیغات مربوط به "
اوتباند
" قرار دهند و یا به کاربران پیشنهاد خرید آن را بدهند.
⚠️
نکات مهم برای کاربران عزیز:
—
انتظارات از کیفیت:
کانفیگ‌ها باید بتوانند تلگرام، اینستاگرام و یوتیوب را به راحتی باز کنند. با توجه به شرایط فعلی اینترنت، داشتن سرعت‌های بسیار بالایِ گذشته کمی دور از انتظار است (هرچند ممکن است کیفیت سرویس‌ها عالی باشد)، پس لطفاً واقع‌بین باشید.
—
اختلال و پشتیبانی:
ممکن است در طول هفته، گاهی با اختلال مواجه شوید. پشتیبان‌ها موظف‌اند در سریع‌ترین زمان ممکن مشکل را حل کنند؛ اما لطفاً صبور باشید، حداقل یک ساعت به آن‌ها فرصت دهید و از ایجاد فشار زودهنگام به پشتیبانی کانال‌ها خودداری کنید.
— در ضمن، توجه داشته باشید که
ما ذی‌نفع این کانال‌ها نیستیم
و فقط به دلیل درخواست‌های زیاد شما این دوستان را معرفی می‌کنیم.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/iaghapour/2589" target="_blank">📅 23:36 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4e592IZocgifTW3kX4pPo-s8wCEn_nQ7ii0vTF0fHp0TioEQnkP6ULcNQ53Gm6_U2BoMT0CPYgBuAVpk4cYZO3Aav_xjol1BexA56EsLdm7GEaHIvKQdDFA0hkmINLyP1FemXSCagVzV2fel2GRAs3DeCPzvDb93hs2NQjOAKus9fCJphSlAClYDml_qo8H7eHGlRbmHq7m9WOjDmqSok7F-Vi_T-v6e10t4ckONDLN17a3DUenuZVlkix7K1V9d6toSrSumpnUNiGp-6pugmOhokzdif0TtTzK_1Zgw_jn-L2benwdioNO-3rULCK1C3wHKIAtmwiBNDk_SPrjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
سخنگو وزارت خارجه حذف تیک آبی خود در شبکه X را (سرکوب حقیقت) خواند.
68 روزه اینترنت مردم ایران رو قطع کردن، بعد یه تیک آبی‌شو گرفتن میگه حقیقت سرکوب شد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/iaghapour/2588" target="_blank">📅 20:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
تسنیم: درآمد طرح اینترنت «پرو» در سال به ۹۶ هزار میلیارد تومن می‌رسه!
🔹
خب با این رقم‌های نجومی و پول هنگفتی که درمیاد، معلومه که از این تبعیضی که راه انداختن حسابی راضی‌ان. وقتی محدودیت و فیلترینگ این‌قدر براشون سود داره، چرا نباید اینترنت داخلی و بسته رو بیشتر تحویل بگیرن؟
🔸
این وسط یه تشکر ویژه و خسته نباشید هم باید بگیم به اون دسته از دوستانی که رفتن تو صف اینترنت پرو و این سیستم طبقاتی رو خیلی راحت پذیرفتن. از رئیس فلان اتحادیه و مدیر فلان اداره بگیر تا نماینده صنف لاستیک‌فروش‌ها و یه سری کسب‌وکارهایی که واقعاً بدون اینترنت آزاد هم کارشون لنگ نمی‌موند. تو شرایطی که ۹۹ درصد مردم هیچ دسترسیِ عادی به اینترنت آزاد ندارن، مرسی از شماها که رفتین این اینترنت رو گرفتین و با این کارتون، قشنگ به این تبعیض و نابرابری رسمیت دادین!
پ.ن: البته به این نکته هم توجه کنید که خبرگذاری داخلی اینو گفته و ممکنه دقیقا مقصودشون از این حرف هم همین باشه که بگن چقدر این طرح خوب و سودآور هستش و...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/iaghapour/2587" target="_blank">📅 14:33 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭕️
وعده بازگشت به وضعیت عادی؛ توجیه محدودیت‌ها یا امید به بهبود اینترنت؟
معاون ارتباطات دفتر رئیس‌جمهور به تازگی اعلام کرده که وضعیت فعلی اینترنت مورد تایید دولت نیست و رئیس‌جمهور، محمدرضا عارف را مامور ساماندهی این شرایط کرده است. به گفته او، این محدودیت‌های شدید و قطعی‌ها صرفا تصمیماتی از سوی شورای عالی امنیت ملی و به دلیل شرایط خاص امنیتی و جنگی بوده‌اند.
🔹
وعده روزهای بهتر:
این مقام مسئول قول داده که با عبور از این شرایط ویژه، اینترنت نه تنها به حالت قبل برمی‌گردد، بلکه وضعیتی بهتر از گذشته پیدا خواهد کرد و وعده‌های انتخاباتی رئیس‌جمهور در این زمینه همچنان پیگیری می‌شوند.
🔸
دفاع از اینترنت پرو:
در واکنش به انتقادات، دولت ادعا می‌کند طرح «اینترنت پرو» صرفا برای نجات کسب‌وکارها در روزهای محدودیت ایجاد شده و نباید به آن برچسب اینترنت طبقاتی زد؛ چرا که به گفته آن‌ها، در شرایط عادی اصلا نیازی به چنین طرحی نخواهد بود.
🔹
کاهش محدودیت‌های عمومی:
خبر دیگر این است که قرار شده تدابیر جدیدی برای دسترسی بهتر سایر شهروندان به اینترنت اتخاذ شود تا فشار محدودیت‌های فعلی روی مردم کاهش یابد.
در حالی که دولت تلاش می‌کند قطعی‌ها و طرح‌های بحث‌برانگیزی مثل اینترنت پرو را صرفا به شرایط اضطراری گره بزند، کاربران و کسب‌وکارها همچنان منتظرند تا ببینند آیا این وعده‌ها در عمل به یک اینترنت آزاد و بدون محدودیت ختم می‌شود یا صرفا وعده‌ای برای کنترل نارضایتی‌های فعلی است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/iaghapour/2585" target="_blank">📅 21:12 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭕️
ایده عجیب در مجلس: تاسیس «اینستاگرام دولتی» و مدیریت کامل اینترنت!
نمایندگان مجلس در تازه‌ترین نشست خود با وزیر ارتباطات، از طرح‌ها و نگاه‌های جدیدی برای کنترل بیشتر فضای مجازی پرده برداشتند. در این جلسه، پیشنهاد ایجاد یک پلتفرم کاملا دولتی مشابه اینستاگرام مطرح شد تا به زعم آن‌ها، نیاز کشور برطرف شود.
🔹
اینستاگرام دولتی:
یکی از نمایندگان با اشاره به بازار سیاه و چند میلیونی فیلترشکن‌ها، رسما پیشنهاد ساخت یک سکوی دولتی شبیه اینستاگرام را برای پر کردن جای خالی این پلتفرم ارائه داده است.
🔸
رویای مدیریت اینترنت:
نایب رئیس مجلس تاکید کرده که مشکل آن‌ها اصل اینترنت نیست، بلکه می‌خواهند در صحنه بین‌المللی، مدیریت اینترنت کاملا در دست خودشان باشد و این فضا را به یک جبهه تقابل تشبیه کرده است.
🔹
فرصت‌سازی از بحران:
بخش قابل توجهی از صحبت‌های نمایندگان، حسرت خوردن برای از دست رفتن فرصت در شرایط ملتهب و جنگی است؛ آن‌ها معتقدند باید از این شرایط استفاده می‌کردند تا مردم و کسب‌وکارها به اجبار به سمت سکوهای داخلی کوچ کنند.
این صحبت‌ها به وضوح نشان می‌دهد که دغدغه اصلی، کاهش نارضایتی مردم از قیمت و کیفیت اینترنت نیست؛ بلکه تلاش برای بومی‌سازی اجباری، قطع ارتباط با شبکه‌های اجتماعی بین‌المللی و کشاندن کاربران به پلتفرم‌های تحت کنترل و نظارت است. / زومیت
✍🏻
پ.ن: از سوپر اپلیکیشن های ایتا و سروش و گپ و بله که از تلگرام کپی کردین مشخصه توانایی اینکار رو دارید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/iaghapour/2584" target="_blank">📅 19:36 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭕️
مرگ خاموش اقتصاد خرد: نابودی ۴۰ درصد از کسب‌وکارهای اینستاگرامی!
قطعی‌ها و محدودیت‌های اینترنتی فقط حق دسترسی آزاد ما به شبکه‌های اجتماعی را سلب نکرده، بلکه تیشه به ریشه‌ی اقتصاد خرد و معیشت مردم زده است. طبق اعلام پشوتن پورپزشک، عضو هیئت‌مدیره اتحادیه کسب‌وکارهای مجازی، فیلترینگ و اختلالات باعث نابودی بخش عظیمی از مشاغل آنلاین شده است.
🔹
فاجعه‌ی آماری: نزدیک به ۴۰ درصد از کسب‌وکارهای اینستاگرامی برای همیشه از بین رفته‌اند؛ این یعنی مرگ مستقیم بیش از ۴۰۰ هزار شغل!
🔸
دومینوی ویرانی: وقتی شوکی مثل محدودیت اینترنت وارد می‌شود، ابتدا کسب‌وکارهای کوچک و آسیب‌پذیر می‌میرند، اما این نابودی با کمی تاخیر گریبان شرکت‌های بزرگ اقتصادی را هم خواهد گرفت.
🔹
زنجیره‌ی به هم پیوسته: کسب‌وکارهای بزرگ در تولید، تامین و توزیع به شدت به همین کسب‌وکارهای خرد وابسته‌اند. توهم مصونیت برای شرکت‌های بزرگ، در نهایت منجر به فروپاشی خود آن‌ها می‌شود. منبع: زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/iaghapour/2583" target="_blank">📅 19:29 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اسم این زندگــــــی نبود
یک مبارزه تمام عیار بود...
#جوانی
#زندگی
#جنگ
#اینترنت</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/iaghapour/2581" target="_blank">📅 19:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭕️
حل مشکل دانلود از ریلیز گیت‌هاب با LatestReleaseMirror
اگر در دانلود فایل‌ها از بخش ریلیزهای (Releases) گیت‌هاب به دلیل محدودیت‌های اینترنت مشکل دارید، این اسکریپت کاربردی دقیقاً برای شما ساخته شده است!
ابزار
LatestReleaseMirror
به صورت خودکار فایل‌های آخرین آپدیتِ ریپازیتوری‌های دلخواه شما را دریافت کرده و آن‌ها را به عنوان فایل‌های عادی در ساختار پوشه‌های گیت‌هاب ذخیره می‌کند؛ در نتیجه می‌توانید آن‌ها را به راحتی و حتی با اینترنت داخلی دانلود کنید.
🔹
دریافت و آپدیت خودکار آخرین نسخه با استفاده از GitHub Actions.
🔸
امکان فیلتر کردن فایل‌های مورد نیاز (مثلاً فقط نسخه‌های ویندوز یا اندروید)
🔹
دسته‌بندی تمیز فایل‌های خروجی در مسیرهای مشخص.
🔗
لینک ریپازیتوری و راهنمای استفاده
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/iaghapour/2580" target="_blank">📅 16:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ركورد جديد سرعت اينترنت ژاپن:
با سرعت 1.02 پتابيت بر ثانيه، كل نتفليكس را در 1 ثانيه دانلود مى‌كند.
✍
ما هم اینجا باید با DNStt وصل بشیم تا بزور بتونیم فقط این خبر رو بخونیم...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/iaghapour/2579" target="_blank">📅 13:56 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
اسکریپت بهینه شده XHTTP Relay ECO برای Vercel Pro
🔹
نسخه ECO طوری تیون شده که علاوه بر امنیت سفت‌وسخت v1.3، کم‌هزینه‌ترین رفتار ممکن روی Vercel Pro رو داشته باشه؛ یعنی با کنترل هوشمند Timeout، Inflight، Throttle و Logها، مصرف منابع و هزینه نهایی تا جای ممکن پایین نگه داشته میشه.
🔸
فقط با GET، HEAD و POST کار می‌کنه تا امنیت بالاتر بره.
🔹
احراز هویت فقط از طریق هدر x-relay-key انجام میشه
🔸
هدرهای اضافی پلتفرم و hop-by-hop رو بی‌رحمانه فیلتر می‌کنیم.
🔹
روی آپلود و دانلود محدودیت سرعت (Throttling) واقعی گذاشتیم.
🔸
بردیمش روی Node runtime با لیمیت ۱۲۸ مگابایت رم و مدیریت کانکشن‌های همزمان.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/iaghapour/2578" target="_blank">📅 22:28 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
ورژن جدید کلاینت اندروید GooseRelayVPN منتشر شد
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
هسته پروژه به ورژن 1.5.0 آپدیت شد.
🔸
قابلیت fake dns اضافه شد.
🔹
باگ ها در این نسخه برطرف شدن.
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/iaghapour/2577" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esbw_qSrPII0CbJuAqul3MmK-d7H4Vkp-4oPspspABru_4bzcORev5bbiGRSWWFXbSzuPVuj8likuSKVanxhft0bYKHfR7nazZZ7ibxirUK6Tt-5Y9kdQN8GJFADW2lbh0YhJCQDlKlgRV5B_62IU-npUrS-ViSkrua0wIYzab7ToocYCbt-StNuHnqaBWXerwj82BtiCjL_Yqq9D0XzS2S0tIWv4tToPlphSpJhtnsYHeJSvE1UHuzbzQKulWCogL1FqMfMTXuAj-w4bx0UxFu_0z9MTxqrH0obB_G597VrquEx2IshsU70KA2nmbGdQ-WmjW9-EqGX8wZJtRflFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن رایگان و شخصی به 2 روش با نت ملی
🔹
با استفاده از دو ابزار قدرتمند MHRV و Nova-Proxy، دیگه نیازی به خرید کانفیگ‌ها و سرورهای گرون‌قیمت ندارید. تو این آموزش قدم‌به‌قدم به ۲ روش مختلف پیش میریم تا بتونید یه اتصال پایدار و بدون قطعی داشته باشید. حتماً تا آخر ویدیو همراه من باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔹
دانلود کلاینت ویندوز
🔸
دانلود کلاینت اندروید
#آموزش
#فیلترشکن
#mhrv
#novaproxy
#رایگان
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/iaghapour/2576" target="_blank">📅 19:53 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-SMrzaCYv-ozuxnyvabiz8luJF9_nIhHQjA_gAXZZfAPLg7JMnkM92T7dL0dZc51qaf9mpUH-Khk1ZvBfAjH_2hmqcS4l705Y5YWCweleKkUiFlMxlij5L20trxlNcYRQNelQ7HzDp8lPbjc8nEZr3eqTk8UhBocaXa_O4qLmiVJV8fs53ev1EIp6XouV4cV4aBPIzYoXNKGI03SffeHD8o7XnYNPgGIPDbPDlYhQoNJZHGgOEe4yO19-WZpuMFIl9KdWMbkZkocamULwkwJuDiyE--nWHcHVrsry2YeSrUw6V9LjdtMWV8TlLbQg9uxNl11pqYzEWTwBZCO3k8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پشت‌پرده‌ی «اینترنت پرو»؛ امتیاز ویژه یا تله‌ی نظارتی؟
این روزها سیم‌کارت‌های بدون فیلتر با نام «اینترنت پرو» در ازای دریافت هزینه و ثبت کامل مشخصات هویتی به فروش می‌رسند. اما هدف اصلی این طرح، دلسوزی برای نیاز اینترنتی اقشار مختلف نیست.
هدف اصلی و پنهان این ماجرا، چیزی جز «تشخیص هویت دقیق و رصد لحظه‌ایِ کاربر» نیست.
👁‍🗨
وقتی اینترنت آزاد را مستقیماً با نام و کد ملی خودتان دریافت می‌کنید دقیقاً چه اتفاقی می‌افتد؟
🔹
پایان گمنامی:
تمام سایت‌هایی که سر می‌زنید و محتوایی که می‌بینید، مستقیماً و شفاف روی نام خودتان ثبت و مانیتور می‌شود.
🔸
تزریق خودسانسوری:
وقتی می‌دانید هر کلیک شما رصد می‌شود، ناخودآگاه وارد یک «زندان شیشه‌ای» می‌شوید که خودتان هزینه‌اش را داده‌اید!
🔹
تجارت با حقوق اولیه:
حق بدیهی دسترسی به اینترنت آزاد را مسدود کرده‌اند و حالا همان را به قیمت نقض حریم خصوصی، به عنوان یک «آپشن ویژه» به خودمان می‌فروشند.
«اینترنت پرو» یک امکان رفاهی نیست؛ ابزاری برای کنترل نقطه‌ای و عادی‌سازیِ اینترنت طبقاتی است. بهای اصلی این سیم‌کارت‌ها پول نیست؛ حریم خصوصی ماست.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/iaghapour/2575" target="_blank">📅 15:30 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN8ks9-8MgbKxTzPFw4TxPmSZxVgdQXSyqzoaHAND6xzcpt65KPoSB3GWJjPVuSPSkl04EoZ0JJf-FmtWMtJsdUO56zxFiv0CAYSUjPExreza8FNB3x8T9qVwPzecVw8MPYw2L5CZNvHSvEKzeQmSo7xemkuRpIwiL1L7S_bYcAUVEgvhsQt8uhmjqEoqZQSU2ID7nwGdQKwUmUYovoi-z9ta4Skho99eHIhwpfk-ERPpWRI7rOrag70eDSt8fiBGqtxcNq__0WKmRIZmF2jR2DtQDpG5YAG6Cv7nBnW7xJ8Gla0DQdow6o5cWC49aCQxagr3Qq79Ea0Gtm5Cewe2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کلاینت اندروید GooseRelayVPN
🔹
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
پیکربندی مبتنی بر پروفایل
🔸
وضعیت و تله‌متری در صفحه Home
🔹
تب Logs برای عیب‌یابی Android/Core
🔸
قابلیت Split Tunneling و Internet Sharing
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/iaghapour/2573" target="_blank">📅 20:06 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">💢
رئیس اتحادیه کسب‌وکارهای مجازی
:
به شرکت‌ها زنگ می‌زنند و پیشنهاد فروش اینترنت بدون فیلتر(پرو) برای کارمندانشان را می‌دهند.
⁉️
اگر موضوع واقعاً امنیت ملی است، چطور با پرداخت پول، امنیت تأمین می‌شود؟!
منبع: کانال خبری
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/iaghapour/2572" target="_blank">📅 13:23 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 ⁉️نظرسنجی درباره سوال بالا (اگه واقعا نیاز دارید بله رو بزنید).</h4>
<ul>
<li>✓ بله معرفی بشه.</li>
<li>✓ خیر نیازی نیست.</li>
</ul>
</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/iaghapour/2571" target="_blank">📅 00:25 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✍🏻
دوستان، همان‌طور که خودتون در جریان هستید، من در این چند ماه حتی یک مورد
تبلیغ فیلترشکن، اوتباند
و موارد مشابه
قرار ندادم.
الان هم واقعاً تمایلی به این کار ندارم، چون شرایط اصلاً به‌گونه‌ای نیست که بشه کسی را معرفی کرد.
با این حال، در همین چند ماه پیام‌های بسیار زیادی داشتیم که درخواست می‌کردند حتماً یک شخص معتبر را معرفی کنیم؛ چرا که خیلی‌ها از کلاهبرداری‌های پیاپی خسته شدن و ارسال این دست پیام‌ها تا به همین امروز هم ادامه داره.
به همین دلیل، اگه خودتون موافق باشید،
افرادی رو که
از قبل با ما همکاری می‌کردند
و تا حدودی قابل‌اطمینان هستند، یکی‌یکی به شما معرفی کنیم. در این مورد ذکر چند نکته ضروری هستش:
🔸
عدم تضمین صددرصدی:
ناگفته نماند ما واقعاً نمیتونیم کسی را با اطمینان ۱۰۰ درصدی تأیید کنیم، اما افرادی که معرفی میشن همگی سابقه همکاری با ما را دارن.
🔹
عدم پذیرش تبلیغ جدید و اوتباند:
تا زمانی که شرایط استیبل و پایدار نشود، تبلیغ
هیچ فرد جدیدی را قبول نمی‌کنیم.
در ضمن،
تبلیغ فروش اوتباند هم به‌هیچ‌وجه پذیرفته نمی‌شود.
🔸
قیمت‌های منصفانه:
تمام سعی ما بر اینه افرادی را معرفی کنیم که در این زمینه منصف باشند و قیمت‌های بالایی ارائه ندهند. ولی خب، طبیعتاً نمیشه انتظار قیمت‌های قدیمی را داشت؛ چون همان‌طور که خودتون میدونید در حال حاضر هیچ‌کس با اون قیمت‌های قبلی فروشی نداره.
اگه تمایل دارید، لطفاً در نظرسنجی زیر شرکت کنید.
البته نظر شخصی خودم اینه که اگه در حال حاضر واقعاً مشکل خاصی ندارید، در نظرسنجی همان گزینه
(خیر) را انتخاب کنید
.</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/iaghapour/2570" target="_blank">📅 00:24 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚠️
هشدار مهم درباره اسکریپت VPN Over GitHub
▪️
لطفاً از این ابزار به عنوان
فیلترشکن
استفاده نکنید!
🚫
بن شدن اکانت:
تبدیل گیت‌هاب به تونل ترافیک، خلاف قوانین این سایت است و خیلی زود باعث مسدود شدن حساب شما می‌شود.
🐢
سرعت بسیار پایین:
برای هر ارتباط به یک بار
push
و
pull
نیاز دارد که آن را عملاً غیرقابل استفاده می‌کند.
🔻
خطر برای برنامه‌نویس‌ها:
گیت‌هاب یک سایت حیاتی برای توسعه‌دهندگان است؛ سوءاستفاده از آن ممکن است باعث حساسیت شده و دسترسی به این پلتفرم مهم را دوباره از کار بیندازد. (خارج شدن از لیست سفید و...)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/iaghapour/2569" target="_blank">📅 19:21 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ای بابا روش Vercel چرا بسته شد؟ هنوز آموزش نداده بودم که.
😁
سازمان فیلترینگ زرنگ شده ها. فک کنم خودشون رو آپدیت کردن دیگه به کانال من نگاه نمیکنن :)</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/iaghapour/2567" target="_blank">📅 16:34 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
دلار 177 و طلا 19,400,000
شب میخوابی صبح بلند میشی یه پله بدبخت تر میشی!</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/iaghapour/2566" target="_blank">📅 11:10 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حالا نیاز نیست پول بدین ری اکشن فیک بزنید.
😁</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/iaghapour/2565" target="_blank">📅 20:52 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GooseRelayVPN Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.2 KB</div>
</div>
<a href="https://t.me/iaghapour/2564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
دستورات
برای ویدیو
GooseRelayVPN
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/iaghapour/2564" target="_blank">📅 14:21 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INaqaKMX7CzUu_nM0c-jMKtILIo7NGXhKbUVwoHtJB9HEPOnDfANkNLes8Hi-M52wpym2TPTtlBTQhLOabawNpq8PLeY-DKIxoGm-ZqjSeM941a6lHcupELcT84g-b-Pidd5Lt0_iixtLPQqMo79vssXGB9KAb3kUuoNILurM4Qh3Re7U94rCdwgv7cwxp2bx2Nlu7Mq3b73WwrnFpbz1XDTs_Wi9N2EE1MvDHrPX1x05b_oQ7FCtnbynv0Qk_EXLzwaIUovJD_T1S3euzjvB-4nH6VM7WYMLmpWVgi_PFGRSMNw9jdJk5dKan4oMPY93yKragp_l482BK5BOljgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن شخصی و تانلینگ امن با سرویس‌های ابری! (GooseRelayVPN)
🔹
در این آموزش، یک روش عالی به نام GooseRelayVPN رو بهتون معرفی می‌کنم. با استفاده از اسکریپت‌های ابری (Apps Script) به عنوان واسطه و اتصال اون به سرور لینوکسی خودمون، یک تانل امن میسازیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل کدها
#آموزش
#فیلترشکن
#گوگل
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/iaghapour/2563" target="_blank">📅 14:18 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✍🏻
از اونجایی که دیگه کسی حوصله خوندن خبر رو نداره براتون عناوین خبر رو قرار دادم :)
🔸
دو ماه قطعی اینترنت؛ تعدیل ۳۰ تا ۵۰ درصدی نیروی انسانی در شرکت‌های اینترنت اشیا
🔹
ثبت ۳۱۸ هزار درخواست کار در یک روز در جاب‌ویژن
🔸
کانون وکلای اصفهان هم اینترنت «پرو» را نپذیرفت
🔹
ارسال پیامک اینترنت «پرو» این بار برای مهندسان
🔸
خزنده‌های گوگل پس از ۶۰ روز قطعی، دوباره سایت‌های ایرانی را می‌بینند
🔹
ضربه سنگین قطعی اینترنت به اشتغال زنان
🔸
دبیر سابق شورای‌ عالی فضای مجازی: اینترنت بین‌الملل می‌تواند ظرف ۵ دقیقه وصل شود.
🔹
سخنگوی دولت: با پایان بحران وضعیت اینترنت تغییر خواهد کرد
منبع: زومیت - دیجیاتو
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/iaghapour/2562" target="_blank">📅 11:54 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اسکریپت KevinNet DNS با پشتیبانی از VayDNS آپدیت شد
حدودا 1 هفته پیش یک آموزش ضبط شده به اسم
(بهینه ترین روش اتصال با پروتکل DNS)
و توی این ویدیو ما اومدیم اسکریپت
KevinNet
رو معرفی کردیم. و الان در آپدیت جدید میتونه از VayDns هم ساپورت کنه.
🔹
اضافه شدن قابلیت تغییر مقادیر در برنامه
🔸
قابلیت تست ریزالور حتی در vaydns
🔹
قابلیت ایجاد پروفایل متعدد برای دامنه
. قابلیت های دیگه ...
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/iaghapour/2559" target="_blank">📅 19:22 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKF7OsvIozsjx0Cw2DFBN5rssBJiouaMY6SIA3uz6oi2uk9GdW4qrOj1mItlna4qshqFdBRimFAB8qqKgCFQ4K8uP1LOTacI3ujXFYyRoZjqE2lcCEbSXOVW2e8G0MudNBEkdrcI0qfnsrW1qRdP1FORayUJ55-fmlIAaB9PXi-rV2n2WHM8SZrYfhJfe1DdJUeS2OTPRiNc2D8voz8u3vj2phV1nldCVDLwiSEdbKB6wNzpS0XT9lt7Q64iXh33aGZSXLZZ6uNZDQH3OJCP3-pFrdLq-QD3BJf8nfec0eoUBo1wQL_8zzvmgPuWxNqCFM2NIUmmGesXeYLbenwwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت هارد ۱۰ ترابایت بنفش (Western Digital Purple) ناقابل 108 میلیون
🫠
همینطوری ادامه داشته باشه برای خرید یک گوشی دکمه ای هم باید همین مقدار پول بدیم....
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2558" target="_blank">📅 09:34 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dznZnAmpOUZOmWVxQIDx28FFE9Cqfuo8uiBQ56eBxlWn6OtQkkcohc-FT7FuAsuHniTKZnTGt6hzrtH2EsjDd3wk7XY3oxqJ0j6HnovQUDpr-R38-dOBj4UYiClrNSQaIxroQHGwOqBFIff5QHQRrBEi3kiCJScaRnTN2G6hdZuzavBBz4vhU2Zq4hSkDCC0bW8W8GBVwDjsnhryVS_VtdR02y1wYC2hgHUwwF4ypgnIKuqD89qntJOsEr271u68JOrc8Gn_FR7R-ZdGqDzHSHlliBCqotAuSW7RBTXO2eq-rdDXH_EYJuYNUmvq4JAOBOnO3IRv9sFcUELwI3gQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب‌کننده خودکار Parley Chat
🔻
از اونجایی که راه‌اندازی و کانفیگ کامل یک پلتفرم چت روی سرور (با تمام دردسرهای تنظیم دیتابیس، وب‌سرور و گواهینامه امنیتی) کار سخت و زمان‌بریه، این ابزار جذاب اومده تا همه چیز رو براتون ساده کنه!
🔸
راه‌اندازی کامل بکند (Backend) و فرانت‌اند (Frontend)
🔹
کانفیگ خودکار Nginx به همراه دریافت گواهینامه SSL
🔸
ایجاد سرویس‌های Systemd برای مدیریت آسان‌تر و پایداری سرویس
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/iaghapour/2557" target="_blank">📅 21:48 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvvhYTgGhfWVXXFR1Gz5BAKpvfv3uAD4DA7CE8ARjvA8M22rJk_Lt6-ypZrzIKz4-dYDq-2_5kXVyl_QZm5CrtA_cSAl6-KblSf3Zof0-EzDf-QeLS1tZVE0QBriHGHWGxrkABHn4hbk6gP5oOntzgvahuRl4M6EKDF3N0yWiA8n0toBvP93RNsxkkTmHnkXletE5T_nN6HUQ-XjIzhhLm7OO8tKnHPAmOFtQ0NfHaiJgfAqsoaXZq0tr8lTEQTuWLv1BTDC34xXTl1cjKZnihZ_UcDfU3-YFHR0LxzLwLuQKXLVZrqduesa0xD0TODrOtWzB-Fwx8lkKviSchLzvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
لینک همه سایت‌های کاربردی تو این سایته!
🔹
از اونجایی که پیدا کردن لینک سایت‌های کاربردی در دسته‌بندی‌های مختلف مثل آپلودسنترها، سایت‌های دانلود فیلم و سریال، ابزارهای آنلاین و... خیلی سخت و زمان‌بر شده، سایت WebDX اومده همه این‌ها رو به صورت منظم و دسته‌بندی شده یک جا جمع‌آوری کرده.
🔗
لینک ورود به سایت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/iaghapour/2556" target="_blank">📅 21:40 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">💢
سازمان نظام پرستاری:
با وجود اینکه امکان برقراری اینترنت پرو برای اعضای خود را داریم، تا زمانی که همه مردم ایران به اینترنت متصل نشوند از این امکان استفاده نخواهیم کرد.
🔴
در اطلاعیه کامل سازمان نظام پرستاری:
«بسمه تعالی
سازمان نظام پرستاری جمهوری اسلامی ایران به اطلاع کلیه پرستاران و مردم عزیز ایران می‌رساند؛ با توجه به محدودیت‌های ایجادشده در دسترسی به اینترنت بین‌الملل به‌دلیل شرایط خاص جنگی کشور و ارائه دسترسی محدود (اینترنت پرو) به برخی اقشار، امکان اعطای این امتیاز به اعضای سازمان نظام پرستاری نیز از سوی مقامات مسئول اعلام شد، لکن سازمان نظام پرستاری جمهوری اسلامی ایران براساس بررسی جوانب مختلف تا زمان رفع محدودیت‌های دسترسی عموم مردم به اینترنت بین‌الملل، درخواست هیچ امتیاز ویژه‌ای را برای اعضای خود نخواهد داشت.
ان‌شالله زمانی که این امکان برای همه مردم ایران فراهم باشد، پرستاران نیز در کنار آحاد مردم از این امکان استفاده خواهند نمود.»
﻿
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/iaghapour/2555" target="_blank">📅 13:20 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDSnOJ6VjEkfkBcnIFDOjBjo1Wr6HdRfQUPrcJtvgc-m8fwy_ZWVuMsb3HHdBb_HjD-FFRM2xtV5Idh0XBzdBL-1N5WNdOnVTGJlQ4r_cjGdo4ce8ZHctS-ad9BxGVnz2lAUkr7El7W-JsK8cbGRCXUTb9RY0MiQGlgu1nX71eG-4Xmf-QRbBOMxuUBNyu79Y7Jan4JSj0NT7b-So19583REaFvTaUAUurMtkIXMeasj4R_-MApP-HPmpeaVNOXma4uVuKON625cFqgdZ-irgSTZm2Q4NYofdebi8z8IDLJ_lxLqQpI4SdBqBEbD3VCEGf37b6sBGuISr94rHwcrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات‌های کاربردی تلگرام برای شرایط اینترنت محدود
با توجه به محدودیت‌های فعلی، این ربات‌ها حکم یک اینترنت آزاد و همه‌کاره را در قلب تلگرام دارند:
🔹
@GPT4Telegrambot
دسترسی به ChatGPT، جمنای و تولید تصویر.
🔸
@WebSearchAiBot
جستجو در گوگل و خواندن محتوای سایت‌های فیلتر شده.
🔹
@apkdl_bot
دانلود مستقیم برنامه‌های گوگل‌پلی (جایگزین استور).
🔸
@SaveAsBot
دانلود ویدیو و عکس از یوتیوب، اینستاگرام و توییتر.
🔹
@reddit_download_bot
دانلود محتوای متنی و تصویری از سایت ردیت.
🔸
@UrlUploadBot
تبدیل لینک دانلود سایت‌ها به فایل مستقیم تلگرامی.
🔹
@ReadabBot
تبدیل مقالات وب به حالت مطالعه سریع در خود تلگرام.
🔸
@vtovbot
تبدیل فایل‌های صوتی پرحجم به ویس باکیفیت و کم‌حجم.
🔹
@voicybot
تبدیل ویس به متن با پشتیبانی از زبان فارسی.
🔸
@fakemailbot
ساخت ایمیل موقت برای زمان‌هایی که جیمیل در دسترس نیست.
🔹
@newfileconverterbot
تغییر فرمت انواع فایل‌ها مثل عکس، ویدیو و داکیومنت.
©️
با تشکر از ایوب عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/iaghapour/2553" target="_blank">📅 20:41 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2552">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💢
اردستانی؛ نماینده مجلس
:
حکومت تصمیم گرفته فعلا روایت خودشو بیان کنه. برای‌همین به خبرنگارها؛ دانشگاهی ها؛ نماینده های مجلس و هنرمندانی که با حکومت همراهن اینترنت داده تا برای خارجی ها تولید محتوا کنن.
پ.ن: عجب بابا عجب دیگه کار از مخفی کردن و شرمنده بودن و... گذشته. خیلی قشنگ این تبعیض رو فریاد میزنن.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/iaghapour/2552" target="_blank">📅 17:38 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✍🏻
یه تناقض عجیب بین حرفای مسئولین و واقعیت اینترنت کشور هست. از یه طرف رئیس‌جمهور میگه موافق وصل شدن اینترنته، از اون طرف سخنگوی دولت میگه اصلاً اینترنت طبقاتی نداریم و وزیر ارتباطات هم کلاً وجود لیست سفید رو گردن نمی‌گیره.
ولی خب تو عمل، داریم یه جور تبعیض و آپارتاید اینترنتی رو به چشم می‌بینیم:
افراد رانتی:
اینترنت کاملاً آزاد و بدون فیلتر (همون لیست سفید).
شهروندای درجه دو:
یه اینترنتی که بدون فیلترشکن دوزار نمی‌ارزه (همون اینترنت پرو).
مردم عادی:
محدودیت کامل و حبس شدن تو شبکه داخلی.
از همه جالب‌تر مسئولینی هستن که میان میگن این محدودیتا موقتیه. یعنی ۶۰ روز قطعیِ پشت سر هم، معنی «موقت» میده؟ اصلاً می‌دونید موقت یعنی چی؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/iaghapour/2551" target="_blank">📅 19:30 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUWeJX988aHj4SCUBXt8p9KXp9rG9nVkamT_UmeVTMVckuKypblQjk5Gk3d-TxHvOH29_-_0bWen75XNlATlK57wmq0nE2OW_oVPozqyhObej4keLQeMQoNZh6NXI24VQ2TYDKef9RjV7abqh6FF-nEiDdEaLJbeL1cctVDAqB1d5fagwweIuCakn5r5wx8-rckyg64ljoKRT1I0S-Xf8GHHJn1Ifd8n8PQmkU8ANCxW7cBNtRNL6LjbiJrSq4d2TsUIOAqoUuVnZaSfrn8ASEz5PpiiQH2jkJXYcv0uFs-YsbJXjoD2Hp14eLQgZ2ns1KRZ1NdPYXCxTHCGHRhqjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
روز ۵۶ام از قطع اینترنت در
#ایران
هستش و اتصال بین‌المللی بیش از ۱۳۲۰ ساعته که قطع شده و کسی پاسخگو نیست!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/iaghapour/2550" target="_blank">📅 11:19 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚠️
یک یادآوری و هشدار خیلی مهم به دوستان عزیز
دیگه واقعاً حسابش از دستم در رفته که تا حالا چند بار این موضوع رو گفتم، اما باز هم باید تکرار کنم:
ما اصلاً هیچ گروهی نداریم!
متأسفانه بعضی‌ها با استفاده از اسم و عکس ما اقدام به ساخت گروه یا کانال می‌کنند. حتی بعضی‌ها خودشون رو به عنوان «پشتیبانی» ما معرفی می‌کنند. من قصد قضاوت در مورد هدف این افراد رو ندارم، اما این کار باعث سردرگمی شما میشه و اصلاً درست نیست.
لطفاً توجه کنید که فعالیت رسمی ما فقط و فقط در چند آدرس زیر انجام میشه و تمام:
🔸
یوتیوب:
youtube.com/@iAghapour
🔹
کانال تلگرام:
t.me/iaghapour
🤖
ربات تماس با ما:
@iaghapourbot
🐦
توییتر:
(که البته خیلی اونجا فعال نیستم)
نکته مهم: هر گروه، کانال یا شخصی که خارج از این لیستِ بالا خودش رو مرتبط با ما معرفی کرد، هیچ ارتباطی به ما نداره.
ممنون از درک و همراهی همیشگی‌تون!
🌹</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/iaghapour/2547" target="_blank">📅 15:42 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
معرفی پیام‌رسان دلتا چت و سرور Madmail
🔹
یک پیام‌رسان امن و غیرمتمرکز بر بستر ایمیل که حتی در زمان محدودیت‌های اینترنت هم به کارتان می‌آید! با پروژه Madmail می‌توانید به سادگی و سرعت، سرور اختصاصی خودتان را بالا بیاورید.
🔻
ویژگی‌های کلیدی:
- امنیت به شدت بالا: رمزنگاری پیشرفته و عدم نیاز به شماره موبایل.
- مقاوم در برابر قطعی‌ها: امکان راه‌اندازی آسان رله‌ها روی سرورهای داخلی.
- اجرای سرور چت‌میل تنها با یک فایل باینری (حتی روی سرورهای آپدیت‌نشده و بدون اینترنت بین‌الملل).
- پشتیبانی از تماس صوتی و تصویری.
🔗
لینک گیت‌هاب برای بررسی و نصب
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/iaghapour/2545" target="_blank">📅 13:15 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✍🏻
دوستان، اگر برای باز کردن تلگرام و سایت‌های مختلف از روش
MasterHttpRelayVPN
استفاده می‌کنید، حتماً حواستون به این 2 تا نکته مهم باشه:
۱. آی‌پی شما تغییر نمی‌کنه:
برخلاف فیلترشکن‌های عادی، آی‌پی شما تو این روش همون ایران می‌مونه. در نتیجه سایت‌های تحریمی براتون باز نمیشن و حتی ممکنه سایت‌های حساس اکانتتون رو به خاطر آی‌پی ایران بن کنن.
۲. جیمیل اصلی‌تون رو استفاده نکنید:
یه سری گزارش‌ها به دستمون رسیده که گوگل ممکنه اکانت‌ها رو مسدود کنه. با اینکه هنوز مدرک زیادی وجود نداره و قطعی نشده، اما بهتره اصلاً ریسک نکنید و از جیمیل شخصی‌تون استفاده نکنید.
۳. نسخه اندروید رسید:
خبر خوب اینه که از امروز می‌تونید نسخه اندروید این روش رو هم نصب و استفاده کنید.
🔻
ممکنه مواردی رو من پوشش ندم ولی کانال
IRCF
که یکی از قدیمی ترین و بهترین کانال ها هستش میتونه راهنمای شما باشه.</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/iaghapour/2544" target="_blank">📅 13:09 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⁉️
جواب به سوالات پرتکرار شما + بهینه ترین روش اتصال با پروتکل DNS
🔹
توی این ویدیو به پرتکرارترین سوالات شما درباره ساخت فیلترشکن جواب دادم. در نیمه دوم هم یک روش فوق‌العاده و بهینه برای اتصال با پروتکل DNS رو به صورت قدم‌به‌قدم آموزش دادم تا پایداری بیشتری…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/iaghapour/2542" target="_blank">📅 17:08 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfigy8C1-0EQ24XC1HJPWUFWQrCJMXwV1TmX97i-xxbme37ES6_qvjLXcCgZ7GTIROK9LnK-F8-w-cd3DFqHA6AQPQLL_BWvgUqBLwBrn1H5nT7hbQzYkjRakBa5V6TqNk-7KnMHyLOUNTunf-ocYghUtqXGwrX1FWzghKmX_CV-nQjVvLzWmi7rbwOmFdiGrIIbo4ZfMeTiVZ7D5-piGImTcyqN128aYvSH6PawAbiQmTE9fDL29tXA6cvXKLUsMRNMkGlS3ZpE9CPPfjlCqmkQVY-7gIa5P3_lmnjDQPGe6_fmACRJAQ_a8GWxYWCGUuX5kloI_T3m06Q0CXKcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
جواب به سوالات پرتکرار شما + بهینه ترین روش اتصال با پروتکل DNS
🔹
توی این ویدیو به پرتکرارترین سوالات شما درباره ساخت فیلترشکن جواب دادم. در نیمه دوم هم یک روش فوق‌العاده و بهینه برای اتصال با پروتکل DNS رو به صورت قدم‌به‌قدم آموزش دادم تا پایداری بیشتری داشته باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل exe اسکریپت
#آموزش
#فیلترشکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/iaghapour/2540" target="_blank">📅 16:25 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-jLlw9aqAQ8sroQM5tx1lFqxu2GYzIjum1LbTCzH6_65u3RMMZ5WfZXJ4f9NfGKReHsyqdoALLbWlWlXoaRkfF53AoBM9NNbFvLcGo2MqHZGKbKPSPPJyXCHQIwtnZ3B6btlpnfCYlZr4IUXfr5dqFGXuAyjYpJD4Xd3u84F7PeOAUQMLmQbTI7NUquVrBb3wOM_0j2RT_Ln8zzFqZA1QKYBBsnkYKVRt5FIWR3YeUIT0m3aqrHAB6UNXfEIF7wBHk-jzZ6m0ZXQAS2HgVUW0gAmYwL5Bq1bMShB1tBe7x3QaZ5wjolC5E3zoeuuOOrn-KJNVadl6yEj5ZXGFwx3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست ملی کردن کامل اینترنت فقط برای طرفداران نت ملی!
🔹
هرچی از طنز ماجرا بگم کمه :) یک
کارزار
ساختن و گفتن کد ملی طرفدارهای نت ملی رو بگیرید و اینترنت رو برای اونا برای همیشه ملی کنید :)
داداشایی که سنگ اینترنت ملی رو به سینه می‌زنن، بفرما این گوی و این میدان! لطفاً اینترنت این عزیزان رو روی کد ملی‌شون برای همیشه «ملی» کنید تا دیگه غصه ما رو نخورن. ما خودمون یه جوری با این اینترنتِ پر از فسادِ بین‌المللی کنار میایم!
🤣
🔥
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/iaghapour/2537" target="_blank">📅 01:02 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بچه‌ها حجم پیام‌ها اون‌قدر زیاده که اون عزیزی که به عنوان پشتیبان داره همکاری میکنه با ما واقعاً نمی‌رسه همه رو سریع بخونه یا جواب بده. شرمنده‌ی روی ماهتونیم و بابت این موضوع از همگی عذر می‌خوایم.
🙏🏻
🌹</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/iaghapour/2535" target="_blank">📅 00:37 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
آپدیت مسنجر سانگبرد منتشر شد
(
v0.9.0
)
🔹
با اسکریپت زیر میتونید روی سرور ایران یک مسنجر شخصی برای خودتون و خانواده بسازید.
-
📥
قابلیت آپدیت آفلاین برنامه از اسکریپت
-
🔒
رمزنگاری Client-Server
-
📃
قابلیت Context Menu اختصاصی برنامه
-
↪️
قابلیت فوروارد کردن پیام
-
🗑
قابلیت پاک کردن پیام (یک طرفه و دو طرفه)
-
✏️
قابلیت ادیت پیام
-
💬
قابلیت پاک کردن خودکار پیام های متنی
-
📜
امکان دریافت سرتیفیکیت 6 روزه برای IP در اسکریپت
-
♻️
دستور بازیابی دیتابیس از بکاپ در اسکریپت
-
🚫
دستور بن کردن یوزرها در اسکریپت
-
✨
بهبود UI/UX
-
📜
قابلیت نصب سرتیفیکیت با فایل های کلید SSL
-
👤
دستور ادیت مشخصات یوزر در اسکریپت
-
⚙️
قابلیت تنظیم پورت دلخواه برای nginx در حالت نصب با دامنه
-
🔧
به همراه رفع باگ های متعدد
اطلاعات بیشتر در گیت‌هاب
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/iaghapour/2534" target="_blank">📅 00:31 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">2 تا آموزش عمومی و خوب در پیش داریم.
👈🏻
یکی آموزش نصب و اجرا هوش مصنوعی لوکال و بدون اینترنت.
👈🏻
و یک آموزش کاربردی و پاسخ به سوالات پر تکرار شما.
فردا یکی از اینها منتشر میشه.
💚</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/iaghapour/2533" target="_blank">📅 00:26 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✍🏻
همان‌طور که احتمالاً دیده‌اید، اخیراً آموزش‌ها و اسکریپت‌هایی (مشابه Spoof SNI) برای دور زدن فیلترینگ یوتیوب و برخی سایت‌ها منتشر شده است. البته قبلاً هم شاهد موارد مشابه بوده‌ایم.
دلیل اینکه ما این روش‌ها را در کانال قرار ندادیم، درخواست بعضی از دوستان بود! درخواستشان چه بود؟
اینکه روش‌های جدید را «پابلیک» نکنیم
تا مبادا هزاران نفر از مردم عادی از آن استفاده کنند و روش بسته شود؛ در عوض، فقط یک عده محدود بتوانند با خیال راحت از آن لذت ببرند. واقعاً عجب منطق جالب و «ازخودگذشته‌ای»!
😇
ولی خب به هر حال، کانال‌های دیگه این آموزش‌ها را منتشر کردن و میتونید از اون ها استفاده کنید.
این توضیحات هم بماند برای آن دسته از دوستانی که قدرت تفکر دارند و متوجه ماجرا میشن. :)</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/iaghapour/2532" target="_blank">📅 00:25 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
آتش بس تا اطلاع ثانوی تمدید شد.
🔹
ولی اینترنت باز نمیشه. چون امنیت به خطر میفته. این که 2 ماهه سیستم خودمون و حتی گوشی رو آپدیت نکردیم و آنتی ویروس خودمون رو آپدیت نکردیم و.. خیلی به امنیت آسیبی نمیزنه. حداقل به امنیت ما آسیبی نمیزنه :|</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/iaghapour/2531" target="_blank">📅 00:14 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💢
رئیس شورای اطلاع رسانی دولت: قطعی اینترنت موقتیه و یکم دندون رو جیگر بزارید تا دشمن رو به یه شکست ذلیلانه بکشونیم بعدش حتما وصل میشه و به شرایط عادی برمیگرده.
پ.ن: کاملا از ثبت نام اینترنت پرو در رسته ها و شغل های مختلف مشخصه دارید راست میگید.
👌
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/iaghapour/2529" target="_blank">📅 17:53 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
گوگل و گیت‌هاب دوباره باز شد!
بازی موش و گربه شده قشنگ!
🧐
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/iaghapour/2528" target="_blank">📅 13:31 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚠️
گیت هاب هم بسته شد
احتمال موقت بودن یا اختلال هم وجود داره!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/iaghapour/2525" target="_blank">📅 11:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚠️
گوگل مجدد فیلتر شد
البته وقتی سرچ میکردی سایت های توش رو نمیتونستی باز کنی پس خیلی هم فایده نداشت! مثل این میمونه که بچه رو ببری ویترین اسباب بازی رو بهش نشون بدی ولی بگی حق دست زدن نداری...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/iaghapour/2524" target="_blank">📅 11:44 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-xGuC1qbc0ec3GS6sDkf9HhuSWWEVdXb3C-DthLN07nHThgE5tcqBK50vhelYDYgy0yJ3xqIwBxy764OFNWugM_QtTBwGOd6xtq2fSc5OTVEvi5aY8nPx1LoXOdIRZ0ZjioCNPGn3AC4awnL47zsJ0J-NPP1MC-xzBrLlhjiVetdptfC8XT9zlvr2Qp7-CDHICAs16ty_lsHOUJUYbG8YiyS9TRwa1i2hVnl7wPiISO6a9SZ3phDTHFkCAzo-AwTlJNbBPaZdsyi71J0s1K-nc95ybU5iWr4_hQqr037HLtS8JqndqeRMerOcVeytWeMDIvB1SA6HqUSwiLEwikow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استارت اینترنت طبقاتی توسط همراه اول!
🔹
همراه اول رسماً از طرح اینترنت طبقاتی خود رونمایی کرد. با افزوده شدن بخش «اشتراک پرو» به منوی این اپراتور، زین‌پس تنها افراد خاصی که فرآیند احراز هویت را طی کرده باشند، امکان دسترسی به این سرویس را خواهند داشت. گفتنی است هزینه بسته ۵۰ گیگابایتی در این اشتراک، ۲ میلیون تومان تعیین شده است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/iaghapour/2523" target="_blank">📅 00:27 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY9VXjuSopOSHJ7BPTN-WiOAKfyTkgsslmZ-gpDzRoSTrR_do14bs5-5ucweBJguI8ysC1WTh4mGBPZT_BNAFqpv2ayTQU_gyR3td00-0ZlIio-b7h4p-nJAwa6R6vCHp9mmCYwOIGyHwBkNA5bIFj3GOWMYH59ip4TaNFKTqsHf2Jh9xnpeDS13ofEG8V3NRazPvbgNoK8Jo4a_Jq598gwYWFz7D_RORg4kiyELVW_-9A2WSswQkEWQS3g5Gvlv4l-tIMWWzGUVgsf8d7BexWio0g_lhV4SYSSsozdhG1n-GoSLV3LnR7sk8dHywYgeuQa1_7y7Zo0ZHRWsQ1kLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
چرا جهان، زندان دیجیتال ایران را نمی‌بیند؟
بیش از دو ماه است که اینترنت در ایران قطع شده و میلیون‌ها نفر در یک «اینترانتِ» محدود و ایزوله حبس شده‌اند. کسب‌وکارها نابود شده و ارتباطات فلج شده است، اما در کمال تعجب، سازمان‌های مدعی حقوق بشر خود را به خواب زده‌اند.
🔻
چرا نهادهای بین‌المللی خفه خون گرفته‌اند؟
سازمان ملل سال‌ها پیش قطع اینترنت را نقض صریح حقوق بشر اعلام کرد. اما ظاهراً وقتی نوبت به ایران می‌رسد، این قوانین چیزی جز کاغذپاره‌های نمایشی نیستند.
اگر اینترنت در یک کشور غربی دو ساعت قطع شود، دنیا جلسه اضطراری می‌گذارد! اما ماه‌ها حبس دیجیتال در ایران، ارزش یک واکنش قاطع را برای آن‌ها ندارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/iaghapour/2522" target="_blank">📅 19:45 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS90kAJEuFl5YMQ-7sOE0yve0vVD9bHwxsmxihTH2DVZ4cNXtoL-g62x4gTKyE9DbJS_g4EgwCtxWEhlR7SYXg0DlI87AloLVgEwmIlYCP6rJ9qFQuyoonz8JDUcywSV7MLUVIO4Z3jfFaZI1aGFBHxqih0IVzy6xvtAWjshV6_SQfYzmw8INbhxhxVnx7rLKhQ8AAGRWNVrvtQSuYb2gnasemdcuqhKDEnEKd6PA1z5nal314AZEPlf7Iqotlnv0TBwS8ij-LU-yVgZGNOeHQP61WM-cKjKbqt61OI_pGG_7xaN-BUPxzWRFCGc5ovyxYfeRfHQFU-xtzOasrTPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین کانفیگ فروش دنیا
😊</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/iaghapour/2521" target="_blank">📅 15:30 · 31 Farvardin 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
