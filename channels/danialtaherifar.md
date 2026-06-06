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
<img src="https://cdn4.telesco.pe/file/UxDMI8RQJ9gBWKWgoshMIYLvMUuwBzxvlqRMAyM9A3f0cWNgV_qSq8o5HLRXTCz-d29fa5-BEHJ2E0gruZz_QMDkVhLvedidL6ZdxdNG8xdgVKniEhdh45H8BpEsYXA4mAJchZ2P0rPkldjr4PG5BA3YUXoAdDkiqi5p3AQsjD2RF03rhzTKx5hDj6eEScNix4aKtuqsoZlxsA--O2rRpyuMlWObei-0s_s7LvtXQoyo85wtB9o3ZABDnYrWoXYwr7Ngx-4eFgpRtfVTQYPt9AsXhYoEQOIOhDtQk2r0HYS_k4lGqbcx43jMaXf7tbdJ0UfWNa83HIH21ERtCxP6DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 14:32:04</div>
<hr>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=UjFlNbyEt_x5DLWc8pucerIDjdgMmXKrAwRKxc_ZqGJ55nLGakxGf9xmD_XDsqVoXdLSEQozmY7lFuCH1rZjs1IdyBKULUUmePPqL6h8EstpKd1ZBC7M0zNIDZWkIIfD6wCJSIentyKruNhu9BrL8d9s_ueeBdU8P_ViB6b-7UoDM3qs3UE_p9GIxO9_80Uj_nB5pVkdxB2qLSoWHkzsbY07yl3W5zzBbCh57LQW2mNn2JqJWIx5q1x9nYOwKSLvQqUk4njD6tDBzeS-TBbURsEMaMJjuWQjvuE3NLD4EVDv4QfFPUkmpujgoMLqruP65cyxvXHPnbBlsoaZhxG92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=UjFlNbyEt_x5DLWc8pucerIDjdgMmXKrAwRKxc_ZqGJ55nLGakxGf9xmD_XDsqVoXdLSEQozmY7lFuCH1rZjs1IdyBKULUUmePPqL6h8EstpKd1ZBC7M0zNIDZWkIIfD6wCJSIentyKruNhu9BrL8d9s_ueeBdU8P_ViB6b-7UoDM3qs3UE_p9GIxO9_80Uj_nB5pVkdxB2qLSoWHkzsbY07yl3W5zzBbCh57LQW2mNn2JqJWIx5q1x9nYOwKSLvQqUk4njD6tDBzeS-TBbURsEMaMJjuWQjvuE3NLD4EVDv4QfFPUkmpujgoMLqruP65cyxvXHPnbBlsoaZhxG92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 62 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNRQZ2wcmWxb8Xmrx37BD2srfke6upfE8JCk0CLzTudVDwAay6bfTlCHutFSdluqiy7uc83rbvhVX-3ggNPZb0gKOyyLa0bCn3BPLfpF-TqPqKW8UNXv4_KG21Kgda8BsTGomh6eyA-qs5GaKf8H93783HA9pxYF0hcziWN97in6lyVgOtZDQQo6Fl7AS6Q5WOp6rBj55RXYpMK4VStXAZDUnAQNHz-qaPY3hasBbsPnDoCK3-LC4-W9I1Z4x8CB7ntSVs7F_m70HrHORN2SMWL5sM4YQ9A4V8nsLUdbl1peM-wGDDzDZHBvsnvGLHtEveGAmpJdB9qCXcYSQ9Yblw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 278 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 507 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 631 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiyacRXJ5VxPYJ0ZFOdvXrt4kFDAl3mc6dUMg7Qb9lh6fMZLV8WUwtLhkC_iN6rGBqNHLWG_HTHGoZOGgfGjJ9Tc1_N9saR1Pw4FKQzdejyZ1dv6s4A3bwqTwDlyBZqzwc3ZMD4asqtWbzJw7GFoMfLl7J6DV9EP0prIPkLYcuuc7Ojn2Eeu_oVEWBgvTq_HvGB38n74ZbZCg3ZJCosk22hclOBBbbe2TG88lvBzs-GEsAXEQt-Gf2ODa0yCKuvl_ieuDBAjvHinzuXRUSSInibfZgfHuVnn4IjX2hoclA6GwgUNFGfhNxrAD6x_IywP5f9yLoTZlby_FmTvpgaOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7AyeVFTSqUn0Tegy_PRqsgBtIVktsXY33G6hhObGP_gIQofCQqZ2tGHsaL2qKIouoXWkmyUc79Ey_-lXg8flGupuXGOevqdYt8d0-teFUn5FJ11sMJ4RjpeaSbon5n4-CDuw34144YpHuVl7BxDTyuAnhae6Bh-yKMAB3-Ldv6W8Livz-mdlhqQtlek-CxFfX_t0SACxSLkLh5DFlrJywpTiIy22W77qt9NeemkoJ5uhcRhAHY_1XhgBFKM6Wgxyn56-w9sXygx4mG1WRTVesJf7-pu0_EFPvhoTsCUuC1rcmFwzI3KpNW62MqVVYQVMvm4okbIEqSq-Lq-f-AWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULRRrpH-9qV3Tuicknb9OdtYok5CWTn6wEqnSRZ-47_YkxhdpizCo3jd-WGFaXbbimFidtMqRNhsfuYLv-yisdtycp7Sh9h84jgHtlK8IRqUyvDXILwnpdOM-L296azlKmm_kqIw4JGsaoBfoNfgBJDYV4EbjLwBIdfqXAZLsTpTru3-ZM5vhP2sKNPdJPt-oGlcUGZBSJHkgxY2_SV8KJJl9qwslku1OG2laJet8mcHbF0wxAx6UKX0AQBldDcUgXga7hwapz1UxETSNwKVmpVVLGX4nXh83PqdBSzENV6ItxfY6iwCxPmaU4DAWtVeHZSWcISPIs6fdYm0pEwBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heNoS9oaYzphvrdDiYbV4hxUySzGvI_soESOZsOUqzwBw8wM7JgBo2y7YdlDd7HzEGFQitdSveEXJ3aAPebnBU8W85vH5xCm2rvlepNP_eBqmu57Yucgu0opE8lCv_QuuPoa0MA2UShnjo8i9GkCwSUOfS5bIMqBshKbFXj9weU7y1UJ4WOn8YIOBn90r5JBmj3zw7QeSv2PFjUmsb-wxZKcvvKKI8V5RYGZEKCxBc794rCzq0XMM9nyCJ2sH2iC6qqj_pDt_SasECMnHdowKX2amG3_lVgC6PPUFo-nv5KpAbo6iGpatigK2YAgtT6gCRA4Hs-sO3VOGAJVpLOfnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE5eY-CheYiVLUdpkXCo2nczCNzWr519IRtsi_W9X8d4U-9r_IGxxIX2jpKWnP8QTMyeN37LQZcG9LCiea4_oxqqkSjnZvzDRFbLDdARRf27NxC3r9MFepi8iCIO6DW7sAQy24AQ1qywrvwoP2k6VhZG86KWmLz5R26GH-tfAFUSYa0VezdRsgEZLtFY1vMFx2SOtSpN-q5V2jJ9HT3h0mIWP2-X8qyIGcux3smE3tPqhumrlMnsRSpicEMAJj2jYIJ5czIU76VcBRQM9v6Oo7BDC8JKZY2Pp3h5YyOw0Bk4um2vRWozBj_aWrrquNoX4mpEnw02GVJRGnzgBCGEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 846 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLv6_7MrtGMAox8vbCDmXzaUZPuiRweXx7m_WvowG5gtPQH_I2F3F50zZqWIhPlWin9chh0sfTHwwViDUdhqn53I6fwUr2s3NekxaznJWB4KhB_KP2x3aIbp-N4KYBroqeA7ZnxqqdTzWKxh6FFpEhPLnI_CeOPJVfHrZ6k87Xi1kUrCmSwSGxIbUt9vAydBqit0EzE4tO55fB_ontTB_G3NxuAWNW_SaPytiXYS-lY8zUfBXk1S2hosbiWNsYi6IOB8U0ke7ZYL2ABC6BvBArhmqavHKyEUSqXPGRKUZQ2OLRVaLC7bI-N2InUmzAa5q9GYY3bup-SkfueglRgkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eILunT7ganW-fRukhHJXSPqigqidg6d-LSzCET3TVr_87-qfCg8l6M5Ahly7ESY_k3pwf38KD2kb6oJsn8ASxQSyCacxFVtHycIf2Bws6Jof0_ntpd-2s6uXIiQkJ1ai6TGkUf3oc9bVN7weoS55Jsmmu6pHan5wuWobRHxj25BIEnj0-p8fzWXaaKidMeLwDYH_d9aY8PVJmjwVLlibyhbgeoNrgcY7JSneZuAGe_7tN2TfdqFZMWvL4idBbsl-Edc9KluEN92RyVqzx6bhkjGgi4qpVSvTzT8ZKFZVk_OzjQXMFCh5jCct6KyUo7EYPlPJdAM6k6PfHaIzT6EZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M45zU3HAZ7qGWcpKW6LudVtHW7XVJ6oFdi7fOXXiYZw_k9grieopeMSEQ4aFBpJ7FsscpQjlFMZZSR1PWyn_7QzfSGA_HwkIevZQi3jrffZ8xl0CZjpwoThUlhdhxaV63-wmHyGoICG7ZWL1IvHq0TFLiwBnqsUJfus3TCwNB_9CCZtZRZyPiz15seCOxHbHTUDRCPFdBzi6-kZKDru-qYDSoovB-7cs0kdcoQj3pXB-HH2D-P8Jl4wFK9mMEr5VB_o3jYnR_MhJL2aG8Q6WhGDg30NtALxu49O2DPjrPD7Xv-S-TvqeCFJBlC6Bm6cVByuPQZy-YjpRElj_FHv5iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDsvQ_Sj9XcwcBSStIYIWLMAcTCnOQjC_nKN68FGwVzINq8kHMgOuKGZoZmE0tCsTbn5vVLMyN3gVAf7PoYhhxqzOPq1XGlJoc_wjslY7EP05_D96Ktihd_R2WAxMTjKQZfvOoNFRxqv4DSXe5fsVatMu8pmGmbyqGALHh5jHoY56g54k5wXpFcrrcHbl889nAqMV9Ytcn9ND4v2LnO8HbwyI4OKOUMIm3sfB2CpT3lq1UPTA9HM0wjK74KFJlW9KopOO6v6UxMeiaVJQ5f2dlNqZ1VCMYK_zz6KAHx3-C1H58c7zgHcCEtGmiPYpz5_l4_q5rKjDgcFEcScKPBY7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 941 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0OzrhahqW1uK6SGoMMM-xRVJXSfP4d7NGxlM4AVeEASBoZGEwwgP_607V9XuWnaSEdowUZEbee7YaxeWv9v4-XJ6LFIJ2gw5oCkLxcoXJRdibWrk9Fc1IMUGLr8pk6hVMhCqyfftVHZuyzDGBBoBnoPUaL8Cvt5rSeJy1iF7rhz_2uo264rIOha8JwSc8HOXn9XY3v4Fz6JKu4st5gCnfUVFCx9sVoziK9Nxk0buuGb_Mp4Rz2IzoyvRKAkY3U0y9X-YCqkPgRbFe5RSNHA9Ljm-BFT_sMdEpgydN_4w-AHNP0UFJuTEThaz906Avq9FrwVhDw-lx8EdGhvqNbKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDBT9HmY4C8-nUmkypfM_BTx2iA8_Vgp_b1J3OisTgfuFEZ4QMt3mcAN184xs2QMBYaG2W8QT4fhMtK90cYprl-flBJmJJik_GxorvRmVtWzrCVDJNDfXwjhuXxkuQq8dC_ZiDcdevILkX__JAjIGyXOw-gPmOI3Ul0kOEZAjokMHpeNrjPyTBNrEnuTQzgbSlv2dfaw9rxHO1ILlsfZ6eXPaaw9UbxH6Ikw7Zq_snSonPYuEWqg7YzMWuz1I8MGecQ1nqspqP6p91eJ6FMWRGB0KsWqHRCKSPMtH3BEjN2I_oNvhM0gFzBLQrgOKsYbpiHAzTxZo4dGkBtfZWsMtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 676 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9R_HNCd_x5pTBVt2MmZQDD_smZ8O2izEXYZ4nadKekG6ENKNQsjPG7g1jybyOurgmGxw647kGuqv0LUELtHGvGRgpNEh3mElk8Gy7hkyihwGXA7KDTHDccXdFi__rJbTpzMVR44_VV2_wRgnvXy6qzrq_WT3dB5ojcCZRQbo3gb4DcLAoEeh3BjKwd6FguSfJVJd745LuyLXk8MtmO2MVQfzc1lyhdeB8wHkUPMgnVwKEDMiS9dd1N_jO4NRpEWxRsxS47T8IQsJwFKhECvZDKkdKHPZ2_TDVV74zKGzU72ORuzceC86GCELXNdhvmgi2knA5L9qNd33Um7QyDdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXmQq_Pm6DQu9VUYcChErXtadoeoDQ_t0quJ_Vs0ix80MpO9OwQrRSZcUqhECTpqBpmTYyjAWkAfFqYcxtBOk6RKPlYxf1mjcVFmP5VdP0pXVlsRgjubSYZX3viib_YzjpbjbmnR9VrboYdttn-MjBMHhll4fBrftiYNAIiNO4HXfXAe8CqsRBgMIhahoQxqLn5o4q1cMs2A41LE-vtKzM5nTsNcdCzXwD9tX7vMysLz1hHQdKVfK6T_kF4PHkLrcUezZMMHPm349a-EaaI-hruIIIB1_fHoE6qdx-KrjV0YIUEdb0U1kw73tJbtU8vRNPxv6bATRLxhF8cmIEwXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJJmISAsNN_D09NcbGfFxeZdrimUm8deRUn4Z1cvfWSVv8CAg36f5iLdKJjmauOfz28YIbrsGPoxH-H7PFad9ZFkRLevNiuKl9Ngx8YaQsWsL3WbFOpULvGqalT0GTvbQjmS3crT_9AbZ_K7p5HmAAcHRqjecGPo51QClsbouwS1MlrTxxfI_GcD3EzfUJdxsdzY6DNKBmpuNsUhRWrRZwy0zhKnQRB9yywXuUnwpG8ebHUfARZlvXuvwnsgLkr3bIPOZkwbjeWOvNz0VzZTCGvD2myNPjxoJLpoQB2pZiQfXue-0t2qyAsvgBJTK6PcmqTwBLsCq7i4bZvF6f0Z5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_yHQufs28BUCAycubDvYVMy6T5EVX5Whdj7bJY6bXgotGB7YuLlWshDrTrhnfMB6dv7GzYDmhQdWHTfchDC_VaNKEtkbduJCuVgSatO6yydlSg7Di2Qyf8uSaDFAs9NUoqZuUHJ9THkaEb2XgUJAufQSX-gvbSRC1AQVUD0gJsOtCShIApwTSzciqi5IGW2fKObUVEeltFevk7A-uoi2CpLzsKoSl3BI9yMnYtSsYfYVuXTwQXVp8cwX86TzzJvJtgtoSBwhRNv4XnNqkAbAUZJjKROdo-HLYmjYrvPMDc35SxWcPJf_b7m9Y0glnr1J_yZGJgPqXMTZEoo_C0-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEPCyXxT5FR-mQC1AJUZ0Hg6ZGLU8VgOiA9xn9I2BOnyVFxxckSMpiI3LdieRGYxeHbIefEFzraJc5HPCLva9rFsFE8RKbVH7fPlkSzPK8-XJDIurOqaf_2qRPuc_j-E-mG0wHj2r9eW-V6xMr9O7IqSi6_nLO_UcFLpWTN6yXaro-QCwKPm8ab91y8DM-KmIiac3Ud71ERGs_3uQcioXlPs4A4zla5cqbTiQI5g3nHUTRiY5zmpr5McMvctfO7xaqG1rt5F8R1HWMYKtyHQR7z0bN9AxwUgQHASSzvkN6kkS5Uq4ZtQhwpYox-p2Y6n6XnroYm02QHBQLhtwgA0Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmGIY8ma4HOT7kiQMAmFvmUwvs7-wIUxhaB-Gssa4gW0imYjFk-KcUf__BjCCYKIDJdIN3bqTruNDPnrQluVxEre3A_5eAXuzAo12bul-E6k8N6nbV8imDGTE0enRfQ-1owhq9pJUjY1VwcCRSpnHjrgpkMmutEmZR8iRnhr4060SPciedoYPtT84kHDBd4Bi7aBKmngh6h9HvDhZETErldmBjUQIjDrV2ssmbDsf1aivdkvD9fcM3Y7dWx9hMJv-i2FukXbB-t-G-Jw_KeWRlyNlFSxgPWEorYDt7_k831iGza1D7QpwmTzn_jb50EMMLnOkoEkRsgbzVI4em5suQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=qDB-8E0M4aOi5dfX2qUerxB5kGlzjwsNp_6johC0xiBK7SiUTN1YMOSbHi5mFIqyvMs2BmuSYTNUd4gX5Y8oCwJjMmwi5HLodacI23te7dZdSGvZsAPeCKkZeGjCkvDt6Js-PBaPCsvQFYtza2fUuOFY8oguZFwOwPf6kv-ZbW4tK8mW68w8FFViGxoVSGfreIijI6Iz6AfHaUR7p9_LoqDLje5KBeNKymTwkMuZ8u41Q8qeM8tPeQVhoY10BG9-MP7ULZUXbTC8ZMGFqNifsMtj0JI-gKA9gFEcqsJn8D45eM-HrM-VNbPyhRxQTht98KNn4bjTu-T3nIPqmhdb3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=qDB-8E0M4aOi5dfX2qUerxB5kGlzjwsNp_6johC0xiBK7SiUTN1YMOSbHi5mFIqyvMs2BmuSYTNUd4gX5Y8oCwJjMmwi5HLodacI23te7dZdSGvZsAPeCKkZeGjCkvDt6Js-PBaPCsvQFYtza2fUuOFY8oguZFwOwPf6kv-ZbW4tK8mW68w8FFViGxoVSGfreIijI6Iz6AfHaUR7p9_LoqDLje5KBeNKymTwkMuZ8u41Q8qeM8tPeQVhoY10BG9-MP7ULZUXbTC8ZMGFqNifsMtj0JI-gKA9gFEcqsJn8D45eM-HrM-VNbPyhRxQTht98KNn4bjTu-T3nIPqmhdb3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNKs1az6NhlqGPpC0m8nHMV5z4v7lfvnj0W6ZxmbxiIMrcxunyWqhJRCmUgHQKy4ZpCUgBM3FSg9T0_Cy0fn7iqH2menfFS482x07bCFjYxELopACiNq7qcrvb_P6dar7OpvrURurneqTMIUXZZUxu6DN4TOMvt_okkPprETKLZTm85El2htPUo1lLG5tzcPEmz9Ho2OL_95iuU8QVk0IkOov3PCRztGgcCZzhW7aIEKGbbnV95ZoU-23959tjqhswCvunjM8UQoNhTqBVl-awvWUyKzlSekoEy5jHo5gXOW_s1yljsJMLeUxGqiqE24VZSqA_QcOLhGnsZYH1dtpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiP_UqUh_t7LRPDVw9Gdefjsq5CE9_7FqGas_XBC3Q7StnBvlusH1ITVsMY5lOvFjft32PjJFdRBmowBKw94mZ1zBVcZ1C132j2MrWOXhs8TfaHZOwpRk1_GTCDjotitApNEO_KaOLhZRLJ27JW-fHwM0Zuu0zqRRzWPIBzpYuLIfOgRL0Ed5VWGbh3L96HI4N9MStrM0Co7p1CgtR54f_VCA5-tplHUTqPEkm6Icwjv3SLcRpoZZE2uYzOCkysQ9uXSbUqyK-S5wN6U_kc6Gs9LazM3PQHIbkHAtNp-9l28JLt-GOd9oeuqThgjoCbEJHw-ajVGHXf0TBajmNm-pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-48vws5-sLW2tSlJxRnmpBvsI-PfWqGu7Sd0T4n4MIVNPw6qbMq_Dh4wJKiqR2G1HVIGFqYoYXkwb4xh1logy9PXb05v3eHD6AB_TeQNcYafLJYnndbLrsVqUJjp-KmrStiwMzcZDaahTwaZQyltHg8TJd-LqVFxZ8F0UJdDDKxDaq-ysX0lJO508qlRemxuqlEN7Ya9nb6VDqXR1XIwYQJJz8X37a9KNrQSWD5Sn1h8GUMo-lT-H9XllKWhvmU1lJV5iPJdf_a9dozOun2SaKSUw_ZbVsD81ysI-5ZoObf0XWpBfeNs-8n2cxRcwM8aJ32jOfvzI2Ja9fvhzwhcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nV1mcyyskaWjesbAb6HJag5XVZoTPoZmaAOAOm9QhgsUFDClKbJkPP4JfiaQaGNGf1E8wyA5aBMowPSA4QHYng2eCkEbXZxkbp_Kfd3pfL1qL4lEL6Za6rfieGiYcn2Gp379zPwaFB7SkL0Lu8mdFixEFKfyDp3ay80T98_3CMhKd0KZyaMAmJwcdOSumMXDZVsYjAFsma5b5-anozl32dhbD_S8TlDjkZ3raI6hewFy1jG7vHfbFF04Vjg6CDLNvTjps-WdQZPfglTtuBz0-_VUvyvbqIhKvC8K7IAPIOarbn616eqBq_7nW9WOgaz28ALsY3XATSboibpnJ8_gwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 983 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqPCimEjQgaHk9FJ6r_RMuace7kVDJ51tZDypzaZWNIT-QYM103kkdWHxvy2SNk0CyZZhaft5UcbNn74MJhq_MGaMyEb85YYRJUQaYW9qCbE2l9PwsGUHe39zNMWFFW3eWpmDxkrl6Cf0-X_o_Z2sdGI92gMvqXlFNHKqrXaGXLKgsjGMtGOdMwDFksDrV9TVCk92VffcoQV8lY44V_vcw657YjOWnlzEbi2Hj-6BvDq9gdMQnT6k-pOgYJ6nuz_fv5_u6O-H0K8-UssZYtZdKM15tGxm33tawajQmJaQZa8sY__AWoduL-QVVmnEA9L110ws5IOYC8LEjm3q1QClA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NM5CPq82vcTPT60N-haMttBqSk-ItddjQUR4CMwryf1ntadoopBrI4CTOPk2MswoxjXTmrBPfisnlwlQr9I9mk-1R0JbnuMfqvk_6hgrovTKORUBdqukIsKI35sRU9kgLZzs5eli7I0n63YUq_UUhgrvPsVjetMpJk1Ls1QY2Uxbu-4NLWECesTv98WZDzustwlygdHuAbfASaTd-oWNkb3FCYUPsKJelpneQLJidbTfqIKuLPil7_IOx9-BIBmYtVmgjQq29_C8OZ0Qzdm2BBwSRJIpi7aHocoX7Ac7K2ONoWCQjIutL0MUU_nbpxU1vgdj5LOkrIHbvFk7LpOPkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWleNhyZRabqEZsaTb5iQ3g4Gv0Xp76PGuvAaE3RJLHpwMBOPkRxO6KHTUgDdrC5hEKaK9xxgP9FY6VMh6TTvE8ipXo7saMZjG9jI8UM3b06vijvh0Kj6UtnrmqT9ocv_wqYVOrnvf9mFBOcF9e9BywXXSDVOMPxWUi8Fp5RSrkb5-9BmyiMN-YhrHndM_e2P92VeNi_9TYtNs-VXBi5THYE5lJ0AV_VHXOHN2lyHCB-M3KHrJ_ZjVZE1u5V_71aMIHPY0P5jlMYnne9yu3439aNvO3R6aVGsfCTKYWocM7Qyom0FN4C7gzmmhYeADlcPV9kHFIXKaW8TZ6BLfCX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkVIJhWmq-MPNUkItXYigOFQu3xmuShc6Wn-m2nFTZ-fjcmDIXxLwQAKLUV8qBYmMPR_dIWiIsfp7LhRuYVL9dyfTYC7JXNusOLdKpthsmOdxZwDjKC9LqjjUkrq04G0YQdNKW8APJcvPbqjn-7us1zm23HCadfsm1bmowLVpf0uvw9mjN8vUF0ecMYsRxiua6iMZyXVH3fvuGiSFXjkLOFpDrtyRbKssNqO7XbkKl7f1S2jC-uUCXw_jwSONxByMyvRLQSdNPIqKfYtFgkL0M-cv6q2cGY9IaKltwBHJvCzmvOyOTls62iU_h2XCWUqwvzzoWJQzEwwTdA5EBtE8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JusCK6-2r9s0guyEp9go-vR7ukU_0WmCMG68kbbLMs1m-YZnN7uK_TzSetkHQkZYzBOvMfvGgGN_edcO5SdKc0kBJgLuw-pmFUIvgfS6SrvHPip2Vr0z0p9Nl3RdHloXmPgJiTD5bx0zkQi-0eFOd44SBpYq0PCPe7mVl61xd8Bz0Eik-7JCMQr_NtfRCNyffMGct6YTt9b0N0WEWlumtgB4Ba3tLdU1MotP8b6WlaoNOG_xfQ9dcB4PUFPQG0DUTvp5XWO9iWdbr_OH19fDpdubVWfrEbi-pYCNB6I8LGf2eSWYK0IaPAwiOAgQWKEDX7qtSAzKmvCysi6Xm13I1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GinPrnKuaeQSl6PYlcgT0VxSWzW9ExgjK49zHfIdZvzVoXB9iU6HW-fS6UuqeDXXSU-a2gO2Q1da0AT8A61HBN3-1AwuAchmDxa-FtDZU-nESqeFjMs8WAa1Vb0R099I-PnJG5gQm8YusfKYbsx-eJCOtgJKgBgnCdA2x-Wv4B8GeiqP9sp3MIRMTmv5jwJlksEGNp4aXM40AZ7QqunIRQofxnQqGYSWRH2iBrCHgo84-G4y6C4_rz5oSkyrIX5SZ17vl30dYFmyXLlACfaQrOyuEytl88S_rLDtNqxZy4X1w-H0slGALRFVqEofeyenBPMvoVaqcuCpViS5zjINug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8ATE5an215Bfa7e2JiwioN668iXCs_r1oEVOAt8sAmpygTVT7hWNLL3jGmdZksN-2e2NQR9aE0cNo2ox-rOTdOahI7CQnEKNok7Xa2Y5qtBmaqbrPMChkqJ_83Aj8nlBqczLJ_3QxRvq7MyUWBZsezpEZZaHI2RMfT1xEG0nXl-mqJ0acwrVgPEFnGYmXOO6UBLpnlyxtBzD_W35vRX6SXshu5R3R6f8wMwWw9OCh_RQTtfBP4lMkFPLqVh0hjb9Q5NrmHu_kZSRmkyrKsY6c6lw6ZZfTM0E2NVdZjpojLa0x59q970qOV4ykgaerc45T1AiTJvt6oEJ29_toI6Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdqFhUIza3D8aiGEucXXZYI2-ZtwWQjcdoEJEzfdhz4fc0OGvAbawCWufTPSVghZmla4aEMp_gM-I5ECdnohWAmlBrd29GFWHV-GHvpl_7vBMF67_VFiH-hQUsAKXgWH4jhzxZ2-8t1hBN2H3mguxO1oTw2dI0Ad_kXDy9LjXLSxPI4Jka_SmgDU3H-bB86jrzEHzWzW2JMOBzHgaMYbUTyn9x46ES_lg3FQFgnEUJo7x35ti0dZfdVStgnXi6cXyvzQUzqq9xE6VOHNn3glf_vK-U3DjfZM9uxbLstoOKE2xABc3npEW8ntLsJfyUHveBEJDxEfvEzVwwwa4OrVuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgPwQOmuh-8DXhhDF-NiIOGccalQFpu0sim5No_Vb4cM3bIQVnJIQrEDVagfyLqeV44DGyVFB-m3wTluAZ4rCCVYFgWJtHyqCwhlWlJ7j3P00-h61QTWQvOuQVbAgWn_9Dk4GdvA2aE7rzYrpMTVxKPKHFHj5i96oqAjColC1va3yIMs70l7opbOWCT6TKbP_eyMD2Rp9BcpBPAYPZhZzXtnTAU5yvQ_XnlFzW3AV2heCiHJsbWugrzBaVQeL-IOW3XqRkE3i01YKfbX4sfdJ2qkxPKlWJ-nnghINkQ9sJwEEjUyItD0nDL-ogdb0lAoqOxq267xLFZB7l0u2UWf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZ-38aT3H7gGX1wbUlG_CASfVFhRKHEtw2OEpcEYt1YARiyBv_6Ghw2RuyNK92YVDAdbX6z-tSl6zA58fWlpuRQLV4Hv-cPGCzZgxUi_rh1No1ukdhxA5IP2uj8m_WODRmdpVj_FN5X9XrjuNQZ2MuA94sDuzymfykLuyEbvmDebtJd50wKc4-EhBvTYlJIF73tTwLi6gUccFgfBKIvISPhpj-6BHELjM50xJ_XaRgNAgZfrpW4kUVAC-mHmdSr0EVq4Jb5sqrsRYW39YLFVOm_onEiL7o3G06nZidkE5oVIjxR5NzuefdRv-KcLUopiJP889u9RE5AzVeg7aAPrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BW15BJ3Cy7l8H0OBqCppm3l2yF1_Ch1EBhLyWDIRJ9erdZ3Qu8gCNM7zbvkso16DFS0JcTgjMjPAOeCVla0QkB_beVAZGjvNk8MJayI057Bftul7ctLV0XnkzRt7-2C0ZgVk4mrKKQb8fK-ZiLAp1LliKJpetSg78xiZPbqKG2M5QIsYcD2pEEGwWd-GeBeFXkOm39KXCtHQaOuCoP47G5DttWBI2jc0zVbP1IlBSRe2Jvfy0RUt-uI6t3gmXvUh1wPkx4hrAF2QV3jXwvjdjQ885B0HmkHaKGlDFts2rlsivYUVq_XD4-sPHpLlyOWGRCrBhOzePatkZZZzfA3KRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DD0BlOOJJk0oWG9b33bxHlh8Etmtr5xS788gyXaivoD_4Kdp8jR97tOeS8hdREm8geUbpkRal1ER_YGeDzYzxBJHjeoADc1h-76toMXhtGKjRzAU7FadhFCXkK5Gec-EfcXxzcXgr3qZgvVCJNGQqbQU_irYgsacQkNqff21Sh2iPEN-ShxIsnkPXPo_sLGYD8OUXnOnID8xbeNMhjhaGqKK0QncMwgO4heQ_ihSLWfJNeuY_Bh8jbVxeNbU4jE9r_fGpswTq6CZCL9eGUCAc-U2DJFWoqGl-eCUdiS6B609B9vR4vD2WtJdr5QCjdKtjCJgoenA_d_4VO1rUXLP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5pYY1eQY_APJIDZwpkVDfx5nfQvw_ylnVFRnmcT6dqfd0or8DxwuNdfb1UkXtMHg46v4V_0uAM2IU8OBjKbW2YPlmjwEue4j6Gk0kECCC9poPEQ7DNXlfd3QSjxiZrxf8QXwY7tKKzDUeUgYLXiEN6IaBtW7s6QqnJ3YMTvOPB9CNJc6KHb9ZiuUucbgo71T8-hrWr04hFJM2L4OKKCNkNOLPc9I-zxYON-8P8NUU_rEbdTvf77Ea34n1k2eY0MC5gzjru1m5_zpbKnUnJjA0bE_iXqe8AiqbhAQx8lXRluwjXWrLYhtap3d_akBDJKtHj0_mlEmYEZKnmUVEhkOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT_4LiZlVdCbAulPeXb_oTPxAmqZQypYXnHx3W_CAY-xAkU-WZr2Rvtp7ei3R8JV4FnfipO-kpG5SUaS3G7AkRS91clfhdzR0Gra9i4-uyMC0Aj4B2sAB6ukkUeup-0DUrtWk4MDdsjQmH1NSTwfK0VYN2VYfZJtZcLaqdXVu_jtwqEnUFELY8WcnX4FOSPPkJ_fXbUSnvf_gjPEuPHN48IcFUmLhes2Hi-VuOWqIAxWV3l9VZr_StB01lgRnZypJT53LbvMyEUqteeaKMXbfowiIKRxa8taa2J_Qc7dYQX-D8QPRIG8Vx74cXgyj23hz9Fj06lJaBjdNhy3GYfS-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-nMskYp6o_yPdOBo9-pSAEgYotCsVBpWkyQYuVMpRvaaDjNfDPyxNMnUdu4dDJVWmA2D_mO-AmtbK6bT_B-rEScqALoiZz1ZA62bC0AaC3XdnrSMSt2k364iSaG46UVM3bI6S39WL3_hje9JFiZaE2BxasgEuUuBr0NbK-RMtOto1a6suptx3lyg0OHy8Y5c-Gzb_7yvRZL6rXfZhXDG6vJnfEx4nUCd_qe65-v4brJMxOuT7P6_21xyAXmkOJ93pn4G9KWrsp0SyXqm0es19q5Z9TMKq0ZS0bU2ybT8Wc1LMOLwWbc7NMH3fTKYNEQgCKknVJGgw92jtz-hGOt4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjgvkY8YafzHmXKkJClI7EdgDn_Xn3InUcJXXfZVvaRlZpeQqZcLt6R7AvmuaZuEzxou-YmU9eeMZVaJLO7I5lPafTsReEB36XdE8MGWcfGeeGB004rcgezXPGgW4d9e4i4YhgmrLOVTRmIuYVQcz7X7VRC6dMYPJg1Lei6x8rjxlbEEEOi2R_UVhTWvT0KjTD8nuVP0hWQnXj_P2ukmmKdL_64HjMAYasygc0BVwElNBajQZPLCIAxfBL-n_FsczoYaUa4HKVy6jKTLXMi6MvIzqRzkJJ4TKLdxXBHuVR5zeIKvo6Bf5LDqwN7Jyo-dUxymdvcmTtPe9Lh9mckMcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSJiRk4LB8-6FgFR99KC-If_Nq5SiRRGUWdfIDaxAHk1eKuCsWLi_KQFQcoqTCnKXnnfSlN0mUvyxkDzzyOMpBMS-C0n5oEqB0y2nk7N_PZQhwogpdLKVnWktC7BFdtrAi-ehVXblEkuPKTYtbieIXc0ZRjpz1oUO4jkGQOowWmDHjAAUQakZUjzOpoIUWlooc_WAtm6QUKVp0hHqgRa-YE5o17GgZ5Y9zqGhCQ4m6xtc2LsR1_1-4gI1QOqt9R-oDqJo2ux6Ay2bZa_x_CkhfU58mLp1chgGfwtoYNGHThmj_M082NM0-tQ9WYsbu0H2RzL-aUYFCBds7seCg0Wjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJb_ex7BYObLl9ZpLAtwWDlqOgeaS0fc6cXZPZcbVEoIDV_C14j9wt5D30OzI0Uu4oe-VHp5ZEO_hvCC8-aRcI5oKCG_rTdXNpG3xzs9TZNzxKn-hFzH7_W5i3lVNjsp-S5_qEOwx_80O-zz98tIkHBl2f1ZOt78wQ-ouWgryFbZAJagH48_wCgu1ZLmmcCvNqWcOIje2WK302IrMHFE_n1oQ-EAGOXyVZfhgWJ5Op9XVYYxWkojDFwgEqT4ICe3EBD_bi7LDhiz4OMqBmm40sIYuCgKIznDDOfA7WBL8f2NZWokm_di7c1_cIoTZNFnMbsY_pgzxnkRrVKUtPEO6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTgPUSYvW4Vw6LqPXxHFGv8E6MduzUw7-7krc0eVVjFLGoQ7ArFxkVzHXmA_tvM37g6SfgDvjG_3EuIv4-0o1F3l7UMluOAJ9RTuGTq3S0SJzKTrrQf0ikLctZbCUk5y9hRA8D-T0YOD1AFOJ4fb2GBbIXV_hSkan8yeMdIP1C7lMndJX-rMpr7fEBMjHDl1qnEwSDfP9w_YdAEP3b2n0NAbjQIIQO8korJLltyaXypqFbiDM9vzPffwiZRR7ZaYF0Gum1eDmuiaTFP5qGegsCrwHqqFOgwhp_kTvm-xRWTQL-Jy30pg3fOJH708eOIHeFswaTlZ1Oqt5M1nWY9mmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txHr0vl5n4jIJmQLDpFXg_vfCPTmm421VkWrnDJs41wYhvvj9AJq2GhV6xXvKl-ZzGM6FDgSxHW450VAHz8oBdOiUgoNUSlWi2Cuc8sM6xHQJaxH6-GHPmO470aLTqk3tFfWgKKyFb2iqPAwQxlk1h6e7fbGTE1hAGaiMWNJiDAZdNHAxwhY9J1dxWqV1BiSrSf3JofO78scG3KD5DB5iP2HYXUzzNeIFxdcQKloayhsXCYfEODa3gnVenc8k3IwwZUwt5FZxBBK_i72e3RFhYGarz1mtHgvB3fuz7d6UEkaX-l-gn0Z0LsTug_70WDnChFnYZ_Nx8CkfdBEqnk6ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 637 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBp80FQxlhj_Jajrf4H0CIhWrkunFJoQTCnlEQ1drG08QoLVumnT_XTmX0GfdWXp0hXR6yXHsUiUZ5_fjnnJK5peifoGY1OkodT7sY7SnQwhpq2Cx1vYDQTlzoKq3SNoqeii9R5dLbed2Fom9meeJzrpsYL8HmGkF-KimVIclaruVxbj7x3kzJhoiDTOt79Q3G-6wfqiJza10CL1PKPQeumg-ZF5A_N7WAh7dKLjfagqR97gOuetY7HgvOtS6rkilY_n9zEytAN0LtXBB2opyz9VG7E3nrTuL5nDjNIv8nVUCb3m2fFGx51xBOAntB95JgmEj9cwF6t5nworlw79zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HpLpUntfrb4suxTfV3x5SKFqQliY3tPv4J9w0Ox3dkNNwinaDZ82jEHYM3wd5MZ5RM8P5hQ5Tk3mclsIetXdJnqIf1c1hwu4jGEBIOjS-WOXhgsgEum5ltYMaLhddHWta9C0HWp_GW4f25cE4_q-7Mh2LToXZBdtzRs6mufXAjKrPFeLpxC-Dfz0vkmlPGE2j3zru_toq-lQCwaHumeg37ssTJxfeB-6ckTLG8EC8tBiH3YLA2_UsGa83yzv82av2I1LNCaDw0FTW0lQAcWi7xYWIWOTGJ8SJMnPK8-Gee6AXlv-34sTtW0yCnlrtEvobL7M9oupwQuwYUi2iDUl4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckgjC5JHyVMbJ-00F5BYHbwhE7wFLaAAcfU88VERT3qv4MhuUCPH42ASTKPiI4nbmOlmNkaLwG9CSkoVzmXrrS1yogCz_Q63_R_TKwM7U31D1cozKRmc9qeVymlGFcEbropeSsfDbqUtJ-b_8U-2t3LnEZpcV2Kv5mhHIjZbYYkXTtU5rWM78mknVGANz2gq8CDLPorQx5icvgoM_xLVdYOXASVrZg1NKLseh_GdzQ8srj0D12SHsGwwPn2yk17iRCAMHB74MXldvRV1HRU8KufSH4pmXd7ud9F-CBjqurGDE7igr-VdTbo1ctXFm1x3WkID7uxStA72XVQ3YSMzYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2LKD5ma27jK1nUI4e8EYKj9mkoaLU87GZ0WbcVZvEyVssnBmmg2bLk41SYpz_NWSRqUimFBqekw_5Ig--GwpuZ8fnWPsM1evno6qJdkpmfI4hsN3TsPFf2-QFe4aHL2fXtnAp_3sEFquksscrNf-TIi7ZRShyCTtt67gaek4gi_M_GD-dmKFYZ82Ht1v-ESMLMTyrs6qTvEDBx07Ue99MXyF6kqiE39MdKLS2zhorYpIg-wxV24zbZNUGyHdSmndtLymfQKyQpW-RabTTxK_JH4oN3CTRLzEqQnKSrqsMQ-WWORIpQRVu4kz5w_3-RPoIgajB6fRa7WY2A85xIEfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsc-txD02KdwMk11Pr3hFOXugFfvBizwpA6mljX1XhkMDQN2bNJBNgZq30KcYCp0_gH6fyCKxq_myCpG-vvGQVBrBzKxhUxHefa-5OhtBU7r26XXAjRMMMIL21UplO1fwzDj2f3nwb3x7bZQe33CyVrWrQoINWvP_U1VXGGR23VG4K1AF7MZ9obXFZR_qU5SIJT5fHeNe-i-HQad9_rYyurKpig8KW8YV-2GyIMalRRRd0JHLPOw03tVOFaJmoTM_7JoiQRYzmL4CLyZij3zOQBmJjVU2Aq_ZMi-0wN1y233383Iuc5ImcTs6KEHUH1FUSRrOs-E1C_rZVvSVF2VOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlxVy2T3J1SOK8mhEw_JUAGf078aeyb7qi5zZXW-5YbL3Cs0r-3XCzQ2ymdV_vZoUnHqdQX9-JgidbWwaxW6p3W2iV0fzjO6kjxsZOdRkvG1ZKLmKI6c6dFAdCkNK_Ezi4YoMcL_4scLW-n0Re663JBsllaOr1-30RSA8k4opo7jc7pygCjAqZ7cjb5ja2bIaEG0p2m684G9aYnGR77JVFVjvv1iwzXI5qNq4IlbNjJa8N_HNSiNMmsNimuT1v3BU39dwkNFddANgPpGyxbqWA0W96NuW5Kmb5pDdEepYeUxsLDRyzVSi9vMuvsTTJ8wM0V77F96UVGqO1GCsNpSxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsRWD3kKJkOcjkyJAsHaqokt65GZoVDJiXCAzC0nvymx-MED5CURnkxyJmWp-WD9NSlYtlq2Eh5AH_S2SLEMS7HticD9SQmG1b84zIrNoTfTWKn_URF8Fom1wX-Ynznnc1mozF4WxL6XMFURtJXMIdZOZnwRTlmdAwvKCzSfPiUXGBJ7wEzBkBf-K67yNg3XCAcI8nUsdSpvGUWs1TVd3bAYIOTWs1Ets2skoWV24Y_nsr2FqDk2R8G7IIBpk5zjRj5W_ztPgE3XyX9HIcLCtUCxEwV4yLGwemmwzRigpzqP36zb6VyFBnHI_QT5DcTNb1h-TwHOByOgzG3qef3s1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aT08xd4XMovHYSQQMLzpkmxCyXl1QR49tdLSpRMyXHULPz5Y3Ndun4Dfv2Pv-_gOkotHT7koBSxgwYCppqMaFLpyc5lLSNIrGFQdzoASmn15QM3wVY6igQbI83sfSFDZEUS2ewziOgdJOo6Wen7GCCitNfyXRJyLNUROBeBsKbTTZnNnP5tLhygYyj_D6CTbzFvvA-Ez0R9NobzSRFf2IyhDBUakMya7v_2Qf5v4OMMO8AfPBkZ0rx-OSWR2MnkBmq0ytnZ526LaTCPGQCfiX5CIKmKdYpzQCXKr-3p_LqWYh2DMgNjMS5XF4Jjve_uHYtggBTVbtH68x2D4EpKIvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUxWQdwod-IJDL4_Y9UBVca6NcBK2Vm1PRLfW1uodekJWMtewgcHICWOUCoF07EeVsjopOd0WURoA8Aw0bh_TaJjkQ9vVE9-DHhr9_3uG-01lZJY7FFfq7OctpC7_ADjrWodT7IYkMm0Ah7GNyduMgw-RuV-ZoUictCZp5PoryZUd_45BKSfRKdD6GvfcFX6TXcANRlP62UCOXsNNts5rOvYscJBAsAmOxrHtHsYWYn58CHhOnAjBp9XzLcveN85zN8Hk_ygxW4u8dRfnFVgvZ42NWcNG5i9Ec-yF-1AKIv4oCcBu1dGx8n09xYZfkO4AxzLlZvZ7Sj2cqbsF59spw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ue5ghvg3OrKfCecEu8JaO7frIieK7a170QNZh_gFP_zWjGUvKNbj19MaJ8j1pmPWMBPRcTw09Iar4Uw5Je_fsyDhWJOs1KE1GWK-nRmYw_1g1-4sArk9J6aAJtF_Q_lkSiw4x8-oZRhH1_s1oszRZ8CoTJ18t_VIN-OxIL9m4lhrNTVfCzj3UqtXh5gaAFPWlVlM78TN21ffhj5RhRKEe8chOBhDHrRke5IO5qSDUdvNnqlwLquoazF16agcd1Bmxb2YLUtwMdc5ugnyfJi9gaPlZ4Y3kcr77qzrOjLH3-FcfO5bVMZCKpGqk_b4DJsjxREZZA18mEUvFXJWscRPrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cizpHL7l9a-rW-inI-hJkombm8ChkGLTKH7EhHTl6jtqg83G6MJ1b9WEB1jqxim9P7H9uVhcT6GKE9b7WiH-4WaAkuiQLhW4-ZCAttzOU38cKfTPC9UOn7YPdgemvQxGMYhbfmZnlGgTZov9UhlFxbduoUy0o6s-xHjvRdo70vWfi2sb51ai0_k-zy-jW29_IRczNq4_elC-doj9K_o_k4amXXpHefxrIKKH9wiTYouR5587axN7AqJz6WOmIUSwYLqp8ikKDj3zBjp0HbeOEhJWi6vXscX27BscaS4At18H3mQ6s18vHBHQq2NuzUd_nVF-o3yAZkhL94gDzKHwzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PILJdj9D-3lZOS3ZGdB-KK24LZ_H5Hcrdz2RSCjteKmMLxsBeuRrqupXglo4HXrGTDIClml8sYA0VzkkW4wbtchb2uQ2SyJve6OwC_rtzzP9atk0Jr7M82YcDoeIB1dIJd92RCP-l5n8bacwS2sw2qfo7BPkYRHCr3q1FuzjEKnX2Vd-YEJbgv2kgnh_NJe9BtQzepujir_-r7OXFght1lUE5wid_yxasVcUx9EOx7f_sc56KNhpdFy2ejVq7fWcbOcQBUGMk8_VxrZxsqzR6mKAjSFec_75VsxLhLv3uUXl4XAov0Lzp2y-vZVMUE_DsCla6KObwg5wBcLkqKEOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjw1EFZYfbHbQSdouGCs3Yqm_avokPeDFvo4MblKJFwZx24SHuV_FXqBR8Wo9VKqVf3t_-xOZb_3g1nIZKYo9hCKuygbSq_A54E6hi4kwm-iwYQTbMlHDi4qZCLU7xeT2x1XdKguoDWLGSF2-k6guL2ufZyoiyqzEFUfT4V1nagZs_l-94BcERW2N_uNcpKZlL-F7noZI2VepLr2klet6KFEHM-Sl-dRfg1nRyfN_Nc2DHJQ-utSorZEWH1oVP5xcyE0p16h3-qE5_e927PxNctH0Vhl59tQ9GG93HqD-hb1psDiOBPJ75r9jvetdqAUpcM4wPABLYPUhouw8CuRmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAklExqlRUMG29ziO92mJJ1c5GtcCiigY9wp6zXC3wa9ePeOWz-t148vaETWJB5W4M3D9w08M854QUMMAhbeLPcLeLAhvQ8vnP4xeHjcx2F_tWJEi4kMK8nEkrMUUGxBuI4TzawFdcDEHoIGEuMu206HnwlQwA5BqlKZbfDfZQqaeyxj7-ZXZs-obqp-vPegil4WYDa9UYSTU8Va35eTFyMGt9Zso7Rn4VxO-Mwn2oTZPnZBpDAYsQDu3Ui3IUIunVJ3PEpn7hqIQ3RiJGsuKCtuuODUC3znnI9LnKaGe23evbrJQ4-VmSvUlq4p8GafK-Vl0cR0Tlx_Mk1V8leyNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXRlfQdYT5BR5rgFWoW9FU1bjh769ImQb90IImQr_wOn-CujQHaqvduGj-O-bqJNakubpyliSIMYj-i_XRLFu8vo1ouYmCyMIpifxo2p_caaULGD_eQBCRKqY21vkr0NfUzsihQcwVRZ9QTfamJplFGSWkxSJuGKdCaGhSKWUYSV4IuM0ly3gmqRHKZXYbrv2UKeIc5MX7SLDQxuWIZGOQWucaW4jo4eNnKGapOoptWPSjj2Fcqcr4ESNFohOGa7cwfa9qUbsq552LnbwHJv39sXzu9SL3ewVWfCpIbJMjANuIygTUXxBSzs7EpLtjKPCkK3yNS2Q2shnzie8xfJrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ4loNsOMttlnPBjsQ_mTJNFWIc6TiXpiDjmr_EvEYiPv-wxGCItmzD76j8CLd39lpFmk9k7aQ5YjSGL9xVf-9IQn5UlywGhwz1aZNvOPMHVN4RB5yqMX_0mUFbR7OOX_QFu3G2JNAdjaV_D5HZDmtimWpqQ28lCDWnAdF2UyVt0QQ0F87TNSbAxT-42mELhLyLytVC2ambYAI7ZwpINVJSVeNYfNkcCa4DHZBxPu9UW2NDYzaVamD9o2dBsbuuFKZAFee0Eti2fCJf2ROv5GG1NvuTD_2XQliYK3LzKKhcYOvYRn9m3KVg41UT06mFl3VrZRJT4fKjg8UavxYeX5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tF-IR5iurOjFAPUTqFbO5zhzU57tFXlsv0D8ZLbA_ys7aYZpYDbv8MCJY1NNPng1_FD0D9PNsr5lX00VwSStjq03nvBXevxDjCg1Hvkon-KWdscxBZCOXgRw0ewtdtO4WXPIp6VbFXtmSbodZ6W2OpB20dF09cvgZdbKiHcfSBQ0oXQP9_YQD0sw0j7XwdSVWmvQQFTS8xw2O1SD5anjPoe-JAcSTHHRQlhTHgK05X_aTAbh5Egl-RaSOZ8W1XkgWTcf93sJ-afQ3y48w1fz_oviNP8wx7PKUGFhLKLZOT__q1l0PMSNHPdFOAFRG_EQlAZ8rQ9ecZcVoxifMa_eMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fveCXnznpJfezKVQS6GDr2tKznlFDSX-IwSdVYaZCZkp1o0Fe6xpbs1JKKhJ4tH9U67b3qUDSjjfhJgIPFWs8tqBIsGkaZQ2MbFmHdbhbFQKmnKdqhOVVGzMy46McJBItWHnBX6TZgpVJ1bsQI3TvwPZeZuo-CH3-dbaHKyFk7lAyJHa_5siKpkrnezbT60OK5CusIjIaL1JK2IomNkhOzbUNqqw4ScY9AUDR-wRaODYc4Fsafxagb4XtDyCQ1mWFLDebRpu4-J-T2zK-v7lOuTVhuO7qPWAPMx8EjB8sqZOu9CWTUuXV8Z11zXKkYsxsPgQDAIgFuk7251aFpT7Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE399w1MxTshDZRrGZEielESVGveD9WATr65BPg39rdyGjxwpTi8srScW-u3vbkOzXwCnoeCDnMsfokMDEOBoPW_cKCfBY3Y9M5kDV5AcVfdFmS97faVjikISUxRFSOSGUwtc0xh0tnOlC1va8U1vbn9E2RfI1lBRVUUdT5tfrc6CulcE6L18RLyH9_bTG5vuDGOjmazeMaxWwOk5-zt16_bujGPTMhrNMe_LAVieUycrG2y6GnInbLds01QDlpRAzCP6mAELQyzRf2jV9Zj5Tn7bjNnGgjAlrL9Gb1TSs9AciVgImet9AAI_r17rhkw034GCVvlgS4-8oAvDTcbNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHyE17Um-jgi7KX8jUQnBd4hnKAmz52eztAopnEA5WlhIfLA0GmoA_InUT8WuOn06k7ikN-IOxSAOssnJ828YF4VGQ_4mk_-HriyIaA4GlW4g1CiW6L68z_XWKVCjbRhFNaMzo_X9dLNoO2cdSYTmO8OhkdHd9bws0Lb0BETHxBKmFESSTPjmsjhD1Sccm2u6yrmqGoxLmQWXL1c6Btc9P3zBMYZiO-jOwd2RdUmmW3wGjU1o0h22SYkuncedmPPmSow1nFSITYjbhUB1h4R-XaYJpURe2JMOfxwNq0tyYtwAwI9bMD8r2pxJHlm7i9w9n8CYGnfHK9sCFXghHpvOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsKxLeSSF-dQAaxggiQJCJHQwZAcLtj71vJPzkK4SQ24QdVwmYtJi7LE14DIfpDmMtpe8YNzzzzUcB2qtgQjVl4q4Hi9oVUOwVQMgGe3wErzpN_0X8M5J5Q4VUBfCYmvQ1C-tqDuTQ0UFi8enW8YnZtRx2oi5DdPasrl6K1WzzsvIrXSRGVTKbDkt1EinajzeMwi8XZOGek2aoOEn_paZcmiF99rHwMgZIbZ1QBAaspZZmEPgH_MiHLoi3bCboy1TAvg0zh5zxhi0u32qvaIWCZxz39gYLw2cB4mqxBg_Zc1yU3km3Nw8hmV20I_Edf8hMNFm4-9QwKAOvDnoJhCCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmfoW9e7Lm-9n825SXYj8R97SFHgxVwjZ8uCMmZWJnp5B49aDWhSno2b0VjfLcI6fG_FYC0UhvpSuPHJ-65i_fcJ7l3IXKO9_Kn0-EUTaQn3IQeJ7dxSIRs7pS5XTF9IxF7VijhzP2vJWgI3uqIMOCiKOvNufp-CC8NfUAAhsevDboFLOoKwBPaX7tqB-sJ_ghOYoLungIo4PcScnj97DvfSKnhdJjw0MW5hDipbj0mNO4Pz8ssmLghfr3jwlV4Klt0HiiZxNFKBplyYJzYOnH-9LKOKloVAT0pGgvZ3CQKIaQXQvl1ccv1F0mfxnnyjHsud9NkBBGv9F31gIeFBeQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=vKxPh7l5K5Ptz0IE-0TU1FQJQ2B9o-iqY_ejoGJoajV1L-oN2tnxbcQaq9OElRe8Wt_Hq1X_zXtIE7kUj2hStBSUbqyfzfjJQaajYUxQZws7f4tvYxrzMXcTF0xM6T9riBZPENqtwq4-gjWrUwPVZR2y5cSrl-08Oa41kwDVmq9CKcJdPSPDOnI9I5eVQIYdHRzLUuMVQrZ9cYC5RDybkR-uNbq_gEmtlhj-1Ytd0752KPld--1jNzAS7f9W1P3xdB_neBupxAhJn9e_0DDMIuRk_T0rIV5u94qj7iO7soM9PAzMAXTQfrpRIY0BoPIInkJkgKuO0JTF4WVTkSNAWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=vKxPh7l5K5Ptz0IE-0TU1FQJQ2B9o-iqY_ejoGJoajV1L-oN2tnxbcQaq9OElRe8Wt_Hq1X_zXtIE7kUj2hStBSUbqyfzfjJQaajYUxQZws7f4tvYxrzMXcTF0xM6T9riBZPENqtwq4-gjWrUwPVZR2y5cSrl-08Oa41kwDVmq9CKcJdPSPDOnI9I5eVQIYdHRzLUuMVQrZ9cYC5RDybkR-uNbq_gEmtlhj-1Ytd0752KPld--1jNzAS7f9W1P3xdB_neBupxAhJn9e_0DDMIuRk_T0rIV5u94qj7iO7soM9PAzMAXTQfrpRIY0BoPIInkJkgKuO0JTF4WVTkSNAWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGTC_mWCZg2SGYiDthHd45QcQ9xZVUcbKXTCX0V7Y9kCv7vX2zQMFyg5I1IVWAu4CLk89eMofg4-eUauf7eUO7Iyj8ROP7hkw3D5ck0r-lwvKFAAeIcAzs6YgzUToti-0RwJ1bHCUFTx9jG9fMlVh7btNGHKNqjC9aRibezuxXuwVeVAInecoO0dnYzqFkXLDCDkoGH4ewe0o-MlTqD9Rc6EqLIDAFCwvCGEc9thI23wInUrdbeZmrJ9vzwMRT883pv0MO8-5pLvkaMD6bJvVCTkzlhdGbNk5p7a8-0gurGGeKeJZtwO4nYYNKyfSZiCfkokoQj2N7IOmkM0jnp56g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBkutt2xR5h_dyvk-BvtRwLyt0PSghve9c06-6SHL6fSUh9c_7vrLGBzET_-QlIp4MT0BXxoEitFHwxFnXaUV2dPZiWleJZlC5_obWHADK9vWAleCs0ZTBD8PCQhtlM-bV2gjk9siuFIZwfve6WGCz7_S9D_jp3nFcJQo3KuKcpYOmTxi1oNJWrFNRxgo3UN24zxnNo3wtjNYBY6ONyqFegZFX2_z7qmA_33Bnyf86i1CpKeuxOMezjdTOuOu_5NGtN06yUICARzgos9pCAzpRSt-wZmWxTCZOmXoN-tB_3VLRhlzLXyw8O_lRRFxibO04KrYpnc3J4eP8eQ81u3FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGNA_3z_DCRCc1a843gECiohW51vBjoSk1o-a1wsmpU4L85jhKJlpa6LTF0gsGu0Y-HWMqQZ0zvbbJnnQmSzIrf-wi3im5a2V7RnDkJ_0LqJlRqvtFt7ZkmGm-9t_GLI9jV0cGl2RZV1_smz4igwUhndF70zQzDGUYq9gQwSqozJMvdvMO5O2jNI1ViyzDK-xF5lyhpnnP3UlJecG8Rv8VKsLfJgFeyoGRnlWThv9GWvqImdZDXFo7K4yo__KjAX_pIz7Q_Z4hEgubvxjyQbtJiKPQkHhd7NtA_i7XeK0YCVm1hPNmeLqt3pFC_QOLIO8LVzf1Uj92QpsX_mvBIZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1Z-gioYFhOHwNGtCOsSE3HmLfE630XUzaRzQYbcDEALhOc15hXAK_pxpSqijfRgCHNBpXMpAsBUkm45H05toxMuawNG_kj0VccT-3Qt-kQsx22s74C2jqwbI2chL1higOr5hbuTcpfX49gpmGi0sSe7pqokUdziGNb9n-t1a5GQ9o8f5zYt3sqx-ReLhDdu-BIAK2AABwfhHwAuLdXzM9R-g-Q2fGRfHmGvJFqdR5dVqOiI0HtCPWymmKo0jRU4G15217ZfCoreey8vriyXYsmKqI5JS-0PAiyQiWnUYY5BxZwTeUjrkhZyjt05dwS7E9EpMoPN_XS4Yx5E0Pf_BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDmvy_Yup5NpvnZKRZuIqOG3TiRcl6vb0VAaPgFPLCXhzBYlvCR9pDyI2Ww9J0NaVa2smon91d1WkNNxb_5209RReaqFWTK1Bd9QmYVwFbG7kk1zGWWN_diHtCSs84awq_Cbk6ZnNBEKnIRIzUTJvQCJGnJq88wSKrEM4g4Sa-8fSnydSB0Qkza57_gDxaGl_2ewt-c4hcWM7YNsIgDGU2rdvJ-OtsRj7ZdevheJefxf5Gyrymo9DWAI5mq3ALc-NohwBRfc45MaPLpPlGG1ZGe150Aum0CR0flXD1Kai_atyDRnISX5mdalh6wAkhXJ9t5OB7ke4Yh4zDvbSkpEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ped-kQXXihCMclqpL0w4p4RQCOlAcp_wRa0BDRfCg4ybqXEtrxmBUMAkJJlBqTMzlFtt6iCADr49W6D2esC1i2FLp6gD_YmHq4Jhg8gG7Olo_L01DHZHEkCFMjVjEXwSaQIEr58fwNfDKmF7xHTaUbBvef9dEDsrKmCBvtLUnpcUk9vs7LAOI01O7ML-XA1a-gwElsVTmUpddQaRnoY4WKJ77xbrt9WnmmebwaLEEWcsFQkfwYe-k7bqs46qXr8aB28fy7N3iMPm_maCm4cvaHqUzA6h4tWIaA3bydPV-7jXClhNmv5jjXjtRjuhvwfBbGd8sW00LWivIowuRVUIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wA94Fm3EBZqszl9OOKKRT2zv4Nyck2vVrNJjqNMlnUofDtu0X_D5UZMC8ueWKCCTHk1FKy5jBJfS-kUMUgWzpHrnq3L-JfyioyKd9vgnfkhfrW1g5OzZD6IL6efvr3x2UMU5R2fkaGrCYFpt2xSLvX8Cyy3cT4uB34cXZqDBUHSQxIiOod3tM5iuoLHNLbgNBp4NDMNLivduqdBzdLZibK4fc4-pa5JI7lTN86g6q5RUicYgXLx1Lgp1PpycQej8jufXTWJsAJdMeSkragW5deU6ixa1KdUeykJGNRgRL_l1BBgCcqKJ1S6C1C5SvhRrAAZlv-jNgpV0UHAdq751Tw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=EhVSnm7-RFbk0KKZrwyBcRY7I4q7ZPfkQPHJDRPGOF1IfBy7BCzlrBwcNgDJLzhU5Ewyl2cNFu_cxG2Qv577qlI1SQo_HKJ233hYU_Pu0669TRiz7_UcdkcArmEP_b6o5VcXLW0O6ZNV4jm0WuLyTO0DJQp_9m8MSbiyd9H63bvg2btX2_wkna5rAOd7UQOSSk2YUqJFf3v7MRHsyIYnenGNzEW-ilzT1CqxTLcpaDf6V1WTDrdHgmnoxxOg2hwfmxK9PWu8S_xmufTNWOYb5pj6zNZiLSRV4DIU3nnq-TmHhzQZ3gATt17C5rNtBaXMvzHFSsgRRVNw93owIat1jTidrlNWdmz2gQvKy_ia-BvN4bhDz-WblS_JqscYuFUvd_O3xlIXBmtNVJ5GZjCLsxjbq8BUR3YURRnjEs3I3l0_KoYeMyWUnFdUK4sigVuerehliBejetqdNJXRFMM8KNmi8KqfKPmhM6GvB3KCxi6SOkHh9X9Piv0emEcshC4s_IF6cRCSjQJCtB5noVrYePnCwvCnxec1u_nlVS4jiUss2HWxIlwGZ5N_AIABqXcjuoaSKxXyQhHLKsO9PG_6CclQsG4R-xy7dxvGySJ7mzbfgxfO8QaLmCBAuluDElePwKiKGRSrZ8XocqdEulGddAmHZbHm3oU_tQg80hsX4Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=EhVSnm7-RFbk0KKZrwyBcRY7I4q7ZPfkQPHJDRPGOF1IfBy7BCzlrBwcNgDJLzhU5Ewyl2cNFu_cxG2Qv577qlI1SQo_HKJ233hYU_Pu0669TRiz7_UcdkcArmEP_b6o5VcXLW0O6ZNV4jm0WuLyTO0DJQp_9m8MSbiyd9H63bvg2btX2_wkna5rAOd7UQOSSk2YUqJFf3v7MRHsyIYnenGNzEW-ilzT1CqxTLcpaDf6V1WTDrdHgmnoxxOg2hwfmxK9PWu8S_xmufTNWOYb5pj6zNZiLSRV4DIU3nnq-TmHhzQZ3gATt17C5rNtBaXMvzHFSsgRRVNw93owIat1jTidrlNWdmz2gQvKy_ia-BvN4bhDz-WblS_JqscYuFUvd_O3xlIXBmtNVJ5GZjCLsxjbq8BUR3YURRnjEs3I3l0_KoYeMyWUnFdUK4sigVuerehliBejetqdNJXRFMM8KNmi8KqfKPmhM6GvB3KCxi6SOkHh9X9Piv0emEcshC4s_IF6cRCSjQJCtB5noVrYePnCwvCnxec1u_nlVS4jiUss2HWxIlwGZ5N_AIABqXcjuoaSKxXyQhHLKsO9PG_6CclQsG4R-xy7dxvGySJ7mzbfgxfO8QaLmCBAuluDElePwKiKGRSrZ8XocqdEulGddAmHZbHm3oU_tQg80hsX4Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7h-RgdZJmJZGydRctHdL_26JFWtya_Ws7YXlbgIFvr8a-WhKEM_VhLIojok2ITQ5PH0QHshb-3RlZODJF-Ob4qs4i1XHoFhOayGSnaAosaEFm-RLf2Jry0-jctbUKqPUVje7t01l17yztM6NQbo8I5RnJ5rQ8n22KehAvTJrCAxCH8s4gF7B2wcQs2rzFD-hbeTlSTUgSVyXATOoyVsVnLeIgYk6qE3Q6tdsDZoO1IkMq8cE-E0JRK-gnSnVLpWGPMQ9-jCUNGIH-XwrLml9lB86wLegUXyACtDwbP81fGlOWIdfc4Ui9BN2OPWHPRIWgwWC36Aict-Czo89dmkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjjniUv_MhUl__EkR3ekil8nBuMIXamnygirZh0U3IR9UkLBPJ-I-o44dNSVS5cHq7dUl0YVzwSCMd355GVRdm4hMFJb7cD24oDt5L8qqjAL1l1NeXVdh34E_CcURZtdb0TusQS7UWhArSr9a_uE2XNLuitNdRCtrcMmgXXqtBbNwfYKy_woqwLb_s4Xakfkq_JPwpwbtbcqQRjrDvvtNMWjHSdA6DAChNFIEf0-PqVIlBVh_sWL3DY1gqdKRmCxkFpp8FqepcjQzGFnPS1gmvGmX5FElGo6rAgMeQHMDOWlm4x2-R1bBBwUaSkyY7szB74t_E4SIy9s9UMzfenzmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeGMaU7Iy_rfKKOnAV1_tNOZRo1BEo9NyPWiL9eU4lXpOe9Fa5aHwqTnkSUnXv_cAhQDBZrmkAkvzMpyorh32Af_yX1rkn60ghjGI2KVHoVJmpmL8S39yFSvzXV2j1bFQrspHvXM6K0rK8T5e7r6xGkSNPkpLVm7yRY7gkqqaaiAdo5DtDBbQVNCLADeA_fiGVuh-qAILGupe3uqRKz0gC8itun2-FIUf33wZeQKEQreI0T4YdNK3kE-waH5aYWRs_y2mVTWjVmoXR9aw1Aj5fY2g0IuguoOJ6sgER32vn4quRzVpH0DlCyfIn2Vw71zX4tCc0Z48H2sPyZBvPkTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBL5prlaQotjMxcer8cZFXyl_AMh2az2m4D223FW6a5kt33dyB0kgiQ0-D7rmInXYTcLdV1uCvCiviGSiutUskGcsgOQqb0vH_5cN6gM8CzycQoRIAxgb93Wp_EjR5tL2vS-48YK2GMLDWoCjNCfZlLpvDTG8F1aoQ56l8oRHntnzlowt9i9YHCeN5zIPV03g0VXLcBJcthYGWf-gdnE5zb3ypts8bOawDz_UhrWU9Zm_vuxh30XVjB3Gj0J3284UBVdNEX6M-9b5PkqcNa2Ogmxg9fBzmnYa80lMSwUsW13mbQSvhLSQjBNBObsXdMaxIAQ0tLSZYQK2UGJDNEqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScdD9K0nLLnWFTzXB8b-TX8lpgRLuyXf5tVzGH89noiBk3ItiGaudxucle61RENFK-r8bcq28FOYV8L73pNKRByw7iG9pGf4JIHlR1CMu-gpyrThR2Es9Y_PueL2PVHNcrQ_PJHILG_FuLhO7lBEmXQwWMSYuOwUwJV-79wDLWzPnuUZItbA-ehhxJNsFdoCILykWdKKwON-3K5YhRNiL1jnl7jdiqY2NnEqodFTnnCkDWkT0ovj3_A1d_97G3IOfx1MMk9MJNKuXl7Frh76KoD-zldCWbiNzabhqfmKzAdRyJNhirUXI4ThnRK0X09jJqA4qmxtXZoCsSJaI3KIVw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TG5EH0epSfe5gmOmotbbYdV6IZCpIl6h_Q4oZf3-9nvDoxhzL7dF-OLUWy7y13fzH2Bks4GyK8S-Mymm8pN39UfNXZfWbWKKMvFxF1Z-0VaFhGkQYa87vQm723dFznCUOZ67u4LxPQ0qNWtiL26CLvfDl1OKKTRH-YTzMXI0hGnAaiqlhWW27t71GQOnUnyYMaaXUCfLoZRm-DWHLrIj--x8ve0zJYtPM8oleMnOvJ2AiY5qtc2RfdtJ8UlwD_EhiiXqBUAb_BSIs06ABn4pzx2UfpJEwpnOnyZP-AKHH6ltnGl1XQ117REjYtBd64jvs5RVPO9iUEwu9iPoyqExXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TG5EH0epSfe5gmOmotbbYdV6IZCpIl6h_Q4oZf3-9nvDoxhzL7dF-OLUWy7y13fzH2Bks4GyK8S-Mymm8pN39UfNXZfWbWKKMvFxF1Z-0VaFhGkQYa87vQm723dFznCUOZ67u4LxPQ0qNWtiL26CLvfDl1OKKTRH-YTzMXI0hGnAaiqlhWW27t71GQOnUnyYMaaXUCfLoZRm-DWHLrIj--x8ve0zJYtPM8oleMnOvJ2AiY5qtc2RfdtJ8UlwD_EhiiXqBUAb_BSIs06ABn4pzx2UfpJEwpnOnyZP-AKHH6ltnGl1XQ117REjYtBd64jvs5RVPO9iUEwu9iPoyqExXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqqE6FOpz1w0JfCG71SNuCJCl_JwFHLvZTZG0RDKALYhx0tW30ZcECiL24iGAtt_60WTkRpl2BM1iDpyWUaGdcfjBVG3G1hJuxZAW4TFOEXMRin-3ZJ2hwY0Ad-tNYnNT_k2P0wbf33Ee_Z6Suotaf4s9TZiiihZoRhGVAAavVc9N3xDmwMJq12B9tCP7Stp7WXNj96R9_dZBKEJUSHb7v4TQcmHe007ecwOdopGurwC0QFNHjmd6sbr3EJCTQltI-W2zK22fvHodVWdNReIlpXWMw_fxSZOg3X3ZeGDSrRdx7F5m_79791MCSdzo4z_6kfwUSLjUFscUmZLuybCiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhka1rbbRyJZ-dsGuAbN0zejms-9yikJytIxEPVQi7FHCdIflVD4s32lfyG2NmLa8eLZ5Vz0Fyf0wPvHPRyCoiPf4ythYvLzGIB_WSxZNSEOGlTpZT09c6DmVWHapJhFXRASzLGtXYFWUhYokSyyMv2RPlQnT31sGGEbNqhYE3U1pr8Os5j46ITQYTwJGx4-ymqdrc2JBtisirIWF9zLKQX7Q-N3iH-6Zso3bUOr2iOtus-vxuhWFyv8F45enEdv_QCYVUSA33EgFsRABpsxg9ITtXqw2fbm0ufW_8d2fpGiPeJwri_gUHwuu3AHBRLrW4CffBQla_7l2AIgR-VflQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDvH8Jqj5ta1faOqTLZc4z5hCTMZvtBy9XM3j4l-qBrnhL34hfb2hHPYNRREMpiykrfltH0xeOccT_lSIn-KdD-keQpeKNPh3Yj1lsvi9GHAsvr7A2NMnBgmSor8PyqwFeyzSpIjYn91U1ZLwpWbryB5ggxWvO3vSFm4qXE2EqKboM2IN5iDhBAKhMvFmoAtEShF0i_GaYRGz-FBsl1X-gEmmR4P46DrevYCkjoK4c37NJ8RUM9_r4Z_TBmOsGi4gJiEXsJll-Lszv_yIgpAbpSaWWR4w_GyojrlAsXHDQUGlJqlTAiheXXYQUMXV5ve6UbOVZbSpdpYN1b5_qeoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5gIhJiOsNR8Rkh05ysF6ubbJZ5dCQVAHCfEaJv1UE_K2vQOrYI0m5nOnByRq-2LvJ6IHFKAKfkWqYsdd1kApEOZKXbJZRf-OwNAFTWZrEOvz-aV5TPZcF2XhuOxQ8zVYjCzeYMldVO3n_Lk_eC8luHRJ9S6DLyyvfA4f0ty9w_5bU9IBQQM1oDBkMJA2_fcFuVsFTmKZEvKf__7niGiAPMj4OF64dKckIW2s0QL76UPzRCPtUw6Q2ZymxtZgHtgq5s25FDmWhhAcncC30m6yXoT6RKxSYp2lSpSRMrryX6PhhLc1uM7on8S1qaEjLUNX43ElIkhIJ-OpHaoLRpRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_lVN-_4MBgHmxiJFQcToUD5yrQnt6220jebXIMPtc0wlx0Ot1z9SlElotc7fFfZaGaA3jHdP2z-3K88eEj5Bd-ytjS9h8fzCXsZUrZ3LrtPfhWN_vnpkCdluahgeERQhrDOnwJtGR_GFdrat1RRqgBHApflmopFrs-yVzzOP0MQAbogtO5Q470T3mIjuZworruLxW3qw3c0AtiQuTwAx80nSKmb7SWw_g-Bzu0U6XtZPknZmtjH2nGW3InzNjJpXtBzkTPGIRnJ8XHaut8yp4tIMTowJuhHgArSeYaKiWdaf8Ak5sgB9_Tbb26IxYtfK3pxVvoQ81Qne9-EmHhCeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWOPwVtgNwUD2pWmEoAN0j_reQv-kxqPP4Amk8f5cz3sNfp0icoAaD8L7Ky9jIgtqJZrGY2QfZQPSVF7t0DSoQxaTBBC6EtgfOngFuf2wDYaB38IeaQ6Hf-HSnuz1hK0cgnku3FQV5hTSvjzGSmySFsdNwAXLti7pnqH7P8B1hG7O8XrSuD85O-PSgficP9jVH-E86npTJRVS3UoZPb7uaZFhf9Q66sB9eQrDhMOaxbVBevn2wc--fRxY2k6T8R2xtM5ZgJvy-yNI_jamn2sOHHWz7bw7CQmkTFuZepZ7QzhXCv5Wk4BatBuH0LpjwwbycLN9_OYXKbCO85_hINaGQ.jpg" alt="photo" loading="lazy"/></div>
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
