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
<img src="https://cdn4.telesco.pe/file/MwFTyyjH0Nl7IleWE3JkE1Nw6GCSCwsrt3WLeGIpKV4MtrxrxRhrMU-xrnNI2L-DzgUOvfJgoh1FXJVncpIU4FTqBXhZN-OAJs2tczfMEKnx9Y_zGhxfvSzkR3Zwf5v7fliZ1_fUHvhgiZCitYWfLL8FmDcJ7kwmkgGw7Ey22XdbAXHtYBlo1YrpuPvnFEH2ppOH57s38TuM0ZbUmApfhzuGHhCLXiy_B7qPNE9wqzB7jcHuoYg8vNtQyMhcztB8UPbDq08VgkWb68X5sE82Pe3iewz4mL57DH8bBVE7cDDKqgyN_oodlVpp9JSsZBoXZsH_io1I0gBmNYsKxSyyvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 01:59:55</div>
<hr>

<div class="tg-post" id="msg-687558">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGoldiran | گلدیران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80aba6e820.mp4?token=Wd7qEnBLRzt9RsJ0PlKvVMgxLiCqBajCFou4AlR0Wsk_mpsW5F9s6LtsBhonyem_y_dXnlf0Yp8UM3b3NFesQjCv9Qp-1AErT2_WenxN00SJYqJgvpEGI7FKq3JyUR7RxBKA28PyvlbQfPc1VVjiF6LsljIcD3zP8CvIkNzqk48RkqYfCLwtTfHIHYON65N2m5hZLLMr9W1NCIZAFl1RXj6X4mhPjx0NHHGPInz-odOrB5flsXt6TZ44TMk7jtuZ1_5m3Fq4aWF8ZRuXoIsFIZUfAsRg1Y0ixHGu_CRMUy5kiUZDSpCN0WNqT_bS4hJTWTh3rq8RDNBp8fE1cB-FrJHbgsSXAYtHly72GfIP23_vc8dxOIlz6pY41RFT7MhsmGIgMDGz9LvnRHhaQ-KmgeB__qnYLnpaA5IH99L8H1kV-0S41z1y3TzRv0JS3M-8YnLDtD6Vx7e7gl_c4YVHULQYnr5PQzZxaQOQPpRwG1eXZ2OGDDCjx47DoEYqTuuHsqK7CPpvRH2jS3_3HjAC6kD_ujoNv5_cYgRkNtTobpH8qfakHPwNJDlaOqlXiwh4Owhi54w8sqEb-wR4L1eYYyD0ipPUvv9d-Ar_C4LCR3TqCkgagrYEq5WGN3IUstv5pVNYevArJ0sm9ljXQeWJZIPEHAEFhMSBs-_a4lD6FwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80aba6e820.mp4?token=Wd7qEnBLRzt9RsJ0PlKvVMgxLiCqBajCFou4AlR0Wsk_mpsW5F9s6LtsBhonyem_y_dXnlf0Yp8UM3b3NFesQjCv9Qp-1AErT2_WenxN00SJYqJgvpEGI7FKq3JyUR7RxBKA28PyvlbQfPc1VVjiF6LsljIcD3zP8CvIkNzqk48RkqYfCLwtTfHIHYON65N2m5hZLLMr9W1NCIZAFl1RXj6X4mhPjx0NHHGPInz-odOrB5flsXt6TZ44TMk7jtuZ1_5m3Fq4aWF8ZRuXoIsFIZUfAsRg1Y0ixHGu_CRMUy5kiUZDSpCN0WNqT_bS4hJTWTh3rq8RDNBp8fE1cB-FrJHbgsSXAYtHly72GfIP23_vc8dxOIlz6pY41RFT7MhsmGIgMDGz9LvnRHhaQ-KmgeB__qnYLnpaA5IH99L8H1kV-0S41z1y3TzRv0JS3M-8YnLDtD6Vx7e7gl_c4YVHULQYnr5PQzZxaQOQPpRwG1eXZ2OGDDCjx47DoEYqTuuHsqK7CPpvRH2jS3_3HjAC6kD_ujoNv5_cYgRkNtTobpH8qfakHPwNJDlaOqlXiwh4Owhi54w8sqEb-wR4L1eYYyD0ipPUvv9d-Ar_C4LCR3TqCkgagrYEq5WGN3IUstv5pVNYevArJ0sm9ljXQeWJZIPEHAEFhMSBs-_a4lD6FwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☀️
این تابستان، خرید راسل با هدیه نقدی همراه است.
در جشنواره تابستانی جی‌پلاس، با خرید و نصب ساید بای ساید چهار درب Russell، هدیه‌ای ویژه در انتظار شماست.
تمام خریداران این محصول پس از نصب، حداقل ۱۰ میلیون تومان هدیه نقدی دریافت می‌کنند و بر اساس قرعه‌کشی، این مبلغ می‌تواند تا ۲۰ میلیون تومان افزایش پیدا کند.
برای مشاهده جزئیات محصول و خرید، به فروشگاه اینترنتی گلدیران پلاس مراجعه فرمایید:
goldiranplus.ir
مشاهده آدرس فروشگاه‌ها
@goldirangroup
گلدیران | روی خوش زندگی</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/akhbarefori/687558" target="_blank">📅 01:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5072b66a5.mp4?token=lctbIftGvMFZ2jGrtyp3_HfzNsE0zhLogkirzFQ3eZ3R6Ho3BYKzBdxjvyx-ZjDpfF4gvmAZo8jbCwsiAriqWD0em_UI2s9OlakY0D91KnSYp828_z7jCA5Lo3AKDFDjB0GtT7lZi5HwoVd9ndzh18BgkCMw6OLNkh6cb0dzYIbSR-P-kM4N7GG0yDde8iWvjuHb1vHWdpLrfY218slq93S7ZABN_T0abhsuh0zfITxP766dOfS0gzWZqtStqZlORhx7ga2MAH0grGOU8JruN_p59_go9ZsFb1niz6dtuC8CchI0Utyzxd3WZ2fHIAHjdNTlXh7ZCNcASACMFVORtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5072b66a5.mp4?token=lctbIftGvMFZ2jGrtyp3_HfzNsE0zhLogkirzFQ3eZ3R6Ho3BYKzBdxjvyx-ZjDpfF4gvmAZo8jbCwsiAriqWD0em_UI2s9OlakY0D91KnSYp828_z7jCA5Lo3AKDFDjB0GtT7lZi5HwoVd9ndzh18BgkCMw6OLNkh6cb0dzYIbSR-P-kM4N7GG0yDde8iWvjuHb1vHWdpLrfY218slq93S7ZABN_T0abhsuh0zfITxP766dOfS0gzWZqtStqZlORhx7ga2MAH0grGOU8JruN_p59_go9ZsFb1niz6dtuC8CchI0Utyzxd3WZ2fHIAHjdNTlXh7ZCNcASACMFVORtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از ۴۰ سالگی، چه ویتامین‌‌هایی برای بدنت ضروریه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/687557" target="_blank">📅 00:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687556">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
عناصر وابسته به امارات در یمن از میان برداشته شدند
🔹
منابع یمنی از کشته شدن حداقل ۳۳ نفر از شبه‌نظامیان «العمالقه» (همسو با امارات) در حملات نیروهای ارتش و انصارلله یمن خبر دادند.
🔹
این شبه‌نظامیان برای کمک به نیروهای وابسته به دولت عدن (وابسته به ریاض) به استان عدن اعزام شده بودند.
🔹
محمد سیف المحولی، فرمانده یک گروه واکنش سریع در گروه نظامی «العمالقه»، جزو کشته‌شدگان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/687556" target="_blank">📅 00:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687555">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9FQp0q1FyzU1zSVtgngiBOgKgdqofhj_9NayuZ5EVO5zKDtv9f9hLZivCck9DCZFMsnz6d9_JaHVP-uab_hq6g6W5CBdlHWd28Bvpa8qsmuTUo1VkTMUTjnMF78yhmesdWKNfL4u2noSjBYcKZonMXwzgJuhmivgpAo5EJADNQ8UNRI5kuPUV8ERmYVslIzYryHdjMUNYcm6qo037Z7IPUmxvB9zGEj6RZOHQGRfoqdx4i-TDi8PG9Vd4zhP21bjIP2tfyJl4v3z2zmatye0WHKFefQDoKLrpSzWvqOJS5iwYG-HkcaUoX-mjaZKhf8Wnyo0oR07QFwbPPAmImJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رقیب نتانیاهو برای ایران چه برنامه‌ای دارد؟ | از «منطقه کشتار» هسته‌ای تا بازگشت عملیات موساد | توهمات ناتمام صهیونیست‌ها
🔹
با نزدیک شدن به انتخابات پارلمانی اسرائیل، رقابت برای نخست‌وزیری وارد مرحله حساس‌تری شده است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3242959</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/687555" target="_blank">📅 00:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687554">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5558d5321a.mp4?token=AyfzVdxWw_oAMM3Y4PvN1d-0TVGezkSfG_JZdFn3IiNnutFIZ7HPnfTtbQ3cYiWJB4-bYl8QBQXKrhCsblkNmWjJ3sRb4XNN-Xusxx7I7qMJ7MFxrRrUqANMGBQi2H1Vwk4JbygnvUWS62SE9yrauzP_6gRyWZBd9KLw__4kFveFEFo4JOSeZnaRBGbdJAI9nCUIo1wkWbmQ3cQhG8QnO6AgQI87ZbrvTz8EAjSx-6qJX-oMrV0Kb44qbZTegGxlF0YFK4BbeRt1WhgtdEro3x1O9olrpvqwea9fe_3x_O4KfSkeiy_qrkAwSKHLcAqvEu_2uJVqFhzGoyNEelzHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5558d5321a.mp4?token=AyfzVdxWw_oAMM3Y4PvN1d-0TVGezkSfG_JZdFn3IiNnutFIZ7HPnfTtbQ3cYiWJB4-bYl8QBQXKrhCsblkNmWjJ3sRb4XNN-Xusxx7I7qMJ7MFxrRrUqANMGBQi2H1Vwk4JbygnvUWS62SE9yrauzP_6gRyWZBd9KLw__4kFveFEFo4JOSeZnaRBGbdJAI9nCUIo1wkWbmQ3cQhG8QnO6AgQI87ZbrvTz8EAjSx-6qJX-oMrV0Kb44qbZTegGxlF0YFK4BbeRt1WhgtdEro3x1O9olrpvqwea9fe_3x_O4KfSkeiy_qrkAwSKHLcAqvEu_2uJVqFhzGoyNEelzHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبتهای تامل‌برانگیز آزیتا لاچینی درباره زندگی...
🔹
اگر درست زندگی نکنیم، چی میشه؟ به کی ضرر می‌زنیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/687554" target="_blank">📅 00:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687553">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
انتشار برای اولین بار، تصاویر منتشر نشده از رصد و اقدام علیه شناورهای متخلف
🔹
اقدام و مدیریت قاطع نیروی دریایی سپاه در تنگه هرمز؛ هر گونه اقدام مشکوک مورد هدف قرار می‌گیرد.
🔹
ایالات متحده بزرگترین تهدید برای امنیت کشورهای منطقه و تجارت دریایی است؛ پشتیبانی و اسکورت ایالات متحده دروغی بزرگ است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/687553" target="_blank">📅 00:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687552">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
اولیانوف: در جلسه شورای حکام، درباره ایران بحث خواهد شد
نماینده روسیه نزد سازمان‌های بین‌المللی در وین:
🔹
روز دوشنبه، جلسه شورای حکام آژانسک بین‌المللی انرژی اتمی مربوط به ماه سپتامبر آغاز خواهد شد.
🔹
می‌توانیم انتظار داشته باشیم که بحث‌های فعالی در مورد ایران، سوریه و اوکراین برگزار شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/687552" target="_blank">📅 00:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
پایان دیدار نمایندگان ترامپ با پوتین
🔹
استیو ویتکاف و جرد کوشنر پس از ۳ ساعت مذاکره با رئیس‌جمهور روسیه ولادیمیر پوتین، کاخ کرملین را ترک کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/687551" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
خبرهای جذاب امروز را به انتخاب مخاطبان خبرفوری بخوانید و ببینید و نظر بدهید
🔹
🔹
فاز جدید جنگ ایران و آمریکا | حمله به نفتکش ایرانی در جزيره خارک
👇
khabarfoori.com/fa/tiny/news-3242835
🔹
پشت‌پرده شایعه حمله اتمی آمریکا به تهران چیست؟
👇
khabarfoori.com/fa/tiny/news-3242751
🔹
ماجرای اعزام ناو از کره به خلیج فارس | ایران با کره جنوبی وارد جنگ می شود؟
👇
khabarfoori.com/fa/tiny/news-3242872
🔹
جزئیات فعالیت شبکه فحشا در شهرداری | نقش یک مسئول شهرداری در سازماندهی شبکه فاش شد
👇
khabarfoori.com/fa/tiny/news-3242669
🔹
خبر تکان‌دهنده درباره سرنوشت غم‌انگیز خواننده زن قبل از انقلاب
👇
khabarfoori.com/fa/tiny/news-3242916
🔹
خبرهای لحظه‌ای جنگ را اینجا دنبال کنید
🔹
khabarfoori.com/fa/tiny/news-3242976</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/687550" target="_blank">📅 00:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بازداشت عوامل رژۀ موتوری منتسب به سازمان منافقین در حوالی کرج
🔹
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن ظاهرا تعدادی از هواداران سازمان منافقین در خیابان‌هایی که گفته شده در حوالی شهر کرج قرار دارد، اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند.
🔹
تمامی افرادی که در این کلیپ حضور داشته‌اند، توسط نیروهای امنیتی شناسایی و دستگیر شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/687549" target="_blank">📅 00:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR8pqSm5EUAeWNh8qI7doAyK2GMdUBnid8EW3tGsQtliCzkxHynATxabJqgCFgnL39ZDu1MDmCXtppE3a-Nz9c97TzGfVoLb4SIlIUWVV3s6pfTuhp893EyxC9OqiKX4kSwaa1NWZ00FDVZNc-39rtrtBJQAddMVOeq3RkJbQh0MFS8_3sJhn0IoJfojl5cSQ5OGgMMFndVwj0ZImUt9f4d8YUEC7fSDcPaE2ogN-egt4B5V_4btTuOOCRsv7WJdEdSt3xzqq8kj2vixBVQCc3Wii4C9hrXH43t_TQ9URSEkH23-f5GU1rrYZcOprQXxAJnjOheuvYZ1RL7bE9mFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦋
خاص بپوشید، متفاوت دیده شوید
🦋
حوریا عبایا | HORIA ABAYA
مجموعه‌ای از عباهای لوکس، مجلسی و روزمره با طراحی اختصاصی
✨
با پارچه‌های خاص و وارداتی، همراه با گلدوزی و نگین‌کاری‌های ظریف و منحصربه‌فرد
از مدل‌های مینیمال و روزمره تا عباهای فاخر و خاص،
برای استایلی زنانه، شیک و متفاوت
🤍
📍
خرید حضوری از شوروم حوریا عبایا در فرمانیه تهران
📦
ارسال با تیپاکس به سراسر ایران
مشاهده مدل‌ها، قیمت و ثبت سفارش
👇🏻
📸
اینستاگرام:
https://www.instagram.com/horia_abaya
کانال بله:
https://ble.ir/horia_abaya
📲
سفارش و مشاوره:
09103156129</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/687548" target="_blank">📅 00:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMUDRaOXfuKBUFERsX-SfQX_F6raVIW7CBDSgSMJ2PRBS1Q3o3-m8sIwSyw6tyTtEio7TlkVG5z3RFBo15Wk1THzsYFr9fuqX4uhxIlzinKaNHNh-vBCIAPFhLRiFnxvPFjHrltVrxdeiy-Dw02Y4JG-qwsMBOsHpoZr5IYmKHw5IreE02fs8kUumrxWAfspHGToAKjJvMyltDUdUtYPyn6T5lYhgBe5GG0YDW62nRxVh9GGW6CeFcWM2HGi4qHrz5I2xz6q7sReS_s2XswzzKMNSYzjAKDusHEmFL8_izaMBi6nn7rCd_fAm2-eZuEnYWuy3UdBVfn98fFLOvMThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/687547" target="_blank">📅 00:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صولت مرتضوی: حسن روحانی همه مسائل کشور را به برجام پیوند زده بود و حتی تلف شدن گاومیش‌ها در خوزستان از کم آبی را به برجام پیوند می‌زد/ رشد اقتصادی در دولت حسن روحانی کمتر از ۱ درصد بود و شهید رییسی رشد اقتصادی را به ۷ درصد رساند
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری :
🔹
ترامپ برجام را پاره کرد و بسیاری از مفاد برجام را هم دولت اوباما اجرا نکرد و زیر میز زدند. دولت رییسی گفت اقتصاد بدون برجام هم قابل اجرا است؛ رشد اقتصادی را به ۷درصد، نرخ بیکاری را از ۱۰۰ درصد به ۷/۶ درصد، میزان نقدینگی را از ۵۰ درصد به ۲۹درصد، تورم را از ۵۰ درصد به ۳۲ درصد، صادرات نفتی را از ۳۰۰ تا ۴۰۰ هزار بشکه نفت در روز به یک میلیون و ۷۰۰ هزار بشکه رساند؛ اینها بدون برجام بود یا با برجام؟
🔹
در جلسه‌ای آقای روحانی اعلام کرده بود اگر کسی در مملکت ۳۰۰ تا ۴۰۰ هزار بشکه نفت در روز صادر کند، بگویید او را وزیر نفت بگذارم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/687546" target="_blank">📅 23:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4d13812.mp4?token=g9S3Ahrrj07nqZKmwpWXscnNH6SdEhuWxRyD7pdKnZPhpvWa8cAuXMT7UDMOsvxkDIx8KVjbFwTPtlgoYAwEmWiUGXCVCTEx2_bXytyhGr3nmlWpDGLIHgpPILLHY1pQ7TDwv-KE4o4e5Pwwk_8BbkWLVpw-bBeDajHwWSW-AvXca1j-MPLU4Gh9w-u1e1LYlC-e9q2Uq324q0Ifoj7Xx4QstejjHFkLfBxi5lCI_mSKe75ExAUxnMF_lo6utTt-rHLue-h5-mvmedFwJFp4n55AC2kcwJhx4UGJfnAwXUUT3YVlwnOYgriYwX9xxON9w0mRTasHbXHa-PCSyU4wCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4d13812.mp4?token=g9S3Ahrrj07nqZKmwpWXscnNH6SdEhuWxRyD7pdKnZPhpvWa8cAuXMT7UDMOsvxkDIx8KVjbFwTPtlgoYAwEmWiUGXCVCTEx2_bXytyhGr3nmlWpDGLIHgpPILLHY1pQ7TDwv-KE4o4e5Pwwk_8BbkWLVpw-bBeDajHwWSW-AvXca1j-MPLU4Gh9w-u1e1LYlC-e9q2Uq324q0Ifoj7Xx4QstejjHFkLfBxi5lCI_mSKe75ExAUxnMF_lo6utTt-rHLue-h5-mvmedFwJFp4n55AC2kcwJhx4UGJfnAwXUUT3YVlwnOYgriYwX9xxON9w0mRTasHbXHa-PCSyU4wCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پزشکیان آسانسور را ممنوع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/687545" target="_blank">📅 23:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a553f8c48.mp4?token=RIXYmApoOC1q_AeKwHvj_CjVVN5kzZTYRptepqzJL5TK2jeilDoUHgxS7kGM-yeNJYge1xNSbYznlo1T6aCmgBMw4L6qcPndm2s2OK6rekyDzJx5ejmi4aJ_9eakpaMyqy6zYRSxuIxuHw_nOsT4BQj8N_RQOzuMdeAiFBX4vwFABSLH52WkEXDikL31XGHWukI4wOgjE9VSEpiV_uwpjhbHyBLISXOus9ln2zEdpsQyJoP3BM6RPFG7Fmh0hWA-8u79l7ZKcsxTiOuAyFIEbddJrSRfLFvxPTbVeNgYlvYURKlogA7cr8GnUFqUWUqql47UBam4NN1c43zUDUmh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a553f8c48.mp4?token=RIXYmApoOC1q_AeKwHvj_CjVVN5kzZTYRptepqzJL5TK2jeilDoUHgxS7kGM-yeNJYge1xNSbYznlo1T6aCmgBMw4L6qcPndm2s2OK6rekyDzJx5ejmi4aJ_9eakpaMyqy6zYRSxuIxuHw_nOsT4BQj8N_RQOzuMdeAiFBX4vwFABSLH52WkEXDikL31XGHWukI4wOgjE9VSEpiV_uwpjhbHyBLISXOus9ln2zEdpsQyJoP3BM6RPFG7Fmh0hWA-8u79l7ZKcsxTiOuAyFIEbddJrSRfLFvxPTbVeNgYlvYURKlogA7cr8GnUFqUWUqql47UBam4NN1c43zUDUmh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصمیم جنجالی داور؛ از کرنر گلگهر تا گل تراکتور
🔹️
داور ابتدا به سود گل‌گهر کرنر گرفت اما لحظاتی بعد تصمیمش را تغییر داد و ضربه دروازه اعلام کرد؛ تراکتور هم بلافاصله بازی را شروع کرد و در ادامه مهاجم این تیم در موقعیت تک‌به‌تک گلزنی کرد.
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/687544" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687543">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy56NaymjI-jmzjSnmS8FElzDTPyC4IbAVRLL0iQYaznkdCW72nXzhnHdDy6YeQpOIEhpmhSxr-FeGUdNjL9LmaAwIH-75Hl6Zvx8nL_dQCKI0sIgxcrGJSVcU8cXaccE5PZC83u9VVfQ-pLwze96DGO5wgh5sbVloh1T4AXHODGYRe_CEpBzsm_mB7bOSASd_lrhQ4hQwxANGegtLsxAaDaCFrhKUuR5suRFu7sGO3VGHYXVMI6_JnLA61P02AHwsCKb2zeQfWlg1Ooc8VNwmdrGDL_jrVzCs7h6QR7xowLt7ss_yOe8t-klehG0ZNMDmvX0ITUSN2dr8lqHLjyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«فخوز» به تابلو بازگشت؛ اعتماد سهامداران به آينده فولاد خوزستان
🔹
فروردین‌ماه ۱۴۰۵، تنها یک ماه پس از آغاز جنگ، شرکت فولاد خوزستان هدف حمله دشمن قرار گرفت و در جریان این حادثه، بخش‌هایی از این مجموعه با آسیب جدی مواجه شد. با این حال، اتکا به توان فنی و دانش بومی و تلاش مستمر کارکنان و متخصصان شرکت موجب شد فولاد خوزستان در مدت‌زمان کوتاهی وارد مرحله بازسازی و ریکاوری شود.
🔹
حالا پس از گذشت حدود پنج ماه از آن حادثه، نماد «فخوز» بار دیگر به تابلو معاملات بازگشته و واکنش بازار به بازگشایی سهم، قابل توجه بوده است.
👇
👇
akharinkhabar.ir/local/10996072/
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687543" target="_blank">📅 23:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687542">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
هشدار هواشناسی برای شمال کشور؛ بارندگی شدید در راه است
یک کارشناس سازمان هواشناسی:
🔹
بارندگی شدید از روزهای دوشنبه و سه‌شنبه در سواحل شمالی آغاز می‌شود و با تشدید رگبارها، هشدار نارنجی برای مناطق صادر خواهد شد، مسافران و کوهنوردان احتیاط کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/687542" target="_blank">📅 23:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687541">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
غرامت دهید تا از تنگه هرمز عبور کنید
عباس گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس در
#گفتگو
با خبرفوری:
🔹
طرح امنیت پایدار تنگه هرمز در مرحله پایانی بررسی در کمیسیون است. این طرح می‌تواند تنگه هرمز را به یک منبع درآمدی بسیار ارزنده برای کشور تبدیل کند. نوع رفتار با شناورهای کشورهای مختلف طبیعتا متفاوت خواهد بود، هر یک از دولت‌ها وضعیت متفاوتی دارند و علیه کشورهای متخاصم نیز اقداماتی انجام خواهد شد.
🔹
یکی از بندهایی که جدیدا در کمیسیون امنیت ملی مطرح شده، پرداخت غرامت از سوی کشورها، سازمان‌ها و افراد حقیقی و حقوقی است که در جنگ تحمیلی گذشته خسارت‌هایی را به جمهوری اسلامی ایران وارد کردند. در غیر این صورت، شناورهای متعلق به این کشورها نیز با ممنوعیت عبور از تنگه مواجه خواهند شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/687541" target="_blank">📅 23:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687540">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
معاون سیاسی نیروی دریایی سپاه: روزانه ۲ تا ۵ شناور در تنگۀ هرمز هدف قرار گرفته شده‌اند
علی محمدی:
🔹
در ۱۰ روز منتهی به ۸ شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.
🔹
حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل ارادۀ نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/687540" target="_blank">📅 23:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
چهارمین حمله رژیم صهیونیستی به سوریه طی ساعات اخیر
🔹
نظامیان رژیم صهیونیستی مستقر در پادگان الجزیره، منازل مردم روستای معریه در حومه یرموک سوریه را گلوله باران کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/687539" target="_blank">📅 23:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
واکنش سفارت ایران در آنکارا به بیانیه سفیر آمریکا در ترکیه
🔹
سفارت ایران در آنکارا، اظهارات اخیر سفیر آمریکا را تلاشی برای پنهان‌سازی سیاست یکجانبه‌گرایانه واشنگتن در قبال ایران خواند و تأکید کرد: تغییر واژگان، ماهیت عملیات طرد اقتصادی را تغییر نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/687538" target="_blank">📅 23:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687537">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd94871eaa.mp4?token=Efsc5WyZjjTIhThGZKnSsthkeXvpgI4Aq8xRQpXtQQgY_fVg_uTI6iTaQa9_mFiOBvVN9PUmd54qNA0z6tlibKi9zFhLn8ziXoI2i_8ZiVPPWsS936VdYNHlk9ch-soYxiKMwQJ8ZOgkZoviFSb4ZFzxV1P9aigCac9wvjrtecTNGL6-mxQPFogctrw7XUGOYimu3utzqbFGsMjyX-y_czSDSovl0pAhYYoGWXE4JFVsCVLNCVkhlXrPoS8_H7m2IUHy_MjuycMVit1-HOXhRavPNQlZgQKr_KUDpAcNOb26m97mjMxjWunId-iBo46qO2DEna6S1xCppjxXIXAtwb6wDIrSfolDJwOuuTdfqVXgGZsVxsa0mYaJ9lLC2eWRzteFRYFIxFDkjcjzsNI-RmKoKx7xpZW1n5hO07xKWZ7uw3vY7QXP-SW5naRLa-eCcqCSglhx10swlzT0O0bqWn5R1AcbhkOosNiFWtvNKKy31G07MyA8vkqhDxooT6IR5STZUpfb4EiaFPUFXDeNj-0cujWNeS98y2gFrxgMzNvs4bBSeW5wna-P-E2YtiwvwTqNfTXnKIWbhZJj4Y90KFFcnenHoLW1-EbX-kMilh3dzziRa1KrHoHIK2yjwaU0rY9af7NLqETLB11bJY2vMdP9GHioHs9RUrWG8AoWxHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd94871eaa.mp4?token=Efsc5WyZjjTIhThGZKnSsthkeXvpgI4Aq8xRQpXtQQgY_fVg_uTI6iTaQa9_mFiOBvVN9PUmd54qNA0z6tlibKi9zFhLn8ziXoI2i_8ZiVPPWsS936VdYNHlk9ch-soYxiKMwQJ8ZOgkZoviFSb4ZFzxV1P9aigCac9wvjrtecTNGL6-mxQPFogctrw7XUGOYimu3utzqbFGsMjyX-y_czSDSovl0pAhYYoGWXE4JFVsCVLNCVkhlXrPoS8_H7m2IUHy_MjuycMVit1-HOXhRavPNQlZgQKr_KUDpAcNOb26m97mjMxjWunId-iBo46qO2DEna6S1xCppjxXIXAtwb6wDIrSfolDJwOuuTdfqVXgGZsVxsa0mYaJ9lLC2eWRzteFRYFIxFDkjcjzsNI-RmKoKx7xpZW1n5hO07xKWZ7uw3vY7QXP-SW5naRLa-eCcqCSglhx10swlzT0O0bqWn5R1AcbhkOosNiFWtvNKKy31G07MyA8vkqhDxooT6IR5STZUpfb4EiaFPUFXDeNj-0cujWNeS98y2gFrxgMzNvs4bBSeW5wna-P-E2YtiwvwTqNfTXnKIWbhZJj4Y90KFFcnenHoLW1-EbX-kMilh3dzziRa1KrHoHIK2yjwaU0rY9af7NLqETLB11bJY2vMdP9GHioHs9RUrWG8AoWxHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کار دولت شهید رییسی: رشد اقتصادی کشور در دولت شهید رییسی به ۷ درصد رسیده بود و اگر دولت ایشان ادامه پیدا می‌کرد رکورد رشد اقتصادی ۸ درصد را می‌شکستیم/ کاهش ۸ میلیونی جمعیت فقرا از اقدامات دولت شهید رئیسی بود
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری:
🔹
میانگین رشد هشت ساله آقای روحانی پایین تر از ۱ درصد بود. برنامه مصوب مجلس ۸ درصد بود و ما در بازه ۲ سال و ۹ ماه دولت شهید رییسی با کمی فراز و نشیب به رشد ۷ درصد رسیدیم و اگر دولت تداوم می‌یافت برنامه داشتیم رکورد رشد ۸ درصدی را بزنیم.
🔹
زمانی که شهید رییسی دولت را تحویل گرفت تعداد جمعیت فقیر ۲۷ میلیون بود اما این جمعیت در زمانی که دولت شهید رییسی تحویل داده شد به ۱۹ میلیون نفر رسید
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/687537" target="_blank">📅 23:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os7Sf195R3-dyNltpumYmhdAlcrsP_DLUYM8cmwV6bbsSahjQGDvm1qEyDS_hkx2pCB1ME38SFHtmhMgReCMlSTttvpk5wVABwETtx-czDJtxNSHGqTdExZLyLvf_KmrQzm0oQcT0IDTwWCvC1J8zJcBItm7NQ5Q1g2Y7WVJgbN3-LptXdJCtVtm0iWzjfZ08XvyH7ki8kw61gIyhM-kYjNPr4QxAa34Wx-gBCLoPwdLpkv5OZsX_rRQAOAygbVlf45W7NPhV19bpmf1kyHvjAnkb9zrw0luf8nWozMZIuZX5IwwsH-CJMRg3S7teJkncYfJtA2QrTFiKM8n0RGc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه جهان قرار است واقعی‌تر دیده شود!
🔹
مجمع عمومی سازمان ملل با تصویب قطعنامه‌ای از تغییر نقشه جهان از مرکاتور به نقشه‌هایی دقیق‌تر برای نشان دادن اندازه کشورها حمایت کرد.
🔹
این قطعنامه با رأی ۱۶۴ کشور تصویب شد و آمریکا تنها مخالف آن بود.
🔹
نقشه مرکاتور شکل و جهت کشورها را حفظ می‌کند، اما مساحت مناطق نزدیک قطب‌ها را بزرگ‌تر از واقعیت نشان می‌دهد.
🔹
در واقعیت مساحت برخی کشورها از جمله  آمریکا کوچک‌تر از آن چیزی است که روی نقشه مرکاتور دیده می‌شود و کشورهای نزدیک خط استوا، مانند آفریقا و برزیل، بزرگ‌تر از تصور رایج‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/687536" target="_blank">📅 23:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xakr5X6DLPftok1a0-OycB26oLQRo46rh07acXmemnFRWfcQ6EFG7cbZSqEdRZDwMcwclbDLWWMXT5ET_M7aNmOwfPfqYw9pMZiDsBM8f6cdo6UYaW-1RY4YtEBtM9t_MQF37NBUM8fd2rNwYbzXNrmzxtMS9TKnMDguuTEdGxDfOtVOXkn_OPwHra4BZsz6wikZGOktBoVc5w0w1buyKCNJDKc7S1iVEM8Q5E0czvGierwx7nn6G5zCY8XYFqps60bfNLyhGU1roVpGIJZ_0i7CAKXS5oi6mKrmlaUHNkOO-vLFEf9T06sR1c__6YpqL9bCFHGg8BNOs2H55ieYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار قاطع فرمانده نیروی دریایی سپاه: فریب آمریکا را نخورید؛ هر تحرک مشکوک هدف قرار می‌گیرد/ پاسخ به تجاوز ارتش تروریستی امریکا در حمله به سه فروند نفتکش متعلق به جمهوری اسلامی ایران
نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
بسم‌الله الرحمن الرحیم
والحمدلله قاصم الجبارین و مبیر الظالمین
🔹
ملت قهرمان و بپا خواسته ایران عزیز؛صبح امروز ارتش تروریست و متجاوز امریکایی طی یک اقدام وحشیانه و از سر استیصال در بستن بودن تنگه هرمز به سه فروند نفتکش متعلق به جمهوری اسلامی ایران حمله کرد که خساراتی را به بار آورد.
🔹
رزمندگان نیروی دریایی سپاه با استمداد از قدرت لایزال الهی و با حمایت و پشتوانه شما مردم دلیر و به مصداق آیه نورانی قرآن کریم که می فرماید :« فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم» سه فروند نفتکش در مسیر غیر مجاز تنگه هرمز و سه فروند شناور وابسته به امریکای کودک کش را در مناطق دیگر مورد هدف قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/687535" target="_blank">📅 23:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLsxYGaDnqQzzVJd-WDL52lcSyTzJzr4Ef3C5I25t1tiwQU0Bf495WngHK2S_6sW4kmLAKcW83Anz5SMdG32OnjpnqK9eJK5zig-SGIjsQRCfbovgx3LGdCGTjlA0SXaTs2HCn7CyLoVhmbWo73pipruXB-zVMI5Y_Wr7qHu7rO9CS8oqwBmysbGcrUGXCV5aPHYXCS1I2-bdFVPKJ_Y6DiLVyELYXSsh4wWMMrhghAJ-gutSszvEvifvwKj3caYP1Qi0kz-b-lMuyirS2uiIBUMDkkOaGXHt7O34w1ldg7Q9AQYNaYt8_EY5lS0Ll6bVfROAXukbSY_j0ip3JsNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484016062d.mp4?token=XwK6m1hNvUuNz1N1qvsvmDpKxC3-OkGlD7NwXqm4TCm9U3Jt93DTslvQKHwS4oQN57n8wmkTOJMrAy_Q09n8g1HqQRJ3s8Lfph9B96WVqpsukWp7dCUE9DAHR4CcGWIWGzOyNf_LSZG54y8Z0raQ6jfdqnntH-ASKvUVYzegqQjennQxp9ptINxxDe74tXdzXv4ACsYEf9ro0M8mRpBFZIEudIyzk8MUP9brEH6xKA4izw7p8tcvCSa79yW8wbMmLmjyZBB49yBIpRyTjCS79zYX31qDt3z9O1itgoRet0MtjpJtyo6kXaqA7Rvsb8pVrvu2d6l_jYFWPieAcT6tNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484016062d.mp4?token=XwK6m1hNvUuNz1N1qvsvmDpKxC3-OkGlD7NwXqm4TCm9U3Jt93DTslvQKHwS4oQN57n8wmkTOJMrAy_Q09n8g1HqQRJ3s8Lfph9B96WVqpsukWp7dCUE9DAHR4CcGWIWGzOyNf_LSZG54y8Z0raQ6jfdqnntH-ASKvUVYzegqQjennQxp9ptINxxDe74tXdzXv4ACsYEf9ro0M8mRpBFZIEudIyzk8MUP9brEH6xKA4izw7p8tcvCSa79yW8wbMmLmjyZBB49yBIpRyTjCS79zYX31qDt3z9O1itgoRet0MtjpJtyo6kXaqA7Rvsb8pVrvu2d6l_jYFWPieAcT6tNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای فاکس نیوز: نیروهای آمریکایی پس از آنکه ایران به دو کشتی جنگی آمریکا موشک شلیک کرد، سه نفتکش ایرانی را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/687533" target="_blank">📅 23:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687532">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6a40b18d.mp4?token=FaCteOnp3qgRTDgV0DwDjq1lBgRbEpdbjh4ZBTkIgQPiP42uc5YuWikyFZb_NtypDWHvDN9GrFWqZ9GC_Za6XZC9MeaoW8eCeuIfvEKBv9KG5YxrXbLk6vOrAbR2erpuhC0x0tCZJ9ZMkRcTaPv7lOjW_PbKDqjSuUaOnRNOcedXG9Fhr3a1Pd4ZPplTBxhkj0XqRoli_lGji-sHwgLfLkBeJrben2gAPVj8yyiPu4kiCv0LE1fV50H5a1w3uCqWbUmFvQBTPEvm-mo8Xv2-xkfiPCRLK8iiyad2YhYHO3zkU4cEoBuO9I7QlqUJxZ_BisiQ2xI5Bsva6FnnCTgrf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6a40b18d.mp4?token=FaCteOnp3qgRTDgV0DwDjq1lBgRbEpdbjh4ZBTkIgQPiP42uc5YuWikyFZb_NtypDWHvDN9GrFWqZ9GC_Za6XZC9MeaoW8eCeuIfvEKBv9KG5YxrXbLk6vOrAbR2erpuhC0x0tCZJ9ZMkRcTaPv7lOjW_PbKDqjSuUaOnRNOcedXG9Fhr3a1Pd4ZPplTBxhkj0XqRoli_lGji-sHwgLfLkBeJrben2gAPVj8yyiPu4kiCv0LE1fV50H5a1w3uCqWbUmFvQBTPEvm-mo8Xv2-xkfiPCRLK8iiyad2YhYHO3zkU4cEoBuO9I7QlqUJxZ_BisiQ2xI5Bsva6FnnCTgrf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه قضاییه ایران در اجلاس روسای قوه قضاییه کشورهای عضو بریکس حضور پیدا کرد
🔹
حجت‌الاسلام‌والمسلمین محسنی اژه‌ای که به هند سفر کرده در روز سوم سفر خود در محل برگزار اجلاس روسای قوه قضاییه کشورهای عضو بریکس حاضر شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/687532" target="_blank">📅 23:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سفید شویی حمله هسته‌ای به ایران
🔹
از برخی چهرها و رسانه‌ها، زمزمه‌هایی مبنی بر عادی سازی حمله هسته‌ای به گوش می‌رسد. آیا این اظهارات صرفاً مواضعی پراکنده هستند یا بخشی از روندی برای عادی‌سازی چیزی که تا دیروز غیرقابل تصور بود؟
🔹
در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/687529" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ارتش آمریکا: ایران به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌ شونده آمریکایی حمله کرد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/687528" target="_blank">📅 22:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
وحشت نهادهای امنیتی آمریکا از گسترش جنگ با ایران
🔹
شبکه ۱۴ اسرائیل شامگاه امروز اذعان کرد نهادهای امنیتی آمریکا، به شدت نگران گسترش جنگ با ایران هستند.
🔹
این نهادهای امنیتی ابراز نگرانی کردند که احتمال دارد نیروهای مسلح ایران تصمیم به تشدید و گسترش حملات خود بگینگرند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/687527" target="_blank">📅 22:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
استاندار کردستان در پی انفجار تانکر سوخت ۲ روز عزای عمومی اعلام کرد
🔹
در پی حادثه دلخراش انفجار تانکر حامل سوخت در محدوده پلیس‌راه سنندج ـ همدان که تاکنون منجر به جان‌ باختن ۱۱ نفر و مصدومیت هفت نفر شده است، استاندار کردستان، ۲ روز عزای عمومی در استان اعلام کرد.
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/687526" target="_blank">📅 22:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687525">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6EMwo5SPprbLAfQyuUOfWubA2MrxTAIN-JpgtL58h_bl-0SkaGCzF9GXbEEh9XdCGaow3vYeOCNzy12KhEo-eJgty--I6AJWg_SOJ0whLO_PMf0ZbQ5BVWbsEkLF01KfNOeFeBtWq1ykPTuO7gqQf5ABQq3RXHfnlzUDlCo1ZqJQmlrGmZAZghdlx1OrVgxJwuwv8iPci9Dt8Zd71QZQPQZop8JgomDNAqhZHVnrqceAgtM3W7g-Jssmn7zIoiZ_JyyAEy1PXTiaCi0zC03fTgdc4psRp8OZmpryCqpmmHKyImhkj5pjYsDOVpkqycZbEvD56Y7Y__VG-QuJeZIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف گردنبند ۵۰۰۰ساله از جنس دندان
🔹
باستان‌شناسانی که در حال کاوش یک تپه‌ خاکسپاری ماقبل تاریخ در نزدیکی «وروتسواف» بودند، یک گردنبند خارق‌العاده ساخته‌شده از ۴۲ دندان را در کنار اسکلت یک مرد بالغ، سلاح‌های سنگی و بقایای جمجمه‌ انسان کشف کرده‌اند.
🔹
در بررسی‌های اولیه قدمت آن ۲۹۰۰ پیش از میلاد تاریخ‌گذاری شده است که به عبارتی دیگر می‌توان گفت تقریبا ۵۰۰۰ سال قدمت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/687525" target="_blank">📅 22:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687524">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9dRQrm7HWwBklyKbd213d-405NtDS9tNAy5kVkhaTWMQSN-MTW4VevdSNwbFIfgmA3HjBwAw7CyXKEveRjd3lw9HcJ0vJdiBVs-v72CH44B5Ven3xRrZNmi7MmicM9FpDqVvdQ9sh70GsAgmE0Nu6RUL4Drd8Qhc_2E5Qs3jfYUonB4pOfyFPiI30zQpH0rGGNO602PhQBzim2nMLFFttegknR8M01MzWFdbInS-2ds4KEuEFF_8-B6ndPelrcuWDt2-eKLH_e-R4Z2BRYCq9gy1J3qV8aBDbq09npBrtzbPLYbNF4EY_FzsukEY2tyNSotDXNJvHWuqGENAQMO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سر در برابر چشم
🔹
با شروع بازی خطرناک نفتکش در برابر نفتکش توسط آمریکایی‌ها، به نظر می‌رسد راهبرد سر در برابر چشم که پیش از این روبیو آن‌ را برای مواجهه آمریکا با ایران پیشنهاد کرده بود، اینک می‌تواند به یکی از راهبردهای ایران در برابر آمریکا بدل شود؛ حالا که نفتکش‌های ایران مورد هدف دشمن قرار می‌گیرد، چرا باید خط لوله‌ها و بندرهایی که تنگه هرمز را دور می‌زنند به راحتی به کار خود ادامه بدهند و سالم بمانند؟
🔹
هشتصدوپنجاه‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/687524" target="_blank">📅 22:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687523">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/687523" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0Ne8o1PIwjnCQ69ZGD9Sc2wlUmCSaIW8DnskA8KIUKb83869jJ33t4w_k470foiky1xosb44mZUf81JQ-KbdcMjBbkZAtSGsuF60V2v7oa9XeFr-B0fRj_Bz9nReZSPrUjh5ZroJzV3_bjit7OS7EEPjZeS2V71zm7dIAvEGlP4RyvBajwQ3qYoFpSYaCr2tb53RJJbVQaYE9FC66XPY1MY84vi1lr_1VZ7kIPb64-R2UJ21vaGweYJpVZ5UGxtCeBKTB00IV4Mpsc2_Da8XVqXTDjPJLKmDElDbz7UQFm6tQl3wyRCQb-JgAobcSb_plqXTldEeNZo0wDChXMf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gjm5wK1Ze3kN4P4oIzlJm8w3DplwK4zy8Qi9rEbq-39uGvHxGBb1LPRWw7koh26mXqHBTL7OrBDw5Y83oxSXkAZleRa5dKapwl_Snt_DpgsJxUxsssvdy8Juu6josnaIJdtTDMNOIKCJj93bmlxw3GjFuPuWckrVuoM_pzctgknWMQCHccB6bWwo6kq3LuqOr3xf2EiHnaBFUdnU00iEqPWHSgli92fdXwblaIfOJTdH-jsSDyYWDeJBNJgS9bqyNaz6FgKVZxEPnJNAQSYNQQLGy4pk3n4JQgK5L5Sjn9QdYuwKZtM_diNQ_b25sJjx8pRi2omQ9Af6cyK3z3JnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7CTRYCSQ89QsJESkC0lOJM7ILZjYJc28cINssq9g84sEGlZCwtFUBR2N9Xih43clbVM5YWHJVOfGYklr4kVZd_4aNRYA8asFn-75RxE-NaekVWCW4xhPZK9v9ojJkTDA416Ss6eL0fk7r_2cW9PhSMIWkEFQsU7koUPuAoE2oZvtqq8txO9ukOaHq2PiUBKt1QOPsk2d2gbIghOdz2GLPt5SyiqTQVnZ1GmBVZHkk5M3e9Dzq7oz7SqNVmhvVA8wbiEgYxO_cqP4zhnnuz4uGodpNF9RytVPTk2RR3y_kczrRki1ruj-sSwFoL6ERpYyiXaoIc0gAEZFDHVxBRMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1IGV6_Wh_YA1bp1mRVlGpWrCH-XkzQsvr-WYOdMlu7OKarpMiFzROYZ6lkMQ0A5r56HEVGT5Ag8g5bnR8clyw1C7CeC97H89G9FpVBAOTtIJE6I9JLgZ-N7a_2MR1roG9ixg9ReaS8S1PoRM9luEJMQqL_w9Wvmeke6nuQsnjrQX8xEzJ4ut6gM15IFUuJkOugsdEom6spicD82AdPcYkIv2kXAn1MQkscLjutKlrcwc0ujOl5_tZrv6Cg6PDvWP1UfpmDSgKxEiqjZzIHpYsOVOJ43-tcCBLMI5spabJghFCN9DYAP9w2PaqhRRVxAgqQuc4X3n2roZQ3DVEKqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_0JGQlERSZZPsK1Q72ZFLZ6Qnv0xAsXMtJ2aft6u8eBIGumpYIviv6-6FkwXUX79gq34Ah8UHabN0oPMRn-MdoiNP4RbVWVu8lUDT-i0lZDkNuBSoSLnj38nTtBqG6hWy5A95GNPBlAgrnGcKPPEZvNyXPDdjagZHsVZDczS2MTJ-fNXrxExABf8UZvt5L3oMHUrSezYerzqw5Zb8-hfejrT7Pujj7BWr00JRhHGVXe-R9VnjlTahwiWoDA1DbZqtL-N68mgbZmEy0ts8DiRIOUHBglQY--UqJUCLHbaUlAZtS5uPKzHQ7EUsbyqKANH8nOEjWYAEY2RBJ87GKF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTEzPoorykQ4TCP867kbKDDpnstepPBZgHGEe3XwZkjVTq1qzDGeshUNuTzwsakp5j6LBIqAToLN4aEnuBaqjM8c4vaKBJ7nnhb2msjfkf0PC70cHSxGDLlp-gGkMF2ujLB_kp9Yxrr5YR5remewK_I6j5xzfVXZi1bg176_f2WtfC5_zPEinUvNiqvd4KTKwpAcH3VNwws89gSPy9LRLlYga8pxP72R-BdPj-nGM6Uh7689eaT5i6O2KRSgBkbOOcVgZrMPoqeZgzd7ctl65OWRjq0WQ8rEceja4a-UcjGxz2aJVTS-vDs8wlN_vT-XTEUfm-Xmle1fuNSuAObBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cI7yQCxX_XABWxpYnThHeRUq6pFvjJLIhh1ha_GAXsNYIVybut_CnxkJohdhszzNc_AJP0lvSDcVXty8PqQNJTFf4Ig5VYtEY7Xh990Qxfb3q5DBKMPRzcIdcnRDDYf-iT9pBHDLi3wvXlJbCTcqZXg9i6MxQ5zJFV3AeHTj_YB9wVNtz5hHmk-qBCCMxZj-UWFC-rDqohy02R_51GUvbGu0xgfKIbikFmub3VHyo6e-1bxRTAnJlUnOFOlNP-8qAKTtOPLBbwrTxU0mjpYX9WdSvOxpMcl3Z9unYY7BuhhCzP9dMcwT297rvDf_RyRrHP-0JPJX1nP0DpHGDs-xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cb1BijU4m09iXYIMgguIKC3oweMCCsi_XAt2pxVuKh4K4Yn90MmiD6_mHu0lEMVC5pnuGrAwKmQZBHMhEIgEIEHS6JCq2bruL3dTdkw6azYDTJKP-tCgSqzcS0Xf1uaA3JVbvRzDHOll_c7HIlggCzK2yYQRTodwSQH4tkYAlvr1ZK3kHG1xX5pCUPWZs17eXe0CufncojQNvM2RIlt3BBoQ1bpZiuDHCoMBt6zRWCF_gZ-tMG-ha5VerGXBtvP7CfqwSfRAcn6gdI78BiFfTA_I9h4v9o_MjIw9G6ReTe4p5ALtEETVg_Y0ANBlEVWefGvEV7V5L4DTmvrz4CxAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twRVn_Nz1wFTByon9_NRBZaFRCmocTRqj8egPu0QqdBYQI3dwQBHmqcJ_PGJJXhn4fGgiWZh2vY-bkFsjyrRPjHSsNQx2LtLmgeELOWvGw0eEapJSnjMkcdREM4dG60rKkZcSylJQLGzN1f9cKBvC1wh2HwTKNNidP4Hk90XJ2mAyjmV-7SChdM-mmpgW3EDoVI-1-gT7cot9247x3X_5BrFBNEO4aO-29F4siHSYQpYsRSdmDuvQ0JxVailJEFBI4-b-iprVGCziLbPykHZfwJb-jQ4ptp-hQ7H0BV50m7DGpy_jsWQF8lauGt__MkbaUUCrNfvS6lOckGPFznTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPwVx4Ch3CCwXGmvxWJTxsUu2dmiLqhQgFYpF3tr10t3Kv8or15nTARW-Xn34tQIFnULm7nSHIbtfQq026Pgo53xAEhaw6R5yGs9NLkPzB0Eob-DamLIoyycS3o8OgCDkKq8vnkVx4KPWz1bjWAmsrn6tOHVkVxAZ90Hagn1yZ0YH3g56Kt1v2Sk0YWW4Aa89Ngf1zuyWcQ3aE3-NHkKoaVg11sHKr4cUjp1OHLmcniOmH3gC-t_d1AqTSE5VDuknnP3yhtO0dnpbVAkAFSkGuHDnFD5tVkiJubD5uFG3BjLzPCtRejwt9N_4Je13EhGCge9rvQ0j3xebvKmsGK95w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
انعکاسِ مشکلات مخاطبین الوفوری برای  تهیه اقلام دارویی ضروری .
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/687513" target="_blank">📅 22:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
اولیانوف: انتظار می‎رود موضوع مربوط به ایران در نشست شورای حکام آژانس بررسی شود
🔹
نماینده دائم روسیه نزد سازمان‌های بین‌المللی در وین اعلام کرد، مسکو انتظار دارد مسائل مربوط به ایران، سوریه و اوکراین در نشست ماه سپتامبر شورای حکام آژانس بین‌المللی انرژی اتمی که روز دوشنبه آغاز می‌شود، به‌طور فعال مورد بحث و بررسی قرار گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/687512" target="_blank">📅 22:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD0iTl-8bZkwvAfeYePNU693anqZBFAVy6mbIoq6wCY711mcswgmrVfiBJR48ChojM8WagYrw7eURlFrD7Y4jtkJDmfVZ1BRxCDtmyiShq0Q7hjnGR8bXXFSzbLIZk92IuflvzG3JRMUJXtTr71cP2IDiORrqLfaGsp64ALxZg0s9KLbrudt_zogi7h0L5vmCD6aXiKBaRDbrebLn2uUwP08DO449hCk-2RMD__3uPOvsorw97bRelJht4gNcuzRYT1EgyAG1VjN3U_QHfLj1SyTII8Fc3S_rPgTIdRyBjDgLz1ewE8OZiKggbj7n1nTcOxLwwEnRppX9cxh2-6LJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای اعزام ناو از کره به خلیج فارس/ ایران با کره‌جنوبی وارد جنگ می‌شود؟
🔹
به نظر می‌رسد در صورت اعزام ناو از سمت کره‌جنوبی به خلیج فارس، ایران عملیات تقابلی شدیدی را آغاز خواهد کرد، چرا که این مساله می‌تواند سبب به هم خوردن تعادل جبهه ها و باز شدن دروازه ورود کشورهای خارجی به خلیج فارس و کمک به آمریکا می‌شود و این اصلا برای ایران خوب نیست.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3242872</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/687511" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI1q0636gc_sEDF53KpULULAAQr_Sb2Q1UN2EVLmNLg9wTD2LEPzlM4Lza7VuBny3ajMw-VIEEN_HZysP_BKWwYiVFrkFuY-MNO--iyEs61TLUktqISXlj0AC6_BOFJHhipi3Ern0kDn9-QAVvv2WL5ukK5RWUYBzk1Uiifclyy_RYAIntjflaKMAsAfAWtSrZwDysLbSfFsLa5YAGZHBVDhs8UtlpGKCM-qB56fjmyf7wWVjYtwQC_WLXmFUsXzBLk5YjUtJi2oJ2Qs1OXHz95hZyhKW3EhkKzBwk9jzMYqyJhR2nWqBQysDz2wEBdTKHUWCI0v-U9Et6IJ1nN_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توانایی، وقتی ارزشمند است که با خویشتن‌داری همراه باشد؛ قدرت واقعی، در کنترل خواسته‌هاست
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید: «هرگاه توانایی افزون شود، شهوت کاهش می‌یابد.» انسان هرچه بر نفس و خواسته‌های خود مسلط‌تر باشد، از وابستگی و زیاده‌خواهی دورتر…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/687510" target="_blank">📅 22:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای رسانه صهیونیست: ایران در حال آماده شدن برای یک حمله شبیه ۷ اکتبر است
ادعای جروزالم‌پست:
🔹
ایران در حال آماده‌سازی برای یک حمله هماهنگ و گسترده علیه اسرائیل در چندین جبهه به‌طور همزمان است. این سناریو شبیه به حمله ۷ اکتبر طراحی شده، اما با این تفاوت که از ابتدا برای گرد هم آوردن تمامی مؤلفه‌های محور مقاومت برنامه‌ریزی می‌شود.
🔹
بر اساس این ارزیابی‌ها، ایران به دنبال ترکیب نیروهای خود با حزب‌الله لبنان، حماس، حوثی‌های یمن و شبه‌نظامیان طرفدار ایران در عراق در یک کارزار واحد است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/687509" target="_blank">📅 21:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VglW0WEzJXA4CuYZtLBOqBaMSanRRz9XTg6U5wO6L98g8LBpKO3xSBXaAZ5ZQG1nqHKVbOgDtybsjGMWTIqjYFZ7H12cDAiuc06FmacRZdK7JBDJ1v1ZljFvjCvL6pSepjkeDQ3cxt-aMRqceH-I7ypO2ps1YlCYF0uIOq0REF0cgoIanH8FB2MTHs6CB7CDfN4eiNt6J6qZ5lM1F4BiBFo1xDuEChkW-mEhWT0gVKMLU2iW8PwblMUh25OA4FqHxa4sS6zXd5hhBhEGm9L1XEazAn8HXIgac4faj5pQjhno1KWdiRMpHHaS2LFyH5n5wrv6Ye8hl8RJbA_57wkZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارمزد خرید طلا در زرپی برای همیشه نصف شد!
🔹
از این به بعد کارمزد خرید طلا در زرپی به‌جای ۱٪، فقط
۰.۵٪
است.
🔹
یعنی با هر خرید، هزینه کمتری پرداخت می‌کنی و بخش بیشتری از سرمایه‌ات صرف خرید خودِ طلا می‌شود.
🔹
این کاهش کارمزد موقتی و کمپینی نیست؛ تصمیمی دائمی برای کم‌هزینه‌تر و شفاف‌تر شدن خرید طلا در زرپی است.
🔹
اگر طلا می‌خری، چه به‌صورت دوره‌ای و چه با مبالغ مختلف، این تغییر می‌تواند در طول زمان تفاوت قابل‌توجهی ایجاد کند.
🔹
برای آشنایی بیشتر با زرپی و اطلاع از آخرین خبرها و قابلیت‌ها، عضو کانال تلگرام زرپی شو.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687508" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سنتکام: ناو جورج واشنگتن مجبور به فرار از دست موشک های بالستیک ایرانی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/687507" target="_blank">📅 21:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5a97038f.mp4?token=iP1Ax3CWiBVpXN2mdrGTfR_VORzvLlt8d8JIleGvppU5YlTUugaUP6NBlRHwkCH5R5iQTyYD_jLI4WCYpSesq_3HVTok-v23bV5ct4_DzZk1n7MAeT0Y3lprYP-HbMHxZo-vW4hmqbT5Dqmvk_9N1i25C4F72rC2PPil3399DX430iOdTcYLcATbpEo4R84KmYQ2ttAv9LxJ0ULHo36xzddt2WFD5tCFZ2jj6i3JLAnr62DlPw-rBhyK02xbeghSAqZEMQjI21u7g_9zg0vGyLO48jPl1j8nX8agrpuKmEidrRUhc7y8MhTn4HRE-pCKTumMaumrKgeq6NLNXCbU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5a97038f.mp4?token=iP1Ax3CWiBVpXN2mdrGTfR_VORzvLlt8d8JIleGvppU5YlTUugaUP6NBlRHwkCH5R5iQTyYD_jLI4WCYpSesq_3HVTok-v23bV5ct4_DzZk1n7MAeT0Y3lprYP-HbMHxZo-vW4hmqbT5Dqmvk_9N1i25C4F72rC2PPil3399DX430iOdTcYLcATbpEo4R84KmYQ2ttAv9LxJ0ULHo36xzddt2WFD5tCFZ2jj6i3JLAnr62DlPw-rBhyK02xbeghSAqZEMQjI21u7g_9zg0vGyLO48jPl1j8nX8agrpuKmEidrRUhc7y8MhTn4HRE-pCKTumMaumrKgeq6NLNXCbU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان بولتون: هگست صلاحیت تصدی وزارت جنگ‌ آمریکا را ندارد
🔹
طبق گزارش‌ها، هگزت برای پست «سخنگوی پنتاگون» به ترامپ درخواست داده بود؛ پستی که با توجه به سوابقش، گزینه بسیار مناسبی برای او محسوب می‌شد. اما کاری که الان به او سپرده شده بسیار فراتر از توان و حد توانایی‌های اوست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/687506" target="_blank">📅 21:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
حملۀ هوایی صهیونیست‌ها به علی‌الطاهر با وجود ادعای تسلط بر آن
الجزیره:
🔹
جنگنده‌های رژیم صهیونیستی شهرک المنصوری و ارتفاعات منطقه علی‌الطاهر در جنوب لبنان را بمباران کردند. بمباران ارتفاعات علی الطاهر در حالی است که رژیم صهیونیستی روز پنجشنبه گذشته مدعی «کنترل عملیاتی» این ارتفاعات و ورود به دو مسیر زیرزمینی در آن شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/687505" target="_blank">📅 21:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ5TBiJF0mODV4yyjOxvwbpucoy2a1GA2afhN0hspZruGzK-b_bCRKg9PoxNNJiij1phQnFTmnHrmYAVNAt7qXxWi8BO0faGLhiWqWWmkhP5uKtnPVXL9hoquXBSVHWCJ0qa2aLsKA5ZoLo3utAZ0jqRO7g55GJL4nmoflUoruYbwVSK5hmOBi4Ykn5RiZQ9Q0gkpEYqGUqHkiVpqEZFSRrdA0yXocu3SfuMffpJ2cV0jHRipJSus5QHORxmTsGHm781oUX5umHdnpVpDktzSY04_6MUcUSQz5IHIF7txN0oot7UppptZjmh8lwMRaHBSdR8fT_NSLuqdef8opl5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: اکنون تمام کشتی‌های نیروی دریایی آمریکا هدف هستند. هرگونه حمله به کشتی‌های ایرانی با حملات متعدد به کشتی‌های مرتبط با کشورهای شرکت‌کننده در تجاوز ضد ایرانی مواجه خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/687504" target="_blank">📅 21:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5fEE6Xmid7XEz7mzA2IDIB9zEfVm6PomtJBnBJLlZgk7rdaMP_NP8-fqp0cpT-rlgfwPO-_xhu4nxM8ZBFiTPA-UE6heVIFaComen2hJuRnMyXsn5ec6h6Bi0Pvt5rsTRmctHZnj7L-Gj5PTtVY1i3Uiv8dwoRncpV6a0R92zjMyDeoPDgNKHuaEcAxTmuxAY4iLN4TY8o5jj1eH9TE936GDtkyHTGSHDuRmtUhcGHlwzVJFpgKx-dLKqXVafuShFnLQ9mqcBAwa3qB9A4Bug4XfXLO3VvE_WG6nRto9w55rKjSb3Xy2GlSVC8kQ27AAv8EP2v7AgQ1TGz8fy3ALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه در محکومیت شدید حملات غیرقانونی آمريکا علیه شناورهای ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/687503" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تذکر قاضی‌زاده هاشمی به دولت: ادبیات سیاسیون و دولتمردان اصلاح شود
امیرحسین قاضی‌زاده‌هاشمی در
#گفتگو
با خبرفوری:
🔹
اگر امنیت جلوگیری از جنگ می‌خواهیم و اگر صلح‌طلب واقعی هستیم، باید یک روایت قدرت به خارج که ما در موضع قدرت هستیم از ایران انجام دهیم و به‌درستی روایت ناتوانی دشمن را بگوییم، به جای اینکه بیایم به سستی‌های خودمان اشاره بکنیم.
🔹
اینکه ما بیاییم یک روایت ضعف ارائه دهیم که هنر نیست و امیدواریم که ادبیات سیاسیون و دولتمردان اصلاح شود و بعد کم‌کم شاهد توسعه آن در ادبیات مردم باشیم. به نظرم ما هنوز به این بلوغ نرسیده‌ایم که فصل انتخابات با بعد از انتخابات متفاوت است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687501" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a6521f5d.mp4?token=GItTsLAKorWs5EQNgzyhTD_FNi2Mm8WorQ6FtX0JKim3Y1c9pQFxs5GcMaD5nMoyq7Dl-ptQy4aU6pDidozEN3qc5xauyt9T_1cRSL4lrvbxpjtNEz-VMoS70P18yBh5mxfEe9iVehxrMJr3H-VffiCLeDxavrbV0UcfjUaQRDLhZxVSlQZChWjYwWWzigfU1W2yjBm3SNf666O-OrBg7YvrGU9W-5AUZeQaU7FZO4FGwLpstJbyqY-xIEz5hBxs4k7Bd6ROKqEClqEov6QrRJBwyuohqeevZkg2axvq4mBQ8osJ1b4WV9jrMhcQWiNqX6z1T10JzaBNsJWakpKhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a6521f5d.mp4?token=GItTsLAKorWs5EQNgzyhTD_FNi2Mm8WorQ6FtX0JKim3Y1c9pQFxs5GcMaD5nMoyq7Dl-ptQy4aU6pDidozEN3qc5xauyt9T_1cRSL4lrvbxpjtNEz-VMoS70P18yBh5mxfEe9iVehxrMJr3H-VffiCLeDxavrbV0UcfjUaQRDLhZxVSlQZChWjYwWWzigfU1W2yjBm3SNf666O-OrBg7YvrGU9W-5AUZeQaU7FZO4FGwLpstJbyqY-xIEz5hBxs4k7Bd6ROKqEClqEov6QrRJBwyuohqeevZkg2axvq4mBQ8osJ1b4WV9jrMhcQWiNqX6z1T10JzaBNsJWakpKhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت حضور پلنگ ماده در منطقه شکار ممنوع کوه سفید/ پریزاد نام پلنگ جدید شناسایی شده در دماوند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/687500" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f970358b.mp4?token=GXq8qISXklNNxOKbawT4YxpBspGDyPtnN7Q9TqSp1uvn2uI16jds7_zf0-PnS6xsBETeSsG9-4I2_o12BBWpNb26foJMCnf9HaxlJeBZCG3zRfj-qR0cTAhstByr7hTPXXxxiPTjfpJX8ayo5GJbGpgszGIB7iJlWm7I0qGHbVyMIcw9rR9iXIHXjiEoP1OExKQs1a29iR3s_AyH36eiAAo469AcseZVN-pagEjFGxyCLnKae8qDNnM4hJ2K-FOiUMuLEahaRBTlJPn2t1VEhz6UuGJIMGZSNRtfKZlyv45lqY0fVY8guvSeFeaIhucTtMKaUN4O54rrDprPAxKeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f970358b.mp4?token=GXq8qISXklNNxOKbawT4YxpBspGDyPtnN7Q9TqSp1uvn2uI16jds7_zf0-PnS6xsBETeSsG9-4I2_o12BBWpNb26foJMCnf9HaxlJeBZCG3zRfj-qR0cTAhstByr7hTPXXxxiPTjfpJX8ayo5GJbGpgszGIB7iJlWm7I0qGHbVyMIcw9rR9iXIHXjiEoP1OExKQs1a29iR3s_AyH36eiAAo469AcseZVN-pagEjFGxyCLnKae8qDNnM4hJ2K-FOiUMuLEahaRBTlJPn2t1VEhz6UuGJIMGZSNRtfKZlyv45lqY0fVY8guvSeFeaIhucTtMKaUN4O54rrDprPAxKeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این کدهای مخفی خروجی‌های خاص و متفاوت از هوش‌مصنوعی بگیرید #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/687499" target="_blank">📅 21:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در جاسک و قشم: صداهای شنیده شده در این مناطق ناشی از تنبیه شناورهای متخلف در تنگه هرمز است و در این مناطق انفجاری رخ نداده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/687498" target="_blank">📅 21:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: به ارتش تروریست آمریکا هشدار داده می‌شود در صورت تداوم شرارت، ناامنی و مزاحمت برای کشتی های ایرانی و محاصره دریایی ایران، ضربات نیروهای مسلح جمهوری اسلامی ایران علیه شناورهای نظامی آمریکا در منطقه شدیدتر از قبل خواهد بود و امکان گسترش آن نیز وجود دارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/687497" target="_blank">📅 21:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSNYNs4HN0pdFSMxW0BM9uUxpE-QJlypN8gHds6dvzIHsoyBDGK6CABpgGxcdIfQbDrJ2pt0znQ9PDz1WNMZ8AS-z8CFIHOJHDbWqi4WC_Yd82nbHK0V8l2USZ-8ShpN5_Enc4rVEqtFLDmwna4AshrtffHTXzi8gq4QtVnaEs9mVKIQwgdRJELP2ZV4Baw5Svrt959m4-ipOdI_0CjQOTv-oYZlvM6kaQmIBP2YnYO253paxYVWuvWcuhDGLqNJ_UHubz7PLF9Q0551MLY4xY_VAv-89D9HbEUBykeTe-u06aNrs26eQnyi5VzhcxCiWo4lb7-stg0GoQpMK1648g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر معظم انقلاب: امروز روزی است که چشم‌انداز غلبه نهایی حق بر باطل، و اسلام بر کفر به‌مراتب بیش از همه‌ ادوار گذشته به عینیّت نزدیک شده است
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/687495" target="_blank">📅 20:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در جاسک و قشم: صداهای شنیده شده در این مناطق ناشی از تنبیه شناورهای متخلف در تنگه هرمز است و در این مناطق انفجاری رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/687494" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-RR59dutna6g4zvtTrbgRH-HhecBZq4S1BuXTOAVtF5s2BD05oGJQydMA_1jPM8zpzPYVq7Xk-BXedOBRCWCWkPFbDcrhEwNWhz6Snv3Ux_RaYtWu_8garzz6Fe1o6J41K1R2cBGy0IAqDK5b-q4psP-AmTiLtXos4Visr3MSM_6tTIHjSi5YzpY0gDWtpKqHsr85wkO3zDDGGt2HtxrjxQSOlMK2wr6JPNbFB-d1wuucrr2HPbylsSExRX0CryTX_ueKliKuH-XiPwGJIZHu7k2gqsRUr90W7Q_zamoEpuvFbnlUJ_XcQpzH4gilC2FH5v5jg8Xu197QDP5txp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افتتاح متمرکز هزاران پروژه‌ خانواده ارتباطات در سراسر کشور
🔹
رویداد ملی «یک ایران متصل» به‌زودی با حضور جمعی از مسئولان دولتی و فعالان حوزه ارتباطات و اقتصاد دیجیتال برگزار می‌شود. در جریان این رویداد ۷۹۴۷ پروژه ارتباطی و فناوری اطلاعات در سراسر کشور با برقراری ارتباط مستقیم با ۳۱ استان به بهره‌برداری می‌رسد.
🔹
«یک ایران متصل» قرار است تصویری از دستاوردهای دوساله وزارت ارتباطات و تلاش خانواده ارتباطات کشور برای توسعه دسترسی عادلانه مردم به خدمات دیجیتال، افزایش پایداری شبکه و تقویت زیرساخت‌های اقتصاد دیجیتال ارائه دهد.
🔹
هدف نهایی این طرح‌ها، کاهش فاصله مناطق مختلف کشور در برخورداری از زیرساخت‌های نوین و نزدیک‌تر شدن به مفهوم عدالت ارتباطی است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687493" target="_blank">📅 20:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
مورخ برجسته اسرائیلی-بریتانیایی:
طراح و معمار این جنگ نتانیاهوست؛ او یک روان‌پریش نسل‌کش است و هدفش نابودی ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/687492" target="_blank">📅 20:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sJu3dgm3y_xFnGPbI7G7jKE0Zx2O_XQkDFJX2bvz0UwjQKjlrNRsRy45DJhp-cRjEDynFyM6Ro3wVhQqLsNjN4e3OdiIe82rgZa0oIHB-wY4lNETTqErfOMUYuylRGE7iAuMfsGWVHBNiX2AUs5jy0I6Vnyed8XsoT2yJA-UUHdqglpK4-BLLZAm-CMaV2m0FbHyR0bsoLKIYEb69v-EItReIdl-3Na259EeBFfBcY5X55fNZpdtCpmIfdU43AfRmYbPkBVKXfZM5ZJAqT3Nub6_8oDKTOx20FwrvDWA7R4XS-srlXY35uPr5n2jiKs4awUS7UfK_osEPMdwUZgSNWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sJu3dgm3y_xFnGPbI7G7jKE0Zx2O_XQkDFJX2bvz0UwjQKjlrNRsRy45DJhp-cRjEDynFyM6Ro3wVhQqLsNjN4e3OdiIe82rgZa0oIHB-wY4lNETTqErfOMUYuylRGE7iAuMfsGWVHBNiX2AUs5jy0I6Vnyed8XsoT2yJA-UUHdqglpK4-BLLZAm-CMaV2m0FbHyR0bsoLKIYEb69v-EItReIdl-3Na259EeBFfBcY5X55fNZpdtCpmIfdU43AfRmYbPkBVKXfZM5ZJAqT3Nub6_8oDKTOx20FwrvDWA7R4XS-srlXY35uPr5n2jiKs4awUS7UfK_osEPMdwUZgSNWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری وزیر کار دولت شهید رییسی: برخی کارکنان موسسات نفتی و پتروشیمی بیش از ۲۵۰ میلیون حقوق می‌گرفتند
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبر‌فوری:
🔹
در طول تاریخ افزایش کالابرگ و یارانه در هیچ دولتی به اندازه دولت شهید رییسی افزایش نیافت.
🔹
در دولت شهید رییسی حقوق حداقل بگیران ۱۷۰ درصد افزایش یافت. در سال ۱۴۰۰  با تورم بالای ۵۰ درصد دولت را تحویل گرفتیم و با تورم ۳۳ درصد تحویل دادیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/687491" target="_blank">📅 20:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee0880e45.mp4?token=Mv7iimG4PtJDZoneD3x7rLrmWUiIS4UwVPaQyJ5-KbY56KGukXPO_lE1v7msxwH6unSPi68U99P71u1jcd0sE6usEV8P93DW7MsHNPV7IUabp9kh9hAFArUTPzkVTXLblLdyBJuHM9KunBsVpORg0FrB3vEO0zcgxChzMYIdyI00c71La15lHl6CM3x787CGaxXAdvnkelRHIVSvBlohCqc98QBmx7FaL04r_vRSoxVNaNYzty6CumlRTE0nQv1Q-PE5Ymx1-H2Um-Q6pVd7uDHCsAZw60FI5273T7TJL9mG6F1U4NLwWHOh193SSxf3QJ1JHiKMTMzcZ5FOAdoCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee0880e45.mp4?token=Mv7iimG4PtJDZoneD3x7rLrmWUiIS4UwVPaQyJ5-KbY56KGukXPO_lE1v7msxwH6unSPi68U99P71u1jcd0sE6usEV8P93DW7MsHNPV7IUabp9kh9hAFArUTPzkVTXLblLdyBJuHM9KunBsVpORg0FrB3vEO0zcgxChzMYIdyI00c71La15lHl6CM3x787CGaxXAdvnkelRHIVSvBlohCqc98QBmx7FaL04r_vRSoxVNaNYzty6CumlRTE0nQv1Q-PE5Ymx1-H2Um-Q6pVd7uDHCsAZw60FI5273T7TJL9mG6F1U4NLwWHOh193SSxf3QJ1JHiKMTMzcZ5FOAdoCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروریختن پل معلق در لحظه افتتاح اندونزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/687489" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آغاز مذاکرات پوتین با فرستادگان ترامپ در مسکو
🔹
کرملین از آغاز مذاکرات ولادیمیر پوتین رئیس جمهوری روسیه و فرستادگان ترامپ تروریست(کوشنر و ویتکاف) در مسکو خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/687488" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b76139f2e.mp4?token=LDPefTE7nNPu-gjkqtKdnVgyYYdYB95UEX81jL95ARqcoUu6VksC0Fde4U--SctDDIXg1UYrLQg9JpR18R-Ohl4V92FLK525FViZtkUZec3JTUgmfS5qUoznnUohdeesk54NSBqbS0mAR0QX3WXWMZWy8qE2Ggte9cDGRCtNMnZV08Qtqll5-SLOeaEWZwC82PuG0Zp00SNn8Wiit4qvYVc9nNjnsJsa76Cu9Sqq9DwTvF8SeI7V3Tp4M8dpeF25jrg4P9iP7eGjm-JiQ-eEneM4l84zDM7EvXwGTIRpYBCktUounzSOEO4xt62e1aSeP2nz1g-dCbwhvIv2FJBiiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b76139f2e.mp4?token=LDPefTE7nNPu-gjkqtKdnVgyYYdYB95UEX81jL95ARqcoUu6VksC0Fde4U--SctDDIXg1UYrLQg9JpR18R-Ohl4V92FLK525FViZtkUZec3JTUgmfS5qUoznnUohdeesk54NSBqbS0mAR0QX3WXWMZWy8qE2Ggte9cDGRCtNMnZV08Qtqll5-SLOeaEWZwC82PuG0Zp00SNn8Wiit4qvYVc9nNjnsJsa76Cu9Sqq9DwTvF8SeI7V3Tp4M8dpeF25jrg4P9iP7eGjm-JiQ-eEneM4l84zDM7EvXwGTIRpYBCktUounzSOEO4xt62e1aSeP2nz1g-dCbwhvIv2FJBiiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی نظم تردد ماشین‌ها به دلیل مسدود شدن مسیر راه که بیش‌ از ۹ میلیون بازدید خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/687487" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b3afd89d.mp4?token=I5v4D-TE2s-Mq3ybcF0Jr_2rdG2cToff0M5Y_D1jnjLskM3CI7HcsstD6hQu8k4ghSU0KfArtIni_rRDGxviYXwbegcZRGC7zl9H8RwJFLeqKZVij3CrVABZLR9JPwozh82nF6Mf2YgWvsGsABvu-vym_EsiL-1J1TpOV45nJickuP9Xd_cBTlep3ZvQ92mYXUg9_aeQ-1yZxZ1Xu6AVQTJOFya_b8HBauutLYMAmevs2mclBh8-3WbIRnofpsw9TQbro_RvFY1JcKJ8-Mbaoby_8BnEut7JBgHFod-6ZKP6Jr0-6SJnDsobS0ngDDlMJWERJGO80BJqOZMV32qYaL7-JrprU6YnhzY90FlI_uvJOWdMuRs_5PGXrpsLuK36jPGVni57k1TGWGI3lbm_36TNlxof4IPL7Dw9WaITLZykmarwfU9ICmaP9cEZukhmfhNnm_VOOKkc_FX7mXc-TTDQ88sZvJ-ULVbkEAPGi1pAE38RmeGrlhrks8jfNSfDLAEH58Dkfd4PaksSEjV6AeTsmjORlK_RQ6-Sc1oGh5hbm1PoFWTWjYxhFIJw0ISYJYn7io9qiDDbpifE6fBQGzzcO5qeRPQQyA0mYw_BUb-Coc-Ws8Xly4eBREdpTLsrdYW-g5fRd4kEvCzWvGadaZ9s5ccpYSYogSMCJYxL6wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b3afd89d.mp4?token=I5v4D-TE2s-Mq3ybcF0Jr_2rdG2cToff0M5Y_D1jnjLskM3CI7HcsstD6hQu8k4ghSU0KfArtIni_rRDGxviYXwbegcZRGC7zl9H8RwJFLeqKZVij3CrVABZLR9JPwozh82nF6Mf2YgWvsGsABvu-vym_EsiL-1J1TpOV45nJickuP9Xd_cBTlep3ZvQ92mYXUg9_aeQ-1yZxZ1Xu6AVQTJOFya_b8HBauutLYMAmevs2mclBh8-3WbIRnofpsw9TQbro_RvFY1JcKJ8-Mbaoby_8BnEut7JBgHFod-6ZKP6Jr0-6SJnDsobS0ngDDlMJWERJGO80BJqOZMV32qYaL7-JrprU6YnhzY90FlI_uvJOWdMuRs_5PGXrpsLuK36jPGVni57k1TGWGI3lbm_36TNlxof4IPL7Dw9WaITLZykmarwfU9ICmaP9cEZukhmfhNnm_VOOKkc_FX7mXc-TTDQ88sZvJ-ULVbkEAPGi1pAE38RmeGrlhrks8jfNSfDLAEH58Dkfd4PaksSEjV6AeTsmjORlK_RQ6-Sc1oGh5hbm1PoFWTWjYxhFIJw0ISYJYn7io9qiDDbpifE6fBQGzzcO5qeRPQQyA0mYw_BUb-Coc-Ws8Xly4eBREdpTLsrdYW-g5fRd4kEvCzWvGadaZ9s5ccpYSYogSMCJYxL6wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ ترفند کوچیک، کلی تفاوت در آشپزی!
🍳
#ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/687486" target="_blank">📅 20:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e045414.mp4?token=bHT6hlOci_Yt06xwuMWSncOwZK2D6OcILafD0wzCxC2-IIXgmqiI7kNxmqIfF0Q9u2mza20JR2hzDeFmlvscAtyH54L-EULSG1nef3UOEZFp5Vkl9ZGK60YEukITbN8CMzxAU7rtrHtFiZLLy0tpPBMONBrx8ArskoFm-N9dAG2g5gPZo7Sd9IK7Uf2uWT9S0I7zm1-qfiTV5VyFhV5Cz-YyTMhdyFN8UFfyWhtTdzW-Tcxt5vc5p4OKfqxitkfYp5wY-xQdZVs3AkrwLMhd4gJuJ6IL1iPG-iwCf2QPieO8WRO__oE_QJVwhZCnzoxFxFBawEwTf1Ct3CzQxItamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e045414.mp4?token=bHT6hlOci_Yt06xwuMWSncOwZK2D6OcILafD0wzCxC2-IIXgmqiI7kNxmqIfF0Q9u2mza20JR2hzDeFmlvscAtyH54L-EULSG1nef3UOEZFp5Vkl9ZGK60YEukITbN8CMzxAU7rtrHtFiZLLy0tpPBMONBrx8ArskoFm-N9dAG2g5gPZo7Sd9IK7Uf2uWT9S0I7zm1-qfiTV5VyFhV5Cz-YyTMhdyFN8UFfyWhtTdzW-Tcxt5vc5p4OKfqxitkfYp5wY-xQdZVs3AkrwLMhd4gJuJ6IL1iPG-iwCf2QPieO8WRO__oE_QJVwhZCnzoxFxFBawEwTf1Ct3CzQxItamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت اضطراری در نتانیا بعد از تیراندازی نظامی صهیونیست
🔹
به دنبال تیراندازی یکی از نظامیان ارتش صهیونیستی که در جنگ غزه شرکت کرده بود، نیروهای امنیتی صهیونیست وضعیت فوق العاده در این منطقه اعلام کردند.
🔹
رسانه‌های عبری گزارش دادند که این نظامی بعد از جنگ غزه، دچار اختلال روحی و روانی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/687484" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDD1Xvn4R5QPNTzlJvrGH8Zf3-VGcOPOXx4YLjMuuk347pwaX1uLyUVV2t6R7qD8hx1i4rx6sPWn-5isiqYZkbC6l_Wu7YPRGCF8yPDS6kc8eE3MzcQAzbj1r1Pri4o4Ck9CTDr_Thx7tZu1OTv2N-IGeDVxvDkJbGLYbuA6EfkglthqllP-0zfUh2TpKqgE21d8Hmvo2dZPqO4gU328SQu0N2bnrsjiUSCqM-4qv1XNX13S4vCIMj9VLyTwiKgwVADjL0CNe8-b8JH27mHM03qKX3K_Y11nCtyCEYAKz_6jooja7lgLAc-ZF2KqaRFnxGJE9SfUAr5D7cUQiGGm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛چالش های شروع سال تحصیلی
🔹
اگر برای شروع سال تحصیلی با مشکلاتی همچون  گرانی لوازم‌التحریر، لباس فرم، هزینه ثبت‌نام و ...  مواجه شده‌اید، تجربه خود را با ما در میان بگذارید.
🔸
روایت خود را در قالب ویس (حداکثر ۳۰ ثانیه) یا متن ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/687483" target="_blank">📅 20:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
دنیس راس، مذاکره‌کننده سابق آمریکا:  احتمالا ایران در مقطعی تنش را تشدید کند، اما این اقدام ممکن است همزمان با ارسال پیامی به میانجی‌ها برای تلاش جهت یافتن راهی برای خروج از این وضعیت باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/687482" target="_blank">📅 20:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687479">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عصبانیت هگزث از حملات ایران به ناوهای جنگی آمریکا
پیت هگزث،‌ وزیر جنگ آمریکا:
🔹
اگر ایران به کشتی‌های ما حمله کند، نفتکش‌هایش را نابود کرده و غرق می‌کنیم.
🔹
ما می‌توانیم تمامی نفتکش‌های ایران در دو منطقه سنتکام و اقیانوس آرام را هدف قرار دهیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/687479" target="_blank">📅 20:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687478">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">12 Ane Manaee (1404-01-25)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/687478" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه دوازدهم
حجت‌الاسلام امینی‌خواه:
🔹
شأن نزول "سوره قتال" در ابتدای شکل گیری جامعه اسلامی و اولین مواجهه نظامی با براندازان بیرونی [03:53]
🔹
"سوره محمد(ص) "، مانیفست مقاومت برای تحلیل فضای عاشورایی جامعه امروز [10:14]
🔹
"الهیات جنگ" یعنی، درک خطر موشکِ بدون تقوا و اقتدارِ بدون اعتقاد [18:22]
🔹
ترامپِ مشکل‌گشا و رهبریِ مشکل‌ساز!.. خطر نفوذِ نرم کوفی مآبان با پمپاژ شبهه در جامعه [20:16]
🔹
چالش استفاده‌ ابزاری از نام رهبری در خدمت اهداف برجامی! [38:53]
🔹
سوره محمد(ص)، نقشه راهبردیِ ورود به جنگ و پرهیز از جنگ [41:45]
🔹
انطباق با منطق رهبری، شرط لازم برای دستیابی به پیروزی [47:40]
🔹
فداکاری اهل‌بیت علیهم‌السلام برای حفظ "ظاهر دین" به قیمت“ گشاد بودن پیراهن خلافت” بر تن غاصب [01:04:05]
🔹
خطر بی‌ثباتیِ ناشی از بی‌دولتی، یکی از تهدیدهای جدی برای جمهوری اسلامی [01:12:36]
🔹
تحلیلی بر تفاوت‌های تفسیری تسنیم و المیزان، از توجه ویژه به شأن نزول، تا تمرکز بیشتر بر تحلیل عقلی- فلسفی [01:19:31]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/687478" target="_blank">📅 20:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de28e29cb.mp4?token=ML1qOobRtqBY2vbQlNxwORyAfhXA9k2rxXJjC6d19saLK0VX2fEn9yXnbfiMkbmcg4BJu8A-Ts1oedXwJPhpErg-17YqzkOibF5i1PdDQa7JaUW6Yu0sPfspn7DZskqt1jY75xUpB3GYyRt9EqkcQnAmZRHKSqq9DHZNzkPPNjMKRQAEHQiSNBuInvkclUzGfOUF1aqJZ4HFzp7NIRJJNUs7x4-ziA1bazUFND60gh2LDYJmyjaD-dXOwyoYURbQ0INOgczNDDpAdiSMTjhvQdXOOBwVuO-greriiSRDnInJDfHCRlymMW4y5ccOEPRdMfFC5hqRCLsH_L1KgN7GHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de28e29cb.mp4?token=ML1qOobRtqBY2vbQlNxwORyAfhXA9k2rxXJjC6d19saLK0VX2fEn9yXnbfiMkbmcg4BJu8A-Ts1oedXwJPhpErg-17YqzkOibF5i1PdDQa7JaUW6Yu0sPfspn7DZskqt1jY75xUpB3GYyRt9EqkcQnAmZRHKSqq9DHZNzkPPNjMKRQAEHQiSNBuInvkclUzGfOUF1aqJZ4HFzp7NIRJJNUs7x4-ziA1bazUFND60gh2LDYJmyjaD-dXOwyoYURbQ0INOgczNDDpAdiSMTjhvQdXOOBwVuO-greriiSRDnInJDfHCRlymMW4y5ccOEPRdMfFC5hqRCLsH_L1KgN7GHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزشی ۳۰ ثانیه‌ای که به اندازه یک عمر ارزش دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/687476" target="_blank">📅 20:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFfRBl8FyyVsJu2_1vszXGAKAHSGLUyA97Jm9-gt4oZCCp9DS-T6R9mZkkqFAMOqtqKJKTjv0c6m08oVcfXrsv5-bjEQA9Dqqu9YOet7QZqiB-D7AGgHMs_eVejndTeqrS1yR59UCo6jIxbP0q-mP1VzeuUk6KdjrP9o0GWF1eOjZGxthSXt4aluV9h1fxO5VMA9ZMw_ie4p3j8N1kEEN_c_QZ0CrGRI5jckltRt8wfY92F-KLIf0YGhmXCBkqmlDm6ZpnSz-tfq4AqeeCLG-6CS0ap0rlTBFrHM4uieGf6pw4xDpMlnCNNLgOPrLZNbIJKm3_KSZkZQyTvSM5aYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهدای یک سال اینترنت رایگان به خریداران مودم 5G در آمل
🔹
پس از پوشش سراسری نسل پنجم اینترنت همراه اول در آمل، ۵ نفر از مشترکانی که تا ۳۱ مهر ۱۴۰۵ اقدام به خرید و فعال‌سازی مودم‌های 5G در این شهر کنند، یک سال اینترنت رایگان دریافت می‌کنند.
🔹
این طرح با هدف آشنایی بیشتر شهروندان با قابلیت‌های نسل پنجم و افزایش استفاده عملی از زیرساخت تازه توسعه‌یافته در آمل اجرا می‌شود. خرید و فعال‌سازی از طریق مراکز فروش و خدمات همراه اول در آمل یا فروشگاه اینترنتی به آدرس
shop.mci.ir
امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/687475" target="_blank">📅 20:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163c87db5.mp4?token=PLZvjU9tY9-byaZfG2RHfFgAXLxt4ZWZUE5IsTM8kWlkMPi3YZz2s2nyEd0k7k7orpdOT5f9Wen22_zGrb2_ve8caVnHetF3H72BerHhQ4a7RLQ-4iXZQHgk5NfiarraYEbKNikvVabRF8YpVrADV2uPyVhZz2bgWkLc2-JXZK2pEL6BQzptQasauz9LWKt21DzN2tk38ue9nc46uYCZXF08Yhsv-55F7rfCkcjUA0prl4LvUnQYbKWGbMRDZPAdr_4Ib8JEI7g72lPI2RG1W_NME4lwk07M0PLNlz5FpeCgVDKCGfuuprqoppBl6d2Jy4Blguwl9eO-D1mH0V858w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163c87db5.mp4?token=PLZvjU9tY9-byaZfG2RHfFgAXLxt4ZWZUE5IsTM8kWlkMPi3YZz2s2nyEd0k7k7orpdOT5f9Wen22_zGrb2_ve8caVnHetF3H72BerHhQ4a7RLQ-4iXZQHgk5NfiarraYEbKNikvVabRF8YpVrADV2uPyVhZz2bgWkLc2-JXZK2pEL6BQzptQasauz9LWKt21DzN2tk38ue9nc46uYCZXF08Yhsv-55F7rfCkcjUA0prl4LvUnQYbKWGbMRDZPAdr_4Ib8JEI7g72lPI2RG1W_NME4lwk07M0PLNlz5FpeCgVDKCGfuuprqoppBl6d2Jy4Blguwl9eO-D1mH0V858w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: زمستان سختی نخواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/687472" target="_blank">📅 19:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687470">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvrYoy6FjQ57oXXKLbEySC3bFJaXeNjBDSSW1_yi3qRsoYRFBk8ge63NEaC5J12Orq6DGnV_Z7IcKcKohAQ7UbFk-yd-QcrCpUUu5LlFAOXPf_kRUOS9uWx7xroqB1jotzhVghWEebxLPSAM9CtjeS0g_kgn-Y7D8Gan96rormw7KnW8LpYfFPuE0MCrm8w6bcC1efHTSsnxfF2SlVU3i3SeNdvkH911Rw9Q0__hJ6BTbdCC8F2ohMxLXLais3SYPPsq9-NF5a3O7ifjzFMhpNKUDW_8OU7DudbqsOPtVQPLtmU3oEzJVATNDy8TW5yTPF7mbZvwVh1755mptwx1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس «بارگاه امیرالمؤمنین (ع)»
این تندیس، فقط یک المان دکور نیست؛
روایتی‌ست از شکوه حرم و آرامشی که از آنِ دل‌های مشتاق است.
✨
مشخصات محصول:
▫️
ابعاد: ۲۰ × ۱۶.۵ × ۱۴ سانتی‌متر
▫️
متریال: سنگ مصنوعی
▫️
وزن: ۹۴۵ گرم
▫️
طراحی باکیفیت و باجزئیات
▫️
مناسب دکور منزل، محل کار و فضای معنوی
💰
قیمت: 5,198,000
قیمت با تخفیف ویژه: 4,995,000 تومان
⏳
موجودی محدود؛
برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687470" target="_blank">📅 19:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687469">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5487963f.mp4?token=O-OXqZGOh2a6jn7xzT_OxHjprwS6c_-L-Rgrf5qEGjMIOkBY8WsiTwww50DpaF6esa9UzN_8HqUTwjk-4iflijsi08uPr0E0ZQvwUJPeIv7YLGYxMVlSs-HE2P1Yq1QzsereNaV1S6ebVRkJCJ8RKdAhia7Tck5cxmW1LwsmtjBW0-HPPfS-OyrA2E3eyzVgMGXFQU9yptXVLDNY3e7TtfBtsjFIiQUljU4wxvyTHWicoEC3wNJaAeYuM9Qq0h9FjYsPb4jAMM84jIj5XIPGe3wRKjlwfnR9XnIrH4Cnet2U43VTa9cT_1Kqu48GNiC6nH07Ftdtuxi3IVTQk-sqtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5487963f.mp4?token=O-OXqZGOh2a6jn7xzT_OxHjprwS6c_-L-Rgrf5qEGjMIOkBY8WsiTwww50DpaF6esa9UzN_8HqUTwjk-4iflijsi08uPr0E0ZQvwUJPeIv7YLGYxMVlSs-HE2P1Yq1QzsereNaV1S6ebVRkJCJ8RKdAhia7Tck5cxmW1LwsmtjBW0-HPPfS-OyrA2E3eyzVgMGXFQU9yptXVLDNY3e7TtfBtsjFIiQUljU4wxvyTHWicoEC3wNJaAeYuM9Qq0h9FjYsPb4jAMM84jIj5XIPGe3wRKjlwfnR9XnIrH4Cnet2U43VTa9cT_1Kqu48GNiC6nH07Ftdtuxi3IVTQk-sqtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: دیگر قطعی برق برنامه‌ریزی شده نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/687469" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687468">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
جان باختن ۲ خلبان اف۴ در یونان
🔹
خبرگزاری رویترز به نقل از مقامات خبر داد که در پی سقوط جنگنده آمریکایی متعلق به ارتش یونان، روز شنبه هر دو خلبان جنگنده جان خود را از دست دادند.
🔹
این حادثه در خلالِ نمایش هوایی در پایگاه تاناگرا در شمال آتن رخ داد و جنگنده در فاصله حدود دو کیلومتریِ فرودگاه سقوط کرده است. گزارشی از مجروحیت عابران یا ساکنان منطقه دریافت نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/687468" target="_blank">📅 19:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687467">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
هانتر بایدن: ارسال تسلیحات به اسرائیل اشتباه بود
🔹
هانتر بایدن در پاسخ به سوالات مهدی حسن، روزنامه‌نگار انگلیسی، اعتراف کرد که تصمیم جو بایدن برای ارسال تسلیحات به اسرائیل اشتباه بود، سلاح‌هایی که برای نسل‌کشی در غزه استفاده شد.
🔹
جو بایدن از دوران سناتوری تا پایان دوره ریاست‌جمهوری خود، یکی از حامیان بزرگ رژیم صهیونیستی در آمریکا محسوب می‌شد و از معدود سیاستمداران غیریهودی در آمریکا بود که علناً خود را «صهیونیست» معرفی می‌کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/687467" target="_blank">📅 19:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687466">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای فاکس نیوز: نیروهای آمریکایی پس از آنکه ایران به دو کشتی جنگی آمریکا موشک شلیک کرد، سه نفتکش ایرانی را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/687466" target="_blank">📅 19:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXuvTbL9tTKkKpe7WtuZKegwFYOiZDKyVKvU93w8DfrnUbnPOP2oSOn5-pCZD0fvwITZ0mhn7xWIKaAZHbi9OnAzS8tnAPg7m0QgvfkyQAmLUgP45pQBi_ukZV9XogvgUumxnGXzrj0fAFPcFGT9nUFVImuKHrWumpzUYmnrQgZQ5tmTV6GwocddeZ_mlqLVQtoqzjxs-zKe70KNcaWTbpdwr2bXpDQWoP5X4LiUiS7Xqqldl60xyB3HoTucdxg6nwhFC2fSyoB4r9T6hI-B26qzs_juuvrmK3fF9Oe1nSawCf5Zg5o4u4xY96SBedqVkHlLav9bKfggWpE3x7Gd2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoNrQyBm15tyTcek5Q6rpqJCZ-FHZE0Pd7MGlLSyNUaB3CC5KOVWoTUbx-i0IWErm67-uR38q7ceHieJfwsh1NgsAxiTZFI0xXatdFl0oKzFww0BrwTB0DSYWP166aexJ3HLBY6m6ZQEE-BGWSfJXX9dj8tWbWFg47K3sBc1rxSV2NqQfljIwzwy29z9wfX1t6ZjsAWju1R3nrOaKtueM4INr7hpEKmW3ku6OGfTkK8BVtgxKWvcf5cMhZ8cgRlcS8cHuaFykoP_JYczpL9qH29LzupzI5vDoGV6f0NOUJ_CwJZMnsdP3TaIJ-8KBtLCuezLTWjbujtMuIcQBJrovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1Wi_BYBdw5EMJdifQ6oXDe1ZvxRBwUvZ0XuYQPcNG29ihg7geQWyAIE9nDUOx7mjJc5wV3wK_libd0FIxaC8WT3ttSj4L2R2GwSG_fRckv7GRWzFLKm1ZxVzDvOhehylOrw43I8fF6lOxJlHOyg2Efa3nmZPXxB_OvepTMGmC6khpL2wvWwMYJhhdvC9zC1SNBgRrM25UMJWQ7cOLiUc2RKVC6U76j42EJkBs0AWfmSS4y-L6rdWLoLIjchpRDzinSGFjJD-Cd6-AZhrGPlMjzBNR694DECXTVr-3Z7AyZ-az-hPNSHZS9P7rnnjCNUD3j1Gea5iMlKuLjWjW4-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7taUyfNYNXt_KVO26VkVFwQKSP6uyOAjy1U_6Tg7NXP5ihZg4_mV43nNbxq0fkyBN6AkicWIDjXxauYd72Ti43CfSIXge4zUibF9dk-TJY86doAQHEe68bvRpJIQgAZUCQCp7uDkzsUOPXaS9YaV8HfI43b_P7PFHybjHh1lHUfNk4sfV_QtasE0fNJ-dbXPxk2Es_OIqJUCxNbpRSMZLvVDOReI2qZdCkwbiKqL5SBu3FE6LsEsFSDdMW_AM_TG_TpN1khZZa9yWMlKSP6fdUX0qM_V5xYFcJePib-XxTd7X2QEP1rA34v6eoIgBxozPEEq5iYmYY0KrQvaMTYEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
«تابان فردا» وارد بورس شد؛ هلدینگی با سهام ۸ غول نفت و پتروشیمی ایران
درباره‌ تابان فردا بیشتر بدانید:
🔹
تابان فردا با سرمایه‌گذاری در زنجیره نفت، گاز و پتروشیمی وارد بورس تهران شد.
🔹
بیش از ۸۹ درصد از مالکیت تابان فردا در اختیار شرکت سرمایه‌گذاری اهداف است.
🔹
خالص ارزش روز دارایی‌های تابان فردا حدود ۹۶۰ هزار میلیارد تومان برآورد شده است.
🔹
تابان فردا امسال ۲۵ همت سود محقق کرده و برای سال ۱۴۰۹ چشم‌انداز ۳۲۱ همتی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/687462" target="_blank">📅 19:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صولت مرتضوی: اساساً میدان رقابت‌های انتخاباتی میدان وعده و وعید بوده است
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبر‌فوری:
🔹
اساسا داوطلبان و نامزدها در انتخابات طوری برخورد می‌کنند که اساسا تمام گذشته را زیرسوال می‌برند و این اغواگری است.
🔹
آن‌ کس که فراتر از توان اقتصاد و ظرفیت کشور وعده می‌دهد، قطعا وعده‌اش دروغ است.
🔹
اگر کسی وعده بیخود داد و نخواست وعده‌اش را عملیاتی کند، لیاقت و شایستگی این مسند را ندارد و مجلس باید حتما برخورد کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/687461" target="_blank">📅 19:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687460">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حادثه دریایی در شمال خلیج فارس و دریای عمان
سازمان عملیات تجارت دریایی انگلیس:
🔹
گزارشی از حادثه دریایی در شمال خلیج فارس و دریای عمان شامل چند کشتی تجاری دریافت کردیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/687460" target="_blank">📅 19:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687459">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4010eaa.mp4?token=n8NK-w09nWy70HLf7zOJ0N65FxWn9RZFeT6C24tUSjisGmlzXA3_BwrxLuYXFdFhiNcChKOD47TtUbrlhVG7Y56IbtzCNqrtH1mnUezR-2q9DkABIbpxCkn0YK3MPK6huU0hJBDzwD3-e4dHDhXFx8Cx5TK1l5ze5EURrWWBjmZ0GuZPX3YH_qIUS24BHZumYMJ0aaOrmb8nAy_rWL0EpoR7k8ouFN4GshFGCxi2XUPksS3s0NyuBTIAHceQCUfvU01De2rYwiN1a7BPpX0y4jNACpZRBQnqIi5xSKjJYvAyThERBTXhh6fQVOtDLRCiHMWJUt2cgXMNk3Iz8baKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4010eaa.mp4?token=n8NK-w09nWy70HLf7zOJ0N65FxWn9RZFeT6C24tUSjisGmlzXA3_BwrxLuYXFdFhiNcChKOD47TtUbrlhVG7Y56IbtzCNqrtH1mnUezR-2q9DkABIbpxCkn0YK3MPK6huU0hJBDzwD3-e4dHDhXFx8Cx5TK1l5ze5EURrWWBjmZ0GuZPX3YH_qIUS24BHZumYMJ0aaOrmb8nAy_rWL0EpoR7k8ouFN4GshFGCxi2XUPksS3s0NyuBTIAHceQCUfvU01De2rYwiN1a7BPpX0y4jNACpZRBQnqIi5xSKjJYvAyThERBTXhh6fQVOtDLRCiHMWJUt2cgXMNk3Iz8baKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار تانکر سوخت و جان‌باختن ۱۰ نفر در ورودی سنندج
رئیس اورژانس کردستان:
🔹
درپی وقوع یک حادثه رانندگی منجر به انفجار تانکر سوخت در محور سنندج - همدان، ۱۰ نفر جان باختند.
🔹
عملیات امداد و نجات و پاکسازی محل حادثه همچنان با حضور نیروهای امدادی و آتش‌نشانی ادامه دارد.
#اخبار_کردستان
در فضای مجازی
👇
@Akhbarkordestan</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/687459" target="_blank">📅 19:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687458">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال:
۲۰۲۶ به «سال از دست‌رفته» اقتصاد خلیج فارس تبدیل شد
🔹
امید به بهبود شرایط اقتصادی در سال ۲۰۲۶ عملاً از بین رفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/687458" target="_blank">📅 19:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687457">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksUMoQuPyKTux1iQqnm3jMqGlqM7bOXPGju71ajm0mlHXrzpKKovdNkkjtHt_DBw7GJNHr1_p4dtcTekfYbl0sOUZenRGTogYgNpOpM1lyLvnLo-uTF1_Vq0I3blo3Ur1PhvLIwjX5PIAmErV7i6xPiVbgBGGHISHvgkEqXNEyKEgukpI2ggbWaez68hG80bhqLki2t3GOlPnaVFL5Fd5YDyLzUDjVmEg34DRdz1SnEZrse9WRG1vtk11owYjIDjgll9-XzUp-torWpDdbFVLq9uWRZ2kxO7owRTx6qiW4MsV5497uo6nh2BWipbZIinEw_FuQRcGN_U3fc8RS8TGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز پرقدرت
#اسکورت
روی پرده سینماها با فروش ۶.۵ میلیاردی و همراهی ۳۵ هزار مخاطب
🔹
«
اسکورت
»، پدیده‌ی جشنواره فجر پس از سه روز اکران و همراهی ۳۵ هزار تماشاگر، در میان افتتاحیه‌های پرفروش سال قرار گرفت و پیش‌بینی می‌شود این موجِ استقبال روز‌به‌روز گسترده‌تر شود.
🔹
با نقش آفرینی:
امیر جدیدی، هدی زین‌العابدین، افشین هاشمی، مهدی زمین‌پرداز، هادی شیخ‌الاسلامی و با هنرمندی رضا کیانیان
پخش و تبلیغات این فیلم را،
شهرفرنگ
برعهده دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/687457" target="_blank">📅 19:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687456">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b18bebc9.mp4?token=MztnwxwC9cyeXq-CiY1myW4-Gaq5XnFvxkkNoap3xEI4C-pYe3hs4YvjHipW3uMC12AWJLz1HoOZ_dLAD-qPgt8F3q5RkbczOlwx6wL-aYG4b728-8km3D_QsPOZagtMM9Xd2qSeZPd6VV3SwBCUede8Myjs5PHInhiThxq9rmdbgErmMw29XrKv6I_sMk4CeXhCihs8thAzDS-stCrleKWT1r1l9Qxe1fB794V7HG7Q1YJHkElq-saxZlegypOeYlJn0gKZDQtDeE9zULg75_9J9u4bRRnvQiusqphTZgMFGIpe9OivdsII8SvoQWLrYoIfJEnBdgr4aPNsSwJOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b18bebc9.mp4?token=MztnwxwC9cyeXq-CiY1myW4-Gaq5XnFvxkkNoap3xEI4C-pYe3hs4YvjHipW3uMC12AWJLz1HoOZ_dLAD-qPgt8F3q5RkbczOlwx6wL-aYG4b728-8km3D_QsPOZagtMM9Xd2qSeZPd6VV3SwBCUede8Myjs5PHInhiThxq9rmdbgErmMw29XrKv6I_sMk4CeXhCihs8thAzDS-stCrleKWT1r1l9Qxe1fB794V7HG7Q1YJHkElq-saxZlegypOeYlJn0gKZDQtDeE9zULg75_9J9u4bRRnvQiusqphTZgMFGIpe9OivdsII8SvoQWLrYoIfJEnBdgr4aPNsSwJOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد شدید نماینده کنگره از دولت ترامپ: مراسم عروسی در ایران را بمباران می‌کنید و یک پسربچه‌ی شش‌ساله و چهار عضو خانواده‌اش را می‌کشید/ زودتر این جنگ غیر قانونی را تمام کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/687456" target="_blank">📅 19:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687455">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
گزافه‌گویی فرمانده سنتکام علیه ناوگان نفتکش‌های ایران
🔹
دریادار «برد کوپر» فرمانده سازمان تروریستی سنتکام در سخنانی خلاف قوانین بین‌المللی گفت که در صورت لزوم، ناوگان نفتی ایران را نابود خواهد کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/687455" target="_blank">📅 19:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687454">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2293727863.mp4?token=M15XXwdiMuSmkW4Dhyhvmmx3N5Xg7R3dY0CXNR5V1UzhlWjWRwr8A5uZfW7BQ-hqlKvA79eAjzgFRVaWVIweF7VGFQu0lu4WJtMAKEIXwEPPbSct2F9YbrHORz_snJmEDvJ62IL8vzuv70mNlDcRYH0lpDT9wztAh7fDF3z8IYkSSSWmSHvdz6xji4fVyoe-_keQ3uXJti1Z8uyhx_u6ThVSEsb5gSYsgaEbPsPC0V9LHxC2eVFz4JCzeZMX_9gt7Ui_br7PtE2SVxp8h-1Xo2C1JXBEfNDgrmLqzU8cKcV_LLmV3XUS6pvoQuSNb2Da6sEtkR5LkJrwcmeoqwMmhi6A9BZoy5v5YIf248BxpGO8QAytNYm8UU_TBSAqDx3iXR_ReP54zgVeT2fOr9hJjNUbBpOhxCZaxGwgQ1SeGy457z79HZfllqBrd-cPspjNDop9fpQ1LCkZTI7kwdKBxXS5kyspH94zy2L7VPATt57wJMhjr5RxVrlUbq0PRuFV4lpq2OkLUtrEPe3ojPyS9ffGLps6JTSxn3XV-7dvKiVq9iAfw_uFN-RK8fAS6zrV4I3ErRdjBFLID0WIvs5AkdQKPaCUE7Uzltu7TUgP4SKnJIO-J5esF_VIJJA046BgbRYPU7O0Uep2JyhkpDhfn22rS7BZCGFsE7bVj3DUkIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2293727863.mp4?token=M15XXwdiMuSmkW4Dhyhvmmx3N5Xg7R3dY0CXNR5V1UzhlWjWRwr8A5uZfW7BQ-hqlKvA79eAjzgFRVaWVIweF7VGFQu0lu4WJtMAKEIXwEPPbSct2F9YbrHORz_snJmEDvJ62IL8vzuv70mNlDcRYH0lpDT9wztAh7fDF3z8IYkSSSWmSHvdz6xji4fVyoe-_keQ3uXJti1Z8uyhx_u6ThVSEsb5gSYsgaEbPsPC0V9LHxC2eVFz4JCzeZMX_9gt7Ui_br7PtE2SVxp8h-1Xo2C1JXBEfNDgrmLqzU8cKcV_LLmV3XUS6pvoQuSNb2Da6sEtkR5LkJrwcmeoqwMmhi6A9BZoy5v5YIf248BxpGO8QAytNYm8UU_TBSAqDx3iXR_ReP54zgVeT2fOr9hJjNUbBpOhxCZaxGwgQ1SeGy457z79HZfllqBrd-cPspjNDop9fpQ1LCkZTI7kwdKBxXS5kyspH94zy2L7VPATt57wJMhjr5RxVrlUbq0PRuFV4lpq2OkLUtrEPe3ojPyS9ffGLps6JTSxn3XV-7dvKiVq9iAfw_uFN-RK8fAS6zrV4I3ErRdjBFLID0WIvs5AkdQKPaCUE7Uzltu7TUgP4SKnJIO-J5esF_VIJJA046BgbRYPU7O0Uep2JyhkpDhfn22rS7BZCGFsE7bVj3DUkIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: در مدارس دولتی هیچ مدیری حق دریافت شهریه هنگام ثبت‌نام را ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/687454" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687453">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593d9a8f06.mp4?token=WVePxenTtgBCCg9V8wCDaPsogw8-AjSex7ZBXotgpMHEs_bhrX5gU0ke6Qb7KZmwCJ1prSBLDlK81Qvejf_0xOueNFrsS4fwTnmF1I6lVddJil4hCpHtREqIAFfYOMB3MDINPBLKvaK5VJTLpEkmEbpi9XKT9aV8WBc0I9kHywnYPjw1LHRtY9QAQdowgv0josgNgJvkwtld_Vs8_MGiQorbsAcCDLAKRajrbjETH6vVA8XG5mC9yKTh6bCRy5LjjWP87iAHAhq1AFq4PsAOvwZLuC3O2U4pvxGr4LINjM0vv-vqxM_q6X_j-T0uNFy92tTtftaH7aiW9n1SmmdOFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593d9a8f06.mp4?token=WVePxenTtgBCCg9V8wCDaPsogw8-AjSex7ZBXotgpMHEs_bhrX5gU0ke6Qb7KZmwCJ1prSBLDlK81Qvejf_0xOueNFrsS4fwTnmF1I6lVddJil4hCpHtREqIAFfYOMB3MDINPBLKvaK5VJTLpEkmEbpi9XKT9aV8WBc0I9kHywnYPjw1LHRtY9QAQdowgv0josgNgJvkwtld_Vs8_MGiQorbsAcCDLAKRajrbjETH6vVA8XG5mC9yKTh6bCRy5LjjWP87iAHAhq1AFq4PsAOvwZLuC3O2U4pvxGr4LINjM0vv-vqxM_q6X_j-T0uNFy92tTtftaH7aiW9n1SmmdOFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه حمله آمریکا به تأسیسات هسته‌ای ایران در قسمت جدید سریال سیلو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/687453" target="_blank">📅 18:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687446">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPBYPObdzCLBl9rDIboO0dOR5Y5Yt33xWi1YBwo2UdVLe149cBWkZiD0jmH6tzpOoi1qXYeM24gauskQCmOc8wSViXumKPkKSyefapBjI62ugMSxtZsTIWHHM_c0M9R4FOK-UjF-aVko5nArrhw9ASHVC6hFpTJsZ5jnI1vu2P0uiXOkhfYBUfuny8vpzcke4Boj5uP-REEBUeFBvwxNq5mFmsvkRLtDH-wNLYXWnLPW_fcMcfpYRpzLy8J5Is34ry9B_5XrO1_chC-ZXnqTTl2M6_84hQqCFjyqm3cHX2vR8p7S9t9-tAe-b5CexnIgSodeY4VwruNVnaqTR6l-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SP9DxbXe8uXVe_-YLwM9OnR0VNTHV64dNgmlNA8m5-3Wu0YBXS8QTDiqGNLMccUdh23jOdYxzCVH9_JEOMOPv2Zm0alyQPCihn7S8xhPZdvY3rOKYisR-CVFsMpCuhjMucyiPWQ896fujjTyFhER9gs4Br0BJRQ3l2Fr6ORPBKHGfucA3GwrFyQGI5-MFOSgx4H7HuUkMwZcWf2Uq2OpetIhPfIBRLtEhuYBNSNrF8RGVmvVflp6GQnK_fovpUMp7V4TGOuOHBDyQqTd0qm_trWNHDlmGHabNlJBwrJP0rioHdjDmqcVFwzPpVVi2wMKnUvZvXegv-Ax5J7X39793Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8o56VYDC1WaH4dECWvjjFWwrGea2UcSsBr--a2qb8cbg4HlYiTISFcQMwIrsxNcXZ2iXub4CmBmb6jeAVU381WJx7_Bgv0zccVzRf_1xQB4rmNL2dUjGc7qrgb39gsENY5o_iSXggfB1QwVNrX5y5JOAxvT3eu52kwDZvkHZFy30XzQcFB_ZffuFphlG-evq8LxEaW_gMhV-3N8TK35ZyYnm1b5IDAdKGoXK4I9YKPNXH24oCsXZgwvDmgeRFmMF3k5Qhu5lXUzTiQqi69ZwdhgzrHOC7MW7Xrg8YBDMAVgwITrDugzN6d5jN57MVjyBYpmUcW32EASxhjKHCaMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWgQPm2_hgwtw4VcNaI-mPV0xzOvUQ1XllKIczt6W6SBJv4iFpzoehIEFx1H2TLjRYmbb_oUfR5URFFvhXTnEiO7dqZVfFwYQZ2Go8l_hoXHht2YEBCVevykMipydqubateKa2_FLX62kCpz1xqFbzj_daaBxPtZrVI0orG--sUhM5AKcpshApq-yPe5SULicwfsVL5X9wqBMfmrz60z0IHu8KP2a6wp6uxsmLwQ-ztr8mmAqDD-GnYnJkuQPvwgx2_d-XlAUimVup-vVK-4E5COl3TAY45Eju-5aiDflFzyb3PUOqYQaWNTdAMkxMVOiZ5ODmR_Cq1RKcZ_E4gNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADHZICdNjUkMKALZytwSiUGjCY7AwoSakxxNQIgkp5TJ2kU6NDhm0-bH_WID2g-v-7ob_oPzynLlhGohjHOWWI35phIKTDK5yBG8R3lbAYUsKCbRo-cuvS7i1V_UyStjV0NImsadQhD4izxM_vd058sBdD5v3-KQHM8EyZ7fQWpPrpBYqQkUx7KXLzm_4mgXGllhcNMxlLBHVQwkKfyJ6LAZxmGNzqoqIYgL9aMJZVF4FaI8a9ZfIeM5pJw-71iQdrD_PYf6hdDCmyJa6Ejq5DoQFvAJJDYzXV0avWgs1jDjiG4xnJNguVBb0yLELzSksM1lFewnAxXN1YtcapTIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxJNGUqKWyLI-CYlwsnk4BrHscjAfssYaHVBOwCKGAUr4NfSgTaO-JO-eRul0Oaosh8_kuBOt5cv0ZzEuWJGufJv_JW_sY91wV8tzj7T8Xj23gtaQcOqveoUEVh5zkDjNUQYvPRJmeN2HpQesl4gq6AvbFFqYd7uQG10nBLy-3xwQgF032DS42N2aNTfJ32Fl6Zn0HHRKucW6AnShB71qzk2HnFQGa4xYLc_nr_mgIL-KM23B5YmOkZ3tmrvZcZB2BELUlVCl5GaMo3YhwI89h31HJ7w-fT5KRlJuyMzQKDTYXeUcPkQWegBfYO5LpejbpZNeQU6HZBf9d5F_LCWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWc4WC62UbKwnCT5dpKFGZCv6x3yWwoP9gHaDxQXmjBKbp7KJ5v7Ytnw6vuM4QMYsPf--XsbOAYMSQ-Mk1IU6FIWvDbkxwMQHUzQEu_RhOUdKBU3WYplmUQD8ueMqzMY_IHGzG5vKZcpOPzPvS7Xirl6qJqbFYdEqIPQDUqokAgpBK4FBah8zva9AQCCkvIut2WwEW29bdsUs1TWUS67xeG6M7NwNHxtPCZCz68RkWS5l25T91UP6-KOYrfX-6PNsNxD7NvIB_2HpqGBDk8_H_F6F7D4Odt0GLtlU0Br5pTQb3fhK_EyH6946xDm70uDjJEpV_qEzZBCdkT9puqS6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
در آستانه هفتاد و پنجمین سال فعالیت بانک صادرات ایران
🏛
موزه بانک صادرات ایران افتتاح شد
🔹
موزه بانک صادرات ایران با هدف حفظ و معرفی میراث تاریخی و فرهنگی بیش از ۷ دهه خدمت‌رسانی در پی برگزاری آئین رونمایی افتتاح شد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#موزه
#روابط_عمومی
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/687446" target="_blank">📅 18:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687445">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
پوتین دستور توقف حملات به اوکراین را صادر کرد
🔹
به‌مدت سه روز هیچ حمله‌ای به کی‌یف انجام نشود؛ این تصمیم در چارچوب مقدمات سفر هیئت آمریکایی اتخاذ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/687445" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687444">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهای آمریکایی سه نفتکش نفت خام ایران را هدف قرار دادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/687444" target="_blank">📅 18:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687443">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ساعت کاری ادارات تغییر نکرد
🔹
با ابلاغ رئیس سازمان اداری و استخدامی، ساعت کاری فعلی تا پایان تابستان باقی خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/687443" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687442">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCvmwXvUF8jXu9kCG5rBD31aMfRPFaeoV_2BR-k6K-AmKIdsddn65RVLizXNS1g48pix-U0S_imbZ0KidO_jAIISUNE7vuyvz2zUlIwBcXVFPaWYCXdpOeHZr5Bz3nZSageonzu85eIy3asuHTmbr9N8X98xs0uo5eHDQxwG9jL2qwEsrZw6tEtrgmAMaPhWASW3aUnyue-3QpzTodzWd6SIx7CnkbKXBPFz86iMgjT-bPbH27wbMt5WCSieY3fDSr5dcvjkrPyraj5HwQ3GzOYsNsOLYVYqPubwf6ovOeWj5XBS8FfnQ9dUA2C1MY-QHlpYCEgsmtiEHUp55pM_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاروان زندگی به شهر زنجان رسید
🔹
همه باهم برای ایرانی قوی
💪
🔹
همه دعوتید به رویداد کاروان زندگی،تجربه‌ای نو
🙏
🔹
با محوریت موسسه فرهنگی هنری تبیان(پرسان)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/687442" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687441">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه: اعضای گروه ۲۰ خواستار پایان جنگ آمریکا علیه ایران هستند.
🔹
نتانیاهو: هیچ بازسازی در غزه انجام نخواهد شد.
🔹
زلنسکی: آماده‌ایم تا ۳ روز از انجام حملات به مسکو خودداری کنیم؛ انتظار داریم روس‌ها نیز از حمله به کی‌یف خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/687441" target="_blank">📅 18:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تصویر ادعایی سنتکام از هدف قرار دادن ۳ نفتکش ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/687440" target="_blank">📅 18:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cdd869e8.mp4?token=f07rO0eXtykZz_9nUeNi-UOFxyKnmL5tEUGKhiCLjQWVLO3qE2wbgcDdQC3LGnGBxhu7uTrE7TTyavVaJ59dQUm1-wvz45vDTJeBwlWy1BEB2dmZ5HwbXmkLJIIiPEMs6CUiGlFoATNAcBR1m6LKPdFWxcZrQAOzqBxAr3sl64W-kohjlyb2TM30RJeHTKCnjcL9BoYMuIow5_QVQyMa36JDOyTREhFhKFGXKlDbWzo_lGdkiBNVRjQQh6JX-jvX9e7mGtvF_WK7QcMA_6QTVirTY2VMCCgHVvpFyMOIfxefxr03U2twGlcbcXGPc8WqiFrpQGVOxyM0S9XZI95rIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cdd869e8.mp4?token=f07rO0eXtykZz_9nUeNi-UOFxyKnmL5tEUGKhiCLjQWVLO3qE2wbgcDdQC3LGnGBxhu7uTrE7TTyavVaJ59dQUm1-wvz45vDTJeBwlWy1BEB2dmZ5HwbXmkLJIIiPEMs6CUiGlFoATNAcBR1m6LKPdFWxcZrQAOzqBxAr3sl64W-kohjlyb2TM30RJeHTKCnjcL9BoYMuIow5_QVQyMa36JDOyTREhFhKFGXKlDbWzo_lGdkiBNVRjQQh6JX-jvX9e7mGtvF_WK7QcMA_6QTVirTY2VMCCgHVvpFyMOIfxefxr03U2twGlcbcXGPc8WqiFrpQGVOxyM0S9XZI95rIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی ساده و کاربردی میوه‌ها رو به انگلیسی یاد بگیر و کم‌کم دایره‌لغاتت‌ ‌رو گسترش بده #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/687439" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687438">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f07a869d6.mp4?token=qTkRWkTAxsggKJ8emb_eCgJziCkFwcSG1KvIF7ioQ059nPe_CguZg42rKwChLpgoqZCIgRJO_qLlakQN3IIXpkuCAxT5czD6ixn1NnRctZOYRSUz7MfdaXHZ0bjeAe_tYNKjLxn2fEUucAU4JKzK2XgnSYRqM-ZTH3R9pKjE_meFVgfy4KL050ohfEOu-60w0JgC2p0zUyKIZGrpYhOiwKDvRVvr4Fykvtnz1I65f3sZRQTLnCECBzHR4ZFPBJvRbmqiFszoCCY0XLtzP4hqVyQiVshDH5NgZHl6c32XELXdMqw24Rf8ltTiu0-OVXsvwjd9u1o_V7dEzf0wEhpIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f07a869d6.mp4?token=qTkRWkTAxsggKJ8emb_eCgJziCkFwcSG1KvIF7ioQ059nPe_CguZg42rKwChLpgoqZCIgRJO_qLlakQN3IIXpkuCAxT5czD6ixn1NnRctZOYRSUz7MfdaXHZ0bjeAe_tYNKjLxn2fEUucAU4JKzK2XgnSYRqM-ZTH3R9pKjE_meFVgfy4KL050ohfEOu-60w0JgC2p0zUyKIZGrpYhOiwKDvRVvr4Fykvtnz1I65f3sZRQTLnCECBzHR4ZFPBJvRbmqiFszoCCY0XLtzP4hqVyQiVshDH5NgZHl6c32XELXdMqw24Rf8ltTiu0-OVXsvwjd9u1o_V7dEzf0wEhpIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«آبراهام لینکلن» از جنگ با ایران تا دعوای مستی در تایلند
🔹
ناو هواپیمابر «آبراهام لینکلن» که ماه‌ها در جنگ علیه ایران حضور داشت، پس از پهلوگیری در تایلند شاهد درگیری دو خدمه مست خود در پاتایا بود؛ دو نظامی آمریکایی در پی این درگیری تا پایان حضور ناو در بندر…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/687438" target="_blank">📅 18:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0259de181.mp4?token=iVBQAWo0rJ4qfOs9NFUJFTKDnUCM85VaPjJ_szTyqySYOjYhMVY_1i4KNTwlK4BjF5okroNZzSCamlMPGGEWocq-toYZw_F5ndpDKqY9o2fn4em4MHUtCAvcfu2BBX7Ko4CooM8Ir2UaJSP3dPD1K7Gm7KuHtFiOI4USRPHqAAeUv_mbbbGUVmiURwmyFB-CIB9Oy3cJELy6aoQ8Xe_tY2NuXA_UvIk7_r6sjqOHGGRCW5gx5cHlYBJmIsPiFfMmHb_1W6GVPxUyRVFdUcbzZCkwrAqoLAC26hR-j85pgSpCUil-vma0VXbz03Ci-JClalaZQ1NmzqR0pWgKlCoGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0259de181.mp4?token=iVBQAWo0rJ4qfOs9NFUJFTKDnUCM85VaPjJ_szTyqySYOjYhMVY_1i4KNTwlK4BjF5okroNZzSCamlMPGGEWocq-toYZw_F5ndpDKqY9o2fn4em4MHUtCAvcfu2BBX7Ko4CooM8Ir2UaJSP3dPD1K7Gm7KuHtFiOI4USRPHqAAeUv_mbbbGUVmiURwmyFB-CIB9Oy3cJELy6aoQ8Xe_tY2NuXA_UvIk7_r6sjqOHGGRCW5gx5cHlYBJmIsPiFfMmHb_1W6GVPxUyRVFdUcbzZCkwrAqoLAC26hR-j85pgSpCUil-vma0VXbz03Ci-JClalaZQ1NmzqR0pWgKlCoGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت یک تشکر ساده اما عمیق از سیم‌بان‌های فداکار صنعت برق
و چه زیباست وقتی مردم، خستگی این زحمت را می‌بینند و با محبت و قدردانی پاسخ می‌دهند....
‍‌‌‌‌‌‌‌‌‌#سیمبانان
#صنعت_برق_عرصه_تلاش_و_خدمت
💫
با ما همراه بمانید.
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/687432" target="_blank">📅 18:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qsy4YzxWMQUQ7Vz6-FZCMognT5d9MATUJLBxbn2881tQd0wfWqVWo6M5mCZWKpaThip4KFPGjrLO4Ufc2MV9EsV-EjkDT7KYguCuYQp0nWKKodSP1MzXZMel7kN4bOVKmV1GtgIq6AlXSMXxgohpgChoI8VtrXPxuBJre4S-cS9VYDtronLs9IWuuTqn_1QfQiwVjwjuIESjcV43ei-6_lr_GRAqiUdKjbNJkg5GYMg0_Yym5ZoeZgd0jK6brjqmbXClFXZ1cB44VuAz7MNL_qE_QlCfWlHNGBVSIBE386qTYf25QzwqrVK9iIZRhBvrUj-lxt6YBfgy0R-1kXS3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
احمــد کلاتــه
🔅
همایش سیستم بازاریابی تکرار
شونده
🔻
مشهــد - آمفی تئاتر شهدای سلامت(برج سپید)
🔺
چهارشنبه ۱۸ شهریور ماه ۱۴۰۵
🔸
رزرو بلیت:
🌐
metatickt.com</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/687431" target="_blank">📅 18:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht5XuWYOFAgVP5TKQB74GUrxeLE5vmVJeu5kPfLx6a0wdEepglPsfjsOvNgxsJpvQtajummey530k4iy2rPjYz1xzRUJ0qAWPAUsWN-ghfgSna7HX4zyVHklU1W85AhECzhr1Okv15kCAyEHlhcb1TiZ__bOE4bmduhQo8zoLlifQwvAhazPeo3efAJrhyFPhl-LtR493I57IXIt7f9U0DJayLf2Z6fgXAJGCjz2NB_ifNtn7gDrDVAd4C5KX2MREyC9EQTRNh3wANgO77sT4nToj-flVsm4iwLpnFZYDV9ivZ6ClONH58ugEl5fd9eEbmPWldd2-DfoMmP3rEYRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهل مطالبه رهبر معظم انقلاب از کارگزاران نظام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/687430" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صولت مرتضوی: دشمن نقشه داشت که ۸۰۰ هزار‌ نفر در فتنه دی ماه کشته شوند که تدبیرها اجازه نداد برنامه دشمن عملی شود/ وقتی فراخوان صادر شود دیگر ماجرا با اعتراض اجتماعی تفاوت دارد
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری:
🔹
جمهوری اسلامی از بانیان فتنه دی ماه نمی‌گذرد.
🔹
این امکان وجود داشت که بهتر از این موضوع فتنه دی ماه را مدیریت کنیم.
🔹
نتانیاهو گفته تعداد قابل توجهی را برای ورود به ایران آموزش دادیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/687429" target="_blank">📅 17:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687427">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
هشدار امنیتی سفارت آمریکا در بحرین
🔹
سفارت آمریکا در بحرین به شهروندان آمریکایی مقیم این کشور واقع در خلیج فارس نسبت به حملات احتمالی ایران هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/687427" target="_blank">📅 17:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687425">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83203145ee.mp4?token=Y8kmoWeMdIT5lv6IPdMoyFru3ctjut-0IJqmKitWOJI5ocmC5dmYlXkASArDh23EmMQXCPtxHNF39biq8KAW5jf3-p7m_7ODoVlNioKlr_3r_E21DcFSfKpjrTBe85FkUOgujd_n3-nu3-T6T2V-W_DA3KtIjg6zYS3i0RJE7YkYAi-rDGZfP4UP-uWwx3v9ZQXlEegxxPfug5Ih-oFfuYfmAWb3KBGt9ebwvp_cJEcplio2vOME5AKxXQGguqOstRuh8jioiSVkRbEKFq48Z69wto0XQkpQ1XjZ9EECkYm1yW5VEK1K0yjCkHw6psxMecKTYTzDLmxwSaWcTh8V7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83203145ee.mp4?token=Y8kmoWeMdIT5lv6IPdMoyFru3ctjut-0IJqmKitWOJI5ocmC5dmYlXkASArDh23EmMQXCPtxHNF39biq8KAW5jf3-p7m_7ODoVlNioKlr_3r_E21DcFSfKpjrTBe85FkUOgujd_n3-nu3-T6T2V-W_DA3KtIjg6zYS3i0RJE7YkYAi-rDGZfP4UP-uWwx3v9ZQXlEegxxPfug5Ih-oFfuYfmAWb3KBGt9ebwvp_cJEcplio2vOME5AKxXQGguqOstRuh8jioiSVkRbEKFq48Z69wto0XQkpQ1XjZ9EECkYm1yW5VEK1K0yjCkHw6psxMecKTYTzDLmxwSaWcTh8V7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهای آمریکایی سه نفتکش نفت خام ایران را هدف قرار دادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/687425" target="_blank">📅 17:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687424">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/687424" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687423">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdVVUUWtwK4z_jJy88xANuew0JrZAvdtMBCr-qbcQ1VFHviLbnA8Sbb0pZl5nV0oxHoE896q2XoAT8Z_orEaq-AsTkszE__-OhpwitlNR4Qe2UCLKo4AXXHdqJ9AFMrSH5p7g_zQTwnyGXlmhQrniGJukn-esQxzjsTXrlF-dhFPzWrVxYBcoMhHAHc45mM2W72EsMQzLFHxnPb1W2Ii7UD6QWYfPvU3HhVqGSmxskvS9vIv42Ixmk-wPQ9OKdU_Q8FKMkdNwyc2DJ6bVwbAv8oPMfa1hiU_m8YBwGld1i1dfaEVgKMKjuEwn8QrZsJefaPwyHPHvdkoCdX81AJiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت خطاب به مدیرعامل بانک اقتصادنوین:
🔸
اقدام مسئولانه شما در حمایت از تامین دارو، شایسته سپاس است
🔹
وزیر بهداشت، درمان و آموزش پزشکی اقدام مسئولانه بانک اقتصادنوین در حمایت از تامین داروهای مورد نیاز کشور و تقویت توان مالی شرکت‌های دارویی را شایسته سپاس و تقدیر خواند.
🔻
اطلاعات بیشتر:
https://enbank.ir/s/mfa9ZF
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/687423" target="_blank">📅 17:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687422">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عراق: اردوگاه داعشی «الهول» به زودی بسته خواهد شد
🔹
روسیه: اعضای گروه ۲۰ خواستار پایان جنگ آمریکا علیه ایران هستند
🔹
پلیس امنیت اقتصادی خراسان رضوی ۲ لکوموتیو ترانزیتی قاچاق به ارزش حدود ۱۰۰۰ میلیارد تومان را توقیف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/687422" target="_blank">📅 17:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687421">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-dlffEPNSxuMfw6gbNjx25jnS6it0Rj-y5XMUwwI-Yd1c86LJNkfA_C6aCkeTLp89Tei6pGTgKLF5DWZ3F-3Pk9zqltxq-F-pMy_GF3bCPtZhhVyA4dW5ACtG64rMWQu8I7u14SxUi-pYt0dY7Q2CN8d_1sFCTi73GORvl7SIJ6Dg2CqGr6l-R2b7sHOi-AEYUxsmFRkV4SsucNAoNgR9O8y5iIGAWlN8TwxGRC6_czMxJUwlmO0fPDiAc49ZIQP1tvfOvxBTpAgnmhZ21hmJ9MLU12P_wfzm-zlVDjn4s5nO433HZgiy8djXoVf2KL5RXFmZMx97yjbhaYl-aV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
سنتکام: نیروهای آمریکایی سه نفتکش نفت خام ایران را هدف قرار دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/687421" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
