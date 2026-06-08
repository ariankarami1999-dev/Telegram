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
<img src="https://cdn4.telesco.pe/file/XlughshuXavDHmS0j-GKoiDQ9lZmhl-wDeXl9mJZh_r0mIRtUkYssB-JMuDeCSsdc8FjzSt_21jZbtwFEY6IR8_Fem6V8emk7wsz8DkGUMM117XBb_r5UP_ceURaweKPI-LBk6vg-vYsTltz33beuKY1sUYfGSVDQH0gkD8Oeym7A5CCro9byO5ziBkWyX5sxdLSg5NZQtrEo_XwC45gHfrGYjTztaloAbHc0_5gGwHw8BQRnVHM6iSORTn6cb6HQQZg1KBbpdxetj5epdxiV7pNbPD7oq6HabMM10iY8mvdD8PjdK8Yw23niC6UCThl3mMvz7e8q6FgYbxH7eWKAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
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
<div class="tg-footer">👁️ 209 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv5jMWbrrkeE-GlbiqgoVvbDRHKLO1oWqzechJTdbqtvw1RM181vz5sFVFoTuir3igztZiHe7OcxDsE82vNOhkB7eTMC4kupLuV9FTW2USPdEMak8m1iOqd_tBQ_KCLjuZ8DJVwITGw4d70Igss4lbBMAqVVIImXwc_wi1P6czVXNv86M3oj34UIY-3wQB5A7PfHBVutwJNM1DI98LqTlXBKVbdxd6D3BGnZFyPb9YjCqhY8Om07nLbyDI8d3sF_LjVn93cf-SYo3mV_A4xzFXCY3OMQW_hbgWQAHuwdiusQbgo-CjIxw2M09v-RdoizRiezuywgFKTuQrBYOgHI6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 332 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 553 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwXZ3a1Vo6YofEfw1ZeLP8JQ6cTTTelbPc26-Qrl93HCCNBDI_oWXZhpReIwV7GgtQLFq3AFIvcoI1hv9xLLf0oRaad6MIIpe9zx7j-FdJMlWFEjXfz9NysBVtVjJiCFBIiLa6zhcAUdo_iUO0-nRy-piE9cdBygRETA6fz6f5vFhGFMw0s8neQPgyvN0d6pCSiDFElqne8ab27yly2N3PSobndguTkIqs_8dHRNb2LjKfnV9GJZ2RlCIkvsqT7pLLr2O30VkMaYgqxun7sQ5nnBS_yAYUuYs8lXfUlYPv5GVIje2D0-EverxzqSUq4-MgRHfdqceeRVJoWvypuPJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIIQM0sijwnTxLjl5XM6nSmxbyIveoclbCyyhoIGQF8L5ajN8SPcouI9uOmWi7gz2_ItGGAqASBK8VdS7E8k0MCeLp9zO7g4LetVsVCuoWTJQTJnUdynI8dr-WuJ9v5sAP9QdTywSIQHzrwowJD5rXpYdJQBfFRsefk7Z86CI58ZTriAkHjheN5UK4Q3lw7DHix265Lb78aAWKxXgE3nL_qJgjfRgykUYjEICFeGl4cPt639RkIaPisG6KvvwaRr9-h9gD_K2vF7uYLNDMl5Ut9qABXRWCqljbFLAq_GMOqOC1rqClEDpkQIFy5Vls4e2JdlN1C7lkM7AgNoUq7kZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHquTgmTTIHdIVOLOPiNplwO98AnBc6KdSVF4Vnx9mQyCAfiRITdUaCIisrL_EHYfZqtcMtzXVtQi6bKWzRr4aNKjpBwf6aIrqkoxZX7KENB5jG0DtB8s8IqFyGWMzcERGcIwyJikGv5deuR3Tl6UDwz4wTrEKE_iO6DB0rsKh1TAkXChSfJVKyCukEN62vT-iCqA01FAiGpwCUTVjAigh9s7eqWA1fZGubzBQXvDuYJEErKoIzsWCtEfMsDl8EuB9hXYTv0t3GJ2DgC2Z3-LMAgLHmrFMtkEUH88CMvjMT0fgbBt3jYpzWc9njSWIcM15m30tt3tYf3oIaQmnbXmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsvGHDio5CA7ywEpVBF_naSkBXp006WqdoCGiT9TEHfMUk106_xqSIj9o4vztbyNcWjyBItvjGRsM9bGLF8hl9cNhfsa943KTW6C5mBxyg2puf8gNOtMJ3sW-dH3oHsjqPJKVqfmnB3nIvhGoNHTUEqqKexjHScTTxj13nXIol4mvB5oshXPodC1cLtKv6YuzOwh_MF4E0OLFN90Op5dRjG4Ke6ovMkE7ZP7Ed2lr2sGNUi63VZmBlCVXN1H0utWrWMCZaPwniAwhJ6bizx6XXc1CKp-hHh05zD4dgHRxsJ3OiwWafvUqDTOXblajMC0e1dKJN60hm6-E5vcMCkgkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeWMXz6RxroQCdHdFf9qzY9L3RHcvKTg9h1_0O58ZdPQsmE_xuK5XX8vey6ZYcOTwh6IUR6m7ezsuoy69UJHcNvqaOnmt2_fSqcPLEMBPET2tLkpFOBthQ5YCwB3kUnBJolDR3I34tTeQ0t2gZ7MarvNJ8K9iSKadkT4gXSHVx077ck2EVEVTdZb-MTMbGgEhwQBtZfCEpai-SzrvRiv0YP8XyT4NWyt9XitgsbAUCwzJMmyuKA6e-kLNl8-o224LsOyazoO1l3jct6TbXascJ3HQ4yU-QibHl9H4gTTCxWEPKTROoaQnaJjOGSzXgh-4QUcDMHETlAZyKDuajXcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVpgWFc3T_2yzJztjvDCUZKjxoWqnrMFJtN1J-88LgjvxregqQptflBBlI1uCMtwgt12ywFOZi8TmrhO4yqJz5cY_NxV04Mb2aIWmUbl6rThIsXDD60dsvKLzXmGaVDMdgObYohRF4FfsW33POOj8el-pP4HzAutcNV5n_5KhIwyn8y2QmKtbLMQadtS_y-iSy1Lzr3gmL_TYAvMup-C3AIyTH9QG1LomMwMnHR1_L0V-x9eezfh-pahsnH17hw0OQXaHOeTsRxuuCPQCS9ryAg53Po3fzuN50E6dUSlc2L4MglQ7ms1i4O7hUSTk5Mm9X6iYaRIbs1tgghz8bW5Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MopY3UHIGami9ygyowNB6UUX1EtzBZx5CIyVrDBk3eGewqkGcBgmyuipIofT13qhgtXPZE5hL3knMxH6YIVkP9p6HY-k6yuiotPQdZRUjQC3poY_UVPBKVgx84MOqJLGPVYdYemKIqJr4mYZAjxwLFIRVuq7V0lHinul0jY1wYzhUN-2kqEF4xf_SefZkaTPUG7pNwdPbeaJxg9b886REz3_sCUgYYgKVqCwzuTSyta3FmscaWbjaTyXUjDza4DcIjMyHuTJxQkg9p325Qp1Z2vwBa9rFxg8AJTOl-LLAVjUPh25KGuPllm591aE03pxLcqroDvgCaq2tFTztL-YJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APgJ4Y5LiCmjiVLbAUBVjOCk3OstlFeWpdea9T58-T80B_korSZqjYWvbqNfDXHDmYGaOdv4nTKb1_ovcD0qgPHbXzlIzNUC4lUAkugbGkE5YGmmnFHYzJ1iKDrpTsW9wYTItckDu32H_Md632qLSvomJA215dW_kob8v8gKdVDFqpV3jKyv7bpg5MOalAGFYG1GJaq3OHY5DDXi0f2ejj7W2Jt8Kv2IEP2ILkcYJCihdrEAvF9yBlELiD8tIgwA5vhDDmQsfSwGcOYSNvZSq-49s4kEnqd4XxDcaFsa9Pn8hM6OOa1mdywURyxCNROvwSu-aVsO5JYwSP9xDcor_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3pJ3QExg_wwdkN6Q_Kekclgp_UxlgaRX6NF2KZ6TuSY20MitX1opGAj9A-WTKGGMqpAPMSymjwyFFsBKzKQ26qoe4yrig5tz6NrldvECZ-WUI7zE5awvjjJcAqTjD4SfIu57CoqA-CSUwmKk-XxFay5jgs04Qwis1NGxsBJgdbNci4VYsRVIprE2L-o4nX-vF4SNReahMlOsL_3K_wKMDDezhTatn_IigS5pgD2Jmrb_Kr-L6jZqRcYKzEE25eXSI9G5mzsBtc5BtTtwh3HZyMnFQ9nMKnxRbNMUZLHco1B6Yq39YksYDaihTO31ZKG8aw9qN9xV05LqrXb-uTFJw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=D2HPwmSyqe659JzDTS-FtSY4To8YL-jyfnPVRg-Su2px-_a63_RS1RDoKt3N32K3vJTBK1rr1rfmkhwuD55SQoMvx7BZdc0xvbAETzpumb8cqyMAs-rlTTQXUiwRfFELbVS6tNULmgvYsp7Tq9m9tqdSLIVPMdtE8f8hbF_8Nwb4olv_PLHPFmn_3IlraVOGJctcuMQgT1kunjhqelEPe9en_bL1cTEr48_yMTBgLnhWqnLbqZtVi1BzRyfvVr5cxDv1yqwe6d73z3olSBCFFnEvP3S6Uh5fRCzNr0vPQ7IycAV73t-_j2qU5Rjc8ijrRhyu6Bts1fTGLoW0BpZOww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=D2HPwmSyqe659JzDTS-FtSY4To8YL-jyfnPVRg-Su2px-_a63_RS1RDoKt3N32K3vJTBK1rr1rfmkhwuD55SQoMvx7BZdc0xvbAETzpumb8cqyMAs-rlTTQXUiwRfFELbVS6tNULmgvYsp7Tq9m9tqdSLIVPMdtE8f8hbF_8Nwb4olv_PLHPFmn_3IlraVOGJctcuMQgT1kunjhqelEPe9en_bL1cTEr48_yMTBgLnhWqnLbqZtVi1BzRyfvVr5cxDv1yqwe6d73z3olSBCFFnEvP3S6Uh5fRCzNr0vPQ7IycAV73t-_j2qU5Rjc8ijrRhyu6Bts1fTGLoW0BpZOww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUJFdbVn38vcxzNkWUnD62KWBDIwSSlrknaWFtGHq-LQwMc3-DtuxAnDPUywudyCXhO5G-hQzw0zf-RtkD6LfapN6HyKXK49Ss_IaSfXwkAf8sCD4gCDBcgx4GMf0of-dBpvtSqhXK8nA5dNi8_pvqL21Ygnczf7u82gIrk9tCzNapKqTa7n8lcnyT4t_DXA5Kf5ibenoab63d2ucQnpy9MxXnHWFs1Yn94F50ePqSrq53TNZDrp0bP3efWNrbevuoiceLdsVkSFpiKjVBKDDEECeZ9cz-ulejygkB2OW7Uw22wjt19yKOY2j8dNT08JbA3LKcdFXxQXKmrX9Kf3rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWtvAvje9RekC8Cptpr7_QxsLt5E6SEMEe5qsVYakeHT85LsFsfVrGrSzCbSJEgda4-XnRLTBP6GojnM_N8yDsPUp9EKNLoIM6OgPPNhKFkDoWchBgcajSerSjRAuvp5z31rEbyBazFPx1gfQSiNBcAZPxjVbyVc1jSReNwMxKnx2A727l7vol54HBLOHVhFTESGu1E747uOmgjfi5ATcf-V1EJq_5JXIsksCzSqBdNLTux4l9ovMeu_LcZVaKHj1Qtvd639fxEWBO_RCC7vqd-8WIxhQFmR4p8vACAeu9ppwAAprOE2o64zBV9KircFKaU-QHRyOfmMUlu7uU06BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYmxwyJdwRPDIyUuwZPmFTtCVOtbb-bBgjZAp5W1dRPkdbCwgdey-zAOrJ1z0KSxfE_dw0J03Ryv39Y0l_nfX4SFsDzkVvYquNW3OyXFlV8hmypriEnY9N9qb-I_iJRE7yMBs2jtHlnZZaa8r-JQEASmK17wJgesDx44nJ55Iochy1377KxxUJziXn42x43m3QTjLbGTK0471EHnZz-Kp9vvbIAkUGdGxZA_wuvmcwIgka0ng9gpD90dp_cPcBOjF6jUbVME_m1Ptx8ZfEX_lZmS2R772yGW2EAwuEzsywQmG9AJ6DNmAWtC8kD7Bi58thSCCQ5s_1uwWs3sM-CvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7d5ymYIVMDJLgGhgwzf2IagogmgYhpFqmq2oXRfRCH7TWhreqDGTt6yHiAxb9SQQe6utjwskcNm-_Jp6CpPERrwf7GVW2NXEdpDvAkdYz67UbkdbOwaD2kj9hxu1-Xb3XkC3gGKSPXyka8NmvScqmlHnRqoNpCpWMcTzzQkQrprR0OnN-2AA1oHhRWjM6GLSUogXsTE-sWxpXhMivrJBaqj6i982PTfX-2-Y0Yt5LnYQqLsPXsTNW6lx65DCmr_ISM6JgXjL5SklY9ZNfBYpE2Myj9nHHOSxJRlcFU1KmI43LjJv6aHJu2ThipdmP5UiUj93W1gat13OvUEXXKVSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvQk_ZVCh1iFAlHSAWawPamyj-pglbj-YJN8UFKwuJQO0Y1jXIYIVdg-ZN4qG387vZOOjPgBRrcEuI361Pdykpn9wJNzH-pECn6dknuwP4Cv_UXwH38_BI6tz9bmnygtVkKEppXUgmyGsOMhoJIht5KN0lmbAse3HosYnE1qh9DAv1Z_bRSNfah5BzIUIDD1-JYUTfHSPVGOIFTocxzyvLeMDxMlzgRQ6ks72OW5uL_63DsGnmdhwbOzMcuU5n4EmVFhiDgOeusbNXJWX0jBCR3MwbR2-GIQkLd42PW9y-E4D51-dhoMHbLsxKaeISiNoWuwTY6yHwKqQMkVcz0FTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1vAFDTQwfPHN0oewDoMGmQF5hy_y5QYLc-fYWLBpRQWgR0nzb0vkwrOQa58qwPByTdjWB4gE7_F_3BWGe-2H9N_-zrdMSShUxfH7z2xMA0S0eAf7I7LGyn-n7dKrkKONgZkaXOIYoBo-QggCVsvRS9JjQJEA0SODl9m6JrwyaA1febtHAs06x76yQM-stdF5GP9rbzURCmbtUvoFZ_-WhrFahF66BYYM71F9KMPbCQ0TPFMvMN6ZAAUBs5KwxCDYfvB5s_BuUv2o-5LuXvvTrxG8ZHXkeHIDevnVtG4EL7VLk_GZHDF1an5nH20JdGGLVyJ1ux3mStt5NfAxGYLTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNgwcYMgJqcADWDPJUK1nPpBzHjV5zaxiOfcPWk3-BHg7TmvA2KaRR4M2vCzrQWqsW4Vgfkno221JngmitMcZtrfziVHOCAIMYFBYDEzFeRI9SBgvg5AOWYnoNlw5kjBFSHo5_h-S486iRyxueYiQ70_CVixSBF80Vjvusnc-z3moC1D9t1p1R4ymBVH5vQdxtlVD6Tb4wD6J3AEl396jp_hEZpilENSSc0kmBtXr5Xfvwn5CegrDoDepCOFMAr-oEcnMrXtkuiKCs20h_vwlrVsX2czRlywXfEDPxX1Elmqj2NeSqa_0rODW-Vsw_spHkT-Trbq5X9A753ShqGQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRaR7exlpMkqUS0_QWA-jJuWqzUPtuTgRzfRoVKgzdDXyAZjafCee1feAnflryTIZEysIxa0PRFnzFpeU3GqJF92acivTxR7DLo1XGta92f-yTynQfU_OrazPxf0nTWy6Rw98GTTbvdoWbClnHeVIG-JVb3_MnvuTadqE2LAIscHcp3vS6vdEfM5_wrxcl5qs4XJarTIGD2v32RWRZsYil7PlsKXHBhANS5rxdmtOr7ze6cMcm8cymtjvMDkZuqUxokBMMAxynCEY6yvnc2vEz-yTqaHQ-0XnC5rNnXelavqjrKHZ8XVHUBj_ZROwClf2KUCS1p0OK11RVeQGU5h-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2GwiCdkLVa8oSepGjsL2KwQzACGdX9LkBIPWs8JearBhwPwN0DElK6cqHq5xysGBFgFtJ91r6RPeC_oJHba0FCIFHg3363kstI-QCXHWuLW7svj_4oMWq0mHFywe0QLm9qwuX_7MxscNi0lnbkviOuinVZjU6U0nWy0ZiVJAXmQapUbfgD7Uz6BWTUsSE9TjW8z6N6eSq2tO2SUSLaZOclan6RtkTZFSbDI7UyB3ZFtB9WvG8EEAa2MSXDxaIHG5DxgqmxuzgsncGUkOHIUBQraYTrC4_-Qp34_2o3zs7-iuJWrP1_gCyN8pG5ukugQcg5YkNmCKCfteNI_H9XzUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjCmD-8Vccgt5KomfWtRV4Qklr6uh-TAFQ4Ds2smUujdOKs_WkyieYnICKOYvhj-pIdhazTRxx_iUyo4zuS309J5q3kLe0RwDa7z5PP6Xu4MWEaJnhndq_EkYgk8mNabKHSl_jDrFr4eO3v2Vd6waHAZZl0QSU7O6FPmyDkj5QFBXPz1AvmiIlhtlXW98-WRCBc6LS6SVX7ibuWXlOiFU_W-vDIx0vWEdQRaa8TXGEVebMY5Bw85FGI06oVtfMUGoIp_Dr4YeVEuc68-Ax_1IQ0EZ9eaVvT-C4Z0AsXm_TGtPoaWOVVyTicjFD_lkYNfrbOJN4cB0-1s_uw54GlqrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKVrwRo1n8vQAXKp60F-nWP82yeJZKeK0NFqFrAHK5mmMsmi2loLJ1XI64-U0Bv8CwTOYnKfZxpi16_Tw_cyNuTA1cBVKNBFzzRcsFuvyGfr0t_5rkabrrhVx2pRFW8qCJf2JqjuhgBMt2l6n8f94Mbv_geyEGCKtSzKlaapmsB5dT241DIKQtHOxCKsQb8wq9kIutapEyn3mXNcTQn1urpRsegZrtxoh-u-Q0Qx7ZWKv0mBskt9pIQJu7QVXUsBvjSnX1ponBLd2Ke-0hdgzXOq7HnQs61_BlzbAGu9a-0dA1OUbStLlGd-Pog-v3AZB2RHOgXPckcj35QcwAMHPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUO0c7tpDBhnSy2aKq1y-CxNQaO55sSx1N0TgLZI0dQEj9aR_h6e7CBAIexjE4Rw5MtdP1GaVfsIO-nyzX8su3XbaR5S_vNhgYCd2-issRJ1RffP3r2fCUY35obPHRc51DAHtJ3DojQ0APuECUf7io0cJTPYTSQLScDiLduwCIdZequzzcO5YhPLd8_-oEKVfr4VBVGmiVJEHPGWyfHU95GG8PIKgc8K_eD_uN7mBtY2bYeQSjSVxlVG0jnkpXfyekCR26ZfXxm08Li72H-CCFjdV_-zZAC8xN9sh_SeeIwM7Qxh8fdp7D48-yu0SM4YnY5xZyZZdVMIJ9ACSjueUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enBi-4iKu0EyAS1S-ZzKi-xvHhS33QJTFFs1dGXRvFVDAfXKKnDsUpUmzRzaNqjA6MIk2-78NAw4vD6TA--w9SLvJWd47mE-M0WpINPZd74pGegRUPwKXaZ7977mAqQqGcvJF3UBwIleUKCtL7C-mJxREuFBYJDsTPF9xF4wUNjNBc5sogiVW3dy7qMoxGUtTXu35dA3MdtrZyS2U-jVcVT1zHdGdor_dtMAAHkcr6wlbm_9rTF5kodSgpbV-ykd_CqMUhZIId8zjd-bfW4YBygRu9XEUEQHVF_T8rN_xomSqNvu4rlBAc0Livm1ChCc0Yftq-we27aWZkzJ310QwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvKgX1xrmTzur5eRBMKO7o9RIeOqN4jAf4Hax7y2huK7KkibjMQ7B5lKzMhr-GWSNNrmp8LRnRwJiqT4xE5RW660h4unB4E3EjPYGP42hRManXVBgC0pLTh_izONq-IEQnLF3iOOd3Kk6f60V_bk965He0yA_FE4Y1hDM2a5BKau8mBKsIPStt5i_DuJqBqa_ixvUMNSTDMj4A8jFrzEFDKbx6L-GauBWMNM-87fz1ruK9hbm0olZ86okC3PlaQdIcLu5ejHgYkcOa7W8pj-qUPxnP2BwSzHce2AbUFi2Xf8S0l6F44Up-Gfs2yzM1ParjjBi9bFuZU1ef4YmuhW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUKVrzmaf58MlSuNCmK5q1OjsLKC_8OGeJTTy9BH50AcllZyXubYSaq0SdLIyYEOSAkkv_048pd_KuvaNn9dUf51gwloLK2FSRSOimI3NbjAD8T5bJssiRc4bFiQ-iWxEy6iWLQEHfbdpJgtB9C6Il9rJeFDCYwCgQvOVCoC-e-OpvkhPU87iQyHOnnoxFmDHWzgPhvskxnufPccggA7Vf5MgKDCNmdK4NQfDNwVFpSPqTnAdiTE-9iV0Yg3ajnCtaJvA40bBeGEn60Q0gibiT92PijuBfye-OeEsBDowwZpUmBj9OhZrLzUh7Do_BvIVi8PJ4xMOCwW98wzb_KBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXE3NxmXj-m3niHjNJSXqq-uuNq7ZH3yhqNOc5-XulRNx9Vrtf53oz1LJmsGbpn_-LNKeaKMph2_uf8kxEjTNf1mHy1Os-DuFy6Z8JfmRg4OvA8LhKUPEV_uvkpeM9N4eY3zJu9MTn4hYMnPMN6i5MEQj8l1JV1oVdmx0o1WhtvRv3YKMNRaQ-xgaOjmRjn8w6_m3deYhnEqhVANMJqOiRfp1A_I57UJyOWA8GIGpY-nLp1ZYRiB8HR2sPGNvbIkJQHKb25p-SqPWu_WOzvnnH245Mh3wasyHzgdlQwJbayjeSd0jF9leziJ_5rd2_VKKcqfR28UnLYBOHDZyBNotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/advAm9GUDpnGRNM8WjHMi0fCS1plNbNXS5-0A4dRw_99GXGYZ1Mo3fx16OWUvLSVxegou7IcDM_uxC1ETYRp_ZDan8Y8n5uIn0z2NDbbQx8yYsQjmfbBRsRsPI3pzHadIe_j0sfSXss-9PoV3wV8KYtuflc9GveARqyDSwt2u3IBydb7HhUreMaNj2cTfVK-Hiiod-_l_R1v33eaNzAD2hJ_LTcj-ZCof_9i_GvVNrnIXk7KUthYQuxJWGznKa5yetCDDMAL6_rHrpITENSMoTwhL77dftm60VTp4yq33IUXUhndpIOzqyx3VUnNwdI2ZwMvKGNCLnk-YaFYCx8F4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USy3yVxiWgXZIX7jzfYmBuf2aKjQISZceLxw5g7aSS2QJBX172AcVy5Z3WBv1zX9PS61WdS68xbznEQpg6rBnF2xm0e96s9k0fx1eC1cD-Ez_o1u21bU-nQSeD67Z5eOu7gMjkc5FndljbRb4j_vqjmziSwSr1QJErV3a-8DaoobedXq9YI_3VsFwXDC_mdAhM9FM_vf9339gmL7cZiZX2UJ6ONK6M3tXQCQYOLYKeDJT7jBP2TsPXkOE1JOzvyn2uReSSAoqOGhIpZ3YvSIOiHMMkl8gJoLIIrb0clZS3yPBq9cMANY8svr0WeZ6E9jJM9TfN9PKSoCkrhX-fhMTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDnnLQnIARNtDY6an6wGTlcHkjngg13Nn1BFLEeY1aDVgfUUn3trtq1fRr86s6MaUNdUO8fheHpjckler0HLynmgd1Q1ZOG-5RuljSQg0I55lpnmDCZTuLorP0BvezJoxJnSdT_XTXtG5ezTnY8qDKD4Z_RGcRCbMSbljsjCvEyhkXaeCQtkrJMGOMe1TASyAclQfJqCgnHDY3E88taMjl_MWwYpkr599mxz7Wahgge5mFx3vz4QqRymw0j3DieV84a6K0WBrS1uqUtXv_-3GiW4Xzs1BF6Gb4OzIJhXww-AW0KQPLtHZunZeaOPOT6_dqzdt8GAua5LAtGJ9CZVzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtIX6r3sl4GbOlKL727a-XPWgo6ms5Kc5IkVe1j2DcPts3Ujw7iJ7pdIrdjqcTs3PbvhRv7pgCDCENzliI9-y5-iTMzNsRuVK7za1dMf8NlrilHh9-vNLuvdbzAoNfig6eYN8e0Xr22nFtszpj8C6_oN1I1e00Ly4K6Ciel5EDxheZAD1NB7_kViT_zbjJdT-IiS2NUozVhD-eoR12grMijmGGQa3XX3_d_DQC9zqrg-A15g3jnDLF_WfGPHoa2Z2sn0Y_thy4WlC_VjJknUT-8MrfGg-itn1k9Dswl1EYOEajpx8Syx8biMXPdnt56eGKX5vDO6gv8OKGcqBZg1_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwJ4kBi-iriepn43sgX1DZrSLzsPiQPStnm3o4DtDSmXxmuaFbgBSLLaRmETRUgKHo5wmbyW9zybRztZCVd6M5JMmQqslqon-mDzKb8ejuiNVlFt3RR39ZqwdGL_4FdtViZxDrl-K7r9Qo7SyXN9sjnggOwwkjolI-B6rm27t-BTyRVo-0gVX7GEWdz3drck8MkZSLKUz4ROfpUNg5Wg8Jt_EgKCoUv3_87iZSXWKK3fu3wjNwhm_msKH4kcTSYr5FCoDyUbBpfCLyxRMFjtZuQTIsvWYvh1--1a3Jbx-VHZSmo3COkQV1Rn59szYN1uVy8SCI1lwj_lVg82sGcW4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU8fPE3OaG6GzW2kohLaRPvcryXSnVbD_BFgpSmrqB9TscRZMzp_c2VF5Gn3XUM3LxefkLlR2c8ybb3o597rjsKgOOU0CbEbw-6E2WiZm-Yibwdd8_I7ztCJ0dHEkfY_-Jic8sgXMWKPhmZLgA3Jo1AYOWFcc2Be6JZjd-cUXgpVS-7QLilNqPJucIwmGhT8XhcO41YYPvr-bXTNaVbmZJlu5-vdNH_MUkBHUSNUFek7PBqPent8EbvhU2LpbCT8OEb2LWHJ9cRWm5v0yjRvPM0EGez9Jj9Xd1qPQClXMo_vSo5D8fUYUBvIqeu_V6-liCDzBlTIH_1upFhjSG6TWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZttKzL_tjejbxe8lS1EIfIQX1H8BrfjaVbmj3VqKI5FPfx6jfDZ3DWdMLPiGz608tFZ0kOYI4r-E8qV2k-iD_R_pfaRHEP7OvS7FVKaz9ZYbwwmfq-C-RPu5fSwN_hB-AiM1nmo2AgRYS_J2S37Lw5b-eyeDi4rIGFgq4w0yjzsG2GtCrd7WvHLAIBAUGUhfZ22Y_B1LTHYYRU4x42C79Vvaz2-KKx9Ns2S4NlIsRuVB4bmcg5E7pm74m01OeTBQG_l6eSkn7FoCKlvWHo9d-_RC12KqCACAYV0nTApTvrBTCJzERi-2H0QAkcvMqIIEQxEk4hjgXpbvL5HOWxZ_MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af8gbpf_JpTlWnbKBdR-uM6MB1WLW68FCqcMedaDAAgVvGDdI5yuDFvtMSfKdXURdc4XcPHwy4cTUUG2XasnPEcctKv3Q9zo3-s2g-eWg3VlY4Cv2RdxEU_ncyOKda4UgqYfloH0VifPknIN8JrbjKzmsHbM82RDDQK5wi3dk8IL-zSqgjB1cZ0LjaW1bqGQPFlFyT4yk3SmpViV8QiJza6OsKc24S4iyRPb6kjV0JiCR1kn2aY4RV1Y1gr8X9SaiXfHAi8yFiJ6AMwnDinFMOtOxFIyiaR9WAAvPuXUdKnGbN72Wsh-lh6bDRV3XtC8GFPruDxOdVQ_XpR2kDPz8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fa_y-ooqnRh8ahQlO3A2g7K4WTMqZegG3u6m6Uo6dLqJqjvCkIbTOH5pRhqbggb12KBntcZ5qdF9qqKU3PDxTQR4s80IAeyZ5_64T2EHHhbaJO15NhF98BnTgIPXpaLMgdGC8cOEIUn8DczM315qgCa3r2g66JwWG12kb23-nWZ_Rpy7QT3mVuQsKhBeB-RjTSCCodL2KcBmv--9bynAUdkbiZcBqWEV7s5AWR6zTHBx3WJS7r-a23pkLROyU2Z16J9aPEg3UHVs6AIZHCjke2t39QeCxBoHdHa06UsOzem5VSiC3UMiLvxh9xq5n00Ij7UPfsMratg-XryTuEswIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKXZDCQ690_JFjIg01GbpVFDE6aGfI3MISKeKr2xVpEErPP0PN2idr6PMJnXy9ays8QKZ93kzxMFx78P-l4sG-VdJ_27jddBwvBZ03wnAJY_nqHPVeW79S38j7j44-nQ6--UDRxSW4N_mcN9uBR1f5MyHF1KMyQ7aMj1UefecmeMuhUKpscnf7jzmpq_4bcF4PwaLlNR88-UxtYMKsyPUbkWQdggKDRki1ON3tMUtOd5SAwgu27j4Izy8biByBlqR5V65fM9pqUl_SMfUmrP5kaH74MeM-sZRv2gMB-vAfiChdiOSiJV8F0ihsjWWv7v0AWDWB3uBErvQkn31dlQjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGQtdHDUuO9_6yCtHLEc-YDwKmDi5s4fLUPQsJAljf1og6qgO5uSTA0J_x9PzdHDQL-L8x6nWPwQvI1Oa1ql3MHlRtIWAJB8dJCfJZjEhyCaaTSyxUbzXbxCpUIQPiuxya9pU9skBcShn6F_4ElHPMTA6gdC6EvJ6epo6G0Kd6vIkkOyEn5b1nX4wyxqgiwrLZ_wI3XNeVV3hbTzQohqmZrfMvC-n5E_tlZerK5pff4yD8XapFhfWMiZXSefeU8wzsshjE5VhbTrofQjie9dKg3YE_xA8-tVHwRzQkEHqrz3Lr-eTuN7scY28pMtFPN0rkJk0FA75kjx6uPrgCzX2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6_a8t_RMTwwzNVUGrMsUtQZtMqSKCoyY1Ugbt9r11BbaqqDbhU2kQGHRCg1iZjmcWGbCW9L2N0RjmCqABidPeuaBNZvzv-ffF2179cO0Ybb_d7aLShbhSRoQQ2MUUeGMmd2IiUQWTCQFG3WlORwLupQrcB2OdSezwv0zqd09erefN3LCvzr0phUA8jG_NhfDVv_JZoaUI8s7GMMEXA7E6CA1yatyxVwVmOIKatfI_wgXQs5EQ-NQt0ETOxfVdDqOhwKZLPRKG3qWxrE5o5nDVpZLlCOnCtkyKbwIBaNlYhA4SbXGIY4Xbil65qdAlPELmgzGUFQssqLPkkdVCCwCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4LMWuKPCv_O7cA1iO2iVVjWeXMgFxVpzp5gMhQWyErEfbMS61uPytAJ10qfAccNxmgsGodmK0kuNnnCSvyR2OSFiQZ9kFs4z3LmuTy5_m6cLRfzSrEGCJxVNAXeOk7bahBaIKoponhWI234aoJdaUQ3U6ZxRxU9RVdjV1hHk4V769XKVUyJYK3KHGieIjxIws5jIbMFMdgKqqDC6EpchezaiP2ad7A768tVTdmZHM8TsY8WUgm3vtljySt6vEvSNhOxVsdu7u91D_1SSFL4Sdnd4oxfFeb_3LODEP9hpzLvbBty9t-1bM6Z6dPig1I2BbnTS6wuHcMl8v2RCF23MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpIaUK0mmfOFR9FGokcaXN8j0UQGuZj9UIy4GdbSEmVNp1Gw-iWYrB1Xl3whBuI_-ErMQPs29ORz3tVYVGGHsngL50j0ooSjQJOOwJ7KSEM5dSUrS2HbifhH2RVE0fry6hmTNWb_oQCyMVbh90HxIF2r6e7KGUDrAlFtAFAaPmQS2k0Zx1EWS1pPqSJyQKGDomLIA9YXG9pdlmTtEC03xyzxpXZQtQYZQO3fw58DqPoz82jbwKIbXqOnaQ-pCGEwQp1ofNbMs_elkco8t5nSH2mN3-1vPMmNM6oW-Bic84Jiu1JdwF-zy6rfu6N-ykv87hEzuVMlcMS1RjJuIUBf8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlbEz3yNYZXIOQJBkF1vDnPYi3yYYf1sDZ3zpxQLI8RJfj1ufk_68E5K35xVecc3L6SPK-CoK6ALHU14kwqdNtjZq7TlNJzRk-w6ElqxfeC7KnLchlPi5_hbTBFxuAfZvXvWYm2gHweVICXSlm0aGKPTT_mz9rKOQyJpAHAZNj-IWX-M6CLM4DUyyKUYl7zy2CukLsZrMXjVwTPp6ottwxdMCR0SSgJ-VbC-BsIpR1Abvf27ih16kiUXb5LY3Roaju7YfbMORj7Exnux672gcjrxf8OI6cbVgL-qqbBLAPNbsHPSvOlmcfGk4nDsWNUaQqbKy05UltDA07PYhFX46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQ-5pdDQkhU-H3VT_PqLZ-985DABEnfgewX3Ica4IfvTLmHjA1E6kGZKTlw7Mjcb1znu3291nyjJ8-3Ozb6Du4nsGaXR9sflqEZxVstTvqDkCc6R35P3bMdR-iioIDbdgHfH0Mx6WJUCgebIon3CkW5zl87ZhUCaIbVqrMynYFfbG1lZVo8ma0gq_hnO3HZ08toDySMWOhesOJCUVOCqXYkis_6I7QIo0Oq8cgsQiivstqdE9_qt_M-NFMZ75FtTpO-P1hasubyN56uPp-Y9yQWFeT_acFXNMk1AJpXaI_nzQjrRI1Gfp0LFV_lp7Az7CQSyoaxegMx2vu_MQCSEgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPHLfWpGixkfhlc7foYW7qofFXXnViUEOSsStQIZiLPtv-X8gAmAhurFXlVpcvuOUkuXKiqwU5KBOkuHYb_l7Yf_KW4ipnKXu1S8zD6hPtaeMwDIAmdc49AFkDWvFH9Eezxzw7qHDhz1ycRBB_Fd3uwNGD9RziF7Op5gknX3CQJ8eyTy3OyGK5yS6Jc9QXieSbu0j-9L-fbzt7qcbLP2X7OR2LmMirjV0-DuIv2vFh4yAXTgWjbZZOIiCkVwJjswGwy-qX5R9ZlhVmZ5JtmEQRY6aYeG7Ivm_Xkka4Wc3fo_5VKGA54eFUJaO7Y-fyiyZhrNszB6cCQNm8WSsH28Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmEeI64C_LLctkgAu4b3kdTPSEAUIUmH84WQmfDqapKE_Pvw4qrPOuOCuESpDnidcolxz5g2zRGMgPfNs5HrzjWnBxX8piDngCUUXWeDuKyrDCCLkWKfWvxMMTR4dJfyaXPdoYW6tdi3q7hW3yqO2ZNSdHw1FR9tbIlE2WfKpMyPe1txlbaj9WhIWbnGecnlsW-7PyxjXstM17bhAZIIyK9HddwzCw6UXTOK5Q5R56AHv2e4IrbJe12fn4zbbQTQzaumhFw7HSicIeQuXLFhcLzDIpz-0yAmG9Nl0w3DGv0nwkHRwWdkBl0V0JYdS2iXHNbCH9HkCBlmg_RDx1VETQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSqFKDJPi3AJ6PyvsxYBYS7K18skUlsjL2XGQaGtrGl7-Homa35baBi6dYhU483jCXd65lioF8y3_M0mi59r2bNq_KXdqrY0w9Eup060toA6hLEzGLN9XVGE8AhcogsVJVUPd0qpfexYuPp2WzYreldB6qMVIQkcE1oU2a2RzSoMpdElawiDmsb-iN7cLCBjQ0vSfPo4aYauKu0IBfTRDhcj_BkzJ3HxehMDH4BotI4UQUyjpBIkgCs-K0mmr8DZg3Z6NVDdmamIgUYrp-ZMvQ-6cA3Hu1pBoYbk3TaL8ESGbxszXLLs9sZ5lGmYRss3p-UaEp7fQnk-n5cOH_BYTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbhDva2uld_o6VYoXznqDoTI3b-QbMGBzoaqwiDighIacINx5BKoSfSGNyku6JHN3cFBu2eZwylO8SF78HMlvVO4-Ufs6KeeTwTZFusk5qCgWjEIgjVShnAL0-tDHBQHD9LsTBSfsUDEMxnCmr1ejMJOto9DOpkJXZXKQICJLAhQDSYLiWX9KQFHLbvhYufeU_e97aTFo_MeIapsX0UokmpOMlPlO28n8H2f9DoRp-BbAhya8cTl2C21TkpRVI758DfI5Y5WqyfS0Qlpr6emxep8LujNb9lZiXJYc87Bta_HrjSHt7sVUohSp0E-Iv4tar80_fO-8NuONVVvU5iQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpOQ6JPX_N477KaoKNT1IDEhI-D7mZWVd83cEfUm08asPL5Ao1z_NBdfpRafQJujDrfUIfSQtXRLF80QkbWeEXVN8vC_6D9YC2djAXuynZIS-VWVKisUXFq24_6okZlhsfpT9mY-QVnnf4hOynFfUaAIvrpFAyqKrR5UYlpvkqipyiPHZJ0U1QScICImjkajbBH7B7PCpZ4t-q1r-VYFqs_jC0x5cC-CPrkkcYp5RLhFzja5IQF5mUI0KyEYO4qf7BgixDpdqK8c8__ymtaM8xaXBT1JiAlKmrlhAehtoJTm7-y9RUB4Y_6Y_ToKYl1kgkgoYwk8FXINOEjmoLJGpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xufp2OQg8WzW6z1S0X3WBhwpwH_pMIxGsnNUDYAiZKr5YS_2x_uXnGtWqraS05DMxutBrjRLGtgNljycxz0xAqY0Xp7iL1GhdPVYoGpEBazcIViVAFe88PMTFxFU3Ls4OlA-paptH_gleY6GP8XWoNxdjVfSNp017Ka9HhRz7DaUhbeCZ3CED0D1_4eb-Kwc5kVYe8vjKLx-0w_NSK8eHHIfBdxhZtnKbs7Tng2MoXQjTzeLBtzegIeyDMUS4DVIEf7PaeAGQpwmiNb0ldyigpzstGDutIymT5BQZoyEl9vTF2yZUu8wCc0YHymaPPkyD9qAF4oSN_pfcOxAlKJHrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhxaBoAWuSsVAOvuxokQ-V5DQkmotjYvfoNJXair_pfm5Z6DoDKfd8P-5767cxk5G0B8XcWvqpnoK2lfRwRnNzXpnLwMIL63EGcmJXCBE7JhvHPBYXDZ8QgNtuDsj9r2mGRTDqfVksAJF8DxzQs9uGJeSPeep2hf_T8N0BHMjiZnwNiJjb6gzRJVIXsqlnR2zP43L7eVZl0UiaumQKY8KBObheMkfse7I9oCjUIIdfTuNU76c-S5fW1F_7WEs3I30rEO_cUdfbSP8lLlW4CIblyohTEsP7W3pjogTmYS1gS_HaoF83bzFP-3ca5HxS_W8WVQ-K0r6mem-dKYyFIKtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T408P8kgh-K0ay8oI22eFBHq_PRqmUoNsjEuO4M-hnI2XshWLtsjxaGoJKPAbVPoDzm6NhkEecB2KaDMQN1V4duTxxpZO6iv3obF7t83KLM-34eyKY5B2jTtU9JG8Rz2Dq7pyT8PxWO_vrWpD6L2L6MI4VEWVKAPNUddPylhk1E_RCxOkFom6GgZt3mtrnmgVWXT0kFThp3h3nq2GzkGhr6mL-NauMjSau_OGTRmOgjleDWZM0EFJoj1IDq5P7xqYOInxQFtwcT4FH9Tn_Ag-NIdCY_AcgdtUWdfOlqdO33faqutIFm45ceqUlw_8_uE6m4FiYvRRmx6MivEa0s0yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzLLXQQKoQroBRgOs1HW9Cs5m6tpE_0Cob_Tyu4_htz7gmVZIZKWcXlYlV--JWI8lQctBvPi4Y7QlKSY1JGsjEu_jA4sflw3806eqDTrexg8VtOKEmaNoa5L3f_S3frO9IL5SjqMNQAlG7u53o4RXKgPEkiSH0RdmKQbdz68dhG-UVTKvmGPQW1AZ8BlM1ZeE5kFOPYyD4jSqtMrsHOiIfafmh8zgSbl1fShlQ8DiKontVTq5mDv0h7WIklNSNOuGu9WswYRj1kUta-3K7XzNcSLwyHM4akckrOFnZLvcK3ewPdOy2cfka89JK8OazauUpVjHL6SzyKh_jABCKIzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WB6f9Fhs42Jz9dNdtyEhh1PIeCl--7vhAgz-Mw_mDTGS36r9wUT2M_jmilg514kJI_UVmmsz2OqHzsCOyLf8qB9T9X7RfMFmhRDLy-xugregjVeAYtkV4OdBNFoRxR9H-eT0yXuAVHkeeOTKPMZ7oXBAjv4x_XWWPBrQ-Ql0fI5-YythTbXad1vgXUDTwuEpR5CJmpJQB8fnwjx30Rkv883es1QCm8ZwBCPULNvWsEZ6Hts5mbZpRx9z_gSA4z0NVfz0Hu-mPpHZbNqAAsU-oAkIARe2Hfh2zK56KfYOWRA44FoqV0MlRKYR9-eldZ0DGWV0_T2PQ3MCT_03eEhk1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_OCBtI8mYG5J3JYeqOHwFSlSCF_C5CqZBf21M738U5kpYC3OonBr2vHoixz4kITru-ncVnrRy4y8wsqvH71Or5CmKf9Quyqck8_w7HJnwYbaW7KUfmj4cVAmXOPwbx3e893w3d-F_j_0syENbGwlLXSHv6osThQMHArPylY6phQOJ93BWxS9UMVZALQLSKRa4zEmlWwtcJh0xqhmQPay-nGztTse32hKNKltZEEiovTyVO0SO2_QEbWhQUyRq9d4J3jHVotCMv7R5OnIJCgPDXh5y7OM68dXj4MQfLcqxcl32KcC5iM_neFW8Gh5vogMA3Bq3dZyTVTWrbXbVakkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLbX9WX-WpTjUhVLKXZf9t7u-3mIHS_HVundR4WG1LoSM_D3_mmeuKOy429CqbVcv4gs4MT9LkUOYRPCvONbgz59eLtwIDv6G3sPeElV90rze6sJLTcITP-vSG4iRykIPCD-WTX17D9tXnDttdnyrAbi9mliZebrEEqzO49l23VW3pl6Z8WPbNkjmrHRnlpXvaSnnh5JAnIBMFDEJPYiq8GYB790VOrJJvhsfkNrV-sLmJwUwTexT4LXcYKabDMPW4Xka_7Ei6wiJSi2xZlhuwQgy5-oNBm2inuOCOOWJFn_EhQWAMEWbQ7Kel_aYzM1lZoWQcNZRjp29UApGI4okA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i53xzmZPSmQBYCkJXGbY9tjLQWsercRZCjhW3g0dQQ8bDKoyUci7Ljmlc9B3I5SDaCA-XedLA-3DzuF_T4-OUtwSfiqFAe0CU5FnPi9gSB460qtrKmTOOrUk-GFIV9FipHICwJtr1qE48-fir1tzJ89LKjCLKvXj4p9QvkMplhirPjwtcBt5sDeUq9oNYdvPLkGMEPeZV65bNwOINJolpZjpd27DLrAqFuimPVUzIWoTOLSJZr8URxVqnsbLaYsemjUnNt7KRMNnegJ0XNd-Y9_ysuA09TzmQMDPMP6wKeGLnmhjReF1jyoDJrzJKKmfZIyKpLNng0yUE-h1QzjK-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0PJenUwEoMcvm5VRSv58dxpIH5xHatMjI57klFn6ieLoUGTc84lFdNDTpVzizEARLRuJwVWLlWcL7V5fcqQ_uBkUXIJuiiXblfsTEudWN14q-jB1oZQJb1OrCpLXmtXefOAME_1pK-nqZU_c0nG2yeBP57cip2qPAujgpL8A1o7pk7P3HLcHebmCJCFeeZ1SUUzQ1MR4SXIv26eaz-l7fDFdMRNW3hoU5kf9ARFml2zF-cOg79KqMQlorItotYCg9WFSZro4cWz40lXtbcg3TjVo_EFWjha7nE_rVOS7PGVjJPVXh4YVlDOoudxQWk6aKkiL0_MATzKVUPBS4OBqQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=PiPJgEn-EDU4l2wg3-xMszp6-u3_YVS-FZ5Gajfrq6Zt-LMzvxa3Q-yjN2a3ZenUFI7cGrZjAYLV7K4caj4qYd1m352Wlr7sQTvMQ6CDhK9MMblqjvvgL1ck7HgkNwMNkCbq4yOdQDkpTTKzuCPZhxrsIcs7mp7oQFQrhGlrfPcQCNBjIVRTB-OY3vL-KzgctNAak677XL5sxMDb4pQ5PJPNX_CPrNrcQ1GJN08xIXBjK0oJA2E-S3w9WkcJTqzVRbCaddLhrnBnZkppCaG2pzfko0rprhXGrQzCwsckM__0-G-gEgSUXw7QlsbmeD779pyKOYfHb-O7zah7njMzTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=PiPJgEn-EDU4l2wg3-xMszp6-u3_YVS-FZ5Gajfrq6Zt-LMzvxa3Q-yjN2a3ZenUFI7cGrZjAYLV7K4caj4qYd1m352Wlr7sQTvMQ6CDhK9MMblqjvvgL1ck7HgkNwMNkCbq4yOdQDkpTTKzuCPZhxrsIcs7mp7oQFQrhGlrfPcQCNBjIVRTB-OY3vL-KzgctNAak677XL5sxMDb4pQ5PJPNX_CPrNrcQ1GJN08xIXBjK0oJA2E-S3w9WkcJTqzVRbCaddLhrnBnZkppCaG2pzfko0rprhXGrQzCwsckM__0-G-gEgSUXw7QlsbmeD779pyKOYfHb-O7zah7njMzTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYehelR0CjAZ8rsx2mDNAJLl1L_wJHhXMON-hbUl1zPBoXDiGH1UP7I3F7Gt_jzoWamUP9iHmsG9n0PD87l1BAkkEIVXjRh-o5eJd4mSKHRNt7rhIaHUldv_3XAjHYKiZLxK-7a78zP45_OUV_I3a0Y161eHsfB1ucSZVcRFGRPK_T35VzdeG6-cu2g9hh-kW6YTxr7DpxFionGillre-UZnU_xbnTRsGn5wVZejtsEtHgKMSqEcR_aBHlsIGTXNXJpZy63dPH5QDkHxEbePuQ_H79Zk3Eg0lNzMCQJ1wJaIb9CuG-djb9DsrdgPwa97RtDHe0b2z9RmzGieOn1yVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwJj0t5K8FyGz7L2z5V6faTODu286VeobhzPvGEvzCnaKKxom0PEhlsLLEDU88hFarpLOFsfHlw4PR8mJJ_H5l-o_hGmCrfCZscf_eeQ0iIJFxhShOIx-sFwFvLoKJOZ-P2ao9aO7-k1M4GPjrG6D66effnXjMK35d0nDZsikqnVhEzosa4tgOHjpqtyVKvCEnINZ-QBeDnGJA_T5A4rsEpOLwolWbDh7Gr6enF2i9oNt35MrzP7hGDAA8JIl0NGDQoi9MsX8XcnRcS5lI099w3S0EVT-hreeIdtMtrNzaYqIA_hnMZtUzhmozhMS1eYMJxZl8Iz0kLmvmsJaPfjhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUQk2LAfVLgQQvACri2yWvDTWE2ZNhS8ZL_WK-CCtAFd-g5pk9DLjUMq82X_KpFhJ0t0Lze6AS3N9iabFbEe1lU3pEm9j5E7I1xM3iHpSZJ8QHNABvtSz4YJfwk_PR57yA9Az60Bd150gx03Vrmw9vDaqECC6VlGZJUA6PG5I6i6gcsuK6Rju-7J4_WmnQD_iAVvll8Sg8DfCIgY2LIuib-MlCjGBRPyFpgpedU0fWM9cblBO6iouXgAMhzxUrt5wwq6UK9PxWUAry0shfE7GVqN9jQ8Cht2lY8cArTAyW0u6abXEYiUHg2WjHo1r3SA2wLP7ZZY8L9HRwlws0WBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j07Z93tsp36C_C-emC_PtOc1zrI1wXUlx6dUsh01LX4VTKFkesCvcvUydrgAM8pJDiw0OtMMsONa2XlSpmNn373GnUMy5B4IDquHW6lucO3Ilven7nwJ4k7nC4QikG-PA7491Y49ha2G9EE4TmRf1VXVA-kyaAFJR023xSYs4in09IIVhq_dZ6moLBzxjQyfUET62xtXrp5bJiEsnpgRiQfh2zTwGeRgaDlMcEBFXVw9BVJiahmaSozIIEtXnfkEianhlM7AhIPC3E0-F3k7yQ_dn8zovFUlyRqOHoyD94W8wcmLgfTWEfQRcJXyXASU6ZprEmckGA9wb8_0flfxvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2BK_q01C9leuXw3j-pDVarwI1EBXtKt-mBUl17XXb1_tdYzYubjf6dCoeCB4eVgeljO9hrL-yxi9wbKwSEdfe4tUCaa4DqiYeLje6rw36KX-57oWH1UKdbAfOAa97o7Meyc7h3hEwTkU1P9qVja8jXqQqaCCp-0dT1Oik3Yvj4QqL8bSC2uAO_XdNobpp1l_1OpR1kZhliD9eomnSyC9Hjkc6xGHxFoVXeTEUf5FfsoUXCGLB3I-8RU3URJ64kncdVINJUED7puwbXoRuI9wOW7TxBk58uOCdcjxJB9zozqURuOLZnFezU0CDG6EKEnWsTMnv3r63cDfGTw7vD-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDgRi3t4ZmVf-oUrTr39EBxZa0_ShPNwJB9N0b6-cPrqpM1b79skbAa53FDvu4kIp3GeGZu_3FHcoVjNtES3FzRPOdu419nvdH2sBDyNxSq4X6gV45zKLDHdZGpclFyY0ogyaR78A-d_Z42CcGAr154TjVjAVIhhhzja1XnXQqgbfYhJBscjP1yoIl7ewvhY-MpwH_LKhxgI3BMwdr9sfQbgjM8XQSaXo6MIm4Pcr1oaKcaF_YqgouME9Ty2Nt8KXp5DB0pAUCWJwkY6lY6Mtfzk0FpQflu3YIxO8xA3LilUgJ_jAguLBP71MdhdZUkco4GbZ39dDWBdpCpIldzttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMbHFEBMZflr1wuFpB7-ma6umUH4uMmrIM58FDaxAH1m_HQ9pbb9NJkTq1aBxru7_pF-UCTZLezL4UNxl8V9oOA7wvcTpCO77PTLdzetj7itnij1lHy_ZzYzx3r7Rg3NAQtEQu3YqhaYwhQZs2CYY1H_RpSA-7SJVM26ZdLX2iw7WVl_8lczYuyohn5rGwKllnMhwhkZdvpqooLw3RqvLPhU2cLwfmC5BR5I71s4mUpHymT4DY0a6fBDUHBb8zh-C-4SpoDCxVNZ6V4ct4OLZrenBYDrncJXML6JE2d09FshUpDgGSVLd08FmtPBhd-4kXTBjhVtdcj26-Fh7YO2KQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=LGxxYrMjKy1tcHKcPuGO9BCriJYOKnVvvG3ihKkf2x2qF1QDy8p_e_QMVW6Wet8g7XB58suTmm47sr3joI8650n0my_w-puuXxz7p9MQFdsaDJyaK94X1jLd9adhLlRz-i3_OSPSNjsqezJ47I1Ni2du2q_hve06wZ6bkPLyPH_xcUEVxxBCFWHvxRKzidr6OS3UklzMziKO1UgS60mXkqIpKpIxYNtSyx_l9RsAexwUFsud8llgwGkCOByrmKsgdDLIWBIvdCw09nFCAG12cWsjS5OXLTeVuGtTQLhQeoFQqrb8cJsR8Vv2usgwBRZGNswQBAkbR0UzSjIsWXOfhQStkoF_Gga0Y_WV4yuDUUi67Wo0xTmJBQcOBS9DcJhqCmv4cH4HIyiVVLCWWcRpjUtQgMbjRUO75htoV2jTzesn_LKpaV71PPugW6ySIHQsXE4dYhNbVRn467hWdIkbK5zJu1hHK7HFsQ9Pa_BHBCCtHMeJg-T_odvB8mLlamh8jJyUrn5Ki2V0UUiAKn2jnW4gXJhZT2LkuXjVucx8gycsPBq_zcUdNr2Wv9RJgb9mPPBm3m07YaiDM0ICsHvpxhVOKWtYHLivBzW1-nbNX_Vx3ZEOTIdgoRf44CQbHktYw6ws3hzCQB6T6_sMWooWak6yB9FLsuNAbDujiyPanKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=LGxxYrMjKy1tcHKcPuGO9BCriJYOKnVvvG3ihKkf2x2qF1QDy8p_e_QMVW6Wet8g7XB58suTmm47sr3joI8650n0my_w-puuXxz7p9MQFdsaDJyaK94X1jLd9adhLlRz-i3_OSPSNjsqezJ47I1Ni2du2q_hve06wZ6bkPLyPH_xcUEVxxBCFWHvxRKzidr6OS3UklzMziKO1UgS60mXkqIpKpIxYNtSyx_l9RsAexwUFsud8llgwGkCOByrmKsgdDLIWBIvdCw09nFCAG12cWsjS5OXLTeVuGtTQLhQeoFQqrb8cJsR8Vv2usgwBRZGNswQBAkbR0UzSjIsWXOfhQStkoF_Gga0Y_WV4yuDUUi67Wo0xTmJBQcOBS9DcJhqCmv4cH4HIyiVVLCWWcRpjUtQgMbjRUO75htoV2jTzesn_LKpaV71PPugW6ySIHQsXE4dYhNbVRn467hWdIkbK5zJu1hHK7HFsQ9Pa_BHBCCtHMeJg-T_odvB8mLlamh8jJyUrn5Ki2V0UUiAKn2jnW4gXJhZT2LkuXjVucx8gycsPBq_zcUdNr2Wv9RJgb9mPPBm3m07YaiDM0ICsHvpxhVOKWtYHLivBzW1-nbNX_Vx3ZEOTIdgoRf44CQbHktYw6ws3hzCQB6T6_sMWooWak6yB9FLsuNAbDujiyPanKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKiGDoHN3Empi5NNSm47kLoHL7LoDyuJqo5dMNy1_0wuzgrYJOs6Bh6BzYdhCtLRZ4kKlGYbCrdUwEOz3eHkZsaeUuV8QJbqK8qYxd7_98YaXbvOLS_c80UziwfRGQPg9tx9J8JgJeipXnOI6JFfgSe5S_-8G2zAcbnElzv9Xc566CnnFkY12_vTuj5ncEZjdwD1amtvpzqnrWn94MoRo0csS3wYiIDJslieuXtopRrDKOzieIbuvq4tgIZiXNe0WICBHrP7okTH_WQunphMx9Oc2CnNrBOf96b3kRRkLzZzOlCUIdZgW1J3z5x9Eo9ZJAUyRiZZ-tk0SEK-rJTejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPvPMXaDlNJ7OfnQtQuLXXlJzhOoO71haWgdMB291VSvdZ3ibE4rqDPw0khYk7P24T8eAF2OkZjTJzBNRpFl4ud1T-fbs-Mj2FmWU8AVeG4hNgr8IQmdciOKXH3OZVK6XLSZAmzbAx2CQ-Fc3-4QFHHjDGWdlMhbhCNDkL3W6HLabq07P3r_wM07UN00c0X6qCXMx4OQwiSMFpEGU13DuSdQXO94_S-roHHZMfGpmbr0xnXxhR09YmtAK2O4O3feT4q5wCB-LU7FbIH_b2Z1329Lnc5PXOn1_eQpUn5O2TJqniqhRSgR_IFaYciBRr4bofMuYhIkHalpgIqCrUXMbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmtvlLecJOf_rWsGt2VZmfkq0yPsg2rDP3WUR6_7XFFOpirYwJlcOMi87SuQHBLoVHsTr1oVW0QvhVJSn-b-cDJASQ6jdO1DTxYZU3kfZyEOoO7qmrezwmCZ-zQQs4Z8o8WWbkV698qGpdiHZXYzIcVUCaItCpzPQ-JgggEDmzlBttlenHVWYfpkcXzwDMVL8eaqx5dDUYmoER6ZCK9X10rU4yQ-Jvyr0sSRITpXeXKCYz4MPDBSPInkkAI3Xv0FQOAR3rMKayEoaOMql6_SI48-HK3PfytEnY7HblNLuLU_qXYNGM-I1lazklXKgCPHnHnsDb08N2piwCWUDj2fjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_x75lgAWa-CR_4HGAqojgC2zKu1JVLs4Jn8Le-R5toChZpOaoSuIniMZPoABOYzVDvGdp7bfYW-t-XRoQ92FoEuz4yw4V5Io4eKi4xZphNUmmO8Y_Cn1w0tmiXVc_KN7yLrpa0JRNYzbKcQO7p-wUPX86wz8BEJoJ78GuTfLxBo1b9XckBt7Xbdn9TZHOgCs6CYAvM1pAzIi_ytsJbDkYNScw0lPtuF2GG6UwPa5NpiIPhlx02eIZyrJmi50nwlbkB9GmBqR4QuvrXX35S5AfIISnzWkUZufMJEZ94nelzZG_POmxcfoyyVH0f0PP9Jw5gAfnGwZp7TV_EZjxhpHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxZ-nj7E79S9ezqD8Od_7xmxYMDki_F7po4_KGWwvj9AKZDpShtN6KzBMTADd6KbxF-7-pfY9V_So6wYp14uTZrYF_jB6qkjyOQbE9Pp254iehBRs_bmSPLOmFHtTJqXjP9cMXa_UFbTKRCWQJsY6wjswY-J1c9jgfKL0iwS56k0Ukw0SS6_uEizFj8cyXWcLeaJHRhuFTV4OM7LjwHpTEP1CRBukZsGivxIj2OmFskdtXR1ZACe_BYmPP8XupW-IWw1QO0rO9aXYaIY6_g84EAZ9i6bglHgDMgEVWS0im4ikR8huRv7XLqUopwtsHWnuVL4QkGuLeapiImcrEFGGg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0W74MBxB8FUVEl8JOqakM0ESS0ShHY0eqhnLtItrfpkHoTK3Vc7V5ptEdjLs0vlSq1AyoQzmgAatWcHZA7IHPnO-eO_0LH7syj4t7DyrUOsOfSZVT72FA7lYf2lRfg6nyRrtDydQjIejTt0Zwux7rh_5lFgeVi4syFzLNincFRpnXSaCWE02bIHDLUnRawlwzWeJnTHfWbKebJ0m4d5JxRDWeW2KPI5R0LIMwoG2NcY0z4iskzoF537iBjWK3HGBbJwZ8oacvoy4246mHMkSmWHBxHWnkx73U6nhn_SVtKrNp31yPE70zfcHg2AQ2Sk-Z00AaBFmjt27avFIxXrTqJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0W74MBxB8FUVEl8JOqakM0ESS0ShHY0eqhnLtItrfpkHoTK3Vc7V5ptEdjLs0vlSq1AyoQzmgAatWcHZA7IHPnO-eO_0LH7syj4t7DyrUOsOfSZVT72FA7lYf2lRfg6nyRrtDydQjIejTt0Zwux7rh_5lFgeVi4syFzLNincFRpnXSaCWE02bIHDLUnRawlwzWeJnTHfWbKebJ0m4d5JxRDWeW2KPI5R0LIMwoG2NcY0z4iskzoF537iBjWK3HGBbJwZ8oacvoy4246mHMkSmWHBxHWnkx73U6nhn_SVtKrNp31yPE70zfcHg2AQ2Sk-Z00AaBFmjt27avFIxXrTqJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDp_1BEsGuXq3_eXWD0OVYAH_4Wwmyo6vlXX6dxKwokJ9COmatddhRKgzxbfR_5MZc-IMf8ey53GPRWcQruGhEATc61BMkgj5tGxWUeDNwrRsBKhVejf3wE-9q3QiynjRAzFfpOVaw8l5uBY7Mw8mHRSR2yRXiEI7ajuN9k0SlOBBOizq6ndIlVYX91IAvlkUghQimVJp4VzuuBI9tq311iNPXbR7INwbf6siXZlG1722fbIE6FtHQ9NqlNlKQ6GOp-R846WoGjFclcI_AAxEtcgVTHQPiCYQNzE5pKV-dPg1UZe9DmiUYzTeK5ST7Hhf0CooKGIr8okCQ835chV7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQAUKMZkO_TUxtMnDPS9k1v2KQ4kYWuNxglRDnOKLyEIqMokgL1O6mUwneuEH0GLMOT4OwxqZvuhIjKyL1xCzjzYhb3eqdCcDizsWE7EmzVj9Fo3cnx_GpWUWoI46gYZJTu0YgkRf6y6EQ8NYXZOZyjhkT3slewS-Rxscuyrq10wbbvAVFX8A7HvMgyjfnaltBGdAxbTcM2oWaoFIarz2wziM2Gg_qrrpBNboWp4fEE4mT0mM5QatoNs76yeJ0FceiuTWw88Ah98HOn_7V0MU3OhJc7wNk8s6-Nr2rUV3wA0nVTQrLh1uBvtC59myI0pWerfa8kbXY5tOCgNu58t3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LmKgocaLGwdyKzgl23-85rs2MFnJ9pMEP2HsBykKwrNh8YWeGRq_ue-woukmJJBLBa5aAlVOZiUsoA1IisPCncjj4c0l2PL0tghB7Q44GZ6yci-lsTwbsAPTz4f_JH4xTTsJ0bj0I4AKFoVsTI__X9E4cyxw4VDtDsz2BS2R9Mmi8Bng1DImUCzMrlklxoJs6oo6ABSOyqYvBV1vj_VghQXXX9B9RDbWh3Jnj7LqQL32DNHHKL1F7jTWIqTiOxy9ut44RMTSOU_0mqisqDFxUY32ql8B2Veh8wm-jPmkqyTuG5t6nZaXRcEyJAOJ-NSEq-I74ClxWv0_DKH--TEnHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOe3zw45vnqImOxb7HnHAbUGz67yvZzLaYmLJii3Dl1-yI-KUCptckRkRPBazIp3SHeSCtpk5WYwbB2StTgkg8xSqE2jR1e2_gXRswR3mx8k9CNw-hw_VtvYgcG99gnZcac688y85M0CTOBTdlR3Um4RJ_HaKhVPtZ74ZfsLEuodXw8prdtyPrwecQXGNRV0xiD70qLbL4vkubgMQlc3XMKemyjzaXh38LO7InIPJU39F7i0WNW-55q_baSE925fnXRSRIlJ_6QBWSeiAndliZD3E8X0HvW35pATvSUVp0yKlfPzTnkAz_tKEp5pCa8nKN3ZI3NlEBz0ub6m22mmXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPpaEa2WVy5JqFrRKfKGggLtw4LW2t9CdJbZIDtNiHo-9uFbK3s4hF4WF0POzm-iUJB3wqpDofypueUD46uxqaPaUN1JVZVY-Q27XLOqoIFpX2hPLAyY6j_hi0RdQWZTN-BNFX94hxPQ6KcWaTizysOc7S5WMIJkjUdqi8ZpXxGTJAKUh62PM8F_JkFLzbYC1-nhrBGyIM7z5_VL4U94gH4OD6KXHG6v-YNlFcUlLog2PzAGx4bm24zzBeNSIrfwqV45vX-JRdFfnoRG4eOmVhWQPLc70_rg3YZwqeKydb1m7ABhr0Bvv84q0fPW272RIv6LsDUk9_lR3OtGUg-0Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF1mn4y06zeQhLyLXegtVW-QqrJqBAtcaW6WHPZvkxj0GhQXouV9uQnMB74VLy7NJQO_lCVwQKtZaMPAI1W-aOISVDTkpprZ7J_mBPzgFFdpARGTppchs22hp0xCItakILnpsGmsfd0BdSjmjYSqq2RRK09NXRjXDIPfT0Uq3kLhsah26ogl7AEWTrM8dZ2FKW9VHJkZeglG13ffBFMC72yQxbXaaNcd3hH3LRoW7R1hORN-lavQq9e4KzpTE390V03a_p_JBr7qO3oYa-fBtC5q3igvp_xTzaRU3-3yRIla0mOm5mha63OGt3-cV-6vQLyZ6VbRPvBGyagh-SyM6g.jpg" alt="photo" loading="lazy"/></div>
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
