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
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 10:00:44</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 162 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 234 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 306 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 460 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 599 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 809 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3UNmTUujj8xK5RlrCveszINJdqZuxnZ6MLAVNJOWTQ1DVaagQNNArRRd7vISsaQSk070tGDOcO2fkRexuP-EqTSww9-O1HJdNG_otghEMSa57KOTjVStUO_2rG6ASZG7LhFYQlY4dijGbaugGjYvPXX0ghUuKxfcuj6H8mSJpglqiYM0QsGh2IW6iz0SAJcxmcxRjovg92L8SlkHi6FcQV9XWl9R-vB0Jk6eeK76oeC84SjQ7XplCx3he6o1Cnjte9tfTdW1RgHUwcpZyhfGHdoXyiZ93iwKVL6AOzOR9-I-6Fr7D7uU-JgdenZGLyUk_p1su_JrhNMno2a0Pd0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJe5l8doY0JqpGK4WiO-ymkRlfSC-teBGn9D0cvc9ak5QVVzbkQqAWL-Ucly8F2wqRU5YABGiAq7vieRx1TUZBYYKtJ5hykRAg5WvJ-5m2P6k6p8JeCdoqtN_F2zIDEzQG5JVL8zau3UtiJW3b3C_Y8PgCxIZz1pjN1_2rJakiH97uLQCHqOjDmAES9DiQOAhzjQ_L-R8ZSWuEuRvYLrKodgFLGN5JucQv72_B9CNjtdvABJ737xemjYzMENmaIAqvEcqSnZzUD2Prtde8oZ3G2uS-H8fmyR1A3QF8-4mLaD_XtFl837B1-T9OFQ76BsL63OR-eswJMEmnFIINa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf20aaDoq54qn-MVHtLFx5KEf4ZzqTTSAZpzVFo9pWFKGSGD-uobTxvXq5cJDGFdduzI-F-Bwes5GPhtKRHllnYUDbUvbLtSaUCLPtIWK8PNNOHsBOxjK7BRvKCrFblgKHNEbdTi5EsMPlQtawxEIJfaZBNeToqS0LmZ284K39mT0wCZHdm4C0icu7hMcb7UD_T8vO_j3GOaaYRaQdMcmiPqmB_MSnNCDOg22nmC3WInncmLPP8mhgbbxu03ghyGneb_zOFVxM1l3EmRyeA-ld97VIV7nbbkYEOEJ1xx9oudDc9KsiPSGrER3voh-pbv6EucIr-5XNW95v0OTTAb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeGU8awJCa5AMbxtk6U_4BsxopTkkZ1rnKEjn7lIhhT3T12jPPrGlnEM6mx63X4wm58fXzDaO13llQmAECw8-R5_bct2J4OJJCS5bYEBCKysKagGTC9-bHqfarCEBhxQctlJ0gS3nRx93LhSvSK-XM2dobTfgzfq0FgfSRGxMkpeXPSX6oqZIVNndhvPxxU05_yweFIV-pX8ESIIRh4QxMaP44FrNNXgzdbdMYfYveWbkAko1g5QtdKFJ3SLcPwR642g-BpfsO3zUSkVdJ_2OZzk4QWfbLQIrAftzJEUd5ZCHNb0ZQynPCyXAFGE0HI3M3HOYdh_DuhZg1E0Bm4WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4g7Zc-fs3udd3dyzTzmpRxrGe8Xa8h2lWi0RGHUsklit9e_mvTXYKRu6E_hgtFtEgOErcthMrYjL525F4jQYBu_Qu2sq9EfT74zA1eGwd4lONzscBxxNqslPt1hGu0RnH7BP5efrszQkxnhFZYfYBV6w1ey7dVrZrUfzlifJXlRz9qvpJQvI4xwwT0G1SIqQEM5WjMdV47HagV4jIxpOn0sXGyHo1AFoZNLqv6tUL8gTxrVtf5J7kCxoYle6NeVOdOwr0YAk5uQNQ6oepbK4mj9zTUXbFgkV_2kyWXYMfebD0NdzjiLYbz1ARKthMjW1vuEflcUIjcjuMw5PuOJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-8mf6RnsgMnCAB5FkQz9Jh_IXCFN9U-SLMfjot8XMYvIu0blXCWsC7_LBQGWAKVo7lWLpXFn4sYk7ZfPmG9v04V14SL3B77dNhh9f-HmVn-dxg-0mod4Y65hsbl0pDbcuWbjL2uQIhQ9E2Jusmf9R6PRYZv6yUCJG4RBFIbOwozfVs111UEHy3uGaGWASDbI5oVS2fcxJEL8Suwt_ckPPSVbWZIf97eDY4n8gwMAgxfaGu5JkzLHlE9GmKbEOVKMIrELXcZWhIpqYMMGCoEpcha4RzAU_qk2ta-l3bChmpeqh6wUwyi4LlnME-uxZU5zO_w_WWHbN_qJQG7ReS-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIhCyd0xleY19ibIve3HvJ5yUq0IwAb56RtF90-UA1oB_d0LSE3rodnGFimCi37ncG1BusihMV5BmTBc4UfgPefYkQBhEZH5qQKgzYUcFuOApqiyrIH9oAenn7AHvC5UQa5_8sl98RCNYrvLrD_iQsI0f3rWbtWEzeL-m3p5fzh8jW0pEEyw6KScAo19BQjUR2dDdIoTUeurhUdpmsFp2-eV9XqOWr1cwyZGvQzPqgqeqaSSSeofZnI5ffUFgBWMPsRsaS0tTlUaISGxnZyk55gYL9b0BFVykg8FHBt1r8zye-7w1XQERTRbhZsU_mH7Ps1sswPo8EpYtNPJuMikHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qih8V946eiaUnHsTuMZIL9PEiAoAtOZLTezKJ6YRF8irG_3G5zWYR26Qn_q6yF9iP2t0Vzp3lzdZaC7Or3Swjujwy4a43gC71zoycgdjMW_-FLgaqXyiOatZ4PI2JBQAvoKD1EXqhdf594j_X4DKGE8s8-hh7m8E3vS0E5-yqEnM_v-1E-uKrFHNrGGxt4yQJLIrMY892Fs3ilwVG02qCl9mPFCaPpGv3wJWAwUquyTGZYB2cxjOmeNxqu6vSc49NU5dnl6ENs8pDlNx1NZ3opbqTjyjjqxNPnad9V1FJEm5Clwz9mud2fdZCC-9_SzRkvMRNHCDzRmVmPNjxgzYMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMzrinOh_kdv7NY28v8-ts0yNeGvMIyq0ccJH7rF0uKBYxyIadvKpYscO-aJihVlyT_cZg9Dg5Y6DUUft-mk4TiPg35wb3lASDKhkGMYdDmpMJr1AVZiWm-oB_p37ZjOEDpegvsodVOedQJxGv3NfVo7MsLTQBxA9TmK-U2pW0qBjik0CkvrqFJNr-SWbNR3TiCdy-s8u-mhShFE2mKj-1bRDNb4wvVmVVvUYHrhqJ6O2P-L7jzj_q9XUuFddQrLskqkvmdDD9lDWcSJ0yzRNdiQ6rRBMpC1Dye_8zYtMPDm2QerG7wsG1bM28aU8FXrPsVbTC7u11OTGgJ7kbQ3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba_PsliGhOTPaIcwHDnbYPut7mzRogyyF0_DaruzTMskwTXWakwYEmtGLVMCDb9Kog1aG8uoeMfRiCNyFtXvIu9kh4OE96Zzssn7i5ax3v2h6A6p47azHgOpg-IXxGC_Pdy6MI1nEjc5SIGMEB6oTvkiTOXz8zoqsLSzOofyfVn59LAFqxAdWzuhCFwaQnx7uf7MhFPSpJMjV_52nWSbYkf6owZzMEShu6H6quew7PqDZsPdYcn0TBJeAraboo0XxPiYTfoQIQuCB5i0sraIKZ41o6rXfqqwz5LNgOh1W0cLe0lL8u__K3TKuMIGVLwaQ3nfk5tB2XcyAznXyNJiJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwbC2VqpQL2Zi2kKUmLKKg80LCG9PdteMYfmxpZR67153_wtW8dqgsxOr7vLlCDwGSEcz8YODmvr3jA1-R2JSre-STzxTa3OdQhY5LFrsucWbeZGhZBIwNHwe-G-8C_hIo-5dUyCetzhtq0zbqDNJ4_xW8NmtEQhg9DyycxT80HqRuvzqk0KEEvfIr2lpukYNDV8OCycNgJ3Ajwpc4AdiGgotYi0wmoTvm7LOrfgwaesG1kRBg6MaXgBQBQn8Y_ZYZB6SbQeHShtjU7IEQMDkJZo0bXsx3RyWngsxv2FED-k5dXgD-5WUQJ69JrKWiWFP3AFnNLs-KmTCQ5jPftr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 844 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO4JKbmdgmEn7lMWOSwy3IjIk0lmdm0LFfc7UZuOScLhQN3gwARcUWBQfClFf7rX6NMusWQZoSVsz1pqWgoFdB7ThONaoZuJ9Fky31gf9GXzh3UzduYQs3r8tw8r5e9tToWG_PrkzaJoGDWE-h3NW9sWMqW2gwBhJ-7Oml1GFGBgo9FJ-ZTfT9frdaGeVtCxq03gI3UjyAJ3DTBIawJ3Uoo9wxlQjNNuTKZ7mHINo6AvI2R4cO00x-5uC2S637uk3n4SprdDNDi_VnS3LhsfB-oztblCyNGqsKxFYwAIwdxxPhvHsMvMKckUNJApOJfhk6DCnDkqemOLEn_wutilAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUbAPpXlXWkPdhRiarI-_YQOXoFVa4T4BR4kghJ6kxpYrxZRpJNC28bqHLRmPuVmDI5k7gJkc98ZnnlMgTDNjf8Yy_gPS8sNJau5KxW5vw1uBF13QKNHS11K9gGh1tvgSc-v46nV3ebKbUhWuiqgY-VTBFbjVjaPCJ4171qeja5GbMzM6EXaaaMdH59CwvIWVTBDrldja9Va4_FTQGhuhLpqWXVznyZNltUwpBieqKKZt6E0qIqEBEmT3SWWeBrOwpEcn84HjRnnXoUGsW9wzeuPvuO2OWgIFbEg2B-n2u-CO_Gd7YNoryI7Dyn42ur5ZdtCrwOcBdxWhExGwAs2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agjyE6XTQrlKLb2E02relD9eb07TW7o4RVBzTlIwH_ZEU7gerkX_2X31DFuUaVizpPiDk8owbwOLJVMUL7u3sYWyBujR98lX7BLo-N9z7pqfepEFMxl2QbY9H1VVWLUMXw4vwaTLtON2zwOCiwu_UtHIV_Y2N8atSiszMe3FOGfE_kGLyhVZfFA5o_bL3_OOfU8W1GedtUqaslv5DYJWpO6YDZh5jgJr5KV05U1BJRMWo6azHSX7M2lCsYTGRCwS17E-pPFOpRHPI_OkEKVArwWaAOw6chulDx15bPbEF17kBhOZ-jYg5DQPRhzZS7Jf9JAIFzEJNppqw1Gb3nvQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLCHkC7YtTUALHDc8Uea_zspbEe_UWJI9XPNKJDiWrAhjaOYnm_-3UpSWcicmuWGE6nqLCIzxXKB0M5YarVVWK9rPa3CSehKpu7Vmz_rE3nrjzlLPn5OFIpCnjkQ4WIj3xvliA0ycKZwRhnZPnVk0rhnwNEFegyuVIHCGK5i7r7zgT1NQms7AJ5y-H4XuMapU89Uh3Zl8kd0d8x4U7wCyfC3CSHp2-uUNgN9PcpmbK0IrCmN0SeVgri7t_8cQ-eqo0REYwc2IkPscEjBrV1B2H5DJPKc-f-tefNxRiA084VwanO-c2489ZI9NsKmCJr4ap-4QwvlhKD0GsJduKmg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsGyLgvq3Bfiy_QGJP2X91N83NSXAwSbmyWIuk82FB0blof1h9RyLUsQaLtVkWzANUX0K6dn7YTEZ_ziLWE_qs1uKMLvG7EiOvGLqq23bBCde02Ijx_mJE2FiWRKAqrqgz8Kssu3YLUqPDwB6NA6Z5L2c5FWkpf0HJSfvTGGFM2lMci51c6oFdJ8ZSy9luW3W0evaO_Cia0VYuHCD7hGaaLdD9odzoFYsTAg_vWASEJGzNxKdwACFadyWq8luT8dHvQ2mn6GovBAMtJcyFLhCtHF5NiTnC09NsIcrhQDoEexHlThfVemPy2OtPuZVuE8EVjU9XtwdLyRZOiVrLottA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXbNplGqzVu6YAcEj7nZmirkvUEe5tM9nuf3xcuYGqaeOloacwIXT-NNz4_y9gKxUrFs-0TpD6fehg3UjioE2EfJZn20QqTTfkmVRW_vqQTC7myRlb7EUEm4jNclj4q2Vs9VuBy8ReWbwGJgCa1W50oYKCAyCPLiuLHTTAlOrLLapgBuLwvJeuq86_-nOQ4gnhz_wDO1QsH_GohJdjocvZGwxnjz6sFD-Xk51ds3QNIn9D0cOUKmdU8wqIA_0PI66td1McLkSp9Qwz1NOOtIriKavk447wb278zXxKZW48Dizbs6zFPhiSVuqgmld6y20hpCBKzn1wsiD7SaUsP1Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=Tclw-nYG6YMP3S-7P5Rm19ycnyL26TBRtwDPOYl3sJVX-TIYqufAom5z-VP1f1ZlEoeigG8THYjls_3yAp6I69j0ZzfPVtkCulWCCAaOEl9N7EXS8v6PM-8P_IwFv4VJWImznr1SkEYcU7JTucYQ7pZ4bsvi1Q0_zVw1srP9b_S2vMWmoJYVjRV-p-5CnF-HNTPnjKto8Z4F1bB7rCtnZury5ieag6-KczKHO6xwD8DSO6mL2mkRb394qUeaUsf9mvOUai2Sh0NwAL2Anf3PercHVzGmNE1Hp4DyLJ_AzhTIg067rRKg2gqbNve_Q-ehM-NoRBlzFW0VKhjaREDJUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=Tclw-nYG6YMP3S-7P5Rm19ycnyL26TBRtwDPOYl3sJVX-TIYqufAom5z-VP1f1ZlEoeigG8THYjls_3yAp6I69j0ZzfPVtkCulWCCAaOEl9N7EXS8v6PM-8P_IwFv4VJWImznr1SkEYcU7JTucYQ7pZ4bsvi1Q0_zVw1srP9b_S2vMWmoJYVjRV-p-5CnF-HNTPnjKto8Z4F1bB7rCtnZury5ieag6-KczKHO6xwD8DSO6mL2mkRb394qUeaUsf9mvOUai2Sh0NwAL2Anf3PercHVzGmNE1Hp4DyLJ_AzhTIg067rRKg2gqbNve_Q-ehM-NoRBlzFW0VKhjaREDJUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRObD2Nmf4Xd3GzaHsaibDAUx7DLFRhJYoXPfrExNncozhMk0KZfm6vhm3wnmHvMD8AxH4mIXdjq5pNVVm_kQ6i2ypO1m8kvVwUAssoiqsDgrz6DIRfQsY3LqWokvyY4WJYTCnfnoEWps_SRvNyz2Fr0XhT3QNcl-ZSDyHOFQknJRCNsQo1LKrP__bQSrjFnBypuyfwqZbWc2lEU9q2rC3Qq0u-hql2DVWwpRNl9cjM19i8RIX8-FafxE7EPgDwZYYlXSqP2Jhlo5vusPpvBqvUBFrPAPKW6LIwOK9AErpWLT0pPBhPjoMbszfw43ylA73XATKvb62qd1mXfKleEMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLBnvwZWXvTAvGfeDEdsX8yaNZsIYDukidUUPDfrMXFRwPHzMF1txF3Zg9WKly6XcwSZjMfiBXxPcrZj7p3DDZcgr6ua_gD5tHAGjJyvtA7ix0vgXv503BkCcheTKKRC8Fyz8WRQYT6X6tKG3crnHRUnxOujSIVAw9Gcx3OepJSawgXD8qr27n4Rd90EYM1Hb32ycovZZq4CVrmLfWzQ8wl3U0GFbz_oYPIsspUby0pkYZzxcTddS1JsuYsKFsXRW6OrlztjkXSqHLjKWiKs-ddFdJsRZd_55-SN3P62HDNi4ZPoD1tTHkshr3Qijure2M9Lj_8SwwdTt5hNoSmEkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRfldpt4Fv4bdusMdnJFJL1VpAlSxljArOjeQVRTrrwDoxBeb5b83aAXQryaly-b8y7YiSxXk4PAUMkvftIE2J6w0QgEIwJeYKNEdwGw86F1M6yDNS8SCjL75Y9sw9hSBWhUXXQ2SBZ_WvSduz_5xfqhdNEpYjgS431zIPWffhXgMFkIpCLGgjvh6ACcgKtloAuEjaQnLnbMYcdsewqfB6gdE9NWG6Mv8_UuSvu-gUtUPHuxWxQhu2u8WWVLOA2FLSsN0OWKKOqeZZYihZ5FeB9tgizpk3k1VUBUkTUa2U2nBI-4MVNdlFd5Ht4vNAPbdCH4m71Yy-5cxE1gD6dxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpnlFDxrovyNiY7yKCnMUqjHlGldDk7IVAVpCBmMB3H9K3elKydYZ4CPmoVH8-A1Yd071DrZLrEXjNiLjC80PjQs5LxuIlJoeJUAgUPYIkenfU8cBjVHI0_-QmxWhe2gxJLZN0fwQL8_Blkp-KSA0_bwjd1NeXuR0Zj_RkiiI0D0WOfXp4ALlIke1HirgmmntwjZALi8cmWghlQ6gMcNnKbQ1FtuYXsZOq0qV1vgBTamEyItQIThbQs1vTgJpeoTaTsAAdxp_8jSN-oR2GCrLP4T68jOajYgwLQ4kNwAvnwnfdd2gINxHgBxDcF-0rewQ0Z2iRSATSjuvH-dUJipNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sToiDG-Ft6L2MZeTrQ2eDi99E93r3EbCzz3XSpEjFsCxbvjGH7Yc79x1_om6-gt6unkvNWBccex277SmOY31SBO8SonW6NZmfpixc2pJGTJr23pe8IGUyHH6fbnaJdF3YeTDQR-xsQIqTgWo_h3ulZf7QjZX60eLKvv2ZMkD6ohKxX9ETrp-A22VRLs4tAFQ--gRD0JSY37JcaoXxE6wl7pRIfoa5TeK1hlRk3onp5A35MyXBSPKf1UwKBFfxdm7jf9byJrTnKsBT8X9OD9ZTkcV-cKHWWJ5G9xiK8_mpZ9AJbYTKM_QW6tL3LYgmbkj_E1BjGdXmh3Poo658iKyTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McO2iI3gy-gtH4S4H7eJkD7ZeoKmwi9ntYt-WHznhKTYeTs3nex_RxOC_7gMgx5HUrUDAuU4dCypX1NJiDQgabe9SYuGbF2yvrJxVlhyAoHPMS1gQmTkZvx7wTApRPQWJWsgfXwZ9hu0wdCBbqj0i-zLClELtHmOWAI1MFbfolEGeto-_KY3xtrt6vZpU0wXA_RFlmrAjSIcPuqtUB629828Sdff-daHIEMHeB2UgfT1DzOBkC112kl4khKHLvKk5btSt5P_SXU67-DjdJNN1ngPZ43h3eIEQmmABxGhRNMy9DP_XMlPnnxppLCzuAKCPbdOf2qzJ011GSzWWT9BSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIG5Gs1EDktUAdCzFPBRRgJS2eQiOQ4QsZ5Wt3z9ubAjpSjpA0OgHVaoPsblDGJKK3QUpDS-PTlzOgiB0UQw7cuHjrCqG09nO4qe-V7SoFR-zRVYy0qZDVyOlmzQVDkxfKHCkpY5CHPfgOjWVUxS_wABGA5ig0YhbBBg_345LPt5x1Mb-6B9GYeDVaqjkY7BbH2LCNAR6ErEy5PDCaJq4Ywe86H9xjPLyOjQ2TS_ALaA88WBpEeJFNSs0U2xP8nh5lh9ZolwWq2L_nG-S3yrcI2Zw1_BWKYJcJejse7KCIuHxMc9LXYzHnmvJXznQc_3bjfjyOoHa-hZ_I90SB1cXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTE_TpSBofh7XWN_-MJZWwnFpQeHMFb5l3v4w5_8GagleCAkuEnP0g5kdah6nmylg3M-54aMTYmFT-olcR-e4tH3IEiiivQaHSEKrKmNPBTREpru21ZL3_m1sv6obgpRW5uCygxd9-XYyan0lnId0BRmgOcEf_vSOQUf6l0DrVGjnS_Q8B-LP9vQ225H23otmcjQ7OHl2wqbAd5st15zB46C1OEJnJC49IFTFWpY9Fzch2lY6cPSZXuuOOEFaxqd6AssT_qLVC5t0ddsfI71aup_dDqn8KPHTD7nTWseew7DT4xgZd_PA9VF-GLkym8BGhjFLHeCr8FuM9mDe22XYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfPEOFdRMO5ZAz886WDth7WHDdZybrycsC7w_t2hty9ylhBD6Th00nNY60yCQVaThDnw4-tWdMZxpm66CHO-ZUX-ys4ryu3i_tnzeb0IzzyS5FP0CjHmEkBYmORW9nxZspnVzXekL568zbH5_8CW1lzIWom1oZF7oaTplloDvqHU1WSab0cblXvTlB2cf0sJPaTrpNszjaayTJkiQBcOCsoyyFL8_TNN13IO4Hx0uhUrq1owLHDJPqoyYp0O9INFru4rvW_Q39RZvWF8HK0lMkmfdo1AOTSA2yEDoPqBFipF2tpTWn-OG3VTFwBNnQskxSp6tFw7Rcuk4vLexdPWeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 809 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIC1noZQtSilCIw2oFGwMh_EyZIYzY2QMZdqhPXP4iYmfGND-gWrpmNgCB5YnA-ttXuBpXRrBDohte84m7E72jx3KnfTAy8GppJ7ZHD1Q8GWPfBNAeXnvd73dZWvg-EJ6v-HROi5nXVunFeVGgm5sAmW85XDqBEwJxBsj-x3Wey6QZSLxJkvdcZudYa1eFJAMy9mgkeJkVfsQx2jgSmL31vJ0VqSkyuYTkrLMoNBM2r0-UMna4KXZkh6YL1WrXmNUbLLdvSkNktS468GcYzaMcpYO2Qh84IhvYT-qCSRWw9xudubrD69iYgFAJgvk_Ddn3tcdSpMYEQ4d5S9efCBpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNwg3DlXeR_TmxHXe6cTIMMSuy9dE-jTY9Ztg41GIyhfGSmDz1daDdBN9-BgnNmGAjhNDXfwnZIXQYGuJjPC5keGCNsYCuXVB2t6LmMMTFfoT7bF6b6jfn0D23ddGNovqz_mIYHZNuTS2sgAWrOd-24CQ3tnjFMFzf41-IDrcd7cQsNdWUcAiGGB-Z0uOcQMzgyeuu7P9nP1u1hKQ-V4k9CzIZrRPtOpMk1I01HkBDR406PrLcG1GqOt1VtI0rRk87f336e-Ef0MBf1V4y7UY_4kl3aF2DITURmQWagDoj6oAp5aYD0u0Ti_7bIObIsMxcbFRR5YFXWqyCzh2EsHFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXoPxoAgacLNbojxwQqlNYiv1Q3obE0oqUvMQK5OChE7zVxON9C22ZFR4kHHW37H3MeOId9ylXICkw51xjek4dhwzlzSEjmd8bUw4rsbc43SAZ8JTkx8SITUONdkvfgr3YT0eKiZibFhWHQhjGR17vCOn81KLE2ZYsadNsf2iHTePHfS2b57REJIyQarYqNrsSvBQHAmqlucOwpbeSvSy-3htZ9r7j5soVWzr8EqF1U5nPQbZjnaad4g7cY2FSfrDcT17DoP0DtIkLVW0vz9B8FvwLWDXS7kmPrmHTT-CaicYecUqCy4WRqkUcNaVVg25QWP1im79xKuNNG0L6waug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deTvcTpg3rrdyrch-nuom5QnZa35gNR764BQ2IpU07l-PBp3MkmRco2WSo7oAvHdpssKuGLcT-8I-sNV1jzl7TU0z32wxg5xLB9rs7NLQBtthtL4pUaLYneN1DW7R0SBX1TTjZR_TcDI7rcYZzZ4hMC3AuOUBdZ8xtD7nSIajbi8T99WfokRyOxWt_qmXk5ZLjMH2bn1-O9VQ7n1bThNnvMCGnlyMnOa9acWyvkr5kS6o1IWbARSEbVIixjQx1KaZH4_q8WWDwoFhHyzUrzEEehgFxfNsvVGerA_bhUX0FCLFFF21nEbpKrX0sqq6b_I2E3oHDscDL6YWblbftoAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofo32-wIvv0_Mnu88c4TDsaXUGGU_qPEvsZUb9GXkMJ1CAl1mhGOQIryzb_W-_SBghrsjOL9siviivSr_rKBCqIQBTrj3BbQiZaYmAGniFA_7Qy2lyGUlGJE3dIFY-7ZI7lH44EMAmMNjCot6Z4c7K6dHaBiAvxrIzMCDjDgshGQdpOuxICxoNvkw5IpgoKv4VJR32b5Y2Dg-YgMbyVCZ7qFpAec7_JIpGqa9o6laaEfoHRYZWueLae1QG3CEID1KJoC7EhP6U2YuHCdievp_uzgF-Gl4abk6mPaA35Mv08pFAc0i6fI7FIPTSGii08pYisxaoGsbDYmEVWE61SeCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOXDz8PapJ6QGsfMwT1ZVmR7GZg3wKwFU2t48RKP013bwyBX6aHcwmMOEg7Q0MZdj0Geiw9kmh5aUmbuvG4ZYTodVAoc-4hv85C1mU8k7zYEeRjJZ-XuFX6GMeAPEJdAn7KzHlL0d3MT2EpingT6h5r_v-Mirp1m7fYIlqflGjoGDWHUCFN9Z3bPbB-syrcKIJNbK_xMHgOwLTEThTRFASvXTMKVo4NyXFOPZ8IO32GLUIj51LkuwFkpwnFdQOvrkI0j7C1nnoTSW-snWnhEoMoFsRt4iKIIf6qWB2OoRs2WtGcjHLU19-K_f1vQ2v5jen5xqkpV6jZnuudHp1gMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z85xwYgm3Ex_lvO6MaN_6fZp2ZJF_0xBTJpX8O7F-ErZI_Wa5ZENCGPzIpaZAZYa_oOxq2QbC4pOZhWARajQyJ-_mGvKvAO6xLkjchiEVvbv6_TLQ_WgIGIbuw-s7EJcmljfHLCluJ4AUjd3-Lc2Qz1mowT04WivlYbyOdG0p8zwdA2KKrDKV9KUutYNE8jGnGVw9Ag7NlNaeE1IhuuOqK3rzSpvumY4ZhcD5fPm5K9JbMAj5ElnDkw6owS-UKzR_ab-IgHF8qai91qduX-Cp2mnKl8u1lZwAs31KtfLMTPuHO8pHQUhS2su7nGlep1Epes1TiFsHEUJfCEHsl9Tzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSyn50p381ra8vEao6M66DzrtpU54mvFbcbUJrEPJiBj8RGFun7m1igxue9bu_qrvZwyTk8qHmYgEevXwTSaPsV4Rp8FMODBCn1CyVha6_CkqWe4mW6uOaGLhfyf5WzwNuOnIOvC6UXmuIbaM38fxe24p_J0FNkbkXGfUNNV858RYuEEGZl3k4niY9JIxkAgs8CWoHblP4XMfSkd2mQTuW2-ebNWHN2yeb2OHum3SwFIbN0qLBSPdDMRG1uBH9Rxy73kyZLr9jGRM1ML4UT13TZoWpnQihdZvgRJtiC6ypdBJE4e0Jh0mxPFwhfEs0BxWeQ4z1dKPcoL17rRM5Mc0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atvGcCgMJ31d8GYG-gnpi5v9abUX5AGFtUjaz2ENv-BhmbTOIIOdipLADPzZDGe4nM3g9jixT1K6lTAXtsJkPaSkvOpuWx9-DIcFiITiAcSgqaRCZmQO5CpdnOhdXjwF4oLGs9v_hJz01eF2hLmyGbDGI3VnY3O4pL9amZ47-MJ-B8RdM_FJgeLbfGsYD2p2SCwh4Xcc12WVFsnPnVOhJs8P_MbZLp7X-mB6eVSm4hcT_-ZdlffsGLFiquQcoYMQLxV_WcnrMY62S7JbA55tklF42WUFJ5tL4BjeyV4GE9OnXR3yAfFLpY8JOXbi1VurX9LaZ1fkoBNnQoVqgp3V1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUvAaMgDSPgeRO7q_wlPxPJBu6dYKS35etVdmL1qZhpDIDtq2NDo38_fIT5iMAwbuwAjM3HYee_DFpIt2kMBR9QWe0ZkHKOcik5tn5lL5IIasLNIuKWCHUR_voNlSR7oklJf8YHtFQPObHnyvEealgdQc1WI8RUrDgjWxFWfvJ5QJtVt2JGKRocrvC_5xJ4zqHyWtGhPSPpFaZr1cY9Ecn5O9tSSCs_rzBWGTa2JuF14nY-Yi5vRQetkU5KUeyIjJnGeSe2ejMMH6aYKsdsnjT7GYJAtOTvwJqI7iOghnWHs8T3lQvDy6LqZh8x2ZS5n32OcMWMyRnB3DLU4yTXnIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwMD2flD3W0kE5hoJo2dSIXo-Irjbg82l6jA8QjAweDOUkMOCI-1-NfSwWRuRmHXq_YQavUGjqYwkirXuxQVmZiMwZN4FNHxD1kxK4htptWyyC1TIxXFJhQgWzlbGLGwsUdSUS9DWCp-rGnfhIilmNB_yWd9EJj5OUFjdJJLn7-xyga2eDN6iYe3PBy-MjhEX4ZVgdGYIOQPIA1YfWd6WC0NilcrmoxMlGOFLUpl2gWC105ezm3bttU407S7eizPPE3KBj84c75VLa-oByLFKSyHq1dC87oZKOeuzdhkbV8V6MDpYM2cHRWUHr43ByTo7vD7q8dEk-aYElCER-tmBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT6p-QT4vx4-ovAK6B4eO2tghQxryuAVs8TUiVsRJ4kr1LhXSa1gb8Yf23uMyOVF0-_RSiIQHwIJMTuhIf0hCJew7WZX6ck_LV2fsWnMXKmYzv54IpskC59_3LS8ZmdSgXGxsGapki4KQuQCF5u4QNWF8MVAsfiW6gP32WwzF2H2LipwCYc2VbJYeZH-jptpPObFZHBgHjiQYQG7tz0PCwUdOH_jJ5clTkpxM3XI0bPilzHESm1PrVCTs65vJjGQpMHcfmakzoYrk--dr8euZlDSbKepk9sKp63U0YqFnkIeyHSuvlCuALfsPvuB3YsO3QvdLg_AAdx0S-MUiAmFcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF1hxzp50P4pSMsthlb2VIGkKuWouPFUmAhnNfMmMmdTzAVWINvBiZCIRP4LLxrSrHnRx7CuYrcD3WYS6aR-ZnT-CYFWBgYy-dvctD3ZN3aCj0grmyBIk4t-ThHtGgz0lnPrHr_rgCAem3uxRTUjOge2z-lX9qEPp6l0PWbw9V23xJnt7Yq_ikB7xsSyodpmlJ2LFzZAh3X5lhQjT5TEZASCvMMPXWoHoeZgyRLqfX9ks3y48bCsovCLC5drszW2emp_8fMc17eS3LrkrcakvPZcJ3AM_IEMIVUEUVBMZK4owLgvMmyOKkg8UGE8yqMIrQsu8dZ4DWIpBlVGw92gGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4CPNdKChAbk1pUkIjzQt5EWjNdkcMK8mUqjyogMEiO6dA8mByt5sz_O3b2LbzeIQUgSNKEaWPSuGucl2jOcUqckGFwL4C7PIDmEAwOUQ8a0IgFyBwL_COIKr9sHKnNXQw0nt9mcfN33xEjK1JdOcLbgY5lutIrm9XJpjgK-HVLm6BegwgHZaNVyd0hauZlFK4LK4iVB0RlNA2h83o18THoos0aBLUYSvNoi3pBF7f-78I6Vvm_O582DTUeNWNzEuVA0N29VMNt_RdFL3IoYgBTxJjZrtFynL41zP75QIj-NWG26ymja5aasiGjgTkgy1bfcB39FNvg83Gi9W9x_tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKv5GzGuvrg5b1lI3HroVpr4n0rxmLLl-sNpt7sUIXRwIEBA4y5ruAhFsbvZXyZ3VKVUbpZsM3s6giPhIn202MWxlatv8Z1OuY4VoCxOJ7AmCPUEetUW17gF-7gMPMMCYsZXCDeN19ijWFphM2ZByscoNI6bUVD3n_gFJt7XniSvEMS3eLCvzme7pb7Uw2yr9HXOCG4IeqaQ2H128jQAvjTyxLJI1k6ecqk4nzD4-IwfBjhjFc9FI9S1Gw241_iTsO4BDNTyPkF_2LNP9kTeA4suLSPzpLP9H2SJKquxwrRQP4Z8RQdDcP6zr1q-ERT5P-yV5CPts6yE2HsOHs9LVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-ag_yDv8MIJG0-UTeChg7_UQiMLpZn7_FBNRzdCofzswo14uCYmjUB1MZDkDcQ8Y39VLBmz7ccy7k1TqDJeUAFzl69mf-JV44akmNIRsn4-jfhmMErcDig2kOuZqxe7wRU8JLRScz3s7T6BrrnxMr3Xj8LPbBAZ6t9RbgPLhGmaJAg1XsMQf0CBwcUBb181b5JWIXZLKf-k_suZ1zZG4FupZ8DO0lj_mKHt_uJldTIKD_W9pW6yEPOTFfbEUdZkpP8LKK_BpTu9cvt5J3f3yx71tqwC655o08LDR2vske2zya78TWJ5X600SA9DzB6uIOcsSBUWP0R6ro2_cQKBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGcFipp3H6Xw4Td0xcJnKhI8T0bnuhjuGUext9J4BMnaQc8hgK4ScLO6t7JIOQwUt6S_XS1Ao8odo2vq3AhGw99dVX5vjKRZ08M7YeWjWrBMUXYOnkjjpxHnx_IWdvIBValPtGL6a5F_nz8xZxzKAtz_gWKcmGaCRe0o0WeX26zIY1Vy04NK15bp6Xylvag7MLxx_EPkgKg5JQslF9e-2308fdzDZ8Zjep1pheGvOHWhU3fPx7s1p-eyELWErBBWj8fm0crRO42u5-ILP42Y2Yf-Pw2uOmdHftX9nGmjIOE9dqv3miuX88KiZFIRp-Y_mLvaHy7GHZvxJ2T6aLLRcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQO92s5FZaWGNH12cdw-6rXpp1Qz9wR2p-jdo7fvREEWpU1D46pHGFSB4s3AG8dbB-LbIaIkxEWZsU0auJvyWwfcSoj1juAj1pM0Yh0Bz3UsKB-rvVyLW0dsA6p9FYB1cIWQdUY66UBIbguuYhRVi3WrxTctA95O017X-dx1iOlyvW4_oT3T6euJ32IiHFBkf7cCOd0DW8Npl28YQKZPyPSYcpZatlDOL4UCMVIj5nYTH7YIxw1xN1gLeMel0Vy5xbpNGKk2rO0kal0_l1wp3OXSD-0mxaEs0XpF-ZxXh4ugbVFIABsHXUwJtyR8Lf6uShCVZGVaGlEgQr_Wn6kh2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewjsewgu50novbXLaEIH5du6vHkuhxhhx-9zehfLb5Ocl3saoepeyJAA9n2v5Gjz7thCzGGzP7TH-RxmLTNElGHqfGbwXmxg9lrzGKY2l24bgnwKJPkjsijj9zJHpWBs8QF0t1hlBxTjIKn5msiiNRfNTGVsn93ywT41g_a2cGk79F0jFtupsc46GWSy6YWaaULcVeBay2eXeqXEj4Q8ozkmXpac9_ToSBrWhe2nlAllkTxHtoD4RdzrsVNushkzLy3l_xlaTqJ6pSZffKJnuzzYrz4_zRi0jDtEYnkBHF1DmgA8XqzXgPnGCRU9xK-0o6BhNIr9HkCMayj6BeiO7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsMW4AREdO2T_j3_cAumD5QTBbf0_BFDyqiHquXOT_Leig9fVK600_mq9M6a458k5RX4NnrlPCNUpb2YZ7LRU4gxO9KeCkHEWJCNUZ4hwOllEB-gr9ZGxKCfjjfyEc8WXoiFKFtKy_QfZliARBMHk2UKbrTPbfv4bKINguWRBE35rAfc3yVBW52c7-dSIQTlIook-mHTcxodY4u2yT8fCaI_lPdR4j3Pcz-f0L6ZJcY_O2xIAoCweP9fH6sLgqY3nGuZYgVzzpOoKcvNCKWqhOAQ7iAwbL1p4DKGm5rQ4u1Fj1b7864Irlz6h60ysMWsFHESUc5Py1ph1h7rNm81TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGfHAf6txTJBJngo8KLDeAfIXUZkxL8IxxYxvpIZMladXoHy7zYPu3aCkXFr2zaoedBvCRyzLLfl-Bf8RZb1I_FgkuH3_lzHDPgopHEVxV_18C0ysnjkrPknKPIcsygHYzO-pdjUDbZRvg3hHPS64tg05_GsdNvbxXt8IsxL000OHgOCbGGqGNlIHLgN0G9gXYQbejHcH_EXJLwAaua7tKR5r25t6eK2WS1mkpNBtLIHZmixLNAY3xFQFgURSRYxzKtr52VYUtW9VTdr7PaV_vufkmoiyNpvl4nNax0a_cUZOp-Grwk_H6t8Wu0IkRj5-wTguWd2jPFx_gKDp49aLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAuRsCFSU5cBsA_aG50ASADhiMGg6HIp4RLdgQ-tz3k5TBUlyQNDZwUUjahrzUvUUiV3XNRm4ovDERCFxp7lmDdAOi-nLI2n2GtnknDQhkjlL-5FChvPgUQVYouTaZmVpGCvQRdrTh451oMKiIWTC7p1tYHOGtmX_mdKkdmA3xbHhqKFQbIyiByBgbKEmQ6Eehx7pemy_5Mg96gSxdSLwFiMRNtrLLtAkpMXVyibCaf0XpqobTVTdFSy3gfO7WTGDxyB5bFfFUr_qbR7RNNEcdr_Bkmd2D-oPWpKfAA3ShQEviArN2WpqrD_nnR2v0mGiem6_bma3sdVm6T_tGDaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNTnYtMW9tOP4-mGbuNx80NJ58rF33cnm0IEUv_weB0Yp20ltHuwkpkiGtp88EbYN-MeZrofPyc63qrzXWLHQstg5fkwQcetU35xU05H0ef-Za3e-_AA2CF6nQr1eklINNEJkB4nT5u_94TXfWFyoBbLr8kMBTPci21favkTmrCZF5jS1vYSmBtAhmfTfibfuYf56Aqm7D9IZ-_gLghVwcisoW2Ta0mrsv-pRN5k6QCGZu_TYOix2Ne9quCgkriXvYmN_PL8NhkAE4RAzauQHi-15c0fiIAVD-qgdLq4HIS18pE72ApQDSKZv3guzgOyp6RZP7XwMA7WlOp014daYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHFf01K_TVyQXvEbiZn7g_jZegZ7FHG3hxReT9QEpqtpRjpUAytSt2dSxZXI6Wc-ZJTN5uGCaJ4TUTGwya56Hk4hGzcOLeh3V4VbDsK2J1bP5lVNROUM7BdbKNgzvL3SFXcJ9RHceRAN-o3_WLSFfsNK6cOUI_BVWogUJWxFxJ9qcrHodR5xu7Z6gXdADQicd4bTBdRm5CH-hlZTDXqsDvRcR3ryTKb7w2zJZ-kuEzmvkBdTk32Ur7dCLG0Lkvo4O44HlSNu9rjbquCkCFf11EL-K88s4XvVA-a1hxNQbGwa1dEuXRZdTsqBv9fPJhjEz3lOzGLcnJTBcAz0w60dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4NLoFQXAlm0PHYaPVfARYTmmd6XWGtQ6kCFmxiRD1wky_Ru-1LDNWB_A6G8sjF9TPxA-ih__iLpjQGTfGt4GQ38sDigvSZarTMSMpDmnGjHA3aZcmUv4PVtpoRSdaLvA355HTokKmAn__oDHcM82TYO2wwhmDrTaYSZaLg6Ca7Z6GMLeHpuvCDEKmVT2iBUy6FYBLRess_G_C3-FVrB6CGbMJnXazca0FvcoN0Ey5v_YKGHtCjDjX7_pvA8jzps5htOg9mQzy1oIH1OWIHv-s5kpibTb_AwV1bYRxShXSosf5fAqdvdAMiporJQdVZ3CzXWE-NpLMsUIFcXERsYig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTVUTDFjsQf-YUJPboacOm7aPl9Cz__4ksy-3EyxUuBXYvFcl3icPfogDYqQ5YzAgjaQFtNUpG9AVMFG27hwa3ygoH_T5jpZp7UkSzNZgwHiAF5KWXDKxw2FY3CQuVFS4YyuuVSsgQuIUtfjQKpUdXTjEe-QFXsK7nawSPyWN60vlh6aeBhE9xmb80jrXkm-oGnPl2WJkwqfBUQccq9KtDxiLz-2-V-Mqoz3tiKKb3UeKI11GnveqL8GtSblbMC-kZvrIBVbd8U0nw3WUL_NYZ5qqgwltj5fWOODC6slsp7RTchBchSpvKFWxcBM10tjjQq_FxbJncBQpONi4VX2zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1Y5grcgNs02J8LwA9aZeQJrreO5-fghkcyyYQ0-siTMBshIh6_fU3GAKsSWwpoMgsGXCZzVHTkgG8XIAPdVAUCgFUmr46-1YNx6tsnahD2IMiURvVPwxRGkQmxvJjVZMkY5hWIMiYsajsr8EJ6UK79ElcaKSc8yyQji4EXbHkWNjtYKh87Ae1gRD5wvc3snOaZUgJvMsi4lIToTCIuEADRoS8yPJUviNSItM1bp7q9nCrzs6P6UZrK9kt7kWopT75HbNW3W9Yp9I1hxxItWAPIEpAbRZ_VLebLSD8cTCwtHMPPPmAnGbh3NkqT76xVXDKaeqPwk7Z5ujd_s5s4Qmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aURJ7FfhDfLZsq5a7bpyUSd1mmcp1HMnRvybQzNjvM1ZCZfxmckBbLvWRs9e2SNwYAxBX7Guo7R3zk5GZdSEw1soVidmBVfJZRt4oxyAnR_uAqr709ONI3iE00q1VEZoxHuzLHkbCikJRPPooWSZRhStpuiF1TSfLy2hj1PxbgrSrH0ngryTXrmQid3lBU_deydC_mgAYWri7r_6A5098mdNGVP9T3CnURCutNnEy5zhaXBuw7JhuvHo4IS7HJ6RRl9F1wQrlogoT0llCScd7flakZNHEZO1ivF7hPOGwLR29StyZZjzvpYE0u8cuzsL6ajpJWJ9zTc3NYYO04ubkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEFFhItczN1u_ERfRQxh1ZgxPUNhoEEPPzCwOBoGCmA_dFYmn_h0aGQguW2HKpl5u4S_4sZWYYIT5bszrOFsugE3l7wPgYQXCro2zQ22OuHWKZ1AiIy3EdExcMnFc2ijXrRbqKkmufmuXj88jk0QhORcSvmNRo3X3kK3OINdhnaz5CvzGduLBOny5fbNzN4StOcjKEvy_BrFatWQaOq8v8nsGDBynfw-CKCdaMKUxtoeFjiLseq-WFQcLAXe3DTCYESzHu8EThxG1r1nsz_KddHKJdErOONg66h2z3gNTREQUjDAbCk_AX6CUprD8k1lHJC3vySIoKTPTcsSJ-qkAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzyZgsqLL222VnjFyzfXj9Wn64ztgfyWJRA3UEEoMevSogyzzQE99rkDgt8je4bEijX59Puo4m-PmssKSS7Eb_mfcHiNMIsMX8JmZVSUDmJ6Tvi5CvvCqBwSNxbPdFkdMD_5i2XgeC5viPszB3x7OssSmiNnAk9nheAPoF2EwEndBSf14oQ1RQ1EwfgY8v3VOQR7EdzUmjaRNjdj8SmF1cRrxIBvHW7iQHzpU4FgparZGZAVn4KNU9Ca3cebjJ13cuhEpDQlHOl3NtvUrnFruw74HwW0s5ImD43gmrqyYYibeTKfVtz8npxaluRGBiG1j_6lXfYOyXm9_wFOTJiNsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAWYL6ymeB0gT2hwz2Md-ZRqWdNPgag7nKxlPBb4sZfQNdVdyYr6HPwQc8yLxINR6JNcxG4qDKF9bZuAelPqGOVVbDKl2w3ccnNIR-rV4NtFl3ab-D9QoWQ1sGGdfIPCv0rCYhfQFJmZvLxehETr7Zx145iibDR-ZQV5xlRBPEA9JD6MCsEEYXVb0upR76uRFNtojM356CnkhSwSBioQQRAhQMusLr1wNM1TE4nD2Udki-ii1GM_ueMTbGILidId4ME7IM-8imdB9NVTOMtRk4mqmCRCbsv52uH3CmK4Y4XcG2QQdg8fz46OxA8_ELvrDkIhxpRJjFd5vNR_QcSyfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luu96iAM0wkd157BxyfkMmTPQkXgJWVseKHfYohE9hwKDzADLUf-ufRW5b2xxCXIwiOSsByxVTovOp9SqUQopExmPgUVZs5H09ExFcFht8kFsUoGOTQ5rqJ7XiGPCRjutjm3ClJAr1ncXvGzRSacxf2ItrcIogaW4NendU6z_kkdpwuyTEoEszGoCeroycwI1heoxBbrhH3EEp47Beiw4ODUndPoUD8fndJ4VkUCcoO4y1NQiEPDxlfHbmWLZVWQkA9Mp3-SDaqBJkyk3XYESnm8nLSydGyv-xnY1q8S5nywz1DxoxwS_DwL1XPjULemu9i9ozsKdVnAjYuOBehYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PulLTIRltQKWZP-bpcbD_y55frrPpkhTiohQVR7ybJnzcykrMepYjhjPJX79sAEQPxIlKZ1f1FL0-efmB5KtwV7r1vs9JOkZeoMC2kql9FZ7jQ7YlmIHrR41F9Gu8qmDuL7IaEylXQyltODPEgmf5UTA9OWFj8phNN4RV-teAVvBLmdLJN_1tkjpFsQk2RmNBpTqOAKrs_NKEMfaEKDL5_Qsu2xK0v8jhtbsDeRJn068gdCoidlbv1ARLta0VQpg-xK1tfgPz4cMwMtcM9kmZ71O0jw7CR7lks3UtMyY-FsFdIMo4x3dzjMFAxsAxj2Y5b2xtSKLSNbMJOn0Oj4dRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIaLf2kg7uGy9oHjSQ286nW7-X89-xrtX1JFjNu0RLrfktz1MDF81ozAcPng5okoAFVX1EuJz1tO8tao8J_R4kOYD1w-mFznIlBhoPDCeM7Hc1VFp7yPs1u3IhZG1uey2sb04vSxPOGtoK5YDB032OaAXentLG5Qa22qmNqxEjg5dutOk6g6fKt51UM81BD5KyuVuzRVLZPvsZFuHK0VBhse1622Uot9Zb0Q6dj-qMAcnXsObHWWPKCxO6dLo5JPd6faZyTLXFALYBX-V88a52qyN9kOMga45q2WL2J0SDaptVdQjOVscUnfbNmb4IkZlyEh6t3xRTL6B1LSPZqRIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o11aL_z-FbxBVJMEAiyEQottC3P6AUWL5n0d31o161f3qFNsCnJBzcWWFgwY2fsviygh12Flgx1f7moCXLSjoydUhOARXCoDmAfxqEPmMupxvkhL53n3clhGMMMMK7eq96nygVQoZc5NtY1u2ZF1QzeCS2NsuJZHSpAPFMhkw0mLsjHB3mcRjuCP4r-Ox62ZhkUwIER_O2d13aZLZVYiU3Ko1JVz5HwE6uu_qqod0IqdTkayhhBW90QR6MFjMwzGzcb14d61nZVyUFae0gePc0ww4iDwxqDYfdn-fq2paKH0ia0N87RcoqxoHuW1D02anLnYW6hjJyzD7gVJBdiU0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0ItjS4XlEAA4X_MmPf5oNCa3Fw1155-rpH24F4ZJoL3bm_Zuv7W7rSsse-2NIs6Dz-cZOeFpz1bU__WbWn17CmZlLriee9HohJFo0BaZm8i6eZD8oESIHlNOZTz1QEt325krUGobn6JCCcE5aFWnF_LD6RwuRXBFVf8O9l7KwPQHvTn_aGtMsKCzIk_Yu_LPlH3LoWTpkiX5vYCsdqTBo21ZFRo0bpzRi554JeySFQRqsT0wcEfpihxjpU8gXNywYEn_3ofWvM5NvAI2s8i6WxcieNawut0Jxv33RMldJ7kNsj9jLgeiu8ZQIT_wN3-QbM86E-jKEC0cqLQ1AJ13g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq2S6AGv2apA4TxWXFoIPCl7krzOEC3dN3IPljUhhLBRFhNvnAJLaiF3L6ghnIu4tRiknRo6kNE19qlpP_DNgnSXE9nIKsyi9id4D80SJVWcifm8aLdEDFkjs4nCG0ISf6Loa467YXYnPnk25okSiVy1Ej7VxBJWuotJ36AjOg-Zd4cnZJVmVRhMZOFOI6gHBjC03qChS6FOHy2hdDMi-Kx7NMTAr3sH-xnxlt8kriHgTbMZ8TEFo-Lo61gjKfZwmNl5tYxOOw6grouOSvpNekVwBioRa7_oZfHShZEkTlFOVhzzqLjyvf1yhTCOWaoV82hlu65Pa45NBp8XbGkAzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=CQT1HElXItb2LOhD6LNumzOeN0loXr2NOBdOtW0lTCZtzbztnFcs60jXrUreMBoYKrCLxTTa-CyV2Sf6zXx64bIXVs5Y4GS3qF__vRRe8Cx5hcmL88V8B1LAJz2AmzyqGcAKG0YL5ztIkR5AfkEvZ1kzHdnkRhuVmjAZxqZDx5CzAtV5kIxAVs3tPCk0-gXxQHyznPn_bUPrDyPJjZLXhPypcnexKtEVAUWb2EBdIgVrGyME7hTWfpdtO8rNOvUadJyw19fUyA4mxBdqeDvzLWZngsFHFn58gHEiKg1_0isOdjXQo-h_LmytUKqEbXFrk1C_ctKHlm7PKxfDR9Dq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=CQT1HElXItb2LOhD6LNumzOeN0loXr2NOBdOtW0lTCZtzbztnFcs60jXrUreMBoYKrCLxTTa-CyV2Sf6zXx64bIXVs5Y4GS3qF__vRRe8Cx5hcmL88V8B1LAJz2AmzyqGcAKG0YL5ztIkR5AfkEvZ1kzHdnkRhuVmjAZxqZDx5CzAtV5kIxAVs3tPCk0-gXxQHyznPn_bUPrDyPJjZLXhPypcnexKtEVAUWb2EBdIgVrGyME7hTWfpdtO8rNOvUadJyw19fUyA4mxBdqeDvzLWZngsFHFn58gHEiKg1_0isOdjXQo-h_LmytUKqEbXFrk1C_ctKHlm7PKxfDR9Dq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLU4lHUzv8ClZ6YxzJn1Xr_wdxCaWy2KBaFMmqlfiCi9LaaFS2LcPqMCwOxtXq2mmrvtm48kzkHavMNIrBpiQsG8OnJg_LxHPdrjHcAnX1pHgA7ccJnfja6Ik9GwivIjYq3XQIg5-6ER13eeJQCL0uBcvYNWzUcJ5H5kDHwaseMEZ_sWP7xKeO6TC22kxSTbbRHVjTRmzwnfzDw3cWtohuhwmEXF4n_cKpHeXOpKLGIt_QkCjyBvNJV9CJdXeX2NG-0awFx0lbcj8jutSrY_VpI4o-EmBavn8GtQ6tOttfk3gQqmY9IPhIev2pRmoM-F13Hcb_smHtyK8S4X8113oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLWnHWdSTBI1MpN0SSKIz6LQ8Fxh2N8bxFEcl1DjL73b2mwQyRbvKJr-zRRU1otcXIstmtQZNFbNNgb3Wqtl_XYeOIXmwilELZqnoJ_WL0GVDQrGj-i8ji7Vm1Z0vDK_sPkLIztzkA2mu88kxzUwYkNKMQsJC9hDgaVGRue9_Cl7R6aethx6zyOvl_JMZWEcgiPGFUJJrq9p15Xoe-3-M0y_0b5iSrnHOwwErAuc7iw_od_TN9BACMcvlJ49wWRF1TGb4UGIfS4-0V05caCKGfrrBJL5mGsg6YPRlOM0zL_k9_lfasUwwoY1rWB6R1u6YsK5iOe3-Kdj6G4RXZr7hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWHUkhLVyT4P2Izbnob63Gbgz98v2XXHt0Z7KK2j0QYmXfZe7Do0rBwGXrCI8LwA07S28CdWOhYdba4ah5vs2QsdnCWnZ6nSmjtXvKPGJkvL4XkXC-ydR3TUiEGMOf-K-4qvScM2HvaMNk2oWXZqmdH9Ixo-DavK3Sh7FtL-gcURM7SQE-eonoILPrgVrqPe0hZl3tLWfvdoqQYw9r8lArMVv5-vJRSxjakC8b5suZgNQhv_ynlk9q8VRqXFvPESewjtfr7yEUXfmQ9x-LnB3Jt_FlvnLTKY2iS_itF5sZr1LAkH9GcEfzvcmS3Rr-3lJ_KBZ8J8dJnpDhD9MlmFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAaQs8JbRS4e9lIFNtjLgaXKDg4RteKxzmdQAcs3hjMPbGXBeIN_s3E-GlSUlYggoBUOZacX5WNHMK55Ic0Ar6vTJWgjhQn42AnfuCeou-QHDU0b79a1f-igCjsG6nuVTFridWD0lqK42Mp8j0nBTvnfYoJbUY5HHWG5VkHMvcV7g4Ae9veseFicwxB37rtKo4w6euSLaDAUKy8nhJ8QT0exD2K9xi_y82oC0vnVxXgubF1jl-jwhBnYADdp1W-Vy8racwe29uYOXmxQQIHXU_2Q3419nSG8x3gi1o2vlKkZXg6gRnp62Vc0sONXFz7nwfJl3mS5IXOxwqLqnecDIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lV54VqIV6M5ZH4ndnC93lTNHqgWjsIniof8KCy5bC6jkGzGZRweK-qhlE4N-BPH6XOiSLev92Tibn50L6f3yg0jGaiyOTdZvKV-5XsdX7GKI8bDJB6oE0mFnlOecBmRvBvxDJJKNP9Ra3cxpthdmp_5SCDhXD-aEC5zZhGchQqEn0m4vuNHcx5NYqS47yfGDua-eebuDgvN1MUKU9XO-d7W95YRoFhZqkIfgOwXmaosiW9T_g2-KUPyIbYtyKJSYreqNgOKufOYakkvl7zLmXwCa1njKozJPyAAjQ4ZjC7lOXiQp6aznQ0jkte3jb2TMp-C4qS1p09iG7IRvRl4UJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WI8OdYYGaTjVX9UlS_8kmikV38nYIe4CcOkwOTa0hyD-WyRETAsgPyvZAy5BJGIZGzDW4xNpyHz910gVwW2KnLW1DsrRESQp_Z9NmHQZorgNCn9J2GiONYL60x28d1GDptXKImZya7lEVS_tox0hDNtUwusSCBj1RxdRUwxozBiEbcWj2WKgLOno37rH-9j2V7Y7kOGLfjJr5WBg98V-waEwkC3hYQ5abyK3HehaHtKPQcHv_2Lix5lu4TYdUmFjdpOOJTc9GJpqugmc-ijBdBI3u3ryhsFMm8e3X4BVGVygvuiOgGz65UjUYnrtvmBNH9ZoQ1ivVfSdTaKyw9m5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7rKo5Va0fnhhn311KYuF4j6ZEowpBcMe_xHJ9I_LglWWoYxcgt3lBAQNsnQud7iNINwwvzL1dSD5a2LliWqHhivQZSy_eazEj_JVX2T_ioSKrrh_SRIOJvlwoC0T_IrRopG8dXxzg0VKqzBSbyMI2lyH9uQkvaV_k_h2rtqho22y4LkIvSri4ShaEAuZDYNur4D0mUlohizOPuP2LdtFw8r7pT_mitf8qCur8n6jt9hhzsV5iezg8EmGMOAj78Ly52cLShYaPg5TcA6ohPfOpEjKwSc_0nEuGDcTi1mIKazYIrj_MjSPY4HhhYTrabMQf6kzqFHYFbAlLL5tBniVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=d73PXUy2tfmM9pjItS9lWxEgsPWmPdUhqq6sD-k_tqd_ld6__SAhVk1NOeH8HvF43CDxmmWmdK5Q2oQ0G6LWLkRwDX2MYLWjoPyBkP-qXvmcIyaxlmpl9R1eOmAnCz1M5ZB8uqK3xncbhd4JVKOe1-S0HB67VhEnD22-l0Lm6tC8IRN1OTIdP-9wy4wllmLpaI_JVUAGmeExjEI-bgHyLagsIbSmMybW0Ztn8XmgZh7wcJTWT90NbVKHXxn7xsrI7c6M1ys9BipjdamcfgzDb3Ny_ySEFwc2lA3qSRbOAFVfp_CKlQsB7_tqXQiGwTm2j9p4p4WweI3Sa95Lg5ffCaQeMuhqKduDPXvVIsHuXHysdYFQ8yggBMW6GEv3xibsDUPMrfYvJg0R6YxT77q9ZEm43w13g92V0L4y62Y95xvHRTfb2qleq9bGaqpTRZ0wu8-U3aZiENsgk2X3DVFTjwQzXm71YJHFit4xdifv-Qjn-LqB0HVcG0sGLUh_DAyPY1VHmeevzVKXzKfPL0Yl1ERXJluzdOc3LpzwyiI1rCoJ0bruG6YDWWtqCZjVu32ovgtVUWnNN9MwisMRp3Fp2HZ5k0eHL-HNljVNeTVAc7_MTIdrajTZkC5OtKPGbDA4Hr5vEUXJAkyeq3EDbZ5R4NUCdi3oPWDRJJps6OMdZ0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=d73PXUy2tfmM9pjItS9lWxEgsPWmPdUhqq6sD-k_tqd_ld6__SAhVk1NOeH8HvF43CDxmmWmdK5Q2oQ0G6LWLkRwDX2MYLWjoPyBkP-qXvmcIyaxlmpl9R1eOmAnCz1M5ZB8uqK3xncbhd4JVKOe1-S0HB67VhEnD22-l0Lm6tC8IRN1OTIdP-9wy4wllmLpaI_JVUAGmeExjEI-bgHyLagsIbSmMybW0Ztn8XmgZh7wcJTWT90NbVKHXxn7xsrI7c6M1ys9BipjdamcfgzDb3Ny_ySEFwc2lA3qSRbOAFVfp_CKlQsB7_tqXQiGwTm2j9p4p4WweI3Sa95Lg5ffCaQeMuhqKduDPXvVIsHuXHysdYFQ8yggBMW6GEv3xibsDUPMrfYvJg0R6YxT77q9ZEm43w13g92V0L4y62Y95xvHRTfb2qleq9bGaqpTRZ0wu8-U3aZiENsgk2X3DVFTjwQzXm71YJHFit4xdifv-Qjn-LqB0HVcG0sGLUh_DAyPY1VHmeevzVKXzKfPL0Yl1ERXJluzdOc3LpzwyiI1rCoJ0bruG6YDWWtqCZjVu32ovgtVUWnNN9MwisMRp3Fp2HZ5k0eHL-HNljVNeTVAc7_MTIdrajTZkC5OtKPGbDA4Hr5vEUXJAkyeq3EDbZ5R4NUCdi3oPWDRJJps6OMdZ0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmc_h6QRcj5MHoiM1RQW37EiaucqZxN_Y584DxkTgCBxn41Ea_1B-bO10s1cUGJb1QItDeHzM7i6K81N7msoLSODIyjzGkrr0SgGP_ih0Y0SUbAmcLrmeh7Ms2AGQXjKp4ZT4sgSjYfwgtgVHTxDHLCBrzgV7squSb0I2yD8vOXlj-1PIpyGCdiOW-gkXzB-UkNGRrQwWm5RwPjI6mLvwTjaYYZUySK-RCtUALUuS4sOT9QWsxXAPFrED7GgbePzsRs5ygazRLgqTg8ondZgvOVtunbPNUblPdmMcwur_mAlPDs82cffjqjUptDUOnQgQ8bxcvxea6_CYJ2eLAuLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2sSpLr27RzqxYj8hh3525dNSEenUqW4krQQcRBD8j3wSPpf2bP2W9tcz4sN-qI8oPnnOVvr2Wssjh1s9ek2BTqXRRSHb6c25HPop-8yrp8v0LO4ibvQZGKOVFsEuzabfh1XOfJIDZZS6zrdvr3wia_Q3XCJQIDUciAYgVvqMWRHCHx2w81UGk-p5W-KYx5Wabim3xSG-7MwwL7uIWoI874K4Qsw4ElbNszMrO58QXKaCgGZoiYHMconLn_CxrMXvSEVEWu-nJbf6ywcVmJY_9_vQEpXHZwt7GC2w-IzQEQMtU4XLGX3vGMkRFFADzP-1O1CkzvtCvnZOvlhzG70tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzfTEuWx32L_inmOWVE3ChLJdjFqPOQEGei7KWTaRZO2r0AUSCQbiJVdQPrV0wlafvJnWTxXlMeb_QJWHr1G99MfJK7sbUyIl3HeOjoi8YxksA1_RumwNGx7XfsLddcQwfa6apF-xiZcxWSh-xWcPZuAr9hW5LCyLTudhcUttCSy_PgsYorpmsL56ARjo-4vxJETlpIKkj-1odjDv_uJ9aqHx-pRLjK94_hPKO-YGjoBJCZJnQjyU6b-VN0WsSKcY7TI924QE5nLjm5vBtv80hWseZ37d29BBJod65k1v5HRNYx0hneIbXtyHobIHAG9aMzJbCq09RNVh4VcP_DQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8Xq9JqWBMB1oyr8bOVPSSPEO_Brbyebt1yBTbGCznrHUNZqCORt-LCDHIXR9JMmoLpncKu3Mm_P3NHX8vYRmC4LlUmx0MrNkryp-bTYVPvwTk8ELfQXZt_PrxF50DmBh_Kg_h4I2mkZwPseNMXk4Ve2HssnYd0Jl4Fy9Y7AhbICmX358t2KRBLsHcvJ8L7i7uAv8dsoH_NUCg1R66GdQmbuy8Dzu2PRwQzdQZpq0MldxkjqY3sH5heeG3iBPWj8oL0t8D88tF6ITh8qlAYxJOFhOFsaJuJ7ne8Lv285bnybINnlWUZfFCHDUbYxW_h6Na4D7TNX9w4W0_OiwS9y4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9oKUxMbrAIN9atc1SRYcOVP7Ke3y8tK9hddHi3H7N5MjvvN_sGlrltH8lN7TXcS9celW38tp5r16YFrNgKFar7w5R3EW_f7LMhj2-oZbhVUSTq_9ytBnJgFaYLrm3HEbmMn1m-ySjLcdmAb614J_Is_6a6vMLuIOy_f1v-xDqfaTOCxEvOyW8zy86hV5c5y-3Il94Y-A8M1wIp7YkmZdGaf58EVaSmty2d3nEPX0TRqqO7Y6YIZg5Jq4JooazdQx2xlzTzIFKQlMVTspv2sbxZGJuIEPS9gddaIyAZOBbriFIDuukPL_Pw3jb1Xx7SqgGiRjghSmQ8HDFQsfVnYig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aXqY7V0bcno_af9GUQiJ90edM1fU9ZRBpnxN1hsXsDx594a4-HDWdDE6jJLnJAzFxC278Wv8p4ovrv2iHtUQwd7fZeRZ5nn7B1Ue8lUZ6g9eUTwhg8Wg378qm3naiZICqZuAT-2LgSzwsVdeBO2YBb2P5Bwoy7t8_3qBuS44qjhpjy1Jqdtz0CR8sVkcc6nfS61qubMHSpjGwkQGn-FODvW8msO9a30qILajmb7sgI8v6sARqgi1NvG1EwxYQDQ9hr16I7cXtvapaHRoSxOGiuJS3Do_C5pd3LGV1Y15UO5OzXGmZiwJQmDXKuSYhPELD6qkJcfM1otdJgyFX-c9aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aXqY7V0bcno_af9GUQiJ90edM1fU9ZRBpnxN1hsXsDx594a4-HDWdDE6jJLnJAzFxC278Wv8p4ovrv2iHtUQwd7fZeRZ5nn7B1Ue8lUZ6g9eUTwhg8Wg378qm3naiZICqZuAT-2LgSzwsVdeBO2YBb2P5Bwoy7t8_3qBuS44qjhpjy1Jqdtz0CR8sVkcc6nfS61qubMHSpjGwkQGn-FODvW8msO9a30qILajmb7sgI8v6sARqgi1NvG1EwxYQDQ9hr16I7cXtvapaHRoSxOGiuJS3Do_C5pd3LGV1Y15UO5OzXGmZiwJQmDXKuSYhPELD6qkJcfM1otdJgyFX-c9aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0AZa1q4haR2aNmNHvTYnjtTlINLn_GGXQEpMueswkWXaUWtV3Cl4nLn86OgknqQXMY1lgFmACCFWL3stOVaeLf9OV5ym0flqbcluYoU2IDOuxw0wu2vUg2EGObPh6yF9a-tNfyvdiM3kZRvlBVEDBBR1-6VLby4U8NZQQ-CqMrWBjY4p_J3GdMiksw__zLdgDQptvR0B1EpLrl6mC67HCdY1mxmupDPcKp8kTrwq4CYLzBic7zFaUojYWFL91UT2E5kyKuOspB1r4upyotzGJSJcUMFNbsjxtgvv27LcjonU8-x_Hfugs5Bwoyyh0QoCPeRYH6RM8egEknSA2m5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcvtgoQkBM9ytxWPnBjPLq1yIhzY4Iif3Ir0zPozes29_eTtwWlb32t8AiqLsGukS_Bbpz4-TtEao-Im1w-MzmFooTMU9EDdLGD-1PMuHQZ9ryvum4nuJfa6kgesNILgITZ50Kx0nWDkeBuoteuyz_ubGdQkOWjP3HsrKBqljnXtEyj6qLfW528ZB9OJ65FY_cEXWMhQKa32zln7Droji4Yls1EUg_Bg_klqKY3LTAp0m3Bu50ypy3gr-aVXKdmU_gzU97o3rn6Xp52LWUTqVPDi8oiWFescwdcHN47XKMjvtVEfMjKNLv1-hGNTo8Gt4p2jZzRyxau7rR5TZb9XSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN9_yMOvS9BuM69DOGbfT4M6ksHDDm6t7ndV76NPErHKNZGyuTjRfJNi9e61gXM_hr6aJBiujhi8TSkxHpQNO9mKAN7_C1SFDd8ayVmqFDB2HctdiMBgFxtlWwKXFna0L8XkQzxoh2rVC1pA8MRIJotL3PxdgjE0IR_d1_bl4nU9sL13aITvEny7pnOg4ALuW9rg49L2Dd7fg78_hWzSdmznkXWjS29645RYnvh9CRLoowvr0TalHDefpgzrtFwZOFL6bizlGVGIUJ59jf1fh7oNGz2n2p68qVvBcdlgMYR6tJDA7X-uOHKjKfGrdzFiLdxL1ed2nqxzrW1or1V9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmhSmIhNwlR0EQ8oe7_8zWE6oYn3Qc6cKNDz3bH301kjXaBEQyKLyoEp0agyw-VDpy9wug0aKDsEp3Clf5U-prk9viDYeAB61kAfUcXeYLlwjquUnEAN48GoWsmbrJznYdk1z3fBy4COFlFjd8d9EZo4yvkaZ_m79NQlWDMBxqt5DW_b3PnNEl-CyXAdLTqO0FhucuJS06jnEBHDkm7AQ6JLfRhksmlnUBNH8rzlvHahYIvNiF6GOjMEryMCzUWcux2ttghYvZiZAC3GGSZ_81fTU92JXfbZ4dBMZb4jV5P_Vd-xz1Qhew3aA37qQ2ngmq6UXJipQkmCGvuHscUqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_PU0qkm6Pz1utNXvqHX18zrLIv9RQblza-EQE_h75FJvKiJ0MKBxZnWs4JEHYUd6v-7neYYTb3yx9XW6KlGE2gcaAMX_-h6qLlrEMpYOZB5XY7A1ROqPpd9-sK7IvvPVXUR7f0iZnliTZs6tX3SJzmbdtZEj8BcEzPhjTfVLkUCMqziy1FOianpZeYS2erFIzEFkhofe-ZURUBui3BxIKcBUOJT78krLtSVptbbdbj8qMkOoK9TlatZF5hQNmeFylRn41xkzTZV2s9GdYf5tBRZOeYk1ScfplT8qEcteSmKLAm754s6DQMK9eFWnT7bonmTxyojOsAsRF-LOFhGWA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
