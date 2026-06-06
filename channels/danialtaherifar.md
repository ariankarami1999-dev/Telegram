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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 16:19:20</div>
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
<div class="tg-footer">👁️ 101 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPC1URXdBVz3MFAfnlS_gsRFjttlhQtNr3JuUic56uNX5WyXokz7zuHme9dEtu_J-KVjgwYDPU39AG5QheYWMSuY-8UXq1VSiZrRrhDNfTJQlA3EjjX28eI3Ln3n_QTtmvNKCMU5KOKVOOlrL1J6nXeJvNqRbgBr72n0W8xl3DVcB5klm1JvD-T4548HbOlyIWZA3syqdyzuP8_FQo9OCNBsXZQC05yFfH_BZoiSlUTM_gQMSwJan6XEnvdbl6nEqANVMnwgctPFpOO7FTvsMv3dPTI77lVU8jDBc_DfURGIq3gQRfdC_7HpYac-i469rycuPOKsfM4ysV6Z59-Xtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 283 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 516 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiyacRXJ5VxPYJ0ZFOdvXrt4kFDAl3mc6dUMg7Qb9lh6fMZLV8WUwtLhkC_iN6rGBqNHLWG_HTHGoZOGgfGjJ9Tc1_N9saR1Pw4FKQzdejyZ1dv6s4A3bwqTwDlyBZqzwc3ZMD4asqtWbzJw7GFoMfLl7J6DV9EP0prIPkLYcuuc7Ojn2Eeu_oVEWBgvTq_HvGB38n74ZbZCg3ZJCosk22hclOBBbbe2TG88lvBzs-GEsAXEQt-Gf2ODa0yCKuvl_ieuDBAjvHinzuXRUSSInibfZgfHuVnn4IjX2hoclA6GwgUNFGfhNxrAD6x_IywP5f9yLoTZlby_FmTvpgaOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULRRrpH-9qV3Tuicknb9OdtYok5CWTn6wEqnSRZ-47_YkxhdpizCo3jd-WGFaXbbimFidtMqRNhsfuYLv-yisdtycp7Sh9h84jgHtlK8IRqUyvDXILwnpdOM-L296azlKmm_kqIw4JGsaoBfoNfgBJDYV4EbjLwBIdfqXAZLsTpTru3-ZM5vhP2sKNPdJPt-oGlcUGZBSJHkgxY2_SV8KJJl9qwslku1OG2laJet8mcHbF0wxAx6UKX0AQBldDcUgXga7hwapz1UxETSNwKVmpVVLGX4nXh83PqdBSzENV6ItxfY6iwCxPmaU4DAWtVeHZSWcISPIs6fdYm0pEwBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 847 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
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
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_AA99FFfIkRf9X-1T-Pj5ZEgALcVjcOiNIed6e2NZ5Aq1r6WAcNPkdDLT2cid74rARSECcUfIsrRIyxXyA-uH9uSDUcaH-epIi7CnJCsfsVce2BDxRwvFUyk8l5H1ELwkXaRB1c6R5hBeraux76JYxPAKsCkZi9JsESqQMq_SHma2tYZGudYDoKwjqhddEHNGgKCb2yenkfFAVBFPf57fG6q8T2oZyKIt1Lm3d-7cP0uTo6YW7aue23jUhrQfpWXtKnShbaaqxIGUWcOPLG-qLOB4mvEXxnIt5W83S5--qNZ2xusYrFPAUHnHSXbt40dvwcktfOi_cVxqpIPNG_cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2s0Lqw1ShyZ68griYChzZUFskMcbMgwxfRaj1focMMGxtVBjnv9aP7p451GjHLe13heXhojewbo0if6VzpNwA1g860bvEkKkx7WzbWgjRoAXC3rQOgfR-Lq-_2YS3CMTcfQ4UG7v3bxKCczlIR2-v6cdqANI6gM2hfYSkELdR8CB1-9n-coXTXqsCHeSAlPcz06_oHnACFRr9yRVNlVap4y3GHyEQ1sQ5u7mAeEkoplhUOPdd9rF010zBd5P2nW-36AgASYDca2yGnmL7KSsAIuys6DKETP6dFQQTqblutVbtywv6y0E0tuUb8HX2wflfcMV5fTcEzsT3USPfMYmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heA73zW1MRlhEM2MEeJG8OYQQLh5F98rnEmwPqt0UeJxXw2xrQnj-T2lEX4Jx3Oqkq7bWlMBh9reyfUIjZGtOMHggryGZixS3nqps-sPJjQHkv_UJPBcKSli_cACohY-8nvPE4Z6UAwfas1ZBkwQhzAAXZcPfFw7Mk1VS8UIyncArrNZq6RWB1foa7Qbgju2-WgAJANGyfD098NegooVHAEBAiaNakUhzEmVmEi3WesuLauN8lJVHszautrdj7859yS3IRxao3cNXG4jh8NhefgCvtInvNeLP-IaDZ1jtYT7EB_qDRZhiS83zNnTaQI343FcFyKs-oS8vjtOMkGJBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jF-icxbGIU1uy-TBQTwOHyNZzIvxmIoDzTgQpLTPSkLE5fPdn_ntLI5j5GBjbZ5hQ4Ba6RF2y82f1DmNhStCknNr2G8q7jruhjAMpEEyGlZxT1WfibtmnVzQAUCGnVbEplE-C5VvyLH0DfQkea2enAI_WvmOzYHaTQ_vkD73c9y8qkkd3UWWTEkAlgk5HHWaD-k4gRqxyWD-MmxXITUaO6O_g_2vssSnFMxGFeq8FCHNo4-JuA6YbKKNIF4FXOUNh9rLDHNybsc789tz387Iu81SQPkfgZMvYpoYpCylTNdP0Dnl9DlxZGagnMcnEfHQ5RwPHU4QHCT4jtorLmkfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRGAwJv0Dve1BAcxj79aLvnS7myUVZLRSmkL-K-beQferEcc1mGURwEhfMfiQdE-mDZhLryK-8ED6qJP-wlLhrXw0Grfl3HFG-4UEvRnsVCSHbQ2k-yLfZE3IcDWp5JUaiGI8kJVLYTw1PAy8tZBzTCIPMn1lzk0NAeMs4k1qSblzpIbV5TOUm_72SvGuJfVQwBdmpBixXOD8FRlGGR2ykstIpX7MxbKUOQoHyrIfYaQo3RN0xlHsS2NYsEcixLGjDyFkMpgsWwvtpjLJQltt6oO49Z954ru_lQE1_7lkSnNx-yp7PtWtJsggeTOrAHDQ6K7d7Yc-UvTUpwSYXNWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-nA5CKXOKPGoTdKEIvDVmhzmaSj0_rnSuATys7_-iEfLUF4tY4I4opbH0xPZvxq4zE54pfpU0D9wK6XHcpAAYIN8jk76as7259GCWbOZ4nVPry_1aO085Q8hcp8BF51Qj-W_LDtcJ5DoEqULNGuvjcSMwlIhhVqkgkHVYV4_eqVQuovIjsY1K-u1wjAVP49EFphAjWgQ2ML8xFwU8qwgjthB3xEJdqWlHYDoiGrO9PaDQ3OxN6OkNcN1DLchcpo2A-LUN366-zDe7-TbhHJle2h2_0L1a9pqIem-gpke1Nbczz4XLEGUDjVPsASkswDsdA3Iz9KB7xk_UPlGREEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqYYSZCVbg6AkdCHPpyvv7p8aj1Jnm0gNDRzMzQeMDm-SpXjjGRiVoLKSpD_oYUXkQAwFrHe1EWlkBLyruuelqCmW6J5rcC_ILagMhaDD-wjdqdit4aLjojox5Xm6nu0wSYRnEyrtG1umfFlDKRAnHNKxX7C69LGoJYCJ4Wm5IKshaIHNoMVC9viutxu9w0bgfAIwbk9nysrf-tewtQoOH4ubvays-w4KpR8l26DLzwwu8YtcgMzUvg5JDjMgvPhHb6yjoQckWc2uERUpkdBk2EFlR_2UGTxZ1EiXYBTvqipyFtNQBWFz0pYkaJOSD0lvXDbo0SEuZ2e_LwujZzC6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oflsTAsPewAoZ4sPhzd7k2XPKmeR2Q27i-QPnXk30iHXdMmGgRnBaWZC2naFDIuByFwDEN6eEdT9Tsdy3tyGiMiEHpWTkRBb-Zein_1jZijmZ8bgjxLteOJwiqHE9_DM2opT38TZ4xRjRD2hbJ3JTuNSWExgdHBk9Pk1krIy4T8xOFgDd0Yfo0CKfGLWt6BTWvvtnbDuiuXL2bv2rOMtWf3-ZWvrhICEiwABFyUtXvnIfUsrrUR4cGdb6j-tz1fbP3Qun94qGNcO3dDASjwXQVK_0nPk9Y30SbAfUxa2G6tGUqU11nxcEIjGe_844AYtERcmoCwv5AJhsn2HujhbhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=kiZgJzW5rZaZJpYZw_ep77c-K-SKs2C3dwtHyg5lwoXdVfzRmOsARH7EnPojQLpCJ5bJXrNhX7mv-lwR5Spm1_RT-7v9KJyztKtpxRedOQQghBcsTChF23-ko_yuq15gB8AjOCBoqqlgMvHypMnTuZnB4Pu58O9RHo_FynGEDnS9eNenMf9Pshu6FL368BebbryWXWfZHxsHIqAze8pJrYtfeG3Ww0Gd_CEy-IXc_N4qxGzMmGQ5ZL7TkQQY3bN87zaklVwRFtNqWgUVFHfAsCyGy7BrGMgk70kGhYhrd4E_UhO_dNirHfnh8ZaSNHgvAEQU0CoxyXoXl8ume3BJHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=kiZgJzW5rZaZJpYZw_ep77c-K-SKs2C3dwtHyg5lwoXdVfzRmOsARH7EnPojQLpCJ5bJXrNhX7mv-lwR5Spm1_RT-7v9KJyztKtpxRedOQQghBcsTChF23-ko_yuq15gB8AjOCBoqqlgMvHypMnTuZnB4Pu58O9RHo_FynGEDnS9eNenMf9Pshu6FL368BebbryWXWfZHxsHIqAze8pJrYtfeG3Ww0Gd_CEy-IXc_N4qxGzMmGQ5ZL7TkQQY3bN87zaklVwRFtNqWgUVFHfAsCyGy7BrGMgk70kGhYhrd4E_UhO_dNirHfnh8ZaSNHgvAEQU0CoxyXoXl8ume3BJHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0cvirWVXbB0i-fjBvBjJNrnFwQGs-ToEN8kYxS9Ap_oU0nnq4p_P1LrfiKVROY4WmExfsXKZ2V56N1hQIbCOf5jowNCHac6OmHP8iRZHOW8FNv3xOGFI2YgzaqTsmVT8yUSJq3yoNeqEFL5_q-nEHuG3YutMIYP1HWCJdj4oR5IF3dBmwytSoL7kpqoXcuUEhXhDS48m3pGoqUgP4kYCpn30bmXmUoZ0bRHMUfcTdc3CXFK9f3pCWUd941YzDgJtTJ4Z4MLXUOt4cMb1Eo7aT7su1HiH_H4Fzfrz0-00aPSMeoCVUOIBbtzjia2BpkLfwUcNgzpr5r695j8-MUbbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5G_5SBTvaE99z5Xm-jkgd8BGSO50ITMD93-6nuVWie1C69JlecJz5g93Zlu8lwPni08x0nr4rCFDxCxgkk68NgORNkXV6Pc327r1dPLlUjS3j5jOlHbCKOhdvEA9W6579FaFbHqatVzAHh6nSlhgl4DX5eeswIp7XfHgbPOI_82UqZYWapFgrPQip-GQY8vjeTnTjAxEaHamEWRJ30LG818YFVx_0roWtNCQxlvAM5ToNVjpzZqfD9_T-98fLZpB8hHstyVUQ2XIB-72xVXhN8LF-LeRcM4rK_P-WCbp1bypjLWgn4PoXx9XgzqaDbLZ_qYyLQODPcLhXjgy79eLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVjoCFBHORtzXIYGsOsgW4QImrzzh9MHLuPPxehMvmTlbgsswBiT0_QguTM5dZHz4Xo_iOic5jJFdf-QUPUwTaVbcv3RqTDZ-BLx8ndnET7mNNaXC6lJUk5KWGyKy-AaRRXExDwr721hcr9bzU-3l3iadqki_WopQ1R1h7jLqgMWNwp2FWMCd0Y3JBjQtD5HWGvEStxoc652zivBG7auYbkij2bb9TvlWxUoxLnXyEoB9LQz_dpy2jF0A0Q9tG2T80k0kZG1-9ODX1DL1WFjZqF961W3EAscPyXpJ60TODDO-UvEMPSYmjhk3nQHwD_JLv5OU1MrE3eQUFyMqJgBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYshF-pGcLmDtRrkmVMq4RHlO8khdqHMk2ygiy8eahUjt-ZKrvN0V5xLbUY4mbhA-CPUcF3D6HYHeh1p3YxGizKUj2B2XAU6Xhjl1LkpogdOwQj_ubjUKl4nKj0trPIlqn9SUTFYz7u4nlYd6bB8WPbVtDPTrxdL48AksEI3RR2H066zzzkloieDq4dmWD8oHwbQ2wP5X3Gljg9eOBQgDl-GrgBSOgV2gLwzwWH_WOPBHISvSwn--uLcyoYIB0z33zftxUzev4orHsptOKW6M2LILt68-vfeikZiqVrAJCMqB5LLMYmFmO4xwjg6GtsBJl33BaS-XqsiH9As0e7ZzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBD-MjQxdvhkHB5fnUS_zHdQyCX38Q3rMWsycAx1Sm74gYvv1Hcv-xEhmHTWn-25VwSqcD3QPffsZyaKa32U_p5SNTmoBT-n2FBETRCQPFTpM058L-BrvvZOmsG4uZJdkW-ts8TLYKXYws_Mvb8VQwBVrY2aD1ZC4ni7RLPtcp4TcJPet7sRJklgP2ksr1Q61UKtdZZuFK1Aj_a2kDZIVXiWuhoxdoGbdG7qyqciYgJB20Hpf5dtzZ4ya8Ajoswu4jZ2hQTne4eMBoSvOyEEc0db2Cpk-nadHFFMKP0dpA9kg5QOVmcJWyR9QqsjNj1XVL72xv_-QQz6wh7_rVpEtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUraUXNeuq0TEzkjkJYxVBt0GZCj8I_Km-BvuSfx3VKJvzeW9mLzpgKGwMZCBQ3Mj2friQ5jmOx_5hc-H-yWbA43oUFn2JQbWvFWrd61k1DwkJBnejc7jh4xaruMMz4PILUiRZ9x_BacRvs5mMfKBXhyLNVKamdJw6FUOq_uBXpYxRTVKMeeMJp_x8PiN5JLROXByG2QCKmizqfiLrNOEnaNCsmVtInVo4ppSY_3LZ08TS4Zmweo7BfUd3GdqjNHvJVHA1HzZ9R5VUkjADzFgJI9s99eBRRRj7FNtwzJbLY7VkfYxUO9GWWY4Q_BA6ig08aYslrr2EJVTCQkIRh9kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Brn_wJGmeXeyyXX6mMK2u_SsMpcT43VZ7LXkd3FR910zV5uHjm9FhXakZGX8nziZZVHPi5h-YVQv7K1A-hKjLSD4Jy3-GjOUwv6D3_eUQAJKQphrwmcUZHiJCvVpKfXwrLPQP7Dm1NpJDyGTsz8WQbsmGYYzjfI1UlLw_NARSt044Du6GUXzgDhQtvRMfjut3yNTNtcu2fPdiaEmWZaZ2JexQZ0YgCWg1FTWSsYp6efBKx0dMGagJ60ce0kF02HCt_n9ZpqqHPHteMUDyvv71VpOFbe3lqY_3XJVQz6VsfaSfNoG_iwToypCG0zNVj46frrgvEuY9U2Pe2Km84xY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2SldBR5-7KOLNwdePOpldM0CHoJn1hza5972YYqAARsOUGgsOyMo96TWske0EB3VgmdajZVDNSIyL1XgKBAo9EB32LhoE0OOhR9Vfu4qzEU-1WNpWfx5th8vwXamcdRvTDV56QmC5xEs6XCLaGzSiYLPnqnkN7Ls-ffSYd1AYatZzOTs5T7VZf_gjwZEU6Ttrde2NxnK4MJhBOPFt4XJlVCjpmRfVr8n8Iila8A7pPlNbFStmUVvFsgm8kI4zsIl28de9gS_fTcyA7LzWfbUF4ijw1zrQMidfMkonVo-2eeQhkr5jX7nXzzSWQulrTOB7TfnojC-2bUN0Rsv0QUAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7S1f_EC7QWNAGl1fGvbmxGebFujZAK1ZegcZVzRFd87RDfEpGQ3aQQwcuzBePdY7XgWFi_7WaUcX5yXex8aQfqqil8hGQlH0G1Px7YwlPM92KxgVnk7yIXd_6OM3iEGdKqhhRjLbg0ergiwOvskY84LfYhEUswYcW86YTR5lyrMiWTTo21Obr6rGnhrJTqW7lYqd-F5Umv7jwChZl3nFPBj5QU4ewNm7_F2f-wHbDroX46YGOoIU_fNL_jngLQPmNx3Tau-_wZmuam2qwH_7Dc8QsbyKcxBeMeExYGDs6FKC2ZdLai8prCzExVdGL0b4v_q3QcFG52T3dqeq1geSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAXpvU26r51_OwIwW5utBv1agRHndPIsTDsD_UUUKAYiiNDkQzmXr9czntMP36yXlAPk1KEmuyPcPBxu8vAXAzMlnu022YzUYynUcZyaAHoifW7G-V0bt4-u7lPRO5mRKMns_HdooXDsTbRHjn-pnHRLtVm4dXeYX1QvHPElCVIbWeYZpYAZ-FcbWNbtK9RyckgUpEMg7kuoIoJnvF6hKNa4G7dtUrpKPLiDFhU26VEXgxefpT7g-46iFIpmbDlcsSfYj9x3tBpFJzwuK7QT9oi9XPcmhhn1sToI-PIHd5e2l-Gi77uxfom-JHGgvVilx8XvZBBY6HwpNKUcg6Fe1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKgBjYHluQagG0YCXniufb7QLmGubK3J1STUKKzhrml4qYLtYXtGlhMEGFLmPxnXW7cAlkEgI9mEEaoRM9acupx23xSfJd8DPyNpyyZAEMxFLrDa1jCsnJDKX8TjRQpMjsfYlz6buCtc6rwmvtnRaePi-Y4tTApUaPXqCOUcJOECubU6W_8rYVDzGwfaxBtkTwawk61r380JRTSyDcEkWqzWELplx7toSU416OXrAsMqKR72-vkz7fEq2Gnr0rgbNRotOHzpyy2hc7wD1NZc2nDGXuNO9S6nX72QFlJjFWYelDPJZTnqFqPPsywGeGK41SpXyll4CGijcJJV2YxuyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOqY09Z4Ln_7US2veMZ9pX4vLhhuqUFOeUIA2myD2GAX9x6XKptp2rrCocq46NowU1laYKgXVHxnNkawX8lKwGfo8kV3JJYZqz9Ifj1ScE2HkEIdkqV2KJcXt8l17g--XFN4dIBXI1CAAFD-6z4a68zn47ViAlqN1oU_WzcDtObw_Oicl1qgijoF1B3_8JEOu_FkRe7Vt21U8TPoJgvZas1fOcxfn730BYxzQ_xLe3WPROhGYrowcjHLSgtx2aobK_4HOSoHG-uw6BDd84X4qy2nMAw1y3kv5IcXCTJiUvcYNlRXiZfai0JoL7WTMcD1sLdKIXL4cyk5-6-7Y4IAWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKL3RKKmIry5OgGJZxOa8zx294p1uqU_e6AxIffz9pjG9o_R6lS7TMS4P6loZJwZmVuI_7og3urPecvTkkTnEM_vOlNwpy3oD9HfyHblbkcbuJalhbGrgaQdivtATxuzrn8LieTV6orv8MyskAqn6aa3sRVcG3j_Qzuf78K7eNM80Yifn4rqIPgg_65nDpvvmPTTM36TPxjHcxuubsdWyre803gYX1w9Q8e6pArAuuHUwadn5C6mLQ98rxJBFxbRaMRxKzZCQMuZdxZCjQ3uxADn2r51vhUuo5UtWS_lrSxJa0o0obx2HSfoRIQVF2Tn6uSp3NLZDhkVfyqdJSBEuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brMbA1fnPoAXTxb19exkeSRrBsGGkB4mUPY4BVOP9BlimPJx4N5vUWtUThbEFnT_Lbf4WFSiZUanU8DOUPlujspX1ZYW6dFanhXqwHRe7l1_IMHf_P6dX5VLpr2ajcfga3IV69JWlQHcQUzzHlx_hm4770T_bKQ6ws49ASCLkQsUHNjhsxF-iIX9Lb35C2zTIsl43denuSOFjZMkO0_VB1BOQ-9ASfXQgiYOyHDIVuPQc-o2PKm53I96SkqlU-1ncC8bLI78myVx1TGjRZgMorpWd5PoVFOjkbKAo3ciUOeYHKBhS2Bs5aIojPnzpD02fvLoOjCX8VZJBf3v3goMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTl2NmagT9DT6ceYt4OuxMQL9Ji1NI3cBvm3Kgp3feh_r82xLi-OHvxND-_PrS6BRvAbnnCbitHR_kn4JjSPsHitX7Z7t9-iImqvwJLVnbDoVLTN_COwqrKByLCacicMII6omLIqbrX8PNW4CeeHBO3XX_To4ivqGtdJk3yxyWDdlwQWzdqlxDcQs0v9GZekAxm5mc1HPjDt2IAbzIuG_hwDpRx1NkOimzBYASU_gY3czmaHLfVXiTNgh0eDvSbG4SLS6rfi6c8XAmNZZ6Mieir7RlMOGLKfPDeIocXfZr7LMkvu2XVHB7K1K40CPnARtFFLuldYmBFG3IqTppoySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eA4Ad-jll8GUyQOEFgiGqbKV7yhVGqwYjGKpwCJIxl1VHHt4HfqfQqDIhyQx2HwXrHh8TQOl7mpHblLlh9kGQDoUf1jqeQKf4OtmW9G8MVbi6BBRSTvGor3Rfl-DLcZDjOO4nKL5zvgiFxsdiBB5BrTJUKw1Dn0vEbdUOI326HUc7vR2eIpdBlgxoSU8eICkvYyFauu0J366rj2nDF2UWpU2-h9X9Sj900NTLteK8taNPJx8tQjOWY5-NgkoM7cz9VnnSPZedvkuVUx25p8JzT5CFABeutVjiwtqI5aWwhKu3-Mm_bTpDNmvimZdOz4kXUD5M0xrXebE6r3GCpTkLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpIlvwqP8Kd-0Y9t_VrZZNdxvpnKPmj5lpWyA_BajkWJWbFMZYqlcYMcTVlK0ikxJnXp6UHE4BsaoUAdxzzuZgDHMlLCofWq85HNLZHUPLZz-_XA5SK0fOFmkDLiAyxESTSoJzRCEJ8GRp-bhme3LjpVGrf5MjvulSAZoX0qjf26CT70epC_qKDaKkVuuGUOyTsNRBHmHrzQjOn81E-uTOHivnBWxlARd-5d2H12ZEgP3zzeAZFDjxNI_TyL1Y_BzGWcDmbg4hCr6h_rkOrMKZ5gf7eaP-lkdBVXQG9KY6zDIHA4GicO84-E92NElNlWdb4G8XtKxV5kX-0_D7cXfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPQYcWr93TPysr8MxT0kQS6f_RyhXbIeKRdxM6zF7cIVBZCGp0LDFOC-qe_5Gyt-lYE9-ijjPu8Bnp-bS5MjCfy5kH0PbuD-TO6Cy633sqzK9Qi0-dZa-X42cPXcdk4nhCIbZo_phND6QykaBkvXi4ERNbDWVBiEkx3-V7z6_evJjTjSRN6Wrd-NaqNXiNlgiy3eAaidW5fhLn7v_mEipn7FR1_pd9sjzbZq-JBkD67wpOdfzod8qrpLRhmm0ZefPI0FDcHdnDCu-IlCqGjhuHCxj_qG9fLPqO40iVTQdsE-ohhM2a9ccwKlAYoT06YtlrTnaimJ9M_zw_Zk_4EI9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwT0FkwzDB1oq2TSLTd3jQDySBItipKijHpzoz4H2z_TJ-VSjvRz6QAKiFCLkKbRVftrKLnFVobZajSQy3fX6f20vtLyNa-_TMTnsnPN3InPUJnAokpQvcERQLDywouryjORi8sKOQHi6Bf_zg8DXMszhQtlFPQ6IVL1GRkqNC9K_JDstNsOGbMbn_e5EUcs5utIUsxgkNa8fQG4jpyyJVEbT21xQzkC0Zla24tM30E1jUVRqZy13TM0IUiv3ACrAR0_0UWWELg690GfYZxtBhkpH8YXrHwJdkod_a03xaIatLxZgI_Jnns3csF14fxb8CSFOcl229a3q1hZwS7vqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFItOpDltjj0f2y7B09BPObeluGH_jKVzbU-PWVbeGhHUzFQyXkxoTZqMHMTtYV_BqflBx7Cav974b5IMMCuwCZIHqX0ibxGV7lY1CkzizELAvMDyAFXBRNMifInrfFHVkXH9WfICITNjBWMhMqrLZ9xA3D7WbjurTJr1vNzcQW10PNdB3_nFa-OUFKu9SEABkiLQVgKjy4blWH6Kq2UfpHZ2mwC1ooTsB4ZpSFZgqj_jTWVdtZDhTRMnFmP5eQ6_Zr5pzgXC1GjdsPuylcvHoH4qjUh3A9OV3Y1PtE2399kKYOewijETF1sdDJI4o3_OEpYZNjdlNiMYiOGxuNLeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECSrdkrSX70aB_yoH4rpnxGf5qOONzQyk3TfwDMuDF17JKutrfU8u2i77l0WQOPocNBGnljljAC2mOdWDeC4glb81P6ouc8XTqfmlV86C37wmtTLIY6O7P3nOkw6TFOl-pqlIBiY3xkzzoyxoAyuUuDFL9Q6sKHySVZ3RYIrHRa4nh_GvXc4yrZcHWu9s1T_8uKnEnuvIAZNYU-K4bYKIJ50mez1UT_YoiuZu4j48YnQgHoninwAfwd4B21RJYo7BhmGTolpEVX8HJATV-DlPieAMLeig4Aw0X3s_g9hTgiPtXhHzmzuLctpp7f-h4hELENMjmIHA410tv_MqWAIyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIcCP9qkg3tr_AbrlSeGLjBVaAzwvnENB3m5bKPBondLjA7xTzXgoAUpa6l35UrmsfI9LLS_suKA_EBtuvIHrpN5dFIiRWuzDmbvn86QDWVewvT1y4Mb3X7WoK417c5iXiJcpBw7geEme1UNCslpEk430kj1oqJK2s4uyXaamj_TYvvqIX0mfs3Ijv0pWwkRi79fS5hMYqQTwtUbmCti1sJ9El9xJUgzJTQn48Xq6qBvEPnRV-L3DhCoTVmqZ_fcCeTzjiCwnlkp3MYoow0IMdWsLVde0GOXJZK_NEUiKbuj-VNlsfBEGWcPBks_YgDl1ug7V0lJgXVxyFPjUm5ndg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMHQEF1WWJvVIba134bBYWuEEoItSNuohN8Rt48Jy7-8JMy3Q0xpjsP0F_WswXkKPwBDC6C_cid948U3GA9nDU7MLh4C5LEePpy6YBuRYlJGbJydwwt7UE23dm3_VsL_quygX-RUTNr9k1g0DEXu9Gu9inPB1aAov5VSKbGU46VfKCYLsjDDCmcl3Q_I-Fw8j8sdKlyTi0Xt-6J5Rhmgx0_wa_-2Kt65qKGknAWByqqx1tnxWyPkDgRF2JXsmLLCvQZR-JUI8E6223DY_8Nl067NqsJ7-j4P1c6OEB1q09CVBWYc-xyNTUZ7ZC6cppEZyfRH2GYeWMmXXmAnufFd-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIRXmxWzeGVra1A5kDrGvdEEvDU5x436HzC3qkYk4dWLgnYTLlxq0XiHFFWz1T-hPzPJJPQCcVhXpu8OQGi4LsNHkb8VvKl5qLcA5TG2cRwBy_JOjfNB4vvJ46nLsHNaHkt5VYSZogpWikjnl9a4KzV0Q9pEyeojHv2Y3IXlGxE4PECfZXr9vDrvPnWxMj7NwRRVo5-Y4HWR2pTgAaXjOJtvqdk8gSTpst0dpV9mq-JVeLGiZQCa6yI0xL3yi_O-ycHGcnRsZftsRIXC008uvV4j2sAnzrOmpur93Xd5Fbajx3r8iT6TBMp4_s_rVZClgNtspoKHKHW5h2upDkVI9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBCrO01yGCRj5gsWTTJYOt8hc-9t2D0OTxnXvn7PLf9rwAmazwK-C4D8xopIjpDl5mLck6VgyhZlEiO8XJiEhn6iTjEvc6bwQe2bXjajMJwJ77dvdhNnEseih2dvyqaqyChBxDiit1GNM_rjiZGV3TlEwb0HrueK8OiauiyvfjEmiLm-gLtKgXv-Wu7tjl7mIouc4xrRlDs8MJaF-xSxa5_PdvPUhO0OCxCbuUXt6RmKtnXi06_CoELPJa2PbbarU_GqBQSM9axKfk2XNMpPtLgVE9RalfQuZ2niJYduLCOMcyTBY6DicHDt4_Phl7EdeXUW42P-vl3Z5z7DQXmPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrBAkLMv4K8BsFUqQqQjRROAHTxL7wndWdSx1I7h5o2YNmroWIsadQGPC7AUdLbmj92hzR696AhkiiS44QavwvhDMcYW1Q1_xStlyEtbsDH6RfZEpm_prdwuybdEinKng3P-kzj9SklvKLZYMHQ7JUyt3xSeUA8kD01-boyVDe-FOD_mROiGM2q8vDS8WTc4-IjErvLUmGkROXW7bApFSuqH0IAc5fxQIZe0rQavN9PBW7F-XbVt5S7g7oV1T9_QUItZ1sGB1av_wLp6EPjuF4fqHnbHZMcqbupH7lmeIFl5e0dvhkg96rYwM85abxG1hrQuEhWwHSyql7PDiXzbVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkVmbsRPkainwEXX0CRgXX4vmVqjYANqbVKQaeoWN9HJpSjgs6GJqO7lSrJ_mAloo7QnCQAvV77lGTQmihGjvJKT92rIALYiB76Lbu5cmr0j7IYTOkDZNWORTEC4Df-CvdV9ewktPu6TCeCN_pvDbPzM3NRUSr9ariAGKZUPydWKQUxAtllxogInYvc87-X6Sjam10WSR5Tz5Y7xtHo_397wffwXj1-gGNtTVwVwImqc5r4AtX-jPk7pXYSFh692zWz8pK1tzRIZX_ihCtQBcQsVOTmxRWt3V8TRLtF6DkApwkpZU6d44NSjz-Z54NueLLZSr70FmPMJW71GZsO0Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZHT1J87FmJOqKub14-DnNTF3DI9LD7k0wX5WfHx2zEeOXRo11zULpqo7nJhNgDjJC_a-pJqkQJi727LJQ9ozzfnGwKqbYSKfqUjsgGUZMJgHsnafCay_RhTPCYVJ_uOb9TWZyRo4WZQJDEkebxCqahrlaPfUKUR7lDFCNulAVWYwa1GPUdMvBgRVL4Hdsfb7uYc6Hf5X3jP7lZY88oJCAonhOkIjOv6j3vzl1el8AGXN6eAUxixxP_L2YUW5GM2h-Mtd4sAkhbjLn0jGQKLOn1POtdc7_nKGy9gekq9tdTKUNLbQsHBavQKIiSbmtBtUPBLcwYLwxUUH2JWNFC3vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYktQrIuE01CV4K3kPw0EMma9heY1xXn6rwxPjYYD_acH9ZYumipiAZmdoxFROvmc92210Ni6wznjMHnLVg2i73wu49i3lVI5NqBmP0M_xt9yvP9ZmO3hxR_Hqxp7JJqPPHzMhRV3lCyE9KZgrt5opsT5LFb2xqa7k4kpfZ_dYIA-alHdT8_NWyHNDIW7soO6agntH9Ymi_rwZDNM_aXFjULs6BlcKfkmKIFBwjqnMz7mvlA92qnwbFrFDsAbTK0sXqjs9hkX-2zbdNhJavTRr9vpOuHPDHjJ96N4CjRqKwq_6Y0vrhlNsOl2AgPgWN1bIMVY4j4vRzMMi2E5Kw9Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjzgyW1aiwtShnx4qEnarsaCLd5TcDk3QKxEPKz0aaV1sc8bgPawJvEjjPiWNDRiZxIQtwOaToByaa45uLM6_Y4AdRIlqC_j-qrzoBoNpOLc2uWCHcD6vUBW1NEfZmLKYtRsgYBaHwmQXwPcVnA55RUTJtNdfEaMfjFmpZW6Ep764JKA5Ox-I1pop4rLRDwZnGabELtv8pHFHrsjO5ylwKTDCIgqKL0EdlSJPqkvlGrQtf0flMiKs3J_Ixntg-Lt3aNmdt9lBRxCeMGELmKVFM0hMTMi5Hm8fHzeuoNQTL4zogw9r32TqPZ2-mRUFNiKIpvr1EfI0GXejCSKjDBTKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rewTnb-gXN_umjQxuH5HmAa6qLCRtWKSKLfVjQXdQaC3PCn5ssQPlInLSRA_0Hcl9gWk2onLhFQe_QpcPQpjKwu8DfFJCJqT89GWALvIxONYX1hCzDzwuhM-A3P9UR96Ch6hakWwIVuUER8fyBVO36W_r_G0M4wWzH_TEzQxKy26uDAwLqqXiN8MvjHpDGvO9L8kdENFK_UOARbDjBtizEtsdyP-fpDolYOShoN9nC4fgVpKGb0Z9pgza4qOabCnWTXml36bd_AZ207f-RWkzSHXcfAWYweVz-lxcfXbUxqOhJh__kX7-XSxpv58LbivkwHkt7auKcuX7pmPjsGwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGL_ZlDr3EYDKVo2urTNhhNfasWxTgA-yHVb7TvxsRfaW37CCm2oUQq1fie1Z5CPQ7vOFqWF5vzSmfYgNGdGxrkGSqNCKrosyniDiTUwKUz_yRSPb29kIjtasgEi1RfVPqJtKcuhiP4gTHWHe9ClyXxxnEp5IXsOncSrfztWNEx95O1E_xPB0FHkHYIR3FCTt2MxCjRxHjdMa8L9bxDYWwfqSbDO6LmfiUgRVUNjczF9_PMoXQ6RG6hA0P4HePmM1AeYuCuiNisP_F8oA4dyfrO23qgTLWr2K3xFa6SJvbrh-NvGAtwXtEDKunxIQjEXVoQ_PGPoY8_64eLXoTD_4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vr9TZzck4MX9een7fcvsOAD43eN6HRIcqru-mjInXKJ4-YWrwMbz7VLWNFlTbAAJeH0Q5qwboLf4p77h5VhsckSVdXyGPBs4rPYPuQUiopcLzgJyL3Y7hyuPeEzSEQ5NRmEVtJ9MtF8AeN3RIVlaFAJShQ5g3jCg8RWl86EMY7u-9Q2ksg3ZvsKykrNLEiH8OzKRGLpGlozAw46A83o4XD2GSL6ehT1UVPj6-yXRpOsYFkK2ZqDglWlTWDR4GJKaDZPOHPEzGIEQpnylDqgoj47pelVbDuYCefb6Epcj-pTwgh_f3T2_vv5CdQW6iL1pcqpIfRJhPCuUAwqeQ-jvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCor56oyjy2dq55Yt-uc2kb0RvwOnKR1gIl8uylVmNWs4zEC7ptLrbRA6Sto8jHpCity14d0zk3wG2cE1QLtG2Ec6DTQXDU4kx4EHbn54kUaaT53bmUmQkwB_60vW5TKpSN1ML-4etwXo_7_KMG8BfsuoDFsC81cO5gQrRw1U_pHKBvDZbqggzI--M92_FIOYkxnKwwhOX0ps6qDE904G9d7kJT6Vy3AyDRV3Itb_h__Jxvc3uMlDyOv8rHSjjXGUnAyukil4c2oa3rSpcxZOOgsGDoxWB-G9ePyTZziJnm95CY6gF0857BcrSPuzhdznjjJSUzve31EU8wgOLkF_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7kuIPir9yG09_3ydYidFBxXgH-kRqmmffWxUL4wG-JdaYoJ5TPyAAKh9Mklqa0jtfT0sfeR0Pi6kp-xJ2Aqz_Z_o3_txVW-UjKzpAxFGB0i5cNyaO8sgVybWcqpDzle-0E8CWlj288lujD8vmL-ixZ9eInz4Lq1USvhiDM-TZyL1Emwv16y6Ow9Ov-Lb1LgDb2CfNHnYiO-02y-lCUy8ZJDmA9vK13ZKdUOdeXypIZDaw8yvSRtZSSTuFMYThhdgLXsF5enV9DlOjpbdN6gSXZ2KKnYpNOE438_4gKOZs1HrWoLl470TXvrOm9jhQzfgX5WtZXClTopSowXBbNQuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ol81r-BZ3Dinz253OF9d1FITLGhj5MYvLQk8n7vXf1pyhLPDncp4KnxhRiSvWQRDAJDvRY_St0KguJmgnSjHI2l-C4H7Xu_YxOCmB8bx5e6RVltJX4zsTSR0WVpinXZcLRkFput3rR_cHJJaL4U5KnRQrohb5Wwpr6oHarzC8xYWv87Wure3TWyH0L6wXGlbYRN3KqF1nnOFNGnLQBaAtjBE0H0ZOzVf1W3MKLPpSQ8opjDimaCTT20pA_U0hXTjq6j0nCLpVku0SoYYkd5j37yUS1SeqsMbrZscXT_Mw3KJA5xfWUWkkD8Hx6eZH4HMPFTzvT_eVK7ZrMbgTu-g3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dl1_aUV4CB7kM0vd0Iu-8jw2Czlws46GllD3RcmoYnXt1UvJPezEKr-I62aKRRpuPsJDvRohgkzx4tox38p3vcThIPrMNUxWAmAH4ivfoYh7JE6x41wTlBt91aYnjB5LxurtshLl5F90S9MRGDLuO98LAFlFfAyIxHdXsB83jRr_zZibU2M4WnM681T5iX8nkPh7tvWLNsBQMtd3VrHYG-fMlAd7GtflRG84DFFcGezwtq7XYMK62ANYdsuvgMO5vaIF4AlkCL7FzTDTORbTU9pgQ_Xau8WLOiFr9rCpNnjZtIBd5hRTPtVkuMDNltuGwwzeDe5JL9k7hifL5o9YvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqshOAyM2jS_e6_hQBnehIbGA84wwMiNYgFSqAeWtQRFTrTzjdSWRy-v_IdDY2a60WCenODobIfw-1TYP0cZ-Wb0gji808Z0Fo4dg88hMqq1JTYrzqx4xriFBwZbSGHW7GYjkZI8p549PFiTNENb3vhkUBGF_5D9aui0Ja8AkLDR3RFq0MTnjWicSYqly59nEplpOkM-wta7swK74tHkbnxmtnsAOO1s1V3HqcFQzfuTufgz9VQlTCMU2hcxMlXXFgcBHxbmFWqkR7DinjCnTZWzZDinSvHRkDOAfJOPJifASCg8msMA62cp9qhxcsABQ4vYZlgwjy2WXhvLghQ43Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xwmaitjy7X_ImYMJBwQbS8rnm1_e8FgrPM71LkUxi_GXgzNYrAF3cHkCAkq8kfUx45bQwNT1rs13ohbry42Cv0WwB3OBUQsghNbmWZJ3GjsPFWbtBqoU0mJ1NB8JMBxeDOUqNQbVzVT6Oe1_1FMkxz5XfoO8vfVN5VdsuA0Vc6sfebi_TAUuPo8JMe3lEwbvBO0fTl2MBWRd9j5txSgOoBVrrFJae7hL2V0Wd6tkgyJP-d-zKGYsI7XkN_CDEaAF8tC4309GONbtbYBNsePeiBOn7vSCh6gMMebO-nJnC6RUzDYAVwEvqeQ_D8Vj9GJa7Kr10w2KyhxPgsKnuz7f6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS27pEmOtUF2euzD4ZsEO2q5gMzg7xZEGrE6yj6aQ0o4mypZZZiAfxZlkpvcWVM9dNg6s16Z2PZUla8ZdKnu3T28oen0tFJ05j-vmoAquHN5xCngfYot4i-DbfMIV4xNXo11IQ36ux_2AblbIPIZtTzeUMe1fxB1AIy7cKZpiVhzAGF0ZBVBIc00fAtFr9dvBQhE4kxxoQW9IcYBIYFxvt_ocyktO1i8UJelLSF83az0m5aaOdFRTGR9Ym8P0Ysoo8fIa1lToVA7uM9iyriqQY_Vi7ImlnsmQ_KCKbaV1BRDAh-fwEhx7BAlW6K44Wup9zjzWrNauo6T6fvuc2EM1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c68kojpTXS7ljlpU1ngPJeMp83eylmDvTHd93LfdFZ44rNXi8J_qMlnlDnLJ9AOJjFQY9Bk2OBnRgGHiL2PBOIkij7ZWMbCzJ8htzo-CZIqR11VgBnB4AaVif0_r-rbr-4ZhTxjiLGOFjxSo_H4Q5ElVaDtxRY7lYGbpK-ejUDjIOqzMQc8Pi75OhVwkZRFWaR85qK9hE3_zNVlWgmnGkZwBa1aHFz03WAAazJ1R9KbFA9jo3aO4WBODjM2_UZj9O-1M7A7yydWCYwoE2ipiXlV4h2AZKMYYIFlynYxs408oOS4GTMg0Ssob2HJH1yzJJ-2aqPDQOSMNfJ0OFADg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfwThF5Fn4iEuwYenQVrMbVHRW4pgk8HmAj5Dw0HlkmJGafeataKtbM4yv6g-VhvxRkYN9GJxyrbZCKuvameKUYKfD62iTFq1SAQk-NtgG22JSB_DhlUmAzGICStRGtCA-4BUj8SmUCozc78ZlHULGx2JtPGTIbgJUbgQDGAmrttkniifdHgbpsYohaAU8W_tbl56iLdfGKJ1WYQcvGfmDa_paXLgEHNvjyqgX1gpURq4NJBq8IjrDccs1vaKcBEgTm19za4-jxDVQqrqKE09afOWwx8BEioluUpb1hth_QRQe7VGyDsYwoTdUOF7EWDyB-fZO2gpNbMRsa5wf1M-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1jh67kuCvu5Ek6G3-JjvMCYUCYSyYVAwGwHhkSPRZq7gghPv5UU8ucVnEAPcUbg11ISj16KmGfzeAxipw8qmMa21_3JJ09mFXsk_ZxUgoAhL_keLZ5ZuhFW4lF30veJfB-lr1cTC7XEg6-SvACiDEBlEUPWOKNM46zSS0oMLx9R-V1-ky5p9dJlTYBLYM9PcEJXi5BSbJ-JoaLJ3YzvAMXZhosgBbd6ipmrObK_PpieQ8qA9ri_Z3iGMAYCA34xyFesFUbGqCXxY6X_ny8QwFDh1RQvoTegORn9C2WeWJk1-9EYJW1TKMsk3Qd6J83SikurW5iJ6HNOLQjxkq2udQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaRCHFlC-myBYzqmKCiXllFh_apaYAJlQ_iEUKXyx_CQhwL2jIxqO8vxDRJ-6DTUAtj0shgpk8qCCo_a0_cl4SXXpPYFSEG2xutMU_sr0KnLfocrpsNgYMq_fFVtIfLDGoEQaGLs5qCcRUvqloqugATHlgAvqBMWZU2FmV-ibJDcm19F8Xk2FfMEUJ-tY1vPvP4YBgwAq84nuzfYSXffiiKgG0EKud59XDlAVkqhzkp8GZEbTXyb7RUCWzZpI9nQSYTAoCEf8sYr93N8h4Y5d4TdRWlPzPi5UiH7gBj2a03Q0BgkINJtJIgKofJRcCG6txG4Ht5rQQ_D0D-UWVY-DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQMCaUQczn98M46EUBGSn7PSaDsD1d4SorWe_O-ldZG_5cnn2hfr-sgONuJTiFPT0UKEEeBrl1_HoodCA-RTXTYrFOf1c0Hx4xvNf_gTLEeug1EsrqutOapgfVb9vQbFDre3vJ4JxRPS3rknn3JCD7LMT3xIjYBbZzE7tHE7mCN9HOFl6lVX9c7Jp6zw1SX6CzFtbPdI7Zfol8dO4XLp3A0q9NqNVHrIhS6qx00vrrA5Rszm3v80iH7r8alTRhmx6k3-5KrFXW_oRd1EowHXp6DiS7fACKAh6fRmoUCld3rNTrNNNP_AU2lSi0wkWVem2vP2NDmtqS1UQuS4gP63eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eoj8eyuHNF6NfKMGtzo9Tr7MGjyoxOeygcAlSid0wRe8R7Ri3Xv2gPO8UB0kcgWi0lzi_MHeCnsXXtolixGkSrbrwOtohCyJdpNCXqIA-vlmi31-7SJMZcf-t9jsI0fpNPwmGfEy5qMgY3Er0EoTAw5sBA79O1nLhsPDBhYh45EQIrOC2c__ICKkcik1p0lYRwrgLQTgtQoGB8WfdR5b-WfVVt2klmfHCvUOWFdd09aoLMiRn_tY-gL-cpuyw4_udyhYWnnYRLNQuirKwrGu7vrjmT1x0FtXqDfpTOXHSICdkk0fd8BpaVR27iB8g55m5LRtxBPfFUjz_-znVsm03A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qD5948DalGSAeyd5NDt640fF61C_1ixh3rQacrmttjS6tVD7QdDYeJilMd_MuTFrPdo9Ed4uiD2gE-8zHLLpk0TZmOpt-OENf7H19us2n1-3o_xDmGu58r4yvIFMV-lvy7FtyucqjIa0kdkm5dVNPjBtlWH5b2tRsLBOSZ2VAiYB2m_QbfLEDPpoVAoh5kKk_IO7MjkLg8cSONPE7D1n-h6uxMYYo6f6Q5IyOC4P1yAZlWJpSWcm9G782TbcWbb0J31ey1qlgdSpxJ35EtHjXKXci9uKGC3e6WVGinCRdDyqr3KKfAOcsDDjIxRRyBBvA3FDGO05WmWGOwZwTOWuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qD5948DalGSAeyd5NDt640fF61C_1ixh3rQacrmttjS6tVD7QdDYeJilMd_MuTFrPdo9Ed4uiD2gE-8zHLLpk0TZmOpt-OENf7H19us2n1-3o_xDmGu58r4yvIFMV-lvy7FtyucqjIa0kdkm5dVNPjBtlWH5b2tRsLBOSZ2VAiYB2m_QbfLEDPpoVAoh5kKk_IO7MjkLg8cSONPE7D1n-h6uxMYYo6f6Q5IyOC4P1yAZlWJpSWcm9G782TbcWbb0J31ey1qlgdSpxJ35EtHjXKXci9uKGC3e6WVGinCRdDyqr3KKfAOcsDDjIxRRyBBvA3FDGO05WmWGOwZwTOWuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa4O3ocfPk7HVgSvoI6Junm3Ti1-ywfeIBFWMxw52tVvcJSwfG3Tybfyc5GNWe2-kihPFUacy7z0220l5SD5R1kPKU7NAH3BFrzCpC8-2WXo3K9UZCn0O_HU1S-QVWibBIV1ZA88KVvd_44WIujycoB-TjTQAHy1n2nH8YAObz-A2mmRLIYoj9Y1nNyYaW5XRp9t1goB3OQ8GTjfyyYuUI0HyRpf20C4YftRbgQ6AtoI6N9Uf2I_Op-HNR7XYOtyaMMxQEzP8QocXE78HEM5mFHIWyde1NIEu7zGznz7JjcvMRHOgm4UAi4R9NF5-huvMCFE24IaSKU6lx5sW_Btxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuMzTv2FqUV_Hd94WFydS-bjRWRbEvNUw46LjEuYjfmzFk9VVn7Eiz66SYEepu-8kbFTmp9-lyjOREG2dadTc8oE7TVHUk56optEeKWGJvo7adjZ5-NfHwCdsfSJy97RzVJu89brQolaatXep4Lk3gN6legLiB1O1l-3QFtv13bC8nQPOX7aXO8znAQ7TBpEVQ8trxltxmu6UfLzUKAZXfSjdGKx5r-tvWpip3ih4fMMzpi5-igtInvcokhUSG9_SS86gkH0QOrB6SD3QsThox9kLEUU-nJa9uTF_oaqmo--CFDju6yLL5jcUca35NdJoewCCRnd1XgTPz3sUa5hyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lspZMMHY6UMWI4u6ajInUoknOfFbxKNW25ZYNUvJCPM_ueXQE6ZYFoj_7QKR69yGkGzYunOOSV3Kq9HXneIbavXjaJRm1Dke9BBt9ghmMSor-34DLxmopPXN1vKjO913rQe51lUQIcUc6j-OkfPFNyx77YilGYMPUUuB_Uw_TJIchnu9so1HWH0xUw1qoLOtQ61thzdA1-jf_jhhKM01ur5-8B9J3ShNJHpjSI8KB1U8ek28eUu4ZTGl7SIJDTrg-ktLR6Gx4Ua8J2vn9UgYpo3A4wQOfsMYE7BsGlHx0IhmB7LOXyI23pNKdOhy9l-jCtRWbALikqA47yOvmaBeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emDU7-wt4zh1MCMDbWaEA9cog0vukwJL7Mh3jQv6l8_hJzRJyIGXH-n5duxr1TqBSPQ60qkBdEvVpvyutD4KyltcwvphZKLdB2p1gpTJaX_Yaw4eBMKt05c0GXqwPrOrtehhUoprDSA870AJgWozIdxVdExlB5PT4li5Bg2Io0heeQTS26aOASxSS27b5dH37sWvqbqzEMic-caitfCXrtuga0zJIG_AaWBkvxic-tCiIYKLtWSqsLVkd-G9LaXwCUaHAUPCpbm6ePw9C6GBeRXtCAJYMm_RcQcjweEtfCWcmpHQR1gjdniJBP8RAityCv6T6THiXPbGxJ_T88ARHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHgeqDMc9XDe5X4HzPB73vLaB4pCugQdWjucBYRQRHdL10XRY70TpN3EQqRbzQu4IuOs-vMohfvK45PMUQ6WRBP8depGRiVayXzpQSQ3W9XRGZgosSbWj8tg_cw28K7L21pKRkJDnEALjJlawZ2cQrQszgKfEImyN11eR1YSYSik3gharQPSfICmUN6s9mbGpD_roDZKomaQNDEPtlJDC9xk_EFQhnpw7PESdEqkNkLcsrh3oHT-s3vHISEFGDNlb6g_6Z_QmoA6kYlPaRXvOZKv5mDw2moxc9WkWirBlNC2F0SOB2IPxcEn0EV24wf9F_Fuiv_F0VVTTuqS-23UeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYWDmAXXo_KjO-V_iOLQw_P94Bs_5NcVwLKwv-RLhai3jkFNdEEi2i8gUjS4KDWBQTZRx6ag7rCBb6qUqfZ5FItGIQrIvTVq9q5Azu0eVbe9sS4xp1bZZNNfUdJ_T4_fSdNItmpa9X_3IocVDCwYSWmWNGU8Rsf1HxnVSMtBhtqm0mEL6brihbUzWRU3JMS9U9yZRhBqgzz5YJi7LjFaG2ICaKdg-cukDdYuwrrkrk7HL3v_4PZaf6LAG-EYYh-KDRB8RewYnNOsxZEpjVUDDI8veIQN1wcb5_GrNms0oRcEYzdkRWTZXyGgxchKqssb_gSP2NPHEFVdk8zu7k7bCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Of75FT7T-4gCXer67nk9Z4CqulzlddKavNLlv8-eJtEvF68qqUycJnHyQZS8GveHIXQym6IXTqgo8m3Yz9MiI5F8eRUhwlu8i3YoisdWaNaVO5Y1HqW9BBYh7HkZoj4WYbyqbxEPaoVM4G7hnLF38cc1MJMh4FMouPS5gDwFflgy94sm-4Zon6zArrti-D5wFed48eS4QD_EAXToMc33ULPaAfN3DsxO23sD70UcU-y9gVi4LWbrN9ymlOH_lXI7uen0nIxZlSECCjsOt0Pu5TInXW6msBS1ozPKwT6rNKwBR06PKuk49w8Uzfq48o1OZWqTd3qWtY8g4avyQIyH-Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=HLAD1-quzkQMIxyNe6Y7VKLY_y95C3edzioQZJGcZnTGOFW1l1GHIUfHNKVoiQ1A334CHznW6mGOCNRJzAcCuZ65EEHRNKAaGzLC9v2Dv_VyZYa3iIVdkrUkwJJZA5C6YfjCAaGwG1EwVHJj8qKGKzy6uBFo7oZuwDEaVCS_QJFHg6cDi-lpQk0wv43ARh4LObbLzlK_J1L8tWZ89c9qzCiCRb_6iroAmvssqysB25AZrKBXuPCJubx8EyuS7uucZqtn4CBxVab1VnQOL3TLAcTdxZ_R5Haz7iH5gLfQcMCFWxXDtRNtDdR0AeUURn7lwZgqypNTDNanG9wD2v31QH4KbtemLDTkhxEL2hqGYAMBN0gcEZKKNU33vv5CZZUMDRJ9-f-PWgCvsMT9sT0BiarlXH5yPM_xlxZUdZsa-A3p8RHpgJ1hT98ukggtA2LdGxDHOqXDy2od2VehjyZFFiSdMsZarOqaDu8mkZLRGUv90Na8Vd35cMR0QJMa5XSVxokTO2_zWlSxWatsojVDfiLl-JUnMuvuWlPzBsWlsBqkg4a11j5-hYoO_vP34NN5v-ACYJF75dBDFNa0Mdr98njMNda431gp8KcvlL20FdCuiGTy89Gb659ZGEyWy94e0KjMJ-0KJ83WACbGeOMlErVgE2LDfMVFqsgEIUO0haQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=HLAD1-quzkQMIxyNe6Y7VKLY_y95C3edzioQZJGcZnTGOFW1l1GHIUfHNKVoiQ1A334CHznW6mGOCNRJzAcCuZ65EEHRNKAaGzLC9v2Dv_VyZYa3iIVdkrUkwJJZA5C6YfjCAaGwG1EwVHJj8qKGKzy6uBFo7oZuwDEaVCS_QJFHg6cDi-lpQk0wv43ARh4LObbLzlK_J1L8tWZ89c9qzCiCRb_6iroAmvssqysB25AZrKBXuPCJubx8EyuS7uucZqtn4CBxVab1VnQOL3TLAcTdxZ_R5Haz7iH5gLfQcMCFWxXDtRNtDdR0AeUURn7lwZgqypNTDNanG9wD2v31QH4KbtemLDTkhxEL2hqGYAMBN0gcEZKKNU33vv5CZZUMDRJ9-f-PWgCvsMT9sT0BiarlXH5yPM_xlxZUdZsa-A3p8RHpgJ1hT98ukggtA2LdGxDHOqXDy2od2VehjyZFFiSdMsZarOqaDu8mkZLRGUv90Na8Vd35cMR0QJMa5XSVxokTO2_zWlSxWatsojVDfiLl-JUnMuvuWlPzBsWlsBqkg4a11j5-hYoO_vP34NN5v-ACYJF75dBDFNa0Mdr98njMNda431gp8KcvlL20FdCuiGTy89Gb659ZGEyWy94e0KjMJ-0KJ83WACbGeOMlErVgE2LDfMVFqsgEIUO0haQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyRQ4LZqlahR0zA65YIrCjjORAeBTbcFD5VM_ToR2MyHSfCaypUAqWq2I69KZwCRDs3MCnX99DzPb_g-AFA7VWApZ2kGnb-j9rm5Y51trVyTB9CjX75zJdRmbV6Sqd2d6LvOLVCFVputorxSa0QloNgh5Djf79SVsa7Cck0315opUX713Ylx1WilVcEs8il2SndTPv_4vwdFOVz-jyQb14Zt0geb7jGhjtMRMBg7K8_VQhcOfdlh0YSYeSp2zRre2JB2Ub8ItIMXe38rc9TFSLX4mC0XD30jfUmJSpLiyW3POsjV93emH95YpIV5g3vWZmWgdqUcI_OJzOz-bYnC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4OEiAMhLoo9ewfBwTjDyLUhw6zj9G2yyv059fgbLA6Tt0lSfQ5deLa65G7-MnRXuZpwgXR1_xb7qeKyqt8ws2fxQht2rGVjzP_8EjHPRjb08r9GfwZf8IqHK_8LQkYkCNB5qylgLeQ331YQimEJXVMGZYS5-vDurS_wPMfoQFCyujTSkm9lK-Tp-nyx0vViIZWyQJvCEXT-y6wQXTE8B3ZStB754ebuHvxtQ1bmu_k04ViJddlRvUUtYuO4TVXRNo1NEDyBpzTGsOp0FqE2LL0ooYRthtkLEDPS5uRRX7nfu1aTClnNXLsBLepBUOxhaUUuiIZp3Cr0pxTKUrT1pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhtGrxGCQjUMmtpRcWzcORMITA-xCEa_PzllklLUiekiojudqeZoRIYD2qOFlSCYotfBFpC-L8TN8zVbIPHXrse6Y07KJshlcCaeE8WBs7zoeJAWCVgBLzQ1dIrnHAod7RJKmu2aFq0ayv2euJgMIutPWKhS1o6Z9KeTQFulMtBWLbcpt1GaRZuVBpO9RgIOD6A85UkG8s94Q2Eg90AXE9ea-OsLQyGmijsH1yE6AUZ-dx3aQH9HMEzy5BgIe7PuYOwKXXTaRk4FX9upChP88FycnuS2J7_MlmrJ5mR9VtFfkcvPO3VcG6JXWfqkmKoIEIxH90BZtzDrgjmxQkLYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zi10SndGuSuu6tXWQAjnlk7SINnfupd2BmfU5pgkXTEnDcKdMOXeT2GN8HWw5zhEncCqasNbS0J8oYuljK5kfa57k-MDannx_SCp8vxwyn_DL9Ytke59UQNMSlsw2q3zhP0kMztT2u9hEE-txtYc6quJWZ9gq9K-Ppda5zhbIg7ElynlC5fcERRgkIg_BgxM9ZaYqrU1WIRcUfHZfTkBjduuHVoMgiYYWUVAyfO3N5u1-i9YJKljoBwk0SAA1oFLcijxCM7O_ry_pSgzqgKhOwS8Dz0aZHm7TLAH-WW8QryLUZcczlp4zkZ9bemRr4dhoqLLKzXK3Tb3HGMcO5k9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZH3foYyOFxjbbO3mfSJDJsOjyUJFnD_iUEU879_uDRzMSg0g2ASMeFmzxT8FLfQQ_J6DnDLIWjn23f_8Mq8APWVtDT6x3t-LZXoZ4thdnu_K7oivoAWLNGodcZcBX_SMEFrYkGu1eBM8F6KxayKk5m5HUYicbhkwrBS1ytAK6Ov-tDt3FqfMWyxQgCoHh-kDrLFoqQ_uTujDfoYIqb8MczHbqPc-gj16b2xMR620E0MiDa2NdKZWrnWfh6SvxjuIomyOuku1XhEfjRURD9frjGMxWnPWmgrNyL5PNTiCKvrz5svcbvv3ccmbEM3UGUbQJwc8TyPH_w0RN6qdA28RA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Z2FpbHszT0CWEd_rD0EC8kNxe6XIftIsgjT7YLwdx_zvgv3KiSqQoRDLyU1akVNpIIozsKcyQCiMsKVRIfz0uHsEg_ia69yAL8UaecL-6IO1gfQZxQNb8mXHfrCEEsVUOglfZUIzWT7gDNduc8cIe1xbx5aw5TWKPf_sfGDCANsCs9ZacFVKJpSctOYtXfPJPuJDirLm5LNzKYvIWFN-Gr1b26IGK9x2EVgq_U_uw-yxMqxSzyXPx8sQe8vysr4FASGIO07UWLOmffN9DNdRKfsf7DlFvnR9fD9hy2z0jJ6IfBZGD5cGjYwbox21ahODIlpNwh7lrkWKq80qJvDnE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Z2FpbHszT0CWEd_rD0EC8kNxe6XIftIsgjT7YLwdx_zvgv3KiSqQoRDLyU1akVNpIIozsKcyQCiMsKVRIfz0uHsEg_ia69yAL8UaecL-6IO1gfQZxQNb8mXHfrCEEsVUOglfZUIzWT7gDNduc8cIe1xbx5aw5TWKPf_sfGDCANsCs9ZacFVKJpSctOYtXfPJPuJDirLm5LNzKYvIWFN-Gr1b26IGK9x2EVgq_U_uw-yxMqxSzyXPx8sQe8vysr4FASGIO07UWLOmffN9DNdRKfsf7DlFvnR9fD9hy2z0jJ6IfBZGD5cGjYwbox21ahODIlpNwh7lrkWKq80qJvDnE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV8GotWxjwTQ2IaPQLsx5qsVap4HibXBtjEUy1OTC1hbEgsbhY2zs0IqIh1iS0d_4e7V2_T9Vmt1UgqNcuoDzPk28nYWy-kEW7Fj4CEhxpvmyDxLUCpjZ3GKe4J4FW2cQ5WgoRvCI8sOOk5jFcR-t5CCWiq9s1aRr876_mBkFjI2THlCBYUCipdbIhoR3bYFM4dmlV1qLKLFiN7_yCUrYrZr2mgjWBhiPLGibeu7dCAiRU1Am-Q2VyKPRccLzVY8RX8gphjCfv1U0r2COGXRu2iyjG-GxDtIBDIt-vrdRZvF2yU4k1vW0sb4TCtoayNS_uRKbusUft08Kba6GnOPCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLYHkEnytlc0KGyxkKsnnPvWg7IJhoh-QrOalfaws2ZzjsCcXSXDTUmxb7bzcxV_eDcdzkIF1nZDOrT5wLmx95wZizZNNkc7r2TQ_CY9YLm2CSzSOw1FZZOxYEwB9KjmlkI8MtW60gedEmGwKFF203dryde8kLr0nAer3pFW64JL2KrNZiw1qsocKJ4JTRxfNCK_Kpgda56h-gfjxHcm9GOsNJyi9z5TL_Fdr0HLs4njXkTkAcrrJMIR-ffUaFpjxEKhq9HefjMDMRDPfE7XeYJ6cbP-kCSSumFQx3PJY6f05rQxmBSfULGnM0ZHP4BWfZ5-8MHsLqigdy9gHtsGOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3JMnMaypcns8JXTj0r1o2T7LiFGRAHwNciBbjk5U301y0oKUnaceCmEb42kdwPBWioeXu4BeI6mRwhwbynyguv1m-ZYSoEUio56anuUjcZvnIycU9bNctxnTSoVkMDhBx6LhJFT41loN2AX4vHZYMMxV4lUEug6KjF45pb5z_UyJSDdwwy506FTPebBZ1Ui0Nz3adVrN4-p_seqi6ER0EsuiZgLmHhTT57gFiKBjlB2wpqulUuTrmTBHYINrnvmwk1c06qNHUbRdfqtn1BF3PJyx3rVELuTznky6TvhujW9x2RmAnJ3_sXhZ5IrbFR9JZDExicliJto3xOsRozJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wcv8QoAdh6IfQ7pQuxsHyh7NPDEUXe3eXldhwPl8rhKVB45noOYA3TGP03Jt8L558xuKwXo7MP1HNMCeXAQEw5qN8uAvKRm3fbzQSFU8dn6PLUk4smSxXAEfL6do9Z1atmCYS8PICidZ7sfjDSdVE2rlFtL46rY2iNEcMfSq9obCaCguB3n-hIY8fiGrlmdytISBVUWejZvlsUn4mdQJopRfV_z0AM5OQACWN0nKP3pCCubH3CesnZSDecEcDSWboyGAVQ3oFooMvgRg7lIsjMe9-7925NcohNRsYaAekdk9VRvJjwT4q2SFrOA8tPE3Ag8tdHBKcKCge2A1C3PjLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQYi22waVLCHZeyNo_M1hXwoI2BthaN4abod9JPPvMn-oMcO3ddePMJnAp8Eu3XJS2dw8sFTPHpcpyPq3Y_G7vquux95pcnpq3m5knKamEPtvamjfSH2qClNwYz6AwuBL9KS6-mHp8kddvzCKjagv_xYB_Wwr4dGUwkLnetCvrLIHgyEAY536CPWtV_WqfNIhr1YZqI4kjhni9DlJQ4h8-tgQQqq2SxXbvqXWS6ehWbik8C8pFMSmj5i8Mg1QpoYoVisiWDgrEALp3-5B0sqX-H2GbLwvGuAfjWjmd6roOEkiWNh9lMGccq--NGyoepPQJJMZX_AtYoWyAHn5BI8ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJP4tXMlFY0AdA8t-PNYMAWH0m9FdZJrgfk7cqODRem1F-XYkpBc5NjfG9-N4h5ObkOGUxZBsrn-Uat_dhRmzrXxoR8wzvA1Vu48Hwv4-Af4o3-p96RhWtCVCAug-VX_2orrqq2mndIypnIrGk4oXwPMxmVVARr0GafuOR2CMfLyZLzSdXQkURib_2R9TIOegIFXEZFN2EvF_VRFTM2rWan_09Syu_UHQoWlFb6xxXgGX2IWTNlaL1e6O1fCdDGBxTkAeQo-W9sVg47Gqm686sGhBpBd-6hPN2Z7kIXBGqEF4DJplFrAHxZ-VnOjOjyIZlJIRf2tYRuEaIAZji023Q.jpg" alt="photo" loading="lazy"/></div>
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
