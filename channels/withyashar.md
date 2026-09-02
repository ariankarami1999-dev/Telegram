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
<img src="https://cdn4.telesco.pe/file/vkr3Ud69VSP6xKDWzuSF8BHYM030NUsP3JES7G0OSEqP_Sp0JhE2YN1j_iApSkEgKn03aeoTRLowdy6S0bysCLXHJDHfeYaIHa4E86lATTKZm85cOh4vQO3uw2dfAkouGeMa8D2qJ5vrgAQN39zMjOl3eJq38YNfCje7HR4Gm6RFoiHXVPpklLJv4I9BNy7omAvIKCsOZfWRna_5NsUmCZTGqzPIu9s9PyjvJ6UyCZDwh0yb6f3z_b_qCJFdh6XbQ2SNaMYxR1So7pfAx5cF8qs8Kz-CDHSkV4cI1lJq8Ub4ZLlSW94B9ZPjUVr8JP-s9KJiecwa7f0nOXAyILtroQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-22081">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رسانه های رژیم : سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
1⃣
کمپ تیتین در اردن
حمله سنگین موشکی؛ هدف‌گیری نیروها، تأسیسات و بالگردهای آمریکایی. تسنیم مدعی کشته‌شدن نیروها و انهدام تأسیسات و بالگردهاست.
2⃣
پایگاه پرنس حسن در اردن
حمله سنگین موشکی؛ هدف‌گیری پهپادهای RQ-4 و MQ-9 و زیرساخت‌های فنی. تسنیم مدعی انهدام پهپادها و آسیب به تأسیسات است.
3⃣
پایگاه‌های آمریکا در اربیل عراق
حمله ترکیبی موشکی و پهپادی؛ هدف‌گیری مراکز تعمیراتی، انبارها، سامانه بالن جاسوسی و مخازن سوخت. تسنیم مدعی انهدام و آتش‌سوزی و کشته‌شدن نیروهاست.
4⃣
پایگاه علی‌السالم در کویت
حمله ترکیبی موشکی و پهپادی؛ هدف‌گیری قرارگاه، آشیانه و محل استقرار پهپادها. تسنیم مدعی کشته‌شدن نیروها و انهدام پهپادها و تأسیسات است.
5⃣
پایگاه نیروی دریایی آمریکا در بحرین
حمله ترکیبی موشکی و پهپادی؛ جزئیات کامل درباره نتایج حمله هنوز اعلام نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/withyashar/22081" target="_blank">📅 10:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22080">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnhnIE54b6--4cywvKY7ZjzZa_Tz-D6bTgtOVbSaPdY0Gi9Bz9j0I-ZUL3GQjJLmmv7R4F_nWS7JtWxF-ymttNFhmHJwI7WaZnanDomwyKW2edclt64UkF8pjhoXtno6i_POlNPPVqNehOdVyQVoaUa-BFlOZV1oQsU1A8-RbCqN09xxbVb_iTE1EyNCHhHvna_RonB5jDGQglfDnF8IEZFVVtc8FMdTuBFheDHmoZPvSrIevQ95Cug7eqgqvZlSPjCzGQtzxsknBAjnGPZQ5XFCiS52xcch7FFcBClZhL3zZIHzK1JlOMiy3SiRBTWgKwMsh3hFIAC88z9LRGdtvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که سه پا ادعا میکنه در ۳ روز اخیر مورد هدف قرار داده.
@WarRoom</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/22080" target="_blank">📅 10:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سه پا:
نیروهای انقلاب اسلامی بامداد امروز، یک حمله موشکی و پهپادی را علیه پایگاه آمریکایی "علی السالم" در کویت انجام دادند. این اقدام در واکنش به بمباران یک منزل مسکونی در "سیریک" صورت گرفت که منجر به شهادت ۴ نفر و زخمی شدن حدود ۷۰ نفر دیگر شد. این حمله، مقر و محل اقامت فرمانده پایگاه را هدف قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/22079" target="_blank">📅 09:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6fc9a16f.mp4?token=V6c4M7TRQa58s3HL_9LzzP70iw1YN8hfvIXdcfdZ2CNFFx6Qqaod55DlrmBydqIY8CiDfOktSB95uplUx4zRWhPywEbeB-klqv5exIjnv6JW6XpMQU1Jv5g_laIRDt7gS5FTt25LOtRp3qB0PKPPr49S8WFWDeP6mXvTXB3PVsRrSyBQCd2hNJv3tgONmcDlJ-pcY6qT0DXMrunu_GSouEJK_BM5rnT_GICZ_0eGU9XZ2cibtDvSSmEktxXXtanGdu1-m2BEf5dkNM3ge-KzxlkIWGRyzOC80YIYqHd2lCfIb7pvVB1nss1uR2udO-w7Vhcy5IK3mouS3uY90zEfIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6fc9a16f.mp4?token=V6c4M7TRQa58s3HL_9LzzP70iw1YN8hfvIXdcfdZ2CNFFx6Qqaod55DlrmBydqIY8CiDfOktSB95uplUx4zRWhPywEbeB-klqv5exIjnv6JW6XpMQU1Jv5g_laIRDt7gS5FTt25LOtRp3qB0PKPPr49S8WFWDeP6mXvTXB3PVsRrSyBQCd2hNJv3tgONmcDlJ-pcY6qT0DXMrunu_GSouEJK_BM5rnT_GICZ_0eGU9XZ2cibtDvSSmEktxXXtanGdu1-m2BEf5dkNM3ge-KzxlkIWGRyzOC80YIYqHd2lCfIb7pvVB1nss1uR2udO-w7Vhcy5IK3mouS3uY90zEfIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیلاخ چین به رژیم و ۴ شرط برای سفر قالیباف به پکن
حسین مرعشی، دبیرکل حزب کارگزاران:
چین سفر قالیباف به پکن و گسترش روابط تهران-پکن را مشروط به موارد زیر کرده است:
۱. باز کردن تنگه هرمز توسط ایران
۲. دریافت نکردن هیچ‌گونه عوارضی
۳. پایان دادن به اختلافات با عربستان
۴. پایان دادن به اختلافات با آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/22078" target="_blank">📅 09:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روابط عمومی استانداری هرمزگان:
«امیرعلی کریمی» چهار ساله، «محمد ملاحی» ۱۶ ساله، «کلثوم ملاحی نژندنیا» ۴۳ ساله و «زرخاتون طاهری» ۵۰ ساله، اسامی چهار شهید حمله دیشب به شهرستان سیریک می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/22077" target="_blank">📅 09:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWOHMFdgVjhx_3deI1tMjXYFmucusAymmVnTS16pjiHzOuoZrHx9q_vJ4R_NGzBuPdDliwZ2Zd5gvhnd8Fhf7lzygjtEeB7XkD7jzvsb4pSkmHfb03DA84Qs4yU6hz-7239ZSGW1EapG3fOvLOspTiLYmN5RnzHAY5W6_BhBRygNiyObK4cLfNgfcKUtdKyHifX8p0lXktTsAEa9Ev5uKO84x_zQ__r--ORSzIRUuagqq8kUvM5jqajrzHxDbjTZaRi8lsGSzx9r-B7CdLy1Qa_vj_sahcmojWy4ya6qrMzwNLZXdzVyG14o9d8vNqCWRbpI9K07RV4f5YapzCZ3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : من آن‌طور که ای‌بی‌سی نیوز جعلی گزارش کرده، تلاش نمی‌کنم ایران را به پای میز مذاکره بکشانم. برایم هیچ اهمیتی ندارد که آنها توافقی بی‌ارزش را امضا کنند؛ توافقی که برای خودشان هم بی‌ارزش است. من موضع کنونی‌مان را بسیار بیشتر می‌پسندم؛ با کنترل تقریباً کامل بر تنگه هرمز و اقتصادی که در حال فروپاشی کامل است. آنها فقط دارند اجتناب‌ناپذیر را به تعویق می‌اندازند.
مردم ایران قرار است چه زمانی قیام کنند و بجنگند؟
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/22076" target="_blank">📅 09:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ4yrrT7k09lPTSYb0x98TMJ4pcwccO8VW-3PrmGRSzIaavCwSSXDlPoGMT-UBfvBIqrVqffN6lv981OYOOIdBJbiCao-TidmYUSVn0AoG1aH5t8PBjURLsAhe_yMtqCO4JDuy3yCnoqA5Jbc87UOL0AJR12Mf4sx8zuZCcopafyzeNLbTzL-JThHWrgTjSta2n9fzxF7ogr826VRdjL9AUzfaXfNi5dKTvO_g4_VcprvDWRXymXuPBxIFUPnl9PwhW5XJGzHNZmEsFsVEhK1Anbr6mMdjurxgCWomI9g8IHjk2jDGqSMYzF51zGrOOruAUMOyphW_BeC19QVPwFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون ۶ هواپیما تانکر سوخترسان در محدوده تنگه هرمز به جنگنده های آمریکایی در عملیات علیه ایران مانند پمپ بنزین های هوایی خدمات میدهند
@WarRoom</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/22075" target="_blank">📅 09:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ : نمی‌خواهم ایران را به میز مذاکره بیاورم
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/22074" target="_blank">📅 09:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آکسیوس: ترامپ دستور حمله به نفتکش‌های ایرانی را صادر کرده است
آکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش آمریکا روز سه‌شنبه دو نفتکش ایرانی را در نزدیکی سواحل ایران، در شمال خط محاصره دریایی آمریکا، هدف قرار داده است. پهپادهای آمریکایی با شلیک موشک به موتورخانه این دو نفتکش حمله کردند؛ اقدامی که نخستین هدف قرار دادن مستقیم نفتکش‌های ایرانی از سوی واشنگتن در واکنش به حملات علیه کشتی‌های عبوری از تنگه هرمز محسوب می‌شود. این اقدام بخشی از سیاست جدید دولت ترامپ با عنوان «نفتکش در برابر نفتکش» برای افزایش فشار و بازدارندگی در برابر ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/22073" target="_blank">📅 08:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دیدبان اتاق جنگ : اهواز همین الان پهباد شاهد بالا سرمه @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22072" target="_blank">📅 03:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22071">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86022269b5.mp4?token=gIT4bD2jW_q82_S7_iY1JIpkCa8wPilAXCpQlS9p70HGuBBM9twH7qw3IF2yqiMZSmTZmgplZF8gtDQXe7EDksbQ8xDan765bXPA5BpPyeN0kIAT0hboxzr0Oej5YtufdKXziigglfZlvpIjHTQgQUjEt4eX5ZMXp23ymSt_BWk3RyLpRnW48LDPmEwQ27LydpBnI91X8-e3MwIvfpz3FG8RLv5kR3fWaOdGmiac5uOQkgta90g0-9vdW6ihU1oF5IgVc4v0FelEt8wvsXQbFprnxFJX4qARR-Ocib_Dub-jQaFc57Y5V2yUgOc4FotBXF0JoABUfWLfrrMpDRGdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86022269b5.mp4?token=gIT4bD2jW_q82_S7_iY1JIpkCa8wPilAXCpQlS9p70HGuBBM9twH7qw3IF2yqiMZSmTZmgplZF8gtDQXe7EDksbQ8xDan765bXPA5BpPyeN0kIAT0hboxzr0Oej5YtufdKXziigglfZlvpIjHTQgQUjEt4eX5ZMXp23ymSt_BWk3RyLpRnW48LDPmEwQ27LydpBnI91X8-e3MwIvfpz3FG8RLv5kR3fWaOdGmiac5uOQkgta90g0-9vdW6ihU1oF5IgVc4v0FelEt8wvsXQbFprnxFJX4qARR-Ocib_Dub-jQaFc57Y5V2yUgOc4FotBXF0JoABUfWLfrrMpDRGdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : اهواز همین الان پهباد شاهد بالا سرمه
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22071" target="_blank">📅 03:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0KwNHcPUhRVp0TZIJs8VjQHBK0R35Hg_oFjPsY3Hvi87bo0gJ9PiQPI-wRHr1n563hva_OKBVyN9JXHOpVAL05GpNz5XEoFjM_UW5cCMBJRRjcqU84krxcvl0lk6gSK2BbpYcR4Un03qY0brsOv9ieLlB6jbhyZYIJdAVnzO11zv2wYIpnMR4N9KBPBCeK_mV-AaZkLc8krGlYhRYbWsl1DXnSWHfwQ1uXuyLQqPV1-2HQm4C_DQMWfazpVxvJOgohlBXke9SCPNkAOPOnvDHzCaz-ZUU5dpNgPYWrOwzmunWKKgMFpDpcLSapTuEwOsEWw02KgplcDu7VJWRZ0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : هم اکنون بیمارستان میناب
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22070" target="_blank">📅 03:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پخش زنده فاکس نیوز:
امروز ایران حملاتی علیه پایگاه‌ های آمریکا در خاورمیانه انجام داد. اکنون همه ما منتظر واکنش ترامپ هستیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22069" target="_blank">📅 03:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هم اکنون حمله پهپادی جدید به اربیل عراق مواضع کورد ها
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22068" target="_blank">📅 02:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سه پا : با حمله سنگین موشک‌های بالستیک به آشیانه‌ هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ در پایگاه پرنس حسن،  تعدادی از پهپادها و تعدادی از خلبانان و خدمه فنی پروازی را از بین بردیم
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22067" target="_blank">📅 02:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">😂
😂
🙌🏾</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22066" target="_blank">📅 02:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پدافند بحرین فعال شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22065" target="_blank">📅 02:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv0LbKq5hN1cbwZoZk-5d2Fj8OfcDffiAH47oduJuZ-fFn-CE6BXAOUrZgRY0CeGNM4oWyZmqJSh90yob6aLsY81u6dMquZFv1USN5TZGE3hFGFRhkJROXo6yluBd7lM25kHq-qfVp5v2zRc1ufPQTcVVgIGxpPq_BkQtyaf4qoIsKHOs4GIXbAe3AhlPs59ZH3KPoyhTjDQDGylbuiyWnoTamuNC4I5-SpwdG35AK0ttmbubz1noKR_eG01YBwinYXxgiNb-rkefch7FRXx9IyWVcqhAaqhs6odiYVYqYERhOffhf7y7gH9hIT0_s9j8oRuYN2UoK8tHWp3seiQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند. نیروهای آمریکایی اهداف سپاه پاسداران انقلاب اسلامی را هدف قرار دادند که شامل مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22064" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb49700c6.mp4?token=A3g8fM2sU5qWMBIpbLvIfK3880llaaBU2ihPjmm3UYxx42clXPqkE-76DU9HWh6oD0KAyifwmJE1uslMfh7RpL15tpKTkQJPkFGFBKD2klvuZ-S0ClKNwwrYleY0C3-NoUBOiTepMTy1ry5DAQPHkkq-Ve7dW9ObKnjS1TVesMvyJKxu2lvya0zq69H5bgBUkRvDHUFir0ywBzGPYIox9dWTeKy5HN3mbFczXrnrS1JuoJKARIl3XFixYO93ZPfazZfaeaiqSpEezsiJMyea21dT3kD-7BeI_ketlgt02E2dSG_2WxJ2xaX9g0ONq-APbPW9Vnk_2K3B0fWDxQtukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb49700c6.mp4?token=A3g8fM2sU5qWMBIpbLvIfK3880llaaBU2ihPjmm3UYxx42clXPqkE-76DU9HWh6oD0KAyifwmJE1uslMfh7RpL15tpKTkQJPkFGFBKD2klvuZ-S0ClKNwwrYleY0C3-NoUBOiTepMTy1ry5DAQPHkkq-Ve7dW9ObKnjS1TVesMvyJKxu2lvya0zq69H5bgBUkRvDHUFir0ywBzGPYIox9dWTeKy5HN3mbFczXrnrS1JuoJKARIl3XFixYO93ZPfazZfaeaiqSpEezsiJMyea21dT3kD-7BeI_ketlgt02E2dSG_2WxJ2xaX9g0ONq-APbPW9Vnk_2K3B0fWDxQtukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
نیروهای آمریکایی اهداف سپاه پاسداران انقلاب اسلامی را هدف قرار دادند که شامل مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، توانمندی‌های مین‌گذاری و مراکز ارتباطی بود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22063" target="_blank">📅 02:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f8dab5ef2.mp4?token=GkEaIQvEfShPMkdhj8kWHc1jtIoAFbXbInZLCajA0JcIuwb0AJkXcMicNy4srGQNuSsY9xcou4VJocupNXtRaK4Ox427EDKbEwroPdOGlF8xfp798PFPO1ANmbbxQny-UtC8uLXo-lD-u-Ne96pvAWK3n_gN0UYdgtq-pvjRje4udCkWLiyOQhdj4_0CQC5PkHH5HBBSefXOkG8emCTXF-0EFoajfTCF8eOVdBA4jULwzFuTow0zgU582qCe91SSGBsNUIXg8RREekXV6AMyxG7vAt2UoEko8m5AHmYG1mR5NUPP9_VxDpZqN0OJCt6ipmYPx7VN6CWKgT00FoZokg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f8dab5ef2.mp4?token=GkEaIQvEfShPMkdhj8kWHc1jtIoAFbXbInZLCajA0JcIuwb0AJkXcMicNy4srGQNuSsY9xcou4VJocupNXtRaK4Ox427EDKbEwroPdOGlF8xfp798PFPO1ANmbbxQny-UtC8uLXo-lD-u-Ne96pvAWK3n_gN0UYdgtq-pvjRje4udCkWLiyOQhdj4_0CQC5PkHH5HBBSefXOkG8emCTXF-0EFoajfTCF8eOVdBA4jULwzFuTow0zgU582qCe91SSGBsNUIXg8RREekXV6AMyxG7vAt2UoEko8m5AHmYG1mR5NUPP9_VxDpZqN0OJCt6ipmYPx7VN6CWKgT00FoZokg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با NBC، در پاسخ به این پرسش که آیا با وجود حمایت مالی چین از تهران می‌توان ایران را به میز مذاکره آورد، گفت چارچوب این سؤال نادرست است. خبرنگار با اشاره به تهدید تهران علیه پایگاه‌های آمریکا گفت: ایران تهدید به حملات تازه می‌کند. بسنت پاسخ داد: «آن‌ها تهدید نمی‌کنند؛ در حال انجام آن هستند.» او افزود روز گذشته حدود ۱۷ میلیون بشکه نفت خام از منطقه خارج شده و این نشان می‌دهد تهران کنترل تنگه هرمز را در دست ندارد. بسنت همچنین گفت «رسانه‌ها یکی از بهترین متحدان ایران هستند» و با تأکید بر اینکه هیچ مینی در تنگه وجود ندارد، گفت دو کشتی نیز به مین برخورد نکرده‌اند. او در پایان گفت یا سپاه علیه یکدیگر برخواهد خاست، یا مردم علیه آن‌ها خواهند شورید، یا تهران به میز مذاکره بازخواهد گشت و خواهان توافقی خواهد شد که بتواند به آن پایبند بماند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22062" target="_blank">📅 02:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ZkyA4Qgx5tD8Fr9GzdCUMSuJXJl0diX5brUqPBv_ozcUTYFEghz2FPJhn0bKq9t9KhomHPAM-QzF2TEnOnsnMBSrIm7OYRAwggMxM8upnTCLIfynhifwr2QXxO6oq3FPtUjA4c_6hNCAn_lsooEty3mPXkhI1hJv43EMeEZRIK7FcBIztkmMSDH1G-sV_JFpM3g2QrcWrP9lgSQ1u2d4b8F8oW8e6JIWZunl-4hF6-nSSDyqtWvPTUWUbasyu5qpc-mpgh00okBsSrZ77eXolTKNIvXTYNZLqom2xpJrZhB4j6m9ro8LjLrDpRFYxDqja_ybDFxeo-g8nq8MDe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بسیجی هایی تجمعات حکومتی مشهد پرچمی که آورده بود و تکونش میداد به کفنش تبدیل شد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22061" target="_blank">📅 01:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش انفجار در مواضع کودر ها در اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22060" target="_blank">📅 01:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjpyvLT99-LRxj7hcl2K7NGFVsukINp6O6TywK_eBX9vlaIVOQqpYFxuuupL3Aj2C662r7VBF-s9pGjdYe61oafNo4cTz-jXjbG6bTp43G2RkLqnKbfkFsBjrxMhxaqTcHufvrAqvfsVERFxaIpW01gQN7VYPMnH8WROkSuKxBCvFp1WUVQ5gCQaDndhMIOxVhQNOwtY0xoXGl9sTErRvjY9y5wIMO0QX3VrJxtbCxuZgkKV-sLU16J4GOy8WyBseG8DEnRTMHC_y2lmsWcO9fEqxEJD4npSZlb27UkQqO3JwEvZOkU7yXiYsc8UnJBcKbYvdDB7UF38uzQu5Pyclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سه سوخت‌رسان آمریکایی، در محدوده خلیج فارس و تنگه هرمز مشغول عملیات هستند؛ یکی از آنها تازه از قطر برخاسته موضوعی که می‌تواند نشانه ادامه‌دار بودن عملیات باشد. همچنین یک فروند
E-11A BACN
(هواپیمای ارتباطی و انتقال داده در میدان نبرد که ارتباط میان هواپیماها، پهپادها و نیروهای زمینی را برقرار می‌کند) با ترانسپاندر خاموش در حال فعالیت است و موقعیت آن از طریق سیگنال‌های ماهواره‌ای برای ما قابل مشاهده شده حضور دارند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22059" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بقائی، سخنگوی وزارت خارجه رژیم، در واکنش به حمله آمریکا به یک منزل مسکونی در کوهستکِ سیریک هنگام برگزاری جشن عروسی، اعلام کرد بیش از ۵۰ زن، مرد و کودک کشته و زخمی شده‌اند. او این حمله را در ادامه حملات آمریکا به میناب، لامرد، قشم و دیگر نقاط ایران دانست و تأکید کرد ایران به این حملات «قاطعانه پاسخ خواهد داد». بقائی همچنین سکوت یا توجیه این حملات از سوی دولت‌ها و سازمان‌های بین‌المللی را به معنای بی‌طرفی ندانست و نسبت به عادی‌شدن بمباران و پیامدهای آن هشدار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22058" target="_blank">📅 01:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پدافند کویت درگیر شد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22057" target="_blank">📅 01:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">موج جدید شروع شد
گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22056" target="_blank">📅 01:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ff745370.mp4?token=OP7GWkrZ9Gu-9Ja8xjmzk0kADZ9jrpjgwqhnfTMKOJg49tfkJUq7CnwMIrcnXCwvdKNHXZvAfnKw7lUMvyJN87JCFS0Ho4QeN118xr9JJjpjOMqdn4n4c5hk9PFgkZ0Suj5fEmJCfIYhhjqRc_JNkq3IlxKzxZ8p9MX5TWoybZkUDtx2_iqZ85qbQO1W69p7aUa1agRwTFrOMzb2YTCljlm4qmOaD5hO3cTUJ2h9KI9EX0cZyeZVyBza3XedyjhmlIFdjGjmB6N0fXkvoqKCLC-9ICqIo7oQBj_y7pWYUCG8mw10BImE1WJRGQQ2uelJB-SEGotG3816J9J6_F2GDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ff745370.mp4?token=OP7GWkrZ9Gu-9Ja8xjmzk0kADZ9jrpjgwqhnfTMKOJg49tfkJUq7CnwMIrcnXCwvdKNHXZvAfnKw7lUMvyJN87JCFS0Ho4QeN118xr9JJjpjOMqdn4n4c5hk9PFgkZ0Suj5fEmJCfIYhhjqRc_JNkq3IlxKzxZ8p9MX5TWoybZkUDtx2_iqZ85qbQO1W69p7aUa1agRwTFrOMzb2YTCljlm4qmOaD5hO3cTUJ2h9KI9EX0cZyeZVyBza3XedyjhmlIFdjGjmB6N0fXkvoqKCLC-9ICqIo7oQBj_y7pWYUCG8mw10BImE1WJRGQQ2uelJB-SEGotG3816J9J6_F2GDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزعیات حادثه مشهد با یک کشته
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22055" target="_blank">📅 01:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مدیرعامل توانیر: چند نقطه از شبکه برق هرمزگان هدف حملات هوایی قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22054" target="_blank">📅 01:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره گفت: حملات به سایت‌های داخل ایران هنوز ادامه دارد و ما پایان آنها را به محض تکمیل اعلام خواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22053" target="_blank">📅 01:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پدافند شرق تهران بی قراری میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22052" target="_blank">📅 01:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جزئیات حادثۀ بلوار وکیل‌آباد مشهد
رئیس پلیس راهور خراسان‌رضوی:
این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا جنسیس سدان در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
این خودرو با یک دستگاه خودروی چانگان که در مسیر موازی در حال تردد بود، برخورد کرد که در پی این تصادف، تعادل خودروی هیوندا از دست رفت و مسیر حرکت آن تغییر کرد.
پس از این برخورد، خودرو با بشکه‌ها و علائم ترافیکی برخورد کرده و سپس وارد محدودۀ حضور جمعیتی شد که در حاشیۀ خیابان حضور داشتند.
طبق بررسی‌های انجام‌شده، رانندۀ خودرو در زمان وقوع حادثه در شرایط عادی قرار نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22051" target="_blank">📅 01:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش ایران در بیانیه‌ای اعلام کرد که در موج جدید حملات تلافی‌جویانه، پایگاه‌های آمریکا در بحرین را با پهپاد هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22050" target="_blank">📅 01:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ارتش اردن : سامانه‌های پدافند هوایی با ۱۳ فروند موشک بالستیک که وارد حریم هوایی کشور شدند مقابله کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22049" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22048" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تا موشک‌های سپاه برسه، از اون سمت بعدش آمریکا بخواد جواب بده داداشتون مثل جان اسنو  (نگهبان شب) بیداره ، یه لطفی کنین حالا همه که آنلاین هستین، چنل یوتیوب من رو سابسکرایب کنین که از هفته دیگه می‌خوام شروع کنم. اگه از تلگرام هم با من آشنا شدین که حتما برید اینستاگرام هم فالو کنین، چون اونجا هم یه مطالبی می‌ذارم مخصوص اینستاگرامه
📸
instagram.com/yashar
🐦
x.com/yasharrapfa
📺
youtube.com/yasharrapfa
⛑️
paypal.com/paypalme/yasharrapfa</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22047" target="_blank">📅 00:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارشهای تأیید نشده حاکی از اینه که تو شیراز هم یک نفر با ماشین رفته تجمعات حکومتی، یه سری فاطی کاماندو رو زیر گرفته.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22046" target="_blank">📅 00:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c3bf9130.mp4?token=A1R8g-SDKNsMWi7FplMJU_W7asDLuo1BiTMNGYFWmDCMMltilYrJ5nqdt2ohW43M5LG4QvkwdQlaUnPiMaxbS4gZCNCGjSANmqIf_0mZkXWCP5CGRuGDrODD7PxDq98YjmqZR7me2P4Z2tZs7MMe85iMO58X68Huq3MuRsknh7sUdezH0kmKTEb67DppuF-zVHtdJqFo1CplwvoOjytUA3SYiwexWyvP8ri37OP8UIQhmVpQXoH4XetdKhzgCj_IFVSaC_X0tXBZMIsdPlCZEqPMVnR5Yc6B6XiF-Vq-zJ4ExYGorQgRjG5HXzi4FB706mvtfHTo1xWLJ6A2dcuCiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c3bf9130.mp4?token=A1R8g-SDKNsMWi7FplMJU_W7asDLuo1BiTMNGYFWmDCMMltilYrJ5nqdt2ohW43M5LG4QvkwdQlaUnPiMaxbS4gZCNCGjSANmqIf_0mZkXWCP5CGRuGDrODD7PxDq98YjmqZR7me2P4Z2tZs7MMe85iMO58X68Huq3MuRsknh7sUdezH0kmKTEb67DppuF-zVHtdJqFo1CplwvoOjytUA3SYiwexWyvP8ri37OP8UIQhmVpQXoH4XetdKhzgCj_IFVSaC_X0tXBZMIsdPlCZEqPMVnR5Yc6B6XiF-Vq-zJ4ExYGorQgRjG5HXzi4FB706mvtfHTo1xWLJ6A2dcuCiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی قدس سه پا، ویدئویی را منتشر کرد که در آن، شلیک موشک‌ها به سمت پایگاه‌های آمریکایی در اردن را به تصویر کشیده است. این اقدام امشب انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22045" target="_blank">📅 00:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb2a6fd69.mp4?token=KrmbYXuFU75HXXY-Ptz_qHesBv1_2XFScyoh5Lkli9DvvaXUoPA3YQQyTrBALyZ0v_pzCvi1I_3dY3wClUvw-CFLvJ0k8-4siSxhV6Io2EhORFejGf2r-Vfjm-4QkINKYuGdPwuweo1bwmPWSsgA0pqoIDypmhutxpRCxQzqvg6nQwhSIM7rAEkbjftTt6BqEBI14i_xFJm2BFKevzdXnAmzgV7f6griviGr2AHno01hGGHid_wipl9HoF4cvJlKCeQYuPQa8ERWCGvXv11Uy7rKm-L58ZQXPAWLaZYHFmFibOsftuMy6pW5i5ZInDohDP5zlAAN1dQubNWmfAqpaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb2a6fd69.mp4?token=KrmbYXuFU75HXXY-Ptz_qHesBv1_2XFScyoh5Lkli9DvvaXUoPA3YQQyTrBALyZ0v_pzCvi1I_3dY3wClUvw-CFLvJ0k8-4siSxhV6Io2EhORFejGf2r-Vfjm-4QkINKYuGdPwuweo1bwmPWSsgA0pqoIDypmhutxpRCxQzqvg6nQwhSIM7rAEkbjftTt6BqEBI14i_xFJm2BFKevzdXnAmzgV7f6griviGr2AHno01hGGHid_wipl9HoF4cvJlKCeQYuPQa8ERWCGvXv11Uy7rKm-L58ZQXPAWLaZYHFmFibOsftuMy6pW5i5ZInDohDP5zlAAN1dQubNWmfAqpaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ابتدایی حمله کوهستک ، سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22044" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏گروه تروریستی سپاه پاسداران مدعی شد پادگان تفنگداران آمریکایی در اردن موسوم به «کمپ تبتین» را با موشک‌های بالستیک هدف قرار داده و ادعا کرد شمار زیادی از نیروهای آمریکایی در این حمله کشته شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22043" target="_blank">📅 00:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پرتاب موشک جدید از تبریز/ارومیه
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22042" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پرتاب موشک شاهین شهر
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22041" target="_blank">📅 00:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22040" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3nv1cXR2fghTdoqSvSwT3UPepLynyFdfHxEX0oJzNMgMqWuZ34PGUbwMMq-6jyo9VMVMIcD3DQnE6DkcBHg7B-6JDpMMOA1MiEXvp_OaaehsCErBirYWkQI4PpjvNsAHH_yQ7-g3JJBpSkzQFM8wMngxNgdy8j-sSEOiVcEl-mUvL67AaCcwceGZK82JCoJlArnwpEs2EM65JKYVgIOah4N6QqcJjBvwk7oUKFM2x9mxBKhotXu5UkjSY0ukH3L4qQ6oLU8BOrD8-GsSXC5F_hat54v-mlI0VRo0mkwrrQUtWkZ421McJhuoa84j2mBYJ0Fe865bT4gGnlUZJ993g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpiqsya5lTBKU0UhfRe0zsyJG0ONs_popdid3m_g31-yaCkv7gtptxn0fkqjZEqW7eNcEAyeqomkZXydzD7qPp8JY1-TsxVjIhyCoxMYC6Q0PXkqJ_Krk1idwU3va6hY3xKkFP9LGbaMRdFPTup_RX0JJLhdE0a7xXFsreFWc5rIdpZ7Le_3vD7Pqiy4q6W4z9IEfzdutgikHvgQUMk8EBR8RsBZPvxqis-MpFcqV_sMCO3k0rNYUmKzgDCL6XhrhIF2R5kcJRYgYzRg5_DlGmQfAjfCvPOiafcpCZXZjHDAtmQKuw41Wn56-2qYeSNv6OgUPArDuiHb8m2HftxUPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22034" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22033">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22033" target="_blank">📅 00:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22032">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22032" target="_blank">📅 00:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22031">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤯</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22031" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a99ae4fbb.mp4?token=hQhG88VaX1QEVeVwXGZe1VO2LirXq6aXYmBerGwdKGABXf8oWyKqOkKUmhlCXNpPDawYC4VDfiwzyXNsTmnoNKfYddwXVAzvcejxqZJfAimzuaYOO1K5viiL4pIoaj4TCO815tsukt_n3qPPuNWEbuhYCcr5irZMng72NsBRi1BqsfR3K5apGUNtT06Va9QP23QI1DSGyVWOuG2x0f5o2Lr3LWQFSZVf_ihHJUF12a3hVpPGXEuJYUaECg0a4i8CaM1yL5_cMF2tCSRoSHMwjuR9SOgx-MJvOSZXbfBnEZhNX7lnI2CTw3na4aGinf0-uzE34fD3GZEgqnFNpDHAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a99ae4fbb.mp4?token=hQhG88VaX1QEVeVwXGZe1VO2LirXq6aXYmBerGwdKGABXf8oWyKqOkKUmhlCXNpPDawYC4VDfiwzyXNsTmnoNKfYddwXVAzvcejxqZJfAimzuaYOO1K5viiL4pIoaj4TCO815tsukt_n3qPPuNWEbuhYCcr5irZMng72NsBRi1BqsfR3K5apGUNtT06Va9QP23QI1DSGyVWOuG2x0f5o2Lr3LWQFSZVf_ihHJUF12a3hVpPGXEuJYUaECg0a4i8CaM1yL5_cMF2tCSRoSHMwjuR9SOgx-MJvOSZXbfBnEZhNX7lnI2CTw3na4aGinf0-uzE34fD3GZEgqnFNpDHAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/22029" target="_blank">📅 23:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اگه الان بی بی بود ۱۵ رأس سپاهی هلاک کرده بود ۲۵ تا دیگشونم منتظر تایید بودیم که پودر شدن بخار شدن کتلت شدن یا زیر آوارن
😩</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22028" target="_blank">📅 23:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22027" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22026">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐋𝐎𝐎𝐑𝐀𝕏</strong></div>
<div class="tg-text">داداش یاشار این زارتان زورتان گفتنت واقعا برکت داره</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22026" target="_blank">📅 23:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d64055f1c.mp4?token=MXQblqgjzcmprZm2nd8myF-NU9r04DQ9Z96gxQeBpWzHdeLMHdGCDMxkPIwyhopERPsnp9WiHIQIo0PIgJzQsNC8d5Rlcp-FMMjyMpPgZx93Q-u4Luw9Rmh4BWQQbDKUbopLHAMIV39AZFT0-FkkcULfT9N-GcIstomYon-TIOrDXHQz1faJFW4YSc_dqY8P6SXqmestijrQEaLSZ8JqehsI88SY7w01l5RvRFKXQrnPQatc_Ze6CJ5tUwNtQrO_iuS5rWn6eeMoUnqtJL25oW09-wUA7jtHQ_p-KThR9zGQmKkM48pcNcl9UNaTS8en8Aw6rrjnAXttcfau2gGhMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d64055f1c.mp4?token=MXQblqgjzcmprZm2nd8myF-NU9r04DQ9Z96gxQeBpWzHdeLMHdGCDMxkPIwyhopERPsnp9WiHIQIo0PIgJzQsNC8d5Rlcp-FMMjyMpPgZx93Q-u4Luw9Rmh4BWQQbDKUbopLHAMIV39AZFT0-FkkcULfT9N-GcIstomYon-TIOrDXHQz1faJFW4YSc_dqY8P6SXqmestijrQEaLSZ8JqehsI88SY7w01l5RvRFKXQrnPQatc_Ze6CJ5tUwNtQrO_iuS5rWn6eeMoUnqtJL25oW09-wUA7jtHQ_p-KThR9zGQmKkM48pcNcl9UNaTS8en8Aw6rrjnAXttcfau2gGhMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏حمله به دکل مخابراتی سیریک با پهپاد لوکاس آمریکای (نسخه کپی شاهد)
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/22025" target="_blank">📅 23:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کاربر اتاق جنگ : وقتی از یزد میزنه یعنی جنگ ناموسی شده
@WarRoom
😂
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22024" target="_blank">📅 23:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22023">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پدافند پارچین فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22023" target="_blank">📅 23:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22022">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رسانه های داخلی : پدافند شرق تهران فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22022" target="_blank">📅 23:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22021">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22021" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22020">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzUxDLaydHU44ohZf9bm3XwpKcRBdZhzIGnSDuvjp8zmktvggHmnSKc4YKXtYKK4v0cKkc_Vlpd71L_GdVSGs2qti6Sf8H4QdhBTqC-HdSirsr1q18-4kdxxY-c6FFK92GZRUEbGhewoULGleGPw22oTORGmEgQx1VkI4VTv2Fk9hmJKuNyTBOQyxQU_Mu9G0SdIPPSIy_G72htttrGKX1oBNLy0VqxKG37zqv9NOWI3HahWkma68cifjQFOu-Vh_vWwrcTwBKUALgsFF_jHB72nQUxSPx_qdqPupbzLmSsxlzMwJhFmGg8act5DGAwP4AT_Gh2UlPOCzQ-CXarFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل کوهستک ، سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22020" target="_blank">📅 23:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22019">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پدافند اردن درگیر شد</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22019" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22018">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">از همه شهر ها گزارش پرتاب موشک دارم سه پا زد سیم آخر</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22018" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22017">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حدود ۲۰ موشک پرتاب شده</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22017" target="_blank">📅 23:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22016">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">از همه شهر ها گزارش پرتاب موشک دارم سه پا زد سیم آخر</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22016" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22015">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هیچ خبری نیست. همین خبرها رو زدم. همچنان همین خبرها رو تکراری می‌زنند. یه اسکرول کنید بالا رو ببینید لطفاً.
😁</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22015" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22014" target="_blank">📅 23:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22013" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بانک اهداف امریکا بسیار زیاد بوده امشب ! همچنان حملات ادامه داره…
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22011" target="_blank">📅 22:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">العربیه: حملات آمریکا تسلیحات و ادوات نظامی ایرانی در حال انتقال به تنگه هرمز را هدف قرار داد
آمریکا ارزیابی‌هایی در اختیار دارد که نشان می‌دهد ایران برای گسترش حملات علیه کشتیرانی طرح‌ریزی می‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22010" target="_blank">📅 22:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7aDqojGoGAsxa4n3MBgJEAg7anY5Img-8CHx21R2PJhinLursu-B-zRrP-0Y9lxpp_8jINvhy7eg9Ggj0FYBVYP6yBcXpJuC6gMWv0vMgwa9rwErQqYrtZzC8wyVeCXCZjEHPrJM1K8kyZHtQsZybZi5pbQWWKVCZF0RhT8NeavBeEpKlby4CSjK-huPi-1iHRae4TkXQLePOI41dNdqBpskz5qx_VRMACSoqEy6BGlvG_XxdumIZMUx5sIF6j-2moFBIDnEbC2wne59oKlIIwy8IZZQBZuhctaAtDilgfSqbWv1VcyO4yUHa9u9DD_Lxfe8ym_Jfgr81XZM817tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای پزشکیان
گاز کش درحال بازگشت به کشور
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22009" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجار جدید چابهار  @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22008" target="_blank">📅 22:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دیدبان اتاق جنگ : سنگین ترین انفجار قشم تا کنون صورت گرفت الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22007" target="_blank">📅 22:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرماندار سیریک : امریکا امشب یه خونه زده عروسی بوده
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22006" target="_blank">📅 22:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نیروهای آمریکایی کافی رو زدن برگشن پر و پیمون
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22005" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بی بی نتانیاهو : مگسم سمت ما نیومده حوسلمون سر رفته
😁
@WarRoom
جوک</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22004" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجار جدید چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22003" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">۳ انفجار جدید بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22002" target="_blank">📅 22:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه های رژیم
: نقاطی در بندرلنگه و جاسک در استان هرمزگان هدف حمله قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22001" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قشم رو دوباره زدن الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22000" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سیریک کلی کشته داده نیرو های که اطراف دکل بودن ترکش هم پریده اطراف
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/21999" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">معاون امنیتی و انتظامی استاندار کرمان از اصابت یک پرتابه دشمن آمریکایی به محدوده خارج از باند فرودگاه جیرفت خبر داد.
@WarRoom
تو که راست میگی
🤡</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21998" target="_blank">📅 22:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فارس: منابع عراقی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21997" target="_blank">📅 22:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21996" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21995">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAZSOl-wgGzh0eZJxqH8RtF8dv87XWxVxrbmrAIOsox8TNi3ksSjYqt8lKWIWxRL85aW50K0PS3teVs8CicWzslwFJ2xDH4hbC-kSBDSt-FkjmxvdBcBAk3BwNA6ciNiFAo3ELx5TZyHWAWl0YWjjcmJMHFgpDfGCrUJYl7ZIXQY6YD77EUKyIKfC8d0tqkf369YncO0sFZO8wfQJ6q0NXkzezhyzOnnBdFSfg186EW_WqkOvIgcaOGDu6rwhWf9msi1JKUkNTmBeTc1e5Aj3bWMkX5UtWZxJjaplhi3YDFyMTWxmzyr6QhZGkQ8x2fzYPTk9LNcJtmyiTUHuZpEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک موشک با دکل ساختمان وزارت اطلاعات سیریک برخورد کرد؛ شاهدان می‌گویند دکل متلاشی شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21995" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21994">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0159d75a.mp4?token=opY-tOg2enmoxbDy9hWXenVZkZovr_r8mk_V7mCqxJSNT1DUl50tO9XXKwliTHAHbwEvzzReY0pdmKkHrO_WqxEB6odVQCxTPlX_FOWT73FqBG3Sh0SHa-IjfeRNpaP9kd4D0fG70PCGSBCtxDAGuc7LCZ4-uIsv7gSvhgmPd4WVKUdgDr5ECsEGOIhpgK33rqP9KXjXxfM5l7JBWCRd1FIRGY0LngiFH8E1pntuFfv9NI_gRjnAhQZH5ITvdL7s8iy95F1Jv-izFqJj6VtfDI_049QSvoQVRswlYA99VqcUQo1B_p9Km22Y2-iC4jcJmu8txT5htAFGXhVFPnUn9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0159d75a.mp4?token=opY-tOg2enmoxbDy9hWXenVZkZovr_r8mk_V7mCqxJSNT1DUl50tO9XXKwliTHAHbwEvzzReY0pdmKkHrO_WqxEB6odVQCxTPlX_FOWT73FqBG3Sh0SHa-IjfeRNpaP9kd4D0fG70PCGSBCtxDAGuc7LCZ4-uIsv7gSvhgmPd4WVKUdgDr5ECsEGOIhpgK33rqP9KXjXxfM5l7JBWCRd1FIRGY0LngiFH8E1pntuFfv9NI_gRjnAhQZH5ITvdL7s8iy95F1Jv-izFqJj6VtfDI_049QSvoQVRswlYA99VqcUQo1B_p9Km22Y2-iC4jcJmu8txT5htAFGXhVFPnUn9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21994" target="_blank">📅 22:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21993">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش انفجار جدید در قشم/تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21993" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21992">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رسانه های رژیم : پهپاد شاهد در وکردیم
💨
🤡
😂
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21992" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21991">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار : حملات آمریکا همچنان ادامه دارد , فرودگاه جیرفت رو زدند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21991" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21990">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e93ddf06.mp4?token=h1m0pF2exzQCDQafYaGSGqNNtW37pi752vuRcn5CPP-FVlgx0eCx9areYmJkdXQG1qEzIbP24PsZb7ojUMWQcwgGKMT62mgLkuDVF6CEveGcori-81JIRDODNu5bynB60GoeO47FcQB9Pqg1sTm_oRyVQHaHhDFa0cGkLKAE7hyxGU13VlSWei2XBLGZANmLxzZTX1YIJfq6AFovahZZPRb1zOU8xaW-venpO-iPXKJZUVIYZ_qQY9ZqwK6mfKZBZANHVc4dHGgh6N0jXRJP7bBQShfQkfkGbtdQurc5jNx2RhO35R8uU1SMy0aBOegHbZEt80goncB08A89H_cIADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e93ddf06.mp4?token=h1m0pF2exzQCDQafYaGSGqNNtW37pi752vuRcn5CPP-FVlgx0eCx9areYmJkdXQG1qEzIbP24PsZb7ojUMWQcwgGKMT62mgLkuDVF6CEveGcori-81JIRDODNu5bynB60GoeO47FcQB9Pqg1sTm_oRyVQHaHhDFa0cGkLKAE7hyxGU13VlSWei2XBLGZANmLxzZTX1YIJfq6AFovahZZPRb1zOU8xaW-venpO-iPXKJZUVIYZ_qQY9ZqwK6mfKZBZANHVc4dHGgh6N0jXRJP7bBQShfQkfkGbtdQurc5jNx2RhO35R8uU1SMy0aBOegHbZEt80goncB08A89H_cIADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارش ها حاکی است امریکا امشب مکان های حساس جدیدی رو زده که شاید تا پایان این رژیم هم اعلام نشه ولی کار اساسی انجام شده ! @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21990" target="_blank">📅 21:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21989">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش انفجار عسلویه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21989" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21988">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ به فاکس نیوز: آن‌ها سعی کردند رادارهایشان را بازسازی کنند، زیرا چیزی نمی‌توانستند ببینند. ما منتظر ماندیم تا این بازسازی تکمیل شود و مجدداً به آن‌ها ضربه زدیم
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21988" target="_blank">📅 21:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21987">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ به فاکس نیوز : ناو هواپیمابر USS George Washington به طور کامل با مهمات پر شده است.
@WarRoom
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21987" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21986">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بمباران سیریک هم اکنون
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21986" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21985">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ به فاکس نیوز: اگر ایران به حملات ما پاسخ دهد، موجودیتش از بین خواهد رفت
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21985" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21984">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21984" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21983">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f800b25bb.mp4?token=EEg9m72POBXpPufeJd4vkMr4Ci5WtP358rZxUuvTBiucsjspTtX8gSMkz_EUNRLWuupkXOzLoZjizMDEUxcdPwYTX15tyeMuVPV8KaD4kHwPh_NAqHdIvjzHXC6uY9Ipx7lpa2d6u8KUo4jqL73cP9F1wOYBQaLuqQhreCgMQvI76rXdGPS7slv7JjnktMbxfBW1oowVIJ_V1KYm2FwLk0j_aVvQu79E_I32_CTgdhIfptbiYsc1uMUDSGYME-R4AENgWwGpkZZn4CicbZKDeJ2z_fpzanGx0J16XmIp_R23TiSR7I0U5GBZ92ihqEdC4yhkztxP9FNL8qCG4-nWmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f800b25bb.mp4?token=EEg9m72POBXpPufeJd4vkMr4Ci5WtP358rZxUuvTBiucsjspTtX8gSMkz_EUNRLWuupkXOzLoZjizMDEUxcdPwYTX15tyeMuVPV8KaD4kHwPh_NAqHdIvjzHXC6uY9Ipx7lpa2d6u8KUo4jqL73cP9F1wOYBQaLuqQhreCgMQvI76rXdGPS7slv7JjnktMbxfBW1oowVIJ_V1KYm2FwLk0j_aVvQu79E_I32_CTgdhIfptbiYsc1uMUDSGYME-R4AENgWwGpkZZn4CicbZKDeJ2z_fpzanGx0J16XmIp_R23TiSR7I0U5GBZ92ihqEdC4yhkztxP9FNL8qCG4-nWmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از دیدبان اتاق جنگ از خمین
🚨
🚨
عراقی ها مردین بدزدین
😂
😂
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21983" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21982">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پهپاد های آمریکایی حضور قاطع دارن
💥</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21982" target="_blank">📅 21:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21981">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">موشک خمین رو رو هوا رهگیری‌کردن زدن و سقوط کرد
😂
🚨
🚨
🚨
🚨
برگام
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21981" target="_blank">📅 21:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21980">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سه انفجار کوه گنو بندر عباس  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21980" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21979">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش پرتاب موشک از خمین
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21979" target="_blank">📅 21:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21978">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مقام آمریکایی: حملات آمریکا به ایران حدود دو ساعت است که ادامه دارد و بر زیرساخت‌های مورد استفاده برای هدف قرار دادن تنگه هرمز متمرکز است. واشنگتن انتظار واکنش ایران را دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21978" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21977">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیج دوم شاهزاده (دفتر شاهزاده) از دسترس خارج شد @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21977" target="_blank">📅 21:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21976">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش انفجار عسلویه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21976" target="_blank">📅 21:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21975">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارش ها حاکی است امریکا امشب مکان های حساس جدیدی رو زده که شاید تا پایان این رژیم هم اعلام نشه ولی کار اساسی انجام شده !
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21975" target="_blank">📅 21:26 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
