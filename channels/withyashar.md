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
<img src="https://cdn4.telesco.pe/file/qVHde0o13jMNt-Ec4OMzlsaB0Pc9rs22hFnG8PV42CkdxHKEt9E24yc8EjktIaGFtigglAwvqPWLK5LG5VQ-QsMxlnUd4KWPVKnqHcivASJ5Wt-Tm36WHpDlWh4A71DP_JBvNwA5T9yWULNcv9xlTwW1PbKhdpwh5hE8O4-3Qt0KxtyB81SLEVOBYCrLKAonv0hJ0TId8iKV4jJY7y7ZFv3tbK9M3nqlNBehXLVc6eJGVKXODcT49x3vsmtPu1-1gn3f2UlXx2M-UjHjE9A76Sg8ut4rkXSwNevcxPZGIfkCU_NSah-EP9yrSo_Nle4takE7v7hh2kKMqBgh62MQZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 447K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
<hr>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabf8dc5a2.mp4?token=ILTdHeqonGEegkH9Mkp4Jo5J37Rz7Ymf55MkZ5ZPBVf1-74lgd2Zz61a5X25zUwqYQTn7MXKH3nNy4o9cM2gYtdOwPkFKOtWnpSrpR6ngEyt0w0MbtifwOWvLMBdjudxfnXvQi0u3Kz60au4H5eDggORxv7N58P8ETILcrGmQcygtBfh80-ZCoaqsnZeKTa3vf-tABfGQB7eUNT3y016nlMAREHD_44bmYqxMBR2BtD7p1K_nkCJxLmwyko1mp7y0hRZHZaKk5Uo54eaKW_ffm88ffuR0L51YNvVTd284TUcpdjG_9ycZ9mFJKDxz6xOUtI48xa4VYaKXvw-zmnIjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabf8dc5a2.mp4?token=ILTdHeqonGEegkH9Mkp4Jo5J37Rz7Ymf55MkZ5ZPBVf1-74lgd2Zz61a5X25zUwqYQTn7MXKH3nNy4o9cM2gYtdOwPkFKOtWnpSrpR6ngEyt0w0MbtifwOWvLMBdjudxfnXvQi0u3Kz60au4H5eDggORxv7N58P8ETILcrGmQcygtBfh80-ZCoaqsnZeKTa3vf-tABfGQB7eUNT3y016nlMAREHD_44bmYqxMBR2BtD7p1K_nkCJxLmwyko1mp7y0hRZHZaKk5Uo54eaKW_ffm88ffuR0L51YNvVTd284TUcpdjG_9ycZ9mFJKDxz6xOUtI48xa4VYaKXvw-zmnIjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راننده جنسیسی که تجمعات مشهد رو زیر گرفت: خدا شاهده عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و بجای اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@WarRoom</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/withyashar/22113" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مارکو روبیو درباره ایران: هیچ کشوری نباید به ایران در دور زدن تحریم‌ها کمک کند. هیچ کشوری نباید به آنها در ایجاد سازوکارهایی که بتوانند از طریق آنها درآمد کسب کنند و سپس از آنها برای حمایت از تروریسم و ​​تلاش برای ساخت سلاح هسته‌ای استفاده کنند، کمک کند. و…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/22112" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b1fd93ee.mp4?token=Po7b3V3-Ek1ymfNzM1QoBte26U8eo7KHdTP5CWeU9QhibMbUilBWZ0__mdvZ2-XmWt8NQvCGzjXwN9VyB863eCtP2iGnjWJkqkluOE2ApgRdVXOUvVDjFLkTnv91SC0Snldd6zYHYBbeBCQakuaklhwxY5LwKYVcUtxaDNtMTLdGvWaldSOPuo30ZvNidr9qGl9k95InEvo1HhQvdpodcc7_guJ2rqrd6dW6SGlQnm6vyHL6B-Nr4t-HqMv5E2L8IbD2WW2lygY7ScivfQgQQQDsz8Pt4xv1GUgVjRDpKw1s-ihHx5dRLhYZRCftvhkcx8ZaaezHiRFh16jwVgQ-6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b1fd93ee.mp4?token=Po7b3V3-Ek1ymfNzM1QoBte26U8eo7KHdTP5CWeU9QhibMbUilBWZ0__mdvZ2-XmWt8NQvCGzjXwN9VyB863eCtP2iGnjWJkqkluOE2ApgRdVXOUvVDjFLkTnv91SC0Snldd6zYHYBbeBCQakuaklhwxY5LwKYVcUtxaDNtMTLdGvWaldSOPuo30ZvNidr9qGl9k95InEvo1HhQvdpodcc7_guJ2rqrd6dW6SGlQnm6vyHL6B-Nr4t-HqMv5E2L8IbD2WW2lygY7ScivfQgQQQDsz8Pt4xv1GUgVjRDpKw1s-ihHx5dRLhYZRCftvhkcx8ZaaezHiRFh16jwVgQ-6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران: هیچ کشوری نباید به ایران در دور زدن تحریم‌ها کمک کند. هیچ کشوری نباید به آنها در ایجاد سازوکارهایی که بتوانند از طریق آنها درآمد کسب کنند و سپس از آنها برای حمایت از تروریسم و ​​تلاش برای ساخت سلاح هسته‌ای استفاده کنند، کمک کند.
و اگر کشورها تصمیم به انجام این کار بگیرند، ما نیز باید آنها را تحریم کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/22111" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مسئول مرکز ایثارگران سپاه فجر فارس اعلام کرد:
حدود ساعت یک بامداد امروز، سه‌شنبه ۱۱ شهریور ، یک راننده بیل مکانیکی از نیروهای قرارگاه خاتم‌ و بسیجیان سه پا ناحیه فسا که در پروژه‌های عمرانی شهرستان جهرم مشغول فعالیت بود، در پی حمله آمریکا به این شهرستان کشته شد.
@WarRoom</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/22110" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCBa8y0tIwCQpgbI6ILN-zWWxyfRO6BYss0-tfsBaeVII1AOZe1rnpZQ-tFoUMJ59Pt537tiL1fskACsrADqSsmY2QynlIgdyuxuIDTixsplUBWhw-O2NdBGTowo9mbucgu4XK4otCrBy-pmiJeKX9vnO39vTYft9xJZycguvZigP8TQ6U6P6TyrwiVskgEQ9Z7iBscw3SpqFMxHHrIb_F_61Mvj0GUzRyrz4tjvn21k7UtTj0ICJvJAGZBkla790OlENALK_InFMojfjVzDnHlkDT0_cOID-14NL_AeH6zSlLKWQdw4g2qi6fNmgQj4aWOLzCHe3rj3746MlxZMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ترامپ در تروث :
اکنون که این منطقه تحت کنترل ایالات متحده قرار دارد، آیا باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم؟
درست مانند خود آمریکا، این منطقه از همیشه «داغ‌تر» خواهد بود!
@WarRoom</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/22109" target="_blank">📅 19:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3b32fad2.mp4?token=MukLS1um51-tcuOH0jEA-JOZp-YMj17iL4SpLdhaxyF-qhv_vcF8oVvcg46cV7RFJSpnHRS1nR_2qgQ-X2vjXOrYu7Dvx6kRZL0iuvmsA_0xBdAnAW4wPXfhio-dOT59sqzoRQfZ5a7O0rUuyFs9g791lqE5aJ1cCedrnvZaPH0SOZivgOnn7fGUU1XAUQuYPDkSafZwNcLosajF8EuvnF3e0ZAqYnFfZq9ac9wD5ylapeCsEWtA7rh-Y80o9qSiBSiBYxav3LFNR_ASVMEHM0rQb-SQGhCSYPxgH5ZXgZfBqm2Op0TbM9RXJHIXlCQQfdpXqaT0KJvfgL_M_CcOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3b32fad2.mp4?token=MukLS1um51-tcuOH0jEA-JOZp-YMj17iL4SpLdhaxyF-qhv_vcF8oVvcg46cV7RFJSpnHRS1nR_2qgQ-X2vjXOrYu7Dvx6kRZL0iuvmsA_0xBdAnAW4wPXfhio-dOT59sqzoRQfZ5a7O0rUuyFs9g791lqE5aJ1cCedrnvZaPH0SOZivgOnn7fGUU1XAUQuYPDkSafZwNcLosajF8EuvnF3e0ZAqYnFfZq9ac9wD5ylapeCsEWtA7rh-Y80o9qSiBSiBYxav3LFNR_ASVMEHM0rQb-SQGhCSYPxgH5ZXgZfBqm2Op0TbM9RXJHIXlCQQfdpXqaT0KJvfgL_M_CcOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران: ما الان کنترل تنگه هرمز رو در دست داریم. کنترلش می‌کنیم.
دیشب ۲۸ تا قایق، ۲۸ تا شناور رو از بین بردیم. ما تنگه رو تحت کنترل داریم؛ اونا دیگه چیزی گیرشون نمیاد و ما چندین شناور رو هم زدیم.
@WarRoom</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/22108" target="_blank">📅 19:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3543df88e.mp4?token=NRt42UoTpSslzyI_j6qGmdB5pLustT-oHWA-FzYqxA7TdOIWQOplhKUkUyYa5E8YpwmE6skJgHSEuiymBPM03u6I_JR-4o-0cYUWk02m19ScLAXM7jwnVzzdNJTAT6eRJll-3z2ie5N7u7IkWdZWlzAHN8QSslm-Tx5kPnSeTPOcXeknvedxjZUEPlLVynIosXs1jfXPQfW2B9mFLu8m4PQ9iQTTBUm7jUO7RGaKoAz1tIneCRFnthCr2Yi55oW6dhNWJgJmOAUG4D2oS_EX7OSfv7Xfc2dHd57xzp6vyKUSYY7Lgz-sd--wl4GXJYSoPdO9Y6tZ_ly2LlKw5Erzaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3543df88e.mp4?token=NRt42UoTpSslzyI_j6qGmdB5pLustT-oHWA-FzYqxA7TdOIWQOplhKUkUyYa5E8YpwmE6skJgHSEuiymBPM03u6I_JR-4o-0cYUWk02m19ScLAXM7jwnVzzdNJTAT6eRJll-3z2ie5N7u7IkWdZWlzAHN8QSslm-Tx5kPnSeTPOcXeknvedxjZUEPlLVynIosXs1jfXPQfW2B9mFLu8m4PQ9iQTTBUm7jUO7RGaKoAz1tIneCRFnthCr2Yi55oW6dhNWJgJmOAUG4D2oS_EX7OSfv7Xfc2dHd57xzp6vyKUSYY7Lgz-sd--wl4GXJYSoPdO9Y6tZ_ly2LlKw5Erzaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
من به مردمم گفتم: "ما باید در جایی به نام ایران، جمهوری اسلامی ایران، متوقف شویم و باید آنها را از داشتن سلاح هسته‌ای بازداریم."
شما می‌خواهید مشکلی ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند. شما نیمی از جهان را نابود خواهید کرد. آنها بیمار هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/22107" target="_blank">📅 18:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صدای انفجارهایی در کشور کویت شنیده شد که از استان بصره عراق نیز قابل شنیدن بوده
@WarRoom</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/22106" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مارکو روبیو: ایالات متحده به هدف قرار دادن ایران در واکنش به حملات علیه کشتی‌ها ادامه خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/22105" target="_blank">📅 18:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقام اسرائیلی:تلاش برای دستیابی به توافق امنیتی با سوریه شکست خورد.
تمایل سوریه برای دستیابی به توافق با اسرائیل پس از لغو برخی تحریم‌ها علیه دمشق کاهش یافته است.
کانال‌های ارتباطی با دولت سوریه همچنان برقرار هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/22104" target="_blank">📅 18:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نرخ دلار ۲۲۱،۵۰۰ تومان(سقف تاریخی)
دلار کف بازار :۲۲۵-۲۲۷ هزار تومان!
تتر ۲۱۹،۰۵۲ تومان (سقف تاریخی)
بیتکوین ۷۷،۳۴۰ $
انس جهانی طلا ۴،۳۸۵ $
نفت برنت  ۹۴،۵۰$
@WarRoom
🚨
🚨
🚨
🚨
۶ عصر تهران</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/22103" target="_blank">📅 18:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیویورک تایمز: امشب می‌تواند بدتر از دیشب باشد فقط باید منتظر ماند!
@WarRoom</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/22102" target="_blank">📅 17:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبر زنده فاکس نیوز:
ترامپ ممکن است امشب دستور حمله مجدد بدهد
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/22101" target="_blank">📅 17:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سه پا نبی اکرم کرمانشاه در بیانیه‌ای اعلام کرد:
شب گذشته 4 پرسنل نیروی هوافضای این استان در پی حمله ارتش آمریکا به لانچر موشک بالستیک کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22100" target="_blank">📅 16:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxdhly18eKbcJSPcsfXIYUpCOIAjcPQz1JISSQ084gUztH8U-NycAGwLeCZYxSMQkbK_Px0qGGOUZ6IL7meZF-1co9Liiyikgqy5XsgDzyitkfQMOeC8sD8vSWt3NrhAAHfD_zqYpoHwQa0v36kD10CokjTMwzDcv4aDmOeddzm9avm1tiMBx0kAf3csjikbVkhm42hmgrKMbxyyuKGuYCoabNdLaiq6r4qZ5fkOrpXlfjUWvYzmuumraI0P5eVNi67cexOREKUGkuiCestd-i2re1GouetUi25pKGDAHnRWMGccFQ1QzCZZsVfhimPelkGqOSLlSIAMHMSVhrLFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجیکالا داره تتر میفروشه چهارقسطه
16 هزار تومن بالاتر از قیمت 215 تومن.
تتر قسطی دیگه چیه ؟! جیانکارلو دواسینی میگن دو تا سکته رد کرد بعد دیدن این پست
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22099" target="_blank">📅 16:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی مرتبط با یک نفتکش خبر داد که در پی آن دو نفر کشته یا زخمی شده‌اند و این حادثه در حال بررسی است. @WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22098" target="_blank">📅 16:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/542ffb7905.mp4?token=LEpasbfuZem5v6vCZp_2QjBQcAEr0bWzWNeJw09UGADMgB-xKJ9aSn6NYWuJv7a1XNVkUBjzN8-Z1Jm1Yol6vggv5GRXy_eHN-KS-S5s4UHuNC5uVzPUPYHwPSeOeGoE8ycGC99edS_uq0_pi0M99sEQd0i1KFyq_QrDA0AP-jEFIIM9VVg4nbC11Ax58zcn7JxZJeBXXNoGi9NiHvulU2P9m8uvGkgukASi8h3qUvblnhFGLCb2AG2CAZXEpxlUottcnt3nQPAU0PMSrt1YvDaVPxqEex_FLv3C8aPHBmwmVTPe-HyEQoi99Q2bdfGrjzBlL3FCat-LBWAz78rM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/542ffb7905.mp4?token=LEpasbfuZem5v6vCZp_2QjBQcAEr0bWzWNeJw09UGADMgB-xKJ9aSn6NYWuJv7a1XNVkUBjzN8-Z1Jm1Yol6vggv5GRXy_eHN-KS-S5s4UHuNC5uVzPUPYHwPSeOeGoE8ycGC99edS_uq0_pi0M99sEQd0i1KFyq_QrDA0AP-jEFIIM9VVg4nbC11Ax58zcn7JxZJeBXXNoGi9NiHvulU2P9m8uvGkgukASi8h3qUvblnhFGLCb2AG2CAZXEpxlUottcnt3nQPAU0PMSrt1YvDaVPxqEex_FLv3C8aPHBmwmVTPe-HyEQoi99Q2bdfGrjzBlL3FCat-LBWAz78rM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت درباره ایران :
«ما اختیارات جدیدی برای وزارت خزانه‌داری ایجاد کرده‌ایم تا بتواند در حوزه‌های
هوانوردی، دریانوردی و دارایی‌های دیجیتال
تحریم‌هایی اعمال کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22097" target="_blank">📅 16:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe871b13a.mp4?token=C2H3x9C8ArPbt9ZBRXquOLiwQAFQ7VXMCrEnr1fHAsqkLyCEjAKureOpCKZ4AbPce-IdPD_Typziqq3RFkcpeJh-CzXLet8E5qlB63iUQnwvMCw-uuEa5AvXZa7UkKHzbwhRJvNjuHci-ywoRY20Zez2nC0dgNVFE7B3WIAD2yvKtSnDPBl6wwN7QX-MVhylLbmH4OjtQ2gJyOFValVxMYvA776y08XvBu_GjD72zER563j2JlLdIH4QmVlA3XPJdbzusibnngQu6xMxItVTuY1JbGt47SU1mGUgy4GmzKBo-7XoU0YeInK2Vz_gkMZFi5H6JVchnBUbPFlvqM2X2j9RWal9WyqEci3HNFL7dcoYrczNO7IkHu0TTP9gXgKDYLLKPICf_zqxwy_Z5ATMo__9X0PkOOvDMLmzNManx9Q_185T_k16KjLOtx_vlZetTQ4-_9aFPzhT3kK1FSCuKCkP4TFs0bNf3LXIUPPC5GMm4rGgilkXWPUdaB71hfO4E30xm_EOcgZ1aChWFbcUjgiVUZmlYOS8UD6cYw7wOrtDI4Dd1ICX5qo8SQ9ZLdui98gjzTY_DNq0VUmghcsSmpjfdQp7SJZ96ny1h2ImdJonX4E0fUvE-UavIXKG2gTgk7gilMmHrK9jicebrUkoD5DjJJID0XVC2v-3mlEcveM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe871b13a.mp4?token=C2H3x9C8ArPbt9ZBRXquOLiwQAFQ7VXMCrEnr1fHAsqkLyCEjAKureOpCKZ4AbPce-IdPD_Typziqq3RFkcpeJh-CzXLet8E5qlB63iUQnwvMCw-uuEa5AvXZa7UkKHzbwhRJvNjuHci-ywoRY20Zez2nC0dgNVFE7B3WIAD2yvKtSnDPBl6wwN7QX-MVhylLbmH4OjtQ2gJyOFValVxMYvA776y08XvBu_GjD72zER563j2JlLdIH4QmVlA3XPJdbzusibnngQu6xMxItVTuY1JbGt47SU1mGUgy4GmzKBo-7XoU0YeInK2Vz_gkMZFi5H6JVchnBUbPFlvqM2X2j9RWal9WyqEci3HNFL7dcoYrczNO7IkHu0TTP9gXgKDYLLKPICf_zqxwy_Z5ATMo__9X0PkOOvDMLmzNManx9Q_185T_k16KjLOtx_vlZetTQ4-_9aFPzhT3kK1FSCuKCkP4TFs0bNf3LXIUPPC5GMm4rGgilkXWPUdaB71hfO4E30xm_EOcgZ1aChWFbcUjgiVUZmlYOS8UD6cYw7wOrtDI4Dd1ICX5qo8SQ9ZLdui98gjzTY_DNq0VUmghcsSmpjfdQp7SJZ96ny1h2ImdJonX4E0fUvE-UavIXKG2gTgk7gilMmHrK9jicebrUkoD5DjJJID0XVC2v-3mlEcveM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیوز
:
پوتین عملاً به ایران گفت: «ما پشت شما هستیم.» پیام شما به روس‌ها چیست؟
بسنت
:
«پیام من به همه این است:
دور بمانید.
»
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22095" target="_blank">📅 16:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHWQkv6ObtiVJVVUG1fWcRFAjSnH7josMSuhjhAgRHSR9WjJEGnWvqHmGkzTMsPoFuwXUobnMtlDY_pnVzkx2rJwhQofMVioJszAd3IwMesR5ex9BroNZl5-n102J6Ex0kuSDRF7DIkO8r2o7oGlltnnrbIf5ZGdHF4WkpTdFduAYooHVweBWO4RikXru5o2Y1TenqoZU0xmberR5vKp_WAOL2GcXz8u1ipZA4vCsO-t_eA14TiJO3ibO99s-VpSqpZ1HweLg-8MfluTgyv3-x2cZSp4YgQI7HOtgtWQu_pV9v-_bAp5eD9Hh-mc8wdlzHBm_zWOnP7P22fEBTj23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی مرتبط با یک نفتکش خبر داد که در پی آن دو نفر کشته یا زخمی شده‌اند و این حادثه در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22094" target="_blank">📅 15:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هواپیمای پزشکیان گاز کش درحال بازگشت به کشور  @WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22093" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ در تروث : من آن‌طور که ای‌بی‌سی نیوز جعلی گزارش کرده، تلاش نمی‌کنم ایران را به پای میز مذاکره بکشانم. برایم هیچ اهمیتی ندارد که آنها توافقی بی‌ارزش را امضا کنند؛ توافقی که برای خودشان هم بی‌ارزش است. من موضع کنونی‌مان را بسیار بیشتر می‌پسندم؛ با کنترل…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22092" target="_blank">📅 15:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش صداوسیما: تنگۀ هرمز همچنان بسته است و کشتی‌های مختلف هدف قرار می‌گیرند
گزارش خبرنگار شبکه سه از جزیره لارک؛ جزیره‌ای که هدف حمله آمریکا قرار گرفت و در پی آن تعدادی از نیروهای نیروی دریایی سه پا کشته و زخمی‌شدن‌
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22091" target="_blank">📅 14:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22090">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoh</strong></div>
<div class="tg-text">داداش ما بانكوك رسيديم تازه بريم واسه قدر دانى از بچه ها ابرام؟</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22090" target="_blank">📅 14:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارک لوین : ترامپ  اکنون در حال خفه کردن دشمنه ( رژیم ایران )
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22089" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ناو آبراهام لینکلن رسید پاتایا
🥴
😂
ناو هواپیمابر آبراهام لینکلن CVN72 پس از ۲۸۶ روز متوالی حضور در دریا و جنگ با ایران ، که یک رکورد مدرن برای نیروی دریایی ایالات متحده است، در تاریخ ۲ سپتامبر امروز به بندر لائم چابانگ تایلند رسید.انتظار می‌رود هزاران پرسنل از پاتایا، شهری در نزدیکی این مکان، بازدید کنند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22088" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نرخ دلار ۲۲۰،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار :نامعلوم ! تونستی بخر!
تتر ۲۱۸،۰۰۰ تومان (سقف تاریخی)
بیتکوین ۷۷،۲۴۸ $
انس جهانی طلا ۴،۳۲۱ $
نفت برنت  ۹۴،۹۱$
@WarRoom
🚨
🚨
🚨
🚨
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22087" target="_blank">📅 12:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، در مورد ایران:
احتمال حمله ایران به اسرائیل وجود دارد ! میگین چرا؟ برای فرار از منطقه!
بین محاصره و جنگ، آنها ممکن است دومی را ترجیح دهند.
ما برای این کار آماده‌ایم، به خصوص که در فصل تعطیلات هستیم.
آنها دوست دارند در تعطیلات یهودیان حمله کنند زیرا از یهودیان متنفرند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22086" target="_blank">📅 12:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU5A9WNTJ_TyECiwqOqoVvzEkgVFZVBqrLqxkMb51OzBx_HSrE7SVEfeyouCeqO4P7OpjtFTRlkWQzrw-ik_Zxkt_TBMrsZ96xDYZUftKj1TuPTpNRi76cReIqxBIA-xHiUmKhh2ixnuCVtmMlT-Yonuqab4Vz8Da93Z-XJ-c7GajdOPq4Df8AGLKGvPmPIlrTRvP_97wigMRmUVhKri7xpk4yuu76quWINMMKWYxpzIBQ4QCo4JhhdoPB1rjJ1KRYLy2eh22Q2NedR8XxIp1HNI0nTphkahaUpHnK_EBkhvE01qiaD77EMvpGSq_G3Xup6VLMqe66p7GEhJKZ40yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاصله حدود ۱۳۶ متری بین دکل مخابراتی و محل عروسی در کوهستک سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22085" target="_blank">📅 11:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22084">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر دفاع اسرائیل: با آمریکا برای دفاع و حمله هماهنگی کامل داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22084" target="_blank">📅 11:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjjMCH9QW4kMJS-Dqj7CELAhfnILKM_Jaor5t11o_f21v83igNSm7O25ddbm7kpXSdHONWrBOnXef0uST0rmALcNv4jTedm9VI3-EIF0wYQdktBptf0xlh19EBCpb6kG55VCYxmpkvbdpcPEgVMIGM4G5ui6AgMNxOb-kggVkXKyLzSjwHpu3zQjM0ykuk716ICgjJ2QNKbGIpthMT9sq2OTqp6FXmGjFuv632e1_cu4Z50Y34zY5QyN1ryTq_Ki-wCQOyzmTA8Xzw4NzJfJEyqSx51LsNHnKDaul-M3MTrjWbYKgTQofkb_hkruoRtLJpjuhQIJMXmz05qGmZSaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود ارومیه
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22083" target="_blank">📅 10:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">۳ بسیجی شهرستان دیر درجزیره لاوان کشته
شدند
جانشین فرمانده سه پا سیدالشهدا شهرستان دیّر:در این تهاجم، «مهدی بحرانی»، «حسین صالح‌نژاد» و «حسن مؤمنی» کشته و تعدادی دیگر از نیروهای مدافع امنیت شهرستان دیّر نیز مجروح شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22082" target="_blank">📅 10:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22081">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22081" target="_blank">📅 10:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22080">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnhnIE54b6--4cywvKY7ZjzZa_Tz-D6bTgtOVbSaPdY0Gi9Bz9j0I-ZUL3GQjJLmmv7R4F_nWS7JtWxF-ymttNFhmHJwI7WaZnanDomwyKW2edclt64UkF8pjhoXtno6i_POlNPPVqNehOdVyQVoaUa-BFlOZV1oQsU1A8-RbCqN09xxbVb_iTE1EyNCHhHvna_RonB5jDGQglfDnF8IEZFVVtc8FMdTuBFheDHmoZPvSrIevQ95Cug7eqgqvZlSPjCzGQtzxsknBAjnGPZQ5XFCiS52xcch7FFcBClZhL3zZIHzK1JlOMiy3SiRBTWgKwMsh3hFIAC88z9LRGdtvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که سه پا ادعا میکنه در ۳ روز اخیر مورد هدف قرار داده.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22080" target="_blank">📅 10:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سه پا:
نیروهای انقلاب اسلامی بامداد امروز، یک حمله موشکی و پهپادی را علیه پایگاه آمریکایی "علی السالم" در کویت انجام دادند. این اقدام در واکنش به بمباران یک منزل مسکونی در "سیریک" صورت گرفت که منجر به شهادت ۴ نفر و زخمی شدن حدود ۷۰ نفر دیگر شد. این حمله، مقر و محل اقامت فرمانده پایگاه را هدف قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22079" target="_blank">📅 09:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22078" target="_blank">📅 09:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روابط عمومی استانداری هرمزگان:
«امیرعلی کریمی» چهار ساله، «محمد ملاحی» ۱۶ ساله، «کلثوم ملاحی نژندنیا» ۴۳ ساله و «زرخاتون طاهری» ۵۰ ساله، اسامی چهار شهید حمله دیشب به شهرستان سیریک می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22077" target="_blank">📅 09:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22076" target="_blank">📅 09:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ4yrrT7k09lPTSYb0x98TMJ4pcwccO8VW-3PrmGRSzIaavCwSSXDlPoGMT-UBfvBIqrVqffN6lv981OYOOIdBJbiCao-TidmYUSVn0AoG1aH5t8PBjURLsAhe_yMtqCO4JDuy3yCnoqA5Jbc87UOL0AJR12Mf4sx8zuZCcopafyzeNLbTzL-JThHWrgTjSta2n9fzxF7ogr826VRdjL9AUzfaXfNi5dKTvO_g4_VcprvDWRXymXuPBxIFUPnl9PwhW5XJGzHNZmEsFsVEhK1Anbr6mMdjurxgCWomI9g8IHjk2jDGqSMYzF51zGrOOruAUMOyphW_BeC19QVPwFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون ۶ هواپیما تانکر سوخترسان در محدوده تنگه هرمز به جنگنده های آمریکایی در عملیات علیه ایران مانند پمپ بنزین های هوایی خدمات میدهند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22075" target="_blank">📅 09:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ : نمی‌خواهم ایران را به میز مذاکره بیاورم
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22074" target="_blank">📅 09:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22073">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آکسیوس: ترامپ دستور حمله به نفتکش‌های ایرانی را صادر کرده است
آکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش آمریکا روز سه‌شنبه دو نفتکش ایرانی را در نزدیکی سواحل ایران، در شمال خط محاصره دریایی آمریکا، هدف قرار داده است. پهپادهای آمریکایی با شلیک موشک به موتورخانه این دو نفتکش حمله کردند؛ اقدامی که نخستین هدف قرار دادن مستقیم نفتکش‌های ایرانی از سوی واشنگتن در واکنش به حملات علیه کشتی‌های عبوری از تنگه هرمز محسوب می‌شود. این اقدام بخشی از سیاست جدید دولت ترامپ با عنوان «نفتکش در برابر نفتکش» برای افزایش فشار و بازدارندگی در برابر ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22073" target="_blank">📅 08:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دیدبان اتاق جنگ : اهواز همین الان پهباد شاهد بالا سرمه @WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22072" target="_blank">📅 03:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22071">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86022269b5.mp4?token=gIT4bD2jW_q82_S7_iY1JIpkCa8wPilAXCpQlS9p70HGuBBM9twH7qw3IF2yqiMZSmTZmgplZF8gtDQXe7EDksbQ8xDan765bXPA5BpPyeN0kIAT0hboxzr0Oej5YtufdKXziigglfZlvpIjHTQgQUjEt4eX5ZMXp23ymSt_BWk3RyLpRnW48LDPmEwQ27LydpBnI91X8-e3MwIvfpz3FG8RLv5kR3fWaOdGmiac5uOQkgta90g0-9vdW6ihU1oF5IgVc4v0FelEt8wvsXQbFprnxFJX4qARR-Ocib_Dub-jQaFc57Y5V2yUgOc4FotBXF0JoABUfWLfrrMpDRGdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86022269b5.mp4?token=gIT4bD2jW_q82_S7_iY1JIpkCa8wPilAXCpQlS9p70HGuBBM9twH7qw3IF2yqiMZSmTZmgplZF8gtDQXe7EDksbQ8xDan765bXPA5BpPyeN0kIAT0hboxzr0Oej5YtufdKXziigglfZlvpIjHTQgQUjEt4eX5ZMXp23ymSt_BWk3RyLpRnW48LDPmEwQ27LydpBnI91X8-e3MwIvfpz3FG8RLv5kR3fWaOdGmiac5uOQkgta90g0-9vdW6ihU1oF5IgVc4v0FelEt8wvsXQbFprnxFJX4qARR-Ocib_Dub-jQaFc57Y5V2yUgOc4FotBXF0JoABUfWLfrrMpDRGdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : اهواز همین الان پهباد شاهد بالا سرمه
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22071" target="_blank">📅 03:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0KwNHcPUhRVp0TZIJs8VjQHBK0R35Hg_oFjPsY3Hvi87bo0gJ9PiQPI-wRHr1n563hva_OKBVyN9JXHOpVAL05GpNz5XEoFjM_UW5cCMBJRRjcqU84krxcvl0lk6gSK2BbpYcR4Un03qY0brsOv9ieLlB6jbhyZYIJdAVnzO11zv2wYIpnMR4N9KBPBCeK_mV-AaZkLc8krGlYhRYbWsl1DXnSWHfwQ1uXuyLQqPV1-2HQm4C_DQMWfazpVxvJOgohlBXke9SCPNkAOPOnvDHzCaz-ZUU5dpNgPYWrOwzmunWKKgMFpDpcLSapTuEwOsEWw02KgplcDu7VJWRZ0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : هم اکنون بیمارستان میناب
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22070" target="_blank">📅 03:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پخش زنده فاکس نیوز:
امروز ایران حملاتی علیه پایگاه‌ های آمریکا در خاورمیانه انجام داد. اکنون همه ما منتظر واکنش ترامپ هستیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22069" target="_blank">📅 03:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هم اکنون حمله پهپادی جدید به اربیل عراق مواضع کورد ها
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22068" target="_blank">📅 02:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22067">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سه پا : با حمله سنگین موشک‌های بالستیک به آشیانه‌ هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ در پایگاه پرنس حسن،  تعدادی از پهپادها و تعدادی از خلبانان و خدمه فنی پروازی را از بین بردیم
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22067" target="_blank">📅 02:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">😂
😂
🙌🏾</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22066" target="_blank">📅 02:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پدافند بحرین فعال شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22065" target="_blank">📅 02:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv0LbKq5hN1cbwZoZk-5d2Fj8OfcDffiAH47oduJuZ-fFn-CE6BXAOUrZgRY0CeGNM4oWyZmqJSh90yob6aLsY81u6dMquZFv1USN5TZGE3hFGFRhkJROXo6yluBd7lM25kHq-qfVp5v2zRc1ufPQTcVVgIGxpPq_BkQtyaf4qoIsKHOs4GIXbAe3AhlPs59ZH3KPoyhTjDQDGylbuiyWnoTamuNC4I5-SpwdG35AK0ttmbubz1noKR_eG01YBwinYXxgiNb-rkefch7FRXx9IyWVcqhAaqhs6odiYVYqYERhOffhf7y7gH9hIT0_s9j8oRuYN2UoK8tHWp3seiQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند. نیروهای آمریکایی اهداف سپاه پاسداران انقلاب اسلامی را هدف قرار دادند که شامل مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات…</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22064" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22063">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22063" target="_blank">📅 02:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f8dab5ef2.mp4?token=GkEaIQvEfShPMkdhj8kWHc1jtIoAFbXbInZLCajA0JcIuwb0AJkXcMicNy4srGQNuSsY9xcou4VJocupNXtRaK4Ox427EDKbEwroPdOGlF8xfp798PFPO1ANmbbxQny-UtC8uLXo-lD-u-Ne96pvAWK3n_gN0UYdgtq-pvjRje4udCkWLiyOQhdj4_0CQC5PkHH5HBBSefXOkG8emCTXF-0EFoajfTCF8eOVdBA4jULwzFuTow0zgU582qCe91SSGBsNUIXg8RREekXV6AMyxG7vAt2UoEko8m5AHmYG1mR5NUPP9_VxDpZqN0OJCt6ipmYPx7VN6CWKgT00FoZokg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f8dab5ef2.mp4?token=GkEaIQvEfShPMkdhj8kWHc1jtIoAFbXbInZLCajA0JcIuwb0AJkXcMicNy4srGQNuSsY9xcou4VJocupNXtRaK4Ox427EDKbEwroPdOGlF8xfp798PFPO1ANmbbxQny-UtC8uLXo-lD-u-Ne96pvAWK3n_gN0UYdgtq-pvjRje4udCkWLiyOQhdj4_0CQC5PkHH5HBBSefXOkG8emCTXF-0EFoajfTCF8eOVdBA4jULwzFuTow0zgU582qCe91SSGBsNUIXg8RREekXV6AMyxG7vAt2UoEko8m5AHmYG1mR5NUPP9_VxDpZqN0OJCt6ipmYPx7VN6CWKgT00FoZokg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با NBC، در پاسخ به این پرسش که آیا با وجود حمایت مالی چین از تهران می‌توان ایران را به میز مذاکره آورد، گفت چارچوب این سؤال نادرست است. خبرنگار با اشاره به تهدید تهران علیه پایگاه‌های آمریکا گفت: ایران تهدید به حملات تازه می‌کند. بسنت پاسخ داد: «آن‌ها تهدید نمی‌کنند؛ در حال انجام آن هستند.» او افزود روز گذشته حدود ۱۷ میلیون بشکه نفت خام از منطقه خارج شده و این نشان می‌دهد تهران کنترل تنگه هرمز را در دست ندارد. بسنت همچنین گفت «رسانه‌ها یکی از بهترین متحدان ایران هستند» و با تأکید بر اینکه هیچ مینی در تنگه وجود ندارد، گفت دو کشتی نیز به مین برخورد نکرده‌اند. او در پایان گفت یا سپاه علیه یکدیگر برخواهد خاست، یا مردم علیه آن‌ها خواهند شورید، یا تهران به میز مذاکره بازخواهد گشت و خواهان توافقی خواهد شد که بتواند به آن پایبند بماند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22062" target="_blank">📅 02:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ZkyA4Qgx5tD8Fr9GzdCUMSuJXJl0diX5brUqPBv_ozcUTYFEghz2FPJhn0bKq9t9KhomHPAM-QzF2TEnOnsnMBSrIm7OYRAwggMxM8upnTCLIfynhifwr2QXxO6oq3FPtUjA4c_6hNCAn_lsooEty3mPXkhI1hJv43EMeEZRIK7FcBIztkmMSDH1G-sV_JFpM3g2QrcWrP9lgSQ1u2d4b8F8oW8e6JIWZunl-4hF6-nSSDyqtWvPTUWUbasyu5qpc-mpgh00okBsSrZ77eXolTKNIvXTYNZLqom2xpJrZhB4j6m9ro8LjLrDpRFYxDqja_ybDFxeo-g8nq8MDe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بسیجی هایی تجمعات حکومتی مشهد پرچمی که آورده بود و تکونش میداد به کفنش تبدیل شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22061" target="_blank">📅 01:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش انفجار در مواضع کودر ها در اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22060" target="_blank">📅 01:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYAGP9qfdthZBYhoUJSLrKG_VksrdhjyUKLAAs2KmZDNnlifq3mAipgZzDFirubKqIly1krlPRHQcz-eSjwgv9YcBqZtvj46d5FREdxGqsMGdz71uUd0ThpwCs9I0lKBAPgpAvfS5Dffj1pfCN2v6fCPcz8JDrRNjpo-ltTcD-Wb2ioGOLQxxmvxjh5JMQB5LL9x0HpcD_SQfSGoRE-MT4xMyFeOTw4Kqli-irawi3bEHOymFoZeLFbai9FHJ_O6UZPVutwoHdmAi3tkMfjTlsvCZ9-oWdo10w_S-_BEfEPv_JlKwQjbs48q1Tk7OimE11SDd7fKTgklmpmayM13qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سه سوخت‌رسان آمریکایی، در محدوده خلیج فارس و تنگه هرمز مشغول عملیات هستند؛ یکی از آنها تازه از قطر برخاسته موضوعی که می‌تواند نشانه ادامه‌دار بودن عملیات باشد. همچنین یک فروند
E-11A BACN
(هواپیمای ارتباطی و انتقال داده در میدان نبرد که ارتباط میان هواپیماها، پهپادها و نیروهای زمینی را برقرار می‌کند) با ترانسپاندر خاموش در حال فعالیت است و موقعیت آن از طریق سیگنال‌های ماهواره‌ای برای ما قابل مشاهده شده حضور دارند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22059" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بقائی، سخنگوی وزارت خارجه رژیم، در واکنش به حمله آمریکا به یک منزل مسکونی در کوهستکِ سیریک هنگام برگزاری جشن عروسی، اعلام کرد بیش از ۵۰ زن، مرد و کودک کشته و زخمی شده‌اند. او این حمله را در ادامه حملات آمریکا به میناب، لامرد، قشم و دیگر نقاط ایران دانست و تأکید کرد ایران به این حملات «قاطعانه پاسخ خواهد داد». بقائی همچنین سکوت یا توجیه این حملات از سوی دولت‌ها و سازمان‌های بین‌المللی را به معنای بی‌طرفی ندانست و نسبت به عادی‌شدن بمباران و پیامدهای آن هشدار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22058" target="_blank">📅 01:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پدافند کویت درگیر شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22057" target="_blank">📅 01:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22056">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">موج جدید شروع شد
گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22056" target="_blank">📅 01:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ff745370.mp4?token=OP7GWkrZ9Gu-9Ja8xjmzk0kADZ9jrpjgwqhnfTMKOJg49tfkJUq7CnwMIrcnXCwvdKNHXZvAfnKw7lUMvyJN87JCFS0Ho4QeN118xr9JJjpjOMqdn4n4c5hk9PFgkZ0Suj5fEmJCfIYhhjqRc_JNkq3IlxKzxZ8p9MX5TWoybZkUDtx2_iqZ85qbQO1W69p7aUa1agRwTFrOMzb2YTCljlm4qmOaD5hO3cTUJ2h9KI9EX0cZyeZVyBza3XedyjhmlIFdjGjmB6N0fXkvoqKCLC-9ICqIo7oQBj_y7pWYUCG8mw10BImE1WJRGQQ2uelJB-SEGotG3816J9J6_F2GDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ff745370.mp4?token=OP7GWkrZ9Gu-9Ja8xjmzk0kADZ9jrpjgwqhnfTMKOJg49tfkJUq7CnwMIrcnXCwvdKNHXZvAfnKw7lUMvyJN87JCFS0Ho4QeN118xr9JJjpjOMqdn4n4c5hk9PFgkZ0Suj5fEmJCfIYhhjqRc_JNkq3IlxKzxZ8p9MX5TWoybZkUDtx2_iqZ85qbQO1W69p7aUa1agRwTFrOMzb2YTCljlm4qmOaD5hO3cTUJ2h9KI9EX0cZyeZVyBza3XedyjhmlIFdjGjmB6N0fXkvoqKCLC-9ICqIo7oQBj_y7pWYUCG8mw10BImE1WJRGQQ2uelJB-SEGotG3816J9J6_F2GDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزعیات حادثه مشهد با یک کشته
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22055" target="_blank">📅 01:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مدیرعامل توانیر: چند نقطه از شبکه برق هرمزگان هدف حملات هوایی قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22054" target="_blank">📅 01:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره گفت: حملات به سایت‌های داخل ایران هنوز ادامه دارد و ما پایان آنها را به محض تکمیل اعلام خواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22053" target="_blank">📅 01:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پدافند شرق تهران بی قراری میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22052" target="_blank">📅 01:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جزئیات حادثۀ بلوار وکیل‌آباد مشهد
رئیس پلیس راهور خراسان‌رضوی:
این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا جنسیس سدان در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
این خودرو با یک دستگاه خودروی چانگان که در مسیر موازی در حال تردد بود، برخورد کرد که در پی این تصادف، تعادل خودروی هیوندا از دست رفت و مسیر حرکت آن تغییر کرد.
پس از این برخورد، خودرو با بشکه‌ها و علائم ترافیکی برخورد کرده و سپس وارد محدودۀ حضور جمعیتی شد که در حاشیۀ خیابان حضور داشتند.
طبق بررسی‌های انجام‌شده، رانندۀ خودرو در زمان وقوع حادثه در شرایط عادی قرار نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22051" target="_blank">📅 01:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش ایران در بیانیه‌ای اعلام کرد که در موج جدید حملات تلافی‌جویانه، پایگاه‌های آمریکا در بحرین را با پهپاد هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22050" target="_blank">📅 01:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ارتش اردن : سامانه‌های پدافند هوایی با ۱۳ فروند موشک بالستیک که وارد حریم هوایی کشور شدند مقابله کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22049" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22048" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تا موشک‌های سپاه برسه، از اون سمت بعدش آمریکا بخواد جواب بده داداشتون مثل جان اسنو  (نگهبان شب) بیداره ، یه لطفی کنین حالا همه که آنلاین هستین، چنل یوتیوب من رو سابسکرایب کنین که از هفته دیگه می‌خوام شروع کنم. اگه از تلگرام هم با من آشنا شدین که حتما برید اینستاگرام هم فالو کنین، چون اونجا هم یه مطالبی می‌ذارم مخصوص اینستاگرامه
📸
instagram.com/yashar
🐦
x.com/yasharrapfa
📺
youtube.com/yasharrapfa
⛑️
paypal.com/paypalme/yasharrapfa</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/22047" target="_blank">📅 00:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارشهای تأیید نشده حاکی از اینه که تو شیراز هم یک نفر با ماشین رفته تجمعات حکومتی، یه سری فاطی کاماندو رو زیر گرفته.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22046" target="_blank">📅 00:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c3bf9130.mp4?token=jLhjVgdZQBAb5qo70jYKrxPTBZgTa1hum1iL_pjE9AvQTKX3AR_7yDItpQ2mAKditwXdaW8-uz6ubWW42iSwuT9F6qUYRf-iR8-r-SgMT0oT6-IwBOZmuUqn4CiJDXC-nDYCDN7YcBn_lbacNDmaBMAicSvFUsWxYHpRNFMICuDutKVLncibDU7WrEl8MBAo-JabWxquNcjXcPd4gfh_Qu_D2TJv0bT8mia0hawXmQvir8-vFumvlHaZOBFZKKJzN_60eLEUJWE2UFBwo-PsMhiLWq5u0VFcixyDyH8hCo90o1_B9fmsztseXdOJAigTHOHzrvAzP8sXQAawSSRkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c3bf9130.mp4?token=jLhjVgdZQBAb5qo70jYKrxPTBZgTa1hum1iL_pjE9AvQTKX3AR_7yDItpQ2mAKditwXdaW8-uz6ubWW42iSwuT9F6qUYRf-iR8-r-SgMT0oT6-IwBOZmuUqn4CiJDXC-nDYCDN7YcBn_lbacNDmaBMAicSvFUsWxYHpRNFMICuDutKVLncibDU7WrEl8MBAo-JabWxquNcjXcPd4gfh_Qu_D2TJv0bT8mia0hawXmQvir8-vFumvlHaZOBFZKKJzN_60eLEUJWE2UFBwo-PsMhiLWq5u0VFcixyDyH8hCo90o1_B9fmsztseXdOJAigTHOHzrvAzP8sXQAawSSRkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی قدس سه پا، ویدئویی را منتشر کرد که در آن، شلیک موشک‌ها به سمت پایگاه‌های آمریکایی در اردن را به تصویر کشیده است. این اقدام امشب انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22045" target="_blank">📅 00:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb2a6fd69.mp4?token=Tkh7tvT0f2xq4gjd5ds1-P_JEhAcG7ZiQshvdGTthQExnh9ParB52Ow3XsqFnpYDiAGUmpXT_rwkHv4G1ESYr9ArhXc_JVwo9zmqQq6nqikIFvjQZXVuCBbioQ99fpB_suKaDpm2b-bmk-AJVaSBEEtGeMpTJwZVvxKONeezd7TCGOgbt1Rht8h7jSQNNLZ1xE9uCllfX1Ut3ixxgrYqIyy3GO2I0ihAS0HwsWPfHP4hcGnWhK1mh5NfF8rJBBevX-kkNWDGCIoudes62mmd4llreB4CDW29FPMGTNgTifWWlLNMbqedHW4jY4it3xclc0mvr65EpdeL_wC-slrZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb2a6fd69.mp4?token=Tkh7tvT0f2xq4gjd5ds1-P_JEhAcG7ZiQshvdGTthQExnh9ParB52Ow3XsqFnpYDiAGUmpXT_rwkHv4G1ESYr9ArhXc_JVwo9zmqQq6nqikIFvjQZXVuCBbioQ99fpB_suKaDpm2b-bmk-AJVaSBEEtGeMpTJwZVvxKONeezd7TCGOgbt1Rht8h7jSQNNLZ1xE9uCllfX1Ut3ixxgrYqIyy3GO2I0ihAS0HwsWPfHP4hcGnWhK1mh5NfF8rJBBevX-kkNWDGCIoudes62mmd4llreB4CDW29FPMGTNgTifWWlLNMbqedHW4jY4it3xclc0mvr65EpdeL_wC-slrZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ابتدایی حمله کوهستک ، سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/22044" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏گروه تروریستی سپاه پاسداران مدعی شد پادگان تفنگداران آمریکایی در اردن موسوم به «کمپ تبتین» را با موشک‌های بالستیک هدف قرار داده و ادعا کرد شمار زیادی از نیروهای آمریکایی در این حمله کشته شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/22043" target="_blank">📅 00:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پرتاب موشک جدید از تبریز/ارومیه
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/22042" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پرتاب موشک شاهین شهر
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/22041" target="_blank">📅 00:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/22040" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPEsINdSF7HhQ0gCvRJcd4cjwvfA67BG-KcdVZoWW3K9VJbl6pdEWeVCkg54g1OoxKs0yhCcvPCoL5ESrZKEUY99SzGg201kHwBocHOfHka0EH8XHW6qu-C2JtWkqYj4PQczSu1ofpT2uoROzjGKMsbVToGhh6dkA1vhPnzpeITYeKIScrZKjV6VG6RG4SMnkQsloEgLX27cPjOftdhDoFwceFznLp4BR-Lf9KIEdB8QAJsWOYPsht3rgcmdBia9jWdLjTauGodLl59efFTCVJDR7TkeDd5o10SoaK7A_WPJyqXw-tK_fLpbl-Bf9LuxZ3YsHqFR3HunBcWJGUeE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG_4dDN1_YQY8zGFgw4ALJv4pcWNsDjUZOQh1tpNGxDbQ35pXrqFAEPBIVW8FNutnEzU_4J2o7-0jWsZeOXpfmbNJ99nCtyp1Nys-1P5SvjJfO3ppKsSARprZJABryUojFhvLcmQzz2ls4_UkCEOVDgzvh7jILEzLTxYDnJcpdhW6isdq0o7i1Du5pp9AIZj3J7W8SXpG2ig0qKcwLfJ4E5CizC46vCzbZH4bVjzDDwfFGYlJIHo5bkUjBX9LC21auD1BVCiLlkZzC8BvNSh7TjAPJ0v5r0iUuxRvL9A_sntaPQFdS8RFyuywZtv6QbbGVfIaHPET78a2TXJ32yH0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/22034" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22033">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22033" target="_blank">📅 00:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22032">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22032" target="_blank">📅 00:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22031">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🤯</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/22031" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22029">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a99ae4fbb.mp4?token=CZydvL4wj1cryMbw7jDXBOKUMkb4MIfch4aHdnFsyLDa9ZhG6jl7S4ixAktyjlGupWcFr47f8HZKwsdukyEJHCx6xCxYs3WXmV0UTidYEzWFL9WF1SJGDqQehIzY0W3kZUjyzr7mpxb0zEgxua9ZjLpdSfoNnSXh2AV1ivwCkU4ftD8CNG6dHPdWLHHBRf1RqymB91UKP_f9Cjy7x1aVQvBCDtxBkDIU-0a-LYNh82lbz2T8dtfSpp7CqSorOUnkrvks_MYvtt9Nq-nlfYl5aIduy7m2R_1nxqxs3p80b9m1PnqDaPJnYJ6pbzcK71A9Pwrlf2ApqV20Dk7G1Lrx9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a99ae4fbb.mp4?token=CZydvL4wj1cryMbw7jDXBOKUMkb4MIfch4aHdnFsyLDa9ZhG6jl7S4ixAktyjlGupWcFr47f8HZKwsdukyEJHCx6xCxYs3WXmV0UTidYEzWFL9WF1SJGDqQehIzY0W3kZUjyzr7mpxb0zEgxua9ZjLpdSfoNnSXh2AV1ivwCkU4ftD8CNG6dHPdWLHHBRf1RqymB91UKP_f9Cjy7x1aVQvBCDtxBkDIU-0a-LYNh82lbz2T8dtfSpp7CqSorOUnkrvks_MYvtt9Nq-nlfYl5aIduy7m2R_1nxqxs3p80b9m1PnqDaPJnYJ6pbzcK71A9Pwrlf2ApqV20Dk7G1Lrx9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/22029" target="_blank">📅 23:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22028">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگه الان بی بی بود ۱۵ رأس سپاهی هلاک کرده بود ۲۵ تا دیگشونم منتظر تایید بودیم که پودر شدن بخار شدن کتلت شدن یا زیر آوارن
😩</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/22028" target="_blank">📅 23:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22027">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/22027" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22026">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐋𝐎𝐎𝐑𝐀𝕏</strong></div>
<div class="tg-text">داداش یاشار این زارتان زورتان گفتنت واقعا برکت داره</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/22026" target="_blank">📅 23:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d64055f1c.mp4?token=OoWXdneiB6oL7m9eDtkhqD7ySjc1HYtHeH1OfbVNqx4du6A3yruKSFQgfVqlNARtGkCkqJKTJV_Aw6RTGYevusls8ujXXftO_xLywUUMpnJTx2IqXhQ8TsLkMhpwbF3F_aoX3ohRuaj3m58k26S3KjAWN47XIBFIRl2pSm2yLEYU7dH6gsUGLXHUmpR_2ANqFgfm2QTclo1bnGVJiiGTfpsfaKsvWNS0jkbaSAHx9ui4YpnB7PcUYMIReUU92uUKdJYZvpVzWo7JkKY27pDJMRfljs-JU-gqilZaO9rNjZVHIUcxjUa9n3lDFLghQAFq3ph_AqSMlGWkbIjuEVLw4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d64055f1c.mp4?token=OoWXdneiB6oL7m9eDtkhqD7ySjc1HYtHeH1OfbVNqx4du6A3yruKSFQgfVqlNARtGkCkqJKTJV_Aw6RTGYevusls8ujXXftO_xLywUUMpnJTx2IqXhQ8TsLkMhpwbF3F_aoX3ohRuaj3m58k26S3KjAWN47XIBFIRl2pSm2yLEYU7dH6gsUGLXHUmpR_2ANqFgfm2QTclo1bnGVJiiGTfpsfaKsvWNS0jkbaSAHx9ui4YpnB7PcUYMIReUU92uUKdJYZvpVzWo7JkKY27pDJMRfljs-JU-gqilZaO9rNjZVHIUcxjUa9n3lDFLghQAFq3ph_AqSMlGWkbIjuEVLw4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏حمله به دکل مخابراتی سیریک با پهپاد لوکاس آمریکای (نسخه کپی شاهد)
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/22025" target="_blank">📅 23:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کاربر اتاق جنگ : وقتی از یزد میزنه یعنی جنگ ناموسی شده
@WarRoom
😂
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22024" target="_blank">📅 23:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پدافند پارچین فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/22023" target="_blank">📅 23:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رسانه های داخلی : پدافند شرق تهران فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/22022" target="_blank">📅 23:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22021">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22021" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22020">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXzJRZ4VbOxonbezeP8IfL1VWCGJoFmUclrmNWD9kCU890veQkpZkt2UiBcvg9VvV_D1GvUzPVjOTTxwKKo1viu8FndDfGauxl3Ntm9PuTxv4srKlc22fNwlJuccH2mNC2q-MEISXrRC8tiaxYBFkPqRdP9k0zPyn39wmxYvK7KTGxqcBIRBRH-AcBEJ3sY21qMnAFXOJJ9ADZe0RP3i2yToTviIEPy19Y6zgou_nPE3-Yu_zZ-m4_ceK_2My3T_3WjlufSngQDNRM3gjTkFwtP8ygRzsK26snyp5-sC1CnYmra8E0vvL1tECOFQ5HS_GgnrvR5UroRTCyh1jZ4MxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل کوهستک ، سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/22020" target="_blank">📅 23:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22019">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پدافند اردن درگیر شد</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22019" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22018">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">از همه شهر ها گزارش پرتاب موشک دارم سه پا زد سیم آخر</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/22018" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22017">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حدود ۲۰ موشک پرتاب شده</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/22017" target="_blank">📅 23:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22016">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از همه شهر ها گزارش پرتاب موشک دارم سه پا زد سیم آخر</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/22016" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22015">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هیچ خبری نیست. همین خبرها رو زدم. همچنان همین خبرها رو تکراری می‌زنند. یه اسکرول کنید بالا رو ببینید لطفاً.
😁</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/22015" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/22014" target="_blank">📅 23:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/22013" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بانک اهداف امریکا بسیار زیاد بوده امشب ! همچنان حملات ادامه داره…
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/22011" target="_blank">📅 22:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">العربیه: حملات آمریکا تسلیحات و ادوات نظامی ایرانی در حال انتقال به تنگه هرمز را هدف قرار داد
آمریکا ارزیابی‌هایی در اختیار دارد که نشان می‌دهد ایران برای گسترش حملات علیه کشتیرانی طرح‌ریزی می‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/22010" target="_blank">📅 22:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fjcjpv91EAmSFYU5WCsVfavfH5zMa8sHe9Iz7dXZlQPckhHqyCfA1Ujg0M27XIt01c4nuz_vXerEirEy1nm49UkSbgwiVrUa5DIaIiDfGgC3s4y8RZ0mPMPBTov5SIzmXcr3FkjLBFIOpNw43cZ42tIaX9BCgvfp_jZSepbAz29GlJra3XP28wxrgI0i7hfnUcEN9PNFljwPPwXG5GfVo-9GtdFRD2TJsbxVPUuRUEpq9cZQiEzUDORz0SaFrDUaI5PNSWrOeuBY1KWr5c3cPzebrMjAs4QEUa8kURYWa-3QOa_AMrsueg8F2Omq7Rp6b3OGFSi6pzlNBummMzGmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای پزشکیان
گاز کش درحال بازگشت به کشور
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22009" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجار جدید چابهار  @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22008" target="_blank">📅 22:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیدبان اتاق جنگ : سنگین ترین انفجار قشم تا کنون صورت گرفت الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22007" target="_blank">📅 22:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرماندار سیریک : امریکا امشب یه خونه زده عروسی بوده
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22006" target="_blank">📅 22:36 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
