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
<img src="https://cdn4.telesco.pe/file/Sz23KVtTVXotEPb4QFZMNk5g97-Lgi03a478I0RpPYSu0LQj4QuCruoLgjWh6vQkvbixXz7cr8jAovn5kcTQjubUSEaiOr7bEjprpdEcpT9N7qs-0I_qJU1keZmUcFjsN_72jl7PYAL22ogRg07B-veMTYCQCIfN_Jy5BhNbYXtgAblxtONaFCZ14K6awQSJZpb6QYboiA459dAWGH3tXx2iF4H7Apsm2w1LX0-sRWjOjAa3OdaMLIlEvuQYisTFGQItuUiDBXWfk_trTewGKdkRdF0gckDEKj4Xzs434WzrE2IB42CvI8gxNPWdg_RpYcBakj3d_fqmTvBYslqgQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=myOdUZI7zbPuo4IPwo26_ZXDsdpP7dKL9Jf_g8GyCF1ZH4CNjMwzS19r0-zz7wmuP-wMU8xYrepAC73qIDcMuSCgO8Q4fWRWACk6aMIjgM1CN-czPL_JEQZEoKWSGISalNyMsCQLtdlh7S0oilqZ5NiH4g8oyhOeo0l7iu85ZX7O_2wQvG2wmjQJrKLzLHWF4_CF1hGnE_WhzLWoF1GLQtGMtIZwv2MYInWYhZ-FVAigDO7MMNSdsE3NtgLuaV70K-tVMJKGGgpk-1BojlBE6b2PJTV6SZiIE_RbJE51pewLgcAp97sosrtiwDTtWIXC8fbQ6q2DiziUKzJYb3W5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=myOdUZI7zbPuo4IPwo26_ZXDsdpP7dKL9Jf_g8GyCF1ZH4CNjMwzS19r0-zz7wmuP-wMU8xYrepAC73qIDcMuSCgO8Q4fWRWACk6aMIjgM1CN-czPL_JEQZEoKWSGISalNyMsCQLtdlh7S0oilqZ5NiH4g8oyhOeo0l7iu85ZX7O_2wQvG2wmjQJrKLzLHWF4_CF1hGnE_WhzLWoF1GLQtGMtIZwv2MYInWYhZ-FVAigDO7MMNSdsE3NtgLuaV70K-tVMJKGGgpk-1BojlBE6b2PJTV6SZiIE_RbJE51pewLgcAp97sosrtiwDTtWIXC8fbQ6q2DiziUKzJYb3W5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 206 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAL8fZVN4RDu3mKb4sjdgMWaI5j5lUSxXxNEyaG_ikMeRMqlVGtmQXR3gxi2-lysPSuBG7JFR-at8dTdIjaI8puQcjd2odLBucnzDIyiV6l7GZpBnnxlxKw_cm3fqqO8EMZ5rFlQQKzo1NmwA0TmTBJBT3ffpOXitrpvng4N5d5n0zU8T42gEeCl3-wfrxoYmgiV5XgvbDOV9gt5z9C-fK2FxrIl3yd9PuyY1rT7YdL1mdn73ML6ZLbhy7UYj4zpDSasZBO_7Mw7Rz4unmWn3UGjO_fQar19QGyRv9k1fqcLvbsKJXsNXZZ_y8c3pp7JOFsaA3IMBcwoOWJg_LUgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 330 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 552 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3UNmTUujj8xK5RlrCveszINJdqZuxnZ6MLAVNJOWTQ1DVaagQNNArRRd7vISsaQSk070tGDOcO2fkRexuP-EqTSww9-O1HJdNG_otghEMSa57KOTjVStUO_2rG6ASZG7LhFYQlY4dijGbaugGjYvPXX0ghUuKxfcuj6H8mSJpglqiYM0QsGh2IW6iz0SAJcxmcxRjovg92L8SlkHi6FcQV9XWl9R-vB0Jk6eeK76oeC84SjQ7XplCx3he6o1Cnjte9tfTdW1RgHUwcpZyhfGHdoXyiZ93iwKVL6AOzOR9-I-6Fr7D7uU-JgdenZGLyUk_p1su_JrhNMno2a0Pd0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 792 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJe5l8doY0JqpGK4WiO-ymkRlfSC-teBGn9D0cvc9ak5QVVzbkQqAWL-Ucly8F2wqRU5YABGiAq7vieRx1TUZBYYKtJ5hykRAg5WvJ-5m2P6k6p8JeCdoqtN_F2zIDEzQG5JVL8zau3UtiJW3b3C_Y8PgCxIZz1pjN1_2rJakiH97uLQCHqOjDmAES9DiQOAhzjQ_L-R8ZSWuEuRvYLrKodgFLGN5JucQv72_B9CNjtdvABJ737xemjYzMENmaIAqvEcqSnZzUD2Prtde8oZ3G2uS-H8fmyR1A3QF8-4mLaD_XtFl837B1-T9OFQ76BsL63OR-eswJMEmnFIINa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGaRX_3F_S5Q4WwHtHA6-sQGZ3Y1Zi85521Qeiydzo5JHF_ii5dDOyaIk6Q6XMY76cb_lAi82b5w-yZ4_m23iA6Q5hcfPX1snTmVpWx5k_yRmW44zuqSBe8Yr64v00n6bOFYNyFAOLjSDgMACXgcD1FgkUreGpw0s7nnx1tIXzd3SnRXdYN4H8ySnlETdDlJl4fFzxNTRWDLPEnq6PLLnVGJGIdjVa7ygLvXN-tUGOS877etOmdoGWJ6bhaREqJoU62cTtU2ELbIGFiN1S8AekUuOQ-6UJQ62sY6UfWY9Om3MIP77kqHPiIQdgI7s_R5Z0T6iaPqk2pPUx52OabvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fhs9De4wPQnfUfexl2sCjXWX7HoIcpomFR0aJNa7XOJE60KKFH0JXAebwJTIBjldXcyn4_R_rkKHn59gx_4tTv0HjuYr-pB0AuhaIZU_t7oYtpyZklNUW8jTefKubwZ2etazVaZXu4-qIwHJillMpu8z1sn_QYBwP51y7JJntHFcVqzBLpOCfWrgHQww9UJPcHzs17xFW4myOYHwt5jifpJo_5Mh7alvwnBvQabxE9U8ibxKld4PDFmlG3m7w9DgfHswOF5s15vo4wSfuhI9FYG2AnZXr-Kocv1xYqjtbiRapm6pOF8-VBIrw-mmZ4q8ihvA75eBVpr8hREmJMa-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp2pwvxCSzPzM60_vDtAw8lgpxWvKmgmMBYHzdrO_3uS2n8QXqEwwXdMBuyC-V8jk6JJy9gBOXxIUyczK-UM1EMRWOOhYi9hbVD54CyB8rBmGQF3KytpEHogGbcOJnEt8nyfHW6AWFsm5SrYvFU2pkoWO9tlCeQ8rEnA-2yaUREcVzwETSAXHg-uH6O54wW7nFu_j5SX2XVr_mPbxvq3SrJIVaaF_HIgaCPkRKncJu48Oohlvs0SBm1qFRx3SfQgnJd4nrg97Ssrzi1S6L9PMzVBx22Pysr-kDNpahRBLSQkv94C_bz7vdYmUsDofhp0WvegyHYgCV8wgUVscx5bsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeXu06ViUTN7WxTBjx7BIA2h9O8wcLVPAKA5nhi291Ayhjda5jXOU-VfUlH3i5MKAh5WMnA5MFJ86TT8BhLDYFboQtjeDrGxTV22_uwWYp0wy_8_2DVoxDfnaYf92cOOB7hgFUedfzNMbGp9Ki9lBEfPNeLBS3HMobNNfNSkYENE_HyWAkzA-DEiFRQGdkoMkSsi7pj4hQBQyCQqLhigleAn3bhOLbCgWdvyrt36uGuZxyGLpdChksUhrsMHDMFeP8_mKzxOjDU-JSN-Q3l9CY9k9PYaEXjTE5ouy3o2hqdgPuSjO-xWnCnF9kBVyptjTEvpHRpEdGBlZbXVQ7EKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIhCyd0xleY19ibIve3HvJ5yUq0IwAb56RtF90-UA1oB_d0LSE3rodnGFimCi37ncG1BusihMV5BmTBc4UfgPefYkQBhEZH5qQKgzYUcFuOApqiyrIH9oAenn7AHvC5UQa5_8sl98RCNYrvLrD_iQsI0f3rWbtWEzeL-m3p5fzh8jW0pEEyw6KScAo19BQjUR2dDdIoTUeurhUdpmsFp2-eV9XqOWr1cwyZGvQzPqgqeqaSSSeofZnI5ffUFgBWMPsRsaS0tTlUaISGxnZyk55gYL9b0BFVykg8FHBt1r8zye-7w1XQERTRbhZsU_mH7Ps1sswPo8EpYtNPJuMikHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qih8V946eiaUnHsTuMZIL9PEiAoAtOZLTezKJ6YRF8irG_3G5zWYR26Qn_q6yF9iP2t0Vzp3lzdZaC7Or3Swjujwy4a43gC71zoycgdjMW_-FLgaqXyiOatZ4PI2JBQAvoKD1EXqhdf594j_X4DKGE8s8-hh7m8E3vS0E5-yqEnM_v-1E-uKrFHNrGGxt4yQJLIrMY892Fs3ilwVG02qCl9mPFCaPpGv3wJWAwUquyTGZYB2cxjOmeNxqu6vSc49NU5dnl6ENs8pDlNx1NZ3opbqTjyjjqxNPnad9V1FJEm5Clwz9mud2fdZCC-9_SzRkvMRNHCDzRmVmPNjxgzYMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I124eKBKrtkU-mC5gXuG15xuwW1IHTXUZYUsAhumeaH8PVV8_gxWACJnVrxbsn6OegqQEbtESBlHCAlebZQ1K3fycwDGyVL6q4XLMJ7UHk0N2FCF5P62pP8ZSlXeWMPUWpRDdW5s7xC2_bGKGHiVIpONGB1I16M0tiArHeHGOt-bDC3FnrhQYfdFwUWKYomO9P2RD9q38Ttknr0fKhGTL0QNkRwXaXK0NcfBnEzjPtNaIFLSWQAfUAhRaKgc_efdAF3QEOTPn3DJhqPTR4Q7RprSSC_5SmGVEuNDvkB79wk1qx4hvtQ6RQ1R0h1VDeBMHHycd8UtdNI9QHkz6930lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqUpH3SieC-yDQ2wb_3fvW0BhutsJ95l7DcFwOofxIMM-xvMR2DWTKxoL2hLa958WMSeU_Jb306Y8AttozrQVEOdD5UNKSZyBDardYERqu0jD2-izBy3jgDe7OlFMK7cWICd8kn_-XfZJwZNQ67vXkJg-Pe026_3kPZen2s7-NWeMwMfKhFiU-Q0Fssj58xuhJtQ8oRzwWb8y73-Lcn22w6JWJ09BB9OJ7tYG2Y18_HtgcBGBIv1hzOJiGaBSCW9Vqo9q-WKvXRN74mc-mLx4FDURR8weVrwPcYhqMyCct_O1UeONpXoRnHHz-8QItZIqNnQTzB1vvJFPD9FpNWayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3De76MXIEKs-Xiog9-_SJpu_pvJPorp3UoDx1MPQwce-h28v3_enI00Ng9TEXHKgMzTKsLGXI2ZtgdayvTtRcPpk2UMEd9JUrKtecDNKz8LSq2__OCODwx6Ha8AlZIKTJRWmzbT2byHm3p4IIiR3Hv1u48FwHVn1lZrIN2IzZ5dfMpvoQ46SjUIztQZqivfXLf0flDf7N0xKmEUlvvaJ03YZDXQp75As8R0f96dWXzH3PF6T9ylnw8oVuzROHTRcpmQKL2-RXiV9h43Qbj-zteQ2eNeuhXCKoKLAAZJ8ptJYkpb4RtMhs_Sv7C9BE0pXR_B8OGL-PiS-0rYPTv66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewf8prXX1b1Lsq8yfGZKbnsTxYfzMUwGS-BOilO6eURzBMvHoTLeW7SXpVY-DjkuKGayMaxCpfIXLAgvu8lRa6lAUXSdgrMENC2vYOJkHmZXgsZy4Dm8BruwWsjv-JihneGCgFMe08jo1gaOpK7db0_NOauVy9UZ_wAd2Dv0VHHt2sFFKLuERV4b52vlmuERe5Nbwj0_w4uHkbUeI9hKvcDwKvq0DfnL1tgF9IQwgwV1cLZ2eviRFT9OrnRuFRFMNaWiww0EgcvMr_50-Essnv4pMkL54a6wwgNa_NbkUl-6Jsp2YBqbJRnvo0kgGfcgnBkXTsV8vUqDP7Dvntkeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLAojIVJvmYOFL5vgVCgwjK-TRSU7df-dmiCRHFkl_0pdkcd7g_6f7XJUBuGHWl1HeuIgDlbW0NiUB1xrhR16T-M-Cs1YYCJTL0X31FKu6rySuiSfAOVtMOzLJyBGSwGFmy1j22vkVk3uLgxI0HmCkDE5HbF0sbGBjRefUp_pnVMb0mAmpspfn6_Ou3PJfJIdvmehbPEqXnJkIDGkX70Az_4gO2Z8WLJCR0SgRgS-Y5dyi7iX1M2i690N3mkMzoZiifPz7YjGrL5ZoPCOLLHWuHSO52B-Kh9xEGZ_wixUKj-KOyzrMO0nGLnRrIcLvxXnA1tJrSS8ANS578haqI-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kn-3JzBfJdZPGc3I2S7WGUXUvVzwM-rFZWHlpsOv4WfAzKvEbS4wUtDwYmCz0Ed-NY8bak1CsDf4Nz_Yq-bCszyIKEXkJMP034hI6udL4uC2lWgVqm8zHE78GYLSeI8wsHjTk4tSY8iAvswKD3Zeyffspd_uxLdRhAkn2yxbroyCMKN00Ine9mAtgDqSxBQm_ONvSsq8q-q6Zl3ej5AlESmzMc2gBM0f1wl-dHpDCAYCyozPSimQhtJts1EzOgpuKzmG-1dxVvlPRE7xjFb27e3nK901xOxrWv0-wzW3-qVKqaBNLcbzqydTEtJMv_ywgFndaFe7kXhgZm2PYB8OUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-51FA9EvTR9Id-sgBofdlSr5eukKc8ov4xmylXjrKj2nvwChIFWHlZK3RzPZiVNccEv_cqmxL52x7x0ln4jvRI0IoEVmzXC9JIsn9jCzqVVfLJcv-Zscazzrp3qyWSrXHNsFIfkZdqDRE9oEV7Xm5EJ7v59JjKz9eR_hRp3J9R7djL9dH5K___HsJejvexst3S1RZ-oRpWTAzo7EyVCiEw_9EJOhSPFaBVAtTJEIj_A7o8D_tQD4QK7HVem7g4AD1lrcuWmZKra7ht2yIES90uuF0IwrnHF7uDP1V-8yh2MV0KmAEHDHnwPf9pd5gP0pGobnQNGwccoYI_xThN_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5c1a5GXTeG-c3vsFfJk4wm6poRoP-DDGxOt7It8Lcqz_fEp9Lb5WAehQk0Zr0BtjgCrK2dTT9ENFmsAKx7SvzC30NOizSM7ZPE_3g8xBV2pbrsuaZ2pkfLX9gwdjL0LHGS2Dp3yzBxm6r3lSHuFJlkWTLooWAU-dOfLI5P6jf2FaJXoq3gR9Ybwg9tKG9K1KsmZtjHdf23lUFf2-ZuCqMo7HCf8WUhPsr8mziuuppVOMgdtWvn-P9wvwA6V5YVacoR6BPOX-ODG5DC0lM3Uy9rR4vmpRz9eDhJy9mkvcDqAOf-osWx8ohJcmbx3i9fWzlnFBFo6EE61Tju2V98g-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hH0NOqcfVJjan69i09Yrqfz_O00kFZM13WljpynfTB8T5vgEmk6D7zrNWz5BsyKAA7mzyp2YQOzCNQ2ow48sGi5tIkyl0mW2Ss-z8CAJggHGWOdPXcJYaAME5co6DRVSGbCF8zKycXfkTTrfZ5jWzDVpp_kphIQv9GfYXu0bx3Kxmn9YSv8QMPUXceRfpj7i4K6YIqAPT2b3zkkrydINVO2YRiTul4GLwOgs6hMPN9nSnG-y_gJcUqVV_IifsOJETZbnq2DlEx6VoxqOtEFsrS_LT1Vdg32yRR-3eYT_qYivtdpDGI5Ww_Az9Ru5b-lNjEOdovWP1YTjemAjQn04Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=S1YjGiXT5gb7Hba21glaCYl0Foen0BIb_go_EJvFtuQmKuMvftg39fWYx3r4y1G5NzFRjXl1ZI0sD7b41TB7Ujxkl6rZHCCeboE9QY86RS5R-FheSbMPDB9NTSV2U51KXK74ugb-Rt4mdxLvb2HBb2wFf30z_G1ewdPRPgEq4crcDq0OL6idC375tlgAjAGKoS8RUD8p6zMeaWKlvx0XjG_4CUuskPHeiSslxtDLm4_INLmVEt3VdWgHw6FV3M-ONJn-L2p21s_ETdDu_bzEIhWmDm4nY1MYD949eJBNYY-yxmwlftsb5BdMRWUYVOXwFO4NL35SJ9P1FZ3QMmx39g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=S1YjGiXT5gb7Hba21glaCYl0Foen0BIb_go_EJvFtuQmKuMvftg39fWYx3r4y1G5NzFRjXl1ZI0sD7b41TB7Ujxkl6rZHCCeboE9QY86RS5R-FheSbMPDB9NTSV2U51KXK74ugb-Rt4mdxLvb2HBb2wFf30z_G1ewdPRPgEq4crcDq0OL6idC375tlgAjAGKoS8RUD8p6zMeaWKlvx0XjG_4CUuskPHeiSslxtDLm4_INLmVEt3VdWgHw6FV3M-ONJn-L2p21s_ETdDu_bzEIhWmDm4nY1MYD949eJBNYY-yxmwlftsb5BdMRWUYVOXwFO4NL35SJ9P1FZ3QMmx39g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIE_N6CVXfuBpYr_vygO-XOv8Ki-91dP-Zl1myQcmUL3ugBlKWsws3MPC1ymvvvX7eI14gv_KQAaMEnDyKDeqhTK8XEBoeLNaLohYeBexv5grXL2Ah1aqLhDRaTYUqdWyhajgzRdmRBGDbUQ-6ZZivD89lGZ5S1_as-y3PQmb_yVk5aZiOOLhSU-tu1RZh-3OLrwA9iqeACUdz8WrSAdqXzYLKeCWVs4kLPP55FmxGGMY6hcpbTFoHwK_BvAOdeT8KULXeKG5Yzm-S5EHqnOytPa9gFyUGB5mloDJTzRpo7FQosYoxy1EQsqNyUkwymJrVlYi4664ZUHJkF4DpkBMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fku-SAbkMv-MLgyt631l3zUj9v60tIS_R_2xFpV27liQmPeCCpBsIsEwG5eQQ8LoBAXFy_WMrA--WcGg9Cr9xbOSPn4GfEsS_I1yNlXr0mu1ZDexFdR6VmAixZJiPU1g4Qd-Zt2eLHdyL_UjU1fsYDQWTQxXl-ud1b9XWc18rv7lNqjfSxpkEwcPTB_NdKlgTk_InmBKk0Ziy3FHjaAWyViw0U2EK1iouoasZBxttV2el2kKlRdUnOM7-O9JnF_vlclutS7sW9vdYrGLOjWJv_ImFNT3I68aiVFBLUXqhqUD1_KM18QanUKg9vp-tJZhl-jm-cMB8xfsI1_lKUAxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIBuhouHKzgg8XG_ywY0qYR_g6hb4obzfC-gWKlZS7IR2LkdNCImE61cog0Ia79muFrndaOxGq6j3lYImfuzuQ5jTBNY8kdrbczf0pe-z56chYSVMLYALQ04hrxMSuSDLyY3_BnxIS-CYPkCwEXSPJ-qcXSD6BWhLh6JshfMgD0f6XHvouMIe6VXfyj9G2KGHyJJPX4Tmf65RXElEO8_eu0YuTLR-M77GhxJ2nU7AF4ufPhD2ql32wy69A7Bj6ShBgKkz5YaEa9WE2VPYjaFxG4HJCPSEQLl9mQ1g46YMMIT8RTdTb56d2VQsgbrB_9V1EDekEU9OT1xbV2EeeapxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCdRWr8vu2Z6aDM22e3SXHCR0s14ee7ChBglAk3w8WtzA5r5SUKFk-Bm5KKlmSmd1ZOjUKuWblMT7su3xQfPaWZib-FJpT5qBoi6IUy8Iumf6JKZ-Lywv0KoOrSd9IhsTV3a2Zcj1WJ2kqTnsX587IhAuDrC4UbUaq0pq32JWHWzVYL66rpKa3FjPu7hqox_UFBfudJ2R9FgPzoTGamMgwVKEx0IvU9kT610Ovf7fe6SEr4SYZL4B6drIvbgmxt7sgawbPq793fqq96LOPtZkZetHGuMQLUllx4dBmYBkl7_-6Jy-T60NprUIhFW2ajW6QeHNqq0WmSq6J41KJBkxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 797 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZc_nTGCejN0PC_LnGGCM4n6glNzPQ7K7Eo5rwL5nDOvcXnBNjac7lbPgF_bwMHrB_XVLRo0R-LyGFphq3E_1CqqxAQhNbOOhdTU3n1egq1PI4uE4tpyC8G6OkQWjWgw8mCuLCzIMpWNfa7RHmKhSsJtWIX5nU5x99uiIFQS_V1HJx-OcwkoCDjk9eJfDdbUubEfsrLoekKDQfDoQkyWfOdlon4-o0o3AAyJeGxKOLoHMCGL0Hmc9XU-MRTXKGudv6dPTZCBdbTozgPEMD6ozJHpfYQGrrbtXOk3zGkJeaNHxXYaHZjlL9sQYr3r1GVoLYd7w4PxPkPWk4LuiwCBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKOCBB7Z-ch6sPXOu73iZ9oY2DzZtuJW_fcLF5Ts_DGSZA7p-WBcMPXUBmAktCmyWm4rduiVpUVae2kDkgRn5bfCUAclFUDUrD4XoxRZ6xK9sMlPyRpz01jDngn1IJHHfPQiRbbIWVtNh3KbtVjm6ifDMmEO_q0HtStJ-BcQh1VtcnpEJ1tb-6WIRxET94syhdZ09TUgI-iYz3l67cjzxqw4Ff-LcO9yZmp0InLu0XroBk6EQQsNOuAg0fh37LX0hSNwxnxMDe9CQjU5h6CleE86RSoEPvu1_vk8NnC3Cu04_6v1TuTR6tR39REsaZvVkk89H-VlpoaMwqRhFyDQow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7LewoI6AFLBWGS2lo3rMnlyaKid-dj6wzKs2hgibH6kZO77pxs2A9--YLWDHI9NSiZ23Bvd8_k0aMZM9MNYfTwUGNSjuQsnVPaR3xj_mNyJaMbzAVcIL7pmI6s0YJczQQpmE2OqTeUIPoD0glwomavRs8KQDWnZIT0OIyS0ilAZhXCcIn-PzhRaA-g9fs4ldiopDgdeFMUuLd4rOtBp-IEzaUNP4dWsr_BHsTkVZOxLosplWFcxAZpl91xIg1ouBHnwrrQ8TkYRB9_WC-I8U6hzjx82MmlpML2sI3s1GbrF7NMa8wd67rDY40kog2oLq6wek0Ewdl40lVpcDuC2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDzr3jcudI9JBxiXsRf67PqVRSbxKx4xq7FdhUUPUu_zQuW_oQsWyqCVuH8DbktQ1vxNvP_x5OVp2MskncKEhkRL5h_MrjtOz51ViYI_xvTp4JZnJb4FZeLrGfhqexxqf7wMGQDzW9TlM0JMCs0ncE2ghMJEownWJHrwHm5Dx5wKGfEpbSsfplbm8XjvHYZZcvp0iDpEejLk4UNI35r2L2Cbh0eETRA7s-FMiO30J4zfLqBiS1932lrAvjZmV9roqzC4zToqHt429i3Yo0sfMZRwb-6sO98rPqGs8xyZcy-H2kCuzH6osnCaD4cbwAp8eLHZbjcMK3A9xEJeg8CZtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6NC1KzzMm8UV2UxcqDe1rjmhY21gkYBzwcPTxhn_k400Z3neRsPSLwYKXGZl1O8_WZ_mpo9gq0iFUdFdejLEYeWrSsKhVhRT6kmGs93b7SoQFFwXTWBE0aIPzFe_t2AAUsD4Z7Vrw-sY41hjp2dkIdR0rmMFKRCch3VXwh3eqb27_CSq6T6lX0pAxb6d6_ZVdujGpbTJCplEOmiqIlLMA2OUfsF6M1iu2W70nDK0Q7s8nCDY_MU3jyMPM8hVUmfA8twdRoWIzWsCcxjxIaOjvE6E_E0gtltIQydb0cUjsgeK0LBo1BEneLjAuTSfYurHkkzbzlnGdL0ex1h7WeUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 660 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 808 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 719 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maP-ufjMXZMEA2hIIZveJm6fyxeEBkKDn3Au6IJEqwm0R87Z7kTVsI2z4uHnpFo-sSYTMn3hbMwEJIOlvzO6oxMWdGHsx2Y69j_E0YgeQxiBB-c4jqi0Q0CEgVJ_-Kl8A4DAcflm_X67dc4hnH5ZFgq0OcaguE3PkXcPZ7-pbxV2CShpwZONzKOVgDBgDeZm-34ZTgIvl0XjMHZCxLaxfHRGGbggJmq2r49vTxx5WWXE-7osmLVSUvxs5MMsrwo_myCCDiNwkV2cbP1oHUIU9Pi4oOhRhJngs5gntAo4EZ6ZfNb_bWEAd2L9KkJi95xn6zNaD2SpTrYvtmHm4B2OZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHmOUbMrXe3UKi9s2ppUBs379ONi7a2as3GYJasU-UX5ZUpsZGL1QLkHRK-RInN3KAYMmgTaf4PeJm32VRr_F2UlV1Nq9XSZd_AbX6pBdwNPw0Mq5MFPxNsROvvNRMECL9vvTPjzBK79QXJ_nESv4A9EfbEhOoLnwNAd-G3FXKqr_mKDirbO_J46i-k5cNnuKLnGtTHufERFpPmQwyGId2K6fUywk3wkQa_JQXW3lM4UNluAxTef_-GNj3_Woq9rCdf1Gl9ZeHz_AvqQyal5gJ0Ppp_ZWPjLCT6DFEG496_of5bYdLDHH6b0V_gpqWGk6tn13y-3SNrQcWeFe1x9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUdKQBBgIbKf3VUF4Ii7ceaOEspNPASv2pOMy1dN82tRy0_OpT01EnFox9iqwjVlR7JPRQds5RJKkBbfklrAAoAVR2qyK8DB8LymSjAgi09s9b2CMwUjgHRea_9nr8xxZBPWyS0tf599NmBnpbEjzXmAN2YF9lquWfJ9lngUybyLLec94FMyRLZrpjQ-GJrqFwkJE2ayzvIcGFgjXwvPHu7IHZmaRoDKFwKZ-0F0oVF52DmxOwTVnSKui7ntvCNT--z09V7NPjPsOsLijcUIiwOdfIWgp7kAvtd5V0iJNriW2Wtt2q78sY--dx5Y5PpOF3A-fhJGyDyr79ddlcVOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNjIDWS20uShnxW-sjbJPjrO8LxgbSmduYIJCwPyk0NLoZpYElFb0aruO9_QwNl5zZ5sujbJFgkb_a0RJJ4nGYep5Th20KqbRxXOvIQj2OAw3mByR7RHqLABSQVJQ2SyEHZC7A_-BKwjxvztu97Rv424wMnDI4A9nW7SLjjn4gVmXLk-bEz1qGzHF1Bsf3013K57QUipqXUQ-p09xEgL3kjFolF46h6jEOy9PT590AOfBuZlNf8c9fndXeryiHiAjTtLbVuoV-ITZZD4UCojgyBlhxUIN8Loal1JVhzth2DwPmeUVbr3eLYwlh8c0WqwhkmWd0MJBNpHTpvtCDP2mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcmsJEq8foELd1aTi_94Ir6zyOQANt0diDa-OgL1Cw3bFduppOOcNun7oQsCs5mdWRz9VuLnOL8I3zcbN1Mh5TWQkfgmsWizkJ8bJjQ3usjOQEGAX3RWiq2gdXYFG0q62uWIJekxKXeWLDGp5IRecRwniS6zXN8iSs5x9WXpjWYhsszRQDw4rOxw57gjJSpPFJA4bC89A_NqGMvj62lOHDKftjsKCtKy55dDWSfKVDz1tn6izG2inGS3mZ66tZNUJ532bnJzHx1amDFgCdj0Y9RakEeqvszdo3QbZq3sKAGDg6w6XNkWlov7bYFWODC006G8rphaME4LL_0lHScHJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quuee5981WzSb13_QIGtLgh_Y5fFPm_XqJplxbeYNmXr3T376DnQImwXkt16ScJWkOT31yyXajoBbU3WTWMAu72vQ97phKBBc5gcKDqlRnTARHUN4VOAmQ1rAilieLWk-XH_hIi8kpEbrabBzBQRu7nOE48nRTbW5rlLwo8_NrCXk4a3W3WOsUpVxyg7xywjiOWyibnPQMZ6PiQmUm3t3B9tiv7wvteOiXulSSXzjuMjPbw96wRTX2jSKWSQa-hgDhXaytXFIxwCPNwpBS2NaFSuIMprXgsT91xwzplq_AJbpA3tkeas6pPp6jUOwgr9UJYoiOh6D-m1Hi9OrqKCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vL5UB_YJVb2ri0yIUGlLWDuW78L7ckc8Jc35Ovg8QznNwLTffrJVaSfiiZLRvT5vDW638COgWNW4_enf5KxeVXP11zCcRwZfO_asICodnqLRyhSG1wZD3rHk6QB5conwA0RjMvwDbWEp4_EfbjP82d-v1Zei23Rvw7mjVlcduD4CTa3c6Qr3ErQayrCR2rxJkx1yFPlq3v6xmNFX2D2pa6Pwp7niHQDB9OFM0_Di5UHzkLUC0zFIkcmmTt6mRYayvs_RltxhPWAUUdGbmHG57KSUgqOQbRQTYZtGpt0DLFOifTytKxNc77nS6IrPpz2lPB43WuHeGLnJlBHJxULhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPt8LISb0qL7bBgtsN1oZGbe5sGLCC2C-N7nBetbvLTk24Rjc0TTGs80cHxuXZDFD0ozsGCRr3TaaqknUYKVB3CHavxpXufdpa3cw-02QoivAzlbXyF33v8jOJbR-OAmWwEctY0HJsuTXiLJt5wRMKNhx4Vz20b39j1Xa_EIg6UVL9MB55MPvel6i2WaADq2hwPdC6mzmA6bXuwG84vJDhOqrnNt6WVoGYuu1RM9k5Yv1_qBGwTynsUWvhBPQkKrm2TaPDkUSfG8o_Itb8AUv0M_JJKs9fXqOlwZAPQGxzhW_RaMLPJsNMyyfufjjBNGJ9USuWPoRUCqnhue3xUoKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaShqOM3AIZGaSeB5vd5Vm8O12_4QVkbJV3r7EFezvxeUzoufa3Ya_ziP8y719MGUrjf1aGdXaa7v9F7yLfywKUbrIDCTIDegv4IiklLi0Pbfi3dh7QzgF_tUykdiPkiV804eO8jwRvKGrrTb8YZR1Piz0Xb5CbzGEPuhG6Z2UD4rnCvz5yKeIZFZwW-RYOO9AW6Ichyr-9Rgv1_fGrt5mqe48glIj79xZhmJhhb5cG-1FW3aucROywn3H4mce6AuchDT1h3zJWZ669_xjYmMBXOOIepW8x03FbD9HeNouv77IXw0TosknqIteKoMmgRJMDU7IWYtRLAEIWZAMvQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNEE-Pa7Xc4tyR7Skf5PeyjXAhJv0klGBWDlNWPAMw9NR-r3B6XncCqAZMRPHeZ1_sCzdS8ZB3F6kPlzt7UbwOHtvrUY0Sd10AkeOxi5YluYxSFl82q0MkVZEn6f6o0eYoMzGCnII_BhXt5RQII8gEGF-vRMU6gmslOFx2l0HpuOGhBV0XJNA91agLEymvgWJkQSZCBJXp4iUzwfrR3rdBNpuTXmZS5hq5aAm3YXI6A0y7k5EYVvUKCElm5KolqFm9AjvSiOmlMfnJjxtVA7XZ_g7j2VGPLK-mYlNQcj95_s25-UumAGLTLMeLCQ80eXQY-UHLmFgcw0PnwadCFa2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 588 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp-bGR9AVt2HEdDR4s_Xgr2oTAJ0FFzKsLpl-lUp8oODP0uK5HxYjBMY7UjbaBcGT8avn-36HKCTwDF-muXa6SJ3ydK2gVWt99n223pOGu7E3yVbGKgxsBmA7ppCHnPvCowobtyTsdUeobSrIRl0b6_PXYk8GguHRnQ30svaHofhBJr3W5r0DGvDOIMDKFaHC-zQGQaLgAwsmNZX2VHVZxVdqM54UXCXeiCvnECb7pUo8MVxyZg0nm5KZMuEBvHghBOOjRWPR11ubZ9BWSC5WxAtGj-3DO263fusdHB6n6MMziE3snTrApSZl_NudnrGbbtdbve3kRjgiiYOUVeFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kays2ZI0pYl2OoAYygV-TE6bz1KqwkNIBOpBTrCyKeZrmxAJxYfnj4GJfJF4tyaRqDW6nkpjYn7imSnXy-CghHvawTUNUHrd9xhGeJxx37EU0-DQmfMdawu8oR-9rk3yJDpyKqO2bTbbyuNKsJsmpoDIXG_wlUmvcsYYjjzSqF4qXvAi0YuMZUqgookxfzhn6nrijFvu4YMpd-DrlsKcIP_8ejzxuza0vMhpV1VnfOvf5DR5fdPQ72g3AZJwSF6ObEDEHD4YJUjeWB3jJZH9bsBcFZJzK8zcG94ls-9UZ4cT9i-N0iybAjVsrU9NVBB7sInUZzZ7dzKLq7HQ2Lo5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 642 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aImRDJxKmK1KEx4E2ULkPovKh0dU0OpVp6HiyoqIlajCrKELmAeRbZ8svwB019j4CucgHt8KXgsOBFhI-fNDo_o1maFap4QXLS8PL8b5UuUCiVyEa_CEdMIwkJJa18tlvzrHaZ1QqM6Bdr1fE3ek-Db246ujli3-IHaR4eSTlGPOF2d7NuPjcMZTkZo9HyR7XzNkd-bbNzMGnJYCXepR6veRA9d76sApC1A9FAGnN8qJIwLnHLDnEyy_Hs40hWaE5ArePA3Q5iK8vI6pzkk4msVDM-ikxjIAEQsSKQMPRi6NV4g8A4KSL5rKW6W7WQ40FpEfIvBRHh7vuU6WcchtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq0GJ62FLpvegb8jGHzqe_KpFHmpSJVD8-KHvktNJm8Qjy7IVSfKS7BJhZTLxCsRSIFbEWbtEvYZlhNmUJ2-tcjVB8QXcEDy0gYPUXAQH_Ff2QnaN3M-vPIDGeD_sGcnfnQ-9THLLeXsvncL8lBT6vuxvou4V5l5QdP_uf46rjNvVOJObnrRguS2b2x1PLBoJb_lYYkl0UM9nu1bdTqFbdMuZDPBKQgfWK_CXFEb0ozR_M-4EXIJAwscRDO3coJuh9csCkAnAA_9Nc2UTvu9lyAq5ye3lCD9Z6666mDNxmfGibbe0VsniuQVDBhCg7odl6DjRo6f14iXoCmxTrveOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En9A8z_mJC-S7T7DEyagxkpkqqQmDRO8lsEa_i_6Ps06_NyxvDnh1lXLeaHF4hRl77emp9BngohomsGu-B0GyyvDYFFBCJFJ9heA0Pc08P23Uq4oyMMd4X60YAtkDVVqGELGh4egOBrAsYL19G2j6vDtGBNwNrvRoNDwTfJMh-oT667Kg-9XveI_7JsSOoco69wj9p6S4FfMg63NQS2Tupl_fjZ2yhu3JgNAqYKh0OX9nkAzTs0HXXWMmHsMWIiGMDiPaYPIaQexLhxlgNHHUy7ARd2ycDltvUavBTq2GthOnUROY6oO7uftPV7bbz6nRwRt3dBvSO6a_TTbQrvvoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noS8CADAt8eWnSLV-A1s6mMacdft9rJwSluV8HzlDdfYE94gK_Pz4IMSI2U6q1FCIJfEfKE2CnhRGLfCa852kt4jLJV8pmbO1c8PbSx7KI7kfYDGyhFfBzlww0H79KCNjIwGYy_9v03dwwUopCXEUw4eomCAnPtnruzdQ_PIhqLh-l3k-j_LDO0uSYRshsd1UGUuD8d2TD49xg5axkiMNpjkuz50ApplBBdpRPgdwHXr0mKi5ORi_b8Vcv8dZxwYIcdACV2BGdzh1TTBYj4jcxPEgpjrCMvBguneUyafZrSSn16eLvy8jRhTBRyv1ygQ1m6uRgAGJIJBUz96wh66ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2YzgGLn5-S_vYsaAKNR9aVHnmHvwNMnPB3_A4Mrk2qHhTvQrzsUF5b9BgjnO81UT_5U4Ios5VSlsjbImhycoFqsdZkalMrvDxVjrsokIHjbgFhLp3f6J2UX5Oo2ROwIp3p18U5_y_xiNOIJ3JWL0l5exqCJgTIDN8Q2duVTcp4kNdrBtKIpUGWzyVDpblnUiFF1YMbfT4SZ2P7LbjqVOTU2BCX3nglyj1KwjasUv0DtYgXjCHMX7FI4AWP0KdgySmlk8iR8XfANANIvFLL_QHaNrzB3aFNC6DHg8aa6ZtnKDyGrgRKy4OMwPAsbI26ImBnLEc14_plROar1058NOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne443mxtSkxL6_GZoFviZ8_A_2DyW00qA5WxtGqIL4KnOZ9YKcmo0Rxq6wBUQomsFGIRuHpa0FMo7pSspAc9D4plbEDu5DZ2GC_ZbUXcUoYAbWQXj2ai_pMAD8Wo2BGfsesjI4ONZdrenNiku8WrWb5z7c8ir40kwDIHRf8h7-ft0Q4i4bERREwnrkF-GcJr5rwz49Dy7SplS7T0_WREp7prmR5389B7RGxZ95MOAX-HEwuHkS2q7kohRMpzHgnVPuw_T51eHUnVCL0RK24AyRWsVh1b-aRDqE7Gqz1qj_byPVFK0jlxrKvEiMN7Q7hVnEdQ0H5CoZrrn8l4L6Xm0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxhYFQf-n9WLDMioehe2PA323hsPhLRQHgN-XfTKw1gptMJAwujuKxf4ebgulGV2qAP57KoI3suYJlwU8ojX7zDaSmXH66kLv-4IJ8yCPhG7KzNJS_gQ2RUpzH1Mw96wsovpNOXotp7IcmNoL9KUn_Z14bASlB_Shfr4NNmwjo315BpfpZBRSSoJtJusp_1Hl9J8I8c6aS8MQghJkYLe4TcR7vjUpQtqQ_kTHlxQH7hfx5uJafp3KF4fq58zuDWsU2FO_YZtZvyPBekf8vsP9NRXsPqxnjXCr5x2JltN7Yq2M644wWI08J6Y2FwuqHTL2_lEo6C5xRveJ2xZOkBIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAnq0i-Y9StWuRcXWp8GIi1MzvgKmKrjiQKI5Q66qdooeK8OowrSw1yMk4NZJ9XKLKcp1J7buj_odMLGDVGysO82c5V5k7nMqIw9RUEoZoRWopKKT2wMN6aFiuw7-hToGEGGGk72rNchJ55VWPdl0G3szG_hsvjCkrz1-oUzZ1Ua-CtXhTUHkftut1x6sTTddP_keNHe1c0UsQHnw2MmgT7b4xQqTaYsCNF0opMDn7kBHGZH1Y2bNIy9tIQjk_V3hQroZPuza6WJTIka6kPzoaWSXLGx7u3RI4vYvUhs0ZuP29Kbcp1kmmWEF1k6g4x8VJ-wl7-C0hGiRT7cIvfzXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZDn4IqhNF0k7xfJRPI2vBoQOkBMhE2zD8R7Q5Qux2mdEqfY0kBYSOdHq19BQEqmOxjHCa9bglV-eH6L9BUq4_q2GGUftjNYBFkoGFrTc0bAijp-IkDHQxwiuOE_c_ubc8ifH7Z2YCqr9DYe6SRWY0Bte0X5o_CKzZARHZf_BV1f4C4fhifn_7KM6vebTSyzvslKZPelAU5AIpgx931W9yFIA8Qm6qajji7QIciSd0lqXcQK5U9bqXO1eUUXinx9hxq84hnJZCet2xmk06gf-eKbdWkbb5RlxVWh4ofaQFTtUz-J8CfUYBgM69w4k-UXzC8_TlTPYEFQPrt-WYk--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mx5Za3JY_nxsKzCZuscrFzFnuighR5chi8ynDIqEzrDRik9sPz_YjLmPpBYJVwJUyWvykGEbEiV-8y81Syvn4BQcS2YQ1VPZx7MI6UwC5s9rte01WUS0bXEg0h1D9_myifff7YEjD1yxmXBUuXKlHaJOFDwg9vj2nBgbMDk_KKDtH4ADRpEIOrOYle5rqr3_X1zIejdsuiHVAhK3HwmdGXukjBQ5XjYbv8N2WXCJj6J3Wmsiv5v-ZH7QIoilGO9eFSJASGErEfN8NgZpvqt_FW7x0603BMRb_5Q6_GWM8O_AMEIwZjc65Yv-B07zYhPt2p-_m4U3bwcN6BdUA-1UwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hs1Nfpksfa9Z25hNzOde9yzd979CEM8qCXGbJTnCCwLyDSEnUKdK4gOxNYdFlyue_DDnw81axRl_H0KRFnQs4RwRNczkk7PZunjosjd67-LJ5FJASu26u1g7a_K2mMjYSe3J38yDrA-wyUqtAWaiG5jaX0P0QYwFNbSds9dmaIL574_1HENEHXOuTjOa7et0F3k1qZ3RXjlyFuzX4_exLDEpxcAScHtY0spOFkyzNyjyt0botuOSflzKxVNmEmGFj-ax-KbhC9Xahs8mw303I6H38amn4q7tbcdd5qT8dexmpSk90fsq_eUaQM4lJHBiXsKqq_mGOci_esAIDYW_Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nspdy8UZGkiizbroL5j-aHMcUgeq9pEw5yHznNMkmCn7yrVMojZkncSpIOAc42JH6wj5ODiOsl2CK32BBIrSB8RhwB7hHI5Nz695gxnUmJsNl_D2L_TOphxa3Ae_dJgWagRSPoE6k-bQIFRCQi8_LMNMSEuCFhM-lsIlGbZHPHTYITCaVwX3e9REDVMmq8MFj2Q3vRcMxBw5IpEE_Tc7LCAOuzH-QYVKXzkCDlkrjI9QxLcajxqvmc4Pt80EcPYhvS-03e-6EdjSzluyuhGHMIp6gXcnMH6Ru0O8ifNlcJ3-nv6nO7LEaJD6Kp5G1QNr9fgpq5-7MR0EskN8ievNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFZHeWVUIPs93za0pBqBkUsdUsJSzBMZVnfcE8hP9BOoFHNuIOJzYkTNDkVrYMU9W04dhseyfa5SNn2FV3Y2PzAFhqFiTaG4fpwOZwJ6Gnmdrhs_5uq9-rYq_igX7PHHF-RDNzml8a7fl5Z-pqFsPaf4j-Ckp5oSxitZw2oMHBb3ZgRSOs5zmcO3HSIBa616nf7_FHX0ea3DmhLL0lRRCzPNZZkUXMxCi2YhpdTIaeYbeo-4uEgqI54sLn2wxItwBXgt-xCEyorR16uQSspcdeYlvltHGGDjO7C0GruQ4YySX8wacQyJFUxtpRSG4lS3w6Rj9kg6kACFTYwc6Z1now.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUZ_mVgQVLhjhblU-UsFR7sq8bA-1GC8uiBuxam6kKFYrq8k_LpI_vVvuyXMw-QeZ6JQQQXbZ1Y00XH6z0Z4MvEZOXEeuNj97Vo9Fi86zUJdDKUwT6e0LYFEVYmT8fq31NcwSdOmBHxcXgbBuY_iuHhgs5fqsjJ0qEjZwA4bpln6naQDwvGi5XBl6vFJ-w2TxbH7g8PUBtpN-jjGx7SrwpuH-YJbJ4uqJBP75_71ET98z_7PC6MVfgbhsG4-tZ-Zgi8DR0OlnnmV1S8KZnQHwfLemIota0yzipWNAixJo5_pG5nc9JJIXaIO7IrU1m3cUFrNaki6K73yIVvr7l0iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfWHKWb5jxXai7qfG0Xol4fhtEvWDaoTpo4blsMbyLwSBz0p6_Oh2vpQRFiytOWojpZFhELols_R1U0MSR8tm2DbCNa65gr-wCIO5xAVOWMONIFgOxW7nF8ZjfpM9AgC_0YnWm8-9ArMiqfqzuIOUKY5MkGMYMGvGgfsQPipfDYLrQrKnF4vCLVdfrDaTqefW7IDDjtxjVimP4Tc4EbkdX0c1QWJwNlW53iusE0v6Yu3lZWiPuTLoISo-jIQILmVAlbNf4ODd6sQj3QvRqdD0z-iloHXyZP5eFjNa0RBC1eLqk_WdhSTzJ9SYo_2nLelvkFecN4c5KqX3soZ77dpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbqTzRXI8_Or5S_qImnEnCGdHWGq1eRYQpoK3xZaGwZDWR8K9nicC6PgMxCizDQ-sQIGLLvAg59qlBkOSVKMmSTOYjA9IMbxEXjypcf9ccoFVPJJzYTKSmp5hZ_Af9_mQpcoCxpmFq0mZDUJSd5vEhgvialhIVYi3EXZrwLzqEZHjHUYkRgeOgCWFDQ9_DTe1hg-mVOtPfosV9EIyP8E488CCFQtQSQJ0Q_rRzAGugMHXbnB37Fes6lu47v_A2HbaNdsEIaGeEpbcjAulT0fa64HX0GcC2wa3CeV2PIpK9u1n9cedpiHZkFx3TkJzVdZCfpMrwBRxOAiWCu2YBmdsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTks7TmiMaCDsOQENreip1sjsqEHZxtXqC4EmBNRTIPzHja_dEY40UXsA3HyhJ_nnvu2K0dN10x4WOd3WbGKihqJ47quByw45EPqCHubhf8AIfSpe_ZHuWrf80bxgNAq3VI9NEmitiTFNVdoKo9p-vp4QLtJkciZ8HsMbz8rr8MOKUjMz8YIQ7D1_-HltHBqQB1xtR0bLqLf-ZxlHYIZqjrqRbhA-KvB2p1v_22W5WZUaODgkML_9YZ3Bv4xVDwf4xcvbU_zcz4D87HXSI5x_BegAK4jX1BSLksp80d2ohR4m3J0oGm1SqXnCdHLACFFMvJ3MEOXJEe7PtncMetM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4rqafmQjEj7WSEs2P8ipmAnskcNzhexjROPhhGGh5GjC7wxtlrHUG5C6iN36DXc9yyID5he7_cfrM5PuJM_pPbQOxA7VgP0a9JBKJIgrJzu7FAcl3UuCQZjjNVkbh6lm-Vo5XN_NL5ePk_FViP_Qt-S7LbesU2yW0BuV_z0kA1qsN8TM4N6b1ivZlgc3__61W3Eh9UNBHuCu-YBUiPRqpn00w1PPOUTGw5S_IqWPmqoa5OHFj-EcaumF3VaEQRq3CGJ6Zlye-5e66B_RAsP3Ew50iFImMKYMHG4vQQd-q5UW4rIgRpiKIP4_JtysleiOEkpwYthGysHGuzl1S2kzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZDjJNjPa6dROH9drdy0uwear8KW8HTueq-UrLFERFdq4OfPetBDulR8D6Ngwf-Bl60vSfw8c_MUJ4tCMXbEnraaOg2_Xzcl3XLqBvfneKYl9Ke4PDJlbQcrjOrXadU2LBFhi0zPiEgT22YsXXOz6oXs1Hzw2ENL6_2i1h5HOLuDeCe2b7cWsC5Pfn3c5p_G3sRrMK_0__u9jqSG8W3ut4Rj9HzBNrCjIGxa2uBG5QUEEqw-q5PWI5Y3Gn9KOfTa4iLInh_1r9VbRRtt--ieEmYL1sfu27gcZ-HRIm8f568meBCgxf1jPCvMVzsf2RuQPFk53n-AaptAckKHLS4Mbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nib-bD0wwRLyDfg4vdltRQSPRHbbhrnrE-sK2I0NAGUUWZZABwLSk0W6Pakapp2e30u9twwy4LQXz9g1dRKikVCSTLA5FnjPKMMpcGmP3HC_lp6Cn-citDECP15gijgrAtzVh2Qh15ryPoxxu-740rZMls-Cz_zO2lK3VxdfTLe81ayY_8tMKt5QbxibDc89cHv-3v9aEktk7DLxW1FyAGVzd4Esi7ur9RGIGkzGq3_VrDw2-TXhIafsaWDWeQ2X13FaG9KPACTHOG_kHMZ6SuWbGtRZlIMN_mev_LUwT0Hzc-g6K-SXWCER1sbcN2Sj-_CfZbe5ZEy2MAJJzCLwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyH1QV-zfAd-BwPtInzHdl0FMJPC4bP425bx4fF3K8MFIlMFDOLyjBgEfyXp_kwzdJwC8kpCx1830d4zDyqqzxcdoW2C5zOO95jEoQT0xBluBaCtFJ2WElHNsqRUQFrtZVP-x9eZCjxVP9T_g5e-nbppLo0dmGu9Pi_yT5KCGKv3iVhlN68_3NnOjtZlUwiMIAh-Pr6b6oapQQVyC-xLc3EPJTl124GB6c0Ygeu3ZRpWQqX7VHqWcWjXxTtTBGxLsDL5ftd9AI2NTjb4Qp0uHrgfdFahQIuHv5Nt8zCZU4ELHvA2OU1SFSoJqx5_xnyLCWx_nzFxTGbKFmarkkvbjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW7EM6c9Rvk1-70Ualg_JFltVTDV8ELrtYubybNSbNuw0llVU3Pe1h7lTusLqqt3t26qui5I27Jn-TfCqslRq0kUHYuxSeJ-GgZnofDauQje6l9953nqMiRPOLIyG00oWtjW3wKew2_6V9FRncv3HK-4xsSmDDevGOvqz3rVDKfcjEiGrSZmxEZOx_HgQvwuygCoBvSc2uHqOCYFmKz28-_ZjUIw2GXVvN7gsP3TOvqGsHdDpUzLdqzvS3vlDMlkmcbrFw37Sb3anACvZJfls5mi_l-lFRG5-s6DhvhBXfTXWxi_3JgIvUmUi7aa_z-gPkPkdiEu9PWclpP2mmsBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viq9sL9Yqc9Rj1zrFWTWPmttCIKzHmL7OY8LkgMimc3dAQB0GBLqxBfOw1SNiZoANDPaE381DDh_GanwntfB1P66qH_gtEKlOOBTChbehrSCIiwALpY5STnn7YzZ-bADBrgPWJsbd-p8UUsbgjFxofLCZynaF31YYtzKZ-1mhFlZrZBeYleYfB7u-kBhoGGlnb6oTSaI0u6SIhbAc1PPMG2hKdBtwykPG-cAOGswgE6nQVrlvTFnHdJtrJ9DEQHypu1_9CvHk07BxdN19-yqLtp05a9jmEyhObYXV2UgFU6AEpEvi70Yz9ZvGqmFHfqxT8zxTRIabrnqTk_jvprX3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzCK5rOFbHQGzs8RayBfl9NGtG5EX7KY9SnkN2C2S404xHzXXvySA1eJZyriASKEGcwmZBgY3iFXrZapnSawk8V7LklTtmbH9ljQ5HCt0r-1lTrvUNWcDW3rAwVjYcJ8JLw_anUgpbZ2zD0cpopzsbl6pd1XrhgtVqSRhGpYO1DfvtHG6OMZs3xEXNlm3HAILlumU6ta1oQfECoOSlOkCjM31Hsw7GeJ0u5NqtRUIvjV6IhTFfwkKOO7wUIqanlwK2EoOJn59vN279DiWKDG0FSTaCBVbdn7qxhCf87Hfy2p8KNQji5t7Xmd6Y0QVYvPzRXpWK91b4QwAPSKhkLl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb6s9oD_NdSw0FXMXpEDnLgZdtIThE_s5WDUIUZvYE7Emtl5O4LvNoF2Lej3_GKTmQwrb1UMzrfrGAGkJn1WPOcOVJeD1N03_XXU1Do52TGmtNv1beb8c8DX1FWCxtADRe2COyj2oDEoqDjxKzUxHpezwbZqODD0mmVGuZ_CSS_jYC4qfR1qso3GNpBh_32j5XX_il-zcTz-gTM06qdIuIYQEh6ZYdypUO7UMgYGVeeXMlCuayVecGbHlaQ_w9rEFv8K9yEpW3-sksMalvM5AEdhowcOlA4eYJr5L-IWwPyU51wZiedjZ7Ggr7hRmcXXPU00s-u_hp4HqAuLHr2Zww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=JAKgqpX7Ff6iUaFVex_P_xuWd8azzwWpUKOgH3TP0zm5imOwoTiTN5SUjUGzwtlkqhm_TFwJ3CEnPonVZzRPPLWxtyb6KHl7iKGxTa29zumxBdQJnH6qJdYLrmZZEIdPMyVDd6499pnrnJonQoOwAH8NkPEVLfgjlvQkttLtFUz5ktpCZfxFPdX9aYh8P-VLkOKcLOUQWZjztb9LQaabEfjWDAerHNcM2i5Rb4s4x4OVzFSe_SThiMCZGn8IaNLdA4Blh9zZnfrTSpVFBnXe106hCoBTgbdfsCy3JA1qWQ7s1wlkHvceStsrR75qoCcqi2nlXh6mI0Sb7N_Tjte3mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=JAKgqpX7Ff6iUaFVex_P_xuWd8azzwWpUKOgH3TP0zm5imOwoTiTN5SUjUGzwtlkqhm_TFwJ3CEnPonVZzRPPLWxtyb6KHl7iKGxTa29zumxBdQJnH6qJdYLrmZZEIdPMyVDd6499pnrnJonQoOwAH8NkPEVLfgjlvQkttLtFUz5ktpCZfxFPdX9aYh8P-VLkOKcLOUQWZjztb9LQaabEfjWDAerHNcM2i5Rb4s4x4OVzFSe_SThiMCZGn8IaNLdA4Blh9zZnfrTSpVFBnXe106hCoBTgbdfsCy3JA1qWQ7s1wlkHvceStsrR75qoCcqi2nlXh6mI0Sb7N_Tjte3mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J043gK4iGANikC_jeEYc6JzjfLVsyAYCyCNKxy25nvnXZx_10nLs6grmU9Nzp9gRSt8V06ZKzrqLq3hE9es-tYFFQO3cqQOrjUzwyVslu4Ia95x0RjeJRh88ZME04lXQ3xyBB_zp7hx8Msk0IeE3Zi_MvuZvB8VPIw6RQfStMxpi0OwAWb9zUT1gBQ4khzHCrL-LfYFkKirofLJ5soTm17honMc-7xd-889uRJl25vg9Nvz4VXJxhLGt7FR4_wdDrfpOEZvpe-LbE3-tN3Z2hfsdrLKh8gVkSJCRvuKaGuO3aHzoTjVbAFexEr_j58g0LP5ph5yLH1c7wF2trVyy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s26mLtUXoeRa6KgRIXvLwsJAuv-z1FkOgsakprKJViAq0yDH_5zJ0T73CeJWMPPWaxNybfm69cHpWlnC129d_u8fxWIN6cpGhTwsXYpFfpSJsgtJ-MfkZptI8VdLHcNFdtHL39JatT2ilzUiwLhcWiGj0FW6Ij4I6GHK_a0yJvSgd6vfaypyKsQpcoAi8quiFw05FS1UkWoTwWxxBs3BinT7MQZb_U65kvAsAMU3Es8-TCwQzTeJq_1ROBZ3CqVaCGx5TxK6i3pdsX1uej0fHb8kkHsm5rBI0LNwHQGaxJraqme6opf0ejafiIdfkroQ8I-nOaNmNyToB8nckXGM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/or8kjVxwFNzb93clm4FHb7c_RKvPJL3KfVLVjzzT7eYb19hdFMdLzVqvtPH-nkZ1VCwBXvWuqGjZuLPFQFUDAthWnICSSG6HI7pEK76WxPA_n1fFDV0mtuiu1Wqe8R0HKswVMhQHscL8JguOW9aXyNnajO1bJY1-y9SG_pOUalqnU1RZ4uhvjw_0kP0r2ybTDUBvNQ4KS_tn96_EnxHL_5myVEA0eUGtMzx-ul4ujnSYGParQ5tLGSDD32bnWR_C5MUe4OE9f8mtOKNLaMpxNVIyk5lOVnEOeiugCWVWZXKyHMlr8vxEoadSciMBUo-7-jWWrbGyCa2nsTm17QNBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_GiXUsdcS_UJYGUnuLJzRJMQAaerdwN-tCBAY37j7zkogfRCf0V2gnqAqZm1PTlD7lQ79YStoUBrFnniX22i_F4bzmWc6S4IiY9mhhwOzK7H9fbuS8XOjmVoK8V3QZGDIFlsGlBUd_1m9YE20cKGFzqXhWvMLSnx_JKDV7v0CZAXihipmTohZee2CUSbckm4b_5j5PVA3EWnvXwcpl9lpNd7mywPzyfgz-HX8IhsQOXIrTVlOKSz0ZCi2zaYc_SCeCq4zwZCjOjU25t67gxn2EEIGOu0iFJGXNll8a4ePb-wZlWgEMvDLkWEXZCpsAmsuwonZdvcmayV5eJ1lML1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwJ_X0WbMCNrJqWQvj75KRB84AXzGOXqVCB2OAL6ReyZgmxo7bT0dZ7ctVEq62wwAy8ZXSyMObQ6Xrba3YvBLphnUXOUCliKJXNsG1SxKbYPJPOZ3_U012aYC5pu_g1Vvku66yA5iWvQVjE_zD_o5kAACSwUAYezy49AFDCsY7WoZbceM_GjdvhgAqJiARyB9qEhfXlbqulu69AFpb0r3XFLdmmSBNWEjixfhoub3IIMDIFxrMipl8_q1K3quLBLoN5kgfG_lljPhoHge-5SIkIFD6VVm1eWdxHoZW52i9UhA0sjUy4EficnPM9rEf8eSg-HN43eegqUjyUpYC79Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPWNpHjPUwcjV0o7-rMqiso5rHW0IRNbHPpTQuYxV1C7JRS-n7UDhklU0SFWEJpvBAFmwfjJ8Z_TdZunOCTodWvkC5VmHktW5in5z_WBdEGZzgKkM9uEVc8FLOC6_guVnbY4M3DJU348f15tYuUc1vblWXKu3Xo_v6N3Hgx8bt2z320Jf1aRKsl9oJ7iszEU0u4utbcpWgl4ePF2KtBtELaurJvr1LQv8HV12x8LtZf_2FJl4yubmk7eb1raaIaxdl0NDJH5oSTkOMcoUTNgVXeyLD25V5jh7i0sfGZbZLWD42AhfYaca1cUtl3O8b2BStiMaxVkMHcwSqh0WarUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCPuwOodR_ddYokMaoww0ogYoczREQDYEllmAYAGQklc0-80jb4-VyKlwo-_-DHMMOnn5olqN_A3Ms1L4v0EVwKh-wXKOtrT4JRr0ZQMf2uQmHNQrkWy6YVHSp1dSHHQIyaD0VZKor7N8x6DTicgJfp14Ca3UaZjXbRVt7Sm6ZymM_HsxPQdKCqPd-LE6bxcC--O25tH577STT2hQNR76B3GAPH9wn5I6JmGktJl8qzyMOFRFhEsHIJFuVR-lnL0z6pLcen3V46V1l4Thh45FnKTQn-qrtlwSiK4aWgB94tFZsd80ljxDuZrFaRr_lJVTVPwRl0vIuRKkM_X4qdbfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=TuBtRLVZQ3gymoAEMrx7sgDgxB0HDdzmoXZAndLgXnzmBclYgZWZY7c8t3jyIRQILxwIyxMFfd2XH98eQXAmv3dUnDO5B62L0BspNgL2BVnE2Jep3zYuU4FNxxobs1gTlJfKJ2TwBHKOugNJQF6dNh5xydGVsMc9QyRHyXZ4Es3FwEVMx3_4OiA1dvFqDpNfzSAm2mFaK1jeyNGcq8DHOPbEg19LfRqR_CakbU0K6qr_zHPG4Gd7YJrp9ZNYp5kbGCqy7VUMy9NRR2mg38KVssO-fh7z2fZT16-HYutb4Ofd__ymLT_qm9992FYmE4BokuFXPgvQDv8eW2wJSUZNfIpwh7X9m6SQQHP0ttLR19FpFb1lN7WtvDZGZQHIj74XoXU7LJJtTdHrPhXs1mhb8dVwL0JiJVDtxRYRADYm5o4hHG3k6ylZIkC5eV6LYfWBmINjYsPsoqna-0aosuCPKaOK2t-_7fMnx6tqszcGWcjhMOVU3m16QezyGDy0RcWgoLimFOVUY_ZAFrmRqe0m6M6z54MughIdzJMfKMT3ovwna2HAYzCSi2mkzfLzBr1c-AJQHT5CJBIzB1BzbyPM3aKbh-Btmg_u0JLrhsQ8egMA8A-nJJg0KJ254EBoonuc3u0V6-3VrgGFCdjJslv6a2X8TiE8fd9wKta0Qs035k8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=TuBtRLVZQ3gymoAEMrx7sgDgxB0HDdzmoXZAndLgXnzmBclYgZWZY7c8t3jyIRQILxwIyxMFfd2XH98eQXAmv3dUnDO5B62L0BspNgL2BVnE2Jep3zYuU4FNxxobs1gTlJfKJ2TwBHKOugNJQF6dNh5xydGVsMc9QyRHyXZ4Es3FwEVMx3_4OiA1dvFqDpNfzSAm2mFaK1jeyNGcq8DHOPbEg19LfRqR_CakbU0K6qr_zHPG4Gd7YJrp9ZNYp5kbGCqy7VUMy9NRR2mg38KVssO-fh7z2fZT16-HYutb4Ofd__ymLT_qm9992FYmE4BokuFXPgvQDv8eW2wJSUZNfIpwh7X9m6SQQHP0ttLR19FpFb1lN7WtvDZGZQHIj74XoXU7LJJtTdHrPhXs1mhb8dVwL0JiJVDtxRYRADYm5o4hHG3k6ylZIkC5eV6LYfWBmINjYsPsoqna-0aosuCPKaOK2t-_7fMnx6tqszcGWcjhMOVU3m16QezyGDy0RcWgoLimFOVUY_ZAFrmRqe0m6M6z54MughIdzJMfKMT3ovwna2HAYzCSi2mkzfLzBr1c-AJQHT5CJBIzB1BzbyPM3aKbh-Btmg_u0JLrhsQ8egMA8A-nJJg0KJ254EBoonuc3u0V6-3VrgGFCdjJslv6a2X8TiE8fd9wKta0Qs035k8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-CtCqVE3E6sNo4ivnzK-j-9oWT0aQrkXvtmQ1US3_J63zC9l9kgn_H_GDxZUXlYmN8MyvaEslkSHKxWJXUI_fAXqgQ2UfmcLuqKvgQmqn2lKvMeBTSAoZZ7BFFTnD_PNPEktiDRI7JX7Ra7Q5CCAL5pRsBRRDUB0kuA0ULUrSXSgYC9tOQQdG1i4dnJmTE2PDdQSMAl518SH9HGTM_izhiwRJFVI2PssLalINR20b-yLYYwV4KIMGRpgcv_BmW67LgDUrPzJ6roY7xCO988pR1KlYZ7AAHHIKtZYEKyUvgryJTuxCxaqIhoTE_6SZYeFKFi0vR-NG_0fsDhTMuMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfeZmDfNA4vi-mWMcP0SlToyGOOlhzHq82lQyqhW03KP52NoRiHvIm5KgviTfyKiU7snkT7X9cHEi_fTg1hEhQmvMoVBUrpijImnf3N66YeCpoKWd2veG_T-SIhB2Pfjq8xCf-W93DfJgFruuTLg45o75CrpBbOAbR0prgj9s28eai9thyFTrYMXtErNHS9caGPkG7Q4wbkXCWlqSu09ojjFDohRVbplngxL9_A_-cz7E1ak1mMz5WP5xJBAck0GUiDTT2CuQPf8DxndbL0ybjMF-56Lvg4opTtG1pLa21m-M_2DZ-rtsXy452ten2sRCy8yHjDgO7UApcJISWtDIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogxH95lnpMKT4Z0sSM2xvQx5bgW0tATPk0ppbmbzFDz3GUhNFa8ZBtZi4XAzzt1xBc6vTywcsaSr6fVZpi8GKEnTPPv7wDfMom-RIvNNJZesZruQHZ02HGl3pp0nAVTYU96wZRtBcWp9AXN2qOOCw_NvmiSmEtAmfT-TQ2VsyxNllPo8QGYhSK276Pp5gcnr1KEMQkQtgITC90Mvc77bDjp7iZBcfSs5JpWEJqAOT7pxs0HKVR4aieaEzLgxzNgdddhJA8jTxgjYfjdfSHFLxeghTDIL0pZ4WsjZAukXwRlI3GIzrit1Se7FIDLpIs3qubqe_12J-ZwVvD6b0yDkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQduEZ9cUY41lQiyz1F4UjwcF9-bpNu2n_8kkmktk5wDgi2Cj6Kb6xElRAMxeiSjFMKl60SjZlWUTUJz8kD2THQ3S0fgve7CsoOOh9Sz1wS8uXo5MdQ5WlIww4CvV5GzXX6e9rgEVYA-_e_DAUwPH3Z-rFk3BjmmmbSpOEYFjn6FOFksAElXePcpQ_uWsNJlvXYPfTtoM2I_IniMRpItRuX9M-kkXtXpnmZrnYohu7Ab9-SYS8CmRR3kjBmbUK4ARvJMqdNrFj8K8iqJsE5Zg2M6Wp4-s8WEA-w3fHJTmoGFaki_DHT9dBxzNUG2pOqd6Mx8ct3wleKyJulqUhY8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xc0B90XUBR_lsYYrF41lYXaDt1UYMiqraicGu8daRfGiFdEyNWJfySz-3EEx1_YDgBF7LJjvJKkxS6CoNfpZ4a7uhUHHc4aj6IEk7zPU3jYjWeiVUww-kNYPHoskrnH9EQZljoj5aKDVHX7bLzvxRyLdDPnZtSRphttBvmJw2x6TNcdwj_hPpaGR2Kc35DhtnOpCsUMbKaT3iLGrSmDUG8Jdlvddv5JWvDs_iB4ZGrDk8wCGNbyFNqnXbvYPmL-G-dR-pAAUKQAdsZ9i6golnkmafg7f3vz_M8S3gFHP3T_CXCiQ7nM8YEimlgAIXjwyJGduhyCjFpzNsFcRi8ZGqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUV2QFSL6tJQzYAIEsOf7B_1Omp2z0EKI_XvQC0j0SHNozkmPaGUSBwrp45uZnvSn7t5RpWdtzEie3g3GSUcFXHqzdk9SOMVxrtW7b9iPl0LsFPvI_ZByzwInEpaW6OJBcwa0vNS0b2yjI83Yx968gWmB7PR0hMNB8HbiLEX3u9r7KHbaQDCPP1Mxqk3pA1hEvkA814Zvgl_2vAJqKoTnsMJurn-ZMjJ5wwTbTTcyrFpjvC7_DS1xyYq8a0YdwAfgm2P93Pt5IlY3WR6YImgaeyGhS0QRGyFifeKZ4Kdxw-se2MMPb6kdr5eQ2ef3BX8mvPWpRnvVQaIM9MmvtiQaF38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUV2QFSL6tJQzYAIEsOf7B_1Omp2z0EKI_XvQC0j0SHNozkmPaGUSBwrp45uZnvSn7t5RpWdtzEie3g3GSUcFXHqzdk9SOMVxrtW7b9iPl0LsFPvI_ZByzwInEpaW6OJBcwa0vNS0b2yjI83Yx968gWmB7PR0hMNB8HbiLEX3u9r7KHbaQDCPP1Mxqk3pA1hEvkA814Zvgl_2vAJqKoTnsMJurn-ZMjJ5wwTbTTcyrFpjvC7_DS1xyYq8a0YdwAfgm2P93Pt5IlY3WR6YImgaeyGhS0QRGyFifeKZ4Kdxw-se2MMPb6kdr5eQ2ef3BX8mvPWpRnvVQaIM9MmvtiQaF38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvMH9KMy0gbfSpRJxXoFSMzdxd6WZgByYg0WBVKnasy6igTMpi7f925BE36WYpLYZD9cU__TY79ui-J3rfXa0uBKtATvvPSL-kYuySISla1a9F4HMZs0D2Eg0Iyoo7oEIxz4fkYt3yJaPn-5ixBvyySjgtMpE8hxRJgUOUb1oNFvpHi5GmPmuUJbE2LHt4S33Tlz9F2QtEPkGojCdJMt39qqzkHh_jKDTgmHcg3WQJbipCHHuYj9S3-eq1tH8ohWWy8duY5463WzoW27cVxuYQAyLUFWwFLK8__Z9IT-Lsr7K9f1PeE8J5XXD6qC6OI9YSTzuiX6lNf_gzkXcuZUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_H4HjdYhxFSqhlckkeQ5JvdvPg68pyBPdWqd4r4dfwtgTHQ1UBXCk7QyZ1bziZVD77JeryYUuXGWuPmZfneYE27kiZwdrUm1Ft61AZHhTH6e5xQiPGo2KLxOx0pmXl586J7rIudGqncavkoZqHdo5oZagS3sdjzoTeqLLCmk04f5EQ2dIwa6O_ieJGyjjFv1z_cxtV9Ne_FisRW4XdlOz0wMuP4yaeoBA8hAsVJgP0BnBmH8TzwGQq3mViiQ5oCuBbSmwk9M82mdnJv3CCeCF5Yw4NjKCVje2NZXsYd0Y4jbAsQS_KQs3u2ZDvyCbA-BuC6AZSedSgrB3YKvC1YGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">shape-of-design-@danialtaherifar.pdf</div>
  <div class="tg-doc-extra">1.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/811" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">The Shape of Design
