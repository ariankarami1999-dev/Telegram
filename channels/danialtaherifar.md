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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 111 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 249 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 379 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 570 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3UNmTUujj8xK5RlrCveszINJdqZuxnZ6MLAVNJOWTQ1DVaagQNNArRRd7vISsaQSk070tGDOcO2fkRexuP-EqTSww9-O1HJdNG_otghEMSa57KOTjVStUO_2rG6ASZG7LhFYQlY4dijGbaugGjYvPXX0ghUuKxfcuj6H8mSJpglqiYM0QsGh2IW6iz0SAJcxmcxRjovg92L8SlkHi6FcQV9XWl9R-vB0Jk6eeK76oeC84SjQ7XplCx3he6o1Cnjte9tfTdW1RgHUwcpZyhfGHdoXyiZ93iwKVL6AOzOR9-I-6Fr7D7uU-JgdenZGLyUk_p1su_JrhNMno2a0Pd0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJe5l8doY0JqpGK4WiO-ymkRlfSC-teBGn9D0cvc9ak5QVVzbkQqAWL-Ucly8F2wqRU5YABGiAq7vieRx1TUZBYYKtJ5hykRAg5WvJ-5m2P6k6p8JeCdoqtN_F2zIDEzQG5JVL8zau3UtiJW3b3C_Y8PgCxIZz1pjN1_2rJakiH97uLQCHqOjDmAES9DiQOAhzjQ_L-R8ZSWuEuRvYLrKodgFLGN5JucQv72_B9CNjtdvABJ737xemjYzMENmaIAqvEcqSnZzUD2Prtde8oZ3G2uS-H8fmyR1A3QF8-4mLaD_XtFl837B1-T9OFQ76BsL63OR-eswJMEmnFIINa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGaRX_3F_S5Q4WwHtHA6-sQGZ3Y1Zi85521Qeiydzo5JHF_ii5dDOyaIk6Q6XMY76cb_lAi82b5w-yZ4_m23iA6Q5hcfPX1snTmVpWx5k_yRmW44zuqSBe8Yr64v00n6bOFYNyFAOLjSDgMACXgcD1FgkUreGpw0s7nnx1tIXzd3SnRXdYN4H8ySnlETdDlJl4fFzxNTRWDLPEnq6PLLnVGJGIdjVa7ygLvXN-tUGOS877etOmdoGWJ6bhaREqJoU62cTtU2ELbIGFiN1S8AekUuOQ-6UJQ62sY6UfWY9Om3MIP77kqHPiIQdgI7s_R5Z0T6iaPqk2pPUx52OabvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp2pwvxCSzPzM60_vDtAw8lgpxWvKmgmMBYHzdrO_3uS2n8QXqEwwXdMBuyC-V8jk6JJy9gBOXxIUyczK-UM1EMRWOOhYi9hbVD54CyB8rBmGQF3KytpEHogGbcOJnEt8nyfHW6AWFsm5SrYvFU2pkoWO9tlCeQ8rEnA-2yaUREcVzwETSAXHg-uH6O54wW7nFu_j5SX2XVr_mPbxvq3SrJIVaaF_HIgaCPkRKncJu48Oohlvs0SBm1qFRx3SfQgnJd4nrg97Ssrzi1S6L9PMzVBx22Pysr-kDNpahRBLSQkv94C_bz7vdYmUsDofhp0WvegyHYgCV8wgUVscx5bsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 864 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeXu06ViUTN7WxTBjx7BIA2h9O8wcLVPAKA5nhi291Ayhjda5jXOU-VfUlH3i5MKAh5WMnA5MFJ86TT8BhLDYFboQtjeDrGxTV22_uwWYp0wy_8_2DVoxDfnaYf92cOOB7hgFUedfzNMbGp9Ki9lBEfPNeLBS3HMobNNfNSkYENE_HyWAkzA-DEiFRQGdkoMkSsi7pj4hQBQyCQqLhigleAn3bhOLbCgWdvyrt36uGuZxyGLpdChksUhrsMHDMFeP8_mKzxOjDU-JSN-Q3l9CY9k9PYaEXjTE5ouy3o2hqdgPuSjO-xWnCnF9kBVyptjTEvpHRpEdGBlZbXVQ7EKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIhCyd0xleY19ibIve3HvJ5yUq0IwAb56RtF90-UA1oB_d0LSE3rodnGFimCi37ncG1BusihMV5BmTBc4UfgPefYkQBhEZH5qQKgzYUcFuOApqiyrIH9oAenn7AHvC5UQa5_8sl98RCNYrvLrD_iQsI0f3rWbtWEzeL-m3p5fzh8jW0pEEyw6KScAo19BQjUR2dDdIoTUeurhUdpmsFp2-eV9XqOWr1cwyZGvQzPqgqeqaSSSeofZnI5ffUFgBWMPsRsaS0tTlUaISGxnZyk55gYL9b0BFVykg8FHBt1r8zye-7w1XQERTRbhZsU_mH7Ps1sswPo8EpYtNPJuMikHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qih8V946eiaUnHsTuMZIL9PEiAoAtOZLTezKJ6YRF8irG_3G5zWYR26Qn_q6yF9iP2t0Vzp3lzdZaC7Or3Swjujwy4a43gC71zoycgdjMW_-FLgaqXyiOatZ4PI2JBQAvoKD1EXqhdf594j_X4DKGE8s8-hh7m8E3vS0E5-yqEnM_v-1E-uKrFHNrGGxt4yQJLIrMY892Fs3ilwVG02qCl9mPFCaPpGv3wJWAwUquyTGZYB2cxjOmeNxqu6vSc49NU5dnl6ENs8pDlNx1NZ3opbqTjyjjqxNPnad9V1FJEm5Clwz9mud2fdZCC-9_SzRkvMRNHCDzRmVmPNjxgzYMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYLdtWqFfZfgXzl0VcUZM9Cn9FMxX6wW7uQv72UywFA_hA5FJSRUVJrNeCWE1TWF1ECYCaBIPOwofaRYvGJ8mkXzZ97QiW5Ph-tGV_MGIb8UYp-GmWU6TuzfPXYsDDPZGkO1PeRIBOWQk4S-cDx3PquUZhNI50nsx6MKiAkTioGCkbprFMdUXmJZvv45lLLzZuR-dnfpXUnd6GAD5fUxpluf86U4aufje_NXVHRzCh6PiboMZnJvyTFUs7btE4cICsn0_hasFsrNJo5RQV-v3DJfe3WmAgMsecWnX7wqlZd0hJa9KI17w3Gtj-uF4Td2pjiHfbLOsLyoOsOiwH3aXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQDp-XRr5_26EDJ9bdyN0xB76DyHxhdJ64kOIWiJ3sSfyjl_lV1wo9MQwxJokZERSUJBlMNJVkcVl4mdn6WkK6g_Q9FsCeD7fHOgqZJ-elSc2fDnIYwa1GGh5yXGLh8HYkXOEoVJVpKx1IXNzKQr7WkKuVT708zeyL9fE-X5YMfV6PmJbZE8G5E-QY9L1wD_rEhvSHzN9YfyqRC68NcpnolngN6NT6jWaovrMCjqJ4OPTd4Pb1NGKomoN4uARuXj2ojK0mjJYrngTaKLMhHY0ZyUfcTEnGirQRZRqyvk9PTpV9jxSwWfCPOgKFjHXBV9zP9VX_nC0hl_swnv7xNv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWVX434DD4EHut26ne64oLUCfr76J_ileLFOoXIJ_bFF0swevlSkOeae_NglAX3QmSelE9oCVSuhN8jrORO9oALAjB9Miz5kj-XTqpJ3Jgv7srNSmj3rEC10qzHjdw5ixjRNXq0nlvbM0pdaIDMgh5vAVqgzTA9Oe9aH4OByCZlGJQjzvgnsXMMMsvtUyYMu_7PM-IqzvaTp9LH3Axv7F96gHh1-9CCgXOueorDy8okFpHcXXAVrzhPnzKvyHWIQz5QNlnZveUhpKJUlnMGRHARQj9MHDRmPwxfWi-6Cho5xrWYMHfP0s69nG_mjuHw_nTtumrsYVQ6h0f4dUCQITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 841 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlBNWR7sD55MePQAFxH86OZMbQBTX4fIzDFm--BDHE35nGsnFlVapxep1azKYGX0cnlsWoOpJZ5nUGekx4BHBNlHjQmEUWqsmahjJWwGk8-0WIsF2l2NiVgl3QD4g8Z7J1Vk1xLq1rh_PYJgYs2Z_7zFfEA2EL9lUacjWx_e3OV-qYM2Uw9r5A8fLriULBh3QKUOisXqCC9XSBIj6Fj723j54F4fezvkfSBQokpuihSfghMIBaiRl17M89KCapaPPvQnLtSHny-DqcfctXzgMKoRLoc0KVWbzrYc9F0CbjwZceMeAC9lQch20Ihmr3qteHd6h0OJROEiPZQBEoadgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGregTQSfBZP37l2LTrcB5g3EDMMmifLChlV_uDPI5M5fDRq9YPV1M-QTLBb4ltWo4pA79h0BcpLybfZLJ65IcNXfwQ4FLgn4YVjuk5FC4bF2ciPNnQS9_gO2X7l76rp3uW2uWz0TNdMtGg6WjVxiuH_z-wMEE-kHAR5Kt5hptLzx-d8GQcU1s3wWElAX_dY4gv2NgEVT_Bjq8B4p2Z27Y0ehMa27SkElKGuXdLV-ZHZEQLat3eWgZ_I_VHSfMb-29UqVOtl5JdE8iXeYe7ph_SlCe0UmfaY_eYcYMz74DtfD9wkR4rR83Hjzf8gNCtf147nL0LoJFjXz0JqUT2IsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZASlpKlEQ3-URjnVbTChV7XyRY67XbURBidi-MJxDvlMPuaiIen89Wn-pvK0UleO1gvNjk5uhHbmkitM8ptMHqtWsawqjl___U1RwqoIDKClB3wmeTCFEvN7F_2zc4gly3b-MwgRCJUzo4p8uK3EibL3F7IecxFr7sflYzzeJumet8c4Vg5crmtTEnK0jiNLTKiIjLKYr6SPQbJ7QNpVZCQ9GVkQsCE33m8YL69YdmkjLxV88muHPaIUrUnx2RVvctvp3GDsXv5RGbHLRyiyD0QSIUUEXVZck73Tg9z2h2d3R-mVSAaLImFKun8ZRCs0P0z0YfHlqepqamJ7EdlVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8vSnUtgOtCFmldjc8XS0n_2VkqoHC8hxe7Ki9IXi348MCtmqzPKEZrYi6Dx9PswJkbStCFb_GuBY1xJ7lVHDp1aNGgV4C_ZpniDsbTA_IMwYDthRXlruAyELzeSWLPPrz5_EwXNZgZB9ProOVfMNcGWV0qlIHfGiMe6vYYRVyMAHspvj_NB5hoNkaSW0vPzR8BklghPc_efIToleRgR4-0JRfVI1xipBTe7ejaXuiRHbX2XYzrIn6LlJRbNiyA3fEVhaGWAqDAwBGAnS-eOwzlhitE5KmpTDW6nL5HCLbEaJUkzOPpzQ9v69_80n3fY2006h_Zxovtbp0AWVFvhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lsNB6sC020E5rZGNfP7elMeCjeLYA93EhuRyUmj_W_LkBtYeizvFkFkewqaC3V_i9J8oe6ertBjRh_x1VIuKdxZEULveuVfkScSlftsF_52n7aNPqbTLUxbzmVqDKY9d66afAL-XbUVUrpsTTiUvanNOFXit6MuGetAdIbg38ymZvoEqaR83BeSI9AA85xuLennEo7bG3YymZwg50vpCT4Tfv_d0uXBMsLj9yFqfe_wgPxjJa5rfA3wpUEeAUiHjwHcWngYTUS0uylPYNQDaPuSv6SpFVITrLuOUq7kCpPd5xX6lWU-PmShpQXy6mjJQi_oMDHS2h_gCm_jCwD4LGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unwDU3CytH8PVWGUa9HNubhph8053Vw3PvPK4u7OZjmgY0fMd5XpmBohUCTFVF6runzeW4XtNN25sd545GL0c6k-E4kMYD7S-XQoYjSEnC9H0oIGiBBOsf-YpwTBj5Gd8cgJaIt54cBaym_rj57t536YOwkBfvooQYT0_Ag7KrRxgQxvVluER2YDfzY_k07FYnbq1x0fnzfdPhr9v_OSgrfGh3vEYfO4AtbehPmYqW0mymJo2qVS9ep3YBUMKS3RgGvuLOX-eKIUU7gF4VtOAZm3EadVA0LZbs7uAmqzfnj8U4G9GTKAJDdDJHDulscf90xjQC5YwEFmmvia90qi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=iulNLHp7O7TBRAgJ_6Vsljb2yiQTyVjA37jwkdGTp4FFJz31WT8QLsUrlWRiFOV0GtiQQQHemuFJ6GKKzwu92NF7xbLdvkw4L5TguIbDCW_dgtE_jjjjqlXK8qAy5_-qnK0UqkCOXRGSWglYnGQZJgTS6d6IJ4IJEOUSnHmfsJMBBfNbhTU6oXuGw2sgY78JXo67jajx6R6rd8puwKayjmxCp3kHKhfDo9pysZr66zL94Mqdal8f7M3NZvtSuIcuFbE5yjKwhGidhFNXPuISK-RdR4pF-MiZJzMNtEzXHCnc65Htr_R0EVICRZv2n1es5HXTKIDXKzR-6tAYmMaHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=iulNLHp7O7TBRAgJ_6Vsljb2yiQTyVjA37jwkdGTp4FFJz31WT8QLsUrlWRiFOV0GtiQQQHemuFJ6GKKzwu92NF7xbLdvkw4L5TguIbDCW_dgtE_jjjjqlXK8qAy5_-qnK0UqkCOXRGSWglYnGQZJgTS6d6IJ4IJEOUSnHmfsJMBBfNbhTU6oXuGw2sgY78JXo67jajx6R6rd8puwKayjmxCp3kHKhfDo9pysZr66zL94Mqdal8f7M3NZvtSuIcuFbE5yjKwhGidhFNXPuISK-RdR4pF-MiZJzMNtEzXHCnc65Htr_R0EVICRZv2n1es5HXTKIDXKzR-6tAYmMaHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTcJg4mLbqvsKrG8jje-Udp9KNliC12xIanPo5zUmsCs-5FxEi9CakJjeiMhNErxizbplg7F19oPvrj7_QhBL4GnFuw627TsZLHDEVaOo-gZALnqYYyzNXosYtGNKJzGX0mJb25F2t2zVI5CBfaoMOUVHZkLn-hdZys8bMN3xVwb_iwARhaSF6c8NYJNYewmLh1hR1tX1ilaZGGMAiEMo-noTehqAX3FkIz1YeRLas854JZoI-VxaGNy4Uwdq0VZfW-p7rJ9ofCLieyGlUkcKlcJNJ76Yv6eTqbQU-u9nFuFtGBl3F73_-NtcB0EGGTlL0M1Be2Ckw2M16IA85emtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVY11YD3ikJ_mHlONEYeuDilsiK5QgmdI86j45Nq9Dx14X_YB-cxAcyfOYcRtaDdlJgzwovrTI5t6VzhU_zJh1tkhquK4cyGuYYfpR-A9bKRBNIbZ9qBWzn-BAEZJuYIae28B-McA3rpPJpYrHa55xYIf8b9BdvdfmnfGnTGR6LxiE8lL5XljfVP4Yo6JXdKoQctYQ6yahEDSW9EyV9QFG8H3vIAJsxhPmN3A4RyrCIsh1Z9U3ctWNoUDgDQtD-qgidrsLHLPo3GPe2R9-EOWa088MnGRgPcg528XlKAQQ6EfRMf2vluUYgqSjIfBiLzoR_8a0U31W4MRWXIamC1Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cm0VNbJl9XJQhJc6c4V34-QlfhQyS5BuiRGw_9BRa83vb5xTx_c7thURZcz0C0I4C2UCh7W7lAkcAHp_6MJ2Ocdo5FibJ6WsPW-YCxY3GtGjvfszu8CgSc7V3GuTA4kKRpseh7jDOlVwdT59HoxFYeLmql5zT0QM97caDUvJCVxlMfF4cY-UfeRIuwivorKyYMkDXP-Rwqq7i4eIdIfks3nMD99oawB7bHLdZwvjt7ve3_26N-YuPj9aq0FyATsHLjW71GYzYCWqzbjWYduM2fEyevM-F1TiGQwpBthJ0ppLIGQ5s60OJKlmEZ8cAhtNHO-EXCzx1TJR4GseRXqbgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXrgRCVwtMFJFCiqq9ZJ4Z2uklyHTau4fksolBiz79WTUV3A9BLmNQvXrg1sKtJwAy5eBTfVqXd_pEWkPtf7_OAiIXllrjzFDlymykACnNYcHE4FQualcjTd50fD4WZUTlrBnKdnvo6cTx0D0unGGijUOQcjiM7lT3hp4dCXXhjGve_jgcOS_u2pbk4jG0pQNgshWEvOvgfwGBMvaVCsbz_lrMreaWLlHi3pYE9uK2i2UjrF5oqvpU812m4sDD6RC4crrBorw-OMQkzye0iclfPDjyxw2FVEJaACb83oQwKdjsEc2Nq7EkUVKiinru8rGdoiC4M-9YLf6_csvz-NBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOH2HUW6eCXcaWhIhwtcxxgYunra47IvlKuYHLp2SnjA6VAL1KsnLUuP_lG0ZZbZj-e2oXR-yC7eFEHaK2rpXxTlLp2z0rH77PG4kI9Z-qQMlSqLsk-DPVnQcKlu-B9IgidGFI-VxyG2zljSqeod9BOFULKBHUHNyrozWrA1ME9tE_PUG7y_itGbegBaUwNFyqqcP9UWObvmsW12VzmxPbms29EJwPvpAf_FcZgWZnTMbObupNHeXJ8FOZWgGfkUNN_Qc8QNj6lm9qCQKrSvddHV5vi3OaLUoTGP9uCdycb_8XC1CmNmVJuJ0ezLqS4hQKV5quTK0tjiqWuok2owDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojB36thw8bm1pH1YwVc6wEl-DJH13xGGGrWiDhss6xyV2APPT4LFtOCQgO2GXFXTfzJyhXDybpiVYpmfCKupJzwQh3tKw9piEnlPYXbhokdVbmrtbW5nZlz3uFMJIsUC7ZTGtdWzQdseXRXUjrDiss90BjykdTRSxrrkP0iRNETY5Kn61eHpGYTTdI8ghjqVQsXn6YA2CtWOr8fOTQ97pSRg14fArhg__moOjOo_Ga-WC7MI0zIg_av0sfvV0yLz8mqR_4g27zPkz0fq_NhkGYXDqVDqghbxUJH4Zf61SwfJA4X1bObg3kSNxaXzLZHeHddc9P4uEpdVZTgAl1OD0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W18XBUfsrThe6iGwF-8T3dfXcXth0s2r7x9by4JmsKMdbsBipNHKChC4x9m5m5Wb0x2TCTIr_CY8lMjwZyMLaWo_6RpUCPajfbX9QBjaTKm9hzMB2CsMxJhiDuq9T-o1UyWzg_JzR1sftUTeEU4cTomI6NsfnlS3P5mTogN4l9G692csY_wAvh1p4z03rpN76bthPenVrXsSI_0aPPDqTjbkNNe_2TC0nNw-Iaez67aqHIt-jAeB6PfHLzulVR2TNsnefM_V2STxrFUiFwj2IRWhbh9yNL4mxRW_yiHdy3O9PMRNDYL6iYfgmkFvT18pJea6JAI6K2bhpO7lpYldAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soKJqRqOCPNWDVPz-_GfKnhEMBdkhdoyR3-otsyD-5XHgLOMgCHRjBjXszSWn9a7MmoBcy2Q8yj9XnRqcWErAFg6o_LgfZZBXaMeyaZ8tNnfk5HEj_v0L6cTKuUL-theBpfgRErXTYwvFZ9dCO5y50KQxiZFrfa_kEzYXXCVA7cW-LniJh6ETJvk9AKfxfqb6-7ZBdJWEte7VSSp0CHCdsL0OMUMNiRYkPpX92Xg6sSwzg9_OIAOeEpyrRugejQTWhVYXucjGAbDTrg36qnIqWgvWe21wVnh7QizZz5VFkAMdwVUbJ-5KQIfY1rTo2gv4ip8T1Y5ue0cv68dQ2rGLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxFWIJ2b5yd86LwmdxAXfBqeyR43vWGRzqRjKZwZLgM5OFh2B3012icYBJgwm53vw3XGfOOHJLmJy_gG1ApBwuCsg5b3WtAo72s-iE_y1N_vNgVuY5yLpXGCLJL2wnCa06ddfppq0S3khPjTM9lmRkHCti5iTIIH1fNjdMl2SZ3vzxiiKXyeWkrbdlHdjYqSm5hTZNzpJZJJWy-MPrmPuj7nFP2FmB43m8D7yXUrDXe-B-F1pKrTvIoiBMaOuPKXHPDpf2lNiT-hapATovQCrzt2rYtInh7YkG0e0tu5MHVao4lK8kb8DS01l8C3BtK0pKZ7VCsXWgXLVRbDz81h5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezzQGxTqDMPtQeo-p-7j2Y-CJ1yTKZ8RSnBCu7x3bvrxA3MTFXYPp_SIWMd-Ljq_9Q_ztxXiMd1uEXodmBovmy0tRir_hAqk0zDpXwRnVuavFOeG2Zc1d0xH3gpztZjeba7xSqye9usokBGMQPM4jwswRUdpGZAYksH-ZKzTlvWLRLyxXzkrjhIQNVtYrr4DqM4S6B0W1-Z40NpCoMp0S4ZrqAbAotQnoHidQ4EkAsRgPvE3Iz4E4TZOUOjDrYFf8yfRqDfERQypfE9Ntqe0GHQ8VA9peGWNjzdtgPzf75v013EQNG0PZNPPj7XQEhJ0WZFPYxFSu8d_MNGyvSZ0BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWsx-rHmh1HB7RF8RQkL5GbRfF-taK2vP5QG70ZSE9W4a2PQk3NIZQomVONRo7vA7-QsEvYllaEP4CmhNHSNax830ox7x95bj3XBz7xwnpLH7063CGapQ1zYMuAge-K-6mq_QFAuYSmoHl8IlLMbXCyJPxMOsu6QMMcRilRWQRekTwQy0VnKKWS06_OAxYJzcjIE8aVUF8Mnyhr70Ll9UouOdc4T_rPSK4JSAa_WZzAyxmeRR-CftIsXlRrgzvfCHhyLHGu2pl8gtYH9_hh5OZupMC4354wssBXJ57lgyGFvayUOVjl2J8Dnumwm7XKAmLTQAM9NQhFtogxs_ZJSSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7Zve0BWTA6nsTGPFCe0U_v3TSAxD5WBLheghqna0W2u5VHVH3kVOekdq-J77M3wGZUH-_1pc0IXXZvfSXU_vG1rSColwfpltFbnnyGo6B5vzdcuBmWweWoj_yJxtv3szIrl3cTnIH540MQ73jzRUoF58Ar3zAZ0Vn52C-oZUF4ZHq-W9KppPHyL92v51lBDSz9V6G3WJ0dquPly9nJXpka0QxN_yhAMtDsR7mW-djbDO5bNJB4X-kCH6K3_KVn2G7aF4xprfF0Lvat8GFI2mM0rcMsmMHD746-xgT2g5XbCZRBC7VcSuMCvQ0DA8XA5zTGbWiX82elXelNMTcvoLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3TMTnCZnyvlvEbXUM3kA5swE1AeMSkaOCqVQW23m3xF1aUzwHrBBlcpNhnjAVbgcyt3XCTsnUODiChS1S_rzQfZD6moVjnSjwGtp0BcG2rQ4_t7-8nXs9-T8nM6WWUi6F4et51UXthUG3SaYxxLB3pykzG4gjwdUAKKLOk4XIdMibxJITahhbt-uAFwKJWTDLN8flTSUZbJcfi8fZk8FrHA8_7iWqgQSeWaHe33eLvGjSybv9TJ2T8Yk1_yQ9yId_oYStIAXjip4vxb1FjVRa2_lnJERB7F_j_wNubhBl5ZB1BF6pbr5tM7QQR-ju0aHjtEQJy_lfCweh0hR_35mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3XLptkhii0SXXazkXBCLvjmFyOLB3WZl_LgQDbcIRQD9lyyie3kCoc3O6EevidvHXQROncUkLAl83jTtz55WYKZPyIcI1oZpPdkiIB9NsDF0WoofjprHl34E06sWY0eaxGeqY08rNIO1f6fK3UVjf4sOL6IV0jCW4Byi_g3YdoMvZg5y70e9_3a_sQ7-ltEe06vhRLFj7vlAi_NuiE3emOaeOtr1GMc_OZjSUVgkQLBzcmIhRFY7JJBTbGGtWzyGQYdk4QggXjAPtsFraZI-OkKj9PZ82WDru44DM-HIj9inqKqSQrQoj1VS27zFv5I8EQjjMVgzc6JAYbqB-nN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TeICr9XhjBRUju4q1rjEMdUxBwi_Kx-ked2GSPtKaqKq0dGL5xHtGJhQXBFI7fjo6phJWPb6koT5BYQCM-Eo47VDsqkwZvXrsnziiqHk6bjM3zjm8lFoSu2TuuIn9Y181jlnUUtWCssY25DEqkHAXUDNyVZ3AsTXFigGJUbbnxH7zT00D5OWft83jFO3ditv_RiUcbHszJblDzJZmNyursYnO9quuhBZbR6kDdMD8VqilPbLoDRjNndveBXtzvB-8iRze6DJ1r_6b8uE2H9XSZNr1P5kI8_FWNvEj0A3Koa8uJncpbHZiX7oDrTZB_3CbqTieigBZZVeprRDkMEp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyUI2cWDHeLOeIoO9jzv3v48Ggk24X7X4-kXPPqolDR7fR-fEChDCOQWNsrTSrla7nFtTQBNdAeq2pEVhg6GLJEiMNgTcvrLGRjMTSBzBD7yVxWrGCJgyBllwkem7YzVDdIkY5-ExgY3Bod7uYtMjsQKgeTOIUVCqzPl4vUH639kTQIL-4nTmYD1bVg4TdpiDsUC0N3jT4CPPv-qbsIfqphxfxg9A1Gm5H7NNa17pDIrwdDmwK1pLXdB5xG2x0OBN9DfZDXAVi3VxYKOxc6SmottZQS2EfPkoRJBcbpzTFbDiEAatMUyebOHLwUJvCr2bA00g5kwYSbIVoT9FXlZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYY1h7hdCCNREQA8bwb6SBntdgDVrN33dJZQI9Yb2ze2GYzxkHLSbGlqUuEQH8RTxI-SEtjdDXBNL8kt53kV8epKTx2GNBXIOnPDQbUGjrx9S3sce283WhL2TZA48NgegyWcs0TJgsAPOq6tTNuPkerrdpJPfvdh4ZJcDByaGQot-USoIAH6tuMW7Z7qBP19lxU6WQg7wb6RmW5mf1Yd0CB_NGjq2Kd8Ds3tnhFTeassSZ884EN70c_QrU9KIfZYa1kseidV40lPkkRLsgNVew6GyzJ7VrzxQLNvP5t9lE1lFcZeARpQgG5coHg05NG6GCP-u5SgKIDIZJfb1UVrGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU4_o-NmwuHKZxCaMndNhNtFKQrgbiSb--f0A9AtHtdZK2_v8YDkIY9kiYktUTa-JUzxvZCPQTdojdjl5FozyRDMnXRDPWYn1_-vgx2WUnuXr6mTQseVAzqACPcnhvrG33OnSRKjnsGXv0SweRs774tQMG4aCYpjOTtdD3sHYDG9Gxz9dMbW0Du_JTjP_qAEcU3OwF5Rq9LiYlhB-boLtWx7Hj85ASIwalZMW1q70uNS6yDyy7eIJy5Zvrd9YmskL7RvNc6vCJOKfW4XCR_QQkCGjY3r4m2yiNojo_IOezu1nFgN4sirv8fvjBvBsTfm7UfvgMufDAOu9b1i43kUdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndKiejHb33zbrnVusIUXs2YGq7dIRHTiSmk_8CnRi863tzouCctf7Hkh3euR6pGuE2387CCmzQdjKO-1FPEl1ZxwoNce9bmD_D3Ejeq34kfQAExmzYY9m_kwjz5zk61FbM91N0AjRRM9IiNe0qk2t9EU4CAXmpkOR4Y8hq0SyUnElvhVGUeq4EwafAlImX5H7PRbu8_M1zp2W9vpYqino3aGhO2JkYz1YGlcQHj9IiUO97CtU202Z6SzDy3XcOaJo9tcO4tKlGC-pZWpFZfVFTRmUNw2s35_YUzmE8Ca3J1oBR-bxN9-Y6xv4hMaRrLjnCLYQM3t_9eMNvZb-lZLBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfzv1pUWHWXMZ3YDzCCBIKPlytjfHDevP1Pn9T3n4x6mWdRAaryt624ROx3aT6eCVXswxhJOkyAQx31R9yazCA7OC5QPmIH4oLVMkjqSUgduQOgOvRl0fWjladDBxNBN83h8JGO5XI7yFdnKSyzdquIevfDV46O2Oi_KbPbCc2VxbsqYPSloMrXU9nd2uPG9SL0w8spZxBWnmWbAfjDZn2eFxxVBPAAS6fIYk7DB7feSq1eRaDC2VrlHfFD_HyuFHIwHbm8I-i8dbPJwfO5OMNMP8xLsa0viL7CYkA99Hg8rKVIaTsnu8aM6nNA8W0rOlpg-CxbafGSSZdea1AdwEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiNKEU5bNC-eG8bo1zFXLYhr0uRNH8ttq3f0jRpR8AaKkPbatDDpQV7DFsHPPZzyQ4pveRVXqkWI35FQID_OnuOU0DkIoc6AJ6g6rGmidgWquNB3ekN7V_HcYAisbdEyKIYVsL11yaJbZdhSaie7F9jbsQLEMSmJ7ALfrdRYRgWn5bz3xHI-wbtLL29lGSgpAwBFa2tqx_eUolP3ikhTq6LrrRHGkVcInmTnO2uGT0YYOTRaEjEtfSGUR22EdYVY_ECA8ms2oQqhu6Awajd1QEqx-nlgppB4raNQx1x_bsENQlg2LwmHYxIqTIio8YsiwoQIz5M4DKbzZZiRYmQSvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFv9KGF5uJz3eHwN3KwZ9l74w89_4n1kpdaSyXOPWzw0ZXqdHwUD7wYdxBWM-ujs0So9aW7TFQ9iE4QEiqCvDTfKeVWYifCW5SeM3GzM1EsCFwr9onIyDqsVljhVn-96u15wk8q0bXO4_tZSsWRIBFyUTFOCCDwTVBtQ3ndfAY8J2lK-fS9PFBR4cBVLle5kRFyvwdc2ooMm29PIZQKZqZg_clFr7295eMkp1LrSKR992vA-HxS84-K3zOudY3OGjPqWiLbOGnNZ0lARY02lZsZBatOYWGU3-emMn2J3lGQlFf4In-yjq6WBhbnNTbhmDfjDl1rHR5MaaV374TNIIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4IVBoPupbrXHR6iWtngEcjn6TlDvrndf371jY7Pn8VLLuBLBTWaaZq9fEz4mNA73nVaNzONevj3vhku3NTLfJLiJtghxLHonZzjsfEKw7hO3yYA0jYYtpjtRTGBG9Z0iItmFI_vnPV5ERcJyQ1fILUxOEhy0Y_XZHyUAoiAxGO71T4qk89Oj-jUuxneciRWuGtVc9yjlT34QvBfCx5KRVKKSaQgaMbmadLw01HUNZysErL1IDwt4AvyGBMqBqnTObb2Wv64NTWHeyc_PwITqVBEoLHY_4Tlj-E1j6qYhOOqyEfjQ8XuOe1HcvQyiYSE2lS7RC3uSoXC9mUIzS5kFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSnSHFxQvCOeUt2BLhPDfP3dtIySDV7G6G2_IvGt68kKz5JCZIkKsUr-ihpDdwu9WnHiy6if_XU0NZP_KBqJg0_ycd6KsDJJlKb4TXf9XCHWASS3l0YIj4mcxF32vI7XDqs_fD9kXIop113_Rnl_qULixHechZFyUoRcBo62IRaG5wg0EfG7Tr3ieLXkLvhX36d-jQ1iXzZoCBZxnA2BmTC-4Gl_Dht19RdKc5brF2B_JKCYJHwCSM5wyB8ZbIhXISJXcQkIOXsLr-7s58DRtvSSRWqaGParD_y8Uzcq_je7a6AinOuLaJeR0eyoKD6mpO6KpxPZ54abvOtN_dP9bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_GGGUMDJbJdgzAj0RoIKgDrwgnYQF5E14ZtX0u83k5sAJ4WOjjdTFgTWsFN-oUN6s-jf6243tNl7z2KDq__YBjwVduJxCixT7OqlSgMvh_jDUBfqDkXyS4P7uhXYJG09WKiedPfrtGIY8fCCriiooBVYMcmBAx3IlTN5Q-r3lpaHW46ToSqPTfzKmRPfDQat-P67ya-FtqQavgli0V_fE7VS0kst21KH8sYxM81qevnwlqFSPEh9grMwJ3ZRK7RrdxDNwEuloweaId7SVd8pz1A05hoAvBOwJpLrLN2USx2JGwnQ_O8T9V01TqN67RVfDAQm8REIGqtGlKFdYhP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3caltGuDO1Dbz-KHHYzDzLmFQ80QCanhfioahfdmWS9h8P5V4_XuPDy63WajCQdNvLaOnZ3YKXpZv-46coX7p1KhVgYgVJuNClWhDXGJtHLO8Ku9TF1mDCQU6ESDwYW4L3Gg_PmB2U7czO_5cCSfY1VC42B7q9VGeo6MYzKEC6zwYNC0pbR6ORtne2aGr923PLtxVdMJi_6b8kPhXdyj7fwAOQrkdNp7yaW91wQBIh9jWJqu8GYkPFGnLsqOVdwOgtaJ8eZhoIu31QsUWiYTyDQxhXRgvFuPd2rn6KSZUSQKDxL49B25yjYO13xihYgYdhK_i565Smm34qQUNV3Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLBLO4Cch0dpYbv44gHfbHQ-rHFAqU_xMYEkPO73YmneCmT-4VbajFQ5GgUGjgkCl5UI1Hlpo5shNqWPVnBu_wU73YH0oI-l6HtwPN7ftXi05T8rLwlK0H6wNc8AQkDAi7xYNn7j0TX5FIczO882bYdA24ByIgiMeecS-M2XHNAZEKPRf0oU8D2wlPWlUy9kGIlndMOqSdChoaqycPJiwznqFJzzL6BaqkNJnvlLxZmnmMPBZa7BbIx9tO5Mz4w9cw-V6_SNVoGDC7Ci5ByfuetfkNjEXBMVft4yhoaut6DQ6RbzRFVNvpHr1S0neQpCljILQCIcz9-cIPqIZDU-Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naG4QfR38VT_spKLtcFtzzpdytLN9pQeUQL1_tj0nM7-Pff7S51vwRC7T3q27S0s5EJfPAG9UcGJ_6x_USkQ6ABNFODyVjm8Zrq7nEIGuZ9JmRORvgkCS93NzEpv1jUgj7n0AIUJT0SPB9XVC9KMreUbf4FDaA3135xqI7CjVfKhF9QauCCzlFqyNBIO0niA210NIdpMpHAJZWUAw7L2FqrhN3-9Sezw6LgxFcidtAHPuV2-vBPDg85KrVtCRvYHK7j9cums3002ms75ccSyp8Yo6wCpavW5nvVY7RJipT2Nhyi9oSYCGapcYs0SRAfsWL78xVGfmvZfz5cywi-RLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0GCRgC6VGwyFlDmewGV_LU3TvBLM0Us_nyqF3MAG9Wggq_mEF0P_P_bt0MguTHT2cxvrD6o7HTsjN7v74dweJBDGeSM6JUpYbt5NFdnM7N8ABfIiVcsJw_K-l3Pg8EUCBXGrdtca8DrA8vhbQwGDDIY8igdZ-mYjBLTPPqhEUSlSu1zhFGVu-JWmyZmnn03r8BdvQISc0WfGalFFnBPJgrJP6DIeXr0yzmeiHSqN1JyDLMsNaxBJzNSt8QqpefBQuNIbZg9n66xkYcXCFuO15HGUkTpYY3_GxqO9ra0OEbaNjm88jaG1XSDYd5eD6NM17S9chb0v9uefkuxZmsT8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqEaDbB3YtFADzcgmvb5ty8g4IWbgzWq0r3qX0lXQ6uRfG_xwKXH4qLBB9QcNWA215hKLzYEz-eqPgJ3PAT8mIfRubZMkeeL3AJAEr4yVjv9nFSUd-aPbeBuixEVRpapJVvCdL9zc9REUO8vFLY-m3wiGJVCu8ZDrQvHc0C2raFjp1QhgMnAaILkW_L_12viBcFkdAXqtHj5XliImjRyiDaNC03k28gwvAJwpsggH6TLac9R137RXyi9-jC21k0Nk_jOe30MR-pZ2Vxz32ZkC4fMkAHIUCstxZdGZUe4kxt-pNrJBsfQclfaNhrPAq42FMKDobNg_HVzYHfxFX2VVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjyhrcEOhtT7VVy6sidjeNefjbT8yuBU0fQfmad5lxZIhdNL23XlyahzalJO8nTcBhajfGIxCMZDGtS39jAVxcx-2U6ME0OLgrB-WBfjQx1VRZ44nZ4rsCrUh5URAoPXkZy0wj8GOLLFBSrz3BO2faaNogBOtJA2VNpNMAQhcUsmmztNooiS0fIjkwuXreUasl_M_uk97VNfBezG_9MKODcS1h53muhkCd9KpohcCYuVAY60-xsFoVZDLyaPFp8JCovg2rEaUMvxGGA4gc2IkriI3JWJcferDGUV9Ksmd0w9X3KCq9QgN4uXg4-HdnP-6tMcA37DzPtiNBmHgWLHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1WwYADf0EIp17PE6SJiBBus0cdJy0hF0KCmW4GsW0Pn71Uf15y2mTuvpNDHRmLRWZ2OBbp8nIdVo42XEPSrQcW28gO4Qf4rb7iOqK2z9SdSsnsF5F_7eKGcbVFtSUUzaLLtkOZbRzc4SlLnItbVSiWbu774pLiP4m90_MbKzOCitn2hHA-NJtDolVTPzyBccf4XydvqqHckifMau851r6nmewXA6dEMGL31cIoYzIWGnkzMR2yEwy0Xfxmeb6iPkZrcKCoscr0sGtdLbkmYk6zrDUulGJcSj2cSHlVQm5NFja2wHDkcaSCVjlIibe6o66ChQ0NYASyRvmecFkqRRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0gHX1mKzFaw81pdLU3AvEmehWRav7Pez_NqG29Mx0tnJ1CjbxzDcJa4PLRAdFsTYkvTR5TKxgvtIsAm6hLTOD8CStv3oaIH4upGa7ZKAm7r1khLXFTsp540CbtVpWERAcnCaHcnPUw9X_PQJHaph_N0McRCuigxLJlHfprUEgg8BZwO271Fp0I5ZwnpAokCJi5DcEWtTntNpIYtAJtZM86Y2i-8iNZhsNpCRy78q80ymLjKWXEtUjAR1x2fC0Lsl-OKzHSzfDGD9JouI7IJmjOAvPijmZyphTZdkiMcWj2gYAO3yftMSfEtoAtTPIKoBsc-EBk6tAZL7CkhjaMGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTGoSBEqztRoDNvIZJpo-BGAKORNPnv5orjCHsTXqP6CZTOS0269e-USPagIxoJhhxaWrVUffMf3oNuOAq3Qmn1OaM5u224MqDB7kR-hutpf-pLDciuHKFsTRkF3vBeA_JYu87WiIM2S9_4vL8URFw8FXLEP8kfGNVVl22SxF4rp4g5vD1OF1G8Ldb5kVNV_BYP7e3WqxhukRiz1_63kb-se8x17wdbB_Vj0sLMQT8CYnuDEY4qAi-RJUu3c2bXWUkber1tE_kDW3qsf-Nf2N90sX0pYecPpyfuK1BfYPNq-eVbBY8g4w2WM1_Xwmi5MlSj3Rdd4wnFu4oZK5C0gQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7x4ViAeKnnvMLymA2Nvv2_xPmbiTs4pPdRpy5-ibAkNVupuB5mE7uDbveFytEK2kdjtMVM0AIrENv66NrvNOmq4xQ6UxOF9DvUyZWoE28l4TW20Hdh6MXeBalBTegRxYRh1X0Lg5b7we8UIViaxcbXODK3eCdB2vtS9ICCCfyc3fj9WwNAk_9b5ZWt3RRQQbh9CiDCsr4NfVwgbnqsOVy_JXUQ-25FfyFUDHXiz2b8UHiOajdghW0XlJQ-OSgdOnzALt2G1Ue15hb3RCvyda1eJ2fTvz2S8fJ3sb1vUriyU1eufaZONbXK3de_9NgJ4v_sFaRi5Hh6OKlRbD7i5Pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUOe1f206F0Aij-zTzro-N6Zig9iHjgnJhqTHI_ZvFPAVsbUcfUg4VRp8pwVy1DVcCUHb_rIdcirkDr-rRsjhuPgE-brPRg49fvFtFDx0uR7EmseL0efUbkLTJTGrLeP30OyaZfzvW0O1oBwgdFEI4x8Y-Wa8bKJ3folajWb4h0fPI48wO9eOMxV-A4DCzeWAdEepBMa8Vsn1FwhQ2qb4-OBRNVC9hMJzhLy9ppS3R0-BkowTpBf4lgKM4S-vPiXxcC6bGlA9Xq7sxAgjf6i3mbzXlmI5fhSMoHVpNQfP3_FsaKA-qSKz0180wxCTbt7x_1eTFt_tsrf6oGDeeHldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLWi7_JhRkMp4e9ZnwHmI6VhBwj4VnODopdJVtht3WaCWnFwiOoR7ZyfiE04pF0Qj_wlHRYRF0-AR8cGvHlmAEFG6nXWi0-WzFmpQW069N2_7InJZXW1BZAOAe3wO6DbyHDQfOQXKXgyjbq7KucLKyah121DC-tNdpnek_ai78CgmGWJ-8YLWxd0BYstzRzmQJsjPJu2K3k8XfHBPO4u3AlEHehV71ukUg7zNJvsRDIvbnjW-xp5dAjwKL7Xlm_aJu7kpuqJ96ngsvLNUUDo-K0xoIJPKiUdapTITPNxKZRyUVsdAU4V_S7wRbJScsyB8CyDfnUCFOU8DDzQ8CaN8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1Rn_J6QZ_QYH4RwHB9mnMBpvbeFHVLNLtM97eM0YMO6ASbqLPkGly4OROX1uU5bMqpwJZd1suGQyanxZ3pvP3R1lT_pe9K_vzC-RF-kPOffwvqOwMO--08j1eDECwDweFRYOJF_07lq-vkh7LC3RsA2yb1B5ZOzOZh4jGtvgNEDWilVsbzS7YgAhwXoQwGy-3_NxGyATz-9RbHRHdD7_ZGXNWF1r0ZYnfHuoYIHNktrDaJ3TeVGG-gu7jEf48UxhlGgKVn70sW2EeX2XKLft2RWv9eFzv-ckkHHFFcnHllXup3oLkub5cnFURQO9eQIroV4BlF2MMA0Gp6i28Y1JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjp2bxW2pwve9b-VLu2u-fqAyO3vlHIwaFqGnA37Ona_HW6DIxSaryVN44-AdFzmW9xGkEcGfo9FXOh6RObm4Qkp3fhb29SEju8xIoZ67RVAIZBGRsnT9VQ86NRejhEgQV39f3FZVRU6qxkX-pOlvXScUuBDFbfp1kT8e1iSGL0XzyhY7XNkZNjAuZ_YrQhHhAwDh0TP7LB1efE8gz07PO1LxONGoqLICV0RuGTjXiAscqi50UXNR0ocJunaYMNfPcnXrol1sQhwb6JqgYBPR2OtSnv-KmmrgD_mDoxj5KPS79orylsDCXYSt-nB3xxXZgTytO04wj8FIrrXr2PP6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0qbqUM9koHsPovqcZeZihLyaA1OQfN8Y8RI6hzW5XTOAjyk4UHj07iFy8-Itak-ogwftgtkz6Tp3xBivURaUPlWHasjHaHPlNSUHGb3BK2SWDa2iOnxxWocYhuSfXb5QmwJEoesAfT4221STxEh2q--0bIFg1ETThkRijDFRXFeWel2ToJs8MieYIqUF80nE4IzpdK9HyDj37MVES5nYPNIE2SBbyc5UUgVQGkmCOjY1ldPE6sL9uBrn8hZTnDL5yrbmlruBCBDJAoAfUkVnC678A49qDKiFs1s60fUjzYnkzaU4KqN5NmXCVKqyX44qvPnKLzMfUjOXaJVdcJZ-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pzeue0vELkKman9BQTyDqHbbXIX1dVKnbCqEmnSRrZxLu_90yX3NO4S9CuvRhv4XLT1a_t67JII_y71dl1l9qynFutjru3D6S80ZpI7PiKXwyLokiMkGS6LcSDFXqKI2sYUhtCS29ObZfsd1yePzlkqtPp8M50oiyoFZJzh-CM1OFaU7GvCBQB885VbkcURzrgkMBN4soj7iRo9nMsca5jqMm8AMeVg8Y-__iPfeaGj7XLPSJyQQuJ7d_BFd_HQs-wdr710GpjY8lJhTSixJmp6MgkdbKcgvoDTgNECzBg3FbIlDzuQY50Cy0ZYdG7MKIf9qYpqqAqQ_LeTfb5Otjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWtgkGmBHCV-1-pwbESq2_V-u3XtbtPgybE16K-fUKwOFDd4_HPLTkrf7NtR536tWYKfA6cmdN_rHJsPazF1byqmJC7ti-skfS1lmOgefO8wb11K0mR1B1E57SrUcWl3HBAu1f19t9ByaX7s7k_FrQlmNKjHC2jkjptgWgvHSU0WT-gfwQ43I0tuyekDu0uc3xK5iZ4K50OBLzBXKLQTSmi8db-jlyjteXK_p11yIESZUOx7uQJNQC6PzD_Vit2D681sPNdOJBMTalS6bicmkyxCE3rxQ1dqIB7tTiUSIT3vVV7g8CYFIIvqaZOErVYtvqth8ZdFp_9YYvH8vGFD7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd-XkCuNH0NhVx7A2P6aEm7IvJxis42TBNQZEAtY9i_Byt6cYIqdLqMnDM9bQ0yaR0PSw5SGuVc8iKLddDWLrXfvruAv0ZfT-8YiNRlAchTT1-ubxPwl_6W9G1qyjc4AI3Aw_0Sid-mYxOr5dEBBDbU_Ck458_XIIq0lN8Is-6OWhvzEPtpo5ymyUEmDrGMtSRhTtSk0GYfm5VK5pPCqOOf7FLPYnTVLaZEq8HUCSznFqS7rxeyf9bCRKuP5CLmwLbPqXKdfPNnSqi_wJr5aSagCRazVqvogHYYNoUOpxsoUC-VPPFiK6M7GyYxiR4Sy2tkP8PZq6uk_OyLjKuJwtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWZG_74V1GLXHHm0WTMWdAXKI5UjxsBxoMdo4G5tj3GypevA0E1C8tV8bS7jRde1Myk1zXUa6cr5Z0yAfKf0DSJ86ZCaLkt3yq6VuYE5RuCnHBdFldPT7LfhNBriheAUyGLnaqURmNCF5_lOIOQyZqYAAKisYLi7fxUpvkuEWR2rTbgSgylJf71gNUP0oAuG-hrjokrrC2oQaFIs4SwfNf_xDpHvJoyFHQ0MpeoYcGgtqkeq5Hh0LtEDIp_JuXbw9PdvUzm6-5ED_kwoPCZj1oeCZS1-76lLQKHpnh0uWfh9F3Lk0Bqkz0Ttn9i6VA0nciU7VgL5pP149WHBRhvY7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVynDxOGlJ4uSJvqOuFYIpLotPFazQZMmsathO_E4N8bi7af4RlbKp6OlCAMSg8wdoX4i4sgBa95sD86sEYtiDhIUq6my4Zsy_m6z2ogcFAwR81fx371NcXLSmzV-y_MLL8qpKZJpNu3wjnPD7oS0wiIMvI35aF8UXy8w0gitJnKE593W6CAAXOeLBIfQUaBf2qGhgHxIHd1N9LiGdEgCnLurnd6Cp_e1nlq4rsT9vVw8xvNVYwP5ZAP1O4jlR6SZaDesNBWfE0EAq7kwD7oyznNO-6l_jAyXsZhb3qTOys4cta41eT-hnWf2N5keTPQu0xQ10f1NAj7JvXzxz2wmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRRH0pg8uJE1SNZi7K86-WP2xumw1ZuQK15y6N-RiPDAXWxAP1FWNv6ADASN_MPNweHtqL-dH-8bq3ma9MXFy9755H7rS-AkrtoEXtA8HC71G27gPTO5Mzg9jLpIBzsM6438gWpB_Qht1l8oNfPNKixLmn3cmIyTDjWlcQl9f_4fMDF48KWjReVDxxr9yeewwDpE5kW7DzlzM1G7oQj0uZxzbF0bbDa2TJvj4SBQGvVVU49HFZSt2xsBZ8LkqbUOZ0s_6y2XkJSMq93Q2J8FWz_v4uMBFwc23rZPhZT8Vh-iHC_pGbiOIbGtu1K6dExcs5ZtGIS2K0oP7wj0zmo_jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=StW_SGIyGFHjbe5t_pYC9MLHhGccIxtZIwR4coMi6RNglF59YB6z6luSZUGQA4Jesi-u858MliKTLOWd_F1FzZDek4VW59G1374ZEhAAZHN1uwcU-yJJVi-zBkL-xL4Vfyb7kxx_3mSjTMVv8FNXmlyhEQ5tjTSYOgKVi-3mz35zwyVICsMNSfhov61Yy7OXJGn37ELUqz790LRGTJI0LclGuseYr1bGqDDxbjhYs9BrRkSdCEYaml0aV3YnI3sqtEGEML39olUyMPPOpkw5aI80ZtTOAWRfLj40IWcrm5G7MDOxcg9azoQB8leu8EBsEVhugy0tnOtH2W0J8dF0-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=StW_SGIyGFHjbe5t_pYC9MLHhGccIxtZIwR4coMi6RNglF59YB6z6luSZUGQA4Jesi-u858MliKTLOWd_F1FzZDek4VW59G1374ZEhAAZHN1uwcU-yJJVi-zBkL-xL4Vfyb7kxx_3mSjTMVv8FNXmlyhEQ5tjTSYOgKVi-3mz35zwyVICsMNSfhov61Yy7OXJGn37ELUqz790LRGTJI0LclGuseYr1bGqDDxbjhYs9BrRkSdCEYaml0aV3YnI3sqtEGEML39olUyMPPOpkw5aI80ZtTOAWRfLj40IWcrm5G7MDOxcg9azoQB8leu8EBsEVhugy0tnOtH2W0J8dF0-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUqX2YkFNLNTmDPybn0EVU_EtG79sX0fSrYsSuiAGDHzo0-Fj9ZGlCC3fshpKf3nrt6PG7mtyM8NJv9XHiz8416ibKJH97DHzg7APckKnENXpGb8EsWIs0bfR8NwsOvq4A1dgkkrauDm6W9zVzs8Zafu2JwKUjUygyHrZlBwNJXMU7ERxCmH-i6gXEtZvx5QOhmxiA8XL2xeueb6ehIn3b5vbv0O5uLNDpoYtN3UN8W9So1G4fDpQstrgVomLRfu8cHtvHoXn7OVVF13Ev5mQekBhPhplgvxNuO2GGK3gRmkm6c9s117dG3EBToOsLEwSEgAhgEOQYWv9iE21kDJyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oktJxyU_x2nV7td3bVeoqrP8337DyGSEsb8ZmOgeXQR2E_Fcez0c6Skvlm2gyHbYgIwbMNa0Y_yQ6vLDhvyQzKavw2xqZ9ZVki3lr10rTsHZrfbahMONVho5rCjMWMY6B1qNkXn6fYkzFcE5sM7xlxjvdYAQr98CdyRFKLAmytaxjKRR8wVtyOdjF_p8G-gvLQLzxR_Btu8Hj8Mi5yZRo4yAyflYPje-ebRdX3hI5tr1eacsKjLJn0cfjhkPAxY9lH-g2e14bRkbJfFN2dGga982R6EvrrGOdjaa_2CfR8vGxkg9xHFtzMedelgiUtQ7IR_HVWb2zM61CkVHr_PEGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQJzevbMgJcsNo6ZzXwORO2CWSph4c4DnwZ9xihcB-NYqsPlQI1I6c8byCIWItQgJ-aJA0Sa7JwLjF4FB4WJA4yZmmpiC1xmh8Caf_jbuWQ7D5ZkDVVuEYhke42uERlErNudgTxGXn450M3RlYeVYovIZwZ0EDeAmfj2R8AnhH2fW7-DwVe5HpsAKSHtfa3TzdvPfjgKHqHjpErksRSuCsjaP84LNnzYBq2ZFcouZ_3WQCQ3o9JEx-0U8tgHVyLCA6NsSjuGCRmAaf8TdW_fjriEXQN7z2A4ENN1XTxwa8Z-cjafUu3Zz8WiT9C1ukIN4ZB5XEiV3JSNhipzj9nOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hp2xzEmgtG8g0xYzpN9_VCVNdkDucFCREbgGtTKe8HcW3XMRayggFvX6QO78ghZNT2--wBl78F2_0VJb6RLow2MYQne_51vhVEPcaa6zrOuqjQRqQPUeJbMc2pWT6WC_faY0xdoRxRBij8M21H60ySXSW2b6nJkbKWieMa8O80mYN3Ul9ESQkH3BUU5UYZwKIDZevTa1vVNt6kf7oUzf6ELDWWzSbeS9QF8F__4z05cdAH-EjaJh5ntR23vyRaihrJ8X3blM7EQQj2fOY21PNnHaXiaN0vl50LuyMTjp9QW9tFXHfanuoNHg7IatFjTO4gqtixw_UgUxdnl99PrZ3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_xObvIh2uu8z771b3-ubsbPN--RvsBXMcVaLXCxG26wZiDU709f5mVH321iDZaT8BhVsUwp8iMgFJMBE9T7HOAhupGGzBD8xb6ZPC27CCRSNGQPk_E2En5eUxpkC08mKfl68r1XoyOzP5lLEEpjEawxOfR-bEbhq5OGTJytXDBXMESVBj0pL_HJ7Xl-Hqd0lFHSVSustdM6QFSvrAtRXnyLG8qBwu1RJ0rmnU7c_xKee0_23MS1xHEM7x4MMl4XU3iy-iwUtS5ZVT2xjxACGIrO1NU1J5kkxKwGojQ4tNcHanG0EAG4oqjqlHDmqrOVRfUrX-tCAKpnIwG8g6z34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mE9Z-LZSss0unbhO1qdcTSOihF8NTfSTahjwSStAE1SyzFZm_FGRcyXTZQNENhk2H-orSItBdEDtrnrZ-qgmcYunRXMU6ruNvSKtrR0sAgvwN5a2hv57LWFGuT9sZgwYXZVJOrVlTUSeZ4jE0kQRldrpzugPYypRA5kC_dgV3rDhbm1Ln9cmioNN781oiHvRne2MNEM6SVEebkzdpsbN2ZeK6jkQ3aTLF159gmsQynjBPV4stVBv3uVvH3P466AWzSXiMl79IwPFv_1Mhk0NY9Axxp-hipp7xucXLLTiTU37M5daWV7W5X2uamo8t60_FWt7WHhcMliCftdSND4mUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usqRpeZLYAOeYofKRrpCqKerl6TyrQIo5krRbVg_pNseAxXv4ljBgdovUTar3VfVU_UT-98JKsCXKpJ_GlRtu-GaprPhCFyMTcaSVwtceiJvYF7jonL0NgvlejELF5FLYgY3paiqzEGB_CTVnwAfg1WExd0CLMo_0xgkjyYL70Z6LrU5ezO74Hhr8dK6wU0_0DqRPH0yF8EurMAYYeWBbLgYkfCeoRn-E8s2vLhlRjkoutLlpVDqh5wmG7_bu9jQEec4ahygb6HTQXaJfy_HdqtSPueph0mpY9oQAucaRP4vfqItR6TfqS63dBE7ItwuNbSIM04lYi-t3mvYbu58Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=ur1r3ehbZzCJRAKISqsCFx8kujfb7c9OOX3u7KSDLkLQLe6lB4tuRQSS4O5UxQQJrpkQdgSBQ7_rCWTqxNbds9IrnaPQwt5FVZrcUlcXa_sM9OgVP7hF_n7PtwEvi-Rn67PZ8I4OSmQ7usHxdn4jbrteIE4fMT9V4fyCYavyI38H2_ZdKoVbUyQjxrYVDG78dHhGIoYkPVIHvG2T4ufhUXP-T3DdNfJ3R9yN7aqsUND0v6m73_-Sspsvr_-Vz_1z-MAVCCMX4A68ignzU2Gs74vNI5k1GZuTBeN7PaHuDLSz8WOF7le4Go5xOemevFkGhacs4-rw3ysuPl5yXj1qm2f9PwdgoeBXrxBaOBNIQiMVOtdEDpduUmo3TMQLR92h4qjhidKoxice0G5ujaQFP4E3XdFDbPg1Dd_yIif19lYxYpQBMo4p4zyNJqTp_Q-pl3czfEiIrDLnc5Cz46DPXvVG1f4kllecL3Nugj3sFobbLqwwJH1NnT9T-hKffVsYpctvCtubBCEMgyBqr1EUlNDbF1wZRl09lj5qJ5Wrmiai7KYrRUZ72kHhEZS3kS68oDuIgnZxeUW8DLYNPgOKJv8E0QtNpiAeDVssBE9uU6X2NI8s8ETWyWqw0qIXmw8lNK_GTzItz__tk2bTgIYjo7oJZNNOEUrdwzqObL1dGS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=ur1r3ehbZzCJRAKISqsCFx8kujfb7c9OOX3u7KSDLkLQLe6lB4tuRQSS4O5UxQQJrpkQdgSBQ7_rCWTqxNbds9IrnaPQwt5FVZrcUlcXa_sM9OgVP7hF_n7PtwEvi-Rn67PZ8I4OSmQ7usHxdn4jbrteIE4fMT9V4fyCYavyI38H2_ZdKoVbUyQjxrYVDG78dHhGIoYkPVIHvG2T4ufhUXP-T3DdNfJ3R9yN7aqsUND0v6m73_-Sspsvr_-Vz_1z-MAVCCMX4A68ignzU2Gs74vNI5k1GZuTBeN7PaHuDLSz8WOF7le4Go5xOemevFkGhacs4-rw3ysuPl5yXj1qm2f9PwdgoeBXrxBaOBNIQiMVOtdEDpduUmo3TMQLR92h4qjhidKoxice0G5ujaQFP4E3XdFDbPg1Dd_yIif19lYxYpQBMo4p4zyNJqTp_Q-pl3czfEiIrDLnc5Cz46DPXvVG1f4kllecL3Nugj3sFobbLqwwJH1NnT9T-hKffVsYpctvCtubBCEMgyBqr1EUlNDbF1wZRl09lj5qJ5Wrmiai7KYrRUZ72kHhEZS3kS68oDuIgnZxeUW8DLYNPgOKJv8E0QtNpiAeDVssBE9uU6X2NI8s8ETWyWqw0qIXmw8lNK_GTzItz__tk2bTgIYjo7oJZNNOEUrdwzqObL1dGS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Njnzxr4c86IWrjQIaruicPm7GmMM5mcZhpiKE9R7t1DEcApg0ZQJI2Q8hEeiXp4BP9QtxPI0jv7hXOca68RV4L83l2v1uLQwGSriFz3lODtjAr7UQvMwosFakovbofhLX_FHUW87hDd4JPrfAFW51euMBY8v4R6cIlvADTOZBtBMMfj-w0uePWnZmbZfqMzzteHeNFTcVFIIygsCzmoIKHTwOYV6Auazj5FBbT3qPHi2hijk7JOBd_gCl-FUjeBoi0a_9nIzJoYHEAvzd0bj65rjpLlFmjPINIYdO0nW48w3j5y3zu_4dUvLiYtYNBItgojRqQe9dtcHxFmnkOof0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSE6Ie2eyI3lzwgemqmeOi-Sxj_s8kJqBTCaNpLVP5lQpypUeurqbR6Qg8a5cI-m9w3Atbk4RVYuBdI2Q6WpHrA0_wTJ71x6D-zUZwdlv5aVgq8VwAgBbSOplL8imnxkiXde8b5KmKLepqUuPpgqV3t2x0Gi7Jk8mry_4WFUB_Fs9nyOQD1UFy18-PEJ-dnaHrfKnyin0A_Hbmit8Vfoanxtg2BJMVkEsBk3wQ-be1P_Re6TKEXePo7N4PnBm-IKIjZfdDAHx-P5kv8a8UzscAAVEoFJFzwxp1kg-Z5wPKG8_KtDKRYgn4YlZT1rFAgbxOm9lb_Ruw-CsdRXvmT_3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JeYgx2s4y7XzkbAUfNWaQjYh1IMP8PVnAOgJMPyJV0dk9PuNEH5sO1wnDfxfZUy3X0q7iuoigva__VuneDn1zCe4BKeFzQWbcFMcmXZ0P_XvnTLi5dlAoutyyc1nDiDkVZOSTV6a-KZxfKdMFbIxClgq-4DXVRZnLiIMvXGA_hhihcaB1kfzGqKlkFuci-xS3QdtlplXNMnOf7N8b__ALtk4lnxU_ZJhmkgCsAXFgzbCI5aDaPpMJyR6vwznMTMSwtrdfeJrOCCTQWsOnB2EKNcmOQ6xblYDyzwbh-91gAXLDozNN3DfHFWqEvwAk7_73HkMzGgR6XiBWZpCkVYkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBm7B_oYQPD0BeKeemOHpyyqHNNaMdyVIQq7bK6z2niKJ9hVQMQE1Eyt9HToSsJs480Ttv9psiyRPhNotbJ4aZbWyLwZndNdduU2YsXnSxh_CPPbhoonFDzkF1rG7n003wiyejqSRENPkf4UrWEnrh9nzNgY253T1ro_n5OZCNkxyfup8mECUMMa3d_pY1-4xfXEeK641uTRCxr1PtO35khJYfP5OT3icJjcSKxMsYKfdDFp8QsW4tRZQ4kAi0C7RpR5RAVD0f-G5KWRjtmLzEmNA0Yd8e1-YUFysrAbqBnqlB-5I8QNeuyIPkTxDGG20jRDkEAvDey3YdhiaBIs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHeu0dyEH1DvXtWCxh4OUR9HlwwzW8XLhMvN0R8UDdFg251T1ii1hohbJ-Pjb-fofp5jOvgUQ7KGavtCubQbY4MIIKyl4nS4N9cWTIzJ7NwpQz_vuJFqKdc7jNEPdusS8zBLWp6GroPxrHDh7kSeHgYRpVJbmhIfwnuHeXox1MGtN3VXxqi2f-Met1rh0MD3nT1JsqnufQYpqWFRZ-Pvdhdn4F63D7tXqE--WHTjZhs6LKSbuisj86cv5lnkGgyGLGzfrpmKvCzYCjEgtbQ64KoTpAlsyaXaDD1kCDQMIxs42-aEUSHHME3yjfGXB1P15h8DrHink5QijG11NL24lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZrdoRL2V6Nrn10pkEVhiTsoNAAT2M_Tt8VPNCLHgFNh9psVveAcIY9vhp3Fn6-5sbzHozkQJxT1XcO5Q1Qid3vIOINsqc5yllV1UcAVQqQjwQwYvS36hlF7LY__AoabYLuk59KYB-uvRQufIrcDOWcZqotEBGzSikPhc2YsLeV4L8FZ92_AKXQ7cGtptMCjNM1E9HiB76iT7GaGpnSx54kCqtN21RpdaBXlgbAAPwgwd1pfFBquSdWg2aTteAJJXzZrTAGhnUc6YxMYOSTgoZ2xaBsYe0KGeIMh2qD568xIcUGt7Z0AHClv-ykENTNUt4pDzpIe2Wrq-hr_3y68rrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZrdoRL2V6Nrn10pkEVhiTsoNAAT2M_Tt8VPNCLHgFNh9psVveAcIY9vhp3Fn6-5sbzHozkQJxT1XcO5Q1Qid3vIOINsqc5yllV1UcAVQqQjwQwYvS36hlF7LY__AoabYLuk59KYB-uvRQufIrcDOWcZqotEBGzSikPhc2YsLeV4L8FZ92_AKXQ7cGtptMCjNM1E9HiB76iT7GaGpnSx54kCqtN21RpdaBXlgbAAPwgwd1pfFBquSdWg2aTteAJJXzZrTAGhnUc6YxMYOSTgoZ2xaBsYe0KGeIMh2qD568xIcUGt7Z0AHClv-ykENTNUt4pDzpIe2Wrq-hr_3y68rrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_s_DdBKGCVaU2g2_WSMXotvLKNKuLNv0Yy5mXRPX9HPv0MvjKrb6m3v33QQKXMyvUoQ9OnvKOvlhnVEbPMkb4_MPVChfUxAUuBZPkItaM6w4bP-bNE3xlV0TJlCEOtAmZk7TD6mSA-6YxAqMs-zLF-P2QbLQsDSPCSEe-RSiyMK1hoeOUfircJ40aphJyuN_DgOg1k6ii40dWrloYM4JM9UEGaIPXsHdZHhdomdkFQNsA7dQBoVn73XPjGfGQk489hbcXf1veqykPVh96TU9YC_01g3J8cCO_DuDIpZdlElsxyDC8D3VQeK3dfbatKB8w9EhfeAD8yKN3E36cDFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diONTPg-zuDGYoouaBlp0OZe9NhTLunljEKzV9pxOleSZ-tgNhwop_CwXzphZBHAdjutZfHpHsgVlnJNUGbjfkj7sYZ_W1svT6XRyU7eLNh7Hk33CtorjXkTx46sMbQEPw8j3DvQhSWTraOtps3QNV-6VgjKtpUQO7OaU8tCCeq2IJpwQZKnA9TeslJ-cGxzSRywMbgNUyUt4xzLUkJsMf1RPxeGeUothLlkFn0Ag_c21vzkt-RJRTsAt3WPjZPN9Db50uGhT7Wo5eGH3GSO8GMdlYzxhp3zBhgf_efQ4LjGt1A8EBPZSQRhEsKwE9PYpzG4J9ML9BJnO_ue8154OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nprcH0tGdh5x4rUrJgbwKrbxmvBW0Nnp0_zXcZ7-BIn1KLl9HLf2dsbofdhaVlkH1lehCI4NIXl5oN61dpazBkfJ-Za08e1HGCzkNDMLhBpt1JErkFkS69TfbyeDMWkmJaz_SnhJtFb9zA2iNBD-FmmXfeQGwS5Ac-d95JNbF0eBLPUbi6FiAiru8q_gdsnXLJm-bm4gV72rudD79aa9TxvpeNl7giVaK1L8m2nvIqE4T0EQGEatRKhriQ6xO3EswMW1E3BDk25F8BAfOPoOK0V468zYp-WEa0z5v9VT3IDLGPdMZmxbdjazrR_utfAeUgmRwDOU91wfJOhkhtthdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyR2o-J7uVgsSOwRtJ6z_cGfcSkse8IMcWuNtziSJtP6AeD5uM-glR1eCccnDJ5FoRWyQeIpRl43TxHSAPQRXzAtSsrED6JZ8Mp13uNwND7_JfkYATLBd0-WlmxCdSFyh27VIWhYcPLYcQIcwWR0F578-kGXK4sDRxNLynOvmPMavSe21JwprIyyGIEZJsZFopYoul4GPwC3YGg4dDVQM6txdDPx5xp8-BLhCvDFqtVk2euW1Btu25egeQCc1T2QCZXMGtOkCHuWgGYnf3So7CzUZbOH72nxBaVjtEJCGODDk9TcC8U-BqC1AdMuDEVuFNUG9YTJPsQiyZKTqBF0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cp629goDM4AYSqW27_3rpAp31sNZJdRVW82J76rp83RxE1oezlo95a-EsTed-x6zJTZfzqTFhdvBRZOlKnEbY1tHvWpF5dTDJMHnV7X_Q0YHDoeHhaeM9uaedZxhVdw2rgLV9gcJF7StCYWrqbLY1ADtLT-kTheybyd06ibHPZbNU8mi4SigxHGTChk-y9mbeLeQ3BAm2-DOV9Jpbu3CyVpggZ4KnWn0hnwIUQ_dDUpxfQUXvVFGS4jT-xb7LF93Nm7erCvr62cA-ghNu_zG-6WGWMe0z6TTIv3yBPodXDbG6uxsgNGzohYE-a5BqcG27oL0AIqM8-1P0Da5LNPBog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhYasoOHU4lVX8DygL6o_wLqP3mnIfRvYUXNLw7DCBJ-jw80wGZNICMYJXLutVoqUTWl7O8Y-VRBin8QxlveIIVSb434ISZJK3kg2i-aPttvjogyqw0gU8jfp1XZ2U1K6l7SWge8Bsoejg1RclLhljbhKf5ioh9T4Ad9VURNnQwcp8jnXKPtcJj_UujbxYK_kth-UZ_wVFnuGbV9_carJe8LAozBregzJ-mVBALCWtkUJoFSw9O8R4AFhy2-aXlwD-cUdJV0OvqrCRPjqO0lOzEYlX9QOJHzbdOajX0stnjusdjyNEVoqG29PNLEP_OreOn10YFgxhzxyyhYsxkldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آزمایش گوگل دیسکاور در نسخه دسکتاپ
💢
بعد از مدت ها انتظار گوگل به صورت رسمی فید دیسکاور رو در کشور هند به طور آزمایشی فعال کرده و محتوای توصیه‌ شده مانند اخبار، آب‌ و هوا، امتیازات ورزشی و قیمت سهام را به کاربران نمایش میده.
♻️
فید دیسکاور روی دسکتاپ شبیه نسخه موبایل است و به‌ صورت الگوریتمی درباره تاپیک های خبری، سرگرمی‌، ورزش، امور مالی و سایر محتواها قرار گرفته است. اضافه شدن دیسکاور در نسخه دسکتاپ یکی از تغییرات بزرگ گوگل خواهد بود چرا که بیش از 20 سال است که صفحه اصلی گوگل بدون تغییر مانده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/danialtaherifar/807" target="_blank">📅 22:07 · 22 Mehr 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
