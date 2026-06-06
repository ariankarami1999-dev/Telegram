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
<img src="https://cdn4.telesco.pe/file/Xf1AEcvyWgns_NnKppYllb1ya7qxf8UpX93T33IJxPZmsgOpmnFZr8areMDOd1GXJ9CcgenY2f-OGoNmhkK0qbyXsWgYwu_AHSrWNiwJn1M5yKVXBtQxGXz8acVZ5xhdilG8t8TDwwdt4QcWzaWiyuKjy24PoskJP4v7xQtJ4FR9GhC8B_y_jqHHP-T-mdZpX0SgeVmMZawB1Yz4LjBagTf1yl90QHvusrRwlw_bByz4-e-FwvvMviYJ0nYfPuS1uIkVEpJu8f_jUoP0_OslF-UyTwpGq5KKmNKXSakY2RG2jNXp1bdOlazP0AV85jeRPhp6J1SPfKeL5OwyZ5cHlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 23:34:57</div>
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
<div class="tg-footer">👁️ 161 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 303 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 533 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 653 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiyacRXJ5VxPYJ0ZFOdvXrt4kFDAl3mc6dUMg7Qb9lh6fMZLV8WUwtLhkC_iN6rGBqNHLWG_HTHGoZOGgfGjJ9Tc1_N9saR1Pw4FKQzdejyZ1dv6s4A3bwqTwDlyBZqzwc3ZMD4asqtWbzJw7GFoMfLl7J6DV9EP0prIPkLYcuuc7Ojn2Eeu_oVEWBgvTq_HvGB38n74ZbZCg3ZJCosk22hclOBBbbe2TG88lvBzs-GEsAXEQt-Gf2ODa0yCKuvl_ieuDBAjvHinzuXRUSSInibfZgfHuVnn4IjX2hoclA6GwgUNFGfhNxrAD6x_IywP5f9yLoTZlby_FmTvpgaOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7AyeVFTSqUn0Tegy_PRqsgBtIVktsXY33G6hhObGP_gIQofCQqZ2tGHsaL2qKIouoXWkmyUc79Ey_-lXg8flGupuXGOevqdYt8d0-teFUn5FJ11sMJ4RjpeaSbon5n4-CDuw34144YpHuVl7BxDTyuAnhae6Bh-yKMAB3-Ldv6W8Livz-mdlhqQtlek-CxFfX_t0SACxSLkLh5DFlrJywpTiIy22W77qt9NeemkoJ5uhcRhAHY_1XhgBFKM6Wgxyn56-w9sXygx4mG1WRTVesJf7-pu0_EFPvhoTsCUuC1rcmFwzI3KpNW62MqVVYQVMvm4okbIEqSq-Lq-f-AWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULRRrpH-9qV3Tuicknb9OdtYok5CWTn6wEqnSRZ-47_YkxhdpizCo3jd-WGFaXbbimFidtMqRNhsfuYLv-yisdtycp7Sh9h84jgHtlK8IRqUyvDXILwnpdOM-L296azlKmm_kqIw4JGsaoBfoNfgBJDYV4EbjLwBIdfqXAZLsTpTru3-ZM5vhP2sKNPdJPt-oGlcUGZBSJHkgxY2_SV8KJJl9qwslku1OG2laJet8mcHbF0wxAx6UKX0AQBldDcUgXga7hwapz1UxETSNwKVmpVVLGX4nXh83PqdBSzENV6ItxfY6iwCxPmaU4DAWtVeHZSWcISPIs6fdYm0pEwBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 851 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 854 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRT5aS8s_MkqwrCYfLp2a6YCK8C7EnARE_9Y48k5H262vsyHTNbsnEL9clCnmfO09pQ5MK8-3NY84SD6EdAIlmzxl3o9tHk35tCdDIp7agHHVo_RV8k9igq-JsXp4qLLEp039BdHssffQDIde2TDgqxBG3IKtSjMPVsLu2ojS_Zg2GyIoeh9C6Wfkj3oD5kw4LBtbZry6ufCCaP0H_NKI4nhe_2p_DLryYNk0C6Nfi6s0BqIzM5hg_TzO4BhCHmipSnLBmJ5tg18gjurH0ZzC3aU0RODfnQoa-R0jgc45TZX3er-vhgmd_oc9ROk_UGFTQziu-2WlWlf3koIo6cgZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 879 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBr2bm-g3D7JR2wc9-aEHKlJD3WCPfhZVAc7U0GP9wSzYp9MPDmuUrP1kmmTN9nbTVP55LMb6jX3OMuy9zxdoDsfS1xau7lJZpVIQb5GMcZGwo5WuJuinqyU7TjqzNPHTIMPe6gNWFJa_XKXXt1MgRSK3il99ralnsl_sjmt60Jh8iuF9NARyDdXNn52vdCT1sIAaNhDN20SivVxKSnveB-mcG0eA8eX-RZrRRDlfE2zuRi0_PPnA7AvLgajEcwJnFtR1hXm8BZtSvo9-pexEtbNxUp4p3a2POWQ2EzjrRcim5gK5J752Bcggj-AJwyAdJnLKX5TmXqg2H4BcmdA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4IaiYSZFxfoEV2n81kO1_hs_TG1O0vziCZoCVgnJ_LC8D4chFbyPkKWqyBssNa511bLxa-4wUpZpx_lP7gFvrUKFAZCVTFEsPj70AlGRfNBJsGU_WN6NVlmysHOtrCu6xiyIZYQDIuQE3A9a6zAs39itL5Mv1j3_LDyyytBWPtP83cKvydc1ngzRdqfqbnhEaZaFtnESoE8GhcPmjl67bKmfaDjl78HNmU16ZOfXuot5UCxSU1JjEYv9bnmdx-BkFpEhg2emLbDE6s-goM2Wv_D2tHA2ZS9igvXDMJzeStQ6EwU_xx4hhZ1DmzpQd7_ga4NhN-_mviKZjHgxx9Afg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7jY2ggO1gjpT501EUH6gp6_XLzrHZX7z5WrVwOSMjZFM4oEP_hKexkNQcG0YZwo2UgPf-nmZx7t5s2Iwe0qOmrFLrWqnTMuvsxr-X9tv7vhq--phrDzkQn8l0pJpGaGXgDGT0i5Wq8nSk4XdMNvLquojbUMtkmvH7v0jGK8Rfr395Yln8FWj64d32UFPlAL3fEWmYcUp9MHC1H5pVSIlsASt71JOjEzj3dECBCSP0Cxb_fmEJfSZNNYZhd7n6xft_gX1jEKIUaB0giZn0ParNyWmNICJyDUqYzN4ys7fA2W4pXPEqDhIbmWEcXyG46rG8Vv_CQmNMKpN3Hn8jDnxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HneD0fMziBp925uCl1b1YBW2vnXcHbkR9HE4bXVEck89Qauy5rjBqOIhumxQZ__KEeOAPhqaoHM2WtDuTXyrbpy1xIBaqlMWOIWNanifytCIApnGsgsVniCsltxsH7Zrj0Ks5nDU-1ayR7dZgM2mXW021bVJJKfLTv1iyyvp2qSSPBtemn9Iy3Tqy8xi2zLOVA9paeejl0Dbh7Gz3XzUMGFFDsdLNg6g6U3JX-3Hx5y_5gNxJx_9jTsf4DHTi36F8zh5Fp_URM52bEuF_YmPagucKD9HNZQuW7HUo7yxMfxvDD0-gNUnWpaFP04XwQgq0LCvMXRrRMw8ep5eoE43Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMoutK1tCzYRJH0iYcM0Pm9ZGKP-nVFmEZ_N1KM1y2VdZZ2VnX0kO4j7W_wujnAu870qbB6m0-7kXGySzKSdfEm6upnAko3GAQUC7PnM0lsfkkHLmTWpvlPf93Osmc9EO1dNz_a932BFWMFp0ZDjXiau3Dq0_qif9Kw6qLllaVVAYmi7c4O2ZzZgoRrppVTgXWZz2P-GEfExod5h5ntH_ItPeE-IIwgj6lAAWMLwz4rIYz9lTZnt2mrd4Ah-vUhLxYJTbv2awwtPUs0UxXFbdfzWoDn-_4y6At5yjULoQCP38dBx-HQBvaJJCC5454v0fd6tViSNw7N1ooVC7cWnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rl2aQfuAIivcr96Ew0Vv6w2dGECsTkd6gPh9F_nb7k4rJQzsFoJKh6klVMzPylrpizhbtRKZec8rvxiYvssrf132jmB1_0OjukzCxTmobifi_tLoT8cSzlHsb5nmKlLg9fIoW7U1H4hg-scBCBKjI1tm1VMSBaixyAPcQMuP_s41BRpGlPVT60F8ZY0a4BpWHFz7LFr6893QInU60DbLpQP5NZZbjYfakRl2yYiIy6mKuetoYaxD2D_XG15F1sv90_DGnY60t0xluaT2nEJ9hpcIoN-e2K56Iw5CNrTWpPqiPdeFcPj18id1onMlYlfxjwuxH5vYOPNV1uBaQDhRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkIFjIVjZL8TVw5-uBOfcQ2Bz7L7_7ncv3GJaG1gmlnm0RxIif1VKHw2as_DrJrjSBSAh1CUQk9Ohfn5htK6fk3wfk8reFbzGeEEDTakBgXv4smb2VK-_0ppYO9Oyl7XJtoPx3Rvz12j1B8WCL8YLS8v6oWPbbwXhkNAovClwClZNwGkCJANVQGqJR3x6dYo1iRcGP86vOALUw4YLvYSuQ91ZrdpyLakUB-k9mcjk5hbEuWZgYCDis3IAi5RRlawP2sy02kcDbBQ8BCOA947nAdYaYVNj1j1x47iAJ2OmIsg8WAJxedDbf1h1ovgNJwYi3q6kuNNnwZmqVSuby8pMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQsE-0e41uXDBevxKJm51VxojeACmr871Dl73SwMED1Hw_4_laEmsvliJZLjETm6rEpckPlmd6qdL75DratPhOpF2fkysly5jtQi-LuF0Vr-w61NizeWtNi9HO6IHc6U59UtXraWK_DRe0zBz-xY5tbM7AEtb40ktKSIb2rqtCxrtTfgY591SqiF8inh1RYxSBVbjt2iA5ALEaJt7YbSMutLxVKu3Y8_0qUXUvjn9SZK6fhZaV1qLZeu4SJr4QYRgqUZy_4fYnZv4pdjMGBHRjUPOTLWrt8e8ssATUy5_Bz0vS3SqnPubjQPiPHx4YbYsm7ZQDfMiRBG3CXTCKGlLg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=pQc8g7Vif9MmY1KNPbO_ydTGhCzHPbPPkIDHhexBfmeZr7vEpvuxMHbb5I71Jgk1J96VA3SubYENf8Oj7TW4KusKEcAqhrzdStL9a_JcDOf7w24zY3490Eb8ib9AHcruMe42SvXWzdoWC2olwwZvoEBj16-5209NOC5br7EDaAMrwzxjG7maAF07wg0fsWF-sin3GozJn_EuH0eV3vLNTL3u5Us38zJguK63qtXv5PtUo2X85C7h84PGC4VU3SbT2eIvReghrqLaCQ3HfG2p8JE1yBQxkw5nGgnVwlX-4vbwK6hDuTFQvXTvOx_doJEBh_Y12lLtbP8ccnwm9dq4Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=pQc8g7Vif9MmY1KNPbO_ydTGhCzHPbPPkIDHhexBfmeZr7vEpvuxMHbb5I71Jgk1J96VA3SubYENf8Oj7TW4KusKEcAqhrzdStL9a_JcDOf7w24zY3490Eb8ib9AHcruMe42SvXWzdoWC2olwwZvoEBj16-5209NOC5br7EDaAMrwzxjG7maAF07wg0fsWF-sin3GozJn_EuH0eV3vLNTL3u5Us38zJguK63qtXv5PtUo2X85C7h84PGC4VU3SbT2eIvReghrqLaCQ3HfG2p8JE1yBQxkw5nGgnVwlX-4vbwK6hDuTFQvXTvOx_doJEBh_Y12lLtbP8ccnwm9dq4Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiL42tBCERtgXJszjwRbLB8oj7VeksPUXSEbdv4CC_pQDSwJcQ2Ev6oBpWag0D8AyGiQf9mML8F3OwPrx3NYMg6tNmDWiqxmSAiBeaNVVZiWcUVfQMdcWkkbDSID9pkyFsl0ACCrBZI4_4ihiYHLXkwORHtZkpXradE3nWpDBuo_T83inmO2z9rmeN8TOH-_0L0oCXWQqDrR9MrMii8LBska8zuOCm9QJ-JjDSnCDuN59tDYTG5vRPUfsD6Yaj3A_FvJGahQoDRXv3h8yHPDgll3Jp7r2A_AtKLH7J1G3cc6DIX3TWnSfTmUdhQ-ZgD1ZJvgAn7UPaai-bHvYjL_ZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqGemmrYeaxaOhQHsr5VdyNDmwdFYkekw8VpWn6qt7nA86vTPMZWua805wgDHaBPndg7gTF0hwnnri_9EMGM4Fv3Co-JD1uVY3Kle-98DhOfGcAum1F9Fs9U7t0cwFoQJQzhDSpVDZzx6Y5ibNpx6skpHepLG23bxA3zETHkzXjN7zqQ4o108ciXzkR9Altx6PS4mb4vu7xu--YbvCEBol-QDEo7_gOFx851gr1YoaQlpq9_BVdrq9nl8uhlgAtsT4LoYa43nzUVIaktw9nJOnDNduh57Pdbb7-XfcQR5cyRmSNghA0ayLwwkdf-IzMej_6fjyoHBlnaBN3LZnAHRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoDmd4qPvCPCsSoogFhqy4zw6ij9tzzBhXU4N_1vZyigMi7wjHZYuI_8yDKyKwnQfqE5_4JO5kIeruZh3GTyFfOHitZZKlNLbLb97u3WjG1Z4szX30q8gbiwKji0KEMy5V43ZgQUdFCXQeM3WuPp_v238M2NC6aj8VSOIS4M0g4BQ5tlJ-Njw0C83nFNz-Hj4ivufSdbRX5n_JuoCj1OF8ASl-fc8j19_Xvj4HZQ7j4G4IIpE1CVZ4Q7rt4Y3kQoGI7PB35DalyjPiTQadbkUko1j7QPg3TxRPHtVuqsT4iAqz8huENW7tOkyj1ghk0qNJZL5dQyHGciE4eYigqn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_7KQcn3tFaONvVfeemcyuRD1MmUgDxT5iqrnwvvPW8CfmLkJ2i9RGaXeui8_5gHjahtK5iS4P9p5icBSUghf_BsJWMUycRwbDgUpSl7NtIw1O03cNZKFjCwA2vqv_RBiq1Q7FD1AqTURJKbmSaFmoGhcuTj16NQhvKSn0xUC5ZRtcVxlsWydVV2YMbPwwNH4YXEEXKFh4CpgFJr8DLbWp8I7nAZ9W2bAX2VVv8X1FxuL2G5A9gEUHwgtQU1j9bddz9jMXaHqWXZhBCAsFiXgdM44sawYNRMM1akOazuwXAAAqLhbmOsNarmaZ4ck1O7cqLAjUsFgOTSD77Aew-2UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odaQ62tYDti4_XWl7T6TD6_HDVGPqVshnnz8MOKz8OawBZHv-eRZFIau57jfA4kfUtLaJjIGUAFWKO7Uvk7lLGTnO33DiCWPTqgDOTX4Giiz9H7cerM9iTiuSptMk427joLyhhr_DRYBDyFMzSdPSuNfx6ey6SxLnAIaEp9YJRNuAFcblil5ctr-pGAww0jtW7Mm30GUuMc5Tuo5XAsOwJ2QAk4cWcv69ejOI6ax7giwfHsDxY1XorzWuUKtfGvrKg0U_QoqP9zmt2zogeAnr6lBfKrK8xIkfMTDrGAE64wT2-m6bldPdkqG2iwhYtwMWzCNeXGC4uZDKCLYfAjuvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPp19CBbEhckKbB27WLDLyWS8ppBfO3xzUFTJAYBzxt2wAt2OrDnlnMizccZhUWceIVy1MyShRS1darKEbT8lw72eqKo1NSrbTSy93CJoxbd2FRB6SgjSvIxS-qPc9gkArfwjI6QbR3eyO9ZbE6ZkZCLmzQcKXv7sMUr75LJ1eKSsG9G6cJ7Lk3KRYjEtGrPN4IT5HEOBJHd_Hg5dx38cJVEH6H2wBSZYmCumtKcBtsNI_XfYX-5aqQyGgKc9ih-aH-RYoO963Z5y-K_j0Z3pbzQ7w0UeMdPotQVofVQfMA2nYiokujJC461AhczHqakYzUIqW_65AhFDDoC3JZSgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpMz5GCOqyaEDR4snZiyub7g6PfA_6CwvVLH-QuKL4rSBqG9ecrWxTuyfQ-nYul0Zi1As5G3vu0TbLMQnNAStvbK7g3FdEr1ol5cGBAxGuqYXkGZaxOR6QtZiD8xKU5UbPrEE7m0Mv96SAgX_A5aY85KfHj9vXnQLpvCm8lVuIJHkMjdUpZE0s71mvDvKXY68xi6p4XIe2xEKGLIaKpwP4Qd8K6IvTVxJS468RSxJ44US2x14sBpp7KmQujUVfCKO5HFffAHOXMWMTDlcy_uhTA4Zf0IOYOXrgB-WpzbbcrkfmUvsx4BzarvWCcAZuWwP0OpmMXNxvWfW77UMaqW7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SqFOU2CRSy1NOyMlHonalGj5dIuzh-nmlsIi4ssOEVLZ-WMhQbVNiZOMfPLmnwVVcA6dlC-E4mJnQQkpwMUyN8DgkPEvJvY46Yg1zD77pn6BC3vomI1RCrpHLZetlDQGc4kLuCRU7TuqjoLLyUiAG-v3JceNBHjEAwg-u6zt3onJAx8dZ0_7OABLPvUCjRC8EaJ6BmQI0Tio7zdnUzaTcvaIZMf-lazLXVb4eRM9yCE4KnjkP80FwCNSZaSHIqgk35YIz8QHSnZhGwneEhXIZvZiwL0tK772bxbh8BsSZwzjnBKbQOIV5_KTUoJn1H-oND5x4j6899XSi9uJ_XQ8tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSbYSKcKR41U7tjYBXF49FmbbAvmzdn8DmBVuy7g_E-DPKze16ZsysYmOkMp99I0eg3d0M6iaDHF0o3YAHalZ9h8PTL5mLRxXIIuhv-YAE8V3E1TTDjbZiQQcnqbm04ZqJXdZcTPLFkJEtok4iZJJ-R7FHGVzl-2N8QLiiAus0wKFMQTq2AAMss9sFZqXBkInY9ZdBpRHsARJzNL_sRT6VPHSjaizxMN8tntBDMUN1nI53Fj7gJJVYFu91z8Ur_ms_oqxqir_tgQXVBgcAf9ykmoFISR9ANV3tJ1RjHhxVAyJ0ZO4bx3NbK3uBpks3jaTu2Swdyz3IhR9ZSMglBKGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUPzcu-f7Y-TRarrX7DhopNAtU8R4vNRVAXZgj9g-lS2a7D7NXfAi_4bCqZDskAf5MQAo8uzpEminUyaIoNaTonY_r6jjK9vQZhcTMxumYeO2paikcLFoTAAl1ZEtTywNGSoBoSt-iNj-Qkq75eGQHAvTXNBe_daUFjQELTBskhMc6-YBg5-qY2QhYPQy2mPpsv038lTQHxNhZRdd7fK-0f46Hdx4eAMfXW4dVoDpQGMP4mVvd8Si4Bpfx-n3IAyt9f5FLo0wFlvpp30Ox12CGsIvxtUdRNvzxiCAyLEUKNfOdRF8P5wEWRm5WQT4Ej9XuRHHyQMZMldPDjx9pLKbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpO9EtBl42wR7e-qInCyNBjVtoKoLwEFSRvEGU-xfVtiiOLXXo3-uARtzTVom9puv8GF5Ld-1L7hz_1aRWrL9G3k1hvOvFyNu_WvYaWnndYwvp_qwLjmoSk_2UhLYSrTyfBWodHiQVeFlBTVxdKHSN8VcnrkU-MyCA-eov4pW6ECFOqv65Lpn2H35ZDSmoANKxAZ53GiE_5Z_YsM5avNYhIaXDjmOHxTgiuNG8NVe_i8bMQpiBb-WLBw1A_hehqJZTsn04QSs_nmyrI6Zt6UrN7rH8tc-Ckrq358c6HkShheMM5xz1ieJw1QjrDYc5DFu392DbzJJihZndfx8MTEZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk2mV439mS2fUqKI4axFuaVaDhFPYoE47lzjDsbGc1tMWjXCaro6PsiWpR-0kPmaYaQ20tC4oUlOWuKWddHkyCDOEU2eSb3wSX5Oi-jQN4XRP30mPF6ll1nWDN22073fH_SbzqPyM43ed-6YXJV3vIvkfatZkfV2vOgBxoXl_9ABeEAChbg2Whlf6u0XPfIk0V6iEXfjpOr2uoCCeYslW2yJZgiZzBpiRtMF8G8nZ15EV_eyQKEMCcxKSiG-9rH184I5Z-n2Xz8nk6T8Ec8uktoatJKTbizyi2HNtBMq7AnCdEeDSac7tY2DlbOOA51GHcYr8K1z0GzF8Vdk5oZigQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8RmJLyKktj8aSICMUOik1ARzRYiPtoSoT8hkZTmZfa9hcrQ3hVCsB9huBWzmXP9oVzUp482UYfCN7_zhCkPFHrwLyneA1zPJ26PR3uionnjoh2TFYL5uMSJu7u0di8dTjbegwkFIQF2zHOlnoxh6yXfXtzp_BjVN9hnpfULpoCYtelLuBBYb3rRSQMv3I-JGuNREncLZ6QXYg3iXaVQpujtIeBUJySilk_EWTb-LLLzwUQBH5MHZEvAOJ-5rTgB4YrGVLspZz7__7J5GFTLYMgYZ9EtfAdwMUgtaz0KQ_mnaVSThgDdfx1meUjo3g1fgipngPX3cd8DnA_qWBQlsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKpHhzhNiKsO2TY5oWPlvsuywIlHyqUzaQuusjv5S1Znr4UV2wZYzpzusqPpsx_jZyWfyb9K-FW62VnGWk2WpCIUQfNrbnCwtvvTyLP8MtyfXcnQQdSzy0Fb4c8BZyz_ZuS3O1bRhd_PsaMVpsLwGC0pfUeChqb0ZX3Y4cWg2jULbiqlGAI7Iidt1G4gOKIro29msE0aFGmkT-co6qnrB5qe8-K60HY8u5Dghwy3M9LgXWOWWZp2WDloC0BkQQ4TtUg8NCxixHpx9KmbRYf36RbnX1gpUTFpAI1u4ewb044jwqN-t5JXh7KGC_H99xgQgCsLr1XJGg5OoGUmuJNKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3RIdAJ88f1sUxeuvADctREdoQZ4L9t7LrM8L-v8xfYHHleeQ_Ni9Yoi2aoKw-AfltiwYkWMTPYIxY77R1YnIsh-c9tC_cRKOZFxc067qau3crFk-L85KzOgZ_n0IfhOS1lL5VS6NgU01wyW5I1Xq8Z4Dcq0rP_xMmB8Qlt_e8bqjN2N9FRykR7ef4LQ0u3ICll2-LKwatspJ5DZ9S7JgSv0oFKfqojKMJCTSkGfP2ud1Vj6iN_WI0JHjahA_96cwEDZ6kg9y5r4DWsN_-3mCn8QYWNgz693-JsxW9rvKf9D2TYId9cp9RgNI8-fSK6HElpyB7p64wbcmnsrVlBwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7DM6U3k2IoNEzdvulL3reg-_vFFYK1UVPV6Cg93Yx8tRtORM74IQzr59yc5kDGi8fvvsFroMM4WVEe5PxJ8dx1-c5uYYkkDtgD7HD171WwxnOFNOlJfmF_5_k6dAuhAasPC6KiKj1ax4-V37i680pTt2vH2nmz-ZY3g6kgLzXy3Lm3TKIFk5l3ry4dgI0rHEslHhG9Y_qOx4nIEWCg7KAsddg641lP34pfHnOb4QuZhmsPk6semLSiNMXzGbPlgLxTg9b0rECAAySsTzHFg8rAOszdglYUB5w84gJVwSBwKxRdbUIsdTrzpFVMfd1gW9fz9UlPiHr6_grTFkY5yTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDUJRnE6u2Rc2_cdQb1Br5IBZwCtfRB4v-nYVuSuwg5NNhJEEmAyiKjYTCC6VwhkEJVyzqfZcAP4Z4p4Xid99eiysRcwnzUEmfAhzxiRSEb_ki6YC3q35evlCgRkqIbNbJGwfFbjc2zwXAk-TFxHozq7sSt4RawOA6ui71wGpY3LNh6MLZ13cqDfOOXd2we2iSNQvV1CI44W5aKCB0yHZ9IkE0KDmm-OTZni3aP0TgA0iWK4nEeHT0x6aMUV5hTnlimSwCK8gcXtH6yR-51xmnTytBKIThG-hJQVAr9zCUOmdbw_7pSpRli-JEvt0yF8IFVubv3329XU6hszYqqZfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLpQiyjua0ba1_zXtCQXn4ZqLAikrU33FELp8zqeEkBiXX9I9wAqOh06Dl5ti5fzl8J9qZkQ7DAv3-OfImKRrB5Vik3JdajNH_I2pTJn3M5GNfYZWdW-42vBEVz7xYlcqT8w6XXPYtuGRBBj_K5rbciJvOmp5gMQvq2nJZtEtlG2gTB0LZNh68WFe3ICYFgQ2K66aZMAoFKQOLw4C2PZFv-hkrcbtyj5amHZ7UAuWxUUieNXLpVE-ghLLj9SlkgPI02rP7TRfJwEHBMzwN5AxVU0n7Ye1xCmGCnDLZXh39pVKo88R-Kszyzrg5M2sWz0OfRj9zUo2qVu2HMmWFD0eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX5IhLgL_kxsIovTlK1dASXJ2A52K3AKoDo5cw4wI3WNfMIIVxL3lhnblBY5xUbc69ImD5yR-B02QAle9qCXS7Sbz3CQI7Wm3y8oLny7CNagZRtr5wyx5oNYo8fNjiLJnezuNmSLQyDkrbVAYGD9MAv938Kp78QsjMrc8QHNf_qwan7oDJrZ1iZnvb8UFLC7Nwr5GjnKkZ1ZN9wpzDATXQ8TarPkA9LLUNKn2gXbfYMN3snO8LAEhDM1Hd6okCjByI1qwLv7FHgRjHbhRB5TWu1G1Mn-UAky9EDaMXjdfagVfHlD3gGatX354scw-ReRpGuHc6hoWv9Nrrl_RZKHpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK75Uygt3xlqMjr7tq3UDs3FjduEx1k1hNh74yhUNkqN3l46QtIf7mQfooAkG7uiHZf8S3FC0sJwwgTrSwE728IgCKYJdzSg_BTnJhX10Kgn8_yhc01iiEq1j0yLisTmNlkB2oy_GCpJX9nqrex6FlpT6B5UzoH6WPiQEgVFPnF1oHa7O_PUxry1pDT246EGFYuTO6C5w6XNq_F2D3azSIyJRrHCdUBTvdSBe24v9wEERfaGecxUJr8pllkAw9XEKu95YploHG_54VTokG-_rcoddCOHN_orvwWVzNiE54oyO9SJ4VYP-Fzutz-UWF3x3AVt5aQvP-K5_kXSLgNTww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftgT5vVXMx9rUpztM8AWpsZcz3W8RDs26ktcFOQEy3rJNhFDCkHDFA25YZ1hdBk_AgShetMjrnim4EHF7WcYYVZRkgKMevDwaiutMXEqsJTjD5y5oT4E2mu-pFCn3JnpyCD_KVlQW6XQJm4ntGtEvqQ28Xzppow3oGLjHKx9roEg56Yknl6S7If-7dqSd5FIh6fHO4I35Pbpujndky50nmvbTT-iWpr4tU-JPpxo0nKC27XIc_FmiluUyimZVl-cbff6YGhczeDHZhd619qbRpAQLrs4oU39xqO49HVT4U_gD136IzzlvuXY22JA93lXjHcIypzFmX21vreZ4rjM4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwp2F1T8zYY0hHWqq-Bxe7gc514mmREcczIi3Q_8Iu6W55cz1L87B9n2lCt08iGcG0Q0z0Ian8iEatdKTleEjm0zUckMH1iFD10WRHONuxSEpBmHy40wP-Umx2c25BsW2hNMHFoCO8VGj6vfV_M8OGKcajgeB3ZctJ4kwHfwvg0gK4FqVjCb-9kPhlNLCqt51Zx8i2lP_2IKjYFmf7_mmAlwU9pehd4N8hXSChj70mR0lx8nDJEeVIPAnfCrgVaM4jLnsGxKf3TXyzJ9WeEiqWedvvQfNmiwnUIKY9Mohd7ywJ9JuDqMA-L2tYr9n0v0EcwQCubOQwU2356xIYzoiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMX14KbqShDPA8p1TshdgnCuDylFP7-J96habyu_wljZyOAuIu9h5530IKx_Irl5tFEpd9lqeE3sk8BvorxOBq974RznWtPOrocdEQURtRw5vHSalvfUkvBJpXaQD2jR8_ttcXNUfxeehNm8VnWVN3aq5qjstLMD7yYJi2piSWuAxfaAOfHGr8W5jCEV4MQ8AGG09XKNbQM4L1PqfNBogK9zRWSg_NepzfRz1Wk4kH0yTGaSSfwHMCcCvZuWeHaF4amWNMYHhbg1Vn8r4tSN3p1wJPggaircQa3-tQDQDfoNC_GrL1vTbyNJsdPmQljQG2Rz5EJk1ZH715yhXnHW2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJC7yQ3d8sHJOL64fMO2ysWT_cZeNMPMlQ183FT9zlTl2QRkL4kdvFo-FL176LypgoD1x5e4WwPSxoaG7pIdGMU8vj22aeEXtQz_YtQ3o_Dr0nTTl1Xb__dL8VIpfJ_7ExlfRF1XvTEVxpNGcT9FTmvqmnkV00OEr9YFkbB73HNaaL7MCdni4AofG7_fG6G1hna9mqOqawVCNhlx8f0WnlQ-PJhcZ8YSUDN_dkrJqbbB1Lj0P72fScCoBVUH9GjRBEmqBeSR71cdb2zcFIxJIlPwuJaAfPXYFnTdrsaEYKiCll2CBOWB273uYR8jKbCW5fahPWO3EkGnrDL9moHwwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTA0rm2Z-2o_h5YERCs56ggzZWoi55f2KF9LHV0VIYEaR8Da2N0dPG9uL8L4rmHyY4ow14gl-6SDciARPysDGkQZ70IKDhgMaYp5fjmBkkCGml5nhIAu1wz5Gpyve3kgXpKXW3zYbjDKnFX4IzPx1N7l7Eeymtun-YJPogTIo8w9-pe8jCs1KpF04z1Q5P2CEnyl0YW-0GH2mMu5aov4SgTF9pJD4ddTo0HvV3X3KBIyJgZj48uRQZUC7Bk6fu4E_FF2PMWi6pks9pmbqOI2F4CfREyaQ7zGdWit542Ufc5ygSg4Vo-VEoSE1G3rrmw_gb_DKwDL57D8dA6XxVkQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbBb4vCgPTsOKZpwbwfoS4Dz6xGcUxAArkufTzasq759poiMbJrwBPqmy1q6cAfKOe74bCNIueyS079Xu-eZn3e7q_AJRqZcPlUEdbWWvvvfms5A1Pr2ul79kRNIQA-ATsb82dzfQwxya5SliKyPxd3jLv9vw8CQ1ToWTPIJ3Tm4TfuftG2n_T-DyoIjOT4_Sd7aMX0GcPUOFZvzwtXXiWLTNCINHZ6x5UBi-wi_hiN7wOSE6S2mWVTMwDPiMd9AzpPRITWJO_kuqCtpvv3cvYgM7Gyb9l4T-kVTcF8m8DQmdKUXQ0iWeFoEwlsogDiQlA0XGkCa1TARshXDuJQD_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkepDHoD4F6JwUoSz96XwvWsIKdBm9f04LvnKBNqchqt2nXhGogx5pE6LiL05ruFNcrfXC9Z55RsJndDj84mxFZYfQT9FLdALeUjKiPp4uf4fmJfqHdU7dMjGtjPkVgGNmD7zFmFVQJwcAaQQk8gPCBgl81Vi48ADt5Am6M1QtG9O5IRD1dkjifD9QuXXMDOkMDjSJXsJ2bdNiVeklFKtvt1V2-ePBY0u3LyxGeHXuFtWw2vlsz8dj-twAqJaJrGeFlVKDEIHYxtGFzdMWHc-HXuvu0RjAlwfYoNOY4EGqfjV3uEChDsMMavaGoFthv55C7TMtgtDb_9vO4Oatv_WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOrwchoUzVpaXhvjLa4mVvqipS3VrZjnzBAwOqUfbn2V-eUgynV5cfyLjag8iz4ewFaWTdX-Vg18A6K-gmYrSAhIu3ogTvc5gdC1YX7nSBtlhLSdq445T6OW6F3VlDccDfl-e_TQlsB-ZC8ZIvOLoEpcmiqwRrWTlnlhlJgD-CHIPlzd_14qfBKFTaE7uHm1NfiDoi7xJ_m2B9iVkBAKpNEfRyLC29n_CufzyzIRi7WoAoC2RYDdhe2WqEzWCptguMUrUF4Qn57epviucGAbUMtCDEST4GFY3BTyc5dVL34tRJeV_5Vyiw7N5uNrvuNew1JpSP2ZBAdNQ570m8EP7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHTTUV7qfxusZkgtDGSjcLULOoFMFXJMGaaUV9Qr7EnXkrGqbP9ALpWtgl4O9rZf-zPofBDU8fv3Y5QTbb9T-cBkJQDZ6-equeMAA7XChgnxmfvohw5AA8ePbVAFhkyxKdzOWWwd5dPPJqCqENTDTBGMppjqgaMa8XxE4Re4RyeCHjz37qeqOT5G-f0uu6PWhrh0YZorHhwyesokvQk4D5ZqwQ2arUJIcMCEKHOVNSrG_xJ37bgwePA_s6YiACCKsEdnFUa11uu2ild3tqSEqKDtyDdVtZRDNdDO9xD34z2eEO1qKPIqLE-z_xi5Lj-_0oYQCxgeKwKWxKFAAloFYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmDhvTOAVQlP-BRAYq5-90XZu6cnBkLjg_n6KEjhOFRB7MII7ZuZxEi-pP-9hEyEMeYIyYV7gkZZ3IMsnvfkfHcgEbNRMSnPZOUTGovkME6BfoSvChScFW4Y-AckgAM3-mRfdllWUb_RTvcjcVGy4MtIBIsxKgOR9_cRGX7vCaRnj1_wDipklKcALdAWdqJtxJ9vbfSULZc9AA3TIRL7gilgu6NZBCZdoSnanCPqM8fyHz6bQyyTObZIvLJIiKeaACWIDWzSvFFNh2l51kN6zqXPUKctyR9IBrWiw7HUBXs79N8Hjm0nCh0FOjtFwJHQK26IbaA__76AM7bRZMLegw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJ6HFtndc4uZk9RqEz3G7mxTyLtQr-P7u9CulzJj6fDQ9vIiu9PCmOACdwM_1naW23nGW_uAutqgY4sNfdVc-3LFsCIKlZ4hUnWp8vZvVoVf1hHkiqJyfOKp4HkW_lpED2MDpYIG_XeCnp64DaiwY_2smD1Ixs156or6Ko2fExNenE06vhjMF_JgrCS8YCDnKMQlOMLOV00HdlQAa5XViHTJkZhV-0dnTyLtFmjVWn5H5Q3twfOOLqXJJ3VR8Ols6VFXUt57kCB0JbBFaRAs3PgF0MHYTWEqPoFTz_GnclQdZ9CukBuJj5FBaXvus5VTjay_hXZmgfOuGVfx1Pl1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJFIEUHB0ztpAkxBJIL_ra0cljkyi8NT8VrkPl46d1ex7EH5peP-Z1eastC_AZccEFF6MqPvWrqH_vl6FsNwlVMd16yabVhj16y-KffSGQIoGsKBUO57l3T2ExUkRm40LY7G151bcLzodlvrBF1hcoUJXxV4lDcUMwC8fHk05bgQSNKAvBtMcQY5RKb4f7LKYu9Yl7eTZt5dwBqzfJ1FVaGsfnKJCmbw-wJXnxKlLsYygk8kgqLxyBz9UnvFCyMBwobyCxwlNwhXNrR772BhFmzq5ZMXHmnIBceoZdjNCMWu7wW3ZSn9oQOLJoCtBNY_nXKnZ5V4N_ntxsEFieT3zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAEvXjFHjsEjFY67Kw-WvBHcubOrr-qrM93eMDf_0HIVBM3meHtObojZnX782hMLVHOx7h7jS1K8lyC8cTWxEPsp12hRpogrQRkfAUYx3soW1pjud_OolO8pn2m4VL1s7Nk961fI5i20lJkdjZIRvnw-YdDbJPWV-Pzl3eAxPqz59pxIWWTs1xAsqla3zt-CTeLEHOAk2PgC7rmfrmylK6fMxXpRO7uD6_0-X9RRPOZUXa00Hz8wJR41fl3Vxs_xjjFJEeFm71YuXPgkR0EaOhWlMCmcJMTW-lhEwOLYDjPE3Znkjegv50P46I2WrBle0IA1mNOjc5_Kx1gd9T0XGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEPNFZu5ngJ6KHu-GySNggHs7N-IAC92Fffasr3puFZ9VDa6Bn1U2CYGjxI3XnvQ4P3y4kIp_Vah1hG0ggngPJBHyei57hwXMkwdNc-hG_MHaVVpA7HegsCjz6SsBmndpY3gjtiR-lkxuvg3Tj-iP2vtiYs6IFgs_SRqTC3HPafs4cOXLP9TQjZCktPdGlrQaEMvr7cqAyKlgp48prV6691qnzTMS0snYRcSxEtXhuqj9phb7bg_psi0daic-akCq84efcRHu7ACdChmvKZMH6ijEG3-x9BZ53PYakf7ZM8Iy7jGehXuNlFCnwOI9X98IcsInTlHW2gegAQL3l_5tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1nXszMHGdwU-Zai8mSjCWYCazbvK3FaK8bMKvNvrMJ6pMmAuEwx5ZawMluEm-q3n3qmf5Mgq8rM4ldN_cTvAtnoqVLuqhDwmWIS5DB7UB_3TlSd2xm1VQlBlW3jo9BGUiRClg9sXsseEAaMpQxTpXhsIu-38Lamx7DWNkgsM7qRhwDXwizEtEde324rCaX7DtcUVJhDvALwAF-jwznCmoTiAKwiq1L_MhMUmpNB-5iZ2GNyYfstzceGSOx3-hFROAalkYb1RwGOA1H7NSj2qCsMugg2CCQs9MmP2iQLEZ94pMpLRYb54pojU9MUf-g1jYHMhSFiiuKZ0bQdXF-71Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ji1kF9owQhbwHOektQsF0kkaSFpossYx02wTmT2BcAzvw1iHUl-uCLHkhNnRNr_q1Pr3oJ2zasDh51HXrWl_R8_x3rp7pEIBa1wJQ9g0jgp28dKuV-g-MGToql1ZWa1tKxf-GDbNLgoIoVjvEt0FkCWK1AHfnuCr_NpmYCehuKokdKDe864TtEM3cj0t4He8YWtkiDt838n-EMmp6ZrRpN3f2KlwiIK34JCaoV7lIdaS9z_PKTqz559GuRgd2eMAxANQeRTpnyCwLgi6MiVX45AkWeQevZXe3bg0jkcVSOWSyocunQ2G9iRFB8CdJPU7yu7xuin8E9yOoN3htcP22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez4MmGIAeLEObUNKRyEq9yS45l0SIr01tm2FWmh0sy0fzH0IRc7thuS8JuiBHSCIbzDgZ7GcY_n56S4xDuITsOHbVQkNFuBIBeX5OrCRolekV0Ov_noscpGrDopb9OlCaI46sn65YhShPp3A0mjWts3WL08geXY00L1o-o1wDTIs1jf8cBxf2ub8wHB2XK8z1BQYCMDniIVBpyCjbDDQEIbyeoEARDzN7-brm76kZMEIa0gxjkMhYz9WHQ9yptXZptQDNvhdkxRLjuwA5E3Zxsxt5_ZzPtLqOmG-8EiI7anR6fzrMsOl8mvwLtah3sYqUKWO_n4jGXwHJXofFiQZVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj_iJU9H1v-njB_8XwCjZr-una0Rabysx0tpFGQptlIl2vWyxqCNMwUyyKzoP_oS3e3bgN2ZQanbCV_k55IG-0xjeZbP8sQ8FuFOeGOiiuwLHeTFpimag8X97eUDao2LnGoo182rSCByJ5zVpbVoCvr9-HZZdnUJ-GmNt_GeHuAiYJt1uYSmgaw5HQ6n1nSebWso0hUVJRzphmBGXKAPjpo3KmbnWKw-LMxWD538BELhmqWy1B-W5g5Q6aVlxIW--WqRhe_z82HgYxQwdomx0CyNZ_0-XU-wpfMR6VKiLBTmX0sn0wfL_QQxpSjX6w9Yfp9zlESixfDX7leRDB8Dug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EccGGCBJ8qdqg0da5CTqMoai-6tr5U8L2KXPTiaoPU4JJOJA8LQL-OZFob4yiAUjYAaG0gFlJfVJaqDVWQ6TtLry-SYC4-roqsOC8G40DgkA7noBsy8T-ucQZ1zfMBrNBjDFXNMHx0XR7DZ6m-k99uS4kbDtRBVgdS2hDoUqc8R47mJawpw34AcmLFArZo1cxE4okg5sbG697jZEH2Lav5eOLjhv9Boa4DUBEs4PFtv_atn921mPOjhBPlnvDD6MtbpwMG_g8e4nKAtMFCYnPvDeJ43ajQzHsbSwok5498rFr4nQ1-mFnnWchdpPsfw1MCRZnf3X_7VKhndJirZwsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmn-Gs8SfabA1vKg0xKYcrIErC65d7-qDXFhoZVDTtEIF8J0Ooa47uApzNqxaX766_ozLRvxf0AQGTwcMbncIG3w_tqY6ZOlW5U6umrEsfBMmLQBpE1ZId_UXVbVglY9l4KgxrSooAeH7YuMelAkL4RXxV5q9u5Gxolbm92aj2T9uJd5yX2qIv8giId4Nw0bVrc5h3MmNriu3t34H9g2lAXmhaxKmBaIzUj4lAa9Szr1PMjwu5wLgANaKVX9S8llFoy8nypxwMm5XRsl07ZhmJ69Fn3U9g-SNhz6SJrBl8nvJZSurpEMWrBiSeBNvkZWfjV1o8bTSx6UhnpM50iSTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRAUsWYBxO3xcU8rhyLJZwmQYVvIDn9eGlN8783VlAb2kMVz1f3IY8R5OC8LNCNKnT7NQ7ccMtCDt0AZ_YSxCEp4v-iHfmOraz8LKRRpiDPnPNAlWw3BCLnOf-xd888C8NZS63w__hQSXdrAuaglAXH6d8Oaws9YnvaUhwP7JiNmuH3pukntd-AqrObYJqW7cHnR6mwBPJHbkNTa6wJ8QC33EFMoSR9BerKQYVYxJkBGlv88C6N_F9ptUbD7w6Wd8wsVvSpdDtTBBF3zbbCEOKXdN4HBNoDiwjVfLoUCTYYSZQcZFl1tMC1lmBE6C2-EC-Crr12zJ2e6qpEyqo0GCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9Pin7bGN4GZIstQiRlhz5COBHy7CakR9xvV_G4urSIEoG_j8te2N2cPWs156gdbjpRfaq22yZzXwtSEWKmvIzM55yecM2kZ2WWtd7pQuOqJwTHWgdfTTJVfqInrRXscSfb0x5-3k3Sz6QxRBJ5hxNgghIbd4gOOjyIDIH5yCegfPZMnBvYv-xtuxbkqW69sUHyjFILxShh8urZD1LvYKMs3HpWKcuys8IdjwrxI3mAlCzlVHJ2r7S00UlWDbLKj52y8MVV4zsasnP0Yj6RbOvYqX0X0-Z7fZb4LZuJw2LF6HiDRmBf5Ru-fI_U-Gp4iO8zEaTCdmP0pL47vuetBYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHNFrrMPvBG78ABHbnA8jDaSX5gvG9ItPpIxFbEEjN7T2KfPtcPee3KLXkwuvHfYEbm86Fehzme4NEUGXjXhS_gRuQIFW2oZK7fI2wcgxA2roi-i_qiOPbmLJ3aJjS1EqhWt5cJG4c8yxDutby-Skb45StIVxOwkhe7TrlXBnAIvOrf1pr6musBLOJiuXKm5oMUPBh2RmyPwMyQ0liF2maeS--PKHXyjmUVF00fwq_jJh9VVEEOmNqqhS-bHnt0Rs8HF728Lr1OjQexGUti4Y58w5wIKdLQ5dT4-EZlharPexuxCycfCBJUCtO0OoKsUdcnWeQ0UdxDE0dcrZ4HHhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr-7EUv9ZKldo9l1Ftta01vB1gzXisqSNtOEhbvRb11F-UdU7hXymjWVKTBvIIo9XPzgHvQaQCadwg95zCky6ZsUi_Qgmmgq5U3xpgOL9c0hDpRVCkwgXUhQjhPjgjkidNPxTm2rZVgrX267pHoB0HlK0_Q9tYx1qsO75WXkWhxIUSKaNeQrKSalzt5JPJLFF1uJ2yYL4do59gD6FaMZyuJL941q0Xe3lf2bAhMc6htY7KX9juIN14TWqVUpOjmR_lBz3AQVSINRtLCnDm2xHpnk9wiwxpU5fXzu1nfiPaIvw8pmPr6Ohxk8kAAqdVJTmzbpctA1Jt0j9gs7syZ7HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhkikfN_XVztaKeME1fDZ7V_diXRCTV-ftGiqbgrbuvA5fGR3ijMmEMn7B9X_RqegT8XL4P5Xcqrpr2Z0nvoYr8kQOg1CS4lQSRXh_huOCOx7bfnCTBIHGVFpINfekP4zYPUpurPx_XQ0JJnVwUTk3Vl2hqlFczrH4Kp8ZGgKSIDMqOA-Xb1uzl-HLju-ckx8ue2ZONgKyTyAx5XZaYfo2cy_m8f9CKK-WXPm4FeJFuxwCSpBdUTO5yrMkXHsLZZCoJdnDmNCpeGMiI7Kugc8N1FLCGLUEIxtiJharCZ15RjlJKSbP33A36imzLf11FzW5w6MBTe71OqG912BWT6Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTPRWEhjLW8MymW1VrtBUdbpdX5c4MMOfHhIWy9SaQvgt1De0iEu-Nu8l1CelLay9Ue-Rdo5mxNYP6NqVzekrPb_7OgU8g5LXlBBEBik6fZn9RTVy5aPg-2rBMa1TowRZ4xwEkgc8qU3q4uZwmWqjkxurDUwSSq20kbsycYQu2qiwWPeV3Fr1Oe9em266Z-9hDBlR-CmjWuaFJP7hFOjZRb846wuLHne4f664L-T6mwkMQ7YQ5eqA7c9dpoq784Xmi4NFhG71gP63AEM01KRG4YPFTtFGsVTss9X-N0MctyY_jD76FLTIK6JGaiUzOuI8Zs1QYzKyX9JAudah_VX9g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=UGOjzTdUySeCBAT9el3PQKiBL8MRN5kskdYzGT8V3bEz0ih_nqOjN0vz7svX9mz_H_MaN7yV496KS8c_3IJ3sthKwI0BW4CgOD-0vgPPsJgOa9zkPyqotUxj3YajoDdJNSX8dtDrwlmylEFUl-ylmoYLbdNIQlVVCjHOMFBlz2E6jAGqUTf1WGwvifJ91ezJEjgkwaMQx3k7G4fQ7XsaaKx0dImZ8DW0FP-VJdHdBf4otM9a9YnKrl6g6C7rEQFn8y5_QBlNZh8V48gB1-QuibPy9CIykBz2x9lQSNNoZZZcJ0ehDEMv4OwuHM59pcvc_wIgcthsPXU6ctNhdgQihw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=UGOjzTdUySeCBAT9el3PQKiBL8MRN5kskdYzGT8V3bEz0ih_nqOjN0vz7svX9mz_H_MaN7yV496KS8c_3IJ3sthKwI0BW4CgOD-0vgPPsJgOa9zkPyqotUxj3YajoDdJNSX8dtDrwlmylEFUl-ylmoYLbdNIQlVVCjHOMFBlz2E6jAGqUTf1WGwvifJ91ezJEjgkwaMQx3k7G4fQ7XsaaKx0dImZ8DW0FP-VJdHdBf4otM9a9YnKrl6g6C7rEQFn8y5_QBlNZh8V48gB1-QuibPy9CIykBz2x9lQSNNoZZZcJ0ehDEMv4OwuHM59pcvc_wIgcthsPXU6ctNhdgQihw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1Oi4WAfWnD18QFe39L_HheUAZfQjqyshiQk7Odbcque30xQqndoNpKDu4E5XrF-c7gNTgkW1nNhlEXJxeC2r-CoFySDN5nOJebYeo0FaKqowQSX6_IYWawlcmEpna6AxctGCZTu8udmYIi4tbtLpaSeyhcJDK7qt3o7t1Jk9DBLAR6qTvC9TY74r9ehyzUeOv8mjqoJCNK_nQEWn8Q8m2yhjiQjR81UuB8epxrDjtBWk7IYCVcNvCxIYArJiHOkaqUR33cbYs3WY0kSvfmlCL2B3Wv0qAku23jN_sz4H-MITVvKnYjlFsCiH5k2uR-1WSwIuSRxvWe6qUTxNN3geg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqc1kLatEDEe6T8vfKfdTShLcuSzL41UPpheVlvhkmohgRQ_erI_LruGGLESmbsmYwLigT-Zc0eJt9vuICKnyOWd87KAR3s5U7AwF4MT1ZIfXuNWHBR-nIrBbzBtbB7nBuiDjWWUcHo0GxA52hbnOvGLQnpaCeljGvWM_HKMm4HogsRwd9fFUbecE36AApMuRaqBcxh8n5p-L5J15qkcYZWMBt-rgygc1y-nccMvGjP02k8M_szyNeLCrQAqXQtPm0OhFYM7ssH6ERhM63SJpop2OHNjQBsbtWLYCZLwzqrWUT7kVws663uREOwL5Z-t_YCjonNuud2BTulaeEUQ1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptqigI3OKXrftkM4lHa6vmL5AhrrYjI4-EFxoT3l8rCW6yIkvutDYdh3uGg-qyVV6RfHNyGHLqK_vMzyGiEhbiO5s9VayJUsoGTebVoGmhqpDu6SY8wnNE8bFyxQP4Rup8rK5etqkOtWmjIqfyM1h1zm_1tfCK1LQBqfnQ_P2tsDgXEshcEpSRNcQwGvICdFkIiqQA51whWSpTy2o0xu2xnkKuu4vkbK23BNIMCksWEaNYvwRKrGXb5sPJzUwkxkj89pHloNXHpxGcGTRiLoGeU8xBpH8K3P9AbsLX-gke7bpq7ITX7u4J-FE0pcA9c9W3E2QOC__43pPaB5WxTK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFzNwUwyB3FgWb3pAoHZQyLwi7OREloWOpKAHqx3sF4TdnFSh21ZJQA8FvM74dyld5GaBDcRFQ_XWhxgkk08EQkstgSTDs8ixi2AGJlxwa0KLO1bKwUSLYRSMAfF4QmG5H3vt6dyUWQbFJZ700ITWR0bE9VysgO8MTs4E9vNb3oBZ4h-hrLuqrd61M9a7p1HB2bail05fGQznRx68Nf6J-awnW2zxqiUqcD7zxnAPnL13qOenM2hBfT9-KusBLH081nZRPYORgMRKYm1YdZo6JuFkRs9Ej81ii9BEzB3IkmUcYzBnZbpGjVrNltceXMWk4jgVLiaYxqmPV0sT6gh7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRUSo89FwsYwzhnb9PIsBTWHMZl0t43QW9xouvUSKIRmqylWC-aBilzICFVTV6QQSe_msKhF9DTM_DagjqKQthvZ_Mi7hRjQ7ziXV1DH7HrcxmYXU0w0HLJMMo1ZbveOjr8-8OUV1OZmXgKaDBb1XzkMZcc1mb5XqnCfxo9SnTrjsFgp4dF-9677-L5nMmdVFGk5b3sus6iImg-swTkHO66F1iUUDPq-97sspt2na9dTtDJ07-_tVxEBbvVC-a9IzF7AHVfBiXAKnrq3p47eleXplvgNzW8LWqpN8VGhv3J0W2oBTck-8O6pP9H5K7gc-5DM8XhrGHv2_z_8WHxsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJRxlJtpXA25tMFfy8nB_4Xwux25PPBTmix1si9jifRQrQi0YnVY6npqAzqb6jOkZpBYejZkIWW9C_xrO2HFj12Ss3MX2WDSjNDHT9sWAnYj1sHtiJ_49wRxOH0_fcCLodI_n_FS8Kcdx6Xg0u_5EwhkFHFAelxn--YETgpp_zSRJvuGgkeqv9wgc0oEfdOvvYrUhAbNowO8nnHUzi2uakKO6pkviBghsnP3vV_UTBgfFqZRsGGhrfr732qj-_UQNLmtr_jAnq1V16mFpPRzY036KJDpb3IgHTyShbLQX0IMpZaQZEQ9UBVVxKYnuy2w3pd9W-MNTljWyElKc71vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaeGaQDRLxsn9T4_7-06nd36ZbDHi7mMww7kq5TzLN31SSXSsneN-WfRiOR37InD3NEcu6deNv2ws5AwBr6hYMtRYfE0TuxwWZatyG_xEBGA-p7MkYs0BKJkCiM0J7eHnnAt03qRQ4skctSZsFEO198b9k2l704NrGlSDJmJE3eYqPNVyLdY1L8IR5pmh97OeRnYmsqTLZFqk6Qi3ad2S6QH9VrRQ0Ow51ft0h8DYq632bvoy1BziDBuU4k8qn66adGCBHzGDPKbXiesLS9D_cl8cPKT95B-uNn9cQzL917wLlYus7k5qS1ITlWoSJhF5aF2IvMAbR8a7hDZgBEgsQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=erD--rfDvrCCP-oyxhob3KzuiECYZZ2ZHEfLrlEftEfjosM-wVEJPXvwZ_ex1t_L9CCtywujbMG0KBsbnrekdjxrOnqavXm_TGA6gaB7mImtrXBxMvnUbRDsYG7eLz7lf8I6PxVYqxb4oxuO_4GhpOd7a_wkaT2GnGvUmrGkfvPiAAdwqkeI_5AnBorE3c7BRwLBNkDE2mSqaEs31bhStQf086Z7kUtpnyNVP-kGtu8VYWuFfA4FO-Ddz8I0Jf6fb2pmbohxTThOaXNgG0xiMK7WWwoybDqzNudCuByGvT7-x6TNxI709XRHGPgjP5HUL5EyYx2gRKUgHshVynUbohuHq9ZmtGMv6tlRtm0XPdwoYDi05oHQIQ159xiP6fWk8eV6OpwMmehPMbXqyTJOCHGHKEHoESwD7Ys98Seq_yyEi0lW0wMHsbE-hdUoYjk-x_by-qQWSBSip0sNIOt5Gk_ZRNTVecXB2FQJpMoeXXFgYMLSdQpttFgbaVMpe6YvBTFL_jF6MHdfFnlT7LIe472ZTaSnAGElqAtQVYCBlrAirMjrYLHByMJ_1PzYCDKSkRRv3yfMXDrsLKueKwAUtA_La5QSB8xZgJiVd4UFSRiq50MjaghgPItBw_JE2MJz2h9qaM2UqLIMEuLWpF6SATkXR0EE6BVVjRIgMD4hZ0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=erD--rfDvrCCP-oyxhob3KzuiECYZZ2ZHEfLrlEftEfjosM-wVEJPXvwZ_ex1t_L9CCtywujbMG0KBsbnrekdjxrOnqavXm_TGA6gaB7mImtrXBxMvnUbRDsYG7eLz7lf8I6PxVYqxb4oxuO_4GhpOd7a_wkaT2GnGvUmrGkfvPiAAdwqkeI_5AnBorE3c7BRwLBNkDE2mSqaEs31bhStQf086Z7kUtpnyNVP-kGtu8VYWuFfA4FO-Ddz8I0Jf6fb2pmbohxTThOaXNgG0xiMK7WWwoybDqzNudCuByGvT7-x6TNxI709XRHGPgjP5HUL5EyYx2gRKUgHshVynUbohuHq9ZmtGMv6tlRtm0XPdwoYDi05oHQIQ159xiP6fWk8eV6OpwMmehPMbXqyTJOCHGHKEHoESwD7Ys98Seq_yyEi0lW0wMHsbE-hdUoYjk-x_by-qQWSBSip0sNIOt5Gk_ZRNTVecXB2FQJpMoeXXFgYMLSdQpttFgbaVMpe6YvBTFL_jF6MHdfFnlT7LIe472ZTaSnAGElqAtQVYCBlrAirMjrYLHByMJ_1PzYCDKSkRRv3yfMXDrsLKueKwAUtA_La5QSB8xZgJiVd4UFSRiq50MjaghgPItBw_JE2MJz2h9qaM2UqLIMEuLWpF6SATkXR0EE6BVVjRIgMD4hZ0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFbO5XjjncZgnIKt3QlpY_LHXOw53GreLBUKPgfDEVFt1p48U1K2xBEZ-EYC_m9R5lZ9U-qUW64BXkdn6at6S5YsVqeBEETztiFc1-WKqfTems0F40pnB4ntm6aKW5qVtcWzvh3HblhFoEjMus9k3MB66-7Dnr66VlQ74Ja19dhS0qcSBSApQxkSBPxBgHywfH1SEIUHzRPp69mCMzlRzYedSXX_QUMMSKyVvA-9IPe0nfHAIYzjxWsssh0iimlecTJaInpqvHVcH0l4_p9LDz8muWQeQT1FzE9ghRmJbpc7QlGJ0vAsSaalR7_0fqQMJ37w09gQiBBx8ua41IMfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R18YuiorwLcTxwnsT7tk_qWGIDEamnj_Y3REiVAvAuFTklYx19KxzyQKIYEK4erRIkKV5DxoQKj3wC9jGbfD8OOFCtHSPSpfcMhbE1IR4pw9mjI8FRlHSqb4A4uqkPsZmEW4NvJbkN1Fa-MEAe8H40zHT6aKENn-dlWKWlhuavatHbqaQn5teWhb5FZTezmTFdgJimSBRr0rJAFZxQtEhJtqGU6f0x4ZF88fVNOQqe5TQ1giYXnEBUQ-Fiyw-gZnPZ1ZTrxoeD4nMGIKa_HJwbQvZXoHsulX3eCNEe_1Md2ubXbKwIbReeQMByqgn2lABtdCToyahy35EGMa7zMmEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfXX3DSuLPkzR1eDhnRVLxt_pDCEUj0q6sn5Zp5DOrHsqqRTRAFR4Wh5Ulgr9qplqh-Y3iwQr8qxR0fOQ73nMTIwPWxuFe0poyqR62VMeBirqNrZA069G1Fni9LDO6xQbWr7n00LD-_GUPCSSmIpncrOWHSGld3-ZwCXnPcDhSUQDTcxO5ii4UPb_xeM5TX97HSaBuhaoa0OEDn51EJIPBqMLS8ksUgo6y-SJyF--OkuXfVru4d7UmLIOCQItdsWAOk24EHaGiqA1vpfBw9LbegAzxDbJRKL-QNZL5cObNm0ceKGbHEyt-yeSypCu2ji5BZQRFRsE70duHlFCPOvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_2oVoBLNYZQ-QePhsrhLLs8Ww5UcA-rQsPWEQY-bT00C_VEiFb0b6JFEX0xlNJ-uRXKvs7Au1ylpNChkDBcckJ_FLq2IqCpjaVTeuPURNLC3kwHMGbEsvtGC-yWdgg9D6bTKvRnPgojkB49EMcHd9yFwN0Rp7EXWa210cDnlI4aQPtL7Gt6MCnMe-gWhYs-hPUHPzU9IdW5MKiniW8jG_smnaZW6CSpSUGzpGqTy-AfDvsPlp74OOMR9aEOCFERiMgYzLRPn6rZ8qNnFPp0tPu_wDbo7634JsbtNVOwjRkQ7TdednH2L707lnB8zyQLBm7HqCSW8XENI9UlZT19Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLF8kFyZtgvzk1TYfhBBi1LRJ_6OmvD7jIb3cicEPHYJ_kpB3Y_4F9whqZ3gCDiXeulY2usSx9EDiWqQkbNtULFVrTsxfmNN4q4Wd5DeaemXefjCyqKgBsrhvZzslbTUSJJnoXczAkODEJQAiDwKeb174DrDP4bmy6uILvwTH32rXeke4-_vYW4ewAhifZAjkp5VMk8X7ZSZ2vdDVMg6alepEXyj60SCizcmHpQIRflSjyY3-AeSfHnR2o8pszpnrGBY_rORXJzMp6dFqHOHPMT_xKe3MnlW07UhHbpUR5hNGs-MQmHgvtbBzZhGsPryPbPe1bTEl-tJ9zG-2yRbFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aixgbTXPBrxtrz12V2c0TkJOiH6cRVzTcJQrCp-dIG8k924CCQ19e6hp_wctzmhZis_-TzV2iGNJrNW4CfqDA0u1Uz2vAkAKYAOIjtGZfoPuJB08wa9UWxwSG-8U4Ma72WSRpZe2lFlCX6UG72ShQ7xj-Tyhy2RJDViiHwRLiWK7wjv-q4IJFY9my5WlQQaswhQTlY51FQidGyrYqBGf91U_pa5Hn5pw2FTGwulkEtT9jVyVznwDYnD-YDiozNVwhkwvupaR2wwoIAxsRqwLzr47KTy7qAgBJq7FK5XFFGkk6cXtEu0jeLEAg36qjxlurtzDkA5YzrWWHQm00j_nbE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aixgbTXPBrxtrz12V2c0TkJOiH6cRVzTcJQrCp-dIG8k924CCQ19e6hp_wctzmhZis_-TzV2iGNJrNW4CfqDA0u1Uz2vAkAKYAOIjtGZfoPuJB08wa9UWxwSG-8U4Ma72WSRpZe2lFlCX6UG72ShQ7xj-Tyhy2RJDViiHwRLiWK7wjv-q4IJFY9my5WlQQaswhQTlY51FQidGyrYqBGf91U_pa5Hn5pw2FTGwulkEtT9jVyVznwDYnD-YDiozNVwhkwvupaR2wwoIAxsRqwLzr47KTy7qAgBJq7FK5XFFGkk6cXtEu0jeLEAg36qjxlurtzDkA5YzrWWHQm00j_nbE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5Ukxgy6E175woh9KaGDPZVW1VbtYgQmc54P5Z4QWHiupVEJZdYYMzMaO3E_mqmune9Uz3Jag2zrx-24WMCOCXQ24hR6QI8G2HDL7kPICJW73V2J_5XjVXi4vlEmumASjYDleE4VWCiw3zVPLRn6Vg1G4vNZYa9WjoavYJ2q06ZaLh-DbA7vOSKrKNqdMj4D86g5uAt5NUkCEo76SzPj8nxeISwmoe8XdqPMjo47-yp0VXDOQCkzOUPuPNGqUJTP2kYhWva3HUBvZddebQH61I-INP_Ka0OzGsPvfcBB-3MJ6hNxjnIzavm7JVxIalYME02SrRDZNZ63sDlgFI-frA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUhLAnuGXe2Hdc0Qck7Gvps_yFo_V6GimCxzSZApsNttDQ9p_tvNwQTuCnP5GsNhjXJ0-a9rbumUlFOKK3jFT6Dh0flHVNEcvE3odJ68m8oi9rRsf5KHYiqgMHiRQJztQ5mdh1C2t6h0XTcUzReAsoy4ptnyupf6hFDwUd-HA_tB6W4XwbIe8w7ElPo3Qms_uN44E64-_6jF3yDWYH7h2Be_MxFCF3huYsi0olyYS5sv5rWMOiirNJJ3bTDcofCAo3r-ZvU2HxZ4fzNwXbQveIgxYEjsYpz-QihMdMFd1k5SSeS-puREnkIUrSo8qjBLVeBJr5eMdJFJFi9EXqWWGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4x-67ZRSLa3PJREZhVhLYEK7nShEKS0DDAO20EEZawDddhfUWvYDmD8BPJEN7SXb93p9Aag41fcKs7zZIRwVNMrnlRQqmXZlOzN4BRfKxvnGMF3RRaaLe7t5VqKOmGNUHp8_8cpJeoGdKTYMFi04wq6G6CejgcNfBGgfN2yU_LvmYlHMdoiWreZ5zTPoEfeszNzdfZAkQXxMbfd_JLXzBc0hdj6KWsl5ZZShyK_r-scAoTyGxAtML7zkLnj5yop7xxzIszogXNu2WUoFpQwozBm_vvBJpkdav2SlvIsd6jYOnBrq4FZoKzYmrPtLI8IjN5o-lPI8MKotkIs6-beGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i898b1dERgMjwAkwTm1M_TTvB-gibdsgx8MQXd-FO-fo4UjwV6f73nCW3CBACG2QKZn8v_YjZlHKKWfQAUEBipsXXNiMGcrH88wpZjXKVCB2dibj1wyFHHWWltLmnVyDCzmQtGnyYpXX3f-tDI_ODPbzkmj-qJDA5jmNRhnx_ATqPvQ2RfiaUiUa4BFNGTTLrMrmDc50Fa_r-cB1YM17X0rrAysfzonksmMkTOkQiDEvmNkBkxbcIjyOoKozMHJ-G5asalYig29spuzAZiW6iVR-eL3-zMIfLSXeq2ng3LJ9sKISDbvW3H24KSP-XB_LXRY9FBJ8tTWcqNoaF18R2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/excbCl75Qs0K8GLcpDrBTQtDghgt_S_NjChDB_etXK86fJBCVE9ue_mdeP55AXcBkOJ7gKp1wDXEdM3UyE-QmsoEUyPfVGguiHNX0CQIfX8NtnD_i5wjEpVn6ZMR85xZhbwxfZRMxqURQZL4sFF5OozwnoixZig-r8N_uV2QsXQqnMiNjEwSia99FHKBzwJrd4f3cT4DQZ_1erdPu1B8PqKepNLTIGHnUOO9L7AgvHnr9GOqIRwl5spGxCL-vu1mowN4yDb3bJ-lpZQYjA6Ca9LJnfq6G711KGdxshTArzTU0D4Be4Am1vyNmV6zJTletPh6VKhZbxA8qnS9Vxmygw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEObfKoTqV2gHe-q9ciwaMspUtI6I6Wj9OOmLX0EKjnJRVmXzH_tDc_43EGdC1PZQF6YzOVazXXBdDW_dr1owD9rVTQZkVOUkCdNswGAeFH0nbvIfi6y1VKttM9eOJZgRc0E2ENwQOx_osdkzUQ73RoBBs11jCIiUpFz0I5ohaHoE0m2PfV22ApuGKVoGWoOtzeF1WHk6ujNsr0GK8CCuPuLvdJfqYmoIdFd4uwNuVwHLDXwhcG-lYs5kIDX-HpRImFtjTOHPJAHKAC5m4NjB6ZmFT4VdcNqPaXaS9TMKZHrdCQb8NGPGiq1CIGmnKvDXMkhvPAqgkxRF5lnSOOWcQ.jpg" alt="photo" loading="lazy"/></div>
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