امروز می‌خواهم با شما درباره‌ی یک کتاب بسیار جذاب صحبت کنم که به نظرم هر کسی که به طراحی وابسته است باید آن را بخواند. این کتاب “شکل طراحی” نام دارد و نویسنده‌ی آن فرانک چیمرو است.
این کتاب فقط یک سری از ترفندها یا فهرستی از کارهایی که باید انجام دهید نیست. در عوض، چیمرو به بررسی فرآیند طراحی می‌پردازد و در این راه، چند سوال مهمی را مطرح می‌کند که همه‌ی ما در یک نقطه از مسیر شغلی‌مان به آن فکر کرده‌ایم.
شاید بپرسید چرا یک کتاب طراحی را در یک کانال سئو معرفی می‌کنم؟ دلیل این است که سئو و طراحی به شدت به هم وابسته هستند. طراحی وب‌سایتی که برای کاربران جذاب باشد و همچنین موتورهای جستجو را جذب کند، نیازمند درک عمیقی از هر دوی این حوزه‌ها است.
پس اگر شما هم مثل من علاقه‌مند به یادگیری و رشد هستید، این کتاب را از دست ندهید. امیدوارم لذت ببرید!
▫️
این متن را Chatgpt نوشته
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/danialtaherifar/811" target="_blank">📅 17:35 · 13 Aban 1402</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6vKctLVQ28UvmzWAnI56wLbsYAkKrGH1c-7pSKAlxa9hjpYZR6L0j11WPah5e-Onr9xAMoMD2DhxNIpO-wzQM_ZYB8Bz0ky6h9cgXo6oCzrpPWlJFnUgdI4kahV7OQ3wRMLVJ4BNSm_46Ul791hkLe2DTNkPVGAUE3Vde0scD-s_lNjh56pdHqDVLvd2MalmtRAXY_l2-WfZghxYKSCl1W2YZtVXd27vrk7dCpZRDu8_opE32QKvX7ZjgR-oEzyRCTKxUm-lTU9mq5iAIW1O3-s-jU6z77FbfmFTQFwl6lYo6FNzHfuhMj9YdHsAllfdcH1Z18b3wUUvn03MiPm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z36D_NPe1f18GigZUtoUq22X5Bc3rx3AsjZNFQgNblH8SlR_5na9NL4bkNoY_qDaOKEFQP9faarPGiZTHoMwU8riyba7hPogSyY1bJfZ2Tl03H22PkkzD4UASn9MNs7B4OpPUn5-D2wE10o0Z7rIbRuqP3wfg77wIIc6tdNnATheSku6gHcqJYiYDbSZE3uyXEG2U4izDAmmany217ggji2kcozXf0RHxweFL_5pgzrvriE-xc64rxby4tszPw8D8C4pbVQj81jUeHhEizIunMT4Idp67sYAhuPshNlEsZ7JF7qwM3_lLBG-RSbbT783TY_Wgfvv-6IUgMzXOUk0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvPleXqThIWfMwB9TDSYPg74qKoSm5JIVU5ap65v8bn5dWTG1Sx4zKToiOQuf5YVTnhZyiTi8Dl3holxXDw3HdblgNmcnAppDD2vhqcnRQEgrsmRfhjh6XfAdya6m8yweUoEtW51prBJ3qCxsRMZkDCiWfiTqt9imJPPnRmKCz4A6yUtWqQS4q_cNylZmB9QX_gD8079722o9n6uu90jY8zO8Pc4KUbV-fkxoxcP4TiFgoTxgvLR8eIRg0jRm7JsljVxX7nmtQAOpKX-Bgqykk-dyWHIKkG1B00uhygRgFb6Wlrzm3R2cwXlr48i0FC5ZZmlSplzJexWWOZczG7hYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن استراکچر دیتای قیمت خودرو در گوگل
💢
داده‌های ساختار یافته جدید خودرو به وبسایت های خودرو اجازه می‌دهد تا موجودی خودروی خود را برای فروش در گوگل به کاربران خود نمایش دهند. همچنین کاربران می توانند در این فیچر جدید فیلتر هایی مانند مدل ماشین، وضعیت فروش، تصاویر خودرو و قیمت آن را بررسی کنند.
⚠️
در حال حاظر این فیچر برای مناطق ایالات متحده در دسترس است، اما  در نسخه موبایل و دسکتاپ نمایش داده می شود.
♻️
به علاوه گوگل در سرچ کنسول، گزارش جدیدی از این ریچ ریزالت را برای نظارت بر مشکلات و ارور های این داده ساختار یافته جدید راه اندازی کرده است که این گزارش موارد معتبر و نامعتبر را برای صفحات دارای داده‌های ساختاریافته برای نشانه‌گذاری فهرست خودروی شما را نشان می‌دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/danialtaherifar/808" target="_blank">📅 11:47 · 26 Mehr 1402</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIeA7bVfOTmeXOOYGdSZZaciny2NvfoUdOLUfNkzKNX91qGDqDPlTIpHpScx0UqfM33X0qj9JFmLC1TM_3GcV5f1xOzN7Iie90zqsRVTZNLPpNMhiDbS4jvN5sMb6hv00pb_qVEsWGaXMSByg0SxxoLqreZ8rjncscLpfENp4MWLxtRsEKP6pzHxZf4rP8mizM2VW1-ZEI8JvSWIwnsED6lwtE97QXJA3hyVUJkXwgXMPcmmvr3D4mUw7GQnkkghzCbcbeO_AJg82uqIt3jADIvcuznGRmcoc94FALh49VyxDVW_qSOW0jRBDrsnoa9E1_hBl8tFI5U0udbykozHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آزمایش گوگل دیسکاور در نسخه دسکتاپ
💢
بعد از مدت ها انتظار گوگل به صورت رسمی فید دیسکاور رو در کشور هند به طور آزمایشی فعال کرده و محتوای توصیه‌ شده مانند اخبار، آب‌ و هوا، امتیازات ورزشی و قیمت سهام را به کاربران نمایش میده.
♻️
فید دیسکاور روی دسکتاپ شبیه نسخه موبایل است و به‌ صورت الگوریتمی درباره تاپیک های خبری، سرگرمی‌، ورزش، امور مالی و سایر محتواها قرار گرفته است. اضافه شدن دیسکاور در نسخه دسکتاپ یکی از تغییرات بزرگ گوگل خواهد بود چرا که بیش از 20 سال است که صفحه اصلی گوگل بدون تغییر مانده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/danialtaherifar/807" target="_blank">📅 22:07 · 22 Mehr 1402</a></div>
</div>

<div class="tg-post" id="msg-803">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Yoast 20.4 Package_2.zip</div>
  <div class="tg-doc-extra">8.4 MB</div>
</div>
<a href="https://t.me/danialtaherifar/803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود رایگان افزونه ی 20.4 Yoast Seo Premium
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/danialtaherifar/803" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
