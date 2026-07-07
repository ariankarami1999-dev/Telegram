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
<img src="https://cdn4.telesco.pe/file/osdWt1GLC7NyW_x5VFgBwooyo6rUnF4bJBGE1lSt8yaqkk6BKtJolol1lI9i1kG7WeTmX8XWljmYa-KpL3jSyaNLhhuh5CmDIFMJwOHf-gD_A2r0ZprT7MEiRCGtX6KVubnCivqRF4xpLOI0nFBtVVu5F7_1NYAf36t1E14Xed-7-uyyTD9CLVtFjwHYMnOMgU3vqi3nPutrGcxPpcoKAffnIzn2Lu93C_kyJiu6ro5bNQm6J0n1rCF9guBQOQrHYE1XHxWJI4UdMCnm2jLnP8-X2b_vEORvuaVG06XtwoOPWdYW10UAXRf923PCYBK6M-EftC36TwPbqKerLh7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-16659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مقام ارشد آمریکایی:ایران با شلیک موشک ها به سمت تنگه هرمز،یادداشت تفاهم نامه با آمریکا را نقض کرده است. @withyashar</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/16659" target="_blank">📅 19:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مقام ارشد آمریکایی:ایران با شلیک موشک ها به سمت تنگه هرمز،یادداشت تفاهم نامه با آمریکا را نقض کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/16658" target="_blank">📅 19:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ecd9127e.mp4?token=LU_ZUJJU-29oDej8uoegnaC_Yrn07PgHm3NQJub9qOzEMqhqu9_so6tO43qVBxx4czxTgDK97jCu_aGpOVDtAOjDWNSkJKXZLhKRKhmnvN10uJvXbQLKKyViL3gsFgQAu9-fYli8XippnLOvX_MT0s_himJGqfsM8cu0j50vbmesEsNym370AGr9_PpLHruGTCDNU4nbjjf957HcNrMfyi3EkKb6PoZEgtGfn4jkr-F5o0lmH-n1hp4jNQd4V5rZNh3ra-lIXQ9g6kvHObKwXSDIb7namalfYbzqAex-jeNKlLKEbfrUnmIXUL0H4zThijYFs4Zu1rgzLLnvaI2nzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ecd9127e.mp4?token=LU_ZUJJU-29oDej8uoegnaC_Yrn07PgHm3NQJub9qOzEMqhqu9_so6tO43qVBxx4czxTgDK97jCu_aGpOVDtAOjDWNSkJKXZLhKRKhmnvN10uJvXbQLKKyViL3gsFgQAu9-fYli8XippnLOvX_MT0s_himJGqfsM8cu0j50vbmesEsNym370AGr9_PpLHruGTCDNU4nbjjf957HcNrMfyi3EkKb6PoZEgtGfn4jkr-F5o0lmH-n1hp4jNQd4V5rZNh3ra-lIXQ9g6kvHObKwXSDIb7namalfYbzqAex-jeNKlLKEbfrUnmIXUL0H4zThijYFs4Zu1rgzLLnvaI2nzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکل زبون وا کرد
😩
@withyashar</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/16657" target="_blank">📅 19:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b528ebf23a.mp4?token=ksnFPAuyXHnoRgyk0mjU3FKqG8WSbB8Oi4LwkG_Hzceq5pBo373NupCL_YTTZH2Jwt_qb0N2tDpGdsfmYfFmYWPY4gPvM0xFNiPcUZ6uORwBPYLtX2GTTr1X4Utveh48qIzzhpVIhptEKz-dOrVtvNsFpWk0rnaxf974KCAick07RfKWpzCbfmXUCCRrBZFGmCe1Mn0oh584jSQ9pjA2Q5EAJAdvnZxbsl-1Vu0XKgPUf3lX_lp5WQrZKdbHuxZtYV_xAYTvSnWR7frN5I_W3vYh_ntBOWUr3Wn41K2pgXMAFOLJUat_tfEgpwkD49FnWgSHm-4CX9Xg-BhL7EO3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b528ebf23a.mp4?token=ksnFPAuyXHnoRgyk0mjU3FKqG8WSbB8Oi4LwkG_Hzceq5pBo373NupCL_YTTZH2Jwt_qb0N2tDpGdsfmYfFmYWPY4gPvM0xFNiPcUZ6uORwBPYLtX2GTTr1X4Utveh48qIzzhpVIhptEKz-dOrVtvNsFpWk0rnaxf974KCAick07RfKWpzCbfmXUCCRrBZFGmCe1Mn0oh584jSQ9pjA2Q5EAJAdvnZxbsl-1Vu0XKgPUf3lX_lp5WQrZKdbHuxZtYV_xAYTvSnWR7frN5I_W3vYh_ntBOWUr3Wn41K2pgXMAFOLJUat_tfEgpwkD49FnWgSHm-4CX9Xg-BhL7EO3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جایزه موش طلایی سیرک هم به این تاپاله میرسه
@withyashar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/16655" target="_blank">📅 19:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شبکه ان‌بی‌سی به نقل از یک مسئول آمریکایی: ایران شب گذشته دو کشتی را با دو موشک که مسافتی کوتاه را با سرعت بالا طی کردند، مورد حمله قرار داد.
@withyashar
اتاق جنگ با یاشار : دو تا هم  الان زد ، پس امشب دکل سیریک و برای بار ۴۸ ام میزنند
🤒
🚨
@withyashar</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/16654" target="_blank">📅 19:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl-2ZtBDHaVPPZJDMrB-F9rINXPNFY0EgQ3X_3VIC3aln78inpYtCB-_5iJcMOuYRThfwFWM8-lfu1qMyIuoZM78tSKnWTuNFRLa6GksLbuaMKOgHVQ8hPErhaxXxV4sL7X04D0NHlAmQXG5x-gUmR30O01nXWhlS69Njxp-A7sfrAu8CLnTb5DoBSkrsxMrOswm3oU_uFl0xO3Ky6NbaIs4QxiHkOhQdBy8cGv8z-YeWauor067IBsAyHDcrHhrUDIapXGmBxod-3KZBY-ASkO5ESsZwUGa7Vs6zX_Tn0hFEb80Bq9L9sKHvvVHWQlbDkVGQraOO2qdgpRhZzQ9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اینم یکی از کشتیایی که دیشب بهش حمله شده، به وضوح نشتی سوختش مشخصه، قبلا خیلی گفتم ۳پا میخواد بخش جنوبی هرمز(مسیر عمان) رو باطل کنه و به طبع تمام ترافیک رو بکشه بخش شمالی برای ایران، اینجوری نبض هرمز هم دستشه
@withyashar</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/withyashar/16653" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk2Gu3R9KGfh8rO9qFTBYQHLoPDfi-qFoV8OMu5GugNEjyZsGOENb9I2KZh5kBLA6SoWvgxEP5okXzQuQ2vo3-Xor0-EKhlfXNiBHE3PEYZPgcZ2LbadQPdDfE32em-oPjzUCcDkISMW5CRbVxJ416-eGJvVg2c4haI4To9doUYjjEaHxefINHR1gzDWVxniuRwL6Qw7bPytjkCfUqnjnWSiZ8vieD2Tg0KOQ8ip4d-hAyVgV6GgvslWkIPXHj81Kd2R6e5kntYsNYoFfrB2TszZhxmWIXCdjzG2xEFNleghJ4sPt25ibDcA3DPCAny8rM9kbv9Y0LilRgS5rzkmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله دیگر به یک نفتکش در تنگه
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از اصابت یک پهپاد ناشناس به یک نفتکش خبر داد.
این نفتکش هدف حمله یک پهپاد با هویت نامشخص قرار گرفته که منجر به ایجاد خسارات  در بدنه کشتی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/16652" target="_blank">📅 17:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک مقام ناتو به الجزیره گفت: رهبران این ائتلاف، در نشست خود که فردا چهارشنبه برگزار می‌شود، به موضوع تنگه هرمز و آزادی کشتیرانی خواهند پرداخت.
@withyashar</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/withyashar/16651" target="_blank">📅 17:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گروه فرانسوی "مهاجرین" که از جولانی حمایت می‌کند، مسئولیت انفجارات در نزدیکی کاروان مکرون در دمشق را بر عهده گرفت
@withyashar</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/16650" target="_blank">📅 17:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">درگیری مرزی طالبان و ارتش پاکستان
منابع محلی در ولایت ننگرهار اعلام کردند میان نیروهای طالبان و ارتش پاکستان در نقاط مرزی شهرستان دوربابا تبادل آتش صورت گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/16649" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqqvLLdlNLXU0r-rhyruydF3Ri8e39Q7k6rp9JRbHWoxmJTfhkB8Lq-QcKKfQJMBAk_X2JKtXddUXzrwQBfa5F6CKxX8_bG81ZO94QkarLu4CLF52x84_SXjXTiYURKIhohqK-o6EaKQCSlbFPGewsvK49TP5TvL75iDPGTC7qfZrs1w-o1jzSHFI5Q1DaqLMw8WdCUcoBsF-frH9caVNJgeDze5niSUDbhw9zcIvzi-Q2yWCGSb2V4m9g9iBnLnssN4w_nKvpxMjDtONjgQXZPQCnPS0Hj6rLJPMfaNMp4Jio_mvnnq69qs6K6OnLi6rgYQ7vKEXMrMf7TmHMtTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات دریایی تجارت بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفت‌کش در حال عبور از تنگه هرمز دریافت کرده است.
این نفت‌کش مورد اصابت یک پرتابه ناشناس قرار گرفته و به نظر می‌رسد آسیب‌های ساختاری به آن وارد شده باشد.
@withyashar</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/16648" target="_blank">📅 17:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/16647" target="_blank">📅 17:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دبیرکل ناتو: بدون اروپا، آمریکا نمی‌توانست به ایران حمله کند
رومانی بزرگترین فرودگاه‌های تجاری خود را بست تا به هواپیما‌های آمریکایی اجازه برخاست و فرود دهد
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/16646" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: ترکیه به خاطر من درگیر جنگ با ایران نشد و نمی‌خواهد شاهد دستیابی ایران به سلاح هسته‌ای باشد
@withyashar</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/16645" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بدل موشتبی خامنه ای خودش دهن باز‌ کرد !
این ویدیو رو پرت کنین تو صورت عرزشی ها !
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/16644" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ به ناتو : کاری که تو ایران انجام دادیم، اصلاً به کمک هیچ‌کس احتیاج نداشت
حتی خودم هم کمکی نمی‌خواستم. البته قبل از اینکه برم، گفتن کنارمون هستن
ما هم تریلیون‌ها دلار خرج ناتو کردیم؛ برای چی
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/16643" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور، آیا قصد دارید جنگنده‌های اف-۳۵ را به ترکیه بفروشید و محدودیت‌های قانونی آن چه می‌شود؟
ترامپ: ما قرار است تصمیمی بگیریم. فکر می‌کنم خیلی‌ها - می‌توانم بگویم، خیلی از افرادی که همین جا نشسته‌اند - بگویند چرا این کار را نکنیم؟
ما رابطه بهتری با ترکیه داریم و ترکیه از بسیاری جهات بسیار وفادارتر از سایر کشورهایی بوده است که فکر می‌کنیم وفادار خواهند بود.
و مطمئناً چیزی است که ما در نظر خواهیم گرفت - بله
@withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/16642" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قطر: ایران مسئول حمله به نفتکش ماست
ما ایران را مسئول قانونی این تجاوز و خسارات احتمالی ناشی از آن می‌دانیم.
هدف قرار دادن نفت‌کش قطری هنگام عبور از تنگه هرمز، تجاوزی مردود به امنیت کشتیرانی است.
ما از ایران می‌خواهیم اقدامات‌هایی را که به امنیت منطقه آسیب می‌زند یا کشتیرانی را تهدید می‌کند، فوراً متوقف کند.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/16641" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز: نفتکش حامل گاز قطر که در تنگه هرمز هدف قرار گرفته، به دلیل آتش‌سوزی در اتاق موتور، در معرض انفجار است
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/16640" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOf3-V2lCIBsOCBUZH-jHIZ5wa-CR_gWAHcXKxiE1utrbTsl1TiBw7hqaAEIMH35WK-Qiy78K9nAq_oosX9GLZpbttZkQ6n6MdX4SLXpOBbZvnKoPK01Zv7Nt-IIbgMV_ay5mhXsrUHa3GXg5aKwJmSVRcJX0NJSeX8EVwoxS-RaD83x2rqFNVTq7Wxf5peY-_Ch72rcw_UReYkYpWic0YTpWPPS4LeohgIXbbHmBmbD2OZFJIJt__CP_eRnJOnHX06jyLmJzNALOt8J7lf1xZYVhTO5npXz8YSikLHmXG1sQNvq9gtnuIyvFUnmGEffZULAAYxiSrD63BFoOO9ozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : کارخانه تویوتا از مکزیک به ایالات متحده (تگزاس!) منتقل می‌شود. یک معامله بسیار بزرگ. تعرفه‌ها در حال اجرا هستند!
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/16639" target="_blank">📅 16:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارتش اسرائیل و شاباک : ارتش دیروز در شمال نوار غزه به دو پایگاه تروریستی حمله کرد ابتدا، احمد یحیی ابراهیم بتش، فرمانده یک گروه نفوذی در سازمان تروریستی حماس و در یک عملیات دیگر  جنوب نوار غزه، حمواده ابودقه، فرمانده یک واحد اطلاعاتی نظامی در این سازمان را به هلاکت رساند.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/16638" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/16637" target="_blank">📅 16:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب سنگ به سوی وزیر امورخارجه ، عراقچی که با چند متر اختلاف به ماشین کنار وی میخوره
@withyashar</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/16636" target="_blank">📅 15:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال اردوغان از ترامپ در فرودگاه آنکارا، همینطور حضور سربازان ناتو با یونیفرم جنگ جهانی دوم.
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/16635" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">علیرضا فغانی کاندید قضاوت فینال جام جهانی 2026 شد.
@withyashar
🏆
😍
💥</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/16634" target="_blank">📅 15:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان در فرودگاه از ترامپ استقبال کرد
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/16633" target="_blank">📅 14:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.  اما امروز، خوشبختانه، با همه امکانات موجود،…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/16632" target="_blank">📅 14:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.
اما امروز، خوشبختانه، با همه امکانات موجود، از تمام رؤسای کشورها به بهترین و امن‌ترین شکل ممکن پذیرایی می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/16631" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/16630" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafRirPbCVKW3R0Dg3EuoIpaXLIRBKWP3rOw1c1q8yOe2LO9eZ_KMmxumBkRbIXaEOnxSQesHNZ2MKN8z5dqFH69_tE21Uzr-Mn1KBxBnWHFDhRXNia8pg9_nJOcvTiDeyJQEvb_aASzkeoN5bx-ZD0D-NAT3cZgM3IoC3JU90VzLATvRvnFutaa2mCNOj1FM1DGvzWjqFNBwHMxSyfSH6apR8aC1-QqQo-hFTj9GOI2blu3eG_pI5y8BmwRIIVeQDSSdk0R50kwt8Vvv5yy9pPHGzLA3xQ9yye9qzg5eLTGgTStGQ-JXMln5hc7xlrBN9SfHVQqwcV8zakcH_kfB3OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafRirPbCVKW3R0Dg3EuoIpaXLIRBKWP3rOw1c1q8yOe2LO9eZ_KMmxumBkRbIXaEOnxSQesHNZ2MKN8z5dqFH69_tE21Uzr-Mn1KBxBnWHFDhRXNia8pg9_nJOcvTiDeyJQEvb_aASzkeoN5bx-ZD0D-NAT3cZgM3IoC3JU90VzLATvRvnFutaa2mCNOj1FM1DGvzWjqFNBwHMxSyfSH6apR8aC1-QqQo-hFTj9GOI2blu3eG_pI5y8BmwRIIVeQDSSdk0R50kwt8Vvv5yy9pPHGzLA3xQ9yye9qzg5eLTGgTStGQ-JXMln5hc7xlrBN9SfHVQqwcV8zakcH_kfB3OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ همکنون در آنکارا به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/16629" target="_blank">📅 14:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/16628" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ7ifgJwnfVggHDzuGrwCtfTBIRHRseHYALbntKxnGDxdjfpti0YqA6ZH6gMzteZjls7haUnJ___PKyglNM3Z9kug88f1bWP21LA8O6CXifaeTA7nxK1u5bF3En6sjrETOBuGXNaQydouTaz-zxQHVJAPlybol6HJKcFAYmaEf9E67Gnsbt4Jyo8oj_dhZRTq6OjxpuZbVKq4CahdE4zlX2y58fIIyTVmKwMMMK6T6ZwWor-TJyM_e5oCZNjjk0V7lDbuvmlTTQw0YfIgXVzrsYWxyhyd6d7OnRChLl_9zoEPGskgpRqjWDziU3S3X_LHULPRFfIyleyD_oEVXAkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با هواپیمای ایرفورس وان جدید هم اکنون در حال ورود به آسمان استانبول است و حدود چهل دقیقه دیگر در فرودگاه آنکارا به زمین مینشیند.
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/16627" target="_blank">📅 13:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16626">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">منابع امنیت دریایی: یک نفتکش نفت خام با پرچم عربستان سعودی در نزدیکی تنگه هرمز در نزدیکی عمان آسیب دید، پس از آنکه یک نفتکش LNG در همان منطقه مورد اصابت قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/16626" target="_blank">📅 13:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16625">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfVLnW7NAwiGyT79VHbsUTxo_iUfVUG-T19k13EW6Iz4U0eBY2aIM9n-cKOCf6cMESGRY3f7aKE_F-BQAzi7jUfzmEjwhRyQUCNNB_vr0XqezeRLefX9LXAB8i3JtwzmkKe49xL30B-NVA31p04QRPbkXd_MEs3q6qmNuZq6ROQlD1upzDkM8SzohFHxRDegENXQ4SVjLQ4R4kNiOeHsqLt38qbySIbiyQeQKrLICGvMWobUsC56pP-SqPJzBUzYN6k5S-532Fv-La5yYkdd2n_p7E0YoocEFz55aDHkJ62Z9wP6CQXq5M_RBE5izYrm0m3BBkX6pRaR6wOveOZqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا هر وقت این کامیون عجیب و ماجرای تابوتهای یخچالدار را میبینیم ، یاد فیلم «سرباز جهانی» محصول سال ۱۹۹۲ می افتم که داستان دو سرباز آمریکایی را روایت می‌کند که در جنگ ویتنام کشته می‌شوند، اما اجسادشان در قالب یک پروژه فوق‌محرمانه ارتش بازسازی شده و به سربازانی با توانایی‌های فرا انسانی تبدیل می‌شوند. این نیروها با یک کامیون بسیار پیشرفته و مجهز جابه‌جا می‌شوند که درون آن محفظه‌های سرمایشی یخی ویژه قرار دارد و سربازان هنگام نداشتن مأموریت در آن‌ها به حالت ریکاوری نگهداری می‌شوند چون گرما ضعف این پروژه بود.
امیدوارم موشتبی خامنه ای‌ رو هیچوقت نبینیم و زنده نشه
😂
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/16625" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات بالاخره تپه علی الطاهر در جنوب لبنان توسط ارتش اسرائیل فتح شد
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/16623" target="_blank">📅 12:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم مثل تهران دیدن جمعیت کمه
در مسیر فیلم خورش خوب نیست کامیون ضریحی جنازه ها رو از وسط راه اصلی خارج کردن و از یه مسیر فرعی بردن
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/16622" target="_blank">📅 12:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مقام ارشد آمریکایی به آکسیوس:
ایالات متحده با حملاتی علیه اهداف ایرانی،انتقام حمله به نفتکش ها در تنگه هرمز را خواهد گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16621" target="_blank">📅 12:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=fE2AN4K-764v2P0ZZBIIzNREcD4-eUk_az_0cr-NGFSU2uaDGDfYTLNUobrBjjcUbkokBGW8Zrz0AX34m97rQ6ahBR2YB8mtR7DcPqCgf6l4s2NOrNBtO9lgME-Ftpw5QfmD6J88qNrvhN75oMAz88aN0L7TA-Fdids4bo_7pXdSM79mrcgB6EHaWEhIN87dl1LcVAGkoEdMOf7eYoFig61KtVltPmpL3hRt5nV1T5I6CbcB0m3OAVTZREFqIpYMwmeRG4TZN7wH2pE-nkE2rKDJi838I7zMe4w5BYnBGX1Po4Pt8JftjzqQbmwRtE8kRb7yNmLSDpTJJSUuyh_vbgx2WoVrNQrPVJCNNQjt0CemiOsqWEWwZWAjRTyKkiZO63MXkGI88--iAbKNm9UED3xO-7ys6x3QD-adxU2H4apaOu_xPRkpJZQ-pbvuENXv6G4rp8xjwDeqyHHSUs1XsXXRA5lo_cxycAwZLY1qbVxqXqHQlkoGtUJBjJakB_UnmU32zEJWU2yk-yMzdQgeh9AXYKH0DDiMxawrIsGZTHa7VYZB_DH5qY8_-pyxT1TM1W9flUz6sZMfcGYko21s9DT833fKlobeNq3CbCLU5yeQujCnSO2L3HSBUG6wqrZvXJVW_96zCIz0aIDp_sQ53f59ws0xAO-vEu0629QFBvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=fE2AN4K-764v2P0ZZBIIzNREcD4-eUk_az_0cr-NGFSU2uaDGDfYTLNUobrBjjcUbkokBGW8Zrz0AX34m97rQ6ahBR2YB8mtR7DcPqCgf6l4s2NOrNBtO9lgME-Ftpw5QfmD6J88qNrvhN75oMAz88aN0L7TA-Fdids4bo_7pXdSM79mrcgB6EHaWEhIN87dl1LcVAGkoEdMOf7eYoFig61KtVltPmpL3hRt5nV1T5I6CbcB0m3OAVTZREFqIpYMwmeRG4TZN7wH2pE-nkE2rKDJi838I7zMe4w5BYnBGX1Po4Pt8JftjzqQbmwRtE8kRb7yNmLSDpTJJSUuyh_vbgx2WoVrNQrPVJCNNQjt0CemiOsqWEWwZWAjRTyKkiZO63MXkGI88--iAbKNm9UED3xO-7ys6x3QD-adxU2H4apaOu_xPRkpJZQ-pbvuENXv6G4rp8xjwDeqyHHSUs1XsXXRA5lo_cxycAwZLY1qbVxqXqHQlkoGtUJBjJakB_UnmU32zEJWU2yk-yMzdQgeh9AXYKH0DDiMxawrIsGZTHa7VYZB_DH5qY8_-pyxT1TM1W9flUz6sZMfcGYko21s9DT833fKlobeNq3CbCLU5yeQujCnSO2L3HSBUG6wqrZvXJVW_96zCIz0aIDp_sQ53f59ws0xAO-vEu0629QFBvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه ۱۴ اسرائیل، درباره مجتبی خامنه‌ای : اون هنوز زنده‌ست
- از مخفیگاهش بیرون نمیاد و می‌ترسه، اما تو دورِ بعدی درگیری‌، یه بمب اسرائیلی به سراغش میاد
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/16620" target="_blank">📅 12:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید @withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/16619" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به ادعای رسانه ها دولت مصر با یک تصمیم سیاسی، تمام برنامه‌های سالگرد درگذشت محمدرضا شاه پهلوی شاهنشاه فقید ایران را که همه ساله در مسجد الرفاعی برگزار می‌شد لغو کرده است.
‏همچنین گزارش شد که از سوی مقام‌های مصری به وزارت خارجه این کشور ابلاغ شده اجازه ورود چهره سرشناس مخالف حکومت ایران به قاهره داده نشود.
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/16618" target="_blank">📅 11:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: کنگره باید بودجه ۳۵۰ میلیارد دلاری دفاعی را تصویب کند
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/16617" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شبکه الخدث عربستان سعودی گزارش می‌دهد که رئیس‌جمهور ماکرون، ربع ساعت قبل از وقوع انفجار، هتلی را که در دمشق اقامت داشت، ترک کرده است.
در سوریه‌ نیز گزارش شده است که رئیس‌جمهور احمد الشرع، دقایقی پیش از رئیس‌جمهور ماکرون در کاخ ریاست‌جمهوری در دمشق استقبال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/16616" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=h3cYolUcr2Tbjp6IpKSfwb1iUzZOvRB_uRYXMtqkFe9Hgkh-5eFvI5zRND-1IkUWq-ZRjpPUmzmfNPbbmJLCpSRVyJux9KSnUK2_qczidlQVHl7diKV1RqNRYpfDjFqa59XA-2Sv_zUcArfwoPCM183xj9b7D1JsYFbx4vKlDJsdufGO0iAHzoUfbzbFf-ygQzb1c1qID6I9ZaLYdbJ64tXvAMXDlzUMxYiUWr1FyC2-P9VhIgpG_dHv-A5smqYatpL5SUWu5yBQQV3-mqo9oT6Vrw9i7-cDOokL0F_zVIvzucYq8Dd91Y5M_m4V8ucQkj5aRAc-yEO2NKoFQKZT6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=h3cYolUcr2Tbjp6IpKSfwb1iUzZOvRB_uRYXMtqkFe9Hgkh-5eFvI5zRND-1IkUWq-ZRjpPUmzmfNPbbmJLCpSRVyJux9KSnUK2_qczidlQVHl7diKV1RqNRYpfDjFqa59XA-2Sv_zUcArfwoPCM183xj9b7D1JsYFbx4vKlDJsdufGO0iAHzoUfbzbFf-ygQzb1c1qID6I9ZaLYdbJ64tXvAMXDlzUMxYiUWr1FyC2-P9VhIgpG_dHv-A5smqYatpL5SUWu5yBQQV3-mqo9oT6Vrw9i7-cDOokL0F_zVIvzucYq8Dd91Y5M_m4V8ucQkj5aRAc-yEO2NKoFQKZT6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تصاویر ماهواره‌ای رویترز از تهران در بهترین ارزیابی حدود چند صد هزار نفر را نشان میدهد
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/16615" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=LkU70ypk24I5dGRNROX-Y3668KJiJlfgYjxQbm2lqj0m1rcE6wTDjsvR1TZO3wKRtLgJWE8hNfgj_VoVNVHC4JemmY3eOjfqmz8IPytU2Tkv-ZQT4tZZZIw2zinNXQm_KcaMNrOINqTTRJvU9BxjEP9HdCgHrArlsQJvN0YTUy6cmbkOjKbvcSg2QP-kawPGvut_Jr81jiOrpaeNXadxxMmnsSBzsqwbiovCSORVwWgMpesww40Nf-r0XkjoRwbhCR4-rypClYfh1FmDmH4jKcRIaaVywixtY_FpvG6SnZu32edLkDvaKDvkf4wh8gzWztn5s3H-u2KrE_Tbqh5ZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=LkU70ypk24I5dGRNROX-Y3668KJiJlfgYjxQbm2lqj0m1rcE6wTDjsvR1TZO3wKRtLgJWE8hNfgj_VoVNVHC4JemmY3eOjfqmz8IPytU2Tkv-ZQT4tZZZIw2zinNXQm_KcaMNrOINqTTRJvU9BxjEP9HdCgHrArlsQJvN0YTUy6cmbkOjKbvcSg2QP-kawPGvut_Jr81jiOrpaeNXadxxMmnsSBzsqwbiovCSORVwWgMpesww40Nf-r0XkjoRwbhCR4-rypClYfh1FmDmH4jKcRIaaVywixtY_FpvG6SnZu32edLkDvaKDvkf4wh8gzWztn5s3H-u2KrE_Tbqh5ZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند انفجار در دمشق، در نزدیکی هتلی که رئیس‌جمهور فرانسه، ماکرون، در آن اقامت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16614" target="_blank">📅 11:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک منبع امنیتی ارشد لبنانی امروز به روزنامه "ال-جوماهوریه" لبنان گفت:
"ما در صحنه، هیچ اقدامی از سوی اسرائیل ندیدیم که نشان‌دهنده عقب‌نشینی از مناطق مشخص شده در توافق‌نامه باشد. برعکس، شاهد تشدید عمدی تنش‌ها هستیم."
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/16613" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رویترز به نقل از یک منبع امنیتی: انفجاری با استفاده از تعدادی مواد منفجره در نزدیکی هتلی که ماکرون در آن اقامت دارد، در دمشق رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/16612" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صداوسیما : نفتکش هدف‌گرفته‌شده در تنگه هرمز پس از نادیده گرفتن هشدارهای مکرر مورد اصابت قرار گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/16611" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=IjRupySFkfV_gddBm9hsyQrXZ0XHDmx1usUC1NbWJOw4Yq_8MjEReq0uY2qZhPZFQthI_SOeVbTTVkpEedTKir7eKVrDtftvZfelkDUnfPGvq8FayfTubz8Kl68UmzxP-LjFu6gzlMDpzgaQZ49pJOsDsgdhahfCi6tGoDw3dG0sQoWukfW9n0HKOgc9lHUAIbHluyotBGRPIAXO9-OscCcqS79MAeUCOEjG-m6oEcNhduWerkaxgdmW1YFGUFdGwBUflg5xN7EOg3tgGBh7qW0T9dc_MSE_xMoGrR8MMD73jOLwMHf7_wzGfk7hqC87WXcUc0wystNtHjqq3m_HuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=IjRupySFkfV_gddBm9hsyQrXZ0XHDmx1usUC1NbWJOw4Yq_8MjEReq0uY2qZhPZFQthI_SOeVbTTVkpEedTKir7eKVrDtftvZfelkDUnfPGvq8FayfTubz8Kl68UmzxP-LjFu6gzlMDpzgaQZ49pJOsDsgdhahfCi6tGoDw3dG0sQoWukfW9n0HKOgc9lHUAIbHluyotBGRPIAXO9-OscCcqS79MAeUCOEjG-m6oEcNhduWerkaxgdmW1YFGUFdGwBUflg5xN7EOg3tgGBh7qW0T9dc_MSE_xMoGrR8MMD73jOLwMHf7_wzGfk7hqC87WXcUc0wystNtHjqq3m_HuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره ای از ۶ ژوئیه دیروز ، چند هزار نفر را نشان می‌دهد که در نزدیکی برج آزادی در تهران، ایران، برای مراسم تشییع، جمع شده‌اند که کاملا برخلاف ادعا های میلیونی رژیم است
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16610" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN3m7ICGIsYpIddRTA2xNyw-bbHsM1twKEyGpQNh5bBuXCe4djNA-p317rxqoGnWTm2iXSy9P_PzUbaiQGGyupzO8nyK6_zUJLWCpnOv33GjvxohuZSTvXCKaM4dfL-VpN5sk1NsxOgDbhkT4v7ZPO-tMsVHxl469MqzUCr1USK4zFpBON8gie-tpfFJ4W5AaQDj7V0TsByB-YkL8G5biQ75BlnkNJhNnB1niI3mE4WP8CKgnSdAQ5acPJXnD9pCcnMDJl9-X4XL1OkKQX2aKu8b47GUQrcEibMWUnpXGpo-7-9FSwZgL3rdjhbjgzAM5AxkILkECMmyGtcUZV6KIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدل ایست نیوز : تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/16609" target="_blank">📅 10:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB7GtZtQ7gV2uuFzx8a-JytthMDbpAGtclfZtfJWGIy3tTi5fgWCw20SFYmebTBADpKX_XMun_OxHolXDqLZbnsgOX8FNdrIjLh4sfxJRogIxIPumfdSdZkx2ArHo-AN5l4ofYWzkulfMU6AsBy8QKtUXcKY55w7wdnTE9lDVo87M1CW7gXk3p_83LCBGMZEmgGwnslIHSXn0lTbXbE5mEmxTXWWbSUUkOXTZBFYS4jgNJE_utRAB7ZC0z47Qdl8OlvGaDqAdal5EehyiJFizwvQAhxYaQSSxsvIj7OKJ_a7Gq-xeHhgoc_-Jp4wkd7EkpUm_Y_2L6UL5KLlI5p8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/16608" target="_blank">📅 10:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عراقچی به ترامپ: به امضای خود پایبند باشید
تا زمانی که تهدید‌ها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/16607" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به وب‌سایت والا گفت:
حماس هیچ قصدی برای خلع سلاح شدن، تسلیم کردن سلاح‌های خود، یا تخریب تونل‌ها ندارد.
استعفای دولت حماس یک اقدام نمادین است که با هدف نشان دادن تغییر به واشنگتن و شورای صلح انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/16606" target="_blank">📅 09:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/16605" target="_blank">📅 09:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTWHSiItylAfhanwHch8it4yaJZ7xRwr1IQKt9jhu4Qwury5nNTQI8vtxn5mTvklhN8fwSe_65zFXNys0eQagcyLlidvovB9DNcsDMvateWaaaZkHta0g2oYTNnIA8Bu4ONw00SwmT4_kuU5h_yWVMkrVfu6kXiJcy2-EI5WMLe9lJqYTc7qGKgtA5pb8IW8w1lz3dHnYu4hg6Vd3u6ALGnnfXgdBqssQhiSNmFN_83A0SKhu6lo9kMcabzG5Z-gfEQ0rdSwac1oF1cirUsW0iOYuoGkzlyOjU71fDgOASD9zDWnKZMhv4cnL34rv-ulMM0pv0DR2d2VzF_awmHc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
گفته شده نفتکش مذکور حامل گاز صادراتی قطر بوده است
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/16604" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=RmU4rwA5U9eAhuHdfCmlxf9FuAGtByBr7juJl-IhAtNfgiprdbOWZiMrvNJimISxcQ-oWqNnZZNe3dAjZo2RRk-DcEENOCfznRzQToqDf33PSQR8Gl7_jCSvMHpOx5JaVDukuU4nmFRmmCu4I7baQlKF3VFvELIF4dKmetmEVl5EG2pxXpMn4e0HafoSTQSw_yK2S8wV69orRNRkZC2-2fbig2YRsq3DymyCc40SoCmbz1_mu3TG6F_XWa-7gpHGkv8Xuke4gsdrSM0pTzYYAyEve9Q_I11fGDfU3t5EmYeoaypSPgaE5bJ9MlSBBQl4Y4VmV6nLiYhBHTqgeeS2Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=RmU4rwA5U9eAhuHdfCmlxf9FuAGtByBr7juJl-IhAtNfgiprdbOWZiMrvNJimISxcQ-oWqNnZZNe3dAjZo2RRk-DcEENOCfznRzQToqDf33PSQR8Gl7_jCSvMHpOx5JaVDukuU4nmFRmmCu4I7baQlKF3VFvELIF4dKmetmEVl5EG2pxXpMn4e0HafoSTQSw_yK2S8wV69orRNRkZC2-2fbig2YRsq3DymyCc40SoCmbz1_mu3TG6F_XWa-7gpHGkv8Xuke4gsdrSM0pTzYYAyEve9Q_I11fGDfU3t5EmYeoaypSPgaE5bJ9MlSBBQl4Y4VmV6nLiYhBHTqgeeS2Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوایی که ما تنفس میکنیم سیاسی هستش !
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16603" target="_blank">📅 02:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=CelMbeSbmaKmwRP01ReYmyuXENzstBCfD8cq3FfL2EQEmOwVJ598s_nFpZAk4DiuHJDCWy05x4MMXTS2frHWtDz_R03lrSYtpqYPngarPfBRoUn436tnhH5opZAmxy9RarfHy0N5m52XBXNYb2K3XUR7jfcsKGifOU5eXApKE4qD7g-z2fhZYAHskfNx5i5ACVQesC8R572VoqBgv-xVYAD3PX55PXP5KyeulXmENCERNzsp15Mx7H3X7sfGM1L0Es67YnuUBKWDMX5JCjII52BO-nqv2ZyndFpkUrRrgggxokbw8u5MtkiinnH1rdkW5a-op2PCEcSerrDsg4Nx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=CelMbeSbmaKmwRP01ReYmyuXENzstBCfD8cq3FfL2EQEmOwVJ598s_nFpZAk4DiuHJDCWy05x4MMXTS2frHWtDz_R03lrSYtpqYPngarPfBRoUn436tnhH5opZAmxy9RarfHy0N5m52XBXNYb2K3XUR7jfcsKGifOU5eXApKE4qD7g-z2fhZYAHskfNx5i5ACVQesC8R572VoqBgv-xVYAD3PX55PXP5KyeulXmENCERNzsp15Mx7H3X7sfGM1L0Es67YnuUBKWDMX5JCjII52BO-nqv2ZyndFpkUrRrgggxokbw8u5MtkiinnH1rdkW5a-op2PCEcSerrDsg4Nx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع جنازه انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16602" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1Qpkz4jH0miFTWVCXNBTt8JujW5CB2_2R19HsHGZGTP5feAYgKgphoLGCTQiq8tSPRP_aFPNmSvflEZPPxi-0jRlB-ro4KwkOpKmtnYBRNkVNvTir-4TVcslHIzP7FuwI3xj1YKW2uZGcqoGRzQAhGxcdaJJyjyRyLwrIM2iQ_LgAS6uIOIAuRTdALgqIJeR39me8s1aunCxRmwzqKZPKidd8MX6MBVtAR8IX9uidU_W2UoEHyvoOJRKCU63bAZahBwOBQa6sBm5pXHg97edw5cNJGsUMxArUpG_dGlkUt38uXf_7pLSJuzD6jg1Z7etS_0NilD23fFDzOVVNa9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16601" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر امور خارجه آلمان:
ایران باید تمام هزینه عملیات‌های بین‌المللی برای پاک‌سازی تنگه‌هرمز از مین‌های دریایی را پرداخت کند
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/16600" target="_blank">📅 01:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو لوئیز نازاریو دلیما</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16599" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16598" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from~‌🇭🇦‌‌🇦🇳‌~,</strong></div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16597" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی : کیپ‌ورد آرژانتین رو حذف میکنه، من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود! @withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16596" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doFf2Qc6QfNtSl_sy0uzGN0FRlSxR7MjteqfLsPT9AZ6Z4GrxF5LjMVx2kM7FdhOWds_lwH8LJsuvZaSYBF8y7LThJV3sbJAvQH_PLaNa6H06IVa6WE8biw8gAbuLKzdPlwPR2WUd1Dg3l5D5Rdfl-_HhukKyAr3Ht1lRziUDm6ncGBA5T1k6zJ7dcunmqmLfa2OQUW2DfzGojCBFIHg8_LYAHeKS0C9H3aEsOqFXt5tc0JfbbfeH4MuYeoGclbNZ6vT0r6bhB4wqRa-ADaP9zkw4PP9Q4puepYgEDzpPIU5OmvSKLwY7R0UWta66fiQRleAJAkTQS-YSEWGw6iZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ پاسدار صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@withyashar
🚨
🚨
🚨
🚨
سربازان گمنام حضرت موسی بد فرمون دادن</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16595" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آکسیوس : نتانیاهو در تماس تلفنی با ترامپ؛
- خواسته که به اردوغان «تذکر جدی بده» یا «جلوی رفتارش رو بگیره»
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16594" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است. @withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16593" target="_blank">📅 00:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استان هایی که تاکنون سه شنبه ١۶ تیر را تعطیل اعلام کرده‌اند:
استان تهران
استان قم
استان سمنان
استان خوزستان
استان مازندران
استان اصفهان(شهرستان های آران و بیدگل و کاشان)
استان یزد
استان مرکزی
استان بوشهر
استان لرستان
استان هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/16592" target="_blank">📅 23:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دیوید کیس مشاور نتانیاهو:
بمباران مراسم ؟
شوخی میکنید؟
صدها مامور موساد توی اون مراسمه!
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/16590" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=JpluzN_VijObx1XiPnfLmmY8NuvXjfpXZ4_zQM7S-adqQ28GA1c7Gv8sJYw4dTUs_0M9Kah9O9WcAz8uozsjgIvGybdhjm9_dz606082yB9p0EALqxdpBj6c-eGf_U0RDkSptJ5WyrVfONYZsIPrIyPOvg9uT7fLcCvB2I8-lqNIPM-4SiQ1RQ9hdX-L3Bz-n8SeFPMp7bqWf-wH0MKI0xeXHfZOlt8rmAuYLY53XFqUyx_-2erDYlpamVlYbcz0mJO5ljzFrPDv8uhuvhylq2zSR8agxz8tM0hGqNtBLV-eba1IGlfVsfCBdAGAsx6QqXH50X5CYuBOBCmMACjj5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=JpluzN_VijObx1XiPnfLmmY8NuvXjfpXZ4_zQM7S-adqQ28GA1c7Gv8sJYw4dTUs_0M9Kah9O9WcAz8uozsjgIvGybdhjm9_dz606082yB9p0EALqxdpBj6c-eGf_U0RDkSptJ5WyrVfONYZsIPrIyPOvg9uT7fLcCvB2I8-lqNIPM-4SiQ1RQ9hdX-L3Bz-n8SeFPMp7bqWf-wH0MKI0xeXHfZOlt8rmAuYLY53XFqUyx_-2erDYlpamVlYbcz0mJO5ljzFrPDv8uhuvhylq2zSR8agxz8tM0hGqNtBLV-eba1IGlfVsfCBdAGAsx6QqXH50X5CYuBOBCmMACjj5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16589" target="_blank">📅 22:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم. @withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16588" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=ZbWrecxze7ZRGgQRwiSf1PQ4kWf-g5EVoANbAxKi4sC35T44SjazCm75l-TyrqKylNt7p_Tz6utQR9oWOtqWIob96Ct3uKFb3KlJN3w2a1LjvnWY2KEzFR1abk3ONCW8Nw6nyNLo8frVQiHMUKMl22CN1pTn-N7sYOoLDK5IjMxthsAjFJEXiQAg7u6ljU4erljQWOHUCKeXAnhu9v4LPltVm0fKVRdOMy52X3r4RrG7kBultN8SvhecRe_Swr_576QA_aLwLwfXV7GqKYLwIqtxGPtBBpHUGUNfZyfUbHeDZRyNaqfRxUms3nvmY8JhfWHbjn6hkWNL-5Hbmes9Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=ZbWrecxze7ZRGgQRwiSf1PQ4kWf-g5EVoANbAxKi4sC35T44SjazCm75l-TyrqKylNt7p_Tz6utQR9oWOtqWIob96Ct3uKFb3KlJN3w2a1LjvnWY2KEzFR1abk3ONCW8Nw6nyNLo8frVQiHMUKMl22CN1pTn-N7sYOoLDK5IjMxthsAjFJEXiQAg7u6ljU4erljQWOHUCKeXAnhu9v4LPltVm0fKVRdOMy52X3r4RrG7kBultN8SvhecRe_Swr_576QA_aLwLwfXV7GqKYLwIqtxGPtBBpHUGUNfZyfUbHeDZRyNaqfRxUms3nvmY8JhfWHbjn6hkWNL-5Hbmes9Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون با عینک آفتابی معروفش که ترامپ مسخرش میکنه وارد سوریه شد
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16587" target="_blank">📅 21:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئیس‌جمهور فرانسه پس از ۱۸ سال وارد سوریه شد
یک منبع ریاست‌جمهوری فرانسه اعلام کرد که سفر رئیس‌جمهور این کشور به دمشق با هدف از سرگیری همکاری‌های اقتصادی و تجاری با سوریه انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16586" target="_blank">📅 20:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=kvS5tsEdmd9ozgcXsG2X5JiMheKhyWS3UGlzsNosIJGbHgk6OLYBBlopWjKKicM48fK57VMW57-i_1rID5_hoGwcMg6_GPWYQTICh1nDHbudgShX44f4HUblMnPJ6q-kddviZ50nB1hyl8kagPiZhfU0jPWpPEzwPYLgZuHcESHR5G1kbD9_n2rLZPoDe2i1k5pbKPLFxLMAWVr6XsA9lp6Er7x7e_SJssoa0g27ltb-NgkwW8O5JjVA_74f7907WqedMeFzxthfkR4VXw9_lDqhPhJVwgq-JrRtQWaR4knugd0jXZ-SaQWNTp_0n0WvgnEiVKcfWt9UcctgGl5gDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=kvS5tsEdmd9ozgcXsG2X5JiMheKhyWS3UGlzsNosIJGbHgk6OLYBBlopWjKKicM48fK57VMW57-i_1rID5_hoGwcMg6_GPWYQTICh1nDHbudgShX44f4HUblMnPJ6q-kddviZ50nB1hyl8kagPiZhfU0jPWpPEzwPYLgZuHcESHR5G1kbD9_n2rLZPoDe2i1k5pbKPLFxLMAWVr6XsA9lp6Er7x7e_SJssoa0g27ltb-NgkwW8O5JjVA_74f7907WqedMeFzxthfkR4VXw9_lDqhPhJVwgq-JrRtQWaR4knugd0jXZ-SaQWNTp_0n0WvgnEiVKcfWt9UcctgGl5gDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16585" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=uMYcjo0MjenGWSPGWVpQh3SGYhCNdJjRQ2RHVK8LAiP-u7yTtCO-SPphmk5YrJZYSIy0EHWq6U_OIOK3vsR7xgW9bbqWuOLjzZT9EX2JtmGowupzK5BisQhkMqyqm7fZ39gGRBaaYX5iyUksburJsQ_VTERdkpejaLfAeUcWl4NnIJNBaE4Pi3jGOldmjn4_aeDfaV5nCPD0OBV0JrT1CBOeBzARLXn-Cpv-oXy1YbAQNafqBtIxK8BjsB3KaG1OQ4WQKmhlqXJ3VJTQzLQh2n-ZiYM9qXSbWT9HI-88fP8Prcc-57w2fqyg4Em4XmjM-IGZAdzjJCZXzMJMB_rF5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=uMYcjo0MjenGWSPGWVpQh3SGYhCNdJjRQ2RHVK8LAiP-u7yTtCO-SPphmk5YrJZYSIy0EHWq6U_OIOK3vsR7xgW9bbqWuOLjzZT9EX2JtmGowupzK5BisQhkMqyqm7fZ39gGRBaaYX5iyUksburJsQ_VTERdkpejaLfAeUcWl4NnIJNBaE4Pi3jGOldmjn4_aeDfaV5nCPD0OBV0JrT1CBOeBzARLXn-Cpv-oXy1YbAQNafqBtIxK8BjsB3KaG1OQ4WQKmhlqXJ3VJTQzLQh2n-ZiYM9qXSbWT9HI-88fP8Prcc-57w2fqyg4Em4XmjM-IGZAdzjJCZXzMJMB_rF5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نسل چی میخواد از جون ما ؟
اومده تخم مرغ آبپزشو بگیره…
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16584" target="_blank">📅 20:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=VqOOF62TIPW6h1OY1-SCUKb6Emavb0fXG0sM0_2DbJ9q-WQKPgrcIm6RtJ5BqQBw2FA4yMlrZxBuDH_ITdupdqs4iHUB_IiZn8-FhDmyYGTb-lv0wu5p763VyHqqB22Q1sV9ovHkI0hDXtmMWrwqehRADUtZmGYqUgjqHT4z3UGazl9aViakQLq_Md5xaFmb1GJ_Z-PFuBHshCuc41uQrD9LxkdDIp_ly6wR8xK29WBtcmRFFq8-iz-hlpUWP-FFMPLZ6f5lMnwrspM7e4AdnqZnNXRzWloqT3G-ZFU9mxsjn-RHZQZ7jCOsqJQhvBO8flECZhQ47KxIQlHf4whTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=VqOOF62TIPW6h1OY1-SCUKb6Emavb0fXG0sM0_2DbJ9q-WQKPgrcIm6RtJ5BqQBw2FA4yMlrZxBuDH_ITdupdqs4iHUB_IiZn8-FhDmyYGTb-lv0wu5p763VyHqqB22Q1sV9ovHkI0hDXtmMWrwqehRADUtZmGYqUgjqHT4z3UGazl9aViakQLq_Md5xaFmb1GJ_Z-PFuBHshCuc41uQrD9LxkdDIp_ly6wR8xK29WBtcmRFFq8-iz-hlpUWP-FFMPLZ6f5lMnwrspM7e4AdnqZnNXRzWloqT3G-ZFU9mxsjn-RHZQZ7jCOsqJQhvBO8flECZhQ47KxIQlHf4whTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16583" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-1c24-CM9OwG2P3y4hd0tQqeKEmY40_8oFfzE4x_S_BPp0ap2cYAGQMICuzxeJygNKP8p-nhBxfNaWoiHWBgoGBNSnUzPXt894RYPsJQj-npuGf8fGm9jWXqJrYgalWXMHN5TlQIgBzuUtTBBp2L1LsaoQ3I-nuB2fmt3xrQWtuJzz0aNzw9ApvtesIxvhUnP1iiluO8ijDu61ZmMVgndljS-cKz9vpINzwg-P26K_VniuODaKs_1mC8zvovyQcIa0-xptD-SGg2iMG_HQZ_qlUTJwyh_CUWiMroUFzBAcug0BR_XzGZPp-jrRJLwHOsDvu8vRIF7lJXA8e6MZx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام شرکت دل پس از اظهارنظر دونالد ترامپ مبنی بر اینکه «بروید و یک کامپیوتر دل بخرید» ۸.۳ درصد افزایش یافت
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16582" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16581" target="_blank">📅 18:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=oPqI6fkNY-KCwYHQY1hwC5TDLwaAaUSTlQMenb0KP6od_qoSPAKMbAyogH6qoaWch3cKMZtwzLN_juNk-Dy-CeVtz7CEJZeETw5C9Qk2gP_9clKktUTNMFzcsLPGQEK5oRFUTEJkqrpbYRq_F_SXqqlLJxzsz6ALSnaV0CrH3zH3EAsJpT28eEY6OSuQNVuyc-0BTJNiF8rlo8jsE7_thXBP-8KjEZTg0tFH5NwPpR32FTrRo1sH2VVL2Q7Vtfzos2hU2HL_2Hu6h5pzk1V_hal22JMtGNU__pYWheOz0EULt8iPPAeNxMAAKh-qOL6bCjr8IKJHHNbDqMUSUbCPyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=oPqI6fkNY-KCwYHQY1hwC5TDLwaAaUSTlQMenb0KP6od_qoSPAKMbAyogH6qoaWch3cKMZtwzLN_juNk-Dy-CeVtz7CEJZeETw5C9Qk2gP_9clKktUTNMFzcsLPGQEK5oRFUTEJkqrpbYRq_F_SXqqlLJxzsz6ALSnaV0CrH3zH3EAsJpT28eEY6OSuQNVuyc-0BTJNiF8rlo8jsE7_thXBP-8KjEZTg0tFH5NwPpR32FTrRo1sH2VVL2Q7Vtfzos2hU2HL_2Hu6h5pzk1V_hal22JMtGNU__pYWheOz0EULt8iPPAeNxMAAKh-qOL6bCjr8IKJHHNbDqMUSUbCPyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بررسی ترافیک کشتی‌های تجاری از طریق تنگه هرمز طی ۲۴ ساعت گذشته که از طریق مرین ترافیک قابل مشاهده است، نشان می‌دهد که اکثریت قریب به اتفاق کشتی‌ها همچنان از طریق طرح جداسازی ترافیک (شمالی) ایران عبور می‌کنند و تنها تعداد کمی از آنها کریدور جنوبی تحت حمایت ایالات متحده از طریق آب‌های عمان را انتخاب می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16580" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=bYt5hgnIbKZNC5dYomSbtZpQjxINhbI755lYtmeB6OVfX5mKX1AjlEn342VilY92Rj2F-nBPdy_n4Fq4VmDkFH5uYW2ZUwz0z6ixbU2ax5hVOH2idWjaawWRlSawkguRXTN9cLONpaROUkS-M_lQ5y2UO7wfJg8tsZtJDSGLZWMRDivY6Nvrswn6X7YyD6p19BtJz9FGVk8trgAGz6f4a3o721Z-c9Oawz0SFKnBFtMHplMtup4lcUPDPZRYIjNFXD4XV1BQV9Rch7qfFnfxh0_jfA-YNoWQ2SPrdnjBfXda2R9STh00OIZV8oycyN7ua5-hFX2OXdQfs6m4fIEtAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=bYt5hgnIbKZNC5dYomSbtZpQjxINhbI755lYtmeB6OVfX5mKX1AjlEn342VilY92Rj2F-nBPdy_n4Fq4VmDkFH5uYW2ZUwz0z6ixbU2ax5hVOH2idWjaawWRlSawkguRXTN9cLONpaROUkS-M_lQ5y2UO7wfJg8tsZtJDSGLZWMRDivY6Nvrswn6X7YyD6p19BtJz9FGVk8trgAGz6f4a3o721Z-c9Oawz0SFKnBFtMHplMtup4lcUPDPZRYIjNFXD4XV1BQV9Rch7qfFnfxh0_jfA-YNoWQ2SPrdnjBfXda2R9STh00OIZV8oycyN7ua5-hFX2OXdQfs6m4fIEtAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جنگهای پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/16579" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
هیچ پولی به ایران نمی‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16578" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=vwcn_lUp7L7TiO7gnvTpfGRa5d3yuNSKzMrnvwOWPdKZd_KuFBTxtp2K1PrBkWe3PE3jnbJjZmlN54GPIq8HEuQptVfGiUDxLj-tsPWaBBGMIbf4zn3ec2LWVWz2UE6eysK3eM0-2bc5nJ-m4vEQK3s5ac_Acr1nOr1UFvtnKP3WqfoWuGcy76zHN1la-3zCytMk1cJ8nXwaEKQfPd6bc65jArz-y7-a06qBfbvpngCL_wanh9c63_5lF-eEfJW_zDY4Yr26IeFaEB9ZMor8D8tVKIMytHWkUWP0JmGjw4P0UxC0_lgb1pz43n8QuNvjE0Fd3zD2T4TwrK9-8gu3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=vwcn_lUp7L7TiO7gnvTpfGRa5d3yuNSKzMrnvwOWPdKZd_KuFBTxtp2K1PrBkWe3PE3jnbJjZmlN54GPIq8HEuQptVfGiUDxLj-tsPWaBBGMIbf4zn3ec2LWVWz2UE6eysK3eM0-2bc5nJ-m4vEQK3s5ac_Acr1nOr1UFvtnKP3WqfoWuGcy76zHN1la-3zCytMk1cJ8nXwaEKQfPd6bc65jArz-y7-a06qBfbvpngCL_wanh9c63_5lF-eEfJW_zDY4Yr26IeFaEB9ZMor8D8tVKIMytHWkUWP0JmGjw4P0UxC0_lgb1pz43n8QuNvjE0Fd3zD2T4TwrK9-8gu3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/16577" target="_blank">📅 18:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6831709af6.mp4?token=ELOvUihw2pldPYsgDiEOrY9eO5XqcNacWuMzIB0tExqOmgLtnFhii0mBjOIg54GJjL_10V4HLgJjKFi707p2DcES_tMCjQB_zMNqZ02ScGYUaGk7dMumywuBUhbGyMW6rzAqHE8E6SPaxtp42nwkGXb9G08IlQbmByDW9F09tkaEHDz6AGpY-dTINnbL9WgxsvvIpE5IZgsia9VHLCixhusTBa3XQq_fdxve5tuHS4IsNBGI_kkTkId1iSmub7gbDRe4LmcHnjfe8tkHBp4MWnzFgXZLk82TDiLJFglwYtxmdfKGjgbSlzv0FBSCzMngF6hmA930BC6Z8jIGaMFi86GNPnfXXqX-mEloIlISJTL_6u8aJzPeR_ka0jNJZ55MW9vVHvbiFFSs6RNeCWNsgdzAvLLs-f7_uNtj3aeKZ-UZ4TC1dhRvg4wugX56Mx8g1mUtgUS0LCLcT_WOFK1H-Dp5M32-xIeaBcvU0HW3fTLSL15WSilOkSAnlQ3bYWi3Q5wUkO_hClp6_9CYPbP1YvL1Tjo55EWDLmT88hprz2RHY4UZOH8vYK74B3oUAWGHevkuulEcfMxwt9O2Nd7iTkVIWUfVbKrWilie6gbAfymLU3Ka2eJJtThVTZ5Pu2cPbNgiOy82_-qXX3Cg-S0jEh8LOxnPdzuLg2K3kbMOkW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6831709af6.mp4?token=ELOvUihw2pldPYsgDiEOrY9eO5XqcNacWuMzIB0tExqOmgLtnFhii0mBjOIg54GJjL_10V4HLgJjKFi707p2DcES_tMCjQB_zMNqZ02ScGYUaGk7dMumywuBUhbGyMW6rzAqHE8E6SPaxtp42nwkGXb9G08IlQbmByDW9F09tkaEHDz6AGpY-dTINnbL9WgxsvvIpE5IZgsia9VHLCixhusTBa3XQq_fdxve5tuHS4IsNBGI_kkTkId1iSmub7gbDRe4LmcHnjfe8tkHBp4MWnzFgXZLk82TDiLJFglwYtxmdfKGjgbSlzv0FBSCzMngF6hmA930BC6Z8jIGaMFi86GNPnfXXqX-mEloIlISJTL_6u8aJzPeR_ka0jNJZ55MW9vVHvbiFFSs6RNeCWNsgdzAvLLs-f7_uNtj3aeKZ-UZ4TC1dhRvg4wugX56Mx8g1mUtgUS0LCLcT_WOFK1H-Dp5M32-xIeaBcvU0HW3fTLSL15WSilOkSAnlQ3bYWi3Q5wUkO_hClp6_9CYPbP1YvL1Tjo55EWDLmT88hprz2RHY4UZOH8vYK74B3oUAWGHevkuulEcfMxwt9O2Nd7iTkVIWUfVbKrWilie6gbAfymLU3Ka2eJJtThVTZ5Pu2cPbNgiOy82_-qXX3Cg-S0jEh8LOxnPdzuLg2K3kbMOkW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : یا توافق میکنیم یا کار رو تموم می‌کنیم، تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم توافق کنیم چون نمی‌خوام به ۹۱ میلیون نفر آسیب بزنم. می‌تونیم پل‌هایشان رو در یک ساعت خراب کنیم.
می‌تونیم تأمین انرژی‌شان رو قطع کنیم، تمام کارخانه‌های بزرگ که ساختن، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی هم ندارن. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان رو، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این رو می‌دانند.
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16576" target="_blank">📅 18:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ:من به دنبال تغییر رژیم در ایران نیستم و ترجیح می‌دهم به توافق برسیم زیرا نمی‌خواهم به ۹۱ میلیون نفر آسیبی برسد.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/16575" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16574" target="_blank">📅 17:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpkFjkqjLE4ytASHY6ZW3SgDCIVFwMbsYHYLKb5vPSSBG-SMs-Os4jp3xn6_dXVYEI55eFeYWp-4imChxgGeb5kiK76KBYvLNWeylS4xAZqG-RXGFiri8m-5YodcmWyZIkaf9CBgIwbr6SXLqw9O4Wt7sv7i5QiGLOC_iKGJmAjIaZOKRfgaijMZ5Mx7w8z30giLuCZZ3PN0EayJCnhLG-U6p_WNuHHgmm8uT4kTuiPdF3FImYyEla-uodETHCtg4kw4kV_LRqcqHpbjTdCW_WjD9QBHybgYcsFuyqvfS1lGkGjgMpAbFJo8FcH5bi1aFk3QROMcsfsmhMyAKuy7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاه وشی این استوری حقیرانه را منتشر کرد …
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16573" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مجری فاکس
:
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16572" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=lB0StLSCR-8TnbaNCy8sf9EDVleh1L8YltwhVIpd-OdhaZMFkoZyW0Aramy4SMHLAQKLgmaetW1UTwTsP8ZfAac0BYIPQ8xsM_uKJ73vmraOsU7xrDv7b4duyP3FiJEJn8pK_PAbCVVBMWgbM9vdu9I_9Wpqyi4JXJHwSiwbpI84nEc2IBJc1wax1OR5c-dD7PPpIM-OrGlyLXb1XARIIWGu0nqp1fnk6A79ICRheL-70FjvxAYnLnyxchz77rPBx8FTuwlzx2awgyqpKZhSLneh2DQX2T_uo0oZXaynGUYtKgW75wTNjzanB9b4v9biaa26KeY5a9eNPu61MXG0jxwHgKQS29cr374OwHAN-l9tcx4qVN0_lMHzVWWtTvb50yBovwZajy6YdDH4cARVXGM5mvHsbuLWzD4COZKKhuBXhwfS-qBaFnlVwrgEbx1mh85v_wGKoBjf2LvQQz4WmfMum_--qDMyXPZyROKZ26mZW01kOeNwNVgEinPNJMofmDO3kVB8Zjl90xhCIu2O5vtPwvogPS0StHVk6yJsViFkAj-S9KhzsZ0Y-rBuU0ANep4gbPmk9zt46p1Nu7_wqDUUQPzDm-cMv5Xpp9X_clKoiLd6NwywPhA1UMRCndYaAuc6QUN_4xeiIcU9GZAjCY8IsQWf5EUqxOASNR7GlRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=lB0StLSCR-8TnbaNCy8sf9EDVleh1L8YltwhVIpd-OdhaZMFkoZyW0Aramy4SMHLAQKLgmaetW1UTwTsP8ZfAac0BYIPQ8xsM_uKJ73vmraOsU7xrDv7b4duyP3FiJEJn8pK_PAbCVVBMWgbM9vdu9I_9Wpqyi4JXJHwSiwbpI84nEc2IBJc1wax1OR5c-dD7PPpIM-OrGlyLXb1XARIIWGu0nqp1fnk6A79ICRheL-70FjvxAYnLnyxchz77rPBx8FTuwlzx2awgyqpKZhSLneh2DQX2T_uo0oZXaynGUYtKgW75wTNjzanB9b4v9biaa26KeY5a9eNPu61MXG0jxwHgKQS29cr374OwHAN-l9tcx4qVN0_lMHzVWWtTvb50yBovwZajy6YdDH4cARVXGM5mvHsbuLWzD4COZKKhuBXhwfS-qBaFnlVwrgEbx1mh85v_wGKoBjf2LvQQz4WmfMum_--qDMyXPZyROKZ26mZW01kOeNwNVgEinPNJMofmDO3kVB8Zjl90xhCIu2O5vtPwvogPS0StHVk6yJsViFkAj-S9KhzsZ0Y-rBuU0ANep4gbPmk9zt46p1Nu7_wqDUUQPzDm-cMv5Xpp9X_clKoiLd6NwywPhA1UMRCndYaAuc6QUN_4xeiIcU9GZAjCY8IsQWf5EUqxOASNR7GlRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎نتانیاهو به فاکس : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16571" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حماس: رئیس کمیته پیگیری امور دولتی استعفا کرد و این کمیته منحل شد. همچنین اختیارات این نهاد به «کمیته ملی اداره غزه» منتقل شده و تمامی مقدمات برای واگذاری مدیریت نوار غزه به پایان رسیده است. @withyashar
🚨</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16570" target="_blank">📅 16:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvZVyshOUuviFUf_dHYtQDQB5LE_3IMmnOZBNuiC0FNhOz-aUxRaHnGSTI2zlHheHURh06c6yFJc-h1tBFmZoChFQCxluSfbIUxf0Ymj-wmxbugM9HH1RBdNxIo6gMjLLchIxqQ6bjjnPJkLaY0g5jkKm_ghoEd4uS7iQa-7GpojCDSoN2bKLF3f2sr_nWbODLJLle-f-X9EwWEonzcWQtkFHI6qKxcntKCBoKvUsq_0d4zKb6nl6Vu_EO1GoFqprEplGUHoFdLrEuvxN5-MmTPH3K7ZLw6DMAIFGbsIkdVS44dXmuYtnqjOySafQlfgXpVZ79dlJ-snSw_9PlwFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم @withyashar</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/16569" target="_blank">📅 15:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16568" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=lfjAXxOU7N4u00kHX7tFJbIgPyz-mf0SjzPBHCkBrl0R4fbNrEgbv8qdlyNqbLj1juT0iktfelqzs_GhT10lHvfj8tNuwJp0-Pb20bZrIR6qE5t05qY47S5ooNfN9cw7NHBXwsMr4-510oQXultliuQZdz0H1w-sDt73YFb4KKY1iYqJ_8skbJgvsd4-Ozu-x4wz1psXibfZeYk060zPbhuA_wAdoozfcGTFIN-kd1GrdG8Sg1Cp2LozKpK5Kne_5xuvoiQIZQtQvhGd2SAiz8EjWvBG5cMoeU_1lmNNszOTNKQbyBCxkFRSEsB3Vai0uP77BzOM6cAP88XFstcPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=lfjAXxOU7N4u00kHX7tFJbIgPyz-mf0SjzPBHCkBrl0R4fbNrEgbv8qdlyNqbLj1juT0iktfelqzs_GhT10lHvfj8tNuwJp0-Pb20bZrIR6qE5t05qY47S5ooNfN9cw7NHBXwsMr4-510oQXultliuQZdz0H1w-sDt73YFb4KKY1iYqJ_8skbJgvsd4-Ozu-x4wz1psXibfZeYk060zPbhuA_wAdoozfcGTFIN-kd1GrdG8Sg1Cp2LozKpK5Kne_5xuvoiQIZQtQvhGd2SAiz8EjWvBG5cMoeU_1lmNNszOTNKQbyBCxkFRSEsB3Vai0uP77BzOM6cAP88XFstcPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه در مسیر تبدیل شدن به جمهوری اسلامی تخت گاز پیش میرود
: ویدیو تعداد زیادی از مردم ترکیه در یک تجمع اعتراضی که هدف آن، وارد کردن یک ضربه به کیسه بوکس با تصویر نتانیاهو برای نشان همبستگی با ساکنان غزه  است
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16567" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16566" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQyQPlTc7dyHZUsSC-ccjmxvY4se-96l0M9RXioqwKgqVUJNMs3GDWnnHy7sUzh-cr9QuTyzO5HL9Ih9wO5aVHH4ax_l-_6MxF94XiGnK-vWbjZljkdd6Y39f8wu7sT6W2AXQz6uepeiX7BDzatRgkbRSnXYXj8OyXtz91RZ9pwDLRjeQgtWoySsXOzjN2x6L9-blYOAOnqvUCfdC6oBXg0b4RoSixRwIkkkAj6XXJQuGIMMcVBOq5e6jfF0xRDaGqKQ-2SZS9LH5NC7Vn2Hl9T-JMr3SjBYJWDL9pKV6g8Pa3xZ9UIN6C78r5XjUSiFdZN8_w4EY1uEwUQ8TopPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=vEku68woJL8a4mj1hMyTx24xy6mgpmY7gv3xkJkgb-H0Ga5MkI08Rlkrf1lNTl5aJbxhZCi39gY8D0MlL0FLc5mpU7bsuwEGVOZbiYhMR_YSj9e8XgXDeQ9_Hp6jxOpWzWzxXaB70H2c2sq_r2MMELDR7b64BsSNfU4_66WgMWiVfXIdshwvZpN4SfZqOV1ZwEk0-IJWiA_rmNhdOv4oa0V-kURCs_-KNtuStpRlJbH0lssLD-5MjgTA8KBQHi65wOJwBqF04LUsY50pI3fvcZ4swdFZDtUFrw_xvjESuSUoJCAhwliHeelYS7BcI9GXwTQ_93TU1VCHO0nI6I1AQg9lAEjnG7Hx7w0V4IYAqloEgLxEH_9nuW2NzeRZ3QgEiWNmN_mE3_AcAkhp1yP8RRqkVMbs6Wa_wFDrlsYqkCF6NJC3hzmKGW3uEOzQDUdAKfY3ayZqwp8T9o2b6jGbGoqmkMmI_5qIX9Sw8lG1_JrlV8k7pKCtRIe7p-o9O1KIkIBvLQlgu63gf6vkBLoCLbLzd5O45-y9rdyawx9AuVdEHFf0a5F2NlldHFmPfaixFhP52kz783xuBQrXTaDyHeYMKP1XIDp1_kWUmNO9eO7MivnshCaPdWUkh8sfxiIMXYnCKNqQr38ZysSV_EO9okQIwziiPGjYlw4mPSHpkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=vEku68woJL8a4mj1hMyTx24xy6mgpmY7gv3xkJkgb-H0Ga5MkI08Rlkrf1lNTl5aJbxhZCi39gY8D0MlL0FLc5mpU7bsuwEGVOZbiYhMR_YSj9e8XgXDeQ9_Hp6jxOpWzWzxXaB70H2c2sq_r2MMELDR7b64BsSNfU4_66WgMWiVfXIdshwvZpN4SfZqOV1ZwEk0-IJWiA_rmNhdOv4oa0V-kURCs_-KNtuStpRlJbH0lssLD-5MjgTA8KBQHi65wOJwBqF04LUsY50pI3fvcZ4swdFZDtUFrw_xvjESuSUoJCAhwliHeelYS7BcI9GXwTQ_93TU1VCHO0nI6I1AQg9lAEjnG7Hx7w0V4IYAqloEgLxEH_9nuW2NzeRZ3QgEiWNmN_mE3_AcAkhp1yP8RRqkVMbs6Wa_wFDrlsYqkCF6NJC3hzmKGW3uEOzQDUdAKfY3ayZqwp8T9o2b6jGbGoqmkMmI_5qIX9Sw8lG1_JrlV8k7pKCtRIe7p-o9O1KIkIBvLQlgu63gf6vkBLoCLbLzd5O45-y9rdyawx9AuVdEHFf0a5F2NlldHFmPfaixFhP52kz783xuBQrXTaDyHeYMKP1XIDp1_kWUmNO9eO7MivnshCaPdWUkh8sfxiIMXYnCKNqQr38ZysSV_EO9okQIwziiPGjYlw4mPSHpkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16564" target="_blank">📅 14:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پاکستان آبزرور : احتمالم میرود برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) شروع شود
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16563" target="_blank">📅 14:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">توافق اوپک پلاس برای افزایش محدود تولید همزمان با بازگشت قیمت نفت به سطح قبل از جنگ
هفت کشور عضو ائتلاف اوپک پلاس توافق کردند تولید مجموع نفت خود را در ماه اوت به طور محدود و روزانه ۱۸۸ هزار بشکه افزایش دهند، همزمان که قیمت نفت خام به سطح پیش از جنگ ایران سقوط کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/16562" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOFEKeDRsRuKBhP_z-sqAINhzEhfaPaf4F7i6Ntsg4FeuUewTwCtuM7DaoR-O9y8RhFYGQEmHvXzSOLqMFc0WKv3_A3AA6xtT2nPvtWI2DOlAglbyOLsdSqef6IfAZjEOGqF72m4Jcj4T-iidXF0HdjL5ymh7uK3eC9PGdUyB91a1kkfHiyDe7ilOFB_m18DQwCV093dTCLEUk2cKJvWr3-NmsZsReMPwwKkjaKoQIiYvJEtB5C76D4pwm_kR_fXKiqJASqbhMDCGtvau-ON8FQ2zEfbjo5NICVQU8yQRYhjeCTD_-J8BAnZ6r5GRACLkLrXgMXVmJa3MuX5BoD_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
@withyashar
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16561" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کره‌ جنوبی:ایران برای مراسم وداع با رهبرش از ما دعوت کرد ولی زمانی که میخواستیم هیئتی برای مراسم بفرستیم به ما پیام داد و دعوتشو پس گرفت و اعلام کرد حق حضور تو مراسمو نداریم
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16560" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-ai5c0yehyNIO0vdiBP2Uo0wnfukTYfRv4vUFcl5t9w7vGW_7-FSK3Sbg2sQn8ZAPmn3l4Qyr4rWAr0hjXGr54Sql_u9qOuz6PkGlzGDf0klzMONrWsJqFdAn92bBoT9W9XL3npt39pCH04WvlcFAo_L-XJcqHqzyRFSTApZoEhTHizdsd_yoX83MQ1LbxFSfKra9vOYKbF8eyLj3pqmik6DGeHGjfMVJlcA7mHmsSnt8CHrY85L0BB812VfcXhF5bm1gNP6ftGc_HvlPvWmw2Z_7deAo-Jjaabd1LPIzmvpf7CqSFS0JexUgQQfSvds3UMrdicFCF2Zmso3EGA4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16559" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است. @withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16558" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16557" target="_blank">📅 13:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNdfDfT6lMsjjrt6b8uVv1U1Ze224iKrGlN4F_0-6vaTKh13BGzPdwsbUmLf_Fso8W1f95AtncLBw32-eX1cQq-Rigz1Oa3n9LVmzRrBP3e7iDtUjv-zXG2fKg5k7rv9d-q8nF0v5Akr0MMLXrOPCZv2-ZfKXLH32vmyXmEskwxw1tsTP2vuaWym5_fsgebnupxWRUiQQjvXzFXETMcsnY0oWOKdgMjY-DvwtS-fQLTy-tUtbjCRlGy3-U8DZKhEmkS3nRMuM7s2J4gSZiK_hLnR4yFvwRrR5WMoGrmnp-IT0LLAmgiriI33BdsOx6E6Tq04T4RcnHGT1B7oDlt5zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16556" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
