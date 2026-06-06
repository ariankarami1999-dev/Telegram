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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 22:15:48</div>
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
<div class="tg-footer">👁️ 157 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 302 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 531 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 906 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8lmo6LguONXPQj3XKi5ipBchuZuSjA_V8rC_leMMPlqBjJlbrCexnfGmJYACBvx3Md2y8uQ5UupHjVwUkXY6VGxKCbn3CZdXgUov_MBJJ25F6xNNyuk7BMeZ5TkDuq4ofk_SPnYOPECTM706jGRQ1Jqk_C0lmdbvRUkHE4tFrcMx06p6gPBYXSYcPQUV9REyq_QufPO9eIIJxY_BdqTODhA4iuw8dw3T9VWJBkfRTreWWcN7-fkb440KiOckXbJDawdSsXDaDFIdRAUbaSimWfHsfRXvETiy7EBGEN4Tdn8zCuvFmQebKuz7-QBG14DADdqk-OMr1KQ2nUgCijfWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4pQoOSxFMyfToxEU5V3ETgZcEngApNqogRIUutraw-hTJfYhRqc1v1bjqvJyvo6dF0L2xj4670eUuCrhVPgoMGMNtLtykTuTfVrU36oZvfndAfzQEmUlArEXoPW49DTNPk9f6IvBWqbqhlnCea5CodJSruMMO8TIzUaKR1Tmj8Ob79BIOmDnLg3oGSz9EbuFsA3CrqC6YekYrufDqqhkgx2btltPq1z0tuQZXJd94jT_e53MtxZ6ByzNzf9qmRqkObmyxwWS4RKBEJ_0MyAeBMlT2QjZxS6gOl16b2SxDzFeiupPpQRzfYKkHCZ1FyN4hVGkNMas9-u6FhKClm2Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5T0o3J6xe6LvITPW6YrMv7XJlPPbjQt_6E1AebYb3hLf3ONUxkkXWHIPttRz7NFbMx2cPqkQ2LFOuaL2MUBmVJI_VC7XSsIRMCZpsW-KzCrLLh78fF4mVcg9t_-DZ9jBWJruvBaDKRCKQwp7zWCitEID2iobGkXhQ9iJb1Yg2S6hy5TRe320cgoB3e-4Oe-QK0Fc3IHr4KMsCAfO9s60UX1Ma6TjePncDy6WGav3Xun_cnE4N-Ps-f9crGh7fCjCKMhxh6vCMVca2gy0n1QkcWdjEK7_o9_UBgjnTjFq3qbKUm0IB4Bssb1APU-yIjF5HhoH-oKDLKYQB84GmIOhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIczWx8f8DoQSRlqi9Quj5AF5EQDllFpelXBLhBnSR1EvQrAfnhur2cpo9wC_qfEPxkC6gTKTGegVjbmFweZglLfVhmG2N9n1x8Mtl5TgsVhOw_bb8zTUL6RGwdU6iRxaIPZnYaGdbEZYbayARRYnb-dY-b3L-4XZDoUF4bZTSHP2MH_0AHPOlgt-KB1Iua9PfmFdJtIxDxJYq-Q4QGYnCSeoYv7-x9qgC2MCidNQrwK-obPCGZzoNEpc9N9dfq2SPYgE4tkUdiPIVY52GY6aYQiFOydQyD73IuE6KG0f8nILLxBNzLla0VUddaOH3wXWa4nU9lsEFjGa2FJYdYhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5JciGZ48zEFXzJu8B15fZ3Uvv-h_PU4QzGL1fK6HXSAxRELm9hkelBsV-tkaL26Hqy151vkHJCV2yxdYXPjg4MXu5JVYfY_bXYw8ToUkRHPg-QFE-e7rjW4Tkx2xqK9m_fZ6gXV-34oHkhq1EEoZBdBydPovLi__o-RqxpWpaK33tjbmBr-B5soFyR18danEHulVTG05uDSes20kuNm445zlEuNL97Q9-XCYv_CLa8O4ACTs_5i7E6f59h-DkIR-wZBHLm2NRAlgRQnqEY98AwMEov2hEU-odFDKk9n14qakIYJrNrLlG3O7FCXBCZLpZEupyC9a_m02yHemWwylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZSiKo8FiTExEEpWeM8j_8hmfdd7tPrnYVf-XG7HUVPZFy0COuqkcsyBXqS8i1lm9TBsTCGra1ZSs-TyRT80KuJdYtd-VDnTMbvCXAwWVvdhKMWPLYOJNZBicO6UKEj5nkisTLq1unzN7J4vAJQviGUvuFQD_Z4DYDNknN3fSSyLBsFEJXZm13D484MsD6Qo9TN1dGhUFrQ29SgzPDdLYwOl64cU67rzjcEOR4vlwmwvvCAC73DxTUw0nOaOif5irA5h9NkI25vrcF7wVf2TyOb1uHt9lId5D0R8kciOCZi1mWmJK7cPpUDfFfvtz3J_95lqP8gBnmPDnsJ0I2DZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPzVhyN7bqa1cyFxud0LJFJVeZNXps2eY1iw5wjiOIoCamQYMVD0VQxZNyvj33Id6kVw1H2iEpNC8xWaagaUEzImMM7Twx6hgzUzW5MTpesmnHPNImal1zEmf91dyfUvWgjz9REDPY51uShSuy7MMZt1I1b1opzijBR5tb2AMrF1y1x-EMqvVMcJg6MDaz4wcWOFCy3n0tSjQURHT_e3zALW5M4QyGYLTjuhgH4HJA7APxGWrbQhDrzjFYp9k6vfIZ2ZU-K04InOGWWpGWN2axqnjCgCt5gv6o0cJT2blnZMnH2MvV6H5mOKTOfUonfgOo0_2wpBImhwIDLGOxEkTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4KKs_W_gx0X9axamHmCZJH5nbsBXuP6Sm5X_0vv8reiQGrNmaUmUe3boumWOvP_eDW8vcTwdhURlPKRet42XM55Rp6eSJbmgikEbHdUd41mBozHsDeXWVaPd2KYKMVgNZtg2xwRPTb6Qey2eVMxYKMlY80luk9AVqmP9-t-z-iEphzWLlSZC7lITbNn8NbjnjSQc9Jf53o-Wi2ezxkiTjTUb1PxRCrTBM2hV0ECA6AX2DIL6KQyXkkVYT1TXn9uSQAfsWtbhju0-FAgMpFLspwnFp7brrqbmJcxbGvwkTYJfEBYRRAnwmXwB0m2JgjlyZC3NFyUL9N2Se3CSn8Ptg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=LA2lpOx2rQR04yARAcBVHK5-fUlI4aiiOBoqL9F-Ej1FVIL2izHqyTdnAVRR6eY1IKwg2P9z20NWecxsLubBMfuQpUhyYoGfAphPcPrk4PSkNWEZ252xh0T7k82dJzgeEkn6CgIo5wpJGjYwG3RLmU-JxLMRCiNT-0a6CW5n80VJtmz3LCOn80V6dRs0Jw6RAa3xnHxCd9kWZFK49yxMUnl91foAHs_4jZkmcTkTdYC3Fcu0m7wwoLt7EuyDTjQ2tP-ukrhu7YxBYXj4YVMJhzIkm9WWGwimVwxkM00K3MBd3BCk-snW20bXOYD9YjgJD-9z57FzUcvi-VFLv8HVYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=LA2lpOx2rQR04yARAcBVHK5-fUlI4aiiOBoqL9F-Ej1FVIL2izHqyTdnAVRR6eY1IKwg2P9z20NWecxsLubBMfuQpUhyYoGfAphPcPrk4PSkNWEZ252xh0T7k82dJzgeEkn6CgIo5wpJGjYwG3RLmU-JxLMRCiNT-0a6CW5n80VJtmz3LCOn80V6dRs0Jw6RAa3xnHxCd9kWZFK49yxMUnl91foAHs_4jZkmcTkTdYC3Fcu0m7wwoLt7EuyDTjQ2tP-ukrhu7YxBYXj4YVMJhzIkm9WWGwimVwxkM00K3MBd3BCk-snW20bXOYD9YjgJD-9z57FzUcvi-VFLv8HVYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gbfjx8JAzpBWhGv9NvMoS1vtMCJzXULqP37cZ6IN7WizfMhV8nSZgVsnvhr9_Uop4Zz-eo7b32fao8qWkB3WoyXUzGnnWFgFz34gJVLcF9fC607Wy00tvmf6DfwIp1tfNtfweVsk2fPAfUzqOn6RgYc3GD8uaXeWAR6uAi4wapTTXdzLYl4N-absme5CgHHNnQ4wl1r577zYxBOCGaMvHhj_bKFzO9bHqgceQN-lfo5gMJG6GiBZ4DqqAacDvLRGULgg0tPwmCxKVocDGc0pjN7n_kZD5fqZ1wT_RrU2w8sneSwdWbCkZ1iTPXMqfxgishN7g5n0e1y_pZu9KtdikA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqOCYyW1576SajfajbgxS2giwkspy0x3_UCiDyIH38poLTJvHk30szuWvshMNyf_1k4PGwPNKuGkTDiVI39YfDOcME2KPlqVW2qDUmM0ytgb-Sxu3-mKrE9F09LooIhteE4FKa_ldcgxNwBCd2FsekC0HB_f9_je532RQOM2U0KF7lPi3qs3bBWCG_fMq1bs6pqHktmo56ofguJI0VWU8KxR0R7zGbF9J1nyJv10z4jTtI7W2k9KKGq0jHvmq-qEpHCte6wYhi-8b5ZmYbNnh11dNYkP2DrH2lDaIQ0WTk1b1-xPtcKXet7FTeYhUCrq2pUS2M3Byo6jSz8gL-LFew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDnUQf674haeXGV_tOxk9XXDfe5koaifKLa57DYXa6j8PzVba8purBNJwRrL1KeOU4TKlV7TGO2MIdPi80_qbGrKEKxtWEpKcAhYJt7Jaupl4XjaBcVi22r3VxLaZHUNeen4HG4Ex0LkfYM1tEwr2hXpSHbLgMNd64BrUA3WlRIQmi4Eagz46oNF83Yw2G5WYx-alWVEDKCXZLMypQzZZRWYUMK-KJ-JJq36VJVolUqX_Otzh-jhiT-74JyBiICF5zYYoyROwpaiLOFZNjtxMXRsG3fv9SZjWGINs_eqYvT8jbtVFfwfAbb_8o0kH6OX83_HoyoH28p0dsEDbJoGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfuHgT_9i40xVeZpJq2AEKPXZpohlkGAlq0jx2PFxwSv4oG74lL6iIbhgMkD3Z8nkuvJZ0q1JFp1Vu_1Ea_-WEKLoXUMWbJSVOiSTcVaE8thbjL61kisUulCCPBNip6BUB8qXu1xrxeUwr74UMw5Qs3kHUT0pvkfmyjWRzVeK6UnKYjGCPzs0GsHu7axyXHGGOIUVf5TvY1UrivjNMrA2KsR3fVm5w0W6ChwJ9qS_9hanmr2zxxXVWcdLCVkdT7tK3gC4KTn5zPcgj4q7NnkDm56qqLLgXh8IOU1YmIb0AZGGXLPeTH87gxTBvg2p-mGdlkaNXRJnW5MKQEepvn3wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMVfvAIEKNhTKljIPY3ZCEqr-U6WOtk1l8e_X9LLWWB_ZNsFmT4A_rLfifVJRwis9gW0U6thfAlkeDYhJZGFyH9ix8DcAla3nO2ns4PKiKkCPW4WYT8P0dv6eg99Voqdr3AaPiPP_39bHtMqu-XdOV25SkAUWjRhnQA8YdO2YyvaH7AY_pDS6K0oU7dAZ6Av6WAhR20Tb8AsBodxj1XZI1TyheAELypPYXK6SP5_CbUkT01uhqDiqsZgaR3dMyydKysYrL18DaKTKpZzovX8Wr3ZRPH016RABW_nT-SYuptuqrQmvoCmVDVthhJI18MCCHI-ffFa45whrRLU7WPx-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFWk1KbJOGRVIod3K0QbBsojoHEyZVYRH_qrXVCHfXBs67fUXtT_0uEP0SotM23JpoVtV_z5fDpjObMswZDNjGV3mAYXlzV64l5eB2nrLqWXLIECHPja-4j1wJJUVYRDSKVSYMm0mCaDAyF7e96IYzqwm2piFyqwZnL6EfPgvI2V1o0dw5PzN-GEn05LNi-xrtLQqi3Uq1pJVmnXTWkDGQzJ4lxOnCJQUlqmZ1TJXW9e1IWWVdXLoEvb1DZ660s9w1jG1tvF-dLMnJqY-NqJDZ5bgR3xUwjXyiYj6LZXsy__M1CNNnY5XS0_NlCp83vMP5_f-CcXgzk0L2A29pTBDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOEHP2irWy4XghEEeHCvCmrJL_OjrnyEOySS9wXSTSntrA3d9gR5nsD9wA1EI47SeUBrkl_gD1bG7v3Wy2Qln3FRWvSxruP9IQDhKe8Ww7UP2QuTrQ6oWfd-lB4lRkMPnwNOGwb-xfOJlcVe5ILi8_j7i1e9FIkPXfQlSBejiyxgE0quvl_ESHvukQLlZ3BMPCHnVxmElUnQgmASypb6ODkZEQzWuaE5Wc0pqAB-akBtzQE_mAcHQRH0UjuL61ewzBO0YWrbRLc0A6EJustriJ835-SDLUAWK9AHvK6JzbGF9fBxRVGIBW9nqWmNhQIBlJErbxJuHlmv8CP_p9gjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKiRg17TlWbSN6UuoFVCmefb9cBtYfcdWf9_ES_3qNkTDqq-8kPjv9ENkicO5U4ZKr4E-9QGFt9nglpSJLhAp4pfdMBeu2ECsYp4bUfFIr7xzXFov2ScBjF1hgfEHdlQr6cceSPh7KBJyqPyJM3lQy622zzEGDLDo25_QkMIT1yfBYRnTBePsrRci1qaadX5vsQen53CeReHBBbF9UpvBNIG-KZxVeAsAx102mvM1WfsocQaA9rpbSt7CHCTHu2b5TEsMQacoe5cX12m8Edqei3j_aRqTU0I9tWmRi4e_T4ePlRao5CbAzeyrYrwNAU0EF_ytS_CqymtrS81hoCDfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f76tz3g0zt3lcHOLA9l8AD0aRkyF6eBcgmZxTwGX8b7ZfJHf64hv56oKyjhKeI9gb2_ZgfiZ30PmETIaXNRRDOMauMs2D9KNQta65sOndaYImSvewdeOxc2vkRUPdfBrBZEhiFLr9Nsr70MC5FykY94WCDwCjxxCwIJPGBdh9O8IFnJ3Zu_Y0Tr9-xn2vdL4YcobaPCm4ugvVXV3c_lFJvY3_efYZlffPFymBPBTbEwlujdqStZuZBkYepQSlDnuvpvUl0wIaxChTztJf7o9-m3XGGZf2nvjULmFMuy4kaC4homxhj_SCudP-umfiF-SObDtZg9ZprPtLFsmD9PeZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGLoY04Z2VvIhv2EwRCsiRKEX9p6RR5CKXrJHO3p3x6lyW0hbuyWOsrtO4oYa3ZaSRrd87_oM5X4BfoDVud0bCkZ464gpYcZsWXfySymL6sVwyt-U4jJGk-1uccwQlF8kphiIBgRqeXwKAUKYTmTu5UEgHKv6pPzneaxYyQaZRRkPHMU1xaXWAdMtCYFtI3NNjN7-QCRGqzVCeNHMl_cEudjBQE5uhOBWHaGKfXMDbk-rpmax9nl3rIhLHf1vykenR0jHXWHWXGtwA5_3ZYVsK2UKtCCvrqSsApyF956aMquI76xrqKgksh9JSkcE_1B7vHxEDVNC38j3pCwN94aEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3U4vadP_1Tx01990R-Qv6M26uji3zwoS5mJJb2BYQWaz1iPAeYuyy2qlwiegJgJAhVchXw-z1UO4-29b6wi3RyWN1UBzEI5lxRZ082N7UlCEQi3E_dfxkkg8vuo13QQLGuAEOLrSRxHVNJfeA3VN6XzRSVxBDgLtsoc8trN7q2qtWAvHsRTygqHgd9vOzudpcG543jfWqiqdSv4IVr7vOQrQpOcuYd79YPd8JBUEhOvDBthTuv0MalMWTmZzLDaRxGFMWl6Z-1AM_MI_P1gtyJEfb2L--_tEfH68K33F75mEmXfIT7VSgXJBvXQC67bs4SIourPOoIhtEQePuP1_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H60ZZfZY-Xg-dOUSW_020GwtYnpl9GpuCImlu-xDqPSOAe-7yA7ApNMEZ2tINvcCzLAcIDM4swahXmlT2a1jSEbHoltJK9U9aP5CRUgDnvW1wvAbt--yjWkxMTb-tuXSnr7-QF6XLq-kdhor54f0SEOCeyCZrVHTO75BmC31Xi1Ez1P7b3j0yZ8KaX6LV_KMiJtKBvmVYMnjJq_oV_GXRUkoVXXhUcqI8NVwz95FWMBx3VGR8tpr2rpNFXd8Sg6cWq5_HLe1BaS8OTzI30WLqb94XxBgUyGjjnh-Agp6f7Kvi65aOuDlUzu5YRQu3VciJJfkjd0CAAsS0PvXUNOUAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmRF-atUk7ehF25O57HnFfRLDxGhheVrih0EoruG5wrfBkhuzccrA29yMuzm0K6L2siSvO5yBxpFtWnHOuP1KamobEnNWpKUT6s_RC9Aho_BsLBiRwZ2SU4RWUYP1zhix6XXpvFTqYjdS62-g-eYMLRVu9Ie5uBREWEWla-ImyCVl4o-UFQiEpcaNOwS7B4sZib6xsdRrC18FqUohF1m0fm432Wq6HZDB4nvuxAVT4_KcHQFAudVNB8xp9ILfTuMH8ygG5Ia327bhx1P3XzyB4W6UQyzad2yyv4rEe-FcDpCR7oxpirkvFOMxbmOIyZEbPAzHIFcDlrk-FPoWryzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3tMp6vfQTIXsGvYdRBTBMWw1x873kIJpYaEy8_XZRtyBAjuGtfTEDzms98Nn7bgg8NdmURXHlywTfzzAS4BSbiQEGv10P14skFtsEQqVs4rkHRxXozPLwx3x8eS_ZbGdkbOrkfh79BuJx_FQHVO4lk_5r7jbGL26cvv-OJDuY8rH-rVX0Y9yanivQaphmM-cuN4yNkTHRo77OpdaZltgWZWsr2WQxlq0UoPT9_RLTjJKY8cngG3IBe-K6LWlq6dUPhETvm7MMsU0Q0PGPZxdxAj38j3zEK5dTGhd3eiyCiaSK1tkQCifj7_rWMZZR_Q4_EURxWuosn2_qXMCsRvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utkGpKAFrPLjDJJNquIVT1hvxmZsSobG09spbHcZCt7X-vbwJo_XeWB3BAMaJTzwELmTXLggOgx7eVTGkujmOVlftxxivgnHCF-cDXviw9vOx7q3UvCj6stb6Nhasu3QzUKj6Kk_1LwJk_3qGP9F5vnHpgUl8wYvVbcXem7RegqvNLluEsyfFv-GeeHuKx2cUns1BXiHtQwCXXAWmeyuaIyhiKf-Xbf8eLwpuSyIP2xj9WJ422aMFN4tHb9lx7kVHI23LI3Zlbp0BGgLxhAu_4aYayZ3fKtYbnHg6t-lhiD-xttnglaeexfy27NIWg2_VZCiw9XHtMVzOmOM0itVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msz_OiKJgTgTewictuWpGq_xgzUKqFgy9IeC7aKhwc8W33fBZDvOPMWOPoJONB_8ogUalVj2LFuCVbrLO-a03H_k102_MSX1FjLCJaC7_EB4j3J0pQyhh_DbPTBznSASASTiItx4H4d_dWLgC7lNIVRW3RKp4_IWXZDUEj8hgeQwnhFNCXPu9gZeekbdnQy8sIm8gkhHTQS8jNGZP9DeFjxsNA-yNBVYi46rfzPe1aVc7csWBlyJOiyS2Z27KPEdenPmV5d4aqRrrDM8QUBVhQXrI3trJmRpzm6jwKM8cOitbO9Z2OHDIUuVxY0RnyIf_HN9G9x5PVODYwJO5WQ0_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr-buTnngghVH6npl0khNIOqWJ77wKm-ToJJWRLQs3SdFoCu5eMriB4hYvxNsnYuzYAgAacDoepx4kPRbyljO2Sksin2jw4ZwCJJdHUx3SZldsgTioN7vhUODh5ivfW3sXXdaD_opExmG6H7dmhTN9HZx0575SEu1gzjlciv21qxfp3L966FAn9sMsYJeqKyqzcd0PkwPzooXcWBZd26H5zZKvNo0MvRCApjxuA1PDkHZ5aUFUh7M5PkETVX1Ty6_EB32FtJ4mvW4knfkKYgzGzICQ0wVw2JVXU-kUTkQOSyzsy40RjKm1cxl0Xfl6Pd5Lzg3xEFrHNLxfmPeOMgYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb9UwHLK_IGaNodVq5f7aQkVq82TprswOk9Z668yXpe3cRHvwhUv99x9HHleGvg8g9ua9tZji4iCDK_E43S1NrS3TWbkGJYXQrBFLgdQOmKOLfLJIDn_wMCDBlXRHKKwtvI-Vpmdc4rc7Zf7jXFlzZ7vSN4_5m35mmRV8PgTsD2id6etRSvfRZV52RBIE8Q5391hAWggnIWwar4WLQcv_LFt6MLRgBsHX1rg6azILwAMwzWj2DmsbULRnEQ4kAOULGNYWYd4UoJOMV_WlUih307h0eUWjzjOqaP9XxsIB-yg2hTdUAU7O-Hfhb9JrjCjNktaF-z43_qDxbsQOW8TrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMO6sHDv7jfoTp3OoZEdgsCbwwDqUCTx9q6VN7hgaKiu_d2IzwQ349DPeb5_iaMFpsqVJazwKjjon7bi6vgmW8McWj4yhVhpXwD82b65loii4AfDcxqFG2XiYvwYh9m-S5l9YeoCZ4J_gy0Oc_ZczIiehlB0DLJexclfMfujOzjlrsuCtgTwUp4XC1y5H0B4X8fg3G54MosLJGJIB9_CesVJL9d4z_cxyGewLfAQSpTa83Fu5TE-3bakSlig0yWScwliVO6dXnDBA3m2-QhLhp-5ytAqWy-X2wRTxYnyx9rF_jAN-IYQiHiG8PBJDhroaRtelSjIFk6bCv8U4BdQ_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwKCgxg0MuNpKHHBv3sn6Mj_0PuD0xK7c0d9vI2RzBO1A_V1RThJFWqH8G3m6FDKuLPIQDWIzZbHyx8q4KXNZj_NvXFgfuzLVI_LEbQI2VxtH7aDcI51E_130Fje8XvdKaitfFisqrf-QRlcWDPiATUTLU-lQdeR3AXr94-UuXXlI--hvQMkOBCSUlEtZWsuab8xAhkImdoNm7uS1qEv9LdvMEO6dDagodFZp7UvCT9JcWSCWSg1eo7ZrpjgW-RZsmkXbPV2KTH3BXonyb_EYU85EiL7l1OwhJwULYR3vXz19SCbm--jjewVD2Z1IlKI7CJ2OUAOUzt-inh5-N6izw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su4sqZKidjIaO07JYczBGG_C9nWR1xlvFJ3qA4SYv6AaibcwQmWFIPNYRnHaKfNZfuTMfR65sJE_dOh-uGozceM-loj7r6IYGKjhUkY92c6g5zAYiupKc3ZHsOhvvCO51LR2yMORfCWu70ZhcTCm9x94mb-cffrg6I4efcCBLNLkN9CQAVM3JcObbmTUEVZNra_MUBVBzskUvnKbMrafF53B58fIlroD1sU0gCq2JfJNKOwTKd6NZ2G4flzGCOHfWFF7k4KT_PVp7uJ3UzUcoCb_nUKWaoxqtr9SCzpB21GDu_VvsbtkU95MbIbY0wqAavSG4q7Ug_cu2EgDoEirFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVZC5WG269MjVY4UcqloJT353LuyCO-FhH5Z9ru7bYOP4tY1et4jmeAAbt0a1tNVJ-EwISKueam2GSIMxAmB3OjSajlNvZtkxKcet7kfZWMfT72pRGeGLln0AtoKD-9NPEfY6bT3o3MeSZDvJYNkE4vB6n7Lg0uUWKOqpsZX_TA2_G_YgjiR8-yywWUm98P5rdKZW6z-YLRHlnX5P2Lk9bW7NUBOI_sbyWqa9mSIRfGpgFVIkkFV-CnTXXsBoiSMAllxVRE7k0vO8JrSTZOr_s0eaylKqhnf-hWkpq0Qtt_57NlIXtpTsazG_lStnu4zQ8nj_TE32pQ_QFkYHCyR3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O02rSvbVOJ0-8L9uOTndEq3WwvKwwqktB94vFYNsSRrOVdvEjjZW84pJhWDQv-7riu_rbwbZU-OG0ihnsH1hKTBfzRwQ86k3t4kRr_mlY9j5vWbcsbxlO_4S7QEnutEyjopIXoWMB29-Nc7dA_zS1ldtK7KVZm7UovL-ApwZjigs3J1z3b4sVBLm3fBf_QChIwAxlZBG_x7wbgnt1AIYawDn0LgsdGry8ir-BxH9dwEnlruAHU2NXatk1vYaOH3Au9GujRKv4FvASN6BpRjc6kjNNP4_MZJP94K9CK67H6H7IWj8BLyBSYE3H0CpFO7QW7zWN4mqYLxbiYDnXyvzNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkdmEm9rCbokJHHMkyN7ltqZ2P1E3M1OOD7mWTE_A3ELlXusxNE1o8uLmycXrwmE_BOXpFk6chzpz0qUKBpUEwLQE15Ipqs6Vrrv8tbL5eKm1GZA7-7EgdhyWSsw9UxNXZLkC8PySOe2b-MzCJ8-j21ZLtO9sfw4NdKJLM8fj1LExj2GghVEWjKEuIm7AmdUF3ZNsRUBjOinQHR5XRnS3WVL-rDxQrmlgoX9l37mHFjVg3t28Fese9jVoPNreYPqf_ju7ZYN41v1_jD7iF_KZO9nLv6SaaHAazebqxuTxLEr8A83B0zI-ImWRbk3v74Tb8BeOYWvb4_CosXAjkdHtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvpHut5ackhEF-ADjR7jdlDTn-n-KgjFmH1cL_AZmajSofgAoWbYDVsGLF9va7sIyD7nDJJJys2l0AOp53MV4N1ZlVY-oekTSBgUA8w84TBHPsVrldg_eUX9ZmrBTR98IA5Xdne4jOFB8npebnmGAV_8AOfLxcq74MNUU447fpUpeJ2X-gqtwRbwge9wzVLnqcTmmAAVXmtpgvTS28cu4Ctn82TjYOwDC96TbiiCKZodEtimKOCHJCDxEQCfajFEzHwfXtmVh0zcC-q2SXgy_FulDzk1Jm3DUOcUWA4hgRYbEHuyAxPF69SxD8jQkAfa_-aH2waRPcz65TLsc1ZK3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM-CgOf9QQiGIFV5qg7j29C0fJXt_egxKhnl6NfmpwvKhapTVYtrYfEgLIwQHsxDNpNCl__EOn4tKASC-CBC6ONH0A5meu9b2u-RT1BJ42VbylIo9FgIDYlfUoi4Up5i1xnMFXc1z9BvwHlNXvy4hEUn_uns46bnr_Y4xmycKRK7cOizBm8hirz_xMJQsiQEsnY4ldEhk2-eUGjPPSSQDyI5vPd7bPzdspxLB9Um-DEo93zUwWRpBzGmuu5146Gdy_jUDWp6buxP_JXGcL18OwICVaGeNN3P-x7GHZGPemgtLqn0k8GW7pAnX73sHEffePt_rwWKugAqvyo5FVT71Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OimJa2yf48eLko1-Gn95hnOA6ipmZDwWTjV_0k2I3Vkrjx_K1OU9u-tW0uKZLSZxKtrKLOQNlrVJxVdFXqCWwOEDrMXjmCWRYjzM1CczG5prc5mkdQJrUMyUhcMqnNrytehT3eSxmAImCqlcHNw6r323Eu4st01t2vtd_VFt02qYBXpGO01VwbYnuzG240clWTPz0xT58HwRd7OjG_JpMSmCkktuOUleqR0q9fr24vAbw4OtgicM_rCukXpcmtyJQLVfAE6J24YeY2Xt67_lxF-tnAXHeUpsdPw0_NysDg-fssn22ReV6z-Kgna2bDkK03i04k92HNQ7bI04rIQmJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twYsFC5Cvni3wR2HvQs8O0sSzXvq7CuCMXEBEiS2NJkOGJNTw8mrbE6J20oQ5QRbGZAygRrlnDNisoXfIF383SyLrV_zk2IxLnSnN9v4t2r5CpVcqLXQSjDY8x2T9ek9vxSCyypqA9f5ys-fBZWmDkv367O3Lo4sQnT_sUraf8jDAuBlgpxGtutAI4q0sX94dXofT_Eb9HkCU54YGE2sxYjlSZaYpYgniCv_b1t2qe_wB84gO-bJzj39rJ8sHADI1On3D1FsdhbldMNrpg6gaMQQxDhey_xiTQTVJtASAD9c522Kl5aYmAQPpS3CNWB1XT42wmqsLHdIMWP9ApM84w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsLqTnkT88-Jb158eRnQsMD6usIBXnQp2CsmpMTWIbff6aJH-lOhcI_ATJh2cY0lrLI91iogWN8cjnBFbjQdB08eFR_-1NZMPgPlmnSGkaDXU-71tTuiiQOx6xoFcciotJr4NKJYENEMouTY07BEtgQSHUAdTTg7j-q30iLDNdVfQJLbGqy3jimW1tu85BU_4QH0l4smwhYmZF0GhXp4v4XKm-eLKTEejPY3QGTV3aKGjxZa223txsfkViBLyjK0ppcrKVkSERTefERm6t90YgWyk6XfIMOEgk-zr4PgzEVnnQ5H5b46s0eIfHnvXDXJOjxDQbwJRPpqOfRU7KWo2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GR9WyAbY8ljWIcd_vlmkacTsAaxHrHGwbKGTKRvO6Trh_F8HjGypiBI0pEPKgMU6bOq3ohhVrLjXl5XVisKHP_Y1G1hL5tID3VI2b7xTX7ajvqa0bW02ept6lzQVyzssQIUvKbGB1S1p94YvpNQ_cLCUQtVEW2ILMIusq0tiF5JfSUPkWNZTkRgTOjwPQgzsRA5kIkVVbN4PgUaVKmZspyjCB_XCvV81c25tJKyub4FP1yM9jJ-fvgcfPygRLWJ7ulQifvkDLc9OHQfXyG-UHUXcwKrNRF5zb61UMdULnaGFcqLj21GBNph39y9j89JF53_mlg1gu5r9xh0UPVr_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knC9Y21DJqutZHtwDQEJoI7gWPWHzBXwtxGHRuqF9-VcyQIx9Xjmz4md_EAR8YJ58nYo1KmQg-gCY8f1iaYDJTg98yQmYqFHn-60U49ZSTvyEvSPpSAZFV5of52e_J4gFMlXV98qNUwLWDWQN_eAUC8rKJdbg8oYIOvFjqd63_cBD1Tu4fQQnpiwrfTUNCpnYrr2TIr8T0Krinc58jE4YiSxQ6efycMW0jMh_iJrKV5l7jLcx4K9QU3yTFftkR0gSaStmBNU5noNqwowMFL_sxiqHM2MzjAB2DT5Uotq8VWP2MYgqyk-kDTrx5u-TeaBxJ0VHULh1J0dEh4VEhoesQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0_j4h1WHAhiO6JcUXXojquUah2mNs3PdSa-80RZuz6RmOWh3twTj3TEP9oZCWh5l-KCckwr6uMyvssCIiUVsn0YbEgMCAJn2tIkHBtezs6NjnhQhN4Rh4-6ml54W1Dnx-mISp599UrpikrViQ5GpL02L5DU-U2FCxXciDN_GH-q0Ne8llIrgbDzLlkoLSBbmfA75kX0EZn-Zi9KYdvKEEwu4CKjmlpPFvBw18CDeu_QqsJJfIksnDrXHuFEn-fCoQmcc8c2Bg7yxisQteWdoTNiSfcrptQZMB3cQlmmQWxGQ6ebM4dA7TKLNlNdzzv4nZ6fTDLeejVeZftB8OaksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk3jvSLzyy9qugXyx2TPG4Ijj7OMv43Fub65hnjKAyIN_7fuQSsnVVaKqcxTVGdvGfjKWITHZfgSRQq7-ZFLxe_iKgqb0771whLI30Gxu3H3c6pYmuSE7CWv2BmewLuBGkjcTnx_dEvETP_uy7wLkUv4vtL8qipRvF3yeX9FY_vy727JbWxOExvhli2DdX20Y3B1DJVq7O8eY7o9owKUgE9Ag6XxRrOClmTaHKXiVa0FS-sQwHHxRdcxkPYlc0R6EPdqYktq58CyYrSINrE3xjVO5q6MQAvoNJrItwAfSSuFTNTheYEXhuuASjZ8DC700dpQtSufnVXm2OfCb23s4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKV4m1qHMoBJiRhwJODjwaK4pY25ld_KR3Bjy_Q5bPP9KmiHO10mPmY4dpPiKQyhVuECZLGPlxxWJRA-hZP7fjVACVzunqgIpWm2GaaLdXXggM1de7Ik1iUo9IX9mFvSDXvUCNcQd9wWyLPST2n9jXi5k9kugJQsL7zxVYET34FJFS6LzZ0A2QXbHUl4Ks4trDHwTsaOrWEmmVVa9OQQe1DdXNjfsrV0sVXn2MO-yL89MIYtXD4PFLA8mQJgRLTCR9BLWx1MH9_Puax_XiRjpgA1dTTjOWPynAUhCC8zCACCQarnAq6W9yNRJc7GgVi_emfihjtqDlX0sG-PIeRnyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhSkhpT9L9pWAtMvevfII8sNI3hQuhdq5HlMdkdZYDuN7-GDwvBf3uuGta9w2sAthqvAsV43C4dVU7yUbkMw-iLG9AEXNa6zNNGY_Hqrf_TxR3tQMbvyRrMp51g5V62-u6r_EvsPI7ODDspF1gzpQy2wBBDy0ghK-AGxwyP1fyfaDWApsq4gCNpolzwKOxhj1YVJhrwFwPG3zPsIU4muncHmbeSB-CMk9pKzXTxsAy4EaSGLPLnsd9G3qctup8-9FCY_LRIQ0py9nacVgxJK2Ge-CchDHeAIlVkpG6WgWUemk_YD7bcFXRvxumGcVeELZIlZge6jI0BDqsZ-9dsGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-hncm47XGRD-QSDxHrHgtut13KRXT5YvOoFPHAEKvWHIuWWfsI5RFz-bZbfFmjK9k39VQoCPZdtMfjwa5COT0pGf6T090qPNIB8-YTQFZ5Oh3DNSjV8NW6veds29fHy5k5ILtKV2NkQg5DI_zUWJZcRQvn7irwSGa2WCLrVFbXZKbTvO_tqzMdikVVsa-_eC1M6MJ41HrFb7tRInIpaZnZ519GEQqsPnzrnp7CzlxZBHX5_ryGKnvV-gaSM2YNXpv_dPbqpn-Sv7iR5NOHYCVpLiBGgYsHB6Jcwz9a7erzdBlOKHSy1sI3lZLsKGoCrh4S7adOtfNSbu3EYqHGMKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD2iYd-obCLiwBjheutv0_nH_2hRaDGFOiMxkbb46G0Mawk2B62_fS_0b20TVCQaHXTL5F4rA9Nn0nQb2IKyTsZHfymhHBm_PJ3BR3IPl4icq_BKjtDl-pSpAd0Cjb42CKmQfjgq1hffSjaPb0V_skiLFz-b61C4N4OUSCbtGCCtbvDzM7-lRqCPUbFr3-JIV-_aj1bacOg3BjOrqku5DjA1J_-MNuda6iVecg1eFyiDa7nYqZhM5sICBUkbbJdSePDpVtoIfBmMgQtyA8GwLr-b4CelljcZhkPhW6No1Jme558lV5bm1JckbnZuAXWBtfN5QlGFMVmDXAswBV7WPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz3aiyDDwtuzqEBvjmQyEbKbq_SU2jsczPkcFKBmhHfKBMRrorzj8BpKEQgnvMUU5ayn2H62zaPbpngWUPqJfksKbZ3n5qnkp8IXyqDg4rBphBJvTgxvIB20VrlSin098eS06KxPrQFUAAIqLqRRpw24wPLs2oP5Ml2ERB_fn_TVYF-461mdmGfETa_RKX8y4Ds5cga-NIoRTMq3dipKOTy9cHrsfxXVF4OyCJ_emh8durIakQPBxM76TTICo95M1YT6J1z2xC39W5F7zmn0nf---Pfk-E2WTTiwARs3vMbVBcyEr75SdboS-a40z-Y0QotmBIf7EPwhL3ZABKcDIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC5CLCDYTjljTFrQiQh0uLFCWWziPCL1Nv4dz66HDklramlcl1pjb38lzEPSrWiGlL3GJt6cFJs-2hZ8B1fzwxdR7ksiXlY1vUtxDbrPICah2ADgWjkh3AIOIK4XwraDadDQ2npvL3EydR9iiMwdYg8d7mGQAqR4M_2OIdHZdmp_E7fW3Ybj5m1eef7xjyO6rKQm4Kqf-a-HFT7Mi1xOfL9869scrMmzI-e98vKObZUJGaHEt7da_mZmuMS9iVPyMjl5rX-sd3fnQS8PPeBN7SVCpSaeT8dvfzP60Id7pHfuenKcbR-raUES60h6xjzi_PcCIctwXAUO9tcZiKnnRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbBa9C3Z-Dm5me8LWgvDlW4Qa3PBkvVjpzgWHPJm_1tNSMuW1abK9omE2pFxDfjgaX9-BvYxNtj8qPgrWW74Bb8Lr-pTyWoeukHZG0Cbi6EVh2inAdjeo5B4RVlaiE1zDijAhobfGPCZ_6GPtGROpzL-I680S-0ZqcX6n3QW-oAZPhq6-Itx-G5NH7BJzPF0P7kXh2RppPjQBcL6FHPY1whfc67sQdCRj-42DwC7uhWiL_FQn--CitbgVuu70Z5ReTnUpcWJ7rVCLeK8yqLeMj2o65OO6OaQfJz5Tzn4V_EBpXuhPgzOuEkBWEEJAgHIPM79GvPH016cQ-U3MQsRbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fu_--B8rar1KyLb0EyjfNYeUHf75uqZOe7hmVklJiRcST0B2Arcl0rLoHY7fqkMvAVBg4cgTj0emheex-QJ9IkhQxg_5fjBNMeWFrUwmrmiLJ0_ibuSBGY8WATSKvJAeLdc-WWsxmatO5YosDEUvc9KSgMXXZRyJenmkvgzXMm8v8EXDCtonTPEyAVH6gxpC3P7Z8hiszdN7dVnE8-cXWWb6JkXq7p-Fq8Dl_mDtYciK5WXLwU1acM6BFoSaCetFZiIZLlKoJIrjsSZ3I2tTV6JxMFOt-NVGft2Zqjlno2pQprxSaWPgluF86xov5mb74Dk8OVQlxwpH2ltlshecuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZIb6g_Qw0SiXkXWv7nsRbg4iBj38vqlKFtDHugB1bFWMQ1PqWAbELwk_W5fq9Zef_yBWUlc4T7HIv3Yee6ssiocfSuSAyVYvhaXYN0Ny0gLDqYBTcDA5qZJZF3eXZiTDcO7cT0NC2N870XQKQPg_Pk_cz_7OpKb7waKFXUjm3JJ3xrgvd6TpBcRMZOmByShTle4JQd-ZyftGUYMZdlV5G8kPI1sLZCg5Nya6FKO63w2LPGkXHJP9xdlRMSZhNtMvCxfLoWTOGoem640T-3YfhFm_zhF7mpnjN07kJSOqtkQZ1-5kJu9FietALQj5EV3ProRrn6hYZZBWTDawLROaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8Ra3lpHb4Gt-x21mPleQkZxuyndAwJEhPlGlbRLw6L7MaiOOwaDQ5Hdp9MLn2eT_SSGFozbbKz2PiT_5eokSBAlMzWjGNIe-de86MQ0LeS2MOneKszYvW-OUKbkbPzUIPZY9BFJGmKTSsBpPY4inxkacH2ELCfBJX3vBSgpUxcEzHwfVtvqGLbeYPjcFpj3z9OITkGsV8Q0-fqCzxBi3aIZytV9OhabgO9wj03euRyYxc_DIFfK6LFCWYWLsdkhoMGxU8YJPaMPJjlIAWGt3XnU39dkJThnE0IXeU4wqaduUBnOs_H8UXZ1kXApJCIAGP-xhinO6-X2SL3xlid9dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQKhuEVTFk0ICn9uqpc3X2jb0dNYYMOniaDrmEXF2wTKI08PcZywcMwJEGkFdPP96LLCuaN79UM0CcD_JiW2yyV83h2Ju1rTZJm14MwieVsr4R53qDjRWrK4nXMAHPrA1Ftv4C83Hv08FhkAxpzQkubG-LDAc7W7IM8TcSFZcBeR97626PEwgKM1vYSGoqL-sO_aHTA3mYsAXI7q471oDwO-x2PzJSFCily20lm2JKVjO2hzZq8_1w13J9WVkFJnRRKuqYldYZ-gEXTQOWL1j58-IdAyhNCrhctzApn2c-9dcySDMv0Cmj4yLKzjfLjWiR_Y1rNwr7OPL2a8BSWrdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM1rm6PUqg8K3v4_95QIv9ueWJwbphCdV4ma4TsfQv-7JjvyYDOceqxWFRSnCdoxNr4dPBJc4tirk8p2TeNkbRaYWgwuj_jO7KRJtsPvBooYEWbxvjfNEMsDsKKuBvVAcM4frbAM9WiK9Qt9LPEQ-FbpI38u0zlObEUacjPiYWhHTMk486NQrgp-ElXdIAnySXoS21f_slyS7TMeSlEKaQvle4xzEImKUxTuNdSezP7KQfsBB_TLgCc1KbZYFwZAGOQzVvM1BXZpsrV9_Akct_knTsqwBu0_vWdXLUWStqkaI4PNXTutEupHaxzhkDijZyAYRxeb5Cq9IPj6LQjEhg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=GuQwHRg3UfOG0twfXv2XuOvldd54TtHV9dm_LVtBF6bpGt3rni48qmbwKw234bSi2Qn8uMJPKRWAPG5DCufY5KnmCtpcJXJpx75SV4Bwj8tjgnY6RkgDqBi3vNX7mVlzr6D1J8ZfBnHOjHETg4z106tVJ9X6RxQ9paWMjHdfsWCQK5ci6ASjIMwBwPj50wjBZMEPJttAN6-z_YNaxuZBtXBBDjgNkHdMRAFOOWrc_ypGexxGP-b4Ui4K05huG4c0texPdKO-S7oEmF2Fn-8Gz3M3axShQqY42-TUNoEYauNG3qKyGe2I79CnDGWoI6Mn28i-31nGCLh-CWWGdIHOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=GuQwHRg3UfOG0twfXv2XuOvldd54TtHV9dm_LVtBF6bpGt3rni48qmbwKw234bSi2Qn8uMJPKRWAPG5DCufY5KnmCtpcJXJpx75SV4Bwj8tjgnY6RkgDqBi3vNX7mVlzr6D1J8ZfBnHOjHETg4z106tVJ9X6RxQ9paWMjHdfsWCQK5ci6ASjIMwBwPj50wjBZMEPJttAN6-z_YNaxuZBtXBBDjgNkHdMRAFOOWrc_ypGexxGP-b4Ui4K05huG4c0texPdKO-S7oEmF2Fn-8Gz3M3axShQqY42-TUNoEYauNG3qKyGe2I79CnDGWoI6Mn28i-31nGCLh-CWWGdIHOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8ffGyFRE1rfIqXaN8zs0f1AzKinDzCz8MDJ9OTgHbJx27KB0dv5SxX0ABs5dHM3_XQvmo7tEnbPeJlM27aZ5RZk7rCA7dh7390GVI49tN8wHGxV_9OaCGTJBd5025qFYPY6rLJIwNwPz1ENPTgSjISMODwvPzmeVHssHpU2rojHX2uzMfi_iSUjSi1o8Z0JONqZcCaVsm-5_g8jdiqpy56zxrUPVjvGEfUj-bTmnr-XvXkszFOnEBtFC7uz9QxBOettfKsC32rBklfUl1T4XooZo6FLrzlrR-ij3njFaoLI5rEC7ITyS_MbJJKWkgPpAi1IOzPiuEUfcTCnXKmiDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC-XCVI2xu8UkoR0QUq6G8I1c06nF4afNHNESvcap5BrEMCMzLgExU0j6nwSlY7jpw_bhEUNAzBSuI08JtgH7vVqKRSlUYZZfSKFh1sAp475FTf19cNjWZBmVtSKlGVFxASJT1Khd-nk4gnxtvKVLbIEqChjRFZHMtH6ZIGGdbVXj5sMa4qe22R_UORuqMMZ_m07I2nncDthiQB7NPVD1urdlyq-TetxiZgSSddw76vTTywhC7j9D7zOQd6uKGkxiwA2HiibzG0B90th0BohbynVPwKt6tV050z9VDJLjYpED3o24EbHhFWbErRFnFZkOunpqov35lWfwzhs2aNqbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lq8CZqrCx0PL25oy4GnhhckZbMTGocfRvnpxHLjH0xsIvvuIykNkT9O1ze3YCCAhIsTH7l46RAhPJJdYEzjoveOQS6LinGSSUeaGX3muDIe87NlCzmFnN6TlbwFp4YB22CqTaNxsQP81QB9_FUQbvbgLgZVEiax5aQXOpZbakO0ufgoeqKiJbOXUnF0WFukc3eqQ9wfZKNDuwlPgHbt2ttu4GsKHocNo-c4eqKn74sbepSr38j3JOWckiK8dXwzCzeIiij1jGTxk17F-xELsMCMrzkzWo-_sA_8ubwrinzwVOvjV-sIMx2ECBnhlnA0vpklnce3UwYShQwvMYhsGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od70tSAzwYC3PFEmT6JiGEfFo3cpAK5vPQ5oaa6lzyVHW7UCwZgxSJMSUCH3SRVjQEHPaKzjnTsre1qtmxdy7ko5_JdP5wpjcp5UDvfBDFHhEhKYPCw0TdhOmQWOCeVN1-ylIG7f6Rp8NbvhkdFr_FXUEzsABGKaBx6yw4-HhRe0WRDYvcAWmVuIBAD2h6WvV-QOnbMuUWR3dHMp8XfdhpKMMmm32RYKaSsNpH_GcP0y7sE5jAvKg9eL_lQ8znYb72-o3o3dgxtK2ZfmuRgSzyCz5xzoIq7MEwX20Tq0PMjDzOVC3Kvhi0GR9NkGFhwuGWr-ImmQ7Zbr2eV55RaPpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wv3WPwdrAPyl-s0qw_VevHtiQEwQv8REZf-S3OO6UN0h0bbkhN6jIdAo0SkLjUJmXaiIm2nlGdI9y54LN-115R6aHx8QSiInSDLIfF6Yupg8V8CqOO2y51S_ZN9k7310WmyTYSgNDJDBAjXoq0OPoX8JRGvZsrK_8NtOuXSnL---HkpG6rd20iojmSzW5ewIuDOiS4vVReR_VjTJuQ2_Rgfcuf_kNMoDQ-G4YJWeXXfpkrvMZAPa5EtSm42gnUJm3aufPXpvIPIaGBvnhxpXS66Td2e6TqCguyFqMNP8HvkWDB5xmD_nuKGMI4Pk816gmE0nzrAwdjxWoHzVk7KB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elBbTkucXhf8CtEQo63IM_a4CaJlfa6gTdIo6rh-HmPIO6N0wMeLXMQRRn2VgSWrGg5AaHAYBCy0vBZMi9Uz8pGteksq4fPy4HXOq72NmecC4DYCq8h4vpQzJm1N6Jm0188qZ1UQ-eWPrXBZ_Bh4p2JZdb6YWEbmFsjHe8pzmgkKLr3cLKF9ObSsMcSAFXAlaQg9EkPCCybPpayCJxXXXytb11PJgUO3R6MTc_xnWS0uO09T6lg3DA7diTI5lSB39Iwtow7dlC4cutYzt3RP4fgQWUqDn8kXqT6OHCuOz0a90hnPTFGqmOUAFkWBB2z3Yy-u4iSm3Dj_DIwdJnDvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2a8gIYz4PCjSRLCMMEXSq3DyHC5Jt9uljD55iYAIAsrRIAGHvB-DzDsBUeW-Z5MBSDEkxmNAEzZ_0bswJah1znhqIfuehsjV1le3zZkiixIrAN_F8jp3sy3r0JqJqePApc9Kz1_PyHxahahEEZd9qo628dvMnmb6DaHavtclrh-Cb3vjoiQA97P6M-akCOGBqdtL0mqm-KeF1npztUC45IJB68N6ieX_cMpg4jD6MxsYhDHWSQr5x0r_xZFQmlhoqG14_JyR1B6FfY0x9FloUGEhqO04DWRzTh7Jfz5THU70jNayApaAMj4K265sotVFyUs6S_BxrRaAsuylnuehA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=kWYOahm_ogxSKq8ug_IeV1NcGpDQLRjAhgO1YZ89zEAZ0K7pUVxoEBhY1_D3EvqVOujn3H_wansulbHwT8PDNHkzVTSOkUnlCHDq9CfBnaeXR1EuYBR1x_q2WizLceyqjnfPkywi_kacEoz04HJctmSFwTC-q98QK5h3D3vcGyCD_QvmjiEhjzALEQssYCU77XvBbemyZUs_wGIvFhqFl1cvkDzJkoGz_6C6aq4Mn2LJDIkOrUZJY-yFkLBMQSabivqbEki3IbPlsfJmqMqgraHAbrMT-CN6YwqxxsB7QHyEDhaRTHShT658Rj2xgNxTHJz92dWt6cjRCT-ty6zrzbzGsXM2a-vp3e0gvr4cv7OvNIwAgq6Pm1JZB9EQ-R7pXv-bVC-U3tJtJs58QkRiqMRqnOsaYbUPVWQEuFXcDZu09qkhTU4AWBp74qf6FV_mSAkWiZhmTs-00niO9Sm6VbuxXZPP9UMe62opNcqjmA97ZQUb8LoSiiWi6Md7kiLXymDUvA8e_f06M_m_Ig2e69VFAT1NcCEEHZS185ElDrUECF3kFJENwuxAGanJl9PEhO3tIvp-fBdWnikGOTA9JWqpKxTq0Au9DtXPgHz8sfB7NEDvvoJEYKFr0df6SQ7nguQqYqZDprtIpZo4HMn81hTtzWqohO3iQbYBWXzQpok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=kWYOahm_ogxSKq8ug_IeV1NcGpDQLRjAhgO1YZ89zEAZ0K7pUVxoEBhY1_D3EvqVOujn3H_wansulbHwT8PDNHkzVTSOkUnlCHDq9CfBnaeXR1EuYBR1x_q2WizLceyqjnfPkywi_kacEoz04HJctmSFwTC-q98QK5h3D3vcGyCD_QvmjiEhjzALEQssYCU77XvBbemyZUs_wGIvFhqFl1cvkDzJkoGz_6C6aq4Mn2LJDIkOrUZJY-yFkLBMQSabivqbEki3IbPlsfJmqMqgraHAbrMT-CN6YwqxxsB7QHyEDhaRTHShT658Rj2xgNxTHJz92dWt6cjRCT-ty6zrzbzGsXM2a-vp3e0gvr4cv7OvNIwAgq6Pm1JZB9EQ-R7pXv-bVC-U3tJtJs58QkRiqMRqnOsaYbUPVWQEuFXcDZu09qkhTU4AWBp74qf6FV_mSAkWiZhmTs-00niO9Sm6VbuxXZPP9UMe62opNcqjmA97ZQUb8LoSiiWi6Md7kiLXymDUvA8e_f06M_m_Ig2e69VFAT1NcCEEHZS185ElDrUECF3kFJENwuxAGanJl9PEhO3tIvp-fBdWnikGOTA9JWqpKxTq0Au9DtXPgHz8sfB7NEDvvoJEYKFr0df6SQ7nguQqYqZDprtIpZo4HMn81hTtzWqohO3iQbYBWXzQpok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD4VpEHMMG6X-PE0W5dctmWm4mIWc9y1T2OcBvi68cFXfyeRjJ5b9wM2PKChgHgFOELtEe_W95ckqZt2n2tQdda9GCCXM27W81nhbKdg_x_pJ9yIkrRcBXY3J1ydUa6tyU-LkwYR204DSabVzZuVx6Lvf55189XKJpfWsMgpO9PEKt7iwaTsrBbjqW_Ft24Tx1SjDDS86s8ZDm70P4pGyjokHpm8GEw6U3hNSdXILe_esb4OWlfqvevUkU5nrZQUliFsnClHhSMFM4bI_xf03M5aHmqC29ZfsMnpaCHt-aZ-5ZnOJ3_oetG8OjbtEpRBFBAOT3_0k81fR81J9qmFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_rW4M3EI6UJgFmjcPUkMDuDbufO7KHkkCY-Yqffl-XugJeeqJYag2pMwS2HNlZJ6K0thVjG35l-Pk6vCbJAnw3VIbnOoqoPTaKpFz0lJl4AX1wSTY_lIUqBsDJC3BoJXhg6Z0BEY4Ls3z9yOUFu6J1yHCoAKXTzMZu2cRCmCqnoUEo5Gi1JJ53MO9nCe-KloJH7Z-SNXwOezqUyG09ftSjhTltBbQu_sBJUe6FenjU-dJCAnLnZgNZWOjB-j7VZ0xAI6iKkVvhr_Vdiy3L0z9iIRekCsFWM9PgB8-kQzzfWztjIEDX3Bs8adrWk1raib8pcw0dfO-k9TENF5S662g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/io_0QY4axch5OFKnN0omizlYEKATaVTXKWGoGyzwn-UMNZ-EA9XEiM-HlCkL0d4j8n5ONzd0uWk4kQ44bJzkN0zOiv8OUm7EomVmHC_nYlVAk9MLJqYXf9yLeVaKEfoumk1lEFFKT0QmzZ3GAX1Tlr1uRv8AUNCVMVdJ0YA-2ooASfCphr7AiTYFcGb5PafvrmE8p17wMAPJ0a-HmJM0mo6IwWrQWrimZKPexBGB98dNfdHME2GSUsaqfs-M7skz6bbKwW7tduyHYsJDDKCXJqMkEwbDcIIDOPF-a7CIBZdu2kKP7jnr9pGkpy6bDnL6EkJSr4r7tzWsSO5rMJM92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttK5rdhfpx-asuHaVAY5xA4CJgjlIVhtVQ-EkMRK-Rm7vLsUrYqpQiz_1FZHnILxyZ10pgH2tuv9nLOuwdtOf6VigA1sAjRONkEi0vQX_bhn-oWGGqNJIM2-7_sKZw5kN3UFW944sFxEwZy7XD9U6b8J1t7_bCz6d5vukEqgO_sdtfY3oHxEpFZrSWJkAcLKBoxrZc80LhVd1Wmp1gal1RaimRdkLktHBcL40vuDTvMk6xsD9xTuYZaiGqmjo8M6lRWzM_L888v1AGKPv4Ab-67iuhDnPc8U8Bvt3WsgTT9MXu2cokw7iPTKj4dpi9nZyApzrCV4onqRxeNc6SKSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtX0MyAGJtkpMIO1X0VbhTcq_V6aAn9G1hXDpc1uQPQINPqW8pE80PQvfYtmSE_COs71qKm8IuPqGX7-6xPKY_viPlSNtr__45qFpKj43RCxhzSaNxDZuuvfqgvTiHD4nwBKBjf1B9n3EJGwmJpBdGgigJL9hH7zVw2LmshOsP_lDxRoZ3AfyZhapggbveaTAGVEliHn3O-caHMNN59p_xrPLAKJveMnJJs9eU-F-LAhO6kYq46xBlLgk699rJo7p0Oyp3V-FgS70aZTQZpSDUl8F5kt9GDcpH3MGcvPYDxGRtmmezJ-phJ8aC010JzSyqetsg5aIB-fr9XaZo_axQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QdY9zkOCs40YFHbqi5-oCEhwpA6_Npu1an1JOCiVESG8WfkAoC0sXMpAO8weYbAir033lXGS7TAqQ_xKbqTcgg7i0plKQYXFw9W_zVjCgxuYriX72cxDfdO3Xaq69m1KHAz3JbcvoggcfO8G9H65B1lCaFjXw99SN81v4dPRH_zMCcdXfKZfoG8Uw0o6c7hpE0oMPtz73O1MDjWolf87GB4NQLCWm9_1gjGVBkPPv6OTPNGD9b9q6HES5r_rdKjtc7yanm_KXxy3XwscCcVELO-OhJB4U7zzgI4s0BjMgLMjFMLH_XW5pTaIXfC0XYIvHDlx2Fb7bYVOyg5aL9ex68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QdY9zkOCs40YFHbqi5-oCEhwpA6_Npu1an1JOCiVESG8WfkAoC0sXMpAO8weYbAir033lXGS7TAqQ_xKbqTcgg7i0plKQYXFw9W_zVjCgxuYriX72cxDfdO3Xaq69m1KHAz3JbcvoggcfO8G9H65B1lCaFjXw99SN81v4dPRH_zMCcdXfKZfoG8Uw0o6c7hpE0oMPtz73O1MDjWolf87GB4NQLCWm9_1gjGVBkPPv6OTPNGD9b9q6HES5r_rdKjtc7yanm_KXxy3XwscCcVELO-OhJB4U7zzgI4s0BjMgLMjFMLH_XW5pTaIXfC0XYIvHDlx2Fb7bYVOyg5aL9ex68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqwdom-hCerEG7sZzrSlOpRAI-FhqtrfiL-q1hPzKk_NFeKr0U19hf47aoMucQxJN4AgwY5681WwfwBGRs8Vwh31ZIFGq4EhocuPOLKTeNinbvK3jaG17lCCNQf54_kOb6vHxUSZT5q1wbruIoLQq2v45VeA1one9DCKYeZeyhqNHCCK75pxMHslrRJ2GwOn4r3WcR-LOcsWmHo0VCuWbqSOOmrIqu2cGczgQdrQyQhXPp0h6DmNrTPE0dyurau2smbMsT2CmnJej7m66RGFlGEvvbHTgvPZVF70M4PputkIAtXumUn3CMe0PKbLo71Nn54voKyTv3izxXwe6YWFww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAC3xIYFEeUQp7_OsfA2oCgScRfxYkR5_52DVOMrx_iLhTjMKNjOOg56hUUSQU5oYFn6GzMLTN2IFjOAbo1_nNDS7NLcMw3s-Zd4q6SKyyterDR0js9J2-KHe3AXtbDLnZjUENhnD9eyrKRwxoxkZ7Ahd0OZ2VqGZEtRm5-sqRJaeAseoZUAuXUtE1swUh5DYVCScCxtNTa_5Nky7abjB_4x0NTzGflmwArecfry8cbJoCyo1OQ68nTwnsRqBQR-UWk2zXmh6BE24aMCDBFt54P2uQRkJhsYSQROUwx3kQ5dva7Vy9yMYRzKUavmL4NLJLmRVWejOjfHVmi5hC-fRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwO7_lBl_Wit3iDqHFqFOcqiAQScPgbrC_bFUUWHK9xi32aouPN7_KF577c7Gy3MJHm8Dk6baewNSK8Tc9gbFMMs4lGf2m_19cUPPdbWc2U7724zLNPtnsNIqLaVgkQVGzC3tUzYcLXMtuyJ2GGOA1D5HwtUDejy1h4pSMwX9h-P4MVtqV2KtUCOPQEZKP-ixjSumQxWNgvu0uBO3OQ_3LFEaCfHhh3yOECy6fuPyiq1aGGjC1Eh1KczeVULdvM3UtvbnsIFF6yP6pSEwoP2MLYfkeJOtf8Nplv9DXobWV6XfQNYyYwFX6QotSi8pNJJS4g8skgk_Y6f4Fdllhvf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTVh6EFHhsJtT8HIUIlSkxECYOmAjCQds1tk0pxPin7Diu2Norwp_5KDgBY9NSalBG7sQad-FxQ8Br1nYqp5KUbhD62FVg5gggCApMFj3IEsUjO_KbDvn0EouOZpC9CHJPjifHt-jRQofT1_NZ87U7Pc2uxa7QCf6_rvZRHSEDPv_CituTQbP6sMc6cTQtm8lJPiqpvuRfw0gJ5WPahH-6uQKdqGt08CmL70vuhp35Ry_MRI1t4AfIls21rD26yLe1JV3PwZED9ktFnLsnBgr2j-t-x1DdrNgLbXSdpR6uo6WExTlJi0VQiSAyJE6JoJHnZnKZhV0KsPLbxJ4RpoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlEsgiUjWR7SDj62rAaBX3jMs7Omn9oOALnkMK8_1B5i5x3QSCSk4idDz_KPI6TkU2G6rYquc6D4-KR2hq4T5sbs07W3-FG_wh5aZw72EuUhFyARypT5rQ0TKiODAei3AsVTGEiERF2B68FsvnLTFVuwzCaYmKeVXshI8jqoKILKJuff3C-F0RgZXmppvGF50-S5R748R-MihnrW4kqjVB1BuqTn3cjoK757ZeUacfr93zC7IT8P1_4uSFjNWdDEzBkMjcf2PsdIVOPKUuQdFxJ1az3CocIXk5sSUFpk73yVVgkOJnKx7V031DgiM85zjJnA2lgttxRwUZm_B4WFjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6CGR7yopS44zCr8svveh3_K25h6YLpqEgxkM12WPNx249udQKMh2kZgUUQ-kaLI6NcSouwh87B_YDg5gJgTWrFt1ewbz05UgjJE2XQT7_SV6pMAak29o7MfM-lfGSmxw90S1mwdsNg2brdto_3w4oa_30_xFI_Ii_X2gcKDCfgScBvVrZ0X3bx0AdUw5Mqz5YS9TvMkXKfgW3g7eQSzIJrEVRTZeJG4EW0cxFk0fkQHhu_P4AS1O_zptbfh5JO-OZIg3nf_PouIzq6EqCF0gp7bBOhsR3jadMPJbm4U686JNAVyn0Gd6KeUc53Dw3dWnD4nt4uQ0Lk_ZeWjQZ8OFA.jpg" alt="photo" loading="lazy"/></div>
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
