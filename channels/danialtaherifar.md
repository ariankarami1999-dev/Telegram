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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 05:43:38</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 87 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 203 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 291 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 439 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 704 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3UNmTUujj8xK5RlrCveszINJdqZuxnZ6MLAVNJOWTQ1DVaagQNNArRRd7vISsaQSk070tGDOcO2fkRexuP-EqTSww9-O1HJdNG_otghEMSa57KOTjVStUO_2rG6ASZG7LhFYQlY4dijGbaugGjYvPXX0ghUuKxfcuj6H8mSJpglqiYM0QsGh2IW6iz0SAJcxmcxRjovg92L8SlkHi6FcQV9XWl9R-vB0Jk6eeK76oeC84SjQ7XplCx3he6o1Cnjte9tfTdW1RgHUwcpZyhfGHdoXyiZ93iwKVL6AOzOR9-I-6Fr7D7uU-JgdenZGLyUk_p1su_JrhNMno2a0Pd0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJe5l8doY0JqpGK4WiO-ymkRlfSC-teBGn9D0cvc9ak5QVVzbkQqAWL-Ucly8F2wqRU5YABGiAq7vieRx1TUZBYYKtJ5hykRAg5WvJ-5m2P6k6p8JeCdoqtN_F2zIDEzQG5JVL8zau3UtiJW3b3C_Y8PgCxIZz1pjN1_2rJakiH97uLQCHqOjDmAES9DiQOAhzjQ_L-R8ZSWuEuRvYLrKodgFLGN5JucQv72_B9CNjtdvABJ737xemjYzMENmaIAqvEcqSnZzUD2Prtde8oZ3G2uS-H8fmyR1A3QF8-4mLaD_XtFl837B1-T9OFQ76BsL63OR-eswJMEmnFIINa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf20aaDoq54qn-MVHtLFx5KEf4ZzqTTSAZpzVFo9pWFKGSGD-uobTxvXq5cJDGFdduzI-F-Bwes5GPhtKRHllnYUDbUvbLtSaUCLPtIWK8PNNOHsBOxjK7BRvKCrFblgKHNEbdTi5EsMPlQtawxEIJfaZBNeToqS0LmZ284K39mT0wCZHdm4C0icu7hMcb7UD_T8vO_j3GOaaYRaQdMcmiPqmB_MSnNCDOg22nmC3WInncmLPP8mhgbbxu03ghyGneb_zOFVxM1l3EmRyeA-ld97VIV7nbbkYEOEJ1xx9oudDc9KsiPSGrER3voh-pbv6EucIr-5XNW95v0OTTAb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4g7Zc-fs3udd3dyzTzmpRxrGe8Xa8h2lWi0RGHUsklit9e_mvTXYKRu6E_hgtFtEgOErcthMrYjL525F4jQYBu_Qu2sq9EfT74zA1eGwd4lONzscBxxNqslPt1hGu0RnH7BP5efrszQkxnhFZYfYBV6w1ey7dVrZrUfzlifJXlRz9qvpJQvI4xwwT0G1SIqQEM5WjMdV47HagV4jIxpOn0sXGyHo1AFoZNLqv6tUL8gTxrVtf5J7kCxoYle6NeVOdOwr0YAk5uQNQ6oepbK4mj9zTUXbFgkV_2kyWXYMfebD0NdzjiLYbz1ARKthMjW1vuEflcUIjcjuMw5PuOJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeXu06ViUTN7WxTBjx7BIA2h9O8wcLVPAKA5nhi291Ayhjda5jXOU-VfUlH3i5MKAh5WMnA5MFJ86TT8BhLDYFboQtjeDrGxTV22_uwWYp0wy_8_2DVoxDfnaYf92cOOB7hgFUedfzNMbGp9Ki9lBEfPNeLBS3HMobNNfNSkYENE_HyWAkzA-DEiFRQGdkoMkSsi7pj4hQBQyCQqLhigleAn3bhOLbCgWdvyrt36uGuZxyGLpdChksUhrsMHDMFeP8_mKzxOjDU-JSN-Q3l9CY9k9PYaEXjTE5ouy3o2hqdgPuSjO-xWnCnF9kBVyptjTEvpHRpEdGBlZbXVQ7EKRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_StXX5d6ahcx-B_3gAcojeCvJhWuWB85qKY1RG89Y-llrgWFgrOEUAMlpczCeUcsTiftG2sZlhCG9_5Z42xBKXQ216EKSDeh0q92Ukfj2OJ1USUNv7m4RZbzG_0uHM3USzg27jLaNXkLmUSt-Fl6yZXWjwqyYjOMD1SL7LNq6Qf87Hx0Bd4K6t6f8nNr3A5-IB6t2zhNeStYdCyICF16vz4pHQR9hdhdeElNLFtXyQixMchRg5RhbMdOeCtg20rqm0iDAja7QA4zMECHRqFzO6qm4aLtHChUMTca61iqCVuGnmn7W89Mp-ZBbCUcs2AIwa37wKS46hOH297X9KoHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m70Kf9EGnPqFaU2RDFW1fq3he3cCOXPZ3x9zfc5RHm_JqCsql-JQLw1AxqxbnZX1BXtUt8XahXOv9g-A3HORxTKK--JHym_RbU3cWLBZgVkjEGRi2FzOMPMBntR-Q0WnxK54iI6qYM9vxITtXEWfFJ_BUxX1TlP1f0a02KHws9pvtEpCtElHNxcTpDgAPHDA7Xe9MH9E3toLWypXYbkn1UYENvBw7BVI72NMdr2o5ZyM6guY-JlRE_xb1SKS6cZdsGbXaX7ZePQPp8gmFFTIUDKlCaI0kZvuJbN7l3rPL4x5j8je7Bg2pl67uBBZpobwxAoLZPKVunqUfSdXq2t5BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BG8y97_82RKw8uiZMuLRJbbFTRiVPkoHDL39uEVrJTDCNrG9i5XKaDvWyst3DcsD6d5UtA2nXX_G0DD2LIg3nU-TU5SGXtjeBpXpT9Pc5oiFtz_ZQskLkNyZFsaoc7BR7cY2ZSp4cKlIb8KLZvh0WVP4fn9OZ1H_Z-6pUjGR3Dvyk8nIhR5h_QWLco5nd0Q4AC7g20BbVvpX2tWRrFdxCDKJJgn9OH27_ZjpADVl3cydzxidh8EwNz5dvDEv5ejzBBD80vR2HVgUPrEtn38CVX9s7qZTyG2TaImvJPo-NzBjEI8IJURBitjLlPpQ84-yiajYPi1--TYxLqauN0upOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojJrd6XrhlEGABQwYXvIJek4MdPRn0zVecy9GisX4dDeNqXyHbpzY3qao_QHWrgU-4_Ff48PS8ld89ET3WsL5LuSFuY2qwwkt5j5WDRqHTyeAPAmIVCgEOLe5aAEQvcEfYHsBYOMo3hA7ieUUIbPa8QVNh-31yDpCZmO_fkM_FkzOeWWfIhgO8CRiC_16jrSN_aCUt6XZHKQAwR1kdwgn5UA-7te0WvqdkK0F4HWi4ion7_KyPfz2hO4-a3BHBuT-qVowvOUHhZoQNwK8zas2xhWb5nXG7yhv-m4Q7yCbDrXvPXWuUfWhLxrmdQQfO95DbgmM9Rf5tL6xFuodNoETg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAWuORviAsUQ72OiJcPmiPZcDzh7S1LX08WwBcBcYnB203gdri0K9DBk_AOg21Yx6I4Wc8kkUz9TnEWLB6JezqJgKMSjqVl7frofJpJm0cFd_54uWsuRSsUFqZ3s_5ATancf9KG6h343yzwnif-XFM9KMwqfytC2hNtLApJ_Nkx0z2Q21uxHozBIepUQQbwP1fiwRIDnV6DlVgEDhFawy4NbYU5-gpRtHqA__JZvK4BLhQTR8hh4RTEkkZuMHeE6_eBvMkZLcP_oW9y1iCBeTUezUMGBoYTNI7q_tEB6xXyJCXsSx-gNXASJvf1QX7ulG3xe4IYJpAc5y3S4hdkddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWPPJG8qIYjJuFGTz4Vt0ACKfzuvv-LS_BSdB7eLCKwCU2iP8M7yY65pwmRFFgl_vCx6OmBvzS2R7MHoWKMHIGzHcEWgfz4NE8paX2edO2LFr341XCl-OerDEYrs-wlEtXtsoum2jagAwSKn95ckr64QiwKfCULiVDbmeFSP85yIjLRlwzJa8FC7--esnA4TJZoyXKfkS5YbqozOjOu9wfoKgDNwUKkxxe1fTzHPF15f7fLthbwQxNxwZTK9JjrvbvNEqDyy2oTJoceOHkiAX7RsyucTCtw-lgRkA9xKjMh_zCA8ckhl5iarMlquPMTj85iXpSAJNOQyjWh2kkXPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_etI8jZmT3YFtD6phhiV_4ZRORhCFB-5zuYXUf3Vj8z7mhSRRROw7MUba15BzbBIp4fNxODHvuL2QPg6Y7wyCBnYLeoL0-D0ahl0_NCveA9HcRysFW_oH4Lv95jSr12-4ejdDqLbgHn4JNEx7ZGcivb0M7Ggpb8HTO_7hA9t8270r-zcJGd4rnMwfc9M60BR-iBgpQmFWwlny1h1XUArH1b1dv5z25ppfebOsNb5AE-3gvDtXUjZlMzqShq3lOMowVHUJGxUwaI3oj00VS-D-XcxiYPPmyiwFZK_XzQmH-JDJSi7a2rnhNBY755sEjXiGoAtd4hDvyrRtBEGw5mnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sh_uOS9DOchBi6gicPCY8DeD6NsJsh0uIK7qwP1tbaYUEo9RJg_6jMmL6KiOwbWA4aXD9IJrZv8GscweHtYbziNggVzjpjzYLN9raeLhy2_lyAy_RA9Pam-7o1wznOIH8PB3qyeD0Hieqc8iMATUtetKmF2TDyiI-XkJcgdC4X-3kUaDz0875nXC1skvV9Dku0nsFyGyuWzRDaaj55xpEuFDEF-0Q5uL7fPnlcEgkD-s9FoLyBCuSfV9xw836CzhLdreNR7oFdwtq8cT-o3tK9EegN_ZFYKcKljKLDLsej2I2oGBTHrFwL4D0epvKRuKeeksbAfqvaiu4Cn7TM5YVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9BWBXrdlBp8lPDfZTcpuWIhPWqXBnutiop47GPiNqDzC_KPPfB6VShusUkGKdapeXQ4J-1wiJvWok3tVp2knBoNDRJwKnNwcjBe8TBDvusRQzQLQOJpnbv2OAbAAmnpAdC6WmpONMnVWlcDIfFiPlxtDlGbhAXZ33nenNbL9lK3gjHB0k6Pv2dlQBkN3fh_g2Z6tBiHLG3KK4m2KppluB46zbj4q5Qvvsqr6oo28N2vQjnD7mL2AsxGQyHG1F_O8rFnAP9QVWFtPkH6IGQbI9ryf27EaPwcIlp6SkTSKvpQvBm6SDmIwfahgbOgwwLQjc4yTwwmKEaZ-xwjZ_2oQA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=beMpv3nJdhTEvSxVj5yQkpiq_W_8XQbLFA_-O-fmLlZgwXBlTEGsIHPhmxvmgtnY2i8L-pF0bvbpgjcdlkIO9IacU2Dy7v6O-e14pwKm-NvfVrfWTSX8-VFu3hluT_uKtSSwqthSEH7AfbLjlL7KoTMMwLhCy7_37IHNUaliGp6DmAhU-mnMsb4-CAZdrt5RePrEta-gCBrMSKBsmawVntwL3pG2cH8l5m35FBG2xrS9-CkrUkd_59IxdBFf4ON1O7AqZaDpJ50Uu2hyPDAkSPKdvzg6wHTUH8Vbu2RaCg0FNol0rWmG80Wo3Uy-EGzUDcpEN3ARelaqWBaFZgVCVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=beMpv3nJdhTEvSxVj5yQkpiq_W_8XQbLFA_-O-fmLlZgwXBlTEGsIHPhmxvmgtnY2i8L-pF0bvbpgjcdlkIO9IacU2Dy7v6O-e14pwKm-NvfVrfWTSX8-VFu3hluT_uKtSSwqthSEH7AfbLjlL7KoTMMwLhCy7_37IHNUaliGp6DmAhU-mnMsb4-CAZdrt5RePrEta-gCBrMSKBsmawVntwL3pG2cH8l5m35FBG2xrS9-CkrUkd_59IxdBFf4ON1O7AqZaDpJ50Uu2hyPDAkSPKdvzg6wHTUH8Vbu2RaCg0FNol0rWmG80Wo3Uy-EGzUDcpEN3ARelaqWBaFZgVCVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt27rH8OgxF8ZB0eR9BIrueKMNIFGREUiG-Vho5XU7xyVXayy5hvZDuzuKuaOcqcBjsmKczyDNcqhNA0pzZERjrjC19yBb2kfb3K3MxsLnrvTaPYDPeQupmoW0gthjit2vIpOYcw-i-8Mpd8GRIffHMMU0aTLlS7y3oEglD-AGCd-hmnFx9J1UR_wMNnArqf1-53BoZx8F4lV7REWTZcYXfVshUcrc-KRCRuJckl3eJf3Dsjm_UUZKB22thIYQ5SEO8xcxgzXgnrFizuBy9GVMfEeAwLuN9vBmN55-wdKye4_hbSGRrYrQSJlBVdmOQvt3vt4MVMf4Pjos_cxxHQGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1YWOrHf35jxU7TRkt7TqbH0KeQHQ3GLWGDZJECCYCzrqFkkwmjx2nuas7JIpFy_fldOERTe0M77ivm_wj76kYVsJNmq_ZAm8gZ0nyJ9xkIe3BKKAt1XQ_kbjoIZzq3U8csFBLqWo3zaY2cyZYAnqIwBElLkItUtFlgZI5PSxlzc7CPT8aZDpJ3jplsgQxnPZDteu54FcMoUCcdAKrh_LvpomGmoLQFJ2-vawyDrs-8ZFQxe_LXJndstK8CO58L2yBjlENFA0z9F1nxCpfkpgVa37tKAdM_T9Gp5TBb61JGv4Fm3ZSglKqyjPywJJ5KZ_Oj5Jb73PuRecpZgGj3f3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptsGt-cE6twKv2RcyuwGa9IvQqhZ3hCj9hnJzTA3aXrKyuywxj8jFITkMfm4UWRstrRwkLcjrehAz1t1JRHQlqGrTR5HnD8ZtEbbCdV-qFHuedwR82NlyDLt9pbE6OfgdaG7_nCjv5fLwFw1mt4HGb4DJsb1OCy4iz1clOeVzwEALsG8J4MY21XBwF3dkK541cqkGj8erOVc2uDYuHCneMnzgavuAyiklbQIvEat67YfrvkXy6UmC0CE24kD3ZAcfst7UWuELwWtDUBjf6SIslDYMhXbHjGNKYHE6633iKYVxA42L6deqpRU3PI6Gx4sv9cjH1p6qluntTHSbkZ20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mF7qWnZ7730iVJa-3jIB1CbAQypFcPK-AI8_7afUnuSOhqG77nLiXj96i8lEU0yqjO7ZJkyqTkTBeczAQ2a1w0HyPoWCKzyV-SFTcGlgFmg9FaQV15HGQO3w2pVKLKdjm2As0Nhc3Vtl2C6xYJjQjIya4xZEOEeJtVfd3WHLfoSi7Js1u9ByYrkuSDnDL1WjJIZL7jA6ApvXlCjOoyrHD3r2aupgL4yvFPqIDA6X5CPV2ScnO9_fjWh8Hrfx2DYkIVvoezV23NvEo2Qe1CyVZ0GL_f_CmBo1aR93jznZY-ALlufNxk1ZQ5ytM3M9BY-RJCigEDctiV-YsPk6J4C2bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS271xiZAUUEFTbpSaRzneTQlwOvbq42N6UCnnHOvuaV2Gk1MI0qW8yUk02PL6Qki3A7dH48FETT5EbCVacpU9GrQeKqBcNiYa3_7WwundJx7T8OJMFpu54XKdLw_p2DpyV1WjEb-YB_ybB-N_Og2rQONlEwek8ag4RfS0IcAThZePgSUD8rL5NubJfIbf_HCkxkd0JftVwPPNVJ6NcZMyinv3Wt9FP8h6bTxHEPu-xsdtquz1ir1ysRKWR8dCjQCge4VRjk8eG7iVO_jYbGj1ImMoIS-KHQDLJGA66fFEtHLlDS8WvOOFQdTD0YWTFCYaKWMXMi0jxgMFAHjOfhmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHn2fGjO1PP1c_VeAjXp4Nb2mDori6QjLyp23AdWsnSWHgIS5QGkowU3JZcPO982WkLgwK7O8_9rsFWXr-MmLZeQ1tsoQoqvfd2PPRePwAIAQdxS491THCyke-5T7GqlF8sLsFKIE_gLR-EiYhWcaVn4-qCQPUvz33qy53u2bj7tM0_TNQeT6yv581ojR8JHEX6QuVsqT3DOEFMK_RSe6G7J6SYJvTcpbpxWmy5H9CTD38hscgRbXASVZamAflAwW6L418-DTZJz2neqdKgu4BKYe5RDMKhrU_PjH0hqbOi01l66yi8HPYfrNFDIO31iOk0KZx8EartV8Qu8CnzJJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjbiyi0BrjafCp3HQFD7dhbF77sDOoYYzOJD8o4cgiIqrZwke39KDkbPEhgd_odCUmpWv8MJfmKgEfol5QKu6t7CDCuI3maHYPPgPpuR1jzVjmxXWLCkrM6wFxjhc_o_kNcLgQqmv4GabkD2i6_KLViBjn589qFzzrIWO8flIoI-q7rBbJ5nzbTMmyqOMjLvVUnLOZURdOOlDmRjor8r4wFXI5ssfto8tWzgkBmMzoumYam7LxWoM1FjzL-qTbP-6tSNWV3vP1_mz7HEdio1Jh2Q4s9MoValF1TWJKyLw_8TIuaf4nAermfNt4Ml7n05pCrhLiT997dN4U037Mj22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaSP5QXp8U68X-S5gOkNu9mO9PSkqiZR57e__YnJkCsujQ2gBy-LTldOWVHZ8u9A2UuqmOJxD7AvmrY7xF_YtObxZDeVJ6MGgJH0x8ARrMix1hy9B9XI0VoeqYoE_tcFx11EBbq2LZktV9l_CXr83VdzCYrz3LFF2GFi0t9VW3X38AkmRgdd4YfR4ZoGR99f7zXtCbr83SIofqhfXvYf62Wiwxzx3M--vyljUejkYkkYLSh53EM9QqFG475N7FtjeaFETt6NLGzjyFZFbPjjKFpIlswenbo0X7DeRok9uNaw6oIJ0SdZXP5nFsSz5Bcy56Z1_tx-Tzx3_oQb2Kezuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpvGOpMKBeqhJU5PBfIs3Zjd47m6h7OyZod4AILbpTJQFFMSmjitn9dOCjI28CIXEXP63zSe1lfjtIO3npOhSlbwvwEGoSNT77LGPr4Bzw_vV_OzqbYp-yDRk_TF_O6ExPFSrFjNECPG9MprSvpfsMCnnjbf0w-VCB4YAW57p4mJdDZxCVe_HTKBNDoSaceijvW3U8fqffADGyRAzA4dIO5DBzXZTT_tRYNHefHho400l29-sDiLPmv7xcmuEXRVArypSGpu-6xiqy7FXL1N_HfIKYxw9iNTYweieoNiX3RG9llY8qEUZR8PuNNJpyUt6AJPEPcUlxTNun4B6jBW8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AboYM8SBXnw_iFc8AxMBJca4iA5lLNEiWU4a5TYnNku6e9lGD2DH8siWRhX2XAstaRYGZscxfTUt1RI5WTtXPONAn2ef2i97shtrjPyE_93GlgpFQVOtF-WJjgOLsvPn_Err2tF-9q5lhuEjJCrw2gb0mi9eScOmlOQKPok_5kD0gPxbXT5Uz9V7crfkqPoNtB96q9OSbZCIfABRqWyBZzMRD7odX9mOvqHhd-3EVCYC7BstkLWdsqaGRUdNJ_3IsvYuvG3jbJrxoqqWxLlEWaGr6rqa-CvCus3VhliJ5TVO1l_rzr8wOh9FHA515k4xIyc72aP_mBaHyYAR-Sg97w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2GunBvF1TZCXJedK515l_PXipc6RWQXsi6Z5FlXX9FF2orgnp4XWSeiCW5B2oTaQFqi_tEV-5_tqUT8qhBcLWFlGBJgurY5wdFH9Q0V5WDKTvyWeIHZyOgsvG4S2p9UecEuqIBjgrww8G_WmMl6UTpMkHw2mlSIn8n2HX0IvOQTvfICgZWLhhK9-GLW5Q6jU-zwB6RSVYxfbmWk-OSBrgwreLaTENNi05ouGJpq_H7lSWryhmOhOcnivnjEVEs6VvjkOp-UgIXz9A3TdZXIS_3QqEvymS-E98gIud_y_Qf14rhHgxsQMZ5tNACH9sv4OMFS06dbVgShaO-g3yuY5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unIIOi1n9NdhQX_2-e6zexmoBdXan1RRFV7T6k3GESUNxeXM5T_rAaHHvn2Zv1efT-EKtrcAQEm1K74eaa3cSs4yxs-KZAQol27gE7gp9QhtO__RRu2ej_rXUq2GQdPFkxxz0IGdJs-EM1J61uwbNXGSUt9M4TS2CM_vp5MlOZgr8XnZ0UxI1hS3JAWcKWFonv9hWNGrNLWiORDrA7GHigz6dpyJOSlRvuCDaRg9mwtWqFaPpxk-4hgSeH9YDTa1xKDuaR7PooEV4ENrUZ_076FZuOmUCzW09uDagh6PERZfmQTGgSj-nnuJBOGOSXIstnpsZHruD_a7-SijNXYLew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQ82hKOTE1b-_IptBO4Dkr9lLI2Z5NzRQ7wOFeXtermhdGA6cQyD5KeGcGNfSs_yYoGbnhYrB9CFxtyxty7LvNJDKiK54_fRtdkwZ_VO8l9Wo-VES-9aCw3c-d4veFmvlhwkl_Xejv5WGFZzi4xz_FjOiATUT9K_AzEE71gMO57f8rAXzBiREwYE846a7cobWK2u3aOPQXpZXm3-9lmB8tvSjG4hTlLKIFnEx5XXlEfdQN-Fk9xcaavnrPTmcXNmrkR1j0lR7uLK_LBHjcftkUkSRpQ9vOWckzIUD3DAAkq_0HfJ5obqWDewBSRyNpTeWEY99DYVhd5MmQftJRKgYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvJQ5QNSWPd7G7FBmAe-xGZMxY_tDLeOtCFyX6ZW8-Ft7RQ6wbw5zmtriuassTbeLZV3ZSVZuFEAcPbKlcGOR9fptl6z32idHFdO0A80MAI_Ox-qMzh-MMRYK8veeGKCO1j66gO3c_kL6Uv_cKAOHlL313_cJJKqps1y0o0f50Ct0i98AZzhzrv1SDCwSTDx1jwa-PFs_FSfOwJvwGZN67HlhFPVVGJrJ9pd3_u7OpruiEK9rR29qOk80G0Iq07-E4CPB-miQD910YaaF_RYFZALhf_tS_tItFQbv5K1wFTuRaUViCvdfzDQM5yc_1xI4cBNt62Q8HG1IUAr2vqkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxSYPAQ5utjTWhdNXmSzA1tEFUOUw5M7M0X8Cui-9hFjSCIIKyOLarP1Tx2X7p4iHzmlnnmucP8vlMAeE711x2UuXYDHsbEuDFtbFXRcFVpqmpDYPZ1imDTLT2UnESK9ZF_fZMJ-MoSL6NzFPl94Mml5UtAqY7KWvDdc6KBOtfbQ6Oy8d93bvkDoair3AZmFZxAQZYU8J6EzJD_WVaijAM1yl8Hw2zQezrnQOC7GQyRYxdSnmulxHlaWEyKUoJ8ZgALnJFuIQ_w9p-mdZm_tlz2QHqw7BJxzNn_LWIqj_iuXUTLfKVqJdecS1oIU2mi4THhr0xGs_fGVg-_8cJSxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBu7jm3KS3_EaO1ZepoSSD4PppHTLPY92ZQpp2wDfO9VRz_Nt3yD7L3NXQQ53eeXw_Q27PmvzX04Em0KMPCJkEb2YJO89pw_BAK3j1HjKGxRN4iwligW7PMqkTC3dRzNA4NPsUyyQ7MMqZDw-LLGiqr9faW3y87T1W48NvjUFwB0MID2B2UJQBh3m3apsvOQbkLsNzWsJqKg0Z9gXHXnXm5WPrbt5U9OM60uubKYGGuuB8QNtyiS44EgNrQgLk5xzXRmOEQExiXH-dAocXhzUxxcjigHlGSk1Utz00ReX6kQQf4rN4gTR5yX2v5X36izW0qUsG7ijvBaQNKOTGbdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IO9gMnTcST4C5KHGiVyr6OUwRJekOj3ZEqm2Ls_l74UhIu_Qy-TZzboLr52I2HkgfG0etOH8g8Qtcr1FkmxAiuk1Qob1FAdB28Ms06eKrmUKP3YhT6dvDBzhugJwuZQ6MWlu5xtrEc6egaJOiM2Ha19PoymcbytCJQSuQJU4G6Ckm78X_Qn4SvQ14lY5oUEd8pl9whFVM2S9Np3jdNqteTA2lY-ZEAoGsFguqrcG1jsO-t4e2Y8IcSN7PzeOxXt-IqvWqQR1H6cxUv6_4mbyBzNGADfx-erlDvEYFR9FXZ-xviXbAple089xPCASyvt9xucYEMkw04SBKS1jz6RO6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeOzxUhZs3yuvhh2HsslskRLO1HCYRpW9onaevBsAFEz0Hr3aF-Gv_K8UPOR-LGuD4gk2--qvhoYX-yjH-b611lo915B8hRTrUtyO3vOMk9NDsmypqt0_P5r9yAV7wNSNROAdm9FObnHh_Ym2kVPSohMIzvsoSKyUDmLLOqVn3ieWyAOe7qXiNADDPG6Fv6uabLfrH-XoTZ9HEj4iRwDGCb70qDnLfQYUwvyDuKlye48P-iNd7uO-JFq_dDzcpJOb1XzHGzN_XpOrn32SQDmFjCA3FsudMQvUARjPkAFirlM2Xw-UR2__-1vcesamQjbv9NBeEN6K00vyY7bjnN4cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id381BHsaODzElhHJM1iDl2MiTAmW3SoFERuppFnBIcSwOJUCYGwiVDi-__jrEq2VMT8DmV1bYsIfMJSm6VpoLB9OASpLopUsgO8a2eH5shZUw_iObuCOPXojbwa0Np-shx4WmSA0tNks8tSlak6uT2YSvXURjeRvUcm7XW3tyvEemFnyWWM573b0YOQgEgYT9qTI7CoJmyXrp_aau3rx4zT93agUKv5TkXHGWDeUs5mrtp12buRBDEPOOm3me9Gv6UJkN9Ya-r4Ynmh13enCFXueWERU965qpcsqtDQSmf8IHik0pa8IjO5d8MHt5RbAGvx0HMhysDCLaXucsWfsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFJu1cbvYpoFGsTCdh93IR3SdObqIxjoGCiAQSwduU2q14WyGm5zwLYKyPNKQ15scEYtsrv4oj05eO3ddjb2ucCLJN5xoNhkkS2796PHHMweBPFT035aJpQAun8p_KcWxWbODjKIGnFcUufv-Zv3MYwvzt5QsGdWDLa3XL-t5B869ZgwdFkEt2Gezf_ClLocvpETkCiyWhy0Z5fHFmndV1Bad-6ACTy5ZIZwq6qd5sRE9VDkLwhhhy5yNBwLoSSPnzrY44VyvH3vq1iDs6FjWe9qx3G9ws1hzP1y0SuKMMQS5fc6MTn1EvqVp7uibLn4tdBqnmJCQy5MP7HLqi7_Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6frX3dTHSzoi-IuYd4rlk5nklSzXYX3duLz28NBYdcT5g11VExAAQ1lDmhAnfyEZDyWj1LwgFLxbAcEjSHGEq64wyH3hQ2LZQAs30ioqCP9Y5Nu0O9GbVLZDm_N6dcY7ZaFzrhUPFJoz9VX5jBtxYj7TwwIrvrCwCzj8n2XhCGd4xzkHJqX4v30BBfRntmFbp2n_2DsgpJPlHkF9STcyMq949XDdpos7xQ0r1pWCHGsziFYEU7SSee_kvPOhcL0_nYLI30kjVdAiYQfg4SzrZSA8AZcUbMczhNHXxwsXSsAt8fy_hqtM-tKO3A0noi7iz4zP40O9DZFjQMg6Ng9VQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1-7M3IMqUIlYlWrk_4WAw5PQYgpIoTvHIEs0VGGEEBObauIwqrEpYNafdRm22Lm9vFkLXh3bl0w8rrEXy0hXA3ORD4CkW5LRs5CtT8y3zR2ZZaqGPkr8jiRXOAOz4wKwwawHs2TbSqvEcBEQnwAl5U3DRJ8fB8s9Bhgfi09jZ-oxOESjfH--A6z10uZTkt8BWc5hQqveFFMVbzDgf35A9nKRCpdI0o8VU4fudpBQiBzaHxrrsJKPy_mfEghb0p5PKRrR5S5phGZtOSCVzqxW440M50nSFEi6prFySVywwPilSB_ShsYDiu9-X_90jm_7Q6kIpGq1ANYiTpfoWEAQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1CuEJdYri7TYRNc6-K3FuwafzKhE6WXOCFCW9xUZbtd1DLhd-82QRIENJYLiw55Xx7AHKTvKsKmdS60r21u8VSK-CnzfesBuBvPGdD1HDR-1S5kOHORTqIFYe587z0IdWVKaVbdA_6mDOlx8OEU-pssuJwv489EDbQHWyWeo_HVgW6va44KRknMPpZsWj1jBpgb49vP51m5CXIv21p-u_BWnSXtobwpZ4IyeGcswjU2IzMbg1cW7INsj60i593YiW-IyFfVT4HpH0Ol8ahsy_sL1K6uR22j--xRHcYQh7GcZu_W3Gn4_GBe0AFxWVcax1PgSd5kjZuSVPLdKHHX_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbW5HJKZNRA3_GXvbAzI5n4T0S1dtegCT2c4iKinI82e_dI3BwD0XAUwvI6TFaED6OtHShcWe0L7-Rlz0OrAYW1T-9SFXF9I97gX3CnSTNi5x7xb53c-rW7o8c2G1lhmyQH1x7geBl1PWXYRobEd3P2jSGUaJr11Vxzl0RI7LTvV6ZKKJR9CP8PRyZ39c8wb5UiN3lo_tSay_NQzQPIx8uxkH_oqkB0Y_HR-MGhyrVe9pmU4qLTi9CaiIBx0ssqlVcbCIuvr8vA0eNlCGYOB3sHMp8Mw6Xo9YXLTTkjgnHDyAfWgLh0g3Ypr9USBVa8qiuq-eEcJ7EiOUsQT-W4aFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUfgdN_liLqUfLGb6-pxcM7ShoJgIsTgKhPAoWgZBR9omRaZZXRs2ull-qqqzVZVxHo15N-y4qddsqOhyFzhFoByi4iC8sKhQM7VJ_UTjLysopUB_biqENeMindeXaEK3R33ilYP2oQt96SXFbmAiMrWpJ7wcM9CL6JZYkmLTz2eMdFbnqm2HvBF83fxEOf0suGdEMLtK8AkJZvMwjg_EVCTm7-ZmgTlGWvhNEUnCNu4uXUpnsjp6-ykzEGcXkmcdGp9KXcfInLQ4IQl9UBR77mP8bF1NK6SLtG9Q_ddtXKmMDDCYAzwjXo3vExdGfzmkeBTya2bUoFl14nnEiR-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-zaVBx-ognUmu1orDSrcsWvoSpf95proNo2LkjKzLTlYrEPK5ywU4UwhhH-l_cp7pyq5CFNwCVEl5zWy2Vq6-ndFFziQO92MMQPqdwqjoFefHpfP-V08DV6MCJZwSSw6G6Vp-_zY0w7P9fSsTeoXnR6CMTLQuw0r_H2lIVX6Gm3i8uM4RCW3OGYDK-bKFhgLvr84y9vKjnjnM70h3OGljWN-w58Evq7-swpDmVLwVeOJBwFQopJrOFdCrac60Oj9sKLw5y93BGGMSQ470r2nqz0gwStawjE5xtj9jn3rcPQSQKMvHtlaYrI7K6GeOS5_CmrrMkJCpXfxUYnIAiwNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1-7dvwej5IBDz9UFW-sFPPIedzg_W3rYai0xUZry8tKVR0fHZaYIx7cNha_4lJlt2650ZjjWz1o0Dt-TN8TZUmZIhIRS5IR7W_3zDZq2STfoyTED47-AoL1pQwiXVw-GTTfx18TcKVuXDjnBJDRMFFfpeR63WIztaVweZAR6RAtIw1ZKrhWZ0WAm00NjEM8IpJd0WfJueW8ljZJb2VvYC5Zd3RDEnDih95m0oMauofyVm3xbFwXc4Nr656asB__Xp9h2_fe0gJcyZvDjvdEmNjMjguD4QS69kzgfY_Rt4ZHgXG2cLy5cgpoJ4aUG6tIgWnvCPyWU8Cg_G5HYvN8OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRCXzYyQ3-_ju54D0xM3YYJyTy4MFT9acaR5qsN53whuN9l9wOey4d8WlDi6n8hPI-eX_DU2v2wsiUJOxe-EXCFxFdcUUQSUQ2sXFiThZyZLOpvcjcV1jEyoblH87IVajsh_NJ12ed5zi3Qe5jw-hTFUm9xI9QiW-ozhCD8xQT8_gwExG5PKhPCIwElhGAMRUhrXOcqcncokyU9ssSf7e6klUnHZdfHJCtqJjG7P7aHzFy0JCVhrw7KcH3odg1Xm94x4WgASDeF8DWlfscrZiNEgwEBU_VKRPVAqWuhN1QA8y8tdOiXRrFQrm-odA-EYtckI8k8ug76qT3y8lCyacQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5om90QlbEgbvZzBpmXxNQL5yp4AHpTq0eG3ClI8XyHGwjNJ2of_DcEH02DZShzNx0q-QmZZEEqLgXQWgKD-xmkhFlnRQxX4HgRrT1S6tQcfxntlzk0xz6whJGp-LIDwvcUaN9UOAPNJsHGe8f3FKRtUo32LDVCiqd1GkiF-V5yM8oNe47CSbImAGMSn8inJaE-aQA1SZvuTZErYrTb9FX1tkBPuyrpMAHHQ8eiehnflWsaM8JXI5xsfybq-XhybV4xHoPF8anxb_KXSbZwbIVJdrUgTwtWBuaQso137Vp4pfCZxr1fN_GYS7UdWAPrjNGdlbbIlzH3PgDXSAYcO_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7rhjJqKtINuozEz9LpOKIgs95R-qTh2NzzPkHy7wAh1R4JwgTsrtWreReCYZ83aiEKpqwY-K0yiQzLmZM5nl5xaA-ZL8uTRO0ENTKBaSCEXMKSEtWpli9fNyPJH2XnTTiIj0XISnWz4FAaw4Bz4umBxV8ijO7s5wqI8XiKbQimPuxOIWN362dfcdtx0ZfpIoxppHsuhFVycJqvkRegS4j871_pPbN-ju3AfS2BdcuDo5pFaB0RAKqQlF0X-LRDH6pjERlnR_ZWB-_ZtGCYTUB2O2o8qa6bYKcSnKfbb6GbGEd73nfAmiyzK4ypk2bTI2FzjK3lsXgfTp3DMeBsQvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thiWkW7fmRkDVVMb-rUkr0WJTNB7HdpPGwQ-bEzcNb7IHe4Dc00dCXfFjBXTkmLimDqUJoFcUA0VD9vsYkmPZF_aDyoZinWf0PS-zb2wSOUq3p3JE15fEy_uxdrx-j_E74CAdFuNz9zyMiw_hALjL4YpmBcAVOsnZxD4Tv1g5IlPz1VRelezYQ7aX7rKxEU2ainriYCeV9MdPW4WvH2ePP15hzkmHSSNliLG3fkys4C1Oz2nhIAjXcmPrvtlXMDYzpv39pYcx-65UUKNA6gWYkAYsJrvk6eA_drheClAQekf1LvAU9PzaFCQz7IH1s_f__y3XNvd4R37p5fULMhyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYaKIX8r0aW-3pH_nlIVlIdsRszvclwG4I9hTVgXZStthsP9PoI7cAXAiBonCDLU8SV6gKlQ1HunTU5xePJWYzr-lR5hGtYcGEEjWnfX7nfXDeDUbaKMaqKfBIusrUxjLAR3ttKOHnDoFH99YEYzF4trsWQdMKZRSjX8jIrJKcqrDcFKNNqtKnreJK3imllrdG-fNmuFogI0UE-NibGQ0yi7QltyAEJE2OL-gtfMqC0hZ0sgoYaiNdR7BmflU5dzNaMeJIs8kAFQj4QUX-znyOaq_3FD67Bspr96MJ5AjIu31j-9TomEgpJhst1CL2vSFx9cj1l2cGIN2CTkTf8Djw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LB0jjufvnMPG-zTKm-QEKDn_jEBE1S8ITY7YQWsBVO7BcDvsNXIyu4BNdTk7jRWw45oCPFHE_9OCoIsbzJ2s5Wu_DeykpxThrRqoDd9kCN9K4cagyQgy4xHfDswdqxOXvy-6kVsQliFex3hpWw4xLj4BXZrz0eusU700vfiSTEYoW42ie4oR3SXJy95loIw7au-H9IfRp_7Ox1Fm72lvAxTOQI5SYx_GI6UHixuhvGR-qD0ho0Jq_vshIC0CboOqzyx6C9ee7lizn7DTxPSLbgARdNxqiWYiNzZmlz7IKapnxwJKXshtB2ZuF0c9QgtqiiyRHu493mFBr3ghToyXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MocWjywMZ7eJj4JaBSBEX1p4U6H7dJu7BQtl7r1ABQsGN4mh9i-5SrgzxQN8M8MCOWCpQ54VIVu26hqpWuQi8D5cH9oKbITqoof4QemXU12_s9ZYZFkwnkLs3Hs_KwxIvekofgRLzC3wB6ct5BCabCnnru35QkM1vpOpI3D4T_lRMEgmfOuLNz-uImSUSxwsdbLs_XYwl8XhdnWb-1VSs536bTCGcuEhFZp7O3MAOX_YpEcLhA5cyh-UO5Jdy5I1BgdOn9ZJ5vi_m_cTOK10Q5cmmxdFGo5yT72r16jj4LlHhgtHRZkId22y6eDDdWlwOIQPDcfrQHiuxjaK3raGjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLBVL8q2RHrnu8_iyyfZGF09LWmg91IpUAHO1KfGnwNgeIryhOJxIlLG62HclTwApZwvhUJovTHjJuLhPoUepTtoUFK55Qo0WqPvpwXXhezOu0QvQDUFPW83etv-pS2E_01sTN27tOlJZCVkOqZbeCe5AlTsbmNIpvebQkRjbYT2eSQabZ7NxoqGsxc3jjrQ4ubydUrLs_evOCkngN8htr8OPdor1bTptQiAkP0rKpKE2wTNYbYYUoN9RjQ0wZur7hnQ59WxSnWr_dVEk9w3qAJX4IFkQymngS4X5Yal-Tz0esrhy4spBqgkEjouuigTjtusAc9Jhqi54JHoAx-UCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Je0aicecs-k2qyCRdt3ubgqv41fZzc6OvuO2hHEUGU0iqXtJKYW2PHIfkSRhox7_qPPEfhJHmh6w1laCOPIhL9ngtk8EaaIbF_CEQpqg5G9E3Cxi4BiIyqJZyySz6OgiBEWSk585bvx3Wlhq4dj_KOg1zQW2y0EJGjvkX_UpAIGtmwDhw6yIiY8bCo2xVPvaeDxE4K2xQBOQBdZfCmcot80NvTCr1PGwi2Ecw8lf4ONv9RD5T3IIeHBq2umCQcQLj9qo-9fY2_l59tpflFr7g5-ijKBEj2_QCw9nrr1z8Ykk8Ig7p0kyOoqgk2td0KjWHoSdMBsuPBmSGjrIUbPHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwzKN5Om86hA_TLTXz18GddAbBb4bvEGRYJtB5uKrOZdXN6aA1imk9bVQppWgQk6cG_w5EF1l-4leSGBl4HxYBMzFBhJdysaLtK-Esa6HR7WOVxc74kjre3L7SkAaQ-BRKlVVpI8nbdvhRqXh6SEyPIlzmBu1ffSRPRFWxIh0zmOZcDCo_ezTG1zYNoLRhCGDjSg2ufX-6tDm-YD24dzF12m759iNmyAutMexq9X3gUhIvFQlhGeUK2zCMnbbIj4Kh73DK2gEHg19D-q6GaH8-riAJ0DZ_7kvo0UxNsd8HDfs71P6qrqbs-enAP8i2Nj6bKpzJWJTwM1HcDVAUHdaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2D8HTsv5a5zVnBAMWBrWUnzgN016jy9eRPvqettZyD57E2c8wMs2ORBGAWbr9YMSgyGOr2yP9hiBSQMi7xNXZMkKSWNmSxm65k7cIwPHiIZ8SVGhUTGpRg8SkmRxXCu9ggbSYPjBs0bWTANC0y5qRLiXTJgkVou2OxxROv_K8T_fqKv__s3roHgwBDZ0N6supa_nzD64xFaAf3IfnCWlP9GXd_sgVib8tdbA6_W3u_pRHtSYjRM3aQGvWKOUzfbsYAyycrpI2q3puMT0CAZLHza6v8qipNT5S4D8L3xkvl03e6pWcrQtrKlEAUx_o8e17L3YNtiF3khvL2EtTH5-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTeFltBCpRfouoWMv3bqlRNolr8gxh3xdn_JMg90VZvsGqnPAUmVoSeJIMopBkFWlmdV4DeDiCFaM3W6amVpN7y7QyBwMoYVFLBoCUBluE21AOSN5rsoHw9uqgGFLyfZHCbqRvh5s-zfaZrPkmK9syoXKobHzTSwSdpueY6WB2m3wBdcaCUJBPLMMh-AUBL4I9Tyba3QKlthYTloZNkVrofFzUTFBsr9JQbRQkGUAX6HuW8vx0iqM8NOfTFPKx9CqCZ65b3dD3ix-OOZd4Gi95-gLvam8DeVjlmBW72p6H8Bo0nm6Ax_yI0-3wcnj-4SATDbxKjeQCDxmispgi-Q4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCCQ72zDpE9NSJtA-S6zPFRqgp_ts2jcDymKfkosflaBdl3Qcy6g1kiGO120066KiIKKexwwkwkJc12ema3BeE3ViOA4yd6BucJAw1Hf-AY6qF61KxUWIcVU6v5OrQocxHeO2xQoJosA-auS2c6RgpK9RmcC83Ycv1BEeee7vMGtzqMJLIxgICUDT_gkGbYKiydiDAF6upmDoI69OlFEEinbyoZ-XYckj5FzW6vXNzsQipSHlUDbUMiUAt9fNNkqu0wotn1VqSCFHJq-bVXAwC8XpfG3YC8Nocy-xvHUhOSKL6SyaYlC5Uch1eUHFmYeGtMbIWZZQ6ePET1bB7nGnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZGrkK2bArR5NWh4zjYFYjqHIu2DMH1RKNbbeoGiKkq2S_IThfUYryz_U4R1iBD7CiNUYV78VK0BdFsAl0e2WZP4_nDPp2-m65lgdr72VFnCUWwDrc9ZQDZ_PdNlp7Qgyvmxrz7p2ARb7uByElJ8unokGTrdCoLMafCRay0ij28hk0LyDsD9WezbtiOC911cvFxYhEVwtiFQfMmeectMoxghVEarNpl-9ZNlmuVlKdVMFHuK4G8wCK4JocA4vBKlGYIuZB_1B6BFZFV_1CsPwABhi15YR69KigSZWHSrTHEZm_G_bxWNXSSK_d1bCQe3cYcljBgrBrjqCduKPLVO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SeePmkfzM1lrw3CbSUeDxUIQDdnmJIXXnlaDcqzah2_ngZwwAtFz-UZqi-_beBZwjFvZvT8--MUlUf_VZxWOTOGqsMsjarNc2vnfjPmfreuAwX5Uj-FBa6JFb2Vv9E9CmLfwTaQ2OyNndMl6GfOs7CD3OONM7ywsoIjHK_5Lqab2AuEU3V_dkRtPxn_gY8jaM6P2cdPniDPk6JoJzulj8ZpCpjmSOriV-fFI7BxEnv6DNQHBh1ENFrr81dCOwnfp0gKBBCB9MhjOIzHUA0LTgjSWsCladUSIilLGINMj_O5aT9jaLXyh6JQ605jugExwuesvObzVFrJM3q5y8e_0rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMoyfNp-wfRXRC4gCpFmzR7WNtjrgvRC1JA09aAs4YaGPFmaEO0B55WVF_8mAo2zoeCkpUHiR6UFKwswKRSTRTeEvcgwi8BU1tQDGBIKR0woDHNhXF8y_Y4Mimz5_TfCBF5rJyDUQr8C64lGjo-DU_KUe5iep032ypNctMFxxVaPk_3m2QGyEMJlmravA_QEKry0VMwEwzsM6XiDrFy-HX2DuDJQ-ZhRiHAHYd78L3te9h6YTzS2jxQK3UOOBfRZ_NAeVSPVlUH85XvWhp-GPemaWnYcSyOraLOzxaTlAdoTXml2YZnQsuh9TTJPdvtu9ZCT5u_4v5_Iw8wkjg-X5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bex7-YX2WZqiRTWq1CvYyXBq4_Sj-A2MRaj3krmAPbGrfbYuLHkF53lwqNMmFzPloJcMo9YZV4irxiXEBhskgVoW3uyk2NSINbKqyI-uwjCFq2NyA--o9p5wrWCvODv9bLdmR2XwMTemSzWV3QHPO6SGgeJ7aoLqjH190NUjqNPuxkxTK28Sd2aErBMiVzoZ_VeO37x2gRWycNbpirCd5Uk747HVNU5SYGZZtNfy2DfLSaVAk0n5S4yN5lBZaIm-7yDH3oS3p7IWBJaafTk4weLsx1Bm5dor6H7sQrbZyQJxQyaVAZDbXm9Q23ZONPxFtW7n_tTvyDYp5cdedgjH0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMV1Bz8x_i3VS6sBpQd2hIDN8ZF8Yq1u5Q04BmRVmVL4J3zRYVlme7Uu0yBlmx6EpMzMtQqwBZ3JNjTKY1bz8G8rvMKqtRKa7TOuSY0oLVIQlYkLOIYqxA918T4617XtqXuQ3xGo5RqwfUpDdh92LaG0igN7EU5z1Y785aTQ0REceQ0pioTp-5_R391SxC_3WrREgLK7TdrY1s9uM3y28lB40IGW1a-kmA2uiUNx6-XJADaevhVDfoG6e3cSZGzwFRcn63QYetNixrOYRLg4OQt5UNIwE-5cZzvN541FvcV-wBqavzjxOXi9NCnoj45IDN2n3dd27yYHZlXoS9XBYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDZKH75jEk9exxak-5H1-FVjyl1yThG1VqgC0ZQO1W8KjGszBXK61gFs35XKvGynIKn1BefP3aoQ_ssJIJajrDTWLqlWFhU-G8W3bHhnO4vcGNaJ0Dl_kEFinGqABkJSjWAF48ajnNb1e4ep-VkiFB9EyBJd5Y-0AjbA94Vt_JXtOcKpK3VfvyiuViE1lUiRncFpvX36tQFkCXap95pcW1fJ5WPZDzCjwJunnhha-HFkgYhbG9MFgCAOuPtSsO5p7aQ586FOCo029X7c39r009PZCrWNFfELX4Qp90ZCRXbUnz6zbcP_ascYuaqHNaB1mPnVct9JUbsgVoxONCK5cw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Raeg7eY_0-Tq8k4BVGl_-nHBxHA3PE4koLPG9X4CH9Rq_j283bUR5EFdujkYWfafOTSwd2_k9tbJ5BJSzNDHTRCbrxAvM5zqlyx_f-NfI1YG3Wn2XEpLcDzeMvbY0lRmUGlU87Z4roipbZrAueourw9annF2TuQLcYZebsdcFFcVaigI41gjU-wbQmNmUcvJoTAWZtJiZbt7F8q0mFqq7ljzxl8VFt7y6Y0WOXfZtPaqyN6LjqRb77nyroj4ILvGnoaaIngAsEb3eq5AmWKacl55cq_4JG0jBNekTOQ-S0ocJtUk5wkN7N86naX_pfgj8f_6xjE6kvIxPmi2o-5J9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Raeg7eY_0-Tq8k4BVGl_-nHBxHA3PE4koLPG9X4CH9Rq_j283bUR5EFdujkYWfafOTSwd2_k9tbJ5BJSzNDHTRCbrxAvM5zqlyx_f-NfI1YG3Wn2XEpLcDzeMvbY0lRmUGlU87Z4roipbZrAueourw9annF2TuQLcYZebsdcFFcVaigI41gjU-wbQmNmUcvJoTAWZtJiZbt7F8q0mFqq7ljzxl8VFt7y6Y0WOXfZtPaqyN6LjqRb77nyroj4ILvGnoaaIngAsEb3eq5AmWKacl55cq_4JG0jBNekTOQ-S0ocJtUk5wkN7N86naX_pfgj8f_6xjE6kvIxPmi2o-5J9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YayK7ZxoUaFT0CCKnbNBWbMKNN3B3qMOC_FBPmZwFFjZP1pPy0NZrB93rLK7mPy2eBIhJJv48s4FD81bhIfdd1bUkOLGk8iZOA9OusgAWWfxoreqkjE9_1nD_0j37V_DFNQHR_AZ8wwFPKs7OA3rRjoAIF4QPUQIAo2VMVheaqiRFNXxo8kRrruRkKnVJSVPuPFmb5q5Taf8XXNDCk8RK7HiKFrvSBENsGW7pK8B_AjKxBaKQWPVQlNHJIK648ZNWHK2is1wt057yxaB4DgKNQzIw1BulCLh1M6n622Uzt3FIK0ZWH2mNqCWJOROsb8SOlOSrv5UE2oW_GJP4KWOig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBcoPF_hnRj9oV73iUfYu1HOrD3IrdnKucgHZA_UbW2chn1H-UZqMHfrTPpmcftshf8RXT-Yjhb2SDBlSoqcFgizKfxWIXzWscrXZrHMsNKaKu-laJkHX355qSiyE-izzMcDjJZLlWTaSTVeOsHizSSMGX3UJCHZgV6rbjqwo-XzcTKx-6tTBrOk4U-EHR4U3G16tGDH3J7E2_MI7sAbiSJJmE5T5wUBbHXgFBggw63QBF9-zTTG8HGjZzWNGD5dwliAfqHwdPkcEue9_JTSKT0LqLVli4NtvPryD36Fn6l7jJTazhF1jTNTSMz0K3i1ZNTmGG-sVpSJzQb7V4BZkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMm1p7Uruhb1CkQ5kUapQZNDiV3fftppWOfGtsm5Hn3a6BB0s_XdraAMiBdxxNSGCgnml24Q0EA9CV-q80uO3oteTR0Nwd3u-Y2m91CxnUJyBN3INO7Wyolb8zlr5jlwbEt9mvla4od4q0upAzVsagvhVuLG95nZdNP_neDsw_hJOFmA7ewrZ6_mpeA3chARQU7TWJjHRie_6hpI10oW3tVpKF7trt0d_HaB20fNs6rD6vcM3TpUX9tdYV96X-uAH251-f28pz0WKjHTBc6RsejQEpG0i9JTCrZ55wWgY8GEXCoOYphhkYmYOoFRwne1puEFKBBKIM8CfGouYhNoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwOQDBcohY3LwEdgtsKGXDMyI266CdSp3CZYci-7NShpyT3Da7rdvlDAtk0VlruqvmPpNXuDOpnY7_JbulOJMiPGjCiutsh8JsMmVGLkWBbSwnn_1q5QmOZK1NCmquXVvnYygqL3zuc88b_vq-hmSjR9rLnvyGImK6KZAtvw7_xhCo9HUnMJ0CULBXDOgEYkq2bhgWtUWWe6_GGjDhGFTnGhSvrNHT9vJw4VK4Te8hYjlc0VplGXdSEmqDrWsRrogMVA6SPVX5VMaGLGXiKeAx-81ea9b5ycMs6TjuyqOcRfKnW4R8-VcjSuggqOczu5BQ4mzAT7V8Yc98w2WLl-MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1r-DODnr8uq-TqthyReYtIwI1I6UVLN4UpdZ1zfRAhkfGeMDpIZVEDUbMn74qY6HA3D5r8x56hs21qeDu9CMv7ohlicXrggrZ1VcS1hYX2R2z5t02hFaX4qRWS4KkDERBXY6aJ5vz1AEbEnIz6rO8OeFaBg7XnA1DMyOElsPn3jkgJZFInOhEKFEYgjgduHszi7TNS8PS9UJcVZ_MxgPB9Go8U-Jxmb2yZ6IdaoRNK1na-yzjyNLuVhXmMQ5vhKJKIuR5ciCvRC_Py6oc9P-QJAU85Yy2CL21RJA3a24k8Q8x4TAnWJE2AnpSxbJ8FeMkm-DXuuzikyVRGs1hDMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_2CO6wwHEdZ8hSQ0km9KPzGqtD4nwjlkeNLjT_hFXj2KGNV-pQZydZc3ku3V0KA-cWO9oc_RCUjqcvcVH9YzENgbTp2p-lurxqCaRrBd4D0dmhCCZfos4-EKS0ObPIBe4R2QNIO94PCHKFmj3DI2m2L-ifQSZ4ZhW6uWrHhyrw58BkY2Lti7BPK_H_E30Ah4Htg3GaXKKYEO4_HWQwTd-qJk9qWQEDX1p6XYobQwcj-4hGYjl6vLO9swJHeK2MUZ6igr7f_wRlVyY3voqB1nXco13zUIo4iKpuVtILle9w70IhzRmbHKeOpO5NqtQQexSaOJY5tRXYjpxU5-8FM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkbMhh-VUG8DXCZRTJMhhrVHJmY6B36u9f2QiyWJUJbawl1YSxFUARpYr6ZUUS1rCw7HXTfqmAaauCj2xXE4bnJVys1gBPlCFbR41c1klb3WZz1CGpoyjuoRnMRcr9_aBEdRBAfjMQuI4r6_bbEmY_hdydcnbTw3UxGNfGjU0Tbjw0lMhlMWn5W6HDLvGxD4TTs2gDigiM2RRGZAH9kagb8yy6bxa7ZR1suPgNMnDD_j3QtQJ_oEC8_1pJIySVRjMcyRAdxt9W1o6JeSqtcqvvKld2-9pNRFUqdDYvdMondxBJXWp9Epi29czEwT3wyjZdffGIrFwUYg7FhM3NC3bA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=m6XKdVtGJWAFdmgnjP5ixRNa2nihXPkDYLcK0PRV4pTGpMa6GfFmcN9AoSYTCoskPRtvmDDaZfdYJ12i1BWmLmFz7qu3gYZDDvV62wdsT4IAUW6sQLu_mxgc-9LnDHC-JB4xC_yhnlITfvCXG3NGBhJyI4UtEFcM4NGFLbeBe60wIrw0uZmEFYnr1t7do1f7oYqUKR42ixLic8vuAvyM0W6gJTim5HlPdRpmOvmmMFTS6lzy5BdyDd31j3X197APV-G6lkCzqr4FIPil4Nj5LTtFZ_ddqwfY8V0krB5Fqq9HWGt4ZGo9vLJeBFXncnJzwqZgaKGUOwlWkdfPzrSifp9J25ZsnkEGha7Zi9TI6aEk4ivHKjb9CYpaerRWeN6Yxr0-h6dePV1rSs1xXBzok3EBbtYsg2R6BHoU1vIkcz2LFNCgIqDNWh9dy3VIkvTUbtmxRG5vSEo696xTEyV3tjXMRNhP9hHVwJzX6TY5TEoHT7dRDAiXOk8Kd8RKDpi2LkRRB4bwin-CjzcwmX3xPcLqEcvVFLRscM232cv97M1UHz51yUqobR5KwE7MZdIqAJkStcn76CyKx7BxXOswmcm02afL1DioYYwUyjRf2-FSTjn8f8Hmvt8Rbt0SjtXmyRYSyJJbIcOPtp8jJZ8lP0AWMn0_6NtBouk2eZIJpwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=m6XKdVtGJWAFdmgnjP5ixRNa2nihXPkDYLcK0PRV4pTGpMa6GfFmcN9AoSYTCoskPRtvmDDaZfdYJ12i1BWmLmFz7qu3gYZDDvV62wdsT4IAUW6sQLu_mxgc-9LnDHC-JB4xC_yhnlITfvCXG3NGBhJyI4UtEFcM4NGFLbeBe60wIrw0uZmEFYnr1t7do1f7oYqUKR42ixLic8vuAvyM0W6gJTim5HlPdRpmOvmmMFTS6lzy5BdyDd31j3X197APV-G6lkCzqr4FIPil4Nj5LTtFZ_ddqwfY8V0krB5Fqq9HWGt4ZGo9vLJeBFXncnJzwqZgaKGUOwlWkdfPzrSifp9J25ZsnkEGha7Zi9TI6aEk4ivHKjb9CYpaerRWeN6Yxr0-h6dePV1rSs1xXBzok3EBbtYsg2R6BHoU1vIkcz2LFNCgIqDNWh9dy3VIkvTUbtmxRG5vSEo696xTEyV3tjXMRNhP9hHVwJzX6TY5TEoHT7dRDAiXOk8Kd8RKDpi2LkRRB4bwin-CjzcwmX3xPcLqEcvVFLRscM232cv97M1UHz51yUqobR5KwE7MZdIqAJkStcn76CyKx7BxXOswmcm02afL1DioYYwUyjRf2-FSTjn8f8Hmvt8Rbt0SjtXmyRYSyJJbIcOPtp8jJZ8lP0AWMn0_6NtBouk2eZIJpwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEJw5F0V9h_OhJM98vbsJOyxLa8CGvKS3_rAz0doTtlMFhZ6Pk4wckR_5ojf2HmVCMdo7ANH_eFLynEo8MtaicevoZ_kHzOXGJIgke0A8bjS9O9UTOuhTr_JnhVgewgN2P3hgJB-ixvy2ig6icnoO9sn9Za-kPjnIPCCmZ7O9glTiXaTihXx-1vzfJeIeykD6XHv771XaA3Y3x153hkUA4K7SKOpOS4jo4pHNUbD49zzS74yD5HsJz-qhJHQVkCn8J7g3msUG30m4rzvAUwhc_JxGb3Mnj2gYMnuzZFyP9T14YQBxjn0RKQtwIKrq1nqZZpkmvv42BjDZtM7FrobMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZr6k0czytoxIYICy5mK8GjOE4vbHfQvu0hKKaFMOhSMMny3MKldlUOJy-azyPOAXEt-6kq-QUuGC6WTuGyZRSItRfnvpmn4qItbfgakq591adydTfm6uw2d4H6VtVgFXEWLImG5xwT-5uAtWTbfrYtQVPqxQ46_E6YBNpgMOJUglU2EOL-0RHBZIv9f0HCYs2agvKPfixY9Bzhy83Aw55e2aOaneRf-jIRiN2ohyk_cMSmGhzi7C82qWENcQrvzEGTcDB3_dzE8XtIz0zV6GKzffJAkpKRgXjkQ86oGyjwdBvtZMUlEhJjo3RtSO4WX0lRVVBrQBuMus2B0LmTpYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhn-HY9UJhraSqIq_wSXXG701DuUC0gYIrCiMH-kGu4DDQ4QFRPgxmnUE92rDU5_-YQBBdb5vxt0u5-ARyvwm72dVG5QPpXsyDfsWXvt_fUiM3kYZFZGuT4epw6E7FcoMZL1vDriioxkojeKn1H0vB2FkDagSF9aM2vEnuaXLkuBQHWE7xktVAQNm4epoPmNMy7wyMAMwNDIinbPIzHBbfq9l4M7WnKkpM58KM4QesUFL5u2oXQxHPt-oGL-lJll5phtmiKWNhRolICOQT4xVlyDvBzpxzUhuhwz0w43euB5JyZX91BSBVOUgDrlSqGcnc6QjDeWEUpfavcxOR0i1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQK6vMpT49-uO_xAnZGamHyL6I-MJ0uQ7E5Ot1oS7VE88_QGbA8KYOplWto0XC3ueezSLX3KmYfHdYmvKhfhCARtjXzCWXDyNsQRNa4u071nFvw0FDxsX1QTEQKI7NMl2Wq-twJqUY_DpQ3czbgfEPDjJs1doJ9ohBDxg31hSZc14ite-tdohoL55dY8fR0XVK8GFNi7tZfoKzfmbsc5iKBL9L7ymQBrhFNK6R9zeNe9v_nZQnUCzvdVtcDzyZDq2QBqMVpRM5iX81Wdu42W3J2dL5eidwDJOn5vp-7z4ue6rKVn6VHzB2kGP9PMMrvSaqZ-2bQ6Bv6rYMCLuLSOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAIWDk050UXcf7u3wMjB3gF7Rwh3gQJGyPNVurddW7HmLCYwq4_wk3i9hOeY7ELqEDabiCwr2VMy90IVEV8TLGQB68XuJOUi_xUazl-fHHCtrkVJx8Ib5xzoX4eRVSUiUait0syTGjESA9mkHNmuU_KyuSOVx2NB8oc-kJU09VV64xb1yeTTCQctdo3hsSg2xQtgE54si5_Wc1-IirpIu7pEsD-WumCfrEq-rN3NSNrNlrGp8QWFNj8mrjdjA94NZru_uXSfxGMisJRISU46szX66Jm0du00nbutxgwNT09wHvMFwkkPsQf-pi96YoPg2sA1VK-V5wlby6XlVM7Qeg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TNy9-CIJmb_Zk3UfIVd5UFPzYvXklPcDb41oLpm1ZDw5WdlZu0DUCPtbR3lGlQgerjZY1ruaK2PtXyuw1nOdlpIl5q-g6qxyO0RRZdjsjyjV37U72xtRPCF863TRVUebORWyS_ymH1SWI60wxYczjXdv3aZdWcG5nJxExgKZsEEu6UfbowmD3eICMzYVJ7sWAOw10X6gSJrLmC-gp7ozkrKPwPLgY4jk2eE7ph3n-vmbJAkt1XNAc8wgXhN73YX-ksmppv_vz2_RmGXJ_z28W7qmRjq2D_nBdCPg471QZUy9TbJUFI1L8-Sfr62TE3wFRoWLHkTf_NxqRR1I-nQYBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TNy9-CIJmb_Zk3UfIVd5UFPzYvXklPcDb41oLpm1ZDw5WdlZu0DUCPtbR3lGlQgerjZY1ruaK2PtXyuw1nOdlpIl5q-g6qxyO0RRZdjsjyjV37U72xtRPCF863TRVUebORWyS_ymH1SWI60wxYczjXdv3aZdWcG5nJxExgKZsEEu6UfbowmD3eICMzYVJ7sWAOw10X6gSJrLmC-gp7ozkrKPwPLgY4jk2eE7ph3n-vmbJAkt1XNAc8wgXhN73YX-ksmppv_vz2_RmGXJ_z28W7qmRjq2D_nBdCPg471QZUy9TbJUFI1L8-Sfr62TE3wFRoWLHkTf_NxqRR1I-nQYBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU01p1oINPdrjIxQeEisME_jVwws4LaoPvBxr0Zbp_aIGRL7NGn4qd_y8li7hovDwID1SJRISpB1MjsatS5bC7Dk2qYZsvnxosNyyNy0ZwuO7mrDLgt2YCD_NbkIRmAvPU7vPEs-iU8eIxA95SUGIJHW-Omm_6v6nKeSPghkQQujorgb9_PWNTwMT0MCRHX3LfG8XMp1x78zqC_fUfjxSTgFg6PUXMTtcKxRl7AH3flkrgy5mslYlVwOrHXoFFbtIaQIGXBQcskIt0MBk6DB51iVxy6ThY4wWI6x26Qt1XH-Vpy0l7Z_PVLHUoP_QLbz8PilEuvK4V41wE0HRU9KjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_K6UujZor-X6ZcLxL2jMeWz75WlRy9wBmlrt_6vIq4DJz-gd3fgrqNywyDR5mbnEcYQRB04YxWPeLzqStoLdYeGFfjOPxgfbPNlcS35UMuZ-rWx3Cg-cDgWY2mWwqPrSDiXfcr1Npxuoo2uQtCSKwfPs3fNCVkkx8OxmgbNQiFFbDAslbdHBtLQkzVwkO-jIbN14MnHjR4NXyQA2ROUmrK1pv-4vsb2wz-bo-3Qh15e34A76Un9jMARe8wXNsmQCTD_mP2ZeICo_SPIytHyDd_9tgkamsA-gUGraCdPg2xfKQVf3izg1MDkH92CEjOzYZdfb5JC_tV-PxB6Hnj32w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n78LtP4qicKWGvvREYUSZnesYv8nejrvMu25V3tILEnLcKz_Idco6DanAPe1gJiEtS9S0oz_ezf2xOJ4jnZzb3EgphUg1si79eclKf7qjO6LwGoK2zFUsu7adrlz7frcDEkZExmqJQse9zKhrajaEMffAB5_wwmXzeVGWGhgqQBPwzBiOXxM-WAM7s6JwYiABbeEi1J_I9UEEPwzm__VEjvSdaSXVGv4RdtJLWYCc4i5wdefpH9u7ghH5ugSRyR2pLhvXKYW1GdBxTc8KBY_P6w_1U8U2ojjGJ3XdvppVC-RXySCzIdMBbPPqdT87b1xQhFWw9oMj7R2xWx5LIfvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pllqq1cFkY0WW42q7-iCERBXPzai1hwY_ujual3qpqiesJjRnWgyPSW0DBRU17vBz8ivTq5D8CCU_dxHfz-dzoGHjv8ZVmiGEUS-RYq-6IfqA7_Jw-TAOWUs1ImxHkw5_GdNvJVZFtvgZdW_CSVrcvEjQoSZy-w5es2ZHuDtCo2aWIHVjf0poFcjJD0bmekPC3gjTj7UmiF45aItvQ1wmGeqh8UVf-apaJx2tB8OpGDZMX_emRlD0YasQPPDfO19CpBZlmFOZ3JbzOUr73q-KXEFXTLFAK4r3G5VBPEi4W8Rwr--LnEg-JNryINIa8iy4gvW_q0ADWS7ia1dRl_h5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQ27uJvxw2310bUdo3QLUOUTYGsxAdspVQV4HnYY4CICzxM2RWh1RvPxlvUAKIQU8zYFThJgXz_ovvWXMWUDA_7GaCVNiVtZLBEPkaqSHzCmzZAHvwIaeM0eJz7BgoRVbZtNIDfgN13elwE2_eH08B11FV9e2vyYClcVok_G99nsoZ4UKs2UfawjXlO9FM6lmIFdo9bNlDKPEJRIHMxp_tsayzDCNSYpR2PvnrFYcair7PDqUKmGN-lQtgoXe2zKVMS86Gi30ISn-WSQdupOoM-3LWeULk41Q7L9u2mD_-TwROeCyUYjIut29lRpCAvJ5YXQstc9QeF5beQSwKIWsg.jpg" alt="photo" loading="lazy"/></div>
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
