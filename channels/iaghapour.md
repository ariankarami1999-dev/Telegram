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
<img src="https://cdn4.telesco.pe/file/UP4jXBaW9TdXvNf1Nvfdh5QVENFr7PzCjJyYAm6p7UiE0enCInHvrea7zD6Yg_4PwzV_00qd9CU5wvChXYyKUzlXKLo9MCgBV6R4vdk_u0Ixtjdo_z4cuii-W0Bk4bEgWlPvdKbhH184tMG-ExN7bXj9aY80GpToxE8rxO6ovO34TMwKLenQcDyIWSCnetCurft5yXAShLJ7iiUHpQpEWp1BMVKk9FnNNN5MLRoowM6USNCwJY_zSigrXWAMEI3FYMRvofAtMfLGNh0YUptu5tUzIpSDMU7OtS8hMi1H1fzhQIB9MYNoFt4uY6SMnPVQd1GNkgfRWHJVdvX2eegNyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 52.8K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 17:17:09</div>
<hr>

<div class="tg-post" id="msg-2805">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from༄𝘼Ꮮꀤ™࿐</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S29pqOI6g6-vKHFV-NFkQlbZylCHmBdd48I9uI9mof1wYWlesEwT3jlNUU7uwg1ia7ELBZs_yWLDeoR-FSST0UzDojtEVAUDVuxfemQ9qaBFePOT6Tti8oVIfi0TZ0hMgaTYaLgUm_aV1ol3XtSbu6TTjj0X--taMYqeWOLOvNzSeh3gCz3VhkKwVifpFbVXYao10i0uBPCSom3bBWjmKmaeZEIh9hHWSzz0_A_7Y4HGdjqGhkyMIQmyHChEXzQT0e-dsw2Qaxx34L7kPUCk_9zdumYYWFRzN6oeqv1zL2m4e_ZAO7gF1LVUl66SAnUd4H6bOJnknr1JhUQ8-X3OMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
گلایسیت استور | فروش اکانت‌های اورجینال و قانونی
✨
اگه دنبال خرید اکانت‌های کاربردی و مطمئن هستی، گلایسیت استور بهترین انتخابته!
ما انواع اکانت‌های
هوش مصنوعی، استریم موزیک، فیلم و سریال، کاهش پینگ و ضد تحریم، آنتی‌ویروس
و کلی سرویس دیگه رو با قیمت مناسب ارائه می‌کنیم.
✅
اکانت‌های اورجینال و قانونی
✅
تحویل سریع و بدون اتلاف وقت
✅
پشتیبانی سریع و دقیق 24/7
✅
خرید راحت، امن و مطمئن
از ChatGPT و ابزارهای هوش مصنوعی گرفته تا Spotify، YouTube، Netflix، آنتی‌ویروس و سرویس‌های گیمینگ، همه رو یکجا داشته باش!
برای مشاهده محصولات و ثبت سفارش وارد ربات شوید
👇
👤
Tm.GlysitBot
✈️
Tm.Glysit</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/iaghapour/2805" target="_blank">📅 21:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2804">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ19CDKgs75JZFMUiRC12Z8s61huhulm-WpIERX68t6pkZDpo50tOs2q-RwkfDBUND5lyX13Rt8koL0JkwiXnlY8ZY3ZvGC41WAkamx5IcA8tQv5v224vf-VYI--GhTUMPtzsMwgn761rpQf0_4EcUDW5SsaT4L5ONyH2vktaFu8kOOmCcgWp0vjvnHLv4bypS0hXxN7HRc96VwbcuwbH_RCpQ96uvZEGsBZb9SxWxty8ioKonCo1jkGlLPFdftIExhe_rP-gf4OGJYZWN3XBk9H3lk8NHmlnhDnnAGsKLKjFet_JQ0j72SPx_Pa9jK0UYjo-hT4DghdBhtyO0YckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون نیاز به خرید سرور فیلترشکن شخصی خودت رو بساز!
🔹
در این ویدیو یاد می‌گیریم که چطور با استفاده از پنل قدرتمند BPB روی بستر کلودفلر ورکر یک فیلترشکن کاملاً شخصی و رایگان بسازیم. این روش نیازی به تهیه سرور مجازی ندارد و به شما کمک می‌کند تا بدون صرف هزینه اضافی، یک پروکسی اختصاصی و پایدار برای دسترسی آزاد به اینترنت راه‌اندازی کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#رایگان
#ورکر
#کلودفلر
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/iaghapour/2804" target="_blank">📅 15:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2803">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5lmj6sQck0UYWvTnTVJ-bKHK6o0kvN4P0p6__m0FTwr1I7NOKgPmJLJHH9GVh7mC7qf_CU3Ubh3RMuHWynR2kCeD6TYhqXZ1Cb6m9nAisyzWt8BySbNTXK3MVVm9fAezx__80K07QUyuaQq3qlXqVwV1gtpSkec_dCyMcRG7dzYAfsSy8bJUAvs7rKxwdBwmr59iYAF_K1T8XbBH8uk0Q2AqsjOmzkOrwDqMS1Ft1f2X9cbVNdNk-jUh-Lg0UojR1s4M1fEwwekwwLsLBpvy9gcENjlj0D1-l5g0rvp-VK5x8jVmRysM8XB_YTP4arGRYmcEv9_Yn4t85k6cp0a0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Holt Chat؛ پیام‌رسان امن و ضد سانسور
اسکریپت (Holt Chat) یک پلتفرم پیام‌رسان کاملاً متن‌باز و سلف‌هاست است که با تمرکز ویژه بر حریم خصوصی و مقابله با سانسور اینترنت طراحی شده است.
✨
ویژگی‌های کلیدی:
🔹
رمزنگاری سرتاسری (E2EE):
تمام پیام‌های شخصی و گروهی به صورت کلاینت-ساید و امن رمزنگاری می‌شوند.
🔸
سلف‌هاست:
می‌توانید سرور و دیتابیس آن را به طور کامل روی سرور و دامنه شخصی خودتان راه‌اندازی و مدیریت کنید.
🔹
مقاوم در برابر سانسور:
معماری پروژه صراحتاً با هدف عبور از محدودیت‌های اینترنتی و فیلترینگ توسعه داده شده است.
🔸
دسترسی‌پذیری:
دارای اپلیکیشن اختصاصی برای اندروید و کلاینت تحت وب.
🔗
گیت‌هاب پروژه برای بررسی و راه‌اندازی
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/iaghapour/2803" target="_blank">📅 14:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2802">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDoprax</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-VFkcxTPYaxHi-7x_ihONuAojjjoA6pRdrpSRkVNVhC_hutyB-E1O7eOLfPXHcXbdaeG8OHQkpogDuAtxUh1B_aXsfbXrxFuW70oREmhmcjqzxrmnVcE22MISETDwzyLC8N2-jHs1B1wFk-rA1vAEWIpcFR2dYVnm-VK2ir3oG3nkzOlddTBgkmS5qK0Vftj1jJ7Pj3_0tXIelN-ddWqWQWQHr9th4QrCfucnH2xykogqO9BuzBNbjXzrHCsMGyQ93RA70MxE0iLyxXhJD6ndRqNJEXgjRHeHX1eBOX60KrrPzjyvQ05oWDsNwR9reWadtxQ1AmB9TQAggdeULyMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
سرور ابری رو از هر جای دنیا و با هر ارزی که دوست داری بخر!
🌍
دیگه نیازی نیست برای خرید سرور از دیتاسنترهای معتبر جهانی دغدغه پرداخت یا محدودیت لوکیشن داشته باشی. در دوپراکس (Doprax)، بهترین زیرساخت‌های ابری دنیا در یک پنل اختصاصی زیر دست شماست!
با دوپراکس می‌تونی از غول‌های تکنولوژی مثل Google Cloud, DigitalOcean, Hetzner, Vultr و چندین پروایدر دیگر، سرور تهیه کنی.
✨
چرا دوپراکس بهترین انتخاب شماست؟
📍
تنوع لوکیشن:
دسترسی به ده‌ها لوکیشن مختلف در اروپا، آمریکا، آسیا.
💳
پرداخت بدون مرز:
امکان پرداخت آسان با ریال و یا رمزارز.
⏱️
پرداخت ساعتی
: فقط به اندازه‌ای که مصرف می‌کنی پول بده!
🔄
امکان تعویض IP
: قابلیت تغییر آی‌پی در اکثر دیتاسنترها.
همین حالا وارد سایت شو و اولین سرورت رو با کانفیگ دلخواهت بساز
👇
🌐
وب‌سایت:
www.doprax.com
💬
پشتیبانی و اخبار در کانال ما:
@dopraxcloud</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/iaghapour/2802" target="_blank">📅 23:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcns-yLnDpPtD7kvCUlWEi3uzc1q1ltmfjkntzCePTHaLi-I7-8jYCr3qNZDB9qFce7_UAIJxLmhHFTm5GYejAwAA_oEzJb3GXUuoBwIo5HuTWZmy5B0Es8Sz7fKY5pHeTjARYZLdOvqS4B2I4sP7WIULXVmpIMUEapxRqSRBqKapRAWNs6NAkxAaE-WVRLq06GZ8RzNDTaOU5LtQvrYdp-CZqSMGKrw1eCDufY7-FmPYKSAD-TlFaAqAfP75CLAEWfTQ4guAppJ3kSm_UUOKU2ZIPEpE3Z9TOV6cg3Eq6vn8I-KrhqUa0WtD7a2IXDGaVCcPb1168f870soUd7Sjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل‌ها برای نمایندگی فروش کانفیگ
👌🏻
🔹
در این ویدیو به معرفی و بررسی ۲ پنل قدرتمند می‌پردازیم که دارای سیستم نمایندگی فروش و قابلیت‌ مالتی اینباند هستند. با استفاده از این پنل‌ها می‌توانید به راحتی برای مدیران خود سطح دسترسی‌های مختلفی به عنوان نماینده تعریف کنید. اگر قصد دارید سیستم فروش خود را گسترش دهید و نمایندگان جدیدی اضافه کنید، این ویدیو دقیقاً برای شماست.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پنل
#نمایندگی
#فروش
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/2801" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNaUlfUVdYsXsscGH69RPbmIAEiTEm-YICARlbHkkjes7bTEZ50OhHCW6NsRB4Ug9HkIgELkIStdliTko2a4eeqdJlRxdwmvMUB-n_cPJ4uU3WgXNG5mHTWpJ_V2JMOcdXWBhULL9xIWjnKRQ8XnmpKcuKNhwau3KVRkbVUUt7qdMwd-uE4cXsfgGcUhGi8xk058dCfRnDZDvsSAYUmg6MF791E06jGUBljSszUeVzdY7NaKbgQbUvRbDu8Dn5W83UxeNr3ulyK-cO0tv-yfeVhWfxF8P5-ygEKn7n-B6bo2-6IusVdzKhJYCtdM5-0xkqNJDSk9EDKXckJT4dALYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت نسخه 1.0.3 نرم‌افزار UAC SNI Spoofer Windows منتشر شد!
✨
نسخه جدید این ابزار با قابلیت‌ها و بهینه‌سازی‌های جدیدی همراه شده که در زیر میتونید برخی از این ویژگی ها رو مشاهده کنید.
🌐
انتخاب کشور:
امکان انتخاب کشور دلخواه برای متصل شدن به موقعیت مکانی موردنظر.
⚡️
بهبود سرعت:
افزایش سرعت بارگذاری صفحات و برقراری سریع‌تر اتصال.
🔌
کنترل پروکسی ویندوز:
اضافه شدن گزینه فعال یا غیرفعال کردن پروکسی سیستم.
🎨
رابط کاربری بهینه‌شده:
جمع‌وجورتر شدن منوی خانه برای دسترسی راحت‌تر و یک‌جای تمامی گزینه‌ها.
🔗
لینک دریافت نسخه 1.0.3 از گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/2800" target="_blank">📅 17:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yrf19scCGQiHSTdWwKlVVoK6Mr1HdQrOySiVarNCenIGpl0SM9FccZELUThmO2dlzAW8YohQHl4nRCa11O1dPp3a6_cE4uSnNm8gqQxUwImp3eFI0Ai7NLsR5T-f1Axj1kobfhsQPOz1wwprmKXb3pGVU92urALjLmlWTkVrsUYnHaNsJt7XQCJsM6TiVG7q-UU8V4T4YzSMg3W80CBm15YuRVgAphLdq8v36NJBUjnMtiQql0G0xBJdHUrWBke1bzJArdbq4ICly2pKrKVLYzGBYVngHh1XDDUAfGwSiFrayguhU-5EUvEvHK2RPKYfcihbDXjVGCZhetZbFK2GZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی SIMORGH VPN؛ کلاینت چند‌موتوره اندروید برای شبکه‌های محدود
برنامه
SIMORGH VPN
یک کلاینت قدرتمند برای اندروید است که اختصاصی برای اتصال در شرایط اینترنت ملی، محدودیت‌های شدید و اختلالات بین‌المللی طراحی شده است.
⚡️
نکات و قابلیت‌های مهم:
🛰
حالت MSP:
اتصال ویژه در شرایط اینترنت ملی و اختلالات شدید شبکه.
🧩
فرگمنت (Fragment) پیشرفته:
قابلیت تنظیم پارامترهای فرگمنت برای عبور از فیلترینگ و بازیابی آی‌پی‌های کلودفلر.
🟣
پشتیبانی از NipoVPN و MasterDNS:
امکان وارد کردن لینک‌های
nipovpn://
و مدیریت کامل مسیرهای DNS.
🛡
سیستم هوشمند:
استثنا کردن خود برنامه از تونل VPN (برای جلوگیری از لوپ) و پشتیبانی از پروکسی‌های محلی SOCKS5/HTTP.
🔗
لینک پروژه در گیت‌هاب
🔍
لینک اسکنر پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2798" target="_blank">📅 20:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgOc11B-r2RievBXc38aJ74emOVqlzhAt9e-R1VAiTWlEwQgVqCLMRq7yEoQ4OgFb7a7ayJq7_ahbr1UntxsG5Sd-cywEY9f08abwcMQs1Gjq5R8hZFoJ010Y4p_1y310owUp1a5W9XChKA4-b6z-AOGA1IxpF8Zw-cVhKncgMCsDkg0OtZu-CtiEiZ6SRcWy4rfkwYzxVqa9ah85ZDqxDkGP7HTm6aB5kSpq73tWJGtEE-JtNhIhACS7-qiZ_sHbWgu0YJV5dgHHp75bQVdDsI3QsY9RUWRC9JSax6TE5Ye3lePNY7PVHvPZ3jLovGkMn4BlzHjDOzM8FeJO-OASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رخداد امنیتی در Hugging Face: سرقت دیتابیس و کلیدهای دسترسی
پلتفرم
Hugging Face
(بزرگ‌ترین میزبان مدل‌ها و دیتاست‌های هوش مصنوعی) وقوع یک رخنه‌ی امنیتی گسترده را تأیید کرد.
در این حمله، مهاجمان با بارگذاری یک دیتاست مخرب و سوءاستفاده از یک آسیب‌پذیری، موفق به اجرای کد روی سرورها، ارتقای سطح دسترسی و سرقت دیتابیس‌های داخلی و کلیدهای دسترسی شدند.
⚙️
جزئیات و اقدامات انجام‌شده:
🔐
ابطال کلیدها:
هاگینگ فیس تمامی کلیدهای دسترسی افشاشده را باطل کرده و از کاربران خواسته سریعاً کلیدهای امنیتی خود را بازنشانی کنند.
🤖
تحلیل با مدل بومی:
برای بررسی لاگ‌های حساس سرور، از مدل زبانی بومی استفاده شده تا نیازی به ارسال اطلاعات به سرورهای خارجی نباشد.
⚖️
پیگیری قانونی:
موضوع به نهادهای مجری قانون و تیم‌های جرم‌شناسی سایبری برای بررسی دقیق‌تر ارجاع داده شده است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2796" target="_blank">📅 18:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkTLvyr0QPkgYf6xv5qyMKZ7sJoAvYhof7Icu0W9-X3_hhwiGw8wTPQHWmWQ4KUkDnjyobtiIcqJOEYuM_MBvwi0ugocMo5UY_I8qK8GJ15em8EikTFyanfpCqsgQDodl11gPrn4kd1x5Ci0NQYlKeuZH5Rd55DpT6WeYVIXbwMTSKuLo4xJJJA8NX2rLGYzGuy6lPRq7XTGkDDuHcgbtRTdIlqaKIbvOtKYxxSQzkQsTC9lV9bDUl2wa0uBBHVP23yvblKvgA7kCxZ9vtlKVKoFMHEoFdiuxaloofwIXvijC_gtiHevtpxE49o-4Fyz-9wRg-V1V3MOF-Y6yBha5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت جدید پروژه iran-dev-tools؛ ابزارهای جدید برای رفع تحریم
پروژه اوپن‌سورس
iran-dev-tools
که مجموعه‌ای از اسکریپت‌های هوشمند برای حل مشکلات روزمره برنامه‌نویس‌ها توی شبکه ایرانه، آپدیت شد. برعکس لیست‌های ثابت میرور، این اسکریپت‌ها سیستم‌عامل شما رو تشخیص میدن، گزینه‌ها رو بنچمارک و تست می‌کنن و بهترین تنظیمات رو اعمال می‌کنه.
توی آپدیت اخیر، ۳ ابزار جدید به این مجموعه اضافه شده:
👇🏻
🤖
اسکریپت android-fix:
تنظیم و بازگردانی هوشمند میرورهای
Gradle
،
Maven
و
Flutter
برای ویندوز و لینوکس (حل مشکلات برطرف‌نشدنی توسعه‌دهنده‌های اندروید).
🔄
اسکریپت proxy-switch:
تست و تنظیم مجزای پروکسی برای تک‌تک ابزارهای روزمره توسعه‌دهندگان روی ویندوز و لینوکس.
📦
اسکریپت pkg-pack:
باندل کردن پکیج‌های APT، ایمیج‌های داکر یا حتی خود Docker Engine روی سیستم آنلاین و نصب کاملاً آفلاین روی سیستم‌های بدون اینترنت یا دارای دسترسی محدود.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2794" target="_blank">📅 20:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2XsFYSZEVEczfzvFehkWrkDYuE7CXa0mzhdWuq9GvQ-CopazubREAJgumxfd6r-Vut5eVk7JaF3MaoY8EC2L24ac6VEyD5Z95duE8g5uFZH_DRWI18NlnwBlWo93yj02UK7OOiPy9anWFOWA_7SuBoKmLNto2SCzcpowqbjp-_rXNxJgZEOeOAVAMS4vHvaCLkDtjmk9czW9VzMDd0klq39oWtp8xU-fBsXRb28LNQ8twyRkhsP5P0ahD_xy3FLUQiOM7CMlwf199Kw7Az2coK8Hvle_oI7_X6Aw5k7d7j0sqFIrYBpwox9xlX0sXsC74QsCI6_VQHr3bs-Ce16Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش استفاده از TOR در سرور ایران یا خارج (دسترسی به لوکیشن های مختلف در X-UI)
ما حدودا 2 سال پیش همچین ویدیویی رو ساختیم و پروژه ای که توش آموزش دادیم حذف شده به اسم torsina و البته پروژه های مختلفی بعدش ساخته شدن مشابه این پروژه که یکی از اونها رو زیر معرفی کردم.
🔗
آموزش ویدیو این روش
👈🏻
اسکریپت Tor automate
(مشابه پروژه torsina)
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2793" target="_blank">📅 18:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdkPqXwhCjRq03qoOegG5se5X2Er22NWZ1HJRfmejdKFDxj5v31adRDwvFwMMZerQnVc7dKmyyO-9lPL6dUVVygo1p3X32-6E_DQwjLThI3JYnTWiqfKb2evH6BGONTPL6O_H7tQhyn92vSIFF0lgYUn200pHtv5jWXkJzu0uvdaCoRxNA98knVW7NkLIOrxNuZ5N5QIBboKcs0pGW8tZvb0iGG7m0XAVym06xW5tCb2ofEDe91HzCc8QoFBF68ZJ_BXTMmTXhnR8E00vIrFydcaU_9XHpRuMDumQkMOnznnCl_RgCY5c0tCLYXTmyXI4KlREDMZIOf_7q_yA-dybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح...</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2792" target="_blank">📅 16:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2790">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX0ygWoWbDXxwfEbgxMuAelon4zJp8OlrXALXqg11YgWT3RCrQNb9JI9CaDihexi-NsIAnfOL04N1SO6VR8MixBjcZ5259RvBcNXzXl_TncnCU1AXTL1UjMw3IAyPBOdsAptJhPy3n1lBoer7CK3UKhpASIAVPLbpscJ2k44xbhKMNCXk6gyf-1ChZNvEJsRyqK0WQFP9mKO66-fk8cAdwOvCz4TL4y9yn7odXcJZL_8VfI5zV-btnYTchJrFdumvF9I9MCilYzNJwFe-_1CR4beHK9qA3jyL5bOmPdE3cVuFEhx4xg7eqC_iqZDIciyj_GVVHJkFIGb7jkEH2ul7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت کد ۲ مرحله‌ای بدون نیاز به اپلیکیشن با پروژه 2FA
اگه دنبال یه جایگزین شخصی واسه اپلیکیشن‌های Authenticator هستید، این پروژه اوپن‌سورس که روی ورکر کلودفلر (Cloudflare Workers) اجرا میشه فوق‌العاده‌ست. این ابزار بدون نیاز به سرور یا دیتابیس، کدهای ۶ رقمی TOTP رو با امنیت بالا مستقیماً داخل مرورگر جنریت می‌کنه.
⚙️
ویژگی‌های کلیدی:
⚡️
سرورلس و سریع:
دپلوی چند ثانیه‌ای روی شبکه جهانی کلودفلر بدون نیاز به VPS.
🔒
بدون ذخیره داده:
ساختار مستقل بدون نیاز به دیتابیس برای امنیت بیشتر.
⏱️
استاندارد و هوشمند:
تولید کدهای امن با آپدیت خودکار هر ۳۰ ثانیه یک‌بار.
💬
پ.ن:
با اینکه پروژه کاملاً اوپن‌سورس و امن هست، پیشنهاد می‌کنم برای اطمینان کامل خودتون، کدهای سورس رو بدید هوش مصنوعی تا براتون بررسی و آنالیز کنه.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2790" target="_blank">📅 21:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2789">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029b77ae2.mp4?token=hOqxZ4E1vVR9i3NB_hTpIEnVXcexoKP6HEMjdZ5zaaF7hZ_ee8DPwvFvpnw75qpwgkNLurZKM6Z0eUfBkGiu59STV3Im0-A2O3_RfvPlgpKQAUDldtmg4YSoVWA3rbgAMISs2zfJwlCcXKaPywy-atruqZXXIwRoRDjtnKrG33NJqF2o9Kkn_zWBNOG-011-nQWa-RzwcjaeSW2ZX0mZFuMmLerJ-DRoWzinTCEjQUBcxn5KMCoDWc0G8eb_ajeydENaLyqeEGHvmowc33PSA9Pw2w_hqIw0OlVzGmozLp0J5SIfdnlfzRu5hpAi2PJkyEQUVx7GEYETyFFWCAwZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029b77ae2.mp4?token=hOqxZ4E1vVR9i3NB_hTpIEnVXcexoKP6HEMjdZ5zaaF7hZ_ee8DPwvFvpnw75qpwgkNLurZKM6Z0eUfBkGiu59STV3Im0-A2O3_RfvPlgpKQAUDldtmg4YSoVWA3rbgAMISs2zfJwlCcXKaPywy-atruqZXXIwRoRDjtnKrG33NJqF2o9Kkn_zWBNOG-011-nQWa-RzwcjaeSW2ZX0mZFuMmLerJ-DRoWzinTCEjQUBcxn5KMCoDWc0G8eb_ajeydENaLyqeEGHvmowc33PSA9Pw2w_hqIw0OlVzGmozLp0J5SIfdnlfzRu5hpAi2PJkyEQUVx7GEYETyFFWCAwZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی!
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده یک اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
آقای حمزه حوتی عزیز، مبارکتون باشه!
✨
آقا حمزه لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
اصلاً فکرش رو نمی‌کردیم این‌قدر حمایت کنید. حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2789" target="_blank">📅 20:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQstyNZ76tUtH6rKNuOIDyR6oux65WAYZgn85mx1o-IU2Si9CGSZitISLISSME4ZPfmI-J1dDcr2evp3g7KtTnVbMGtqMJYZqMRFRW6RutjOKKg1U-oKOwveRL6Q3zBm_E3_iWajHLhxkaGUx13njr81MSLF4Su_38FXDFXU_sNV6JgYrwf4gPMdVtAyFOHZfVLvkQ6njqgoenCMIr-wJWB0rNdo8hPIgQSTq6Ve-AYGZxmqMPcYHEcGgcpJjxwpOFIR2pSWfHW9Xa25XdSWHjT83xudfwH-1ruJq_LDx5pRBKIj62gge6hVFsHzvv2iYG7tYkz-HjcYfeICFS4nPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
حل مشکل تایپ اشتباهی با کیبورد فارسی و انگلیسی در ویندوز!
مطمئناً واسه شما هم پیش اومده که کلی متن رو تایپ کردید و بعدش تازه متوجه شدید کیبورد روی زبان اشتباه بوده و کل متنتون به زبان عجیب و غریب یا برعکس چاپ شده! نرم‌افزار رایگان و سبک
LangOver
دقیقاً واسه حل همین روی اعصاب‌ترین مشکل ساخته شده.
کافیه متن اشتباه تایپ شده رو انتخاب کنید و با کلیدهای میانبر زیر، تو کسری از ثانیه درستش کنید:
👇🏻
🔄
کلید F10 (تغییر زبان):
اگه حواست نبوده و فارسی رو انگلیسی تایپ کردی (یا برعکس)، متن رو انتخاب کن و F10 رو بزن تا سریع درست بشه.
⬅️
کلید F6 (برعکس کردن متن):
کل متن یا کلمات رو به‌صورت برعکس چیدمان می‌کنه که واسه کارای خاص یا رفع به‌هم‌ریختگی متن‌ها خیلی به کار میاد.
🌐
کلید Ctrl + T (ترجمه سریع):
متن رو انتخاب کن و با زدن این میانبر، مستقیم اون رو از طریق مترجم گوگل به زبان دلخواهت ترجمه کن.
و چند قابلیت دیگه همه به صورت رایگان.
🔗
لینک سایت و دریافت برنامه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/iaghapour/2788" target="_blank">📅 20:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2786">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان این همون آموزش هست که زیاد درخواست میکردین.
👇🏻
🔹
آی‌پی خارج فیلتر باشه مهم نیست.
🔸
سرور ایران تا حدود زیادی ضد اکسس شده.
🔹
تانل ریورس هست با کمترین اختلال.
🔸
سرعت بسیار بالایی داره.
🔹
مصرف منابع کمه و چندین سرور رو میتونید تانل کنید با هم.
همه این موارد در
آموزش بالا
قابل پیاده سازی هستش.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/iaghapour/2786" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2785">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RatholeEngine Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">356 B</div>
</div>
<a href="https://t.me/iaghapour/2785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
تانل ریورس روی سرور با آی‌پی مسدود
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/iaghapour/2785" target="_blank">📅 19:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2784">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7RF52VItm-DPbp5xBquogZ3fmTEP08BqoWlDyIwTWxb8XkvBkwdm6x2eWWketSn0mvf9RaAKOJwrqwJR82KeNr6BYOZjg_3073r2kID68Pt0UX-JA7Bq1aW-T0477CflsKHIYuym4u-BfD-exKXkJfvF1i9Sv8KTeq-HrwI_T28ffbGoBojUjmL0IQuc_qnvKpGxjytup7ICAwxmLnHvcIZRS0iUYbNs8m3x4MQa_A_o-2vj_NQ7hIIsurT8Ytyh3ZosSPUETJuQabmakDNDtWYEunmdz40Ld6f40oCIm_HZtX45Putxyl8C_jJkATZgcya0fc2kk_VXZMwSft_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل ریورس روی سرور با آی‌پی مسدود (مقاوم در برابر اکسس)
🔹
حتماً براتون پیش اومده که آی‌پی سرور خارجتون فیلتر بشه، یا سرور ایرانتون خیلی زود اکسس بشه، یا اینکه بخواید چندین سرور رو به صورت همزمان با هم تانل کنید. حالا با استفاده از تکنیک تانل ریورس می‌تونید تمام این کارها رو به راحتی و با کمترین میزان مصرف منابع سرور انجام بدید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#ریورس
#اکسس
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2784" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2783">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
تعداد 116 دکل مخابراتی هرمزگان از مدار خارج شد
🔹
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔸
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که تلاش برای وصل‌کردن آنها در جریان است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/iaghapour/2783" target="_blank">📅 15:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2782">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚠️
دیتاسنتر ها دوباره اختلال خوردن متاسفانه.
حالا معلوم نیست برای یک سری دیتاسنتر محدود این اتفاق افتاده یا برای همه دیتاسنتر ها.
ولی طبق تست ما آپدیت پکیج ها و گرفتن سرتیفیکیت و کار با داکر دچار مشکل شده.
🔻
در حد توان آمادگی داشته باشید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/iaghapour/2782" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2780">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alC8IX8YVsC1oSAGfMd-nBAm6IwuXW6TEyWDnMNmAnlBkfoKBBFVMe0jmZggd-_otllMWZnn8Gu7kOFe6CUTkgt5ZEN_570xFH9qoaZIau1usqTrFcWftshapPOxGGToQZGAF_BFihAlSpF1uvDtxdOMZKI7pAtmWSMFWX29KGPb-UWD618pS1aax_VBg9_ztnjK7B06W3MHWTcjKWG40PKVJDlIcXKcwY5je2OsEZvVhUNPIFoMYQTuStxplQxYMczuTt_Yoqj74u2Lxt7vaFpG3GQ8QIrYnl51_sJupeRgoIwkhICv3Rb6YNWqvJCBUfOXZ5cOXJCZeGMJQ4WvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
قرعه‌کشی ویژه اعضای کانال!
رفقا، برای قدردانی از همراهی شما یه قرعه‌کشی جذاب داریم!
🎁
👇
شرایط شرکت:
کافیه فقط زیر
آخرین ویدیوی کانال
یه کامنت بذارید.
🏆
جایزه:
اکانت هوش مصنوعی 1 ماهه (Gemini یا ChatGPT به انتخاب ما) برای برنده عزیز!
⏳
زمان قرعه‌کشی:
همین فردا! پس تا فرصت هست کامنتتون رو ثبت کنید.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/iaghapour/2780" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2779">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
آمریکا با تحریم‌های جدیدش، صدور گواهی امنیتی (SSL) واسه سایت خبرگزاری فارس رو مسدود کرده. این کار باعث شده دسترسی کاربرا به سایت مختل بشه و اخبارشون هم کم‌کم داره از نتایج گوگل حذف می‌شه.
پ.ن: من می‌ترسم فردا روز اینا واسه جبران بیان سایتای ارائه‌دهنده گواهی مثل Let's Encrypt و اینجور چیزا رو تحریم کنن و کلاً همه رو به فنا بدن!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/iaghapour/2779" target="_blank">📅 16:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU9ChfHU_jNQ88IuPYGZQFgfUarFEtU4imDaQPARWVY6SY-WUx0asNOnwY1f1ArDTo-Dkti_tVtqCJZhOgbI-bhrskcu0C_LQXUOvupYqQsCIY6PYQoDjkAqqlnaD2d95GyLHe07OxftC6oigfPTRppPYccxmiCIQ6JHSYQtbvy55E5b_hlb2KIK4bp02tlTQsG-iEVLebsTIqXJ5wLwvjswnq6ihTPDdpbj0YVGzj5S9zKxYXh2_FwYCd3hy0Y6iKWyhHHVMFFe2-ODPaHolEUy1MBOfGjGegr_3ha_8IkJEmjpAMsiYttaC7UB35UwROSd11-D_o_VcHck5dSb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره یه روز لو میره که مسی اصلاً آدمیزاد نیست!
یه فضاییه که اومده زمین تا کلاس درس فوتبال برامون بذاره و برگرده سیاره خودش :)</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/iaghapour/2777" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2776">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🟢
بچه‌ها، یه سری از دوستان پیام می‌دن و می‌گن «سرور خارج گرفتیم ولی پینگ نمی‌ده و نمی‌تونیم بهش SSH بزنیم، پس خرابه یا به کارمون نمیاد.
یه نکته‌ی رو یادتون باشه: اگه قصدتون تانل زدنه، در بسیاری از موارد مهم نیست که بتونید بهش SSH بزنید!
مهم‌ترین چیز اینه که
سرور ایران شما
بتونه سرور خارج رو ببینه، بهش دسترسی داشته باشه و پینگش رو بگیره.
👌
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/iaghapour/2776" target="_blank">📅 20:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2775">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دیگه واسه چی غصه بخوریم؟ از اینکه حتی نمی‌شه یه آینده‌ی خوب رو تو ذهنمون تصور کنیم؟ از اینکه هر روز باید با قطعی برق سر و کله بزنیم؟ از اینکه وسط جنگیم؟ یا از اینکه تهش قراره آرزوهامون رو با خودمون به گور ببریم؟
🖤
خدایی دیگه چه انرژی و انگیزه‌ای واسه آدم می‌مونه؟ اصلاً نمی‌خوام نق بزنم یا فاز ناامیدی بدم، ولی واقعاً یه جاهایی آدم کم میاره و رسماً می‌بره... کشته شدن این سربازهای بی‌گناه هم که دیگه مثل یه تیر وسط قلب همه‌مون بود. آخه چرا باید پژو پارس بشه آرزو؟ چرا باید یه ۲۰۷ مشکی بشه سقف رویای یه جوون ایرانی؟
😔
خدایا... فقط بزرگیتو شکر.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/iaghapour/2775" target="_blank">📅 19:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2773">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeM-leRE8c9xChAK0R7axK-5SOb3cbrLyHDEFC5MVpNvi1ZETUX49-6kN1pRmIvZje2xxRgU7n72jiVkn4vn3mHNT1qKnLQ7fevODauvqqy-23V7hZI6UxrbUCNCyxmxwyULBmG0QA0jDySAsgbTag1fLQUIC1db9E1BsYNhVOsxxNmD0Mq37BCOk0rZvHr8SziDFVwmsdrz8PHE1u30RRo_zay8vrIfEEJ7F-RncXnuKRHhpbTJ3lfk2MWT8qjkW-2O-sHhG2_tzu2r_EGlxzou7DTjFmJI_Zbo_cMVfCBdnKL5P88D6D22BIBsWZzPg6Cv7wzEk9q5WSyR5FjojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دور زدن رایگان فیلترینگ در ویندوز
با
UAC SNI Spoofer
🔹
اگه دنبال یه ابزار بی‌دردسر و قوی واسه ویندوز هستید، این برنامه که با هسته Xray و متد SNI Spoofing کار می‌کنه یه گزینه فوق‌العاده‌ست. این ابزار با مدیریت هوشمند مسیرها، بهترین و پایدارترین اتصال رو براتون ردیف می‌کنه.
⚙️
قابلیت‌های کلیدی برنامه:
📱
دارای حالت‌های اختصاصی همراه اول، ایرانسل و حالت هوشمند Auto.
🔍
تست و رتبه‌بندی خودکار SNIها و Edgeها برای پیدا کردن سریع‌ترین مسیر ارتباطی.
🚀
مجهز به سیستم شروع سریع TLS برای همراه اول و قابلیت «گرم‌سازی مسیر یوتیوب» برای پخش بدون بافر ویدیوها.
🔒
تنظیم خودکار پروکسی سیستم
🌐
با قابلیت App Bypass (عبور برنامه‌های دلخواه از پروکسی) و نمایش لاگ زنده.
🔻
برای کارهای حساس استفاده نکنید.
🔗
دانلود از گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/iaghapour/2773" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2772">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucm829yDHnH3gi_7gNkCdaZl4NNDTddjUnkXV4LOPC4jy8NEvBEL4eZWAhXWwgExdxxsnML0weL5o2zOSOudw8m6J3hMg6m8qZ9ml-3hVrjOCi9v7aBS4aeTrX5thHXnf6_5VFObiBMtC8rI3-kuXI4Ldrq6WR5tveKj4Qb1PlLJXrIyJTG9fxnyXsZ5LLDMnaJ61bylocuS7qHNA7KVc70EOrXE27K7s80ypRZYpniaEBAJCZOp1sn1QHXG8_R0BadGTGzzOEgshHOX5yRiNRqYubLSFd6mJpL9xQHuAlYRbzNx8hvLt6Kiw1k4eM9cD2bpsByYIoWahY4Z0HLgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
انتقال بی‌دردسر پنل 3x-ui بین سرورها با پروژه 3xui-mover
اگه تا حالا مجبور شدید پنل 3x-ui رو به یه سرور جدید منتقل کنید، حتماً می‌دونید که روش‌های سنتی (مثل کپی کردن پوشه‌های x-ui و cert) همیشه جواب نمیده؛ مخصوصاً اگه دیتابیس شما روی حالت PostgreSQL باشه، پنل تو سرور جدید بالا میاد ولی کاملاً خالیه!
⚙️
ویژگی‌های اصلی این ابزار:
🔸
پشتیبانی PostgreSQL و SQLite
🔹
بکاپ دیتابیس، تنظیمات و SSL
🔹
انتقال خودکار با SSH
✅
جلوگیری از ریستور اشتباه
🔸
بررسی صحت انتقال و لاگ کامل
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/iaghapour/2772" target="_blank">📅 20:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2771">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1CxJlNO4zTAzS1i96rpq-a0ULnD3FY4KznlpSSpQ8MPTTggGVT_UnQL-7IJwNisK6scTrhrHB0RQzfsccfFeQzjnQ0KzfMzBypl3KYhYoU2NkusSERkqAGr5oA8TX8jDD-RuOPkcecnHWTkTeyh-rPF-wKCqh7EWOtbZki9oy8lAyMgE2Z4W5l-DEGAEZbaxBVOhwQmgvAbEnIro8evzlXnKMYe4pkkJE9KAAmPESIE_WbyWe35hoZz6ABk9ku3f869o_FZkfXTW2y6R2e78WNbgp-G30If9rpSGEwTkI6tsJtZqkie90CDdDgIQe5gEBShNXxdMM_RiAwHWVqygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
توجه! مراقب کلاهبرداریِ فروش پنل‌های رایگان باشید
دوستان عزیز، با توجه به پیام‌ها و درخواست‌های متعددی که از سمت شما دریافت کردم وظیفه خودم دونستم که یک اطلاع‌رسانی مهم در مورد سوءاستفاده‌های اخیر داشته باشم.
متاسفانه اخیراً دیده شده که عده‌ای افراد سودجو، پروژه‌های کاملاً رایگانِ دور زدن فیلترینگ که بر پایه ورکر کلودفلر ساخته شده‌ را به عنوان سرویس‌های پولی و اختصاصی به کاربران می‌فروشند!
ابزارها و پروژه‌هایی مثل:
👇🏻
پنل BPB
پنل نهان
پنل نوا و...
🔹
تمامی این روش‌ها توسط توسعه‌دهندگان به صورت
رایگان و متن‌باز
منتشر شده‌ تا همه بتوانند به سادگی به اینترنت آزاد دسترسی داشته باشند. فروش این پنل‌های رایگان نه تنها یک کار کاملاً غیراخلاقی است، بلکه سوءاستفاده مستقیم از عدم آگاهی کاربران و بی‌احترامی به زحمات سازندگان این پروژه‌هاست.
✍🏻
هدف ما از انتشار آموزش‌ها در این کانال دقیقاً همین است که یاد بگیرید خودتان به سادگی و به صورت کاملاً رایگان این ابزارها را راه‌اندازی کنید. هیچ دلیلی وجود نداره که بابت یک کد رایگانِ کلودفلر به کسی هزینه پرداخت کنید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/iaghapour/2771" target="_blank">📅 15:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2769">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbzvYBtwmx8qsD57w1YkD0Ry_RblWemPNDytYhMhuG45sp35x_gCRgzZLXZRG3X1RQakvyOxZh4Jg6BAyHsBRWXYDupEOAC2TyugyQjhPfZV2vd2W8ykoMqFZoZ0tEG-T-3rxpW57L-I2ttAL5fStQzEpmXmDAlvM6FS0UKzAWxvar4KQAzY1B8hNrFNJUM4x2sVip75kvFUnOftDZZmTK9l2oMpNakJLcxLD3jBQC1wHfbl0MqSuZSr0dXSstBzPQo71ruA0oVO34pb3vLz6uO2Ke2ttJ2l_nHw1eRhaQtwc09Rmy1k3llkIwpjbKK4Qa189wTkRfPcYrxU4ylZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازگشت بانک ملی به مدار اصلی؛ صادرات و تجارت هم به‌زودی
بانک ملی از امروز بالاخره به زیرساخت اصلی برگشت و سرویس‌هاش پایدار شد. بانک‌های صادرات و تجارت هم قرارِ ظرف چند روز آینده به این بستر اصلی منتقل بشن تا مشکل قطعی‌شون کلاً حل بشه.
این اختلالات طولانی‌مدت که از اواخر خرداد شروع شده بود، به خاطر حملات سایبری سنگین و پیچیده بود که تو این مدت با کُر پشتیبان مدیریت می‌شد. در ضمن بانک مرکزی اعلام کرده چک‌هایی که تو این مدت فقط به خاطر این خرابی‌های فنی پاس نشدن، هیچ تاثیر منفی روی رتبه اعتباری مشتری‌ها نمی‌ذارن.
💬
پ.ن:
البته با وجود این خبرها، هنوز یه سری از کاربرها میگن بعضی تراکنش‌ها مشکل داره. از اون طرف هم انگار کلاً بخش وام رو بستن؛ یعنی مردم این‌همه سپرده گذاشتن به امید وام، ولی حالا که می‌خوان اقدام کنن جلوی وام رو گرفتن.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2769" target="_blank">📅 21:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2768">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YblVgXWMyv_QtFK3Pg5Di9QmXIcpbHV48bI77WmLmVPz9EWt_fjVskfDyIabvU1YRD4vwk84ApqC7A84F4eAhIXuJf1xJ6SZ44eUYdFaNiS7rktj7NsHpG67TYXpNuaowcEhcsOsY59a1RIBDCaj27bXLlcO8BOY7hTbvPyx6vlGBTTaly4zWwIHolModlaziwisuwVGPJ5YhR_bRkfiWuv7GQ6OmWNoToxSIUqHkztGcWCJHqakkJ5tmqYcT7ZvC-TGeziMENQcjVAwOGUgwdTYseBA58l15iY7HQLHoLCTJSIYIR2z-BratGsT6A1gbCx7YV3-cDQl0BSst-ElaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دامنه t .me تلگرام دوباره برگشت
امروز دامنه معروف
t.me
(لینک‌های کوتاه تلگرام) ناگهان از کار افتاد! این دامنه توسط رجیستری کشور مونته‌نگرو به حالت تعلیق درآمده و از کل سیستم DNS جهانی پاک شده بود؛ آن هم در حالی که دامنه تا سال ۲۰۳۵ تمدید شده بود.
گزارش‌ها نشان می‌داد که این مسدودی به دلیل تحریم‌های وزارت خزانه‌داری آمریکا رخ داده بود.
🔻
این دامنه مجدداً
فعال و رفع مسدودیت شد
و اکنون تمامی لینک‌های کوتاه تلگرام بدون مشکل کار می‌کنند.
©️
Behrad Javed
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/iaghapour/2768" target="_blank">📅 19:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2767">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxpIUNMBfqEnYJFW41DsWR5a3E9kyn0L766i8o9cJ-dZQJreK5O87n_rZ8UczzUNK_TzNGgFewhiYiXyP1gh_uPZJkpCMxFC6mJ4OD5jb4_K2pj4tDem9nvj60BwcWDaNC0BI59-zJftmz9Yd1JFICIjd8W3XzWoDS2kJ7MXk-VSTQixjTvSKzVGkLbTuRvA6QfrFpP7BeQF5hgldX6EAIbNhS_WJ7TY5SGDY2g8F_-_-JzgHWxdN_7gig_m4m0LvMer9WHeSe96-XKKaasV80nLapB2UiYopSI89vILmgouGS1uxoVsHmaU89t2O33cGbYUqcNN2t8flnl5-wPbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بعضی از بچه‌ها خبر دادن مثل اینکه کج‌دار و مریز
IPv6
روی یه سری از اپراتورها فعال شده. البته هنوز دقیق مشخص نیست که این داستان موقتی و بخاطر اختلالات شبکه‌ست، یا اینکه واقعاً خبریه و دارن یه کارهایی انجام می‌دن.
🔻
از اون طرف هم عده‌ ای از دوستان از جنوب کشور پیام دادن و گفتن که اوضاع اینترنتشون خوب نیست و قطعی و اختلال شدیدی رو دارن تجربه می‌کنن.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/iaghapour/2767" target="_blank">📅 13:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ild7OBira4GlBLiJ20bMtVshuvkkgxmvWMTStww8jEio-GkRFGDwwuXY1XAaf01Ee7ulxR6exCHMjl0sdg4NwQl98QcOObyDNzcbxd0nlBCyzlz83vnGuo1p-OGVN5hp4YHkA3yTv43ZT8DktyDmgLwP9rKNbxboo_hP7ANO-rt6e13ccOeANR852b1WDW331_jDPgYGAOi8RtzDWvvQhb66hhAoYOPJkUp1DLNRFAUHfXn3LjdX6wqURK5GQ91Yo8-TSKVGodwRGeGkbuU5tLi6NUIOKm5LwqeOZn2ObBUiz4BnBqPIhWLDhDWzsFeCe8u-dpEoXP9enFROyDGGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل معکوس با انواع پروتکل (BackPack)
🚀
🔹
در این ویدیو به آموزش صفر تا صد راه‌اندازی تانل معکوس (Reverse Tunnel) بین سرور ایران و خارج می‌پردازیم. اگه به دنبال روشی هستید که ترافیک شما را شبیه به وب‌گردی عادی کند و کمترین ردپا را برای سیستم‌های محدودکننده به جا بگذارد، این آموزش دقیقاً برای شماست.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#ریورس
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/iaghapour/2765" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">متاسفانه به بیشتر از ۱۰ نقطه از کشور حمله شده که بیشترینش سهم بوشهر عزیز بوده.
💔
شاید خیلیا در نگاه اول بگن خب مناطق نظامی بوده و به مردم عادی آسیبی نرسیده، ولی واقعیت اینه که پشت پرده یه اتفاقایی می‌فته که آدم تعجب میکنه از شنیدنش!
مثلاً امروز یکی از بچه‌ها می‌گفت توی شرایط جنگی، حتی اگه اینترنت هم قطع نشه، کلی از فروش‌های ما کنسل می‌شه؛ چون مشتری می‌ترسه و فکر می‌کنه مثلاً ما که از جنوب آنلاین‌شاپ داریم، دیگه نمی‌تونیم بار رو برسونیم تهران یا شهرهای دیگه...
خلاصه که فقط بحث قطعی اینترنت نیست که به کسب‌وکارها ضربه می‌زنه، خود جنگ، ترس از خرید و این ریسک‌ها هم کلی به مردم آسیب می‌رسونه.
دمتون گرم تا جایی که می‌تونید از این کسب‌وکارهای بومی حمایت کنید. قبل از اینکه نگران بشید و عقب بکشید، اول با پشتیبانیشون هماهنگ کنید؛ چون توی خیلی از همین شهرها و استان‌ها پست و تیپاکس دارن مثل قبل کارشون رو انجام می‌دن و جابه‌جایی بار بسته‌ نشده. پس با خیال راحت می‌تونید از این آنلاین‌شاپ‌ها و سایت‌هایی که توی این مناطق هستن خرید کنید.
🤝
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/iaghapour/2764" target="_blank">📅 16:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2762">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/iaghapour/2762" target="_blank">📅 21:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سلام بچه‌ها. یه مدتیه دوست دارم واسه تشکر از اینکه هم تو یوتیوب هم تلگرام کنار ما هستید، ماهی چند بار یه هدیه کوچیک بهتون بدم.
👇🏻
به نظرتون چی باشه بهتره؟
🔹
اکانت هوش مصنوعی
🔸
کانفیگ فیلترشکن
🔹
پول به صورت کریپتو؟
البته این وسط دوباره درگیری‌ها زیاد شده و فقط امیدوارم باز قطعی اینترنت شروع نشه که تمام انرژی و وقتمون رو بگیره :(</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/iaghapour/2761" target="_blank">📅 21:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/iaghapour/2760" target="_blank">📅 20:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❓
سوال یکی از کاربران:
من یه سرور دارم رو همراه اول فوق‌العاده عالی کار می‌کنه اما رو ایرانسل نه. چطوری می‌تونم بفهمم مشکلم از کجاست؟
💡
پاسخ و بررسی مشکل:
دلیل اصلی این اتفاق برمی‌گرده به تفاوت سیستم‌های فیلترینگ (DPI) اپراتورها. تجهیزات و محدودیت‌هایی که هر اپراتور اعمال می‌کنه با بقیه فرق داره؛ در نتیجه یه کانفیگ یا پروتکل خاص ممکنه روی همراه اول عالی باشه، اما روی ایرانسل اختلال داشته باشه یا اصلاً وصل نشه.
به جز این مورد، چند تا دلیل مهم دیگه هم وجود داره که باعث این مشکل می‌شه:
👇🏻
📌
وضعیت آی‌پی سرور:
خیلی وقت‌ها آی‌پی یه سرور روی یک اپراتور خاص شناسایی و محدود (کثیف) می‌شه، در حالی که همون آی‌پی روی اپراتور دیگه کاملاً تمیزه و عالی کار می‌کنه.
📌
مسیریابی شبکه (Routing):
مسیر اینترنتی که شبکه ایرانسل تا دیتاسنترِ سرور شما طی می‌کنه، ممکنه با مسیر همراه اول متفاوت باشه. گاهی شبکه یه اپراتور با یه دیتاسنتر خارجی به مشکل می‌خوره و باعث افت سرعت شدید یا پکت‌لاست می‌شه.
📌
حساسیت روی SNI و دامنه:
الگوریتم‌های تشخیص ترافیک اپراتورها با هم متفاوته. ممکنه ایرانسل روی دامنه یا SNI خاصی که برای کانفیگ استفاده می‌کنید حساس شده باشه و ارتباط رو همون اول قطع کنه.
📌
آی‌پی تمیز و شبکه توزیع محتوا (CDN):
اگه ترافیک سرورتون رو از پشت کلودفلر عبور می‌دید، احتمال خیلی زیاد اون آی‌پی تمیزی که ست کردید روی ایرانسل محدود و کند شده، ولی روی همراه اول هنوز جوابه. تو این حالت معمولاً با اسکن کردن و جایگزین کردن یه آی‌پی تمیز جدید مخصوص همون اپراتور، مشکل حل می‌شه.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/iaghapour/2758" target="_blank">📅 21:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قشنگ 2 ساعت با خودم درگیر بودم تا بالاخره حسش بیاد بشینم پای سیستم و کارای خودم رو انجام بدم. تا اومدم استارت بزنم، برقا رفت.
😁
دوباره این داستان قطعی برقا شروع شد. رسماً دهن سیستم و وسایل برقی خونه سرویس شد رفت!
🥲</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/iaghapour/2757" target="_blank">📅 21:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqiXX6V9HwX6JdiDAm6cEVqYSdiE52v0AVRiEFK7Ynq3Kzny9iU9KgL91U6uHr7mFR3zCoY61acJyFTkg8eToaMhw1o8L9NClys5FEHwylV6zaGC75MtlzCciOKiDs3ydLLS0CfH1RpBPZzwjninVhUqOAHRAg0ft9s6IwnwCUFi5BB2dLQgSBlqBlYXy2tab8iVAaaNuI9ybMsIm59iGzigZF1BnM6JVOMI21kiJfKNj_Ig3K-v-Gxmikl4C0cT6b22f36SE1ZUyWnrihlC3YWaSfTrO2F45xpHIMpsczz4DX-wL9haRAk21cQPyhiKmlSOHIb5bryWDO1Vh3R2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
دلایل ناکارآمدی و خطرات قطع اینترنت برای امنیت سایبری
🔹
توقف به‌روزرسانی‌ها:
آپدیت‌های امنیتی سیستم‌عامل‌ها و آنتی‌ویروس‌ها قطع شده و دستگاه‌ها در برابر هکرها کاملاً بی‌دفاع می‌مانند.
🦠
رشد بدافزارها:
محدودیت‌ها باعث می‌شود کاربران به سمت نصب VPNها و پروکسی‌های ناامن و آلوده سوق پیدا کنند.
🛡
بی‌اثری روی حملات بزرگ:
حملات سایبری پیچیده (مثل استاکس‌نت) معمولاً روی شبکه‌های ایزوله انجام می‌شوند؛ بنابراین قطع اینترنت جلوی آن‌ها را نمی‌گیرد.
🔌
اختلال در اینترنت اشیا (IoT):
دستگاه‌های متصل و هوشمند به دلیل قطعی ارتباط با سرورهای اصالت‌سنجی، از کار می‌افتند یا ناامن می‌شوند.
📉
بحران اقتصادی و اجتماعی:
قطع طولانی‌مدت اینترنت، زندگی و اقتصاد مردم را فلج می‌کند که این موضوع خودش یک تهدید بزرگ برای امنیت ملی است.
⚠️
خطر اینترنت طبقاتی:
تخصیص اینترنت فقط به عده‌ای خاص، باعث ایجاد شکاف در جامعه، می‌شود.
💡
نتیجه‌گیری:
به جای قطع دسترسی مردم، باید امنیت سایبری شبکه‌ها را تقویت کرد و در سیاست‌های فعلی مدیریت اینترنت تجدیدنظر اساسی انجام داد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/iaghapour/2756" target="_blank">📅 15:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2755">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2755" target="_blank">📅 01:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2754">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z99P_SFK8JnaZfX9u4TKhZ6M9Zo31rgH236R4PE6TxMYIAQ2_TxM0X19JhYOI9Z8vPvkn22KWwlPdobXjnWHvFJ72Y_P2mwDgCJi6BFsaajXbE46-HEHOmmRBu8ML_yuZ9mfZ1fYSyzW-8rBI9jBbKNRUMh7N1dGuknVxHk4yXTOCuiWzXwluVnGqpNrvBU3_a_LWZxAonEAQhBSHJ37_3DKBjrQoncGhb6LclMO43jr6zi-JPveNT8tRHjas5eCT5VAqsHN7jYGZs1uwocij1h1cwZuTKOBEIZR8nPoVgD4W38MKCbisovl0bwGOZx1beYB8jpUBggTA5M0vGYdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
قهرمان گمنام دنیای ویدیو؛ چرا VLC هیچ‌وقت پولی و تبلیغاتی نشد؟
🔹
بیشتر از ۲۰ ساله که پلیر محبوب VLC هر فرمت و فایلی که بهش دادیم رو بدون حتی یک ثانیه تبلیغ پخش کرده! دلیل این اتفاق شگفت‌انگیز، شخصی است به نام Jean-Baptiste Kempf که از سال ۲۰۰۳ به این پروژه پیوست.
با وجود اینکه VLC تا حالا بیشتر از 10 میلیارد بار دانلود شده، او پیشنهادهای تبلیغاتی چند میلیون یورویی رو قاطعانه رد کرد تا این برنامه برای همیشه کاملاً رایگان و بدون تبلیغ باقی بمونه.
🔸
اما شاهکار این افراد فقط به ساخت نرم‌افزار VLC ختم نمیشه! در واقع، تقریباً هر جایی از اینترنت که ما در حال تماشای ویدیو هستیم، روی پایه تکنولوژی همین تیم استوار شده است.
انکودر معروف
x264
که سال‌ها استاندارد اصلی پخش ویدیو در وب بوده و همچنین دیکودر
dav1d
برای فرمت جدید و بهینه‌ی **AV1**، دقیقاً دست‌پخت همین تیم و جامعه متن‌باز (Open-Source) است. غول‌های فناوری مثل یوتیوب، نتفلیکس و تمام مرورگرهای مدرنی که امروز استفاده می‌کنیم، همگی در حال استفاده از همین تکنولوژی‌ها هستند.
©️
behrad javed
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/iaghapour/2754" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
نوا کلاینت (Nova Client) منتشر شد!
از همین حالا می‌تونید کلاینت بهینه‌شده، و قدرتمند پروکسی رو با رابط کاربری اختصاصی «نوا» روی تمام دستگاه‌هاتون نصب کنید.
✨
برخی از قابلیت‌های کلیدی:
🔸
ظاهر مدرن و Dark-first:
طراحی چشم‌نواز با زبان بصری نوا و گرادیان‌های نئونی اختصاصی.
🔹
رادار نوا (Nova Radar):
اسکنر فوق‌پیشرفته و یکپارچه برای پیدا کردن سریع آی‌پی‌های تمیز کلاودفلر.
🔸
پشتیبانی کامل از زبان‌ها:
سازگاری بی‌نقص با زبان‌های فارسی و انگلیسی به‌صورت کاملاً راست‌چین (RTL).
🔹
مدیریت هوشمند:
دسترسی به داشبورد زنده، روتینگ، مدیریت پروفایل‌ها و سابسکریپشن‌ها.
🔸
قدرت‌گرفته از Flutter:
فوق‌العاده سریع، سبک و هماهنگ روی تمام پلتفرم‌ها (Multi-platform).
📥
لینک‌های دانلود (نسخه v1.0.0-beta):
🖥
macOS (Apple Silicon)
:
Nova-macOS-arm64.dmg
🪟
Windows
:
Nova-Windows.zip
📱
Android
nova-client.apk
🍎
iOS / iPadOS
TestFlight
🌐
وبسایت رسمی
📦
گیت‌هاب پروژه
نکته مهم برای macOS:
اگر سیستم بلاک کرد، این دستور رو در ترمینال اجرا کنید:
xattr -dr com.apple.quarantine /Applications/
Nova.app
👈🏻
نکته: Nova Client در واقع یک فورک بهینه‌شده از Karing هست که کاملاً با طراحی Nova Proxy هماهنگ شده و رادار قدرتمندش هم داخلش ادغام شده.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/iaghapour/2752" target="_blank">📅 21:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbY7kq9ATI0mWe_l0ZbSfEZ20fpzFwBTneqbjJKlLqXMVt3QUtuMi-s-QlJYNCh8ZJuxq1JBZezysJ3RXUHhuZgnvVuNlqIdxpuiPHbvccPhcqoFiVZF_9o7yfUacmx9QIe9pS52UMqCgqnStt8rDr9tVTjlaGS36ABGJukydb9k4RnwFruBntXdRrlF-Tk0FUK7fvC7U7PQol8uthQf2pUuWMIgl4ok8zBUx1V58G9ZpV_QqSbmHtFPDDeMpv9HPq1pZHMBx1IzGeIGO7DG3b85TWv6wJffGh4RZRBBcUYtv8frKkjGVPKPrGoekj166MaHLM5b1ecJQ5fyj45UFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط بعضی افراد میدونن این چیه
😊</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2751" target="_blank">📅 19:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/iaghapour/2749" target="_blank">📅 20:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0RDh37J0vTNj8TUCUApMhaB6IJ0m5ndtfVaDj0uL01QPNdnMPwb1jvdqxC5Mb2w5S_sB5M7otGbIyew2bxyDlYh92w2WKrkq1XJEc3fkKFM9b27UbcVlNIZA-rhBH7w-2rkMnVdP3LU3T9kzmVWg7NToce4erGkJSVmnatZLjpqI5wuNBfaUVy6dp_S9hK6a5Jre9bYqZX3C6C8Kyh-luUMm5cMbirX2LxsotP36wBUEfLmZ1J2y9gKOx9J1fAjfP5Pzl-VkagYpwP3uv0Hsr6cmL_idcrgJuB9bYXzBey76gnL-i7yfaWZT7QLgHIRK4WHhqCAl_DX1SgRI9VNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مسدود شدن ناگهانی پنل‌های رایگان روی کلادفلر
گزارش‌های متعددی از کاربران دریافت کرده‌ایم مبنی بر اینکه پنل‌های رایگان (مانند نووا و BPB) به‌طور ناگهانی بن شدن.
سر اینکه چرا این اتفاق افتاده دو تا بحث هست؛ یه عده میگن خیلیا از قصد رفتن این پنل‌ها رو به کلادفلر ریپورت کردن تا بسته بشن. یه عده هم میگن نه، خود سیستم هوشمند کلادفلر تشخیص داده و بن کرده. خلاصه دلیلش هر چی که هست، تو استفاده از این ابزارها همیشه ریسک بسته شدن وجود داره.
💡
یه توصیه خیلی مهم:
بچه‌ها، واسه ساخت و راه‌اندازی این پنل‌ها اصلاً و ابداً از اکانت و ایمیل اصلی خودتون استفاده نکنید! همیشه یه حساب فرعی بسازید و با اون کارتون رو راه بندازید.
🔄
آپدیت جدید پنل نووا (Nova):
توسعه‌دهنده پروژه نووا خبر داده که کدهای این پنل رو دوباره بازنویسی کرده و تو آپدیت جدید، مشکل ارورهای مختلف (مثل همون ارور رو اعصاب 1101) کلاً برطرف شده.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/iaghapour/2748" target="_blank">📅 20:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">.
⚠️
ببینید، اینکه بیایم مصرف کاربر رو چند برابر حساب کنیم (مثلاً طرف ۱ گیگ مصرف کرده ولی ۲ گیگ از حجمش کم کنیم)، اسمش زرنگی نیست، رسماً دزدی و کم‌فروشی تو روز روشنه! اینجور کارا فقط گند می‌زنه به اعتماد مردم و باعث میشه مشتری به بقیه فروشنده‌هایی که دارن…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/iaghapour/2747" target="_blank">📅 18:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک تشکر ویژه از همراهان همیشگی
🌺
دوست داشتم از این فرصت استفاده کنم و از تمام کسانی که تو این مدت اخیر که درگیر محدودیت‌های شدید اینترنت بودیم، به هر شکلی پشت ما ایستادند و کمک کردند، از صمیم قلب تشکر کنم. حمایت‌های شما باعث شد تا تیم ما بتونه هر کاری که از دستش برمیاد رو در این رابطه انجام بده.
از دوستانی که کانفیگ‌ در اختیار ما قرار دادن، تا عزیزانی که اکانت سایت‌های مختلف از سرویس‌های هاستینگ گرفته تا ابزارهای هوش مصنوعی و... رو به دست ما رسوندن تا کارها لنگ نمونه؛ واقعاً ازتون ممنونم.
و یک تشکر ویژه از دوستانی که با کامنت‌هاشون و دفاع از کار ما در گروه‌ها، سنگ تمام گذاشتند و بزرگ‌ترین حمایت رو از ما کردند.
خیلی دلم می‌خواست اسم تک‌تک شما عزیزان رو اینجا بیارم و شخصاً قدردانی کنم، اما به دلایل مشخص و برای اینکه برای خودتون بهتر و امن‌تره، از این کار صرف‌نظر می‌کنم. ولی بدونید که تک‌تک کمک‌های شما برای ما ارزشمنده.
دقیقاً تو همین زمان‌های سخت و بحرانیه که باید کنار هم باشیم و بدون هیچ چشم‌داشتی به همدیگه کمک کنیم تا از این شرایط عبور کنیم. (البته بماند که در این میون، کانفیگ‌های میلیونی هم به پست ما خورد که خب... بگذریم!
😄
)
امیدوارم دیگه در هیچ زمانی دچار مشکلاتی شبیه به این نشیم و روزهای بدون محدودیتی رو پیش رو داشته باشیم.
دم همتون گرم!
✌️
💚</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/iaghapour/2746" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCRYbxkHM7dHwQj4BrAT7EGO7qoi3XilWJeIPxTAPmz-w5TdH82g82OtthKYvn_-6POKHALYWT3mIcbIcEIS7SZtUtVhrCJL2qbHn-Q_sDs0COJ2-yd7j4aWtwLlRUXHE1nuQaUxMTlpJLbCw6v4sH6GcuM7hGoLshBXPRMGVME0mttlrfQiE4qmEKlj7igShkcuvkkIUFSm9Kp4_NBcLvodVL2m_-a3nZDifWQ_1KmC0FWQHjwXSxXwBi4RCXQCMUMnbRu6HSqQED_XLhX7H8S8LZ1aGzBoPzkl1pExuB5liDSc55V53nQtXAqKSLraaNDIlqKOe_CNWqJyzuI9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.
⚠️
ببینید، اینکه بیایم مصرف کاربر رو چند برابر حساب کنیم (مثلاً طرف ۱ گیگ مصرف کرده ولی ۲ گیگ از حجمش کم کنیم)، اسمش زرنگی نیست، رسماً دزدی و کم‌فروشی تو روز روشنه! اینجور کارا فقط گند می‌زنه به اعتماد مردم و باعث میشه مشتری به بقیه فروشنده‌هایی که دارن سالم کار می‌کنن هم به چشم دزد نگاه کنه.
اگه خرج سرور و هزینه‌ها بالا رفته، خیلی روراست قیمت‌ها رو ببرید بالا. مشتری ترجیح میده گرون‌تر بخره ولی بدونه دقیقاً داره بابت چی پول میده، تا اینکه یواشکی از حجمش دزدیده بشه.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/iaghapour/2744" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-1l_CFO8Wzw4Oc-8M-tHN0d1U244z0S9UAu883UHtgY3TjyDUS2lqjJfiUWVBohvplE4_CZNy07b-InI3OOP1wWtiji49dKgcmbOc1m1AU73rQgtY5_fxEXzVe0-RtyP15j1nR9kQgT87dVxr3VNH2O5jpHvKdx8M2BVYxlD6Aiqfwg7bs3nuE1twDgY-o3fcTsc5XlArzIVIQzZyTe03Tlb6OpnplszL3y9uEMtW3akXEZxgVYfg-riup8qZ8VDKaJ66EbgOjwe_gTGGg225glN55EvAPj92asYgZZDED27KaVQRnBu4CXaVPivY2RcmFoAgqsDhYQBiFpTk3Xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.11.0 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
-
🛡
پنل ادمین با مدیریت کامل یوزر ها و چت ها
-
👑
رول owner برای بالاترین سطح دسترسی
-
⚔️
رول admin برای دسترسی محدود به پنل ادمین
-
⚙️
دسترسی به تنطیمات برنامه از طریق پنل ادمین
-
📋
بخش لاگ برای مانیتور از چند منبع مختلف
-
👤
ساخت یا ادیت یوزر از طریق پنل ادمین
-
💬
پاک کردن کل پیام ها یا ریست کامل دیتابیس از طریق پنل ادمین
-
📖
وبسایت ویکی سانگبرد در
docs.songbird.website
-
🕑
نشان دادن آخرین بازدید کاربران
-
📡
انتخاب Songbird به عنوان سورس Remote channel
-
💨
بهبود عملکرد قابلیت Remote channel
-
🔧
رفع باگ های گزارش شده
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2743" target="_blank">📅 20:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zxe_k_MXveXjmFbOek81A5RU9FNuT36KMQTmNQmKx2sxxei7xvXpEB9bD1r83_hViEaHtwerMCYpXXVAyUcIEfKsntoM53YOr0EHQ-U5R_wNDyPZ5UyR25jIxn-ky_Eb3gNTaeXtuAwzLM-4gAeXvSjrbNO0jJrqZfkjLaVugkNpQmYPBrmDyyq4DBguLO_6caiVfGi8-GDPWmk2JHlYUOdsG5OWIxGY2oF_ccC5AHAIF9ygSmXI37yYltLUQwDPClc-er-suGbbq6ruMcc-FKNv-1cKC4gG2JL20IoiQABveF0bVVbYQcQLuXcFtDGSr0KSVcNYnHED98d4WZKGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قابلیت جدید گوگل سرچ کنسول: ردیابی دقیق ترافیک شبکه‌های اجتماعی
گوگل ابزار جدیدی به نام Platform Properties را به سرچ کنسول اضافه کرده است که امکان ردیابی ترافیک ورودی به شبکه‌های اجتماعی از طریق نتایج جستجو را فراهم می‌کند. با این قابلیت کاربردی، می‌توانید دقیقاً متوجه شوید مخاطبان با جستجوی چه کلماتی به ویدیوهای یوتوب یا سایر شبکه‌های اجتماعی شما (مثل ایکس، اینستاگرام و تیک‌تاک) رسیده‌اند.
این ابزار سه گزارش جامع ارائه می‌دهد؛ گزارش عملکرد برای نمایش دقیق کلیک‌ها و میزان بازدید، گزارش اینسایت برای شناسایی پست‌های موفق و تحلیل روند ترافیک، و بخش دستاوردها برای ثبت رکوردهای جدید و پیگیری رشد کانال. برای راه‌اندازی این سیستم، کافی است در سرچ کنسول یک ویژگی جدید (Add property) ایجاد کرده و پس از انتخاب پلتفرم هدف، مراحل تأیید هویت را طی کنید. این آپدیت طی هفته‌های آینده فعال می‌شود و یک امکان فوق‌العاده برای تحلیل دقیق‌تر بازخورد ویدیوهای آموزشی و مدیریت سئوی محتوای شما خواهد بود.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/2742" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXjtt_zg5bbe2wg9jN9jz36-Uo3Hi-CInNWZzE8L4GhQAJa4pS4IhGB4XJjBIWTPHHNH4P8wj8TXxLP34GlhtdcYoZHprbdmcj7OA-NiSma9lpjDGKjEQhZ70nNyd9ao8mmRMlLHjA2m9tm2EnfQrBKGeb946AGs0TCiMDjBRuQlMiNolOt9SxoxV4c3ER1gnMFzt1BOKmVOuE6jg0Bh8tjLR36HmrTOIwfIb8pRwoQH71AB6KUiw4GMkTM2kAcrOsx8Kiow5PgY0cb--J8di4tlhsBhXBn9_HHECKviWLqIokaLaAZPEgvemQp0IO57SOxH2jwoN3Wu0qEiqrSoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اعتراض ۱۱۵ هزار نفری به سونی؛ دیسک‌های فیزیکی را حذف نکنید!
یک خرده‌فروش کانادایی (PNP Games) کمپینی با نام «Don't Kill the Disc» به راه انداخته که تاکنون بیش از ۱۱۵ هزار امضا برای توقف برنامه جدید سونی جمع‌آوری کرده است. سونی قصد دارد تا سال ۲۰۲۸ درایو نوری را به طور کامل از کنسول‌های پلی‌استیشن حذف کند.
🔹
جزئیات این ماجرا:
🔸
نگرانی معترضان:
به گفته راه‌اندازان این کارزار، حذف دیسک‌های فیزیکی به معنای نابودی کامل زنجیره‌ای از مشاغل (خرده‌فروشان، توزیع‌کنندگان و تولیدکنندگان)، از بین رفتن بازار بازی‌های دست‌دوم و نادیده گرفتن جامعه کلکسیونرها است.
🔸
دلیل سونی برای این تصمیم:
همسویی با ترجیحات کاربران و رشد خیره‌کننده فروش دیجیتال. آمارها نشان می‌دهد سهم فروش دیجیتال بازی‌ها از ۱۳ درصد در سال ۲۰۱۳ به حدود ۸۰ درصد در سال ۲۰۲۵ رسیده است.
🔸
نظر تحلیلگران:
به دلیل سودآوری بسیار بالاتر فروش دیجیتال و کاهش هزینه‌های تولید سخت‌افزار برای سونی، کارشناسان اقتصادی احتمال تغییر موضع این شرکت را با وجود این اعتراضات گسترده، بسیار اندک می‌دانند.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/2740" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🟢
دوستان عزیز، همون‌طور که قبلاً هم اشاره کردم، کامنت‌های یوتیوب به دلیل جلوگیری از اسپم، به‌صورت دستی تایید میشن. چند ماه پیش یه عده شروع به فرستادن پیام‌های اسپم و نامربوط زیر ویدیوها کردن و برای اینکه مشکلی برای کانال پیش نیاد، مجبور شدم تایید کامنت‌ها رو دستی کنم.
تا الان پیام‌ها هر ۲۴ تا ۴۸ ساعت بررسی می‌شدن، اما از این به بعد
هر شب
کامنت‌ها رو بررسی و تایید می‌کنم. البته در تلاشیم تا راهی پیدا کنیم که این محدودیت به‌زودی کمتر بشه. از درک و همراهی همیشگی شما ممنونم.
💚</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/iaghapour/2739" target="_blank">📅 19:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKqcYgDYLS3rh2y5LlR_Z0XbEYGTrqrQWIShUe6WmQiMxkwKtQb8gAkSJHCjrWQlwT66t_F0TMFi-ST6oiObSQJ1lO3J4sS0vNV1SWFIM47FwQ73gGbPwa6mmZpcnnb7SlSlAmoWapzlntXklTnfx7qsocXso1Xko5uKsrQv_Sc7cHm3DcrJWOpOBLlKJqJXRreHFbaVpvP6GBKzwrCP6kaaHrmSMxaafNQeIGmILWBodpgSJ0fSF71Mjg254X8gWcfnl8_ja6JG2DgbWO2ewbi1turcy9eO98FwMrMeYFBA_GbUhpUaIpRQ0OLhGE776D7I-ET9eVH26KNe5nEy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استفاده پنهانی گوگل از عکس‌ها و ویدیوهای شما برای آموزش هوش مصنوعی!
گوگل به‌تازگی تنظیمات حریم خصوصی خود را تغییر داده است. با این تغییر، فایل‌های صوتی، تصاویر و ویدیوهایی که در سرویس‌های مختلف گوگل (مثل جستجو، مپس، ترنسلیت و...) آپلود می‌کنید، ممکن است برای آموزش مدل‌های هوش مصنوعی این شرکت استفاده شوند.
🔹
چگونه این قابلیت را متوقف کنیم؟
خوشبختانه امکان مسدود کردن این دسترسی وجود دارد. برای جلوگیری از استفاده شدن داده‌هایتان مراحل زیر را طی کنید:
۱. در تنظیمات حساب کاربری گوگل خود به بخش
Search Services History
بروید.
۲. تیک گزینه
Save Media
را بردارید.
۳. در همین بخش می‌توانید کل سابقه جستجو را غیرفعال کنید یا یک زمان مشخص برای حذف خودکار (Auto-delete) اطلاعات تعیین کنید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/iaghapour/2738" target="_blank">📅 19:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2736">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIjnRvtRIk2FGKgZazWWzGo9WUyt1hC-zlqB3e1J8y2ME2pTCL0U1VbVaQGY_3FtATInuho0ROEw_VhfRlobQzxwiS3S2yD2yQYucGbK-OmEJ8_8sL4Af089WQ0c29NAtkNxhIFsSmY6q0BSzxg1O7VHzzxeMDp6Yn6Ed59G6PJo6-0NCvlLxRjmbMgPegpQ_ZuYSHsWS-pZazmhOKAlL0JDQZHmLBHNYlbKCYioPBkD4yvuK114t52FSDlLty9_GIGKcs1Jh4oKsHAXotDatWqqPUegr3BIfR0uGSniDHCutZNPbNrPUZPjnwyynzFrvAGz2uQHzyL9BY3BrLPrUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠
معرفی پروژه Iran Dev Tools؛ حل مشکلات در سروهای ایران
قطعاً به عنوان یک توسعه‌دهنده بارها با چالش تحریم‌ها، فیلترینگ و سرعت پایین دانلود پکیج‌ها و دپندرسی‌ها دست‌وپنجه نرم کرده‌اید. پروژه متن‌باز Iran Dev Tools مجموعه‌ای از اسکریپت‌های هوشمند و مستقل است که دقیقاً برای حل همین مشکلات تکراری برنامه‌نویسان روی اینترنت ایران طراحی شده است.
🔸
منوی مدیریت یکپارچه لینوکس:
شامل اسکریپت نصب Docker به همراه تنظیم خودکار میرورهای رجیستری ایرانی برای دور زدن تحریم‌های داکر.
🔸
بنچمارک و تغییر هوشمند DNS و میرور APT:
تست زنده و تنظیم سریع‌ترین DNSها و مخازن سیستمی (APT) لینوکس بر اساس کیفیت شبکه شما.
🔸
تنظیم خودکار میرورهای برنامه‌نویسی:
شناسایی و ست کردن بهترین میرورها برای پکیج‌منیجرهای محبوب از جمله
npm
،
pip
،
Go
،
Composer
و
NuGet
تا با بالاترین سرعت ممکن پروژه‌های خود را توسعه دهید.
🔗
لینک ریپازیتوری پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/iaghapour/2736" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2735">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e24MJ7TbhtTjLDs6QxaFz0ENhSjd5C9ZNaMMHkDBMIi1H_YPbKOsBTQWFZS7N8lepj347LzHK1WjmvUDw6V0KO0GFTl3MB75_TuHJ1_UTfJ7iVf8Vek89dBtdjfDAFKH9iOf01L7oYDOOyXw-bbethA5UBF5t4Xvo5anTzRfKhjpDPc-eashTc4JokPLXft8gATIWzjBklhkINWb35hFLrBY0LXxllz7p4oCBTziUrJZPQ3koDPTS5Xs6aVMUnGPivi19jpzI_gaReXEoj1k2NaYM-VzOaEWbWZJEh_SqZFr3IFR2emDyOVQoalCivNJ_phPCRSf6v8q_t5Oy-ihAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی (GRoute)؛ کلاینت سبک و مدرن اندروید برای عبور از فیلترینگ
جی‌روت یک کلاینت فوق‌العاده سبک و روان برای اندروید است که بر پایه
Xray-core
ساخته شده و با ظاهر شیک و مینیمال اتصال به اینترنت آزاد را بسیار ساده‌تر کرده است.
🔹
ویژگی‌های کلیدی کلاینت GRoute:
🔸
پشتیبانی از پروتکل‌های مدرن:
سازگاری کامل با VLESS، VMess، Trojan و Shadowsocks در کنار ترنسپورت‌های پیشرفته‌ای مثل REALITY و TLS.
🔸
ابزارهای پیشرفته عبور از فیلترینگ:
مجهز به قابلیت
فرگمنت (Fragment)
برای دور زدن مسدودسازی SNI، سیستم Sniffing و مسیریابی تفکیکی (اتصال مستقیم سایت‌های ایرانی).
🔸
مدیریت ساب‌سکریپشن و وارپ:
به‌روزرسانی خودکار لینک‌های ساب، نمایش حجم و تاریخ انقضای اکانت، به همراه امکان ساخت کانفیگ
WARP کلودفلر
تنها با یک کلیک.
🔸
اسکنر اختصاصی IP تمیز:
اسکن رنج‌های کلادفلر و پیدا کردن کم‌پینگ‌ترین آی‌پی‌ها برای شخصی‌سازی سرورها.
💡
پ.ن:
در حال حاضر فقط نسخه
اندروید
این برنامه منتشر شده است، اما نسخه
ویندوز
آن نیز به‌زودی عرضه خواهد شد.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/iaghapour/2735" target="_blank">📅 20:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2733">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmj7n3woKKE_ZAVe0Aq6KhdHtytsswv68-WHNWAuHxnNEMer5k4buabcuh5b_dVZIYfKke3lpnSabeyw03LWfln-2QaFwx_b0SBuT2CdNYeBd77YBC_i9cLyQvSx256b3TwGOEZZo61Ec36peIiZ9EzUo-R6DpUZIPcdQLKC8OV5QvW9rMnBQdl8fWFE_msQWRFyF7SOqGL-oT0g7JoSjhWvrPfng6bgRVBGXlUHm4Etjy45CbTi2THhPy3X3DoBPkQDwnRhOUzDHEaWpy9KAnkldQenqlQjIA39Rrk4SkubXeGloQgf1l60hZ8eVz916n_N5yCs1jRguCfVykdZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون دانش فنی فیلترشکن شخصی و رایگان بساز! (با یک کلیک)
🚀
🔹
تو این ویدیو قراره یه روش فوق‌العاده راحت رو بهتون معرفی کنم که بدون نیاز به دانش شبکه و بدون سرور مجازی، بتونید فقط با یک کلیک و تو کمتر از ۵ دقیقه یه فیلترشکن شخصی، کاملاً رایگان، پرسرعت با قابلیت تعویض لوکیشن و ایجاد کاربر با محدودیت برای خودتون بسازید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#رایگان
#ورکر
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/iaghapour/2733" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2731">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚠️
آقا این همراه اول قشنگ داره عجیب‌غریب حجم می‌خوره! اول که اومدن نصف بسته‌های خوبشون رو حذف کردن که مجبور بشیم بسته‌های گرون‌تر بخریم. بعدش هم برای تست یه بسته ۶ گیگی خریدم؛ منی که بیشتر از وای‌فای استفاده میکنم و ۶ گیگ برام ۱۰ روز کار می‌کنه، چشم باز کردم دیدم بعد دو روز پیام اومده بسته‌تون تموم شد!
توییتر رو که نگاه می‌کنی همه دارن از همین دزدی و حجم‌خوری شکایت می‌کنن. ایرانسل و رایتل هم همین‌طورین یا فقط اینا این‌جوری دست‌شون تو جیب مردمه...!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/iaghapour/2731" target="_blank">📅 15:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2730">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czEKvVoqT6rVVHIFW3ltAN5iQzIgYomTObwWNfjYXPwzmY5AUduqqJ-AAnprkm3p6GyptoKhbNEOHoiiH88gIayICNUiQeUL1haeFdC1eE_jjoG6UaT6kbSEyGcPCCudiwArxjGUuWS7KyHHyWvTHm3ItKU4aMgGo6PhpxiCrtevJXs5KxKCDgs37fL9RexQMFkU8Mhu4sj8YzVovU668VJolVsCVFHaY0wCbSFKjV7DmcDnrIfUtnZ90izYM-vQ65a_GdUVB-HKL57ZSBZBRL51q2gkMO4rGrxJ0Fa3KS5NInKb8shZR2Gs_AoQoKX0nqYl2KZzNKuxpl17gP_McA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ری‌برندینگ بزرگ سایفون؛ ظاهر کاملاً جدید و بهبود دور زدن فیلترینگ
سایفون (Psiphon) پس از سال‌ها دست به یک تغییر هویت بصری و ری‌برندینگ اساسی زده است. ظاهر قدیمی و سنتی این اپلیکیشن جای خود را به یک طراحی بسیار مدرن، مینیمال و شیک داده است.
🔹
مهم‌ترین تغییرات در نسخه جدید:
🔸
رابط کاربری مینیمال:
محیط برنامه از آن فضای شلوغ قدیمی فاصله گرفته و با استفاده از رنگ‌های گرادینت ملایم و پس‌زمینه روشن، تجربه کاربری (UX) روان‌تری را ارائه می‌دهد.
این تغییر ظاهر نشان می‌دهد که قدیمی‌ترین ابزارهای فیلترینگ نیز برای همگام شدن با سلیقه کاربران مدرن، در حال به‌روزرسانی زیرساخت و طراحی خود هستند.
🔻
دانلود از گوگل پلی
🔻
دانلود از اپ استور
🔻
دانلود سایر نسخه ها
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/iaghapour/2730" target="_blank">📅 20:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2728">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hedioum Tunnel Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.1 KB</div>
</div>
<a href="https://t.me/iaghapour/2728" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
Hedioum Tunnel
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/iaghapour/2728" target="_blank">📅 19:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2727">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsnHS5DwCV8AwrKKpQowUOqdyKFPb8lyjS9BpYdsiWdTUZKge8Arx4bmboNPWNIrUBnNnBQ3WR262on2n3Z9l_FR3iBB8GPmCQ_zQKjqZ_I_6rIshSpBVOAjrHQdI11mxCdZ1IWtZeW_BDEcQ-A9Ybdl0VhrStFR5lhY6Y_Paw1cwGxeeKZMenAyekm6tdPL72v9A7TG2Eq9hFo8ptN38rk8B5AFEqojcCYUA5v0itvKZ-axk7zfbLtO6uw-mMmKXTh1QebhOwTU9fSH7zERWzOhygWkgtOGf2EV2pRUIuZXxE7FOD4FruBmed9w-EutW7i_kwFV8fhm8um1QRvTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش راه‌اندازی Hedioum Tunnel: تانل مقاوم‌ در برابر DPI
🔥
🔹
با پیشرفته‌تر شدن سیستم‌های مانیتورینگ و DPI، خیلی از تانل‌های معمولی این روزها دچار افت سرعت یا قطعی میشن. اما تو این ویدیو رفتیم سراغ یک راهکار قدرتمند به اسم Hedioum Tunnel که به خاطر مکانیزم‌های خاصش مقاومت خوبی در برابر تشخیص و اختلال شبکه داره.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/iaghapour/2727" target="_blank">📅 19:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snASwi5Tw6QD1JFefOSgidkUuM3IMxTPdoHF3hmNoIBI5kHZo8EYSa_el6iLsaIpUuuFfGW_RR26eqQaINjnV3T73P1YHO_BQUHDdqYtqAOX2GgDzdVD9euHhpeXAEb46I3STHD_eVB_UBbPvwUHFmF7M0Y3qOMCAAgd1b5SzuhpXjTUEssyVyM0q366SJ-dbZ6rKJ3ju7cyAW3Oh9ZZWjdbzGfwUXmX7RpFpEiudp5bi7aJ5JiTAJpkDLw5WgIqYENVFr4UbzpbiiulNld9Kbw7HR-b9zhi47dSQ-xp3RI08CZbTGXK_KHBVGY1uqwjg9XGxX5zOwLP1ufREDCZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ارتقای بزرگ هوش مصنوعی پروتون؛ Lumo 2.0 با قابلیت تولید تصویر منتشر شد
شرکت پروتون (توسعه‌دهنده سرویس معروف پروتون‌میل) نسخه جدید هوش مصنوعی خود را با نام
Lumo 2.0
معرفی کرد. این نسخه با تمرکز شدید روی حریم خصوصی، قابلیت‌های جذابی مثل تولید تصویر، حافظه اختصاصی و جستجوی امن وب را به همراه دارد.
🔹
ویژگی‌های کلیدی Lumo 2.0:
🔸
عرضه در دو نسخه:
مدل
Lumo 2.0 Max
برای کارهای پیچیده (با ارتقای ۲۴۰ درصدی عملکرد نسبت به قبل) و مدل سبک‌تر
Lumo 2.0 Lite
برای کارهای روزمره.
🔸
قابلیت‌های چندوجهی:
امکان تولید، ویرایش و تحلیل تصاویر در محیط گفتگو به صورت کاملاً رمزنگاری‌شده.
🔸
شخصی‌سازی پیشرفته:
اضافه شدن قابلیت حافظه تحت کنترل کاربر، تعریف پروژه‌های رمزنگاری‌شده و امکان ساخت دستیارهای سفارشی.
پروتون که حالا بیش از ۱۰ میلیون کاربر در بخش هوش مصنوعی دارد، هدف اصلی نسخه دوم را جذب کسب‌وکارهایی قرار داده که نگران امنیت داده‌های حساس خود هستند.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/iaghapour/2725" target="_blank">📅 20:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1nVvflHacS9crYkX275puTBfBe2IQa3XHOaVfsbf58CMM_s8YmCJ0HqsaQioVKiL_6_5cHufN5UJ5Xndb9FdsCDP4cEfUMCtF7TbPId1qR5HQLHE3bUhQCDoUrxFDhXzQkB8gMabdMOx439NwMFv-NBdrTSFi4stlCQGwa08Ye7PUggiisKQmkvbyj83h81EcK8yMCYmTxJ67yTWbH_hgcV3If3zMKFirCguXGCWRzU7VJ9tvCJ5Dta3Rkym7NYc1Yv5UQnLJ988qzcPJmV7rwESMPUioAdc14pl9C5-P9JuT9YqUJbTxsymzuhKLRed25Rlb5RUXP93744GI4Ctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
افزایش بی‌سروصدا و ۱۰۰ درصدی قیمت اینترنت فیبر نوری مخابرات!
شرکت مخابرات در روزهای گذشته، در سکوت کامل خبری و بدون اطلاع‌رسانی قبلی، قیمت بسته‌های اینترنت فیبر نوری را به شدت گران کرده و تغییرات عجیبی در سرعت آن‌ها به وجود آورده است.
🔹
مهم‌ترین تغییرات اعمال‌شده:
🔸
حذف سرعت‌های نجومی:
بسته‌های جذاب با سرعت ۱۰۰۰ مگابیت (۱ گیگابیت) کاملاً حذف شده‌اند و سرعت تضمین‌شده پایه برای تمام بسته‌های تمدیدی روی ۱۰۰ مگابیت قفل شده است!
🔸
جهش دو برابری قیمت‌ها:
هزینه بسته‌ها بین ۵۰ تا ۱۰۰ درصد افزایش یافته است. به عنوان مثال، بسته یک‌ماهه ۳۰۰ گیگابایتی که قبلاً با سرعت ۱ گیگابیت ۴۰۰ هزار تومان بود، حالا با افت سرعت به قیمت ۹۰۰ هزار تومان (بدون احتساب مالیات) فروخته می‌شود.
🔸
گرانی گیگابایت‌ها:
قیمت هر گیگابایت اینترنت فیبر که پیش از این حدود هزار تومان بود، حالا به نزدیک ۳ هزار تومان (و در بسته‌های کم‌حجم به ۶ الی ۷ هزار تومان) رسیده است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/iaghapour/2724" target="_blank">📅 20:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2722">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g--ORkdO_jLxGkus3DI3N86kF1FF9dwo6I-GQ8GBN7Weq9nwMsy2jldovCz9heGkTqyJ-6zptj2ezX9RoXoW5oD-o3RSP2612RQ805Vu7MqbjRIOpK34DmoX4uuO4L-ewyScKs6q6n4JKfQAnf84noYAbaVvsvq9nFBhIP2xWZI5-QE225qxglFwAgUSLsKmdgCHcWtQHSZxD5EbdreVpjn1w_F9_zliY2LZHEhl0r_Q4JoikOoM-ypD51V-St80EoG6bSM95CQXCTk4nD5ZwD5X0FqLSuzCA05AsQOy33bMv6b5yWnivXCI2CCrVZ2LAAuKuOibur_r3pEdRN3X1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پلتفرم متن‌باز مدیریت DNS با دامنه دلخواه
با این سیستم می‌توانید یک سرویس ارائه ساب‌دامین رایگان روی دامنه اختصاصی خود راه‌اندازی کنید. کاربران می‌توانند رکوردهای دلخواه خود (مثل
mysite.example.com
) را بسازند و تغییرات به‌صورت آنی از طریق API روی Cloudflare اعمال می‌شود.
🔹
ویژگی‌های کلیدی:
🔸
پنل ادمین و کاربری حرفه‌ای:
ورود با اکانت گوگل یا ایمیل، مدیریت کامل زون‌های کلادفلر، تعیین پلن و محدودیت‌گذاری برای ساخت رکوردها.
🔸
ربات تلگرام یکپارچه:
امکان ثبت‌نام و مدیریت کامل رکوردها مستقیماً از طریق ربات دوزبانه تلگرام.
🔸
امکانات ویژه:
سیستم دعوت از دوستان (Referral) برای دریافت سهمیه بیشتر و قابلیت ورود/خروج دسته‌ای رکوردها (CSV).
🔸
راه‌اندازی خودکار:
نصب بسیار آسان با یک دستور لینوکسی (Bash) همراه با گواهینامه SSL رایگان و بکاپ خودکار دیتابیس.
🔗
گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/iaghapour/2722" target="_blank">📅 20:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2721">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
وعده وزیر اقتصاد: بازگشت عمده خدمات بانکی از هفته آینده / اطلاعات مشتریان امن است
علی مدنی‌زاده، وزیر اقتصاد، با اشاره به تداوم حملات سایبری به شبکه بانکی کشور اعلام کرد که بخش عمده خدمات مورد نیاز مردم از ابتدای هفته آینده مجدداً در دسترس قرار خواهد گرفت.
🔹
نکات مهم صحبت‌های وزیر اقتصاد:
🔸
امنیت داده‌ها:
تا این لحظه هیچ‌گونه اطلاعاتی از مشتریان از دست نرفته است و استفاده از سامانه‌های پشتیبان، مانع از بروز مشکلات جدی در حفظ دارایی‌ها و داده‌ها شده است.
🔸
تداوم حملات:
پس از بازگشت سامانه‌های بانک‌های ملی و صادرات به مدار، تجهیزات جدید آن‌ها مجدداً هدف حمله قرار گرفته است؛ اما به لطف سامانه‌های پشتیبان، بخش زیادی از این حملات برای کاربران محسوس نیست.
🔸
اولویت‌های شبکه بانکی:
تمرکز فعلی روی بازگرداندن سریع سرویس‌ها، شناسایی منشأ حملات و افزایش سطح حفاظت سیستم‌هاست. با این حال، راه‌اندازی برخی از خدمات خاص به زمان بیشتری نیاز خواهد داشت.
پ.ن:
الان ۲ هفته‌ست که بخش بزرگی از خدمات ۳ تا بانک اصلی کشور قطعه. تو این هیر و ویر شایعه هم زیاد شده؛ یه عده میگن هک شدن، یه عده هم میگن کار خودشونه تا جلوی بیرون کشیدن پول مردم رو برای خرید طلا و دلار بگیرن.
مثل همیشه هم هیچکس راستش رو نمیگه؛ اول میان کلاً تکذیب می‌کنن، بعد میگن آره حمله شده ولی اطلاعاتی دزدیده نشده، آخر سر هم که همه‌چی به باد میره هیچ‌کس گردن نمی‌گیره و پاسخگو نیست! تو این بلبشو، حالا بماند که بانک‌ها یواشکی جلوی وام‌ها رو هم بستن و طبق گفته بعضی خبرگزاری‌ها، سود وام‌ها رو از ۲۳ درصد کشیدن بالا و کردن ۳۵ تا ۴۰ درصد!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/iaghapour/2721" target="_blank">📅 16:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2719">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcZkyQonpchVOnlYYYT51M_iw2hmwBlTmlSn3BrqVMcnKDeJyIBZhIbnUdN4QgNIaXLx2rYEMYqQf5bHImXgDuBRqQVJoTCeuYaTz6JwiRCqttiJKWfh5gFrHPJ0fRyl96WF_Q-FW7BMw27DVbbyzsFxZlPCpFsUvGG2RzHbim8cSdiHLBAgGGx0EeL5EVt-om89Ef4TVd2yEgA7QOkC0RffTRJt_dvzRlUb70RFcMHPYOFA5nB7J644vn2_vu1iwxpbEapccwgPxUHP0vxmcG1DZhQ7pCZkn2J5aaaUiha_hN49ddyvUlvsidCmi5KUfbnJd28BcYub24VMR5BASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های سرور ایران فقط با یک کلیک
😎
🔹
یکی از مشکلاتی که این روزها خیلی‌ها باهاش درگیرن، محدودیت‌های شدید و اصطلاحاً اینترانت شدن سرورهای ایرانه که باعث میشه ارتباط ما با خارج مسدود بشه تو این ویدیو قراره بهتون یاد بدم چطوری فقط با اجرای یه اسکریپت ساده، تمام این محدودیت‌های شبکه رو روی سرور ایران برطرف کنید و هرچیزی که دوست داشتید دانلود کنید یا نصب کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ایران
#ملی
#محدودیت
#سرور
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/iaghapour/2719" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-lOFK-n1nGOsOiJLluZYuOEuB-EA1nrfyN4Bl6pNyUIGp6GXoHlKkMq3zWyJvrxKPPP9AiSdqh5tZsQfP3cjdYDH2bPaYyzYVhL5F-meQS5nvFbXxSWgcI36n4eEQPu0O9-CEZGBjjgqRMZsPsuu1NRvifidwCcAfq18UIZ7rmkHOXuq5xYQZe0dr4x3Vl9LkaaIBYxhA0YHK2tE2fJQXVmztmg4F5jIewWw9j3XTkPOAzSgLQ97acXsNsY7CA6xc0HJnhxAcA-cqoS5Q3-SWsU1Hc0GjYLhCVUwDQ8vIncPwiXBSd7Yc5DzK9hTjFdh0jDklj432QACcjU3UBs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔌
قطعی برق و سریال تکراری خاموشی اینترنت و شبکه موبایل!
🔸
با شروع فصل تابستان و آغاز خاموشی‌های برق، مشکل همیشگی از دسترس خارج شدن شبکه موبایل و اینترنت دوباره گریبان‌گیر کاربران شده است. گزارش‌ها نشان می‌دهد تنها چند دقیقه پس از رفتن برق، دکل‌های مخابراتی (BTS) خاموش شده و ارتباطات در مناطق وسیعی مختل می‌شود.
🔹
دلیل اصلی این اتفاق، فرسودگی و خرابی باتری‌های پشتیبان این دکل‌هاست که توان روشن نگه داشتن تجهیزات را حتی برای زمان کوتاهی ندارند. این قطعی‌ها نه تنها دسترسی ۸۸ درصد از کاربران به اینترنت موبایل را قطع می‌کند، بلکه باعث از کار افتادن خودپردازها، دستگاه‌های کارت‌خوان، دوربین‌های ترافیکی و سایر خدمات حیاتی و شهری می‌شود./شبکه‌چی
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/iaghapour/2718" target="_blank">📅 12:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1cGL3YJFfTBp040fEPvqcJJ5co9pyaYFjRlh6ntjgRws7szkuJ0G2hVmxaHPrdUhFGFkqUeTbWmh6gJkrWtWU_ZUUo7eCm6zTZkSEwfZz-1xT4jVrIHGIHOdIadc4L4UelbSDab4XK0K2-oq2yzTpu9za7UzGkz4dmxztjyLKZln8lU1Y8JpdKmnteWt6ogAbmWMkXuvwHLuinL7e-3uAlCcDjWtlNWBjqYqbixm-EtoIyEmvyqR6R8LR_VN8Bp1RObbH1_ICNtEYymGQuXt4d8MOa5exmE9MFFjvPkKwVde0IXNPG-O7ZiiFdZpsVtqwJNjXDE1RPJ2qqBtdZwNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی اسکریپت ساده EZxray Direct Server
یک اسکریپت کاملاً خودکار که سرور شما را به یک مرکز Xray با پشتیبانی از ۱۲ پروتکل مختلف و ۲۰ پورت متنوع تبدیل می‌کند؛ آن هم بدون نیاز به هیچ‌گونه تنظیمات دستی یا دانش فنی!
🔹
ویژگی‌های کلیدی اسکریپت EZxray:
🔸
تولید همزمان ۱۲ کانفیگ
🔸
مدیریت بکاپ
🔸
مانیتورینگ لحظه‌ای
🔸
رابط بصری جذاب
🔗
اطلاعات بیشتر در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/iaghapour/2717" target="_blank">📅 17:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2711">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2uAsK_2RGHy3cZTcNDfWWRCllg1iyD0Pw3mceygorGOxwKhBxNVlhTgT0qp46WctRX6cg5VvYZeQ7rIm8m0CUzriPp0gXa5VmXcqA5YSiqIRDh9fCPxwD44-fgeADyv-hAV3n-nobU42iak2Q-dnRXViPE4MGHBDe7AtJOjJLIdDVka9qFP7KIW-qLvSZqrE4DlC_Uc2OeUVThpL6ZuyNs4XVxFdVYYL-fmWAYWwnNnGmO1lzqlzj4mzKTdYiYqrnrDjyz0Zt7IvlXBafIqMWNa9ay2Jvo_-_CzCB39b6yCq23B-z7sXg7pV3ctIhoo4amRMjwnMWz9rrKaX3fQMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhfqU7oZ5BY9oGS4oi1SD6XlvEbxHvsFdt_KdP-Sw7vZaEH4DHy6jKig62pM5p-lsKloa8um_i2GVu3ev6MyjRXHEKkBAx6q0jXUVGKebMBiDhLQ_C-VRv25_Dplxutk6pUaYsNMDxqh9uuVqCXZWC4o4Mxt39GAHJp_pUGTETiG2eudVt4qPMuLzsYc4oYXyWvF7B5T0cZjPNp_R50BFy3THIFfCLw3rQUplgxGEmEY58-ObVDmjEX1P42dbCSS01TZc3nHawPfaIkYURuuhyZUtX6njdkIlnsC4gd_wI_xPcz_omxmko7s_nRZxi2FhugqxpNLzAy57vPVzZFosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRevq5q0CIX5Gmxhe3giEGv9UpqBeQqh3qCUjDlbzK_cul5vYkWan_1pwnctJtc7VW7RIGMKxxEPLy_0gdj1dZn6JPGGb6buvRkOpzMTeIUsdUIB4AClXmRjf30WawoBlHTwSpEFYY9WzNraGS2MQH7mGAJP1qPoFI2MQRro9enXuq8hbFZvMm0Om1W_GWuMyjP4HxKRqFKBMcq92NaATsWvbnmqDRyV8F8vla3DDaWfW1EoZljtbHEr37sYw4Iroe5GeY4rXMOjKo83w4SqQ2wTR3y0m2h08y34U_ynUbOjrLj8wnD1Tns4jjb1FY8YEPyJTqsIwN58tUPeQSRglQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8YAt3aXOk4b2Jm4S0dtUaEHm7CfsWutfXgLjtty0sQ-OaJy-LJ25RjMwnS4KjA2ZjWtxaM6mXOiXRUmWJnYxtUhDMs-o0oiprh7Xj9Zgu5zMvNQPQGFuaWT8veX_z8-gv3a2Qehfq_KGHsAWZwQjiiWM9COGoFTqUHzR3OTvIr_Yh56aK7ZcFoyFy4RtuZFEti8GT5BbdyySmt-kUNxJ868jpZu8faNPK0-S1AM_m4RN6YJ5M3k_wN4VeYJOK5ZBVdPQfPcJ7yjlvpLo1qeNtmMfVyu_UV31QrXX4eLH_68Cc4ZNgtx5g7EEc1Mz3adYGoEJceGcizlX_CX_wbxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/glBpwWkkwhpNerbDxn5S7fjxD4vUQyRbveB12Y856LvVvd_nDHYd07tK7awvv3ifAiiitRd4TwEQuLHaX-mIbm65j7uZ9BREXI_wQ-5psLYpzbr9JV7ggGIBKN9I1PqqZ3CkOyI47b2v5rtQ9oG1M9qwgUKsVHCHLOtmMFJwEufJRkESlbzx2KiivJqQSOJYTaK8ZPOWCig4tAGjJ2TrNaAkq_iF_qbdmimH_z8JvQA67qNUdYGcq_9Ym51BoeKMJ8_j_Mrj5yaoXwss6jXxZ0_NFBm5C-Gpb9w-nw5PxeI5hAMjwMWKDWMOWTg1lk9l48-tZfR5lv1s0N33TNbGMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همراهان عزیز کانال
💚
همون‌طور که خودتون هم می‌دونید، پشت هر اسکریپت یا ابزاری که توی گیت‌هاب منتشر می‌شه و کار ما رو راه می‌ندازه، پشتش توسعه‌دهنده‌هایی هست که بدون چشم‌داشت، دانششون رو رایگان در اختیار همه قرار می‌دن.
من به عنوان کسی که تو یوتیوب و تلگرام فعالیت دارم، همیشه وظیفه خودم دونستم که در حد توانم از این بچه‌های متخصص حمایت مالی (Donation) کنم؛ مخصوصاً اون عزیزانی که واسه اولین بار اسکریپت و ابزارهاشون رو در اختیار تیم ما قرار دادن. این کار اصلاً لطف نیست، بلکه یه وظیفه کوچیک در برابر زحمات اون‌هاست تا انگیزه داشته باشن مسیرشون رو ادامه بدن.
دم همه‌ی توسعه‌دهنده‌های خفن و کاردرست گرم
👌🏻
اگه ابزاری کارتون رو راه می‌ندازه، دمتون گرم که با یه تشکر، ستاره دادن تو گیت‌هاب یا حتی یه دونیشن کوچیک (در حد توان)، خستگی رو از تن این بچه‌ها درمیارید.
مخلص شما...</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/iaghapour/2711" target="_blank">📅 20:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2710">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JltZM3Ft3kHbNVx8R_Xj2PJCjMtKla0-SAwSqRq8qw7M2869mphZkmlsG8MUP5q0tEsiFjeuMS1StO8QgumtdTYnUlfORcKnMQQ5IJ5PzxNIk-WMJpiuZDMSIXNV5Px2_0KdBVn2-ZUu5CK7CNYV1F-AJItm8yG7Weht1rjzIuEiXw0UIH72H9q3ftJwwDHndulEcuaIkohWN3t2EAm_08ML1PW5axVQV25itYnJxa56aYgqi2ptwNYDFPsU63qG8IEeXWBLbYQy7MRWYhOe3ld2ueavj3Fs3OVKajcbFW4HQAZbHwKt_QpqFGposPgxYMcRbffHtw4g56GHs2XbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Defyx VPN؛ دسترسی آزاد و هوشمند به اینترنت
🔹
برنامه Defyx یک VPN مدرن، امن و متن‌باز است که با رابط کاربری بسیار ساده خود، امکان اتصال سریع (تنها با یک لمس) و حفاظت از حریم خصوصی را فراهم می‌کند. این اپلیکیشن با بهره‌گیری از هسته قدرتمند DXcore، از پروتکل‌های معروفی مثل Xray، Warp، Psiphon و Outline پشتیبانی کرده و بدون نیاز به هیچ‌گونه تنظیمات پیچیده، اتصالی هوشمند به همراه ابزار داخلی تست سرعت ارائه می‌دهد.
🔻
بر اساس اطلاعات منتشر شده، نسخه جدید این برنامه هم‌اکنون برای تمامی پلتفرم‌ها از جمله اندروید، ویندوز، iOS، مک و لینوکس در دسترس کاربران قرار گرفته است.
🔗
دانلود آخرین نسخه از گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/iaghapour/2710" target="_blank">📅 18:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2708">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfOJllzgX3QIkribM-m6oVapwOLZvKMzxtRdh-WBH1_AjFohq9dMFhXIqG9UEuYdxF7ZRwcIjBmhXAo4iuRCMDzjfvy9ji69TVV5FrgH22EjuOadCzhEa2UWXFP0My4RyjSAzH_K-Ltnv7xzscPOR153bWq_lB4zKYWYLvJKgaRGadxODc0czRZyRk48HAZpSd4HS8-qHwg8Mkc8FV57iXfTARbXYwQU-oln7tvlIBTovXOdGiCgprmYaem6QHZouGWLHzLRBQM7rvaT_8w3wPVirqduvrikRU4qTQxEw2FEM_oN-vbJv7wm0xfOwlCkiXqa-gXsCQN1vANzrWdusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صرافی کوینکس ارائه خدمات به کاربران ایرانی را رسماً متوقف کرد!
🔹
صرافی بین‌المللی کوینکس (CoinEx) با انتشار بیانیه‌ای رسمی، به دلیل پایبندی به مقررات جهانی مبارزه با پولشویی و در پی گزارش وال‌استریت ژورنال، نام ایران را در کنار کشورهایی مثل آمریکا، بریتانیا، کانادا و چین در لیست مناطق تحت محدودیت کامل قرار داد. در حال حاضر تلاش برای ورود با آی‌پی ایران مسدود شده و حتی در بسیاری از موارد استفاده از VPN نیز کارساز نیست و کاربران با خطای عدم دسترسی مواجه می‌شوند.
🔻
اطلاعیه مهم برای برداشت دارایی‌ها:
کاربران ایرانی حداکثر تا
۲۵ سپتامبر (۳ مهر ۱۴۰۵)
فرصت دارند تا اقدامات لازم را انجام داده و دارایی‌های خود را خارج کنند. در این دوره انتقالی، حساب‌های احراز هویت‌شده (KYC) فقط امکان برداشت خواهند داشت. در بازار اسپات تنها امکان فروش (بدون امکان خرید) و در بخش فیوچرز تنها امکان بستن پوزیشن‌های باز وجود دارد و باز کردن پوزیشن جدید ممنوع است. همچنین اگر وام فعالی دارید، باید هرچه سریع‌تر نسبت به تسویه کامل آن اقدام کنید، چرا که پس از تاریخ ذکر شده احتمال اعمال محدودیت‌های بیشتر وجود دارد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/iaghapour/2708" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2707">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDcajMHvkl2yCi9oid-yKa4FhSSL7gUnab_Ca-2HQk9sedvmhUFkK_VbBgBtQsP5YljeW1M7PuGdqwSG8Rx8Vyel8utNAXgxMETm7pbdNolSBIQxwnvLmMywYnCa_WYBtpByMHmFeDOS2cO9FwpKwejE0x259d1F4J9nq2_iVTzAGq_90HzjZFpR8z1tXUInihqdElUx_ZXLzGy1DWkdc7LoyIs2XkGCaTqUzMKJ9xskV44a1DwTaeV39ED-5mSTHzZmL-QpyLh-dYvNusQnSMic4yyCKj4fjuAVvD4rjKb8LuOSN-DAKbv4Kh2RbEPRfpbaaIADg3325aecENG4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بر اساس گمانه‌زنی‌ها، انتظار می‌رود بازی مورد انتظار
GTA 6
با قیمت پایه ۸۰ دلار (معادل تقریبی ۱۳.۵ میلیون تومان) برای نسخه استاندارد روانه بازار شود. همچنین، خریداران برای تهیه نسخه کامل‌تر یعنی «آلتیمیت ادیشن» (Ultimate Edition) احتمالاً باید مبلغی حدود ۱۰۰ دلار (تقریباً ۱۶.۵ میلیون تومان) پرداخت کنند.
خوش به حال اونایی که توانایی مالی خرید دارن. )</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/iaghapour/2707" target="_blank">📅 19:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">domains List -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.5 MB</div>
</div>
<a href="https://t.me/iaghapour/2705" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دامنه ها برای به ویدیو بالا
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/iaghapour/2705" target="_blank">📅 19:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9lxctYQInsFwtYTH59aH8563OwX4ULjeRfZq8jNTISdSdNs29S2k39IE2lSL0-ZwLjfdh6qcqwWn9hyiCPss-WwJzvOuuozeqOWorxXeH6636asRL3GH0BYga0ZwQyh-otV1V3h4Dp5ipXz4g8GsGCaPkMNGA_f_yb9pqkNT22omYdw6IZMVer7Wft5jqqRuEoNb2lLfu5e56jolVUOl_ZrcnQceW6IlXXA_nwVdcsg0f2pw8QRaA6ed0moNeF8ySrAwpsG8Od_0tYBWabh7QTLVto77E8ttCf89hszHDFyNjwsEdcGM_Cavg6NEDPUlp0CutbBjsZhePoQhmbFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پروتکل ریلیتی رو دوباره زنده کن!
🔥
(+ اسکنر پیشرفته)
🔹
خیلی‌ها فکر می‌کنن با محدودیت‌های اخیر، دوران پروتکل ریلیتی (Reality) دیگه تموم شده و کانفیگ‌هاش از کار افتادن؛ تو این ویدیو قراره با هم یاد بگیریم چطوری پروتکل ریلیتی رو دوباره با بالاترین سرعت ممکن زنده کنیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ریلیتی
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/iaghapour/2704" target="_blank">📅 17:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2703">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eec5mGN_Vw4kC0daAE-Q484-0RYU8iHCRxa-iO44i1O-9H7Wyg0nTzc7k7KuhC-IoTlxXzOaGJ7QkAGCa-yxXW4itkwFO9dVKbRJEP3umshdNLU7EVMlx-EXLRVzlCiiN_81bIrCDcDkESkbxrTerdt9Hc5N0bZNFAoDt2hofQU0wtltaYdDXTIF-gQhTd2cbQF4BRBESLs6SQ95P6M6Zapdo9PGysVLEGtYySInpiXWeSjzIolA3Zw00Gcu0IiYPeM273vdQJgzUqwQK0ZEtSXUnt-cUplo_Lo4Eq2vqL4PVo0LbLQrNTnugCCCe_Secqz9S6jUifi5Xbqu4akRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
خداحافظی با کپچا؛ کلودفلر و غول‌های فناوری به دنبال استاندارد جدید
🔸
شرکت کلودفلر با همکاری توسعه‌دهندگان کروم، اج، فایرفاکس و شاپیفای در حال ساخت سیستم جدیدی به نام PACT است تا برای همیشه به دردسرهای کپچا (CAPTCHA) و اثبات ربات نبودن پایان دهد. ایده این سیستم بسیار هوشمندانه است؛ وب‌سایت‌های معتبر پس از یک بار تایید انسان بودن شما، یک توکن کاملاً ناشناس صادر می‌کنند. از آن پس، مرورگر شما همین توکن را به عنوان «برگه عبور» به سایت‌های دیگر نشان می‌دهد تا بدون فاش شدن هویت یا تاریخچه وب‌گردی‌تان، ثابت کند که شما یک انسان واقعی هستید.
🔹
مدیرعامل کلودفلر می‌گوید در حال حاضر بیش از ۵۶ درصد از کل ترافیک اینترنت را ربات‌ها و ابزارهای هوش مصنوعی تشکیل می‌دهند و ابزارهای امنیتی قدیمی دیگر پاسخگو نیستند. با اجرای این پروتکل جدید، هم حریم خصوصی کاربران به طور کامل حفظ می‌شود و هم دیگر نیازی به حل کردن پازل‌های آزاردهنده و کلیک روی عکسِ چراغ‌راهنمایی نخواهد بود! / دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/iaghapour/2703" target="_blank">📅 17:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2701">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzvTeNKBApACOwK3bm6gvpq3aRsV72ZAqpXRgJD6ZL18KSyoIpAuEEHdrqPvI0mZ33U8ShxrWU_uratrTx4YK9d32QGU24pbD7hJIcGcYRI5XBo6084WFEvFokFJr-Yy4l26UGJLLyt0yO4HtQ7_CeTN95zY0E2h18KiSUzJ3Cea-rxy-_sTVsu60Qgjri1zNdE5M5OtoUsEXPqKTiTn8e-r3cpY2lK1bqZjus3iSeYGPrOGr6KnfLvR26RQ11aQW4ycp-nFxjVNgY02m-vv2po-EYf1KnO_wflHiduGyvh3jXh9lO_UCO6uxuxnM9GXyRttqhVLy2mqIqg_TC76xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سقوط آزاد پلتفرم‌های داخلی و رکوردشکنی هشتگ تخفیف پس از وصل شدن اینترنت
🔸
با بهبود نسبی وضعیت اینترنت، کاربران به سرعت در حال ترک پلتفرم‌های بومی و بازگشت به شبکه‌های جهانی هستند. آمارها نشان می‌دهد فعالیت گروه‌ها در پیام‌رسان «بله» ۸۱ درصد سقوط کرده و ۲۷ درصد آن‌ها کاملاً تعطیل شده‌اند. رشد خیره‌کننده این پلتفرم‌ها در دوران قطعی، صرفاً از روی ناچاری بوده و حالا مردم کانال‌های داخلی را فقط به عنوان یک پایگاه پشتیبان برای قطعی‌های احتمالی بعدی نگه داشته‌اند.
🔹
در همین حال، کسب‌وکارهای آنلاینی که فروش طلایی خود را در دوران محدودیت‌ها از دست دادند، برای جبران خسارت‌های سنگین به تخفیف‌های گسترده روی آورده‌اند؛ به طوری که استفاده از هشتگ «تخفیف» ۱۲۰ درصد جهش داشته است. این آمارها ثابت می‌کند پلتفرم‌های بومی برخلاف ادعاها، هیچ جایگاهی برای جبران ضرر اقتصاد و کسب‌وکارها نداشته‌اند.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/iaghapour/2701" target="_blank">📅 20:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2698">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
حمله سایبری به شبکه بانکی
!
شرکت خدمات انفورماتیک با انتشار اطلاعیه‌ای، دلیل اختلالات گسترده در کارت‌های بانکی را تشریح کرد.
🔹
جزئیات این اختلال بانکی:
🔸
دلیل اصلی قطعی:
وقوع حملات سایبری به سامانه‌های کارت‌محور بانک‌های ملی، صادرات و تجارت.
🔸
اقدام پیشگیرانه:
این شرکت اعلام کرده برای جلوگیری از دسترسی غیرمجاز هکرها و حفظ امنیت داده‌ها و موجودی مشتریان، خدمات مبتنی بر کارت را موقتاً و به‌صورت عمدی از دسترس خارج کرده است.
🔸
گستردگی مشکل:
با وجود اینکه در اطلاعیه رسمی فقط نام ۳ بانک آمده است، اما بررسی‌ها و گزارش‌های مردمی نشان می‌دهد قطعی‌ها گسترده‌تر بوده و بانک‌های دیگری مثل «ملت» هم درگیر این اختلال شده‌اند.
🔸
وضعیت فعلی:
تیم‌های فنی و متخصصان امنیت سایبری در حال کار روی شبکه هستند تا این مشکل برطرف شده و خدمات بانکی به حالت عادی برگردد.
پ.ن: بابا ولش کنید‍! بعد 2 هفته اختلال این حرفا چیه میزنید؟ مثل قبل همون روند تکذیب رو جلو برید. بگید که ما هک نشدیم و قطعه سخت افزاری سوخته!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/iaghapour/2698" target="_blank">📅 19:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU-WOZNE24_HdsJF3rQhqpf7KChZGj4Ba3FcI_tVAjtvRQURIv7vyqW2iItiCo6MXvidYqPn4YQjVkiJV3I2SGALgl-o8u9Nd4meB5tPmtHW8IQWG6SsnuVXJNmYEw23OIKL4CcFmnJRh0hBl83HsKG1IysHrSKIn-hn8eImXBz9yaQnkHLF6B095SpC5mZ4Ax6Fj7FiHgQc8y5j2_F3nTrD_TcRUqXr6Odj6zsl_45WyRDVUHPLqIL3ugUvVvAPfeqIs8XgLn20L2H4Hma39qYZeGAvu6-ausvkkwqmhANs9i0UEl0Zjwj2emjY5UUyQykL6j50lsa77U3FXt2p3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
چرا فعال نبودن IPv6 در ایران یک بحران است؟
در حالی که دنیا به سمت استفاده کامل از IPv6 رفته، اتکای شبکه ما به ظرفیت محدود IPv4 چه مشکلاتی ایجاد کرده است؟
🔹
پیامدهای اصلی این عقب‌ماندگی:
🔸
کابوس CGNAT:
به دلیل کمبود IP، اپراتورها هزاران کاربر را پشت یک IP مشترک مخفی می‌کنند؛ یعنی شما عملاً هویت مستقلی در اینترنت ندارید.
🔸
دردسر همیشگی کپچا:
چون درخواست‌های هزاران نفر با یک IP ارسال می‌شود، سایت‌های خارجی شما را ربات تشخیص داده و محدود می‌کنند.
🔸
مشکلات گیمرها:
گیر افتادن در لایه‌های NAT باعث خطای Strict NAT، افت پینگ و قطعی در بازی‌های آنلاین می‌شود.
🔸
اختلال در دسترسی‌ها:
بدون IP مستقل، راه‌اندازی شبکه‌های خصوصی و دسترسی از راه دور به دوربین‌ها و تجهیزات هوشمند بسیار دشوار است.
🔸
افت کیفیت شبکه:
بار سنگین سیستم‌های تبدیل آدرس (NAT) روی سرورها، باعث تاخیر در مسیریابی و کاهش پایداری اینترنت می‌شود.
پ.ن:
دنیا با میلیاردها آدرس مستقل به دنبال سرعت و پایداری است، اما ما هنوز برای یک ارتباط ساده، درگیر پیدا کردن یک IP تمیز و عبور از لایه‌های NAT اپراتورها هستیم!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/iaghapour/2697" target="_blank">📅 22:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHvnjcspsZcbgyJ6Dy6vyKNIVEfy7ki2rx5nW22OKCEvt-F-2gPLnNP-0BJ5uksGQhERjsBkidXGVp8robFQROrLyn0XWZgo-YSycUeLOhMo-mEC-CL3UHYejQOh7WzTFckSTvWot8GbHqfMwCA5AUQ8f-uRyDibteaV9g6nr7CrpHQtoUD-tg8I9FuEtFMS056fIAsHFyHGikdxLwmy4H9IA1v5P34aFlQZ9QJpfMNVLaKfRCdWb61QKxtyghIJLlNvDcLU5dB9xJ9emm6WK86YexSKjcV5yVu14Rig0chB3TFFpN5xMMOeFfnEC1Wa99loklWosmHBJHYgY8O_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بحران خاموش در دیتاسنترها؛ اینترنت برگشته، اما نه برای کسب‌وکارها!
پس از گذشت چند روز از قطعی گسترده و مسدود شدن کامل ارتباط با اینترنت بین‌الملل در سراسر کشور، اکنون در حالی که اینترنت کاربران خانگی و اپراتورهای موبایل تا حدودی به حالت عادی بازگشته، اما گزارش‌ها حاکی از آن است که دسترسی بسیاری از دیتاسنترهای داخلی به اینترنت جهانی همچنان قطع یا دچار اختلال شدید است.
این دسترسیِ قطره‌چکانی و عدم اتصال دیتاسنترها، پیامدهای مخرب و گسترده‌ای برای زیرساخت‌های شبکه و کسب‌وکارها به همراه داشته است:
🔸
فلج شدن سرویس‌های آنلاین:
بسیاری از استارتاپ‌ها، پلتفرم‌های خدماتی و توسعه‌دهندگانی که برای کارکرد صحیح نرم‌افزارهای خود به APIها، کلادها و منابع بین‌المللی وابسته‌اند، با اختلال جدی مواجه شده‌اند.
🔸
خسارت‌های پنهان و سنگین:
وصل شدن اینترنت گوشی‌ها تنها ظاهر ماجرا را عادی جلوه می‌دهد؛ در حالی که شریان حیاتی بسیاری از کسب‌وکارهای دیجیتال در دیتاسنترها مسدود مانده و خسارت‌های مالی و فنی جبران‌ناپذیری در حال رقم خوردن است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/iaghapour/2696" target="_blank">📅 19:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/iaghapour/2694" target="_blank">📅 21:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2693">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrbZnwl1pXaxw3nF9UNYxYl9-DbyZJg-zG6AtwzxSvjE2w0mWSH1xUqZY8ezE93YbveXvfyKGzS9UaVL_xLUi39bpOL_P5KlND0aSZuIp_i1x5mJPTOldhODQfFmOGSKBXpJ2LtvtXgHkZpqNGZUfjgWKwLFOAwctXu7gGBgVJrQ7W-oWhdLqPwpwwZRo8ith2OkIrLaHObOJK32Jb8t2RpJ_j8bhJEmEmsrvY_rXZoGNblg1O1gqWwwznQBKqbuEY4egXEA4HLz4RcwUZlF3jTXAu7U_YmiS1xzKzMW1UETgjn3VLzaqKpeAxEveNHuWRczE2N1WuUhq7Wqp5-XMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند.
در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس /
ircf
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/iaghapour/2693" target="_blank">📅 21:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2691">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1KrSH_YDGk8MOv9MggbwAAQRvPZG8AQTqLA5PyTbyn-7HO9e6J2Z5soE9z0hVhhc0kGQaJgtEBZIi3h682Brqyq2KMoKatbKRCOZXVhbn6VKcW_BAaIBBfGAVuhzMKjnBTWMzGTakbqH4PlRMc9z-pzcPBXFNUZ7ZSQ2VgIfXGNqKlqUe5khxoZsmtu-maj6ItJFwDJDoA_-nlbKfd5_b1pL_VdCSR4rTsGzSwBVvS0lAfaFxFiphKte4D_hirmPuKmJj9yCbMPI1OeJR9pr8kipwwMjBp60mVDdM4Joe70PiPX4YAiKqlVMmD68OYs8G5IcBNRO2q_7MPUvT5-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش 4 روش تانل پیشرفته و مقاوم در برابر فیلترینگ
🔹
تو این ویدیو قراره با هم ۴ تا از بهترین روش‌های تانل زدن رو بررسی کنیم و یاد بگیریم چطوری تانل‌هایی بسازیم که در برابر فیلترینگ پایداری خودشون رو حفظ کنن.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/iaghapour/2691" target="_blank">📅 18:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2690">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
دوستان عزیز،
ربات «تماس با ما»
چون نسخه رایگانه، به محدودیت ۵ هزار پیام در ماه رسیده و رفته رو حالت تعمیر!
اگه تنظیماتش بر اساس تایم‌زون باشه، اول ماه جدید یعنی 2 روز دیگه خودبه‌خود درست میشه؛ وگرنه به ناچار نسخه پرو رو می‌خرم تا دوباره در دسترس قرار بگیره.
🥸</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/iaghapour/2690" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2689">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
آموزش تانل بین سرور ایران و خارج (۲ روش سبک و سریع)
😍
🔹
تو این ویدیو قراره با هم دو تا از ساده و سبک‌ترین روش‌های تانل زدن بین سرور ایران و خارج رو یاد بگیریم. اگه برای ساخت فیلترشکن شخصی‌تون دنبال یه راه ساده و بدون دردسر برای اتصال سرورها هستید، این آموزش…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/iaghapour/2689" target="_blank">📅 16:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌐
مدیرعامل سروش‌پلاس: فیلترینگ و قطعی اینترنت به ضرر ماست!
امین شریفی، مدیرعامل سروش‌پلاس در نشست گزارش عملکرد سال ۱۴۰۴ اعلام کرد که قطعی اینترنت و اعمال فیلترینگ نه‌تنها به رشد پلتفرم‌های داخلی کمکی نمی‌کند، بلکه نتیجه‌ای جز عصبانیت و لج کاربران ندارد.
🔹
چکیده مهم‌ترین آمارهای گزارش سالانه سروش‌پلاس:
🔸
ریزش کاربران پس از رفع محدودیت‌ها:
با آزاد شدن دسترسی به سایر پیام‌رسان‌ها، سروش‌پلاس با افت ۱۰ تا ۱۵ درصدی در تعداد کاربر و کاهش ۱۰ تا ۳۰ درصدی در شاخص‌های فعالیت مواجه شده است.
🔸
وضعیت کسب‌وکارها:
آمارها نشان می‌دهد حدود ۷۰ درصد از فعالیت کانال‌های فروشگاهی، آموزشی و تولید محتوا که در دوره محدودیت‌ها ایجاد شده بودند، همچنان در این پلتفرم ادامه دارد.
🔸
رشد آمار کاربران و پیام‌ها:
تعداد کل کاربران ثبت‌نامی این پیام‌رسان از مرز ۵۲ میلیون نفر عبور کرده است که از این تعداد حدود ۲۰ میلیون نفر کاربر فعال ماهانه هستند. همچنین در سال ۱۴۰۴ بیش از ۳۰ میلیارد پیام توسط کاربران جابه‌جا شده که ۷۶ درصد از آن‌ها مربوط به چت‌های شخصی بوده است.
🔸
امکانات و تغییرات جدید:
رونمایی از مدل اشتراکی «حساب پرو» (با قابلیت‌هایی مثل نشان ویژه و حذف تبلیغات)، توسعه تنظیمات حریم خصوصی و همچنین افزایش جایگاه‌های تبلیغاتی پلتفرم از ۳ به ۱۳ مورد، از اقدامات مهم این سال بوده است.
🔻
پ.ن: من داشتم میخوندم خندم گرفت این چطوری داشت میگفت خندش نگرفت؟
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/iaghapour/2687" target="_blank">📅 19:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2685">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSGsUeANhXhr5e_P9Zbqy4ztHLGc3kZCoKKQg3p8LOQ6dvts-grnQGoDpNsF9n-xgTZOa73WywB_OYMHuyL_gfpATjvVpNumzQUrAhRyMlvPE53_4P9F5xVBptbLX-kUKfQzIcUDw6lmd31sA1-f1rCCOof34xFDZz6OlH_HBcneBL7WS4Nx7wNIqhuJpmgrFu38plVdtX7rctZnoArFVxxiZGDQ1Va_57ruUA7wo6vLzep22vFz8E3ie5DOecfFtZnBlDw5mn5sx3FFD5Ym2Jw-BGtx55-ORhvZndlFnrZsk8mn0iMBLvgZdEu30XwLfdtiWaSqvqvtKH-thlcUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر (NovaProxy v3)
🔹
تو این ویدیو قراره یه روش فوق‌العاده برای ساخت یه فیلترشکن کاملاً رایگان و پرسرعت رو با هم یاد بگیریم. این بار رفتیم سراغ ورکر کلودفلر و قراره از اسکریپت قدرتمند NovaProxy v3 استفاده کنیم. تو این ورژن حل مشکل تماس صوتی و تصویری رو هم آموزش دادیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ورکر
#novaproxy
#worker
#کلودفلر
#vpn
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/iaghapour/2685" target="_blank">📅 19:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2684">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuFbUKFsDhLG0QkCbTXdTmWTbo7k0btlzuSfehpnZg7uPvULRB2mndc4GedqjeIBJzMPxArmFO2tW_nIo3fl3uB862S5d41_5f6Xgm2BMXEo8vXlN9pH82V9iAW460HawoqZZbH_-r4TvSSnNE0iflCuKje5gKDtubKDmqqudfvwcONuujw97S0cJ7AtTrB3w7W4juN92M2G-HbXUynD-0Wh4YhzEZfj3HH9wFwHhhb2SiYzN6ZEYqNNyeYDUwKXQvmjMMXfLfMBjWqxfKVvMKf65Qsst7b4MYlTqolKOToiXFq5Wk401KFwPUcs0OZ2r2pcDeF8xXYLmqa5rWTZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
افشای ۱۲۴ میلیون پسورد و ۵۶ میلیون ایمیل؛ آیا اطلاعات شما هم لو رفته؟
پایگاه داده سرویس معروف Have I Been Pwned به‌تازگی آپدیت شده و آمار نگران‌کننده‌ای را منتشر کرده است. این بار هکرها مستقیماً به سراغ کامپیوترها و دستگاه‌های شخصی کاربران رفته‌اند و بدون اینکه کسی متوجه شود، حجم عظیمی از داده‌های حساس را سرقت کرده‌اند!
🔹
نکات مهم این نشت اطلاعاتی:
🔸
منبع سرقت:
این اطلاعات نتیجه هک شدن یک سایت خاص نیست؛ بلکه بدافزارهای مخرب، پنهانی روی سیستم‌ها (مخصوصاً ویندوز) نشسته‌اند و پسوردهای ذخیره‌شده، کوکی‌ها و داده‌های مرورگر را دزدیده‌اند.
🔸
خطر پنهان:
از آنجا که بسیاری از کاربران اصلاً متوجه آلوده شدن دستگاه خود نمی‌شوند، این سرقت اطلاعات می‌تواند تا مدت‌ها بدون هیچ ردپایی ادامه داشته باشد.
🔸
اقدام فوری:
همین حالا به وب‌سایت
Have I Been Pwned
سر بزنید و ایمیل خود را جستجو کنید.
🔸
راه‌حل‌های امنیتی:
اگر اطلاعاتتان لو رفته بود، سریعاً رمزهای عبور خود را تغییر دهید. همچنین برای جلوگیری از نفوذ، حتماً تایید دومرحله‌ای (2FA) را برای حساب‌های مهم خود فعال کنید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/iaghapour/2684" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💰
مدیرعامل همراه اول: قیمت فعلی اینترنت با قیمت واقعی آن هیچ سنخیتی ندارد!
مهدی اخوان، مدیرعامل همراه اول، در مجمع عمومی سالانه این اپراتور با گلایه از تعرفه‌های فعلی اعلام کرد که هزینه‌های سرمایه‌گذاری ارزی آن‌ها کاملاً مشابه اپراتورهای منطقه است، اما قیمت هر گیگابایت اینترنت در ایران بسیار پایین‌تر از آن کشورهاست.
پ.ن:
جناب مدیرعامل! اتفاقاً تو این مملکت خیلی چیزها هست که هیچ سنخیتی با هم ندارن؛ از کیفیت اینترنت شما و چیزی که واقعاً به دست ما می‌رسه بگیر تا درآمد بالای مردم منطقه و حقوق‌های پایین ما! از همه مهم‌تر، بین زندگی و رفاه شما و واقعیتِ زندگی مردم هیچ سنخیتی نیست!
اگه واقعاً کار براتون نمی‌صرفه ما هم راضی به ضررتون نیستیم، کلاً درِ این اپراتورها رو تخته کنید و جرم‌انگاری استارلینک رو بردارید تا ببینیم تو یه بازار آزاد اصلاً می‌تونید باهاشون رقابت کنید یا نه! واقعیت اینه که سودهای کلان این اینترنت انحصاری (پرو) حسابی به دهنتون مزه کرده و حالا با گرون کردن‌های نجومی و پشت‌سرهم، به هر دری می‌زنید تا جیب مردم رو خالی‌تر کنید. وگرنه این چیزی که دارید به ما می‌فروشید اصلاً اسمش اینترنت نیست؛ هر وقت یه اینترنت واقعی و بدون فیلتر دست مردم دادید، اون‌وقت پولش رو هم بگیرید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/iaghapour/2682" target="_blank">📅 21:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBxx5f-18QpnZcyDinGfhMVH8xzIFMR_9JD9YqHle3Dhz0qO-b5ZEFnE3kzUk6A8Eubw--apL6lLmp9QNUYJMPlfemPR30xToyyta1jrKAbH5EXyKFiUPu9ZGlrGEIqF-dWVik9HwRCagtCPl1wHomVq75U8Mak_JJxAqXuViDRlFmCcWCKUjKx3AuRgPKjSnahsRry_f13FuQzs4IB6mmfW63CIBpV0ECnP7DMjgAKrSaNEnnBczEJ_8MNM9aRXefEwyrsgPQLhprk2kO9byIPZF8_zdYrkch0_t0xExx4qxhPA3qHRDAJH2GkzflSABFcJZve9l1DOWPyQ58kMKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار خیلی مهم: خطر فریز شدن دارایی‌ها در صرافی‌های خارجی!
بچه‌ها، همونطور که تو تصویر می‌بینید، صرافی‌های خارجی یه اخطار خیلی جدی در مورد تراکنش با پلتفرم‌های تحریم‌شده توسط OFAC (دفتر کنترل دارایی‌های خارجی آمریکا) منتشر کردن.
⚠️
تو این هشدار صراحتاً اسم ۴ تا از صرافی‌های معروف ایرانی آورده شده:
🔹
نوبیتکس (Nobitex)
🔹
والکس (Wallex)
🔹
بیت‌پین (Bitpin)
🔹
رمزینکس (Ramzinex)
❌
مشکل چیه و چه خطری داره؟
این صرافی‌ها اعلام کردن که سیستم‌های ضد پولشویی (AML) به شدت تراکنش‌ها رو بررسی می‌کنن. اگه مستقیم با این پلتفرم‌های ایرانی تراکنشی داشته باشید، ممکنه حسابتون محدود بشه یا حتی کل دارایی‌هاتون رو فریز و مسدود کنن!
💡
حالا باید چیکار کنیم؟
به هیچ‌وجه انتقال مستقیم ارز بین صرافی‌های ایرانی و صرافی‌های خارجی انجام ندید. حتماً از کیف پول‌های شخصی (مثل تراست ولت، یا ولت‌های سخت‌افزاری) به عنوان واسطه استفاده کنید تا مشکلی برای سرمایه‌تون پیش نیاد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/iaghapour/2680" target="_blank">📅 16:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2678">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK9FuAFngSnefbaN3genniRT66YnkcCz0v6ukb8NKBNfsxjX5dQMjR3PAPCPGHruNfn0jM7xT5X7smNDx1xT5A-Jt3di92DwjT3wu0bWyHrFfJiBCmgk5thGysg-XAIrop8MCmDrSVk91BMFvFHv_D_t2Rcl8DPjIAM6XynHi3ZSqDrTD09PJPnkaB_qDOpIJpcaDej5JUZW9TUwkAwTw732ZJ_VL3aWeVPMcy8HVSUNrWSpeiOfmKlYrkaKHGDwdqs7W1Lm7mPfdfyZOc22VgXk6SAjdNKYXReuOWjADHnNN2MOkqSrL8hAhfOB9twiGPC0MjCi1isBXq7TZ1us6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل بین سرور ایران و خارج (۲ روش سبک و سریع)
😍
🔹
تو این ویدیو قراره با هم دو تا از ساده و سبک‌ترین روش‌های تانل زدن بین سرور ایران و خارج رو یاد بگیریم. اگه برای ساخت فیلترشکن شخصی‌تون دنبال یه راه ساده و بدون دردسر برای اتصال سرورها هستید، این آموزش دقیقاً همون چیزیه که نیاز دارید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#vpn
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/iaghapour/2678" target="_blank">📅 19:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2677">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭕️
دسترسی مستقیم و بدون واسطه به اینترنت آزاد
🔹
کافی است آدرس subscription را در برنامه v2rayN/v2rayNG وارد کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
— نکات استفاده
👇🏻
۱. کانفیگ سرورلس برای اجرا نیاز به هسته Xray-core حداقل ورژن 26.6.1 دارد (حداقل v2rayNG v2.2.3)
۲. سرویسها و سایتهایی که ip آنها به طور کلی از سمت ایران بلاک شده با این روش مستقیم قابل دستیابی نیستند، همچنین از آنجایی که سرویسهای خارجی ip ایران را مشاهده میکنند، سرویسها و سایتهایی که ایران را تحریم کرده اند نیز با این روش مستقیم قابل دستیابی نیستند.
۳. در تنظیمات v2rayNG دقت کنید که Enable Hev TUN FEATURE فعال باشد و همچنین پورت پیشفرض 10808 را تغییر نداده باشید.
۴. از آپدیت بودن فایلهای جئو مطمئن شوید (قسمت Asset files در برنامه v2rayNG و قسمت Help-Check Update در برنامه v2rayN)
۵. برای تجربه بهتر پیشنهاد میشود IPv6 خود را فعال کنید (در تنظیمات v2rayNG تیک Enable IPv6 را بزنید و همچنین در صورتی که از اینترنت همراه استفاده میکنید باید IPv6 را در قسمت Access-Point گوشی خود فعال کنید)
۶. در اندروید برای عدم تداخل با (dns و sniffing) کانفیگ بهتر است Private DNS در تنظیمات اندروید و Use secure DNS در تنظیمات کروم خاموش باشد.
۷. از کانفیگها تست نگیرید، نتیجه‌ی تست ارتباطی با کار کردن یا کار نکردن این نوع کانفیگها ندارد.
🟢
به گفته یکی از بچه ها با روش زیر میتونیدمتصل بشید:
کاربر اگر فیک دی ان اس رو از تنظیمات برنامه روشن کنه سرویس هایی که آیپی ایران رو محدود و مسدود کردن مشکلش حل میشه و سایتا بالا میان.
⚠️
برای کارهای حساس از این روش استفاده نکنید!
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/iaghapour/2677" target="_blank">📅 12:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2674">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✍🏻
دوستان، در حال حاضر بیش از ۷ اسکریپت (شامل اسکریپت‌های تانل و روش‌های مستقیم و رایگان) رو در دست بررسی داریم. هر کدوم که بدون مشکل جواب بده رو توی یوتیوب معرفی می‌کنیم. اما مواردی رو که به هر دلیلی (مثل محدودیت‌های دیتاسنتر سرورهایی که استفاده میکنیم و...) نتونیم خودمون ازشون جواب بگیریم، داخل کانال تلگرام معرفی میکنیم تا شما بتونید تست کنید.
ممنون از حمایت همیشگی شما.
💚</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/iaghapour/2674" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2673">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">واقعاً باید درِ این بانک‌های مزخرف رو گل بگیرن! سالی ۳ بار یا هک می‌شید، یا اپلیکیشن بانک کار نمی‌کنه، یا اختلال دارید و هزارتا کوفت و زهر مار دیگه! آخه مگه می‌شه بانک این‌همه بی‌در و پیکر باشه؟
😒</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/iaghapour/2673" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTA5Fv1O-zps3Hiowcd2QuHav-ZM0O_pwB-25FarmLRfIvKsvdtlapqfX8EMZQQsQ61eX2aQDxhp0IXbFgRcU7YZrHlz-j9yR5MO2S5te3Y_z8I4Z-s5U7JFkqNF7GeFQMe7JJsm7oPppYInkiuAG2H1F6u3JKsE7AQZrOJJVidtQeEO1RWRSCsAeEn909AhDazUaroC17HoqI6qkw6Suw1V-MrdBTNjDd_lM-3ED_7_ereTw8M6QZXvfqam_JGCl9gMeyhf82bptGg7420E6Dfsf76XPh3pnkx4EOQnAEC3Ea_1fkd62aShk0Q-uTuKEc3AqxExU6nT9SULwdbQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
درخواست حمید رسایی و ۱۱۹ استاد برای انحلال «ستاد ویژه فضای مجازی»
بیش از ۱۲۰ تن از اساتید حوزه و دانشگاه، و چهره‌های سیاسی از جمله حمید رسایی در نامه‌ای به رئیس قوه قضائیه و فقهای شورای نگهبان، خواستار ابطال فوری مصوبه دولت برای تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی» شدند.
🔹
مهم‌ترین دلایل مخالفان:
🔸
تشکیل این ستاد ناقض جایگاه «شورای عالی فضای مجازی» به عنوان تنها نقطه کانونی سیاست‌گذاری است و یک ساختار موازی محسوب می‌شود.
🔸
به اعتقاد نویسندگان نامه، رئیس‌جمهور صلاحیت ایجاد نهادهای فراقوه‌ای با کارکردهای کلان حاکمیتی را ندارد.
🔸
واگذاری اختیار محدودسازی اینترنت به ستاد جدید، با صلاحیت قانونی (کمیته فیلترینگ) و دادستانی کل کشور در تعارض است.
🔸
ایجاد این ساختار جدید، مصداق تشکیلات غیرضروری بوده و تنها باعث افزایش لایه‌های تصمیم‌گیری در فضای مجازی می‌شود.
پ.ن: جالبه تو این مملکت انگار با فساد و رانتِ کسی کاری ندارن؛ اما وای به روزی که بخوان اینترنتی رو که دست مفسدها رو رو می‌کنه، یه ذره آزاد کنن!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/iaghapour/2671" target="_blank">📅 21:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2eGhyshQBimLQnZKxQUIE3H6lmEwdAmMHYaNsTozZ6HppmJ_tM6w7CgkUNhNnfsZGYgOM1IIw08ZuXwYjffiQGYkDgEHcPGK1k5_f7qEXA7sEZbd_y8UZ-Axar7sdAGX9aOHKUZpYBCG1heI2S-2auE_9wEEKuuPPu_tUh-Zvf1VR6bQgcvS1fb15QSE38oPu6qFtrUvwMOmkSNNWbX9FhqFtZHWsp2mPNYXKNWqnHVULpXtOxigMSpyeAuQdp4z6KIghcnaprY5_nrLr-adViKOXDB2hRsJ6SxyD-Bodeon_2WPyet1UJR2CxZg3z--inq_Na6NjwuxxzE3OrkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وزیر ارتباطات: محدودیت‌های اینترنت شفاف و زمان‌دار می‌شود / خسارت روزانه ۱۵ میلیون دلاری قطعی‌ها!
ستار هاشمی، وزیر ارتباطات در نشست خبری خود با انتقاد از وضعیت فعلی گفت: «در عصر هوش مصنوعی، دردناک است که هنوز دغدغه وصل بودن اینترنت را داریم.» وی تاکید کرد که قطعی اینترنت در فضای غبارآلود شایسته مردم نیست و سازوکار اعمال محدودیت‌ها باید تغییر کند.
🔹
چکیده مهم‌ترین صحبت‌های وزیر ارتباطات:
🔸
شفافیت و زمان‌بندی:
از این پس اگر قرار است محدودیتی ایجاد شود، باید مشخص باشد کدام نهاد و کمیته آن را تصویب کرده و
دقیقاً تا چه زمانی
ادامه دارد.
🔸
خسارت نجومی:
بر اساس گزارش مجلس، کشور روزانه ۱۵ میلیون دلار از قطعی اینترنت آسیب می‌بیند.
🔸
عادی‌شدن فیلترشکن‌ها:
استفاده از VPN که در گذشته قبح داشت، به دلیل سیاست‌های اشتباه به یک رویه عادی و روزمره برای کاربران تبدیل شده است.
پ.ن: وزیر مشکلی با محدودیت و قطعی نداره بیشتر داره میگه شما که داری قطع میکنی بگو تا کی که مردم اطلاع داشته باشن :)
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/iaghapour/2670" target="_blank">📅 21:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X93pAopMErIe4-pRzeHDSY97rpfCCdpKe1laL-PCQ_s-UTCoo45X3w7gd9JF-LCXZUARALakpLu1DgicnvaAoFzS3NgyQLBaLVbU_Iu4GTjbHnmqvpTvgFmxqbHLWqU3VN-dDWSoSJt2YUXYbHpIUQaBAs8pk1SK8RhRBsZ05E1_tKAqt94e4hTHeldHIaEeKLtCtKxcNpASVE5hoBs_p1KCDDNEUUyI3lKphDiI57wVmXlMtMHvlGZUEEoU0qzg_hSk8Qont-Z7R5Lm16VibjBRxOxxf3vwQq2WWAywiHY_vi4_Rad0ZkMOoPfCxUgMMpxIyXDnouuSnrcdhoqx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای ساخت فیلترشکن شخصی با ۲ هسته در پنل پاسارگارد
🔥
🔹
تو این ویدیو قراره با هم یاد بگیریم چطوری یه فیلترشکن شخصی فوق‌العاده با استفاده از پنل پاسارگارد بسازیم. این پنل از 2 هسته Xray و وایرگارد ساپورت میکنه و همینطور از قابلیت نود هم پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پاسارگارد
#pasarguard
#vpn
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/iaghapour/2668" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=ECRAjuQcX47Xj-PtkWIi58mu08TrAIN5HKdXGMdqWZXKHIKa4ileVSPWhUXKpL1e-FnxJEzRDzONVFnKXjBkirW2oepjQGXCtfofOhktCwkFYuoj0XlS3ku8H3KmFcrWU3n3H0m2ZCGbS9JGz4cYxiNS0fhZROOx0Aa3bu8aMz4eLC9gaxhNK88eIdNqx4pA6B3Lom2gkINUbSZjF0SMlTYkoNc_3NqPfeMeW-YTjwRs3WhR55YWBhAzlCKWq45HOuDdNLMbclEKFX1CZiAfbVhnb2I8_bW8IMS5A-gBQY2Fs_TlaeMiheRYUNsABcLf1obAEo38Ze-ZzJzbVA1umQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=ECRAjuQcX47Xj-PtkWIi58mu08TrAIN5HKdXGMdqWZXKHIKa4ileVSPWhUXKpL1e-FnxJEzRDzONVFnKXjBkirW2oepjQGXCtfofOhktCwkFYuoj0XlS3ku8H3KmFcrWU3n3H0m2ZCGbS9JGz4cYxiNS0fhZROOx0Aa3bu8aMz4eLC9gaxhNK88eIdNqx4pA6B3Lom2gkINUbSZjF0SMlTYkoNc_3NqPfeMeW-YTjwRs3WhR55YWBhAzlCKWq45HOuDdNLMbclEKFX1CZiAfbVhnb2I8_bW8IMS5A-gBQY2Fs_TlaeMiheRYUNsABcLf1obAEo38Ze-ZzJzbVA1umQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
چرا عنوان ویدیوهای یوتیوب یا زبان ویدیو برای بعضی‌ها انگلیسی شده؟!
سلام رفقا! جدیداً خیلی‌ها پیام دادید که چرا با وجود فارسی بودن ویدیوها، عنوان و توضیحات کانال رو به انگلیسی می‌بینید. یا اینکه حتی زبان ویدیو هم انگلیسی شده.
علت چیه؟
تقصیر هوش مصنوعی یوتیوبه! اگر زبان گوشی، لپ‌تاپ یا اکانت گوگل شما روی انگلیسی تنظیم شده باشه، یوتیوب به طور خودکار عنوان‌های فارسی و حتی زبان ویدیو رو براتون به انگلیسی ترجمه می‌کنه.
🛠
راه حل سریع فارسی کردن یوتیوب:
👇🏻
در اپلیکیشن موبایل:
🔹
وارد برنامه یوتیوب بشید و روی عکس پروفایلتون بزنید.
🔹
آیکون تنظیمات رو لمس کنید.
🔹
وارد بخش General و سپس App language بشید و زبان رو روی فارسی بذارید.
👇🏻
در نسخه وب (کامپیوتر/مرورگر):
🔹
سایت
YouTube.com
رو باز کنید.
🔹
روی عکس پروفایلتون در بالا سمت راست کلیک کنید.
🔹
گزینه Language رو انتخاب کرده و اون رو روی فارسی بذارید.
🎙
حل مشکل صدای انگلیسی (دوبله خودکار):
اگر وارد ویدیو شدید و دیدید صدای من انگلیسی شده، روی علامت چرخ‌دندهِ خودِ ویدیو بزنید، وارد بخش Audio track بشید و اون رو روی Original (فارسی) بذارید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/iaghapour/2667" target="_blank">📅 16:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAypsHKfYdDTAvb1nTTWtgI-lD6hllSeHth8rgu_ziIK5bgXy36DQPV702ltsa4T6ZVYGT8a4wfeMM5li9g9qIKHCcUSvos3gfte0CQF_ILqrYeL6jsmpAAxik0-ZzyeODoCs1vakg8KgDcH6Zu1orsaZX1xcHG4Cwoe0p6RLjzufjvPob_ziPgGY5H-HpJqhhSTvquo24UHqGWmacb9kyU8xIMItEwUsWYiJ4TK6y4WLL_du2OPLf5OoaULs3jY3cgqA8W_K8VoHggdoXTALlRgcfDRjaZshLtZS6EYflP7ZgE7o6adkb7CRPUxuTWwVVKD-E1S1RASO0u0UIoeGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پولی شدن پیامک فعال‌سازی تلگرام برای برخی پیش‌شماره‌ها!
🔹
تلگرام در جدیدترین به‌روزرسانی‌های خود، سیاست سخت‌گیرانه‌ای را برای ثبت‌نام یا ورود کاربران در برخی از کشورها و پیش‌شماره‌های خاص اعمال کرده است. طبق گزارش‌های کاربران و تصویر منتشر شده، بخش جدیدی به نام
SMS Fee
به اپلیکیشن اضافه شده است.
❓
ماجرا چیست؟
تلگرام اعلام کرده که به دلیل بالا بودن آمار ساخت
حساب‌های جعلی (Fake Accounts)
و همچنین
هزینه‌های بسیار سنگین ارسال پیامک بین‌المللی
در برخی از کشورها، کاربران این پیش‌شماره‌ها باید هزینه پیامک ثبت‌نام خود را پرداخت کنند.
💵
کاربران برای دریافت کد تأییدیه مجبور هستند مبلغ
۱ دلار
پرداخت کنند. تلگرام این پرداخت را در قالب
خرید اشتراک ۱ هفته‌ای تلگرام پرمیوم (Telegram Premium)
ارائه می‌دهد.
پی‌نوشت: این محدودیت فعلاً برای تمام شماره‌ها نیست و تنها روی اپراتورها و کشورهایی که هزینه‌ی مخابراتی بالایی دارند یا سوءاستفاده از آن‌ها زیاد است، فعال شده. خوشبختانه
#ایران
تو این لیست نیست ولی اگه از شماره های مجازی استفاده میکنید باید حواستون به این موضوع باشه.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/iaghapour/2664" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه چیزی میگم شاید باورتون نشه.
مردم الان بیشتر از اینکه نگران جنگ باشن نگران قطعی دوباره
#اینترنت
هستن.
کسب و کارهای آسیب دیده تا میان دوباره سرپا بشن اینترنت رو قطع میکنن یا اختلال میندازن و....
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2663" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNqfNDZKGpPQ2t5P-Jr-i_U3EM3WefF43rFBHSif7k-zPLJkWsZsNTVY52gWWF6CObLh1dN2jVAYhASqdKqSoEu1l1SXoxGAo27bSWYqfs1PCHGioXZBHxW_qQArHKWEuZJnpWTgEIOiABQG-zVt8SzO4_YuFtK18l3kCpquYVjM8xPRZJwhL4hAnBJqzebk5ufFErdamMjAbeq4dD5GIxCa3UVgMS-MjGmWo4T9UtQ6REGzoDnBqSuXTedRJ6B3XsFC3PC5Dm6LfSCSCffjL-xo6mRDP4QN0CrCoT7pRtvfnKBgMX5ETvhD-u_c7X_ByLMCEDLziuXDl8JGjyomCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مدیرعامل آسیاتک: اینترنت دیتاسنترها هنوز وصل نشده است!
محمدعلی یوسفی‌زاده اعلام کرد اینترنت کاربران وصل است اما مراکز داده دسترسی کامل ندارند و شبکه به وضعیت عادی برنگشته است.
فقدان پاسخگویی:
پیگیری‌های زیادی انجام شده، اما مسئولان هیچ دلیل یا پاسخی برای این قطع بودن ارائه نمی‌دهند.
⚠️
مشکل اصلی چیست؟
اینترنت کاربران با اینترنت دیتاسنترها مسیر متفاوتی دارد. در حال حاضر کاربران به سایت‌های داخلی دسترسی دارند، اما
سرورِ خود این سایت‌ها
در دیتاسنترها به اینترنت جهانی وصل نیستند.
—
نتیجه این اختلال:
قطع شدن اتصال سرورها به ابزارهای حیاتی خارجی مثل گوگل، کلادفلر و گیت‌هاب (APIها).
— عدم امکان آپدیت، دسترسی به ریپازیتوری‌ها و سرویس‌های ابری (CDN).
📌
نتیجه:
اینترنت دیتاسنترها قطع است؛ یعنی پلتفرم‌های ایرانی از پشت صحنه به جهان متصل نیستند و زیرساخت فنی آن‌ها عملاً فلج شده است.
پ.ن: البته از وضعیت دیتاسنترهای دیگه اطلاعات زیادی در دسترس نیست.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/iaghapour/2661" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naAbtHftmXnQV7i7jV9kxrpEJnP6oQ9X404Sx72q__2qR7iGOTdBA2TRejXN7o7Np3RW5WG8g9XTCGTjg00C-XAocUAHd1HsN-Gndgk8w2MBIrAbdQLM0RpQltnvoJUnM-2jPahIeS9MS-RYYZuAcfLfLq4yfly37BEe-HeY0luG48qx6jzHQosLco3gvVs6Yr6MmASWZvCHyoD42TD91kZSmUybivU2p2sPqAFz5pBbeB-IyvUZHJn_zog_5NLtpEyEnuQ4qn-GCyQW3hoIAv53R6Q-78yw8wT7OwhrG-mpl940P4j2L-9f0npPlmDY2HjzA6LjNj7zDsYtFv4EBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرقت بی‌اجازه ترافیک کاربران؛ پشت‌پرده دسترسی ناگهانی به کلاد و اسپاتیفای چیست؟
دسترسی ناگهانی و بدون VPN به پلتفرم‌های تحریم‌شده‌ای مثل
کلاد (Claude)
و
اسپاتیفای
، حاصل لغو تحریم‌ها نیست؛ بلکه نتیجه
دستکاری پنهان و بدون اجازه ترافیک کاربران
توسط زیرساخت اینترنت کشور است.
🔍
لایه‌های فنی و عملکرد
روش کار:
دولت ترافیک کاربران را به سمت سرورهای خود هدایت کرده و از آنجا به مقصد پروکسی می‌کند. کارشناسان این کار را مشابه
حملات هکری DNS
می‌دانند که پیش از این در سرویس‌های رفع تحریم (مثل شکن و ۴۰۳) اما این‌بار به صورت اجباری و پنهانی اجرا می‌شود.
امنیت داده‌ها:
به دلیل پروتکل‌های امنیتی، دولت توانایی دیدن محتوای پیام‌ها (مثلاً چت با هوش مصنوعی) را ندارد و فقط می‌تواند ببیند کاربر از چه سرویسی استفاده می‌کند.
⚠️
پیامدها و خطرات
خطر مسدود شدن اکانت‌ها:
ارسال انبوه درخواست‌ها از چند آی‌پی مشخص، پلتفرم‌ها را حساس کرده و ریسک مسدود شدن حساب را بالا می‌برد.
اختلال فنی:
این دستکاری باعث قفل شدن مداوم اکانت‌ها در سایت‌های تخصصی و افت شدید کیفیت VPNهای اختصاصی (به دلیل پدیده تونل در تونل) می‌شود.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/iaghapour/2660" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp798KpqfNb--sNiUiEv-hDrIjA_ij0Bio9YrXBKia0IVjL2-P-SULjTx10UnsSX2RiAKT2IkuWEGx467cQbk0dACTYcroKl-FyLK0mk3Y5fisJv25KClb9ZSQPuKpHKTnIZT23qelWfKV93NkLvkaIc9lUniSc4rs7aV47dt8Q-uySUt4keEcbwc37ddVrMdXlm4LhDqjzQleXTLz_a6Fy4RqabUDx8ojdbaEs8VAp-voa9gyi1JavIhOITwlfS8ccpQtsHbIkTq3rLaRhpPxK-s_K7fXhAFWhmHY-LZNAk4X2Cj58V71bwgDHXadOKHwQD1Bjj23eqt1y7J4AUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب خودکار داکر روی سرورهای ایران
اگر روی سرورهای داخل ایران داکر نصب می‌کنید، حتماً می‌دانید که به خاطر تحریم‌ها و اختلالات شبکه، باز کردن مخازن داکر و دانلود ایمیج‌ها مکافات است. این اسکریپت متن‌باز و امن، کل فرآیند نصب داکر را خودکار کرده و در انتها به شما اجازه می‌دهد از بین ۶ میرور ایرانی (ابرآروان، داکر آی‌آر، لیارا و...) بهترین را برای رفع تحریم انتخاب کنید.
💻
روش اجرا: کد زیر رو کپی کنید و در سرور اجرا کنید:
curl -fsSL https://gist.githubusercontent.com/ShahinDadashpour/35892443c09d582e53b36d09fb5a5df6/raw/install-docker.sh | sudo bash
🔗
لینک سورس کد در گیت‌هاب جهت بررسی
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/iaghapour/2659" target="_blank">📅 01:06 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
